"""
Logistic regression supplement for Appendix M (Mixed-Effects Regression).

Fits GEE logistic regression + cluster-robust logistic regression to the
same data used for the LPM analysis. Reports odds ratios, 95% CIs, and
average marginal effects (AME) for direct comparison with LPM coefficients.

Models:
  1. Cross-complexity (DeepSeek only): correct ~ formulation × complexity + (1|problem_id)
  2. Repo-level cross-model: correct ~ formulation × model + (1|problem_id)

Output: JSON results + markdown report
"""

import json
import os
import sys

import numpy as np
import pandas as pd


EVAL_FILES = [
    # --- DeepSeek CLS repo ---
    ("CLS", "DeepSeek-6.7B", 42,
     "/root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt2105_test_seq8192/predictions.jsonl",
     "repo"),
    ("CLS", "DeepSeek-6.7B", 123,
     "/root/autodl-tmp/eval_results/deepseek_cls_repo_s123_test/predictions.jsonl",
     "repo"),
    ("CLS", "DeepSeek-6.7B", 456,
     "/root/autodl-tmp/eval_results/deepseek_cls_repo_s456_ckpt2163/predictions.jsonl",
     "repo"),
    # --- DeepSeek CWM repo ---
    ("CWM", "DeepSeek-6.7B", 42,
     "/root/autodl-tmp/eval_results/deepseek_cwm_repo_s42_seq4096/eval_repo_cwm_predictions.jsonl",
     "repo"),
    ("CWM", "DeepSeek-6.7B", 123,
     "/root/autodl-tmp/eval_results/deepseek_cwm_repo_s123_test/eval_deepseek_cwm_repo_s123_predictions.jsonl",
     "repo"),
    # --- DeepSeek CLS function ---
    ("CLS", "DeepSeek-6.7B", 42,
     "/root/autodl-tmp/eval_results/deepseek_cls_func_test/predictions.jsonl",
     "function"),
    ("CLS", "DeepSeek-6.7B", 123,
     "/root/autodl-tmp/eval_results/deepseek_cls_func_s123_test/predictions_func.jsonl",
     "function"),
    # --- DeepSeek CWM function ---
    ("CWM", "DeepSeek-6.7B", 42,
     "/root/autodl-tmp/eval_results/deepseek_cwm_func_test/predictions.jsonl",
     "function"),
    ("CWM", "DeepSeek-6.7B", 123,
     "/root/autodl-tmp/eval_results/deepseek_cwm_func_s123_test/eval_repo_cwm_predictions.jsonl",
     "function"),
    # --- Qwen CLS repo ---
    ("CLS", "Qwen3-8B", 42,
     "/root/autodl-tmp/eval_results/cls8b_s42_ckpt2200_test/predictions.jsonl",
     "repo"),
    ("CLS", "Qwen3-8B", 456,
     "/root/autodl-tmp/eval_results/cls8b_repo_s456_ckpt2200/predictions.jsonl",
     "repo"),
    # --- Qwen CWM repo ---
    ("CWM", "Qwen3-8B", 42,
     "/root/autodl-tmp/eval_results/qwen3_8b_cwm_repo_s42_ckpt400_seq4096/eval_repo_cwm_predictions.jsonl",
     "repo"),
]


def load_jsonl(path):
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def build_dataframe(eval_files):
    rows = []
    for formulation, model, seed, fpath, complexity in eval_files:
        if not os.path.exists(fpath):
            print(f"SKIP: {fpath}", file=sys.stderr)
            continue
        preds = load_jsonl(fpath)
        tag = f"{formulation}/{model}/s{seed}/{complexity}"
        print(f"LOAD {tag}: {len(preds)} samples", file=sys.stderr)
        for rec in preds:
            pid = (rec.get("problem_id") or rec.get("instance_id")
                   or rec.get("task_id") or rec.get("id"))
            correct = rec.get("correct")
            if correct is None:
                label = rec.get("label")
                pred = rec.get("pred")
                if label is not None and pred is not None:
                    correct = int(label == pred)
            if pid is None or correct is None:
                continue
            rows.append({
                "problem_id": pid,
                "formulation": formulation,
                "model": model,
                "seed": seed,
                "correct": int(correct),
                "complexity": complexity,
            })
    return pd.DataFrame(rows)


