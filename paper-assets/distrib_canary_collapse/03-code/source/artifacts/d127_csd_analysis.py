import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

raw_data = json.loads('''{"0.0": {"token_entropy": [3.2341948700181407, 2.990560020858481, 3.0210253027501817, 3.0143118826392152, 3.040745918964843, 3.033519169596899, 3.0566470063058757, 3.0500435519521285, 3.0663137671120135, 3.042682389945363, 3.0693134262755994], "distinct_1": [0.0982156685333268, 0.09752517633628247, 0.08881482826974563, 0.08869935695152098, 0.08683875960422309, 0.08563529383964649, 0.08446896293054948, 0.0843671875, 0.08494612734105808, 0.0846484375, 0.0846796875], "n_gen": 11}, "0.1": {"token_entropy": [3.23419483150593, 2.9860799824539708, 3.0125748730959026, 3.0294942249633925, 3.0240987446117735, 3.0351983237530136, 3.0488500618901275, 3.0547791021304715, 3.051467669876491, 3.068355764898854, 3.085810292493476], "distinct_1": [0.09162095491577137, 0.09102786749549609, 0.0725546875, 0.06884375, 0.067875, 0.068515625, 0.0687265625, 0.06928125, 0.0692578125, 0.068390625, 0.0698125], "n_gen": 11}, "0.25": {"token_entropy": [3.23419483150593, 2.982970821354138, 3.015356774173291, 3.0394912882566234, 3.0510859134014026, 3.033953061558668, 3.048800855005907, 3.0668466086642856, 3.063090341957354, 3.1036846433718384, 3.0793514096299655], "distinct_1": [0.0979600146585773, 0.09759209446336131, 0.081546875, 0.07367162032223516, 0.068796875, 0.065734375, 0.06353125, 0.0614375, 0.06096875, 0.0600703125, 0.059609375], "n_gen": 11}, "0.3": {"token_entropy": [3.23419483150593, 2.5080404989853675, 2.523510596175988, 2.562340003532139, 2.592072488473396, 2.6295831255460027, 2.6030902827490157, 2.6530388418216835, 2.657611687956306, 2.6633007653092937, 2.674095885331292], "distinct_1": [0.0979600146585773, 0.09759209446336131, 0.0842578125, 0.078578125, 0.0731640625, 0.069359375, 0.0668359375, 0.064953125, 0.063359375, 0.0628046875, 0.061984375], "n_gen": 11}, "0.35": {"token_entropy": [3.23419483150593, 2.489957576020291, 2.5006408917456184, 2.538066339808064, 2.5565276218014636, 2.5785078582592043, 2.5729746096830977, 2.586707538258231, 2.605213191341737, 2.627628130192116, 2.635019840754219], "distinct_1": [0.0979600146585773, 0.09759209446336131, 0.0828828125, 0.0770390625, 0.07228125, 0.0687734375, 0.06759375, 0.0651484375, 0.063546875, 0.0628125, 0.0623203125], "n_gen": 11}, "0.4": {"token_entropy": [3.23419483150593, 2.4992898164150374, 2.499869426861146, 2.5278057525267226, 2.5614256750902538, 2.5625561206632708, 2.5607226447298257, 2.5665522715586935, 2.602239060750541, 2.609718033284409, 2.615471327237143], "distinct_1": [0.0979600146585773, 0.09759209446336131, 0.0834609375, 0.077234375, 0.072796875, 0.06975, 0.0675, 0.0656953125, 0.0646015625, 0.06371875, 0.063203125], "n_gen": 11}, "0.45": {"token_entropy": [3.23419483150593, 2.494058441616721, 2.534136101724104, 2.5901672458724554, 2.5706613419304554, 2.5727669083072353, 2.5580367110582745, 2.577145103682105, 2.6037081475414983, 2.6331889819766605, 2.628269700087532], "distinct_1": [0.0979600146585773, 0.09759209446336131, 0.0839296875, 0.0783828125, 0.0730703125, 0.0698125, 0.0676796875, 0.06565625, 0.0644375, 0.063875, 0.0632890625], "n_gen": 11}, "0.5": {"token_entropy": [3.23419483150593, 2.513125962738291, 2.5109620436644615, 2.581628010409094, 2.5882908639873565, 2.585607048487396, 2.6079916782279207, 2.656354046597873, 2.660300319157053, 2.672411609051149, 2.7074937347665786], "distinct_1": [0.09162095491577137, 0.09102786749549609, 0.0750859375, 0.070015625, 0.06940625, 0.0685703125, 0.0680078125, 0.0671953125, 0.0669296875, 0.0656015625, 0.064875], "n_gen": 11}, "0.75": {"token_entropy": [3.23419483150593, 2.1737574601166205, 2.105473003087621, 2.0912935053356088, 2.1229484829993304, 2.1407181375955693, 2.161739464378603, 2.165227522840487, 2.202272252583091, 2.240664472671789, 2.282990654807781], "distinct_1": [0.0979600146585773, 0.09759209446336131, 0.0838515625, 0.0778671875, 0.0750625, 0.0741484375, 0.07346875, 0.0733359375, 0.0732265625, 0.073234375, 0.0731015625], "n_gen": 11}}''')

