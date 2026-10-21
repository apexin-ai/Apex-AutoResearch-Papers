#!/usr/bin/env python3
"""Sign-reversal determinants on the 23 empirical LLM confusion matrices.

For each CM:
  * extract simple matrix features
  * compute exposure-topology sign-reversal under default beta and several alt betas
  * search for a simple decision rule that separates flip / no-flip groups
"""

import json
import sys
import itertools
import numpy as np
from pathlib import Path
from collections import defaultdict

PROJ = Path("/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib")
sys.path.insert(0, str(PROJ))

import importlib.util
spec = importlib.util.spec_from_file_location(
    "plan_006", str(PROJ / "plan_006_asv_empirical.py"))
plan_006 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plan_006)

EMPIRICAL_FILE = PROJ / "artifacts/updated_empirical_results.json"
OUT_FILE = PROJ / "artifacts/sign_reversal_determinants_results.json"


# ----------------------------------------------------------------------
# Matrix features
# ----------------------------------------------------------------------

def matrix_features(C):
    """Compute scalar features of a column-stochastic K x K confusion matrix."""
    K = C.shape[0]
    diag = np.diag(C)
    off = C - np.diag(diag)

    min_diag = float(np.min(diag))
    mean_diag = float(np.mean(diag))

    # max off-diagonal element across the matrix
    max_off = float(off.max())
    # max ratio of off-diagonal element to the diagonal of its column
    safe_diag = np.where(diag > 1e-12, diag, np.nan)
    # off[i,j] / diag[j]
    ratio = off / safe_diag[None, :]
    max_off_ratio = float(np.nanmax(ratio))

    # condition number
    try:
        cond = float(np.linalg.cond(C))
    except np.linalg.LinAlgError:
        cond = float("inf")
    if not np.isfinite(cond):
        cond = 1e12

    # per-column entropy (normalized to [0,1])
    H = []
    log_K = np.log(K) if K > 1 else 1.0
    for j in range(K):
        col = C[:, j]
        col = col / col.sum() if col.sum() > 0 else col
        col = np.clip(col, 1e-12, 1.0)
        H.append(-(col * np.log(col)).sum() / log_K)
    mean_entropy = float(np.mean(H))
    max_entropy = float(np.max(H))

    # spectral gap of |eigenvalues|
    eigvals = np.linalg.eigvals(C)
    abs_eig = np.sort(np.abs(eigvals))[::-1]
    if len(abs_eig) >= 2:
        spectral_gap = float(abs_eig[0] - abs_eig[1])
    else:
        spectral_gap = float(abs_eig[0])

    # determinant (sign and magnitude indicator)
    det = float(np.linalg.det(C))

    # minimum singular value (closer to 0 => closer to singular)
    sv = np.linalg.svd(C, compute_uv=False)
    min_sv = float(sv.min())
    sv_ratio = float(sv.max() / sv.min()) if sv.min() > 0 else float("inf")
    if not np.isfinite(sv_ratio):
        sv_ratio = 1e12

    return {
        "K": K,
        "min_diag": min_diag,
        "mean_diag": mean_diag,
        "max_off": max_off,
        "max_off_ratio": max_off_ratio,
        "cond": cond,
        "log_cond": float(np.log10(max(cond, 1.0))),
        "mean_entropy": mean_entropy,
        "max_entropy": max_entropy,
        "spectral_gap": spectral_gap,
        "det": det,
        "min_sv": min_sv,
        "sv_ratio": sv_ratio,
    }


# ----------------------------------------------------------------------
# Exposure sign-reversal evaluation
# ----------------------------------------------------------------------

def exposure_outcome(C, beta, p_A=None, seed=42):
    """Run the exposure DGP with custom beta and return sign-flip details."""
    K = C.shape[0]
    if p_A is None:
        p_A = plan_006.make_p_A(K)
    params = {"beta": np.asarray(beta, dtype=float), "p_A": p_A}
    st = plan_006.precompute_suff_stats(K, "exposure", params, seed=seed)
    plim_true = plan_006.compute_plim(np.eye(K), st, K)
    plim_biased = plan_006.compute_plim(C, st, K)

    if not isinstance(plim_biased, np.ndarray):
        return {
            "any_flip": None,
            "per_coef": None,
            "max_relbias": float("inf"),
            "tau_true": None,
            "tau_hat": None,
        }

    per = []
    any_flip = False
    max_relbias = 0.0
    for i in range(1, K):
        tv = float(plim_true[i])
        bv = float(plim_biased[i])
        sf = bool(np.sign(bv) != np.sign(tv)) if abs(tv) > 1e-10 else False
        rel = abs(bv - tv) / max(abs(tv), 1e-10)
        max_relbias = max(max_relbias, rel)
        if sf:
            any_flip = True
        per.append({"coef_idx": i, "true": tv, "biased": bv, "sign_flip": sf})

    return {
        "any_flip": any_flip,
        "per_coef": per,
        "max_relbias": float(max_relbias),
        "tau_true": float(plim_true[1]),
        "tau_hat": float(plim_biased[1]),
    }


