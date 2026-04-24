"""Build-Script fuer die Urlaubs-Website 'Urlaub 2026 - Daenemark'.

Erzeugt eine self-contained index.html. Fotos werden relativ aus haus_fotos/ verlinkt
(vorher einmal mit compress_fotos.py auf Web-Groesse bringen).

Alle Inhalte wurden aus mehreren unabhaengigen Quellen verifiziert
(esmark.de, visitvesterhavet.dk, tirpitz.dk, hennekirkebykro.dk, tripadvisor,
climate-data.org, serways.de, vejdirektoratet.dk). Keine Fake News - ungeprueftes
ist weggelassen oder als TODO markiert.
"""
import os
from pathlib import Path

# --------------------------------------------------------------------------
# ECKDATEN
# --------------------------------------------------------------------------
TRIP_TITLE       = "Daenemark 2026"
TRIP_SUBTITLE    = "Henne Strand · 22. – 29. August 2026"
COUNTDOWN_TARGET = "2026-08-22T15:00:00+02:00"   # Sa 22.08.2026, Check-in ab 15:00

# Haus-Koordinaten — auf der oeffentlichen Seite bewusst nur Ortsname, keine Hausnummer.
# Exakte Adresse (Timianvej 6) steht in der privaten memory/booking.md.
HOUSE_ADDR   = "Henne+Strand,+6854+Denmark"
HOUSE_MAPS   = "https://www.google.com/maps/search/?api=1&query=Henne+Strand,+6854+Denmark"
START_ADDR   = "Senden,+Nordrhein-Westfalen"     # Startort (Ort statt Hausnummer)

# Foto-Ordner (Web-komprimiert)
FOTO_DIR = Path(__file__).parent / "haus_fotos"
def fotos_sorted():
    return sorted([p.name for p in FOTO_DIR.glob("foto_*.jpg")])

HERO_PHOTO = "haus_fotos/foto_511397.jpg"   # Aussenaufnahme - esmark og:image


# --------------------------------------------------------------------------
# UNTERKUNFT (Quelle: esmark.de/ferienhaus-40789/)
# --------------------------------------------------------------------------
ACCOMMODATION = {
    "name":     "Holzhaus am Duenenrand",
    "location": "Henne Strand · 400 m zum Nordseestrand",
    "booking":  "https://esmark.de/ferienhaus-40789/",
    "maps":     HOUSE_MAPS,
    "features": [
        ("\U0001F525",        "Kaminofen"),
        ("\U0001F6CF️",  "3 Schlafzimmer"),
        ("\U0001F6C1",        "1 Badezimmer"),
        ("\U0001F4CF",        "67 m² auf 1.413 m²"),
        ("\U0001F373",        "Küche mit Geschirrspüler"),
        ("\U0001F9FA",        "Waschmaschine"),
        ("\U0001F4F6",        "Glasfaser-WLAN"),
        ("\U0001F436",        "Haustiere (max. 2)"),
        ("☀️",      "Terrasse offen + überdacht"),
        ("\U0001F356",        "Gasgrill"),
        ("\U0001F4FA",        "Flachbildfernseher"),
        ("\U0001F333",        "Naturgrundstück"),
    ],
    "rooms": [
        ("Schlafzimmer 1", "1 Doppelbett",   "haus_fotos/foto_446653.jpg"),
        ("Schlafzimmer 2", "2 Einzelbetten", "haus_fotos/foto_446657.jpg"),
        ("Schlafzimmer 3", "1 Etagenbett",   "haus_fotos/foto_446658.jpg"),
        ("Badezimmer",     "1 Bad",          None),
    ],
}

# --------------------------------------------------------------------------
# ANREISE (~640 km / ca. 7 h von Senden, NRW)
# Route: A1 Nord -> A7 (ab Hamburg) -> E45 DK -> Abfahrt Varde -> Henne Strand
# --------------------------------------------------------------------------
ROUTE = {
    "distance_km": "640",
    "duration":    "ca. 7 Std.",
    "maps_link":   f"https://www.google.com/maps/dir/{START_ADDR}/{HOUSE_ADDR}",
}

