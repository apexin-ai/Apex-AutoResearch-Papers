"""Vanilla 2PL Kendall tau on full MMLU items (14k), scales 1.5B+3B only."""
import sys, os, json, logging, time
import numpy as np
from scipy.stats import kendalltau
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
log = logging.getLogger(__name__)

from run_irt_calibration import load_pooled_eval_results
from run_exp006 import compute_ground_truth
import cmdstanpy

EVAL_DIR = '/root/autodl-tmp/exp001/eval_results'
STAN_FILE = '/root/contamcal-irt-calibration/stan_models/vanilla_2pl_noll.stan'
OUTPUT_FILE = '/root/autodl-tmp/exp006/vanilla_2pl_tau_fullitems.json'
SCALES = ['1.5B', '3B']

log.info('Loading MMLU data for scales: %s', SCALES)
data = load_pooled_eval_results(
    EVAL_DIR, SCALES,
    benchmarks=['mmlu'],
    seed_filter=None, aligned_only=True
)

models = data['models']
dosages = data['dosages']
bench_data = data['benchmarks']['mmlu']
responses = bench_data['responses']
valid = bench_data['valid_mask']

if not valid.all():
    responses = responses[valid]
    dosages = dosages[valid]
    models = [m for m, v in zip(models, valid) if v]

N_models, N_items = responses.shape
log.info('MMLU: %d models x %d items', N_models, N_items)

ground_truth = compute_ground_truth(responses, dosages, models)

stan_data = {
    'N_models': int(N_models),
    'N_items': int(N_items),
    'y': responses.astype(int).tolist(),
}

log.info('Compiling Stan model: %s', STAN_FILE)
model = cmdstanpy.CmdStanModel(stan_file=STAN_FILE)

log.info('Starting MCMC sampling...')
t0 = time.time()
fit = model.sample(
    data=stan_data, chains=4,
    iter_sampling=1000, iter_warmup=1000,
    adapt_delta=0.95, max_treedepth=12,
    seed=42, show_progress=True,
)
elapsed = time.time() - t0
log.info('Sampling completed in %.1fs (%.1f min)', elapsed, elapsed / 60)

cal_mean = np.mean(fit.stan_variable('calibrated_score'), axis=0)
raw_acc = responses.mean(axis=1)

tau_v2pl, p_v2pl = kendalltau(cal_mean, ground_truth)
tau_raw, p_raw = kendalltau(raw_acc, ground_truth)

cc_tau = None
cc_path = '/root/autodl-tmp/exp006/results_pooled_n24/mmlu/mmlu/irt_2pl_gamma.json'
if os.path.exists(cc_path):
    with open(cc_path) as f:
        cc = json.load(f)
    cc_cal = cc["parameters"]["calibrated_scores"]["mean"]
    if len(cc_cal) == N_models:
        tau_cc, p_cc = kendalltau(cc_cal, ground_truth)
        cc_tau = {'tau': round(tau_cc, 4), 'p': p_cc}

summary = fit.summary()
max_rhat = float(summary['R_hat'].max())
min_ess = float(summary['ESS_bulk'].min())

results = {
    'mmlu': {
        'n_models': N_models,
        'n_items': N_items,
        'scales': SCALES,
        'vanilla_2pl': {
            'tau': round(tau_v2pl, 4),
            'p_value': float(p_v2pl),
            'calibrated_scores': cal_mean.tolist(),
        },
        'raw_accuracy': {
            'tau': round(tau_raw, 4),
            'p_value': float(p_raw),
        },
        'contamcal': cc_tau,
        'ground_truth': ground_truth.tolist(),
        'diagnostics': {
            'max_rhat': round(max_rhat, 4),
            'min_ess': round(min_ess, 1),
            'elapsed_seconds': round(elapsed, 1),
        },
        'models': [
            {
                'name': f"{m['scale']}_d{m['dosage']:03d}_{'s123' if 's123' in m['dirname'] else 's42'}",
                'gt': round(ground_truth[i], 4),
                'v2pl_cal': round(cal_mean[i], 4),
                'raw': round(raw_acc[i], 4),
            }
            for i, m in enumerate(models)
        ],
    }
}

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
with open(OUTPUT_FILE, 'w') as f:
    json.dump(results, f, indent=2)
log.info('Results saved to %s', OUTPUT_FILE)

r = results['mmlu']
cc_str = f"{r['contamcal']['tau']:.4f}" if r['contamcal'] else 'N/A'
print(f"\n{'='*70}")
print(f"VANILLA 2PL KENDALL TAU - FULL MMLU ({N_items} items)")
print(f"{'='*70}")
print(f"Scales: {SCALES}, Models: {N_models}")
print(f"V2PL tau={r['vanilla_2pl']['tau']:.4f} (p={r['vanilla_2pl']['p_value']:.4e})")
print(f"Raw  tau={r['raw_accuracy']['tau']:.4f} (p={r['raw_accuracy']['p_value']:.4e})")
print(f"CC   tau={cc_str}")
print(f"Diagnostics: Rhat={max_rhat:.4f}, ESS={min_ess:.0f}")
print(f"Time: {elapsed:.0f}s ({elapsed/60:.1f} min)")
