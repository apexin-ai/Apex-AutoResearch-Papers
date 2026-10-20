import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.metrics import roc_auc_score
from scipy.stats import rankdata

SIGNALS_DIR = Path("/root/autodl-tmp/exp002/signals")
LABELS_DIR = Path("/root/autodl-tmp/exp001/sft_data")
OUT_DIR = Path("/root/contamcal-irt-calibration/figures")
OUT_DIR.mkdir(parents=True, exist_ok=True)

BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge"]
SIGNAL_KEYS = ["s1_embedding", "s2_minkpp", "s4_selfcritique"]
DOSAGES = ["d005", "d025", "d100"]
MODEL_SIZES = ["0.5B", "1.5B", "3B"]

# S1: higher = more contaminated; S2/S4: lower = more contaminated
SIGNAL_FLIP = {"s1_embedding": 1, "s2_minkpp": -1, "s4_selfcritique": -1}

MODEL_DIRS = {
    ("0.5B", "d000"): "Qwen2.5-0.5B_d000_s42",
    ("0.5B", "d005"): "Qwen2.5-0.5B_d005_s42",
    ("0.5B", "d025"): "Qwen2.5-0.5B_d025_s42",
    ("0.5B", "d100"): "Qwen2.5-0.5B_d100_s42",
    ("1.5B", "d000"): "Qwen2.5-1.5B_d000_s42",
    ("1.5B", "d005"): "Qwen2.5-1.5B_d005_s42",
    ("1.5B", "d025"): "Qwen2.5-1.5B_d025_s42",
    ("1.5B", "d100"): "Qwen2.5-1.5B_d100_s42",
    ("3B", "d000"): "Qwen2.5-3B_d000_s42_a32",
    ("3B", "d005"): "Qwen2.5-3B_d005_s42_a32",
    ("3B", "d025"): "Qwen2.5-3B_d025_v3_s42",
    ("3B", "d100"): "Qwen2.5-3B_d100_a32_s42",
}

def load_signals(model_size, dosage, benchmark):
    d = MODEL_DIRS[(model_size, dosage)]
    path = SIGNALS_DIR / d / f"signals_merged_{benchmark}.json"
    if not path.exists():
        return None
    with open(path) as f:
        items = json.load(f)
    result = {}
    for item in items:
        if "index" in item:
            idx = item["index"]
        elif "item_id" in item:
            idx = int(item["item_id"].split("_")[-1])
        else:
            continue
        result[idx] = item
    return result

def load_labels(benchmark, dosage):
    label_dosage = dosage if dosage != "d100" else "d005"
    path = LABELS_DIR / f"contamination_labels_{benchmark}_{label_dosage}.json"
    with open(path) as f:
        data = json.load(f)
    return data["labels"]

def compute_auc(signals_dict, labels, signal_key):
    indices = sorted(set(signals_dict.keys()) & set(range(len(labels))))
    y = np.array([labels[i] for i in indices])
    scores = np.array([signals_dict[i].get(signal_key) for i in indices], dtype=float)
    scores = scores * SIGNAL_FLIP[signal_key]
    valid = ~np.isnan(scores) & ~np.isinf(scores)
    y, scores = y[valid], scores[valid]
    if len(np.unique(y)) < 2:
        return None
    auc = roc_auc_score(y, scores)
    return max(auc, 1 - auc)

def compute_rrf_auc(signals_dict, labels, k=60):
    indices = sorted(set(signals_dict.keys()) & set(range(len(labels))))
    y = np.array([labels[i] for i in indices])

    all_scores = {}
    for sk in SIGNAL_KEYS:
        raw = np.array([signals_dict[i].get(sk) for i in indices], dtype=float)
        raw = raw * SIGNAL_FLIP[sk]
        valid_mask = ~np.isnan(raw) & ~np.isinf(raw)
        if valid_mask.sum() < len(raw) * 0.5:
            continue
        ranks = np.zeros(len(raw))
        ranks[valid_mask] = rankdata(raw[valid_mask])
        score = np.zeros(len(raw))
        score[valid_mask] = 1.0 / (k + ranks[valid_mask])
        all_scores[sk] = score

    if not all_scores:
        return None

    rrf = np.zeros(len(indices))
    for s in all_scores.values():
        rrf += s

    if len(np.unique(y)) < 2:
        return None
    auc = roc_auc_score(y, rrf)
    return max(auc, 1 - auc)

