#!/usr/bin/env python3
import json
import os
import time
from datetime import datetime

LOGDIR = "/root/autodl-tmp/event-gated-adaptive-horizon/logdir"
RESULTS_FILE = "/root/autodl-tmp/event-gated-adaptive-horizon/checkpoint_results.jsonl"

EXPERIMENTS = {
    "008a": f"{LOGDIR}/exp_008a_fixed_dt2_no_subsample/metrics.jsonl",
    "008c": f"{LOGDIR}/exp_008c_fixed_dt2_no_subsample_h8/metrics.jsonl",
    "008d": f"{LOGDIR}/exp_008d_subsample_on_h8/metrics.jsonl",
}

CHECKPOINTS = {
    "35K":  {"step": 35000,  "baseline": 400, "threshold": 320, "level": "WARN"},
    "65K":  {"step": 65000,  "baseline": 616, "threshold": 493, "level": "GO"},
    "105K": {"step": 105000, "baseline": 916, "threshold": 733, "level": "GO"},
}

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def read_eval_returns(path):
    evals = {}
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if "eval_return" in rec and "step" in rec:
                    evals[int(rec["step"])] = float(rec["eval_return"])
    except FileNotFoundError:
        pass
    return evals


def log_result(result):
    with open(RESULTS_FILE, "a") as f:
        f.write(json.dumps(result) + "\n")


def main():
    judged = set()

    if os.path.exists(RESULTS_FILE):
        try:
            with open(RESULTS_FILE) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    rec = json.loads(line)
                    judged.add((rec["exp"], rec["checkpoint"]))
        except Exception:
            pass

    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] checkpoint_monitor started, polling every 60s")
    print(f"  Tracking: {', '.join(EXPERIMENTS.keys())}")
    print(f"  Checkpoints: {', '.join(CHECKPOINTS.keys())}")
    if judged:
        print(f"  Already judged: {judged}")
    print()

    while True:
        for exp_name, metrics_path in EXPERIMENTS.items():
            evals = read_eval_returns(metrics_path)
            if not evals:
                continue

            for cp_name, cp_cfg in CHECKPOINTS.items():
                if (exp_name, cp_name) in judged:
                    continue

                step = cp_cfg["step"]
                if step not in evals:
                    continue

                val = evals[step]
                baseline = cp_cfg["baseline"]
                threshold = cp_cfg["threshold"]

                if cp_cfg["level"] == "WARN":
                    verdict = "WARN" if val < threshold else "OK"
                    color = YELLOW if verdict == "WARN" else GREEN
                else:
                    verdict = "GO" if val >= threshold else "NO-GO"
                    color = GREEN if verdict == "GO" else RED

                result = {
                    "timestamp": datetime.now().isoformat(),
                    "exp": exp_name,
                    "checkpoint": cp_name,
                    "step": step,
                    "eval_return": round(val, 2),
                    "baseline": baseline,
                    "threshold": threshold,
                    "verdict": verdict,
                }

                log_result(result)
                judged.add((exp_name, cp_name))

                print(f"{color}[{result['timestamp'][:19]}] exp_{exp_name} @{cp_name}: "
                      f"eval_return={val:.1f} (baseline={baseline}, thresh={threshold}) "
                      f"→ {verdict}{RESET}")

        time.sleep(60)


if __name__ == "__main__":
    main()
