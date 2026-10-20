"""CPU-only seed sweep for the directed EC-HTE DGP."""

from __future__ import annotations

import argparse
import json
import os
import sys

from ec_hte_directed_stress_test import load_config, run_config, write_outputs


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run directed DGP seed sweep.")
    p.add_argument("--dgp", default="directed_asym_prevalence_v1")
    p.add_argument("--seeds", required=True)
    p.add_argument("--reps-per-seed", type=int, default=1)
    p.add_argument("--n", type=int, default=5000)
    p.add_argument("--budget", type=int, default=500)
    p.add_argument("--out-dir", required=True)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    cfg = load_config(args.dgp)
    seeds = [int(x) for x in args.seeds.split(",") if x]
    results = [run_config(cfg, 3, args.n, args.reps_per_seed, seed, args.budget) for seed in seeds]
    payload = {"config": {"command": " ".join(sys.argv), "dgp": cfg, "device": "CPU-only"}, "results": results}
    write_outputs(args.out_dir, payload)
    print(json.dumps({"out_dir": args.out_dir, "seeds": seeds}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
