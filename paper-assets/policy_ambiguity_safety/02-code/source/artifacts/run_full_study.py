#!/usr/bin/env python3
"""Full study execution script for policy ambiguity safety experiments.

Orchestrates the complete experiment pipeline:
  Phase 1: Episode generation (300 clauses x 2 conditions x 2 models = 1,200 episodes)
  Phase 2: Cross-judge evaluation (gpt-5.4 episodes judged by gpt-4.1, vice versa)
  Phase 3: Statistical analysis (binary/type/model effects + interactions)

Input:  artifacts/clause_templates_full.json (300 clauses, 6 types x 50)
Output: artifacts/full_study/{episodes,judgments,analysis}/

Dependencies: harness.py, judge.py, analyze.py, config.py
"""

import argparse
import asyncio
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

import config
import harness
import judge
import analyze

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

FULL_STUDY_DIR = config.ARTIFACTS_DIR / "full_study"
EPISODES_DIR = FULL_STUDY_DIR / "episodes"
JUDGMENTS_DIR = FULL_STUDY_DIR / "judgments"
ANALYSIS_DIR = FULL_STUDY_DIR / "analysis"
ERRORS_FILE = FULL_STUDY_DIR / "errors.jsonl"

DEFAULT_MODELS = ["gpt-5.4", "gpt-4.1", "claude-sonnet-4-6"]


# ---------------------------------------------------------------------------
# Phase 1: Episode Generation
# ---------------------------------------------------------------------------

def _load_completed_episodes(model_dir: Path) -> set[str]:
    """Return set of 'clause_id|condition' keys already completed."""
    completed = set()
    episodes_file = model_dir / "episodes.jsonl"
    if episodes_file.exists():
        with open(episodes_file) as f:
            for line in f:
                if line.strip():
                    rec = json.loads(line)
                    completed.add(f"{rec['clause_id']}|{rec['condition']}")
    return completed


async def run_phase1(
    clauses: list[dict],
    models: list[str],
    concurrency: int,
    resume: bool,
):
    """Generate episodes for all model x clause x condition combinations."""
    FULL_STUDY_DIR.mkdir(parents=True, exist_ok=True)

    print("Preflight API check...")
    for m in models:
        try:
            await harness.preflight_check(m)
            print(f"  {m}: OK")
        except Exception as e:
            print(f"  {m}: FAILED — {e}")
            raise SystemExit(f"Preflight failed for {m}. Fix API key/endpoint before running.")

    total_done = 0
    total_errors = 0
    total_skipped = 0

    for model_name in models:
        model_dir = EPISODES_DIR / model_name
        model_dir.mkdir(parents=True, exist_ok=True)

        completed = _load_completed_episodes(model_dir) if resume else set()
        tasks = []
        for clause in clauses:
            for condition in ("ambiguous", "unambiguous"):
                key = f"{clause['clause_id']}|{condition}"
                if key in completed:
                    total_skipped += 1
                    continue
                tasks.append((clause, condition))

        if not tasks:
            print(f"[{model_name}] All {len(completed)} episodes complete.")
            continue

        print(f"[{model_name}] {len(tasks)} episodes to run "
              f"(skipping {len(completed)}, concurrency={concurrency})")

        semaphore = asyncio.Semaphore(concurrency)
        output_file = model_dir / "episodes.jsonl"
        lock = asyncio.Lock()
        done = 0
        errors = 0

        async def _run_one(clause, condition, _model=model_name):
            nonlocal done, errors
            async with semaphore:
                try:
                    result = await harness.run_episode(clause, condition, _model)
                    validity = harness.validate_episode(result)
                    if validity != "ok":
                        raise RuntimeError(
                            f"Episode {validity}: {result.get('error', 'no assistant response')}"
                        )
                    async with lock:
                        with open(output_file, "a") as f:
                            f.write(json.dumps(result, ensure_ascii=False) + "\n")
                        done += 1
                        if done % 50 == 0:
                            print(f"  [{_model}] {done}/{len(tasks)}")
                except Exception as e:
                    async with lock:
                        errors += 1
                        with open(ERRORS_FILE, "a") as f:
                            f.write(json.dumps({
                                "phase": 1, "model": _model,
                                "clause_id": clause["clause_id"],
                                "condition": condition,
                                "error": str(e),
                                "timestamp": time.time(),
                            }, ensure_ascii=False) + "\n")

        await asyncio.gather(*[_run_one(c, cond) for c, cond in tasks])
        print(f"  [{model_name}] {done} done, {errors} errors")
        total_done += done
        total_errors += errors

    print(f"\nPhase 1 summary: {total_done} done / {total_errors} errors / "
          f"{total_skipped} skipped")


# ---------------------------------------------------------------------------
# Phase 2: Cross-Judge Evaluation
# ---------------------------------------------------------------------------

def _load_judged_ids(model_dir: Path) -> set[str]:
    """Return set of episode_ids already judged."""
    judged = set()
    judgments_file = model_dir / "judgments.jsonl"
    if judgments_file.exists():
        with open(judgments_file) as f:
            for line in f:
                if line.strip():
                    judged.add(json.loads(line)["episode_id"])
    return judged


async def run_phase2(
    clauses: list[dict],
    models: list[str],
    concurrency: int,
    resume: bool,
):
    """Cross-judge all episodes (each model's episodes judged by the other)."""
    clause_index = judge.build_clause_index(clauses)
    total_done = 0
    total_errors = 0
    total_skipped = 0

    for model_name in models:
        ep_dir = EPISODES_DIR / model_name
        if not ep_dir.exists():
            print(f"[{model_name}] No episodes found — run Phase 1 first.")
            continue

        episodes = judge.load_episodes(ep_dir)
        if not episodes:
            print(f"[{model_name}] No episode files found.")
            continue

        judge_model = config.CROSS_JUDGE_MAP[model_name]
        jdg_dir = JUDGMENTS_DIR / model_name
        jdg_dir.mkdir(parents=True, exist_ok=True)

        judged_ids = _load_judged_ids(jdg_dir) if resume else set()
        pending = [ep for ep in episodes if ep["episode_id"] not in judged_ids]
        total_skipped += len(episodes) - len(pending)

        if not pending:
            print(f"[{model_name}] All {len(episodes)} episodes already judged.")
            continue

        print(f"[{model_name}] Judging {len(pending)} episodes "
              f"(judge={judge_model}, concurrency={concurrency})")

        semaphore = asyncio.Semaphore(concurrency)
        output_file = jdg_dir / "judgments.jsonl"
        lock = asyncio.Lock()
        done = 0
        errors = 0

        async def _judge_one(episode, _model=model_name):
            nonlocal done, errors
            async with semaphore:
                try:
                    result = await judge.judge_episode(episode, clause_index)
                    async with lock:
                        with open(output_file, "a") as f:
                            f.write(json.dumps(result, ensure_ascii=False) + "\n")
                        done += 1
                        if done % 50 == 0:
                            print(f"  [{_model}] {done}/{len(pending)} judged")
                except Exception as e:
                    async with lock:
                        errors += 1
                        with open(ERRORS_FILE, "a") as f:
                            f.write(json.dumps({
                                "phase": 2, "model": _model,
                                "episode_id": episode.get("episode_id", "?"),
                                "error": str(e),
                                "timestamp": time.time(),
                            }, ensure_ascii=False) + "\n")

        await asyncio.gather(*[_judge_one(ep) for ep in pending])
        print(f"  [{model_name}] {done} judged, {errors} errors")
        total_done += done
        total_errors += errors

    print(f"\nPhase 2 summary: {total_done} done / {total_errors} errors / "
          f"{total_skipped} skipped")


