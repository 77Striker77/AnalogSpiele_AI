---
name: ablage-aufnehmen
description: Nimmt ein HTML-Artefakt und eine README aus einem Claude-Chat in den Input-Bereich auf - legt den Ablage-Ordner an, benennt die Dateien richtig, prüft auf externe Requests und fehlende Angaben. Nutzen bei "ich habe was aus dem Chat", "leg das ab", "neue Ablage", "nimm das Artefakt auf", oder wenn eine lose HTML-Datei einsortiert werden soll.
---

# Ablage aufnehmen

Ziel: aus einer losen HTML plus README eine vollständige, geprüfte Ablage in
`input/` machen.

## Ablauf

### 1. Material einsammeln

Klären, wo HTML und README gerade liegen. Übliche Fälle:

- Dateien liegen schon im Projektordner oder im Download-Ordner
- Der Inhalt steht im Chat und wird eingefügt
- Nur die HTML ist da, die README fehlt noch

Fehlt die README ganz, wird sie in Schritt 4 aus dem Artefakt geschrieben - nicht
danach fragen, sondern einen Entwurf vorlegen.

### 2. Ordnernamen bestimmen

Muster: `input/JJJJ-MM-TT-kurzname/`

- Datum: heute, oder das Datum des Chats, wenn es genannt wird
- Kurzname: klein, Bindestriche, keine Umlaute (`wuerfel`, nicht `würfel`)
- Der Kurzname benennt Spiel oder Thema: `catan-punktezaehler`, `wuerfel-wahrscheinlichkeiten`

Existiert der Ordner schon, nachfragen: ersetzen oder als neue Fassung danebenlegen.

### 3. Dateien ablegen

    input/JJJJ-MM-TT-kurzname/
    ├── index.html      das Artefakt, immer unter diesem Namen
    ├── README.md       die Beschreibung
    └── beilagen/       nur anlegen, wenn es wirklich Beilagen gibt

Heruntergeladene Artefakte heißen oft anders - in `index.html` umbenennen, nicht
kopieren und das Original liegen lassen.

### 4. README füllen

Aufbau siehe `input/_vorlage/README.md`. Titel, Einzeiler, Spielangaben (Titel,
Art, Spielerzahl, Dauer), was das Artefakt tut, Herkunft, offene Punkte.

Was sich aus dem HTML ablesen lässt, selbst ausfüllen: `<title>`, `<h1>`, sichtbare
Beschriftungen, Spielernamen-Felder, Rundenzahlen. Nur das erfragen, was wirklich
nirgends steht - und dann alles auf einmal, nicht Frage für Frage.

### 5. Prüfen

    python werkzeug/ablage_pruefen.py

Jeden `[x]`-Befund abarbeiten, bis die Ablage `vollständig` meldet:

- **lädt extern** - der häufigste Fall. Ein Artefakt darf nichts nachladen.
  CDN-Skript durch Inline-Code ersetzen, entferntes Bild als `data:`-URI einbetten.
  Google Fonts ist erlaubt und erscheint nur als `[i]`.
- **kein `<title>`** - Titel ergänzen, er benennt das Artefakt in der Übersicht.
- **README.md fehlt** - zurück zu Schritt 4.

`[i]`-Hinweise sind Beobachtungen, kein Auftrag.

### 6. Zurückmelden

Kurz sagen: Ordner, Titel, Größe, was am Artefakt geändert wurde. Nicht die
Übersichtstabelle wiederholen - sie steht in `input/UEBERSICHT.md`.

## Grenzen

Dieser Ablauf sortiert ein und prüft die Form. Er beurteilt weder die Gestaltung
des Artefakts noch den Spielinhalt. Für eine gestalterische Bewertung ist der
Agent `design:design-gutachter` da, für Metadaten und Einordnung `spiel-archivar`.
