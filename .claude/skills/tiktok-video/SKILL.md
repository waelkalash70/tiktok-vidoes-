---
name: tiktok-video
description: Erstellt deutschsprachige, faceless TikTok-Videos (9:16) im Stil der Referenzvideos des Users – Ein-Wort-Untertitel, eine Hauptfigur in einer Szene, wörtliche Visualisierung jedes Satzes, Spannungs-Leiste oben. Nutzen, wann immer der User ein neues Video, ein Skript, eine Idee, eine Überarbeitung oder Feedback zu einem Video gibt. Enthält Stilregeln und ein Feedback-Logbuch, das nach jedem Feedback aktualisiert werden MUSS.
---

# TikTok-Video-Skill (Deutsch, faceless)

Du produzierst für einen deutschen TikTok-Creator (Faceless-Account) komplette Kurzvideos
**mit Claude Code + HyperFrames** – Szenen/Animationen als HTML+GSAP, gerendert zu MP4.

> ⭐ **GOLDSTANDARD (vom User als „perfekt, sehr gutes Video“ bestätigt, 2026-11-24):**
> `videos/2026-11-24_brutto-netto/` – jedes neue Video startet als Kopie dieses Projekts und behält
> Aufbau, Look und Qualität bei. Nur Thema, Skript und 3D-Objekte ändern sich. Siehe Abschnitt 1.6.

**Vor jedem Video:** Lies diese Datei komplett, besonders das **Feedback-Logbuch** unten.
Die Regeln im Logbuch haben Vorrang vor den allgemeinen Stilregeln.
Referenzbilder liegen in `referenzen/` – bei Unsicherheit über den Look ansehen.

---

## 1. Stil-DNA (aus den 3 Referenzvideos analysiert)

Referenzen:
- `ref1_roblox_kleinstadt.jpg` – Roblox-Avatar in nächtlicher Kleinstadt, Kamera fährt durch eine Welt.
- `ref2_schlange_cartoon.jpg` + `ref2_detail_leuchtring.jpg` – 2D-Cartoon (Schlange an Säge, „Kernwerte“).
- `ref3_hansetax_3d_gold.jpg` + `ref3_detail_untertitel_rot.jpg` – 3D-Infografik Schwarz/Gold (Unternehmer, zwei Firmen, Nettovermögen-Zähler).

### 1.1 Untertitel (wichtigstes Merkmal)
- **Immer nur EIN Wort** gleichzeitig im Bild, exakt synchron zur Stimme (~2–4 Wörter/Sek.).
- Position: **horizontal mittig, ca. 55–60 % der Bildhöhe** (leicht unter Mitte) – nie im unteren
  Drittel (dort liegt die TikTok-UI) und nicht rechts außen (Like-Leiste).
- Schrift: sehr fett, rund, serifenlos (Montserrat Black / Poppins ExtraBold), ~90–120 px bei 1080 breit.
- Standard: **weiß** mit dunkler Kontur/Schatten.
- **Schlüsselwörter eingefärbt + Glow:** Gold/Gelb für Positives/Geld/Zahlen („Firmen“, „verdient“),
  Rot für Gefahr/Verbote/Feinde („versteckt“, „Finanzamt“). Lautmalerei in GROSSBUCHSTABEN („HUSS!“).
- Kurzer Pop-In (Scale 0.85→1.0 in ~80 ms), kein langes Einblenden.

### 1.2 Bildaufbau
- **Eine Hauptfigur + eine durchgehende Welt.** Keine Stock-Clips, keine harten Themenwechsel.
  Bewegung entsteht durch Kamerafahrten, Zooms, Schwenks innerhalb derselben Szene.
- **Jeder Satz wird wörtlich visualisiert** (Kern des Formats):
  - „winziger Schnitt“ → Leuchtring markiert genau die Wunde.
  - „zwei Firmen“ → zwei Gitter-Türme mit Labels „FIRMA 1“ / „FIRMA 2“.
  - „versteckt“ → Schloss-Icon + Fragezeichen. Geldfluss → goldene Münzen fliegen von A nach B.
- **Fokus-Effekte:** Leuchtring/Highlight-Kreis um das relevante Detail, kurzer Zoom darauf.
- **Partikel/Glow** sparsam aber konstant (Staub, Funken, Münzen, Blutspritzer bei Drama).

