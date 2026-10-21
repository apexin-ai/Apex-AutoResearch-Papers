"""Qwen3-32B statistical analysis: BT + logistic decomposition (GEE).

Task 1: BT on formality + verbosity (pair-level bootstrap, 10000 resamples)
Task 2: GEE logistic decomposition on register
Task 3: GEE logistic decomposition on formality
"""

import json
import sys

import numpy as np
from scipy import stats

# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_records(path: str) -> list[dict]:
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def nli_filter(records: list[dict], threshold: float = 0.90) -> list[dict]:
    return [r for r in records if r.get("nli_cf", 0) >= threshold]


# ---------------------------------------------------------------------------
# Task 1: Bradley-Terry with pair-level bootstrap
# ---------------------------------------------------------------------------

AXIS_CONFIG = {
    "formality": {
        "poles": ("formal", "casual"),
        "field": "original_formality",
        "prefers_key": "trial{}_prefers_formal",
        "wins_key": "formal_wins",
    },
    "verbosity": {
        "poles": ("verbose", "concise"),
        "field": "original_verbosity",
        "prefers_key": "trial{}_prefers_verbose",
        "wins_key": "verbose_wins",
    },
    "register": {
        "poles": ("academic", "conversational"),
        "field": "original_register",
        "prefers_key": "trial{}_prefers_academic",
        "wins_key": "academic_wins",
    },
}


def build_bt_comparisons(records: list[dict], axis: str):
    """Build (winner, loser) tuples for choix. Item 0 = pole_a, item 1 = pole_b."""
    cfg = AXIS_CONFIG[axis]
    comparisons = []
    pair_groups = []  # list of lists, one per pair

    for rec in records:
        pair_comps = []
        for trial in [1, 2]:
            key = cfg["prefers_key"].format(trial)
            prefers_a = rec.get(key)
            if prefers_a is None:
                continue
            if prefers_a:
                pair_comps.append((0, 1))  # pole_a wins
            else:
                pair_comps.append((1, 0))  # pole_b wins
        if pair_comps:
            comparisons.extend(pair_comps)
            pair_groups.append(pair_comps)

    return comparisons, pair_groups


def bt_pair_bootstrap(records: list[dict], axis: str, n_bootstrap: int = 10000, seed: int = 42):
    import choix

    cfg = AXIS_CONFIG[axis]
    pole_a = cfg["poles"][0]

    comparisons, pair_groups = build_bt_comparisons(records, axis)
    n_pairs = len(pair_groups)
    n_comp = len(comparisons)

    # Point estimate
    params = choix.ilsr_pairwise(2, comparisons, alpha=0.01)
    p_a = np.exp(params[0]) / (np.exp(params[0]) + np.exp(params[1]))

    # Pair-level bootstrap
    rng = np.random.RandomState(seed)
    boot_p = []
    for _ in range(n_bootstrap):
        sampled_idx = rng.choice(n_pairs, size=n_pairs, replace=True)
        boot_comps = []
        for i in sampled_idx:
            boot_comps.extend(pair_groups[i])
        try:
            bp = choix.ilsr_pairwise(2, boot_comps, alpha=0.01)
            boot_p.append(np.exp(bp[0]) / (np.exp(bp[0]) + np.exp(bp[1])))
        except Exception:
            pass

    boot_p = np.array(boot_p)
    ci_lo = np.percentile(boot_p, 2.5)
    ci_hi = np.percentile(boot_p, 97.5)

    n_below = np.sum(boot_p < 0.5)
    if n_below == 0:
        p_str = "p < 0.0001"
        p_val = 1.0 / n_bootstrap  # for table
    else:
        p_val = n_below / len(boot_p)
        p_str = f"p = {p_val:.4f}"

    print(f"\n=== Qwen3-32B {axis} BT (pair-level bootstrap, {n_bootstrap} resamples) ===")
    print(f"NLI-filtered: {n_pairs} pairs, {n_comp} comparisons")
    print(f"BT P({pole_a} wins): {p_a:.4f}")
    print(f"95% CI: [{ci_lo:.4f}, {ci_hi:.4f}]")
    print(f"{p_str}")

    return {
        "axis": axis,
        "pole_a": pole_a,
        "n_pairs": n_pairs,
        "n_comp": n_comp,
        "p_a": p_a,
        "ci_lo": ci_lo,
        "ci_hi": ci_hi,
        "p_val": p_val,
        "p_str": p_str,
    }


