# CmdStanPy Bayesian IRT calibration pipeline (replaces PyTorch MLE version)
# 4PL+γ model: P(y=1) = c + (d-c) * logit^{-1}(a*(theta - b) + gamma * exposure)

import argparse
import json
import logging
import os
import re
import sys
import time
from pathlib import Path

import numpy as np
import cmdstanpy

logger = logging.getLogger(__name__)

DOSAGE_PATTERN = re.compile(r"_d(\d+)_s(\d+)(_para)?$")


def parse_model_dir_name(dirname: str) -> dict | None:
    m = DOSAGE_PATTERN.search(dirname)
    if not m:
        return None
    dosage = int(m.group(1))
    seed = int(m.group(2))
    is_para = m.group(3) is not None
    model_name = dirname[: m.start()]
    return {
        "dirname": dirname,
        "model_name": model_name,
        "dosage": dosage,
        "seed": seed,
        "is_para": is_para,
    }


def load_eval_results(eval_dir: str, benchmarks: list[str] | None = None,
                      skip_para: bool = True) -> dict:
    eval_path = Path(eval_dir)
    model_dirs = sorted([
        d for d in eval_path.iterdir()
        if d.is_dir() and (d / "eval_results.json").exists()
    ])

    models = []
    for d in model_dirs:
        info = parse_model_dir_name(d.name)
        if info is None:
            logger.warning("Skipping unrecognized directory: %s", d.name)
            continue
        if skip_para and info["is_para"]:
            continue
        info["path"] = str(d)
        models.append(info)

    if not models:
        raise ValueError(f"No valid eval results found in {eval_dir}")

    logger.info("Found %d model evaluations", len(models))

    with open(Path(models[0]["path"]) / "eval_results.json") as f:
        sample = json.load(f)
    available_benchmarks = list(sample["benchmarks"].keys())

    if benchmarks:
        benchmarks = [b for b in benchmarks if b in available_benchmarks]
    else:
        benchmarks = available_benchmarks

    logger.info("Benchmarks: %s", benchmarks)

    result = {"models": models, "benchmarks": {}, "dosages": np.array([m["dosage"] for m in models])}

    for bench in benchmarks:
        responses = []
        for m in models:
            results_file = Path(m["path"]) / "eval_results.json"
            with open(results_file) as f:
                data = json.load(f)

            if bench not in data["benchmarks"]:
                logger.warning("Benchmark %s missing for %s", bench, m["dirname"])
                responses.append(None)
                continue

            per_item = data["benchmarks"][bench]["per_item"]
            correct = [int(item["correct"]) for item in per_item]
            responses.append(correct)

        lengths = [len(r) for r in responses if r is not None]
        if not lengths:
            continue

        n_items = min(lengths)
        matrix = np.zeros((len(models), n_items), dtype=int)
        valid_mask = np.ones(len(models), dtype=bool)
        for j, r in enumerate(responses):
            if r is None:
                valid_mask[j] = False
            else:
                matrix[j, :n_items] = r[:n_items]

        result["benchmarks"][bench] = {
            "responses": matrix,
            "n_items": n_items,
            "valid_mask": valid_mask,
        }

    return result


def filter_low_variance_items(bench_data: dict, min_variance: float = 0.01) -> dict:
    """Remove items with near-zero response variance (uninformative for IRT).

    Items where all respondents answer identically provide no discrimination
    information. IRT parameters (especially discrimination 'a') cannot be
    estimated for such items.
    """
    matrix = bench_data["responses"]
    valid = bench_data["valid_mask"]
    responses_valid = matrix[valid]

    item_var = responses_valid.var(axis=0)
    keep_mask = item_var >= min_variance
    n_excluded = int((~keep_mask).sum())

    if n_excluded > 0:
        excluded_indices = np.where(~keep_mask)[0].tolist()
        logger.info(
            "Filtered %d/%d items with variance < %.3f (indices: %s...)",
            n_excluded, len(keep_mask), min_variance,
            excluded_indices[:10],
        )
        matrix = matrix[:, keep_mask]
        return {
            "responses": matrix,
            "n_items": int(keep_mask.sum()),
            "valid_mask": bench_data["valid_mask"],
            "excluded_item_indices": excluded_indices,
            "n_excluded": n_excluded,
            "item_keep_mask": keep_mask,
        }

    n_items = bench_data["n_items"]
    return {
        **bench_data,
        "excluded_item_indices": [],
        "n_excluded": 0,
        "item_keep_mask": np.ones(n_items, dtype=bool),
    }


