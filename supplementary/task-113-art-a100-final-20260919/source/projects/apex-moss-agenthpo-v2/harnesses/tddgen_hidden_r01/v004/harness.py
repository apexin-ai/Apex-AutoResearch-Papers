"""v004: Diagnosis-first approach — extract expected values from visible test before implementing.

Key insight from failures:
- bigcodebench_120: Random seed produces wrong shuffle order — agent uses wrong range 
  (exclusive vs inclusive end date) or wrong random function
- bigcodebench_458: Passes visible test but fails hidden suite — spec not fully implemented
- bigcodebench_1057: Passes visible test but fails hidden suite — spec not fully implemented

Strategy: After reading both files, explicitly extract expected outputs from the test,
then verify the implementation produces exactly those outputs before declaring success.
"""

import json
import os

import anthropic

MODEL = "claude-haiku-4-5"
MAX_STEPS = 16

SYSTEM_PROMPT = """You are a coding agent. A working directory contains solution.py and test_solution.py.
Your goal: make ALL tests pass — both the visible test_solution.py AND a hidden final test suite.

CRITICAL FACTS:
1. The visible test only checks ONE scenario. The hidden suite tests MANY more cases.
2. The hidden suite tests every behavior documented in solution.py's docstring.
3. You must implement the COMPLETE specification — every parameter, exception, edge case.
4. When tests fail with wrong output values, the error often comes from subtle bugs:
   - Off-by-one errors in ranges (exclusive vs inclusive end)
   - Wrong random library/function (np.random vs random module)
   - Wrong date formatting
   - Incorrect handling of edge cases

DEBUGGING APPROACH when tests fail:
- Look at the EXACT expected values in the test
- Trace through your implementation step by step
- Check if ranges are inclusive or exclusive
- Verify which random module is imported in the stub
- Try small examples mentally before writing code

Never modify test_solution.py. Only edit solution.py.
"""

ANALYSIS_PROMPT = """Now analyze the test file carefully to understand EXACTLY what's expected.

Look for:
1. What are the exact hardcoded expected values in the test? (e.g., exact list contents, exact numbers)
2. What seed value is used? What random function/module does the expected output imply?
3. What date range is used? Is the end date inclusive or exclusive?
4. What exact format are outputs in?

Then trace through your implementation with the test's exact inputs to verify you'd 
produce those exact outputs. If there's a mismatch, identify WHY and fix it.

For random-seeded tests: the expected output was generated with a specific random 
function call. You must use the SAME function (same library, same way of calling it).
Check the solution.py docstring for hints about which library to use.
"""

