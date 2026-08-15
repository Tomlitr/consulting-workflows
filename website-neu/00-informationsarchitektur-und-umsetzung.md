# 00 – Informationsarchitektur, Slugs und Umsetzung

Vollständiger Neuaufbau von tomklein.de mit dem Ziel, das Gesamtbild der Website auf die
**Beratungsseite** des § 2 Satz 1 Nr. 1 SGB VI zu stellen (Begründung in
`../drv-risikoreview/`).

Die fertigen Texte stehen in `10-seiten-de.md` und `20-seiten-en.md`.

## 1. Zielstruktur

```
/                                   Startseite
/beratung/                          Beratung (Hauptsäule)
/beratung/transformationsvorhaben/  Leistungsfeld 1
/beratung/organisationsdesign/      Leistungsfeld 2
/beratung/umsetzungsbegleitung/     Leistungsfeld 3  ← ersetzt „Training"
/executive-coaching/                Executive Coaching
/mandate/                           Mandate & Referenzen
/ueber-mich/                        Über mich
/artikel/                           Artikel
/kontakt/                           Kontakt (Anfrage → Erstgespräch → Angebot)
/impressum/  /datenschutz/          Rechtliches
```

Englisch spiegelbildlich unter `/en/…` mit `services`, `executive-coaching`,
`engagements`, `about`, `articles`, `contact`.

**Navigationslabels:** Beratung · Executive Coaching · Mandate · Über mich · Artikel ·
Kontakt. Kein „Training", kein „Kurse", kein „Shop", kein „Booking".

## 2. Was entfällt und warum

| Entfällt | Grund | Ersatz |
|---|---|---|
| `/training/` | benennt Lehre als eigenes Produkt | `/beratung/umsetzungsbegleitung/` |
| `/kurse/*`, `/course/*`, `/courses/*` | Kurs-Taxonomie = Kernindiz | `/beratung/*`, `/mandate/*` |
| `/en/lessons/*` | „lesson" = Unterrichtseinheit | `/en/services/*` |
| `/shop/*` | Leistung als Kaufartikel | `/kontakt/` (Anfrage → Angebot) |
| `/en/booking/` | Buchung von Plätzen | `/en/contact/` (initial conversation) |
| `online.tomklein.de` | Selbstlernangebot ist strukturell Lehre | ✅ entschieden: ersatzlose Löschung (Abschnitt 6) |

## 3. Weiterleitungen (301)

Vor dem Umbau die vollständige URL-Liste ziehen (z. B. `wp-sitemap.xml` oder Yoast-Sitemap),
damit keine Seite unbeachtet bleibt. Grundmuster:

| Alt | Neu |
|---|---|
| `/training/` | `/beratung/umsetzungsbegleitung/` |
| `/kurse/einzelcoaching/` | `/executive-coaching/` |
| `/shop/businesscoaching/` | `/executive-coaching/` |
| `/course/organisationsentwicklung-fuer-die-vuca-welt/` | `/beratung/transformationsvorhaben/` |
| `/courses/compassionate-leadership/` | `/beratung/organisationsdesign/` |
| `/courses/team-retrospektive-mit-agilen-teams-praxisworkshop/` | `/beratung/umsetzungsbegleitung/` |
| `/course/`, `/kurse/` (Archive) | `/beratung/` |
| `/en/lessons/topics-2/` | `/en/services/` |
| `/en/booking/` | `/en/contact/` |

Alle übrigen `/course*`- und `/kurse*`-URLs pauschal auf `/beratung/`.

## 4. Technische Punkte in WordPress

1. **Kurs-Plugin entfernen oder stilllegen.** Solange LearnDash o. ä. aktiv ist, erzeugt
   es Post-Types, Archive, Sitemap-Einträge und Strukturdaten mit `course`/`lesson` —
   auch für Seiten, die im Menü nicht mehr auftauchen. Nach der Deaktivierung prüfen:
   `site:tomklein.de` in der Suche, XML-Sitemap, interne Suche.
2. **Seiten als normale WordPress-Seiten neu anlegen**, nicht als Kurs-Objekte.
3. **Permalinks** auf die Struktur aus Abschnitt 1 setzen, danach Permalinks einmal neu
   speichern.