# ---------------------------------------------------------------------------
# Phase 3: Analysis
# ---------------------------------------------------------------------------

def _load_all_judgments(models: list[str]) -> pd.DataFrame:
    """Load judgments from all model subdirectories into one DataFrame."""
    records = []
    for model_name in models:
        jdg_dir = JUDGMENTS_DIR / model_name
        if not jdg_dir.exists():
            continue
        for jsonl_file in jdg_dir.glob("*.jsonl"):
            with open(jsonl_file) as f:
                for line in f:
                    if not line.strip():
                        continue
                    rec = json.loads(line)
                    records.append({
                        "episode_id": rec["episode_id"],
                        "clause_id": rec["clause_id"],
                        "ambiguity_type": rec["ambiguity_type"],
                        "condition": rec["condition"],
                        "model": rec["model"],
                        "violation_level": rec["judgment"]["violation_level"],
                        "confidence": rec["judgment"]["confidence"],
                        "judge_model": rec["judge_model"],
                    })
    df = pd.DataFrame(records)
    if df.empty:
        return df
    level_order = pd.CategoricalDtype(
        categories=config.VIOLATION_LEVELS, ordered=True
    )
    df["violation_level"] = df["violation_level"].astype(level_order)
    return df


def _binary_effect(df: pd.DataFrame) -> dict:
    """(a) Ambiguous vs unambiguous violation rates: global, per-type, per-model."""
    df = df.copy()
    df["violated"] = analyze.binarize_violations(df)

    # Global
    cond_rates = df.groupby("condition")["violated"].agg(["mean", "sum", "count"])
    amb_r = float(cond_rates.loc["ambiguous", "mean"]) if "ambiguous" in cond_rates.index else float("nan")
    una_r = float(cond_rates.loc["unambiguous", "mean"]) if "unambiguous" in cond_rates.index else float("nan")
    ct = pd.crosstab(df["condition"], df["violated"])
    if ct.shape == (2, 2):
        chi2, p, _, _ = stats.chi2_contingency(ct.values)
    else:
        chi2, p = float("nan"), float("nan")
    glob = {
        "ambiguous_rate": amb_r, "unambiguous_rate": una_r,
        "difference": amb_r - una_r if not (np.isnan(amb_r) or np.isnan(una_r)) else None,
        "chi2": float(chi2), "p": float(p),
    }

    # Per-type
    per_type = {}
    for atype, tdf in df.groupby("ambiguity_type"):
        tr = tdf.groupby("condition")["violated"].mean()
        a, u = tr.get("ambiguous", np.nan), tr.get("unambiguous", np.nan)
        ct_t = pd.crosstab(tdf["condition"], tdf["violated"])
        fp = float(stats.fisher_exact(ct_t.values)[1]) if ct_t.shape == (2, 2) else float("nan")
        per_type[atype] = {
            "ambiguous_rate": float(a), "unambiguous_rate": float(u),
            "difference": float(a - u) if not (np.isnan(a) or np.isnan(u)) else None,
            "fisher_p": fp,
        }

    # Per-model
    per_model = {}
    for mname, mdf in df.groupby("model"):
        mr = mdf.groupby("condition")["violated"].mean()
        a, u = mr.get("ambiguous", np.nan), mr.get("unambiguous", np.nan)
        ct_m = pd.crosstab(mdf["condition"], mdf["violated"])
        fp = float(stats.fisher_exact(ct_m.values)[1]) if ct_m.shape == (2, 2) else float("nan")
        per_model[mname] = {
            "ambiguous_rate": float(a), "unambiguous_rate": float(u),
            "difference": float(a - u) if not (np.isnan(a) or np.isnan(u)) else None,
            "fisher_p": fp,
        }

    return {"global": glob, "per_type": per_type, "per_model": per_model}


def _type_effect(df: pd.DataFrame) -> dict:
    """(b) 6-way chi-square across ambiguity types (ambiguous episodes only)."""
    amb = df[df["condition"] == "ambiguous"].copy()
    if amb.empty:
        return {"error": "No ambiguous episodes"}
    amb["violated"] = analyze.binarize_violations(amb)

    type_rates = amb.groupby("ambiguity_type")["violated"].agg(["mean", "sum", "count"])
    type_rates.columns = ["violation_rate", "n_violations", "n_total"]

    ct = pd.crosstab(amb["ambiguity_type"], amb["violated"])
    if ct.shape[0] >= 2 and ct.shape[1] >= 2:
        chi2, p, dof, _ = stats.chi2_contingency(ct.values)
        v = analyze.cramers_v(ct.values)
    else:
        chi2, p, dof, v = float("nan"), float("nan"), 0, 0.0

    return {
        "rates": type_rates.to_dict(orient="index"),
        "chi2": float(chi2), "p": float(p), "dof": int(dof),
        "cramers_v": float(v),
    }


def _model_effect(df: pd.DataFrame) -> dict:
    """(c) Model comparison: gpt-5.4 vs gpt-4.1 violation rates."""
    df = df.copy()
    df["violated"] = analyze.binarize_violations(df)

    model_rates = df.groupby("model")["violated"].agg(["mean", "sum", "count"])
    model_rates.columns = ["violation_rate", "n_violations", "n_total"]

    ct = pd.crosstab(df["model"], df["violated"])
    if ct.shape[0] >= 2 and ct.shape[1] >= 2:
        chi2, p, _, _ = stats.chi2_contingency(ct.values)
        v = analyze.cramers_v(ct.values)
    else:
        chi2, p, v = float("nan"), float("nan"), 0.0

    # Ambiguous-only subset
    amb = df[df["condition"] == "ambiguous"]
    amb_rates = amb.groupby("model")["violated"].agg(["mean", "sum", "count"])
    amb_rates.columns = ["violation_rate", "n_violations", "n_total"]
    ct_a = pd.crosstab(amb["model"], amb["violated"])
    if ct_a.shape[0] >= 2 and ct_a.shape[1] >= 2:
        chi2_a, p_a, _, _ = stats.chi2_contingency(ct_a.values)
    else:
        chi2_a, p_a = float("nan"), float("nan")

    return {
        "overall": model_rates.to_dict(orient="index"),
        "overall_chi2": float(chi2), "overall_p": float(p),
        "cramers_v": float(v),
        "ambiguous_only": amb_rates.to_dict(orient="index"),
        "ambiguous_chi2": float(chi2_a), "ambiguous_p": float(p_a),
    }


