"""Intermediate D-study table from exp-001 single-model 6-facet VCs."""
import json
import math

TAU = 0.1271120031  # sigma^2(item_id)
ITEM_INTERACTIONS = {
    "precision": 0.0071904578,
    "temperature": 0.0063796481,
    "prompt_template": 0.0118973392,
    "seed": 0.0102602214,
    "ordering": 0.0016752615,
}
RESIDUAL = 0.0502927384
N_STUDY = 200


def compute_sigma_delta(n_prec, n_temp, n_prompt, n_seed, n_ordering):
    return (
        ITEM_INTERACTIONS["precision"] / n_prec
        + ITEM_INTERACTIONS["temperature"] / n_temp
        + ITEM_INTERACTIONS["prompt_template"] / n_prompt
        + ITEM_INTERACTIONS["seed"] / n_seed
        + ITEM_INTERACTIONS["ordering"] / n_ordering
        + RESIDUAL / (n_prec * n_temp * n_prompt * n_seed * n_ordering)
    )


def g_at_n(delta, n_items):
    """G(n) = tau*n / (tau*n + N_study*delta) — Spearman-Brown projection."""
    return TAU * n_items / (TAU * n_items + N_STUDY * delta)


def n_for_target_g(delta, target_g):
    """Minimum items for G >= target_g."""
    return math.ceil(target_g * N_STUDY * delta / ((1 - target_g) * TAU))


designs = [
    {"name": "Single-condition (typical)", "n_prec": 1, "n_temp": 1, "n_prompt": 1, "n_seed": 1, "n_ordering": 1},
    {"name": "Minimal upgrade",           "n_prec": 1, "n_temp": 1, "n_prompt": 2, "n_seed": 1, "n_ordering": 1},
    {"name": "Easy upgrade",              "n_prec": 1, "n_temp": 1, "n_prompt": 2, "n_seed": 2, "n_ordering": 1},
    {"name": "Moderate",                  "n_prec": 1, "n_temp": 1, "n_prompt": 3, "n_seed": 3, "n_ordering": 1},
    {"name": "Standard",                  "n_prec": 1, "n_temp": 2, "n_prompt": 4, "n_seed": 4, "n_ordering": 1},
    {"name": "Enhanced",                  "n_prec": 1, "n_temp": 1, "n_prompt": 6, "n_seed": 6, "n_ordering": 2},
    {"name": "Full multi-facet",          "n_prec": 3, "n_temp": 3, "n_prompt": 6, "n_seed": 6, "n_ordering": 4},
]

# Compute
results = []
prev_g = -1.0
for d in designs:
    delta = compute_sigma_delta(d["n_prec"], d["n_temp"], d["n_prompt"], d["n_seed"], d["n_ordering"])
    g200 = g_at_n(delta, 200)
    ng80 = n_for_target_g(delta, 0.80)
    total_cond = d["n_prec"] * d["n_temp"] * d["n_prompt"] * d["n_seed"] * d["n_ordering"]

    # Monotonicity check: G@200 should increase as conditions increase
    # (only for designs that strictly dominate in all facets)

    results.append({
        "name": d["name"],
        "n_precision": d["n_prec"],
        "n_temperature": d["n_temp"],
        "n_prompt": d["n_prompt"],
        "n_seed": d["n_seed"],
        "n_ordering": d["n_ordering"],
        "total_conditions_per_item": total_cond,
        "sigma_delta": round(delta, 10),
        "g_at_200": round(g200, 6),
        "n_for_g80": ng80,
    })

# Validate anchors
assert abs(results[0]["g_at_200"] - 0.592) < 0.005, f"Single-condition anchor fail: {results[0]['g_at_200']}"
assert abs(results[-1]["g_at_200"] - 0.936) < 0.005, f"Full multi-facet anchor fail: {results[-1]['g_at_200']}"

# Monotonicity: verify G increases down the list
for i in range(1, len(results)):
    assert results[i]["g_at_200"] >= results[i-1]["g_at_200"], \
        f"Monotonicity fail: {results[i-1]['name']} ({results[i-1]['g_at_200']}) > {results[i]['name']} ({results[i]['g_at_200']})"

# Also compute G projection curves for selected item counts
item_counts = [25, 50, 75, 100, 150, 200, 300, 500, 1000]
for r in results:
    r["g_projections"] = {str(n): round(g_at_n(r["sigma_delta"], n), 6) for n in item_counts}

output = {
    "source": "exp-001 single-model (Llama-3.1-8B-Instruct) MMLU, Henderson I 6-facet, 259200 records",
    "method": "D-study with Spearman-Brown projection for item count",
    "formula": "G(n) = tau*n / (tau*n + N_study*delta), delta = sum(vc_facet:item / n_facet) + residual / prod(n_facets)",
    "N_study": N_STUDY,
    "variance_components": {
        "tau_item_id": TAU,
        "precision_x_item": ITEM_INTERACTIONS["precision"],
        "temperature_x_item": ITEM_INTERACTIONS["temperature"],
        "prompt_template_x_item": ITEM_INTERACTIONS["prompt_template"],
        "seed_x_item": ITEM_INTERACTIONS["seed"],
        "ordering_x_item": ITEM_INTERACTIONS["ordering"],
        "residual": RESIDUAL,
    },
    "note_on_precision_facet": "The original study has 6 facets including precision (FP16/BF16/FP32). "
        "For practical designs (rows 1-6), precision is fixed at 1 level (practitioners use one precision). "
        "The Full multi-facet row uses all 3 precision levels to match the study's full design.",
    "designs": results,
}

print(json.dumps(output, indent=2))
