"""Main pipeline entry point.

Usage:
    python -m src.run_pipeline --step extract    # hidden state extraction
    python -m src.run_pipeline --step train      # train probes
    python -m src.run_pipeline --step eval       # evaluate
    python -m src.run_pipeline --step all        # full pipeline
"""

import argparse
import os
import sys
import json
from pathlib import Path

import numpy as np
import torch

from .config import (
    HIDDEN_STATES_DIR, PROBES_DIR, ARTIFACTS_DIR,
    SEED, DEVICE, DEFAULT_LAYER, LAYERS
)
from .data_loader import prepare_dataset, split_data, get_commitment_point_stats


def set_seed(seed: int = SEED):
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def step_extract(traces):
    """Extract hidden states from model."""
    from .extract_hidden_states import extract_all_hidden_states

    all_traces = traces["jailbreak_with_commitment"] + traces["safe"]
    print(f"Extracting hidden states for {len(all_traces)} traces...")
    extract_all_hidden_states(all_traces)


def step_train(traces):
    """Train static and temporal probes."""
    from .baselines.linear_probe import train_mlp_probe, save_probe as save_static
    from .crta.temporal_probe import train_temporal_probe, save_probe as save_temporal

    jb_traces = traces["jailbreak_with_commitment"]
    train, val, test = split_data(jb_traces)

    print(f"\nSplit: {len(train)} train / {len(val)} val / {len(test)} test")

    # Train static probe
    print("\n--- Training Static Probe (MLP) ---")
    static_model = train_mlp_probe(train, val)
    save_static(static_model)

    # Train temporal probe
    print("\n--- Training Temporal Probe ---")
    temporal_model = train_temporal_probe(train, val)
    save_temporal(temporal_model)

    return train, val, test


def step_eval(traces):
    """Evaluate probes on test set."""
    from .baselines.linear_probe import MLPProbe, predict_mlp
    from .crta.temporal_probe import TemporalProbe, predict_temporal
    from .eval.evaluate import evaluate_all

    jb_traces = traces["jailbreak_with_commitment"]
    _, _, test = split_data(jb_traces)

    print(f"\nEvaluating on {len(test)} test traces...")

    # Load static probe
    static_model = MLPProbe()
    static_path = PROBES_DIR / "static_mlp_probe.pt"
    static_model.load_state_dict(torch.load(static_path, map_location="cpu", weights_only=False))

    # Load temporal probe
    temporal_model = TemporalProbe()
    temporal_path = PROBES_DIR / "temporal_probe.pt"
    temporal_model.load_state_dict(torch.load(temporal_path, map_location="cpu", weights_only=False))

    # Predict
    preds_static = predict_mlp(static_model, test)
    preds_temporal = predict_temporal(temporal_model, test)

    # Evaluate
    results = evaluate_all(preds_static, preds_temporal)

    # Save results
    results_path = ARTIFACTS_DIR / "eval_results.json"
    serializable = {
        k: {kk: vv for kk, vv in v.items() if kk != "per_trace"}
        for k, v in results.items()
    }
    with open(results_path, "w") as f:
        json.dump(serializable, f, indent=2)
    print(f"\nResults saved to {results_path}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Contrastive Trace Safety Pipeline")
    parser.add_argument("--step", choices=["extract", "train", "eval", "all"],
                        required=True, help="Pipeline step to run")
    args = parser.parse_args()

    set_seed()

    # Always load data
    print("Loading dataset...")
    traces = prepare_dataset()

    jb = traces["jailbreak_with_commitment"]
    jb_no = traces["jailbreak_no_commitment"]
    safe = traces["safe"]
    print(f"Jailbreak with commitment: {len(jb)}")
    print(f"Jailbreak without commitment: {len(jb_no)}")
    print(f"Safe traces: {len(safe)}")

    stats = get_commitment_point_stats(jb)
    print(f"\nCommitment point stats:")
    print(f"  Mean: {stats['mean']:.1f}, Median: {stats['median']:.1f}")
    print(f"  Relative position: {stats['relative_position_mean']:.2%} through trace")

    os.makedirs(HIDDEN_STATES_DIR, exist_ok=True)
    os.makedirs(PROBES_DIR, exist_ok=True)

    if args.step == "extract" or args.step == "all":
        step_extract(traces)

    if args.step == "train" or args.step == "all":
        step_train(traces)

    if args.step == "eval" or args.step == "all":
        step_eval(traces)


if __name__ == "__main__":
    main()
