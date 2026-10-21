import numpy as np
from scipy.stats import spearmanr
import json

pairs = [
    ("Mis×DeBERTa/PW",   1.6655, 6.67),
    ("Mis×RoBERTa/PW",   1.4232, 4.17),
    ("Mis×BART/PW",      1.8590, 5.17),
    ("Qw14×DeBERTa/PW", -0.0827, 0.33),
    ("Qw14×SICA/PW",    -3.5272, 0.50),
    ("LLa8×DeBERTa/PW",  0.4150, 4.17),  # from exp092 complementarity
    ("Qw3×DeBERTa/PW",   0.3618, 1.00),  # from D116 complementarity
    ("Mis×DeBERTa/FO",  -0.4741, 2.94),
    ("Mis×SICA/FO",     -2.9280, 3.43),
    ("Mis×SICA/PW",     -4.6112,-2.83),
]

# Verify LLaMA-8B CIL from complementarity counts
# exp092: nli_right_sc_wrong=120, sc_right_nli_wrong=210, both_right=210, both_wrong=60
br, vrgw, grvw, bw = 210, 120, 210, 60
n_gw = vrgw + bw  # 180
n_gr = br + grvw  # 420
pvgw = vrgw / n_gw  # 0.6667
pvgr = br / n_gr    # 0.5
cil_llama = np.log2(pvgw / pvgr)
print(f"LLaMA-8B CIL verification: {cil_llama:.4f} (P(V|Gw)={pvgw:.4f}, P(V|Gr)={pvgr:.4f})")

# Verify Qwen3-14B CIL
# D116: nli_right_sc_wrong=61, sc_right_nli_wrong=241, both_right=269, both_wrong=29
br2, vrgw2, grvw2, bw2 = 269, 61, 241, 29
n_gw2 = vrgw2 + bw2  # 90
n_gr2 = br2 + grvw2  # 510
pvgw2 = vrgw2 / n_gw2
pvgr2 = br2 / n_gr2
cil_qwen3 = np.log2(pvgw2 / pvgr2)
print(f"Qwen3-14B CIL verification: {cil_qwen3:.4f} (P(V|Gw)={pvgw2:.4f}, P(V|Gr)={pvgr2:.4f})")

# Update pairs with verified CIL
pairs[5] = ("LLa8×DeBERTa/PW", round(cil_llama, 4), 4.17)
pairs[6] = ("Qw3×DeBERTa/PW",  round(cil_qwen3, 4), 1.00)

names = [p[0] for p in pairs]
cil = np.array([p[1] for p in pairs])
gain = np.array([p[2] for p in pairs])
n = len(cil)

print(f"\n{'='*70}")
print(f"CIL Bootstrap CI + LOO Analysis (n={n})")
print(f"{'='*70}")

# 1. Point estimate
rho, p = spearmanr(cil, gain)
print(f"\n1. Point estimate:")
print(f"   Spearman rho = {rho:.4f}, p = {p:.4f}")

# 2. Bootstrap 95% CI
np.random.seed(42)
n_boot = 10000
rhos = []
for _ in range(n_boot):
    idx = np.random.choice(n, n, replace=True)
    if len(set(idx)) < 3:
        continue
    r, _ = spearmanr(cil[idx], gain[idx])
    if not np.isnan(r):
        rhos.append(r)

rhos = np.array(rhos)
ci_lo, ci_hi = np.percentile(rhos, [2.5, 97.5])
print(f"\n2. Bootstrap 95% CI ({len(rhos)} valid resamples):")
print(f"   Mean rho = {np.mean(rhos):.4f}")
print(f"   Median rho = {np.median(rhos):.4f}")
print(f"   95% CI = [{ci_lo:.4f}, {ci_hi:.4f}]")
print(f"   CI excludes 0: {ci_lo > 0 or ci_hi < 0}")

# 3. Leave-one-out
print(f"\n3. Leave-one-out analysis:")
print(f"   {'Dropped':<22} {'rho':>8} {'p':>8} {'delta_rho':>10}")
print(f"   {'-'*50}")

loo_results = []
for i in range(n):
    c_loo = np.delete(cil, i)
    g_loo = np.delete(gain, i)
    r_loo, p_loo = spearmanr(c_loo, g_loo)
    delta = r_loo - rho
    loo_results.append((names[i], r_loo, p_loo, delta))
    sig = "*" if p_loo < 0.05 else " "
    print(f"   {names[i]:<22} {r_loo:>8.4f} {p_loo:>8.4f} {delta:>+10.4f} {sig}")

# Most influential
max_drop = min(loo_results, key=lambda x: x[1])
max_boost = max(loo_results, key=lambda x: x[1])
print(f"\n   Most fragile (removing hurts most):  {max_drop[0]} -> rho={max_drop[1]:.4f}")
print(f"   Most inflating (removing helps most): {max_boost[0]} -> rho={max_boost[1]:.4f}")

# Check if rho stays significant in all LOO
all_sig = all(r[2] < 0.05 for r in loo_results)
print(f"   All LOO p < 0.05: {all_sig}")

# 4. Summary
print(f"\n{'='*70}")
print(f"SUMMARY")
print(f"{'='*70}")
print(f"  n = {n} pairs")
print(f"  Spearman rho = {rho:.4f} (p = {p:.4f})")
print(f"  Bootstrap 95% CI = [{ci_lo:.4f}, {ci_hi:.4f}]")
ci_status = "YES" if (ci_lo > 0) else "NO"
print(f"  CI excludes zero: {ci_status}")
print(f"  LOO stable (all p<0.05): {all_sig}")
if not all_sig:
    unstable = [r for r in loo_results if r[2] >= 0.05]
    for u in unstable:
        print(f"    -> Unstable when dropping {u[0]}: rho={u[1]:.4f}, p={u[2]:.4f}")

# Save results
output = {
    "n_pairs": n,
    "point_estimate": {"spearman_rho": round(rho, 4), "p_value": round(p, 4)},
    "bootstrap_ci": {
        "n_resamples": len(rhos),
        "mean_rho": round(float(np.mean(rhos)), 4),
        "median_rho": round(float(np.median(rhos)), 4),
        "ci_95_lower": round(float(ci_lo), 4),
        "ci_95_upper": round(float(ci_hi), 4),
        "excludes_zero": bool(ci_lo > 0 or ci_hi < 0),
    },
    "leave_one_out": [
        {"dropped": r[0], "rho": round(r[1], 4), "p": round(r[2], 4), "delta_rho": round(r[3], 4)}
        for r in loo_results
    ],
    "pairs": [{"name": p[0], "cil": p[1], "combo_gain": p[2]} for p in pairs],
}
with open("/root/symb_invariant_consensus/results/cil_bootstrap_loo.json", "w") as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to /root/symb_invariant_consensus/results/cil_bootstrap_loo.json")
