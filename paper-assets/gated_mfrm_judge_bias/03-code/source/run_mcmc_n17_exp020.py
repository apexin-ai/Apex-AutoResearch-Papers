"""exp-020 N=17 MCMC fitting: G-MFRM on Arena Hard v0.1 with 7 judges.

Fits 4 methods (raw_average, mfrm_only, sequential, joint_gmfrm) on N=17
target models judged by J=6 judges (mistral-large-2 excluded) on I≤500 items.

Input:
  --judgment-dir  : prepared N=17 judgment directory (per-judge subdirs with
                    arena_hard_judgments.jsonl). Default: exp003/judgment_data_n17/
                    Run exp003/prepare_n17_data.py first to create symlinks.
  --exposure-csv  : exp-002 exposure_scores.csv
  --output-dir    : where to write MCMC results
  --dry-run       : quick run (1 chain, 10 warmup, 10 samples) for validation

Data format:
  Each judgment JSONL record: {item_id, model_a, model_b, judge, score, position, status}
  data_loader.load_data() returns sparse (model_idx, item_idx, judge_idx, y) arrays.

Key parameters:
  N = 17 target models (incl. qwen3-8b contamination probe)
  I ≤ 500 items (Arena Hard v0.1, after min-judge-coverage filter)
  J = 6 judges (after excluding mistral-large-2)
  MCMC: warmup=6000, samples=4000, chains=4, target_accept=0.95
  MCAR pattern: 4 judges complete + gemini ~62.5% + sonnet ~79.2%

qwen3-8b handling (方案B):
  - Included in MCMC fitting (all 17 models)
  - Excluded from τ/ρ correlation with Arena ELO (computed on 16 models)
"""

import os
os.environ.setdefault("JAX_PLATFORMS", "cuda,cpu")
os.environ.setdefault("XLA_PYTHON_CLIENT_PREALLOCATE", "false")
os.environ.setdefault("XLA_PYTHON_CLIENT_MEM_FRACTION", "0.25")

import argparse
import json
import sys
import time

import numpy as np

BASE_DIR = "/root/gated_mfrm_judge_bias"

EXCLUDE_JUDGES = ["mistral-large-2"]
EXCLUDE_MODELS_FROM_TAU = ["qwen3-8b"]


def filter_excluded_judges(data: dict, exclude: list[str]) -> dict:
    """Remove observations from excluded judges and re-index."""
    judge_names = data["judge_names"]
    excluded_set = set(exclude) & set(judge_names)
    if not excluded_set:
        print(f"  No judges to exclude (requested: {exclude})")
        return data

    excluded_indices = {judge_names.index(j) for j in excluded_set}
    mask = np.array([j not in excluded_indices for j in data["judge_idx"]])

    remaining = [j for j in judge_names if j not in excluded_set]
    old_to_new = {}
    for old_j, name in enumerate(judge_names):
        if name not in excluded_set:
            old_to_new[old_j] = len(old_to_new)

    n_removed = (~mask).sum()
    print(f"  Excluded judges {sorted(excluded_set)}: removed {n_removed} observations")
    print(f"  Remaining judges ({len(remaining)}): {remaining}")

    return {
        "model_idx": data["model_idx"][mask],
        "item_idx": data["item_idx"][mask],
        "judge_idx": np.array([old_to_new[j] for j in data["judge_idx"][mask]], dtype=np.int32),
        "y": data["y"][mask],
        "model_names": data["model_names"],
        "item_ids": data["item_ids"],
        "judge_names": remaining,
        "e_i": data["e_i"],
        "N": data["N"],
        "I": data["I"],
        "J": len(remaining),
        "n_obs": int(mask.sum()),
    }


