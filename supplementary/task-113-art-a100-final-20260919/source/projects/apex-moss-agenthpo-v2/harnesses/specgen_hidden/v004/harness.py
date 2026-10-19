"""v004: Spec-first implementation with mental self-verification.

Key insight: The model implements plausible-but-wrong versions because it gets no
behavioral feedback. This version instructs the model to carefully trace through
docstring examples mentally after implementing, since only solution.py can be written.
"""

import json
import os

import anthropic

MODEL = "claude-haiku-4-5"
MAX_STEPS = 18

SYSTEM_PROMPT = """You are an expert Python developer implementing functions from specifications.

CRITICAL CONTEXT:
- The visible test suite ONLY checks that the function is importable and callable
- There is a HIDDEN test suite that rigorously tests actual correctness
- You MUST implement the COMPLETE, CORRECT specification - not just a plausible version

YOUR WORKFLOW:
1. Read solution.py docstring VERY carefully - note ALL details:
   - Exact parameter types and defaults
   - Exact return type and structure (column names, index type, data types)
   - ALL edge cases (empty inputs, boundary conditions, error handling)
   - Example inputs/outputs shown in docstring
   - Required imports from "starting with:" block
   - Constants defined at module level

2. Write a COMPLETE implementation to solution.py

3. Mentally trace through docstring examples:
   - For each example in the docstring, mentally execute your code step by step
   - Verify the output matches what the docstring says
   - Check all edge cases explicitly

4. Fix any discrepancies found in solution.py

5. Run the visible tests to confirm smoke test passes

IMPLEMENTATION PRINCIPLES:
- Use EXACTLY the imports shown in the "starting with:" code block
- Match return types EXACTLY (DataFrame vs dict vs list vs float etc.)
- For DataFrames: match exact column names, index type, data types
- For random functions: use the EXACT random library and seed mechanism shown
- Handle ALL edge cases mentioned
- Pay attention to: sorting, column names, index types, numeric precision
- If spec says to use numpy for calculations, use numpy
- If spec shows constants (like EXTENSIONS, PRODUCTS), use those exact values

IMPORTANT CONSTRAINTS:
- You may ONLY write to solution.py inside the work directory
- NEVER write to test_solution.py or any other file
- The ONLY file you are permitted to write is solution.py
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
            f"## solution.py (implement this completely)\n"
            f"```python\n{solution_content}\n```\n\n"
            f"## test_solution.py (visible smoke test only)\n"
            f"```python\n{test_content}\n```\n\n"
            f"## YOUR TASK\n\n"
            f"Implement the COMPLETE specification in {solution_path}.\n\n"
            f"**PHASE 1 - Analyze the spec:**\n"
            f"Read the docstring above carefully. Identify:\n"
            f"- All parameters with types and defaults\n"
            f"- Exact return type (DataFrame columns/index? list of what? float?)\n"
            f"- All edge cases mentioned\n"
            f"- Any examples or expected outputs\n"
            f"- Required imports from 'starting with:' block\n"
            f"- Any module-level constants\n\n"
            f"**PHASE 2 - Implement:**\n"
            f"Write your complete implementation to {solution_path}.\n\n"
            f"**PHASE 3 - Mental verification:**\n"
            f"After writing the implementation, carefully trace through:\n"
            f"- Each example from the docstring: mentally execute your code and verify output\n"
            f"- Edge cases: empty inputs, boundary values, error conditions\n"
            f"- Return type details: column names, index type, data types, sorting\n"
            f"Think step by step through your code execution.\n\n"
            f"**PHASE 4 - Fix issues:**\n"
            f"If your mental verification reveals bugs, fix {solution_path}.\n\n"
            f"**PHASE 5 - Final check:**\n"
            f"Run the visible tests ({test_path}) to confirm smoke test passes.\n\n"
            f"CONSTRAINTS:\n"
            f"- The ONLY file you may write is {solution_path}\n"
            f"- NEVER write to {test_path} or any other file\n"
            f"- Be thorough - hidden tests check every detail of your implementation"
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

            # If smoke test hasn't passed yet and we have steps remaining, nudge
            if not smoke_passed and step < MAX_STEPS - 2:
                messages.append({
                    "role": "user",
                    "content": (
                        f"You haven't finished yet. Please:\n"
                        f"1. Make sure your implementation is written to {solution_path}\n"
                        f"2. Mentally verify it against the docstring examples and edge cases\n"
                        f"3. Fix any issues in {solution_path}\n"
                        f"4. Run the visible tests: {test_path}"
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
                        # raw_result is a dict with returncode, stdout, stderr, passed
                        passed = raw_result.get("passed", False)
                        stdout = raw_result.get("stdout", "")
                        stderr = raw_result.get("stderr", "")
                        returncode = raw_result.get("returncode", -1)
                        test_path_run = block.input.get("test_path", "")

                        is_smoke_test = "test_solution" in test_path_run

                        if passed:
                            if is_smoke_test:
                                smoke_passed = True
                                feedback = (
                                    f"SMOKE TEST PASSED (returncode={returncode})\n"
                                    f"STDOUT:\n{stdout}\n"
                                    f"The visible smoke test passed - function is callable.\n"
                                    f"Implementation is complete."
                                )
                            else:
                                feedback = (
                                    f"TESTS PASSED (returncode={returncode})\n"
                                    f"STDOUT:\n{stdout}\n"
                                )
                        else:
                            if is_smoke_test:
                                feedback = (
                                    f"SMOKE TEST FAILED (returncode={returncode})\n"
                                    f"STDOUT:\n{stdout}\n"
                                    f"STDERR:\n{stderr}\n"
                                    f"Fix the import/syntax errors so the function is callable."
                                )
                            else:
                                feedback = (
                                    f"TESTS FAILED (returncode={returncode})\n"
                                    f"STDOUT:\n{stdout}\n"
                                    f"STDERR:\n{stderr}\n"
                                    f"Fix the issues in {solution_path}."
                                )
                        result_str = feedback

                    elif block.name == "write_file":
                        write_path = block.input.get("path", "")
                        # Only allow writing to solution.py
                        if write_path != solution_path:
                            result_str = (
                                f"ERROR: You may only write to {solution_path}. "
                                f"Attempted to write to: {write_path}. "
                                f"No other files may be written."
                            )
                        else:
                            result_str = str(raw_result)
                    elif block.name == "read_file":
                        result_str = str(raw_result)[:5000]
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
