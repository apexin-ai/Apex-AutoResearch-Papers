#!/usr/bin/env python3
"""Redraw K_eff vs eta_max scatter (main text) with color-coded tier composition."""

import json
import itertools
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pathlib import Path
from scipy.stats import pearsonr
from scipy import stats

ROOT = Path("/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval")
MI_PATH = ROOT / "artifacts/server_backup/results/plan001/mi_matrix/mi_matrix_15models.json"
SCORES_DIR = ROOT / "artifacts/server_backup/results/plan001/individual_scores"
CKPT_FILES = [
    ROOT / "artifacts/server_backup/results/_taxonomy_checkpoint.json",
    ROOT / "artifacts/server_backup/results/_step2v3_checkpoint.json",
]
OUTPUT_DIR = ROOT / "docs/paper/figures"

DATASETS = ["mmlu", "arc_challenge"]
ATTACKS = [
    "prompt_injection", "sycophancy", "score_manipulation",
    "verbosity_bias", "position_bias", "authority_bias",
]
LOCAL_SET = {"qwen2.5-72b", "llama3.1-70b", "mistral-large",
             "qwen2.5-32b", "qwen2.5-14b", "llama3.1-8b"}

LIGHTWEIGHT_SET = LOCAL_SET | {"gpt-4.1-mini", "gpt-4.1-nano", "claude-3-haiku"}

# ── Load MI data ──
print("Loading MI data...")
mi_data = json.load(open(MI_PATH))
MODELS = mi_data["models"]
N = len(MODELS)
mi_matrices = {ds: np.array(mi_data["mi_matrix"][ds]) for ds in DATASETS}
model_idx = {m: i for i, m in enumerate(MODELS)}

# ── Load scores ──
print("Loading scores...")

def _is_valid(s):
    if s.get("error") or s.get("format_error"):
        return False
    return s.get("winner") in ("A", "B", "tie")

def _invert(scores):
    swap = {"A": "B", "B": "A", "tie": "tie"}
    return [{**s, "winner": swap.get(s.get("winner", "tie"), "tie")} for s in scores]

clean = {ds: {} for ds in DATASETS}
attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}
pairs = {}

for ckpt_path in CKPT_FILES:
    if not ckpt_path.exists():
        continue
    with open(ckpt_path) as f:
        data = json.load(f)
    if "pairs" in data and not pairs:
        for ds in DATASETS:
            if ds in data["pairs"]:
                pairs[ds] = data["pairs"][ds][:300]
    for ds in DATASETS:
        for mid, scores in data.get("clean_scores", {}).get(ds, {}).items():
            if mid not in clean[ds]:
                clean[ds][mid] = scores
        for atk in ATTACKS:
            for mid, scores in data.get("attacked_scores", {}).get(ds, {}).get(atk, {}).items():
                if mid not in attacked[ds][atk]:
                    if atk == "position_bias":
                        scores = _invert(scores)
                    attacked[ds][atk][mid] = scores

for mid in MODELS:
    if mid in LOCAL_SET:
        continue
    for ds in DATASETS:
        fp = SCORES_DIR / f"{mid}__{ds}__clean.json"
        if fp.exists() and mid not in clean[ds]:
            clean[ds][mid] = json.load(open(fp)).get("scores", [])
        for atk in ATTACKS:
            fp = SCORES_DIR / f"{mid}__{ds}__{atk}.json"
            if fp.exists() and mid not in attacked[ds][atk]:
                scores = json.load(open(fp)).get("scores", [])
                if atk == "position_bias":
                    scores = _invert(scores)
                attacked[ds][atk][mid] = scores

for ds in DATASETS:
    loaded = set(clean[ds].keys())
    missing = set(MODELS) - loaded
    print(f"  {ds} clean: {len(loaded)} models, missing: {missing}")

# ── Compute individual ASR per model ──
print("Computing individual ASR per model...")

def individual_asr(mid, ds, atk):
    if mid not in clean[ds] or mid not in attacked[ds][atk]:
        return None
    ps = pairs[ds]
    c_scores = clean[ds][mid]
    a_scores = attacked[ds][atk][mid]
    n = min(len(ps), len(c_scores), len(a_scores))
    if n == 0:
        return None
    n_correct = 0
    n_flips = 0
    for i in range(n):
        if not _is_valid(c_scores[i]) or not _is_valid(a_scores[i]):
            continue
        gt = ps[i]["ground_truth_winner"]
        if c_scores[i]["winner"] == gt:
            n_correct += 1
            if a_scores[i]["winner"] != gt:
                n_flips += 1
    if n_correct == 0:
        return 0.0
    return n_flips / n_correct

model_avg_asr = {}
for mid in MODELS:
    asrs = []
    for ds in DATASETS:
        for atk in ATTACKS:
            a = individual_asr(mid, ds, atk)
            if a is not None:
                asrs.append(a)
    if asrs:
        model_avg_asr[mid] = np.mean(asrs)
        print(f"  {mid}: avg ASR = {model_avg_asr[mid]:.4f} ({len(asrs)} conditions)")

# ── K_eff helper ──
def mi_keff(mi_mat, indices):
    K = len(indices)
    if K <= 1:
        return 1.0
    total = 0.0
    for i in indices:
        term = 1.0
        for j in indices:
            if i != j:
                term += np.exp(-2 * mi_mat[i, j])
        total += term
    return total / K

