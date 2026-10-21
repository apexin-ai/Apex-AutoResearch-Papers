#!/usr/bin/env python3
"""exp-005: 6-Architecture Pairwise Jaccard Analysis (340M, hybrid-3-1 vs transformer)."""
import json, os, glob
import numpy as np
from itertools import combinations

np.random.seed(42)

ARCHS = ["GDN", "RetNet", "HGRN2", "GLA", "DeltaNet", "HGRN"]
BENCHMARKS = ["lambada_openai", "arc_easy"]
N_PERM = 10000
OUTDIR = "/root/entrainment_gated_ft/results/exp005_zoo_expansion"

JSON_340M = "/root/entrainment_gated_ft/lm_eval_clean/340m"
EXP005 = OUTDIR

def load_from_json(path, task):
    with open(path) as f:
        data = json.load(f)
    samples = data["samples"][task]
    return sorted(samples, key=lambda x: x["doc_id"])

def load_from_jsonl(path):
    samples = []
    with open(path) as f:
        for line in f:
            samples.append(json.loads(line))
    return sorted(samples, key=lambda x: x["doc_id"])

def find_jsonl(base_dir, task):
    pattern = os.path.join(base_dir, "**", f"samples_{task}_*.jsonl")
    matches = glob.glob(pattern, recursive=True)
    if not matches:
        pattern = os.path.join(base_dir, "**", f"{task}.jsonl")
        matches = glob.glob(pattern, recursive=True)
    if not matches:
        return None
    return sorted(matches)[-1]

def extract_acc(samples, task):
    return np.array([float(s["acc"]) for s in samples])

def jaccard(a, b):
    if len(a) == 0 and len(b) == 0:
        return 0.0
    return len(a & b) / len(a | b)

print("Loading data...")

transformer_data = {}
transformer_path = os.path.join(JSON_340M, "transformer_340M_baseline.json")
for task in BENCHMARKS:
    samples = load_from_json(transformer_path, task)
    transformer_data[task] = extract_acc(samples, task)
    print(f"  transformer {task}: N={len(transformer_data[task])}, acc={transformer_data[task].mean():.4f}")

arch_data = {}

gdn_path = os.path.join(JSON_340M, "340M-20B-GatedDeltaNet-hybrid-3-1.json")
for task in BENCHMARKS:
    samples = load_from_json(gdn_path, task)
    arch_data[("GDN", task)] = extract_acc(samples, task)
    print(f"  GDN h3-1 {task}: N={len(arch_data[('GDN', task)])}, acc={arch_data[('GDN', task)].mean():.4f}")

exp005_dirs = {
    "RetNet": "RetNet_h3-1",
    "HGRN2": "HGRN2_h3-1",
    "GLA": "GLA_h3-1",
    "DeltaNet": "DeltaNet_h3-1",
    "HGRN": "HGRN_h3-1",
}
for arch, dirname in exp005_dirs.items():
    search_dir = os.path.join(EXP005, dirname)
    for task in BENCHMARKS:
        jsonl_path = find_jsonl(search_dir, task)
        if jsonl_path is None:
            print(f"  WARNING: {arch} {task} not found in {search_dir}")
            continue
        samples = load_from_jsonl(jsonl_path)
        arch_data[(arch, task)] = extract_acc(samples, task)
        print(f"  {arch} h3-1 {task}: N={len(arch_data[(arch, task)])}, acc={arch_data[(arch, task)].mean():.4f}")

missing = []
for arch in ARCHS:
    for task in BENCHMARKS:
        if (arch, task) not in arch_data:
            missing.append(f"{arch}-{task}")
if missing:
    print(f"\nMISSING DATA: {missing}")
    print("Cannot proceed. Exiting.")
    exit(1)

print("\nComputing helped/hurt sets (hybrid correct & transformer wrong / vice versa)...")
results_all = {}

