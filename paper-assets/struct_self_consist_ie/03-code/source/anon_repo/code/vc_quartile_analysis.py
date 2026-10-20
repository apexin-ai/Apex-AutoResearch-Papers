#!/usr/bin/env python3
"""VC Quartile stratification analysis for LP selection F1 (D105)."""

import json
import os
import sys
import numpy as np
from collections import Counter
from itertools import combinations

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import (
    _ner_soft_jaccard_pair,
    _re_soft_jaccard_pair,
    _extract_surface_keys,
)
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie"

DATASETS = {
    "scierc_ner": {
        "path": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
        "subtask": "ner",
        "gold_key": "entities",
    },
    "scierc_re": {
        "path": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
        "subtask": "re",
        "gold_key": "relations",
    },
    "conll_ner": {
        "path": f"{BASE}/output/exp002_conll2003/samples.jsonl",
        "subtask": "ner",
        "gold_key": "entities",
    },
}


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def compute_vc(instance, subtask):
    """Voting Confidence = max_count / N (exact match rate)."""
    samples = instance["samples"]
    N = len(samples)
    if N == 0:
        return 0.0
    if subtask == "ner":
        keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    else:
        keys = [frozenset((r["head"], r["tail"], r["type"]) for r in s.get("relations", [])) for s in samples]
    c = Counter(keys)
    return c.most_common(1)[0][1] / N


def compute_sample_lp_scores(instance):
    """Per-sample mean logprob."""
    return [s.get("mean_logprob", float("-inf")) for s in instance["samples"]]


def compute_sample_sj_scores(instance, subtask):
    """Pairwise soft Jaccard: mean similarity of each sample to all others."""
    samples = instance["samples"]
    N = len(samples)
    field = "entities" if subtask == "ner" else "relations"
    pair_fn = _ner_soft_jaccard_pair if subtask == "ner" else _re_soft_jaccard_pair
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            s = pair_fn(samples[i].get(field, []), samples[j].get(field, []))
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]


def compute_sample_fk_scores(instance, subtask):
    """Surface-key Jaccard (FK proxy): mean pairwise surface Jaccard per sample."""
    samples = instance["samples"]
    N = len(samples)
    key_sets = [frozenset(_extract_surface_keys(s, subtask)) for s in samples]
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            union = len(key_sets[i] | key_sets[j])
            inter = len(key_sets[i] & key_sets[j])
            s = inter / union if union > 0 else 1.0
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]


def compute_sample_em_scores(instance, subtask):
    """EM (Exact Match) score: 1 if sample matches mode output, 0 otherwise."""
    samples = instance["samples"]
    N = len(samples)
    if subtask == "ner":
        keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    else:
        keys = [frozenset((r["head"], r["tail"], r["type"]) for r in s.get("relations", [])) for s in samples]
    c = Counter(keys)
    mode_key = c.most_common(1)[0][0]
    return [1.0 if k == mode_key else 0.0 for k in keys]


def select_by_signal(scores):
    """Return index of sample with highest score. Tie-break: first occurrence."""
    return int(np.argmax(scores))


def compute_f1_for_sample(instance, sample_idx, subtask):
    return per_instance_f1(instance["samples"][sample_idx], instance["gold"], subtask=subtask)


