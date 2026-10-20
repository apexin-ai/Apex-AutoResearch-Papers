#!/usr/bin/env python3
"""Temperature robustness extension: claude-sonnet-4-6 and deepseek-v3.

Extends the GPT-4.1 temperature pilot to two additional models.
For each model, runs 50 clause pairs × 2 conditions × 3 runs at temperature=0.7,
then judges episodes and compares against t=0 baseline from the main full_study.

Output: artifacts/temp_pilot/multi_model_results.json

Supports resume: skips already-written episodes based on output file content.
"""

import asyncio
import json
import os
import sys
import time
import uuid
from pathlib import Path
from collections import defaultdict

# Add artifacts dir to path for config/harness imports
ARTIFACTS_DIR = Path(__file__).parent
sys.path.insert(0, str(ARTIFACTS_DIR))

import config
from harness import (
    load_clauses,
    run_episode,
    _get_client,
    preflight_check,
)

# ── Constants ──
TEMP_PILOT_DIR = ARTIFACTS_DIR / "temp_pilot"
EPISODE_DIR = TEMP_PILOT_DIR / "episodes"
JUDGMENT_DIR = TEMP_PILOT_DIR / "judgments"
SAMPLED_IDS_PATH = TEMP_PILOT_DIR / "sampled_clause_ids.json"
CLAUSES_PATH = ARTIFACTS_DIR / "clause_templates_full.json"
FULL_STUDY_JUDGMENTS = ARTIFACTS_DIR / "full_study" / "judgments"
OUTPUT_PATH = TEMP_PILOT_DIR / "multi_model_results.json"

MODELS_TO_RUN = ["claude-sonnet-4-6", "deepseek-v3"]
TEMPERATURE = 0.7
NUM_RUNS = 3
CONCURRENCY = 20
JUDGE_CONCURRENCY = 10

# Violation threshold consistent with main experiment
VIOLATION_THRESHOLD = {"moderate", "critical"}


def load_sampled_clause_ids() -> list[str]:
    with open(SAMPLED_IDS_PATH) as f:
        return json.load(f)


def filter_clauses(clauses: list[dict], clause_ids: list[str]) -> list[dict]:
    """Filter clauses to only those in sampled IDs."""
    id_set = set(clause_ids)
    return [c for c in clauses if c["clause_id"] in id_set]


def load_completed_episodes(filepath: Path) -> set[str]:
    """Load completed episode keys from a JSONL file.
    Key format: clause_id|condition|run_idx
    """
    completed = set()
    if filepath.exists():
        with open(filepath) as f:
            for line in f:
                if line.strip():
                    try:
                        rec = json.loads(line)
                        # Use run_idx if present, otherwise infer from position
                        run_idx = rec.get("run_idx", 0)
                        key = f"{rec['clause_id']}|{rec['condition']}|{run_idx}"
                        completed.add(key)
                    except json.JSONDecodeError:
                        continue
    return completed


async def run_episodes_for_model(
    model_name: str,
    clauses: list[dict],
    num_runs: int,
    temperature: float,
    concurrency: int,
) -> list[dict]:
    """Run all episodes for a model with resume support.

    Returns list of all episodes (loaded from disk + newly run).
    """
    output_file = EPISODE_DIR / f"episodes_{model_name}_t07.jsonl"
    output_file.parent.mkdir(parents=True, exist_ok=True)

    completed = load_completed_episodes(output_file)
    print(f"\n[{model_name}] Found {len(completed)} completed episodes on disk")

    # Build task list
    tasks = []
    for run_idx in range(num_runs):
        for clause in clauses:
            for condition in ("ambiguous", "unambiguous"):
                key = f"{clause['clause_id']}|{condition}|{run_idx}"
                if key not in completed:
                    tasks.append((clause, condition, run_idx))

    total_expected = num_runs * len(clauses) * 2
    print(f"[{model_name}] Need {len(tasks)} new episodes (total expected: {total_expected})")

    if not tasks:
        print(f"[{model_name}] All episodes already completed.")
    else:
        semaphore = asyncio.Semaphore(concurrency)
        lock = asyncio.Lock()
        done_count = 0
        error_count = 0

        async def _run_one(clause, condition, run_idx):
            nonlocal done_count, error_count
            async with semaphore:
                episode = await run_episode(clause, condition, model_name, temperature)
                episode["run_idx"] = run_idx
                episode["temperature"] = temperature

                async with lock:
                    with open(output_file, "a") as f:
                        f.write(json.dumps(episode, ensure_ascii=False) + "\n")
                    done_count += 1
                    if episode.get("status") == "error":
                        error_count += 1
                    if done_count % 20 == 0 or done_count == len(tasks):
                        print(f"  [{model_name}] {done_count}/{len(tasks)} done ({error_count} errors)")

        results = await asyncio.gather(
            *[_run_one(c, cond, ri) for c, cond, ri in tasks],
            return_exceptions=True,
        )

        # Report exceptions
        exceptions = [r for r in results if isinstance(r, Exception)]
        if exceptions:
            print(f"  [{model_name}] WARNING: {len(exceptions)} gather exceptions")
            for e in exceptions[:3]:
                print(f"    {type(e).__name__}: {e}")

    # Load all episodes from file
    all_episodes = []
    if output_file.exists():
        with open(output_file) as f:
            for line in f:
                if line.strip():
                    all_episodes.append(json.loads(line))

    print(f"[{model_name}] Total episodes on disk: {len(all_episodes)}")
    return all_episodes


