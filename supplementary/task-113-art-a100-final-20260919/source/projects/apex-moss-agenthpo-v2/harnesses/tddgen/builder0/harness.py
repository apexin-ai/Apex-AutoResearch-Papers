import anthropic
import json
import os

MODEL = "claude-haiku-4-5"


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    solution_path = os.path.join(work_dir, "solution.py")
    test_path = os.path.join(work_dir, "test_solution.py")

    # Read both files upfront
    skeleton = tool_dispatch["read_file"]({"path": solution_path})
    tests = tool_dispatch["read_file"]({"path": test_path})

    # Run tests once to see initial failures (understand what's needed)
    initial_result = tool_dispatch["run_tests"]({"test_path": test_path})
    initial_output = initial_result["stdout"] + "\n" + initial_result["stderr"]

    client = anthropic.Anthropic()

    system_prompt = """You are an expert Python developer practicing test-driven development.
Your task: implement a Python function body so that ALL provided pytest tests pass.

Key principles:
1. The test file is the ONLY reliable specification — read every assertion carefully
2. Infer the complete behavior from test cases, including edge cases and boundary conditions
3. The docstring may be vague or misleading — trust the tests over the docstring
4. Write a complete, correct implementation — not a minimal patch
5. Output ONLY valid Python code for solution.py, no explanations, no markdown fences
6. Make sure imports are included if needed (e.g., math, re, collections, etc.)
7. Do not modify any test files"""

    messages = []
    total_tokens = 0
    steps = 0
    max_iterations = 6

    # Build the initial user message with all context
    user_message = f"""Here is the solution skeleton (function signatures + docstrings only):

```python
{skeleton}
```

Here are the tests that define the complete specification:

```python
{tests}
```

Initial test run output (showing what currently fails):
```
{initial_output}
```

Study ALL the test assertions carefully to understand the complete required behavior.
Then write the COMPLETE implementation of solution.py that makes all tests pass.
Output ONLY the complete Python file content, nothing else."""

    messages.append({"role": "user", "content": user_message})

    for iteration in range(max_iterations):
        steps += 1

        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            system=system_prompt,
            messages=messages,
        )

        total_tokens += response.usage.input_tokens + response.usage.output_tokens

        # Extract the implementation from the response
        assistant_content = response.content[0].text.strip()

        # Clean up any accidental markdown fences
        code = assistant_content
        if code.startswith("```python"):
            code = code[len("```python"):].strip()
        if code.startswith("```"):
            code = code[3:].strip()
        if code.endswith("```"):
            code = code[:-3].strip()

        # Write the implementation
        tool_dispatch["write_file"]({"path": solution_path, "content": code})

        # Run the tests
        test_result = tool_dispatch["run_tests"]({"test_path": test_path})

        if test_result["passed"]:
            # All tests pass — we're done
            messages.append({"role": "assistant", "content": assistant_content})
            steps += 1  # count the test run as a step
            break

        # Tests failed — build feedback for next iteration
        test_output = test_result["stdout"] + "\n" + test_result["stderr"]

        # Add assistant response and failure feedback to conversation
        messages.append({"role": "assistant", "content": assistant_content})
        messages.append({
            "role": "user",
            "content": f"""The tests did NOT all pass. Here is the pytest output:

```
{test_output}
```

Carefully analyze each failing test assertion. Re-read the test file to understand
what you missed or misimplemented. Then write the COMPLETE corrected solution.py.
Output ONLY the complete Python file content, nothing else."""
        })

        steps += 1  # count the test run as a step

        if iteration == max_iterations - 1:
            # Last iteration, no more retries
            break

    return {
        "steps": steps,
        "tokens": total_tokens,
        "messages": messages,
    }
