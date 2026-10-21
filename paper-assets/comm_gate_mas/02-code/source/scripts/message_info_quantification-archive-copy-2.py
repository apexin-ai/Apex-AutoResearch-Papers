#!/usr/bin/env python3
"""Quantify information content per function type across backbones/topologies."""

import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

PROJECT = Path("/Users/agent-001/.agent-ml-research/projects/comm_gate_mas")
FULL_SCALE = PROJECT / "outputs" / "full_scale"
OUTPUT_PATH = PROJECT / "outputs" / "message_info_quantification.json"

FUNCTION_TYPES = [
    "acknowledgment", "verification", "information_provision",
    "reasoning_guidance", "coordination"
]

CONFIGS = [
    ("qwen", "round_robin"),
    ("llama", "round_robin"),
    ("gemma", "round_robin"),
]
TOPOLOGIES = ["round_robin"]


def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())


def bigrams(tokens):
    return set(zip(tokens, tokens[1:]))


def trigrams(tokens):
    return set(zip(tokens, tokens[1:], tokens[2:]))


def ngram_overlap(tokens_curr, tokens_prev, n=2):
    if n == 2:
        curr, prev = bigrams(tokens_curr), bigrams(tokens_prev)
    else:
        curr, prev = trigrams(tokens_curr), trigrams(tokens_prev)
    if not curr:
        return 0.0
    return len(curr & prev) / len(curr)


def type_token_ratio(tokens):
    if not tokens:
        return 0.0
    return len(set(tokens)) / len(tokens)


def load_traces(directory):
    """Load traces, return dict: task_id -> list of messages."""
    trace_file = directory / "traces" / "traces.jsonl"
    traces = {}
    with open(trace_file) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
                traces[entry["task_id"]] = entry["messages"]
            except json.JSONDecodeError:
                continue
    return traces


def load_annotations(directory):
    """Load annotations, return dict: (task_id, message_index) -> function_type."""
    ann_file = directory / "annotations" / "annotations.jsonl"
    annotations = {}
    with open(ann_file) as f:
        for line in f:
            entry = json.loads(line)
            tid = entry["task_id"]
            midx = entry["message_index"]
            if entry.get("agreement"):
                ftype = entry["annotation_a"]["type"]
            else:
                a_conf = entry["annotation_a"].get("confidence", 0)
                b_conf = entry["annotation_b"].get("confidence", 0)
                ftype = entry["annotation_a"]["type"] if a_conf >= b_conf else entry["annotation_b"]["type"]
            annotations[(tid, midx)] = ftype
    return annotations


def analyze_config(backbone, topology):
    directory = FULL_SCALE / f"{backbone}_{topology}"
    if not directory.exists():
        return None

    traces = load_traces(directory)
    annotations = load_annotations(directory)

    per_type = defaultdict(lambda: {
        "token_counts": [], "char_counts": [], "ttr": [],
        "bigram_overlap": [], "trigram_overlap": []
    })

    for (tid, midx), ftype in annotations.items():
        if ftype not in FUNCTION_TYPES:
            continue
        msgs = traces.get(tid)
        if not msgs or midx >= len(msgs):
            continue

        content = msgs[midx].get("content", "")
        if not content.strip():
            continue
        tokens = tokenize(content)
        if not tokens:
            continue

        per_type[ftype]["token_counts"].append(len(tokens))
        per_type[ftype]["char_counts"].append(len(content))
        per_type[ftype]["ttr"].append(type_token_ratio(tokens))

        if midx > 0:
            prev_content = msgs[midx - 1].get("content", "")
            prev_tokens = tokenize(prev_content)
            per_type[ftype]["bigram_overlap"].append(ngram_overlap(tokens, prev_tokens, 2))
            per_type[ftype]["trigram_overlap"].append(ngram_overlap(tokens, prev_tokens, 3))

    return per_type


def mean_std(vals):
    if not vals:
        return {"mean": None, "std": None, "n": 0}
    n = len(vals)
    m = sum(vals) / n
    if n > 1:
        s = (sum((x - m) ** 2 for x in vals) / (n - 1)) ** 0.5
    else:
        s = 0.0
    return {"mean": round(m, 4), "std": round(s, 4), "n": n}