def load_exposure_scores(exposure_file: str | None, benchmarks: dict) -> dict:
    if exposure_file and os.path.exists(exposure_file):
        with open(exposure_file) as f:
            raw = json.load(f)
        exposure = {}
        for bench in benchmarks:
            if bench in raw:
                exposure[bench] = np.array(raw[bench], dtype=float)
            else:
                n_items = benchmarks[bench]["n_items"]
                exposure[bench] = np.ones(n_items)
        return exposure

    exposure = {}
    for bench, bdata in benchmarks.items():
        exposure[bench] = np.ones(bdata["n_items"])
    return exposure


def build_exposure_matrix(dosages: np.ndarray, tau: np.ndarray) -> np.ndarray:
    """Build exposure matrix: exposure[i,j] = dosage[i] * tau[j] / max_dosage."""
    max_d = dosages.max() if dosages.max() > 0 else 1.0
    dosage_norm = dosages / max_d
    return np.outer(dosage_norm, tau)


def generate_synthetic_data(n_models=50, n_items=100, gamma_true=0.5,
                            exposure_rate=0.3, seed=42):
    """Generate synthetic data for sanity checking."""
    rng = np.random.default_rng(seed)
    theta = rng.standard_normal(n_models)
    a = rng.lognormal(0, 0.5, n_items)
    b = rng.standard_normal(n_items)
    c = rng.beta(5, 20, n_items)
    d = rng.beta(20, 5, n_items)
    exposure = rng.binomial(1, exposure_rate, (n_models, n_items)).astype(float)

    from scipy.special import expit
    eta = np.outer(np.ones(n_models), a) * (theta[:, None] - b[None, :]) + gamma_true * exposure
    prob = c[None, :] + (d[None, :] - c[None, :]) * expit(eta)
    y = rng.binomial(1, prob)

    return {
        "y": y,
        "exposure": exposure,
        "true_params": {
            "theta": theta.tolist(),
            "a": a.tolist(),
            "b": b.tolist(),
            "c": c.tolist(),
            "d": d.tolist(),
            "gamma": gamma_true,
        },
        "N_models": n_models,
        "N_items": n_items,
    }


def run_stan_fit(stan_file: str, stan_data: dict, chains: int = 4,
                 iter_sampling: int = 1000, iter_warmup: int = 500,
                 adapt_delta: float = 0.95, max_treedepth: int = 12,
                 seed: int = 42) -> cmdstanpy.CmdStanMCMC:
    model = cmdstanpy.CmdStanModel(stan_file=stan_file)
    fit = model.sample(
        data=stan_data,
        chains=chains,
        iter_warmup=iter_warmup,
        iter_sampling=iter_sampling,
        seed=seed,
        adapt_delta=adapt_delta,
        max_treedepth=max_treedepth,
        parallel_chains=min(chains, 4),
        show_progress=True,
    )
    return fit


def extract_diagnostics(fit: cmdstanpy.CmdStanMCMC) -> dict:
    summary = fit.summary()

    diag_text = fit.diagnose()
    divergent = 0
    for line in diag_text.split('\n'):
        if 'divergent' in line.lower():
            parts = [w for w in line.split() if w.isdigit()]
            if parts:
                divergent = int(parts[0])
                break

    total_draws = fit.chains * fit.num_draws_sampling
    divergent_pct = 100.0 * divergent / total_draws if total_draws > 0 else 0.0

    max_rhat = float(summary['R_hat'].max()) if 'R_hat' in summary.columns else None
    if 'ESS_bulk' in summary.columns:
        min_ess_bulk = float(summary['ESS_bulk'].min())
    elif 'N_Eff' in summary.columns:
        min_ess_bulk = float(summary['N_Eff'].min())
    else:
        min_ess_bulk = None

    return {
        "divergent_count": divergent,
        "divergent_pct": round(divergent_pct, 4),
        "max_rhat": round(max_rhat, 5) if max_rhat else None,
        "min_ess_bulk": round(min_ess_bulk, 1) if min_ess_bulk else None,
        "total_draws": total_draws,
        "chains": fit.chains,
    }


