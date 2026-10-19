"""v006: Forced executable spec-verification after visible test passes.

Key insight from v005: bigcodebench_458 always passes visible test but fails hidden suite.
The agent reasons about correctness but doesn't empirically verify all spec behaviors.
Force the agent to write concrete executable assertions for EVERY docstring behavior.
"""

import json
import os

import anthropic

MODEL = "claude-haiku-4-5"
MAX_STEPS = 20

SYSTEM_PROMPT = """You are a coding agent. A working directory contains solution.py and test_solution.py.
Your goal: make ALL tests pass — both the visible test_solution.py AND a hidden final test suite.

CRITICAL FACTS:
1. The visible test checks ONE scenario. The hidden suite tests MANY more cases.
2. The hidden suite tests EVERY behavior documented in solution.py's docstring.
3. You MUST empirically verify — do not just reason about correctness.
4. When seeded random tests fail: the expected output was generated with ONE specific function.
   Try different random libraries/functions until you match the exact expected values.

WORKFLOW:
Phase 1: Read files → implement solution → run visible test until it passes.
Phase 2: Write executable assertions for EVERY docstring behavior as a __main__ block.
         Run the tests (pytest ignores __main__). Fix any issues found.
Phase 3: Remove __main__ block, run final tests.

Never modify test_solution.py. Only edit solution.py.
"""

PHASE2_PROMPT = """PHASE 2: The visible test passes. Now you must write executable assertions for EVERY 
behavior documented in the docstring.

Add a `if __name__ == '__main__':` block to solution.py that contains CONCRETE assertions 
(using assert statements or try/except) for each of the following categories:

1. **Exception Handling** - For EACH "Raises:" entry in the docstring:
   - Write code that calls the function with the invalid input
   - Assert the EXACT exception type is raised
   - Test with multiple invalid inputs if applicable
   Example:
   ```python
   try:
       task_func("not_a_list")  # should raise TypeError
       print("FAIL: should have raised TypeError")
   except TypeError:
       print("PASS: TypeError raised correctly")
   except Exception as e:
       print(f"FAIL: wrong exception type {type(e).__name__}: {e}")
   ```

2. **Default Parameters** - Call with ONLY defaults, verify return type and structure.

3. **Return Type** - Check isinstance() of actual return value matches documented type.

4. **Boundary Inputs**:
   - Empty collections (empty list, empty dict, empty string)
   - None values for optional parameters  
   - Single-element inputs
   - Large inputs

5. **Specific documented behaviors** - Re-read the docstring and for each specific behavior 
   described, write an assertion that tests it.

6. **Data format** - Verify the exact format of returned data (column names, dtypes, structure).

After writing the __main__ block, run the visible tests again (pytest ignores __main__).
Then examine your assertions carefully — if ANY would fail, fix the implementation NOW.
"""

PHASE3_PROMPT = """PHASE 3: Fix and clean up.

1. Review everything you found in Phase 2
2. Fix any remaining issues
3. Remove the `if __name__ == '__main__':` block from solution.py  
4. Run the visible tests one final time to confirm they pass
5. Final check: re-read the ENTIRE docstring and confirm:
   - Every "Raises:" is implemented with the exact exception type
   - Every parameter default value is correct
   - Return type matches exactly
   - All edge cases are handled
"""

