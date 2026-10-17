"""GEE Model Diagnostics for all 6 judge × axis cells."""

import json
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.genmod.generalized_estimating_equations import GEE
from statsmodels.genmod.families import Binomial
from statsmodels.genmod.cov_struct import Exchangeable, Independence
from pathlib import Path

NLI_THRESHOLD = 0.90

CELLS = [
    {
        "judge": "GPT-4o",
        "axis": "Formality",
        "file": "pairwise_results_32b.jsonl",
        "pole_a": "formal",
        "pole_b": "casual",
        "orig_field": "original_formality",
        "pref_key": "prefers_formal",
    },
    {
        "judge": "GPT-4o",
        "axis": "Verbosity",
        "file": "pairwise_results_gpt4o_verbosity.jsonl",
        "pole_a": "verbose",
        "pole_b": "concise",
        "orig_field": "original_verbosity",
        "pref_key": "prefers_verbose",
    },
    {
        "judge": "GPT-4o",
        "axis": "Register",
        "file": "pairwise_results_gpt4o_register.jsonl",
        "pole_a": "academic",
        "pole_b": "conversational",
        "orig_field": "original_register",
        "pref_key": "prefers_academic",
    },
    {
        "judge": "Qwen3-32B",
        "axis": "Formality",
        "file": "pairwise_results_qwen32b_formality.jsonl",
        "pole_a": "formal",
        "pole_b": "casual",
        "orig_field": "original_formality",
        "pref_key": "prefers_formal",
    },
    {
        "judge": "Qwen3-32B",
        "axis": "Verbosity",
        "file": "pairwise_results_qwen32b_verbosity.jsonl",
        "pole_a": "verbose",
        "pole_b": "concise",
        "orig_field": "original_verbosity",
        "pref_key": "prefers_verbose",
    },
    {
        "judge": "Qwen3-32B",
        "axis": "Register",
        "file": "pairwise_results_qwen32b_register.jsonl",
        "pole_a": "academic",
        "pole_b": "conversational",
        "orig_field": "original_register",
        "pref_key": "prefers_academic",
    },
]


def load_gee_data(data_dir, cell):
    path = Path(data_dir) / cell["file"]
    records = [json.loads(l) for l in open(path)]
    records = [r for r in records if r["nli_cf"] >= NLI_THRESHOLD]

    pole_a = cell["pole_a"]
    pole_b = cell["pole_b"]
    orig_field = cell["orig_field"]

    rows = []
    for i, r in enumerate(records):
        pair_id = i
        orig = r[orig_field]

        # Trial 1: pole_a in position A
        is_style_in_A = 1.0
        is_original_in_A = 1.0 if orig == pole_a else 0.0
        chose_A = 1.0 if r["trial1_choice"] == "A" else 0.0
        rows.append({"pair_id": pair_id, "is_style_in_A": is_style_in_A,
                      "is_original_in_A": is_original_in_A, "chose_A": chose_A})

        # Trial 2: pole_b in position A
        is_style_in_A = 0.0
        is_original_in_A = 1.0 if orig == pole_b else 0.0
        chose_A = 1.0 if r["trial2_choice"] == "A" else 0.0
        rows.append({"pair_id": pair_id, "is_style_in_A": is_style_in_A,
                      "is_original_in_A": is_original_in_A, "chose_A": chose_A})

    return pd.DataFrame(rows)


def fit_gee(df, cov_struct):
    exog = sm.add_constant(df[["is_style_in_A", "is_original_in_A"]])
    model = GEE(df["chose_A"], exog, groups=df["pair_id"],
                family=Binomial(), cov_struct=cov_struct)
    return model.fit()


def fit_gee_interaction(df):
    df = df.copy()
    df["style_x_orig"] = df["is_style_in_A"] * df["is_original_in_A"]
    exog = sm.add_constant(df[["is_style_in_A", "is_original_in_A", "style_x_orig"]])
    model = GEE(df["chose_A"], exog, groups=df["pair_id"],
                family=Binomial(), cov_struct=Exchangeable())
    return model.fit()


def extract_or_ci(result, param_name):
    coef = result.params[param_name]
    se = result.bse[param_name]
    p = result.pvalues[param_name]
    or_val = np.exp(coef)
    ci_lo = np.exp(coef - 1.96 * se)
    ci_hi = np.exp(coef + 1.96 * se)
    return or_val, ci_lo, ci_hi, p


