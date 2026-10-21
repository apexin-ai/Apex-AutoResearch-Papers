"""
W5 Mixed-Effects Logistic Regression: formulation x model on repair verification accuracy.

Model 1: correct ~ formulation * model + (1|problem_id)        [repo-level only]
Model 2: correct ~ formulation * complexity + (1|problem_id)    [deepseek, repo+func]

Input:  per-sample prediction JSONL files from CLS / CWM evals
        (each line: {"problem_id": ..., "correct": 0|1, ...})
Output: fixed-effect coefficient table, random-effect variance, p-values

Dependencies: pandas, statsmodels (>=0.14)
"""

import json, sys, os
import pandas as pd
import numpy as np
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration: eval prediction file paths (on the server)
# Each entry: (formulation, model, seed, filepath, complexity)
# ---------------------------------------------------------------------------

EVAL_FILES = [
    # --- CLS (repo-level) ---
    ("CLS", "qwen3-8b", 42,
     "/root/autodl-tmp/eval_results/cls8b_s42_ckpt2200_test/predictions.jsonl",
     "repo"),
    ("CLS", "qwen3-8b", 456,
     "/root/autodl-tmp/eval_results/cls8b_repo_s456_ckpt2200/predictions.jsonl",
     "repo"),

    ("CLS", "deepseek-6.7b", 42,
     "/root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt2105_test_seq8192/predictions.jsonl",
     "repo"),
    ("CLS", "deepseek-6.7b", 123,
     "/root/autodl-tmp/eval_results/deepseek_cls_repo_s123_test/predictions.jsonl",
     "repo"),
    ("CLS", "deepseek-6.7b", 456,
     "/root/autodl-tmp/eval_results/deepseek_cls_repo_s456_ckpt2163/predictions.jsonl",
     "repo"),

    # --- CWM (repo-level) ---
    ("CWM", "qwen3-8b", 42,
     "/root/autodl-tmp/eval_results/qwen3_8b_cwm_repo_s42_ckpt400_seq4096/eval_repo_cwm_predictions.jsonl",
     "repo"),

    ("CWM", "deepseek-6.7b", 42,
     "/root/autodl-tmp/eval_results/deepseek_cwm_repo_s42_seq4096/eval_repo_cwm_predictions.jsonl",
     "repo"),
    ("CWM", "deepseek-6.7b", 123,
     "/root/autodl-tmp/eval_results/deepseek_cwm_repo_s123_test/eval_deepseek_cwm_repo_s123_predictions.jsonl",
     "repo"),

    # --- CLS (function-level) ---
    ("CLS", "deepseek-6.7b", 42,
     "/root/autodl-tmp/eval_results/deepseek_cls_func_test/predictions.jsonl",
     "function"),
    ("CLS", "deepseek-6.7b", 123,
     "/root/autodl-tmp/eval_results/deepseek_cls_func_s123_test/predictions_func.jsonl",
     "function"),

    # --- CWM (function-level) ---
    ("CWM", "deepseek-6.7b", 42,
     "/root/autodl-tmp/eval_results/deepseek_cwm_func_test/predictions.jsonl",
     "function"),
    ("CWM", "deepseek-6.7b", 123,
     "/root/autodl-tmp/eval_results/deepseek_cwm_func_s123_test/eval_repo_cwm_predictions.jsonl",
     "function"),
]


def load_predictions(path: str) -> list[dict]:
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def build_dataframe(eval_files: list[tuple]) -> pd.DataFrame:
    rows = []
    for formulation, model, seed, fpath, complexity in eval_files:
        if not fpath or not os.path.exists(fpath):
            print(f"SKIP (file not found): {formulation} / {model} / s{seed} / {complexity}: {fpath}")
            continue
        preds = load_predictions(fpath)
        print(f"LOAD: {formulation} / {model} / s{seed} / {complexity}: {len(preds)} samples from {fpath}")
        for rec in preds:
            pid = rec.get("problem_id") or rec.get("instance_id") or rec.get("task_id") or rec.get("id")
            correct = rec.get("correct")
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
    df = pd.DataFrame(rows)
    return df


def fit_glmm(df: pd.DataFrame):
    """Fit binomial GLMM: correct ~ formulation * model + (1|problem_id)."""
    from statsmodels.genmod.bayes_mixed_glm import BinomialBayesMixedGLM

    df = df.copy()
    df["formulation"] = pd.Categorical(df["formulation"])
    df["model"] = pd.Categorical(df["model"])

    formula_vars = pd.get_dummies(df[["formulation", "model"]], drop_first=True, dtype=float)
    form_cols = [c for c in formula_vars.columns if c.startswith("formulation_")]
    model_cols = [c for c in formula_vars.columns if c.startswith("model_")]
    for fc in form_cols:
        for mc in model_cols:
            formula_vars[f"{fc}:{mc}"] = formula_vars[fc] * formula_vars[mc]

    exog = formula_vars.copy()
    exog.insert(0, "Intercept", 1.0)
    endog = df["correct"].values

    ident = pd.get_dummies(df["problem_id"], dtype=float)

    print(f"\nFitting BinomialBayesMixedGLM...")
    print(f"  Fixed effects: {list(exog.columns)}")
    print(f"  Random groups (problem_id): {ident.shape[1]} unique problems")
    print(f"  Observations: {len(endog)}")

    mod = BinomialBayesMixedGLM(
        endog, exog, exog_vc=ident, ident=np.zeros(ident.shape[1], dtype=int)
    )
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        result = mod.fit_vb()
    return result, exog.columns.tolist()


