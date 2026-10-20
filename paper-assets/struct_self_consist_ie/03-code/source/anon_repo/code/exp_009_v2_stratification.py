#!/usr/bin/env python3
"""exp-009 v2: Capability Stratification Analysis using v2 unified inference data.

Uses independent difficulty proxy variables (sentence length, entity count,
entity type diversity) to avoid the circularity of greedy-F1-based stratification.
Greedy F1 buckets included as reference only.

Outputs:
  - output/exp_009_v2/results.json
  - output/exp_009_v2/ner_stratification.pdf
  - output/exp_009_v2/re_stratification.pdf
  - output/exp_009_v2/summary.txt
"""

import json
import sys
import os
import math
import numpy as np
from collections import Counter
from itertools import combinations
from scipy.stats import spearmanr
from scipy.optimize import linear_sum_assignment

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUTPUT_DIR = os.path.join(BASE, "output")
RESULT_DIR = os.path.join(OUTPUT_DIR, "exp_009_v2")
N_BOOTSTRAP = 2000
RNG = np.random.RandomState(42)
MIN_STRATUM_SIZE = 50

DATASETS = {
    "ner_seed42": {
        "path": os.path.join(OUTPUT_DIR, "exp_001_seed42_v2", "samples.jsonl"),
        "subtask": "ner",
    },
    "ner_seed123": {
        "path": os.path.join(OUTPUT_DIR, "exp_001_seed123_v2", "samples.jsonl"),
        "subtask": "ner",
    },
    "re_seed42": {
        "path": os.path.join(OUTPUT_DIR, "exp_008_re_n16_v2", "samples.jsonl"),
        "subtask": "re",
    },
}

SIGNALS = ["sj", "fk", "logprob", "voting_conf", "em"]
SIGNAL_LABELS = {
    "sj": "Soft Jaccard",
    "fk": "Fleiss' κ",
    "logprob": "Log-prob",
    "voting_conf": "Voting Conf",
    "em": "Exact Match",
}


# ── Evaluation helpers ──────────────────────────────────────────────

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
    else:
        tp, fp, fn = relation_strict_match(pred.get("relations", []), gold.get("relations", []))
    if tp + fp == 0 or tp + fn == 0:
        return 0.0 if tp == 0 else 1.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r) if (p + r) > 0 else 0.0


# ── Consistency signals ─────────────────────────────────────────────

def _extract_surface_keys(sample, subtask):
    if subtask == "ner":
        return frozenset((e["text"], e["type"]) for e in sample.get("entities", []))
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
    if not all_keys:
        return 1.0
    key_list = sorted(all_keys)
    n_subjects = len(key_list)
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


def _span_soft_jaccard(s1_start, s1_end, s2_start, s2_end):
    overlap = max(0, min(s1_end, s2_end) - max(s1_start, s2_start))
    union = (s1_end - s1_start) + (s2_end - s2_start) - overlap
    return overlap / union if union > 0 else 0.0


def _ner_soft_jaccard_pair(ents_a, ents_b):
    if not ents_a and not ents_b:
        return 1.0
    if not ents_a or not ents_b:
        return 0.0
    types = set(e["type"] for e in ents_a) | set(e["type"] for e in ents_b)
    ga, gb = {}, {}
    for e in ents_a:
        ga.setdefault(e["type"], []).append(e)
    for e in ents_b:
        gb.setdefault(e["type"], []).append(e)
    total_score, total_weight = 0.0, 0
    for t in types:
        a_list, b_list = ga.get(t, []), gb.get(t, [])
        denom = max(len(a_list), len(b_list))
        if denom == 0:
            continue
        total_weight += denom
        if not a_list or not b_list:
            continue
        cost = np.zeros((len(a_list), len(b_list)))
        for i, ea in enumerate(a_list):
            for j, eb in enumerate(b_list):
                cost[i, j] = _span_soft_jaccard(ea["start"], ea["end"], eb["start"], eb["end"])
        ri, ci = linear_sum_assignment(-cost)
        total_score += cost[ri, ci].sum()
    return total_score / total_weight if total_weight > 0 else 1.0


