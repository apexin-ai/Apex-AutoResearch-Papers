"""Diagnose logprob rho discrepancy between exp-001 and exp-012.

Factors to disentangle:
(a) Instance subset (200 vs 529)
(b) Temperature (T=0.7 vs T=1.0)
(c) N samples (16 vs 8) -> averaging stability
(d) Logprob normalization (verified identical: per-token mean)
"""

import json
import sys
import numpy as np
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from evaluation import per_instance_f1

EXP001_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42_200only_backup/samples.jsonl"
EXP012_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl"
OUTPUT_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/logprob_diagnosis/diagnosis.json"


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def compute_logprob_rho(instances, subtask="ner", source="exp012"):
    """Compute Spearman rho between mean_logprob and greedy F1."""
    field = "entities" if subtask == "ner" else "relations"
    
    logprobs = []
    f1s = []
    
    for inst in instances:
        if not inst["gold"].get(field):
            continue
        
        f1 = per_instance_f1(inst["greedy"], inst["gold"], subtask)
        
        if source == "exp012":
            lp = float(np.mean([s["mean_logprob"] for s in inst["samples"]]))
        elif source == "exp001":
            if "logprobs" in inst:
                lp = float(np.mean(inst["logprobs"]))
            else:
                lp = float(np.mean([s["mean_logprob"] for s in inst["samples"]]))
        else:
            raise ValueError(f"Unknown source: {source}")
        
        logprobs.append(lp)
        f1s.append(f1)
    
    if len(logprobs) < 3:
        return {"rho": 0.0, "p": 1.0, "n": len(logprobs)}
    
    r = spearmanr(logprobs, f1s)
    return {"rho": float(r.statistic), "p": float(r.pvalue), "n": len(logprobs)}


