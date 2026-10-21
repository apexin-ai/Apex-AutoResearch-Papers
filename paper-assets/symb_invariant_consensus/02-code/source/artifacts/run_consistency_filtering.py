"""
Experiment 4: Constraint Consistency Filtering
Input: per-trace constraints from exp-001 (Qwen2.5-14B, FOLIO-204, K=12)
Output: accuracy comparison table (SC vs SICA-full vs SICA-filtered at T=4,6,8)
Dependencies: sica.z3_maxsat (ConstraintDeduplicator, MaxSATSolver), sica.scorer (InvariantScorer)
"""
import json
import os
import sys
import time
import traceback
from collections import Counter
from pathlib import Path

sys.path.insert(0, "/root/symb_invariant_consensus")

from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver, UniqueConstraint
from sica.scorer import InvariantScorer

DATA_DIR = Path("/root/symb_invariant_consensus/results/folio_204_14b")
PER_TRACE_DIR = DATA_DIR / "per_trace_constraints"
RESULTS_FILE = DATA_DIR / "folio_204_results.json"
OUTPUT_DIR = Path("/root/symb_invariant_consensus/results/exp4_consistency_filtering")

THRESHOLDS = [1, 4, 6, 8]
K = 12


def normalize_logic_answer(ans: str) -> str:
    ans = ans.strip().lower()
    if ans in ("true", "yes"):
        return "True"
    if ans in ("false", "no"):
        return "False"
    if ans in ("unknown", "uncertain", "undetermined"):
        return "Unknown"
    return ans.capitalize()


def load_per_trace(pid: str) -> dict | None:
    fp = PER_TRACE_DIR / f"{pid}.json"
    if not fp.exists():
        return None
    with open(fp) as f:
        return json.load(f)


def run_filtered_sica(per_trace_data: dict, threshold: int):
    """Run dedup -> filter by threshold -> MaxSAT -> score. Returns (answer, scores, diagnostics)."""
    traces_raw = per_trace_data["per_trace"]

    all_constraints = []
    traces_for_scorer = []
    for t in traces_raw:
        constraints = t.get("constraints", [])
        all_constraints.append(constraints)
        ans = t.get("answer") or t.get("extracted_answer") or ""
        ans = normalize_logic_answer(ans)
        traces_for_scorer.append({"answer": ans, "trace_idx": t["trace_idx"]})

    deduplicator = ConstraintDeduplicator()
    unique_constraints = deduplicator.deduplicate(all_constraints)

    total_unique = len(unique_constraints)

    filtered = [uc for uc in unique_constraints if len(uc.source_traces) >= threshold]

    solver = MaxSATSolver()
    maxsat_result = solver.solve(filtered, timeout_ms=10000)

    candidates = list(set(t["answer"] for t in traces_for_scorer if t["answer"]))
    answer_counts = Counter(t["answer"] for t in traces_for_scorer if t["answer"])

    scorer = InvariantScorer()
    scores = scorer.score(maxsat_result, traces_for_scorer, candidates)
    selected = scorer.select_answer(scores, answer_counts)

    diagnostics = {
        "total_unique": total_unique,
        "filtered_count": len(filtered),
        "filter_ratio": len(filtered) / total_unique if total_unique > 0 else 0,
        "satisfied": len(maxsat_result.satisfied),
        "excluded": len(maxsat_result.excluded),
    }

    return selected, scores, diagnostics


def get_sc_answer(traces_for_scorer: list[dict]) -> str:
    counts = Counter(t["answer"] for t in traces_for_scorer if t["answer"])
    if not counts:
        return ""
    max_count = max(counts.values())
    top = [a for a, c in counts.items() if c == max_count]
    return top[0]


