#!/usr/bin/env python3
"""5-architecture pairwise Jaccard: GDN/RetNet/HGRN2/GLA/DeltaNet at 340M, h3-1 vs pure."""
import json
import numpy as np
from itertools import combinations
from pathlib import Path

BASE = Path("/root/entrainment_gated_ft")
MULTI = BASE / "lm_eval_clean/340m_multi"
EXP5 = BASE / "results/exp005_zoo_expansion"

ARC_EASY_PATHS = {
    "GDN":      {"pure": MULTI / "GDN-pure/samples/arc_easy.jsonl",
                 "h31":  MULTI / "GDN-h3-1/samples/arc_easy.jsonl"},
    "RetNet":   {"pure": MULTI / "RetNet-pure/samples/arc_easy.jsonl",
                 "h31":  MULTI / "RetNet-h3-1/samples/arc_easy.jsonl"},
    "HGRN2":    {"pure": MULTI / "HGRN2-pure/samples/arc_easy.jsonl",
                 "h31":  MULTI / "HGRN2-h3-1/samples/arc_easy.jsonl"},
    "GLA":      {"pure": EXP5 / "GLA_pure/__root__entrainment_gated_ft__models__340M-20B-GLA-pure-baseline/samples_arc_easy_2026-05-23T00-41-14.537211.jsonl",
                 "h31":  EXP5 / "GLA_hybrid-3-1/__root__entrainment_gated_ft__models__340M-20B-GLA-hybrid-3-1/samples_arc_easy_2026-05-22T23-51-08.119053.jsonl"},
    "DeltaNet": {"pure": EXP5 / "DeltaNet_pure_baseline/__root__entrainment_gated_ft__models__340M-20B-DeltaNet-pure/samples_arc_easy_2026-05-23T01-13-35.906959.jsonl",
                 "h31":  EXP5 / "DeltaNet_hybrid-3-1/__root__entrainment_gated_ft__models__340M-20B-DeltaNet-hybrid-3-1/samples_arc_easy_2026-05-23T00-09-47.452122.jsonl"},
}

LAMBADA_PATHS = {
    "GDN":      {"pure": EXP5 / "GDN_pure_lambada/__root__entrainment_gated_ft__models__340M-20B-GatedDeltaNet-pure-baseline/samples_lambada_openai_2026-05-23T00-55-12.446919.jsonl",
                 "h31":  EXP5 / "GDN_h3-1_lambada/__root__entrainment_gated_ft__models__340M-20B-GatedDeltaNet-hybrid-3-1/samples_lambada_openai_2026-05-23T00-57-27.658457.jsonl"},
    "RetNet":   {"pure": EXP5 / "RetNet_pure_lambada/__root__entrainment_gated_ft__models__340M-20B-RetNet-pure/samples_lambada_openai_2026-05-23T01-00-10.816890.jsonl",
                 "h31":  EXP5 / "RetNet_h3-1_lambada/__root__entrainment_gated_ft__models__340M-20B-RetNet-hybrid-3-1/samples_lambada_openai_2026-05-23T01-02-18.914553.jsonl"},
    "HGRN2":    {"pure": EXP5 / "HGRN2_pure_lambada/__root__entrainment_gated_ft__models__340M-20B-HGRN2-pure-baseline/samples_lambada_openai_2026-05-23T01-05-14.495517.jsonl",
                 "h31":  EXP5 / "HGRN2_h3-1_lambada/__root__entrainment_gated_ft__models__340M-20B-HGRN2-hybrid-3-1/samples_lambada_openai_2026-05-23T01-07-22.356663.jsonl"},
    "GLA":      {"pure": EXP5 / "GLA_pure/__root__entrainment_gated_ft__models__340M-20B-GLA-pure-baseline/samples_lambada_openai_2026-05-23T00-41-14.537211.jsonl",
                 "h31":  EXP5 / "GLA_hybrid-3-1/__root__entrainment_gated_ft__models__340M-20B-GLA-hybrid-3-1/samples_lambada_openai_2026-05-22T23-51-08.119053.jsonl"},
    "DeltaNet": {"pure": EXP5 / "DeltaNet_pure_baseline/__root__entrainment_gated_ft__models__340M-20B-DeltaNet-pure/samples_lambada_openai_2026-05-23T01-13-35.906959.jsonl",
                 "h31":  EXP5 / "DeltaNet_hybrid-3-1/__root__entrainment_gated_ft__models__340M-20B-DeltaNet-hybrid-3-1/samples_lambada_openai_2026-05-23T00-09-47.452122.jsonl"},
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
                        "J_null_std": round(float(null_arr.std()), 6), "z": round(float(z), 2), "p": round(float(p), 4)}
    return results

