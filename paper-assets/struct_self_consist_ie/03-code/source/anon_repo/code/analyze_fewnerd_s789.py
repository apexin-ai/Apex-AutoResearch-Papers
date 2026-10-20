#!/usr/bin/env python3
"""Merge FewNERD seed789 shards + full 5-signal unified analysis."""
import json, os, sys
import numpy as np
from collections import Counter
from scipy.stats import spearmanr
from scipy.stats import rankdata

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import structural_consistency_soft_jaccard, fleiss_kappa_surface, _ner_soft_jaccard_pair, _extract_surface_keys
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie/output"
SHARDS = [
    f"{BASE}/exp_021_fewnerd_n8_seed789_shard{i}/samples.jsonl" for i in range(3)
]
OUT_DIR = f"{BASE}/fewnerd_seed789_merged"
MERGED_PATH = f"{OUT_DIR}/samples.jsonl"

sys.stdout = open(sys.stdout.fileno(), mode='w', buffering=1)

# ===== Step 1: Merge shards =====
print("Step 1: Merging shards...")
total_lines = 0
with open(MERGED_PATH, 'w') as out:
    for shard_path in SHARDS:
        count = 0
        with open(shard_path) as f:
            for line in f:
                if line.strip():
                    out.write(line)
                    count += 1
        print(f"  {shard_path}: {count} lines")
        total_lines += count
print(f"  Total merged: {total_lines} lines")
assert total_lines == 37648, f"Expected 37648, got {total_lines}"

# ===== Step 2: Load and filter =====
print("\nStep 2: Loading data...")
instances = []
with open(MERGED_PATH) as f:
    for line in f:
        if line.strip():
            instances.append(json.loads(line))
n_total = len(instances)

gold_filtered = [inst for inst in instances if inst["gold"].get("entities", [])]
n_filtered = len(gold_filtered)
print(f"  Total: {n_total}, Gold-filtered: {n_filtered}")

N_SAMPLES = len(gold_filtered[0]["samples"])
print(f"  N samples per instance: {N_SAMPLES}")

# ===== Step 3: Greedy, Oracle, Sample F1s =====
print("\nStep 3: Computing greedy/oracle F1...")
greedy_f1s = np.zeros(n_filtered)
oracle_f1s = np.zeros(n_filtered)
all_sample_f1s = np.zeros((n_filtered, N_SAMPLES))

for i, inst in enumerate(gold_filtered):
    greedy_f1s[i] = per_instance_f1(inst["greedy"], inst["gold"], subtask="ner")
    for j, s in enumerate(inst["samples"]):
        all_sample_f1s[i, j] = per_instance_f1(s, inst["gold"], subtask="ner")
    oracle_f1s[i] = all_sample_f1s[i].max()
    if (i+1) % 5000 == 0:
        print(f"  {i+1}/{n_filtered}")

greedy_macro = float(greedy_f1s.mean())
oracle_macro = float(oracle_f1s.mean())
headroom_pp = (oracle_macro - greedy_macro) * 100
zero_f1_mask = (all_sample_f1s.max(axis=1) == 0.0)
zero_f1_rate = float(zero_f1_mask.mean()) * 100

# Degeneracy: all N sample F1s identical
degen_flags = np.array([len(set(round(f, 10) for f in all_sample_f1s[i])) <= 1 for i in range(n_filtered)])
degen_rate = float(degen_flags.mean()) * 100

# LP range median
lp_ranges = []
for inst in gold_filtered:
    lps = [s.get("mean_logprob") for s in inst["samples"] if s.get("mean_logprob") is not None]
    if len(lps) >= 2:
        lp_ranges.append(max(lps) - min(lps))
lp_range_median = float(np.median(lp_ranges))

print(f"  Greedy F1: {greedy_macro:.4f}")
print(f"  Oracle F1: {oracle_macro:.4f}")
print(f"  Headroom: {headroom_pp:.2f}pp")
print(f"  Zero-F1 rate: {zero_f1_rate:.2f}%")
print(f"  Degeneracy rate: {degen_rate:.2f}%")

