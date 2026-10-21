# exp-006: Evaluate calibration quality across IRT and baselines
# 5 metrics: MAE, Coverage, Sharpness, Kendall τ, Dose-response monotonicity

import argparse
import json
import logging
import os

import numpy as np
from scipy import stats

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

SEED = 42
N_BOOTSTRAP = 1000


def load_json(path):
    with open(path) as f:
        return json.load(f)


def metric_mae(calibrated, ground_truth):
    return float(np.mean(np.abs(np.array(calibrated) - np.array(ground_truth))))


def metric_coverage(ci_lower, ci_upper, ground_truth, level_name="95%"):
    if ci_lower is None or ci_upper is None:
        return None
    gt = np.array(ground_truth)
    lo = np.array(ci_lower)
    hi = np.array(ci_upper)
    covered = np.mean((gt >= lo) & (gt <= hi))
    return float(covered)


def metric_sharpness(ci_lower, ci_upper):
    if ci_lower is None or ci_upper is None:
        return None
    width = np.array(ci_upper) - np.array(ci_lower)
    return float(np.mean(width))


def metric_kendall_tau(calibrated, ground_truth):
    tau, p_value = stats.kendalltau(calibrated, ground_truth)
    return {"tau": round(float(tau), 4), "p_value": round(float(p_value), 6)}


def metric_dose_response(gamma_stats):
    """Check if gamma is positive and significantly different from zero.
    For baselines without gamma, return None.
    """
    if gamma_stats is None:
        return None
    gamma_mean = gamma_stats.get("mean", 0)
    q025 = gamma_stats.get("q025", 0)
    q975 = gamma_stats.get("q975", 0)
    return {
        "gamma_mean": gamma_mean,
        "gamma_positive": gamma_mean > 0,
        "ci_excludes_zero": (q025 > 0) or (q975 < 0),
        "q025": q025,
        "q975": q975,
    }


def bootstrap_metric(metric_fn, calibrated, ground_truth, n_boot=N_BOOTSTRAP, seed=SEED):
    rng = np.random.default_rng(seed)
    cal = np.array(calibrated)
    gt = np.array(ground_truth)
    n = len(cal)
    boot_vals = []
    for _ in range(n_boot):
        idx = rng.choice(n, size=n, replace=True)
        boot_vals.append(metric_fn(cal[idx], gt[idx]))
    boot_vals = np.array(boot_vals)
    return {
        "mean": round(float(np.mean(boot_vals)), 6),
        "ci_lower": round(float(np.percentile(boot_vals, 2.5)), 6),
        "ci_upper": round(float(np.percentile(boot_vals, 97.5)), 6),
    }


def evaluate_method(method_name, scores, ground_truth,
                    ci_lower=None, ci_upper=None,
                    ci_lower_80=None, ci_upper_80=None,
                    ci_lower_50=None, ci_upper_50=None,
                    gamma_stats=None):
    cal = np.array(scores)
    gt = np.array(ground_truth)

    result = {"method": method_name}

    mae = metric_mae(cal, gt)
    mae_boot = bootstrap_metric(
        lambda c, g: float(np.mean(np.abs(c - g))), cal, gt
    )
    result["mae"] = {"value": round(mae, 6), "bootstrap_95ci": mae_boot}

    for level, lo_key, hi_key in [
        ("50%", ci_lower_50, ci_upper_50),
        ("80%", ci_lower_80, ci_upper_80),
        ("95%", ci_lower, ci_upper),
    ]:
        cov = metric_coverage(lo_key, hi_key, gt, level)
        result[f"coverage_{level}"] = round(cov, 4) if cov is not None else None

    sharpness = metric_sharpness(ci_lower, ci_upper)
    result["sharpness_95"] = round(sharpness, 6) if sharpness is not None else None
    sharpness_80 = metric_sharpness(ci_lower_80, ci_upper_80)
    result["sharpness_80"] = round(sharpness_80, 6) if sharpness_80 is not None else None
    sharpness_50 = metric_sharpness(ci_lower_50, ci_upper_50)
    result["sharpness_50"] = round(sharpness_50, 6) if sharpness_50 is not None else None

    kt = metric_kendall_tau(cal, gt)
    kt_boot = bootstrap_metric(
        lambda c, g: float(stats.kendalltau(c, g).statistic), cal, gt
    )
    result["kendall_tau"] = {**kt, "bootstrap_95ci": kt_boot}

    dr = metric_dose_response(gamma_stats)
    result["dose_response"] = dr

    return result