def fit_gee_logistic(df, formula_str, groups_col="problem_id", label=""):
    """GEE with binomial family and exchangeable correlation."""
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    from statsmodels.genmod.generalized_estimating_equations import GEE
    from statsmodels.genmod.families import Binomial
    from statsmodels.genmod.cov_struct import Exchangeable

    df = df.copy().sort_values(groups_col).reset_index(drop=True)
    for col in ["formulation", "model", "complexity"]:
        if col in df.columns:
            df[col] = df[col].astype(str)

    print(f"\n{'='*60}", file=sys.stderr)
    print(f"GEE Logistic: {label}", file=sys.stderr)
    print(f"  {formula_str}, groups={groups_col}", file=sys.stderr)
    print(f"  N={len(df)}, clusters={df[groups_col].nunique()}", file=sys.stderr)

    model = GEE.from_formula(
        formula_str, groups=groups_col, data=df,
        family=Binomial(), cov_struct=Exchangeable()
    )
    result = model.fit(maxiter=100)
    print(result.summary(), file=sys.stderr)
    return result, df


def compute_odds_ratios(result):
    """Extract odds ratios and 95% CIs from logistic model."""
    params = result.params
    ci = result.conf_int()
    pvals = result.pvalues

    ors = {}
    for name in params.index:
        coef = float(params[name])
        ci_lo, ci_hi = float(ci.loc[name, 0]), float(ci.loc[name, 1])
        ors[name] = {
            "log_odds": round(coef, 4),
            "OR": round(np.exp(coef), 4),
            "OR_ci_lower": round(np.exp(ci_lo), 4),
            "OR_ci_upper": round(np.exp(ci_hi), 4),
            "z": round(float(result.tvalues[name]), 3),
            "p": round(float(pvals[name]), 6),
        }
    return ors


def compute_ame(result, df, formula_str):
    """Average Marginal Effects for the formulation variable."""
    from patsy import dmatrix

    df = df.copy()
    for col in ["formulation", "model", "complexity"]:
        if col in df.columns:
            df[col] = df[col].astype(str)

    ame_results = {}

    # AME for formulation (CWM vs CLS)
    if "formulation" in formula_str:
        df0 = df.copy()
        df1 = df.copy()
        df0["formulation"] = "CLS"
        df1["formulation"] = "CWM"

        X0 = dmatrix(result.model.formula.split("~")[1].strip(), df0, return_type="dataframe")
        X1 = dmatrix(result.model.formula.split("~")[1].strip(), df1, return_type="dataframe")

        beta = result.params.values
        p0 = 1 / (1 + np.exp(-X0.values @ beta))
        p1 = 1 / (1 + np.exp(-X1.values @ beta))
        ame_cwm = float(np.mean(p1 - p0))
        ame_results["CWM_vs_CLS"] = round(ame_cwm, 4)

    # AME by complexity subgroup
    if "complexity" in formula_str and "formulation" in formula_str:
        for cx in ["function", "repo"]:
            sub = df[df["complexity"] == cx].copy()
            if len(sub) == 0:
                continue
            df0 = sub.copy()
            df1 = sub.copy()
            df0["formulation"] = "CLS"
            df1["formulation"] = "CWM"

            rhs = result.model.formula.split("~")[1].strip()
            X0 = dmatrix(rhs, df0, return_type="dataframe")
            X1 = dmatrix(rhs, df1, return_type="dataframe")

            beta = result.params.values
            p0 = 1 / (1 + np.exp(-X0.values @ beta))
            p1 = 1 / (1 + np.exp(-X1.values @ beta))
            ame_cx = float(np.mean(p1 - p0))
            ame_results[f"CWM_vs_CLS_{cx}"] = round(ame_cx, 4)

    return ame_results


def fit_cluster_robust_logistic(df, formula_str, groups_col="problem_id", label=""):
    """Standard logistic regression with cluster-robust (sandwich) SEs."""
    import statsmodels.formula.api as smf

    df = df.copy()
    for col in ["formulation", "model", "complexity"]:
        if col in df.columns:
            df[col] = df[col].astype(str)

    print(f"\n{'='*60}", file=sys.stderr)
    print(f"Cluster-Robust Logistic: {label}", file=sys.stderr)
    print(f"  {formula_str}, cluster={groups_col}", file=sys.stderr)

    model = smf.logit(formula_str, data=df)
    result = model.fit(cov_type="cluster", cov_kwds={"groups": df[groups_col]},
                       disp=False, maxiter=100)
    print(result.summary(), file=sys.stderr)
    return result, df


