#!/usr/bin/env python3
"""
Post-eval pipeline: Table 3 fill + Figure 2 update + LPM regression.

Run after all 3 CWM multi-seed evals complete (Qwen s123/s456, DS s123).

Usage:
  python pipeline_post_eval.py \
    --qwen_s42_acc 65.17 \
    --qwen_s123_acc <from eval> \
    --qwen_s456_acc <from eval> \
    --ds_s42_acc 61.49 \
    --ds_s123_acc <from eval> \
    --ds_s456_acc 56.11 \
    [--dry_run]

Steps:
  1. Compute 3-seed mean±std for Qwen CWM and DS CWM
  2. Replace \tbd{} in experiments.tex Table 3
  3. Update plot_figure2_v2.py DATA dict with multi-seed values
  4. Print commands to run LPM regression (run_w5_full_regression.py)
"""

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEX_PATH = PROJECT_ROOT / "docs" / "paper" / "experiments.tex"
FIG2_PATH = PROJECT_ROOT / "plot_figure2_v2.py"


def compute_stats(values: list[float]) -> tuple[float, float]:
    n = len(values)
    mean = sum(values) / n
    if n < 2:
        return mean, 0.0
    var = sum((x - mean) ** 2 for x in values) / (n - 1)
    std = var ** 0.5
    return round(mean, 2), round(std, 2)


def fill_table3(tex: str, qwen_str: str, ds_str: str, dry_run: bool) -> str:
    lines = tex.split("\n")
    tbd_count = 0
    for i, line in enumerate(lines):
        if r"\tbd{}" in line:
            tbd_count += 1
            if "Qwen3-8B" in line:
                lines[i] = line.replace(r"\tbd{}", qwen_str)
                print(f"  Table 3 line {i+1}: Qwen CWM -> {qwen_str}")
            elif "DeepSeek" in line:
                lines[i] = line.replace(r"\tbd{}", ds_str)
                print(f"  Table 3 line {i+1}: DS CWM -> {ds_str}")
            else:
                print(f"  WARNING: \\tbd{{}} on line {i+1} not matched to model")
    if tbd_count == 0:
        print("  WARNING: No \\tbd{} found — already filled?")
    return "\n".join(lines)


def update_figure2(fig2: str, qwen_mean: float, qwen_std: float,
                   ds_mean: float, ds_std: float) -> str:
    # Replace CWM repo qwen placeholder
    fig2 = re.sub(
        r'("CWM":\s*\{"qwen":\s*\{"mean":\s*)[0-9.]+(\s*,\s*"std":\s*)[0-9.]+(\s*,\s*"n_seeds":\s*)\d+',
        rf'\g<1>{qwen_mean}\g<2>{qwen_std}\g<3>3',
        fig2
    )
    # Replace CWM repo deepseek placeholder
    fig2 = re.sub(
        r'("deepseek":\s*\{"mean":\s*)[0-9.]+(\s*,\s*"std":\s*)[0-9.]+(\s*,\s*"n_seeds":\s*)\d+(\}\},)',
        rf'\g<1>{ds_mean}\g<2>{ds_std}\g<3>3\4',
        fig2
    )
    print(f"  Figure 2: Qwen CWM -> {qwen_mean}±{qwen_std} (3 seeds)")
    print(f"  Figure 2: DS CWM -> {ds_mean}±{ds_std} (3 seeds)")
    return fig2


def update_caption(tex: str) -> str:
    old = r"\cwm{} multi-seed runs in progress."
    new = r"\cwm{}: 3 seeds (42/123/456)."
    if old in tex:
        tex = tex.replace(old, new)
        print("  Caption: updated CWM status note")
    return tex


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--qwen_s42_acc", type=float, default=65.17)
    p.add_argument("--qwen_s123_acc", type=float, required=True)
    p.add_argument("--qwen_s456_acc", type=float, required=True)
    p.add_argument("--ds_s42_acc", type=float, default=61.49)
    p.add_argument("--ds_s123_acc", type=float, required=True)
    p.add_argument("--ds_s456_acc", type=float, default=56.11)
    p.add_argument("--dry_run", action="store_true",
                   help="Print changes without writing files")
    args = p.parse_args()

    # Step 1: Compute stats
    qwen_vals = [args.qwen_s42_acc, args.qwen_s123_acc, args.qwen_s456_acc]
    ds_vals = [args.ds_s42_acc, args.ds_s123_acc, args.ds_s456_acc]

    qwen_mean, qwen_std = compute_stats(qwen_vals)
    ds_mean, ds_std = compute_stats(ds_vals)

    print(f"=== Step 1: CWM 3-seed stats ===")
    print(f"  Qwen: {qwen_vals} -> {qwen_mean} ± {qwen_std}")
    print(f"  DS:   {ds_vals} -> {ds_mean} ± {ds_std}")

    # Format for Table 3 (match existing format: "84.83 $\pm$ 0.67")
    qwen_tex = f"{qwen_mean:.2f} $\\pm$ {qwen_std:.2f}"
    ds_tex = f"{ds_mean:.2f} $\\pm$ {ds_std:.2f}"

    # Step 2: Fill Table 3
    print(f"\n=== Step 2: Table 3 ===")
    tex = TEX_PATH.read_text()
    tex = fill_table3(tex, qwen_tex, ds_tex, args.dry_run)
    tex = update_caption(tex)
    if not args.dry_run:
        TEX_PATH.write_text(tex)
        print("  -> Written to experiments.tex")

    # Step 3: Update Figure 2
    print(f"\n=== Step 3: Figure 2 ===")
    fig2 = FIG2_PATH.read_text()
    fig2 = update_figure2(fig2, qwen_mean, qwen_std, ds_mean, ds_std)
    if not args.dry_run:
        FIG2_PATH.write_text(fig2)
        print("  -> Written to plot_figure2_v2.py")

    # Step 4: LPM regression command
    print(f"\n=== Step 4: LPM regression ===")
    print("  Run on server (after eval results copied):")
    print("  python run_w5_full_regression.py \\")
    print("    --eval_dirs <comma-separated eval result dirs> \\")
    print("    --verify --output_dir artifacts/w5_full_regression")
    print()
    print("  Eval result dirs are at: /root/autodl-tmp/eval_results/")
    print("  Include all CLS + CWM + TRAJ func + repo eval dirs")

    # Summary
    print(f"\n=== Summary ===")
    print(f"  Qwen CWM repo: {qwen_mean} ± {qwen_std} (seeds: {qwen_vals})")
    print(f"  DS CWM repo:   {ds_mean} ± {ds_std} (seeds: {ds_vals})")
    print(f"  CLS-CWM gap (Qwen): {84.83 - qwen_mean:.2f}pp")
    print(f"  CLS-CWM gap (DS):   {84.38 - ds_mean:.2f}pp")
    if not args.dry_run:
        print("  Files updated: experiments.tex, plot_figure2_v2.py")
        print("  Next: latexmk -pdf main.tex && python plot_figure2_v2.py")


if __name__ == "__main__":
    main()
