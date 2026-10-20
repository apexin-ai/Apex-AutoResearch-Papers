import sys, os, json, logging
import numpy as np
from scipy.stats import kendalltau
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
log = logging.getLogger(__name__)

from run_irt_calibration import load_pooled_eval_results, STAN_MODELS
from run_exp006 import compute_ground_truth
import cmdstanpy

EVAL_DIR = '/root/autodl-tmp/exp001/eval_results'
OUTPUT_FILE = '/root/autodl-tmp/exp006/vanilla_2pl_tau_results.json'

results = {}

for bench in ['arc_challenge', 'mmlu', 'gsm8k']:
    log.info('=' * 60)
    log.info('BENCHMARK: %s', bench)
    log.info('=' * 60)
    
    data = load_pooled_eval_results(
        EVAL_DIR, ['0.5B', '1.5B', '3B'],
        benchmarks=[bench],
        seed_filter=None, aligned_only=True
    )
    
    models = data['models']
    dosages = data['dosages']
    
    bench_data = data['benchmarks'][bench]
    responses = bench_data['responses']
    valid = bench_data['valid_mask']
    
    if not valid.all():
        responses = responses[valid]
        dosages_bench = dosages[valid]
        models_bench = [m for m, v in zip(models, valid) if v]
    else:
        dosages_bench = dosages
        models_bench = list(models)
    
    N_models, N_items = responses.shape
    log.info('%s: %d models x %d items', bench, N_models, N_items)
    
    ground_truth = compute_ground_truth(responses, dosages_bench, models_bench)
    
    # Fit vanilla 2PL
    stan_file = STAN_MODELS['vanilla_2pl']
    stan_data = {
        'N_models': int(N_models),
        'N_items': int(N_items),
        'y': responses.astype(int).tolist(),
    }
    
    model = cmdstanpy.CmdStanModel(stan_file=stan_file)
    fit = model.sample(
        data=stan_data, chains=4,
        iter_sampling=1000, iter_warmup=1000,
        adapt_delta=0.95, max_treedepth=12,
        seed=42, show_progress=True,
    )
    
    cal_mean = np.mean(fit.stan_variable('calibrated_score'), axis=0)
    raw_acc = responses.mean(axis=1)
    
    tau_v2pl, p_v2pl = kendalltau(cal_mean, ground_truth)
    tau_raw, p_raw = kendalltau(raw_acc, ground_truth)
    
    # Load ContamCal for comparison if exists
    cc_tau = None
    cc_path = f'/root/autodl-tmp/exp006/results_pooled_n24/{bench}/{bench}/irt_2pl_gamma.json'
    if os.path.exists(cc_path):
        with open(cc_path) as f:
            cc = json.load(f)
        cc_cal = cc["parameters"]["calibrated_scores"]["mean"]
        if len(cc_cal) == N_models:
            tau_cc, p_cc = kendalltau(cc_cal, ground_truth)
            cc_tau = {'tau': round(tau_cc, 4), 'p': p_cc}
    
    # Diagnostics
    summary = fit.summary()
    max_rhat = float(summary['R_hat'].max())
    min_ess = float(summary['ESS_bulk'].min())
    
    results[bench] = {
        'n_models': N_models,
        'n_items': N_items,
        'vanilla_2pl': {
            'tau': round(tau_v2pl, 4),
            'p_value': p_v2pl,
            'calibrated_scores': cal_mean.tolist(),
        },
        'raw_accuracy': {
            'tau': round(tau_raw, 4),
            'p_value': p_raw,
        },
        'contamcal': cc_tau,
        'ground_truth': ground_truth.tolist(),
        'diagnostics': {
            'max_rhat': round(max_rhat, 4),
            'min_ess': round(min_ess, 1),
        },
        'models': [
            {
                'name': f"{m['scale']}_d{m['dosage']:03d}_{'s123' if 's123' in m['dirname'] else 's42'}",
                'gt': round(ground_truth[i], 4),
                'v2pl_cal': round(cal_mean[i], 4),
                'raw': round(raw_acc[i], 4),
            }
            for i, m in enumerate(models_bench)
        ],
    }
    
    log.info('RESULT %s: V2PL tau=%.4f, Raw tau=%.4f, CC tau=%s',
             bench, tau_v2pl, tau_raw, cc_tau)

with open(OUTPUT_FILE, 'w') as f:
    json.dump(results, f, indent=2)
log.info('Results saved to %s', OUTPUT_FILE)

# Print summary table
print('\n' + '=' * 70)
print('VANILLA 2PL KENDALL TAU RESULTS')
print('=' * 70)
for bench, r in results.items():
    cc_str = f"{r['contamcal']['tau']:.4f}" if r['contamcal'] else 'N/A'
    print(f"{bench} (N={r['n_models']}, I={r['n_items']}): "
          f"V2PL={r['vanilla_2pl']['tau']:.4f}, "
          f"Raw={r['raw_accuracy']['tau']:.4f}, "
          f"CC={cc_str}")
    print(f"  Diagnostics: Rhat={r['diagnostics']['max_rhat']:.4f}, ESS={r['diagnostics']['min_ess']:.0f}")