alphas = [0.0, 0.1, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.75]

def compute_ac1(x):
    x = np.array(x)
    if len(x) < 3:
        return np.nan
    return np.corrcoef(x[:-1], x[1:])[0, 1]

def compute_rolling_ac1(x, window=3):
    x = np.array(x)
    ac1s = []
    for i in range(len(x) - window + 1):
        w = x[i:i+window]
        if len(w) >= 3:
            ac1s.append(np.corrcoef(w[:-1], w[1:])[0, 1])
    return ac1s

def compute_rolling_variance(x, window=3):
    x = np.array(x)
    variances = []
    for i in range(len(x) - window + 1):
        variances.append(np.var(x[i:i+window], ddof=1))
    return variances

results = {
    "alphas": alphas,
    "token_entropy_ac1": [],
    "token_entropy_variance": [],
    "token_entropy_rolling_ac1_mean": [],
    "token_entropy_rolling_var_mean": [],
    "distinct_1_ac1": [],
    "distinct_1_variance": [],
    "distinct_1_rolling_ac1_mean": [],
    "distinct_1_rolling_var_mean": [],
}

for alpha in alphas:
    key = str(alpha)
    te = raw_data[key]["token_entropy"]
    d1 = raw_data[key]["distinct_1"]

    te_ac1 = compute_ac1(te)
    te_var = np.var(te, ddof=1)
    te_rolling_ac1 = compute_rolling_ac1(te, window=3)
    te_rolling_var = compute_rolling_variance(te, window=3)

    d1_ac1 = compute_ac1(d1)
    d1_var = np.var(d1, ddof=1)
    d1_rolling_ac1 = compute_rolling_ac1(d1, window=3)
    d1_rolling_var = compute_rolling_variance(d1, window=3)

    results["token_entropy_ac1"].append(round(te_ac1, 6))
    results["token_entropy_variance"].append(round(float(te_var), 8))
    results["token_entropy_rolling_ac1_mean"].append(round(float(np.mean(te_rolling_ac1)), 6))
    results["token_entropy_rolling_var_mean"].append(round(float(np.mean(te_rolling_var)), 8))

    results["distinct_1_ac1"].append(round(d1_ac1, 6))
    results["distinct_1_variance"].append(round(float(d1_var), 10))
    results["distinct_1_rolling_ac1_mean"].append(round(float(np.mean(d1_rolling_ac1)), 6))
    results["distinct_1_rolling_var_mean"].append(round(float(np.mean(d1_rolling_var)), 10))

# CSD detection: check if AC1 rises and variance inflates near onset (0.45 -> 0.50)
te_ac1s = results["token_entropy_ac1"]
te_vars = results["token_entropy_variance"]
d1_ac1s = results["distinct_1_ac1"]
d1_vars = results["distinct_1_variance"]

# Index mapping: alphas = [0.0, 0.1, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.75]
idx_045 = alphas.index(0.45)
idx_050 = alphas.index(0.50)
idx_040 = alphas.index(0.40)

te_ac1_jump_045_050 = te_ac1s[idx_050] - te_ac1s[idx_045]
d1_ac1_jump_045_050 = d1_ac1s[idx_050] - d1_ac1s[idx_045]
te_var_jump_045_050 = te_vars[idx_050] - te_vars[idx_045]
d1_var_jump_045_050 = d1_vars[idx_050] - d1_vars[idx_045]

# Baseline: mean AC1 for alpha <= 0.35
baseline_alphas = [i for i, a in enumerate(alphas) if a <= 0.35]
te_ac1_baseline = np.mean([te_ac1s[i] for i in baseline_alphas])
d1_ac1_baseline = np.mean([d1_ac1s[i] for i in baseline_alphas])
te_var_baseline = np.mean([te_vars[i] for i in baseline_alphas])
d1_var_baseline = np.mean([d1_vars[i] for i in baseline_alphas])

# CSD criterion: AC1 at onset should be elevated relative to baseline
te_ac1_elevated = te_ac1s[idx_045] > te_ac1_baseline and te_ac1s[idx_050] > te_ac1_baseline
d1_ac1_elevated = d1_ac1s[idx_045] > d1_ac1_baseline or d1_ac1s[idx_050] > d1_ac1_baseline
te_var_elevated = te_vars[idx_045] > te_var_baseline or te_vars[idx_050] > te_var_baseline

csd_detected = te_ac1_elevated or d1_ac1_elevated

