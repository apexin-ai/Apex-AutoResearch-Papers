import json
import numpy as np
from itertools import combinations
from pathlib import Path

CONFIGS = {
    "qwen_scierc": "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl",
    "llama_scierc": "/root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference/samples.jsonl",
    "qwen_conll": "/root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003/samples.jsonl",
    "llama_conll": "/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl",
}

def load_data(path):
    instances = []
    with open(path) as f:
        for line in f:
            obj = json.loads(line)
            if obj["gold"]["entities"]:
                instances.append(obj)
    return instances

def entity_key(e):
    return (e["start"], e["end"], e["type"])

def build_presence_matrix(samples):
    """Build N_samples x M_entities binary matrix."""
    all_entities = set()
    for s in samples:
        for e in s["entities"]:
            all_entities.add(entity_key(e))
    if not all_entities:
        return None, []
    all_entities = sorted(all_entities)
    ent_to_idx = {e: i for i, e in enumerate(all_entities)}
    M = len(all_entities)
    N = len(samples)
    matrix = np.zeros((N, M), dtype=int)
    for i, s in enumerate(samples):
        for e in s["entities"]:
            matrix[i, ent_to_idx[entity_key(e)]] = 1
    return matrix, all_entities

def pairwise_agreement(matrix):
    """Compute observed pairwise agreement rate for all C(N,2) pairs."""
    N, M = matrix.shape
    if M == 0:
        return []
    agreements = []
    for i, j in combinations(range(N), 2):
        agree = np.mean(matrix[i] == matrix[j])
        agreements.append(agree)
    return agreements

def chance_agreement(matrix):
    """Expected agreement under independence assumption.
    For each entity, p = marginal rate of presence.
    P(agree) = p^2 + (1-p)^2 for that entity.
    Average over all entities.
    """
    N, M = matrix.shape
    if M == 0:
        return 0.0
    p = matrix.mean(axis=0)  # marginal presence rate per entity
    p_agree_per_entity = p**2 + (1 - p)**2
    return float(np.mean(p_agree_per_entity))

def phi_coefficient(x, y):
    """Phi coefficient between two binary vectors."""
    n = len(x)
    n11 = np.sum(x & y)
    n10 = np.sum(x & ~y)
    n01 = np.sum(~x & y)
    n00 = np.sum(~x & ~y)
    denom = np.sqrt(float((n11+n10)*(n01+n00)*(n11+n01)*(n10+n00)))
    if denom == 0:
        return 0.0
    return float(n11*n00 - n10*n01) / denom

def analyze_config(instances):
    all_observed = []
    all_chance = []
    all_excess = []
    phi_values = []
    entity_counts_per_instance = []
    
    for inst in instances:
        samples = inst["samples"]
        if len(samples) < 8:
            continue
        samples = samples[:8]
        
        matrix, ent_list = build_presence_matrix(samples)
        if matrix is None or matrix.shape[1] == 0:
            continue
        
        N, M = matrix.shape
        
        # Pairwise agreement
        obs = pairwise_agreement(matrix)
        if not obs:
            continue
        mean_obs = np.mean(obs)
        
        # Chance agreement
        ch = chance_agreement(matrix)
        
        all_observed.append(mean_obs)
        all_chance.append(ch)
        all_excess.append(mean_obs - ch)
        
        # Phi coefficients between sample pairs for mid-frequency entities
        p = matrix.mean(axis=0)
        mid_freq_mask = (p >= 0.2) & (p <= 0.8)
        mid_freq_indices = np.where(mid_freq_mask)[0]
        
        if len(mid_freq_indices) > 0:
            for ei in mid_freq_indices[:5]:  # up to 5 entities per instance
                for si, sj in combinations(range(N), 2):
                    # phi across entities for this sample pair - not meaningful
                    pass
            # Instead: for each mid-freq entity, compute phi between sample pairs
            # Reinterpret: for pairs of mid-freq entities, compute phi across samples
            if len(mid_freq_indices) >= 2:
                for ei, ej in combinations(mid_freq_indices[:10], 2):
                    phi = phi_coefficient(
                        matrix[:, ei].astype(bool),
                        matrix[:, ej].astype(bool)
                    )
                    phi_values.append(phi)
        
        # Entity count ICC proxy: variance of entity counts across samples
        counts = [len(s["entities"]) for s in samples]
        entity_counts_per_instance.append(counts)
    
    # ICC for entity counts (one-way random model)
    counts_arr = np.array(entity_counts_per_instance, dtype=float)  # n_instances x 8
    n_inst, k = counts_arr.shape
    grand_mean = counts_arr.mean()
    # Between-instance variance
    instance_means = counts_arr.mean(axis=1)
    MSB = k * np.sum((instance_means - grand_mean)**2) / (n_inst - 1)
    # Within-instance variance
    MSW = np.sum((counts_arr - instance_means[:, None])**2) / (n_inst * (k - 1))
    ICC = (MSB - MSW) / (MSB + (k - 1) * MSW) if (MSB + (k - 1) * MSW) > 0 else 0.0
    
    # Split-half correlation
    split_agreements = []
    rng = np.random.RandomState(42)
    for inst in instances:
        samples = inst["samples"]
        if len(samples) < 8:
            continue
        samples = samples[:8]
        perm = rng.permutation(8)
        half1 = [samples[i] for i in perm[:4]]
        half2 = [samples[i] for i in perm[4:]]
        
        # Entity sets for each half (union)
        set1 = set()
        set2 = set()
        for s in half1:
            for e in s["entities"]:
                set1.add(entity_key(e))
        for s in half2:
            for e in s["entities"]:
                set2.add(entity_key(e))
        
        if len(set1) == 0 and len(set2) == 0:
            continue
        union = set1 | set2
        if len(union) == 0:
            continue
        jaccard = len(set1 & set2) / len(union)
        split_agreements.append(jaccard)
    
    mean_obs = float(np.mean(all_observed))
    mean_ch = float(np.mean(all_chance))
    mean_excess = float(np.mean(all_excess))
    
    return {
        "n_valid": len(all_observed),
        "mean_pairwise_agreement": round(mean_obs, 4),
        "expected_chance_agreement": round(mean_ch, 4),
        "excess_agreement": round(mean_excess, 4),
        "excess_relative_pct": round(mean_excess / max(mean_ch, 1e-9) * 100, 1),
        "entity_count_ICC": round(float(ICC), 4),
        "split_half_jaccard": round(float(np.mean(split_agreements)), 4) if split_agreements else None,
        "mean_inter_entity_phi": round(float(np.mean(phi_values)), 4) if phi_values else None,
        "n_phi_pairs": len(phi_values),
    }

