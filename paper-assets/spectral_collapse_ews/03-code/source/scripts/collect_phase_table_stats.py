"""Compute Table 3 (phase-diagram summary) statistics from per-seed result JSONs.

Reads generational JSON files from the remote results directory, extracts
Gen-10 metrics, and computes cross-seed mean±std, CV, max_Δt, and EMA
violation diagnostics.
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np


def ratio_to_filename_tag(ratio: float) -> str:
    """Convert a numeric ratio to the filename tag used on the server.

    0.0  -> pure_collapse
    0.25 -> r025
    0.3  -> r03
    0.5  -> (empty string, no ratio tag)
    """
    if ratio == 0.0:
        return "pure_collapse"
    if ratio == 0.5:
        return ""
    # Remove the decimal point: 0.3->"03", 0.25->"025", 0.2->"02"
    s = f"{ratio:.10f}".rstrip("0").rstrip(".")
    tag = s.replace(".", "")
    return f"r{tag}"


def resolve_path(results_dir: str, ratio: float, seed: int) -> str:
    tag = ratio_to_filename_tag(ratio)
    if ratio == 0.0:
        if seed == 42:
            return f"{results_dir}/phase0_results.json"
        return f"{results_dir}/phase1_pure_collapse_seed{seed}_results.json"
    if ratio == 0.5:
        return f"{results_dir}/phase1_fixed_mix_seed{seed}_results.json"
    return f"{results_dir}/phase1_fixed_mix_{tag}_seed{seed}_results.json"


def load_seed_data(path: str) -> list[dict]:
    with open(path) as f:
        data = json.load(f)
    return sorted(data, key=lambda r: r["generation"])


def extract_sigma1(record: dict) -> float | None:
    svs = record.get("top_10_singular_values")
    if svs and len(svs) > 0:
        return svs[0]
    return None


def compute_ema(values: list[float], alpha: float) -> list[float]:
    ema = [values[0]]
    for v in values[1:]:
        ema.append(alpha * v + (1 - alpha) * ema[-1])
    return ema


def detect_ema_violations(ema: list[float]) -> list[int]:
    """Return 0-based indices where EMA decreases."""
    return [i for i in range(1, len(ema)) if ema[i] < ema[i - 1]]


def main():
    parser = argparse.ArgumentParser(description="Compute Table 3 row statistics.")
    parser.add_argument("--ratio", type=float, required=True, help="Mix ratio (e.g. 0.3)")
    parser.add_argument("--seeds", type=int, nargs="+", required=True, help="Seeds (e.g. 42 43 44)")
    parser.add_argument("--results-dir", default="/root/spectral_collapse_ews/results/",
                        help="Remote results directory")
    parser.add_argument("--gen", type=int, default=10, help="Target generation (default: 10)")
    args = parser.parse_args()

    all_records: dict[int, list[dict]] = {}  # seed -> sorted records
    for seed in args.seeds:
        path = resolve_path(args.results_dir, args.ratio, seed)
        try:
            records = load_seed_data(path)
        except FileNotFoundError:
            print(f"ERROR: {path} not found", file=sys.stderr)
            sys.exit(1)
        all_records[seed] = records
        print(f"Loaded seed {seed}: {len(records)} generations from {Path(path).name}")

    # --- Gen N metrics ---
    target_gen = args.gen
    gen_n_records = {}
    for seed, records in all_records.items():
        match = [r for r in records if r["generation"] == target_gen]
        if not match:
            max_gen = max(r["generation"] for r in records)
            print(f"WARNING: seed {seed} has no Gen {target_gen} (max={max_gen}), using Gen {max_gen}")
            match = [r for r in records if r["generation"] == max_gen]
        gen_n_records[seed] = match[0]

    metrics = {
        "SLV": ("log_det", ".1f"),
        "eff_rank": ("effective_rank", ".1f"),
        "PPL": ("perplexity", ".2f"),
        "D-4": ("distinct_4", ".3f"),
    }

    n_seeds = len(args.seeds)
    print(f"\n=== Table 3 Row (r={args.ratio}, {n_seeds} seeds) ===")

    for display_name, (field, fmt) in metrics.items():
        vals = [gen_n_records[s][field] for s in args.seeds]
        mean = np.mean(vals)
        std = np.std(vals, ddof=0)
        cv = (std / abs(mean) * 100) if mean != 0 else 0.0
        print(f"{display_name}: {mean:{fmt}} ± {std:{fmt}} (CV={cv:.2f}%)")

    sigma1_vals = [extract_sigma1(gen_n_records[s]) for s in args.seeds]
    if all(v is not None for v in sigma1_vals):
        s1_mean = np.mean(sigma1_vals)
        s1_std = np.std(sigma1_vals, ddof=0)
        print(f"σ₁: {s1_mean:.1f} ± {s1_std:.1f}")
    else:
        print("σ₁: n/a (missing top_10_singular_values)")

    # --- max_Δt (normalized SLV drop) ---
    slv_trajectories = []
    for seed in args.seeds:
        slv_trajectories.append([r["log_det"] for r in all_records[seed]])

    min_len = min(len(t) for t in slv_trajectories)
    slv_trajectories = [t[:min_len] for t in slv_trajectories]
    mean_slv = np.mean(slv_trajectories, axis=0)

    deltas = []
    for t in range(1, len(mean_slv)):
        delta = mean_slv[t] - mean_slv[t - 1]
        deltas.append((t, delta, mean_slv[t - 1]))

    negative_deltas = [(t, d, prev) for t, d, prev in deltas if d < 0]
    if not negative_deltas:
        max_dt = 0.0
        max_dt_gen = None
    else:
        worst = min(negative_deltas, key=lambda x: x[1])
        max_dt = abs(worst[1] / worst[2]) if worst[2] != 0 else 0.0
        max_dt_gen = worst[0]

    if max_dt == 0:
        print(f"max_Δt: 0")
    else:
        gens_in_data = [r["generation"] for r in all_records[args.seeds[0]]]
        actual_gen = gens_in_data[max_dt_gen] if max_dt_gen < len(gens_in_data) else max_dt_gen
        print(f"max_Δt: {max_dt:.4f} (at Gen {actual_gen})")

    # --- EMA violations ---
    alphas = [0.3, 0.5, 0.7]
    ema_parts = []
    for alpha in alphas:
        ema = compute_ema(mean_slv.tolist(), alpha)
        violations = detect_ema_violations(ema)
        if not violations:
            ema_parts.append(f"none (α={alpha})")
        else:
            gens_in_data = [r["generation"] for r in all_records[args.seeds[0]]]
            viol_gens = [gens_in_data[i] if i < len(gens_in_data) else i for i in violations]
            ema_parts.append(f"Gen {','.join(map(str, viol_gens))} (α={alpha})")
    print(f"EMA violations: {', '.join(ema_parts)}")

    # --- Phase classification heuristic ---
    slv_gen0 = mean_slv[0]
    slv_final = mean_slv[-1]
    slv_change_pct = (slv_final - slv_gen0) / abs(slv_gen0) * 100 if slv_gen0 != 0 else 0

    ppl_vals = [gen_n_records[s]["perplexity"] for s in args.seeds]
    mean_ppl = np.mean(ppl_vals)
    d4_vals = [gen_n_records[s]["distinct_4"] for s in args.seeds]
    mean_d4 = np.mean(d4_vals)

    if max_dt == 0 and slv_change_pct > 0:
        phase = "I"  # monotonic growth
    elif mean_ppl > 50 or mean_d4 < 0.05:
        phase = "III"  # collapse
    elif max_dt > 0.01:
        phase = "III"
    else:
        phase = "II"  # intermediate

    # --- Onset generation ---
    slv_peak_idx = int(np.argmax(mean_slv))
    onset_gen = "–"
    for i in range(slv_peak_idx + 1, len(mean_slv) - 1):
        if mean_slv[i] < mean_slv[i - 1] and mean_slv[i + 1] < mean_slv[i]:
            gens_in_data = [r["generation"] for r in all_records[args.seeds[0]]]
            onset_gen = gens_in_data[i] if i < len(gens_in_data) else i
            break

    # --- LaTeX row ---
    slv_mean = np.mean([gen_n_records[s]["log_det"] for s in args.seeds])
    er_mean = np.mean([gen_n_records[s]["effective_rank"] for s in args.seeds])
    ppl_mean = np.mean([gen_n_records[s]["perplexity"] for s in args.seeds])
    d4_mean = np.mean([gen_n_records[s]["distinct_4"] for s in args.seeds])

    d4_str = f"{d4_mean:.3f}".lstrip("0")  # 0.232 -> .232

    print(f"\nLaTeX row:")
    print(f"{args.ratio:.2f} & {phase} & {slv_mean:.1f} & {er_mean:.1f} & "
          f"{ppl_mean:.2f} & {d4_str} & {max_dt:.0f} & {onset_gen} \\\\")

    # --- Raw per-seed dump for verification ---
    print(f"\n--- Per-seed Gen {target_gen} values ---")
    header = f"{'seed':>6} {'SLV':>10} {'eff_rank':>10} {'PPL':>10} {'D-4':>10} {'σ₁':>10}"
    print(header)
    for seed in args.seeds:
        r = gen_n_records[seed]
        s1 = extract_sigma1(r)
        s1_str = f"{s1:.1f}" if s1 is not None else "n/a"
        print(f"{seed:>6} {r['log_det']:>10.1f} {r['effective_rank']:>10.1f} "
              f"{r['perplexity']:>10.2f} {r['distinct_4']:>10.3f} {s1_str:>10}")


if __name__ == "__main__":
    main()
