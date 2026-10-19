"""Extract and validate generated harness source without seeing benchmark data."""

import ast
import re

MODEL_LINE = 'MODEL = "claude-haiku-4-5"'
RUN_SIGNATURE = (
    "def run(work_dir: str, tool_definitions: list, "
    "tool_dispatch: dict) -> dict"
)
ALLOWED_IMPORTS = {"anthropic", "json", "os"}
ALLOWED_OS_CHAINS = {
    ("os", "environ"),
    ("os", "environ", "get"),
    ("os", "getenv"),
    ("os", "path"),
    ("os", "path", "join"),
}
FORBIDDEN_CALLS = {
    "open",
    "exec",
    "eval",
    "compile",
    "__import__",
    "getattr",
    "setattr",
    "globals",
    "vars",
}
ALLOWED_TASK_PYTHON_FILES = {"solution.py", "test_solution.py"}
PYTHON_FILENAME_RE = re.compile(
    r"(?<![A-Za-z0-9_])([A-Za-z_][A-Za-z0-9_]*\.py)\b"
)


class InvalidHarness(ValueError):
    """The generator response does not contain an executable harness contract."""


def extract_python_block(text: str) -> str:
    """Return the outer Python block, preserving nested fences in string literals."""
    opening = re.search(r"(?m)^```python[ \t]*\r?\n", text)
    if not opening:
        raise InvalidHarness(f"no Python block found; got: {text[:500]}")

    # Generated harnesses often put Markdown fences inside their own prompts. The
    # outer response fence is therefore the last closing fence, not the first.
    closing = text.rfind("\n```")
    if closing < opening.end():
        raise InvalidHarness("Python block has no closing fence")
    return text[opening.end():closing].strip() + "\n"


def validate_harness(code: str) -> None:
    """Check the frozen source contract and the tool-dispatch calling convention."""
    try:
        tree = ast.parse(code)
    except SyntaxError as exc:
        raise InvalidHarness(
            f"syntax error at line {exc.lineno}: {exc.msg}"
        ) from exc

    if MODEL_LINE not in code:
        raise InvalidHarness(f"missing exact frozen model line: {MODEL_LINE}")
    if RUN_SIGNATURE not in code:
        raise InvalidHarness(f"missing exact run signature: {RUN_SIGNATURE}")

    run_defs = [
        node for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == "run"
    ]
    if len(run_defs) != 1 or isinstance(run_defs[0], ast.AsyncFunctionDef):
        raise InvalidHarness("harness must define exactly one synchronous run()")

    for node in ast.walk(tree):
        if not isinstance(node, ast.Constant) or not isinstance(node.value, str):
            continue
        for filename in PYTHON_FILENAME_RE.findall(node.value):
            if filename not in ALLOWED_TASK_PYTHON_FILES:
                raise InvalidHarness(
                    f"prompt/source names forbidden task file {filename}; "
                    "the executor may write only solution.py"
                )

    dispatch_calls = 0
    run_test_wrappers = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        for child in ast.walk(node):
            if not isinstance(child, ast.Return) or not isinstance(child.value, ast.Call):
                continue
            called = child.value.func
            if (
                isinstance(called, ast.Subscript)
                and isinstance(called.value, ast.Name)
                and called.value.id == "tool_dispatch"
                and isinstance(called.slice, ast.Constant)
                and called.slice.value == "run_tests"
            ):
                run_test_wrappers.add(node.name)

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Subscript):
            continue
        if not isinstance(node.func.value, ast.Name) or node.func.value.id != "tool_dispatch":
            continue
        dispatch_calls += 1
        if len(node.args) != 1 or node.keywords:
            raise InvalidHarness(
                "tool_dispatch functions accept one input dict, for example "
                'tool_dispatch[name]({"path": path}); keyword unpacking is invalid'
            )
        tool_name = (
            node.func.slice.value
            if isinstance(node.func.slice, ast.Constant) else None
        )
        required_keys = {
            "read_file": {"path"},
            "write_file": {"path", "content"},
            "run_tests": {"test_path"},
        }.get(tool_name)
        input_arg = node.args[0]
        if required_keys and isinstance(input_arg, ast.Dict):
            literal_keys = {
                key.value for key in input_arg.keys
                if isinstance(key, ast.Constant) and isinstance(key.value, str)
            }
            missing = required_keys - literal_keys
            if missing:
                raise InvalidHarness(
                    f"{tool_name} input dict is missing required "
                    f"key(s): {', '.join(sorted(missing))}"
                )

    if dispatch_calls == 0:
        raise InvalidHarness("harness never invokes a provided tool via tool_dispatch")

    run_result_names = set()
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        value = node.value
        if not isinstance(value, ast.Call):
            continue
        direct_run_tests = (
            isinstance(value.func, ast.Subscript)
            and isinstance(value.func.value, ast.Name)
            and value.func.value.id == "tool_dispatch"
            and isinstance(value.func.slice, ast.Constant)
            and value.func.slice.value == "run_tests"
        )
        wrapped_run_tests = (
            isinstance(value.func, ast.Name)
            and value.func.id in run_test_wrappers
        )
        if not (direct_run_tests or wrapped_run_tests):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        run_result_names.update(
            target.id for target in targets if isinstance(target, ast.Name)
        )

    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "lower"
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id in run_result_names
        ):
            raise InvalidHarness(
                f"{node.func.value.id} is the dict returned by run_tests; "
                'check result["passed"] or read result["stdout"]/["stderr"] '
                "instead of calling .lower()"
            )


def validate_sandbox_contract(code: str) -> None:
    """Reject source that can bypass the frozen tools or inspect scorer state."""
    try:
        tree = ast.parse(code)
    except SyntaxError as exc:
        raise InvalidHarness(
            f"syntax error at line {exc.lineno}: {exc.msg}"
        ) from exc

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name not in ALLOWED_IMPORTS:
                    raise InvalidHarness(
                        f"import {alias.name} is outside the sandbox allowlist "
                        f"{sorted(ALLOWED_IMPORTS)}"
                    )
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            raise InvalidHarness(
                f"from {module} import ... is outside the sandbox contract; "
                "use direct imports from the allowlist"
            )

        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in FORBIDDEN_CALLS:
                raise InvalidHarness(
                    f"call to {node.func.id}() is forbidden by the sandbox contract"
                )

        if isinstance(node, ast.Attribute):
            parts = []
            current = node
            while isinstance(current, ast.Attribute):
                parts.append(current.attr)
                current = current.value
            if isinstance(current, ast.Name) and current.id == "os":
                chain = ("os", *reversed(parts))
                if chain not in ALLOWED_OS_CHAINS:
                    dotted = ".".join(chain)
                    raise InvalidHarness(
                        f"{dotted} is forbidden by the sandbox contract; only "
                        "os.environ.get, os.getenv, and os.path.join are allowed"
                    )


def parse_generated_harness(text: str) -> tuple[str, str]:
    """Extract (source, mechanism) and reject invalid generated artifacts."""
    code = extract_python_block(text)
    validate_harness(code)
    validate_sandbox_contract(code)
    mechanism_match = re.search(r"(?m)^MECHANISM:\s*(.+)$", text)
    mechanism = (
        mechanism_match.group(1).strip()
        if mechanism_match else "(not reported)"
    )
    return code, mechanism
