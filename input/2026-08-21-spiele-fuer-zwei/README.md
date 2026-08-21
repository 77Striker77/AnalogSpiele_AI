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

## Was das Artefakt tut

Eine statische Seite, die siebzehn Spiele in zwei Blöcken gegenüberstellt:
*Miteinander* (kooperativ) und *Gegeneinander* (kompetitiv). Jede Karte trägt
eine Metatabelle (Spieler, Alter, Dauer, Verlag, Reisetauglichkeit, Preis),
eine Beschreibung, den vollständigen Schachtelinhalt, je ein Pro und Contra
aus Reviews und einen Link zum Preisvergleich.

Die Cover sind gezeichnet – siebzehn Illustrationen als Inline-SVG, ohne ein
einziges Bitmap. Liegt eine echte Coverdatei in `covers/`, ersetzt sie die
Zeichnung; fehlt sie, entfernt sich das `<img>` selbst und die Zeichnung
bleibt stehen. Kein JavaScript, keine Interaktion.

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
- Preise und Verfügbarkeit veralten; Stand ist der 21.08.2026

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
