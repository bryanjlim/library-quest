# Library Quest 📚

An interactive library-card quest site. Track the public library cards you collect to unlock more ebooks and audiobooks in the Libby app.

## Supported States

### California
California residents can get a library card at any public library system in the state (in person with a CA ID; many also online). Each card unlocks that system's digital collection in Libby.

### Washington
Washington has no statewide open-borrowing law. Library systems form **reciprocal borrowing agreements** that let cardholders use partner libraries. Most smaller systems share one Libby catalog through the **Washington Digital Library Consortium (WDLC)**, branded "Washington Anytime Library." The largest systems (KCLS, Seattle Public Library, Pierce County, Spokane) maintain independent Libby collections.

### New York
New York has **23 public library systems**, each with its own independent Libby collection. **Any NYS resident** can get free digital library cards at The New York Public Library (NYPL), Brooklyn Public Library, and Queens Public Library — three of the largest Libby collections in the country.

## Pages

[`index.html`](index.html) is the home page. State maps: [`california.html`](california.html), [`washington.html`](washington.html), [`newyork.html`](newyork.html).

## Features

- Mark cards **collected** (saved in your browser via `localStorage`); collected shows a ✓ check (colorblind‑safe) plus gold.
- **Shared‑catalog grouping**: libraries that pool one Libby catalog share a color — collecting one in a group is enough, since they share the same books *and* the same holds queue.
- **Rail overlay** (toggleable): schematic station‑to‑station corridors for trip planning.
- Search, region/catalog filter, sidebar list, progress meter, per‑pin "Open in Google Maps" link, and an info panel.

## Project layout

```
data/ca_libraries.json       # California dataset (182 systems)
data/ca_library_urls.json    # California library card / website links
data/wa_libraries.json       # Washington dataset (57 systems)
data/ny_libraries.json       # New York dataset (23 systems)
scripts/build_data.py        # generates data/ca_libraries.json
scripts/build_wa_data.py     # generates data/wa_libraries.json
scripts/build_ny_data.py     # generates data/ny_libraries.json
scripts/build_california.py  # builds california.html
scripts/build_washington.py  # builds washington.html
scripts/build_newyork.py     # builds newyork.html
index.html                   # home page
california.html              # California map
washington.html              # Washington map
newyork.html                 # New York map
```

## Rebuilding

Run from the repo root:

```bash
# California
python3 scripts/build_data.py
python3 scripts/build_california.py

# Washington
python3 scripts/build_wa_data.py
python3 scripts/build_washington.py

# New York
python3 scripts/build_ny_data.py
python3 scripts/build_newyork.py
```

## Data notes & caveats

- **California**: System list from the California State Library's CLSA member jurisdictions (2023–24) — ~182 systems across 57 of 58 counties. Notable: Glendale (no Libby).
- **Washington**: 57 library systems across 25 counties. 51 share the WDLC catalog; 6 have independent collections. Reciprocal borrowing agreements vary by system.
- **New York**: 23 public library systems covering all 62 counties. Three consolidated (NYC), four federated (county-led), sixteen cooperative (member-library associations).
- Each pin is a library **system** (one card per system), not an individual branch.
- Libby availability and eligibility are **best‑effort** from official library and consortium sites — confirm with your library before relying on it.
- Coordinates are city/branch‑level placements (good for a state map, not turn‑by‑turn). Rail lines are schematic corridors between real stations.
