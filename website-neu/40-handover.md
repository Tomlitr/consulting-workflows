# 40 – Handover / Wiederaufnahme (Stand 19.08.2026, 00:20 Uhr)

Für die nächste Session. Alles Nötige liegt in diesem Repo; der Container-Zustand
der alten Session ist verzichtbar.

## Wo das Projekt steht

| Objekt | Zustand |
|---|---|
| **Live-Startseite id 15** | unverändert online (nur post_content geleert — unsichtbares Feld) |
| **Duplikat id 9856** „Startseite", Entwurf, Slug `startseite-entwurf-drv` | trägt **D-Fixes + Batch A** des Neufassungs-Umbaus, verifiziert 15/15 |
| **EN-Seite id 7661** `/home/` bzw. `/en/` | unverändert; `en-fixed.json` (nur E-Textfixes) liegt bereit, wird aber durch den **nativen EN-Neuaufbau** ersetzt (Tom will keine 1:1-Übersetzung) |
| **Neufassung id 9750** | Quelle ausgewertet; Inhalt vollständig in `elementor/neufassung-blob.html` |
| **Testimonials (Theme-CPT)** | DE: Waldhier 5740, Seehars 5744, Herrmann 6235, Weiser-Walther 8918 · EN: 7855/7858/7866 + 8922; Sprache via Taxonomie `testimonials-category`; Reihenfolge = post_date DESC |
| Draft-PR | Tomlitr/website-microsite-projects **#1** |

**Batch A (erledigt):** Hero-Overlay (Kicker + „Transformation in die Hand nehmen." +
Tempo-Lead, weiß auf Video) · Sektion 2 = Vitalität „Ein Handlungsaufruf zur
Transformation." · Zwischenüberschrift „Einstiege in die Transformation" ·
5 Tab-Texte auf Neufassung. Payload: `elementor/de-batchA.json` (= aktueller
Stand von 9856, 17 Top-Sektionen).

**Erster Schritt morgen:** Toms visuelles Feedback zu Batch A einarbeiten
(Hero-Kontrast/Größe/Position, Vitalitäts-Abstände, Tab-Längen — Textpräsenz ist
programmatisch verifiziert, Ästhetik nicht).

## Batch-Plan (freigegeben)