def extract_item_parameters(fit: cmdstanpy.CmdStanMCMC, n_items: int) -> dict:
    a_draws = fit.stan_variable("a")  # shape: (n_draws, n_items)
    b_draws = fit.stan_variable("b")
    c_draws = fit.stan_variable("c")
    d_draws = fit.stan_variable("d")

    items = []
    for j in range(n_items):
        items.append({
            "item_idx": j,
            "a_mean": round(float(np.mean(a_draws[:, j])), 4),
            "a_sd": round(float(np.std(a_draws[:, j])), 4),
            "b_mean": round(float(np.mean(b_draws[:, j])), 4),
            "b_sd": round(float(np.std(b_draws[:, j])), 4),
            "c_mean": round(float(np.mean(c_draws[:, j])), 4),
            "c_sd": round(float(np.std(c_draws[:, j])), 4),
            "d_mean": round(float(np.mean(d_draws[:, j])), 4),
            "d_sd": round(float(np.std(d_draws[:, j])), 4),
        })

    return {"items": items, "n_items": n_items}


def extract_model_parameters(fit: cmdstanpy.CmdStanMCMC, n_models: int,
                             model_info: list[dict] | None = None) -> dict:
    theta_draws = fit.stan_variable("theta")  # (n_draws, n_models)
    gamma_draws = fit.stan_variable("gamma")  # (n_draws,) scalar

    gamma_mean = float(np.mean(gamma_draws))
    gamma_sd = float(np.std(gamma_draws))
    gamma_q025 = float(np.percentile(gamma_draws, 2.5))
    gamma_q975 = float(np.percentile(gamma_draws, 97.5))

    models = []
    for i in range(n_models):
        theta_i = theta_draws[:, i]
        entry = {
            "model_idx": i,
            "theta_mean": round(float(np.mean(theta_i)), 4),
            "theta_sd": round(float(np.std(theta_i)), 4),
            "theta_q025": round(float(np.percentile(theta_i, 2.5)), 4),
            "theta_q975": round(float(np.percentile(theta_i, 97.5)), 4),
        }
        if model_info and i < len(model_info):
            entry["dirname"] = model_info[i]["dirname"]
            entry["model_name"] = model_info[i]["model_name"]
            entry["dosage"] = model_info[i]["dosage"]
        models.append(entry)

    return {
        "gamma": {
            "mean": round(gamma_mean, 4),
            "sd": round(gamma_sd, 4),
            "q025": round(gamma_q025, 4),
            "q975": round(gamma_q975, 4),
            "ci_excludes_zero": bool(gamma_q025 > 0 or gamma_q975 < 0),
        },
        "models": models,
    }


def extract_calibrated_scores(fit: cmdstanpy.CmdStanMCMC, n_models: int,
                              responses: np.ndarray) -> dict:
    cal_draws = fit.stan_variable("calibrated_score")  # (n_draws, n_models)

    raw_scores = responses.mean(axis=1).tolist()
    entries = []
    for i in range(n_models):
        cal_i = cal_draws[:, i]
        entries.append({
            "model_idx": i,
            "raw_accuracy": round(raw_scores[i], 4),
            "calibrated_mean": round(float(np.mean(cal_i)), 4),
            "calibrated_sd": round(float(np.std(cal_i)), 4),
            "calibrated_q025": round(float(np.percentile(cal_i, 2.5)), 4),
            "calibrated_q975": round(float(np.percentile(cal_i, 97.5)), 4),
            "adjustment": round(float(np.mean(cal_i)) - raw_scores[i], 4),
        })

    return {"scores": entries}


