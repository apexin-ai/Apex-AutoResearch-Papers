"""
Experiment 4: Constraint Consistency Filtering
Input: per-trace constraints from exp-001 (Qwen2.5-14B, FOLIO-204, K=12)
Output: accuracy comparison table (SC vs SICA-full vs SICA-filtered at T=4,6,8)
Dependencies: sica.z3_maxsat (ConstraintDeduplicator, MaxSATSolver), sica.scorer (InvariantScorer)
"""
import json
import sys
import time
import traceback
from collections import Counter
from pathlib import Path

sys.path.insert(0, "/root/symb_invariant_consensus")

from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver
from sica.scorer import InvariantScorer

DATA_DIR = Path("/root/symb_invariant_consensus/results/folio_204_14b")
PER_TRACE_DIR = DATA_DIR / "per_trace_constraints"
RESULTS_FILE = DATA_DIR / "folio_204_results.json"
OUTPUT_DIR = Path("/root/symb_invariant_consensus/results/exp4_consistency_filtering")

THRESHOLDS = [1, 4, 6, 8]
K = 12


def normalize_logic_answer(ans: str) -> str:
    a = ans.strip().lower()
    if a in ("true", "yes"):
        return "True"
    if a in ("false", "no"):
        return "False"
    if a in ("unknown", "uncertain", "undetermined"):
        return "Unknown"
    return a.capitalize()


def process_problem(ptc_data: dict, gt: str, thresholds: list[int]):
    """Dedup once, then filter+MaxSAT+score at each threshold."""
    traces_raw = ptc_data["per_trace"]

    all_constraints = []
    traces_info = []
    for t in traces_raw:
        all_constraints.append(t.get("constraints", []))
        ans = normalize_logic_answer(t.get("answer") or t.get("extracted_answer") or "")
        traces_info.append({"answer": ans, "trace_idx": t["trace_idx"]})

    # SC baseline
    counts = Counter(t["answer"] for t in traces_info if t["answer"])
    sc_ans = max(counts, key=counts.get) if counts else ""
    sc_correct = normalize_logic_answer(sc_ans) == normalize_logic_answer(gt)

    # Dedup once
    deduplicator = ConstraintDeduplicator()
    unique_constraints = deduplicator.deduplicate(all_constraints)
    total_unique = len(unique_constraints)

    candidates = sorted(set(t["answer"] for t in traces_info if t["answer"]))
    answer_counts = dict(counts)

    results = {"SC": {"correct": sc_correct}}
    solver = MaxSATSolver()
    scorer = InvariantScorer()

    for threshold in thresholds:
        filtered = [uc for uc in unique_constraints if len(uc.source_traces) >= threshold]
        maxsat_result = solver.solve(filtered, timeout_ms=10000)
        scores = scorer.score(maxsat_result, traces_info, candidates)
        selected = scorer.select_answer(scores, answer_counts)
        is_correct = normalize_logic_answer(selected) == normalize_logic_answer(gt)

        results[f"T={threshold}"] = {
            "correct": is_correct,
            "answer": selected,
            "total_unique": total_unique,
            "filtered_count": len(filtered),
            "satisfied": len(maxsat_result.satisfied),
            "excluded": len(maxsat_result.excluded),
        }

    return results


def main():
    print("Loading data...", flush=True)
    with open(RESULTS_FILE) as f:
        results_data = json.load(f)

    gt_map = {}
    for r in results_data["results"]:
        gt_map[r["problem_id"]] = r["ground_truth"]

    pids = sorted(gt_map.keys(), key=lambda x: int(x.split("_")[1]))
    n = len(pids)

    print(f"Problems: {n}, Thresholds: {THRESHOLDS}, K={K}", flush=True)

    correct = {"SC": 0}
    for t in THRESHOLDS:
        correct[f"T={t}"] = 0
    diag_agg = {f"T={t}": {"total_unique": 0, "filtered_count": 0, "satisfied": 0, "excluded": 0} for t in THRESHOLDS}
    errors = []

    t_start = time.perf_counter()

    for i, pid in enumerate(pids):
        if (i + 1) % 20 == 0:
            elapsed = time.perf_counter() - t_start
            print(f"  [{i+1}/{n}] {elapsed:.0f}s", flush=True)

        fp = PER_TRACE_DIR / f"{pid}.json"
        if not fp.exists():
            errors.append(f"{pid}: missing")
            continue

        with open(fp) as f:
            ptc = json.load(f)

        try:
            res = process_problem(ptc, gt_map[pid], THRESHOLDS)
        except Exception as e:
            errors.append(f"{pid}: {e}")
            continue

        if res["SC"]["correct"]:
            correct["SC"] += 1

        for t in THRESHOLDS:
            key = f"T={t}"
            r = res[key]
            if r["correct"]:
                correct[key] += 1
            for field in ["total_unique", "filtered_count", "satisfied", "excluded"]:
                diag_agg[key][field] += r[field]

    elapsed_total = time.perf_counter() - t_start

    acc = {k: v / n for k, v in correct.items()}

    print(flush=True)
    print("=" * 65, flush=True)
    print(f"{'Method':<25} {'Correct':>8} {'Accuracy':>10}", flush=True)
    print("-" * 65, flush=True)
    print(f"{'SC (baseline)':<25} {correct['SC']:>8} {acc['SC']:>10.4f}", flush=True)
    for t in THRESHOLDS:
        key = f"T={t}"
        label = f"SICA (T={t}, {'all' if t == 1 else f'>={t}/{K}'})"
        print(f"{label:<25} {correct[key]:>8} {acc[key]:>10.4f}", flush=True)
    print("=" * 65, flush=True)

    print(flush=True)
    print("Diagnostics (averages per problem):", flush=True)
    print(f"{'Threshold':<12} {'Unique':>8} {'Filtered':>10} {'Filter%':>9} {'Satisfied':>10} {'Excluded':>10}", flush=True)
    print("-" * 65, flush=True)
    for t in THRESHOLDS:
        key = f"T={t}"
        d = diag_agg[key]
        avg_u = d["total_unique"] / n
        avg_f = d["filtered_count"] / n
        avg_s = d["satisfied"] / n
        avg_e = d["excluded"] / n
        filt_pct = d["filtered_count"] / d["total_unique"] * 100 if d["total_unique"] > 0 else 0
        print(f"T={t:<9} {avg_u:>8.1f} {avg_f:>10.1f} {filt_pct:>8.1f}% {avg_s:>10.1f} {avg_e:>10.1f}", flush=True)

    if errors:
        print(f"\nErrors ({len(errors)}):", flush=True)
        for e in errors[:10]:
            print(f"  {e}", flush=True)

    print(f"\nTotal time: {elapsed_total:.1f}s", flush=True)

    output = {
        "experiment": "exp4_consistency_filtering",
        "dataset": "folio_204",
        "model": "Qwen2.5-14B",
        "K": K,
        "thresholds": THRESHOLDS,
        "n_problems": n,
        "accuracies": acc,
        "correct_counts": correct,
        "diagnostics": {
            f"T={t}": {
                "avg_unique": diag_agg[f"T={t}"]["total_unique"] / n,
                "avg_filtered": diag_agg[f"T={t}"]["filtered_count"] / n,
                "filter_ratio": diag_agg[f"T={t}"]["filtered_count"] / diag_agg[f"T={t}"]["total_unique"]
                if diag_agg[f"T={t}"]["total_unique"] > 0 else 0,
                "avg_satisfied": diag_agg[f"T={t}"]["satisfied"] / n,
                "avg_excluded": diag_agg[f"T={t}"]["excluded"] / n,
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
    print(f"\nResults saved to {out_path}", flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
