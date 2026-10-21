"""
exp-014 v2 Independent Analysis (fixes circular reasoning)

Correlation analysis using 6 quality metrics that are fully independent
of the OBD 15D feature set. OBD features (freq_entropy, ttr, etc.) are
reported separately as sanity checks with explicit overlap warnings.

Input:  data_exp014_v2/{cc_quality_independent.csv, cc_predictions.csv,
                        cc_sample.jsonl, cc_features.csv}
Output: results/exp014_v2/{independent_analysis_results.json,
        independent_violin.pdf, depth_distribution.pdf, mauve_by_bin.pdf}
"""

import csv
import json
import logging
import sys
import time
from pathlib import Path

import numpy as np
from scipy import stats

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

PROJECT_ROOT = Path("/root/autodl-tmp/gen-depth-contamination")
DATA_DIR = PROJECT_ROOT / "data_exp014_v2"
OUT_DIR = PROJECT_ROOT / "results" / "exp014_v2"
SEED = 42

INDEPENDENT_COLS = ["gpt2_ppl", "mtld", "hdd", "rep_3gram", "rep_4gram", "zipf"]
INDEPENDENT_LABELS = {
    "gpt2_ppl": "GPT-2 Large PPL",
    "mtld": "MTLD",
    "hdd": "HD-D",
    "rep_3gram": "3-gram Rep Rate",
    "rep_4gram": "4-gram Rep Rate",
    "zipf": "Zipf Coefficient",
}

OBD_FEAT_COLS = [
    "ttr", "hapax_ratio", "freq_entropy", "freq_kurtosis", "low_freq_ratio",
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std", "self_bleu",
]


def load_csv(path, cols):
    data = {c: [] for c in cols}
    with open(path) as f:
        reader = csv.DictReader(f)
        available = [c for c in cols if c in reader.fieldnames]
        for row in reader:
            for c in available:
                v = row.get(c, "")
                data[c].append(float(v) if v not in ("", "nan") else float("nan"))
    return {c: np.array(data[c]) for c in available}


def load_data():
    pred_path = DATA_DIR / "cc_predictions.csv"
    indep_path = DATA_DIR / "cc_quality_independent.csv"
    feat_path = DATA_DIR / "cc_features.csv"
    sample_path = DATA_DIR / "cc_sample.jsonl"

    for p in [pred_path, indep_path]:
        if not p.exists():
            log.error(f"{p} not found")
            sys.exit(1)

    with open(pred_path) as f:
        rows = list(csv.DictReader(f))
    predicted_depths = np.array([int(r["predicted_depth"]) for r in rows])
    expected_depths = np.array([float(r["expected_depth"]) for r in rows])

    indep_metrics = load_csv(indep_path, INDEPENDENT_COLS)
    missing = [c for c in INDEPENDENT_COLS if c not in indep_metrics]
    if missing:
        log.error(f"Missing independent metrics: {missing}")
        sys.exit(1)

    obd_features = {}
    if feat_path.exists():
        obd_features = load_csv(feat_path, OBD_FEAT_COLS)

    text_lengths = None
    if sample_path.exists():
        lengths = []
        with open(sample_path) as f:
            for line in f:
                lengths.append(len(json.loads(line)["text"].split()))
        text_lengths = np.array(lengths)

    n = len(predicted_depths)
    log.info(f"Loaded {n} samples, depth range [{predicted_depths.min()}, {predicted_depths.max()}]")
    return predicted_depths, expected_depths, indep_metrics, obd_features, text_lengths


# ── Statistical helpers ──

def cliffs_delta(x, y):
    nx, ny = len(x), len(y)
    if nx == 0 or ny == 0:
        return 0.0
    more = less = 0
    for xi in x:
        for yj in y:
            if xi > yj:
                more += 1
            elif xi < yj:
                less += 1
    return (more - less) / (nx * ny)


def cliffs_delta_fast(x, y):
    nx, ny = len(x), len(y)
    if nx * ny > 5_000_000:
        rng = np.random.RandomState(SEED)
        if nx > 5000:
            x = rng.choice(x, 5000, replace=False)
            nx = 5000
        if ny > 5000:
            y = rng.choice(y, 5000, replace=False)
            ny = 5000
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    diffs = x[:, None] - y[None, :]
    more = np.sum(diffs > 0)
    less = np.sum(diffs < 0)
    return float((more - less) / (nx * ny))


