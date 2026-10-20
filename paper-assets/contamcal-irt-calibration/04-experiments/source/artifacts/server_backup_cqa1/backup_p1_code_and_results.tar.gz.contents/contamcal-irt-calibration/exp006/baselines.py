"""
7 baseline calibration methods for comparison with IRT 4PL+gamma.
All methods share a unified interface: matrix-level inputs, dict outputs.

B0: Raw -- no adjustment (anchor)
B1: Remove-and-rescore -- drop high-exposure items, rescore on remainder
B2: Single-signal 2PL+gamma -- simplified IRT with contamination covariate
B3: Vanilla 4PL -- standard IRT without contamination covariate
B4: Linear exposure regression + bootstrap CI
B5: Emperor's mitigation -- rephrasing / exposure-weighted downweighting
B6: DCR fuzzy inference -- adapted from Xu et al. (EMNLP 2025)

Dependencies: numpy, scipy, cmdstanpy (B2/B3 only)
"""

import logging
import os
import time

import numpy as np
from scipy import stats

log = logging.getLogger(__name__)

STAN_MODEL_DIR = "/root/contamcal-irt-calibration/stan_models"
SEED = 42
N_BOOTSTRAP = 1000


class BaselineMethod:
    """Unified interface for baseline calibration methods."""
    name = "base"
    description = ""

    def fit(self, correctness_matrix, exposure_scores, **kwargs):
        """
        Args:
            correctness_matrix: (N_models, N_items) binary int array
            exposure_scores: (N_models, N_items) float array
        Returns:
            dict with keys: calibrated_scores, ci_lower, ci_upper,
                           ci_80_lower, ci_80_upper, ci_50_lower, ci_50_upper
        """
        raise NotImplementedError


class RawBaseline(BaselineMethod):
    """B0: No adjustment -- raw accuracy per model."""
    name = "B0_raw"
    description = "Raw accuracy (no adjustment)"

    def fit(self, y, exposure, **kwargs):
        acc = y.mean(axis=1)
        n_items = y.shape[1]

        from scipy.stats import norm
        def _wilson_ci(p, n, z):
            denom = 1 + z**2 / n
            center = (p + z**2 / (2 * n)) / denom
            margin = z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / denom
            return np.clip(center - margin, 0, 1), np.clip(center + margin, 0, 1)

        ci95_lo, ci95_hi = _wilson_ci(acc, n_items, norm.ppf(0.975))
        ci80_lo, ci80_hi = _wilson_ci(acc, n_items, norm.ppf(0.9))
        ci50_lo, ci50_hi = _wilson_ci(acc, n_items, norm.ppf(0.75))

        return {
            "calibrated_scores": acc.tolist(),
            "ci_lower": ci95_lo.tolist(), "ci_upper": ci95_hi.tolist(),
            "ci_80_lower": ci80_lo.tolist(), "ci_80_upper": ci80_hi.tolist(),
            "ci_50_lower": ci50_lo.tolist(), "ci_50_upper": ci50_hi.tolist(),
        }