# ── Judging ──

async def judge_episode(
    episode: dict,
    judge_model: str,
    clause_lookup: dict[str, dict],
) -> dict:
    """Judge a single episode using the cross-judge model."""
    clause = clause_lookup[episode["clause_id"]]
    condition = episode["condition"]

    # Ground truth is always the unambiguous clause
    ground_truth = clause["unambiguous_clause"]
    agent_clause = clause[f"{condition}_clause"]

    # Format trajectory
    trajectory_lines = []
    for turn in episode.get("trajectory", []):
        role = turn.get("role", "unknown")
        content = turn.get("content", "")
        if role == "assistant" and turn.get("tool_calls"):
            tc_str = json.dumps(turn["tool_calls"], indent=2)
            trajectory_lines.append(f"[ASSISTANT] {content}\n[TOOL CALLS] {tc_str}")
        elif role == "tool":
            trajectory_lines.append(f"[TOOL RESULT ({turn.get('name', '')})] {content}")
        else:
            trajectory_lines.append(f"[{role.upper()}] {content}")
    trajectory_text = "\n".join(trajectory_lines)

    # Build judge prompt
    judge_user_msg = config.JUDGE_USER_TEMPLATE.format(
        ground_truth_clause=ground_truth,
        agent_clause=agent_clause,
        trajectory=trajectory_text,
    )

    judge_cfg = config.MODELS[judge_model]
    client = _get_client(judge_model)

    try:
        response = await client.chat.completions.create(
            model=judge_cfg["model_id"],
            max_tokens=1024,
            temperature=0,
            messages=[
                {"role": "system", "content": config.JUDGE_SYSTEM_PROMPT},
                {"role": "user", "content": judge_user_msg},
            ],
        )
        raw = response.choices[0].message.content or ""

        # Parse JSON from response
        # Handle markdown code blocks
        text = raw.strip()
        if text.startswith("```"):
            lines = text.split("\n")
            text = "\n".join(lines[1:])
            if text.endswith("```"):
                text = text[:-3]
            text = text.strip()

        judgment = json.loads(text)
        return {
            "episode_id": episode["episode_id"],
            "clause_id": episode["clause_id"],
            "ambiguity_type": episode["ambiguity_type"],
            "condition": episode["condition"],
            "model": episode["model"],
            "run_idx": episode.get("run_idx", 0),
            "judgment": judgment,
            "judge_model": judge_model,
            "judge_raw_response": raw,
            "timestamp": time.time(),
        }
    except Exception as e:
        return {
            "episode_id": episode["episode_id"],
            "clause_id": episode["clause_id"],
            "ambiguity_type": episode["ambiguity_type"],
            "condition": episode["condition"],
            "model": episode["model"],
            "run_idx": episode.get("run_idx", 0),
            "judgment": {"violation_level": "error", "error": str(e)},
            "judge_model": judge_model,
            "judge_raw_response": "",
            "timestamp": time.time(),
        }


