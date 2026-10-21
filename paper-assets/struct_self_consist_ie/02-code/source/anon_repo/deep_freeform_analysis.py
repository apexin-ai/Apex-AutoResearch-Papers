"""Deep analysis of constrained vs free-form decoding ablation.

Focuses on:
1. RE LP Selection Flip: why LP selection fails for RE in constrained but works in free-form
2. Non-Tied Subset Overlap: how the tied/non-tied instance sets differ between conditions
"""

from __future__ import annotations
import json
import os
import sys
import numpy as np
from collections import Counter, defaultdict
from scipy.stats import spearmanr, mannwhitneyu

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "code"))
from evaluation import per_instance_f1, entity_strict_match, relation_strict_match

CONSTRAINED_PATH = "output/exp_012_rerun_1024/samples.jsonl"
FREEFORM_PATH = "results/exp_freeform_ablation/samples.jsonl"

def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]

def safe_spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    x, y = x[m], y[m]
    if len(x) < 3:
        return float("nan"), float("nan")
    r = spearmanr(x, y)
    return float(r.statistic), float(r.pvalue)

# ============================================================
# Section: LP Selection Gap computation
# ============================================================

def compute_lp_selection(data, subtask="ner"):
    """For each instance: pick sample with highest mean_logprob, compute its F1.
    Compare to greedy F1. Return per-instance (lp_selected_f1, greedy_f1)."""
    lp_f1s = []
    greedy_f1s = []
    for inst in data:
        gold = inst["gold"]
        samples = inst.get("samples", [])
        lps = inst.get("logprobs", [])
        if not samples or not lps:
            continue
        # LP selection: pick sample with highest mean logprob
        best_idx = int(np.argmax(lps))
        lp_sel = samples[best_idx]
        lp_f1 = per_instance_f1(lp_sel, gold, subtask)
        greedy_f1 = per_instance_f1(inst["greedy"], gold, subtask)
        lp_f1s.append(lp_f1)
        greedy_f1s.append(greedy_f1)
    return np.array(lp_f1s), np.array(greedy_f1s)

def lp_selection_gap(data, subtask="ner"):
    lp_f1s, greedy_f1s = compute_lp_selection(data, subtask)
    return float(np.mean(lp_f1s) - np.mean(greedy_f1s)) * 100

# ============================================================
# Analysis 1: RE LP Selection Flip
# ============================================================

def get_relation_types_per_instance(data):
    """For each instance, return the set of gold relation types."""
    result = []
    for inst in data:
        gold_rels = inst["gold"].get("relations", [])
        types = [r["type"] for r in gold_rels]
        result.append(types)
    return result

def per_relation_type_lp_gap(data_c, data_f):
    """Compute LP selection gap by relation type.
    For instances that have a given relation type, compute the LP selection gap."""
    all_rel_types = set()
    for inst in data_c:
        for r in inst["gold"].get("relations", []):
            all_rel_types.add(r["type"])

    results = {}
    for rtype in sorted(all_rel_types):
        # Filter instances with this relation type
        for label, data in [("constrained", data_c), ("freeform", data_f)]:
            indices = [i for i, inst in enumerate(data)
                       if any(r["type"] == rtype for r in inst["gold"].get("relations", []))]
            if not indices:
                results.setdefault(rtype, {})[label] = {"gap": float("nan"), "n": 0}
                continue
            subset = [data[i] for i in indices]
            lp_f1s, greedy_f1s = compute_lp_selection(subset, "re")
            gap = float(np.mean(lp_f1s) - np.mean(greedy_f1s)) * 100
            results.setdefault(rtype, {})[label] = {
                "gap": gap,
                "n": len(indices),
                "lp_mean_f1": float(np.mean(lp_f1s)) * 100,
                "greedy_mean_f1": float(np.mean(greedy_f1s)) * 100,
            }
    return results