def _re_soft_jaccard_pair(rels_a, rels_b):
    if not rels_a and not rels_b:
        return 1.0
    if not rels_a or not rels_b:
        return 0.0
    cost = np.zeros((len(rels_a), len(rels_b)))
    for i, a in enumerate(rels_a):
        for j, b in enumerate(rels_b):
            if a["type"] != b["type"]:
                continue
            h = _span_soft_jaccard(a["head_start"], a["head_end"], b["head_start"], b["head_end"])
            t = _span_soft_jaccard(a["tail_start"], a["tail_end"], b["tail_start"], b["tail_end"])
            cost[i, j] = h * t
    ri, ci = linear_sum_assignment(-cost)
    return cost[ri, ci].sum() / max(len(rels_a), len(rels_b))


def soft_jaccard(samples, subtask="ner"):
    n = len(samples)
    if n <= 1:
        return 1.0
    pair_fn = _ner_soft_jaccard_pair if subtask == "ner" else _re_soft_jaccard_pair
    field = "entities" if subtask == "ner" else "relations"
    scores = []
    for i, j in combinations(range(n), 2):
        scores.append(pair_fn(samples[i].get(field, []), samples[j].get(field, [])))
    return float(np.mean(scores))


def voting_confidence(samples, subtask="ner"):
    n = len(samples)
    if n == 0:
        return 0.0
    keys_per_sample = [_extract_surface_keys(s, subtask) for s in samples]
    all_keys = set()
    for ks in keys_per_sample:
        all_keys |= set(ks)
    if not all_keys:
        return 1.0
    freqs = []
    for k in all_keys:
        cnt = sum(1 for ks in keys_per_sample if k in ks)
        freqs.append(cnt / n)
    return float(np.mean(freqs))


def exact_match_rate(samples, subtask="ner"):
    n = len(samples)
    if n <= 1:
        return 1.0
    keys_per_sample = [_extract_surface_keys(s, subtask) for s in samples]
    counts = Counter(keys_per_sample)
    return counts.most_common(1)[0][1] / n


# ── Bootstrap & statistics ──────────────────────────────────────────

def bootstrap_spearman(signal_vals, f1_vals, n_boot=N_BOOTSTRAP):
    n = len(signal_vals)
    if n < 10:
        return {"rho": float("nan"), "ci_lo": float("nan"), "ci_hi": float("nan"), "p": float("nan")}
    sig = np.array(signal_vals)
    f1 = np.array(f1_vals)
    rho_obs, p_obs = spearmanr(sig, f1)
    rhos = []
    for _ in range(n_boot):
        idx = RNG.randint(0, n, size=n)
        if np.std(sig[idx]) < 1e-12 or np.std(f1[idx]) < 1e-12:
            continue
        r, _ = spearmanr(sig[idx], f1[idx])
        if not np.isnan(r):
            rhos.append(r)
    if len(rhos) < 100:
        return {"rho": float(rho_obs), "ci_lo": float("nan"), "ci_hi": float("nan"), "p": float(p_obs)}
    ci_lo, ci_hi = np.percentile(rhos, [2.5, 97.5])
    return {"rho": float(rho_obs), "ci_lo": float(ci_lo), "ci_hi": float(ci_hi), "p": float(p_obs)}


def fisher_z_test(rho1, n1, rho2, n2):
    if any(math.isnan(x) for x in [rho1, rho2]) or n1 < 10 or n2 < 10:
        return {"z": float("nan"), "p": float("nan")}
    rho1 = max(-0.9999, min(0.9999, rho1))
    rho2 = max(-0.9999, min(0.9999, rho2))
    z1 = 0.5 * math.log((1 + rho1) / (1 - rho1))
    z2 = 0.5 * math.log((1 + rho2) / (1 - rho2))
    se = math.sqrt(1.0 / (n1 - 3) + 1.0 / (n2 - 3))
    z_stat = (z1 - z2) / se
    from scipy.stats import norm
    p_val = 2 * norm.sf(abs(z_stat))
    return {"z": float(z_stat), "p": float(p_val)}


