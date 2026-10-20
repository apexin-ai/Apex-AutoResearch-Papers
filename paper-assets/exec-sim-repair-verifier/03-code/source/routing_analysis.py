#!/usr/bin/env python3
"""Routing Heuristic Analysis: CLS vs CWM formulation routing.

Post-hoc analysis using existing per-instance predictions to test whether
simple routing heuristics can capture oracle complementarity between
CLS and CWM formulations.
"""
import json
import os
import sys
from collections import defaultdict
import numpy as np

BASE = "/home/sonny/exec-sim-repair-verifier"

# ── Data loading ──────────────────────────────────────────────────────

def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]

def load_json(path):
    with open(path) as f:
        return json.load(f)

def load_predictions_jsonl(path):
    """Load JSONL predictions: {index, problem_id, mutation_type, label, pred, gen_text}"""
    rows = load_jsonl(path)
    out = []
    for r in rows:
        out.append({
            "index": r["index"],
            "problem_id": r["problem_id"],
            "mutation_type": r.get("mutation_type", ""),
            "label": r["label"],
            "pred": r["pred"],
        })
    return out

def load_predictions_json_array(path):
    """Load JSON array predictions: [{index, problem_id, label, prediction, correct}, ...]"""
    data = load_json(path)
    if isinstance(data, dict) and "predictions" in data:
        items = data["predictions"]
    else:
        items = data
    out = []
    for r in items:
        pred = r.get("pred", r.get("prediction"))
        label = r.get("label")
        if isinstance(label, str):
            label = 1 if label.upper() == "PASS" else 0
        if isinstance(pred, str):
            pred = 1 if pred.upper() == "PASS" else 0
        true_label = r.get("true_label")
        if label is None and true_label is not None:
            label = 1 if str(true_label).upper() == "PASS" else 0
        predicted_label = r.get("predicted_label")
        if pred is None and predicted_label is not None:
            pred = 1 if str(predicted_label).upper() == "PASS" else 0
        out.append({
            "index": r.get("index", r.get("idx")),
            "problem_id": r["problem_id"],
            "mutation_type": r.get("mutation_type", ""),
            "label": label,
            "pred": pred,
        })
    return out

def load_test_data(path):
    """Load test.jsonl to get problem structure."""
    rows = load_jsonl(path)
    out = []
    for i, r in enumerate(rows):
        out.append({
            "index": i,
            "problem_id": r["problem_id"],
            "mutation_type": r.get("mutation_type", ""),
            "label": r["label"],
            "source": r.get("source", ""),
        })
    return out

# ── Core analysis ─────────────────────────────────────────────────────

def compute_per_test_accuracy(preds):
    correct = sum(1 for p in preds if p["pred"] == p["label"])
    return correct / len(preds) * 100

def group_by_problem(preds):
    groups = defaultdict(list)
    for p in preds:
        groups[p["problem_id"]].append(p)
    return dict(groups)

def compute_problem_level_metrics(preds):
    """For each problem, check if ALL tests are correct."""
    groups = group_by_problem(preds)
    results = {}
    for pid, tests in groups.items():
        n_tests = len(tests)
        n_correct = sum(1 for t in tests if t["pred"] == t["label"])
        all_correct = (n_correct == n_tests)
        results[pid] = {
            "n_tests": n_tests,
            "n_correct": n_correct,
            "all_correct": all_correct,
            "accuracy": n_correct / n_tests * 100,
        }
    return results

def compute_per_test_complementarity(cls_preds, cwm_preds):
    """Compute per-test oracle complementarity between CLS and CWM."""
    assert len(cls_preds) == len(cwm_preds), f"Length mismatch: {len(cls_preds)} vs {len(cwm_preds)}"
    n = len(cls_preds)
    both_correct = 0
    cls_only = 0
    cwm_only = 0
    both_wrong = 0
    for c, w in zip(cls_preds, cwm_preds):
        cc = (c["pred"] == c["label"])
        wc = (w["pred"] == w["label"])
        if cc and wc:
            both_correct += 1
        elif cc and not wc:
            cls_only += 1
        elif not cc and wc:
            cwm_only += 1
        else:
            both_wrong += 1
    oracle = both_correct + cls_only + cwm_only
    return {
        "n": n,
        "cls_acc": (both_correct + cls_only) / n * 100,
        "cwm_acc": (both_correct + cwm_only) / n * 100,
        "oracle_acc": oracle / n * 100,
        "both_correct": both_correct,
        "cls_only": cls_only,
        "cwm_only": cwm_only,
        "both_wrong": both_wrong,
        "complementarity_pct": (cls_only + cwm_only) / max(1, cls_only + cwm_only + both_wrong) * 100,
    }

