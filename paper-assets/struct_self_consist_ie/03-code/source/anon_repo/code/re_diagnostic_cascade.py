"""RE Diagnostic Cascade Analysis for SciERC RE.

Uses span-based strict matching (relation_strict_match from evaluation.py).
Data: exp_012_rerun_1024/samples_with_logprobs.jsonl (SciERC, N=8, seed=42).
"""
import json
import sys
import numpy as np
from scipy.stats import spearmanr
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from evaluation import relation_strict_match

BASE = Path("/root/autodl-tmp/struct_self_consist_ie")
DATA_PATH = BASE / "output" / "exp_012_rerun_1024" / "samples_with_logprobs.jsonl"
OUT_PATH = BASE / "output" / "re_diagnostic_cascade_results.json"


def f1_from_counts(tp, fp, fn):
    p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    return 2 * p * r / (p + r) if (p + r) > 0 else 0.0


def instance_re_f1(pred, gold):
    tp, fp, fn = relation_strict_match(
        pred.get("relations", []), gold.get("relations", [])
    )
    return f1_from_counts(tp, fp, fn)


def rel_set_span(rels):
    return frozenset(
        (r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"])
        for r in rels
    )


def main():
    data_all = [json.loads(l) for l in open(DATA_PATH)]
    data = [d for d in data_all if d["gold"].get("relations", [])]
    N = len(data[0]["samples"])
    print(f"RE instances: {len(data)}, N={N}")

    # Degeneracy
    n_degen = sum(
        1 for inst in data
        if len({rel_set_span(s.get("relations", [])) for s in inst["samples"]}) == 1
    )

    # Greedy F1 and zero-F1
    greedy_f1s = []
    n_zero_greedy = 0
    for inst in data:
        f1 = instance_re_f1(inst.get("greedy", {}), inst["gold"])
        greedy_f1s.append(f1)
        if f1 == 0:
            n_zero_greedy += 1

    # Oracle
    oracle_f1s = []
    for inst in data:
        best = max(instance_re_f1(s, inst["gold"]) for s in inst["samples"])
        oracle_f1s.append(best)

    # Majority Vote
    mv_f1s = []
    for inst in data:
        rel_counts = Counter()
        for s in inst["samples"]:
            for r in s.get("relations", []):
                key = (r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"])
                rel_counts[key] += 1
        mv_set = {k for k, c in rel_counts.items() if c > N / 2}
        gold_set = rel_set_span(inst["gold"].get("relations", []))
        tp = len(mv_set & gold_set)
        fp = len(mv_set - gold_set)
        fn = len(gold_set - mv_set)
        mv_f1s.append(f1_from_counts(tp, fp, fn))

    # LP-best
    lp_best_f1s = []
    for inst in data:
        best_idx = max(range(N), key=lambda i: inst["samples"][i].get("mean_logprob", float("-inf")))
        lp_best_f1s.append(instance_re_f1(inst["samples"][best_idx], inst["gold"]))

    # LP-F1 correlation
    all_lps, all_f1s, within_rhos = [], [], []
    for inst in data:
        inst_lps, inst_f1s = [], []
        for s in inst["samples"]:
            lp = s.get("mean_logprob", float("nan"))
            f1 = instance_re_f1(s, inst["gold"])
            inst_lps.append(lp)
            inst_f1s.append(f1)
            if np.isfinite(lp):
                all_lps.append(lp)
                all_f1s.append(f1)
        if len(set(inst_f1s)) > 1 and np.std(inst_lps) > 0:
            r, _ = spearmanr(inst_lps, inst_f1s)
            if np.isfinite(r):
                within_rhos.append(r)

    pooled_rho, pooled_p = spearmanr(all_lps, all_f1s)
    within_rho_mean = np.mean(within_rhos) if within_rhos else float("nan")

    greedy_macro = np.mean(greedy_f1s)
    oracle_macro = np.mean(oracle_f1s)
    mv_macro = np.mean(mv_f1s)
    lp_best_macro = np.mean(lp_best_f1s)

    results = {
        "data_source": str(DATA_PATH),
        "n_instances": len(data),
        "N": N,
        "degeneracy_rate": n_degen / len(data),
        "n_degenerate": n_degen,
        "greedy_f1_macro": float(greedy_macro),
        "mv_f1_macro": float(mv_macro),
        "mv_delta_pp": float((mv_macro - greedy_macro) * 100),
        "lp_best_f1_macro": float(lp_best_macro),
        "lp_best_delta_pp": float((lp_best_macro - greedy_macro) * 100),
        "oracle_f1_macro": float(oracle_macro),
        "oracle_headroom_pp": float((oracle_macro - greedy_macro) * 100),
        "zero_f1_pct": float(n_zero_greedy / len(data) * 100),
        "zero_f1_count": n_zero_greedy,
        "lp_f1_rho_pooled": float(pooled_rho),
        "lp_f1_rho_pooled_p": float(pooled_p),
        "lp_f1_rho_within_mean": float(within_rho_mean),
        "n_within_rho": len(within_rhos),
    }

    with open(OUT_PATH, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nDegeneracy:      {results['degeneracy_rate']*100:.1f}%")
    print(f"Greedy F1:       {greedy_macro:.4f}")
    print(f"MV F1:           {mv_macro:.4f} (Δ={results['mv_delta_pp']:+.2f}pp)")
    print(f"LP-best F1:      {lp_best_macro:.4f} (Δ={results['lp_best_delta_pp']:+.2f}pp)")
    print(f"Oracle F1:       {oracle_macro:.4f} (Δ={results['oracle_headroom_pp']:+.2f}pp)")
    print(f"Zero-F1%:        {results['zero_f1_pct']:.1f}%")
    print(f"LP-F1 ρ pooled:  {pooled_rho:.4f}")
    print(f"LP-F1 ρ within:  {within_rho_mean:.4f}")
    print(f"\nSaved to {OUT_PATH}")


if __name__ == "__main__":
    main()
