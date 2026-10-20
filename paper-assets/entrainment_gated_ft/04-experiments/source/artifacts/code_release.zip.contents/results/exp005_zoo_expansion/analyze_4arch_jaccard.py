#!/usr/bin/env python3
"""4-architecture pairwise Jaccard: GDN/RetNet/HGRN2/GLA at 340M, h3-1 vs pure."""
import json
import numpy as np
from itertools import combinations
from pathlib import Path

BASE = Path("/root/entrainment_gated_ft")
MULTI = BASE / "lm_eval_clean/340m_multi"
EXP5 = BASE / "results/exp005_zoo_expansion"

ARC_EASY_PATHS = {
    "GDN":    {"pure": MULTI / "GDN-pure/samples/arc_easy.jsonl",
               "h31":  MULTI / "GDN-h3-1/samples/arc_easy.jsonl"},
    "RetNet": {"pure": MULTI / "RetNet-pure/samples/arc_easy.jsonl",
               "h31":  MULTI / "RetNet-h3-1/samples/arc_easy.jsonl"},
    "HGRN2":  {"pure": MULTI / "HGRN2-pure/samples/arc_easy.jsonl",
               "h31":  MULTI / "HGRN2-h3-1/samples/arc_easy.jsonl"},
    "GLA":    {"pure": EXP5 / "GLA_pure/__root__entrainment_gated_ft__models__340M-20B-GLA-pure-baseline/samples_arc_easy_2026-05-23T00-41-14.537211.jsonl",
               "h31":  EXP5 / "GLA_hybrid-3-1/__root__entrainment_gated_ft__models__340M-20B-GLA-hybrid-3-1/samples_arc_easy_2026-05-22T23-51-08.119053.jsonl"},
}

LAMBADA_PATHS = {
    "GDN":    {"pure": EXP5 / "GDN_pure_lambada/__root__entrainment_gated_ft__models__340M-20B-GatedDeltaNet-pure-baseline/samples_lambada_openai_2026-05-23T00-55-12.446919.jsonl",
               "h31":  EXP5 / "GDN_h3-1_lambada/__root__entrainment_gated_ft__models__340M-20B-GatedDeltaNet-hybrid-3-1/samples_lambada_openai_2026-05-23T00-57-27.658457.jsonl"},
    "RetNet": {"pure": EXP5 / "RetNet_pure_lambada/__root__entrainment_gated_ft__models__340M-20B-RetNet-pure/samples_lambada_openai_2026-05-23T01-00-10.816890.jsonl",
               "h31":  EXP5 / "RetNet_h3-1_lambada/__root__entrainment_gated_ft__models__340M-20B-RetNet-hybrid-3-1/samples_lambada_openai_2026-05-23T01-02-18.914553.jsonl"},
    "HGRN2":  {"pure": EXP5 / "HGRN2_pure_lambada/__root__entrainment_gated_ft__models__340M-20B-HGRN2-pure-baseline/samples_lambada_openai_2026-05-23T01-05-14.495517.jsonl",
               "h31":  EXP5 / "HGRN2_h3-1_lambada/__root__entrainment_gated_ft__models__340M-20B-HGRN2-hybrid-3-1/samples_lambada_openai_2026-05-23T01-07-22.356663.jsonl"},
    "GLA":    {"pure": EXP5 / "GLA_pure/__root__entrainment_gated_ft__models__340M-20B-GLA-pure-baseline/samples_lambada_openai_2026-05-23T00-41-14.537211.jsonl",
               "h31":  EXP5 / "GLA_hybrid-3-1/__root__entrainment_gated_ft__models__340M-20B-GLA-hybrid-3-1/samples_lambada_openai_2026-05-22T23-51-08.119053.jsonl"},
}

def load_acc_dict(jsonl_path):
    acc = {}
    with open(jsonl_path) as f:
        for line in f:
            item = json.loads(line)
            doc_id = item["doc_id"]
            a = item.get("acc", item.get("exact_match", 0))
            acc[doc_id] = int(float(a))
    return acc

def jaccard(set_a, set_b):
    if not set_a and not set_b:
        return 1.0
    inter = len(set_a & set_b)
    union = len(set_a | set_b)
    return inter / union if union > 0 else 0.0

