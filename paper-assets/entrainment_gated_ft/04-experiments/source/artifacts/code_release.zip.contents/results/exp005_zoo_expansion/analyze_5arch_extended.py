#!/usr/bin/env python3
"""5-architecture pairwise Jaccard extended to 4 benchmarks: LAMBADA, ARC-Easy, HellaSwag, PIQA."""
import json
import glob
import numpy as np
from itertools import combinations
from pathlib import Path

BASE = Path("/root/entrainment_gated_ft")
MULTI = BASE / "lm_eval_clean/340m_multi"
EXP5 = BASE / "results/exp005_zoo_expansion"

def find_jsonl(directory, task_prefix):
    """Find a JSONL file matching task prefix in a directory tree."""
    pattern = str(directory / f"**/*{task_prefix}*.jsonl")
    matches = glob.glob(pattern, recursive=True)
    if matches:
        return Path(matches[0])
    return None

# Build path mapping for all 4 benchmarks × 5 archs × {pure, h31}
PATHS = {}

# --- LAMBADA ---
PATHS["lambada_openai"] = {
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

# --- ARC-Easy ---
PATHS["arc_easy"] = {
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

# --- HellaSwag ---
PATHS["hellaswag"] = {
    "GDN":      {"pure": MULTI / "GDN-pure/samples/hellaswag.jsonl",
                 "h31":  MULTI / "GDN-h3-1/samples/hellaswag.jsonl"},
    "RetNet":   {"pure": MULTI / "RetNet-pure/samples/hellaswag.jsonl",
                 "h31":  MULTI / "RetNet-h3-1/samples/hellaswag.jsonl"},
    "HGRN2":    {"pure": MULTI / "HGRN2-pure/samples/hellaswag.jsonl",
                 "h31":  MULTI / "HGRN2-h3-1/samples/hellaswag.jsonl"},
    "GLA":      {"pure": None, "h31": None},  # will be filled after eval
    "DeltaNet": {"pure": None, "h31": None},
}

# --- PIQA ---
PATHS["piqa"] = {
    "GDN":      {"pure": MULTI / "GDN-pure/samples/piqa.jsonl",
                 "h31":  MULTI / "GDN-h3-1/samples/piqa.jsonl"},
    "RetNet":   {"pure": MULTI / "RetNet-pure/samples/piqa.jsonl",
                 "h31":  MULTI / "RetNet-h3-1/samples/piqa.jsonl"},
    "HGRN2":    {"pure": MULTI / "HGRN2-pure/samples/piqa.jsonl",
                 "h31":  MULTI / "HGRN2-h3-1/samples/piqa.jsonl"},
    "GLA":      {"pure": None, "h31": None},
    "DeltaNet": {"pure": None, "h31": None},
}

# Auto-discover GLA/DeltaNet hellaswag+piqa paths from eval output
for arch, out_h31, out_pure in [
    ("GLA", "GLA_h31_hswag_piqa", "GLA_pure_hswag_piqa"),
    ("DeltaNet", "DeltaNet_h31_hswag_piqa", "DeltaNet_pure_hswag_piqa"),
]:
    for task in ["hellaswag", "piqa"]:
        h31_path = find_jsonl(EXP5 / out_h31, task)
        pure_path = find_jsonl(EXP5 / out_pure, task)
        if h31_path and pure_path:
            PATHS[task][arch] = {"pure": pure_path, "h31": h31_path}
        else:
            missing = []
            if not h31_path: missing.append(f"{arch} h31 {task}")
            if not pure_path: missing.append(f"{arch} pure {task}")
            print(f"WARNING: Missing {', '.join(missing)}")


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
            random_sets[a] = set(rng.choice(n_total, size=sizes[a], replace=False))
        for a, b in pairs:
            j = jaccard(random_sets[a], random_sets[b])
            null_jaccards[f"{a}-{b}"].append(j)
    results = {}
    for a, b in pairs:
        key = f"{a}-{b}"
        obs_j = jaccard(helped_dict[a], helped_dict[b])
        null_arr = np.array(null_jaccards[key])
        null_mean = float(np.mean(null_arr))
        null_std = float(np.std(null_arr))
        z = (obs_j - null_mean) / null_std if null_std > 0 else 0.0
        p = float(np.mean(null_arr >= obs_j))
        results[key] = {"J_obs": round(obs_j, 6), "J_null_mean": round(null_mean, 6),
                        "J_null_std": round(null_std, 6), "z": round(z, 2), "p": round(p, 4)}
    return results


def analyze_benchmark(task_name, task_paths, archs):
    print(f"\n{'='*60}")
    print(f"BENCHMARK: {task_name}")
    print(f"{'='*60}")

    active_archs = []
    pure_acc = {}
    h31_acc = {}
    for arch in archs:
        p = task_paths.get(arch, {})
        pp, hp = p.get("pure"), p.get("h31")
        if pp is None or hp is None:
            print(f"  SKIP {arch}: missing paths")
            continue
        if not Path(pp).exists() or not Path(hp).exists():
            print(f"  SKIP {arch}: files not found ({pp}, {hp})")
            continue
        pure_acc[arch] = load_acc_dict(pp)
        h31_acc[arch] = load_acc_dict(hp)
        active_archs.append(arch)

    if len(active_archs) < 2:
        print("  Not enough architectures, skipping")
        return None

    doc_ids = set(pure_acc[active_archs[0]].keys())
    n_total = len(doc_ids)
    print(f"  n_samples = {n_total}, archs = {active_archs}")

    helped = {}
    hurt = {}
    for arch in active_archs:
        h = set()
        u = set()
        for did in doc_ids:
            p = pure_acc[arch].get(did, 0)
            q = h31_acc[arch].get(did, 0)
            if q == 1 and p == 0:
                h.add(did)
            elif q == 0 and p == 1:
                u.add(did)
        helped[arch] = h
        hurt[arch] = u
        net = len(h) - len(u)
        pa = sum(pure_acc[arch].values()) / n_total
        ha = sum(h31_acc[arch].values()) / n_total
        print(f"  {arch:10s}: helped={len(h):4d}, hurt={len(u):4d}, net={net:+4d}, pure_acc={pa:.4f}, h31_acc={ha:.4f}")

    pairs = list(combinations(active_archs, 2))
    pair_results = {}
    for a, b in pairs:
        jh = jaccard(helped[a], helped[b])
        ju = jaccard(hurt[a], hurt[b])
        pair_results[f"{a}-{b}"] = {
            "J_helped": round(jh, 6), "J_hurt": round(ju, 6),
            "|helped_a|": len(helped[a]), "|helped_b|": len(helped[b]),
            "|hurt_a|": len(hurt[a]), "|hurt_b|": len(hurt[b]),
            "|helped_inter|": len(helped[a] & helped[b]),
            "|hurt_inter|": len(hurt[a] & hurt[b]),
        }

    jh_vals = [v["J_helped"] for v in pair_results.values()]
    ju_vals = [v["J_hurt"] for v in pair_results.values()]
    mean_jh = np.mean(jh_vals)
    mean_ju = np.mean(ju_vals)

    print(f"\n  Pairwise Jaccard ({len(pairs)} pairs):")
    for k, v in pair_results.items():
        print(f"    {k:20s}: J_helped={v['J_helped']:.4f}, J_hurt={v['J_hurt']:.4f}")
    print(f"  Mean: J_helped={mean_jh:.4f}, J_hurt={mean_ju:.4f}")

    print(f"\n  Running permutation tests (10000 permutations)...")
    perm_helped = permutation_test(helped, active_archs, n_total)
    perm_hurt = permutation_test(hurt, active_archs, n_total)

    print(f"  Permutation test (helped):")
    sig_count_h = 0
    for k, v in perm_helped.items():
        sig = "***" if v["p"] < 0.001 else ("**" if v["p"] < 0.01 else ("*" if v["p"] < 0.05 else ""))
        if v["p"] < 0.05: sig_count_h += 1
        print(f"    {k:20s}: J_obs={v['J_obs']:.4f}, null={v['J_null_mean']:.4f}±{v['J_null_std']:.4f}, z={v['z']:.2f}, p={v['p']:.4f} {sig}")

    print(f"  Permutation test (hurt):")
    sig_count_u = 0
    for k, v in perm_hurt.items():
        sig = "***" if v["p"] < 0.001 else ("**" if v["p"] < 0.01 else ("*" if v["p"] < 0.05 else ""))
        if v["p"] < 0.05: sig_count_u += 1
        print(f"    {k:20s}: J_obs={v['J_obs']:.4f}, null={v['J_null_mean']:.4f}±{v['J_null_std']:.4f}, z={v['z']:.2f}, p={v['p']:.4f} {sig}")

    print(f"  Significant pairs: helped={sig_count_h}/10, hurt={sig_count_u}/10")

    z_helped_vals = [v["z"] for v in perm_helped.values()]
    z_hurt_vals = [v["z"] for v in perm_hurt.values()]

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
        "z_range_helped": [round(float(min(z_helped_vals)), 2), round(float(max(z_helped_vals)), 2)],
        "z_range_hurt": [round(float(min(z_hurt_vals)), 2), round(float(max(z_hurt_vals)), 2)],
        "sig_pairs_helped": sig_count_h,
        "sig_pairs_hurt": sig_count_u,
        "permutation_test_helped": perm_helped,
        "permutation_test_hurt": perm_hurt,
    }


ARCHS = ["GDN", "RetNet", "HGRN2", "GLA", "DeltaNet"]
BENCHMARKS = ["lambada_openai", "arc_easy", "hellaswag", "piqa"]

results = {
    "experiment": "exp-005",
    "date": "2026-05-23",
    "scale": "340M-20B",
    "description": "5-architecture pairwise Jaccard extended to 4 benchmarks (h3-1 vs pure)",
    "benchmarks": {}
}

for bm in BENCHMARKS:
    bm_result = analyze_benchmark(bm, PATHS[bm], ARCHS)
    if bm_result:
        results["benchmarks"][bm] = bm_result

# Cross-benchmark summary
print(f"\n{'='*60}")
print("CROSS-BENCHMARK SUMMARY (4 benchmarks)")
print(f"{'='*60}")

summary = {}
for bm in BENCHMARKS:
    if bm in results["benchmarks"]:
        r = results["benchmarks"][bm]
        print(f"  {bm:20s}: mean J_helped={r['mean_J_helped']:.4f}, J_hurt={r['mean_J_hurt']:.4f}, "
              f"z_helped=[{r['z_range_helped'][0]:.1f}, {r['z_range_helped'][1]:.1f}], "
              f"z_hurt=[{r['z_range_hurt'][0]:.1f}, {r['z_range_hurt'][1]:.1f}], "
              f"sig_h={r['sig_pairs_helped']}/10, sig_u={r['sig_pairs_hurt']}/10, n={r['n_samples']}")
        summary[f"mean_J_helped_{bm}"] = r["mean_J_helped"]
        summary[f"mean_J_hurt_{bm}"] = r["mean_J_hurt"]
        summary[f"z_range_helped_{bm}"] = r["z_range_helped"]
        summary[f"z_range_hurt_{bm}"] = r["z_range_hurt"]
        summary[f"sig_pairs_helped_{bm}"] = r["sig_pairs_helped"]
        summary[f"sig_pairs_hurt_{bm}"] = r["sig_pairs_hurt"]

# Grand mean across benchmarks
all_jh = [r["mean_J_helped"] for r in results["benchmarks"].values()]
all_ju = [r["mean_J_hurt"] for r in results["benchmarks"].values()]
summary["grand_mean_J_helped"] = round(float(np.mean(all_jh)), 6)
summary["grand_mean_J_hurt"] = round(float(np.mean(all_ju)), 6)
summary["n_benchmarks"] = len(results["benchmarks"])
summary["total_sig_helped"] = sum(r["sig_pairs_helped"] for r in results["benchmarks"].values())
summary["total_sig_hurt"] = sum(r["sig_pairs_hurt"] for r in results["benchmarks"].values())
summary["total_pairs_tested"] = len(results["benchmarks"]) * 10

print(f"\n  Grand mean: J_helped={summary['grand_mean_J_helped']:.4f}, J_hurt={summary['grand_mean_J_hurt']:.4f}")
print(f"  Total significant: helped={summary['total_sig_helped']}/{summary['total_pairs_tested']}, "
      f"hurt={summary['total_sig_hurt']}/{summary['total_pairs_tested']}")

results["cross_benchmark_summary"] = summary

out_path = str(EXP5 / "jaccard_5arch_extended.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to {out_path}")
