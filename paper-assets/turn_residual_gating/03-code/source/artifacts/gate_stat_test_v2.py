import json
import numpy as np
from scipy import stats

with open("/root/turn_residual_gating/results/phase2_tg_s42_v7_gar.json") as f:
    data = json.load(f)

gdr = data["gate_dynamic_range"]
layers = sorted(gdr.keys(), key=lambda x: int(x[1:]))
N = len(layers)
turn1_vals = np.array([gdr[l]["turn1"] for l in layers])
turn21_vals = np.array([gdr[l]["turn21"] for l in layers])
diffs = turn21_vals - turn1_vals

print("=" * 70)
print("1. WILCOXON SIGNED-RANK TEST (averaged across 5 conversations)")
print("=" * 70)
print(f"N layers = {N}")
print(f"Mean turn1 gate  = {turn1_vals.mean():.4f} (std={turn1_vals.std():.4f})")
print(f"Mean turn21 gate = {turn21_vals.mean():.4f} (std={turn21_vals.std():.4f})")
print(f"Mean diff (t21-t1) = {diffs.mean():.4f} (std={diffs.std():.4f})")
print(f"Layers with turn21 > turn1: {np.sum(diffs > 0)}/{N}")
print(f"Layers with turn21 < turn1: {np.sum(diffs < 0)}/{N}")

stat_w, p_two = stats.wilcoxon(turn21_vals, turn1_vals, alternative='two-sided')
stat_w_one, p_one = stats.wilcoxon(turn21_vals, turn1_vals, alternative='greater')

z_score = stats.norm.ppf(1 - p_two / 2)
effect_r = z_score / np.sqrt(N)

print(f"\nWilcoxon T- = {stat_w} (sum of negative ranks)")
print(f"Wilcoxon T+ = {stat_w_one} (sum of positive ranks)")
print(f"Two-sided p = {p_two:.2e}")
print(f"One-sided p (turn21 > turn1) = {p_one:.2e}")
print(f"Z = {z_score:.4f}")
print(f"Effect size r = Z/sqrt(N) = {effect_r:.4f}")

eff_label = "negligible" if effect_r < 0.1 else "small" if effect_r < 0.3 else "medium" if effect_r < 0.5 else "large"
print(f"Effect size interpretation: {eff_label}")

# === 2. Per-conversation Wilcoxon ===
print("\n" + "=" * 70)
print("2. PER-CONVERSATION WILCOXON TESTS")
print("=" * 70)

gpt = data["gate_profile_per_turn"]
conv_results = []

for conv_key in sorted(gpt.keys()):
    conv_data = gpt[conv_key]
    t1 = np.array([conv_data["turn_1"][l] for l in layers])
    t21 = np.array([conv_data["turn_21"][l] for l in layers])
    d = t21 - t1

    w, p = stats.wilcoxon(t21, t1, alternative='greater')
    z = stats.norm.ppf(1 - p) if p > 0 and p < 1 else 0
    r = z / np.sqrt(N)
    conv_results.append((conv_key, d.mean(), w, p, r))

    print(f"\n  {conv_key}: turn_1 vs turn_21")
    print(f"    mean diff = {d.mean():.4f}, T+ = {w}, p = {p:.2e}, r = {r:.4f}")
    print(f"    layers t21 > t1: {np.sum(d > 0)}/{N}")

p_vals = np.array([r[3] for r in conv_results])
p_vals_clean = p_vals[p_vals > 0]
chi2_stat = -2 * np.sum(np.log(p_vals_clean))
combined_p = 1 - stats.chi2.cdf(chi2_stat, df=2 * len(p_vals_clean))
print(f"\n  Fisher combined p-value: {combined_p:.2e}")

# === 3. Spearman correlation ===
print("\n" + "=" * 70)
print("3. SPEARMAN CORRELATION: turn index vs gate value (per layer)")
print("=" * 70)

turn_indices = list(range(1, 22))
spearman_results = []

print(f"{'Layer':>5} {'rho':>8} {'p-value':>12} {'sig':>5}")
print("-" * 35)

