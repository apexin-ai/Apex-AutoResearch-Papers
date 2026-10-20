#!/usr/bin/env python3
import json
import sys
from collections import defaultdict
import numpy as np

B = 10000
SEED = 42

def compute_entity_f1(pred_entities, gold_entities):
    pred = {(e["start"], e["end"], e["type"]) for e in pred_entities}
    gold = {(e["start"], e["end"], e["type"]) for e in gold_entities}
    if not gold and not pred: return 1.0
    if not gold or not pred: return 0.0
    tp = len(pred & gold)
    if tp == 0: return 0.0
    p = tp / len(pred)
    r = tp / len(gold)
    return 2 * p * r / (p + r)

def compute_vc(samples):
    N = len(samples)
    entity_sets = []
    for s in samples:
        es = frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
        entity_sets.append(es)
    return [sum(1 for j in range(N) if entity_sets[j] == entity_sets[i]) / N for i in range(N)]

def vc_weighted_construct(inst, threshold):
    samples = inst["samples"]
    vc = compute_vc(samples)
    total_vc = sum(vc)
    entity_vc_vote = defaultdict(float)
    for i, s in enumerate(samples):
        seen = set()
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_vc_vote[key] += vc[i]
                seen.add(key)
    consensus = []
    for entity_key, vote in entity_vc_vote.items():
        normalized = vote / total_vc if total_vc > 0 else 0
        if normalized > threshold:
            consensus.append(entity_key)
    return [{"start": s, "end": e, "type": t} for s, e, t in consensus]

def is_degenerate(inst):
    key_sets = set()
    for s in inst["samples"]:
        ks = frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
        key_sets.add(ks)
    return len(key_sets) == 1

def load_data(path, gold_filter=True):
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip(): continue
            obj = json.loads(line)
            if gold_filter and not obj["gold"].get("entities", []): continue
            instances.append(obj)
    return instances

def run_bootstrap(greedy_f1s, vc_f1s, degen_flags, label=""):
    rng = np.random.RandomState(SEED)
    greedy_arr = np.array(greedy_f1s)
    vc_arr = np.array(vc_f1s)
    degen_arr = np.array(degen_flags, dtype=bool)
    n = len(greedy_arr)
    diffs = vc_arr - greedy_arr
    obs_diff = float(diffs.mean())
    boot = np.zeros(B)
    for b in range(B):
        idx = rng.randint(0, n, n)
        boot[b] = diffs[idx].mean()
    boot.sort()
    ci_lo = float(boot[int(0.025 * B)])
    ci_hi = float(boot[int(0.975 * B)])
    p_value = float(np.mean(boot <= 0))
    std_diff = diffs.std()
    cohens_d = float(obs_diff / std_diff) if std_diff > 0 else 0.0
    n_positive = int(np.sum(diffs > 0))
    n_negative = int(np.sum(diffs < 0))
    n_tied = int(np.sum(diffs == 0))
    n_degen = int(degen_arr.sum())
    n_nondegen = n - n_degen
    result = {
        "label": label, "n_instances": n,
        "greedy_f1": float(greedy_arr.mean()),
        "vc_constructed_f1": float(vc_arr.mean()),
        "delta_f1_pp": obs_diff * 100,
        "bootstrap_p": p_value,
        "ci_95": [ci_lo, ci_hi],
        "cohens_d": cohens_d,
        "instance_positive": n_positive,
        "instance_negative": n_negative,
        "instance_tied": n_tied,
        "n_degenerate": n_degen,
        "n_nondegenerate": n_nondegen,
        "mean_degeneracy": n_degen / n if n > 0 else 0,
    }
    if n_nondegen > 0:
        nd_mask = ~degen_arr
        nd_greedy = float(greedy_arr[nd_mask].mean())
        nd_vc = float(vc_arr[nd_mask].mean())
        nd_diffs = diffs[nd_mask]
        nd_n = nd_diffs.shape[0]
        nd_boot = np.zeros(B)
        for b in range(B):
            idx = rng.randint(0, nd_n, nd_n)
            nd_boot[b] = nd_diffs[idx].mean()
        nd_boot.sort()
        nd_ci_lo = float(nd_boot[int(0.025 * B)])
        nd_ci_hi = float(nd_boot[int(0.975 * B)])
        nd_p = float(np.mean(nd_boot <= 0))
        result["nondegen_greedy_f1"] = nd_greedy
        result["nondegen_vc_f1"] = nd_vc
        result["nondegen_diff_pp"] = (nd_vc - nd_greedy) * 100
        result["nondegen_ci_95"] = [nd_ci_lo, nd_ci_hi]
        result["nondegen_p"] = nd_p
    return result

def process_config(config):
    path = config["path"]
    config_name = config["config"]
    expected_greedy = config.get("expected_greedy")
    instances = load_data(path, gold_filter=True)
    if not instances:
        return {"config": config_name, "error": "No instances after gold filtering"}
    N = len(instances[0]["samples"])
    if N != 8:
        return {"config": config_name, "error": f"N={N}, expected 8"}
    theta = 2 / N
    greedy_f1s, vc_f1s, degen_flags = [], [], []
    for inst in instances:
        gold_ents = inst["gold"]["entities"]
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1s.append(compute_entity_f1(greedy.get("entities", []), gold_ents))
        vc_ents = vc_weighted_construct(inst, threshold=theta)
        vc_f1s.append(compute_entity_f1(vc_ents, gold_ents))
        degen_flags.append(is_degenerate(inst))
    computed_greedy = float(np.mean(greedy_f1s))
    greedy_verified = True
    if expected_greedy is not None:
        if abs(computed_greedy - expected_greedy) > 0.01:
            return {"config": config_name, "error": f"M030 FAIL: computed={computed_greedy:.4f}, expected={expected_greedy:.4f}"}
    result = run_bootstrap(greedy_f1s, vc_f1s, degen_flags, label=config_name)
    result["config"] = config_name
    result["greedy_f1_verified"] = greedy_verified
    result["n_instances"] = len(instances)
    result["threshold"] = theta
    return result

def main():
    configs = json.loads(sys.stdin.read())
    results = []
    for cfg in configs:
        print(f"Processing {cfg['config']}...", file=sys.stderr)
        r = process_config(cfg)
        results.append(r)
        if "error" in r:
            print(f"  ERROR: {r['error']}", file=sys.stderr)
        else:
            print(f"  greedy={r['greedy_f1']:.4f} vc={r['vc_constructed_f1']:.4f} delta={r['delta_f1_pp']:+.2f}pp p={r['bootstrap_p']:.4f}", file=sys.stderr)
    json.dump(results, sys.stdout, indent=2)
    print(file=sys.stdout)

if __name__ == "__main__":
    main()
