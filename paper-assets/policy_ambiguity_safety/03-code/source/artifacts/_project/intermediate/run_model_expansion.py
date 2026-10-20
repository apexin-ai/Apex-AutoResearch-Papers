#!/usr/bin/env python3
"""Model expansion experiment: replicate matched-pair study on new model families.

Selected models (probed 2026-05-21):
  - google/gemini-2.5-flash  (Google family, tool calling confirmed)
  - meta-llama/llama-4-scout (Meta family, tool calling confirmed)

Pipeline mirrors run_full_study.py: Phase 1 (episodes) → Phase 2 (judge) → analysis.
Judge: gpt-5.4 (consistent with Claude/Qwen3 experiments).
"""

import argparse
import asyncio
import json
import os
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

# -- Bootstrap API key before importing config --
sys.path.insert(0, "/home/ubuntu/agent-ml-research")
from core.crypto import load_secret

key = load_secret(Path(
    "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
    "/config/secrets/policy_ambiguity_safety/openrouter_api_key.enc"
))
os.environ["OPENROUTER_API_KEY"] = key

import config
import harness
import judge
import analyze

# ---------------------------------------------------------------------------
# Register new models
# ---------------------------------------------------------------------------

EXPANSION_MODELS = {
    "gemini-2.5-flash": {
        "model_id": "google/gemini-2.5-flash",
        "max_tokens": 4096,
        "api_key_env": config.API_KEY_ENV,
        "base_url": config.OPENROUTER_BASE_URL,
    },
    "llama-4-scout": {
        "model_id": "meta-llama/llama-4-scout",
        "max_tokens": 4096,
        "api_key_env": config.API_KEY_ENV,
        "base_url": config.OPENROUTER_BASE_URL,
    },
}

JUDGE_MODEL = "gpt-5.4"

for name, cfg in EXPANSION_MODELS.items():
    config.MODELS[name] = cfg
    config.CROSS_JUDGE_MAP[name] = JUDGE_MODEL

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

BASE_DIR = config.ARTIFACTS_DIR / "model_expansion"
CLAUSES_PATH = config.ARTIFACTS_DIR / "_project" / "data" / "clause_templates_full.json"
ERRORS_FILE = BASE_DIR / "errors.jsonl"

CONCURRENCY = 5
JUDGE_CONCURRENCY = 5

# ---------------------------------------------------------------------------
# Phase 1: Episode Generation
# ---------------------------------------------------------------------------

def _load_completed_episodes(episodes_file: Path) -> set[str]:
    completed = set()
    if episodes_file.exists():
        with open(episodes_file) as f:
            for line in f:
                if line.strip():
                    rec = json.loads(line)
                    completed.add(f"{rec['clause_id']}|{rec['condition']}")
    return completed


async def run_phase1(clauses: list[dict], model_name: str, resume: bool):
    model_dir = BASE_DIR / model_name
    model_dir.mkdir(parents=True, exist_ok=True)
    episodes_file = model_dir / "episodes.jsonl"

    completed = _load_completed_episodes(episodes_file) if resume else set()
    tasks = []
    for clause in clauses:
        for condition in ("ambiguous", "unambiguous"):
            key = f"{clause['clause_id']}|{condition}"
            if key in completed:
                continue
            tasks.append((clause, condition))

    if not tasks:
        print(f"[{model_name}] All {len(completed)} episodes complete — skipping Phase 1.")
        return

    print(f"[{model_name}] Phase 1: {len(tasks)} episodes to run "
          f"(skipping {len(completed)}, concurrency={CONCURRENCY})")

    semaphore = asyncio.Semaphore(CONCURRENCY)
    lock = asyncio.Lock()
    done = 0
    errors = 0
    t0 = time.time()

    async def _run_one(clause, condition):
        nonlocal done, errors
        for attempt in range(3):
            async with semaphore:
                try:
                    result = await harness.run_episode(clause, condition, model_name)
                    async with lock:
                        with open(episodes_file, "a") as f:
                            f.write(json.dumps(result, ensure_ascii=False) + "\n")
                        done += 1
                        if done % 100 == 0 or done == len(tasks):
                            elapsed = time.time() - t0
                            rate = done / elapsed * 60
                            print(f"  [{model_name}] {done}/{len(tasks)} "
                                  f"({elapsed:.0f}s, {rate:.1f}/min)")
                    return
                except Exception as e:
                    if attempt < 2:
                        await asyncio.sleep(2 ** attempt)
                        continue
                    async with lock:
                        errors += 1
                        with open(ERRORS_FILE, "a") as f:
                            f.write(json.dumps({
                                "phase": 1, "model": model_name,
                                "clause_id": clause["clause_id"],
                                "condition": condition,
                                "error": str(e),
                                "timestamp": time.time(),
                            }, ensure_ascii=False) + "\n")

    await asyncio.gather(*[_run_one(c, cond) for c, cond in tasks])
    elapsed = time.time() - t0
    print(f"  [{model_name}] Phase 1 done: {done} ok, {errors} errors ({elapsed:.0f}s)")


