# AnalogSpiele_AI

Eine KI-Umgebung für analoge Spiele - Brettspiele, Kartenspiele, Würfelspiele,
Rollenspiele. Was in Claude-Chats an Spielhilfen, Punktezählern, Regelübersichten
und Auswertungen entsteht, landet hier, wird geprüft und aufbewahrt.

## Was hier liegt

| Ordner | Zweck |
| --- | --- |
| [input/](input/) | Ablagebereich für HTML-Artefakte und READMEs aus dem Chat |
| [werkzeug/](werkzeug/) | Prüf- und Hilfsskripte, Python 3 ohne Fremdpakete |
| [docs/](docs/) | Veröffentlichungsbereich für GitHub Pages, erzeugt |
| [.claude/](.claude/) | Agenten, Fähigkeiten und Befehle dieser Umgebung |

## Etwas ablegen

1. Ordner anlegen: `input/JJJJ-MM-TT-kurzname/`
2. HTML als `index.html` hineinlegen, README als `README.md`
3. Prüfen:

       python werkzeug/ablage_pruefen.py

Ausführlich in [input/LIESMICH.md](input/LIESMICH.md). Wer Claude Code nutzt,
sagt einfach `/ablage-aufnehmen` - dann läuft der Ablauf geführt ab.

## Veröffentlichen

    python werkzeug/veroeffentlichen.py

Kopiert jede fehlerfreie Ablage nach `docs/` und schreibt eine Startseite, die
alle verlinkt. Damit GitHub die Seiten ausliefert, muss unter *Settings → Pages*
die Quelle auf Branch `main`, Ordner `/docs` stehen.

## Stand

Input-Bereich und Veröffentlichung stehen. Als Nächstes: ein Katalog, der die
Ablagen inhaltlich erschließt (Spiel, Art, Spielerzahl, Dauer), damit sich die
Startseite filtern lässt.
