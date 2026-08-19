# 40 – Handover (Stand 19.08.2026, Abend — für neue Session maßgeblich)

**Neue Session:** Dieses Dokument zuerst lesen. Zugang: Tom stellt das
WordPress-Anwendungspasswort im Chat bereit (User `tomklein`, Login per E-Mail
funktioniert, `https://www.tomklein.de`); Domain ist in der Umgebungs-Netzwerk-Policy
bereits freigegeben. Repo: `Tomlitr/website-microsite-projects`, Branch
`claude/drv-classification-risk-review-7x0nce`, Draft-PR #1.

## Aktueller Zustand

| Objekt | Zustand |
|---|---|
| **Entwurf id 9856** „Startseite", Slug `startseite-entwurf-drv` | **DE-One-Pager KOMPLETT** im Neufassungs-Design. Stand = `elementor/de-batchF.json` (20 Sektionen). Reihenfolge: Hero(Video+Overlay) → Vitalität → Wann(Bild-Grid) → Prozess(01–04, Playfair) → Exec(dunkel, Bild, Button→/executive-coaching/) → Beratungsprojekte(Box+Bild) → TK&Co → Über → Vitalität2(dunkel, flach) → Testimonials → Kundenliste → Was-ich-nicht → Kontakt → Social |
| **Live-Startseite id 15** | Elementor-Daten unverändert (alter Stand). Yoast-Titel alt. post_content geleert. |
| **Heute LIVE geändert** | Testimonials: Herrmann→Seehars→Weiser-Walther, Waldhier (5740) auf draft, Seehars-Text geglättet · Subpages **/beratung/ (9795)** + **/executive-coaching/ (9738) publiziert** (DRV-geprüft: Rot-Treffer nur in Negations-Absätzen = gewollt) · **Nav DE (Menü 97): Unterpunkte „Beratung" (Item 9886) + „Executive Coaching" (9887) unter „Leistungen" (5892)** · unsichtbares „Seminare"-Menü-Relikt (8881) gelöscht |
| EN id 7661 (/en/, Polylang; EN-Menü 156, „Services" 7892) | unverändert; nativer Neuaufbau steht aus |
| Neufassung id 9750 | Quelle; Referenz = gerenderte Fassung `elementor/neufassung-blob-v3.html` |

## Offen für die nächste Session (Reihenfolge sinnvoll)

1. **Toms Sichtprüfung** von Batch E+F (Wann-Bildzellen, Mandate-Box, Vitalität2 flach, Abstand Exec↔Mandate, Subpage-Nav-Dropdown).
2. **KI-Satz:** „Und zunehmend KI-gestützte Entscheidungsprozesse, die Tempo geben, ohne Verantwortung zu verwischen." steht in KEINER gespeicherten Fassung (nur Toms Screenshot; vermutlich ungesicherter Elementor-Editor-Stand von 9750). Wenn gewünscht: Tom liefert Satz/Speichert — dann in Vitalität2 von 9856 einfügen.
3. **Go-Live DE:** de-batchF-Payload per Snippet-Rezept auf **id 15** schreiben (in-place; Menü/Polylang/Anker bleiben) + `_yoast_wpseo_title` von 15 auf „Tom Klein - Beratung für Business Transformation" + danach 9856 als Arbeitskopie behalten oder löschen. Rollback: `elementor/de-live.json`.
4. **EN nativ:** One-Pager EN neu (Toms EN-Hero unten; restliche Texte nativ zur Freigabe oder von Tom) · EN-Subpages · EN-Nav (Menü 156, Parent 7892).
5. **Hygiene:** Search-Console-Entfernung der toten Alt-URLs · „© 2025"-Quelle (nicht in Footer-Templates 39/1392 — vermutlich Theme-Option; per Snippet `get_option`-Scan) · Anker `#über mich` (Leerzeichen) optional.
6. **DRV-Doku:** drv-risikoreview/-Dateien sind aktuell; langfristig 05 (Schwerpunktnachweis) jährlich fortschreiben.

**EN-Hero (Tom, freigegeben):** „Take charge of your transformation. — Somewhere
between the decision and the day-to-day, your organisation is losing momentum.
That's where my work begins: assessing the situation, developing the target model,
and supporting implementation until it holds in daily operations. At executive
level, I work as a sparring partner in decision-making and reflection processes."

## Technik-Rezept (verifiziert, unverändert gültig)

Elementor-Daten schreiben via Code-Snippets-REST (`code-snippets/v1`):
1. Snippet anlegen (`scope:"global"`, `active:false`) — Payload base64 im Code.
2. Aktivieren per POST `{"active":true}` auf `/snippets/<id>` (das `active` beim
   Anlegen wird ignoriert; `single-use` läuft über REST nie).
3. Frontend-GET als Trigger; Snippet-Hook `init` mit Option-Flag-Guard
   (`ccr_*`); Beacon über `post_excerpt` von 9856.
4. Schreibsequenz: `update_post_meta(9856,'_elementor_data',wp_slash($json))` +
   `delete_post_meta(…,'_elementor_element_cache')` + `delete_post_meta(…,'_elementor_css')`.
   NICHT `clear_cache()` (bricht ab), NICHT `Document::save` (Auth-Timing).
5. Verifizieren: 9856 kurz publishen → Render fetchen → Strings prüfen → draft.
6. Aufräumen: letztes Snippet mit `DELETE FROM wp_snippets WHERE name LIKE '[Claude]%'`
   + `delete_option('ccr_…')` (Plugin-REST-Delete löscht nicht zuverlässig).
Design-Tokens: Teal `#1B5F71` · Akzent `#64A6AF` · Tinte `#1F2A2D` · Linie `#D6D8D6`
· Serif-Akzent `Playfair Display` italic (em in H2s, Step-Nummern 52px) · Eyebrow
Poppins 700/12px/LS 5px · Fließtext Poppins 300/17px · Outline-Buttons uppercase.

## Payload-Kette in `website-neu/elementor/`

`de-live.json` (Original Live = **Rollback**) → de-fixed → de-batchA…E →
**`de-batchF.json` = aktueller Stand 9856**. Quellen: `neufassung-blob-v3.html`
(gerenderte Neufassung = maßgeblich), export-20260818.xml.gz, testimonials-cpt.json,
footer-de/en.json, en-live.json (EN-Rollback). Übrige Dateien wie beschriftet.
