import json
import math
from collections import defaultdict

THETA = 0.25

DATASETS = {
    "fewnerd_5epoch": "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_5epoch_lp_seed42/samples.jsonl",
    "fewnerd_3epoch_mf4v2": "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_mf4v2_seed42/samples.jsonl",
    "fewnerd_3epoch_exp021": "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl",
}

def load_data(path):
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if not obj["gold"].get("entities", []):
                continue
            instances.append(obj)
    return instances

def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}

def get_lp_weights(inst):
    samples = inst["samples"]
    logprobs = inst.get("logprobs", None)
    lps = []
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob", None)
        if lp is None and logprobs is not None and i < len(logprobs):
            lp = logprobs[i]
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

def compute_micro(pred_sets, gold_sets):
    tp_total, fp_total, fn_total = 0, 0, 0
    for pred, gold in zip(pred_sets, gold_sets):
        tp = len(pred & gold)
        fp = len(pred - gold)
        fn = len(gold - pred)
        tp_total += tp
        fp_total += fp
        fn_total += fn
    if tp_total == 0:
        return 0.0, 0.0, 0.0
    p = tp_total / (tp_total + fp_total)
    r = tp_total / (tp_total + fn_total)
    f = 2 * p * r / (p + r)
    return p, r, f

def evaluate(path, name):
    import os
    if not os.path.exists(path):
        print(f"SKIP {name}: {path} not found")
        return None

    data = load_data(path)
    N_inst = len(data)

    gold_sets = []
    greedy_sets = []
    uniform_sets = []
    lp_sets = []
    degen_count = 0

    for inst in data:
        gold = entity_set(inst["gold"]["entities"])
        gold_sets.append(gold)

        greedy_ents = inst.get("greedy", inst["samples"][0])
        greedy_sets.append(entity_set(greedy_ents.get("entities", [])))

        samples = inst["samples"]
        N = len(samples)

        # Degeneracy: all samples produce identical entity set
        sample_ent_sets = [frozenset(entity_set(s.get("entities", []))) for s in samples]
        if len(set(sample_ent_sets)) == 1:
            degen_count += 1

        # Uniform construction
        uniform = entity_majority_vote(samples, THETA)
        uniform_sets.append(uniform)

        # LP-weighted construction
        weights = get_lp_weights(inst)
        lp = entity_majority_vote(samples, THETA, weights=weights)
        lp_sets.append(lp)

    gp, gr, gf = compute_micro(greedy_sets, gold_sets)
    up, ur, uf = compute_micro(uniform_sets, gold_sets)
    lpp, lpr, lpf = compute_micro(lp_sets, gold_sets)

    degen_rate = degen_count / N_inst * 100

    print(f"\n{'='*60}")
    print(f"{name} Entity Construction (N=8, T=1.0, θ={THETA}, seed=42)")
    print(f"{'='*60}")
    print(f"  n_instances: {N_inst} (gold-nonempty subset)")
    print(f"  greedy_f1:                    {gf:.6f}  (P={gp:.6f}, R={gr:.6f})")
    print(f"  uniform_construction_f1:      {uf:.6f}  (P={up:.6f}, R={ur:.6f})")
    print(f"  lp_weighted_construction_f1:  {lpf:.6f}  (P={lpp:.6f}, R={lpr:.6f})")
    print(f"  Δ_uniform_construction:       {(uf-gf)*100:+.2f} pp")
    print(f"  Δ_lp_construction:            {(lpf-gf)*100:+.2f} pp")
    print(f"  degeneracy_rate:              {degen_rate:.1f}%  ({degen_count}/{N_inst})")

    return {"greedy_f1": gf, "uniform_f1": uf, "lp_f1": lpf,
            "delta_uniform": (uf-gf)*100, "delta_lp": (lpf-gf)*100,
            "degen_rate": degen_rate, "n_instances": N_inst}

if __name__ == "__main__":
    results = {}
    for name, path in DATASETS.items():
        r = evaluate(path, name)
        if r:
            results[name] = r

    if "fewnerd_3epoch_exp021" in results:
        r3 = results["fewnerd_3epoch_exp021"]
        print(f"\n3-epoch cross-validation (exp021):")
        print(f"  greedy_f1: {r3['greedy_f1']:.6f} (expect ~0.7911)")
        print(f"  lp_construction_f1: {r3['lp_f1']:.6f} (expect ~0.8051)")
        print(f"  Δ_lp: {r3['delta_lp']:+.2f} pp (expect ~+1.40pp)")
