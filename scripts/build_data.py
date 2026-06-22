#!/usr/bin/env python3
"""Build the California Libby library-systems dataset -> ca_libraries.json"""
import json

# name, city, county, system (cooperative), region (travel grouping),
# shared (shared Libby/OverDrive collection or "" = own), note, lat, lon
D = [
 # ---------------- Black Gold (Central Coast) ----------------
 ("Carpinteria Library","Carpinteria","Santa Barbara","Black Gold","Central Coast","Black Gold shared","",34.3989,-119.5185),
 ("Goleta Public Library","Goleta","Santa Barbara","Black Gold","Central Coast","Black Gold shared","",34.4358,-119.8276),
 ("Lompoc Public Library","Lompoc","Santa Barbara","Black Gold","Central Coast","Black Gold shared","",34.6391,-120.4579),
 ("Paso Robles City Library","Paso Robles","San Luis Obispo","Black Gold","Central Coast","Black Gold shared","",35.6269,-120.6910),
 ("Santa Maria Public Library","Santa Maria","Santa Barbara","Black Gold","Central Coast","Black Gold shared","",34.9530,-120.4357),
 ("Santa Paula (Blanchard Community) Library","Santa Paula","Ventura","Black Gold","Central Coast","Black Gold shared","",34.3542,-119.0593),

 # ---------------- Inland (Inland Empire / Desert) ----------------
 ("Banning Library District","Banning","Riverside","Inland","Inland Empire","","Joint-use w/ school district",33.9256,-116.8761),
 ("Beaumont Library District","Beaumont","Riverside","Inland","Inland Empire","","",33.9295,-116.9770),
 ("Colton Public Library","Colton","San Bernardino","Inland","Inland Empire","","",34.0739,-117.3137),
 ("Corona Public Library","Corona","Riverside","Inland","Inland Empire","","",33.8753,-117.5664),
 ("Hemet Public Library","Hemet","Riverside","Inland","Inland Empire","","",33.7475,-116.9719),
 ("Inyo County Free Library","Independence","Inyo","Inland","Inland Empire","","",36.8027,-118.2001),
 ("Palm Desert Public Library","Palm Desert","Riverside","Inland","Inland Empire","","",33.7223,-116.3744),
 ("Moreno Valley Public Library","Moreno Valley","Riverside","Inland","Inland Empire","","",33.9425,-117.2297),
 ("Murrieta Public Library","Murrieta","Riverside","Inland","Inland Empire","","",33.5539,-117.2139),
 ("Ontario City Library","Ontario","San Bernardino","Inland","Inland Empire","","",34.0633,-117.6509),
 ("Palm Springs Public Library","Palm Springs","Riverside","Inland","Inland Empire","","",33.8303,-116.5453),
 ("Palo Verde Valley District Library","Blythe","Riverside","Inland","Inland Empire","","",33.6103,-114.5964),
 ("Rancho Cucamonga Public Library","Rancho Cucamonga","San Bernardino","Inland","Inland Empire","","",34.1064,-117.5931),
 ("Rancho Mirage Public Library","Rancho Mirage","Riverside","Inland","Inland Empire","","",33.7397,-116.4128),
 ("Riverside County Library System","Riverside","Riverside","Inland","Inland Empire","","",33.9806,-117.3755),
 ("Riverside Public Library","Riverside","Riverside","Inland","Inland Empire","","",33.9825,-117.3735),
 ("San Bernardino County Library","San Bernardino","San Bernardino","Inland","Inland Empire","","",34.1083,-117.2898),
 ("San Bernardino Public Library","San Bernardino","San Bernardino","Inland","Inland Empire","","",34.1066,-117.2861),
 ("Upland Public Library","Upland","San Bernardino","Inland","Inland Empire","","",34.0975,-117.6484),
 ("Victorville City Library","Victorville","San Bernardino","Inland","Inland Empire","","",34.5362,-117.2928),

 # ---------------- NorthNet: MVLS (Sacramento / Sierra) ----------------
 ("Alpine County Library","Markleeville","Alpine","NorthNet (MVLS)","Sacramento & Sierra","NCDL shared","",38.6946,-119.7782),
 ("Colusa County Free Library","Colusa","Colusa","NorthNet (MVLS)","Sacramento & Sierra","NCDL shared","",39.2143,-122.0094),
 ("El Dorado County Library","Placerville","El Dorado","NorthNet (MVLS)","Sacramento & Sierra","NCDL shared","",38.7296,-120.7985),
 ("Folsom Public Library","Folsom","Sacramento","NorthNet (MVLS)","Sacramento & Sierra","NCDL shared","",38.6779,-121.1761),
 ("Lincoln Public Library","Lincoln","Placer","NorthNet (MVLS)","Sacramento & Sierra","NCDL shared","",38.8916,-121.2930),
 ("Mono County Free Library","Bridgeport","Mono","NorthNet (MVLS)","Sacramento & Sierra","NCDL shared","",38.2566,-119.2310),
 ("Nevada County Library","Nevada City","Nevada","NorthNet (MVLS)","Sacramento & Sierra","NCDL shared","",39.2616,-121.0161),
 ("Placer County Library","Auburn","Placer","NorthNet (MVLS)","Sacramento & Sierra","NCDL shared","",38.8966,-121.0769),
 ("Roseville Public Library","Roseville","Placer","NorthNet (MVLS)","Sacramento & Sierra","NCDL shared","",38.7521,-121.2880),
 ("Sacramento Public Library","Sacramento","Sacramento","NorthNet (MVLS)","Sacramento & Sierra","","Also own Libby collection",38.5816,-121.4944),
 ("Sutter County Library","Yuba City","Sutter","NorthNet (MVLS)","Sacramento & Sierra","NCDL shared","",39.1404,-121.6169),
 ("Woodland Public Library","Woodland","Yolo","NorthNet (MVLS)","Sacramento & Sierra","NCDL shared","",38.6785,-121.7733),
 ("Yolo County Library","Davis","Yolo","NorthNet (MVLS)","Sacramento & Sierra","NCDL shared","",38.5449,-121.7405),
 ("Yuba County Library","Marysville","Yuba","NorthNet (MVLS)","Sacramento & Sierra","NCDL shared","",39.1457,-121.5914),

 # ---------------- NorthNet: North Bay ----------------
 ("Belvedere-Tiburon Library","Tiburon","Marin","NorthNet (North Bay)","North Bay","NCDL shared","",37.8736,-122.4566),
 ("Benicia Public Library","Benicia","Solano","NorthNet (North Bay)","North Bay","NCDL shared","",38.0494,-122.1586),
 ("Dixon Public Library","Dixon","Solano","NorthNet (North Bay)","North Bay","NCDL shared","",38.4455,-121.8233),
 ("Lake County Library","Lakeport","Lake","NorthNet (North Bay)","North Bay","NCDL shared","",39.0429,-122.9158),
 ("Larkspur Public Library","Larkspur","Marin","NorthNet (North Bay)","North Bay","NCDL shared","",37.9341,-122.5353),
 ("Marin County Free Library","San Rafael","Marin","NorthNet (North Bay)","North Bay","NCDL shared","",38.0827,-122.5333),
 ("Mendocino County Library","Ukiah","Mendocino","NorthNet (North Bay)","North Bay","NCDL shared","",39.1502,-123.2078),
 ("Mill Valley Public Library","Mill Valley","Marin","NorthNet (North Bay)","North Bay","NCDL shared","",37.9061,-122.5450),
 ("Napa County Library","Napa","Napa","NorthNet (North Bay)","North Bay","NCDL shared","",38.2975,-122.2869),
 ("San Anselmo Public Library","San Anselmo","Marin","NorthNet (North Bay)","North Bay","NCDL shared","",37.9746,-122.5616),
 ("San Rafael Public Library","San Rafael","Marin","NorthNet (North Bay)","North Bay","NCDL shared","",37.9735,-122.5311),
 ("Sausalito Public Library","Sausalito","Marin","NorthNet (North Bay)","North Bay","NCDL shared","",37.8591,-122.4853),
 ("Solano County Library","Fairfield","Solano","NorthNet (North Bay)","North Bay","NCDL shared","",38.2494,-122.0399),
 ("Sonoma County Library","Santa Rosa","Sonoma","NorthNet (North Bay)","North Bay","","Also own Libby collection",38.4405,-122.7141),
 ("St. Helena Public Library","St. Helena","Napa","NorthNet (North Bay)","North Bay","NCDL shared","",38.5052,-122.4703),

 # ---------------- NorthNet: North State (Far North) ----------------
 ("Butte County Library","Oroville","Butte","NorthNet (North State)","Far North","NCDL shared","",39.5138,-121.5564),
 ("Del Norte County Library District","Crescent City","Del Norte","NorthNet (North State)","Far North","NCDL shared","",41.7558,-124.2026),
 ("Humboldt County Library","Eureka","Humboldt","NorthNet (North State)","Far North","NCDL shared","",40.8021,-124.1637),
 ("Lassen Library District","Susanville","Lassen","NorthNet (North State)","Far North","NCDL shared","",40.4163,-120.6530),
 ("Modoc County Library","Alturas","Modoc","NorthNet (North State)","Far North","NCDL shared","",41.4871,-120.5424),
 ("Orland Free Library","Orland","Glenn","NorthNet (North State)","Far North","NCDL shared","",39.7474,-122.1964),
 ("Plumas County Library","Quincy","Plumas","NorthNet (North State)","Far North","NCDL shared","",39.9368,-120.9472),
 ("Shasta Public Libraries","Redding","Shasta","NorthNet (North State)","Far North","NCDL shared","",40.5865,-122.3917),
 ("Siskiyou County Free Library","Yreka","Siskiyou","NorthNet (North State)","Far North","NCDL shared","",41.7354,-122.6345),
 ("Tehama County Library","Red Bluff","Tehama","NorthNet (North State)","Far North","NCDL shared","",40.1785,-122.2358),
 ("Trinity County Library","Weaverville","Trinity","NorthNet (North State)","Far North","NCDL shared","",40.7307,-122.9420),
 ("Willows Public Library","Willows","Glenn","NorthNet (North State)","Far North","NCDL shared","",39.5243,-122.1936),

 # ---------------- Pacific: BALIS (Bay Area) ----------------
 ("Alameda County Library","Fremont","Alameda","Pacific (BALIS)","San Francisco Bay Area","","",37.5485,-121.9886),
 ("Alameda Free Library","Alameda","Alameda","Pacific (BALIS)","San Francisco Bay Area","","",37.7652,-122.2416),
 ("Berkeley Public Library","Berkeley","Alameda","Pacific (BALIS)","San Francisco Bay Area","","",37.8715,-122.2730),
 ("Contra Costa County Library","Pleasant Hill","Contra Costa","Pacific (BALIS)","San Francisco Bay Area","","",37.9480,-122.0608),
 ("Hayward Public Library","Hayward","Alameda","Pacific (BALIS)","San Francisco Bay Area","","",37.6688,-122.0808),
 ("Livermore Public Library","Livermore","Alameda","Pacific (BALIS)","San Francisco Bay Area","","",37.6819,-121.7680),
 ("Oakland Public Library","Oakland","Alameda","Pacific (BALIS)","San Francisco Bay Area","","",37.8044,-122.2712),
 ("Pleasanton Public Library","Pleasanton","Alameda","Pacific (BALIS)","San Francisco Bay Area","","",37.6624,-121.8747),
 ("Richmond Public Library","Richmond","Contra Costa","Pacific (BALIS)","San Francisco Bay Area","","",37.9358,-122.3477),
 ("San Francisco Public Library","San Francisco","San Francisco","Pacific (BALIS)","San Francisco Bay Area","","",37.7790,-122.4156),
 ("San Leandro Public Library","San Leandro","Alameda","Pacific (BALIS)","San Francisco Bay Area","","",37.7249,-122.1561),

 # ---------------- Pacific: MOBAC (Monterey Bay) ----------------
 ("Harrison Memorial Library (Carmel)","Carmel-by-the-Sea","Monterey","Pacific (MOBAC)","Monterey Bay","","",36.5552,-121.9233),
 ("Monterey County Free Libraries","Salinas","Monterey","Pacific (MOBAC)","Monterey Bay","","",36.6777,-121.6555),
 ("Monterey Public Library","Monterey","Monterey","Pacific (MOBAC)","Monterey Bay","","",36.6002,-121.8947),
 ("Pacific Grove Public Library","Pacific Grove","Monterey","Pacific (MOBAC)","Monterey Bay","","",36.6177,-121.9166),
 ("Salinas Public Library","Salinas","Monterey","Pacific (MOBAC)","Monterey Bay","","",36.6745,-121.6552),
 ("San Benito County Free Library","Hollister","San Benito","Pacific (MOBAC)","Monterey Bay","","",36.8525,-121.4016),
 ("San Juan Bautista City Library","San Juan Bautista","San Benito","Pacific (MOBAC)","Monterey Bay","","",36.8455,-121.5380),
 ("Santa Cruz Public Libraries","Santa Cruz","Santa Cruz","Pacific (MOBAC)","Monterey Bay","","",36.9741,-122.0308),
 ("Watsonville Public Library","Watsonville","Santa Cruz","Pacific (MOBAC)","Monterey Bay","","",36.9102,-121.7569),

 # ---------------- Pacific: Peninsula ----------------
 ("Burlingame Public Library","Burlingame","San Mateo","Pacific (Peninsula)","Peninsula","Peninsula shared","",37.5841,-122.3661),
 ("Daly City Public Library","Daly City","San Mateo","Pacific (Peninsula)","Peninsula","Peninsula shared","",37.6879,-122.4702),
 ("Menlo Park Public Library","Menlo Park","San Mateo","Pacific (Peninsula)","Peninsula","Peninsula shared","",37.4530,-122.1817),
 ("Redwood City Public Library","Redwood City","San Mateo","Pacific (Peninsula)","Peninsula","Peninsula shared","",37.4852,-122.2364),
 ("San Bruno Public Library","San Bruno","San Mateo","Pacific (Peninsula)","Peninsula","Peninsula shared","",37.6305,-122.4111),
 ("San Mateo County Libraries","Belmont","San Mateo","Pacific (Peninsula)","Peninsula","Peninsula shared","",37.5202,-122.2758),
 ("San Mateo Public Library","San Mateo","San Mateo","Pacific (Peninsula)","Peninsula","Peninsula shared","",37.5630,-122.3255),
 ("South San Francisco Public Library","South San Francisco","San Mateo","Pacific (Peninsula)","Peninsula","Peninsula shared","",37.6547,-122.4077),

 # ---------------- Pacific: Silicon Valley ----------------
 ("Los Gatos Public Library","Los Gatos","Santa Clara","Pacific (Silicon Valley)","Silicon Valley","","",37.2261,-121.9747),
 ("Mountain View Public Library","Mountain View","Santa Clara","Pacific (Silicon Valley)","Silicon Valley","","",37.3861,-122.0839),
 ("Palo Alto City Library","Palo Alto","Santa Clara","Pacific (Silicon Valley)","Silicon Valley","","",37.4419,-122.1430),
 ("San Jose Public Library","San Jose","Santa Clara","Pacific (Silicon Valley)","Silicon Valley","","",37.3382,-121.8863),
 ("Santa Clara City Library","Santa Clara","Santa Clara","Pacific (Silicon Valley)","Silicon Valley","","",37.3541,-121.9552),
 ("Santa Clara County Library District","Campbell","Santa Clara","Pacific (Silicon Valley)","Silicon Valley","","",37.2872,-121.9500),
 ("Sunnyvale Public Library","Sunnyvale","Santa Clara","Pacific (Silicon Valley)","Silicon Valley","","",37.3688,-122.0363),

 # ---------------- Santiago (Orange County) ----------------
 ("Anaheim Public Library","Anaheim","Orange","Santiago","Orange County","","",33.8366,-117.9143),
 ("Buena Park Library District","Buena Park","Orange","Santiago","Orange County","","",33.8675,-117.9981),
 ("Fullerton Public Library","Fullerton","Orange","Santiago","Orange County","","",33.8704,-117.9242),
 ("Huntington Beach Public Library","Huntington Beach","Orange","Santiago","Orange County","","",33.6595,-117.9988),
 ("Mission Viejo Library","Mission Viejo","Orange","Santiago","Orange County","","",33.6000,-117.6720),
 ("Newport Beach Public Library","Newport Beach","Orange","Santiago","Orange County","","",33.6189,-117.9298),
 ("OC Public Libraries","Santa Ana","Orange","Santiago","Orange County","","",33.7175,-117.8311),
 ("Orange Public Library","Orange","Orange","Santiago","Orange County","","",33.7879,-117.8531),
 ("Placentia Library District","Placentia","Orange","Santiago","Orange County","","",33.8722,-117.8703),
 ("Santa Ana Public Library","Santa Ana","Orange","Santiago","Orange County","","",33.7455,-117.8677),
 ("Yorba Linda Public Library","Yorba Linda","Orange","Santiago","Orange County","","",33.8886,-117.8131),

 # ---------------- Serra (San Diego & Imperial) ----------------
 ("Brawley Public Library","Brawley","Imperial","Serra","San Diego & Imperial","Serra shared","",32.9787,-115.5300),
 ("Camarena Memorial Library (Calexico)","Calexico","Imperial","Serra","San Diego & Imperial","Serra shared","",32.6789,-115.4989),
 ("Carlsbad City Library","Carlsbad","San Diego","Serra","San Diego & Imperial","Serra shared","",33.1581,-117.3506),
 ("Chula Vista Public Library","Chula Vista","San Diego","Serra","San Diego & Imperial","Serra shared","",32.6401,-117.0842),
 ("Coronado Public Library","Coronado","San Diego","Serra","San Diego & Imperial","Serra shared","",32.6859,-117.1831),
 ("El Centro Public Library","El Centro","Imperial","Serra","San Diego & Imperial","Serra shared","",32.7920,-115.5631),
 ("Escondido Public Library","Escondido","San Diego","Serra","San Diego & Imperial","Serra shared","",33.1192,-117.0864),
 ("Imperial County Free Library","El Centro","Imperial","Serra","San Diego & Imperial","Serra shared","",32.8000,-115.5550),
 ("Imperial Public Library","Imperial","Imperial","Serra","San Diego & Imperial","Serra shared","",32.8475,-115.5694),
 ("National City Public Library","National City","San Diego","Serra","San Diego & Imperial","Serra shared","",32.6781,-117.0992),
 ("Oceanside Public Library","Oceanside","San Diego","Serra","San Diego & Imperial","Serra shared","",33.1959,-117.3795),
 ("San Diego County Library","San Diego","San Diego","Serra","San Diego & Imperial","","Also own Libby collection",32.8328,-117.1490),
 ("San Diego Public Library","San Diego","San Diego","Serra","San Diego & Imperial","","Also own Libby collection",32.7157,-117.1611),

 # ---------------- SJVLS (San Joaquin Valley) ----------------
 ("Coalinga-Huron Library District","Coalinga","Fresno","SJVLS","San Joaquin Valley","SJVLS shared","",36.1397,-120.3601),
 ("Fresno County Public Library","Fresno","Fresno","SJVLS","San Joaquin Valley","SJVLS shared","",36.7378,-119.7871),
 ("Kern County Library","Bakersfield","Kern","SJVLS","San Joaquin Valley","SJVLS shared","",35.3733,-119.0187),
 ("Kings County Library","Hanford","Kings","SJVLS","San Joaquin Valley","SJVLS shared","",36.3275,-119.6457),
 ("Madera County Library","Madera","Madera","SJVLS","San Joaquin Valley","SJVLS shared","",36.9613,-120.0607),
 ("Mariposa County Library","Mariposa","Mariposa","SJVLS","San Joaquin Valley","SJVLS shared","",37.4849,-119.9663),
 ("Merced County Library","Merced","Merced","SJVLS","San Joaquin Valley","SJVLS shared","",37.3022,-120.4830),
 ("Porterville Public Library","Porterville","Tulare","SJVLS","San Joaquin Valley","SJVLS shared","",36.0652,-119.0168),
 ("Tulare County Library","Visalia","Tulare","SJVLS","San Joaquin Valley","SJVLS shared","",36.3302,-119.2921),
 ("Tulare Public Library","Tulare","Tulare","SJVLS","San Joaquin Valley","SJVLS shared","",36.2077,-119.3473),

 # ---------------- Southern California: MCLS (LA / Ventura) ----------------
 ("Alhambra Public Library","Alhambra","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.0953,-118.1270),
 ("Altadena Library District","Altadena","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.1897,-118.1312),
 ("Arcadia Public Library","Arcadia","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.1397,-118.0353),
 ("Azusa City Library","Azusa","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.1336,-117.9076),
 ("Beverly Hills Public Library","Beverly Hills","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","Free card only for LA/Orange/Ventura residents; others pay a fee",34.0696,-118.4004),
 ("Burbank Public Library","Burbank","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.1808,-118.3090),
 ("Calabasas Public Library","Calabasas","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.1367,-118.6614),
 ("Camarillo Public Library","Camarillo","Ventura","Southern California (MCLS)","Greater Los Angeles","","",34.2164,-119.0376),
 ("City of Commerce Public Library","Commerce","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",33.9961,-118.1597),
 ("Covina Public Library","Covina","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.0900,-117.8903),
 ("Downey City Library","Downey","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",33.9401,-118.1332),
 ("El Segundo Public Library","El Segundo","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",33.9192,-118.4165),
 ("Glendale Public Library","Glendale","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.1425,-118.2551),
 ("Glendora Library & Cultural Center","Glendora","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.1361,-117.8653),
 ("Irwindale Public Library","Irwindale","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.1070,-117.9351),
 ("Long Beach Public Library","Long Beach","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",33.7701,-118.1937),
 ("Los Angeles Public Library","Los Angeles","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.0537,-118.2428),
 ("Monrovia Public Library","Monrovia","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.1443,-118.0019),
 ("Bruggemeyer Library (Monterey Park)","Monterey Park","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.0625,-118.1228),
 ("Moorpark City Library","Moorpark","Ventura","Southern California (MCLS)","Greater Los Angeles","","",34.2856,-118.8820),
 ("Oxnard Public Library","Oxnard","Ventura","Southern California (MCLS)","Greater Los Angeles","","",34.1975,-119.1771),
 ("Palos Verdes Library District","Rolling Hills Estates","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",33.7717,-118.3870),
 ("Pomona Public Library","Pomona","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.0551,-117.7500),
 ("Redondo Beach Public Library","Redondo Beach","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",33.8492,-118.3884),
 ("San Marino Public Library","San Marino","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.1212,-118.1065),
 ("Santa Clarita Public Library","Santa Clarita","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.3917,-118.5426),
 ("Santa Fe Springs City Library","Santa Fe Springs","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",33.9472,-118.0853),
 ("Santa Monica Public Library","Santa Monica","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.0157,-118.4955),
 ("Sierra Madre Public Library","Sierra Madre","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.1612,-118.0531),
 ("Signal Hill Public Library","Signal Hill","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",33.8042,-118.1681),
 ("Simi Valley Public Library","Simi Valley","Ventura","Southern California (MCLS)","Greater Los Angeles","","",34.2694,-118.7815),
 ("South Pasadena Public Library","South Pasadena","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",34.1161,-118.1503),
 ("Thousand Oaks Library","Thousand Oaks","Ventura","Southern California (MCLS)","Greater Los Angeles","","",34.1706,-118.8376),
 ("Torrance Public Library","Torrance","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",33.8358,-118.3406),
 ("Ventura County Library","Ventura","Ventura","Southern California (MCLS)","Greater Los Angeles","","",34.2746,-119.2290),
 ("Whittier Public Library","Whittier","Los Angeles","Southern California (MCLS)","Greater Los Angeles","","",33.9792,-118.0328),

 # ---------------- Southern California: South State ----------------
 ("LA County Library","Downey","Los Angeles","Southern California (South State)","Greater Los Angeles","","",33.9379,-118.1370),
 ("Inglewood Public Library","Inglewood","Los Angeles","Southern California (South State)","Greater Los Angeles","","",33.9617,-118.3531),
 ("Palmdale City Library","Palmdale","Los Angeles","Southern California (South State)","Greater Los Angeles","","",34.5794,-118.1165),
 ("Pasadena Public Library","Pasadena","Los Angeles","Southern California (South State)","Greater Los Angeles","","",34.1478,-118.1445),

 # ---------------- 49-99 (Gold Country / North San Joaquin) ----------------
 ("Amador County Library","Jackson","Amador","49-99 Cooperative","Gold Country","","",38.3488,-120.7741),
 ("Calaveras County Library","San Andreas","Calaveras","49-99 Cooperative","Gold Country","","",38.1960,-120.6807),
 ("Lodi Public Library","Lodi","San Joaquin","49-99 Cooperative","Gold Country","","",38.1302,-121.2724),
 ("Stanislaus County Library","Modesto","Stanislaus","49-99 Cooperative","Gold Country","","",37.6391,-120.9969),
 ("Stockton-San Joaquin County Public Library","Stockton","San Joaquin","49-99 Cooperative","Gold Country","","",37.9577,-121.2908),
 ("Tuolumne County Library","Sonora","Tuolumne","49-99 Cooperative","Gold Country","","",37.9841,-120.3822),
]

# Systems that do NOT use Libby/OverDrive (use cloudLibrary/Hoopla/etc. instead).
# The value is the explanatory note shown in the popup for that system.
NO_LIBBY = {
    "Glendale Public Library": "Does not use Libby; left OverDrive in 2020 and now uses cloudLibrary and Hoopla.",
}

records = []
for (name, city, county, system, region, shared, note, lat, lon) in D:
    records.append({
        "name": name, "city": city, "county": county, "system": system,
        "region": region, "shared": shared, "note": note or NO_LIBBY.get(name, ""),
        "lat": lat, "lon": lon,
        "libby": name not in NO_LIBBY,
    })

assert len(records) == len({r["name"] for r in records}), "duplicate names!"
for r in records:
    assert 32.4 <= r["lat"] <= 42.1, f"lat OOB {r['name']} {r['lat']}"
    assert -124.6 <= r["lon"] <= -114.0, f"lon OOB {r['name']} {r['lon']}"

from collections import Counter
print("TOTAL systems:", len(records))
print("\nBy region:")
for k,v in sorted(Counter(r["region"] for r in records).items()):
    print(f"  {v:3d}  {k}")
print("\nBy cooperative:")
for k,v in sorted(Counter(r["system"] for r in records).items()):
    print(f"  {v:3d}  {k}")
print("\nCounties covered:", len({r["county"] for r in records}))

with open("data/ca_libraries.json","w", encoding="utf-8") as f:
    json.dump(records, f, indent=1)
print("Wrote ca_libraries.json")
