"""exp-004: RE diagnostic analysis.

Per-relation-type consistency breakdown, error propagation patterns,
conditional threshold sensitivity, bootstrap CI, NER vs RE comparison.
CPU-only. Uses pilot_004 samples.jsonl.
"""

from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.optimize import linear_sum_assignment
from scipy.stats import spearmanr, norm

# ── paths ──────────────────────────────────────────────────────────────
BASE = Path("/root/autodl-tmp/struct_self_consist_ie")
PILOT_004 = BASE / "output" / "mvp_pilot_004" / "samples.jsonl"
PILOT_005 = BASE / "output" / "mvp_pilot_005" / "samples.jsonl"
OUT_DIR = BASE / "output" / "exp004_re_diagnostic"


# ── helpers (copied from consistency.py / evaluation.py to be self-contained) ──

def _span_sj(s1s, s1e, s2s, s2e):
    overlap = max(0, min(s1e, s2e) - max(s1s, s2s))
    union = (s1e - s1s) + (s2e - s2s) - overlap
    return overlap / union if union > 0 else 0.0


def re_soft_jaccard_pair(rels_a, rels_b):
    if not rels_a and not rels_b:
        return 1.0
    if not rels_a or not rels_b:
        return 0.0
    cost = np.zeros((len(rels_a), len(rels_b)))
    for i, a in enumerate(rels_a):
        for j, b in enumerate(rels_b):
            if a["type"] != b["type"]:
                continue
            h = _span_sj(a["head_start"], a["head_end"], b["head_start"], b["head_end"])
            t = _span_sj(a["tail_start"], a["tail_end"], b["tail_start"], b["tail_end"])
            cost[i, j] = h * t
    ri, ci = linear_sum_assignment(-cost)
    return cost[ri, ci].sum() / max(len(rels_a), len(rels_b))


def re_sj_instance(samples):
    n = len(samples)
    if n <= 1:
        return 1.0
    scores = []
    for i, j in combinations(range(n), 2):
        scores.append(re_soft_jaccard_pair(
            samples[i].get("relations", []),
            samples[j].get("relations", []),
        ))
    return float(np.mean(scores))


def fleiss_kappa_re(samples):
    n = len(samples)
    if n <= 1:
        return 1.0
    sets = []
    all_keys = set()
    for s in samples:
        keys = {(r["head"], r["tail"], r["type"]) for r in s.get("relations", [])}
        sets.append(keys)
        all_keys |= keys
    if not all_keys:
        return 1.0
    key_list = sorted(all_keys)
    rating = np.zeros((len(key_list), 2), dtype=np.int64)
    for es in sets:
        for idx, k in enumerate(key_list):
            rating[idx, 1 if k in es else 0] += 1
    if np.all(np.max(rating, axis=1) == n):
        return 1.0
    P_i = (np.sum(rating ** 2, axis=1) - n) / (n * (n - 1))
    P_bar = np.mean(P_i)
    p_j = np.sum(rating, axis=0) / (len(key_list) * n)
    P_e = np.sum(p_j ** 2)
    if abs(1.0 - P_e) < 1e-12:
        return 1.0
    return float((P_bar - P_e) / (1.0 - P_e))


def ner_sj_instance(samples):
    n = len(samples)
    if n <= 1:
        return 1.0
    scores = []
    for i, j in combinations(range(n), 2):
        scores.append(_ner_sj_pair(
            samples[i].get("entities", []),
            samples[j].get("entities", []),
        ))
    return float(np.mean(scores))


