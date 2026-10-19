#!/usr/bin/env python3
"""
Semi-real case study: end-to-end causal inference pipeline with VAST K=3
real LLM confusion matrices.

Uses 10 confusion matrices estimated from production LLM annotation on
VAST stance detection (4 models × 2-3 prompting strategies). Each matrix
is column-stochastic C[j,k] = P(A*=j | A=k) with K=3 classes
(pro, con, neutral). Unlike e2e_demo.py which uses a symmetric C0
(d_rel ≈ 0.005), these real matrices are highly asymmetric
(median d_rel ≈ 0.33, using ||C - C_sym||_F / ||C||_F).

Two causal topologies demonstrate the key dichotomy:
  - Exposure: annotation A is a direct cause of Y.  PPI++ correction
    significantly reduces bias.
  - Confounding: annotation A is a confounder between T and Y.  FWL
    invariance makes plug-in correction ineffective (≈ 0% improvement).

Pipeline per (matrix, topology):
  1. Generate synthetic data (N=10000, K=3) with known causal structure.
  2. Apply real VAST C0 to produce noisy labels A*.
  3. Sample 20% gold subset; estimate C_hat.
  4. Compute naive and PPI++-corrected estimates.
  5. Record bias and improvement over 100 MC replicates.

Inputs:
  - artifacts/plan011_frontier_cms.json + plan011_new_cms*.json
    (later files override earlier; source of 10 VAST C0 matrices)

Outputs:
  - artifacts/e2e_real_cm_results.json
  - artifacts/e2e_real_cm_table.tex
"""

import json
import os
import sys
import time

import numpy as np

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from annot_sensitivity.correction import correct_naive_plugin, correct_ppi
from annot_sensitivity.dgp import gen_confounding, gen_exposure
from annot_sensitivity.utils import make_dummies, misclassify, ols_with_se

SEED = 42
N = 10_000
K = 3
GOLD_FRACTION = 0.20
N_REPS = 100

CONFOUNDING_PARAMS = {
    "p_A": np.array([0.40, 0.35, 0.25]),
    "alpha": np.array([0.6, -0.3]),
    "beta_A": np.array([0.8, -0.4]),
    "beta_T": 0.5,
    "sigma_T": 1.0,
}

EXPOSURE_PARAMS = {
    "p_A": np.array([0.40, 0.35, 0.25]),
    "beta": np.array([0.0, 1.0, -0.5]),
}

CMS_FILES = [
    os.path.join(PROJECT_ROOT, "artifacts", f)
    for f in [
        "plan011_frontier_cms.json",
        "plan011_new_cms.json",
        "plan011_new_cms_round2.json",
        "plan011_new_cms_vast_qwen3_zs.json",
    ]
]


def load_vast_matrices():
    """Load all VAST K=3 confusion matrices, later files override earlier."""
    raw = {}
    for src in CMS_FILES:
        if not os.path.exists(src):
            continue
        with open(src) as f:
            raw.update(json.load(f))
    matrices = {}
    for key in sorted(raw.keys()):
        if not key.startswith("vast/"):
            continue
        entry = raw[key]
        cm = np.array(entry["confusion_matrix_normalized"])
        if cm.shape != (K, K):
            continue
        label = key.replace("vast/", "vast_")
        matrices[label] = cm
    return matrices


def estimate_C(A_true_gold, A_star_gold, K):
    """Column-stochastic C_hat[j,k] = P(A*=j | A=k) from gold labels."""
    C_hat = np.zeros((K, K))
    for k in range(K):
        mask = A_true_gold == k
        if mask.sum() > 0:
            for j in range(K):
                C_hat[j, k] = (A_star_gold[mask] == j).sum() / mask.sum()
        else:
            C_hat[k, k] = 1.0
    return C_hat


def symmetry_deviation(C):
    """Relative Frobenius deviation from symmetry: ||C - C_sym||_F / ||C||_F."""
    C_sym = (C + C.T) / 2
    return float(np.linalg.norm(C - C_sym, "fro") / np.linalg.norm(C, "fro"))


