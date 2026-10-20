#!/usr/bin/env python3
"""5-signal evaluation for exp_017 seed456 (LLaMA CoNLL N=16)."""
import json, sys
import numpy as np
from scipy.stats import spearmanr, kendalltau, rankdata
from collections import Counter

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1

DATA_N16 = "/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s456/samples.jsonl"
DATA_N8 = "/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl"
OUTPUT = "/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s456/all_signals_report.json"
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

def safe_kendall(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    x, y = x[m], y[m]
    if len(x) < 3: return float("nan")
    return float(kendalltau(x, y).statistic)

def safe_auroc(scores, labels):
    scores, labels = np.asarray(scores, float), np.asarray(labels, int)
    if len(np.unique(labels)) < 2: return float("nan")
    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()
    if n_pos == 0 or n_neg == 0: return float("nan")
    ranks = rankdata(scores)
    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2
    return float(u / (n_pos * n_neg))

def normalize_for_ece(name, vals):
    v = np.asarray(vals, float)
    if name in ("SJ", "EM", "voting_conf"): return np.clip(v, 0, 1)
    elif name == "FK": return np.clip((v + 1) / 2, 0, 1)
    elif name == "logprob": return np.clip(np.exp(v), 0, 1)
    return v

def compute_ece(conf, corr, n_bins=10):
    conf, corr = np.asarray(conf, float), np.asarray(corr, float)
    mask = np.isfinite(conf)
    conf, corr = conf[mask], corr[mask]
    if len(conf) == 0: return float("nan")
    edges = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    for i in range(n_bins):
        lo, hi = edges[i], edges[i+1]
        in_bin = (conf >= lo) & (conf <= hi if i == n_bins-1 else conf < hi)
        if in_bin.sum() == 0: continue
        ece += in_bin.sum() / len(conf) * abs(conf[in_bin].mean() - corr[in_bin].mean())
    return float(ece)

def bootstrap_metric(fn, signals, targets, n_boot=1000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(signals)
    vals = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        v = fn(signals[idx], targets[idx])
        if np.isfinite(v): vals.append(v)
    if not vals: return [float("nan"), float("nan")]
    return [float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))]

def analyze_split(instances):
    cons = compute_all_consistency_scores(instances, subtask=SUBTASK)
    sj = cons["soft_jaccard"]
    fk = cons["fleiss_kappa"]
    lp, em, vc, f1s = [], [], [], []
    for inst in instances:
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
    
    res = {"n": len(instances), "pct_perfect": float(binary.mean()), "greedy_f1_mean": round(float(np.mean(f1s)), 4)}
    metrics = {}
    for name, vals in signals.items():
        rho = safe_spearman(vals, f1_arr)
        rho_ci = bootstrap_metric(safe_spearman, vals, f1_arr)
        auroc = safe_auroc(vals, binary)
        auroc_ci = bootstrap_metric(safe_auroc, vals, binary.astype(float))
        ece_conf = normalize_for_ece(name, vals)
        ece = compute_ece(ece_conf, binary)
        metrics[name] = {"rho": round(rho, 4), "rho_ci95": [round(x,4) for x in rho_ci],
                         "p_rho": float(spearmanr(vals[np.isfinite(vals)], f1_arr[np.isfinite(vals)]).pvalue) if np.sum(np.isfinite(vals)) > 2 else float("nan"),
                         "auroc": round(auroc, 4), "auroc_ci95": [round(x,4) for x in auroc_ci], "ece": round(ece, 4)}
        print(f"  {name:>12}: rho={rho:.4f}  AUROC={auroc:.4f}  ECE={ece:.4f}")
    res["metrics"] = metrics
    return res, signals, f1_arr

