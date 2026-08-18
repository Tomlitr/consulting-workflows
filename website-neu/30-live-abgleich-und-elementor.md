# 30 – Live-Abgleich und Elementor-Strategie

Arbeitsstand 18.08.2026. Grundlage: Screenshots der eingeloggten Ansicht (Admin-Bar
„Duplicate Post" sichtbar), Teil 1 von mehreren Lieferungen. Wird mit jeder weiteren
Lieferung fortgeschrieben.

## 1. Entscheidung: Elementor behalten

**Empfehlung: Ja — und zwar so, dass sich die Design-Frage von selbst erledigt.**

Der bisherige One-Pager ist eine Elementor-Seite. Design, Typografie, Farbwelt,
Abstände und sämtliche Bewegung (Einblendungen, Parallax, Karussells, Hover-Effekte)
stecken als Einstellungen in dieser Seite. Daraus folgt:

- **Nicht das Design im Entwurf nachbauen, sondern die Seite duplizieren und die Texte
  tauschen.** Das Plugin dafür ist bereits installiert („Duplicate Post" in der
  Admin-Bar). Duplikat der bestehenden Seite anlegen → im Elementor-Editor Abschnitt
  für Abschnitt die freigegebenen Texte einsetzen → Layout- und Motion-Einstellungen
  nicht anfassen. Ergebnis ist per Konstruktion 1:1 das bisherige Design samt
  Bewegung — die „Differenzen" können gar nicht mehr auftreten.
- Die in Claude Chat entstandenen Entwurfsseiten (Gutenberg) sind damit **Textquelle,
  nicht Endprodukt**. Nichts davon ist verloren; es wandert in das Duplikat.
- **Elementor abschaffen** wäre ein eigenes Modernisierungsprojekt (kompletter Nachbau
  aller Sektionen und Animationen, Responsive-Tests) **ohne jeden Nutzen für das
  DRV-Ziel** — die Einstufung hängt an Wörtern und Struktur, nicht am Page-Builder.
  Falls Performance irgendwann drückt: nach dem Risiko-Umbau, nicht jetzt.

## 2. Woher die „Bewegung" kommt und wie sie erhalten bleibt

Die Fluidität der bestehenden Seite sind Elementor-Einstellungen je Sektion/Widget:

| Effekt | Wo er wohnt |
|---|---|
| Einblenden beim Scrollen | Widget/Sektion → Erweitert → **Bewegungseffekte → Eingangsanimation** (+ Dauer, Verzögerung) |
| Parallax/Scroll-Effekte auf Hintergründen | Sektion → Stil/Erweitert → **Scrolling-Effekte** |
| Testimonial-Wechsel | Karussell-Widget (Autoplay, Intervall) |
| Button-/Karten-Hover | Widget → Stil → **Hover** (Übergangsdauer) |

Beim **Duplizieren bleiben alle diese Einstellungen erhalten** — deshalb ist der
Duplikat-Weg der einzige, bei dem die Bewegung nichts kostet. Für **neue** Abschnitte
(z. B. „Was ich nicht anbiete"): im Editor eine bestehende, ähnlich aufgebaute Sektion
rechtsklick-duplizieren, Inhalte ersetzen — Abstände, Typografie und Animation werden
geerbt; sonst die Werte der Nachbarsektion ablesen und identisch setzen.

## 3. Arbeitsteilung für den Texttausch

Elementor speichert Seiteninhalte als JSON im Postmeta `_elementor_data`; die normale
REST-API gibt das nicht her. Drei gangbare Wege, in dieser Reihenfolge empfohlen:

1. **Template-Export an mich.** Elementor-Editor → Pfeil neben „Aktualisieren" →
   „Als Template speichern" → Templates-Bibliothek → Export als `.json` → Datei hier
   in den Chat. Ich nehme die Textchirurgie im JSON vor (nur `title`/`editor`/
   `text`-Felder, kein Layout) und gebe die Datei zum Re-Import zurück. Präzise,
   diff-bar, kein Design-Drift.
2. **Tauschtabelle für die Handarbeit.** Ich liefere je Sektion „alter Satz → neuer
   Satz" (Grundlage: `10-seiten-de.md` + Abschnitt 4 unten); Einsetzen im Editor ist
   dann mechanisch — von Hand oder mit Claude Chat am Browser.
3. Direktzugriff per REST in der netzfähigen Session: für Elementor-Inhalte **nicht**
   der richtige Hebel (s. o.), bleibt aber der Weg für alles außerhalb des Builders
   (Seiten anlegen, Slugs, Menü, Redirects).

## 4. Befunde aus Screenshot-Lieferung 1

### S1-01 — Expertise-Liste (Über-mich-Sektion) · **Risiko: hoch** — Haupttreffer dieser Lieferung

Ist-Zustand (wörtlich):
1. „Den organisatorischen Rahmen für eine hoch motivierte Leistungskultur zu schaffen" — ✅ unbedenklich
2. „Menschen und Teams dafür aufzustellen, **ihren eigenen Lernweg gehen und meistern
   zu können**" — 🔴 „Lernweg"
3. „**Methoden und Tools** für die offene, flexible und verantwortungsvolle
   Zusammenarbeit **zu erklären** und zu implementieren" — 🔴 „Methoden und Tools
   erklären" ist fast wörtlich die Lehrerdefinition
4. „Die Grundlagen für eine **lernende Organisation** zu schaffen, inklusive Aufbau der
   internen Kapazitäten." — 🟡 etablierter OD-Fachbegriff, aber im ohnehin belasteten
   Umfeld besser ersetzen

Neufassung (Vitalitäts-Ton bleibt, Lehr-Vokabular verschwindet):
1. unverändert
2. „Menschen und Teams so aufzustellen, dass sie Veränderung **aus eigener Kraft tragen
   und weiterentwickeln**"
3. „Die **Steuerungs- und Arbeitsformen** für offene, flexible und verantwortungsvolle
   Zusammenarbeit **auszuwählen und im Tagesgeschäft zu verankern**"
4. „Die Grundlagen dafür zu schaffen, dass sich die Organisation **aus sich heraus
   weiterentwickelt** — einschließlich der internen Strukturen und Verantwortlichkeiten."

Der einleitende Absatz derselben Sektion („…aus einer Kultur der Freiheit und
Verantwortung … nehmen wir ihre Führungskräfte und ihre Mitarbeiter auf die gleiche
Reise mit") ist unbedenklich und bleibt — das ist genau der Vitalitätston, der erhalten
werden soll.

### S1-02 — Testimonial Weiser-Walther · **Risiko: mittel, besondere Regel**

Das prominenteste Zitat enthält: „…dass sie **ihre eigenen Lernwege** erfolgreich
beschreiten können" sowie „Einzelpersonen und Teams **fördern**".

**Zitate werden nicht umgeschrieben** — es sind attribuierte Aussagen Dritter; ein
redigiertes Zitat wäre unauthentisch und im Zweifel peinlicher als das Risikowort.
Der Hebel ist die **Auswahl und Reihenfolge**:
- An Position 1 ein Zitat, das Beratungsarbeit beschreibt (Strategie, Neuordnung,
  Umsetzung, Ergebnis). Das vorhandene Zitat spricht von „maßgeschneiderten
  Strategien" — es kann bleiben, aber nicht als Auftakt.
- Mittelfristig (siehe `05`, Schwerpunktnachweis): zwei, drei aktuelle Auftraggeber um
  Kurzstatements bitten, die Mandate beschreiben. Das dient Kunden UND Prüfbild.

### S1-03 — Kundenliste „Mit wem ich bereits zusammenarbeiten durfte" · ✅ **Stärke, ausbauen**

BASF, BMW, Continental, Daimler, Roland Berger, Max-Planck-Gesellschaft u. v. a. —
diese Sektion ist doppelt wertvoll: kommerziell **und** als Beleg für viele
Auftraggeber (entkräftet zugleich die Arbeitnehmerähnlichkeit nach § 2 S. 1 Nr. 9).
Unverändert übernehmen, prominent halten.

### S1-04 — Podcast/Social-Sektion („Living Transformation!") · ✅ weitgehend unbedenklich

Publizistik ist keine Lehre im Sinne des § 2 — Podcast und YouTube-Kanal bleiben.
Einzige Kleinigkeit, niedrige Priorität: die YouTube-Beschreibung „**Gezieltes
Wissen** rund um die Themen Transformation & Wandel" bei Gelegenheit zu „Impulse und
Gespräche zu Transformation & Wandel" drehen — „Wissen" ist hier das einzige
Vokabular mit Signalwirkung.

### S1-05 — Kontakt-Sektion „Jetzt Erstgespräch vereinbaren" · ✅ passt — plus ein Tippfehler

Die Sektion entspricht bereits der Zielarchitektur (Anfrage → Erstgespräch), das
Formular ist unproblematisch. **Tippfehler im Live-Text:** „…in dem wir die
Möglichkeit **habe** uns kennenzulernen…" → „…die Möglichkeit **haben**, uns
kennenzulernen…" (Komma ergänzen). Beim Texttausch mit beheben.

## 5. Befunde aus Screenshot-Lieferung 2 (Entwurfs-Gegenstücke)

Lieferung 2 zeigt überwiegend die **Entwurfsseiten** (weißer Hintergrund,
Sechs-Spalten-Kundenliste, zentriertes Testimonial, harte Zeilenumbrüche) neben dem
Hero. Diagnose: Die Differenzen zum Live-Design sind **Builder-Artefakte**, keine
inhaltlichen — sie verschwinden mit der Duplikat-Strategie aus Abschnitt 1 von selbst
und müssen nicht nachgebaut werden.

### S2-01 — Navigation im Hero · ✅ sauber, eine offene Frage

„Lösungen · Netzwerk · Über Mich · Leistungen · English · Kontakt" — **frei von
Lehr-Vokabular**, so übernehmen. Offene Frage: **„Lösungen" und „Leistungen"
nebeneinander** — auf welche Anker zeigen die beiden? Zwei ähnliche Rubriken verwirren
Besucher und verwässern die Beratungssäule. Empfehlung: eine Rubrik führen
(idealerweise „**Beratung**"), die zweite auflösen oder umbenennen.

### S2-02 — „Über Tom Klein" · ✅ DRV-unbedenklich, sprachlich nacharbeiten

Inhaltlich auf der Beratungsseite (begleiten, unterstützen, Kultur der Freiheit und
Verantwortung — der Vitalitätston, der bleiben soll). Beim Einsetzen korrigieren:

1. Kommasetzung/Stellung: „…ungewöhnliche Lösungen verlangen — manchmal bis hin zu
   einem Wechsel der Art, **wie Sie erfolgreich sind**." (Ist-Satz bricht grammatisch:
   „…den Wechsel der gesamten Art, wie sie erfolgreich sind erfordern")
2. Höflichkeitsform groß: „…nehmen wir **Ihre** Führungskräfte und **Ihre**
   Mitarbeiter…"
3. Schlusssatz entschlacken: statt „legen weitere internationale Erfahrung in die
   Waagschale der Erfahrung und der Kompetenz" → „**Unsere Kollegen bringen
   zusätzliche internationale Erfahrung ein.**"
4. Perspektive vereinheitlichen (wechselt zwischen „wir" und „ich"): Empfehlung
   durchgängig „ich", Netzwerk als „mein Netzwerk erfahrener Kolleginnen und
   Kollegen" — deckt sich mit der Positionierung in `10-seiten-de.md`.

### S2-03 — Testimonial mit Herrenporträt · ⭐ **als Zitat Nr. 1 führen**

> „Indem er Perspektive und nicht nur Rat liefert, ermöglicht er mir kontinuierliche
> Selbstreflektion, immer passend zu meiner jeweiligen Situation. […] sich auf das
> Individuum und die besonderen Umstände zu fokussieren, **statt auf Tools und
> Methoden**. Ein wirklich einzigartiger Coach!"

Das ist inhaltlich das stärkste Zitat des gesamten Materials — **die
BSG-Abgrenzung in Kundenstimme**: individuelle Situation, Selbstreflexion,
ausdrücklich *nicht* Tools und Methoden. Es entschärft sogar sein eigenes Schlusswort
„Coach", weil es die Rolle als Reflexionsbegleiter beschreibt. Konkretisierung der
Empfehlung aus S1-02: **dieses Zitat an Position 1**, Weiser-Walther („Lernwege")
nachgeordnet. Zitate unverändert lassen (auch die Schreibweise „Selbstreflektion" —
es ist ein Zitat).

### S2-04 — Harte Zeilenumbrüche im Entwurf · Praxisregel für den Texttausch

Die Entwurfstexte enthalten eingebettete Umbrüche mitten im Satz (Folge des
Einfügens aus formatierter Quelle). Beim Übertragen in das Elementor-Duplikat:
**Fließtext ohne manuelle Umbrüche** einsetzen, Absätze nur als Absätze — sonst
bricht das Responsive-Verhalten auf schmalen Viewports.

### S2-05 — Kundenliste (weiße Variante) · inhaltlich identisch

Vollständigerer Ausschnitt als in Lieferung 1 (zusätzlich sichtbar: Union
Investment, Vaillant, Vesta, Weber Hydraulik, Zotz-Klimas). Bewertung unverändert
S1-03: Stärke, unverändert übernehmen; Layoutdifferenz erledigt die
Duplikat-Strategie.

## 6. Vollständiger Live-Abgleich per Direktzugriff (18.08.2026)

Ab hier gilt: Der REST-Zugriff auf die Site steht; die Befunde beruhen auf dem
vollständigen gerenderten Live-One-Pager (DE und EN), nicht mehr auf Screenshots.

### 6.1 Technische Befunde

- **Der Live-One-Pager (id 15, als Startseite gesetzt) ist eine Elementor-Seite**
  (764 Elementor-Marker im gerenderten HTML). Design und Bewegung liegen in
  `_elementor_data`. Die Duplikat-Strategie aus Abschnitt 1 gilt unverändert.
- **Der am 14.08. eingefügte Arbeitstext ist unsichtbar und harmlos.** Er wurde in
  das WordPress-Inhaltsfeld (post_content) von id 15 eingefügt — ein Feld, das
  Elementor beim Rendern ignoriert. Öffentlich war und ist er nie zu sehen
  (verifiziert: kein „Lead", „Button:", „PRÜFEN" im gerenderten HTML). Revisionen
  zeigen: Das Feld war vorher leer, nichts wurde überschrieben. **Aufräum-Empfehlung:**
  post_content von id 15 und id 9856 bei Gelegenheit leeren, damit ein späterer
  Theme-/Builder-Wechsel den Text nie rendert.
- **Duplikat verifiziert:** id 9856 „Startseite" (Entwurf, angelegt per „Duplicate
  Post") ist im Inhaltsfeld byte-identisch mit der Live-Seite; Duplicate Post kopiert
  Metadaten (= Elementor-Daten) standardmäßig mit. Visuelle 10-Sekunden-Kontrolle im
  Backend: id 9856 „Mit Elementor bearbeiten" öffnen → muss exakt wie die Live-Seite
  aussehen.
- **Die LMS-Schicht existiert nicht mehr.** Keine Kurs-Post-Types registriert (nur
  Core + Elementor); `/kurse/…`, `/course/…`, `/courses/…`, `/training/`,
  `/en/lessons/…`, `/shop/…`, `/en/booking/` liefern sämtlich **404**. Die
  Strukturbefunde **F-01, F-04, F-11 sind gegenstandslos** (Vermerk in `02`).
  Rest ist Suchmaschinen-Hygiene: veraltete Snippets sterben mit den 404ern aus;
  optional Entfernung via Search Console beschleunigen.
- **Seiteninventar (11 Seiten):** Live: Startseite (15), Home/EN (7661), Impressum,
  Imprint, Privacy. Entwürfe: Duplikat (9856), Chat-Entwürfe „Startseite – Neufassung"
  (9750, Elementor), `/beratung/` (9795), `/executive-coaching/` (9738) sowie AGB und
  Terms (**auf Entwurf = derzeit offline — bewusst?**). Rolle der Chat-Entwürfe
  klären: als Tiefen-Seiten gemäß Zielarchitektur weiterentwickeln oder verwerfen.
- **`/en/` und `/home/` sind dieselbe, manuell gepflegte EN-Seite** (kein
  Übersetzungs-Plugin). Konsequenz: **jede Korrektur zweisprachig ausführen** (6.3 + 6.4).
- **Navigation:** „Lösungen" verlinkt schlicht auf die Startseite (kein Anker) — die
  vermutete Doppelung mit „Leistungen" (→ `#leistungen`) ist keine; ggf. „Lösungen"
  einen eigenen Anker geben. Der Anker `#über mich` enthält ein Leerzeichen → robuster:
  `#ueber-mich`.

### 6.2 Gesamtbefund in einer Zeile

**Der Live-One-Pager ist zu ~95 % beratungssauber.** Die Tabs Projekte/Coaching/
Kultur/Management, alle vier Leistungsblöcke (Strategie, Sense & Respond,
Choreografie — „Am Ende sagen alle, wir haben es selbst gemeistert" —, Coaching als
Reflexion) und beide Vitalitäts-Essays sind unbedenklich bis vorbildlich. Es bleiben
chirurgische Eingriffe:

### 6.3 Tauschtabelle DE (im Duplikat id 9856 ausführen)

| # | Fundstelle | Ist (wörtlich) | Neu |
|---|---|---|---|
| D1 🔴 | Lösungen → Tab „Organisation", letzter Halbsatz | „…als Change Agents um, die durch Training und Coaching unterstützt werden." | „…als Change Agents um, die wir dabei im Prozess begleiten." |
| D2 🔴 | Expertise, Punkt 2 | „Menschen und Teams dafür aufzustellen, ihren eigenen Lernweg gehen und meistern zu können" | „Menschen und Teams so aufzustellen, dass sie Veränderung aus eigener Kraft tragen und weiterentwickeln" |
| D3 🔴 | Expertise, Punkt 3 | „Methoden und Tools für die offene, flexible und verantwortungsvolle Zusammenarbeit zu erklären und zu implementieren" | „Die Steuerungs- und Arbeitsformen für offene, flexible und verantwortungsvolle Zusammenarbeit auszuwählen und im Tagesgeschäft zu verankern" |
| D4 🟡 | Expertise, Punkt 4 | „Die Grundlagen für eine lernende Organisation zu schaffen, inklusive Aufbau der internen Kapazitäten." | „Die Grundlagen dafür zu schaffen, dass sich die Organisation aus sich heraus weiterentwickelt — einschließlich der internen Strukturen und Verantwortlichkeiten." |
| D5 🟡 | Essay „Vitalität in Menschen und Organisationen" | „…Schlüsselpersonen … die Möglichkeit zu geben, neues Wissen zu erwerben und sich in ihrer beruflichen Rolle zu reflektieren." | „…Schlüsselpersonen … die Möglichkeit zu geben, sich in ihrer beruflichen Rolle zu reflektieren und neue Perspektiven zu gewinnen." |
| D6 🔴 | Testimonials (Reihenfolge + Auswahl) | Waldhier-Zitat: „…begeistert er … in seinen Trainings und Coachings…" | Zitate nie umformulieren. Reihenfolge: **Herrmann (KOSTAL) zuerst** („…statt auf Tools und Methoden"), dann Seehars (Grammer, „Sparringspartner"), dann Weiser-Walther; Waldhier-Zitat zurückstellen oder um ein aktualisiertes Zitat bitten. |
| D7 | „Über Tom Klein", Grammatik | s. S2-02 | „…ungewöhnliche Lösungen verlangen — manchmal bis hin zu einem Wechsel der Art, wie Sie erfolgreich sind." · „…nehmen wir Ihre Führungskräfte und Ihre Mitarbeiter…" · „Unsere Kollegen bringen zusätzliche internationale Erfahrung ein." (die EN-Fassung ist hier die bessere Vorlage) |
| D8 | CTA Erstgespräch | „…die Möglichkeit habe uns kennenzulernen…" | „…die Möglichkeit haben, uns kennenzulernen…" |
| D9 🟡 | Social → YouTube | „Gezieltes Wissen rund um die Themen Transformation & Wandel." | „Impulse und Gespräche zu Transformation & Wandel." |
| D10 🟡 | SEO-Titel der Seite | „Tom Klein – Organisationsentwicklung & Business Coaching" | „Tom Klein – Beratung für Business Transformation" |
| D11 | Testimonial Seehars | harte Zeilenumbrüche mitten im Satz | als Fließtext setzen |
| D12 | Footer | „© 2025" | „© 2026" |

### 6.4 Tauschtabelle EN (`/en/` bzw. `/home/`, id 7661)

| # | Fundstelle | Ist (wörtlich) | Neu |
|---|---|---|---|
| E1 🔴 | Organization-Tab | „…involving employees as change agents, supported by training and coaching." | „…involving employees as change agents, whom we support throughout the process." |
| E2 🔴 | Expertise 2 | „Preparing individuals and teams to embark on and master their own learning paths." | „Preparing individuals and teams to drive change on their own — and to keep developing it." |
| E3 🔴 | Expertise 3 | „Explaining and implementing methods and tools for open, flexible, and responsible collaboration." | „Selecting the ways of working and steering that open, flexible, responsible collaboration requires — and anchoring them in daily business." |
| E4 🟡 | Expertise 4 | „Laying the foundations for a learning organization, including the development of internal capacities." | „Laying the foundations for an organization that keeps developing from within — including its internal structures and responsibilities." |
| E5 🟡 | Essay (Vitality) | „…the opportunity to acquire the knowledge they need to reflect on their changing roles… giving teams the opportunity to learn through facilitated retrospectives." | „…the opportunity to reflect on their changing roles and gain new perspective… giving teams the opportunity to grow through facilitated retrospectives." |
| E6 🔴 | Testimonial Waldhier (EN) | „…in his training and coaching sessions all over the world…" | wie D6: Reihenfolge ändern, Zitat zurückstellen/aktualisieren lassen |
| E7 🟡 | Social → YouTube | „Targeted knowledge on the topics of transformation & change." | „Ideas and conversations on transformation & change." |
| E8 | SEO-Titel EN | analog D10 prüfen | „Tom Klein – Business Transformation Consulting" |

### 6.5 Reihenfolge der Anwendung

1. Duplikat 9856 in Elementor öffnen (Sichtprüfung Design) → Tauschtabelle DE
   ausführen (Weg A: Template-JSON-Export an Claude; Weg B: Handarbeit nach Tabelle).
2. Sichtprüfung → Veröffentlichen (bzw. „Neu veröffentlichen" bei Rewrite & Republish).
3. EN-Seite (7661) genauso — per Duplikat oder direkt.
4. post_content-Reste in 15/9856 leeren.
5. Search-Console-Hygiene für die toten Alt-URLs.
6. Danach: Entscheidung über die Chat-Tiefenseiten (`/beratung/`, `/executive-coaching/`)
   und die AGB-Entwürfe.
