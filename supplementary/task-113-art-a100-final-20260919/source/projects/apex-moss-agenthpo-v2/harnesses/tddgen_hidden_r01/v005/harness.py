"""v005: Empirical verification via executable diagnostics.

Key insight: agents fail on hidden suites because they REASON about edge cases
instead of RUNNING them. Force the agent to write executable diagnostic code
that tests all docstring behaviors, catch failures empirically, then clean up.
"""

import json
import os

import anthropic

MODEL = "claude-haiku-4-5"
MAX_STEPS = 20

SYSTEM_PROMPT = """You are a coding agent. A working directory contains solution.py and test_solution.py.
Your goal: make ALL tests pass — both the visible test_solution.py AND a hidden final test suite.

CRITICAL FACTS:
1. The visible test checks ONE scenario. The hidden suite tests MANY more cases from the docstring.
2. You MUST empirically verify your implementation — do not just reason about correctness.
3. When you see a seeded random test failing, the expected values tell you EXACTLY which 
   random function/library to use. Try different approaches until you match the expected output.

WORKFLOW:
Phase 1 - Implement: Read files, implement solution, run visible test until it passes.
Phase 2 - Diagnose: Add a __main__ block to solution.py that tests ALL docstring edge cases.
          Run the tests (pytest ignores __main__) — but also run solution.py directly if needed.
Phase 3 - Fix & Clean: Fix any issues found, then remove the __main__ block, run tests again.

For random-seeded failures: The expected output was generated with ONE specific random call.
Try: random.shuffle, np.random.shuffle, random.sample — run them and compare outputs.

Never modify test_solution.py. Only edit solution.py.
"""

PHASE2_DIAGNOSTIC_PROMPT = """PHASE 2: The visible test passes. Now write and run diagnostic tests.

Add a `if __name__ == '__main__':` block to solution.py that explicitly tests:

1. **All documented exceptions**: Call the function with invalid inputs that should raise each 
   documented exception. Verify they raise the right exception TYPE.
   Example:
   ```python
   if __name__ == '__main__':
       import traceback
       # Test exception: invalid type
       try:
           task_func(invalid_input)
           print("FAIL: Should have raised ValueError")
       except ValueError as e:
           print(f"PASS: Got ValueError: {e}")
       except Exception as e:
           print(f"FAIL: Got wrong exception {type(e)}: {e}")
   ```

2. **All default parameter values**: Call with defaults, verify behavior matches docstring.

3. **Boundary conditions**: Empty inputs, None values, minimum/maximum values, etc.

4. **Return type verification**: Check isinstance() of return value.

5. **The exact visible test case**: Re-run it manually and verify exact output.

After adding the __main__ block, run the visible tests (they pass through pytest which ignores __main__).
Then look at whether your diagnostic logic would produce the right results.
If you find failures, fix solution.py, then in Phase 3 remove the __main__ block.
"""

PHASE3_CLEANUP_PROMPT = """PHASE 3: Fix any issues found and clean up.

1. Review all diagnostic results you found in Phase 2
2. Fix any issues in the implementation
3. Remove the `if __name__ == '__main__':` block from solution.py
4. Run the visible tests one final time to confirm they still pass
5. Do a final review: read solution.py and confirm every docstring behavior is implemented

Then you are done.
"""

