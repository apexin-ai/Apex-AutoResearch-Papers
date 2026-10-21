"""
IRT calibration for contamination-aware benchmark score correction.
Fits 4PL+gamma IRT model via CmdStanPy MCMC (NUTS) per benchmark.

Input:
  - Correctness matrix (N_models x N_items): binary 0/1
  - Exposure matrix (N_models x N_items): continuous exposure scores
  OR
  - eval-dir with per-model eval results + per-benchmark exposure scores

Output (per benchmark):
  - Posterior: gamma, theta, item params (a, b, c, d)
  - Calibrated scores (exposure=0 counterfactual) with 50/80/95% CIs
  - Convergence diagnostics (Rhat, ESS, divergences)
  - Posterior predictive checks

Dependencies: cmdstanpy (CmdStan 2.38+), numpy, scipy
"""

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

log = logging.getLogger(__name__)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STAN_MODEL_DIR = "/root/contamcal-irt-calibration/stan_models"
STAN_MODELS = {
    "4pl_gamma": os.path.join(STAN_MODEL_DIR, "contam_irt_4pl_simple.stan"),
    "2pl_gamma": os.path.join(STAN_MODEL_DIR, "contam_irt_2pl_gamma.stan"),
    "vanilla_4pl": os.path.join(STAN_MODEL_DIR, "vanilla_4pl.stan"),
    "4pl_gamma_wider": os.path.join(STAN_MODEL_DIR, "contam_irt_4pl_simple_wider.stan"),
}

DOSAGE_PATTERN = re.compile(
    r"_d(\d+)(?:_(?:v\d+|a(\d+)))?_s(\d+)(?:_a(\d+))?(_para)?(_aligned)?(?:_v\d+)?$"
)


# ── Data Loading ──

def parse_model_dir_name(dirname):
    """Extract model name, dosage, seed from directory like Qwen2.5-0.5B_d025_s42."""
    m = DOSAGE_PATTERN.search(dirname)
    if not m:
        return None
    return {
        "dirname": dirname,
        "model_name": dirname[:m.start()],
        "dosage": int(m.group(1)),
        "seed": int(m.group(3)),
        "is_para": m.group(5) is not None,
        "is_aligned": m.group(6) is not None,
        "has_alpha": m.group(2) is not None or m.group(4) is not None,
    }


def get_train_lr(dirname, checkpoint_dir):
    """Read lr from checkpoint's train_config.json (D076)."""
    ckpt_name = re.sub(r'(_para)?(_aligned)?$', '', dirname)
    config_path = os.path.join(checkpoint_dir, ckpt_name, "train_config.json")
    try:
        with open(config_path) as f:
            return json.load(f).get("lr")
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    # Fallback: eval dir may have version suffix not in checkpoint name
    ckpt_fallback = re.sub(r'_v\d+(?=_s\d+$)', '', ckpt_name)
    if ckpt_fallback != ckpt_name:
        config_path = os.path.join(checkpoint_dir, ckpt_fallback, "train_config.json")
        try:
            with open(config_path) as f:
                return json.load(f).get("lr")
        except (FileNotFoundError, json.JSONDecodeError):
            pass
    return None


def load_matrix(path):
    """Load matrix from .npy, .csv, or .json."""
    ext = os.path.splitext(path)[1].lower()
    if ext == ".npy":
        return np.load(path)
    elif ext == ".csv":
        return np.loadtxt(path, delimiter=",", skiprows=1)
    elif ext == ".json":
        with open(path) as f:
            return np.array(json.load(f))
    raise ValueError(f"Unsupported format: {ext}")


