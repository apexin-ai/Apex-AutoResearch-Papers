#!/usr/bin/env python3
"""5-signal evaluation for exp_018 seed42 r1024 (LLaMA SciERC joint)."""
import json, sys
import numpy as np
from scipy.stats import spearmanr, kendalltau, rankdata
from collections import Counter

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1

DATA = "/root/autodl-tmp/struct_self_consist_ie/output/exp_018_llama_scierc_seed42_r1024/samples.jsonl"
OUTPUT = "/root/autodl-tmp/struct_self_consist_ie/output/exp_018_llama_scierc_seed42_r1024/all_signals_report.json"

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

def safe_kendall(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    x, y = x[m], y[m]
    if len(x) < 3: return float("nan"), float("nan")
    r = kendalltau(x, y)
    return float(r.statistic), float(r.pvalue)

def safe_auroc(scores, labels):
    scores, labels = np.asarray(scores, float), np.asarray(labels, int)
    if len(np.unique(labels)) < 2: return float("nan")
    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()
    if n_pos == 0 or n_neg == 0: return float("nan")
    ranks = rankdata(scores)
    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2
    return float(u / (n_pos * n_neg))

def analyze_split(instances, subtask):
    cons = compute_all_consistency_scores(instances, subtask=subtask)
    sj = cons["soft_jaccard"]
    fk = cons["fleiss_kappa"]
    lp, em, vc, f1s = [], [], [], []
    for inst in instances:
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
    
    res = {"n": len(instances), "pct_perfect": round(float(binary.mean()), 4),
           "greedy_f1_mean": round(float(np.mean(f1s)), 4)}
    metrics = {}
    for name, vals in signals.items():
        rho, p_rho = safe_spearman(vals, f1_arr)
        tau, p_tau = safe_kendall(vals, f1_arr)
        auroc = safe_auroc(vals, binary)
        metrics[name] = {
            "rho": round(rho, 4), "p_rho": p_rho,
            "tau": round(tau, 4), "p_tau": p_tau,
            "auroc": round(auroc, 4),
        }
    res["metrics"] = metrics
    return res

def main():
    instances = load_data(DATA)
    print(f"Loaded {len(instances)} instances, N={len(instances[0]['samples'])}")
    
    results = {}
    for subtask in ["ner", "re"]:
        valid = [inst for inst in instances if len(inst["gold"].get(
            "entities" if subtask == "ner" else "relations", [])) > 0]
        greedy_f1s = []
        for inst in valid:
            greedy = inst.get("greedy", inst["samples"][0])
            greedy_f1s.append(per_instance_f1(greedy, inst["gold"], subtask=subtask))
        conditional = [inst for inst, f1 in zip(valid, greedy_f1s) if f1 > 0]
        
        print(f"\n=== {subtask.upper()} ===")
        print(f"Valid: {len(valid)}, Conditional: {len(conditional)}")
        
        full_res = analyze_split(valid, subtask)
        cond_res = analyze_split(conditional, subtask)
        
        print(f"\n{'Signal':<15} {'ρ_full':>8} {'ρ_cond':>8} {'τ_full':>8} {'AUROC_f':>8} {'AUROC_c':>8}")
        print("-" * 65)
        for sig in ["SJ", "FK", "logprob", "EM", "voting_conf"]:
            fm = full_res["metrics"][sig]
            cm = cond_res["metrics"][sig]
            print(f"{sig:<15} {fm['rho']:+.4f} {cm['rho']:+.4f} {fm['tau']:+.4f} {fm['auroc']:.4f} {cm['auroc']:.4f}")
        
        results[subtask] = {"full": full_res, "conditional": cond_res}
    
    def json_default(obj):
        if isinstance(obj, (np.floating,)): return float(obj)
        if isinstance(obj, (np.integer,)): return int(obj)
        if isinstance(obj, np.ndarray): return obj.tolist()
        return str(obj)
    
    with open(OUTPUT, "w") as f:
        json.dump(results, f, indent=2, default=json_default)
    print(f"\nSaved to {OUTPUT}")

if __name__ == "__main__":
    main()
