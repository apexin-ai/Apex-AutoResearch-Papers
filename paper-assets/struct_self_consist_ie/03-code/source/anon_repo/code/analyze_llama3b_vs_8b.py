#!/usr/bin/env python3
"""Scale ablation: LLaMA 3.2-3B vs LLaMA 3.1-8B — SciERC NER — 5-signal comparison."""
import json, sys, os
import numpy as np
from scipy.stats import spearmanr, rankdata
from collections import Counter

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1

EXPERIMENTS = {
    "llama_8b_scierc": {
        "path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_018_llama_scierc_seed42_r1024/samples.jsonl",
        "subtask": "ner",
        "model": "LLaMA-3.1-8B",
    },
    "llama_3b_scierc": {
        "path": "/root/autodl-tmp/struct_self_consist_ie/output/review_round9_experiments/llama3b_scierc/samples.jsonl",
        "subtask": "ner",
        "model": "LLaMA-3.2-3B",
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

def analyze(path, subtask):
    instances = load_data(path)
    entity_key = "entities" if subtask == "ner" else "relations"
    valid = [inst for inst in instances if len(inst["gold"].get(entity_key, [])) > 0]

    greedy_f1s = []
    for inst in valid:
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1s.append(per_instance_f1(greedy, inst["gold"], subtask=subtask))
    conditional = [inst for inst, f1 in zip(valid, greedy_f1s) if f1 > 0]

    oracle_f1s = []
    for inst in valid:
        best = max(per_instance_f1(s, inst["gold"], subtask=subtask) for s in inst["samples"])
        oracle_f1s.append(best)

    results = {
        "n_total": len(instances), "n_valid": len(valid), "n_conditional": len(conditional),
        "greedy_f1": round(float(np.mean(greedy_f1s)), 4),
        "oracle_f1": round(float(np.mean(oracle_f1s)), 4),
    }

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

        signals = {"SJ": np.array(sj), "FK": np.array(fk), "LP": np.array(lp),
                    "EM": np.array(em), "Voting": np.array(vc)}
        f1_arr = np.array(f1s)
        binary = (f1_arr >= 1.0).astype(int)

        split_res = {"n": len(split_insts), "greedy_f1_mean": round(float(np.mean(f1s)), 4)}
        for name, vals in signals.items():
            rho, p_rho = safe_spearman(vals, f1_arr)
            auroc = safe_auroc(vals, binary)
            split_res[name] = {"rho": round(rho, 4), "p_rho": p_rho, "auroc": round(auroc, 4)}

        results[split_name] = split_res
    return results

if __name__ == "__main__":
    all_results = {}
    for exp_id, cfg in EXPERIMENTS.items():
        print(f"Processing {exp_id} ({cfg['model']})...")
        res = analyze(cfg["path"], cfg["subtask"])
        res["model"] = cfg["model"]
        all_results[exp_id] = res

    print("\n" + "="*80)
    print("  SCALE ABLATION: LLaMA-3.2-3B vs LLaMA-3.1-8B — SciERC NER")
    print("="*80)

    for split in ["full", "conditional"]:
        print(f"\n--- {split.upper()} split ---")
        print(f"{'Signal':<12} {'8B rho':>8} {'8B AUROC':>10} {'3B rho':>8} {'3B AUROC':>10} {'delta_rho':>10}")
        print("-"*62)
        for sig in ["Voting", "SJ", "FK", "EM", "LP"]:
            r8 = all_results["llama_8b_scierc"][split][sig]
            r3 = all_results["llama_3b_scierc"][split][sig]
            delta = r3["rho"] - r8["rho"]
            print(f"{sig:<12} {r8['rho']:>+8.4f} {r8['auroc']:>10.4f} {r3['rho']:>+8.4f} {r3['auroc']:>10.4f} {delta:>+10.4f}")
        print(f"\n  Greedy F1:  8B={all_results['llama_8b_scierc'][split]['greedy_f1_mean']:.4f}  "
              f"3B={all_results['llama_3b_scierc'][split]['greedy_f1_mean']:.4f}")

    print(f"\n--- Greedy/Oracle F1 ---")
    for exp_id in ["llama_8b_scierc", "llama_3b_scierc"]:
        r = all_results[exp_id]
        print(f"  {r['model']}: greedy={r['greedy_f1']:.4f} oracle={r['oracle_f1']:.4f} gap={r['oracle_f1']-r['greedy_f1']:+.4f}")

    print(f"\n--- SJ > FK ordering ---")
    for exp_id in ["llama_8b_scierc", "llama_3b_scierc"]:
        r = all_results[exp_id]
        sj_rho = r["full"]["SJ"]["rho"]
        fk_rho = r["full"]["FK"]["rho"]
        print(f"  {r['model']}: SJ={sj_rho:.4f} FK={fk_rho:.4f} SJ>FK={sj_rho > fk_rho} (delta={sj_rho-fk_rho:+.4f})")

    out_dir = "/root/autodl-tmp/struct_self_consist_ie/output/review_round9_experiments/llama3b_scierc"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "comparison_vs_8b.json")
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2, default=lambda o: float(o) if isinstance(o, (np.floating,)) else str(o))
    print(f"\nReport saved to {out_path}")