# ── Heuristic 1: Complexity-based routing ─────────────────────────────

def heuristic_complexity_routing(cls_preds, cwm_preds, test_data):
    """Route based on # tests per problem. T=1: use CWM, T>=2: use CLS."""
    groups_cls = group_by_problem(cls_preds)
    groups_cwm = group_by_problem(cwm_preds)
    groups_test = group_by_problem([{"problem_id": t["problem_id"], "index": t["index"]} for t in test_data])

    # Build per-test routing decisions
    cls_by_idx = {p["index"]: p for p in cls_preds}
    cwm_by_idx = {p["index"]: p for p in cwm_preds}

    # Count tests per problem
    problem_test_count = {}
    for pid, tests in groups_cls.items():
        problem_test_count[pid] = len(tests)

    # T-bins
    bins = {"T=1": [], "T=2": [], "T=3-5": [], "T>=6": []}
    def get_bin(t):
        if t == 1: return "T=1"
        elif t == 2: return "T=2"
        elif t <= 5: return "T=3-5"
        else: return "T>=6"

    results_by_bin = defaultdict(lambda: {"n_tests": 0, "cls_correct": 0, "cwm_correct": 0,
                                           "oracle_correct": 0, "routed_correct": 0,
                                           "n_problems": 0})

    # Per-problem level analysis
    for pid in sorted(groups_cls.keys()):
        T = problem_test_count.get(pid, 1)
        b = get_bin(T)
        results_by_bin[b]["n_problems"] += 1

        cls_tests = sorted(groups_cls.get(pid, []), key=lambda x: x["index"])
        cwm_tests = sorted(groups_cwm.get(pid, []), key=lambda x: x["index"])

        for ct, wt in zip(cls_tests, cwm_tests):
            cc = (ct["pred"] == ct["label"])
            wc = (wt["pred"] == wt["label"])

            results_by_bin[b]["n_tests"] += 1
            results_by_bin[b]["cls_correct"] += int(cc)
            results_by_bin[b]["cwm_correct"] += int(wc)
            results_by_bin[b]["oracle_correct"] += int(cc or wc)

            # Routing: T=1 → CWM (arbitrary, equivalent), T>=2 → CLS
            if T == 1:
                results_by_bin[b]["routed_correct"] += int(wc)  # use CWM for T=1
            else:
                results_by_bin[b]["routed_correct"] += int(cc)  # use CLS for T>=2

    # Also compute "always CLS for T>=2" variant
    total_n = 0
    total_routed = 0
    total_cls = 0
    total_cwm = 0
    total_oracle = 0

    summary = {}
    for b in ["T=1", "T=2", "T=3-5", "T>=6"]:
        r = results_by_bin[b]
        n = r["n_tests"]
        if n == 0:
            continue
        summary[b] = {
            "n_tests": n,
            "n_problems": r["n_problems"],
            "cls_acc": r["cls_correct"] / n * 100,
            "cwm_acc": r["cwm_correct"] / n * 100,
            "oracle_acc": r["oracle_correct"] / n * 100,
            "routed_acc": r["routed_correct"] / n * 100,
        }
        total_n += n
        total_routed += r["routed_correct"]
        total_cls += r["cls_correct"]
        total_cwm += r["cwm_correct"]
        total_oracle += r["oracle_correct"]

    summary["overall"] = {
        "n_tests": total_n,
        "cls_acc": total_cls / total_n * 100,
        "cwm_acc": total_cwm / total_n * 100,
        "oracle_acc": total_oracle / total_n * 100,
        "routed_acc": total_routed / total_n * 100,
    }

    return summary

# ── Heuristic 1b: Route per-problem (all-correct) ────────────────────

