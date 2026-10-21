#!/usr/bin/env python3
"""Parse all experiments from registry JSON and output structured data."""

import json
import sys

INPUT_FILE = "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/cd03d944-31d8-4706-ad87-0759b31a8651/tool-results/mcp-agent-ml-research-read_registry-1778718961321.txt"
OUTPUT_FILE = "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/all_experiments_parsed.json"


def extract_experiment(exp_id, exp_data):
    """Extract all fields from one experiment into a flat dict."""
    spec = exp_data.get("spec", {})
    metrics = exp_data.get("metrics", {})
    extra = exp_data.get("extra", {})

    # Determine formulation from exp_id
    formulation = None
    eid_lower = exp_id.lower()
    if "cls" in eid_lower:
        formulation = "cls"
    elif "cwm" in eid_lower:
        formulation = "cwm"
    elif "traj" in eid_lower:
        formulation = "traj"
    elif "judge" in eid_lower:
        formulation = "llm-judge"
    elif "oracle" in eid_lower:
        formulation = "oracle-sim"
    elif "bootstrap" in eid_lower or "voting" in eid_lower or "corr" in eid_lower:
        formulation = "analysis"
    elif "p2p" in eid_lower or "mvp" in eid_lower:
        formulation = "analysis"
    else:
        formulation = "other"

    # Determine level
    level = None
    if "repo-level" in eid_lower or "repo" in eid_lower:
        level = "repo"
    elif "traj" in eid_lower:
        level = "trajectory"
    elif any(x in eid_lower for x in ["cls-seed", "cwm-seed", "cls8b", "cwm8b", "cwm-baseline"]):
        level = "function"
    elif "judge" in eid_lower:
        level = "function"
    else:
        level = spec.get("level", "function")

    hypothesis = exp_data.get("hypothesis", spec.get("hypothesis", ""))

    result = {
        "exp_id": exp_id,
        "status": exp_data.get("status"),
        "conclusion": exp_data.get("conclusion"),
        "hypothesis": hypothesis,
        "hypothesis_short": (hypothesis[:80] + "...") if len(hypothesis) > 80 else hypothesis,
        "model_name": spec.get("model_name"),
        "seed": spec.get("seed"),
        "formulation": formulation,
        "level": level,
        # Core metrics
        "accuracy": metrics.get("accuracy") or metrics.get("overall_accuracy"),
        "f1_macro": metrics.get("f1_macro"),
        "pass_f1": metrics.get("pass_f1"),
        "fail_f1": metrics.get("fail_f1"),
        "pass_precision": metrics.get("pass_precision"),
        "pass_recall": metrics.get("pass_recall"),
        "fail_precision": metrics.get("fail_precision"),
        "fail_recall": metrics.get("fail_recall"),
        "unparseable_pct": metrics.get("unparseable") if metrics.get("unparseable") is not None else metrics.get("unparseable_predictions") if metrics.get("unparseable_predictions") is not None else metrics.get("unparseable_pct"),
        "exact_match_rate": metrics.get("exact_match_rate"),
        "test_set_size": spec.get("data_count"),
        # Additional metrics
        "train_loss": metrics.get("train_loss"),
        "eval_loss": metrics.get("eval_loss"),
        "train_runtime_sec": metrics.get("train_runtime_sec"),
        "majority_baseline": metrics.get("majority_baseline"),
        "accuracy_vs_baseline_gap": metrics.get("accuracy_vs_baseline_gap"),
        "trajectory_accuracy": metrics.get("trajectory_accuracy"),
        "unresolved_f1": metrics.get("unresolved_f1"),
        "resolved_f1": metrics.get("resolved_f1"),
        "per_test_consistency": metrics.get("per_test_consistency"),
        # All raw metrics
        "all_metrics": metrics if metrics else None,
        # Spec details
        "server": spec.get("server"),
        "gpu": spec.get("gpu"),
        "checkpoint_path": spec.get("checkpoint_path"),
        "data_path": spec.get("data_path"),
        "learning_rate": spec.get("learning_rate") or spec.get("lr"),
        "batch_size": spec.get("batch_size"),
        "grad_accumulation": spec.get("grad_accumulation"),
        "max_seq_length": spec.get("max_seq_length"),
        "num_train_epochs": spec.get("num_train_epochs") or spec.get("epochs"),
        "lora_rank": spec.get("lora_rank"),
        "lora_alpha": spec.get("lora_alpha"),
        "wall_clock_seconds": spec.get("wall_clock_seconds"),
        "gpu_hours": spec.get("gpu_hours"),
        "hyperparams": spec.get("hyperparams"),
        # Metadata
        "tags": exp_data.get("tags"),
        "notes": exp_data.get("notes"),
        "failure_reason": exp_data.get("failure_reason"),
        "created_at": exp_data.get("created_at"),
        "updated_at": exp_data.get("updated_at"),
        "completed_at": exp_data.get("completed_at"),
        "retry_count": exp_data.get("retry_count"),
        "parent": exp_data.get("parent"),
        "extra": extra if extra else None,
    }
    return result


