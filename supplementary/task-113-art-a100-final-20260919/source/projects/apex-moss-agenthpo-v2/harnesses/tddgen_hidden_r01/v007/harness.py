"""v007: Focused spec-mining with concrete assertion verification.

Key changes from v006:
- Reduced MAX_STEPS to 15 (v005/v006 hit timeout at 20 steps, 300s)
- Pre-load both files in initial context (saves tool calls)
- After visible test passes: inject a targeted "spec-mining" prompt that forces
  the agent to enumerate EVERY docstring clause and write concrete runnable assertions
- Specifically target bigcodebench_458's repeated failure by pushing harder on
  exact numeric types, string extraction edge cases, and empty/invalid inputs
- Clearer phase structure with explicit step budgets
"""

import json
import os

import anthropic

MODEL = "claude-haiku-4-5"
MAX_STEPS = 15

SYSTEM_PROMPT = """You are a coding agent. A working directory contains solution.py and test_solution.py.
Your goal: make ALL tests pass — both the visible test_solution.py AND a hidden final test suite.

CRITICAL FACTS:
1. The visible test checks ONE scenario. The hidden suite tests MANY more cases.
2. The hidden suite tests EVERY behavior documented in solution.py's docstring.
3. You MUST empirically verify your implementation — do not just reason about it.
4. When seeded random tests fail: the exact expected output tells you which random function to use.

WORKFLOW:
Phase 1: Implement solution.py → run visible test until it passes.
Phase 2: Write a __main__ block with CONCRETE assertions for EVERY docstring clause.
         Run tests (pytest ignores __main__). Fix any issues.
Phase 3: Remove __main__ block, final test run.

Never modify test_solution.py. Only edit solution.py.
"""

PHASE2_SPEC_MINING_PROMPT = """PHASE 2: The visible test passes. Now mine the docstring for EVERY testable behavior.

You must add a `if __name__ == '__main__':` block to solution.py that tests EVERY behavior 
mentioned in the docstring. Work through each section systematically:

**Step 1: List all "Raises:" entries**
For each one, write code that:
- Calls the function with an input that SHOULD trigger that exception
- Catches the EXACT exception type and prints "PASS"
- If a different exception or no exception: prints "FAIL"

**Step 2: List all parameters and their defaults**
For each optional parameter:
- Call the function using ONLY that default (omit the parameter)
- Verify the behavior matches the docstring description

**Step 3: Check return type and structure**
- Verify isinstance() of return value
- Check column names if returning a DataFrame
- Check dtypes if specified

**Step 4: Test boundary/edge cases from docstring**
- Empty inputs (empty list, empty string, empty dict)  
- None values for optional parameters
- Single-element inputs
- Numeric edge cases (0, negative numbers, very large numbers)

**Step 5: Data format correctness**
- If the docstring shows example output, verify your code produces the same format
- Check exact string formatting, number types (int vs float), etc.

After adding the __main__ block, run the visible tests again (pytest ignores __main__).
Then carefully review your assertions. Fix ANY issue you find.
Write the fixed solution, run tests again, then proceed to Phase 3.
"""

