#!/usr/bin/env python3
"""RE Selection F1 recomputation — three instance sets, five signals."""

import json
import os
import sys
from collections import Counter

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from consistency import (
    _re_soft_jaccard_pair,
    _extract_surface_keys,
)
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl"
OUTPUT_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/review_round2/re_selection_recompute.json"

N_RANDOM_REPEATS = 200


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


# ── Per-sample signal scores ────────────────────────────────────

def sample_sj_scores(samples, subtask="re"):
    N = len(samples)
    field = "relations"
    pair_fn = _re_soft_jaccard_pair
    mat = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            s = pair_fn(samples[i].get(field, []), samples[j].get(field, []))
            mat[i][j] = s
            mat[j][i] = s
    np.fill_diagonal(mat, 1.0)
    return [float(np.mean([mat[k][j] for j in range(N) if j != k])) for k in range(N)]


def sample_surface_jaccard_scores(samples, subtask="re"):
    N = len(samples)
    key_sets = [frozenset(_extract_surface_keys(s, subtask)) for s in samples]
    mat = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            union = len(key_sets[i] | key_sets[j])
            inter = len(key_sets[i] & key_sets[j])
            s = inter / union if union > 0 else 1.0
            mat[i][j] = s
            mat[j][i] = s
    np.fill_diagonal(mat, 1.0)
    fk_scores = [float(np.mean([mat[k][j] for j in range(N) if j != k])) for k in range(N)]
    return fk_scores, key_sets


def sample_voting_conf(key_sets, N):
    all_keys_count = Counter()
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


def sample_em_scores(key_sets):
    N = len(key_sets)
    return [float(sum(1 for j in range(N) if j != k and key_sets[k] == key_sets[j])) for k in range(N)]


def sample_logprob_scores(samples):
    return [s.get("mean_logprob", float("-inf")) for s in samples]


def select_top1(scores):
    return int(np.argmax(scores))


# ── Main analysis ───────────────────────────────────────────────

def analyze_set(instances, set_name):
    n = len(instances)
    rng = np.random.default_rng(42)

    greedy_f1s = []
    oracle_f1s = []
    random_f1s = []
    signal_f1s = {sig: [] for sig in ["sj", "fk", "em", "voting_conf", "logprob"]}

    for inst in instances:
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy", samples[0])
        N = len(samples)

        g_f1 = per_instance_f1(greedy, gold, subtask="re")
        greedy_f1s.append(g_f1)

        sample_f1_list = [per_instance_f1(s, gold, subtask="re") for s in samples]
        oracle_f1s.append(max(sample_f1_list))
        random_f1s.append(float(np.mean(sample_f1_list)))

        # SJ
        sj_sc = sample_sj_scores(samples, "re")
        signal_f1s["sj"].append(sample_f1_list[select_top1(sj_sc)])

        # FK (surface Jaccard)
        fk_sc, key_sets = sample_surface_jaccard_scores(samples, "re")
        signal_f1s["fk"].append(sample_f1_list[select_top1(fk_sc)])

        # EM
        em_sc = sample_em_scores(key_sets)
        signal_f1s["em"].append(sample_f1_list[select_top1(em_sc)])

        # voting_conf
        vc_sc = sample_voting_conf(key_sets, N)
        signal_f1s["voting_conf"].append(sample_f1_list[select_top1(vc_sc)])

        # logprob
        lp_sc = sample_logprob_scores(samples)
        signal_f1s["logprob"].append(sample_f1_list[select_top1(lp_sc)])

    result = {
        "n": n,
        "greedy_f1": round(float(np.mean(greedy_f1s)), 6),
        "oracle_f1": round(float(np.mean(oracle_f1s)), 6),
        "random_f1": round(float(np.mean(random_f1s)), 6),
        "signals": {},
    }
    for sig in ["sj", "fk", "em", "voting_conf", "logprob"]:
        arr = np.array(signal_f1s[sig])
        result["signals"][sig] = {
            "selection_f1": round(float(arr.mean()), 6),
            "delta_vs_greedy": round(float(arr.mean()) - float(np.mean(greedy_f1s)), 6),
        }

    return result, greedy_f1s


