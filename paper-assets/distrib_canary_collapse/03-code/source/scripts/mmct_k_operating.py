#!/usr/bin/env python3
"""MMCT K-threshold operating characteristics analysis.
Computes FPR/TPR at K=2,3,4,5 across all alpha levels.
"""
import json
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import defaultdict
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
ARTIFACTS = PROJECT / "artifacts"
FIGURES = PROJECT / "docs" / "paper" / "figures"
NULL_JSON = ARTIFACTS / "fpr_transparency_all_seeds.json"
CSV_FILE = ARTIFACTS / "_project" / "data" / "dose_response_d120_recompiled.csv"

# ── 1. FPR from null JSON (6-pair basis, 6 seeds) ──────────────────────────

def compute_fpr():
    with open(NULL_JSON) as f:
        data = json.load(f)

    all_votes = []
    per_seed = {}
    for seed_data in data["seeds"]:
        sid = seed_data["seed"]
        votes = [p["consensus_votes"] for p in seed_data["pairs"]]
        all_votes.extend(votes)
        per_seed[sid] = votes

    total = len(all_votes)  # 36
    fpr = {}
    for k in [2, 3, 4, 5]:
        count = sum(1 for v in all_votes if v >= k)
        fpr[k] = {"count": count, "total": total, "rate": count / total}

    return fpr, per_seed


# ── 2. TPR from CSV (fp32, alpha_sweep, gpt2, wikitext, T=10) ──────────────

def load_csv_data():
    rows = []
    with open(CSV_FILE) as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def select_experiments(rows):
    """Filter and deduplicate: alpha_sweep + gpt2 + wikitext + fp32 + T=10.
    For alpha=1.0, also include padding_robustness.
    Prefer fp32 suffix, latest version for same (alpha, seed)."""

    candidates = []
    for r in rows:
        cat = r["category"]
        model = r["model"]
        domain = r["domain"]
        prec = r["precision"]
        T = int(r["T"])
        alpha = float(r["alpha"])

        if model != "gpt2" or domain != "wikitext" or prec != "fp32" or T != 10:
            continue
        if cat == "alpha_sweep" or (cat == "padding_robustness" and alpha == 1.0):
            candidates.append(r)

    # Deduplicate: for same (alpha, seed), pick the best version
    grouped = defaultdict(list)
    for r in candidates:
        key = (float(r["alpha"]), int(r["seed"]))
        grouped[key].append(r)

    selected = []
    for key, exps in sorted(grouped.items()):
        if len(exps) == 1:
            selected.append(exps[0])
        else:
            # Prefer experiment names with _fp32, then latest version
            # Exclude postd093 variants (pre-D93 fix), prefer standard names
            best = None
            for e in exps:
                name = e["experiment"]
                if "postd093" in name:
                    continue
                if best is None:
                    best = e
                elif "_fp32" in name and "_fp32" not in best["experiment"]:
                    best = e
                elif "v3_d080" in name and "v4" in best["experiment"]:
                    # v3_d080 gave results consistent with bf16 control; v4 is an outlier
                    best = e
                elif "v4" in name and "v3_d080" not in best["experiment"]:
                    best = e
            selected.append(best or exps[0])

    return selected


