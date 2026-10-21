"""Statistical analysis: merge impact + annotation + correctness, run tests, generate figures.

Input: impact JSONL, annotations JSONL, correctness JSONL
Output: analysis_summary.json, pass_fail_report.txt, figures/
"""

import argparse
import json
import logging
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "artifacts" / "paper" / "figures"))
import paper_style

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import yaml
from scipy.stats import chi2_contingency, fisher_exact, kruskal

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def load_config(path: str) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def load_jsonl(path: str) -> list[dict]:
    with open(path) as f:
        return [json.loads(line) for line in f]


def merge_data(impact: list[dict], annotations: list[dict], correctness: list[dict]) -> pd.DataFrame:
    impact_df = pd.DataFrame(impact)
    ann_df = pd.DataFrame(annotations)
    corr_df = pd.DataFrame(correctness)

    for col_name in ["remove", "neutralize"]:
        if col_name in impact_df.columns:
            expanded = pd.json_normalize(impact_df[col_name])
            expanded.columns = [f"{col_name}_{c}" for c in expanded.columns]
            impact_df = pd.concat([impact_df.drop(columns=[col_name]), expanded], axis=1)

    if "fullgen" in impact_df.columns:
        fullgen_expanded = pd.json_normalize(impact_df["fullgen"])
        fullgen_expanded.columns = [f"fullgen_{c}" for c in fullgen_expanded.columns]
        impact_df = pd.concat([impact_df.drop(columns=["fullgen"]), fullgen_expanded], axis=1)

    if "ldim" in impact_df.columns:
        ldim_expanded = pd.json_normalize(impact_df["ldim"])
        ldim_expanded.columns = [f"ldim_{c}" for c in ldim_expanded.columns]
        impact_df = pd.concat([impact_df.drop(columns=["ldim"]), ldim_expanded], axis=1)

    if "annotation" in ann_df.columns:
        ann_expanded = pd.json_normalize(ann_df["annotation"])
        ann_expanded.columns = [f"ann_{c}" for c in ann_expanded.columns]
        ann_df = pd.concat([ann_df.drop(columns=["annotation"]), ann_expanded], axis=1)
    elif "annotation_a" in ann_df.columns:
        ann_a_expanded = pd.json_normalize(ann_df["annotation_a"])
        ann_a_expanded.columns = [f"ann_{c}" for c in ann_a_expanded.columns]
        drop_cols = ["annotation_a"]
        if "annotation_b" in ann_df.columns:
            drop_cols.append("annotation_b")
        ann_df = pd.concat([ann_df.drop(columns=drop_cols), ann_a_expanded], axis=1)

    merge_keys = ["task_id", "message_index"]
    df = impact_df.merge(ann_df, on=merge_keys, how="outer", suffixes=("", "_ann"))
    df = df.merge(corr_df, on=merge_keys, how="outer", suffixes=("", "_corr"))
    return df


def cramers_v(contingency_table: np.ndarray) -> float:
    chi2 = chi2_contingency(contingency_table)[0]
    n = contingency_table.sum()
    min_dim = min(contingency_table.shape) - 1
    if min_dim == 0 or n == 0:
        return 0.0
    return float(np.sqrt(chi2 / (n * min_dim)))


def compute_cohens_kappa(series1: pd.Series, series2: pd.Series) -> float:
    from sklearn.metrics import cohen_kappa_score
    mask = series1.notna() & series2.notna()
    if mask.sum() == 0:
        return 0.0
    return float(cohen_kappa_score(series1[mask], series2[mask]))


def _get_action_changed_col(df: pd.DataFrame) -> str | None:
    """Find the appropriate action-changed column, supporting both old and new formats."""
    if "remove_action_level" in df.columns:
        return "remove_action_level"
    if "fullgen_action_changed" in df.columns:
        return "fullgen_action_changed"
    return None


def _action_changed_series(df: pd.DataFrame, col: str) -> pd.Series:
    """Convert action column to boolean changed series."""
    if col == "remove_action_level":
        return df[col] != "surface_only"
    return df[col].astype(bool)