### 1.3 Retention-Element oben
- Feste Leiste im oberen Bereich (unter der TikTok-Tab-Leiste, ~8–12 % Höhe), z. B.:
  - kleines Label in Sperrschrift („NETTOVERMÖGEN“) + große **goldene, leuchtende Zahl, die permanent hochzählt**, oder
  - Herzschlag-/EKG-Linie, Countdown, Fortschrittsbalken.
- Muss zum Thema passen und sich während des ganzen Videos verändern.

### 1.4 Look
- Hoher Kontrast, eher **dunkel**: Schwarz + Gold-Neon, Nachtszenen, satte Farben.
- Format **1080×1920, 30 oder 60 fps, H.264 + AAC**, Länge typischerweise 20–60 s.
- Safe-Zones: oben ~150 px (TikTok-Tabs), unten ~420 px (Caption/Musik), rechts ~140 px (Buttons) frei von wichtigen Inhalten.

### 1.5 Skript-Aufbau
1. **Hook (Satz 1, < 2 s):** provokante These / überraschende Behauptung.
   Muster: „Eine Schlange tötet sich selbst. Nicht wegen X, sondern wegen Y.“ /
   „Reiche Unternehmer haben immer zwei Firmen.“
2. **Erklärung Schritt für Schritt**, kurze Sätze, jeder Satz = ein neues Bild.
3. **Wendepunkt / Aha** (Farbwort in Rot oder Gold).
4. **Lehre oder Cliffhanger** („Teil 2 kommt…“), passend für Serien.
- Sprache: **Deutsch**, umgangssprachlich, direkt, keine Füllwörter.
- Caption-Text für TikTok mitliefern (1 Satz Hook + „👀 … Teil 2 kommt“ + 3–5 Hashtags).

---

### 1.6 Bestätigtes Erfolgsrezept (Video 1, vom User gelobt) – IMMER so beibehalten
- **Länge ~35–40 s**, 12–13 kurze Sätze, ein Satz = ein Bild/Kameraziel.
- **Dramaturgie:** Hook mit konkreter Zahl („Du verdienst 4.000 € brutto.“) → Frage an den Zuschauer („…gehört wirklich DIR?“)
  → Schritt-für-Schritt-Abzüge/Steigerungen mit je einer Zahl → Zwischenergebnis (Kamera-Totale) → „Und jetzt kommt's:“
  Twist → Prozent-/Vergleichs-Punchline → Cliffhanger „Teil 2: …“ mit großem goldenem „?“.
- **Bildsprache:** goldene Gitter-Türme = Geldmengen (1 Einheit Höhe = 1.000 €), Geldblöcke fliegen mit Münzen
  in beschriftete Käfige (rote Badges für „Gegner“ wie Finanzamt, goldene für Beträge), Kamera fliegt mit,
  Glanz-Figur (weißer Kopf, blauer Kapsel-Körper) reagiert (schaut dem Geld nach, Fragezeichen, lässt Kopf hängen),
  zweite Figur für den Twist (Chef, schwarz mit Goldkrawatte). Nacht-Skyline, Spiegelboden, Goldstaub.
- **Zähler oben** wechselt Label passend zur Story (DEIN GEHALT → NETTO → DEIN JOB KOSTET DEN CHEF → BEI DIR
  KOMMEN AN → FOLGEN FÜR TEIL 2), zählt animiert, wackelt + blitzt rot bei Abzügen, rote/orange Delta-Zeile darunter.
- **Untertitel** Wort für Wort, Beträge gold, Abzüge/Gegner rot, Pop-In; Annahmen klein als Quellenzeile in den ersten Sekunden.
- **Sound:** Whoosh beim Abflug, Pop bei Landung, Sparkle beim Ergebnis, Riser vor dem Twist, Bass-Schlag bei Twist
  und Punchline, Cinematic-Whoosh beim Cliffhanger. Musik macht der User in TikTok.
- **Lieferumfang:** MP4-Entwurf (Platzhalterstimme) + `VOICEOVER_TEXT.md` (Zahlen ausgeschrieben, TikTok-Beschreibung
  + Hashtags). Finale Version nach ElevenLabs-Datei des Users.
- Zahlen immer real und nachvollziehbar, Annahmen nennen, User bitten, Schätzungen kurz gegenzuprüfen.

## 2. Arbeitsablauf pro Video

