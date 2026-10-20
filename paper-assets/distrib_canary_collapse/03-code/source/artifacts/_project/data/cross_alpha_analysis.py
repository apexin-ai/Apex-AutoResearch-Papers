"""Cross-alpha analysis for distributional canary collapse experiments.

Scans results/alpha_sweep/a*_s42/ directories, computes:
  1. Dose-response table (gen0→genN drift% per metric per α)
  2. Bidirectional permutation Granger causality with BH FDR correction
  3. Cross-correlation lead-lag analysis (Δmetric pairs)
  4. Per-generation velocity analysis for distinct_1

Input:  results/alpha_sweep/a{NNN}_s42/all_metrics.json
Output: results/analysis/cross_alpha_v{VERSION}.json + terminal summary

Dependencies: numpy, scipy, pandas, statsmodels
"""

import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime

import numpy as np
from statsmodels.stats.multitest import multipletests


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SWEEP_DIR = os.path.join(BASE_DIR, "results", "alpha_sweep")
ANALYSIS_DIR = os.path.join(BASE_DIR, "results", "analysis")

METRICS = ["distinct_1", "distinct_2", "distinct_3", "token_entropy", "ece", "perplexity"]

# Granger test pairs: (cause, effect, label)
GRANGER_PAIRS = [
    ("token_entropy", "distinct_1", "entropy→d1"),
    ("ece",           "distinct_1", "ECE→d1"),
    ("token_entropy", "distinct_2", "entropy→d2"),
    ("ece",           "distinct_2", "ECE→d2"),
    ("distinct_1", "token_entropy", "d1→entropy"),
    ("distinct_1", "ece",           "d1→ECE"),
    ("distinct_2", "token_entropy", "d2→entropy"),
    ("distinct_2", "ece",           "d2→ECE"),
]

XCORR_PAIRS = [
    ("token_entropy", "distinct_1", "entropy_vs_d1"),
    ("ece",           "distinct_1", "ece_vs_d1"),
]


def discover_alpha_dirs(explicit=None):
    """Find alpha experiment directories. Returns sorted list of (alpha_key, alpha_float, path)."""
    if explicit:
        dirs = []
        for name in explicit:
            path = os.path.join(SWEEP_DIR, name)
            if not os.path.isdir(path):
                print(f"WARNING: {path} not found, skipping", file=sys.stderr)
                continue
            m = re.match(r"a(\d{3})_s\d+", name)
            if m:
                alpha_val = int(m.group(1)) / 100.0
                dirs.append((name.split("_")[0], alpha_val, path))
        return sorted(dirs, key=lambda x: x[1])

    pattern = os.path.join(SWEEP_DIR, "a*_s42")
    found = sorted(glob.glob(pattern))
    dirs = []
    for path in found:
        name = os.path.basename(path)
        m = re.match(r"a(\d{3})_s42", name)
        if m:
            alpha_val = int(m.group(1)) / 100.0
            dirs.append((f"a{m.group(1)}", alpha_val, path))
    return dirs


def load_metrics(alpha_dir):
    """Load all_metrics.json from an alpha directory. Returns list of dicts sorted by generation."""
    path = os.path.join(alpha_dir, "all_metrics.json")
    with open(path) as f:
        data = json.load(f)
    return sorted(data, key=lambda x: x["generation"])


def extract_series(metrics_list, key):
    """Extract a metric as numpy array ordered by generation."""
    return np.array([m[key] for m in metrics_list], dtype=float)


# ---------------------------------------------------------------------------
# 1. Dose-response
# ---------------------------------------------------------------------------

