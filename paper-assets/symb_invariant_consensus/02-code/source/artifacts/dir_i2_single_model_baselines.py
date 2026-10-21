#!/usr/bin/env python3
"""Dir-I2: Single-model SC baselines for confound analysis."""

import json
import os
import random
import numpy as np

RESULTS_ROOT = "/root/symb_invariant_consensus/results"
OUTPUT_DIR = "/root/symb_invariant_consensus/results/dir_i2_single_model_baselines"

MODELS = {
    "mistral-7b": f"{RESULTS_ROOT}/exp033_mistral_7b_folio204/intermediates",
    "qwen2.5-7b": f"{RESULTS_ROOT}/exp035_qwen25_7b_folio204/intermediates",
    "qwen2.5-14b": f"{RESULTS_ROOT}/folio_204_14b/intermediates",
    "qwen3-14b": f"{RESULTS_ROOT}/exp027_qwen3_14b_nonthinking/intermediates",
}

N_PROBLEMS = 204
N_SC5_RUNS = 10
VALID_ANSWERS = {"True", "False", "Unknown"}
HGE_B_ACCURACY = 0.8201

random.seed(42)
np.random.seed(42)


def normalize_answer(ans):
    if not ans or not isinstance(ans, str):
        return None
    low = ans.strip().lower()
    if low in ("true", "yes"):
        return "True"
    if low in ("false", "no"):
        return "False"
    if low in ("unknown", "uncertain", "undetermined"):
        return "Unknown"
    return None


def load_model_traces(model_dir):
    """Load all traces for a model. Returns {problem_id: {"answers": [...], "gold": str}}"""
    traces = {}
    for i in range(N_PROBLEMS):
        fpath = os.path.join(model_dir, f"folio_{i}.json")
        with open(fpath) as f:
            data = json.load(f)
        pid = data["problem"]["id"]
        gold = normalize_answer(data["problem"]["answer"]) or data["problem"]["answer"]
        raw = data["sica_result"]["traces"]
        answers = []
        for t in raw:
            norm = normalize_answer(t.get("answer", ""))
            if norm:
                answers.append(norm)
        traces[pid] = {"answers": answers, "gold": gold}
    return traces


def majority_vote(answers):
    """Majority vote with dict-insertion-order tiebreak."""
    counts = {}
    for a in answers:
        if a in VALID_ANSWERS:
            counts[a] = counts.get(a, 0) + 1
    if not counts:
        return None
    return max(counts, key=counts.get)


def compute_sc_accuracy(traces, k=None, seed=None):
    """Compute SC accuracy. If k is given, subsample k traces per problem."""
    if seed is not None:
        rng = random.Random(seed)
    correct = 0
    total = 0
    for pid in sorted(traces.keys()):
        info = traces[pid]
        answers = info["answers"]
        if not answers:
            continue
        if k is not None:
            if len(answers) < k:
                continue
            answers = rng.sample(answers, k)
        pred = majority_vote(answers)
        if pred is None:
            continue
        total += 1
        if pred == info["gold"]:
            correct += 1
    return correct, total


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    results = {"models": {}}

    for model_name, model_dir in MODELS.items():
        print(f"\n=== {model_name} ===")
        traces = load_model_traces(model_dir)

        n_traces_list = [len(traces[pid]["answers"]) for pid in traces]
        min_traces = min(n_traces_list)
        max_traces = max(n_traces_list)
        median_traces = int(np.median(n_traces_list))
        print(f"  Traces per problem: min={min_traces}, max={max_traces}, median={median_traces}")

        # SC@all
        correct_all, total_all = compute_sc_accuracy(traces)
        acc_all = correct_all / total_all if total_all > 0 else 0
        print(f"  SC@all: {correct_all}/{total_all} = {acc_all:.4f}")

        model_result = {
            "n_traces_min": min_traces,
            "n_traces_max": max_traces,
            "n_traces_median": median_traces,
            "sc_all_accuracy": round(acc_all, 4),
            "sc_all_correct": correct_all,
            "sc_all_total": total_all,
        }

        # SC@5
        if min_traces >= 5:
            sc5_runs = []
            for run_i in range(N_SC5_RUNS):
                c, t = compute_sc_accuracy(traces, k=5, seed=run_i * 1000 + 42)
                sc5_runs.append(round(c / t, 4) if t > 0 else 0)
            sc5_mean = round(np.mean(sc5_runs), 4)
            sc5_std = round(np.std(sc5_runs), 4)
            print(f"  SC@5: {sc5_mean} ± {sc5_std}  runs={sc5_runs}")
            model_result["sc5_mean"] = sc5_mean
            model_result["sc5_std"] = sc5_std
            model_result["sc5_runs"] = sc5_runs
        else:
            print(f"  SC@5: SKIPPED (min traces = {min_traces} < 5)")
            model_result["sc5_note"] = f"skipped, min_traces={min_traces}"

        results["models"][model_name] = model_result

    # Find best single model
    best_model = max(results["models"], key=lambda m: results["models"][m]["sc_all_accuracy"])
    best_acc = results["models"][best_model]["sc_all_accuracy"]
    true_gain = round(HGE_B_ACCURACY - best_acc, 4)

    results["best_single_model"] = best_model
    results["best_single_accuracy"] = best_acc
    results["hge_b_accuracy"] = HGE_B_ACCURACY
    results["true_ensemble_gain_pp"] = true_gain

    print(f"\n=== SUMMARY ===")
    print(f"Best single model: {best_model} ({best_acc:.4f})")
    print(f"HGE-(b) accuracy: {HGE_B_ACCURACY:.4f}")
    print(f"True ensemble gain: {true_gain:.4f} ({true_gain*100:.2f} pp)")
    if best_acc >= 0.80:
        print("WARNING: Best single model ≥ 80%, HGE gain may be from stronger model, not ensemble diversity")
    else:
        print("Ensemble diversity is a key contributor to HGE gain")

    out_path = os.path.join(OUTPUT_DIR, "results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
