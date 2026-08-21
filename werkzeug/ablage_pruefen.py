#!/usr/bin/env python3
"""Prüft den Input-Bereich und schreibt eine Übersicht.

Geht jeden Ablage-Ordner in input/ durch, meldet fehlende Pflichtdateien,
liest Titel und Beschreibung heraus, prüft ob das HTML self-contained ist,
und schreibt input/UEBERSICHT.md.

    python werkzeug/ablage_pruefen.py
    python werkzeug/ablage_pruefen.py --streng
"""

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
INPUT = WURZEL / "input"
UEBERSICHT = INPUT / "UEBERSICHT.md"

# Hosts, die ein Claude-Artefakt laden darf - alles andere ist ein Verstoß.
ERLAUBTE_HOSTS = {"fonts.googleapis.com", "fonts.gstatic.com"}

# Tag -> Attribut, das eine Ressource nachlädt. <a href> fehlt hier bewusst:
# ein Link ist kein Request.
LADEND = {
    "link": "href",
    "script": "src",
    "img": "src",
    "image": "href",
    "iframe": "src",
    "frame": "src",
    "embed": "src",
    "source": "src",
    "track": "src",
    "video": "src",
    "audio": "src",
    "object": "data",
    "use": "href",
}

RE_CSS_URL = re.compile(r"""url\(\s*['"]?(https?:)?//([^)'"\s]+)""", re.I)
RE_JS_HOLT = re.compile(
    r"""(fetch|XMLHttpRequest|WebSocket|importScripts|EventSource)\s*\(\s*['"`](https?:)?//([^'"`]+)""",
    re.I,
)