def lp_f1_correlation_by_subtask(data):
    """Per-instance correlation between mean_logprob (of LP-selected sample) and F1 for NER and RE."""
    ner_f1s = []
    re_f1s = []
    lps = []
    for inst in data:
        gold = inst["gold"]
        samples = inst.get("samples", [])
        logprobs = inst.get("logprobs", [])
        if not samples or not logprobs:
            continue
        best_idx = int(np.argmax(logprobs))
        lps.append(logprobs[best_idx])
        ner_f1s.append(per_instance_f1(samples[best_idx], gold, "ner"))
        re_f1s.append(per_instance_f1(samples[best_idx], gold, "re"))
    rho_ner, p_ner = safe_spearman(lps, ner_f1s)
    rho_re, p_re = safe_spearman(lps, re_f1s)
    return {
        "ner": {"rho": rho_ner, "p": p_ner},
        "re": {"rho": rho_re, "p": p_re},
    }

def lp_variance_analysis(data):
    """Per-instance LP variance. Also compute correlation of LP std with NER/RE F1 range."""
    lp_stds = []
    lp_ranges = []
    ner_f1_ranges = []
    re_f1_ranges = []
    for inst in data:
        gold = inst["gold"]
        samples = inst.get("samples", [])
        logprobs = inst.get("logprobs", [])
        if not samples or len(logprobs) < 2:
            continue
        lp_stds.append(float(np.std(logprobs)))
        lp_ranges.append(float(np.max(logprobs) - np.min(logprobs)))
        ner_f1s = [per_instance_f1(s, gold, "ner") for s in samples]
        re_f1s = [per_instance_f1(s, gold, "re") for s in samples]
        ner_f1_ranges.append(max(ner_f1s) - min(ner_f1s))
        re_f1_ranges.append(max(re_f1s) - min(re_f1s))

    rho_ner, p_ner = safe_spearman(lp_stds, ner_f1_ranges)
    rho_re, p_re = safe_spearman(lp_stds, re_f1_ranges)
    return {
        "mean_lp_std": float(np.mean(lp_stds)),
        "mean_lp_range": float(np.mean(lp_ranges)),
        "lp_std_vs_ner_f1_range": {"rho": rho_ner, "p": p_ner},
        "lp_std_vs_re_f1_range": {"rho": rho_re, "p": p_re},
    }

