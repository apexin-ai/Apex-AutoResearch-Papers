"""Safe Python code execution sandbox for MATH code interpreter.

Input: Python code string
Output: dict with stdout, stderr, returncode, success
"""

import ast
import subprocess
import tempfile
import os


def auto_print_last_expr(code: str) -> str:
    """If the last statement is a bare expression (not a print call), wrap it in print()."""
    try:
        tree = ast.parse(code)
        if tree.body and isinstance(tree.body[-1], ast.Expr):
            expr_value = tree.body[-1].value
            if (isinstance(expr_value, ast.Call)
                    and isinstance(expr_value.func, ast.Name)
                    and expr_value.func.id == 'print'):
                return code
            last = tree.body[-1]
            lines = code.split('\n')
            expr_lines = lines[last.lineno - 1:last.end_lineno]
            expr_text = '\n'.join(expr_lines).strip()
            prefix = '\n'.join(lines[:last.lineno - 1])
            wrapped = f'print({expr_text})'
            return (prefix + '\n' + wrapped) if prefix else wrapped
    except SyntaxError:
        pass
    return code


def execute_code(code: str, timeout: int = 30) -> dict:
    """Execute Python code in isolated subprocess, return stdout/stderr/returncode."""
    code = auto_print_last_expr(code)
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(code)
        f.flush()
        tmp_path = f.name
    try:
        result = subprocess.run(
            ['python3', tmp_path],
            capture_output=True, text=True,
            timeout=timeout,
            cwd='/tmp'
        )
        return {
            'stdout': result.stdout[:5000],
            'stderr': result.stderr[:2000],
            'returncode': result.returncode,
            'success': result.returncode == 0
        }
    except subprocess.TimeoutExpired:
        return {'stdout': '', 'stderr': 'TIMEOUT', 'returncode': -1, 'success': False}
    finally:
        os.unlink(tmp_path)


if __name__ == "__main__":
    r = execute_code("print(2 + 2)")
    print(r)
    r2 = execute_code("import time; time.sleep(60)", timeout=2)
    print(r2)
