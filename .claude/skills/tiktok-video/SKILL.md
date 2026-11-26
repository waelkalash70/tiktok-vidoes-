---
name: tiktok-video
description: Erstellt deutschsprachige, faceless TikTok-Videos (9:16) im Stil der Referenzvideos des Users – Ein-Wort-Untertitel, eine Hauptfigur in einer Szene, wörtliche Visualisierung jedes Satzes, Spannungs-Leiste oben. Nutzen, wann immer der User ein neues Video, ein Skript, eine Idee, eine Überarbeitung oder Feedback zu einem Video gibt. Enthält Stilregeln und ein Feedback-Logbuch, das nach jedem Feedback aktualisiert werden MUSS.
---

# TikTok-Video-Skill (Deutsch, faceless)

Du produzierst für einen deutschen TikTok-Creator (Faceless-Account) komplette Kurzvideos
**mit Claude Code + HyperFrames** – Szenen/Animationen als HTML+GSAP, gerendert zu MP4.

> 🔥 **BESTES VIDEO BISHER (geht viral, User: „gefällt mir richtig richtig gut“, 2026-11-26):**
> `videos/2026-11-25_gta6/` – „GTA 6: 44.000 $ pro Sekunde“. Rezept in Abschnitt 1.9 – bei Themenwahl IMMER zuerst prüfen.
>
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

### 1.7 Hook- und Retention-Regeln (User-Wunsch 2026-11-25: „richtig spannend, starke Hooks“)
- **Themen-Filter:** Nur Themen mit (a) offener Frage, die erst am Ende aufgelöst wird, (b) einer kaum glaubbaren,
  aber belegbaren Zahl, (c) sichtbarem Spektakel im Gold-Stil (Zähler rast, Turm explodiert/schmilzt).
- **Hook (erste 2 s):** direkt „du“ + Entscheidung/Wette oder Schock-Zahl. Muster: „Würdest du X nehmen – oder Y?“,
  „Dieser Mann hat für A bezahlt – heute wäre es B wert.“, „Du kaufst X. Am Ende zahlst du so viel.“
- **Re-Hooks alle ~8 s:** Fake-out („Tag 20: erst 5.242 €. Die Million sieht gut aus, oder?“), „Und jetzt wird's
  verrückt …“, „Aber das ist nicht das Schlimmste.“ Auflösung der Hook-Frage erst in den letzten ~8 s.
- **Kommentar-Köder:** Frage, bei der sich jeder positioniert („Ich hätte die Million genommen“).
- Themen-Pipeline (geprüft/zu prüfen): Cent-Wette (0,01 € × 2^29 = 5.368.709,12 € an Tag 30; Tag 20 = 5.242,88 €;
  Tag 27 = 671.088,64 €; Tag 28 = 1.342.177,28 €), Bitcoin-Pizza 2010 (10.000 BTC – Kurs am Produktionstag prüfen),
  Ratenkauf-Falle (reale DE-Zinssätze belegen), danach Inflation, Milliardäre ohne Gehalt, Brutto-Netto Teil 2.

### 1.7b KONTROVERSER HOOK – Pflicht ab Video 6 (User-Wunsch 2026-11-26)
Der erste Satz (< 3 s) muss provozieren, polarisieren oder den Zuschauer direkt herausfordern – damit er
widersprechen, sich rechtfertigen oder sein Wissen prüfen will und dranbleibt.
**Hook-Formeln (immer mindestens eine):**
1. **Direkter Vorwurf an „dich“:** „Du wirst gerade abgezockt – und merkst es nicht.“
2. **Unbequeme Wahrheit / Mehrheitsmeinung kippen:** „Die meisten glauben X. Sie liegen falsch.“
3. **Provokante Frage mit Entscheidung:** „Würdest du X nehmen – oder Y? Die meisten wählen falsch.“
4. **Unpopular Opinion:** „Unpopuläre Meinung: Y ist eine Falle.“
5. **Persönliche Herausforderung:** „Wenn du X machst, verschenkst du jedes Jahr Y €.“
6. **Schuldfrage / Feindbild (Sache, nicht Person):** „Das Finanzamt freut sich über diesen Fehler.“
**Leitplanken (verbindlich):** Provokation muss durch belegte Fakten im Video aufgelöst werden (kein Fake-Clickbait).
Keine Beleidigung von Gruppen, keine Falschaussagen über reale Personen/Firmen, keine Anlage-/Steuerberatung als
Versprechen. Kontrovers gegenüber Ideen/Systemen/Gewohnheiten – nicht gegenüber Menschen.
**Zusätzlich:** Die Provokation am Ende als Kommentar-Frage zurückspiegeln („Hättest du die Million genommen?“).
Re-Hook alle ~8 s bleibt Pflicht (1.7).

