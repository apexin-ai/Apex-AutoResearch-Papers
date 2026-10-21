#!/usr/bin/env python3
"""S2-removal ablation: compare Full RRF (S1+S2+S4) vs No-S2 (S1+S4) IRT calibration."""

import json
import logging
import os
import re
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
from run_irt_calibration import STAN_MODELS

log = logging.getLogger(__name__)

SIGNAL_DIR = "/root/autodl-tmp/exp002/signals"
EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
STAN_FILE = STAN_MODELS["2pl_gamma"]
OUTPUT_DIR = Path("/root/contamcal-irt-calibration/artifacts/s2_removal_ablation")

BENCHMARK = "mmlu"
MAX_ITEMS = 300
SEED = 42
RRF_K = 60

MODELS_16 = [
    ("Qwen2.5-1.5B_d000_s123_aligned", "Qwen2.5-1.5B_d000_s123"),
    ("Qwen2.5-1.5B_d000_s42_aligned", "Qwen2.5-1.5B_d000_s42"),
    ("Qwen2.5-1.5B_d005_s123_aligned", "Qwen2.5-1.5B_d005_s123"),
    ("Qwen2.5-1.5B_d005_s42_aligned", "Qwen2.5-1.5B_d005_s42"),
    ("Qwen2.5-1.5B_d025_s123_aligned", "Qwen2.5-1.5B_d025_s123"),
    ("Qwen2.5-1.5B_d025_s42_aligned", "Qwen2.5-1.5B_d025_s42"),
    ("Qwen2.5-1.5B_d100_s123_aligned", "Qwen2.5-1.5B_d100_s123"),
    ("Qwen2.5-1.5B_d100_s42_aligned", "Qwen2.5-1.5B_d100_s42"),
    ("Qwen2.5-3B_d000_s123_aligned", "Qwen2.5-3B_d000_s123"),
    ("Qwen2.5-3B_d000_s42_a32_aligned", "Qwen2.5-3B_d000_s42_a32"),
    ("Qwen2.5-3B_d005_s123_aligned", "Qwen2.5-3B_d005_s123"),
    ("Qwen2.5-3B_d005_s42_a32_aligned", "Qwen2.5-3B_d005_s42_a32"),
    ("Qwen2.5-3B_d025_s123_aligned", "Qwen2.5-3B_d025_s123"),
    ("Qwen2.5-3B_d025_v3_s42_aligned", "Qwen2.5-3B_d025_v3_s42"),
    ("Qwen2.5-3B_d100_a32_s123_aligned", "Qwen2.5-3B_d100_a32_s123"),
    ("Qwen2.5-3B_d100_a32_s42_aligned", "Qwen2.5-3B_d100_a32_s42"),
]


def compute_ranks(scores):
    order = np.argsort(-scores)
    ranks = np.empty_like(order)
    ranks[order] = np.arange(1, len(scores) + 1)
    return ranks


def compute_rrf(items, signals, k=RRF_K, normalize=True):
    n = len(items)
    rrf_scores = np.zeros(n)
    for sig in signals:
        vals = np.array([item.get(sig, 0.0) or 0.0 for item in items], dtype=float)
        ranks = compute_ranks(vals)
        rrf_scores += 1.0 / (k + ranks)
    if normalize and n > 0:
        mn, mx = rrf_scores.min(), rrf_scores.max()
        if mx > mn:
            rrf_scores = (rrf_scores - mn) / (mx - mn)
    return rrf_scores


def extract_item_index(item):
    if "index" in item:
        return item["index"]
    item_id = item.get("item_id", "")
    m = re.search(r'(\d+)$', item_id)
    return int(m.group(1)) if m else 0


def load_signals(signal_dir, benchmark):
    path = Path(signal_dir) / f"signals_merged_{benchmark}.json"
    if not path.exists():
        raise FileNotFoundError(f"Signal file not found: {path}")
    with open(path) as f:
        items = json.load(f)
    items.sort(key=extract_item_index)
    return items


def load_eval_per_item(eval_dir_name, benchmark):
    eval_path = Path(EVAL_DIR) / eval_dir_name / "eval_results.json"
    with open(eval_path) as f:
        data = json.load(f)
    if "benchmarks" in data:
        data = data["benchmarks"]
    bench_key = benchmark
    if bench_key not in data:
        for k in data:
            if benchmark in k.lower():
                bench_key = k
                break
    result = data[bench_key]
    if isinstance(result, dict) and "per_item" in result:
        return result["per_item"]
    return result


