"""Agent tools: file operations and test runner (frozen — harness may not modify)."""

import subprocess
import sys


def read_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


def write_file(path: str, content: str) -> str:
    with open(path, "w") as f:
        f.write(content)
    return f"Written {len(content)} bytes to {path}"


def run_tests(test_path: str) -> dict:
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", test_path, "-v", "--tb=short", "-p", "no:cacheprovider"],
            capture_output=True,
            text=True,
            timeout=60,
        )
        return {
            "returncode": result.returncode,
            "stdout": result.stdout[-4000:],
            "stderr": result.stderr[-2000:],
            "passed": result.returncode == 0,
        }
    except subprocess.TimeoutExpired:
        return {"returncode": -1, "stdout": "", "stderr": "TIMEOUT: tests ran longer than 60s", "passed": False}


TOOL_DEFINITIONS = [
    {
        "name": "read_file",
        "description": "Read the contents of a file at the given path.",
        "input_schema": {
            "type": "object",
            "properties": {"path": {"type": "string", "description": "File path to read"}},
            "required": ["path"],
        },
    },
    {
        "name": "write_file",
        "description": "Write content to a file at the given path. This will overwrite the file.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "File path to write"},
                "content": {"type": "string", "description": "Content to write"},
            },
            "required": ["path", "content"],
        },
    },
    {
        "name": "run_tests",
        "description": "Run pytest on the given test file and return results.",
        "input_schema": {
            "type": "object",
            "properties": {"test_path": {"type": "string", "description": "Path to test file"}},
            "required": ["test_path"],
        },
    },
]


TOOL_DISPATCH = {
    "read_file": lambda args: read_file(args["path"]),
    "write_file": lambda args: write_file(args["path"], args["content"]),
    "run_tests": lambda args: run_tests(args["test_path"]),
}
