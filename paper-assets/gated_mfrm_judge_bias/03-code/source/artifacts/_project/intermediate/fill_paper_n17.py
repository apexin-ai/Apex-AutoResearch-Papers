#!/usr/bin/env python3
"""
fill_paper_n17.py — Extract N=17 MCMC results and generate paper artifacts.

Input:  MCMC trace directory (output_n17/) containing results.json + downstream/
Output: paper_values_n17.json + 3 Appendix LaTeX tables

Usage:
  python fill_paper_n17.py --trace-dir /path/to/output_n17
  python fill_paper_n17.py --trace-dir /path/to/output_n17 --out-dir ./paper_artifacts
"""
import argparse
import json
import sys
from pathlib import Path
from typing import Any

# Precision rules: τ/ρ 3dp, θ/c/d 2dp, ELPD 1dp, ESS/counts int
def fmt_tau(v): return f"{v:.3f}"
def fmt_theta(v): return f"{v:.2f}"
def fmt_elpd(v): return f"{v:.1f}"
def fmt_int(v): return str(int(round(v)))
def fmt_ci(lo, hi, fn=fmt_theta): return f"[{fn(lo)}, {fn(hi)}]"
def sign_theta(v): return f"+{v:.2f}" if v >= 0 else f"{v:.2f}"


