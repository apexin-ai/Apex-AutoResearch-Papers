#!/usr/bin/env python3
"""Plan 006: Reliability Test — API models (gpt-5.4 + gpt-4.1)

30 representative clauses × 2 conditions × 2 models × 3 replicates = 360 episodes.
Each replicate is an independent API call (no cache reuse).
Computes ICC(2,1) to assess experiment reproducibility.

Steps:
  1. Select 30 representative clauses from plan_002 judgments
  2. Run 360 episodes with independent replicates
  3. Cross-judge all episodes (gpt-5.4 ↔ gpt-4.1)
  4. Compute ICC(2,1) — overall, per-type, per-model, binary
  5. Validate and print summary
"""

import asyncio
import json
import os
import random
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.stats import f as f_dist

import config
import harness
import judge


def _load_api_key():
    if os.environ.get("OPENROUTER_API_KEY"):
        return
    try:
        sys.path.insert(0, "/home/ubuntu/agent-ml-research")
        from core.crypto import load_secret
        key = load_secret(Path(
            "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
            "/config/secrets/policy_ambiguity_safety/openrouter_api_key.enc"
        ))
        if key:
            os.environ["OPENROUTER_API_KEY"] = key
            return
    except Exception:
        pass
    raise RuntimeError("OPENROUTER_API_KEY not found")

# ── Paths ──
PLAN_DIR = config.ARTIFACTS_DIR / "plan_006"
EPISODES_FILE = PLAN_DIR / "episodes_api.jsonl"
JUDGMENTS_FILE = PLAN_DIR / "judgments_api.jsonl"
SELECTED_FILE = PLAN_DIR / "selected_clauses.json"
ICC_FILE = PLAN_DIR / "icc_results.json"

# ── Parameters ──
MODELS = ["gpt-5.4", "gpt-4.1"]
N_REPLICATES = 3
CONCURRENCY = 10
JUDGE_CONCURRENCY = 5
ERROR_RATE_THRESHOLD = 0.05

VIOLATION_NUMERIC = {"none": 0, "minor": 1, "moderate": 2, "critical": 3}


# ═══════════════════════════════════════════════════════════════════════════════
# Step 1: Select 30 representative clauses
# ═══════════════════════════════════════════════════════════════════════════════