INTERVENTION_PROMPT = """You've been running for many steps. Let's refocus.

The visible test is passing but the hidden suite likely checks:
1. Exception types for invalid inputs (must match EXACTLY — TypeError vs ValueError matters)
2. Default parameter values (must match EXACTLY what's in the docstring)
3. Return value format/structure (exact column names, dtypes, shapes)
4. Edge cases (None inputs, empty inputs, boundary values)

Re-read the docstring RIGHT NOW and list every "Raises:" entry, every parameter with its 
default, and the return type. Then check your implementation handles each one.

If you haven't already, add a __main__ block with concrete assertions and reason through
whether each assertion would pass.
"""


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    client = anthropic.Anthropic(base_url=os.environ.get("ANTHROPIC_BASE_URL") or None)

    solution_path = os.path.join(work_dir, "solution.py")
    test_path = os.path.join(work_dir, "test_solution.py")

    # Read both files upfront to give full context immediately
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
            f"IMPLEMENTATION REQUIREMENTS:\n"
            f"1. Read the docstring COMPLETELY — every behavior documented must be implemented\n"
            f"2. For 'Raises:' sections: implement EVERY exception with the EXACT type documented\n"
            f"3. Default parameter values must match the docstring EXACTLY\n"
            f"4. Return type and structure must match the docstring EXACTLY\n"
            f"5. Check which random library is implied (random vs numpy) for seeded tests\n"
            f"6. Check if ranges are inclusive or exclusive for boundary conditions\n\n"
            f"PHASE 1: Implement solution.py and run visible tests until they pass.\n"
            f"When the visible test passes, I will give you Phase 2 instructions."
        ),
    }]

    total_tokens = 0
    step = 0
    visible_tests_passed = False
    phase2_injected = False
    phase3_injected = False
    intervention_injected = False
    consecutive_failures = 0
    total_test_runs = 0

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
            # Agent stopped without tool use — nudge it forward
            if not visible_tests_passed and step < MAX_STEPS - 4:
                messages.append({
                    "role": "user",
                    "content": (
                        "Please implement and test your solution. "
                        "Use write_file to update solution.py and run_tests to verify."
                    )
                })
                continue

            if visible_tests_passed and not phase2_injected and step < MAX_STEPS - 7:
                phase2_injected = True
                messages.append({
                    "role": "user",
                    "content": PHASE2_PROMPT
                })
                continue

            if phase2_injected and not phase3_injected and step < MAX_STEPS - 2:
                phase3_injected = True
                messages.append({
                    "role": "user",
                    "content": PHASE3_PROMPT
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
                    total_test_runs += 1
                    if result["passed"]:
                        visible_tests_passed = True
                        consecutive_failures = 0
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": f"VISIBLE TESTS PASSED:\n{result['stdout'][:2000]}",
                        })
                    else:
                        consecutive_failures += 1
                        stdout = result["stdout"]
                        stderr = result["stderr"]

                        # Detect random/seed-related failures
                        is_random_failure = (
                            "seed" in stdout.lower() or
                            "reproducib" in stdout.lower() or
                            ("AssertionError" in stdout and "Lists differ" in stdout)
                        )

                        random_hint = ""
                        if is_random_failure:
                            random_hint = (
                                "\n\n⚠️ RANDOM SEED ISSUE: The test expects specific values from "
                                "a seeded random operation. You need the EXACT same random function "
                                "as the reference. Check the docstring imports section. Try:\n"
                                "- from random import seed, shuffle (random module)\n"
                                "- import numpy as np; np.random.seed(); np.random.shuffle()\n"
                                "The docstring often mentions which library to use."
                            )

                        off_by_one_hint = ""
                        if "length" in stdout.lower() or "len" in stdout.lower():
                            off_by_one_hint = (
                                "\n\n⚠️ LENGTH MISMATCH: Check if your range is inclusive or exclusive. "
                                "Use (end - start).days + 1 for inclusive, or (end - start).days for exclusive."
                            )

                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": (
                                f"TESTS FAILED:\nstdout:\n{stdout[:2000]}\n"
                                f"stderr:\n{stderr[:500]}"
                                f"{random_hint}{off_by_one_hint}"
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

        # Inject intervention if stuck for many steps without passing
        if (not visible_tests_passed and not intervention_injected
                and step >= 8 and step < MAX_STEPS - 4):
            intervention_injected = True
            messages.append({
                "role": "user",
                "content": INTERVENTION_PROMPT
            })

        # Inject phase 2 immediately after visible test passes
        if visible_tests_passed and not phase2_injected and step < MAX_STEPS - 7:
            phase2_injected = True
            messages.append({
                "role": "user",
                "content": PHASE2_PROMPT
            })

        # Inject phase 3 after phase 2 has had some steps to work
        elif (phase2_injected and not phase3_injected
              and step >= MAX_STEPS - 6 and step < MAX_STEPS - 1):
            phase3_injected = True
            messages.append({
                "role": "user",
                "content": PHASE3_PROMPT
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
