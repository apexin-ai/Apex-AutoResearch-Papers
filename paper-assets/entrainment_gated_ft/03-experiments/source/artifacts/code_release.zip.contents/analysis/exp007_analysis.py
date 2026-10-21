import json, os, glob, itertools
import numpy as np
from scipy import stats

base = '/root/entrainment_gated_ft/lm_eval_clean/exp007'

# ============================================================
# Step 1: Load all accuracy data
# ============================================================
all_acc = {}
for scale in ['340m', '1.3b']:
    all_acc[scale] = {}
    scale_dir = os.path.join(base, scale)
    for model_dir in sorted(os.listdir(scale_dir)):
        json_files = glob.glob(os.path.join(scale_dir, model_dir, '*.json'))
        for jf in json_files:
            if 'samples' not in jf:
                with open(jf) as f:
                    data = json.load(f)
                r = data.get('results', {}).get('lambada_openai', {})
                acc = r.get('acc,none', None)
                ppl = r.get('perplexity,none', None)
                all_acc[scale][model_dir] = {'acc': acc, 'ppl': ppl}

# ============================================================
# Step 2: Cross-architecture std by attention ratio (340M)
# ============================================================
archs = ['GDN', 'RetNet', 'HGRN2']
ratios_ordered = ['pure', 'h24-1', 'h12-1', 'h6-1', 'h3-1']
attn_layers = {'pure': 0, 'h24-1': 1, 'h12-1': 2, 'h6-1': 4, 'h3-1': 8}

def compute_cross_arch_std(acc_dict, scale):
    std_by_ratio = {}
    acc_by_ratio = {}
    for ratio in ratios_ordered:
        vals = []
        arch_vals = {}
        for arch in archs:
            key = f'{arch}-{ratio}' if ratio != 'pure' else f'{arch}-pure'
            if key in acc_dict[scale]:
                vals.append(acc_dict[scale][key]['acc'])
                arch_vals[arch] = acc_dict[scale][key]['acc']
        if len(vals) >= 2:
            std_by_ratio[ratio] = float(np.std(vals, ddof=0))
            acc_by_ratio[ratio] = arch_vals
    return std_by_ratio, acc_by_ratio

std_340m, acc_340m = compute_cross_arch_std(all_acc, '340m')
std_1_3b, acc_1_3b = compute_cross_arch_std(all_acc, '1.3b')

print("=== 340M Cross-Arch Std ===")
for r in ratios_ordered:
    if r in std_340m:
        vals_str = ', '.join(f'{a}={acc_340m[r][a]:.4f}' for a in archs if a in acc_340m[r])
        print(f"  {r:8s}: std={std_340m[r]:.6f}  ({vals_str})")

print("\n=== 1.3B Cross-Arch Std (from exp-007 data) ===")
for r in ratios_ordered:
    if r in std_1_3b:
        vals_str = ', '.join(f'{a}={acc_1_3b[r][a]:.4f}' for a in archs if a in acc_1_3b[r])
        n_archs = len(acc_1_3b[r])
        print(f"  {r:8s}: std={std_1_3b[r]:.6f}  (n_arch={n_archs}, {vals_str})")

# ============================================================
# Step 3: Spearman rho + exact permutation test for 340M
# ============================================================
# Using all 5 ratios for 340M
attn_values_340m = [attn_layers[r] for r in ratios_ordered if r in std_340m]
std_values_340m = [std_340m[r] for r in ratios_ordered if r in std_340m]

rho_340m, raw_p_340m = stats.spearmanr(attn_values_340m, std_values_340m)

# Exact permutation test (two-tailed, n=5)
n = len(attn_values_340m)
observed_rho = rho_340m
count_extreme = 0
total_perms = 0
for perm in itertools.permutations(std_values_340m):
    r, _ = stats.spearmanr(attn_values_340m, list(perm))
    if abs(r) >= abs(observed_rho):
        count_extreme += 1
    total_perms += 1

perm_p_340m = count_extreme / total_perms

print(f"\n=== 340M Spearman ===")
print(f"  rho={rho_340m:.4f}, raw_p={raw_p_340m:.4f}")
print(f"  exact permutation p={perm_p_340m:.4f} (two-tailed, {total_perms} perms)")

# ============================================================
# Step 3b: Spearman for 1.3B (reference from exp-001)
# ============================================================
ref_1_3b_std = {'pure': 0.024, 'h24-1': 0.016, 'h12-1': 0.014, 'h6-1': 0.006, 'h3-1': 0.005}
attn_ref = [attn_layers[r] for r in ratios_ordered]
std_ref = [ref_1_3b_std[r] for r in ratios_ordered]
rho_1_3b_ref, raw_p_1_3b_ref = stats.spearmanr(attn_ref, std_ref)

