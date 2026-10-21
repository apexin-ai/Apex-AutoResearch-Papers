#!/usr/bin/env python3
"""α_c(T, N) Empirical Scaling Law — Zero-GPU Meta-Analysis"""
import json, os
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import norm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, ScalarFormatter

OUT = os.path.dirname(os.path.abspath(__file__))
N_PAIRS = 8
T0 = 10

# ================================================================
# STEP 1: Verify sigmoid fit against FDR-corrected dose-response
# ================================================================
# Pythia-410M WikiText fp32 — permg_count per seed
dr_raw = {
    0.00: [0, 0, 0],   0.10: [0, 3],       0.25: [0, 0, 0],
    0.30: [0],          0.35: [0],          0.40: [0],
    0.45: [0],          0.50: [6, 6, 6],    0.55: [0],
    0.60: [0, 0],       0.75: [6, 5, 0],    1.00: [6, 6],
}

alphas = np.array(sorted(dr_raw.keys()))
mean_rates = np.array([np.mean([c/N_PAIRS for c in dr_raw[a]]) for a in alphas])
n_seeds = np.array([len(dr_raw[a]) for a in alphas])
total_counts = np.array([sum(dr_raw[a]) for a in alphas])
total_trials = n_seeds * N_PAIRS

EX = dict(k=200.0, alpha_c=0.4755, y_max=0.7518)

def sigmoid(a, k, ac, ym):
    x = np.clip(-k * (a - ac), -500, 500)
    return ym / (1.0 + np.exp(x))

# Refit excluding sync-dip regime
sync_dip = np.isin(alphas, [0.55, 0.60])
mask = ~sync_dip
a_f, r_f, w_f = alphas[mask], mean_rates[mask], np.sqrt(n_seeds[mask])

popt, pcov = curve_fit(sigmoid, a_f, r_f, p0=[100, 0.48, 0.75],
                       bounds=([1, 0.2, 0.4], [1000, 0.8, 1.0]),
                       sigma=1.0/w_f, maxfev=20000)
k_new, ac_new, ym_new = popt
perr = np.sqrt(np.diag(pcov))

ssr_ex = np.sum((r_f - sigmoid(a_f, EX['k'], EX['alpha_c'], EX['y_max']))**2)
ssr_new = np.sum((r_f - sigmoid(a_f, *popt))**2)
use_new = ssr_new <= ssr_ex
K, AC, YM = (k_new, ac_new, ym_new) if use_new else (EX['k'], EX['alpha_c'], EX['y_max'])

print("=== STEP 1: Sigmoid Fit ===")
print(f"Existing: k={EX['k']:.1f}  α_c={EX['alpha_c']:.4f}  y_max={EX['y_max']:.4f}  SSR={ssr_ex:.6f}")
print(f"Refit:    k={k_new:.1f}  α_c={ac_new:.4f}  y_max={ym_new:.4f}  SSR={ssr_new:.6f}")
print(f"  SE:     k={perr[0]:.1f}  α_c={perr[1]:.4f}  y_max={perr[2]:.4f}")
print(f"Selected: {'refit' if use_new else 'existing'}")

# ================================================================
# STEP 2: Cross-architecture S(N) from α=1.0 data
# ================================================================
# Two models:
#   Simple:  S(N) = Φ⁻¹(rate) / √T
#   Threshold:  z = S_θ(N)·α·√T − θ  →  S_θ(N) = (Φ⁻¹(rate) + θ) / √T
#
# Threshold model calibration from base (Pythia-410M, α_c, T=10):
#   S_θ₀·√T₀·(1 − α_c) = Φ⁻¹(rate_base@α=1) = 0.6745
#   θ = S_θ₀·α_c·√T₀

base_rate = 0.75
z_base = norm.ppf(base_rate)  # 0.6745
S_theta0 = z_base / (np.sqrt(T0) * (1 - AC))
theta = S_theta0 * AC * np.sqrt(T0)

print(f"\n=== STEP 2: S(N) Back-solve ===")
print(f"Threshold model: S_θ₀={S_theta0:.4f}, θ={theta:.4f}")

# Model data: name → (N_params, [permg_counts@α=1.0], family)
models = {
    "GPT-2-M":      (355e6,  [6, 6],  "gpt2"),
    "Pythia-410M":   (410e6,  [6, 6],  "pythia"),
    "Qwen2.5-0.8B": (800e6,  [8, 6],  "qwen"),
    "OPT-1.3B":     (1.3e9,  [6, 6],  "opt"),
    "Pythia-1.4B":   (1.4e9,  [2, 6],  "pythia"),
    "SmolLM3-3B":   (3.0e9,  [3, 0],  "smollm"),
    "Pythia-6.9B":   (6.9e9,  [7, 6],  "pythia"),
}