def permutation_test(helped_dict, archs, n_total, n_perms=10000):
    rng = np.random.default_rng(42)
    pairs = list(combinations(archs, 2))
    sizes = {a: len(helped_dict[a]) for a in archs}
    null_jaccards = {f"{a}-{b}": [] for a, b in pairs}
    for _ in range(n_perms):
        random_sets = {}
        for a in archs:
            idxs = rng.choice(n_total, size=sizes[a], replace=False)
            random_sets[a] = set(idxs.tolist())
        for a, b in pairs:
            null_jaccards[f"{a}-{b}"].append(jaccard(random_sets[a], random_sets[b]))
    results = {}
    for a, b in pairs:
        key = f"{a}-{b}"
        obs = jaccard(helped_dict[a], helped_dict[b])
        null_arr = np.array(null_jaccards[key])
        z = (obs - null_arr.mean()) / null_arr.std() if null_arr.std() > 0 else 0
        p = np.mean(null_arr >= obs)
        results[key] = {"J_obs": round(float(obs), 6), "J_null_mean": round(float(null_arr.mean()), 6),
                        "J_null_std": round(float(null_arr.std()), 6), "z": round(float(z), 2), "p": round(float(p), 6)}
    return results

def analyze_benchmark(name, paths, archs):
    print(f"\n{'='*60}")
    print(f"Benchmark: {name}")
    print(f"{'='*60}")
    
    pure_acc = {}
    h31_acc = {}
    for arch in archs:
        if arch not in paths:
            continue
        pure_acc[arch] = load_acc_dict(paths[arch]["pure"])
        h31_acc[arch] = load_acc_dict(paths[arch]["h31"])
        n = len(pure_acc[arch])
        pc = sum(pure_acc[arch].values())
        hc = sum(h31_acc[arch].values())
        print(f"  {arch}: n={n}, pure_acc={pc/n:.4f}, h31_acc={hc/n:.4f}")
    
    active_archs = [a for a in archs if a in pure_acc]
    if len(active_archs) < 2:
        return None
    
    doc_ids = sorted(pure_acc[active_archs[0]].keys())
    n_total = len(doc_ids)
    
    helped = {}
    hurt = {}
    for arch in active_archs:
        helped[arch] = set()
        hurt[arch] = set()
        for did in doc_ids:
            p = pure_acc[arch].get(did, 0)
            h = h31_acc[arch].get(did, 0)
            if h == 1 and p == 0:
                helped[arch].add(did)
            elif h == 0 and p == 1:
                hurt[arch].add(did)
    
    pairs = list(combinations(active_archs, 2))
    
    print(f"\n  Per-arch helped/hurt:")
    for arch in active_archs:
        print(f"    {arch}: helped={len(helped[arch])}, hurt={len(hurt[arch])}, net={len(helped[arch])-len(hurt[arch])}")
    
    print(f"\n  Pairwise Jaccard (h3-1 vs pure):")
    print(f"    {'Pair':<18} {'J_helped':>9} {'J_hurt':>9} {'|H∩|':>5} {'|U∩|':>5}")
    print(f"    {'-'*52}")
    
    pair_results = {}
    j_helped_vals = []
    j_hurt_vals = []
    for a, b in pairs:
        jh = jaccard(helped[a], helped[b])
        ju = jaccard(hurt[a], hurt[b])
        j_helped_vals.append(jh)
        j_hurt_vals.append(ju)
        key = f"{a}-{b}"
        pair_results[key] = {
            "J_helped": round(jh, 6), "J_hurt": round(ju, 6),
            "|helped_a|": len(helped[a]), "|helped_b|": len(helped[b]),
            "|hurt_a|": len(hurt[a]), "|hurt_b|": len(hurt[b]),
            "|helped_intersection|": len(helped[a] & helped[b]),
            "|hurt_intersection|": len(hurt[a] & hurt[b]),
        }
        print(f"    {key:<18} {jh:>9.4f} {ju:>9.4f} {len(helped[a]&helped[b]):>5} {len(hurt[a]&hurt[b]):>5}")
    
    mean_jh = np.mean(j_helped_vals)
    mean_ju = np.mean(j_hurt_vals)
    print(f"\n    Mean J_helped = {mean_jh:.4f}")
    print(f"    Mean J_hurt  = {mean_ju:.4f}")
    
    print(f"\n  Permutation test (10k, helped):")
    perm_helped = permutation_test(helped, active_archs, n_total)
    for key, v in perm_helped.items():
        print(f"    {key}: J_obs={v['J_obs']:.4f}, J_null={v['J_null_mean']:.4f}±{v['J_null_std']:.4f}, z={v['z']:.2f}, p={v['p']:.4f}")
    
    print(f"\n  Permutation test (10k, hurt):")
    perm_hurt = permutation_test(hurt, active_archs, n_total)
    for key, v in perm_hurt.items():
        print(f"    {key}: J_obs={v['J_obs']:.4f}, J_null={v['J_null_mean']:.4f}±{v['J_null_std']:.4f}, z={v['z']:.2f}, p={v['p']:.4f}")
    
    if "GLA" in active_archs and len(active_archs) == 4:
        orig3_pairs = [(a, b) for a, b in pairs if a != "GLA" and b != "GLA"]
        gla_pairs = [(a, b) for a, b in pairs if a == "GLA" or b == "GLA"]
        
        orig3_jh = np.mean([pair_results[f"{a}-{b}"]["J_helped"] for a, b in orig3_pairs])
        orig3_ju = np.mean([pair_results[f"{a}-{b}"]["J_hurt"] for a, b in orig3_pairs])
        gla_jh = np.mean([pair_results[f"{a}-{b}"]["J_helped"] for a, b in gla_pairs])
        gla_ju = np.mean([pair_results[f"{a}-{b}"]["J_hurt"] for a, b in gla_pairs])
        
        print(f"\n  Subgroup comparison:")
        print(f"    Original 3-arch (GDN/RetNet/HGRN2): mean J_helped={orig3_jh:.4f}, J_hurt={orig3_ju:.4f}")
        print(f"    GLA vs others:                       mean J_helped={gla_jh:.4f}, J_hurt={gla_ju:.4f}")
        print(f"    All 4-arch:                          mean J_helped={mean_jh:.4f}, J_hurt={mean_ju:.4f}")
    
    return {
        "n_samples": n_total,
        "architectures": active_archs,
        "per_arch": {
            arch: {"helped": len(helped[arch]), "hurt": len(hurt[arch]),
                   "net": len(helped[arch]) - len(hurt[arch]),
                   "pure_acc": round(sum(pure_acc[arch].values()) / n_total, 6),
                   "h31_acc": round(sum(h31_acc[arch].values()) / n_total, 6)}
            for arch in active_archs
        },
        "pairwise": pair_results,
        "mean_J_helped": round(float(mean_jh), 6),
        "mean_J_hurt": round(float(mean_ju), 6),
        "permutation_test_helped": perm_helped,
        "permutation_test_hurt": perm_hurt,
    }

