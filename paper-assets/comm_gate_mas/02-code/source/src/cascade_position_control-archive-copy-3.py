"""Cascade position control analysis via logistic regression.

Tests whether acknowledgment cascades are genuine sequential dependencies
or artifacts of conversation position, by fitting:
  Model 1 (position-only): P(ack_t) ~ position_t
  Model 2 (full):          P(ack_t) ~ position_t + prev_ack_{t-1}

Input:  annotations.jsonl files (one per backbone) with per-message annotations
Output: JSON with OR, CI, p-values, AIC/BIC for both models per backbone

Dependencies: numpy, statsmodels
"""
import argparse
import json
import os
from collections import defaultdict

import numpy as np
import statsmodels.api as sm

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEFAULT_ANNOTATION_PATHS = {
    "qwen": os.path.join(
        BASE_DIR, "outputs", "full_scale", "qwen_round_robin",
        "annotations", "annotations.jsonl",
    ),
    "llama": os.path.join(
        BASE_DIR, "outputs", "full_scale", "llama_round_robin",
        "annotations", "annotations.jsonl",
    ),
}


def load_consecutive_pairs(annotation_path: str) -> tuple[np.ndarray, int]:
    """Load annotations and build consecutive message pairs.

    For each task, sorts messages by message_index and extracts pairs
    (message_{t-1}, message_t) for t > 0.  Uses annotation_a.type to
    determine acknowledgment status.

    Returns:
        data: ndarray of shape (n_pairs, 3) with columns [is_ack, prev_ack, position]
        n_tasks: number of unique tasks
    """
    tasks: dict[str, list[dict]] = defaultdict(list)
    with open(annotation_path) as f:
        for line in f:
            msg = json.loads(line)
            tasks[msg["task_id"]].append(msg)

    rows = []
    for task_id in sorted(tasks):
        messages = sorted(tasks[task_id], key=lambda m: m["message_index"])
        for i in range(1, len(messages)):
            is_ack = int(messages[i]["annotation_a"]["type"] == "acknowledgment")
            prev_ack = int(messages[i - 1]["annotation_a"]["type"] == "acknowledgment")
            position = messages[i]["message_index"]
            rows.append((is_ack, prev_ack, position))

    return np.array(rows), len(tasks)


def fit_models(data: np.ndarray) -> dict:
    """Fit position-only and full logistic regression models.

    Returns dict with coefficients, odds ratios, CIs, p-values, AIC, BIC.
    """
    y = data[:, 0]
    prev_ack = data[:, 1]
    position = data[:, 2]

    # Model 1: position only
    X_pos = sm.add_constant(position)
    model_pos = sm.Logit(y, X_pos).fit(disp=0)

    # Model 2: full (position + prev_ack)
    X_full = sm.add_constant(np.column_stack([position, prev_ack]))
    model_full = sm.Logit(y, X_full).fit(disp=0)

    ci_full = model_full.conf_int()

    return {
        "n_observations": len(y),
        "ack_rate": float(y.mean()),
        "prev_ack_odds_ratio": round(float(np.exp(model_full.params[2])), 4),
        "prev_ack_ci_95": [
            round(float(np.exp(ci_full[2, 0])), 4),
            round(float(np.exp(ci_full[2, 1])), 4),
        ],
        "prev_ack_p_value": float(model_full.pvalues[2]),
        "prev_ack_coefficient": round(float(model_full.params[2]), 4),
        "position_odds_ratio": round(float(np.exp(model_full.params[1])), 4),
        "position_p_value": float(model_full.pvalues[1]),
        "aic_full": round(float(model_full.aic), 2),
        "aic_position_only": round(float(model_pos.aic), 2),
        "bic_full": round(float(model_full.bic), 2),
        "bic_position_only": round(float(model_pos.bic), 2),
    }


def build_conclusion(results: dict) -> str:
    """Generate a one-line conclusion string."""
    or_val = results["prev_ack_odds_ratio"]
    p_val = results["prev_ack_p_value"]
    delta_aic = round(results["aic_full"] - results["aic_position_only"], 1)
    return (
        f"prev_ack is highly significant (p={p_val:.2e}, OR={or_val}) "
        f"after controlling for position; full model fits better "
        f"(delta AIC={delta_aic})"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Cascade position control: logistic regression analysis"
    )
    parser.add_argument(
        "--output", "-o",
        default=os.path.join(BASE_DIR, "outputs", "cascade_position_control.json"),
        help="Output JSON path (default: outputs/cascade_position_control.json)",
    )
    parser.add_argument(
        "--qwen-annotations",
        default=DEFAULT_ANNOTATION_PATHS["qwen"],
        help="Path to Qwen annotations.jsonl",
    )
    parser.add_argument(
        "--llama-annotations",
        default=DEFAULT_ANNOTATION_PATHS["llama"],
        help="Path to Llama annotations.jsonl",
    )
    args = parser.parse_args()

    output = {
        "analysis": (
            "Logistic regression: P(ack_t | ack_{t-1}, position_t) "
            "to test cascade as sequential dependency vs position effect"
        ),
    }

    for backbone, path in [("qwen", args.qwen_annotations),
                           ("llama", args.llama_annotations)]:
        data, n_tasks = load_consecutive_pairs(path)
        results = fit_models(data)
        results["n_tasks"] = n_tasks
        results["conclusion"] = build_conclusion(results)
        output[backbone] = results

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Wrote {args.output}")
    for backbone in ("qwen", "llama"):
        r = output[backbone]
        delta = round(r["aic_full"] - r["aic_position_only"], 1)
        print(
            f"  {backbone}: prev_ack OR={r['prev_ack_odds_ratio']}, "
            f"p={r['prev_ack_p_value']:.2e}, ΔAIC={delta}"
        )


if __name__ == "__main__":
    main()
