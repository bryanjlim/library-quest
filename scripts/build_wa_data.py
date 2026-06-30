#!/usr/bin/env python3
"""Build the Washington Libby library-systems dataset -> wa_libraries.json

Washington differs from California: there is no statewide open-borrowing policy.
Instead, library systems have pairwise reciprocal borrowing agreements.
Most smaller systems share one Libby catalog — the Washington Digital Library
Consortium (WDLC), branded "Washington Anytime Library."  The largest systems
maintain their own independent Libby/OverDrive collections.
"""
import json

# name, city, county, system, region, shared, note, lat, lon
D = [
 # ---- Independent Libby collections (not WDLC-shared) ----
 # Puget Sound
 ("King County Library System","Issaquah","King","Independent","Puget Sound","",
  "Reciprocal with SPL, Pierce County, Sno-Isle, Kitsap, Timberland, Fort Vancouver, NCW, Tacoma, Puyallup, North Olympic",
  47.5301,-122.0326),
 ("Seattle Public Library","Seattle","King","Independent","Puget Sound","",
  "Reciprocal with KCLS. Digital card available to any WA resident who works, attends school, or owns property in Seattle",
  47.6062,-122.3321),
 ("Pierce County Library System","Tacoma","Pierce","Independent","Puget Sound","",
  "Reciprocal with KCLS, SPL, Kitsap, Sno-Isle, Tacoma, Puyallup, Fort Vancouver, NCW, North Olympic, Timberland",
  47.2529,-122.4443),
 ("Tacoma Public Library","Tacoma","Pierce","Independent","Puget Sound","",
  "Reciprocal with Pierce County, KCLS",
  47.2529,-122.4543),

 # Eastern
 ("Spokane Public Library","Spokane","Spokane","Independent","Eastern Washington","",
  "",47.6588,-117.4260),
 ("Spokane County Library District","Spokane","Spokane","Independent","Eastern Washington","",
  "",47.6740,-117.3900),

 # ---- WDLC members (share Washington Anytime Library) ----
 # These systems give access to the shared WDLC Libby collection.
 # A card at any one WDLC member accesses the same digital catalog.

 # Puget Sound
 ("Puyallup Public Library","Puyallup","Pierce","WDLC","Puget Sound","WDLC shared",
  "Reciprocal with Pierce County, KCLS",
  47.1854,-122.2929),

 # North Sound
 ("Sno-Isle Libraries","Marysville","Snohomish","WDLC","North Sound","WDLC shared",
  "Serves Snohomish & Island counties. Reciprocal with KCLS, Pierce County",
  48.0518,-122.1771),
 ("Anacortes Public Library","Anacortes","Skagit","WDLC","North Sound","WDLC shared",
  "",48.5126,-122.6127),
 ("Bellingham Public Library","Bellingham","Whatcom","WDLC","North Sound","WDLC shared",
  "",48.7519,-122.4787),
 ("Burlington Public Library","Burlington","Skagit","WDLC","North Sound","WDLC shared",
  "",48.4757,-122.3254),
 ("Central Skagit Library","Sedro-Woolley","Skagit","WDLC","North Sound","WDLC shared",
  "",48.5036,-122.2362),
 ("Guemes Island Library","Anacortes","Skagit","WDLC","North Sound","WDLC shared",
  "",48.5541,-122.6310),
 ("La Conner Regional Library","La Conner","Skagit","WDLC","North Sound","WDLC shared",
  "",48.3924,-122.4957),
 ("Mount Vernon City Library","Mount Vernon","Skagit","WDLC","North Sound","WDLC shared",
  "",48.4201,-122.3341),
 ("Upper Skagit Library","Concrete","Skagit","WDLC","North Sound","WDLC shared",
  "",48.5391,-121.7516),
 ("Whatcom County Library System","Bellingham","Whatcom","WDLC","North Sound","WDLC shared",
  "Serves Whatcom County outside Bellingham",
  48.7800,-122.4600),

 # San Juan Islands
 ("Lopez Island Library","Lopez Island","San Juan","WDLC","San Juan Islands","WDLC shared",
  "",48.5138,-122.8975),
 ("Orcas Island Public Library","Eastsound","San Juan","WDLC","San Juan Islands","WDLC shared",
  "",48.6938,-122.9060),
 ("San Juan Island Library","Friday Harbor","San Juan","WDLC","San Juan Islands","WDLC shared",
  "",48.5343,-123.0170),
 ("Shaw Island Library","Shaw Island","San Juan","WDLC","San Juan Islands","WDLC shared",
  "",48.5842,-122.9290),

 # Olympic Peninsula
 ("Kitsap Regional Library","Bremerton","Kitsap","WDLC","Olympic Peninsula","WDLC shared",
  "Reciprocal with KCLS, Pierce County, North Olympic",
  47.5673,-122.6329),
 ("North Olympic Library System","Port Angeles","Clallam","WDLC","Olympic Peninsula","WDLC shared",
  "Reciprocal with KCLS, Kitsap, Pierce County",
  48.1184,-123.4307),
 ("Jefferson County Library","Port Hadlock","Jefferson","WDLC","Olympic Peninsula","WDLC shared",
  "",48.0330,-122.7580),
 ("Port Townsend Public Library","Port Townsend","Jefferson","WDLC","Olympic Peninsula","WDLC shared",
  "Free non-resident cards for KCLS, Kitsap, North Olympic cardholders",
  48.1170,-122.7604),

 # Southwest
 ("Fort Vancouver Regional Library","Vancouver","Clark","WDLC","Southwest Washington","WDLC shared",
  "Serves Clark, Skamania, Klickitat, part of Kittitas counties. Reciprocal with Pierce County, KCLS",
  45.6387,-122.6615),
 ("Timberland Regional Library","Tumwater","Thurston","WDLC","Southwest Washington","WDLC shared",
  "Serves Grays Harbor, Lewis, Mason, Pacific, Thurston counties. Reciprocal with KCLS, Pierce County",
  46.9960,-122.9049),
 ("Camas Public Library","Camas","Clark","WDLC","Southwest Washington","WDLC shared",
  "",45.5871,-122.3996),
 ("Castle Rock Public Library","Castle Rock","Cowlitz","WDLC","Southwest Washington","WDLC shared",
  "",46.2754,-122.9079),
 ("Cathlamet Public Library","Cathlamet","Wahkiakum","WDLC","Southwest Washington","WDLC shared",
  "",46.2026,-123.3828),
 ("Kalama Public Library","Kalama","Cowlitz","WDLC","Southwest Washington","WDLC shared",
  "",46.0084,-122.8446),
 ("Kelso Public Library","Kelso","Cowlitz","WDLC","Southwest Washington","WDLC shared",
  "",46.1468,-122.9085),
 ("Longview Public Library","Longview","Cowlitz","WDLC","Southwest Washington","WDLC shared",
  "",46.1382,-122.9382),
 ("Ocean Shores Public Library","Ocean Shores","Grays Harbor","WDLC","Southwest Washington","WDLC shared",
  "",46.9735,-124.1556),
 ("Carpenter Memorial Library","Cle Elum","Kittitas","WDLC","Southwest Washington","WDLC shared",
  "",47.1943,-120.9383),

 # Central Washington
 ("NCW Libraries","Wenatchee","Chelan","WDLC","Central Washington","WDLC shared",
  "Serves Chelan, Douglas, Grant, Okanogan, Ferry counties. Reciprocal with KCLS, Pierce County",
  47.4235,-120.3103),
 ("Mid-Columbia Libraries","Kennewick","Benton","WDLC","Central Washington","WDLC shared",
  "Serves Benton & Franklin counties",
  46.2112,-119.1372),
 ("Yakima Valley Libraries","Yakima","Yakima","WDLC","Central Washington","WDLC shared",
  "Serves Yakima County",
  46.6021,-120.5059),
 ("Ellensburg Public Library","Ellensburg","Kittitas","WDLC","Central Washington","WDLC shared",
  "",46.9965,-120.5478),
 ("Roslyn Public Library","Roslyn","Kittitas","WDLC","Central Washington","WDLC shared",
  "",47.2168,-120.9986),
 ("Gilmour Memorial Library","Kittitas","Kittitas","WDLC","Central Washington","WDLC shared",
  "",46.9834,-120.4177),

 # Eastern Washington
 ("Richland Public Library","Richland","Benton","WDLC","Eastern Washington","WDLC shared",
  "Reciprocal with Mid-Columbia, Walla Walla Public, Walla Walla County Rural, Columbia County Rural",
  46.2856,-119.2845),
 ("Walla Walla Public Library","Walla Walla","Walla Walla","WDLC","Eastern Washington","WDLC shared",
  "Reciprocal with Mid-Columbia, Richland, Walla Walla County Rural, Columbia County Rural",
  46.0646,-118.3430),
 ("Walla Walla County Rural Library District","Walla Walla","Walla Walla","WDLC","Eastern Washington","WDLC shared",
  "Reciprocal with Walla Walla Public, Mid-Columbia, Richland, Columbia County Rural",
  46.0800,-118.3100),
 ("Columbia County Rural Library District","Dayton","Columbia","WDLC","Eastern Washington","WDLC shared",
  "Reciprocal with Walla Walla Public, Walla Walla County Rural, Mid-Columbia, Richland",
  46.3233,-117.9726),
 ("Neill Public Library","Pullman","Whitman","WDLC","Eastern Washington","WDLC shared",
  "",46.7312,-117.1796),
 ("Whitman County Rural Library District","Colfax","Whitman","WDLC","Eastern Washington","WDLC shared",
  "",46.8800,-117.3650),
 ("East Adams Library District","Ritzville","Adams","WDLC","Eastern Washington","WDLC shared",
  "",47.1266,-118.3790),
 ("Liberty Lake Municipal Library","Liberty Lake","Spokane","WDLC","Eastern Washington","WDLC shared",
  "",47.6744,-117.1083),
 ("Davenport Public Library","Davenport","Lincoln","WDLC","Eastern Washington","WDLC shared",
  "",47.6543,-118.1500),
 ("Sprague Public Library","Sprague","Lincoln","WDLC","Eastern Washington","WDLC shared",
  "",47.3063,-117.9765),
 ("Odessa Public Library","Odessa","Lincoln","WDLC","Eastern Washington","WDLC shared",
  "",47.3335,-118.6876),
 ("Reardan Memorial Library","Reardan","Lincoln","WDLC","Eastern Washington","WDLC shared",
  "",47.6639,-117.8728),
 ("Hesseltine Public Library","Wilbur","Lincoln","WDLC","Eastern Washington","WDLC shared",
  "",47.7580,-118.7060),
 ("Harrington Public Library","Harrington","Lincoln","WDLC","Eastern Washington","WDLC shared",
  "",47.4788,-118.2548),
 ("Denny Ashby Library","Pomeroy","Garfield","WDLC","Eastern Washington","WDLC shared",
  "",46.4713,-117.6049),
 ("Weller Public Library","Waitsburg","Walla Walla","WDLC","Eastern Washington","WDLC shared",
  "",46.2677,-118.1526),
]

NO_LIBBY = {}

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
    assert 45.0 <= r["lat"] <= 49.1, f"lat OOB {r['name']} {r['lat']}"
    assert -125.0 <= r["lon"] <= -116.5, f"lon OOB {r['name']} {r['lon']}"

from collections import Counter
print("TOTAL systems:", len(records))
print("\nBy region:")
for k,v in sorted(Counter(r["region"] for r in records).items()):
    print(f"  {v:3d}  {k}")
print("\nBy system type:")
for k,v in sorted(Counter(r["system"] for r in records).items()):
    print(f"  {v:3d}  {k}")
print("\nCounties covered:", len({r["county"] for r in records}))

with open("data/wa_libraries.json","w", encoding="utf-8") as f:
    json.dump(records, f, indent=1)
print("Wrote wa_libraries.json")