class RemoveRescoreBaseline(BaselineMethod):
    """B1: Remove items with exposure above 75th-percentile threshold, rescore."""
    name = "B1_remove_rescore"
    description = "Remove flagged items and rescore"

    def fit(self, y, exposure, threshold_pct=75, **kwargs):
        item_exposure = exposure.mean(axis=0)
        threshold = float(np.percentile(item_exposure, threshold_pct))
        keep = item_exposure <= threshold
        n_kept = int(keep.sum())
        log.info("B1: threshold=%.3f (p%d), kept=%d/%d items",
                 threshold, threshold_pct, n_kept, y.shape[1])

        if n_kept == 0:
            log.warning("B1: all items removed, falling back to raw accuracy")
            acc = y.mean(axis=1)
            kept_idx = np.arange(y.shape[1])
        else:
            acc = y[:, keep].mean(axis=1)
            kept_idx = np.where(keep)[0]

        rng = np.random.default_rng(SEED)
        boot = np.zeros((N_BOOTSTRAP, y.shape[0]))
        for b in range(N_BOOTSTRAP):
            idx = rng.choice(kept_idx, size=len(kept_idx), replace=True)
            boot[b] = y[:, idx].mean(axis=1)

        return {
            "calibrated_scores": acc.tolist(),
            "ci_lower": np.percentile(boot, 2.5, axis=0).tolist(),
            "ci_upper": np.percentile(boot, 97.5, axis=0).tolist(),
            "ci_80_lower": np.percentile(boot, 10, axis=0).tolist(),
            "ci_80_upper": np.percentile(boot, 90, axis=0).tolist(),
            "ci_50_lower": np.percentile(boot, 25, axis=0).tolist(),
            "ci_50_upper": np.percentile(boot, 75, axis=0).tolist(),
            "n_kept": n_kept,
            "n_removed": int(y.shape[1] - n_kept),
            "threshold": threshold,
        }


class SingleSignal2PLGamma(BaselineMethod):
    """B2: 2PL IRT with gamma contamination covariate (no c/d params)."""
    name = "B2_2pl_gamma"
    description = "Single-signal 2PL+gamma IRT"

    def fit(self, y, exposure, chains=4, samples=1000, **kwargs):
        import cmdstanpy
        stan_file = os.path.join(STAN_MODEL_DIR, "contam_irt_2pl_gamma.stan")
        stan_data = {
            "N_models": int(y.shape[0]),
            "N_items": int(y.shape[1]),
            "y": y.astype(int).tolist(),
            "exposure": exposure.tolist(),
        }
        log.info("B2: fitting 2PL+gamma (%d x %d)", y.shape[0], y.shape[1])
        model = cmdstanpy.CmdStanModel(stan_file=stan_file)
        fit = model.sample(
            data=stan_data, chains=chains,
            iter_sampling=samples, iter_warmup=samples,
            adapt_delta=0.95, seed=SEED, show_progress=True,
        )

        cal = fit.stan_variable("calibrated_score")
        gamma_draws = fit.stan_variable("gamma")

        return {
            "calibrated_scores": np.mean(cal, axis=0).tolist(),
            "ci_lower": np.percentile(cal, 2.5, axis=0).tolist(),
            "ci_upper": np.percentile(cal, 97.5, axis=0).tolist(),
            "ci_80_lower": np.percentile(cal, 10, axis=0).tolist(),
            "ci_80_upper": np.percentile(cal, 90, axis=0).tolist(),
            "ci_50_lower": np.percentile(cal, 25, axis=0).tolist(),
            "ci_50_upper": np.percentile(cal, 75, axis=0).tolist(),
            "gamma_mean": round(float(np.mean(gamma_draws)), 4),
            "gamma_sd": round(float(np.std(gamma_draws)), 4),
        }


class Vanilla4PL(BaselineMethod):
    """B3: Standard 4PL IRT without contamination covariate (gamma=0)."""
    name = "B3_vanilla_4pl"
    description = "Vanilla 4PL IRT (no gamma)"

    def fit(self, y, exposure, chains=4, samples=1000, **kwargs):
        import cmdstanpy
        stan_file = os.path.join(STAN_MODEL_DIR, "vanilla_4pl.stan")
        stan_data = {
            "N_models": int(y.shape[0]),
            "N_items": int(y.shape[1]),
            "y": y.astype(int).tolist(),
        }
        log.info("B3: fitting vanilla 4PL (%d x %d)", y.shape[0], y.shape[1])
        model = cmdstanpy.CmdStanModel(stan_file=stan_file)
        fit = model.sample(
            data=stan_data, chains=chains,
            iter_sampling=samples, iter_warmup=samples,
            adapt_delta=0.95, seed=SEED, show_progress=True,
        )

        cal = fit.stan_variable("calibrated_score")

        return {
            "calibrated_scores": np.mean(cal, axis=0).tolist(),
            "ci_lower": np.percentile(cal, 2.5, axis=0).tolist(),
            "ci_upper": np.percentile(cal, 97.5, axis=0).tolist(),
            "ci_80_lower": np.percentile(cal, 10, axis=0).tolist(),
            "ci_80_upper": np.percentile(cal, 90, axis=0).tolist(),
            "ci_50_lower": np.percentile(cal, 25, axis=0).tolist(),
            "ci_50_upper": np.percentile(cal, 75, axis=0).tolist(),
        }