# ===== Step 4: 5 signals =====
print("\nStep 4: Computing 5 signals...")
lp_values = np.zeros(n_filtered)
sj_values = np.zeros(n_filtered)
fk_values = np.zeros(n_filtered)
em_values = np.zeros(n_filtered)
vc_values = np.zeros(n_filtered)

for i, inst in enumerate(gold_filtered):
    samples = inst["samples"]
    n = len(samples)

    # LP: mean of sample mean_logprobs
    lps = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    lp_values[i] = float(np.mean(lps)) if lps else float("nan")

    # SJ
    sj_values[i] = structural_consistency_soft_jaccard(samples, subtask="ner")

    # FK
    fk_values[i] = fleiss_kappa_surface(samples, subtask="ner")

    # EM: pairwise exact match rate
    sample_keys = []
    for s in samples:
        keys = frozenset((e.get("text",""), e.get("type","")) for e in s.get("entities", []))
        sample_keys.append(keys)
    match_count = sum(1 for a in range(n) for b in range(a+1, n) if sample_keys[a] == sample_keys[b])
    total_pairs = n*(n-1)//2
    em_values[i] = match_count / total_pairs if total_pairs > 0 else 1.0

    # VC: voting confidence
    counter = Counter()
    for s in samples:
        for e in s.get("entities", []):
            counter[(e.get("text",""), e.get("type",""))] += 1
    majority_votes = [v/n for v in counter.values() if v > n/2]
    vc_values[i] = float(np.mean(majority_votes)) if majority_votes else 0.0

    if (i+1) % 5000 == 0:
        print(f"  {i+1}/{n_filtered}")
print("  Signals computed.")

# ===== Step 5: Selection F1 =====
print("\nStep 5: Computing selection F1...")

# LP selection
lp_sel_f1 = np.zeros(n_filtered)
for i, inst in enumerate(gold_filtered):
    per_sample_lp = np.array([s.get("mean_logprob", float("-inf")) for s in inst["samples"]])
    best_idx = int(np.argmax(per_sample_lp))
    lp_sel_f1[i] = all_sample_f1s[i, best_idx]

# SJ selection (soft Jaccard with Hungarian span matching)
sj_sel_f1 = np.zeros(n_filtered)
for i, inst in enumerate(gold_filtered):
    samples = inst["samples"]
    n = len(samples)
    sj_matrix = np.zeros((n, n))
    for ii in range(n):
        for jj in range(ii + 1, n):
            s = _ner_soft_jaccard_pair(samples[ii].get("entities", []), samples[jj].get("entities", []))
            sj_matrix[ii][jj] = s
            sj_matrix[jj][ii] = s
    np.fill_diagonal(sj_matrix, 1.0)
    per_sample_sj = [float(np.mean([sj_matrix[k][j] for j in range(n) if j != k])) for k in range(n)]
    best_idx = int(np.argmax(per_sample_sj))
    sj_sel_f1[i] = all_sample_f1s[i, best_idx]
    if (i+1) % 10000 == 0:
        print(f"  SJ {i+1}/{n_filtered}")
print("  SJ done")

# EM selection
em_sel_f1 = np.zeros(n_filtered)
for i, inst in enumerate(gold_filtered):
    samples = inst["samples"]
    n = len(samples)
    sample_keys = [frozenset((e.get("text",""), e.get("type","")) for e in s.get("entities", [])) for s in samples]
    agreement = [sum(1 for j in range(n) if j != k and sample_keys[j] == sample_keys[k]) for k in range(n)]
    best_idx = int(np.argmax(agreement))
    em_sel_f1[i] = all_sample_f1s[i, best_idx]
print("  EM done")

# VC selection
vc_sel_f1 = np.zeros(n_filtered)
for i, inst in enumerate(gold_filtered):
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

# FK selection = EM mode selection
fk_sel_f1 = em_sel_f1.copy()
print("  FK done")

