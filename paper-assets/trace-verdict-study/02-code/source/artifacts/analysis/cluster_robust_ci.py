import json
import numpy as np
from collections import defaultdict
import os
import math

DATA_DIR = "/root/autodl-tmp/trace-verdict-study-data"
CKPT_DIR = "/root/autodl-tmp/trace-verdict-study-checkpoints"
OUT_DIR = f"{CKPT_DIR}/analysis"

CONDITIONS = {
    "ae_only": {"test_file": "ae_only_test.jsonl"},
    "exception_only": {"test_file": "exception_only_test.jsonl"},
    "vota": {"test_file": "vota_test.jsonl"},
    "loop_only": {"test_file": "loop_only_test.jsonl"},
    "full_trace": {"test_file": "full_trace_test.jsonl"},
    "no_trace": {"test_file": "no_trace_test.jsonl"},
    "full_trace_label_only": {"test_file": "full_trace_test.jsonl"},
    "vota_no_ae": {"test_file": "vota_no_ae_test.jsonl"},
    "deepseek_vota": {"test_file": "vota_test.jsonl"},
    "deepseek_no_trace": {"test_file": "no_trace_test.jsonl"},
    "deepseek_exception_only": {"test_file": "exception_only_test.jsonl"},
    "deepseek_full_trace": {"test_file": "full_trace_test.jsonl"},
}

B = 10000
SEED = 42
Z = 1.96


def load_predictions(condition):
    pred_path = f"{CKPT_DIR}/{condition}/final/predictions.jsonl"
    if not os.path.exists(pred_path):
        return None
    preds = []
    with open(pred_path) as f:
        for line in f:
            preds.append(json.loads(line))
    return preds


def load_problem_ids(test_file):
    path = f"{DATA_DIR}/{test_file}"
    pids = []
    with open(path) as f:
        for line in f:
            d = json.loads(line)
            pids.append(d["problem_id"])
    return pids


def wilson_ci(n_correct, n_total, z=Z):
    if n_total == 0:
        return [0.0, 0.0]
    p = n_correct / n_total
    denom = 1 + z**2 / n_total
    center = (p + z**2 / (2 * n_total)) / denom
    spread = z * math.sqrt(p * (1 - p) / n_total + z**2 / (4 * n_total**2)) / denom
    return [center - spread, center + spread]


def cluster_robust_bootstrap(problem_accs, problem_sizes, rng, B=B):
    n_problems = len(problem_accs)
    all_correct = np.array([a * s for a, s in zip(problem_accs, problem_sizes)])
    all_sizes = np.array(problem_sizes)

    boot_accs = np.empty(B)
    for i in range(B):
        idx = rng.integers(0, n_problems, size=n_problems)
        boot_accs[i] = all_correct[idx].sum() / all_sizes[idx].sum()

    lo = np.percentile(boot_accs, 2.5)
    hi = np.percentile(boot_accs, 97.5)
    return [float(lo), float(hi)]


def analyze_condition(condition, test_file):
    preds = load_predictions(condition)
    if preds is None:
        return None

    problem_ids = load_problem_ids(test_file)
    assert len(preds) == len(problem_ids), f"{condition}: {len(preds)} preds vs {len(problem_ids)} test"

    groups = defaultdict(lambda: {"correct": 0, "total": 0})
    total_correct = 0
    for pred, pid in zip(preds, problem_ids):
        correct = 1 if pred["pred"] == pred["label"] else 0
        groups[pid]["correct"] += correct
        groups[pid]["total"] += 1
        total_correct += correct

    n_samples = len(preds)
    n_problems = len(groups)
    sample_acc = total_correct / n_samples

    problem_accs = []
    problem_sizes = []
    for pid in sorted(groups.keys()):
        g = groups[pid]
        problem_accs.append(g["correct"] / g["total"])
        problem_sizes.append(g["total"])

    problem_level_acc = float(np.mean(problem_accs))

    rng = np.random.default_rng(SEED)
    cr_ci = cluster_robust_bootstrap(problem_accs, problem_sizes, rng, B)
    w_ci = wilson_ci(total_correct, n_samples)

    return {
        "n_samples": n_samples,
        "n_problems": n_problems,
        "sample_accuracy": round(sample_acc, 6),
        "problem_level_accuracy": round(problem_level_acc, 6),
        "cluster_robust_ci": [round(cr_ci[0], 6), round(cr_ci[1], 6)],
        "wilson_ci": [round(w_ci[0], 6), round(w_ci[1], 6)],
        "cluster_robust_ci_width": round(cr_ci[1] - cr_ci[0], 6),
        "wilson_ci_width": round(w_ci[1] - w_ci[0], 6),
        "bootstrap_B": B,
    }


def main():
    results = {"conditions": {}}
    skipped = []

    for cond, cfg in CONDITIONS.items():
        r = analyze_condition(cond, cfg["test_file"])
        if r is None:
            skipped.append(cond)
            continue
        results["conditions"][cond] = r

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = f"{OUT_DIR}/cluster_robust_ci.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"{'Condition':<28} {'Acc':>7} {'ProbAcc':>8} {'CR-CI':>20} {'Wilson-CI':>20} {'CR-w':>7} {'W-w':>7} {'#P':>4}")
    print("-" * 110)
    for cond, r in results["conditions"].items():
        cr = r["cluster_robust_ci"]
        w = r["wilson_ci"]
        print(f"{cond:<28} {r['sample_accuracy']:.4f}  {r['problem_level_accuracy']:.4f}  "
              f"[{cr[0]:.4f}, {cr[1]:.4f}]  [{w[0]:.4f}, {w[1]:.4f}]  "
              f"{r['cluster_robust_ci_width']:.4f}  {r['wilson_ci_width']:.4f}  {r['n_problems']:>3}")

    if skipped:
        print(f"\nSkipped (no predictions.jsonl): {', '.join(skipped)}")

    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
