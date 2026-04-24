"""Build-Script fuer die Urlaubs-Website 'Urlaub 2026 - Daenemark'.

Gleiche Idee wie Kroatien-Projekt: erzeugt eine einzelne self-contained index.html.
Details (Unterkunft, Strasnde, Restaurants etc.) folgen noch - aktuell Platzhalter.
"""
import os

# --------------------------------------------------------------------------
# PLATZHALTER - werden spaeter durch echte Daten ersetzt
# --------------------------------------------------------------------------
TRIP_TITLE       = "Daenemark 2026"
TRIP_SUBTITLE    = "Unterkunft · Datum folgt"
COUNTDOWN_TARGET = "2026-07-01T15:00:00+02:00"   # TODO: Anreisedatum setzen
HERO_BG_URL      = ""                             # TODO: Foto-URL oder data-URI

ACCOMMODATION = {
    "name":      "TODO Unterkunft",
    "location":  "TODO Ort, Daenemark",
    "booking":   "#",       # z.B. FeWo-direkt / Airbnb Link
    "maps":      "#",       # Google-Maps Koordinaten
    "features":  [
        ("\U0001F3CA", "Pool / Sauna"),
        ("\U0001F6CF",  "Schlafzimmer"),
        ("\U0001F6C1", "Badezimmer"),
        ("\U0001F4CF", "Wohnflaeche"),
        ("\U0001F373", "Kueche"),
        ("\U0001F4F6", "WLAN"),
        ("\U0001F436", "Haustierfreundlich"),
        ("\U0001F33B", "Garten / Terrasse"),
    ],
    "rooms": [
        ("Schlafzimmer 1", "TODO Betten"),
        ("Schlafzimmer 2", "TODO Betten"),
        ("Wohnzimmer",     "TODO Schlafsofa"),
    ],
}

ROUTE = {
    "distance_km":  "TODO",
    "duration":     "TODO Std.",
    "maps_link":    "#",
}

WEATHER = [
    ("☀️",   "TODO °C", "Lufttemperatur"),
    ("\U0001F30A",     "TODO °C", "Wassertemperatur"),
    ("\U0001F31E",     "TODO Std.",  "Sonnenstunden / Tag"),
    ("\U0001F327️", "TODO Tage",  "Regentage / Monat"),
]

BEACHES      = [ {"name": f"Strand {i}",     "desc": "TODO Beschreibung", "maps": "#", "tag": "Platzhalter"} for i in range(1, 5) ]
ATTRACTIONS  = [ {"name": f"Sehenswuerdigkeit {i}", "desc": "TODO Beschreibung", "link": "#", "maps": "#", "distance": "TODO"} for i in range(1, 5) ]
RESTAURANTS  = [ {"name": f"Restaurant {i}", "loc": "TODO Ort", "desc": "TODO Beschreibung", "link": "#", "maps": "#", "icon": "\U0001F374"} for i in range(1, 5) ]
SHOPPING     = [
    {"icon": "\U0001F6D2", "name": "Supermarkt",   "desc": "TODO Adresse / Details", "link": "#"},
    {"icon": "\U0001F34E", "name": "Wochenmarkt",  "desc": "TODO Adresse / Details", "link": "#"},
    {"icon": "\U0001F3EA", "name": "Baeckerei",    "desc": "TODO Adresse / Details", "link": "#"},
]
REST_STOPS   = [ {"name": f"Raststaette {i}", "loc": "TODO km", "desc": "TODO Beschreibung", "link": "#", "maps": "#"} for i in range(1, 5) ]


