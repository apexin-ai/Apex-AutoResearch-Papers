"""Per-seed bootstrap construction test for FewNERD 7B (seeds 42/123/456).
Computes per-instance greedy_f1 and LP-weighted construction_f1,
then runs paired bootstrap test (B=10000).
"""
import json
import math
import os
import sys
import numpy as np
from collections import defaultdict

BASE = "/root/autodl-tmp/struct_self_consist_ie"
sys.stdout = open(sys.stdout.fileno(), mode='w', buffering=1)

SEED_PATHS = {
    42: f"{BASE}/output/exp_021_inference/samples.jsonl",
    123: f"{BASE}/output/exp_021_fewnerd_n8_seed123/samples.jsonl",
    456: f"{BASE}/output/exp_021_fewnerd_n8_seed456/samples.jsonl",
}

SEED_OUTPUT_DIRS = {
    42: f"{BASE}/output/exp_021_inference",
    123: f"{BASE}/output/exp_021_fewnerd_n8_seed123",
    456: f"{BASE}/output/exp_021_fewnerd_n8_seed456",
}

N_BOOTSTRAP = 10000


def load_data(path, gold_filter=True):
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if gold_filter and not obj["gold"].get("entities", []):
                continue
            instances.append(obj)
    return instances


def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}


def compute_prf(pred_set, gold_set):
    if not gold_set and not pred_set:
        return 1.0, 1.0, 1.0
    if not pred_set:
        return 0.0, 0.0, 0.0
    if not gold_set:
        return 0.0, 0.0, 0.0
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0, 0.0, 0.0
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    f = 2 * p * r / (p + r)
    return p, r, f


def get_lp_weights(inst):
    samples = inst["samples"]
    lps = []
    for s in samples:
        lp = s.get("mean_logprob", None)
        if lp is None or not math.isfinite(lp):
            lp = -100.0
        lps.append(lp)
    max_lp = max(lps)
    ws = [math.exp(lp - max_lp) for lp in lps]
    total = sum(ws)
    return [w / total for w in ws]


def entity_majority_vote(samples, threshold, weights=None):
    entity_counts = defaultdict(float)
    N = len(samples)
    for i, sample in enumerate(samples):
        w = weights[i] if weights is not None else 1.0
        for e in sample.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            entity_counts[key] += w
    total_weight = sum(weights) if weights is not None else N
    constructed = set()
    for key, count in entity_counts.items():
        if count / total_weight >= threshold:
            constructed.add(key)
    return constructed