# Quellen: serways.de, raststaetten.de, tank.rast.de, vejdirektoratet.dk
REST_STOPS = [
    {
        "name":  "\U0001F309 Dammer Berge Ost",
        "loc":   "A1 · Holdorf · ~105 km / 1:10 h",
        "desc":  "Brückenrasthöf – Restaurant spannt sich 103 m über die A1. Burger King, Nordsee, Shell, Spielplatz, Sanifair-WC.",
        "link":  "https://www.serways.de/standorte/dammer-berge-ost/",
        "maps":  f"https://www.google.com/maps/dir/{START_ADDR}/Serways+Rastst%C3%A4tte+Dammer+Berge+Ost,+49451+Holdorf",
        "photo": "content_fotos/rs_dammer.jpg",
    },
    {
        "name":  "⛽ Grundbergsee Süd",
        "loc":   "A1 · Sottrum · ~265 km / 2:45 h",
        "desc":  "Modern gebaute Rastanlage mit Burger King, Aral-Tanke und grossem Wickelbereich. Guter Tank-Stopp vor Hamburg.",
        "link":  "https://www.serways.de/standorte/grundbergsee-sued/",
        "maps":  f"https://www.google.com/maps/dir/{START_ADDR}/Serways+Grundbergsee+S%C3%BCd",
        "photo": "content_fotos/rs_grundbergsee.jpg",
    },
    {
        "name":  "\U0001F37D️ Autohof Bockel",
        "loc":   "A1 Abfahrt 49 · ~310 km / 3:15 h",
        "desc":  "Großer Aral-Autohof mit günstigem Service-Restaurant (Schnitzel, Fisch, Pizza). Beliebte Alternative zu den Brücken-Raststaetten.",
        "link":  "https://autohof-bockel.de/",
        "maps":  f"https://www.google.com/maps/dir/{START_ADDR}/Aral+Autohof+Bockel,+27386+Bockel",
        "photo": None,
    },
    {
        "name":  "\U0001F332 Hüttener Berge Ost",
        "loc":   "A7 · Alt Duvenstedt · ~450 km / 4:45 h",
        "desc":  "Landschaftlich sehr schön mitten im Naturpark Hüttener Berge. Letzter grösserer Stopp vor der dänischen Grenze – hier noch volltanken!",
        "link":  "https://www.raststaetten.de/standorte/huettener-berge-ost/",
        "maps":  f"https://www.google.com/maps/dir/{START_ADDR}/Serways+H%C3%BCttener+Berge+Ost",
        "photo": "content_fotos/rs_huettener.jpg",
    },
    {
        "name":  "\U0001F1E9\U0001F1F0 Rasteplads Frøslev Øst",
        "loc":   "E45 · kurz hinter Grenze · ~520 km / 5:30 h",
        "desc":  "Erste dänische Rastanlage nach Padborg. Circle K mit Tankstelle, Imbiss, Spielplatz und seit 2024 Schnellladesaeulen. Hunde dürfen an der Leine auf die Grünflaeche.",
        "link":  "https://www.vejdirektoratet.dk/trafikant/rastepladser-din-pause-paa-turen",
        "maps":  f"https://www.google.com/maps/dir/{START_ADDR}/Rasteplads+Fr%C3%B8slev+%C3%98st",
        "photo": None,
    },
    {
        "name":  "\U0001F6E3️ Rasteplads Skærup Vest",
        "loc":   "E45 · südlich Vejle · ~600 km / 6:30 h",
        "desc":  "Letzter Stretch-Stopp vor Abzweig Richtung Varde/Henne. OK/Circle K, Imbiss, WC, Spielplatz, seit 2026 neuer Schnellladepark.",
        "link":  "https://www.vejdirektoratet.dk/trafikant/rastepladser-din-pause-paa-turen",
        "maps":  f"https://www.google.com/maps/dir/{START_ADDR}/Rasteplads+Sk%C3%A6rup+Vest",
        "photo": "content_fotos/rs_skaerup.jpg",
    },
]

# --------------------------------------------------------------------------
# WETTER August Henne Strand (Quelle: climate-data.org Esbjerg-Station, 34 km)
# Verifiziert: Luft 18-20 °C, Wasser 17-19 °C, waermster Monat des Jahres
# Sonnenstunden/Regentage: Durchschnittswerte fuer dänische Westküste im August
# --------------------------------------------------------------------------
WEATHER = [
    ("☀️",     "18 – 20 °C",  "Lufttemperatur"),
    ("\U0001F30A",       "17 – 19 °C",  "Wassertemperatur"),
    ("\U0001F31E",       "~ 6 – 7 Std.",     "Sonnenstunden / Tag"),
    ("\U0001F327️", "~ 12 Tage",             "Regentage / Monat"),
]

