#!/usr/bin/env python3
"""Alpha ablation: test if MAX-SAT vs count-only agreement is sensitive to alpha mixing."""

import json
import os
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, "/root/symb_invariant_consensus")
from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver, MaxSATResult
from sica.scorer import InvariantScorer

CONDITIONS = {
    "Mistral-7B_FOLIO": {
        "constraint_dir": "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache",
        "results_file": "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json",
        "label": "Mistral-7B x FOLIO (BR=4.97)",
    },
    "Qwen25-14B_FOLIO": {
        "constraint_dir": "/root/symb_invariant_consensus/results/multi_seed/qwen25_folio_seed123/per_trace_constraints",
        "results_file": "/root/symb_invariant_consensus/results/multi_seed/qwen25_folio_seed123/results.json",
        "label": "Qwen2.5-14B x FOLIO (seed123)",
    },
}

ALPHAS = [0.1, 0.3, 0.5, 0.7, 0.9]
ALPHA_PENALTY = 0.5
N_PROBLEMS = 204


def norm_ans(ans):
    a = str(ans).strip().lower()
    if a in ("true", "yes", "t"):
        return "True"
    if a in ("false", "no", "f"):
        return "False"
    if a in ("unknown", "uncertain", "u", "undetermined", ""):
        return "Unknown"
    return a.capitalize()


def normalize_to_dist(scores):
    if not scores:
        return {}
    min_v = min(scores.values())
    shifted = {k: v - min_v for k, v in scores.items()} if min_v < 0 else dict(scores)
    total = sum(shifted.values())
    if total == 0:
        n = len(shifted)
        return {k: 1.0 / n for k in shifted}
    return {k: v / total for k, v in shifted.items()}


def mix_select(c_dist, v_dist, alpha, candidates):
    final = {}
    for c in candidates:
        final[c] = alpha * c_dist.get(c, 0.0) + (1 - alpha) * v_dist.get(c, 0.0)
    mx = max(final.values())
    winners = sorted(c for c, s in final.items() if abs(s - mx) < 1e-9)
    return winners[0]


def sc_answer(vote_counts):
    if not vote_counts:
        return "Unknown"
    mx = max(vote_counts.values())
    return sorted(a for a, c in vote_counts.items() if c == mx)[0]


def run_condition(name, config):
    cdir = config["constraint_dir"]

    per_alpha = {a: {"ms_ok": 0, "co_ok": 0, "agree": 0, "n": 0, "sc_ok": 0} for a in ALPHAS}
    per_problem = []
    skipped = 0

    t0 = time.time()
    for i in range(N_PROBLEMS):
        pid = f"folio_{i}"
        cpath = os.path.join(cdir, f"{pid}.json")
        if not os.path.exists(cpath):
            skipped += 1
            continue

        with open(cpath) as f:
            cdata = json.load(f)

        gt = norm_ans(cdata["gt"])
        per_trace = cdata["per_trace"]

        trace_dicts = []
        all_constraints = []
        for t in per_trace:
            ans = norm_ans(t.get("answer", ""))
            trace_dicts.append({"trace_idx": t["trace_idx"], "answer": ans})
            all_constraints.append(t.get("constraints", []))

        valid_ans = [td["answer"] for td in trace_dicts if td["answer"]]
        vote_counts = Counter(valid_ans)
        candidates = sorted(set(valid_ans))

        if not candidates:
            skipped += 1
            continue

        sc_ans = sc_answer(vote_counts)

        deduplicator = ConstraintDeduplicator()
        unique = deduplicator.deduplicate(all_constraints)

        solver = MaxSATSolver()
        ms_result = solver.solve(unique, timeout_ms=10000)

        co_result = MaxSATResult(
            satisfied=list(unique),
            excluded=[],
            total_weight=sum(uc.weight for uc in unique),
            solve_time_ms=0.0,
        )

        scorer = InvariantScorer(alpha=ALPHA_PENALTY)
        ms_scores = scorer.score(ms_result, trace_dicts, candidates)
        co_scores = scorer.score(co_result, trace_dicts, candidates)

        ms_dist = normalize_to_dist(ms_scores)
        co_dist = normalize_to_dist(co_scores)
        total_votes = sum(vote_counts.get(c, 0) for c in candidates)
        v_dist = {c: vote_counts.get(c, 0) / total_votes for c in candidates} if total_votes > 0 else {c: 1.0 / len(candidates) for c in candidates}

        detail = {"pid": pid, "gt": gt, "sc": sc_ans, "sc_correct": sc_ans == gt}

        for alpha in ALPHAS:
            ms_ans = mix_select(ms_dist, v_dist, alpha, candidates)
            co_ans = mix_select(co_dist, v_dist, alpha, candidates)

            per_alpha[alpha]["ms_ok"] += (ms_ans == gt)
            per_alpha[alpha]["co_ok"] += (co_ans == gt)
            per_alpha[alpha]["agree"] += (ms_ans == co_ans)
            per_alpha[alpha]["n"] += 1
            per_alpha[alpha]["sc_ok"] += (sc_ans == gt)

            detail[f"a{alpha}"] = {"maxsat": ms_ans, "countonly": co_ans, "agree": ms_ans == co_ans}

        per_problem.append(detail)

        if (i + 1) % 50 == 0:
            elapsed = time.time() - t0
            print(f"  [{i+1}/{N_PROBLEMS}] {elapsed:.1f}s")

    elapsed = time.time() - t0
    print(f"  Done: {N_PROBLEMS - skipped} problems, {skipped} skipped, {elapsed:.1f}s")

    summary = {}
    for alpha in ALPHAS:
        d = per_alpha[alpha]
        n = d["n"]
        if n == 0:
            continue
        summary[str(alpha)] = {
            "alpha": alpha,
            "n": n,
            "maxsat_acc": round(d["ms_ok"] / n * 100, 2),
            "countonly_acc": round(d["co_ok"] / n * 100, 2),
            "agreement_pct": round(d["agree"] / n * 100, 1),
            "sc_acc": round(d["sc_ok"] / n * 100, 2),
            "delta_sica_sc_pp": round((d["ms_ok"] - d["sc_ok"]) / n * 100, 2),
        }

    return summary, per_problem