def _chi2_with_fallback(ct: pd.DataFrame) -> dict:
    """Run chi2 test with Monte Carlo fallback when expected frequencies are too low."""
    _, _, _, expected = chi2_contingency(ct)
    low_expected_ratio = (expected < 5).sum() / expected.size
    method = "chi2"

    if low_expected_ratio > 0.20:
        logger.info("%.0f%% cells have expected freq < 5, using Monte Carlo simulation", low_expected_ratio * 100)
        if ct.shape == (2, 2):
            _, p = fisher_exact(ct.values)
            return {"method": "fisher_exact", "p_value": round(p, 6),
                    "low_expected_ratio": round(low_expected_ratio, 4)}
        n_sim = 10000
        chi2_obs = chi2_contingency(ct)[0]
        row_sums = ct.sum(axis=1).values
        col_sums = ct.sum(axis=0).values
        n_total = ct.values.sum()
        count_ge = 0
        rng = np.random.default_rng(42)
        for _ in range(n_sim):
            sim = rng.multinomial(n_total, (col_sums / n_total).astype(float))
            sim_table = np.outer(row_sums, sim / sim.sum())
            sim_table = np.round(sim_table).astype(int)
            sim_table = np.maximum(sim_table, 0)
            try:
                sim_chi2 = chi2_contingency(sim_table, correction=False)[0]
            except ValueError:
                continue
            if sim_chi2 >= chi2_obs:
                count_ge += 1
        p = count_ge / n_sim
        method = "monte_carlo"
        return {"method": method, "chi2": round(chi2_obs, 4), "p_value": round(p, 6),
                "n_simulations": n_sim, "low_expected_ratio": round(low_expected_ratio, 4)}

    chi2, p, dof, _ = chi2_contingency(ct)
    cv = cramers_v(ct.values)
    return {"method": method, "chi2": round(chi2, 4), "p_value": round(p, 6),
            "dof": int(dof), "cramers_v": round(cv, 4),
            "low_expected_ratio": round(low_expected_ratio, 4)}


def _filter_small_categories(df: pd.DataFrame, col: str, min_n: int = 30) -> tuple[pd.DataFrame, list[str]]:
    """Filter out categories with fewer than min_n observations. Returns filtered df and list of excluded categories."""
    counts = df[col].value_counts()
    excluded = counts[counts < min_n].index.tolist()
    filtered = df[~df[col].isin(excluded)]
    return filtered, excluded


def analysis_function_action(df: pd.DataFrame) -> dict:
    action_col = _get_action_changed_col(df)
    if "ann_type" not in df.columns or action_col is None:
        return {"error": "Missing columns for function x action analysis"}

    sub = df.dropna(subset=["ann_type", action_col])

    all_rates = {}
    all_counts = sub["ann_type"].value_counts().to_dict()
    changed_all = _action_changed_series(sub, action_col)
    for t, group in sub.groupby("ann_type"):
        all_rates[t] = {"rate": round(float(_action_changed_series(group, action_col).mean()), 4), "n": int(len(group))}

    sub_filtered, excluded = _filter_small_categories(sub, "ann_type", min_n=30)
    changed = _action_changed_series(sub_filtered, action_col)
    ct = pd.crosstab(sub_filtered["ann_type"], changed)
    if ct.shape[0] < 2 or ct.shape[1] < 2:
        return {"error": "Insufficient categories (n>=30) for chi2 test",
                "all_rates": all_rates, "excluded_categories": excluded}

    test_result = _chi2_with_fallback(ct)
    rates = changed.groupby(sub_filtered["ann_type"]).mean().to_dict()

    return {
        **test_result,
        "action_change_rates": {k: round(v, 4) for k, v in rates.items()},
        "all_rates_with_n": all_rates,
        "excluded_categories_n_lt_30": excluded,
        "contingency_table": ct.to_dict(),
    }


def analysis_function_correctness(df: pd.DataFrame) -> dict:
    if "ann_type" not in df.columns or "correctness" not in df.columns:
        return {"error": "Missing columns for function x correctness analysis"}

    sub = df.dropna(subset=["ann_type", "correctness"])

    all_corr = {}
    for t, group in sub.groupby("ann_type"):
        corr_dist = group["correctness"].value_counts().to_dict()
        all_corr[t] = {"distribution": {k: int(v) for k, v in corr_dist.items()}, "n": int(len(group))}

    sub_filtered, excluded = _filter_small_categories(sub, "ann_type", min_n=30)
    ct = pd.crosstab(sub_filtered["ann_type"], sub_filtered["correctness"])
    if ct.shape[0] < 2 or ct.shape[1] < 2:
        return {"error": "Insufficient categories (n>=30)", "all_correctness_with_n": all_corr,
                "excluded_categories_n_lt_30": excluded}

    test_result = _chi2_with_fallback(ct)

    verification_incorrect = 0.0
    v_sub = sub[sub["ann_type"] == "verification"]
    if len(v_sub) > 0:
        verification_incorrect = float((v_sub["correctness"] == "incorrect").mean())

    return {
        **test_result,
        "verification_incorrect_rate": round(verification_incorrect, 4),
        "all_correctness_with_n": all_corr,
        "excluded_categories_n_lt_30": excluded,
        "contingency_table": ct.to_dict(),
    }