# --------------------------------------------------------------------------
# STRAENDE (Quellen: visitvesterhavet.com, visitvesterhavet.dk, Wikipedia,
# esmark.dk/hundestrande/, blavandstrand.com)
# Hunderegel-Standard DK: 1.4.-30.9. Leinenpflicht, 1.10.-31.3. frei
# --------------------------------------------------------------------------
BEACHES = [
    {
        "name":  "Henne Strand (Hauptstrand)",
        "desc":  "Breiter, feiner Sandstrand direkt am Ort, ca. 400 m vom Haus. Autofrei, Lifeguard Ende Juni bis Ende August. Starke Strömung – auf Warnflaggen achten.",
        "maps":  f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Henne+Strand+beach",
        "tag":   "Hauptstrand · 400 m",
        "photo": "content_fotos/strand_henne.jpg",
    },
    {
        "name":  "Henne Mølle Å",
        "desc":  "Ruhiger Natur-Sandstrand nördlich vom Ort, wo die Henne Mølle Å in die Nordsee mündet. Weite Dünen, kaum Infrastruktur – perfekt für lange Spaziergänge.",
        "maps":  f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Henne+M%C3%B8lle+%C3%85+Strand",
        "tag":   "Geheimtipp",
        "photo": "content_fotos/strand_henne_m.jpg",
    },
    {
        "name":  "Houstrup Strand",
        "desc":  "Weitlaeufiger Sandstrand nord-westlich mit grosser Dünenlandschaft. Weniger touristisch als Blåvand, gute Brandungsbedingungen.",
        "maps":  f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Houstrup+Strand",
        "tag":   "Ruhig · Dünen",
        "photo": None,
    },
    {
        "name":  "Nymindegab Strand",
        "desc":  "Nördlich von Henne am Übergang zum Ringkøbing Fjord. Breiter Sandstrand mit Dünen; in der Nähe die Tipperne-Vogelschutzgebiete.",
        "maps":  f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Nymindegab+Strand",
        "tag":   "Natur · Vögel",
        "photo": "content_fotos/strand_nymindegab.jpg",
    },
    {
        "name":  "Vejers Strand",
        "desc":  "Klassischer befahrbarer Nordseestrand (man darf mit dem Auto auf den Sand!). Lifeguard im Sommer, Kiosk und Strand-Camping direkt nebenan – familienfreundlich.",
        "maps":  f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Vejers+Strand",
        "tag":   "Auto auf Strand · Familie",
        "photo": "content_fotos/strand_vejers.jpg",
    },
    {
        "name":  "Blåvand Strand",
        "desc":  "Einer der bekanntesten Strände Daenemarks, westlichster Punkt des Landes. Feiner weisser Sand, Bunker-Skulpturen (Tirpitz-Stellung). Häufig mit der Blauen Flagge ausgezeichnet.",
        "maps":  f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Bl%C3%A5vand+Strand",
        "tag":   "Blaue Flagge · Highlight",
        "photo": "content_fotos/strand_blaavand.jpg",
    },
    {
        "name":  "\U0001F436 Hundewald Øksby",
        "desc":  "Eingezäunter Hundewald nahe Blåvand – hier dürfen Hunde ganzjährig frei laufen. Praktisch an heissen Tagen als Schatten-Alternative zum Strand.",
        "maps":  f"https://www.google.com/maps/dir/{HOUSE_ADDR}/%C3%98ksby+Hundeskov",
        "tag":   "\U0001F436 Frei laufen ganzjährig",
        "photo": None,
    },
]

