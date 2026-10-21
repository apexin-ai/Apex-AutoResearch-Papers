"""
Evaluate calibration quality: IRT 4PL+gamma vs 7 baselines.

8 metrics:
  1. MAE -- mean absolute error (calibrated vs ground-truth clean scores)
  2. ECE -- expected calibration error (binned)
  3. MCE -- maximum calibration error (binned)
  4. Brier Score -- mean squared error
  5. Coverage -- fraction of ground-truth within 50/80/95% CIs
  6. Sharpness -- mean CI width (lower is better, conditional on coverage)
  7. Kendall tau -- rank correlation preservation
  8. Dose-response monotonicity -- gamma or calibration error increases with dosage

Input: IRT result JSONs + baseline result JSON + ground-truth clean scores
Output: per-method metrics JSON + LaTeX comparison table + reliability diagram data

Dependencies: numpy, scipy
"""

import argparse
import json
import logging
import os

import numpy as np
from scipy import stats

log = logging.getLogger(__name__)

SEED = 42
N_BOOTSTRAP = 1000


# ── Metrics ──

def metric_mae(calibrated, ground_truth):
    """Mean Absolute Error between calibrated and ground-truth scores."""
    return float(np.mean(np.abs(np.array(calibrated) - np.array(ground_truth))))


def metric_brier(calibrated, ground_truth):
    """Brier Score (MSE) between calibrated and ground-truth scores."""
    return float(np.mean((np.array(calibrated) - np.array(ground_truth)) ** 2))


def metric_ece(calibrated, ground_truth, n_bins=10):
    """Expected Calibration Error: weighted average of per-bin |mean_cal - mean_gt|."""
    cal = np.array(calibrated)
    gt = np.array(ground_truth)
    n = len(cal)
    if n == 0:
        return 0.0
    bin_edges = np.linspace(cal.min() - 1e-8, cal.max() + 1e-8, n_bins + 1)
    ece = 0.0
    for k in range(n_bins):
        mask = (cal >= bin_edges[k]) & (cal < bin_edges[k + 1])
        n_k = mask.sum()
        if n_k == 0:
            continue
        ece += (n_k / n) * abs(cal[mask].mean() - gt[mask].mean())
    return float(ece)


def metric_mce(calibrated, ground_truth, n_bins=10):
    """Maximum Calibration Error: max per-bin |mean_cal - mean_gt|."""
    cal = np.array(calibrated)
    gt = np.array(ground_truth)
    if len(cal) == 0:
        return 0.0
    bin_edges = np.linspace(cal.min() - 1e-8, cal.max() + 1e-8, n_bins + 1)
    max_err = 0.0
    for k in range(n_bins):
        mask = (cal >= bin_edges[k]) & (cal < bin_edges[k + 1])
        if mask.sum() == 0:
            continue
        err = abs(cal[mask].mean() - gt[mask].mean())
        max_err = max(max_err, err)
    return float(max_err)


def reliability_diagram_data(calibrated, ground_truth, n_bins=10):
    """Bin data for reliability diagram plotting.

    Returns list of dicts with bin_center, mean_calibrated, mean_ground_truth, count.
    """
    cal = np.array(calibrated)
    gt = np.array(ground_truth)
    if len(cal) == 0:
        return []
    bin_edges = np.linspace(cal.min() - 1e-8, cal.max() + 1e-8, n_bins + 1)
    bins = []
    for k in range(n_bins):
        mask = (cal >= bin_edges[k]) & (cal < bin_edges[k + 1])
        n_k = int(mask.sum())
        if n_k == 0:
            continue
        bins.append({
            "bin_lower": round(float(bin_edges[k]), 6),
            "bin_upper": round(float(bin_edges[k + 1]), 6),
            "bin_center": round(float((bin_edges[k] + bin_edges[k + 1]) / 2), 6),
            "mean_calibrated": round(float(cal[mask].mean()), 6),
            "mean_ground_truth": round(float(gt[mask].mean()), 6),
            "count": n_k,
        })
    return bins