### 1.7d Referenz 4: „Never Chase Money“ (583K Likes, vom User als Vorbild gezeigt 2026-11-26)
Bild: `referenzen/ref4_never_chase_money_lineart.jpg`. Mindset-Clip, 18 s, Querformat, Schwarz-Weiß.
- **Look:** minimalistische, weiß leuchtende Line-Art auf Schwarz (Strichfiguren, Münz-Icons, Blaupausen-Bemaßung,
  Netzwerk-Linien, Speed-Lines), sanfter Glow, KEINE Farben, KEINE Wort-für-Wort-Untertitel – nur 1–2 Schlüsselwörter
  pro Szene als ruhige Versal-Typo („HOW IS IT MADE?“, „THE GOAL“, „VALUE“).
- **Tempo:** neue Bild-Metapher alle ~1,5–2,5 s, harte Wechsel, jede Szene = ein Gedanke:
  Figur jagt Münze, die davonläuft → Münzen zerstreuen sich in ein Netzwerk → Münze als technische Blaupause
  („Wie wird es gemacht?“) → Zähler „THE GOAL“ $0 → $1.000.000 mit Menschenreihe darunter → Eisberg:
  oben „$1.000.000“, unter Wasser riesig „VALUE“ → Automat mit „$0“.
- **Hook:** widerspricht dem Wunsch der Zielgruppe („Je mehr du dem Geld hinterherjagst, desto schwerer …“) =
  kontroverser Hook (1.7b) + Mindset-Lehre statt Zahlen-Fakten.
- **Übernehmen:** (1) Metaphern-Szenen im 2-s-Takt, (2) Line-Art-Icons im Glow-Stil (passt zu unseren Gitterlinien),
  (3) Zähler-auf-Ziel mit Menschenreihe, (4) Eisberg-/Blaupausen-Metaphern, (5) Mindset-Hooks gegen den Strom.
  Eigene Inhalte/Texte – nicht kopieren.

### 1.7c Zielgruppe junge Leute / „schnell reich“ (User-Wunsch 2026-11-26)
- User will Geld-Themen mit **viel Dopamin** für junge Zuschauer, die schnell reich werden wollen.
- Umsetzung: Dopamin im **Bild und Tempo** (explodierende Zahlen, rasende Zähler, Gold-Explosionen, Fake-out-Re-Hooks),
  aber **ehrliche Auflösung**: keine Trading-/Krypto-/Glücksspiel-Versprechen, keine konkreten Anlagetipps, keine
  „passives Einkommen in 30 Tagen“-Mythen. Die Provokation („Nimm nicht die Million“) zahlt auf eine echte Lehre ein
  (Zinseszins, Zeit, Abzock-Fallen erkennen). So bleibt der Kanal glaubwürdig und TikTok-richtlinienkonform.
- Gute Themenfelder: Mathe-Wetten, Abzock-Fallen (Raten, Abos, Fake-Rabatte), krasse echte Geldgeschichten,
  „Was reiche Leute anders machen“ (belegt), Gaming/Pop-Kultur + Geld (GTA-Rezept).

### 1.8 Trend-Recherche 25.11.2026 (Fakten geprüft, vor Produktion Stand erneut prüfen)
- **GTA 6** (Launch 19.11.2026): laut Take-Two **3,79 Mrd. $ Day-One-Retail-Umsatz** (Firmenschätzung), 32,5 Mio.
  Vorbestellungen. ≈ **43.900 $ pro Sekunde** (3,79 Mrd./86.400). GTA V 2013: ~800 Mio. $ am ersten Tag.
  Avengers: Endgame (2019): 1,2 Mrd. $ am ganzen Startwochenende → GTA 6 an EINEM Tag ≈ 3×.
  Quelle: take2games.com IR-Meldung; Fox Business.
- **Black Friday 27.11.2026 / Cyber Monday 30.11.:** HDE-Prognose 6,2 Mrd. € (Umfrage IFH Köln, Kaufabsicht).
  idealo-Analyse Black Friday 2025 (10.000 Produkte, 3.500 Shops): 79 % günstiger als im Oktober, **Ø nur 8 %
  Ersparnis**, **52 % waren an einem anderen Novembertag noch billiger**; keine flächendeckenden Vorab-Preiserhöhungen.
  Verbraucherzentrale: „Statt“-Preise oft UVP, die kaum ein Händler verlangt.
- **Bitcoin** 25.11.2026: ~58.400 $ (−24 % im November). Pizza-Bitcoin (10.000 BTC, 2010) ≈ **584 Mio. $** →
  NICHT „über eine Milliarde“ sagen (F2!).