# --------------------------------------------------------------------------
# AUSFLUEGE (Quellen: tirpitz.dk, vardemuseerne.dk, visitribe.dk, fimus.dk,
# visitfanoe.dk, naturstyrelsen.dk, legoland.dk, Wikipedia)
# Alle als Saison 2026 geoeffnet bestaetigt (Stand April 2026 recherchiert).
# --------------------------------------------------------------------------
ATTRACTIONS = [
    {
        "name":     "\U0001F3DB️ Tirpitz-Museum, Blåvand",
        "desc":     "Unterirdisches Museum im ehemaligen Atlantikwall-Bunker, 2017 von Bjarke Ingels (BIG) in die Dünen gebaut. Vier Ausstellungen: Atlantikwall, Bernstein, Westküsten-Geschichte und Wechsel. Eintritt Erwachsene 125 DKK, unter 18 frei.",
        "link":     "https://tirpitz.dk/",
        "maps":     f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Tirpitz,+Tirpitzvej+1,+6857+Bl%C3%A5vand",
        "distance": "~ 30 Min.",
        "photo":    "content_fotos/tirpitz.jpg",
    },
    {
        "name":     "\U0001F3EF Blåvandshuk Fyr",
        "desc":     "39 m hoher Leuchtturm (1900), westlichster Punkt Daenemarks. 170 Stufen zur Aussichtsplattform mit Blick auf Horns Rev und die Seehundsbank. Betrieben von Varde Museerne.",
        "link":     "https://www.vardemuseerne.dk/museum/blaavandshuk-fyr/",
        "maps":     f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Bl%C3%A5vandshuk+Fyr,+6857+Bl%C3%A5vand",
        "distance": "~ 32 Min.",
        "photo":    None,
    },
    {
        "name":     "⛪ Ribe – älteste Stadt Skandinaviens",
        "desc":     "Um 710 n.Chr. gegründet. Dom aus dem 12. Jh. mit modernen Fresken von Carl-Henning Pedersen, Fachwerk-Altstadt mit Kopfsteinpflaster. Nachtwächter-Rundgang Mai–September täglich 20 und 22 Uhr.",
        "link":     "https://www.visitribe.dk/",
        "maps":     f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Ribe,+Denmark",
        "distance": "~ 55 Min.",
        "photo":    "content_fotos/ribe.jpg",
    },
    {
        "name":     "\U0001F41F Fiskeri- og Søfartsmuseet (Esbjerg)",
        "desc":     "Saltwater-Aquarium und Seefahrts-/Fischereimuseum mit Robbenbecken (Fütterungen 11:00 und 14:30 Uhr). Außenbereich mit historischen Fischerbooten.",
        "link":     "https://www.fimus.dk/",
        "maps":     f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Fiskeri-+og+S%C3%B8fartsmuseet,+Tarphagevej+2,+6710+Esbjerg",
        "distance": "~ 45 Min.",
        "photo":    "content_fotos/fimus.jpg",
    },
    {
        "name":     "\U0001F5FF Mennesket ved Havet",
        "desc":     "9 m hohe Betonskulptur von Svend Wiig Hansen (1995) am Sædding Strand, Esbjerg. Vier sitzende weisse Männer, die aufs Meer schauen. Kostenlos, jederzeit zugänglich – gut kombinierbar mit Fimus-Museum.",
        "link":     "https://www.visitesbjerg.com/ln-int/esbjerg/man-meets-sea-gdk600115",
        "maps":     f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Mennesket+ved+Havet,+Esbjerg",
        "distance": "~ 42 Min.",
        "photo":    "content_fotos/mennesket.jpg",
    },
    {
        "name":     "⛴️ Fanø (Inselausflug)",
        "desc":     "12-Minuten-Autofähre ab Esbjerg, halbstündlich in der Hochsaison. Breite Strände, reetgedeckte Seefahrerdoerfer Nordby und Sønderho. Letzteres mehrfach zum schönsten Dorf Daenemarks gewählt.",
        "link":     "https://www.visitfanoe.dk/",
        "maps":     f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Esbjerg+F%C3%A6rgehavn",
        "distance": "~ 45 Min. + Fähre",
        "photo":    "content_fotos/fanoe.jpg",
    },
    {
        "name":     "\U0001F4A7 Filsø",
        "desc":     "Zweitgrösster See Jütlands (~915 ha), seit 2012 renaturiertes Vogelschutzgebiet. Aussichtsturm, markierte Wanderwege, 28-km-Radrunde um den See.",
        "link":     "https://naturstyrelsen.dk/naturoplevelser/naturguider/filsoe",
        "maps":     f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Fils%C3%B8,+6830+Nr.+Nebel",
        "distance": "~ 12 Min.",
        "photo":    "content_fotos/filsoe.jpg",
    },
    {
        "name":     "\U0001F9F1 Legoland Billund",
        "desc":     "Ältester und grösster Legoland-Park der Welt (1968). 65+ Attraktionen, Miniland aus ~65 Mio. Lego-Steinen. Im August verlängerte Öffnungszeiten bis 21 Uhr.",
        "link":     "https://www.legoland.dk/",
        "maps":     f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Legoland+Billund",
        "distance": "~ 1:15 h",
        "photo":    "content_fotos/legoland.jpg",
    },
]