def load_eval_results(eval_dir, benchmarks=None, skip_para=True,
                      model_scale=None, seed_filter=None, aligned_only=False,
                      lr_filter=None, checkpoint_dir=None):
    """Load per-model eval results into response matrices per benchmark."""
    eval_path = Path(eval_dir)
    model_dirs = sorted([
        d for d in eval_path.iterdir()
        if d.is_dir() and (d / "eval_results.json").exists()
    ])

    models = []
    for d in model_dirs:
        info = parse_model_dir_name(d.name)
        if info is None:
            log.warning("Skipping unrecognized dir: %s", d.name)
            continue
        if skip_para and info["is_para"]:
            continue
        if aligned_only and not info.get("is_aligned", False):
            log.info("Skipping non-aligned dir: %s", d.name)
            continue
        if model_scale and model_scale not in d.name:
            log.info("Skipping dir (scale mismatch): %s", d.name)
            continue
        if seed_filter is not None and info["seed"] != seed_filter:
            log.info("Skipping dir (seed mismatch): %s", d.name)
            continue
        # D076: lr filter — exclude checkpoints trained with non-standard lr
        if lr_filter is not None and checkpoint_dir:
            lr = get_train_lr(d.name, checkpoint_dir)
            if lr is None or abs(lr - lr_filter) > 1e-6:
                log.info("Skipping dir (lr=%s, want %.1e): %s",
                         f"{lr/.1e}" if lr is not None else "unknown",
                         lr_filter, d.name)
                continue
        info["path"] = str(d)
        models.append(info)

    # D076: prefer _a32_ (alpha=32) dirs over non-alpha for same (name, dosage, seed, is_para)
    seen = {}
    for m in models:
        key = (m["model_name"], m["dosage"], m["seed"], m["is_para"])
        if key not in seen:
            seen[key] = m
        elif m.get("has_alpha") and not seen[key].get("has_alpha"):
            log.info("Replacing %s with alpha variant %s", seen[key]["dirname"], m["dirname"])
            seen[key] = m
        elif not m.get("has_alpha") and seen[key].get("has_alpha"):
            log.info("Skipping %s (alpha variant %s preferred)", m["dirname"], seen[key]["dirname"])
    if len(seen) < len(models):
        log.info("Dedup: %d -> %d models (alpha preference)", len(models), len(seen))
        models = list(seen.values())

    if not models:
        raise ValueError(f"No valid eval results in {eval_dir}")
    log.info("Found %d model evaluations", len(models))

    with open(Path(models[0]["path"]) / "eval_results.json") as f:
        sample = json.load(f)
    available = list(sample["benchmarks"].keys())
    benchmarks = [b for b in (benchmarks or available) if b in available]
    log.info("Benchmarks: %s", benchmarks)

    result = {
        "models": models,
        "benchmarks": {},
        "dosages": np.array([m["dosage"] for m in models]),
    }

    for bench in benchmarks:
        responses = []
        for m in models:
            with open(Path(m["path"]) / "eval_results.json") as f:
                data = json.load(f)
            if bench not in data["benchmarks"]:
                responses.append(None)
                continue
            per_item = data["benchmarks"][bench]["per_item"]
            responses.append([int(item["correct"]) for item in per_item])

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


def load_exposure_scores(exposure_file, benchmarks_data, model_id=None):
    """Load per-benchmark per-item exposure scores tau.

    Three tau sources:
    1. model_id specified -> extract that model from nested format
    2. Flat {bench: [floats]} -> use directly (aggregated or oracle)
    3. Nested without model_id -> raise ValueError
    """
    if exposure_file and os.path.exists(exposure_file):
        with open(exposure_file) as f:
            raw = json.load(f)

        first_val = next(iter(raw.values()), None) if raw else None
        if isinstance(first_val, dict):
            if "exposure_scores" in first_val:
                raw = {k: v["exposure_scores"] for k, v in raw.items()}
            else:
                if model_id:
                    if model_id not in raw:
                        raise ValueError(
                            f"model_id '{model_id}' not found in exposure file. "
                            f"Available: {list(raw.keys())}")
                    model_data = raw[model_id]
                else:
                    raise ValueError(
                        f"Nested exposure format with models {list(raw.keys())}. "
                        f"Specify --tau-model-id to select one, or use aggregated/oracle tau.")
                inner_val = next(iter(model_data.values()), None)
                if isinstance(inner_val, dict) and "exposure_scores" in inner_val:
                    raw = {b: d["exposure_scores"] for b, d in model_data.items()}
                elif isinstance(inner_val, list):
                    raw = model_data

        exposure = {}
        for bench in benchmarks_data:
            if bench in raw:
                exposure[bench] = np.array(raw[bench], dtype=float)
            else:
                exposure[bench] = np.ones(benchmarks_data[bench]["n_items"])
        return exposure
    return {b: np.ones(bd["n_items"]) for b, bd in benchmarks_data.items()}


