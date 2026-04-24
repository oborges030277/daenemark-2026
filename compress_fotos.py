"""Einmalig ausfuehren: komprimiert die heruntergeladenen Fotos auf Web-Groesse.
Originale werden nach haus_fotos/_original/ verschoben, web-Version bleibt im Hauptordner.
"""
import os
from pathlib import Path
from PIL import Image

SRC = Path(__file__).parent / "haus_fotos"
ORIG = SRC / "_original"
ORIG.mkdir(exist_ok=True)

MAX_W = 1400
QUALITY = 82

for f in sorted(SRC.glob("foto_*.jpg")):
    dst_orig = ORIG / f.name
    if not dst_orig.exists():
        f.rename(dst_orig)
    with Image.open(dst_orig) as im:
        im = im.convert("RGB")
        w, h = im.size
        if w > MAX_W:
            im = im.resize((MAX_W, int(h * MAX_W / w)), Image.LANCZOS)
        im.save(SRC / f.name, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    print(f"{f.name}: {dst_orig.stat().st_size//1024} KB -> {(SRC/f.name).stat().st_size//1024} KB")

total = sum((SRC/p.name).stat().st_size for p in sorted(SRC.glob('foto_*.jpg')))
print(f"\nTotal web size: {total/1024/1024:.1f} MB (29 photos)")