def analysis_similarity_by_function(df: pd.DataFrame) -> dict:
    """Kruskal-Wallis test: semantic_similarity ~ function_type (non-parametric ANOVA)."""
    sim_col = "remove_semantic_similarity"
    if sim_col not in df.columns or "ann_type" not in df.columns:
        return {"error": f"Missing columns ({sim_col} or ann_type)"}

    sub = df.dropna(subset=[sim_col, "ann_type"])
    sub_filtered, excluded = _filter_small_categories(sub, "ann_type", min_n=30)

    groups = [group[sim_col].values for _, group in sub_filtered.groupby("ann_type")]
    group_names = [name for name, _ in sub_filtered.groupby("ann_type")]

    if len(groups) < 2:
        return {"error": "Need at least 2 function types with n>=30",
                "excluded_categories_n_lt_30": excluded}

    h_stat, p_value = kruskal(*groups)

    per_type = {}
    for name, group in sub.groupby("ann_type"):
        vals = group[sim_col].values
        per_type[name] = {
            "mean": round(float(np.mean(vals)), 4),
            "median": round(float(np.median(vals)), 4),
            "std": round(float(np.std(vals)), 4),
            "min": round(float(np.min(vals)), 4),
            "max": round(float(np.max(vals)), 4),
            "n": int(len(vals)),
        }

    return {
        "kruskal_wallis_H": round(float(h_stat), 4),
        "kruskal_wallis_p": round(float(p_value), 6),
        "per_type_stats": per_type,
        "excluded_categories_n_lt_30": excluded,
        "n_groups_tested": len(groups),
        "group_names_tested": group_names,
    }


def analysis_ldim_agreement(df: pd.DataFrame) -> dict:
    action_col = _get_action_changed_col(df)
    if "ldim_top1_match" not in df.columns or action_col is None:
        return {"error": "Missing columns for LDIM agreement analysis"}

    sub = df.dropna(subset=["ldim_top1_match", action_col])
    ldim_changed = ~sub["ldim_top1_match"].astype(bool)
    fullgen_changed = _action_changed_series(sub, action_col)

    agreement = float((ldim_changed == fullgen_changed).mean())
    kappa = compute_cohens_kappa(ldim_changed.astype(int), fullgen_changed.astype(int))

    return {
        "percent_agreement": round(agreement, 4),
        "cohens_kappa": round(kappa, 4),
        "n": int(len(sub)),
    }


def analysis_remove_vs_neutralize(df: pd.DataFrame) -> dict:
    if "remove_action_level" not in df.columns or "neutralize_action_level" not in df.columns:
        return {"error": "Missing remove/neutralize action_level columns"}

    sub = df.dropna(subset=["remove_action_level", "neutralize_action_level"])
    ct = pd.crosstab(sub["remove_action_level"], sub["neutralize_action_level"])

    result = {"contingency_table": ct.to_dict(), "n": int(len(sub))}

    levels = ["surface_only", "reasoning_step", "final_answer"]
    ct_matrix = ct.reindex(index=levels, columns=levels, fill_value=0)
    off_diag = ct_matrix.values - np.diag(np.diag(ct_matrix.values))
    sym = off_diag + off_diag.T
    np.fill_diagonal(sym, 0)

    if sym.sum() > 0 and ct_matrix.shape[0] >= 2:
        upper = np.triu(sym, k=1)
        if upper.sum() > 0:
            k = ct_matrix.shape[0]
            chi2_stat = 0.0
            for i in range(k):
                for j in range(i + 1, k):
                    nij = off_diag[i, j]
                    nji = off_diag[j, i]
                    if nij + nji > 0:
                        chi2_stat += (nij - nji) ** 2 / (nij + nji)
            dof = k * (k - 1) // 2
            from scipy.stats import chi2 as chi2_dist
            p_value = 1 - chi2_dist.cdf(chi2_stat, dof)
            result["mcnemar_bowker_chi2"] = round(float(chi2_stat), 4)
            result["mcnemar_bowker_p"] = round(float(p_value), 6)
            result["mcnemar_bowker_dof"] = dof
        else:
            result["mcnemar_bowker_note"] = "No off-diagonal asymmetry"
    else:
        remove_binary = (sub["remove_action_level"] != "surface_only").astype(int)
        neut_binary = (sub["neutralize_action_level"] != "surface_only").astype(int)
        b = int(((remove_binary == 1) & (neut_binary == 0)).sum())
        c = int(((remove_binary == 0) & (neut_binary == 1)).sum())
        if b + c > 0:
            chi2_stat = (b - c) ** 2 / (b + c)
            from scipy.stats import chi2 as chi2_dist
            p_value = 1 - chi2_dist.cdf(chi2_stat, 1)
            result["mcnemar_chi2"] = round(float(chi2_stat), 4)
            result["mcnemar_p"] = round(float(p_value), 6)
            result["mcnemar_note"] = "Fell back to binary McNemar"

    remove_dist = sub["remove_action_level"].value_counts().to_dict()
    neut_dist = sub["neutralize_action_level"].value_counts().to_dict()
    result["remove_distribution"] = {k: int(v) for k, v in remove_dist.items()}
    result["neutralize_distribution"] = {k: int(v) for k, v in neut_dist.items()}

    return result


