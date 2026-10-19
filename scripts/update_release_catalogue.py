#!/usr/bin/env python3
"""Rebuild collection indexes from small per-project manifests in a sparse checkout."""
import csv, html, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def main():
    manifests=[json.loads(p.read_text()) for p in sorted((ROOT/'paper-assets').glob('*/08-index/asset-manifest.json'))]
    n=len(manifests)
    collection=json.loads((ROOT/'traces/projects.json').read_text())
    stats={p['project']:p['statistics'] for p in collection['projects']}
    root_readme=(ROOT/'README.md').read_text()
    import re
    root_readme=re.sub(r'The repository currently contains .*? paper projects\.',f'The repository currently contains {n} research projects with manuscripts and supporting assets.',root_readme)
    root_readme=re.sub(r'interactive \d+-item asset matrix','interactive project asset matrix',root_readme)
    (ROOT/'README.md').write_text(root_readme)
    content=['# Contents','',f'This catalogue covers **{n} research projects**. Open a project README for its manuscript, research code, experiment outputs, and recorded research process.','', '| Project | Manuscript | Code/config files | Data/result files | Trace sources | Recorded events |','|---|---|---:|---:|---:|---:|']
    cards=[];matrix=[]
    for m in manifests:
        p=m['project'];s=stats.get(p,{})
        pdf=f'[PDF](paper-assets/{p}/01-manuscript/paper.pdf)' if m.get('paper_pdf') else 'No PDF in snapshot'
        content.append(f"| [{p}](paper-assets/{p}/README.md) | {pdf} | {m['code_count']:,} | {m['data_count']:,} | {s.get('files',m.get('trace_count',0)):,} | {s.get('messages',0):,} |")
        evidence=''.join('<tr><th>'+html.escape(r['name'])+'</th><td>'+html.escape(r['status'])+'</td><td>'+html.escape(r['evidence'])+'</td><td>'+html.escape(r['gap'])+'</td></tr>' for r in m['criteria'])
        for r in m['criteria']:matrix.append([p,m['title'],r['name'],r['status'],r['evidence'],r['gap'],p+'/'+r['path']])
        links=f'<a href="{p}/README.md">Asset guide</a><a href="{p}/03-code/source/">Research code</a><a href="{p}/05-generation-trace/readable/README.md">Read conversations</a>'
        if m.get('paper_pdf'):links=f'<a href="{p}/01-manuscript/paper.pdf">Paper PDF</a>'+links
        cards.append(f'<article data-search="{html.escape((p+" "+m["title"]).lower(),quote=True)}"><small>{html.escape(p)}</small><h2>{html.escape(m["title"])}</h2><p>{m["code_count"]:,} code/configuration files · {m["data_count"]:,} data/result files · {s.get("files",m.get("trace_count",0)):,} trace sources</p><nav>{links}</nav><details><summary>Asset evidence and verification limits</summary><div class="table"><table><thead><tr><th>Requirement</th><th>Status</th><th>Evidence</th><th>Limit</th></tr></thead><tbody>{evidence}</tbody></table></div></details></article>')
    content+=['','[Interactive asset catalogue](paper-assets/index.html) · [Full asset matrix](paper-assets/asset-matrix.csv) · [Readable trace guides](traces/README.md)','', 'Counts describe archived files and recorded events, including overlapping snapshots. Code presence does not establish reproduction. Internal reviews and manuscript labels do not establish external acceptance. Source documents preserve their original language.','']
    (ROOT/'CONTENTS.md').write_text('\n'.join(content))
    with (ROOT/'paper-assets/asset-matrix.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['Paper project','Paper title','Category','Status','Organized assets','Open questions / gaps','Asset directory']);w.writerows(matrix)
    page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Research assets</title><style>
    *{box-sizing:border-box}body{margin:0;background:#f4f6f5;color:#163134;font:15px/1.6 system-ui,sans-serif}header{background:#153e42;color:#fff;padding:48px max(24px,calc((100% - 1160px)/2))}header p{color:#c5dad8;max-width:780px}h1{font-size:38px;line-height:1.15}main{max-width:1208px;margin:auto;padding:24px}input{width:100%;padding:14px 18px;border:1px solid #b9ceca;border-radius:8px;font:inherit;margin:8px 0 24px}article{background:white;border:1px solid #d4dfdc;padding:24px;margin-bottom:18px;border-radius:10px}small{font:12px ui-monospace,monospace;color:#54706b}h2{margin:8px 0;font-size:22px;line-height:1.35}article p{color:#54706b}nav{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0}a{color:#116b60}nav a{border:1px solid #cbdad6;padding:7px 12px;border-radius:5px;text-decoration:none}nav a:first-child{background:#146459;color:white}summary{cursor:pointer;font-weight:600}.table{overflow:auto}table{border-collapse:collapse;font-size:12px;min-width:800px;margin-top:14px}th,td{border-bottom:1px solid #d8e1df;padding:10px;text-align:left;vertical-align:top}td{min-width:100px}td:nth-child(3),td:nth-child(4){min-width:220px}.notice{padding:14px 18px;border-left:4px solid #a67c36;background:#fff9ec;margin-bottom:24px}[hidden]{display:none}footer{padding:20px;color:#54706b} @media(max-width:600px){h1{font-size:29px}h2{font-size:19px}article{padding:18px}main{padding:16px}}
    </style><header><small style="color:#b7d8d2">AUTOMATED RESEARCH / REVIEWABLE EVIDENCE</small><h1>Research assets</h1><p>Manuscripts, code, experiment results, and readable research conversations from COUNT projects.</p></header><main><div class="notice">Project files document generated research and its workflow. Experimental reproduction, author identity, submission, and external acceptance are not established by these files alone.</div><label for="search">Find a project or paper</label><input id="search" placeholder="Search titles or project names…" type="search"><p id="count">COUNT projects</p>CARDS<footer>Generated guides are English; original evidence retains its recorded language. <a href="asset-matrix.csv">Download asset matrix</a> · <a href="../traces/README.md">Trace catalogue</a></footer></main><script>const cards=[...document.querySelectorAll('article')];document.querySelector('#search').addEventListener('input',e=>{const q=e.target.value.toLowerCase().trim();for(const c of cards)c.hidden=!c.dataset.search.includes(q);document.querySelector('#count').textContent=cards.filter(c=>!c.hidden).length+' projects';});</script></html>'''.replace('COUNT',str(n)).replace('CARDS',''.join(cards))
    (ROOT/'paper-assets/index.html').write_text(page)
    trace=['# Research Trace Atlas','',f'Browse recorded tasks, user-role instructions, assistant responses, tool calls, and tool results from **{len(stats)} research projects**. Open **Readable Markdown** in any project guide for a GitHub reading view, or select the adjacent JSON link for the complete structured record.','', '[Offline preview](demo.html) · [Interactive browser](index.html) · [Format and provenance](FORMAT.md)','','For the complete browser, run `python3 scripts/serve_traces.py --open` from a downloaded repository. The offline preview embeds one actual bounded round per project when a matching round exists.','','| Project | Conversations | Worker logs | Results | Context notes | Events | Readable Markdown |','|---|---:|---:|---:|---:|---:|---|']
    for p in collection['projects']:
        s=p['statistics'];slug=p['project'];trace.append(f"| [{slug}](../paper-assets/{slug}/05-generation-trace/README.md) | {s.get('conversation',0):,} | {s.get('worker',0):,} | {s.get('result',0):,} | {s.get('history',0):,} | {s.get('messages',0):,} | [Read](../paper-assets/{slug}/05-generation-trace/readable/README.md) |")
    total=sum(s.get('messages',0) for s in stats.values());sources=sum(s.get('files',0) for s in stats.values())
    trace+=['',f'**{sources:,} source records · {total:,} recorded messages/events.** Counts include overlapping snapshots and parallel logs; they are not deduplicated research actions.','','Source language and order are retained. A user-role message can originate from another agent or system and does not identify a human author. Missing prompts and timestamps are not reconstructed. Credentials and embedded attachment payloads are redacted.','']
    (ROOT/'traces/README.md').write_text('\n'.join(trace))
    fmt=ROOT/'traces/FORMAT.md';fmt.write_text(fmt.read_text().replace('every file in the eight released trace archives','every file in the released sanitized trace archives'))
    print(json.dumps({'projects':n,'trace_sources':sources,'recorded_events':total}))

if __name__=='__main__':main()