def convergence_stoploss(idata, output_dir):
    """Check R-hat and ESS; write marker file."""
    import arviz as az

    rhat = az.rhat(idata)
    ess_bulk = az.ess(idata, method="bulk")

    rhat_max = max(
        float(rhat[v].values.max()) if rhat[v].values.ndim > 0 else float(rhat[v].values)
        for v in rhat.data_vars
    )
    ess_min = min(
        float(ess_bulk[v].values.min()) if ess_bulk[v].values.ndim > 0 else float(ess_bulk[v].values)
        for v in ess_bulk.data_vars
    )

    print(f"\n=== CONVERGENCE CHECK ===")
    print(f"R-hat max: {rhat_max:.4f} (threshold: 1.1)")
    print(f"ESS min: {ess_min:.0f} (threshold: 50)")

    if rhat_max > 1.1 or ess_min < 50:
        print("STOP-LOSS TRIGGERED: R-hat > 1.1 or ESS < 50")
        with open(os.path.join(output_dir, "CONVERGENCE_FAILED"), "w") as f:
            f.write(f"rhat_max={rhat_max}, ess_min={ess_min}\n")
        return False
    else:
        print("Convergence OK")
        with open(os.path.join(output_dir, "CONVERGENCE_OK"), "w") as f:
            f.write(f"rhat_max={rhat_max}, ess_min={ess_min}\n")
        return True