STUCK_RANDOM_PROMPT = """You're struggling with a seeded random test. Here's how to debug it:

The test expects SPECIFIC output for a specific seed. This means the reference implementation
used ONE specific random function call. You need to find which one produces that output.

Strategy:
1. Add a __main__ block that tries DIFFERENT random approaches with the same seed:
   ```python
   if __name__ == '__main__':
       import random
       import numpy as np
       
       # Try approach 1: random.shuffle on list
       random.seed(42)  # or whatever seed
       items = [...]  # your items
       random.shuffle(items)
       print("random.shuffle:", items[:3])
       
       # Try approach 2: np.random.shuffle
       np.random.seed(42)
       items2 = [...]
       np.random.shuffle(items2)
       print("np.random.shuffle:", items2[:3])
       
       # Try approach 3: random.sample
       random.seed(42)
       items3 = random.sample([...], len([...]))
       print("random.sample:", items3[:3])
   ```
2. Run the tests — pytest ignores __main__ blocks
3. Compare outputs against the expected values from the test
4. Use whichever approach matches

Remember: the docstring may say which library to use — check it!
"""


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    client = anthropic.Anthropic(base_url=os.environ.get("ANTHROPIC_BASE_URL") or None)

    solution_path = os.path.join(work_dir, "solution.py")
    test_path = os.path.join(work_dir, "test_solution.py")

    # Read both files upfront
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
            f"=== solution.py (EDIT THIS FILE) ===\n{solution_content}\n\n"
            f"=== test_solution.py (READ ONLY - DO NOT MODIFY) ===\n{test_content}\n\n"
            f"CRITICAL IMPLEMENTATION NOTES:\n"
            f"1. The docstring defines ALL required behaviors - implement EVERY behavior\n"
            f"2. Check EXACTLY which random library/function is expected (random vs numpy)\n"
            f"3. Check whether ranges are inclusive or exclusive (off-by-one errors are common)\n"
            f"4. Implement ALL documented exceptions with EXACT exception types\n"
            f"5. Use exact default parameter values from the docstring\n"
            f"6. The hidden test suite will test EVERY behavior in the docstring\n\n"
            f"PHASE 1: Implement solution.py and run visible tests until they pass.\n"
            f"Use write_file to update solution.py and run_tests to verify.\n"
            f"When the visible test passes, I will give you Phase 2 instructions."
        ),
    }]

    total_tokens = 0
    step = 0
    visible_tests_passed = False
    phase2_injected = False
    phase3_injected = False
    consecutive_failures = 0
    stuck_random_injected = False

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
            # Agent stopped without tool use
            if not visible_tests_passed and step < MAX_STEPS - 3:
                messages.append({
                    "role": "user",
                    "content": (
                        "Please implement and test your solution. "
                        "Use write_file to update solution.py and run_tests to verify."
                    )
                })
                continue

            if visible_tests_passed and not phase2_injected and step < MAX_STEPS - 6:
                phase2_injected = True
                messages.append({
                    "role": "user",
                    "content": PHASE2_DIAGNOSTIC_PROMPT
                })
                continue

            if phase2_injected and not phase3_injected and step < MAX_STEPS - 2:
                phase3_injected = True
                messages.append({
                    "role": "user",
                    "content": PHASE3_CLEANUP_PROMPT
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
                        consecutive_failures = 0
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": (
                                f"VISIBLE TESTS PASSED:\n{result['stdout'][:2000]}"
                            ),
                        })
                    else:
                        consecutive_failures += 1
                        stdout = result["stdout"]
                        stderr = result["stderr"]

                        # Detect if it's a random/seed-related failure
                        is_random_failure = (
                            "seed" in stdout.lower() or
                            "reproducib" in stdout.lower() or
                            ("AssertionError" in stdout and "Lists differ" in stdout)
                        )

                        extra_hint = ""
                        if is_random_failure and not stuck_random_injected and consecutive_failures >= 2:
                            extra_hint = (
                                "\n\n⚠️ RANDOM SEED MISMATCH DETECTED: The test expects specific values "
                                "from a seeded random operation. You need to use the EXACT same random "
                                "function as the reference implementation. Check the docstring for hints "
                                "about which library (random vs numpy) to use. Try both and compare outputs."
                            )

                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": (
                                f"TESTS FAILED:\n"
                                f"stdout:\n{stdout[:2000]}\n"
                                f"stderr:\n{stderr[:500]}"
                                f"{extra_hint}"
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

        # Inject stuck-random prompt after 3+ consecutive failures with random issues
        if (consecutive_failures >= 3 and not stuck_random_injected
                and not visible_tests_passed and step < MAX_STEPS - 4):
            # Check if the failures seem random-related
            recent_failures_random = any(
                isinstance(msg.get("content"), list) and
                any(
                    isinstance(item, dict) and
                    "RANDOM SEED MISMATCH" in item.get("content", "")
                    for item in msg.get("content", [])
                )
                for msg in messages[-6:]
                if msg.get("role") == "user"
            )
            if recent_failures_random:
                stuck_random_injected = True
                messages.append({
                    "role": "user",
                    "content": STUCK_RANDOM_PROMPT
                })

        # Inject phase 2 after visible tests pass
        if visible_tests_passed and not phase2_injected and step < MAX_STEPS - 6:
            phase2_injected = True
            messages.append({
                "role": "user",
                "content": PHASE2_DIAGNOSTIC_PROMPT
            })

        # Inject phase 3 after phase 2 has been running for a few steps
        elif (phase2_injected and not phase3_injected
              and step >= MAX_STEPS - 7 and step < MAX_STEPS - 2):
            phase3_injected = True
            messages.append({
                "role": "user",
                "content": PHASE3_CLEANUP_PROMPT
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