1. **Logbuch lesen** (Abschnitt 4) und offene Präferenzen beachten.
2. **Skript** auf Deutsch schreiben (erst rechnen, dann Hook – F2), dann `python3 -I .claude/skills/tiktok-video/werkzeuge/qa_skript.py <projekt>/script.json` (muss „OK“ melden – F1).
3. **Storyboard** als Tabelle: Satz | Zeit | Bild/Animation | Farbwörter | Leiste-Zustand.
4. **Audio:** Voiceover vom User (bevorzugt) → `transcribe --language de` liefert Wort-Timestamps
   (`transcript.json`) → daraus die Ein-Wort-Untertitel-Clips bauen. Ohne User-Audio: HeyGen
   Voice Turbo über `/media-use` (braucht `auth login`). Lokales `tts` (Kokoro) kann **kein Deutsch**.
   Deutsche Platzhalter-Stimme (getestet): `pip install piper-tts`, Stimme laden von
   `https://huggingface.co/rhasspy/piper-voices/resolve/main/de/de_DE/thorsten/high/de_DE-thorsten-high.onnx`
   (+ `.onnx.json`), dann `echo "Text" | python3 -m piper -m de_DE-thorsten-high.onnx -f voice.wav`.
5. **Rendern mit HyperFrames** (siehe Abschnitt 2a): Projekt in `videos/<datum>_<slug>/`,
   Start aus `vorlage/index.html` (1080×1920, Zähler-Leiste, Farb-Untertitel, Pop-In).
   Vor Eigenbau von Effekten (Glow, Partikel, Kamerafahrt, 3D) die Registry durchsuchen (`/hyperframes-registry`).
   Wiederverwendbare Bausteine, die sich bewähren, nach `vorlage/` zurückführen.
6. **Selbst-QA vor Abgabe:** `check --json` (Fehler fixen, `outside_safe_zone` ernst nehmen),
   `snapshot` an jeder Satzgrenze ansehen – Untertitel lesbar? Jeder Satz visualisiert?
   Schlüsselwörter eingefärbt? Leiste bewegt sich? Frame 0 ist schon der Hook (kein Schwarz)?
7. Rendern (`render --quality delivery -o final.mp4`), mit ffprobe prüfen (1080×1920, Länge),
   MP4 + Skript + TikTok-Caption dem User senden, committen & pushen.

## 2a. Technik: HyperFrames in dieser Umgebung

- HyperFrames-Skills liegen in `.claude/skills/` (`hyperframes`, `hyperframes-cli`, `media-use`,
  `hyperframes-registry`, `reverse-any-video`, `style-sampling`). **Vor dem Bauen `/hyperframes` lesen**
  (Render-Vertrag!) und `references/types/vertical.md`.
- CLI immer über den Launcher, Version gepinnt, mit Proxy-Variablen für Node:
  ```bash
  export NODE_USE_ENV_PROXY=1 NODE_EXTRA_CA_CERTS=/root/.ccr/ca-bundle.crt NODE_NO_WARNINGS=1
  HF="node /home/user/tiktok-vidoes-/.claude/skills/hyperframes/scripts/plugin-cli.mjs --cli-version 0.9.91"
  $HF init videos/<slug> --skip-skills    # neues Projekt (danach index.html aus vorlage/ übernehmen)
  $HF check --json | $HF snapshot --at 1,3,5 | $HF render --quality draft -o test.mp4
  $HF transcribe voice.mp3 --language de --json
  ```
- Ohne `NODE_USE_ENV_PROXY=1` scheitern Downloads mit `ENOTFOUND`. Die Cloud-Umgebung
  `tiktok-vidoes-` erlaubt Hugging Face (Whisper-Modelle). Fehlt ein Host → `update_environment`.
- Getestet am 2026-11-24: Render 1080×1920 ok, Whisper-small Deutsch ok (Wort-Timestamps sauber).
- Safe-Zone laut HyperFrames (1080×1920): Inhalt zwischen y 288–1248 px und x 120–888 px
  (unter y 840 nur bis x 780). Zähler-Leiste daher bei ~y 300, Untertitel bei ~y 1040.
- Gebündelte Fonts (ohne @font-face): Montserrat, Poppins, Archivo Black, Outfit, Inter u. a.
- `transcribe` für Deutsch IMMER mit `--model small --language de` (Default `small.en` übersetzt ins Englische!).