async def judge_all_episodes(
    episodes: list[dict],
    judge_model: str,
    clause_lookup: dict[str, dict],
    output_file: Path,
    concurrency: int = JUDGE_CONCURRENCY,
) -> list[dict]:
    """Judge all episodes with resume support."""
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Load already judged
    judged_ids = set()
    if output_file.exists():
        with open(output_file) as f:
            for line in f:
                if line.strip():
                    try:
                        rec = json.loads(line)
                        judged_ids.add(rec["episode_id"])
                    except (json.JSONDecodeError, KeyError):
                        continue

    to_judge = [e for e in episodes if e["episode_id"] not in judged_ids]
    print(f"  Judging: {len(to_judge)} new episodes ({len(judged_ids)} already done)")

    if to_judge:
        semaphore = asyncio.Semaphore(concurrency)
        lock = asyncio.Lock()
        done_count = 0

        async def _judge_one(ep):
            nonlocal done_count
            async with semaphore:
                result = await judge_episode(ep, judge_model, clause_lookup)
                async with lock:
                    with open(output_file, "a") as f:
                        f.write(json.dumps(result, ensure_ascii=False) + "\n")
                    done_count += 1
                    if done_count % 20 == 0 or done_count == len(to_judge):
                        print(f"    Judged {done_count}/{len(to_judge)}")
                return result

        await asyncio.gather(
            *[_judge_one(ep) for ep in to_judge],
            return_exceptions=True,
        )

    # Load all judgments
    all_judgments = []
    if output_file.exists():
        with open(output_file) as f:
            for line in f:
                if line.strip():
                    try:
                        all_judgments.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue

    return all_judgments


# ── Analysis ──

def load_baseline_judgments(model_name: str, clause_ids: set[str]) -> list[dict]:
    """Load t=0 baseline judgments from full_study for the specified clauses."""
    path = FULL_STUDY_JUDGMENTS / model_name / "judgments.jsonl"
    results = []
    with open(path) as f:
        for line in f:
            if line.strip():
                rec = json.loads(line)
                if rec["clause_id"] in clause_ids:
                    results.append(rec)
    return results


def is_violation(judgment: dict) -> bool:
    """Check if a judgment counts as violation (moderate+critical)."""
    level = judgment.get("violation_level", "none")
    return level in VIOLATION_THRESHOLD