def effect_label(d):
    d = abs(d)
    if d >= 0.474:
        return "large"
    if d >= 0.33:
        return "medium"
    if d >= 0.147:
        return "small"
    return "negligible"


def bootstrap_spearman(depths, vals, n_boot=1000, ci=0.95):
    rng = np.random.RandomState(SEED)
    valid = ~np.isnan(vals) & ~np.isnan(depths)
    d = depths[valid]
    v = vals[valid]
    n = len(d)
    if n < 30:
        return None
    rhos = []
    for _ in range(n_boot):
        idx = rng.choice(n, n, replace=True)
        rho, _ = stats.spearmanr(d[idx], v[idx])
        if not np.isnan(rho):
            rhos.append(rho)
    if len(rhos) < 100:
        return None
    rhos = sorted(rhos)
    lo = (1 - ci) / 2
    hi = 1 - lo
    return [round(rhos[int(lo * len(rhos))], 4), round(rhos[int(hi * len(rhos))], 4)]


# ── Analysis functions ──

def correlation_analysis(depths, indep_metrics):
    n_tests = len(INDEPENDENT_COLS)
    alpha = 0.05 / n_tests  # Bonferroni
    results = {}

    for m in INDEPENDENT_COLS:
        vals = indep_metrics[m]
        valid = ~np.isnan(vals) & ~np.isnan(depths.astype(float))
        nv = valid.sum()
        if nv < 30:
            log.info(f"  {m}: too few valid ({nv})")
            continue

        d = depths[valid].astype(float)
        v = vals[valid]

        rho, p_rho = stats.spearmanr(d, v)
        tau, p_tau = stats.kendalltau(d, v)
        ci = bootstrap_spearman(depths.astype(float), vals)

        results[m] = {
            "spearman_rho": round(float(rho), 4),
            "spearman_p": float(p_rho),
            "spearman_sig_bonferroni": bool(p_rho < alpha),
            "kendall_tau": round(float(tau), 4),
            "kendall_p": float(p_tau),
            "kendall_sig_bonferroni": bool(p_tau < alpha),
            "bootstrap_ci_95": ci,
            "n_valid": int(nv),
        }
        sig = "***" if p_rho < alpha else ""
        log.info(f"  {m}: rho={rho:.4f} (p={p_rho:.2e}{sig}), tau={tau:.4f}, CI={ci}")

    return results, alpha


def stratified_analysis(depths, indep_metrics):
    bin_defs = [("0", lambda d: d == 0), ("1", lambda d: d == 1),
                ("2", lambda d: d == 2), ("3+", lambda d: d >= 3)]
    result = {}
    for label, fn in bin_defs:
        mask = fn(depths)
        n = mask.sum()
        if n == 0:
            continue
        entry = {"count": int(n)}
        for m in INDEPENDENT_COLS:
            vals = indep_metrics[m][mask]
            valid = vals[~np.isnan(vals)]
            if len(valid) == 0:
                continue
            q1, q3 = np.percentile(valid, [25, 75])
            entry[m] = {
                "mean": round(float(np.mean(valid)), 6),
                "median": round(float(np.median(valid)), 6),
                "std": round(float(np.std(valid)), 6),
                "iqr": round(float(q3 - q1), 6),
            }
        result[label] = entry
        log.info(f"  depth {label}: n={n}")
    return result


def statistical_tests(depths, indep_metrics):
    bin_defs = [("0", lambda d: d == 0), ("1", lambda d: d == 1),
                ("2", lambda d: d == 2), ("3+", lambda d: d >= 3)]
    result = {}

    for m in INDEPENDENT_COLS:
        groups = []
        labels = []
        for label, fn in bin_defs:
            mask = fn(depths)
            vals = indep_metrics[m][mask]
            valid = vals[~np.isnan(vals)]
            if len(valid) >= 5:
                groups.append(valid)
                labels.append(label)

        if len(groups) < 2:
            continue

        kw_stat, kw_p = stats.kruskal(*groups)

        pairwise = {}
        for i in range(len(groups)):
            for j in range(i + 1, len(groups)):
                pair = f"{labels[i]}_vs_{labels[j]}"
                u, u_p = stats.mannwhitneyu(groups[i], groups[j], alternative="two-sided")
                cd = cliffs_delta_fast(groups[i], groups[j])
                pairwise[pair] = {
                    "mann_whitney_U": float(u),
                    "p_value": float(u_p),
                    "cliffs_delta": round(cd, 4),
                    "effect_size": effect_label(cd),
                }

        result[m] = {
            "kruskal_wallis": {"statistic": round(float(kw_stat), 4), "p_value": float(kw_p)},
            "pairwise": pairwise,
        }
        log.info(f"  {m}: KW H={kw_stat:.2f}, p={kw_p:.2e}")

    return result