## 2c. Bewährte Pipeline „Schwarz-Gold-3D“ (Referenzprojekt: `videos/2026-11-24_brutto-netto/`)
Neues Video = Projektordner kopieren, `script.json` neu schreiben, 3D-Szene in `tools/index.tpl.html` anpassen.
- `script.json`: Sätze mit `beat`-Namen; jedes Token = `[Anzeige, gesprochen, Farbe?]`
  (z. B. `["4.000 €","viertausend Euro","gold"]`) → Untertitel zeigen Ziffern, TTS liest Wörter.
- `tools/tts.py <projekt> <piper.onnx>` → satzweise Piper-Stimme + exakte Satzgrenzen (`build/sentences.json`),
  danach `transcribe` + `tools/align.py` → `build/captions.json`.
- **Fremdes Voiceover (ElevenLabs):** Datei als `assets/voice.wav` (ffmpeg → wav), `transcribe --model small --language de`,
  dann `python3 -I tools/align_global.py <projekt>`: globale difflib-Zuordnung Skript↔Whisper + Satzgrenzen per
  DP auf echte Sprechpausen (silencedetect) mit Satzlängen-Prior. Getestet: alle Satzgrenzen ±0,25 s.
  Whisper-Wortzeiten allein lagen bis 1,4 s daneben → nie ungeprüft übernehmen.
- `tools/build.py <projekt>` erzeugt `index.html` (3D + Audio + SFX), `compositions/hud.html` (Zähler oben),
  `compositions/captions.html` (Ein-Wort-Untertitel). Alle Zeiten kommen aus Beats → neues Audio = nur neu bauen.
- 3D: Three.js 0.170 lokal in `assets/lib/three` (npm pack), Importmap im `<head>`, Modul-Script mit
  `window.__hf.buildReady.world`-Promise **vor** `await document.fonts.load(...)` registrieren, Szene als reine
  Funktion `render(t)` im `hf-seek`-Listener. WebGL läuft hier in Software (SwiftShader) – Snapshots ~15 s.
- Look-Werte, die funktioniert haben: Exposure 0.92, Gold-Emissive 0.16 (höher = weiß ausgebrannt), Bloom
  (0.55, 0.5, Schwelle 0.78), Skyline weit hinten (z ≈ −45) mit gedimmten Fenstern, Spiegelboden (Reflector)
  + 74 % dunkle Abdeckung + Goldraster, Gitterkäfige mit `LineSegments2` (Linienbreite 2–2.6 px).
- Fallstricke: `Object.assign(mesh, {position})` wirft (position ist read-only). 3D-Schilder nicht über y≈4.5
  im Bild (kollidieren mit Zähler oben) → Kamera-Ziel höher legen, damit die Szene im Bild tiefer sitzt.
  Untertitel-Clips dürfen sich nicht überlappen (Ende = Start des nächsten). Kamera-Keyframes können sich
  zeitlich überholen → nach Landungen mit `Math.max` absichern. SFX `riser.mp3`: laut nur bei 1,5–4 s.
- Bundled SFX (Pixabay-Lizenz, frei nutzbar): `.claude/skills/media-use/audio/assets/sfx/`.
- **ElevenLabs-Voiceover einbauen (erprobt bei Video 2, 2026-11-25):** 1) Datei transkribieren und am Text erkennen,
  zu welchem Video sie gehört. 2) Platzhalter sichern (`build/voice_platzhalter.wav`, `build/*_platzhalter.json`).
  3) `ffmpeg -i <el.mp3> -af loudnorm=I=-15:TP=-1.5:LRA=11 -ar 44100 assets/voice.wav` (ElevenLabs war ~5 dB leiser
  als die Platzhalterstimme → ohne Normalisierung übertönen die SFX). 4) `transcribe --model small --language de`,
  `align_global.py`, `build.py`, `check`, `snapshot`, dann `render --quality delivery -o build/final.mp4`.
  Ergebnis Video 2: alle 14 Satzgrenzen lagen exakt auf den Sprechpausen. User-Stimme: „Rene Deutschmann –
  Trustworthy and Calm“ (eleven v4).
