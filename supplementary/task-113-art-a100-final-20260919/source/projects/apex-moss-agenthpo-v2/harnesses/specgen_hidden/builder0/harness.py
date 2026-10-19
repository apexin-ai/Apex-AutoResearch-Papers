import anthropic
import json
import os

MODEL = "claude-haiku-4-5"


def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict:
    """
    Harness for specgen_hidden: pure spec-to-implementation workflow.

    Strategy:
    1. Read solution.py (has imports, signatures, docstrings only)
    2. Read test_solution.py (smoke test only - confirms importability)
    3. Ask model to deeply analyze spec and build explicit checklist
    4. Ask model to implement fully based on checklist
    5. Self-review pass for edge cases and correctness
    6. Write final implementation
    7. Run smoke tests to confirm no syntax/import errors
    8. If smoke fails, do one repair pass
    """
    client = anthropic.Anthropic(api_key=[REDACTED]"ANTHROPIC_API_KEY"))

    messages = []
    steps = 0
    total_tokens = 0

    def call_model(system: str, conversation: list, max_tokens: int = 4096) -> tuple[str, int]:
        """Call the model and return (response_text, tokens_used)."""
        response = client.messages.create(
            model=MODEL,
            max_tokens=max_tokens,
            system=system,
            messages=conversation,
        )
        text = response.content[0].text
        tokens = response.usage.input_tokens + response.usage.output_tokens
        return text, tokens

    # === Step 1: Read the files ===
    steps += 1
    solution_content = tool_dispatch["read_file"]({"path": os.path.join(work_dir, "solution.py")})

    steps += 1
    test_content = tool_dispatch["read_file"]({"path": os.path.join(work_dir, "test_solution.py")})

    # === Step 2: Deep spec analysis + checklist generation ===
    steps += 1

    system_spec_analysis = """You are an expert Python developer. Your task is to analyze a Python file that contains only imports, function signatures, and detailed docstrings — NO implementation yet.

Your job is to:
1. Carefully read every docstring, type hint, and signature
2. Extract ALL requirements: normal paths, edge cases, error handling, return types, preconditions, postconditions
3. Build an explicit numbered checklist of everything the implementation must handle
4. Note any ambiguities and how you will resolve them conservatively

Be thorough and precise. The hidden test suite will check correctness exhaustively."""

    spec_conversation = [
        {
            "role": "user",
            "content": f"""Here is the solution.py file with specs but no implementation:

```python
{solution_content}
```

Here is the visible smoke test (only checks importability):
```python
{test_content}
```

Please analyze the specifications thoroughly and produce:
1. A summary of what each function must do
2. An explicit checklist of ALL requirements extracted from the docstrings
3. Edge cases and boundary conditions you identified
4. Error/exception handling requirements
5. Return type and value requirements
6. Your plan for implementing each function

Be extremely thorough - the hidden test suite tests all behaviors."""
        }
    ]

    spec_analysis, tokens = call_model(system_spec_analysis, spec_conversation, max_tokens=4096)
    total_tokens += tokens
    messages.append({"role": "assistant_spec_analysis", "content": spec_analysis})

    # === Step 3: Full implementation ===
    steps += 1

    system_impl = """You are an expert Python developer implementing functions based on their specifications.

Key principles:
- Implement EXACTLY what the docstring specifies, nothing more, nothing less
- Handle ALL edge cases mentioned or implied by the spec
- Use correct Python idioms and handle errors as specified
- Return the exact types and values specified
- Do not add extra functionality not in the spec
- Make sure imports needed are already in the file (use only what's imported)

You must output the COMPLETE solution.py file with full implementations."""

    impl_conversation = [
        {
            "role": "user",
            "content": f"""Here is the solution.py to implement:

```python
{solution_content}
```

Based on this spec analysis and checklist:
{spec_analysis}

Now write the COMPLETE implementation of solution.py.

Requirements:
- Include ALL original imports from the file
- Keep ALL original function signatures exactly as-is
- Implement every function completely based on its docstring
- Handle all edge cases from your checklist
- Use only imports that are already in the file
- Output the complete file, not just the functions

Output ONLY the complete Python file content, starting with the imports, with no markdown fences or explanation."""
        }
    ]

    implementation, tokens = call_model(system_impl, impl_conversation, max_tokens=8192)
    total_tokens += tokens
    messages.append({"role": "assistant_implementation", "content": implementation})

    # Clean up implementation if model added markdown fences
    impl_clean = implementation.strip()
    if impl_clean.startswith("```python"):
        impl_clean = impl_clean[9:]
        if impl_clean.endswith("```"):
            impl_clean = impl_clean[:-3]
        impl_clean = impl_clean.strip()
    elif impl_clean.startswith("```"):
        impl_clean = impl_clean[3:]
        if impl_clean.endswith("```"):
            impl_clean = impl_clean[:-3]
        impl_clean = impl_clean.strip()

    # === Step 4: Self-review pass ===
    steps += 1

    system_review = """You are a meticulous code reviewer checking a Python implementation against its specification.

Your review must check:
1. Does each function match its docstring exactly?
2. Are all edge cases handled?
3. Are all error conditions handled with the right exceptions?
4. Are return types correct?
5. Are there any off-by-one errors, logic bugs, or missing cases?
6. Does the code use only the imports available in the file?
7. Is the syntax valid Python?

If you find issues, provide the CORRECTED complete file. If no issues, confirm the implementation is correct and output the same file."""

    review_conversation = [
        {
            "role": "user",
            "content": f"""Original specification:
```python
{solution_content}
```

Current implementation to review:
```python
{impl_clean}
```

Spec analysis/checklist:
{spec_analysis}

Please:
1. Review the implementation against the spec checklist item by item
2. Identify any bugs, missing cases, or spec violations
3. Output the CORRECTED complete Python file (or the same file if correct)

Output ONLY the complete Python file content with no markdown fences or explanation."""
        }
    ]

    reviewed_impl, tokens = call_model(system_review, review_conversation, max_tokens=8192)
    total_tokens += tokens
    messages.append({"role": "assistant_review", "content": reviewed_impl})

    # Clean up reviewed implementation
    reviewed_clean = reviewed_impl.strip()
    if reviewed_clean.startswith("```python"):
        reviewed_clean = reviewed_clean[9:]
        if reviewed_clean.endswith("```"):
            reviewed_clean = reviewed_clean[:-3]
        reviewed_clean = reviewed_clean.strip()
    elif reviewed_clean.startswith("```"):
        reviewed_clean = reviewed_clean[3:]
        if reviewed_clean.endswith("```"):
            reviewed_clean = reviewed_clean[:-3]
        reviewed_clean = reviewed_clean.strip()

    # Use reviewed version as final (it's either corrected or same)
    final_impl = reviewed_clean

    # === Step 5: Write the implementation ===
    steps += 1
    write_result = tool_dispatch["write_file"]({
        "path": os.path.join(work_dir, "solution.py"),
        "content": final_impl
    })
    messages.append({"role": "write_result", "content": write_result})

    # === Step 6: Run smoke tests ===
    steps += 1
    test_result = tool_dispatch["run_tests"]({"test_path": os.path.join(work_dir, "test_solution.py")})
    messages.append({"role": "smoke_test", "content": {
        "passed": test_result["passed"],
        "returncode": test_result["returncode"],
        "stdout": test_result["stdout"][:500] if test_result["stdout"] else "",
        "stderr": test_result["stderr"][:500] if test_result["stderr"] else "",
    }})

    # === Step 7: Repair if smoke test failed ===
    if not test_result["passed"]:
        steps += 1

        system_repair = """You are an expert Python developer fixing a syntax or import error in code.
The smoke test only checks that the module is importable and functions are callable.
Fix ONLY the syntax/import/structural errors while preserving all logic.
Output ONLY the complete corrected Python file with no markdown fences."""

        repair_conversation = [
            {
                "role": "user",
                "content": f"""The implementation failed the smoke test (import/syntax check).

Error output:
STDOUT: {test_result['stdout']}
STDERR: {test_result['stderr']}

Original spec:
```python
{solution_content}
```

Current (broken) implementation:
```python
{final_impl}
```

Fix the syntax/import errors and output the COMPLETE corrected Python file."""
            }
        ]

        repaired_impl, tokens = call_model(system_repair, repair_conversation, max_tokens=8192)
        total_tokens += tokens
        messages.append({"role": "assistant_repair", "content": repaired_impl})

        # Clean repair
        repair_clean = repaired_impl.strip()
        if repair_clean.startswith("```python"):
            repair_clean = repair_clean[9:]
            if repair_clean.endswith("```"):
                repair_clean = repair_clean[:-3]
            repair_clean = repair_clean.strip()
        elif repair_clean.startswith("```"):
            repair_clean = repair_clean[3:]
            if repair_clean.endswith("```"):
                repair_clean = repair_clean[:-3]
            repair_clean = repair_clean.strip()

        # Write repaired version
        steps += 1
        tool_dispatch["write_file"]({
            "path": os.path.join(work_dir, "solution.py"),
            "content": repair_clean
        })

        # Final smoke test
        steps += 1
        final_test = tool_dispatch["run_tests"]({"test_path": os.path.join(work_dir, "test_solution.py")})
        messages.append({"role": "final_smoke_test", "content": {
            "passed": final_test["passed"],
            "returncode": final_test["returncode"],
        }})

        # If still failing, do one more repair attempt with fresh implementation
        if not final_test["passed"]:
            steps += 1

            fallback_conversation = [
                {
                    "role": "user",
                    "content": f"""Still failing smoke test after repair attempt.

Errors:
STDOUT: {final_test['stdout']}
STDERR: {final_test['stderr']}

Please rewrite the complete solution from scratch based only on the spec:
```python
{solution_content}
```

Focus on getting a clean, syntactically valid implementation.
Output ONLY the complete Python file."""
                }
            ]

            fallback_impl, tokens = call_model(system_impl, fallback_conversation, max_tokens=8192)
            total_tokens += tokens
            messages.append({"role": "assistant_fallback", "content": fallback_impl})

            fallback_clean = fallback_impl.strip()
            if fallback_clean.startswith("```python"):
                fallback_clean = fallback_clean[9:]
                if fallback_clean.endswith("```"):
                    fallback_clean = fallback_clean[:-3]
                fallback_clean = fallback_clean.strip()
            elif fallback_clean.startswith("```"):
                fallback_clean = fallback_clean[3:]
                if fallback_clean.endswith("```"):
                    fallback_clean = fallback_clean[:-3]
                fallback_clean = fallback_clean.strip()

            steps += 1
            tool_dispatch["write_file"]({
                "path": os.path.join(work_dir, "solution.py"),
                "content": fallback_clean
            })

            steps += 1
            tool_dispatch["run_tests"]({"test_path": os.path.join(work_dir, "test_solution.py")})

    return {
        "steps": steps,
        "tokens": total_tokens,
        "messages": messages,
    }
