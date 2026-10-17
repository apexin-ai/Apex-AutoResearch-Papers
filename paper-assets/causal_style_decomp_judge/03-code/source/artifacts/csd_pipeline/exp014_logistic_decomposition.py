"""exp-014: Logistic Regression for Original-Preference Decomposition.

Decomposes pairwise preference into formality effect + original preference
using logistic regression, replacing ad-hoc additive correction.

Two models: (A) sklearn LR + pair-level bootstrap CI, (B) GEE with
exchangeable correlation to properly handle within-pair dependence.

Also provides direction-asymmetry formal test on subsets.

Input:  pairwise results jsonl (with trial choices, original_formality)
Output: Console report + optional CSV
"""

import argparse
import csv
import json
import os

import numpy as np
from scipy import stats


def load_records(path: str) -> list[dict]:
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def direction_subset_analysis(records: list[dict], axis: str = "formality"):
    """Sign test on direction subsets — the core direction-asymmetry test."""
    axis_config = {
        "formality": {"poles": ("formal", "casual"), "field": "original_formality"},
        "verbosity": {"poles": ("verbose", "concise"), "field": "original_verbosity"},
    }
    cfg = axis_config[axis]
    pole_a, pole_b = cfg["poles"]
    field = cfg["field"]
    wins_key = f"{pole_a}_wins"

    consistent = [r for r in records if r.get("consistent") is True and r.get(wins_key) is not None]

    print(f"\n{'='*70}")
    print(f"  Direction-Asymmetry Analysis ({axis})")
    print(f"{'='*70}")
    print(f"  Consistent pairs: {len(consistent)}")

    results = []
    for direction in [pole_a, pole_b]:
        sub = [r for r in consistent if r.get(field) == direction]
        if len(sub) < 3:
            continue

        n = len(sub)
        a_wins = sum(1 for r in sub if r[wins_key] is True)
        b_wins = n - a_wins
        win_rate = a_wins / n

        sign_p = stats.binomtest(a_wins, n, 0.5).pvalue

        z = 1.96
        denom = 1 + z**2 / n
        center = (win_rate + z**2 / (2 * n)) / denom
        spread = z * (win_rate * (1 - win_rate) / n + z**2 / (4 * n**2))**0.5 / denom
        ci_lo, ci_hi = max(0, center - spread), min(1, center + spread)

        target = pole_b if direction == pole_a else pole_a
        label = f"{direction}→{target}"

        print(f"\n  --- {label} (n={n}) ---")
        print(f"  {pole_a} wins: {a_wins}/{n} ({win_rate*100:.1f}%)")
        print(f"  {pole_b} wins: {b_wins}/{n}")
        print(f"  95% CI (Wilson): [{ci_lo:.4f}, {ci_hi:.4f}]")
        print(f"  Sign test p: {sign_p:.6f}")
        print(f"  Significant: {'YES' if sign_p < 0.05 else 'NO'}")

        if direction == pole_a:
            print(f"  Interpretation: {pole_a}=original → {pole_a} win = prefer ORIGINAL")
            print(f"    Formality effect and original preference are CONFOUNDED (same direction)")
        else:
            print(f"  Interpretation: {pole_b}=original → {pole_a} win = prefer REWRITE")
            print(f"    Formality effect and original preference are OPPOSING")
            print(f"    This subset cleanly isolates formality effect from original preference")

        results.append({
            "direction": label,
            "n": n,
            f"{pole_a}_wins": a_wins,
            "win_rate": win_rate,
            "ci_lo": ci_lo,
            "ci_hi": ci_hi,
            "sign_p": sign_p,
        })

    return results


def _build_trial_data(records: list[dict], axis: str = "formality"):
    """Build observation-level data from pairwise records, tracking pair_id."""
    axis_config = {
        "formality": {"poles": ("formal", "casual"), "field": "original_formality"},
    }
    cfg = axis_config.get(axis)
    if not cfg:
        return None, None, None, None, None

    pole_a, pole_b = cfg["poles"]
    field = cfg["field"]

    X_rows, y_rows, pair_ids = [], [], []
    pair_idx = 0

    for rec in records:
        if not rec.get("trial1_choice") or not rec.get("trial2_choice"):
            continue
        original_pole = rec.get(field)
        if original_pole not in (pole_a, pole_b):
            continue

        # Trial 1: A=pole_a, B=pole_b
        is_formal_in_A = 1.0
        is_original_in_A = 1.0 if original_pole == pole_a else 0.0
        chose_A = 1.0 if rec["trial1_choice"] == "A" else 0.0
        X_rows.append([is_formal_in_A, is_original_in_A])
        y_rows.append(chose_A)
        pair_ids.append(pair_idx)

        # Trial 2: A=pole_b, B=pole_a
        is_formal_in_A = 0.0
        is_original_in_A = 1.0 if original_pole == pole_b else 0.0
        chose_A = 1.0 if rec["trial2_choice"] == "A" else 0.0
        X_rows.append([is_formal_in_A, is_original_in_A])
        y_rows.append(chose_A)
        pair_ids.append(pair_idx)

        pair_idx += 1

    return (np.array(X_rows), np.array(y_rows), np.array(pair_ids),
            pole_a, pole_b)


