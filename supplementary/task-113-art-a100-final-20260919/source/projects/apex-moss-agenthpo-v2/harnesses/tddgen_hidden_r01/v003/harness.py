"""v003: Explicit boundary testing phase after visible test passes.

After the visible test passes, force the agent to extract all documented edge cases
from the docstring and verify them with explicit test code, catching hidden suite gaps.
"""

import json
import os

import anthropic

MODEL = "claude-haiku-4-5"
MAX_STEPS = 14

SYSTEM_PROMPT = """You are a coding agent. A working directory contains solution.py and test_solution.py.
Your goal: make ALL tests pass — both the visible test_solution.py AND a hidden final test suite.

CRITICAL FACTS:
1. The visible test only checks ONE scenario. The hidden suite tests MANY more cases.
2. The hidden suite tests every behavior documented in solution.py's docstring.
3. You must implement the COMPLETE specification — every parameter, exception, edge case.

Strategy:
1. Read solution.py carefully — the docstring IS the full specification
2. Read test_solution.py to see one example
3. Implement the complete spec
4. Run the visible test to verify
5. Verify additional docstring edge cases by adding a temporary __main__ block to solution.py
6. Fix any gaps, then remove the __main__ block

Never modify test_solution.py. Only edit solution.py.
"""

BOUNDARY_TEST_PROMPT = """The visible test is passing. Now you must verify ALL edge cases from the specification.

Do the following:
1. Re-read solution.py's docstring completely
2. Add a temporary `if __name__ == '__main__':` block at the bottom of solution.py that tests:
   - Each documented exception (wrong input types, invalid values) — verify they raise correctly
   - Each documented parameter with its default value
   - Boundary conditions (empty inputs, None, wrong types, min/max values)
   - The exact return type and structure documented
   - Any specific examples given in the docstring
3. Run the visible tests again (they will ignore the __main__ block)
4. Also mentally trace through your __main__ block — if any case would fail, fix solution.py now
5. Once satisfied, remove the __main__ block from solution.py and run the tests one final time

This is critical — the hidden test suite checks all of these cases.
"""

FINAL_REVIEW_PROMPT = """Before finishing, do one final check:

1. Re-read the ENTIRE docstring of the main function in solution.py
2. List every "Raises:" entry and confirm each is implemented with the exact exception type
3. List every parameter and confirm default values are correct
4. Confirm the return type matches exactly what's documented
5. If you find any gaps, fix them now.

Only respond with "DONE" if everything matches the specification perfectly.
"""


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    client = anthropic.Anthropic(base_url=os.environ.get("ANTHROPIC_BASE_URL") or None)

    solution_path = os.path.join(work_dir, "solution.py")
    test_path = os.path.join(work_dir, "test_solution.py")

    messages = [{
        "role": "user",
        "content": (
            f"Working directory: {work_dir}\n\n"
            f"This task has a HIDDEN test suite that checks many more cases than the visible test.\n"
            f"You must implement the COMPLETE specification from solution.py's docstring.\n\n"
            f"Start by reading solution.py to understand the FULL specification, "
            f"then read test_solution.py to see the visible test.\n"
            f"Implement solution.py to satisfy ALL documented behaviors.\n\n"
            f"Files:\n"
            f"- {solution_path} (edit this only)\n"
            f"- {test_path} (read only)\n\n"
            f"Pay special attention to:\n"
            f"- All documented exceptions and when they're raised\n"
            f"- Default parameter values\n"
            f"- Exact return types and data structures\n"
            f"- Any specific algorithms or libraries specified (e.g., exact random functions)"
        ),
    }]

    total_tokens = 0
    step = 0
    visible_tests_passed = False
    boundary_test_injected = False
    final_review_injected = False

    for step in range(1, MAX_STEPS + 1):
        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            messages=messages,
            tools=tool_definitions,
        )
        total_tokens += response.usage.input_tokens + response.usage.output_tokens

        # Check for tool_use blocks in response.content authoritatively,
        # regardless of stop_reason.
        tool_use_blocks = [block for block in response.content if block.type == "tool_use"]
        has_tool_use = len(tool_use_blocks) > 0

        if not has_tool_use:
            # No tool use blocks — purely text response
            messages.append({"role": "assistant", "content": response.content})

            # Inject boundary test phase after tests pass
            if visible_tests_passed and not boundary_test_injected and step < MAX_STEPS - 4:
                boundary_test_injected = True
                messages.append({
                    "role": "user",
                    "content": BOUNDARY_TEST_PROMPT
                })
                continue

            # Inject final review after boundary tests
            if boundary_test_injected and not final_review_injected and step < MAX_STEPS - 1:
                final_review_injected = True
                messages.append({
                    "role": "user",
                    "content": FINAL_REVIEW_PROMPT
                })
                continue

            break

        # Has tool_use blocks — must process ALL of them and return tool_results
        messages.append({"role": "assistant", "content": response.content})
        tool_results = []

        for block in response.content:
            if block.type != "tool_use":
                continue

            # Contract fix (2): for write_file, only allow exact solution_path
            if block.name == "write_file":
                requested_path = block.input.get("path", "")
                if requested_path != solution_path:
                    # Block the write — do not dispatch
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": (
                            f"BLOCKED: write_file is only allowed to '{solution_path}'. "
                            f"Writing to '{requested_path}' is not permitted."
                        ),
                        "is_error": True,
                    })
                    continue

            try:
                result = tool_dispatch[block.name](block.input)

                if block.name == "run_tests":
                    if result["passed"]:
                        visible_tests_passed = True
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": f"VISIBLE TESTS PASSED:\n{result['stdout'][:2000]}",
                        })
                    else:
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": (
                                f"TESTS FAILED:\n"
                                f"stdout:\n{result['stdout'][:1500]}\n"
                                f"stderr:\n{result['stderr'][:500]}"
                            ),
                        })
                else:
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

        # Inject boundary test phase after tests pass (mid-loop)
        if visible_tests_passed and not boundary_test_injected and step < MAX_STEPS - 4:
            boundary_test_injected = True
            messages.append({
                "role": "user",
                "content": BOUNDARY_TEST_PROMPT
            })

        # Inject final review after boundary test phase is done
        elif boundary_test_injected and not final_review_injected and step >= MAX_STEPS - 4:
            final_review_injected = True
            messages.append({
                "role": "user",
                "content": FINAL_REVIEW_PROMPT
            })

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