def main():
    all_instances = load_data(DATA_PATH)
    print(f"Loaded {len(all_instances)} total instances, N={len(all_instances[0]['samples'])}")

    # Full set: gold relations non-empty
    full = [inst for inst in all_instances if len(inst["gold"].get("relations", [])) > 0]
    print(f"Full set (gold relations > 0): {len(full)}")

    full_result, full_greedy_f1s = analyze_set(full, "full_set")

    # Conditional set: full set where greedy F1 > 0
    conditional_insts = [inst for inst, f1 in zip(full, full_greedy_f1s) if f1 > 0]
    print(f"Conditional set (greedy F1 > 0): {len(conditional_insts)}")
    cond_result, _ = analyze_set(conditional_insts, "conditional_set")
    cond_result["filter"] = "greedy_f1 > 0"

    # Unfiltered: all 551
    print(f"Unfiltered: {len(all_instances)}")
    unfiltered_result, unfiltered_greedy_f1s = analyze_set(all_instances, "unfiltered")

    # Histogram of per-instance greedy RE F1 (full set)
    f1_arr = np.array(full_greedy_f1s)
    hist = {
        "0": int(np.sum(f1_arr == 0)),
        "(0,0.2]": int(np.sum((f1_arr > 0) & (f1_arr <= 0.2))),
        "(0.2,0.4]": int(np.sum((f1_arr > 0.2) & (f1_arr <= 0.4))),
        "(0.4,0.6]": int(np.sum((f1_arr > 0.4) & (f1_arr <= 0.6))),
        "(0.6,0.8]": int(np.sum((f1_arr > 0.6) & (f1_arr <= 0.8))),
        "(0.8,1.0]": int(np.sum((f1_arr > 0.8) & (f1_arr <= 1.0))),
    }
    print(f"\n=== Full set greedy RE F1 histogram ===")
    for bucket, count in hist.items():
        pct = count / len(full_greedy_f1s) * 100
        print(f"  {bucket:>10s}: {count:4d} ({pct:5.1f}%)")

    # Also compute micro F1 for full set to check
    from evaluation import relation_strict_match, _prf
    total_tp = total_fp = total_fn = 0
    for inst in full:
        greedy = inst.get("greedy", inst["samples"][0])
        tp, fp, fn = relation_strict_match(
            greedy.get("relations", []), inst["gold"].get("relations", []))
        total_tp += tp
        total_fp += fp
        total_fn += fn
    micro = _prf(total_tp, total_fp, total_fn)
    print(f"\n=== Micro-averaged RE F1 (full set, greedy) ===")
    print(f"  P={micro['precision']:.6f}, R={micro['recall']:.6f}, F1={micro['f1']:.6f}")
    print(f"  tp={total_tp}, fp={total_fp}, fn={total_fn}")

    # Build diagnosis
    diag_lines = []
    diag_lines.append(f"Full set (n={full_result['n']}): greedy_f1={full_result['greedy_f1']:.6f} (macro)")
    diag_lines.append(f"Micro F1={micro['f1']:.6f}")
    diag_lines.append(f"Conditional set (n={cond_result['n']}): greedy_f1={cond_result['greedy_f1']:.6f}")
    diag_lines.append(f"Unfiltered (n={unfiltered_result['n']}): greedy_f1={unfiltered_result['greedy_f1']:.6f}")
    
    best_sig_full = max(full_result["signals"].items(), key=lambda x: x[1]["selection_f1"])
    best_sig_cond = max(cond_result["signals"].items(), key=lambda x: x[1]["selection_f1"])
    diag_lines.append(f"Full set best signal: {best_sig_full[0]} = {best_sig_full[1]['selection_f1']:.6f}")
    diag_lines.append(f"Conditional set best signal: {best_sig_cond[0]} = {best_sig_cond[1]['selection_f1']:.6f}")
    
    # Check if macro vs micro explains the discrepancy
    diag_lines.append(f"Macro-micro gap: {abs(full_result['greedy_f1'] - micro['f1']):.6f}")
    diag_lines.append(f"Full-conditional gap: {abs(full_result['greedy_f1'] - cond_result['greedy_f1']):.6f}")
    
    diagnosis = "\n".join(diag_lines)

    output = {
        "full_set": full_result,
        "conditional_set": cond_result,
        "unfiltered": unfiltered_result,
        "greedy_f1_histogram_full_set": hist,
        "micro_f1_full_set_greedy": {
            "precision": round(micro["precision"], 6),
            "recall": round(micro["recall"], 6),
            "f1": round(micro["f1"], 6),
            "tp": total_tp, "fp": total_fp, "fn": total_fn,
        },
        "diagnosis": diagnosis,
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2, default=lambda x: float(x) if isinstance(x, (np.floating,)) else int(x) if isinstance(x, (np.integer,)) else str(x))
    
    print(f"\n=== Full JSON output ===")
    print(json.dumps(output, indent=2, default=lambda x: float(x) if isinstance(x, (np.floating,)) else int(x) if isinstance(x, (np.integer,)) else str(x)))

    print(f"\nSaved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
