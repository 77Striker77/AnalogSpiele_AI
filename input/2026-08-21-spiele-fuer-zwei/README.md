# Spiele für Zwei

Übersicht analoger Spiele für zwei – zwanzig Titel, sechs kooperative
und vierzehn kompetitive, gegliedert in fünf Bereiche mit Menüführung.

## Spiel

- **Titel:** kein einzelnes – eine Auswahl von zwanzig Spielen
- **Art:** Brettspiele, Kartenspiele, ein Würfelspiel
- **Spieler:** zu zweit spielbar, viele auch für größere Runden;
  einzige Ausnahme ist Köder, das auf mehr Mitspieler ausgelegt ist
- **Dauer:** 10–60 Min je nach Titel
- **Preise:** 11,67 € bis 37,80 €, Stand 21.08.2026

## Punkte

Jedes Spiel trägt vier Zahlen von 0 bis 100, aus vier Richtungen gemessen:

- **Kritik** — Redaktionswertung von H@LL9000 (Skala 1–6), linear gestreckt.
  Liegt für 15 der 20 Titel vor.
- **Community** — BoardGameGeek-Nutzerschnitt, nach Stimmenzahl gedämpft, plus
  H@LL9000-Leserwertung mit einem Viertel Gewicht. Liegt für alle 20 vor.
- **Zu zweit** — aus der BGG-Spielerzahl-Umfrage: beste Besetzung 100, eine von
  mehreren besten 88, nur empfohlen 62, weder noch 28. Bei reinen Duellspielen
  ist die 100 trivial; solche Titel sind gedämpft dargestellt.
- **Unterwegs** — Packmaß aus Schachtelmaßen und Gewicht (brettspielversand.de):
  `100 − 75 × log₁₀(Liter ÷ 0,6)`, plus Abzug ab 500 g. Liegt für 17 der 20 vor.
  Die benötigte Tischfläche misst diese Zahl nicht — die steht in der Zeile
  *Reisetauglich* auf den Karten.

Die Zahlen sind nicht untereinander vergleichbar, nur innerhalb ihrer
Spalte. Formeln, Rohwerte und alle Quellen stehen im Reiter *Punkte & Quellen*
der Seite selbst.

## Was das Artefakt tut

Eine Seite mit fünf Bereichen, zwischen denen eine Menüleiste umschaltet –
jeder ohne Scrollen erreichbar:

| Bereich | Inhalt |
| --- | --- |
| **Start** | Kennzahlen, die Spitzenreiter je Skala, Einstiege in die Bereiche |
| **Miteinander** | 6 kooperative Titel als Karten |
| **Gegeneinander** | 14 Duelle als Karten |
| **Rangliste** | alle 20 in einer Tabelle, je Spalte sortierbar; ein Klick auf den Spielnamen führt zur Karte |
| **Punkte & Quellen** | Methode, Formeln, Rohwerte, Quellenliste |

Jede Karte trägt eine Metatabelle (Spieler, Alter, Dauer, Verlag,
Reisetauglichkeit, Preis), die vier Punktzahlen mit ihren Belegen, eine
Beschreibung, den vollständigen Schachtelinhalt, je ein Pro und Contra aus
Rezensionen, einen Link zum Preisvergleich und ein Regelvideo.

In den beiden Kartenbereichen lässt sich die Reihenfolge nach jeder der vier
Skalen umschalten oder in die ursprüngliche Anordnung zurücksetzen.

Die Cover sind gezeichnet – zwanzig Illustrationen als Inline-SVG, ohne ein
einziges Bitmap. Liegt eine echte Coverdatei in `covers/`, ersetzt sie die
Zeichnung; fehlt sie, entfernt sich das `<img>` selbst und die Zeichnung
bleibt stehen.

## Videos

Zu jedem der zwanzig Titel ist ein Regelvideo verlinkt, gesucht über die
YouTube-Trefferliste und zweifach geprüft: Der Videotitel muss den Spielnamen
enthalten, und die oembed-Schnittstelle muss das Video als abrufbar melden.
Achtzehn sind deutschsprachig. Bei Schotten Totten und Hive steht ein
englisches *How to Play* – die deutschen Treffer führten zum Nachfolger
beziehungsweise zu einer anderen Ausgabe, und ein englisches Video zum
richtigen Spiel ist besser als ein deutsches zum falschen.

## Enthaltene Spiele

**Miteinander:** Codenames Duett · Pandemie · Paleo · MicroMacro: Crime City ·
Der Fuchs im Wald: Duett · Hanabi

**Gegeneinander:** 7 Wonders Duel · Splendor Duel · Watergate · Targi ·
Hive Pocket · Patchwork · Compile: Main 1 · Mindbug · Schotten Totten ·
Jaipur · Agent Avenue · Revolver Noir · Lost Cities: Das Duell · Köder

## Woher

- **Chat:** Claude-Chat, Artefakt als einzelne HTML-Datei
- **Stand:** 2026-08-21; am selben Tag um fünf Titel erweitert (Mindbug,
  Compile, Agent Avenue, Revolver Noir, Köder), danach um vier weitere
  (Der Fuchs im Wald: Duett, Jaipur, Lost Cities: Das Duell, Watergate)
  bei gleichzeitiger Entfernung von Die Crew: Mission Tiefsee

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
- Die Crew: Mission Tiefsee wurde entfernt: höchste Redaktionswertung der
  Liste, aber zu zweit laut BGG-Umfrage weder beste noch empfohlene Besetzung
  (28 von 100) – ein gutes Spiel am falschen Platz
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
