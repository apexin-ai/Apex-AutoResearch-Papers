#!/usr/bin/env python3
"""Agent Execution Harness for policy ambiguity safety experiments.

Runs LLM agents against ambiguous/unambiguous policy clauses and records
full conversation trajectories for downstream evaluation.
"""

import argparse
import asyncio
import json
import os
import sys
import time
import uuid
from pathlib import Path
from typing import Any

import config

# ---------------------------------------------------------------------------
# Provider clients (lazy-initialized)
# ---------------------------------------------------------------------------

_anthropic_client = None
_openai_client = None


def _get_anthropic_client():
    global _anthropic_client
    if _anthropic_client is None:
        import anthropic
        _anthropic_client = anthropic.AsyncAnthropic(
            api_key=[REDACTED]"ANTHROPIC_API_KEY"]
        )
    return _anthropic_client


def _get_openai_client():
    global _openai_client
    if _openai_client is None:
        import openai
        _openai_client = openai.AsyncOpenAI(
            api_key=[REDACTED]"OPENAI_API_KEY"]
        )
    return _openai_client


# ---------------------------------------------------------------------------
# Clause loading
# ---------------------------------------------------------------------------

def load_clauses(path: str) -> list[dict]:
    """Load clause definitions from JSON.

    Expected schema per clause:
    {
        "clause_id": "S01",
        "ambiguity_type": "scopal|lexical|incompleteness",
        "ambiguous_clause": "...",
        "unambiguous_clause": "...",
        "user_scenario": "...",
        "tools": [...],              # optional tool definitions
        "stripped_tool_desc": [...]   # tool defs with info stripped from descriptions
    }
    """
    with open(path) as f:
        clauses = json.load(f)
    if isinstance(clauses, dict) and "clauses" in clauses:
        clauses = clauses["clauses"]
    return clauses


# ---------------------------------------------------------------------------
# System prompt construction
# ---------------------------------------------------------------------------

def build_system_prompt(clause_text: str) -> str:
    return config.SYSTEM_PROMPT_TEMPLATE.format(
        agent_instruction=config.AGENT_INSTRUCTION,
        policy_clause=clause_text,
    )


# ---------------------------------------------------------------------------
# Provider-specific agent calls
# ---------------------------------------------------------------------------

async def _call_anthropic(
    model_cfg: dict,
    system_prompt: str,
    messages: list[dict],
    tools: list[dict] | None,
) -> dict:
    client = _get_anthropic_client()
    kwargs: dict[str, Any] = {
        "model": model_cfg["model_id"],
        "max_tokens": model_cfg["max_tokens"],
        "system": system_prompt,
        "messages": messages,
    }
    if tools:
        kwargs["tools"] = [
            {
                "name": t["function"]["name"],
                "description": t["function"].get("description", ""),
                "input_schema": t["function"].get("parameters", {"type": "object", "properties": {}}),
            }
            for t in tools
        ]
    response = await client.messages.create(**kwargs)

    assistant_text = ""
    tool_calls = []
    for block in response.content:
        if block.type == "text":
            assistant_text += block.text
        elif block.type == "tool_use":
            tool_calls.append({
                "id": block.id,
                "name": block.name,
                "arguments": block.input,
            })
    return {
        "role": "assistant",
        "content": assistant_text,
        "tool_calls": tool_calls,
        "stop_reason": response.stop_reason,
    }


async def _call_openai(
    model_cfg: dict,
    system_prompt: str,
    messages: list[dict],
    tools: list[dict] | None,
) -> dict:
    client = _get_openai_client()
    full_messages = [{"role": "system", "content": system_prompt}] + messages
    kwargs: dict[str, Any] = {
        "model": model_cfg["model_id"],
        "max_tokens": model_cfg["max_tokens"],
        "messages": full_messages,
    }
    if tools:
        kwargs["tools"] = tools
    response = await client.chat.completions.create(**kwargs)
    choice = response.choices[0]
    msg = choice.message

    tool_calls = []
    if msg.tool_calls:
        for tc in msg.tool_calls:
            tool_calls.append({
                "id": tc.id,
                "name": tc.function.name,
                "arguments": json.loads(tc.function.arguments) if isinstance(tc.function.arguments, str) else tc.function.arguments,
            })
    return {
        "role": "assistant",
        "content": msg.content or "",
        "tool_calls": tool_calls,
        "stop_reason": choice.finish_reason,
    }


async def call_agent(
    model_name: str,
    system_prompt: str,
    messages: list[dict],
    tools: list[dict] | None = None,
) -> dict:
    model_cfg = config.MODELS[model_name]
    if model_cfg["provider"] == "anthropic":
        return await _call_anthropic(model_cfg, system_prompt, messages, tools)
    elif model_cfg["provider"] == "openai":
        return await _call_openai(model_cfg, system_prompt, messages, tools)
    else:
        raise ValueError(f"Unknown provider: {model_cfg['provider']}")


# ---------------------------------------------------------------------------
# Single episode execution
# ---------------------------------------------------------------------------

MAX_TURNS = 10