def compute_dose_response(all_data):
    """Compute gen0→genN drift% for each metric at each α."""
    result = {}
    for alpha_key, alpha_val, metrics_list in all_data:
        entry = {"alpha": alpha_val}
        for metric in METRICS:
            vals = extract_series(metrics_list, metric)
            gen0, genN = vals[0], vals[-1]
            drift_pct = round((genN - gen0) / abs(gen0) * 100, 2) if abs(gen0) > 1e-12 else 0.0
            entry[metric] = {
                "gen0": round(float(gen0), 6),
                f"gen{len(vals)-1}": round(float(genN), 6),
                "drift_pct": drift_pct,
            }
        result[alpha_key] = entry
    return result


# ---------------------------------------------------------------------------
# 2. Permutation Granger causality (reused from permutation_granger.py)
# ---------------------------------------------------------------------------

def _build_lag_matrix(y, x, max_lag):
    T = len(y)
    n = T - max_lag
    Y = y[max_lag:]
    cols_r = [np.ones(n)]
    for lag in range(1, max_lag + 1):
        cols_r.append(y[max_lag - lag: T - lag])
    cols_u = list(cols_r)
    for lag in range(1, max_lag + 1):
        cols_u.append(x[max_lag - lag: T - lag])
    return Y, np.column_stack(cols_r), np.column_stack(cols_u)


def _granger_f_stat(y, x, max_lag):
    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)
    n = len(Y)
    q = max_lag
    try:
        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]
        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]
    except np.linalg.LinAlgError:
        return np.nan
    rss_r = np.sum((Y - X_r @ beta_r) ** 2)
    rss_u = np.sum((Y - X_u @ beta_u) ** 2)
    k_u = X_u.shape[1]
    df_resid = n - k_u
    if df_resid <= 0 or rss_u < 1e-15:
        return np.nan
    return ((rss_r - rss_u) / q) / (rss_u / df_resid)


def permutation_granger_test(x, y, max_lag=1, n_perm=5000, seed=42, difference=True):
    """Permutation-based Granger causality: does x Granger-cause y?"""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if difference:
        x, y = np.diff(x), np.diff(y)
    T = len(x)
    if T <= max_lag + 2:
        return {"f_stat": None, "p_raw": None, "note": f"Series too short: T={T}"}

    f_obs = _granger_f_stat(y, x, max_lag)
    if np.isnan(f_obs):
        return {"f_stat": None, "p_raw": None, "note": "F-stat computation failed"}

    # Effect size f²
    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)
    rss_r = np.sum((Y - X_r @ np.linalg.lstsq(X_r, Y, rcond=None)[0]) ** 2)
    rss_u = np.sum((Y - X_u @ np.linalg.lstsq(X_u, Y, rcond=None)[0]) ** 2)
    f2 = (rss_r - rss_u) / rss_u if rss_u > 1e-15 else None

    rng = np.random.default_rng(seed)
    null_f = np.empty(n_perm)
    for i in range(n_perm):
        null_f[i] = _granger_f_stat(y, rng.permutation(x), max_lag)
    valid = null_f[~np.isnan(null_f)]
    if len(valid) == 0:
        return {"f_stat": round(float(f_obs), 4), "p_raw": None, "note": "All permutations failed"}

    p_value = (np.sum(valid >= f_obs) + 1) / (len(valid) + 1)
    return {
        "f_stat": round(float(f_obs), 4),
        "p_raw": round(float(p_value), 6),
        "n_perm": n_perm,
        "effect_size_f2": round(float(f2), 4) if f2 is not None else None,
    }


def run_granger_all(all_data, max_lag=1, n_perms=5000):
    """Run bidirectional Granger for all α × all pairs. Returns list of result dicts."""
    results = []
    for alpha_key, alpha_val, metrics_list in all_data:
        for cause_key, effect_key, label in GRANGER_PAIRS:
            x = extract_series(metrics_list, cause_key)
            y = extract_series(metrics_list, effect_key)
            res = permutation_granger_test(x, y, max_lag=max_lag, n_perm=n_perms)
            res.update({
                "alpha": alpha_val,
                "alpha_key": alpha_key,
                "direction": label,
                "cause": cause_key,
                "effect": effect_key,
            })
            results.append(res)
    return results