def instance_level_flip_analysis(data_c, data_f):
    """Find instances where LP selection:
    - WRONG in constrained (LP-sel RE F1 < greedy RE F1)
    - RIGHT in free-form (LP-sel RE F1 >= greedy RE F1)
    Analyze their characteristics."""
    assert len(data_c) == len(data_f)

    flip_ids = []
    flip_stats = []
    all_stats = {"constrained_wrong_freeform_right": [], "other": []}

    for i in range(len(data_c)):
        ic, if_ = data_c[i], data_f[i]
        assert ic["id"] == if_["id"], f"ID mismatch: {ic['id']} vs {if_['id']}"

        gold = ic["gold"]
        # Constrained
        lps_c = ic.get("logprobs", [])
        samples_c = ic.get("samples", [])
        if not lps_c or not samples_c:
            continue
        best_c = int(np.argmax(lps_c))
        lp_re_f1_c = per_instance_f1(samples_c[best_c], gold, "re")
        greedy_re_f1_c = per_instance_f1(ic["greedy"], gold, "re")

        # Free-form
        lps_f = if_.get("logprobs", [])
        samples_f = if_.get("samples", [])
        if not lps_f or not samples_f:
            continue
        best_f = int(np.argmax(lps_f))
        lp_re_f1_f = per_instance_f1(samples_f[best_f], gold, "re")
        greedy_re_f1_f = per_instance_f1(if_["greedy"], gold, "re")

        n_gold_rels = len(gold.get("relations", []))
        n_gold_ents = len(gold.get("entities", []))
        avg_output_len_c = float(np.mean([s.get("n_tokens", 0) for s in samples_c])) if samples_c else 0
        avg_output_len_f = float(np.mean([s.get("n_tokens", 0) for s in samples_f])) if samples_f else 0

        # NER F1 of LP-selected
        lp_ner_f1_c = per_instance_f1(samples_c[best_c], gold, "ner")
        lp_ner_f1_f = per_instance_f1(samples_f[best_f], gold, "ner")

        stat = {
            "id": ic["id"],
            "n_gold_rels": n_gold_rels,
            "n_gold_ents": n_gold_ents,
            "lp_re_f1_c": lp_re_f1_c,
            "greedy_re_f1_c": greedy_re_f1_c,
            "lp_re_f1_f": lp_re_f1_f,
            "greedy_re_f1_f": greedy_re_f1_f,
            "lp_ner_f1_c": lp_ner_f1_c,
            "lp_ner_f1_f": lp_ner_f1_f,
            "avg_output_len_c": avg_output_len_c,
            "avg_output_len_f": avg_output_len_f,
            "lp_std_c": float(np.std(lps_c)),
            "lp_std_f": float(np.std(lps_f)),
            "lp_range_c": float(np.max(lps_c) - np.min(lps_c)),
            "lp_range_f": float(np.max(lps_f) - np.min(lps_f)),
            "rel_types": list(set(r["type"] for r in gold.get("relations", []))),
        }

        c_wrong = lp_re_f1_c < greedy_re_f1_c
        f_right = lp_re_f1_f >= greedy_re_f1_f

        if c_wrong and f_right:
            flip_ids.append(ic["id"])
            flip_stats.append(stat)
            all_stats["constrained_wrong_freeform_right"].append(stat)
        else:
            all_stats["other"].append(stat)

    # Summarize flip characteristics
    if flip_stats:
        summary = {
            "n_flip": len(flip_stats),
            "n_total": len(data_c),
            "mean_n_gold_rels": float(np.mean([s["n_gold_rels"] for s in flip_stats])),
            "mean_n_gold_ents": float(np.mean([s["n_gold_ents"] for s in flip_stats])),
            "mean_avg_output_len_c": float(np.mean([s["avg_output_len_c"] for s in flip_stats])),
            "mean_avg_output_len_f": float(np.mean([s["avg_output_len_f"] for s in flip_stats])),
            "mean_lp_std_c": float(np.mean([s["lp_std_c"] for s in flip_stats])),
            "mean_lp_std_f": float(np.mean([s["lp_std_f"] for s in flip_stats])),
            "mean_lp_range_c": float(np.mean([s["lp_range_c"] for s in flip_stats])),
            "mean_lp_range_f": float(np.mean([s["lp_range_f"] for s in flip_stats])),
            "mean_lp_ner_f1_c": float(np.mean([s["lp_ner_f1_c"] for s in flip_stats])),
            "mean_lp_ner_f1_f": float(np.mean([s["lp_ner_f1_f"] for s in flip_stats])),
            "rel_type_distribution": dict(Counter(
                t for s in flip_stats for t in s["rel_types"]
            )),
        }
    else:
        summary = {"n_flip": 0}

    # Also compute for "other" group for comparison
    other_stats = all_stats["other"]
    if other_stats:
        other_summary = {
            "n_other": len(other_stats),
            "mean_n_gold_rels": float(np.mean([s["n_gold_rels"] for s in other_stats])),
            "mean_n_gold_ents": float(np.mean([s["n_gold_ents"] for s in other_stats])),
            "mean_lp_std_c": float(np.mean([s["lp_std_c"] for s in other_stats])),
            "mean_lp_std_f": float(np.mean([s["lp_std_f"] for s in other_stats])),
            "mean_lp_range_c": float(np.mean([s["lp_range_c"] for s in other_stats])),
            "mean_lp_range_f": float(np.mean([s["lp_range_f"] for s in other_stats])),
        }
    else:
        other_summary = {}

    return {"flip_summary": summary, "other_summary": other_summary, "flip_ids": flip_ids}