def heuristic_complexity_routing_problem_level(cls_preds, cwm_preds):
    """Route at problem level: T=1 → CWM, T>=2 → CLS.
    Problem is 'correct' if all per-test predictions match labels."""
    cls_problems = compute_problem_level_metrics(cls_preds)
    cwm_problems = compute_problem_level_metrics(cwm_preds)

    def get_bin(t):
        if t == 1: return "T=1"
        elif t == 2: return "T=2"
        elif t <= 5: return "T=3-5"
        else: return "T>=6"

    bins = defaultdict(lambda: {"n": 0, "cls_correct": 0, "cwm_correct": 0,
                                 "oracle_correct": 0, "routed_correct": 0})

    all_pids = set(cls_problems.keys()) & set(cwm_problems.keys())
    for pid in sorted(all_pids):
        cp = cls_problems[pid]
        wp = cwm_problems[pid]
        T = cp["n_tests"]
        b = get_bin(T)
        bins[b]["n"] += 1

        cc = cp["all_correct"]
        wc = wp["all_correct"]
        bins[b]["cls_correct"] += int(cc)
        bins[b]["cwm_correct"] += int(wc)
        bins[b]["oracle_correct"] += int(cc or wc)

        if T == 1:
            bins[b]["routed_correct"] += int(wc)
        else:
            bins[b]["routed_correct"] += int(cc)

    total = {"n": 0, "cls_correct": 0, "cwm_correct": 0, "oracle_correct": 0, "routed_correct": 0}
    summary = {}
    for b in ["T=1", "T=2", "T=3-5", "T>=6"]:
        r = bins[b]
        n = r["n"]
        if n == 0:
            continue
        summary[b] = {
            "n_problems": n,
            "cls_acc": r["cls_correct"] / n * 100,
            "cwm_acc": r["cwm_correct"] / n * 100,
            "oracle_acc": r["oracle_correct"] / n * 100,
            "routed_acc": r["routed_correct"] / n * 100,
        }
        for k in total:
            total[k] += r[k]

    n = total["n"]
    summary["overall"] = {
        "n_problems": n,
        "cls_acc": total["cls_correct"] / n * 100,
        "cwm_acc": total["cwm_correct"] / n * 100,
        "oracle_acc": total["oracle_correct"] / n * 100,
        "routed_acc": total["routed_correct"] / n * 100,
    }
    return summary

# ── Heuristic 2: Level-based routing ─────────────────────────────────

def heuristic_level_routing():
    """Trivial routing: function-level → CWM, repo-level → CLS.
    Uses aggregate numbers from comprehensive results summary."""
    return {
        "description": "Function-level: use CWM (diagnostic value, ~equivalent accuracy). Repo-level: use CLS (25pp higher accuracy, 217x throughput).",
        "function_level": {
            "recommended": "CWM",
            "rationale": "CLS 88.43% vs CWM 87.19% (4B mean) — gap 1.24pp not significant after Bonferroni. CWM provides execution trace for diagnosis.",
            "cls_acc_4b_mean": 88.43,
            "cwm_acc_4b_mean": 87.19,
            "gap_pp": 1.24,
        },
        "repo_level": {
            "recommended": "CLS",
            "rationale": "CLS 84.56% vs CWM 58.57% (8B mean). CWM collapses at repo-level complexity. CLS also 217x faster throughput.",
            "cls_acc_8b_mean": 84.56,
            "cwm_acc_8b_mean": 58.57,
            "gap_pp": 25.99,
        },
        "combined_weighted_accuracy": "If 50/50 func/repo split: (87.19 + 84.56)/2 = 85.88% vs best-single CLS (88.43+84.56)/2 = 86.50%. Routing adds no value over always-CLS.",
        "conclusion": "Level-based routing is trivially correct for repo-level (CWM unusable) but at function-level the gap is too small to matter. Net effect: equivalent to always-CLS with CWM diagnostic bonus.",
    }

# ── Heuristic 3: Mutation-type routing ────────────────────────────────

