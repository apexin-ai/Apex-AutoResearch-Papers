from __future__ import annotations

import hashlib
import re
import shlex
import subprocess
import time
from pathlib import Path, PurePosixPath

from optimization_lab.adapters.base import BenchmarkAdapter, EvaluationResult, EvaluationStatus
from optimization_lab.adapters.kernelbench import KernelBenchAdapter, PreflightCheck
from optimization_lab.task_spec import TaskSpec


class SSHKernelBenchAdapter(BenchmarkAdapter):
    """Run the pinned scorer on one explicitly selected GPU behind an SSH alias."""

    def __init__(
        self,
        *,
        host: str,
        remote_repository: str,
        remote_root: str,
        gpu_index: int,
        remote_uv: str,
    ):
        if not re.fullmatch(r"[A-Za-z0-9_.-]+", host):
            raise ValueError("SSH host must be a configured alias")
        for value in (remote_repository, remote_root, remote_uv):
            if not value.startswith("/") or "\n" in value:
                raise ValueError("remote paths must be absolute and single-line")
        if gpu_index < 0:
            raise ValueError("GPU index must be nonnegative")
        self.host = host
        self.remote_repository = PurePosixPath(remote_repository)
        self.remote_root = PurePosixPath(remote_root)
        self.gpu_index = gpu_index
        self.remote_uv = PurePosixPath(remote_uv)
        self.parser = KernelBenchAdapter(repository=Path("/"), mode="local")

    def estimated_gpu_seconds(self, task: TaskSpec) -> float:
        return float(task.timeout_seconds + 120)

    def preflight(self, task: TaskSpec) -> list[PreflightCheck]:
        checks = []
        commit = self._ssh_output(
            ["git", "-C", str(self.remote_repository), "rev-parse", "HEAD"]
        )
        checks.append(
            PreflightCheck(
                "repository_commit",
                "ready" if commit == task.repository_commit else "blocked",
                f"actual={commit or 'unknown'} expected={task.repository_commit}",
            )
        )
        task_path = self.remote_repository / task.task_path
        sha_line = self._ssh_output(["sha256sum", str(task_path)])
        actual_sha = sha_line.split()[0] if sha_line else "missing"
        checks.append(
            PreflightCheck(
                "task_hash",
                "ready" if actual_sha == task.task_sha256 else "blocked",
                f"actual={actual_sha} expected={task.task_sha256}",
            )
        )
        gpu = self._ssh_output(
            [
                "nvidia-smi",
                f"--id={self.gpu_index}",
                "--query-gpu=name,memory.free,utilization.gpu",
                "--format=csv,noheader",
            ]
        )
        checks.append(
            PreflightCheck(
                "gpu",
                "ready" if task.target_gpu in gpu else "blocked",
                gpu or "GPU query failed",
            )
        )
        probe = self._run_remote(
            [
                "env",
                f"CUDA_VISIBLE_DEVICES={self.gpu_index}",
                *self._cache_env(),
                str(self.remote_uv),
                "run",
                "python",
                "-c",
                (
                    "import torch,triton; "
                    "assert torch.cuda.is_available(); "
                    "print(torch.__version__,triton.__version__,torch.cuda.get_device_name(0))"
                ),
            ],
            cwd=self.remote_repository,
            timeout=180,
        )
        checks.append(
            PreflightCheck(
                "python_gpu_stack",
                "ready" if probe.returncode == 0 and task.target_gpu in probe.stdout else "blocked",
                self.parser._summary(probe.stdout),
            )
        )
        return checks

    def evaluate(
        self,
        task: TaskSpec,
        candidate_path: Path,
        private_log_dir: Path,
    ) -> EvaluationResult:
        private_log_dir.mkdir(parents=True, exist_ok=True)
        raw_log_path = private_log_dir / "raw.log"
        candidate_sha = hashlib.sha256(candidate_path.read_bytes()).hexdigest()
        remote_candidates = self.remote_root / "candidates"
        remote_candidate = remote_candidates / f"{candidate_sha}.py"
        mkdir = self._run_remote(["mkdir", "-p", str(remote_candidates)], timeout=30)
        if mkdir.returncode != 0:
            return self._environment_failure(mkdir.stdout, raw_log_path)
        transfer = subprocess.run(
            [
                "rsync",
                "-az",
                "-e",
                "ssh -o BatchMode=yes",
                str(candidate_path),
                f"{self.host}:{remote_candidate}",
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=120,
            check=False,
        )
        if transfer.returncode != 0:
            return self._environment_failure(transfer.stdout, raw_log_path)
        command = [
            "env",
            f"CUDA_VISIBLE_DEVICES={self.gpu_index}",
            *self._cache_env(),
            "LITELLM_LOCAL_MODEL_COST_MAP=True",
            str(self.remote_uv),
            "run",
            "python",
            "scripts/run_and_check.py",
            "ref_origin=kernelbench",
            "dataset_src=local",
            f"level={task.level}",
            f"problem_id={task.problem_id}",
            f"kernel_src_path={remote_candidate}",
            "eval_mode=local",
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
            process = self._run_remote(
                command,
                cwd=self.remote_repository,
                timeout=task.timeout_seconds + 180,
            )
        except subprocess.TimeoutExpired as exc:
            elapsed = time.monotonic() - started
            output = (exc.stdout or "") + "\nSSH KernelBench timeout"
            raw_log_path.write_text(output, encoding="utf-8")
            return EvaluationResult(
                status=EvaluationStatus.TIMEOUT,
                compiled=False,
                correct=False,
                error_summary="SSH KernelBench timeout",
                elapsed_seconds=elapsed,
                gpu_seconds=elapsed,
                hardware=task.target_gpu,
                raw_log_path=str(raw_log_path),
            )
        elapsed = time.monotonic() - started
        raw_log_path.write_text(process.stdout, encoding="utf-8")
        return self.parser.parse_result(
            process.stdout,
            returncode=process.returncode,
            elapsed_seconds=elapsed,
            raw_log_path=raw_log_path,
            task=task,
        )

    def _cache_env(self) -> list[str]:
        cache = self.remote_root / "cache"
        return [
            f"PYTHONPATH={self.remote_repository / 'src'}",
            f"UV_CACHE_DIR={cache / 'uv'}",
            f"XDG_CACHE_HOME={cache / 'xdg'}",
            f"TMPDIR={self.remote_root / 'tmp'}",
            f"TORCH_EXTENSIONS_DIR={cache / 'torch_extensions'}",
            f"TRITON_CACHE_DIR={cache / 'triton'}",
            (
                f"C_INCLUDE_PATH={self.remote_root / 'python-dev/usr/include/python3.10'}:"
                f"{self.remote_root / 'python-dev/usr/include'}"
            ),
        ]

    def _environment_failure(self, output: str, raw_log_path: Path) -> EvaluationResult:
        raw_log_path.write_text(output, encoding="utf-8")
        return EvaluationResult(
            status=EvaluationStatus.ENVIRONMENT_INVALID,
            compiled=False,
            correct=False,
            error_summary=self.parser._summary(output),
            raw_log_path=str(raw_log_path),
        )

    def _ssh_output(self, command: list[str]) -> str:
        result = self._run_remote(command, timeout=30)
        return result.stdout.strip() if result.returncode == 0 else ""

    def _run_remote(
        self,
        command: list[str],
        *,
        cwd: PurePosixPath | None = None,
        timeout: int,
    ) -> subprocess.CompletedProcess[str]:
        command_text = shlex.join(command)
        if cwd is not None:
            command_text = f"cd {shlex.quote(str(cwd))} && {command_text}"
        return subprocess.run(
            [
                "ssh",
                "-o",
                "BatchMode=yes",
                "-o",
                "ConnectTimeout=12",
                self.host,
                command_text,
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
        )