async def run_episode(
    clause: dict,
    condition: str,  # "ambiguous" or "unambiguous"
    model_name: str,
) -> dict:
    """Run a single agent episode and return the full trajectory."""
    clause_text = clause[f"{condition}_clause"]
    system_prompt = build_system_prompt(clause_text)
    tools = clause.get("stripped_tool_desc") or clause.get("tools")

    trajectory: list[dict] = []
    messages: list[dict] = []

    user_msg = {"role": "user", "content": clause["user_scenario"]}
    messages.append(user_msg)
    trajectory.append(user_msg)

    for _turn in range(MAX_TURNS):
        try:
            response = await call_agent(model_name, system_prompt, messages, tools)
        except Exception as e:
            trajectory.append({"role": "error", "content": str(e)})
            break

        trajectory.append(response)

        if response["tool_calls"]:
            tool_results = []
            for tc in response["tool_calls"]:
                tool_result = {
                    "role": "tool",
                    "tool_call_id": tc["id"],
                    "name": tc["name"],
                    "content": json.dumps({"status": "simulated", "note": "Tool execution simulated for safety evaluation"}),
                }
                tool_results.append(tool_result)
                trajectory.append(tool_result)

            if config.MODELS[model_name]["provider"] == "anthropic":
                messages.append({"role": "assistant", "content": response["content"] if response["content"] else None,
                                 "tool_calls": response["tool_calls"]})
                for tr in tool_results:
                    messages.append({"role": "user", "content": [
                        {"type": "tool_result", "tool_use_id": tr["tool_call_id"], "content": tr["content"]}
                    ]})
            else:
                messages.append({
                    "role": "assistant",
                    "content": response["content"],
                    "tool_calls": [
                        {"id": tc["id"], "type": "function",
                         "function": {"name": tc["name"], "arguments": json.dumps(tc["arguments"])}}
                        for tc in response["tool_calls"]
                    ],
                })
                for tr in tool_results:
                    messages.append({"role": "tool", "tool_call_id": tr["tool_call_id"], "content": tr["content"]})
        else:
            if response.get("stop_reason") in ("end_turn", "stop", None):
                break
            messages.append({"role": "assistant", "content": response["content"]})

    return {
        "episode_id": str(uuid.uuid4()),
        "clause_id": clause["clause_id"],
        "ambiguity_type": clause["ambiguity_type"],
        "condition": condition,
        "model": model_name,
        "system_prompt": system_prompt,
        "trajectory": trajectory,
        "timestamp": time.time(),
    }


# ---------------------------------------------------------------------------
# Batch runner with concurrency + resume
# ---------------------------------------------------------------------------

def _load_completed(output_dir: Path) -> set[str]:
    """Return set of (clause_id, condition, model) keys already completed."""
    completed = set()
    for jsonl_file in output_dir.glob("*.jsonl"):
        with open(jsonl_file) as f:
            for line in f:
                if line.strip():
                    rec = json.loads(line)
                    key = f"{rec['clause_id']}|{rec['condition']}|{rec['model']}"
                    completed.add(key)
    return completed


def _episode_key(clause_id: str, condition: str, model: str) -> str:
    return f"{clause_id}|{condition}|{model}"


async def run_all(
    clauses: list[dict],
    models: list[str],
    output_dir: Path,
    concurrency: int = config.DEFAULT_CONCURRENCY,
    resume: bool = True,
):
    output_dir.mkdir(parents=True, exist_ok=True)
    completed = _load_completed(output_dir) if resume else set()

    tasks = []
    for clause in clauses:
        for condition in ("ambiguous", "unambiguous"):
            for model in models:
                key = _episode_key(clause["clause_id"], condition, model)
                if key in completed:
                    continue
                tasks.append((clause, condition, model))

    if not tasks:
        print("All episodes already completed.")
        return

    print(f"Running {len(tasks)} episodes (concurrency={concurrency})…")
    semaphore = asyncio.Semaphore(concurrency)
    output_file = output_dir / "episodes.jsonl"
    lock = asyncio.Lock()
    done_count = 0

    async def _run_one(clause, condition, model):
        nonlocal done_count
        async with semaphore:
            result = await run_episode(clause, condition, model)
            async with lock:
                with open(output_file, "a") as f:
                    f.write(json.dumps(result, ensure_ascii=False) + "\n")
                done_count += 1
                if done_count % 10 == 0 or done_count == len(tasks):
                    print(f"  [{done_count}/{len(tasks)}] completed")

    await asyncio.gather(
        *[_run_one(c, cond, m) for c, cond, m in tasks],
        return_exceptions=True,
    )
    print(f"Done. Results written to {output_file}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run agent episodes against ambiguous/unambiguous policy clauses."
    )
    parser.add_argument(
        "--clauses", required=True,
        help="Path to clauses JSON file.",
    )
    parser.add_argument(
        "--models", default="claude-sonnet-4-5,gpt-5.4",
        help="Comma-separated model names (default: claude-sonnet-4-5,gpt-5.4).",
    )
    parser.add_argument(
        "--output", default=str(config.DEFAULT_OUTPUT_DIR),
        help="Output directory for episode results.",
    )
    parser.add_argument(
        "--concurrency", type=int, default=config.DEFAULT_CONCURRENCY,
        help=f"Max concurrent API calls (default: {config.DEFAULT_CONCURRENCY}).",
    )
    parser.add_argument(
        "--resume", action="store_true", default=True,
        help="Skip already-completed episodes (default: True).",
    )
    parser.add_argument(
        "--no-resume", action="store_false", dest="resume",
        help="Re-run all episodes, ignoring previous results.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None):
    args = parse_args(argv)
    clauses = load_clauses(args.clauses)
    models = [m.strip() for m in args.models.split(",")]

    for m in models:
        if m not in config.MODELS:
            print(f"Error: unknown model '{m}'. Available: {list(config.MODELS.keys())}")
            sys.exit(1)

    asyncio.run(run_all(
        clauses=clauses,
        models=models,
        output_dir=Path(args.output),
        concurrency=args.concurrency,
        resume=args.resume,
    ))


if __name__ == "__main__":
    main()