# ---------------------------------------------------------------------------
# Integrity check between phases
# ---------------------------------------------------------------------------

def check_integrity(model_name: str, n_clauses: int) -> tuple[int, int, int]:
    episodes_file = BASE_DIR / model_name / "episodes.jsonl"
    if not episodes_file.exists():
        return 0, 0, 0
    total = 0
    ok = 0
    error_count = 0
    with open(episodes_file) as f:
        for line in f:
            if not line.strip():
                continue
            total += 1
            rec = json.loads(line)
            status = harness.validate_episode(rec)
            if status == "ok":
                ok += 1
            else:
                error_count += 1
    expected = n_clauses * 2
    print(f"  [{model_name}] Integrity: {total}/{expected} episodes "
          f"({ok} ok, {error_count} errors)")
    return total, ok, error_count


# ---------------------------------------------------------------------------
# Phase 2: Judge Evaluation
# ---------------------------------------------------------------------------

def _load_judged_ids(judgments_file: Path) -> set[str]:
    judged = set()
    if judgments_file.exists():
        with open(judgments_file) as f:
            for line in f:
                if line.strip():
                    judged.add(json.loads(line)["episode_id"])
    return judged


async def run_phase2(clauses: list[dict], model_name: str, resume: bool):
    model_dir = BASE_DIR / model_name
    episodes_file = model_dir / "episodes.jsonl"
    if not episodes_file.exists():
        print(f"[{model_name}] No episodes — run Phase 1 first.")
        return

    episodes = []
    with open(episodes_file) as f:
        for line in f:
            if line.strip():
                episodes.append(json.loads(line))
    if not episodes:
        print(f"[{model_name}] No episodes found.")
        return

    clause_index = judge.build_clause_index(clauses)
    judgments_file = model_dir / "judgments.jsonl"
    judged_ids = _load_judged_ids(judgments_file) if resume else set()
    pending = [ep for ep in episodes if ep["episode_id"] not in judged_ids]

    if not pending:
        print(f"[{model_name}] All {len(episodes)} episodes already judged — skipping Phase 2.")
        return

    actual_judge = config.CROSS_JUDGE_MAP[model_name]
    print(f"[{model_name}] Phase 2: judging {len(pending)} episodes "
          f"(judge={actual_judge}, concurrency={JUDGE_CONCURRENCY})")

    semaphore = asyncio.Semaphore(JUDGE_CONCURRENCY)
    lock = asyncio.Lock()
    done = 0
    errors = 0
    t0 = time.time()

    async def _judge_one(episode):
        nonlocal done, errors
        for attempt in range(3):
            async with semaphore:
                try:
                    result = await judge.judge_episode(episode, clause_index)
                    async with lock:
                        with open(judgments_file, "a") as f:
                            f.write(json.dumps(result, ensure_ascii=False) + "\n")
                        done += 1
                        if done % 100 == 0 or done == len(pending):
                            elapsed = time.time() - t0
                            rate = done / elapsed * 60
                            print(f"  [{model_name}] {done}/{len(pending)} judged "
                                  f"({elapsed:.0f}s, {rate:.1f}/min)")
                    return
                except Exception as e:
                    if attempt < 2:
                        await asyncio.sleep(2 ** attempt)
                        continue
                    async with lock:
                        errors += 1
                        with open(ERRORS_FILE, "a") as f:
                            f.write(json.dumps({
                                "phase": 2, "model": model_name,
                                "episode_id": episode.get("episode_id", "?"),
                                "error": str(e),
                                "timestamp": time.time(),
                            }, ensure_ascii=False) + "\n")

    await asyncio.gather(*[_judge_one(ep) for ep in pending])
    elapsed = time.time() - t0
    print(f"  [{model_name}] Phase 2 done: {done} judged, {errors} errors ({elapsed:.0f}s)")