def build_exposure_matrix(dosages, tau):
    """Build exposure matrix: exposure[i,j] = dosage[i] * tau[j] / max_dosage."""
    max_d = dosages.max() if dosages.max() > 0 else 1.0
    return np.outer(dosages / max_d, tau)


def load_pooled_eval_results(eval_dir, scales, benchmarks=None,
                              lr_filter=None, lr_filter_scales=None,
                              checkpoint_dir=None, **kwargs):
    """Load and merge eval results across multiple model scales.

    Calls load_eval_results once per scale, tags each model with its scale,
    and stacks response matrices vertically. Items are truncated to the
    minimum count across scales for consistency.
    """
    all_models = []
    all_dosages = []
    bench_accum = {}

    for scale in scales:
        kw = dict(kwargs)
        if lr_filter is not None and checkpoint_dir:
            if lr_filter_scales is None or scale in lr_filter_scales:
                kw["lr_filter"] = lr_filter
                kw["checkpoint_dir"] = checkpoint_dir
        data = load_eval_results(eval_dir, benchmarks, model_scale=scale, **kw)
        log.info("Pool scale %s: %d models, dosages=%s",
                 scale, len(data["models"]), data["dosages"].tolist())
        for m in data["models"]:
            m["scale"] = scale
        all_models.extend(data["models"])
        all_dosages.extend(data["dosages"].tolist())

        for bench, bd in data["benchmarks"].items():
            if bench not in bench_accum:
                bench_accum[bench] = {"n_items": bd["n_items"],
                                      "responses": [], "valid": []}
            bench_accum[bench]["n_items"] = min(
                bench_accum[bench]["n_items"], bd["n_items"])
            bench_accum[bench]["responses"].append(bd["responses"])
            bench_accum[bench]["valid"].append(bd["valid_mask"])

    result_benchmarks = {}
    for bench, acc in bench_accum.items():
        ni = acc["n_items"]
        responses = np.vstack([r[:, :ni] for r in acc["responses"]])
        valid = np.concatenate(acc["valid"])
        result_benchmarks[bench] = {
            "responses": responses, "n_items": ni, "valid_mask": valid,
        }

    return {
        "models": all_models,
        "dosages": np.array(all_dosages),
        "benchmarks": result_benchmarks,
    }



# ── Stan Fitting ──

def prepare_stan_data(y, exposure, model_type="4pl_gamma"):
    """Prepare data dict for Stan model."""
    N_models, N_items = y.shape
    data = {
        "N_models": int(N_models),
        "N_items": int(N_items),
        "y": y.astype(int).tolist(),
    }
    if model_type != "vanilla_4pl":
        data["exposure"] = exposure.tolist()
    return data


def fit_stan_model(stan_file, stan_data, chains=4, iter_warmup=1000,
                   iter_sampling=1000, adapt_delta=0.95, max_treedepth=12,
                   seed=42, parallel_chains=None):
    """Fit Stan model via CmdStanPy NUTS sampler."""
    log.info("Compiling Stan model: %s", os.path.basename(stan_file))
    model = cmdstanpy.CmdStanModel(stan_file=stan_file)

    log.info("Fitting: %d models x %d items, %d chains x %d samples",
             stan_data["N_models"], stan_data["N_items"], chains, iter_sampling)
    t0 = time.time()
    fit = model.sample(
        data=stan_data,
        chains=chains,
        iter_warmup=iter_warmup,
        iter_sampling=iter_sampling,
        seed=seed,
        adapt_delta=adapt_delta,
        max_treedepth=max_treedepth,
        parallel_chains=parallel_chains if parallel_chains is not None else min(chains, 4),
        show_progress=True,
    )
    elapsed = time.time() - t0
    log.info("Sampling completed in %.1fs", elapsed)
    return fit, elapsed




