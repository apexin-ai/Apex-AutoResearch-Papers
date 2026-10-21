"""E4 Pythia Seed Calibration Analysis
Computes Jaccard overlap of correct/helped/hurt sets across seeds.
"""
import json, os, itertools, sys
from pathlib import Path
import numpy as np

base = Path("/root/entrainment_gated_ft/results/e4_pythia_seed/")

def load_samples(seed_dir, task_prefix):
    """Load per-example results from lm-eval log_samples files."""
    seed_dir = Path(seed_dir)
    # lm-eval 0.4.x saves samples as samples_<task>_*.jsonl
    for f in sorted(seed_dir.rglob(f"samples_{task_prefix}*.jsonl")):
        results = {}
        with open(f) as fh:
            for line in fh:
                doc = json.loads(line)
                doc_id = doc.get("doc_id", doc.get("idx"))
                # lm-eval stores per-metric results; check common acc fields
                acc = doc.get("acc", doc.get("exact_match"))
                if acc is None:
                    # For some tasks, check filtered metrics
                    for k, v in doc.items():
                        if "acc" in k.lower() and isinstance(v, (int, float)):
                            acc = v
                            break
                if acc is not None:
                    results[doc_id] = int(acc)
        if results:
            return results
    return None

def jaccard(a, b):
    if not a and not b:
        return 1.0
    return len(a & b) / len(a | b)

# Collect results
tasks = ["lambada_openai", "arc_easy"]
seed_dirs = sorted(base.glob("seed*"))

if not seed_dirs:
    print("ERROR: No seed directories found")
    sys.exit(1)

print(f"Found {len(seed_dirs)} seed directories: {[d.name for d in seed_dirs]}")

analysis = {}

