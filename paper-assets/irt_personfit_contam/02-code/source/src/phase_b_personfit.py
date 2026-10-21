"""Phase B: Compute person-fit statistics for 12 models on 5 target benchmarks."""

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent))
from person_fit import (
    compute_infit,
    compute_lz,
    compute_lz_star,
    compute_outfit,
    filter_valid_items,
)

ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS = ROOT / "artifacts"

BENCHMARK_COLS = {
    "ARC-C":            (0, 295),
    "BBH":              (295, 6806),
    "Chinese_SimpleQA": (6806, 9806),
    "GPQA_Diamond":     (9806, 10004),
    "GSM8K":            (10004, 11323),
    "HellaSwag":        (11323, 21365),
    "HumanEval":        (21365, 21529),
    "MATH":             (21529, 26529),
    "MBPP":             (26529, 27029),
    "MMLU":             (27029, 41071),
    "TheoremQA":        (41071, 41871),
}

TARGET_BENCHMARKS = ["MMLU", "HellaSwag", "GSM8K", "ARC-C", "HumanEval"]


def load_data():
    item_params = pd.read_csv(ARTIFACTS / "psn_irt_params" / "item_parameters_all.csv")
    responses = np.loadtxt(
        ARTIFACTS / "psn_irt_phase_b" / "combine.csv", delimiter=","
    )
    abilities = pd.read_csv(ARTIFACTS / "psn_irt_phase_b" / "student_abilities.csv")
    return item_params, responses, abilities


def get_benchmark_data(benchmark, item_params, responses):
    col_start, col_end = BENCHMARK_COLS[benchmark]
    X_bench = responses[:, col_start:col_end]

    params_bench = item_params[item_params["benchmark"] == benchmark].sort_values(
        "item_idx"
    )
    assert len(params_bench) == col_end - col_start, (
        f"{benchmark}: expected {col_end - col_start} items, got {len(params_bench)}"
    )

    a = params_bench["a_discrimination"].values
    b = params_bench["b_difficulty"].values
    c = params_bench["c_guessing"].values
    d = params_bench["d_feasibility"].values

    mask = filter_valid_items(a, b, c, d, min_a=0.0)
    n_filtered = (~mask).sum()
    if n_filtered > 0:
        print(f"  {benchmark}: filtered {n_filtered} items with a <= 0")

    return X_bench[:, mask], a[mask], b[mask], c[mask], d[mask]


def compute_all(benchmark, X, a, b, c, d, abilities_df):
    rows = []
    for i in range(X.shape[0]):
        x = X[i]
        theta = float(abilities_df.loc[abilities_df["student_id"] == i, "ability"].values[0])
        acc = float(x.mean())

        lz_star = float(compute_lz_star(x, theta, a, b, c, d))
        lz = float(compute_lz(x, theta, a, b, c, d))
        outfit = float(compute_outfit(x, theta, a, b, c, d))
        infit = float(compute_infit(x, theta, a, b, c, d))

        rows.append({
            "student_id": i,
            "benchmark": benchmark,
            "theta": theta,
            "lz_star": lz_star,
            "lz": lz,
            "outfit": outfit,
            "infit": infit,
            "accuracy": acc,
        })
    return rows


def make_summary(df):
    summary = {}
    for bench in TARGET_BENCHMARKS:
        sub = df[df["benchmark"] == bench]
        lz_vals = sub["lz_star"].values
        summary[bench] = {
            "n_models": len(sub),
            "lz_star_mean": float(np.mean(lz_vals)),
            "lz_star_std": float(np.std(lz_vals, ddof=1)),
            "lz_star_min": float(np.min(lz_vals)),
            "lz_star_max": float(np.max(lz_vals)),
            "n_significant_neg": int(np.sum(lz_vals < -1.96)),
            "n_significant_pos": int(np.sum(lz_vals > 1.96)),
            "significant_models_neg": sub.loc[
                sub["lz_star"] < -1.96, "student_id"
            ].tolist(),
        }
    return summary


