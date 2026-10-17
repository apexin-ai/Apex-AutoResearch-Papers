#!/usr/bin/env python3
"""Step 2 v3: Multi-variate regression — K_eff as ASR predictor controlling for η_max."""

import os
os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import glob
import numpy as np
import statsmodels.api as sm
from itertools import combinations
from pathlib import Path
from datetime import datetime, timezone

from src.config import MODEL_REGISTRY
from src.attacks import ALL_ATTACKS, apply_attack_to_pairs, measure_asr
from src.judge_service import JudgeService
from src.eval_pipeline import load_eval_dataset, generate_response_pairs
from src.panels import Panel, measure_panel_asr
from src.utils import setup_logging, set_seed

logger = setup_logging("step2v3")

MODEL_IDS = ["qwen2.5-72b", "llama3.1-70b", "mistral-large", "qwen2.5-32b", "qwen2.5-14b", "llama3.1-8b"]
ATTACK_NAMES = ["prompt_injection", "sycophancy", "score_manipulation"]
DATASETS = ["mmlu", "arc_challenge"]
LARGE_MODEL_IDS = ["qwen2.5-72b", "llama3.1-70b", "qwen2.5-32b", "mistral-large"]
EPS = 0.001
RESULTS_DIR = Path("/root/cert_manip_resist_eval/artifacts/results")
CKPT_PATH = RESULTS_DIR / "_step2v3_checkpoint.json"


def get_attacks_by_name():
    out = {}
    for atk in ALL_ATTACKS:
        if atk.name in ATTACK_NAMES and atk.name not in out:
            out[atk.name] = atk
    assert len(out) == 3, f"Expected 3 attacks, got {list(out.keys())}"
    return out


def load_step1():
    files = sorted(glob.glob(str(RESULTS_DIR / "results_step1_full_*.json")))
    assert files, "No Step 1 results found"
    with open(files[-1]) as f:
        return json.load(f)


def mi_based_keff(pairwise_list, judge_ids):
    K = len(judge_ids)
    if K <= 1:
        return 1.0
    mi_lu = {}
    for e in pairwise_list:
        mi_lu[(e["judge_i"], e["judge_j"])] = e["mi"]
        mi_lu[(e["judge_j"], e["judge_i"])] = e["mi"]
    total = 0.0
    for i, ji in enumerate(judge_ids):
        ki = 1.0
        for j, jj in enumerate(judge_ids):
            if i != j:
                ki += np.exp(-2.0 * mi_lu.get((ji, jj), 0.0))
        total += ki
    return float(total / K)


def save_ckpt(data):
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    with open(CKPT_PATH, "w") as f:
        json.dump(data, f, default=_json_default)
    logger.info(f"Checkpoint saved ({CKPT_PATH.name})")


def load_ckpt():
    if CKPT_PATH.exists():
        with open(CKPT_PATH) as f:
            return json.load(f)
    return None


def _json_default(obj):
    if isinstance(obj, (np.floating,)):
        v = float(obj)
        return None if np.isnan(v) else v
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    raise TypeError(f"Not serializable: {type(obj)}")


# ── Phase 1: Inference ──────────────────────────────────────────────

def phase1_inference():
    ckpt = load_ckpt()
    if ckpt and ckpt.get("phase1_complete"):
        logger.info("Phase 1 complete (checkpoint). Skipping inference.")
        return ckpt["clean_scores"], ckpt["attacked_scores"], ckpt["pairs"]

    set_seed(42)
    attacks = get_attacks_by_name()

    if ckpt and "pairs" in ckpt:
        logger.info("Resuming from partial checkpoint")
        pairs = ckpt["pairs"]
        clean_scores = ckpt.get("clean_scores", {ds: {} for ds in DATASETS})
        attacked_scores = ckpt.get("attacked_scores",
                                   {ds: {a: {} for a in ATTACK_NAMES} for ds in DATASETS})
    else:
        pairs = {}
        for ds in DATASETS:
            samples = load_eval_dataset(ds, 300)
            pairs[ds] = generate_response_pairs(samples, ds)
            logger.info(f"Dataset {ds}: {len(pairs[ds])} pairs prepared")
        clean_scores = {ds: {} for ds in DATASETS}
        attacked_scores = {ds: {a: {} for a in ATTACK_NAMES} for ds in DATASETS}

    attacked_items = {}
    for ds in DATASETS:
        attacked_items[ds] = {}
        for aname in ATTACK_NAMES:
            attacked_items[ds][aname] = apply_attack_to_pairs(pairs[ds], attacks[aname])

    for mid in MODEL_IDS:
        needs_work = any(
            mid not in clean_scores.get(ds, {}) or
            any(mid not in attacked_scores.get(ds, {}).get(a, {}) for a in ATTACK_NAMES)
            for ds in DATASETS
        )
        if not needs_work:
            logger.info(f"[{mid}] already scored, skip")
            continue

        logger.info(f"[{mid}] Loading model...")
        judge = JudgeService(mid)
        judge.load()
        try:
            for ds in DATASETS:
                if mid not in clean_scores[ds]:
                    logger.info(f"  [{mid}] scoring {ds} clean...")
                    clean_scores[ds][mid] = judge.batch_score(pairs[ds], mode="pairwise")
                    logger.info(f"    {len(clean_scores[ds][mid])} scores")
                for aname in ATTACK_NAMES:
                    if mid not in attacked_scores[ds][aname]:
                        logger.info(f"  [{mid}] scoring {ds}+{aname}...")
                        attacked_scores[ds][aname][mid] = judge.batch_score(
                            attacked_items[ds][aname], mode="pairwise"
                        )
        finally:
            logger.info(f"[{mid}] Unloading...")
            judge.unload()

        save_ckpt({
            "clean_scores": clean_scores,
            "attacked_scores": attacked_scores,
            "pairs": pairs,
            "phase1_complete": False,
        })

    save_ckpt({
        "clean_scores": clean_scores,
        "attacked_scores": attacked_scores,
        "pairs": pairs,
        "phase1_complete": True,
    })
    return clean_scores, attacked_scores, pairs