def main():
    output_dir = "/root/symb_invariant_consensus/results/alpha_ablation"
    os.makedirs(output_dir, exist_ok=True)

    all_results = {}

    for name, config in CONDITIONS.items():
        label = config["label"]
        print(f"\n{'=' * 60}")
        print(f"Condition: {label}")
        print(f"{'=' * 60}")

        summary, per_problem = run_condition(name, config)
        all_results[name] = {"label": label, "summary": summary}

        print(f"\n| {'a':>3} | {'SICA_acc':>8} | {'CO_acc':>8} | {'Agree%':>7} | {'SC_acc':>7} | {'D(SICA-SC)':>10} |")
        print(f"|-----|----------|----------|---------|---------|------------|")
        for alpha in ALPHAS:
            s = summary.get(str(alpha))
            if not s:
                continue
            print(f"| {alpha} | {s['maxsat_acc']:>6.2f}% | {s['countonly_acc']:>6.2f}% | {s['agreement_pct']:>5.1f}% | {s['sc_acc']:>5.2f}% | {s['delta_sica_sc_pp']:>+8.2f}pp |")

        with open(os.path.join(output_dir, f"{name}_detail.json"), "w") as f:
            json.dump({"summary": summary, "per_problem": per_problem}, f, indent=2)

    with open(os.path.join(output_dir, "alpha_ablation_combined.json"), "w") as f:
        json.dump(all_results, f, indent=2)

    txt = os.path.join(output_dir, "alpha_ablation_report.txt")
    with open(txt, "w") as f:
        f.write("Alpha Ablation: MAX-SAT vs Count-only Agreement Sensitivity\n")
        f.write("=" * 60 + "\n\n")
        for name in CONDITIONS:
            r = all_results[name]
            f.write(f"Condition: {r['label']}\n")
            f.write(f"| {'a':>3} | {'SICA_acc':>8} | {'CO_acc':>8} | {'Agree%':>7} | {'SC_acc':>7} | {'D(SICA-SC)':>10} |\n")
            f.write(f"|-----|----------|----------|---------|---------|------------|\n")
            for alpha in ALPHAS:
                s = r["summary"].get(str(alpha))
                if not s:
                    continue
                f.write(f"| {alpha} | {s['maxsat_acc']:>6.2f}% | {s['countonly_acc']:>6.2f}% | {s['agreement_pct']:>5.1f}% | {s['sc_acc']:>5.2f}% | {s['delta_sica_sc_pp']:>+8.2f}pp |\n")
            f.write("\n")

    print(f"\nResults saved to {output_dir}")


if __name__ == "__main__":
    main()
