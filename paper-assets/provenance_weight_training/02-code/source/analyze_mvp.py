#!/usr/bin/env python3
"""MVP analysis for provenance_weight_training experiments.

Collects eval perplexity from eval_results.json / trainer_state.json,
compares adaptive_fix vs grid-best vs uniform baselines, and runs
MVP pass/fail judgment. Also analyzes b* trajectories for adaptive runs.

Usage:
    python analyze_mvp.py [--base_dir OUTPUT_MODELS_DIR]
"""

import argparse
import json
import math
import sys
from pathlib import Path

SEEDS = [42, 123, 456]
GRID_B_VALUES = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
B_TAG = {0.5: "0_5", 1.0: "1_0", 1.5: "1_5", 2.0: "2_0", 3.0: "3_0", 5.0: "5_0"}

KNOWN_BASELINES = {
    "uniform": {42: 17.69, 123: 17.69, 456: 17.70},
    "adaptive_orig": {42: 17.69, 123: 17.63, 456: 17.64},
    "grid_b_seed123": {
        0.5: 17.638, 1.0: 17.674, 1.5: 17.701,
        2.0: 17.725, 3.0: 17.760, 5.0: 17.804,
    },
}


def parse_args():
    p = argparse.ArgumentParser(description="MVP analysis for provenance_weight_training")
    p.add_argument("--base_dir", type=str,
                   default="/root/provenance_weight_training/output/models",
                   help="Base directory containing experiment output dirs")
    return p.parse_args()


def extract_ppl_from_eval_results(exp_dir: Path) -> float | None:
    """Read eval_results.json produced by eval_perplexity.py."""
    path = exp_dir / "eval_results.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text())
        for key, val in data.items():
            if isinstance(val, dict) and "perplexity" in val:
                return val["perplexity"]
    except (json.JSONDecodeError, KeyError):
        pass
    return None


def extract_ppl_from_trainer_state(exp_dir: Path) -> float | None:
    """Fallback: get last eval_loss from trainer_state.json, convert to ppl."""
    candidates = sorted(exp_dir.glob("checkpoint-*/trainer_state.json"))
    if (exp_dir / "final" / "trainer_state.json").exists():
        candidates.append(exp_dir / "final" / "trainer_state.json")
    if not candidates:
        return None
    state_path = candidates[-1]
    try:
        state = json.loads(state_path.read_text())
        log_history = state.get("log_history", [])
        eval_entries = [e for e in log_history if "eval_loss" in e]
        if not eval_entries:
            return None
        last_eval_loss = eval_entries[-1]["eval_loss"]
        return math.exp(last_eval_loss)
    except (json.JSONDecodeError, KeyError, OverflowError):
        pass
    return None


def get_ppl(exp_dir: Path) -> tuple[float | None, str]:
    """Try eval_results.json first, then trainer_state.json fallback."""
    ppl = extract_ppl_from_eval_results(exp_dir)
    if ppl is not None:
        return ppl, "eval_results"
    ppl = extract_ppl_from_trainer_state(exp_dir)
    if ppl is not None:
        return ppl, "trainer_state"
    return None, "missing"


def get_training_status(exp_dir: Path) -> str:
    if not exp_dir.exists():
        return "NOT_FOUND"
    if (exp_dir / "final").exists():
        return "DONE"
    checkpoints = sorted(exp_dir.glob("checkpoint-*"))
    if checkpoints:
        config = exp_dir / "config.json"
        max_steps = None
        if config.exists():
            try:
                max_steps = json.loads(config.read_text()).get("max_steps")
            except json.JSONDecodeError:
                pass
        last_ckpt = int(checkpoints[-1].name.split("-")[1])
        suffix = f" (step {last_ckpt}"
        if max_steps:
            suffix += f"/{max_steps}"
        suffix += ")"
        return "TRAINING" + suffix
    return "STARTED"


def load_b_star_trajectory(exp_dir: Path) -> list[dict]:
    path = exp_dir / "step_metrics.jsonl"
    if not path.exists():
        return []
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return records