def _interaction(df: pd.DataFrame) -> dict:
    """(d) Model x Type interaction (ambiguous episodes only)."""
    amb = df[df["condition"] == "ambiguous"].copy()
    if amb.empty:
        return {"error": "No ambiguous episodes"}
    amb["violated"] = analyze.binarize_violations(amb)

    per_model_rates = {}
    per_model_chi2 = {}
    rankings = {}

    for mname, mdf in amb.groupby("model"):
        tr = mdf.groupby("ambiguity_type")["violated"].agg(["mean", "sum", "count"])
        tr.columns = ["violation_rate", "n_violations", "n_total"]
        per_model_rates[mname] = tr.to_dict(orient="index")

        ct = pd.crosstab(mdf["ambiguity_type"], mdf["violated"])
        if ct.shape[0] >= 2 and ct.shape[1] >= 2:
            chi2, p, dof, _ = stats.chi2_contingency(ct.values)
            v = analyze.cramers_v(ct.values)
        else:
            chi2, p, dof, v = float("nan"), float("nan"), 0, 0.0
        per_model_chi2[mname] = {
            "chi2": float(chi2), "p": float(p),
            "dof": int(dof), "cramers_v": float(v),
        }

        sorted_types = sorted(
            per_model_rates[mname].items(),
            key=lambda x: x[1]["violation_rate"], reverse=True,
        )
        rankings[mname] = [t[0] for t in sorted_types]

    return {
        "per_model_type_rates": per_model_rates,
        "per_model_chi2": per_model_chi2,
        "type_rankings": rankings,
    }


def _print_full_report(binary: dict, type_eff: dict,
                       model_eff: dict, interact: dict):
    """Print formatted analysis report to console."""
    print("\n" + "=" * 72)
    print("FULL STUDY — STATISTICAL ANALYSIS REPORT")
    print("=" * 72)

    # (a) Binary effect
    print("\n-- (a) Binary Effect: Ambiguous vs Unambiguous --\n")
    g = binary["global"]
    diff_str = f"{g['difference']:+.1%}" if g["difference"] is not None else "N/A"
    print(f"  Global: amb={g['ambiguous_rate']:.1%}  unamb={g['unambiguous_rate']:.1%}"
          f"  D={diff_str}  chi2 p={g['p']:.4f}")

    print(f"\n  {'Type':<25} {'Amb':>7} {'Unamb':>7} {'D':>7} {'Fisher p':>9}")
    print(f"  {'-'*25} {'-'*7} {'-'*7} {'-'*7} {'-'*9}")
    for atype in sorted(binary["per_type"]):
        r = binary["per_type"][atype]
        d = r["difference"]
        if d is not None:
            print(f"  {atype:<25} {r['ambiguous_rate']:>6.1%} {r['unambiguous_rate']:>6.1%}"
                  f" {d:>+6.1%} {r['fisher_p']:>9.4f}")
        else:
            print(f"  {atype:<25}  insufficient data")

    print(f"\n  {'Model':<15} {'Amb':>7} {'Unamb':>7} {'D':>7} {'Fisher p':>9}")
    print(f"  {'-'*15} {'-'*7} {'-'*7} {'-'*7} {'-'*9}")
    for mname in sorted(binary["per_model"]):
        r = binary["per_model"][mname]
        d = r["difference"]
        if d is not None:
            print(f"  {mname:<15} {r['ambiguous_rate']:>6.1%} {r['unambiguous_rate']:>6.1%}"
                  f" {d:>+6.1%} {r['fisher_p']:>9.4f}")

    # (b) Type effect
    print("\n-- (b) Type Effect: 6-way chi-square (ambiguous only) --\n")
    rates = type_eff.get("rates", {})
    print(f"  {'Type':<25} {'Rate':>10} {'N':>6}")
    print(f"  {'-'*25} {'-'*10} {'-'*6}")
    for atype in sorted(rates):
        r = rates[atype]
        print(f"  {atype:<25} {r['violation_rate']:>9.1%} {r['n_total']:>6.0f}")
    print(f"\n  chi2={type_eff['chi2']:.3f}  p={type_eff['p']:.4f}"
          f"  dof={type_eff['dof']}  Cramer's V={type_eff['cramers_v']:.3f}")

    # (c) Model effect
    print("\n-- (c) Model Effect --\n")
    ov = model_eff.get("overall", {})
    print(f"  {'Model':<15} {'Rate':>8} {'N_viol':>7} {'N':>6}")
    print(f"  {'-'*15} {'-'*8} {'-'*7} {'-'*6}")
    for mname in sorted(ov):
        r = ov[mname]
        print(f"  {mname:<15} {r['violation_rate']:>7.1%} {r['n_violations']:>7.0f}"
              f" {r['n_total']:>6.0f}")
    print(f"\n  Overall: chi2 p={model_eff['overall_p']:.4f}  V={model_eff['cramers_v']:.3f}")
    print(f"  Ambiguous-only: chi2 p={model_eff['ambiguous_p']:.4f}")

    # (d) Interaction
    print("\n-- (d) Model x Type Interaction --\n")
    for mname in sorted(interact.get("per_model_chi2", {})):
        c = interact["per_model_chi2"][mname]
        print(f"  [{mname}] type chi2={c['chi2']:.3f}  p={c['p']:.4f}"
              f"  V={c['cramers_v']:.3f}")
    print()
    for mname in sorted(interact.get("type_rankings", {})):
        ranking = interact["type_rankings"][mname]
        print(f"  {mname}: {' > '.join(ranking)}")

    print("\n" + "=" * 72)


# ---------------------------------------------------------------------------
# Phase 3 Extended: Dream reviewer analyses (A3, A4, A10 + bootstrap/McNemar/Fleiss)
# ---------------------------------------------------------------------------