def _ner_sj_pair(ents_a, ents_b):
    if not ents_a and not ents_b:
        return 1.0
    if not ents_a or not ents_b:
        return 0.0
    types = {e["type"] for e in ents_a} | {e["type"] for e in ents_b}
    ga = defaultdict(list)
    gb = defaultdict(list)
    for e in ents_a:
        ga[e["type"]].append(e)
    for e in ents_b:
        gb[e["type"]].append(e)
    total_score = 0.0
    total_weight = 0
    for t in types:
        a_list, b_list = ga.get(t, []), gb.get(t, [])
        denom = max(len(a_list), len(b_list))
        if denom == 0:
            continue
        total_weight += denom
        if not a_list or not b_list:
            continue
        cost = np.zeros((len(a_list), len(b_list)))
        for i2, ea in enumerate(a_list):
            for j2, eb in enumerate(b_list):
                cost[i2, j2] = _span_sj(ea["start"], ea["end"], eb["start"], eb["end"])
        ri, ci = linear_sum_assignment(-cost)
        total_score += cost[ri, ci].sum()
    return total_score / total_weight if total_weight > 0 else 1.0


def fleiss_kappa_ner(samples):
    n = len(samples)
    if n <= 1:
        return 1.0
    sets = []
    all_keys = set()
    for s in samples:
        keys = {(e["text"], e["type"]) for e in s.get("entities", [])}
        sets.append(keys)
        all_keys |= keys
    if not all_keys:
        return 1.0
    key_list = sorted(all_keys)
    rating = np.zeros((len(key_list), 2), dtype=np.int64)
    for es in sets:
        for idx, k in enumerate(key_list):
            rating[idx, 1 if k in es else 0] += 1
    if np.all(np.max(rating, axis=1) == n):
        return 1.0
    P_i = (np.sum(rating ** 2, axis=1) - n) / (n * (n - 1))
    P_bar = np.mean(P_i)
    p_j = np.sum(rating, axis=0) / (len(key_list) * n)
    P_e = np.sum(p_j ** 2)
    if abs(1.0 - P_e) < 1e-12:
        return 1.0
    return float((P_bar - P_e) / (1.0 - P_e))


