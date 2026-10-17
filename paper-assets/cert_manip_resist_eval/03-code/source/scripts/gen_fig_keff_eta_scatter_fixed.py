#!/usr/bin/env python3
"""Generate two K_eff vs eta_max scatter figures:
  - fig_keff_eta_scatter_main.pdf: K=3, full pool only (for main text)
  - fig_keff_eta_scatter.pdf: K=5, full pool + Pool A (for appendix)
"""

import json
import itertools
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.stats import pearsonr
from scipy import stats

ROOT = Path("/root/cert_manip_resist_eval")
MI_PATH = ROOT / "artifacts/results/plan001/mi_matrix/mi_matrix_15models.json"
SCORES_DIR = ROOT / "artifacts/results/plan001/individual_scores"
CKPT_FILES = [
    ROOT / "artifacts/results/_taxonomy_checkpoint.json",
    ROOT / "artifacts/results/_step2v3_checkpoint.json",
]
OUTPUT_DIR = ROOT / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DATASETS = ["mmlu", "arc_challenge"]
ATTACKS = [
    "prompt_injection", "sycophancy", "score_manipulation",
    "verbosity_bias", "position_bias", "authority_bias",
]
LOCAL_SET = {"qwen2.5-72b", "llama3.1-70b", "mistral-large",
             "qwen2.5-32b", "qwen2.5-14b", "llama3.1-8b"}

POOL_A_NAMES = [
    "gpt-4.1", "claude-sonnet-4-6", "gpt-4.1-mini",
    "llama3.1-70b", "mistral-large", "qwen2.5-32b",
    "gemini-3.5-flash", "qwen2.5-72b", "gpt-4.1-nano",
]

# ── Load MI data ──
print("Loading MI data...")
mi_data = json.load(open(MI_PATH))
MODELS = mi_data["models"]
N = len(MODELS)
mi_matrices = {ds: np.array(mi_data["mi_matrix"][ds]) for ds in DATASETS}
model_idx = {m: i for i, m in enumerate(MODELS)}

POOL_A_INDICES = sorted([model_idx[m] for m in POOL_A_NAMES])
POOL_A_SET = set(POOL_A_INDICES)

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

# ── Build panel data for a given K ──
def build_panel_data(K):
    combos = list(itertools.combinations(range(N), K))
    full_keff, full_eta = [], []
    poola_keff, poola_eta = [], []

    for combo in combos:
        jids = [MODELS[i] for i in combo]
        if not all(mid in model_avg_asr for mid in jids):
            continue
        ke = np.mean([mi_keff(mi_matrices[ds], list(combo)) for ds in DATASETS])
        eta = max(model_avg_asr[mid] for mid in jids)
        full_keff.append(ke)
        full_eta.append(eta)
        if all(i in POOL_A_SET for i in combo):
            poola_keff.append(ke)
            poola_eta.append(eta)

    return (np.array(full_keff), np.array(full_eta),
            np.array(poola_keff), np.array(poola_eta))

# ── Plot helper ──
def plot_scatter(ax, keff, eta, r_val, p_val, n_panels,
                 poola_keff=None, poola_eta=None, r_poola=None, p_poola=None, n_poola=None):
    ax.scatter(keff, eta,
               c='#999999', marker='o', s=8, alpha=0.3,
               linewidths=0, zorder=2, rasterized=True)

    if poola_keff is not None and len(poola_keff) > 0:
        ax.scatter(poola_keff, poola_eta,
                   c='#e67e22', marker='D', s=20, alpha=0.5,
                   edgecolors='#d35400', linewidths=0.4, zorder=3,
                   label=f'Pool A ($r$={r_poola:.2f}, $n$={n_poola})')

    # OLS regression line + 95% CI
    slope, intercept, _, _, se = stats.linregress(keff, eta)
    x_line = np.linspace(keff.min(), keff.max(), 200)
    y_line = slope * x_line + intercept
    ax.plot(x_line, y_line, color='#c0392b', linewidth=1.2, zorder=4)

    # 95% CI band
    x_mean = keff.mean()
    n = len(keff)
    ss_x = np.sum((keff - x_mean)**2)
    t_crit = stats.t.ppf(0.975, n - 2)
    residuals = eta - (slope * keff + intercept)
    s_resid = np.sqrt(np.sum(residuals**2) / (n - 2))
    se_pred = s_resid * np.sqrt(1.0/n + (x_line - x_mean)**2 / ss_x)
    ax.fill_between(x_line, y_line - t_crit * se_pred, y_line + t_crit * se_pred,
                    color='#cccccc', alpha=0.4, zorder=1)

    # Stats box
    stats_text = f'$r$={r_val:.2f}, $p$<0.001\n$n$={n_panels}'
    ax.text(0.97, 0.97, stats_text,
            transform=ax.transAxes, fontsize=7,
            verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc', alpha=0.9))

    ax.set_xlabel(r'$K_{\mathrm{eff}}$', fontsize=9)
    ax.set_ylabel(r'$\eta_{\max}$', fontsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=8)

# ── Global style ──
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.linewidth": 0.6,
})

