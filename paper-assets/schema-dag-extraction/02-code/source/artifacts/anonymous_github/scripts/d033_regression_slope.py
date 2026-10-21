import json, numpy as np
from scipy.stats import linregress

with open('./artifacts/fewrel_16rel_bootstrap/results.json') as f:
    data = json.load(f)

bcs_arr = np.array([b['bcs'] for b in data])
acc_arr = np.array([b['accuracy'] for b in data])

slope, intercept, r_value, p_value, stderr = linregress(bcs_arr, acc_arr)

rng = np.random.default_rng(42)
n = len(bcs_arr)
boot_slopes = []
for _ in range(1000):
    idx = rng.choice(n, n, replace=True)
    s, _, _, _, _ = linregress(bcs_arr[idx], acc_arr[idx])
    boot_slopes.append(s)
ci_lower, ci_upper = np.percentile(boot_slopes, [2.5, 97.5])

result = {
    "experiment": "D033 (exp_fewrel_16rel_bootstrap)",
    "n_batches": int(n),
    "bcs_range": [float(bcs_arr.min()), float(bcs_arr.max())],
    "acc_range": [float(acc_arr.min()), float(acc_arr.max())],
    "regression": {
        "slope": float(slope),
        "intercept": float(intercept),
        "r_squared": float(r_value**2),
        "r_value": float(r_value),
        "p_value": float(p_value),
        "stderr": float(stderr),
        "bootstrap_slope_ci_95": [float(ci_lower), float(ci_upper)]
    },
    "interpretation": f"Each +0.1 BCS -> {slope*0.1*100:.2f}pp accuracy change"
}

with open('./artifacts/fewrel_16rel_bootstrap/regression_slope.json', 'w') as f:
    json.dump(result, f, indent=2)

print(json.dumps(result, indent=2))