# --------------------------------------------------------------------------
# RESTAURANTS (aus mehreren Quellen verifiziert - Hennegaarden existiert NICHT,
# korrekt ist Strandgaarden auf Klitvej 3. Pizzeria = Taverna Colosseo.)
# --------------------------------------------------------------------------
RESTAURANTS = [
    {
        "icon":  "⭐",
        "name":  "Henne Kirkeby Kro",
        "loc":   "Henne Kirkeby · ~5 km",
        "desc":  "2-Sterne-Michelin-Restaurant von Paul Cunningham in einem restaurierten Kro aus dem 18. Jh. Saison 2026: 6. März – 19. Dezember. Mi 18–21, Do–Sa 12–21. Reservierung zwingend 2–3 Monate vorher.",
        "link":  "https://hennekirkebykro.dk/",
        "maps":  f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Henne+Kirkeby+Kro,+Strandvejen+234,+6854+Henne",
    },
    {
        "icon":  "\U0001F373",
        "name":  "Strandgaarden Restaurant",
        "loc":   "Henne Strand · ~1 km",
        "desc":  "Traditionell-dänische Küche mit frischen, saisonalen Zutaten. Tripadvisor 4,3 (Rang 2 in Henne), Trustpilot 1000+ Bewertungen. Gemütliches Strandhaus-Ambiente.",
        "link":  "https://www.strandgaarden-henne.dk/",
        "maps":  f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Strandgaarden+Restaurant,+Klitvej+3,+6854+Henne",
    },
    {
        "icon":  "\U0001F368",
        "name":  "Ishuset ved Henne Strand",
        "loc":   "Henne Strand Zentrum · ~1 km",
        "desc":  "Institution am Strand – #1 auf Tripadvisor (4,5 von 5). Eis, Waffeln, Kaffee, Snacks. Perfekter Stopp nach dem Strandtag.",
        "link":  "https://www.tripadvisor.com/Restaurant_Review-g4067331-d7973871-Reviews-Ishuset_Ved_Henne_Strand.html",
        "maps":  f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Ishuset+ved+Henne+Strand",
    },
    {
        "icon":  "\U0001F956",
        "name":  "Købmand Hansens Bageri & Café",
        "loc":   "Henne Strand · ~1 km",
        "desc":  "Bäckerei, Café und Eisbar unter einem Dach. Wienerbrød, Kanelsnegle und belegte Brote – der Frühstücks-Treff am Ort.",
        "link":  "https://www.kobmand-hansen.dk/",
        "maps":  f"https://www.google.com/maps/dir/{HOUSE_ADDR}/K%C3%B8bmand+Hansens+Bageri,+Strandvejen+450,+6854+Henne",
    },
    {
        "icon":  "\U0001F355",
        "name":  "Taverna Colosseo",
        "loc":   "Henne Strand · ~1 km",
        "desc":  "Einzige Pizzeria im Ort – Pizza, Pasta und Steaks. Tripadvisor 3,3 (gemischtes Bild, aber praktisch für einen unkomplizierten Abend).",
        "link":  "https://www.tripadvisor.com/Restaurant_Review-g4067331-d6350616-Reviews-Taverna_Colosseo.html",
        "maps":  f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Taverna+Colosseo,+Henne+Strand",
    },
    {
        "icon":  "\U0001F35F",
        "name":  "Restaurant Sløjfen, Blåvand",
        "loc":   "Blåvandvej, Blåvand · ~35 km",
        "desc":  "Casual-Karte (Burger, Steak, Fisch, Kinderteller) direkt in Blåvand. Ideal zu kombinieren mit einem Ausflug zum Leuchtturm oder Tirpitz-Museum.",
        "link":  "https://sloejfen.dk/",
        "maps":  f"https://www.google.com/maps/dir/{HOUSE_ADDR}/Restaurant+Sl%C3%B8jfen,+Bl%C3%A5vand",
    },
]

# --------------------------------------------------------------------------
# EINKAUFEN (verifiziert)
# --------------------------------------------------------------------------
SHOPPING = [
    {
        "icon": "\U0001F6D2",
        "name": "SPAR Henne (Købmand Hansen)",
        "desc": "Mo–Do + So 8–18, Fr+Sa 8–19 · Grösster Supermarkt am Ort, wenige hundert Meter vom Haus. Backshop, Frischfleisch, Fisch, Getränke.",
        "link": "https://spar.dk/butik/spar-henne",
    },
    {
        "icon": "\U0001F956",
        "name": "Købmand Hansens Bageri & Café",
        "desc": "Bäckerei morgens, Café tagsüber, Eis am Nachmittag – der Dreifach-Treff im Ort.",
        "link": "https://www.kobmand-hansen.dk/",
    },
    {
        "icon": "\U0001F45C",
        "name": "COAST Henne Strand",
        "desc": "Outlet für Premium-Marken mitten im Ort – Regenjacken, Outdoor-Mode und skandinavisches Design.",
        "link": "https://www.visitvesterhavet.dk/vesterhavet/vesterhavsferie/coast-henne-strand-gdk1090434",
    },
    {
        "icon": "\U0001F3EA",
        "name": "Grössere Märkte: Varde / Nørre Nebel",
        "desc": "Für den Wocheneinkauf lohnt ein Abstecher nach Nørre Nebel (~10 km, Rema 1000/Netto) oder Varde (~25 km, Bilka/Føtex).",
        "link": "https://www.google.com/maps/search/Rema+1000+N%C3%B8rre+Nebel",
    },
]


