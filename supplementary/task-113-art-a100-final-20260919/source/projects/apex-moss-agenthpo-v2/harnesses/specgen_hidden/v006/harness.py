"""v006: Two-call review structure - implement then independently review for correctness.

The model consistently produces plausible-but-wrong implementations that pass smoke tests.
This version uses a separate "reviewer" prompt that reads the actual written code and
critiques it specifically for the common failure modes seen in this task type.
"""

import json
import os

import anthropic

MODEL = "claude-haiku-4-5"
MAX_STEPS = 20

SYSTEM_PROMPT_IMPLEMENTER = """You are an expert Python developer implementing functions from specifications.

CRITICAL: There is a HIDDEN test suite testing actual correctness. The visible test only checks callability.

IMPLEMENTATION RULES:
1. Use EXACTLY the imports shown in the "You should write self-contained code starting with:" block
2. Match return types EXACTLY - column names, index, dtypes all matter
3. Handle ALL edge cases mentioned in the docstring
4. Use the EXACT algorithm specified (specific library functions matter)
5. Pay attention to: naive datetime handling, int vs float, sorting, column names

You may ONLY write to solution.py. Never write to any other file.
"""

SYSTEM_PROMPT_REVIEWER = """You are an expert Python code reviewer specializing in finding subtle correctness bugs.

Your job: Review a Python function implementation against its specification and find bugs that would cause
hidden test failures. The smoke test (import/callability) already passes, so focus on CORRECTNESS bugs.

Common failure patterns to check:
1. **datetime/timezone**: Are naive datetimes handled correctly? Is localize() vs astimezone() used correctly?
2. **Return type structure**: Exact column names? Index type? DataFrame vs dict vs list?
3. **Data types**: int vs float? .date() vs datetime? string formats?
4. **Algorithm specifics**: numpy mean vs python mean? random.randint vs random.random?
5. **Edge cases**: empty input, single element, boundary values
6. **Constants**: Are module-level constants used exactly as defined?
7. **Sorting/ordering**: Is the output sorted as specified?
8. **File path vs filename**: Does the function return paths or just filenames?

Be SPECIFIC about each bug you find. Then provide a corrected implementation.

You may ONLY write to solution.py. Never write to any other file.
"""


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    client = anthropic.Anthropic(base_url=os.environ.get("ANTHROPIC_BASE_URL") or None)

    solution_path = os.path.join(work_dir, "solution.py")
    test_path = os.path.join(work_dir, "test_solution.py")

    # Read both files upfront
    solution_content = tool_dispatch["read_file"]({"path": solution_path})
    test_content = tool_dispatch["read_file"]({"path": test_path})

    total_tokens = 0
    step = 0
    all_messages = []

    # =========================================================
    # PHASE 1: Implementation
    # =========================================================
    impl_messages = [{
        "role": "user",
        "content": (
            f"Working directory: {work_dir}\n\n"
            f"## solution.py (implement this completely)\n"
            f"```python\n{solution_content}\n```\n\n"
            f"## test_solution.py (visible smoke test - passes even with stub)\n"
            f"```python\n{test_content}\n```\n\n"
            f"Implement the COMPLETE specification in {solution_path}.\n\n"
            f"Before writing code, carefully extract from the docstring:\n"
            f"1. Exact function signature (parameter names, types, defaults)\n"
            f"2. Exact return type (DataFrame columns/index? list? float? dict?)\n"
            f"3. Algorithm steps in order\n"
            f"4. All edge cases\n"
            f"5. Required imports (copy EXACTLY from 'starting with:' block)\n"
            f"6. Any module-level constants\n\n"
            f"Then write your complete implementation to {solution_path}.\n\n"
            f"CONSTRAINT: You may ONLY write to {solution_path}. Never write to any other file."
        ),
    }]

    for step in range(1, MAX_STEPS + 1):
        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            system=SYSTEM_PROMPT_IMPLEMENTER,
            messages=impl_messages,
            tools=tool_definitions,
        )
        total_tokens += response.usage.input_tokens + response.usage.output_tokens
        all_messages.append({"role": "assistant", "content": _serialize_content(response.content)})

        if response.stop_reason != "tool_use":
            impl_messages.append({"role": "assistant", "content": response.content})
            break

        impl_messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        wrote_solution = False

        for block in response.content:
            if block.type == "tool_use":
                try:
                    if block.name == "write_file":
                        write_path = block.input.get("path", "")
                        if write_path != solution_path:
                            result_str = f"ERROR: You may only write to {solution_path}. Rejected."
                        else:
                            raw_result = tool_dispatch[block.name](block.input)
                            wrote_solution = True
                            result_str = str(raw_result)
                    elif block.name == "run_tests":
                        raw_result = tool_dispatch[block.name](block.input)
                        passed = raw_result.get("passed", False)
                        stdout = raw_result.get("stdout", "")
                        stderr = raw_result.get("stderr", "")
                        result_str = f"Tests passed: {passed}\nSTDOUT:\n{stdout}"
                        if stderr:
                            result_str += f"\nSTDERR:\n{stderr}"
                    else:
                        raw_result = tool_dispatch[block.name](block.input)
                        if isinstance(raw_result, dict):
                            result_str = json.dumps(raw_result, ensure_ascii=False)
                        else:
                            result_str = str(raw_result)[:6000]

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

        impl_messages.append({"role": "user", "content": tool_results})
        all_messages.append({"role": "user", "content": tool_results})

        if wrote_solution:
            # Implementation written, move to review phase
            break

    # =========================================================
    # PHASE 2: Read the actual written implementation
    # =========================================================
    written_solution = tool_dispatch["read_file"]({"path": solution_path})

    # =========================================================
    # PHASE 3: Independent review and correction
    # =========================================================
    review_messages = [{
        "role": "user",
        "content": (
            f"## Original specification (solution.py stub with docstring)\n"
            f"```python\n{solution_content}\n```\n\n"
            f"## Current implementation (written to solution.py)\n"
            f"```python\n{written_solution}\n```\n\n"
            f"## YOUR TASK: Code Review for Hidden Test Correctness\n\n"
            f"The smoke test (import/callability) passes. But there is a HIDDEN test suite "
            f"that tests actual correctness. Your job is to find bugs that would cause hidden "
            f"test failures.\n\n"
            f"**REVIEW CHECKLIST** (check each one explicitly):\n\n"
            f"1. **datetime/timezone handling**: \n"
            f"   - Are naive datetimes handled as specified? (UTC? local? unspecified?)\n"
            f"   - Is `localize()` vs `astimezone()` used correctly?\n"
            f"   - Are datetime objects vs date objects used correctly?\n\n"
            f"2. **Return type details**:\n"
            f"   - Exact column names (case-sensitive)?\n"
            f"   - Is the index correct (what type? sorted how?)?\n"
            f"   - DataFrame vs list vs dict vs float?\n\n"
            f"3. **Numeric types**:\n"
            f"   - int vs float?\n"
            f"   - numpy types vs Python native types?\n"
            f"   - Boolean values treated as int?\n\n"
            f"4. **Algorithm specifics**:\n"
            f"   - numpy.mean vs statistics.mean vs sum/len?\n"
            f"   - Exact random library and seed mechanism?\n"
            f"   - Are constants from the spec used exactly?\n\n"
            f"5. **Edge cases**:\n"
            f"   - Empty input handling?\n"
            f"   - Single element handling?\n"
            f"   - Boundary conditions?\n\n"
            f"6. **File/path handling** (if applicable):\n"
            f"   - Returns filenames or full paths?\n"
            f"   - How are extensions matched (case-sensitive? with/without dot?)?\n\n"
            f"7. **Sorting/ordering**:\n"
            f"   - Is output sorted as specified?\n"
            f"   - Column order?\n\n"
            f"For each checklist item, state explicitly whether there is a bug or not.\n"
            f"If you find bugs, write a corrected implementation to {solution_path}.\n"
            f"Then run the smoke test at {test_path} to confirm it still passes.\n\n"
            f"CONSTRAINT: You may ONLY write to {solution_path}. Never write to any other file."
        ),
    }]

    review_phase_start = step
    for step in range(step + 1, MAX_STEPS + 1):
        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            system=SYSTEM_PROMPT_REVIEWER,
            messages=review_messages,
            tools=tool_definitions,
        )
        total_tokens += response.usage.input_tokens + response.usage.output_tokens
        all_messages.append({"role": "assistant", "content": _serialize_content(response.content)})

        if response.stop_reason != "tool_use":
            review_messages.append({"role": "assistant", "content": response.content})
            break

        review_messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        smoke_passed = False

        for block in response.content:
            if block.type == "tool_use":
                try:
                    if block.name == "write_file":
                        write_path = block.input.get("path", "")
                        if write_path != solution_path:
                            result_str = f"ERROR: You may only write to {solution_path}. Rejected."
                        else:
                            raw_result = tool_dispatch[block.name](block.input)
                            result_str = str(raw_result)
                    elif block.name == "run_tests":
                        raw_result = tool_dispatch[block.name](block.input)
                        passed = raw_result.get("passed", False)
                        stdout = raw_result.get("stdout", "")
                        stderr = raw_result.get("stderr", "")
                        if passed:
                            smoke_passed = True
                            result_str = (
                                f"SMOKE TEST PASSED\n{stdout}\n"
                                f"Implementation complete and callable."
                            )
                        else:
                            result_str = (
                                f"SMOKE TEST FAILED\n{stdout}\nSTDERR:\n{stderr}\n"
                                f"Fix syntax errors in {solution_path}."
                            )
                    else:
                        raw_result = tool_dispatch[block.name](block.input)
                        if isinstance(raw_result, dict):
                            result_str = json.dumps(raw_result, ensure_ascii=False)
                        else:
                            result_str = str(raw_result)[:6000]

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

        review_messages.append({"role": "user", "content": tool_results})
        all_messages.append({"role": "user", "content": tool_results})

        if smoke_passed:
            break

    # =========================================================
    # PHASE 4: Final smoke test if not already done
    # =========================================================
    final_check = tool_dispatch["run_tests"]({"test_path": test_path})
    if not final_check.get("passed", False):
        # Try to fix: re-read spec and rewrite
        final_solution = tool_dispatch["read_file"]({"path": solution_path})
        fix_messages = [{
            "role": "user",
            "content": (
                f"The smoke test is FAILING. This means there's a syntax or import error.\n\n"
                f"Current broken implementation:\n```python\n{final_solution}\n```\n\n"
                f"Original spec:\n```python\n{solution_content}\n```\n\n"
                f"Fix the syntax/import errors in {solution_path} so the function is importable "
                f"and callable. Then run the tests at {test_path} to verify."
            ),
        }]

        for step in range(step + 1, MAX_STEPS + 1):
            response = client.messages.create(
                model=MODEL,
                max_tokens=4096,
                system=SYSTEM_PROMPT_IMPLEMENTER,
                messages=fix_messages,
                tools=tool_definitions,
            )
            total_tokens += response.usage.input_tokens + response.usage.output_tokens
            all_messages.append({"role": "assistant", "content": _serialize_content(response.content)})

            if response.stop_reason != "tool_use":
                fix_messages.append({"role": "assistant", "content": response.content})
                break

            fix_messages.append({"role": "assistant", "content": response.content})
            tool_results = []
            fixed = False

            for block in response.content:
                if block.type == "tool_use":
                    try:
                        if block.name == "write_file":
                            write_path = block.input.get("path", "")
                            if write_path != solution_path:
                                result_str = f"ERROR: You may only write to {solution_path}. Rejected."
                            else:
                                raw_result = tool_dispatch[block.name](block.input)
                                result_str = str(raw_result)
                        elif block.name == "run_tests":
                            raw_result = tool_dispatch[block.name](block.input)
                            passed = raw_result.get("passed", False)
                            stdout = raw_result.get("stdout", "")
                            stderr = raw_result.get("stderr", "")
                            result_str = f"Tests passed: {passed}\nSTDOUT:\n{stdout}"
                            if stderr:
                                result_str += f"\nSTDERR:\n{stderr}"
                            if passed:
                                fixed = True
                        else:
                            raw_result = tool_dispatch[block.name](block.input)
                            if isinstance(raw_result, dict):
                                result_str = json.dumps(raw_result, ensure_ascii=False)
                            else:
                                result_str = str(raw_result)[:6000]

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

            fix_messages.append({"role": "user", "content": tool_results})
            all_messages.append({"role": "user", "content": tool_results})

            if fixed:
                break

    return {"steps": step, "tokens": total_tokens, "messages": all_messages}


def _serialize_content(content):
    """Convert response content blocks to serializable format."""
    result = []
    for item in content:
        if hasattr(item, "model_dump"):
            result.append(item.model_dump())
        elif isinstance(item, dict):
            result.append(item)
        else:
            result.append(str(item))
    return result


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
