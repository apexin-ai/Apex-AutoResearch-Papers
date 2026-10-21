#!/usr/bin/env python3
"""Compute 5-signal metrics for 3 seeds (NER N=16)."""
import json, sys
import numpy as np
from scipy.stats import spearmanr, rankdata
from collections import Counter

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1

SEEDS = {
    "seed42": "/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl",
    "seed123": "/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2/samples.jsonl",
    "seed456": "/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed456_v2_ner/samples.jsonl",
}
SUBTASK = "ner"

def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]

def compute_exact_match_rate(samples):
    keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    if not keys: return 0.0
    c = Counter(keys)
    return c.most_common(1)[0][1] / len(samples)

def compute_voting_confidence(samples):
    N = len(samples)
    if N == 0: return 0.0
    counter = Counter()
    for s in samples:
        for e in s.get("entities", []):
            counter[(e["text"], e["type"])] += 1
    if not counter: return 0.0
    return float(np.mean([v / N for v in counter.values()]))

def compute_mean_logprob(samples):
    lps = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    lps = [lp for lp in lps if np.isfinite(lp)]
    return float(np.mean(lps)) if lps else float("nan")

def safe_spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    x, y = x[m], y[m]
    if len(x) < 3: return float("nan")
    return float(spearmanr(x, y).statistic)

def safe_auroc(scores, labels):
    scores, labels = np.asarray(scores, float), np.asarray(labels, int)
    if len(np.unique(labels)) < 2: return float("nan")
    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()
    if n_pos == 0 or n_neg == 0: return float("nan")
    ranks = rankdata(scores)
    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2
    return float(u / (n_pos * n_neg))

def analyze_seed(path):
    instances = load_data(path)
    valid = [inst for inst in instances if len(inst["gold"].get("entities", [])) > 0]
    
    greedy_f1s = []
    for inst in valid:
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1s.append(per_instance_f1(greedy, inst["gold"], subtask=SUBTASK))
    conditional = [inst for inst, f1 in zip(valid, greedy_f1s) if f1 > 0]
    
    results = {}
    for split_name, split_insts in [("full", valid), ("conditional", conditional)]:
        cons = compute_all_consistency_scores(split_insts, subtask=SUBTASK)
        sj = cons["soft_jaccard"]
        fk = cons["fleiss_kappa"]
        
        lp, em, vc, f1s = [], [], [], []
        for inst in split_insts:
            samples = inst["samples"]
            greedy = inst.get("greedy", samples[0])
            lp.append(compute_mean_logprob(samples))
            em.append(compute_exact_match_rate(samples))
            vc.append(compute_voting_confidence(samples))
            f1s.append(per_instance_f1(greedy, inst["gold"], subtask=SUBTASK))
        
        signals = {"SJ": np.array(sj), "FK": np.array(fk), "logprob": np.array(lp),
                    "EM": np.array(em), "voting_conf": np.array(vc)}
        f1_arr = np.array(f1s)
        binary = (f1_arr >= 1.0).astype(int)
        
        split_res = {"n": len(split_insts)}
        for name, vals in signals.items():
            split_res[name] = {
                "rho": safe_spearman(vals, f1_arr),
                "auroc": safe_auroc(vals, binary),
            }
        results[split_name] = split_res
    return results

all_results = {}
for seed_name, path in SEEDS.items():
    print(f"Processing {seed_name}...")
    all_results[seed_name] = analyze_seed(path)

print(json.dumps(all_results, indent=2, default=lambda o: float(o) if isinstance(o, (np.floating,)) else str(o)))
