#!/usr/bin/env python3
"""
Prepare VAST (K=3, stance) + CivilComments (K=2, toxicity) test data for
plan011 frontier-model annotation.

VAST: try HF QCRI/VAST first; fall back to GitHub raw vast_test.csv if needed.
      Output JSONL fields: {idx, text, topic, label, label_name, split}
      Classes (in canonical order matching VAST paper): ["Con", "Pro", "Neutral"]
      Sample size: 1000 (random seed 42, deduplicated by (text, topic)).

CivilComments: load via HF google/civil_comments, test split.
      toxicity >= 0.5 -> "toxic", else "non-toxic".
      Balanced sample: 500 toxic + 500 non-toxic.
"""
import csv
import io
import json
import os
import sys
from pathlib import Path

import numpy as np

OUT_DIR = Path("/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_annotations/data")

VAST_LABEL_MAP = {0: "Con", 1: "Pro", 2: "Neutral"}
VAST_CLASSES = ["Con", "Pro", "Neutral"]

CC_LABEL_MAP = {0: "non-toxic", 1: "toxic"}
CC_CLASSES = ["non-toxic", "toxic"]


def write_jsonl(records, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"  Wrote {len(records)} records to {path}")


def prepare_vast(sample_size=1000, seed=42):
    print("=" * 60)
    print("VAST")
    print("=" * 60)

    rows = None
    # Try HuggingFace first
    try:
        from datasets import load_dataset
        for name in ("QCRI/VAST", "Yueh-Huan/VAST"):
            try:
                ds = load_dataset(name, split="test")
                rows = []
                for r in ds:
                    rows.append({
                        "text": r.get("post") or r.get("text") or r.get("text_s"),
                        "topic": r.get("topic_str") or r.get("topic"),
                        "label": int(r["label"]),
                    })
                print(f"  Loaded {len(rows)} rows from HF {name}")
                break
            except Exception as e:
                print(f"  HF load_dataset({name}) failed: {type(e).__name__}: {e}")
                continue
    except ImportError:
        print("  datasets package not available")

    if rows is None:
        # Fallback: download vast_test.csv from GitHub
        import requests
        urls = [
            "https://raw.githubusercontent.com/emilyallaway/zero-shot-stance/master/data/VAST/vast_test.csv",
            "https://raw.githubusercontent.com/MalavikaSrikanth16/adversarial-learning-vast/main/data/VAST/vast_test.csv",
        ]
        csv_text = None
        for url in urls:
            try:
                resp = requests.get(url, timeout=60)
                if resp.status_code == 200 and "post" in resp.text[:1000]:
                    csv_text = resp.text
                    print(f"  Downloaded {len(csv_text)} chars from {url}")
                    break
            except Exception as e:
                print(f"  GET {url} failed: {e}")
        if csv_text is None:
            raise RuntimeError("Could not load VAST test data from any source")
        reader = csv.DictReader(io.StringIO(csv_text))
        rows = []
        for r in reader:
            rows.append({
                "text": r.get("post") or r.get("text_s"),
                "topic": r.get("topic_str") or r.get("topic"),
                "label": int(r["label"]),
            })
        print(f"  Parsed {len(rows)} rows from CSV")

    # Filter valid rows, dedupe by (text, topic, label)
    seen = set()
    cleaned = []
    for r in rows:
        if not r["text"] or r["label"] not in VAST_LABEL_MAP:
            continue
        key = (r["text"].strip(), (r["topic"] or "").strip(), r["label"])
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(r)
    print(f"  After dedup: {len(cleaned)} rows")

    # Sample
    if sample_size and len(cleaned) > sample_size:
        rng = np.random.default_rng(seed)
        idx = rng.choice(len(cleaned), size=sample_size, replace=False)
        idx.sort()
        cleaned = [cleaned[i] for i in idx]

    # Build records
    records = []
    for i, r in enumerate(cleaned):
        records.append({
            "idx": i,
            "text": r["text"],
            "topic": r["topic"] or "",
            "label": r["label"],
            "label_name": VAST_LABEL_MAP[r["label"]],
            "split": "test",
        })

    from collections import Counter
    dist = Counter(r["label_name"] for r in records)
    print(f"  Class distribution: {dict(sorted(dist.items()))}")

    write_jsonl(records, OUT_DIR / "vast" / "test.jsonl")


def prepare_civil_comments(sample_size=1000, seed=42):
    print("\n" + "=" * 60)
    print("CivilComments")
    print("=" * 60)

    from datasets import load_dataset
    ds = load_dataset("google/civil_comments", split="test")
    print(f"  Loaded {len(ds)} rows from HF google/civil_comments[test]")

    toxic_pool = []
    nontoxic_pool = []
    for i, row in enumerate(ds):
        lid = 1 if row["toxicity"] >= 0.5 else 0
        text = row["text"]
        if not text or not text.strip():
            continue
        rec = {
            "text": text,
            "label": lid,
            "label_name": CC_LABEL_MAP[lid],
        }
        if lid == 1:
            toxic_pool.append(rec)
        else:
            nontoxic_pool.append(rec)
    print(f"  Pools: toxic={len(toxic_pool)} non-toxic={len(nontoxic_pool)}")

    # Balanced sample
    n_per_class = sample_size // 2
    rng = np.random.default_rng(seed)

    def _sample(pool, n):
        idx = rng.choice(len(pool), size=min(n, len(pool)), replace=False)
        idx.sort()
        return [pool[i] for i in idx]

    sampled = _sample(toxic_pool, n_per_class) + _sample(nontoxic_pool, n_per_class)
    # Shuffle the combined list
    perm = rng.permutation(len(sampled))
    sampled = [sampled[i] for i in perm]

    records = []
    for i, r in enumerate(sampled):
        records.append({
            "idx": i,
            "text": r["text"],
            "label": r["label"],
            "label_name": r["label_name"],
            "split": "test",
        })

    from collections import Counter
    dist = Counter(r["label_name"] for r in records)
    print(f"  Sampled: {len(records)} | Class distribution: {dict(sorted(dist.items()))}")

    write_jsonl(records, OUT_DIR / "civil_comments" / "test.jsonl")


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    prepare_vast()
    prepare_civil_comments()
    print("\nDone.")
