"""CPU-only directed-asymmetric EC-HTE stress test.

This script implements the C006 DGP with asymmetric confusion, prevalence
imbalance, and directed flow from high-CATE true groups into low-CATE observed
labels. It supports 1-2 rep smoke tests and larger full runs, but this file
does not allocate or use GPU.

Inputs: CLI DGP name, k/N grid, rep count, seeds, output directory.
Outputs: results.json, summary.csv, global_worse_region_heatmap.csv,
directed_flow_diagnostics.json, and config.json.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np


Z975 = 1.959963984540054


def parse_csv_ints(text: str) -> list[int]:
    return [int(x) for x in text.split(",") if x]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run directed-asymmetric EC-HTE stress test.")
    p.add_argument("--dgp", default="directed_asym_prevalence_v1")
    p.add_argument("--k-values", default="3,6")
    p.add_argument("--n-values", default="2000,5000")
    p.add_argument("--reps", type=int, default=2)
    p.add_argument("--seeds", default="20260531")
    p.add_argument("--budget", type=int, default=500)
    p.add_argument("--out-dir", required=True)
    return p.parse_args()


def load_config(name: str) -> dict:
    path = Path(__file__).with_name("directed_dgp_config.json")
    with open(path, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    if cfg["name"] != name:
        raise ValueError(f"Unknown DGP {name}; available {cfg['name']}")
    return cfg


def validate_matrix(c: np.ndarray) -> None:
    if c.ndim != 2 or c.shape[0] != c.shape[1]:
        raise ValueError("confusion matrix must be square")
    if not np.allclose(c.sum(axis=1), 1.0):
        raise ValueError(f"confusion rows must sum to 1: {c.sum(axis=1)}")
    if np.allclose(c, c.T):
        raise ValueError("confusion matrix must be asymmetric for C006")


def dgp_for_k(cfg: dict, k: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, str]:
    spec = cfg[f"k{k}"]
    pi = np.array(spec["prevalence"], dtype=float)
    tau = np.array(spec["true_cate"], dtype=float)
    c = np.array(spec["confusion_rows_p_observed_given_true"], dtype=float)
    pi = pi / pi.sum()
    validate_matrix(c)
    return pi, tau, c, spec["directed_flow"]


def sample_labels(rng: np.random.Generator, g: np.ndarray, c: np.ndarray) -> np.ndarray:
    z = np.empty_like(g)
    for group in range(c.shape[0]):
        idx = np.flatnonzero(g == group)
        z[idx] = rng.choice(c.shape[1], size=idx.size, p=c[group])
    return z


def estimate_observed_tau(y: np.ndarray, t: np.ndarray, z: np.ndarray, k: int) -> tuple[np.ndarray, np.ndarray]:
    tau = np.zeros(k)
    var = np.zeros(k)
    for label in range(k):
        mask = z == label
        y1 = y[mask & (t == 1)]
        y0 = y[mask & (t == 0)]
        if y1.size < 2 or y0.size < 2:
            tau[label] = np.nan
            var[label] = np.inf
        else:
            tau[label] = y1.mean() - y0.mean()
            var[label] = y1.var(ddof=1) / y1.size + y0.var(ddof=1) / y0.size
    return tau, var


def estimate_confusion(g: np.ndarray, z: np.ndarray, budget: int, rng: np.random.Generator, k: int) -> tuple[np.ndarray, np.ndarray]:
    idx = rng.choice(g.size, size=min(budget, g.size), replace=False)
    alpha = 1.0
    pi_hat = (np.bincount(g[idx], minlength=k).astype(float) + alpha)
    pi_hat = pi_hat / pi_hat.sum()
    counts = np.full((k, k), alpha)
    for true_g, obs_z in zip(g[idx], z[idx]):
        counts[true_g, obs_z] += 1
    return pi_hat, counts / counts.sum(axis=1, keepdims=True)


def posterior_true_given_observed(pi: np.ndarray, c: np.ndarray) -> np.ndarray:
    joint = pi[:, None] * c
    return joint / np.maximum(joint.sum(axis=0, keepdims=True), 1e-12)


def global_confusion(pi: np.ndarray, c: np.ndarray) -> np.ndarray:
    k = c.shape[0]
    pooled_error = float(np.sum(pi[:, None] * c * (1.0 - np.eye(k))))
    g = np.full((k, k), pooled_error / (k - 1))
    np.fill_diagonal(g, 1.0 - pooled_error)
    return g


def corrected(obs_tau: np.ndarray, obs_var: np.ndarray, pi: np.ndarray, c: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    b = posterior_true_given_observed(pi, c)
    inv = np.linalg.pinv(b.T)
    est = inv @ obs_tau
    se = np.sqrt(np.maximum(np.diag(inv @ np.diag(obs_var) @ inv.T), 0.0))
    return est, se


def summarize(records: list[dict], true_tau: np.ndarray) -> list[dict]:
    out = []
    for method in sorted({r["method"] for r in records}):
        est = np.array([r["estimate"] for r in records if r["method"] == method])
        err = est - true_tau[None, :]
        widths = [r["ci_width"] for r in records if r["method"] == method]
        cover = [r["coverage"] for r in records if r["method"] == method]
        out.append({
            "method": method,
            "pehe_mean": float(np.mean(np.sqrt(np.mean(err ** 2, axis=1)))),
            "gate_bias_mean": float(np.mean(np.abs(err))),
            "gate_rmse_mean": float(np.sqrt(np.mean(err ** 2))),
            "coverage_mean": float(np.mean(cover)),
            "ci_width_mean": float(np.mean(widths)),
            "subgroup_cate_bias_mean": [float(x) for x in np.mean(np.abs(err), axis=0)]
        })
    return out


def run_config(cfg: dict, k: int, n: int, reps: int, seed: int, budget: int) -> dict:
    pi, tau, c, directed_flow = dgp_for_k(cfg, k)
    rng = np.random.default_rng(seed)
    rows = []
    for rep in range(reps):
        g = rng.choice(k, size=n, p=pi)
        t = rng.binomial(1, 0.5, size=n)
        y = tau[g] * t + rng.normal(0.0, 1.0, size=n)
        z = sample_labels(rng, g, c)
        obs_tau, obs_var = estimate_observed_tau(y, t, z, k)
        pi_hat, c_hat = estimate_confusion(g, z, budget, rng, k)
        methods = {
            "uncorrected": (obs_tau, np.sqrt(obs_var)),
            "global_correction": corrected(obs_tau, obs_var, pi_hat, global_confusion(pi_hat, c_hat)),
            "subgroup_ec_hte_lite": corrected(obs_tau, obs_var, pi_hat, c_hat),
        }
        for method, (est, se) in methods.items():
            rows.append({
                "rep": rep,
                "method": method,
                "estimate": [float(x) for x in est],
                "coverage": float(np.mean((est - Z975 * se <= tau) & (tau <= est + Z975 * se))),
                "ci_width": float(np.mean(2 * Z975 * se)),
            })
    summaries = summarize(rows, tau)
    by = {s["method"]: s for s in summaries}
    return {
        "k": k,
        "n": n,
        "reps": reps,
        "seed": seed,
        "prevalence": pi.tolist(),
        "true_cate": tau.tolist(),
        "confusion": c.tolist(),
        "directed_flow": directed_flow,
        "summaries": summaries,
        "global_worse_than_uncorrected": bool(
            by["global_correction"]["pehe_mean"] > by["uncorrected"]["pehe_mean"]
            or by["global_correction"]["gate_bias_mean"] > by["uncorrected"]["gate_bias_mean"]
        ),
    }


def write_outputs(out_dir: str, payload: dict) -> None:
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "results.json"), "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    with open(os.path.join(out_dir, "config.json"), "w", encoding="utf-8") as f:
        json.dump(payload["config"], f, indent=2, ensure_ascii=False)
    rows = []
    heat = []
    for r in payload["results"]:
        for s in r["summaries"]:
            row = {"k": r["k"], "n": r["n"], "seed": r["seed"], **s}
            row["subgroup_cate_bias_mean"] = json.dumps(row["subgroup_cate_bias_mean"])
            rows.append(row)
        heat.append({"k": r["k"], "n": r["n"], "seed": r["seed"], "global_worse_than_uncorrected": r["global_worse_than_uncorrected"]})
    for path, data in [("summary.csv", rows), ("global_worse_region_heatmap.csv", heat)]:
        with open(os.path.join(out_dir, path), "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
            writer.writeheader()
            writer.writerows(data)
    with open(os.path.join(out_dir, "directed_flow_diagnostics.json"), "w", encoding="utf-8") as f:
        json.dump([{"k": r["k"], "prevalence": r["prevalence"], "true_cate": r["true_cate"], "confusion": r["confusion"], "directed_flow": r["directed_flow"]} for r in payload["results"]], f, indent=2)


def main() -> int:
    args = parse_args()
    cfg = load_config(args.dgp)
    results = []
    for k in parse_csv_ints(args.k_values):
        for n in parse_csv_ints(args.n_values):
            for seed in parse_csv_ints(args.seeds):
                results.append(run_config(cfg, k, n, args.reps, seed, args.budget))
    payload = {
        "config": {"created_at": datetime.now(timezone.utc).isoformat(), "command": " ".join(sys.argv), "dgp": cfg, "device": "CPU-only"},
        "results": results,
    }
    write_outputs(args.out_dir, payload)
    print(json.dumps({"out_dir": args.out_dir, "configs": len(results), "global_worse_count": sum(r["global_worse_than_uncorrected"] for r in results)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