# ---------------------------------------------------------------------------
# Tasks 2 & 3: GEE logistic decomposition
# ---------------------------------------------------------------------------

def build_trial_data(records: list[dict], axis: str):
    """Build observation-level data for logistic decomposition."""
    cfg = AXIS_CONFIG[axis]
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
        is_a_in_A = 1.0
        is_original_in_A = 1.0 if original_pole == pole_a else 0.0
        chose_A = 1.0 if rec["trial1_choice"] == "A" else 0.0
        X_rows.append([is_a_in_A, is_original_in_A])
        y_rows.append(chose_A)
        pair_ids.append(pair_idx)

        # Trial 2: A=pole_b, B=pole_a
        is_a_in_A = 0.0
        is_original_in_A = 1.0 if original_pole == pole_b else 0.0
        chose_A = 1.0 if rec["trial2_choice"] == "A" else 0.0
        X_rows.append([is_a_in_A, is_original_in_A])
        y_rows.append(chose_A)
        pair_ids.append(pair_idx)

        pair_idx += 1

    return (np.array(X_rows), np.array(y_rows), np.array(pair_ids), pole_a, pole_b)


def gee_decomposition(records: list[dict], axis: str):
    """GEE with exchangeable correlation + pair-level bootstrap."""
    import statsmodels.api as sm
    from statsmodels.genmod.generalized_estimating_equations import GEE
    from statsmodels.genmod.cov_struct import Exchangeable
    from statsmodels.genmod.families import Binomial
    from sklearn.linear_model import LogisticRegression
    import pandas as pd

    X, y, pair_ids, pole_a, pole_b = build_trial_data(records, axis)
    n_pairs = len(np.unique(pair_ids))

    print(f"\n{'='*70}")
    print(f"  GEE Decomposition — {axis} (Qwen3-32B)")
    print(f"{'='*70}")
    print(f"  Observations: {len(y)} (2 trials x {n_pairs} pairs)")

    # GEE fit
    df = pd.DataFrame({
        "chose_A": y,
        f"is_{pole_a}_in_A": X[:, 0],
        "is_original_in_A": X[:, 1],
        "pair_id": pair_ids,
    })
    exog = sm.add_constant(df[[f"is_{pole_a}_in_A", "is_original_in_A"]])
    model = GEE(
        df["chose_A"], exog, groups=df["pair_id"],
        family=Binomial(), cov_struct=Exchangeable(),
    )
    fit = model.fit()
    print(f"\n{fit.summary()}")

    # Pair-level bootstrap for robust CI (2000 resamples)
    n_boot = 2000
    rng = np.random.RandomState(42)
    unique_pairs = np.unique(pair_ids)
    boot_coefs = []
    for _ in range(n_boot):
        sampled = rng.choice(unique_pairs, size=len(unique_pairs), replace=True)
        idx = np.concatenate([np.where(pair_ids == p)[0] for p in sampled])
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

    results = {}
    param_names = [f"{pole_a}_effect", "originality_effect"]
    gee_names = [f"{pole_a}_effect", "originality_effect"]

    for i, name in enumerate(param_names):
        idx_gee = i + 1
        coef_gee = fit.params.iloc[idx_gee]
        se_gee = fit.bse.iloc[idx_gee]
        p_gee = fit.pvalues.iloc[idx_gee]
        ci_gee = fit.conf_int().iloc[idx_gee]
        or_gee = np.exp(coef_gee)
        or_ci_lo = np.exp(ci_gee.iloc[0])
        or_ci_hi = np.exp(ci_gee.iloc[1])

        # Bootstrap CI
        if len(boot_coefs) > 0:
            boot_or = np.exp(boot_coefs[:, i])
            boot_ci_lo = np.percentile(boot_or, 2.5)
            boot_ci_hi = np.percentile(boot_or, 97.5)
            boot_se = np.std(boot_coefs[:, i])
        else:
            boot_ci_lo = boot_ci_hi = boot_se = 0

        print(f"\n  {name}:")
        print(f"    GEE coef: {coef_gee:.4f} (SE={se_gee:.4f})")
        print(f"    GEE OR: {or_gee:.4f} [{or_ci_lo:.4f}, {or_ci_hi:.4f}]")
        print(f"    GEE p: {p_gee:.6f} {'***' if p_gee<0.001 else '**' if p_gee<0.01 else '*' if p_gee<0.05 else 'ns'}")
        print(f"    Bootstrap OR 95% CI: [{boot_ci_lo:.4f}, {boot_ci_hi:.4f}]")

        results[name] = {
            "or": or_gee,
            "or_ci": (or_ci_lo, or_ci_hi),
            "boot_or_ci": (boot_ci_lo, boot_ci_hi),
            "p": p_gee,
            "coef": coef_gee,
            "se": se_gee,
        }

    results["intercept"] = fit.params.iloc[0]
    results["n_pairs"] = n_pairs
    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    data_dir = "/root/causal_style_decomp_judge/data"

    # --- Task 1: BT on formality + verbosity ---
    print("=" * 70)
    print("  TASK 1: Bradley-Terry Analysis")
    print("=" * 70)

    bt_results = []
    for axis in ["formality", "verbosity"]:
        path = f"{data_dir}/pairwise_results_qwen32b_{axis}.jsonl"
        records = load_records(path)
        filtered = nli_filter(records, 0.90)
        print(f"\n[{axis}] Loaded {len(records)} pairs, NLI>=0.90: {len(filtered)}")
        r = bt_pair_bootstrap(filtered, axis, n_bootstrap=10000, seed=42)
        bt_results.append(r)

    # --- Task 2: GEE register ---
    print("\n\n" + "=" * 70)
    print("  TASK 2: GEE Logistic Decomposition — Register")
    print("=" * 70)

    path = f"{data_dir}/pairwise_results_qwen32b_register.jsonl"
    records = load_records(path)
    filtered = nli_filter(records, 0.90)
    print(f"\nLoaded {len(records)} pairs, NLI>=0.90: {len(filtered)}")
    gee_register = gee_decomposition(filtered, "register")

    # --- Task 3: GEE formality ---
    print("\n\n" + "=" * 70)
    print("  TASK 3: GEE Logistic Decomposition — Formality")
    print("=" * 70)

    path = f"{data_dir}/pairwise_results_qwen32b_formality.jsonl"
    records = load_records(path)
    filtered = nli_filter(records, 0.90)
    print(f"\nLoaded {len(records)} pairs, NLI>=0.90: {len(filtered)}")
    gee_formality = gee_decomposition(filtered, "formality")

    # --- Summary table ---
    print("\n\n" + "=" * 70)
    print("  SUMMARY")
    print("=" * 70)

    def fmt_p(p):
        if p < 0.0001:
            return "< 0.0001"
        return f"{p:.4f}"

    rows = []
    for r in bt_results:
        rows.append((
            f"BT {r['axis'].capitalize()}",
            f"P({r['pole_a']})",
            f"{r['p_a']:.4f}",
            f"[{r['ci_lo']:.4f}, {r['ci_hi']:.4f}]",
            fmt_p(r['p_val']),
        ))

    for label, gee_r in [("GEE Register", gee_register), ("GEE Formality", gee_formality)]:
        for effect_name in [k for k in gee_r if isinstance(gee_r[k], dict)]:
            e = gee_r[effect_name]
            short = effect_name.replace("_effect", "")
            rows.append((
                label,
                f"{short} OR",
                f"{e['or']:.4f}",
                f"[{e['or_ci'][0]:.4f}, {e['or_ci'][1]:.4f}]",
                fmt_p(e['p']),
            ))

    print(f"\n| {'Analysis':<18} | {'Metric':<16} | {'Value':<8} | {'95% CI':<20} | {'p':<10} |")
    print(f"|{'-'*20}|{'-'*18}|{'-'*10}|{'-'*22}|{'-'*12}|")
    for row in rows:
        print(f"| {row[0]:<18} | {row[1]:<16} | {row[2]:<8} | {row[3]:<20} | {row[4]:<10} |")

    print("\nDone.")


if __name__ == "__main__":
    main()