# ── Phase 2: Individual Model ASR ───────────────────────────────────

def phase2_individual_asr(clean_scores, attacked_scores, pairs):
    logger.info("=" * 60)
    logger.info("PHASE 2: Individual Model ASR")
    logger.info("=" * 60)

    ind_asr = {ds: {a: {} for a in ATTACK_NAMES} for ds in DATASETS}
    for ds in DATASETS:
        for aname in ATTACK_NAMES:
            for mid in MODEL_IDS:
                ind_asr[ds][aname][mid] = measure_asr(
                    clean_scores[ds][mid],
                    attacked_scores[ds][aname][mid],
                    pairs[ds],
                )

    for ds in DATASETS:
        logger.info(f"\n--- {ds} ---")
        hdr = f"{'Model':<20}" + "".join(f"{a:<22}" for a in ATTACK_NAMES)
        logger.info(hdr)
        logger.info("-" * len(hdr))
        for mid in MODEL_IDS:
            row = f"{mid:<20}" + "".join(
                f"{ind_asr[ds][a][mid]:<22.4f}" for a in ATTACK_NAMES
            )
            logger.info(row)

    return ind_asr


# ── Phase 3: Panel Enumeration + OLS Regression ─────────────────────

def phase3_regression(clean_scores, attacked_scores, pairs, ind_asr, step1):
    logger.info("=" * 60)
    logger.info("PHASE 3: Multi-variate Regression (20 panels)")
    logger.info("=" * 60)

    combos = list(combinations(MODEL_IDS, 3))
    all_panels = []

    for combo in combos:
        jids = list(combo)
        panel = Panel(jids)
        entry = {"judge_ids": jids, "k_eff": {}, "asr_by_attack": {}, "eta_max_by_attack": {}}

        for ds in DATASETS:
            entry["k_eff"][ds] = mi_based_keff(step1[ds]["pairwise"], jids)
            entry["asr_by_attack"][ds] = {}
            entry["eta_max_by_attack"][ds] = {}
            for aname in ATTACK_NAMES:
                cs = {m: clean_scores[ds][m] for m in jids}
                at = {m: attacked_scores[ds][aname][m] for m in jids}
                entry["asr_by_attack"][ds][aname] = measure_panel_asr(
                    panel, cs, at, pairs[ds]
                )
                entry["eta_max_by_attack"][ds][aname] = max(
                    ind_asr[ds][aname][m] for m in jids
                )

        all_panels.append(entry)

    reg = {ds: {} for ds in DATASETS}
    for ds in DATASETS:
        for aname in ATTACK_NAMES:
            y_raw = np.array([p["asr_by_attack"][ds][aname] for p in all_panels])
            x_keff = np.array([p["k_eff"][ds] for p in all_panels])
            x_eta = np.array([p["eta_max_by_attack"][ds][aname] for p in all_panels])

            y = np.log(y_raw + EPS)
            X = np.column_stack([np.log(x_keff), np.log(x_eta + EPS)])
            X = sm.add_constant(X)

            fit = sm.OLS(y, X).fit()

            reg[ds][aname] = {
                "coefficients": {
                    "const": float(fit.params[0]),
                    "log_keff": float(fit.params[1]),
                    "log_eta_max": float(fit.params[2]),
                },
                "t_values": {
                    "const": float(fit.tvalues[0]),
                    "log_keff": float(fit.tvalues[1]),
                    "log_eta_max": float(fit.tvalues[2]),
                },
                "p_values": {
                    "const": float(fit.pvalues[0]),
                    "log_keff": float(fit.pvalues[1]),
                    "log_eta_max": float(fit.pvalues[2]),
                },
                "r_squared": float(fit.rsquared),
                "adj_r_squared": float(fit.rsquared_adj),
                "n_panels": 20,
                "f_stat": float(fit.fvalue) if np.isfinite(fit.fvalue) else None,
                "f_pvalue": float(fit.f_pvalue) if np.isfinite(fit.f_pvalue) else None,
            }

            sig = ("***" if fit.pvalues[1] < 0.001 else
                   "**" if fit.pvalues[1] < 0.01 else
                   "*" if fit.pvalues[1] < 0.05 else "ns")
            logger.info(f"\n[OLS] {ds} x {aname}")
            logger.info(f"  R2={fit.rsquared:.4f}  Adj_R2={fit.rsquared_adj:.4f}")
            logger.info(
                f"  log(K_eff): B={fit.params[1]:+.4f}  t={fit.tvalues[1]:.3f}"
                f"  p={fit.pvalues[1]:.4f} {sig}"
            )
            logger.info(
                f"  log(eta_max): B={fit.params[2]:+.4f}  t={fit.tvalues[2]:.3f}"
                f"  p={fit.pvalues[2]:.4f}"
            )

    return all_panels, reg