def analyze_benchmark(task_name, paths, archs):
    print(f"\n{'='*60}")
    print(f"Benchmark: {task_name}")
    print(f"{'='*60}")

    active_archs = []
    for arch in archs:
        if arch not in paths:
            continue
        p = paths[arch]["pure"]
        h = paths[arch]["h31"]
        if not Path(p).exists():
            print(f"  SKIP {arch}: missing pure file {p}")
            continue
        if not Path(h).exists():
            print(f"  SKIP {arch}: missing h31 file {h}")
            continue
        active_archs.append(arch)

    if len(active_archs) < 2:
        print("  Not enough architectures, skipping")
        return None

    pure_acc = {}
    h31_acc = {}
    for arch in active_archs:
        pure_acc[arch] = load_acc_dict(paths[arch]["pure"])
        h31_acc[arch] = load_acc_dict(paths[arch]["h31"])

    n_total = len(pure_acc[active_archs[0]])
    for arch in active_archs:
        assert len(pure_acc[arch]) == n_total, f"{arch} pure has {len(pure_acc[arch])} samples, expected {n_total}"
        assert len(h31_acc[arch]) == n_total, f"{arch} h31 has {len(h31_acc[arch])} samples, expected {n_total}"

    helped = {}
    hurt = {}
    for arch in active_archs:
        helped[arch] = {doc_id for doc_id in pure_acc[arch] if h31_acc[arch][doc_id] == 1 and pure_acc[arch][doc_id] == 0}
        hurt[arch] = {doc_id for doc_id in pure_acc[arch] if h31_acc[arch][doc_id] == 0 and pure_acc[arch][doc_id] == 1}

    print(f"\n  Per-architecture (n={n_total}):")
    for arch in active_archs:
        pa = sum(pure_acc[arch].values()) / n_total
        ha = sum(h31_acc[arch].values()) / n_total
        print(f"    {arch:10s}: pure_acc={pa:.4f}, h31_acc={ha:.4f}, |helped|={len(helped[arch])}, |hurt|={len(hurt[arch])}, net={len(helped[arch])-len(hurt[arch])}")

    pairs = list(combinations(active_archs, 2))
    pair_results = {}
    print(f"\n  Pairwise Jaccard ({len(pairs)} pairs):")
    j_helped_vals = []
    j_hurt_vals = []
    for a, b in pairs:
        jh = jaccard(helped[a], helped[b])
        ju = jaccard(hurt[a], hurt[b])
        pair_results[f"{a}-{b}"] = {
            "J_helped": round(float(jh), 6), "J_hurt": round(float(ju), 6),
            "|helped_a|": len(helped[a]), "|helped_b|": len(helped[b]),
            "|hurt_a|": len(hurt[a]), "|hurt_b|": len(hurt[b]),
            "|helped_inter|": len(helped[a] & helped[b]),
            "|hurt_inter|": len(hurt[a] & hurt[b]),
        }
        j_helped_vals.append(jh)
        j_hurt_vals.append(ju)
        print(f"    {a:10s}-{b:10s}: J_helped={jh:.4f}, J_hurt={ju:.4f}")

    mean_jh = np.mean(j_helped_vals)
    mean_ju = np.mean(j_hurt_vals)
    print(f"\n    Mean J_helped = {mean_jh:.4f}")
    print(f"    Mean J_hurt  = {mean_ju:.4f}")

    print(f"\n  Permutation test (10k, helped):")
    perm_helped = permutation_test(helped, active_archs, n_total)
    for key, v in perm_helped.items():
        print(f"    {key}: J_obs={v['J_obs']:.4f}, J_null={v['J_null_mean']:.4f}+/-{v['J_null_std']:.4f}, z={v['z']:.2f}, p={v['p']:.4f}")

    print(f"\n  Permutation test (10k, hurt):")
    perm_hurt = permutation_test(hurt, active_archs, n_total)
    for key, v in perm_hurt.items():
        print(f"    {key}: J_obs={v['J_obs']:.4f}, J_null={v['J_null_mean']:.4f}+/-{v['J_null_std']:.4f}, z={v['z']:.2f}, p={v['p']:.4f}")

    # Subgroup: original 3-arch vs 4-arch vs 5-arch
    orig3 = [a for a in ["GDN", "RetNet", "HGRN2"] if a in active_archs]
    orig4 = [a for a in ["GDN", "RetNet", "HGRN2", "GLA"] if a in active_archs]
    if len(orig3) == 3 and len(active_archs) == 5:
        orig3_pairs = list(combinations(orig3, 2))
        orig4_pairs = list(combinations(orig4, 2))
        new_pairs = [(a, b) for a, b in pairs if "DeltaNet" in (a, b)]

        orig3_jh = np.mean([pair_results[f"{a}-{b}"]["J_helped"] for a, b in orig3_pairs])
        orig3_ju = np.mean([pair_results[f"{a}-{b}"]["J_hurt"] for a, b in orig3_pairs])
        orig4_jh = np.mean([pair_results[f"{a}-{b}"]["J_helped"] for a, b in orig4_pairs])
        orig4_ju = np.mean([pair_results[f"{a}-{b}"]["J_hurt"] for a, b in orig4_pairs])
        delta_jh = np.mean([pair_results[f"{a}-{b}"]["J_helped"] for a, b in new_pairs])
        delta_ju = np.mean([pair_results[f"{a}-{b}"]["J_hurt"] for a, b in new_pairs])

        print(f"\n  Subgroup comparison:")
        print(f"    Original 3-arch (GDN/RetNet/HGRN2):  mean J_helped={orig3_jh:.4f}, J_hurt={orig3_ju:.4f}")
        print(f"    4-arch (+ GLA):                       mean J_helped={orig4_jh:.4f}, J_hurt={orig4_ju:.4f}")
        print(f"    DeltaNet vs others:                   mean J_helped={delta_jh:.4f}, J_hurt={delta_ju:.4f}")
        print(f"    All 5-arch:                           mean J_helped={mean_jh:.4f}, J_hurt={mean_ju:.4f}")

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

ARCHS = ["GDN", "RetNet", "HGRN2", "GLA", "DeltaNet"]

results = {"experiment": "exp-005", "date": "2026-05-23", "scale": "340M-20B",
           "description": "5-architecture pairwise Jaccard for helped/hurt sets (h3-1 vs pure)",
           "benchmarks": {}}

arc_result = analyze_benchmark("arc_easy", ARC_EASY_PATHS, ARCHS)
if arc_result:
    results["benchmarks"]["arc_easy"] = arc_result

lambada_result = analyze_benchmark("lambada_openai", LAMBADA_PATHS, ARCHS)
if lambada_result:
    results["benchmarks"]["lambada_openai"] = lambada_result

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
        "reference_4arch_J_helped_lambada": 0.1219,
        "reference_4arch_J_hurt_lambada": 0.0965,
        "reference_4arch_J_helped_arceasy": 0.1034,
        "reference_4arch_J_hurt_arceasy": 0.1059,
        "reference_1.3B_3arch_J_helped": 0.10,
        "reference_1.3B_3arch_J_hurt": 0.09,
    }

out_path = "/root/entrainment_gated_ft/results/exp005_zoo_expansion/jaccard_5arch.json"
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to {out_path}")
