#!/usr/bin/env python3
"""Build the New York Libby library-systems dataset -> ny_libraries.json

New York has 23 public library systems organized by the State Education Dept.
Key Libby insight: ANY New York State resident can obtain free digital library
cards from the New York Public Library (NYPL), Brooklyn Public Library (BPL),
and Queens Public Library (QPL) — three of the largest Libby collections in
the country — regardless of which borough or county they reside in.

Each of the 23 systems maintains its own independent OverDrive/Libby collection.
"""
import json

# name, city, county, system_type, region, shared, note, lat, lon
D = [
 # ---- New York City (Consolidated systems) ----
 ("The New York Public Library","New York","New York","Consolidated","New York City","",
  "Serves Bronx, Manhattan, Staten Island. FREE digital card available to ALL New York State residents",
  40.7532,-73.9822),
 ("Brooklyn Public Library","Brooklyn","Kings","Consolidated","New York City","",
  "FREE digital card available to ALL New York State residents",
  40.6722,-73.9684),
 ("Queens Public Library","Jamaica","Queens","Consolidated","New York City","",
  "FREE digital card available to ALL New York State residents",
  40.7075,-73.7935),

 # ---- Long Island ----
 ("Nassau Library System","Uniondale","Nassau","Cooperative","Long Island","",
  "54 member libraries serving Nassau County",
  40.7226,-73.5923),
 ("Suffolk Cooperative Library System","Bellport","Suffolk","Cooperative","Long Island","",
  "56 member libraries serving Suffolk County",
  40.7573,-72.9393),

 # ---- Hudson Valley ----
 ("Westchester Library System","Elmsford","Westchester","Cooperative","Hudson Valley","",
  "38 member libraries serving Westchester County",
  41.0534,-73.8190),
 ("Mid-Hudson Library System","Poughkeepsie","Dutchess","Cooperative","Hudson Valley","",
  "Serves Columbia, Dutchess, Greene, Putnam, Ulster (part) counties. 66 member libraries",
  41.7004,-73.9209),
 ("Ramapo Catskill Library System","Middletown","Orange","Cooperative","Hudson Valley","",
  "Serves Orange, Rockland, Sullivan, Ulster (part) counties. 47 member libraries",
  41.4459,-74.4229),

 # ---- Capital Region ----
 ("Upper Hudson Library System","Albany","Albany","Cooperative","Capital Region","",
  "Serves Albany and Rensselaer counties. 29 member libraries",
  42.6526,-73.7562),
 ("Mohawk Valley Library System","Schenectady","Schenectady","Cooperative","Capital Region","",
  "Serves Fulton, Montgomery, Schenectady, Schoharie counties. 28 member libraries",
  42.8142,-73.9396),
 ("Southern Adirondack Library System","Saratoga Springs","Saratoga","Cooperative","Capital Region","",
  "Serves Hamilton, Saratoga, Warren, Washington counties. 34 member libraries",
  43.0831,-73.7846),

 # ---- Central New York ----
 ("Onondaga County Public Library","Syracuse","Onondaga","Federated","Central New York","",
  "Serves Onondaga County. 32 member libraries",
  43.0481,-76.1474),
 ("Mid York Library System","Utica","Oneida","Cooperative","Central New York","",
  "Serves Herkimer, Madison, Oneida counties. 43 member libraries",
  43.1009,-75.2327),
 ("Four County Library System","Vestal","Broome","Cooperative","Central New York","",
  "Serves Broome, Chenango, Delaware, Otsego counties. 42 member libraries",
  42.0851,-76.0546),
 ("Finger Lakes Library System","Ithaca","Tompkins","Cooperative","Central New York","",
  "Serves Cayuga, Cortland, Seneca, Tioga, Tompkins counties. 33 member libraries",
  42.4440,-76.5019),

 # ---- Western New York ----
 ("Monroe County Library System","Rochester","Monroe","Federated","Western New York","",
  "Serves Monroe County. Rochester Public Library is the central library",
  43.1566,-77.6088),
 ("Buffalo & Erie County Public Library","Buffalo","Erie","Federated","Western New York","",
  "Serves Erie County. 37 member libraries",
  42.8864,-78.8784),
 ("OWWL Library System","Canandaigua","Ontario","Cooperative","Western New York","",
  "Serves Livingston, Ontario, Wayne, Wyoming counties. 42 member libraries",
  42.8873,-77.2814),
 ("Nioga Library System","Lockport","Niagara","Cooperative","Western New York","",
  "Serves Genesee, Niagara, Orleans counties. 23 member libraries",
  43.1709,-78.6903),
 ("Chautauqua-Cattaraugus Library System","Jamestown","Chautauqua","Cooperative","Western New York","",
  "Serves Chautauqua and Cattaraugus counties. 38 member libraries",
  42.0970,-79.2353),
 ("Southern Tier Library System","Painted Post","Steuben","Cooperative","Western New York","",
  "Serves Allegany, Chemung, Schuyler, Steuben, Yates counties. 48 member libraries",
  42.1597,-77.0964),

 # ---- North Country ----
 ("North Country Library System","Watertown","Jefferson","Cooperative","North Country","",
  "Serves Jefferson, Lewis, Oswego, St. Lawrence counties. 65 member libraries",
  43.9748,-75.9108),
 ("Clinton-Essex-Franklin Library System","Plattsburgh","Clinton","Federated","North Country","",
  "Serves Clinton, Essex, Franklin counties. 33 member libraries",
  44.6995,-73.4529),
]

NO_LIBBY = {}

records = []
for (name, city, county, system_type, region, shared, note, lat, lon) in D:
    records.append({
        "name": name, "city": city, "county": county, "system": system_type,
        "region": region, "shared": shared, "note": note or NO_LIBBY.get(name, ""),
        "lat": lat, "lon": lon,
        "libby": name not in NO_LIBBY,
    })

assert len(records) == len({r["name"] for r in records}), "duplicate names!"
for r in records:
    assert 40.0 <= r["lat"] <= 45.5, f"lat OOB {r['name']} {r['lat']}"
    assert -80.0 <= r["lon"] <= -71.5, f"lon OOB {r['name']} {r['lon']}"

from collections import Counter
print("TOTAL systems:", len(records))
print("\nBy region:")
for k,v in sorted(Counter(r["region"] for r in records).items()):
    print(f"  {v:3d}  {k}")
print("\nBy system type:")
for k,v in sorted(Counter(r["system"] for r in records).items()):
    print(f"  {v:3d}  {k}")
print("\nCounties covered:", len({r["county"] for r in records}))

with open("data/ny_libraries.json","w", encoding="utf-8") as f:
    json.dump(records, f, indent=1)
print("Wrote ny_libraries.json")
