#!/usr/bin/env python3
"""Residual variance decomposition: run replicated episodes.

Stratified-samples 50 clauses (≈8 per ambiguity type), then runs each
clause × condition × model × 5 reps as independent conversations.
Judges each episode via the cross-judge map.
"""

import argparse
import asyncio
import json
import os
import random
import sys
import time
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config
import harness
import judge as judge_mod

# ── Defaults ──
N_CLAUSES = 50
N_REPS = 5
MODELS = ["gpt-4.1", "claude-sonnet-4-6"]
SEED = 42

ARTIFACTS_DIR = Path(__file__).resolve().parent
CLAUSES_PATH = ARTIFACTS_DIR.parent / "clause_templates_full.json"


def stratified_sample(clauses: list[dict], n: int, seed: int) -> list[dict]:
    """Sample n clauses with roughly equal representation per ambiguity type."""
    rng = random.Random(seed)
    by_type: dict[str, list[dict]] = defaultdict(list)
    for c in clauses:
        by_type[c["ambiguity_type"]].append(c)

    types = sorted(by_type.keys())
    n_types = len(types)
    base = n // n_types
    remainder = n % n_types
    extra_types = rng.sample(types, remainder)

    selected = []
    for t in types:
        k = base + (1 if t in extra_types else 0)
        pool = by_type[t]
        chosen = rng.sample(pool, min(k, len(pool)))
        selected.extend(chosen)

    rng.shuffle(selected)
    return selected


def _rep_key(clause_id: str, condition: str, model: str, rep: int) -> str:
    return f"{clause_id}|{condition}|{model}|rep{rep}"


def load_completed(output_dir: Path) -> set[str]:
    """Load completed episode keys from existing JSONL files."""
    completed = set()
    for f in output_dir.glob("episodes*.jsonl"):
        with open(f) as fh:
            for line in fh:
                if not line.strip():
                    continue
                rec = json.loads(line)
                rep = rec.get("rep", 0)
                key = _rep_key(rec["clause_id"], rec["condition"], rec["model"], rep)
                completed.add(key)
    return completed


def load_judged(output_dir: Path) -> set[str]:
    """Load already-judged episode IDs."""
    judged = set()
    for f in output_dir.glob("judgments*.jsonl"):
        with open(f) as fh:
            for line in fh:
                if not line.strip():
                    continue
                rec = json.loads(line)
                judged.add(rec["episode_id"])
    return judged


async def run_and_judge(
    clauses: list[dict],
    models: list[str],
    n_reps: int,
    output_dir: Path,
    concurrency: int = 8,
    judge_concurrency: int = 5,
    resume: bool = True,
):
    output_dir.mkdir(parents=True, exist_ok=True)
    clause_index = judge_mod.build_clause_index(clauses)

    # ── Phase 1: Run episodes ──
    completed = load_completed(output_dir) if resume else set()

    tasks = []
    for clause in clauses:
        for condition in ("ambiguous", "unambiguous"):
            for model in models:
                for rep in range(n_reps):
                    key = _rep_key(clause["clause_id"], condition, model, rep)
                    if key not in completed:
                        tasks.append((clause, condition, model, rep))

    episodes_file = output_dir / "episodes.jsonl"

    if tasks:
        print(f"Running {len(tasks)} episodes ({len(completed)} already done, concurrency={concurrency})…")
        sem = asyncio.Semaphore(concurrency)
        lock = asyncio.Lock()
        done = 0
        total = len(tasks)
        all_new_episodes = []

        async def _run_one(clause, condition, model, rep):
            nonlocal done
            async with sem:
                try:
                    episode = await harness.run_episode(clause, condition, model)
                    episode["rep"] = rep
                except Exception as e:
                    episode = {
                        "episode_id": f"error-{clause['clause_id']}-{condition}-{model}-{rep}",
                        "clause_id": clause["clause_id"],
                        "ambiguity_type": clause["ambiguity_type"],
                        "condition": condition,
                        "model": model,
                        "rep": rep,
                        "trajectory": [],
                        "status": "error",
                        "error": str(e),
                        "timestamp": time.time(),
                    }

                async with lock:
                    with open(episodes_file, "a") as f:
                        f.write(json.dumps(episode, ensure_ascii=False) + "\n")
                    all_new_episodes.append(episode)
                    done += 1
                    if done % 20 == 0 or done == total:
                        print(f"  Episodes: [{done}/{total}]")

        await asyncio.gather(*[_run_one(*t) for t in tasks], return_exceptions=True)
        print(f"Episodes done. Total new: {len(all_new_episodes)}")
    else:
        print("All episodes already completed.")
        all_new_episodes = []

    # ── Phase 2: Judge episodes ──
    all_episodes = []
    for f in output_dir.glob("episodes*.jsonl"):
        with open(f) as fh:
            for line in fh:
                if line.strip():
                    all_episodes.append(json.loads(line))

    valid_episodes = [ep for ep in all_episodes if ep.get("status") == "ok"]
    judged_ids = load_judged(output_dir) if resume else set()
    pending_judge = [ep for ep in valid_episodes if ep["episode_id"] not in judged_ids]

    judgments_file = output_dir / "judgments.jsonl"

    if pending_judge:
        print(f"Judging {len(pending_judge)} episodes ({len(judged_ids)} already judged)…")
        sem_j = asyncio.Semaphore(judge_concurrency)
        lock_j = asyncio.Lock()
        done_j = 0
        total_j = len(pending_judge)

        async def _judge_one(episode):
            nonlocal done_j
            async with sem_j:
                result = await judge_mod.judge_episode(episode, clause_index)
                result["rep"] = episode.get("rep", 0)
                async with lock_j:
                    with open(judgments_file, "a") as f:
                        f.write(json.dumps(result, ensure_ascii=False) + "\n")
                    done_j += 1
                    if done_j % 20 == 0 or done_j == total_j:
                        print(f"  Judgments: [{done_j}/{total_j}]")

        await asyncio.gather(*[_judge_one(ep) for ep in pending_judge], return_exceptions=True)
        print(f"Judging done.")
    else:
        print("All episodes already judged.")

    # ── Summary ──
    total_eps = sum(1 for f in output_dir.glob("episodes*.jsonl")
                    for line in open(f) if line.strip())
    total_jdg = sum(1 for f in output_dir.glob("judgments*.jsonl")
                    for line in open(f) if line.strip())
    print(f"\nFinal counts: {total_eps} episodes, {total_jdg} judgments")