def main():
    parser = argparse.ArgumentParser(description="exp-020 N=17 G-MFRM MCMC fitting")
    parser.add_argument("--judgment-dir",
                        default=os.path.join(BASE_DIR, "exp003", "judgment_data_n17"),
                        help="N=17 judgment directory (per-judge subdirs)")
    parser.add_argument("--exposure-csv",
                        default=os.path.join(BASE_DIR, "exp002", "results", "exposure_scores.csv"))
    parser.add_argument("--output-dir",
                        default=os.path.join(BASE_DIR, "exp003", "output_n17_exp020"))
    parser.add_argument("--warmup", type=int, default=6000)
    parser.add_argument("--samples", type=int, default=4000)
    parser.add_argument("--chains", type=int, default=4)
    parser.add_argument("--target-accept", type=float, default=0.95)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--device", choices=["cpu", "gpu", "cuda"], default="gpu")
    parser.add_argument("--dry-run", action="store_true",
                        help="Quick validation: 1 chain, 10 warmup, 10 samples")
    parser.add_argument("--methods", nargs="+",
                        default=["raw_average", "mfrm_only", "sequential", "joint_gmfrm"])
    args = parser.parse_args()

    if args.dry_run:
        args.warmup = 10
        args.samples = 10
        args.chains = 1
        print("=== DRY-RUN MODE: 1 chain, 10 warmup, 10 samples ===\n")

    os.makedirs(args.output_dir, exist_ok=True)

    import jax
    import numpyro
    if args.device in ("gpu", "cuda"):
        try:
            jax.config.update("jax_default_device", jax.devices("cuda")[0])
            print(f"Using GPU: {jax.devices('cuda')[0]}")
        except RuntimeError:
            print("WARNING: No GPU available, falling back to CPU")
    numpyro.set_host_device_count(1)

    sys.path.insert(0, os.path.join(BASE_DIR, "exp003"))
    from data_loader import load_data
    from models import fit_raw_average, fit_mfrm_only, fit_sequential, fit_joint_gmfrm
    from evaluation import run_evaluation

    # --- Step 1: Load data ---
    print("=" * 60)
    print("STEP 1: Loading data")
    print("=" * 60)
    data = load_data(args.judgment_dir, args.exposure_csv)

    # --- Step 2: Filter judges ---
    print("\n" + "=" * 60)
    print("STEP 2: Filtering judges")
    print("=" * 60)
    data = filter_excluded_judges(data, EXCLUDE_JUDGES)
    print(f"\n  Final dimensions: N={data['N']}, I={data['I']}, J={data['J']}, n_obs={data['n_obs']}")

    # Per-judge coverage summary
    print("\n  Per-judge observation counts:")
    for j, name in enumerate(data["judge_names"]):
        n_j = (data["judge_idx"] == j).sum()
        expected = data["N"] * data["I"] * 2  # AB + BA positions → 1 binary obs per (model, item)
        max_possible = data["N"] * data["I"]
        coverage = n_j / max_possible * 100 if max_possible > 0 else 0
        print(f"    {name}: {n_j} obs ({coverage:.1f}% coverage)")

    # --- Step 3: Fit models ---
    print("\n" + "=" * 60)
    print("STEP 3: Fitting models")
    print("=" * 60)

    mcmc_kwargs = dict(
        warmup=args.warmup,
        samples=args.samples,
        chains=args.chains,
        target_accept=args.target_accept,
        seed=args.seed,
    )

    method_fns = {
        "raw_average": lambda: fit_raw_average(data),
        "mfrm_only": lambda: fit_mfrm_only(data, **mcmc_kwargs),
        "sequential": lambda: fit_sequential(data, **mcmc_kwargs),
        "joint_gmfrm": lambda: fit_joint_gmfrm(data, **mcmc_kwargs),
    }

    results = {}
    timings = {}
    for method_name in args.methods:
        if method_name not in method_fns:
            print(f"  Unknown method: {method_name}, skipping")
            continue
        print(f"\n--- {method_name} ---")
        t0 = time.time()
        results[method_name] = method_fns[method_name]()
        elapsed = time.time() - t0
        timings[method_name] = elapsed
        print(f"  Done in {elapsed:.1f}s")

    # --- Step 4: Save MCMC InferenceData + convergence check ---
    import arviz as az
    convergence_passed = True
    for name, res in results.items():
        mcmc_obj = res.get("mcmc")
        if mcmc_obj is not None:
            try:
                idata = az.from_numpyro(mcmc_obj)
                nc_path = os.path.join(args.output_dir, f"{name}_idata.nc")
                idata.to_netcdf(nc_path)
                print(f"  Saved InferenceData: {nc_path}")
                if name == "joint_gmfrm":
                    if not convergence_stoploss(idata, args.output_dir):
                        convergence_passed = False
            except Exception as e:
                print(f"  Warning: failed to save InferenceData for {name}: {e}")

    # --- Step 5: Evaluation ---
    print("\n" + "=" * 60)
    print("STEP 5: Evaluation")
    print("=" * 60)
    report = run_evaluation(results, data, args.output_dir)

    # --- Step 6: Save theta/c arrays ---
    for name, res in results.items():
        np.save(os.path.join(args.output_dir, f"{name}_theta.npy"), res["theta_hat"])
        if "c_hat" in res:
            np.save(os.path.join(args.output_dir, f"{name}_c.npy"), res["c_hat"])

    # --- Step 7: Save run metadata ---
    metadata = {
        "experiment": "exp-020-n17-mcmc",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "dry_run": args.dry_run,
        "mcmc_config": {
            "warmup": args.warmup,
            "samples": args.samples,
            "chains": args.chains,
            "target_accept": args.target_accept,
            "seed": args.seed,
        },
        "data_summary": {
            "judgment_dir": args.judgment_dir,
            "exposure_csv": args.exposure_csv,
            "N": data["N"],
            "I": data["I"],
            "J": data["J"],
            "n_obs": data["n_obs"],
            "model_names": data["model_names"],
            "judge_names": data["judge_names"],
        },
        "excluded_judges": EXCLUDE_JUDGES,
        "excluded_models_from_tau": EXCLUDE_MODELS_FROM_TAU,
        "timings_seconds": timings,
        "convergence_passed": convergence_passed,
    }
    with open(os.path.join(args.output_dir, "run_metadata.json"), "w") as f:
        json.dump(metadata, f, indent=2)

    # --- Summary ---
    print("\n" + "=" * 60)
    total_time = sum(timings.values())
    print(f"TOTAL TIME: {total_time:.0f}s ({total_time/60:.1f}min)")
    print(f"  Per method: " + ", ".join(f"{k}={v:.0f}s" for k, v in timings.items()))
    if args.dry_run:
        ratio = (6000 + 4000) * 4 / ((args.warmup + args.samples) * args.chains)
        est_full = total_time * ratio
        print(f"\n  Estimated full run time: {est_full:.0f}s ({est_full/60:.0f}min / {est_full/3600:.1f}h)")
        print(f"  (extrapolation ratio: {ratio:.0f}x)")
    if convergence_passed:
        print("\nDONE — Convergence OK")
    else:
        print("\nDONE — CONVERGENCE FAILED")
        sys.exit(1)
    print("=" * 60)


if __name__ == "__main__":
    main()
