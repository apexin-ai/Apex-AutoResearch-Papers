"""
Dose-response 3-seed statistical analysis for OCC gradient flow duration → CAR/TSR.
Reads comprehensive_results.csv, computes paired t-tests vs Vanilla baseline,
generates publication-quality dose-response curve figure.
"""
import argparse
import csv
import sys
from pathlib import Path

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── Condition definitions ────────────────────────────────────────────────────

DOSE_CONDITIONS = {
    "Detach+BN":       {"x": 0,     "label": "Detach+BN\n(0K)"},
    "Cutoff@15K":      {"x": 15000, "label": "15K"},
    "Cutoff@25K":      {"x": 25000, "label": "25K"},
    "Cutoff@35K":      {"x": 35000, "label": "35K"},
    "Cutoff@45K":      {"x": 45000, "label": "45K"},
    "Full OCC":        {"x": 50000, "label": "Full OCC\n(50K)"},
}

SEED_MAP = {42: "s0", 43: "s1", 44: "s2"}

# Full OCC s1 (mvp_occ_s1) is a 200-ep outlier; replace with occ_s1_fresh 50K
FULL_OCC_S1_REPLACEMENT = {
    "from_exp": "mvp_occ_s1",
    "to_exp": "occ_s1_fresh",
    "to_condition": "Full OCC (fresh)",
    "to_seed": 43,
}


def read_csv(path):
    """Parse comprehensive_results.csv into list of dicts."""
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def extract_condition_data(rows, metric="CAR"):
    """Extract per-condition seed values for dose-response conditions + Reverse Cutoff + Vanilla.

    Returns dict: condition_name -> {"seeds": {seed_label: value}, "training": [seed_labels]}
    """
    result = {}

    # Find Full OCC s1 replacement value
    replacement_val = None
    for row in rows:
        if (row.get("exp_id", "").strip() == FULL_OCC_S1_REPLACEMENT["to_exp"]
                and row.get("seed", "").strip() == str(FULL_OCC_S1_REPLACEMENT["to_seed"])
                and row.get("checkpoint_step", "").strip() == "50000"):
            val = row.get(metric, "").strip()
            if val and val != "training":
                replacement_val = float(val)
            break

    for cond_name in list(DOSE_CONDITIONS.keys()) + ["Reverse Cutoff", "Vanilla"]:
        result[cond_name] = {"seeds": {}, "training": []}

    for row in rows:
        cond = row.get("condition", "").strip()
        if cond not in result:
            continue

        seed_raw = row.get("seed", "").strip()
        if not seed_raw:
            continue
        seed_int = int(seed_raw)
        seed_label = SEED_MAP.get(seed_int, f"s{seed_int - 42}")

        val = row.get(metric, "").strip()
        exp_id = row.get("exp_id", "").strip()

        # Skip retrain / non-canonical entries
        if "retrain" in cond.lower() or "retrain" in exp_id:
            continue

        if val == "training" or val == "":
            result[cond]["training"].append(seed_label)
            continue

        # Full OCC s1 outlier replacement
        if cond == "Full OCC" and exp_id == FULL_OCC_S1_REPLACEMENT["from_exp"]:
            if replacement_val is not None:
                result[cond]["seeds"][seed_label] = replacement_val
            continue

        # Skip Full OCC (fresh) — already used as replacement above
        if cond == "Full OCC (fresh)":
            continue

        result[cond]["seeds"][seed_label] = float(val)

    return result


def cohens_d(x, y):
    """Paired Cohen's d: mean difference / pooled SD."""
    n = len(x)
    if n < 2:
        return None
    diff = np.array(x) - np.array(y)
    sd = np.std(diff, ddof=1)
    if sd == 0:
        return float("inf") if np.mean(diff) != 0 else 0.0
    return np.mean(diff) / sd


def paired_ttest(cond_vals, baseline_vals):
    """Paired t-test. Returns (t_stat, p_value) or (None, None) if n < 3."""
    n = min(len(cond_vals), len(baseline_vals))
    if n < 3:
        return None, None
    c = np.array(cond_vals[:n])
    b = np.array(baseline_vals[:n])
    t_stat, p_val = stats.ttest_rel(c, b)
    return t_stat, p_val


