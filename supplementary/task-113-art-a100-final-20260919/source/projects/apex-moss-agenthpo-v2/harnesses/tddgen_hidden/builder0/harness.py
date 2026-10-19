import anthropic
import json
import os

MODEL = "claude-haiku-4-5"


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    client = anthropic.Anthropic(api_key=[REDACTED]"ANTHROPIC_API_KEY"))

    messages = []
    total_tokens = 0
    steps = 0

    MAX_ITERATIONS = 8

    # --- Step 1: Read solution.py and test_solution.py ---
    solution_path = os.path.join(work_dir, "solution.py")
    test_path = os.path.join(work_dir, "test_solution.py")

    solution_content = tool_dispatch["read_file"]({"path": solution_path})
    test_content = tool_dispatch["read_file"]({"path": test_path})
    steps += 2

    # --- Step 2: Run visible tests first to calibrate interface ---
    initial_test_result = tool_dispatch["run_tests"]({"test_path": test_path})
    steps += 1

    initial_test_status = (
        "PASSED" if initial_test_result["passed"] else "FAILED"
    )
    initial_test_output = (
        initial_test_result["stdout"] + "\n" + initial_test_result["stderr"]
    ).strip()

    # --- Step 3: Build the comprehensive system prompt ---
    system_prompt = """You are an expert Python developer implementing functions from specifications.

Your task is to implement Python functions based STRICTLY on their docstrings and type signatures.

Key principles:
1. The docstring is your PRIMARY and COMPLETE specification - read every line carefully
2. Extract ALL requirements: input types, output structure, exceptions, edge cases, boundary conditions
3. The visible test is only ONE sample - there are many hidden tests covering edge cases
4. After implementing, mentally simulate these cases:
   - Empty inputs (empty string, empty list, empty dict, None if allowed)
   - Single-element inputs
   - Large inputs / performance considerations
   - Type boundaries (0, negative numbers, max values)
   - Special characters, Unicode if strings involved
   - All documented exception conditions
   - Order/sorting guarantees mentioned in docs
   - Return type consistency across all code paths

When writing your implementation:
- Preserve ALL existing imports
- Keep the function signature EXACTLY as given
- Implement ONLY the function body, replacing any `pass` or placeholder
- Do not add extra functions unless needed as helpers within the module
- Handle ALL edge cases documented in the docstring
- Return EXACTLY the types specified in the docstring

Output ONLY valid Python code for the complete solution.py file. No explanations, no markdown fences, just the raw Python code."""

    # --- Step 4: Build the initial user prompt ---
    user_prompt = f"""Here is the solution.py file you need to implement:

```python
{solution_content}
```

Here is the visible test (only ONE sample - there are hidden tests for all edge cases):

```python
{test_content}
```

Initial test run status: {initial_test_status}
Initial test output:
{initial_test_output}

Instructions:
1. Carefully read EVERY line of the docstring(s) in solution.py
2. List (mentally) all the requirements, edge cases, and constraints you find
3. Implement the complete function(s) handling ALL documented behaviors
4. Pay special attention to:
   - Exact return types and structures
   - All documented exceptions and when they're raised
   - Boundary conditions (empty, None, zero, negative, etc.)
   - Any ordering or format guarantees
   - Performance requirements if mentioned

Write the complete solution.py file now:"""

    messages.append({"role": "user", "content": user_prompt})

    # --- Main iteration loop ---
    for iteration in range(MAX_ITERATIONS):
        steps += 1

        # Call the model
        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            system=system_prompt,
            messages=messages,
        )

        total_tokens += response.usage.input_tokens + response.usage.output_tokens

        assistant_content = response.content[0].text
        messages.append({"role": "assistant", "content": assistant_content})

        # Extract the Python code from the response
        code = assistant_content.strip()

        # Strip markdown fences if present
        if "```python" in code:
            start = code.find("```python") + len("```python")
            end = code.find("```", start)
            if end != -1:
                code = code[start:end].strip()
        elif "```" in code:
            start = code.find("```") + 3
            end = code.find("```", start)
            if end != -1:
                code = code[start:end].strip()

        # Write the solution
        tool_dispatch["write_file"]({"path": solution_path, "content": code})
        steps += 1

        # Run tests
        test_result = tool_dispatch["run_tests"]({"test_path": test_path})
        steps += 1

        test_output = (
            test_result["stdout"] + "\n" + test_result["stderr"]
        ).strip()

        if test_result["passed"]:
            # Tests pass - now do a self-audit pass to check edge cases
            if iteration < MAX_ITERATIONS - 2:
                # Ask model to self-audit for hidden edge cases
                audit_prompt = f"""The visible test PASSED. However, there are hidden tests covering all edge cases from the docstring.

Current implementation:
```python
{code}
```

Please carefully re-read the docstring and check your implementation against these potential hidden test scenarios:
1. Empty/None inputs (all documented combinations)
2. Single-element edge cases
3. Negative numbers, zero, maximum values
4. Special string characters, Unicode
5. All documented exception conditions - are they raised at the right times?
6. Return type consistency - is it ALWAYS the documented type?
7. Order/format guarantees - are they always maintained?
8. Any undocumented but reasonable edge cases a test suite would check

If you find ANY potential issues, write an improved complete solution.py.
If the implementation looks complete and correct for all edge cases, write it again unchanged.

Write the complete solution.py:"""

                messages.append({"role": "user", "content": audit_prompt})
                # Continue loop for self-audit
            else:
                # Last iterations - we're done
                break
        else:
            # Tests failed - provide targeted feedback
            feedback_prompt = f"""The test FAILED. Here is the output:

{test_output}

Current implementation:
```python
{code}
```

Analyze the failure carefully:
1. What exactly failed?
2. What does the docstring say about this case?
3. Fix the implementation to handle this case AND all other documented edge cases

Write the complete corrected solution.py:"""

            messages.append({"role": "user", "content": feedback_prompt})

    # Final check - if we ended on audit loop without final write, ensure last good code is written
    # (The last write_file call already wrote the latest version)

    return {
        "steps": steps,
        "tokens": total_tokens,
        "messages": messages,
    }