# ── Diagnostics ──

def check_convergence(fit):
    """Check Rhat, ESS, divergences."""
    summary = fit.summary()
    diag = {}

    for col in ["R_hat", "Rhat"]:
        if col in summary.columns:
            diag["max_rhat"] = round(float(summary[col].max()), 4)
            diag["rhat_ok"] = diag["max_rhat"] < 1.01
            break

    for col in ["ESS_bulk", "N_Eff", "N_eff"]:
        if col in summary.columns:
            diag["min_ess"] = round(float(summary[col].min()), 1)
            diag["ess_ok"] = diag["min_ess"] > 400
            break

    diag_text = fit.diagnose()
    divergent = 0
    for line in diag_text.split("\n"):
        if "divergent" in line.lower():
            try:
                nums = [int(w) for w in line.split() if w.isdigit()]
                if nums:
                    divergent = max(divergent, max(nums))
            except ValueError:
                pass
    diag["divergent_count"] = divergent
    diag["divergence_ok"] = divergent == 0

    log.info("Diagnostics: max_rhat=%.4f, min_ess=%.0f, divergences=%d",
             diag.get("max_rhat", 0), diag.get("min_ess", 0), divergent)
    return diag


def posterior_predictive_check(fit, y_obs):
    """Calculate posterior predictive p-value."""
    try:
        y_rep = fit.stan_variable("y_rep")
    except ValueError:
        return {"overall_ppp": "N/A (no y_rep in model)"}

    n_draws = y_rep.shape[0]
    obs_stat = y_obs.mean()
    rep_stats = y_rep.mean(axis=(1, 2)) if y_rep.ndim == 3 else y_rep.mean(axis=1)
    ppp = float((rep_stats >= obs_stat).mean())
    return {
        "overall_ppp": round(ppp, 4),
        "obs_mean": round(float(obs_stat), 4),
        "rep_mean": round(float(rep_stats.mean()), 4),
    }


# ── Result Extraction ──

def _summarize_vector(name, draws):
    """Summarize a 1D posterior sample."""
    return {
        "name": name,
        "mean": round(float(np.mean(draws)), 4),
        "sd": round(float(np.std(draws)), 4),
        "q025": round(float(np.percentile(draws, 2.5)), 4),
        "q10": round(float(np.percentile(draws, 10)), 4),
        "q50": round(float(np.median(draws)), 4),
        "q90": round(float(np.percentile(draws, 90)), 4),
        "q975": round(float(np.percentile(draws, 97.5)), 4),
    }