def main():
    with open(RESULTS_FILE) as f:
        results_data = json.load(f)

    gt_map = {}
    for r in results_data["results"]:
        gt_map[r["problem_id"]] = r["ground_truth"]

    pids = sorted(gt_map.keys(), key=lambda x: int(x.split("_")[1]))
    n_problems = len(pids)

    print(f"Problems: {n_problems}")
    print(f"Thresholds: {THRESHOLDS}")
    print(f"K = {K}")
    print()

    correct = {f"T={t}": 0 for t in THRESHOLDS}
    correct["SC"] = 0
    diag_agg = {f"T={t}": {"total_unique": 0, "filtered_count": 0, "satisfied": 0, "excluded": 0} for t in THRESHOLDS}
    errors = []

    t_start = time.perf_counter()

    for i, pid in enumerate(pids):
        if (i + 1) % 50 == 0:
            elapsed = time.perf_counter() - t_start
            print(f"  [{i+1}/{n_problems}] elapsed={elapsed:.1f}s")

        ptc = load_per_trace(pid)
        if ptc is None:
            errors.append(f"{pid}: per_trace file missing")
            continue

        gt = gt_map[pid]

        traces_raw = ptc["per_trace"]
        traces_for_sc = []
        for t in traces_raw:
            ans = t.get("answer") or t.get("extracted_answer") or ""
            ans = normalize_logic_answer(ans)
            traces_for_sc.append({"answer": ans, "trace_idx": t["trace_idx"]})
        sc_ans = get_sc_answer(traces_for_sc)
        if normalize_logic_answer(sc_ans) == normalize_logic_answer(gt):
            correct["SC"] += 1

        for threshold in THRESHOLDS:
            try:
                ans, scores, diag = run_filtered_sica(ptc, threshold)
                if normalize_logic_answer(ans) == normalize_logic_answer(gt):
                    correct[f"T={threshold}"] += 1
                key = f"T={threshold}"
                for field in ["total_unique", "filtered_count", "satisfied", "excluded"]:
                    diag_agg[key][field] += diag[field]
            except Exception as e:
                errors.append(f"{pid} T={threshold}: {e}")

    elapsed_total = time.perf_counter() - t_start

    accuracies = {}
    for key, c in correct.items():
        accuracies[key] = c / n_problems

    print("=" * 65)
    print(f"{'Method':<25} {'Correct':>8} {'Accuracy':>10}")
    print("-" * 65)
    print(f"{'SC (baseline)':<25} {correct['SC']:>8} {accuracies['SC']:>10.4f}")
    for t in THRESHOLDS:
        key = f"T={t}"
        label = f"SICA (T={t}, {'all' if t == 1 else f'>={t}/{K}'})"
        print(f"{label:<25} {correct[key]:>8} {accuracies[key]:>10.4f}")
    print("=" * 65)

    print()
    print("Diagnostics (averages per problem):")
    print(f"{'Threshold':<12} {'Unique':>8} {'Filtered':>10} {'Filter%':>9} {'Satisfied':>10} {'Excluded':>10}")
    print("-" * 65)
    for t in THRESHOLDS:
        key = f"T={t}"
        d = diag_agg[key]
        avg_u = d["total_unique"] / n_problems
        avg_f = d["filtered_count"] / n_problems
        avg_s = d["satisfied"] / n_problems
        avg_e = d["excluded"] / n_problems
        filt_pct = d["filtered_count"] / d["total_unique"] * 100 if d["total_unique"] > 0 else 0
        print(f"T={t:<9} {avg_u:>8.1f} {avg_f:>10.1f} {filt_pct:>8.1f}% {avg_s:>10.1f} {avg_e:>10.1f}")

    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors[:10]:
            print(f"  {e}")

    print(f"\nTotal time: {elapsed_total:.1f}s")

    output = {
        "experiment": "exp4_consistency_filtering",
        "dataset": "folio_204",
        "model": "Qwen2.5-14B",
        "K": K,
        "thresholds": THRESHOLDS,
        "n_problems": n_problems,
        "accuracies": accuracies,
        "correct_counts": correct,
        "diagnostics": {
            f"T={t}": {
                "avg_unique": diag_agg[f"T={t}"]["total_unique"] / n_problems,
                "avg_filtered": diag_agg[f"T={t}"]["filtered_count"] / n_problems,
                "filter_ratio": diag_agg[f"T={t}"]["filtered_count"] / diag_agg[f"T={t}"]["total_unique"]
                if diag_agg[f"T={t}"]["total_unique"] > 0 else 0,
                "avg_satisfied": diag_agg[f"T={t}"]["satisfied"] / n_problems,
                "avg_excluded": diag_agg[f"T={t}"]["excluded"] / n_problems,
            }
            for t in THRESHOLDS
        },
        "errors": errors,
        "wall_time_s": round(elapsed_total, 1),
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / "results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
