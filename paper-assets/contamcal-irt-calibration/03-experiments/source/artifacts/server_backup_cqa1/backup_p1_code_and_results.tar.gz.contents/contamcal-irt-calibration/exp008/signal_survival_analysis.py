"""
exp-008 Signal Survival Analysis — core analysis module.
v2: Extended from SFT/RL pairwise to N-regime comparison.

Computes:
  - AUC matrix: N_signals x N_regimes AUROC for contamination detection
  - Pairwise tests: statistical tests between all adjacent regime pairs
    (Cohen's d, Spearman rho, AUROC ratio, Wilcoxon signed-rank)

Input:  OrderedDict mapping regime_name -> {signal_key: [records]}, plus labels.
Output: {regime_names, auc_matrix, pairwise_tests, per_signal (compat), summary}
"""

import json
import logging
from collections import OrderedDict
from pathlib import Path

import numpy as np
from scipy import stats
from sklearn.metrics import roc_auc_score

logger = logging.getLogger(__name__)

SIGNAL_KEYS = ["s1_embedding", "s2_minkpp", "s3_constat", "s4_selfcritique"]
SIGNAL_LABELS = {
    "s1_embedding": "Embedding",
    "s2_minkpp": "Min-K%++",
    "s3_constat": "ConStat",
    "s4_selfcritique": "Self-Critique",
}