# ── Phase 4: 4-Model Control Group ──────────────────────────────────

def phase4_control(clean_scores, attacked_scores, pairs, ind_asr, step1):
    logger.info("=" * 60)
    logger.info("PHASE 4: 4-Model Control Group (large models only)")
    logger.info("=" * 60)

    combos = list(combinations(LARGE_MODEL_IDS, 3))
    ctrl = {ds: {a: [] for a in ATTACK_NAMES} for ds in DATASETS}

    for combo in combos:
        jids = list(combo)
        panel = Panel(jids)
        for ds in DATASETS:
            keff = mi_based_keff(step1[ds]["pairwise"], jids)
            for aname in ATTACK_NAMES:
                cs = {m: clean_scores[ds][m] for m in jids}
                at = {m: attacked_scores[ds][aname][m] for m in jids}
                asr = measure_panel_asr(panel, cs, at, pairs[ds])
                eta = max(ind_asr[ds][aname][m] for m in jids)
                ctrl[ds][aname].append({
                    "panel_ids": jids,
                    "k_eff": keff,
                    "asr": asr,
                    "eta_max": eta,
                })

    for ds in DATASETS:
        for aname in ATTACK_NAMES:
            logger.info(f"\n[Control] {ds} x {aname}")
            for p in sorted(ctrl[ds][aname], key=lambda x: x["k_eff"], reverse=True):
                logger.info(
                    f"  K_eff={p['k_eff']:.3f}  ASR={p['asr']:.4f}"
                    f"  eta_max={p['eta_max']:.4f}  {p['panel_ids']}"
                )

    return ctrl


# ── Main ─────────────────────────────────────────────────────────────

def main():
    logger.info("Step 2 v3: Multi-variate Regression Analysis")
    step1 = load_step1()

    clean, attacked, pairs = phase1_inference()
    ind_asr = phase2_individual_asr(clean, attacked, pairs)
    all_panels, reg = phase3_regression(clean, attacked, pairs, ind_asr, step1)
    ctrl = phase4_control(clean, attacked, pairs, ind_asr, step1)

    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    out_path = RESULTS_DIR / f"results_step2v3_regression_{ts}.json"
    output = {
        "individual_asr": ind_asr,
        "regression": reg,
        "control_group_4model": ctrl,
        "all_20_panels": all_panels,
        "metadata": {
            "model_ids": MODEL_IDS,
            "attack_names": ATTACK_NAMES,
            "datasets": DATASETS,
            "epsilon": EPS,
            "large_model_ids": LARGE_MODEL_IDS,
            "timestamp": ts,
        },
    }
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default)
    logger.info(f"\nResults saved: {out_path}")

    logger.info("\n" + "=" * 60)
    logger.info("SUMMARY")
    logger.info("=" * 60)
    for ds in DATASETS:
        for aname in ATTACK_NAMES:
            r = reg[ds][aname]
            sig = ("***" if r["p_values"]["log_keff"] < 0.001 else
                   "**" if r["p_values"]["log_keff"] < 0.01 else
                   "*" if r["p_values"]["log_keff"] < 0.05 else "ns")
            logger.info(
                f"  {ds} x {aname}: B_keff={r['coefficients']['log_keff']:+.4f}"
                f" (p={r['p_values']['log_keff']:.4f} {sig}),"
                f" R2={r['r_squared']:.4f}"
            )


if __name__ == "__main__":
    main()
