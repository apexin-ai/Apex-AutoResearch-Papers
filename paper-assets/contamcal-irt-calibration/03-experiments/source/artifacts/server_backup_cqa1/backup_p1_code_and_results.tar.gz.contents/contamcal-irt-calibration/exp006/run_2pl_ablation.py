"""2PL vs 4PL ablation: IRT-only fits (no baselines) for fast comparison."""
import json, logging, os, sys, time, traceback
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_irt_calibration import (
    load_pooled_eval_results, build_exposure_matrix,
    prepare_stan_data, check_convergence, posterior_predictive_check,
    extract_results, STAN_MODELS,
)
from run_exp006 import load_exp002_signals
import cmdstanpy

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
SIGNALS_DIR = "/root/autodl-tmp/exp002/signals"
OUTPUT_DIR = "/root/autodl-tmp/exp006/results_pooled_05B_15B_2pl_ablation"
BENCHMARKS = ["gsm8k", "arc_challenge", "mmlu"]

def robust_fit(stan_file, stan_data, chains=4, warmup=1000, samples=1000,
               adapt_delta=0.95, max_treedepth=12, seed=42):
    """Fit with retry: if some chains fail, retry with higher adapt_delta."""
    model = cmdstanpy.CmdStanModel(stan_file=stan_file)
    
    for attempt, (ad, td, sd) in enumerate([
        (adapt_delta, max_treedepth, seed),
        (0.99, 14, seed + 1),
        (0.995, 15, seed + 2),
    ]):
        try:
            log.info("Attempt %d: adapt_delta=%.3f, max_treedepth=%d, seed=%d",
                     attempt + 1, ad, td, sd)
            t0 = time.time()
            fit = model.sample(
                data=stan_data, chains=chains,
                iter_warmup=warmup, iter_sampling=samples,
                seed=sd, adapt_delta=ad, max_treedepth=td,
                parallel_chains=min(chains, 4), show_progress=True,
            )
            elapsed = time.time() - t0
            log.info("Sampling completed in %.1fs", elapsed)
            return fit, elapsed
        except RuntimeError as e:
            log.warning("Attempt %d failed: %s", attempt + 1, str(e)[:200])
            if attempt == 2:
                raise
    raise RuntimeError("All attempts failed")


def run_2pl_fit(bench_name, y, exposure):
    """Fit 2PL model for a single benchmark."""
    N_models, N_items = y.shape
    log.info("=== %s: %d models x %d items ===", bench_name, N_models, N_items)
    
    stan_file = STAN_MODELS["2pl_gamma"]
    stan_data = prepare_stan_data(y, exposure, "2pl_gamma")
    
    fit, elapsed = robust_fit(stan_file, stan_data)
    diagnostics = check_convergence(fit)
    ppc = posterior_predictive_check(fit, y)
    results = extract_results(fit, y, "2pl_gamma")
    
    return {
        "benchmark": bench_name, "model_type": "2pl_gamma", "method": "nuts",
        "stan_file": os.path.basename(stan_file),
        "n_models": int(N_models), "n_items": int(N_items),
        "fit_time_sec": round(elapsed, 1),
        "config": {"chains": 4, "warmup": 1000, "samples": 1000,
                   "adapt_delta": 0.95, "max_treedepth": 12},
        "diagnostics": diagnostics,
        "posterior_predictive": ppc,
        "parameters": results,
    }


data = load_pooled_eval_results(
    EVAL_DIR, ["0.5B", "1.5B"], benchmarks=BENCHMARKS,
    seed_filter=42, aligned_only=True)

dosages = data["dosages"]
models = data["models"]
log.info("Models: %d | Benchmarks: %s", len(models), list(data["benchmarks"].keys()))
log.info("Dosages: %s", dosages.tolist())

os.makedirs(OUTPUT_DIR, exist_ok=True)
results = {}

for bench in BENCHMARKS:
    if bench not in data["benchmarks"]:
        log.warning("Benchmark %s not found, skipping", bench)
        continue

    bench_data = data["benchmarks"][bench]
    responses = bench_data["responses"]
    valid = bench_data["valid_mask"]
    n_items = bench_data["n_items"]

    if not valid.all():
        responses = responses[valid]
        dosages_bench = dosages[valid]
        models_bench = [m for m, v in zip(models, valid) if v]
    else:
        dosages_bench = dosages
        models_bench = list(models)

    signal_scores = load_exp002_signals(SIGNALS_DIR, models_bench, bench, pool_mode=True)
    for sc in set(m.get("scale", "") for m in models_bench):
        s_mask = np.array([m.get("scale", "") == sc for m in models_bench])
        d0s_mask = np.array([m["dosage"] == 0 and m.get("scale", "") == sc for m in models_bench])
        if d0s_mask.any():
            bl = float(signal_scores[d0s_mask].mean())
            log.info("D024 delta [%s]: d000 baseline = %.4f", sc, bl)
            signal_scores[s_mask] -= bl
    signal_scores = np.clip(signal_scores, 0, None)

    tau = np.ones(n_items)
    exposure_matrix = build_exposure_matrix(signal_scores, tau)
    log.info("Exposure (D024 delta): %s", signal_scores.tolist())

    bench_dir = os.path.join(OUTPUT_DIR, bench)
    os.makedirs(bench_dir, exist_ok=True)

    log.info("=" * 60)
    log.info("BENCHMARK: %s — fitting 2pl_gamma", bench)
    log.info("=" * 60)
    
    try:
        result_2pl = run_2pl_fit(bench, responses, exposure_matrix)
        with open(os.path.join(bench_dir, "irt_2pl_gamma.json"), "w") as f:
            json.dump(result_2pl, f, indent=2)
        results[bench] = result_2pl

        g = result_2pl["parameters"]["gamma"]
        d = result_2pl["diagnostics"]
        log.info("  2PL gamma: mean=%.4f, sd=%.4f, 95%%CI=[%.4f, %.4f]",
                 g["mean"], g["sd"], g["q025"], g["q975"])
        log.info("  2PL diag: Rhat=%.4f, ESS=%.1f, div=%d",
                 d["max_rhat"] or 0, d["min_ess"] or 0, d["divergent_count"])
    except Exception as e:
        log.error("Failed to fit %s: %s", bench, e)
        traceback.print_exc()
        results[bench] = {"error": str(e)}

# Save summary
summary = {
    "metadata": {
        "models": [{"dirname": m["dirname"], "dosage": m["dosage"], "scale": m.get("scale", "")} for m in models],
        "dosages": dosages.tolist(),
        "signals_dir": SIGNALS_DIR,
    },
    "benchmarks": {}
}
for bench, res in results.items():
    if "error" in res:
        summary["benchmarks"][bench] = {"error": res["error"]}
    else:
        summary["benchmarks"][bench] = {
            "gamma": res["parameters"]["gamma"],
            "diagnostics": res["diagnostics"],
            "calibrated_scores": res["parameters"].get("calibrated_scores", {}),
            "fit_time_sec": res["fit_time_sec"],
        }

with open(os.path.join(OUTPUT_DIR, "2pl_ablation_summary.json"), "w") as f:
    json.dump(summary, f, indent=2)
log.info("Done. Summary: %s", os.path.join(OUTPUT_DIR, "2pl_ablation_summary.json"))