def run_power_analysis(df: pd.DataFrame, clauses: list[dict]) -> dict:
    """Dream A3: Power analysis for C2 (type uniformity) and C3 (per-type)."""
    amb = df[df["condition"] == "ambiguous"].copy()
    if amb.empty:
        return {"error": "No ambiguous episodes"}
    amb["violated"] = analyze.binarize_violations(amb)

    types = sorted(amb["ambiguity_type"].unique())
    n_types = len(types)
    alpha = 0.05
    target_power = 0.80

    def _find_mde(n_total, df_val):
        crit = stats.chi2.ppf(1 - alpha, df_val)
        lo, hi = 1e-4, 1.0
        for _ in range(200):
            mid = (lo + hi) / 2
            pwr = 1 - stats.ncx2.cdf(crit, df_val, n_total * mid ** 2)
            if pwr < target_power:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    def _compute_power(w, n_total, df_val):
        crit = stats.chi2.ppf(1 - alpha, df_val)
        return float(1 - stats.ncx2.cdf(crit, df_val, n_total * w ** 2))

    c2_n_per_type = 200
    c2_n_total = c2_n_per_type * n_types
    c2_df = max(n_types - 1, 1)
    c2_mde = _find_mde(c2_n_total, c2_df)

    c3_n = 200
    c3_df = 1
    c3_mde = _find_mde(c3_n, c3_df)

    ct = pd.crosstab(amb["ambiguity_type"], amb["violated"])
    observed_v = (
        analyze.cramers_v(ct.values)
        if ct.shape[0] >= 2 and ct.shape[1] >= 2
        else 0.0
    )

    actual_n = len(amb)
    mde_actual = _find_mde(actual_n, c2_df)
    power_at_observed = (
        _compute_power(observed_v, actual_n, c2_df) if observed_v > 0 else 0.0
    )

    underpowered = observed_v < 0.20 and c2_mde > observed_v

    result = {
        "c2_type_uniformity": {
            "design_N_per_type": c2_n_per_type,
            "design_N_total": c2_n_total,
            "n_types": n_types,
            "df": c2_df,
            "alpha": alpha,
            "target_power": target_power,
            "mde_cramers_v": round(c2_mde, 4),
        },
        "c3_per_type_comparison": {
            "design_N": c3_n,
            "df": c3_df,
            "alpha": alpha,
            "target_power": target_power,
            "mde_cramers_v": round(c3_mde, 4),
        },
        "observed_cramers_v": round(float(observed_v), 4),
        "actual_sample": {
            "N_total": actual_n,
            "per_type": {
                t: int(v)
                for t, v in amb.groupby("ambiguity_type").size().items()
            },
            "mde_cramers_v": round(mde_actual, 4),
            "power_at_observed": round(power_at_observed, 4),
        },
        "underpowered_warning": underpowered,
    }

    out = ANALYSIS_DIR / "power_analysis.json"
    with open(out, "w") as f:
        json.dump(result, f, indent=2, default=str)
    print(f"  -> {out.name}")
    return result


def run_tost_equivalence(df: pd.DataFrame, clauses: list[dict]) -> dict:
    """Dream A4: TOST equivalence test for C2 type uniformity."""
    amb = df[df["condition"] == "ambiguous"].copy()
    if amb.empty:
        return {"error": "No ambiguous episodes"}
    amb["violated"] = analyze.binarize_violations(amb)

    types = sorted(amb["ambiguity_type"].unique())
    margins = [0.15, 0.10]

    results_by_margin = {}
    for margin in margins:
        pairwise = []
        for i in range(len(types)):
            for j in range(i + 1, len(types)):
                t1, t2 = types[i], types[j]
                d1 = amb[amb["ambiguity_type"] == t1]["violated"]
                d2 = amb[amb["ambiguity_type"] == t2]["violated"]
                p1, n1 = float(d1.mean()), len(d1)
                p2, n2 = float(d2.mean()), len(d2)
                diff = p1 - p2

                if n1 > 0 and n2 > 0:
                    se = np.sqrt(
                        p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2
                    )
                else:
                    se = float("inf")

                if se > 0 and np.isfinite(se):
                    z_lower = (diff + margin) / se
                    p_lower = float(1 - stats.norm.cdf(z_lower))
                    z_upper = (diff - margin) / se
                    p_upper = float(stats.norm.cdf(z_upper))
                    tost_p = max(p_lower, p_upper)
                    equivalent = tost_p < 0.05
                else:
                    z_lower = z_upper = tost_p = float("nan")
                    p_lower = p_upper = float("nan")
                    equivalent = False

                pairwise.append({
                    "type_1": t1,
                    "type_2": t2,
                    "rate_1": round(p1, 4),
                    "rate_2": round(p2, 4),
                    "difference": round(diff, 4),
                    "se": round(float(se), 4),
                    "z_lower": round(float(z_lower), 4),
                    "p_lower": round(float(p_lower), 4),
                    "z_upper": round(float(z_upper), 4),
                    "p_upper": round(float(p_upper), 4),
                    "tost_p": round(float(tost_p), 4),
                    "equivalent": equivalent,
                })

        all_equiv = all(p["equivalent"] for p in pairwise) if pairwise else False
        results_by_margin[f"margin_{int(margin * 100)}pp"] = {
            "margin": margin,
            "pairwise": pairwise,
            "all_pairs_equivalent": all_equiv,
        }

    result = {
        "test": "TOST two one-sided z-tests for proportions",
        "margin_justification": (
            "15pp = practical significance threshold for policy remediation "
            "cost; 10pp = stricter robustness check"
        ),
        **results_by_margin,
    }

    out = ANALYSIS_DIR / "tost_equivalence.json"
    with open(out, "w") as f:
        json.dump(result, f, indent=2, default=str)
    print(f"  -> {out.name}")
    return result