def run_synthetic_validation(stan_file: str, output_dir: Path, args):
    logger.info("Generating synthetic data...")
    synth = generate_synthetic_data()
    y = synth["y"]
    exposure = synth["exposure"]
    true = synth["true_params"]

    stan_data = {
        "N_models": synth["N_models"],
        "N_items": synth["N_items"],
        "y": y.tolist(),
        "exposure": exposure.tolist(),
    }

    logger.info("Fitting Stan model (synthetic, %d models x %d items)...",
                synth["N_models"], synth["N_items"])
    t0 = time.time()
    fit = run_stan_fit(
        stan_file, stan_data,
        chains=args.chains,
        iter_sampling=args.iter_sampling,
        adapt_delta=args.adapt_delta,
        max_treedepth=args.max_treedepth,
        seed=args.seed,
    )
    elapsed = time.time() - t0
    logger.info("Sampling done in %.1fs", elapsed)

    # Recovery metrics
    theta_draws = fit.stan_variable("theta")
    theta_post = np.mean(theta_draws, axis=0)
    theta_corr = float(np.corrcoef(theta_post, true["theta"])[0, 1])

    gamma_draws = fit.stan_variable("gamma")
    gamma_mean = float(np.mean(gamma_draws))
    gamma_sd = float(np.std(gamma_draws))

    a_draws = fit.stan_variable("a")
    a_post = np.mean(a_draws, axis=0)
    a_corr = float(np.corrcoef(a_post, true["a"])[0, 1])

    b_draws = fit.stan_variable("b")
    b_post = np.mean(b_draws, axis=0)
    b_corr = float(np.corrcoef(b_post, true["b"])[0, 1])

    diag = extract_diagnostics(fit)

    result = {
        "mode": "synthetic_validation",
        "true_gamma": true["gamma"],
        "estimated_gamma_mean": round(gamma_mean, 4),
        "estimated_gamma_sd": round(gamma_sd, 4),
        "gamma_bias": round(gamma_mean - true["gamma"], 4),
        "gamma_rel_bias": round(abs(gamma_mean - true["gamma"]) / abs(true["gamma"]), 4),
        "theta_corr": round(theta_corr, 4),
        "a_corr": round(a_corr, 4),
        "b_corr": round(b_corr, 4),
        "diagnostics": diag,
        "elapsed_sec": round(elapsed, 1),
    }

    logger.info("Recovery: gamma=%.4f (true=%.4f), theta_corr=%.4f, a_corr=%.4f, b_corr=%.4f",
                gamma_mean, true["gamma"], theta_corr, a_corr, b_corr)
    logger.info("Diagnostics: R-hat=%.4f, divergent=%d (%.2f%%)",
                diag["max_rhat"] or 0, diag["divergent_count"], diag["divergent_pct"])

    output_dir.mkdir(parents=True, exist_ok=True)
    out_file = output_dir / "synthetic_validation.json"
    with open(out_file, "w") as f:
        json.dump(result, f, indent=2)
    logger.info("Saved: %s", out_file)
    return result


