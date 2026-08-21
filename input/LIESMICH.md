# Input-Bereich

Hier landet alles, was aus einem Claude-Chat herauskommt: das HTML-Artefakt und die
zugehörige README. Ein Ordner pro Ablage — nichts direkt hier hineinlegen.

## Ablegen in drei Schritten

1. Ordner anlegen: `input/JJJJ-MM-TT-kurzname/`
   Beispiel: `input/2026-08-21-catan-punktezaehler/`
2. Das HTML-Artefakt aus dem Chat hineinkopieren, als `index.html`.
3. Die README aus dem Chat hineinkopieren, als `README.md`.

Fertig. Alles Weitere macht das Prüfwerkzeug.

## Was ein Ablage-Ordner enthält

    input/2026-08-21-catan-punktezaehler/
    ├── index.html      (Pflicht) das Artefakt, self-contained
    ├── README.md       (Pflicht) Beschreibung aus dem Chat
    └── beilagen/       (frei)    Screenshots, Notizen, Regel-PDFs, Rohdaten

`_vorlage/` ist das Muster zum Abgucken und Kopieren. Ordner, deren Name mit `_`
beginnt, ignoriert das Prüfwerkzeug.

## Namensregeln für den Ordner

- Datum voran, damit die Ablage chronologisch sortiert: `JJJJ-MM-TT-`
- Kurzname klein, mit Bindestrichen, keine Umlaute: `wuerfel` statt `würfel`
- Der Kurzname sagt, um welches Spiel oder welches Thema es geht

## Prüfen, was drin liegt

    python werkzeug/ablage_pruefen.py

Das Werkzeug geht jeden Ablage-Ordner durch, meldet fehlende Pflichtdateien,
liest Titel und Beschreibung heraus, prüft ob das HTML wirklich self-contained
ist (keine externen Requests) und schreibt `input/UEBERSICHT.md`.

    python werkzeug/ablage_pruefen.py --streng

Beendet sich mit Fehlercode, sobald eine Ablage unvollständig ist — für später,
wenn das automatisch laufen soll.