def interpret(r):
    excess = r["excess_agreement"]
    excess_pct = r["excess_relative_pct"]
    icc = r["entity_count_ICC"]
    
    if excess < 0.02:
        severity = "minimal"
    elif excess < 0.05:
        severity = "mild"
    elif excess < 0.10:
        severity = "moderate"
    else:
        severity = "substantial"
    
    return (
        f"Independence violation is {severity}. "
        f"Observed agreement exceeds chance by {excess:.4f} ({excess_pct:.1f}% above chance). "
        f"Entity count ICC={icc:.4f} (high ICC = samples correlated in count). "
        f"FK's independence assumption is {'mildly' if severity in ('minimal','mild') else 'notably'} violated, "
        f"but this is expected for temperature sampling sharing model+prompt."
    )

results = {}
for name, path in CONFIGS.items():
    print(f"Processing {name}...")
    if not Path(path).exists():
        print(f"  SKIP: {path} not found")
        results[name] = {"error": f"file not found: {path}"}
        continue
    instances = load_data(path)
    print(f"  {len(instances)} gold-nonempty instances")
    r = analyze_config(instances)
    r["interpretation"] = interpret(r)
    results[name] = r
    print(f"  Done: excess_agreement={r['excess_agreement']}")

out_dir = Path("/root/autodl-tmp/struct_self_consist_ie/output/review_round2")
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "fk_independence_test.json"
with open(out_path, "w") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"\nSaved to {out_path}")
print("\n" + "="*80)
print(json.dumps(results, indent=2, ensure_ascii=False))
print("="*80)

# Summary
print("\n=== SUMMARY ===")
for name, r in results.items():
    if "error" in r:
        print(f"{name}: ERROR - {r['error']}")
        continue
    print(f"\n{name}:")
    print(f"  N={r['n_valid']}, Observed={r['mean_pairwise_agreement']:.4f}, "
          f"Chance={r['expected_chance_agreement']:.4f}, Excess={r['excess_agreement']:.4f} "
          f"({r['excess_relative_pct']:.1f}%)")
    print(f"  ICC={r['entity_count_ICC']:.4f}, Split-half Jaccard={r['split_half_jaccard']}")
    print(f"  {r['interpretation']}")

print("\n=== CONCLUSION ===")
excess_vals = [r["excess_agreement"] for r in results.values() if "error" not in r]
if excess_vals:
    mean_excess = np.mean(excess_vals)
    print(f"Average excess agreement across configs: {mean_excess:.4f}")
    if mean_excess < 0.05:
        print("Temperature sampling shows mild departure from independence. "
              "FK's independence assumption is approximately satisfied — "
              "the shared model/prompt induces some correlation, but the "
              "resulting bias in FK is likely small.")
    else:
        print("Temperature sampling shows notable departure from independence. "
              "FK values may be biased. Consider reporting FK with this caveat "
              "or using alternative metrics that account for rater dependence.")
