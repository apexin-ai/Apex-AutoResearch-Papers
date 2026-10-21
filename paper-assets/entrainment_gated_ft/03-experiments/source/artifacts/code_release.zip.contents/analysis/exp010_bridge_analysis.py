import json
import os
import csv
import numpy as np
from itertools import combinations, permutations

OUT_DIR = '/root/entrainment_gated_ft/analysis'
DATA_DIR = '/root/entrainment_gated_ft/lm_eval_clean'

ARCHS = ['GDN', 'HGRN2', 'RetNet']
VARIANTS = ['pure', 'h24-1', 'h12-1', 'h6-1', 'h3-1']
ATTN_RATIOS = {
    'pure': 0.0,
    'h24-1': 1/25,
    'h12-1': 1/13,
    'h6-1': 1/7,
    'h3-1': 1/4,
}
VARIANT_LABELS = {
    'pure': '0 (pure)',
    'h24-1': '1/25 (h24-1)',
    'h12-1': '1/13 (h12-1)',
    'h6-1': '1/7 (h6-1)',
    'h3-1': '1/4 (h3-1)',
}

JSON_MAP = {
    ('GDN', 'pure'): '1.3B-100B-GatedDeltaNet-pure.json',
    ('GDN', 'h12-1'): '1.3B-100B-GatedDeltaNet-hybrid-12-1.json',
    ('HGRN2', 'pure'): '1.3B-100B-HGRN2-pure.json',
    ('HGRN2', 'h24-1'): '1.3B-100B-HGRN2-hybrid-24-1.json',
    ('HGRN2', 'h12-1'): '1.3B-100B-HGRN2-hybrid-12-1.json',
    ('HGRN2', 'h6-1'): '1.3B-100B-HGRN2-hybrid-6-1.json',
    ('HGRN2', 'h3-1'): '1.3B-100B-HGRN2-hybrid-3-1.json',
    ('RetNet', 'pure'): '1.3B-100B-RetNet-pure.json',
    ('RetNet', 'h24-1'): '1.3B-100B-RetNet-hybrid-24-1.json',
    ('RetNet', 'h12-1'): '1.3B-100B-RetNet-hybrid-12-1.json',
    ('RetNet', 'h6-1'): '1.3B-100B-RetNet-hybrid-6-1.json',
    ('RetNet', 'h3-1'): '1.3B-100B-RetNet-hybrid-3-1.json',
}

JSONL_MAP = {
    ('GDN', 'h24-1'): '1.3b/GDN-h24-1-logsamples/samples/lambada_openai.jsonl',
    ('GDN', 'h6-1'): '1.3b/GDN-h6-1-logsamples/samples/lambada_openai.jsonl',
    ('GDN', 'h3-1'): '1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl',
}

# ── Load functions ──
def load_json_samples(path, task='lambada_openai'):
    with open(path) as f:
        d = json.load(f)
    return sorted(d['samples'][task], key=lambda x: x['doc_id'])

def load_jsonl(path):
    samples = []
    with open(path) as f:
        for line in f:
            samples.append(json.loads(line))
    return sorted(samples, key=lambda x: x['doc_id'])

# ── Load all per-example data ──
print("Loading per-example LAMBADA data for all 15 models...")
model_acc = {}  # (arch, variant) -> np.array of acc per sample

for arch in ARCHS:
    for var in VARIANTS:
        key = (arch, var)
        if key in JSON_MAP:
            path = os.path.join(DATA_DIR, JSON_MAP[key])
            samples = load_json_samples(path)
        elif key in JSONL_MAP:
            path = os.path.join(DATA_DIR, JSONL_MAP[key])
            samples = load_jsonl(path)
        else:
            print(f"  WARNING: No data for {arch}-{var}")
            continue
        model_acc[key] = np.array([s['acc'] for s in samples])
        print(f"  {arch}-{var}: {len(samples)} samples, acc={model_acc[key].mean():.4f}")

# Verify all have same number of samples
n_samples = len(model_acc[('GDN', 'pure')])
for key, arr in model_acc.items():
    assert len(arr) == n_samples, f"{key} has {len(arr)} samples, expected {n_samples}"
print(f"\nAll models: {n_samples} samples aligned.\n")

# ── A. Aggregate convergence ──
print("=" * 60)
print("A. AGGREGATE CONVERGENCE (cross-architecture std)")
print("=" * 60)

