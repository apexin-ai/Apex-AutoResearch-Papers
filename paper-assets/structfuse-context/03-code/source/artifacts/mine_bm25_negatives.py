#!/usr/bin/env python3
"""Mine BM25 hard negatives for contrastive training data.

Reads existing training data (for instance ordering / train-val split),
then re-mines negatives using BM25 scoring on the full candidate pool
(all non-positive .py files in the same repo).

Input:
  - Existing training data: {DATA_DIR}/train_random_s{seed}.jsonl  (for record ordering)
  - Extraction JSONs: {EXTRACTION_DIR}/*.json  (for buggy_file + connectivity)
  - Repo source code: {REPOS_DIR}/{repo_name}/

Output:
  - {DATA_DIR}/train_bm25_s{seed}.jsonl   (BM25 hard negatives)
  - {DATA_DIR}/val_bm25_s{seed}.jsonl     (copied from val_random, same as other strategies)
"""

import json
import os
import re
import shutil
import sys
import time
from collections import defaultdict
from pathlib import Path

from rank_bm25 import BM25Okapi

MAX_FILE_CHARS = 4096
POOL_SIZE = 50
EXTRACTION_DIR = "/root/autodl-tmp/structfuse/full_m1_data"
REPOS_DIR = "/root/autodl-tmp/structfuse/full_m1_data/repos"
DATA_DIR = "/root/autodl-tmp/structfuse/full_m2_training_data"
SEEDS = [42, 43, 44]


def tokenize_code(text: str) -> list[str]:
    """Code-aware tokenization: split camelCase, snake_case, punctuation."""
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    text = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', text)
    tokens = re.split(r'[^a-zA-Z0-9]+', text)
    return [t.lower() for t in tokens if len(t) > 1]


def collect_py_files(repo_path: str) -> dict[str, str]:
    files = {}
    for root, dirs, filenames in os.walk(repo_path):
        dirs[:] = [d for d in dirs if not d.startswith(".")
                   and d != "__pycache__" and d != "node_modules" and d != ".git"]
        for fname in filenames:
            if fname.endswith(".py"):
                full = os.path.join(root, fname)
                rel = os.path.relpath(full, repo_path)
                try:
                    with open(full, encoding="utf-8", errors="replace") as f:
                        content = f.read()
                    files[rel] = content[:MAX_FILE_CHARS]
                except OSError:
                    pass
    return files


def resolve_file(target: str, all_files: list[str]) -> str | None:
    if target in all_files:
        return target
    for f in all_files:
        if f.endswith("/" + target) or target.endswith("/" + f):
            return f
    basename = os.path.basename(target)
    candidates = [f for f in all_files if os.path.basename(f) == basename]
    if len(candidates) == 1:
        return candidates[0]
    return None


def get_positive_files(extraction: dict, buggy_file: str, all_py: list[str]) -> set[str]:
    """Derive positive files from extraction (same logic as build_m1_training_data.py)."""
    positive_files = set()

    for path in extraction.get("dataflow_paths", []):
        sf = path.get("source_file", "")
        skf = path.get("sink_file", "")
        if sf != skf:
            rsf = resolve_file(sf, all_py)
            rskf = resolve_file(skf, all_py)
            if rsf and rskf:
                if rsf == buggy_file and rskf != buggy_file:
                    positive_files.add(rskf)
                elif rskf == buggy_file and rsf != buggy_file:
                    positive_files.add(rsf)

    if not positive_files:
        for entry in extraction.get("call_graph", []):
            fp = entry.get("file_path", "")
            rfp = resolve_file(fp, all_py)
            if rfp and rfp != buggy_file and entry.get("hop_distance", 99) <= 1:
                positive_files.add(rfp)

    return positive_files


def mine_bm25_pool(query_content: str, non_pos_files: list[str],
                    source_files: dict[str, str], pool_size: int = 50):
    """BM25-rank non-positive files and return top-k."""
    if not non_pos_files:
        return [], {}

    docs = [source_files.get(f, "") for f in non_pos_files]
    tokenized_docs = [tokenize_code(d) for d in docs]
    query_tokens = tokenize_code(query_content)

    if not query_tokens or all(len(d) == 0 for d in tokenized_docs):
        selected = non_pos_files[:pool_size]
        return selected, {f: 0.0 for f in selected}

    bm25 = BM25Okapi(tokenized_docs)
    scores = bm25.get_scores(query_tokens)

    scored = sorted(zip(non_pos_files, scores), key=lambda x: -x[1])
    selected = [f for f, _ in scored[:pool_size]]
    score_dict = {f: float(s) for f, s in scored[:pool_size]}

    return selected, score_dict