# --------------------------------------------------------------------------
CSS = """
:root{--sea:#0B4F6C;--sea-d:#063B52;--sea-l:#E4F1F7;--sand:#F5E6D0;--sand-light:#FBF5ED;--tc:#C8102E;--tc-d:#8A0A20;--wh:#fff;--gr:#6B7280}
*{margin:0;padding:0;box-sizing:border-box}html{scroll-behavior:smooth}
body{font-family:'Inter',sans-serif;color:var(--sea-d);background:var(--sand-light);line-height:1.6}
h1,h2,h3,h4{font-family:'Playfair Display',serif}
a{color:var(--sea);transition:color .2s}a:hover{color:var(--tc)}
nav{position:fixed;top:0;width:100%;background:rgba(6,59,82,.95);backdrop-filter:blur(10px);z-index:1000}
nav ul{display:flex;list-style:none;max-width:1200px;margin:0 auto;padding:0 1rem;overflow-x:auto}
nav ul::-webkit-scrollbar{display:none}
nav li a{display:block;padding:1rem .8rem;color:var(--sand);text-decoration:none;font-size:.85rem;font-weight:500;white-space:nowrap}
nav li a:hover{color:var(--tc)}
.hero{position:relative;height:100vh;min-height:600px;display:flex;align-items:center;justify-content:center;text-align:center;color:#fff;overflow:hidden;background:linear-gradient(135deg,#0B4F6C,#063B52)}
.hero-bg{position:absolute;inset:0;background-size:cover;background-position:center;filter:brightness(.5)}
.hero-content{position:relative;z-index:1;padding:2rem}
.hero h1{font-size:clamp(2.5rem,8vw,5rem);margin-bottom:.5rem;text-shadow:2px 2px 20px rgba(0,0,0,.5)}
.hero .sub{font-size:clamp(1rem,3vw,1.5rem);font-weight:300;margin-bottom:2rem;opacity:.9}
.cd{display:flex;gap:1.5rem;justify-content:center;flex-wrap:wrap;margin-top:1rem}
.cd-i{background:rgba(255,255,255,.15);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.3);border-radius:12px;padding:1.2rem 1.5rem;min-width:90px}
.cd-i .n{font-family:'Playfair Display',serif;font-size:2.5rem;font-weight:700;display:block;line-height:1}
.cd-i .l{font-size:.75rem;text-transform:uppercase;letter-spacing:2px;opacity:.8;margin-top:.3rem;display:block}
section{padding:5rem 1.5rem;max-width:1200px;margin:0 auto}
.sf{max-width:100%;background:var(--wh);padding-left:0;padding-right:0}
.si{max-width:1200px;margin:0 auto;padding:0 1.5rem}
.st{font-size:clamp(1.8rem,4vw,2.5rem);margin-bottom:.5rem}
.ss{color:var(--gr);font-size:1.05rem;margin-bottom:2.5rem;font-weight:300}
.cg{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.5rem}
.card{background:var(--wh);border-radius:16px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.08);transition:transform .3s,box-shadow .3s}
.sf .card{background:var(--sand-light)}.card:hover{transform:translateY(-4px);box-shadow:0 8px 30px rgba(0,0,0,.12)}
.card .ph{width:100%;height:200px;background:linear-gradient(135deg,var(--sea-l),var(--sand));display:flex;align-items:center;justify-content:center;color:var(--sea);font-size:3rem}
.cb{padding:1.5rem}.cb h3{font-size:1.15rem;margin-bottom:.5rem}.cb p{color:var(--gr);font-size:.93rem}
.cb a.more{display:inline-block;margin-top:.5rem;font-size:.85rem;font-weight:500;color:var(--sea);text-decoration:none}
.cb a.more:hover{color:var(--tc);text-decoration:underline}
.tag{display:inline-block;background:var(--sea-l);color:var(--sea);padding:.2rem .7rem;border-radius:20px;font-size:.8rem;font-weight:500;margin-top:.6rem;margin-right:.2rem}
.tag.dog{background:#FEF3C7;color:#92400E}
.tag.todo{background:#FEE2E2;color:#991B1B}
.ig{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:1rem;margin:1.5rem 0}
.ii{display:flex;align-items:center;gap:.7rem;padding:.7rem;background:var(--sand-light);border-radius:10px;font-size:.9rem}
.sf .ii{background:var(--wh)}.ii .em{font-size:1.3rem}
.ib{background:var(--sea-l);border-left:4px solid var(--sea);padding:1.2rem 1.5rem;border-radius:0 10px 10px 0;margin:1.5rem 0}
.wg{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:1.5rem;margin:1.5rem 0}
.wc{text-align:center;padding:2rem 1.5rem;background:linear-gradient(135deg,var(--sea),var(--sea-d));color:#fff;border-radius:16px}
.wc .wi{font-size:2.5rem;margin-bottom:.5rem}.wc .wv{font-family:'Playfair Display',serif;font-size:2rem;font-weight:700}.wc .wl{font-size:.85rem;opacity:.8;margin-top:.25rem}
.rg{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:1rem;margin:1.5rem 0}
.ri{display:flex;align-items:center;gap:.7rem;padding:1rem;background:var(--sand-light);border-radius:10px}.ri .ric{font-size:1.5rem}
.rmg{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:1rem;margin:1.5rem 0}
.rmc{padding:1.2rem;background:var(--sand-light);border-radius:12px;text-align:center}.rmc .ro{font-size:2rem;margin-bottom:.5rem}.rmc h4{font-size:1rem;margin-bottom:.2rem}.rmc p{font-size:.85rem;color:var(--gr)}
.rl{display:grid;grid-template-columns:repeat(auto-fill,minmax(350px,1fr));gap:1.5rem}
.rc{display:flex;gap:1rem;padding:1.5rem;background:var(--sand-light);border-radius:12px;box-shadow:0 2px 10px rgba(0,0,0,.06)}
.rc .rci{font-size:1.5rem;flex-shrink:0;width:50px;height:50px;background:var(--tc);color:#fff;border-radius:12px;display:flex;align-items:center;justify-content:center}
.rc h3{font-size:1.05rem;margin-bottom:.2rem}.rc .rloc{font-size:.8rem;color:var(--tc);font-weight:500}.rc .rdesc{font-size:.9rem;color:var(--gr);margin-top:.3rem}
.rc a.more{font-size:.8rem;color:var(--sea);text-decoration:none;margin-top:.3rem;display:inline-block}
.rc a.more:hover{text-decoration:underline}
.tc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1.5rem;margin:1.5rem 0}
.tip{padding:1.5rem;background:var(--sand-light);border-radius:12px;border-top:4px solid var(--tc)}.sf .tip{background:var(--wh)}
.tip h4{margin-bottom:.5rem}.tip p{font-size:.9rem;color:var(--gr)}
.rst{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1.5rem;margin:1.5rem 0}
.rs{padding:1.5rem;border-radius:12px;background:#FEF2F2;border-left:4px solid #DC2626}.sf .rs{background:#FEF2F2}
.rs h4{margin-bottom:.3rem;font-size:1rem}.rs .rsl{font-size:.8rem;color:#DC2626;font-weight:500;margin-bottom:.5rem}.rs p{font-size:.9rem;color:var(--gr)}
.rs a.rslink{display:inline-block;margin-top:.5rem;font-size:.82rem;color:#DC2626;font-weight:500;text-decoration:none}.rs a.rslink:hover{text-decoration:underline}
.sl{list-style:none}.sl li{padding:1rem 1.2rem;background:var(--sand-light);border-radius:10px;margin-bottom:.7rem;display:flex;align-items:flex-start;gap:.7rem}
.sl li .sli{font-size:1.3rem;flex-shrink:0;margin-top:2px}.sl li strong{display:block;margin-bottom:.2rem}.sl li span{font-size:.9rem;color:var(--gr)}
.sl li a{font-size:.8rem;display:inline-block;margin-top:.3rem}
.map-ph{width:100%;height:400px;border-radius:16px;background:linear-gradient(135deg,var(--sea-l),var(--sand));display:flex;align-items:center;justify-content:center;color:var(--sea);font-size:1.2rem;margin-top:1.5rem;box-shadow:0 4px 20px rgba(0,0,0,.1)}
footer{background:var(--sea-d);color:var(--sand);text-align:center;padding:2rem 1.5rem;font-size:.85rem}
@media(max-width:768px){nav li a{padding:.8rem .6rem;font-size:.75rem}section{padding:3rem 1rem}.cd{gap:.7rem}.cd-i{padding:.8rem 1rem;min-width:70px}.cd-i .n{font-size:1.8rem}.cg,.rl{grid-template-columns:1fr}}
"""

