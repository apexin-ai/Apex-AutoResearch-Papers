"""Length-controlled FK Grade analysis.

For verbosity and formality rewrites, compute:
  - delta sentence length and delta FK grade (CF - original)
  - Cohen's d for each axis
  - OLS regression: delta_FK ~ axis (and + delta_sentlen)
  - Pearson correlation between delta_sentlen and delta_FK

Outputs JSON to stdout.
"""
import json
import re
import sys
import warnings

import numpy as np
import pandas as pd
import textstat
from scipy import stats
import statsmodels.api as sm

warnings.filterwarnings("ignore")

DATA_ROOT = "/root/causal_style_decomp_judge/data"
FORMALITY_FILE = f"{DATA_ROOT}/verified.jsonl"
VERBOSITY_FILE = f"{DATA_ROOT}/verified_verbosity.jsonl"


_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+|\n+")


def sentence_count(text: str) -> int:
    sents = [s.strip() for s in _SENT_SPLIT.split(text) if s.strip()]
    return max(1, len(sents))


def word_count(text: str) -> int:
    return max(1, len(re.findall(r"\b[\w']+\b", text)))


def avg_sentence_length(text: str) -> float:
    return word_count(text) / sentence_count(text)


def fk_grade(text: str) -> float:
    return float(textstat.flesch_kincaid_grade(text))


def features(text: str) -> dict:
    return {
        "fk": fk_grade(text),
        "sentlen": avg_sentence_length(text),
        "words": word_count(text),
    }


def load_pairs(path: str, axis_name: str) -> pd.DataFrame:
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            orig = obj.get("original_text") or obj.get("response")
            cf = obj.get("counterfactual_text")
            if not orig or not cf:
                continue
            of = features(orig)
            cff = features(cf)
            rows.append({
                "id": obj.get("id"),
                "axis": axis_name,
                "passed_cf": bool(obj.get("passed_cf", False)),
                "orig_fk": of["fk"],
                "cf_fk": cff["fk"],
                "delta_fk": cff["fk"] - of["fk"],
                "orig_sentlen": of["sentlen"],
                "cf_sentlen": cff["sentlen"],
                "delta_sentlen": cff["sentlen"] - of["sentlen"],
                "orig_words": of["words"],
                "cf_words": cff["words"],
                "delta_words": cff["words"] - of["words"],
            })
    return pd.DataFrame(rows)


def cohens_d_paired(deltas: np.ndarray) -> float:
    deltas = np.asarray(deltas, dtype=float)
    if deltas.size < 2:
        return float("nan")
    sd = deltas.std(ddof=1)
    if sd == 0:
        return float("nan")
    return float(deltas.mean() / sd)


def describe(df: pd.DataFrame) -> dict:
    return {
        "n": int(len(df)),
        "delta_fk_mean": float(df["delta_fk"].mean()),
        "delta_fk_sd": float(df["delta_fk"].std(ddof=1)),
        "delta_fk_d": cohens_d_paired(df["delta_fk"].to_numpy()),
        "delta_sentlen_mean": float(df["delta_sentlen"].mean()),
        "delta_sentlen_sd": float(df["delta_sentlen"].std(ddof=1)),
        "delta_sentlen_d": cohens_d_paired(df["delta_sentlen"].to_numpy()),
        "delta_words_mean": float(df["delta_words"].mean()),
        "delta_words_d": cohens_d_paired(df["delta_words"].to_numpy()),
    }


def run_regressions(df_all: pd.DataFrame) -> dict:
    df = df_all.copy()
    df["style_axis"] = (df["axis"] == "verbosity").astype(int)

    # Model 1: delta_fk ~ style_axis
    X1 = sm.add_constant(df[["style_axis"]])
    m1 = sm.OLS(df["delta_fk"], X1).fit()

    # Model 2: delta_fk ~ style_axis + delta_sentlen
    X2 = sm.add_constant(df[["style_axis", "delta_sentlen"]])
    m2 = sm.OLS(df["delta_fk"], X2).fit()

    c1 = float(m1.params["style_axis"])
    c2 = float(m2.params["style_axis"])
    reduction = float((c1 - c2) / c1 * 100) if c1 != 0 else float("nan")

    return {
        "n_total": int(len(df)),
        "n_verbosity": int(df["style_axis"].sum()),
        "n_formality": int((df["style_axis"] == 0).sum()),
        "model1_no_control": {
            "style_axis_coef": c1,
            "style_axis_se": float(m1.bse["style_axis"]),
            "style_axis_t": float(m1.tvalues["style_axis"]),
            "style_axis_p": float(m1.pvalues["style_axis"]),
            "intercept": float(m1.params["const"]),
            "r2": float(m1.rsquared),
            "adj_r2": float(m1.rsquared_adj),
        },
        "model2_length_controlled": {
            "style_axis_coef": c2,
            "style_axis_se": float(m2.bse["style_axis"]),
            "style_axis_t": float(m2.tvalues["style_axis"]),
            "style_axis_p": float(m2.pvalues["style_axis"]),
            "delta_sentlen_coef": float(m2.params["delta_sentlen"]),
            "delta_sentlen_se": float(m2.bse["delta_sentlen"]),
            "delta_sentlen_t": float(m2.tvalues["delta_sentlen"]),
            "delta_sentlen_p": float(m2.pvalues["delta_sentlen"]),
            "intercept": float(m2.params["const"]),
            "r2": float(m2.rsquared),
            "adj_r2": float(m2.rsquared_adj),
        },
        "coef_reduction_pct": reduction,
    }


