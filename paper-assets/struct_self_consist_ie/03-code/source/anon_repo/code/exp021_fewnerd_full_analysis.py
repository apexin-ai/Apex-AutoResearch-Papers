#!/usr/bin/env python3
"""Full 5-signal SCS analysis for exp_021 Few-NERD (N=8, 37648 instances).
Optimized for large-scale: avoids per-sample SJ recomputation."""
import json, os, sys
import numpy as np
from collections import Counter
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import structural_consistency_soft_jaccard, fleiss_kappa_surface
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl"
OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference"

# Force unbuffered output
sys.stdout = open(sys.stdout.fileno(), mode='w', buffering=1)

print("Loading data...")
instances = []
with open(DATA_PATH) as f:
    for line in f:
        if line.strip():
            instances.append(json.loads(line))
n_total = len(instances)
print(f"Total instances: {n_total}")

# ===== Phase 1: Greedy and Oracle F1 =====
print("Phase 1: Computing greedy/oracle F1...")
greedy_f1s = np.zeros(n_total)
oracle_f1s = np.zeros(n_total)
all_sample_f1s = np.zeros((n_total, 8))  # N=8

for i, inst in enumerate(instances):
    greedy_f1s[i] = per_instance_f1(inst["greedy"], inst["gold"], subtask="ner")
    for j, s in enumerate(inst["samples"]):
        all_sample_f1s[i, j] = per_instance_f1(s, inst["gold"], subtask="ner")
    oracle_f1s[i] = all_sample_f1s[i].max()
    if (i+1) % 5000 == 0:
        print(f"  {i+1}/{n_total}")

greedy_macro_f1 = float(greedy_f1s.mean())
oracle_macro_f1 = float(oracle_f1s.mean())
headroom = oracle_macro_f1 - greedy_macro_f1
zero_f1_mask = (all_sample_f1s.max(axis=1) == 0.0)
zero_f1_rate = float(zero_f1_mask.mean())

print(f"Greedy macro F1: {greedy_macro_f1:.4f}")
print(f"Oracle macro F1: {oracle_macro_f1:.4f}")
print(f"Headroom: {headroom:.4f}")
print(f"Zero-F1 rate: {zero_f1_rate:.4f} ({int(zero_f1_mask.sum())}/{n_total})")

# ===== Phase 2: 5 signals (instance-level) =====
print("\nPhase 2: Computing 5 signals...")
lp_values = np.zeros(n_total)
sj_values = np.zeros(n_total)
fk_values = np.zeros(n_total)
em_values = np.zeros(n_total)
vc_values = np.zeros(n_total)

for i, inst in enumerate(instances):
    samples = inst["samples"]
    n = len(samples)
    
    # LP
    lps = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    lp_values[i] = float(np.mean(lps)) if lps else float("nan")
    
    # SJ
    sj_values[i] = structural_consistency_soft_jaccard(samples, subtask="ner")
    
    # FK
    fk_values[i] = fleiss_kappa_surface(samples, subtask="ner")
    
    # EM (pairwise exact match rate)
    sample_keys = []
    for s in samples:
        keys = frozenset((e.get("text",""), e.get("type","")) for e in s.get("entities", []))
        sample_keys.append(keys)
    match_count = sum(1 for a in range(n) for b in range(a+1, n) if sample_keys[a] == sample_keys[b])
    total_pairs = n*(n-1)//2
    em_values[i] = match_count / total_pairs if total_pairs > 0 else 1.0
    
    # VC
    counter = Counter()
    for s in samples:
        for e in s.get("entities", []):
            counter[(e.get("text",""), e.get("type",""))] += 1
    majority_votes = [v/n for v in counter.values() if v > n/2]
    vc_values[i] = float(np.mean(majority_votes)) if majority_votes else 0.0
    
    if (i+1) % 5000 == 0:
        print(f"  {i+1}/{n_total}")

print("Signals computed.")

# ===== Phase 3: Selection F1 =====
print("\nPhase 3: Computing selection F1...")

