#!/usr/bin/env python3
"""Falcon3-7B-Base DiD (Difference-in-Differences) analysis for Table 3.

Computes treated vs untreated item accuracy changes at d025 MMLU,
using the same method as treated_untreated_analysis.py.

Usage (on server with eval data):
    python falcon3_did_analysis.py \
        --sft-dir /root/autodl-tmp/exp001/sft_data \
        --eval-dir /root/autodl-tmp/exp001/eval_results \
        --output-dir /root/contamcal-irt-calibration/artifacts/falcon3_did
"""

import argparse
import json
import os
from pathlib import Path

import numpy as np


EVAL_PREFIX = "Falcon3-7B-Base"
DOSAGES = ["d005", "d025", "d050", "d100"]
DOSAGE_PCTS = {"d005": 0.5, "d025": 2.5, "d050": 5.0, "d100": 10.0}
BENCHMARKS = ["mmlu", "arc_challenge"]


def load_contamination_labels(sft_dir, benchmark, dosage):
    path = Path(sft_dir) / f"contamination_labels_{benchmark}_{dosage}.json"
    with open(path) as f:
        data = json.load(f)
    return np.array(data["labels"], dtype=bool)


def load_correctness(eval_dir, dosage, benchmark):
    path = Path(eval_dir) / f"{EVAL_PREFIX}_{dosage}_s42_aligned" / "correctness_matrix.json"
    with open(path) as f:
        data = json.load(f)
    return np.array(data[benchmark], dtype=bool)


def bootstrap_diff_ci(x, y, n_boot=10000, ci=0.95, seed=42):
    rng = np.random.RandomState(seed)
    diffs = []
    for _ in range(n_boot):
        mx = np.mean(rng.choice(x, size=len(x), replace=True))
        my = np.mean(rng.choice(y, size=len(y), replace=True))
        diffs.append(mx - my)
    diffs = np.array(diffs)
    alpha = (1 - ci) / 2
    lo, hi = np.percentile(diffs, [alpha * 100, (1 - alpha) * 100])
    p_value = 2 * min(np.mean(diffs > 0), np.mean(diffs < 0))
    return lo, hi, p_value


def classify_verdict(treated_delta, untreated_delta, treated_p, untreated_p, alpha=0.05):
    t_sig = treated_p < alpha
    u_sig = untreated_p < alpha
    if t_sig and treated_delta > 0 and not u_sig:
        return "memorization"
    elif t_sig and treated_delta > 0 and u_sig and untreated_delta < 0:
        return "memorization+forgetting"
    elif t_sig and treated_delta > 0 and u_sig and untreated_delta > 0:
        return "generalization"
    elif t_sig and treated_delta < 0:
        return "anti-contamination"
    elif not t_sig and u_sig and untreated_delta < 0:
        return "forgetting-only"
    elif not t_sig and not u_sig:
        return "no-effect"
    else:
        return "mixed"


