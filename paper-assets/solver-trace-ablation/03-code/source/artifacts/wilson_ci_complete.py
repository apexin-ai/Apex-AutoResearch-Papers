#!/usr/bin/env python3
"""Complete Wilson CI analysis with all taxonomy data."""
import json
import csv
import math
from scipy import stats
from collections import OrderedDict

def wilson_ci(k, n, alpha=0.05):
    if n == 0:
        return (0.0, 0.0, 0.0)
    p = k / n
    z = stats.norm.ppf(1 - alpha / 2)
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (p, max(0, c - m), min(1, c + m))

def fisher_test(a, b, c, d):
    table = [[a, b], [c, d]]
    odds_ratio, p_value = stats.fisher_exact(table)
    return odds_ratio, p_value

# ============================================================
# RAW DATA (all verified via classify_h7.py or registry)
# ============================================================

data = OrderedDict()

# ISR β=0.1
data["ISR_b01"] = {
    "label": "ISR β=0.1",
    "seeds": {
        "s42": {"n": 81, "h7": 13, "h1": 42, "genuine": 26, "source": "classify_h7.py"},
        "s43": {"n": 61, "h7": 59, "h1": 0, "genuine": 2, "source": "derived (100% single_premise, h7_rate=0.967)"},
        "s44": {"n": 89, "h7": 77, "h1": 0, "genuine": 12, "source": "classify_h7.py"},
    }
}

# Random β=0.1
data["Random_b01"] = {
    "label": "Random β=0.1",
    "seeds": {
        "s42": {"n": 79, "h7": 0, "h1": 56, "genuine": 23, "source": "classify_h7.py"},
        "s43-r2": {"n": 88, "h7": 0, "h1": 82, "genuine": 6, "source": "registry"},
        # s44: DATA UNAVAILABLE - no eval JSON, no checkpoint (disk cleanup casualty)
    },
    "missing": ["s44 (eval JSON + checkpoint both cleaned)"]
}

# Exec-only
data["Exec_only"] = {
    "label": "Exec-only",
    "seeds": {
        "s42-r2": {"n": 93, "h7": 0, "h1": 81, "genuine": 12, "source": "classify_h7.py"},
        "s43-r4": {"n": 13, "h7": 0, "h1": 13, "genuine": 0, "source": "classify_h7.py"},
        "s44": {"n": 98, "h7": 98, "h1": 0, "genuine": 0, "source": "classify_h7.py (plan001_s44_eval_sta.json)"},
    }
}

# ISR β=0.3
data["ISR_b03"] = {
    "label": "ISR β=0.3",
    "seeds": {
        "s42": {"n": 18, "h7": 0, "h1": 14, "genuine": 4, "source": "registry (plan002-additive-b03-s42)"},
        "s43-r3": {"n": 86, "h7": 4, "h1": 59, "genuine": 23, "source": "classify_h7.py"},
        "s44-r2": {"n": 95, "h7": 95, "h1": 0, "genuine": 0, "source": "classify_h7.py (eval_sta_correct.json)"},
    }
}

# Random β=0.3
data["Random_b03"] = {
    "label": "Random β=0.3",
    "seeds": {
        "s43-r4": {"n": 92, "h7": 0, "h1": 89, "genuine": 3, "source": "classify_h7.py"},
        "s44-r2": {"n": 23, "h7": 0, "h1": 23, "genuine": 0, "source": "classify_h7.py"},
    },
    "missing": ["s42 (experiment does not exist)"]
}

# SFT
data["SFT"] = {
    "label": "SFT",
    "seeds": {
        "s42-r4": {"n": 14, "h7": 0, "h1": 1, "genuine": 13, "source": "registry"},
        "s43": {"n": 15, "h7": 0, "h1": 1, "genuine": 14, "source": "registry"},
    },
    "missing": ["s44 (still RUNNING)"]
}

# ============================================================
# COMPUTE POOLED + WILSON CI
# ============================================================

results = OrderedDict()