sn = {}
print(f"\n{'Model':22s} {'N':>8s} {'rate':>6s} {'S_simple':>9s} {'S_θ':>7s} {'α_c(10)':>8s}")
for name, (N, counts, fam) in models.items():
    rate = np.mean([c/N_PAIRS for c in counts])
    rate_c = np.clip(rate, 1/(2*N_PAIRS), 1 - 1/(2*N_PAIRS))
    z = norm.ppf(rate_c)
    S_simple = z / np.sqrt(T0)
    S_th = (z + theta) / np.sqrt(T0)
    ac_th = theta / (S_th * np.sqrt(T0)) if S_th > 0 else np.inf
    sn[name] = dict(N=N, rate=rate, rate_c=rate_c, z=z,
                    S_simple=S_simple, S_theta=S_th, alpha_c_T10=ac_th,
                    family=fam, counts=counts)
    ac_str = f"{ac_th:.4f}" if ac_th < 10 else "∞"
    print(f"{name:22s} {N/1e9:7.2f}B {rate:6.3f} {S_simple:9.4f} {S_th:7.4f} {ac_str:>8s}")

# ================================================================
# STEP 3: Power-law fit S(N) = s₀·N^β
# ================================================================
# Using threshold-model S values (S_θ) — more physically meaningful
pos = {k: v for k, v in sn.items() if v['S_theta'] > 0}
N_pos = np.array([v['N'] for v in pos.values()])
S_pos = np.array([v['S_theta'] for v in pos.values()])
names_pos = list(pos.keys())

logN, logS = np.log10(N_pos), np.log10(S_pos)
c_all = np.polyfit(logN, logS, 1)
beta_all, s0_all = c_all[0], 10**c_all[1]
ss_r = np.sum((logS - np.polyval(c_all, logN))**2)
ss_t = np.sum((logS - np.mean(logS))**2)
R2_all = 1 - ss_r/ss_t if ss_t > 0 else 0

# Pythia-only
pyth = {k: v for k, v in pos.items() if v['family'] == 'pythia'}
Np = np.array([v['N'] for v in pyth.values()])
Sp = np.array([v['S_theta'] for v in pyth.values()])
c_py = np.polyfit(np.log10(Np), np.log10(Sp), 1)
beta_py, s0_py = c_py[0], 10**c_py[1]
ss_rp = np.sum((np.log10(Sp) - np.polyval(c_py, np.log10(Np)))**2)
ss_tp = np.sum((np.log10(Sp) - np.mean(np.log10(Sp)))**2)
R2_py = 1 - ss_rp/ss_tp if ss_tp > 0 else 0

print(f"\n=== STEP 3: Power Law ===")
print(f"All (S_θ>0, n={len(pos)}):  β={beta_all:.4f}  s₀={s0_all:.4e}  R²={R2_all:.4f}")
print(f"Pythia (n={len(pyth)}):       β={beta_py:.4f}  s₀={s0_py:.4e}  R²={R2_py:.4f}")

# ================================================================
# STEP 4: α_c(T, N) predictions
# ================================================================
# Model A (Probit-√T): α_c = const ≈ α where sigmoid = 0.5
alpha_c_A = AC + np.log(YM/0.5 - 1) / K if YM > 0.5 else AC

# Model B (Linear-threshold): α_c(T, N) = θ / (S_θ(N)·√T)
# For base model:
T_arr = np.array([5, 10, 15, 20, 25, 30])
ac_B_base = theta / (S_theta0 * np.sqrt(T_arr))

# Bootstrap CI from α_c bootstrap (propagated through 1/√T)
ac_ci_lo, ac_ci_hi = 0.425, 0.558  # from locked predictions
ac_B_lo = ac_ci_lo * np.sqrt(T0 / T_arr)
ac_B_hi = ac_ci_hi * np.sqrt(T0 / T_arr)