for task in tasks:
    print(f"\n{'='*60}")
    print(f"Task: {task}")
    print(f"{'='*60}")
    
    # Load all seed results
    seed_results = {}
    for sd in seed_dirs:
        res = load_samples(sd, task)
        if res is not None:
            correct_set = {k for k, v in res.items() if v == 1}
            total = len(res)
            seed_results[sd.name] = {"correct": correct_set, "total": total, "acc": len(correct_set)/total}
            print(f"  {sd.name}: {len(correct_set)}/{total} correct ({len(correct_set)/total:.4f})")
    
    if len(seed_results) < 2:
        print(f"  Need at least 2 seeds, got {len(seed_results)}")
        continue
    
    seed_names = sorted(seed_results.keys())
    n = len(seed_names)
    
    # 1. Correct set Jaccard (all pairs)
    j_correct = []
    for i, j in itertools.combinations(range(n), 2):
        si, sj = seed_names[i], seed_names[j]
        j_val = jaccard(seed_results[si]["correct"], seed_results[sj]["correct"])
        j_correct.append(j_val)
    
    print(f"\n  Correct-set Jaccard (all {len(j_correct)} pairs):")
    print(f"    mean={np.mean(j_correct):.4f}, std={np.std(j_correct):.4f}")
    print(f"    min={min(j_correct):.4f}, max={max(j_correct):.4f}")
    
    # 2. Helped/Hurt analysis (each seed as base, take average)
    all_j_helped = []
    all_j_hurt = []
    
    for base_idx in range(n):
        base_name = seed_names[base_idx]
        base_set = seed_results[base_name]["correct"]
        
        helped_sets = {}
        hurt_sets = {}
        for k in range(n):
            if k == base_idx:
                continue
            other_name = seed_names[k]
            other_set = seed_results[other_name]["correct"]
            helped_sets[other_name] = other_set - base_set
            hurt_sets[other_name] = base_set - other_set
        
        others = [sn for sn in seed_names if sn != base_name]
        for i, j in itertools.combinations(range(len(others)), 2):
            h = jaccard(helped_sets[others[i]], helped_sets[others[j]])
            u = jaccard(hurt_sets[others[i]], hurt_sets[others[j]])
            all_j_helped.append(h)
            all_j_hurt.append(u)
    
    print(f"\n  Helped-set Jaccard (base-averaged):")
    print(f"    mean={np.mean(all_j_helped):.4f}, std={np.std(all_j_helped):.4f}")
    print(f"    min={min(all_j_helped):.4f}, max={max(all_j_helped):.4f}")
    
    print(f"\n  Hurt-set Jaccard (base-averaged):")
    print(f"    mean={np.mean(all_j_hurt):.4f}, std={np.std(all_j_hurt):.4f}")
    print(f"    min={min(all_j_hurt):.4f}, max={max(all_j_hurt):.4f}")
    
    # 3. Ambiguity alpha
    all_examples = set()
    for sr in seed_results.values():
        all_examples |= set(sr.get("correct", set()))
        # Need all doc_ids, not just correct ones
    # Recompute: alpha = fraction where not all seeds agree
    # For this we need full prediction sets
    first_sd = seed_dirs[0]
    full_res = load_samples(first_sd, task)
    if full_res:
        total_examples = len(full_res)
        unanimous_correct = set.intersection(*[sr["correct"] for sr in seed_results.values()])
        # Unanimous wrong = not in any correct set
        all_correct_union = set.union(*[sr["correct"] for sr in seed_results.values()])
        unanimous_wrong = set(full_res.keys()) - all_correct_union
        unanimous = len(unanimous_correct) + len(unanimous_wrong)
        alpha = 1 - unanimous / total_examples
        print(f"\n  Ambiguity alpha: {alpha:.4f}")
        print(f"    Total examples: {total_examples}")
        print(f"    Unanimous correct: {len(unanimous_correct)}")
        print(f"    Unanimous wrong: {len(unanimous_wrong)}")
        print(f"    Ambiguous: {total_examples - unanimous}")
    else:
        alpha = None
    
    # 4. Comparison with reference values
    print(f"\n  --- Comparison with cross-arch references ---")
    if task == "lambada_openai":
        ref_j_helped = 0.10
        ref_j_hurt = 0.09
        ref_alpha = 0.30
    elif task == "arc_easy":
        ref_j_helped = None
        ref_j_hurt = None
        ref_alpha = 0.21
    else:
        ref_j_helped = ref_j_hurt = ref_alpha = None
    
    if ref_j_helped is not None:
        ratio_h = np.mean(all_j_helped) / ref_j_helped
        print(f"    J_helped: within-seed={np.mean(all_j_helped):.4f} vs cross-arch={ref_j_helped}")
        print(f"    Ratio: {ratio_h:.2f}x")
    if ref_j_hurt is not None:
        ratio_u = np.mean(all_j_hurt) / ref_j_hurt
        print(f"    J_hurt: within-seed={np.mean(all_j_hurt):.4f} vs cross-arch={ref_j_hurt}")
        print(f"    Ratio: {ratio_u:.2f}x")
    if ref_alpha is not None and alpha is not None:
        print(f"    Alpha: within-seed={alpha:.4f} vs cross-arch={ref_alpha}")
    
    # Store for JSON output
    analysis[task] = {
        "n_seeds": n,
        "seed_accuracies": {sn: sr["acc"] for sn, sr in seed_results.items()},
        "correct_set_jaccard": {
            "mean": float(np.mean(j_correct)),
            "std": float(np.std(j_correct)),
            "min": float(min(j_correct)),
            "max": float(max(j_correct)),
        },
        "helped_set_jaccard": {
            "mean": float(np.mean(all_j_helped)),
            "std": float(np.std(all_j_helped)),
        },
        "hurt_set_jaccard": {
            "mean": float(np.mean(all_j_hurt)),
            "std": float(np.std(all_j_hurt)),
        },
        "ambiguity_alpha": float(alpha) if alpha else None,
        "reference_comparison": {
            "cross_arch_j_helped": ref_j_helped,
            "cross_arch_j_hurt": ref_j_hurt,
            "cross_arch_alpha": ref_alpha,
        }
    }

# Summary judgment
print(f"\n{'='*60}")
print("SUMMARY JUDGMENT")
print(f"{'='*60}")
for task, res in analysis.items():
    jh = res["helped_set_jaccard"]["mean"]
    ref = res["reference_comparison"]["cross_arch_j_helped"]
    if ref:
        if jh > ref * 1.5:
            verdict = "BAD (within-seed >> cross-arch)"
        elif jh < ref * 0.5:
            verdict = "STRONG SUPPORT (within-seed << cross-arch)"
        else:
            verdict = "WEAK/AMBIGUOUS"
        print(f"  {task}: J_helped={jh:.4f} vs ref={ref} → {verdict}")

# Save JSON
out_path = base / "e4_analysis.json"
with open(out_path, "w") as f:
    json.dump(analysis, f, indent=2)
print(f"\nResults saved to {out_path}")
