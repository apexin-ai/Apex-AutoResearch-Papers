"""Treated vs Untreated Item Analysis for contamination causal design."""

import argparse
import json
import os
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from scipy import stats

plt.rcParams.update({
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})


MODELS = ["gemma2", "olmo2", "phi4", "qwen14b", "qwen7b"]
MODEL_DISPLAY = {
    "gemma2": "Gemma-2-9B",
    "olmo2": "OLMo-2-7B",
    "phi4": "Phi-4",
    "qwen14b": "Qwen2.5-14B",
    "qwen7b": "Qwen2.5-7B",
}
DOSAGES = ["d005", "d025", "d050", "d100"]
DOSAGE_PCTS = {"d005": 0.5, "d025": 2.5, "d050": 5.0, "d100": 10.0}
BENCHMARKS = ["mmlu", "arc_challenge"]


def load_contamination_labels(sft_dir, benchmark, dosage):
    path = Path(sft_dir) / f"contamination_labels_{benchmark}_{dosage}.json"
    with open(path) as f:
        data = json.load(f)
    return np.array(data["labels"], dtype=bool)


def load_correctness(eval_dir, model, dosage, benchmark):
    path = Path(eval_dir) / f"{model}_{dosage}" / "correctness_matrix.json"
    with open(path) as f:
        data = json.load(f)
    return np.array(data[benchmark], dtype=bool)