def _bca_ci(g1: np.ndarray, g2: np.ndarray, rng, B: int = 10000,
            alpha: float = 0.05) -> dict:
    """BCa bootstrap CI for difference in means (g1 - g2)."""
    n1, n2 = len(g1), len(g2)
    if n1 == 0 or n2 == 0:
        return {"observed_diff": None, "ci_lower": None, "ci_upper": None}

    observed = float(g1.mean() - g2.mean())

    idx1 = rng.integers(0, n1, size=(B, n1))
    idx2 = rng.integers(0, n2, size=(B, n2))
    boot_stats = g1[idx1].mean(axis=1) - g2[idx2].mean(axis=1)

    prop_below = np.mean(boot_stats < observed)
    prop_below = np.clip(prop_below, 1 / (B + 1), B / (B + 1))
    z0 = stats.norm.ppf(prop_below)

    if n1 >= 2 and n2 >= 2:
        jack = np.empty(n1 + n2)
        g1_sum, g2_mean = g1.sum(), g2.mean()
        g1_mean, g2_sum = g1.mean(), g2.sum()
        for i in range(n1):
            jack[i] = (g1_sum - g1[i]) / (n1 - 1) - g2_mean
        for j in range(n2):
            jack[n1 + j] = g1_mean - (g2_sum - g2[j]) / (n2 - 1)
        jm = jack.mean()
        d = jm - jack
        denom = 6 * np.sum(d ** 2) ** 1.5
        a = float(np.sum(d ** 3) / denom) if denom > 0 else 0.0
    else:
        a = 0.0

    z_lo = stats.norm.ppf(alpha / 2)
    z_hi = stats.norm.ppf(1 - alpha / 2)

    def _adj(z):
        num = z0 + z
        den = 1 - a * num
        if abs(den) < 1e-12:
            return 0.5
        return stats.norm.cdf(z0 + num / den)

    a1 = np.clip(_adj(z_lo), 0.5 / B, 1 - 0.5 / B)
    a2 = np.clip(_adj(z_hi), 0.5 / B, 1 - 0.5 / B)

    return {
        "observed_diff": round(observed, 4),
        "ci_lower": round(float(np.percentile(boot_stats, 100 * a1)), 4),
        "ci_upper": round(float(np.percentile(boot_stats, 100 * a2)), 4),
        "z0": round(float(z0), 4),
        "acceleration": round(a, 6),
    }


def run_bootstrap_ci(df: pd.DataFrame, clauses: list[dict]) -> dict:
    """BCa bootstrap 95% CIs for all pairwise comparisons."""
    B = 10000
    rng = np.random.default_rng(42)

    dfc = df.copy()
    dfc["violated"] = analyze.binarize_violations(dfc).astype(float)

    results: dict = {"n_resamples": B}

    # Global ambig vs unambig
    amb_v = dfc.loc[dfc["condition"] == "ambiguous", "violated"].values
    una_v = dfc.loc[dfc["condition"] == "unambiguous", "violated"].values
    results["ambig_vs_unambig_global"] = _bca_ci(amb_v, una_v, rng, B)

    # Per-type ambig vs unambig
    per_type = {}
    for atype in sorted(dfc["ambiguity_type"].unique()):
        tdf = dfc[dfc["ambiguity_type"] == atype]
        a = tdf.loc[tdf["condition"] == "ambiguous", "violated"].values
        u = tdf.loc[tdf["condition"] == "unambiguous", "violated"].values
        per_type[atype] = _bca_ci(a, u, rng, B)
    results["ambig_vs_unambig_per_type"] = per_type

    # Type pairs (ambiguous only)
    amb_df = dfc[dfc["condition"] == "ambiguous"]
    types = sorted(amb_df["ambiguity_type"].unique())
    type_pairs = {}
    for i in range(len(types)):
        for j in range(i + 1, len(types)):
            t1, t2 = types[i], types[j]
            v1 = amb_df.loc[amb_df["ambiguity_type"] == t1, "violated"].values
            v2 = amb_df.loc[amb_df["ambiguity_type"] == t2, "violated"].values
            type_pairs[f"{t1}_vs_{t2}"] = _bca_ci(v1, v2, rng, B)
    results["type_pairs_ambiguous"] = type_pairs

    # Model pairs
    models = sorted(dfc["model"].unique())
    model_pairs = {}
    for i in range(len(models)):
        for j in range(i + 1, len(models)):
            m1, m2 = models[i], models[j]
            v1 = dfc.loc[dfc["model"] == m1, "violated"].values
            v2 = dfc.loc[dfc["model"] == m2, "violated"].values
            model_pairs[f"{m1}_vs_{m2}"] = _bca_ci(v1, v2, rng, B)
    results["model_pairs"] = model_pairs

    out = ANALYSIS_DIR / "bootstrap_ci.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"  -> {out.name}")
    return results


def run_mcnemar_matched(df: pd.DataFrame, clauses: list[dict]) -> dict:
    """Matched-pair McNemar test for C1 (binary effect)."""
    dfc = df.copy()
    dfc["violated"] = analyze.binarize_violations(dfc)

    amb = dfc.loc[dfc["condition"] == "ambiguous", ["clause_id", "model", "violated"]]
    una = dfc.loc[dfc["condition"] == "unambiguous", ["clause_id", "model", "violated"]]
    merged = pd.merge(amb, una, on=["clause_id", "model"], suffixes=("_amb", "_una"))

    if merged.empty:
        return {"error": "No matched pairs found"}

    merged["amb_only"] = merged["violated_amb"] & ~merged["violated_una"]
    merged["una_only"] = ~merged["violated_amb"] & merged["violated_una"]
    merged["both"] = merged["violated_amb"] & merged["violated_una"]
    merged["neither"] = ~merged["violated_amb"] & ~merged["violated_una"]

    b_total = int(merged["amb_only"].sum())
    c_total = int(merged["una_only"].sum())
    n_pairs = len(merged)
    n_disc = b_total + c_total

    # Overall McNemar
    if n_disc > 0:
        if n_disc >= 25:
            mcn_chi2 = float((abs(b_total - c_total) - 1) ** 2 / n_disc)
            mcn_p = float(1 - stats.chi2.cdf(mcn_chi2, 1))
            method = "chi-square (continuity corrected)"
        else:
            mcn_p = float(stats.binomtest(b_total, n_disc, 0.5).pvalue)
            mcn_chi2 = None
            method = "exact binomial"
    else:
        mcn_chi2 = 0.0
        mcn_p = 1.0
        method = "no discordant pairs"

    # Odds ratio b/c with Wald 95% CI
    if b_total > 0 and c_total > 0:
        or_val = b_total / c_total
        log_or = np.log(or_val)
        se_log = np.sqrt(1 / b_total + 1 / c_total)
        or_lo = float(np.exp(log_or - 1.96 * se_log))
        or_hi = float(np.exp(log_or + 1.96 * se_log))
    elif c_total == 0 and b_total > 0:
        or_val, or_lo, or_hi = float("inf"), float("nan"), float("nan")
    elif b_total == 0 and c_total > 0:
        or_val, or_lo, or_hi = 0.0, float("nan"), float("nan")
    else:
        or_val = or_lo = or_hi = float("nan")

    # Per-model McNemar
    per_model = {}
    for model_name, mdf in merged.groupby("model"):
        b_m = int(mdf["amb_only"].sum())
        c_m = int(mdf["una_only"].sum())
        disc_m = b_m + c_m
        if disc_m > 0:
            p_m = float(stats.binomtest(b_m, disc_m, 0.5).pvalue)
        else:
            p_m = 1.0
        per_model[model_name] = {
            "n_pairs": len(mdf),
            "b_amb_only": b_m,
            "c_una_only": c_m,
            "mcnemar_p": round(p_m, 6),
        }

    # Mantel-Haenszel OR stratified by ambiguity_type
    mh_strata = []
    for atype, sdf in merged.groupby(
        merged["clause_id"].map(
            lambda cid: dfc.loc[dfc["clause_id"] == cid, "ambiguity_type"].iloc[0]
            if cid in dfc["clause_id"].values else "unknown"
        )
    ):
        b_s = int(sdf["amb_only"].sum())
        c_s = int(sdf["una_only"].sum())
        a_s = int(sdf["both"].sum())
        d_s = int(sdf["neither"].sum())
        n_s = len(sdf)
        mh_strata.append({
            "stratum": atype, "n": n_s,
            "a": a_s, "b": b_s, "c": c_s, "d": d_s,
        })

    # Haldane 0.5 correction for strata with zero cells
    mh_num = 0.0
    mh_den = 0.0
    for s in mh_strata:
        if s["n"] == 0:
            continue
        a, b, c, d, n = s["a"], s["b"], s["c"], s["d"], s["n"]
        if a == 0 or b == 0 or c == 0 or d == 0:
            a, b, c, d, n = a + 0.5, b + 0.5, c + 0.5, d + 0.5, n + 2
        mh_num += b * d / n
        mh_den += c * a / n
    mh_or = mh_num / mh_den if mh_den > 0 else float("inf") if mh_num > 0 else float("nan")

    def _safe_round(v, n=4):
        if isinstance(v, float) and (np.isnan(v) or np.isinf(v)):
            return str(v)
        return round(float(v), n)

    result = {
        "n_pairs": n_pairs,
        "n_concordant": int(merged["both"].sum() + merged["neither"].sum()),
        "n_discordant": n_disc,
        "b_amb_only": b_total,
        "c_una_only": c_total,
        "mcnemar": {
            "method": method,
            "statistic": _safe_round(mcn_chi2) if mcn_chi2 is not None else None,
            "p": round(mcn_p, 6),
        },
        "odds_ratio": {
            "or": _safe_round(or_val),
            "ci_95_lower": _safe_round(or_lo),
            "ci_95_upper": _safe_round(or_hi),
        },
        "mantel_haenszel": {
            "or": _safe_round(mh_or),
            "correction": "haldane_0.5",
            "note": "Primary OR=44.8 (non-stratified); MH OR is supplementary",
            "strata": mh_strata,
        },
        "per_model": per_model,
    }

    out = ANALYSIS_DIR / "mcnemar_matched.json"
    with open(out, "w") as f:
        json.dump(result, f, indent=2, default=str)
    print(f"  -> {out.name}")
    return result