print(f"\n=== STEP 4: α_c Predictions ===")
print(f"Model A (Probit-√T): α_c = {alpha_c_A:.4f} (fixed)")
print(f"Model B (threshold): α_c(T) = θ/(S₀·√T) = {theta:.4f}/({S_theta0:.4f}·√T)")
print(f"\n{'T':>3s} {'Model A':>9s} {'Model B':>9s} {'CI_lo':>7s} {'CI_hi':>7s}")
for i, T in enumerate(T_arr):
    tag = " ←measured" if T == 10 else ""
    print(f"{T:3d} {alpha_c_A:9.4f} {ac_B_base[i]:9.4f} {ac_B_lo[i]:7.4f} {ac_B_hi[i]:7.4f}{tag}")

# T=20 specific comparison
ac_t20_B = theta / (S_theta0 * np.sqrt(20))
print(f"\nT=20 base model prediction:")
print(f"  Model A: α_c = {alpha_c_A:.4f}")
print(f"  Model B: α_c = {ac_t20_B:.4f}")

# Load locked predictions
with open(os.path.join(os.path.dirname(OUT),
          "t20_predictions_locked.json")) as f:
    locked = json.load(f)
print(f"\nLocked T=20 predictions (Probit-√T model):")
for key, pred in locked['predictions'].items():
    print(f"  {key}: rate={pred['predicted_rate']:.4f}")

# General formula
print(f"\nScaling law (Model B):")
print(f"  α_c(T, N) = {theta:.4f} / (S_θ(N) · √T)")
print(f"  where S_θ(N) = {s0_all:.4e} · N^{{{beta_all:.4f}}}")
print(f"  Combined: α_c(T, N) = {theta/s0_all:.4e} / (N^{{{beta_all:.4f}}} · √T)")

# ================================================================
# STEP 5: Figures
# ================================================================
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman'],
    'font.size': 11, 'axes.labelsize': 13, 'axes.titlesize': 13,
    'xtick.labelsize': 10, 'ytick.labelsize': 10, 'legend.fontsize': 9,
    'figure.dpi': 150, 'savefig.dpi': 300, 'savefig.bbox': 'tight',
})

COLORS = {'pythia': '#1976D2', 'gpt2': '#388E3C', 'qwen': '#F57C00',
           'opt': '#7B1FA2', 'smollm': '#D32F2F'}
MARKERS = {'pythia': 'o', 'gpt2': 's', 'qwen': 'D', 'opt': '^', 'smollm': 'x'}

# --- Fig 1: S(N) vs N ---
fig1, ax1 = plt.subplots(figsize=(5.5, 4))
for name, v in sn.items():
    c = COLORS[v['family']]
    m = MARKERS[v['family']]
    s = 80 if v['S_theta'] > 0 else 60
    alpha = 1.0 if v['S_theta'] > 0 else 0.4
    y = v['S_theta'] if v['S_theta'] > 0 else 0.02
    ax1.scatter(v['N']/1e9, y, c=c, marker=m, s=s, alpha=alpha,
               edgecolors='k', linewidths=0.5, zorder=5, label=name)

# Power law fit lines
N_line = np.logspace(np.log10(0.2), np.log10(10), 200)
S_line_all = s0_all * (N_line*1e9)**beta_all
S_line_py = s0_py * (N_line*1e9)**beta_py
ax1.plot(N_line, S_line_all, 'k--', alpha=0.5, lw=1.5,
         label=f'All: β={beta_all:.3f}, R²={R2_all:.2f}')
ax1.plot(N_line, S_line_py, 'b:', alpha=0.5, lw=1.5,
         label=f'Pythia: β={beta_py:.3f}, R²={R2_py:.2f}')

ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlabel('Model size $N$ (billion parameters)')
ax1.set_ylabel('Signal strength $S_{\\theta}(N)$')
ax1.set_title('Cross-architecture signal strength at $\\alpha=1.0$')
ax1.legend(loc='best', framealpha=0.9, fontsize=8)
ax1.grid(True, alpha=0.2, which='both')
ax1.axhline(0, color='gray', lw=0.5)

# Custom x-axis labels
ax1.set_xticks([0.3, 0.5, 1, 2, 3, 5, 7])
ax1.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:.1f}' if x < 1 else f'{x:.0f}'))

for fmt in ['pdf', 'png']:
    fig1.savefig(os.path.join(OUT, f'fig_s_vs_n.{fmt}'))
plt.close(fig1)

# --- Fig 2: α_c(T) vs T ---
fig2, ax2 = plt.subplots(figsize=(5.5, 4))
T_dense = np.linspace(3, 35, 300)

# Model B curve + CI
ac_dense_B = theta / (S_theta0 * np.sqrt(T_dense))
ac_lo_dense = ac_ci_lo * np.sqrt(T0 / T_dense)
ac_hi_dense = ac_ci_hi * np.sqrt(T0 / T_dense)