# ── Build panel data (K=3) with tier info ──
print("\n=== K=3 panels ===")
K = 3
combos = list(itertools.combinations(range(N), K))
panel_keff = []
panel_eta = []
panel_n_lightweight = []

for combo in combos:
    jids = [MODELS[i] for i in combo]
    if not all(mid in model_avg_asr for mid in jids):
        continue
    ke = np.mean([mi_keff(mi_matrices[ds], list(combo)) for ds in DATASETS])
    eta = max(model_avg_asr[mid] for mid in jids)
    n_lw = sum(1 for mid in jids if mid in LIGHTWEIGHT_SET)
    panel_keff.append(ke)
    panel_eta.append(eta)
    panel_n_lightweight.append(n_lw)

keff = np.array(panel_keff)
eta = np.array(panel_eta)
n_lw = np.array(panel_n_lightweight)
r_val, p_val = pearsonr(keff, eta)
print(f"  {len(keff)} panels, r={r_val:.4f}, p={p_val:.2e}")
for nl in range(4):
    mask = n_lw == nl
    print(f"  n_lightweight={nl}: {mask.sum()} panels")

# ── Style ──
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
    "mathtext.fontset": "stix",
    "font.size": 9,
    "axes.linewidth": 0.6,
    "axes.edgecolor": "#333333",
})

COLORS = {
    0: "#1B6B5A",   # deep teal — all frontier/mid
    1: "#2E86C1",   # rich blue
    2: "#E9A820",   # warm amber
    3: "#C44536",   # deep coral red — all lightweight
}
LABELS = {
    0: "0 lightweight (frontier/mid only)",
    1: "1 lightweight",
    2: "2 lightweight",
    3: "3 lightweight (all lightweight)",
}
SIZES = {0: 18, 1: 14, 2: 14, 3: 20}
ALPHAS = {0: 0.7, 1: 0.5, 2: 0.5, 3: 0.8}
MARKERS = {0: "o", 1: "o", 2: "s", 3: "D"}

fig, ax = plt.subplots(figsize=(3.3, 2.8))

# Plot each tier group (back to front: 1,2 behind, 0,3 in front)
for nl in [1, 2, 0, 3]:
    mask = n_lw == nl
    if mask.sum() == 0:
        continue
    ax.scatter(keff[mask], eta[mask],
               c=COLORS[nl], marker=MARKERS[nl],
               s=SIZES[nl], alpha=ALPHAS[nl],
               linewidths=0.3, edgecolors="white",
               zorder=2 + nl, rasterized=True)

# OLS regression line + 95% CI
slope, intercept, _, _, se = stats.linregress(keff, eta)
x_line = np.linspace(keff.min(), keff.max(), 200)
y_line = slope * x_line + intercept
ax.plot(x_line, y_line, color='#1A1A2E', linewidth=1.4, zorder=5, linestyle='-')

x_mean = keff.mean()
n_pts = len(keff)
ss_x = np.sum((keff - x_mean)**2)
t_crit = stats.t.ppf(0.975, n_pts - 2)
residuals = eta - (slope * keff + intercept)
s_resid = np.sqrt(np.sum(residuals**2) / (n_pts - 2))
se_pred = s_resid * np.sqrt(1.0/n_pts + (x_line - x_mean)**2 / ss_x)
ax.fill_between(x_line, y_line - t_crit * se_pred, y_line + t_crit * se_pred,
                color='#2E86C1', alpha=0.12, zorder=1)

# Correlation annotation
ax.annotate(f'$r = {r_val:.2f}$',
            xy=(0.03, 0.97), xycoords='axes fraction',
            fontsize=10, fontweight='bold', color='#1A1A2E',
            va='top', ha='left',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#2E86C1', alpha=0.9, linewidth=0.8))
ax.text(0.03, 0.85, f'$n = {n_pts}$ panels',
        transform=ax.transAxes, fontsize=7, color='#555555',
        va='top', ha='left')

# Legend
legend_elements = [
    Line2D([0], [0], marker=MARKERS[nl], color='w',
           markerfacecolor=COLORS[nl], markersize=5,
           markeredgecolor='white', markeredgewidth=0.3,
           label=LABELS[nl])
    for nl in [0, 1, 2, 3]
]
ax.legend(handles=legend_elements, loc='lower right',
          fontsize=5.5, frameon=True, fancybox=True,
          framealpha=0.9, edgecolor='#CCCCCC',
          handletextpad=0.3, borderpad=0.4)

ax.set_xlabel(r'$K_{\mathrm{eff}}$ (diversity)', fontsize=9)
ax.set_ylabel(r'$\eta_{\max}$ (weakest-link vulnerability)', fontsize=9)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(labelsize=7.5)

fig.tight_layout(pad=0.4)
for ext in ("pdf", "png"):
    fig.savefig(OUTPUT_DIR / f"fig_keff_eta_scatter_main.{ext}",
                dpi=300, bbox_inches="tight")
plt.close(fig)
print(f"Saved fig_keff_eta_scatter_main.pdf/png to {OUTPUT_DIR}")
print("Done!")