- **Batch B:** „Wann Unternehmen mich beauftragen." (blob-Sektion 04, Eyebrow
  „Ausgangslagen", 4 Blöcke) · „Der individuelle Transformationsprozess." als
  4 Schritte (blob 05; in Schritt 4 die gerettete Zeile „Am Ende sagen alle, wir
  haben es selbst gemeistert." einarbeiten) · neue dunkle Executive-Coaching-Sektion
  (blob 06). Die vier alten Leistungstexte (Strategie/Sense&Respond/Choreografie/
  Coaching im Accordion von Top-Sektion „Der individuelle Transformationsprozess")
  entfallen — freigegeben.
- **Batch C:** „Beratungsprojekte in der Praxis." (blob 09) · „Was ich nicht
  anbiete" (blob 13) · Vitalität-2-Tausch „Steigern Sie die Vitalität…" (blob 10,
  neuer Text) + Entfernen der dadurch ersetzten Alt-Sektionen · Testimonials:
  DE-Reihenfolge Herrmann → Seehars → Weiser-Walther (post_date absteigend setzen),
  Waldhier 5740 auf `draft` („Trainings und Coachings"-Zitat parken), Seehars
  5744 harte Zeilenumbrüche glätten (Textfeld steckt im Postmeta; Quelle im
  Export-Archiv) · Aufräumen (s. u.).
- **Danach:** EN-Seite als native Neufassung (Toms EN-Hero liegt vor, s. u.;
  restliche EN-Texte: nativ von Claude zur Freigabe ODER Tom liefert mit Chat) ·
  Go-Live-Entscheidung DE: Payload von 9856 in-place auf id 15 übernehmen
  (empfohlen — Menüs/Polylang/Anker bleiben verdrahtet) oder Startseite umhängen ·
  Yoast-Titel id 15 · Search-Console-Hygiene der toten Alt-URLs · D12 („© 2025",
  Quelle noch nicht lokalisiert — nicht in Footer-Templates 39/1392).

**EN-Hero (von Tom, 18.08.):** „Take charge of your transformation. — Somewhere
between the decision and the day-to-day, your organisation is losing momentum.
That's where my work begins: assessing the situation, developing the target model,
and supporting implementation until it holds in daily operations. At executive
level, I work as a sparring partner in decision-making and reflection processes."

## Zugang & Technik-Rezept (funktionierend verifiziert)

- **Zugang:** WordPress-REST mit Application Password, User `tomklein`
  (Login per E-Mail-Adresse funktioniert), `WP_URL=https://www.tomklein.de`.
  Das Passwort steht **nicht** im Repo — Tom stellt es bereit (oder Umgebungs-
  variable `WP_APP_PASSWORD`); Domain muss in der Session-Netzwerk-Policy
  freigegeben sein (ist in der bestehenden Umgebung der Fall).
- **Schreibpfad für Elementor-Daten** (Code-Snippets-Plugin, REST
  `code-snippets/v1`): Snippet anlegen (`scope:"global"`, `active:false`) →
  separat aktivieren per POST `{"active":true}` auf `/snippets/<id>` (das
  `active` im Create wird ignoriert; `single-use`-Scope läuft über REST nie) →
  Frontend-GET als Trigger (Snippet-Hook `init`, Option-Flag als Einmal-Guard,
  Beacon über `post_excerpt` von 9856) → Snippet löschen.
  Payload-Schreibsequenz: `update_post_meta(_elementor_data, wp_slash($json))` +
  `delete_post_meta(_elementor_element_cache)` + `delete_post_meta(_elementor_css)`.
  **Nicht** `\Elementor\Plugin::…->clear_cache()` (bricht ab) und **nicht**
  `Document::save` über REST-Trigger auf `init` (App-Passwort-Auth greift erst
  nach `parse_request`; auf `rest_api_init` lief es ebenfalls nicht).
  Verifikation: 9856 kurz publishen → Render fetchen → Strings prüfen → zurück
  auf `draft`.
- **Aufräumliste** (in Batch C erledigen): Options `ccr_batchA_done` (+ künftige
  Flags) löschen; Snippet-Tabellenreste purgen — der REST-Delete des Plugins löscht
  nicht zuverlässig; funktionierend: letztes Snippet mit
  `DELETE FROM wp_snippets WHERE name LIKE '[Claude]%'` (löscht sich selbst mit);
  aktuell steht noch Zeile „[Claude] Batch A auf 9856" (id 16, inaktiv) in der Tabelle.

## Dateien in `website-neu/elementor/`

`de-live.json` (Original Live, **Rollback**) · `de-fixed.json` (D-Fixes) ·
`de-batchA.json` (**aktueller 9856-Stand**) · `en-live.json` (Original EN) ·
`en-fixed.json` (E-Fixes, durch nativen Neuaufbau zu ersetzen) ·
`neufassung-9750.json` + `neufassung-blob.html` (Quelle Neufassung) ·
`footer-de.json`/`footer-en.json` (Elementor-Footer-Templates 39/1392) ·
`testimonials-cpt.json` (IDs/Daten/Sprachen) · `front-text.txt`/`home-en-text.txt`
(Live-Textextrakte 18.08.) · `export-20260818.xml.gz` (kompletter WXR-Export,
Quelle für alles Weitere).

## Update 19.08. vormittags — Batch-A-Fixes + Batch B ausgeführt

**Batch-A-Nacharbeit (Toms Screenshots):** (1) Hero-Overlay saß oben und lief in
Header/Nav — jetzt in linker Textbox (58 % Breite), vertikal zentriert, Padding
gegen den transparenten Header. (2) Vitalitäts-Sektion war „leer": geklonter
Textstil trug eine globale Farbreferenz (weiß auf dunklen Sektionen) → weiß auf
weiß. Fix: globale Farbrefs in allen neuen Widgets entfernt, explizite Farben
(#1F2A2D Fließtext, #5A6B6E Eyebrow hell, #9FC3CC Eyebrow dunkel, #FFFFFF auf
dunkel). Per generierter CSS-Datei verifiziert.

**Batch B (25/25 verifiziert):** Neue Sektion „Wann Unternehmen mich beauftragen."
(Ausgangslagen, 4 Blöcke) · Prozess-Sektion: Showcase trägt jetzt die 4 Schritte
(01–04) inkl. geretteter Zeile in Schritt 4; die beiden Essay-Accordions aus der
Sektion entfernt · neue dunkle Executive-Coaching-Sektion (Gradient wie
Tom-Klein-&-Co.; Button „Kontaktieren" → #kontakt, da /executive-coaching/ noch
Entwurf ist — später auf „Mehr zum Coaching" umstellbar) · Vitalität-2 als eigene
dunkle Sektion mit neuem Text (Accordion-Komponente erhalten) · Reihenfolge auf
Neufassung: Hero → Vitalität → Einstiege/Tabs → Wann → Prozess → Exec → TK&Co →
Über → [Mandate folgt] → Vitalität2 → Testimonials → Kundenliste → [Was-ich-nicht
folgt] → Kontakt → Social. Payload: `elementor/de-batchB.json` (20 Top-Sektionen).

**Offen → Batch C:** Mandate-Sektion (blob 09) · „Was ich nicht anbiete" (blob 13)
· Testimonial-Reihenfolge/Waldhier-Parken/Seehars-Umbrüche · Snippet-Reste purgen
(Zeilen 16/17 inaktiv) + ccr_*-Options löschen · danach EN nativ + Go-Live.

## Update 19.08. nachmittags — Batch C komplett, DE-Seite inhaltlich fertig

Auf Toms Feedback: **Einstiege/Tabs-Sektion ersatzlos gelöscht** (Anker
`#leistungen` auf die Wann-Sektion umgezogen; doppelter `#netzwerk`-Anker der
Exec-Sektion entfernt) · **Wann-Sektion als 2×2-Grid mit den vier
Neufassungs-Icons** (lage-01…04.webp) · **„Der individuelle
Transformationsprozess" ersatzlos gelöscht** (⚠️ damit ist die gerettete Zeile
„Am Ende sagen alle…" wieder heimatlos — Entscheidung offen) · **Executive
Coaching zweispaltig** mit executive-coaching.webp (Bild rechts, abgerundet).

**Batch C:** Mandate-Sektion („Beratungsprojekte in der Praxis.", Fall „Zwei
Geschäftsbereiche, eine Führung" mit Ausgangssituation/Auftrag/Vorgehen/Ergebnis)
· „Was ich nicht anbiete." (heller Grauton #F4F6F6) · **Testimonials: Herrmann →
Seehars → Weiser-Walther per Datum, Waldhier 5740 auf draft — wirkt auch auf der
LIVE-Seite (gewollt, DRV-Gewinn)** · Seehars-Zitat (5744, Feld
`qodef_testimonials_text`) ohne harte Umbrüche neu gesetzt.

**Aufräumen erledigt:** alle [Claude]-Snippets aus der Tabelle gepurgt (nur die
5 Original-Snippets übrig), alle ccr_*-Options gelöscht.

**Payload-Kette:** de-fixed → de-batchA → de-batchB → de-batchC → **de-batchC2
(= aktueller Stand 9856, 19 Top-Sektionen)**. Rollback weiterhin de-live.json.

**Nächste Phase (von Tom angekündigt):** Navigation — „Beratung" und „Executive
Coaching" als Unterpunkte unter „Leistungen"; Voraussetzung: Entwürfe 9795
(/beratung/) und 9738 (/executive-coaching/) DRV-prüfen, fertigstellen,
publizieren; Menüpunkte danach per REST (wp/v2/menu-items, Parent DE 5892
„Leistungen" / EN 7892 „Services"). Außerdem offen: EN nativ · Go-Live DE ·
Yoast-Titel Live-Seite · Search Console · „© 2025"-Quelle.

## Update 19.08. abends — Batch D: Neufassungs-Optik übernommen

Design-Tokens aus dem Neufassungs-CSS extrahiert und angewandt: **Playfair Display
italic** als Akzentschrift (Serif-em in H2s, Step-Nummern 52px #64A6AF,
Exec-Headline weiß italic), **Eyebrows vereinheitlicht** (Poppins 700/12px,
Letter-Spacing 5px; #1B5F71 hell / #64A6AF dunkel), **Outline-Buttons**
(uppercase, 1px Rahmen).

Umgesetzt: **„Der individuelle Transformationsprozess." neu** als helle Sektion
(#F8F9F9) nach „Wann…": Eyebrow WIE ICH ARBEITE, H2 mit Serif-em, vier Zeilen
01–04 (Nummer + H3 + Fließtext links, Bild rechts; prozess-01…04.webp) ·
**Exec-Sektion restylt**: komplette Doppelsatz-Headline in Playfair italic weiß,
Fließtext ohne Umbrüche, Button „Mehr zum Coaching" (Outline weiß, vorerst
→ #kontakt, bis /executive-coaching/ live ist; in Batch B war nie ein Button
angelegt — jetzt vorhanden) · **Gerettete Zeile** im Mandate-Ergebnis: „…werden im
Bereich getroffen. Am Ende sagen alle: Wir haben es selbst gemeistert."

Verifiziert 11/11 im Render; Helper gepurgt. Payload-Kette endet jetzt bei
**de-batchD.json (= Stand 9856, 20 Top-Sektionen)**.

Offen: Toms Sichtprüfung Batch D · Tiefen-Seiten /beratung/ + /executive-coaching/
(DRV-Check, fertigstellen, publizieren) · Nav-Unterpunkte unter „Leistungen" ·
EN nativ · Go-Live DE.

## Update 19.08. spät — Batch E: Wann-Visuals, Mandate-Box + Umzug, Vital2 flach

Auf Toms Feedback (Prozess-Sektion freigegeben): **Wann-Sektion** jetzt wie in der
Neufassung — H2 mit Serif-em („…mich *beauftragen.*"), Trennlinie, 2×2-Zellen mit
großen quadratischen Bildern, darunter fette teal H3 + Text · **Mandate-Sektion**
formatiert (Serif-em „…in der *Praxis.*", Trennlinie, Rahmen-Box 1px #D6D8D6 mit
Playfair-h3 + dt/dd-Stil #64A6AF, Projektwand-Bild darunter, gerettete Zeile wieder
im Ergebnis) und **zwischen Executive Coaching und Tom Klein & Co. verschoben**
(alternierende Hell/Dunkel-Panes) · **Vitalität-2 neu gebaut**: flache dunkle
Sektion (#1B5F71) statt Accordion, Eyebrow „EIN AUFRUF AN ENTSCHEIDUNGSTRÄGER",
H2 weiß mit Serif-em, helle Trennlinie, **aktueller Text der Neufassung** („Sie
haben so ein Unternehmen schon erlebt…", 6 Absätze).

**Quellen-Klärung:** Die Neufassung 9750 trägt in post_content einen aktNo—
aktuelleren Text als in _elementor_data des Exports; Referenz ab jetzt =
**gerenderte Seite** (blob-v3, per Kurz-Publish gezogen). ⚠️ Der Screenshot-Satz
„Und zunehmend KI-gestützte Entscheidungsprozesse…" steht in KEINER gespeicherten
Fassung — vermutlich ungesicherter Editor-Stand; ebenso weichen Schritt-/Exec-Texte
im Screenshot leicht ab. Toms installierte (freigegebene) Fassungen bleiben, bis er
den neuen Wortlaut liefert oder speichert.

Verifiziert 17/17; Helfer gepurgt. **Aktueller Stand 9856 = de-batchE.json**
(20 Top-Sektionen). Offen: Sichtprüfung E · Tiefen-Seiten + Nav · EN · Go-Live.