def run_exposure_rep(rng, C0, tau_true):
    data = gen_exposure(N, params=EXPOSURE_PARAMS, rng=rng)
    Y, A = data["Y"], data["A"]
    Astar = misclassify(A, C0, rng)

    gold_idx = rng.choice(N, size=int(N * GOLD_FRACTION), replace=False)
    gold_mask = np.zeros(N, dtype=bool)
    gold_mask[gold_idx] = True
    C_hat = estimate_C(A[gold_mask], Astar[gold_mask], K)

    X_other = np.ones((N, 1))
    D_star = make_dummies(Astar, K)
    X = np.column_stack([X_other, D_star])
    beta_naive, _ = ols_with_se(X, Y)
    tau_naive = float(beta_naive[1])

    tau_ppi, _, ok_ppi = correct_ppi(
        X_other, Y, Astar, A, gold_mask, tau_idx=1, rng=rng
    )

    return {
        "tau_naive": tau_naive,
        "tau_ppi": tau_ppi if ok_ppi else np.nan,
        "tau_true": tau_true,
    }


def run_confounding_rep(rng, C0, tau_true):
    data = gen_confounding(N, params=CONFOUNDING_PARAMS, rng=rng)
    T, Y, A = data["T"], data["Y"], data["A"]
    Astar = misclassify(A, C0, rng)

    gold_idx = rng.choice(N, size=int(N * GOLD_FRACTION), replace=False)
    gold_mask = np.zeros(N, dtype=bool)
    gold_mask[gold_idx] = True
    C_hat = estimate_C(A[gold_mask], Astar[gold_mask], K)

    X_other = np.column_stack([np.ones(N), T])
    D_star = make_dummies(Astar, K)
    X = np.column_stack([X_other, D_star])
    beta_naive, _ = ols_with_se(X, Y)
    tau_naive = float(beta_naive[1])

    tau_np, _, ok_np = correct_naive_plugin(X_other, Y, Astar, C_hat, tau_idx=1)

    return {
        "tau_naive": tau_naive,
        "tau_np": tau_np if ok_np else np.nan,
        "tau_true": tau_true,
    }


def summarize_reps(reps, corrected_key, tau_true):
    naive_vals = np.array([r["tau_naive"] for r in reps])
    corrected_vals = np.array([r[corrected_key] for r in reps])
    valid = np.isfinite(corrected_vals)

    naive_bias = naive_vals - tau_true
    naive_abs_bias = float(np.mean(np.abs(naive_bias)))
    naive_bias_pct = float(100.0 * np.mean(naive_bias) / tau_true)

    if valid.sum() == 0:
        return {
            "tau_true": float(tau_true),
            "naive_bias_pct": naive_bias_pct,
            "naive_abs_bias": naive_abs_bias,
            "corrected_bias_pct": float("nan"),
            "corrected_abs_bias": float("nan"),
            "improvement_pct": float("nan"),
            "n_valid": 0,
        }

    corr = corrected_vals[valid]
    corr_bias = corr - tau_true
    corr_abs_bias = float(np.mean(np.abs(corr_bias)))
    corr_bias_pct = float(100.0 * np.mean(corr_bias) / tau_true)
    improvement = float(100.0 * (1.0 - corr_abs_bias / naive_abs_bias)) if naive_abs_bias > 1e-12 else float("nan")

    return {
        "tau_true": float(tau_true),
        "naive_bias_pct": naive_bias_pct,
        "naive_abs_bias": naive_abs_bias,
        "corrected_bias_pct": corr_bias_pct,
        "corrected_abs_bias": corr_abs_bias,
        "improvement_pct": improvement,
        "n_valid": int(valid.sum()),
    }


