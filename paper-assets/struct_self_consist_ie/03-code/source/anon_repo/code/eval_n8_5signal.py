#!/usr/bin/env python3
"""5-signal evaluation for N=8 experiments (baseline for N=8 vs N=16 comparison)."""
import json, sys
import numpy as np
from scipy.stats import spearmanr, rankdata
from collections import Counter

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1

EXPERIMENTS = {
    "exp_002_conll_n8": {
        "path": "/root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003/samples.jsonl",
        "subtask": "ner",
        "dataset": "conll2003",
    },
    "exp_007_llama_n8": {
        "path": "/root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference/samples.jsonl",
        "subtask": "ner",
        "dataset": "scierc",
    },
}

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

def safe_spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    x, y = x[m], y[m]
    if len(x) < 3: return float("nan"), float("nan")
    r = spearmanr(x, y)
    return float(r.statistic), float(r.pvalue)

def safe_auroc(scores, labels):
    scores, labels = np.asarray(scores, float), np.asarray(labels, int)
    if len(np.unique(labels)) < 2: return float("nan")
    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()
    if n_pos == 0 or n_neg == 0: return float("nan")
    ranks = rankdata(scores)
    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2
    return float(u / (n_pos * n_neg))

def compute_ece(scores, labels, n_bins=10):
    scores, labels = np.asarray(scores, float), np.asarray(labels, float)
    mask = np.isfinite(scores)
    scores, labels = scores[mask], labels[mask]
    if len(scores) == 0: return float("nan")
    s_min, s_max = scores.min(), scores.max()
    if s_max == s_min: return float("nan")
    norm = (scores - s_min) / (s_max - s_min)
    ece = 0.0
    for i in range(n_bins):
        lo, hi = i / n_bins, (i + 1) / n_bins
        mask_bin = (norm >= lo) & (norm < hi) if i < n_bins - 1 else (norm >= lo) & (norm <= hi)
        if mask_bin.sum() == 0: continue
        avg_conf = norm[mask_bin].mean()
        avg_acc = labels[mask_bin].mean()
        ece += mask_bin.sum() / len(norm) * abs(avg_conf - avg_acc)
    return float(ece)

def analyze(path, subtask):
    instances = load_data(path)
    entity_key = "entities" if subtask == "ner" else "relations"
    valid = [inst for inst in instances if len(inst["gold"].get(entity_key, [])) > 0]

    greedy_f1s = []
    for inst in valid:
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1s.append(per_instance_f1(greedy, inst["gold"], subtask=subtask))
    conditional = [inst for inst, f1 in zip(valid, greedy_f1s) if f1 > 0]

    results = {"n_total": len(instances), "n_valid": len(valid), "n_conditional": len(conditional)}
    
    for split_name, split_insts in [("full", valid), ("conditional", conditional)]:
        cons = compute_all_consistency_scores(split_insts, subtask=subtask)
        sj = cons["soft_jaccard"]
        fk = cons["fleiss_kappa"]
        
        lp, em, vc, f1s = [], [], [], []
        for inst in split_insts:
            samples = inst["samples"]
            greedy = inst.get("greedy", samples[0])
            lp.append(compute_mean_logprob(samples))
            em.append(compute_exact_match_rate(samples, subtask))
            vc.append(compute_voting_confidence(samples, subtask))
            f1s.append(per_instance_f1(greedy, inst["gold"], subtask=subtask))
        
        signals = {"SJ": np.array(sj), "FK": np.array(fk), "logprob": np.array(lp),
                    "EM": np.array(em), "voting_conf": np.array(vc)}
        f1_arr = np.array(f1s)
        binary = (f1_arr >= 1.0).astype(int)
        
        split_res = {"n": len(split_insts)}
        for name, vals in signals.items():
            rho, p_rho = safe_spearman(vals, f1_arr)
            auroc = safe_auroc(vals, binary)
            ece = compute_ece(vals, f1_arr)
            split_res[name] = {"rho": round(rho, 4), "p_rho": p_rho, "auroc": round(auroc, 4), "ece": round(ece, 4)}
        
        split_res["greedy_f1_mean"] = round(float(np.mean(f1s)), 4)
        results[split_name] = split_res
    return results

all_results = {}
for exp_id, cfg in EXPERIMENTS.items():
    print(f"Processing {exp_id} ({cfg['dataset']})...")
    all_results[exp_id] = analyze(cfg["path"], cfg["subtask"])
    all_results[exp_id]["dataset"] = cfg["dataset"]

out_path = "/root/autodl-tmp/struct_self_consist_ie/output/n8_5signal_results.json"
with open(out_path, "w") as f:
    json.dump(all_results, f, indent=2, default=lambda o: float(o) if isinstance(o, (np.floating,)) else str(o))
print(f"\nSaved to {out_path}")
print(json.dumps(all_results, indent=2, default=lambda o: float(o) if isinstance(o, (np.floating,)) else str(o)))