def metric_coverage(ci_lower, ci_upper, ground_truth):
    """Fraction of ground-truth values falling within the CI."""
    if ci_lower is None or ci_upper is None:
        return None
    gt = np.array(ground_truth)
    lo = np.array(ci_lower)
    hi = np.array(ci_upper)
    return float(np.mean((gt >= lo) & (gt <= hi)))


def metric_sharpness(ci_lower, ci_upper):
    """Mean CI width -- measures precision of uncertainty estimates."""
    if ci_lower is None or ci_upper is None:
        return None
    return float(np.mean(np.array(ci_upper) - np.array(ci_lower)))


def metric_kendall_tau(calibrated, ground_truth):
    """Kendall rank correlation between calibrated and ground-truth ordering."""
    cal = np.array(calibrated)
    gt = np.array(ground_truth)
    if len(np.unique(cal)) < 2 or len(np.unique(gt)) < 2:
        return {"tau": 0.0, "p_value": 1.0}
    tau, p_value = stats.kendalltau(cal, gt)
    return {"tau": round(float(tau), 4), "p_value": round(float(p_value), 6)}


def metric_dose_response(gamma_stats):
    """Check if gamma is positive and 95% CI excludes zero."""
    if gamma_stats is None:
        return None
    return {
        "gamma_mean": gamma_stats.get("mean", 0),
        "gamma_positive": gamma_stats.get("mean", 0) > 0,
        "ci_excludes_zero": gamma_stats.get("ci_excludes_zero", False),
        "q025": gamma_stats.get("q025", 0),
        "q975": gamma_stats.get("q975", 0),
    }


def bootstrap_metric(metric_fn, calibrated, ground_truth,
                     n_boot=N_BOOTSTRAP, seed=SEED):
    """Bootstrap 95% CI for a scalar metric."""
    rng = np.random.default_rng(seed)
    cal = np.array(calibrated)
    gt = np.array(ground_truth)
    n = len(cal)
    vals = np.empty(n_boot)
    for b in range(n_boot):
        idx = rng.choice(n, size=n, replace=True)
        vals[b] = metric_fn(cal[idx], gt[idx])
    return {
        "mean": round(float(np.mean(vals)), 6),
        "ci_lower": round(float(np.percentile(vals, 2.5)), 6),
        "ci_upper": round(float(np.percentile(vals, 97.5)), 6),
    }


# ── Evaluation ──

def evaluate_method(method_name, scores, ground_truth,
                    ci_lower=None, ci_upper=None,
                    ci_80_lower=None, ci_80_upper=None,
                    ci_50_lower=None, ci_50_upper=None,
                    gamma_stats=None, dosages=None):
    """Evaluate a single calibration method on all 8 metrics."""
    cal = np.array(scores)
    gt = np.array(ground_truth)

    result = {"method": method_name}

    # 1. MAE
    mae = metric_mae(cal, gt)
    mae_boot = bootstrap_metric(
        lambda c, g: float(np.mean(np.abs(c - g))), cal, gt)
    result["mae"] = {"value": round(mae, 6), "bootstrap_95ci": mae_boot}

    # 2. ECE
    ece = metric_ece(cal, gt)
    ece_boot = bootstrap_metric(
        lambda c, g: metric_ece(c, g), cal, gt)
    result["ece"] = {"value": round(ece, 6), "bootstrap_95ci": ece_boot}

    # 3. MCE
    mce = metric_mce(cal, gt)
    result["mce"] = round(mce, 6)

    # 4. Brier Score
    brier = metric_brier(cal, gt)
    brier_boot = bootstrap_metric(
        lambda c, g: float(np.mean((c - g) ** 2)), cal, gt)
    result["brier"] = {"value": round(brier, 6), "bootstrap_95ci": brier_boot}

    # 5. Coverage at 50%, 80%, 95%
    result["coverage_95"] = metric_coverage(ci_lower, ci_upper, gt)
    result["coverage_80"] = metric_coverage(ci_80_lower, ci_80_upper, gt)
    result["coverage_50"] = metric_coverage(ci_50_lower, ci_50_upper, gt)

    # 6. Sharpness
    result["sharpness_95"] = metric_sharpness(ci_lower, ci_upper)
    result["sharpness_80"] = metric_sharpness(ci_80_lower, ci_80_upper)
    result["sharpness_50"] = metric_sharpness(ci_50_lower, ci_50_upper)

    # 7. Kendall tau
    kt = metric_kendall_tau(cal, gt)
    kt_boot = bootstrap_metric(
        lambda c, g: float(stats.kendalltau(c, g).statistic)
        if len(np.unique(c)) >= 2 else 0.0,
        cal, gt)
    result["kendall_tau"] = {**kt, "bootstrap_95ci": kt_boot}

    # 8. Dose-response
    result["dose_response"] = metric_dose_response(gamma_stats)

    # Auxiliary: calibration error monotonicity with dosage
    if dosages is not None and len(dosages) == len(cal):
        cal_errors = np.abs(cal - gt)
        doses = np.array(dosages)
        if len(np.unique(doses)) >= 3:
            tau_dose, _ = stats.kendalltau(doses, cal_errors)
            result["dose_monotonicity_tau"] = round(float(tau_dose), 4)

    # Reliability diagram data
    result["reliability_diagram"] = reliability_diagram_data(cal, gt)

    return result


