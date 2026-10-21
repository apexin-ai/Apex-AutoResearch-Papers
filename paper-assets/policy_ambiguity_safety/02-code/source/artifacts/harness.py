#!/usr/bin/env python3
"""Agent Execution Harness for policy ambiguity safety experiments.

Runs LLM agents against ambiguous/unambiguous policy clauses and records
full conversation trajectories for downstream evaluation.

All model calls go through OpenRouter-compatible endpoint via openai SDK.
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
# API client (lazy-initialized, per-model routing)
# ---------------------------------------------------------------------------

_clients: dict[str, Any] = {}


def _get_client(model_name: str = ""):
    """Return an AsyncOpenAI client for the given model.

    Each unique (base_url, api_key_env) pair gets its own client instance.
    Falls back to OPENROUTER defaults when model_name is empty or not in MODELS.
    """
    model_cfg = config.MODELS.get(model_name, {})
    base_url = model_cfg.get("base_url", config.OPENROUTER_BASE_URL)
    key_env = model_cfg.get("api_key_env", config.API_KEY_ENV)
    cache_key = f"{base_url}|{key_env}"

    if cache_key not in _clients:
        api_key = [REDACTED]
        if not api_key:
            raise RuntimeError(
                f"API key env var '{key_env}' is not set. "
                f"Cannot create client for model '{model_name}'."
            )
        import openai
        _clients[cache_key] = openai.AsyncOpenAI(
            api_key=[REDACTED],
            base_url=base_url,
        )
    return _clients[cache_key]


async def preflight_check(model_name: str) -> bool:
    """Verify API connectivity with a minimal request. Raises on failure."""
    client = _get_client(model_name)
    model_cfg = config.MODELS[model_name]
    response = await client.chat.completions.create(
        model=model_cfg["model_id"],
        max_tokens=5,
        messages=[{"role": "user", "content": "Say OK"}],
    )
    text = response.choices[0].message.content or ""
    if not text.strip():
        raise RuntimeError(f"Preflight for {model_name}: empty response")
    return True


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
        "tool_responses": [...]      # pre-generated tool responses
    }
    """
    with open(path) as f:
        clauses = json.load(f)
    if isinstance(clauses, dict) and "clauses" in clauses:
        clauses = clauses["clauses"]
    for c in clauses:
        if "ambiguous_version" in c and "ambiguous_clause" not in c:
            c["ambiguous_clause"] = c["ambiguous_version"]
        if "unambiguous_version" in c and "unambiguous_clause" not in c:
            c["unambiguous_clause"] = c["unambiguous_version"]
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
# Agent call (unified OpenAI-compatible path)
# ---------------------------------------------------------------------------

async def call_agent(
    model_name: str,
    system_prompt: str,
    messages: list[dict],
    tools: list[dict] | None = None,
    temperature: float | None = None,
) -> dict:
    model_cfg = config.MODELS[model_name]
    client = _get_client(model_name)
    full_messages = [{"role": "system", "content": system_prompt}] + messages
    kwargs: dict[str, Any] = {
        "model": model_cfg["model_id"],
        "max_tokens": model_cfg["max_tokens"],
        "messages": full_messages,
    }
    if tools:
        kwargs["tools"] = tools
    if temperature is not None:
        kwargs["temperature"] = temperature
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


# ---------------------------------------------------------------------------
# Single episode execution
# ---------------------------------------------------------------------------

MAX_TURNS = 10


def _match_tool_response(
    tool_name: str,
    tool_args: dict,
    tool_responses_remaining: list[dict],
) -> dict:
    """Match a tool call to a pre-generated response, consuming from the list.

    Responses are matched by tool_name and args_pattern (where "*" matches any
    value). The first matching entry is popped from tool_responses_remaining so
    that repeated calls to the same tool return successive responses.
    """
    for i, tr in enumerate(tool_responses_remaining):
        if tr["tool_name"] != tool_name:
            continue
        pattern = tr.get("args_pattern", {})
        match = True
        for k, v in pattern.items():
            if v != "*" and tool_args.get(k) != v:
                match = False
                break
        if match:
            tool_responses_remaining.pop(i)
            return tr["response"]
    return {"status": "simulated", "note": "No matching pre-generated response"}


async def run_episode(
    clause: dict,
    condition: str,  # "ambiguous" or "unambiguous"
    model_name: str,
    temperature: float | None = None,
) -> dict:
    """Run a single agent episode and return the full trajectory."""
    clause_text = clause[f"{condition}_clause"]
    system_prompt = build_system_prompt(clause_text)
    tools = clause.get("stripped_tool_desc") or clause.get("tools")

    trajectory: list[dict] = []
    messages: list[dict] = []
    tool_responses_remaining = list(clause.get("tool_responses", []))

    user_msg = {"role": "user", "content": clause["user_scenario"]}
    messages.append(user_msg)
    trajectory.append(user_msg)

    status = "ok"
    error_msg = ""

    for _turn in range(MAX_TURNS):
        try:
            response = await call_agent(model_name, system_prompt, messages, tools, temperature)
        except Exception as e:
            trajectory.append({"role": "error", "content": str(e)})
            status = "error"
            error_msg = str(e)
            break

        trajectory.append(response)

        if response["tool_calls"]:
            tool_results = []
            for tc in response["tool_calls"]:
                response_content = _match_tool_response(
                    tc["name"],
                    tc.get("arguments", {}),
                    tool_responses_remaining,
                )
                tool_result = {
                    "role": "tool",
                    "tool_call_id": tc["id"],
                    "name": tc["name"],
                    "content": json.dumps(response_content, ensure_ascii=False),
                }
                tool_results.append(tool_result)
                trajectory.append(tool_result)

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

    result = {
        "episode_id": str(uuid.uuid4()),
        "clause_id": clause["clause_id"],
        "ambiguity_type": clause["ambiguity_type"],
        "condition": condition,
        "model": model_name,
        "system_prompt": system_prompt,
        "trajectory": trajectory,
        "status": status,
        "temperature": temperature,
        "timestamp": time.time(),
    }
    if error_msg:
        result["error"] = error_msg
    return result


def validate_episode(episode: dict) -> str:
    """Check episode has meaningful content. Returns 'ok', 'error', or 'invalid'."""
    if episode.get("status") == "error":
        return "error"
    trajectory = episode.get("trajectory", [])
    has_assistant = any(t.get("role") == "assistant" for t in trajectory)
    has_tool_call = any(
        t.get("role") == "assistant" and t.get("tool_calls")
        for t in trajectory
    )
    if not has_assistant:
        return "invalid"
    return "ok"


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