4. **301-Weiterleitungen** setzen (Redirection-Plugin oder `.htaccess`).
5. **Sitemap neu einreichen** und in der Search Console die Entfernung der alten
   `/course/`-URLs beantragen, damit die Kurs-Slugs aus den Suchergebnissen verschwinden.
6. **Menü, Footer, Breadcrumbs, interne Verlinkungen** durchgehen — die alten Begriffe
   stehen oft noch in Widgets und Buttons.
7. **Bilder-Alt-Texte und Dateinamen** prüfen (z. B. `seminar-2019.jpg`); sie sind
   indexiert und lesbar.
8. **Meta-Titles und Descriptions** aus Abschnitt 5 eintragen.
9. **Strukturierte Daten:** kein `Course`-Schema, kein `EducationalOrganization`.
   Passend ist `ProfessionalService` bzw. `Person` mit `jobTitle: Unternehmensberater`.

## 5. Meta-Angaben

| Seite | Title | Description |
|---|---|---|
| `/` | Tom Klein – Beratung für Business Transformation | Beratung für Veränderungsvorhaben: Analyse der Ausgangslage, Zielbild, Umsetzung bis zur Wirksamkeit im Tagesgeschäft. |
| `/beratung/` | Beratung – Transformation, Organisationsdesign, Umsetzung | Beratungsleistungen für Unternehmen in Veränderungsvorhaben. Vorgehen, Leistungsfelder, Zusammenarbeit. |
| `/executive-coaching/` | Executive Coaching – Sparring für Führungsentscheidungen | Vertraulicher Reflexionsraum für Entscheidungen auf oberer Führungsebene. Kein Programm, keine festen Inhalte. |
| `/mandate/` | Mandate – Beratungsprojekte in der Praxis | Anonymisierte Beratungsmandate: Ausgangssituation, Vorgehen, Ergebnis. |
| `/ueber-mich/` | Tom Klein – Unternehmensberater für Transformation | Über 30 Jahre Praxis in Transformationsvorhaben, Projekte in 40 Ländern. |
| `/kontakt/` | Kontakt – Erstgespräch vereinbaren | Anfrage, Erstgespräch, Angebot. |

## 6. Zwei Entscheidungen, die vor dem Umbau zu treffen sind

**`online.tomklein.de`.** Ein Selbstlernangebot lässt sich nicht in Beratung umformulieren.
Drei Wege (mit der Rechtsberatung abzuwägen): einstellen bzw. auslaufen lassen · in eine
Kapitalgesellschaft ausgliedern · bewusst weiterführen und über einen dokumentiert kleinen
Umsatzanteil verteidigen. Solange die Subdomain unverändert online ist, bleibt der
schwerste Einzelbefund bestehen.

**Bestehende Formate mit Teilnehmern.** Wo Formate real als offene Veranstaltung mit
Teilnehmern stattfinden, ändert der neue Text nichts an der Sache. Entweder das Format
wird auf Mandatsarbeit umgestellt (Auftraggeber ist das Unternehmen, gearbeitet wird am
eigenen Fall) — oder es bleibt, was es ist, und wird in der Schwerpunktrechnung
mitgeführt.

## 7. Reihenfolge

1. Entscheidungen aus Abschnitt 6 treffen.
2. Angebots-, Vertrags- und Rechnungsvorlagen anpassen (`../drv-risikoreview/05-…`).
3. Seiten neu anlegen und Texte einsetzen.
4. Alte Seiten löschen, Kurs-Plugin stilllegen, Weiterleitungen setzen.
5. Menü, Footer, interne Links, Meta-Angaben, Sitemap.
6. LinkedIn und weitere Profile nachziehen.
7. Kontrolle: `site:tomklein.de` nach „Kurs", „Training", „Lektion", „Teilnehmer" durchsuchen.

## 8. Hinweis zu Platzhaltern

In den Texten stehen Angaben in eckigen Klammern — `[PRÜFEN: …]` und `[ERGÄNZEN: …]`.
Das sind Stellen, an denen ich Tatsachen über Ihre Arbeit nicht verifizieren konnte.
**Diese Stellen bitte nicht ungeprüft übernehmen:** Eine unzutreffende Leistungsbeschreibung
wäre in einem Prüfverfahren schädlicher als der bisherige Text.