def bootstrap_test(f1_method, f1_baseline, B=10000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(f1_method)
    diffs = f1_method - f1_baseline
    observed_diff = float(diffs.mean())
    boot_diffs = np.zeros(B)
    for b in range(B):
        idx = rng.randint(0, n, n)
        boot_diffs[b] = diffs[idx].mean()
    ci_low = float(np.percentile(boot_diffs, 2.5))
    ci_high = float(np.percentile(boot_diffs, 97.5))
    p_value = float((boot_diffs <= 0).mean())
    cohens_d = observed_diff / float(diffs.std(ddof=1)) if diffs.std(ddof=1) > 0 else 0.0
    return {
        "observed_diff": observed_diff,
        "ci_95": [ci_low, ci_high],
        "p_value": p_value,
        "cohens_d": float(cohens_d),
        "significant_005": p_value < 0.05,
    }


def process_seed(seed, path, output_dir):
    print(f"\n{'='*60}")
    print(f"Seed {seed}: {path}")
    print(f"{'='*60}")

    data = load_data(path, gold_filter=True)
    n = len(data)
    n_samples = len(data[0]["samples"])
    theta = 2.0 / n_samples  # 0.25 for N=8
    print(f"Instances: {n}, N={n_samples}, theta={theta}")

    greedy_f1s = np.zeros(n)
    lp_construction_f1s = np.zeros(n)
    lp_selection_f1s = np.zeros(n)
    per_instance = []

    for i, inst in enumerate(data):
        gold = entity_set(inst["gold"]["entities"])

        # Greedy
        greedy = inst.get("greedy", inst["samples"][0])
        pred_greedy = entity_set(greedy.get("entities", []))
        _, _, f_greedy = compute_prf(pred_greedy, gold)
        greedy_f1s[i] = f_greedy

        # LP-weighted construction
        ws = get_lp_weights(inst)
        pred_lp = entity_majority_vote(inst["samples"], theta, weights=ws)
        _, _, f_lp = compute_prf(pred_lp, gold)
        lp_construction_f1s[i] = f_lp

        # LP selection (best-of-N by logprob)
        lps = [s.get("mean_logprob", -999) for s in inst["samples"]]
        best_idx = int(np.argmax(lps))
        pred_sel = entity_set(inst["samples"][best_idx].get("entities", []))
        _, _, f_sel = compute_prf(pred_sel, gold)
        lp_selection_f1s[i] = f_sel

        per_instance.append({
            "instance_id": inst.get("instance_id", i),
            "greedy_f1": float(f_greedy),
            "lp_construction_f1": float(f_lp),
            "lp_selection_f1": float(f_sel),
        })

        if (i + 1) % 5000 == 0:
            print(f"  {i+1}/{n}")

    print(f"Greedy F1: {greedy_f1s.mean():.4f}")
    print(f"LP-construction F1: {lp_construction_f1s.mean():.4f} (Δ={100*(lp_construction_f1s.mean()-greedy_f1s.mean()):+.2f}pp)")
    print(f"LP-selection F1: {lp_selection_f1s.mean():.4f} (Δ={100*(lp_selection_f1s.mean()-greedy_f1s.mean()):+.2f}pp)")

    # Save per-instance
    pi_path = os.path.join(output_dir, "fewnerd_per_instance.json")
    with open(pi_path, "w") as f:
        json.dump(per_instance, f)
    print(f"Saved: {pi_path} ({len(per_instance)} instances)")

    # Bootstrap tests
    print("Running bootstrap tests (B=10000)...")
    bt_construction = bootstrap_test(lp_construction_f1s, greedy_f1s, B=N_BOOTSTRAP, seed=42)
    bt_selection = bootstrap_test(lp_selection_f1s, greedy_f1s, B=N_BOOTSTRAP, seed=42)

    result = {
        "seed": seed,
        "n_instances": n,
        "n_samples": n_samples,
        "theta": theta,
        "greedy_f1": float(greedy_f1s.mean()),
        "lp_construction_f1": float(lp_construction_f1s.mean()),
        "lp_selection_f1": float(lp_selection_f1s.mean()),
        "bootstrap_lp_construction_vs_greedy": bt_construction,
        "bootstrap_lp_selection_vs_greedy": bt_selection,
    }

    bp_path = os.path.join(output_dir, "fewnerd_paired_bootstrap_result.json")
    with open(bp_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"Saved: {bp_path}")

    print(f"\nConstruction bootstrap: obs_diff={bt_construction['observed_diff']:.4f}, "
          f"95%CI=[{bt_construction['ci_95'][0]:.4f}, {bt_construction['ci_95'][1]:.4f}], "
          f"p={bt_construction['p_value']:.4f}, d={bt_construction['cohens_d']:.4f}")
    print(f"Selection bootstrap:    obs_diff={bt_selection['observed_diff']:.4f}, "
          f"95%CI=[{bt_selection['ci_95'][0]:.4f}, {bt_selection['ci_95'][1]:.4f}], "
          f"p={bt_selection['p_value']:.4f}, d={bt_selection['cohens_d']:.4f}")

    return result


def main():
    all_results = {}
    for seed in sorted(SEED_PATHS.keys()):
        path = SEED_PATHS[seed]
        output_dir = SEED_OUTPUT_DIRS[seed]
        if not os.path.exists(path):
            print(f"SKIP seed {seed}: {path} not found")
            continue
        result = process_seed(seed, path, output_dir)
        all_results[seed] = result

    # Summary
    print("\n" + "=" * 60)
    print("3-SEED SUMMARY")
    print("=" * 60)
    print(f"{'Seed':>6} | {'Greedy':>8} | {'LPConstr':>8} | {'ΔConstr':>8} | {'p_constr':>8} | {'d_constr':>8} | {'LPSel':>8} | {'ΔSel':>8} | {'p_sel':>8}")
    print("-" * 100)
    for seed in sorted(all_results.keys()):
        r = all_results[seed]
        bc = r["bootstrap_lp_construction_vs_greedy"]
        bs = r["bootstrap_lp_selection_vs_greedy"]
        print(f"{seed:>6} | {r['greedy_f1']:.4f}   | {r['lp_construction_f1']:.4f}   | "
              f"{100*bc['observed_diff']:+.2f}pp | {bc['p_value']:.4f}   | {bc['cohens_d']:.4f}   | "
              f"{r['lp_selection_f1']:.4f}   | {100*bs['observed_diff']:+.2f}pp | {bs['p_value']:.4f}")

    # Save combined
    combined_path = f"{BASE}/output/fewnerd_3seed_construction_bootstrap.json"
    with open(combined_path, "w") as f:
        json.dump({str(k): v for k, v in all_results.items()}, f, indent=2)
    print(f"\nCombined results: {combined_path}")


if __name__ == "__main__":
    main()
