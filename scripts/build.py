"""Builds the animated SVGs in assets/ that the profile README shows. Run: python3 scripts/build.py"""
from html import escape
from pathlib import Path
import textwrap

OUT = Path(__file__).resolve().parent.parent / "assets"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
BG, INK, DIM = "#0a0e17", "#e8edf5", "#8b96a8"
# shared: honour reduced motion wherever the SVG is shown
CALM = "@media (prefers-reduced-motion: reduce) { * { animation: none !important; } }"


def write(name, svg):
    (OUT / name).write_text(svg.strip() + "\n", encoding="utf-8")


def hero():
    # a small network on the right: the "Digital Twin" idea, nodes pulsing and a signal travelling through it
    nodes = [(760, 120), (850, 70), (950, 110), (1040, 60), (1110, 140), (820, 210), (920, 200), (1020, 230),
             (1100, 290), (880, 300), (980, 320), (760, 290), (1150, 220), (700, 200)]
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 5), (5, 6), (2, 6), (6, 7), (7, 4), (7, 8), (6, 9), (9, 10), (10, 8),
             (5, 11), (11, 9), (4, 12), (12, 8), (13, 0), (13, 5), (13, 11), (2, 7)]
    lines = "\n".join(f'<line x1="{nodes[a][0]}" y1="{nodes[a][1]}" x2="{nodes[b][0]}" y2="{nodes[b][1]}" class="edge" '
                      f'style="animation-delay:{(i * 0.37) % 4:.2f}s"/>' for i, (a, b) in enumerate(edges))
    dots = "\n".join(f'<circle cx="{x}" cy="{y}" r="{5 if i % 3 else 7}" class="node" style="animation-delay:{(i * 0.53) % 3:.2f}s"/>'
                     for i, (x, y) in enumerate(nodes))
    route = " L ".join(f"{nodes[i][0]} {nodes[i][1]}" for i in (13, 0, 1, 2, 6, 7, 4, 12, 8, 10, 9, 11, 5, 13))
    chips = ["AI research", "LLM agents", "Speech + 3D", "XR", "Java at scale"]
    x, chip_svg = 64, []
    for c in chips:
        w = 18 + len(c) * 8.4
        chip_svg.append(f'<g transform="translate({x:.0f} 292)"><rect width="{w:.0f}" height="30" rx="15" class="chip"/>'
                        f'<text x="{w / 2:.0f}" y="20" text-anchor="middle" class="chiptext">{escape(c)}</text></g>')
        x += w + 10
    write("hero.svg", f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 380" width="1200" height="380" role="img" aria-label="Faaz Khan Mohammad: I build AI systems you can audit.">
<defs>
  <radialGradient id="g1" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#3fd6bd" stop-opacity=".45"/><stop offset="1" stop-color="#3fd6bd" stop-opacity="0"/></radialGradient>
  <radialGradient id="g2" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#8f6bff" stop-opacity=".45"/><stop offset="1" stop-color="#8f6bff" stop-opacity="0"/></radialGradient>
  <linearGradient id="name" x1="0" x2="1" y1="0" y2="0" gradientUnits="objectBoundingBox">
    <stop offset="0" stop-color="#ffffff"/><stop offset=".35" stop-color="#3fd6bd"/><stop offset=".65" stop-color="#b388ff"/><stop offset="1" stop-color="#ffffff"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="-1 0; 1 0" dur="7s" repeatCount="indefinite"/>
  </linearGradient>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#ffffff" stroke-opacity=".045"/></pattern>
  <clipPath id="card"><rect width="1200" height="380" rx="24"/></clipPath>
</defs>
<style>
  .edge {{ stroke: #3fd6bd; stroke-opacity: .18; stroke-width: 1.4; animation: edge 4s ease-in-out infinite; }}
  .node {{ fill: #0a0e17; stroke: #3fd6bd; stroke-width: 2; animation: node 3s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
  @keyframes edge {{ 0%,100% {{ stroke-opacity: .12; }} 50% {{ stroke-opacity: .55; stroke: #b388ff; }} }}
  @keyframes node {{ 0%,100% {{ transform: scale(1); fill: #0a0e17; }} 50% {{ transform: scale(1.35); fill: #3fd6bd; }} }}
  .drift1 {{ animation: d1 14s ease-in-out infinite alternate; }} .drift2 {{ animation: d2 17s ease-in-out infinite alternate; }}
  @keyframes d1 {{ to {{ transform: translate(120px, 40px); }} }} @keyframes d2 {{ to {{ transform: translate(-140px, -30px); }} }}
  .hi {{ font: 600 15px {MONO}; fill: #3fd6bd; letter-spacing: 3px; }}
  .name {{ font: 800 62px {SANS}; fill: url(#name); letter-spacing: -1px; }}
  .tag {{ font: 500 26px {SANS}; fill: {INK}; }}
  .sub {{ font: 400 17px {SANS}; fill: {DIM}; }}
  .chip {{ fill: #ffffff; fill-opacity: .06; stroke: #ffffff; stroke-opacity: .14; }}
  .chiptext {{ font: 500 13.5px {SANS}; fill: {INK}; }}
  {CALM}
</style>
<g clip-path="url(#card)">
  <rect width="1200" height="380" fill="{BG}"/>
  <rect width="1200" height="380" fill="url(#grid)"/>
  <circle class="drift1" cx="300" cy="80" r="320" fill="url(#g1)"/>
  <circle class="drift2" cx="1000" cy="320" r="340" fill="url(#g2)"/>
  <g>{lines}</g>
  <g>{dots}</g>
  <circle r="5" fill="#ffffff"><animateMotion dur="9s" repeatCount="indefinite" path="M {route}"/></circle>
  <circle r="12" fill="#3fd6bd" fill-opacity=".25"><animateMotion dur="9s" repeatCount="indefinite" path="M {route}"/></circle>
  <g><text x="64" y="92" class="hi">HELLO, I'M</text></g>
  <g><text x="62" y="158" class="name">Faaz Khan Mohammad</text></g>
  <g><text x="64" y="208" class="tag">I build AI systems you can audit.</text></g>
  <g><text x="64" y="248" class="sub">B.Tech Computer Science, MIT World Peace University · Pune, India</text></g>
  <g>{"".join(chip_svg)}</g>
  <rect x=".5" y=".5" width="1199" height="379" rx="24" fill="none" stroke="#ffffff" stroke-opacity=".1"/>
</g>
</svg>""")


def typing():
    lines = [
        "Building Rapport: an AI patient whose mind is code you can read",
        "3rd in India at Google Build with AI, out of 2,500+",
        "Ten projects shipped across AI agents, systems and XR",
        "Two journal manuscripts on trustworthy simulated patients",
        "Open to research collaborations and internships",
    ]
    W, H, fs, cw, per = 1200, 64, 22, 13.2, 5.0  # cw: monospace advance at 22px
    T = per * len(lines)
    css, body = [], []
    for i, ln in enumerate(lines):
        w = len(ln) * cw
        x0 = (W - w) / 2
        a, type_end, hold, gone = (i * per / T * 100, (i * per + 2.0) / T * 100, (i * per + 4.2) / T * 100,
                                   (i * per + 4.8) / T * 100)
        steps = len(ln)
        css.append(f"""@keyframes t{i} {{ 0%, {a:.2f}% {{ width: 0; opacity: 1; }} {type_end:.2f}% {{ width: {w + 2:.0f}px; }}
          {hold:.2f}% {{ width: {w + 2:.0f}px; opacity: 1; }} {gone:.2f}%, 100% {{ width: {w + 2:.0f}px; opacity: 0; }} }}
        @keyframes c{i} {{ 0% {{ opacity: 0; }} {max(a - 0.01, 0):.2f}% {{ opacity: 0; transform: translateX(0); }} {a:.2f}% {{ transform: translateX(0); opacity: 1; }} {type_end:.2f}% {{ transform: translateX({w + 4:.0f}px); }}
          {hold:.2f}% {{ transform: translateX({w + 4:.0f}px); opacity: 1; }} {gone:.2f}%, 100% {{ opacity: 0; transform: translateX({w + 4:.0f}px); }} }}
        .r{i} {{ animation: t{i} {T}s infinite; animation-timing-function: steps({steps}, end); width: 0; }}
        .k{i} {{ animation: c{i} {T}s infinite; animation-timing-function: steps({steps}, end); opacity: 0; }}""")
        body.append(f'<clipPath id="m{i}"><rect class="r{i}" x="{x0:.0f}" y="10" height="44"/></clipPath>'
                    f'<text x="{x0:.0f}" y="40" class="t" clip-path="url(#m{i})">{escape(ln)}</text>'
                    f'<rect class="k{i}" x="{x0:.0f}" y="18" width="11" height="28" fill="#3fd6bd"/>')
    write("typing.svg", f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{escape(' / '.join(lines))}">
<style>
  .t {{ font: 500 {fs}px {MONO}; fill: #3fd6bd; }}
  {"".join(css)}
  @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} .r0 {{ width: 2000px; }} .k0 {{ opacity: 0; }} }}
</style>
{"".join(body)}
</svg>""")


def stats():
    # every number is from the two papers (papers/ in faazkhn/Rapport)
    tiles = [
        ("512", "blind benchmark questions", "reworded, with a strict test split"),
        ("0 vs 6", "jailbreak checks failed", "code-governed vs prompt-only"),
        ("1.8 s", "to the patient's first word", "median, all on one laptop"),
        ("0 bytes", "leave the device", "no audio or text sent anywhere"),
    ]
    bars = [("Keyword tags", 35.1, "#5b6b82"), ("Hybrid: tags + 33M encoder (deployed)", 72.7, "#3fd6bd"),
            ("Same 4B model, zero-shot", 94.8, "#b388ff")]
    tile_svg = []
    for i, (big, lab, small) in enumerate(tiles):
        x = 40 + i * 285
        tile_svg.append(f"""<g transform="translate({x} 112)">
  <rect width="265" height="128" rx="16" class="tile"/>
  <text x="22" y="56" class="big">{escape(big)}</text>
  <text x="22" y="86" class="lab">{escape(lab)}</text>
  <text x="22" y="108" class="small">{escape(small)}</text></g>""")
    bar_svg = []
    for i, (lab, v, col) in enumerate(bars):
        y = 330 + i * 52
        w = 760 * v / 100
        bar_svg.append(f"""<text x="40" y="{y + 19}" class="blab">{escape(lab)}</text>
<rect x="390" y="{y}" width="760" height="26" rx="13" class="track"/>
<rect x="390" y="{y}" width="{w:.1f}" height="26" rx="13" fill="{col}" class="bar"/>
<text x="{390 + w - 12:.1f}" y="{y + 18}" text-anchor="end" class="bval">{v}%</text>""")
    write("rapport-stats.svg", f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 500" width="1200" height="500" role="img" aria-label="Rapport in numbers: 512-question blind benchmark; 0 jailbreak checks failed versus 6 for a prompt-only baseline; 1.8 s median to first word; fully on-device. Reworded risk-question recall on the test half: keyword tags 35.1%, deployed hybrid 72.7%, zero-shot 4B model 94.8%.">
<defs><linearGradient id="edge" x1="0" x2="1"><stop offset="0" stop-color="#3fd6bd"/><stop offset="1" stop-color="#b388ff"/></linearGradient></defs>
<style>
  .tile {{ fill: #ffffff; fill-opacity: .045; stroke: #ffffff; stroke-opacity: .1; }}
  .big {{ font: 800 40px {SANS}; fill: url(#edge); }}
  .lab {{ font: 600 15px {SANS}; fill: {INK}; }}
  .small {{ font: 400 12.5px {SANS}; fill: {DIM}; }}
  .h {{ font: 800 26px {SANS}; fill: {INK}; }} .hs {{ font: 400 15px {SANS}; fill: {DIM}; }}
  .k {{ font: 600 13px {MONO}; fill: #3fd6bd; letter-spacing: 2.5px; }}
  .blab {{ font: 500 15px {SANS}; fill: {INK}; }} .bval {{ font: 700 14px {MONO}; fill: #0a0e17; }}
  .track {{ fill: #ffffff; fill-opacity: .06; }}
  .bar {{ animation: grow 1.4s cubic-bezier(.2,.8,.2,1) both; transform-origin: 390px 0; }}
  @keyframes grow {{ from {{ transform: scaleX(0); }} }}
  {CALM}
</style>
<rect width="1200" height="500" rx="24" fill="{BG}"/>
<rect x=".5" y=".5" width="1199" height="499" rx="24" fill="none" stroke="#ffffff" stroke-opacity=".1"/>
<text x="40" y="52" class="k">RAPPORT · IN NUMBERS</text>
<text x="40" y="86" class="h">Decide in code, voice with the model</text>
{"".join(tile_svg)}
<text x="40" y="300" class="lab">Reworded suicide-risk questions recognised, held-out test half</text>
{"".join(bar_svg)}
</svg>""")


CARDS = [
    # (file, title, badge, one-liner, tech, accent, team)
    ("prevista", "Prevista", "Founder · CII 2026 University Startups",
     "Walk through your next home before you visit it: true-to-scale VR tours on Meta Quest 3, guided live by an agent.",
     ["Meta Quest 3", "OpenXR", "Blender", "Live agent control"], "#d9835a"),
    ("cyclone-sentinel", "CycloneSentinel", "3rd in India · Google Build with AI",
     "Predicts what a cyclone will break a day before landfall: which hospitals lose power, which roads flood, who to warn.",
     ["Gemini", "Earth Engine", "NASA VIIRS", "Cloud Run"], "#4cc9f0"),
    ("segsense", "SegSense", "Nebius × NVIDIA Global AI Hackathon",
     "Hunts segfaults and leaks in C with AddressSanitizer, patches the bug and re-tests. Only sanitizer-clean fixes count.",
     ["C", "AddressSanitizer", "Nemotron", "Docker"], "#9be15d"),
    ("allowance", "Allowance", "PayPal AI Hackathon",
     "AI buying agents for a team: they find the deal and pay with PayPal, while code, not the model, enforces the budget.",
     ["Next.js", "PayPal Vault", "Gemini", "Zod"], "#3d9be9"),
    ("huddle", "Huddle", "Amazon Developer Hackathon",
     "A Fire TV party game where every phone becomes the TV's camera and on-device pose estimation scores your form.",
     ["Fire TV", "MediaPipe Pose", "Bedrock", "WebSockets"], "#ff9900"),
    ("hivemind", "Hivemind", "Codex × TwitchCon Hackathon",
     "Turns a Twitch chat too fast to read into one live AI character that speaks for the whole crowd.",
     ["TypeScript", "EventSub", "Embeddings", "OBS"], "#b388ff"),
    ("ridetaste", "RideTaste", "Qloo Agentic Hackathon",
     "Tell it the films, music and food you and a friend love; it plans a bike ride with stops you'd both enjoy.",
     ["Qloo Taste AI", "Function calling", "OSRM", "Leaflet"], "#ff6b6b"),
    ("lecture-kit", "Lecture Revision Kit", "UGREEN Hackathon 2026 on AI NAS",
     "Recordings, slides and board photos in, sourced revision notes out, all on a home AI NAS.",
     ["Agent workflows", "Speech to text", "OCR", "On-device"], "#39d98a"),
    ("scanforge", "ScanForge", "Personal project",
     "Turns a camera, phone or video capture of an object into a point-based 3D model.",
     ["3D reconstruction", "Point clouds", "Python"], "#f5c542"),
]


def card(file, title, badge, line, tech, accent, wide=False):
    W, H = (1200, 210) if wide else (590, 250)
    wrap = textwrap.wrap(line, 100 if wide else 58)
    text = "".join(f'<text x="28" y="{118 + i * 24}" class="d">{escape(t)}</text>' for i, t in enumerate(wrap))
    x, chips = 28, []
    for t in tech:
        w = 16 + len(t) * 7.3
        chips.append(f'<g transform="translate({x:.0f} {H - 52})"><rect width="{w:.0f}" height="26" rx="13" class="chip"/>'
                     f'<text x="{w / 2:.0f}" y="17.5" text-anchor="middle" class="ct">{escape(t)}</text></g>')
        x += w + 8
    write(f"card-{file}.svg", f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{escape(title)}: {escape(badge)}. {escape(line)}">
<defs>
  <radialGradient id="glow" cx="1" cy="0" r="1"><stop offset="0" stop-color="{accent}" stop-opacity=".32"/><stop offset=".6" stop-color="{accent}" stop-opacity="0"/></radialGradient>
  <linearGradient id="sheen" x1="0" x2="1"><stop offset="0" stop-color="{accent}" stop-opacity="0"/><stop offset=".5" stop-color="{accent}"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></linearGradient>
  <clipPath id="c"><rect width="{W}" height="{H}" rx="20"/></clipPath>
</defs>
<style>
  .t {{ font: 800 30px {SANS}; fill: {INK}; }}
  .b {{ font: 600 13px {MONO}; fill: {accent}; letter-spacing: .5px; }}
  .d {{ font: 400 16px {SANS}; fill: #c3ccda; }}
  .chip {{ fill: {accent}; fill-opacity: .12; stroke: {accent}; stroke-opacity: .4; }}
  .ct {{ font: 500 12px {SANS}; fill: {INK}; }}
  .sheen {{ animation: sweep 5s ease-in-out infinite; }} @keyframes sweep {{ from {{ transform: translateX(-{W}px); }} to {{ transform: translateX({W}px); }} }}
  .pulse {{ animation: pulse 2.4s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
  @keyframes pulse {{ 50% {{ transform: scale(1.6); opacity: .35; }} }}
  {CALM}
</style>
<g clip-path="url(#c)">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <rect width="{W}" height="{H}" fill="url(#glow)"/>
  <rect class="sheen" y="0" width="{W}" height="3" fill="url(#sheen)"/>
  <circle class="pulse" cx="{W - 34}" cy="34" r="6" fill="{accent}"/>
  <text x="28" y="52" class="b">{escape(badge.upper())}</text>
  <text x="28" y="88" class="t">{escape(title)}</text>
  {text}
  {"".join(chips)}
  <rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="20" fill="none" stroke="#ffffff" stroke-opacity=".1"/>
</g>
</svg>""")


def footer():
    waves = []
    for i, (col, op, dur, amp) in enumerate([("#3fd6bd", .28, 9, 18), ("#b388ff", .22, 12, 24), ("#4cc9f0", .16, 15, 14)]):
        y = 96 + i * 10
        d1 = f"M0 {y} C 300 {y - amp}, 600 {y + amp}, 1200 {y} L1200 160 L0 160 Z"
        d2 = f"M0 {y} C 300 {y + amp}, 600 {y - amp}, 1200 {y} L1200 160 L0 160 Z"
        waves.append(f'<path d="{d1}" fill="{col}" fill-opacity="{op}"><animate attributeName="d" dur="{dur}s" repeatCount="indefinite" '
                     f'values="{d1};{d2};{d1}"/></path>')
    write("footer.svg", f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 160" width="1200" height="160" role="img" aria-label="faazkhan.in">
<style>.f {{ font: 600 15px {MONO}; fill: #ffffff; letter-spacing: 4px; }}</style>
<defs><clipPath id="c"><rect width="1200" height="160" rx="24"/></clipPath></defs>
<g clip-path="url(#c)"><rect width="1200" height="160" fill="{BG}"/>{"".join(waves)}
<text x="600" y="70" text-anchor="middle" class="f">FAAZKHAN.IN</text></g>
</svg>""")


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    hero(); typing(); stats(); footer()
    for i, c in enumerate(CARDS):
        card(*c, wide=(i == 0))
    print("wrote", len(list(OUT.glob("*.svg"))), "SVGs")