def run_irt_fit(responses, exposure, label):
    import cmdstanpy

    N_models, N_items = responses.shape
    stan_data = {
        "N_models": N_models,
        "N_items": N_items,
        "y": responses.tolist(),
        "exposure": exposure.tolist(),
    }

    log.info("[%s] Compiling Stan model...", label)
    model = cmdstanpy.CmdStanModel(stan_file=STAN_FILE)

    log.info("[%s] Fitting: N=%d, I=%d, 4 chains...", label, N_models, N_items)
    t0 = time.time()
    fit = model.sample(
        data=stan_data,
        chains=4,
        iter_warmup=1000,
        iter_sampling=1000,
        adapt_delta=0.95,
        max_treedepth=12,
        seed=SEED,
        show_progress=True,
    )
    fit_time = time.time() - t0
    log.info("[%s] Fit done in %.1fs", label, fit_time)

    summary = fit.summary()
    rhats = summary["R_hat"].dropna()
    ess = summary["N_Eff"].dropna()
    diagnostics = {
        "max_rhat": float(rhats.max()),
        "min_ess": float(ess.min()),
        "fit_time_sec": fit_time,
    }

    diag_str = fit.diagnose()
    n_div = diag_str.lower().count("transition") if "divergent" in diag_str.lower() else 0
    diagnostics["divergent_count"] = n_div

    gamma_samples = fit.stan_variable("gamma")
    gamma_stats = {
        "mean": float(np.mean(gamma_samples)),
        "sd": float(np.std(gamma_samples)),
        "q025": float(np.percentile(gamma_samples, 2.5)),
        "q975": float(np.percentile(gamma_samples, 97.5)),
    }

    cal_samples = fit.stan_variable("calibrated_score")
    cal_mean = np.mean(cal_samples, axis=0).tolist()

    # PPP
    a_samples = fit.stan_variable("a")
    b_samples = fit.stan_variable("b")
    theta_samples = fit.stan_variable("theta")
    n_draws = gamma_samples.shape[0]
    obs_stat = np.mean(responses)
    rng = np.random.RandomState(42)
    n_checks = min(n_draws, 500)
    draw_idx = rng.choice(n_draws, n_checks, replace=False)
    ppp_count = 0
    for di in draw_idx:
        a_d, b_d = a_samples[di], b_samples[di]
        theta_d, gamma_d = theta_samples[di], gamma_samples[di]
        eta = np.outer(theta_d, a_d) - np.outer(np.ones(N_models), a_d * b_d) + gamma_d * exposure
        prob = 1.0 / (1.0 + np.exp(-eta))
        y_rep = (rng.random(prob.shape) < prob).astype(int)
        if np.mean(y_rep) >= obs_stat:
            ppp_count += 1
    ppp = ppp_count / n_checks

    log.info("[%s] gamma=%.4f [%.4f,%.4f], R̂=%.4f, ESS=%.0f, PPP=%.3f",
             label, gamma_stats["mean"], gamma_stats["q025"], gamma_stats["q975"],
             diagnostics["max_rhat"], diagnostics["min_ess"], ppp)

    return {
        "gamma": gamma_stats,
        "diagnostics": diagnostics,
        "ppp": ppp,
        "calibrated_mean": cal_mean,
    }


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Verify signals exist (try alternative names if needed)
    resolved = []
    for eval_dir, sig_dir in MODELS_16:
        sig_path = Path(SIGNAL_DIR) / sig_dir
        if not sig_path.exists():
            # Try swapping a32/s42 order
            alt = sig_dir.replace("_s42_a32", "_a32_s42").replace("_s123_a32", "_a32_s123")
            sig_path2 = Path(SIGNAL_DIR) / alt
            if sig_path2.exists():
                log.info("Resolved %s -> %s", sig_dir, alt)
                resolved.append((eval_dir, alt))
                continue
            log.error("Missing signal dir: %s (tried %s too)", sig_dir, alt)
            sys.exit(1)
        resolved.append((eval_dir, sig_dir))

    # Get total items & compute subsample indices
    per_item_0 = load_eval_per_item(resolved[0][0], BENCHMARK)
    total_items = len(per_item_0)
    log.info("Total %s items: %d", BENCHMARK, total_items)

    subsample_idx = None
    if total_items > MAX_ITEMS:
        np.random.seed(SEED)
        subsample_idx = sorted(np.random.choice(total_items, MAX_ITEMS, replace=False).tolist())

    n_items = MAX_ITEMS if subsample_idx else total_items
    N = len(resolved)

    # Build response matrix
    responses = np.zeros((N, n_items), dtype=int)
    dosages = np.zeros(N, dtype=float)
    for i, (eval_dir, _) in enumerate(resolved):
        per_item = load_eval_per_item(eval_dir, BENCHMARK)
        items_sel = [per_item[j] for j in subsample_idx] if subsample_idx else per_item[:n_items]
        for j, item in enumerate(items_sel):
            if j >= n_items:
                break
            if isinstance(item, dict):
                responses[i, j] = 1 if item.get("correct", False) else 0
            else:
                responses[i, j] = int(item)
        m = re.search(r'_d(\d+)', eval_dir)
        if m:
            dosages[i] = int(m.group(1))

    raw_accuracy = np.mean(responses, axis=1)
    log.info("Responses: %s, raw acc range: [%.3f, %.3f]", responses.shape,
             raw_accuracy.min(), raw_accuracy.max())

    # Build exposure matrices
    full_sigs = ["s1_embedding", "s2_minkpp", "s4_selfcritique"]
    nos2_sigs = ["s1_embedding", "s4_selfcritique"]
    exposure_full = np.zeros((N, n_items))
    exposure_nos2 = np.zeros((N, n_items))

    for i, (_, sig_dir) in enumerate(resolved):
        items = load_signals(os.path.join(SIGNAL_DIR, sig_dir), BENCHMARK)
        rrf_full = compute_rrf(items, full_sigs)
        rrf_nos2 = compute_rrf(items, nos2_sigs)
        if subsample_idx:
            exposure_full[i] = rrf_full[subsample_idx]
            exposure_nos2[i] = rrf_nos2[subsample_idx]
        else:
            exposure_full[i] = rrf_full[:n_items]
            exposure_nos2[i] = rrf_nos2[:n_items]

    log.info("Exposure correlation (full vs no-s2) per model:")
    for i in range(N):
        r = np.corrcoef(exposure_full[i], exposure_nos2[i])[0, 1]
        log.info("  %s: r=%.4f", resolved[i][0], r)

    # Run IRT fits
    log.info("=" * 60)
    log.info("FIT 1: Full RRF (S1+S2+S4)")
    log.info("=" * 60)
    full_res = run_irt_fit(responses, exposure_full, "Full_RRF")

    log.info("=" * 60)
    log.info("FIT 2: No-S2 RRF (S1+S4)")
    log.info("=" * 60)
    nos2_res = run_irt_fit(responses, exposure_nos2, "No_S2")

    # Compute metrics
    from scipy.stats import kendalltau

    full_cal = np.array(full_res["calibrated_mean"])
    nos2_cal = np.array(nos2_res["calibrated_mean"])

    full_mae = float(np.mean(np.abs(raw_accuracy - full_cal)))
    nos2_mae = float(np.mean(np.abs(raw_accuracy - nos2_cal)))

    tau_raw, _ = kendalltau(dosages, raw_accuracy)
    tau_full, _ = kendalltau(dosages, full_cal)
    tau_nos2, _ = kendalltau(dosages, nos2_cal)

    # Save full results
    summary = {
        "benchmark": BENCHMARK,
        "n_models": N,
        "n_items": n_items,
        "full_rrf": {
            "signals": full_sigs,
            "mae": full_mae,
            "tau": float(tau_full),
            "gamma": full_res["gamma"],
            "ppp": full_res["ppp"],
            "diagnostics": full_res["diagnostics"],
            "calibrated_mean": full_res["calibrated_mean"],
        },
        "no_s2": {
            "signals": nos2_sigs,
            "mae": nos2_mae,
            "tau": float(tau_nos2),
            "gamma": nos2_res["gamma"],
            "ppp": nos2_res["ppp"],
            "diagnostics": nos2_res["diagnostics"],
            "calibrated_mean": nos2_res["calibrated_mean"],
        },
        "raw_accuracy": {
            "values": raw_accuracy.tolist(),
            "tau": float(tau_raw),
        },
        "dosages": dosages.tolist(),
        "models": [e for e, _ in resolved],
    }

    with open(OUTPUT_DIR / "s2_ablation_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    # Print table
    print("\n" + "=" * 90)
    print("S2 REMOVAL ABLATION — MMLU (N=16, I=300, 2PL+γ)")
    print("=" * 90)
    fmt = "{:<25s} {:>8s} {:>8s} {:>8s} {:>24s} {:>8s}"
    print(fmt.format("Pipeline", "MAE", "τ", "γ_mean", "γ CI95", "PPP"))
    print("-" * 90)
    print(fmt.format("Raw Accuracy", "—", f"{tau_raw:.3f}", "—", "—", "—"))
    g = full_res["gamma"]
    print(f"{'Full RRF (S1+S2+S4)':<25s} {full_mae:>8.4f} {tau_full:>8.3f} "
          f"{g['mean']:>8.4f} [{g['q025']:>7.3f}, {g['q975']:>6.3f}] "
          f"{full_res['ppp']:>8.3f}")
    g = nos2_res["gamma"]
    print(f"{'No-S2 RRF (S1+S4)':<25s} {nos2_mae:>8.4f} {tau_nos2:>8.3f} "
          f"{g['mean']:>8.4f} [{g['q025']:>7.3f}, {g['q975']:>6.3f}] "
          f"{nos2_res['ppp']:>8.3f}")
    print("=" * 90)
    print(f"\nΔMAE (No-S2 − Full): {nos2_mae - full_mae:+.4f}")
    print(f"Δτ   (No-S2 − Full): {tau_nos2 - tau_full:+.3f}")
    print(f"\nDiagnostics:")
    print(f"  Full: R̂={full_res['diagnostics']['max_rhat']:.4f}, "
          f"ESS={full_res['diagnostics']['min_ess']:.0f}")
    print(f"  No-S2: R̂={nos2_res['diagnostics']['max_rhat']:.4f}, "
          f"ESS={nos2_res['diagnostics']['min_ess']:.0f}")
    print(f"\nResults saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
