#!/usr/bin/env python3
"""Local open-source model harness for policy ambiguity safety experiments.

Runs LLM agents using local GPU inference (vLLM server or HuggingFace
Transformers) with the same input/output format as harness.py.
"""

import argparse
import asyncio
import json
import re
import sys
import time
import uuid
from pathlib import Path
from typing import Any

import config
import config_local
from harness import (
    MAX_TURNS,
    _match_tool_response,
    build_system_prompt,
    load_clauses,
)

# ---------------------------------------------------------------------------
# Backend: vLLM (OpenAI-compatible server)
# ---------------------------------------------------------------------------

_vllm_client = None
_vllm_client_base_url = None


def _get_vllm_client(base_url: str):
    global _vllm_client, _vllm_client_base_url
    if _vllm_client is None or _vllm_client_base_url != base_url:
        import openai

        _vllm_client = openai.AsyncOpenAI(api_key="[REDACTED]", base_url=base_url)
        _vllm_client_base_url = base_url
    return _vllm_client


async def call_agent_vllm(
    model_id: str,
    system_prompt: str,
    messages: list[dict],
    tools: list[dict] | None = None,
    base_url: str = "http://localhost:8000/v1",
    gen_params: dict | None = None,
) -> dict:
    client = _get_vllm_client(base_url)
    params = {**config_local.DEFAULT_GENERATION_PARAMS, **(gen_params or {})}

    full_messages = [{"role": "system", "content": system_prompt}] + messages
    kwargs: dict[str, Any] = {
        "model": model_id,
        "messages": full_messages,
        **params,
    }
    if tools:
        kwargs["tools"] = tools

    response = await client.chat.completions.create(**kwargs)
    choice = response.choices[0]
    msg = choice.message

    tool_calls = []
    if msg.tool_calls:
        for tc in msg.tool_calls:
            tool_calls.append(
                {
                    "id": tc.id,
                    "name": tc.function.name,
                    "arguments": (
                        json.loads(tc.function.arguments)
                        if isinstance(tc.function.arguments, str)
                        else tc.function.arguments
                    ),
                }
            )
    return {
        "role": "assistant",
        "content": msg.content or "",
        "tool_calls": tool_calls,
        "stop_reason": choice.finish_reason,
    }


# ---------------------------------------------------------------------------
# Backend: HuggingFace Transformers (direct inference)
# ---------------------------------------------------------------------------

_hf_model = None
_hf_tokenizer = None


def _load_hf_model(model_id: str, device_map: str = "auto"):
    global _hf_model, _hf_tokenizer
    if _hf_model is not None:
        return _hf_model, _hf_tokenizer
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    print(f"Loading model {model_id} ...")
    _hf_tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    _hf_model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.bfloat16,
        device_map=device_map,
        trust_remote_code=True,
    )
    print("Model loaded.")
    return _hf_model, _hf_tokenizer


# ---- tool-call parsing ----------------------------------------------------