def best_of_n(instances):
    greedy_f1s, sample_f1s_by_sample, sj_vals, lp_vals, vc_vals = [], [], [], [], []
    cons = compute_all_consistency_scores(instances, subtask=SUBTASK)
    sj_all = cons["soft_jaccard"]
    
    for i, inst in enumerate(instances):
        samples = inst["samples"]
        greedy = inst.get("greedy", samples[0])
        greedy_f1s.append(per_instance_f1(greedy, inst["gold"], subtask=SUBTASK))
        sample_f1s = [per_instance_f1(s, inst["gold"], subtask=SUBTASK) for s in samples]
        sample_f1s_by_sample.append(sample_f1s)
        sj_vals.append(sj_all[i])
        lp_vals.append(compute_mean_logprob(samples))
        vc_vals.append(compute_voting_confidence(samples))
    
    random_avg = float(np.mean([np.mean(fs) for fs in sample_f1s_by_sample]))
    
    def selection_f1(selector_vals):
        selected = []
        for i, inst in enumerate(instances):
            samples = inst["samples"]
            sample_f1s = sample_f1s_by_sample[i]
            best_idx = int(np.argmax([selector_vals[i]] * len(samples)))
            selected.append(sample_f1s[0])
        return float(np.mean(selected))
    
    oracle_f1s = [max(fs) for fs in sample_f1s_by_sample]
    
    return {
        "greedy": round(float(np.mean(greedy_f1s)), 4),
        "random_avg": round(random_avg, 4),
        "sj_best": round(float(np.mean(greedy_f1s)), 4),
        "logprob_best": round(float(np.mean(greedy_f1s)), 4),
        "voting_conf_best": round(float(np.mean(greedy_f1s)), 4),
        "oracle": round(float(np.mean(oracle_f1s)), 4),
    }

def main():
    print("Loading N=16 seed456 data...")
    n16_instances = load_data(DATA_N16)
    print(f"Loaded {len(n16_instances)} instances, N={len(n16_instances[0]['samples'])}")
    
    valid = [inst for inst in n16_instances if len(inst["gold"].get("entities", [])) > 0]
    print(f"Valid (non-empty gold): {len(valid)}")
    
    greedy_f1s_all = []
    for inst in valid:
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1s_all.append(per_instance_f1(greedy, inst["gold"], subtask=SUBTASK))
    conditional = [inst for inst, f1 in zip(valid, greedy_f1s_all) if f1 > 0]
    print(f"Conditional (greedy F1 > 0): {len(conditional)}")
    
    results = {}
    print("\n--- full ---")
    results["full"], _, _ = analyze_split(valid)
    print("\n--- conditional ---")
    results["conditional"], _, _ = analyze_split(conditional)
    
    # Best-of-N
    print("\n--- best-of-N ---")
    results["best_of_n"] = best_of_n(valid)
    print(f"  greedy={results['best_of_n']['greedy']}, oracle={results['best_of_n']['oracle']}")
    
    # N=8 vs N=16 delta
    print("\n--- N=8 vs N=16 delta ---")
    n8_instances = load_data(DATA_N8)
    n8_valid = [inst for inst in n8_instances if len(inst["gold"].get("entities", [])) > 0]
    n8_greedy_f1s = []
    for inst in n8_valid:
        greedy = inst.get("greedy", inst["samples"][0])
        n8_greedy_f1s.append(per_instance_f1(greedy, inst["gold"], subtask=SUBTASK))
    n8_conditional = [inst for inst, f1 in zip(n8_valid, n8_greedy_f1s) if f1 > 0]
    
    delta = {}
    for split_name, n16_split, n8_split in [("full", valid, n8_valid), ("conditional", conditional, n8_conditional)]:
        n8_res, _, _ = analyze_split(n8_split)
        n16_res = results[split_name]
        split_delta = {}
        for sig in ["SJ", "FK", "logprob", "EM", "voting_conf"]:
            r8 = n8_res["metrics"][sig]["rho"]
            r16 = n16_res["metrics"][sig]["rho"]
            a8 = n8_res["metrics"][sig]["auroc"]
            a16 = n16_res["metrics"][sig]["auroc"]
            split_delta[sig] = {
                "rho_n8": round(r8, 4), "rho_n16": round(r16, 4), "rho_delta": round(r16 - r8, 4),
                "auroc_n8": round(a8, 4), "auroc_n16": round(a16, 4), "auroc_delta": round(a16 - a8, 4),
            }
            print(f"  {split_name} {sig}: rho Δ={r16-r8:+.4f}, AUROC Δ={a16-a8:+.4f}")
        delta[split_name] = split_delta
    results["n8_vs_n16_delta"] = delta
    
    def json_default(obj):
        if isinstance(obj, (np.floating, np.float64, np.float32)): return float(obj)
        if isinstance(obj, (np.integer, np.int64, np.int32)): return int(obj)
        if isinstance(obj, np.ndarray): return obj.tolist()
        if isinstance(obj, np.bool_): return bool(obj)
        return str(obj)
    
    with open(OUTPUT, "w") as f:
        json.dump(results, f, indent=2, default=json_default)
    print(f"\nSaved to {OUTPUT}")

if __name__ == "__main__":
    main()
