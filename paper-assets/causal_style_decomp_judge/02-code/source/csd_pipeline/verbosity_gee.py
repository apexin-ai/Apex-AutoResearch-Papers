"""Verbosity axis GEE logistic decomposition.

Decomposes judge preference into style effect (verbose vs concise)
and originality effect (original vs rewrite), confirming verbosity bias
is not an originality artifact.
"""

import json
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.genmod.generalized_estimating_equations import GEE
from statsmodels.genmod.cov_struct import Exchangeable
from statsmodels.genmod.families import Binomial
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "pairwise_results_qwen32b_verbosity.jsonl"
NLI_THRESHOLD = 0.90


def load_records():
    records = []
    with open(DATA_PATH) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def build_trial_data(records):
    X_rows, y_rows, pair_ids = [], [], []
    pair_idx = 0

    for rec in records:
        if not rec.get("trial1_choice") or not rec.get("trial2_choice"):
            continue
        original_pole = rec.get("original_verbosity")
        if original_pole not in ("verbose", "concise"):
            continue

        # Trial 1: A=verbose, B=concise
        is_verbose_in_A = 1.0
        is_original_in_A = 1.0 if original_pole == "verbose" else 0.0
        chose_A = 1.0 if rec["trial1_choice"] == "A" else 0.0
        X_rows.append([is_verbose_in_A, is_original_in_A])
        y_rows.append(chose_A)
        pair_ids.append(pair_idx)

        # Trial 2: A=concise, B=verbose
        is_verbose_in_A = 0.0
        is_original_in_A = 1.0 if original_pole == "concise" else 0.0
        chose_A = 1.0 if rec["trial2_choice"] == "A" else 0.0
        X_rows.append([is_verbose_in_A, is_original_in_A])
        y_rows.append(chose_A)
        pair_ids.append(pair_idx)

        pair_idx += 1

    return np.array(X_rows), np.array(y_rows), np.array(pair_ids)


def main():
    records = load_records()
    print(f"Total records loaded: {len(records)}")

    filtered = [r for r in records if r.get("nli_cf", 0) >= NLI_THRESHOLD]
    print(f"After NLI filter (>= {NLI_THRESHOLD}): {len(filtered)}")

    X, y, pair_ids = build_trial_data(filtered)
    n_pairs = len(np.unique(pair_ids))
    print(f"Observations: {len(y)} (2 trials x {n_pairs} pairs)")

    df = pd.DataFrame({
        "chose_A": y,
        "is_verbose_in_A": X[:, 0],
        "is_original_in_A": X[:, 1],
        "pair_id": pair_ids,
    })

    exog = sm.add_constant(df[["is_verbose_in_A", "is_original_in_A"]])
    model = GEE(
        df["chose_A"], exog, groups=df["pair_id"],
        family=Binomial(), cov_struct=Exchangeable(),
    )
    fit = model.fit()

    print(f"\n{'='*60}")
    print("  GEE Logistic Decomposition — Verbosity (Qwen3-32B)")
    print(f"{'='*60}")

    for i, name in enumerate(["verbose_effect", "originality_effect"]):
        idx = i + 1
        coef = fit.params.iloc[idx]
        se = fit.bse.iloc[idx]
        p = fit.pvalues.iloc[idx]
        ci = fit.conf_int().iloc[idx]
        or_val = np.exp(coef)
        or_lo = np.exp(ci.iloc[0])
        or_hi = np.exp(ci.iloc[1])

        sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
        print(f"\n  {name}:")
        print(f"    Coef = {coef:.4f} (SE = {se:.4f})")
        print(f"    OR = {or_val:.4f}  95% CI [{or_lo:.4f}, {or_hi:.4f}]")
        print(f"    p = {p:.2e}  {sig}")

    print(f"\n  Intercept: {fit.params.iloc[0]:.4f}")
    print(f"  Exchangeable corr: {fit.cov_struct.summary()}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