- **Neues Video starten (bewährt bei Video 2):** Projekt NICHT mit `cp -r` + `rm -rf` klonen (rm wird blockiert),
  sondern Ordner anlegen und nur `AGENTS.md CLAUDE.md hyperframes.json meta.json package.json tools/ assets/lib assets/sfx`
  kopieren; in `meta.json`/`package.json` Namen ersetzen. `tools/tts.py`: GAP-Tabelle auf neue Beat-Namen anpassen,
  `--length-scale 0.86` ergibt ~40 s. In `build.py` die SFX-Liste pro Video neu setzen, HUD (`hud.tpl.html`) und
  3D-Mitte/`render(t)` in `index.tpl.html` neu schreiben, Rest (Renderer, Boden, Skyline, Staub, Labels, Kamera-System,
  Bloom) unverändert übernehmen.
- **Zwei Objekte nebeneinander (Vergleich) im Hochformat:** Kamera-FOV 48 statt 38, sonst sind Figuren angeschnitten.
  Namensschilder an die Figuren hängen (nicht oben auf Türme → kollidiert mit Zähler).
- Beträge nicht dreifach zeigen (3D-Schild + Untertitel + Zähler) → 3D-Ergebnisschild weglassen.
- Quellenzeile unten max. ~40 Zeichen, `white-space: nowrap`, sonst bricht sie aus der Safe-Zone.
- Zähler, der einen Wert aus der 3D-Szene zeigt, mit derselben Formel/Tabelle wie die 3D-Szene rechnen (sonst springt er).

## 2b. Skript-Tempo aus den Referenzen (Whisper-Transkripte)
- Ref 3 (Hansetax), 9 s: „Reiche Unternehmer haben immer zwei Firmen. Die erste verdient das Geld
  und die zweite versteckt es vor dem Finanzamt. …“ → ~2,6 Wörter/s, These + Auflösung in 8 s.
- Ref 1 (Roblox, EN): „In this town, everybody goes out partying except me. Hush hush hush … You see,
  every single night there's a party somewhere. Pool parties, pizza parties, even a birthday party
  for the mayor's goldfish.“ → Aufzählung mit absurder Steigerung am Ende = Humor-Beat.
- Ref 2 (Schlange): „Schlangen kriechen über eine Säge und schneiden sich. Nur ein winziger Schnitt.
  Doch die Schlange denkt, sie wird angegriffen. Also beißt sie in die Säge und schneidet sich das Maul …“
  → Lehrgeschichte/Metapher, jeder Satz eine Eskalationsstufe.

---

## 3. Selbstverbesserung (PFLICHT)

Wenn der User Feedback gibt – positiv oder negativ:
1. Feedback in **eine konkrete, überprüfbare Regel** übersetzen
   (schlecht: „Video war gut“; gut: „Zähler-Leiste mit Euro-Betrag kam sehr gut an → bei Finanz-Themen immer verwenden“).
2. Regel im **Feedback-Logbuch** unten eintragen (Datum, Video, Feedback, abgeleitete Regel).
3. Widerspricht sie einer bestehenden Regel → alte Regel anpassen/streichen, nicht doppelt führen.
4. Wenn eine Regel mehrfach bestätigt wurde → in die Stil-DNA (Abschnitt 1) übernehmen.
5. Änderung an dieser Datei committen und pushen (Container ist flüchtig – nur Gepushtes bleibt).

**Auch aus eigenen Fehlern lernen (User-Wunsch, 2026-11-25 – PFLICHT):** Nach JEDER Aufgabe kurz prüfen:
Was ging schief, was hat Zeit gekostet, was hätte der User fast falsch bekommen? Jeden solchen Fehler unten im
**Fehler-Logbuch (3a)** eintragen – mit Ursache und einer Gegenmaßnahme, die ihn künftig verhindert. Wo möglich,
die Gegenmaßnahme **automatisieren** (Prüfskript, Vorlage, Checkliste) statt sich nur vorzunehmen, aufzupassen.