def logistic_decomposition(records: list[dict], axis: str = "formality"):
    """Logistic regression with pair-level bootstrap (fixes independence violation)."""
    from sklearn.linear_model import LogisticRegression

    result = _build_trial_data(records, axis)
    if result[0] is None:
        print(f"Logistic decomposition not configured for axis: {axis}")
        return None

    X, y, pair_ids, pole_a, pole_b = result
    n_pairs = len(np.unique(pair_ids))

    print(f"\n{'='*70}")
    print(f"  Logistic Regression — Pair-Level Bootstrap ({axis})")
    print(f"{'='*70}")
    print(f"  Observations: {len(y)} (2 trials × {n_pairs} pairs)")
    print(f"  DV: chose_position_A (1/0)")
    print(f"  IV1: is_{pole_a}_in_A (formality effect)")
    print(f"  IV2: is_original_in_A (original preference)")
    print(f"  Bootstrap unit: pair (not observation)")

    model = LogisticRegression(penalty=None, solver='lbfgs', max_iter=1000)
    model.fit(X, y)

    coefs = model.coef_[0]
    intercept = model.intercept_[0]

    # Pair-level bootstrap: resample pairs, keep both trials per pair
    n_boot = 2000
    rng = np.random.RandomState(42)
    unique_pairs = np.unique(pair_ids)
    boot_coefs = []
    for _ in range(n_boot):
        sampled_pairs = rng.choice(unique_pairs, size=len(unique_pairs), replace=True)
        idx = np.concatenate([np.where(pair_ids == p)[0] for p in sampled_pairs])
        X_b, y_b = X[idx], y[idx]
        if len(np.unique(y_b)) < 2:
            continue
        try:
            m = LogisticRegression(penalty=None, solver='lbfgs', max_iter=1000)
            m.fit(X_b, y_b)
            boot_coefs.append(m.coef_[0])
        except Exception:
            pass

    boot_coefs = np.array(boot_coefs)

    print(f"\n  Successful bootstrap iterations: {len(boot_coefs)}/{n_boot}")
    print(f"  Intercept (position A bias): {intercept:.4f}")

    results = {}
    for i, name in enumerate([f"{pole_a}_effect", "original_effect"]):
        coef = coefs[i]
        odds_ratio = np.exp(coef)
        if len(boot_coefs) > 0:
            ci_lo_coef = np.percentile(boot_coefs[:, i], 2.5)
            ci_hi_coef = np.percentile(boot_coefs[:, i], 97.5)
            se = np.std(boot_coefs[:, i])
            or_ci_lo = np.exp(ci_lo_coef)
            or_ci_hi = np.exp(ci_hi_coef)
        else:
            ci_lo_coef, ci_hi_coef, se = 0, 0, 0
            or_ci_lo, or_ci_hi = 0, 0
        z_val = coef / se if se > 0 else 0
        p_val = 2 * (1 - stats.norm.cdf(abs(z_val)))

        print(f"\n  {name}:")
        print(f"    Coefficient: {coef:.4f} (SE={se:.4f})")
        print(f"    Coef 95% CI (pair-bootstrap): [{ci_lo_coef:.4f}, {ci_hi_coef:.4f}]")
        print(f"    Odds ratio: {odds_ratio:.4f}")
        print(f"    OR 95% CI: [{or_ci_lo:.4f}, {or_ci_hi:.4f}]")
        print(f"    z={z_val:.4f}, p={p_val:.6f}")
        print(f"    Significant: {'YES' if p_val < 0.05 else 'NO'}")

        results[name] = {
            "coef": coef, "se": se, "or": odds_ratio,
            "coef_ci": (ci_lo_coef, ci_hi_coef),
            "or_ci": (or_ci_lo, or_ci_hi),
            "z": z_val, "p": p_val,
        }

    results["intercept"] = intercept
    results["n_pairs"] = n_pairs
    results["n_obs"] = len(y)
    results["method"] = "pair_bootstrap"
    return results