JS = r"""
function uc(){var t=new Date('__COUNTDOWN__'),n=new Date(),d=t-n;if(d<=0){document.getElementById('cd').innerHTML='<p style="font-size:1.5rem">🎉 Der Urlaub hat begonnen!</p>';return}var dd=Math.floor(d/864e5),hh=Math.floor(d%864e5/36e5),mm=Math.floor(d%36e5/6e4),ss=Math.floor(d%6e4/1e3);document.getElementById('cd-d').textContent=dd;document.getElementById('cd-h').textContent=('0'+hh).slice(-2);document.getElementById('cd-m').textContent=('0'+mm).slice(-2);document.getElementById('cd-s').textContent=('0'+ss).slice(-2)}uc();setInterval(uc,1e3);
document.querySelectorAll('nav a').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();var t=document.querySelector(this.getAttribute('href'));if(t)window.scrollTo({top:t.getBoundingClientRect().top+window.pageYOffset-50,behavior:'smooth'})})});
""".replace("__COUNTDOWN__", COUNTDOWN_TARGET)


def placeholder_img(emoji="\U0001F4F7"):
    return f'<div class="ph">{emoji}</div>'


def features_html():
    return "".join(f'<div class="ii"><span class="em">{e}</span> {t}</div>' for e, t in ACCOMMODATION["features"])


def rooms_html():
    return "".join(f'<div class="rmc"><div class="ro">\U0001F6CC</div><h4>{n}</h4><p>{d}</p></div>' for n, d in ACCOMMODATION["rooms"])


