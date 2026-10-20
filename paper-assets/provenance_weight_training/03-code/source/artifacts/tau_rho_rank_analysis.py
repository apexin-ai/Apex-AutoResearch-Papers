import json
import csv
import os
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(OUT_DIR, "figures")

# === Data ===
rho04 = {
    0.50: {"ppl": 17.688,  "exp_id": "tau_05_seed42"},
    0.60: {"ppl": 17.6805, "exp_id": "tau_06_seed42"},
    0.70: {"ppl": 17.6793, "exp_id": "tau_07_seed42"},
    0.80: {"ppl": 17.6527, "exp_id": "adaptive_fix_seed42"},
    0.90: {"ppl": 17.712,  "exp_id": "tau_09_seed42"},
    0.95: {"ppl": 17.723,  "exp_id": "tau_095_seed42"},
}
uniform_04 = 17.6939

rho06 = {
    0.60: {"ppl": 17.7359, "exp_id": "contamination_60_tau06_seed42"},
    0.70: {"ppl": 17.730,  "exp_id": "contamination_60_tau07_seed42"},
    0.80: {"ppl": 17.740,  "exp_id": "contamination_60_seed42_r2"},
}
uniform_06 = 17.766

# === 1. Rank preservation on shared τ values {0.6, 0.7, 0.8} ===
shared_taus = [0.6, 0.7, 0.8]

ppl_04 = [rho04[t]["ppl"] for t in shared_taus]
ppl_06 = [rho06[t]["ppl"] for t in shared_taus]

# Ranks: lower PPL = better = rank 1
rank_04 = stats.rankdata(ppl_04, method='ordinal')  # ascending: rank 1 = lowest PPL
rank_06 = stats.rankdata(ppl_06, method='ordinal')

print("=== Rank Preservation (shared τ = {0.6, 0.7, 0.8}) ===")
for i, t in enumerate(shared_taus):
    print(f"  τ={t}: ρ=0.4 PPL={ppl_04[i]:.4f} rank={int(rank_04[i])}, ρ=0.6 PPL={ppl_06[i]:.4f} rank={int(rank_06[i])}")

# Kendall's tau correlation on ranks
kendall_tau, kendall_p = stats.kendalltau(rank_04, rank_06)
spearman_r, spearman_p = stats.spearmanr(rank_04, rank_06)

print(f"\nKendall's τ = {kendall_tau:.4f} (p = {kendall_p:.4f})")
print(f"Spearman's ρ = {spearman_r:.4f} (p = {spearman_p:.4f})")

# Count rank swaps
rank_swaps = sum(1 for i in range(len(shared_taus)) if rank_04[i] != rank_06[i])
print(f"Rank swaps: {rank_swaps}/{len(shared_taus)}")

# === 2. Normalized PPL gap ===
print("\n=== Normalized PPL Gap ===")
rows = []

for t in sorted(rho04.keys()):
    gap = (rho04[t]["ppl"] - uniform_04) / uniform_04 * 100
    rank_within = None  # compute below
    rows.append({"tau": t, "rho": 0.4, "ppl": rho04[t]["ppl"], "uniform_ppl": uniform_04,
                 "normalized_gap_pct": gap, "exp_id": rho04[t]["exp_id"]})

for t in sorted(rho06.keys()):
    gap = (rho06[t]["ppl"] - uniform_06) / uniform_06 * 100
    rows.append({"tau": t, "rho": 0.6, "ppl": rho06[t]["ppl"], "uniform_ppl": uniform_06,
                 "normalized_gap_pct": gap, "exp_id": rho06[t]["exp_id"]})

# Compute rank_within_rho
for rho_val in [0.4, 0.6]:
    subset = [r for r in rows if r["rho"] == rho_val]
    ppls = [r["ppl"] for r in subset]
    ranks = stats.rankdata(ppls, method='ordinal')
    for r, rank in zip(subset, ranks):
        r["rank_within_rho"] = int(rank)

for r in rows:
    print(f"  τ={r['tau']}, ρ={r['rho']}: PPL={r['ppl']:.4f}, gap={r['normalized_gap_pct']:.4f}%, rank={r['rank_within_rho']}")

# === 3. Safe range analysis ===
print("\n=== Safe Range Analysis ===")
safe_04 = [t for t in rho04 if rho04[t]["ppl"] < uniform_04]
safe_06 = [t for t in rho06 if rho06[t]["ppl"] < uniform_06]
print(f"ρ=0.4 safe τ (< uniform {uniform_04}): {sorted(safe_04)}")
print(f"ρ=0.6 safe τ (< uniform {uniform_06}): {sorted(safe_06)}")

best_04 = min(rho04.items(), key=lambda x: x[1]["ppl"])
best_06 = min(rho06.items(), key=lambda x: x[1]["ppl"])
print(f"Best τ at ρ=0.4: {best_04[0]} (PPL={best_04[1]['ppl']:.4f})")
print(f"Best τ at ρ=0.6: {best_06[0]} (PPL={best_06[1]['ppl']:.4f})")

max_ppl_gap_safe = 0
for t in shared_taus:
    gap = abs(rho04[t]["ppl"] - rho06[t]["ppl"])
    if gap > max_ppl_gap_safe:
        max_ppl_gap_safe = gap

print(f"Max absolute PPL gap within shared safe range: {max_ppl_gap_safe:.4f}")

# === Write CSV ===
csv_path = os.path.join(OUT_DIR, "tau_rho_rank_analysis.csv")
with open(csv_path, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["tau", "rho", "ppl", "uniform_ppl", "normalized_gap_pct", "rank_within_rho", "exp_id"])
    writer.writeheader()
    for r in rows:
        writer.writerow(r)
