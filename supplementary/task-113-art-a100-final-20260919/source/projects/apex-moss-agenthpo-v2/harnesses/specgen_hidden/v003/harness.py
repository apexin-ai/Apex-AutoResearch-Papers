"""v003: Two-phase spec-first implementation with self-verification.

Phase 1: Read solution.py docstring carefully, implement full spec
Phase 2: Mentally verify edge cases before finalizing
Key insight: visible tests only check callability; hidden tests check full correctness.
"""

import json
import os

import anthropic

MODEL = "claude-haiku-4-5"
MAX_STEPS = 14

SYSTEM_PROMPT = """You are an expert Python developer implementing functions from specifications.

CRITICAL CONTEXT:
- The visible test suite ONLY checks that the function is importable and callable
- There is a HIDDEN test suite that rigorously tests actual correctness
- An empty function or stub WILL PASS the visible test but FAIL the hidden tests
- You MUST implement the complete, correct specification

YOUR WORKFLOW:
1. Read the solution.py docstring VERY carefully - it contains the COMPLETE spec
2. Note ALL of: parameter types, return types, edge cases, examples, constants, imports
3. Implement the FULL specification - every detail matters
4. Review your implementation mentally against all edge cases in the spec
5. Fix any issues found
6. Run the visible tests to confirm smoke test passes

IMPLEMENTATION PRINCIPLES:
- Use EXACTLY the imports listed in the "You should write self-contained code starting with:" section
- Match return types EXACTLY (DataFrame vs dict vs list vs float etc.)
- Handle ALL edge cases mentioned (empty inputs, boundary conditions, error cases)
- Use the EXACT constants/defaults shown in the function signature
- If the spec shows example outputs, your function must produce those exact outputs
- Pay attention to: sorting, column names, index types, data types, precision

IMPORTANT: You may only write to solution.py. Do not write to any other file.
Never modify test_solution.py or any file other than solution.py.
"""


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    client = anthropic.Anthropic(base_url=os.environ.get("ANTHROPIC_BASE_URL") or None)

    # Pre-read both files to provide full context upfront
    solution_path = os.path.join(work_dir, "solution.py")
    test_path = os.path.join(work_dir, "test_solution.py")

    solution_content = tool_dispatch["read_file"]({"path": solution_path})
    test_content = tool_dispatch["read_file"]({"path": test_path})

    messages = [{
        "role": "user",
        "content": (
            f"Working directory: {work_dir}\n\n"
            f"## solution.py (you must implement this completely)\n"
            f"```python\n{solution_content}\n```\n\n"
            f"## test_solution.py (visible smoke test - will ALWAYS pass if function is callable)\n"
            f"```python\n{test_content}\n```\n\n"
            f"## YOUR TASK\n"
            f"Implement the COMPLETE specification in solution.py. The visible test only checks "
            f"that `task_func` is importable and callable - it tells you NOTHING about correctness. "
            f"There is a hidden test suite that will test the actual behavior.\n\n"
            f"STEP 1: Carefully read the docstring above and identify:\n"
            f"- All parameters and their types/defaults\n"
            f"- The exact return type and structure\n"
            f"- All edge cases mentioned\n"
            f"- Any examples or expected outputs\n"
            f"- Required imports (use the 'starting with:' code block exactly)\n\n"
            f"STEP 2: Write the complete implementation to {solution_path}\n\n"
            f"STEP 3: Review your implementation carefully against the spec, checking all edge "
            f"cases and return type details.\n\n"
            f"STEP 4: Fix any issues found during review by updating {solution_path}\n\n"
            f"STEP 5: Run the visible tests to confirm smoke test passes\n\n"
            f"IMPORTANT: You may only write to solution.py. Do not create or write to any other file.\n\n"
            f"Be thorough - the hidden tests will check every detail of your implementation."
        ),
    }]

    total_tokens = 0
    step = 0
    smoke_passed = False

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
            # If smoke test hasn't passed yet, nudge the model
            if not smoke_passed and step < MAX_STEPS:
                messages.append({
                    "role": "user",
                    "content": (
                        "Please run the visible tests with run_tests to confirm your "
                        "implementation is complete."
                    )
                })
                continue
            break

        messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                try:
                    raw_result = tool_dispatch[block.name](block.input)

                    if block.name == "run_tests":
                        # raw_result is a dict
                        passed = raw_result.get("passed", False)
                        stdout = raw_result.get("stdout", "")
                        stderr = raw_result.get("stderr", "")
                        returncode = raw_result.get("returncode", -1)

                        if passed:
                            smoke_passed = True
                            feedback = (
                                f"Tests PASSED (returncode={returncode})\n"
                                f"STDOUT:\n{stdout}\n"
                                f"NOTE: The visible smoke test passed. "
                                f"However, this only confirms the function is callable. "
                                f"The hidden tests check full correctness. "
                                f"Review your implementation once more against the spec to ensure "
                                f"all edge cases are handled correctly."
                            )
                        else:
                            feedback = (
                                f"Tests FAILED (returncode={returncode})\n"
                                f"STDOUT:\n{stdout}\n"
                                f"STDERR:\n{stderr}\n"
                                f"Fix the import/syntax errors so the function is at least callable."
                            )
                        result_str = feedback
                    elif block.name == "write_file":
                        result_str = str(raw_result)
                    elif block.name == "read_file":
                        result_str = str(raw_result)
                    elif isinstance(raw_result, dict):
                        result_str = json.dumps(raw_result, ensure_ascii=False)
                    else:
                        result_str = str(raw_result)

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result_str[:5000],
                    })
                except Exception as e:
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": f"Error executing {block.name}: {e}",
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
