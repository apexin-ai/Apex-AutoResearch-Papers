"""Z3 subprocess sandbox — isolates Z3 C library in a child process.

Z3's C++ layer can crash with SIGABRT on malformed expressions ('unreachable'
assertion). This kills the entire Python process without triggering any
exception handler. Solution: run all Z3 eval() calls in a persistent child
process. If it crashes, the parent survives and restarts the worker.

Usage:
    from .z3_sandbox import get_sandbox
    sandbox = get_sandbox()
    valid, err = sandbox.validate(fol_str, vocab)
    is_sat, ic_score, mcs_size = sandbox.check_ic(fol_strs, vocab, ...)
"""

import logging
import multiprocessing as mp
import queue
import threading

logger = logging.getLogger(__name__)


def _build_z3_env(vocab):
    """Build Z3 namespace from vocab dict. Runs inside child process."""
    import z3
    env = {
        "ForAll": z3.ForAll, "Exists": z3.Exists,
        "And": z3.And, "Or": z3.Or, "Not": z3.Not,
        "Implies": z3.Implies,
        "BoolSort": z3.BoolSort, "IntSort": z3.IntSort,
        "Int": z3.Int, "Bool": z3.Bool,
        "Function": z3.Function, "Const": z3.Const,
        "True": z3.BoolVal(True), "False": z3.BoolVal(False),
    }
    for v in ("x", "y", "z", "w", "u", "v"):
        env[v] = z3.Int(v)
    for name, info in vocab.get("predicates", {}).items():
        arity = info.get("arity", 1)
        sorts = [z3.IntSort()] * arity + [z3.BoolSort()]
        env[name] = z3.Function(name, *sorts)
    for name in vocab.get("constants", {}):
        env[name] = z3.Const(name, z3.IntSort())
    return env


def _parse_fol(fol_str, env):
    """Parse FOL string to Z3 expression. Runs inside child process."""
    import z3
    result = eval(fol_str, {"__builtins__": {}}, env)
    if isinstance(result, z3.ExprRef):
        return result
    return None


def _greedy_mcs_impl(exprs, premise_exprs, z3_timeout_ms):
    """Greedy MCS computation. Runs inside child process."""
    import z3
    remaining = list(exprs)
    while len(remaining) > 1:
        solver = z3.Solver()
        solver.set("timeout", z3_timeout_ms)
        for pe in premise_exprs:
            solver.add(pe)
        solver.add(*remaining)
        if solver.check() == z3.sat:
            break

        found = False
        for i in range(len(remaining) - 1, -1, -1):
            test = remaining[:i] + remaining[i + 1:]
            s = z3.Solver()
            s.set("timeout", z3_timeout_ms)
            for pe in premise_exprs:
                s.add(pe)
            s.add(*test)
            if s.check() == z3.sat:
                remaining = test
                found = True
                break

        if not found:
            remaining.pop()

    return len(remaining)


def _worker_loop(req_q, res_q):
    """Main loop for the Z3 worker subprocess."""
    import z3

    while True:
        try:
            task = req_q.get()
        except (EOFError, OSError):
            break
        if task is None:
            break

        task_type = task[0]
        try:
            if task_type == "validate":
                _, fol_str, vocab = task
                env = _build_z3_env(vocab)
                result = eval(fol_str, {"__builtins__": {}}, env)
                if isinstance(result, (z3.BoolRef, z3.QuantifierRef)):
                    res_q.put(("ok", True, None))
                else:
                    res_q.put(("ok", False, f"expression evaluates to {type(result).__name__}, expected BoolRef"))

            elif task_type == "check_ic":
                _, fol_strs, vocab, total_claims, premise_fol_strs, z3_timeout_ms = task
                env = _build_z3_env(vocab)

                premise_exprs = []
                for pfol in premise_fol_strs:
                    try:
                        e = _parse_fol(pfol, env)
                        if e is not None:
                            premise_exprs.append(e)
                    except Exception:
                        pass

                exprs = []
                for fol in fol_strs:
                    try:
                        e = _parse_fol(fol, env)
                        if e is not None:
                            exprs.append(e)
                    except Exception:
                        pass

                n_formalized = len(exprs)
                if not exprs:
                    res_q.put(("ok", True, 0.0, 0))
                    continue

                denom = total_claims if total_claims > 0 else n_formalized

                solver = z3.Solver()
                solver.set("timeout", z3_timeout_ms)
                for pe in premise_exprs:
                    solver.add(pe)
                solver.add(*exprs)

                result = solver.check()
                if result == z3.sat:
                    res_q.put(("ok", True, n_formalized / denom, n_formalized))
                elif result == z3.unsat:
                    mcs_size = _greedy_mcs_impl(exprs, premise_exprs, z3_timeout_ms)
                    res_q.put(("ok", False, mcs_size / denom, mcs_size))
                else:
                    res_q.put(("ok", True, n_formalized / denom, n_formalized))

            elif task_type == "check_sat_set":
                _, fol_strs, vocab, premise_fol_strs, z3_timeout_ms = task
                env = _build_z3_env(vocab)

                premise_exprs = []
                for pfol in premise_fol_strs:
                    try:
                        e = _parse_fol(pfol, env)
                        if e is not None:
                            premise_exprs.append(e)
                    except Exception:
                        pass

                exprs = []
                for fol in fol_strs:
                    try:
                        e = _parse_fol(fol, env)
                        if e is not None:
                            exprs.append(e)
                    except Exception:
                        pass

                if not exprs:
                    res_q.put(("ok", True))
                    continue

                solver = z3.Solver()
                solver.set("timeout", z3_timeout_ms)
                for pe in premise_exprs:
                    solver.add(pe)
                solver.add(*exprs)
                res_q.put(("ok", solver.check() == z3.sat))

            elif task_type == "check_entailment":
                _, claim_fol_strs, vocab, premise_fol_strs, conclusion_fol, z3_timeout_ms = task
                env = _build_z3_env(vocab)

                solver = z3.Solver()
                solver.set("timeout", z3_timeout_ms)

                for pfol in premise_fol_strs:
                    try:
                        e = _parse_fol(pfol, env)
                        if e is not None:
                            solver.add(e)
                    except Exception:
                        pass

                for fol in claim_fol_strs:
                    try:
                        e = _parse_fol(fol, env)
                        if e is not None:
                            solver.add(e)
                    except Exception:
                        pass

                try:
                    concl = _parse_fol(conclusion_fol, env)
                    if concl is None:
                        res_q.put(("ok", False, "parse_error"))
                        continue
                    solver.add(z3.Not(concl))
                except Exception:
                    res_q.put(("ok", False, "parse_error"))
                    continue

                result = solver.check()
                if result == z3.unsat:
                    res_q.put(("ok", True, "entails"))
                elif result == z3.sat:
                    res_q.put(("ok", False, "not_entails"))
                else:
                    res_q.put(("ok", False, "unknown"))

            elif task_type == "crash_test":
                import os
                os.abort()

            else:
                res_q.put(("error", f"unknown task type: {task_type}"))

        except Exception as e:
            res_q.put(("error", f"{type(e).__name__}: {e}"))


