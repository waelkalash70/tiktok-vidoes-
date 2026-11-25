# Prüft script.json vor TTS/Render auf typische Fehler (aus dem Fehler-Logbuch abgeleitet).
# Aufruf: python3 -I qa_skript.py <projekt>/script.json
import json, re, sys

E = ["", "ein", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf",
     "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn"]
Z = ["", "", "zwanzig", "dreißig", "vierzig", "fünfzig", "sechzig", "siebzig", "achtzig", "neunzig"]
def unter100(n):
    if n < 20: return E[n]
    z, e = divmod(n, 10)
    return (E[e] + "und" if e else "") + Z[z]
def unter1000(n):
    h, r = divmod(n, 100)
    return (E[h] + "hundert" if h else "") + unter100(r)
def wort(n):
    if n == 0: return "null"
    t, r = divmod(n, 1000)
    s = (unter1000(t) + "tausend" if t else "") + unter1000(r)
    return s
def norm(s): return re.sub(r"[^a-zäöüß]", "", s.lower())

sc = json.load(open(sys.argv[1]))
fehler, warn = [], []
for s in sc["saetze"]:
    for tok in s["tokens"]:
        anz, gespr = tok[0], tok[1]
        for zahl in re.findall(r"\d[\d.]*", anz):
            n = int(zahl.replace(".", ""))
            w = wort(n)
            alt = {w, w.replace("einhundert", "hundert").replace("eintausend", "tausend"), w.replace("eins", "ein")}
            if n == 1: alt |= {"eins", "einem", "einen", "eine"}
            if not any(a in norm(gespr) for a in alt) and zahl not in gespr:
                fehler.append(f"{s['id']}: Anzeige „{anz}“ ≠ gesprochen „{gespr}“ (erwartet: {w})")
        if "%" in anz and "prozent" not in norm(gespr): fehler.append(f"{s['id']}: „{anz}“ – „Prozent“ fehlt im gesprochenen Text")
        if "€" in anz and "euro" not in norm(gespr) and not re.search(r"\d", gespr):
            warn.append(f"{s['id']}: „{anz}“ – „Euro“ wird nicht gesprochen (ok, wenn gewollt)")
    farben = [t[2] for t in s["tokens"] if len(t) > 2]
    if any(f not in ("gold", "red") for f in farben): fehler.append(f"{s['id']}: unbekannte Farbe {farben}")
text = " ".join(t[1] for s in sc["saetze"] for t in s["tokens"])
silben = len(re.findall(r"[aeiouäöüy]+", text.lower()))
dauer = silben / 4.0  # kalibriert an Video 1 + 2 (Piper und ElevenLabs): 4,0 Silben/s inkl. Pausen
print(f"{len(sc['saetze'])} Sätze, {silben} Silben → geschätzt {dauer:.0f} s (Ziel 35–42 s)")
if not 33 <= dauer <= 44: warn.append(f"Länge {dauer:.0f} s liegt außerhalb des bewährten Bereichs")
for w in warn: print("WARNUNG", w)
for f in fehler: print("FEHLER ", f)
print("OK – keine Fehler." if not fehler else f"{len(fehler)} Fehler gefunden!")
sys.exit(1 if fehler else 0)