def run_real_data(eval_dir: str, stan_file: str, output_dir: Path,
                  exposure_file: str | None, benchmarks_filter: list[str] | None,
                  args):
    data = load_eval_results(eval_dir, benchmarks_filter)
    exposure_scores = load_exposure_scores(exposure_file, data["benchmarks"])
    dosages = data["dosages"]

    output_dir.mkdir(parents=True, exist_ok=True)

    all_results = {
        "mode": "real",
        "eval_dir": eval_dir,
        "stan_model": stan_file,
        "models": [
            {"dirname": m["dirname"], "model_name": m["model_name"],
             "dosage": m["dosage"], "seed": m["seed"]}
            for m in data["models"]
        ],
        "benchmarks": {},
    }

    for bench, bench_data in data["benchmarks"].items():
        min_var = getattr(args, 'min_item_variance', 0.01)
        bench_data = filter_low_variance_items(bench_data, min_variance=min_var)
        n_models = bench_data["responses"].shape[0]
        n_items = bench_data["n_items"]
        responses = bench_data["responses"]
        valid = bench_data["valid_mask"]
        item_keep_mask = bench_data["item_keep_mask"]
        tau_full = exposure_scores[bench]
        tau = tau_full[:len(item_keep_mask)][item_keep_mask]

        # Filter to valid models
        if not valid.all():
            responses = responses[valid]
            dosages_bench = dosages[valid]
            n_models = responses.shape[0]
        else:
            dosages_bench = dosages

        exposure_matrix = build_exposure_matrix(dosages_bench, tau)

        logger.info("=== %s: %d models x %d items ===", bench, n_models, n_items)
        logger.info("Mean accuracy: %.3f", responses.mean())
        logger.info("Dosage range: %d - %d", dosages_bench.min(), dosages_bench.max())

        stan_data = {
            "N_models": int(n_models),
            "N_items": int(n_items),
            "y": responses.tolist(),
            "exposure": exposure_matrix.tolist(),
        }

        t0 = time.time()
        fit = run_stan_fit(
            stan_file, stan_data,
            chains=args.chains,
            iter_sampling=args.iter_sampling,
            adapt_delta=args.adapt_delta,
            max_treedepth=args.max_treedepth,
            seed=args.seed,
        )
        elapsed = time.time() - t0
        logger.info("Sampling done in %.1fs", elapsed)

        diag = extract_diagnostics(fit)
        item_params = extract_item_parameters(fit, n_items)
        model_params = extract_model_parameters(fit, n_models,
                                                [data["models"][i] for i, v in enumerate(valid) if v])
        cal_scores = extract_calibrated_scores(fit, n_models, responses)

        bench_result = {
            "n_models": n_models,
            "n_items": n_items,
            "n_items_excluded": bench_data["n_excluded"],
            "excluded_item_indices": bench_data["excluded_item_indices"],
            "elapsed_sec": round(elapsed, 1),
            "diagnostics": diag,
            "gamma": model_params["gamma"],
            "item_parameters": item_params,
            "model_parameters": model_params["models"],
            "calibrated_scores": cal_scores["scores"],
        }
        all_results["benchmarks"][bench] = bench_result

        logger.info("gamma: mean=%.4f, sd=%.4f, 95%%CI=[%.4f, %.4f]",
                    model_params["gamma"]["mean"], model_params["gamma"]["sd"],
                    model_params["gamma"]["q025"], model_params["gamma"]["q975"])
        logger.info("Diagnostics: R-hat=%.4f, divergent=%d (%.2f%%)",
                    diag["max_rhat"] or 0, diag["divergent_count"], diag["divergent_pct"])

    # Save outputs
    with open(output_dir / "stan_fit_summary.json", "w") as f:
        json.dump(all_results, f, indent=2)

    # Separate files for convenience
    for bench, br in all_results["benchmarks"].items():
        bench_dir = output_dir / bench
        bench_dir.mkdir(parents=True, exist_ok=True)

        with open(bench_dir / "item_parameters.json", "w") as f:
            json.dump(br["item_parameters"], f, indent=2)
        with open(bench_dir / "model_parameters.json", "w") as f:
            json.dump({"gamma": br["gamma"], "models": br["model_parameters"]}, f, indent=2)
        with open(bench_dir / "calibrated_scores.json", "w") as f:
            json.dump(br["calibrated_scores"], f, indent=2)
        with open(bench_dir / "diagnostics.json", "w") as f:
            json.dump(br["diagnostics"], f, indent=2)

    logger.info("Results saved to %s", output_dir)
    return all_results


def main():
    parser = argparse.ArgumentParser(
        description="Bayesian IRT calibration via CmdStanPy (4PL+γ NUTS)")
    parser.add_argument("--eval-dir", type=str,
                        help="Directory with per-model eval subdirectories")
    parser.add_argument("--stan-model", type=str, required=True,
                        help="Path to .stan model file")
    parser.add_argument("--output-dir", type=str, required=True,
                        help="Output directory for results")
    parser.add_argument("--exposure-file", type=str, default=None,
                        help="JSON with per-benchmark exposure scores")
    parser.add_argument("--benchmarks", nargs="*", default=None,
                        help="Benchmarks to analyze (default: all)")
    parser.add_argument("--chains", type=int, default=4)
    parser.add_argument("--iter-sampling", type=int, default=1000)
    parser.add_argument("--iter-warmup", type=int, default=500)
    parser.add_argument("--adapt-delta", type=float, default=0.95)
    parser.add_argument("--max-treedepth", type=int, default=12)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--min-item-variance", type=float, default=0.01,
                        help="Minimum item response variance to keep (default: 0.01)")
    parser.add_argument("--synthetic", action="store_true",
                        help="Run synthetic data validation instead of real data")

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    output_dir = Path(args.output_dir)

    if args.synthetic:
        run_synthetic_validation(args.stan_model, output_dir, args)
    else:
        if not args.eval_dir:
            parser.error("--eval-dir is required when not using --synthetic")
        run_real_data(args.eval_dir, args.stan_model, output_dir,
                      args.exposure_file, args.benchmarks, args)


if __name__ == "__main__":
    main()
