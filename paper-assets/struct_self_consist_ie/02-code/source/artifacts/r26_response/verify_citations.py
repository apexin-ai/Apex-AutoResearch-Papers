#!/usr/bin/env python3
"""Batch verify bib entries against Semantic Scholar API."""

import json
import re
import time
import urllib.request
import urllib.parse
import urllib.error

BIB_PATH = "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"

def parse_bib(path):
    with open(path) as f:
        content = f.read()

    entries = {}
    pattern = re.compile(r'@\w+\{(\w+),\s*(.*?)\n\}', re.DOTALL)
    for m in pattern.finditer(content):
        key = m.group(1)
        body = m.group(2)
        entry = {"key": key}
        for field in ["title", "author", "year", "journal", "booktitle", "url", "doi"]:
            fp = re.search(rf'{field}\s*=\s*\{{(.*?)\}}', body, re.DOTALL)
            if fp:
                val = fp.group(1).strip()
                val = re.sub(r'\s+', ' ', val)
                val = val.replace('{', '').replace('}', '')
                entry[field] = val
        entries[key] = entry
    return entries

def query_s2(title, retries=2):
    clean = re.sub(r'[{}\\]', '', title)
    clean = re.sub(r'\s+', ' ', clean).strip()
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(clean)}&limit=3&fields=title,authors,year,venue,externalIds"
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "CitationVerifier/1.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 10 * (attempt + 1)
                print(f"  Rate limited, waiting {wait}s...")
                time.sleep(wait)
            else:
                print(f"  HTTP {e.code} for {title[:50]}")
                return None
        except Exception as e:
            print(f"  Error: {e}")
            if attempt < retries:
                time.sleep(5)
    return None

def normalize(s):
    return re.sub(r'[^a-z0-9 ]', '', s.lower()).strip()

def titles_match(t1, t2):
    n1, n2 = normalize(t1), normalize(t2)
    if n1 == n2:
        return True
    if n1 in n2 or n2 in n1:
        return True
    words1 = set(n1.split())
    words2 = set(n2.split())
    if len(words1) == 0 or len(words2) == 0:
        return False
    overlap = len(words1 & words2) / max(len(words1), len(words2))
    return overlap > 0.8

def verify_entry(key, entry, results):
    title = entry.get("title", "")
    if not title:
        results["not_found"].append(key)
        return

    data = query_s2(title)
    if not data or not data.get("data"):
        results["not_found"].append(key)
        results["details"][key] = {"status": "not_found", "reason": "no S2 results"}
        return

    bib_year = entry.get("year", "")
    bib_authors = entry.get("author", "")

    best_match = None
    for paper in data["data"]:
        if titles_match(title, paper.get("title", "")):
            best_match = paper
            break

    if not best_match:
        for paper in data["data"]:
            paper_title = paper.get("title", "")
            n1, n2 = normalize(title), normalize(paper_title)
            words1 = set(n1.split())
            words2 = set(n2.split())
            if len(words1) > 0 and len(words2) > 0:
                overlap = len(words1 & words2) / max(len(words1), len(words2))
                if overlap > 0.6:
                    best_match = paper
                    break

    if not best_match:
        results["not_found"].append(key)
        results["details"][key] = {
            "status": "not_found",
            "reason": "no title match in top 3",
            "s2_titles": [p.get("title", "") for p in data["data"]]
        }
        return

    issues = []
    s2_year = best_match.get("year")
    s2_authors = [a.get("name", "") for a in best_match.get("authors", [])]
    s2_title = best_match.get("title", "")

    if bib_year and s2_year and str(bib_year) != str(s2_year):
        issues.append(f"year: bib={bib_year} vs s2={s2_year}")

    if not titles_match(title, s2_title):
        issues.append(f"title mismatch")

    if issues:
        results["mismatch"].append(key)
        results["details"][key] = {
            "status": "mismatch",
            "issues": issues,
            "s2_title": s2_title,
            "s2_year": s2_year,
            "s2_authors": s2_authors
        }
    else:
        results["verified"].append(key)
        results["details"][key] = {
            "status": "verified",
            "s2_title": s2_title,
            "s2_year": s2_year,
            "s2_authors": s2_authors[:5]
        }

def main():
    entries = parse_bib(BIB_PATH)
    print(f"Parsed {len(entries)} bib entries")

    results = {
        "total_entries": len(entries),
        "verified": [],
        "not_found": [],
        "mismatch": [],
        "fabricated": [],
        "orphan_keys": [],
        "fixes_needed": [],
        "critical_alerts": [],
        "details": {}
    }

    for i, (key, entry) in enumerate(entries.items()):
        print(f"[{i+1}/{len(entries)}] Verifying {key}...")
        verify_entry(key, entry, results)
        time.sleep(3.2)

    print(f"\nResults: {len(results['verified'])} verified, {len(results['mismatch'])} mismatch, {len(results['not_found'])} not_found")

    out_path = "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r26_response/s2_raw_results.json"
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