# Load from summary CSV for official numbers
agg_acc = {}
with open(os.path.join(DATA_DIR, 'summary_all_1.3b.csv')) as f:
    reader = csv.DictReader(f)
    for row in reader:
        family = row['model_family']
        variant = row['variant']
        if family in ARCHS:
            agg_acc[(family, variant)] = float(row['lambada_acc'])

cross_arch_std = {}
for var in VARIANTS:
    accs = [agg_acc[(arch, var)] for arch in ARCHS]
    cross_arch_std[var] = np.std(accs, ddof=0)
    print(f"  {VARIANT_LABELS[var]:20s}: accs={[f'{a:.4f}' for a in accs]}, std={cross_arch_std[var]:.6f}")

# ── B. Per-example divergence ──
print("\n" + "=" * 60)
print("B. PER-EXAMPLE DIVERGENCE")
print("=" * 60)

arch_pairs = list(combinations(ARCHS, 2))

results_rows = []

for var in VARIANTS:
    ratio_val = ATTN_RATIOS[var]
    row = {
        'variant': var,
        'attention_ratio': f"{ratio_val:.4f}",
        'cross_arch_std': cross_arch_std[var],
    }

    if var == 'pure':
        # No helped/hurt for pure (it IS the baseline)
        row['mean_jaccard_helped'] = float('nan')
        row['mean_jaccard_hurt'] = float('nan')
        row['mean_net_asymmetry'] = float('nan')
        for pair in arch_pairs:
            pname = f"{pair[0]}_vs_{pair[1]}"
            row[f'jaccard_helped_{pname}'] = float('nan')
            row[f'jaccard_hurt_{pname}'] = float('nan')
            row[f'net_asymmetry_{pname}'] = float('nan')
        results_rows.append(row)
        print(f"\n  {VARIANT_LABELS[var]}: baseline (no helped/hurt)")
        continue

    print(f"\n  {VARIANT_LABELS[var]}:")

    # Compute helped/hurt for each architecture
    helped = {}
    hurt = {}
    net_effect = {}
    for arch in ARCHS:
        pure_acc = model_acc[(arch, 'pure')]
        hybrid_acc = model_acc[(arch, var)]
        h = set(np.where((hybrid_acc == 1) & (pure_acc == 0))[0])
        u = set(np.where((hybrid_acc == 0) & (pure_acc == 1))[0])
        helped[arch] = h
        hurt[arch] = u
        net_effect[arch] = len(h) - len(u)
        print(f"    {arch}: helped={len(h)}, hurt={len(u)}, net={net_effect[arch]:+d}")

    # Pairwise Jaccard and net asymmetry
    jaccard_helped_vals = []
    jaccard_hurt_vals = []
    net_asym_vals = []

    for a1, a2 in arch_pairs:
        pname = f"{a1}_vs_{a2}"

        # Jaccard of helped sets
        h_inter = len(helped[a1] & helped[a2])
        h_union = len(helped[a1] | helped[a2])
        j_h = h_inter / h_union if h_union > 0 else 0.0

        # Jaccard of hurt sets
        u_inter = len(hurt[a1] & hurt[a2])
        u_union = len(hurt[a1] | hurt[a2])
        j_u = u_inter / u_union if u_union > 0 else 0.0

        # Net effect asymmetry
        na = abs(net_effect[a1] - net_effect[a2]) / n_samples

        jaccard_helped_vals.append(j_h)
        jaccard_hurt_vals.append(j_u)
        net_asym_vals.append(na)

        row[f'jaccard_helped_{pname}'] = j_h
        row[f'jaccard_hurt_{pname}'] = j_u
        row[f'net_asymmetry_{pname}'] = na

        print(f"    {pname}: J_helped={j_h:.4f}, J_hurt={j_u:.4f}, net_asym={na:.6f}")

    row['mean_jaccard_helped'] = np.mean(jaccard_helped_vals)
    row['mean_jaccard_hurt'] = np.mean(jaccard_hurt_vals)
    row['mean_net_asymmetry'] = np.mean(net_asym_vals)

    print(f"    MEAN: J_helped={row['mean_jaccard_helped']:.4f}, J_hurt={row['mean_jaccard_hurt']:.4f}, net_asym={row['mean_net_asymmetry']:.6f}")

    results_rows.append(row)

# ── C. Co-evolution test ──
print("\n" + "=" * 60)
print("C. CO-EVOLUTION TEST (Spearman with exact permutation)")
print("=" * 60)