def select_clauses() -> list[dict]:
    """Pick 5 clauses per ambiguity type based on violation-rate distribution.

    Per type: highest, lowest, median violation rate + 2 random (seed=42).
    Violation rate = fraction of (moderate + critical) in ambiguous condition,
    pooled across both API models from plan_002 judgments.
    """
    judgments: list[dict] = []
    for model_dir in MODELS:
        jpath = (
            config.ARTIFACTS_DIR
            / "full_study"
            / "judgments"
            / model_dir
            / "judgments.jsonl"
        )
        with open(jpath) as f:
            for line in f:
                if line.strip():
                    judgments.append(json.loads(line))

    clause_stats: dict[str, dict] = defaultdict(
        lambda: {"violations": 0, "total": 0, "ambiguity_type": ""}
    )
    for j in judgments:
        if j["condition"] != "ambiguous":
            continue
        cid = j["clause_id"]
        clause_stats[cid]["total"] += 1
        clause_stats[cid]["ambiguity_type"] = j["ambiguity_type"]
        if j["judgment"]["violation_level"] in ("moderate", "critical"):
            clause_stats[cid]["violations"] += 1

    clause_rates: dict[str, dict] = {}
    for cid, s in clause_stats.items():
        if s["total"] > 0:
            clause_rates[cid] = {
                "violation_rate": s["violations"] / s["total"],
                "ambiguity_type": s["ambiguity_type"],
            }

    type_groups: dict[str, list[tuple[str, float]]] = defaultdict(list)
    for cid, info in clause_rates.items():
        type_groups[info["ambiguity_type"]].append((cid, info["violation_rate"]))

    rng = random.Random(42)
    selected: list[dict] = []

    for atype in config.AMBIGUITY_TYPES:
        group = sorted(type_groups[atype], key=lambda x: (x[1], x[0]))
        n = len(group)
        if n < 5:
            raise ValueError(
                f"Type '{atype}' has only {n} clauses with judgments, need >= 5"
            )

        highest_cid = group[-1][0]
        lowest_cid = group[0][0]
        median_cid = group[n // 2][0]

        chosen: dict[str, str] = {
            highest_cid: "highest_vrate",
            lowest_cid: "lowest_vrate",
            median_cid: "median_vrate",
        }
        remaining = [(cid, r) for cid, r in group if cid not in chosen]
        for cid, _ in rng.sample(remaining, 2):
            chosen[cid] = "random"

        rate_map = dict(group)
        for cid, reason in chosen.items():
            selected.append(
                {
                    "clause_id": cid,
                    "ambiguity_type": atype,
                    "violation_rate": round(rate_map[cid], 4),
                    "selection_reason": reason,
                }
            )

    return sorted(selected, key=lambda x: (x["ambiguity_type"], x["clause_id"]))


# ═══════════════════════════════════════════════════════════════════════════════
# Step 2: Run episodes (3 independent replicates)
# ═══════════════════════════════════════════════════════════════════════════════

def _load_completed_keys(path: Path) -> set[str]:
    keys: set[str] = set()
    if path.exists():
        with open(path) as f:
            for line in f:
                if line.strip():
                    rec = json.loads(line)
                    keys.add(rec.get("episode_key", ""))
    return keys


async def run_episodes(clauses: list[dict], selected_ids: set[str]):
    PLAN_DIR.mkdir(parents=True, exist_ok=True)

    for model in MODELS:
        print(f"  Preflight: {model} ... ", end="", flush=True)
        await harness.preflight_check(model)
        print("OK")

    selected_clauses = [c for c in clauses if c["clause_id"] in selected_ids]
    if len(selected_clauses) != len(selected_ids):
        found = {c["clause_id"] for c in selected_clauses}
        missing = selected_ids - found
        raise ValueError(f"Missing clauses in template file: {missing}")

    completed = _load_completed_keys(EPISODES_FILE)
    tasks: list[tuple] = []
    for clause in selected_clauses:
        for condition in ("ambiguous", "unambiguous"):
            for model in MODELS:
                for rep in range(1, N_REPLICATES + 1):
                    key = f"{clause['clause_id']}|{condition}|{model}|rep{rep}"
                    if key not in completed:
                        tasks.append((clause, condition, model, rep, key))

    if not tasks:
        print("  All episodes already completed.")
        return

    total = len(tasks)
    print(f"  Running {total} episodes (concurrency={CONCURRENCY}) ...")
    semaphore = asyncio.Semaphore(CONCURRENCY)
    lock = asyncio.Lock()
    done = 0
    errors = 0

    async def _run_one(clause, condition, model, rep, key):
        nonlocal done, errors
        async with semaphore:
            episode = await harness.run_episode(clause, condition, model)
            episode["episode_key"] = key
            episode["replicate"] = rep

            status = harness.validate_episode(episode)
            if status != "ok":
                errors += 1

            async with lock:
                with open(EPISODES_FILE, "a") as f:
                    f.write(json.dumps(episode, ensure_ascii=False) + "\n")
                done += 1
                if done % 20 == 0 or done == total:
                    err_rate = errors / done if done else 0
                    print(f"    [{done}/{total}] errors={errors} ({err_rate:.1%})")
                    if err_rate > ERROR_RATE_THRESHOLD and done >= 20:
                        print(
                            f"  FATAL: error rate {err_rate:.1%} > "
                            f"{ERROR_RATE_THRESHOLD:.0%}"
                        )
                        sys.exit(1)

    results = await asyncio.gather(
        *[_run_one(*t) for t in tasks], return_exceptions=True
    )
    exceptions = [r for r in results if isinstance(r, Exception)]
    if exceptions:
        print(f"  WARNING: {len(exceptions)} tasks raised exceptions:")
        for e in exceptions[:5]:
            print(f"    {e}")

    final_err_rate = errors / done if done else 0
    if final_err_rate > ERROR_RATE_THRESHOLD:
        print(f"  FATAL: final error rate {final_err_rate:.1%} exceeds threshold")
        sys.exit(1)

    print(f"  Episodes done: {done} → {EPISODES_FILE}")


# ═══════════════════════════════════════════════════════════════════════════════
# Step 3: Cross-judge
# ═══════════════════════════════════════════════════════════════════════════════

async def run_cross_judge(clauses: list[dict]):
    episodes: list[dict] = []
    with open(EPISODES_FILE) as f:
        for line in f:
            if line.strip():
                ep = json.loads(line)
                if harness.validate_episode(ep) == "ok":
                    episodes.append(ep)

    clause_index = judge.build_clause_index(clauses)

    judged_ids: set[str] = set()
    if JUDGMENTS_FILE.exists():
        with open(JUDGMENTS_FILE) as f:
            for line in f:
                if line.strip():
                    judged_ids.add(json.loads(line)["episode_id"])

    pending = [ep for ep in episodes if ep["episode_id"] not in judged_ids]
    if not pending:
        print("  All episodes already judged.")
        return

    print(f"  Judging {len(pending)} episodes (concurrency={JUDGE_CONCURRENCY}) ...")
    semaphore = asyncio.Semaphore(JUDGE_CONCURRENCY)
    lock = asyncio.Lock()
    done = 0

    async def _judge_one(episode):
        nonlocal done
        async with semaphore:
            result = await judge.judge_episode(episode, clause_index)
            result["episode_key"] = episode.get("episode_key", "")
            result["replicate"] = episode.get("replicate", 0)
            async with lock:
                with open(JUDGMENTS_FILE, "a") as f:
                    f.write(json.dumps(result, ensure_ascii=False) + "\n")
                done += 1
                if done % 20 == 0 or done == len(pending):
                    print(f"    [{done}/{len(pending)}] judged")

    await asyncio.gather(
        *[_judge_one(ep) for ep in pending], return_exceptions=True
    )
    print(f"  Judgments done: {done} → {JUDGMENTS_FILE}")


# ═══════════════════════════════════════════════════════════════════════════════
# Step 4: ICC computation
# ═══════════════════════════════════════════════════════════════════════════════

def _icc_2_1(ratings: np.ndarray):
    """ICC(2,1) two-way random, single measures.

    Parameters
    ----------
    ratings : ndarray of shape (n_subjects, k_raters)

    Returns
    -------
    (icc, ci_lower, ci_upper) — 95 % CI via Shrout & Fleiss (1979) F method.
    Returns (None, None, None) when computation is impossible.
    """
    n, k = ratings.shape
    if n < 2 or k < 2:
        return None, None, None

    grand_mean = np.mean(ratings)
    row_means = np.mean(ratings, axis=1)
    col_means = np.mean(ratings, axis=0)

    SS_total = float(np.sum((ratings - grand_mean) ** 2))
    SS_between = float(k * np.sum((row_means - grand_mean) ** 2))
    SS_raters = float(n * np.sum((col_means - grand_mean) ** 2))
    SS_error = SS_total - SS_between - SS_raters

    df_between = n - 1
    df_error = (n - 1) * (k - 1)

    BMS = SS_between / df_between if df_between > 0 else 0.0
    JMS = SS_raters / (k - 1) if k > 1 else 0.0
    EMS = SS_error / df_error if df_error > 0 else 0.0

    denom = BMS + (k - 1) * EMS + k * (JMS - EMS) / n
    if abs(denom) < 1e-15:
        return None, None, None

    icc = (BMS - EMS) / denom

    # 95 % CI using F-ratio method (Shrout & Fleiss 1979, Table 4 row 2)
    alpha = 0.05
    try:
        if EMS < 1e-15:
            return float(icc), None, None

        F_val = BMS / EMS
        FL = f_dist.ppf(1 - alpha / 2, df_between, df_error)
        FU = f_dist.ppf(alpha / 2, df_between, df_error)

        a = k * (JMS - EMS) / (n * EMS) if EMS > 0 else 0.0

        ci_lower = (F_val / FL - 1) / (F_val / FL + (k - 1) + a)
        ci_upper = (F_val / FU - 1) / (F_val / FU + (k - 1) + a)

        return float(icc), float(ci_lower), float(ci_upper)
    except Exception:
        return float(icc), None, None


def _interpret_icc(icc) -> str:
    if icc is None:
        return "undefined"
    if icc < 0.5:
        return "poor"
    if icc < 0.75:
        return "moderate"
    if icc < 0.9:
        return "good"
    return "excellent"


def _round_or_none(v, decimals=4):
    return round(v, decimals) if v is not None else None


def compute_all_icc() -> dict:
    """Load judgments, build replicate matrix, compute ICC statistics."""
    judgments: list[dict] = []
    with open(JUDGMENTS_FILE) as f:
        for line in f:
            if line.strip():
                judgments.append(json.loads(line))

    # (clause_id, condition, model) → {rep_number: numeric_level}
    replicate_data: dict[tuple, dict[int, int]] = defaultdict(dict)
    clause_type_map: dict[str, str] = {}

    for j in judgments:
        key = (j["clause_id"], j["condition"], j["model"])
        rep = j.get("replicate", 0)
        level = VIOLATION_NUMERIC.get(j["judgment"]["violation_level"], 0)
        replicate_data[key][rep] = level
        clause_type_map[j["clause_id"]] = j["ambiguity_type"]

    # Build matrix — only groups with all 3 replicates
    rows: list[list[float]] = []
    meta: list[dict] = []
    for key in sorted(replicate_data):
        reps = replicate_data[key]
        if len(reps) >= N_REPLICATES and all(i in reps for i in range(1, N_REPLICATES + 1)):
            rows.append([float(reps[i]) for i in range(1, N_REPLICATES + 1)])
            meta.append(
                {"clause_id": key[0], "condition": key[1], "model": key[2]}
            )

    if not rows:
        print("  ERROR: no complete replicate groups found")
        return {}

    matrix = np.array(rows)
    binary_matrix = (matrix >= 2).astype(float)  # moderate+ = 1

    def _icc_block(mat):
        icc, lo, hi = _icc_2_1(mat)
        return {
            "icc_2_1": _round_or_none(icc),
            "ci_95": [_round_or_none(lo), _round_or_none(hi)],
            "interpretation": _interpret_icc(icc),
        }

    # Overall
    overall = _icc_block(matrix)
    binary_overall = _icc_block(binary_matrix)

    # Per-type
    per_type: dict[str, dict] = {}
    for atype in config.AMBIGUITY_TYPES:
        idx = [
            i
            for i, m in enumerate(meta)
            if clause_type_map.get(m["clause_id"]) == atype
        ]
        if len(idx) >= 2:
            blk = _icc_block(matrix[idx])
            blk["n"] = len(idx)
            per_type[atype] = blk

    # Per-model
    per_model: dict[str, dict] = {}
    for model in MODELS:
        idx = [i for i, m in enumerate(meta) if m["model"] == model]
        if len(idx) >= 2:
            blk = _icc_block(matrix[idx])
            blk["n"] = len(idx)
            per_model[model] = blk

    # Per-clause detail
    per_clause_detail: list[dict] = []
    for i, m in enumerate(meta):
        reps = matrix[i].tolist()
        per_clause_detail.append(
            {
                "clause_id": m["clause_id"],
                "type": clause_type_map.get(m["clause_id"], ""),
                "model": m["model"],
                "condition": m["condition"],
                "replicates": [int(r) for r in reps],
                "mean": round(float(np.mean(reps)), 4),
                "std": round(float(np.std(reps, ddof=0)), 4),
                "exact_agreement": len(set(int(r) for r in reps)) == 1,
            }
        )

    results = {
        "n_clauses": len({m["clause_id"] for m in meta}),
        "n_replicates": N_REPLICATES,
        "n_episodes": len(judgments),
        "n_complete_groups": len(rows),
        "overall_icc": overall,
        "binary_icc": binary_overall,
        "per_type": per_type,
        "per_model": per_model,
        "per_clause_detail": sorted(
            per_clause_detail,
            key=lambda x: (x["type"], x["clause_id"], x["model"], x["condition"]),
        ),
    }

    with open(ICC_FILE, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"  ICC results → {ICC_FILE}")
    return results


# ═══════════════════════════════════════════════════════════════════════════════
# Step 5: Validate & summarize
# ═══════════════════════════════════════════════════════════════════════════════

def validate_and_summarize(icc_results: dict):
    n_episodes = 0
    if EPISODES_FILE.exists():
        with open(EPISODES_FILE) as f:
            for line in f:
                if line.strip():
                    n_episodes += 1

    n_judgments = icc_results.get("n_episodes", 0)
    expected = 30 * 2 * len(MODELS) * N_REPLICATES  # 360

    print()
    print("=" * 60)
    print("Plan 006 — Reliability Test Summary")
    print("=" * 60)
    print(f"Episodes:         {n_episodes} / {expected}")
    print(f"Judgments:         {n_judgments} / {expected}")
    print(
        f"Complete groups:  {icc_results['n_complete_groups']} / "
        f"{30 * 2 * len(MODELS)}"
    )
    print()

    ov = icc_results["overall_icc"]
    print(f"Overall ICC(2,1):  {ov['icc_2_1']}")
    if ov["ci_95"][0] is not None:
        print(f"  95% CI:          [{ov['ci_95'][0]}, {ov['ci_95'][1]}]")
    print(f"  Interpretation:  {ov['interpretation']}")
    print()

    bi = icc_results["binary_icc"]
    print(f"Binary ICC(2,1):   {bi['icc_2_1']}")
    if bi["ci_95"][0] is not None:
        print(f"  95% CI:          [{bi['ci_95'][0]}, {bi['ci_95'][1]}]")
    print(f"  Interpretation:  {bi['interpretation']}")
    print()

    print("Per-type ICC:")
    for atype, data in sorted(icc_results["per_type"].items()):
        print(f"  {atype:26s} {data['icc_2_1']}  (n={data['n']}, {data['interpretation']})")
    print()

    print("Per-model ICC:")
    for model, data in sorted(icc_results["per_model"].items()):
        print(f"  {model:26s} {data['icc_2_1']}  (n={data['n']}, {data['interpretation']})")

    details = icc_results["per_clause_detail"]
    exact = sum(1 for d in details if d["exact_agreement"])
    print(
        f"\nExact agreement:  {exact}/{len(details)} "
        f"({exact / len(details) * 100:.1f}%)"
    )
    print("=" * 60)


# ═══════════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════════

async def main():
    _load_api_key()
    PLAN_DIR.mkdir(parents=True, exist_ok=True)

    # Step 1
    print("Step 1: Select 30 representative clauses")
    if SELECTED_FILE.exists():
        with open(SELECTED_FILE) as f:
            selected = json.load(f)
        print(f"  Loaded {len(selected)} clauses from cache")
    else:
        selected = select_clauses()
        with open(SELECTED_FILE, "w") as f:
            json.dump(selected, f, indent=2, ensure_ascii=False)
        print(f"  Saved {len(selected)} clauses → {SELECTED_FILE}")

    selected_ids = {s["clause_id"] for s in selected}
    clauses = harness.load_clauses(
        str(config.ARTIFACTS_DIR / "clause_templates_full.json")
    )

    # Step 2
    print("\nStep 2: Run episodes (3 replicates)")
    await run_episodes(clauses, selected_ids)

    # Step 3
    print("\nStep 3: Cross-judge")
    await run_cross_judge(clauses)

    # Step 4
    print("\nStep 4: Compute ICC")
    icc_results = compute_all_icc()

    # Step 5
    if icc_results:
        print("\nStep 5: Validate")
        validate_and_summarize(icc_results)
    else:
        print("\nStep 5: FAILED — no ICC results")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
