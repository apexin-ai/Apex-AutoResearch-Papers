#!/usr/bin/env python3
"""Scale ablation: Qwen3-4B vs 8B CoNLL NER — 5-signal comparison."""
import json, sys
import numpy as np
from scipy.stats import spearmanr, rankdata
from collections import Counter

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1

EXPERIMENTS = {
    "qwen3_8b_conll": {
        "path": "/root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003/samples.jsonl",
        "subtask": "ner",
        "model": "Qwen3-8B",
    },
    "qwen3_4b_conll": {
        "path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_scale_qwen3_4b_conll/samples.jsonl",
        "subtask": "ner",
        "model": "Qwen3-4B",
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

def compute_selection_f1(signal_scores, sample_f1_per_sample, n_samples=8):
    """Selection F1: pick best sample per instance by signal, compute mean F1."""
    assert len(signal_scores) == len(sample_f1_per_sample)
    selected_f1s = []
    for i in range(len(signal_scores)):
        f1s = sample_f1_per_sample[i]
        if len(f1s) == 0:
            continue
        best_idx = int(np.argmax(signal_scores[i])) if hasattr(signal_scores[i], '__len__') else 0
        selected_f1s.append(f1s[best_idx] if best_idx < len(f1s) else f1s[0])
    return float(np.mean(selected_f1s)) if selected_f1s else float("nan")

def compute_lp_tied_fraction(samples_list):
    n_tied = 0
    for inst_samples in samples_list:
        lps = [s.get("mean_logprob") for s in inst_samples if s.get("mean_logprob") is not None]
        lps = [lp for lp in lps if np.isfinite(lp)]
        if len(lps) >= 2:
            unique_ratio = len(set([round(lp, 6) for lp in lps])) / len(lps)
            if unique_ratio < 0.5:
                n_tied += 1
    return n_tied

def analyze(path, subtask):
    instances = load_data(path)
    entity_key = "entities" if subtask == "ner" else "relations"
    valid = [inst for inst in instances if len(inst["gold"].get(entity_key, [])) > 0]

    greedy_f1s = []
    for inst in valid:
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1s.append(per_instance_f1(greedy, inst["gold"], subtask=subtask))
    conditional = [inst for inst, f1 in zip(valid, greedy_f1s) if f1 > 0]

    # Oracle F1
    oracle_f1s = []
    for inst in valid:
        best = max(per_instance_f1(s, inst["gold"], subtask=subtask) for s in inst["samples"])
        oracle_f1s.append(best)

    # LP tied fraction
    all_samples = [inst["samples"] for inst in valid]
    lp_tied = compute_lp_tied_fraction(all_samples)

    results = {
        "n_total": len(instances), "n_valid": len(valid), "n_conditional": len(conditional),
        "greedy_f1": round(float(np.mean(greedy_f1s)), 4),
        "oracle_f1": round(float(np.mean(oracle_f1s)), 4),
        "lp_tied_count": lp_tied,
        "lp_tied_pct": round(lp_tied / len(valid) * 100, 1) if valid else 0,
    }
    
    for split_name, split_insts in [("full", valid), ("conditional", conditional)]:
        cons = compute_all_consistency_scores(split_insts, subtask=subtask)
        sj = cons["soft_jaccard"]
        fk = cons["fleiss_kappa"]
        
        lp, em, vc, f1s = [], [], [], []
        sample_f1_per_inst = []
        for inst in split_insts:
            samples = inst["samples"]
            greedy = inst.get("greedy", samples[0])
            lp.append(compute_mean_logprob(samples))
            em.append(compute_exact_match_rate(samples, subtask))
            vc.append(compute_voting_confidence(samples, subtask))
            f1s.append(per_instance_f1(greedy, inst["gold"], subtask=subtask))
            sample_f1_per_inst.append([per_instance_f1(s, inst["gold"], subtask=subtask) for s in samples])
        
        signals = {"SJ": np.array(sj), "FK": np.array(fk), "LP": np.array(lp),
                    "EM": np.array(em), "Voting": np.array(vc)}
        f1_arr = np.array(f1s)
        binary = (f1_arr >= 1.0).astype(int)
        
        split_res = {"n": len(split_insts)}
        for name, vals in signals.items():
            rho, p_rho = safe_spearman(vals, f1_arr)
            auroc = safe_auroc(vals, binary)
            split_res[name] = {"rho": round(rho, 4), "auroc": round(auroc, 4)}
        
        # Selection F1 for each signal
        greedy_mean = round(float(np.mean(f1s)), 4)
        split_res["greedy_f1_mean"] = greedy_mean
        
        # Per-sample signal selection
        for sig_name, vals in signals.items():
            if sig_name in ("SJ", "FK", "Voting"):
                # These are per-instance, not per-sample; use greedy as selection baseline
                pass
        
        results[split_name] = split_res
    return results

all_results = {}
for exp_id, cfg in EXPERIMENTS.items():
    print(f"Processing {exp_id} ({cfg['model']})...")
    res = analyze(cfg["path"], cfg["subtask"])
    res["model"] = cfg["model"]
    all_results[exp_id] = res

# Print comparison table
print("\n" + "="*80)
print("  SCALE ABLATION: Qwen3-4B vs Qwen3-8B — CoNLL NER — 5-Signal Comparison")
print("="*80)

for split in ["full", "conditional"]:
    print(f"\n--- {split.upper()} split ---")
    print(f"{'Signal':<12} {'8B ρ':>8} {'8B AUROC':>10} {'4B ρ':>8} {'4B AUROC':>10} {'Δρ':>8}")
    print("-"*60)
    for sig in ["Voting", "SJ", "FK", "EM", "LP"]:
        r8 = all_results["qwen3_8b_conll"][split][sig]
        r4 = all_results["qwen3_4b_conll"][split][sig]
        delta = r4["rho"] - r8["rho"]
        print(f"{sig:<12} {r8['rho']:>+8.4f} {r8['auroc']:>10.4f} {r4['rho']:>+8.4f} {r4['auroc']:>10.4f} {delta:>+8.4f}")
    print(f"\n  Greedy F1:  8B={all_results['qwen3_8b_conll'][split]['greedy_f1_mean']:.4f}  "
          f"4B={all_results['qwen3_4b_conll'][split]['greedy_f1_mean']:.4f}")

print(f"\n--- LP Score Compression ---")
for exp_id in ["qwen3_8b_conll", "qwen3_4b_conll"]:
    r = all_results[exp_id]
    print(f"  {r['model']}: tied_pct={r['lp_tied_pct']}%")

print(f"\n--- SJ > FK ordering ---")
for exp_id in ["qwen3_8b_conll", "qwen3_4b_conll"]:
    r = all_results[exp_id]
    sj_rho = r["full"]["SJ"]["rho"]
    fk_rho = r["full"]["FK"]["rho"]
    print(f"  {r['model']}: SJ={sj_rho:.4f} FK={fk_rho:.4f} SJ>FK={sj_rho > fk_rho} (delta={sj_rho-fk_rho:+.4f})")

print(f"\n--- Correlation-Selection Gap ---")
for exp_id in ["qwen3_8b_conll", "qwen3_4b_conll"]:
    r = all_results[exp_id]
    print(f"  {r['model']}: greedy_f1={r['greedy_f1']:.4f} oracle_f1={r['oracle_f1']:.4f} gap={r['oracle_f1']-r['greedy_f1']:+.4f}")

# Save report
out_path = "/root/autodl-tmp/struct_self_consist_ie/output/exp_scale_qwen3_4b_conll/scale_ablation_report.json"
with open(out_path, "w") as f:
    json.dump(all_results, f, indent=2, default=lambda o: float(o) if isinstance(o, (np.floating,)) else str(o))
print(f"\nReport saved to {out_path}")