def extract_results(fit, y_obs, model_type="4pl_gamma"):
    """Extract posterior summaries and calibrated scores."""
    results = {}

    # Gamma
    if model_type != "vanilla_4pl":
        gamma_draws = fit.stan_variable("gamma")
        results["gamma"] = _summarize_vector("gamma", gamma_draws)

    # Theta
    theta_draws = fit.stan_variable("theta")
    results["theta"] = {
        "mean": np.mean(theta_draws, axis=0).tolist(),
        "sd": np.std(theta_draws, axis=0).tolist(),
    }

    # Item params
    for param in ["a", "b"]:
        try:
            draws = fit.stan_variable(param)
            results[param] = {
                "mean": np.mean(draws, axis=0).tolist(),
                "sd": np.std(draws, axis=0).tolist(),
            }
        except ValueError:
            pass

    if model_type in ("4pl_gamma", "4pl_gamma_wider", "vanilla_4pl"):
        for param in ["c", "d"]:
            try:
                draws = fit.stan_variable(param)
                results[param] = {
                    "mean": np.mean(draws, axis=0).tolist(),
                    "sd": np.std(draws, axis=0).tolist(),
                }
            except ValueError:
                pass

    # Calibrated scores (counterfactual exposure=0)
    a_draws = fit.stan_variable("a")
    b_draws = fit.stan_variable("b")
    N_models, N_items = y_obs.shape
    n_draws = theta_draws.shape[0]

    # Compute clean score = 1/N * sum_j ICC(exposure=0)
    # For 2PL+gamma: ICC(exp=0) = sigmoid(a_j * (theta_i - b_j))
    cal_scores = np.zeros((n_draws, N_models))
    for draw in range(n_draws):
        for i in range(N_models):
            total = 0.0
            for j in range(N_items):
                eta_clean = a_draws[draw, j] * (theta_draws[draw, i] - b_draws[draw, j])
                total += 1.0 / (1.0 + np.exp(-eta_clean))
            cal_scores[draw, i] = total / N_items

    results["calibrated_scores"] = {
        "mean": cal_scores.mean(axis=0).tolist(),
        "sd": cal_scores.std(axis=0).tolist(),
        "ci50_lower": np.percentile(cal_scores, 25, axis=0).tolist(),
        "ci50_upper": np.percentile(cal_scores, 75, axis=0).tolist(),
        "ci80_lower": np.percentile(cal_scores, 10, axis=0).tolist(),
        "ci80_upper": np.percentile(cal_scores, 90, axis=0).tolist(),
        "ci95_lower": np.percentile(cal_scores, 2.5, axis=0).tolist(),
        "ci95_upper": np.percentile(cal_scores, 97.5, axis=0).tolist(),
        "raw_scores": y_obs.mean(axis=1).tolist(),
    }

    return results


# ── Standalone Runner ──

def run_benchmark_fit(bench, y, exposure, model_type, args):
    """Fit IRT for a single benchmark and return results dict."""
    stan_file = STAN_MODEL_DIR + "/" + {
        "4pl_gamma": "contam_irt_4pl_simple.stan",
        "2pl_gamma": "contam_irt_2pl_gamma.stan",
        "vanilla_4pl": "vanilla_4pl.stan",
        "4pl_gamma_wider": "contam_irt_4pl_simple_wider.stan",
    }[model_type]

    stan_data = prepare_stan_data(y, exposure, model_type)
    fit, elapsed = fit_stan_model(
        stan_file, stan_data,
        chains=args.chains if hasattr(args, "chains") else 4,
        iter_warmup=args.warmup if hasattr(args, "warmup") else 1000,
        iter_sampling=args.samples if hasattr(args, "samples") else 1000,
        adapt_delta=args.adapt_delta if hasattr(args, "adapt_delta") else 0.95,
        max_treedepth=args.max_treedepth if hasattr(args, "max_treedepth") else 12,
        seed=args.seed if hasattr(args, "seed") else 42,
    )

    diag = check_convergence(fit)
    ppc = posterior_predictive_check(fit, y)
    res = extract_results(fit, y, model_type)

    return {
        "benchmark": bench,
        "model_type": model_type,
        "n_models": y.shape[0],
        "n_items": y.shape[1],
        "fit_time_sec": round(elapsed, 1),
        "diagnostics": diag,
        "posterior_predictive": ppc,
        **res,
    }