- **TikTok-Formate:** „In this town everybody goes out partying except me“ steigt gerade (= Referenz 1 des Users!),
  Black-Friday-Content (182 Mio. Views in Europa/Woche), GTA-6-Loading-Screen-Intro.

### 1.9 Viral-Rezept aus Video 3 (GTA 6) – höchste Priorität bei Themenwahl
Was den Unterschied gemacht hat (gegenüber Video 1/2, die „nur“ gut waren):
1. **Trend-Jacking:** Thema war DAS Gesprächsthema der Woche (Launch 6 Tage vorher) → Publikum sucht danach.
   → Vor jedem Video Trend-Recherche (WebSearch, „extended“) und Thema mit aktuellem Hype bevorzugen; schnell liefern.
2. **Unvorstellbare Zahl greifbar gemacht:** 3,79 Mrd. → „44.000 $ pro SEKUNDE“ (Zahl pro Zeiteinheit).
3. **Live-Zähler „Während du zuschaust“:** der Zuschauer ist Teil der Rechnung → bleibt bis zum Ende, um die Endzahl zu sehen.
4. **Vergleich mit bekanntem Rekord:** GTA 5, Avengers: Endgame → „das Dreifache an einem Tag“.
5. **Fan-Community-Thema** (Gamer) + Geld-Winkel → breites Publikum, das kommentiert und teilt.
6. Gleicher Gold-3D-Stil + ElevenLabs-Stimme „Rene Deutschmann – Trustworthy and Calm“.
→ Ideale nächste Themen kombinieren: aktueller Hype + Riesenzahl pro Sekunde/Minute + Live-Zähler + Rekord-Vergleich.
→ Teil 2 eines viralen Videos zeitnah liefern (Zuschauer warten darauf).

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
- **Live-Zähler-Prinzip (Video 3, GTA):** Zahl oben läuft die ganze Zeit mit Rate × Zeit („Während du zuschaust“) –
  wie das ständig steigende NETTOVERMÖGEN in Referenz 3; Abschnitts-Fakten in der Delta-Zeile darunter.
- `tools/tts.py` nutzt jetzt `GAP.get(beat, 0.35)` → neue Beat-Namen brechen nichts mehr.
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
| F18 | Zähler über hellem 3D-Hintergrund schlecht lesbar (GTA, Turmspitze hinter HUD) | Kein Kontrast-Schutz | HUD hat jetzt dunklen weichen Radial-Hintergrund (`#hud-bar::before`, z-index 0, Kinder z-index 1) – in jede neue `hud.tpl.html` übernehmen. |
| F19 | Punktlicht nah am Goldturm → weißer Hotspot | Licht zu nah/zu stark | Punktlicht seitlich-vorne (z. B. 3.2/2.4/5.0), Intensität ≤ 2,5. |
| F20 | Wort doppelt (3D-Schild „WELTREKORD“ + Untertitel) | Gleiche Info zweimal | Kein 3D-Schild mit demselben Wort wie der gleichzeitige Untertitel. |
| F21 | Skript 46 s zu lang (QA-Skript fing es) | Zu viele Füllwörter | Erst QA-Skript, dann kürzen: Nebensätze streichen, Zahlen behalten. |
| F22 | Live-Aussage („bis Video vorbei: über 1,7 Mio.“) hängt von der Videolänge ab | Zahl = Rate × Dauer | Im VOICEOVER_TEXT Mindestlänge angeben; nach ElevenLabs-Einbau prüfen: Rate × T ≥ genannte Zahl. |
| F23 | Zähler zeigte „0 $“ zwischen Satzanfang und Betrag (GTA, erst im finalen MP4 bemerkt → 15 min Neu-Render) | Zählt erst ab `key`, davor Startwert 0 | Vor dem `key` Platzhalter „? $“ statt 0; Snapshots auch zwischen Satzanfang und Betrag setzen (nicht nur auf Satzmitte). |
| F24 | Kamera flog bei Käfig-zu-Käfig-Wechsel dicht an der Figur vorbei (Teil 2) | Direkter Weg zwischen zwei Käfigen kreuzt die Figur | Vor jedem Abflug eine Totale-Keyframe (`k(d.k - 0.15, Totale)`) einfügen – zeigt zugleich den Abflug. |
| F25 | Käfig-Schilder (Name/Betrag/Zusatz) auf Untertitel-Höhe | Kamera-Ziel zu tief | Bei Nahaufnahmen von Käfigen Kamera-Ziel ≈ 4,6 (Schilder rutschen unter den Untertitel); Zusatz-Objekte (Uhr) darüber. HUD-Labels ≤ 26 Zeichen, sonst Umbruch. |
| F26 | HUD blieb das ganze Video auf dem Startwert stehen (Black Friday) | `const RATE` doppelt deklariert (alte Konstante aus kopierter HUD-Vorlage) → Script-Abbruch | Beim Kopieren der HUD-Vorlage eigene Konstanten mit Video-Präfix benennen (`BF_RATE`); nach jedem Build sofort Snapshot – „Zähler ändert sich nie“ = Script-Fehler. |
| F27 | 3D-Objekte (Preisschild, Kalender, UVP) auf Untertitel-Höhe | Objekt-y ≈ Kamera-Ziel-y | Faustregel: Hauptobjekt ≈ 1,0–1,4 Einheiten UNTER dem Kamera-Ziel; Text/Label lieber aufs Objekt (Textur) als als eigenes Schild darüber. |
| F28 | Erstes Wort („Hör“) erschien am Ende wieder | Voiceover beginnt bei 0,0 s; Untertitel-Start auf ≥ 0,1 s geklemmt → Clip-Dauer 0 → HyperFrames zeigt ihn bis zum Ende | `build.py`: Start ≥ 0,0 und Dauer ≥ 0,08 s (in allen Projekten gefixt). Snapshot immer auch in den letzten 2 s prüfen. |
| F29 | InstancedMesh-Münzen unsichtbar an neuer Position | Frustum-Culling nutzt alte Bounding-Sphere | Bei InstancedMesh, die über Stationen wandern: `frustumCulled = false`. |
| F30 | Schilder drehten sich mit Objekt aus dem Bild (Eisberg) | Labels Kind der rotierenden Gruppe | Nur Geometrie rotieren, Schilder in nicht-rotierender Gruppe. |
| F31 | Text dreifach (3D-Schild + Untertitel + HUD), erneut | F20 bei neuem Szenen-Stil vergessen | Bei Schlüsselwort-HUD (Referenz-4-Stil) KEINE Text-Schilder in 3D – nur Bild-Metaphern (Münzen, Glühbirne, Herzen). |

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
- Video 3 „GTA 6 – 44.000 $ pro Sekunde (Teil 1)“ (`videos/2026-11-25_gta6/`): **FINAL geliefert** mit ElevenLabs (42,3 s).
  Teil 2 versprochen: „Wer das Geld wirklich bekommt“ (Aufteilung Plattform/Handel/Take-Two – vorher recherchieren).
