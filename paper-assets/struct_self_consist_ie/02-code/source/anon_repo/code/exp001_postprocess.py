"""exp-001 post-processing: compute all 5 confidence signals and correlations.

Signals: soft_jaccard, fleiss_kappa, logprob, exact_match_rate, voting_confidence
Metrics: Spearman rho, Kendall tau, AUROC (for NER and RE separately)
"""

import argparse
import json
import os
import sys
from collections import Counter

import numpy as np
from scipy.stats import spearmanr, kendalltau

sys.path.insert(0, "/root/autodl-tmp/struct_self_consist_ie/code")

from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1


def load_jsonl(path):
    instances = []
    with open(path) as f:
        for line in f:
            if line.strip():
                instances.append(json.loads(line))
    return instances


def auroc(scores, labels):
    scores = np.array(scores, dtype=float)
    labels = np.array(labels, dtype=int)
    if len(set(labels)) < 2:
        return float("nan")
    pos = scores[labels == 1]
    neg = scores[labels == 0]
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    count = sum(
        float(np.sum(p > neg) + 0.5 * np.sum(p == neg)) for p in pos
    )
    return count / (len(pos) * len(neg))


def _entity_set_key(sample):
    return frozenset((e["text"], e["type"]) for e in sample.get("entities", []))

def _relation_set_key(sample):
    return frozenset((r["head"], r["tail"], r["type"]) for r in sample.get("relations", []))

def exact_match_rate(samples, subtask):
    if not samples:
        return 0.0
    key_fn = _entity_set_key if subtask == "ner" else _relation_set_key
    keys = [key_fn(s) for s in samples]
    counter = Counter(keys)
    return counter.most_common(1)[0][1] / len(samples)


def voting_confidence_ner(samples):
    N = len(samples)
    if N == 0:
        return 0.0
    counter = Counter()
    for s in samples:
        for e in s.get("entities", []):
            counter[(e["text"], e["type"])] += 1
    if not counter:
        return 0.0
    return float(np.mean([c / N for c in counter.values()]))

def voting_confidence_re(samples):
    N = len(samples)
    if N == 0:
        return 0.0
    counter = Counter()
    for s in samples:
        for r in s.get("relations", []):
            counter[(r["head"], r["tail"], r["type"])] += 1
    if not counter:
        return 0.0
    return float(np.mean([c / N for c in counter.values()]))


def compute_all_signals(instances, subtask):
    consistency = compute_all_consistency_scores(instances, subtask=subtask)
    sj = consistency["soft_jaccard"]
    fk = consistency["fleiss_kappa"]

    em_rates = []
    v_confs = []
    logprobs = []
    greedy_f1s = []

    vote_fn = voting_confidence_ner if subtask == "ner" else voting_confidence_re

    for inst in instances:
        em_rates.append(exact_match_rate(inst["samples"], subtask))
        v_confs.append(vote_fn(inst["samples"]))
        if "logprobs" in inst:
            logprobs.append(float(np.mean(inst["logprobs"])))
        else:
            logprobs.append(None)
        greedy_f1s.append(per_instance_f1(inst["greedy"], inst["gold"], subtask))

    return {
        "soft_jaccard": sj,
        "fleiss_kappa": fk,
        "exact_match_rate": em_rates,
        "voting_confidence": v_confs,
        "logprob": logprobs,
        "greedy_f1": greedy_f1s,
    }


def compute_correlations(signals, f1s, instances, subtask):
    field = "entities" if subtask == "ner" else "relations"
    valid = [i for i, inst in enumerate(instances) if inst["gold"].get(field)]
    n_gold_empty = len(instances) - len(valid)

    f1_v = [f1s[i] for i in valid]
    median_f1 = float(np.median(f1_v)) if f1_v else 0.0
    labels = [1 if f > median_f1 else 0 for f in f1_v]

    cond = [i for i in valid if f1s[i] > 0]
    f1_c = [f1s[i] for i in cond]

    results = {}
    for name, scores in signals.items():
        if name == "greedy_f1":
            continue
        sc_v = [scores[i] for i in valid]
        sc_c = [scores[i] for i in cond]

        if any(s is None for s in sc_v):
            results[name] = {"rho": None, "tau": None, "auroc": None,
                             "rho_cond": None, "tau_cond": None, "auroc_cond": None}
            continue

        rho, p_rho = spearmanr(sc_v, f1_v) if len(sc_v) >= 3 else (0.0, 1.0)
        tau, p_tau = kendalltau(sc_v, f1_v) if len(sc_v) >= 3 else (0.0, 1.0)
        auc = auroc(sc_v, labels)

        rho_c, p_rho_c = spearmanr(sc_c, f1_c) if len(sc_c) >= 3 else (0.0, 1.0)
        tau_c, p_tau_c = kendalltau(sc_c, f1_c) if len(sc_c) >= 3 else (0.0, 1.0)
        median_c = float(np.median(f1_c)) if f1_c else 0.0
        labels_c = [1 if f > median_c else 0 for f in f1_c]
        auc_c = auroc(sc_c, labels_c)

        results[name] = {
            "rho": float(rho), "p_rho": float(p_rho),
            "tau": float(tau), "p_tau": float(p_tau),
            "auroc": float(auc) if not np.isnan(auc) else None,
            "n_full": len(sc_v),
            "rho_cond": float(rho_c), "p_rho_cond": float(p_rho_c),
            "tau_cond": float(tau_c), "p_tau_cond": float(p_tau_c),
            "auroc_cond": float(auc_c) if not np.isnan(auc_c) else None,
            "n_cond": len(sc_c),
        }

    return results, n_gold_empty


