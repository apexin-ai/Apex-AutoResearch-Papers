"""D-study: single-condition baseline for IRT comparison (Claim 3).

Computes G_item under three condition regimes:
  - multi_facet: original design (prec=3, temp=3, prompt=6, seed=6, ord=4)
  - reduced: halved (prec=2, temp=2, prompt=3, seed=3, ord=2)
  - single: IRT-like (all facets = 1)
"""
import json
from math import prod

INPUT  = "./results/analysis/llama_single_model_gstudy.json"
OUTPUT = "./results/exp001_analysis/dstudy_single_condition.json"

N_ACTUAL = 200  # items in original study

# Original design levels (verified from raw data)
ORIG_LEVELS = {
    "precision": 3, "temperature": 3,
    "prompt_template": 6, "seed": 6, "ordering": 4,
}
NON_ITEM_FACETS = list(ORIG_LEVELS.keys())

# --- Load variance components ---
with open(INPUT) as f:
    data = json.load(f)

correct = data["correct"]
total_var = correct["total_variance"]
pct = correct["components_pct"]

# Convert percentages to absolute variance estimates
vc = {k: total_var * v / 100.0 for k, v in pct.items()}

tau = vc["item_id"]
residual = vc["residual"]

print(f"tau (σ²_item) = {tau:.8f}")
print(f"residual      = {residual:.8f}")
print(f"total_var     = {total_var:.8f}")
print()


def compute_delta(vc, levels):
    """Relative error variance for given facet levels."""
    delta = 0.0
    terms = {}
    for comp, est in vc.items():
        if comp == "item_id" or est <= 0:
            continue
        parts = comp.split(":")
        if "item_id" in parts:
            other = [p for p in parts if p != "item_id"]
            divisor = prod(levels.get(f, 1) for f in other) if other else 1
            contrib = est / divisor
            terms[comp] = {"est": est, "divisor": divisor, "contrib": contrib}
            delta += contrib
        elif comp == "residual":
            divisor = prod(levels.get(f, 1) for f in NON_ITEM_FACETS)
            contrib = est / divisor
            terms["residual"] = {"est": est, "divisor": divisor, "contrib": contrib}
            delta += contrib
    return delta, terms


def dstudy_g(tau, delta, n_actual, n_target):
    if (tau + delta) <= 0:
        return 0.0
    return tau / (tau + delta * n_actual / n_target)


def find_min_items(tau, delta, n_actual, threshold=0.80, max_n=10000):
    for n in range(1, max_n + 1):
        if dstudy_g(tau, delta, n_actual, n) >= threshold:
            return n
    return None


# --- Three condition regimes ---
conditions_spec = {
    "multi_facet": {"precision": 3, "temperature": 3, "prompt_template": 6, "seed": 6, "ordering": 4},
    "reduced":     {"precision": 2, "temperature": 2, "prompt_template": 3, "seed": 3, "ordering": 2},
    "single":      {"precision": 1, "temperature": 1, "prompt_template": 1, "seed": 1, "ordering": 1},
}

n_items_list = [10, 20, 30, 50, 72, 75, 100, 116, 150, 200, 300, 500]

conditions_out = {}
curves_out = {"n_items": n_items_list}

for cname, levels in conditions_spec.items():
    delta, terms = compute_delta(vc, levels)
    g_at_200 = dstudy_g(tau, delta, N_ACTUAL, 200)
    min_g80 = find_min_items(tau, delta, N_ACTUAL)

    print(f"=== {cname} ===")
    print(f"  levels: {levels}")
    print(f"  delta = {delta:.8f}")
    print(f"  G(200) = {g_at_200:.4f}")
    print(f"  min items G≥0.80 = {min_g80}")
    print(f"  delta breakdown:")
    for comp, info in sorted(terms.items(), key=lambda x: -x[1]["contrib"]):
        pct_of_delta = info["contrib"] / delta * 100 if delta > 0 else 0
        print(f"    {comp:30s}: {info['est']:.8f} / {info['divisor']:>5d} = {info['contrib']:.8f} ({pct_of_delta:.1f}%)")
    print()

    curve = [round(dstudy_g(tau, delta, N_ACTUAL, n), 4) for n in n_items_list]
    conditions_out[cname] = {
        "levels": levels,
        "delta": round(delta, 8),
        "g_at_200": round(g_at_200, 4),
        "min_items_g80": min_g80,
        "delta_breakdown": {
            comp: {"estimate": round(info["est"], 8), "divisor": info["divisor"],
                   "contribution": round(info["contrib"], 8)}
            for comp, info in sorted(terms.items(), key=lambda x: -x[1]["contrib"])
        }
    }
    curves_out[cname] = curve

# Monotonicity check
for cname in conditions_spec:
    vals = curves_out[cname]
    assert all(vals[i] <= vals[i+1] for i in range(len(vals)-1)), \
        f"{cname}: G not monotonically increasing: {vals}"
print("Monotonicity check: PASSED for all conditions\n")

# --- Key findings ---
single_delta = conditions_out["single"]["delta"]
multi_delta = conditions_out["multi_facet"]["delta"]

key = {
    "single_g_at_200": round(dstudy_g(tau, single_delta, N_ACTUAL, 200), 4),
    "single_min_items_g80": conditions_out["single"]["min_items_g80"],
    "single_g_at_116": round(dstudy_g(tau, single_delta, N_ACTUAL, 116), 4),
    "multi_g_at_72": round(dstudy_g(tau, multi_delta, N_ACTUAL, 72), 4),
    "multi_g_at_200": round(dstudy_g(tau, multi_delta, N_ACTUAL, 200), 4),
    "delta_ratio_single_vs_multi": round(single_delta / multi_delta, 2),
    "items_ratio_single_vs_multi": (
        f"{conditions_out['single']['min_items_g80']} vs {conditions_out['multi_facet']['min_items_g80']}"
    ),
}

print("=== Key findings ===")
for k, v in key.items():
    print(f"  {k}: {v}")

# --- Assemble output ---
output = {
    "analysis": "dstudy_single_condition",
    "description": "D-study comparing multi-facet averaged G vs single-condition G for fair IRT baseline",
    "n_actual_items": N_ACTUAL,
    "variance_components": {k: round(v, 8) for k, v in sorted(vc.items(), key=lambda x: -x[1])},
    "tau_item": round(tau, 8),
    "conditions": conditions_out,
    "dstudy_curves": curves_out,
    "key_findings": key,
}

with open(OUTPUT, "w") as f:
    json.dump(output, f, indent=2)

print(f"\nSaved: {OUTPUT}")
