#!/usr/bin/env python3
"""6-architecture pairwise Jaccard: GDN/RetNet/HGRN2/GLA/DeltaNet/HGRN at 340M, h3-1 vs pure."""
import json, glob, os
import numpy as np
from itertools import combinations
from pathlib import Path

BASE = Path("/root/entrainment_gated_ft")
MULTI = BASE / "lm_eval_clean/340m_multi"
EXP5 = BASE / "results/exp005_zoo_expansion"

def find_jsonl(base_dir, task_prefix):
    pattern = str(base_dir / "**" / f"samples_{task_prefix}*.jsonl")
    matches = glob.glob(pattern, recursive=True)
    if not matches:
        pattern = str(base_dir / "**" / f"{task_prefix}.jsonl")
        matches = glob.glob(pattern, recursive=True)
    if not matches:
        return None
    return sorted(matches)[-1]

def build_paths(task):
    paths = {}
    arc_or_lam = "arc_easy" if task == "arc_easy" else "lambada_openai"

    # GDN
    if task == "arc_easy":
        paths["GDN"] = {
            "pure": str(MULTI / "GDN-pure/samples/arc_easy.jsonl"),
            "h31":  str(MULTI / "GDN-h3-1/samples/arc_easy.jsonl"),
        }
    else:
        paths["GDN"] = {
            "pure": find_jsonl(EXP5 / "GDN_pure_lambada", arc_or_lam),
            "h31":  find_jsonl(EXP5 / "GDN_h3-1_lambada", arc_or_lam),
        }

    # RetNet
    if task == "arc_easy":
        paths["RetNet"] = {
            "pure": str(MULTI / "RetNet-pure/samples/arc_easy.jsonl"),
            "h31":  str(MULTI / "RetNet-h3-1/samples/arc_easy.jsonl"),
        }
    else:
        paths["RetNet"] = {
            "pure": find_jsonl(EXP5 / "RetNet_pure_lambada", arc_or_lam),
            "h31":  find_jsonl(EXP5 / "RetNet_h3-1_lambada", arc_or_lam),
        }

    # HGRN2
    if task == "arc_easy":
        paths["HGRN2"] = {
            "pure": str(MULTI / "HGRN2-pure/samples/arc_easy.jsonl"),
            "h31":  str(MULTI / "HGRN2-h3-1/samples/arc_easy.jsonl"),
        }
    else:
        paths["HGRN2"] = {
            "pure": find_jsonl(EXP5 / "HGRN2_pure_lambada", arc_or_lam),
            "h31":  find_jsonl(EXP5 / "HGRN2_h3-1_lambada", arc_or_lam),
        }

    # GLA
    paths["GLA"] = {
        "pure": find_jsonl(EXP5 / "GLA_pure", arc_or_lam),
        "h31":  find_jsonl(EXP5 / "GLA_hybrid-3-1", arc_or_lam),
    }

    # DeltaNet
    paths["DeltaNet"] = {
        "pure": find_jsonl(EXP5 / "DeltaNet_pure_baseline", arc_or_lam),
        "h31":  find_jsonl(EXP5 / "DeltaNet_hybrid-3-1", arc_or_lam),
    }

    # HGRN (the new 6th architecture)
    paths["HGRN"] = {
        "pure": find_jsonl(EXP5 / "HGRN_pure_baseline", arc_or_lam),
        "h31":  find_jsonl(EXP5 / "HGRN_hybrid-3-1", arc_or_lam),
    }

    return paths


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