def hypothesis_test_lp_variance_re_difficult(data_c, data_f):
    """Test: free-form LP within-instance variance on RE-difficult instances
    vs RE-easy instances.
    RE-difficult = instances where greedy RE F1 < median greedy RE F1."""

    greedy_re_f1s = []
    lp_std_c_all = []
    lp_std_f_all = []

    for i in range(len(data_c)):
        ic, if_ = data_c[i], data_f[i]
        gold = ic["gold"]
        if not gold.get("relations"):
            continue
        greedy_re_f1 = per_instance_f1(ic["greedy"], gold, "re")
        greedy_re_f1s.append(greedy_re_f1)
        lps_c = ic.get("logprobs", [])
        lps_f = if_.get("logprobs", [])
        lp_std_c_all.append(float(np.std(lps_c)) if len(lps_c) >= 2 else 0)
        lp_std_f_all.append(float(np.std(lps_f)) if len(lps_f) >= 2 else 0)

    greedy_re_f1s = np.array(greedy_re_f1s)
    lp_std_c_all = np.array(lp_std_c_all)
    lp_std_f_all = np.array(lp_std_f_all)

    median_f1 = float(np.median(greedy_re_f1s))
    difficult = greedy_re_f1s < median_f1
    easy = greedy_re_f1s >= median_f1

    result = {
        "median_greedy_re_f1": median_f1,
        "n_difficult": int(difficult.sum()),
        "n_easy": int(easy.sum()),
    }

    # Constrained LP std: difficult vs easy
    result["constrained_lp_std_difficult"] = float(np.mean(lp_std_c_all[difficult]))
    result["constrained_lp_std_easy"] = float(np.mean(lp_std_c_all[easy]))

    # Free-form LP std: difficult vs easy
    result["freeform_lp_std_difficult"] = float(np.mean(lp_std_f_all[difficult]))
    result["freeform_lp_std_easy"] = float(np.mean(lp_std_f_all[easy]))

    # Mann-Whitney U test: is freeform LP std higher on difficult instances?
    if difficult.sum() > 0 and easy.sum() > 0:
        u_f, p_f = mannwhitneyu(lp_std_f_all[difficult], lp_std_f_all[easy], alternative="greater")
        u_c, p_c = mannwhitneyu(lp_std_c_all[difficult], lp_std_c_all[easy], alternative="greater")
        result["freeform_mannwhitney_U"] = float(u_f)
        result["freeform_mannwhitney_p"] = float(p_f)
        result["constrained_mannwhitney_U"] = float(u_c)
        result["constrained_mannwhitney_p"] = float(p_c)

    # Also: ratio of freeform/constrained LP std on difficult vs easy
    if result["constrained_lp_std_difficult"] > 0:
        result["ratio_f_c_difficult"] = result["freeform_lp_std_difficult"] / result["constrained_lp_std_difficult"]
    if result["constrained_lp_std_easy"] > 0:
        result["ratio_f_c_easy"] = result["freeform_lp_std_easy"] / result["constrained_lp_std_easy"]

    return result

# ============================================================
# Analysis 2: Non-Tied Subset Overlap
# ============================================================

def compute_tied_nontied(data, threshold=0.05):
    """Return sets of instance IDs that are tied vs non-tied based on LP range."""
    tied = set()
    nontied = set()
    lp_ranges = {}
    for inst in data:
        lps = inst.get("logprobs", [])
        if len(lps) < 2:
            tied.add(inst["id"])
            lp_ranges[inst["id"]] = 0.0
            continue
        lr = float(np.max(lps) - np.min(lps))
        lp_ranges[inst["id"]] = lr
        if lr < threshold:
            tied.add(inst["id"])
        else:
            nontied.add(inst["id"])
    return tied, nontied, lp_ranges

def nontied_overlap_analysis(data_c, data_f):
    tied_c, nontied_c, ranges_c = compute_tied_nontied(data_c)
    tied_f, nontied_f, ranges_f = compute_tied_nontied(data_f)

    intersection = nontied_c & nontied_f
    union = nontied_c | nontied_f
    jaccard = len(intersection) / len(union) if union else 0.0

    # New non-tied in free-form (were tied in constrained)
    new_nontied = nontied_f - nontied_c
    # Lost non-tied (were non-tied in constrained, now tied in free-form)
    lost_nontied = nontied_c - nontied_f

    result = {
        "n_total": len(data_c),
        "constrained_tied": len(tied_c),
        "constrained_nontied": len(nontied_c),
        "freeform_tied": len(tied_f),
        "freeform_nontied": len(nontied_f),
        "constrained_tied_frac": len(tied_c) / len(data_c) * 100,
        "freeform_tied_frac": len(tied_f) / len(data_f) * 100,
        "jaccard_similarity": jaccard,
        "intersection_size": len(intersection),
        "union_size": len(union),
        "new_nontied_in_freeform": len(new_nontied),
        "lost_nontied_in_freeform": len(lost_nontied),
    }

    return result, new_nontied, lost_nontied, ranges_c, ranges_f