count_extreme_ref = 0
total_perms_ref = 0
for perm in itertools.permutations(std_ref):
    r, _ = stats.spearmanr(attn_ref, list(perm))
    if abs(r) >= abs(rho_1_3b_ref):
        count_extreme_ref += 1
    total_perms_ref += 1
perm_p_1_3b_ref = count_extreme_ref / total_perms_ref

print(f"\n=== 1.3B Spearman (exp-001 reference) ===")
print(f"  rho={rho_1_3b_ref:.4f}, perm_p={perm_p_1_3b_ref:.4f}")

# ============================================================
# Step 4: Rebound detection at h3-1
# ============================================================
print("\n=== Rebound Analysis (340M) ===")
# Check if std increases from h6-1 to h3-1
if 'h6-1' in std_340m and 'h3-1' in std_340m:
    delta = std_340m['h3-1'] - std_340m['h6-1']
    rebound = delta > 0
    print(f"  h6-1 std = {std_340m['h6-1']:.6f}")
    print(f"  h3-1 std = {std_340m['h3-1']:.6f}")
    print(f"  delta    = {delta:+.6f}")
    print(f"  rebound  = {rebound}")

# Also check full pattern
print("\n  Full 340M std pattern:")
for r in ratios_ordered:
    if r in std_340m:
        print(f"    {r:8s}: {std_340m[r]:.6f}")

# Check monotonicity
stds_list = [std_340m[r] for r in ratios_ordered]
monotonic_decrease = all(stds_list[i] >= stds_list[i+1] for i in range(len(stds_list)-1))
print(f"  Monotonically decreasing: {monotonic_decrease}")

# ============================================================
# Step 5: Per-example analysis (340M h3-1 vs pure)
# ============================================================
print("\n=== Per-Example Analysis (340M) ===")

def load_samples(path):
    samples = {}
    with open(path) as f:
        for line in f:
            d = json.loads(line)
            doc_id = d.get('doc_id', d.get('idx', None))
            correct = d.get('acc', d.get('exact_match', None))
            if correct is None:
                # Try target field
                target = d.get('target', '')
                filtered = d.get('filtered_resps', [[]])
                if filtered and len(filtered) > 0:
                    correct = 1 if filtered[0][0] == target else 0
            samples[doc_id] = correct
    return samples

def compute_helped_hurt(pure_samples, hybrid_samples):
    helped = set()
    hurt = set()
    common_ids = set(pure_samples.keys()) & set(hybrid_samples.keys())
    for doc_id in common_ids:
        p = pure_samples[doc_id]
        h = hybrid_samples[doc_id]
        if p == 0 and h == 1:
            helped.add(doc_id)
        elif p == 1 and h == 0:
            hurt.add(doc_id)
    return helped, hurt

# For each arch at h3-1, compute helped/hurt vs pure
jaccard_results = {}
helped_sets = {}
hurt_sets = {}

for arch in archs:
    pure_path = os.path.join(base, '340m', f'{arch}-pure', 'samples', 'lambada_openai.jsonl')
    h3_path = os.path.join(base, '340m', f'{arch}-h3-1', 'samples', 'lambada_openai.jsonl')
    
    if os.path.exists(pure_path) and os.path.exists(h3_path):
        pure_s = load_samples(pure_path)
        h3_s = load_samples(h3_path)
        helped, hurt = compute_helped_hurt(pure_s, h3_s)
        helped_sets[arch] = helped
        hurt_sets[arch] = hurt
        frac_helped = len(helped) / len(pure_s)
        frac_hurt = len(hurt) / len(pure_s)
        print(f"  {arch} h3-1 vs pure: helped={len(helped)} ({frac_helped:.4f}), hurt={len(hurt)} ({frac_hurt:.4f}), net={len(helped)-len(hurt)}")

# Cross-arch Jaccard for helped sets
print("\n  Helped Jaccard (340M h3-1):")
arch_pairs = list(itertools.combinations(archs, 2))
jaccard_helped_vals = []
for a1, a2 in arch_pairs:
    if a1 in helped_sets and a2 in helped_sets:
        intersection = len(helped_sets[a1] & helped_sets[a2])
        union = len(helped_sets[a1] | helped_sets[a2])
        jacc = intersection / union if union > 0 else 0
        jaccard_helped_vals.append(jacc)
        print(f"    {a1} vs {a2}: {jacc:.4f} (|∩|={intersection}, |∪|={union})")

print(f"  Mean helped Jaccard: {np.mean(jaccard_helped_vals):.4f}")

# Cross-arch Jaccard for hurt sets
print("\n  Hurt Jaccard (340M h3-1):")
jaccard_hurt_vals = []
for a1, a2 in arch_pairs:
    if a1 in hurt_sets and a2 in hurt_sets:
        intersection = len(hurt_sets[a1] & hurt_sets[a2])
        union = len(hurt_sets[a1] | hurt_sets[a2])
        jacc = intersection / union if union > 0 else 0
        jaccard_hurt_vals.append(jacc)
        print(f"    {a1} vs {a2}: {jacc:.4f} (|∩|={intersection}, |∪|={union})")