def permutation_test(helped_dict, archs, n_total, n_perms=1000):
    rng = np.random.default_rng(42)
    pairs = list(combinations(archs, 2))
    sizes = {a: len(helped_dict[a]) for a in archs}
    null_jaccards = {f"{a}-{b}": [] for a, b in pairs}
    indices = np.arange(n_total)
    for _ in range(n_perms):
        random_sets = {}
        for a in archs:
            random_sets[a] = set(rng.choice(indices, size=sizes[a], replace=False))
        for a, b in pairs:
            key = f"{a}-{b}"
            null_jaccards[key].append(jaccard(random_sets[a], random_sets[b]))
    results = {}
    for a, b in pairs:
        key = f"{a}-{b}"
        null_arr = np.array(null_jaccards[key])
        obs_j = jaccard(helped_dict[a], helped_dict[b])
        null_mean = float(null_arr.mean())
        null_std = float(null_arr.std())
        z = (obs_j - null_mean) / null_std if null_std > 0 else float("inf")
        p = float((np.sum(null_arr >= obs_j) + 1) / (n_perms + 1))
        results[key] = {"J_obs": round(obs_j, 6), "J_null_mean": round(null_mean, 6),
                        "J_null_std": round(null_std, 6), "z": round(z, 2), "p": round(p, 4)}
    return results