def significance_label(p):
    if p is None:
        return "n<3"
    if p < 0.001:
        return "***"
    if p < 0.01:
        return "**"
    if p < 0.05:
        return "*"
    return "ns"


def run_analysis(csv_path, metric="CAR"):
    """Run full statistical analysis. Returns (summary_rows, dose_curve_data, vanilla_stats, reverse_stats)."""
    rows = read_csv(csv_path)
    data = extract_condition_data(rows, metric=metric)

    vanilla = data.get("Vanilla", {})
    vanilla_vals = sorted(vanilla["seeds"].items())
    vanilla_arr = np.array([v for _, v in vanilla_vals])
    vanilla_mean = np.mean(vanilla_arr)
    vanilla_sd = np.std(vanilla_arr, ddof=1) if len(vanilla_arr) > 1 else 0.0
    vanilla_se = vanilla_sd / np.sqrt(len(vanilla_arr)) if len(vanilla_arr) > 1 else 0.0

    summary = []
    dose_curve = []

    all_conditions = list(DOSE_CONDITIONS.keys()) + ["Reverse Cutoff"]

    for cond_name in all_conditions:
        cond = data.get(cond_name, {"seeds": {}, "training": []})
        vals = sorted(cond["seeds"].items())
        arr = np.array([v for _, v in vals])
        n = len(arr)
        training = cond["training"]

        mean_val = np.mean(arr) if n > 0 else float("nan")
        sd_val = np.std(arr, ddof=1) if n > 1 else 0.0
        se_val = sd_val / np.sqrt(n) if n > 1 else 0.0

        # Paired comparison vs Vanilla (match seeds in order)
        n_paired = min(n, len(vanilla_arr))
        if n_paired >= 3:
            t_stat, p_val = paired_ttest(
                [v for _, v in vals], list(vanilla_arr)
            )
            d = cohens_d([v for _, v in vals][:n_paired], list(vanilla_arr[:n_paired]))
        elif n_paired >= 2:
            t_stat, p_val = None, None
            d = cohens_d([v for _, v in vals][:n_paired], list(vanilla_arr[:n_paired]))
        else:
            t_stat, p_val, d = None, None, None

        sig = significance_label(p_val)

        row = {
            "condition": cond_name,
            "n_seeds": n,
            "training": training,
            f"mean_{metric}": mean_val,
            "SD": sd_val,
            "SE": se_val,
            "seed_values": {k: v for k, v in vals},
            "t_stat": t_stat,
            "p_value": p_val,
            "cohens_d": d,
            "significance": sig,
        }
        summary.append(row)

        if cond_name in DOSE_CONDITIONS:
            dose_curve.append({
                "condition": cond_name,
                "x": DOSE_CONDITIONS[cond_name]["x"],
                "label": DOSE_CONDITIONS[cond_name]["label"],
                f"mean_{metric}": mean_val,
                "SE": se_val,
                "SD": sd_val,
                "n": n,
                "training": training,
            })

    reverse = next((s for s in summary if s["condition"] == "Reverse Cutoff"), None)
    vanilla_stats = {
        f"mean_{metric}": vanilla_mean,
        "SD": vanilla_sd,
        "SE": vanilla_se,
        "n": len(vanilla_arr),
        "seed_values": {k: v for k, v in vanilla_vals},
    }

    dose_curve.sort(key=lambda c: c["x"])
    return summary, dose_curve, vanilla_stats, reverse