# LP selection: pick sample with highest mean_logprob
lp_sel_f1 = np.zeros(n_total)
for i, inst in enumerate(instances):
    per_sample_lp = np.array([s.get("mean_logprob", float("-inf")) for s in inst["samples"]])
    best_idx = int(np.argmax(per_sample_lp))
    lp_sel_f1[i] = all_sample_f1s[i, best_idx]

# EM/FK selection: pick sample that matches most others (mode)
em_sel_f1 = np.zeros(n_total)
for i, inst in enumerate(instances):
    samples = inst["samples"]
    n = len(samples)
    sample_keys = [frozenset((e.get("text",""), e.get("type","")) for e in s.get("entities", [])) for s in samples]
    agreement = [sum(1 for j in range(n) if j != k and sample_keys[j] == sample_keys[k]) for k in range(n)]
    best_idx = int(np.argmax(agreement))
    em_sel_f1[i] = all_sample_f1s[i, best_idx]
print("  EM done")

# VC selection: pick sample with highest entity support
vc_sel_f1 = np.zeros(n_total)
for i, inst in enumerate(instances):
    samples = inst["samples"]
    n = len(samples)
    entity_counter = Counter()
    for s in samples:
        for e in s.get("entities", []):
            entity_counter[(e.get("text",""), e.get("type",""))] += 1
    per_sample_vc = []
    for s in samples:
        ents = [(e.get("text",""), e.get("type","")) for e in s.get("entities", [])]
        if ents:
            per_sample_vc.append(float(np.mean([entity_counter[ent]/n for ent in ents])))
        else:
            per_sample_vc.append(0.0)
    best_idx = int(np.argmax(per_sample_vc))
    vc_sel_f1[i] = all_sample_f1s[i, best_idx]
print("  VC done")

# SJ selection: pick sample with highest avg soft-jaccard to others
# Approximate: use entity overlap fraction vs consensus
sj_sel_f1 = np.zeros(n_total)
for i, inst in enumerate(instances):
    samples = inst["samples"]
    n = len(samples)
    # Build entity sets per sample
    sample_sets = []
    for s in samples:
        eset = set()
        for e in s.get("entities", []):
            eset.add((e.get("text",""), e.get("type","")))
        sample_sets.append(eset)
    # Avg jaccard of each sample vs all others
    per_sample_sj = []
    for k in range(n):
        jaccards = []
        for j in range(n):
            if j == k:
                continue
            inter = len(sample_sets[k] & sample_sets[j])
            union = len(sample_sets[k] | sample_sets[j])
            jaccards.append(inter/union if union > 0 else 1.0)
        per_sample_sj.append(float(np.mean(jaccards)) if jaccards else 0.0)
    best_idx = int(np.argmax(per_sample_sj))
    sj_sel_f1[i] = all_sample_f1s[i, best_idx]
    if (i+1) % 10000 == 0:
        print(f"  SJ {i+1}/{n_total}")
print("  SJ done")

# FK selection = same as EM (both use agreement/mode)
fk_sel_f1 = em_sel_f1.copy()
print("  FK done (same as EM mode selection)")

selection_results = {
    "LP": float(lp_sel_f1.mean()),
    "SJ": float(sj_sel_f1.mean()),
    "FK": float(fk_sel_f1.mean()),
    "EM": float(em_sel_f1.mean()),
    "VC": float(vc_sel_f1.mean()),
}

# ===== Phase 4: Correlations =====
print("\nPhase 4: Correlations...")
cond_mask = greedy_f1s > 0
cond_f1 = greedy_f1s[cond_mask]

signals_dict = {"LP": lp_values, "SJ": sj_values, "FK": fk_values, "EM": em_values, "VC": vc_values}
corr_results = {}
for sig_name, sig_arr in signals_dict.items():
    valid = np.isfinite(sig_arr) & np.isfinite(greedy_f1s)
    rho, p = spearmanr(sig_arr[valid], greedy_f1s[valid]) if valid.sum() > 2 else (float("nan"), float("nan"))
    
    cond_sig = sig_arr[cond_mask]
    cond_valid = np.isfinite(cond_sig) & np.isfinite(cond_f1)
    cond_rho, cond_p = spearmanr(cond_sig[cond_valid], cond_f1[cond_valid]) if cond_valid.sum() > 2 else (float("nan"), float("nan"))
    
    corr_results[sig_name] = {
        "global_rho": round(float(rho), 4),
        "global_p": float(p),
        "conditional_rho": round(float(cond_rho), 4),
        "conditional_p": float(cond_p),
    }