def main():
    results = {}

    for backbone, topology in CONFIGS:
        key = f"{backbone}_{topology}"
        print(f"Processing {key}...")
        per_type = analyze_config(backbone, topology)
        if per_type is None:
            continue

        results[key] = {}
        for ftype in FUNCTION_TYPES:
            data = per_type.get(ftype)
            if not data:
                results[key][ftype] = {
                    "token_count": mean_std([]),
                    "char_count": mean_std([]),
                    "type_token_ratio": mean_std([]),
                    "bigram_overlap": mean_std([]),
                    "trigram_overlap": mean_std([]),
                }
                continue
            results[key][ftype] = {
                "token_count": mean_std(data["token_counts"]),
                "char_count": mean_std(data["char_counts"]),
                "type_token_ratio": mean_std(data["ttr"]),
                "bigram_overlap": mean_std(data["bigram_overlap"]),
                "trigram_overlap": mean_std(data["trigram_overlap"]),
            }

    # Aggregate per backbone (across topologies)
    backbone_agg = {}
    for backbone in ["qwen", "llama", "gemma"]:
        backbone_agg[backbone] = {}
        for ftype in FUNCTION_TYPES:
            merged = {"token_counts": [], "char_counts": [], "ttr": [],
                      "bigram_overlap": [], "trigram_overlap": []}
            for topology in TOPOLOGIES:
                key = f"{backbone}_{topology}"
                directory = FULL_SCALE / f"{key}"
                if not directory.exists():
                    continue
                per_type = analyze_config(backbone, topology)
                if per_type and ftype in per_type:
                    for metric in merged:
                        merged[metric].extend(per_type[ftype][metric])
            backbone_agg[backbone][ftype] = {
                "token_count": mean_std(merged["token_counts"]),
                "char_count": mean_std(merged["char_counts"]),
                "type_token_ratio": mean_std(merged["ttr"]),
                "bigram_overlap": mean_std(merged["bigram_overlap"]),
                "trigram_overlap": mean_std(merged["trigram_overlap"]),
            }

    # Grand aggregate (all backbones)
    grand = {}
    for ftype in FUNCTION_TYPES:
        merged = {"token_counts": [], "char_counts": [], "ttr": [],
                  "bigram_overlap": [], "trigram_overlap": []}
        for backbone in ["qwen", "llama", "gemma"]:
            for topology in TOPOLOGIES:
                key = f"{backbone}_{topology}"
                directory = FULL_SCALE / f"{key}"
                if not directory.exists():
                    continue
                per_type = analyze_config(backbone, topology)
                if per_type and ftype in per_type:
                    for metric in merged:
                        merged[metric].extend(per_type[ftype][metric])
        grand[ftype] = {
            "token_count": mean_std(merged["token_counts"]),
            "char_count": mean_std(merged["char_counts"]),
            "type_token_ratio": mean_std(merged["ttr"]),
            "bigram_overlap": mean_std(merged["bigram_overlap"]),
            "trigram_overlap": mean_std(merged["trigram_overlap"]),
        }

    output = {
        "per_config": results,
        "per_backbone": backbone_agg,
        "grand_aggregate": grand,
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    # Print summary table
    print("\n" + "=" * 90)
    print("GRAND AGGREGATE (all backbones, all topologies)")
    print("=" * 90)
    print(f"{'Type':<25} {'Tokens':>10} {'Chars':>10} {'TTR':>8} {'Bi-OL':>8} {'Tri-OL':>8} {'N':>6}")
    print("-" * 90)
    for ftype in FUNCTION_TYPES:
        d = grand[ftype]
        tc = d["token_count"]
        cc = d["char_count"]
        ttr = d["type_token_ratio"]
        bo = d["bigram_overlap"]
        to_ = d["trigram_overlap"]
        print(f"{ftype:<25} {tc['mean']:>10.1f} {cc['mean']:>10.1f} {ttr['mean']:>8.4f} "
              f"{bo['mean']:>8.4f} {to_['mean']:>8.4f} {tc['n']:>6}")

    print("\n" + "=" * 90)
    print("PER BACKBONE AGGREGATE")
    print("=" * 90)
    for backbone in ["qwen", "llama", "gemma"]:
        print(f"\n--- {backbone.upper()} ---")
        print(f"{'Type':<25} {'Tokens':>10} {'Chars':>10} {'TTR':>8} {'Bi-OL':>8} {'Tri-OL':>8} {'N':>6}")
        print("-" * 90)
        for ftype in FUNCTION_TYPES:
            d = backbone_agg[backbone][ftype]
            tc = d["token_count"]
            cc = d["char_count"]
            ttr = d["type_token_ratio"]
            bo = d["bigram_overlap"]
            to_ = d["trigram_overlap"]
            if tc["mean"] is None:
                print(f"{ftype:<25} {'N/A':>10} {'N/A':>10} {'N/A':>8} {'N/A':>8} {'N/A':>8} {0:>6}")
            else:
                print(f"{ftype:<25} {tc['mean']:>10.1f} {cc['mean']:>10.1f} {ttr['mean']:>8.4f} "
                      f"{bo['mean']:>8.4f} {to_['mean']:>8.4f} {tc['n']:>6}")

    print(f"\nResults saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
