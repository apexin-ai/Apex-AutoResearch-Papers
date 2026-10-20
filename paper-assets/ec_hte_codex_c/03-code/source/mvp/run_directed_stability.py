"""Single runner entry for directed DGP stability checks.

This wrapper avoids a shell-level `&&` chain. It calls the aggregate-reps and
seed-sweep routines as explicit Python subcommands and records those subcommands
in runner_subcommands.json.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run directed stability wrapper.")
    p.add_argument("--dgp", default="directed_asym_prevalence_v1")
    p.add_argument("--mode", choices=["both"], default="both")
    p.add_argument("--seeds", default="20260531,20260601,20260602")
    p.add_argument("--reps-per-seed", type=int, default=100)
    p.add_argument("--reps-aggregate", type=int, default=300)
    p.add_argument("--n", type=int, default=5000)
    p.add_argument("--budget", type=int, default=500)
    p.add_argument("--out-dir", required=True)
    return p.parse_args()


def run_checked(cmd: list[str], env: dict) -> None:
    subprocess.run(cmd, check=True, env=env)


def main() -> int:
    args = parse_args()
    base = Path(args.out_dir)
    base.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = ""
    here = Path(__file__).resolve().parent
    aggregate = [
        sys.executable, str(here / "ec_hte_directed_stress_test.py"),
        "--dgp", args.dgp, "--reps", str(args.reps_aggregate), "--seeds", "20260531",
        "--n-values", str(args.n), "--k-values", "3,6", "--budget", str(args.budget),
        "--out-dir", str(base / "reps300"),
    ]
    sweep = [
        sys.executable, str(here / "ec_hte_directed_seed_sweep.py"),
        "--dgp", args.dgp, "--seeds", args.seeds, "--reps-per-seed", str(args.reps_per_seed),
        "--n", str(args.n), "--budget", str(args.budget), "--out-dir", str(base / "seedx3"),
    ]
    with open(base / "runner_subcommands.json", "w", encoding="utf-8") as f:
        json.dump({"runner": "wrapper", "subcommands": [aggregate, sweep], "shell_chain_used": False}, f, indent=2)
    run_checked(aggregate, env)
    run_checked(sweep, env)
    with open(base / "stability_summary.csv", "w", encoding="utf-8") as f:
        f.write("component,path\n")
        f.write(f"aggregate,{base / 'reps300' / 'results.json'}\n")
        f.write(f"seed_sweep,{base / 'seedx3' / 'results.json'}\n")
    print(json.dumps({"out_dir": str(base), "runner": "wrapper", "shell_chain_used": False}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
