#!/usr/bin/env python3
"""exp-009 v2 RE rerun: Fix gold-empty filtering + proxy independence check.

Changes from original exp_009_v2_stratification.py:
1. Filter out instances with empty gold relations (F1 always=0)
2. Add proxy-vs-F1 independence analysis (sentence_length, entity_count, relation_count)
3. Use sentence_length quartiles (most independent proxy) as primary stratification
4. Report filtering stats
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
RESULT_DIR = os.path.join(OUTPUT_DIR, "exp_009_v2_re_rerun")
N_BOOTSTRAP = 2000
RNG = np.random.RandomState(42)
MIN_STRATUM_SIZE = 30

RE_PATH = os.path.join(OUTPUT_DIR, "exp_008_re_n16_v2", "samples.jsonl")

SIGNALS = ["sj", "fk", "logprob", "voting_conf", "em"]
SIGNAL_LABELS = {
    "sj": "Soft Jaccard",
    "fk": "Fleiss' κ",
    "logprob": "Log-prob",
    "voting_conf": "Voting Conf",
    "em": "Exact Match",
}


# ── Evaluation helpers ──────────────────────────────────────────────

def relation_strict_match(pred_rels, gold_rels):
    pred_set = {(r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"]) for r in pred_rels}
    gold_set = {(r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"]) for r in gold_rels}
    tp = len(pred_set & gold_set)
    return tp, len(pred_set - gold_set), len(gold_set - pred_set)


def per_instance_f1(pred, gold):
    tp, fp, fn = relation_strict_match(pred.get("relations", []), gold.get("relations", []))
    if tp + fp == 0 or tp + fn == 0:
        return 0.0 if tp == 0 else 1.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r) if (p + r) > 0 else 0.0


# ── Consistency signals ─────────────────────────────────────────────

def _extract_surface_keys(sample):
    return frozenset((r["head"], r["tail"], r["type"]) for r in sample.get("relations", []))


def fleiss_kappa_surface(samples):
    n_raters = len(samples)
    if n_raters <= 1:
        return 1.0
    entity_sets = []
    all_keys = set()
    for s in samples:
        keys = set(_extract_surface_keys(s))
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


def soft_jaccard(samples):
    n = len(samples)
    if n <= 1:
        return 1.0
    scores = []
    for i, j in combinations(range(n), 2):
        scores.append(_re_soft_jaccard_pair(samples[i].get("relations", []), samples[j].get("relations", [])))
    return float(np.mean(scores))


def voting_confidence(samples):
    n = len(samples)
    if n == 0:
        return 0.0
    keys_per_sample = [_extract_surface_keys(s) for s in samples]
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


def exact_match_rate(samples):
    n = len(samples)
    if n <= 1:
        return 1.0
    keys_per_sample = [_extract_surface_keys(s) for s in samples]
    counts = Counter(keys_per_sample)
    return counts.most_common(1)[0][1] / n


# ── Bootstrap & statistics ──────────────────────────────────────────

def bootstrap_spearman(sig, f1, n_boot=N_BOOTSTRAP):
    sig = np.array(sig, dtype=np.float64)
    f1 = np.array(f1, dtype=np.float64)
    n = len(sig)
    if n < 10 or np.std(sig) < 1e-12 or np.std(f1) < 1e-12:
        return {"rho": float("nan"), "ci_lo": float("nan"), "ci_hi": float("nan"), "p": float("nan")}
    rho_obs, p_obs = spearmanr(sig, f1)
    rhos = []
    for _ in range(n_boot):
        idx = RNG.choice(n, n, replace=True)
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


# ── Data loading with filtering ────────────────────────────────────

def load_and_compute(jsonl_path):
    instances = []
    with open(jsonl_path) as f:
        for line in f:
            instances.append(json.loads(line))

    n_total = len(instances)
    n_empty_gold = 0
    records = []

    for idx, inst in enumerate(instances):
        if idx % 100 == 0:
            print(f"  signals: {idx}/{n_total}", file=sys.stderr)

        text = inst["text"]
        gold = inst["gold"]
        samples = inst["samples"]
        greedy = inst.get("greedy", samples[0] if samples else {"entities": [], "relations": []})
        logprobs_list = inst.get("logprobs", [])

        gold_rels = gold.get("relations", [])
        gold_ents = gold.get("entities", [])

        # Filter: skip instances with no gold relations
        if len(gold_rels) == 0:
            n_empty_gold += 1
            continue

        gf1 = per_instance_f1(greedy, gold)
        sj = soft_jaccard(samples)
        fk = fleiss_kappa_surface(samples)
        vc = voting_confidence(samples)
        em = exact_match_rate(samples)
        lp = float(np.mean(logprobs_list)) if logprobs_list else float(np.mean([s.get("mean_logprob", 0) for s in samples]))

        sent_len = len(text.split())
        ent_count = len(gold_ents)
        rel_count = len(gold_rels)
        type_diversity = len(set(r["type"] for r in gold_rels))

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
            "rel_count": rel_count,
            "type_diversity": type_diversity,
        })

    filter_stats = {
        "n_total_raw": n_total,
        "n_empty_gold_filtered": n_empty_gold,
        "n_after_filter": len(records),
    }
    return records, filter_stats


# ── Stratification functions ────────────────────────────────────────

def stratify_by_quartiles(records, key):
    arr = np.array([r[key] for r in records])
    q25, q50, q75 = np.percentile(arr, [25, 50, 75])

    strata = {"Q1 (low)": [], "Q2": [], "Q3": [], "Q4 (high)": []}
    for r in records:
        v = r[key]
        if v <= q25:
            strata["Q1 (low)"].append(r)
        elif v <= q50:
            strata["Q2"].append(r)
        elif v <= q75:
            strata["Q3"].append(r)
        else:
            strata["Q4 (high)"].append(r)

    # Merge small strata
    merged = {}
    keys = list(strata.keys())
    carry = []
    carry_labels = []
    for k in keys:
        carry.extend(strata[k])
        carry_labels.append(k)
        if len(carry) >= MIN_STRATUM_SIZE:
            label = "+".join(carry_labels) if len(carry_labels) > 1 else carry_labels[0]
            merged[label] = carry
            carry = []
            carry_labels = []
    if carry:
        if merged:
            last_key = list(merged.keys())[-1]
            merged[last_key].extend(carry)
            new_key = last_key + "+" + "+".join(carry_labels)
            merged[new_key] = merged.pop(last_key)
        else:
            merged["+".join(carry_labels)] = carry

    thresholds = {"q25": float(q25), "q50": float(q50), "q75": float(q75)}
    return merged, thresholds


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
            result["signals"][sig_name] = {"rho": float("nan"), "ci_lo": float("nan"), "ci_hi": float("nan"), "p": float("nan")}
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
            ("low_vs_mid", valid[0], valid[mid_idx]),
            ("high_vs_mid", valid[-1], valid[mid_idx]),
            ("low_vs_high", valid[0], valid[-1]),
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


# ── Main ────────────────────────────────────────────────────────────

def main():
    os.makedirs(RESULT_DIR, exist_ok=True)

    print("Loading RE data...", file=sys.stderr)
    records, filter_stats = load_and_compute(RE_PATH)
    print(f"  Raw: {filter_stats['n_total_raw']}, Empty gold filtered: {filter_stats['n_empty_gold_filtered']}, "
          f"After filter: {filter_stats['n_after_filter']}", file=sys.stderr)

    results = {"filter_stats": filter_stats, "n_total": len(records)}

    # ── Section 1: Proxy independence check ──────────────────────
    print("\n=== Proxy Independence Check ===", file=sys.stderr)
    f1s = np.array([r["greedy_f1"] for r in records])
    slens = np.array([r["sent_len"] for r in records])
    ents = np.array([r["ent_count"] for r in records])
    rels = np.array([r["rel_count"] for r in records])
    tdiv = np.array([r["type_diversity"] for r in records])

    proxy_pairs = [
        ("sent_len_vs_F1", slens, f1s),
        ("ent_count_vs_F1", ents, f1s),
        ("rel_count_vs_F1", rels, f1s),
        ("type_diversity_vs_F1", tdiv, f1s),
        ("sent_len_vs_ent_count", slens, ents),
        ("sent_len_vs_rel_count", slens, rels),
        ("ent_count_vs_rel_count", ents, rels),
        ("ent_count_vs_type_diversity", ents, tdiv),
    ]

    proxy_corrs = {}
    for name, a, b in proxy_pairs:
        r, p = spearmanr(a, b)
        proxy_corrs[name] = {"rho": float(r), "p": float(p)}
        flag = " *** NOT INDEPENDENT" if abs(r) > 0.3 else ""
        print(f"  {name:<35} ρ={r:.3f} (p={p:.1e}){flag}", file=sys.stderr)
    results["proxy_correlations"] = proxy_corrs

    # Determine best proxies (|ρ| with F1 < 0.3)
    proxy_ranking = []
    for proxy_name in ["sent_len", "ent_count", "rel_count", "type_diversity"]:
        key = f"{proxy_name}_vs_F1"
        rho = abs(proxy_corrs[key]["rho"])
        proxy_ranking.append((proxy_name, rho, rho < 0.3))
    proxy_ranking.sort(key=lambda x: x[1])
    results["proxy_ranking"] = [{"proxy": p, "abs_rho_with_f1": r, "independent": ok} for p, r, ok in proxy_ranking]
    print(f"\n  Proxy ranking (by |ρ| with F1):", file=sys.stderr)
    for p, r, ok in proxy_ranking:
        print(f"    {p:<20} |ρ|={r:.3f}  {'✓ INDEPENDENT' if ok else '✗ NOT INDEPENDENT'}", file=sys.stderr)

    # ── Section 2: Global signal correlations ────────────────────
    print("\n=== Global Signal Correlations (filtered) ===", file=sys.stderr)
    global_sigs = {}
    for sig_name in SIGNALS:
        sig_vals = [r[sig_name] for r in records]
        sp = bootstrap_spearman(sig_vals, [r["greedy_f1"] for r in records])
        global_sigs[sig_name] = sp
        ci = f"[{sp['ci_lo']:.3f}, {sp['ci_hi']:.3f}]" if not math.isnan(sp.get("ci_lo", float("nan"))) else "[?,?]"
        print(f"  {sig_name:<14} ρ={sp['rho']:.3f} {ci}  p={sp['p']:.1e}", file=sys.stderr)
    results["global_signals"] = global_sigs

    # ── Section 3: Stratification by sentence_length quartiles ───
    print("\n=== Stratification by sentence_length (quartiles) ===", file=sys.stderr)
    sl_strata, sl_thresh = stratify_by_quartiles(records, "sent_len")
    results["by_sent_len_quartiles"] = analyze_strata(sl_strata, "sentence_length quartiles")
    results["by_sent_len_quartiles_thresholds"] = sl_thresh
    results["by_sent_len_quartiles_fisher_z"] = compute_fisher_z_comparisons(results["by_sent_len_quartiles"])

    # Also do tertiles for comparison with original
    sl_tert, sl_tert_thresh = stratify_by_tertiles(records, "sent_len")
    results["by_sent_len_tertiles"] = analyze_strata(sl_tert, "sentence_length tertiles")
    results["by_sent_len_tertiles_thresholds"] = sl_tert_thresh
    results["by_sent_len_tertiles_fisher_z"] = compute_fisher_z_comparisons(results["by_sent_len_tertiles"])

    # ── Section 4: Greedy F1 reference stratification ────────────
    gf1_strata = stratify_by_greedy_f1(records)
    results["by_greedy_f1"] = analyze_strata(gf1_strata, "greedy F1 (reference)")
    results["by_greedy_f1_fisher_z"] = compute_fisher_z_comparisons(results["by_greedy_f1"])

    # ── Section 5: Conditional check — stratify by independent proxies only if they pass ──
    for proxy_name in ["ent_count", "rel_count"]:
        key = f"{proxy_name}_vs_F1"
        rho = abs(proxy_corrs[key]["rho"])
        if rho < 0.3:
            print(f"\n=== Stratification by {proxy_name} (tertiles, |ρ|={rho:.3f} < 0.3) ===", file=sys.stderr)
            strata, thresh = stratify_by_tertiles(records, proxy_name)
            results[f"by_{proxy_name}"] = analyze_strata(strata, f"{proxy_name} tertiles")
            results[f"by_{proxy_name}_thresholds"] = thresh
            results[f"by_{proxy_name}_fisher_z"] = compute_fisher_z_comparisons(results[f"by_{proxy_name}"])
        else:
            print(f"\n  SKIP {proxy_name} stratification: |ρ| with F1 = {rho:.3f} > 0.3", file=sys.stderr)
            results[f"by_{proxy_name}_skipped"] = f"|rho_with_f1|={rho:.3f} > 0.3, not independent"

    # ── Save results ─────────────────────────────────────────────
    result_path = os.path.join(RESULT_DIR, "results.json")
    with open(result_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {result_path}", file=sys.stderr)

    # ── Print summary ────────────────────────────────────────────
    print_summary(results)


def print_summary(results):
    lines = []
    lines.append("=" * 90)
    lines.append("EXP-009 v2 RE RERUN — FILTERED + PROXY INDEPENDENCE CHECK")
    lines.append("=" * 90)

    fs = results["filter_stats"]
    lines.append(f"\nFiltering: {fs['n_total_raw']} raw → {fs['n_empty_gold_filtered']} empty-gold removed → {fs['n_after_filter']} kept")

    lines.append(f"\n{'─' * 70}")
    lines.append("Proxy Independence Check (proxy vs F1 Spearman ρ)")
    lines.append(f"{'─' * 70}")
    for item in results["proxy_ranking"]:
        mark = "✓" if item["independent"] else "✗"
        lines.append(f"  {mark} {item['proxy']:<20} |ρ|={item['abs_rho_with_f1']:.3f}")

    lines.append(f"\nProxy cross-correlations:")
    for pair, vals in results["proxy_correlations"].items():
        if "vs_F1" not in pair:
            lines.append(f"  {pair:<35} ρ={vals['rho']:.3f} (p={vals['p']:.1e})")

    lines.append(f"\n{'─' * 70}")
    lines.append(f"Global Signal ρ (n={results['n_total']}, after filtering)")
    lines.append(f"{'─' * 70}")
    for sig in SIGNALS:
        gs = results["global_signals"][sig]
        ci_str = f"[{gs['ci_lo']:.3f}, {gs['ci_hi']:.3f}]" if not math.isnan(gs.get("ci_lo", float("nan"))) else "[?,?]"
        lines.append(f"  {sig:<14} ρ={gs['rho']:.3f} {ci_str}  p={gs['p']:.1e}")

    strat_configs = [
        ("by_sent_len_quartiles", "Sentence Length QUARTILES (primary, independent)"),
        ("by_sent_len_tertiles", "Sentence Length TERTILES (comparison)"),
        ("by_ent_count", "Entity Count TERTILES (if independent)"),
        ("by_rel_count", "Relation Count TERTILES (if independent)"),
        ("by_greedy_f1", "Greedy F1 (reference only)"),
    ]

    for strat_key, strat_label in strat_configs:
        if strat_key not in results:
            skipped = results.get(f"{strat_key}_skipped")
            if skipped:
                lines.append(f"\n  ▸ {strat_label}: SKIPPED — {skipped}")
            continue

        strata = results[strat_key]
        lines.append(f"\n{'─' * 70}")
        lines.append(f"▸ Stratification by {strat_label}")
        lines.append(f"{'─' * 70}")
        header = f"  {'Stratum':<25} {'n':>5} {'mean_F1':>8}"
        for sig in SIGNALS:
            header += f"  {sig:>14}"
        lines.append(header)
        lines.append("  " + "-" * (len(header) - 2))

        for sname, sdata in strata.items():
            n = sdata["n"]
            mf1 = sdata["mean_f1"]
            row = f"  {sname:<25} {n:>5} {mf1:>8.3f}"
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
        if fz_key in results and results[fz_key]:
            lines.append(f"\n  Fisher z-test comparisons:")
            for pair_name, pair_data in results[fz_key].items():
                s1, s2 = pair_data["strata"]
                lines.append(f"    {pair_name}: {s1} vs {s2}")
                for sig, fz in pair_data["signals"].items():
                    star = "*" if fz["p"] < 0.05 else ""
                    lines.append(f"      {sig:<14} z={fz['z']:>6.3f}  p={fz['p']:.3f}{star}")

    lines.append("\n" + "=" * 90)
    summary = "\n".join(lines)
    print(summary)

    summary_path = os.path.join(RESULT_DIR, "summary.txt")
    with open(summary_path, "w") as f:
        f.write(summary)
    print(f"\nSummary saved to {summary_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