def fit_lpm(df: pd.DataFrame):
    """Fallback: Linear probability model with MixedLM."""
    import statsmodels.formula.api as smf

    df = df.copy()
    df["formulation"] = df["formulation"].astype(str)
    df["model"] = df["model"].astype(str)

    formula = "correct ~ C(formulation) * C(model)"
    print(f"\nFitting MixedLM (linear probability model)...")
    print(f"  Formula: {formula} + (1|problem_id)")
    print(f"  Observations: {len(df)}")

    md = smf.mixedlm(formula, df, groups=df["problem_id"])
    result = md.fit(reml=True)
    return result


def fit_complexity_interaction(df: pd.DataFrame):
    """Fit: correct ~ formulation * complexity + (1|problem_id)."""
    import statsmodels.formula.api as smf

    df = df.copy()
    df["formulation"] = df["formulation"].astype(str)
    df["complexity"] = df["complexity"].astype(str)

    formula = "correct ~ C(formulation) * C(complexity)"
    print(f"\nFitting MixedLM (complexity interaction)...")
    print(f"  Formula: {formula} + (1|problem_id)")
    print(f"  Observations: {len(df)}")
    print(f"  Unique problem_ids: {df['problem_id'].nunique()}")
    print(f"  Cell counts:")
    print(df.groupby(["formulation", "complexity"]).size().to_string())

    md = smf.mixedlm(formula, df, groups=df["problem_id"])
    result = md.fit(reml=True)
    return result


def main():
    print("=" * 70)
    print("W5 Mixed-Effects Logistic Regression")
    print("=" * 70)

    df = build_dataframe(EVAL_FILES)
    if df.empty:
        print("ERROR: No data loaded. Check file paths.")
        sys.exit(1)

    print(f"\n--- Data Summary (all) ---")
    print(f"Total observations: {len(df)}")
    print(f"Unique problem_ids: {df['problem_id'].nunique()}")
    print(f"\nBy complexity:")
    for c in df["complexity"].unique():
        sub = df[df["complexity"] == c]
        print(f"  {c}: {len(sub)} obs, {sub['problem_id'].nunique()} problems")
    print(f"\nCell accuracy (formulation x model x complexity):")
    print(df.groupby(["formulation", "model", "complexity"])["correct"].mean().round(4).to_string())

    out_lines = []

    # ---- Model 1: formulation * model on repo-level only ----
    df_repo = df[df["complexity"] == "repo"].copy()
    print("\n" + "=" * 70)
    print("MODEL 1: correct ~ formulation * model + (1|problem_id)  [repo-level]")
    print("=" * 70)
    print(f"\nRepo-level observations: {len(df_repo)}")
    print(f"Unique problem_ids (repo): {df_repo['problem_id'].nunique()}")
    print(f"\nCell counts (formulation x model x seed):")
    print(df_repo.groupby(["formulation", "model", "seed"]).size().to_string())
    print(f"\nCell accuracy (formulation x model):")
    print(df_repo.groupby(["formulation", "model"])["correct"].mean().round(4).to_string())

    try:
        result_glmm, col_names = fit_glmm(df_repo)
        print("\n--- Bayesian GLMM Results (BinomialBayesMixedGLM) ---")
        print(result_glmm.summary())
        out_lines.append("=== MODEL 1: Bayesian GLMM (repo-level) ===\n")
        out_lines.append(str(result_glmm.summary()))

        print("\n--- Fixed Effects (logit scale) ---")
        fe = result_glmm.fe_mean
        fe_sd = result_glmm.fe_sd
        for i, name in enumerate(col_names):
            z = fe[i] / fe_sd[i] if fe_sd[i] > 0 else float("inf")
            print(f"  {name:40s}  coef={fe[i]:+.4f}  sd={fe_sd[i]:.4f}  z={z:.2f}")

        print(f"\n--- Random Effects (problem_id) ---")
        print(f"  Variance component SD: {np.exp(result_glmm.vcp_mean[0]):.4f}")
    except Exception as e:
        print(f"GLMM failed: {e}")

    result_lpm = fit_lpm(df_repo)
    print("\n--- Mixed LM Results (Linear Probability Model) ---")
    print(result_lpm.summary())
    out_lines.append("\n\n=== MODEL 1: Linear Probability Model (repo-level) ===\n")
    out_lines.append(str(result_lpm.summary()))

    # ---- Model 2: formulation * complexity on deepseek only (has both levels) ----
    df_ds = df[df["model"] == "deepseek-6.7b"].copy()
    if df_ds["complexity"].nunique() >= 2:
        print("\n" + "=" * 70)
        print("MODEL 2: correct ~ formulation * complexity + (1|problem_id)  [deepseek only]")
        print("=" * 70)

        result_cx = fit_complexity_interaction(df_ds)
        print("\n--- Complexity Interaction Results ---")
        print(result_cx.summary())
        out_lines.append("\n\n=== MODEL 2: Complexity Interaction (deepseek, repo+func) ===\n")
        out_lines.append(str(result_cx.summary()))
    else:
        print("\nSKIP Model 2: need both repo and function complexity levels")

    # --- Save results ---
    out_path = os.path.join(os.path.dirname(__file__) or ".", "artifacts", "w5_glmm_results.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        f.write("\n".join(out_lines))
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
