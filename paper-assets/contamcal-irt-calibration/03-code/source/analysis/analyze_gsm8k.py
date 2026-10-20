"""GSM8K contamination specificity analysis.

Tests whether MMLU-targeted contamination transfers to GSM8K (math reasoning).
Scans eval result directories, computes dose-response deltas, and compares
GSM8K vs MMLU profiles across model families.

Input:  eval result directories containing gsm8k_results.json / eval_results.json
Output: CSV summary table + dose-response comparison plots (GSM8K vs MMLU)
        Written to --output-dir (default: analysis/results/gsm8k/)

C009: All GSM8K data must come from the same version of evaluate.py.
      Reference md5: 001a9bc23f808c47d25ef9eaeecb81f1
      Files with .old suffix are excluded (deprecated old-version outputs).
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

MODELS = {
    "qwen7b": {"display": "Qwen2.5-7B", "patterns": ["Qwen2.5-7B", "qwen7b"]},
    "qwen14b": {"display": "Qwen2.5-14B", "patterns": ["Qwen2.5-14B", "qwen14b"]},
    "gemma2": {"display": "Gemma-2-9B", "patterns": ["gemma-2-9b", "gemma2", "gemma2_9b"]},
    "olmo2": {"display": "OLMo-2-7B", "patterns": ["olmo2", "OLMo-2-7B"]},
    "phi4": {"display": "Phi-4", "patterns": ["phi-4", "phi4"]},
}

DOSAGES = ["d000", "d005", "d025", "d050", "d100"]
DOSAGE_PCTS = {"d000": 0.0, "d005": 0.5, "d025": 2.5, "d050": 5.0, "d100": 10.0}

MODEL_COLORS = {
    "qwen7b": "#1f77b4",
    "qwen14b": "#ff7f0e",
    "gemma2": "#2ca02c",
    "olmo2": "#d62728",
    "phi4": "#9467bd",
}

EVALUATE_PY_REF_MD5 = "001a9bc23f808c47d25ef9eaeecb81f1"


def check_evaluate_py_version(eval_py_path: Path) -> bool:
    """Verify evaluate.py matches the reference md5 (C009)."""
    if not eval_py_path.exists():
        return False
    md5 = hashlib.md5(eval_py_path.read_bytes()).hexdigest()
    return md5 == EVALUATE_PY_REF_MD5


def identify_model(dirname: str) -> str | None:
    dn = dirname.lower().replace("-", "").replace("_", "")
    for key, cfg in MODELS.items():
        for pat in cfg["patterns"]:
            if pat.lower().replace("-", "").replace("_", "") in dn:
                return key
    return None


def identify_dosage(dirname: str) -> str | None:
    m = re.search(r"(d\d{3})", dirname)
    return m.group(1) if m and m.group(1) in DOSAGES else None


def identify_seed(dirname: str) -> str | None:
    m = re.search(r"s(\d+)", dirname)
    return m.group(1) if m else None


def _is_old_file(path: Path) -> bool:
    """Check if any component of the path has .old suffix."""
    return any(part.endswith(".old") for part in path.parts)


def load_gsm8k_accuracy(result_dir: Path) -> float | None:
    gsm_path = result_dir / "gsm8k_results.json"
    if gsm_path.exists() and not _is_old_file(gsm_path):
        with open(gsm_path) as f:
            data = json.load(f)
        return data.get("accuracy")

    eval_path = result_dir / "eval_results.json"
    if eval_path.exists() and not _is_old_file(eval_path):
        with open(eval_path) as f:
            data = json.load(f)
        benchmarks = data.get("benchmarks", {})
        if "gsm8k" in benchmarks:
            return benchmarks["gsm8k"].get("accuracy")
    return None


def load_mmlu_accuracy(result_dir: Path) -> float | None:
    mmlu_path = result_dir / "mmlu_results.json"
    if mmlu_path.exists() and not _is_old_file(mmlu_path):
        with open(mmlu_path) as f:
            data = json.load(f)
        return data.get("accuracy")

    eval_path = result_dir / "eval_results.json"
    if eval_path.exists() and not _is_old_file(eval_path):
        with open(eval_path) as f:
            data = json.load(f)
        benchmarks = data.get("benchmarks", {})
        if "mmlu" in benchmarks:
            return benchmarks["mmlu"].get("accuracy")
    return None


def scan_results(base_dirs: list[Path], benchmark: str = "gsm8k") -> pd.DataFrame:
    """Scan directories for eval results. Returns DataFrame with model, dosage, seed, accuracy."""
    load_fn = load_gsm8k_accuracy if benchmark == "gsm8k" else load_mmlu_accuracy
    rows = []
    seen = set()

    for base_dir in base_dirs:
        if not base_dir.exists():
            continue
        for subdir in sorted(base_dir.iterdir()):
            if not subdir.is_dir():
                continue
            model = identify_model(subdir.name)
            dosage = identify_dosage(subdir.name)
            if model is None or dosage is None:
                continue

            acc = load_fn(subdir)
            if acc is None:
                continue

            seed = identify_seed(subdir.name) or "42"
            key = (model, dosage, seed)
            if key in seen:
                continue
            seen.add(key)

            rows.append({
                "model": model,
                "model_display": MODELS[model]["display"],
                "dosage": dosage,
                "dosage_pct": DOSAGE_PCTS[dosage],
                "seed": seed,
                "accuracy": acc,
                "source_dir": str(subdir),
            })

    return pd.DataFrame(rows)


def compute_deltas(df: pd.DataFrame) -> pd.DataFrame:
    """Add delta_acc column: acc(d_i) - acc(d000) for same model+seed."""
    if df.empty:
        return df
    df = df.copy()
    df["delta_acc"] = np.nan
    for (model, seed), grp in df.groupby(["model", "seed"]):
        baseline = grp.loc[grp["dosage"] == "d000", "accuracy"]
        if baseline.empty:
            continue
        base_val = baseline.iloc[0]
        mask = (df["model"] == model) & (df["seed"] == seed)
        df.loc[mask, "delta_acc"] = df.loc[mask, "accuracy"] - base_val
    return df


def plot_dose_response_comparison(gsm8k_df: pd.DataFrame, mmlu_df: pd.DataFrame,
                                  output_path: Path):
    """Side-by-side dose-response: GSM8K (left) vs MMLU (right)."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

    for ax, df, title in [(axes[0], gsm8k_df, "GSM8K (math)"),
                          (axes[1], mmlu_df, "MMLU (knowledge)")]:
        if df.empty:
            ax.text(0.5, 0.5, "No data", ha="center", va="center",
                    transform=ax.transAxes, fontsize=14, color="gray")
            ax.set_title(title)
            continue

        for model in sorted(df["model"].unique()):
            mdf = df[df["model"] == model].sort_values("dosage_pct")
            seeds = mdf["seed"].unique()
            for seed in seeds:
                sdf = mdf[mdf["seed"] == seed]
                label = MODELS[model]["display"] if seed == seeds[0] else None
                ax.plot(sdf["dosage_pct"], sdf["delta_acc"] * 100,
                        "o-", color=MODEL_COLORS.get(model, "gray"),
                        label=label, markersize=5, linewidth=1.5,
                        alpha=0.7 if len(seeds) > 1 else 1.0)

        ax.axhline(0, color="black", linewidth=0.5, linestyle="--")
        ax.set_title(title, fontsize=13, fontweight="bold")
        ax.set_xlabel("Contamination dosage (%)")
        ax.set_xticks([0, 0.5, 2.5, 5.0, 10.0])

    axes[0].set_ylabel("Δ Accuracy (pp) relative to d000")
    axes[1].legend(fontsize=9, loc="upper left")

    fig.suptitle("Contamination Specificity: MMLU dosage → GSM8K vs MMLU",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {output_path}")


def plot_delta_overlay(gsm8k_df: pd.DataFrame, mmlu_df: pd.DataFrame,
                       output_path: Path):
    """Per-model overlay: GSM8K (dashed) vs MMLU (solid) delta on same axes."""
    models_with_data = sorted(
        set(gsm8k_df["model"].unique()) | set(mmlu_df["model"].unique())
    )
    if not models_with_data:
        return

    n = len(models_with_data)
    cols = min(n, 3)
    rows = (n + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4 * rows), squeeze=False)

    for idx, model in enumerate(models_with_data):
        ax = axes[idx // cols][idx % cols]
        display = MODELS[model]["display"]
        color = MODEL_COLORS.get(model, "gray")

        for df, style, label in [(mmlu_df, "-", "MMLU"),
                                 (gsm8k_df, "--", "GSM8K")]:
            mdf = df[(df["model"] == model)].sort_values("dosage_pct")
            if mdf.empty:
                continue
            for seed in sorted(mdf["seed"].unique()):
                sdf = mdf[mdf["seed"] == seed]
                lbl = f"{label} (s{seed})" if len(mdf["seed"].unique()) > 1 else label
                ax.plot(sdf["dosage_pct"], sdf["delta_acc"] * 100,
                        style, color=color, label=lbl, markersize=4,
                        marker="o", linewidth=1.5)

        ax.axhline(0, color="black", linewidth=0.5, linestyle=":")
        ax.set_title(display, fontsize=12, fontweight="bold")
        ax.set_xlabel("Dosage (%)")
        ax.set_ylabel("Δ Accuracy (pp)")
        ax.set_xticks([0, 0.5, 2.5, 5.0, 10.0])
        ax.legend(fontsize=8)

    for idx in range(n, rows * cols):
        axes[idx // cols][idx % cols].set_visible(False)

    fig.suptitle("Per-Model: MMLU vs GSM8K Dose-Response", fontsize=14,
                 fontweight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="GSM8K contamination specificity analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python analyze_gsm8k.py
  python analyze_gsm8k.py --gsm8k-dirs /path/to/eval_results --mmlu-dirs /path/to/eval_results_v2
  python analyze_gsm8k.py --output-dir /tmp/gsm8k_analysis
""")
    parser.add_argument("--data-source-dir", type=Path,
                        default=None,
                        help="Unified data source directory (overrides --gsm8k-dirs). "
                             "Default: scan legacy dirs. Use this to point at "
                             "cqa1-aligned data exclusively.")
    parser.add_argument("--gsm8k-dirs", nargs="+", type=Path,
                        default=[
                            Path("/root/autodl-tmp/exp001/eval_results"),
                            Path("/root/autodl-tmp/exp001/eval_results_v2"),
                            Path("/root/autodl-tmp/exp001/eval_results_14b"),
                            Path("/root/autodl-tmp/exp001/eval_results_cross_family"),
                        ],
                        help="Directories to scan for GSM8K eval results")
    parser.add_argument("--mmlu-dirs", nargs="+", type=Path,
                        default=[
                            Path("/root/autodl-tmp/exp001/eval_results_v2"),
                            Path("/root/autodl-tmp/exp001/eval_results"),
                            Path("/root/autodl-tmp/exp001/eval_results_14b"),
                            Path("/root/autodl-tmp/exp001/eval_results_cross_family"),
                        ],
                        help="Directories to scan for MMLU eval results (comparison)")
    parser.add_argument("--output-dir", type=Path,
                        default=Path("/root/contamcal-irt-calibration/analysis/results/gsm8k"),
                        help="Output directory for CSV and plots")
    parser.add_argument("--check-evaluate-py", type=Path, default=None,
                        help="Path to evaluate.py to verify md5 (C009)")
    args = parser.parse_args()

    if args.data_source_dir is not None:
        args.gsm8k_dirs = [args.data_source_dir]
        print(f"[C009] Data source override: {args.data_source_dir}")

    if args.check_evaluate_py:
        ok = check_evaluate_py_version(args.check_evaluate_py)
        status = "PASS" if ok else "FAIL"
        md5 = hashlib.md5(args.check_evaluate_py.read_bytes()).hexdigest() if args.check_evaluate_py.exists() else "NOT_FOUND"
        print(f"[C009] evaluate.py version check: {status} (md5={md5}, ref={EVALUATE_PY_REF_MD5})")
        if not ok:
            print("[C009] WARNING: evaluate.py version mismatch! Results may be invalid.", file=sys.stderr)

    args.output_dir.mkdir(parents=True, exist_ok=True)

    print(f"[C009] GSM8K data sources: {[str(d) for d in args.gsm8k_dirs]}")
    print(f"[C009] MMLU data sources:  {[str(d) for d in args.mmlu_dirs]}")
    print(f"[C009] Files with .old suffix will be excluded.")
    print()
    print("Scanning GSM8K results...")
    gsm8k_df = scan_results(args.gsm8k_dirs, benchmark="gsm8k")
    gsm8k_df = compute_deltas(gsm8k_df)

    print("Scanning MMLU results...")
    mmlu_df = scan_results(args.mmlu_dirs, benchmark="mmlu")
    mmlu_df = compute_deltas(mmlu_df)

    print(f"\nGSM8K: found {len(gsm8k_df)} results "
          f"({gsm8k_df['model'].nunique() if not gsm8k_df.empty else 0} models)")
    if not gsm8k_df.empty:
        for model in sorted(gsm8k_df["model"].unique()):
            doses = sorted(gsm8k_df[gsm8k_df["model"] == model]["dosage"].unique())
            print(f"  {MODELS[model]['display']}: {', '.join(doses)}")

    print(f"\nMMLU:  found {len(mmlu_df)} results "
          f"({mmlu_df['model'].nunique() if not mmlu_df.empty else 0} models)")

    # Save CSVs
    cols = ["model_display", "dosage", "dosage_pct", "seed", "accuracy", "delta_acc"]
    if not gsm8k_df.empty:
        csv_path = args.output_dir / "gsm8k_summary.csv"
        gsm8k_df[cols].sort_values(["model_display", "seed", "dosage"]).to_csv(
            csv_path, index=False, float_format="%.6f")
        print(f"\n  Saved: {csv_path}")

    if not mmlu_df.empty:
        csv_path = args.output_dir / "mmlu_summary.csv"
        mmlu_df[cols].sort_values(["model_display", "seed", "dosage"]).to_csv(
            csv_path, index=False, float_format="%.6f")
        print(f"  Saved: {csv_path}")

    # Combined CSV
    if not gsm8k_df.empty or not mmlu_df.empty:
        combined = []
        if not gsm8k_df.empty:
            g = gsm8k_df[cols].copy()
            g["benchmark"] = "gsm8k"
            combined.append(g)
        if not mmlu_df.empty:
            m = mmlu_df[cols].copy()
            m["benchmark"] = "mmlu"
            combined.append(m)
        combined_df = pd.concat(combined, ignore_index=True)
        csv_path = args.output_dir / "gsm8k_vs_mmlu_combined.csv"
        combined_df.sort_values(
            ["benchmark", "model_display", "seed", "dosage"]
        ).to_csv(csv_path, index=False, float_format="%.6f")
        print(f"  Saved: {csv_path}")

    # Plots
    print("\nGenerating plots...")
    if not gsm8k_df.empty or not mmlu_df.empty:
        plot_dose_response_comparison(
            gsm8k_df, mmlu_df,
            args.output_dir / "dose_response_gsm8k_vs_mmlu.png")
        plot_delta_overlay(
            gsm8k_df, mmlu_df,
            args.output_dir / "per_model_gsm8k_vs_mmlu.png")

    # Print summary table
    if not gsm8k_df.empty:
        print("\n--- GSM8K Dose-Response Summary ---")
        pivot = gsm8k_df.pivot_table(
            index="model_display", columns="dosage", values="accuracy",
            aggfunc="mean"
        )
        pivot_delta = gsm8k_df.pivot_table(
            index="model_display", columns="dosage", values="delta_acc",
            aggfunc="mean"
        )
        print("\nAccuracy:")
        print(pivot.to_string(float_format=lambda x: f"{x:.4f}"))
        print("\nΔ Accuracy (vs d000):")
        print(pivot_delta.to_string(float_format=lambda x: f"{x:+.4f}" if pd.notna(x) else ""))

    if gsm8k_df.empty:
        print("\nNo GSM8K results found yet. Re-run after evals complete.")

    print("\nDone.")


if __name__ == "__main__":
    main()