for cond_key, cond_data in data.items():
    seeds = cond_data["seeds"]
    label = cond_data["label"]

    # Per-seed Wilson CI
    seed_results = []
    for seed_name, sd in seeds.items():
        n = sd["n"]
        row = {
            "condition": label,
            "seed": seed_name,
            "n_proved": n,
            "h7_count": sd["h7"],
            "h1_count": sd["h1"],
            "genuine_count": sd["genuine"],
            "source": sd["source"],
        }
        for cat in ["h7", "h1", "genuine"]:
            k = sd[cat]
            p, lo, hi = wilson_ci(k, n)
            row[f"{cat}_rate"] = round(p, 4)
            row[f"{cat}_ci_lo"] = round(lo, 4)
            row[f"{cat}_ci_hi"] = round(hi, 4)

        # Verify sum
        row["sum_check"] = sd["h7"] + sd["h1"] + sd["genuine"] == n
        seed_results.append(row)

    # Pooled
    pool_n = sum(sd["n"] for sd in seeds.values())
    pool_h7 = sum(sd["h7"] for sd in seeds.values())
    pool_h1 = sum(sd["h1"] for sd in seeds.values())
    pool_gen = sum(sd["genuine"] for sd in seeds.values())

    pooled_row = {
        "condition": label,
        "seed": "POOLED",
        "n_proved": pool_n,
        "h7_count": pool_h7,
        "h1_count": pool_h1,
        "genuine_count": pool_gen,
        "source": f"pooled ({len(seeds)} seeds)",
    }
    for cat, k in [("h7", pool_h7), ("h1", pool_h1), ("genuine", pool_gen)]:
        p, lo, hi = wilson_ci(k, pool_n)
        pooled_row[f"{cat}_rate"] = round(p, 4)
        pooled_row[f"{cat}_ci_lo"] = round(lo, 4)
        pooled_row[f"{cat}_ci_hi"] = round(hi, 4)
    pooled_row["sum_check"] = pool_h7 + pool_h1 + pool_gen == pool_n

    results[cond_key] = {
        "label": label,
        "per_seed": seed_results,
        "pooled": pooled_row,
        "missing": cond_data.get("missing", []),
    }

# ============================================================
# FISHER EXACT TESTS
# ============================================================

fisher_results = []

# ISR b01 vs Random b01 (genuine)
isr_b01_pool = results["ISR_b01"]["pooled"]
rand_b01_pool = results["Random_b01"]["pooled"]
a = isr_b01_pool["genuine_count"]
b = isr_b01_pool["n_proved"] - a
c = rand_b01_pool["genuine_count"]
d = rand_b01_pool["n_proved"] - c
or_val, p_val = fisher_test(a, b, c, d)
fisher_results.append({
    "comparison": "ISR_b01 vs Random_b01",
    "metric": "genuine",
    "table": f"[{a},{b}],[{c},{d}]",
    "odds_ratio": round(or_val, 4),
    "p_value": round(p_val, 6),
    "significant_005": p_val < 0.05,
})

# ISR b01 vs Exec-only (genuine)
exec_pool = results["Exec_only"]["pooled"]
a = isr_b01_pool["genuine_count"]
b = isr_b01_pool["n_proved"] - a
c = exec_pool["genuine_count"]
d = exec_pool["n_proved"] - c
or_val, p_val = fisher_test(a, b, c, d)
fisher_results.append({
    "comparison": "ISR_b01 vs Exec_only",
    "metric": "genuine",
    "table": f"[{a},{b}],[{c},{d}]",
    "odds_ratio": round(or_val, 4),
    "p_value": round(p_val, 6),
    "significant_005": p_val < 0.05,
})

# ISR b01 vs SFT (genuine)
sft_pool = results["SFT"]["pooled"]
a = isr_b01_pool["genuine_count"]
b = isr_b01_pool["n_proved"] - a
c = sft_pool["genuine_count"]
d = sft_pool["n_proved"] - c
or_val, p_val = fisher_test(a, b, c, d)
fisher_results.append({
    "comparison": "ISR_b01 vs SFT",
    "metric": "genuine",
    "table": f"[{a},{b}],[{c},{d}]",
    "odds_ratio": round(or_val, 4),
    "p_value": round(p_val, 6),
    "significant_005": p_val < 0.05,
})

# Random b01 vs Exec-only (genuine)
a = rand_b01_pool["genuine_count"]
b = rand_b01_pool["n_proved"] - a
c = exec_pool["genuine_count"]
d = exec_pool["n_proved"] - c
or_val, p_val = fisher_test(a, b, c, d)
fisher_results.append({
    "comparison": "Random_b01 vs Exec_only",
    "metric": "genuine",
    "table": f"[{a},{b}],[{c},{d}]",
    "odds_ratio": round(or_val, 4),
    "p_value": round(p_val, 6),
    "significant_005": p_val < 0.05,
})

