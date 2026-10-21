#!/usr/bin/env python3
"""TOST sensitivity analysis at ±1pp, ±2pp, ±3pp margins."""
import json, math
from scipy.stats import norm

with open("/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/table1_bh_correction.json") as f:
    data = json.load(f)

conditions = data["conditions"]

def derive_se(cond):
    """Derive SE of proportion difference from McNemar z-statistic.

    For raw_p < 1.0: SE = |delta| / |z| where z from two-sided p.
    For raw_p = 1.0: estimate using paired proportion model with assumed
    correlation r=0.95 between methods (reasonable for similar prompting variants).
    """
    delta = cond["delta_pp"] / 100.0
    n = cond["n"]
    raw_p = cond["raw_p"]

    if raw_p < 1.0 and abs(delta) > 1e-10:
        z = abs(norm.ppf(raw_p / 2.0))
        se = abs(delta) / z
        return se, "derived"
    else:
        # Estimate SE from accuracy levels with assumed inter-method correlation
        p1 = cond["sc_pct"] / 100.0
        p2 = cond["sica_pct"] / 100.0
        var1 = p1 * (1 - p1)
        var2 = p2 * (1 - p2)
        r = 0.95  # conservative correlation for near-identical methods
        cov = r * math.sqrt(var1 * var2)
        var_diff = (var1 + var2 - 2 * cov) / n
        se = math.sqrt(max(var_diff, 1e-12))
        return se, "estimated_r095"


def tost(delta_pp, se, margin_pp):
    """Two one-sided tests for equivalence within ±margin_pp."""
    delta = delta_pp / 100.0
    margin = margin_pp / 100.0

    z_lower = (delta + margin) / se  # test H0: delta <= -margin
    z_upper = (margin - delta) / se  # test H0: delta >= +margin

    p_lower = 1.0 - norm.cdf(z_lower)
    p_upper = 1.0 - norm.cdf(z_upper)

    tost_p = max(p_lower, p_upper)
    return tost_p


def classify(tost_p, delta_pp, margin_pp, raw_p):
    if tost_p < 0.05:
        return "equivalent"
    elif abs(delta_pp) > margin_pp and raw_p < 0.05:
        return "genuinely_different"
    else:
        return "underpowered"


margins = [1, 2, 3]
results = []

for cond in conditions:
    se, se_method = derive_se(cond)

    entry = {
        "model": cond["model"],
        "dataset": cond["dataset"],
        "n": cond["n"],
        "delta_pp": cond["delta_pp"],
        "raw_p": cond["raw_p"],
        "se": round(se, 6),
        "se_method": se_method,
    }

    for m in margins:
        p = tost(cond["delta_pp"], se, m)
        cls = classify(p, cond["delta_pp"], m, cond["raw_p"])
        entry[f"tost_{m}pp"] = {
            "p": round(float(p), 6),
            "equivalent": bool(p < 0.05),
            "classification": cls,
        }

    results.append(entry)

# Summary
summary = {}
for m in margins:
    key = f"{m}pp"
    n_eq = sum(1 for r in results if r[f"tost_{m}pp"]["classification"] == "equivalent")
    n_diff = sum(1 for r in results if r[f"tost_{m}pp"]["classification"] == "genuinely_different")
    n_under = sum(1 for r in results if r[f"tost_{m}pp"]["classification"] == "underpowered")
    summary[key] = {
        "n_equivalent": n_eq,
        "n_different": n_diff,
        "n_underpowered": n_under,
    }

output = {
    "margins_pp": margins,
    "method": "TOST via paired proportion z-test. SE derived from McNemar z-statistic where raw_p < 1.0; "
              "estimated via paired proportion model (r=0.95 inter-method correlation) where raw_p = 1.0.",
    "conditions": results,
    "summary": summary,
}

outpath = "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/tost_sensitivity.json"
with open(outpath, "w") as f:
    json.dump(output, f, indent=2)

# Print summary table
print(f"{'Margin':<10} {'Equivalent':<12} {'Different':<12} {'Underpowered':<12}")
print("-" * 46)
for m in margins:
    s = summary[f"{m}pp"]
    print(f"±{m}pp      {s['n_equivalent']:<12} {s['n_different']:<12} {s['n_underpowered']:<12}")

print(f"\nPer-condition details:")
print(f"{'Model':<20} {'Dataset':<15} {'Δpp':>6} {'SE':>8} {'SE src':>12}  {'±1pp':>8} {'±2pp':>8} {'±3pp':>8}")
print("-" * 95)
for r in results:
    t1 = r["tost_1pp"]
    t2 = r["tost_2pp"]
    t3 = r["tost_3pp"]
    def fmt(t):
        if t["classification"] == "equivalent":
            return f"✓ {t['p']:.3f}"
        elif t["classification"] == "genuinely_different":
            return f"✗ {t['p']:.3f}"
        else:
            return f"? {t['p']:.3f}"
    print(f"{r['model']:<20} {r['dataset']:<15} {r['delta_pp']:>6.2f} {r['se']:>8.5f} {r['se_method']:>12}  {fmt(t1):>8} {fmt(t2):>8} {fmt(t3):>8}")
