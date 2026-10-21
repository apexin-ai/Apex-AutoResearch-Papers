"""Random 300-item subset Kendall tau baseline for MMLU.

Compares random 300-item selection vs RRF 300-item selection (tau=0.73).
Uses vanilla 2PL IRT, 5 random seeds.
"""
import sys, os, json, logging, time
import numpy as np
from scipy.stats import kendalltau
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
log = logging.getLogger(__name__)

from run_irt_calibration import load_pooled_eval_results, STAN_MODELS
from run_exp006 import compute_ground_truth
import cmdstanpy

EVAL_DIR = '/root/autodl-tmp/exp001/eval_results'
OUTPUT_FILE = '/root/autodl-tmp/exp006/random_300_tau_baseline.json'
SCALES = ['1.5B', '3B']
BENCHMARK = 'mmlu'
N_SUBSET = 300
SEEDS = [42, 123, 456, 789, 1024]

STAN_FILE = STAN_MODELS['vanilla_2pl']

log.info('Loading %s data for scales: %s', BENCHMARK, SCALES)
data = load_pooled_eval_results(
    EVAL_DIR, SCALES,
    benchmarks=[BENCHMARK],
    seed_filter=None, aligned_only=True
)

models = data['models']
dosages = data['dosages']
bench_data = data['benchmarks'][BENCHMARK]
responses = bench_data['responses']
valid = bench_data['valid_mask']

if not valid.all():
    responses = responses[valid]
    dosages = dosages[valid]
    models = [m for m, v in zip(models, valid) if v]

N_models, N_items = responses.shape
log.info('%s: %d models x %d items (full)', BENCHMARK, N_models, N_items)

ground_truth = compute_ground_truth(responses, dosages, models)

log.info('Compiling Stan model: %s', STAN_FILE)
stan_model = cmdstanpy.CmdStanModel(stan_file=STAN_FILE)

seed_results = []
all_taus = []

for seed in SEEDS:
    log.info('=' * 60)
    log.info('SEED %d: sampling %d items from %d', seed, N_SUBSET, N_items)

    rng = np.random.RandomState(seed)
    idx = rng.choice(N_items, size=N_SUBSET, replace=False)
    idx.sort()
    resp_sub = responses[:, idx]

    stan_data = {
        'N_models': int(N_models),
        'N_items': int(N_SUBSET),
        'y': resp_sub.astype(int).tolist(),
    }

    t0 = time.time()
    fit = stan_model.sample(
        data=stan_data, chains=4,
        iter_sampling=1000, iter_warmup=1000,
        adapt_delta=0.95, max_treedepth=12,
        seed=seed, show_progress=True,
    )
    elapsed = time.time() - t0

    cal_mean = np.mean(fit.stan_variable('calibrated_score'), axis=0)
    raw_acc_sub = resp_sub.mean(axis=1)

    tau_cal, p_cal = kendalltau(cal_mean, ground_truth)
    tau_raw, p_raw = kendalltau(raw_acc_sub, ground_truth)

    summary = fit.summary()
    max_rhat = float(summary['R_hat'].max())
    min_ess = float(summary['ESS_bulk'].min())

    result = {
        'seed': seed,
        'n_items': N_SUBSET,
        'tau_calibrated': round(tau_cal, 4),
        'p_calibrated': float(p_cal),
        'tau_raw': round(tau_raw, 4),
        'p_raw': float(p_raw),
        'max_rhat': round(max_rhat, 4),
        'min_ess': round(min_ess, 1),
        'elapsed_seconds': round(elapsed, 1),
        'calibrated_scores': cal_mean.tolist(),
    }
    seed_results.append(result)
    all_taus.append(tau_cal)

    log.info('Seed %d: tau_cal=%.4f (p=%.4e), tau_raw=%.4f, Rhat=%.4f, ESS=%.0f, %.0fs',
             seed, tau_cal, p_cal, tau_raw, max_rhat, min_ess, elapsed)

tau_mean = np.mean(all_taus)
tau_std = np.std(all_taus)

output = {
    'experiment': 'random_300_item_tau_baseline',
    'benchmark': BENCHMARK,
    'scales': SCALES,
    'n_models': N_models,
    'n_items_total': N_items,
    'n_items_subset': N_SUBSET,
    'seeds': SEEDS,
    'model_type': 'vanilla_2pl',
    'summary': {
        'tau_mean': round(tau_mean, 4),
        'tau_std': round(tau_std, 4),
        'tau_values': [round(t, 4) for t in all_taus],
    },
    'per_seed': seed_results,
    'ground_truth': ground_truth.tolist(),
    'models': [
        {
            'name': f"{m['scale']}_d{m['dosage']:03d}_{'s123' if 's123' in m['dirname'] else 's42'}",
            'dosage': m['dosage'],
            'scale': m.get('scale', ''),
            'gt': round(ground_truth[i], 4),
        }
        for i, m in enumerate(models)
    ],
}

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
with open(OUTPUT_FILE, 'w') as f:
    json.dump(output, f, indent=2)
log.info('Results saved to %s', OUTPUT_FILE)

print('\n' + '=' * 70)
print('RANDOM 300-ITEM SUBSET KENDALL TAU BASELINE')
print('=' * 70)
print(f'Benchmark: {BENCHMARK}, Scales: {SCALES}, Models: {N_models}')
print(f'Full items: {N_items}, Subset: {N_SUBSET}')
print(f'Seeds: {SEEDS}')
print()
print(f'{"Seed":<8} {"tau_cal":>8} {"p_cal":>10} {"tau_raw":>8} {"Rhat":>8} {"ESS":>6} {"Time":>6}')
print('-' * 60)
for r in seed_results:
    print(f'{r["seed"]:<8} {r["tau_calibrated"]:>8.4f} {r["p_calibrated"]:>10.4e} '
          f'{r["tau_raw"]:>8.4f} {r["max_rhat"]:>8.4f} {r["min_ess"]:>6.0f} {r["elapsed_seconds"]:>5.0f}s')
print('-' * 60)
print(f'{"Mean":8} {tau_mean:>8.4f}')
print(f'{"Std":8} {tau_std:>8.4f}')
print()
print(f'Random 300 tau: {tau_mean:.4f} +/- {tau_std:.4f}')
print(f'RRF 300 tau:    0.7313 (from unified_baselines_n16)')
print(f'Full items tau: (run compute_vanilla_2pl_tau.py for comparison)')