def print_summary(summary, vanilla_stats, metric="CAR"):
    """Print formatted summary table."""
    mk = f"mean_{metric}"

    print(f"\n{'='*100}")
    print(f"  Dose-Response 3-Seed Statistical Analysis — {metric}")
    print(f"{'='*100}")
    print(f"\n  Vanilla baseline: {mk}={vanilla_stats[mk]:.3f} ± {vanilla_stats['SD']:.3f} (n={vanilla_stats['n']})")
    print(f"  Seeds: {vanilla_stats['seed_values']}\n")

    header = f"  {'Condition':<18} {'n':>3}  {mk:>10}  {'SD':>6}  {'SE':>6}  {'t':>7}  {'p':>8}  {'d':>7}  {'sig':>5}  {'notes'}"
    print(header)
    print("  " + "-" * (len(header) - 2))

    for row in summary:
        notes = ""
        if row["training"]:
            notes = f"training: {','.join(row['training'])}"

        t_str = f"{row['t_stat']:.3f}" if row["t_stat"] is not None else "—"
        p_str = f"{row['p_value']:.4f}" if row["p_value"] is not None else "—"
        d_str = f"{row['cohens_d']:.3f}" if row["cohens_d"] is not None else "—"

        print(f"  {row['condition']:<18} {row['n_seeds']:>3}  "
              f"{row[f'mean_{metric}']:>10.3f}  {row['SD']:>6.3f}  {row['SE']:>6.3f}  "
              f"{t_str:>7}  {p_str:>8}  {d_str:>7}  {row['significance']:>5}  {notes}")

    print()


def write_dose_curve_csv(dose_curve, vanilla_stats, reverse, output_path, metric="CAR"):
    """Write CSV consumable by matplotlib for dose-response plotting."""
    mk = f"mean_{metric}"
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["type", "condition", "x_step", mk, "SE", "SD", "n", "notes"])

        # Vanilla baseline
        writer.writerow(["baseline", "Vanilla", "", f"{vanilla_stats[mk]:.4f}",
                          f"{vanilla_stats['SE']:.4f}", f"{vanilla_stats['SD']:.4f}",
                          vanilla_stats["n"], ""])

        # Forward cutoff curve
        for pt in dose_curve:
            notes = f"training:{','.join(pt['training'])}" if pt["training"] else ""
            writer.writerow(["forward", pt["condition"], pt["x"],
                              f"{pt[mk]:.4f}", f"{pt['SE']:.4f}", f"{pt['SD']:.4f}",
                              pt["n"], notes])

        # Reverse cutoff
        if reverse:
            notes = f"training:{','.join(reverse['training'])}" if reverse["training"] else ""
            writer.writerow(["reverse", "Reverse Cutoff", 15000,
                              f"{reverse[mk]:.4f}", f"{reverse['SE']:.4f}", f"{reverse['SD']:.4f}",
                              reverse["n_seeds"], notes])

    print(f"  Curve CSV: {output_path}")