def rel_strict_match(pred_rels, gold_rels):
    pred = {(r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"]) for r in pred_rels}
    gold = {(r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"]) for r in gold_rels}
    tp = len(pred & gold)
    fp = len(pred - gold)
    fn = len(gold - pred)
    return tp, fp, fn


def ent_strict_match(pred_ents, gold_ents):
    pred = {(e["start"], e["end"], e["type"]) for e in pred_ents}
    gold = {(e["start"], e["end"], e["type"]) for e in gold_ents}
    tp = len(pred & gold)
    fp = len(pred - gold)
    fn = len(gold - pred)
    return tp, fp, fn


def prf(tp, fp, fn):
    p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
    return p, r, f


def instance_f1(pred, gold, subtask="re"):
    if subtask == "re":
        tp, fp, fn = rel_strict_match(pred.get("relations", []), gold.get("relations", []))
    else:
        tp, fp, fn = ent_strict_match(pred.get("entities", []), gold.get("entities", []))
    return prf(tp, fp, fn)[2]


def voting_confidence_re(samples):
    """Per-relation voting confidence: mean fraction of samples containing each unique relation."""
    n = len(samples)
    if n == 0:
        return 0.0
    all_rels = set()
    rel_sets = []
    for s in samples:
        keys = {(r["head"], r["tail"], r["type"]) for r in s.get("relations", [])}
        rel_sets.append(keys)
        all_rels |= keys
    if not all_rels:
        return 1.0
    rates = []
    for k in all_rels:
        rate = sum(1 for rs in rel_sets if k in rs) / n
        rates.append(rate)
    return float(np.mean(rates))


def voting_confidence_ner(samples):
    n = len(samples)
    if n == 0:
        return 0.0
    all_ents = set()
    ent_sets = []
    for s in samples:
        keys = {(e["text"], e["type"]) for e in s.get("entities", [])}
        ent_sets.append(keys)
        all_ents |= keys
    if not all_ents:
        return 1.0
    rates = [sum(1 for es in ent_sets if k in es) / n for k in all_ents]
    return float(np.mean(rates))


# ── data loading ────────────────────────────────────────────────────────

def load_samples(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(json.loads(line))
    return data


# ── 1. Per-relation-type breakdown ──────────────────────────────────────

def per_relation_type_breakdown(data):
    """Group instances by which gold relation types they contain.
    For each type, compute SJ, FK, voting_conf correlation with greedy F1."""
    type_instances = defaultdict(list)
    for inst in data:
        gold_rels = inst["gold"]["relations"]
        if not gold_rels:
            continue
        types_present = {r["type"] for r in gold_rels}
        for t in types_present:
            type_instances[t].append(inst)

    results = {}
    for rtype, insts in sorted(type_instances.items()):
        sj_scores = [re_sj_instance(inst["samples"]) for inst in insts]
        fk_scores = [fleiss_kappa_re(inst["samples"]) for inst in insts]
        vc_scores = [voting_confidence_re(inst["samples"]) for inst in insts]
        f1_scores = [instance_f1(inst["greedy"], inst["gold"], "re") for inst in insts]

        n = len(insts)
        rho_sj = float(spearmanr(sj_scores, f1_scores).statistic) if n >= 3 else 0.0
        rho_fk = float(spearmanr(fk_scores, f1_scores).statistic) if n >= 3 else 0.0
        rho_vc = float(spearmanr(vc_scores, f1_scores).statistic) if n >= 3 else 0.0
        p_sj = float(spearmanr(sj_scores, f1_scores).pvalue) if n >= 3 else 1.0
        p_fk = float(spearmanr(fk_scores, f1_scores).pvalue) if n >= 3 else 1.0
        p_vc = float(spearmanr(vc_scores, f1_scores).pvalue) if n >= 3 else 1.0

        n_gold_rels = sum(len([r for r in inst["gold"]["relations"] if r["type"] == rtype]) for inst in insts)
        mean_f1 = float(np.mean(f1_scores))

        results[rtype] = {
            "n_instances": n,
            "n_gold_relations": n_gold_rels,
            "mean_greedy_f1": round(mean_f1, 4),
            "rho_sj": round(rho_sj, 4),
            "p_sj": float(f"{p_sj:.4e}"),
            "rho_fk": round(rho_fk, 4),
            "p_fk": float(f"{p_fk:.4e}"),
            "rho_voting_conf": round(rho_vc, 4),
            "p_voting_conf": float(f"{p_vc:.4e}"),
            "mean_sj": round(float(np.mean(sj_scores)), 4),
            "mean_fk": round(float(np.mean(fk_scores)), 4),
            "mean_voting_conf": round(float(np.mean(vc_scores)), 4),
        }

    return results


# ── 2. Error propagation analysis ──────────────────────────────────────

def classify_re_errors(pred_rels, gold_rels):
    """Classify each FN gold relation into error categories.

    Returns dict with counts of:
    - head_error: head span wrong, tail+type correct
    - tail_error: tail span wrong, head+type correct
    - type_error: spans correct, type wrong
    - head_tail_error: both spans wrong, type correct (or doesn't matter)
    - full_error: everything wrong (no partial match found)
    """
    pred_set = {(r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"])
                for r in pred_rels}
    gold_set = {(r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"])
                for r in gold_rels}
    fn_tuples = gold_set - pred_set

    counts = Counter()

    for g_hs, g_he, g_ts, g_te, g_type in fn_tuples:
        # Check if any pred has partial match
        best_match = "full_error"
        for p_hs, p_he, p_ts, p_te, p_type in pred_set:
            head_ok = (p_hs == g_hs and p_he == g_he)
            tail_ok = (p_ts == g_ts and p_te == g_te)
            type_ok = (p_type == g_type)

            if head_ok and tail_ok and not type_ok:
                best_match = "type_error"
                break
            elif head_ok and not tail_ok and type_ok:
                best_match = "tail_error"
                break
            elif not head_ok and tail_ok and type_ok:
                best_match = "head_error"
                break
            elif head_ok and not tail_ok and not type_ok:
                if best_match == "full_error":
                    best_match = "tail_type_error"
            elif not head_ok and tail_ok and not type_ok:
                if best_match == "full_error":
                    best_match = "head_type_error"
            elif not head_ok and not tail_ok and type_ok:
                if best_match == "full_error":
                    best_match = "head_tail_error"

        counts[best_match] += 1

    return dict(counts)


def error_propagation_analysis(data):
    """Analyze error patterns in greedy RE predictions."""
    total_errors = Counter()
    per_type_errors = defaultdict(Counter)
    consistency_by_error = defaultdict(list)

    for inst in data:
        gold_rels = inst["gold"]["relations"]
        pred_rels = inst["greedy"]["relations"]
        if not gold_rels:
            continue

        errors = classify_re_errors(pred_rels, gold_rels)
        for etype, cnt in errors.items():
            total_errors[etype] += cnt

        # Per relation type
        for rtype in {r["type"] for r in gold_rels}:
            type_gold = [r for r in gold_rels if r["type"] == rtype]
            type_pred = [r for r in pred_rels if r["type"] == rtype]
            type_errors = classify_re_errors(type_pred, type_gold)
            for etype, cnt in type_errors.items():
                per_type_errors[rtype][etype] += cnt

        # Consistency of instances grouped by dominant error type
        dominant = max(errors, key=errors.get) if errors else None
        if dominant:
            sj = re_sj_instance(inst["samples"])
            consistency_by_error[dominant].append(sj)

    # Total error distribution
    total_fn = sum(total_errors.values())
    error_dist = {k: {"count": v, "pct": round(100 * v / total_fn, 2) if total_fn > 0 else 0}
                  for k, v in total_errors.most_common()}

    # Per-type error distribution
    per_type_dist = {}
    for rtype, errs in sorted(per_type_errors.items()):
        t_total = sum(errs.values())
        per_type_dist[rtype] = {k: {"count": v, "pct": round(100 * v / t_total, 2) if t_total > 0 else 0}
                                for k, v in errs.most_common()}

    # Consistency by error type
    consistency_summary = {}
    for etype, sj_vals in sorted(consistency_by_error.items()):
        consistency_summary[etype] = {
            "n_instances": len(sj_vals),
            "mean_sj": round(float(np.mean(sj_vals)), 4),
            "std_sj": round(float(np.std(sj_vals)), 4),
        }

    return {
        "total_fn": total_fn,
        "error_distribution": error_dist,
        "per_relation_type_errors": per_type_dist,
        "consistency_by_dominant_error": consistency_summary,
    }


# ── 3. Threshold sensitivity ──────────────────────────────────────────

def threshold_sensitivity(data, thresholds=None):
    """Vary the exclusion threshold on greedy F1 and measure rho_sj and rho_voting."""
    if thresholds is None:
        thresholds = [round(x * 0.05, 2) for x in range(11)]  # 0.0 to 0.5

    # Pre-compute per-instance scores
    instances = []
    for inst in data:
        if not inst["gold"]["relations"]:
            continue
        greedy_f1 = instance_f1(inst["greedy"], inst["gold"], "re")
        sj = re_sj_instance(inst["samples"])
        fk = fleiss_kappa_re(inst["samples"])
        vc = voting_confidence_re(inst["samples"])

        # Also compute sample-level: any sample F1 > 0?
        sample_f1s = [instance_f1(s, inst["gold"], "re") for s in inst["samples"]]
        max_sample_f1 = max(sample_f1s) if sample_f1s else 0.0

        instances.append({
            "greedy_f1": greedy_f1,
            "max_sample_f1": max_sample_f1,
            "sj": sj,
            "fk": fk,
            "vc": vc,
        })

    results = []
    for thr in thresholds:
        # Exclude instances where greedy_f1 <= threshold
        subset = [x for x in instances if x["greedy_f1"] > thr]

        n = len(subset)
        if n < 5:
            results.append({"threshold": thr, "n": n, "rho_sj": None, "rho_fk": None, "rho_voting": None})
            continue

        sj_vals = [x["sj"] for x in subset]
        fk_vals = [x["fk"] for x in subset]
        vc_vals = [x["vc"] for x in subset]
        f1_vals = [x["greedy_f1"] for x in subset]

        rho_sj = float(spearmanr(sj_vals, f1_vals).statistic)
        rho_fk = float(spearmanr(fk_vals, f1_vals).statistic)
        rho_vc = float(spearmanr(vc_vals, f1_vals).statistic)

        results.append({
            "threshold": thr,
            "n": n,
            "rho_sj": round(rho_sj, 4),
            "rho_fk": round(rho_fk, 4),
            "rho_voting": round(rho_vc, 4),
        })

    return results


# ── 4. Bootstrap CI ───────────────────────────────────────────────────

def bootstrap_ci(scores_a, scores_b, n_boot=1000, alpha=0.05, seed=42):
    """Bootstrap 95% CI for Spearman rho."""
    rng = np.random.RandomState(seed)
    n = len(scores_a)
    assert n == len(scores_b)
    rhos = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        a_boot = [scores_a[i] for i in idx]
        b_boot = [scores_b[i] for i in idx]
        r = spearmanr(a_boot, b_boot).statistic
        if not np.isnan(r):
            rhos.append(float(r))
    rhos.sort()
    lo = np.percentile(rhos, 100 * alpha / 2)
    hi = np.percentile(rhos, 100 * (1 - alpha / 2))
    return {
        "rho_point": round(float(spearmanr(scores_a, scores_b).statistic), 4),
        "ci_lo": round(float(lo), 4),
        "ci_hi": round(float(hi), 4),
        "n_boot": n_boot,
        "n": n,
    }


def compute_bootstrap_cis(data):
    """Compute bootstrap CI for key rho values on both NER and RE."""
    # Separate NER and RE instances
    ner_insts = [d for d in data if d["gold"]["entities"]]
    re_insts = [d for d in data if d["gold"]["relations"]]

    results = {}

    # NER
    ner_sj = [ner_sj_instance(inst["samples"]) for inst in ner_insts]
    ner_fk = [fleiss_kappa_ner(inst["samples"]) for inst in ner_insts]
    ner_vc = [voting_confidence_ner(inst["samples"]) for inst in ner_insts]
    ner_f1 = [instance_f1(inst["greedy"], inst["gold"], "ner") for inst in ner_insts]

    results["ner_sj"] = bootstrap_ci(ner_sj, ner_f1)
    results["ner_fk"] = bootstrap_ci(ner_fk, ner_f1)
    results["ner_voting_conf"] = bootstrap_ci(ner_vc, ner_f1)

    # RE
    re_sj_scores = [re_sj_instance(inst["samples"]) for inst in re_insts]
    re_fk_scores = [fleiss_kappa_re(inst["samples"]) for inst in re_insts]
    re_vc_scores = [voting_confidence_re(inst["samples"]) for inst in re_insts]
    re_f1_scores = [instance_f1(inst["greedy"], inst["gold"], "re") for inst in re_insts]

    results["re_sj"] = bootstrap_ci(re_sj_scores, re_f1_scores)
    results["re_fk"] = bootstrap_ci(re_fk_scores, re_f1_scores)
    results["re_voting_conf"] = bootstrap_ci(re_vc_scores, re_f1_scores)

    # Conditional RE (exclude greedy_F1=0 instances)
    re_cond = [inst for inst in re_insts if instance_f1(inst["greedy"], inst["gold"], "re") > 0]

    if len(re_cond) >= 10:
        cond_sj = [re_sj_instance(inst["samples"]) for inst in re_cond]
        cond_fk = [fleiss_kappa_re(inst["samples"]) for inst in re_cond]
        cond_vc = [voting_confidence_re(inst["samples"]) for inst in re_cond]
        cond_f1 = [instance_f1(inst["greedy"], inst["gold"], "re") for inst in re_cond]

        results["re_cond_sj"] = bootstrap_ci(cond_sj, cond_f1)
        results["re_cond_fk"] = bootstrap_ci(cond_fk, cond_f1)
        results["re_cond_voting_conf"] = bootstrap_ci(cond_vc, cond_f1)

    return results


# ── 5. NER vs RE comparison (Fisher z-transform) ────────────────────────

def fisher_z_test(r1, n1, r2, n2):
    """Two-sided Fisher z-test for comparing two Spearman correlations."""
    z1 = np.arctanh(r1)
    z2 = np.arctanh(r2)
    se = np.sqrt(1 / (n1 - 3) + 1 / (n2 - 3))
    z_diff = (z1 - z2) / se
    p = 2 * (1 - norm.cdf(abs(z_diff)))
    return {
        "z1": round(float(z1), 4),
        "z2": round(float(z2), 4),
        "z_diff": round(float(z_diff), 4),
        "p_value": float(f"{p:.4e}"),
        "significant_005": bool(p < 0.05),
    }


def ner_vs_re_comparison(data):
    """Statistical comparison of NER vs RE correlation strengths."""
    ner_insts = [d for d in data if d["gold"]["entities"]]
    re_insts = [d for d in data if d["gold"]["relations"]]

    # NER scores
    ner_sj = [ner_sj_instance(inst["samples"]) for inst in ner_insts]
    ner_fk = [fleiss_kappa_ner(inst["samples"]) for inst in ner_insts]
    ner_vc = [voting_confidence_ner(inst["samples"]) for inst in ner_insts]
    ner_f1 = [instance_f1(inst["greedy"], inst["gold"], "ner") for inst in ner_insts]

    rho_ner_sj = float(spearmanr(ner_sj, ner_f1).statistic)
    rho_ner_fk = float(spearmanr(ner_fk, ner_f1).statistic)
    rho_ner_vc = float(spearmanr(ner_vc, ner_f1).statistic)

    # RE scores
    re_sj_scores = [re_sj_instance(inst["samples"]) for inst in re_insts]
    re_fk_scores = [fleiss_kappa_re(inst["samples"]) for inst in re_insts]
    re_vc_scores = [voting_confidence_re(inst["samples"]) for inst in re_insts]
    re_f1_scores = [instance_f1(inst["greedy"], inst["gold"], "re") for inst in re_insts]

    rho_re_sj = float(spearmanr(re_sj_scores, re_f1_scores).statistic)
    rho_re_fk = float(spearmanr(re_fk_scores, re_f1_scores).statistic)
    rho_re_vc = float(spearmanr(re_vc_scores, re_f1_scores).statistic)

    n_ner = len(ner_insts)
    n_re = len(re_insts)

    results = {
        "ner_n": n_ner,
        "re_n": n_re,
        "comparisons": {
            "sj": {
                "ner_rho": round(rho_ner_sj, 4),
                "re_rho": round(rho_re_sj, 4),
                "delta": round(rho_ner_sj - rho_re_sj, 4),
                **fisher_z_test(rho_ner_sj, n_ner, rho_re_sj, n_re),
            },
            "fk": {
                "ner_rho": round(rho_ner_fk, 4),
                "re_rho": round(rho_re_fk, 4),
                "delta": round(rho_ner_fk - rho_re_fk, 4),
                **fisher_z_test(rho_ner_fk, n_ner, rho_re_fk, n_re),
            },
            "voting_conf": {
                "ner_rho": round(rho_ner_vc, 4),
                "re_rho": round(rho_re_vc, 4),
                "delta": round(rho_ner_vc - rho_re_vc, 4),
                **fisher_z_test(rho_ner_vc, n_ner, rho_re_vc, n_re),
            },
        },
    }

    return results


# ── main ────────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    print(f"Loading pilot_004 data from {PILOT_004} ...")
    data = load_samples(PILOT_004)
    print(f"  {len(data)} instances loaded")

    # 1. Per-relation-type breakdown
    print("\n[1/5] Per-relation-type consistency breakdown ...")
    rt_results = per_relation_type_breakdown(data)
    with open(OUT_DIR / "per_relation_type.json", "w") as f:
        json.dump(rt_results, f, indent=2)
    for rtype, res in sorted(rt_results.items()):
        print(f"  {rtype:15s}  n={res['n_instances']:3d}  F1={res['mean_greedy_f1']:.3f}  "
              f"ρ_sj={res['rho_sj']:+.3f}  ρ_fk={res['rho_fk']:+.3f}  ρ_vc={res['rho_voting_conf']:+.3f}")

    # 2. Error propagation
    print("\n[2/5] Error propagation analysis ...")
    err_results = error_propagation_analysis(data)
    with open(OUT_DIR / "error_propagation.json", "w") as f:
        json.dump(err_results, f, indent=2)
    print(f"  Total FN: {err_results['total_fn']}")
    for etype, info in err_results["error_distribution"].items():
        print(f"  {etype:20s}  {info['count']:4d}  ({info['pct']:.1f}%)")
    print("  Consistency by dominant error:")
    for etype, info in err_results["consistency_by_dominant_error"].items():
        print(f"    {etype:20s}  n={info['n_instances']:3d}  mean_sj={info['mean_sj']:.3f}")

    # 3. Threshold sensitivity
    print("\n[3/5] Threshold sensitivity analysis ...")
    thr_results = threshold_sensitivity(data)
    with open(OUT_DIR / "threshold_sensitivity.json", "w") as f:
        json.dump(thr_results, f, indent=2)
    print(f"  {'thr':>5s}  {'n':>4s}  {'ρ_sj':>7s}  {'ρ_fk':>7s}  {'ρ_vc':>7s}")
    for r in thr_results:
        sj = f"{r['rho_sj']:+.4f}" if r["rho_sj"] is not None else "   N/A"
        fk = f"{r['rho_fk']:+.4f}" if r["rho_fk"] is not None else "   N/A"
        vc = f"{r['rho_voting']:+.4f}" if r["rho_voting"] is not None else "   N/A"
        print(f"  {r['threshold']:5.2f}  {r['n']:4d}  {sj}  {fk}  {vc}")

    # 4. Bootstrap CI
    print("\n[4/5] Bootstrap confidence intervals (1000 resamples) ...")
    boot_results = compute_bootstrap_cis(data)
    with open(OUT_DIR / "bootstrap_ci.json", "w") as f:
        json.dump(boot_results, f, indent=2)
    for metric, ci in boot_results.items():
        print(f"  {metric:25s}  ρ={ci['rho_point']:+.4f}  95%CI=[{ci['ci_lo']:+.4f}, {ci['ci_hi']:+.4f}]  n={ci['n']}")

    # 5. NER vs RE comparison
    print("\n[5/5] NER vs RE statistical comparison (Fisher z-transform) ...")
    comp_results = ner_vs_re_comparison(data)
    with open(OUT_DIR / "ner_vs_re_comparison.json", "w") as f:
        json.dump(comp_results, f, indent=2)
    for metric, res in comp_results["comparisons"].items():
        sig = "*" if res["significant_005"] else ""
        print(f"  {metric:15s}  NER={res['ner_rho']:+.4f}  RE={res['re_rho']:+.4f}  "
              f"Δ={res['delta']:+.4f}  z={res['z_diff']:+.3f}  p={res['p_value']:.4e} {sig}")

    print(f"\nAll results saved to {OUT_DIR}/")


if __name__ == "__main__":
    main()
