"""v005: Structured spec extraction + targeted verification to catch plausible-but-wrong implementations.

The core insight: the model implements plausible versions that pass the smoke test but fail
hidden tests because it doesn't carefully internalize every detail. This version forces:
1. An explicit spec extraction step (enumerate ALL constraints)
2. Implementation based on those constraints
3. Targeted verification questions about each constraint type
4. A correction pass if issues found
"""

import json
import os

import anthropic

MODEL = "claude-haiku-4-5"
MAX_STEPS = 20

SYSTEM_PROMPT = """You are an expert Python developer implementing functions from precise specifications.

CRITICAL CONTEXT:
- The visible test suite ONLY checks that the function is importable and callable (smoke test)
- There is a HIDDEN test suite that rigorously tests actual correctness against the full spec
- The smoke test passes even with an empty or stub function
- You MUST implement the COMPLETE, EXACT specification

WORKFLOW - follow these phases strictly:

PHASE 1 - SPEC EXTRACTION: Before writing ANY code, explicitly list:
  a) Function signature (exact parameter names, types, defaults)
  b) Return type (exact structure: DataFrame? list? float? dict? what columns/keys?)
  c) Algorithm steps in order
  d) Edge cases mentioned (empty inputs, boundary conditions, error handling)
  e) Required imports (copy EXACTLY from "starting with:" block)
  f) Module-level constants and their exact values

PHASE 2 - IMPLEMENTATION: Write the complete implementation to solution.py using those specs

PHASE 3 - TARGETED VERIFICATION: After writing, answer these questions about your implementation:
  Q1: What does your function return when given the minimum valid input? Does this match the spec?
  Q2: What does your function return for each edge case mentioned in the spec?
  Q3: Are your column names/keys EXACTLY as specified (case-sensitive)?
  Q4: Are the data types correct (int vs float, string vs datetime, etc.)?
  Q5: Is the sorting/ordering correct?
  Q6: Are you using the EXACT algorithm the spec requires (e.g., specific library functions)?
  Q7: Are the module-level constants used correctly?

PHASE 4 - FIX: If any answers reveal issues, fix solution.py

PHASE 5 - SMOKE TEST: Run the visible tests to confirm importability

CONSTRAINTS:
- You may ONLY write to solution.py - no other files
- Use EXACTLY the imports from the "starting with:" block
- Match return types EXACTLY
"""


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    client = anthropic.Anthropic(base_url=os.environ.get("ANTHROPIC_BASE_URL") or None)

    solution_path = os.path.join(work_dir, "solution.py")
    test_path = os.path.join(work_dir, "test_solution.py")

    solution_content = tool_dispatch["read_file"]({"path": solution_path})
    test_content = tool_dispatch["read_file"]({"path": test_path})

    # Initial message with full context
    initial_message = (
        f"Working directory: {work_dir}\n\n"
        f"## solution.py (implement this completely)\n"
        f"```python\n{solution_content}\n```\n\n"
        f"## test_solution.py (visible smoke test only - passes even with stub)\n"
        f"```python\n{test_content}\n```\n\n"
        f"## YOUR TASK\n\n"
        f"Implement the COMPLETE specification in {solution_path}.\n\n"
        f"**PHASE 1 - SPEC EXTRACTION (do this FIRST, before any code):**\n"
        f"Read the docstring carefully and explicitly list:\n"
        f"a) Function signature with all parameter names, types, and defaults\n"
        f"b) Exact return type and structure (what columns/keys/type exactly?)\n"
        f"c) Step-by-step algorithm\n"
        f"d) All edge cases (empty inputs, error conditions, boundary values)\n"
        f"e) Required imports (copy exactly from 'starting with:' block)\n"
        f"f) Any module-level constants with their exact values\n\n"
        f"**PHASE 2 - IMPLEMENTATION:**\n"
        f"Write complete implementation to {solution_path}.\n\n"
        f"**PHASE 3 - TARGETED VERIFICATION:**\n"
        f"After writing your implementation, explicitly answer:\n"
        f"Q1: Trace through the minimum valid input - what does your code return step by step?\n"
        f"Q2: For each edge case in the spec, what does your code return?\n"
        f"Q3: Are column names/keys/return structure EXACTLY as specified?\n"
        f"Q4: Are data types correct (int/float/str/datetime distinctions)?\n"
        f"Q5: Is the ordering/sorting correct?\n"
        f"Q6: Are you using exactly the algorithm/library functions specified?\n\n"
        f"**PHASE 4 - FIX:**\n"
        f"If verification reveals any issue, fix {solution_path}.\n\n"
        f"**PHASE 5 - SMOKE TEST:**\n"
        f"Run visible tests at {test_path} to confirm smoke test passes.\n\n"
        f"CONSTRAINT: You may ONLY write to {solution_path}. Never write to any other file."
    )

    messages = [{"role": "user", "content": initial_message}]

    total_tokens = 0
    step = 0
    smoke_passed = False
    implementation_written = False

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

            # Determine what to nudge based on state
            if not implementation_written and step < MAX_STEPS - 3:
                messages.append({
                    "role": "user",
                    "content": (
                        f"You haven't written the implementation yet. Please:\n"
                        f"1. First extract all spec details (PHASE 1)\n"
                        f"2. Then write your complete implementation to {solution_path}\n"
                        f"3. Then verify it (PHASE 3)\n"
                        f"4. Then run: {test_path}"
                    )
                })
                continue
            elif implementation_written and not smoke_passed and step < MAX_STEPS - 1:
                messages.append({
                    "role": "user",
                    "content": f"Please run the visible tests now: {test_path}"
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
                        passed = raw_result.get("passed", False)
                        stdout = raw_result.get("stdout", "")
                        stderr = raw_result.get("stderr", "")
                        returncode = raw_result.get("returncode", -1)

                        if passed:
                            smoke_passed = True
                            result_str = (
                                f"SMOKE TEST PASSED (returncode={returncode})\n"
                                f"STDOUT:\n{stdout}\n"
                                f"The visible smoke test passed - function is importable and callable.\n"
                                f"Your implementation is complete. The hidden tests will verify correctness."
                            )
                        else:
                            result_str = (
                                f"SMOKE TEST FAILED (returncode={returncode})\n"
                                f"STDOUT:\n{stdout}\n"
                                f"STDERR:\n{stderr}\n"
                                f"Fix syntax/import errors in {solution_path} so the function is callable."
                            )

                    elif block.name == "write_file":
                        write_path = block.input.get("path", "")
                        if write_path != solution_path:
                            result_str = (
                                f"ERROR: You may only write to {solution_path}. "
                                f"Attempted to write to: {write_path}. Operation rejected."
                            )
                        else:
                            implementation_written = True
                            result_str = str(raw_result)

                    elif block.name == "read_file":
                        result_str = str(raw_result)[:6000]

                    elif isinstance(raw_result, dict):
                        result_str = json.dumps(raw_result, ensure_ascii=False)
                    else:
                        result_str = str(raw_result)

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result_str[:6000],
                    })

                except Exception as e:
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": f"Error executing {block.name}: {e}",
                        "is_error": True,
                    })

        messages.append({"role": "user", "content": tool_results})

        # After smoke test passes, do a targeted re-verification pass
        if smoke_passed and step < MAX_STEPS - 2:
            # Check if this was the step that passed the smoke test
            just_passed = any(
                block.type == "tool_use" and block.name == "run_tests"
                for block in response.content
            )
            if just_passed:
                messages.append({
                    "role": "user",
                    "content": (
                        f"Good - the smoke test passes. Now do a final detailed verification.\n\n"
                        f"Read your current implementation in {solution_path} and answer these "
                        f"specific questions about potential hidden test failures:\n\n"
                        f"1. **Return value structure**: Is the exact return type (columns, index, "
                        f"dtype) matching the spec precisely?\n"
                        f"2. **Algorithm correctness**: Are you using the exact algorithm specified? "
                        f"(e.g., numpy mean vs Python mean, specific library calls)\n"
                        f"3. **Edge cases**: What happens with empty input, single element, boundary "
                        f"values? Does this match the spec exactly?\n"
                        f"4. **Constants and defaults**: Are module-level constants used correctly? "
                        f"Are default parameter values correct?\n"
                        f"5. **Data types**: Are numeric types (int vs float), string formats, and "
                        f"datetime formats exactly as specified?\n\n"
                        f"If you find ANY issue, fix it in {solution_path} now."
                    )
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