class LinearRegressionBaseline(BaselineMethod):
    """B4: Regress accuracy on mean exposure, subtract slope*exposure."""
    name = "B4_linear_regression"
    description = "Linear exposure regression + bootstrap CI"

    def fit(self, y, exposure, **kwargs):
        acc = y.mean(axis=1)
        exp_mean = exposure.mean(axis=1)

        # Guard: constant exposure means no regression is possible
        if np.std(exp_mean) < 1e-10:
            log.info("B4: constant exposure, falling back to raw accuracy")
            adjusted = acc.copy()
            slope, r_value = 0.0, 0.0
        else:
            slope, intercept, r_value, _, _ = stats.linregress(exp_mean, acc)
            adjusted = acc - slope * exp_mean
            log.info("B4: slope=%.4f, R2=%.4f", slope, r_value**2)

        rng = np.random.default_rng(SEED)
        n = len(acc)
        boot = np.zeros((N_BOOTSTRAP, n))
        for b in range(N_BOOTSTRAP):
            idx = rng.choice(n, size=n, replace=True)
            if np.std(exp_mean[idx]) < 1e-10:
                boot[b] = acc
            else:
                s, _, *_ = stats.linregress(exp_mean[idx], acc[idx])
                boot[b] = acc - s * exp_mean

        return {
            "calibrated_scores": adjusted.tolist(),
            "ci_lower": np.percentile(boot, 2.5, axis=0).tolist(),
            "ci_upper": np.percentile(boot, 97.5, axis=0).tolist(),
            "ci_80_lower": np.percentile(boot, 10, axis=0).tolist(),
            "ci_80_upper": np.percentile(boot, 90, axis=0).tolist(),
            "ci_50_lower": np.percentile(boot, 25, axis=0).tolist(),
            "ci_50_upper": np.percentile(boot, 75, axis=0).tolist(),
            "slope": round(float(slope), 6),
            "r_squared": round(float(r_value**2), 6),
        }


class EmperorMitigationBaseline(BaselineMethod):
    """B5: Emperor's mitigation -- rephrasing or exposure-weighted downweighting."""
    name = "B5_emperor_mitigation"
    description = "Emperor's mitigation (rephrasing + option shuffling)"

    def fit(self, y, exposure, rephrased_y=None, **kwargs):
        if rephrased_y is not None:
            acc = rephrased_y.mean(axis=1)
            log.info("B5: using actual rephrased responses")
        else:
            # Downweight high-exposure items
            weights = 1.0 - exposure.mean(axis=0)
            weights = np.clip(weights, 0.01, 1.0)
            weights = weights / weights.sum() * len(weights)
            acc = (y * weights[None, :]).mean(axis=1)
            log.info("B5: exposure-weighted downweighting (no rephrased data)")

        rng = np.random.default_rng(SEED)
        n_items = y.shape[1]
        boot = np.zeros((N_BOOTSTRAP, y.shape[0]))
        for b in range(N_BOOTSTRAP):
            idx = rng.choice(n_items, size=n_items, replace=True)
            if rephrased_y is not None:
                boot[b] = rephrased_y[:, idx].mean(axis=1)
            else:
                w = 1.0 - exposure[:, idx].mean(axis=0)
                w = np.clip(w, 0.01, 1.0)
                w = w / w.sum() * len(w)
                boot[b] = (y[:, idx] * w[None, :]).mean(axis=1)

        return {
            "calibrated_scores": acc.tolist(),
            "ci_lower": np.percentile(boot, 2.5, axis=0).tolist(),
            "ci_upper": np.percentile(boot, 97.5, axis=0).tolist(),
            "ci_80_lower": np.percentile(boot, 10, axis=0).tolist(),
            "ci_80_upper": np.percentile(boot, 90, axis=0).tolist(),
            "ci_50_lower": np.percentile(boot, 25, axis=0).tolist(),
            "ci_50_upper": np.percentile(boot, 75, axis=0).tolist(),
        }


