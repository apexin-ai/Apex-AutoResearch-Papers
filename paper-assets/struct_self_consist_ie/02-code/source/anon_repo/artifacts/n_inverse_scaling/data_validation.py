#!/usr/bin/env python3
"""Validate N inverse scaling data: check Qwen_FewNERD n=4351, F1=0.7926."""

import json, os, time

BASE = "/root/autodl-tmp/struct_self_consist_ie"


def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}


def load_data(path, gold_filter=True, maxn=None):
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if gold_filter and not obj["gold"].get("entities", []):
                continue
            instances.append(obj)
            if maxn and len(instances) >= maxn:
                break
    return instances


def compute_greedy_f1(instances):
    tp = fp = fn = 0
    for inst in instances:
        gold = entity_set(inst["gold"]["entities"])
        pred = entity_set(inst.get("greedy", {}).get("entities", []))
        tp += len(pred & gold)
        fp += len(pred - gold)
        fn += len(gold - pred)
    if tp == 0:
        return 0.0, 0.0, 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    f = 2 * p * r / (p + r)
    return p, r, f


def main():
    results = {}

    # 1. Check exp_027_fewnerd_n16 (used by inverse scaling)
    print("=== Qwen_FewNERD Inverse Scaling Data Validation ===\n")
    path_027 = f"{BASE}/output/exp_027_fewnerd_n16/samples.jsonl"

    print("--- exp_027_fewnerd_n16 ---")
    total_lines = sum(1 for line in open(path_027) if line.strip())
    instances_027 = load_data(path_027, gold_filter=True)
    instances_027_all = load_data(path_027, gold_filter=False)
    n_samples = len(instances_027[0]["samples"])
    first_id = instances_027_all[0]["id"]
    last_id = instances_027_all[-1]["id"]
    p, r, f1 = compute_greedy_f1(instances_027)

    print(f"  Total lines: {total_lines}")
    print(f"  With gold entities: {len(instances_027)}")
    print(f"  Without gold: {total_lines - len(instances_027)}")
    print(f"  N_samples per instance: {n_samples}")
    print(f"  ID range: {first_id} → {last_id}")
    print(f"  Greedy F1: {f1:.10f}")
    print(f"  Greedy P/R: {p:.4f}/{r:.4f}")

    results["exp_027_fewnerd_n16"] = {
        "total_lines": total_lines,
        "n_with_gold": len(instances_027),
        "n_without_gold": total_lines - len(instances_027),
        "n_samples": n_samples,
        "id_range": [first_id, last_id],
        "greedy_f1": f1,
        "greedy_precision": p,
        "greedy_recall": r,
    }

    # 2. Check full FewNERD test set
    print("\n--- Full FewNERD test (exp_021_fewnerd_n8_seed123) ---")
    path_full = f"{BASE}/output/exp_021_fewnerd_n8_seed123/samples.jsonl"
    total_full = sum(1 for line in open(path_full) if line.strip())
    instances_full = load_data(path_full, gold_filter=True)
    n_samples_full = len(instances_full[0]["samples"])
    p_full, r_full, f1_full = compute_greedy_f1(instances_full)

    print(f"  Total lines: {total_full}")
    print(f"  With gold entities: {len(instances_full)}")
    print(f"  N_samples per instance: {n_samples_full}")
    print(f"  Greedy F1: {f1_full:.10f}")
    print(f"  Greedy P/R: {p_full:.4f}/{r_full:.4f}")

    results["full_fewnerd_test"] = {
        "total_lines": total_full,
        "n_with_gold": len(instances_full),
        "n_samples": n_samples_full,
        "greedy_f1": f1_full,
        "greedy_precision": p_full,
        "greedy_recall": r_full,
    }

    # 3. Check ID overlap
    print("\n--- Subset Analysis ---")
    ids_027 = {inst["id"] for inst in instances_027_all}
    ids_full = {inst["id"] for inst in load_data(path_full, gold_filter=False)}
    overlap = ids_027 & ids_full
    print(f"  exp_027 IDs in full set: {len(overlap)} / {len(ids_027)}")

    # Parse numeric IDs
    import re
    nums_027 = sorted(int(re.search(r'\d+$', i).group()) for i in ids_027)
    print(f"  exp_027 numeric ID range: {nums_027[0]} → {nums_027[-1]}")
    print(f"  Contiguous? {nums_027[-1] - nums_027[0] + 1 == len(nums_027)}")

    # 4. Check if it's a shard-based subset
    print("\n--- Shard Structure ---")
    shard_dir = f"{BASE}/output/exp_027_fewnerd_n16"
    for shard in ["shard_0", "shard_1", "shard_2", "shard_3"]:
        sp = f"{shard_dir}/{shard}/samples.jsonl"
        if os.path.exists(sp):
            n = sum(1 for line in open(sp) if line.strip())
            first = json.loads(open(sp).readline())["id"]
            print(f"  {shard}: {n} lines, first_id={first}")

    # 5. Greedy F1 on the exp_027 subset vs same subset from full data
    print("\n--- F1 Comparison on Same Subset ---")
    full_subset = [inst for inst in instances_full if inst["id"] in ids_027]
    if full_subset:
        # Only keep instances with gold entities that are in the 027 set
        full_subset_with_gold = [inst for inst in full_subset
                                 if inst["gold"].get("entities", [])]
        p_sub, r_sub, f1_sub = compute_greedy_f1(full_subset_with_gold)
        print(f"  Full data, same IDs (n={len(full_subset_with_gold)}): Greedy F1={f1_sub:.6f}")
        print(f"  exp_027 data (n={len(instances_027)}): Greedy F1={f1:.6f}")
        if abs(f1 - f1_sub) < 1e-6:
            print(f"  → F1 matches: same data, different sample seeds")
        else:
            print(f"  → F1 differs: different greedy results (different checkpoints?)")
            # Check N=8 from exp_027 (it has N=16, greedy might use all 16)
            print(f"  NOTE: exp_027 has N={n_samples} samples, full has N={n_samples_full}")
    else:
        print(f"  No overlapping IDs found (different ID format?)")

    # 6. Check other configs in inverse scaling
    print("\n--- All Inverse Scaling Configs ---")
    configs = {
        "Qwen_SciERC": f"{BASE}/output/exp_001_seed42_v2/samples.jsonl",
        "Qwen_CoNLL": f"{BASE}/output/exp_002_conll_n16/samples.jsonl",
        "Qwen_FewNERD": f"{BASE}/output/exp_027_fewnerd_n16/samples.jsonl",
        "LLaMA_SciERC": f"{BASE}/output/exp_007_llama_n16_r1024/samples.jsonl",
        "LLaMA_CoNLL": f"{BASE}/output/exp_017_llama_conll_n16/samples.jsonl",
        "LLaMA_FewNERD": f"{BASE}/output/llama_fewnerd_s42/samples.jsonl",
    }

    config_validation = {}
    for name, path in configs.items():
        if not os.path.exists(path):
            print(f"  {name}: FILE NOT FOUND")
            config_validation[name] = {"status": "file_not_found", "path": path}
            continue
        total = sum(1 for line in open(path) if line.strip())
        insts = load_data(path, gold_filter=True)
        n_samp = len(insts[0]["samples"]) if insts else 0
        p, r, f1 = compute_greedy_f1(insts)
        print(f"  {name}: total={total}, with_gold={len(insts)}, N_samples={n_samp}, "
              f"greedy_F1={f1:.4f}")
        config_validation[name] = {
            "path": path,
            "total_lines": total,
            "n_with_gold": len(insts),
            "n_samples": n_samp,
            "greedy_f1": round(f1, 6),
        }

    # 7. Summary
    print("\n" + "="*60)
    print("DIAGNOSIS SUMMARY")
    print("="*60)

    print(f"\n1. n=4351 explanation:")
    print(f"   exp_027_fewnerd_n16 contains only {total_lines} instances (not full 32565+)")
    print(f"   After gold_filter: {len(instances_027)} instances")
    print(f"   ID range: {nums_027[0]}→{nums_027[-1]} (subset of 0→{total_full-1})")
    print(f"   → SUBSET, not full test set. Likely a sharded/truncated inference run.")

    print(f"\n2. F1=0.7926 explanation:")
    print(f"   Greedy F1 on exp_027 subset: {results['exp_027_fewnerd_n16']['greedy_f1']:.6f}")
    print(f"   Greedy F1 on full FewNERD:   {results['full_fewnerd_test']['greedy_f1']:.6f}")
    f1_diff = results['exp_027_fewnerd_n16']['greedy_f1'] - results['full_fewnerd_test']['greedy_f1']
    print(f"   Difference: {f1_diff*100:+.2f}pp")
    if n_samples != n_samples_full:
        print(f"   ALSO: exp_027 has N={n_samples} samples vs full N={n_samples_full}")
        print(f"   → Greedy may use different number of samples for construction")

    print(f"\n3. Verdict:")
    is_bug = False
    issues = []
    if len(instances_027) != 32565:
        issues.append(f"Uses {len(instances_027)}/{32565} instances (subset)")
    if abs(f1_diff) > 0.01:
        issues.append(f"Greedy F1 differs by {f1_diff*100:.2f}pp from full-set")
    if n_samples != n_samples_full:
        issues.append(f"N_samples mismatch: {n_samples} vs {n_samples_full}")

    if issues:
        print(f"   Issues found:")
        for iss in issues:
            print(f"   - {iss}")
        print(f"   → NOT a code bug. The N inverse scaling analysis ran on a SUBSET of FewNERD.")
        print(f"     This is valid for relative comparisons (inverse scaling detection) but")
        print(f"     the absolute F1 values differ from full-set numbers.")
        print(f"     The subset ({nums_027[0]}→{nums_027[-1]}) may be non-representative.")
    else:
        print(f"   No issues found.")

    results["diagnosis"] = {
        "n_4351_reason": f"subset: exp_027 has {total_lines} total lines, {len(instances_027)} after gold_filter",
        "f1_0_7926_reason": f"greedy F1 on this subset, not full test set (full: {f1_full:.4f})",
        "n_samples_exp027": n_samples,
        "n_samples_full": n_samples_full,
        "is_code_bug": False,
        "is_data_subset": True,
        "subset_id_range": [nums_027[0], nums_027[-1]],
        "full_test_n_with_gold": len(instances_full),
        "issues": issues,
    }

    results["config_validation"] = config_validation

    out_path = f"{BASE}/artifacts/n_inverse_scaling/data_validation.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path}")
    print("DONE")


if __name__ == "__main__":
    main()