def characterize_instance_set(ids, data_c, data_f, ranges_c, ranges_f):
    """Characterize a set of instances by their gold stats, LP ranges, F1s."""
    id_to_c = {inst["id"]: inst for inst in data_c}
    id_to_f = {inst["id"]: inst for inst in data_f}

    stats = []
    for iid in ids:
        ic = id_to_c.get(iid)
        if_ = id_to_f.get(iid)
        if not ic or not if_:
            continue
        gold = ic["gold"]
        stats.append({
            "n_gold_rels": len(gold.get("relations", [])),
            "n_gold_ents": len(gold.get("entities", [])),
            "has_relations": len(gold.get("relations", [])) > 0,
            "lp_range_c": ranges_c.get(iid, 0),
            "lp_range_f": ranges_f.get(iid, 0),
            "greedy_ner_f1_c": per_instance_f1(ic["greedy"], gold, "ner"),
            "greedy_re_f1_c": per_instance_f1(ic["greedy"], gold, "re") if gold.get("relations") else None,
            "n_tokens_c": float(np.mean([s.get("n_tokens", 0) for s in ic.get("samples", [])])),
            "n_tokens_f": float(np.mean([s.get("n_tokens", 0) for s in if_.get("samples", [])])),
            "lp_std_c": float(np.std(ic.get("logprobs", [0]))),
            "lp_std_f": float(np.std(if_.get("logprobs", [0]))),
            "text_len": len(ic.get("text", "")),
        })

    if not stats:
        return {}

    return {
        "n": len(stats),
        "mean_n_gold_rels": float(np.mean([s["n_gold_rels"] for s in stats])),
        "mean_n_gold_ents": float(np.mean([s["n_gold_ents"] for s in stats])),
        "pct_has_relations": float(np.mean([s["has_relations"] for s in stats])) * 100,
        "mean_lp_range_c": float(np.mean([s["lp_range_c"] for s in stats])),
        "mean_lp_range_f": float(np.mean([s["lp_range_f"] for s in stats])),
        "mean_greedy_ner_f1": float(np.mean([s["greedy_ner_f1_c"] for s in stats])),
        "mean_greedy_re_f1": float(np.mean([s["greedy_re_f1_c"] for s in stats if s["greedy_re_f1_c"] is not None])) if any(s["greedy_re_f1_c"] is not None for s in stats) else None,
        "mean_n_tokens_c": float(np.mean([s["n_tokens_c"] for s in stats])),
        "mean_n_tokens_f": float(np.mean([s["n_tokens_f"] for s in stats])),
        "mean_lp_std_c": float(np.mean([s["lp_std_c"] for s in stats])),
        "mean_lp_std_f": float(np.mean([s["lp_std_f"] for s in stats])),
        "mean_text_len": float(np.mean([s["text_len"] for s in stats])),
    }

def lp_range_correlation(data_c, data_f):
    """Per-instance Spearman ρ between constrained and free-form LP range."""
    ranges_c = []
    ranges_f = []
    for ic, if_ in zip(data_c, data_f):
        lps_c = ic.get("logprobs", [])
        lps_f = if_.get("logprobs", [])
        if len(lps_c) < 2 or len(lps_f) < 2:
            continue
        ranges_c.append(float(np.max(lps_c) - np.min(lps_c)))
        ranges_f.append(float(np.max(lps_f) - np.min(lps_f)))
    rho, p = safe_spearman(ranges_c, ranges_f)
    return {
        "spearman_rho": rho,
        "p_value": p,
        "n": len(ranges_c),
        "mean_range_c": float(np.mean(ranges_c)),
        "mean_range_f": float(np.mean(ranges_f)),
    }

# ============================================================
# Additional: per-instance LP selection correctness for RE
# ============================================================