def apply_fdr(granger_results):
    """Apply BH FDR correction across all tests with valid p-values."""
    valid_idx = [i for i, r in enumerate(granger_results) if r.get("p_raw") is not None]
    if not valid_idx:
        return granger_results

    raw_ps = [granger_results[i]["p_raw"] for i in valid_idx]
    _, fdr_ps, _, _ = multipletests(raw_ps, method="fdr_bh")

    for j, idx in enumerate(valid_idx):
        granger_results[idx]["p_fdr"] = round(float(fdr_ps[j]), 6)

    # Annotate α=0.00 false-positive warning
    for r in granger_results:
        if r.get("alpha", -1) == 0.0 and r.get("p_raw") is not None and r["p_raw"] < 0.05:
            r["note"] = "consistent with FPR, likely false positive"

    return granger_results


# ---------------------------------------------------------------------------
# 3. Cross-correlation lead-lag
# ---------------------------------------------------------------------------

def cross_correlation(all_data, max_lag=3):
    """Compute Δmetric cross-correlations at various lags."""
    result = {}
    for alpha_key, alpha_val, metrics_list in all_data:
        entry = {"alpha": alpha_val}
        for cause_key, effect_key, pair_label in XCORR_PAIRS:
            dx = np.diff(extract_series(metrics_list, cause_key))
            dy = np.diff(extract_series(metrics_list, effect_key))
            lags = {}
            best_lag, best_r = 0, 0.0
            for lag in range(-max_lag, max_lag + 1):
                if lag >= 0:
                    a, b = dx[:len(dx) - lag] if lag > 0 else dx, dy[lag:] if lag > 0 else dy
                else:
                    a, b = dx[-lag:], dy[:len(dy) + lag]
                n = min(len(a), len(b))
                if n < 3:
                    continue
                a, b = a[:n], b[:n]
                std_a, std_b = np.std(a, ddof=1), np.std(b, ddof=1)
                if std_a < 1e-15 or std_b < 1e-15:
                    r = 0.0
                else:
                    r = float(np.corrcoef(a, b)[0, 1])
                lags[str(lag)] = round(r, 4)
                if abs(r) > abs(best_r):
                    best_lag, best_r = lag, r
            entry[pair_label] = {
                "peak_lag": best_lag,
                "peak_r": round(best_r, 4),
                "lags": lags,
            }
        result[alpha_key] = entry
    return result


# ---------------------------------------------------------------------------
# 4. Per-gen velocity
# ---------------------------------------------------------------------------

def per_gen_velocity(all_data):
    """Compute d1 per-generation deltas, early vs late comparison."""
    result = {}
    for alpha_key, alpha_val, metrics_list in all_data:
        vals = extract_series(metrics_list, "distinct_1")
        deltas = np.diff(vals)
        n = len(deltas)
        mid = n // 2
        early_mean = float(np.mean(deltas[:mid])) if mid > 0 else None
        late_mean = float(np.mean(deltas[mid:])) if mid < n else None
        max_drop_idx = int(np.argmin(deltas))
        result[alpha_key] = {
            "alpha": alpha_val,
            "d1_values": [round(float(v), 6) for v in vals],
            "d1_deltas": [round(float(d), 6) for d in deltas],
            "cumulative_drift_pct": round((vals[-1] - vals[0]) / abs(vals[0]) * 100, 2),
            "mean_velocity": round(float(np.mean(deltas)), 6),
            "max_drop_gen": max_drop_idx,
            "max_drop_value": round(float(deltas[max_drop_idx]), 6),
            "early_mean_velocity": round(early_mean, 6) if early_mean is not None else None,
            "late_mean_velocity": round(late_mean, 6) if late_mean is not None else None,
            "deceleration_ratio": round(late_mean / early_mean, 4) if early_mean and abs(early_mean) > 1e-12 else None,
        }
    return result


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def auto_version():
    """Find next version number by scanning existing analysis files."""
    os.makedirs(ANALYSIS_DIR, exist_ok=True)
    existing = glob.glob(os.path.join(ANALYSIS_DIR, "cross_alpha_v*.json"))
    max_v = 0
    for f in existing:
        m = re.search(r"cross_alpha_v(\d+)", f)
        if m:
            max_v = max(max_v, int(m.group(1)))
    return max_v + 1