class HtmlLeser(HTMLParser):
    """Zieht Titel und nachgeladene Ressourcen aus dem HTML."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.titel = ""
        self.h1 = ""
        self.extern = []          # (zeile, tag, url)
        self._sammle = None
        self._puffer = []

    def handle_starttag(self, tag, attrs):
        werte = dict(attrs)
        attr = LADEND.get(tag)
        if attr:
            url = (werte.get(attr) or "").strip()
            if url.startswith(("http://", "https://", "//")):
                self.extern.append((self.getpos()[0], tag, url))
        if (tag == "title" and not self.titel) or (tag == "h1" and not self.h1):
            self._sammle = tag
            self._puffer = []

    def handle_endtag(self, tag):
        if self._sammle == tag:
            text = " ".join("".join(self._puffer).split())
            if tag == "title" and not self.titel:
                self.titel = text
            elif tag == "h1" and not self.h1:
                self.h1 = text
            self._sammle = None
            self._puffer = []

    def handle_data(self, daten):
        if self._sammle:
            self._puffer.append(daten)


def host_von(url):
    ohne = url.split("//", 1)[-1]
    return ohne.split("/", 1)[0].split(":")[0].lower()


def lies(pfad):
    return pfad.read_text(encoding="utf-8", errors="replace")


def pruefe_html(pfad):
    """-> (titel, h1, [(schwere, text)])"""
    quelle = lies(pfad)
    leser = HtmlLeser()
    try:
        leser.feed(quelle)
        leser.close()
    except Exception as fehler:                     # kaputtes HTML soll nicht abbrechen
        return "", "", [("warnung", "HTML nicht vollständig lesbar: {}".format(fehler))]

    treffer = list(leser.extern)
    for fund in RE_CSS_URL.finditer(quelle):
        zeile = quelle.count("\n", 0, fund.start()) + 1
        treffer.append((zeile, "css url()", fund.group(0).split("url(", 1)[1].strip("'\" ")))
    for fund in RE_JS_HOLT.finditer(quelle):
        zeile = quelle.count("\n", 0, fund.start()) + 1
        treffer.append((zeile, fund.group(1), (fund.group(2) or "") + "//" + fund.group(3)))

    befunde = []
    for zeile, tag, url in sorted(treffer):
        kurz = url if len(url) <= 68 else url[:65] + "..."
        if host_von(url) in ERLAUBTE_HOSTS:
            befunde.append(("hinweis", f"Zeile {zeile}: {tag} lädt von Google Fonts - {kurz}"))
        else:
            befunde.append(("fehler", f"Zeile {zeile}: {tag} lädt extern - {kurz}"))
    if not leser.titel:
        befunde.append(("warnung", "kein <title> im HTML"))
    return leser.titel, leser.h1, befunde


def lies_readme(pfad):
    """-> (ueberschrift, einzeiler)

    Der Einzeiler ist der erste Absatz unter der Überschrift, zu einer Zeile
    zusammengezogen - ein umbrochener Satz soll in der Übersicht nicht
    mitten im Wort enden.
    """
    ueberschrift = ""
    absatz = []
    for roh in lies(pfad).splitlines():
        zeile = roh.strip()
        if not zeile:
            if absatz:
                break
            continue
        if not ueberschrift and zeile.startswith("#"):
            ueberschrift = zeile.lstrip("#").strip()
            continue
        if not ueberschrift:
            continue
        if zeile.startswith(("#", "---", "```", "|", "*Der folgende")):
            if absatz:
                break
            continue
        absatz.append(zeile)

    einzeiler = " ".join(absatz)
    if len(einzeiler) > 140:
        einzeiler = einzeiler[:137].rsplit(" ", 1)[0] + "..."
    return ueberschrift, einzeiler


def groesse(bytes_):
    if bytes_ >= 1024 * 1024:
        return f"{bytes_ / 1024 / 1024:.1f} MB"
    return f"{bytes_ / 1024:.1f} KB"


def pruefe_ablage(ordner):
    befund = {
        "name": ordner.name,
        "titel": "",
        "beschreibung": "",
        "html": None,
        "bytes": 0,
        "meldungen": [],       # (schwere, text)
        "beilagen": 0,
    }
    m = befund["meldungen"]

    htmls = sorted(p for p in ordner.glob("*.html") if p.is_file())
    readme = next((p for p in ordner.iterdir()
                   if p.is_file() and p.name.lower() in ("readme.md", "liesmich.md")), None)

    if not htmls:
        m.append(("fehler", "keine HTML-Datei - das Artefakt fehlt"))
    else:
        haupt = next((p for p in htmls if p.name.lower() == "index.html"), htmls[0])
        befund["html"] = haupt.name
        befund["bytes"] = haupt.stat().st_size
        if haupt.name.lower() != "index.html":
            m.append(("warnung", f"HTML heißt {haupt.name} - bitte in index.html umbenennen"))
        if len(htmls) > 1:
            m.append(("hinweis", f"{len(htmls)} HTML-Dateien im Ordner, geprüft wurde {haupt.name}"))
        titel, h1, befunde = pruefe_html(haupt)
        befund["titel"] = titel or h1
        m.extend(befunde)

    if readme is None:
        m.append(("fehler", "README.md fehlt"))
    else:
        ueberschrift, einzeiler = lies_readme(readme)
        befund["beschreibung"] = einzeiler or ueberschrift
        if not befund["titel"]:
            befund["titel"] = ueberschrift
        if not (einzeiler or ueberschrift):
            m.append(("warnung", "README.md ist leer"))

    beilagen = ordner / "beilagen"
    if beilagen.is_dir():
        befund["beilagen"] = sum(1 for p in beilagen.rglob("*") if p.is_file())

    if not re.match(r"^\d{4}-\d{2}-\d{2}-[a-z0-9-]+$", ordner.name):
        m.append(("hinweis", "Ordnername folgt nicht dem Muster JJJJ-MM-TT-kurzname"))

    befund["fehler"] = sum(1 for s, _ in m if s == "fehler")
    befund["warnungen"] = sum(1 for s, _ in m if s == "warnung")
    return befund


def schreibe_uebersicht(befunde):
    zeilen = [
        "# Übersicht Input-Bereich",
        "",
        "Erzeugt von `werkzeug/ablage_pruefen.py` - nicht von Hand bearbeiten.",
        "",
    ]
    if not befunde:
        zeilen += ["Noch keine Ablage. Anleitung steht in [LIESMICH.md](LIESMICH.md).", ""]
    else:
        zeilen += ["| Ablage | Titel | Beschreibung | HTML | Zustand |",
                   "| --- | --- | --- | --- | --- |"]
        for b in befunde:
            zustand = "vollständig" if not b["fehler"] else f"{b['fehler']} Fehler"
            if not b["fehler"] and b["warnungen"]:
                zustand = f"{b['warnungen']} Warnung(en)"
            html = f"{b['html']} - {groesse(b['bytes'])}" if b["html"] else "-"
            zeilen.append(
                f"| [{b['name']}]({b['name']}/) | {b['titel'] or '-'} | "
                f"{b['beschreibung'] or '-'} | {html} | {zustand} |"
            )
        zeilen.append("")

        offen = [b for b in befunde if b["meldungen"]]
        if offen:
            zeilen += ["## Anmerkungen", ""]
            for b in offen:
                zeilen.append(f"**{b['name']}**")
                zeilen.append("")
                for schwere, text in b["meldungen"]:
                    marke = {"fehler": "Fehler", "warnung": "Warnung", "hinweis": "Hinweis"}[schwere]
                    zeilen.append(f"- {marke}: {text}")
                zeilen.append("")
    UEBERSICHT.write_text("\n".join(zeilen), encoding="utf-8")


def main():
    zerleger = argparse.ArgumentParser(description="Prüft den Input-Bereich.")
    zerleger.add_argument("--streng", action="store_true",
                          help="Rückgabecode 1, sobald eine Ablage unvollständig ist")
    argumente = zerleger.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    if not INPUT.is_dir():
        print(f"Kein Input-Bereich unter {INPUT}")
        return 1

    ordner = sorted(p for p in INPUT.iterdir() if p.is_dir() and not p.name.startswith(("_", ".")))
    befunde = [pruefe_ablage(p) for p in ordner]

    print(f"\nAblage-Prüfung - {INPUT}\n")
    if not befunde:
        print("  Noch keine Ablage vorhanden.")
        print("  Anleitung: input/LIESMICH.md - Muster: input/_vorlage/\n")
    for b in befunde:
        zustand = "vollständig" if not b["fehler"] else "unvollständig"
        print(f"  {b['name']:<44} [{zustand}]")
        if b["titel"]:
            print(f"      Titel        {b['titel']}")
        if b["beschreibung"]:
            print(f"      README       {b['beschreibung']}")
        if b["html"]:
            laedt_extern = any(s == "fehler" and "lädt extern" in t for s, t in b["meldungen"])
            sauber = "lädt extern" if laedt_extern else "self-contained"
            print(f"      HTML         {b['html']}, {groesse(b['bytes'])}, {sauber}")
        if b["beilagen"]:
            print(f"      Beilagen     {b['beilagen']} Datei(en)")
        for schwere, text in b["meldungen"]:
            marke = {"fehler": "[x]", "warnung": "[!]", "hinweis": "[i]"}[schwere]
            print(f"      {marke} {text}")
        print()

    if befunde:
        heil = sum(1 for b in befunde if not b["fehler"])
        print(f"{len(befunde)} Ablage(n): {heil} vollständig, {len(befunde) - heil} mit Fehlern")
    schreibe_uebersicht(befunde)
    print(f"Übersicht geschrieben: {UEBERSICHT.relative_to(WURZEL)}\n")

    if argumente.streng and any(b["fehler"] for b in befunde):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