def main():
    print("Loading data...")
    exp001 = load_jsonl(EXP001_PATH)
    exp012 = load_jsonl(EXP012_PATH)
    
    print(f"exp-001: {len(exp001)} instances (N=16, T=0.7)")
    print(f"exp-012: {len(exp012)} instances (N=8, T=1.0)")
    
    # Build ID maps
    exp001_ids = {inst["id"] for inst in exp001}
    exp012_by_id = {inst["id"]: inst for inst in exp012}
    
    # Find overlap
    overlap_ids = exp001_ids & set(exp012_by_id.keys())
    print(f"Overlapping instances: {len(overlap_ids)}")
    
    exp012_overlap = [exp012_by_id[id_] for id_ in sorted(overlap_ids)]
    exp001_overlap = [inst for inst in exp001 if inst["id"] in overlap_ids]
    
    # Also get non-overlapping exp-012 instances
    exp012_nonoverlap = [inst for inst in exp012 if inst["id"] not in overlap_ids]
    
    report = {"summary": {}, "tests": {}}
    
    # ========== TEST 1: Baseline reproduction ==========
    print("\n=== TEST 1: Reproduce reported rho values ===")
    
    for subtask in ["ner", "re"]:
        r001 = compute_logprob_rho(exp001, subtask, "exp001")
        r012 = compute_logprob_rho(exp012, subtask, "exp012")
        print(f"  {subtask.upper()} exp-001 (200, N=16, T=0.7): rho={r001['rho']:.4f}, n={r001['n']}")
        print(f"  {subtask.upper()} exp-012 (529, N=8, T=1.0):  rho={r012['rho']:.4f}, n={r012['n']}")
        report["tests"][f"baseline_{subtask}"] = {"exp001": r001, "exp012": r012}
    
    # ========== TEST 2: Instance subset effect ==========
    # Use exp-012 data (N=8, T=1.0) but only on 200-instance subset
    print("\n=== TEST 2: Instance subset effect (exp-012 data, 200-instance overlap) ===")
    
    for subtask in ["ner", "re"]:
        r_overlap = compute_logprob_rho(exp012_overlap, subtask, "exp012")
        r_full = compute_logprob_rho(exp012, subtask, "exp012")
        r_nonoverlap = compute_logprob_rho(exp012_nonoverlap, subtask, "exp012")
        
        print(f"  {subtask.upper()} exp-012 overlap (200):     rho={r_overlap['rho']:.4f}, n={r_overlap['n']}")
        print(f"  {subtask.upper()} exp-012 full (529):        rho={r_full['rho']:.4f}, n={r_full['n']}")
        print(f"  {subtask.upper()} exp-012 non-overlap (329): rho={r_nonoverlap['rho']:.4f}, n={r_nonoverlap['n']}")
        
        report["tests"][f"subset_effect_{subtask}"] = {
            "exp012_on_200_overlap": r_overlap,
            "exp012_full_529": r_full,
            "exp012_nonoverlap": r_nonoverlap,
        }
    
    # ========== TEST 3: Same instances, different conditions ==========
    # On overlapping 200, compare exp-001 (N=16, T=0.7) vs exp-012 (N=8, T=1.0)
    print("\n=== TEST 3: Same 200 instances, different conditions ===")
    
    for subtask in ["ner", "re"]:
        r_001 = compute_logprob_rho(exp001_overlap, subtask, "exp001")
        r_012 = compute_logprob_rho(exp012_overlap, subtask, "exp012")
        
        print(f"  {subtask.upper()} exp-001 (N=16,T=0.7): rho={r_001['rho']:.4f}, n={r_001['n']}")
        print(f"  {subtask.upper()} exp-012 (N=8,T=1.0):  rho={r_012['rho']:.4f}, n={r_012['n']}")
        print(f"  -> Delta = {r_001['rho'] - r_012['rho']:+.4f}")
        
        report["tests"][f"same_instances_{subtask}"] = {
            "exp001_N16_T07": r_001,
            "exp012_N8_T10": r_012,
            "delta": r_001["rho"] - r_012["rho"],
        }
    
    # ========== TEST 4: N=8 subsample from exp-001 ==========
    # Use exp-001 data but only first 8 of 16 samples to simulate N=8
    print("\n=== TEST 4: N effect (exp-001 data, subsample N=8 from N=16) ===")
    
    exp001_n8_sim = []
    for inst in exp001:
        inst_copy = dict(inst)
        inst_copy["samples"] = inst["samples"][:8]
        inst_copy["logprobs"] = inst["logprobs"][:8]
        exp001_n8_sim.append(inst_copy)
    
    for subtask in ["ner", "re"]:
        r_n16 = compute_logprob_rho(exp001, subtask, "exp001")
        r_n8 = compute_logprob_rho(exp001_n8_sim, subtask, "exp001")
        
        print(f"  {subtask.upper()} exp-001 N=16: rho={r_n16['rho']:.4f}")
        print(f"  {subtask.upper()} exp-001 N=8:  rho={r_n8['rho']:.4f}")
        print(f"  -> Delta(N) = {r_n16['rho'] - r_n8['rho']:+.4f}")
        
        report["tests"][f"N_effect_{subtask}"] = {
            "N16": r_n16,
            "N8_subsampled": r_n8,
            "delta_N": r_n16["rho"] - r_n8["rho"],
        }
    
    # ========== TEST 5: Logprob distribution stats ==========
    print("\n=== TEST 5: Logprob distribution comparison ===")
    
    exp001_lps = [float(np.mean(inst["logprobs"])) for inst in exp001]
    exp012_lps = [float(np.mean([s["mean_logprob"] for s in inst["samples"]])) for inst in exp012]
    exp012_overlap_lps = [float(np.mean([s["mean_logprob"] for s in inst["samples"]])) for inst in exp012_overlap]
    
    for name, lps in [("exp-001 (N=16,T=0.7)", exp001_lps), 
                       ("exp-012 full (N=8,T=1.0)", exp012_lps),
                       ("exp-012 overlap (N=8,T=1.0)", exp012_overlap_lps)]:
        lps_arr = np.array(lps)
        print(f"  {name}:")
        print(f"    mean={lps_arr.mean():.5f}, std={lps_arr.std():.5f}")
        print(f"    min={lps_arr.min():.5f}, max={lps_arr.max():.5f}")
        print(f"    range={lps_arr.max()-lps_arr.min():.5f}")
    
    report["tests"]["logprob_distributions"] = {
        "exp001_N16_T07": {"mean": float(np.mean(exp001_lps)), "std": float(np.std(exp001_lps)),
                           "min": float(np.min(exp001_lps)), "max": float(np.max(exp001_lps))},
        "exp012_full_N8_T10": {"mean": float(np.mean(exp012_lps)), "std": float(np.std(exp012_lps)),
                                "min": float(np.min(exp012_lps)), "max": float(np.max(exp012_lps))},
        "exp012_overlap_N8_T10": {"mean": float(np.mean(exp012_overlap_lps)), "std": float(np.std(exp012_overlap_lps)),
                                   "min": float(np.min(exp012_overlap_lps)), "max": float(np.max(exp012_overlap_lps))},
    }
    
    # ========== TEST 6: F1 distribution comparison ==========
    print("\n=== TEST 6: F1 distribution comparison (NER) ===")
    
    exp001_f1s = [per_instance_f1(inst["greedy"], inst["gold"], "ner") for inst in exp001 
                  if inst["gold"].get("entities")]
    exp012_f1s = [per_instance_f1(inst["greedy"], inst["gold"], "ner") for inst in exp012 
                  if inst["gold"].get("entities")]
    exp012_overlap_f1s = [per_instance_f1(inst["greedy"], inst["gold"], "ner") for inst in exp012_overlap 
                          if inst["gold"].get("entities")]
    exp012_nonoverlap_f1s = [per_instance_f1(inst["greedy"], inst["gold"], "ner") for inst in exp012_nonoverlap 
                              if inst["gold"].get("entities")]
    
    for name, f1s in [("exp-001 200", exp001_f1s), ("exp-012 529", exp012_f1s),
                       ("exp-012 overlap", exp012_overlap_f1s), ("exp-012 non-overlap", exp012_nonoverlap_f1s)]:
        arr = np.array(f1s)
        pct_zero = 100.0 * np.sum(arr == 0) / len(arr)
        pct_perfect = 100.0 * np.sum(arr == 1.0) / len(arr)
        print(f"  {name}: mean={arr.mean():.4f}, std={arr.std():.4f}, "
              f"pct_zero={pct_zero:.1f}%, pct_perfect={pct_perfect:.1f}%, n={len(arr)}")
    
    report["tests"]["f1_distributions_ner"] = {
        "exp001_200": {"mean": float(np.mean(exp001_f1s)), "std": float(np.std(exp001_f1s)),
                        "pct_zero": float(100.0 * np.sum(np.array(exp001_f1s)==0) / len(exp001_f1s)),
                        "n": len(exp001_f1s)},
        "exp012_529": {"mean": float(np.mean(exp012_f1s)), "std": float(np.std(exp012_f1s)),
                        "pct_zero": float(100.0 * np.sum(np.array(exp012_f1s)==0) / len(exp012_f1s)),
                        "n": len(exp012_f1s)},
        "exp012_overlap": {"mean": float(np.mean(exp012_overlap_f1s)), "std": float(np.std(exp012_overlap_f1s)),
                            "pct_zero": float(100.0 * np.sum(np.array(exp012_overlap_f1s)==0) / len(exp012_overlap_f1s)),
                            "n": len(exp012_overlap_f1s)},
    }
    
    # ========== DIAGNOSIS ==========
    print("\n" + "="*80)
    print("  DIAGNOSIS")
    print("="*80)
    
    # Check factor (a): instance subset
    ner_test2 = report["tests"]["subset_effect_ner"]
    rho_012_on200 = ner_test2["exp012_on_200_overlap"]["rho"]
    rho_012_full = ner_test2["exp012_full_529"]["rho"]
    subset_effect = rho_012_on200 - rho_012_full
    
    # Check factor (b)+(c): T and N combined (same instances, different conditions)
    ner_test3 = report["tests"]["same_instances_ner"]
    condition_effect = ner_test3["delta"]
    
    # Check factor (c) alone: N effect
    ner_test4 = report["tests"]["N_effect_ner"]
    n_effect = ner_test4["delta_N"]
    
    # Infer T effect
    t_effect = condition_effect - n_effect  # approximate
    
    total_gap = 0.314 - 0.140
    
    print(f"\n  Total gap: 0.314 - 0.140 = {total_gap:.3f}")
    print(f"\n  Factor decomposition (NER):")
    print(f"    (a) Instance subset effect (200 vs 529, same T=1.0/N=8): {subset_effect:+.4f}")
    print(f"    (b+c) Condition effect (same 200 inst, N16/T0.7 vs N8/T1.0): {condition_effect:+.4f}")
    print(f"    (c) N effect alone (N=16 vs N=8, same T=0.7): {n_effect:+.4f}")
    print(f"    (b) T effect (inferred, T=0.7 vs T=1.0): ~{t_effect:+.4f}")
    
    conclusions = []
    if abs(subset_effect) > 0.05:
        conclusions.append(f"(a) SIGNIFICANT: Instance subset contributes {subset_effect:+.4f} to rho gap")
    else:
        conclusions.append(f"(a) MINOR: Instance subset effect is only {subset_effect:+.4f}")
    
    if abs(condition_effect) > 0.05:
        conclusions.append(f"(b+c) SIGNIFICANT: T/N differences contribute {condition_effect:+.4f} to rho gap")
    else:
        conclusions.append(f"(b+c) MINOR: T/N effect is only {condition_effect:+.4f}")
    
    if abs(n_effect) > 0.03:
        conclusions.append(f"(c) MODERATE: N scaling (16 vs 8) contributes {n_effect:+.4f}")
    else:
        conclusions.append(f"(c) NEGLIGIBLE: N effect is only {n_effect:+.4f}")
    
    conclusions.append("(d) RULED OUT: Both use identical per-token mean logprob normalization")
    
    for c in conclusions:
        print(f"    {c}")
    
    report["summary"] = {
        "total_gap": total_gap,
        "subset_effect_a": subset_effect,
        "condition_effect_bc": condition_effect,
        "n_effect_c": n_effect,
        "t_effect_b_inferred": t_effect,
        "conclusions": conclusions,
        "normalization_difference": False,
    }
    
    # Save
    with open(OUTPUT_PATH, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nReport saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
