import json
import csv
import numpy as np
import sys
sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from evaluation import per_instance_f1

DATA = '/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl'
OUT_CSV = '/root/autodl-tmp/struct_self_consist_ie/analysis_round8/epsilon_sweep.csv'

EPSILONS = [0.01, 0.02, 0.03, 0.05, 0.10, 0.15, 0.20]
N_BOOT = 10000
RNG = np.random.RandomState(42)

# Load data with gold-filtering
instances = []
with open(DATA) as f:
    for line in f:
        rec = json.loads(line)
        if len(rec['gold'].get('entities', [])) == 0:
            continue
        instances.append(rec)

print(f"Gold-filtered instances: {len(instances)}")

# Precompute per-instance values
lp_ranges = []
greedy_f1s = []
lp_best_f1s = []

for rec in instances:
    logprobs = [s['mean_logprob'] for s in rec['samples']]
    lp_range = max(logprobs) - min(logprobs)
    lp_ranges.append(lp_range)

    gold = rec['gold']
    greedy = rec.get('greedy', rec['samples'][0])
    greedy_f1 = per_instance_f1(greedy, gold, 'ner')
    greedy_f1s.append(greedy_f1)

    best_idx = int(np.argmax(logprobs))
    lp_best_f1 = per_instance_f1(rec['samples'][best_idx], gold, 'ner')
    lp_best_f1s.append(lp_best_f1)

lp_ranges = np.array(lp_ranges)
greedy_f1s = np.array(greedy_f1s)
lp_best_f1s = np.array(lp_best_f1s)
deltas = lp_best_f1s - greedy_f1s  # per-instance delta

print(f"Overall LP selection delta: {deltas.mean()*100:.2f} pp")

results = []
for eps in EPSILONS:
    tied = lp_ranges < eps
    tied_frac = tied.mean()
    non_tied = ~tied
    non_tied_n = non_tied.sum()

    if non_tied_n == 0:
        results.append({
            'epsilon': eps,
            'tied_fraction': tied_frac,
            'non_tied_n': 0,
            'non_tied_selection_delta_pp': float('nan'),
            'non_tied_p': float('nan'),
        })
        continue

    nt_deltas = deltas[non_tied]
    sel_delta = nt_deltas.mean() * 100  # pp

    # Bootstrap p-value
    boot_deltas = np.zeros(N_BOOT)
    for b in range(N_BOOT):
        idx = RNG.randint(0, non_tied_n, size=non_tied_n)
        boot_deltas[b] = nt_deltas[idx].mean()
    p_value = (boot_deltas <= 0).mean()

    results.append({
        'epsilon': eps,
        'tied_fraction': tied_frac,
        'non_tied_n': int(non_tied_n),
        'non_tied_selection_delta_pp': sel_delta,
        'non_tied_p': p_value,
    })

    print(f"ε={eps:.2f}: tied={tied_frac:.3f}, non_tied_n={non_tied_n}, "
          f"delta={sel_delta:.2f}pp, p={p_value:.4f}")

# Write CSV
with open(OUT_CSV, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['epsilon', 'tied_fraction', 'non_tied_n',
                                       'non_tied_selection_delta_pp', 'non_tied_p'])
    w.writeheader()
    for r in results:
        w.writerow(r)

print(f"\nCSV saved: {OUT_CSV}")

# Pretty table
print("\n" + "="*75)
print(f"{'ε':>6} | {'tied%':>7} | {'non-tied n':>10} | {'Δ F1 (pp)':>10} | {'p-value':>8}")
print("-"*75)
for r in results:
    p_str = f"{r['non_tied_p']:.4f}" if not np.isnan(r.get('non_tied_p', float('nan'))) else 'N/A'
    d_str = f"{r['non_tied_selection_delta_pp']:.2f}" if not np.isnan(r.get('non_tied_selection_delta_pp', float('nan'))) else 'N/A'
    print(f"{r['epsilon']:>6.2f} | {r['tied_fraction']*100:>6.1f}% | {r['non_tied_n']:>10d} | {d_str:>10} | {p_str:>8}")
print("="*75)