# ===== Phase 5: Bootstrap CI for LP delta =====
print("\nPhase 5: Bootstrap CI for LP delta...")
np.random.seed(42)
n_bootstrap = 1000
lp_deltas_bootstrap = []
for _ in range(n_bootstrap):
    idx = np.random.choice(n_total, size=n_total, replace=True)
    boot_sel = float(lp_sel_f1[idx].mean())
    boot_greedy = float(greedy_f1s[idx].mean())
    lp_deltas_bootstrap.append(boot_sel - boot_greedy)

lp_delta_ci_low = float(np.percentile(lp_deltas_bootstrap, 2.5))
lp_delta_ci_high = float(np.percentile(lp_deltas_bootstrap, 97.5))
lp_delta_mean = float(np.mean(lp_deltas_bootstrap))

# ===== Summary =====
print("\n" + "="*70)
print("EXP-021 FEW-NERD FULL ANALYSIS SUMMARY")
print("="*70)
print(f"Instances: {n_total}")
print(f"N (samples per instance): 8")
print(f"Greedy macro F1: {greedy_macro_f1:.4f}")
print(f"Oracle macro F1: {oracle_macro_f1:.4f}")
print(f"Headroom (oracle - greedy): {headroom:.4f}")
print(f"Zero-F1 rate: {zero_f1_rate:.4f} ({int(zero_f1_mask.sum())}/{n_total})")
print(f"F1>0 instances: {int(cond_mask.sum())}/{n_total}")
print()
print(f"{'Signal':<6} {'Global ρ':>10} {'Cond ρ':>10} {'Sel F1':>10} {'Δ vs greedy':>12}")
print("-"*52)
for sig_name in ["LP", "SJ", "FK", "EM", "VC"]:
    g_rho = corr_results[sig_name]["global_rho"]
    c_rho = corr_results[sig_name]["conditional_rho"]
    s_f1 = selection_results[sig_name]
    delta = s_f1 - greedy_macro_f1
    print(f"{sig_name:<6} {g_rho:>10.4f} {c_rho:>10.4f} {s_f1:>10.4f} {delta:>+12.4f}")
print()
print(f"LP delta 95% CI: [{lp_delta_ci_low:.4f}, {lp_delta_ci_high:.4f}]")
print(f"LP delta mean (bootstrap): {lp_delta_mean:.4f}")

# Save
results = {
    "dataset": "fewnerd",
    "experiment": "exp_021",
    "n_total": n_total,
    "n_samples_per_instance": 8,
    "greedy_macro_f1": round(greedy_macro_f1, 4),
    "oracle_macro_f1": round(oracle_macro_f1, 4),
    "headroom": round(headroom, 4),
    "zero_f1_rate": round(zero_f1_rate, 4),
    "n_zero_f1": int(zero_f1_mask.sum()),
    "n_f1_positive": int(cond_mask.sum()),
    "signals": {},
    "lp_delta_bootstrap": {
        "mean": round(lp_delta_mean, 4),
        "ci_95_low": round(lp_delta_ci_low, 4),
        "ci_95_high": round(lp_delta_ci_high, 4),
    },
}
for sig_name in ["LP", "SJ", "FK", "EM", "VC"]:
    results["signals"][sig_name] = {
        "global_rho": corr_results[sig_name]["global_rho"],
        "global_p": corr_results[sig_name]["global_p"],
        "conditional_rho": corr_results[sig_name]["conditional_rho"],
        "conditional_p": corr_results[sig_name]["conditional_p"],
        "selection_f1": round(selection_results[sig_name], 4),
        "selection_delta": round(selection_results[sig_name] - greedy_macro_f1, 4),
    }

out_path = os.path.join(OUTPUT_DIR, "exp021_full_analysis.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to {out_path}")
print("DONE")