def length_controlled_analysis(depths, indep_metrics, text_lengths):
    if text_lengths is None:
        return {}

    quartiles = np.percentile(text_lengths, [25, 50, 75])
    bins = [
        ("Q1", text_lengths <= quartiles[0]),
        ("Q2", (text_lengths > quartiles[0]) & (text_lengths <= quartiles[1])),
        ("Q3", (text_lengths > quartiles[1]) & (text_lengths <= quartiles[2])),
        ("Q4", text_lengths > quartiles[2]),
    ]

    result = {"quartile_boundaries": [int(q) for q in quartiles]}
    for q_label, q_mask in bins:
        q_n = q_mask.sum()
        if q_n < 50:
            continue
        q_depths = depths[q_mask].astype(float)
        q_res = {}
        for m in INDEPENDENT_COLS:
            vals = indep_metrics[m][q_mask]
            valid = ~np.isnan(vals) & ~np.isnan(q_depths)
            if valid.sum() < 30:
                continue
            rho, p = stats.spearmanr(q_depths[valid], vals[valid])
            q_res[m] = {
                "spearman_rho": round(float(rho), 4),
                "spearman_p": float(p),
                "n_valid": int(valid.sum()),
            }
        result[q_label] = {"n": int(q_n), "correlations": q_res}
        log.info(f"  {q_label} (n={q_n})")

    return result


def obd_sanity_check(depths, obd_features):
    if not obd_features:
        return {}
    result = {}
    for feat in OBD_FEAT_COLS:
        if feat not in obd_features:
            continue
        vals = obd_features[feat]
        valid = ~np.isnan(vals) & ~np.isnan(depths.astype(float))
        if valid.sum() < 30:
            continue
        rho, p = stats.spearmanr(depths[valid].astype(float), vals[valid])
        result[feat] = {
            "spearman_rho": round(float(rho), 4),
            "spearman_p": float(p),
            "n_valid": int(valid.sum()),
            "note": "overlaps with OBD feature, reported as sanity check only",
        }
    return result


# ── Visualization ──