class Z3Sandbox:
    """Persistent Z3 subprocess. Thread-safe, crash-resilient."""

    def __init__(self):
        self._lock = threading.Lock()
        self._proc = None
        self._req_q = None
        self._res_q = None

    def _ensure_worker(self):
        if self._proc is not None and self._proc.is_alive():
            return
        if self._proc is not None:
            logger.warning(
                "Z3 sandbox worker crashed (exit=%s), restarting",
                self._proc.exitcode,
            )
            self._proc.join(timeout=2)
        ctx = mp.get_context("forkserver")
        self._req_q = ctx.Queue()
        self._res_q = ctx.Queue()
        self._proc = ctx.Process(
            target=_worker_loop,
            args=(self._req_q, self._res_q),
            daemon=True,
        )
        self._proc.start()
        logger.info("Z3 sandbox worker started (pid=%d)", self._proc.pid)

    def _call(self, task, timeout=60):
        with self._lock:
            self._ensure_worker()
            self._req_q.put(task)
            deadline = timeout
            try:
                result = self._res_q.get(timeout=deadline)
                if isinstance(result, tuple) and result[0] == "error":
                    logger.warning("Z3 sandbox error: %s", result[1])
                    return None
                return result[1:]
            except queue.Empty:
                logger.error("Z3 sandbox timed out after %ds", timeout)
                if self._proc.is_alive():
                    self._proc.kill()
                self._proc.join(timeout=5)
                self._proc = None
                return None

    def validate(self, fol_str, vocab):
        """Validate FOL string in subprocess. Returns (valid, error_or_none)."""
        result = self._call(("validate", fol_str, vocab), timeout=10)
        if result is None:
            return False, "Z3 subprocess error or crash"
        return result

    def check_ic(self, fol_strs, vocab, total_claims,
                 premise_fols=None, z3_timeout_ms=30000):
        """Full IC check in subprocess. Returns (is_sat, ic_score, mcs_size)."""
        result = self._call(
            ("check_ic", fol_strs, vocab, total_claims,
             premise_fols or [], z3_timeout_ms),
            timeout=max(120, z3_timeout_ms // 1000 * 3),
        )
        if result is None:
            return True, 0.0, 0
        return result

    def check_sat_set(self, fol_strs, vocab,
                      premise_fols=None, z3_timeout_ms=30000):
        """Check satisfiability of a set of FOL strings. Returns bool."""
        result = self._call(
            ("check_sat_set", fol_strs, vocab,
             premise_fols or [], z3_timeout_ms),
            timeout=max(30, z3_timeout_ms // 1000 * 2),
        )
        if result is None:
            return True
        return result[0]

    def check_entailment(self, claim_fol_strs, vocab,
                         premise_fols, conclusion_fol, z3_timeout_ms=30000):
        """Entailment check in subprocess. Returns (entails, status)."""
        result = self._call(
            ("check_entailment", claim_fol_strs, vocab,
             premise_fols, conclusion_fol, z3_timeout_ms),
            timeout=max(30, z3_timeout_ms // 1000 * 2),
        )
        if result is None:
            return False, "subprocess_error"
        return result

    def crash_test(self):
        """Deliberately crash the worker. Returns True if parent survived."""
        result = self._call(("crash_test",), timeout=5)
        return result is None

    def shutdown(self):
        if self._proc and self._proc.is_alive():
            try:
                self._req_q.put(None)
                self._proc.join(timeout=5)
            except Exception:
                self._proc.kill()


_sandbox = None
_sandbox_lock = threading.Lock()


def get_sandbox() -> Z3Sandbox:
    """Get or create the global Z3 sandbox instance."""
    global _sandbox
    with _sandbox_lock:
        if _sandbox is None:
            _sandbox = Z3Sandbox()
        return _sandbox