# ----------------------------------------------------------------------
# Beta configurations
# ----------------------------------------------------------------------

DEFAULT_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]


def beta_default(K):
    return DEFAULT_POOL[:K]


def beta_uniform_pos(K):
    return [0.0] + [1.0] * (K - 1)


def beta_alt_signs(K):
    """Alternating signs of magnitude 1.0 starting positive at index 1."""
    v = [0.0]
    for j in range(K - 1):
        v.append(1.0 if j % 2 == 0 else -1.0)
    return v


def beta_only_first(K):
    """Only coefficient at index 1 is nonzero."""
    v = [0.0] * K
    if K >= 2:
        v[1] = 1.0
    return v


def beta_small(K):
    """Default vector scaled by 0.3 (smaller effect sizes — sign flips easier)."""
    return [0.3 * x for x in DEFAULT_POOL[:K]]


def beta_large(K):
    """Default vector scaled by 3.0 (larger effect sizes — flips harder)."""
    return [3.0 * x for x in DEFAULT_POOL[:K]]


BETA_CONFIGS = {
    "default": beta_default,
    "uniform_pos": beta_uniform_pos,
    "alt_signs": beta_alt_signs,
    "only_first": beta_only_first,
    "scale_0p3": beta_small,
    "scale_3p0": beta_large,
}


# ----------------------------------------------------------------------
# Simple rule search
# ----------------------------------------------------------------------

def evaluate_rule(rows, feat_a, op_a, thr_a, feat_b=None, op_b=None, thr_b=None,
                  combine="AND"):
    def predict(row):
        fa = row["features"][feat_a]
        ok_a = (fa < thr_a) if op_a == "<" else (fa > thr_a)
        if feat_b is None:
            return ok_a
        fb = row["features"][feat_b]
        ok_b = (fb < thr_b) if op_b == "<" else (fb > thr_b)
        return (ok_a and ok_b) if combine == "AND" else (ok_a or ok_b)

    tp = fp = tn = fn = 0
    for r in rows:
        truth = r["sign_flip"]
        pred = predict(r)
        if pred and truth:
            tp += 1
        elif pred and not truth:
            fp += 1
        elif (not pred) and truth:
            fn += 1
        else:
            tn += 1
    n = tp + fp + tn + fn
    acc = (tp + tn) / n if n else 0.0
    sens = tp / (tp + fn) if (tp + fn) else 0.0
    spec = tn / (tn + fp) if (tn + fp) else 0.0
    return {
        "tp": tp, "fp": fp, "tn": tn, "fn": fn,
        "accuracy": acc, "sensitivity": sens, "specificity": spec,
    }


def search_simple_rules(rows, features):
    """Brute-force search over single-feature thresholds and 2-feature AND."""
    # quantile thresholds per feature
    candidates = {}
    for f in features:
        vals = sorted({row["features"][f] for row in rows})
        # midpoints between sorted unique values
        thrs = []
        for i in range(len(vals) - 1):
            thrs.append(0.5 * (vals[i] + vals[i + 1]))
        candidates[f] = thrs

    # single-feature rules
    best_single = None
    for f in features:
        for thr in candidates[f]:
            for op in ("<", ">"):
                m = evaluate_rule(rows, f, op, thr)
                key = (m["accuracy"], m["sensitivity"] + m["specificity"])
                if best_single is None or key > best_single["key"]:
                    best_single = {
                        "rule": f"{f} {op} {thr:.4f} -> sign_flip",
                        "feature": f, "op": op, "thr": thr,
                        "metrics": m, "key": key,
                    }

    # AND-of-2 rules
    best_and = None
    for fa, fb in itertools.combinations(features, 2):
        for ta in candidates[fa]:
            for oa in ("<", ">"):
                for tb in candidates[fb]:
                    for ob in ("<", ">"):
                        m = evaluate_rule(rows, fa, oa, ta, fb, ob, tb, "AND")
                        key = (m["accuracy"], m["sensitivity"] + m["specificity"])
                        if best_and is None or key > best_and["key"]:
                            best_and = {
                                "rule": (f"({fa} {oa} {ta:.4f}) AND "
                                         f"({fb} {ob} {tb:.4f}) -> sign_flip"),
                                "feat_a": fa, "op_a": oa, "thr_a": ta,
                                "feat_b": fb, "op_b": ob, "thr_b": tb,
                                "metrics": m, "key": key,
                            }
    for d in (best_single, best_and):
        if d is not None:
            d.pop("key", None)
    return best_single, best_and


# ----------------------------------------------------------------------
# Descriptive comparisons
# ----------------------------------------------------------------------