def run_information_delta(df: pd.DataFrame, clauses: list[dict]) -> dict:
    """Dream A10: Per-type information (token count) delta + logistic regression."""
    import statsmodels.api as sm

    clause_map = {}
    for c in clauses:
        cid = c["clause_id"]
        amb_tok = len(c.get("ambiguous_clause", "").split())
        una_tok = len(c.get("unambiguous_clause", "").split())
        clause_map[cid] = {
            "ambiguity_type": c.get("ambiguity_type", "unknown"),
            "amb_tokens": amb_tok,
            "una_tokens": una_tok,
            "token_delta": una_tok - amb_tok,
        }

    # Per-type token delta stats
    type_groups: dict[str, list[int]] = {}
    for info in clause_map.values():
        atype = info["ambiguity_type"]
        type_groups.setdefault(atype, []).append(info["token_delta"])

    type_deltas = {}
    for atype, deltas in sorted(type_groups.items()):
        arr = np.array(deltas)
        type_deltas[atype] = {
            "mean": round(float(arr.mean()), 2),
            "median": round(float(np.median(arr)), 2),
            "std": round(float(arr.std(ddof=1)), 2) if len(arr) > 1 else 0.0,
            "min": int(arr.min()),
            "max": int(arr.max()),
            "n_clauses": len(arr),
        }

    # Merge into judgments
    dfc = df.copy()
    dfc["violated"] = analyze.binarize_violations(dfc).astype(int)
    dfc["token_delta"] = dfc["clause_id"].map(
        lambda cid: clause_map.get(cid, {}).get("token_delta", 0)
    )
    dfc["condition_amb"] = (dfc["condition"] == "ambiguous").astype(int)

    # Logistic regression: violation ~ condition + type + token_delta + model
    type_dummies = pd.get_dummies(
        dfc["ambiguity_type"], prefix="type", drop_first=True, dtype=float
    )
    model_dummies = pd.get_dummies(
        dfc["model"], prefix="model", drop_first=True, dtype=float
    )
    X = pd.concat(
        [dfc[["condition_amb", "token_delta"]].astype(float), type_dummies, model_dummies],
        axis=1,
    )
    X = sm.add_constant(X)
    y = dfc["violated"]

    logit_result: dict = {}
    try:
        fit = sm.Logit(y, X).fit(disp=0, maxiter=100)
        coefficients = {}
        ci = fit.conf_int()
        for var in fit.params.index:
            coefficients[var] = {
                "coef": round(float(fit.params[var]), 4),
                "se": round(float(fit.bse[var]), 4),
                "z": round(float(fit.tvalues[var]), 4),
                "p": round(float(fit.pvalues[var]), 6),
                "ci_lower": round(float(ci.loc[var, 0]), 4),
                "ci_upper": round(float(ci.loc[var, 1]), 4),
            }
        logit_result = {
            "converged": bool(fit.mle_retvals.get("converged", False)),
            "n_obs": int(fit.nobs),
            "pseudo_r2": round(float(fit.prsquared), 4),
            "llr_p": round(float(fit.llr_pvalue), 6),
            "coefficients": coefficients,
        }
    except Exception as e:
        logit_result = {"error": str(e)}

    result = {
        "per_type_token_delta": type_deltas,
        "logistic_regression": logit_result,
    }

    out = ANALYSIS_DIR / "information_delta.json"
    with open(out, "w") as f:
        json.dump(result, f, indent=2, default=str)
    print(f"  -> {out.name}")
    return result


