import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from itertools import combinations

OUT_DIR = '/root/entrainment_gated_ft/analysis'
DATA_DIR = '/root/entrainment_gated_ft/lm_eval_clean'

# ── Load helpers ──────────────────────────────────────────────────
def load_jsonl(path):
    samples = []
    with open(path) as f:
        for line in f:
            samples.append(json.loads(line))
    return samples

def load_json_samples(path, task='lambada_openai'):
    with open(path) as f:
        d = json.load(f)
    return d['samples'][task]

# ── Load all 6 conditions ────────────────────────────────────────
print("Loading data...")
model_data = {}

model_data['GDN-pure'] = sorted(
    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-GatedDeltaNet-pure.json')),
    key=lambda x: x['doc_id']
)
model_data['GDN-h3-1'] = sorted(
    load_jsonl(os.path.join(DATA_DIR, '1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl')),
    key=lambda x: x['doc_id']
)
model_data['HGRN2-pure'] = sorted(
    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-pure.json')),
    key=lambda x: x['doc_id']
)
model_data['HGRN2-h3-1'] = sorted(
    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-hybrid-3-1.json')),
    key=lambda x: x['doc_id']
)
model_data['RetNet-pure'] = sorted(
    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-RetNet-pure.json')),
    key=lambda x: x['doc_id']
)
model_data['RetNet-h3-1'] = sorted(
    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-RetNet-hybrid-3-1.json')),
    key=lambda x: x['doc_id']
)

for name, samples in model_data.items():
    print(f"  {name}: {len(samples)} samples")

n_samples = len(model_data['GDN-pure'])
ref_ids = [s['doc_id'] for s in model_data['GDN-pure']]
for name, samples in model_data.items():
    assert len(samples) == n_samples, f"{name} has {len(samples)}, expected {n_samples}"
    ids = [s['doc_id'] for s in samples]
    assert ids == ref_ids, f"{name} doc_id mismatch"
print(f"All {n_samples} samples aligned.\n")

# ── Extract acc arrays ───────────────────────────────────────────
acc = {name: np.array([s['acc'] for s in samples]) for name, samples in model_data.items()}

ARCHS = ['GDN', 'HGRN2', 'RetNet']
ARCH_LABELS = {'GDN': 'GatedDeltaNet', 'HGRN2': 'HGRN2', 'RetNet': 'RetNet'}

# ── Per-architecture helped/hurt ─────────────────────────────────
stats = {}
for arch in ARCHS:
    pure = acc[f'{arch}-pure']
    hybrid = acc[f'{arch}-h3-1']
    helped_mask = (pure == 0) & (hybrid == 1)
    hurt_mask = (pure == 1) & (hybrid == 0)
    both_correct = (pure == 1) & (hybrid == 1)
    both_wrong = (pure == 0) & (hybrid == 0)
    
    stats[arch] = {
        'pure_acc': pure.mean(),
        'h31_acc': hybrid.mean(),
        'helped': int(helped_mask.sum()),
        'hurt': int(hurt_mask.sum()),
        'net': int(helped_mask.sum()) - int(hurt_mask.sum()),
        'both_correct': int(both_correct.sum()),
        'both_wrong': int(both_wrong.sum()),
        'helped_set': set(np.where(helped_mask)[0]),
        'hurt_set': set(np.where(hurt_mask)[0]),
    }

# ── Print summary ────────────────────────────────────────────────
print("=" * 70)
print("THREE-ARCHITECTURE LAMBADA PER-EXAMPLE ANALYSIS (pure -> h3-1)")
print("=" * 70)
print(f"{'Arch':<10} {'Pure Acc':>10} {'H3-1 Acc':>10} {'Helped':>8} {'Hurt':>8} {'Net':>8} {'Both✓':>8} {'Both✗':>8}")
print("-" * 70)
for arch in ARCHS:
    s = stats[arch]
    print(f"{arch:<10} {s['pure_acc']:>10.4f} {s['h31_acc']:>10.4f} {s['helped']:>8} {s['hurt']:>8} {s['net']:>+8} {s['both_correct']:>8} {s['both_wrong']:>8}")
print()

# ── Jaccard matrices ─────────────────────────────────────────────
def jaccard(set_a, set_b):
    if len(set_a) == 0 and len(set_b) == 0:
        return 0.0
    return len(set_a & set_b) / len(set_a | set_b)