def main():
    t_start = time.time()

    # First pass: collect all instance IDs from training data
    print("Collecting instance IDs from training data...")
    all_iids = set()
    for seed in SEEDS:
        for split in ["train", "val"]:
            ref_file = f"{DATA_DIR}/{split}_random_s{seed}.jsonl"
            with open(ref_file) as fh:
                for line in fh:
                    d = json.loads(line)
                    iid = d["query_id"].split("::")[0]
                    all_iids.add(iid)
    print(f"  {len(all_iids)} unique instance IDs")

    # Load only needed extractions (direct path lookup, not glob)
    print("Loading extractions...")
    ext_map = {}
    n_missing = 0
    for iid in sorted(all_iids):
        fpath = os.path.join(EXTRACTION_DIR, f"{iid}.json")
        if not os.path.exists(fpath):
            n_missing += 1
            continue
        with open(fpath) as fh:
            ext = json.load(fh)
        if ext.get("error") is not None:
            continue
        ext_map[ext["instance_id"]] = ext
    print(f"  {len(ext_map)} valid extractions loaded, {n_missing} not found")

    all_bm25_scores = []

    for seed in SEEDS:
        print(f"\n{'='*60}")
        print(f"Seed {seed}")
        print(f"{'='*60}")

        # Copy val file (identical across strategies)
        val_src = f"{DATA_DIR}/val_random_s{seed}.jsonl"
        val_dst = f"{DATA_DIR}/val_bm25_s{seed}.jsonl"
        shutil.copy2(val_src, val_dst)
        print(f"Val: copied {val_src} -> {val_dst}")

        # Process train
        ref_file = f"{DATA_DIR}/train_random_s{seed}.jsonl"
        print(f"\nReading reference: {ref_file}")

        records = []
        with open(ref_file) as fh:
            for line in fh:
                records.append(json.loads(line))
        print(f"  {len(records)} records")

        # Group by instance_id
        instance_records = defaultdict(list)
        for i, r in enumerate(records):
            iid = r["query_id"].split("::")[0]
            instance_records[iid].append(i)
        print(f"  {len(instance_records)} unique instances")

        repo_cache = {}
        instance_bm25_cache = {}
        n_done = 0
        n_fallback = 0

        for iid, record_indices in instance_records.items():
            repo_name = iid.rsplit(".", 2)[0]

            if repo_name not in repo_cache:
                repo_path = os.path.join(REPOS_DIR, repo_name)
                if os.path.isdir(repo_path):
                    repo_cache[repo_name] = collect_py_files(repo_path)
                else:
                    repo_cache[repo_name] = {}

            source_files = repo_cache[repo_name]

            ext = ext_map.get(iid)
            if not source_files or ext is None:
                r0 = records[record_indices[0]]
                instance_bm25_cache[iid] = (r0["neg_candidates"], r0["candidate_tokens"], [])
                n_fallback += 1
                n_done += 1
                continue

            all_py = sorted(source_files.keys())
            buggy_file = ext["buggy_file"]
            resolved = resolve_file(buggy_file, all_py)

            if resolved is None or resolved not in source_files:
                r0 = records[record_indices[0]]
                instance_bm25_cache[iid] = (r0["neg_candidates"], r0["candidate_tokens"], [])
                n_fallback += 1
                n_done += 1
                continue

            buggy_file = resolved
            positive_files = get_positive_files(ext, buggy_file, all_py)
            positive_files = {f for f in positive_files if f in source_files}

            non_pos = [f for f in all_py if f != buggy_file and f not in positive_files]

            selected, scores = mine_bm25_pool(
                source_files[buggy_file], non_pos, source_files, POOL_SIZE
            )

            neg_ids = [iid + "::" + f for f in selected]
            cand_tokens = {iid + "::" + f: source_files.get(f, "") for f in selected}

            instance_bm25_cache[iid] = (neg_ids, cand_tokens, list(scores.values()))
            all_bm25_scores.extend(scores.values())

            n_done += 1
            if n_done % 500 == 0:
                elapsed = time.time() - t_start
                print(f"  [{elapsed:.0f}s] Processed {n_done}/{len(instance_records)} instances...")

        print(f"  BM25 mined: {n_done - n_fallback}, fallback: {n_fallback}")

        # Rebuild records
        output_records = []
        for r in records:
            iid = r["query_id"].split("::")[0]
            neg_candidates, candidate_tokens, _ = instance_bm25_cache[iid]
            output_records.append({
                "query_id": r["query_id"],
                "query_tokens": r["query_tokens"],
                "pos_id": r["pos_id"],
                "pos_tokens": r["pos_tokens"],
                "pos_dataflow_distance": r["pos_dataflow_distance"],
                "neg_candidates": neg_candidates,
                "candidate_tokens": candidate_tokens,
            })

        out_file = f"{DATA_DIR}/train_bm25_s{seed}.jsonl"
        with open(out_file, "w") as fh:
            for r in output_records:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")

        sz = os.path.getsize(out_file) / 1024 / 1024
        print(f"  Output: {out_file} ({len(output_records)} records, {sz:.1f}MB)")

    # Score statistics
    if all_bm25_scores:
        import numpy as np
        scores = np.array(all_bm25_scores)
        print(f"\n{'='*60}")
        print(f"BM25 Score Statistics (across all seeds, top-{POOL_SIZE} negatives)")
        print(f"  count: {len(scores)}")
        print(f"  mean:  {scores.mean():.4f}")
        print(f"  std:   {scores.std():.4f}")
        print(f"  min:   {scores.min():.4f}")
        print(f"  25%:   {np.percentile(scores, 25):.4f}")
        print(f"  50%:   {np.percentile(scores, 50):.4f}")
        print(f"  75%:   {np.percentile(scores, 75):.4f}")
        print(f"  max:   {scores.max():.4f}")

    print(f"\nTotal time: {time.time() - t_start:.1f}s")
    print("Done!")


if __name__ == "__main__":
    main()
