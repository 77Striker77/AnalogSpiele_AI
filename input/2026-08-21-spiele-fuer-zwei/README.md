# Spiele für Zwei

Einseitige Übersicht analoger Spiele für zwei – siebzehn Titel,
sechs kooperative und elf kompetitive.

## Spiel

- **Titel:** kein einzelnes – eine Auswahl von siebzehn Spielen
- **Art:** Brettspiele, Kartenspiele, ein Würfelspiel
- **Spieler:** zu zweit spielbar, viele auch für größere Runden;
  einzige Ausnahme ist Köder, das auf mehr Mitspieler ausgelegt ist
- **Dauer:** 10–60 Min je nach Titel
- **Preise:** 11,67 € bis 37,80 €, Stand 21.08.2026

## Punkte

Jedes Spiel trägt vier Zahlen von 0 bis 100, aus vier Richtungen gemessen:

- **Kritik** — Redaktionswertung von H@LL9000 (Skala 1–6), linear gestreckt.
  Liegt für 13 der 17 Titel vor.
- **Community** — BoardGameGeek-Nutzerschnitt, nach Stimmenzahl gedämpft, plus
  H@LL9000-Leserwertung mit einem Viertel Gewicht. Liegt für alle 17 vor.
- **Zu zweit** — aus der BGG-Spielerzahl-Umfrage: beste Besetzung 100, eine von
  mehreren besten 88, nur empfohlen 62, weder noch 28. Bei reinen Duellspielen
  ist die 100 trivial; solche Titel sind gedämpft dargestellt.
- **Unterwegs** — Packmaß aus Schachtelmaßen und Gewicht (brettspielversand.de):
  `100 − 75 × log₁₀(Liter ÷ 0,6)`, plus Abzug ab 500 g. Liegt für 16 der 17 vor.
  Die benötigte Tischfläche misst diese Zahl nicht — die steht in der Zeile
  *Reisetauglich* auf den Karten.

Die Zahlen sind nicht untereinander vergleichbar, nur innerhalb ihrer
Spalte. Formeln, Rohwerte und alle Quellen stehen im Reiter *Punkte & Quellen*
der Seite selbst.

## Was das Artefakt tut

Eine Seite mit zwei Reitern. Der erste stellt siebzehn Spiele in zwei Blöcken
gegenüber:
*Miteinander* (kooperativ) und *Gegeneinander* (kompetitiv). Jede Karte trägt
eine Metatabelle (Spieler, Alter, Dauer, Verlag, Reisetauglichkeit, Preis),
eine Beschreibung, den vollständigen Schachtelinhalt, je ein Pro und Contra
aus Reviews und einen Link zum Preisvergleich.

Über den Blöcken lässt sich die Reihenfolge umschalten: nach Community, nach
Kritik, nach Zwei-Personen-Tauglichkeit oder zurück in die ursprüngliche
Anordnung. Der zweite Reiter erklärt die
Punkte und listet die Quellen. Beide Reiter sind ohne Scrollen erreichbar.

Die Cover sind gezeichnet – siebzehn Illustrationen als Inline-SVG, ohne ein
einziges Bitmap. Liegt eine echte Coverdatei in `covers/`, ersetzt sie die
Zeichnung; fehlt sie, entfernt sich das `<img>` selbst und die Zeichnung
bleibt stehen.

## Enthaltene Spiele

**Miteinander:** MicroMacro: Crime City · Codenames Duett · Die Crew: Mission
Tiefsee · Paleo · Hanabi · Pandemie

**Gegeneinander:** 7 Wonders Duel · Splendor Duel · Targi · Patchwork ·
Schotten Totten · Hive Pocket · Mindbug · Compile: Main 1 · Agent Avenue ·
Revolver Noir · Köder

## Woher

- **Chat:** Claude-Chat, Artefakt als einzelne HTML-Datei
- **Stand:** 2026-08-21, am selben Tag um fünf Titel erweitert
  (Mindbug, Compile, Agent Avenue, Revolver Noir, Köder)

## Offen

- Die siebzehn Cover unter `covers/` sind nicht dabei – die Seite läuft ohne sie.
  Der Abschnitt weiter unten nennt nur die ersten zwölf Dateinamen; für die
  Nachzügler gilt `mindbug.jpg`, `compile.jpg`, `agent-avenue.jpg`,
  `revolver-noir.jpg`, `koeder.jpg`
- Köder ist ein Spiel für zwei bis fünf Personen und steht als einziger Titel
  nicht wegen, sondern trotz seiner Spielerzahl in der Liste; das gleichzeitige
  Bieten verliert zu zweit an Reiz. Auf der Karte ist das vermerkt
- Für Paleo, Compile, Revolver Noir und Köder gibt es keine Redaktionswertung;
  sie zeigen bei *Kritik* einen Strich und stehen beim Sortieren danach am Ende
- Die Crew: Mission Tiefsee führt bei Kritik und Community, ist zu zweit laut
  BGG-Umfrage aber weder beste noch empfohlene Besetzung (28 von 100). Der
  Titel bleibt in der Liste, die Zahl sagt aber deutlich, was Sache ist
- Für Revolver Noir gibt kein Shop Schachtelmaße her; *Unterwegs* bleibt dort leer
- Wertungen und Preise veralten; Stand ist durchgehend der 21.08.2026

---

*Der folgende Teil stammt unverändert aus dem Chat.*

## Auf GitHub Pages veröffentlichen

1. Auf github.com einloggen → **New repository**
   - Name z. B. `spiele-fuer-zwei`
   - Sichtbarkeit **Public** (bei Free-Accounts ist Pages nur für
     öffentliche Repos verfügbar)
   - **Create repository**
2. Im leeren Repo auf **uploading an existing file** klicken und
   `index.html` (und optional diese `README.md`) hineinziehen →
   **Commit changes**
3. **Settings** → linke Spalte **Pages**
   - Source: *Deploy from a branch*
   - Branch: `main`, Ordner `/ (root)` → **Save**
4. Ein bis zwei Minuten warten. Die Seite liegt dann unter:
   `https://<dein-benutzername>.github.io/spiele-fuer-zwei/`

Diesen Link kannst du verschicken – er funktioniert auf Handy und
Desktop, ohne dass jemand etwas installieren muss.

## Alternative ohne Repo

Wenn es schneller gehen soll: Datei auf **gist.github.com** einfügen,
Gist erstellen, dann die Gist-URL auf **htmlpreview.github.io**
vorschalten. Kein Repo, keine Pages-Einstellungen – dafür eine
hässlichere URL.

## Echte Cover ergänzen (optional)

Neben `index.html` einen Ordner `covers/` anlegen und die Bilder als
`micromacro.jpg`, `codenames.jpg`, `die-crew.jpg`, `paleo.jpg`,
`hanabi.jpg`, `pandemie.jpg`, `7-wonders-duel.jpg`,
`splendor-duel.jpg`, `targi.jpg`, `patchwork.jpg`,
`schotten-totten.jpg`, `hive.jpg` ablegen. Vorhandene Bilder ersetzen
automatisch die gezeichneten Kacheln, fehlende fallen darauf zurück.

## Quellen

Bestenlisten und Reviews u. a. von abenteuer-brettspiele.de,
heldenderfreizeit.com, spiele.tips, reich-der-spiele.de, hall9000.de,
brettspiel-news.de sowie BoardGameGeek-Community-Wertungen.
Preise: brettspiel-angebote.de, Stand 21.08.2026.
