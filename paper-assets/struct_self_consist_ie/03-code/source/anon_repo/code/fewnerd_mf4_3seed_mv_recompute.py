#!/usr/bin/env python3
"""3-seed MV unified recompute for FewNERD finetuned N=8."""
import json
import sys
import os
from collections import Counter

def extract_entities(d):
    return frozenset((e["text"], e["type"], e["start"], e["end"]) for e in d.get("entities", []))

def micro_f1(tp, fp, fn):
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r)

def compute_seed(path, label):
    greedy_tp = greedy_fp = greedy_fn = 0
    mv_tp = mv_fp = mv_fn = 0
    lp_tp = lp_fp = lp_fn = 0
    n_degen = 0
    n_total = 0
    n_gold_nonempty = 0

    with open(path) as f:
        for line in f:
            d = json.loads(line)
            n_total += 1
            gold = extract_entities(d["gold"])
            if not gold:
                continue
            n_gold_nonempty += 1

            # Greedy
            greedy = extract_entities(d["greedy"])
            greedy_tp += len(greedy & gold)
            greedy_fp += len(greedy - gold)
            greedy_fn += len(gold - greedy)

            samples = d["samples"]
            N = len(samples)

            # Per-sample entities and logprobs
            sample_ent_sets = []
            sample_lps = []
            entity_counter = Counter()
            for s in samples:
                ents = extract_entities(s)
                sample_ent_sets.append(ents)
                for e in ents:
                    entity_counter[e] += 1
                lp = s.get("mean_logprob")
                if lp is None:
                    lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
                sample_lps.append(lp)

            # MV strict: count > N/2
            threshold = N / 2
            mv_ents = frozenset(e for e, c in entity_counter.items() if c > threshold)
            mv_tp += len(mv_ents & gold)
            mv_fp += len(mv_ents - gold)
            mv_fn += len(gold - mv_ents)

            # LP-best selection
            best_idx = max(range(N), key=lambda i: sample_lps[i])
            lp_ents = sample_ent_sets[best_idx]
            lp_tp += len(lp_ents & gold)
            lp_fp += len(lp_ents - gold)
            lp_fn += len(gold - lp_ents)

            # Degeneracy
            if len(set(sample_ent_sets)) == 1:
                n_degen += 1

    g_f1 = micro_f1(greedy_tp, greedy_fp, greedy_fn)
    m_f1 = micro_f1(mv_tp, mv_fp, mv_fn)
    l_f1 = micro_f1(lp_tp, lp_fp, lp_fn)
    degen = n_degen / n_gold_nonempty * 100

    print(f"{label}: greedy={g_f1:.4f}, mv={m_f1:.4f}, Δ={((m_f1-g_f1)*100):+.2f} pp, lp={l_f1:.4f}, degen={degen:.1f}% (n={n_gold_nonempty}/{n_total})")
    return {"greedy": g_f1, "mv": m_f1, "lp": l_f1, "degen": degen, "n": n_gold_nonempty}

if __name__ == "__main__":
    base = "/root/autodl-tmp/struct_self_consist_ie/output"
    seeds = {}
    for label, path in [
        ("Seed 42",  os.path.join(base, "fewnerd_mf4_seed42/samples.jsonl")),
        ("Seed 123", os.path.join(base, "fewnerd_mf4_seed123_v2/samples.jsonl")),
        ("Seed 456", os.path.join(base, "fewnerd_mf4_seed456/samples.jsonl")),
    ]:
        if os.path.exists(path):
            seeds[label] = compute_seed(path, label)
        else:
            print(f"{label}: FILE NOT FOUND ({path})")

    if len(seeds) >= 2:
        import numpy as np
        g = [v["greedy"] for v in seeds.values()]
        m = [v["mv"] for v in seeds.values()]
        d = [(v["mv"]-v["greedy"])*100 for v in seeds.values()]
        l = [v["lp"] for v in seeds.values()]
        dg = [v["degen"] for v in seeds.values()]
        print(f"\nMean±σ:   greedy={np.mean(g):.4f}±{np.std(g):.4f}, mv={np.mean(m):.4f}±{np.std(m):.4f}, mv_Δ={np.mean(d):+.2f}±{np.std(d):.2f} pp, lp={np.mean(l):.4f}±{np.std(l):.4f}, degen={np.mean(dg):.1f}±{np.std(dg):.1f}%")