def cohens_d(group1: np.ndarray, group2: np.ndarray) -> float:
    """Cohen's d effect size between two groups."""
    n1, n2 = len(group1), len(group2)
    if n1 < 2 or n2 < 2:
        return float("nan")
    var1 = group1.var(ddof=1)
    var2 = group2.var(ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    if pooled_std == 0:
        return float("nan")
    return (group1.mean() - group2.mean()) / pooled_std


def compute_single_regime_metrics(values: np.ndarray, labels: np.ndarray) -> dict:
    """AUROC and Cohen's d for contamination detection in one regime."""
    mask = ~(np.isnan(values) | np.isnan(labels))
    v = values[mask]
    lab = labels[mask].astype(int)
    contam = lab == 1
    clean = lab == 0

    result = {
        "n_items": int(mask.sum()),
        "n_contaminated": int(contam.sum()),
        "n_clean": int(clean.sum()),
    }

    d = cohens_d(v[contam], v[clean])
    result["effect_size"] = round(d, 4) if not np.isnan(d) else None

    if contam.sum() > 0 and clean.sum() > 0:
        result["auroc"] = round(float(roc_auc_score(lab, v)), 4)
    else:
        result["auroc"] = None

    return result


def compute_pairwise_metrics(
    values_a: np.ndarray,
    values_b: np.ndarray,
    labels: np.ndarray,
) -> dict:
    """
    Pairwise survival metrics between two regimes for one signal.
    Preserves all original statistical tests: Cohen's d, Spearman, AUC, Wilcoxon.
    """
    mask = ~(np.isnan(values_a) | np.isnan(values_b) | np.isnan(labels))
    v_a = values_a[mask]
    v_b = values_b[mask]
    lab = labels[mask].astype(int)

    contam = lab == 1
    clean = lab == 0

    result = {
        "n_items": int(mask.sum()),
        "n_contaminated": int(contam.sum()),
        "n_clean": int(clean.sum()),
    }

    d_a = cohens_d(v_a[contam], v_a[clean])
    d_b = cohens_d(v_b[contam], v_b[clean])
    result["effect_size_a"] = round(d_a, 4)
    result["effect_size_b"] = round(d_b, 4)
    result["effect_size_ratio"] = (
        round(d_b / d_a, 4) if d_a != 0 and not np.isnan(d_a) else None
    )

    if len(v_a) >= 3:
        rho, rho_p = stats.spearmanr(v_a, v_b)
        result["spearman_rho"] = round(rho, 4)
        result["spearman_p"] = float(f"{rho_p:.2e}")
    else:
        result["spearman_rho"] = None
        result["spearman_p"] = None

    if result["n_contaminated"] > 0 and result["n_clean"] > 0:
        auc_a = roc_auc_score(lab, v_a)
        auc_b = roc_auc_score(lab, v_b)
        result["auc_a"] = round(auc_a, 4)
        result["auc_b"] = round(auc_b, 4)
        result["auc_ratio"] = round(auc_b / auc_a, 4) if auc_a > 0 else None
    else:
        result["auc_a"] = None
        result["auc_b"] = None
        result["auc_ratio"] = None

    diffs = v_b - v_a
    nonzero_diffs = diffs[diffs != 0]
    if len(nonzero_diffs) >= 10:
        w_stat, w_p = stats.wilcoxon(nonzero_diffs)
        result["wilcoxon_stat"] = float(w_stat)
        result["wilcoxon_p"] = float(f"{w_p:.2e}")
    else:
        result["wilcoxon_stat"] = None
        result["wilcoxon_p"] = None

    return result


def _extract_signal_vectors(
    regime_signals: dict,
    sig_key: str,
    regime_names: list[str],
    contamination_labels: dict[int, int],
) -> tuple:
    """Extract aligned signal vectors for one signal across all regimes."""
    regime_maps = {}
    for rname in regime_names:
        data = regime_signals[rname].get(sig_key, [])
        regime_maps[rname] = {r["index"]: r.get(sig_key) for r in data}

    common_idx = set(contamination_labels.keys())
    for rname in regime_names:
        common_idx &= set(regime_maps[rname].keys())
    common_idx = sorted(common_idx)

    if len(common_idx) < 10:
        return None, None, None

    labels = np.array([contamination_labels[i] for i in common_idx], dtype=float)
    vectors = OrderedDict()
    for rname in regime_names:
        vectors[rname] = np.array(
            [regime_maps[rname][i] for i in common_idx], dtype=float
        )

    return vectors, labels, common_idx


def run_survival_analysis(
    regime_signals: OrderedDict,
    contamination_labels: dict[int, int],
) -> dict:
    """
    N-regime survival analysis.

    Args:
        regime_signals: OrderedDict {regime_name: {signal_key: [records]}}
        contamination_labels: {item_index: 0 or 1}

    Returns dict with keys:
        regime_names, auc_matrix, effect_size_matrix,
        pairwise_tests, per_signal (backward compat for N=2), summary.
    """
    regime_names = list(regime_signals.keys())
    n_regimes = len(regime_names)

    auc_matrix: dict[str, dict[str, float | None]] = {}
    effect_size_matrix: dict[str, dict[str, float | None]] = {}
    pairwise_tests: OrderedDict[str, dict] = OrderedDict()

    adjacent_pairs = [
        (regime_names[i], regime_names[i + 1]) for i in range(n_regimes - 1)
    ]
    for ra, rb in adjacent_pairs:
        pairwise_tests[f"{ra}_vs_{rb}"] = {}

    for sig_key in SIGNAL_KEYS:
        vectors, labels, common_idx = _extract_signal_vectors(
            regime_signals, sig_key, regime_names, contamination_labels,
        )
        if vectors is None:
            logger.warning("Skipping %s: <10 common items", sig_key)
            continue

        auc_matrix[sig_key] = {}
        effect_size_matrix[sig_key] = {}
        for rname in regime_names:
            m = compute_single_regime_metrics(vectors[rname], labels)
            auc_matrix[sig_key][rname] = m["auroc"]
            effect_size_matrix[sig_key][rname] = m["effect_size"]

        for ra, rb in adjacent_pairs:
            pair_key = f"{ra}_vs_{rb}"
            pm = compute_pairwise_metrics(vectors[ra], vectors[rb], labels)
            pm["signal_label"] = SIGNAL_LABELS[sig_key]
            pairwise_tests[pair_key][sig_key] = pm

        logger.info(
            "%s: AUC %s",
            SIGNAL_LABELS[sig_key],
            " -> ".join(
                f"{r}={auc_matrix[sig_key].get(r, 'N/A')}" for r in regime_names
            ),
        )

    # Backward compat per_signal (maps first adjacent pair to old SFT/RL keys)
    per_signal: dict[str, dict] = {}
    if adjacent_pairs:
        first_pair_key = f"{adjacent_pairs[0][0]}_vs_{adjacent_pairs[0][1]}"
        for sig_key, pm in pairwise_tests.get(first_pair_key, {}).items():
            per_signal[sig_key] = {
                "signal_label": SIGNAL_LABELS.get(sig_key, sig_key),
                "n_items": pm["n_items"],
                "n_contaminated": pm["n_contaminated"],
                "n_clean": pm["n_clean"],
                "effect_size_sft": pm["effect_size_a"],
                "effect_size_rl": pm["effect_size_b"],
                "effect_size_ratio": pm.get("effect_size_ratio"),
                "spearman_rho": pm.get("spearman_rho"),
                "spearman_p": pm.get("spearman_p"),
                "auc_sft": pm.get("auc_a"),
                "auc_rl": pm.get("auc_b"),
                "auc_ratio": pm.get("auc_ratio"),
                "wilcoxon_stat": pm.get("wilcoxon_stat"),
                "wilcoxon_p": pm.get("wilcoxon_p"),
            }

    # Summary: signal "survives" if last regime AUC >= 0.6 and d-ratio >= 0.5
    last_regime = regime_names[-1]
    first_regime = regime_names[0]
    surviving = []
    for sig_key in auc_matrix:
        auc_last = auc_matrix[sig_key].get(last_regime)
        d_first = effect_size_matrix.get(sig_key, {}).get(first_regime)
        d_last = effect_size_matrix.get(sig_key, {}).get(last_regime)
        if (
            auc_last is not None
            and auc_last >= 0.6
            and d_first is not None
            and d_last is not None
            and d_first != 0
            and d_last / d_first >= 0.5
        ):
            surviving.append(sig_key)

    auc_ratios = []
    spearman_rhos = []
    if adjacent_pairs:
        first_pair_key = f"{adjacent_pairs[0][0]}_vs_{adjacent_pairs[0][1]}"
        for pm in pairwise_tests.get(first_pair_key, {}).values():
            if pm.get("auc_ratio") is not None:
                auc_ratios.append(pm["auc_ratio"])
            if pm.get("spearman_rho") is not None:
                spearman_rhos.append(pm["spearman_rho"])

    summary = {
        "n_regimes": n_regimes,
        "regime_names": regime_names,
        "n_signals_analyzed": len(auc_matrix),
        "n_signals_surviving": len(surviving),
        "surviving_signals": surviving,
        "mean_auc_ratio": round(np.mean(auc_ratios), 4) if auc_ratios else None,
        "mean_spearman_rho": round(np.mean(spearman_rhos), 4) if spearman_rhos else None,
    }

    return {
        "regime_names": regime_names,
        "auc_matrix": auc_matrix,
        "effect_size_matrix": effect_size_matrix,
        "pairwise_tests": dict(pairwise_tests),
        "per_signal": per_signal,
        "summary": summary,
    }


def save_report(report: dict, output_dir: str | Path) -> Path:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / "survival_report.json"
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2)
    logger.info("Report saved to %s", out_path)
    return out_path


