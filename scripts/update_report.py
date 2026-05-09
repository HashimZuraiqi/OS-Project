"""
update_report.py
================
Converts docs/REPORT_DRAFT.md to docs/REPORT_VIEWER.html.

Usage:
  python scripts/update_report.py           # one-shot generation
  python scripts/update_report.py --watch   # watch for changes and auto-regenerate

When --watch is active, the HTML gets a <meta http-equiv="refresh"> tag so the
browser auto-reloads each time the markdown is saved.
"""

import os
import sys
import re
import time

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_PATH   = os.path.join(REPO_ROOT, "docs", "REPORT_DRAFT.md")
HTML_PATH = os.path.join(REPO_ROOT, "docs", "REPORT_VIEWER.html")


# ─────────────────────────────────────────────────────────────────────────────
# Markdown → HTML (no external dependencies)
# ─────────────────────────────────────────────────────────────────────────────

def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def inline(text):
    parts = re.split(r'(`[^`]+`)', text)
    out = []
    for p in parts:
        if p.startswith('`') and p.endswith('`'):
            out.append('<code>' + esc(p[1:-1]) + '</code>')
        else:
            s = esc(p)
            s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
            s = re.sub(r'\*(.+?)\*',     r'<em>\1</em>', s)
            s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', s)
            out.append(s)
    return ''.join(out)

def parse_table(lines):
    rows = [[c.strip() for c in ln.strip().strip('|').split('|')] for ln in lines]
    if len(rows) < 2:
        return ''
    html = ['<table><thead><tr>']
    for c in rows[0]:
        html.append(f'<th>{inline(c)}</th>')
    html.append('</tr></thead><tbody>')
    for row in rows[2:]:
        html.append('<tr>')
        for c in row:
            html.append(f'<td>{inline(c)}</td>')
        html.append('</tr>')
    html.append('</tbody></table>')
    return ''.join(html)

