"""v002: specification-first harness that emphasizes full spec compliance over just passing visible tests.

Changes from v001:
- Stronger system prompt emphasizing full specification compliance
- Explicit multi-phase workflow: read spec → reason about ALL cases → implement → test → reflect
- Forces the model to enumerate boundary conditions from docstring before coding
- Warns explicitly against tampering with test files
"""

import json
import os

import anthropic

MODEL = "claude-haiku-4-5"
MAX_STEPS = 12

SYSTEM_PROMPT = """You are a coding agent. A working directory contains solution.py and test_solution.py.
Your goal: make ALL tests pass — both the visible test AND any hidden tests — by editing solution.py ONLY.

CRITICAL RULES:
- NEVER modify test_solution.py or any other file. Only edit solution.py.
- Tampering with test files will cause automatic failure with score 0.
- The visible test is INCOMPLETE feedback — there are hidden tests testing edge cases and boundary conditions.

Your strategy MUST follow these phases in order:

PHASE 1 - READ EVERYTHING:
  - Read solution.py to understand the full docstring/specification
  - Read test_solution.py to understand the visible test cases

PHASE 2 - REASON ABOUT THE FULL SPECIFICATION:
  Before writing any code, explicitly think about:
  - What does the docstring say the function must do?
  - What are ALL the input types mentioned?
  - What validation/errors should be raised and when?
  - What are the exact output types, formats, and shapes?
  - What are the boundary/edge cases implied by the spec?
  - What default values exist and how do they behave?
  - Are there any notes about reproducibility, seeds, or ordering?

PHASE 3 - IMPLEMENT:
  - Write a complete implementation that handles ALL cases in the spec
  - Do not just implement what the visible test checks — implement the FULL specification

PHASE 4 - VERIFY:
  - Run the tests
  - If tests fail, re-read the spec and fix

PHASE 5 - REFLECT:
  - After tests pass, re-read the docstring one more time
  - Ask yourself: "Are there any spec requirements my implementation might miss in hidden tests?"
  - If yes, fix them even if the visible test still passes

Focus on specification completeness, not just making the visible test green.
"""


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    client = anthropic.Anthropic(base_url=os.environ.get("ANTHROPIC_BASE_URL") or None)

    solution_path = os.path.join(work_dir, "solution.py")
    test_path = os.path.join(work_dir, "test_solution.py")

    # Read both files upfront to provide full context immediately
    try:
        solution_content = tool_dispatch["read_file"]({"path": solution_path})
    except Exception as e:
        solution_content = f"Error reading solution.py: {e}"

    try:
        test_content = tool_dispatch["read_file"]({"path": test_path})
    except Exception as e:
        test_content = f"Error reading test_solution.py: {e}"

    # Run tests first to see baseline failures
    try:
        initial_test_result = tool_dispatch["run_tests"]({"test_path": test_path})
        initial_test_output = initial_test_result["stdout"] + initial_test_result["stderr"]
        initial_passed = initial_test_result["passed"]
    except Exception as e:
        initial_test_output = f"Error running tests: {e}"
        initial_passed = False

    initial_context = f"""Working directory: {work_dir}

I've already read the files for you. Here is their content:

=== solution.py ===
{solution_content}

=== test_solution.py ===
{test_content}

=== Initial test run ===
{initial_test_output}

Now follow the phases described in your instructions:

PHASE 2: Before writing any code, reason carefully about the FULL specification in the solution.py docstring. List ALL:
- Input parameters and their types/constraints
- Validation rules and exceptions that must be raised
- Exact output format, type, shape
- Edge cases and boundary conditions
- Default parameter behaviors
- Any special notes (seeds, reproducibility, inclusive/exclusive ranges, etc.)

IMPORTANT: The visible test is INCOMPLETE. Hidden tests will check edge cases from the spec.
Only edit solution.py — NEVER touch test_solution.py.

Then implement the complete solution and verify it passes tests."""

    messages = [{"role": "user", "content": initial_context}]

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
                # Safety check: prevent writing to test file
                if block.name == "write_file":
                    file_path = block.input.get("path", "")
                    if "test_solution" in file_path:
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": "ERROR: You are NOT allowed to modify test_solution.py. Only edit solution.py. This would cause automatic failure.",
                            "is_error": True,
                        })
                        continue

                try:
                    result = tool_dispatch[block.name](block.input)
                    if isinstance(result, dict):
                        # For test results, provide structured feedback
                        if block.name == "run_tests":
                            passed = result.get("passed", False)
                            stdout = result.get("stdout", "")
                            stderr = result.get("stderr", "")
                            feedback = f"Tests {'PASSED' if passed else 'FAILED'}\n\nSTDOUT:\n{stdout}"
                            if stderr:
                                feedback += f"\nSTDERR:\n{stderr}"
                            if passed:
                                feedback += "\n\nNow do PHASE 5: Re-read the docstring in solution.py and check if hidden tests might catch any spec requirements your implementation misses. Fix any gaps even if the visible test passes."
                            tool_results.append({
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": feedback[:3000],
                            })
                        else:
                            tool_results.append({
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": json.dumps(result, ensure_ascii=False)[:3000],
                            })
                    else:
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
