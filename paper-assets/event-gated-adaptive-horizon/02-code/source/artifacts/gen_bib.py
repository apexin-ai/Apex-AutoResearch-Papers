#!/usr/bin/env python3
"""Generate references.bib from literature_map.yaml."""
import yaml
import re
import sys

MAP_PATH = '/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml'
BIB_PATH = '/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib'

with open(MAP_PATH) as f:
    raw = f.read()

entries = yaml.safe_load(raw)
if entries is None:
    print("ERROR: empty YAML")
    sys.exit(1)

VENUE_TO_BOOKTITLE = {
    'ICLR': 'International Conference on Learning Representations',
    'NeurIPS': 'Advances in Neural Information Processing Systems',
    'ICML': 'International Conference on Machine Learning',
    'CoRL': 'Conference on Robot Learning',
    'AAAI': 'AAAI Conference on Artificial Intelligence',
    'ICRA': 'IEEE International Conference on Robotics and Automation',
    'AISTATS': 'International Conference on Artificial Intelligence and Statistics',
    'UAI': 'Conference on Uncertainty in Artificial Intelligence',
    'JMLR': 'Journal of Machine Learning Research',
}

def format_authors(authors):
    if isinstance(authors, str):
        return authors
    formatted = []
    for a in authors:
        a = a.strip().rstrip('.')
        parts = a.split()
        if len(parts) >= 2:
            last = parts[0]
            first = ' '.join(parts[1:])
            formatted.append(f"{last}, {first}")
        else:
            formatted.append(a)
    return ' and '.join(formatted)

CONFERENCE_PREFIXES = ['ICLR', 'NeurIPS', 'ICML', 'CoRL', 'AAAI', 'ICRA',
                       'AISTATS', 'UAI', 'IJCAI', 'RSS', 'ECCV', 'CVPR']

def classify_venue(venue):
    if not venue:
        return 'misc'
    v = venue.strip()
    for conf in CONFERENCE_PREFIXES:
        if v.startswith(conf) or v.startswith(f"{conf} "):
            return 'conference'
    journal_keywords = ['journal', 'transactions', 'artificial intelligence', 'JMLR',
                        'Nature', 'Science', 'IEEE T', 'TNNLS', 'Reinforcement Learning Journal']
    v_lower = v.lower()
    for kw in journal_keywords:
        if kw.lower() in v_lower:
            return 'journal'
    if 'arxiv' in v_lower:
        return 'arxiv'
    return 'conference'

def extract_conference(venue):
    for conf in CONFERENCE_PREFIXES:
        if venue.startswith(conf):
            return VENUE_TO_BOOKTITLE.get(conf, venue.split('(')[0].strip())
    return venue.split('(')[0].strip()

bib_entries = []
seen_keys = set()

for entry in entries:
    if not isinstance(entry, dict):
        continue
    key = entry.get('paper_id', '')
    if not key or key in seen_keys:
        continue
    seen_keys.add(key)

    title = entry.get('title', '')
    authors = entry.get('authors', [])
    year = entry.get('year', '')
    venue = entry.get('venue', '')

    author_str = format_authors(authors)

    arxiv_match = re.search(r'(\d{4}\.\d{4,5})', venue or '')
    arxiv_id = arxiv_match.group(1) if arxiv_match else ''
    vtype = classify_venue(venue)

    if vtype == 'conference':
        booktitle = extract_conference(venue)
        bib = f"@inproceedings{{{key},\n"
        bib += f"  title = {{{title}}},\n"
        bib += f"  author = {{{author_str}}},\n"
        bib += f"  year = {{{year}}},\n"
        bib += f"  booktitle = {{{booktitle}}},\n"
        if arxiv_id:
            bib += f"  eprint = {{{arxiv_id}}},\n"
            bib += f"  archivePrefix = {{arXiv}},\n"
        bib += "}\n"
    elif vtype == 'journal':
        journal_name = venue.split('(')[0].strip()
        bib = f"@article{{{key},\n"
        bib += f"  title = {{{title}}},\n"
        bib += f"  author = {{{author_str}}},\n"
        bib += f"  year = {{{year}}},\n"
        bib += f"  journal = {{{journal_name}}},\n"
        if arxiv_id:
            bib += f"  eprint = {{{arxiv_id}}},\n"
            bib += f"  archivePrefix = {{arXiv}},\n"
        bib += "}\n"
    else:  # arxiv-only
        bib = f"@article{{{key},\n"
        bib += f"  title = {{{title}}},\n"
        bib += f"  author = {{{author_str}}},\n"
        bib += f"  year = {{{year}}},\n"
        bib += f"  journal = {{arXiv preprint arXiv:{arxiv_id}}},\n"
        if arxiv_id:
            bib += f"  eprint = {{{arxiv_id}}},\n"
            bib += f"  archivePrefix = {{arXiv}},\n"
        bib += "}\n"

    bib_entries.append(bib)

with open(BIB_PATH, 'w') as f:
    f.write(f"% Auto-generated from literature_map.yaml\n")
    f.write(f"% {len(bib_entries)} entries\n\n")
    f.write('\n'.join(bib_entries))

print(f"Generated {len(bib_entries)} BibTeX entries → {BIB_PATH}")