# ── Output Formatting ──

def format_latex_table(all_metrics):
    """Format results as LaTeX table for paper."""
    header = (
        "\\begin{table}[t]\n\\centering\n\\small\n"
        "\\caption{Calibration evaluation: IRT vs.\\ baselines}\n"
        "\\label{tab:calibration-eval}\n"
        "\\begin{tabular}{lcccccccccc}\n\\toprule\n"
        "Method & MAE $\\downarrow$ & ECE $\\downarrow$ & Brier $\\downarrow$ "
        "& Cov@50\\% & Cov@80\\% & Cov@95\\% "
        "& Sharp$_{95}$ $\\downarrow$ & $\\tau$ $\\uparrow$ & $\\gamma > 0$ \\\\\n"
        "\\midrule\n"
    )

    rows = []
    for m in all_metrics:
        name = m["method"].replace("_", "\\_")
        mae_val = f"{m['mae']['value']:.4f}"
        ece_val = f"{m['ece']['value']:.4f}"
        brier_val = f"{m['brier']['value']:.4f}"

        def _fc(key):
            v = m.get(key)
            return f"{v:.0%}" if v is not None else "---"

        def _fs(key):
            v = m.get(key)
            return f"{v:.4f}" if v is not None else "---"

        dr = m.get("dose_response")
        if dr:
            dr_str = f"{dr['gamma_mean']:.3f}"
            if dr["ci_excludes_zero"]:
                dr_str += "*"
        else:
            dr_str = "---"

        rows.append(
            f"{name} & {mae_val} & {ece_val} & {brier_val} "
            f"& {_fc('coverage_50')} & {_fc('coverage_80')} "
            f"& {_fc('coverage_95')} & {_fs('sharpness_95')} "
            f"& {m['kendall_tau']['tau']:.3f} & {dr_str} \\\\"
        )

    footer = "\\bottomrule\n\\end{tabular}\n\\end{table}"
    return header + "\n".join(rows) + "\n" + footer


def format_text_table(all_metrics):
    """Format results as plain-text table for console output."""
    header = (f"{'Method':<30} {'MAE':>8} {'ECE':>8} {'Brier':>8} "
              f"{'C50':>6} {'C80':>6} {'C95':>6} {'S95':>8} {'tau':>6} {'gamma>0':>8}")
    sep = "-" * len(header)
    lines = [sep, header, sep]

    for m in all_metrics:
        name = m["method"][:28]
        mae = f"{m['mae']['value']:.4f}"
        ece = f"{m['ece']['value']:.4f}"
        brier = f"{m['brier']['value']:.4f}"

        def _f(key):
            v = m.get(key)
            return f"{v:.2f}" if v is not None else "  ---"

        dr = m.get("dose_response")
        dr_str = f"{dr['gamma_mean']:.3f}" if dr else "     ---"

        lines.append(
            f"{name:<30} {mae:>8} {ece:>8} {brier:>8} "
            f"{_f('coverage_50'):>6} {_f('coverage_80'):>6} "
            f"{_f('coverage_95'):>6} {_f('sharpness_95'):>8} "
            f"{m['kendall_tau']['tau']:>6.3f} {dr_str:>8}"
        )

    lines.append(sep)
    return "\n".join(lines)