def print_table(subtask, corr, n_gold_empty):
    print(f"\n{'='*90}")
    print(f"  All 5 Signals ({subtask.upper()}, gold_empty_filtered={n_gold_empty})")
    print(f"{'='*90}")
    print(f"  {'Signal':<22} | {'rho_full':>9} | {'tau_full':>9} | {'AUROC':>7} | {'rho_cond':>9} | {'tau_cond':>9} | {'AUROC_c':>7}")
    print(f"  {'-'*22}-+-{'-'*9}-+-{'-'*9}-+-{'-'*7}-+-{'-'*9}-+-{'-'*9}-+-{'-'*7}")

    for name in ["soft_jaccard", "fleiss_kappa", "logprob", "exact_match_rate", "voting_confidence"]:
        m = corr.get(name, {})
        if m.get("rho") is None:
            print(f"  {name:<22} | {'N/A':>9} | {'N/A':>9} | {'N/A':>7} | {'N/A':>9} | {'N/A':>9} | {'N/A':>7}")
            continue
        auc_s = f"{m['auroc']:.4f}" if m.get("auroc") is not None else "N/A"
        auc_c = f"{m['auroc_cond']:.4f}" if m.get("auroc_cond") is not None else "N/A"
        print(f"  {name:<22} | {m['rho']:>+9.4f} | {m['tau']:>+9.4f} | {auc_s:>7} | {m['rho_cond']:>+9.4f} | {m['tau_cond']:>+9.4f} | {auc_c:>7}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", required=True, help="Path to samples.jsonl")
    parser.add_argument("--output_dir", default=None)
    parser.add_argument("--compare_n8", default=None, help="Path to N=8 samples.jsonl for N-scaling comparison")
    args = parser.parse_args()

    if args.output_dir is None:
        args.output_dir = os.path.dirname(args.samples)

    instances = load_jsonl(args.samples)
    print(f"Loaded {len(instances)} instances, N_samples={len(instances[0]['samples'])}")

    has_logprobs = "logprobs" in instances[0]
    print(f"Logprobs available: {has_logprobs}")

    report = {
        "n_instances": len(instances),
        "n_samples": len(instances[0]["samples"]),
        "has_logprobs": has_logprobs,
    }

    for subtask in ["ner", "re"]:
        signals = compute_all_signals(instances, subtask)
        corr, n_gold_empty = compute_correlations(signals, signals["greedy_f1"], instances, subtask)
        print_table(subtask, corr, n_gold_empty)

        stats = {}
        for name in ["soft_jaccard", "fleiss_kappa", "exact_match_rate", "voting_confidence"]:
            vals = signals[name]
            stats[name] = {"mean": float(np.mean(vals)), "std": float(np.std(vals))}
        if has_logprobs:
            lp_vals = [v for v in signals["logprob"] if v is not None]
            stats["logprob"] = {"mean": float(np.mean(lp_vals)), "std": float(np.std(lp_vals))}

        f1s = signals["greedy_f1"]
        stats["greedy_f1"] = {"mean": float(np.mean(f1s)), "std": float(np.std(f1s))}

        report[subtask] = {
            "correlations": corr,
            "stats": stats,
            "n_gold_empty": n_gold_empty,
        }

    if args.compare_n8:
        print(f"\n{'='*90}")
        print("  N-scaling comparison: N=8 vs N=16")
        print(f"{'='*90}")
        n8_instances = load_jsonl(args.compare_n8)
        report["n_scaling"] = {}

        for subtask in ["ner", "re"]:
            signals_8 = compute_all_signals(n8_instances, subtask)
            corr_8, _ = compute_correlations(signals_8, signals_8["greedy_f1"], n8_instances, subtask)

            signals_16 = compute_all_signals(instances, subtask)
            corr_16, _ = compute_correlations(signals_16, signals_16["greedy_f1"], instances, subtask)

            print(f"\n  {subtask.upper()}:")
            print(f"  {'Signal':<22} | {'rho_N8':>9} | {'rho_N16':>9} | {'delta':>9}")
            print(f"  {'-'*22}-+-{'-'*9}-+-{'-'*9}-+-{'-'*9}")

            scaling = {}
            for name in ["soft_jaccard", "fleiss_kappa", "exact_match_rate", "voting_confidence"]:
                r8 = corr_8.get(name, {}).get("rho", 0) or 0
                r16 = corr_16.get(name, {}).get("rho", 0) or 0
                delta = r16 - r8
                print(f"  {name:<22} | {r8:>+9.4f} | {r16:>+9.4f} | {delta:>+9.4f}")
                scaling[name] = {"rho_n8": r8, "rho_n16": r16, "delta": delta}

            report["n_scaling"][subtask] = scaling

    out_path = os.path.join(args.output_dir, "exp001_all_signals_report.json")
    os.makedirs(args.output_dir, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nReport saved to {out_path}")


if __name__ == "__main__":
    main()