# ── Data loading ────────────────────────────────────────────────────

def load_and_compute(jsonl_path, subtask="ner"):
    instances = []
    with open(jsonl_path) as f:
        for line in f:
            instances.append(json.loads(line))

    records = []
    for idx, inst in enumerate(instances):
        if idx % 100 == 0:
            print(f"  signals: {idx}/{len(instances)}", file=sys.stderr)

        text = inst["text"]
        gold = inst["gold"]
        samples = inst["samples"]
        greedy = inst.get("greedy", samples[0] if samples else {"entities": [], "relations": []})
        logprobs_list = inst.get("logprobs", [])

        gf1 = per_instance_f1(greedy, gold, subtask)
        sj = soft_jaccard(samples, subtask)
        fk = fleiss_kappa_surface(samples, subtask)
        vc = voting_confidence(samples, subtask)
        em = exact_match_rate(samples, subtask)
        lp = float(np.mean(logprobs_list)) if logprobs_list else float(np.mean([s.get("mean_logprob", 0) for s in samples]))

        sent_len = len(text.split())

        if subtask == "ner":
            gold_items = gold.get("entities", [])
            ent_count = len(gold_items)
            type_diversity = len(set(e["type"] for e in gold_items)) if gold_items else 0
        else:
            gold_items = gold.get("relations", [])
            ent_count = len(gold_items)
            type_diversity = len(set(r["type"] for r in gold_items)) if gold_items else 0

        records.append({
            "id": inst["id"],
            "greedy_f1": gf1,
            "sj": sj,
            "fk": fk,
            "voting_conf": vc,
            "em": em,
            "logprob": lp,
            "sent_len": sent_len,
            "ent_count": ent_count,
            "type_diversity": type_diversity,
        })

    return records


# ── Stratification functions ────────────────────────────────────────

def stratify_by_greedy_f1(records):
    strata = {"[0, 0.25)": [], "[0.25, 0.5)": [], "[0.5, 0.75)": [], "[0.75, 1.0]": []}
    for r in records:
        f = r["greedy_f1"]
        if f < 0.25:
            strata["[0, 0.25)"].append(r)
        elif f < 0.5:
            strata["[0.25, 0.5)"].append(r)
        elif f < 0.75:
            strata["[0.5, 0.75)"].append(r)
        else:
            strata["[0.75, 1.0]"].append(r)
    return strata


def stratify_by_tertiles(records, key):
    arr = np.array([r[key] for r in records])
    t33, t67 = np.percentile(arr, [33.33, 66.67])

    strata = {"Low (T1)": [], "Medium (T2)": [], "High (T3)": []}
    for r in records:
        v = r[key]
        if v <= t33:
            strata["Low (T1)"].append(r)
        elif v <= t67:
            strata["Medium (T2)"].append(r)
        else:
            strata["High (T3)"].append(r)

    return strata, {"t33": float(t33), "t67": float(t67)}


def stratify_entity_count(records):
    counts = [r["ent_count"] for r in records]
    max_c = max(counts)

    if max_c <= 3:
        strata = {"0": [], "1": [], "2+": []}
        for r in records:
            c = r["ent_count"]
            if c == 0:
                strata["0"].append(r)
            elif c == 1:
                strata["1"].append(r)
            else:
                strata["2+"].append(r)
    else:
        strata = {"0": [], "1-2": [], "3-5": [], "6+": []}
        for r in records:
            c = r["ent_count"]
            if c == 0:
                strata["0"].append(r)
            elif c <= 2:
                strata["1-2"].append(r)
            elif c <= 5:
                strata["3-5"].append(r)
            else:
                strata["6+"].append(r)

    merged = {}
    keys = list(strata.keys())
    carry = []
    carry_label_parts = []
    for k in keys:
        carry.extend(strata[k])
        carry_label_parts.append(k)
        if len(carry) >= MIN_STRATUM_SIZE:
            label = "+".join(carry_label_parts)
            merged[label] = carry
            carry = []
            carry_label_parts = []
    if carry:
        if merged:
            last_key = list(merged.keys())[-1]
            merged[last_key].extend(carry)
            new_key = last_key + "+" + "+".join(carry_label_parts)
            merged[new_key] = merged.pop(last_key)
        else:
            merged["+".join(carry_label_parts)] = carry

    return merged