for category in ['helped', 'hurt']:
    print(f"Jaccard matrix ({category} sets):")
    print(f"{'':>10}", end='')
    for arch in ARCHS:
        print(f"{arch:>10}", end='')
    print()
    for a1 in ARCHS:
        print(f"{a1:>10}", end='')
        for a2 in ARCHS:
            j = jaccard(stats[a1][f'{category}_set'], stats[a2][f'{category}_set'])
            print(f"{j:>10.3f}", end='')
        print()
    print()

# ── Cross-architecture overlap counts ────────────────────────────
for category in ['helped', 'hurt']:
    print(f"Overlap counts ({category}):")
    print(f"{'':>10}", end='')
    for arch in ARCHS:
        print(f"{arch:>10}", end='')
    print()
    for a1 in ARCHS:
        print(f"{a1:>10}", end='')
        for a2 in ARCHS:
            overlap = len(stats[a1][f'{category}_set'] & stats[a2][f'{category}_set'])
            print(f"{overlap:>10}", end='')
        print()
    print()

# ── Upset-style intersection counts ─────────────────────────────
for category in ['helped', 'hurt']:
    sets = {arch: stats[arch][f'{category}_set'] for arch in ARCHS}
    all_union = sets['GDN'] | sets['HGRN2'] | sets['RetNet']
    
    print(f"Set intersection breakdown ({category}, total union={len(all_union)}):")
    # Exclusive to each
    for arch in ARCHS:
        others = set()
        for a2 in ARCHS:
            if a2 != arch:
                others |= sets[a2]
        exclusive = sets[arch] - others
        print(f"  Only {arch}: {len(exclusive)}")
    
    # Pairwise exclusive
    for a1, a2 in combinations(ARCHS, 2):
        third = [a for a in ARCHS if a != a1 and a != a2][0]
        shared_excl = (sets[a1] & sets[a2]) - sets[third]
        print(f"  {a1} ∩ {a2} only: {len(shared_excl)}")
    
    # All three
    all_three = sets['GDN'] & sets['HGRN2'] & sets['RetNet']
    print(f"  All three: {len(all_three)}")
    print()

# ── Visualization ────────────────────────────────────────────────
fig = plt.figure(figsize=(16, 5.5))
gs = gridspec.GridSpec(1, 3, width_ratios=[1.2, 1, 1.2], wspace=0.35)

colors = {'GDN': '#2196F3', 'HGRN2': '#4CAF50', 'RetNet': '#FF9800'}

# Panel A: Helped/Hurt/Net bar chart
ax1 = fig.add_subplot(gs[0])
x = np.arange(len(ARCHS))
w = 0.25
helped_vals = [stats[a]['helped'] for a in ARCHS]
hurt_vals = [-stats[a]['hurt'] for a in ARCHS]
net_vals = [stats[a]['net'] for a in ARCHS]

bars_h = ax1.bar(x - w, helped_vals, w, label='Helped (0→1)', color='#4CAF50', edgecolor='white', linewidth=0.5)
bars_r = ax1.bar(x, hurt_vals, w, label='Hurt (1→0)', color='#F44336', edgecolor='white', linewidth=0.5)
bars_n = ax1.bar(x + w, net_vals, w, label='Net', color=['#2196F3' if n > 0 else '#FF5722' for n in net_vals], edgecolor='white', linewidth=0.5)

for i, (h, r, n) in enumerate(zip(helped_vals, hurt_vals, net_vals)):
    ax1.text(i - w, h + 8, str(h), ha='center', va='bottom', fontsize=8, fontweight='bold')
    ax1.text(i, r - 8, str(-r), ha='center', va='top', fontsize=8, fontweight='bold')
    ax1.text(i + w, n + (8 if n >= 0 else -8), f'{n:+d}', ha='center', 
             va='bottom' if n >= 0 else 'top', fontsize=8, fontweight='bold')

ax1.axhline(0, color='black', linewidth=0.8)
ax1.set_xticks(x)
ax1.set_xticklabels([f'{a}\n({stats[a]["pure_acc"]:.3f}→{stats[a]["h31_acc"]:.3f})' for a in ARCHS], fontsize=9)
ax1.set_ylabel('Number of examples', fontsize=10)
ax1.set_title('(A) Attention effect on LAMBADA (pure → h3-1)', fontsize=11, fontweight='bold')
ax1.legend(fontsize=8, loc='upper left')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Panel B: Jaccard heatmaps (helped + hurt side by side in one panel)
ax2 = fig.add_subplot(gs[1])