def weather_html():
    bgs = ["", "background:linear-gradient(135deg,#0891b2,#164e63)",
           "background:linear-gradient(135deg,#d97706,#92400e)",
           "background:linear-gradient(135deg,#6366f1,#312e81)"]
    return "".join(
        f'<div class="wc" style="{bgs[i]}"><div class="wi">{icon}</div><div class="wv">{val}</div><div class="wl">{lbl}</div></div>'
        for i, (icon, val, lbl) in enumerate(WEATHER)
    )


def beaches_html():
    return "".join(
        f'<div class="card">{placeholder_img("\U0001F3D6️")}<div class="cb"><h3>{b["name"]}</h3><p>{b["desc"]}</p>'
        f'<a class="more" href="{b["maps"]}" target="_blank">\U0001F697 Route</a><br>'
        f'<span class="tag todo">{b["tag"]}</span></div></div>' for b in BEACHES
    )


def attractions_html():
    return "".join(
        f'<div class="card">{placeholder_img("\U0001F3DB️")}<div class="cb"><h3>{a["name"]}</h3><p>{a["desc"]}</p>'
        f'<a class="more" href="{a["link"]}" target="_blank">→ Info</a> · '
        f'<a class="more" href="{a["maps"]}" target="_blank">\U0001F697 Route</a><br>'
        f'<span class="tag">\U0001F697 {a["distance"]}</span></div></div>' for a in ATTRACTIONS
    )


def restaurants_html():
    return "".join(
        f'<div class="rc"><div class="rci">{r["icon"]}</div><div><h3>{r["name"]}</h3>'
        f'<div class="rloc">{r["loc"]}</div><p class="rdesc">{r["desc"]}</p>'
        f'<a class="more" href="{r["link"]}" target="_blank">→ Website</a> · '
        f'<a class="more" href="{r["maps"]}" target="_blank">\U0001F697 Route</a></div></div>' for r in RESTAURANTS
    )


def shopping_html():
    return "".join(
        f'<li><span class="sli">{s["icon"]}</span><div><strong>{s["name"]}</strong>'
        f'<span>{s["desc"]}</span><br><a href="{s["link"]}" target="_blank">→ Details</a></div></li>'
        for s in SHOPPING
    )


def rest_stops_html():
    return "".join(
        f'<div class="rs"><h4>{r["name"]}</h4><div class="rsl">{r["loc"]}</div><p>{r["desc"]}</p>'
        f'<a class="rslink" href="{r["link"]}" target="_blank">→ Website</a> · '
        f'<a class="rslink" href="{r["maps"]}" target="_blank">\U0001F4CD Route</a></div>' for r in REST_STOPS
    )


hero_bg_style = f"background-image:url('{HERO_BG_URL}')" if HERO_BG_URL else ""

html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TRIP_TITLE} – {ACCOMMODATION["name"]}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<nav><ul>
<li><a href="#hero">Start</a></li>
<li><a href="#villa">Unterkunft</a></li>
<li><a href="#anreise">Anreise</a></li>
<li><a href="#wetter">Wetter</a></li>
<li><a href="#straende">Strände</a></li>
<li><a href="#ausfluge">Ausflüge</a></li>
<li><a href="#restaurants">Restaurants</a></li>
<li><a href="#einkaufen">Einkaufen</a></li>
<li><a href="#karte">Karte</a></li>
</ul></nav>

<section class="hero" id="hero">
<div class="hero-bg" style="{hero_bg_style}"></div>
<div class="hero-content">
<h1>{TRIP_TITLE}</h1>
<p class="sub">{TRIP_SUBTITLE}</p>
<div class="cd" id="cd">
<div class="cd-i"><span class="n" id="cd-d">--</span><span class="l">Tage</span></div>
<div class="cd-i"><span class="n" id="cd-h">--</span><span class="l">Stunden</span></div>
<div class="cd-i"><span class="n" id="cd-m">--</span><span class="l">Minuten</span></div>
<div class="cd-i"><span class="n" id="cd-s">--</span><span class="l">Sekunden</span></div>
</div></div>
</section>

<!-- UNTERKUNFT -->
<section id="villa">
<h2 class="st">Die Unterkunft</h2>
<p class="ss">{ACCOMMODATION["name"]} · {ACCOMMODATION["location"]} ·
<a href="{ACCOMMODATION["booking"]}" target="_blank">\U0001F4F7 Fotos &amp; Details</a> ·
<a href="{ACCOMMODATION["maps"]}" target="_blank">\U0001F4CD Google Maps</a></p>

<div class="ib"><strong>⚠️ Platzhalter:</strong> Details zur Unterkunft folgen noch.</div>