def run_fleiss_kappa(df: pd.DataFrame, clauses: list[dict]) -> dict:
    """Fleiss' kappa for inter-model agreement on violation judgment."""
    amb = df[df["condition"] == "ambiguous"].copy()
    if amb.empty:
        result = {"error": "No ambiguous episodes"}
        out = ANALYSIS_DIR / "fleiss_kappa.json"
        with open(out, "w") as f:
            json.dump(result, f, indent=2)
        print(f"  -> {out.name}")
        return result

    amb["violated"] = analyze.binarize_violations(amb).astype(int)
    models = sorted(amb["model"].unique())
    n_models = len(models)

    if n_models < 2:
        result = {"error": f"Need >= 2 models, found {n_models}", "models": models}
        out = ANALYSIS_DIR / "fleiss_kappa.json"
        with open(out, "w") as f:
            json.dump(result, f, indent=2)
        print(f"  -> {out.name}")
        return result

    ratings = amb.groupby("clause_id").agg(
        n_violated=("violated", "sum"),
        n_raters=("violated", "count"),
    ).reset_index()
    ratings = ratings[ratings["n_raters"] >= 2]

    if ratings.empty:
        result = {"error": "No clauses with >= 2 model ratings"}
        out = ANALYSIS_DIR / "fleiss_kappa.json"
        with open(out, "w") as f:
            json.dump(result, f, indent=2)
        print(f"  -> {out.name}")
        return result

    ratings["n_not"] = ratings["n_raters"] - ratings["n_violated"]
    N = len(ratings)
    mat = ratings[["n_violated", "n_not"]].values  # (N, 2)
    n_arr = ratings["n_raters"].values

    # Per-subject agreement P_i
    P_i = np.zeros(N)
    for i in range(N):
        ni = n_arr[i]
        if ni >= 2:
            P_i[i] = (np.sum(mat[i] ** 2) - ni) / (ni * (ni - 1))
    P_bar = float(P_i.mean())

    total_ratings = n_arr.sum()
    p_j = mat.sum(axis=0) / total_ratings  # (2,)
    P_e = float(np.sum(p_j ** 2))

    kappa = (P_bar - P_e) / (1 - P_e) if P_e < 1.0 else 0.0

    # SE (large sample, Fleiss 1971)
    n_fixed = int(np.median(n_arr))
    if N > 1 and P_e < 1.0 and n_fixed >= 2:
        inner = (
            P_e
            - (2 * n_fixed - 3) * P_e ** 2
            + 2 * (n_fixed - 2) * np.sum(p_j ** 3)
        )
        se = float(np.sqrt(2 / (N * n_fixed * (n_fixed - 1))) * np.sqrt(
            abs(inner) / (1 - P_e) ** 2
        ))
        z_val = kappa / se if se > 0 else float("nan")
        p_val = float(2 * (1 - stats.norm.cdf(abs(z_val)))) if np.isfinite(z_val) else float("nan")
    else:
        se = z_val = p_val = float("nan")

    if kappa < 0:
        interp = "less than chance agreement"
    elif kappa < 0.20:
        interp = "slight agreement"
    elif kappa < 0.40:
        interp = "fair agreement"
    elif kappa < 0.60:
        interp = "moderate agreement"
    elif kappa < 0.80:
        interp = "substantial agreement"
    else:
        interp = "almost perfect agreement"

    result = {
        "n_clauses": N,
        "n_models": n_models,
        "models": models,
        "n_raters_per_clause": {
            "min": int(n_arr.min()),
            "max": int(n_arr.max()),
            "mean": round(float(n_arr.mean()), 1),
        },
        "category_proportions": {
            "violated": round(float(p_j[0]), 4),
            "not_violated": round(float(p_j[1]), 4),
        },
        "fleiss_kappa": round(float(kappa), 4),
        "se": round(float(se), 4) if np.isfinite(se) else None,
        "z": round(float(z_val), 4) if np.isfinite(z_val) else None,
        "p": round(float(p_val), 6) if np.isfinite(p_val) else None,
        "interpretation": interp,
    }

    out = ANALYSIS_DIR / "fleiss_kappa.json"
    with open(out, "w") as f:
        json.dump(result, f, indent=2, default=str)
    print(f"  -> {out.name}")
    return result


def run_layer_effect_test(df: pd.DataFrame, clauses: list[dict]) -> dict:
    """C3: Formal test of specification-layer vs linguistic-layer violation rates."""
    SPEC_TYPES = {"incompleteness", "conditional_precedence", "authorization_scope"}
    LING_TYPES = {"scopal", "lexical", "coreferential"}

    dfc = df.copy()
    dfc["violated"] = analyze.binarize_violations(dfc)

    # Filter to ambiguous condition only
    amb = dfc[dfc["condition"] == "ambiguous"].copy()
    amb["layer"] = amb["ambiguity_type"].map(
        lambda t: "specification" if t in SPEC_TYPES else "linguistic" if t in LING_TYPES else "unknown"
    )
    amb = amb[amb["layer"] != "unknown"]

    spec = amb[amb["layer"] == "specification"]
    ling = amb[amb["layer"] == "linguistic"]

    spec_n = len(spec)
    spec_v = int(spec["violated"].sum())
    ling_n = len(ling)
    ling_v = int(ling["violated"].sum())

    spec_rate = spec_v / spec_n if spec_n > 0 else 0
    ling_rate = ling_v / ling_n if ling_n > 0 else 0
    delta_pp = (spec_rate - ling_rate) * 100

    from scipy.stats import chi2_contingency
    table = np.array([
        [spec_v, spec_n - spec_v],
        [ling_v, ling_n - ling_v],
    ])
    chi2, p_val, dof, expected = chi2_contingency(table, correction=False)

    n_total = spec_n + ling_n
    cramers_v = np.sqrt(chi2 / n_total) if n_total > 0 else 0

    a, b = spec_v, spec_n - spec_v
    c, d = ling_v, ling_n - ling_v
    if b > 0 and c > 0 and d > 0 and a > 0:
        or_val = (a * d) / (b * c)
        log_or = np.log(or_val)
        se_log = np.sqrt(1/a + 1/b + 1/c + 1/d)
        or_lo = float(np.exp(log_or - 1.96 * se_log))
        or_hi = float(np.exp(log_or + 1.96 * se_log))
    else:
        or_val = or_lo = or_hi = float("nan")

    np.random.seed(42)
    n_boot = 10000
    spec_arr = spec["violated"].values.astype(float)
    ling_arr = ling["violated"].values.astype(float)
    boot_deltas = []
    for _ in range(n_boot):
        s_idx = np.random.randint(0, len(spec_arr), len(spec_arr))
        l_idx = np.random.randint(0, len(ling_arr), len(ling_arr))
        boot_deltas.append((spec_arr[s_idx].mean() - ling_arr[l_idx].mean()) * 100)
    boot_deltas = np.array(boot_deltas)
    ci_lo = float(np.percentile(boot_deltas, 2.5))
    ci_hi = float(np.percentile(boot_deltas, 97.5))

    per_type = {}
    for atype in list(SPEC_TYPES) + list(LING_TYPES):
        subset = amb[amb["ambiguity_type"] == atype]
        if len(subset) > 0:
            rate = float(subset["violated"].mean())
            per_type[atype] = {
                "n": len(subset),
                "violations": int(subset["violated"].sum()),
                "rate": round(rate * 100, 2),
                "layer": "specification" if atype in SPEC_TYPES else "linguistic",
            }

    result = {
        "test": "layer_effect (C3)",
        "specification_layer": {
            "types": sorted(SPEC_TYPES),
            "n": spec_n,
            "violations": spec_v,
            "rate_pct": round(spec_rate * 100, 2),
        },
        "linguistic_layer": {
            "types": sorted(LING_TYPES),
            "n": ling_n,
            "violations": ling_v,
            "rate_pct": round(ling_rate * 100, 2),
        },
        "delta_pp": round(delta_pp, 2),
        "bootstrap_ci_95": [round(ci_lo, 2), round(ci_hi, 2)],
        "chi_squared": {
            "statistic": round(float(chi2), 4),
            "df": int(dof),
            "p": round(float(p_val), 6),
        },
        "cramers_v": round(float(cramers_v), 4),
        "odds_ratio": {
            "or": round(float(or_val), 4) if np.isfinite(or_val) else str(or_val),
            "ci_95": [round(or_lo, 4) if np.isfinite(or_lo) else str(or_lo),
                       round(or_hi, 4) if np.isfinite(or_hi) else str(or_hi)],
        },
        "per_type_detail": per_type,
    }

    out = ANALYSIS_DIR / "layer_effect_test.json"
    with open(out, "w") as f:
        json.dump(result, f, indent=2, default=str)
    print(f"  -> {out.name}")
    return result


