"""
NER LP-F1 Spearman Correlation Analysis
Computes pooled and within-instance Spearman rho for NER finetuned N=8 data.
"""
import json
import sys
import numpy as np
from scipy.stats import spearmanr


def entity_set(entities):
    """Convert entity list to set of (text, type, start, end) tuples."""
    return {(e["text"], e["type"], e["start"], e["end"]) for e in entities}


def compute_f1(pred_entities, gold_entities):
    pred_set = entity_set(pred_entities)
    gold_set = entity_set(gold_entities)
    if len(pred_set) == 0 and len(gold_set) == 0:
        return 1.0
    if len(pred_set) == 0 or len(gold_set) == 0:
        return 0.0
    tp = len(pred_set & gold_set)
    precision = tp / len(pred_set)
    recall = tp / len(gold_set)
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)


def analyze(samples_path, dataset_name):
    with open(samples_path) as f:
        instances = [json.loads(line) for line in f]

    all_logprobs = []
    all_f1s = []
    within_rhos = []
    n_total = 0
    n_zero_f1_instances = 0

    for inst in instances:
        gold_ents = inst["gold"]["entities"]
        samples = inst["samples"]
        n_total += 1

        inst_lps = []
        inst_f1s = []
        for s in samples:
            lp = s["mean_logprob"]
            f1 = compute_f1(s["entities"], gold_ents)
            inst_lps.append(lp)
            inst_f1s.append(f1)
            all_logprobs.append(lp)
            all_f1s.append(f1)

        if all(f == 0.0 for f in inst_f1s):
            n_zero_f1_instances += 1

        if np.std(inst_f1s) > 0:
            rho, _ = spearmanr(inst_lps, inst_f1s)
            if not np.isnan(rho):
                within_rhos.append(rho)

    pooled_rho, pooled_p = spearmanr(all_logprobs, all_f1s)
    within_rho_mean = np.mean(within_rhos) if within_rhos else float("nan")
    zero_f1_pct = n_zero_f1_instances / n_total * 100

    print(f"{dataset_name}:")
    print(f"  Pooled rho = {pooled_rho:.4f}, p = {pooled_p:.2e}, n_points = {len(all_logprobs)}")
    print(f"  Within-inst rho = {within_rho_mean:.4f}, n_valid = {len(within_rhos)} / {n_total}")
    print(f"  Zero-F1% = {zero_f1_pct:.1f}% ({n_zero_f1_instances}/{n_total})")
    print()
    return {
        "dataset": dataset_name,
        "pooled_rho": pooled_rho,
        "pooled_p": pooled_p,
        "within_rho": within_rho_mean,
        "n_valid": len(within_rhos),
        "n_total": n_total,
        "zero_f1_pct": zero_f1_pct,
        "n_zero_f1": n_zero_f1_instances,
    }


if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        path = sys.argv[1]
        name = sys.argv[2]
        analyze(path, name)
    else:
        base = "/root/autodl-tmp/struct_self_consist_ie/output"
        datasets = [
            (f"{base}/scierc_mf4v2_seed42/samples.jsonl", "SciERC"),
            (f"{base}/conll_mf4v2_seed42/samples.jsonl", "CoNLL"),
            (f"{base}/fewnerd_mf4v2_seed42_v3/samples.jsonl", "FewNERD"),
        ]

        results = []
        for path, name in datasets:
            try:
                r = analyze(path, name)
                results.append(r)
            except FileNotFoundError:
                print(f"{name}: FILE NOT FOUND at {path}\n")

        if results:
            print("=" * 72)
            print("NER LP-F1 Spearman rho (finetuned, N=8, seed=42)")
            print()
            print(f"| {'Dataset':<10} | {'Pooled rho':>10} | {'p-value':>10} | {'Within-inst rho':>15} | {'n_valid':>7} | {'Zero-F1%':>8} |")
            print(f"|{'-'*12}|{'-'*12}|{'-'*12}|{'-'*17}|{'-'*9}|{'-'*10}|")
            for r in results:
                print(f"| {r['dataset']:<10} | {r['pooled_rho']:>10.4f} | {r['pooled_p']:>10.2e} | {r['within_rho']:>15.4f} | {r['n_valid']:>7d} | {r['zero_f1_pct']:>7.1f}% |")