### 3a. Fehler-Logbuch (Fehler → Ursache → Gegenmaßnahme)
| # | Fehler | Ursache | Gegenmaßnahme (verbindlich) |
|---|---|---|---|
| F1 | Gesprochen „neuntausend“ statt „viertausendneunhundert“ (Video 1) | Zahlen von Hand ausgeschrieben | **`werkzeuge/qa_skript.py script.json` vor jeder TTS ausführen** – prüft Ziffern ↔ ausgeschriebene Zahl, %/Prozent, Länge (4,0 Silben/s). Fängt F1 nachweislich. |
| F2 | Hook „100 €/Monat → Millionär“ fast verwendet, stimmte nicht (nur ~262.000 €) | Viraler Hook vor der Rechnung | **Erst rechnen, dann Hook schreiben.** Jede Zahl mit Skript nachrechnen; Annahmen im Video + in `script.json` nennen. |
| F3 | Lohnsteuer in Video 1 nur geschätzt | Kein offizieller Rechner offline | Steuer-/Rechtszahlen per WebSearch gegen offizielle Quelle (BMF-Rechner) prüfen oder dem User klar zum Gegencheck markieren. |
| F4 | 3D-Szene schwarz: `Object.assign(mesh,{position})` | position ist read-only | Positionen nur per `.position.set()`; bei schwarzem Bild zuerst Playwright-Konsole lesen (`pageerror`). |
| F5 | Gold weiß ausgebrannt, Fenster zu hell | Emissive/Bloom zu hoch | Werte aus 2c übernehmen (Emissive 0.16, Bloom 0.55/0.5/0.78, Exposure 0.92). |
| F6 | 3D-Schilder überdecken den Zähler oben; Figuren angeschnitten | Kamera-Ziel zu tief, FOV zu eng | Kamera-Ziel höher legen; bei 2 Objekten FOV 48; Namensschilder an Figuren; Snapshot-Kontaktbogen VOR dem Render. |
| F7 | Zwei Untertitel gleichzeitig sichtbar | Clip-Ende > Start des nächsten | In `build.py` Ende = min(Ende, nächster Start) – ist eingebaut, nicht entfernen. |
| F8 | Kamera sprang (Keyframes überholten sich zeitlich) | Feste Zeiten + dynamische Landungen | Keyframe-Zeiten mit `Math.max(...)` an vorherige Ereignisse koppeln. |
| F9 | Zähler zeigte kurz „0 €“ / falsche Farbe (Array statt CSS-Farbe) | Eigene Formel statt Szenen-Tabelle; Typfehler | Zähler mit derselben Tabelle wie die 3D-Szene; Farben immer als CSS-String. |
| F10 | Riser-SFX stumm | Stille Stelle der Datei gewählt | Vor Nutzung Lautheit je Sekunde messen (`volumedetect` mit `-ss`). Riser: 1,5–4 s. |
| F11 | Quellenzeile brach um → außerhalb Safe-Zone | Zu langer Text | ≤ 40 Zeichen, `nowrap`; `check --json` muss ohne `outside_safe_zone` sein (außer kurzem Pop-In). |
| F12 | Whisper-Wortzeiten bis 1,4 s falsch | Whisper-small ungenau | Immer `align_global.py` (DP auf Sprechpausen) – nie rohe Whisper-Zeiten. |
| F13 | ElevenLabs 5 dB leiser → SFX zu laut | Unterschiedliche Pegel | Fremde Stimme immer `loudnorm=I=-15:TP=-1.5`. |
| F14 | Render-Zwischendateien committet | `build/work-*` nicht ignoriert | `.gitignore` enthält `videos/*/build/work-*/`; vor Commit `git status` lesen. |
| F15 | `cp -r` + `rm -rf` zum Projekt-Klonen blockiert | Sicherheitsprüfung für rm mit Wildcards | Nur benötigte Dateien kopieren (siehe 2c), nie mit rm aufräumen. |
| F16 | Profilbild: Fallback-Serifenschrift, grauer Boden, Kopf überstrahlt | Font per DOM-Injection zu früh; glänzender Boden | Fonts per `FontFace`-API im Init-Script; Boden `MeshBasicMaterial` dunkel; Kopf grauweiß 0xc9cbd2; Rund-Vorschau prüfen. |
| F17 | GitHub-Push 403 (lange Fehlersuche) | Claude-App nicht auf Repo + claude.ai nicht neu verknüpft | Sofort beide Schritte nennen: App installieren UND `claude.ai/customize/connectors?auth_start=github&auth_start_force=1`. |

### 3b. Checkliste vor jeder Abgabe (aus 3a abgeleitet)
1. `qa_skript.py` ohne FEHLER · 2. Zahlen nachgerechnet/Quelle geprüft · 3. `check --json`: keine Fehler, kein
`outside_safe_zone` · 4. Snapshot-Kontaktbogen an jeder Satzgrenze angesehen (Text lesbar, nichts verdeckt, Zähler
plausibel) · 5. Nach Render: ffprobe (1080×1920, Länge), `volumedetect` (mean ≈ −15 dB), Kontaktbogen aus dem MP4 ·
6. `git status` sauber, gepusht · 7. Neue Fehler in 3a eintragen.

