import json
import os
import csv
import numpy as np
from itertools import permutations
from scipy.stats import spearmanr

DATA_DIR = "/root/entrainment_gated_ft/lm_eval_clean/xstorycloze/"
OUT_DIR = "/root/entrainment_gated_ft/analysis/"

ARCHS = ["GatedDeltaNet", "RetNet", "HGRN2"]
ARCH_SHORT = {"GatedDeltaNet": "GDN", "RetNet": "RetNet", "HGRN2": "HGRN2"}
CONFIGS = [
    ("pure", 0.0),
    ("hybrid-24-1", 1/25),
    ("hybrid-12-1", 1/13),
    ("hybrid-6-1", 1/7),
    ("hybrid-3-1", 1/4),
]

def load_acc(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path) as f:
        data = json.load(f)
    return data["results"]["xstorycloze_en"]["acc,none"]

def exact_spearman_p(x, y):
    rho_obs = spearmanr(x, y).statistic
    n = len(x)
    all_perms = list(permutations(range(n)))
    count = sum(1 for perm in all_perms
                if abs(spearmanr(x, [y[i] for i in perm]).statistic) >= abs(rho_obs))
    return rho_obs, count / len(all_perms)

# --- Load all data ---
results = {}  # results[arch][config_name] = acc
for arch in ARCHS:
    results[arch] = {}
    for cfg_name, ratio in CONFIGS:
        fname = f"1.3B-100B-{arch}-{cfg_name}.json"
        results[arch][cfg_name] = load_acc(fname)

transformer_acc = load_acc("transformer_1.3B_baseline.json")

# --- Build table ---
ratios = [r for _, r in CONFIGS]
config_names = [c for c, _ in CONFIGS]

rows = []
for i, (cfg_name, ratio) in enumerate(CONFIGS):
    accs = [results[arch][cfg_name] for arch in ARCHS]
    std = np.std(accs, ddof=0)  # population std across 3 archs
    row = {
        "attention_ratio": ratio,
        "GDN_acc": results["GatedDeltaNet"][cfg_name],
        "RetNet_acc": results["RetNet"][cfg_name],
        "HGRN2_acc": results["HGRN2"][cfg_name],
        "cross_arch_std": std,
        "Transformer_acc": transformer_acc,
    }
    rows.append(row)

# --- CSV output ---
csv_path = os.path.join(OUT_DIR, "xstorycloze_convergence_results.csv")
with open(csv_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["attention_ratio", "GDN_acc", "RetNet_acc", "HGRN2_acc", "cross_arch_std", "Transformer_acc"])
    writer.writeheader()
    writer.writerows(rows)

# --- Spearman: std vs attention_ratio ---
stds = [row["cross_arch_std"] for row in rows]
rho, p_exact = exact_spearman_p(ratios, stds)

print("=" * 70)
print("xstorycloze_en Convergence Analysis")
print("=" * 70)
print()
print(f"{'Config':<12} {'Ratio':<8} {'GDN':<8} {'RetNet':<8} {'HGRN2':<8} {'Std':<10} {'Transformer':<8}")
print("-" * 70)
for i, (cfg_name, ratio) in enumerate(CONFIGS):
    r = rows[i]
    print(f"{cfg_name:<12} {ratio:<8.4f} {r['GDN_acc']:<8.4f} {r['RetNet_acc']:<8.4f} {r['HGRN2_acc']:<8.4f} {r['cross_arch_std']:<10.6f} {r['Transformer_acc']:<8.4f}")

print()
print(f"Spearman (std vs attention_ratio): rho={rho:.4f}, exact_p={p_exact:.4f}")
print()

