"""v002: Two-phase approach — pass visible tests, then review spec for hidden test coverage.

Phase 1: Standard implementation to pass visible tests.
Phase 2: Mandatory spec review to handle undocumented boundary cases for hidden suite.
"""

import json
import os

import anthropic

MODEL = "claude-haiku-4-5"
MAX_STEPS = 10

SYSTEM_PROMPT = """You are a coding agent. A working directory contains solution.py and test_solution.py.
Your goal: make ALL tests pass — both the visible test_solution.py AND a hidden final test suite.

CRITICAL: The visible test only checks one scenario. The hidden suite tests many more cases
based on the specification in solution.py's docstring. You MUST implement the FULL specification.

Strategy:
1. Read solution.py (docstring has the FULL specification — read it carefully)
2. Read test_solution.py (shows ONE example of expected behavior)
3. Implement the complete specification, including ALL edge cases mentioned in the docstring:
   - Error handling / exceptions for invalid inputs
   - Boundary conditions
   - Default parameter behavior
   - Return type contracts
4. Run tests to verify the visible test passes
5. Review your implementation against the docstring spec to find missing cases
6. Fix any gaps between your implementation and the full specification

Never modify test_solution.py. Only edit solution.py.
"""

SPEC_REVIEW_PROMPT = """The visible test is passing. Now do a thorough specification audit.

Re-read solution.py's docstring carefully and check:
1. Are ALL documented parameters handled correctly (including defaults)?
2. Are ALL documented exceptions raised for the right invalid inputs?
3. Are ALL documented return value formats/types correct?
4. Are there any edge cases in the docstring examples you haven't handled?
5. Are there boundary conditions (empty inputs, None values, wrong types) that should raise errors?

Compare your current implementation against every line of the specification.
If you find gaps, fix them in solution.py. If everything matches the spec perfectly, you're done.
"""


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    client = anthropic.Anthropic(base_url=os.environ.get("ANTHROPIC_BASE_URL") or None)
    
    solution_path = os.path.join(work_dir, "solution.py")
    test_path = os.path.join(work_dir, "test_solution.py")
    
    # Initial message: emphasize reading the full spec first
    messages = [{
        "role": "user",
        "content": (
            f"Working directory: {work_dir}\n\n"
            f"IMPORTANT: This task has a hidden test suite beyond the visible test_solution.py.\n"
            f"You must implement the COMPLETE specification from solution.py's docstring.\n\n"
            f"Start by reading solution.py to understand the full specification, "
            f"then read test_solution.py to see what the visible test checks.\n"
            f"Implement solution.py to satisfy ALL documented behaviors.\n\n"
            f"Files:\n"
            f"- {solution_path} (edit this only)\n"
            f"- {test_path} (read only)"
        ),
    }]

    total_tokens = 0
    step = 0
    visible_tests_passed = False
    spec_review_done = False

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
            
            # If agent stopped without doing spec review and tests passed, inject spec review
            if visible_tests_passed and not spec_review_done and step < MAX_STEPS - 1:
                spec_review_done = True
                messages.append({
                    "role": "user",
                    "content": SPEC_REVIEW_PROMPT
                })
                continue
            break

        messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        
        for block in response.content:
            if block.type == "tool_use":
                try:
                    result = tool_dispatch[block.name](block.input)
                    
                    if block.name == "run_tests":
                        # result is a dict
                        if result.get("passed"):
                            visible_tests_passed = True
                            output = result["stdout"]
                            tool_results.append({
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": f"TESTS PASSED:\n{output[:2000]}",
                            })
                        else:
                            output = result["stdout"]
                            stderr = result["stderr"]
                            tool_results.append({
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": f"TESTS FAILED:\nstdout:\n{output[:1500]}\nstderr:\n{stderr[:500]}",
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
        
        # After tests pass, inject spec review prompt if not done yet
        if visible_tests_passed and not spec_review_done and step < MAX_STEPS - 2:
            spec_review_done = True
            messages.append({
                "role": "user",
                "content": SPEC_REVIEW_PROMPT
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