onset_description = (
    f"token_entropy AC1: baseline(α≤0.35)={te_ac1_baseline:.4f}, "
    f"α=0.40={te_ac1s[idx_040]:.4f}, α=0.45={te_ac1s[idx_045]:.4f}, α=0.50={te_ac1s[idx_050]:.4f}; "
    f"Δ(0.45→0.50)={te_ac1_jump_045_050:+.4f}. "
    f"distinct_1 AC1: baseline={d1_ac1_baseline:.4f}, "
    f"α=0.40={d1_ac1s[idx_040]:.4f}, α=0.45={d1_ac1s[idx_045]:.4f}, α=0.50={d1_ac1s[idx_050]:.4f}; "
    f"Δ(0.45→0.50)={d1_ac1_jump_045_050:+.4f}. "
    f"token_entropy variance: baseline={te_var_baseline:.6f}, "
    f"α=0.45={te_vars[idx_045]:.6f}, α=0.50={te_vars[idx_050]:.6f}; "
    f"Δ(0.45→0.50)={te_var_jump_045_050:+.6f}."
)

results["csd_detected"] = bool(csd_detected)
results["onset_ac1_jump"] = onset_description
results["details"] = {
    "te_ac1_baseline_le035": round(te_ac1_baseline, 6),
    "d1_ac1_baseline_le035": round(d1_ac1_baseline, 6),
    "te_var_baseline_le035": round(float(te_var_baseline), 8),
    "d1_var_baseline_le035": round(float(d1_var_baseline), 10),
    "te_ac1_jump_045_to_050": round(te_ac1_jump_045_050, 6),
    "d1_ac1_jump_045_to_050": round(d1_ac1_jump_045_050, 6),
    "te_var_jump_045_to_050": round(float(te_var_jump_045_050), 8),
    "d1_var_jump_045_to_050": round(float(d1_var_jump_045_050), 10),
}

out_dir = Path("/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts")
with open(out_dir / "d127_csd_analysis.json", "w") as f:
    json.dump(results, f, indent=2)

print("=== Summary ===")
print(f"Alphas: {alphas}")
print(f"Token Entropy AC1:  {[f'{v:.4f}' for v in te_ac1s]}")
print(f"Token Entropy Var:  {[f'{v:.6f}' for v in te_vars]}")
print(f"Distinct-1 AC1:     {[f'{v:.4f}' for v in d1_ac1s]}")
print(f"Distinct-1 Var:     {[f'{v:.8f}' for v in d1_vars]}")
print(f"\nCSD Detected: {csd_detected}")
print(f"\n{onset_description}")

# === Plotting ===
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
alpha_labels = [str(a) for a in alphas]

# Top-left: Token Entropy AC1 vs α
ax = axes[0, 0]
ax.plot(alphas, te_ac1s, 'o-', color='#2171b5', linewidth=2, markersize=7)
ax.axvspan(0.45, 0.50, alpha=0.15, color='red', label='onset zone')
ax.set_xlabel('α (noise fraction)', fontsize=12)
ax.set_ylabel('AC1 (lag-1 autocorrelation)', fontsize=12)
ax.set_title('Token Entropy — AC1 vs α', fontsize=13, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Top-right: Token Entropy Variance vs α
ax = axes[0, 1]
ax.plot(alphas, te_vars, 's-', color='#cb181d', linewidth=2, markersize=7)
ax.axvspan(0.45, 0.50, alpha=0.15, color='red', label='onset zone')
ax.set_xlabel('α (noise fraction)', fontsize=12)
ax.set_ylabel('Variance', fontsize=12)
ax.set_title('Token Entropy — Variance vs α', fontsize=13, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Bottom-left: Distinct-1 AC1 vs α
ax = axes[1, 0]
ax.plot(alphas, d1_ac1s, 'o-', color='#2171b5', linewidth=2, markersize=7)
ax.axvspan(0.45, 0.50, alpha=0.15, color='red', label='onset zone')
ax.set_xlabel('α (noise fraction)', fontsize=12)
ax.set_ylabel('AC1 (lag-1 autocorrelation)', fontsize=12)
ax.set_title('Distinct-1 — AC1 vs α', fontsize=13, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Bottom-right: Distinct-1 Variance vs α
ax = axes[1, 1]
ax.plot(alphas, d1_vars, 's-', color='#cb181d', linewidth=2, markersize=7)
ax.axvspan(0.45, 0.50, alpha=0.15, color='red', label='onset zone')
ax.set_xlabel('α (noise fraction)', fontsize=12)
ax.set_ylabel('Variance', fontsize=12)
ax.set_title('Distinct-1 — Variance vs α', fontsize=13, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

fig.suptitle('D127: Critical Slowing Down (CSD) Indicators across α', fontsize=14, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.95])
fig.savefig(out_dir / "d127_csd_ac1_vs_alpha.png", dpi=150, bbox_inches='tight')
print(f"\nPlot saved to {out_dir / 'd127_csd_ac1_vs_alpha.png'}")
print(f"JSON saved to {out_dir / 'd127_csd_analysis.json'}")