# Use only hybrid variants (4 points: h24-1, h12-1, h6-1, h3-1)
hybrid_vars = [v for v in VARIANTS if v != 'pure']
std_vals = np.array([cross_arch_std[v] for v in hybrid_vars])
jaccard_h_vals = np.array([next(r['mean_jaccard_helped'] for r in results_rows if r['variant'] == v) for v in hybrid_vars])
jaccard_u_vals = np.array([next(r['mean_jaccard_hurt'] for r in results_rows if r['variant'] == v) for v in hybrid_vars])

def spearman_r(x, y):
    from scipy.stats import rankdata
    rx = rankdata(x)
    ry = rankdata(y)
    n = len(x)
    d2 = np.sum((rx - ry) ** 2)
    return 1 - 6 * d2 / (n * (n**2 - 1))

def exact_permutation_pvalue(x, y, n):
    observed_r = spearman_r(x, y)
    count_ge = 0
    total = 0
    for perm in permutations(range(n)):
        y_perm = y[list(perm)]
        r_perm = spearman_r(x, y_perm)
        if abs(r_perm) >= abs(observed_r):
            count_ge += 1
        total += 1
    return observed_r, count_ge / total, total

# Test 1: std vs mean_jaccard_helped
r_sh, p_sh, n_perms = exact_permutation_pvalue(std_vals, jaccard_h_vals, len(hybrid_vars))
print(f"\n  Spearman(cross_arch_std, mean_jaccard_helped):")
print(f"    r = {r_sh:.4f}, p = {p_sh:.4f} (exact, {n_perms} permutations, n={len(hybrid_vars)})")

# Test 2: std vs mean_jaccard_hurt
r_su, p_su, _ = exact_permutation_pvalue(std_vals, jaccard_u_vals, len(hybrid_vars))
print(f"\n  Spearman(cross_arch_std, mean_jaccard_hurt):")
print(f"    r = {r_su:.4f}, p = {p_su:.4f} (exact, {n_perms} permutations, n={len(hybrid_vars)})")

# Also test with all 5 points (including pure with Jaccard=0)
all_std = np.array([cross_arch_std[v] for v in VARIANTS])
all_jh = np.array([r['mean_jaccard_helped'] if not np.isnan(r['mean_jaccard_helped']) else 0.0
                    for r in results_rows])
all_ju = np.array([r['mean_jaccard_hurt'] if not np.isnan(r['mean_jaccard_hurt']) else 0.0
                    for r in results_rows])

r_sh5, p_sh5, n_perms5 = exact_permutation_pvalue(all_std, all_jh, 5)
print(f"\n  Spearman(cross_arch_std, mean_jaccard_helped) [5-point, pure=0]:")
print(f"    r = {r_sh5:.4f}, p = {p_sh5:.4f} (exact, {n_perms5} permutations, n=5)")

r_su5, p_su5, _ = exact_permutation_pvalue(all_std, all_ju, 5)
print(f"\n  Spearman(cross_arch_std, mean_jaccard_hurt) [5-point, pure=0]:")
print(f"    r = {r_su5:.4f}, p = {p_su5:.4f} (exact, {n_perms5} permutations, n=5)")

# ── Save results ──

# CSV
csv_path = os.path.join(OUT_DIR, 'exp010_bridge_results.csv')
fieldnames = ['variant', 'attention_ratio', 'cross_arch_std',
              'mean_jaccard_helped', 'mean_jaccard_hurt', 'mean_net_asymmetry']
for a1, a2 in arch_pairs:
    pname = f"{a1}_vs_{a2}"
    fieldnames.extend([f'jaccard_helped_{pname}', f'jaccard_hurt_{pname}', f'net_asymmetry_{pname}'])