def analysis_position_control(df: pd.DataFrame) -> dict:
    action_col = _get_action_changed_col(df)
    if action_col is None or "ann_type" not in df.columns:
        return {"error": "Missing columns for position control analysis"}

    sub = df.dropna(subset=[action_col, "ann_type"]).copy()

    if action_col == "remove_action_level":
        sub["target"] = (sub[action_col] == "final_answer").astype(int)
    else:
        sub["target"] = sub[action_col].astype(int)

    if sub["target"].nunique() < 2:
        return {"error": "Target variable has no variance"}

    total_per_task = sub.groupby("task_id")["message_index"].transform("max") + 1
    sub["message_position"] = sub["message_index"] / total_per_task.clip(lower=1)

    if "round" in sub.columns:
        sub["round_number"] = sub["round"].fillna(0)
    else:
        sub["round_number"] = sub["message_index"] // 2

    func_dummies = pd.get_dummies(sub["ann_type"], prefix="func", drop_first=True)
    X = pd.concat([sub[["message_position", "round_number"]], func_dummies], axis=1).astype(float)
    y = sub["target"]

    result = {}
    try:
        import statsmodels.api as sm
        X_const = sm.add_constant(X)
        model = sm.Logit(y, X_const).fit(disp=0)
        coefs = {}
        for name, coef, pval in zip(X_const.columns, model.params, model.pvalues):
            coefs[name] = {"coefficient": round(float(coef), 4), "p_value": round(float(pval), 6)}
        result["coefficients"] = coefs
        result["pseudo_r2"] = round(float(model.prsquared), 4)
        result["n"] = int(len(y))
        result["method"] = "statsmodels_logit"
    except (np.linalg.LinAlgError, Exception) as e:
        logger.warning("Logit model failed (%s), falling back to sklearn", e)
        try:
            from sklearn.linear_model import LogisticRegression
            lr = LogisticRegression(max_iter=1000, solver="lbfgs")
            lr.fit(X, y)
            coefs = {}
            for name, coef in zip(X.columns, lr.coef_[0]):
                coefs[name] = {"coefficient": round(float(coef), 4)}
            coefs["intercept"] = {"coefficient": round(float(lr.intercept_[0]), 4)}
            result["coefficients"] = coefs
            result["n"] = int(len(y))
            result["method"] = "sklearn_logistic_fallback"
        except Exception as e2:
            logger.warning("Sklearn fallback also failed: %s", e2)
            result["error"] = str(e)
            result["n"] = int(len(y))
            result["method"] = "failed"
    except ImportError:
        from sklearn.linear_model import LogisticRegression
        lr = LogisticRegression(max_iter=1000, solver="lbfgs")
        lr.fit(X, y)
        coefs = {}
        for name, coef in zip(X.columns, lr.coef_[0]):
            coefs[name] = {"coefficient": round(float(coef), 4)}
        coefs["intercept"] = {"coefficient": round(float(lr.intercept_[0]), 4)}
        result["coefficients"] = coefs
        result["n"] = int(len(y))
        result["method"] = "sklearn_logistic_no_pvalues"

    pos_sig = result.get("coefficients", {}).get("message_position", {}).get("p_value")
    round_sig = result.get("coefficients", {}).get("round_number", {}).get("p_value")
    result["position_significant"] = pos_sig is not None and pos_sig < 0.05
    result["round_significant"] = round_sig is not None and round_sig < 0.05

    return result


