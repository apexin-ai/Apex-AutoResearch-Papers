"""v007: Adversarial concrete-test-tracing review to catch plausible-but-wrong implementations.

Key insight: The model produces plausible implementations that pass smoke tests but fail hidden
tests because it reasons abstractly ("handles edge cases ✓"). This version forces concrete
test-case tracing: the reviewer must construct specific inputs from the spec examples and
mentally execute the actual code line-by-line to find mismatches.
"""

import json
import os

import anthropic

MODEL = "claude-haiku-4-5"
MAX_STEPS = 20

SYSTEM_PROMPT_IMPLEMENTER = """You are an expert Python developer implementing functions from precise specifications.

CRITICAL: There is a HIDDEN test suite testing actual correctness. The visible test only checks callability.

IMPLEMENTATION RULES:
1. Use EXACTLY the imports shown in the "You should write self-contained code starting with:" block
2. Match return types EXACTLY - column names, index, dtypes all matter
3. Handle ALL edge cases mentioned in the docstring
4. Use the EXACT algorithm specified (specific library functions matter)
5. Pay attention to: naive datetime handling, int vs float, sorting, column names

You may ONLY write to solution.py. Never write to any other file.
"""

SYSTEM_PROMPT_ADVERSARIAL = """You are an adversarial test engineer whose job is to find bugs in Python implementations.

You will be given a function specification (docstring) and the current implementation.

Your method: CONSTRUCT CONCRETE TEST CASES and TRACE THROUGH THE CODE.

Do NOT give abstract checklist assessments like "edge cases: ✓". Instead:

1. Extract 3-5 concrete test inputs from the spec (use any examples given, plus boundary cases)
2. For each test input, manually execute the code step-by-step and determine what it returns
3. Compare that output to what the spec says it should return
4. If there's a mismatch, identify the exact line causing the bug and fix it

Common bugs to hunt for:
- datetime.fromtimestamp() uses LOCAL time, datetime.utcfromtimestamp() uses UTC - which does the spec want?
- pytz: localize() is for naive datetimes, astimezone() is for aware datetimes - mixing these is wrong
- random.randint(a, b) is inclusive on both ends; random.random() is [0,1)
- pandas DataFrame from dict: .T transposes rows/columns - is the index what the spec wants?
- glob.glob("*ext") vs glob.glob("*.ext") - the dot matters
- shutil.copy2 vs shutil.move - spec might want move not copy
- returning os.path.basename(f) vs just f vs full path - which does spec want?
- int vs float return types - np.mean returns float64, not Python int
- boolean values: isinstance(True, int) is True in Python - should booleans be treated as numeric?

After tracing, write a corrected implementation to solution.py if needed, then run the smoke test.

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
    # PHASE 1: Initial Implementation
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
            f"STEP 1 - Extract from docstring:\n"
            f"- Exact function signature (parameter names, types, defaults)\n"
            f"- Exact return type and structure (DataFrame with what columns/index? list? float?)\n"
            f"- Algorithm steps in order\n"
            f"- All edge cases\n"
            f"- Required imports (copy EXACTLY from 'starting with:' block)\n"
            f"- Any module-level constants\n\n"
            f"STEP 2 - Write complete implementation to {solution_path}\n\n"
            f"STEP 3 - Run smoke test at {test_path} to confirm callable\n\n"
            f"CONSTRAINT: You may ONLY write to {solution_path}. Never write to any other file."
        ),
    }]

    implementation_written = False
    smoke_passed_phase1 = False

    for step in range(1, MAX_STEPS // 2 + 1):
        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            system=SYSTEM_PROMPT_IMPLEMENTER,
            messages=impl_messages,
            tools=tool_definitions,
        )
        total_tokens += response.usage.input_tokens + response.usage.output_tokens
        all_messages.append({
            "role": "assistant",
            "content": _serialize_content(response.content)
        })

        if response.stop_reason != "tool_use":
            impl_messages.append({"role": "assistant", "content": response.content})
            if not implementation_written:
                impl_messages.append({
                    "role": "user",
                    "content": f"Please write your implementation to {solution_path} and run tests at {test_path}."
                })
                all_messages.append({
                    "role": "user",
                    "content": f"Please write your implementation to {solution_path} and run tests at {test_path}."
                })
                continue
            break

        impl_messages.append({"role": "assistant", "content": response.content})
        tool_results = []

        for block in response.content:
            if block.type == "tool_use":
                try:
                    if block.name == "write_file":
                        write_path = block.input.get("path", "")
                        if write_path != solution_path:
                            result_str = f"ERROR: You may only write to {solution_path}. Rejected."
                        else:
                            raw_result = tool_dispatch[block.name](block.input)
                            implementation_written = True
                            result_str = str(raw_result)
                    elif block.name == "run_tests":
                        raw_result = tool_dispatch[block.name](block.input)
                        passed = raw_result.get("passed", False)
                        stdout = raw_result.get("stdout", "")
                        stderr = raw_result.get("stderr", "")
                        if passed:
                            smoke_passed_phase1 = True
                            result_str = f"SMOKE TEST PASSED\n{stdout}"
                        else:
                            result_str = f"SMOKE TEST FAILED\n{stdout}\nSTDERR:\n{stderr}\nFix syntax errors."
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

        if implementation_written and smoke_passed_phase1:
            break

    # =========================================================
    # PHASE 2: Read the actual written implementation
    # =========================================================
    written_solution = tool_dispatch["read_file"]({"path": solution_path})

    # =========================================================
    # PHASE 3: Adversarial concrete-test-tracing review
    # =========================================================
    adversarial_messages = [{
        "role": "user",
        "content": (
            f"## Original specification (docstring from solution.py)\n"
            f"```python\n{solution_content}\n```\n\n"
            f"## Current implementation\n"
            f"```python\n{written_solution}\n```\n\n"
            f"## YOUR TASK: Find bugs via concrete test tracing\n\n"
            f"The smoke test passes. Now find correctness bugs by tracing concrete test cases.\n\n"
            f"**METHOD - Do this for each test case:**\n"
            f"1. Write down a specific input (concrete values)\n"
            f"2. Execute the code step-by-step with that input\n"
            f"3. Write down what the code actually returns\n"
            f"4. Compare to what the spec says should be returned\n"
            f"5. Identify any mismatch\n\n"
            f"**REQUIRED TEST CASES TO TRACE:**\n\n"
            f"TEST 1: Use the EXACT example from the docstring (if any). Trace line by line.\n\n"
            f"TEST 2: Minimum/empty input case (empty list, 0, None as appropriate). "
            f"What does the code return? What should it return?\n\n"
            f"TEST 3: Single-element input. What does the code return? What should it return?\n\n"
            f"TEST 4: A normal case with 2-3 elements. Trace the full execution path.\n\n"
            f"**SPECIFIC BUGS TO HUNT:**\n\n"
            f"For datetime/timezone functions:\n"
            f"- `datetime.fromtimestamp()` uses LOCAL timezone; `datetime.utcfromtimestamp()` uses UTC\n"
            f"- `pytz.localize()` is ONLY for naive datetimes; `astimezone()` is for aware datetimes\n"
            f"- Mixing these causes wrong results or errors\n\n"
            f"For file transfer functions:\n"
            f"- `shutil.copy2()` COPIES; `shutil.move()` MOVES - which does spec want?\n"
            f"- `os.path.basename(f)` vs full path - what does spec say to return?\n"
            f"- glob pattern `*ext` vs `*.ext` - does the dot matter?\n\n"
            f"For DataFrame functions:\n"
            f"- After `.T`, verify what is the index vs columns\n"
            f"- Boolean values in Python: `isinstance(True, int)` is True - should booleans count as numeric?\n"
            f"- `np.mean()` returns float64; explicit `float()` conversion needed?\n\n"
            f"For random/seed functions:\n"
            f"- `random.randint(a, b)` is inclusive on BOTH ends\n"
            f"- Verify the seed is set BEFORE any random calls\n\n"
            f"**AFTER TRACING:**\n"
            f"- List each bug found with: input → expected output → actual output → line to fix\n"
            f"- If bugs found, write corrected implementation to {solution_path}\n"
            f"- Run smoke test at {test_path} to verify it still passes\n\n"
            f"CONSTRAINT: You may ONLY write to {solution_path}. Never write to any other file."
        ),
    }]

    smoke_passed_phase2 = False

    for step in range(step + 1, MAX_STEPS + 1):
        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            system=SYSTEM_PROMPT_ADVERSARIAL,
            messages=adversarial_messages,
            tools=tool_definitions,
        )
        total_tokens += response.usage.input_tokens + response.usage.output_tokens
        all_messages.append({
            "role": "assistant",
            "content": _serialize_content(response.content)
        })

        if response.stop_reason != "tool_use":
            adversarial_messages.append({"role": "assistant", "content": response.content})
            # If review is done without running tests, prompt to run them
            if not smoke_passed_phase2:
                adversarial_messages.append({
                    "role": "user",
                    "content": (
                        f"Please run the smoke test at {test_path} to verify your "
                        f"implementation is still callable. If you found no bugs, just run "
                        f"the test. If you found bugs, fix them first then run the test."
                    )
                })
                all_messages.append({
                    "role": "user",
                    "content": (
                        f"Please run the smoke test at {test_path} to verify your "
                        f"implementation is still callable."
                    )
                })
                continue
            break

        adversarial_messages.append({"role": "assistant", "content": response.content})
        tool_results = []

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
                            smoke_passed_phase2 = True
                            result_str = (
                                f"SMOKE TEST PASSED\n{stdout}\n"
                                f"Implementation complete. Hidden tests will verify correctness."
                            )
                        else:
                            result_str = (
                                f"SMOKE TEST FAILED\n{stdout}\nSTDERR:\n{stderr}\n"
                                f"Fix syntax/import errors in {solution_path}."
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

        adversarial_messages.append({"role": "user", "content": tool_results})
        all_messages.append({"role": "user", "content": tool_results})

        if smoke_passed_phase2:
            break

    # =========================================================
    # PHASE 4: Final smoke test safety check
    # =========================================================
    final_check = tool_dispatch["run_tests"]({"test_path": test_path})
    if not final_check.get("passed", False):
        # Emergency fix: rewrite from scratch
        current_broken = tool_dispatch["read_file"]({"path": solution_path})
        emergency_messages = [{
            "role": "user",
            "content": (
                f"EMERGENCY: The smoke test is failing. Fix it NOW.\n\n"
                f"Current broken code:\n```python\n{current_broken}\n```\n\n"
                f"Original spec:\n```python\n{solution_content}\n```\n\n"
                f"Write a working implementation to {solution_path} and run tests at {test_path}."
            ),
        }]

        for step in range(step + 1, MAX_STEPS + 1):
            response = client.messages.create(
                model=MODEL,
                max_tokens=4096,
                system=SYSTEM_PROMPT_IMPLEMENTER,
                messages=emergency_messages,
                tools=tool_definitions,
            )
            total_tokens += response.usage.input_tokens + response.usage.output_tokens
            all_messages.append({
                "role": "assistant",
                "content": _serialize_content(response.content)
            })

            if response.stop_reason != "tool_use":
                emergency_messages.append({"role": "assistant", "content": response.content})
                break

            emergency_messages.append({"role": "assistant", "content": response.content})
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
                            result_str = f"Tests passed: {passed}\n{stdout}"
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

            emergency_messages.append({"role": "user", "content": tool_results})
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