def run_phase3(models: list[str]):
    """Load all judgments and run the full analysis suite."""
    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)

    df = _load_all_judgments(models)
    if df.empty:
        print("No judgments found. Run Phase 2 first.")
        return

    print(f"Loaded {len(df)} judgments ({df['model'].nunique()} models, "
          f"{df['ambiguity_type'].nunique()} types)")

    binary = _binary_effect(df)
    type_eff = _type_effect(df)
    model_eff = _model_effect(df)
    interact = _interaction(df)

    # JSON report
    report = {
        "binary_effect": binary,
        "type_effect": type_eff,
        "model_effect": model_eff,
        "model_type_interaction": interact,
        "n_judgments": len(df),
    }
    with open(ANALYSIS_DIR / "full_statistics.json", "w") as f:
        json.dump(report, f, indent=2, default=str)

    # Per-clause summary CSV
    summary = analyze.per_clause_summary(df)
    summary.to_csv(ANALYSIS_DIR / "per_clause_summary.csv", index=False)

    # Aggregated rates CSV
    dfc = df.copy()
    dfc["violated"] = analyze.binarize_violations(dfc)
    agg = dfc.groupby(
        ["model", "ambiguity_type", "condition"]
    )["violated"].agg(
        violation_rate="mean", n_violations="sum", n_total="count",
    ).reset_index()
    agg.to_csv(ANALYSIS_DIR / "aggregated_rates.csv", index=False)

    _print_full_report(binary, type_eff, model_eff, interact)

    # Extended analyses (Dream reviewer)
    clauses_path = config.ARTIFACTS_DIR / "clause_templates_full.json"
    if clauses_path.exists():
        with open(clauses_path) as f:
            raw = json.load(f)
        clauses_data = raw if isinstance(raw, list) else raw.get("clauses", raw)
    else:
        clauses_data = []

    print("\n-- Extended analyses (Dream reviewer) --\n")
    run_power_analysis(df, clauses_data)
    run_tost_equivalence(df, clauses_data)
    run_bootstrap_ci(df, clauses_data)
    run_mcnemar_matched(df, clauses_data)
    if clauses_data:
        run_information_delta(df, clauses_data)
    else:
        print("  (skipped information_delta -- no clauses file)")
    run_fleiss_kappa(df, clauses_data)
    run_layer_effect_test(df, clauses_data)

    print(f"\nOutputs in {ANALYSIS_DIR}/:")
    print("  - full_statistics.json")
    print("  - per_clause_summary.csv")
    print("  - aggregated_rates.csv")
    print("  - power_analysis.json")
    print("  - tost_equivalence.json")
    print("  - bootstrap_ci.json")
    print("  - mcnemar_matched.json")
    if clauses_data:
        print("  - information_delta.json")
    print("  - fleiss_kappa.json")
    print("  - layer_effect_test.json")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Full study execution for policy ambiguity safety experiment.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Examples:
  python run_full_study.py --phase 1 --clauses clause_templates_full.json
  python run_full_study.py --phase 2 --resume
  python run_full_study.py --phase 3
  python run_full_study.py --all --clauses clause_templates_full.json
""",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--phase", type=int, choices=[1, 2, 3],
        help="Run a specific phase (1=episodes, 2=judge, 3=analysis).",
    )
    group.add_argument(
        "--all", action="store_true",
        help="Run all 3 phases sequentially.",
    )
    parser.add_argument(
        "--clauses",
        default=str(config.ARTIFACTS_DIR / "clause_templates_full.json"),
        help="Path to clauses JSON (default: clause_templates_full.json).",
    )
    parser.add_argument(
        "--models", default=",".join(DEFAULT_MODELS),
        help=f"Comma-separated model names (default: {','.join(DEFAULT_MODELS)}).",
    )
    parser.add_argument(
        "--concurrency", type=int, default=config.DEFAULT_CONCURRENCY,
        help=f"Max concurrent API calls (default: {config.DEFAULT_CONCURRENCY}).",
    )
    parser.add_argument(
        "--resume", action="store_true", default=True,
        help="Skip completed episodes/judgments (default: True).",
    )
    parser.add_argument(
        "--no-resume", action="store_false", dest="resume",
        help="Re-run everything from scratch.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None):
    args = parse_args(argv)
    models = [m.strip() for m in args.models.split(",")]
    for m in models:
        if m not in config.MODELS:
            print(f"Error: unknown model '{m}'. Available: {list(config.MODELS.keys())}")
            sys.exit(1)

    clauses = harness.load_clauses(args.clauses)
    phases = [1, 2, 3] if args.all else [args.phase]

    for phase in phases:
        print(f"\n{'=' * 40} Phase {phase} {'=' * 40}\n")
        if phase == 1:
            asyncio.run(run_phase1(clauses, models, args.concurrency, args.resume))
        elif phase == 2:
            asyncio.run(run_phase2(clauses, models, args.concurrency, args.resume))
        elif phase == 3:
            run_phase3(models)


if __name__ == "__main__":
    main()
