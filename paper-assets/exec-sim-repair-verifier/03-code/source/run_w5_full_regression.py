"""
W5 Full Mixed-Effects Regression: formulation × complexity / model interaction.

Extends w5_mixed_effects_v2.py to support multi-seed CWM data and per-model analysis.
Reproduces paper numbers (z=-23.7, z=-64.4, etc.) and updates them with new CWM seeds.

Input:
  --eval_dirs   Comma-separated eval result directories (infers metadata from dir names).
                Each dir must contain a prediction JSONL (eval_*_predictions.jsonl or
                predictions.jsonl). Metadata (formulation, model, seed, complexity)
                parsed from directory basename.
  --verify      After fitting, compare key coefficients against paper-reported values.

Output (to --output_dir, default artifacts/w5_full_regression/):
  results.json        All model fits (coefficients, random effects, Wald tests)
  paper_numbers.txt   Paper-ready summary with verification status

Models fitted:
  1. Cross-complexity per model:  correct ~ C(formulation) * C(complexity) + (1|problem_id)
     - One fit per model family that has both func + repo data
  2. Cross-complexity combined:   correct ~ C(formulation) * C(complexity) + (1|problem_id)
     - All models pooled
  3. Cross-model (repo-level):    correct ~ C(formulation) * C(model) + (1|problem_id)
     - Repo-level data from all models

Dependencies: pandas, numpy, statsmodels (>=0.14), scipy
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd


PAPER_EXPECTED = {
    "deepseek_cross_complexity": {
        "interaction_z": -23.7,
        "interaction_p": 0.001,
        "cwm_main_coef": -0.002,
        "cwm_main_p": 0.805,
        "n_obs": 56480,
        "n_clusters": 139,
    },
    "repo_cross_model": {
        "cwm_deficit_z": -64.4,
        "cwm_deficit_p": 0.001,
        "qwen_effect_coef": 0.011,
        "qwen_effect_p": 0.002,
        "interaction_coef": 0.016,
        "interaction_p": 0.006,
    },
}


def parse_args():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--eval_dirs", required=True,
                   help="Comma-separated eval result directories")
    p.add_argument("--output_dir", default="artifacts/w5_full_regression",
                   help="Output directory")
    p.add_argument("--verify", action="store_true",
                   help="Compare results against paper-reported values")
    return p.parse_args()


def infer_metadata(dirpath: str) -> dict:
    """Parse formulation, model, seed, complexity from directory basename."""
    name = os.path.basename(dirpath).lower()

    if "cwm" in name:
        formulation = "CWM"
    elif "traj" in name:
        formulation = "TRAJ"
    elif "cls" in name:
        formulation = "CLS"
    else:
        formulation = "UNKNOWN"

    if "qwen" in name:
        model = "Qwen3-8B"
    elif "deepseek" in name:
        model = "DeepSeek-6.7B"
    else:
        model = "UNKNOWN"

    m = re.search(r"s(\d+)", name)
    seed = int(m.group(1)) if m else 42

    complexity = "function" if "func" in name else "repo"

    return dict(formulation=formulation, model=model, seed=seed,
                complexity=complexity)


def find_prediction_file(dirpath: str) -> str | None:
    """Locate prediction JSONL inside an eval directory."""
    p = Path(dirpath)
    for pattern in ["eval_*_predictions.jsonl", "predictions_*.jsonl",
                    "predictions.jsonl", "results_incremental.jsonl"]:
        hits = sorted(p.glob(pattern))
        if hits:
            return str(hits[0])
    return None


def load_jsonl(path: str) -> list[dict]:
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def build_dataframe(eval_dirs: list[str]) -> pd.DataFrame:
    rows = []
    for dirpath in eval_dirs:
        dirpath = dirpath.strip()
        if not dirpath:
            continue
        info = infer_metadata(dirpath)
        pred_file = find_prediction_file(dirpath)
        if pred_file is None:
            print(f"SKIP (no prediction file): {dirpath}", file=sys.stderr)
            continue

        preds = load_jsonl(pred_file)
        tag = f"{info['formulation']}/{info['model']}/s{info['seed']}/{info['complexity']}"
        print(f"LOAD {tag}: {len(preds)} samples <- {pred_file}", file=sys.stderr)

        for rec in preds:
            pid = (rec.get("problem_id") or rec.get("instance_id")
                   or rec.get("task_id") or rec.get("id"))
            correct = rec.get("correct")
            if pid is None or correct is None:
                continue
            rows.append(dict(
                problem_id=pid,
                formulation=info["formulation"],
                model=info["model"],
                seed=info["seed"],
                correct=int(correct),
                complexity=info["complexity"],
            ))

    return pd.DataFrame(rows)


def fit_mixed_lm(df: pd.DataFrame, formula: str,
                 groups_col: str = "problem_id",
                 label: str = "") -> dict:
    """Fit MixedLM (LPM). Returns dict with coefficients on probability scale (pp)."""
    import statsmodels.formula.api as smf
    from scipy import stats as sp_stats

    df = df.copy()
    for col in ["formulation", "model", "complexity"]:
        if col in df.columns:
            df[col] = df[col].astype(str)

    print(f"\n{'=' * 60}", file=sys.stderr)
    print(f"{label}", file=sys.stderr)
    print(f"  {formula} + (1|{groups_col})", file=sys.stderr)
    print(f"  N={len(df)}, groups={df[groups_col].nunique()}", file=sys.stderr)

    md = smf.mixedlm(formula, df, groups=df[groups_col])
    try:
        result = md.fit(reml=True)
    except np.linalg.LinAlgError:
        fallback = re.sub(r"\s*\*\s*", " + ", formula)
        print(f"  WARN: singular matrix, fallback -> {fallback}", file=sys.stderr)
        md = smf.mixedlm(fallback, df, groups=df[groups_col])
        result = md.fit(reml=True)
        formula = fallback

    print(result.summary(), file=sys.stderr)

    fe = result.fe_params
    se = result.bse_fe
    pvals = result.pvalues

    coefficients = {}
    for name in fe.index:
        z_val = float(fe[name] / se[name]) if se[name] > 0 else 0.0
        coefficients[name] = dict(
            coef=round(float(fe[name]), 4),
            se=round(float(se[name]), 4),
            z=round(z_val, 3),
            p=round(float(pvals[name]), 4) if name in pvals.index else None,
        )

    re_var = (float(result.cov_re.iloc[0, 0])
              if hasattr(result.cov_re, "iloc")
              else float(result.cov_re))

    # Joint Wald chi-squared per term
    param_names = list(result.fe_params.index)
    anova = {}
    terms: dict[str, list[int]] = {}
    for i, name in enumerate(param_names):
        if name == "Intercept":
            continue
        if ":" in name:
            term = "interaction"
        elif "formulation" in name:
            term = "formulation"
        elif "model" in name:
            term = "model"
        elif "complexity" in name:
            term = "complexity"
        else:
            term = name
        terms.setdefault(term, []).append(i)

    for term, indices in terms.items():
        beta = result.fe_params.values[indices]
        cov = result.cov_params().iloc[indices, :]
        cov = cov.iloc[:, indices].values
        try:
            chi2 = float(beta @ np.linalg.solve(cov, beta))
            df_term = len(indices)
            p = float(1 - sp_stats.chi2.cdf(chi2, df_term))
            anova[term] = dict(wald_chi2=round(chi2, 3), df=df_term,
                               p=round(p, 6))
        except np.linalg.LinAlgError:
            anova[term] = dict(wald_chi2=None, df=len(indices), p=None)

    return dict(
        formula=formula,
        n_obs=len(df),
        n_groups=int(df[groups_col].nunique()),
        coefficients=coefficients,
        random_effects=dict(variance=round(re_var, 6),
                            sd=round(float(np.sqrt(max(re_var, 0))), 4)),
        anova=anova,
        log_likelihood=round(float(result.llf), 2),
    )


def format_paper_numbers(results: dict, verify: bool) -> str:
    """Format results as paper-ready text with optional verification."""
    lines = []
    lines.append("=" * 70)
    lines.append("W5 Full Regression: Paper-Ready Numbers")
    lines.append("=" * 70)

    for analysis_key, res in results.items():
        lines.append(f"\n--- {analysis_key} ---")
        lines.append(f"  Formula: {res['formula']}")
        lines.append(f"  N = {res['n_obs']}, clusters = {res['n_groups']}")
        lines.append("")

        for name, v in res["coefficients"].items():
            p_str = f"p={v['p']:.4f}" if v["p"] is not None else "p=N/A"
            if v["p"] is not None and v["p"] < 0.001:
                p_str = "p<0.001"
            lines.append(f"  {name:50s}  coef={v['coef']:+.4f}  "
                         f"z={v['z']:+.2f}  {p_str}")

        if res.get("anova"):
            lines.append("\n  Joint Wald tests:")
            for term, w in res["anova"].items():
                if w["wald_chi2"] is not None:
                    p_str = f"p={w['p']:.6f}" if w["p"] >= 0.001 else "p<0.001"
                    lines.append(f"    {term:20s}  chi2={w['wald_chi2']:.3f}  "
                                 f"df={w['df']}  {p_str}")

    if verify:
        lines.append("\n" + "=" * 70)
        lines.append("VERIFICATION against paper-reported values")
        lines.append("=" * 70)

        # Check DeepSeek cross-complexity
        ds_key = None
        for k in results:
            if "deepseek" in k.lower() and "complexity" in k.lower():
                ds_key = k
                break

        if ds_key:
            res = results[ds_key]
            exp = PAPER_EXPECTED["deepseek_cross_complexity"]

            # Find interaction term
            interaction_z = None
            cwm_main_coef = None
            for name, v in res["coefficients"].items():
                if ":" in name and "formulation" in name.lower():
                    interaction_z = v["z"]
                if ("CWM" in name and ":" not in name
                        and "complexity" not in name.lower()):
                    cwm_main_coef = v["coef"]

            lines.append(f"\n  DeepSeek cross-complexity:")
            lines.append(f"    N:             got {res['n_obs']}, "
                         f"expected {exp['n_obs']}  "
                         f"{'OK' if res['n_obs'] == exp['n_obs'] else 'MISMATCH'}")
            lines.append(f"    Clusters:      got {res['n_groups']}, "
                         f"expected {exp['n_clusters']}  "
                         f"{'OK' if res['n_groups'] == exp['n_clusters'] else 'MISMATCH'}")
            if interaction_z is not None:
                match = abs(interaction_z - exp["interaction_z"]) < 0.5
                lines.append(f"    Interaction z: got {interaction_z:.1f}, "
                             f"expected {exp['interaction_z']}  "
                             f"{'OK' if match else 'MISMATCH'}")
            if cwm_main_coef is not None:
                match = abs(cwm_main_coef - exp["cwm_main_coef"]) < 0.005
                lines.append(f"    CWM main coef: got {cwm_main_coef:.3f}, "
                             f"expected {exp['cwm_main_coef']}  "
                             f"{'OK' if match else 'MISMATCH'}")
        else:
            lines.append("\n  DeepSeek cross-complexity: NOT FOUND in results")

        # Check repo cross-model
        repo_key = None
        for k in results:
            if "cross_model" in k.lower():
                repo_key = k
                break

        if repo_key:
            res = results[repo_key]
            exp = PAPER_EXPECTED["repo_cross_model"]

            cwm_z = None
            for name, v in res["coefficients"].items():
                if "CWM" in name and ":" not in name:
                    cwm_z = v["z"]

            lines.append(f"\n  Repo cross-model:")
            if cwm_z is not None:
                match = abs(cwm_z - exp["cwm_deficit_z"]) < 1.0
                lines.append(f"    CWM deficit z: got {cwm_z:.1f}, "
                             f"expected {exp['cwm_deficit_z']}  "
                             f"{'OK' if match else 'MISMATCH'}")

    return "\n".join(lines)


def main():
    args = parse_args()
    eval_dirs = [d.strip() for d in args.eval_dirs.split(",") if d.strip()]
    os.makedirs(args.output_dir, exist_ok=True)

    df = build_dataframe(eval_dirs)
    if df.empty:
        print("ERROR: no data loaded -- check --eval_dirs", file=sys.stderr)
        sys.exit(1)

    print(f"\nData summary:", file=sys.stderr)
    print(f"  Total: {len(df)} obs, {df['problem_id'].nunique()} problems",
          file=sys.stderr)
    print(f"  Formulations: {sorted(df['formulation'].unique())}", file=sys.stderr)
    print(f"  Models:       {sorted(df['model'].unique())}", file=sys.stderr)
    print(f"  Seeds:        {sorted(df['seed'].unique())}", file=sys.stderr)
    print(f"  Complexity:   {sorted(df['complexity'].unique())}", file=sys.stderr)

    print("\nCell accuracy:", file=sys.stderr)
    grp = df.groupby(["formulation", "model", "complexity"])["correct"]
    print(grp.agg(["mean", "count"]).round(4).to_string(), file=sys.stderr)

    all_results = {}

    # === Analysis 1: Cross-complexity per model ===
    for model_name in sorted(df["model"].unique()):
        sub = df[df["model"] == model_name]
        if sub["complexity"].nunique() < 2:
            print(f"\nSKIP per-model cross-complexity for {model_name}: "
                  f"only 1 complexity level", file=sys.stderr)
            continue
        if sub["formulation"].nunique() < 2:
            print(f"\nSKIP per-model cross-complexity for {model_name}: "
                  f"only 1 formulation", file=sys.stderr)
            continue

        key = f"{model_name}_cross_complexity"
        formula = "correct ~ C(formulation) * C(complexity)"
        res = fit_mixed_lm(sub, formula,
                           label=f"Per-model cross-complexity: {model_name}")
        all_results[key] = res

    # === Analysis 2: Cross-complexity combined ===
    if df["complexity"].nunique() >= 2 and df["formulation"].nunique() >= 2:
        formula = "correct ~ C(formulation) * C(complexity)"
        res = fit_mixed_lm(df, formula,
                           label="Combined cross-complexity (all models)")
        all_results["combined_cross_complexity"] = res

    # === Analysis 3: Cross-model (repo-level only) ===
    df_repo = df[df["complexity"] == "repo"]
    if (not df_repo.empty and df_repo["model"].nunique() >= 2
            and df_repo["formulation"].nunique() >= 2):
        formula = "correct ~ C(formulation) * C(model)"
        res = fit_mixed_lm(df_repo, formula,
                           label="Cross-model (repo-level)")
        all_results["repo_cross_model"] = res

    # --- Save JSON ---
    json_path = os.path.join(args.output_dir, "results.json")
    with open(json_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nSaved: {json_path}", file=sys.stderr)

    # --- Save paper numbers ---
    summary = format_paper_numbers(all_results, verify=args.verify)
    txt_path = os.path.join(args.output_dir, "paper_numbers.txt")
    with open(txt_path, "w") as f:
        f.write(summary)
    print(f"Saved: {txt_path}", file=sys.stderr)

    print(summary)


if __name__ == "__main__":
    main()
