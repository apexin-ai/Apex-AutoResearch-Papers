#!/usr/bin/env python3
"""Generate per-instance reliability data from exp_012_rerun_1024 samples."""
import json
import sys
from collections import Counter
from itertools import combinations

import numpy as np
from scipy.optimize import linear_sum_assignment

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples_with_logprobs.jsonl"
OUTPUT_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/reliability_data_1024.json"


def _span_soft_jaccard(s1_start, s1_end, s2_start, s2_end):
    inter = max(0, min(s1_end, s2_end) - max(s1_start, s2_start))
    union = max(s1_end, s2_end) - min(s1_start, s2_start)
    return inter / union if union > 0 else 1.0


def ner_soft_jaccard(samples):
    n = len(samples)
    if n <= 1:
        return 1.0
    scores = []
    for i, j in combinations(range(n), 2):
        ents_a = samples[i].get("entities", [])
        ents_b = samples[j].get("entities", [])
        if not ents_a and not ents_b:
            scores.append(1.0)
            continue
        if not ents_a or not ents_b:
            scores.append(0.0)
            continue
        # Group by type
        types = set(e["type"] for e in ents_a) | set(e["type"] for e in ents_b)
        total_sim = 0.0
        total_weight = 0.0
        for t in types:
            ga = [e for e in ents_a if e["type"] == t]
            gb = [e for e in ents_b if e["type"] == t]
            if not ga and not gb:
                continue
            weight = max(len(ga), len(gb))
            total_weight += weight
            if not ga or not gb:
                continue
            cost = np.zeros((len(ga), len(gb)))
            for ii, ea in enumerate(ga):
                for jj, eb in enumerate(gb):
                    cost[ii, jj] = _span_soft_jaccard(ea["start"], ea["end"], eb["start"], eb["end"])
            ri, ci = linear_sum_assignment(-cost)
            total_sim += cost[ri, ci].sum()
        if total_weight == 0:
            scores.append(1.0)
        else:
            scores.append(total_sim / total_weight)
    return float(np.mean(scores))


def re_soft_jaccard(samples):
    n = len(samples)
    if n <= 1:
        return 1.0
    scores = []
    for i, j in combinations(range(n), 2):
        rels_a = samples[i].get("relations", [])
        rels_b = samples[j].get("relations", [])
        if not rels_a and not rels_b:
            scores.append(1.0)
            continue
        if not rels_a or not rels_b:
            scores.append(0.0)
            continue
        types = set(r["type"] for r in rels_a) | set(r["type"] for r in rels_b)
        total_sim = 0.0
        total_weight = 0.0
        for t in types:
            ga = [r for r in rels_a if r["type"] == t]
            gb = [r for r in rels_b if r["type"] == t]
            if not ga and not gb:
                continue
            weight = max(len(ga), len(gb))
            total_weight += weight
            if not ga or not gb:
                continue
            cost = np.zeros((len(ga), len(gb)))
            for ii, ra in enumerate(ga):
                for jj, rb in enumerate(gb):
                    h_sim = _span_soft_jaccard(ra["head_start"], ra["head_end"], rb["head_start"], rb["head_end"])
                    t_sim = _span_soft_jaccard(ra["tail_start"], ra["tail_end"], rb["tail_start"], rb["tail_end"])
                    cost[ii, jj] = (h_sim + t_sim) / 2
            ri, ci = linear_sum_assignment(-cost)
            total_sim += cost[ri, ci].sum()
        if total_weight == 0:
            scores.append(1.0)
        else:
            scores.append(total_sim / total_weight)
    return float(np.mean(scores))


def voting_confidence(samples, subtask):
    N = len(samples)
    if N == 0:
        return 0.0
    counter = Counter()
    if subtask == "ner":
        for s in samples:
            for e in s.get("entities", []):
                counter[(e["text"], e["type"])] += 1
    else:
        for s in samples:
            for r in s.get("relations", []):
                counter[(r["head"], r["tail"], r["type"])] += 1
    if not counter:
        return 0.0
    rates = [v / N for v in counter.values()]
    return float(np.mean(rates))


def mean_sample_f1(samples, gold, subtask):
    f1s = [per_instance_f1(s, gold, subtask=subtask) for s in samples]
    return float(np.mean(f1s)) if f1s else 0.0


def main():
    records = []
    with open(DATA_PATH) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))

    print(f"Loaded {len(records)} instances")
    output = []

    for idx, rec in enumerate(records):
        if idx % 50 == 0:
            print(f"  Processing {idx}/{len(records)}...")
        gold = rec["gold"]
        samples = rec["samples"]

        has_gold_ents = len(gold.get("entities", [])) > 0
        has_gold_rels = len(gold.get("relations", [])) > 0

        sj_ner_val = ner_soft_jaccard(samples) if has_gold_ents else None
        sj_re_val = re_soft_jaccard(samples) if has_gold_rels else None
        vc_ner_val = voting_confidence(samples, "ner")
        vc_re_val = voting_confidence(samples, "re")
        f1_ner_val = mean_sample_f1(samples, gold, "ner") if has_gold_ents else None
        f1_re_val = mean_sample_f1(samples, gold, "re") if has_gold_rels else None

        logprobs = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
        logprobs = [lp for lp in logprobs if np.isfinite(lp)]
        mean_lp = float(np.mean(logprobs)) if logprobs else None

        output.append({
            "id": rec["id"],
            "has_gold_ents": has_gold_ents,
            "has_gold_rels": has_gold_rels,
            "sj_ner": sj_ner_val,
            "sj_re": sj_re_val,
            "vc_ner": vc_ner_val,
            "vc_re": vc_re_val,
            "mean_sample_ner_f1": f1_ner_val,
            "mean_sample_re_f1": f1_re_val,
            "mean_logprob": mean_lp,
        })

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Saved {len(output)} instances to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
