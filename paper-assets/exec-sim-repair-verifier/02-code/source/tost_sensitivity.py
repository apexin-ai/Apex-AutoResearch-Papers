"""TOST equivalence margin sensitivity analysis (Dream A6)."""
import json
import numpy as np
from scipy.stats import t as t_dist
from scipy.optimize import brentq

OUTPUT_PATH = "artifacts/tost_sensitivity.json"
MARGINS = [1.0, 1.5, 2.0, 3.0, 5.0]
ALPHA = 0.05


def tost_paired(mean_d, se_d, n, delta):
    """Compute paired TOST p-value."""
    df = n - 1
    t_upper = (mean_d - delta) / se_d
    t_lower = (mean_d + delta) / se_d
    p_upper = t_dist.cdf(t_upper, df)
    p_lower = 1 - t_dist.cdf(t_lower, df)
    p_tost = max(p_upper, p_lower)
    return p_tost


# --- Qwen3-4B: reverse-engineer SE_d from known p=0.007 at delta=2 ---
# mean_d = 1.24, n=5, df=4, delta=2, p_TOST=0.007
# The binding test is upper: p_upper = P(T_4 < (1.24-2)/SE_d) = 0.007
# Solve: t_dist.cdf((1.24 - 2)/se, 4) = 0.007

def solve_se_qwen(se):
    return t_dist.cdf((1.24 - 2.0) / se, 4) - 0.007

se_qwen = brentq(solve_se_qwen, 0.01, 2.0)
print(f"Qwen3-4B: reverse-engineered SE_d = {se_qwen:.4f}")
print(f"  Implied sd_d = {se_qwen * np.sqrt(5):.4f}")

# Verify
p_verify = tost_paired(1.24, se_qwen, 5, 2.0)
print(f"  Verification: TOST p at delta=2 = {p_verify:.4f} (should be ~0.007)")

# --- DeepSeek-coder-6.7B: compute from paired differences ---
d_deepseek = np.array([1.16, -1.11])
mean_d_ds = d_deepseek.mean()
sd_d_ds = d_deepseek.std(ddof=1)
se_d_ds = sd_d_ds / np.sqrt(2)
print(f"\nDeepSeek-6.7B: mean_d={mean_d_ds:.4f}, sd_d={sd_d_ds:.4f}, SE_d={se_d_ds:.4f}")

# --- Compute TOST for all margins ---
results = {
    "metadata": {
        "purpose": "Dream A6: TOST margin sensitivity",
        "date": "2026-05-17",
        "method": "Paired TOST (Two One-Sided Tests)",
        "alpha": ALPHA,
        "note": "Qwen SE_d reverse-engineered from known p=0.007 at delta=2pp"
    },
    "qwen3_4b": {
        "n_seeds": 5,
        "mean_cls": 88.43,
        "mean_cwm": 87.19,
        "mean_diff": 1.24,
        "se_d": round(se_qwen, 4),
        "implied_sd_d": round(se_qwen * np.sqrt(5), 4),
        "margins": []
    },
    "deepseek_6_7b": {
        "n_seeds": 2,
        "mean_cls": 86.85,
        "mean_cwm": 86.83,
        "mean_diff": round(float(mean_d_ds), 4),
        "se_d": round(float(se_d_ds), 4),
        "sd_d": round(float(sd_d_ds), 4),
        "paired_diffs": [1.16, -1.11],
        "margins": []
    }
}

print("\n--- Results ---")
print(f"{'Margin':<8} {'Qwen3-4B p':<14} {'Qwen eq?':<10} {'DeepSeek p':<14} {'DS eq?':<10} {'Both?'}")
print("-" * 70)

table_lines = ["| Margin (pp) | Qwen3-4B p | Qwen eq? | DeepSeek p | DS eq? | Both equivalent? |",
               "|---|---|---|---|---|---|"]

for delta in MARGINS:
    p_qwen = tost_paired(1.24, se_qwen, 5, delta)
    eq_qwen = p_qwen < ALPHA

    p_ds = tost_paired(float(mean_d_ds), float(se_d_ds), 2, delta)
    eq_ds = p_ds < ALPHA

    both = eq_qwen and eq_ds

    results["qwen3_4b"]["margins"].append({
        "delta_pp": delta,
        "tost_p": round(p_qwen, 6),
        "equivalent": bool(eq_qwen)
    })
    results["deepseek_6_7b"]["margins"].append({
        "delta_pp": delta,
        "tost_p": round(p_ds, 6),
        "equivalent": bool(eq_ds)
    })

    print(f"±{delta:<7} {p_qwen:<14.6f} {'Yes' if eq_qwen else 'No':<10} {p_ds:<14.6f} {'Yes' if eq_ds else 'No':<10} {'Yes' if both else 'No'}")
    table_lines.append(f"| ±{delta} | {p_qwen:.4f} | {'Yes' if eq_qwen else 'No'} | {p_ds:.4f} | {'Yes' if eq_ds else 'No'} | {'Yes' if both else 'No'} |")

results["summary_table"] = "\n".join(table_lines)

# Find minimum margin for equivalence (p < 0.05)
for model_key, mean_d, se_d, n in [("qwen3_4b", 1.24, se_qwen, 5),
                                      ("deepseek_6_7b", float(mean_d_ds), float(se_d_ds), 2)]:
    try:
        def find_min_margin(delta):
            return tost_paired(mean_d, se_d, n, delta) - ALPHA
        min_delta = brentq(find_min_margin, abs(mean_d) + 0.001, 10.0)
        results[model_key]["min_margin_for_equivalence"] = round(min_delta, 3)
        print(f"\n{model_key}: minimum margin for equivalence (p<0.05) = ±{min_delta:.3f}pp")
    except Exception as e:
        results[model_key]["min_margin_for_equivalence"] = None
        print(f"\n{model_key}: could not find minimum margin: {e}")

# Save
import os
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
with open(OUTPUT_PATH, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to {OUTPUT_PATH}")
