#!/usr/bin/env python3
"""Phase 5: Stratified sampling of 50 clauses for human validation.

Usage:
    python sample_validation.py

Reads: clauses.jsonl, annotations_claude.jsonl, annotations_gpt.jsonl
Writes: human_validation_sample.csv
"""

import csv
import json
import random
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent
CLAUSES_FILE = BASE_DIR / "clauses.jsonl"
CLAUDE_FILE = BASE_DIR / "annotations_claude.jsonl"
GPT_FILE = BASE_DIR / "annotations_gpt.jsonl"
OUT_CSV = BASE_DIR / "human_validation_sample.csv"

SAMPLE_SIZE = 50
SEED = 42

AMBIGUITY_TYPES = [
    "scopal", "lexical", "coreferential",
    "incompleteness", "authorization_scope", "conditional_precedence",
]


def load_jsonl(path):
    records = {}
    with open(path) as f:
        for line in f:
            rec = json.loads(line)
            records[rec["clause_id"]] = rec
    return records


def main():
    random.seed(SEED)

    clauses = load_jsonl(CLAUSES_FILE)
    claude_ann = load_jsonl(CLAUDE_FILE)
    gpt_ann = load_jsonl(GPT_FILE)

    common_ids = sorted(set(claude_ann.keys()) & set(gpt_ann.keys()))

    # Stratify: ambiguous (by either judge) vs non-ambiguous
    ambiguous_ids = []
    non_ambiguous_ids = []
    type_buckets = defaultdict(list)

    for cid in common_ids:
        c_amb = claude_ann[cid]["is_ambiguous"]
        g_amb = gpt_ann[cid]["is_ambiguous"]
        if c_amb or g_amb:
            ambiguous_ids.append(cid)
            if c_amb:
                type_buckets[claude_ann[cid]["ambiguity_type"]].append(cid)
            elif g_amb:
                type_buckets[gpt_ann[cid]["ambiguity_type"]].append(cid)
        else:
            non_ambiguous_ids.append(cid)

    n_amb = len(ambiguous_ids)
    n_non = len(non_ambiguous_ids)

    # Target: ~25 ambiguous, ~25 non-ambiguous (balanced)
    target_amb = min(25, n_amb)
    target_non = min(SAMPLE_SIZE - target_amb, n_non)

    # For ambiguous: sample proportionally by type, minimum 1 per type if available
    selected_amb = []
    types_with_data = [t for t in AMBIGUITY_TYPES if type_buckets[t]]
    if types_with_data:
        per_type = max(1, target_amb // len(types_with_data))
        remainder = target_amb - per_type * len(types_with_data)

        for t in types_with_data:
            pool = type_buckets[t]
            n_pick = min(per_type, len(pool))
            selected_amb.extend(random.sample(pool, n_pick))

        # Fill remainder from largest buckets
        remaining_pool = [cid for cid in ambiguous_ids if cid not in selected_amb]
        if remainder > 0 and remaining_pool:
            extra = min(remainder, len(remaining_pool))
            selected_amb.extend(random.sample(remaining_pool, extra))
    else:
        selected_amb = random.sample(ambiguous_ids, target_amb) if ambiguous_ids else []

    # Trim to target
    if len(selected_amb) > target_amb:
        selected_amb = random.sample(selected_amb, target_amb)

    # Sample non-ambiguous
    selected_non = random.sample(non_ambiguous_ids, target_non) if non_ambiguous_ids else []

    selected = selected_amb + selected_non
    random.shuffle(selected)

    # Write CSV
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "clause_id", "clause_text", "context", "doc_id", "company", "domain",
            "judge1_ambiguous", "judge1_type", "judge1_justification",
            "judge2_ambiguous", "judge2_type", "judge2_justification",
            "human_is_ambiguous", "human_ambiguity_type", "human_notes",
        ])
        for cid in selected:
            clause = clauses[cid]
            c = claude_ann.get(cid, {})
            g = gpt_ann.get(cid, {})
            writer.writerow([
                cid,
                clause["clause_text"],
                clause.get("context_sentence", ""),
                clause["doc_id"],
                clause["company"],
                clause["domain"],
                c.get("is_ambiguous", ""),
                c.get("ambiguity_type", ""),
                c.get("justification", ""),
                g.get("is_ambiguous", ""),
                g.get("ambiguity_type", ""),
                g.get("justification", ""),
                "",  # human_is_ambiguous (to be filled)
                "",  # human_ambiguity_type (to be filled)
                "",  # human_notes (to be filled)
            ])

    print(f"Sampled {len(selected)} clauses ({len(selected_amb)} ambiguous, {len(selected_non)} non-ambiguous)")
    print(f"Written to {OUT_CSV}")

    # Type breakdown
    for t in AMBIGUITY_TYPES:
        n = sum(1 for cid in selected_amb if cid in set(type_buckets.get(t, [])))
        if n > 0:
            print(f"  {t}: {n}")


if __name__ == "__main__":
    main()