ax2.plot(T_dense, ac_dense_B, 'b-', lw=2,
         label=f'Model B: $\\alpha_c \\propto 1/\\sqrt{{T}}$')
ax2.fill_between(T_dense, ac_lo_dense, ac_hi_dense, alpha=0.15, color='blue',
                 label='95% CI (bootstrap)')

# Model A (horizontal)
ax2.axhline(alpha_c_A, color='r', ls='--', lw=1.5, alpha=0.7,
            label=f'Model A: $\\alpha_c = {alpha_c_A:.3f}$ (fixed)')

# Measured T=10
ax2.scatter([T0], [AC], c='red', marker='*', s=200, zorder=10,
           edgecolors='k', linewidths=0.5,
           label=f'Measured $\\alpha_c(T\\!=\\!10) = {AC:.4f}$')

# Predicted T=20
ax2.scatter([20], [ac_t20_B], c='blue', marker='D', s=100, zorder=10,
           edgecolors='k', linewidths=0.5,
           label=f'Predicted $\\alpha_c(T\\!=\\!20) = {ac_t20_B:.3f}$')

# Extrapolation markers
for T_ex in [5, 15, 25, 30]:
    ac_ex = theta / (S_theta0 * np.sqrt(T_ex))
    ax2.scatter([T_ex], [ac_ex], c='blue', marker='o', s=40, zorder=8,
               edgecolors='k', linewidths=0.3, alpha=0.6)

ax2.set_xlabel('Training generations $T$')
ax2.set_ylabel('Detection threshold $\\alpha_c$')
ax2.set_title('$\\alpha_c$ scaling with training duration (Pythia-410M)')
ax2.legend(loc='upper right', framealpha=0.9, fontsize=8)
ax2.grid(True, alpha=0.2)
ax2.set_xlim(3, 35)
ax2.set_ylim(0, 1.0)

for fmt in ['pdf', 'png']:
    fig2.savefig(os.path.join(OUT, f'fig_alpha_c_vs_t.{fmt}'))
plt.close(fig2)

# --- Fig 3: 2D heatmap α_c(T, N) ---
fig3, ax3 = plt.subplots(figsize=(6.5, 4.5))

T_heat = np.arange(5, 31)
N_heat = np.logspace(np.log10(200e6), np.log10(8e9), 60)
Tg, Ng = np.meshgrid(T_heat, N_heat)

# S(N) from all-model power law
Sg = s0_all * Ng**beta_all
# α_c(T, N) = θ / (S(N)·√T)
ac_grid = theta / (Sg * np.sqrt(Tg))
ac_grid = np.clip(ac_grid, 0, 1.5)

im = ax3.pcolormesh(T_heat, N_heat/1e9, ac_grid, cmap='RdYlGn_r',
                     shading='auto', vmin=0, vmax=1.0)
cbar = fig3.colorbar(im, ax=ax3, label='$\\alpha_c(T, N)$', pad=0.02)
cbar.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])

# Contour lines
cs = ax3.contour(T_heat, N_heat/1e9, ac_grid, levels=[0.2, 0.3, 0.5, 0.7],
                  colors='white', linewidths=0.8, linestyles='--')
ax3.clabel(cs, inline=True, fontsize=8, fmt='%.1f')

# Mark measured models
for name, v in sn.items():
    if v['S_theta'] > 0:
        ax3.scatter([T0], [v['N']/1e9], c='white', edgecolors='black',
                   s=50, zorder=5, linewidths=1.0, marker='o')
        ax3.annotate(name.split('-')[0] if '-' in name else name[:6],
                    (T0+0.5, v['N']/1e9), fontsize=6, color='white',
                    va='center', fontweight='bold')

ax3.set_yscale('log')
ax3.set_xlabel('Training generations $T$')
ax3.set_ylabel('Model size $N$ (billion parameters)')
ax3.set_title('Predicted detection threshold $\\alpha_c(T, N)$')
ax3.set_yticks([0.3, 0.5, 1, 2, 3, 5, 7])
ax3.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:.1f}' if x < 1 else f'{x:.0f}'))

for fmt in ['pdf', 'png']:
    fig3.savefig(os.path.join(OUT, f'fig_alpha_c_heatmap.{fmt}'))
plt.close(fig3)

print(f"\nFigures saved to {OUT}/")