def gee_decomposition(records: list[dict], axis: str = "formality"):
    """GEE with exchangeable correlation — proper clustered inference."""
    import statsmodels.api as sm
    from statsmodels.genmod.generalized_estimating_equations import GEE
    from statsmodels.genmod.cov_struct import Exchangeable
    from statsmodels.genmod.families import Binomial
    import pandas as pd

    result = _build_trial_data(records, axis)
    if result[0] is None:
        print(f"GEE decomposition not configured for axis: {axis}")
        return None

    X, y, pair_ids, pole_a, pole_b = result
    n_pairs = len(np.unique(pair_ids))

    df = pd.DataFrame({
        "chose_A": y,
        f"is_{pole_a}_in_A": X[:, 0],
        "is_original_in_A": X[:, 1],
        "pair_id": pair_ids,
    })

    print(f"\n{'='*70}")
    print(f"  GEE Decomposition — Exchangeable Correlation ({axis})")
    print(f"{'='*70}")
    print(f"  Observations: {len(y)} (2 trials × {n_pairs} pairs)")
    print(f"  Clustering: pair_id (exchangeable correlation)")

    exog = sm.add_constant(df[[f"is_{pole_a}_in_A", "is_original_in_A"]])
    model = GEE(
        df["chose_A"], exog, groups=df["pair_id"],
        family=Binomial(), cov_struct=Exchangeable(),
    )
    fit = model.fit()

    print(f"\n{fit.summary()}")

    results = {}
    param_names = [f"{pole_a}_effect", "original_effect"]
    for i, name in enumerate(param_names):
        idx = i + 1  # skip const
        coef = fit.params.iloc[idx]
        se = fit.bse.iloc[idx]
        p_val = fit.pvalues.iloc[idx]
        ci = fit.conf_int().iloc[idx]
        odds_ratio = np.exp(coef)
        or_ci_lo = np.exp(ci.iloc[0])
        or_ci_hi = np.exp(ci.iloc[1])

        print(f"\n  {name} (GEE):")
        print(f"    Coefficient: {coef:.4f} (SE={se:.4f})")
        print(f"    Coef 95% CI: [{ci.iloc[0]:.4f}, {ci.iloc[1]:.4f}]")
        print(f"    Odds ratio: {odds_ratio:.4f}")
        print(f"    OR 95% CI: [{or_ci_lo:.4f}, {or_ci_hi:.4f}]")
        print(f"    p={p_val:.6f}")
        print(f"    Significant: {'YES' if p_val < 0.05 else 'NO'}")

        results[name] = {
            "coef": coef, "se": se, "or": odds_ratio,
            "coef_ci": (ci.iloc[0], ci.iloc[1]),
            "or_ci": (or_ci_lo, or_ci_hi),
            "p": p_val,
        }

    results["intercept"] = fit.params.iloc[0]
    results["n_pairs"] = n_pairs
    results["n_obs"] = len(y)
    results["method"] = "gee_exchangeable"
    results["correlation"] = fit.cov_struct.summary()
    return results


def _save_results_csv(dir_results, lr_results, gee_results, output_dir, axis):
    """Save all results to a single CSV for audit trail."""
    rows = []
    for dr in (dir_results or []):
        rows.append({"section": "direction_subset", **dr})
    for method_label, res in [("pair_bootstrap", lr_results), ("gee", gee_results)]:
        if not res:
            continue
        for name in [k for k in res if isinstance(res[k], dict)]:
            r = res[name]
            rows.append({
                "section": "logistic",
                "method": method_label,
                "effect": name,
                "coef": r["coef"],
                "se": r["se"],
                "or": r["or"],
                "or_ci_lo": r["or_ci"][0],
                "or_ci_hi": r["or_ci"][1],
                "p": r["p"],
            })
    if rows:
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, f"exp014_logistic_decomposition.csv")
        keys = set()
        for r in rows:
            keys.update(r.keys())
        keys = sorted(keys)
        with open(path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            for r in rows:
                w.writerow(r)
        print(f"\nSaved CSV to {path}")


def main():
    parser = argparse.ArgumentParser(description="exp-014: Logistic Decomposition")
    parser.add_argument("--pairwise-file", required=True)
    parser.add_argument("--axis", default="formality")
    parser.add_argument("--output-dir", default=None)
    args = parser.parse_args()

    records = load_records(args.pairwise_file)
    print(f"Loaded {len(records)} pairwise records")

    dir_results = direction_subset_analysis(records, axis=args.axis)

    lr_results = None
    try:
        lr_results = logistic_decomposition(records, axis=args.axis)
    except ImportError:
        print("\nsklearn not available — skipping logistic regression.")
        print("Install with: pip install scikit-learn")
    except Exception as e:
        print(f"\nLogistic regression (pair-bootstrap) failed: {e}")
        import traceback; traceback.print_exc()

    gee_results = None
    try:
        gee_results = gee_decomposition(records, axis=args.axis)
    except ImportError as e:
        print(f"\nstatsmodels not available — skipping GEE: {e}")
        print("Install with: pip install statsmodels")
    except Exception as e:
        print(f"\nGEE decomposition failed: {e}")
        import traceback; traceback.print_exc()

    # Comparison summary
    if lr_results and gee_results:
        print(f"\n{'='*70}")
        print(f"  Method Comparison: Pair-Bootstrap vs GEE")
        print(f"{'='*70}")
        for name in [k for k in lr_results if isinstance(lr_results[k], dict)]:
            lr = lr_results[name]
            gee = gee_results.get(name, {})
            if not gee:
                continue
            print(f"\n  {name}:")
            print(f"    Pair-bootstrap: OR={lr['or']:.4f} [{lr['or_ci'][0]:.4f}, {lr['or_ci'][1]:.4f}] p={lr['p']:.6f}")
            print(f"    GEE:            OR={gee['or']:.4f} [{gee['or_ci'][0]:.4f}, {gee['or_ci'][1]:.4f}] p={gee['p']:.6f}")

    if args.output_dir:
        _save_results_csv(dir_results, lr_results, gee_results, args.output_dir, args.axis)


if __name__ == "__main__":
    main()