def per_instance_lp_selection_correctness(data, subtask="re"):
    """For each instance, is LP-selected F1 >= greedy F1?"""
    correct = 0
    wrong = 0
    tied = 0
    for inst in data:
        gold = inst["gold"]
        samples = inst.get("samples", [])
        lps = inst.get("logprobs", [])
        if not samples or not lps:
            continue
        if not gold.get("relations") and subtask == "re":
            continue
        best_idx = int(np.argmax(lps))
        lp_f1 = per_instance_f1(samples[best_idx], gold, subtask)
        greedy_f1 = per_instance_f1(inst["greedy"], gold, subtask)
        if lp_f1 > greedy_f1:
            correct += 1
        elif lp_f1 < greedy_f1:
            wrong += 1
        else:
            tied += 1
    return {"correct": correct, "wrong": wrong, "tied": tied,
            "total": correct + wrong + tied,
            "correct_pct": correct / (correct + wrong + tied) * 100 if (correct + wrong + tied) > 0 else 0,
            "wrong_pct": wrong / (correct + wrong + tied) * 100 if (correct + wrong + tied) > 0 else 0}

# ============================================================
# Main
# ============================================================

def main():
    os.chdir("/root/autodl-tmp/struct_self_consist_ie")
    data_c = load_data(CONSTRAINED_PATH)
    data_f = load_data(FREEFORM_PATH)
    print(f"Loaded {len(data_c)} constrained, {len(data_f)} free-form instances")

    # Verify ID alignment
    for i in range(len(data_c)):
        assert data_c[i]["id"] == data_f[i]["id"], f"Mismatch at {i}"

    results = {}

    # ---- Overall LP selection gaps ----
    print("\n=== Overall LP Selection Gaps ===")
    for subtask in ["ner", "re"]:
        gap_c = lp_selection_gap(data_c, subtask)
        gap_f = lp_selection_gap(data_f, subtask)
        print(f"{subtask.upper()}: constrained={gap_c:+.2f}pp, freeform={gap_f:+.2f}pp")
        results[f"overall_lp_gap_{subtask}"] = {"constrained": gap_c, "freeform": gap_f}

    # ---- Analysis 1.1: Per relation type LP gap ----
    print("\n=== Analysis 1.1: Per Relation Type LP Selection Gap ===")
    per_type = per_relation_type_lp_gap(data_c, data_f)
    results["per_relation_type_lp_gap"] = per_type
    print(f"{'Type':<20} {'N':>4} {'Constr Gap':>11} {'Free Gap':>11} {'Δ':>8}")
    print("-" * 60)
    for rtype in sorted(per_type.keys()):
        c = per_type[rtype].get("constrained", {})
        f = per_type[rtype].get("freeform", {})
        n = c.get("n", 0)
        gc = c.get("gap", float("nan"))
        gf = f.get("gap", float("nan"))
        delta = gf - gc if not (np.isnan(gc) or np.isnan(gf)) else float("nan")
        print(f"{rtype:<20} {n:>4} {gc:>+10.2f}% {gf:>+10.2f}% {delta:>+7.2f}%")

    # ---- Analysis 1.2: LP-F1 correlation by subtask ----
    print("\n=== Analysis 1.2: LP-F1 Correlation by Subtask ===")
    for label, data in [("constrained", data_c), ("freeform", data_f)]:
        corr = lp_f1_correlation_by_subtask(data)
        results[f"lp_f1_correlation_{label}"] = corr
        print(f"{label}: NER ρ={corr['ner']['rho']:.3f} (p={corr['ner']['p']:.3e}), "
              f"RE ρ={corr['re']['rho']:.3f} (p={corr['re']['p']:.3e})")

    # ---- Analysis 1.3: LP variance analysis ----
    print("\n=== Analysis 1.3: LP Variance Analysis ===")
    for label, data in [("constrained", data_c), ("freeform", data_f)]:
        va = lp_variance_analysis(data)
        results[f"lp_variance_{label}"] = va
        print(f"{label}: mean_lp_std={va['mean_lp_std']:.4f}, mean_lp_range={va['mean_lp_range']:.4f}")
        print(f"  LP_std vs NER_F1_range: ρ={va['lp_std_vs_ner_f1_range']['rho']:.3f}")
        print(f"  LP_std vs RE_F1_range: ρ={va['lp_std_vs_re_f1_range']['rho']:.3f}")

    # ---- Analysis 1.4: Instance-level flip analysis ----
    print("\n=== Analysis 1.4: Instance-Level Flip Analysis ===")
    flip = instance_level_flip_analysis(data_c, data_f)
    results["flip_analysis"] = flip
    fs = flip["flip_summary"]
    print(f"Flip instances (constrained wrong → freeform right): {fs['n_flip']} / {fs.get('n_total', len(data_c))}")
    if fs["n_flip"] > 0:
        print(f"  Mean gold rels: {fs['mean_n_gold_rels']:.1f}, Mean gold ents: {fs['mean_n_gold_ents']:.1f}")
        print(f"  Mean LP std: constrained={fs['mean_lp_std_c']:.4f}, freeform={fs['mean_lp_std_f']:.4f}")
        print(f"  Mean LP range: constrained={fs['mean_lp_range_c']:.4f}, freeform={fs['mean_lp_range_f']:.4f}")
        print(f"  Mean NER F1 of LP-sel: constrained={fs['mean_lp_ner_f1_c']:.3f}, freeform={fs['mean_lp_ner_f1_f']:.3f}")
        print(f"  Relation type distribution: {fs['rel_type_distribution']}")
        other_s = flip["other_summary"]
        print(f"  [Other instances] Mean LP std: c={other_s['mean_lp_std_c']:.4f}, f={other_s['mean_lp_std_f']:.4f}")
        print(f"  [Other instances] Mean LP range: c={other_s['mean_lp_range_c']:.4f}, f={other_s['mean_lp_range_f']:.4f}")

    # ---- Analysis 1.5: Hypothesis test ----
    print("\n=== Analysis 1.5: Hypothesis Test (LP Variance on RE-Difficult) ===")
    hyp = hypothesis_test_lp_variance_re_difficult(data_c, data_f)
    results["hypothesis_test"] = hyp
    print(f"Median greedy RE F1: {hyp['median_greedy_re_f1']:.3f}")
    print(f"N difficult: {hyp['n_difficult']}, N easy: {hyp['n_easy']}")
    print(f"Constrained LP std: difficult={hyp['constrained_lp_std_difficult']:.4f}, easy={hyp['constrained_lp_std_easy']:.4f}")
    print(f"Free-form LP std: difficult={hyp['freeform_lp_std_difficult']:.4f}, easy={hyp['freeform_lp_std_easy']:.4f}")
    if "freeform_mannwhitney_p" in hyp:
        print(f"Mann-Whitney (free-form, difficult > easy): U={hyp['freeform_mannwhitney_U']:.0f}, p={hyp['freeform_mannwhitney_p']:.4f}")
        print(f"Mann-Whitney (constrained, difficult > easy): U={hyp['constrained_mannwhitney_U']:.0f}, p={hyp['constrained_mannwhitney_p']:.4f}")
    if "ratio_f_c_difficult" in hyp:
        print(f"Freeform/Constrained LP std ratio: difficult={hyp['ratio_f_c_difficult']:.2f}, easy={hyp.get('ratio_f_c_easy', 0):.2f}")

    # ---- Per-instance LP selection correctness ----
    print("\n=== Per-instance LP Selection Correctness (RE) ===")
    for label, data in [("constrained", data_c), ("freeform", data_f)]:
        corr = per_instance_lp_selection_correctness(data, "re")
        results[f"lp_selection_correctness_re_{label}"] = corr
        print(f"{label}: correct={corr['correct']} ({corr['correct_pct']:.1f}%), "
              f"wrong={corr['wrong']} ({corr['wrong_pct']:.1f}%), tied={corr['tied']}")

    # ---- Analysis 2: Non-Tied Subset Overlap ----
    print("\n=== Analysis 2.1: Non-Tied Subset Overlap ===")
    overlap, new_nt, lost_nt, ranges_c, ranges_f = nontied_overlap_analysis(data_c, data_f)
    results["nontied_overlap"] = overlap
    print(f"Constrained: {overlap['constrained_nontied']} non-tied ({100-overlap['constrained_tied_frac']:.1f}%)")
    print(f"Free-form: {overlap['freeform_nontied']} non-tied ({100-overlap['freeform_tied_frac']:.1f}%)")
    print(f"Jaccard similarity: {overlap['jaccard_similarity']:.3f}")
    print(f"Intersection: {overlap['intersection_size']}, Union: {overlap['union_size']}")
    print(f"New non-tied in free-form: {overlap['new_nontied_in_freeform']}")
    print(f"Lost non-tied in free-form: {overlap['lost_nontied_in_freeform']}")

    # ---- Analysis 2.2-2.3: Characterize new/lost non-tied ----
    print("\n=== Analysis 2.2: New Non-Tied Instances (freeform non-tied, constrained tied) ===")
    new_char = characterize_instance_set(new_nt, data_c, data_f, ranges_c, ranges_f)
    results["new_nontied_characteristics"] = new_char
    if new_char:
        print(f"N: {new_char['n']}")
        print(f"  Mean gold rels: {new_char['mean_n_gold_rels']:.1f}, ents: {new_char['mean_n_gold_ents']:.1f}")
        print(f"  % with relations: {new_char['pct_has_relations']:.1f}%")
        print(f"  Mean LP range: c={new_char['mean_lp_range_c']:.4f}, f={new_char['mean_lp_range_f']:.4f}")
        print(f"  Mean greedy NER F1: {new_char['mean_greedy_ner_f1']:.3f}")
        if new_char.get("mean_greedy_re_f1") is not None:
            print(f"  Mean greedy RE F1: {new_char['mean_greedy_re_f1']:.3f}")
        print(f"  Mean tokens: c={new_char['mean_n_tokens_c']:.0f}, f={new_char['mean_n_tokens_f']:.0f}")
        print(f"  Mean text length: {new_char['mean_text_len']:.0f}")

    print("\n=== Analysis 2.3: Lost Non-Tied Instances (constrained non-tied, freeform tied) ===")
    lost_char = characterize_instance_set(lost_nt, data_c, data_f, ranges_c, ranges_f)
    results["lost_nontied_characteristics"] = lost_char
    if lost_char:
        print(f"N: {lost_char['n']}")
        print(f"  Mean gold rels: {lost_char['mean_n_gold_rels']:.1f}, ents: {lost_char['mean_n_gold_ents']:.1f}")
        print(f"  % with relations: {lost_char['pct_has_relations']:.1f}%")
        print(f"  Mean LP range: c={lost_char['mean_lp_range_c']:.4f}, f={lost_char['mean_lp_range_f']:.4f}")
        print(f"  Mean greedy NER F1: {lost_char['mean_greedy_ner_f1']:.3f}")
        if lost_char.get("mean_greedy_re_f1") is not None:
            print(f"  Mean greedy RE F1: {lost_char['mean_greedy_re_f1']:.3f}")
        print(f"  Mean tokens: c={lost_char['mean_n_tokens_c']:.0f}, f={lost_char['mean_n_tokens_f']:.0f}")
        print(f"  Mean text length: {lost_char['mean_text_len']:.0f}")

    # ---- Analysis 2.4: LP range correlation ----
    print("\n=== Analysis 2.4: LP Range Correlation ===")
    lr_corr = lp_range_correlation(data_c, data_f)
    results["lp_range_correlation"] = lr_corr
    print(f"Spearman ρ: {lr_corr['spearman_rho']:.3f} (p={lr_corr['p_value']:.3e})")
    print(f"Mean range: constrained={lr_corr['mean_range_c']:.4f}, freeform={lr_corr['mean_range_f']:.4f}")

    # ---- Characterize baseline (all instances) for comparison ----
    print("\n=== Baseline: All Instances ===")
    all_ids = {inst["id"] for inst in data_c}
    all_char = characterize_instance_set(all_ids, data_c, data_f, ranges_c, ranges_f)
    results["all_instances_characteristics"] = all_char
    if all_char:
        print(f"N: {all_char['n']}")
        print(f"  Mean gold rels: {all_char['mean_n_gold_rels']:.1f}, ents: {all_char['mean_n_gold_ents']:.1f}")
        print(f"  % with relations: {all_char['pct_has_relations']:.1f}%")
        print(f"  Mean LP range: c={all_char['mean_lp_range_c']:.4f}, f={all_char['mean_lp_range_f']:.4f}")
        print(f"  Mean greedy NER F1: {all_char['mean_greedy_ner_f1']:.3f}")

    # Save raw results
    out_path = "results/exp_freeform_ablation/deep_analysis_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")

if __name__ == "__main__":
    main()