def main():
    data_dir = Path(__file__).resolve().parent.parent / "data"

    table_a_rows = []
    table_b_rows = []
    table_c_rows = []

    for cell in CELLS:
        df = load_gee_data(data_dir, cell)
        label = f"{cell['judge']} / {cell['axis']}"
        print(f"Fitting {label} (n_obs={len(df)}, n_pairs={df['pair_id'].nunique()}) ...")

        res_exch = fit_gee(df, Exchangeable())
        res_indep = fit_gee(df, Independence())

        # Correlation parameter
        alpha = res_exch.cov_struct.dep_params
        if hasattr(alpha, '__len__'):
            alpha = alpha[0]

        # QIC (scale=1.0 for Binomial family)
        qic_exch = res_exch.qic(scale=1.0)
        qic_indep = res_indep.qic(scale=1.0)
        delta_qic = qic_exch[0] - qic_indep[0]

        # Coefficient comparison: max absolute difference between structures
        coef_diff = np.max(np.abs(res_exch.params.values - res_indep.params.values))

        table_a_rows.append({
            "judge": cell["judge"], "axis": cell["axis"],
            "alpha": alpha,
            "qic_exch": qic_exch[0],
            "qic_indep": qic_indep[0],
            "delta_qic": delta_qic,
            "coef_diff": coef_diff,
        })

        # Coefficients from exchangeable
        style_or, style_lo, style_hi, style_p = extract_or_ci(res_exch, "is_style_in_A")
        orig_or, orig_lo, orig_hi, orig_p = extract_or_ci(res_exch, "is_original_in_A")

        table_b_rows.append({
            "judge": cell["judge"], "axis": cell["axis"],
            "style_or": style_or, "style_ci": (style_lo, style_hi), "style_p": style_p,
            "orig_or": orig_or, "orig_ci": (orig_lo, orig_hi), "orig_p": orig_p,
        })

        # Interaction test (formality only)
        if cell["axis"] == "Formality":
            res_int = fit_gee_interaction(df)
            main_style_or, _, _, _ = extract_or_ci(res_int, "is_style_in_A")
            main_orig_or, _, _, _ = extract_or_ci(res_int, "is_original_in_A")
            int_or, int_lo, int_hi, int_p = extract_or_ci(res_int, "style_x_orig")

            if int_p < 0.05:
                interp = "Significant interaction"
            else:
                interp = "No significant interaction"

            table_c_rows.append({
                "judge": cell["judge"],
                "main_style_or": main_style_or, "main_orig_or": main_orig_or,
                "int_or": int_or, "int_ci": (int_lo, int_hi),
                "int_p": int_p, "interp": interp,
            })

    # Print results
    print("\n" + "=" * 80)
    print("GEE MODEL DIAGNOSTICS — ALL 6 CELLS")
    print("=" * 80)

    # TABLE A
    print("\nTABLE A: Correlation Structure Comparison")
    print("-" * 95)
    header = f"{'Judge':<12} {'Axis':<12} {'alpha':>8} {'QIC(Exch)':>12} {'QIC(Indep)':>12} {'dQIC':>12} {'Max|dCoef|':>12}"
    print(header)
    print("-" * 95)
    for r in table_a_rows:
        print(f"{r['judge']:<12} {r['axis']:<12} {r['alpha']:>8.4f} {r['qic_exch']:>12.2f} {r['qic_indep']:>12.2f} {r['delta_qic']:>12.5f} {r['coef_diff']:>12.5f}")

    # TABLE B
    print(f"\nTABLE B: GEE Coefficients (Exchangeable)")
    print("-" * 130)
    header = f"{'Judge':<12} {'Axis':<12} {'Style OR':>10} {'Style 95% CI':>20} {'Style p':>12} {'Orig OR':>10} {'Orig 95% CI':>20} {'Orig p':>12}"
    print(header)
    print("-" * 130)
    for r in table_b_rows:
        sci = f"[{r['style_ci'][0]:.3f}, {r['style_ci'][1]:.3f}]"
        oci = f"[{r['orig_ci'][0]:.3f}, {r['orig_ci'][1]:.3f}]"
        sp = f"{r['style_p']:.4f}" if r['style_p'] >= 0.0001 else f"{r['style_p']:.2e}"
        op = f"{r['orig_p']:.4f}" if r['orig_p'] >= 0.0001 else f"{r['orig_p']:.2e}"
        print(f"{r['judge']:<12} {r['axis']:<12} {r['style_or']:>10.3f} {sci:>20} {sp:>12} {r['orig_or']:>10.3f} {oci:>20} {op:>12}")

    # TABLE C
    print(f"\nTABLE C: Interaction Test (Formality axis only)")
    print("-" * 120)
    header = f"{'Judge':<12} {'Main Style OR':>14} {'Main Orig OR':>14} {'Interact OR':>14} {'Interact 95% CI':>22} {'Interact p':>12} {'Interpretation':>25}"
    print(header)
    print("-" * 120)
    for r in table_c_rows:
        ici = f"[{r['int_ci'][0]:.3f}, {r['int_ci'][1]:.3f}]"
        ip = f"{r['int_p']:.4f}" if r['int_p'] >= 0.0001 else f"{r['int_p']:.2e}"
        print(f"{r['judge']:<12} {r['main_style_or']:>14.3f} {r['main_orig_or']:>14.3f} {r['int_or']:>14.3f} {ici:>22} {ip:>12} {r['interp']:>25}")

    print("\n" + "=" * 80)
    print("Notes:")
    print(f"  - NLI threshold: {NLI_THRESHOLD}")
    print("  - QIC: lower = better model fit")
    print("  - α: within-pair exchangeable correlation parameter")
    print("  - OR > 1 for style: judge prefers pole_a (formal / verbose / academic)")
    print("  - OR > 1 for originality: judge prefers whichever version is original")
    print("=" * 80)


if __name__ == "__main__":
    main()