# ── CLI ──

def main():
    parser = argparse.ArgumentParser(description="Evaluate calibration methods")
    parser.add_argument("--irt-results", nargs="+", required=True,
                        help="IRT result JSON files")
    parser.add_argument("--baseline-results", required=True,
                        help="Baselines JSON file")
    parser.add_argument("--ground-truth", required=True,
                        help="Ground truth clean accuracy (JSON/CSV/NPY)")
    parser.add_argument("--benchmark", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--dosages", type=str, default=None,
                        help="JSON list of dosage values per model")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")
    os.makedirs(args.output_dir, exist_ok=True)

    # Load ground truth
    ext = os.path.splitext(args.ground_truth)[1].lower()
    if ext == ".json":
        with open(args.ground_truth) as f:
            gt_data = json.load(f)
        if isinstance(gt_data, dict):
            ground_truth = gt_data.get(
                "clean_accuracy",
                gt_data.get("scores", list(gt_data.values())))
        else:
            ground_truth = gt_data
    elif ext == ".npy":
        ground_truth = np.load(args.ground_truth).tolist()
    elif ext == ".csv":
        ground_truth = np.loadtxt(
            args.ground_truth, delimiter=",", skiprows=1).tolist()
    else:
        raise ValueError(f"Unsupported format: {ext}")

    dosages = json.loads(args.dosages) if args.dosages else None
    log.info("Ground truth: %d models", len(ground_truth))

    all_metrics = []

    # Evaluate IRT models
    for irt_path in args.irt_results:
        with open(irt_path) as f:
            irt = json.load(f)
        model_type = irt.get("model_type", "unknown")
        cal = irt["parameters"]["calibrated_scores"]
        gamma_stats = irt["parameters"].get("gamma")

        m = evaluate_method(
            method_name=f"IRT_{model_type}",
            scores=cal["mean"],
            ground_truth=ground_truth,
            ci_lower=cal.get("q025"), ci_upper=cal.get("q975"),
            ci_80_lower=cal.get("q10"), ci_80_upper=cal.get("q90"),
            ci_50_lower=cal.get("q25"), ci_50_upper=cal.get("q75"),
            gamma_stats=gamma_stats,
            dosages=dosages,
        )
        all_metrics.append(m)
        log.info("IRT_%s: MAE=%.4f, ECE=%.4f, Brier=%.4f, tau=%.3f",
                 model_type, m["mae"]["value"], m["ece"]["value"],
                 m["brier"]["value"], m["kendall_tau"]["tau"])

    # Evaluate baselines
    with open(args.baseline_results) as f:
        baselines = json.load(f)
    for bname, bdata in baselines.items():
        if "error" in bdata:
            log.warning("Skipping %s (errored)", bname)
            continue
        m = evaluate_method(
            method_name=bname,
            scores=bdata["calibrated_scores"],
            ground_truth=ground_truth,
            ci_lower=bdata.get("ci_lower"),
            ci_upper=bdata.get("ci_upper"),
            ci_80_lower=bdata.get("ci_80_lower"),
            ci_80_upper=bdata.get("ci_80_upper"),
            ci_50_lower=bdata.get("ci_50_lower"),
            ci_50_upper=bdata.get("ci_50_upper"),
            dosages=dosages,
        )
        all_metrics.append(m)
        log.info("%s: MAE=%.4f, ECE=%.4f, Brier=%.4f, tau=%.3f",
                 bname, m["mae"]["value"], m["ece"]["value"],
                 m["brier"]["value"], m["kendall_tau"]["tau"])

    # Print
    print(format_text_table(all_metrics))

    # Save
    out_path = os.path.join(
        args.output_dir, f"{args.benchmark}_evaluation.json")
    with open(out_path, "w") as f:
        json.dump(all_metrics, f, indent=2)
    log.info("Evaluation saved to %s", out_path)

    tex_path = os.path.join(
        args.output_dir, f"{args.benchmark}_evaluation.tex")
    with open(tex_path, "w") as f:
        f.write(format_latex_table(all_metrics))
    log.info("LaTeX table saved to %s", tex_path)


if __name__ == "__main__":
    main()
