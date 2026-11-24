# Richtet die Skript-Tokens global am Whisper-Transkript aus (für beliebige Voiceovers, z. B. ElevenLabs).
# Schreibt build/captions.json und build/sentences.json.  Aufruf: python3 -I tools/align_global.py <projekt>
import json, sys, re, difflib
root = sys.argv[1]
sc = json.load(open(f"{root}/script.json"))
tr = json.load(open(f"{root}/assets/transcript.json")); X = tr["words"] if isinstance(tr, dict) else tr
norm = lambda w: re.sub(r"[^a-zäöüß0-9]", "", w.lower())

# Skript-Wörter (gesprochene Form) mit Token-Zuordnung
Wd = []  # (norm, len, sent_idx, tok_idx)
for si, s in enumerate(sc["saetze"]):
    for ti, t in enumerate(s["tokens"]):
        for w in t[1].split(): Wd.append([norm(w), max(1, len(norm(w))), si, ti])
A = [w[0] for w in Wd]; Bn = [norm(x["text"]) for x in X]
ts = [None] * len(Wd)
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, Bn, autojunk=False).get_opcodes():
    if op == "equal":
        for k in range(i2 - i1): ts[i1 + k] = (X[j1 + k]["start"], X[j1 + k]["end"])
    elif op == "replace":
        a, b = X[j1]["start"], X[j2 - 1]["end"]; L = sum(Wd[k][1] for k in range(i1, i2)); x = a
        for k in range(i1, i2):
            d = (b - a) * Wd[k][1] / L; ts[k] = (x, x + d); x += d
# Lücken (nicht erkannte Wörter) interpolieren
for k in range(len(ts)):
    if ts[k] is None:
        prev = next((ts[j][1] for j in range(k - 1, -1, -1) if ts[j]), 0.1)
        nxt = next((ts[j][0] for j in range(k + 1, len(ts)) if ts[j]), prev + 0.4)
        ts[k] = (prev, max(prev + 0.15, min(nxt, prev + 0.4)))
caps, sents = [], []
for si, s in enumerate(sc["saetze"]):
    for ti, t in enumerate(s["tokens"]):
        ks = [k for k, w in enumerate(Wd) if w[2] == si and w[3] == ti]
        caps.append({"s": s["id"], "text": t[0], "color": t[2] if len(t) > 2 else "", "start": round(ts[ks[0]][0], 3), "end": round(ts[ks[-1]][1], 3)})
    mine = [c for c in caps if c["s"] == s["id"]]
    sents.append({"id": s["id"], "start": mine[0]["start"], "end": mine[-1]["end"]})
# Satzgrenzen an echten Sprechpausen einrasten (ffmpeg silencedetect), Wörter im Satz linear mitziehen
import subprocess
voice = sys.argv[2] if len(sys.argv) > 2 else f"{root}/assets/voice.wav"
log = subprocess.run(["ffmpeg", "-hide_banner", "-i", voice, "-af", "silencedetect=noise=-38dB:d=0.12", "-f", "null", "-"], capture_output=True, text=True).stderr
s_st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
s_en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
# Pausen (Lücken zwischen Sprache) als Kandidaten für Satzgrenzen; DP wählt N-1 Lücken in Reihenfolge
gaps = [(e0, s1) for s1, e0 in zip(s_en, s_st) if s1 - e0 >= 0.12 and e0 > 0.05]  # (Stille-Anfang, Stille-Ende)
N = len(sents)
est = [(sents[i]["end"] + sents[i + 1]["start"]) / 2 for i in range(N - 1)]
G = len(gaps)
if G >= N - 1 and N > 1:
    INF = 1e9
    speech_start = (s_en[0] if s_st and s_st[0] < 0.05 and s_en else 0.0)
    speech_end = max(sents[-1]["end"], s_st[-1] if s_st else sents[-1]["end"])
    chars = [sum(len(norm(w)) for t in sc["saetze"][i]["tokens"] for w in t[1].split()) + 3 for i in range(N)]
    rate = (speech_end - speech_start - sum(min(0.8, g[1] - g[0]) for g in gaps) * (N - 1) / max(1, G)) / sum(chars)
    pred = [c * rate for c in chars]
    mid = lambda g: (gaps[g][0] + gaps[g][1]) / 2
    def c(i, gp, g):  # Satz i endet an Lücke g, begann nach Lücke gp (gp=-1: Anfang)
        st = speech_start if gp < 0 else gaps[gp][1]
        return 0.6 * abs(mid(g) - est[i]) + 1.0 * abs((gaps[g][0] - st) - pred[i]) - 0.8 * min(0.8, gaps[g][1] - gaps[g][0])
    dp = [[INF] * G for _ in range(N - 1)]; bk = [[-1] * G for _ in range(N - 1)]
    for g in range(G): dp[0][g] = c(0, -1, g)
    for i in range(1, N - 1):
        for g in range(G):
            for gp in range(g):
                if dp[i - 1][gp] < INF:
                    v = dp[i - 1][gp] + c(i, gp, g)
                    if v < dp[i][g]: dp[i][g], bk[i][g] = v, gp
    lastc = lambda g: abs((speech_end - gaps[g][1]) - pred[N - 1])
    g = min(range(G), key=lambda x: dp[N - 2][x] + lastc(x)); pick = [0] * (N - 1)
    for i in range(N - 2, -1, -1): pick[i] = g; g = bk[i][g]
    speech_start = (s_en[0] if s_st and s_st[0] < 0.05 and s_en else 0.0)
    bounds = [(speech_start, None)]
    for i in range(N - 1):
        bounds[-1] = (bounds[-1][0], gaps[pick[i]][0]); bounds.append((gaps[pick[i]][1], None))
    last_end = max([x for x in s_st if x > bounds[-1][0]] or [sents[-1]["end"]])
    bounds[-1] = (bounds[-1][0], min(last_end, sents[-1]["end"] + 1.0))
    for sn, (a1, b1) in zip(sents, bounds):
        mine = [c for c in caps if c["s"] == sn["id"]]
        a0, b0 = sn["start"], max(sn["end"], sn["start"] + 0.05)
        f = lambda v: round(a1 + (v - a0) * (b1 - a1) / (b0 - a0), 3)
        for c in mine: c["start"], c["end"] = f(c["start"]), f(c["end"])
        sn["start"], sn["end"] = round(a1, 3), round(b1, 3)
for si in range(len(sents) - 1):  # keine Überlappung zwischen Sätzen
    nxt = sents[si + 1]["start"]
    for c in caps:
        if c["s"] == sents[si]["id"]: c["start"] = min(c["start"], nxt - 0.05); c["end"] = min(c["end"], nxt)
for i, c in enumerate(caps):  # Wort bleibt bis zum nächsten stehen (max +0.6 s)
    if i + 1 < len(caps): c["end"] = round(min(caps[i + 1]["start"], c["end"] + 0.6), 3)
    else: c["end"] = round(c["end"] + 1.2, 3)
matched = sum(1 for op in difflib.SequenceMatcher(None, A, Bn, autojunk=False).get_matching_blocks())
json.dump(caps, open(f"{root}/build/captions.json", "w"), ensure_ascii=False, indent=0)
json.dump({"total": caps[-1]["end"], "saetze": sents}, open(f"{root}/build/sentences.json", "w"), ensure_ascii=False, indent=1)
ratio = difflib.SequenceMatcher(None, A, Bn, autojunk=False).ratio()
print(f"{len(caps)} Tokens, Übereinstimmung Skript↔Transkript {ratio:.0%}")
