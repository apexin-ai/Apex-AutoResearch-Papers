#!/usr/bin/env python3
"""Rebuild collection indexes from small per-project manifests in a sparse checkout."""
import csv, html, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def main():
    manifests=[json.loads(p.read_text()) for p in sorted((ROOT/'paper-assets').glob('*/08-index/asset-manifest.json'))]
    manifests.sort(key=lambda m:(not bool(m.get('paper_pdf')),m['project']))
    n=len(manifests);papers=sum(bool(m.get('paper_pdf')) for m in manifests)
    collection=json.loads((ROOT/'traces/projects.json').read_text())
    stats={p['project']:p['statistics'] for p in collection['projects']}
    root_readme=(ROOT/'README.md').read_text()
    import re
    root_readme=re.sub(r'The repository currently contains [^.]*\.',f'The repository currently contains {papers} projects with manuscript PDFs and {n-papers} additional project records with supporting assets.',root_readme)
    root_readme=re.sub(r'interactive \d+-item asset matrix','interactive project asset matrix',root_readme)
    (ROOT/'README.md').write_text(root_readme)
    content=['# Contents','',f'This catalogue covers **{papers} projects with manuscript PDFs** and **{n-papers} additional project records**. Records without a PDF are listed after the manuscript projects. Open a project README for its available manuscript, research code, experiment outputs, and recorded research process.','', '| Project | Manuscript | Code/config files | Data/result files | Trace sources | Recorded events |','|---|---|---:|---:|---:|---:|']
    cards=[];matrix=[]
    for m in manifests:
        p=m['project'];s=stats.get(p,{})
        pdf=f'[PDF](paper-assets/{p}/01-manuscript/paper.pdf)' if m.get('paper_pdf') else 'No PDF in snapshot'
        content.append(f"| [{p}](paper-assets/{p}/README.md) | {pdf} | {m['code_count']:,} | {m['data_count']:,} | {s.get('files',m.get('trace_count',0)):,} | {s.get('messages',0):,} |")
        evidence=''.join('<tr><th>'+html.escape(r['name'])+'</th><td>'+html.escape(r['status'])+'</td><td>'+html.escape(r['evidence'])+'</td><td>'+html.escape(r['gap'])+'</td></tr>' for r in m['criteria'])
        for r in m['criteria']:matrix.append([p,m['title'],r['name'],r['status'],r['evidence'],r['gap'],p+'/'+r['path']])
        links=f'<a href="{p}/README.md">Asset guide</a><a href="{p}/03-code/source/">Research code</a><a href="{p}/05-generation-trace/readable/README.md">Read conversations</a>'
        for snapshot in sorted((ROOT/'research-snapshots'/p).glob('*/08-index/asset-manifest.json')):
            date=snapshot.parents[1].name;links+=f'<a href="../research-snapshots/{p}/{date}/README.md">{date} snapshot</a>'
        if m.get('paper_pdf'):links=f'<a href="{p}/01-manuscript/paper.pdf">Paper PDF</a>'+links
        cards.append(f'<article data-search="{html.escape((p+" "+m["title"]).lower(),quote=True)}"><small>{html.escape(p)}</small><h2>{html.escape(m["title"])}</h2><p>{m["code_count"]:,} code/configuration files · {m["data_count"]:,} data/result files · {s.get("files",m.get("trace_count",0)):,} trace sources</p><nav>{links}</nav><details><summary>Asset evidence and verification limits</summary><div class="table"><table><thead><tr><th>Requirement</th><th>Status</th><th>Evidence</th><th>Limit</th></tr></thead><tbody>{evidence}</tbody></table></div></details></article>')
    content+=['','[Interactive asset catalogue](paper-assets/index.html) · [Full asset matrix](paper-assets/asset-matrix.csv) · [Readable trace guides](traces/README.md)','', 'Counts describe archived files and recorded events, including overlapping snapshots. Code presence does not establish reproduction. Internal reviews and manuscript labels do not establish external acceptance. Source documents preserve their original language.','']
    (ROOT/'CONTENTS.md').write_text('\n'.join(content))
    with (ROOT/'paper-assets/asset-matrix.csv').open('w',newline='') as f:
        w=csv.writer(f,lineterminator="\n");w.writerow(['Paper project','Paper title','Category','Status','Organized assets','Open questions / gaps','Asset directory']);w.writerows(matrix)
    page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Research assets</title><style>
    *{box-sizing:border-box}body{margin:0;background:#f4f6f5;color:#163134;font:15px/1.6 system-ui,sans-serif}header{background:#153e42;color:#fff;padding:48px max(24px,calc((100% - 1160px)/2))}header p{color:#c5dad8;max-width:780px}h1{font-size:38px;line-height:1.15}main{max-width:1208px;margin:auto;padding:24px}input{width:100%;padding:14px 18px;border:1px solid #b9ceca;border-radius:8px;font:inherit;margin:8px 0 24px}article{background:white;border:1px solid #d4dfdc;padding:24px;margin-bottom:18px;border-radius:10px}small{font:12px ui-monospace,monospace;color:#54706b}h2{margin:8px 0;font-size:22px;line-height:1.35}article p{color:#54706b}nav{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0}a{color:#116b60}nav a{border:1px solid #cbdad6;padding:7px 12px;border-radius:5px;text-decoration:none}nav a:first-child{background:#146459;color:white}summary{cursor:pointer;font-weight:600}.table{overflow:auto}table{border-collapse:collapse;font-size:12px;min-width:800px;margin-top:14px}th,td{border-bottom:1px solid #d8e1df;padding:10px;text-align:left;vertical-align:top}td{min-width:100px}td:nth-child(3),td:nth-child(4){min-width:220px}.notice{padding:14px 18px;border-left:4px solid #a67c36;background:#fff9ec;margin-bottom:24px}[hidden]{display:none}footer{padding:20px;color:#54706b} @media(max-width:600px){h1{font-size:29px}h2{font-size:19px}article{padding:18px}main{padding:16px}}
    </style><header><small style="color:#b7d8d2">AUTOMATED RESEARCH / REVIEWABLE EVIDENCE</small><h1>Research assets</h1><p>Manuscripts, code, experiment results, and readable research conversations. PAPER_COUNT projects include manuscript PDFs; OTHER_COUNT additional records preserve supporting project material.</p></header><main><div class="notice">Project files document generated research and its workflow. Experimental reproduction, author identity, submission, and external acceptance are not established by these files alone.</div><label for="search">Find a project or paper</label><input id="search" placeholder="Search titles or project names…" type="search"><p id="count">COUNT projects</p>CARDS<footer>Generated guides are English; original evidence retains its recorded language. <a href="asset-matrix.csv">Download asset matrix</a> · <a href="../traces/README.md">Trace catalogue</a></footer></main><script>const cards=[...document.querySelectorAll('article')];document.querySelector('#search').addEventListener('input',e=>{const q=e.target.value.toLowerCase().trim();for(const c of cards)c.hidden=!c.dataset.search.includes(q);document.querySelector('#count').textContent=cards.filter(c=>!c.hidden).length+' projects';});</script></html>'''.replace('PAPER_COUNT',str(papers)).replace('OTHER_COUNT',str(n-papers)).replace('COUNT',str(n)).replace('CARDS',''.join(cards))
    (ROOT/'paper-assets/index.html').write_text(page)
    trace=['# Research Trace Atlas','',f'Browse recorded tasks, user-role instructions, assistant responses, tool calls, and tool results from **{len(stats)} trace collections**. Open **Readable Markdown** in any project guide for a GitHub reading view, or select the adjacent JSON link for the complete structured record.','', '[Offline preview](demo.html) · [Interactive browser](index.html) · [Format and provenance](FORMAT.md)','','For the complete browser, run `python3 scripts/serve_traces.py --open` from a downloaded repository. The offline preview embeds one actual bounded round per project when a matching round exists.','','| Project | Conversations | Worker logs | Results | Context notes | Events | Readable Markdown |','|---|---:|---:|---:|---:|---:|---|']
    for p in collection['projects']:
        s=p['statistics'];slug=p['project'];base=str(Path(p['catalog']).parent);trace.append(f"| [{slug}]({base}/README.md) | {s.get('conversation',0):,} | {s.get('worker',0):,} | {s.get('result',0):,} | {s.get('history',0):,} | {s.get('messages',0):,} | [Read]({base}/readable/README.md) |")
    total=sum(s.get('messages',0) for s in stats.values());sources=sum(s.get('files',0) for s in stats.values())
    trace+=['',f'**{sources:,} source records · {total:,} recorded messages/events.** Counts include overlapping snapshots and parallel logs; they are not deduplicated research actions.','','Source language and order are retained. A user-role message can originate from another agent or system and does not identify a human author. Missing prompts and timestamps are not reconstructed. Credentials and embedded attachment payloads are redacted.','']
    (ROOT/'traces/README.md').write_text('\n'.join(trace))
    fmt=ROOT/'traces/FORMAT.md';fmt.write_text(fmt.read_text().replace('every file in the eight released trace archives','every file in the released sanitized trace archives'))
    notes=ROOT/'RELEASE_NOTES.md'
    text=notes.read_text()
    text=re.sub(r'This release contains .*?projects collected from (?:the local `workspace\.tar\.gz` archives|project backup snapshots)\.',f'This release contains {n} research projects collected from project backup snapshots.',text)
    text=text.replace('all members of the eight trace archives','all members of the released trace archives').replace("The only archive above GitHub's 100 MB per-file limit was split into 80 MiB parts at `paper-assets/importance_margin_vla_compress/05-generation-trace/trace-files.tar.gz.parts/`.","Files above GitHub's size limit are split into 80 MiB parts with checksum manifests.")
    notes.write_text(text)
    snapshots=sorted((ROOT/'research-snapshots').glob('*/*/08-index/asset-manifest.json'))
    if snapshots:
        lines=['# Additional research snapshots','','These snapshots preserve later project exports alongside the initial workspace releases. A snapshot is a dated source collection, not an additional distinct paper.','','| Project | Snapshot | Manuscript | Assets and conversations |','|---|---|---|---|']
        for path in snapshots:
            m=json.loads(path.read_text());base=path.parents[1];slug=base.parent.name;date=base.name;relative=base.relative_to(ROOT/'research-snapshots')
            pdf=f'[PDF]({relative}/01-manuscript/paper.pdf)' if m.get('paper_pdf') else 'No PDF in snapshot'
            lines.append(f'| {slug} | {date} | {pdf} | [Assets]({relative}/README.md) · [Conversations]({relative}/05-generation-trace/readable/README.md) |')
        (ROOT/'research-snapshots/README.md').write_text('\n'.join(lines)+'\n')
        with (ROOT/'CONTENTS.md').open('a') as f:f.write('\n[Additional dated research snapshots](research-snapshots/README.md) retain later exports and conversations alongside the initial releases.\n')
    supplements=sorted((ROOT/'supplementary').glob('*/manifest.json'))
    if supplements:
        lines=['# Supplementary research materials','','Benchmark code, experiment records, revisions, and rebuttals. These collections are not automatically counted as distinct generated papers.','']
        for path in supplements:
            m=json.loads(path.read_text());slug=path.parent.name;lines.append(f'- [{slug}]({slug}/README.md): {m["included_files"]:,} included source objects.')
        (ROOT/'supplementary/README.md').write_text('\n'.join(lines)+'\n')
        with (ROOT/'CONTENTS.md').open('a') as f:f.write('\n[Supplementary research materials](supplementary/README.md) include benchmark code, results, revisions, and rebuttals.\n')
    print(json.dumps({'projects':n,'trace_sources':sources,'recorded_events':total}))

if __name__=='__main__':main()
