import anthropic
import json
import os

MODEL = "claude-haiku-4-5"


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    client = anthropic.Anthropic()

    messages = []
    total_tokens = 0
    steps = 0
    max_iterations = 8

    solution_path = os.path.join(work_dir, "solution.py")
    test_path = os.path.join(work_dir, "test_solution.py")

    system_prompt = """You are an expert Python debugger. Your job is to fix bugs in solution.py so all pytest tests pass.

Key principles:
- Make the MINIMAL change needed to fix the bug
- Do NOT rewrite the entire file; change only the buggy line(s)
- Bugs are typically small: wrong operator, off-by-one index, bad initial value, wrong condition, etc.
- When you identify the fix, output ONLY the complete corrected solution.py content
- Do not add explanations inside the code; just fix the bug

When given test failure output and source code, diagnose the bug from the assertion errors (expected vs actual values), locate the exact faulty line, and return the fixed file content."""

    def run_tests_now():
        return tool_dispatch["run_tests"]({"test_path": test_path})

    def read_solution():
        return tool_dispatch["read_file"]({"path": solution_path})

    def read_tests():
        return tool_dispatch["read_file"]({"path": test_path})

    def write_solution(content):
        return tool_dispatch["write_file"]({"path": solution_path, "content": content})

    # Step 1: Run tests first to see failures
    steps += 1
    test_result = run_tests_now()

    if test_result["passed"]:
        # Already passing, nothing to do
        return {"steps": steps, "tokens": total_tokens, "messages": messages}

    # Step 2: Read source files
    steps += 1
    solution_code = read_solution()

    steps += 1
    test_code = read_tests()

    # Build initial diagnostic context
    failure_output = test_result["stdout"]
    if test_result["stderr"]:
        failure_output += "\nSTDERR:\n" + test_result["stderr"]

    initial_user_message = f"""Here is the buggy solution.py that needs to be fixed:

```python
{solution_code}
```

Here is test_solution.py (read-only, do not modify):

```python
{test_code}
```

Here are the current test failures:

```
{failure_output}
```

Analyze the failure messages carefully (especially "expected X but got Y" or similar),
identify the minimal fix needed, and return the complete corrected solution.py content.
Output ONLY the Python code for solution.py, with no markdown fences or extra text."""

    messages.append({"role": "user", "content": initial_user_message})

    for iteration in range(max_iterations):
        steps += 1

        # Call the model
        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            system=system_prompt,
            messages=messages,
        )

        total_tokens += response.usage.input_tokens + response.usage.output_tokens

        assistant_content = response.content[0].text.strip()

        # Add assistant response to history
        messages.append({"role": "assistant", "content": assistant_content})

        # Extract code from the response (handle markdown fences if model adds them)
        fixed_code = assistant_content
        if "```python" in fixed_code:
            start = fixed_code.index("```python") + len("```python")
            end = fixed_code.index("```", start)
            fixed_code = fixed_code[start:end].strip()
        elif "```" in fixed_code:
            start = fixed_code.index("```") + 3
            end = fixed_code.index("```", start)
            fixed_code = fixed_code[start:end].strip()

        # Write the fixed solution
        steps += 1
        write_solution(fixed_code)

        # Run tests again
        steps += 1
        test_result = run_tests_now()

        if test_result["passed"]:
            # All tests pass, we're done
            messages.append({
                "role": "user",
                "content": "All tests passed successfully."
            })
            break

        # Tests still failing - provide new failure context for next iteration
        failure_output = test_result["stdout"]
        if test_result["stderr"]:
            failure_output += "\nSTDERR:\n" + test_result["stderr"]

        # Read current state of solution for next iteration context
        current_solution = read_solution()
        steps += 1

        retry_message = f"""The tests are still failing. Here is the current state of solution.py:

```python
{current_solution}
```

New test failure output:

```
{failure_output}
```

Look carefully at the remaining failures. Make only the necessary minimal fix(es) and return the complete corrected solution.py content.
Output ONLY the Python code, no markdown fences or extra text."""

        messages.append({"role": "user", "content": retry_message})

    return {"steps": steps, "tokens": total_tokens, "messages": messages}
