"""Entity-Level Majority Vote Construction for NER and RE.

Core hypothesis: the correct analogy for self-consistency on structured output
is entity-level majority vote construction, not instance-level best-of-N selection.
"""

import json
import math
import os
import sys
import numpy as np
from collections import defaultdict

# ---------------------------------------------------------------------------
# Metrics (mirroring unified_metrics.py)
# ---------------------------------------------------------------------------

def compute_prf(pred_set, gold_set):
    if not gold_set and not pred_set:
        return 1.0, 1.0, 1.0
    if not pred_set:
        return 0.0, 0.0, 0.0
    if not gold_set:
        return 0.0, 0.0, 0.0
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0, 0.0, 0.0
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    f = 2 * p * r / (p + r)
    return p, r, f


def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}


def relation_set(relations):
    return {(r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"])
            for r in relations}


# ---------------------------------------------------------------------------
# Construction
# ---------------------------------------------------------------------------

def entity_majority_vote(samples, threshold, weights=None):
    """Collect entities across N samples, keep those above threshold."""
    entity_counts = defaultdict(float)
    N = len(samples)
    for i, sample in enumerate(samples):
        w = weights[i] if weights is not None else 1.0
        for e in sample.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            entity_counts[key] += w

    total_weight = sum(weights) if weights is not None else N
    constructed = set()
    for key, count in entity_counts.items():
        if count / total_weight >= threshold:
            constructed.add(key)
    return constructed


def relation_majority_vote(samples, threshold, weights=None):
    """Collect relations across N samples, keep those above threshold."""
    rel_counts = defaultdict(float)
    N = len(samples)
    for i, sample in enumerate(samples):
        w = weights[i] if weights is not None else 1.0
        for r in sample.get("relations", []):
            key = (r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"])
            rel_counts[key] += w

    total_weight = sum(weights) if weights is not None else N
    constructed = set()
    for key, count in rel_counts.items():
        if count / total_weight >= threshold:
            constructed.add(key)
    return constructed


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_data(path, gold_filter=True):
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if gold_filter and not obj["gold"].get("entities", []):
                continue
            instances.append(obj)
    return instances


# ---------------------------------------------------------------------------
# Baselines
# ---------------------------------------------------------------------------

def get_lp_weights(inst):
    """exp(mean_logprob) per sample, then normalize to sum=1."""
    samples = inst["samples"]
    logprobs = inst.get("logprobs", None)
    lps = []
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob", None)
        if lp is None and logprobs is not None and i < len(logprobs):
            lp = logprobs[i]
        if lp is None or not math.isfinite(lp):
            lp = -100.0
        lps.append(lp)
    max_lp = max(lps)
    ws = [math.exp(lp - max_lp) for lp in lps]
    total = sum(ws)
    return [w / total for w in ws]


def get_sj_weights(inst):
    """exp(cumulative_logprob) per sample, normalize."""
    samples = inst["samples"]
    lps = []
    for s in samples:
        lp = s.get("cumulative_logprob", None)
        if lp is None or not math.isfinite(lp):
            lp = -1e6
        lps.append(lp)
    max_lp = max(lps)
    ws = [math.exp(lp - max_lp) for lp in lps]
    total = sum(ws)
    return [w / total for w in ws]


def best_of_n_by_key(inst, key="mean_logprob"):
    samples = inst["samples"]
    logprobs = inst.get("logprobs", None)
    best_idx, best_val = 0, -float("inf")
    for i, s in enumerate(samples):
        val = s.get(key, None)
        if val is None and key == "mean_logprob" and logprobs is not None and i < len(logprobs):
            val = logprobs[i]
        if val is not None and math.isfinite(val) and val > best_val:
            best_val = val
            best_idx = i
    return best_idx


def best_of_n_sj(inst):
    best_idx, best_val = 0, -float("inf")
    for i, s in enumerate(inst["samples"]):
        val = s.get("cumulative_logprob", None)
        if val is not None and math.isfinite(val) and val > best_val:
            best_val = val
            best_idx = i
    return best_idx


# ---------------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------------

THRESHOLDS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

DATASETS = {
    "scierc": "/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl",
    "conll": "/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16/samples.jsonl",
    "fewnerd": "/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl",
}

OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/entity_construction"


def bootstrap_ci(values, n_boot=2000, ci=0.95, seed=42):
    arr = np.array(values)
    n = len(arr)
    if n == 0:
        return 0.0, 0.0, 0.0
    rng = np.random.RandomState(seed)
    boot_means = np.array([arr[rng.randint(0, n, n)].mean() for _ in range(n_boot)])
    boot_means.sort()
    lo = boot_means[int((1 - ci) / 2 * n_boot)]
    hi = boot_means[int((1 + ci) / 2 * n_boot)]
    return float(arr.mean()), float(lo), float(hi)


def run_dataset(name, path):
    print(f"\n{'='*70}")
    print(f"Dataset: {name} ({path})")
    print(f"{'='*70}")

    data = load_data(path, gold_filter=True)
    print(f"Loaded {len(data)} instances (gold-filtered)")

    n_samples = len(data[0]["samples"])
    print(f"Samples per instance: {n_samples}")

    has_relations = any(len(inst["gold"].get("relations", [])) > 0 for inst in data)
    print(f"Has relations: {has_relations}")

    results = {}

    # ---- Baselines ----
    greedy_f1s, greedy_ps, greedy_rs = [], [], []
    lp_sel_f1s, lp_sel_ps, lp_sel_rs = [], [], []
    sj_sel_f1s, sj_sel_ps, sj_sel_rs = [], [], []
    oracle_f1s, oracle_ps, oracle_rs = [], [], []
    random_f1s = []

    # RE baselines (scierc only)
    re_greedy_f1s, re_greedy_ps, re_greedy_rs = [], [], []
    re_lp_sel_f1s, re_lp_sel_ps, re_lp_sel_rs = [], [], []
    re_oracle_f1s = []

    for inst in data:
        gold_ents = entity_set(inst["gold"]["entities"])
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_pred = entity_set(greedy.get("entities", []))

        p, r, f = compute_prf(greedy_pred, gold_ents)
        greedy_f1s.append(f)
        greedy_ps.append(p)
        greedy_rs.append(r)

        # LP selection
        lp_idx = best_of_n_by_key(inst, "mean_logprob")
        lp_pred = entity_set(inst["samples"][lp_idx].get("entities", []))
        p, r, f = compute_prf(lp_pred, gold_ents)
        lp_sel_f1s.append(f)
        lp_sel_ps.append(p)
        lp_sel_rs.append(r)

        # SJ selection
        sj_idx = best_of_n_sj(inst)
        sj_pred = entity_set(inst["samples"][sj_idx].get("entities", []))
        p, r, f = compute_prf(sj_pred, gold_ents)
        sj_sel_f1s.append(f)
        sj_sel_ps.append(p)
        sj_sel_rs.append(r)

        # Oracle
        best_f, best_p, best_r = 0.0, 0.0, 0.0
        for s in inst["samples"]:
            sp = entity_set(s.get("entities", []))
            pp, rr, ff = compute_prf(sp, gold_ents)
            if ff > best_f:
                best_f, best_p, best_r = ff, pp, rr
        oracle_f1s.append(best_f)
        oracle_ps.append(best_p)
        oracle_rs.append(best_r)

        # Random
        rand_fs = []
        for s in inst["samples"]:
            sp = entity_set(s.get("entities", []))
            _, _, ff = compute_prf(sp, gold_ents)
            rand_fs.append(ff)
        random_f1s.append(np.mean(rand_fs))

        # RE baselines
        if has_relations:
            gold_rels = relation_set(inst["gold"].get("relations", []))
            greedy_rels = relation_set(greedy.get("relations", []))
            p, r, f = compute_prf(greedy_rels, gold_rels)
            re_greedy_f1s.append(f)
            re_greedy_ps.append(p)
            re_greedy_rs.append(r)

            lp_rels = relation_set(inst["samples"][lp_idx].get("relations", []))
            p, r, f = compute_prf(lp_rels, gold_rels)
            re_lp_sel_f1s.append(f)
            re_lp_sel_ps.append(p)
            re_lp_sel_rs.append(r)

            best_re_f = 0.0
            for s in inst["samples"]:
                sr = relation_set(s.get("relations", []))
                _, _, ff = compute_prf(sr, gold_rels)
                if ff > best_re_f:
                    best_re_f = ff
            re_oracle_f1s.append(best_re_f)

    results["greedy"] = {
        "F1": float(np.mean(greedy_f1s)), "P": float(np.mean(greedy_ps)), "R": float(np.mean(greedy_rs)),
        "F1_ci": bootstrap_ci(greedy_f1s)
    }
    results["lp_selection"] = {
        "F1": float(np.mean(lp_sel_f1s)), "P": float(np.mean(lp_sel_ps)), "R": float(np.mean(lp_sel_rs)),
        "F1_ci": bootstrap_ci(lp_sel_f1s)
    }
    results["sj_selection"] = {
        "F1": float(np.mean(sj_sel_f1s)), "P": float(np.mean(sj_sel_ps)), "R": float(np.mean(sj_sel_rs)),
        "F1_ci": bootstrap_ci(sj_sel_f1s)
    }
    results["oracle"] = {
        "F1": float(np.mean(oracle_f1s)), "P": float(np.mean(oracle_ps)), "R": float(np.mean(oracle_rs)),
        "F1_ci": bootstrap_ci(oracle_f1s)
    }
    results["random"] = {
        "F1": float(np.mean(random_f1s)),
        "F1_ci": bootstrap_ci(random_f1s)
    }

    if has_relations:
        results["re_greedy"] = {
            "F1": float(np.mean(re_greedy_f1s)), "P": float(np.mean(re_greedy_ps)), "R": float(np.mean(re_greedy_rs))
        }
        results["re_lp_selection"] = {
            "F1": float(np.mean(re_lp_sel_f1s)), "P": float(np.mean(re_lp_sel_ps)), "R": float(np.mean(re_lp_sel_rs))
        }
        results["re_oracle"] = {"F1": float(np.mean(re_oracle_f1s))}

    # ---- Construction (threshold sweep) ----
    for variant in ["uniform", "lp_weighted"]:
        for threshold in THRESHOLDS:
            ent_f1s, ent_ps, ent_rs = [], [], []
            re_f1s_c, re_ps_c, re_rs_c = [], [], []

            for inst in data:
                gold_ents = entity_set(inst["gold"]["entities"])
                if variant == "uniform":
                    constructed = entity_majority_vote(inst["samples"], threshold)
                else:
                    ws = get_lp_weights(inst)
                    constructed = entity_majority_vote(inst["samples"], threshold, weights=ws)
                p, r, f = compute_prf(constructed, gold_ents)
                ent_f1s.append(f)
                ent_ps.append(p)
                ent_rs.append(r)

                if has_relations:
                    gold_rels = relation_set(inst["gold"].get("relations", []))
                    if variant == "uniform":
                        constructed_rels = relation_majority_vote(inst["samples"], threshold)
                    else:
                        ws = get_lp_weights(inst)
                        constructed_rels = relation_majority_vote(inst["samples"], threshold, weights=ws)
                    p, r, f = compute_prf(constructed_rels, gold_rels)
                    re_f1s_c.append(f)
                    re_ps_c.append(p)
                    re_rs_c.append(r)

            key = f"construction_{variant}_t{threshold:.1f}"
            results[key] = {
                "F1": float(np.mean(ent_f1s)), "P": float(np.mean(ent_ps)), "R": float(np.mean(ent_rs)),
                "F1_ci": bootstrap_ci(ent_f1s),
                "threshold": threshold, "variant": variant
            }
            if has_relations and re_f1s_c:
                results[key]["RE_F1"] = float(np.mean(re_f1s_c))
                results[key]["RE_P"] = float(np.mean(re_ps_c))
                results[key]["RE_R"] = float(np.mean(re_rs_c))

    return results


def find_best_threshold(results, variant):
    best_f1, best_t = 0.0, 0.0
    for t in THRESHOLDS:
        key = f"construction_{variant}_t{t:.1f}"
        if key in results and results[key]["F1"] > best_f1:
            best_f1 = results[key]["F1"]
            best_t = t
    return best_t, best_f1


def print_table(name, results):
    greedy_f1 = results["greedy"]["F1"]
    print(f"\n--- {name} NER Results ---")
    print(f"{'Method':<30} {'F1':>7} {'P':>7} {'R':>7} {'Δ vs Greedy':>12}")
    print("-" * 70)

    def row(label, r, show_delta=True):
        f1 = r["F1"]
        p = r.get("P", 0)
        rr = r.get("R", 0)
        delta = f"{(f1 - greedy_f1)*100:+.2f}pp" if show_delta else "—"
        ci = r.get("F1_ci", None)
        ci_str = ""
        if ci:
            ci_str = f"  [{ci[1]:.4f}, {ci[2]:.4f}]"
        print(f"{label:<30} {f1:.4f} {p:.4f} {rr:.4f} {delta:>12}{ci_str}")

    row("Greedy (T=0)", results["greedy"], show_delta=False)
    row("LP Selection", results["lp_selection"])
    row("SJ Selection", results["sj_selection"])
    row("Random Sample", results["random"])
    row("Oracle Best-of-N", results["oracle"])
    print()

    for variant in ["uniform", "lp_weighted"]:
        best_t, best_f1 = find_best_threshold(results, variant)
        best_key = f"construction_{variant}_t{best_t:.1f}"
        print(f"  Best {variant} construction: threshold={best_t:.1f}")
        row(f"  Construction({variant})@{best_t}", results[best_key])

        print(f"\n  {variant} threshold sweep:")
        for t in THRESHOLDS:
            key = f"construction_{variant}_t{t:.1f}"
            r = results[key]
            delta = (r["F1"] - greedy_f1) * 100
            marker = " <-- BEST" if t == best_t else ""
            print(f"    θ={t:.1f}  F1={r['F1']:.4f}  P={r['P']:.4f}  R={r['R']:.4f}  Δ={delta:+.2f}pp{marker}")
        print()

    # RE results
    if "re_greedy" in results:
        re_greedy_f1 = results["re_greedy"]["F1"]
        print(f"\n--- {name} RE Results ---")
        print(f"{'Method':<30} {'F1':>7} {'P':>7} {'R':>7} {'Δ vs Greedy':>12}")
        print("-" * 70)

        def re_row(label, f1, p=0, r=0, show_delta=True):
            delta = f"{(f1 - re_greedy_f1)*100:+.2f}pp" if show_delta else "—"
            print(f"{label:<30} {f1:.4f} {p:.4f} {r:.4f} {delta:>12}")

        re_row("Greedy", re_greedy_f1, results["re_greedy"]["P"], results["re_greedy"]["R"], False)
        re_row("LP Selection", results["re_lp_selection"]["F1"], results["re_lp_selection"]["P"], results["re_lp_selection"]["R"])
        re_row("Oracle", results["re_oracle"]["F1"])

        for variant in ["uniform", "lp_weighted"]:
            best_re_f1, best_re_t = 0.0, 0.0
            for t in THRESHOLDS:
                key = f"construction_{variant}_t{t:.1f}"
                re_f1 = results[key].get("RE_F1", 0)
                if re_f1 > best_re_f1:
                    best_re_f1 = re_f1
                    best_re_t = t
            best_key = f"construction_{variant}_t{best_re_t:.1f}"
            re_row(f"Construction({variant})@{best_re_t}",
                   results[best_key].get("RE_F1", 0),
                   results[best_key].get("RE_P", 0),
                   results[best_key].get("RE_R", 0))

            print(f"\n  {variant} RE threshold sweep:")
            for t in THRESHOLDS:
                key = f"construction_{variant}_t{t:.1f}"
                rf1 = results[key].get("RE_F1", 0)
                rp = results[key].get("RE_P", 0)
                rr = results[key].get("RE_R", 0)
                delta = (rf1 - re_greedy_f1) * 100
                marker = " <-- BEST" if t == best_re_t else ""
                print(f"    θ={t:.1f}  F1={rf1:.4f}  P={rp:.4f}  R={rr:.4f}  Δ={delta:+.2f}pp{marker}")
            print()


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    all_results = {}
    summary = {}

    for name, path in DATASETS.items():
        if not os.path.exists(path):
            print(f"SKIP {name}: file not found at {path}")
            continue
        results = run_dataset(name, path)
        all_results[name] = results
        print_table(name, results)

        greedy_f1 = results["greedy"]["F1"]
        best_uniform_t, best_uniform_f1 = find_best_threshold(results, "uniform")
        best_lp_t, best_lp_f1 = find_best_threshold(results, "lp_weighted")

        summary[name] = {
            "greedy_F1": greedy_f1,
            "lp_selection_F1": results["lp_selection"]["F1"],
            "sj_selection_F1": results["sj_selection"]["F1"],
            "oracle_F1": results["oracle"]["F1"],
            "random_F1": results["random"]["F1"],
            "best_uniform_threshold": best_uniform_t,
            "best_uniform_F1": best_uniform_f1,
            "best_uniform_delta_pp": (best_uniform_f1 - greedy_f1) * 100,
            "best_lp_threshold": best_lp_t,
            "best_lp_F1": best_lp_f1,
            "best_lp_delta_pp": (best_lp_f1 - greedy_f1) * 100,
        }

    # Save
    with open(os.path.join(OUTPUT_DIR, "construction_results.json"), "w") as f:
        json.dump(all_results, f, indent=2)
    with open(os.path.join(OUTPUT_DIR, "best_threshold_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)

    # Final summary
    print("\n" + "=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)
    for name, s in summary.items():
        print(f"\n{name}:")
        print(f"  Greedy F1:                {s['greedy_F1']:.4f}")
        print(f"  LP Selection F1:          {s['lp_selection_F1']:.4f} ({(s['lp_selection_F1']-s['greedy_F1'])*100:+.2f}pp)")
        print(f"  SJ Selection F1:          {s['sj_selection_F1']:.4f} ({(s['sj_selection_F1']-s['greedy_F1'])*100:+.2f}pp)")
        print(f"  Random F1:                {s['random_F1']:.4f} ({(s['random_F1']-s['greedy_F1'])*100:+.2f}pp)")
        print(f"  Oracle F1:                {s['oracle_F1']:.4f} ({(s['oracle_F1']-s['greedy_F1'])*100:+.2f}pp)")
        print(f"  Uniform Constr@{s['best_uniform_threshold']:.1f}:      {s['best_uniform_F1']:.4f} ({s['best_uniform_delta_pp']:+.2f}pp)")
        print(f"  LP-Weighted Constr@{s['best_lp_threshold']:.1f}:  {s['best_lp_F1']:.4f} ({s['best_lp_delta_pp']:+.2f}pp)")

    print("\nResults saved to:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
