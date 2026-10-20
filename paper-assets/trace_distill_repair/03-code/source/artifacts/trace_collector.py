"""Trace collection via sys.settrace injection.

Runs target code in a subprocess with an injected trace hook, collects call/return/line/exception
events into TraceEvent objects. Supports settrace backend (default) and viztracer (placeholder).

Dependencies: standard library only (subprocess, pickle, tempfile, sys).
"""
from __future__ import annotations

import logging
import os
import json
import pickle
import subprocess
import tempfile
import textwrap
import time
from typing import List

from dtd_types import TraceEvent

logger = logging.getLogger(__name__)


class TraceCollector:
    def __init__(
        self,
        backend: str = "settrace",
        max_events: int = 100000,
        max_depth: int = 30,
        snapshot_locals: bool = True,
    ):
        self.backend = backend
        self.max_events = max_events
        self.max_depth = max_depth
        self.snapshot_locals = snapshot_locals

    def collect(self, code_path: str, test_command: str, timeout: int = 60, project_root: str = None) -> List[TraceEvent]:
        if self.backend == "viztracer":
            raise NotImplementedError("VizTracer backend not yet implemented")

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = os.path.join(tmpdir, "trace_events.json")
            script_path = os.path.join(tmpdir, "trace_wrapper.py")

            effective_root = project_root or (os.path.dirname(os.path.abspath(code_path)) if code_path else None)
            script_content = self._create_trace_script(code_path, test_command, output_path, effective_root)
            with open(script_path, "w") as f:
                f.write(script_content)

            logger.info("Running trace collection: %s", test_command)
            try:
                result = subprocess.run(
                    ["python3", script_path],
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    cwd=effective_root,
                )
                if result.returncode != 0:
                    logger.warning("Test command exited with code %d: %s", result.returncode, result.stderr[:500])
            except subprocess.TimeoutExpired:
                logger.error("Trace collection timed out after %ds", timeout)
                return []

            if not os.path.exists(output_path):
                logger.error("Trace output file not found. stderr: %s", result.stderr[:500])
                return []

            with open(output_path, "r") as f:
                raw_events = json.load(f)

        events = [
            TraceEvent(
                event_type=e["event_type"],
                function_name=e["function_name"],
                filename=e["filename"],
                lineno=e["lineno"],
                locals_snapshot=e.get("locals_snapshot", {}),
                call_depth=e["call_depth"],
                timestamp=e["timestamp"],
                return_value=e.get("return_value"),
                exception_info=tuple(e["exception_info"]) if e.get("exception_info") else None,
            )
            for e in raw_events
        ]
        logger.info("Collected %d trace events", len(events))
        return events

    def _create_trace_script(self, code_path: str, test_command: str, output_path: str, project_root: str = None) -> str:
        return textwrap.dedent(f"""\
            import sys
            import os
            import time
            import pickle
            import copy
            import traceback
            import shlex

            import json as _json_mod
            _json_dumps = _json_mod.dumps
            _file_open = open
            def _save_trace_output(events, path):
                data = _json_dumps(events)
                fh = _file_open(path, "w")
                fh.write(data)
                fh.close()

            MAX_EVENTS = {self.max_events}
            MAX_DEPTH = {self.max_depth}
            SNAPSHOT_LOCALS = {self.snapshot_locals}
            OUTPUT_PATH = {output_path!r}
            CODE_PATH = {code_path!r}

            # Determine project root for path filtering
            PROJECT_ROOT = {project_root!r} if {project_root!r} else (os.path.dirname(os.path.abspath(CODE_PATH)) if CODE_PATH else os.getcwd())

            trace_events = []
            current_depth = 0
            line_event_counts = {{}}

            def snapshot_locals(local_vars):
                if not SNAPSHOT_LOCALS:
                    return {{}}
                result = {{}}
                for k, v in list(local_vars.items())[:30]:
                    if k.startswith("__"):
                        continue
                    try:
                        if isinstance(v, str):
                            result[k] = v[:500]
                        elif isinstance(v, (list, tuple)):
                            result[k] = repr(v[:100])[:500]
                        elif isinstance(v, dict):
                            result[k] = repr(dict(list(v.items())[:50]))[:500]
                        elif isinstance(v, (int, float, bool, type(None))):
                            result[k] = v
                        else:
                            result[k] = repr(v)[:200]
                    except Exception:
                        result[k] = "<unserializable>"
                return result

            def trace_callback(frame, event, arg):
                global current_depth, trace_events
                if len(trace_events) >= MAX_EVENTS:
                    return None

                filename = frame.f_code.co_filename

                # Skip non-project files: stdlib, site-packages, frozen modules
                if any(skip in filename for skip in [
                    "<frozen", "importlib", "site-packages", "__pycache__",
                    "miniconda3/lib/python", "/usr/lib/python", "lib/python3.",
                    "_pytest/", "pluggy/", "_distutils_hack",
                ]):
                    return trace_callback

                # Only trace files within the project directory
                if not filename.startswith(PROJECT_ROOT):
                    return trace_callback

                if event == "line":
                    _func_key = (filename, frame.f_code.co_name)
                    _lec = line_event_counts.get(_func_key, 0)
                    if _lec >= 500:
                        return trace_callback
                    line_event_counts[_func_key] = _lec + 1

                if event == "call":
                    current_depth += 1
                    if current_depth > MAX_DEPTH:
                        current_depth -= 1
                        return None

                entry = {{
                    "event_type": event,
                    "function_name": frame.f_code.co_name,
                    "filename": filename,
                    "lineno": frame.f_lineno,
                    "locals_snapshot": snapshot_locals(frame.f_locals) if event in ("call", "return", "exception") else {{}},
                    "call_depth": current_depth,
                    "timestamp": time.time(),
                    "return_value": None,
                    "exception_info": None,
                }}

                if event == "return":
                    try:
                        entry["return_value"] = repr(arg)[:500]
                    except Exception:
                        entry["return_value"] = "<unrepresentable>"
                    current_depth = max(0, current_depth - 1)
                elif event == "exception":
                    exc_type, exc_value, exc_tb = arg
                    entry["exception_info"] = (
                        str(exc_type.__name__),
                        str(exc_value)[:500],
                        "".join(traceback.format_tb(exc_tb))[:2000],
                    )

                trace_events.append(entry)
                return trace_callback

            # --- Pre-parse command and pre-import modules BEFORE settrace ---
            os.chdir(PROJECT_ROOT)
            sys.path.insert(0, os.getcwd())

            TEST_COMMAND = {test_command!r}

            _test_parts = None
            _test_runner = None
            _test_module = None
            _test_args = []

            if TEST_COMMAND:
                _test_parts = shlex.split(TEST_COMMAND)
                if _test_parts[0] == 'python' and len(_test_parts) > 2 and _test_parts[1] == '-m':
                    _test_module = _test_parts[2]
                    _test_args = _test_parts[3:]
                    if _test_module == 'pytest':
                        import pytest
                        _test_runner = 'pytest'
                    elif _test_module == 'unittest':
                        import unittest
                        _test_runner = 'unittest'
                    else:
                        import runpy
                        _test_runner = 'runpy'
                elif _test_parts[0] in ('pytest', 'py.test'):
                    import pytest
                    _test_runner = 'pytest_direct'
                    _test_args = _test_parts[1:]
                else:
                    _test_runner = 'exec'
            else:
                _test_runner = 'exec_code'

            # --- NOW start tracing ---
            sys.settrace(trace_callback)
            try:
                if _test_runner == 'pytest':
                    pytest.main(_test_args)
                elif _test_runner == 'unittest':
                    unittest.main(module=None, argv=['unittest'] + _test_args, exit=False)
                elif _test_runner == 'runpy':
                    sys.argv = [_test_module] + _test_args
                    runpy.run_module(_test_module, run_name='__main__', alter_sys=True)
                elif _test_runner == 'pytest_direct':
                    pytest.main(_test_args)
                elif _test_runner == 'exec':
                    sys.argv = _test_parts
                    exec(compile(open(_test_parts[0]).read(), _test_parts[0], "exec"))
                elif _test_runner == 'exec_code':
                    exec(compile(open(CODE_PATH).read(), CODE_PATH, "exec"))
            except SystemExit:
                pass
            except Exception as e:
                print(f"Target code raised: {{e}}", file=sys.stderr)
            finally:
                sys.settrace(None)
                _save_trace_output(trace_events, OUTPUT_PATH)
                print(f"Wrote {{len(trace_events)}} trace events to {{OUTPUT_PATH}}", file=sys.stderr)
        """)


if __name__ == "__main__":
    import tempfile

    buggy_code = textwrap.dedent("""\
        def divide(a, b):
            return a / b

        def process(items):
            results = []
            for item in items:
                results.append(divide(item, item - 3))
            return results

        try:
            print(process([1, 2, 3, 4, 5]))
        except ZeroDivisionError as e:
            print(f"Caught: {e}")
    """)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(buggy_code)
        tmp_path = f.name

    collector = TraceCollector(max_events=1000, max_depth=10)
    events = collector.collect(tmp_path, "")
    print(f"Collected {len(events)} events")
    for e in events[:20]:
        print(f"  [{e.event_type:9s}] {e.function_name}:{e.lineno} depth={e.call_depth}")
    os.unlink(tmp_path)
