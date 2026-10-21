"""Transfer heatmap with fonttype fix."""
import os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

DATA = "/root/gen-depth-fingerprint/data/features_8gen.csv"
OUT_DIR = "/root/gen-depth-fingerprint/chart"

FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
GENERATORS = ["pythia-2.8b", "pythia-1b", "qwen3-0.6b", "qwen3-1.7b",
              "qwen3-8b", "olmo-2-1b", "llama-3.2-3b", "mistral-7b-v0.3"]
SHORT = {"pythia-2.8b": "Py-2.8B", "pythia-1b": "Py-1B",
         "qwen3-0.6b": "Qw-0.6B", "qwen3-1.7b": "Qw-1.7B",
         "qwen3-8b": "Qw-8B", "olmo-2-1b": "OLMo-1B",
         "llama-3.2-3b": "Ll-3B", "mistral-7b-v0.3": "Mi-7B"}

df = pd.read_csv(DATA)
df = df[df["depth"] > 0].copy()
df["label"] = (df["depth"] >= 2).astype(int)

gen_data = {}
for g in GENERATORS:
    sub = df[df["model_name"] == g]
    gen_data[g] = (sub[FEATURES].values, sub["label"].values)

n = len(GENERATORS)
matrix = np.zeros((n, n))
for i, train_gen in enumerate(GENERATORS):
    X_tr, y_tr = gen_data[train_gen]
    clf = XGBClassifier(n_estimators=200, max_depth=6, learning_rate=0.1,
                        random_state=42, use_label_encoder=False, eval_metric="logloss")
    clf.fit(X_tr, y_tr)
    for j, test_gen in enumerate(GENERATORS):
        X_te, y_te = gen_data[test_gen]
        preds = clf.predict(X_te)
        matrix[i, j] = f1_score(y_te, preds, average="binary")

short_names = [SHORT[g] for g in GENERATORS]

from scipy import stats
mask_off = ~np.eye(n, dtype=bool)
cross_f1 = matrix[mask_off]
mean_cross = cross_f1.mean()
rng = np.random.RandomState(42)
boot_means = np.array([rng.choice(cross_f1, size=len(cross_f1), replace=True).mean() for _ in range(1000)])
ci_lo, ci_hi = np.percentile(boot_means, [2.5, 97.5])

fig, ax = plt.subplots(figsize=(6.5, 5.5))
vmin = min(matrix.min(), 0.49)
vmax = max(matrix.max(), 0.51)
norm = TwoSlopeNorm(vmin=vmin, vcenter=0.5, vmax=vmax)
im = ax.imshow(matrix, cmap="RdBu_r", norm=norm, aspect="equal")

ax.set_xticks(range(n))
ax.set_yticks(range(n))
ax.set_xticklabels(short_names, fontsize=8.5, rotation=45, ha="right")
ax.set_yticklabels(short_names, fontsize=8.5)
ax.set_xlabel("Test generator", fontsize=10)
ax.set_ylabel("Train generator", fontsize=10)
ax.set_title("Cross-Generator Binary F1 Transfer Matrix", fontsize=11, pad=10)

for i in range(n):
    for j in range(n):
        val = matrix[i, j]
        color = "white" if abs(val - 0.5) > 0.2 else "black"
        weight = "bold" if i == j else "normal"
        ax.text(j, i, f"{val:.2f}", ha="center", va="center",
                fontsize=8, color=color, fontweight=weight)

for i in range(n):
    rect = plt.Rectangle((i - 0.5, i - 0.5), 1, 1,
                          linewidth=1.5, edgecolor="black", facecolor="none")
    ax.add_patch(rect)

cbar = fig.colorbar(im, ax=ax, shrink=0.82, pad=0.02)
cbar.set_label("Binary F1", fontsize=9)
cbar.ax.tick_params(labelsize=8)

annot = f"Mean cross-gen F1 = {mean_cross:.3f}  [95% CI: {ci_lo:.3f}, {ci_hi:.3f}]"
ax.annotate(annot, xy=(0.5, -0.18), xycoords="axes fraction",
            ha="center", fontsize=8.5, style="italic")
ax.spines[:].set_visible(False)
ax.tick_params(length=0)

fig.tight_layout(rect=[0, 0.04, 1, 1])
fig.savefig(f"{OUT_DIR}/fig_transfer_heatmap.pdf", bbox_inches="tight", dpi=300)
fig.savefig(f"{OUT_DIR}/fig_transfer_heatmap.png", bbox_inches="tight", dpi=300)
plt.close(fig)
print(f"Saved: {OUT_DIR}/fig_transfer_heatmap.pdf")
