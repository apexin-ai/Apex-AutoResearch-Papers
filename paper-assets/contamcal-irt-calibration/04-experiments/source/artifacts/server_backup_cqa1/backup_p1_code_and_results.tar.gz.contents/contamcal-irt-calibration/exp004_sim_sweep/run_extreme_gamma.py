#!/usr/bin/env python3
"""
Extreme gamma sweep: gamma_true ∈ {2.0, 4.0}
Conditions: gamma × AUC{0.70, 0.90} × N{20, 50} × 10 seeds = 80 runs
"""
import sys, time, os
os.environ.setdefault("TMPDIR", "/root/autodl-tmp/tmp_sim")
os.makedirs(os.environ["TMPDIR"], exist_ok=True)

sys.path.insert(0, '/root/contamcal-irt-calibration/exp004_sim_sweep')
import run_sweep
from pathlib import Path

RESULTS_DIR = Path('/root/contamcal-irt-calibration/exp004_sim_sweep/results_extreme_gamma')
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# Patch condition_id to include gamma_true
def patched_condition_id(auc, n_models, gamma_prior_sd, exposure_type):
    return f"g{run_sweep.GAMMA_TRUE}_auc{auc}_n{n_models}_prior{gamma_prior_sd}_{exposure_type}"

run_sweep.condition_id = patched_condition_id
run_sweep.RESULTS_DIR = RESULTS_DIR

CONDITIONS = [
    (0.70, 20, 1.0, "binary"),
    (0.90, 20, 1.0, "binary"),
    (0.70, 50, 1.0, "binary"),
    (0.90, 50, 1.0, "binary"),
]
GAMMA_VALUES = [2.0, 4.0]
SEEDS = list(range(10))

t_start = time.time()
total = len(GAMMA_VALUES) * len(CONDITIONS)
done = 0

for gamma_true in GAMMA_VALUES:
    run_sweep.GAMMA_TRUE = gamma_true
    print(f"\n{'='*60}")
    print(f"GAMMA_TRUE = {gamma_true}")
    print(f"{'='*60}")
    sys.stdout.flush()

    for auc, n_models, prior_sd, exp_type in CONDITIONS:
        done += 1
        cid = patched_condition_id(auc, n_models, prior_sd, exp_type)
        elapsed = time.time() - t_start
        if done > 1:
            eta = elapsed / (done - 1) * (total - done + 1)
            eta_str = f"ETA {eta/3600:.1f}h"
        else:
            eta_str = "ETA ?"
        print(f"\n[{done}/{total}] {cid} ({eta_str})")
        sys.stdout.flush()
        run_sweep.run_condition(auc, n_models, prior_sd, exp_type, SEEDS,
                                parallel_chains=1, resume=True)

total_time = time.time() - t_start
print(f"\n=== EXTREME GAMMA SWEEP COMPLETE ({total_time/3600:.1f}h) ===")
sys.stdout.flush()

run_sweep.aggregate_results()
print("EXTREME_GAMMA_SWEEP_DONE")
sys.stdout.flush()
