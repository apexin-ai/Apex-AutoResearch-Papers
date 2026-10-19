"""v002: Emphasize hidden verification — agent must implement full spec, not just pass smoke test.

Key insight from v001 failures: all failed tasks showed the visible test passing
(test_solution_imports_and_entry_point_is_callable PASSED) but the hidden suite failed.
The agent was stopping after the smoke test passed without implementing the full spec.
"""

import json
import os

import anthropic

MODEL = "claude-haiku-4-5"
MAX_STEPS = 10

SYSTEM_PROMPT = """You are a coding agent implementing Python functions from specifications.

CRITICAL INSIGHT: The visible test suite only contains a smoke test that checks if the function
is importable and callable. This smoke test will pass even with an empty or stub implementation.
However, there is a HIDDEN test suite that rigorously tests the actual correctness of your
implementation against the full specification.

Your goal: Implement the complete, correct specification in solution.py so that both the
visible smoke test AND the hidden correctness tests pass.

Strategy:
1. Read solution.py carefully — the docstring contains the COMPLETE specification
2. Read test_solution.py to understand what the smoke test checks
3. Implement the FULL specification from the docstring, not just enough to pass the smoke test
4. The function signature, return types, edge cases, and behavior must ALL match the spec exactly
5. Run the visible tests to confirm the smoke test passes (but this is NOT sufficient — you must
   implement the full spec regardless)

Key principles:
- An empty function body or stub will pass the smoke test but FAIL the hidden tests
- Read every detail of the docstring: parameter types, return types, edge cases, examples
- Implement ALL described behavior, including edge cases and error handling
- Use the exact libraries and approaches mentioned in the docstring
- Match return types exactly (e.g., if it says return a DataFrame, return a DataFrame)
- Handle all edge cases mentioned (e.g., empty inputs, boundary conditions)

Never modify test_solution.py or any other file.
"""


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    client = anthropic.Anthropic(base_url=os.environ.get("ANTHROPIC_BASE_URL") or None)

    # First, read both files to understand what we're working with
    solution_path = os.path.join(work_dir, "solution.py")
    test_path = os.path.join(work_dir, "test_solution.py")

    solution_content = tool_dispatch["read_file"]({"path": solution_path})
    test_content = tool_dispatch["read_file"]({"path": test_path})

    messages = [{
        "role": "user",
        "content": (
            f"Working directory: {work_dir}\n\n"
            f"Here is the current solution.py (which you must implement):\n"
            f"```python\n{solution_content}\n```\n\n"
            f"Here is test_solution.py (the visible smoke test):\n"
            f"```python\n{test_content}\n```\n\n"
            f"IMPORTANT: The visible test only checks that the function is importable and callable. "
            f"There is a HIDDEN test suite that tests the actual correctness of your implementation. "
            f"You MUST implement the complete specification from the docstring above.\n\n"
            f"Please implement the complete, correct specification in {solution_path}. "
            f"Read the docstring carefully — implement ALL described behavior including edge cases, "
            f"correct return types, and all parameter handling. Then run the visible tests to confirm "
            f"the smoke test passes."
        ),
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
                        # For run_tests, provide structured feedback
                        if block.name == "run_tests":
                            passed = result.get("passed", False)
                            stdout = result.get("stdout", "")
                            stderr = result.get("stderr", "")
                            feedback = f"Tests passed: {passed}\nSTDOUT:\n{stdout}"
                            if stderr:
                                feedback += f"\nSTDERR:\n{stderr}"
                            if passed:
                                feedback += (
                                    "\n\nNOTE: The visible smoke test passed. However, remember "
                                    "there is a HIDDEN test suite testing full correctness. "
                                    "Make sure your implementation is complete and correct per the spec."
                                )
                            result_str = feedback
                        else:
                            result_str = json.dumps(result, ensure_ascii=False)
                    else:
                        result_str = str(result)

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result_str[:4000],
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
