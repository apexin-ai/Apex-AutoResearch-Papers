#!/usr/bin/env python3
"""D140 Task A: Oracle Degeneracy-Gated LP Selection Analysis.

For each dataset, computes:
- Degeneracy rate (F1-based: all N samples have identical F1)
- Ungated LP selection F1 (all instances)
- Gated LP selection F1 (LP on non-degenerate, greedy on degenerate)
- Delta comparisons vs greedy baseline
"""

import json
import os
import sys

sys.path.insert(0, "/root/autodl-tmp/struct_self_consist_ie/code")
from evaluation import entity_strict_match, _prf, per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie"

DATASETS = {
    "Few-NERD": f"{BASE}/output/exp_021_inference/samples.jsonl",
    "SciERC": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
    "CoNLL": f"{BASE}/output/exp002_conll2003/samples.jsonl",
}


def load_gold_filtered(path):
    data = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            inst = json.loads(line)
            if len(inst["gold"].get("entities", [])) > 0:
                data.append(inst)
    return data


def get_tp_fp_fn(pred, gold):
    return entity_strict_match(
        pred.get("entities", []), gold.get("entities", [])
    )


def micro_f1_from_counts(tp, fp, fn):
    return _prf(tp, fp, fn)["f1"]


def analyze_dataset(name, path):
    if not os.path.exists(path):
        print(f"SKIP {name}: {path} not found")
        return None

    data = load_gold_filtered(path)
    n_total = len(data)
    print(f"\n{'='*60}")
    print(f"{name}: {n_total} gold-filtered instances")

    greedy_counts = {"tp": 0, "fp": 0, "fn": 0}
    oracle_counts = {"tp": 0, "fp": 0, "fn": 0}
    lp_all_counts = {"tp": 0, "fp": 0, "fn": 0}
    lp_nondeg_counts = {"tp": 0, "fp": 0, "fn": 0}
    greedy_deg_counts = {"tp": 0, "fp": 0, "fn": 0}
    greedy_nondeg_counts = {"tp": 0, "fp": 0, "fn": 0}
    gated_counts = {"tp": 0, "fp": 0, "fn": 0}

    n_degenerate = 0
    per_inst_greedy_f1 = []
    per_inst_lp_f1 = []
    per_inst_gated_f1 = []

    for inst in data:
        gold = inst["gold"]
        samples = inst["samples"]
        greedy = inst["greedy"]

        g_tp, g_fp, g_fn = get_tp_fp_fn(greedy, gold)
        greedy_counts["tp"] += g_tp
        greedy_counts["fp"] += g_fp
        greedy_counts["fn"] += g_fn
        greedy_f1_i = _prf(g_tp, g_fp, g_fn)["f1"]
        per_inst_greedy_f1.append(greedy_f1_i)

        sample_f1s = []
        sample_lps = []
        sample_tpfpfn = []
        for s in samples:
            tp, fp, fn = get_tp_fp_fn(s, gold)
            f1_i = _prf(tp, fp, fn)["f1"]
            sample_f1s.append(f1_i)
            sample_lps.append(s.get("mean_logprob", s.get("cumulative_logprob", 0)))
            sample_tpfpfn.append((tp, fp, fn))

        best_idx = max(range(len(sample_f1s)), key=lambda i: sample_f1s[i])
        oracle_counts["tp"] += sample_tpfpfn[best_idx][0]
        oracle_counts["fp"] += sample_tpfpfn[best_idx][1]
        oracle_counts["fn"] += sample_tpfpfn[best_idx][2]

        lp_idx = max(range(len(sample_lps)), key=lambda i: sample_lps[i])
        lp_tp, lp_fp, lp_fn = sample_tpfpfn[lp_idx]
        lp_all_counts["tp"] += lp_tp
        lp_all_counts["fp"] += lp_fp
        lp_all_counts["fn"] += lp_fn
        lp_f1_i = _prf(lp_tp, lp_fp, lp_fn)["f1"]
        per_inst_lp_f1.append(lp_f1_i)

        is_degenerate = len(set(round(f, 10) for f in sample_f1s)) == 1
        if is_degenerate:
            n_degenerate += 1
            greedy_deg_counts["tp"] += g_tp
            greedy_deg_counts["fp"] += g_fp
            greedy_deg_counts["fn"] += g_fn
            gated_counts["tp"] += g_tp
            gated_counts["fp"] += g_fp
            gated_counts["fn"] += g_fn
            per_inst_gated_f1.append(greedy_f1_i)
        else:
            lp_nondeg_counts["tp"] += lp_tp
            lp_nondeg_counts["fp"] += lp_fp
            lp_nondeg_counts["fn"] += lp_fn
            greedy_nondeg_counts["tp"] += g_tp
            greedy_nondeg_counts["fp"] += g_fp
            greedy_nondeg_counts["fn"] += g_fn
            gated_counts["tp"] += lp_tp
            gated_counts["fp"] += lp_fp
            gated_counts["fn"] += lp_fn
            per_inst_gated_f1.append(lp_f1_i)

    n_nondeg = n_total - n_degenerate

    greedy_f1 = micro_f1_from_counts(**greedy_counts)
    oracle_f1 = micro_f1_from_counts(**oracle_counts)
    ungated_lp_f1 = micro_f1_from_counts(**lp_all_counts)
    gated_f1 = micro_f1_from_counts(**gated_counts)

    nondeg_lp_f1 = micro_f1_from_counts(**lp_nondeg_counts) if n_nondeg > 0 else 0.0
    nondeg_greedy_f1 = micro_f1_from_counts(**greedy_nondeg_counts) if n_nondeg > 0 else 0.0
    deg_greedy_f1 = micro_f1_from_counts(**greedy_deg_counts) if n_degenerate > 0 else 0.0

    ungated_delta = ungated_lp_f1 - greedy_f1
    nondeg_delta = nondeg_lp_f1 - nondeg_greedy_f1
    gated_delta = gated_f1 - greedy_f1
    improvement = gated_delta - ungated_delta

    macro_greedy = sum(per_inst_greedy_f1) / n_total
    macro_lp = sum(per_inst_lp_f1) / n_total
    macro_gated = sum(per_inst_gated_f1) / n_total

    result = {
        "dataset": name,
        "total_instances": n_total,
        "degenerate_count": n_degenerate,
        "non_degenerate_count": n_nondeg,
        "degeneracy_rate": f"{n_degenerate}/{n_total} ({100*n_degenerate/n_total:.1f}%)",
        "greedy_f1": round(greedy_f1 * 100, 2),
        "oracle_f1": round(oracle_f1 * 100, 2),
        "ungated_lp_selection_f1": round(ungated_lp_f1 * 100, 2),
        "ungated_lp_delta": round(ungated_delta * 100, 2),
        "nondegen_greedy_f1": round(nondeg_greedy_f1 * 100, 2),
        "nondegen_lp_selection_f1": round(nondeg_lp_f1 * 100, 2),
        "nondegen_lp_delta": round(nondeg_delta * 100, 2),
        "degen_greedy_f1": round(deg_greedy_f1 * 100, 2),
        "gated_overall_f1": round(gated_f1 * 100, 2),
        "gated_delta": round(gated_delta * 100, 2),
        "gated_vs_ungated_improvement": round(improvement * 100, 2),
        "macro_avg": {
            "greedy_f1": round(macro_greedy * 100, 2),
            "lp_f1": round(macro_lp * 100, 2),
            "gated_f1": round(macro_gated * 100, 2),
            "lp_delta": round((macro_lp - macro_greedy) * 100, 2),
            "gated_delta": round((macro_gated - macro_greedy) * 100, 2),
        },
    }

    print(f"  Degeneracy: {n_degenerate}/{n_total} ({100*n_degenerate/n_total:.1f}%)")
    print(f"  Greedy F1 (micro):         {greedy_f1*100:.2f}")
    print(f"  Oracle F1 (micro):         {oracle_f1*100:.2f}")
    print(f"  Ungated LP F1 (micro):     {ungated_lp_f1*100:.2f}  (delta: {ungated_delta*100:+.2f})")
    print(f"  NonDegen LP F1 (micro):    {nondeg_lp_f1*100:.2f}  (delta vs nondeg greedy: {nondeg_delta*100:+.2f})")
    print(f"  Degen Greedy F1 (micro):   {deg_greedy_f1*100:.2f}")
    print(f"  Gated F1 (micro):          {gated_f1*100:.2f}  (delta: {gated_delta*100:+.2f})")
    print(f"  Gated vs Ungated improve:  {improvement*100:+.2f}")
    print(f"  ---")
    print(f"  Macro Greedy F1:           {macro_greedy*100:.2f}")
    print(f"  Macro LP F1:               {macro_lp*100:.2f}  (delta: {(macro_lp-macro_greedy)*100:+.2f})")
    print(f"  Macro Gated F1:            {macro_gated*100:.2f}  (delta: {(macro_gated-macro_greedy)*100:+.2f})")

    return result


def main():
    out_dir = f"{BASE}/output/d140_oracle_gated"
    os.makedirs(out_dir, exist_ok=True)

    all_results = []
    for name, path in DATASETS.items():
        r = analyze_dataset(name, path)
        if r:
            all_results.append(r)

    out_path = f"{out_dir}/results.json"
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