def parse_tool_calls(text: str, model_family: str = "auto") -> list[dict]:
    """Parse tool calls from raw model output.

    Handles Qwen3/Hermes, DeepSeek, and generic JSON formats.
    """
    tool_calls: list[dict] = []

    # Qwen3 / Hermes: <tool_call>{"name": ..., "arguments": ...}</tool_call>
    for m in re.finditer(r"<tool_call>\s*(\{.*?\})\s*</tool_call>", text, re.DOTALL):
        try:
            tc = json.loads(m.group(1))
            tool_calls.append(
                {
                    "id": f"call_{uuid.uuid4().hex[:8]}",
                    "name": tc.get("name", ""),
                    "arguments": tc.get("arguments", tc.get("parameters", {})),
                }
            )
        except json.JSONDecodeError:
            continue
    if tool_calls:
        return tool_calls

    # DeepSeek: <｜tool▁call▁begin｜>name\n{args}\n<｜tool▁call▁end｜>
    for m in re.finditer(
        r"<｜tool▁call▁begin｜>(.*?)\n(.*?)\n<｜tool▁call▁end｜>", text, re.DOTALL
    ):
        try:
            args = json.loads(m.group(2).strip())
            tool_calls.append(
                {
                    "id": f"call_{uuid.uuid4().hex[:8]}",
                    "name": m.group(1).strip(),
                    "arguments": args,
                }
            )
        except json.JSONDecodeError:
            continue
    if tool_calls:
        return tool_calls

    # Generic: find JSON objects containing "name" via raw_decode
    decoder = json.JSONDecoder()
    pos = 0
    while pos < len(text):
        idx = text.find("{", pos)
        if idx == -1:
            break
        try:
            obj, end = decoder.raw_decode(text, idx)
            if (
                isinstance(obj, dict)
                and "name" in obj
                and ("arguments" in obj or "parameters" in obj)
            ):
                tool_calls.append(
                    {
                        "id": f"call_{uuid.uuid4().hex[:8]}",
                        "name": obj["name"],
                        "arguments": obj.get("arguments", obj.get("parameters", {})),
                    }
                )
            pos = end
        except json.JSONDecodeError:
            pos = idx + 1

    return tool_calls


def _build_tool_prompt_fallback(tools: list[dict]) -> str:
    """Inject tool definitions into system prompt when the chat template
    does not natively support the ``tools`` parameter."""
    if not tools:
        return ""
    lines = ["\n\n<available_tools>"]
    for tool in tools:
        fn = tool.get("function", tool)
        lines.append(f"- {fn['name']}: {fn.get('description', '')}")
        for pname, pdef in fn.get("parameters", {}).get("properties", {}).items():
            lines.append(
                f"    {pname} ({pdef.get('type', 'string')}): "
                f"{pdef.get('description', '')}"
            )
    lines.append("</available_tools>")
    lines.append(
        '\nTo call a tool, output:\n<tool_call>{"name": "tool_name", '
        '"arguments": {"arg": "value"}}</tool_call>'
    )
    return "\n".join(lines)


def call_agent_transformers(
    model_id: str,
    system_prompt: str,
    messages: list[dict],
    tools: list[dict] | None = None,
    gen_params: dict | None = None,
) -> dict:
    import torch

    model, tokenizer = _load_hf_model(model_id)
    params = {**config_local.DEFAULT_GENERATION_PARAMS, **(gen_params or {})}
    registry = config_local.MODEL_REGISTRY.get(model_id, {})
    model_family = registry.get("family", "auto")

    chat_messages = [{"role": "system", "content": system_prompt}] + messages

    # Try native tool support, fall back to prompt injection
    template_kwargs: dict[str, Any] = {
        "add_generation_prompt": True,
        "return_tensors": "pt",
    }
    tool_injected = False
    try:
        if tools:
            input_ids = tokenizer.apply_chat_template(
                chat_messages, tools=tools, **template_kwargs
            )
        else:
            input_ids = tokenizer.apply_chat_template(chat_messages, **template_kwargs)
    except (TypeError, ValueError, KeyError):
        if tools:
            chat_messages = list(chat_messages)
            chat_messages[0] = {
                "role": "system",
                "content": system_prompt + _build_tool_prompt_fallback(tools),
            }
            tool_injected = True
        input_ids = tokenizer.apply_chat_template(chat_messages, **template_kwargs)

    if input_ids.dim() == 1:
        input_ids = input_ids.unsqueeze(0)
    input_ids = input_ids.to(model.device)

    temperature = params.get("temperature", 0.6)
    with torch.no_grad():
        output_ids = model.generate(
            input_ids,
            max_new_tokens=params.get("max_tokens", 4096),
            temperature=temperature if temperature > 0 else None,
            top_p=params.get("top_p", 0.95) if temperature > 0 else None,
            do_sample=temperature > 0,
        )

    new_tokens = output_ids[0][input_ids.shape[1] :]
    raw_text = tokenizer.decode(new_tokens, skip_special_tokens=False)

    # Strip common EOS / padding tokens
    clean = raw_text
    for tok in ("<|im_end|>", "<|eot_id|>", "</s>", "<|end|>", "<|endoftext|>"):
        clean = clean.replace(tok, "")
    clean = clean.strip()

    tool_calls = parse_tool_calls(clean, model_family) if tools else []

    content = clean
    if tool_calls:
        for pat in (
            r"<tool_call>.*?</tool_call>",
            r"<｜tool▁call▁begin｜>.*?<｜tool▁call▁end｜>",
        ):
            content = re.sub(pat, "", content, flags=re.DOTALL)
        content = content.strip()

    return {
        "role": "assistant",
        "content": content,
        "tool_calls": tool_calls,
        "stop_reason": "tool_calls" if tool_calls else "stop",
    }