def mediation_baron_kenny(df_all: pd.DataFrame) -> dict:
    """Simple Baron-Kenny mediation.

    X = style_axis (0=formality, 1=verbosity)
    M = delta_sentlen
    Y = delta_fk
    """
    df = df_all.copy()
    df["X"] = (df["axis"] == "verbosity").astype(int)
    # a: X -> M
    a_model = sm.OLS(df["delta_sentlen"], sm.add_constant(df[["X"]])).fit()
    a = float(a_model.params["X"])
    a_se = float(a_model.bse["X"])

    # b, c': X+M -> Y
    bc_model = sm.OLS(df["delta_fk"], sm.add_constant(df[["X", "delta_sentlen"]])).fit()
    b = float(bc_model.params["delta_sentlen"])
    b_se = float(bc_model.bse["delta_sentlen"])
    c_prime = float(bc_model.params["X"])

    # total: X -> Y
    c_model = sm.OLS(df["delta_fk"], sm.add_constant(df[["X"]])).fit()
    c = float(c_model.params["X"])

    indirect = a * b
    # Sobel SE
    sobel_se = float(np.sqrt((b ** 2) * (a_se ** 2) + (a ** 2) * (b_se ** 2)))
    sobel_z = indirect / sobel_se if sobel_se > 0 else float("nan")
    sobel_p = float(2 * (1 - stats.norm.cdf(abs(sobel_z)))) if not np.isnan(sobel_z) else float("nan")

    prop_mediated = (indirect / c) if c != 0 else float("nan")

    return {
        "a_X_to_M": a,
        "b_M_to_Y_given_X": b,
        "c_total_X_to_Y": c,
        "c_prime_direct": c_prime,
        "indirect_ab": float(indirect),
        "sobel_se": sobel_se,
        "sobel_z": float(sobel_z) if not np.isnan(sobel_z) else None,
        "sobel_p": sobel_p if not np.isnan(sobel_p) else None,
        "proportion_mediated": float(prop_mediated) if not np.isnan(prop_mediated) else None,
    }


def main():
    form = load_pairs(FORMALITY_FILE, "formality")
    verb = load_pairs(VERBOSITY_FILE, "verbosity")

    # Use NLI-passing subset (matches paper's main-analysis universe)
    form_p = form[form["passed_cf"]].reset_index(drop=True)
    verb_p = verb[verb["passed_cf"]].reset_index(drop=True)

    # Also compute on all pairs for transparency
    out = {}
    out["descriptive_passed_only"] = {
        "verbosity": describe(verb_p),
        "formality": describe(form_p),
    }
    out["descriptive_all_pairs"] = {
        "verbosity": describe(verb),
        "formality": describe(form),
    }
    # Primary regression on passed_cf only (matches main analysis universe)
    df_passed = pd.concat([form_p, verb_p], ignore_index=True)
    out["regression_passed_only"] = run_regressions(df_passed)
    out["mediation_passed_only"] = mediation_baron_kenny(df_passed)

    # Also run on all pairs for robustness
    df_all = pd.concat([form, verb], ignore_index=True)
    out["regression_all_pairs"] = run_regressions(df_all)

    # Pearson corr within verbosity rewrites (where contamination concern lives),
    # within formality, and pooled
    def corr(df):
        if len(df) < 3:
            return {"r": None, "p": None, "n": int(len(df))}
        r, p = stats.pearsonr(df["delta_sentlen"], df["delta_fk"])
        return {"r": float(r), "p": float(p), "n": int(len(df))}

    out["correlation"] = {
        "delta_sentlen_vs_delta_fk": {
            "verbosity_passed": corr(verb_p),
            "formality_passed": corr(form_p),
            "pooled_passed": corr(df_passed),
        }
    }

    # Schema-matching aliases requested in task spec
    out["descriptive"] = out["descriptive_passed_only"]
    out["regression"] = out["regression_passed_only"]

    # Conclusion
    c1 = out["regression"]["model1_no_control"]["style_axis_coef"]
    p1 = out["regression"]["model1_no_control"]["style_axis_p"]
    c2 = out["regression"]["model2_length_controlled"]["style_axis_coef"]
    p2 = out["regression"]["model2_length_controlled"]["style_axis_p"]
    reduction = out["regression"]["coef_reduction_pct"]

    if p1 < 0.05 and (p2 >= 0.05 or abs(reduction) > 50):
        verdict = (
            f"FK cross-axis contamination IS explained by sentence-length changes: "
            f"the verbosity-vs-formality contrast in delta-FK shrinks from "
            f"beta={c1:.2f} (p={p1:.3g}) to beta={c2:.2f} (p={p2:.3g}) once delta "
            f"sentence length is controlled — a {reduction:.0f}% reduction."
        )
    else:
        verdict = (
            f"FK cross-axis contamination is NOT fully explained by sentence length: "
            f"the verbosity-vs-formality contrast moves from beta={c1:.2f} (p={p1:.3g}) "
            f"to beta={c2:.2f} (p={p2:.3g}) after controlling for delta sentence length "
            f"({reduction:.0f}% reduction)."
        )
    out["conclusion"] = verdict

    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