def analyze_dataset(name, cfg):
    print(f"\n{'='*60}")
    print(f"  {name} (subtask={cfg['subtask']})")
    print(f"{'='*60}")

    instances = load_data(cfg["path"])
    subtask = cfg["subtask"]
    gold_key = cfg["gold_key"]

    # Filter gold-empty
    valid = [inst for inst in instances if len(inst["gold"].get(gold_key, [])) > 0]
    print(f"  Total: {len(instances)}, Gold-filtered: {len(valid)}")

    # Compute per-instance metrics
    records = []
    for idx, inst in enumerate(valid):
        if idx % 100 == 0:
            print(f"  Processing {idx}/{len(valid)}...", flush=True)

        vc = compute_vc(inst, subtask)
        lp_scores = compute_sample_lp_scores(inst)
        sj_scores = compute_sample_sj_scores(inst, subtask)
        fk_scores = compute_sample_fk_scores(inst, subtask)
        em_scores = compute_sample_em_scores(inst, subtask)

        # Greedy F1
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1 = per_instance_f1(greedy, inst["gold"], subtask=subtask)

        # Per-sample F1s
        sample_f1s = [per_instance_f1(s, inst["gold"], subtask=subtask) for s in inst["samples"]]

        # Oracle F1
        oracle_f1 = max(sample_f1s)

        # Selection F1 per signal
        lp_sel_idx = select_by_signal(lp_scores)
        sj_sel_idx = select_by_signal(sj_scores)
        fk_sel_idx = select_by_signal(fk_scores)
        em_sel_idx = select_by_signal(em_scores)
        # For EM ties (multiple samples match mode), use LP to break
        em_candidates = [i for i, s in enumerate(em_scores) if s == 1.0]
        if len(em_candidates) > 1:
            em_sel_idx = max(em_candidates, key=lambda i: lp_scores[i])

        records.append({
            "id": inst["id"],
            "vc": vc,
            "greedy_f1": greedy_f1,
            "oracle_f1": oracle_f1,
            "sample_f1s": sample_f1s,
            "lp_sel_f1": sample_f1s[lp_sel_idx],
            "sj_sel_f1": sample_f1s[sj_sel_idx],
            "fk_sel_f1": sample_f1s[fk_sel_idx],
            "em_sel_f1": sample_f1s[em_sel_idx],
        })

    # Sort by VC and split into quartiles
    records.sort(key=lambda r: r["vc"])
    n = len(records)
    q_size = n // 4
    quartiles = {
        "Q1": records[:q_size],
        "Q2": records[q_size:2*q_size],
        "Q3": records[2*q_size:3*q_size],
        "Q4": records[3*q_size:],
    }

    results = {"n_total": len(instances), "n_valid": len(valid), "quartiles": {}}
    for qname, qrecs in quartiles.items():
        nq = len(qrecs)
        mean_vc = np.mean([r["vc"] for r in qrecs])
        vc_range = (min(r["vc"] for r in qrecs), max(r["vc"] for r in qrecs))
        greedy_f1 = np.mean([r["greedy_f1"] for r in qrecs])
        oracle_f1 = np.mean([r["oracle_f1"] for r in qrecs])
        lp_sel_f1 = np.mean([r["lp_sel_f1"] for r in qrecs])
        sj_sel_f1 = np.mean([r["sj_sel_f1"] for r in qrecs])
        fk_sel_f1 = np.mean([r["fk_sel_f1"] for r in qrecs])
        em_sel_f1 = np.mean([r["em_sel_f1"] for r in qrecs])

        # Mean of all sample F1s (random baseline)
        all_sample_f1s = [f for r in qrecs for f in r["sample_f1s"]]
        random_f1 = np.mean(all_sample_f1s)

        results["quartiles"][qname] = {
            "n": nq,
            "mean_vc": float(mean_vc),
            "vc_range": [float(vc_range[0]), float(vc_range[1])],
            "greedy_f1": float(greedy_f1),
            "oracle_f1": float(oracle_f1),
            "random_f1": float(random_f1),
            "lp_sel_f1": float(lp_sel_f1),
            "sj_sel_f1": float(sj_sel_f1),
            "fk_sel_f1": float(fk_sel_f1),
            "em_sel_f1": float(em_sel_f1),
            "lp_delta": float(lp_sel_f1 - greedy_f1),
            "sj_delta": float(sj_sel_f1 - greedy_f1),
            "fk_delta": float(fk_sel_f1 - greedy_f1),
            "em_delta": float(em_sel_f1 - greedy_f1),
            "oracle_headroom": float(oracle_f1 - greedy_f1),
        }

        print(f"  {qname}: n={nq}, VC=[{vc_range[0]:.3f}, {vc_range[1]:.3f}], "
              f"mean_VC={mean_vc:.3f}, greedy={greedy_f1:.4f}, "
              f"LP_sel={lp_sel_f1:.4f}, Δ={lp_sel_f1-greedy_f1:+.4f}, "
              f"oracle={oracle_f1:.4f}")

    # Overall
    overall_greedy = np.mean([r["greedy_f1"] for r in records])
    overall_lp = np.mean([r["lp_sel_f1"] for r in records])
    overall_oracle = np.mean([r["oracle_f1"] for r in records])
    results["overall"] = {
        "n": len(records),
        "greedy_f1": float(overall_greedy),
        "oracle_f1": float(overall_oracle),
        "lp_sel_f1": float(overall_lp),
        "sj_sel_f1": float(np.mean([r["sj_sel_f1"] for r in records])),
        "fk_sel_f1": float(np.mean([r["fk_sel_f1"] for r in records])),
        "em_sel_f1": float(np.mean([r["em_sel_f1"] for r in records])),
        "lp_delta": float(overall_lp - overall_greedy),
        "oracle_headroom": float(overall_oracle - overall_greedy),
    }

    return results


def main():
    all_results = {}
    for name, cfg in DATASETS.items():
        all_results[name] = analyze_dataset(name, cfg)

    out_path = f"{BASE}/output/vc_quartile_analysis.json"
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
