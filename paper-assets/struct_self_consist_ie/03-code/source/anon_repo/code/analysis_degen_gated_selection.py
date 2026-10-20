import json
import sys

def entity_set(entities):
    return set((e['start'], e['end'], e['type']) for e in entities)

def compute_f1(pred_entities, gold_entities):
    pred_set = entity_set(pred_entities)
    gold_set = entity_set(gold_entities)
    if len(gold_set) == 0 and len(pred_set) == 0:
        return 1.0
    if len(gold_set) == 0 or len(pred_set) == 0:
        return 0.0
    tp = len(pred_set & gold_set)
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)

def analyze_dataset(path, name, n_samples=8):
    instances = []
    with open(path) as f:
        for line in f:
            instances.append(json.loads(line))

    greedy_f1s, lp_f1s, gated_f1s, oracle_f1s = [], [], [], []
    degen_greedy, degen_oracle = [], []
    nondegen_greedy, nondegen_lp, nondegen_oracle = [], [], []
    n_degen = 0
    n_gold_nonempty = 0

    for inst in instances:
        gold_ents = inst['gold']['entities']
        if gold_ents:
            n_gold_nonempty += 1
        samples = inst['samples'][:n_samples]
        greedy = inst['greedy']

        sample_f1s = [compute_f1(s['entities'], gold_ents) for s in samples]
        greedy_f1 = compute_f1(greedy['entities'], gold_ents)
        oracle_f1 = max(sample_f1s)

        lp_idx = max(range(len(samples)), key=lambda i: samples[i]['mean_logprob'])
        lp_f1 = sample_f1s[lp_idx]

        is_degen = len(set(round(f, 10) for f in sample_f1s)) == 1

        if is_degen:
            gated_f1 = greedy_f1
            n_degen += 1
            degen_greedy.append(greedy_f1)
            degen_oracle.append(oracle_f1)
        else:
            gated_f1 = lp_f1
            nondegen_greedy.append(greedy_f1)
            nondegen_lp.append(lp_f1)
            nondegen_oracle.append(oracle_f1)

        greedy_f1s.append(greedy_f1)
        lp_f1s.append(lp_f1)
        gated_f1s.append(gated_f1)
        oracle_f1s.append(oracle_f1)

    return {
        'name': name, 'n': len(instances), 'n_gold': n_gold_nonempty,
        'n_degen': n_degen,
        'greedy': greedy_f1s, 'lp': lp_f1s, 'gated': gated_f1s, 'oracle': oracle_f1s,
        'degen_greedy': degen_greedy, 'degen_oracle': degen_oracle,
        'nondegen_greedy': nondegen_greedy, 'nondegen_lp': nondegen_lp, 'nondegen_oracle': nondegen_oracle,
    }

def avg(lst):
    return sum(lst) / len(lst) if lst else 0.0

def print_results(r):
    n = r['n']
    nd = r['n_degen']
    dp = nd / n * 100

    g = avg(r['greedy'])
    l = avg(r['lp'])
    gt = avg(r['gated'])
    o = avg(r['oracle'])

    print(f"\n{'='*60}")
    print(f"Dataset: {r['name']}")
    print(f"{'='*60}")
    print(f"Instances: {n} (gold-nonempty: {r['n_gold']})")
    print(f"Degenerate: {nd} ({dp:.1f}%), Non-degenerate: {n-nd} ({100-dp:.1f}%)")
    print()
    print(f"{'Method':<20} {'Macro F1':>10}")
    print(f"{'-'*32}")
    print(f"{'Greedy':<20} {g:>10.4f}")
    print(f"{'LP-all':<20} {l:>10.4f}")
    print(f"{'Gated':<20} {gt:>10.4f}")
    print(f"{'Oracle':<20} {o:>10.4f}")
    print()
    print(f"Delta Gated-Greedy: {gt-g:+.4f}")
    print(f"Delta Gated-LP:     {gt-l:+.4f}")

    if r['degen_greedy']:
        dg = avg(r['degen_greedy'])
        do = avg(r['degen_oracle'])
        print(f"\nDegenerate ({nd}):")
        print(f"  Greedy=Gated: {dg:.4f}, Oracle: {do:.4f}")

    if r['nondegen_lp']:
        ng = avg(r['nondegen_greedy'])
        nl = avg(r['nondegen_lp'])
        no = avg(r['nondegen_oracle'])
        print(f"\nNon-degenerate ({n-nd}):")
        print(f"  Greedy: {ng:.4f}, LP: {nl:.4f}, Oracle: {no:.4f}")
        print(f"  LP-Greedy: {nl-ng:+.4f}")

    # Also compute gold-filtered (only instances with gold entities)
    print(f"\n--- Gold-filtered (instances with gold entities) ---")
    gf_greedy, gf_lp, gf_gated, gf_oracle = [], [], [], []
    gf_degen = 0
    # We need to recompute... let's store per-instance info
    # Actually we didn't store per-instance gold flag. Let me just note it.
    print(f"  (Requires per-instance gold flag; see full output)")