def make_plots(depths, indep_metrics, mauve_scores):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    # 1. Violin plot: 6 independent metrics by depth bin (2x3 grid)
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    axes = axes.flatten()

    bin_defs = [("0", lambda d: d == 0), ("1", lambda d: d == 1),
                ("2", lambda d: d == 2), ("3+", lambda d: d >= 3)]

    for idx, m in enumerate(INDEPENDENT_COLS):
        ax = axes[idx]
        plot_data = []
        plot_labels = []
        for label, fn in bin_defs:
            mask = fn(depths)
            vals = indep_metrics[m][mask]
            valid = vals[~np.isnan(vals)]
            if len(valid) >= 5:
                plot_data.append(valid)
                plot_labels.append(label)

        if len(plot_data) >= 2:
            vp = ax.violinplot(plot_data, showmedians=True, showextrema=False)
            for body in vp["bodies"]:
                body.set_alpha(0.7)
            ax.set_xticks(range(1, len(plot_labels) + 1))
            ax.set_xticklabels([f"d={l}" for l in plot_labels])

            q1s = [np.percentile(d, 25) for d in plot_data]
            q3s = [np.percentile(d, 75) for d in plot_data]
            all_vals = np.concatenate(plot_data)
            lo = np.percentile(all_vals, 1)
            hi = np.percentile(all_vals, 99)
            ax.set_ylim(lo, hi)

        ax.set_title(INDEPENDENT_LABELS.get(m, m), fontsize=10)
        ax.set_xlabel("Predicted Depth")

    plt.suptitle("Independent Quality Metrics by OBD Predicted Depth", fontsize=13)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_DIR / "independent_violin.pdf", bbox_inches="tight")
    fig.savefig(OUT_DIR / "independent_violin.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    log.info("Saved independent_violin.pdf/png")

    # 2. Depth distribution histogram
    fig, ax = plt.subplots(figsize=(7, 4))
    unique, counts = np.unique(depths, return_counts=True)
    ax.bar(unique, counts, color="#4C72B0", edgecolor="white")
    for u, c in zip(unique, counts):
        ax.text(u, c + max(counts) * 0.01, str(c), ha="center", va="bottom", fontsize=9)
    ax.set_xlabel("Predicted OBD Depth")
    ax.set_ylabel("Count")
    ax.set_title(f"CC Text Predicted Depth Distribution (n={len(depths)})")
    ax.set_xticks(unique)
    plt.tight_layout()
    fig.savefig(OUT_DIR / "depth_distribution.pdf", bbox_inches="tight")
    fig.savefig(OUT_DIR / "depth_distribution.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    log.info("Saved depth_distribution.pdf/png")

    # 3. MAUVE by depth bin
    if mauve_scores:
        fig, ax = plt.subplots(figsize=(6, 4))
        labels = sorted(mauve_scores.keys(), key=lambda x: (0 if x.isdigit() else 1, x))
        vals = [mauve_scores[l] for l in labels if mauve_scores[l] is not None]
        valid_labels = [l for l in labels if mauve_scores[l] is not None]
        bars = ax.bar(range(len(valid_labels)), vals, color="#DD8452", edgecolor="white")
        for bar, v in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.005,
                    f"{v:.3f}", ha="center", va="bottom", fontsize=9)
        ax.set_xticks(range(len(valid_labels)))
        ax.set_xticklabels([f"d={l} vs d=0" for l in valid_labels])
        ax.set_ylabel("MAUVE Score")
        ax.set_title("MAUVE Score by Depth Bin (vs Depth 0)")
        ax.set_ylim(0, 1.05)
        plt.tight_layout()
        fig.savefig(OUT_DIR / "mauve_by_bin.pdf", bbox_inches="tight")
        fig.savefig(OUT_DIR / "mauve_by_bin.png", dpi=150, bbox_inches="tight")
        plt.close(fig)
        log.info("Saved mauve_by_bin.pdf/png")


def main():
    t0 = time.time()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    log.info("=" * 60)
    log.info("exp-014 v2: Independent Correlation Analysis")
    log.info("=" * 60)

    predicted_depths, expected_depths, indep_metrics, obd_features, text_lengths = load_data()

    results = {}

    # 1. Independent correlation (primary evidence)
    log.info("1. Independent metrics correlation (Bonferroni-corrected) ...")
    corr, alpha = correlation_analysis(predicted_depths, indep_metrics)
    results["independent_metrics"] = corr
    results["bonferroni_alpha"] = alpha

    # 2. Stratified by depth bin
    log.info("2. Stratified analysis by depth bin ...")
    results["stratified"] = stratified_analysis(predicted_depths, indep_metrics)

    # 3. Statistical tests
    log.info("3. Statistical tests (KW, Mann-Whitney, Cliff's delta) ...")
    results["statistical_tests"] = statistical_tests(predicted_depths, indep_metrics)

    # 4. Length-controlled
    log.info("4. Length-controlled correlation ...")
    results["length_controlled"] = length_controlled_analysis(
        predicted_depths, indep_metrics, text_lengths
    )

    # 5. OBD sanity check
    log.info("5. OBD feature sanity check (these overlap with model features) ...")
    results["sanity_check_obd_features"] = obd_sanity_check(predicted_depths, obd_features)

    # 6. Depth distribution
    results["depth_distribution"] = {
        str(d): int((predicted_depths == d).sum())
        for d in range(int(predicted_depths.max()) + 1)
    }
    results["num_samples"] = int(len(predicted_depths))

    # 7. MAUVE scores
    mauve_path = OUT_DIR / "mauve_independent.json"
    mauve_scores = {}
    if mauve_path.exists():
        with open(mauve_path) as f:
            mauve_scores = json.load(f)
    results["mauve_by_bin"] = mauve_scores

    # 8. Visualization
    log.info("6. Generating plots ...")
    make_plots(predicted_depths, indep_metrics, mauve_scores)

    # Save
    out_path = OUT_DIR / "independent_analysis_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    log.info(f"Results saved to {out_path}")

    elapsed = time.time() - t0
    log.info("=" * 60)
    log.info(f"Analysis complete in {elapsed:.0f}s")
    log.info("Key independent correlations:")
    for m in INDEPENDENT_COLS:
        if m in corr:
            r = corr[m]
            log.info(f"  {m}: rho={r['spearman_rho']:.4f} (p={r['spearman_p']:.2e}), CI={r['bootstrap_ci_95']}")
    if mauve_scores:
        log.info(f"MAUVE by bin: {mauve_scores}")
    log.info("=" * 60)


if __name__ == "__main__":
    main()