# --------------------------------------------------------------------------
# CSS / JS
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
.hero{position:relative;height:100vh;min-height:600px;display:flex;align-items:center;justify-content:center;text-align:center;color:#fff;overflow:hidden}
.hero-bg{position:absolute;inset:0;background-size:cover;background-position:center;filter:brightness(.55)}
.hero-content{position:relative;z-index:1;padding:2rem}
.hero h1{font-size:clamp(2.5rem,8vw,5rem);margin-bottom:.5rem;text-shadow:2px 2px 20px rgba(0,0,0,.5)}
.hero .sub{font-size:clamp(1rem,3vw,1.5rem);font-weight:300;margin-bottom:2rem;opacity:.95}
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
.card img.ph-img{width:100%;height:200px;object-fit:cover;cursor:pointer;transition:transform .3s}
.card img.ph-img:hover{transform:scale(1.02)}
.rmc.clickable{cursor:pointer;position:relative;overflow:hidden}
.rmc.clickable img.room-thumb{width:100%;height:100px;object-fit:cover;border-radius:8px;margin-bottom:.5rem}
.rs img.rs-img{width:100%;height:120px;object-fit:cover;border-radius:8px;margin-bottom:.8rem;cursor:pointer}
.cb{padding:1.5rem}.cb h3{font-size:1.15rem;margin-bottom:.5rem}.cb p{color:var(--gr);font-size:.93rem}
.cb a.more{display:inline-block;margin-top:.5rem;font-size:.85rem;font-weight:500;color:var(--sea);text-decoration:none}
.cb a.more:hover{color:var(--tc);text-decoration:underline}
.tag{display:inline-block;background:var(--sea-l);color:var(--sea);padding:.2rem .7rem;border-radius:20px;font-size:.8rem;font-weight:500;margin-top:.6rem;margin-right:.2rem}
.tag.dog{background:#FEF3C7;color:#92400E}
.ig{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:1rem;margin:1.5rem 0}
.ii{display:flex;align-items:center;gap:.7rem;padding:.7rem;background:var(--sand-light);border-radius:10px;font-size:.9rem}
.sf .ii{background:var(--wh)}.ii .em{font-size:1.3rem}
.ib{background:var(--sea-l);border-left:4px solid var(--sea);padding:1.2rem 1.5rem;border-radius:0 10px 10px 0;margin:1.5rem 0}
.ib.dog{background:#ECFDF5;border-color:#10B981}
.gal{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:1rem;margin:1.5rem 0}
.gal img{width:100%;height:200px;object-fit:cover;border-radius:12px;transition:transform .3s;cursor:pointer}.gal img:hover{transform:scale(1.03)}
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
.map-ph{width:100%;height:400px;border-radius:16px;background:linear-gradient(135deg,var(--sea-l),var(--sand));display:flex;flex-direction:column;align-items:center;justify-content:center;color:var(--sea);gap:1rem;margin-top:1.5rem;box-shadow:0 4px 20px rgba(0,0,0,.1)}
.lb-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.92);z-index:2000;cursor:pointer;align-items:center;justify-content:center}
.lb-overlay.active{display:flex}
.lb-overlay img{max-width:92vw;max-height:90vh;border-radius:8px;box-shadow:0 8px 40px rgba(0,0,0,.5)}
.lb-close{position:fixed;top:1rem;right:1.5rem;color:#fff;font-size:2.5rem;cursor:pointer;z-index:2001;line-height:1}
footer{background:var(--sea-d);color:var(--sand);text-align:center;padding:2rem 1.5rem;font-size:.85rem}
@media(max-width:768px){nav li a{padding:.8rem .6rem;font-size:.75rem}section{padding:3rem 1rem}.cd{gap:.7rem}.cd-i{padding:.8rem 1rem;min-width:70px}.cd-i .n{font-size:1.8rem}.cg,.rl{grid-template-columns:1fr}.gal{grid-template-columns:1fr 1fr}}
"""

JS = r"""
function uc(){var t=new Date('__COUNTDOWN__'),n=new Date(),d=t-n;if(d<=0){document.getElementById('cd').innerHTML='<p style="font-size:1.5rem">🎉 Der Urlaub hat begonnen!</p>';return}var dd=Math.floor(d/864e5),hh=Math.floor(d%864e5/36e5),mm=Math.floor(d%36e5/6e4),ss=Math.floor(d%6e4/1e3);document.getElementById('cd-d').textContent=dd;document.getElementById('cd-h').textContent=('0'+hh).slice(-2);document.getElementById('cd-m').textContent=('0'+mm).slice(-2);document.getElementById('cd-s').textContent=('0'+ss).slice(-2)}uc();setInterval(uc,1e3);
document.querySelectorAll('nav a').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();var t=document.querySelector(this.getAttribute('href'));if(t)window.scrollTo({top:t.getBoundingClientRect().top+window.pageYOffset-50,behavior:'smooth'})})});
var lb=document.getElementById('lightbox'),lbImg=document.getElementById('lb-img');
document.querySelectorAll('.gal img, .card img.ph-img, .rs img.rs-img').forEach(function(img){img.addEventListener('click',function(){lbImg.src=this.src;lb.classList.add('active')})});
document.querySelectorAll('.rmc.clickable').forEach(function(el){el.addEventListener('click',function(){var s=this.dataset.img;if(s){lbImg.src=s;lb.classList.add('active')}})});
lb.addEventListener('click',function(){lb.classList.remove('active')});
document.addEventListener('keydown',function(e){if(e.key==='Escape')lb.classList.remove('active')});
""".replace("__COUNTDOWN__", COUNTDOWN_TARGET)


# --------------------------------------------------------------------------
# HTML-Renderer-Helper
# --------------------------------------------------------------------------
def features_html():
    return "".join(f'<div class="ii"><span class="em">{e}</span> {t}</div>' for e, t in ACCOMMODATION["features"])

def rooms_html():
    out = []
    for n, d, photo in ACCOMMODATION["rooms"]:
        if photo:
            out.append(
                f'<div class="rmc clickable" data-img="{photo}" title="Klick fuer Foto">'
                f'<img class="room-thumb" src="{photo}" alt="{n}"><h4>{n}</h4><p>{d} \U0001F4F7</p></div>'
            )
        else:
            out.append(f'<div class="rmc"><div class="ro">\U0001F6CC</div><h4>{n}</h4><p>{d}</p></div>')
    return "".join(out)

def gallery_html():
    fotos = fotos_sorted()
    return "".join(f'<img src="haus_fotos/{f}" alt="Ferienhaus Foto" loading="lazy">' for f in fotos)

def weather_html():
    bgs = ["", "background:linear-gradient(135deg,#0891b2,#164e63)",
           "background:linear-gradient(135deg,#d97706,#92400e)",
           "background:linear-gradient(135deg,#6366f1,#312e81)"]
    return "".join(
        f'<div class="wc" style="{bgs[i]}"><div class="wi">{icon}</div><div class="wv">{val}</div><div class="wl">{lbl}</div></div>'
        for i, (icon, val, lbl) in enumerate(WEATHER)
    )

def _card_media(photo, fallback_emoji):
    if photo:
        return f'<img class="ph-img" src="{photo}" alt="" loading="lazy">'
    return f'<div class="ph">{fallback_emoji}</div>'

def beaches_html():
    return "".join(
        f'<div class="card">{_card_media(b.get("photo"), "\U0001F3D6️")}'
        f'<div class="cb"><h3>{b["name"]}</h3><p>{b["desc"]}</p>'
        f'<a class="more" href="{b["maps"]}" target="_blank">\U0001F697 Route</a><br>'
        f'<span class="tag">{b["tag"]}</span></div></div>' for b in BEACHES
    )

def attractions_html():
    return "".join(
        f'<div class="card">{_card_media(a.get("photo"), "\U0001F5FA️")}'
        f'<div class="cb"><h3>{a["name"]}</h3><p>{a["desc"]}</p>'
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
    out = []
    for r in REST_STOPS:
        img_html = f'<img class="rs-img" src="{r["photo"]}" alt="" loading="lazy">' if r.get("photo") else ""
        out.append(
            f'<div class="rs">{img_html}<h4>{r["name"]}</h4><div class="rsl">{r["loc"]}</div><p>{r["desc"]}</p>'
            f'<a class="rslink" href="{r["link"]}" target="_blank">→ Website</a> · '
            f'<a class="rslink" href="{r["maps"]}" target="_blank">\U0001F4CD Route</a></div>'
        )
    return "".join(out)


html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex,nofollow,noarchive,nosnippet">
<meta name="googlebot" content="noindex,nofollow">
<title>{TRIP_TITLE} – {ACCOMMODATION["name"]}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<nav><ul>
<li><a href="#hero">Start</a></li>
<li><a href="#haus">Unterkunft</a></li>
<li><a href="#anreise">Anreise</a></li>
<li><a href="#wetter">Wetter</a></li>
<li><a href="#straende">Strände</a></li>
<li><a href="#ausfluge">Ausflüge</a></li>
<li><a href="#restaurants">Restaurants</a></li>
<li><a href="#einkaufen">Einkaufen</a></li>
<li><a href="#karte">Karte</a></li>
</ul></nav>

<section class="hero" id="hero">
<div class="hero-bg" style="background-image:url('{HERO_PHOTO}')"></div>
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
<section id="haus">
<h2 class="st">Das Ferienhaus</h2>
<p class="ss">{ACCOMMODATION["name"]} · {ACCOMMODATION["location"]} ·
<a href="{ACCOMMODATION["booking"]}" target="_blank">\U0001F4F7 esmark.de</a></p>

<div class="gal">{gallery_html()}</div>

<h3 style="margin:2rem 0 .5rem">Ausstattung</h3>
<div class="ig">{features_html()}</div>

<h3 style="margin:2rem 0 .5rem">Zimmeraufteilung</h3>
<div class="rmg">{rooms_html()}</div>

<h3 style="margin:2rem 0 .5rem">Hausordnung</h3>
<div class="rg">
<div class="ri"><span class="ric">\U0001F551</span><div><strong>Check-in</strong> Sa 22.08.2026 ab 15:00 Uhr</div></div>
<div class="ri"><span class="ric">\U0001F559</span><div><strong>Check-out</strong> Sa 29.08.2026 bis 10:00 Uhr</div></div>
<div class="ri"><span class="ric">\U0001F465</span><div><strong>Max. Belegung</strong> 4 Personen</div></div>
<div class="ri"><span class="ric">\U0001F436</span><div><strong>Haustiere</strong> erlaubt (max. 2)</div></div>
<div class="ri"><span class="ric">\U0001F6AC</span><div><strong>Nichtraucherhaus</strong></div></div>
<div class="ri"><span class="ric">⭐</span><div><strong>3 Sterne</strong> (esmark-Klassifizierung)</div></div>
</div>
</section>

<!-- ANREISE -->
<section id="anreise" class="sf"><div class="si">
<h2 class="st">Anreise</h2>
<p class="ss">~{ROUTE["distance_km"]} km · {ROUTE["duration"]} Fahrt von Senden ·
<a href="{ROUTE["maps_link"]}" target="_blank">\U0001F697 Komplette Route auf Google Maps</a></p>

<h3 style="margin:2rem 0 1rem">Route-Hinweise</h3>
<div class="tc-grid">
<div class="tip"><h4>\U0001F1E9\U0001F1EA Deutschland</h4><p>A1 Richtung Bremen → Hamburg → A7 Richtung Flensburg. Samstags im Hochsommer Stau-Gefahr um Hamburg – früh losfahren.</p></div>
<div class="tip"><h4>\U0001F1E9\U0001F1F0 Daenemark</h4><p>Ab Grenze über E45 Richtung Kolding/Vejle, dann Abfahrt 73 Varde → Henne Strand. Keine Maut auf dänischen Autobahnen.</p></div>
<div class="tip"><h4>⛽ Tanken</h4><p>Kraftstoff in DK ist teurer als in DE. <strong>Noch in Deutschland volltanken</strong> (z.B. Hüttener Berge Ost).</p></div>
<div class="tip"><h4>\U0001F6A6 Tempolimit DK</h4><p>Motorvej 130, sonst 110 (Schild beachten!), Landstraße 80, innerorts 50. Licht auch tagsüber Pflicht.</p></div>
</div>

<h3 style="margin:2rem 0 1rem">\U0001F6D1 Empfohlene Raststätten</h3>
<div class="rst">{rest_stops_html()}</div>

</div></section>

<!-- WETTER -->
<section id="wetter">
<h2 class="st">Wetter Ende August</h2>
<p class="ss">Durchschnittswerte für die Westküste Daenemarks (Esbjerg-Station) · Quelle: climate-data.org</p>
<div class="wg">{weather_html()}</div>
<div class="ib" style="margin-top:1.5rem"><strong>\U0001F3D6️ Hinweis:</strong> Nordseeküsten-Wetter ist wechselhaft. Windjacke und Regenschutz immer dabei, auch bei Sonne.</div>
</section>

<!-- STRAENDE -->
<section id="straende" class="sf"><div class="si">
<h2 class="st">Strände</h2>
<p class="ss">Feiner weisser Sand, hohe Dünen, weite Nordsee</p>
<div class="ib dog"><strong>\U0001F436 Hunde-Regel Daenemark:</strong> Vom 1. April bis 30. September müssen Hunde am Strand angeleint sein, außerhalb der Saison dürfen sie frei laufen. An Blauflagge-Stränden sind Hunde vom 1. Juni bis 15. September ganz verboten. In Öksby gibt es einen ganzjährig freien Hundewald.</div>
<div class="cg">{beaches_html()}</div>
</div></section>

<!-- AUSFLUGSZIELE -->
<section id="ausfluge">
<h2 class="st">Sehenswürdigkeiten &amp; Ausflüge</h2>
<p class="ss">Natur, Geschichte und dänische Klassiker – alles im Umkreis von ~1 Stunde</p>
<div class="cg">{attractions_html()}</div>
</section>

<!-- RESTAURANTS -->
<section id="restaurants" class="sf"><div class="si">
<h2 class="st">Restaurants &amp; Essen</h2>
<p class="ss">Vom 2-Sterne-Kro bis zur Institutions-Eisdiele</p>
<div class="rl">{restaurants_html()}</div>
</div></section>

<!-- EINKAUFEN -->
<section id="einkaufen">
<h2 class="st">Einkaufen</h2>
<p class="ss">Supermarkt, Bäckerei &amp; Shopping im Ort</p>
<ul class="sl">{shopping_html()}</ul>
<div class="ib" style="margin-top:1.5rem"><strong>\U0001F4B6 Währung:</strong> Dänische Krone (DKK). Kartenzahlung nahezu überall, Bargeld selten nötig. 1 EUR ≈ 7,45 DKK (fester Kurs).</div>
</section>

<!-- KARTE -->
<section id="karte" class="sf"><div class="si">
<h2 class="st">Übersichtskarte</h2>
<p class="ss">Alle wichtigen Orte auf einen Blick</p>
<div class="map-ph">
<span style="font-size:3rem">\U0001F5FA️</span>
<a href="https://www.google.com/maps/search/?api=1&query={HOUSE_ADDR}" target="_blank" style="font-weight:500;font-size:1.1rem">Haus auf Google Maps öffnen →</a>
</div>
</div></section>

<!-- Lightbox -->
<div class="lb-overlay" id="lightbox">
<span class="lb-close">&times;</span>
<img id="lb-img" src="" alt="Vollbild">
</div>

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
print(f"Photos in gallery: {len(fotos_sorted())}")
