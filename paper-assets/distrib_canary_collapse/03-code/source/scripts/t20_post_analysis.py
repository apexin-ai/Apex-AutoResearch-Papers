#!/usr/bin/env python3
"""T=20 post-analysis: run D120 5-method lead-lag + verify against locked predictions."""

import argparse
import json
import os
import subprocess
import sys

PROJECT_ROOT = "/root/autodl-tmp/distrib_canary_collapse"
ANALYSIS_SCRIPT = os.path.join(PROJECT_ROOT, "run_5method_analysis_d102.py")
N_PAIRS = 8


def check_experiment_complete(exp_dir, expected_gens=21):
    """Check that all gen_0..gen_{expected_gens-1} have metrics.json."""
    missing = []
    for g in range(expected_gens):
        mpath = os.path.join(exp_dir, f"gen_{g}", "metrics.json")
        if not os.path.exists(mpath):
            missing.append(g)
    return missing


def run_5method(exp_dir, alpha, seed):
    """Run the D120 5-method analysis script and return the JSON result path."""
    cmd = [
        sys.executable, ANALYSIS_SCRIPT,
        "--data_dir", exp_dir,
        "--alpha", str(alpha),
        "--seed", str(seed),
    ]
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"STDERR: {result.stderr}", file=sys.stderr)
        sys.exit(1)

    json_path = os.path.join(exp_dir, "analysis", "5method_leadlag.json")
    if not os.path.exists(json_path):
        print(f"ERROR: expected output not found: {json_path}", file=sys.stderr)
        sys.exit(1)
    return json_path


def load_predictions(pred_path, alpha):
    """Load the locked prediction for a given alpha."""
    with open(pred_path) as f:
        data = json.load(f)

    alpha_key = f"t20_a{str(alpha).replace('.', '').ljust(3, '0')[:3]}"
    if alpha_key not in data["predictions"]:
        for k in data["predictions"]:
            a_str = k.replace("t20_a", "")
            a_val = int(a_str) / (10 ** len(a_str))
            if abs(a_val - alpha) < 1e-6:
                alpha_key = k
                break

    if alpha_key not in data["predictions"]:
        print(f"ERROR: no prediction found for alpha={alpha} (tried key '{alpha_key}')")
        print(f"Available keys: {list(data['predictions'].keys())}")
        sys.exit(1)

    return data["predictions"][alpha_key]


def verify(analysis_path, pred, alpha, seed):
    """Compare observed PermG count against locked prediction."""
    with open(analysis_path) as f:
        results = json.load(f)

    observed_permg = results["summary"]["perm_granger_fdr_forward_sig"]
    observed_rate = observed_permg / N_PAIRS

    predicted_count = pred["predicted_permg_count"]
    predicted_rate = pred["predicted_rate"]
    rate_95ci = pred["rate_95ci"]

    within_ci = rate_95ci[0] <= observed_rate <= rate_95ci[1]

    robust_pairs = results["summary"]["robust_pairs"]

    verification = {
        "alpha": alpha,
        "seed": seed,
        "T": 20,
        "n_generations": results["meta"]["n_gens"],
        "observed_permg_count": observed_permg,
        "observed_rate": round(observed_rate, 4),
        "predicted_permg_count": predicted_count,
        "predicted_rate": round(predicted_rate, 4),
        "predicted_rate_95ci": rate_95ci,
        "within_ci": within_ci,
        "robust_pairs_K3": robust_pairs,
        "per_method_summary": {
            "perm_granger_fdr_fwd": results["summary"]["perm_granger_fdr_forward_sig"],
            "perm_granger_fdr_rev": results["summary"]["perm_granger_fdr_reverse_sig"],
            "diff_xcorr_fdr_fwd": results["summary"]["diff_xcorr_fdr_forward_sig"],
            "threshold_fwd": results["summary"]["threshold_forward_sig"],
            "ty_fwd": results["summary"]["ty_forward_sig"],
        },
        "consensus": results["consensus"],
        "analysis_path": analysis_path,
    }

    return verification


def print_result(v):
    """Print a readable summary."""
    match_symbol = "PASS" if v["within_ci"] else "FAIL"
    print(f"\n{'=' * 70}")
    print(f"T=20 PREDICTION VERIFICATION | alpha={v['alpha']} seed={v['seed']}")
    print(f"{'=' * 70}")
    print(f"  Observed PermG (FDR fwd):  {v['observed_permg_count']}/{N_PAIRS}  (rate={v['observed_rate']:.3f})")
    print(f"  Predicted PermG:           {v['predicted_permg_count']}/{N_PAIRS}  (rate={v['predicted_rate']:.3f})")
    print(f"  Predicted 95% CI:          [{v['predicted_rate_95ci'][0]:.4f}, {v['predicted_rate_95ci'][1]:.4f}]")
    print(f"  Within CI:                 {v['within_ci']}  [{match_symbol}]")
    print(f"  Robust pairs (K>=3):       {v['robust_pairs_K3']}/{N_PAIRS}")
    print(f"\n  Per-method forward significance:")
    s = v["per_method_summary"]
    print(f"    Perm Granger (FDR): {s['perm_granger_fdr_fwd']}/{N_PAIRS}")
    print(f"    Diff XCorr (FDR):   {s['diff_xcorr_fdr_fwd']}/{N_PAIRS}")
    print(f"    Threshold Onset:    {s['threshold_fwd']}/{N_PAIRS}")
    print(f"    TY Granger:         {s['ty_fwd']}/{N_PAIRS}")
    print(f"  PermG reverse:        {s['perm_granger_fdr_rev']}/{N_PAIRS}")
    print(f"{'=' * 70}\n")


def main():
    parser = argparse.ArgumentParser(description="T=20 post-analysis: 5-method + prediction verify")
    parser.add_argument("--exp_dir", required=True, help="T=20 experiment directory (e.g. results/t20/a050_s42_fp32)")
    parser.add_argument("--alpha", type=float, required=True, help="Alpha value")
    parser.add_argument("--seed", type=int, required=True, help="Random seed")
    parser.add_argument("--predictions", required=True, help="Path to locked predictions JSON")
    parser.add_argument("--output_dir", default=None, help="Output dir for verification JSON (default: artifacts/)")
    parser.add_argument("--expected_gens", type=int, default=21, help="Expected number of generations (default: 21 for T=20)")
    parser.add_argument("--skip_completeness_check", action="store_true", help="Skip checking all gens exist")
    args = parser.parse_args()

    if not os.path.isdir(args.exp_dir):
        print(f"ERROR: experiment directory not found: {args.exp_dir}", file=sys.stderr)
        sys.exit(1)

    if not args.skip_completeness_check:
        missing = check_experiment_complete(args.exp_dir, args.expected_gens)
        if missing:
            print(f"ERROR: experiment incomplete — missing gen metrics: {missing}", file=sys.stderr)
            sys.exit(1)
        print(f"Completeness check passed: {args.expected_gens} generations found")

    analysis_path = run_5method(args.exp_dir, args.alpha, args.seed)
    pred = load_predictions(args.predictions, args.alpha)
    verification = verify(analysis_path, pred, args.alpha, args.seed)
    print_result(verification)

    out_dir = args.output_dir or os.path.join(PROJECT_ROOT, "artifacts")
    os.makedirs(out_dir, exist_ok=True)

    alpha_str = str(args.alpha).replace(".", "")
    out_path = os.path.join(out_dir, f"t20_verify_a{alpha_str}_s{args.seed}.json")
    with open(out_path, "w") as f:
        json.dump(verification, f, indent=2)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