def print_summary(output):
    """Print terminal summary tables."""
    print("\n" + "=" * 80)
    print("CROSS-ALPHA ANALYSIS SUMMARY")
    print("=" * 80)

    # Dose-response table
    dr = output["dose_response"]
    alphas = sorted(dr.keys())
    print(f"\n{'DOSE-RESPONSE (drift %)'}")
    print("-" * 80)
    header = f"{'Metric':<16}"
    for ak in alphas:
        header += f" | α={dr[ak]['alpha']:<5}"
    print(header)
    print("-" * 80)
    for metric in METRICS:
        line = f"{metric:<16}"
        for ak in alphas:
            d = dr[ak][metric]["drift_pct"]
            line += f" | {d:>+7.1f}%"
        print(line)

    # Granger table
    gc = output["granger_causality"]
    print(f"\n{'GRANGER CAUSALITY (bidirectional, differenced, permutation)'}")
    print("-" * 80)
    header = f"{'Direction':<20}"
    alpha_keys = sorted(set(r["alpha_key"] for r in gc))
    for ak in alpha_keys:
        header += f" | α={[r for r in gc if r['alpha_key']==ak][0]['alpha']:<4} p_raw   p_fdr"
    print(header)
    print("-" * 80)

    directions = list(dict.fromkeys(r["direction"] for r in gc))
    for d in directions:
        line = f"{d:<20}"
        for ak in alpha_keys:
            match = [r for r in gc if r["alpha_key"] == ak and r["direction"] == d]
            if match:
                r = match[0]
                p_raw = f"{r['p_raw']:.4f}" if r.get("p_raw") is not None else "  N/A "
                p_fdr = f"{r.get('p_fdr', 'N/A')}" if r.get("p_fdr") is not None else "  N/A "
                if isinstance(p_fdr, float):
                    p_fdr = f"{p_fdr:.4f}"
                sig = "*" if r.get("p_fdr") is not None and r["p_fdr"] < 0.05 else " "
                fp = "FP?" if r.get("note", "").startswith("consistent") else "   "
                line += f" | {p_raw} {p_fdr:>7} {sig}{fp}"
            else:
                line += f" |    --       --     "
        print(line)

    # FDR summary
    valid = [r for r in gc if r.get("p_raw") is not None]
    n_total = len(valid)
    n_raw_sig = sum(1 for r in valid if r["p_raw"] < 0.05)
    n_fdr_sig = sum(1 for r in valid if r.get("p_fdr") is not None and r["p_fdr"] < 0.05)
    print(f"\nFDR: {n_raw_sig}/{n_total} raw-sig → {n_fdr_sig}/{n_total} FDR-sig (BH correction across all {n_total} tests)")

    # Cross-correlation
    xcorr = output["cross_correlation"]
    print(f"\n{'CROSS-CORRELATION (Δmetric, peak lag)'}")
    print("-" * 60)
    for pair_label in ["entropy_vs_d1", "ece_vs_d1"]:
        line = f"  {pair_label:<18}"
        for ak in sorted(xcorr.keys()):
            p = xcorr[ak].get(pair_label, {})
            line += f" | α={xcorr[ak]['alpha']}: lag={p.get('peak_lag','?'):>2} r={p.get('peak_r','?'):>7}"
        print(line)

    # Velocity
    vel = output["per_gen_velocity"]
    print(f"\n{'D1 VELOCITY'}")
    print("-" * 60)
    for ak in sorted(vel.keys()):
        v = vel[ak]
        decel = f"{v['deceleration_ratio']:.2f}" if v.get("deceleration_ratio") is not None else "N/A"
        print(f"  α={v['alpha']}: mean_vel={v['mean_velocity']:+.6f}  "
              f"early={v['early_mean_velocity']:+.6f}  late={v['late_mean_velocity']:+.6f}  "
              f"decel_ratio={decel}  max_drop=gen{v['max_drop_gen']}")

    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Cross-alpha analysis for distributional canary collapse experiments."
    )
    parser.add_argument("--alpha-dirs", nargs="*", default=None,
                        help="Specific alpha dirs (e.g. a000_s42 a025_s42). Default: auto-discover all.")
    parser.add_argument("--n-perms", type=int, default=5000,
                        help="Number of permutations for Granger test (default: 5000)")
    parser.add_argument("--max-lag", type=int, default=1,
                        help="Max lag for Granger test (default: 1)")
    parser.add_argument("--version", type=int, default=None,
                        help="Output version number (default: auto-increment)")
    parser.add_argument("--update-registry", action="store_true",
                        help="Print registry update commands after analysis")
    args = parser.parse_args()

    alpha_dirs = discover_alpha_dirs(args.alpha_dirs)
    if not alpha_dirs:
        print("ERROR: No alpha directories found.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(alpha_dirs)} alpha points: {[a[0] for a in alpha_dirs]}")

    all_data = []
    for alpha_key, alpha_val, path in alpha_dirs:
        metrics = load_metrics(path)
        print(f"  {alpha_key} (α={alpha_val}): {len(metrics)} generations")
        all_data.append((alpha_key, alpha_val, metrics))

    # 1. Dose-response
    dose_resp = compute_dose_response(all_data)

    # 2. Granger
    print(f"\nRunning bidirectional Granger ({len(GRANGER_PAIRS)} pairs × {len(all_data)} alphas, "
          f"n_perms={args.n_perms})...")
    granger = run_granger_all(all_data, max_lag=args.max_lag, n_perms=args.n_perms)
    granger = apply_fdr(granger)

    # 3. Cross-correlation
    xcorr = cross_correlation(all_data)

    # 4. Velocity
    velocity = per_gen_velocity(all_data)

    # Assemble output
    version = args.version or auto_version()
    n_gens = len(all_data[0][2]) if all_data else 0
    output = {
        "version": f"v{version}",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "n_alphas": len(all_data),
        "alpha_points": [a[1] for a in all_data],
        "n_generations": n_gens,
        "gen_range": f"gen_0 to gen_{n_gens - 1}" if n_gens else "N/A",
        "statistical_config": {
            "granger_max_lag": args.max_lag,
            "granger_n_perm": args.n_perms,
            "granger_differenced": True,
            "fdr_method": "benjamini-hochberg",
            "fdr_scope": f"all {len(granger)} tests corrected together",
            "n_independent_tests": len([r for r in granger if r.get("p_raw") is not None]),
        },
        "dose_response": dose_resp,
        "granger_causality": granger,
        "cross_correlation": xcorr,
        "per_gen_velocity": velocity,
    }

    # Save JSON
    os.makedirs(ANALYSIS_DIR, exist_ok=True)
    out_path = os.path.join(ANALYSIS_DIR, f"cross_alpha_v{version}.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print_summary(output)
    print(f"Saved: {out_path}")

    if args.update_registry:
        print("\n--- Registry update commands ---")
        for alpha_key, alpha_val, _ in all_data:
            dr = dose_resp[alpha_key]
            print(f"# {alpha_key}: d1_drift={dr['distinct_1']['drift_pct']}%, "
                  f"entropy_drift={dr['token_entropy']['drift_pct']}%, "
                  f"ece_drift={dr['ece']['drift_pct']}%")


if __name__ == "__main__":
    main()