def heuristic_mutation_routing(cls_preds, cwm_preds):
    """Route based on mutation type: use whichever formulation is better per mutation."""
    cls_by_mut = defaultdict(list)
    cwm_by_mut = defaultdict(list)

    for c, w in zip(cls_preds, cwm_preds):
        mt = c.get("mutation_type", "unknown")
        cls_by_mut[mt].append(c["pred"] == c["label"])
        cwm_by_mut[mt].append(w["pred"] == w["label"])

    summary = {}
    total_routed = 0
    total_n = 0
    total_oracle = 0
    total_best_single = 0

    for mt in sorted(cls_by_mut.keys()):
        cls_corr = cls_by_mut[mt]
        cwm_corr = cwm_by_mut[mt]
        n = len(cls_corr)
        cls_acc = sum(cls_corr) / n * 100
        cwm_acc = sum(cwm_corr) / n * 100
        oracle_acc = sum(a or b for a, b in zip(cls_corr, cwm_corr)) / n * 100
        best = max(cls_acc, cwm_acc)
        winner = "CLS" if cls_acc >= cwm_acc else "CWM"

        # Routed = always pick the winner for this mutation type
        routed_correct = sum(cls_corr) if winner == "CLS" else sum(cwm_corr)
        total_routed += routed_correct
        total_n += n
        total_oracle += sum(a or b for a, b in zip(cls_corr, cwm_corr))
        total_best_single += max(sum(cls_corr), sum(cwm_corr))

        summary[mt] = {
            "n": n,
            "cls_acc": round(cls_acc, 2),
            "cwm_acc": round(cwm_acc, 2),
            "oracle_acc": round(oracle_acc, 2),
            "winner": winner,
            "gap_pp": round(abs(cls_acc - cwm_acc), 2),
        }

    overall_cls = sum(sum(v) for v in cls_by_mut.values()) / total_n * 100
    overall_cwm = sum(sum(v) for v in cwm_by_mut.values()) / total_n * 100
    summary["overall"] = {
        "n": total_n,
        "cls_acc": round(overall_cls, 2),
        "cwm_acc": round(overall_cwm, 2),
        "oracle_acc": round(total_oracle / total_n * 100, 2),
        "routed_acc": round(total_routed / total_n * 100, 2),
        "best_single_acc": round(max(overall_cls, overall_cwm), 2),
        "routing_gain_over_best_single_pp": round(total_routed / total_n * 100 - max(overall_cls, overall_cwm), 2),
        "oracle_gap_pp": round(total_oracle / total_n * 100 - total_routed / total_n * 100, 2),
    }
    return summary

# ── Bootstrap CI ──────────────────────────────────────────────────────

def bootstrap_ci(cls_correct, cwm_correct, routed_correct, n_boot=10000, seed=42):
    """Bootstrap 95% CI for routing gain over best single formulation."""
    rng = np.random.default_rng(seed)
    n = len(cls_correct)
    cls_arr = np.array(cls_correct, dtype=float)
    cwm_arr = np.array(cwm_correct, dtype=float)
    routed_arr = np.array(routed_correct, dtype=float)

    gains = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, size=n)
        cls_acc = cls_arr[idx].mean()
        cwm_acc = cwm_arr[idx].mean()
        routed_acc = routed_arr[idx].mean()
        best_single = max(cls_acc, cwm_acc)
        gains.append((routed_acc - best_single) * 100)

    gains = np.array(gains)
    return {
        "mean_gain_pp": round(float(gains.mean()), 3),
        "ci_lo": round(float(np.percentile(gains, 2.5)), 3),
        "ci_hi": round(float(np.percentile(gains, 97.5)), 3),
        "pct_positive": round(float((gains > 0).mean() * 100), 1),
    }