def bootstrap_ci(x, n_boot=10000, ci=0.95, seed=42):
    rng = np.random.RandomState(seed)
    means = np.array([np.mean(rng.choice(x, size=len(x), replace=True)) for _ in range(n_boot)])
    alpha = (1 - ci) / 2
    return np.percentile(means, [alpha * 100, (1 - alpha) * 100])


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

    # ── 1. Main treated vs untreated summary ──
    rows = []
    for benchmark in BENCHMARKS:
        for model in MODELS:
            baseline = load_correctness(eval_dir, model, "d000", benchmark)
            for dosage in DOSAGES:
                labels = load_contamination_labels(sft_dir, benchmark, dosage)
                treated_mask = labels
                untreated_mask = ~labels
                dosed = load_correctness(eval_dir, model, dosage, benchmark)

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

                # DiD: (treated_delta - untreated_delta) bootstrap
                did = treated_delta - untreated_delta
                did_arr = treated_delta_arr[:min(len(treated_delta_arr), len(untreated_delta_arr))]
                # Proper DiD bootstrap
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

                rows.append({
                    "benchmark": benchmark,
                    "model": model,
                    "model_display": MODEL_DISPLAY[model],
                    "dosage": dosage,
                    "dosage_pct": DOSAGE_PCTS[dosage],
                    "n_treated": int(treated_mask.sum()),
                    "n_untreated": int(untreated_mask.sum()),
                    "treated_acc_base": np.mean(treated_base),
                    "treated_acc_dose": np.mean(treated_dose),
                    "treated_delta": treated_delta,
                    "treated_ci_lo": t_lo,
                    "treated_ci_hi": t_hi,
                    "treated_p": t_p,
                    "untreated_acc_base": np.mean(untreated_base),
                    "untreated_acc_dose": np.mean(untreated_dose),
                    "untreated_delta": untreated_delta,
                    "untreated_ci_lo": u_lo,
                    "untreated_ci_hi": u_hi,
                    "untreated_p": u_p,
                    "did": did,
                    "did_ci_lo": did_lo,
                    "did_ci_hi": did_hi,
                    "did_p": did_p,
                    "verdict": verdict,
                })

    df = pd.DataFrame(rows)
    df.to_csv(Path(output_dir) / "treated_untreated_summary.csv", index=False)
    print(f"Saved summary: {len(df)} rows")

    # ── 2. Main figure: treated vs untreated delta by dosage ──
    for benchmark in BENCHMARKS:
        bdf = df[df["benchmark"] == benchmark]
        fig, axes = plt.subplots(1, 5, figsize=(20, 4), sharey=True)
        fig.suptitle(
            f"Treated vs Untreated Accuracy Delta — {benchmark.upper().replace('_', ' ')}",
            fontsize=14, fontweight="bold",
        )

        for ax, model in zip(axes, MODELS):
            mdf = bdf[bdf["model"] == model].sort_values("dosage_pct")
            x = np.arange(len(mdf))
            w = 0.35

            bars_t = ax.bar(x - w / 2, mdf["treated_delta"].values, w,
                            label="Treated", color="#e74c3c", alpha=0.85)
            bars_u = ax.bar(x + w / 2, mdf["untreated_delta"].values, w,
                            label="Untreated", color="#3498db", alpha=0.85)

            # Error bars
            t_err = np.array([
                mdf["treated_delta"].values - mdf["treated_ci_lo"].values,
                mdf["treated_ci_hi"].values - mdf["treated_delta"].values
            ])
            u_err = np.array([
                mdf["untreated_delta"].values - mdf["untreated_ci_lo"].values,
                mdf["untreated_ci_hi"].values - mdf["untreated_delta"].values
            ])
            ax.errorbar(x - w / 2, mdf["treated_delta"].values, yerr=t_err,
                        fmt="none", ecolor="black", capsize=3, linewidth=1)
            ax.errorbar(x + w / 2, mdf["untreated_delta"].values, yerr=u_err,
                        fmt="none", ecolor="black", capsize=3, linewidth=1)

            ax.axhline(0, color="gray", linestyle="--", linewidth=0.8)
            ax.set_xticks(x)
            ax.set_xticklabels([f"{v}%" for v in mdf["dosage_pct"].values])
            ax.set_title(MODEL_DISPLAY[model], fontsize=11)
            ax.set_xlabel("Dosage")
            if ax == axes[0]:
                ax.set_ylabel("Δ Accuracy (vs d000)")
            ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:+.3f}"))

            # Annotate verdicts
            for i, (_, row) in enumerate(mdf.iterrows()):
                y_pos = max(row["treated_delta"], row["untreated_delta"]) + 0.005
                if row["did_p"] < 0.05:
                    ax.text(i, y_pos, "★", ha="center", fontsize=10, color="#e74c3c")

        axes[-1].legend(loc="upper right", fontsize=9)
        fig.tight_layout(rect=[0, 0, 1, 0.92])
        out_path = Path(output_dir) / f"treated_untreated_{benchmark}.pdf"
        fig.savefig(out_path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"Saved plot: {out_path}")

    # ── 3. Difficulty interaction analysis ──
    diff_rows = []
    for benchmark in BENCHMARKS:
        # Compute item difficulty = mean accuracy across all 5 families at d000
        baselines = []
        for model in MODELS:
            baselines.append(load_correctness(eval_dir, model, "d000", benchmark).astype(float))
        item_difficulty = np.mean(baselines, axis=0)  # higher = easier

        difficulty_bins = np.full(len(item_difficulty), "medium", dtype=object)
        difficulty_bins[item_difficulty > 0.7] = "easy"
        difficulty_bins[item_difficulty < 0.4] = "hard"

        for dosage in DOSAGES:
            labels = load_contamination_labels(sft_dir, benchmark, dosage)
            for model in MODELS:
                baseline = load_correctness(eval_dir, model, "d000", benchmark).astype(float)
                dosed = load_correctness(eval_dir, model, dosage, benchmark).astype(float)
                delta = dosed - baseline

                for dbin in ["easy", "medium", "hard"]:
                    bin_mask = difficulty_bins == dbin
                    for group, gmask in [("treated", labels), ("untreated", ~labels)]:
                        combined = bin_mask & gmask
                        n = combined.sum()
                        if n == 0:
                            continue
                        mean_delta = np.mean(delta[combined])
                        ci_lo, ci_hi = bootstrap_ci(delta[combined])
                        diff_rows.append({
                            "benchmark": benchmark,
                            "model": model,
                            "model_display": MODEL_DISPLAY[model],
                            "dosage": dosage,
                            "dosage_pct": DOSAGE_PCTS[dosage],
                            "difficulty_bin": dbin,
                            "group": group,
                            "n_items": int(n),
                            "mean_delta": mean_delta,
                            "ci_lo": ci_lo,
                            "ci_hi": ci_hi,
                        })

    diff_df = pd.DataFrame(diff_rows)
    diff_df.to_csv(Path(output_dir) / "difficulty_interaction.csv", index=False)
    print(f"Saved difficulty interaction: {len(diff_df)} rows")

    # ── 4. Difficulty interaction plot (d025, MMLU focus) ──
    for benchmark in BENCHMARKS:
        subset = diff_df[
            (diff_df["benchmark"] == benchmark) & (diff_df["dosage"] == "d025")
        ]
        if subset.empty:
            continue

        fig, axes = plt.subplots(1, 5, figsize=(20, 4), sharey=True)
        fig.suptitle(
            f"Difficulty × Contamination Interaction (d025) — {benchmark.upper().replace('_', ' ')}",
            fontsize=14, fontweight="bold",
        )
        bin_order = ["hard", "medium", "easy"]
        colors = {"treated": "#e74c3c", "untreated": "#3498db"}

        for ax, model in zip(axes, MODELS):
            mdf = subset[subset["model"] == model]
            x = np.arange(len(bin_order))
            w = 0.35

            for gi, group in enumerate(["treated", "untreated"]):
                gdf = mdf[mdf["group"] == group].set_index("difficulty_bin")
                vals = [gdf.loc[b, "mean_delta"] if b in gdf.index else 0 for b in bin_order]
                ci_los = [gdf.loc[b, "ci_lo"] if b in gdf.index else 0 for b in bin_order]
                ci_his = [gdf.loc[b, "ci_hi"] if b in gdf.index else 0 for b in bin_order]
                offset = -w / 2 + gi * w
                err = np.array([
                    [v - lo for v, lo in zip(vals, ci_los)],
                    [hi - v for v, hi in zip(vals, ci_his)],
                ])
                ax.bar(x + offset, vals, w, label=group.capitalize(),
                       color=colors[group], alpha=0.85)
                ax.errorbar(x + offset, vals, yerr=err,
                            fmt="none", ecolor="black", capsize=3, linewidth=1)

            ax.axhline(0, color="gray", linestyle="--", linewidth=0.8)
            ax.set_xticks(x)
            ax.set_xticklabels([b.capitalize() for b in bin_order])
            ax.set_title(MODEL_DISPLAY[model], fontsize=11)
            ax.set_xlabel("Item Difficulty")
            if ax == axes[0]:
                ax.set_ylabel("Δ Accuracy (vs d000)")
            ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:+.3f}"))

        axes[-1].legend(loc="upper right", fontsize=9)
        fig.tight_layout(rect=[0, 0, 1, 0.92])
        out_path = Path(output_dir) / f"difficulty_interaction_{benchmark}.pdf"
        fig.savefig(out_path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"Saved difficulty plot: {out_path}")

    # ── 5. Dose-response overlay (treated DiD across dosages) ──
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    for ax, benchmark in zip(axes, BENCHMARKS):
        bdf = df[df["benchmark"] == benchmark]
        for model in MODELS:
            mdf = bdf[bdf["model"] == model].sort_values("dosage_pct")
            ax.plot(mdf["dosage_pct"].values, mdf["did"].values,
                    marker="o", label=MODEL_DISPLAY[model], linewidth=2)
            ax.fill_between(mdf["dosage_pct"].values,
                            mdf["did_ci_lo"].values, mdf["did_ci_hi"].values,
                            alpha=0.1)
        ax.axhline(0, color="gray", linestyle="--", linewidth=0.8)
        ax.set_xlabel("Dosage (%)")
        ax.set_ylabel("DiD (Treated Δ − Untreated Δ)")
        ax.set_title(benchmark.upper().replace("_", " "))
        ax.legend(fontsize=9)
    fig.suptitle("Difference-in-Differences by Dosage", fontsize=14, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(Path(output_dir) / "did_dose_response.pdf", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved DiD dose-response plot")

    # ── 6. Print key findings ──
    print("\n" + "=" * 80)
    print("KEY FINDINGS")
    print("=" * 80)

    for benchmark in BENCHMARKS:
        print(f"\n── {benchmark.upper().replace('_', ' ')} ──")
        bdf = df[df["benchmark"] == benchmark]
        d025 = bdf[bdf["dosage"] == "d025"]
        for _, row in d025.iterrows():
            sig_t = "***" if row["treated_p"] < 0.001 else "**" if row["treated_p"] < 0.01 else "*" if row["treated_p"] < 0.05 else "ns"
            sig_u = "***" if row["untreated_p"] < 0.001 else "**" if row["untreated_p"] < 0.01 else "*" if row["untreated_p"] < 0.05 else "ns"
            sig_d = "***" if row["did_p"] < 0.001 else "**" if row["did_p"] < 0.01 else "*" if row["did_p"] < 0.05 else "ns"
            print(
                f"  {row['model_display']:>16s}  "
                f"treated={row['treated_delta']:+.4f}({sig_t})  "
                f"untreated={row['untreated_delta']:+.4f}({sig_u})  "
                f"DiD={row['did']:+.4f}({sig_d})  "
                f"→ {row['verdict']}"
            )

    # Difficulty interaction summary for d025 MMLU
    print(f"\n── DIFFICULTY INTERACTION (d025, MMLU) ──")
    mmlu_diff = diff_df[
        (diff_df["benchmark"] == "mmlu") & (diff_df["dosage"] == "d025")
    ]
    for dbin in ["hard", "medium", "easy"]:
        bdf = mmlu_diff[mmlu_diff["difficulty_bin"] == dbin]
        t_mean = bdf[bdf["group"] == "treated"]["mean_delta"].mean()
        u_mean = bdf[bdf["group"] == "untreated"]["mean_delta"].mean()
        print(f"  {dbin:>8s}: treated_Δ={t_mean:+.4f}  untreated_Δ={u_mean:+.4f}  gap={t_mean - u_mean:+.4f}")

    return df, diff_df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sft-dir", required=True)
    parser.add_argument("--eval-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    run_analysis(args.sft_dir, args.eval_dir, args.output_dir)