class DCRFuzzyBaseline(BaselineMethod):
    """B6: DCR fuzzy inference adapted from Xu et al. (EMNLP 2025).

    Uses continuous exposure thresholds to derive contamination levels,
    then fuzzy inference to compute a multiplicative DCR discount factor.
    """
    name = "B6_dcr_fuzzy"
    description = "DCR fuzzy inference (EMNLP 2025)"

    @staticmethod
    def _trapmf(x, abcd):
        a, b, c, d = abcd
        y = np.zeros_like(x, dtype=float)
        if b > a:
            mask = (x >= a) & (x < b)
            y[mask] = (x[mask] - a) / (b - a)
        y[(x >= b) & (x <= c)] = 1.0
        if d > c:
            mask = (x > c) & (x <= d)
            y[mask] = (d - x[mask]) / (d - c)
        return y

    @staticmethod
    def _trimf(x, abc):
        return DCRFuzzyBaseline._trapmf(x, [abc[0], abc[1], abc[1], abc[2]])

    def _compute_dcr_factor(self, item_exposure):
        """Compute DCR factor from per-item exposure scores for one model."""
        thresholds = [0.1, 0.3, 0.5, 0.7]
        s_values = np.array([float(np.mean(item_exposure > t)) for t in thresholds])

        if np.mean(s_values) < 0.02:
            return 0.0

        x_in = np.linspace(0, 1, 101)
        in_low = self._trapmf(x_in, [0, 0, 0.1, 0.3])
        in_med = self._trapmf(x_in, [0.2, 0.4, 0.5, 0.6])
        in_high = self._trapmf(x_in, [0.5, 0.8, 1.0, 1.0])

        x_out = np.linspace(0, 1, 101)
        out_negligible = self._trapmf(x_out, [0, 0, 0.1, 0.3])
        out_minor = self._trimf(x_out, [0.1, 0.3, 0.5])
        out_moderate = self._trimf(x_out, [0.3, 0.5, 0.7])
        out_significant = self._trimf(x_out, [0.5, 0.7, 0.9])
        out_severe = self._trapmf(x_out, [0.7, 0.9, 1.0, 1.0])

        min_memb = max(0.001, np.mean(s_values))
        memberships = []
        for s in s_values:
            memberships.append({
                "Low": max(float(np.interp(s, x_in, in_low)), min_memb * 0.1),
                "Medium": max(float(np.interp(s, x_in, in_med)), min_memb * 0.1),
                "High": max(float(np.interp(s, x_in, in_high)), min_memb * 0.1),
            })

        r0 = min(m["Low"] for m in memberships)
        r1 = max(memberships[2]["High"], memberships[3]["High"])
        r2 = max(memberships[0]["High"], memberships[1]["High"])
        r3 = np.mean([m["Medium"] for m in memberships])
        r4 = max(memberships[0]["Medium"], memberships[1]["Low"])

        aggregated = np.fmax(
            np.fmin(r0, out_negligible),
            np.fmax(np.fmin(r1, out_severe),
                    np.fmax(np.fmin(r2, out_significant),
                            np.fmax(np.fmin(r3, out_moderate),
                                    np.fmin(r4, out_minor)))))

        if np.max(aggregated) < 0.06:
            aggregated = np.fmax(aggregated, out_negligible * min_memb)

        total = np.sum(aggregated)
        if total < 1e-10:
            return float(min_memb)
        return float(np.clip(np.sum(x_out * aggregated) / total, 0, 1))

    def fit(self, y, exposure, **kwargs):
        raw_acc = y.mean(axis=1)
        N_models = y.shape[0]
        adjusted = np.zeros(N_models)
        dcr_factors = np.zeros(N_models)

        for i in range(N_models):
            dcr_factors[i] = self._compute_dcr_factor(exposure[i])
            adjusted[i] = raw_acc[i] * (1 - dcr_factors[i])

        log.info("B6: mean DCR factor=%.4f", dcr_factors.mean())

        rng = np.random.default_rng(SEED)
        n_items = y.shape[1]
        boot = np.zeros((N_BOOTSTRAP, N_models))
        for b in range(N_BOOTSTRAP):
            idx = rng.choice(n_items, size=n_items, replace=True)
            y_b = y[:, idx]
            exp_b = exposure[:, idx]
            for i in range(N_models):
                f = self._compute_dcr_factor(exp_b[i])
                boot[b, i] = y_b[i].mean() * (1 - f)

        return {
            "calibrated_scores": adjusted.tolist(),
            "ci_lower": np.percentile(boot, 2.5, axis=0).tolist(),
            "ci_upper": np.percentile(boot, 97.5, axis=0).tolist(),
            "ci_80_lower": np.percentile(boot, 10, axis=0).tolist(),
            "ci_80_upper": np.percentile(boot, 90, axis=0).tolist(),
            "ci_50_lower": np.percentile(boot, 25, axis=0).tolist(),
            "ci_50_upper": np.percentile(boot, 75, axis=0).tolist(),
            "dcr_factors": dcr_factors.tolist(),
        }


