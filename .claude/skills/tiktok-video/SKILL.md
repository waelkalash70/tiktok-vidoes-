---
name: tiktok-video
description: Erstellt deutschsprachige, faceless TikTok-Videos (9:16) im Stil der Referenzvideos des Users – Ein-Wort-Untertitel, eine Hauptfigur in einer Szene, wörtliche Visualisierung jedes Satzes, Spannungs-Leiste oben. Nutzen, wann immer der User ein neues Video, ein Skript, eine Idee, eine Überarbeitung oder Feedback zu einem Video gibt. Enthält Stilregeln und ein Feedback-Logbuch, das nach jedem Feedback aktualisiert werden MUSS.
---

# TikTok-Video-Skill (Deutsch, faceless)

Du produzierst für einen deutschen TikTok-Creator (Faceless-Account) komplette Kurzvideos
**mit Claude Code + HyperFrames** – Szenen/Animationen als HTML+GSAP, gerendert zu MP4.

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

## 2. Arbeitsablauf pro Video

1. **Logbuch lesen** (Abschnitt 4) und offene Präferenzen beachten.
2. **Skript** auf Deutsch schreiben → dem User zeigen, falls er nichts anderes gesagt hat.
3. **Storyboard** als Tabelle: Satz | Zeit | Bild/Animation | Farbwörter | Leiste-Zustand.
4. **Audio:** Voiceover vom User (bevorzugt) → `transcribe --language de` liefert Wort-Timestamps
   (`transcript.json`) → daraus die Ein-Wort-Untertitel-Clips bauen. Ohne User-Audio: HeyGen
   Voice Turbo über `/media-use` (braucht `auth login`). Lokales `tts` (Kokoro) kann **kein Deutsch**.
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

---

## 4. Feedback-Logbuch

### Feste Präferenzen des Users
- Videos immer auf **Deutsch**.
- Videos werden mit **Claude Code** (programmatisch) erstellt – Render-Framework: **HyperFrames** (vom User gewünscht).
- Visualisierung soll **sehr nah an den Referenzen** sein.
- Nische: _noch offen – beim User erfragen und hier eintragen._

### Einträge
| Datum | Video | Feedback | Abgeleitete Regel |
|---|---|---|---|
| 2026-11-24 | – (Setup) | Skill angelegt nach Analyse von 3 Referenzen | Stil-DNA siehe Abschnitt 1 |
| 2026-11-24 | – (Setup) | User will HyperFrames (HeyGen) als Werkzeug | Alle Videos mit HyperFrames bauen, siehe 2a |
