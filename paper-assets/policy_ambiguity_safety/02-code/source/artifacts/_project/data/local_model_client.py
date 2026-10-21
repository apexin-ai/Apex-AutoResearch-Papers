#!/usr/bin/env python3
"""Local model client for Qwen3 via vLLM OpenAI-compatible API.

Runs the same Phase 1 (episodes) + Phase 2 (cross-judge) pipeline as
run_full_study.py, but against locally-served Qwen3 models via vLLM.

Models:
  - qwen3-8b:       http://localhost:8001/v1  (Qwen/Qwen3-8B)
  - qwen3-32b-awq:  http://localhost:8002/v1  (Qwen/Qwen3-32B-AWQ)

Cross-judge: 8B episodes judged by 32B-AWQ, and vice versa.
"""

import argparse
import asyncio
import json
import sys
import time
from pathlib import Path

import openai

import config
import harness
import judge

# ---------------------------------------------------------------------------
# Local model definitions
# ---------------------------------------------------------------------------

LOCAL_MODELS = {
    "qwen3-8b": {
        "model_id": "Qwen/Qwen3-8B",
        "max_tokens": 4096,
        "base_url": "http://localhost:8001/v1",
    },
    "qwen3-32b-awq": {
        "model_id": "Qwen/Qwen3-32B-AWQ",
        "max_tokens": 4096,
        "base_url": "http://localhost:8002/v1",
    },
}

LOCAL_CROSS_JUDGE_MAP = {
    "qwen3-8b": "qwen3-32b-awq",
    "qwen3-32b-awq": "qwen3-8b",
}

# ---------------------------------------------------------------------------
# Client management
# ---------------------------------------------------------------------------

_local_clients: dict[str, openai.AsyncOpenAI] = {}


def get_local_client(model_name: str) -> openai.AsyncOpenAI:
    if model_name not in _local_clients:
        cfg = LOCAL_MODELS[model_name]
        _local_clients[model_name] = openai.AsyncOpenAI(
            api_key="[REDACTED]",
            base_url=cfg["base_url"],
        )
    return _local_clients[model_name]


def _inject_model(model_name: str):
    """Inject local model config into config.MODELS and set harness/judge clients."""
    cfg = LOCAL_MODELS[model_name]
    config.MODELS[model_name] = {
        "model_id": cfg["model_id"],
        "max_tokens": cfg["max_tokens"],
    }


def _set_harness_client(model_name: str):
    harness._client = get_local_client(model_name)


def _set_judge_client(model_name: str):
    judge._client = get_local_client(model_name)


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

LOCAL_STUDY_DIR = config.ARTIFACTS_DIR / "local_study"
EPISODES_DIR = LOCAL_STUDY_DIR / "episodes"
JUDGMENTS_DIR = LOCAL_STUDY_DIR / "judgments"
ERRORS_FILE = LOCAL_STUDY_DIR / "errors.jsonl"

# ---------------------------------------------------------------------------
# Phase 1: Episode generation (mirrors run_full_study.run_phase1)
# ---------------------------------------------------------------------------


def _load_completed_episodes(model_dir: Path) -> set[str]:
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
    LOCAL_STUDY_DIR.mkdir(parents=True, exist_ok=True)
    total_done = 0
    total_errors = 0
    total_skipped = 0

    for model_name in models:
        _inject_model(model_name)
        _set_harness_client(model_name)

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
# Phase 2: Cross-judge (mirrors run_full_study.run_phase2)
# ---------------------------------------------------------------------------


def _load_judged_ids(model_dir: Path) -> set[str]:
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
    clause_index = judge.build_clause_index(clauses)
    config.CROSS_JUDGE_MAP.update(LOCAL_CROSS_JUDGE_MAP)
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

        judge_model = LOCAL_CROSS_JUDGE_MAP[model_name]
        _inject_model(judge_model)
        _set_judge_client(judge_model)

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
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run policy ambiguity experiments against local Qwen3 vLLM endpoints.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Examples:
  python local_model_client.py --phase 1 --clauses clause_templates_full.json
  python local_model_client.py --phase 2
  python local_model_client.py --all --clauses clause_templates_full.json
  python local_model_client.py --all --models qwen3-8b
""",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--phase", type=int, choices=[1, 2],
        help="Run a specific phase (1=episodes, 2=cross-judge).",
    )
    group.add_argument(
        "--all", action="store_true",
        help="Run Phase 1 + Phase 2 sequentially.",
    )
    parser.add_argument(
        "--clauses",
        default=str(config.ARTIFACTS_DIR / "clause_templates_full.json"),
        help="Path to clauses JSON (default: clause_templates_full.json).",
    )
    parser.add_argument(
        "--models", default="qwen3-8b,qwen3-32b-awq",
        help="Comma-separated local model names (default: qwen3-8b,qwen3-32b-awq).",
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
        if m not in LOCAL_MODELS:
            print(f"Error: unknown local model '{m}'. "
                  f"Available: {list(LOCAL_MODELS.keys())}")
            sys.exit(1)

    clauses = harness.load_clauses(args.clauses)
    phases = [1, 2] if args.all else [args.phase]

    for phase in phases:
        print(f"\n{'=' * 40} Phase {phase} {'=' * 40}\n")
        if phase == 1:
            asyncio.run(run_phase1(clauses, models, args.concurrency, args.resume))
        elif phase == 2:
            asyncio.run(run_phase2(clauses, models, args.concurrency, args.resume))


if __name__ == "__main__":
    main()