def mean_std(vals: list[float]) -> tuple[float | None, float | None]:
    vals = [v for v in vals if v is not None]
    if not vals:
        return None, None
    m = sum(vals) / len(vals)
    if len(vals) > 1:
        s = math.sqrt(sum((v - m) ** 2 for v in vals) / (len(vals) - 1))
    else:
        s = 0.0
    return m, s


def fmt_ppl(val, src=None):
    if val is None:
        return "N/A"
    s = f"{val:.3f}"
    if src and src not in ("eval_results", None):
        s += f" ({src})"
    return s


def pct_diff(val, ref):
    if val is None or ref is None or ref == 0:
        return "N/A"
    return f"{(val - ref) / ref * 100:+.3f}%"


def main():
    args = parse_args()
    base = Path(args.base_dir)

    if not base.exists():
        print(f"ERROR: base_dir {base} does not exist")
        sys.exit(1)

    print("=" * 78)
    print("  MVP Analysis — provenance_weight_training")
    print("=" * 78)

    # ── Section 1: Training Status ──
    print("\n## Training Status\n")
    all_experiments = []

    for seed in SEEDS:
        all_experiments.append(("adaptive_fix", seed, base / f"adaptive_fix_seed{seed}"))
    for seed in SEEDS:
        for b in GRID_B_VALUES:
            tag = B_TAG[b]
            all_experiments.append((f"grid_b{b}", seed, base / f"grid_b{tag}_seed{seed}"))

    print(f"| {'Experiment':<30} | {'Status':<30} |")
    print(f"|{'-'*32}|{'-'*32}|")
    for name, seed, exp_dir in all_experiments:
        status = get_training_status(exp_dir)
        print(f"| {name}_seed{seed:<24} | {status:<30} |")

    # ── Section 2: Eval Perplexity Collection ──
    print("\n## Eval Perplexity\n")

    results = {}
    need_eval = []

    # Uniform baselines (hardcoded)
    for seed in SEEDS:
        key = f"uniform_seed{seed}"
        results[key] = {"ppl": KNOWN_BASELINES["uniform"][seed], "src": "hardcoded"}

    # Adaptive original (hardcoded)
    for seed in SEEDS:
        key = f"adaptive_orig_seed{seed}"
        results[key] = {"ppl": KNOWN_BASELINES["adaptive_orig"][seed], "src": "hardcoded"}

    # Grid b seed123 (hardcoded)
    for b, ppl in KNOWN_BASELINES["grid_b_seed123"].items():
        key = f"grid_b{b}_seed123"
        results[key] = {"ppl": ppl, "src": "hardcoded"}

    # Adaptive fix (from files)
    for seed in SEEDS:
        exp_dir = base / f"adaptive_fix_seed{seed}"
        key = f"adaptive_fix_seed{seed}"
        ppl, src = get_ppl(exp_dir)
        results[key] = {"ppl": ppl, "src": src}
        if ppl is None and exp_dir.exists():
            need_eval.append(exp_dir)

    # Grid b seed42 (from files)
    for b in GRID_B_VALUES:
        tag = B_TAG[b]
        exp_dir = base / f"grid_b{tag}_seed42"
        key = f"grid_b{b}_seed42"
        if key not in results:
            ppl, src = get_ppl(exp_dir)
            results[key] = {"ppl": ppl, "src": src}
            if ppl is None and (exp_dir / "final").exists():
                need_eval.append(exp_dir)

    # Grid b seed456 (from files, if they exist)
    for b in GRID_B_VALUES:
        tag = B_TAG[b]
        exp_dir = base / f"grid_b{tag}_seed456"
        key = f"grid_b{b}_seed456"
        if key not in results:
            ppl, src = get_ppl(exp_dir)
            results[key] = {"ppl": ppl, "src": src}

    # ── Section 3: Comparison Table ──
    print("### Uniform Baselines\n")
    print(f"| {'Seed':<8} | {'PPL':<12} | {'Source':<15} |")
    print(f"|{'-'*10}|{'-'*14}|{'-'*17}|")
    uniform_ppls = []
    for seed in SEEDS:
        r = results[f"uniform_seed{seed}"]
        print(f"| {seed:<8} | {fmt_ppl(r['ppl']):<12} | {r['src']:<15} |")
        uniform_ppls.append(r["ppl"])
    u_mean, u_std = mean_std(uniform_ppls)
    print(f"| {'mean':<8} | {fmt_ppl(u_mean):<12} | {'±' + f'{u_std:.3f}' if u_std else '':<15} |")

    # Grid-b table
    print("\n### Grid-b Results\n")
    header_seeds = [s for s in SEEDS]
    print(f"| {'b':<6} |", end="")
    for s in header_seeds:
        print(f" {'seed' + str(s):<12} |", end="")
    print(f" {'mean':<12} |")
    print(f"|{'-'*8}|" + f"{'-'*14}|" * len(header_seeds) + f"{'-'*14}|")

    grid_best_per_seed = {}
    for b in GRID_B_VALUES:
        row_ppls = []
        print(f"| {b:<6.1f} |", end="")
        for seed in header_seeds:
            key = f"grid_b{b}_seed{seed}"
            r = results.get(key, {"ppl": None, "src": "missing"})
            ppl = r["ppl"]
            row_ppls.append(ppl)
            print(f" {fmt_ppl(ppl):<12} |", end="")
        m, _ = mean_std(row_ppls)
        print(f" {fmt_ppl(m):<12} |")

        for i, seed in enumerate(header_seeds):
            ppl = row_ppls[i]
            if ppl is not None:
                if seed not in grid_best_per_seed or ppl < grid_best_per_seed[seed][1]:
                    grid_best_per_seed[seed] = (b, ppl)

    print("\n  Best grid-b per seed:")
    grid_best_ppls = []
    for seed in SEEDS:
        if seed in grid_best_per_seed:
            b, ppl = grid_best_per_seed[seed]
            print(f"    seed {seed}: b={b:.1f} → PPL={ppl:.3f}")
            grid_best_ppls.append(ppl)
        else:
            print(f"    seed {seed}: no data")
            grid_best_ppls.append(None)

    # Adaptive fix table
    print("\n### Adaptive Fix Results\n")
    print(f"| {'Seed':<8} | {'PPL':<12} | {'Source':<15} | {'vs uniform':<12} | {'vs grid-best':<12} |")
    print(f"|{'-'*10}|{'-'*14}|{'-'*17}|{'-'*14}|{'-'*14}|")
    afix_ppls = []
    for seed in SEEDS:
        r = results[f"adaptive_fix_seed{seed}"]
        u_ppl = KNOWN_BASELINES["uniform"][seed]
        gb_ppl = grid_best_per_seed.get(seed, (None, None))[1]
        print(f"| {seed:<8} | {fmt_ppl(r['ppl'], r['src']):<12} | {r['src']:<15} | {pct_diff(r['ppl'], u_ppl):<12} | {pct_diff(r['ppl'], gb_ppl):<12} |")
        afix_ppls.append(r["ppl"])
    af_mean, af_std = mean_std(afix_ppls)
    print(f"| {'mean':<8} | {fmt_ppl(af_mean):<12} | {'±' + f'{af_std:.3f}' if af_std else '':<15} |              |              |")

    # Adaptive original comparison
    print("\n### Adaptive Original (n_min=3) Comparison\n")
    print(f"| {'Seed':<8} | {'adaptive_orig':<15} | {'adaptive_fix':<15} | {'delta':<10} |")
    print(f"|{'-'*10}|{'-'*17}|{'-'*17}|{'-'*12}|")
    aorig_ppls = []
    for seed in SEEDS:
        orig = KNOWN_BASELINES["adaptive_orig"][seed]
        fix = results[f"adaptive_fix_seed{seed}"]["ppl"]
        aorig_ppls.append(orig)
        delta = f"{fix - orig:+.3f}" if fix is not None else "N/A"
        print(f"| {seed:<8} | {orig:<15.3f} | {fmt_ppl(fix):<15} | {delta:<10} |")

    # ── Section 4: MVP Judgment ──
    print("\n" + "=" * 78)
    print("  MVP JUDGMENT")
    print("=" * 78)

    gb_mean, gb_std = mean_std(grid_best_ppls)

    print(f"\n  Uniform mean PPL:       {fmt_ppl(u_mean)} ± {u_std:.3f}" if u_mean else "")
    print(f"  Grid-best mean PPL:     {fmt_ppl(gb_mean)} ± {gb_std:.3f}" if gb_mean else "")
    print(f"  Adaptive-fix mean PPL:  {fmt_ppl(af_mean)} ± {af_std:.3f}" if af_mean else "")

    if af_mean is None:
        print("\n  ⚠ CANNOT JUDGE: adaptive_fix PPL data missing.")
        print("  Run eval_perplexity.py on completed adaptive_fix checkpoints.")
    elif gb_mean is None:
        print("\n  ⚠ CANNOT JUDGE: grid-best PPL data incomplete.")
    else:
        threshold = 0.005  # 0.5%
        diff = af_mean - gb_mean
        rel_diff = diff / gb_mean if gb_mean else 0

        print(f"\n  Criterion: adaptive_fix mean ≤ grid-best mean (or gap < 0.5%)")
        print(f"  Difference: {diff:+.4f} ({rel_diff:+.4f} = {rel_diff*100:+.3f}%)")

        if af_mean <= gb_mean:
            print(f"\n  ✅ MVP PASS — adaptive_fix ({af_mean:.3f}) ≤ grid-best ({gb_mean:.3f})")
        elif abs(rel_diff) < threshold:
            print(f"\n  ✅ MVP PASS (marginal) — gap {rel_diff*100:.3f}% < 0.5% threshold")
        else:
            print(f"\n  ❌ MVP FAIL — adaptive_fix ({af_mean:.3f}) > grid-best ({gb_mean:.3f}) by {rel_diff*100:.3f}%")

    # ── Section 5: b* Trajectory Analysis ──
    print("\n" + "=" * 78)
    print("  b* TRAJECTORY ANALYSIS (adaptive_fix)")
    print("=" * 78)

    for seed in SEEDS:
        exp_dir = base / f"adaptive_fix_seed{seed}"
        records = load_b_star_trajectory(exp_dir)
        if not records:
            print(f"\n  seed {seed}: no step_metrics.jsonl found")
            continue

        b_vals = [r["b"] for r in records if "b" in r]
        steps = [r["step"] for r in records if "step" in r]
        alpha_vals = [r["alpha_eff"] for r in records if "alpha_eff" in r]

        if not b_vals:
            print(f"\n  seed {seed}: no b values in step_metrics")
            continue

        n = len(b_vals)
        b_mean = sum(b_vals) / n
        b_std = math.sqrt(sum((v - b_mean) ** 2 for v in b_vals) / max(n - 1, 1))
        b_min, b_max = min(b_vals), max(b_vals)
        b_median = sorted(b_vals)[n // 2]

        last_pct = max(1, n // 10)
        b_tail = b_vals[-last_pct:]
        b_tail_mean = sum(b_tail) / len(b_tail)

        first_pct = b_vals[:last_pct]
        b_head_mean = sum(first_pct) / len(first_pct)

        a_mean = sum(alpha_vals) / len(alpha_vals) if alpha_vals else 0

        max_step = max(steps) if steps else 0

        print(f"\n  seed {seed}: {n} records, steps 0..{max_step}")
        print(f"    b*: mean={b_mean:.3f}, std={b_std:.3f}, median={b_median:.3f}")
        print(f"    b*: min={b_min:.3f}, max={b_max:.3f}")
        print(f"    b* first 10%: mean={b_head_mean:.3f}")
        print(f"    b* last 10%:  mean={b_tail_mean:.3f}")
        print(f"    α_eff mean: {a_mean:.4f}")
        trend = "increasing" if b_tail_mean > b_head_mean * 1.1 else \
                "decreasing" if b_tail_mean < b_head_mean * 0.9 else "stable"
        print(f"    Trend: {trend}")

    # ── Section 6: Missing Eval Warning ──
    if need_eval:
        print("\n" + "=" * 78)
        print("  ⚠ EXPERIMENTS NEEDING EVAL")
        print("=" * 78)
        print("\n  The following completed experiments lack eval_results.json.")
        print("  Run: python eval_perplexity.py --model_path <path>/final\n")
        for d in need_eval:
            print(f"    {d}")

    print()


if __name__ == "__main__":
    main()