for task in BENCHMARKS:
    print(f"\n--- {task} ---")
    t_acc = transformer_data[task]
    N = len(t_acc)

    stats = {}
    for arch in ARCHS:
        h_acc = arch_data[(arch, task)]
        assert len(h_acc) == N, f"Size mismatch: {arch} {task} has {len(h_acc)}, expected {N}"
        helped_mask = (h_acc == 1) & (t_acc == 0)
        hurt_mask = (h_acc == 0) & (t_acc == 1)
        stats[arch] = {
            "helped_set": set(np.where(helped_mask)[0]),
            "hurt_set": set(np.where(hurt_mask)[0]),
            "helped_size": int(helped_mask.sum()),
            "hurt_size": int(hurt_mask.sum()),
            "acc": float(h_acc.mean()),
        }
        print(f"  {arch}: acc={stats[arch]['acc']:.4f}, helped={stats[arch]['helped_size']}, hurt={stats[arch]['hurt_size']}")

    pairs = list(combinations(ARCHS, 2))
    print(f"\n  Pairwise Jaccard ({len(pairs)} pairs):")
    obs = {"helped": {}, "hurt": {}}
    for a1, a2 in pairs:
        key = f"{a1}-{a2}"
        for cat in ["helped", "hurt"]:
            j = jaccard(stats[a1][f"{cat}_set"], stats[a2][f"{cat}_set"])
            obs[cat][key] = j
        print(f"    {key}: J_helped={obs['helped'][key]:.4f}, J_hurt={obs['hurt'][key]:.4f}")

    print(f"\n  Running permutation test ({N_PERM} iterations)...")
    rng = np.random.default_rng(42)
    indices = np.arange(N)

    null_jaccards = {cat: {f"{a1}-{a2}": [] for a1, a2 in pairs} for cat in ["helped", "hurt"]}

    for i in range(N_PERM):
        if (i + 1) % 2000 == 0:
            print(f"    iteration {i+1}/{N_PERM}")
        for cat in ["helped", "hurt"]:
            shuffled_sets = {}
            for arch in ARCHS:
                size = stats[arch][f"{cat}_size"]
                shuffled_sets[arch] = set(rng.choice(indices, size=size, replace=False))
            for a1, a2 in pairs:
                key = f"{a1}-{a2}"
                j = jaccard(shuffled_sets[a1], shuffled_sets[a2])
                null_jaccards[cat][key].append(j)

    perm_results = {"helped": {}, "hurt": {}}
    for cat in ["helped", "hurt"]:
        for a1, a2 in pairs:
            key = f"{a1}-{a2}"
            null_arr = np.array(null_jaccards[cat][key])
            j_obs = obs[cat][key]
            j_null_mean = null_arr.mean()
            j_null_std = null_arr.std()
            p_value = (np.sum(null_arr >= j_obs) + 1) / (N_PERM + 1)
            z_score = (j_obs - j_null_mean) / j_null_std if j_null_std > 0 else float("inf")
            perm_results[cat][key] = {
                "J_obs": round(j_obs, 6),
                "J_null_mean": round(j_null_mean, 6),
                "J_null_std": round(j_null_std, 6),
                "z_score": round(z_score, 2),
                "p_value": round(p_value, 6),
            }

    mean_J_helped = np.mean([obs["helped"][k] for k in obs["helped"]])
    mean_J_hurt = np.mean([obs["hurt"][k] for k in obs["hurt"]])

    z_helped_all = [perm_results["helped"][k]["z_score"] for k in perm_results["helped"]]
    z_hurt_all = [perm_results["hurt"][k]["z_score"] for k in perm_results["hurt"]]

    n_ambiguous = 0
    for i in range(N):
        vals = set()
        for arch in ARCHS:
            h_acc = arch_data[(arch, task)]
            vals.add(int(h_acc[i]))
        if len(vals) > 1:
            n_ambiguous += 1
    alpha = n_ambiguous / N

    print(f"\n  Summary for {task}:")
    print(f"    Mean J_helped = {mean_J_helped:.4f}")
    print(f"    Mean J_hurt = {mean_J_hurt:.4f}")
    print(f"    Mean z_helped = {np.mean(z_helped_all):.2f}")
    print(f"    Mean z_hurt = {np.mean(z_hurt_all):.2f}")
    print(f"    Ambiguity alpha = {alpha:.4f}")

    results_all[task] = {
        "pairwise_jaccard_helped": obs["helped"],
        "pairwise_jaccard_hurt": obs["hurt"],
        "permutation_test_helped": perm_results["helped"],
        "permutation_test_hurt": perm_results["hurt"],
        "mean_J_helped": round(mean_J_helped, 6),
        "mean_J_hurt": round(mean_J_hurt, 6),
        "mean_z_helped": round(np.mean(z_helped_all), 2),
        "mean_z_hurt": round(np.mean(z_hurt_all), 2),
        "ambiguity_alpha": round(alpha, 6),
        "per_arch_accuracy": {arch: round(stats[arch]["acc"], 6) for arch in ARCHS},
        "per_arch_helped_size": {arch: stats[arch]["helped_size"] for arch in ARCHS},
        "per_arch_hurt_size": {arch: stats[arch]["hurt_size"] for arch in ARCHS},
        "transformer_acc": round(float(t_acc.mean()), 6),
        "N": N,
    }

output = {
    "experiment": "exp-005",
    "description": "6-architecture pairwise Jaccard (340M hybrid-3-1 vs transformer)",
    "n_architectures": 6,
    "n_pairs": 15,
    "architectures": ARCHS,
    "n_permutations": N_PERM,
    "benchmarks": results_all,
}

out_path = os.path.join(OUTDIR, "analysis_results.json")
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\nResults saved to {out_path}")

print("\n" + "=" * 80)
print("FINAL SUMMARY")
print("=" * 80)
for task in BENCHMARKS:
    r = results_all[task]
    print(f"\n{task}:")
    print(f"  Transformer acc: {r['transformer_acc']:.4f}")
    print(f"  Per-arch acc: {r['per_arch_accuracy']}")
    print(f"  Mean J_helped: {r['mean_J_helped']:.4f} (z={r['mean_z_helped']:.2f})")
    print(f"  Mean J_hurt: {r['mean_J_hurt']:.4f} (z={r['mean_z_hurt']:.2f})")
    print(f"  Ambiguity alpha: {r['ambiguity_alpha']:.4f}")
    print(f"  All 15 pairs helped J: {list(r['pairwise_jaccard_helped'].values())}")
    print(f"  All 15 pairs hurt J: {list(r['pairwise_jaccard_hurt'].values())}")
