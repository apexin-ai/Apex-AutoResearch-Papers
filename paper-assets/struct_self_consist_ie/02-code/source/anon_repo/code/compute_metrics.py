#!/usr/bin/env python3
"""Compute metrics for struct_self_consist_ie experiments."""
import json, argparse, sys
import numpy as np
from collections import Counter
from itertools import combinations
from scipy.stats import spearmanr

def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f]

def entity_set(ext):
    return {(e["start"], e["end"], e["type"]) for e in ext.get("entities", [])}

def relation_set(ext):
    return {(r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"])
            for r in ext.get("relations", [])}

def entity_surface_set(ext):
    return frozenset((e["text"], e["type"]) for e in ext.get("entities", []))

def f1_from_sets(pred, gold):
    tp = len(pred & gold)
    fp = len(pred - gold)
    fn = len(gold - pred)
    if tp == 0:
        return 0.0, tp, fp, fn
    p, r = tp/(tp+fp), tp/(tp+fn)
    return 2*p*r/(p+r), tp, fp, fn

def compute_sj(samples):
    sets = [entity_surface_set(s) for s in samples]
    if len(sets) < 2:
        return 1.0
    scores = []
    for i, j in combinations(range(len(sets)), 2):
        union = len(sets[i] | sets[j])
        scores.append(len(sets[i] & sets[j]) / union if union else 1.0)
    return float(np.mean(scores))

def compute_fk(samples):
    N = len(samples)
    ent_sets = [{(e["text"], e["type"]) for e in s.get("entities", [])} for s in samples]
    all_ents = set().union(*ent_sets)
    if not all_ents:
        return 0.0
    n_sub = len(all_ents)
    ratings = np.zeros((n_sub, 2))
    for idx, ent in enumerate(all_ents):
        present = sum(1 for es in ent_sets if ent in es)
        ratings[idx] = [N - present, present]
    P_i = (np.sum(ratings**2, axis=1) - N) / (N * (N - 1))
    P_bar = np.mean(P_i)
    p_j = np.sum(ratings, axis=0) / (n_sub * N)
    P_e = np.sum(p_j**2)
    if P_e >= 1.0:
        return 1.0
    return float((P_bar - P_e) / (1 - P_e))

def compute_vc(samples, N):
    counter = Counter()
    for s in samples:
        for e in s.get("entities", []):
            counter[(e["text"], e["type"])] += 1
    rates = [v/N for v in counter.values() if v > N/2]
    return float(np.mean(rates)) if rates else 0.0

def compute_lp(samples):
    lps = [s["mean_logprob"] for s in samples if "mean_logprob" in s and np.isfinite(s["mean_logprob"])]
    return float(np.mean(lps)) if lps else float("nan")

def compute_em(samples):
    keys = [entity_surface_set(s) for s in samples]
    return Counter(keys).most_common(1)[0][1] / len(samples)

def compute_auroc(scores, labels):
    scores, labels = np.array(scores, dtype=float), np.array(labels)
    n_pos, n_neg = int(np.sum(labels==1)), int(np.sum(labels==0))
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    order = np.argsort(scores)
    sorted_labels = labels[order]
    ranks = np.arange(1, len(scores)+1, dtype=float)
    u = np.sum(ranks[sorted_labels==1]) - n_pos*(n_pos+1)/2
    return float(u / (n_pos * n_neg))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--data_path", required=True)
    p.add_argument("--subtask", default="ner", choices=["ner", "joint"])
    p.add_argument("--n_samples", type=int, default=16)
    args = p.parse_args()

    data = load_data(args.data_path)
    N = args.n_samples

    parsed = sum(1 for d in data if len(d.get("samples",[])) >= N)

    greedy_ner = {"tp":0,"fp":0,"fn":0}
    oracle_ner = {"tp":0,"fp":0,"fn":0}
    greedy_re = {"tp":0,"fp":0,"fn":0}
    oracle_re = {"tp":0,"fp":0,"fn":0}
    inst_ner_f1 = []
    inst_re_f1 = []
    sj_v, fk_v, vc_v, lp_v, em_v = [], [], [], [], []

    for d in data:
        gold_e = entity_set(d["gold"])
        samples = d["samples"][:N]

        # Greedy NER
        f1, tp, fp, fn = f1_from_sets(entity_set(d["greedy"]), gold_e)
        greedy_ner["tp"]+=tp; greedy_ner["fp"]+=fp; greedy_ner["fn"]+=fn
        inst_ner_f1.append(f1)

        # Oracle NER (best sample by NER F1)
        best_f1, best_tp, best_fp, best_fn = -1, 0, 0, 0
        best_re = (0, 0, 0)
        for s in samples:
            sf1, stp, sfp, sfn = f1_from_sets(entity_set(s), gold_e)
            if sf1 > best_f1:
                best_f1, best_tp, best_fp, best_fn = sf1, stp, sfp, sfn
                if args.subtask == "joint":
                    _, rtp, rfp, rfn = f1_from_sets(relation_set(s), relation_set(d["gold"]))
                    best_re = (rtp, rfp, rfn)
        oracle_ner["tp"]+=best_tp; oracle_ner["fp"]+=best_fp; oracle_ner["fn"]+=best_fn

        if args.subtask == "joint":
            gold_r = relation_set(d["gold"])
            f1r, tp, fp, fn = f1_from_sets(relation_set(d["greedy"]), gold_r)
            greedy_re["tp"]+=tp; greedy_re["fp"]+=fp; greedy_re["fn"]+=fn
            inst_re_f1.append(f1r)
            oracle_re["tp"]+=best_re[0]; oracle_re["fp"]+=best_re[1]; oracle_re["fn"]+=best_re[2]

        sj_v.append(compute_sj(samples))
        fk_v.append(compute_fk(samples))
        vc_v.append(compute_vc(samples, N))
        lp_v.append(compute_lp(samples))
        em_v.append(compute_em(samples))

    def micro(d):
        denom = 2*d["tp"]+d["fp"]+d["fn"]
        return 2*d["tp"]/denom if denom else 0.0

    metrics = {
        "instance_count": len(data),
        "parse_rate": round(parsed/len(data), 4),
        "ner_greedy_f1": round(micro(greedy_ner), 4),
        "ner_oracle_f1": round(micro(oracle_ner), 4),
    }
    if args.subtask == "joint":
        metrics["re_greedy_f1"] = round(micro(greedy_re), 4)
        metrics["re_oracle_f1"] = round(micro(oracle_re), 4)

    signals = {"sj": sj_v, "fk": fk_v, "vc": vc_v, "lp": lp_v, "em": em_v}

    for name, vals in signals.items():
        valid = [(v,f) for v,f in zip(vals, inst_ner_f1) if np.isfinite(v)]
        if len(valid) > 2:
            v, f = zip(*valid)
            rho, _ = spearmanr(v, f)
            metrics[f"rho_{name}_ner"] = round(float(rho), 4)

    if args.subtask == "joint":
        for name, vals in signals.items():
            valid = [(v,f) for v,f in zip(vals, inst_re_f1) if np.isfinite(v)]
            if len(valid) > 2:
                v, f = zip(*valid)
                rho, _ = spearmanr(v, f)
                metrics[f"rho_{name}_re"] = round(float(rho), 4)

    median_ner = float(np.median(inst_ner_f1))
    labels_ner = [1 if f > median_ner else 0 for f in inst_ner_f1]
    for name, vals in signals.items():
        valid_v = [v if np.isfinite(v) else 0.0 for v in vals]
        auroc = compute_auroc(valid_v, labels_ner)
        metrics[f"auroc_{name}_ner"] = round(auroc, 4)

    print(json.dumps(metrics, indent=2))

if __name__ == "__main__":
    main()