# ── Main ──────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("ROUTING HEURISTIC ANALYSIS")
    print("=" * 60)

    # Load test data for problem structure
    test_data = load_test_data(f"{BASE}/data/test.jsonl")
    print(f"Test data: {len(test_data)} samples")

    # Load all available prediction files
    pred_files = {
        "cls_4b_seed0": ("jsonl", f"{BASE}/predictions_cls_seed0.jsonl"),
        "cwm_4b_seed42": ("json_array", f"{BASE}/eval_results_bf16_predictions.json"),
        "cwm_4b_seed123": ("jsonl", f"{BASE}/predictions_cwm_seed123.jsonl"),
        "cwm_4b_seed789": ("jsonl", f"{BASE}/predictions_cwm_seed789.jsonl"),
        "cwm_4b_seed123_v2": ("json_array", f"{BASE}/eval_cwm_seed123_with_preds_predictions.json"),
        "cls_8b_seed42": ("json_array", f"{BASE}/eval_results/cls8b_seed42_predictions.json"),
        "cls_8b_seed123": ("json_array", f"{BASE}/eval_results/cls8b_seed123_predictions.json"),
    }

    preds = {}
    for name, (fmt, path) in pred_files.items():
        if not os.path.exists(path):
            print(f"  SKIP {name}: {path} not found")
            continue
        try:
            if fmt == "jsonl":
                preds[name] = load_predictions_jsonl(path)
            else:
                preds[name] = load_predictions_json_array(path)
            print(f"  OK {name}: {len(preds[name])} samples, acc={compute_per_test_accuracy(preds[name]):.2f}%")
        except Exception as e:
            print(f"  ERR {name}: {e}")

    # Add mutation_type from test data to predictions that lack it
    test_by_idx = {t["index"]: t for t in test_data}
    for name, pred_list in preds.items():
        for p in pred_list:
            if not p.get("mutation_type"):
                td = test_by_idx.get(p["index"])
                if td:
                    p["mutation_type"] = td["mutation_type"]

    results = {}

    # ── Analyze all CLS-CWM pairs ────────────────────────────────────
    cls_keys = [k for k in preds if "cls" in k]
    cwm_keys = [k for k in preds if "cwm" in k]

    print(f"\nCLS models: {cls_keys}")
    print(f"CWM models: {cwm_keys}")

    # Use best available pairs
    # Primary pair: CLS 4B seed0 + CWM 4B seed42 (closest to matched conditions)
    pairs = []
    for ck in cls_keys:
        for wk in cwm_keys:
            if len(preds[ck]) == len(preds[wk]):
                pairs.append((ck, wk))

    print(f"\nAnalyzing {len(pairs)} CLS-CWM pairs...")

    all_pair_results = {}
    for ck, wk in pairs:
        pair_name = f"{ck}_vs_{wk}"
        print(f"\n{'─'*50}")
        print(f"PAIR: {ck} vs {wk}")
        print(f"{'─'*50}")

        cp = preds[ck]
        wp = preds[wk]

        # Per-test complementarity
        comp = compute_per_test_complementarity(cp, wp)
        print(f"  CLS acc: {comp['cls_acc']:.2f}%")
        print(f"  CWM acc: {comp['cwm_acc']:.2f}%")
        print(f"  Oracle:  {comp['oracle_acc']:.2f}%")
        print(f"  Complementarity: {comp['complementarity_pct']:.1f}%")

        # Heuristic 1: Complexity-based routing (per-test)
        h1_pertest = heuristic_complexity_routing(cp, wp, test_data)
        print(f"\n  H1 (per-test, T=1→CWM, T≥2→CLS):")
        for b in ["T=1", "T=2", "T=3-5", "T>=6", "overall"]:
            if b in h1_pertest:
                r = h1_pertest[b]
                print(f"    {b}: routed={r['routed_acc']:.2f}% cls={r['cls_acc']:.2f}% cwm={r['cwm_acc']:.2f}% oracle={r['oracle_acc']:.2f}%")

        # Heuristic 1b: Complexity-based routing (problem-level)
        h1_problem = heuristic_complexity_routing_problem_level(cp, wp)
        print(f"\n  H1b (problem-level, T=1→CWM, T≥2→CLS):")
        for b in ["T=1", "T=2", "T=3-5", "T>=6", "overall"]:
            if b in h1_problem:
                r = h1_problem[b]
                print(f"    {b}: routed={r['routed_acc']:.2f}% cls={r['cls_acc']:.2f}% cwm={r['cwm_acc']:.2f}% oracle={r['oracle_acc']:.2f}% (n={r['n_problems']})")

        # Heuristic 3: Mutation-type routing
        h3 = heuristic_mutation_routing(cp, wp)
        print(f"\n  H3 (mutation-type routing):")
        for mt in sorted(h3.keys()):
            if mt == "overall":
                continue
            r = h3[mt]
            print(f"    {mt}: cls={r['cls_acc']:.2f}% cwm={r['cwm_acc']:.2f}% → {r['winner']} (gap={r['gap_pp']:.2f}pp)")
        ov = h3["overall"]
        print(f"    OVERALL: routed={ov['routed_acc']:.2f}% best_single={ov['best_single_acc']:.2f}% oracle={ov['oracle_acc']:.2f}%")
        print(f"    Routing gain: {ov['routing_gain_over_best_single_pp']:+.2f}pp")

        # Bootstrap CI for routing gain
        cls_correct = [int(c["pred"] == c["label"]) for c in cp]
        cwm_correct = [int(w["pred"] == w["label"]) for w in wp]

        # H1 routed correct
        cls_groups = group_by_problem(cp)
        h1_routed = []
        for c, w in zip(cp, wp):
            pid = c["problem_id"]
            T = len(cls_groups[pid])
            if T == 1:
                h1_routed.append(int(w["pred"] == w["label"]))
            else:
                h1_routed.append(int(c["pred"] == c["label"]))

        # H3 routed correct
        mut_winners = {}
        cls_by_mut = defaultdict(list)
        cwm_by_mut = defaultdict(list)
        for c, w in zip(cp, wp):
            mt = c.get("mutation_type", "unknown")
            cls_by_mut[mt].append(c["pred"] == c["label"])
            cwm_by_mut[mt].append(w["pred"] == w["label"])
        for mt in cls_by_mut:
            cls_a = sum(cls_by_mut[mt]) / len(cls_by_mut[mt])
            cwm_a = sum(cwm_by_mut[mt]) / len(cwm_by_mut[mt])
            mut_winners[mt] = "CLS" if cls_a >= cwm_a else "CWM"

        h3_routed = []
        for c, w in zip(cp, wp):
            mt = c.get("mutation_type", "unknown")
            if mut_winners.get(mt, "CLS") == "CLS":
                h3_routed.append(int(c["pred"] == c["label"]))
            else:
                h3_routed.append(int(w["pred"] == w["label"]))

        # Bootstrap
        h1_boot = bootstrap_ci(cls_correct, cwm_correct, h1_routed)
        h3_boot = bootstrap_ci(cls_correct, cwm_correct, h3_routed)

        print(f"\n  Bootstrap CI (routing gain over best single, 10k resamples):")
        print(f"    H1: {h1_boot['mean_gain_pp']:+.3f}pp [{h1_boot['ci_lo']:+.3f}, {h1_boot['ci_hi']:+.3f}], positive {h1_boot['pct_positive']:.1f}%")
        print(f"    H3: {h3_boot['mean_gain_pp']:+.3f}pp [{h3_boot['ci_lo']:+.3f}, {h3_boot['ci_hi']:+.3f}], positive {h3_boot['pct_positive']:.1f}%")

        all_pair_results[pair_name] = {
            "complementarity": comp,
            "h1_pertest": h1_pertest,
            "h1_problem": h1_problem,
            "h3_mutation": h3,
            "bootstrap_h1": h1_boot,
            "bootstrap_h3": h3_boot,
        }

    # ── Heuristic 2: Level-based routing (from aggregate data) ───────
    h2 = heuristic_level_routing()
    print(f"\n{'='*60}")
    print("HEURISTIC 2: Level-based routing")
    print(f"{'='*60}")
    print(f"  Function-level: recommend {h2['function_level']['recommended']}")
    print(f"    CLS {h2['function_level']['cls_acc_4b_mean']}% vs CWM {h2['function_level']['cwm_acc_4b_mean']}%")
    print(f"  Repo-level: recommend {h2['repo_level']['recommended']}")
    print(f"    CLS {h2['repo_level']['cls_acc_8b_mean']}% vs CWM {h2['repo_level']['cwm_acc_8b_mean']}%")
    print(f"  Conclusion: {h2['conclusion']}")

    # ── Aggregate across pairs ────────────────────────────────────────
    print(f"\n{'='*60}")
    print("AGGREGATE SUMMARY ACROSS ALL PAIRS")
    print(f"{'='*60}")

    for pair_name, pr in all_pair_results.items():
        comp = pr["complementarity"]
        h1o = pr["h1_pertest"].get("overall", {})
        h3o = pr["h3_mutation"].get("overall", {})
        best_single = max(comp["cls_acc"], comp["cwm_acc"])
        print(f"\n  {pair_name}:")
        print(f"    Best single: {best_single:.2f}%")
        print(f"    H1 (complexity): {h1o.get('routed_acc', 0):.2f}% (delta={h1o.get('routed_acc', 0) - best_single:+.2f}pp)")
        print(f"    H3 (mutation):   {h3o.get('routed_acc', 0):.2f}% (delta={h3o.get('routed_acc', 0) - best_single:+.2f}pp)")
        print(f"    Oracle:          {comp['oracle_acc']:.2f}% (gap from best={comp['oracle_acc'] - best_single:+.2f}pp)")

    results = {
        "pair_results": all_pair_results,
        "h2_level_routing": h2,
        "data_inventory": {
            "prediction_files_loaded": list(preds.keys()),
            "n_pairs_analyzed": len(all_pair_results),
            "test_set_size": len(test_data),
        },
    }

    out_path = f"{BASE}/routing_analysis_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")

if __name__ == "__main__":
    main()