# ===== Step 6: Correlations + AUROC =====
print("\nStep 6: Correlations and AUROC...")
cond_mask = greedy_f1s > 0
signals_dict = {"LP": lp_values, "SJ": sj_values, "FK": fk_values, "EM": em_values, "VC": vc_values}
sel_f1_dict = {"LP": lp_sel_f1, "SJ": sj_sel_f1, "FK": fk_sel_f1, "EM": em_sel_f1, "VC": vc_sel_f1}

qe_results = {}
selection_results = {}
for sig_name, sig_arr in signals_dict.items():
    valid = np.isfinite(sig_arr) & np.isfinite(greedy_f1s)
    rho_g, p_g = spearmanr(sig_arr[valid], greedy_f1s[valid]) if valid.sum() > 2 else (float("nan"), float("nan"))

    cond_sig = sig_arr[cond_mask]
    cond_f1 = greedy_f1s[cond_mask]
    cond_valid = np.isfinite(cond_sig) & np.isfinite(cond_f1)
    rho_c, p_c = spearmanr(cond_sig[cond_valid], cond_f1[cond_valid]) if cond_valid.sum() > 2 else (float("nan"), float("nan"))

    # AUROC: oracle-based sample-level (matches other seeds)
    # Collect per-sample signal scores + oracle labels for this signal
    all_scores_sig = []
    all_labels_sig = []
    for idx in range(n_filtered):
        inst = gold_filtered[idx]
        samples = inst["samples"]
        n_s = len(samples)
        oracle_idx = int(np.argmax(all_sample_f1s[idx]))
        if sig_name == "LP":
            per_s = [s.get("mean_logprob", float("-inf")) for s in samples]
        elif sig_name == "SJ":
            sj_mat = np.zeros((n_s, n_s))
            for ii in range(n_s):
                for jj in range(ii+1, n_s):
                    sv = _ner_soft_jaccard_pair(samples[ii].get("entities",[]), samples[jj].get("entities",[]))
                    sj_mat[ii][jj] = sv
                    sj_mat[jj][ii] = sv
            np.fill_diagonal(sj_mat, 1.0)
            per_s = [float(np.mean([sj_mat[k][j] for j in range(n_s) if j!=k])) for k in range(n_s)]
        elif sig_name == "FK":
            ks = [frozenset(_extract_surface_keys(s, "ner")) for s in samples]
            fk_mat = np.zeros((n_s, n_s))
            for ii in range(n_s):
                for jj in range(ii+1, n_s):
                    union = len(ks[ii] | ks[jj])
                    inter = len(ks[ii] & ks[jj])
                    fk_mat[ii][jj] = inter/union if union > 0 else 1.0
                    fk_mat[jj][ii] = fk_mat[ii][jj]
            np.fill_diagonal(fk_mat, 1.0)
            per_s = [float(np.mean([fk_mat[k][j] for j in range(n_s) if j!=k])) for k in range(n_s)]
        elif sig_name == "EM":
            ks = [frozenset(_extract_surface_keys(s, "ner")) for s in samples]
            per_s = [float(sum(1 for j in range(n_s) if j!=k and ks[k]==ks[j])) for k in range(n_s)]
        elif sig_name == "VC":
            ks = [frozenset(_extract_surface_keys(s, "ner")) for s in samples]
            counter_tmp = {}
            for k_s in ks:
                for key in k_s:
                    counter_tmp[key] = counter_tmp.get(key, 0) + 1
            per_s = []
            for k_s in ks:
                if not k_s:
                    per_s.append(0.0)
                else:
                    per_s.append(float(np.mean([counter_tmp[key]/n_s for key in k_s])))
        else:
            per_s = [0.0] * n_s
        all_scores_sig.extend(per_s)
        all_labels_sig.extend([1 if k == oracle_idx else 0 for k in range(n_s)])
    all_scores_sig = np.array(all_scores_sig)
    all_labels_sig = np.array(all_labels_sig, dtype=int)
    if len(np.unique(all_labels_sig)) < 2 or len(np.unique(all_scores_sig)) < 2:
        auroc = float("nan")
    else:
        n_pos = (all_labels_sig == 1).sum()
        n_neg = (all_labels_sig == 0).sum()
        ranks = rankdata(all_scores_sig)
        u = ranks[all_labels_sig == 1].sum() - n_pos * (n_pos + 1) / 2
        auroc = float(u / (n_pos * n_neg))

    qe_results[sig_name] = {
        "auroc": round(auroc, 4) if not np.isnan(auroc) else None,
        "spearman_global": round(float(rho_g), 4),
        "spearman_global_p": float(p_g),
        "spearman_conditional": round(float(rho_c), 4),
        "spearman_conditional_p": float(p_c),
    }

    sel_macro = float(sel_f1_dict[sig_name].mean())
    delta_pp = (sel_macro - greedy_macro) * 100
    selection_results[sig_name] = {
        "f1": round(sel_macro, 4),
        "delta_pp": round(delta_pp, 4),
    }

