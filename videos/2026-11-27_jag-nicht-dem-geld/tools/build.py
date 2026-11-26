# Baut index.html, compositions/hud.html, compositions/captions.html aus
# script.json + build/sentences.json + build/captions.json
import json, sys, html
root = sys.argv[1]
sc = json.load(open(f"{root}/script.json"))
sent = {s["id"]: s for s in json.load(open(f"{root}/build/sentences.json"))["saetze"]}
caps = json.load(open(f"{root}/build/captions.json"))

# Beats: Satzanfang/-ende + "key" = Start des ersten farbigen Betrags-Tokens (sonst erstes farbiges Token, sonst Satzanfang)
beats = {}
for s in sc["saetze"]:
    toks = [c for c in caps if c["s"] == s["id"]]
    money = [c for c in toks if c["color"] and ("€" in c["text"] or "%" in c["text"])]
    col = [c for c in toks if c["color"]]
    keyc = (money or col or toks)[0]
    beats[s["beat"]] = {"start": toks[0]["start"], "end": toks[-1]["end"], "key": keyc["start"]}
T = round(caps[-1]["end"] + 0.9, 2)
beats["T"] = T
B = json.dumps(beats)

# Soundeffekte (Pixabay-Lizenz, im HyperFrames-Skill gebündelt)
sfx = []
def add(src, start, dur, vol, media_start=None):
    ms = f' data-media-start="{media_start}"' if media_start is not None else ""
    sfx.append(f'      <audio id="sfx{len(sfx)}" src="assets/sfx/{src}" data-start="{round(max(0,start),3)}" data-duration="{dur}"{ms} data-volume="{vol}" data-track-index="4"></audio>')
K = lambda b: beats[b]["key"]
add("whoosh-short.mp3", 0.15, 0.57, 0.5)
add("whoosh-short.mp3", beats["schatten"]["start"], 0.57, 0.4)
add("pop.mp3", K("meisten"), 0.7, 0.45)
add("chime.mp3", K("reiche"), 2.5, 0.35)
add("impact-bass-2.mp3", beats["twist"]["start"], 2.0, 0.45)
add("pop.mp3", K("insta"), 0.7, 0.5)
add("whoosh-cinematic.mp3", K("milliarde") - 0.1, 2.0, 0.45)
add("impact-bass-1.mp3", K("milliarde") + 1.3, 2.0, 0.5)
add("sparkle.mp3", K("wert"), 1.8, 0.45)
add("riser.mp3", beats["eisberg"]["start"] - 0.2, 2.0, 0.25, media_start=1.5)
add("whoosh-short.mp3", beats["punch"]["start"], 0.57, 0.5)
add("sparkle.mp3", K("punch"), 1.8, 0.4)
add("whoosh-cinematic.mp3", beats["cta"]["start"], 3.0, 0.35)
# Überlappende SFX auf eigene Spur verschieben
ends = {}
out = []
for line in sfx:
    import re
    st = float(re.search(r'data-start="([\d.]+)"', line).group(1)); du = float(re.search(r'data-duration="([\d.]+)"', line).group(1))
    lane = 4
    while ends.get(lane, -1) > st: lane += 1
    ends[lane] = st + du
    out.append(line.replace('data-track-index="4"', f'data-track-index="{lane}"'))

idx = open(f"{root}/tools/index.tpl.html").read()
idx = idx.replace("__D__", str(T)).replace("__BEATS__", B).replace("__SFX__", "\n".join(out))
open(f"{root}/index.html", "w").write(idx)

hud = open(f"{root}/tools/hud.tpl.html").read()
hud = hud.replace("__D__", str(T)).replace("__BEATS__", B).replace("__SRCDUR__", str(round(beats["reiche"]["end"], 2))).replace("__SRC2START__", str(beats["insta"]["start"])).replace("__SRC2DUR__", str(round(beats["wert"]["end"] - beats["insta"]["start"], 2)))
open(f"{root}/compositions/hud.html", "w").write(hud)

# Untertitel: ein Wort zur Zeit
items, tw = [], []
for i, c in enumerate(caps):
    st = max(0.0, c["start"] - 0.03)
    nxt = max(0.0, caps[i + 1]["start"] - 0.03) if i + 1 < len(caps) else c["end"]
    du = round(max(0.08, min(c["end"], nxt) - st), 3)  # nie 0 – ein Clip mit Dauer 0 bleibt sonst bis zum Ende stehen (F28)
    cls = f' {c["color"]}' if c["color"] else ""
    items.append(f'    <div id="cap{i}" class="cap clip" data-start="{round(st,3)}" data-duration="{du}" data-track-index="0"><span id="capt{i}" class="t{cls}">{html.escape(c["text"])}</span></div>')
    tw.append([i, round(st, 3), bool(c["color"])])
cap = f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; pointer-events: none; }}
    .cap {{ position: absolute; left: 120px; width: 660px; top: 1010px; height: 190px; display: flex; align-items: center; justify-content: center; text-align: center; overflow: visible; }}
    .t {{ display: inline-block; font-family: "Montserrat"; font-weight: 900; font-size: 112px; line-height: 1.02; color: #fff;
      -webkit-text-stroke: 7px #000; paint-order: stroke fill; text-shadow: 0 8px 22px rgba(0,0,0,.85); transform-origin: 50% 60%; overflow-wrap: anywhere; }}
    .t.gold {{ color: #ffd23f; text-shadow: 0 0 26px rgba(255,190,0,.95), 0 0 60px rgba(255,150,0,.6), 0 8px 22px rgba(0,0,0,.85); }}
    .t.red {{ color: #ff4545; text-shadow: 0 0 26px rgba(255,40,40,.95), 0 0 60px rgba(255,0,0,.55), 0 8px 22px rgba(0,0,0,.85); }}
  </style>
  <div id="root" data-composition-id="captions" data-width="1080" data-height="1920">
{chr(10).join(items)}
  </div>
  <script>
    (function () {{
      const W = {json.dumps(tw)};
      const fit = window.__hyperframes && window.__hyperframes.fitTextFontSize;
      const tl = gsap.timeline({{ paused: true }});
      for (const [i, st, hot] of W) {{
        const el = document.getElementById("capt" + i);
        const txt = el.textContent;
        let fs = 112;
        if (fit) {{ try {{ fs = Math.min(112, fit(txt, {{ fontFamily: "Montserrat", fontWeight: 900, maxWidth: hot ? 560 : 610, baseFontSize: 112, minFontSize: 56 }}).fontSize); }} catch (e) {{}} }}
        else fs = Math.max(56, Math.min(112, Math.floor(610 / (txt.length * 0.68))));
        el.style.fontSize = fs + "px";
        if (hot) tl.fromTo(el, {{ scale: 0.55, y: 18 }}, {{ scale: 1.08, y: 0, duration: 0.14, ease: "back.out(3)" }}, st).to(el, {{ scale: 1, duration: 0.12, ease: "power2.out" }}, st + 0.14);
        else tl.fromTo(el, {{ scale: 0.8, y: 12 }}, {{ scale: 1, y: 0, duration: 0.1, ease: "back.out(2.5)" }}, st);
      }}
      window.__timelines["captions"] = tl;
    }})();
  </script>
</template>
"""
open(f"{root}/compositions/captions.html", "w").write(cap)
print("T =", T); print(json.dumps(beats, indent=0))