# ---------------------------------------------------------------------------
# Resume helpers (same logic as harness.py)
# ---------------------------------------------------------------------------


def _load_completed(output_dir: Path) -> set[str]:
    completed: set[str] = set()
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


# ---------------------------------------------------------------------------
# Single episode execution
# ---------------------------------------------------------------------------


async def run_episode(
    clause: dict,
    condition: str,
    model_id: str,
    backend: str,
    vllm_url: str = "http://localhost:8000/v1",
    gen_params: dict | None = None,
) -> dict:
    clause_text = clause[f"{condition}_clause"]
    system_prompt = build_system_prompt(clause_text)
    tools = clause.get("stripped_tool_desc") or clause.get("tools")

    trajectory: list[dict] = []
    messages: list[dict] = []
    tool_responses_remaining = list(clause.get("tool_responses", []))

    user_msg = {"role": "user", "content": clause["user_scenario"]}
    messages.append(user_msg)
    trajectory.append(user_msg)

    for _turn in range(MAX_TURNS):
        try:
            if backend == "vllm":
                response = await call_agent_vllm(
                    model_id, system_prompt, messages, tools, vllm_url, gen_params
                )
            else:
                response = call_agent_transformers(
                    model_id, system_prompt, messages, tools, gen_params
                )
        except Exception as e:
            trajectory.append({"role": "error", "content": str(e)})
            break

        trajectory.append(response)

        if response["tool_calls"]:
            tool_results = []
            for tc in response["tool_calls"]:
                resp_content = _match_tool_response(
                    tc["name"],
                    tc.get("arguments", {}),
                    tool_responses_remaining,
                )
                tool_result = {
                    "role": "tool",
                    "tool_call_id": tc["id"],
                    "name": tc["name"],
                    "content": json.dumps(resp_content, ensure_ascii=False),
                }
                tool_results.append(tool_result)
                trajectory.append(tool_result)

            messages.append(
                {
                    "role": "assistant",
                    "content": response["content"],
                    "tool_calls": [
                        {
                            "id": tc["id"],
                            "type": "function",
                            "function": {
                                "name": tc["name"],
                                "arguments": json.dumps(tc["arguments"]),
                            },
                        }
                        for tc in response["tool_calls"]
                    ],
                }
            )
            for tr in tool_results:
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tr["tool_call_id"],
                        "content": tr["content"],
                    }
                )
        else:
            if response.get("stop_reason") in ("stop", "end_turn", None):
                break
            messages.append({"role": "assistant", "content": response["content"]})

    return {
        "episode_id": str(uuid.uuid4()),
        "clause_id": clause["clause_id"],
        "ambiguity_type": clause["ambiguity_type"],
        "condition": condition,
        "model": model_id,
        "system_prompt": system_prompt,
        "trajectory": trajectory,
        "timestamp": time.time(),
    }


# ---------------------------------------------------------------------------
# Batch runner
# ---------------------------------------------------------------------------