def run_analysis(sft_dir, eval_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    results = {}

    for benchmark in BENCHMARKS:
        baseline = load_correctness(eval_dir, "d000", benchmark)

        for dosage in DOSAGES:
            labels = load_contamination_labels(sft_dir, benchmark, dosage)
            treated_mask = labels
            untreated_mask = ~labels
            dosed = load_correctness(eval_dir, dosage, benchmark)

            treated_base = baseline[treated_mask].astype(float)
            treated_dose = dosed[treated_mask].astype(float)
            untreated_base = baseline[untreated_mask].astype(float)
            untreated_dose = dosed[untreated_mask].astype(float)

            treated_delta_arr = treated_dose - treated_base
            untreated_delta_arr = untreated_dose - untreated_base

            treated_delta = np.mean(treated_delta_arr)
            untreated_delta = np.mean(untreated_delta_arr)

            t_lo, t_hi, t_p = bootstrap_diff_ci(treated_dose, treated_base, seed=42)
            u_lo, u_hi, u_p = bootstrap_diff_ci(untreated_dose, untreated_base, seed=42)

            did = treated_delta - untreated_delta
            rng = np.random.RandomState(42)
            did_boots = []
            for _ in range(10000):
                t_boot = np.mean(rng.choice(treated_delta_arr, size=len(treated_delta_arr), replace=True))
                u_boot = np.mean(rng.choice(untreated_delta_arr, size=len(untreated_delta_arr), replace=True))
                did_boots.append(t_boot - u_boot)
            did_boots = np.array(did_boots)
            did_lo, did_hi = np.percentile(did_boots, [2.5, 97.5])
            did_p = 2 * min(np.mean(did_boots > 0), np.mean(did_boots < 0))

            verdict = classify_verdict(treated_delta, untreated_delta, t_p, u_p)

            key = f"{benchmark}_{dosage}"
            results[key] = {
                "benchmark": benchmark,
                "dosage": dosage,
                "dosage_pct": DOSAGE_PCTS[dosage],
                "n_treated": int(treated_mask.sum()),
                "n_untreated": int(untreated_mask.sum()),
                "treated_acc_base": round(float(np.mean(treated_base)), 6),
                "treated_acc_dose": round(float(np.mean(treated_dose)), 6),
                "treated_delta": round(float(treated_delta), 6),
                "treated_ci": [round(float(t_lo), 6), round(float(t_hi), 6)],
                "treated_p": round(float(t_p), 6),
                "untreated_acc_base": round(float(np.mean(untreated_base)), 6),
                "untreated_acc_dose": round(float(np.mean(untreated_dose)), 6),
                "untreated_delta": round(float(untreated_delta), 6),
                "untreated_ci": [round(float(u_lo), 6), round(float(u_hi), 6)],
                "untreated_p": round(float(u_p), 6),
                "did": round(float(did), 6),
                "did_ci": [round(float(did_lo), 6), round(float(did_hi), 6)],
                "did_p": round(float(did_p), 6),
                "verdict": verdict,
            }

            sig_t = "***" if t_p < 0.001 else "**" if t_p < 0.01 else "*" if t_p < 0.05 else "ns"
            sig_u = "***" if u_p < 0.001 else "**" if u_p < 0.01 else "*" if u_p < 0.05 else "ns"
            sig_d = "***" if did_p < 0.001 else "**" if did_p < 0.01 else "*" if did_p < 0.05 else "ns"

            print(f"[{benchmark} {dosage}] "
                  f"treated={treated_delta:+.4f}({sig_t}) "
                  f"untreated={untreated_delta:+.4f}({sig_u}) "
                  f"DiD={did:+.4f}({sig_d}) "
                  f"→ {verdict}")

    # Save JSON
    out_path = Path(output_dir) / "falcon3_did_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path}")

    # Print Table 3 row (d025 MMLU)
    d025 = results.get("mmlu_d025")
    if d025:
        sig_t = "***" if d025["treated_p"] < 0.001 else "**" if d025["treated_p"] < 0.01 else "*" if d025["treated_p"] < 0.05 else "ns"
        sig_u = "***" if d025["untreated_p"] < 0.001 else "**" if d025["untreated_p"] < 0.01 else "*" if d025["untreated_p"] < 0.05 else "ns"
        sig_d = "***" if d025["did_p"] < 0.001 else "**" if d025["did_p"] < 0.01 else "*" if d025["did_p"] < 0.05 else "ns"
        t_pp = d025["treated_delta"] * 100
        u_pp = d025["untreated_delta"] * 100
        d_pp = d025["did"] * 100

        print(f"\n{'='*60}")
        print(f"TABLE 3 ROW — Falcon3-7B (d025 MMLU)")
        print(f"{'='*60}")
        print(f"  Treated Δ:   {t_pp:+.1f} ({sig_t})")
        print(f"  Untreated Δ: {u_pp:+.1f} ({sig_u})")
        print(f"  DiD:         {d_pp:+.1f} ({sig_d})")
        print(f"  Verdict:     {d025['verdict']}")
        print(f"\n  LaTeX row:")
        t_str = f"$+${t_pp:.1f}" if t_pp > 0 else f"${t_pp:.1f}$"
        u_str = f"$+${u_pp:.1f}" if u_pp > 0 else f"${u_pp:.1f}$"
        d_str = f"$+${d_pp:.1f}" if d_pp > 0 else f"${d_pp:.1f}$"
        print(f"  Falcon3 7B & {t_str}$^{{{sig_t}}}$ & {u_str}$^{{{sig_u}}}$ & {d_str} ({sig_d}) & {d025['verdict']} \\\\")

    # Power analysis (SE from bootstrap CI)
    if d025:
        se_did = (d025["did_ci"][1] - d025["did_ci"][0]) / (2 * 1.96) * 100
        mdes = (1.96 + 0.84) * se_did
        print(f"\n  Power analysis:")
        print(f"    SE(DiD) = {se_did:.2f}pp")
        print(f"    MDES (80% power) = {mdes:.2f}pp")
        print(f"    |DiD| = {abs(d_pp):.2f}pp {'< MDES (not detectable)' if abs(d_pp) < mdes else '>= MDES (detectable)'}")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sft-dir", required=True)
    parser.add_argument("--eval-dir", required=True)
    parser.add_argument("--output-dir", default="/root/contamcal-irt-calibration/artifacts/falcon3_did")
    args = parser.parse_args()
    run_analysis(args.sft_dir, args.eval_dir, args.output_dir)