# --- Unified multi-benchmark correction ---
# Previous 9 benchmarks raw p-values (exact permutation two-tailed)
prev_benchmarks = {
    "LAMBADA":       {"rho": -1.0, "raw_p": 0.0167},
    "HellaSwag":     {"rho":  0.3, "raw_p": 0.6833},
    "WinoGrande":    {"rho":  0.1, "raw_p": 0.95},
    "ARC-Easy":      {"rho": -0.7, "raw_p": 0.2333},
    "ARC-Challenge": {"rho":  0.6, "raw_p": 0.35},
    "MMLU":          {"rho": -0.7, "raw_p": 0.2333},
    "boolq":         {"rho":  0.2, "raw_p": 0.7833},
    "piqa":          {"rho": -0.5, "raw_p": 0.45},
    "sciq":          {"rho":  0.1, "raw_p": 0.95},
}

# Add xstorycloze_en
all_benchmarks = dict(prev_benchmarks)
all_benchmarks["xstorycloze_en"] = {"rho": rho, "raw_p": p_exact}

# COPA (supplementary, not in main 10)
# Compute COPA supplementary from raw exp011 data
copa_archs = ["GatedDeltaNet", "RetNet", "HGRN2"]
copa_configs = CONFIGS
copa_dir = "/root/entrainment_gated_ft/lm_eval_clean/exp011"
copa_stds = []
for cfg_name, ratio in copa_configs:
    copa_accs = []
    for arch in copa_archs:
        fname = f"1.3B-100B-{arch}-{cfg_name}.json"
        with open(os.path.join(copa_dir, fname)) as f:
            copa_data = json.load(f)
        copa_accs.append(copa_data["results"]["copa"]["acc,none"])
    copa_stds.append(np.std(copa_accs, ddof=0))
copa_ratios = [r for _, r in copa_configs]
copa_rho, copa_p = exact_spearman_p(copa_ratios, copa_stds)
copa_supp = {"rho": round(copa_rho, 4), "raw_p": round(copa_p, 4)}

n_tests = 10  # main benchmarks

# Bonferroni correction (10 tests)
print("=" * 70)
print(f"Unified Multiple Comparison Correction (n={n_tests} main benchmarks)")
print("=" * 70)
print()

bonf_results = {}
for bm, vals in all_benchmarks.items():
    bonf_p = min(vals["raw_p"] * n_tests, 1.0)
    bonf_results[bm] = bonf_p

# BH-FDR correction
sorted_bms = sorted(all_benchmarks.items(), key=lambda x: x[1]["raw_p"])
bh_results = {}
for rank, (bm, vals) in enumerate(sorted_bms, 1):
    bh_p = min(vals["raw_p"] * n_tests / rank, 1.0)
    bh_results[bm] = bh_p

# Enforce monotonicity (BH step-up)
sorted_bh = sorted(bh_results.items(), key=lambda x: all_benchmarks[x[0]]["raw_p"], reverse=True)
running_min = 1.0
for bm, p in sorted_bh:
    running_min = min(running_min, p)
    bh_results[bm] = running_min

print(f"{'Benchmark':<18} {'rho':<8} {'raw_p':<10} {'Bonf_p':<10} {'BH_p':<10} {'Sig?':<6}")
print("-" * 62)
for bm, vals in sorted(all_benchmarks.items(), key=lambda x: x[1]["raw_p"]):
    sig = "***" if bonf_results[bm] < 0.05 else ("*" if bh_results[bm] < 0.05 else "")
    print(f"{bm:<18} {vals['rho']:<8.2f} {vals['raw_p']:<10.4f} {bonf_results[bm]:<10.4f} {bh_results[bm]:<10.4f} {sig:<6}")

# 2-benchmark Bonferroni (LAMBADA + xstorycloze_en) if xstorycloze is significant
print()
print("=" * 70)
print("2-Benchmark Bonferroni (LAMBADA + xstorycloze_en)")
print("=" * 70)
lambada_2bonf = min(prev_benchmarks["LAMBADA"]["raw_p"] * 2, 1.0)
xstory_2bonf = min(p_exact * 2, 1.0)
print(f"LAMBADA:        raw_p={prev_benchmarks['LAMBADA']['raw_p']:.4f}, 2-Bonf_p={lambada_2bonf:.4f}")
print(f"xstorycloze_en: raw_p={p_exact:.4f}, 2-Bonf_p={xstory_2bonf:.4f}")