# ================================================================
# STEP 6: Save JSON
# ================================================================
output = {
    "generated_at": "2026-05-20",
    "method": "meta-analysis of existing experiments, zero GPU cost",

    "step1_sigmoid_verification": {
        "data_source": "dose_response_d120_compiled.csv (FDR-corrected PermG)",
        "model": "Pythia-410M, WikiText, fp32, T=10",
        "n_alpha_points": len(alphas),
        "sync_dip_excluded": [0.55, 0.60],
        "existing_params": EX,
        "refit_params": {"k": float(k_new), "alpha_c": float(ac_new), "y_max": float(ym_new)},
        "refit_std_errors": {"k": float(perr[0]), "alpha_c": float(perr[1]), "y_max": float(perr[2])},
        "ssr_existing": float(ssr_ex),
        "ssr_refit": float(ssr_new),
        "selected": "refit" if use_new else "existing",
        "conclusion": "FDR-corrected data consistent with existing fit" if abs(ac_new - EX['alpha_c']) < 0.05 else "refit differs significantly",
    },

    "step2_signal_strength": {
        "threshold_model": {
            "formula": "z(α,T,N) = S_θ(N)·α·√T − θ",
            "theta": float(theta),
            "S_theta0_base": float(S_theta0),
        },
        "simple_model": {
            "formula": "S(N) = Φ⁻¹(rate) / √T",
        },
        "models": {
            name: {
                "N_params": v['N'],
                "N_display": f"{v['N']/1e9:.2f}B",
                "family": v['family'],
                "permg_rate_alpha1": v['rate'],
                "S_simple": round(v['S_simple'], 4),
                "S_theta": round(v['S_theta'], 4),
                "alpha_c_T10_predicted": round(v['alpha_c_T10'], 4) if v['alpha_c_T10'] < 10 else None,
            }
            for name, v in sn.items()
        },
        "notes": [
            "SmolLM3-3B has S_theta < 0 (detection rate below model baseline)",
            "Pythia-1.4B shows high seed variance (2/8 vs 6/8)",
            "Most models cluster at rate=0.75 → similar S values",
        ],
    },

    "step3_power_law": {
        "formula": "S_θ(N) = s₀ · N^β",
        "all_models": {
            "s0": float(s0_all), "beta": float(beta_all),
            "R2": round(float(R2_all), 4), "n": len(pos),
            "excluded": ["SmolLM3-3B (S_θ < 0)"],
        },
        "pythia_only": {
            "s0": float(s0_py), "beta": float(beta_py),
            "R2": round(float(R2_py), 4), "n": len(pyth),
        },
        "interpretation": "Weak or no power-law scaling: cross-architecture variation dominates size effect",
    },

    "step4_scaling_law": {
        "model_A_probit_sqrt_T": {
            "formula": "α_c = const (T-independent)",
            "alpha_c": round(float(alpha_c_A), 4),
            "rationale": "Probit z-scores scale as √T; α_c is the rate=0.5 crossing which stays fixed",
        },
        "model_B_linear_threshold": {
            "formula": "α_c(T, N) = θ / (S_θ(N) · √T)",
            "theta": float(theta),
            "combined_formula": f"α_c(T, N) = {theta:.4f} / ({s0_all:.4e} · N^{{{beta_all:.4f}}} · √T)",
            "predictions_pythia410m": {
                f"T={int(T)}": round(float(theta / (S_theta0 * np.sqrt(T))), 4)
                for T in T_arr
            },
            "predictions_pythia410m_CI95": {
                f"T={int(T)}": [round(float(lo), 4), round(float(hi), 4)]
                for T, lo, hi in zip(T_arr, ac_B_lo, ac_B_hi)
            },
        },
        "t20_comparison": {
            "model_A_alpha_c": round(float(alpha_c_A), 4),
            "model_B_alpha_c": round(float(ac_t20_B), 4),
            "locked_predictions_use": "Model A (Probit-√T)",
            "discriminating_test": "α=0.40-0.45 at T=20: Model B predicts detection, Model A predicts none",
        },
    },

    "step5_figures": [
        "fig_s_vs_n.pdf", "fig_s_vs_n.png",
        "fig_alpha_c_vs_t.pdf", "fig_alpha_c_vs_t.png",
        "fig_alpha_c_heatmap.pdf", "fig_alpha_c_heatmap.png",
    ],
}

json_path = os.path.join(OUT, "alpha_c_scaling.json")
with open(json_path, 'w') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
print(f"JSON → {json_path}")
