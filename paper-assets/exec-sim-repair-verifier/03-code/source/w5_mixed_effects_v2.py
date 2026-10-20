"""
W5 Mixed-Effects Linear Probability Model (LPM) (v2): multi-seed CWM support.

Uses statsmodels MixedLM (not logistic regression). Coefficients represent
probability differences in percentage points (pp), not log-odds ratios.

Cross-complexity model: correct ~ formulation * complexity + (1|problem_id)
Cross-model model:     correct ~ formulation * model + (1|problem_id)

Input:
  --eval_dirs   comma-separated eval result directories
  --data_dir    directory with {test,cwm_test}.jsonl for mutation_type metadata
  --output_dir  output directory for JSON + LaTeX

Output:
  w5_mixed_effects_results.json   combined model results
  w5_latex_tables.tex             LaTeX table fragments

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


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(
        description="W5 Mixed-Effects LPM: formulation × complexity / model (coefficients = probability diff in pp)"
    )
    p.add_argument("--eval_dirs", required=True,
                   help="Comma-separated eval result directories")
    p.add_argument("--data_dir", default=None,
                   help="Directory with test.jsonl / cwm_test.jsonl for "
                        "mutation_type metadata (optional)")
    p.add_argument("--output_dir", default="artifacts/w5_mixed_effects",
                   help="Output directory (default: artifacts/w5_mixed_effects)")
    p.add_argument("--ref_formulation", default="CLS",
                   help="Reference formulation for empirical odds ratios (default: CLS)")
    p.add_argument("--bootstrap_n", type=int, default=2000,
                   help="Bootstrap iterations for OR CIs (default: 2000)")
    return p.parse_args()


# ---------------------------------------------------------------------------
# Path → metadata inference
# ---------------------------------------------------------------------------

def infer_metadata(dirpath: str) -> dict:
    """Infer formulation, model, seed, complexity from directory name."""
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
    """Locate the prediction JSONL inside an eval directory."""
    p = Path(dirpath)
    for pattern in ["eval_*_predictions.jsonl", "predictions_*.jsonl"]:
        hits = sorted(p.glob(pattern))
        if hits:
            return str(hits[0])
    for name in ["results_incremental.jsonl", "predictions.jsonl"]:
        fp = p / name
        if fp.exists():
            return str(fp)
    return None


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_jsonl(path: str) -> list[dict]:
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def load_metadata(data_dir: str) -> dict:
    """Load problem metadata (mutation_type, source) from test splits."""
    meta = {}
    for fname in ["test.jsonl", "cwm_test.jsonl", "val.jsonl"]:
        fp = os.path.join(data_dir, fname)
        if not os.path.exists(fp):
            continue
        for rec in load_jsonl(fp):
            pid = rec.get("problem_id")
            if pid and pid not in meta:
                meta[pid] = dict(
                    mutation_type=rec.get("mutation_type", "unknown"),
                    source=rec.get("source", "unknown"),
                )
    return meta


def build_dataframe(eval_dirs: list[str],
                    metadata: dict | None = None) -> pd.DataFrame:
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
        tag = (f"{info['formulation']}/{info['model']}/s{info['seed']}"
               f"/{info['complexity']}")
        print(f"LOAD {tag}: {len(preds)} samples ← {pred_file}",
              file=sys.stderr)

        for rec in preds:
            pid = (rec.get("problem_id") or rec.get("instance_id")
                   or rec.get("task_id") or rec.get("id"))
            correct = rec.get("correct")
            if pid is None or correct is None:
                continue

            mut = "unknown"
            if metadata and pid in metadata:
                mut = metadata[pid]["mutation_type"]
            elif "mutation_type" in rec:
                mut = rec["mutation_type"]

            rows.append(dict(
                problem_id=pid,
                formulation=info["formulation"],
                model=info["model"],
                seed=info["seed"],
                correct=int(correct),
                complexity=info["complexity"],
                mutation_type=mut,
            ))

    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Mixed-effects model fitting
# ---------------------------------------------------------------------------

def fit_mixed_lm(df: pd.DataFrame, formula: str,
                 groups_col: str = "problem_id",
                 label: str = "") -> tuple[dict, object]:
    """Fit MixedLM (Linear Probability Model). Coefficients are probability diffs (pp), not log-odds."""
    import statsmodels.formula.api as smf

    df = df.copy()
    for col in ["formulation", "model", "complexity", "mutation_type"]:
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
        # Singular design matrix — drop interaction and retry with main effects only
        fallback = re.sub(r"\s*\*\s*", " + ", formula)
        print(f"  WARN: singular matrix with interaction, fallback → {fallback}",
              file=sys.stderr)
        md = smf.mixedlm(fallback, df, groups=df[groups_col])
        result = md.fit(reml=True)
        formula = fallback
    print(result.summary(), file=sys.stderr)

    # --- fixed effects ---
    fe = result.fe_params
    se = result.bse_fe
    ci = result.conf_int()
    pvals = result.pvalues

    coefficients = {}
    for name in fe.index:
        coefficients[name] = dict(
            coef=round(float(fe[name]), 4),
            se=round(float(se[name]), 4),
            z=round(float(fe[name] / se[name]) if se[name] > 0 else 0, 3),
            p=round(float(pvals[name]), 4) if name in pvals.index else None,
            ci_lower=round(float(ci.loc[name, 0]), 4),
            ci_upper=round(float(ci.loc[name, 1]), 4),
        )

    # --- random effects ---
    re_var = (float(result.cov_re.iloc[0, 0])
              if hasattr(result.cov_re, "iloc")
              else float(result.cov_re))

    # --- joint Wald tests (ANOVA-like) ---
    anova = _joint_wald_tests(result)

    out = dict(
        formula=formula,
        n_obs=len(df),
        n_groups=int(df[groups_col].nunique()),
        coefficients=coefficients,
        random_effects=dict(
            group=groups_col,
            variance=round(re_var, 6),
            sd=round(float(np.sqrt(max(re_var, 0))), 4),
        ),
        anova=anova,
        log_likelihood=round(float(result.llf), 2),
    )
    return out, result


def _joint_wald_tests(result) -> dict:
    """Compute joint Wald χ² for each model term (main effects + interaction)."""
    from scipy import stats as sp_stats

    param_names = list(result.fe_params.index)
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
        elif "complexity" in name or "mutation_type" in name:
            term = "complexity"
        else:
            term = name
        terms.setdefault(term, []).append(i)

    anova = {}
    for term, indices in terms.items():
        beta = result.fe_params.values[indices]
        cov = result.cov_params().iloc[indices, :]
        cov = cov.iloc[:, indices].values
        try:
            chi2 = float(beta @ np.linalg.solve(cov, beta))
            df = len(indices)
            p = float(1 - sp_stats.chi2.cdf(chi2, df))
            anova[term] = dict(wald_chi2=round(chi2, 3), df=df,
                               p=round(p, 4))
        except np.linalg.LinAlgError:
            anova[term] = dict(wald_chi2=None, df=len(indices), p=None,
                               error="singular covariance")
    return anova


# ---------------------------------------------------------------------------
# Empirical odds ratios with bootstrap CI
# ---------------------------------------------------------------------------

def empirical_odds_ratios(df: pd.DataFrame, group_col: str,
                          ref_level: str, n_boot: int = 2000) -> dict:
    """Odds ratio of each group level vs. ref_level, with bootstrap 95% CI."""
    rng = np.random.default_rng(42)
    ref = df.loc[df[group_col] == ref_level, "correct"].values

    results = {}
    for level in sorted(df[group_col].unique()):
        vals = df.loc[df[group_col] == level, "correct"].values
        p = vals.mean()
        p_ref = ref.mean()
        odds = p / (1 - p) if 0 < p < 1 else float("inf")
        odds_ref = p_ref / (1 - p_ref) if 0 < p_ref < 1 else float("inf")
        or_val = (odds / odds_ref
                  if odds_ref not in (0, float("inf")) else None)

        boot_ors = []
        for _ in range(n_boot):
            br = rng.choice(ref, size=len(ref), replace=True)
            bs = rng.choice(vals, size=len(vals), replace=True)
            pr, ps = br.mean(), bs.mean()
            if 0 < pr < 1 and 0 < ps < 1:
                boot_ors.append((ps / (1 - ps)) / (pr / (1 - pr)))

        if boot_ors:
            ci_lo, ci_hi = np.percentile(boot_ors, [2.5, 97.5])
        else:
            ci_lo = ci_hi = None

        results[level] = dict(
            accuracy=round(float(p), 4),
            n=int(len(vals)),
            or_vs_ref=(round(float(or_val), 4)
                       if or_val is not None else None),
            or_ci_lower=(round(float(ci_lo), 4)
                         if ci_lo is not None else None),
            or_ci_upper=(round(float(ci_hi), 4)
                         if ci_hi is not None else None),
        )
    return results


# ---------------------------------------------------------------------------
# LaTeX output
# ---------------------------------------------------------------------------

def _clean_param_name(name: str) -> str:
    """Shorten statsmodels-style parameter names for LaTeX."""
    name = name.replace("C(formulation)", "Form.")
    name = name.replace("C(model)", "Model")
    name = name.replace("C(complexity)", "Compl.")
    name = name.replace("C(mutation_type)", "Mut.")
    name = name.replace("[T.", "[")
    return name.replace("_", r"\_")


def _fmt_p(p: float | None) -> str:
    if p is None:
        return "---"
    if p < 0.001:
        return "$<$.001"
    s = f"{p:.3f}"
    if p < 0.01:
        return s + "**"
    if p < 0.05:
        return s + "*"
    return s


def format_latex_table(results: dict, caption: str, label: str) -> str:
    coeffs = results["coefficients"]
    re = results["random_effects"]

    lines = [
        r"\begin{table}[t]",
        r"\centering\small",
        rf"\caption{{{caption}}}",
        rf"\label{{{label}}}",
        r"\begin{tabular}{lrrrr}",
        r"\toprule",
        r"Effect & Coef.\ (pp) & SE & $z$ & $p$ \\",
        r"\midrule",
    ]
    for name, v in coeffs.items():
        dn = _clean_param_name(name)
        lines.append(
            f"{dn} & {v['coef']:+.3f} & {v['se']:.3f} "
            f"& {v['z']:.2f} & {_fmt_p(v['p'])} \\\\"
        )
    lines.append(r"\midrule")
    lines.append(
        rf"$\sigma^2_{{\text{{pid}}}}$ & "
        rf"\multicolumn{{4}}{{c}}{{{re['variance']:.4f} "
        rf"(SD={re['sd']:.3f})}} \\"
    )
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{table}"]
    return "\n".join(lines)


def format_or_latex(or_dict: dict, ref: str, caption: str,
                    label: str) -> str:
    """LaTeX table for empirical odds ratios."""
    lines = [
        r"\begin{table}[t]",
        r"\centering\small",
        rf"\caption{{{caption}}}",
        rf"\label{{{label}}}",
        r"\begin{tabular}{lrrrl}",
        r"\toprule",
        rf"Formulation & Acc. & OR (vs.\ {ref}) & 95\% CI & $n$ \\",
        r"\midrule",
    ]
    for level, v in or_dict.items():
        or_str = (f"{v['or_vs_ref']:.2f}"
                  if v["or_vs_ref"] is not None else "ref")
        ci_str = (f"[{v['or_ci_lower']:.2f}, {v['or_ci_upper']:.2f}]"
                  if v["or_ci_lower"] is not None else "---")
        if level == ref:
            or_str, ci_str = "1.00", "ref"
        lines.append(
            f"{level} & {v['accuracy']:.3f} & {or_str} & {ci_str} "
            f"& {v['n']} \\\\"
        )
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{table}"]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    eval_dirs = [d.strip() for d in args.eval_dirs.split(",") if d.strip()]
    os.makedirs(args.output_dir, exist_ok=True)

    metadata = None
    if args.data_dir:
        metadata = load_metadata(args.data_dir)
        print(f"Metadata: {len(metadata)} problems loaded", file=sys.stderr)

    df = build_dataframe(eval_dirs, metadata)
    if df.empty:
        print("ERROR: no data loaded — check --eval_dirs", file=sys.stderr)
        sys.exit(1)

    print(f"\nData: {len(df)} obs, {df['problem_id'].nunique()} problems",
          file=sys.stderr)
    print(f"  formulations : {sorted(df['formulation'].unique())}",
          file=sys.stderr)
    print(f"  models       : {sorted(df['model'].unique())}",
          file=sys.stderr)
    print(f"  seeds        : {sorted(df['seed'].unique())}",
          file=sys.stderr)
    print(f"  complexity   : {sorted(df['complexity'].unique())}",
          file=sys.stderr)
    mt = df["mutation_type"].unique()
    if not (len(mt) == 1 and mt[0] == "unknown"):
        print(f"  mutation_type: {sorted(mt)}", file=sys.stderr)

    print("\nCell accuracy (formulation × model × complexity):",
          file=sys.stderr)
    grp = df.groupby(["formulation", "model", "complexity"])["correct"]
    print(grp.agg(["mean", "count"]).round(4).to_string(), file=sys.stderr)

    all_results: dict = {}
    latex_parts: list[str] = []

    # ---- choose complexity variable ----
    has_mutation = (df["mutation_type"].nunique() > 1
                    and (df["mutation_type"] != "unknown").any())
    cx_col = "mutation_type" if has_mutation else "complexity"

    # ==== Model 1: cross-complexity ====
    if df[cx_col].nunique() >= 2:
        formula1 = f"correct ~ C(formulation) * C({cx_col})"
        res1, _ = fit_mixed_lm(
            df, formula1,
            label=f"Model 1 (cross-complexity): {formula1}")
        or1 = empirical_odds_ratios(
            df, "formulation", args.ref_formulation, args.bootstrap_n)
        res1["empirical_or_by_formulation"] = or1
        all_results["cross_complexity"] = res1

        latex_parts.append(format_latex_table(
            res1,
            caption=(r"Mixed-effects LPM: formulation $\times$ "
                     "complexity interaction."),
            label="tab:w5-complexity"))
        latex_parts.append(format_or_latex(
            or1, args.ref_formulation,
            caption="Empirical odds ratios by formulation (cross-complexity).",
            label="tab:w5-or-complexity"))
    else:
        print(f"\nSKIP Model 1: {cx_col} has only 1 level", file=sys.stderr)

    # ==== Model 2: cross-model ====
    if df["model"].nunique() >= 2:
        formula2 = "correct ~ C(formulation) * C(model)"
        res2, _ = fit_mixed_lm(
            df, formula2,
            label=f"Model 2 (cross-model): {formula2}")
        for m in sorted(df["model"].unique()):
            sub = df[df["model"] == m]
            or_m = empirical_odds_ratios(
                sub, "formulation", args.ref_formulation, args.bootstrap_n)
            res2[f"empirical_or_{m}"] = or_m
        all_results["cross_model"] = res2

        latex_parts.append(format_latex_table(
            res2,
            caption=(r"Mixed-effects LPM: formulation $\times$ "
                     "model interaction."),
            label="tab:w5-model"))
    else:
        print("\nSKIP Model 2: only 1 model in data", file=sys.stderr)

    # ---- save ----
    json_path = os.path.join(args.output_dir, "w5_mixed_effects_results.json")
    with open(json_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    latex_path = os.path.join(args.output_dir, "w5_latex_tables.tex")
    with open(latex_path, "w") as f:
        f.write("\n\n".join(latex_parts))

    print(f"\nSaved: {json_path}", file=sys.stderr)
    print(f"Saved: {latex_path}", file=sys.stderr)

    # stdout: JSON for piping
    print(json.dumps(all_results, indent=2, default=str))


if __name__ == "__main__":
    main()