def group_compare(rows, features):
    flip = [r for r in rows if r["sign_flip"]]
    no_flip = [r for r in rows if not r["sign_flip"]]
    out = {}
    for f in features:
        vf = np.array([r["features"][f] for r in flip], dtype=float)
        vn = np.array([r["features"][f] for r in no_flip], dtype=float)
        out[f] = {
            "n_flip": int(vf.size),
            "n_no_flip": int(vn.size),
            "mean_flip": float(np.nanmean(vf)) if vf.size else None,
            "mean_no_flip": float(np.nanmean(vn)) if vn.size else None,
            "median_flip": float(np.nanmedian(vf)) if vf.size else None,
            "median_no_flip": float(np.nanmedian(vn)) if vn.size else None,
            "min_flip": float(np.nanmin(vf)) if vf.size else None,
            "min_no_flip": float(np.nanmin(vn)) if vn.size else None,
            "max_flip": float(np.nanmax(vf)) if vf.size else None,
            "max_no_flip": float(np.nanmax(vn)) if vn.size else None,
        }
    return out


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def main():
    with open(EMPIRICAL_FILE) as f:
        emp = json.load(f)
    cms = {k: np.array(v) for k, v in emp["confusion_matrices"].items()}
    print(f"Loaded {len(cms)} confusion matrices")

    # 1. features for each matrix
    feat_table = {}
    for name, C in cms.items():
        feat_table[name] = matrix_features(C)

    # 2. exposure outcomes per beta config
    per_beta_results = {}
    for beta_name, beta_fn in BETA_CONFIGS.items():
        rows = []
        for name, C in cms.items():
            K = C.shape[0]
            beta = beta_fn(K)
            res = exposure_outcome(C, beta)
            row = {
                "config": name,
                "K": K,
                "beta": beta,
                "sign_flip": bool(res["any_flip"]) if res["any_flip"] is not None else False,
                "tau_true": res["tau_true"],
                "tau_hat": res["tau_hat"],
                "max_relbias": res["max_relbias"],
                "per_coef": res["per_coef"],
                "features": feat_table[name],
            }
            rows.append(row)
        n_flip = sum(1 for r in rows if r["sign_flip"])
        per_beta_results[beta_name] = {
            "beta_label": beta_name,
            "n_total": len(rows),
            "n_flip": n_flip,
            "rows": rows,
        }
        print(f"  beta={beta_name}: {n_flip}/{len(rows)} sign_flips")

    # 3. descriptive analysis under default beta
    feature_names = [
        "min_diag", "mean_diag", "max_off", "max_off_ratio",
        "log_cond", "mean_entropy", "max_entropy",
        "spectral_gap", "det", "min_sv",
    ]
    default_rows = per_beta_results["default"]["rows"]
    group_stats = group_compare(default_rows, feature_names)

    # 4. simple-rule search (default beta)
    best_single, best_and = search_simple_rules(default_rows, feature_names)

    # 5. robustness: best single-feature rule under default re-evaluated on
    #    every other beta configuration
    robustness = {}
    if best_single is not None:
        for beta_name, payload in per_beta_results.items():
            m = evaluate_rule(
                payload["rows"],
                best_single["feature"], best_single["op"], best_single["thr"])
            robustness[beta_name] = m

    # 6. K-stratified
    by_K = defaultdict(list)
    for r in default_rows:
        by_K[r["K"]].append(r)
    k_stratified = {}
    for K, rs in by_K.items():
        n_flip = sum(1 for r in rs if r["sign_flip"])
        k_stratified[str(K)] = {
            "n": len(rs),
            "n_flip": n_flip,
            "configs": [r["config"] for r in rs],
            "flips": [r["config"] for r in rs if r["sign_flip"]],
        }

    # ------------------------------------------------------------------
    # write JSON
    # ------------------------------------------------------------------
    out = {
        "n_matrices": len(cms),
        "beta_configs_tested": list(BETA_CONFIGS.keys()),
        "feature_names": feature_names,
        "features_per_config": feat_table,
        "per_beta_results": per_beta_results,
        "default_beta_descriptive": {
            "group_compare": group_stats,
            "best_single_rule": best_single,
            "best_AND_rule": best_and,
            "k_stratified": k_stratified,
        },
        "rule_robustness_across_betas": robustness,
    }
    with open(OUT_FILE, "w") as f:
        json.dump(out, f, indent=2, default=float)
    print(f"\nWrote {OUT_FILE}")
    print(f"Best single rule (default beta): {best_single['rule'] if best_single else None}")
    if best_single:
        print(f"  metrics: {best_single['metrics']}")
    print(f"Best AND rule (default beta): {best_and['rule'] if best_and else None}")
    if best_and:
        print(f"  metrics: {best_and['metrics']}")
    print("Rule robustness across betas:")
    for k, v in robustness.items():
        print(f"  {k}: acc={v['accuracy']:.3f} sens={v['sensitivity']:.3f} spec={v['specificity']:.3f}")


if __name__ == "__main__":
    main()
