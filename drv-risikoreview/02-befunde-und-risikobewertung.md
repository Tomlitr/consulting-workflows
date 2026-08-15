# 02 – Befunde und Risikobewertung: tomklein.de

## Erkenntnisgrundlage — bitte zuerst lesen

Ein direkter Abruf von tomklein.de war aus dieser Arbeitsumgebung **nicht möglich**
(die Netzwerk-Policy blockiert die Domain). Grundlage der folgenden Befunde sind daher:

- **öffentlich indexierte URLs und Seitentitel** — belastbar, weil es sich um die
  tatsächliche Seitenstruktur handelt;
- **Suchmaschinen-Snippets und deren Zusammenfassungen** — die Formulierungen in
  Abschnitt B sind deshalb **sinngemäß, nicht wörtlich zitiert**. Sie sind vor jeder
  Verwendung am Live-Text zu verifizieren.

Struktur- und Vokabelebene (Abschnitt A) sind damit gesichert, die Satzebene noch nicht.
Was für den vollständigen Durchgang fehlt, steht am Ende unter „Offener Teil".

---

## A. Strukturbefunde (gesichert)

### F-01 — Die Seitenstruktur ist die eines Lernmanagementsystems · **Risiko: hoch**

Beobachtet:

| URL | Bezeichnung |
|---|---|
| `tomklein.de/kurse/einzelcoaching/` | „Kurse" |
| `tomklein.de/course/` | „Kurse Archiv" |
| `tomklein.de/course/organisationsentwicklung-fuer-die-vuca-welt/` | „course" |
| `tomklein.de/courses/compassionate-leadership/` | „courses" |
| `tomklein.de/courses/team-retrospektive-mit-agilen-teams-praxisworkshop/` | „courses" |
| `tomklein.de/en/lessons/topics-2/` | **„lessons"** |
| `tomklein.de/training/` | „Training" |
| `online.tomklein.de` | eigene Online-Plattform |

Warum das riskant ist: Die Taxonomie `course` / `courses` / `kurse` / **`lessons`** ist die
eines Kurs-Plugins (LearnDash o. ä.). „Lesson" ist die wörtliche Entsprechung von
**Unterrichtseinheit**. Damit trägt die Website an prominentester Stelle — in der URL,
also auch in jedem Suchergebnis, jedem Link und jedem Screenshot einer Prüferin — die
Aussage: *hier werden Kurse mit Lektionen erteilt*. Das ist praktisch die Definition des
Lehrerbegriffs aus `01`, Abschnitt 2.

Besonders ungünstig: **`/kurse/einzelcoaching/`** ordnet ausgerechnet das Einzelcoaching —
das inhaltlich stärkste Argument für die Beratungsseite — der Kategorie „Kurse" unter.

Empfehlung:
- Slugs auf beratungsnahe Taxonomie umstellen: `/leistungen/`, `/mandate/`, `/formate/`,
  englisch `/services/`, `/engagements/`. Kein `course`, kein `lesson`, kein `training`.
- 301-Weiterleitungen setzen (SEO), alte URLs nicht bestehen lassen.
- Wenn das Kurs-Plugin nur als technisches Gerüst genutzt wird: entweder Post-Type-Slugs
  überschreiben oder das Plugin für die Beratungsseiten verlassen.

### F-02 — Eigene Online-Kursplattform (`online.tomklein.de`) · **Risiko: hoch**

Eine separate Subdomain mit Online-Angeboten ist strukturell schwer als Beratung
darstellbar: Ein Selbstlernangebot ist definitionsgemäß Wissen für eine unbestimmte
Vielzahl unbestimmter Anwendungssituationen — genau das Kriterium aus B 5 RE 23/14 R.

**Hier hilft Textarbeit nicht.** Das ist eine Geschäftsmodellfrage, keine Formulierungsfrage.
Optionen — mit der Rechtsberatung zu bewerten:
1. Angebot einstellen oder auf Bestandskunden auslaufen lassen;
2. in eine **eigene Kapitalgesellschaft** ausgliedern, sodass die Lehrleistung nicht in
   der selbständigen Person erbracht wird;
3. bewusst weiterführen und über die **Schwerpunktbetrachtung** verteidigen — dann muss
   der Umsatzanteil klein und dokumentiert sein (siehe `05`).

> **✅ Entschieden (15.08.2026):** Die Subdomain war **nie in produktiver Nutzung** und
> wird **ersatzlos gelöscht**. Der Befund entfällt damit vollständig; mangels Nutzung und
> Umsatz trägt das Angebot auch rückwirkend nichts zum Tätigkeitsschwerpunkt bei.
> Abzuarbeiten:
> - Dienst hinter der Subdomain kündigen bzw. abschalten (läuft auf AWS, getrennt vom
>   Hauptserver)
> - DNS-Eintrag `online` in der Domainverwaltung löschen
> - Verweise auf die Subdomain entfernen: interne Links, Profile, Signaturen
> - falls in der Google Search Console angemeldet: Property entfernen

### F-03 — Der Themenkatalog ist ein Curriculum generischen Wissens · **Risiko: hoch**

