from __future__ import annotations

import hashlib
import re
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

from optimization_lab.adapters.base import (
    BenchmarkAdapter,
    EvaluationResult,
    EvaluationStatus,
)
from optimization_lab.task_spec import TaskSpec


@dataclass(frozen=True)
class PreflightCheck:
    name: str
    status: str
    detail: str

    @property
    def ready(self) -> bool:
        return self.status == "ready"

    def to_dict(self) -> dict[str, str]:
        return {"name": self.name, "status": self.status, "detail": self.detail}


class KernelBenchAdapter(BenchmarkAdapter):
    """Thin wrapper around KernelBench's pinned official ``run_and_check.py``."""

    _ENVIRONMENT_SIGNALS = (
        "gpu not attached",
        "cuda is not available",
        "no cuda gpus are available",
        "no module named",
        "modal token",
        "authentication required",
        "failed to initialize nvml",
        "nvidia driver",
        "could not select device",
    )

    def __init__(
        self,
        *,
        repository: Path,
        mode: str,
        uv_executable: str = "uv",
    ):
        if mode not in {"local", "modal"}:
            raise ValueError("KernelBench mode must be local or modal")
        self.repository = repository.resolve()
        self.mode = mode
        self.uv_executable = uv_executable

    def preflight(
        self,
        task: TaskSpec,
        *,
        check_executor: bool = True,
    ) -> list[PreflightCheck]:
        checks: list[PreflightCheck] = []
        if not (self.repository / ".git").exists():
            return [
                PreflightCheck(
                    "repository", "blocked", f"不是 Git checkout：{self.repository}"
                )
            ]
        checks.append(PreflightCheck("repository", "ready", str(self.repository)))
        commit = self._command_output(
            ["git", "-C", str(self.repository), "rev-parse", "HEAD"]
        )
        checks.append(
            PreflightCheck(
                "repository_commit",
                "ready" if commit == task.repository_commit else "blocked",
                f"actual={commit or 'unknown'} expected={task.repository_commit}",
            )
        )
        task_path = self.repository / task.task_path
        actual_sha = hashlib.sha256(task_path.read_bytes()).hexdigest() if task_path.is_file() else "missing"
        checks.append(
            PreflightCheck(
                "task_hash",
                "ready" if actual_sha == task.task_sha256 else "blocked",
                f"{task.task_path} actual={actual_sha} expected={task.task_sha256}",
            )
        )
        script = self.repository / "scripts/run_and_check.py"
        checks.append(
            PreflightCheck(
                "official_evaluator",
                "ready" if script.is_file() else "blocked",
                str(script),
            )
        )
        uv_path = shutil.which(self.uv_executable)
        checks.append(
            PreflightCheck(
                "uv",
                "ready" if uv_path else "blocked",
                uv_path or f"找不到 {self.uv_executable}",
            )
        )
        if check_executor and uv_path:
            checks.append(self._executor_check(task))
        return checks

    def _executor_check(self, task: TaskSpec) -> PreflightCheck:
        if self.mode == "local":
            command = [
                self.uv_executable,
                "run",
                "python",
                "-c",
                (
                    "import torch; "
                    "assert torch.cuda.is_available(), 'CUDA is not available'; "
                    "print(torch.cuda.get_device_name(0))"
                ),
            ]
            name = "local_gpu"
        else:
            command = [self.uv_executable, "run", "modal", "profile", "current"]
            name = "modal_gpu"
        try:
            result = subprocess.run(
                command,
                cwd=self.repository,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=180,
                check=False,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            return PreflightCheck(name, "blocked", str(exc))
        detail = self._summary(result.stdout)
        if result.returncode == 0:
            return PreflightCheck(
                name,
                "ready",
                detail or f"{task.target_gpu} executor available",
            )
        return PreflightCheck(name, "blocked", detail or "executor check failed")

    def estimated_gpu_seconds(self, task: TaskSpec) -> float:
        return float(task.timeout_seconds + 60)

    def evaluate(
        self,
        task: TaskSpec,
        candidate_path: Path,
        private_log_dir: Path,
    ) -> EvaluationResult:
        private_log_dir.mkdir(parents=True, exist_ok=True)
        raw_log_path = private_log_dir / "raw.log"
        command = [
            self.uv_executable,
            "run",
            "python",
            "scripts/run_and_check.py",
            "ref_origin=kernelbench",
            "dataset_src=local",
            f"level={task.level}",
            f"problem_id={task.problem_id}",
            f"kernel_src_path={candidate_path}",
            f"eval_mode={self.mode}",
            f"gpu={task.target_gpu}",
            f"num_correct_trials={task.correctness_trials}",
            f"num_perf_trials={task.performance_trials}",
            f"timeout={task.timeout_seconds}",
            f"precision={task.precision}",
            f"backend={task.backend}",
            "check_kernel=true",
            "--list",
            "gpu_arch",
            task.gpu_arch,
            "list--",
        ]
        started = time.monotonic()
        try:
            process = subprocess.run(
                command,
                cwd=self.repository,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=task.timeout_seconds + 120,
                check=False,
            )
            output = process.stdout
            returncode = process.returncode
        except subprocess.TimeoutExpired as exc:
            output = (exc.stdout or "") + "\nKernelBench wrapper timeout"
            returncode = 124
            elapsed = time.monotonic() - started
            raw_log_path.write_text(output, encoding="utf-8")
            return EvaluationResult(
                status=EvaluationStatus.TIMEOUT,
                compiled=False,
                correct=False,
                error_summary="KernelBench wrapper timeout",
                elapsed_seconds=elapsed,
                gpu_seconds=elapsed,
                hardware=task.target_gpu,
                raw_log_path=str(raw_log_path),
            )
        elapsed = time.monotonic() - started
        raw_log_path.write_text(output, encoding="utf-8")
        return self.parse_result(
            output,
            returncode=returncode,
            elapsed_seconds=elapsed,
            raw_log_path=raw_log_path,
            task=task,
        )

    def parse_result(
        self,
        output: str,
        *,
        returncode: int,
        elapsed_seconds: float,
        raw_log_path: Path,
        task: TaskSpec,
    ) -> EvaluationResult:
        lowered = output.lower()
        environment_failure = any(signal in lowered for signal in self._ENVIRONMENT_SIGNALS)
        compiled_match = re.search(r"\bcompiled=(True|False)\b", output)
        correct_match = re.search(r"\bcorrectness=(True|False)\b", output)
        compiled = bool(compiled_match and compiled_match.group(1) == "True")
        correct = bool(correct_match and correct_match.group(1) == "True")
        hardware_match = re.search(
            r"['\"]?hardware['\"]?\s*[:=]\s*['\"]([^'\"]+)", output
        )
        hardware = hardware_match.group(1) if hardware_match else task.target_gpu
        common = {
            "elapsed_seconds": elapsed_seconds,
            "hardware": hardware,
            "raw_log_path": str(raw_log_path),
        }
        if environment_failure:
            return EvaluationResult(
                status=EvaluationStatus.ENVIRONMENT_INVALID,
                compiled=False,
                correct=False,
                error_summary=self._summary(output),
                gpu_seconds=0.0,
                **common,
            )
        if "static check failed" in lowered:
            return EvaluationResult(
                status=EvaluationStatus.POLICY_REJECTED,
                compiled=False,
                correct=False,
                error_summary=self._summary(output),
                gpu_seconds=elapsed_seconds,
                **common,
            )
        if returncode != 0 and not compiled_match:
            return EvaluationResult(
                status=EvaluationStatus.ENVIRONMENT_INVALID,
                compiled=False,
                correct=False,
                error_summary=self._summary(output),
                gpu_seconds=0.0,
                **common,
            )
        if not compiled:
            return EvaluationResult(
                status=EvaluationStatus.COMPILE_FAILED,
                compiled=False,
                correct=False,
                error_summary=self._summary(output),
                gpu_seconds=elapsed_seconds,
                **common,
            )
        if not correct:
            return EvaluationResult(
                status=EvaluationStatus.INCORRECT,
                compiled=True,
                correct=False,
                error_summary=self._summary(output),
                gpu_seconds=elapsed_seconds,
                **common,
            )
        candidate_runtime = self._timing(output, "Custom Kernel exec time")
        reference_runtime = self._timing(output, "PyTorch Reference Eager exec time")
        compile_runtime = self._timing(output, "PyTorch Reference torch.compile time")
        if candidate_runtime is None or reference_runtime is None:
            return EvaluationResult(
                status=EvaluationStatus.ENVIRONMENT_INVALID,
                compiled=True,
                correct=True,
                error_summary="official scorer returned correctness without complete timing",
                gpu_seconds=elapsed_seconds,
                **common,
            )
        return EvaluationResult(
            status=EvaluationStatus.VALID,
            compiled=True,
            correct=True,
            candidate_runtime_ms=candidate_runtime,
            reference_runtime_ms=reference_runtime,
            reference_compile_runtime_ms=compile_runtime,
            gpu_seconds=elapsed_seconds,
            **common,
        )

    @staticmethod
    def _timing(output: str, label: str) -> float | None:
        match = re.search(re.escape(label) + r":\s*([0-9]+(?:\.[0-9]+)?)\s*ms", output)
        return float(match.group(1)) if match else None

    @staticmethod
    def _summary(output: str) -> str:
        lines = [line.strip() for line in output.splitlines() if line.strip()]
        if not lines:
            return "no evaluator output"
        return " | ".join(lines[-6:])[-800:]

    @staticmethod
    def _command_output(command: list[str]) -> str:
        try:
            return subprocess.check_output(command, text=True, stderr=subprocess.DEVNULL).strip()
        except (OSError, subprocess.CalledProcessError):
            return ""
