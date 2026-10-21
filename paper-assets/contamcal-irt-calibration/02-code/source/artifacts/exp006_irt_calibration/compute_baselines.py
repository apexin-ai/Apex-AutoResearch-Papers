# exp-006: 7 baseline calibration methods for comparison with IRT
# Baseline 0: Raw (no adjustment)
# Baseline 1: Remove-and-rescore
# Baseline 2: Single-signal 2PL+γ
# Baseline 3: Vanilla 4PL (no gamma)
# Baseline 4: Linear exposure regression + bootstrap CI
# Baseline 5: Emperor's mitigation (rephrasing)
# Baseline 6: DCR-inspired linear adjustment (not faithful reproduction)

import argparse
import json
import logging
import os
import sys
import time

import numpy as np
from scipy import stats
import cmdstanpy

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SEED = 42
N_BOOTSTRAP = 1000


def load_matrix(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".npy":
        return np.load(path)
    elif ext == ".csv":
        return np.loadtxt(path, delimiter=",", skiprows=1)
    elif ext == ".json":
        with open(path) as f:
            return np.array(json.load(f))
    else:
        raise ValueError(f"Unsupported format: {ext}")


def baseline_0_raw(y, exposure):
    """No adjustment — raw accuracy per model."""
    acc = y.mean(axis=1)
    return {
        "name": "B0_raw",
        "description": "Raw accuracy (no adjustment)",
        "scores": np.round(acc, 6).tolist(),
        "ci_lower": None,
        "ci_upper": None,
    }


def baseline_1_remove_rescore(y, exposure, threshold=None):
    """Remove items with mean exposure above 75th percentile, rescore on remaining."""
    item_exposure = exposure.mean(axis=0)
    if threshold is None:
        threshold = float(np.percentile(item_exposure, 75))
    keep_mask = item_exposure <= threshold
    n_kept = int(keep_mask.sum())
    n_removed = int((~keep_mask).sum())
    log.info("B1: threshold=%.2f, kept=%d, removed=%d items", threshold, n_kept, n_removed)

    if n_kept == 0:
        log.warning("B1: all items removed, falling back to raw accuracy")
        acc = y.mean(axis=1)
    else:
        acc = y[:, keep_mask].mean(axis=1)

    rng = np.random.default_rng(SEED)
    boot_scores = np.zeros((N_BOOTSTRAP, y.shape[0]))
    kept_items = np.where(keep_mask)[0]
    for b in range(N_BOOTSTRAP):
        idx = rng.choice(kept_items, size=len(kept_items), replace=True)
        boot_scores[b] = y[:, idx].mean(axis=1)

    return {
        "name": "B1_remove_rescore",
        "description": f"Remove items with exposure > {threshold}, rescore",
        "scores": np.round(acc, 6).tolist(),
        "ci_lower": np.round(np.percentile(boot_scores, 2.5, axis=0), 6).tolist(),
        "ci_upper": np.round(np.percentile(boot_scores, 97.5, axis=0), 6).tolist(),
        "n_kept": n_kept,
        "n_removed": n_removed,
        "threshold": threshold,
    }


def baseline_2_2pl_gamma(y, exposure):
    """Single-signal 2PL+γ IRT via Stan NUTS."""
    stan_file = os.path.join(SCRIPT_DIR, "contam_irt_2pl.stan")
    stan_data = {
        "N_models": int(y.shape[0]),
        "N_items": int(y.shape[1]),
        "y": y.astype(int).tolist(),
        "exposure": exposure.tolist(),
    }

    log.info("B2: fitting 2PL+γ Stan model")
    model = cmdstanpy.CmdStanModel(stan_file=stan_file)
    fit = model.sample(
        data=stan_data,
        chains=4,
        iter_warmup=1000,
        iter_sampling=2000,
        adapt_delta=0.95,
        seed=SEED,
        show_progress=True,
    )

    cal_draws = fit.stan_variable("calibrated_score")
    cal_mean = np.mean(cal_draws, axis=0)

    return {
        "name": "B2_2pl_gamma",
        "description": "Single-signal 2PL+γ IRT",
        "scores": np.round(cal_mean, 6).tolist(),
        "ci_lower": np.round(np.percentile(cal_draws, 2.5, axis=0), 6).tolist(),
        "ci_upper": np.round(np.percentile(cal_draws, 97.5, axis=0), 6).tolist(),
    }


def _fit_vanilla_4pl_stan(y):
    """Fit vanilla 4PL IRT (no exposure covariate) via Stan."""
    stan_code = """
data {
  int<lower=1> N_models;
  int<lower=1> N_items;
  array[N_models, N_items] int<lower=0, upper=1> y;
}
parameters {
  vector[N_models] theta;
  vector<lower=0>[N_items] a;
  vector[N_items] b;
  vector<lower=0, upper=1>[N_items] c;
  vector<lower=0, upper=1>[N_items] d;
}
model {
  theta ~ std_normal();
  a ~ lognormal(0, 0.5);
  b ~ std_normal();
  c ~ beta(5, 20);
  d ~ beta(20, 5);
  for (i in 1:N_models)
    for (j in 1:N_items) {
      real eta = a[j] * (theta[i] - b[j]);
      real p = c[j] + (d[j] - c[j]) * inv_logit(eta);
      y[i, j] ~ bernoulli(p);
    }
}
generated quantities {
  array[N_models] real calibrated_score;
  for (i in 1:N_models) {
    real total = 0.0;
    for (j in 1:N_items) {
      real eta = a[j] * (theta[i] - b[j]);
      total += c[j] + (d[j] - c[j]) * inv_logit(eta);
    }
    calibrated_score[i] = total / N_items;
  }
}
"""
    stan_path = os.path.join(SCRIPT_DIR, "_vanilla_4pl_tmp.stan")
    with open(stan_path, "w") as f:
        f.write(stan_code)

    stan_data = {
        "N_models": int(y.shape[0]),
        "N_items": int(y.shape[1]),
        "y": y.astype(int).tolist(),
    }

    model = cmdstanpy.CmdStanModel(stan_file=stan_path)
    fit = model.sample(
        data=stan_data,
        chains=4,
        iter_warmup=1000,
        iter_sampling=2000,
        adapt_delta=0.95,
        seed=SEED,
        show_progress=True,
    )
    return fit


def baseline_3_vanilla_4pl(y, exposure):
    """Standard 4PL IRT with no exposure covariate (gamma=0)."""
    log.info("B3: fitting vanilla 4PL (no gamma)")
    fit = _fit_vanilla_4pl_stan(y)

    cal_draws = fit.stan_variable("calibrated_score")
    cal_mean = np.mean(cal_draws, axis=0)

    return {
        "name": "B3_vanilla_4pl",
        "description": "Vanilla 4PL IRT (no exposure covariate)",
        "scores": np.round(cal_mean, 6).tolist(),
        "ci_lower": np.round(np.percentile(cal_draws, 2.5, axis=0), 6).tolist(),
        "ci_upper": np.round(np.percentile(cal_draws, 97.5, axis=0), 6).tolist(),
    }


def baseline_4_linear_regression(y, exposure):
    """Linear regression of accuracy on mean exposure + bootstrap CIs."""
    acc = y.mean(axis=1)
    exp_mean = exposure.mean(axis=1)

    slope, intercept, r_value, p_value, std_err = stats.linregress(exp_mean, acc)
    adjusted = acc - slope * exp_mean
    log.info("B4: slope=%.4f, intercept=%.4f, R²=%.4f", slope, intercept, r_value**2)

    rng = np.random.default_rng(SEED)
    n = len(acc)
    boot_adjusted = np.zeros((N_BOOTSTRAP, n))
    for b in range(N_BOOTSTRAP):
        idx = rng.choice(n, size=n, replace=True)
        s, i, *_ = stats.linregress(exp_mean[idx], acc[idx])
        boot_adjusted[b] = acc - s * exp_mean

    return {
        "name": "B4_linear_regression",
        "description": "Linear exposure regression + bootstrap CI",
        "scores": np.round(adjusted, 6).tolist(),
        "ci_lower": np.round(np.percentile(boot_adjusted, 2.5, axis=0), 6).tolist(),
        "ci_upper": np.round(np.percentile(boot_adjusted, 97.5, axis=0), 6).tolist(),
        "slope": round(float(slope), 6),
        "intercept": round(float(intercept), 6),
        "r_squared": round(float(r_value**2), 6),
    }


def baseline_5_emperor_rephrasing(y, exposure, rephrased_response_path=None):
    """Emperor's mitigation: use accuracy on paraphrased items.
    If rephrased data is not available, estimate by downweighting high-exposure items.
    """
    if rephrased_response_path and os.path.exists(rephrased_response_path):
        y_rephrased = load_matrix(rephrased_response_path)
        acc = y_rephrased.mean(axis=1)
        log.info("B5: using rephrased response matrix")
    else:
        log.info("B5: no rephrased data, estimating via exposure-weighted downweighting")
        weights = 1.0 - exposure.mean(axis=0)
        weights = weights / weights.sum() * len(weights)
        acc = (y * weights[None, :]).mean(axis=1)

    return {
        "name": "B5_emperor_rephrasing",
        "description": "Emperor's mitigation (rephrasing / exposure-weighted)",
        "scores": np.round(acc, 6).tolist(),
        "ci_lower": None,
        "ci_upper": None,
    }


def baseline_6_dcr(y, exposure):
    """DCR-inspired linear adjustment (not a faithful reproduction of DCR).
    adjusted_acc = raw_acc - mean_exposure * effect_strength, where effect_strength
    is estimated from the correlation between item exposure and item accuracy.
    """
    raw_acc = y.mean(axis=1)
    model_mean_exposure = exposure.mean(axis=1)

    item_acc = y.mean(axis=0)
    item_exp = exposure.mean(axis=0)
    if np.std(item_exp) > 1e-8:
        corr = np.corrcoef(item_exp, item_acc)[0, 1]
        effect_strength = max(0, corr)
    else:
        effect_strength = 0.0

    contamination_effect = model_mean_exposure * effect_strength
    adjusted_acc = raw_acc - contamination_effect
    adjusted_acc = np.clip(adjusted_acc, 0, 1)

    log.info("B6: DCR effect_strength=%.4f, mean_effect=%.4f", effect_strength, contamination_effect.mean())

    rng = np.random.default_rng(SEED)
    n = len(raw_acc)
    boot_adjusted = np.zeros((N_BOOTSTRAP, n))
    for b in range(N_BOOTSTRAP):
        idx_items = rng.choice(y.shape[1], size=y.shape[1], replace=True)
        y_b = y[:, idx_items]
        exp_b = exposure[:, idx_items]
        r_acc = y_b.mean(axis=1)
        m_exp = exp_b.mean(axis=1)
        i_acc = y_b.mean(axis=0)
        i_exp = exp_b.mean(axis=0)
        if np.std(i_exp) > 1e-8:
            c = max(0, np.corrcoef(i_exp, i_acc)[0, 1])
        else:
            c = 0.0
        boot_adjusted[b] = np.clip(r_acc - m_exp * c, 0, 1)

    return {
        "name": "B6_DCR_inspired",
        "description": "DCR-inspired linear adjustment (not faithful reproduction)",
        "scores": np.round(adjusted_acc, 6).tolist(),
        "ci_lower": np.round(np.percentile(boot_adjusted, 2.5, axis=0), 6).tolist(),
        "ci_upper": np.round(np.percentile(boot_adjusted, 97.5, axis=0), 6).tolist(),
        "effect_strength": round(float(effect_strength), 6),
    }


def main():
    parser = argparse.ArgumentParser(description="Compute baseline calibration methods")
    parser.add_argument("--response-matrix", required=True, help="Path to binary response matrix")
    parser.add_argument("--exposure-scores", required=True, help="Path to exposure score matrix")
    parser.add_argument("--benchmark", required=True, help="Benchmark name")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    parser.add_argument("--rephrased-matrix", default=None, help="Path to rephrased response matrix (for B5)")
    parser.add_argument("--remove-threshold", type=float, default=None, help="Exposure threshold for B1 (default: 75th percentile)")
    parser.add_argument("--baselines", default="0,1,2,3,4,5,6", help="Comma-separated baseline IDs to compute")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    y = load_matrix(args.response_matrix)
    exposure = load_matrix(args.exposure_scores)
    assert y.shape == exposure.shape, (
        f"Shape mismatch: response {y.shape} vs exposure {exposure.shape}"
    )
    log.info("Benchmark: %s | Data: %d models × %d items", args.benchmark, y.shape[0], y.shape[1])

    baseline_ids = [int(x.strip()) for x in args.baselines.split(",")]
    baseline_funcs = {
        0: lambda: baseline_0_raw(y, exposure),
        1: lambda: baseline_1_remove_rescore(y, exposure, threshold=args.remove_threshold),
        2: lambda: baseline_2_2pl_gamma(y, exposure),
        3: lambda: baseline_3_vanilla_4pl(y, exposure),
        4: lambda: baseline_4_linear_regression(y, exposure),
        5: lambda: baseline_5_emperor_rephrasing(y, exposure, args.rephrased_matrix),
        6: lambda: baseline_6_dcr(y, exposure),
    }

    all_results = {}
    for bid in baseline_ids:
        if bid not in baseline_funcs:
            log.warning("Unknown baseline ID: %d, skipping", bid)
            continue
        log.info("Computing baseline %d...", bid)
        t0 = time.time()
        result = baseline_funcs[bid]()
        result["compute_time_sec"] = round(time.time() - t0, 1)
        all_results[result["name"]] = result
        log.info("  %s done in %.1fs", result["name"], result["compute_time_sec"])

    out_path = os.path.join(args.output_dir, f"{args.benchmark}_baselines.json")
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    log.info("All baselines written to %s", out_path)


if __name__ == "__main__":
    main()