# ===== Step 7: Bootstrap CI for each signal =====
print("\nStep 7: Bootstrap CI...")
np.random.seed(42)
N_BOOT = 2000
bootstrap_results = {}
for sig_name in ["LP", "SJ", "FK", "EM", "VC"]:
    sel_arr = sel_f1_dict[sig_name]
    deltas = []
    for _ in range(N_BOOT):
        idx = np.random.choice(n_filtered, size=n_filtered, replace=True)
        boot_delta = float(sel_arr[idx].mean() - greedy_f1s[idx].mean())
        deltas.append(boot_delta)
    deltas.sort()
    mean_d = float(np.mean(deltas)) * 100
    lo = deltas[int(0.025 * N_BOOT)] * 100
    hi = deltas[int(0.975 * N_BOOT)] * 100
    p_val = float(np.mean([d <= 0 for d in deltas]))
    bootstrap_results[sig_name] = {
        "mean_delta_pp": round(mean_d, 4),
        "ci_95_lo_pp": round(lo, 4),
        "ci_95_hi_pp": round(hi, 4),
        "p_value": round(p_val, 4),
        "significant_005": p_val < 0.05,
    }

# ===== Step 8: DGS (Degeneracy-Gated Selection) =====
print("\nStep 8: DGS...")
dgs_f1 = np.where(degen_flags, greedy_f1s, lp_sel_f1)
dgs_macro = float(dgs_f1.mean())
dgs_delta_pp = (dgs_macro - greedy_macro) * 100
dgs_vs_lp_pp = (dgs_macro - float(lp_sel_f1.mean())) * 100

# DGS bootstrap
dgs_boot_deltas = []
for _ in range(N_BOOT):
    idx = np.random.choice(n_filtered, size=n_filtered, replace=True)
    dgs_boot_deltas.append(float(dgs_f1[idx].mean() - greedy_f1s[idx].mean()))
dgs_boot_deltas.sort()

print(f"  DGS F1: {dgs_macro:.4f}")
print(f"  DGS delta vs greedy: {dgs_delta_pp:+.2f}pp")
print(f"  DGS delta vs LP: {dgs_vs_lp_pp:+.2f}pp")

# ===== Step 9: Entity type breakdown =====
print("\nStep 9: Entity type breakdown...")
entity_type_map = {}
for i, inst in enumerate(gold_filtered):
    for e in inst["gold"]["entities"]:
        etype = e.get("type", "unknown")
        if etype not in entity_type_map:
            entity_type_map[etype] = {"greedy": [], "oracle": [], "lp_sel": [], "zero_count": 0, "total": 0}
        entity_type_map[etype]["greedy"].append(greedy_f1s[i])
        entity_type_map[etype]["oracle"].append(oracle_f1s[i])
        entity_type_map[etype]["lp_sel"].append(lp_sel_f1[i])
        entity_type_map[etype]["total"] += 1
        if greedy_f1s[i] == 0:
            entity_type_map[etype]["zero_count"] += 1