def load_json(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


def try_load_json(path: Path) -> dict | None:
    if path.exists():
        return load_json(path)
    return None


def extract_values(trace_dir: Path) -> dict:
    """Extract all paper-relevant values from MCMC output directory."""
    values: dict[str, Any] = {}

    # --- Core results ---
    results_path = trace_dir / "results.json"
    if not results_path.exists():
        sys.exit(f"ERROR: {results_path} not found")
    results = load_json(results_path)

    # Design
    values["design"] = {
        "n_models": results.get("n_models", 17),
        "n_items": results.get("n_items"),
        "n_judges": results.get("n_judges"),
        "n_observations": results.get("n_observations"),
    }

    # Table 1: ranking correlations
    table1 = {}
    for method_key in ["raw_average", "mfrm_only", "sequential", "joint_gmfrm"]:
        m = results.get(method_key, results.get("arena_correlation", {}).get(method_key, {}))
        if isinstance(m, dict):
            table1[method_key] = {
                "kendall_tau": fmt_tau(m.get("kendall_tau", 0)),
                "spearman_rho": fmt_tau(m.get("spearman_rho", 0)),
            }
    values["table1"] = table1

    # MCMC diagnostics
    conv = results.get("convergence", {}).get("joint_gmfrm", results.get("convergence", {}))
    values["mcmc_diagnostics"] = {
        "r_hat_max": conv.get("r_hat_max", conv.get("r_hat")),
        "ess_min": conv.get("ess_min", conv.get("ess")),
        "divergent_transitions": conv.get("divergent_transitions", 0),
        "chains": results.get("chains", 4),
        "warmup": results.get("warmup"),
        "samples": results.get("samples"),
    }

    # Per-model θ and c_n
    theta_data = results.get("theta", results.get("refit_posterior", {}).get("theta_95ci", {}))
    cn_data = results.get("c_n", results.get("refit_posterior", {}).get("c_n_95ci", {}))
    values["contamination"] = {}
    for model_name in sorted(cn_data.keys(), key=lambda k: cn_data[k].get("mean", 0), reverse=True):
        entry = cn_data[model_name]
        ci = entry.get("ci", [None, None])
        values["contamination"][model_name] = {
            "c_n_mean": fmt_theta(entry["mean"]),
            "c_n_ci": fmt_ci(ci[0], ci[1]) if ci[0] is not None else "N/A",
            "ess": fmt_int(entry.get("ess_bulk", 0)),
        }

    # Per-judge d_j
    dj_data = results.get("d_j", results.get("refit_posterior", {}).get("d_j_95ci", {}))
    values["judge_severity"] = {}
    for judge_name in sorted(dj_data.keys(), key=lambda k: dj_data[k].get("mean", 0), reverse=True):
        entry = dj_data[judge_name]
        ci = entry.get("ci", [None, None])
        values["judge_severity"][judge_name] = {
            "d_j_mean": fmt_theta(entry["mean"]),
            "d_j_ci": fmt_ci(ci[0], ci[1]) if ci[0] is not None else "N/A",
            "ess": fmt_int(entry.get("ess_bulk", 0)),
        }

    # --- Downstream results ---
    downstream = trace_dir / "downstream"

    # LOO-CV
    loo_paths = [
        downstream / "model_comparison" / "loo_comparison.json",
        downstream / "model_comparison" / "waic_loo_summary.json",
    ]
    for p in loo_paths:
        loo = try_load_json(p)
        if loo:
            values["loo_cv"] = {
                "delta_elpd": fmt_elpd(loo.get("delta_elpd", loo.get("elpd_diff", 0))),
                "se": fmt_elpd(loo.get("se", loo.get("dse", 0))),
                "ratio": fmt_tau(abs(loo.get("delta_elpd", 0)) / max(loo.get("se", 1), 0.01)),
                "stacking_weight_gmfrm": loo.get("stacking_weight_gmfrm", loo.get("weight", None)),
            }
            break
    if "loo_cv" not in values:
        values["loo_cv"] = {"delta_elpd": "N/A", "se": "N/A", "ratio": "N/A"}

    # Bootstrap Δτ
    bootstrap_paths = [
        downstream / "bootstrap_results" / "bootstrap_summary.json",
        downstream / "bootstrap_results" / "results.json",
    ]
    for p in bootstrap_paths:
        bs = try_load_json(p)
        if bs:
            values["ranking_significance"] = {
                "delta_tau_mean": fmt_tau(bs.get("delta_tau_mean", bs.get("mean", 0))),
                "delta_tau_median": fmt_tau(bs.get("delta_tau_median", bs.get("median", 0))),
                "ci_95": fmt_ci(
                    bs.get("ci_lower", bs.get("ci", [0, 0])[0]),
                    bs.get("ci_upper", bs.get("ci", [0, 0])[1]),
                    fmt_tau,
                ),
                "p_positive": fmt_tau(bs.get("p_positive", bs.get("p_delta_ge_0", 0))),
            }
            break
    if "ranking_significance" not in values:
        values["ranking_significance"] = {"delta_tau_mean": "N/A"}

    # Baselines
    baselines_paths = [
        downstream / "baselines" / "results.json",
        downstream / "baselines" / "baseline_results.json",
    ]
    for p in baselines_paths:
        bl = try_load_json(p)
        if bl:
            for method in ["raw_average", "mfrm_only", "sequential",
                           "cyclic_judge", "cyclic_judge_discard",
                           "dcr_factor", "pref_leakage", "preference_leakage"]:
                if method in bl and method not in table1:
                    table1[method] = {
                        "kendall_tau": fmt_tau(bl[method].get("kendall_tau", 0)),
                        "spearman_rho": fmt_tau(bl[method].get("spearman_rho", 0)),
                    }
            if "preference_leakage" in table1 and "pref_leakage" not in table1:
                table1["pref_leakage"] = table1.pop("preference_leakage")
            break

    # Bias absorption (delta theta)
    delta_paths = [
        downstream / "delta_theta" / "results.json",
        downstream / "delta_theta" / "delta_theta.json",
    ]
    for p in delta_paths:
        dt = try_load_json(p)
        if dt:
            values["bias_absorption"] = dt
            break

    # Facet fit
    fit_paths = [
        downstream / "facet_fit" / "results.json",
        downstream / "facet_fit" / "fit_statistics.json",
    ]
    for p in fit_paths:
        ff = try_load_json(p)
        if ff:
            values["fit_statistics"] = ff
            break

    # Headline numbers
    gmfrm = table1.get("joint_gmfrm", {})
    baseline = table1.get("raw_average", {})
    values["headline_numbers"] = {
        "gmfrm_tau": gmfrm.get("kendall_tau", "N/A"),
        "gmfrm_rho": gmfrm.get("spearman_rho", "N/A"),
        "baseline_tau": baseline.get("kendall_tau", "N/A"),
        "baseline_rho": baseline.get("spearman_rho", "N/A"),
        "n_models": values["design"]["n_models"],
        "n_judges": values["design"]["n_judges"],
    }

    return values


def generate_raw_scores_table(values: dict) -> str:
    """Generate LaTeX for per-model estimates (tab:raw_scores), N=17 version."""
    lines = [
        r"\begin{table}[h]",
        r"\centering",
        r"\scriptsize",
        r"\setlength{\tabcolsep}{3pt}",
        r"\begin{tabular}{lcccc}",
        r"\toprule",
        r"\textbf{Model} & $\hat{\theta}$ [95\% CI] & $\hat{c}_n$ [95\% CI] & \textbf{Base} & \textbf{G-MFRM} \\",
        r"\midrule",
    ]
    # TODO: actual ranking data requires theta values sorted
    # Placeholder structure — fill from results.json theta + c_n + rankings
    lines.append(r"% [Auto-generated from MCMC output — rows inserted by fill_paper_n17.py]")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\caption{G-MFRM posterior estimates for ability ($\hat{\theta}$) and contamination susceptibility ($\hat{c}_n$) for all 17 target models.}")
    lines.append(r"\label{tab:raw_scores_n17}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


def generate_bias_absorption_table(values: dict) -> str:
    """Generate LaTeX for bias absorption table, N=17 version."""
    lines = [
        r"\begin{table}[h]",
        r"\centering",
        r"\scriptsize",
        r"\setlength{\tabcolsep}{3pt}",
        r"\begin{tabular}{lcccc}",
        r"\toprule",
        r"\textbf{Model} & $\hat{\theta}_{\text{MFRM}}$ & $\hat{\theta}_{\text{G-MFRM}}$ & $\Delta\theta$ & $\hat{c}_n$ \\",
        r"\midrule",
    ]
    ba = values.get("bias_absorption", {})
    if isinstance(ba, dict):
        for model_name in sorted(ba.keys(),
                                  key=lambda k: ba[k].get("delta_theta", ba[k].get("c_n", 0))
                                  if isinstance(ba[k], dict) else 0,
                                  reverse=True):
            entry = ba[model_name]
            if isinstance(entry, dict):
                theta_mfrm = sign_theta(entry.get("theta_mfrm", 0))
                theta_gmfrm = sign_theta(entry.get("theta_gmfrm", 0))
                delta = sign_theta(entry.get("delta_theta", 0))
                cn = fmt_theta(entry.get("c_n", 0))
                display = model_name.replace("_", r"\_").replace("-", "-")
                lines.append(f"{display} & ${theta_mfrm}$ & ${theta_gmfrm}$ & ${delta}$ & ${cn}$ \\\\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\caption{Contamination bias absorption in MFRM-only estimation for 17 models.}")
    lines.append(r"\label{tab:bias_absorption_n17}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


def generate_judge_severity_table(values: dict) -> str:
    """Generate LaTeX for judge severity table."""
    lines = [
        r"\begin{table}[h]",
        r"\centering",
        r"\small",
        r"\begin{tabular}{lcc}",
        r"\toprule",
        r"\textbf{Judge} & $\hat{d}_j$ & 95\% CI \\",
        r"\midrule",
    ]
    js = values.get("judge_severity", {})
    for judge_name, entry in js.items():
        display = judge_name.replace("_", r"\_").replace("-", "-")
        lines.append(f"{display} & ${entry['d_j_mean']}$ & ${entry['d_j_ci']}$ \\\\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\caption{Judge severity estimates ($d_j$) for N=17 evaluation.}")
    lines.append(r"\label{tab:judge_severity_n17}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Extract N=17 results for paper")
    parser.add_argument("--trace-dir", required=True, help="Path to output_n17/")
    parser.add_argument("--out-dir", default=None, help="Output directory (default: trace-dir)")
    args = parser.parse_args()

    trace_dir = Path(args.trace_dir)
    out_dir = Path(args.out_dir) if args.out_dir else trace_dir / "paper_artifacts"
    out_dir.mkdir(parents=True, exist_ok=True)

    values = extract_values(trace_dir)

    # Write JSON
    json_path = out_dir / "paper_values_n17.json"
    with open(json_path, "w") as f:
        json.dump(values, f, indent=2, ensure_ascii=False)
    print(f"Written: {json_path}")

    # Generate LaTeX tables
    tables = {
        "table_raw_scores_n17.tex": generate_raw_scores_table(values),
        "table_bias_absorption_n17.tex": generate_bias_absorption_table(values),
        "table_judge_severity_n17.tex": generate_judge_severity_table(values),
    }
    for name, content in tables.items():
        path = out_dir / name
        with open(path, "w") as f:
            f.write(content)
        print(f"Written: {path}")

    # Print summary for quick verification
    print("\n--- Headline Numbers ---")
    hl = values.get("headline_numbers", {})
    print(f"G-MFRM τ={hl.get('gmfrm_tau')}  ρ={hl.get('gmfrm_rho')}")
    print(f"Baseline τ={hl.get('baseline_tau')}  ρ={hl.get('baseline_rho')}")
    print(f"Design: {hl.get('n_models')} models, {values['design'].get('n_judges')} judges")

    diag = values.get("mcmc_diagnostics", {})
    print(f"MCMC: R-hat={diag.get('r_hat_max')}, ESS={diag.get('ess_min')}, div={diag.get('divergent_transitions')}")

    loo = values.get("loo_cv", {})
    print(f"LOO: ΔELPD={loo.get('delta_elpd')}, SE={loo.get('se')}, |Δ/SE|={loo.get('ratio')}")


if __name__ == "__main__":
    main()
