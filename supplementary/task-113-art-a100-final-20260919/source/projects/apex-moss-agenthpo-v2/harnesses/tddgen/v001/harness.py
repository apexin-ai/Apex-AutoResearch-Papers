"""v001: deliberately plain generic harness — evolution starting point and control arm.

The improver may change the workflow (prompts, step policy, retries, context)
but NOT: the MODEL line, the run() signature, or anything outside this file.
"""

import json
import os

import anthropic

MODEL = "claude-haiku-4-5"
MAX_STEPS = 10

SYSTEM_PROMPT = """You are a coding agent. A working directory contains solution.py and test_solution.py.
Your goal: make all tests in test_solution.py pass by editing solution.py ONLY.

General strategy:
1. Read solution.py and test_solution.py
2. Understand what the tests expect
3. Edit solution.py
4. Run the tests to verify

Never modify test_solution.py or any other file.
"""


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    client = anthropic.Anthropic(base_url=os.environ.get("ANTHROPIC_BASE_URL") or None)
    messages = [{
        "role": "user",
        "content": f"Working directory: {work_dir}\n"
                   f"Make the tests in {work_dir}/test_solution.py pass by editing "
                   f"{work_dir}/solution.py only. Use the available tools.",
    }]

    total_tokens = 0
    step = 0

    for step in range(1, MAX_STEPS + 1):
        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            messages=messages,
            tools=tool_definitions,
        )
        total_tokens += response.usage.input_tokens + response.usage.output_tokens

        if response.stop_reason != "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            break

        messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                try:
                    result = tool_dispatch[block.name](block.input)
                    if isinstance(result, dict):
                        result = json.dumps(result, ensure_ascii=False)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(result)[:3000],
                    })
                except Exception as e:
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": f"Error: {e}",
                        "is_error": True,
                    })
        messages.append({"role": "user", "content": tool_results})

    return {"steps": step, "tokens": total_tokens, "messages": _serialize(messages)}


def _serialize(messages):
    out = []
    for msg in messages:
        if isinstance(msg.get("content"), list):
            content = []
            for item in msg["content"]:
                if hasattr(item, "model_dump"):
                    content.append(item.model_dump())
                elif isinstance(item, dict):
                    content.append(item)
                else:
                    content.append(str(item))
            out.append({"role": msg["role"], "content": content})
        else:
            out.append(msg)
    return out
