"""Cluster-robust bootstrap CI for trace-verdict-study predictions."""

import json
import os
import sys
from collections import defaultdict

import numpy as np

CKPT_DIR = "/root/autodl-tmp/trace-verdict-study-checkpoints"
DATA_DIR = "/root/autodl-tmp/trace-verdict-study-data"
OUT_DIR = "/root/autodl-tmp/trace-verdict-study-checkpoints/analysis"

CONDITION_TO_TESTFILE = {
    "ae_only": "ae_only_test.jsonl",
    "exception_only": "exception_only_test.jsonl",
    "exception_only_seed123": "exception_only_test.jsonl",
    "exception_only_seed456": "exception_only_test.jsonl",
    "vota": "vota_test.jsonl",
    "vota_seed456": "vota_test.jsonl",
    "vota_no_ae": "vota_no_ae_test.jsonl",
    "loop_only": "loop_only_test.jsonl",
    "full_trace": "full_trace_test.jsonl",
    "full_trace_label_only": "full_trace_test.jsonl",
    "full_trace_256tok": "full_trace_test.jsonl",
    "full_trace_512tok": "full_trace_test.jsonl",
    "full_trace_1024tok": "full_trace_test.jsonl",
    "no_trace": "no_trace_test.jsonl",
    "deepseek_vota": "vota_test.jsonl",
    "deepseek_no_trace": "no_trace_test.jsonl",
    "deepseek_exception_only": "exception_only_test.jsonl",
    "deepseek_exception_only_seed123": "exception_only_test.jsonl",
    "deepseek_exception_only_seed456": "exception_only_test.jsonl",
    "deepseek_full_trace": "full_trace_test.jsonl",
    "deepseek_full_trace_seed42_v3": "full_trace_test.jsonl",
    "debugbench_vota": "debugbench_vota_test.jsonl",
    "debugbench_no_trace": "debugbench_no_trace_test.jsonl",
    "debugbench_exception_only": "debugbench_exception_only_test.jsonl",
}

B = 10000
SEED = 42


def load_jsonl(path):
    data = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(json.loads(line))
    return data


def wilson_ci(n_correct, n_total, z=1.96):
    if n_total == 0:
        return [0.0, 0.0]
    p = n_correct / n_total
    denom = 1 + z**2 / n_total
    center = (p + z**2 / (2 * n_total)) / denom
    margin = z * np.sqrt(p * (1 - p) / n_total + z**2 / (4 * n_total**2)) / denom
    return [float(max(0, center - margin)), float(min(1, center + margin))]


def cluster_robust_bootstrap(problem_accs, rng, B=10000):
    """Bootstrap over problem-level accuracies (cluster units)."""
    n = len(problem_accs)
    boot_means = np.empty(B)
    for b in range(B):
        idx = rng.integers(0, n, size=n)
        boot_means[b] = problem_accs[idx].mean()
    lo = float(np.percentile(boot_means, 2.5))
    hi = float(np.percentile(boot_means, 97.5))
    return [lo, hi]


def process_condition(cond_name, pred_path, test_file, rng):
    preds = load_jsonl(pred_path)
    test_data = load_jsonl(os.path.join(DATA_DIR, test_file))

    assert len(preds) == len(test_data), (
        f"{cond_name}: pred({len(preds)}) != test({len(test_data)})"
    )

    # Build per-problem accuracy
    problem_correct = defaultdict(list)
    n_correct = 0
    for p, t in zip(preds, test_data):
        pid = t["problem_id"]
        correct = int(p["pred"] == t["output"])
        problem_correct[pid].append(correct)
        n_correct += correct

    n_samples = len(preds)
    n_problems = len(problem_correct)
    sample_accuracy = n_correct / n_samples

    # Problem-level accuracy: mean of per-problem accuracy
    problem_accs = np.array([
        np.mean(v) for v in problem_correct.values()
    ])
    problem_accuracy = float(problem_accs.mean())

    # Cluster-robust bootstrap CI
    cr_ci = cluster_robust_bootstrap(problem_accs, rng, B=B)

    # Wilson CI (sample-level, ignoring clustering)
    w_ci = wilson_ci(n_correct, n_samples)

    return {
        "n_samples": n_samples,
        "n_problems": n_problems,
        "sample_accuracy": round(sample_accuracy, 6),
        "problem_accuracy": round(problem_accuracy, 6),
        "cluster_robust_ci": [round(cr_ci[0], 6), round(cr_ci[1], 6)],
        "wilson_ci": [round(w_ci[0], 6), round(w_ci[1], 6)],
        "bootstrap_B": B,
    }


def main():
    rng = np.random.default_rng(SEED)

    # Discover all final prediction files
    results = {}
    for cond_name, test_file in sorted(CONDITION_TO_TESTFILE.items()):
        pred_path = os.path.join(CKPT_DIR, cond_name, "final", "predictions.jsonl")
        if not os.path.exists(pred_path):
            print(f"SKIP {cond_name}: {pred_path} not found", file=sys.stderr)
            continue
        print(f"Processing {cond_name}...", file=sys.stderr)
        results[cond_name] = process_condition(cond_name, pred_path, test_file, rng)

    output = {"conditions": results}

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "cluster_robust_ci.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}", file=sys.stderr)

    # Print summary table
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
