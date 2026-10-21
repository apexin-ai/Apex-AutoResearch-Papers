"""Diversity-stratified selection gap analysis for SciERC NER."""

import json
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.optimize import linear_sum_assignment


def _prf(tp, fp, fn):
    p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
    return f1


def per_instance_f1(pred, gold):
    pred_set = {(e["start"], e["end"], e["type"]) for e in pred.get("entities", [])}
    gold_set = {(e["start"], e["end"], e["type"]) for e in gold.get("entities", [])}
    tp = len(pred_set & gold_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    return _prf(tp, fp, fn)


def _span_soft_jaccard(s1_start, s1_end, s2_start, s2_end):
    overlap = max(0, min(s1_end, s2_end) - max(s1_start, s2_start))
    len1 = s1_end - s1_start
    len2 = s2_end - s2_start
    union = len1 + len2 - overlap
    if union <= 0:
        return 0.0
    return overlap / union


def _ner_soft_jaccard_pair(entities_a, entities_b):
    if not entities_a and not entities_b:
        return 1.0
    if not entities_a or not entities_b:
        return 0.0
    types = set()
    groups_a, groups_b = {}, {}
    for e in entities_a:
        t = e["type"]
        types.add(t)
        groups_a.setdefault(t, []).append(e)
    for e in entities_b:
        t = e["type"]
        types.add(t)
        groups_b.setdefault(t, []).append(e)
    total_score = 0.0
    total_weight = 0
    for t in types:
        ga = groups_a.get(t, [])
        gb = groups_b.get(t, [])
        denom = max(len(ga), len(gb))
        if denom == 0:
            continue
        total_weight += denom
        if not ga or not gb:
            continue
        cost = np.zeros((len(ga), len(gb)), dtype=np.float64)
        for i, ea in enumerate(ga):
            for j, eb in enumerate(gb):
                cost[i, j] = _span_soft_jaccard(ea["start"], ea["end"], eb["start"], eb["end"])
        row_ind, col_ind = linear_sum_assignment(-cost)
        total_score += cost[row_ind, col_ind].sum()
    if total_weight == 0:
        return 1.0
    return total_score / total_weight


def fleiss_kappa_surface(samples):
    n_raters = len(samples)
    if n_raters <= 1:
        return 1.0
    entity_sets = []
    all_keys = set()
    for sample in samples:
        keys = {(e["text"], e["type"]) for e in sample.get("entities", [])}
        entity_sets.append(keys)
        all_keys |= keys
    n_subjects = len(all_keys)
    if n_subjects <= 0:
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


def pairwise_signal_scores(samples, signal_fn):
    n = len(samples)
    scores = np.zeros(n)
    for i, j in combinations(range(n), 2):
        s = signal_fn(samples[i], samples[j])
        scores[i] += s
        scores[j] += s
    scores /= (n - 1)
    return scores


def select_by_sj(samples):
    def pair_fn(a, b):
        return _ner_soft_jaccard_pair(a.get("entities", []), b.get("entities", []))
    scores = pairwise_signal_scores(samples, pair_fn)
    return int(np.argmax(scores))


def select_by_fk(samples):
    def pair_fn(a, b):
        keys_a = {(e["text"], e["type"]) for e in a.get("entities", [])}
        keys_b = {(e["text"], e["type"]) for e in b.get("entities", [])}
        if not keys_a and not keys_b:
            return 1.0
        if not keys_a or not keys_b:
            return 0.0
        return len(keys_a & keys_b) / len(keys_a | keys_b)
    scores = pairwise_signal_scores(samples, pair_fn)
    return int(np.argmax(scores))


def select_by_em(samples):
    sample_keys = []
    for s in samples:
        key = frozenset((e["text"], e["type"]) for e in s.get("entities", []))
        sample_keys.append(key)
    counter = Counter(sample_keys)
    most_common_key = counter.most_common(1)[0][0]
    for i, k in enumerate(sample_keys):
        if k == most_common_key:
            return i
    return 0


def select_by_voting(samples):
    N = len(samples)
    counter = Counter()
    for s in samples:
        for e in s.get("entities", []):
            counter[(e["text"], e["type"])] += 1
    best_idx = 0
    best_score = -1
    for i, s in enumerate(samples):
        ents = s.get("entities", [])
        if not ents:
            score = 0.0
        else:
            score = sum(counter[(e["text"], e["type"])] / N for e in ents) / len(ents)
        if score > best_score:
            best_score = score
            best_idx = i
    return best_idx


def select_by_logprob(samples):
    best_idx = 0
    best_lp = -float("inf")
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob", -float("inf"))
        if lp > best_lp:
            best_lp = lp
            best_idx = i
    return best_idx


def compute_n_unique(samples):
    keys = set()
    for s in samples:
        k = frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
        keys.add(k)
    return len(keys)


def analyze_one_config(path, label):
    with open(path) as f:
        instances = [json.loads(line) for line in f if line.strip()]

    valid = [inst for inst in instances if len(inst["gold"].get("entities", [])) > 0]
    print("\n" + "=" * 60)
    print("Config: " + label)
    print("Total instances: %d, valid (gold non-empty): %d" % (len(instances), len(valid)))

    for inst in valid:
        inst["_n_unique"] = compute_n_unique(inst["samples"])

    strata_defs = [
        ("high_diversity", "n_unique >= 4", lambda n: n >= 4),
        ("medium", "n_unique == 3", lambda n: n == 3),
        ("low_diversity", "n_unique <= 2", lambda n: n <= 2),
    ]

    result = {"n_total_valid": len(valid), "strata": {}}

    for stratum_name, criterion, filter_fn in strata_defs:
        group = [inst for inst in valid if filter_fn(inst["_n_unique"])]
        n = len(group)
        print("\n  Stratum: %s (%s), n=%d" % (stratum_name, criterion, n))

        if n == 0:
            result["strata"][stratum_name] = {
                "criterion": criterion, "n": 0,
                "greedy_f1": None, "oracle_f1": None, "oracle_headroom": None,
                "signals": {}
            }
            continue

        greedy_f1s = []
        oracle_f1s = []
        for inst in group:
            g_f1 = per_instance_f1(inst["greedy"], inst["gold"])
            greedy_f1s.append(g_f1)
            o_f1 = max(per_instance_f1(s, inst["gold"]) for s in inst["samples"])
            oracle_f1s.append(o_f1)

        mean_greedy = float(np.mean(greedy_f1s))
        mean_oracle = float(np.mean(oracle_f1s))
        headroom = mean_oracle - mean_greedy

        print("    Greedy F1: %.4f" % mean_greedy)
        print("    Oracle F1: %.4f" % mean_oracle)
        print("    Oracle headroom: %.4f" % headroom)

        signal_selectors = [
            ("sj", select_by_sj),
            ("fk", select_by_fk),
            ("em", select_by_em),
            ("voting_conf", select_by_voting),
            ("logprob", select_by_logprob),
        ]

        signals_result = {}
        for sig_name, selector in signal_selectors:
            sel_f1s = []
            for inst in group:
                idx = selector(inst["samples"])
                sel_f1 = per_instance_f1(inst["samples"][idx], inst["gold"])
                sel_f1s.append(sel_f1)
            mean_sel = float(np.mean(sel_f1s))
            gap = mean_sel - mean_greedy
            signals_result[sig_name] = {
                "selection_f1": round(mean_sel, 4),
                "selection_gap": round(gap, 4),
            }
            print("    %s: sel_f1=%.4f, gap=%+.4f" % (sig_name, mean_sel, gap))

        result["strata"][stratum_name] = {
            "criterion": criterion,
            "n": n,
            "greedy_f1": round(mean_greedy, 4),
            "oracle_f1": round(mean_oracle, 4),
            "oracle_headroom": round(headroom, 4),
            "signals": signals_result,
        }

    return result


def main():
    configs = [
        ("qwen_scierc_ner", "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl"),
        ("llama_scierc_ner", "/root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference/samples.jsonl"),
    ]

    output = {}
    for label, path in configs:
        output[label] = analyze_one_config(path, label)

    output["ceiling_effect_note"] = (
        "CoNLL (57-88% identical outputs) and WNUT (low diversity) are ceiling-effect cases "
        "where low diversity is a natural consequence of near-perfect model performance, "
        "not constrained decoding. Their selection results should not be cited as independent "
        "evidence for the correlation-selection gap."
    )

    out_path = Path("/root/autodl-tmp/struct_self_consist_ie/output/review_round2/diversity_stratified_selection.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)

    print("\n\n" + "=" * 60)
    print("FULL JSON OUTPUT:")
    print("=" * 60)
    print(json.dumps(output, indent=2))

    print("\n" + "=" * 60)
    print("KEY FINDINGS:")
    print("=" * 60)
    for label in ["qwen_scierc_ner", "llama_scierc_ner"]:
        r = output[label]
        high = r["strata"]["high_diversity"]
        low = r["strata"]["low_diversity"]
        print("\n--- %s ---" % label)
        print("High-diversity (n=%d): oracle_headroom=%.4f" % (high["n"], high["oracle_headroom"]))
        gaps = ", ".join("%s=%+.4f" % (k, v["selection_gap"]) for k, v in high["signals"].items())
        print("  Signal gaps: " + gaps)
        print("Low-diversity (n=%d): oracle_headroom=%.4f" % (low["n"], low["oracle_headroom"]))
        gaps = ", ".join("%s=%+.4f" % (k, v["selection_gap"]) for k, v in low["signals"].items())
        print("  Signal gaps: " + gaps)

        all_gaps_near_zero = all(abs(v["selection_gap"]) < 0.02 for v in high["signals"].values())
        large_headroom = high["oracle_headroom"] > 0.05
        if large_headroom and all_gaps_near_zero:
            print("  => CONFIRMS: Large headroom + near-zero selection gaps in high-diversity group.")
            print("     Diversity exists, signals cannot exploit it. Constrained decoding confound EXCLUDED.")
        elif large_headroom:
            print("  => Headroom is large (%.4f), but some signals show non-trivial gaps." % high["oracle_headroom"])
        else:
            print("  => Headroom is small (%.4f), limited room for selection improvement." % high["oracle_headroom"])


if __name__ == "__main__":
    main()