def main():
    parser = argparse.ArgumentParser(
        description="IRT calibration for benchmark scores")

    parser.add_argument("--eval-dir", type=str, default=None)
    parser.add_argument("--exposure-file", type=str, default=None,
                        help="Per-item exposure scores JSON (aggregated/oracle)")
    parser.add_argument("--tau-model-id", type=str, default=None,
                        help="Model ID to select from nested exposure file")
    parser.add_argument("--response-matrix", type=str, default=None,
                        help="Direct response matrix file (npy/csv/json)")
    parser.add_argument("--exposure-matrix", type=str, default=None,
                        help="Direct exposure matrix file (same format)")
    parser.add_argument("--benchmarks", nargs="*", default=None)
    parser.add_argument("--benchmark", type=str, default=None,
                        help="Benchmark name (for direct matrix mode)")
    parser.add_argument("--model-type", type=str,
                        choices=list(STAN_MODELS.keys()), default="4pl_gamma")
    parser.add_argument("--model-scale", type=str, default=None,
                        help="Filter to single model scale (e.g. '0.5B')")
    parser.add_argument("--data-seed", type=int, default=None,
                        help="Filter to single data seed (e.g. 42)")
    parser.add_argument("--aligned-only", action="store_true",
                        help="Only load aligned-format eval directories.")
    parser.add_argument("--checkpoint-dir", type=str, default=None,
                        help="Checkpoint dir for lr verification (D076)")
    parser.add_argument("--lr-filter", type=float, default=None,
                        help="Only accept checkpoints with this lr (D076)")
    parser.add_argument("--output-dir", type=str, required=True)

    parser.add_argument("--chains", type=int, default=4)
    parser.add_argument("--warmup", type=int, default=1000)
    parser.add_argument("--samples", type=int, default=1000)
    parser.add_argument("--adapt-delta", type=float, default=0.95)
    parser.add_argument("--max-treedepth", type=int, default=12)
    parser.add_argument("--seed", type=int, default=42)

    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Mode 1: direct matrix input
    if args.response_matrix:
        if not args.exposure_matrix and args.model_type != "vanilla_4pl":
            parser.error("--exposure-matrix required with --response-matrix "
                         "(unless --model-type=vanilla_4pl)")
        y = load_matrix(args.response_matrix).astype(int)
        if args.exposure_matrix:
            exposure = load_matrix(args.exposure_matrix)
            assert y.shape == exposure.shape, (
                f"Shape mismatch: response {y.shape} vs exposure {exposure.shape}")
        else:
            exposure = np.zeros_like(y, dtype=float)
        bench_name = args.benchmark or "benchmark"

        result = run_benchmark_fit(bench_name, y, exposure, args.model_type, args)

        out_path = output_dir / f"{bench_name}_{args.model_type}_results.json"
        with open(out_path, "w") as f:
            json.dump(result, f, indent=2)
        log.info("Results saved to %s", out_path)
        return

    # Mode 2: eval-dir input
    if not args.eval_dir:
        parser.error("Specify --eval-dir or --response-matrix")

    data = load_eval_results(args.eval_dir, args.benchmarks,
                              model_scale=args.model_scale,
                              seed_filter=args.data_seed,
                              aligned_only=args.aligned_only,
                              lr_filter=args.lr_filter,
                              checkpoint_dir=args.checkpoint_dir)
    exposure_scores = load_exposure_scores(args.exposure_file, data["benchmarks"],
                                           model_id=args.tau_model_id)
    dosages = data["dosages"]

    all_results = {
        "mode": "eval_dir",
        "eval_dir": args.eval_dir,
        "model_type": args.model_type,
        "models": [
            {"dirname": m["dirname"], "model_name": m["model_name"],
             "dosage": m["dosage"], "seed": m["seed"]}
            for m in data["models"]
        ],
        "benchmarks": {},
    }

    for bench, bench_data in data["benchmarks"].items():
        responses = bench_data["responses"]
        valid = bench_data["valid_mask"]
        tau = exposure_scores[bench]

        if not valid.all():
            responses = responses[valid]
            dosages_bench = dosages[valid]
        else:
            dosages_bench = dosages

        exposure_matrix = build_exposure_matrix(dosages_bench, tau[:bench_data["n_items"]])
        result = run_benchmark_fit(bench, responses, exposure_matrix, args.model_type, args)
        all_results["benchmarks"][bench] = result

        bench_dir = output_dir / bench
        bench_dir.mkdir(parents=True, exist_ok=True)
        with open(bench_dir / f"{args.model_type}_results.json", "w") as f:
            json.dump(result, f, indent=2)

    with open(output_dir / "irt_calibration_results.json", "w") as f:
        json.dump(all_results, f, indent=2)
    log.info("All results saved to %s", output_dir)


if __name__ == "__main__":
    main()