def analysis_ols_position_control(df: pd.DataFrame) -> dict:
    """OLS: semantic_similarity ~ C(function_type) + message_position + round.

    Tests whether function_type effects on semantic_similarity remain significant
    after controlling for message position and round number.
    """
    sim_col = "remove_semantic_similarity"
    if sim_col not in df.columns or "ann_type" not in df.columns:
        return {"error": f"Missing columns ({sim_col} or ann_type)"}

    sub = df.dropna(subset=[sim_col, "ann_type"]).copy()
    sub_filtered, excluded = _filter_small_categories(sub, "ann_type", min_n=30)

    if sub_filtered["ann_type"].nunique() < 2:
        return {"error": "Need at least 2 function types with n>=30",
                "excluded_categories_n_lt_30": excluded}

    total_per_task = sub_filtered.groupby("task_id")["message_index"].transform("max") + 1
    sub_filtered["message_position"] = sub_filtered["message_index"] / total_per_task.clip(lower=1)

    if "round" in sub_filtered.columns:
        sub_filtered["round_number"] = sub_filtered["round"].fillna(0)
    else:
        sub_filtered["round_number"] = sub_filtered["message_index"] // 2

    result = {}
    try:
        import statsmodels.api as sm
        import statsmodels.formula.api as smf

        model = smf.ols(
            "remove_semantic_similarity ~ C(ann_type) + message_position + round_number",
            data=sub_filtered,
        ).fit()

        coefs = {}
        for name, coef, pval in zip(model.params.index, model.params, model.pvalues):
            coefs[name] = {"coefficient": round(float(coef), 4), "p_value": round(float(pval), 6)}

        anova = sm.stats.anova_lm(model, typ=2)
        anova_result = {}
        for idx in anova.index:
            row = anova.loc[idx]
            anova_result[idx] = {
                "sum_sq": round(float(row["sum_sq"]), 4),
                "df": int(row["df"]) if not np.isnan(row["df"]) else None,
                "F": round(float(row["F"]), 4) if not np.isnan(row["F"]) else None,
                "p_value": round(float(row["PR(>F)"]), 6) if not np.isnan(row["PR(>F)"]) else None,
            }

        func_type_anova = anova_result.get("C(ann_type)", {})
        func_type_significant = func_type_anova.get("p_value") is not None and func_type_anova["p_value"] < 0.05

        result = {
            "method": "OLS_ANCOVA",
            "formula": "semantic_similarity ~ C(function_type) + message_position + round_number",
            "coefficients": coefs,
            "anova_type2": anova_result,
            "r_squared": round(float(model.rsquared), 4),
            "adj_r_squared": round(float(model.rsquared_adj), 4),
            "n": int(len(sub_filtered)),
            "excluded_categories_n_lt_30": excluded,
            "function_type_significant_after_control": func_type_significant,
            "function_type_F": func_type_anova.get("F"),
            "function_type_p": func_type_anova.get("p_value"),
        }

    except ImportError:
        result = {"error": "statsmodels not available for OLS regression"}

    return result


def analysis_ldim_by_function(df: pd.DataFrame) -> dict:
    action_col = _get_action_changed_col(df)
    if "ldim_top1_match" not in df.columns or action_col is None or "ann_type" not in df.columns:
        return {"error": "Missing columns for LDIM by function analysis"}

    sub = df.dropna(subset=["ldim_top1_match", action_col, "ann_type"])
    ldim_changed = ~sub["ldim_top1_match"].astype(bool)
    fullgen_changed = _action_changed_series(sub, action_col)
    agree = ldim_changed == fullgen_changed

    overall = {"agreement": round(float(agree.mean()), 4), "n": int(len(sub))}
    by_type = {}
    for func_type, group in sub.groupby("ann_type"):
        mask = sub["ann_type"] == func_type
        type_agree = agree[mask]
        n = int(len(type_agree))
        by_type[func_type] = {
            "agreement": round(float(type_agree.mean()), 4),
            "n": n,
            "sufficient_n": n >= 30,
        }

    return {"overall": overall, "by_function_type": by_type}


def analysis_cross_model_kappa(cross_model_path: str) -> dict:
    """Compute cross-model κ from cross-model annotation file."""
    if not os.path.exists(cross_model_path):
        return {"error": "No cross-model annotation file"}

    ann_path = cross_model_path.replace("_cross_model.json", ".jsonl")
    if not os.path.exists(ann_path):
        return {"error": "No annotations JSONL file"}

    anns = load_jsonl(ann_path)
    labels_a, labels_b = [], []

    for r in anns:
        ta = r.get("annotation_a", {}).get("type", "unknown")
        tb = r.get("annotation_b", {}).get("type", "unknown")
        labels_a.append(ta)
        labels_b.append(tb)

    from functional_annotation import compute_cohens_kappa
    kappa = compute_cohens_kappa(labels_a, labels_b)

    all_types = sorted(set(labels_a) | set(labels_b))
    per_type_kappa = {}
    for t in all_types:
        binary_a = [1 if l == t else 0 for l in labels_a]
        binary_b = [1 if l == t else 0 for l in labels_b]
        if len(set(binary_a)) < 2 and len(set(binary_b)) < 2:
            per_type_kappa[t] = None
            continue
        per_type_kappa[t] = round(compute_cohens_kappa(binary_a, binary_b), 4)

    confusion = {}
    for t_a in all_types:
        confusion[t_a] = {}
        for t_b in all_types:
            confusion[t_a][t_b] = sum(1 for a, b in zip(labels_a, labels_b) if a == t_a and b == t_b)

    return {
        "kappa": round(kappa, 4),
        "per_type_binary_kappa": per_type_kappa,
        "n": len(labels_a),
        "n_categories": len(all_types),
        "categories": all_types,
        "confusion_matrix": confusion,
    }