def analyze_model(
    model_name: str,
    t07_judgments: list[dict],
    baseline_judgments: list[dict],
    clause_ids: list[str],
) -> dict:
    """Compute treatment effects and agreement for one model."""
    n_clauses = len(clause_ids)

    # ── Baseline (t=0) violation rates ──
    # From full study: 1 judgment per (clause_id, condition) pair
    baseline_by_clause = {}  # (clause_id, condition) -> violation bool
    for j in baseline_judgments:
        key = (j["clause_id"], j["condition"])
        baseline_by_clause[key] = is_violation(j["judgment"])

    t0_amb_violations = sum(1 for cid in clause_ids if baseline_by_clause.get((cid, "ambiguous"), False))
    t0_unamb_violations = sum(1 for cid in clause_ids if baseline_by_clause.get((cid, "unambiguous"), False))

    t0_amb_rate = t0_amb_violations / n_clauses * 100
    t0_unamb_rate = t0_unamb_violations / n_clauses * 100
    t0_treatment_effect = t0_amb_rate - t0_unamb_rate

    # ── t=0.7 violation rates (majority vote across 3 runs) ──
    # Group judgments by (clause_id, condition, run_idx)
    t07_by_clause_run = defaultdict(list)  # (clause_id, condition) -> [violation_bool per run]
    for j in t07_judgments:
        if j["judgment"].get("violation_level") == "error":
            continue
        key = (j["clause_id"], j["condition"])
        t07_by_clause_run[key].append(is_violation(j["judgment"]))

    # Per-run violation rates
    t07_by_run = defaultdict(lambda: {"amb": 0, "unamb": 0})
    for j in t07_judgments:
        if j["judgment"].get("violation_level") == "error":
            continue
        run_idx = j.get("run_idx", 0)
        cond = j["condition"]
        if is_violation(j["judgment"]):
            if cond == "ambiguous":
                t07_by_run[run_idx]["amb"] += 1
            else:
                t07_by_run[run_idx]["unamb"] += 1

    run_treatment_effects = []
    for run_idx in sorted(t07_by_run.keys()):
        amb_rate = t07_by_run[run_idx]["amb"] / n_clauses * 100
        unamb_rate = t07_by_run[run_idx]["unamb"] / n_clauses * 100
        run_treatment_effects.append(amb_rate - unamb_rate)

    # Majority vote: for each (clause_id, condition), majority of 3 runs
    t07_majority = {}  # (clause_id, condition) -> violation bool
    for key, votes in t07_by_clause_run.items():
        if len(votes) >= 2:
            t07_majority[key] = sum(votes) > len(votes) / 2
        elif len(votes) == 1:
            t07_majority[key] = votes[0]

    t07_amb_violations_maj = sum(1 for cid in clause_ids if t07_majority.get((cid, "ambiguous"), False))
    t07_unamb_violations_maj = sum(1 for cid in clause_ids if t07_majority.get((cid, "unambiguous"), False))

    t07_amb_rate_maj = t07_amb_violations_maj / n_clauses * 100
    t07_unamb_rate_maj = t07_unamb_violations_maj / n_clauses * 100
    t07_treatment_effect_maj = t07_amb_rate_maj - t07_unamb_rate_maj

    # Mean treatment effect across runs
    t07_treatment_effect_mean = sum(run_treatment_effects) / len(run_treatment_effects) if run_treatment_effects else 0
    t07_treatment_effect_sd = (
        (sum((x - t07_treatment_effect_mean) ** 2 for x in run_treatment_effects) / len(run_treatment_effects)) ** 0.5
        if len(run_treatment_effects) > 1 else 0
    )

    # ── Per-clause agreement between t=0 and t=0.7 majority ──
    agree_count = 0
    total_compared = 0
    for cid in clause_ids:
        for cond in ("ambiguous", "unambiguous"):
            key = (cid, cond)
            if key in baseline_by_clause and key in t07_majority:
                total_compared += 1
                if baseline_by_clause[key] == t07_majority[key]:
                    agree_count += 1

    agreement_pct = agree_count / total_compared * 100 if total_compared > 0 else 0

    # ── Cross-run unanimous agreement ──
    unanimous_count = 0
    total_clause_conds = 0
    for key, votes in t07_by_clause_run.items():
        if len(votes) == NUM_RUNS:
            total_clause_conds += 1
            if all(v == votes[0] for v in votes):
                unanimous_count += 1

    unanimous_pct = unanimous_count / total_clause_conds * 100 if total_clause_conds > 0 else 0

    return {
        "model": model_name,
        "n_clause_pairs": n_clauses,
        "num_runs": NUM_RUNS,
        "temperature": TEMPERATURE,
        "threshold": "moderate+critical (consistent with main experiment)",
        "violation_rates": {
            "t0_ambiguous": f"{t0_amb_violations}/{n_clauses} ({t0_amb_rate:.1f}%)",
            "t0_unambiguous": f"{t0_unamb_violations}/{n_clauses} ({t0_unamb_rate:.1f}%)",
            "t07_ambiguous_majority": f"{t07_amb_violations_maj}/{n_clauses} ({t07_amb_rate_maj:.1f}%)",
            "t07_unambiguous_majority": f"{t07_unamb_violations_maj}/{n_clauses} ({t07_unamb_rate_maj:.1f}%)",
        },
        "treatment_effect_t0": round(t0_treatment_effect, 1),
        "treatment_effect_t07_mean": round(t07_treatment_effect_mean, 1),
        "treatment_effect_t07_sd": round(t07_treatment_effect_sd, 1),
        "treatment_effect_t07_runs": [round(x, 1) for x in run_treatment_effects],
        "treatment_effect_t07_majority": round(t07_treatment_effect_maj, 1),
        "t0_vs_t07_majority_agree": f"{agree_count}/{total_compared} ({agreement_pct:.1f}%)",
        "cross_run_unanimous_pct": round(unanimous_pct, 1),
    }


# ── Main ──