# ---------------------------------------------------------------------------
# Phase 3: Analysis
# ---------------------------------------------------------------------------

def run_analysis(model_name: str) -> dict | None:
    model_dir = BASE_DIR / model_name
    judgments_file = model_dir / "judgments.jsonl"
    if not judgments_file.exists():
        print(f"[{model_name}] No judgments — run Phase 2 first.")
        return None

    records = []
    with open(judgments_file) as f:
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
        print(f"[{model_name}] Empty judgments.")
        return None

    level_order = pd.CategoricalDtype(categories=config.VIOLATION_LEVELS, ordered=True)
    df["violation_level"] = df["violation_level"].astype(level_order)
    df["violated"] = analyze.binarize_violations(df)

    # Overall rates
    amb = df[df["condition"] == "ambiguous"]
    unamb = df[df["condition"] == "unambiguous"]
    amb_rate = float(amb["violated"].mean()) if len(amb) > 0 else None
    unamb_rate = float(unamb["violated"].mean()) if len(unamb) > 0 else None

    # Fisher exact for overall
    ct = pd.crosstab(df["condition"], df["violated"])
    if ct.shape == (2, 2):
        odds_ratio_result = stats.fisher_exact(ct.values)
        or_val = float(odds_ratio_result[0])
        p_val = float(odds_ratio_result[1])
    else:
        or_val = None
        p_val = None

    delta_pp = (amb_rate - unamb_rate) if (amb_rate is not None and unamb_rate is not None) else None

    # Per-type rates
    per_type = {}
    type_amb_rates = {}
    for atype in config.AMBIGUITY_TYPES:
        tdf = df[df["ambiguity_type"] == atype]
        if tdf.empty:
            continue
        t_amb = tdf[tdf["condition"] == "ambiguous"]
        t_unamb = tdf[tdf["condition"] == "unambiguous"]
        a_r = float(t_amb["violated"].mean()) if len(t_amb) > 0 else None
        u_r = float(t_unamb["violated"].mean()) if len(t_unamb) > 0 else None
        d = (a_r - u_r) if (a_r is not None and u_r is not None) else None
        per_type[atype] = {
            "ambiguous_rate": a_r,
            "unambiguous_rate": u_r,
            "delta_pp": d,
        }
        if a_r is not None:
            type_amb_rates[atype] = a_r

    # C1: does binary ambiguity effect replicate?
    c1_replicates = (p_val is not None and p_val < 0.05 and
                     delta_pp is not None and delta_pp > 0)

    # C2: rank correlation with reference ordering
    reference_rank = ["scopal", "lexical", "coreferential",
                      "incompleteness", "conditional_precedence", "authorization_scope"]
    if len(type_amb_rates) >= 4:
        ref_ranks = []
        new_ranks = []
        sorted_new = sorted(type_amb_rates.items(), key=lambda x: -x[1])
        new_rank_map = {t: i for i, (t, _) in enumerate(sorted_new)}
        for i, t in enumerate(reference_rank):
            if t in new_rank_map:
                ref_ranks.append(i)
                new_ranks.append(new_rank_map[t])
        if len(ref_ranks) >= 4:
            rho, rho_p = stats.spearmanr(ref_ranks, new_ranks)
            c2_rank_corr = float(rho)
        else:
            c2_rank_corr = None
    else:
        c2_rank_corr = None

    model_cfg = config.MODELS[model_name]
    result = {
        "model": model_name,
        "model_id": model_cfg["model_id"],
        "n_episodes": len(df),
        "n_ambiguous": len(amb),
        "n_unambiguous": len(unamb),
        "judge_model": JUDGE_MODEL,
        "overall": {
            "ambiguous_rate": amb_rate,
            "unambiguous_rate": unamb_rate,
            "delta_pp": delta_pp,
            "or": or_val,
            "p_value": p_val,
        },
        "per_type": per_type,
        "c1_replicates": c1_replicates,
        "c2_rank_correlation": c2_rank_corr,
        "type_ranking": sorted(type_amb_rates.keys(), key=lambda t: -type_amb_rates[t]),
    }

    analysis_file = model_dir / "analysis.json"
    with open(analysis_file, "w") as f:
        json.dump(result, f, indent=2, default=str)

    _print_analysis(result)
    return result