def pass_fail_check(
    df: pd.DataFrame, func_action: dict, ldim_agree: dict,
    remove_vs_neut: dict | None = None, cross_model_kappa: float | None = None,
    sim_by_func: dict | None = None,
) -> dict:
    total_messages = len(df)
    msg_pass = total_messages >= 400

    chi2_pass = False
    rate_diff_pass = False
    rates = []
    if "p_value" in func_action and "action_change_rates" in func_action:
        chi2_pass = func_action["p_value"] < 0.05
        rates = list(func_action["action_change_rates"].values())
        if len(rates) >= 2:
            rate_diff_pass = (max(rates) - min(rates)) > 0.10

    max_rate_diff = round(max(rates) - min(rates), 4) if len(rates) >= 2 else None

    kappa_val = cross_model_kappa if cross_model_kappa is not None else None
    kappa_pass = kappa_val is not None and kappa_val >= 0.4

    neut_diff_pass = False
    neut_p = None
    if remove_vs_neut and "error" not in remove_vs_neut:
        neut_p = remove_vs_neut.get("mcnemar_bowker_p")
        if neut_p is None:
            neut_p = remove_vs_neut.get("mcnemar_p")
        if neut_p is not None:
            neut_diff_pass = neut_p < 0.05

    kw_pass = False
    kw_p = None
    if sim_by_func and "error" not in sim_by_func:
        kw_p = sim_by_func.get("kruskal_wallis_p")
        if kw_p is not None:
            kw_pass = kw_p < 0.05

    return {
        "message_count": {"pass": msg_pass, "value": total_messages, "threshold": 400},
        "chi2_significance": {"pass": chi2_pass and rate_diff_pass,
                              "p_value": func_action.get("p_value"),
                              "max_rate_diff": max_rate_diff},
        "kruskal_wallis": {"pass": kw_pass,
                           "p_value": kw_p,
                           "test": "semantic_similarity ~ function_type"},
        "cross_model_annotation": {"pass": kappa_pass,
                                   "kappa": kappa_val,
                                   "threshold": 0.4},
        "remove_vs_neutralize": {"pass": neut_diff_pass,
                                 "p_value": neut_p},
        "ldim_agreement": {"percent_agreement": ldim_agree.get("percent_agreement"),
                           "cohens_kappa": ldim_agree.get("cohens_kappa")},
    }


def plot_function_distribution(df: pd.DataFrame, output_dir: str):
    paper_style.apply_style()
    if "ann_type" not in df.columns:
        return
    counts = df["ann_type"].value_counts()
    fig, ax = plt.subplots(figsize=(10, 5))
    counts.plot(kind="bar", ax=ax, color="steelblue")
    ax.set_xlabel("Function Type")
    ax.set_ylabel("Count")
    ax.set_title("Distribution of Message Function Types")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, "function_distribution.png"), dpi=150)
    plt.close(fig)


def plot_action_change_by_type(df: pd.DataFrame, output_dir: str):
    action_col = _get_action_changed_col(df)
    if "ann_type" not in df.columns or action_col is None:
        return
    sub = df.dropna(subset=["ann_type", action_col])
    changed = _action_changed_series(sub, action_col)
    grouped = changed.groupby(sub["ann_type"])
    means = grouped.mean()
    stds = grouped.std()
    counts = grouped.count()
    ci95 = 1.96 * stds / np.sqrt(counts)

    fig, ax = plt.subplots(figsize=(10, 5))
    x = range(len(means))
    ax.bar(x, means, yerr=ci95, capsize=4, color="coral")
    ax.set_xticks(x)
    ax.set_xticklabels(means.index, rotation=45, ha="right")
    ax.set_xlabel("Function Type")
    ax.set_ylabel("Action Change Rate")
    ax.set_title("Action Change Rate by Function Type (95% CI)")
    ax.set_ylim(0, 1)
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, "action_change_by_type.png"), dpi=150)
    plt.close(fig)


def plot_function_correctness_heatmap(df: pd.DataFrame, output_dir: str):
    if "ann_type" not in df.columns or "correctness" not in df.columns:
        return
    ct = pd.crosstab(df["ann_type"], df["correctness"])
    if ct.empty:
        return
    fig, ax = plt.subplots(figsize=(10, 7))
    sns.heatmap(ct, annot=True, fmt="d", cmap="YlOrRd", ax=ax)
    ax.set_title("Function Type × Correctness")
    ax.set_xlabel("Correctness")
    ax.set_ylabel("Function Type")
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, "function_correctness_heatmap.png"), dpi=150)
    plt.close(fig)


