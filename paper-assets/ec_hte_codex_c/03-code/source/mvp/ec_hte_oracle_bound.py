"""CPU-only oracle upper-bound diagnostic for directed EC-HTE DGP.

Oracle/full-truth confusion is reported only as a diagnostic upper bound and is
kept separate from B=500 estimated-confusion results.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from datetime import datetime, timezone

from ec_hte_directed_stress_test import corrected, dgp_for_k, estimate_confusion, estimate_observed_tau, global_confusion, load_config, sample_labels, summarize

import numpy as np


Z975 = 1.959963984540054


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run oracle upper-bound diagnostic.")
    p.add_argument("--dgp", default="directed_asym_prevalence_v1")
    p.add_argument("--compare", default="estimated_b500,oracle_global,oracle_subgroup")
    p.add_argument("--seed", type=int, default=20260531)
    p.add_argument("--reps", type=int, default=2)
    p.add_argument("--n", type=int, default=5000)
    p.add_argument("--budget", type=int, default=500)
    p.add_argument("--out-dir", required=True)
    return p.parse_args()


def run(args: argparse.Namespace) -> dict:
    cfg = load_config(args.dgp)
    pi, tau, c, directed_flow = dgp_for_k(cfg, 3)
    rng = np.random.default_rng(args.seed)
    rows = []
    for rep in range(args.reps):
        g = rng.choice(3, size=args.n, p=pi)
        t = rng.binomial(1, 0.5, size=args.n)
        y = tau[g] * t + rng.normal(0.0, 1.0, size=args.n)
        z = sample_labels(rng, g, c)
        obs_tau, obs_var = estimate_observed_tau(y, t, z, 3)
        pi_hat, c_hat = estimate_confusion(g, z, args.budget, rng, 3)
        methods = {
            "estimated_b500_global": corrected(obs_tau, obs_var, pi_hat, global_confusion(pi_hat, c_hat)),
            "estimated_b500_subgroup": corrected(obs_tau, obs_var, pi_hat, c_hat),
            "oracle_global": corrected(obs_tau, obs_var, pi, global_confusion(pi, c)),
            "oracle_subgroup": corrected(obs_tau, obs_var, pi, c),
        }
        for method, (est, se) in methods.items():
            rows.append({"rep": rep, "method": method, "estimate": [float(x) for x in est], "coverage": float(np.mean((est - Z975 * se <= tau) & (tau <= est + Z975 * se))), "ci_width": float(np.mean(2 * Z975 * se))})
    summaries = summarize(rows, tau)
    by = {s["method"]: s for s in summaries}
    gap = {
        "oracle_subgroup_minus_estimated_b500_subgroup_pehe": by["estimated_b500_subgroup"]["pehe_mean"] - by["oracle_subgroup"]["pehe_mean"],
        "oracle_global_minus_estimated_b500_global_pehe": by["estimated_b500_global"]["pehe_mean"] - by["oracle_global"]["pehe_mean"],
    }
    return {"dgp": cfg, "directed_flow": directed_flow, "summaries": summaries, "oracle_vs_estimated_gap": gap}


def main() -> int:
    args = parse_args()
    os.makedirs(args.out_dir, exist_ok=True)
    result = run(args)
    payload = {"config": {"created_at": datetime.now(timezone.utc).isoformat(), "command": " ".join(sys.argv), "device": "CPU-only"}, "result": result}
    with open(os.path.join(args.out_dir, "results.json"), "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    with open(os.path.join(args.out_dir, "config.json"), "w", encoding="utf-8") as f:
        json.dump(payload["config"], f, indent=2)
    with open(os.path.join(args.out_dir, "oracle_vs_estimated_gap.json"), "w", encoding="utf-8") as f:
        json.dump(result["oracle_vs_estimated_gap"], f, indent=2)
    with open(os.path.join(args.out_dir, "summary.csv"), "w", newline="", encoding="utf-8") as f:
        rows = result["summaries"]
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    with open(os.path.join(args.out_dir, "oracle_separate_report.md"), "w", encoding="utf-8") as f:
        f.write("# Oracle Upper-Bound Diagnostic\n\nOracle rows are diagnostic upper bounds only and are separate from B=500 estimated-confusion rows.\n")
    print(json.dumps({"out_dir": args.out_dir, "oracle_policy": "separate_diagnostic_upper_bound"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