def print_summary_table(report: dict):
    """Print a formatted summary table to stdout."""
    regime_names = report.get("regime_names", [])
    auc_matrix = report.get("auc_matrix", {})
    pairwise_tests = report.get("pairwise_tests", {})
    summary = report["summary"]

    if len(regime_names) == 2 and report.get("per_signal"):
        _print_legacy_table(report)
        return

    # N-regime AUC matrix table
    col_w = 10
    sig_w = 16
    header_parts = [f"{'Signal':<{sig_w}}"]
    for rname in regime_names:
        header_parts.append(f"{rname:>{col_w}}")
    header = " ".join(header_parts)

    print("\n" + "=" * len(header))
    print(
        f"Signal Survival Analysis -- {len(regime_names)} regimes: "
        f"{' -> '.join(regime_names)}"
    )
    print("=" * len(header))
    print(header)
    print("-" * len(header))

    for sig_key in SIGNAL_KEYS:
        if sig_key not in auc_matrix:
            continue
        line_parts = [f"{SIGNAL_LABELS[sig_key]:<{sig_w}}"]
        for rname in regime_names:
            v = auc_matrix[sig_key].get(rname)
            s = f"{v:.4f}" if v is not None else "N/A"
            line_parts.append(f"{s:>{col_w}}")
        print(" ".join(line_parts))

    print("-" * len(header))

    for pair_key, pair_data in pairwise_tests.items():
        ra, rb = pair_key.split("_vs_")
        ratios = [
            m["auc_ratio"]
            for m in pair_data.values()
            if m.get("auc_ratio") is not None
        ]
        rhos = [
            m["spearman_rho"]
            for m in pair_data.values()
            if m.get("spearman_rho") is not None
        ]
        if ratios:
            print(
                f"  {ra} -> {rb}: mean AUC ratio={np.mean(ratios):.3f}, "
                f"mean rho={np.mean(rhos):.3f}"
            )
        else:
            print(f"  {ra} -> {rb}: no data")

    print(
        f"\nSurviving signals: {summary['n_signals_surviving']}"
        f"/{summary['n_signals_analyzed']}  "
        f"({', '.join(summary['surviving_signals']) or 'none'})"
    )
    print("=" * len(header) + "\n")


def _print_legacy_table(report: dict):
    """Original 2-regime table format for backward compatibility."""
    per_signal = report["per_signal"]
    summary = report["summary"]

    header = (
        f"{'Signal':<16} {'d(SFT)':>8} {'d(RL)':>8} {'d ratio':>8} "
        f"{'AUC(SFT)':>9} {'AUC(RL)':>9} {'AUC ratio':>10} "
        f"{'rho':>8} {'Wilcox p':>10} {'n':>6}"
    )
    print("\n" + "=" * len(header))
    print("Signal Survival Analysis -- SFT vs RL-aligned")
    print("=" * len(header))
    print(header)
    print("-" * len(header))

    for sig_key in SIGNAL_KEYS:
        m = per_signal.get(sig_key)
        if m is None:
            continue
        fmt = lambda v, d=4: f"{v:.{d}f}" if v is not None else "N/A"
        print(
            f"{m['signal_label']:<16} "
            f"{fmt(m['effect_size_sft']):>8} "
            f"{fmt(m['effect_size_rl']):>8} "
            f"{fmt(m.get('effect_size_ratio'), 2):>8} "
            f"{fmt(m.get('auc_sft')):>9} "
            f"{fmt(m.get('auc_rl')):>9} "
            f"{fmt(m.get('auc_ratio'), 2):>10} "
            f"{fmt(m.get('spearman_rho')):>8} "
            f"{fmt(m.get('wilcoxon_p'), 2):>10} "
            f"{m['n_items']:>6}"
        )

    print("-" * len(header))
    print(
        f"Surviving signals: {summary['n_signals_surviving']}"
        f"/{summary['n_signals_analyzed']}  "
        f"({', '.join(summary['surviving_signals']) or 'none'})"
    )
    print(
        f"Mean AUC ratio: {summary.get('mean_auc_ratio', 'N/A')}  |  "
        f"Mean Spearman rho: {summary.get('mean_spearman_rho', 'N/A')}"
    )
    print("=" * len(header) + "\n")