def compute_k2_estimate(row):
    """Estimate K>=2 count from per-method counts using pigeonhole lower bound.

    We know: V (total votes), ge3, ge4, ge5 (counts of pairs with ≥3/4/5 votes).
    For pairs with <3 votes: R = n_pairs - ge3 pairs share V_remaining votes.
    By pigeonhole, at least max(0, V_remaining - R) of these pairs have ≥2 votes.
    """
    n = int(row["n_pairs"])
    naive = int(row["naive_fwd"])
    diff = int(row["diffxcorr_fwd_fdr"])
    thresh = int(row["threshold_fwd"])
    perm = int(row["permg_fwd_fdr"])
    ty = int(row["ty_fwd"])
    ge3 = int(row["consensus_ge3"])
    ge4 = int(row["consensus_ge4"])
    ge5 = int(row["consensus_ge5"])

    V = naive + diff + thresh + perm + ty
    # Votes consumed by ge3+ pairs (minimum: each ge3 pair has exactly 3 votes, etc.)
    V_consumed = 3 * (ge3 - ge4) + 4 * (ge4 - ge5) + 5 * ge5
    V_remaining = V - V_consumed
    R = n - ge3  # pairs with 0, 1, or 2 votes

    # Lower bound for n_2 (pairs with exactly 2 votes among the remaining)
    k2_from_remaining_min = max(0, V_remaining - R)
    # Upper bound
    k2_from_remaining_max = min(R, V_remaining // 2) if V_remaining >= 0 else 0

    k2_min = ge3 + k2_from_remaining_min
    k2_max = ge3 + k2_from_remaining_max

    # Use midpoint as estimate
    k2_est = (k2_min + k2_max) / 2

    return k2_est, k2_min, k2_max


# ── 3. Main analysis ───────────────────────────────────────────────────────

def main():
    fpr, fpr_per_seed = compute_fpr()

    rows = load_csv_data()
    selected = select_experiments(rows)

    # Group by alpha
    alpha_groups = defaultdict(list)
    for r in selected:
        alpha = float(r["alpha"])
        alpha_groups[alpha].append(r)

    # Compute detection rates per alpha
    results = []

    # α = 0.0: use null JSON FPR (6-pair basis)
    results.append({
        "alpha": 0.0,
        "n_seeds": 6,
        "n_pairs_per_seed": 6,
        "total_pairs": 36,
        "pair_basis": "6-pair (null JSON, s45-s50)",
        "k2_rate": fpr[2]["rate"],
        "k3_rate": fpr[3]["rate"],
        "k4_rate": fpr[4]["rate"],
        "k5_rate": fpr[5]["rate"],
        "k2_count": fpr[2]["count"],
        "k3_count": fpr[3]["count"],
        "k4_count": fpr[4]["count"],
        "k5_count": fpr[5]["count"],
        "k2_exact": True,
        "is_fpr": True,
    })

    # α > 0: use CSV fp32 data (8-pair basis)
    for alpha in sorted(alpha_groups.keys()):
        if alpha == 0.0:
            continue  # already handled
        exps = alpha_groups[alpha]
        n_seeds = len(exps)
        n_pairs = int(exps[0]["n_pairs"])  # 8
        total = n_seeds * n_pairs

        ge3_total = sum(int(e["consensus_ge3"]) for e in exps)
        ge4_total = sum(int(e["consensus_ge4"]) for e in exps)
        ge5_total = sum(int(e["consensus_ge5"]) for e in exps)

        # K>=2 estimate
        k2_estimates = [compute_k2_estimate(e) for e in exps]
        k2_est_total = sum(e[0] for e in k2_estimates)
        k2_min_total = sum(e[1] for e in k2_estimates)
        k2_max_total = sum(e[2] for e in k2_estimates)

        results.append({
            "alpha": alpha,
            "n_seeds": n_seeds,
            "n_pairs_per_seed": n_pairs,
            "total_pairs": total,
            "pair_basis": f"8-pair (CSV fp32, {n_seeds} seeds)",
            "experiments": [e["experiment"] for e in exps],
            "k2_rate": k2_est_total / total,
            "k2_rate_range": [k2_min_total / total, k2_max_total / total],
            "k3_rate": ge3_total / total,
            "k4_rate": ge4_total / total,
            "k5_rate": ge5_total / total,
            "k2_count_est": k2_est_total,
            "k3_count": ge3_total,
            "k4_count": ge4_total,
            "k5_count": ge5_total,
            "k2_exact": False,
            "is_fpr": False,
        })

    # ── 4. Print summary table ──────────────────────────────────────────────

    print(f"{'α':>6} {'seeds':>5} {'basis':>5} | {'K≥2':>8} {'K≥3':>8} {'K≥4':>8} {'K≥5':>8}")
    print("-" * 60)
    for r in results:
        k2_str = f"{r['k2_rate']:.3f}" if r['k2_exact'] else f"~{r['k2_rate']:.3f}"
        print(f"{r['alpha']:6.2f} {r['n_seeds']:5d} {r['n_pairs_per_seed']:5d} | "
              f"{k2_str:>8} {r['k3_rate']:8.3f} {r['k4_rate']:8.3f} {r['k5_rate']:8.3f}")

    # ── 5. Key metrics ──────────────────────────────────────────────────────

    print("\n=== KEY METRICS ===")
    fpr_row = results[0]
    print(f"K≥2 FPR at α=0.0: {fpr_row['k2_rate']:.3f} ({fpr_row['k2_count']}/36)")
    print(f"K≥3 FPR at α=0.0: {fpr_row['k3_rate']:.3f} ({fpr_row['k3_count']}/36)")
    print(f"K≥4 FPR at α=0.0: {fpr_row['k4_rate']:.3f} ({fpr_row['k4_count']}/36)")
    print(f"K≥5 FPR at α=0.0: {fpr_row['k5_rate']:.3f} ({fpr_row['k5_count']}/36)")

    # Find α=0.75 row
    for r in results:
        if r["alpha"] == 0.75:
            print(f"\nK≥3 TPR at α=0.75: {r['k3_rate']:.3f}")
            print(f"K≥4 TPR at α=0.75: {r['k4_rate']:.3f}")
            print(f"K≥3 vs K≥4 detection gap at α=0.75: {r['k3_rate'] - r['k4_rate']:.3f}")

    # ── 6. Plot ─────────────────────────────────────────────────────────────

    alphas = [r["alpha"] for r in results]
    k2_rates = [r["k2_rate"] for r in results]
    k3_rates = [r["k3_rate"] for r in results]
    k4_rates = [r["k4_rate"] for r in results]
    k5_rates = [r["k5_rate"] for r in results]
    n_seeds_list = [r["n_seeds"] for r in results]

    colors = {
        2: "#E08214",  # orange
        3: "#2166AC",  # blue
        4: "#1B7837",  # green
        5: "#6A3D9A",  # purple
    }

    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Times New Roman', 'DejaVu Serif'],
        'mathtext.fontset': 'dejavuserif',
    })

    fig, ax = plt.subplots(1, 1, figsize=(5.5, 3.5))

    # K≥2: lighter dashed line (estimated, high FPR — less emphasis)
    ax.plot(alphas, k2_rates, 'o--', color=colors[2], label=r'$K \geq 2$',
            linewidth=1.2, markersize=3.5, alpha=0.55, zorder=2)
    # K≥3: primary curve, bold
    ax.plot(alphas, k3_rates, 's-', color=colors[3], label=r'$K \geq 3$ (default)',
            linewidth=2.2, markersize=5.5, zorder=5)
    ax.plot(alphas, k4_rates, '^-', color=colors[4], label=r'$K \geq 4$',
            linewidth=1.6, markersize=5, zorder=4)
    ax.plot(alphas, k5_rates, 'D-', color=colors[5], label=r'$K \geq 5$',
            linewidth=1.4, markersize=3.5, zorder=3)

    # Nominal 5% FPR line
    ax.axhline(y=0.05, color='#aaaaaa', linestyle=':', linewidth=0.7, zorder=1)
    ax.text(0.82, 0.065, '5%', fontsize=6.5, color='#999999', style='italic')

    # FPR annotations at α=0 — right margin, compact
    ax.annotate('38.9%', xy=(0.0, fpr[2]["rate"]), xytext=(-0.035, fpr[2]["rate"]),
                fontsize=5.5, color=colors[2], ha='right', va='center', fontweight='bold')
    ax.annotate('16.7%', xy=(0.0, fpr[3]["rate"]), xytext=(-0.035, fpr[3]["rate"]),
                fontsize=5.5, color=colors[3], ha='right', va='center', fontweight='bold')
    ax.annotate('0%', xy=(0.0, 0.005), xytext=(-0.025, -0.035),
                fontsize=5.5, color=colors[4], ha='right', va='center', fontweight='bold')

    # Shade null region
    ax.axvspan(-0.06, 0.025, color='#f5f5f5', zorder=0)
    ax.text(0.002, 0.97, 'null', fontsize=6.5, color='#bbbbbb', ha='center',
            va='top', rotation=90, transform=ax.get_xaxis_transform())

    ax.set_xlabel(r'Contamination ratio ($\alpha$)', fontsize=10)
    ax.set_ylabel('Detection rate', fontsize=10)
    ax.set_xlim(-0.06, 1.06)
    ax.set_ylim(-0.05, 1.05)
    ax.set_xticks([0.0, 0.1, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels(['0', '0.10', '0.25', '0.50', '0.75', '1.0'])
    ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])

    ax.legend(loc='upper left', fontsize=7.5, framealpha=0.92, edgecolor='#cccccc',
              handlelength=2.2, borderpad=0.5, labelspacing=0.4)
    ax.tick_params(labelsize=8.5)

    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    ax.grid(True, alpha=0.12, linewidth=0.4)

    plt.tight_layout(pad=0.4)

    fig.savefig(FIGURES / "fig_mmct_k_operating.pdf", dpi=300, bbox_inches='tight')
    fig.savefig(FIGURES / "fig_mmct_k_operating.png", dpi=300, bbox_inches='tight')
    print(f"\nPlot saved to {FIGURES / 'fig_mmct_k_operating.pdf'}")
    plt.close()

    # ── 7. Save JSON artifact ───────────────────────────────────────────────

    artifact = {
        "description": "MMCT K-threshold operating characteristics (K=2,3,4,5)",
        "methodology": {
            "fpr": "6-pair basis, 6 null seeds (s45-s50), 36 total pairs from fpr_transparency_all_seeds.json",
            "tpr": "8-pair basis from dose_response_d120_recompiled.csv (alpha_sweep+gpt2+wikitext+fp32+T=10)",
            "k2_estimation": "K≥2 for TPR estimated via pigeonhole lower/upper bound from per-method counts; midpoint used",
            "note": "FPR uses 6-pair (mauve excluded); TPR uses 8-pair (includes mauve). FPR is slightly conservative, TPR slightly diluted vs 6-pair."
        },
        "key_metrics": {
            "k2_fpr": fpr[2]["rate"],
            "k3_fpr": fpr[3]["rate"],
            "k4_fpr": fpr[4]["rate"],
            "k5_fpr": fpr[5]["rate"],
        },
        "results": results,
    }

    # Add TPR at key alpha levels
    for r in results:
        if r["alpha"] == 0.50:
            artifact["key_metrics"]["k3_tpr_a050"] = r["k3_rate"]
            artifact["key_metrics"]["k4_tpr_a050"] = r["k4_rate"]
        elif r["alpha"] == 0.75:
            artifact["key_metrics"]["k3_tpr_a075"] = r["k3_rate"]
            artifact["key_metrics"]["k4_tpr_a075"] = r["k4_rate"]
        elif r["alpha"] == 1.0:
            artifact["key_metrics"]["k3_tpr_a100"] = r["k3_rate"]
            artifact["key_metrics"]["k4_tpr_a100"] = r["k4_rate"]

    output_path = ARTIFACTS / "mmct_k_operating_table.json"
    with open(output_path, 'w') as f:
        json.dump(artifact, f, indent=2)
    print(f"JSON saved to {output_path}")

    return artifact


if __name__ == "__main__":
    main()
