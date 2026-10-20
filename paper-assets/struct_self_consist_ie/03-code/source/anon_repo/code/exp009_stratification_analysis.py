#!/usr/bin/env python3
"""exp-009: Capability Stratification — difficulty-dependent signal effectiveness analysis."""

import json
import sys
import os
import numpy as np
from collections import Counter
from itertools import combinations
from scipy.stats import spearmanr
from scipy.optimize import linear_sum_assignment

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUTPUT_DIR = os.path.join(BASE, "output")
RESULT_PATH = os.path.join(OUTPUT_DIR, "exp009_stratification_results.json")
N_BOOTSTRAP = 2000
RNG = np.random.RandomState(42)

def entity_strict_match(pred_ents, gold_ents):
    pred_set = {(e["start"], e["end"], e["type"]) for e in pred_ents}
    gold_set = {(e["start"], e["end"], e["type"]) for e in gold_ents}
    tp = len(pred_set & gold_set)
    return tp, len(pred_set - gold_set), len(gold_set - pred_set)

def relation_strict_match(pred_rels, gold_rels):
    pred_set = {(r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"]) for r in pred_rels}
    gold_set = {(r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"]) for r in gold_rels}
    tp = len(pred_set & gold_set)
    return tp, len(pred_set - gold_set), len(gold_set - pred_set)

def per_instance_f1(pred, gold, subtask="ner"):
    if subtask == "ner":
        tp, fp, fn = entity_strict_match(pred.get("entities", []), gold.get("entities", []))
    elif subtask == "re":
        tp, fp, fn = relation_strict_match(pred.get("relations", []), gold.get("relations", []))
    else:
        raise ValueError(subtask)
    if tp + fp == 0 and tp + fn == 0:
        return 1.0
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r) if (p + r) > 0 else 0.0

def _extract_surface_keys(sample, subtask):
    if subtask == "ner":
        return frozenset((e["text"], e["type"]) for e in sample.get("entities", []))
    elif subtask == "re":
        return frozenset((r["head"], r["tail"], r["type"]) for r in sample.get("relations", []))

def fleiss_kappa_surface(samples, subtask="ner"):
    n_raters = len(samples)
    if n_raters <= 1:
        return 1.0
    entity_sets = []
    all_keys = set()
    for s in samples:
        keys = set(_extract_surface_keys(s, subtask))
        entity_sets.append(keys)
        all_keys |= keys
    n_subjects = len(all_keys)
    if n_subjects == 0:
        return 1.0
    key_list = sorted(all_keys)
    rating = np.zeros((n_subjects, 2), dtype=np.int64)
    for es in entity_sets:
        for idx, key in enumerate(key_list):
            if key in es:
                rating[idx, 1] += 1
            else:
                rating[idx, 0] += 1
    n = n_raters
    if np.all(np.max(rating, axis=1) == n):
        return 1.0
    P_i = (np.sum(rating ** 2, axis=1) - n) / (n * (n - 1))
    P_bar = np.mean(P_i)
    p_j = np.sum(rating, axis=0) / (n_subjects * n)
    P_e = np.sum(p_j ** 2)
    if abs(1.0 - P_e) < 1e-12:
        return 1.0
    return float((P_bar - P_e) / (1.0 - P_e))

def _span_soft_jaccard(s1s, s1e, s2s, s2e):
    overlap = max(0, min(s1e, s2e) - max(s1s, s2s))
    union = (s1e - s1s) + (s2e - s2s) - overlap
    return overlap / union if union > 0 else 0.0

def _ner_soft_jaccard_pair(ents_a, ents_b):
    if not ents_a and not ents_b: return 1.0
    if not ents_a or not ents_b: return 0.0
    types = set(e["type"] for e in ents_a) | set(e["type"] for e in ents_b)
    ga = {}; gb = {}
    for e in ents_a: ga.setdefault(e["type"], []).append(e)
    for e in ents_b: gb.setdefault(e["type"], []).append(e)
    total_score = 0.0; total_weight = 0
    for t in types:
        a_list = ga.get(t, []); b_list = gb.get(t, [])
        denom = max(len(a_list), len(b_list))
        if denom == 0: continue
        total_weight += denom
        if not a_list or not b_list: continue
        cost = np.zeros((len(a_list), len(b_list)))
        for i, ea in enumerate(a_list):
            for j, eb in enumerate(b_list):
                cost[i, j] = _span_soft_jaccard(ea["start"], ea["end"], eb["start"], eb["end"])
        ri, ci = linear_sum_assignment(-cost)
        total_score += cost[ri, ci].sum()
    return total_score / total_weight if total_weight > 0 else 1.0

def _re_soft_jaccard_pair(rels_a, rels_b):
    if not rels_a and not rels_b: return 1.0
    if not rels_a or not rels_b: return 0.0
    cost = np.zeros((len(rels_a), len(rels_b)))
    for i, a in enumerate(rels_a):
        for j, b in enumerate(rels_b):
            if a["type"] != b["type"]: continue
            h = _span_soft_jaccard(a["head_start"], a["head_end"], b["head_start"], b["head_end"])
            t = _span_soft_jaccard(a["tail_start"], a["tail_end"], b["tail_start"], b["tail_end"])
            cost[i, j] = h * t
    ri, ci = linear_sum_assignment(-cost)
    return cost[ri, ci].sum() / max(len(rels_a), len(rels_b))

def soft_jaccard(samples, subtask="ner"):
    n = len(samples)
    if n <= 1: return 1.0
    pair_fn = _ner_soft_jaccard_pair if subtask == "ner" else _re_soft_jaccard_pair
    field = "entities" if subtask == "ner" else "relations"
    scores = []
    for i, j in combinations(range(n), 2):
        scores.append(pair_fn(samples[i].get(field, []), samples[j].get(field, [])))
    return float(np.mean(scores))

def voting_confidence(samples, subtask="ner"):
    n = len(samples)
    if n == 0: return 0.0
    keys_per_sample = [_extract_surface_keys(s, subtask) for s in samples]
    all_keys = set()
    for ks in keys_per_sample: all_keys |= set(ks)
    if not all_keys: return 1.0
    freqs = []
    for k in all_keys:
        cnt = sum(1 for ks in keys_per_sample if k in ks)
        freqs.append(cnt / n)
    return float(np.mean(freqs))

def exact_match_rate(samples, subtask="ner"):
    n = len(samples)
    if n <= 1: return 1.0
    keys_per_sample = [_extract_surface_keys(s, subtask) for s in samples]
    counts = Counter(keys_per_sample)
    return counts.most_common(1)[0][1] / n

def compute_auroc(scores, labels):
    if len(scores) < 3: return 0.5
    med = np.median(labels)
    pos = [s for s, l in zip(scores, labels) if l > med]
    neg = [s for s, l in zip(scores, labels) if l <= med]
    if not pos or not neg: return 0.5
    conc = sum(1 for p in pos for n_ in neg if p > n_)
    tied = sum(1 for p in pos for n_ in neg if p == n_)
    return (conc + 0.5 * tied) / (len(pos) * len(neg))

def bootstrap_spearman(signal_vals, f1_vals, n_boot=N_BOOTSTRAP):
    n = len(signal_vals)
    if n < 5:
        return {"rho": float("nan"), "ci_lo": float("nan"), "ci_hi": float("nan"), "p": float("nan")}
    sig = np.array(signal_vals); f1 = np.array(f1_vals)
    rho_obs, p_obs = spearmanr(sig, f1)
    rhos = []
    for _ in range(n_boot):
        idx = RNG.randint(0, n, size=n)
        if np.std(sig[idx]) < 1e-12 or np.std(f1[idx]) < 1e-12: continue
        r, _ = spearmanr(sig[idx], f1[idx])
        if not np.isnan(r): rhos.append(r)
    if len(rhos) < 100:
        return {"rho": float(rho_obs), "ci_lo": float("nan"), "ci_hi": float("nan"), "p": float(p_obs)}
    ci_lo, ci_hi = np.percentile(rhos, [2.5, 97.5])
    return {"rho": float(rho_obs), "ci_lo": float(ci_lo), "ci_hi": float(ci_hi), "p": float(p_obs)}

def bootstrap_auroc(signal_vals, f1_vals, n_boot=N_BOOTSTRAP):
    n = len(signal_vals)
    if n < 5:
        return {"auroc": float("nan"), "ci_lo": float("nan"), "ci_hi": float("nan")}
    auroc_obs = compute_auroc(signal_vals, f1_vals)
    aurocs = []
    for _ in range(n_boot):
        idx = RNG.randint(0, n, size=n)
        aurocs.append(compute_auroc([signal_vals[i] for i in idx], [f1_vals[i] for i in idx]))
    ci_lo, ci_hi = np.percentile(aurocs, [2.5, 97.5])
    return {"auroc": float(auroc_obs), "ci_lo": float(ci_lo), "ci_hi": float(ci_hi)}

def load_and_compute(jsonl_path, subtask="ner"):
    instances = []
    with open(jsonl_path) as f:
        for line in f:
            instances.append(json.loads(line))
    records = []
    for idx, inst in enumerate(instances):
        if idx % 100 == 0:
            print(f"  computing signals: {idx}/{len(instances)}", file=sys.stderr, flush=True)
        text = inst["text"]; gold = inst["gold"]; samples = inst["samples"]
        greedy = inst.get("greedy", samples[0] if samples else {"entities": [], "relations": []})
        logprobs_list = inst.get("logprobs", [])
        gf1 = per_instance_f1(greedy, gold, subtask)
        sj = soft_jaccard(samples, subtask)
        fk = fleiss_kappa_surface(samples, subtask)
        vc = voting_confidence(samples, subtask)
        em = exact_match_rate(samples, subtask)
        lp = float(np.mean(logprobs_list)) if logprobs_list else float(np.mean([s.get("mean_logprob", 0) for s in samples]))
        sent_len = len(text.split())
        ent_count = len(gold.get("entities", [])) if subtask == "ner" else len(gold.get("relations", []))
        records.append({"id": inst["id"], "greedy_f1": gf1, "sj": sj, "fk": fk,
                        "voting_conf": vc, "em": em, "logprob": lp,
                        "sent_len": sent_len, "ent_count": ent_count})
    return records

def stratify_by_greedy_f1(records):
    strata = {"[0, 0.25)": [], "[0.25, 0.5)": [], "[0.5, 0.75)": [], "[0.75, 1.0]": []}
    for r in records:
        f = r["greedy_f1"]
        if f < 0.25: strata["[0, 0.25)"].append(r)
        elif f < 0.5: strata["[0.25, 0.5)"].append(r)
        elif f < 0.75: strata["[0.5, 0.75)"].append(r)
        else: strata["[0.75, 1.0]"].append(r)
    return strata

def stratify_by_quartiles(records, key):
    arr = np.array([r[key] for r in records])
    q25, q50, q75 = np.percentile(arr, [25, 50, 75])
    strata = {"Q1 (lowest)": [], "Q2": [], "Q3": [], "Q4 (highest)": []}
    for r in records:
        v = r[key]
        if v <= q25: strata["Q1 (lowest)"].append(r)
        elif v <= q50: strata["Q2"].append(r)
        elif v <= q75: strata["Q3"].append(r)
        else: strata["Q4 (highest)"].append(r)
    return strata, {"q25": float(q25), "q50": float(q50), "q75": float(q75)}

def stratify_entity_count(records):
    strata = {"0": [], "1-2": [], "3-5": [], "6+": []}
    for r in records:
        c = r["ent_count"]
        if c == 0: strata["0"].append(r)
        elif c <= 2: strata["1-2"].append(r)
        elif c <= 5: strata["3-5"].append(r)
        else: strata["6+"].append(r)
    return strata

SIGNALS = ["sj", "fk", "logprob", "voting_conf", "em"]

def analyze_stratum(records):
    n = len(records)
    if n < 5:
        return {"n": n, "mean_f1": float(np.mean([r["greedy_f1"] for r in records])) if records else 0.0,
                "signals": {s: {"rho": None, "auroc": None} for s in SIGNALS}}
    f1s = [r["greedy_f1"] for r in records]
    result = {"n": n, "mean_f1": float(np.mean(f1s)), "std_f1": float(np.std(f1s)), "signals": {}}
    for sig_name in SIGNALS:
        sig_vals = [r[sig_name] for r in records]
        if np.std(sig_vals) < 1e-12:
            result["signals"][sig_name] = {"rho": 0.0, "rho_ci_lo": 0.0, "rho_ci_hi": 0.0, "p": 1.0,
                                           "auroc": 0.5, "auroc_ci_lo": 0.5, "auroc_ci_hi": 0.5}
            continue
        sp = bootstrap_spearman(sig_vals, f1s)
        au = bootstrap_auroc(sig_vals, f1s)
        result["signals"][sig_name] = {"rho": sp["rho"], "rho_ci_lo": sp["ci_lo"], "rho_ci_hi": sp["ci_hi"],
                                       "p": sp["p"], "auroc": au["auroc"], "auroc_ci_lo": au["ci_lo"], "auroc_ci_hi": au["ci_hi"]}
    return result

def analyze_all_strata(strata_dict, label):
    print(f"\n{'='*60}\nStratification: {label}", file=sys.stderr, flush=True)
    results = {}
    for name, records in strata_dict.items():
        print(f"  {name}: n={len(records)}", file=sys.stderr, flush=True)
        results[name] = analyze_stratum(records)
    return results

def main():
    all_results = {}

    print("Loading SciERC NER (exp001)...", file=sys.stderr, flush=True)
    scierc_ner = load_and_compute(os.path.join(OUTPUT_DIR, "exp001_n16_seed42", "samples.jsonl"), subtask="ner")
    print(f"  {len(scierc_ner)} instances", file=sys.stderr, flush=True)
    all_results["scierc_ner"] = {"n_total": len(scierc_ner),
        "by_greedy_f1": analyze_all_strata(stratify_by_greedy_f1(scierc_ner), "SciERC NER / greedy F1")}
    strata_sl, thresh_sl = stratify_by_quartiles(scierc_ner, "sent_len")
    all_results["scierc_ner"]["by_sent_len"] = analyze_all_strata(strata_sl, "SciERC NER / sent_len")
    all_results["scierc_ner"]["sent_len_thresholds"] = thresh_sl
    all_results["scierc_ner"]["by_ent_count"] = analyze_all_strata(stratify_entity_count(scierc_ner), "SciERC NER / ent_count")

    print("\nLoading SciERC RE (exp008)...", file=sys.stderr, flush=True)
    scierc_re = load_and_compute(os.path.join(OUTPUT_DIR, "exp008_re_n16", "samples.jsonl"), subtask="re")
    print(f"  {len(scierc_re)} instances", file=sys.stderr, flush=True)
    all_results["scierc_re"] = {"n_total": len(scierc_re),
        "by_greedy_f1": analyze_all_strata(stratify_by_greedy_f1(scierc_re), "SciERC RE / greedy F1")}
    strata_sl_re, thresh_sl_re = stratify_by_quartiles(scierc_re, "sent_len")
    all_results["scierc_re"]["by_sent_len"] = analyze_all_strata(strata_sl_re, "SciERC RE / sent_len")
    all_results["scierc_re"]["sent_len_thresholds"] = thresh_sl_re
    all_results["scierc_re"]["by_ent_count"] = analyze_all_strata(stratify_entity_count(scierc_re), "SciERC RE / rel_count")

    print("\nLoading CoNLL-2003 NER (exp002)...", file=sys.stderr, flush=True)
    conll_ner = load_and_compute(os.path.join(OUTPUT_DIR, "exp002_conll2003", "samples.jsonl"), subtask="ner")
    print(f"  {len(conll_ner)} instances", file=sys.stderr, flush=True)
    all_results["conll_ner"] = {"n_total": len(conll_ner),
        "by_greedy_f1": analyze_all_strata(stratify_by_greedy_f1(conll_ner), "CoNLL NER / greedy F1")}
    strata_sl_c, thresh_sl_c = stratify_by_quartiles(conll_ner, "sent_len")
    all_results["conll_ner"]["by_sent_len"] = analyze_all_strata(strata_sl_c, "CoNLL NER / sent_len")
    all_results["conll_ner"]["sent_len_thresholds"] = thresh_sl_c
    all_results["conll_ner"]["by_ent_count"] = analyze_all_strata(stratify_entity_count(conll_ner), "CoNLL NER / ent_count")

    for dataset_name, records in [("scierc_ner", scierc_ner), ("scierc_re", scierc_re), ("conll_ner", conll_ner)]:
        f1s = np.array([r["greedy_f1"] for r in records])
        slens = np.array([r["sent_len"] for r in records])
        ents = np.array([r["ent_count"] for r in records])
        r1, p1 = spearmanr(f1s, slens); r2, p2 = spearmanr(f1s, ents); r3, p3 = spearmanr(slens, ents)
        all_results[dataset_name]["proxy_correlations"] = {
            "f1_vs_sent_len": {"rho": float(r1), "p": float(p1)},
            "f1_vs_ent_count": {"rho": float(r2), "p": float(p2)},
            "sent_len_vs_ent_count": {"rho": float(r3), "p": float(p3)}}

    with open(RESULT_PATH, "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {RESULT_PATH}", file=sys.stderr, flush=True)

    # Summary
    for dataset in ["scierc_ner", "scierc_re", "conll_ner"]:
        data = all_results[dataset]
        print(f"\n{'='*70}\n{dataset.upper()} (n={data['n_total']})\n{'='*70}")
        pc = data["proxy_correlations"]
        print(f"Proxy corr: f1-slen={pc['f1_vs_sent_len']['rho']:.3f}, f1-ecnt={pc['f1_vs_ent_count']['rho']:.3f}, slen-ecnt={pc['sent_len_vs_ent_count']['rho']:.3f}")
        for sk, sl in [("by_greedy_f1","Greedy F1"),("by_sent_len","Sent Len"),("by_ent_count","Ent/Rel Count")]:
            strata = data[sk]
            print(f"\n  By {sl}:")
            print(f"  {'Stratum':<16} {'n':>5} {'mF1':>6} | {'SJ_rho':>7} {'FK_rho':>7} {'LP_rho':>7} {'VC_rho':>7} {'EM_rho':>7} | {'SJ_auc':>7} {'FK_auc':>7} {'LP_auc':>7} {'VC_auc':>7} {'EM_auc':>7}")
            for sn, sd in strata.items():
                row = f"  {sn:<16} {sd['n']:>5} {sd['mean_f1']:>6.3f} |"
                for sig in SIGNALS:
                    s = sd["signals"].get(sig, {})
                    rho = s.get("rho")
                    row += f" {rho:>7.3f}" if rho is not None and not (isinstance(rho, float) and np.isnan(rho)) else " N/A"
                row += " |"
                for sig in SIGNALS:
                    s = sd["signals"].get(sig, {})
                    auc = s.get("auroc")
                    row += f" {auc:>7.3f}" if auc is not None and not (isinstance(auc, float) and np.isnan(auc)) else "     N/A"
                print(row)

if __name__ == "__main__":
    main()