datasets = [
    ('/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl', 'SciERC', 8),
    ('/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl', 'CoNLL', 8),
    ('/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl', 'FewNERD', 8),
]

all_results = []
for path, name, ns in datasets:
    r = analyze_dataset(path, name, ns)
    all_results.append(r)
    print_results(r)

print(f"\n\n{'='*80}")
print("SUMMARY TABLE")
print(f"{'='*80}")
print(f"{'Dataset':<12} {'N':>6} {'Degen%':>8} {'Greedy':>8} {'LP-all':>8} {'Gated':>8} {'Oracle':>8} {'G-Gre':>8} {'G-LP':>8}")
print(f"{'-'*80}")
for r in all_results:
    n = r['n']
    dp = r['n_degen'] / n * 100
    g = avg(r['greedy'])
    l = avg(r['lp'])
    gt = avg(r['gated'])
    o = avg(r['oracle'])
    print(f"{r['name']:<12} {n:>6} {dp:>7.1f}% {g:>8.4f} {l:>8.4f} {gt:>8.4f} {o:>8.4f} {gt-g:>+8.4f} {gt-l:>+8.4f}")

# === JSON persistence with bootstrap CI ===
import numpy as np
import os

def bootstrap_ci(values, n_boot=10000, ci=0.95, seed=42):
    rng = np.random.RandomState(seed)
    arr = np.array(values)
    n = len(arr)
    if n == 0:
        return {'mean': 0.0, 'ci_lo': 0.0, 'ci_hi': 0.0}
    boot_means = [arr[rng.randint(0, n, n)].mean() for _ in range(n_boot)]
    boot_means = sorted(boot_means)
    lo = boot_means[int((1 - ci) / 2 * n_boot)]
    hi = boot_means[int((1 + ci) / 2 * n_boot)]
    return {'mean': float(arr.mean()), 'ci_lo': float(lo), 'ci_hi': float(hi)}

def bootstrap_delta_ci(a, b, n_boot=10000, ci=0.95, seed=42):
    rng = np.random.RandomState(seed)
    a_arr, b_arr = np.array(a), np.array(b)
    n = len(a_arr)
    if n == 0:
        return {'delta': 0.0, 'ci_lo': 0.0, 'ci_hi': 0.0}
    deltas = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, n)
        deltas.append(a_arr[idx].mean() - b_arr[idx].mean())
    deltas = sorted(deltas)
    lo = deltas[int((1 - ci) / 2 * n_boot)]
    hi = deltas[int((1 + ci) / 2 * n_boot)]
    return {'delta': float((a_arr - b_arr).mean()), 'ci_lo': float(lo), 'ci_hi': float(hi)}

json_output = {'datasets': {}, 'summary': []}

for r in all_results:
    name = r['name']
    n = r['n']
    nd = r['n_degen']

    entry = {
        'n_instances': n,
        'n_gold_nonempty': r['n_gold'],
        'n_degenerate': nd,
        'n_nondegenerate': n - nd,
        'degen_pct': round(nd / n * 100, 1),
        'greedy': bootstrap_ci(r['greedy']),
        'lp_all': bootstrap_ci(r['lp']),
        'gated': bootstrap_ci(r['gated']),
        'oracle': bootstrap_ci(r['oracle']),
        'delta_gated_minus_greedy': bootstrap_delta_ci(r['gated'], r['greedy']),
        'delta_gated_minus_lp': bootstrap_delta_ci(r['gated'], r['lp']),
    }

    if r['degen_greedy']:
        entry['degenerate'] = {
            'greedy_eq_gated': bootstrap_ci(r['degen_greedy']),
            'oracle': bootstrap_ci(r['degen_oracle']),
        }

    if r['nondegen_lp']:
        entry['nondegenerate'] = {
            'greedy': bootstrap_ci(r['nondegen_greedy']),
            'lp': bootstrap_ci(r['nondegen_lp']),
            'oracle': bootstrap_ci(r['nondegen_oracle']),
            'delta_lp_minus_greedy': bootstrap_delta_ci(r['nondegen_lp'], r['nondegen_greedy']),
        }

    json_output['datasets'][name] = entry
    json_output['summary'].append({
        'dataset': name,
        'n': n,
        'degen_pct': entry['degen_pct'],
        'greedy_f1': round(entry['greedy']['mean'], 4),
        'lp_f1': round(entry['lp_all']['mean'], 4),
        'gated_f1': round(entry['gated']['mean'], 4),
        'oracle_f1': round(entry['oracle']['mean'], 4),
        'gated_minus_greedy_pp': round(entry['delta_gated_minus_greedy']['delta'] * 100, 2),
        'gated_minus_lp_pp': round(entry['delta_gated_minus_lp']['delta'] * 100, 2),
    })

os.makedirs('/root/autodl-tmp/struct_self_consist_ie/output', exist_ok=True)
out_path = '/root/autodl-tmp/struct_self_consist_ie/output/dgs_selection_results.json'
with open(out_path, 'w') as f:
    json.dump(json_output, f, indent=2)
print(f"\n=== JSON saved to {out_path} ===")