print(f"\nCSV written: {csv_path}")

# === Write JSON stats ===
stats_dict = {
    "shared_taus": shared_taus,
    "kendall_tau": round(kendall_tau, 4),
    "kendall_p": round(kendall_p, 4),
    "spearman_r": round(spearman_r, 4),
    "spearman_p": round(spearman_p, 4),
    "rank_swaps": rank_swaps,
    "max_rank_swap_count": rank_swaps,
    "max_absolute_ppl_gap_within_safe_range": round(max_ppl_gap_safe, 4),
    "best_tau_rho04": best_04[0],
    "best_ppl_rho04": best_04[1]["ppl"],
    "best_tau_rho06": best_06[0],
    "best_ppl_rho06": best_06[1]["ppl"],
    "safe_range_rho04": sorted(safe_04),
    "safe_range_rho06": sorted(safe_06),
    "normalized_gap_best_rho04_pct": round((best_04[1]["ppl"] - uniform_04) / uniform_04 * 100, 4),
    "normalized_gap_best_rho06_pct": round((best_06[1]["ppl"] - uniform_06) / uniform_06 * 100, 4),
    "note": "τ=0.8 is optimal at ρ=0.4 but shifts to τ=0.7 at ρ=0.6; τ=0.7-0.8 is optimal across tested ρ values"
}

json_path = os.path.join(OUT_DIR, "tau_rho_rank_stats.json")
with open(json_path, 'w') as f:
    json.dump(stats_dict, f, indent=2)
print(f"JSON written: {json_path}")

# === Figure ===
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2), sharey=False)

# Color palette
c04 = '#2166ac'
c06 = '#b2182b'
c_uniform = '#888888'

# --- Panel A: τ-PPL curves for both ρ ---
taus_04 = sorted(rho04.keys())
ppls_04_all = [rho04[t]["ppl"] for t in taus_04]

taus_06 = sorted(rho06.keys())
ppls_06_all = [rho06[t]["ppl"] for t in taus_06]

ax1.plot(taus_04, ppls_04_all, 'o-', color=c04, linewidth=1.8, markersize=6, label='ρ=0.4', zorder=3)
ax1.plot(taus_06, ppls_06_all, 's-', color=c06, linewidth=1.8, markersize=6, label='ρ=0.6', zorder=3)

ax1.axhline(y=uniform_04, color=c04, linestyle='--', linewidth=1, alpha=0.6, label=f'Uniform (ρ=0.4) = {uniform_04}')
ax1.axhline(y=uniform_06, color=c06, linestyle='--', linewidth=1, alpha=0.6, label=f'Uniform (ρ=0.6) = {uniform_06}')

# Mark best points
ax1.scatter([best_04[0]], [best_04[1]["ppl"]], s=120, facecolors='none', edgecolors=c04, linewidths=2.2, zorder=4)
ax1.scatter([best_06[0]], [best_06[1]["ppl"]], s=120, facecolors='none', edgecolors=c06, linewidths=2.2, zorder=4)

# Shade safe range
ax1.axvspan(0.5, 0.8, alpha=0.08, color='green', zorder=0)
ax1.text(0.65, ax1.get_ylim()[0] if ax1.get_ylim()[0] > 0 else 17.64, 'safe range',
         ha='center', va='bottom', fontsize=8, color='green', alpha=0.7)

ax1.set_xlabel('τ (temperature)', fontsize=11)
ax1.set_ylabel('Perplexity (PPL)', fontsize=11)
ax1.set_title('(a) τ–PPL curves across ρ', fontsize=11)
ax1.legend(fontsize=7.5, loc='upper left')
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax1.set_xticks([0.5, 0.6, 0.7, 0.8, 0.9, 0.95])
ax1.grid(True, alpha=0.3)

# --- Panel B: Normalized gap ---
# Bar chart for shared τ values
bar_width = 0.035
x_positions = np.array(shared_taus)

gaps_04 = [(rho04[t]["ppl"] - uniform_04) / uniform_04 * 100 for t in shared_taus]
gaps_06 = [(rho06[t]["ppl"] - uniform_06) / uniform_06 * 100 for t in shared_taus]

bars1 = ax2.bar(x_positions - bar_width/2, gaps_04, bar_width, color=c04, alpha=0.8, label='ρ=0.4')
bars2 = ax2.bar(x_positions + bar_width/2, gaps_06, bar_width, color=c06, alpha=0.8, label='ρ=0.6')

ax2.axhline(y=0, color='black', linewidth=0.8)
ax2.set_xlabel('τ (temperature)', fontsize=11)
ax2.set_ylabel('Normalized PPL gap (%)\n(negative = better than uniform)', fontsize=10)
ax2.set_title('(b) Relative improvement over uniform', fontsize=11)
ax2.set_xticks(shared_taus)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3, axis='y')
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))

# Add value labels on bars
for bar in list(bars1) + list(bars2):
    h = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, h - 0.003 if h < 0 else h + 0.003,
             f'{h:.3f}%', ha='center', va='top' if h < 0 else 'bottom', fontsize=7)

plt.tight_layout()
fig_path = os.path.join(FIG_DIR, "tau_rho_rank_preservation.pdf")
png_path = os.path.join(FIG_DIR, "tau_rho_rank_preservation.png")
plt.savefig(fig_path, dpi=300, bbox_inches='tight')
plt.savefig(png_path, dpi=200, bbox_inches='tight')
print(f"\nFigure written: {fig_path}")
print(f"Figure written: {png_path}")

print("\n=== DONE ===")