# ISR b03 vs Random b03 (genuine)
isr_b03_pool = results["ISR_b03"]["pooled"]
rand_b03_pool = results["Random_b03"]["pooled"]
a = isr_b03_pool["genuine_count"]
b = isr_b03_pool["n_proved"] - a
c = rand_b03_pool["genuine_count"]
d = rand_b03_pool["n_proved"] - c
or_val, p_val = fisher_test(a, b, c, d)
fisher_results.append({
    "comparison": "ISR_b03 vs Random_b03",
    "metric": "genuine",
    "table": f"[{a},{b}],[{c},{d}]",
    "odds_ratio": round(or_val, 4),
    "p_value": round(p_val, 6),
    "significant_005": p_val < 0.05,
})

# H7 comparisons
# ISR b01 vs Random b01 (h7)
a = isr_b01_pool["h7_count"]
b = isr_b01_pool["n_proved"] - a
c = rand_b01_pool["h7_count"]
d = rand_b01_pool["n_proved"] - c
or_val, p_val = fisher_test(a, b, c, d)
fisher_results.append({
    "comparison": "ISR_b01 vs Random_b01",
    "metric": "h7",
    "table": f"[{a},{b}],[{c},{d}]",
    "odds_ratio": round(or_val, 4) if not math.isinf(or_val) else "inf",
    "p_value": round(p_val, 6),
    "significant_005": p_val < 0.05,
})

# ISR b01 vs Exec-only (h7)
a = isr_b01_pool["h7_count"]
b = isr_b01_pool["n_proved"] - a
c = exec_pool["h7_count"]
d = exec_pool["n_proved"] - c
or_val, p_val = fisher_test(a, b, c, d)
fisher_results.append({
    "comparison": "ISR_b01 vs Exec_only",
    "metric": "h7",
    "table": f"[{a},{b}],[{c},{d}]",
    "odds_ratio": round(or_val, 4),
    "p_value": round(p_val, 6),
    "significant_005": p_val < 0.05,
})

# ============================================================
# HETEROGENEITY (per-seed rate variance)
# ============================================================

heterogeneity = {}
for cond_key, cond_res in results.items():
    seeds = cond_res["per_seed"]
    if len(seeds) < 2:
        continue
    het = {}
    for cat in ["h7", "h1", "genuine"]:
        rates = [s[f"{cat}_rate"] for s in seeds]
        rate_range = max(rates) - min(rates)
        rate_mean = sum(rates) / len(rates)
        rate_var = sum((r - rate_mean) ** 2 for r in rates) / len(rates)
        het[cat] = {
            "rates": [round(r, 4) for r in rates],
            "range": round(rate_range, 4),
            "variance": round(rate_var, 6),
            "mean": round(rate_mean, 4),
        }
    heterogeneity[cond_key] = het

# ============================================================
# OUTPUT
# ============================================================