def format_latex_table(all_metrics):
    header = (
        "\\begin{table}[t]\n\\centering\n\\small\n"
        "\\caption{Calibration evaluation: IRT vs.\\ baselines}\n"
        "\\label{tab:calibration-eval}\n"
        "\\begin{tabular}{lccccccc}\n\\toprule\n"
        "Method & MAE $\\downarrow$ & Cov@50\\% & Cov@80\\% & Cov@95\\% & Sharp$_{95}$ $\\downarrow$ "
        "& $\\tau$ $\\uparrow$ & $\\gamma > 0$ \\\\\n\\midrule\n"
    )

    rows = []
    for m in all_metrics:
        name = m["method"].replace("_", "\\_")
        if "DCR" in name or "dcr" in name:
            name = name.replace("B6\\_dcr", "B6\\_DCR-inspired")

        mae_val = f"{m['mae']['value']:.4f}"

        cov50 = m.get("coverage_50%")
        cov50_str = f"{cov50:.0%}" if cov50 is not None else "---"

        cov80 = m.get("coverage_80%")
        cov80_str = f"{cov80:.0%}" if cov80 is not None else "---"

        cov95 = m.get("coverage_95%")
        cov95_str = f"{cov95:.0%}" if cov95 is not None else "---"

        sharp = m.get("sharpness_95")
        sharp_str = f"{sharp:.4f}" if sharp is not None else "---"

        tau = m["kendall_tau"]["tau"]
        tau_str = f"{tau:.3f}"

        dr = m.get("dose_response")
        if dr is not None:
            dr_str = f"{dr['gamma_mean']:.3f}" + ("*" if dr["ci_excludes_zero"] else "")
        else:
            dr_str = "---"

        rows.append(f"{name} & {mae_val} & {cov50_str} & {cov80_str} & {cov95_str} & {sharp_str} & {tau_str} & {dr_str} \\\\")

    footer = "\\bottomrule\n\\end{tabular}\n\\end{table}"
    return header + "\n".join(rows) + "\n" + footer


def main():
    parser = argparse.ArgumentParser(description="Evaluate calibration methods")
    parser.add_argument("--irt-results", nargs="+", required=True, help="IRT result JSON files")
    parser.add_argument("--baseline-results", required=True, help="Baselines JSON file")
    parser.add_argument("--ground-truth", required=True, help="Ground truth clean accuracy (JSON or CSV)")
    parser.add_argument("--benchmark", required=True, help="Benchmark name")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    ext = os.path.splitext(args.ground_truth)[1].lower()
    if ext == ".json":
        with open(args.ground_truth) as f:
            gt_data = json.load(f)
        if isinstance(gt_data, dict):
            ground_truth = gt_data.get("clean_accuracy", gt_data.get("scores", list(gt_data.values())))
        else:
            ground_truth = gt_data
    elif ext == ".csv":
        ground_truth = np.loadtxt(args.ground_truth, delimiter=",", skiprows=1).tolist()
        if isinstance(ground_truth[0], (list, np.ndarray)):
            ground_truth = [row[-1] for row in ground_truth]
    elif ext == ".npy":
        ground_truth = np.load(args.ground_truth).tolist()
    else:
        raise ValueError(f"Unsupported ground truth format: {ext}")

    log.info("Ground truth: %d models", len(ground_truth))

    all_metrics = []

    for irt_path in args.irt_results:
        irt = load_json(irt_path)
        model_type = irt.get("model_type", "unknown")
        cal = irt["parameters"]["calibrated_scores"]
        gamma_stats = irt["parameters"].get("gamma")

        m = evaluate_method(
            method_name=f"IRT_{model_type}",
            scores=cal["mean"],
            ground_truth=ground_truth,
            ci_lower=cal.get("q025"),
            ci_upper=cal.get("q975"),
            ci_lower_80=cal.get("q10"),
            ci_upper_80=cal.get("q90"),
            ci_lower_50=cal.get("q25"),
            ci_upper_50=cal.get("q75"),
            gamma_stats=gamma_stats,
        )
        all_metrics.append(m)
        log.info("IRT_%s: MAE=%.4f, τ=%.3f", model_type, m["mae"]["value"], m["kendall_tau"]["tau"])

    baselines = load_json(args.baseline_results)
    for bname, bdata in baselines.items():
        m = evaluate_method(
            method_name=bname,
            scores=bdata["scores"],
            ground_truth=ground_truth,
            ci_lower=bdata.get("ci_lower"),
            ci_upper=bdata.get("ci_upper"),
            gamma_stats=None,
        )
        all_metrics.append(m)
        log.info("%s: MAE=%.4f, τ=%.3f", bname, m["mae"]["value"], m["kendall_tau"]["tau"])

    out_path = os.path.join(args.output_dir, f"{args.benchmark}_evaluation.json")
    with open(out_path, "w") as f:
        json.dump(all_metrics, f, indent=2)
    log.info("Evaluation written to %s", out_path)

    latex = format_latex_table(all_metrics)
    tex_path = os.path.join(args.output_dir, f"{args.benchmark}_evaluation.tex")
    with open(tex_path, "w") as f:
        f.write(latex)
    log.info("LaTeX table written to %s", tex_path)


if __name__ == "__main__":
    main()
