"""Laedt passende Fotos fuer Straende, Ausfluege, Restaurants und Rastplaetze.

Strategie: fuer jede Ziel-URL das og:image (oder eine Wikipedia-Thumbnail-URL)
extrahieren, runterladen, auf ~1000 px Breite komprimieren.
"""
import os, re, sys, urllib.request, urllib.parse
from pathlib import Path
from PIL import Image
from io import BytesIO

ROOT = Path(__file__).parent
OUT  = ROOT / "content_fotos"
OUT.mkdir(exist_ok=True)

# Wikimedia verlangt eine aussagekraeftige User-Agent mit Kontakt.
UA = {"User-Agent": "Urlaub2026DaenemarkSite/1.0 (private planning page; oborges03021977@gmail.com)"}
MAX_W = 1100
QUALITY = 82


def fetch(url, binary=False):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read()
    return data if binary else data.decode("utf-8", errors="ignore")


def og_image(url):
    html = fetch(url)
    m = re.search(
        r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html
    ) or re.search(
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html
    )
    if not m:
        m = re.search(
            r'<meta[^>]+name=["\']twitter:image["\'][^>]+content=["\']([^"\']+)["\']', html
        )
    if not m:
        # Fallback: suche ein grosses <img> im Hauptinhalt
        for cand in re.findall(r'<img[^>]+src=["\']([^"\']+\.(?:jpg|jpeg|png|webp))["\']', html, flags=re.I):
            if "logo" in cand.lower() or "icon" in cand.lower() or "pixel" in cand.lower():
                continue
            m_url = cand
            break
        else:
            return None
        img_url = m_url
    else:
        img_url = m.group(1)
    if img_url.startswith("//"):
        img_url = "https:" + img_url
    elif img_url.startswith("/"):
        p = urllib.parse.urlparse(url)
        img_url = f"{p.scheme}://{p.netloc}{img_url}"
    return img_url


def save_image(img_url, filename):
    path = OUT / filename
    if path.exists():
        print(f"  ok  {filename} (vorhanden)")
        return True
    try:
        raw = fetch(img_url, binary=True)
        im = Image.open(BytesIO(raw)).convert("RGB")
        w, h = im.size
        if w > MAX_W:
            im = im.resize((MAX_W, int(h * MAX_W / w)), Image.LANCZOS)
        im.save(path, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        print(f"  DL  {filename}  ({path.stat().st_size//1024} KB)")
        return True
    except Exception as e:
        print(f"  !!  {filename}: {e}")
        return False


def try_og(slug, page_url):
    print(f"{slug}:  {page_url}")
    try:
        img = og_image(page_url)
    except Exception as e:
        print(f"  !!  og-fetch: {e}")
        return False
    if not img:
        print(f"  --  kein og:image")
        return False
    return save_image(img, f"{slug}.jpg")


def try_direct(slug, img_url):
    print(f"{slug}:  {img_url}")
    return save_image(img_url, f"{slug}.jpg")


# --------------------------------------------------------------------------
# Alle Foto-Quellen - URL zeigt entweder auf eine Seite mit og:image oder
# direkt auf ein Bild (Wikimedia Commons).
# Commons-Bilder sind CC-Lizenz, og:images sind teils Werbefotos der
# offiziellen Betreiber (fuer private Planungsseite mit noindex ok).
# --------------------------------------------------------------------------

SOURCES_OG = {
    # Strände
    "strand_henne":       "https://www.visitvesterhavet.com/northsea/north-sea-vacation/henne-beach-gdk609603",
    "strand_blaavand":    "https://www.visitblaavand.dk/blaavand/oplevelser/badestrande/blaavand-strand-gdk603137",
    "strand_vejers":      "https://en.wikipedia.org/wiki/Vejers_Strand",
    # Ausflüge
    "tirpitz":            "https://tirpitz.dk/",
    "blaavandshuk_fyr":   "https://en.wikipedia.org/wiki/Bl%C3%A5vandshuk_Lighthouse",
    "ribe":               "https://en.wikipedia.org/wiki/Ribe",
    "fimus":              "https://en.wikipedia.org/wiki/Fisheries_and_Maritime_Museum",
    "mennesket":          "https://en.wikipedia.org/wiki/Man_Meets_the_Sea",
    "fanoe":              "https://en.wikipedia.org/wiki/Fan%C3%B8",
    "filsoe":             "https://en.wikipedia.org/wiki/Fils%C3%B8",
    "legoland":           "https://en.wikipedia.org/wiki/Legoland_Billund_Resort",
    # Restaurants
    "henne_kirkeby_kro":  "https://hennekirkebykro.dk/",
    "strandgaarden":      "https://www.strandgaarden-henne.dk/",
    "sloejfen":           "https://sloejfen.dk/",
    # Raststätten
    "rs_dammer":          "https://www.serways.de/standorte/dammer-berge-ost/",
    "rs_grundbergsee":    "https://www.serways.de/standorte/grundbergsee-sued/",
    "rs_bockel":          "https://autohof-bockel.de/",
    "rs_huettener":       "https://www.raststaetten.de/standorte/huettener-berge-ost/",
}

# Zusaetzliche og-Quellen fuer Dinge ohne direkte Seite.
# Wenn auch hier nichts klappt: Card bleibt mit Emoji-Placeholder.
SOURCES_OG_EXTRA = {
    # Strände
    "strand_nymindegab":  "https://en.wikipedia.org/wiki/Nymindegab",
    "strand_houstrup":    "https://www.visitvesterhavet.com/northsea/north-sea-vacation/houstrup-beach-gdk609604",
    # Ausflüge
    "tirpitz":            "https://en.wikipedia.org/wiki/Tirpitz_Museum_(Denmark)",
    "blaavandshuk_fyr":   "https://en.wikipedia.org/wiki/Bl%C3%A5vandshuk_Fyr",
    "filsoe":             "https://da.wikipedia.org/wiki/Fils%C3%B8",
    "fimus":              "https://www.fimus.dk/",
    "mennesket":          "https://en.wikipedia.org/wiki/Man_Meets_the_Sea",
    "legoland":           "https://en.wikipedia.org/wiki/Legoland_Billund",
    # Restaurants
    "henne_kirkeby_kro":  "https://en.wikipedia.org/wiki/Henne_Kirkeby_Kro",
}


if __name__ == "__main__":
    for slug, url in SOURCES_OG.items():
        try_og(slug, url)
    print()
    for slug, url in SOURCES_OG_EXTRA.items():
        # nur versuchen, wenn noch nichts da ist
        if not (OUT / f"{slug}.jpg").exists():
            try_og(slug, url)
    print()
    n = len(list(OUT.glob("*.jpg")))
    print(f"Total images in {OUT.name}/: {n}")
    for f in sorted(OUT.glob("*.jpg")):
        print(f"  {f.name}")
