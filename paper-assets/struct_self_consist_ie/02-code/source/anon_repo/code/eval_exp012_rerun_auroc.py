#!/usr/bin/env python3
"""Compute 5-signal AUROC for exp_012_rerun_1024 (joint NER+RE)."""
import json, sys
import numpy as np
from scipy.stats import spearmanr, rankdata
from collections import Counter

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl"

def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]

def compute_exact_match_rate(samples, subtask):
    if subtask == "ner":
        keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    else:
        keys = [frozenset((r["head"], r["tail"], r["type"]) for r in s.get("relations", [])) for s in samples]
    if not keys: return 0.0
    c = Counter(keys)
    return c.most_common(1)[0][1] / len(samples)

def compute_voting_confidence(samples, subtask):
    N = len(samples)
    if N == 0: return 0.0
    counter = Counter()
    if subtask == "ner":
        for s in samples:
            for e in s.get("entities", []):
                counter[(e["text"], e["type"])] += 1
    else:
        for s in samples:
            for r in s.get("relations", []):
                counter[(r["head"], r["tail"], r["type"])] += 1
    if not counter: return 0.0
    return float(np.mean([v / N for v in counter.values()]))

def compute_mean_logprob(samples):
    lps = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    lps = [lp for lp in lps if np.isfinite(lp)]
    return float(np.mean(lps)) if lps else float("nan")

def safe_auroc(scores, labels):
    scores, labels = np.asarray(scores, float), np.asarray(labels, int)
    mask = np.isfinite(scores)
    scores, labels = scores[mask], labels[mask]
    if len(np.unique(labels)) < 2: return float("nan")
    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()
    if n_pos == 0 or n_neg == 0: return float("nan")
    ranks = rankdata(scores)
    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2
    return float(u / (n_pos * n_neg))

def analyze(instances, subtask):
    entity_key = "entities" if subtask == "ner" else "relations"
    valid = [inst for inst in instances if len(inst["gold"].get(entity_key, [])) > 0]

    greedy_f1s = []
    for inst in valid:
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1s.append(per_instance_f1(greedy, inst["gold"], subtask=subtask))
    
    conditional_pairs = [(inst, f1) for inst, f1 in zip(valid, greedy_f1s) if f1 > 0]
    conditional_insts = [p[0] for p in conditional_pairs]
    conditional_f1s = [p[1] for p in conditional_pairs]

    results = {"n_total": len(instances), "n_valid": len(valid), "n_conditional": len(conditional_insts)}

    for split_name, split_insts, split_f1s in [
        ("full", valid, greedy_f1s),
        ("cond", conditional_insts, conditional_f1s),
    ]:
        cons = compute_all_consistency_scores(split_insts, subtask=subtask)
        sj = cons["soft_jaccard"]
        fk = cons["fleiss_kappa"]

        lp, em, vc = [], [], []
        for inst in split_insts:
            samples = inst["samples"]
            lp.append(compute_mean_logprob(samples))
            em.append(compute_exact_match_rate(samples, subtask))
            vc.append(compute_voting_confidence(samples, subtask))

        signals = {"sj": np.array(sj), "fk": np.array(fk), "logprob": np.array(lp),
                    "em": np.array(em), "voting_conf": np.array(vc)}
        f1_arr = np.array(split_f1s)
        binary = (f1_arr >= 1.0).astype(int)

        split_res = {"n": len(split_insts), "n_pos": int(binary.sum()), "n_neg": int((1-binary).sum())}
        for name, vals in signals.items():
            auroc = safe_auroc(vals, binary)
            split_res[f"auroc_{name}"] = round(auroc, 6) if np.isfinite(auroc) else None
        results[split_name] = split_res
    return results

instances = load_data(DATA_PATH)
print(f"Loaded {len(instances)} instances")

all_results = {}
for subtask in ["ner", "re"]:
    print(f"\nProcessing {subtask}...")
    all_results[subtask] = analyze(instances, subtask)
    r = all_results[subtask]
    print(f"  n_valid={r['n_valid']}, n_conditional={r['n_conditional']}")
    for split in ["full", "cond"]:
        sr = r[split]
        print(f"  {split} (n={sr['n']}, pos={sr['n_pos']}, neg={sr['n_neg']}):")
        for sig in ["sj", "fk", "em", "voting_conf", "logprob"]:
            print(f"    {sig}: {sr[f'auroc_{sig}']}")

out_path = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/auroc_5signal.json"
with open(out_path, "w") as f:
    json.dump(all_results, f, indent=2)
print(f"\nSaved to {out_path}")