PHASE3_CLEANUP_PROMPT = """PHASE 3: Clean up and final verification.

1. Remove the `if __name__ == '__main__':` block from solution.py
2. Run the visible tests to confirm they still pass
3. Quick final check: re-read the docstring and confirm:
   - Every "Raises:" entry has the EXACT exception type documented
   - Every parameter default value is correct
   - Return type matches exactly what's documented
   - No debug code left in the implementation

You are done when tests pass and solution.py is clean.
"""


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    client = anthropic.Anthropic(base_url=os.environ.get("ANTHROPIC_BASE_URL") or None)

    solution_path = os.path.join(work_dir, "solution.py")
    test_path = os.path.join(work_dir, "test_solution.py")

    # Pre-load both files to give full context immediately (saves tool-call steps)
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
            f"This task has a HIDDEN test suite that checks MANY more cases than the visible test.\n"
            f"You MUST implement every behavior in the docstring, not just what the visible test checks.\n\n"
            f"=== solution.py (EDIT THIS FILE) ===\n{solution_content}\n\n"
            f"=== test_solution.py (READ ONLY - DO NOT MODIFY) ===\n{test_content}\n\n"
            f"IMPLEMENTATION CHECKLIST:\n"
            f"□ Every 'Raises:' entry implemented with the EXACT exception type\n"
            f"□ Every parameter default value matches the docstring EXACTLY\n"
            f"□ Return type and structure matches the docstring EXACTLY\n"
            f"□ Edge cases: empty inputs, None values, wrong types, boundary values\n"
            f"□ Random functions: check docstring for which library (random vs numpy)\n"
            f"□ Range boundaries: check if end is inclusive or exclusive\n\n"
            f"PHASE 1: Implement solution.py and run visible tests until they pass.\n"
            f"Use write_file to update solution.py and run_tests to verify.\n"
            f"Important: write_file requires both 'path' and 'content' arguments."
        ),
    }]

    total_tokens = 0
    step = 0
    visible_tests_passed = False
    phase2_injected = False
    phase3_injected = False
    nudge_count = 0

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
            # Agent stopped — manage phase transitions
            if not visible_tests_passed and step < MAX_STEPS - 3:
                nudge_count += 1
                messages.append({
                    "role": "user",
                    "content": (
                        "Please implement and test your solution now. "
                        "Use write_file (with 'path' and 'content' arguments) to update solution.py, "
                        "then use run_tests to verify."
                    )
                })
                continue

            if visible_tests_passed and not phase2_injected and step < MAX_STEPS - 5:
                phase2_injected = True
                messages.append({
                    "role": "user",
                    "content": PHASE2_SPEC_MINING_PROMPT
                })
                continue

            if phase2_injected and not phase3_injected and step < MAX_STEPS - 1:
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
                            f"Writing to '{requested_path}' is not permitted. "
                            f"Only solution.py may be modified."
                        ),
                        "is_error": True,
                    })
                    continue

                # Ensure content key is present
                if "content" not in block.input:
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": (
                            "Error: write_file requires a 'content' argument. "
                            "Please provide both 'path' and 'content'."
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
                        stdout = result["stdout"]
                        stderr = result["stderr"]

                        # Detect specific failure types for targeted hints
                        hints = []

                        if ("Lists differ" in stdout and
                                any(kw in stdout.lower() for kw in ["seed", "reproducib", "shuffle"])):
                            hints.append(
                                "⚠️ RANDOM SEED MISMATCH: Check the docstring imports section to "
                                "identify which random library to use (random module vs numpy). "
                                "The expected output was generated with ONE specific function call."
                            )

                        if ("First list contains" in stdout or
                                any(kw in stdout for kw in ["len(", "length"])):
                            hints.append(
                                "⚠️ LENGTH MISMATCH: Check if your range is inclusive or exclusive. "
                                "For date ranges: (end-start).days gives exclusive count, "
                                "(end-start).days+1 gives inclusive count."
                            )

                        hint_str = ("\n\n" + "\n".join(hints)) if hints else ""

                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": (
                                f"TESTS FAILED:\nstdout:\n{stdout[:2000]}\n"
                                f"stderr:\n{stderr[:500]}"
                                f"{hint_str}"
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

        # Inject phase 2 immediately after visible test passes
        if visible_tests_passed and not phase2_injected and step < MAX_STEPS - 5:
            phase2_injected = True
            messages.append({
                "role": "user",
                "content": PHASE2_SPEC_MINING_PROMPT
            })

        # Inject phase 3 when near step budget or after phase 2 has been running
        elif (phase2_injected and not phase3_injected
              and step >= MAX_STEPS - 4 and step < MAX_STEPS - 1):
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
