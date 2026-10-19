#!/usr/bin/env python3
"""Add concrete source-file examples to the paper and category reading guides."""
import csv,json
from pathlib import Path
from urllib.parse import quote
ROOT=Path(__file__).resolve().parents[1]
LABELS={
 '01-manuscript':('Manuscript assets','Paper PDFs, LaTeX source, references, figures, and archived versions.'),
 '02-contributions':('Contribution records','Recorded agent roles, task instructions, and project context.'),
 '03-code':('Research code and configurations','Research scripts, implementation files, analysis code, configurations, and dependency manifests.'),
 '04-experiments':('Experiment and supporting data','Datasets, measured results, analysis outputs, and supporting workflow records. Original paths identify the purpose of each file.'),
 '06-validation':('Internal validation records','Project review reports, audits, checks, and verification artifacts.'),
 '07-maintenance':('Project documentation','Roadmaps, research plans, provenance, checklists, licenses, and maintenance notes.'),
 '08-index':('Provenance and file indexes','Mappings between original archive members and released files, byte counts, source checksums, exclusions, and manuscript version candidates.'),
}

def examples(rows,category):
 subset=[r for r in rows if r['category']==category and r['output_path']]
 def score(row):
  path=row['archive_path'].lower();ext=Path(path).suffix
  if category=='03-code':return (ext not in {'.py','.sh','.ipynb','.jl','.r'},not path.startswith(('scripts/','src/','code/','experiments/')),len(path))
  if category=='04-experiments':return (not path.startswith(('results/','data/','artifacts/')),ext not in {'.csv','.tsv','.json','.npz','.parquet'},len(path))
  if category=='01-manuscript':return (not path.endswith(('main.tex','main.pdf','references.bib')),len(path))
  if category=='07-maintenance':return (Path(path).name not in {'roadmap.md','readme.md','paper_provenance.yaml','license'},len(path))
  return (ext not in {'.md','.json','.txt'},len(path))
 seen=set();selected=[]
 for row in sorted(subset,key=score):
  key=row['output_path']
  if key in seen:continue
  seen.add(key);selected.append(row)
  if len(selected)==4:break
 return selected

def main():
 roots=list((ROOT/'paper-assets').glob('*/08-index/asset-manifest.json'))+list((ROOT/'research-snapshots').glob('*/*/08-index/asset-manifest.json'))
 for manifest in roots:
  project=manifest.parents[1];info=json.loads(manifest.read_text())
  rows=list(csv.DictReader((project/'08-index/asset-manifest.csv').open(encoding='utf-8-sig')))
  table=['## Concrete file examples','','| Content | Examples from this snapshot |','|---|---|']
  for category,(label,description) in LABELS.items():
   folder=project/category;folder.mkdir(exist_ok=True)
   chosen=examples(rows,category)
   guide=[f'# {label}','',description,'','[Back to project guide](../README.md)','']
   links=[]
   if category=='01-manuscript' and info.get('paper_pdf'):
    guide+=['[Read the selected manuscript](paper.pdf) · [Version index](../08-index/version-index.csv)',''];links.append('[Selected paper PDF](01-manuscript/paper.pdf)')
   if category=='08-index':
    guide+=['- [Asset manifest (CSV)](asset-manifest.csv): original and released paths, sizes, and checksums.','- [Snapshot summary (JSON)](asset-manifest.json): source archive, counts, manuscript title, and scope.','- [Exclusion manifest](excluded-files.csv): dependency installations, caches, account files, and other omitted entries.','- [Version index](version-index.csv): archived PDF candidates and their source paths.',''];links=['[Source/file manifest](08-index/asset-manifest.csv)','[Snapshot metadata](08-index/asset-manifest.json)']
   elif chosen:
    guide+=['## Example files','']
    for row in chosen:
     path=row['output_path'];path=path+'.parts/README.md' if row.get('storage')=='split-parts' else path
     inside=Path(path).relative_to(category).as_posix()
     guide.append(f'- [{row["archive_path"]}]({quote(inside,safe="/")})')
     links.append(f'[{row["archive_path"]}]({quote(path,safe="/")})')
   else:guide+=['The source snapshot has no files assigned to this category.','']
   guide+=['','Use [the complete file manifest](../08-index/asset-manifest.csv) to inspect all files and their original archive paths.','']
   (folder/'README.md').write_text('\n'.join(guide))
   table.append('| '+label+' | '+(' · '.join(links[:3]) if links else 'No matching files in this snapshot')+' |')
  table.append('| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |')
  runtime=sum(r['archive_path'].startswith('logs/') and r['category']!='05-generation-trace' for r in rows)
  scans=sum(r['archive_path'].startswith('scan_reports/') for r in rows)
  table+=['',f'Supporting files include {runtime:,} runtime bookkeeping files and {scans:,} automated scan reports. These record the system workflow alongside the experiment assets.','']
  readme=project/'README.md';text=readme.read_text();text=text.split('\n## Concrete file examples\n')[0].rstrip()+'\n\n'+'\n'.join(table)
  readme.write_text(text)
 print(f'Added concrete file examples and category guides to {len(roots)} project snapshots.')

if __name__=='__main__':main()