# ── Per-stratum analysis ────────────────────────────────────────────

def analyze_stratum(records):
    n = len(records)
    if n < MIN_STRATUM_SIZE:
        return {
            "n": n,
            "mean_f1": float(np.mean([r["greedy_f1"] for r in records])) if records else 0.0,
            "too_small": True,
            "signals": {s: {"rho": None} for s in SIGNALS},
        }

    f1s = [r["greedy_f1"] for r in records]
    result = {
        "n": n,
        "mean_f1": float(np.mean(f1s)),
        "std_f1": float(np.std(f1s)),
        "too_small": False,
        "signals": {},
    }

    for sig_name in SIGNALS:
        sig_vals = [r[sig_name] for r in records]
        if np.std(sig_vals) < 1e-12:
            result["signals"][sig_name] = {
                "rho": 0.0, "ci_lo": 0.0, "ci_hi": 0.0, "p": 1.0,
            }
            continue
        sp = bootstrap_spearman(sig_vals, f1s)
        result["signals"][sig_name] = {
            "rho": sp["rho"], "ci_lo": sp["ci_lo"], "ci_hi": sp["ci_hi"], "p": sp["p"],
        }
    return result


def analyze_strata(strata_dict, label):
    print(f"\n{'=' * 60}", file=sys.stderr)
    print(f"Stratification: {label}", file=sys.stderr)
    results = {}
    for stratum_name, records in strata_dict.items():
        print(f"  {stratum_name}: n={len(records)}", file=sys.stderr)
        results[stratum_name] = analyze_stratum(records)
    return results


def compute_fisher_z_comparisons(strata_results):
    keys = list(strata_results.keys())
    valid = [k for k in keys if not strata_results[k].get("too_small", True)]
    if len(valid) < 2:
        return {}

    comparisons = {}
    if len(valid) >= 3:
        mid_idx = len(valid) // 2
        pairs = [
            ("extreme_low_vs_mid", valid[0], valid[mid_idx]),
            ("extreme_high_vs_mid", valid[-1], valid[mid_idx]),
            ("extreme_low_vs_high", valid[0], valid[-1]),
        ]
    else:
        pairs = [("low_vs_high", valid[0], valid[-1])]

    for pair_name, k1, k2 in pairs:
        s1, s2 = strata_results[k1], strata_results[k2]
        n1, n2 = s1["n"], s2["n"]
        comparisons[pair_name] = {"strata": [k1, k2], "signals": {}}
        for sig in SIGNALS:
            rho1 = s1["signals"][sig].get("rho")
            rho2 = s2["signals"][sig].get("rho")
            if rho1 is None or rho2 is None:
                continue
            fz = fisher_z_test(rho1, n1, rho2, n2)
            comparisons[pair_name]["signals"][sig] = fz
    return comparisons


# ── Visualization ───────────────────────────────────────────────────