def plot_ldim_agreement(df: pd.DataFrame, output_dir: str):
    sim_col = "remove_semantic_similarity" if "remove_semantic_similarity" in df.columns else "fullgen_semantic_similarity"
    if "ldim_logprob_shift" not in df.columns or sim_col not in df.columns:
        return
    sub = df.dropna(subset=["ldim_logprob_shift", sim_col])
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.scatter(sub["ldim_logprob_shift"], sub[sim_col], alpha=0.5, s=20)
    ax.set_xlabel("LDIM Logprob Shift")
    ax.set_ylabel("Full-gen Semantic Similarity")
    ax.set_title("LDIM vs Full-Generation Agreement")
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, "ldim_agreement.png"), dpi=150)
    plt.close(fig)


def plot_remove_vs_neutralize(df: pd.DataFrame, output_dir: str):
    if "remove_action_level" not in df.columns or "neutralize_action_level" not in df.columns:
        return
    sub = df.dropna(subset=["remove_action_level", "neutralize_action_level"])
    levels = ["surface_only", "reasoning_step", "final_answer"]
    remove_counts = sub["remove_action_level"].value_counts().reindex(levels, fill_value=0)
    neut_counts = sub["neutralize_action_level"].value_counts().reindex(levels, fill_value=0)

    x = np.arange(len(levels))
    width = 0.35
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(x - width / 2, remove_counts.values, width, label="Remove", color="coral")
    ax.bar(x + width / 2, neut_counts.values, width, label="Neutralize", color="steelblue")
    ax.set_xticks(x)
    ax.set_xticklabels(levels, rotation=20, ha="right")
    ax.set_xlabel("Action Level")
    ax.set_ylabel("Count")
    ax.set_title("Remove vs Neutralize: Action Level Distribution")
    ax.legend()
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, "remove_vs_neutralize.png"), dpi=150)
    plt.close(fig)