def main():
    t0 = time.time()

    vast_matrices = load_vast_matrices()
    n_configs = len(vast_matrices)
    print(f"Loaded {n_configs} VAST K=3 confusion matrices")
    for name, cm in vast_matrices.items():
        print(f"  {name}: diag={np.diag(cm).round(3).tolist()}, d_rel={symmetry_deviation(cm):.3f}")

    print(f"\nSettings: N={N}, K={K}, gold={int(N*GOLD_FRACTION)}, reps={N_REPS}")
    print("=" * 70)

    rng_master = np.random.default_rng(SEED)

    tau_true_exp = EXPOSURE_PARAMS["beta"][1]
    tau_true_conf = CONFOUNDING_PARAMS["beta_T"]

    results = {"exposure": {}, "confounding": {}}

    for ci, (cm_name, C0) in enumerate(vast_matrices.items()):
        print(f"\n[{ci+1}/{n_configs}] {cm_name}")

        # --- Exposure ---
        exp_reps = []
        for rep in range(N_REPS):
            seed_rep = int(rng_master.integers(0, 2**31))
            rng_rep = np.random.default_rng(seed_rep)
            exp_reps.append(run_exposure_rep(rng_rep, C0, tau_true_exp))
        exp_summary = summarize_reps(exp_reps, "tau_ppi", tau_true_exp)
        results["exposure"][cm_name] = exp_summary
        print(f"  exposure:    naive bias {exp_summary['naive_bias_pct']:+.1f}%  "
              f"PPI++ bias {exp_summary['corrected_bias_pct']:+.1f}%  "
              f"improvement {exp_summary['improvement_pct']:+.1f}%")

        # --- Confounding ---
        conf_reps = []
        for rep in range(N_REPS):
            seed_rep = int(rng_master.integers(0, 2**31))
            rng_rep = np.random.default_rng(seed_rep)
            conf_reps.append(run_confounding_rep(rng_rep, C0, tau_true_conf))
        conf_summary = summarize_reps(conf_reps, "tau_np", tau_true_conf)
        results["confounding"][cm_name] = conf_summary
        print(f"  confounding: naive bias {conf_summary['naive_bias_pct']:+.1f}%  "
              f"plugin bias {conf_summary['corrected_bias_pct']:+.1f}%  "
              f"improvement {conf_summary['improvement_pct']:+.1f}%")

    # --- Aggregate ---
    exp_improvements = [v["improvement_pct"] for v in results["exposure"].values() if np.isfinite(v["improvement_pct"])]
    conf_improvements = [v["improvement_pct"] for v in results["confounding"].values() if np.isfinite(v["improvement_pct"])]

    aggregate = {
        "exposure": {
            "median_improvement_pct": float(np.median(exp_improvements)),
            "min_improvement_pct": float(np.min(exp_improvements)),
            "max_improvement_pct": float(np.max(exp_improvements)),
            "mean_improvement_pct": float(np.mean(exp_improvements)),
            "n_configs": len(exp_improvements),
        },
        "confounding": {
            "median_improvement_pct": float(np.median(conf_improvements)),
            "min_improvement_pct": float(np.min(conf_improvements)),
            "max_improvement_pct": float(np.max(conf_improvements)),
            "mean_improvement_pct": float(np.mean(conf_improvements)),
            "n_configs": len(conf_improvements),
        },
    }

    print("\n" + "=" * 70)
    print("AGGREGATE RESULTS")
    print(f"  Exposure PPI++ improvement: median {aggregate['exposure']['median_improvement_pct']:+.1f}%  "
          f"[{aggregate['exposure']['min_improvement_pct']:+.1f}%, {aggregate['exposure']['max_improvement_pct']:+.1f}%]")
    print(f"  Confounding plug-in improvement: median {aggregate['confounding']['median_improvement_pct']:+.1f}%  "
          f"[{aggregate['confounding']['min_improvement_pct']:+.1f}%, {aggregate['confounding']['max_improvement_pct']:+.1f}%]")

    # --- Build output ---
    vast_meta = {}
    for name, cm in vast_matrices.items():
        vast_meta[name] = {
            "C0": cm.tolist(),
            "diagonal": np.diag(cm).tolist(),
            "d_rel": symmetry_deviation(cm),
            "accuracy": float(np.trace(cm) / K),
        }

    output = {
        "meta": {
            "description": (
                "Semi-real case study: confusion matrices estimated from "
                "production LLM annotation on VAST stance detection (K=3); "
                "DGP is controlled synthetic to isolate causal mechanism."
            ),
            "seed": SEED,
            "N": N,
            "K": K,
            "gold_fraction": GOLD_FRACTION,
            "n_reps": N_REPS,
            "n_vast_configs": n_configs,
            "source_files": [os.path.basename(f) for f in CMS_FILES],
            "exposure_params": {
                k: (v.tolist() if isinstance(v, np.ndarray) else v)
                for k, v in EXPOSURE_PARAMS.items()
            },
            "confounding_params": {
                k: (v.tolist() if isinstance(v, np.ndarray) else v)
                for k, v in CONFOUNDING_PARAMS.items()
            },
        },
        "vast_matrices": vast_meta,
        "results": results,
        "aggregate": aggregate,
    }

    out_json = os.path.join(PROJECT_ROOT, "artifacts", "e2e_real_cm_results.json")
    with open(out_json, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nWrote {out_json}")

    write_latex_table(output)
    print(f"\nElapsed: {time.time() - t0:.1f}s")


def write_latex_table(output):
    results = output["results"]
    vast_meta = output["vast_matrices"]
    aggregate = output["aggregate"]

    config_names = list(vast_meta.keys())

    def short_name(name):
        return name.replace("vast_", "").replace("qwen2.5-7b", "Qwen2.5-7B").replace(
            "qwen3", "Qwen3").replace("deepseek", "DeepSeek").replace(
            "llama4", "Llama4").replace("_", " ").replace("few-shot-", "FS-").replace(
            "zero-shot", "ZS")

    lines = []
    lines.append("% Auto-generated by artifacts/e2e_real_cm_demo.py")
    lines.append("\\begin{table}[t]")
    lines.append("\\centering")
    lines.append("\\small")
    lines.append("\\begin{tabular}{l c r r r r r}")
    lines.append("\\toprule")
    lines.append(
        " & & \\multicolumn{2}{c}{Exposure} & & \\multicolumn{2}{c}{Confounding} \\\\"
    )
    lines.append("\\cmidrule(lr){3-4} \\cmidrule(lr){6-7}")
    lines.append(
        "LLM Config & $d_{\\mathrm{rel}}$ & Naive (\\%) & PPI++ (\\%) & "
        "& Naive (\\%) & Plugin (\\%) \\\\"
    )
    lines.append("\\midrule")

    for name in config_names:
        d_rel = vast_meta[name]["d_rel"]
        exp = results["exposure"][name]
        conf = results["confounding"][name]
        lines.append(
            f"{short_name(name)} & {d_rel:.2f} & "
            f"{exp['naive_bias_pct']:+.1f} & {exp['corrected_bias_pct']:+.1f} & "
            f"& {conf['naive_bias_pct']:+.1f} & {conf['corrected_bias_pct']:+.1f} \\\\"
        )

    lines.append("\\midrule")
    exp_agg = aggregate["exposure"]
    conf_agg = aggregate["confounding"]
    lines.append(
        f"\\textit{{Median improvement}} & & "
        f"\\multicolumn{{2}}{{c}}{{{exp_agg['median_improvement_pct']:+.1f}\\%}} & "
        f"& \\multicolumn{{2}}{{c}}{{{conf_agg['median_improvement_pct']:+.1f}\\%}} \\\\"
    )

    lines.append("\\bottomrule")
    lines.append("\\end{tabular}")
    lines.append(
        "\\caption{Semi-real case study with VAST K=3 confusion matrices from "
        f"{output['meta']['n_vast_configs']} LLM configurations. "
        "Bias is relative to true $\\tau$. "
        "Exposure: PPI++ substantially reduces bias. "
        "Confounding: plug-in correction is ineffective (FWL invariance).}"
    )
    lines.append("\\label{tab:e2e-real-cm}")
    lines.append("\\end{table}")

    out_tex = os.path.join(PROJECT_ROOT, "artifacts", "e2e_real_cm_table.tex")
    with open(out_tex, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote {out_tex}")


if __name__ == "__main__":
    main()
