"""Random 300-item subset Kendall tau baseline for MMLU (fixed).

Uses the exact same J=16 model set as unified_baselines_n16 (RRF tau=0.7313).
Fixes: excludes Llama models that were incorrectly included via scale filter.
"""
import json, logging, os, sys, time
import numpy as np
from scipy.stats import kendalltau
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cmdstanpy

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
log = logging.getLogger(__name__)

EVAL_DIR = '/root/autodl-tmp/exp001/eval_results'
OUTPUT_FILE = '/root/autodl-tmp/exp006/random_300_tau_baseline_j16_fixed.json'
STAN_FILE = '/root/contamcal-irt-calibration/stan_models/vanilla_2pl.stan'
BENCHMARK = 'mmlu'
N_SUBSET = 300
SEEDS = [42, 123, 456, 789, 1024]

# Exact J=16 model set from unified_baselines_n16 / pooled_irt_vanilla_2pl_n16_fixed
MODEL_DIRS = [
    ('Qwen2.5-1.5B_d000_s123_aligned', '1.5B', 0),
    ('Qwen2.5-1.5B_d000_s42_aligned', '1.5B', 0),
    ('Qwen2.5-1.5B_d005_s123_aligned', '1.5B', 5),
    ('Qwen2.5-1.5B_d005_s42_aligned', '1.5B', 5),
    ('Qwen2.5-1.5B_d025_s123_aligned', '1.5B', 25),
    ('Qwen2.5-1.5B_d025_s42_aligned', '1.5B', 25),
    ('Qwen2.5-1.5B_d100_s123_aligned', '1.5B', 100),
    ('Qwen2.5-1.5B_d100_s42_aligned', '1.5B', 100),
    ('Qwen2.5-3B_d000_s123_aligned', '3B', 0),
    ('Qwen2.5-3B_d000_s42_a32_aligned', '3B', 0),
    ('Qwen2.5-3B_d005_s123_aligned', '3B', 5),
    ('Qwen2.5-3B_d005_s42_a32_aligned', '3B', 5),
    ('Qwen2.5-3B_d025_s123_aligned', '3B', 25),
    ('Qwen2.5-3B_d025_v3_s42_aligned', '3B', 25),
    ('Qwen2.5-3B_d100_a32_s123_aligned', '3B', 100),
    ('Qwen2.5-3B_d100_a32_s42_aligned', '3B', 100),
]

# Load response data
log.info('Loading %s responses for J=%d models', BENCHMARK, len(MODEL_DIRS))
responses_list = []
for dirname, scale, dosage in MODEL_DIRS:
    path = os.path.join(EVAL_DIR, dirname, 'correctness_matrix.json')
    with open(path) as f:
        cm = json.load(f)
    resp = np.array(cm[BENCHMARK], dtype=int)
    responses_list.append(resp)
    log.info('  %s: %d items, acc=%.4f', dirname, len(resp), resp.mean())

N_items = min(len(r) for r in responses_list)
responses = np.array([r[:N_items] for r in responses_list])
N_models = len(MODEL_DIRS)
log.info('Response matrix: %d models x %d items', N_models, N_items)

dosages = np.array([d for _, _, d in MODEL_DIRS])
scales = [s for _, s, _ in MODEL_DIRS]

# Ground truth: d=0 models get raw acc, d>0 get same-scale d=0 mean
raw_acc = responses.mean(axis=1)
ground_truth = np.empty(N_models)
for i in range(N_models):
    if dosages[i] == 0:
        ground_truth[i] = raw_acc[i]
    else:
        same_scale_d0 = [j for j in range(N_models)
                         if dosages[j] == 0 and scales[j] == scales[i]]
        ground_truth[i] = raw_acc[same_scale_d0].mean()

for sc in sorted(set(scales)):
    d0_idx = [j for j in range(N_models) if dosages[j] == 0 and scales[j] == sc]
    log.info('Ground truth [%s]: d0 mean=%.4f (n=%d)', sc, raw_acc[d0_idx].mean(), len(d0_idx))

log.info('Compiling Stan model')
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
    'experiment': 'random_300_item_tau_baseline_j16_fixed',
    'benchmark': BENCHMARK,
    'n_models': N_models,
    'n_items_total': N_items,
    'n_items_subset': N_SUBSET,
    'seeds': SEEDS,
    'model_type': 'vanilla_2pl',
    'model_set': 'unified_baselines_n16 (8x1.5B + 8x3B Qwen, no Llama)',
    'fix_description': 'Excludes Llama-3.2-3B models that were incorrectly included via 3B scale filter',
    'summary': {
        'tau_mean': round(tau_mean, 4),
        'tau_std': round(tau_std, 4),
        'tau_values': [round(t, 4) for t in all_taus],
    },
    'per_seed': seed_results,
    'ground_truth': ground_truth.tolist(),
    'models': [
        {'name': dirname, 'scale': scale, 'dosage': dosage,
         'gt': round(ground_truth[i], 4), 'full_acc': round(float(raw_acc[i]), 4)}
        for i, (dirname, scale, dosage) in enumerate(MODEL_DIRS)
    ],
}

with open(OUTPUT_FILE, 'w') as f:
    json.dump(output, f, indent=2)
log.info('Results saved to %s', OUTPUT_FILE)

print('\n' + '=' * 70)
print('RANDOM 300-ITEM SUBSET KENDALL TAU BASELINE (FIXED J=16)')
print('=' * 70)
print(f'Benchmark: {BENCHMARK}, Models: {N_models} (8x1.5B + 8x3B Qwen)')
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
print(f'Random 300 tau (fixed): {tau_mean:.4f} +/- {tau_std:.4f}')
print(f'RRF 300 tau:            0.7313 (from unified_baselines_n16, B3_Vanilla2PL)')