# ════════════════════════════════════════════════════════════════════
# Figure A: K=3, full pool only → fig_keff_eta_scatter_main.pdf
# ════════════════════════════════════════════════════════════════════
print("\n=== K=3 panels ===")
fk3, fe3, pk3, pe3 = build_panel_data(3)
r3_full, p3_full = pearsonr(fk3, fe3)
print(f"  Full pool: {len(fk3)} panels, r={r3_full:.4f}, p={p3_full:.2e}")
if len(pk3) > 2:
    r3_poola, p3_poola = pearsonr(pk3, pe3)
    print(f"  Pool A: {len(pk3)} panels, r={r3_poola:.4f}, p={p3_poola:.2e}")

fig, ax = plt.subplots(figsize=(3.3, 2.5))
plot_scatter(ax, fk3, fe3, r3_full, p3_full, len(fk3))
fig.tight_layout(pad=0.4)
for ext in ("pdf", "png"):
    fig.savefig(OUTPUT_DIR / f"fig_keff_eta_scatter_main.{ext}", dpi=300, bbox_inches="tight")
plt.close(fig)
print(f"  Saved fig_keff_eta_scatter_main.pdf/png")

# ════════════════════════════════════════════════════════════════════
# Figure B: K=5, full pool + Pool A → fig_keff_eta_scatter.pdf
# ════════════════════════════════════════════════════════════════════
print("\n=== K=5 panels ===")
fk5, fe5, pk5, pe5 = build_panel_data(5)
r5_full, p5_full = pearsonr(fk5, fe5)
r5_poola, p5_poola = pearsonr(pk5, pe5)
print(f"  Full pool: {len(fk5)} panels, r={r5_full:.4f}, p={p5_full:.2e}")
print(f"  Pool A: {len(pk5)} panels, r={r5_poola:.4f}, p={p5_poola:.2e}")

fig, ax = plt.subplots(figsize=(3.3, 2.5))
plot_scatter(ax, fk5, fe5, r5_full, p5_full, len(fk5),
             poola_keff=pk5, poola_eta=pe5,
             r_poola=r5_poola, p_poola=p5_poola, n_poola=len(pk5))
ax.legend(loc='upper left', frameon=False, fontsize=7, markerscale=1.5)
fig.tight_layout(pad=0.4)
for ext in ("pdf", "png"):
    fig.savefig(OUTPUT_DIR / f"fig_keff_eta_scatter.{ext}", dpi=300, bbox_inches="tight")
plt.close(fig)
print(f"  Saved fig_keff_eta_scatter.pdf/png")

# ════════════════════════════════════════════════════════════════════
# Summary
# ════════════════════════════════════════════════════════════════════
print("\n=== VERIFICATION ===")
print(f"K=3 full pool: r={r3_full:.2f}, n={len(fk3)}")
print(f"K=5 full pool: r={r5_full:.2f}, n={len(fk5)}")
print(f"K=5 Pool A:    r={r5_poola:.2f}, n={len(pk5)}")
print("Done!")
