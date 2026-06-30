# Library Quest 📚

An interactive library-card quest site tracking which library systems you can get cards at, and which Libby catalogs each card unlocks.

## Supported States

- **California** — ~182 systems across 57 counties. Any CA resident can get a card at any system.
- **New York** — 23 public library systems, each with its own Libby catalog. Any NYS resident can get free digital cards at NYPL, Brooklyn, and Queens.

## Pages

[`index.html`](index.html) is the home page. [`california.html`](california.html) and [`newyork.html`](newyork.html) are the state maps.

## Features

- **181 Libby‑offering systems** plotted (plus Glendale shown but flagged — it left Libby in 2020).
- Mark cards **collected** (saved in your browser via `localStorage`); collected shows a ✓ check (colorblind‑safe) plus gold.
- **Shared‑catalog grouping**: libraries that pool one Libby catalog (NCDL, Black Gold, Serra, SJVLS, Peninsula) are marked together — collecting one in a group is enough, since they share the same books *and* the same holds queue. Independent libraries each have their own catalog and waitlist.
- **Rail overlay** (toggleable): Amtrak corridors (Surfliner, San Joaquins, Capitol Corridor, Coast Starlight) plus BART, Caltrain, Metrolink, ACE, SMART, COASTER, SPRINTER, and LA Metro — schematic station‑to‑station corridors for trip planning.
- Search, region/catalog filter, sidebar list, progress meter, per‑pin "Open in Google Maps" link, and an info panel.

## Project layout

```
data/ca_libraries.json      # CA dataset (182 systems)
data/ca_library_urls.json   # official library card / website links
data/ny_libraries.json      # NY dataset (23 systems)
scripts/build_data.py       # generates data/ca_libraries.json
scripts/build_california.py # builds california.html
scripts/build_ny_data.py    # generates data/ny_libraries.json
scripts/build_newyork.py    # builds newyork.html
index.html                  # home page
california.html             # California map
newyork.html                # New York map
```

## Rebuilding

Run from the repo root:

```bash
# California
python3 scripts/build_data.py
python3 scripts/build_california.py

# New York
python3 scripts/build_ny_data.py
python3 scripts/build_newyork.py
```

## Data notes & caveats

- System list is the California State Library's CLSA member jurisdictions (2023–24) — ~182 systems across 57 of 58 counties.
- Libby availability and non‑resident eligibility are **best‑effort** from official library and consortium sites; a few small systems may have changed. Notable flags: Glendale (no Libby), Beverly Hills (free card only for LA/Orange/Ventura residents), Banning (joint‑use school district).
- Each pin is a library **system** (one card per system), not an individual branch — a county system's many branches share one dot and one card.
- Coordinates are city/branch‑level placements (good for a state map, not turn‑by‑turn). Rail lines are schematic corridors between real stations.
