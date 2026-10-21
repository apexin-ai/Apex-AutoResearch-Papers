#!/usr/bin/env python3
"""exp-006 v2: Best-of-N Selection Analysis on v2 unified inference data.

For each instance, selects top-1 sample using different signals and reports
selection F1 (macro-averaged per-instance F1) with paired bootstrap CI.
"""

from __future__ import annotations

import json
import os
import sys
import time
from collections import Counter

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from consistency import (
    _ner_soft_jaccard_pair,
    _re_soft_jaccard_pair,
    _extract_surface_keys,
)
from evaluation import per_instance_f1

# ── Configuration ──────────────────────────────────────────────────

BASE = "/root/autodl-tmp/struct_self_consist_ie"

DATASETS = {
    "scierc_ner_s42": {
        "path": f"{BASE}/output/exp_001_seed42_v2/samples.jsonl",
        "subtask": "ner",
        "label": "NER SciERC (seed42)",
    },
    "scierc_ner_s123": {
        "path": f"{BASE}/output/exp_001_seed123_v2/samples.jsonl",
        "subtask": "ner",
        "label": "NER SciERC (seed123)",
    },
    "conll_ner": {
        "path": f"{BASE}/output/exp002_conll2003/samples.jsonl",
        "subtask": "ner",
        "label": "NER CoNLL-2003",
    },
    "scierc_re": {
        "path": f"{BASE}/output/exp_008_re_n16_v2/samples.jsonl",
        "subtask": "re",
        "label": "RE SciERC",
        "filter_fn": "has_gold_relations",
    },
}

SIGNALS = ["SJ", "logprob", "FK", "EM", "voting_conf", "random", "greedy", "oracle"]
N_BOOTSTRAP = 1000
BOOTSTRAP_SEED = 42
N_RANDOM_REPEATS = 50

OUTPUT_DIR = f"{BASE}/output/exp_006_v2"


# ── Data loading ──────────────────────────────────────────────────

def load_data(path: str) -> list[dict]:
    instances = []
    with open(path) as f:
        for line in f:
            if line.strip():
                instances.append(json.loads(line))
    return instances


# ── Signal computation (per-sample scores) ────────────────────────

def compute_sample_sj_scores(instance: dict, subtask: str) -> list[float]:
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


def compute_sample_surface_scores(instance: dict, subtask: str) -> tuple[list[float], list[frozenset]]:
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

    fk_scores = [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]
    return fk_scores, key_sets


def compute_sample_voting_conf(key_sets: list[frozenset], N: int) -> list[float]:
    all_keys_count: Counter = Counter()
    for ks in key_sets:
        for key in ks:
            all_keys_count[key] += 1
    scores = []
    for ks in key_sets:
        if not ks:
            scores.append(0.0)
        else:
            fracs = [all_keys_count[key] / N for key in ks]
            scores.append(float(np.mean(fracs)))
    return scores


def compute_sample_em_scores(key_sets: list[frozenset]) -> list[float]:
    N = len(key_sets)
    scores = []
    for k in range(N):
        count = sum(1 for j in range(N) if j != k and key_sets[k] == key_sets[j])
        scores.append(float(count))
    return scores


def compute_sample_logprobs(instance: dict) -> list[float]:
    lps = []
    for s in instance["samples"]:
        lp = s.get("mean_logprob")
        if lp is None:
            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        lps.append(lp)
    return lps


# ── Selection ─────────────────────────────────────────────────────

def select_top1(signal_scores: list[float]) -> int:
    return int(np.argmax(signal_scores))


# ── Bootstrap CI ──────────────────────────────────────────────────

def paired_bootstrap_ci(
    f1s_a: np.ndarray,
    f1s_b: np.ndarray,
    n_boot: int = 1000,
    seed: int = 42,
    alpha: float = 0.05,
) -> dict:
    rng = np.random.default_rng(seed)
    n = len(f1s_a)
    deltas = np.empty(n_boot)
    for b in range(n_boot):
        idx = rng.integers(0, n, size=n)
        deltas[b] = f1s_a[idx].mean() - f1s_b[idx].mean()
    lo = float(np.percentile(deltas, 100 * alpha / 2))
    hi = float(np.percentile(deltas, 100 * (1 - alpha / 2)))
    mean_delta = float(np.mean(deltas))
    p_value = float(np.mean(deltas <= 0)) if mean_delta > 0 else float(np.mean(deltas >= 0))
    return {"mean_delta": mean_delta, "ci_lo": lo, "ci_hi": hi, "p_value": p_value}


# ── Main analysis ─────────────────────────────────────────────────

