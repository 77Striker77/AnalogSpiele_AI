#!/usr/bin/env python3
"""Stellt geprüfte Ablagen für GitHub Pages bereit.

Kopiert jede vollständige Ablage aus input/ nach docs/ - ohne Datum im Pfad,
damit die Adresse kurz bleibt - und erzeugt docs/index.html als Startseite.

    python werkzeug/veroeffentlichen.py
    python werkzeug/veroeffentlichen.py --trocken   zeigt nur, was passieren würde

Unvollständige Ablagen bleiben liegen. Was hier nicht auftaucht, ist im
Prüfwerkzeug zu klären.
"""

import argparse
import html
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ablage_pruefen import WURZEL, INPUT, pruefe_ablage, lies_readme   # noqa: E402

DOCS = WURZEL / "docs"


def kurzname(ordnername):
    """2026-08-21-spiele-fuer-zwei -> spiele-fuer-zwei"""
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", ordnername)


def datum(ordnername):
    treffer = re.match(r"^(\d{4})-(\d{2})-(\d{2})-", ordnername)
    return "{2}.{1}.{0}".format(*treffer.groups()) if treffer else ""


def startseite(eintraege):
    karten = []
    for e in eintraege:
        karten.append(
            '    <a class="karte" href="{ziel}/">\n'
            '      <h2>{titel}</h2>\n'
            '      <p>{text}</p>\n'
            '      <span class="fuss">{datum}</span>\n'
            '    </a>'.format(
                ziel=html.escape(e["ziel"]),
                titel=html.escape(e["titel"]),
                text=html.escape(e["text"]),
                datum=html.escape(e["datum"]),
            )
        )
    zahl = len(eintraege)
    leer = ('    <p class="leer">Noch nichts veröffentlicht.</p>'
            if not karten else "\n".join(karten))

    return """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AnalogSpiele &ndash; Spielhilfen und &Uuml;bersichten</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Public+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --filz:#20402F; --filz-tief:#17301F; --papier:#FBFAF5;
    --tinte:#23241F; --tinte-leise:#5C5E54; --gold:#C9A24B; --linie:#E3E1D6;
  }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{
    font-family:'Public Sans',system-ui,-apple-system,sans-serif;
    background:var(--filz);
    background-image:radial-gradient(ellipse at 50% -10%, #2A5039 0%, var(--filz) 55%, var(--filz-tief) 100%);
    background-attachment:fixed;
    color:var(--tinte); line-height:1.55; padding:0 16px 64px; min-height:100vh;
  }}
  .rahmen {{ max-width:900px; margin:0 auto; }}
  header {{ text-align:center; color:#F2EFE4; padding:56px 8px 40px; }}
  .ueberzeile {{
    display:inline-block; font-size:.75rem; letter-spacing:.22em;
    text-transform:uppercase; color:var(--gold); font-weight:700; margin-bottom:14px;
  }}
  h1 {{
    font-family:'Bricolage Grotesque',system-ui,sans-serif; font-weight:800; font-size:clamp(2rem,5.5vw,3.2rem);
    line-height:1.05; letter-spacing:-.01em;
  }}
  header p {{ max-width:620px; margin:16px auto 0; color:#C9D2C4; font-size:.95rem; }}
  .liste {{ display:grid; gap:18px; grid-template-columns:repeat(auto-fill,minmax(280px,1fr)); }}
  .karte {{
    display:block; background:var(--papier); border-radius:12px; padding:22px 24px;
    text-decoration:none; color:inherit; border:1px solid var(--linie);
    box-shadow:0 10px 24px rgba(0,0,0,.22);
    transition:transform .16s ease, box-shadow .16s ease;
  }}
  .karte:hover, .karte:focus-visible {{
    transform:translateY(-3px); box-shadow:0 16px 32px rgba(0,0,0,.3);
  }}
  .karte:focus-visible {{ outline:3px solid var(--gold); outline-offset:3px; }}
  .karte h2 {{ font-family:'Bricolage Grotesque',system-ui,sans-serif; font-size:1.15rem; line-height:1.25; margin-bottom:8px; }}
  .karte p {{ font-size:.9rem; color:var(--tinte-leise); }}
  .fuss {{
    display:block; margin-top:14px; font-size:.75rem; letter-spacing:.12em;
    text-transform:uppercase; color:var(--tinte-leise);
  }}
  .leer {{ color:#C9D2C4; text-align:center; padding:40px 0; }}
  footer {{ text-align:center; color:#8FA091; font-size:.8rem; margin-top:48px; }}
  footer a {{ color:var(--gold); }}
</style>
</head>
<body>
  <div class="rahmen">
    <header>
      <span class="ueberzeile">Analoge Spiele</span>
      <h1>Spielhilfen &amp; &Uuml;bersichten</h1>
      <p>Was am Spieltisch hilft: Auswahllisten, Punktez&auml;hler, Regel&uuml;bersichten.
      {zahl_text}</p>
    </header>
    <main class="liste">
{karten}
    </main>
    <footer>
      Erzeugt aus <a href="https://github.com/77Striker77/AnalogSpiele_AI">AnalogSpiele_AI</a>
    </footer>
  </div>
</body>
</html>
""".format(
        karten=leer,
        zahl_text=("Eine Seite." if zahl == 1 else f"{zahl} Seiten." if zahl else ""),
    )


def main():
    zerleger = argparse.ArgumentParser(description="Stellt geprüfte Ablagen für Pages bereit.")
    zerleger.add_argument("--trocken", action="store_true",
                          help="nur anzeigen, nichts schreiben")
    argumente = zerleger.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    ordner = sorted((p for p in INPUT.iterdir()
                     if p.is_dir() and not p.name.startswith(("_", "."))), reverse=True)

    eintraege, uebersprungen = [], []
    for p in ordner:
        befund = pruefe_ablage(p)
        if befund["fehler"]:
            uebersprungen.append((p.name, befund["fehler"]))
            continue
        _, einzeiler = lies_readme(p / "README.md")
        eintraege.append({
            "quelle": p,
            "ziel": kurzname(p.name),
            "titel": befund["titel"] or kurzname(p.name),
            "text": einzeiler or "",
            "datum": datum(p.name),
        })

    print(f"\nVeröffentlichen nach {DOCS}\n")
    for e in eintraege:
        print(f"  {e['quelle'].name}  ->  docs/{e['ziel']}/")
    for name, fehler in uebersprungen:
        print(f"  {name}  übersprungen, {fehler} Fehler")
    if not eintraege:
        print("  Nichts Vollständiges zum Veröffentlichen.")

    if argumente.trocken:
        print("\nTrockenlauf - nichts geschrieben.\n")
        return 0

    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir(parents=True)
    # Ohne .nojekyll wirft GitHub Pages Dateien mit Unterstrich weg.
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")

    for e in eintraege:
        ziel = DOCS / e["ziel"]
        shutil.copytree(e["quelle"], ziel, ignore=shutil.ignore_patterns("README.md"))

    (DOCS / "index.html").write_text(startseite(eintraege), encoding="utf-8")
    print(f"\n{len(eintraege)} Seite(n) bereitgestellt, Startseite geschrieben.")
    print("Pages muss auf Branch main, Ordner /docs stehen.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