def parse_markdown(md_text):
    lines     = md_text.split('\n')
    html      = []
    i         = 0
    in_list   = False
    list_type = None

    def close_list():
        nonlocal in_list, list_type
        if in_list:
            html.append(f'</{list_type}>')
            in_list = False
            list_type = None

    while i < len(lines):
        line = lines[i]

        # Fenced code block
        if line.strip().startswith('```'):
            close_list()
            lang = line.strip()[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(esc(lines[i]))
                i += 1
            lc = f' class="language-{lang}"' if lang else ''
            html.append(f'<pre><code{lc}>' + '\n'.join(code_lines) + '</code></pre>')
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^---+$', line.strip()):
            close_list()
            html.append('<hr>')
            i += 1
            continue

        # Headings
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            close_list()
            level = len(m.group(1))
            text  = inline(m.group(2))
            slug  = re.sub(r'[^a-z0-9]+', '-', m.group(2).lower()).strip('-')
            html.append(f'<h{level} id="{slug}">{text}</h{level}>')
            i += 1
            continue

        # Table (detect by pipe + separator row)
        if '|' in line and i + 1 < len(lines) and re.match(r'^\|?[\s\-:]+\|', lines[i + 1]):
            close_list()
            tbl = [line]
            i += 1
            while i < len(lines) and '|' in lines[i]:
                tbl.append(lines[i])
                i += 1
            html.append(parse_table(tbl))
            continue

        # Unordered list
        m = re.match(r'^(\s*)[-*+]\s+(.*)', line)
        if m:
            if not in_list or list_type != 'ul':
                close_list()
                html.append('<ul>')
                in_list = True
                list_type = 'ul'
            html.append(f'<li>{inline(m.group(2))}</li>')
            i += 1
            continue

        # Ordered list
        m = re.match(r'^\d+\.\s+(.*)', line)
        if m:
            if not in_list or list_type != 'ol':
                close_list()
                html.append('<ol>')
                in_list = True
                list_type = 'ol'
            html.append(f'<li>{inline(m.group(1))}</li>')
            i += 1
            continue

        # Blockquote
        if line.startswith('>'):
            close_list()
            html.append(f'<blockquote><p>{inline(line[1:].strip())}</p></blockquote>')
            i += 1
            continue

        # Empty line
        if line.strip() == '':
            close_list()
            i += 1
            continue

        # Paragraph
        close_list()
        para = []
        while i < len(lines) and lines[i].strip() != '' \
              and not lines[i].strip().startswith('#') \
              and not lines[i].strip().startswith('```') \
              and not re.match(r'^---+$', lines[i].strip()) \
              and not re.match(r'^(\s*)[-*+]\s', lines[i]) \
              and not re.match(r'^\d+\.\s', lines[i]) \
              and '|' not in lines[i]:
            para.append(lines[i])
            i += 1
        if para:
            html.append('<p>' + inline(' '.join(para)) + '</p>')

    close_list()
    return '\n'.join(html)


# ─────────────────────────────────────────────────────────────────────────────
# Static data & chart helpers
# ─────────────────────────────────────────────────────────────────────────────

TEAM_MEMBERS = [
    {"name": "Faris Asaad",      "id": "20230015", "email": "far20230015@std.psut.edu.jo", "algo": "FCFS"},
    {"name": "Hashim Zuraiqi",   "id": "20230166", "email": "has20230166@std.psut.edu.jo", "algo": "SRTF"},
    {"name": "Mohammad Amayreh", "id": "20230424", "email": "moh20230424@std.psut.edu.jo", "algo": "Priority"},
    {"name": "Nour Al-Qatarneh", "id": "20221067", "email": "nou20221067@std.psut.edu.jo", "algo": "Round Robin"},
    {"name": "Zina Hijazeen",    "id": "20210853", "email": "zin20210853@std.psut.edu.jo", "algo": "SJF"},
]

ALGO_TC1 = [
    {"name": "FCFS",       "awt": 9.25,  "atat": 14.75, "cs": 0,  "color": "#e53935", "preemptive": False},
    {"name": "SJF",        "awt": 8.50,  "atat": 14.00, "cs": 0,  "color": "#43a047", "preemptive": False},
    {"name": "SRTF",       "awt": 5.00,  "atat": 10.50, "cs": 1,  "color": "#1e88e5", "preemptive": True},
    {"name": "Priority",   "awt": 8.75,  "atat": 14.25, "cs": 0,  "color": "#fb8c00", "preemptive": False},
    {"name": "RR (Q=2)",   "awt": 10.25, "atat": 15.75, "cs": 10, "color": "#8e24aa", "preemptive": True},
]

ALGO_TC2 = [
    {"name": "FCFS",       "awt": 18.75, "atat": 26.50, "color": "#e53935"},
    {"name": "SJF",        "awt": 18.75, "atat": 26.50, "color": "#43a047"},
    {"name": "SRTF",       "awt": 2.25,  "atat": 10.00, "color": "#1e88e5"},
    {"name": "Priority",   "awt": 18.75, "atat": 26.50, "color": "#fb8c00"},
    {"name": "RR (Q=2)",   "awt": 3.50,  "atat": 11.25, "color": "#8e24aa"},
]

def bar_chart_h(dataset, val_key, title, unit="ms"):
    max_v = max(a[val_key] for a in dataset) or 1
    rows  = []
    for a in dataset:
        pct = int(a[val_key] / max_v * 100)
        rows.append(
            f'<div class="bar-row">'
            f'<div class="bar-label">{a["name"]}</div>'
            f'<div class="bar-track">'
            f'<div class="bar-fill" style="width:{pct}%;background:{a["color"]};">'
            f'<span class="bar-val">{a[val_key]} {unit}</span>'
            f'</div></div></div>'
        )
    return f'<div class="chart-block"><h4>{title}</h4>' + ''.join(rows) + '</div>'

def algo_dashboard():
    cards = []
    cls_map = {
        "FCFS": "algo-fcfs", "SJF": "algo-sjf", "SRTF": "algo-srtf",
        "Priority": "algo-pri", "RR (Q=2)": "algo-rr",
    }
    for a in ALGO_TC1:
        badge = "badge-pre" if a["preemptive"] else "badge-nonpre"
        label = "Preemptive" if a["preemptive"] else "Non-Preemptive"
        cls   = cls_map.get(a["name"], "")
        cards.append(
            f'<div class="algo-card {cls}">'
            f'<h4>{a["name"]} <span class="badge {badge}">{label}</span></h4>'
            f'<div class="algo-metrics">'
            f'AWT: <strong>{a["awt"]} ms</strong> &nbsp;|&nbsp; '
            f'ATAT: <strong>{a["atat"]} ms</strong> &nbsp;|&nbsp; '
            f'Ctx SW: <strong>{a["cs"]}</strong>'
            f'</div></div>'
        )
    return '<div class="algo-grid">' + ''.join(cards) + '</div>'


# ─────────────────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────────────────

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',Arial,sans-serif;background:#f4f6f9;color:#2c3e50;line-height:1.7;font-size:15px}
.container{max-width:1020px;margin:0 auto;padding:24px 16px}
/* Cover */
.cover{background:linear-gradient(135deg,#1a237e,#283593 55%,#0d47a1);color:#fff;padding:56px 40px;border-radius:14px;margin-bottom:28px;text-align:center}
.cover h1{font-size:2em;line-height:1.3;margin-bottom:12px}
.cover .sub{opacity:.85;font-size:.97em;margin-bottom:28px}
.team-grid{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin-top:18px}
.team-card{background:rgba(255,255,255,.15);border-radius:8px;padding:10px 16px;min-width:155px}
.team-card .tn{font-weight:700;font-size:.93em}
.team-card .tid{font-size:.78em;opacity:.8}
.team-card .tem{font-size:.72em;opacity:.7}
/* Cards */
.card{background:#fff;border-radius:12px;padding:30px 36px;margin-bottom:22px;box-shadow:0 2px 14px rgba(0,0,0,.07)}
.card h2{font-size:1.45em;color:#1a237e;border-bottom:3px solid #1a237e;padding-bottom:8px;margin-bottom:20px}
.card h3{font-size:1.12em;color:#283593;margin:22px 0 10px}
.card h4{font-size:1em;color:#37474f;margin:16px 0 8px}
p{margin-bottom:12px}
ul,ol{margin:8px 0 12px 26px}
li{margin-bottom:4px}
hr{border:none;border-top:1px solid #e0e0e0;margin:20px 0}
strong{color:#1a237e}
em{color:#37474f}
a{color:#1565c0}
blockquote{border-left:4px solid #1a237e;background:#f5f6ff;padding:10px 16px;border-radius:4px;margin:12px 0}
/* Tables */
table{width:100%;border-collapse:collapse;margin:14px 0;font-size:.91em}
th{background:#1a237e;color:#fff;padding:10px 14px;text-align:left}
td{padding:8px 14px;border-bottom:1px solid #e8eaf0}
tr:nth-child(even) td{background:#f5f6ff}
tr:hover td{background:#eef0fb}
/* Code */
pre{background:#263238;color:#cfd8dc;border-radius:8px;padding:16px 20px;overflow-x:auto;margin:14px 0;font-size:.87em;font-family:'Consolas','Courier New',monospace;line-height:1.5}
code{font-family:'Consolas','Courier New',monospace}
p code,li code{background:#e8eaf6;color:#283593;padding:2px 6px;border-radius:4px;font-size:.9em}
/* Algo dashboard */
.algo-grid{display:flex;flex-wrap:wrap;gap:14px;margin:14px 0}
.algo-card{flex:1;min-width:270px;border-radius:8px;padding:14px 18px;border-left:5px solid}
.algo-fcfs{border-color:#e53935;background:#fff5f5}
.algo-sjf {border-color:#43a047;background:#f1f8f1}
.algo-srtf{border-color:#1e88e5;background:#f0f7ff}
.algo-pri {border-color:#fb8c00;background:#fff8f0}
.algo-rr  {border-color:#8e24aa;background:#faf0ff}
.algo-card h4{margin:0 0 6px;font-size:.97em}
.algo-metrics{font-size:.84em;color:#546e7a}
.algo-metrics strong{color:#2c3e50}
.badge{display:inline-block;padding:2px 9px;border-radius:12px;font-size:.75em;font-weight:600;margin-left:6px}
.badge-pre{background:#e3f2fd;color:#1565c0}
.badge-nonpre{background:#fce4ec;color:#c62828}
/* Charts */
.chart-section{display:flex;flex-wrap:wrap;gap:20px;margin:18px 0}
.chart-block{flex:1;min-width:290px}
.chart-block h4{margin-bottom:10px;color:#283593}
.bar-row{display:flex;align-items:center;margin-bottom:7px}
.bar-label{width:90px;font-size:.82em;text-align:right;padding-right:10px;color:#455a64;flex-shrink:0}
.bar-track{flex:1;background:#eceff1;border-radius:4px;overflow:hidden;height:26px}
.bar-fill{height:100%;display:flex;align-items:center;padding-left:8px;border-radius:4px;min-width:38px;transition:width .3s}
.bar-val{color:#fff;font-size:.8em;font-weight:600;white-space:nowrap}
/* Print */
.print-btn{display:inline-block;background:#1a237e;color:#fff;padding:10px 24px;border-radius:6px;cursor:pointer;border:none;font-size:.93em;margin-top:8px}
.print-btn:hover{background:#283593}
.footer{text-align:center;font-size:.82em;color:#90a4ae;padding:20px 0;margin-top:8px}
.watch-badge{background:#fff9c4;padding:8px 14px;border-radius:6px;font-size:.85em;margin-bottom:16px}
@media print{
  .print-btn,.watch-badge{display:none}
  body{background:#fff}
  .card{box-shadow:none;border:1px solid #e0e0e0;page-break-inside:avoid}
  .cover{print-color-adjust:exact;-webkit-print-color-adjust:exact}
}
"""


# ─────────────────────────────────────────────────────────────────────────────
# HTML assembly
# ─────────────────────────────────────────────────────────────────────────────

def generate_html(md_text, watch_mode=False):
    body_html = parse_markdown(md_text)
    # Strip first H1 (shown in cover)
    body_html = re.sub(r'<h1[^>]*>.*?</h1>\s*', '', body_html, count=1)

    ts      = time.strftime("%Y-%m-%d %H:%M:%S")
    refresh = '<meta http-equiv="refresh" content="3">' if watch_mode else ''
    watch_n = ('<div class="watch-badge">&#x21BA; Live mode — browser auto-refreshes every 3 seconds</div>'
               if watch_mode else '')

    team_html = ''.join(
        f'<div class="team-card">'
        f'<div class="tn">{m["name"]}</div>'
        f'<div class="tid">{m["id"]} &middot; {m["algo"]}</div>'
        f'<div class="tem">{m["email"]}</div>'
        f'</div>'
        for m in TEAM_MEMBERS
    )

    tc1_awt  = bar_chart_h(ALGO_TC1, "awt",  "Average Waiting Time — Test Case 1")
    tc1_atat = bar_chart_h(ALGO_TC1, "atat", "Average Turnaround Time — Test Case 1")
    tc2_awt  = bar_chart_h(ALGO_TC2, "awt",  "AWT — Test Case 2 (Convoy Effect)")
    tc2_atat = bar_chart_h(ALGO_TC2, "atat", "ATAT — Test Case 2 (Convoy Effect)")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  {refresh}
  <title>CPU Scheduling — Performance Evaluation</title>
  <style>{CSS}</style>
</head>
<body>
<div class="container">
  {watch_n}

  <!-- COVER -->
  <div class="cover">
    <h1>Performance Evaluation of CPU Scheduling Algorithms</h1>
    <div class="sub">
      CS11335 – Operating Systems &nbsp;&bull;&nbsp;
      Princess Sumaya University for Technology<br>
      King Hussein School of Computing Sciences &middot; Computer Science
    </div>
    <div class="team-grid">{team_html}</div>
    <div style="margin-top:20px;font-size:.83em;opacity:.7">
      Language: C++ &nbsp;&bull;&nbsp; Generated: {ts}
    </div>
  </div>

  <!-- DASHBOARD -->
  <div class="card">
    <h2>Results at a Glance — Test Case 1</h2>
    <p>Process set: P1 (arr=0, burst=10) · P2 (arr=1, burst=4) · P3 (arr=2, burst=5) · P4 (arr=3, burst=3).
       RR time quantum = 2 ms. Priority: lower number = higher priority.</p>
    {algo_dashboard()}
    <div class="chart-section">{tc1_awt}{tc1_atat}</div>
    <p style="font-size:.85em;color:#78909c">
      Best AWT: <strong>SRTF 5.00 ms</strong> (46% better than FCFS).
      Best ATAT: <strong>SRTF 10.50 ms</strong>.
      RR has highest AWT but provides the best fairness guarantee.
    </p>
  </div>

  <!-- CONVOY EFFECT -->
  <div class="card">
    <h2>Convoy Effect — Test Case 2</h2>
    <p>P1 (arr=0, burst=25) · P2 (arr=1, burst=2) · P3 (arr=2, burst=2) · P4 (arr=3, burst=2).
       Non-preemptive algorithms cannot interrupt P1, yielding AWT = 18.75 ms.
       SRTF preempts P1 at t=1: <strong>88% AWT reduction</strong>. RR also limits P1 to 2 ms slices.</p>
    <div class="chart-section">{tc2_awt}{tc2_atat}</div>
  </div>

  <!-- FULL REPORT -->
  <div class="card">
    {body_html}
  </div>

  <!-- FOOTER -->
  <div class="footer">
    <button class="print-btn" onclick="window.print()">&#128438; Print / Save as PDF</button><br><br>
    Princess Sumaya University for Technology &middot; CS11335 Operating Systems
    &middot; {ts}
  </div>
</div>
</body>
</html>"""


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

def generate_once(watch_mode=False):
    with open(MD_PATH, 'r', encoding='utf-8') as f:
        md_text = f.read()
    html = generate_html(md_text, watch_mode=watch_mode)
    with open(HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"[{time.strftime('%H:%M:%S')}] Generated → {HTML_PATH}")


def watch():
    print(f"Watching {MD_PATH} for changes  (Ctrl+C to stop)")
    last_mtime = None
    generate_once(watch_mode=True)
    last_mtime = os.path.getmtime(MD_PATH)
    while True:
        try:
            mtime = os.path.getmtime(MD_PATH)
            if mtime != last_mtime:
                last_mtime = mtime
                generate_once(watch_mode=True)
                print("  → HTML updated. Browser will refresh in 3 s.")
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopped. Generating final HTML (no auto-refresh)...")
            generate_once(watch_mode=False)
            print("Done.")
            break


if __name__ == '__main__':
    if '--watch' in sys.argv:
        watch()
    else:
        generate_once(watch_mode=False)
