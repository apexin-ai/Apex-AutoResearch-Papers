#!/usr/bin/env python3
"""Cross-judge validation: re-judge all 2997 episodes with Claude Sonnet 4.6 and Gemini 2.5 Pro."""

import asyncio
import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, "/home/ubuntu/agent-ml-research")
from core.crypto import load_secret

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config

# ── Constants ──
EPISODES_DIR = Path(__file__).resolve().parent.parent / "full_study" / "episodes"
CLAUSES_FILE = Path(__file__).resolve().parent.parent / "clause_templates_full.json"
OUTPUT_BASE = Path(__file__).resolve().parent

CROSS_JUDGES = {
    "claude": {
        "model_id": "anthropic/claude-sonnet-4-6",
        "output_dir": OUTPUT_BASE / "judgments_claude",
        "label": "claude-sonnet-4-6",
    },
    "gemini": {
        "model_id": "google/gemini-2.5-pro",
        "output_dir": OUTPUT_BASE / "judgments_gemini",
        "label": "gemini-2.5-pro",
    },
}

CONCURRENCY = 5
AGENT_MODELS = ["claude-sonnet-4-6", "deepseek-v3", "gpt-4.1", "gpt-5.4", "qwen3-235b"]


OPENROUTER_OFFICIAL_BASE_URL = "https://openrouter.ai/api/v1"

def setup_api_key():
    key = load_secret(
        Path("/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/secrets/policy_ambiguity_safety/openrouter_api_key_official.enc")
    )
    os.environ["OPENROUTER_API_KEY"] = key


def load_all_episodes() -> list[dict]:
    episodes = []
    for model in AGENT_MODELS:
        ep_file = EPISODES_DIR / model / "episodes.jsonl"
        with open(ep_file) as f:
            for line in f:
                if line.strip():
                    episodes.append(json.loads(line))
    return episodes


def load_clause_index() -> dict[str, dict]:
    with open(CLAUSES_FILE) as f:
        clauses = json.load(f)
    return {c["clause_id"]: c for c in clauses}


def format_trajectory(trajectory: list[dict]) -> str:
    parts = []
    for entry in trajectory:
        role = entry.get("role", "unknown")
        if role == "user":
            parts.append(f"[User] {entry['content']}")
        elif role == "assistant":
            text = entry.get("content", "")
            if text:
                parts.append(f"[Agent] {text}")
            for tc in entry.get("tool_calls", []):
                parts.append(f"[Agent Tool Call] {tc['name']}({json.dumps(tc['arguments'], ensure_ascii=False)})")
        elif role == "tool":
            parts.append(f"[Tool Result ({entry.get('name', '')})] {entry['content']}")
        elif role == "error":
            parts.append(f"[Error] {entry['content']}")
    return "\n".join(parts)


def parse_judge_response(text: str) -> dict:
    json_match = re.search(r'\{[^{}]*"violation_level"[^{}]*\}', text, re.DOTALL)
    if json_match:
        try:
            parsed = json.loads(json_match.group())
            level = parsed.get("violation_level", "").lower()
            if level in config.VIOLATION_LEVELS:
                return {
                    "violation_level": level,
                    "violation_description": parsed.get("violation_description", ""),
                    "relevant_policy_point": parsed.get("relevant_policy_point", ""),
                    "confidence": float(parsed.get("confidence", 0.0)),
                }
        except (json.JSONDecodeError, ValueError):
            pass

    text_lower = text.lower()
    for level in reversed(config.VIOLATION_LEVELS):
        if level in text_lower:
            return {
                "violation_level": level,
                "violation_description": text[:500],
                "relevant_policy_point": "",
                "confidence": 0.5,
            }

    return {
        "violation_level": "none",
        "violation_description": f"Could not parse judge response: {text[:200]}",
        "relevant_policy_point": "",
        "confidence": 0.0,
    }


def load_judged_ids(output_dir: Path) -> set[str]:
    judged = set()
    for jsonl_file in output_dir.glob("*.jsonl"):
        with open(jsonl_file) as f:
            for line in f:
                if line.strip():
                    try:
                        rec = json.loads(line)
                        judged.add(rec["episode_id"])
                    except (json.JSONDecodeError, KeyError):
                        pass
    return judged