Beobachtete Themen: *Organisationsentwicklung für die VUCA-Welt*, *Compassionate
Leadership*, *Team-Retrospektive mit agilen Teams – Praxisworkshop*, Kanban, virtuelle
Teamführung, agile Kommunikation.

Jedes dieser Themen ist ein **Wissensgebiet**, kein Kundenproblem. Ein nach Themen
gegliedertes Angebot ist aus Prüfersicht ein Lehrplan: Der Inhalt steht vor dem Mandat
fest und ist auf beliebige Organisationen übertragbar. Zusätzlich benennt
„**Praxis**workshop" den *praktischen Unterricht*, den die Lehrerdefinition ausdrücklich
mit einschließt.

Empfehlung: Gliederung von **Themen** auf **Ausgangssituationen** umstellen —
„Fusion zweier Bereiche", „Führungswechsel im Top-Management", „Wachstum überfordert die
Organisation". Das Thema wird zum Werkzeug im Mandat, nicht zum Produkt.

### F-04 — Buchbare Formate mit Terminen und Preisen · **Risiko: mittel**

Beobachtet: `tomklein.de/shop/businesscoaching/`, `tomklein.de/en/booking/`.

Ein Shop mit buchbaren Positionen und ein Buchungskalender erzeugen das Bild eines
offenen, standardisierten Angebots mit Plätzen — ein klassisches Kursindiz. Beratung wird
beauftragt, nicht in den Warenkorb gelegt.

Empfehlung: Shop-Logik für Beratungsleistungen ersetzen durch **Anfrage → Erstgespräch →
Angebot**. Wo Buchbarkeit bleiben soll, konsequent als „Termin für ein Erstgespräch"
rahmen, nicht als Kauf einer Leistungseinheit.

### F-05 — Die Beratungssäule fehlt in der Informationsarchitektur · **Risiko: hoch (strategisch)**

In der beobachteten Struktur tauchen `training`, `kurse`, `courses`, `lessons`, `shop`,
`booking` auf — aber **keine erkennbare Beratungssäule**: keine Leistungsseite mit
Analyse/Konzept/Umsetzung, keine Mandats- oder Projektbeschreibungen, keine
Referenzarchitektur.

Das ist der schwerwiegendste Befund, weil er nicht einzelne Sätze betrifft, sondern das
**Gesamtbild**, auf das die Schwerpunktbetrachtung abstellt. Eine Prüferin, die nur die
Navigation ansieht, findet derzeit kein Element, das die Tätigkeit auf der Beratungsseite
verankert.

Empfehlung: Eine erstklassige, prominent verlinkte Leistungsseite „Beratung" mit
2–3 anonymisierten Mandatsbeschreibungen ist die wirksamste Einzelmaßnahme überhaupt
(Vorlage in `04`).

---

## B. Formulierungsbefunde (sinngemäß — am Live-Text zu verifizieren)

### F-06 — Selbstbezeichnung „Trainer und Coach" · **Risiko: hoch**

Sinngemäß beobachtet: *„umsetzungsstarker und kreativer **Trainer und Coach** für Business
Transformation"*.

„Trainer" ist der Begriff, unter dem die DRV subsumiert. Er steht hier zudem an der
Position der Berufsbezeichnung, also dort, wo eine Prüfung zuerst hinsieht.

→ **„Berater für Business Transformation"**, ergänzt um die Funktion:
*„Ich berate Unternehmen in Transformationsvorhaben und begleite Führungskreise in
Entscheidungs- und Reflexionsprozessen."*

### F-07 — „ehemaliger Hochschuldozent" in der Vita · **Risiko: hoch**

Sinngemäß beobachtet: *„Der ehemalige **Hochschuldozent** verfügt über 30 Jahre
Praxiserfahrung."*

„Dozent" ist eine der namentlich erfassten Lehrtätigkeiten. In der Vita platziert, legt
die Formulierung eine **Kontinuität** nahe: Wer als Dozent begonnen hat und heute
„Trainings" anbietet, tut aus Prüfersicht dasselbe wie früher.

→ Entweder streichen oder klar als **abgeschlossene** Episode markieren und die
Praxiserfahrung in den Vordergrund stellen:
*„Nach einer frühen Station in der Hochschullehre seit über 30 Jahren ausschließlich in
der Praxis: Transformationsprojekte in 40 Ländern für deutsche, amerikanische und
französische Unternehmen."*
Das Wort „ausschließlich" trägt hier die Argumentation.

### F-08 — „Teilnehmer … in ihrem Lernprozess" · **Risiko: hoch**

Sinngemäß beobachtet: *„…begleiten wir die **Teilnehmer** in ihrem **Lernprozess**"* und
*„unterstützt Transformationsagenten, Moderatoren, Führungskräfte und Teams in ihren
**Lernprozessen**"*.

Das ist die ungünstigste Formulierung auf der ganzen Website: „Teilnehmer" + „Lernprozess"
beschreibt exakt die Lehr-/Lernsituation, auf die § 2 abstellt. Sie ist doppelt
problematisch, weil sie an mehreren Stellen wiederholt wird und dadurch das Gesamtbild prägt.