def _print_analysis(r: dict):
    print(f"\n{'=' * 60}")
    print(f"  Model: {r['model']} ({r['model_id']})")
    print(f"  Episodes: {r['n_episodes']} ({r['n_ambiguous']} amb + {r['n_unambiguous']} unamb)")
    print(f"  Judge: {r['judge_model']}")
    print(f"{'=' * 60}")

    o = r["overall"]
    print(f"\n  Overall: amb={o['ambiguous_rate']:.1%}  unamb={o['unambiguous_rate']:.1%}"
          f"  delta={o['delta_pp']:+.1%}  OR={o['or']:.2f}  p={o['p_value']:.4f}")

    print(f"\n  {'Type':<25} {'Amb':>7} {'Unamb':>7} {'Delta':>7}")
    print(f"  {'-'*25} {'-'*7} {'-'*7} {'-'*7}")
    for atype in config.AMBIGUITY_TYPES:
        if atype in r["per_type"]:
            t = r["per_type"][atype]
            a = f"{t['ambiguous_rate']:.1%}" if t['ambiguous_rate'] is not None else "N/A"
            u = f"{t['unambiguous_rate']:.1%}" if t['unambiguous_rate'] is not None else "N/A"
            d = f"{t['delta_pp']:+.1%}" if t['delta_pp'] is not None else "N/A"
            print(f"  {atype:<25} {a:>7} {u:>7} {d:>7}")

    c1 = "YES" if r["c1_replicates"] else "NO"
    c2 = f"{r['c2_rank_correlation']:.3f}" if r['c2_rank_correlation'] is not None else "N/A"
    print(f"\n  C1 (binary effect replicates): {c1}")
    print(f"  C2 (type rank correlation):    {c2}")
    print(f"  Type ranking: {' > '.join(r['type_ranking'])}")
    print()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Model expansion experiment.")
    parser.add_argument("--phase", type=int, choices=[1, 2, 3],
                        help="Run a specific phase.")
    parser.add_argument("--all", action="store_true",
                        help="Run all phases sequentially.")
    parser.add_argument("--models", default=",".join(EXPANSION_MODELS.keys()),
                        help="Comma-separated model names.")
    parser.add_argument("--resume", action="store_true", default=True)
    parser.add_argument("--no-resume", action="store_false", dest="resume")
    args = parser.parse_args()

    if not args.phase and not args.all:
        args.all = True

    models = [m.strip() for m in args.models.split(",")]
    clauses = harness.load_clauses(str(CLAUSES_PATH))
    print(f"Loaded {len(clauses)} clauses from {CLAUSES_PATH.name}")

    phases = [1, 2, 3] if args.all else [args.phase]

    for model_name in models:
        if model_name not in config.MODELS:
            print(f"Error: unknown model '{model_name}'")
            sys.exit(1)

    for phase in phases:
        print(f"\n{'=' * 40} Phase {phase} {'=' * 40}")
        for model_name in models:
            if phase == 1:
                asyncio.run(run_phase1(clauses, model_name, args.resume))
            elif phase == 2:
                total, ok, errs = check_integrity(model_name, len(clauses))
                if ok < len(clauses):
                    print(f"  [{model_name}] WARNING: only {ok}/{len(clauses)*2} "
                          f"valid episodes. Proceeding with available data.")
                asyncio.run(run_phase2(clauses, model_name, args.resume))
            elif phase == 3:
                run_analysis(model_name)


if __name__ == "__main__":
    main()