<h3 style="margin:2rem 0 .5rem">Ausstattung</h3>
<div class="ig">{features_html()}</div>

<h3 style="margin:2rem 0 .5rem">Zimmeraufteilung</h3>
<div class="rmg">{rooms_html()}</div>

<h3 style="margin:2rem 0 .5rem">Hausordnung</h3>
<div class="rg">
<div class="ri"><span class="ric">\U0001F551</span><div><strong>Check-in</strong> TODO Uhr</div></div>
<div class="ri"><span class="ric">\U0001F559</span><div><strong>Check-out</strong> TODO Uhr</div></div>
<div class="ri"><span class="ric">\U0001F436</span><div><strong>Haustiere</strong> TODO</div></div>
</div>
</section>

<!-- ANREISE -->
<section id="anreise" class="sf"><div class="si">
<h2 class="st">Anreise</h2>
<p class="ss">~{ROUTE["distance_km"]} km · ca. {ROUTE["duration"]} Fahrt ·
<a href="{ROUTE["maps_link"]}" target="_blank">\U0001F697 Komplette Route auf Google Maps</a></p>

<div class="ib"><strong>⚠️ Platzhalter:</strong> Route und Raststaetten folgen noch.</div>

<h3 style="margin:2rem 0 1rem">Maut &amp; Faehren</h3>
<div class="tc-grid">
<div class="tip"><h4>\U0001F1E9\U0001F1EA Deutschland</h4><p>TODO: Hinweise zu Autobahn &amp; Baustellen.</p></div>
<div class="tip"><h4>\U0001F1E9\U0001F1F0 Daenemark</h4><p>TODO: Brueckenmaut Storebaelt / Oeresund / Faehren.</p></div>
<div class="tip"><h4>⛽ Tanken</h4><p>TODO: Preisvergleich DE/DK, Bezahlung mit Karte.</p></div>
</div>

<h3 style="margin:2rem 0 1rem">\U0001F6D1 Empfohlene Raststätten</h3>
<div class="rst">{rest_stops_html()}</div>

</div></section>

<!-- WETTER -->
<section id="wetter">
<h2 class="st">Wetter im Sommer</h2>
<p class="ss">Durchschnittswerte fuer Daenemark – TODO genauer Zeitraum</p>
<div class="wg">{weather_html()}</div>
</section>

<!-- STRAENDE -->
<section id="straende" class="sf"><div class="si">
<h2 class="st">Strände</h2>
<p class="ss">Nordseekueste &amp; Ostseestrand – TODO Auswahl</p>
<div class="ib"><strong>\U0001F436 Hinweis:</strong> Hundefreundlichkeit je nach Strand pruefen (TODO).</div>
<div class="cg">{beaches_html()}</div>
</div></section>

<!-- AUSFLUGSZIELE -->
<section id="ausfluge">
<h2 class="st">Sehenswürdigkeiten &amp; Ausflüge</h2>
<p class="ss">Natur, Geschichte und Kueste – TODO</p>
<div class="cg">{attractions_html()}</div>
</section>

<!-- RESTAURANTS -->
<section id="restaurants" class="sf"><div class="si">
<h2 class="st">Restaurants &amp; Essen</h2>
<p class="ss">Smoerrebroed, Fisch &amp; daenische Klassiker – TODO</p>
<div class="rl">{restaurants_html()}</div>
</div></section>

<!-- EINKAUFEN -->
<section id="einkaufen">
<h2 class="st">Einkaufen</h2>
<p class="ss">Supermärkte, Maerkte &amp; Shopping</p>
<ul class="sl">{shopping_html()}</ul>
<div class="ib" style="margin-top:1.5rem"><strong>\U0001F4B6 Waehrung:</strong> Daenische Krone (DKK). Kartenzahlung nahezu ueberall moeglich, Bargeld selten noetig.</div>
</section>

<!-- KARTE -->
<section id="karte" class="sf"><div class="si">
<h2 class="st">Übersichtskarte</h2>
<p class="ss">Alle wichtigen Orte auf einen Blick – TODO Kartenbild</p>
<div class="map-ph">\U0001F5FA️ Karte folgt</div>
</div></section>

<footer>
<p>\U0001F1E9\U0001F1F0 {TRIP_TITLE} · {ACCOMMODATION["name"]} · {TRIP_SUBTITLE}</p>
<p style="margin-top:.5rem;opacity:.6">Erstellt mit ❤ für den perfekten Urlaub</p>
</footer>

<script>{JS}</script>
</body></html>"""

outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
with open(outpath, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Created: {outpath}")
print(f"Size: {os.path.getsize(outpath) / 1024:.0f} KB")