→ *„…begleiten wir **den Führungskreis** in seinem **Veränderungs- und
Entscheidungsprozess**."* Die Wörter „Teilnehmer" und „Lernprozess" sollten auf der
gesamten Website nicht mehr vorkommen.

### F-09 — „Werkzeuge und Techniken vermitteln" / „Wissen geben" · **Risiko: hoch**

Sinngemäß beobachtet: *„Die Trainings geben den Teilnehmern **Werkzeuge und Techniken**,
um die Herausforderungen als moderne Führungskraft zu meistern"* und *„vermittelt
Führungskräften wertvolles **Wissen**, um überholte Verhaltensmuster zu optimieren"*.

„Vermitteln" + „Wissen" ist der Wortlaut des Tatbestands. Auch „Werkzeuge und Techniken"
entspricht „Fähigkeiten und Fertigkeiten".

Der eigene Hinweis, dass Werkzeuge *für einen Managementprozess* bereitgestellt werden und
nicht um ihrer selbst willen, ist inhaltlich genau richtig — er steht aber so nicht im Text.
Er muss ausdrücklich hinein:

→ *„Wir arbeiten mit den Instrumenten, die der jeweilige Steuerungsprozess erfordert —
nicht, um sie zu erlernen, sondern um damit die anstehenden Entscheidungen zu treffen.
Die Instrumente bleiben im Unternehmen, weil sie dort in der laufenden Steuerung
eingesetzt werden."*

### F-10 — Werkzeugkatalog „OKR, digitale Whiteboards, Kanban" · **Risiko: mittel**

Eine Aufzählung von Methoden neben dem Wort „Lernprozess" liest sich als
Kursinhaltsverzeichnis.

→ Methoden nicht als Angebotsinhalt aufzählen, sondern als Mittel im Mandat erwähnen:
*„Welche Steuerungsinstrumente eingesetzt werden — OKR, Kanban, andere — ergibt sich aus
der Ausgangslage; es ist Ergebnis der Analyse, nicht deren Voraussetzung."*

### F-11 — „Training" als eigene Angebotssäule · **Risiko: hoch**

Die Seite `tomklein.de/training/` macht Training zu einer der Hauptleistungen. Solange
diese Säule existiert, ist der Schwerpunktvortrag angreifbar: Die Website selbst benennt
Lehre als eigenständiges Produkt.

→ Säule auflösen und ihren berechtigten Kern als **Befähigung innerhalb des Mandats**
in die Beratungsseite integrieren (Vorlage in `04`). Wenn eine eigene Seite bleiben soll:
„Umsetzungsbegleitung" oder „Befähigung im Projekt".

---

## C. Vorhandene Stärken, die ausgebaut werden sollten

Die Website enthält bereits Elemente, die klar auf die Beratungsseite zeigen. Sie sind
derzeit nur schwächer platziert als die Risikoelemente.

- **Einzelcoaching als Reflexionsraum.** Sinngemäß beobachtet: Coaching gibt
  Führungsteams *„Zeit zur Reflexion"*, um Digitalisierung und Globalisierung mit Blick
  auf *die eigenen Ziele* und *das eigene Unternehmen* zu bearbeiten. Das ist
  lehrbuchmäßige Beratung: individuelles Anliegen, konkreter Anwendungszweck, kein
  übertragbares Wissen. — Nur eben unter `/kurse/` abgelegt (F-01).
- **Prozessbegleitung als Selbstbild.** „facilitating, guiding and supporting
  transformational processes" beschreibt Begleitung, nicht Unterricht.
- **Projektnachweis.** Transformationsvorhaben in 40 Ländern, Begleitung globaler
  Management-Meetings — das ist Mandatsarbeit und gehört prominent nach vorn.
- **Netzwerkstruktur.** Ein Netzwerk erfahrener Kolleginnen und Kollegen, das seit Jahren
  gemeinsam in Projekten arbeitet, unterstreicht Projekt- statt Kursgeschäft.

---

## D. Offener Teil — was für den vollständigen Durchgang fehlt

Für die seitengenaue Überarbeitung werden die **Volltexte** folgender Seiten benötigt
(deutsch und englisch):

1. Startseite `/` und `/en/`
2. Über mich / Vita
3. `/training/`
4. `/kurse/einzelcoaching/` und alle `/course/`- bzw. `/courses/`-Seiten
5. `/shop/businesscoaching/`, `/en/booking/`
6. `/en/lessons/topics-2/`
7. Inhalte von `online.tomklein.de`
8. Leistungs-, Referenz- und Kontaktseiten
9. Impressum (Tätigkeitsbeschreibung) und ggf. AGB
10. Blog-/Artikelseiten, soweit sie Angebote beschreiben

Sinnvollerweise zusätzlich, weil die DRV sie ebenfalls heranzieht: **LinkedIn-Profil**,
Angebots- und Rechnungsmuster, Gewerbeanmeldung bzw. Tätigkeitsbeschreibung beim Finanzamt
(siehe `05`).

Sobald die Texte vorliegen, wird dieses Dokument um eine Tabelle
*Seite → Fundstelle → Originalsatz → Neufassung* ergänzt.