def plot_lz_star(df, out_dir):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    for bench in TARGET_BENCHMARKS:
        sub = df[df["benchmark"] == bench].sort_values("student_id")
        fig, ax = plt.subplots(figsize=(10, 5))
        colors = ["#e74c3c" if v < -1.96 else "#3498db" for v in sub["lz_star"]]
        bars = ax.bar(
            range(len(sub)),
            sub["lz_star"].values,
            color=colors,
            edgecolor="white",
            linewidth=0.5,
        )
        ax.axhline(-1.96, color="red", linestyle="--", linewidth=1, label="z = -1.96")
        ax.axhline(0, color="gray", linestyle="-", linewidth=0.5)
        ax.set_xticks(range(len(sub)))
        ax.set_xticklabels(
            [f"M{sid}" for sid in sub["student_id"]], rotation=45, ha="right"
        )
        ax.set_ylabel("lz*")
        ax.set_title(f"lz* by Model — {bench} ({len(sub)} models)")
        ax.legend()
        plt.tight_layout()
        fig.savefig(out_dir / f"lz_star_{bench}.png", dpi=150)
        plt.close(fig)
        print(f"  Saved: lz_star_{bench}.png")


def cross_benchmark_correlation(df):
    pivot = df.pivot(index="student_id", columns="benchmark", values="lz_star")
    pivot = pivot[TARGET_BENCHMARKS]
    n = len(TARGET_BENCHMARKS)
    corr_matrix = {}
    for i in range(n):
        for j in range(i + 1, n):
            b1, b2 = TARGET_BENCHMARKS[i], TARGET_BENCHMARKS[j]
            rho, pval = stats.spearmanr(pivot[b1], pivot[b2])
            corr_matrix[f"{b1}_vs_{b2}"] = {
                "spearman_rho": round(float(rho), 4),
                "p_value": round(float(pval), 4),
            }
    return corr_matrix


def main():
    print("Loading data...")
    item_params, responses, abilities = load_data()
    print(f"  Responses: {responses.shape}, Models: {len(abilities)}")

    out_dir = ARTIFACTS / "phase_b_results"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Quick validation on HumanEval, model 0
    print("\n--- Validation: HumanEval, Model 0 ---")
    X_he, a_he, b_he, c_he, d_he = get_benchmark_data(
        "HumanEval", item_params, responses
    )
    theta_0 = float(abilities.loc[abilities["student_id"] == 0, "ability"].values[0])
    x_0 = X_he[0]
    lz_star_0 = compute_lz_star(x_0, theta_0, a_he, b_he, c_he, d_he)
    print(f"  theta={theta_0:.4f}, acc={x_0.mean():.4f}, lz*={lz_star_0:.4f}")

    # Verify accuracy-theta rank consistency
    accs = [X_he[i].mean() for i in range(X_he.shape[0])]
    thetas = [
        float(abilities.loc[abilities["student_id"] == i, "ability"].values[0])
        for i in range(len(abilities))
    ]
    rho, _ = stats.spearmanr(accs, thetas)
    print(f"  Accuracy-theta Spearman rho (HumanEval): {rho:.4f}")

    # Full computation
    print("\n--- Computing person-fit for all target benchmarks ---")
    all_rows = []
    for bench in TARGET_BENCHMARKS:
        print(f"\nProcessing {bench}...")
        X, a, b, c, d = get_benchmark_data(bench, item_params, responses)
        print(f"  Items after filtering: {X.shape[1]}")
        rows = compute_all(bench, X, a, b, c, d, abilities)
        all_rows.extend(rows)

        lz_vals = [r["lz_star"] for r in rows]
        print(f"  lz* range: [{min(lz_vals):.3f}, {max(lz_vals):.3f}]")
        print(f"  lz* SD: {np.std(lz_vals, ddof=1):.3f}")

    df = pd.DataFrame(all_rows)
    df.to_csv(out_dir / "personfit_matrix.csv", index=False)
    print(f"\nSaved: personfit_matrix.csv ({len(df)} rows)")

    summary = make_summary(df)
    corr = cross_benchmark_correlation(df)
    summary["cross_benchmark_spearman"] = corr

    with open(out_dir / "personfit_summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print("Saved: personfit_summary.json")

    print("\n--- Summary ---")
    for bench in TARGET_BENCHMARKS:
        s = summary[bench]
        print(
            f"  {bench:12s}: lz* mean={s['lz_star_mean']:+.3f} "
            f"std={s['lz_star_std']:.3f} "
            f"[{s['lz_star_min']:+.3f}, {s['lz_star_max']:+.3f}] "
            f"sig(<-1.96)={s['n_significant_neg']}"
        )

    print("\n  Cross-benchmark Spearman correlations:")
    for pair, vals in corr.items():
        print(f"    {pair}: rho={vals['spearman_rho']:.4f} (p={vals['p_value']:.4f})")

    print("\nGenerating plots...")
    plot_lz_star(df, out_dir)
    print("\nDone.")


if __name__ == "__main__":
    main()