jaccard_helped = np.zeros((3, 3))
jaccard_hurt = np.zeros((3, 3))
for i, a1 in enumerate(ARCHS):
    for j, a2 in enumerate(ARCHS):
        jaccard_helped[i, j] = jaccard(stats[a1]['helped_set'], stats[a2]['helped_set'])
        jaccard_hurt[i, j] = jaccard(stats[a1]['hurt_set'], stats[a2]['hurt_set'])

combined = np.zeros((3, 6))
combined[:, :3] = jaccard_helped
combined[:, 3:] = jaccard_hurt

im = ax2.imshow(combined, cmap='YlOrRd', vmin=0, vmax=1, aspect='auto')
for i in range(3):
    for j in range(6):
        val = combined[i, j]
        color = 'white' if val > 0.5 else 'black'
        ax2.text(j, i, f'{val:.2f}', ha='center', va='center', fontsize=9, fontweight='bold', color=color)

ax2.set_xticks(range(6))
ax2.set_xticklabels(ARCHS + ARCHS, fontsize=8, rotation=45, ha='right')
ax2.set_yticks(range(3))
ax2.set_yticklabels(ARCHS, fontsize=9)
ax2.axvline(2.5, color='white', linewidth=2)
ax2.set_title('(B) Jaccard overlap', fontsize=11, fontweight='bold')
ax2.text(1, -0.8, 'Helped', ha='center', fontsize=9, fontstyle='italic', transform=ax2.transData)
ax2.text(4, -0.8, 'Hurt', ha='center', fontsize=9, fontstyle='italic', transform=ax2.transData)
plt.colorbar(im, ax=ax2, shrink=0.8, pad=0.02)

# Panel C: Upset-style stacked bar
ax3 = fig.add_subplot(gs[2])

categories_data = {}
for category in ['helped', 'hurt']:
    sets = {arch: stats[arch][f'{category}_set'] for arch in ARCHS}
    
    only_gdn = sets['GDN'] - sets['HGRN2'] - sets['RetNet']
    only_hgrn2 = sets['HGRN2'] - sets['GDN'] - sets['RetNet']
    only_retnet = sets['RetNet'] - sets['GDN'] - sets['HGRN2']
    gdn_hgrn2 = (sets['GDN'] & sets['HGRN2']) - sets['RetNet']
    gdn_retnet = (sets['GDN'] & sets['RetNet']) - sets['HGRN2']
    hgrn2_retnet = (sets['HGRN2'] & sets['RetNet']) - sets['GDN']
    all_three = sets['GDN'] & sets['HGRN2'] & sets['RetNet']
    
    categories_data[category] = {
        'GDN only': len(only_gdn),
        'HGRN2 only': len(only_hgrn2),
        'RetNet only': len(only_retnet),
        'GDN∩HGRN2': len(gdn_hgrn2),
        'GDN∩RetNet': len(gdn_retnet),
        'HGRN2∩RetNet': len(hgrn2_retnet),
        'All three': len(all_three),
    }

labels = list(categories_data['helped'].keys())
helped_counts = [categories_data['helped'][l] for l in labels]
hurt_counts = [categories_data['hurt'][l] for l in labels]

y = np.arange(len(labels))
h = 0.35
ax3.barh(y + h/2, helped_counts, h, label='Helped', color='#4CAF50', edgecolor='white', linewidth=0.5)
ax3.barh(y - h/2, hurt_counts, h, label='Hurt', color='#F44336', edgecolor='white', linewidth=0.5)

for i, (hc, rc) in enumerate(zip(helped_counts, hurt_counts)):
    if hc > 0:
        ax3.text(hc + 2, i + h/2, str(hc), va='center', fontsize=8)
    if rc > 0:
        ax3.text(rc + 2, i - h/2, str(rc), va='center', fontsize=8)

ax3.set_yticks(y)
ax3.set_yticklabels(labels, fontsize=9)
ax3.set_xlabel('Number of examples', fontsize=10)
ax3.set_title('(C) Set intersection breakdown', fontsize=11, fontweight='bold')
ax3.legend(fontsize=8)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

plt.tight_layout()
for ext in ['png', 'pdf']:
    out_path = os.path.join(OUT_DIR, f'lambada_three_arch_comparison.{ext}')
    fig.savefig(out_path, dpi=200, bbox_inches='tight')
    print(f"Saved: {out_path}")
plt.close()

print("\nDone.")
