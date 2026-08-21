# AnalogSpiele_AI

KI-Umgebung rund um analoge Spiele: Brett-, Karten-, Würfel- und Rollenspiele.
Ausgangsmaterial sind HTML-Artefakte und READMEs, die in Claude-Chats entstehen.

## Aufbau

    input/       Ablagebereich - ein Ordner je Artefakt aus dem Chat
    werkzeug/    Prüf- und Hilfsskripte (Python 3, ohne Fremdpakete)
    .claude/     Agenten, Fähigkeiten, Befehle für diese Umgebung

## Ablage-Muster

Jede Ablage ist ein eigener Ordner `input/JJJJ-MM-TT-kurzname/` mit `index.html`
(Pflicht), `README.md` (Pflicht) und optional `beilagen/`. Alles Weitere steht in
[input/LIESMICH.md](input/LIESMICH.md).

`input/UEBERSICHT.md` wird erzeugt, nie von Hand bearbeitet.

## Regeln für Artefakte

Ein HTML in `input/` ist ein Claude-Artefakt und muss self-contained sein: CSS und
JS inline, Bilder als `data:`-URI, keine CDN-Skripte, keine entfernten Bilder. Der
einzige erlaubte Fremdhost ist Google Fonts. Externe Links (`<a href>`) sind in
Ordnung - sie laden nichts nach.

## Werkzeuge

    python werkzeug/ablage_pruefen.py            prüft input/, schreibt UEBERSICHT.md
    python werkzeug/ablage_pruefen.py --streng   Rückgabecode 1 bei Mängeln

Nach jeder Änderung an `input/` das Prüfwerkzeug laufen lassen, damit
`UEBERSICHT.md` stimmt.

## Sprache

Alles auf Deutsch: Ordnernamen, Bezeichner in Skripten, Kommentare, Ausgaben,
Commit-Nachrichten. Ordnernamen ohne Umlaute (`wuerfel`, nicht `würfel`), Texte mit.

## Skripte

Python 3 aus der Standardbibliothek, keine Abhängigkeiten. Wer eine Fremdbibliothek
braucht, begründet sie vorher.