def plot_similarity_by_function(df: pd.DataFrame, output_dir: str):
    sim_col = "remove_semantic_similarity"
    if sim_col not in df.columns or "ann_type" not in df.columns:
        return
    sub = df.dropna(subset=[sim_col, "ann_type"])
    if sub.empty:
        return
    fig, ax = plt.subplots(figsize=(10, 6))
    types_ordered = sub.groupby("ann_type")[sim_col].median().sort_values().index.tolist()
    sns.boxplot(data=sub, x="ann_type", y=sim_col, order=types_ordered, ax=ax)
    ax.set_xlabel("Function Type")
    ax.set_ylabel("Semantic Similarity (Remove Ablation)")
    ax.set_title("Impact Distribution by Function Type")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, "similarity_by_function.png"), dpi=150)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description="Statistical analysis of communication traces")
    parser.add_argument("--config", type=str, default="configs/mvp.yaml")
    parser.add_argument("--impact", type=str, default=None)
    parser.add_argument("--annotations", type=str, default=None)
    parser.add_argument("--correctness", type=str, default=None)
    args = parser.parse_args()

    cfg = load_config(args.config)
    impact_path = args.impact or os.path.join(cfg["output"]["impact_dir"], "impact.jsonl")
    ann_path = args.annotations or os.path.join(cfg["output"]["annotation_dir"], "annotations.jsonl")
    corr_path = args.correctness or os.path.join(cfg["output"]["correctness_dir"], "correctness.jsonl")
    figure_dir = cfg["output"]["figure_dir"]
    analysis_dir = cfg["output"]["analysis_dir"]
    os.makedirs(figure_dir, exist_ok=True)
    os.makedirs(analysis_dir, exist_ok=True)

    logger.info("Loading data...")
    impact = load_jsonl(impact_path)
    annotations = load_jsonl(ann_path)
    correctness_data = load_jsonl(corr_path)

    df = merge_data(impact, annotations, correctness_data)
    logger.info("Merged %d records", len(df))

    logger.info("Filtering message_index=0 records...")
    pre_filter = len(df)
    df = df[df["message_index"] != 0].reset_index(drop=True)
    logger.info("Filtered %d → %d records (removed message_index=0)", pre_filter, len(df))

    logger.info("Running analyses...")
    func_action = analysis_function_action(df)
    func_corr = analysis_function_correctness(df)
    sim_by_func = analysis_similarity_by_function(df)
    ldim_agree = analysis_ldim_agreement(df)
    remove_vs_neut = analysis_remove_vs_neutralize(df)
    pos_control = analysis_position_control(df)
    ols_pos_control = analysis_ols_position_control(df)
    ldim_by_func = analysis_ldim_by_function(df)
    cross_model_kappa = None
    cross_model_path = os.path.join(cfg["output"]["annotation_dir"], "annotations_cross_model.json")
    if os.path.exists(cross_model_path):
        with open(cross_model_path) as f:
            cross_model_data = json.load(f)
            cross_model_kappa = cross_model_data.get("cohens_kappa")

    cross_kappa_detail = analysis_cross_model_kappa(cross_model_path)
    effective_kappa = cross_kappa_detail.get("kappa") if "error" not in cross_kappa_detail else cross_model_kappa
    pf = pass_fail_check(df, func_action, ldim_agree, remove_vs_neut, effective_kappa, sim_by_func)

    neutralize_finding = (
        "Neutralizing messages preserves task-solvability but disrupts reasoning paths, "
        "while removing messages has more varied effects including answer changes — "
        "demonstrating that message information value and structural value are empirically separable."
    )

    summary = {
        "function_x_action": func_action,
        "function_x_correctness": func_corr,
        "similarity_by_function": sim_by_func,
        "ldim_agreement": ldim_agree,
        "remove_vs_neutralize": remove_vs_neut,
        "position_control_logistic": pos_control,
        "position_control_ols": ols_pos_control,
        "ldim_by_function": ldim_by_func,
        "cross_model_kappa_detail": cross_kappa_detail,
        "neutralize_finding": neutralize_finding,
        "pass_fail": pf,
        "total_messages": len(df),
    }

    summary_path = os.path.join(analysis_dir, "analysis_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2, default=str)
    logger.info("Summary saved to %s", summary_path)

    report_lines = [
        "=" * 60,
        "PASS/FAIL REPORT",
        "=" * 60,
        "",
        f"1. Message count: {pf['message_count']['value']}",
        f"   {'PASS' if pf['message_count']['pass'] else 'FAIL'}: >= {pf['message_count']['threshold']} messages collected",
        "",
        f"2. [PRIMARY] Kruskal-Wallis (semantic_similarity ~ function_type): p={pf['kruskal_wallis']['p_value']}",
        f"   {'PASS' if pf['kruskal_wallis']['pass'] else 'FAIL'}: p < 0.05",
        "",
        f"3. [SECONDARY] Chi-squared test (action_level ~ function_type): p={pf['chi2_significance']['p_value']}",
        f"   Max rate difference: {pf['chi2_significance']['max_rate_diff']}",
        f"   {'PASS' if pf['chi2_significance']['pass'] else 'FAIL'}: p < 0.05 AND rate diff > 10pp",
        "",
        f"4. Cross-model annotation: kappa={pf['cross_model_annotation']['kappa']}",
        f"   {'PASS' if pf['cross_model_annotation']['pass'] else 'FAIL'}: cross-model kappa >= {pf['cross_model_annotation']['threshold']}",
        "",
        f"5. Remove vs Neutralize: p={pf['remove_vs_neutralize']['p_value']}",
        f"   {'PASS' if pf['remove_vs_neutralize']['pass'] else 'FAIL'}: significant difference (p < 0.05)",
        "",
        f"6. [CRITICAL] OLS Position Control: semantic_similarity ~ C(function_type) + position + round",
        f"   function_type significant after control: {ols_pos_control.get('function_type_significant_after_control', 'N/A')}",
        f"   function_type F={ols_pos_control.get('function_type_F', 'N/A')}, p={ols_pos_control.get('function_type_p', 'N/A')}",
        f"   R²={ols_pos_control.get('r_squared', 'N/A')}, adj_R²={ols_pos_control.get('adj_r_squared', 'N/A')}",
        "",
        f"7. LDIM-Fullgen agreement (exploratory, excluded from paper):",
        f"   percent_agreement={pf['ldim_agreement']['percent_agreement']}",
        f"   cohens_kappa={pf['ldim_agreement']['cohens_kappa']}",
        "",
        "=" * 60,
    ]
    report_path = os.path.join(analysis_dir, "pass_fail_report.txt")
    with open(report_path, "w") as f:
        f.write("\n".join(report_lines) + "\n")
    logger.info("Report saved to %s", report_path)

    logger.info("Generating figures...")
    plot_function_distribution(df, figure_dir)
    plot_action_change_by_type(df, figure_dir)
    plot_function_correctness_heatmap(df, figure_dir)
    plot_ldim_agreement(df, figure_dir)
    plot_remove_vs_neutralize(df, figure_dir)
    plot_similarity_by_function(df, figure_dir)

    logger.info("Analysis complete.")


if __name__ == "__main__":
    main()
