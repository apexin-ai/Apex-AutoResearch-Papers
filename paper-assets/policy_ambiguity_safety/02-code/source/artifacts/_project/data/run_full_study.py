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

DEFAULT_MODELS = ["gpt-5.4", "gpt-4.1"]


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
    if ct.shape == (2, 2):
        chi2, p, _, _ = stats.chi2_contingency(ct.values)
        v = analyze.cramers_v(ct.values)
    else:
        chi2, p, v = float("nan"), float("nan"), 0.0

    # Ambiguous-only subset
    amb = df[df["condition"] == "ambiguous"]
    amb_rates = amb.groupby("model")["violated"].agg(["mean", "sum", "count"])
    amb_rates.columns = ["violation_rate", "n_violations", "n_total"]
    ct_a = pd.crosstab(amb["model"], amb["violated"])
    if ct_a.shape == (2, 2):
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

    print(f"\nOutputs in {ANALYSIS_DIR}/:")
    print("  - full_statistics.json")
    print("  - per_clause_summary.csv")
    print("  - aggregated_rates.csv")


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