def plot_stratification(all_strat_results, title, output_path, proxy_labels):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    proxies = list(all_strat_results.keys())
    n_panels = len(proxies)
    fig, axes = plt.subplots(1, n_panels, figsize=(5.5 * n_panels, 4.5), squeeze=False)

    colors = {"sj": "#1f77b4", "fk": "#ff7f0e", "logprob": "#2ca02c",
              "voting_conf": "#d62728", "em": "#9467bd"}
    markers = {"sj": "o", "fk": "s", "logprob": "^", "voting_conf": "D", "em": "v"}

    for pi, proxy_key in enumerate(proxies):
        ax = axes[0, pi]
        strata_data = all_strat_results[proxy_key]
        stratum_names = list(strata_data.keys())
        x = np.arange(len(stratum_names))

        for sig in SIGNALS:
            rhos = []
            ci_los = []
            ci_his = []
            valid = True
            for sname in stratum_names:
                sd = strata_data[sname]
                if sd.get("too_small", True):
                    valid = False
                    break
                r = sd["signals"][sig].get("rho")
                if r is None or (isinstance(r, float) and math.isnan(r)):
                    valid = False
                    break
                rhos.append(r)
                cl = sd["signals"][sig].get("ci_lo", float("nan"))
                ch = sd["signals"][sig].get("ci_hi", float("nan"))
                ci_los.append(cl)
                ci_his.append(ch)

            if not valid or not rhos:
                continue

            rhos = np.array(rhos)
            ci_los = np.array(ci_los)
            ci_his = np.array(ci_his)

            has_ci = not np.any(np.isnan(ci_los))
            if has_ci:
                yerr_lo = rhos - ci_los
                yerr_hi = ci_his - rhos
                ax.errorbar(x, rhos, yerr=[yerr_lo, yerr_hi],
                            label=SIGNAL_LABELS[sig], color=colors[sig],
                            marker=markers[sig], markersize=6, capsize=3,
                            linewidth=1.5)
            else:
                ax.plot(x, rhos, label=SIGNAL_LABELS[sig], color=colors[sig],
                        marker=markers[sig], markersize=6, linewidth=1.5)

        ax.set_xticks(x)
        ax.set_xticklabels(stratum_names, fontsize=8, rotation=15, ha="right")
        ax.set_ylabel("Spearman ρ", fontsize=10)
        ax.set_title(proxy_labels.get(proxy_key, proxy_key), fontsize=11)
        ax.axhline(y=0, color="gray", linestyle="--", linewidth=0.5)
        ax.grid(axis="y", alpha=0.3)

        for xi, sname in enumerate(stratum_names):
            n = strata_data[sname]["n"]
            ax.annotate(f"n={n}", (xi, ax.get_ylim()[0]),
                        textcoords="offset points", xytext=(0, 5),
                        fontsize=7, ha="center", color="gray")

    axes[0, 0].legend(fontsize=8, loc="best")
    fig.suptitle(title, fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved plot: {output_path}", file=sys.stderr)


# ── Main ────────────────────────────────────────────────────────────

def main():
    os.makedirs(RESULT_DIR, exist_ok=True)

    all_results = {}

    for ds_name, ds_info in DATASETS.items():
        subtask = ds_info["subtask"]
        print(f"\nLoading {ds_name}...", file=sys.stderr)
        records = load_and_compute(ds_info["path"], subtask)
        print(f"  {len(records)} instances loaded", file=sys.stderr)

        ds_results = {"n_total": len(records), "subtask": subtask}

        # Greedy F1 stratification (reference only)
        gf1_strata = stratify_by_greedy_f1(records)
        ds_results["by_greedy_f1"] = analyze_strata(gf1_strata, f"{ds_name} / greedy F1 (reference)")
        ds_results["by_greedy_f1_fisher_z"] = compute_fisher_z_comparisons(ds_results["by_greedy_f1"])

        # Independent proxy: sentence length (tertiles)
        sl_strata, sl_thresh = stratify_by_tertiles(records, "sent_len")
        ds_results["by_sent_len"] = analyze_strata(sl_strata, f"{ds_name} / sentence length")
        ds_results["by_sent_len_thresholds"] = sl_thresh
        ds_results["by_sent_len_fisher_z"] = compute_fisher_z_comparisons(ds_results["by_sent_len"])

        # Independent proxy: entity/relation count
        ec_strata = stratify_entity_count(records)
        ds_results["by_ent_count"] = analyze_strata(ec_strata, f"{ds_name} / entity count")
        ds_results["by_ent_count_fisher_z"] = compute_fisher_z_comparisons(ds_results["by_ent_count"])

        # Independent proxy: entity type diversity (tertiles)
        td_strata, td_thresh = stratify_by_tertiles(records, "type_diversity")
        ds_results["by_type_diversity"] = analyze_strata(td_strata, f"{ds_name} / type diversity")
        ds_results["by_type_diversity_thresholds"] = td_thresh
        ds_results["by_type_diversity_fisher_z"] = compute_fisher_z_comparisons(ds_results["by_type_diversity"])

        # Cross-proxy correlations
        f1s = np.array([r["greedy_f1"] for r in records])
        slens = np.array([r["sent_len"] for r in records])
        ents = np.array([r["ent_count"] for r in records])
        tdiv = np.array([r["type_diversity"] for r in records])

        proxy_corrs = {}
        for (name, a, b) in [
            ("f1_vs_sent_len", f1s, slens),
            ("f1_vs_ent_count", f1s, ents),
            ("f1_vs_type_diversity", f1s, tdiv),
            ("sent_len_vs_ent_count", slens, ents),
            ("sent_len_vs_type_diversity", slens, tdiv),
            ("ent_count_vs_type_diversity", ents, tdiv),
        ]:
            r, p = spearmanr(a, b)
            proxy_corrs[name] = {"rho": float(r), "p": float(p)}
        ds_results["proxy_correlations"] = proxy_corrs

        # Global signal correlations (full dataset)
        global_sigs = {}
        for sig_name in SIGNALS:
            sig_vals = [r[sig_name] for r in records]
            sp = bootstrap_spearman(sig_vals, [r["greedy_f1"] for r in records])
            global_sigs[sig_name] = sp
        ds_results["global_signals"] = global_sigs

        all_results[ds_name] = ds_results

    # NER seed averaging
    if "ner_seed42" in all_results and "ner_seed123" in all_results:
        print("\nAveraging NER seeds...", file=sys.stderr)
        avg = {"n_total": all_results["ner_seed42"]["n_total"], "subtask": "ner", "note": "averaged from seed42 and seed123"}
        for key in ["global_signals"]:
            avg[key] = {}
            for sig in SIGNALS:
                r42 = all_results["ner_seed42"][key][sig]
                r123 = all_results["ner_seed123"][key][sig]
                avg[key][sig] = {
                    "rho": (r42["rho"] + r123["rho"]) / 2,
                    "rho_seed42": r42["rho"],
                    "rho_seed123": r123["rho"],
                    "rho_diff": abs(r42["rho"] - r123["rho"]),
                }
        all_results["ner_avg"] = avg

    # Save results
    result_path = os.path.join(RESULT_DIR, "results.json")
    with open(result_path, "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {result_path}", file=sys.stderr)

    # Visualization
    proxy_labels_ner = {
        "by_sent_len": "Sentence Length",
        "by_ent_count": "Entity Count",
        "by_type_diversity": "Type Diversity",
        "by_greedy_f1": "Greedy F1 (ref.)",
    }
    proxy_labels_re = {
        "by_sent_len": "Sentence Length",
        "by_ent_count": "Relation Count",
        "by_type_diversity": "Type Diversity",
        "by_greedy_f1": "Greedy F1 (ref.)",
    }

    for ds_name in ["ner_seed42", "ner_seed123"]:
        if ds_name not in all_results:
            continue
        strat_for_plot = {
            k: all_results[ds_name][k]
            for k in ["by_sent_len", "by_ent_count", "by_type_diversity", "by_greedy_f1"]
            if k in all_results[ds_name]
        }
        plot_stratification(
            strat_for_plot,
            f"NER Stratification ({ds_name})",
            os.path.join(RESULT_DIR, f"{ds_name}_stratification.pdf"),
            proxy_labels_ner,
        )

    if "re_seed42" in all_results:
        strat_for_plot = {
            k: all_results["re_seed42"][k]
            for k in ["by_sent_len", "by_ent_count", "by_type_diversity", "by_greedy_f1"]
            if k in all_results["re_seed42"]
        }
        plot_stratification(
            strat_for_plot,
            "RE Stratification (re_seed42)",
            os.path.join(RESULT_DIR, "re_seed42_stratification.pdf"),
            proxy_labels_re,
        )

    # Print summary
    print_summary(all_results)


def print_summary(results):
    lines = []
    lines.append("=" * 90)
    lines.append("EXP-009 v2 — CAPABILITY STRATIFICATION (INDEPENDENT PROXIES)")
    lines.append("=" * 90)

    for ds_name in ["ner_seed42", "ner_seed123", "re_seed42"]:
        if ds_name not in results:
            continue
        data = results[ds_name]
        lines.append(f"\n{'─' * 70}")
        lines.append(f"Dataset: {ds_name.upper()} (n={data['n_total']})")
        lines.append(f"{'─' * 70}")

        lines.append("\n  Global signal ρ (full dataset):")
        for sig in SIGNALS:
            gs = data["global_signals"][sig]
            ci_str = f"[{gs['ci_lo']:.3f}, {gs['ci_hi']:.3f}]" if not math.isnan(gs.get("ci_lo", float("nan"))) else "[?,?]"
            lines.append(f"    {sig:<14} ρ={gs['rho']:.3f} {ci_str}  p={gs['p']:.1e}")

        lines.append("\n  Proxy independence check:")
        for pair, vals in data["proxy_correlations"].items():
            lines.append(f"    {pair:<35} ρ={vals['rho']:.3f} (p={vals['p']:.1e})")

        strat_keys = [
            ("by_sent_len", "Sentence Length (INDEPENDENT)"),
            ("by_ent_count", "Entity/Relation Count (INDEPENDENT)"),
            ("by_type_diversity", "Type Diversity (INDEPENDENT)"),
            ("by_greedy_f1", "Greedy F1 (REFERENCE ONLY)"),
        ]
        for strat_key, strat_label in strat_keys:
            if strat_key not in data:
                continue
            strata = data[strat_key]
            lines.append(f"\n  ▸ Stratification by {strat_label}:")
            header = f"  {'Stratum':<20} {'n':>5} {'mean_F1':>8}"
            for sig in SIGNALS:
                header += f"  {sig:>14}"
            lines.append(header)
            lines.append("  " + "-" * (len(header) - 2))

            for sname, sdata in strata.items():
                n = sdata["n"]
                mf1 = sdata["mean_f1"]
                row = f"  {sname:<20} {n:>5} {mf1:>8.3f}"
                for sig in SIGNALS:
                    sd = sdata["signals"].get(sig, {})
                    rho = sd.get("rho")
                    if rho is None or (isinstance(rho, float) and math.isnan(rho)):
                        row += f"  {'N/A':>14}"
                    else:
                        ci_lo = sd.get("ci_lo", float("nan"))
                        ci_hi = sd.get("ci_hi", float("nan"))
                        if not math.isnan(ci_lo):
                            row += f"  {rho:>5.3f}[{ci_lo:.2f},{ci_hi:.2f}]"
                        else:
                            row += f"  {rho:>5.3f}[?,?]"
                lines.append(row)

            fz_key = strat_key + "_fisher_z"
            if fz_key in data and data[fz_key]:
                lines.append(f"\n    Fisher z-test comparisons:")
                for pair_name, pair_data in data[fz_key].items():
                    s1, s2 = pair_data["strata"]
                    lines.append(f"      {pair_name}: {s1} vs {s2}")
                    for sig, fz in pair_data["signals"].items():
                        star = "*" if fz["p"] < 0.05 else ""
                        lines.append(f"        {sig:<14} z={fz['z']:>6.3f}  p={fz['p']:.3f}{star}")

    if "ner_avg" in results:
        lines.append(f"\n{'─' * 70}")
        lines.append("NER Seed Stability (seed42 vs seed123)")
        lines.append(f"{'─' * 70}")
        for sig in SIGNALS:
            d = results["ner_avg"]["global_signals"][sig]
            lines.append(f"  {sig:<14} avg_ρ={d['rho']:.3f}  seed42={d['rho_seed42']:.3f}  seed123={d['rho_seed123']:.3f}  |Δ|={d['rho_diff']:.3f}")

    lines.append("\n" + "=" * 90)

    summary = "\n".join(lines)
    print(summary)

    summary_path = os.path.join(RESULT_DIR, "summary.txt")
    with open(summary_path, "w") as f:
        f.write(summary)
    print(f"\nSummary saved to {summary_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
