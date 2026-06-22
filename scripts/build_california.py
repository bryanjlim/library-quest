#!/usr/bin/env python3
import json
import os

records = json.load(open("data/ca_libraries.json"))
library_urls = json.load(open("data/ca_library_urls.json")) if os.path.exists("data/ca_library_urls.json") else {}
for r in records:
    r["url"] = library_urls.get(r["name"], "")
if library_urls:
    missing = sorted({r["name"] for r in records} - set(library_urls))
    assert not missing, "missing URLs: " + ", ".join(missing[:5])
records.sort(key=lambda r: (r["region"], r["name"]))
data_json = json.dumps(records, separators=(",",":"))

RAIL = [{'name': 'Amtrak Pacific Surfliner', 'op': 'Amtrak', 'color': '#08306b', 'dash': True, 'coords': [[35.2906, -120.6625], [35.1216, -120.6213], [34.953, -120.4357], [34.4146, -119.6936], [34.3989, -119.5185], [34.2805, -119.292], [34.2156, -119.178], [34.2653, -118.728], [34.2528, -118.5996], [34.1899, -118.449], [34.1969, -118.3553], [34.1466, -118.2554], [34.0561, -118.2365], [33.8704, -117.9242], [33.8071, -117.8887], [33.7497, -117.8606], [33.6499, -117.7316], [33.5008, -117.6628], [33.427, -117.612], [33.1959, -117.3795], [32.9912, -117.2713], [32.7551, -117.1996], [32.717, -117.1696]]}, {'name': 'Amtrak San Joaquins (Oakland)', 'op': 'Amtrak', 'color': '#08306b', 'dash': True, 'coords': [[35.3733, -119.0187], [35.594, -119.341], [36.098, -119.56], [36.3275, -119.6457], [36.7378, -119.7871], [36.9613, -120.0607], [37.3022, -120.483], [37.526, -120.797], [37.6391, -120.9969], [37.9577, -121.2908], [38.019, -122.1341], [37.9358, -122.3477], [37.8703, -122.299], [37.8406, -122.289], [37.7949, -122.2766]]}, {'name': 'Amtrak San Joaquins (Sacramento)', 'op': 'Amtrak', 'color': '#08306b', 'dash': True, 'coords': [[37.9577, -121.2908], [38.1302, -121.2724], [38.5816, -121.4944]]}, {'name': 'Amtrak Capitol Corridor', 'op': 'Amtrak', 'color': '#08306b', 'dash': True, 'coords': [[38.8966, -121.0769], [38.7521, -121.288], [38.5816, -121.4944], [38.5449, -121.7405], [38.2469, -122.0177], [38.019, -122.1341], [37.9358, -122.3477], [37.8703, -122.299], [37.8406, -122.289], [37.7949, -122.2766], [37.7541, -122.1969], [37.6699, -122.087], [37.5575, -121.9766], [37.353, -121.936], [37.3297, -121.9024]]}, {'name': 'Amtrak Coast Starlight', 'op': 'Amtrak', 'color': '#08306b', 'dash': True, 'coords': [[41.208, -122.272], [40.5865, -122.3917], [39.728, -121.838], [38.5816, -121.4944], [38.5449, -121.7405], [38.019, -122.1341], [37.8406, -122.289], [37.7949, -122.2766], [37.3297, -121.9024], [36.6745, -121.6552], [35.6269, -120.691], [35.2906, -120.6625], [34.4146, -119.6936], [34.2156, -119.178], [34.2653, -118.728], [34.1969, -118.3553], [34.1466, -118.2554], [34.0561, -118.2365]]}, {'name': 'BART', 'op': 'BART', 'color': '#0072bc', 'dash': False, 'coords': [[37.5997, -122.3866], [37.6376, -122.4163], [37.6642, -122.4439], [37.6847, -122.4663], [37.7063, -122.469], [37.7215, -122.4475], [37.7522, -122.4181], [37.7796, -122.4137], [37.7929, -122.3968], [37.8048, -122.2952], [37.803, -122.2716], [37.8076, -122.2687], [37.8294, -122.267], [37.853, -122.27], [37.87, -122.268], [37.874, -122.2835], [37.9028, -122.299], [37.925, -122.3168], [37.9369, -122.353]]}, {'name': 'BART (SFO)', 'op': 'BART', 'color': '#0072bc', 'dash': False, 'coords': [[37.6376, -122.4163], [37.616, -122.3925]]}, {'name': 'BART (Antioch)', 'op': 'BART', 'color': '#0072bc', 'dash': False, 'coords': [[37.8294, -122.267], [37.8443, -122.2515], [37.8782, -122.1838], [37.8934, -122.1245], [37.9057, -122.0676], [37.9281, -122.056], [37.9737, -122.0294], [38.0032, -122.0246], [38.0189, -121.945], [37.9963, -121.7838]]}, {'name': 'BART (Berryessa)', 'op': 'BART', 'color': '#0072bc', 'dash': False, 'coords': [[37.803, -122.2716], [37.7975, -122.2655], [37.7748, -122.2241], [37.7541, -122.1969], [37.7219, -122.1608], [37.697, -122.1267], [37.6699, -122.087], [37.6345, -122.0574], [37.591, -122.0173], [37.5575, -121.9766], [37.5022, -121.9395], [37.4103, -121.8916], [37.3686, -121.8746]]}, {'name': 'BART (Dublin/Pleasanton)', 'op': 'BART', 'color': '#0072bc', 'dash': False, 'coords': [[37.697, -122.1267], [37.6907, -122.0756], [37.6997, -121.9282], [37.7016, -121.9]]}, {'name': 'Caltrain', 'op': 'Caltrain', 'color': '#d9261c', 'dash': False, 'coords': [[37.7766, -122.3947], [37.6557, -122.4053], [37.5841, -122.3661], [37.538, -122.302], [37.4852, -122.2364], [37.4546, -122.1825], [37.4419, -122.143], [37.3861, -122.0839], [37.3688, -122.0363], [37.353, -121.936], [37.3297, -121.9024], [37.3115, -121.8853], [37.2997, -121.8003], [37.1294, -121.65], [37.0058, -121.5663]]}, {'name': 'ACE (Altamont Corridor)', 'op': 'ACE', 'color': '#0a9648', 'dash': False, 'coords': [[37.3297, -121.9024], [37.5636, -121.987], [37.6597, -121.876], [37.6819, -121.768], [37.7397, -121.4252], [37.9577, -121.2908]]}, {'name': 'SMART', 'op': 'SMART', 'color': '#6a3d9a', 'dash': False, 'coords': [[37.945, -122.509], [37.9735, -122.5311], [38.1074, -122.5697], [38.2324, -122.6367], [38.3276, -122.7094], [38.4405, -122.7141], [38.5471, -122.8164], [38.6102, -122.8694], [38.8055, -123.0173]]}, {'name': 'Metrolink San Bernardino Line', 'op': 'Metrolink', 'color': '#f47b20', 'dash': False, 'coords': [[34.0561, -118.2365], [34.0667, -118.169], [34.0686, -118.027], [34.0846, -117.9637], [34.09, -117.8903], [34.0726, -117.75], [34.0967, -117.7197], [34.075, -117.69], [34.0975, -117.6484], [34.1063, -117.5931], [34.0922, -117.435], [34.1064, -117.37], [34.1083, -117.2898]]}, {'name': 'Metrolink Antelope Valley Line', 'op': 'Metrolink', 'color': '#f47b20', 'dash': False, 'coords': [[34.0561, -118.2365], [34.1466, -118.2554], [34.1808, -118.309], [34.2206, -118.369], [34.309, -118.448], [34.384, -118.536], [34.492, -118.196], [34.5794, -118.1165], [34.6968, -118.137]]}, {'name': 'Metrolink Riverside Line', 'op': 'Metrolink', 'color': '#f47b20', 'dash': False, 'coords': [[34.0561, -118.2365], [34.005, -118.11], [34.019, -117.954], [33.993, -117.487], [33.9806, -117.3755]]}, {'name': 'COASTER', 'op': 'COASTER', 'color': '#0b7fab', 'dash': False, 'coords': [[33.1959, -117.3795], [33.1581, -117.3506], [33.0369, -117.292], [32.9912, -117.2713], [32.9, -117.23], [32.7551, -117.1996], [32.717, -117.1696]]}, {'name': 'SPRINTER', 'op': 'SPRINTER', 'color': '#b15928', 'dash': False, 'coords': [[33.1959, -117.3795], [33.195, -117.236], [33.13, -117.17], [33.1192, -117.0864]]}, {'name': 'LA Metro A Line', 'op': 'LA Metro', 'color': '#16a085', 'dash': False, 'coords': [[33.7683, -118.1956], [33.805, -118.189], [33.8975, -118.22], [33.943, -118.243], [34.027, -118.27], [34.0489, -118.2587], [34.0561, -118.2365], [34.064, -118.235], [34.111, -118.192], [34.1161, -118.1503], [34.1478, -118.1445], [34.152, -118.113], [34.148, -118.082], [34.133, -118.035], [34.134, -118.019], [34.137, -117.956], [34.107, -117.9351], [34.1336, -117.9076], [34.138, -117.889]]}, {'name': 'LA Metro E Line', 'op': 'LA Metro', 'color': '#16a085', 'dash': False, 'coords': [[34.0157, -118.4955], [34.028, -118.389], [34.024, -118.335], [34.022, -118.278], [34.0489, -118.2587], [34.05, -118.239], [34.033, -118.154]]}, {'name': 'LA Metro C Line', 'op': 'LA Metro', 'color': '#16a085', 'dash': False, 'coords': [[33.894, -118.376], [33.914, -118.388], [33.93, -118.377], [33.928, -118.238], [33.914, -118.105]]}, {'name': 'LA Metro K Line', 'op': 'LA Metro', 'color': '#16a085', 'dash': False, 'coords': [[34.024, -118.335], [33.989, -118.352], [33.9617, -118.3531], [33.946, -118.377]]}, {'name': 'LA Metro B/D subway', 'op': 'LA Metro', 'color': '#16a085', 'dash': False, 'coords': [[34.0561, -118.2365], [34.0489, -118.2587], [34.0625, -118.291], [34.1016, -118.326], [34.139, -118.364], [34.1689, -118.377]]}]
rail_json = json.dumps(RAIL, separators=(",",":"))
total_libby = sum(1 for r in records if r["libby"])

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>California Library Quest</title>
<script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
<script src="https://cdn.jsdelivr.net/npm/topojson-client@3"></script>
<style>
  :root{--bg:#0b0e14;--panel:#121620;--line:#232a38;--txt:#e8ebf0;--muted:#94a0b3;--gold:#f2c14e;--accent:#5aa2ff;}
  *{box-sizing:border-box}
  html,body{margin:0;height:100%;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--txt);overflow:hidden}
  #app{display:flex;height:100vh}
  #side{width:360px;min-width:300px;background:linear-gradient(180deg,#141926,#0f131c);border-right:1px solid var(--line);display:flex;flex-direction:column;z-index:5}
  header{padding:16px 16px 12px;border-bottom:1px solid var(--line);position:relative}
  h1{font-size:16px;margin:0 0 2px;letter-spacing:.2px}
  .sub{font-size:11.5px;color:var(--muted)}
  .homebtn{display:inline-flex;margin:0 0 10px;color:var(--muted);font-size:12px;font-weight:700;text-decoration:none}
  .homebtn:hover{color:var(--txt)}
  .infobtn{position:absolute;top:14px;right:14px;display:flex;align-items:center;gap:5px;background:#0b0e14;border:1px solid var(--line);color:var(--muted);font-size:11px;padding:4px 9px;border-radius:7px;cursor:pointer}
  .infobtn:hover{color:var(--txt);border-color:var(--accent)}
  .menubtn{display:none;position:absolute;top:14px;right:14px;align-items:center;justify-content:center;width:30px;height:27px;background:#0b0e14;border:1px solid var(--line);color:var(--muted);font-size:18px;padding:0;border-radius:7px;cursor:pointer;line-height:1}
  .menubtn:hover{color:var(--txt);border-color:var(--accent)}
  .prog{display:flex;align-items:center;gap:12px;margin-top:12px}
  .ring-wrap{position:relative;width:54px;height:54px;flex:none}
  .ring-wrap svg{transform:rotate(-90deg)}
  .ring-wrap .pct{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:var(--gold)}
  .prog .lbl{font-size:12px;color:var(--muted)}
  .prog .lbl b{color:var(--txt);font-size:15px;display:block}
  .controls{padding:10px 14px;border-bottom:1px solid var(--line);display:flex;flex-direction:column;gap:8px}
  input[type=text],select{width:100%;padding:8px 10px;border-radius:8px;border:1px solid var(--line);background:#0b0e14;color:var(--txt);font-size:13px}
  .row{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--muted)}
  .btns{display:flex;gap:8px}
  .btns button{flex:1;padding:7px;border-radius:8px;border:1px solid var(--line);background:#0b0e14;color:var(--muted);font-size:12px;cursor:pointer}
  .btns button:hover{color:var(--txt);border-color:var(--accent)}
  #list{overflow-y:auto;flex:1;padding:6px 8px}
  .grp{margin:8px 4px 2px;padding:4px 5px;border-radius:7px;font-size:11.5px;line-height:1.25;color:var(--muted);display:flex;align-items:flex-start;gap:6px;cursor:pointer;user-select:none}
  .grp:hover{background:#1b2333;color:var(--txt)}
  .grp .chev{width:10px;text-align:center;color:var(--txt)}
  .grp .cnt{margin-left:auto;color:var(--muted)}
  .gdot{width:10px;height:10px;border-radius:50%;flex:none}
  .item{display:flex;align-items:flex-start;gap:9px;padding:6px 8px;border-radius:8px;cursor:pointer}
  .item:hover{background:#1b2333}
  .item input{margin-top:3px;flex:none;width:15px;height:15px;accent-color:var(--gold)}
  .item .nm{font-size:12.5px;line-height:1.25}
  .item .loc{font-size:11px;color:var(--muted)}
  .item .meta{flex:1;min-width:0}
  .item .gm{margin-left:auto;color:var(--accent);text-decoration:none;font-size:15px;padding:0 2px;flex:none}
  .item .gm:hover{color:#9cc4ff}
  .item.done .nm{color:var(--gold)}
  #map{flex:1;position:relative;background:radial-gradient(1200px 800px at 60% 30%, #131a28 0%, #0b0e14 70%)}
  svg.stage{width:100%;height:100%;display:block;cursor:grab}
  svg.stage:active{cursor:grabbing}
  .county{cursor:default}
  .rail{fill:none;stroke-linecap:round;stroke-linejoin:round}
  .city-label{fill:#94a0b3;font-size:11px;font-weight:600;pointer-events:none;paint-order:stroke;stroke:#0b0e14;stroke-width:3px;stroke-linejoin:round;text-anchor:middle;letter-spacing:.02em}
  .node{cursor:pointer}
  .node .dot{transition:fill .15s}
  .chk{fill:#1a1a1a;font-weight:900;text-anchor:middle;dominant-baseline:central;paint-order:stroke;stroke:#fff;stroke-width:.6px}
  .tooltip{position:fixed;pointer-events:none;background:rgba(10,13,20,.95);border:1px solid var(--line);border-radius:8px;padding:7px 10px;font-size:12px;color:var(--txt);max-width:240px;z-index:50;opacity:0;transition:opacity .12s;box-shadow:0 6px 20px rgba(0,0,0,.5)}
  .tooltip b{display:block;font-size:12.5px;margin-bottom:2px}
  .tooltip .meta{color:var(--muted);font-size:11px}
  .popup{position:fixed;display:none;width:min(280px,calc(100vw - 24px));background:rgba(13,17,26,.97);border:1px solid var(--line);border-radius:10px;padding:11px 12px;z-index:70;box-shadow:0 10px 30px rgba(0,0,0,.55);font-size:12px}
  .popup.show{display:block}
  .popup .x{position:absolute;top:6px;right:8px;background:none;border:none;color:var(--muted);font-size:18px;line-height:1;cursor:pointer}
  .popup .h{font-weight:700;font-size:13.5px;padding-right:18px;margin-bottom:3px}
  .popup .m{color:var(--muted);font-size:11px;line-height:1.35}
  .popup .note{margin-top:8px;padding:7px 8px;border-radius:8px;background:#1b2333;color:#dfe6f2;line-height:1.35}
  .popup .warn{background:#2b1d16;color:#ffd5bd}
  .popup .actions{display:flex;align-items:center;gap:9px;margin-top:10px;flex-wrap:wrap}
  .popup .collect{background:var(--gold);border:none;color:#1a1a1a;border-radius:7px;padding:7px 10px;font-size:12px;font-weight:700;cursor:pointer}
  .popup a{color:var(--accent);font-weight:700;text-decoration:none}
  /* on-map key */
  .legend{position:absolute;right:12px;bottom:12px;background:rgba(13,17,26,.92);border:1px solid var(--line);border-radius:10px;padding:10px 12px;font-size:11px;max-width:300px;box-shadow:0 6px 20px rgba(0,0,0,.45)}
  .legend .ttl{font-size:10px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin-bottom:5px}
  .legend .li{display:flex;align-items:flex-start;gap:8px;margin:3px 0}
  .legend details{margin-top:6px}
  .legend summary{cursor:pointer;color:var(--muted);font-size:10px;text-transform:uppercase;letter-spacing:.06em}
  .swatch{width:11px;height:11px;border-radius:3px;flex:none;display:inline-block}
  .rsw{display:inline-block;width:18px;height:0;border-top:3px solid #000;flex:none}
  .zbtns{position:absolute;left:12px;top:12px;display:flex;flex-direction:column;gap:6px}
  .zbtns button{width:32px;height:32px;border-radius:8px;border:1px solid var(--line);background:rgba(13,17,26,.92);color:var(--txt);font-size:18px;cursor:pointer;line-height:1}
  .zbtns button:hover{border-color:var(--accent)}
  /* modal */
  .modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,.6);display:none;align-items:center;justify-content:center;z-index:1000;padding:20px}
  .modal-overlay.show{display:flex}
  .modal{background:var(--panel);border:1px solid var(--line);border-radius:14px;max-width:540px;width:100%;max-height:88vh;overflow-y:auto;padding:22px 24px;position:relative;box-shadow:0 10px 40px rgba(0,0,0,.5)}
  .modal h2{margin:0 0 12px;font-size:19px}
  .modal p{font-size:13.5px;line-height:1.55;color:#dde2ea;margin:0 0 12px}
  .modal p.muted{color:var(--muted);font-size:12.5px}
  .modal-x{position:absolute;top:10px;right:14px;background:none;border:none;color:var(--muted);font-size:22px;cursor:pointer}
  .modal-ok{background:var(--gold);color:#1a1a1a;border:none;font-weight:600;font-size:13px;padding:8px 16px;border-radius:8px;cursor:pointer}
  .modal-cancel{background:transparent;color:var(--muted);border:1px solid var(--line);font-weight:600;font-size:13px;padding:7px 15px;border-radius:8px;cursor:pointer}
  .modal-cancel:hover{color:var(--txt);border-color:var(--accent)}
  .modal-actions{display:flex;gap:10px;justify-content:flex-end;margin-top:14px;flex-wrap:wrap}
  .badge{position:absolute;left:12px;bottom:12px;font-size:10px;color:var(--muted);background:rgba(13,17,26,.8);border:1px solid var(--line);border-radius:6px;padding:3px 7px}
  .loading{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:var(--muted);font-size:13px;pointer-events:none;z-index:1}
  .loading .spinner{width:22px;height:22px;border:2.5px solid var(--line);border-top-color:var(--gold);border-radius:50%;animation:spin 1s linear infinite;margin-right:10px;flex:none}
  @keyframes spin{to{transform:rotate(360deg)}}
  @media (max-width:700px){
    html,body{height:100%;overflow:hidden}
    #app{height:100dvh;display:block;position:relative}
    #map{position:absolute;inset:0;width:100%;height:100dvh;min-height:0}
    #side{position:absolute;top:10px;left:10px;right:10px;width:auto;min-width:0;height:auto;max-height:calc(100dvh - 20px);border:1px solid var(--line);border-radius:10px;background:rgba(18,22,32,.94);backdrop-filter:blur(10px);overflow:hidden}
    header{padding:12px}
    h1{font-size:15px;padding-right:128px}
    .sub,.prog{display:none}
    .homebtn{margin-bottom:8px}
    .infobtn{top:10px;right:78px}
    .menubtn{display:flex;top:10px;right:10px}
    .controls{padding:10px 12px}
    #side:not(.open) header{border-bottom:0}
    #side:not(.open) .controls,#side:not(.open) #list{display:none}
    #side.open #list{flex:none;display:block;max-height:42dvh;min-height:130px}
    .zbtns{top:96px}
    .legend{left:10px;right:10px;bottom:10px;max-width:none;max-height:28dvh;overflow:auto}
    .badge{display:none}
    .modal-overlay{padding:10px}
    .modal{max-height:92dvh;padding:18px}
  }
</style>
</head>
<body>
<div id="app">
  <div id="side">
    <header>
      <a class="homebtn" href="index.html">&larr; Library Quest</a>
      <h1>California Library Quest &#128218;</h1>
      <div class="sub">Find which cards add new Libby catalogs</div>
      <button class="infobtn" id="infobtn" aria-label="Info"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M12 2a10 10 0 100 20 10 10 0 000-20zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>Info</button>
      <button class="menubtn" id="menubtn" aria-label="Menu" aria-expanded="false">&#9776;</button>
      <div class="prog">
        <div class="ring-wrap">
          <svg width="54" height="54"><circle cx="27" cy="27" r="22" fill="none" stroke="#222b3a" stroke-width="6"/><circle id="ringfg" cx="27" cy="27" r="22" fill="none" stroke="url(#gg)" stroke-width="6" stroke-linecap="round" stroke-dasharray="138.2" stroke-dashoffset="138.2"/><defs><linearGradient id="gg"><stop offset="0" stop-color="#f2c14e"/><stop offset="1" stop-color="#ffd97a"/></linearGradient></defs></svg>
          <div class="pct" id="pct">0%</div>
        </div>
        <div class="lbl"><b id="pcount">0</b>of __TOTAL__ systems collected</div>
      </div>
    </header>
    <div class="controls">
      <input type="text" id="search" placeholder="Search by name, city, or county...">
      <select id="region"><option value="">All catalogs</option></select>
      <div class="btns"><button id="resetview">Reset view</button><button id="clearmine">Reset progress</button></div>
      <label class="row"><input type="checkbox" id="railtoggle" checked> Show rail lines</label>
      <label class="row"><input type="checkbox" id="uncoltoggle"> Show uncollected only</label>
    </div>
    <div id="list"></div>
  </div>
  <div id="map">
    <div id="loading" class="loading"><div class="spinner"></div>Loading California map…</div>
    <div class="zbtns"><button id="zin">+</button><button id="zout">&minus;</button></div>
    <div class="legend" id="legend"></div>
    <div class="badge">Pan &amp; scroll to zoom &middot; click a dot for details</div>
  </div>
</div>
<div class="tooltip" id="tip"></div>
<div class="popup" id="popup"></div>
<div id="about" class="modal-overlay">
  <div class="modal">
    <button class="modal-x" id="aboutclose">&times;</button>
    <h2>California Library Quest &#128218;</h2>
    <p>California residents can get library cards at <b>any public library system in the state</b>, not just their local branch. Each card adds that system's collection to the <b>Libby</b> app, opening up more ebooks, audiobooks, and waitlists. This map shows all <b>181</b> Libby systems.</p>
    <p><b>Dot color = catalog.</b> Libraries that share one Libby catalog share a color; independent libraries are grey.</p>
    <p>Libraries with the same shared-catalog color share one Libby catalog and one holds list, so a card at any one gives the same books and waits &mdash; only one in the group is worth holding.</p>
    <p>Independent libraries are grey: their own catalog and holds list, so each extra card means more books and shorter waits.</p>
    <p class="muted">Each pin is a library <b>system</b> (one card per system), not an individual branch. Click a dot for details, or use the list checkboxes to collect; progress saves in your browser.</p>
    <button class="modal-ok" id="aboutok">Got it</button>
  </div>
</div>
<div id="confirmclear" class="modal-overlay">
  <div class="modal" style="max-width:440px">
    <button class="modal-x" id="confirmclearclose">&times;</button>
    <h2>Clear all collected cards?</h2>
    <p>This resets your progress to zero. This can't be undone.</p>
    <div class="modal-actions">
      <button class="modal-cancel" id="confirmclearno">Cancel</button>
      <button class="modal-ok" id="confirmclearyes">Clear progress</button>
    </div>
  </div>
</div>
<script>
const DATA=__DATA__, RAIL=__RAIL__;
const CITIES=[
  {n:"Eureka",lat:40.8021,lon:-124.1637},{n:"Redding",lat:40.5865,lon:-122.3917},
  {n:"Sacramento",lat:38.5816,lon:-121.4944},{n:"Stockton",lat:37.9577,lon:-121.2908},
  {n:"San Francisco",lat:37.7790,lon:-122.4156},{n:"Oakland",lat:37.8044,lon:-122.2712},
  {n:"San Jose",lat:37.3382,lon:-121.8863},{n:"Fresno",lat:36.7378,lon:-119.7871},
  {n:"Bakersfield",lat:35.3733,lon:-119.0187},{n:"Santa Barbara",lat:34.4208,lon:-119.6982},
  {n:"Los Angeles",lat:34.0537,lon:-118.2428},{n:"Long Beach",lat:33.7701,lon:-118.1937},
  {n:"Anaheim",lat:33.8366,lon:-117.9143},{n:"San Bernardino",lat:34.1083,lon:-117.2898},
  {n:"Riverside",lat:33.9533,lon:-117.3962},{n:"San Diego",lat:32.7157,lon:-117.1611}
];
const TOTAL=DATA.filter(d=>d.libby).length;
const KEY="library_quest_ca_v1";
const US="https://cdn.jsdelivr.net/npm/us-atlas@3/counties-10m.json";

function loadSet(){ try{const s=JSON.parse(localStorage.getItem(KEY)); if(Array.isArray(s)) return new Set(s);}catch(e){} return new Set(); }
function saveSet(){ try{localStorage.setItem(KEY,JSON.stringify([...collected]));}catch(e){} }
let collected=loadSet();

const isShared=d=>d.libby&&!!d.shared;
const CAT_ORDER=["NCDL shared","Black Gold shared","Peninsula shared","SJVLS shared","Serra shared","Independent","No Libby"];
const CAT_COLOR={"NCDL shared":"#1f77b4","Black Gold shared":"#ff7f0e","Peninsula shared":"#e377c2","SJVLS shared":"#9467bd","Serra shared":"#2ca02c","Independent":"#c2cbd9","No Libby":"#2b2b2b"};
const CAT_LABEL={"NCDL shared":"NCDL","Black Gold shared":"Black Gold","Peninsula shared":"Peninsula","SJVLS shared":"SJVLS","Serra shared":"Serra","Independent":"Independent","No Libby":"No Libby"};
const CAT_KEY_LABEL={"NCDL shared":"Northern California Digital Library","Black Gold shared":"Black Gold Cooperative Library System","Peninsula shared":"Peninsula Library System","SJVLS shared":"San Joaquin Valley Library System","Serra shared":"Serra Cooperative Library System","Independent":"Independent catalog","No Libby":"No Libby"};
const catKey=d=>!d.libby?"No Libby":(d.shared||"Independent");
const catColor=d=>CAT_COLOR[catKey(d)];
const gmapUrl=d=>"https://www.google.com/maps/search/?api=1&query="+encodeURIComponent(d.name+", "+d.city+", CA");
const catalogName=s=>s.replace(/ shared$/,'');
const libraryUrl=d=>d.url||"";

const mapDiv=document.getElementById('map');
const svg=d3.select('#map').append('svg').attr('class','stage')
  .attr('viewBox','0 0 975 610').attr('preserveAspectRatio','xMidYMid meet');
const defs=svg.append('defs');

const g=svg.append('g');
const gCounty=g.append('g'), gState=g.append('g'), gRail=g.append('g'), gLabel=g.append('g'), gNode=g.append('g');
const tip=document.getElementById('tip');
const popup=document.getElementById('popup');

let projection, path, k=1;
let lastTouchPopup=0;
const isMobile=()=>matchMedia('(max-width:700px)').matches;

const zoom=d3.zoom().scaleExtent([1,14]).on('zoom',ev=>{ g.attr('transform',ev.transform); k=ev.transform.k; rescale(); });

d3.json(US).then(us=>{
  const states=topojson.feature(us,us.objects.states).features;
  const ca=states.find(d=>d.id==="06");
  const counties=topojson.feature(us,us.objects.counties).features.filter(d=>String(d.id).slice(0,2)==="06");

  projection=d3.geoMercator().fitExtent([[20,20],[955,590]], ca);
  path=d3.geoPath(projection);

  gCounty.selectAll('path').data(counties).join('path').attr('class','county').attr('d',path)
    .attr('fill','#19202e').attr('fill-opacity',0.85)
    .attr('stroke','#2c3647').attr('stroke-width',0.4);

  gState.append('path').datum(ca).attr('d',path).attr('fill','none').attr('stroke','#62748c').attr('stroke-width',1.1);

  // rail (project lon/lat into the same albersUsa space)
  const line=d3.line();
  gRail.selectAll('path').data(RAIL).join('path').attr('class','rail')
    .attr('d',d=>line(d.coords.map(c=>projection([c[1],c[0]]))))
    .attr('stroke',d=>d.color).attr('stroke-width',1.5)
    .attr('stroke-dasharray',d=>d.dash?'4,3':null).attr('opacity',.85)
    .on('mousemove',(e,d)=>showTip(e,`<b>${d.name}</b>`)).on('mouseout',hideTip);

  // city labels for geographic context (fade out as you zoom in)
  const cityPts=CITIES.map(c=>{const p=projection([c.lon,c.lat]); return {n:c.n,x:p?p[0]:null,y:p?p[1]:null};}).filter(c=>c.x!=null);
  gLabel.selectAll('text').data(cityPts).join('text').attr('class','city-label')
    .attr('x',d=>d.x).attr('y',d=>d.y).attr('dy','-7').text(d=>d.n);

  // nodes
  DATA.forEach(d=>{const p=projection([d.lon,d.lat]); d._x=p?p[0]:null; d._y=p?p[1]:null;});
  const node=gNode.selectAll('g.node').data(DATA.filter(d=>d._x!=null)).join('g')
    .attr('class','node').attr('transform',d=>`translate(${d._x},${d._y})`)
    .on('pointerdown',(e,d)=>{ if(e.pointerType!=='mouse') e.stopPropagation(); })
    .on('pointerenter',function(e,d){ if(e.pointerType==='mouse') d3.select(this).raise().select('.dot').attr('r',7.5/k); })
    .on('pointermove',(e,d)=>{ if(e.pointerType==='mouse') showTip(e,tipHTML(d)); })
    .on('pointerleave',function(e,d){ d3.select(this).select('.dot').attr('r',dotR(d)); hideTip(); })
    .on('pointerup',(e,d)=>{
      if(e.pointerType==='mouse') return;
      e.stopPropagation(); e.preventDefault(); lastTouchPopup=Date.now(); hideTip(); showPopup(e.clientX,e.clientY,d);
    })
    .on('click',(e,d)=>{
      e.stopPropagation();
      if(Date.now()-lastTouchPopup<500){ e.preventDefault(); return; }
      hideTip(); showPopup(e.clientX,e.clientY,d);
    });
  node.append('circle').attr('class','halo').attr('fill','#f2c14e').attr('fill-opacity',0.28).attr('stroke','none').attr('display','none');
  node.append('circle').attr('class','dot').attr('stroke','#fff');
  node.append('text').attr('class','chk').attr('display','none').text('✓');

  paint();
  initT=d3.zoomIdentity;
  svg.call(zoom);
  svg.on('click',()=>{ if(Date.now()-lastTouchPopup>=500) hidePopup(); });
  const ld=document.getElementById('loading'); if(ld) ld.remove();
}).catch(err=>{ const ld=document.getElementById('loading'); if(ld) ld.remove(); mapDiv.insertAdjacentHTML('beforeend','<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#94a0b3;padding:30px;text-align:center">Could not load the base map (needs internet for the California geometry).</div>'); console.error(err); });

let initT=d3.zoomIdentity;
function dotR(d){
  const mobile=isMobile();
  const base=collected.has(d.name)?(mobile?10:6):(mobile?8:5);
  const max=collected.has(d.name)?22:18;
  return mobile?Math.min(base/Math.sqrt(k),max/k):base/k;
}
function paint(){
  gNode.selectAll('g.node').each(function(d){
    const sel=d3.select(this), on=collected.has(d.name);
    sel.select('.dot')
      .attr('r',dotR(d))
      .attr('fill', on? '#f2c14e' : catColor(d))
      .attr('stroke', on? '#a6791f' : (!d.libby? '#cfd6e0' : '#ffffff'))
      .attr('stroke-dasharray', d.libby? null : '2,2');
    sel.select('.halo').attr('display', on? null : 'none');
    sel.select('.chk').attr('display', on? null : 'none');
  });
  rescale();
}
function rescale(){
  gNode.selectAll('.dot').attr('r',d=>dotR(d)).attr('stroke-width',1/k);
  gNode.selectAll('.halo').attr('r',d=>dotR(d)+3.5/k);
  gNode.selectAll('.chk').style('font-size',(11/k)+'px').attr('stroke-width',(0.6/k)+'px');
  gRail.selectAll('path').attr('stroke-width',1.5/k);
  gCounty.selectAll('path').attr('stroke-width',0.4/k);
  gState.select('path').attr('stroke-width',1.1/k);
  gLabel.selectAll('text').style('font-size',(11/k)+'px').attr('stroke-width',(3/k)+'px')
    .attr('opacity',Math.max(0,1-(k-1)/2));
}

function tipHTML(d){
  const kind = !d.libby? 'No Libby' : (isShared(d)? 'Shared catalog: '+catalogName(d.shared) : 'Own Libby collection');
  return `<b>${d.name}</b><span class="meta">${d.city}, ${d.county} County &middot; ${d.region}<br>${kind}${collected.has(d.name)?' &middot; ✓ collected':''}</span>`;
}
function esc(s){ return String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[c])); }
function noteHTML(d){
  if(!d.libby) return '';
  if(d.shared) return `<div class="note">Part of the <b>${esc(catalogName(d.shared))}</b> Libby group. One card gives you the same catalog and waitlists as the rest of this group.</div>`;
  return '<div class="note">Independent Libby collection with its own titles and waitlists.</div>';
}
function showPopup(x,y,d){
  const done=collected.has(d.name);
  popup.innerHTML=`<button class="x" aria-label="Close">&times;</button>
    <div class="h">${esc(d.name)}</div>
    <div class="m">${esc(d.city)}, ${esc(d.county)} County &middot; ${esc(d.region)}<br>System: ${esc(d.system)}</div>
    ${noteHTML(d)}
    ${d.note?`<div class="note warn">${esc(d.note)}</div>`:''}
    <div class="actions">
      ${d.libby?`<button class="collect">${done?'✓ Collected — undo':'Mark as collected'}</button>`:''}
      ${libraryUrl(d)?`<a href="${esc(libraryUrl(d))}" target="_blank" rel="noopener">Library card / website &#8599;</a>`:''}
      <a href="${gmapUrl(d)}" target="_blank" rel="noopener">Open in Google Maps &#8599;</a>
    </div>`;
  popup.classList.add('show');
  const pad=12, rect=popup.getBoundingClientRect();
  popup.style.left=Math.max(pad,Math.min(x+pad,innerWidth-rect.width-pad))+'px';
  popup.style.top=Math.max(pad,Math.min(y+pad,innerHeight-rect.height-pad))+'px';
  popup.querySelector('.x').onclick=hidePopup;
  const b=popup.querySelector('.collect');
  if(b) b.onclick=e=>{ e.stopPropagation(); toggle(d.name); showPopup(x,y,d); };
}
function hidePopup(){ popup.classList.remove('show'); }
popup.addEventListener('click',e=>e.stopPropagation());
function showTip(e,html){ tip.innerHTML=html; tip.style.opacity=1; moveTip(e); }
function moveTip(e){ const pad=14; let x=e.clientX+pad,y=e.clientY+pad; if(x>innerWidth-250)x=e.clientX-250; tip.style.left=x+'px'; tip.style.top=y+'px'; }
document.addEventListener('mousemove',e=>{ if(tip.style.opacity==='1') moveTip(e); });
document.addEventListener('click',e=>{ if(!popup.contains(e.target)) hidePopup(); });
function hideTip(){ tip.style.opacity=0; }

function toggle(name){
  const r=DATA.find(d=>d.name===name); if(!r.libby) return;
  const on=!collected.has(name);
  const group=(r.libby&&r.shared)? DATA.filter(d=>d.shared===r.shared) : [r];
  group.forEach(gd=>{ if(on) collected.add(gd.name); else collected.delete(gd.name); });
  saveSet(); paint(); refresh();
}

// region dropdown
const cats=CAT_ORDER.filter(c=>DATA.some(d=>catKey(d)===c));
const collapsedCats=new Set();
const rsel=document.getElementById('region');
cats.forEach(c=>{const o=document.createElement('option');o.value=c;o.textContent=CAT_KEY_LABEL[c]+' ('+DATA.filter(d=>catKey(d)===c).length+')';rsel.appendChild(o);});

function passes(d){
  const q=document.getElementById('search').value.toLowerCase().trim();
  const rf=document.getElementById('region').value;
  const uf=document.getElementById('uncoltoggle').checked;
  if(rf && catKey(d)!==rf) return false;
  if(uf && d.libby && collected.has(d.name)) return false;
  if(q && !(d.name.toLowerCase().includes(q)||d.city.toLowerCase().includes(q)||d.county.toLowerCase().includes(q))) return false;
  return true;
}
function refresh(){
  const n=collected.size, pct=Math.round(n/TOTAL*100);
  document.getElementById('pcount').textContent=n;
  document.getElementById('pct').textContent=pct+'%';
  const C=2*Math.PI*22; document.getElementById('ringfg').setAttribute('stroke-dashoffset', C*(1-n/TOTAL));
  // dim non-matching nodes
  gNode.selectAll('g.node').attr('opacity',d=>passes(d)?1:0.12).style('pointer-events',d=>passes(d)?null:'none');
  renderList();
}
function renderList(){
  const list=document.getElementById('list');
  const prevTop=list.scrollTop, prevH=list.scrollHeight;
  list.innerHTML=''; let cur=null;
  const rows=DATA.filter(passes).slice().sort((a,b)=>(CAT_ORDER.indexOf(catKey(a))-CAT_ORDER.indexOf(catKey(b)))||a.name.localeCompare(b.name));
  rows.forEach(d=>{
    const ckey=catKey(d);
    if(ckey!==cur){cur=ckey;const h=document.createElement('div');h.className='grp';
      const collapsed=collapsedCats.has(ckey), n=rows.filter(r=>catKey(r)===ckey).length;
      h.tabIndex=0; h.setAttribute('role','button'); h.setAttribute('aria-expanded', String(!collapsed));
      h.innerHTML=`<span class="chev">${collapsed?'▸':'▾'}</span><span class="gdot" style="background:${CAT_COLOR[ckey]};border:1px solid rgba(255,255,255,.25)"></span>${CAT_KEY_LABEL[ckey]}<span class="cnt">${n}</span>`;
      h.onclick=()=>{ collapsed ? collapsedCats.delete(ckey) : collapsedCats.add(ckey); renderList(); };
      h.onkeydown=e=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); h.click(); } };
      list.appendChild(h);}
    if(collapsedCats.has(ckey)) return;
    const on=collected.has(d.name);
    const it=document.createElement('div'); it.className='item'+(on?' done':'');
    const tag=!d.libby?' &mdash; no Libby':(isShared(d)?' &middot; shared':' &middot; own');
    const cb=d.libby?`<input type="checkbox" ${on?'checked':''}>`:`<span style="width:15px;flex:none"></span>`;
    it.innerHTML=`${cb}<div class="meta"><div class="nm">${d.name}</div><div class="loc">${d.city}, ${d.county} Co.${tag}</div></div><a class="gm" href="${gmapUrl(d)}" target="_blank" rel="noopener" title="Open in Google Maps">&#8599;</a>`;
    const ck=it.querySelector('input'); if(ck) ck.addEventListener('click',e=>{e.stopPropagation();toggle(d.name);});
    const gm=it.querySelector('a.gm'); if(gm) gm.addEventListener('click',e=>e.stopPropagation());
    it.addEventListener('click',()=>flyTo(d));
    list.appendChild(it);
  });
  // Keep scroll stable when the list hasn't shrunk (e.g. toggling a checkbox);
  // if a search shrank the list below the previous scroll position, the browser
  // clamps scrollTop to the new max, which lands us at the bottom — so only
  // restore when the new content is at least as tall as before.
  if(list.scrollHeight>=prevH) list.scrollTop=prevTop;
  else list.scrollTop=0;
}
function flyTo(d){
  if(d._x==null) return;
  const t=d3.zoomIdentity.translate(975/2,610/2).scale(8).translate(-d._x,-d._y);
  svg.transition().duration(800).call(zoom.transform,t);
  if(isMobile()) setSideOpen(false);
}

document.getElementById('search').addEventListener('input',refresh);
document.getElementById('region').addEventListener('change',refresh);
document.getElementById('uncoltoggle').addEventListener('change',refresh);
document.getElementById('resetview').onclick=()=>svg.transition().duration(700).call(zoom.transform,initT);
const confirmClear=document.getElementById('confirmclear');
function closeConfirmClear(){ confirmClear.classList.remove('show'); }
document.getElementById('clearmine').onclick=()=>confirmClear.classList.add('show');
document.getElementById('confirmclearclose').onclick=closeConfirmClear;
document.getElementById('confirmclearno').onclick=closeConfirmClear;
document.getElementById('confirmclearyes').onclick=()=>{ collected=new Set(); saveSet(); paint(); refresh(); closeConfirmClear(); };
confirmClear.addEventListener('click',e=>{ if(e.target===confirmClear) closeConfirmClear(); });
document.getElementById('railtoggle').onchange=function(){ gRail.attr('display',this.checked?null:'none'); };
document.getElementById('zin').onclick=()=>svg.transition().duration(250).call(zoom.scaleBy,1.6);
document.getElementById('zout').onclick=()=>svg.transition().duration(250).call(zoom.scaleBy,1/1.6);
document.getElementById('menubtn').onclick=()=>{
  setSideOpen(!document.getElementById('side').classList.contains('open'));
};
function setSideOpen(open){
  const side=document.getElementById('side');
  side.classList.toggle('open',open);
  const btn=document.getElementById('menubtn');
  btn.innerHTML=open?'&times;':'&#9776;';
  btn.setAttribute('aria-expanded',String(open));
}

// legend
(function(){
  let catrows=cats.map(c=>`<div class="li"><span class="swatch" style="background:${CAT_COLOR[c]};border-radius:50%;border:1px solid rgba(255,255,255,.3)"></span>${CAT_KEY_LABEL[c]}</div>`).join('');
  let seen={},rl='';
  RAIL.forEach(r=>{ if(!seen[r.op]){seen[r.op]=1; rl+=`<div class="li"><span class="rsw" style="border-top-color:${r.color};${r.dash?'border-top-style:dashed;':''}"></span>${r.op}</div>`;} });
  const legend=document.getElementById('legend');
  legend.innerHTML=`<details class="catkey" open><summary>Catalog color</summary>${catrows}</details>
    <details><summary>Rail lines</summary>${rl}</details>`;
  if(matchMedia('(max-width:700px)').matches) legend.querySelector('.catkey').removeAttribute('open');
})();

// modal
const aboutEl=document.getElementById('about');
document.getElementById('infobtn').onclick=()=>aboutEl.classList.add('show');
document.getElementById('aboutclose').onclick=()=>aboutEl.classList.remove('show');
document.getElementById('aboutok').onclick=()=>aboutEl.classList.remove('show');
aboutEl.addEventListener('click',e=>{if(e.target===aboutEl)aboutEl.classList.remove('show');});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){aboutEl.classList.remove('show');closeConfirmClear();}});
try{ if(!localStorage.getItem('library_quest_ca_about_seen')){ aboutEl.classList.add('show'); localStorage.setItem('library_quest_ca_about_seen','1'); } }catch(e){}

refresh();
</script>
</body>
</html>"""

out=(HTML.replace("__DATA__",data_json)
        .replace("__RAIL__",rail_json)
        .replace("__TOTAL__",str(total_libby)))
open("california.html","w", encoding="utf-8").write(out)
print("wrote California map, bytes:",len(out),"libby:",total_libby)