def plot_dose_response(dose_curve, vanilla_stats, reverse, output_dir, metric="CAR"):
    """Generate publication-quality dose-response figure."""
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman", "DejaVu Serif"],
        "font.size": 9,
        "axes.labelsize": 11,
        "axes.titlesize": 11,
        "xtick.labelsize": 8.5,
        "ytick.labelsize": 8.5,
        "legend.fontsize": 8,
        "figure.dpi": 300,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    })

    mk = f"mean_{metric}"
    fig, ax = plt.subplots(1, 1, figsize=(4.8, 3.4))

    xs = [pt["x"] / 1000 for pt in dose_curve]
    means = [pt[mk] for pt in dose_curve]
    ses = [pt["SE"] for pt in dose_curve]
    ns = [pt["n"] for pt in dose_curve]

    # SE band
    ax.fill_between(xs,
                     [m - s for m, s in zip(means, ses)],
                     [m + s for m, s in zip(means, ses)],
                     alpha=0.18, color="#2166AC", zorder=2)

    # Main curve — filled circles
    ax.plot(xs, means, "o-", color="#2166AC", linewidth=1.8,
            markersize=7, markerfacecolor="#2166AC", markeredgecolor="white",
            markeredgewidth=0.8, zorder=5)

    # n= annotations
    for i, (x, m, se, n) in enumerate(zip(xs, means, ses, ns)):
        y_offset = se + 0.008 if se > 0 else 0.008
        color = "#999999" if n >= 3 else "#CC4444"
        ax.annotate(f"n={n}", (x, m + y_offset), ha="center", fontsize=6.5,
                    color=color, fontweight="bold" if n < 3 else "normal")

    # Reverse cutoff — diamond marker
    if reverse:
        rc_x = 16.5  # slight offset from 15K
        rc_mean = reverse[mk]
        rc_se = reverse["SE"]
        ax.errorbar(rc_x, rc_mean, yerr=rc_se, fmt="D", color="#B2182B",
                    markersize=7.5, markerfacecolor="#B2182B", markeredgecolor="white",
                    markeredgewidth=0.8, capsize=3, linewidth=1.5, zorder=6)
        rc_n = reverse["n_seeds"]
        n_color = "#999999" if rc_n >= 3 else "#CC4444"
        ax.annotate(f"n={rc_n}", (rc_x, rc_mean + rc_se + 0.008),
                    ha="center", fontsize=6.5, color=n_color,
                    fontweight="bold" if rc_n < 3 else "normal")

    # Axis formatting
    metric_label = "Collision Avoidance Rate (CAR)" if metric == "CAR" else "Task Success Rate (TSR)"
    ax.set_xlabel("OCC Gradient Flow Duration (K steps)")
    ax.set_ylabel(metric_label)
    ax.set_xlim(-2, 54)
    ax.set_xticks([0, 15, 25, 35, 45, 50])
    ax.set_xticklabels(["0\n(Detach)", "15K", "25K", "35K", "45K", "50K\n(Full)"])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Y limits with padding
    all_vals = list(means)
    if reverse:
        all_vals.append(reverse[mk])
    y_min = min(all_vals) - 0.05
    y_max = max(all_vals) + 0.05
    ax.set_ylim(y_min, y_max)

    # Legend
    forward_patch = plt.Line2D([0], [0], marker="o", color="#2166AC", linewidth=1.5,
                                markerfacecolor="#2166AC", markeredgecolor="white",
                                markersize=7, label="Forward cutoff")
    handles = [forward_patch]
    if reverse:
        reverse_marker = plt.Line2D([0], [0], marker="D", color="w",
                                     markerfacecolor="#B2182B", markeredgecolor="white",
                                     markersize=7, label="Reverse cutoff (late 15K)")
        handles.append(reverse_marker)
    ax.legend(handles=handles, loc="lower right", framealpha=0.9, edgecolor="#CCCCCC")

    plt.tight_layout()

    pdf_path = Path(output_dir) / "dose_response_3seed_final.pdf"
    png_path = Path(output_dir) / "dose_response_3seed_final.png"
    plt.savefig(pdf_path)
    plt.savefig(png_path, dpi=300)
    plt.close()
    print(f"  Figure: {pdf_path}")
    print(f"  Figure: {png_path}")


def main():
    parser = argparse.ArgumentParser(description="Dose-response 3-seed statistical analysis")
    parser.add_argument("--csv", default=str(Path(__file__).parent / "comprehensive_results.csv"),
                        help="Path to comprehensive_results.csv")
    parser.add_argument("--dry-run", action="store_true",
                        help="Run with current data, marking missing seeds")
    parser.add_argument("--output-dir", default=str(Path(__file__).parent),
                        help="Output directory for figures and CSV")
    parser.add_argument("--metric", choices=["CAR", "TSR"], default="CAR",
                        help="Y-axis metric (default: CAR)")
    args = parser.parse_args()

    csv_path = Path(args.csv)
    if not csv_path.exists():
        print(f"ERROR: CSV not found: {csv_path}", file=sys.stderr)
        sys.exit(1)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    summary, dose_curve, vanilla_stats, reverse = run_analysis(csv_path, metric=args.metric)

    print_summary(summary, vanilla_stats, metric=args.metric)

    curve_csv_path = output_dir / f"dose_response_curve_data_{args.metric.lower()}.csv"
    write_dose_curve_csv(dose_curve, vanilla_stats, reverse, curve_csv_path, metric=args.metric)

    plot_dose_response(dose_curve, vanilla_stats, reverse, output_dir, metric=args.metric)

    # Completeness check
    incomplete = [s for s in summary if s["training"]]
    if incomplete:
        print(f"\n  ⚠ {len(incomplete)} conditions have seeds still training:")
        for s in incomplete:
            print(f"    {s['condition']}: missing {','.join(s['training'])}")

    if args.dry_run:
        print("\n  [dry-run] Analysis used current available data only.")


if __name__ == "__main__":
    main()
