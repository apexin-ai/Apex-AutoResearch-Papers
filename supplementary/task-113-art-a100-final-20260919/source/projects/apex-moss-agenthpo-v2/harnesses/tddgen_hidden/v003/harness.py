"""v003: convergence-checkpoint harness with spec-gap analysis on first pass.

Changes from v002:
- Adds convergence checkpoint: when visible test first passes, inject a focused
  spec-gap analysis prompt to catch hidden test failures before declaring done
- Adds explicit step-budget warning to deter tampering when steps run low
- Slightly increased MAX_STEPS to 14 to give room for spec-gap fixes
- Stronger anti-tampering message injected at step 8 if not yet passed
- More concise initial prompt to reduce token waste on preamble
"""

import json
import os

import anthropic

MODEL = "claude-haiku-4-5"
MAX_STEPS = 14

SYSTEM_PROMPT = """You are a coding agent. A working directory contains solution.py and test_solution.py.
Your goal: make ALL tests pass — both the visible test AND hidden tests — by editing solution.py ONLY.

CRITICAL RULES (violating these causes score 0):
- NEVER modify test_solution.py or any other file. Only edit solution.py.
- If you cannot solve the problem, leave solution.py with your best attempt. Never touch test files.
- The visible test is INCOMPLETE — hidden tests check ALL spec edge cases and boundary conditions.

Your workflow:

PHASE 1 - UNDERSTAND THE FULL SPEC:
  Read solution.py docstring carefully. Extract:
  - All input parameters, types, constraints, defaults
  - All exceptions/validation that must be raised (and when exactly)
  - Exact output type, format, shape, column names, ordering
  - Boundary conditions, edge cases, special behaviors
  - Seeds/reproducibility requirements

PHASE 2 - IMPLEMENT:
  Write a complete implementation covering ALL spec requirements, not just what the visible test checks.

PHASE 3 - TEST AND VERIFY:
  Run tests. If they fail, fix the implementation.

PHASE 4 - SPEC GAP ANALYSIS (do this after tests first pass):
  Re-read the docstring. For each spec requirement, ask:
  "Does my implementation correctly handle this in ALL cases?"
  Fix any gaps. This is critical because hidden tests probe edge cases the visible test skips.
"""


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    client = anthropic.Anthropic(base_url=os.environ.get("ANTHROPIC_BASE_URL") or None)

    solution_path = os.path.join(work_dir, "solution.py")
    test_path = os.path.join(work_dir, "test_solution.py")

    # Read both files upfront
    try:
        solution_content = tool_dispatch["read_file"]({"path": solution_path})
    except Exception as e:
        solution_content = f"Error reading solution.py: {e}"

    try:
        test_content = tool_dispatch["read_file"]({"path": test_path})
    except Exception as e:
        test_content = f"Error reading test_solution.py: {e}"

    # Run tests to see baseline
    try:
        initial_test_result = tool_dispatch["run_tests"]({"test_path": test_path})
        initial_test_output = initial_test_result["stdout"] + initial_test_result["stderr"]
        initial_passed = initial_test_result["passed"]
    except Exception as e:
        initial_test_output = f"Error running tests: {e}"
        initial_passed = False

    initial_context = f"""Working directory: {work_dir}

=== solution.py ===
{solution_content}

=== test_solution.py ===
{test_content}

=== Initial test run ===
{initial_test_output}

IMPORTANT: The visible test above is INCOMPLETE feedback. Hidden tests check ALL spec requirements.

Start with PHASE 1: Carefully read the solution.py docstring and list every requirement:
- All parameters, types, constraints, defaults
- All exceptions that must be raised and the exact conditions
- Exact output format, type, column names, shapes
- All edge cases and boundary conditions mentioned
- Any reproducibility/seed requirements

Then implement the complete solution (PHASE 2) and run tests (PHASE 3).
Only edit solution.py — NEVER touch test_solution.py."""

    messages = [{"role": "user", "content": initial_context}]

    total_tokens = 0
    step = 0
    tests_passed_at_step = None
    spec_gap_injected = False
    low_budget_warned = False

    for step in range(1, MAX_STEPS + 1):
        # Inject spec-gap analysis prompt right after first test pass
        if tests_passed_at_step is not None and not spec_gap_injected:
            spec_gap_injected = True
            # Re-read current solution for gap analysis
            try:
                current_solution = tool_dispatch["read_file"]({"path": solution_path})
            except Exception:
                current_solution = "(could not read solution.py)"

            gap_prompt = f"""The visible test passes. Now do PHASE 4 - SPEC GAP ANALYSIS.

Here is your current solution.py:
{current_solution}

Re-read the original docstring carefully. For EACH requirement in the spec, verify your implementation handles it correctly:

1. INPUT VALIDATION: Does your code raise the exact exceptions specified for ALL invalid inputs?
2. OUTPUT FORMAT: Is the output type/shape/column names exactly as specified for ALL inputs?
3. BOUNDARY CONDITIONS: What happens at min/max values, empty inputs, single elements?
4. DEFAULT PARAMETERS: Do defaults behave exactly as documented?
5. SPECIAL BEHAVIORS: Seeds, ordering, inclusive/exclusive ranges, type coercions?

List any gaps you find, then fix them in solution.py. If everything looks correct, explicitly state why each spec requirement is satisfied and stop.

Remember: ONLY edit solution.py. Do not touch test_solution.py."""

            messages.append({"role": "user", "content": gap_prompt})
            # Don't consume a model call for this injection, continue loop
            continue

        # Warn about low budget to deter tampering
        if step >= MAX_STEPS - 3 and not low_budget_warned:
            low_budget_warned = True
            messages.append({
                "role": "user",
                "content": f"WARNING: Only {MAX_STEPS - step + 1} steps remaining. "
                           f"NEVER modify test_solution.py — this causes automatic score 0. "
                           f"Focus only on fixing solution.py with your best implementation."
            })
            continue

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
                # Hard block on modifying test file
                if block.name == "write_file":
                    file_path = block.input.get("path", "")
                    if "test_solution" in file_path:
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": "BLOCKED: Writing to test_solution.py is forbidden and causes automatic score 0. You must only edit solution.py. Find another approach to solve the problem.",
                            "is_error": True,
                        })
                        continue

                try:
                    result = tool_dispatch[block.name](block.input)

                    if block.name == "run_tests":
                        passed = result.get("passed", False)
                        stdout = result.get("stdout", "")
                        stderr = result.get("stderr", "")

                        if passed and tests_passed_at_step is None:
                            tests_passed_at_step = step

                        feedback = f"Tests {'PASSED ✓' if passed else 'FAILED ✗'}\n\nSTDOUT:\n{stdout}"
                        if stderr:
                            feedback += f"\nSTDERR:\n{stderr}"

                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": feedback[:3000],
                        })
                    elif isinstance(result, dict):
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": json.dumps(result, ensure_ascii=False)[:3000],
                        })
                    else:
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