if xstory_2bonf < 0.05:
    print("=> Both survive 2-benchmark Bonferroni at alpha=0.05")
elif lambada_2bonf < 0.05 and xstory_2bonf >= 0.05:
    print("=> Only LAMBADA survives 2-benchmark Bonferroni")
else:
    print("=> Neither survives 2-benchmark Bonferroni")

# --- JSON summary ---
summary = {
    "xstorycloze_en": {
        "per_config": {},
        "spearman_rho": rho,
        "exact_p": p_exact,
        "direction": "convergence increases with attention" if rho < 0 else "convergence decreases with attention" if rho > 0 else "no trend",
    },
    "all_10_benchmarks": {},
    "copa_supplementary": copa_supp,
    "correction_10_benchmark": {
        "n_tests": n_tests,
        "bonferroni": {},
        "bh_fdr": {},
    },
    "correction_2_benchmark_lambada_xstorycloze": {
        "LAMBADA": {"raw_p": prev_benchmarks["LAMBADA"]["raw_p"], "bonf2_p": lambada_2bonf},
        "xstorycloze_en": {"raw_p": p_exact, "bonf2_p": xstory_2bonf},
    },
    "conclusion": "",
}

for i, (cfg_name, ratio) in enumerate(CONFIGS):
    summary["xstorycloze_en"]["per_config"][cfg_name] = {
        "attention_ratio": ratio,
        "GDN": results["GatedDeltaNet"][cfg_name],
        "RetNet": results["RetNet"][cfg_name],
        "HGRN2": results["HGRN2"][cfg_name],
        "cross_arch_std": rows[i]["cross_arch_std"],
        "Transformer": transformer_acc,
    }

for bm, vals in all_benchmarks.items():
    summary["all_10_benchmarks"][bm] = {
        "rho": vals["rho"],
        "raw_p": vals["raw_p"],
        "bonferroni_p": bonf_results[bm],
        "bh_fdr_p": bh_results[bm],
        "significant_bonferroni": bonf_results[bm] < 0.05,
        "significant_bh": bh_results[bm] < 0.05,
    }

summary["correction_10_benchmark"]["bonferroni"] = {bm: bonf_results[bm] for bm in all_benchmarks}
summary["correction_10_benchmark"]["bh_fdr"] = {bm: bh_results[bm] for bm in all_benchmarks}

# Conclusion
sig_bonf = [bm for bm in all_benchmarks if bonf_results[bm] < 0.05]
sig_bh = [bm for bm in all_benchmarks if bh_results[bm] < 0.05]
conclusion_parts = []
conclusion_parts.append(f"xstorycloze_en: rho={rho:.4f}, exact_p={p_exact:.4f}")
if bonf_results["xstorycloze_en"] < 0.05:
    conclusion_parts.append("xstorycloze_en IS significant after 10-benchmark Bonferroni correction")
else:
    conclusion_parts.append("xstorycloze_en is NOT significant after 10-benchmark Bonferroni correction")
conclusion_parts.append(f"Significant benchmarks (Bonferroni): {sig_bonf if sig_bonf else 'none'}")
conclusion_parts.append(f"Significant benchmarks (BH-FDR): {sig_bh if sig_bh else 'none'}")
if xstory_2bonf < 0.05:
    conclusion_parts.append("xstorycloze_en survives 2-benchmark Bonferroni with LAMBADA => viable second anchor")
else:
    conclusion_parts.append("xstorycloze_en does NOT survive even 2-benchmark Bonferroni => NOT a viable second anchor")
summary["conclusion"] = "; ".join(conclusion_parts)

json_path = os.path.join(OUT_DIR, "all_benchmark_convergence_summary.json")
with open(json_path, "w") as f:
    json.dump(summary, f, indent=2)

print()
print("=" * 70)
print("CONCLUSION")
print("=" * 70)
for part in conclusion_parts:
    print(f"  - {part}")
print()
print(f"Output CSV: {csv_path}")
print(f"Output JSON: {json_path}")
