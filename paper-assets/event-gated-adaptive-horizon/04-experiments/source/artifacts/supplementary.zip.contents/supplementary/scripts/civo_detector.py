"""CIVO Online Detector v2 - Standalone Analysis Script.

Reads metrics.jsonl from a DreamerV3 logdir and applies the baseline-free
CIVO detection rules to identify value inflation onset.

Usage:
    python scripts/civo_detector.py --logdir ./logdir/exp_xxx/
"""

import argparse
import json
import os
import sys


def load_metrics(logdir):
    """Load eval_return and value_mean from metrics.jsonl."""
    path = os.path.join(logdir, "metrics.jsonl")
    if not os.path.exists(path):
        print(f"ERROR: {path} not found")
        sys.exit(1)

    eval_data = {}  # step -> eval_return
    value_data = {}  # step -> value_mean

    with open(path) as f:
        for line in f:
            d = json.loads(line.strip())
            step = d.get("step")
            if step is None:
                continue
            if "eval_return" in d:
                eval_data[step] = d["eval_return"]
            if "value_mean" in d:
                value_data[step] = d["value_mean"]

    return eval_data, value_data


def detect_civo(eval_data, value_data):
    """Apply CIVO v2 detection rules. Returns list of checkpoint results."""
    eval_steps = sorted(eval_data.keys())
    if len(eval_steps) < 3:
        print("WARNING: Need at least 3 eval checkpoints for detection.")
        return []

    results = []
    prev_ve_ratio = None
    prev_delta_ve = None
    eval_history = []

    for step in eval_steps:
        eval_ret = eval_data[step]
        vm = value_data.get(step)

        if vm is None:
            results.append({
                "step": step, "eval_return": eval_ret, "value_mean": None,
                "ve_ratio": None, "delta_ve": None, "conditions": [],
                "alert": False, "note": "no value_mean at this step"
            })
            continue

        eval_ret_clipped = max(eval_ret, 1e-6)
        ve_ratio = vm / eval_ret_clipped

        delta_ve = (ve_ratio - prev_ve_ratio) if prev_ve_ratio is not None else None

        # Eval history tracking
        eval_history.append(eval_ret)

        # Check conditions
        conditions = []
        c1 = ve_ratio >= 0.49
        c2 = delta_ve is not None and delta_ve > 0.1
        c3 = (delta_ve is not None and prev_delta_ve is not None and
              delta_ve > prev_delta_ve and prev_delta_ve > 0.1 and delta_ve > 0.1)

        # Condition 4: at least 2 of last 3 checkpoints declined vs predecessor
        c4 = False
        if len(eval_history) >= 4:
            recent = eval_history[-4:]  # need 4 to check 3 transitions
            declines = sum(1 for i in range(1, 4) if recent[i] < recent[i-1])
            c4 = declines >= 2
        elif len(eval_history) >= 3:
            recent = eval_history[-3:]
            declines = sum(1 for i in range(1, 3) if recent[i] < recent[i-1])
            c4 = declines >= 2

        if c1: conditions.append("C1:ve_ratio>=0.49")
        if c2: conditions.append("C2:delta_ve>0.1")
        if c3: conditions.append("C3:accelerating")
        if c4: conditions.append("C4:eval_decline")

        alert = c1 and c2 and c3 and c4

        results.append({
            "step": step,
            "eval_return": round(eval_ret, 4),
            "value_mean": round(vm, 6),
            "ve_ratio": round(ve_ratio, 4),
            "delta_ve": round(delta_ve, 4) if delta_ve is not None else None,
            "conditions": conditions,
            "alert": alert,
        })

        prev_delta_ve = delta_ve
        prev_ve_ratio = ve_ratio

    return results


def print_results(results, logdir):
    """Print formatted detection results."""
    print(f"\n{'='*80}")
    print(f"CIVO Detector v2 — {os.path.basename(logdir)}")
    print(f"{'='*80}")
    print(f"{'Step':>8} {'EvalRet':>10} {'ValMean':>12} {'VE_Ratio':>10} "
          f"{'DeltaVE':>10} {'Conditions':>30} {'Alert':>6}")
    print(f"{'-'*80}")

    alert_step = None
    for r in results:
        if r["ve_ratio"] is None:
            continue
        conds = ",".join(c.split(":")[1] for c in r["conditions"]) if r["conditions"] else "-"
        alert_str = "** YES **" if r["alert"] else ""
        print(f"{r['step']:>8} {r['eval_return']:>10.2f} {r['value_mean']:>12.4f} "
              f"{r['ve_ratio']:>10.4f} {r['delta_ve'] if r['delta_ve'] is not None else 'N/A':>10} "
              f"{conds:>30} {alert_str:>6}")
        if r["alert"] and alert_step is None:
            alert_step = r["step"]

    print(f"{'-'*80}")
    if alert_step:
        print(f">>> CIVO ALERT triggered at step {alert_step}")
    else:
        print(f">>> No CIVO alert triggered (all clear)")
    print()
    return alert_step


def main():
    parser = argparse.ArgumentParser(description="CIVO Detector v2")
    parser.add_argument("--logdir", required=True, help="Path to experiment logdir")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    args = parser.parse_args()

    eval_data, value_data = load_metrics(args.logdir)
    results = detect_civo(eval_data, value_data)

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print_results(results, args.logdir)


if __name__ == "__main__":
    main()