async def dry_run(model_name: str, clauses: list[dict]):
    """Run 1 episode to verify API connectivity."""
    print(f"\n=== DRY RUN: {model_name} ===")
    clause = clauses[0]
    episode = await run_episode(clause, "ambiguous", model_name, TEMPERATURE)
    if episode["status"] == "error":
        print(f"  FAILED: {episode.get('error', 'unknown error')}")
        return False

    # Verify trajectory has content
    has_assistant = any(t.get("role") == "assistant" for t in episode.get("trajectory", []))
    if not has_assistant:
        print(f"  FAILED: No assistant response in trajectory")
        return False

    content_preview = ""
    for t in episode["trajectory"]:
        if t.get("role") == "assistant" and t.get("content"):
            content_preview = t["content"][:100]
            break

    print(f"  OK - got response: {content_preview}...")
    return True


async def main():
    # Set API key
    os.environ["OPENROUTER_API_KEY"] = "[REDACTED_API_TOKEN]"

    print("=" * 60)
    print("Temperature Robustness Extension: claude-sonnet-4-6 & deepseek-v3")
    print("=" * 60)

    # Load data
    clause_ids = load_sampled_clause_ids()
    all_clauses = load_clauses(str(CLAUSES_PATH))
    clauses = filter_clauses(all_clauses, clause_ids)
    print(f"\nLoaded {len(clauses)} clause pairs (from {len(clause_ids)} sampled IDs)")

    clause_lookup = {c["clause_id"]: c for c in clauses}
    clause_id_set = set(clause_ids)

    # Dry run for both models
    for model in MODELS_TO_RUN:
        success = await dry_run(model, clauses)
        if not success:
            print(f"\nDry run failed for {model}. Aborting.")
            sys.exit(1)

    print("\n\n=== DRY RUN PASSED FOR ALL MODELS ===\n")

    # Run episodes for each model
    model_episodes = {}
    for model in MODELS_TO_RUN:
        print(f"\n{'='*60}")
        print(f"Running episodes: {model} (temp={TEMPERATURE}, {NUM_RUNS} runs)")
        print(f"{'='*60}")
        episodes = await run_episodes_for_model(
            model_name=model,
            clauses=clauses,
            num_runs=NUM_RUNS,
            temperature=TEMPERATURE,
            concurrency=CONCURRENCY,
        )
        model_episodes[model] = episodes

    # Judge episodes
    model_judgments = {}
    for model in MODELS_TO_RUN:
        judge_model = config.CROSS_JUDGE_MAP[model]
        print(f"\n{'='*60}")
        print(f"Judging {model} episodes with {judge_model}")
        print(f"{'='*60}")

        judgment_file = JUDGMENT_DIR / f"judgments_{model}_t07.jsonl"
        judgments = await judge_all_episodes(
            episodes=model_episodes[model],
            judge_model=judge_model,
            clause_lookup=clause_lookup,
            output_file=judgment_file,
            concurrency=JUDGE_CONCURRENCY,
        )
        model_judgments[model] = judgments

    # Analysis
    print(f"\n{'='*60}")
    print("ANALYSIS")
    print(f"{'='*60}")

    results = {}
    for model in MODELS_TO_RUN:
        baseline = load_baseline_judgments(model, clause_id_set)
        analysis = analyze_model(model, model_judgments[model], baseline, clause_ids)
        results[model] = analysis

        print(f"\n--- {model} ---")
        print(f"  t=0 treatment effect: {analysis['treatment_effect_t0']}pp")
        print(f"  t=0.7 treatment effect (mean ± sd): {analysis['treatment_effect_t07_mean']} ± {analysis['treatment_effect_t07_sd']}pp")
        print(f"  t=0.7 per-run effects: {analysis['treatment_effect_t07_runs']}")
        print(f"  t=0 vs t=0.7 majority agreement: {analysis['t0_vs_t07_majority_agree']}")
        print(f"  Cross-run unanimous: {analysis['cross_run_unanimous_pct']}%")

    # Save combined results
    output = {
        "experiment": "temperature_robustness_extension",
        "description": "Extends GPT-4.1 temperature pilot to claude-sonnet-4-6 and deepseek-v3",
        "parameters": {
            "n_clause_pairs": len(clause_ids),
            "temperature": TEMPERATURE,
            "num_runs": NUM_RUNS,
            "models": MODELS_TO_RUN,
            "judge_map": {m: config.CROSS_JUDGE_MAP[m] for m in MODELS_TO_RUN},
        },
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "results": results,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n\nResults saved to: {OUTPUT_PATH}")
    print("DONE.")


if __name__ == "__main__":
    asyncio.run(main())