async def run_all(
    clauses: list[dict],
    model_id: str,
    backend: str,
    output_dir: Path,
    vllm_url: str = "http://localhost:8000/v1",
    concurrency: int = config.DEFAULT_CONCURRENCY,
    resume: bool = True,
    gen_params: dict | None = None,
):
    output_dir.mkdir(parents=True, exist_ok=True)
    completed = _load_completed(output_dir) if resume else set()

    tasks = []
    for clause in clauses:
        for condition in ("ambiguous", "unambiguous"):
            key = _episode_key(clause["clause_id"], condition, model_id)
            if key in completed:
                continue
            tasks.append((clause, condition))

    if not tasks:
        print("All episodes already completed.")
        return

    output_file = output_dir / "episodes.jsonl"
    print(
        f"Running {len(tasks)} episodes "
        f"(backend={backend}, model={model_id}, concurrency={concurrency}) …"
    )

    if backend == "transformers":
        _load_hf_model(model_id)
        for i, (clause, condition) in enumerate(tasks):
            result = await run_episode(
                clause, condition, model_id, backend, vllm_url, gen_params
            )
            with open(output_file, "a") as f:
                f.write(json.dumps(result, ensure_ascii=False) + "\n")
            if (i + 1) % 10 == 0 or (i + 1) == len(tasks):
                print(f"  [{i + 1}/{len(tasks)}] completed")
    else:
        semaphore = asyncio.Semaphore(concurrency)
        lock = asyncio.Lock()
        done_count = 0

        async def _run_one(clause, condition):
            nonlocal done_count
            async with semaphore:
                result = await run_episode(
                    clause, condition, model_id, backend, vllm_url, gen_params
                )
                async with lock:
                    with open(output_file, "a") as f:
                        f.write(json.dumps(result, ensure_ascii=False) + "\n")
                    done_count += 1
                    if done_count % 10 == 0 or done_count == len(tasks):
                        print(f"  [{done_count}/{len(tasks)}] completed")

        await asyncio.gather(
            *[_run_one(c, cond) for c, cond in tasks],
            return_exceptions=True,
        )

    print(f"Done. Results written to {output_file}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Run agent episodes using local open-source models."
    )
    p.add_argument("--clauses", required=True, help="Path to clauses JSON file.")
    p.add_argument(
        "--model", required=True, help="HuggingFace model ID (e.g. Qwen/Qwen3-32B)."
    )
    p.add_argument(
        "--backend",
        choices=["vllm", "transformers"],
        default="vllm",
        help="Inference backend (default: vllm).",
    )
    p.add_argument(
        "--vllm-url",
        default="http://localhost:8000/v1",
        help="vLLM server URL (default: http://localhost:8000/v1).",
    )
    p.add_argument(
        "--output",
        default=str(config.DEFAULT_OUTPUT_DIR),
        help="Output directory for episode results.",
    )
    p.add_argument(
        "--concurrency",
        type=int,
        default=config.DEFAULT_CONCURRENCY,
        help=f"Max concurrent requests for vLLM backend (default: {config.DEFAULT_CONCURRENCY}).",
    )
    p.add_argument("--resume", action="store_true", default=True)
    p.add_argument("--no-resume", action="store_false", dest="resume")
    p.add_argument("--temperature", type=float, default=None)
    p.add_argument("--max-tokens", type=int, default=None)
    return p.parse_args(argv)


def main(argv: list[str] | None = None):
    args = parse_args(argv)
    clauses = load_clauses(args.clauses)

    gen_params = dict(config_local.DEFAULT_GENERATION_PARAMS)
    if args.temperature is not None:
        gen_params["temperature"] = args.temperature
    if args.max_tokens is not None:
        gen_params["max_tokens"] = args.max_tokens

    asyncio.run(
        run_all(
            clauses=clauses,
            model_id=args.model,
            backend=args.backend,
            output_dir=Path(args.output),
            vllm_url=args.vllm_url,
            concurrency=args.concurrency,
            resume=args.resume,
            gen_params=gen_params,
        )
    )


if __name__ == "__main__":
    main()
