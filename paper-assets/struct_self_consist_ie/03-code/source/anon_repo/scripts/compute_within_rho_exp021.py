import json
import numpy as np
from scipy.stats import spearmanr

N_SAMPLES = 8

def entity_strict_f1(pred_entities, gold_entities):
    pred_set = {(e["start"], e["end"], e["type"]) for e in pred_entities}
    gold_set = {(e["start"], e["end"], e["type"]) for e in gold_entities}
    tp = len(pred_set & gold_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    return 2*p*r/(p+r) if (p+r) > 0 else 0.0

def get_lp(sample, inst_logprobs, idx):
    if "mean_logprob" in sample:
        return sample["mean_logprob"]
    if inst_logprobs is not None and idx < len(inst_logprobs):
        return inst_logprobs[idx]
    if "cumulative_logprob" in sample:
        return sample["cumulative_logprob"] / max(sample.get("n_tokens", 1), 1)
    return None

def compute_within_rho(input_path, label):
    instances = []
    with open(input_path) as f:
        for line in f:
            if line.strip():
                instances.append(json.loads(line))

    n_total = len(instances)
    gold_filtered = [inst for inst in instances if len(inst["gold"].get("entities", [])) > 0]
    n_gf = len(gold_filtered)

    within_rhos = []
    for inst in gold_filtered:
        samples = inst["samples"][:N_SAMPLES]
        gold_ents = inst["gold"]["entities"]
        inst_logprobs = inst.get("logprobs", None)

        f1s = [entity_strict_f1(s.get("entities", []), gold_ents) for s in samples]
        lps = []
        for idx, s in enumerate(samples):
            lp = get_lp(s, inst_logprobs, idx)
            if lp is not None:
                lps.append(lp)
            else:
                break

        if len(lps) == N_SAMPLES:
            f1_arr = np.array(f1s)
            lp_arr = np.array(lps)
            if np.std(f1_arr) > 0 and np.std(lp_arr) > 0:
                rho, _ = spearmanr(lp_arr, f1_arr)
                if np.isfinite(rho):
                    within_rhos.append(rho)

    rho_arr = np.array(within_rhos) if within_rhos else np.array([])

    result = {
        "label": label,
        "input": input_path,
        "n_total": n_total,
        "n_gold_filtered": n_gf,
        "n_samples": N_SAMPLES,
        "within_instance_rho": {
            "mean": round(float(np.mean(rho_arr)), 4) if len(within_rhos) > 0 else None,
            "median": round(float(np.median(rho_arr)), 4) if len(within_rhos) > 0 else None,
            "std": round(float(np.std(rho_arr)), 4) if len(within_rhos) > 0 else None,
            "valid_count": len(within_rhos),
            "valid_pct": round(len(within_rhos) / n_gf * 100, 2) if n_gf > 0 else 0,
        }
    }
    print(json.dumps(result, indent=2))
    return result

# exp_027 (3-epoch, same 5000 instances as exp_028, N=8 from 16)
print("=== exp_027 (3-epoch, 5000 instances, N=8) ===")
r1 = compute_within_rho(
    "/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl",
    "exp_027_3epoch_5k"
)

# exp_021 full (3-epoch, full 37648 instances, N=8)
print("\n=== exp_021 full (3-epoch, full dataset, N=8) ===")
r2 = compute_within_rho(
    "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl",
    "exp_021_3epoch_full"
)

# exp_028 reference
print("\n=== Comparison ===")
print(f"exp_027 3-epoch (5k):  mean={r1['within_instance_rho']['mean']}, median={r1['within_instance_rho']['median']}, valid={r1['within_instance_rho']['valid_count']}/{r1['n_gold_filtered']}")
print(f"exp_021 3-epoch (full): mean={r2['within_instance_rho']['mean']}, median={r2['within_instance_rho']['median']}, valid={r2['within_instance_rho']['valid_count']}/{r2['n_gold_filtered']}")
print(f"exp_028 5-epoch (5k):  mean=0.4066, median=0.6151, valid=2988/4351 (reference)")