with open(csv_path, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in results_rows:
        writer.writerow(row)
print(f"\nCSV saved: {csv_path}")

# JSON summary
summary = {
    'experiment': 'exp-010',
    'description': 'Convergence-Divergence Bridge: aggregate convergence vs per-example divergence',
    'task': 'lambada_openai',
    'n_samples': int(n_samples),
    'architectures': ARCHS,
    'aggregate_convergence': {
        var: {
            'attention_ratio': ATTN_RATIOS[var],
            'cross_arch_std': float(cross_arch_std[var]),
            'per_arch_acc': {arch: float(agg_acc[(arch, var)]) for arch in ARCHS}
        }
        for var in VARIANTS
    },
    'per_example_divergence': {},
    'co_evolution_tests': {
        '4-point (hybrids only)': {
            'std_vs_jaccard_helped': {'r': float(r_sh), 'p': float(p_sh), 'n': len(hybrid_vars)},
            'std_vs_jaccard_hurt': {'r': float(r_su), 'p': float(p_su), 'n': len(hybrid_vars)},
        },
        '5-point (including pure=0)': {
            'std_vs_jaccard_helped': {'r': float(r_sh5), 'p': float(p_sh5), 'n': 5},
            'std_vs_jaccard_hurt': {'r': float(r_su5), 'p': float(p_su5), 'n': 5},
        },
        'n_permutations_4pt': int(n_perms),
        'n_permutations_5pt': int(n_perms5),
    },
}

for var in VARIANTS:
    if var == 'pure':
        continue
    entry = {'attention_ratio': ATTN_RATIOS[var], 'per_arch': {}, 'pairwise': {}}
    for arch in ARCHS:
        pure_acc = model_acc[(arch, 'pure')]
        hybrid_acc = model_acc[(arch, var)]
        h = set(np.where((hybrid_acc == 1) & (pure_acc == 0))[0])
        u = set(np.where((hybrid_acc == 0) & (pure_acc == 1))[0])
        entry['per_arch'][arch] = {
            'helped': len(h), 'hurt': len(u), 'net': len(h) - len(u)
        }
    for a1, a2 in arch_pairs:
        pname = f"{a1}_vs_{a2}"
        row = next(r for r in results_rows if r['variant'] == var)
        entry['pairwise'][pname] = {
            'jaccard_helped': float(row[f'jaccard_helped_{pname}']),
            'jaccard_hurt': float(row[f'jaccard_hurt_{pname}']),
            'net_asymmetry': float(row[f'net_asymmetry_{pname}']),
        }
    entry['mean_jaccard_helped'] = float(row['mean_jaccard_helped'])
    entry['mean_jaccard_hurt'] = float(row['mean_jaccard_hurt'])
    entry['mean_net_asymmetry'] = float(row['mean_net_asymmetry'])
    summary['per_example_divergence'][var] = entry

json_path = os.path.join(OUT_DIR, 'exp010_bridge_summary.json')
with open(json_path, 'w') as f:
    json.dump(summary, f, indent=2)
print(f"JSON saved: {json_path}")

# ── Human-readable summary ──
print("\n" + "=" * 60)
print("SUMMARY: Convergence-Divergence Bridge")
print("=" * 60)
print(f"\nLAMBADA ({n_samples} samples), 3 architectures: {', '.join(ARCHS)}")
print(f"\n{'Variant':12s} {'Attn ratio':>10s} {'Cross-arch σ':>12s} {'J_helped':>10s} {'J_hurt':>10s} {'Net asym':>10s}")
print("-" * 66)
for row in results_rows:
    jh = f"{row['mean_jaccard_helped']:.4f}" if not np.isnan(row['mean_jaccard_helped']) else "—"
    ju = f"{row['mean_jaccard_hurt']:.4f}" if not np.isnan(row['mean_jaccard_hurt']) else "—"
    na = f"{row['mean_net_asymmetry']:.6f}" if not np.isnan(row['mean_net_asymmetry']) else "—"
    print(f"{row['variant']:12s} {row['attention_ratio']:>10s} {row['cross_arch_std']:12.6f} {jh:>10s} {ju:>10s} {na:>10s}")

print(f"\nCo-evolution (4-point, hybrids only):")
print(f"  std vs J_helped: r={r_sh:.4f}, p={p_sh:.4f}")
print(f"  std vs J_hurt:   r={r_su:.4f}, p={p_su:.4f}")
print(f"\nCo-evolution (5-point, pure Jaccard=0):")
print(f"  std vs J_helped: r={r_sh5:.4f}, p={p_sh5:.4f}")
print(f"  std vs J_hurt:   r={r_su5:.4f}, p={p_su5:.4f}")

# Interpretation
std_trend = "decreasing" if cross_arch_std['h3-1'] < cross_arch_std['pure'] else "increasing"
jh_mean_h31 = next(r['mean_jaccard_helped'] for r in results_rows if r['variant'] == 'h3-1')
print(f"\nInterpretation:")
print(f"  Aggregate: cross-arch std is {std_trend} from pure ({cross_arch_std['pure']:.4f}) to h3-1 ({cross_arch_std['h3-1']:.4f})")
print(f"  Per-example: mean Jaccard of helped sets at h3-1 = {jh_mean_h31:.4f} (low = architectures help different samples)")
print(f"  The equalizer closes the aggregate gap while each architecture's per-example effects remain distinct.")