HIDDEN_SUITE_PROMPT = """The visible test passes. Now verify coverage for the hidden test suite.

The hidden suite will test EVERY behavior in the docstring. Go through each section:

**Raises section**: For EACH documented exception:
- What input triggers it?
- Is your code raising it for exactly that input?
- Is it the right exception TYPE?

**Parameters section**: For EACH parameter:
- What's the default value? Does your code use that exact default?
- What types are accepted? Does your code handle all of them?

**Returns section**:
- What's the exact return type?
- What's the structure/format?

**Examples in docstring**:
- Run each example mentally through your code
- Would you get the exact output shown?

If you find ANY gap, fix it immediately.
"""


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    client = anthropic.Anthropic(base_url=os.environ.get("ANTHROPIC_BASE_URL") or None)

    solution_path = os.path.join(work_dir, "solution.py")
    test_path = os.path.join(work_dir, "test_solution.py")

    # Read both files upfront so the agent has full context immediately
    try:
        solution_content = tool_dispatch["read_file"]({"path": solution_path})
    except Exception:
        solution_content = "(could not read solution.py)"

    try:
        test_content = tool_dispatch["read_file"]({"path": test_path})
    except Exception:
        test_content = "(could not read test_solution.py)"

    messages = [{
        "role": "user",
        "content": (
            f"Working directory: {work_dir}\n\n"
            f"This task has a HIDDEN test suite that checks many more cases than the visible test.\n"
            f"You must implement the COMPLETE specification from solution.py's docstring.\n\n"
            f"Here are both files for your reference:\n\n"
            f"=== solution.py (EDIT THIS FILE) ===\n{solution_content}\n\n"
            f"=== test_solution.py (READ ONLY - DO NOT MODIFY) ===\n{test_content}\n\n"
            f"IMPORTANT NOTES:\n"
            f"1. Read the docstring VERY carefully - it defines ALL required behaviors\n"
            f"2. Look at the exact expected values in the test - they tell you the EXACT algorithm needed\n"
            f"3. Pay attention to which random library/function is implied by the expected output\n"
            f"4. Check if date ranges are inclusive or exclusive (off-by-one is a common bug)\n"
            f"5. Implement ALL documented exceptions with the EXACT exception types specified\n"
            f"6. Use exact default parameter values from the docstring\n\n"
            f"Now implement solution.py to satisfy ALL documented behaviors."
        ),
    }]

    total_tokens = 0
    step = 0
    visible_tests_passed = False
    analysis_injected = False
    hidden_suite_check_injected = False
    consecutive_pass_count = 0

    for step in range(1, MAX_STEPS + 1):
        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            messages=messages,
            tools=tool_definitions,
        )
        total_tokens += response.usage.input_tokens + response.usage.output_tokens

        tool_use_blocks = [block for block in response.content if block.type == "tool_use"]
        has_tool_use = len(tool_use_blocks) > 0

        messages.append({"role": "assistant", "content": response.content})

        if not has_tool_use:
            # No tool use — agent is done or thinking
            
            # If we haven't passed visible tests yet, encourage continuation
            if not visible_tests_passed and step < MAX_STEPS - 2:
                messages.append({
                    "role": "user",
                    "content": (
                        "Please write and test your implementation. "
                        "Use write_file to update solution.py and run_tests to verify."
                    )
                })
                continue

            # If tests passed but we haven't done hidden suite check, inject it
            if visible_tests_passed and not hidden_suite_check_injected and step < MAX_STEPS - 2:
                hidden_suite_check_injected = True
                messages.append({
                    "role": "user",
                    "content": HIDDEN_SUITE_PROMPT
                })
                continue

            break

        # Process tool calls
        tool_results = []

        for block in response.content:
            if block.type != "tool_use":
                continue

            # Block writes to files other than solution.py
            if block.name == "write_file":
                requested_path = block.input.get("path", "")
                if requested_path != solution_path:
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": (
                            f"BLOCKED: write_file is only allowed to '{solution_path}'. "
                            f"Writing to '{requested_path}' is not permitted. "
                            f"Only solution.py may be modified."
                        ),
                        "is_error": True,
                    })
                    continue

            try:
                result = tool_dispatch[block.name](block.input)

                if block.name == "run_tests":
                    if result["passed"]:
                        visible_tests_passed = True
                        consecutive_pass_count += 1
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": (
                                f"VISIBLE TESTS PASSED:\n{result['stdout'][:2000]}\n\n"
                                f"Good! Now verify the hidden test suite coverage."
                            ),
                        })
                    else:
                        consecutive_pass_count = 0
                        # Provide detailed failure info to help debugging
                        stdout = result["stdout"]
                        stderr = result["stderr"]
                        
                        # Extract the assertion error if present for better diagnosis
                        failure_detail = ""
                        if "AssertionError" in stdout:
                            lines = stdout.split("\n")
                            for i, line in enumerate(lines):
                                if "AssertionError" in line or "First differing" in line:
                                    failure_detail = "\n".join(lines[max(0, i-2):min(len(lines), i+5)])
                                    break
                        
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": (
                                f"TESTS FAILED:\n"
                                f"stdout:\n{stdout[:2000]}\n"
                                f"stderr:\n{stderr[:500]}\n\n"
                                f"DEBUGGING HINTS:\n"
                                f"- If you see wrong values with a seed, check which random function is used\n"
                                f"- If list length is wrong, check inclusive vs exclusive range boundaries\n"
                                f"- Compare your logic step-by-step against what the test expects"
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

        # After tests fail multiple times, inject analysis prompt to help debug
        if (not visible_tests_passed and not analysis_injected 
                and step >= 3 and step < MAX_STEPS - 4):
            # Check if we've seen test failures (agent tried but failed)
            has_failed_tests = any(
                isinstance(msg.get("content"), list) and
                any(
                    isinstance(item, dict) and 
                    "TESTS FAILED" in item.get("content", "")
                    for item in msg.get("content", [])
                )
                for msg in messages
                if msg.get("role") == "user"
            )
            if has_failed_tests:
                analysis_injected = True
                messages.append({
                    "role": "user",
                    "content": ANALYSIS_PROMPT
                })

        # Inject hidden suite check after tests pass
        if visible_tests_passed and not hidden_suite_check_injected and step < MAX_STEPS - 2:
            hidden_suite_check_injected = True
            messages.append({
                "role": "user",
                "content": HIDDEN_SUITE_PROMPT
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