def main():
    with open(INPUT_FILE, "r") as f:
        raw = json.load(f)

    inner = json.loads(raw["result"])
    experiments_dict = inner["data"]["experiments"]

    all_experiments = []
    for exp_id, exp_data in experiments_dict.items():
        parsed = extract_experiment(exp_id, exp_data)
        all_experiments.append(parsed)

    # Save clean JSON
    with open(OUTPUT_FILE, "w") as f:
        json.dump(all_experiments, f, indent=2, ensure_ascii=False)

    print(f"Total experiments: {len(all_experiments)}")
    print(f"Saved to: {OUTPUT_FILE}")
    print()

    # Print COMPLETE dump of every experiment
    for exp in all_experiments:
        print(f"=== EXP: {exp['exp_id']} ===")
        print(f"  conclusion: {exp['conclusion']}")
        print(f"  status: {exp['status']}")
        print(f"  model: {exp['model_name']}")
        print(f"  seed: {exp['seed']}")
        print(f"  formulation: {exp['formulation']}")
        print(f"  level: {exp['level']}")
        print(f"  accuracy: {exp['accuracy']}")
        print(f"  f1_macro: {exp['f1_macro']}")
        print(f"  pass_f1: {exp['pass_f1']}  fail_f1: {exp['fail_f1']}")
        print(f"  pass_precision: {exp['pass_precision']}  pass_recall: {exp['pass_recall']}")
        print(f"  fail_precision: {exp['fail_precision']}  fail_recall: {exp['fail_recall']}")
        print(f"  unparseable_pct: {exp['unparseable_pct']}")
        print(f"  exact_match_rate: {exp['exact_match_rate']}")
        print(f"  test_set_size: {exp['test_set_size']}")
        print(f"  train_loss: {exp['train_loss']}  eval_loss: {exp['eval_loss']}")
        print(f"  majority_baseline: {exp['majority_baseline']}")
        print(f"  trajectory_accuracy: {exp['trajectory_accuracy']}")
        print(f"  unresolved_f1: {exp['unresolved_f1']}  resolved_f1: {exp['resolved_f1']}")
        print(f"  per_test_consistency: {exp['per_test_consistency']}")
        print(f"  wall_clock_sec: {exp['wall_clock_seconds']}  gpu_hours: {exp['gpu_hours']}")
        print(f"  server: {exp['server']}  gpu: {exp['gpu']}")
        print(f"  lr: {exp['learning_rate']}  batch: {exp['batch_size']}  grad_accum: {exp['grad_accumulation']}")
        print(f"  max_seq_len: {exp['max_seq_length']}  epochs: {exp['num_train_epochs']}")
        print(f"  lora_rank: {exp['lora_rank']}  lora_alpha: {exp['lora_alpha']}")
        print(f"  hyperparams: {json.dumps(exp['hyperparams'], ensure_ascii=False) if exp['hyperparams'] else None}")
        print(f"  hypothesis: {exp['hypothesis_short']}")
        print(f"  tags: {exp['tags']}")
        print(f"  notes: {exp['notes']}")
        print(f"  failure_reason: {exp['failure_reason']}")
        print(f"  created_at: {exp['created_at']}")
        print(f"  completed_at: {exp['completed_at']}")
        print(f"  retry_count: {exp['retry_count']}")
        print(f"  parent: {exp['parent']}")
        print(f"  all_metrics: {json.dumps(exp['all_metrics'], indent=4, ensure_ascii=False) if exp['all_metrics'] else None}")
        print()


if __name__ == "__main__":
    main()