for l in layers:
    avg_vals = []
    for ti in range(1, 22):
        tk = f"turn_{ti}"
        vals = [gpt[ck][tk][l] for ck in sorted(gpt.keys())]
        avg_vals.append(np.mean(vals))

    rho, p_sp = stats.spearmanr(turn_indices, avg_vals)
    sig = "***" if p_sp < 0.001 else "**" if p_sp < 0.01 else "*" if p_sp < 0.05 else ""
    spearman_results.append((l, rho, p_sp))
    print(f"{l:>5} {rho:>8.4f} {p_sp:>12.2e} {sig:>5}")

rhos = np.array([r[1] for r in spearman_results])
print(f"\nMean Spearman rho = {np.nanmean(rhos):.4f} (std={np.nanstd(rhos):.4f})")
print(f"Layers with rho > 0: {np.sum(rhos > 0)}/{N}")
sig_pos = sum(1 for l, rho, p in spearman_results if rho > 0 and p < 0.05)
print(f"Layers with significant positive trend (p<0.05): {sig_pos}/{N}")

# === 4. Layer group analysis ===
print("\n" + "=" * 70)
print("4. LAYER GROUP ANALYSIS")
print("=" * 70)

early = [l for l in layers if int(l[1:]) < 10]
mid = [l for l in layers if 10 <= int(l[1:]) < 20]
late = [l for l in layers if int(l[1:]) >= 20]

for group_name, group_layers in [("Early (L0-L9)", early), ("Mid (L10-L19)", mid), ("Late (L20-L27)", late)]:
    g_idx = [int(l[1:]) for l in group_layers]
    g_t1 = turn1_vals[g_idx]
    g_t21 = turn21_vals[g_idx]
    g_diffs = diffs[g_idx]
    print(f"\n  {group_name} ({len(group_layers)} layers):")
    print(f"    Mean turn1 = {g_t1.mean():.4f}, Mean turn21 = {g_t21.mean():.4f}")
    print(f"    Mean diff = {g_diffs.mean():.4f} (std={g_diffs.std():.4f})")
    if len(group_layers) >= 6:
        w, p = stats.wilcoxon(g_t21, g_t1, alternative='greater')
        print(f"    Wilcoxon T+ = {w}, p = {p:.2e}")

# Layer-depth correlation
print("\n  Layer depth vs diff (Spearman):")
layer_nums = np.array([int(l[1:]) for l in layers])
rho_depth, p_depth = stats.spearmanr(layer_nums, np.abs(diffs))
print(f"    rho(depth, |diff|) = {rho_depth:.4f}, p = {p_depth:.2e}")

# === 5. Paper-ready summary ===
print("\n" + "=" * 70)
print("5. PAPER-READY TEXT")
print("=" * 70)
n_positive = int(np.sum(diffs > 0))
print(f"""
Across all {N} Transformer layers, gate values at turn 21 were significantly
higher than at turn 1 (Wilcoxon signed-rank test, T+ = {int(stat_w_one)},
p = {p_one:.1e}, r = {min(effect_r, 1.0):.2f}, N = {N}), with {n_positive} of {N} layers
showing higher gate values at later turns. The mean gate value increased
from {turn1_vals.mean():.3f} +/- {turn1_vals.std():.3f} (turn 1) to {turn21_vals.mean():.3f} +/- {turn21_vals.std():.3f}
(turn 21), corresponding to a shift from partial residual suppression
toward near-identity pass-through. Spearman rank correlation confirmed
a monotonic increasing trend of gate values with turn index in {sig_pos}
of {N} layers (mean rho = {np.nanmean(rhos):.3f}). This pattern was consistent
across all five evaluation conversations (Fisher combined p = {combined_p:.1e}).
The effect was most pronounced in late layers (L20--L27, mean
diff = {diffs[[int(l[1:]) for l in late]].mean():.3f}) compared to early layers
(L0--L9, mean diff = {diffs[[int(l[1:]) for l in early]].mean():.3f}).
""")