print(f"  Mean hurt Jaccard: {np.mean(jaccard_hurt_vals):.4f}")

# Also compute per-example for other ratios to see trend
print("\n=== Per-Example by Ratio (340M) ===")
for ratio in ratios_ordered[1:]:  # skip pure
    print(f"\n  --- {ratio} ---")
    ratio_helped = {}
    ratio_hurt = {}
    for arch in archs:
        pure_path = os.path.join(base, '340m', f'{arch}-pure', 'samples', 'lambada_openai.jsonl')
        hybrid_path = os.path.join(base, '340m', f'{arch}-{ratio}', 'samples', 'lambada_openai.jsonl')
        if os.path.exists(pure_path) and os.path.exists(hybrid_path):
            pure_s = load_samples(pure_path)
            hybrid_s = load_samples(hybrid_path)
            helped, hurt = compute_helped_hurt(pure_s, hybrid_s)
            ratio_helped[arch] = helped
            ratio_hurt[arch] = hurt
    
    # Jaccard for helped
    jacc_h = []
    for a1, a2 in arch_pairs:
        if a1 in ratio_helped and a2 in ratio_helped:
            inter = len(ratio_helped[a1] & ratio_helped[a2])
            union = len(ratio_helped[a1] | ratio_helped[a2])
            j = inter / union if union > 0 else 0
            jacc_h.append(j)
    
    jacc_hu = []
    for a1, a2 in arch_pairs:
        if a1 in ratio_hurt and a2 in ratio_hurt:
            inter = len(ratio_hurt[a1] & ratio_hurt[a2])
            union = len(ratio_hurt[a1] | ratio_hurt[a2])
            j = inter / union if union > 0 else 0
            jacc_hu.append(j)
    
    if jacc_h:
        print(f"    Helped Jaccard: {np.mean(jacc_h):.4f}  ({', '.join(f'{v:.4f}' for v in jacc_h)})")
    if jacc_hu:
        print(f"    Hurt Jaccard:   {np.mean(jacc_hu):.4f}  ({', '.join(f'{v:.4f}' for v in jacc_hu)})")

# ============================================================
# Step 6: Save summary JSON
# ============================================================
summary = {
    'experiment': 'exp-007',
    'task': 'lambada_openai',
    'n_samples': 5153,
    'models': {
        '340m': {k: v for k, v in all_acc['340m'].items()},
        '1.3b': {k: v for k, v in all_acc['1.3b'].items()}
    },
    'cross_arch_std': {
        '340m': {r: round(std_340m[r], 6) for r in ratios_ordered if r in std_340m},
        '1.3b_exp007': {r: round(std_1_3b[r], 6) for r in ratios_ordered if r in std_1_3b},
        '1.3b_exp001_ref': ref_1_3b_std
    },
    'spearman': {
        '340m': {
            'rho': round(rho_340m, 4),
            'raw_p': round(raw_p_340m, 4),
            'perm_p': round(perm_p_340m, 4),
            'n_ratios': len(attn_values_340m)
        },
        '1.3b_exp001_ref': {
            'rho': round(rho_1_3b_ref, 4),
            'perm_p': round(perm_p_1_3b_ref, 4)
        }
    },
    'rebound_analysis': {
        'h6_1_std': round(std_340m.get('h6-1', 0), 6),
        'h3_1_std': round(std_340m.get('h3-1', 0), 6),
        'delta': round(std_340m.get('h3-1', 0) - std_340m.get('h6-1', 0), 6),
        'rebound_detected': std_340m.get('h3-1', 0) > std_340m.get('h6-1', 0),
        'monotonic_decrease': monotonic_decrease
    },
    'per_example': {
        '340m_h3_1': {
            'helped_jaccard_mean': round(np.mean(jaccard_helped_vals), 4) if jaccard_helped_vals else None,
            'hurt_jaccard_mean': round(np.mean(jaccard_hurt_vals), 4) if jaccard_hurt_vals else None,
            'helped_counts': {arch: len(helped_sets[arch]) for arch in helped_sets},
            'hurt_counts': {arch: len(hurt_sets[arch]) for arch in hurt_sets}
        }
    },
    'comparison_with_1_3b': {
        '1.3b_exp010_jaccard_ref': '~0.092-0.100 (helped), ~0.081-0.099 (hurt)',
        'note': '1.3B exp-007 data incomplete (missing GDN h3/h6/h24, RetNet pure); use exp-001 ref for comparison'
    }
}

os.makedirs('/root/entrainment_gated_ft/analysis', exist_ok=True)
with open('/root/entrainment_gated_ft/analysis/exp007_analysis_summary.json', 'w') as f:
    json.dump(summary, f, indent=2)

print("\n\nSaved to /root/entrainment_gated_ft/analysis/exp007_analysis_summary.json")