---

## 4. Feedback-Logbuch

### Feste Präferenzen des Users
- Videos immer auf **Deutsch**.
- Videos werden mit **Claude Code** (programmatisch) erstellt – Render-Framework: **HyperFrames** (vom User gewünscht).
- Visualisierung soll **sehr nah an den Referenzen** sein.
- Nische: **„Geld-Geheimnisse“** (Gehalt, Steuern, wie Reiche denken, Konsum-Psychologie) – von Claude vorgeschlagen, User hat zugestimmt.
- Themen-Backlog: Milliardäre ohne Gehalt, Lottogewinner pleite, Supermarkt-Psychologie, 72er-Regel, Brutto-Netto Teil 2 (wo das Geld landet).
- **Leitstil: Schwarz-Gold-3D-Infografik (Ref 3, Hansetax)** – vom User gewählt 2026-11-24.
- **Voiceover:** User macht das finale Voiceover selbst mit **ElevenLabs**. Claude baut das Video mit einer
  Platzhalter-Stimme (Piper `de_DE-thorsten-high`, lokal, via Hugging Face) und timt Untertitel/Animationen
  danach neu auf die ElevenLabs-Datei (`transcribe --language de`).
- HyperFrames-Nutzung inkl. Nutzungsmeldung (Telemetrie): **erlaubt**.
- User kommuniziert auf **Deutsch** – immer auf Deutsch antworten, Schritt-für-Schritt-Anleitungen mögen.

### Stand bei Übergabe (2026-11-24, erste Sitzung)
- Erledigt: Referenzanalyse (3 Videos), dieser Skill, HyperFrames-Skills installiert und getestet
  (Render 1080×1920 ok, deutsche Whisper-Transkription ok), Vorlage `vorlage/index.html`.
- Cloud-Umgebung **`tiktok-vidoes-`** existiert (erlaubt Hugging Face für Whisper). Neue Sessions darin starten.
- Die Original-Referenzvideos sind NICHT im Repo – nur Frame-Raster in `referenzen/`. Bei Bedarf User
  bitten, sie erneut hochzuladen.
- **Offene Fragen an den User** (beim nächsten Start klären, Antworten hier eintragen):
  1. (alle beantwortet)
- Video 1 „Brutto vs. Netto (Teil 1)“: Entwurf mit Platzhalterstimme fertig (39 s). Wartet auf Feedback +
  ElevenLabs-Voiceover des Users → dann `align_global.py` + `build.py` + `render --quality delivery`.
- Video 2 „Zinseszins: Anna vs. Ben (Teil 1)“ (`videos/2026-11-25_zinseszins/`): **FINAL geliefert** mit ElevenLabs-Stimme
  (43,6 s, delivery-Qualität, `zinseszins_FINAL_elevenlabs.mp4`). Video 1 wartet noch auf ElevenLabs-Datei.
- GitHub: Push auf `waelkalash70/tiktok-vidoes-` funktioniert (seit 2026-11-24). Lösung bei 403 war:
  Claude GitHub App auf das Repo installieren UND auf claude.ai neu verknüpfen
  (`https://claude.ai/customize/connectors?auth_start=github&auth_start_force=1`).

### Einträge
| Datum | Video | Feedback | Abgeleitete Regel |
|---|---|---|---|
| 2026-11-24 | – (Setup) | Skill angelegt nach Analyse von 3 Referenzen | Stil-DNA siehe Abschnitt 1 |
| 2026-11-24 | – (Setup) | User will HyperFrames (HeyGen) als Werkzeug | Alle Videos mit HyperFrames bauen, siehe 2a |
| 2026-11-24 | Video 1 „Brutto vs. Netto“ (Entwurf) | „Perfekt, sehr gutes Video – mach weiter solche Arbeit für die nächsten Chats“ | Video 1 = Goldstandard; Erfolgsrezept in 1.6 festgeschrieben; neue Videos als Kopie dieses Projekts starten |
| 2026-11-25 | Video 2 + Profilbild | „Vergiss nicht, dich zu verbessern, indem du aus all deinen Fehlern lernst“ | Fehler-Logbuch 3a + Abgabe-Checkliste 3b eingeführt; QA-Skript automatisiert die Zahlenprüfung; nach jeder Aufgabe neue Fehler eintragen |