# ── Registry ──

ALL_BASELINES = {
    "B0_raw": RawBaseline(),
    "B1_remove_rescore": RemoveRescoreBaseline(),
    "B2_2pl_gamma": SingleSignal2PLGamma(),
    "B3_vanilla_4pl": Vanilla4PL(),
    "B4_linear_regression": LinearRegressionBaseline(),
    "B5_emperor_mitigation": EmperorMitigationBaseline(),
    "B6_dcr_fuzzy": DCRFuzzyBaseline(),
}


def run_all_baselines(y, exposure, skip_stan=False, **kwargs):
    """Run all baseline methods. Returns dict of method_name -> result."""
    results = {}
    for name, method in ALL_BASELINES.items():
        if skip_stan and name in ("B2_2pl_gamma", "B3_vanilla_4pl"):
            log.info("Skipping %s (--skip-stan)", name)
            continue
        log.info("Running %s: %s", name, method.description)
        try:
            t0 = time.time()
            result = method.fit(y, exposure, **kwargs)
            result["compute_time_sec"] = round(time.time() - t0, 1)
            result["method_name"] = name
            result["description"] = method.description
            results[name] = result
            log.info("  %s done in %.1fs", name, result["compute_time_sec"])
        except Exception as e:
            log.error("  %s failed: %s", name, e)
            results[name] = {"method_name": name, "error": str(e)}
    return results


# ── CLI ──

if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Run baseline calibration methods")
    parser.add_argument("--response-matrix", required=True)
    parser.add_argument("--exposure-matrix", required=True)
    parser.add_argument("--benchmark", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--skip-stan", action="store_true",
                        help="Skip Stan-based baselines (B2, B3)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

    from run_irt_calibration import load_matrix
    y = load_matrix(args.response_matrix).astype(int)
    exposure = load_matrix(args.exposure_matrix)
    assert y.shape == exposure.shape

    results = run_all_baselines(y, exposure, skip_stan=args.skip_stan)

    os.makedirs(args.output_dir, exist_ok=True)
    out_path = os.path.join(args.output_dir, f"{args.benchmark}_baselines.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    log.info("Results saved to %s", out_path)