def analyze_benchmark(task, all_paths, archs):
    paths = all_paths
    print(f"\n{'='*60}")
    print(f"Benchmark: {task}")
    print(f"{'='*60}")

    active_archs = []
    for arch in archs:
        p = paths.get(arch, {})
        if p.get("pure") and p.get("h31") and os.path.exists(p["pure"]) and os.path.exists(p["h31"]):
            active_archs.append(arch)
        else:
            print(f"  SKIP {arch}: pure={p.get('pure')}, h31={p.get('h31')}")

    if len(active_archs) < 2:
        print("  Not enough architectures with data. Skipping.")
        return None

    pure_acc, h31_acc = {}, {}
    for arch in active_archs:
        pure_acc[arch] = load_acc_dict(paths[arch]["pure"])
        h31_acc[arch] = load_acc_dict(paths[arch]["h31"])
        print(f"  {arch}: pure N={len(pure_acc[arch])}, h31 N={len(h31_acc[arch])}")

    n_total = len(pure_acc[active_archs[0]])
    for arch in active_archs:
        assert len(pure_acc[arch]) == n_total, f"{arch} pure has {len(pure_acc[arch])}, expected {n_total}"
        assert len(h31_acc[arch]) == n_total, f"{arch} h31 has {len(h31_acc[arch])}, expected {n_total}"

    helped, hurt = {}, {}
    for arch in active_archs:
        helped[arch] = set()
        hurt[arch] = set()
        for doc_id in pure_acc[arch]:
            p = pure_acc[arch][doc_id]
            h = h31_acc[arch][doc_id]
            if h == 1 and p == 0:
                helped[arch].add(doc_id)
            elif h == 0 and p == 1:
                hurt[arch].add(doc_id)
        print(f"  {arch}: helped={len(helped[arch])}, hurt={len(hurt[arch])}, net={len(helped[arch])-len(hurt[arch])}")

    pairs = list(combinations(active_archs, 2))
    print(f"\n  Pairwise Jaccard ({len(pairs)} pairs):")

    pair_results = {}
    for a, b in pairs:
        key = f"{a}-{b}"
        jh = jaccard(helped[a], helped[b])
        ju = jaccard(hurt[a], hurt[b])
        ih = len(helped[a] & helped[b])
        iu = len(hurt[a] & hurt[b])
        pair_results[key] = {
            "J_helped": round(jh, 6), "J_hurt": round(ju, 6),
            "|helped_a|": len(helped[a]), "|helped_b|": len(helped[b]),
            "|hurt_a|": len(hurt[a]), "|hurt_b|": len(hurt[b]),
            "|helped_inter|": ih, "|hurt_inter|": iu,
        }
        print(f"    {key}: J_helped={jh:.4f} ({ih}), J_hurt={ju:.4f} ({iu})")

    mean_jh = np.mean([pair_results[k]["J_helped"] for k in pair_results])
    mean_ju = np.mean([pair_results[k]["J_hurt"] for k in pair_results])
    print(f"\n  Mean J_helped={mean_jh:.4f}, Mean J_hurt={mean_ju:.4f}")

    print(f"\n  Running permutation tests (1000 permutations)...")
    perm_helped = permutation_test(helped, active_archs, n_total, n_perms=1000)
    perm_hurt = permutation_test(hurt, active_archs, n_total, n_perms=1000)

    sig_helped = sum(1 for v in perm_helped.values() if v["p"] < 0.05)
    sig_hurt = sum(1 for v in perm_hurt.values() if v["p"] < 0.05)
    print(f"  Significant pairs (p<0.05): helped={sig_helped}/{len(pairs)}, hurt={sig_hurt}/{len(pairs)}")

    for k in perm_helped:
        v = perm_helped[k]
        print(f"    helped {k}: J_obs={v['J_obs']:.4f}, null={v['J_null_mean']:.4f}±{v['J_null_std']:.4f}, z={v['z']:.2f}, p={v['p']:.4f}")
    for k in perm_hurt:
        v = perm_hurt[k]
        print(f"    hurt   {k}: J_obs={v['J_obs']:.4f}, null={v['J_null_mean']:.4f}±{v['J_null_std']:.4f}, z={v['z']:.2f}, p={v['p']:.4f}")

    # Subgroup trends: 3->4->5->6 arch
    subgroups = {
        "3arch (GDN/RetNet/HGRN2)": ["GDN", "RetNet", "HGRN2"],
        "4arch (+GLA)": ["GDN", "RetNet", "HGRN2", "GLA"],
        "5arch (+DeltaNet)": ["GDN", "RetNet", "HGRN2", "GLA", "DeltaNet"],
        "6arch (+HGRN)": ["GDN", "RetNet", "HGRN2", "GLA", "DeltaNet", "HGRN"],
    }
    print(f"\n  Subgroup trends:")
    subgroup_stats = {}
    for label, sub_archs in subgroups.items():
        sub_active = [a for a in sub_archs if a in active_archs]
        if len(sub_active) < 2:
            continue
        sub_pairs = list(combinations(sub_active, 2))
        sub_jh = np.mean([pair_results[f"{a}-{b}"]["J_helped"] for a, b in sub_pairs if f"{a}-{b}" in pair_results])
        sub_ju = np.mean([pair_results[f"{a}-{b}"]["J_hurt"] for a, b in sub_pairs if f"{a}-{b}" in pair_results])
        subgroup_stats[label] = {"mean_J_helped": round(float(sub_jh), 6), "mean_J_hurt": round(float(sub_ju), 6),
                                  "n_archs": len(sub_active), "n_pairs": len(sub_pairs)}
        print(f"    {label}: J_helped={sub_jh:.4f}, J_hurt={sub_ju:.4f} ({len(sub_pairs)} pairs)")

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
        "subgroup_trends": subgroup_stats,
    }


ARCHS = ["GDN", "RetNet", "HGRN2", "GLA", "DeltaNet", "HGRN"]

results = {"experiment": "exp-005", "date": "2026-05-23", "scale": "340M-20B",
           "description": "6-architecture pairwise Jaccard for helped/hurt sets (h3-1 vs pure)",
           "n_architectures": 6, "n_pairs": 15, "architectures": ARCHS,
           "n_permutations": 1000, "benchmarks": {}}

for task in ["arc_easy", "lambada_openai"]:
    paths = build_paths(task)
    result = analyze_benchmark(task, paths, ARCHS)
    if result:
        results["benchmarks"][task] = result

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
        "reference_5arch_J_helped_lambada": 0.122107,
        "reference_5arch_J_hurt_lambada": 0.094597,
        "reference_5arch_J_helped_arceasy": 0.10813,
        "reference_5arch_J_hurt_arceasy": 0.104682,
        "reference_4arch_J_helped_lambada": 0.1219,
        "reference_4arch_J_hurt_lambada": 0.0965,
        "reference_4arch_J_helped_arceasy": 0.1034,
        "reference_4arch_J_hurt_arceasy": 0.1059,
    }

out_path = str(EXP5 / "jaccard_6arch.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to {out_path}")
