"""Wider prior ablation: reproduce ARC v2 pooled fit with wider priors."""
import json, logging, sys, time, os
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from run_irt_calibration import (
    load_pooled_eval_results, prepare_stan_data,
    fit_stan_model, extract_results, check_convergence,
    posterior_predictive_check, STAN_MODELS
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

OUTPUT_DIR = "/root/autodl-tmp/exp006/results_pooled_05B_15B_arc_v2_wider_prior"
# Original exposure from ARC v2 run
ORIG_EXPOSURE = [0.0, 0.02662309302404875, 0.09863496108978687, 0.3052745653958451,
                 0.0, 0.02662309302404875, 0.09863496108978687, 0.3052745653958451]
GT = [0.46928327645051193]*4 + [0.7721843003412969]*4

def main():
    data = load_pooled_eval_results(
        "/root/autodl-tmp/exp001/eval_results",
        scales=["0.5B", "1.5B"],
        benchmarks=["arc_challenge"], aligned_only=True
    )
    bd = data["benchmarks"]["arc_challenge"]
    y = bd["responses"]
    n_models, n_items = y.shape
    log.info("Data: %d models x %d items", n_models, n_items)

    exposure = np.outer(np.array(ORIG_EXPOSURE), np.ones(n_items))
    
    stan_data = prepare_stan_data(y, exposure, "4pl_gamma_wider")
    stan_file = STAN_MODELS["4pl_gamma_wider"]
    
    log.info("Fitting wider prior model...")
    fit, elapsed = fit_stan_model(
        stan_file, stan_data,
        chains=4, iter_warmup=1000, iter_sampling=1000,
        adapt_delta=0.95, max_treedepth=12, seed=42,
    )
    log.info("Sampling done in %.1fs", elapsed)
    
    results = extract_results(fit, y, "4pl_gamma_wider")
    diag = check_convergence(fit)
    ppc = posterior_predictive_check(fit, y)
    
    results["diagnostics"] = diag
    results["posterior_predictive"] = ppc
    results["prior_type"] = "wider"
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    def ser(o):
        if isinstance(o, (np.ndarray, np.integer, np.floating)):
            return o.tolist() if isinstance(o, np.ndarray) else (int(o) if isinstance(o, np.integer) else float(o))
        return o
    with open(os.path.join(OUTPUT_DIR, "irt_4pl_gamma_wider.json"), "w") as f:
        json.dump(results, f, indent=2, default=ser)
    
    # Coverage analysis
    cal = results["calibrated_scores"]
    log.info("\n=== WIDER PRIOR RESULTS ===")
    log.info("gamma: mean=%.4f, sd=%.4f, 95%%CI=[%.4f, %.4f]",
             results["gamma"]["mean"], results["gamma"]["sd"],
             results["gamma"]["q025"], results["gamma"]["q975"])
    
    for i in range(n_models):
        w = cal["q975"][i] - cal["q025"][i]
        covered = "✓" if cal["q025"][i] <= GT[i] <= cal["q975"][i] else "✗"
        log.info("  M%d: %.4f [%.4f, %.4f] w=%.4f GT=%.4f %s",
                 i, cal["mean"][i], cal["q025"][i], cal["q975"][i], w, GT[i], covered)
    
    cov95 = sum(1 for i in range(n_models) if cal["q025"][i] <= GT[i] <= cal["q975"][i]) / n_models
    cov80 = sum(1 for i in range(n_models) if cal["q10"][i] <= GT[i] <= cal["q90"][i]) / n_models
    cov50 = sum(1 for i in range(n_models) if cal["q25"][i] <= GT[i] <= cal["q75"][i]) / n_models
    avg_w = np.mean([cal["q975"][i] - cal["q025"][i] for i in range(n_models)])
    
    log.info("\n=== COVERAGE ===")
    log.info("  Coverage_95: %.3f (original: 0.625)", cov95)
    log.info("  Coverage_80: %.3f (original: 0.250)", cov80)
    log.info("  Coverage_50: %.3f (original: 0.000)", cov50)
    log.info("  Avg CI width: %.4f (original: ~0.068)", avg_w)
    log.info("  Diagnostics: rhat=%.4f, ess=%.1f, div=%d",
             diag["max_rhat"], diag["min_ess"], diag["divergent_count"])

if __name__ == "__main__":
    main()