def main():
    print("="*70, file=sys.stderr)
    print("Logistic Regression Analysis for Appendix M", file=sys.stderr)
    print("="*70, file=sys.stderr)

    df_all = build_dataframe(EVAL_FILES)
    if df_all.empty:
        print("ERROR: no data loaded", file=sys.stderr)
        sys.exit(1)

    print(f"\nTotal: {len(df_all)} obs, {df_all['problem_id'].nunique()} problems",
          file=sys.stderr)
    print(f"Cell accuracy:", file=sys.stderr)
    print(df_all.groupby(["formulation", "model", "complexity"])["correct"]
          .agg(["mean", "count"]).round(4).to_string(), file=sys.stderr)

    results = {}

    # ================================================================
    # Model 1: Cross-complexity (DeepSeek only)
    # ================================================================
    df_ds = df_all[df_all["model"] == "DeepSeek-6.7B"].copy()
    print(f"\n--- DeepSeek cross-complexity: {len(df_ds)} obs ---", file=sys.stderr)

    formula1 = "correct ~ C(formulation, Treatment('CLS')) * C(complexity, Treatment('function'))"

    # GEE logistic
    gee1, gee1_df = fit_gee_logistic(df_ds, formula1, label="Cross-complexity (DeepSeek)")
    or1 = compute_odds_ratios(gee1)
    ame1 = compute_ame(gee1, gee1_df, formula1)

    # Cluster-robust logistic (for comparison)
    cr1, cr1_df = fit_cluster_robust_logistic(df_ds, formula1, label="Cross-complexity (DeepSeek)")
    or1_cr = compute_odds_ratios(cr1)
    ame1_cr = compute_ame(cr1, cr1_df, formula1)

    results["cross_complexity_gee"] = {
        "method": "GEE (exchangeable)",
        "n_obs": len(df_ds),
        "n_clusters": int(df_ds["problem_id"].nunique()),
        "odds_ratios": or1,
        "ame": ame1,
    }
    results["cross_complexity_cluster_robust"] = {
        "method": "Cluster-robust logistic",
        "n_obs": len(df_ds),
        "n_clusters": int(df_ds["problem_id"].nunique()),
        "odds_ratios": or1_cr,
        "ame": ame1_cr,
    }

    # ================================================================
    # Model 2: Cross-model (repo-level only)
    # ================================================================
    df_repo = df_all[df_all["complexity"] == "repo"].copy()
    print(f"\n--- Repo cross-model: {len(df_repo)} obs ---", file=sys.stderr)

    formula2 = "correct ~ C(formulation, Treatment('CLS')) * C(model, Treatment('DeepSeek-6.7B'))"

    gee2, gee2_df = fit_gee_logistic(df_repo, formula2, label="Cross-model (repo)")
    or2 = compute_odds_ratios(gee2)
    ame2 = compute_ame(gee2, gee2_df, formula2)

    cr2, cr2_df = fit_cluster_robust_logistic(df_repo, formula2, label="Cross-model (repo)")
    or2_cr = compute_odds_ratios(cr2)
    ame2_cr = compute_ame(cr2, cr2_df, formula2)

    results["cross_model_gee"] = {
        "method": "GEE (exchangeable)",
        "n_obs": len(df_repo),
        "n_clusters": int(df_repo["problem_id"].nunique()),
        "odds_ratios": or2,
        "ame": ame2,
    }
    results["cross_model_cluster_robust"] = {
        "method": "Cluster-robust logistic",
        "n_obs": len(df_repo),
        "n_clusters": int(df_repo["problem_id"].nunique()),
        "odds_ratios": or2_cr,
        "ame": ame2_cr,
    }

    # Save JSON
    out_dir = os.path.join(os.path.dirname(__file__) or ".", "artifacts")
    os.makedirs(out_dir, exist_ok=True)
    json_path = os.path.join(out_dir, "logistic_regression_results.json")
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nSaved: {json_path}", file=sys.stderr)

    # Print JSON to stdout
    print(json.dumps(results, indent=2, default=str))


if __name__ == "__main__":
    main()