async def run_judge(judge_key: str, episodes: list[dict], clause_index: dict[str, dict]):
    judge_cfg = CROSS_JUDGES[judge_key]
    model_id = judge_cfg["model_id"]
    output_dir = judge_cfg["output_dir"]
    label = judge_cfg["label"]

    output_dir.mkdir(parents=True, exist_ok=True)
    judged_ids = load_judged_ids(output_dir)
    pending = [ep for ep in episodes if ep["episode_id"] not in judged_ids]

    if not pending:
        print(f"[{label}] All episodes already judged. Skipping.")
        return

    print(f"[{label}] Judging {len(pending)} episodes (skipped {len(judged_ids)} already done)...")

    import openai
    client = openai.AsyncOpenAI(
        api_key=[REDACTED]"OPENROUTER_API_KEY"],
        base_url=OPENROUTER_OFFICIAL_BASE_URL,
    )

    semaphore = asyncio.Semaphore(CONCURRENCY)
    output_file = output_dir / "judgments.jsonl"
    lock = asyncio.Lock()
    done_count = 0
    error_count = 0

    async def judge_one(episode: dict):
        nonlocal done_count, error_count
        clause = clause_index[episode["clause_id"]]
        ground_truth = clause["unambiguous_clause"]
        condition = episode["condition"]
        agent_clause = clause.get(f"{condition}_clause", ground_truth)
        trajectory_text = format_trajectory(episode["trajectory"])

        user_prompt = config.JUDGE_USER_TEMPLATE.format(
            ground_truth_clause=ground_truth,
            agent_clause=agent_clause,
            trajectory=trajectory_text,
        )

        judgment = None
        raw_response = ""
        for attempt in range(3):
            try:
                async with semaphore:
                    response = await client.chat.completions.create(
                        model=model_id,
                        max_tokens=1024,
                        messages=[
                            {"role": "system", "content": config.JUDGE_SYSTEM_PROMPT},
                            {"role": "user", "content": user_prompt},
                        ],
                        timeout=120,
                    )
                raw_response = response.choices[0].message.content or ""
                judgment = parse_judge_response(raw_response)
                break
            except Exception as e:
                raw_response = str(e)
                if attempt == 2:
                    judgment = {
                        "violation_level": "none",
                        "violation_description": f"Judge call failed after 3 attempts: {e}",
                        "relevant_policy_point": "",
                        "confidence": 0.0,
                    }
                    error_count += 1
                else:
                    await asyncio.sleep(2 ** attempt)

        result = {
            "episode_id": episode["episode_id"],
            "clause_id": episode["clause_id"],
            "ambiguity_type": episode["ambiguity_type"],
            "condition": episode["condition"],
            "model": episode["model"],
            "judgment": judgment,
            "judge_model": label,
            "judge_raw_response": raw_response,
            "timestamp": time.time(),
        }

        async with lock:
            with open(output_file, "a") as f:
                f.write(json.dumps(result, ensure_ascii=False) + "\n")
            done_count += 1
            if done_count % 50 == 0 or done_count == len(pending):
                print(f"  [{label}] {done_count}/{len(pending)} done ({error_count} errors)")

    await asyncio.gather(*[judge_one(ep) for ep in pending], return_exceptions=True)
    print(f"[{label}] Complete: {done_count} judged, {error_count} errors → {output_file}")


async def main():
    global CONCURRENCY

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--judge", choices=["claude", "gemini", "both"], default="both")
    parser.add_argument("--concurrency", type=int, default=CONCURRENCY)
    args = parser.parse_args()

    CONCURRENCY = args.concurrency

    setup_api_key()
    episodes = load_all_episodes()
    clause_index = load_clause_index()
    print(f"Loaded {len(episodes)} episodes, {len(clause_index)} clauses")

    if args.judge == "both":
        await asyncio.gather(
            run_judge("claude", episodes, clause_index),
            run_judge("gemini", episodes, clause_index),
        )
    else:
        await run_judge(args.judge, episodes, clause_index)


if __name__ == "__main__":
    asyncio.run(main())
