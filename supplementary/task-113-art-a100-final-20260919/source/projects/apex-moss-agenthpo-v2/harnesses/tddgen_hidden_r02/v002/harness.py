"""v002: adds a spec-review hardening phase after visible tests pass.

After the visible test passes, the model re-reads the docstring specification
and reasons about boundary conditions for the hidden test suite.
"""

import json
import os

import anthropic

MODEL = "claude-haiku-4-5"
MAX_STEPS = 20

SYSTEM_PROMPT = """You are a coding agent. A working directory contains solution.py and test_solution.py.
Your goal: make ALL tests pass — both the visible test and hidden tests in the final suite.

CRITICAL: The visible test_solution.py is INCOMPLETE FEEDBACK. It only tests one case.
The hidden final test suite tests many more cases based on the FULL SPECIFICATION in the docstring.

General strategy:
1. Read solution.py (docstring is the full specification) and test_solution.py
2. Understand ALL requirements from the docstring, not just what the visible test checks
3. Implement solution.py to satisfy the COMPLETE specification
4. Run tests to verify
5. After passing visible tests, review your implementation against ALL docstring requirements
6. Consider: edge cases, error handling, boundary values, type handling, return types, etc.

Never modify test_solution.py or any other file.
"""

HARDENING_PROMPT = """The visible test passes. But there is a HIDDEN test suite that tests the FULL specification.

Please now:
1. Re-read the solution.py docstring very carefully
2. List EVERY requirement mentioned (parameters, return values, error handling, edge cases, data types, formats)
3. Check your implementation against EACH requirement
4. Identify any gaps: things the docstring specifies but your implementation may not handle correctly
5. Fix any gaps you find
6. Re-run the tests to confirm nothing broke

Focus especially on:
- Input validation and error handling (what errors should be raised and when?)
- Boundary values and edge cases (empty inputs, None values, type mismatches)
- Exact output formats (column names, data types, value formats)
- Default parameter behavior
- Any numerical precision or ordering requirements
"""


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    client = anthropic.Anthropic(base_url=os.environ.get("ANTHROPIC_BASE_URL") or None)

    solution_path = os.path.join(work_dir, "solution.py")
    test_path = os.path.join(work_dir, "test_solution.py")

    # Initial user message
    messages = [{
        "role": "user",
        "content": (
            f"Working directory: {work_dir}\n"
            f"Make ALL tests pass (visible + hidden) by editing {solution_path} only.\n\n"
            f"IMPORTANT: The visible test only covers one case. The hidden suite tests the FULL spec.\n"
            f"Read the docstring in solution.py as the authoritative specification and implement ALL of it.\n\n"
            f"Use the available tools. Start by reading both files."
        ),
    }]

    total_tokens = 0
    step = 0
    visible_passed = False
    hardening_done = False

    for step in range(1, MAX_STEPS + 1):
        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            messages=messages,
            tools=tool_definitions,
        )
        total_tokens += response.usage.input_tokens + response.usage.output_tokens

        # Check actual content blocks for tool_use, regardless of stop_reason
        tool_use_blocks = [block for block in response.content if block.type == "tool_use"]
        has_tool_use = len(tool_use_blocks) > 0

        messages.append({"role": "assistant", "content": response.content})

        if has_tool_use:
            # Always process tool_use blocks and return tool_results
            tool_results = []

            for block in response.content:
                if block.type == "tool_use":
                    # Hard-block write_file calls to any path other than solution_path
                    if block.name == "write_file":
                        requested_path = block.input.get("path", "")
                        if requested_path != solution_path:
                            tool_results.append({
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": (
                                    f"Blocked: write_file is only permitted for "
                                    f"{solution_path}. "
                                    f"Attempted path '{requested_path}' was not written."
                                ),
                                "is_error": True,
                            })
                            continue

                    try:
                        result = tool_dispatch[block.name](block.input)

                        # Check if tests passed
                        if block.name == "run_tests":
                            if isinstance(result, dict) and result.get("passed"):
                                visible_passed = True
                            result_str = json.dumps(result, ensure_ascii=False)
                        elif isinstance(result, dict):
                            result_str = json.dumps(result, ensure_ascii=False)
                        else:
                            result_str = str(result)

                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result_str[:3000],
                        })
                    except Exception as e:
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": f"Error: {e}",
                            "is_error": True,
                        })

            # After tests pass, inject hardening prompt alongside tool results
            if visible_passed and not hardening_done:
                hardening_done = True
                messages.append({"role": "user", "content": tool_results})
                messages.append({
                    "role": "user",
                    "content": HARDENING_PROMPT
                })
            else:
                messages.append({"role": "user", "content": tool_results})

        else:
            # No tool_use blocks in content — model finished a text-only turn
            if not visible_passed:
                messages.append({
                    "role": "user",
                    "content": "Please run the tests to verify your implementation."
                })
            elif not hardening_done:
                hardening_done = True
                messages.append({
                    "role": "user",
                    "content": HARDENING_PROMPT
                })
            else:
                # Done — model finished text-only with tests passed and hardening done
                break

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
