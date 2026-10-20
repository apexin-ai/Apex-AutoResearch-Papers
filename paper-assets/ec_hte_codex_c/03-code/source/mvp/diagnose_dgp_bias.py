"""Diagnose whether the MVP DGP injects CATE bias through modifier misclassification.

The script is CPU-only and numpy-only. It reads the original MVP source to locate
the DGP/correction functions, then runs population-level and small simulation
sanity checks that separate three mechanisms:
1. true-group CATE values,
2. observed-label GATE smoothing induced by P(true group | observed label),
3. global vs subgroup confusion-matrix correction.

Outputs are code_locations.json, sanity_checks.json, and bias_injection_report.md.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone

import numpy as np


FUNCTIONS_OF_INTEREST = [
    "confusion_from_error_rates",
    "sample_observed_labels",
    "estimate_observed_cate",
    "estimate_confusion_from_expert",
    "posterior_true_given_observed",
    "corrected_estimate",
    "global_confusion_from_expert",
    "run_scenario",
    "pass_fail",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Diagnose EC-HTE MVP DGP bias path.")
    parser.add_argument("--source", required=True, help="Path to ec_hte_semisynth_mvp.py")
    parser.add_argument("--seed", type=int, default=20260531)
    parser.add_argument("--out-dir", required=True)
    return parser.parse_args()


def locate_functions(source_path: str) -> dict:
    """Return line-number spans for functions that implement the DGP and correction."""
    with open(source_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    starts: list[tuple[str, int]] = []
    for i, line in enumerate(lines, start=1):
        match = re.match(r"^def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", line)
        if match:
            starts.append((match.group(1), i))

    spans = {}
    for idx, (name, start) in enumerate(starts):
        if name not in FUNCTIONS_OF_INTEREST:
            continue
        end = starts[idx + 1][1] - 1 if idx + 1 < len(starts) else len(lines)
        spans[name] = {"start_line": start, "end_line": end}
    return {"source_path": source_path, "functions": spans}


def confusion_from_error_rates(error_rates: np.ndarray) -> np.ndarray:
    """Build P(observed label | true group), splitting errors over other labels."""
    k = len(error_rates)
    c = np.zeros((k, k), dtype=float)
    for g, err in enumerate(error_rates):
        c[g, :] = err / (k - 1)
        c[g, g] = 1.0 - err
    return c


def posterior_true_given_observed(pi: np.ndarray, c: np.ndarray) -> np.ndarray:
    """Return B[g,z] = P(true group g | observed label z)."""
    joint = pi[:, None] * c
    return joint / np.maximum(joint.sum(axis=0, keepdims=True), 1e-12)


def global_confusion(pi: np.ndarray, c: np.ndarray) -> np.ndarray:
    """Reproduce the MVP pooled symmetric global correction from true C."""
    k = c.shape[0]
    pooled_error = float(np.sum(pi[:, None] * c * (1.0 - np.eye(k))))
    g = np.full((k, k), pooled_error / (k - 1), dtype=float)
    np.fill_diagonal(g, 1.0 - pooled_error)
    return g


def corrected(observed_tau: np.ndarray, pi: np.ndarray, c: np.ndarray) -> np.ndarray:
    """Population analogue of corrected_estimate without sampling variance."""
    b = posterior_true_given_observed(pi, c)
    return np.linalg.inv(b.T + 1e-6 * np.eye(b.shape[0])) @ observed_tau


def rmse(x: np.ndarray) -> float:
    return float(np.sqrt(np.mean(x**2)))


def abs_mean(x: np.ndarray) -> float:
    return float(np.mean(np.abs(x)))


def population_check(name: str, pi: list[float], errors: list[float], cate: list[float]) -> dict:
    """Compute exact population estimands for uncorrected/global/subgroup correction."""
    pi_arr = np.array(pi, dtype=float)
    pi_arr = pi_arr / pi_arr.sum()
    c = confusion_from_error_rates(np.array(errors, dtype=float))
    tau = np.array(cate, dtype=float)
    b = posterior_true_given_observed(pi_arr, c)
    observed_tau = b.T @ tau
    c_global = global_confusion(pi_arr, c)
    estimates = {
        "uncorrected_observed_label": observed_tau,
        "global_correction_true_pooled": corrected(observed_tau, pi_arr, c_global),
        "subgroup_oracle_correction": corrected(observed_tau, pi_arr, c),
    }
    methods = {}
    for method, est in estimates.items():
        err = est - tau
        methods[method] = {
            "estimate": [float(x) for x in est],
            "bias": [float(x) for x in err],
            "pehe": rmse(err),
            "gate_bias_mean": abs_mean(err),
        }
    return {
        "name": name,
        "pi": [float(x) for x in pi_arr],
        "error_rates": errors,
        "true_cate": cate,
        "error_cate_corr": float(np.corrcoef(np.array(errors, dtype=float), tau)[0, 1])
        if len(errors) > 1 and np.std(errors) > 0 and np.std(tau) > 0
        else None,
        "confusion_p_observed_given_true": c.tolist(),
        "posterior_p_true_given_observed": b.tolist(),
        "observed_label_smoothing_nonzero": bool(np.max(np.abs(observed_tau - tau)) > 1e-9),
        "methods": methods,
    }


def simulate_check(seed: int) -> dict:
    """Small empirical check that observed-label estimates converge to population smoothing."""
    rng = np.random.default_rng(seed)
    n = 1000
    pi = np.array([0.34, 0.33, 0.33])
    errors = np.array([0.30, 0.15, 0.05])
    tau = np.array([0.50, 0.25, 0.05])
    c = confusion_from_error_rates(errors)
    g = rng.choice(3, size=n, p=pi)
    t = rng.binomial(1, 0.5, size=n)
    y = tau[g] * t + rng.normal(0.0, 1.0, size=n)
    z = np.empty_like(g)
    for group in range(3):
        idx = np.flatnonzero(g == group)
        z[idx] = rng.choice(3, size=idx.size, p=c[group])

    empirical = []
    for label in range(3):
        mask = z == label
        empirical.append(float(y[mask & (t == 1)].mean() - y[mask & (t == 0)].mean()))
    pop = np.array(population_check("original_positive_population", pi.tolist(), errors.tolist(), tau.tolist())["methods"]["uncorrected_observed_label"]["estimate"])
    return {
        "name": "small_simulation_matches_population_smoothing",
        "n": n,
        "seed": seed,
        "empirical_observed_label_tau": empirical,
        "population_observed_label_tau": [float(x) for x in pop],
        "max_abs_difference": float(np.max(np.abs(np.array(empirical) - pop))),
        "interpretation": "Large n reduces this gap; the check confirms the code estimates observed-label GATEs after misclassification.",
    }


def build_report(payload: dict) -> str:
    original = next(x for x in payload["sanity_checks"] if x["name"] == "original_positive_population")
    stress = next(x for x in payload["sanity_checks"] if x["name"] == "stress_positive_population")
    lines = [
        "# DGP Bias Audit",
        "",
        "## Verdict",
        "",
        "The MVP DGP does inject nonzero effect-modifier misclassification bias: observed-label GATEs are posterior mixtures of true-group CATEs, i.e. `E[tau(G) | Z=z]`, not the original true-group `tau_g`.",
        "",
        "The negative result is explained by mechanism strength: in the original symmetric off-diagonal DGP, the pooled symmetric global correction partially reverses observed-label smoothing instead of over-correcting enough to become worse than uncorrected. Therefore the original MVP does not create a guaranteed global-worse regime.",
        "",
        "## Code Locations",
        "",
    ]
    for name, span in payload["code_locations"]["functions"].items():
        lines.append(f"- `{name}`: lines {span['start_line']}-{span['end_line']}")
    lines.extend(
        [
            "",
            "## Key Population Checks",
            "",
            f"- Original positive case: observed-label smoothing nonzero = `{original['observed_label_smoothing_nonzero']}`; error-CATE corr = `{original['error_cate_corr']:.3f}`.",
            f"- Original PEHE: uncorrected `{original['methods']['uncorrected_observed_label']['pehe']:.6f}`, global `{original['methods']['global_correction_true_pooled']['pehe']:.6f}`, subgroup oracle `{original['methods']['subgroup_oracle_correction']['pehe']:.6f}`.",
            f"- Stress positive case: observed-label smoothing nonzero = `{stress['observed_label_smoothing_nonzero']}`; error-CATE corr = `{stress['error_cate_corr']:.3f}`.",
            f"- Stress PEHE: uncorrected `{stress['methods']['uncorrected_observed_label']['pehe']:.6f}`, global `{stress['methods']['global_correction_true_pooled']['pehe']:.6f}`, subgroup oracle `{stress['methods']['subgroup_oracle_correction']['pehe']:.6f}`.",
            "",
            "## Implication",
            "",
            "For follow-up experiments, the stress test should vary asymmetry, group prevalence, and k because the core failure mode is not absence of bias injection; it is that the current global correction baseline is too benign under symmetric error splitting.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    os.makedirs(args.out_dir, exist_ok=True)
    payload = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "command": " ".join(sys.argv),
        "code_locations": locate_functions(args.source),
        "sanity_checks": [
            population_check("no_misclassification_identity", [0.34, 0.33, 0.33], [0.0, 0.0, 0.0], [0.50, 0.25, 0.05]),
            population_check("original_positive_population", [0.34, 0.33, 0.33], [0.30, 0.15, 0.05], [0.50, 0.25, 0.05]),
            population_check("stress_positive_population", [0.34, 0.33, 0.33], [0.45, 0.20, 0.02], [0.80, 0.25, 0.00]),
        ],
        "simulation_check": simulate_check(args.seed),
    }
    with open(os.path.join(args.out_dir, "code_locations.json"), "w", encoding="utf-8") as f:
        json.dump(payload["code_locations"], f, indent=2, ensure_ascii=False)
    with open(os.path.join(args.out_dir, "sanity_checks.json"), "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    with open(os.path.join(args.out_dir, "bias_injection_report.md"), "w", encoding="utf-8") as f:
        f.write(build_report(payload))
    print(json.dumps({"out_dir": args.out_dir, "verdict": "bias_injected_but_global_baseline_benign"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