ARCHS = ["GDN", "RetNet", "HGRN2", "GLA"]

results = {"experiment": "exp-005", "date": "2026-05-23", "scale": "340M-20B",
           "description": "4-architecture pairwise Jaccard for helped/hurt sets (h3-1 vs pure)",
           "benchmarks": {}}

# ARC-Easy
arc_result = analyze_benchmark("arc_easy", ARC_EASY_PATHS, ARCHS)
if arc_result:
    results["benchmarks"]["arc_easy"] = arc_result

# LAMBADA
lambada_result = analyze_benchmark("lambada_openai", LAMBADA_PATHS, ARCHS)
if lambada_result:
    results["benchmarks"]["lambada_openai"] = lambada_result

# Cross-benchmark summary
if "arc_easy" in results["benchmarks"] and "lambada_openai" in results["benchmarks"]:
    print(f"\n{'='*60}")
    print("CROSS-BENCHMARK SUMMARY")
    print(f"{'='*60}")
    for bm in ["arc_easy", "lambada_openai"]:
        r = results["benchmarks"][bm]
        print(f"  {bm:20s}: mean J_helped={r['mean_J_helped']:.4f}, J_hurt={r['mean_J_hurt']:.4f}, n={r['n_samples']}")
    
    results["cross_benchmark_summary"] = {
        "mean_J_helped_arc_easy": results["benchmarks"]["arc_easy"]["mean_J_helped"],
        "mean_J_hurt_arc_easy": results["benchmarks"]["arc_easy"]["mean_J_hurt"],
        "mean_J_helped_lambada": results["benchmarks"]["lambada_openai"]["mean_J_helped"],
        "mean_J_hurt_lambada": results["benchmarks"]["lambada_openai"]["mean_J_hurt"],
        "reference_1.3B_3arch_J_helped": 0.10,
        "reference_1.3B_3arch_J_hurt": 0.09,
    }

out_path = "/root/entrainment_gated_ft/results/exp005_zoo_expansion/jaccard_4arch.json"
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to {out_path}")