def setup_api_key():
    if os.environ.get("OPENROUTER_API_KEY"):
        return
    try:
        sys.path.insert(0, "/home/ubuntu/agent-ml-research")
        from core.crypto import load_secret
        key = load_secret(Path(
            "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
            "/config/secrets/policy_ambiguity_safety/openrouter_api_key_official.enc"
        ))
        os.environ["OPENROUTER_API_KEY"] = key
    except Exception as e:
        print(f"Failed to load API key: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Residual variance decomposition: replicated episodes")
    parser.add_argument("--clauses", default=str(CLAUSES_PATH))
    parser.add_argument("--models", default=",".join(MODELS))
    parser.add_argument("--n-clauses", type=int, default=N_CLAUSES)
    parser.add_argument("--n-reps", type=int, default=N_REPS)
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--output", default=str(ARTIFACTS_DIR))
    parser.add_argument("--concurrency", type=int, default=8)
    parser.add_argument("--judge-concurrency", type=int, default=5)
    parser.add_argument("--no-resume", action="store_true")
    parser.add_argument("--sample-only", action="store_true", help="Print sampled clauses and exit")
    args = parser.parse_args()

    all_clauses = harness.load_clauses(args.clauses)
    sampled = stratified_sample(all_clauses, args.n_clauses, args.seed)
    models = [m.strip() for m in args.models.split(",")]

    print(f"Sampled {len(sampled)} clauses:")
    from collections import Counter
    type_counts = Counter(c["ambiguity_type"] for c in sampled)
    for t, n in sorted(type_counts.items()):
        print(f"  {t}: {n}")

    if args.sample_only:
        for c in sampled:
            print(f"  {c['clause_id']} ({c['ambiguity_type']})")
        return

    # Save sample manifest
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "seed": args.seed,
        "n_clauses": len(sampled),
        "n_reps": args.n_reps,
        "models": models,
        "clause_ids": [c["clause_id"] for c in sampled],
        "type_distribution": dict(type_counts),
        "timestamp": time.time(),
    }
    with open(output_dir / "manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)

    total_episodes = len(sampled) * 2 * len(models) * args.n_reps
    total_judgments = total_episodes
    print(f"\nTotal planned: {total_episodes} episodes + {total_judgments} judgments")
    print(f"Models: {models}")
    print(f"Reps per cell: {args.n_reps}")

    setup_api_key()

    for m in models:
        if m not in config.MODELS:
            print(f"Error: unknown model '{m}'. Available: {list(config.MODELS.keys())}")
            sys.exit(1)

    asyncio.run(run_and_judge(
        clauses=sampled,
        models=models,
        n_reps=args.n_reps,
        output_dir=output_dir,
        concurrency=args.concurrency,
        judge_concurrency=args.judge_concurrency,
        resume=not args.no_resume,
    ))


if __name__ == "__main__":
    main()