entity_types = {}
for etype, data in sorted(entity_type_map.items()):
    entity_types[etype] = {
        "count": data["total"],
        "greedy_f1": round(float(np.mean(data["greedy"])), 4),
        "oracle_f1": round(float(np.mean(data["oracle"])), 4),
        "lp_selection_f1": round(float(np.mean(data["lp_sel"])), 4),
        "lp_delta_pp": round((float(np.mean(data["lp_sel"])) - float(np.mean(data["greedy"]))) * 100, 4),
        "zero_f1_rate": round(data["zero_count"] / data["total"] * 100, 1),
    }

# ===== Build output JSON (matching full_signal_analysis.json format) =====
result = {
    "meta": {
        "input": MERGED_PATH,
        "n_total": n_total,
        "n_filtered": n_filtered,
        "n_samples": N_SAMPLES,
    },
    "basic": {
        "greedy_macro_f1": greedy_macro,
        "oracle_macro_f1": oracle_macro,
        "headroom_pp": headroom_pp,
        "zero_f1_rate_pct": zero_f1_rate,
        "degeneracy_rate_pct": degen_rate,
        "lp_range_median": lp_range_median,
    },
    "qe": qe_results,
    "selection": selection_results,
    "bootstrap": bootstrap_results,
    "dgs": {
        "dgs_f1": round(dgs_macro, 4),
        "dgs_delta_vs_greedy_pp": round(dgs_delta_pp, 4),
        "dgs_delta_vs_lp_pp": round(dgs_vs_lp_pp, 4),
        "dgs_bootstrap_ci_95": {
            "lo_pp": round(dgs_boot_deltas[int(0.025 * N_BOOT)] * 100, 4),
            "hi_pp": round(dgs_boot_deltas[int(0.975 * N_BOOT)] * 100, 4),
        },
        "n_degenerate": int(degen_flags.sum()),
        "n_nondegenerate": int((~degen_flags).sum()),
    },
    "entity_types": entity_types,
}

# Save
analysis_path = f"{OUT_DIR}/analysis.json"
with open(analysis_path, "w") as f:
    json.dump(result, f, indent=2)
print(f"\nSaved analysis to {analysis_path}")

# Also save as full_signal_analysis.json for consistency with other seeds
fsa_path = f"{OUT_DIR}/full_signal_analysis.json"
with open(fsa_path, "w") as f:
    json.dump(result, f, indent=2)
print(f"Saved full_signal_analysis.json to {fsa_path}")

# ===== Summary =====
print(f"\n{'='*70}")
print("FEWNERD SEED789 ANALYSIS SUMMARY")
print(f"{'='*70}")
print(f"Instances: {n_total} total, {n_filtered} gold-filtered")
print(f"Greedy F1:     {greedy_macro:.4f}")
print(f"Oracle F1:     {oracle_macro:.4f}")
print(f"Headroom:      {headroom_pp:.2f}pp")
print(f"Degen rate:    {degen_rate:.2f}%")
print(f"Zero-F1 rate:  {zero_f1_rate:.2f}%")
print(f"\n{'Signal':<6} {'AUROC':>7} {'ρ_glob':>8} {'ρ_cond':>8} {'Sel F1':>8} {'Δpp':>8}")
print("-"*48)
for sig in ["LP", "SJ", "FK", "EM", "VC"]:
    q = qe_results[sig]
    s = selection_results[sig]
    auroc_str = f"{q['auroc']:>7.4f}" if q['auroc'] is not None else "   None"
    print(f"{sig:<6} {auroc_str} {q['spearman_global']:>8.4f} {q['spearman_conditional']:>8.4f} {s['f1']:>8.4f} {s['delta_pp']:>+8.2f}")
print(f"\nDGS F1: {dgs_macro:.4f} (Δ greedy: {dgs_delta_pp:+.2f}pp, Δ LP: {dgs_vs_lp_pp:+.2f}pp)")
print("DONE")