rows = ["S1 Embedding", "S2 Min-K%++", "S4 Self-Critique", "RRF Ensemble"]
signal_map = {"S1 Embedding": "s1_embedding", "S2 Min-K%++": "s2_minkpp", "S4 Self-Critique": "s4_selfcritique"}

data_matrix = np.zeros((len(rows), len(MODEL_SIZES) * len(DOSAGES)))

for ci, (ms, dos) in enumerate([(ms, dos) for ms in MODEL_SIZES for dos in DOSAGES]):
    bench_aucs = {r: [] for r in rows}

    for bench in BENCHMARKS:
        sigs = load_signals(ms, dos, bench)
        if sigs is None:
            print(f"  MISSING: {ms} {dos} {bench}")
            continue
        labels = load_labels(bench, dos)

        for row_name in rows[:3]:
            sk = signal_map[row_name]
            auc = compute_auc(sigs, labels, sk)
            if auc is not None:
                bench_aucs[row_name].append(auc)

        rrf_auc = compute_rrf_auc(sigs, labels)
        if rrf_auc is not None:
            bench_aucs["RRF Ensemble"].append(rrf_auc)

    for ri, row_name in enumerate(rows):
        aucs = bench_aucs[row_name]
        if aucs:
            data_matrix[ri, ci] = np.mean(aucs)
        else:
            data_matrix[ri, ci] = np.nan

    col_label = f"{ms}/{dos}"
    print(f"{col_label}: " + " | ".join(f"{rows[ri]}={data_matrix[ri,ci]:.3f}" for ri in range(len(rows))))

print("\nFull matrix:")
print(data_matrix)

# Plot
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

fig, ax = plt.subplots(figsize=(3.25, 2.8))

im = ax.imshow(data_matrix, cmap='Blues', aspect='auto', vmin=0.4, vmax=1.0)

n_cols = len(MODEL_SIZES) * len(DOSAGES)
for i in range(len(rows)):
    for j in range(n_cols):
        val = data_matrix[i, j]
        if np.isnan(val):
            continue
        bg_norm = (val - 0.4) / 0.6
        text_color = 'white' if bg_norm > 0.6 else 'black'
        weight = 'bold' if val >= 0.55 else 'normal'
        ax.text(j, i, f"{val:.2f}", ha='center', va='center',
                color=text_color, fontsize=7.5, fontweight=weight)

ax.set_xticks(range(n_cols))
ax.set_xticklabels([dos for _ in MODEL_SIZES for dos in DOSAGES], fontsize=7)
ax.set_yticks(range(len(rows)))
ax.set_yticklabels(rows, fontsize=8)

for gi, ms in enumerate(MODEL_SIZES):
    center = gi * 3 + 1
    ax.text(center, -1.4, ms, ha='center', va='center', fontsize=8.5, fontweight='bold')

for gi in range(1, len(MODEL_SIZES)):
    ax.axvline(x=gi * 3 - 0.5, color='white', linewidth=2)

ax.set_title("Detection AUC by Signal, Scale, and Dosage", fontsize=9, pad=18)

cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label("AUC", fontsize=8)
cbar.ax.tick_params(labelsize=7)

ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.tick_params(left=False, bottom=False)

plt.tight_layout()

for ext in ['pdf', 'png']:
    out_path = OUT_DIR / f"fig_signal_heatmap.{ext}"
    fig.savefig(out_path, dpi=300, bbox_inches='tight', pad_inches=0.05)
    print(f"Saved: {out_path} ({out_path.stat().st_size} bytes)")

plt.close()