- Video 4 „GTA 6 – Wer bekommt das Geld? (Teil 2)“ (`videos/2026-11-26_gta6-teil2/`): **FINAL geliefert** (42,8 s).
  79,99 € → −12,77 € MwSt → −20,17 € Store → 47,05 € Rockstar (−41 %); Live-Zähler Sony/MS 13.160 $/s. CTA = Kommentar-Frage statt Teil 3.
- Video 5 „Black Friday – 18.000 € pro Sekunde“ (`videos/2026-11-26_black-friday/`): **FINAL geliefert** (38,3 s), Posting
  26./27.11. Neu: Live-Zähler bleibt als Zusatzzeile („seit du zuschaust“) im HUD, auch wenn die Hauptzahl wechselt.
- Video 7 „Jag nicht dem Geld hinterher“ (`videos/2026-11-27_jag-nicht-dem-geld/`): **FINAL geliefert** (39,1 s).
  Erstes Video im Referenz-4-Stil: harte Schnitte zwischen 3 Stationen (Verfolgung / Instagram / Eisberg),
  Schlüsselwort-HUD statt Zahlenzähler, Bild-Metaphern statt 3D-Texten. A/B-Test Mindset vs. Zahlen-Fakten.
- Video 6 „Cent-Wette“: Skript + Sprechertext fertig, wartet auf ElevenLabs-Datei.
- Offen: User meldet, ob GTA 6 Teil 2 / Black Friday viral gehen → Ergebnis ins Logbuch.
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
| 2026-11-26 | Video 3 „GTA 6“ (gepostet) | „Scheint das beste zu sein, geht etwas viral, Thema sehr interessant – gefällt mir richtig richtig gut“ | GTA-Video = neues Top-Vorbild; Viral-Rezept 1.9 (Trend-Jacking + Zahl pro Sekunde + Live-Zähler + Rekord-Vergleich) bei jeder Themenwahl zuerst anwenden |
| 2026-11-26 | Video 5 „Black Friday“ | „Dieses Video war auch gut“ + Wunsch: am Anfang etwas Kontroverses sagen/fragen, damit Zuschauer länger dranbleiben | Neue Pflicht-Regel 1.7b: kontroverser Hook mit Formeln + Leitplanken; Provokation am Ende als Kommentar-Frage spiegeln |