# CSV
csv_path = "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci_complete.csv"
fieldnames = [
    "condition", "seed", "n_proved",
    "h7_count", "h7_rate", "h7_ci_lo", "h7_ci_hi",
    "h1_count", "h1_rate", "h1_ci_lo", "h1_ci_hi",
    "genuine_count", "genuine_rate", "genuine_ci_lo", "genuine_ci_hi",
    "source"
]
with open(csv_path, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
    w.writeheader()
    for cond_key, cond_res in results.items():
        for row in cond_res["per_seed"]:
            w.writerow(row)
        w.writerow(cond_res["pooled"])
        # Blank row between conditions
        w.writerow({})

# JSON
json_path = "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci_complete.json"
output = {
    "generated": "2026-05-15",
    "method": "Wilson score interval (alpha=0.05)",
    "conditions": results,
    "fisher_exact_tests": fisher_results,
    "heterogeneity": heterogeneity,
    "data_notes": {
        "ISR_b01_s43": "Derived from registry: proved_single_premise_ratio=1.0, h7_rate_calibrated=0.967. No eval JSON or checkpoint available.",
        "Random_b01_s44": "DATA UNAVAILABLE. Eval JSON and checkpoint both cleaned up in disk cleanup incident.",
        "Random_b03_s42": "Experiment does not exist in registry.",
        "SFT_s44": "Still RUNNING at time of analysis.",
        "Exec_only_s44": "Registry says n=98; used plan001_s44_eval_sta.json (98 proved, 98 H7).",
        "ISR_b03_s44_r2": "Used eval_sta_correct.json (n=95); original eval dir has n=98 from wrong test set.",
        "Random_b03_s43_r4_fix": "Registry had h7=7,h1=90,genuine=2 (sum=99≠92). classify_h7.py confirms h7=0,h1=89,genuine=3 (sum=92).",
        "ISR_b01_s42_fix": "Registry had genuine_count=25 (sum=80≠81). classify_h7.py confirms genuine=26 (sum=81).",
    },
    "registry_corrections": [
        {"exp_id": "plan002-additive-b01-s42", "field": "genuine_count", "old": 25, "new": 26},
        {"exp_id": "plan001-exec-only-s44", "field": "h7_count", "old": 97, "new": 98},
        {"exp_id": "exp1-random-b03-s43-r4", "field": "h7_count", "old": 7, "new": 0},
        {"exp_id": "exp1-random-b03-s43-r4", "field": "h1_count", "old": 90, "new": 89},
        {"exp_id": "exp1-random-b03-s43-r4", "field": "genuine_count", "old": 2, "new": 3},
    ],
}
with open(json_path, "w") as f:
    json.dump(output, f, indent=2, default=str)

# ============================================================
# PRINT TABLES
# ============================================================

print("=" * 90)
print("  PER-SEED TABLE")
print("=" * 90)
print(f"{'Condition':<16} {'Seed':<10} {'n':>4}  {'H7':>4} {'H7%':>7} {'H7 CI':>15}  {'H1':>4} {'H1%':>7} {'H1 CI':>15}  {'Gen':>4} {'Gen%':>7} {'Gen CI':>15}")
print("-" * 130)
for cond_key, cond_res in results.items():
    for row in cond_res["per_seed"]:
        print(f"{row['condition']:<16} {row['seed']:<10} {row['n_proved']:>4}  "
              f"{row['h7_count']:>4} {row['h7_rate']:>6.1%} [{row['h7_ci_lo']:.3f},{row['h7_ci_hi']:.3f}]  "
              f"{row['h1_count']:>4} {row['h1_rate']:>6.1%} [{row['h1_ci_lo']:.3f},{row['h1_ci_hi']:.3f}]  "
              f"{row['genuine_count']:>4} {row['genuine_rate']:>6.1%} [{row['genuine_ci_lo']:.3f},{row['genuine_ci_hi']:.3f}]")
    if cond_res.get("missing"):
        for m in cond_res["missing"]:
            print(f"{cond_res['label']:<16} {m}")
    print()

print("=" * 90)
print("  POOLED TABLE (with Wilson 95% CI)")
print("=" * 90)
print(f"{'Condition':<16} {'n':>4} {'seeds':>5}  {'H7%':>7} {'H7 CI':>15}  {'H1%':>7} {'H1 CI':>15}  {'Gen%':>7} {'Gen CI':>15}")
print("-" * 110)
for cond_key, cond_res in results.items():
    p = cond_res["pooled"]
    n_seeds = len(cond_res["per_seed"])
    note = ""
    if cond_res.get("missing"):
        note = f"  [{n_seeds}/{n_seeds + len(cond_res['missing'])} seeds]"
    print(f"{p['condition']:<16} {p['n_proved']:>4} {n_seeds:>5}  "
          f"{p['h7_rate']:>6.1%} [{p['h7_ci_lo']:.3f},{p['h7_ci_hi']:.3f}]  "
          f"{p['h1_rate']:>6.1%} [{p['h1_ci_lo']:.3f},{p['h1_ci_hi']:.3f}]  "
          f"{p['genuine_rate']:>6.1%} [{p['genuine_ci_lo']:.3f},{p['genuine_ci_hi']:.3f}]{note}")

print()
print("=" * 90)
print("  FISHER EXACT TESTS")
print("=" * 90)
print(f"{'Comparison':<30} {'Metric':<10} {'Table':>25}  {'OR':>8} {'p-value':>12} {'Sig?':>5}")
print("-" * 100)
for ft in fisher_results:
    sig = "*" if ft["significant_005"] else ""
    print(f"{ft['comparison']:<30} {ft['metric']:<10} {ft['table']:>25}  {ft['odds_ratio']:>8} {ft['p_value']:>12.6f} {sig:>5}")

print()
print("=" * 90)
print("  SEED HETEROGENEITY")
print("=" * 90)
for cond_key, het in heterogeneity.items():
    label = results[cond_key]["label"]
    print(f"\n{label}:")
    for cat in ["h7", "h1", "genuine"]:
        h = het[cat]
        print(f"  {cat:>8}: rates={h['rates']}  range={h['range']:.4f}  var={h['variance']:.6f}  mean={h['mean']:.4f}")

print()
print(f"CSV written to: {csv_path}")
print(f"JSON written to: {json_path}")