def analyze_dataset(instances: list[dict], subtask: str, label: str) -> dict:
    n_inst = len(instances)
    rng = np.random.default_rng(BOOTSTRAP_SEED)

    # Per-instance: compute all signal scores, select top-1, get F1
    signal_f1s = {sig: [] for sig in SIGNALS}
    all_per_sample_f1s = []

    t0 = time.time()
    for idx, inst in enumerate(instances):
        if (idx + 1) % 200 == 0:
            print(f"    {idx+1}/{n_inst} ({time.time()-t0:.0f}s)")

        samples = inst["samples"]
        gold = inst["gold"]
        N = len(samples)

        # Per-sample F1s
        sample_f1s = [per_instance_f1(s, gold, subtask=subtask) for s in samples]
        all_per_sample_f1s.append(sample_f1s)

        # Greedy F1
        greedy_f1 = per_instance_f1(inst["greedy"], gold, subtask=subtask)
        signal_f1s["greedy"].append(greedy_f1)

        # Oracle
        signal_f1s["oracle"].append(max(sample_f1s))

        # Logprob
        lps = compute_sample_logprobs(inst)
        signal_f1s["logprob"].append(sample_f1s[select_top1(lps)])

        # SJ
        sj_scores = compute_sample_sj_scores(inst, subtask)
        signal_f1s["SJ"].append(sample_f1s[select_top1(sj_scores)])

        # FK + surface keys (reused for voting_conf and EM)
        fk_scores, key_sets = compute_sample_surface_scores(inst, subtask)
        signal_f1s["FK"].append(sample_f1s[select_top1(fk_scores)])

        # Voting confidence
        vc_scores = compute_sample_voting_conf(key_sets, N)
        signal_f1s["voting_conf"].append(sample_f1s[select_top1(vc_scores)])

        # Exact match
        em_scores = compute_sample_em_scores(key_sets)
        signal_f1s["EM"].append(sample_f1s[select_top1(em_scores)])

        # Random (average over repeats)
        random_f1s = []
        for _ in range(N_RANDOM_REPEATS):
            ri = int(rng.integers(0, N))
            random_f1s.append(sample_f1s[ri])
        signal_f1s["random"].append(float(np.mean(random_f1s)))

    elapsed = time.time() - t0
    print(f"    Done in {elapsed:.1f}s")

    # Convert to arrays
    for sig in SIGNALS:
        signal_f1s[sig] = np.array(signal_f1s[sig])

    # Macro F1 and bootstrap CI vs greedy
    results = {}
    greedy_arr = signal_f1s["greedy"]
    for sig in SIGNALS:
        arr = signal_f1s[sig]
        mean_f1 = float(arr.mean())
        std_f1 = float(arr.std())

        if sig != "greedy":
            boot = paired_bootstrap_ci(arr, greedy_arr, N_BOOTSTRAP, BOOTSTRAP_SEED)
        else:
            boot = {"mean_delta": 0.0, "ci_lo": 0.0, "ci_hi": 0.0, "p_value": 1.0}

        results[sig] = {
            "mean_f1": round(mean_f1, 5),
            "std_f1": round(std_f1, 5),
            "delta_vs_greedy": round(float(arr.mean() - greedy_arr.mean()), 5),
            "bootstrap_ci_lo": round(boot["ci_lo"], 5),
            "bootstrap_ci_hi": round(boot["ci_hi"], 5),
            "bootstrap_p": round(boot["p_value"], 5),
        }

    # Oracle gap analysis
    oracle_arr = signal_f1s["oracle"]
    oracle_gap = float(oracle_arr.mean() - greedy_arr.mean())

    return {
        "label": label,
        "subtask": subtask,
        "n_instances": n_inst,
        "n_samples": len(instances[0]["samples"]),
        "greedy_macro_f1": results["greedy"]["mean_f1"],
        "oracle_macro_f1": results["oracle"]["mean_f1"],
        "oracle_gap": round(oracle_gap, 5),
        "signals": results,
    }


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    all_results = {}

    for ds_key, ds_cfg in DATASETS.items():
        print(f"\n{'='*60}")
        print(f"  {ds_cfg['label']} ({ds_key})")
        print(f"{'='*60}")

        if not os.path.exists(ds_cfg["path"]):
            print(f"  SKIP: {ds_cfg['path']} not found")
            continue

        instances = load_data(ds_cfg["path"])
        print(f"  Loaded {len(instances)} instances")

        if ds_cfg.get("filter_fn") == "has_gold_relations":
            before = len(instances)
            instances = [inst for inst in instances if len(inst["gold"].get("relations", [])) > 0]
            print(f"  Filtered: {before} -> {len(instances)} (with gold relations)")

        result = analyze_dataset(instances, ds_cfg["subtask"], ds_cfg["label"])
        all_results[ds_key] = result

        # Print table
        print(f"\n  {'Signal':>15s}  {'Mean F1':>8s}  {'Δ greedy':>9s}  {'95% CI':>18s}  {'p':>6s}")
        print(f"  {'-'*15}  {'-'*8}  {'-'*9}  {'-'*18}  {'-'*6}")
        for sig in SIGNALS:
            r = result["signals"][sig]
            ci_str = f"[{r['bootstrap_ci_lo']:+.4f}, {r['bootstrap_ci_hi']:+.4f}]"
            print(f"  {sig:>15s}  {r['mean_f1']:.4f}  {r['delta_vs_greedy']:+.4f}  {ci_str:>18s}  {r['bootstrap_p']:.3f}")
        print(f"\n  Oracle gap: {result['oracle_gap']:.4f}")

    # Save JSON
    out_path = os.path.join(OUTPUT_DIR, "exp_006_v2_results.json")
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved: {out_path}")

    # Summary: which signals beat greedy?
    print(f"\n{'='*60}")
    print("  SUMMARY: Signals that beat greedy (p < 0.05)")
    print(f"{'='*60}")
    for ds_key, result in all_results.items():
        print(f"\n  {result['label']}:")
        beats = []
        for sig in ["SJ", "logprob", "FK", "EM", "voting_conf"]:
            r = result["signals"][sig]
            if r["delta_vs_greedy"] > 0 and r["bootstrap_ci_lo"] > 0:
                beats.append(f"{sig} (+{r['delta_vs_greedy']:.4f})")
        if beats:
            print(f"    {', '.join(beats)}")
        else:
            print(f"    None")


if __name__ == "__main__":
    main()
