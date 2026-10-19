from __future__ import annotations

import hashlib
import json
import re
import shlex
import subprocess
import time
import uuid
from pathlib import Path, PurePosixPath
from typing import Any

from optimization_lab.feedback import FeedbackCard
from optimization_lab.profiling import (
    HARDWARE_COUNTER_METRICS,
    ProfileSummary,
    ProfilerCapabilities,
    static_structure_signature,
)
from optimization_lab.task_spec import TaskSpec


class SSHTierAProfiler:
    """Collect nsys timeline and Triton compiler evidence without privileged counters."""

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
            raise ValueError("SSH profiler host must be a configured alias")
        for value in (remote_repository, remote_root, remote_uv):
            if not value.startswith("/") or "\n" in value:
                raise ValueError("SSH profiler paths must be absolute and single-line")
        if gpu_index < 0:
            raise ValueError("SSH profiler GPU index must be nonnegative")
        self.host = host
        self.remote_repository = PurePosixPath(remote_repository)
        self.remote_root = PurePosixPath(remote_root)
        self.gpu_index = gpu_index
        self.remote_uv = PurePosixPath(remote_uv)
        self._capabilities: ProfilerCapabilities | None = None

    def capabilities(self) -> ProfilerCapabilities:
        if self._capabilities is not None:
            return self._capabilities
        probe = self._run_remote(
            [
                "sh",
                "-c",
                (
                    "for x in nsys ncu ptxas cuobjdump nvdisasm; do "
                    "if command -v $x >/dev/null 2>&1; then echo $x=yes; "
                    "else echo $x=no; fi; done; "
                    "if [ -r /proc/driver/nvidia/params ]; then "
                    "grep '^RmProfilingAdminOnly:' /proc/driver/nvidia/params || true; fi"
                ),
            ],
            timeout=30,
        )
        facts: dict[str, str] = {}
        for line in probe.stdout.splitlines():
            if "=" in line:
                key, value = line.strip().split("=", 1)
                facts[key] = value
        admin_only = "RmProfilingAdminOnly: 1" in probe.stdout
        nsys = facts.get("nsys") == "yes"
        ncu = facts.get("ncu") == "yes"
        counters = ncu and not admin_only
        detail = (
            "Tier A timeline/compiler evidence available; hardware counters unavailable"
            if nsys and not counters
            else "Profiler capability probe completed"
        )
        self._capabilities = ProfilerCapabilities(
            nsys=nsys,
            ncu=ncu,
            hardware_counters=counters,
            ptxas=facts.get("ptxas") == "yes",
            cuobjdump=facts.get("cuobjdump") == "yes",
            detail=detail,
        )
        return self._capabilities

    def estimated_gpu_seconds(self, task: TaskSpec, level: str) -> float:
        if level not in {"light", "full"}:
            raise ValueError("profile level must be light or full")
        return 0.0 if level == "light" else float(min(task.timeout_seconds + 300, 600))

    def profile(
        self,
        *,
        task: TaskSpec,
        candidate_path: Path,
        candidate_id: str,
        feedback: FeedbackCard,
        level: str,
        private_log_dir: Path,
    ) -> ProfileSummary:
        if not feedback.correct or feedback.speedup_vs_eager is None:
            raise ValueError("profiler requires an already-correct scored candidate")
        if feedback.candidate_runtime_ms is None or feedback.reference_runtime_ms is None:
            raise ValueError("profiler requires public candidate and reference runtimes")
        candidate_path = candidate_path.resolve()
        if not candidate_path.is_file():
            raise ValueError("profile candidate is missing")
        source = candidate_path.read_text(encoding="utf-8")
        candidate_sha = hashlib.sha256(candidate_path.read_bytes()).hexdigest()
        structure = static_structure_signature(source)
        signature = hashlib.sha256(
            json.dumps(structure, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()[:20]
        if level == "light":
            return self._light_summary(
                task=task,
                candidate_id=candidate_id,
                candidate_sha=candidate_sha,
                feedback=feedback,
                structure=structure,
                signature=signature,
            )
        if level != "full":
            raise ValueError("profile level must be light or full")
        private_log_dir.mkdir(parents=True, exist_ok=True)
        capabilities = self.capabilities()
        if not capabilities.nsys:
            return self._full_unavailable(
                task=task,
                candidate_id=candidate_id,
                candidate_sha=candidate_sha,
                feedback=feedback,
                structure=structure,
                signature=signature,
                detail="nsys is unavailable on the selected host",
            )

        run_label = f"{candidate_sha[:16]}-{uuid.uuid4().hex[:12]}"
        remote_profile = self.remote_root / "profiles/p2b" / run_label
        remote_cache = remote_profile / "cache"
        remote_tmp = remote_profile / "tmp"
        remote_candidate = remote_profile / "candidate.py"
        remote_helper = remote_profile / "profile_cache_summary.py"
        mkdir = self._run_remote(
            ["mkdir", "-p", str(remote_cache), str(remote_tmp)], timeout=30
        )
        if mkdir.returncode != 0:
            raise RuntimeError("could not create the remote P2b profiler directory")
        helper = Path(__file__).with_name("profile_cache_summary.py")
        candidate_transfer = self._rsync_file(candidate_path, remote_candidate)
        helper_transfer = self._rsync_file(helper, remote_helper)
        if candidate_transfer.returncode != 0 or helper_transfer.returncode != 0:
            raise RuntimeError("could not transfer the P2b profiler inputs")

        command = [
            "env",
            f"CUDA_VISIBLE_DEVICES={self.gpu_index}",
            *self._cache_env(remote_cache=remote_cache, remote_tmp=remote_tmp),
            "LITELLM_LOCAL_MODEL_COST_MAP=True",
            "nsys",
            "profile",
            "--trace=cuda,nvtx",
            "--sample=none",
            "--cpuctxsw=none",
            "--force-overwrite=true",
            f"--output={remote_profile / 'trace'}",
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
            "num_correct_trials=1",
            "num_perf_trials=5",
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
            profiled = self._run_remote(
                command,
                cwd=self.remote_repository,
                timeout=task.timeout_seconds + 300,
            )
        except subprocess.TimeoutExpired as exc:
            profiled = subprocess.CompletedProcess(
                args=command,
                returncode=124,
                stdout=(exc.stdout or "") + "\nProfiler timeout",
            )
        elapsed = time.monotonic() - started

        trace_path = remote_profile / "trace.nsys-rep"
        stats = self._run_remote(
            [
                "nsys",
                "stats",
                "--report",
                "cuda_gpu_kern_sum",
                "--format",
                "json",
                str(trace_path),
            ],
            timeout=240,
        )
        compiler = self._run_remote(
            [
                "python3",
                str(remote_helper),
                "--cache-root",
                str(remote_cache),
                "--candidate-source",
                str(remote_candidate),
            ],
            timeout=180,
        )
        timeline_rows = parse_nsys_json(stats.stdout) if stats.returncode == 0 else []
        compiler_data = _parse_json_object(compiler.stdout) if compiler.returncode == 0 else {}
        expected_names = [str(item) for item in structure.get("triton_kernel_names", [])]
        matched_rows = [
            row
            for row in timeline_rows
            if any(name in str(row.get("Name", "")) for name in expected_names)
        ]
        self._archive_private(
            private_log_dir=private_log_dir,
            remote_profile=remote_profile,
            profiled_output=profiled.stdout,
            stats_output=stats.stdout,
            compiler_output=compiler.stdout,
        )
        return self._full_summary(
            task=task,
            candidate_id=candidate_id,
            candidate_sha=candidate_sha,
            feedback=feedback,
            structure=structure,
            signature=signature,
            profile_returncode=profiled.returncode,
            timeline_rows=matched_rows,
            compiler=compiler_data,
            gpu_seconds=elapsed,
        )

    def _light_summary(
        self,
        *,
        task: TaskSpec,
        candidate_id: str,
        candidate_sha: str,
        feedback: FeedbackCard,
        structure: dict[str, Any],
        signature: str,
    ) -> ProfileSummary:
        warps = structure.get("num_warps_values") or []
        stages = structure.get("num_stages_values") or []
        missing = {
            "launch_count",
            "registers_per_thread",
            "register_spills",
            "shared_memory_bytes",
            "theoretical_occupancy_pct",
            *HARDWARE_COUNTER_METRICS,
        }
        return ProfileSummary(
            task_id=task.task_id,
            candidate_id=candidate_id,
            candidate_sha256=candidate_sha,
            level="light",
            status="complete",
            candidate_runtime_ms=float(feedback.candidate_runtime_ms),
            reference_runtime_ms=float(feedback.reference_runtime_ms),
            speedup=float(feedback.speedup_vs_eager),
            structural_signature=signature,
            structure=structure,
            kernel_count=int(structure.get("triton_kernel_count", 0)) or None,
            num_warps=max(warps) if warps else None,
            num_stages=max(stages) if stages else None,
            compiler_summary=(
                f"Static AST found {int(structure.get('triton_kernel_count', 0))} Triton kernels.",
                "No GPU profiler was invoked for this light evidence pass.",
            ),
            missing_metrics=tuple(sorted(missing)),
            gpu_seconds=0.0,
        )

    def _full_summary(
        self,
        *,
        task: TaskSpec,
        candidate_id: str,
        candidate_sha: str,
        feedback: FeedbackCard,
        structure: dict[str, Any],
        signature: str,
        profile_returncode: int,
        timeline_rows: list[dict[str, Any]],
        compiler: dict[str, Any],
        gpu_seconds: float,
    ) -> ProfileSummary:
        launches = sum(int(row.get("Instances", 0) or 0) for row in timeline_rows)
        names = {str(row.get("Name", "")) for row in timeline_rows if row.get("Name")}
        metadata = compiler.get("metadata") if isinstance(compiler.get("metadata"), list) else []
        kernel_count = len(names) or len(metadata) or int(structure.get("triton_kernel_count", 0))
        timeline_summary = tuple(
            (
                f"{str(row.get('Name', 'kernel'))[:160]}: "
                f"{int(row.get('Instances', 0) or 0)} launches, "
                f"{float(row.get('Avg (ns)', 0) or 0) / 1000:.2f} us average."
            )
            for row in sorted(
                timeline_rows,
                key=lambda item: float(item.get("Total Time (ns)", 0) or 0),
                reverse=True,
            )[:8]
        )
        compiler_summary = [f"Compiler cache identified {len(metadata)} candidate Triton kernels."]
        if compiler.get("registers_per_thread") is not None:
            compiler_summary.append(
                f"Maximum static register allocation: {int(compiler['registers_per_thread'])} registers per thread."
            )
        if compiler.get("shared_memory_bytes") is not None:
            compiler_summary.append(
                f"Maximum shared-memory allocation: {int(compiler['shared_memory_bytes'])} bytes per kernel."
            )
        if compiler.get("local_memory_bytes") is not None:
            compiler_summary.append(
                f"Maximum compiler-reported local memory: {int(compiler['local_memory_bytes'])} bytes; this is not labeled as a spill count."
            )
        if compiler.get("theoretical_occupancy_pct") is not None:
            compiler_summary.append(
                "Static A100 occupancy estimate: "
                f"{float(compiler['theoretical_occupancy_pct']):.1f}%; not a measured achieved-occupancy counter."
            )
        missing = set(HARDWARE_COUNTER_METRICS) | {"register_spills"}
        values = {
            "kernel_count": kernel_count or None,
            "launch_count": launches or None,
            "registers_per_thread": _optional_int(compiler.get("registers_per_thread")),
            "shared_memory_bytes": _optional_int(compiler.get("shared_memory_bytes")),
            "num_warps": _optional_int(compiler.get("num_warps")),
            "num_stages": _optional_int(compiler.get("num_stages")),
            "theoretical_occupancy_pct": _optional_float(
                compiler.get("theoretical_occupancy_pct")
            ),
        }
        for key, value in values.items():
            if value is None:
                missing.add(key)
        tier_a_complete = profile_returncode == 0 and bool(timeline_rows) and bool(metadata)
        return ProfileSummary(
            task_id=task.task_id,
            candidate_id=candidate_id,
            candidate_sha256=candidate_sha,
            level="full",
            status="complete" if tier_a_complete else "partial",
            candidate_runtime_ms=float(feedback.candidate_runtime_ms),
            reference_runtime_ms=float(feedback.reference_runtime_ms),
            speedup=float(feedback.speedup_vs_eager),
            structural_signature=signature,
            structure=structure,
            **values,
            timeline_summary=timeline_summary,
            compiler_summary=tuple(compiler_summary),
            missing_metrics=tuple(sorted(missing)),
            gpu_seconds=gpu_seconds,
        )

    def _full_unavailable(
        self,
        *,
        task: TaskSpec,
        candidate_id: str,
        candidate_sha: str,
        feedback: FeedbackCard,
        structure: dict[str, Any],
        signature: str,
        detail: str,
    ) -> ProfileSummary:
        missing = {
            "launch_count",
            "registers_per_thread",
            "register_spills",
            "shared_memory_bytes",
            "num_warps",
            "num_stages",
            "theoretical_occupancy_pct",
            *HARDWARE_COUNTER_METRICS,
        }
        return ProfileSummary(
            task_id=task.task_id,
            candidate_id=candidate_id,
            candidate_sha256=candidate_sha,
            level="full",
            status="unavailable",
            candidate_runtime_ms=float(feedback.candidate_runtime_ms),
            reference_runtime_ms=float(feedback.reference_runtime_ms),
            speedup=float(feedback.speedup_vs_eager),
            structural_signature=signature,
            structure=structure,
            kernel_count=int(structure.get("triton_kernel_count", 0)) or None,
            compiler_summary=(detail,),
            missing_metrics=tuple(sorted(missing)),
        )

    def _archive_private(
        self,
        *,
        private_log_dir: Path,
        remote_profile: PurePosixPath,
        profiled_output: str,
        stats_output: str,
        compiler_output: str,
    ) -> None:
        (private_log_dir / "raw.log").write_text(
            profiled_output + "\n\n--- nsys stats ---\n" + stats_output
            + "\n\n--- compiler summary ---\n" + compiler_output,
            encoding="utf-8",
        )
        (private_log_dir / "remote_manifest.json").write_text(
            json.dumps(
                {
                    "remote_profile_root": str(remote_profile),
                    "trace": str(remote_profile / "trace.nsys-rep"),
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        transfer = subprocess.run(
            [
                "rsync",
                "-az",
                "-e",
                "ssh -o BatchMode=yes",
                f"{self.host}:{remote_profile}/trace.nsys-rep",
                f"{self.host}:{remote_profile}/cache/",
                str(private_log_dir),
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=240,
            check=False,
        )
        if transfer.returncode != 0:
            (private_log_dir / "archive_warning.txt").write_text(
                "Private remote profiler artifacts could not be copied locally.\n",
                encoding="utf-8",
            )

    def _cache_env(
        self, *, remote_cache: PurePosixPath, remote_tmp: PurePosixPath
    ) -> list[str]:
        shared_cache = self.remote_root / "cache"
        return [
            f"UV_CACHE_DIR={shared_cache / 'uv'}",
            f"XDG_CACHE_HOME={shared_cache / 'xdg'}",
            f"TMPDIR={remote_tmp}",
            f"TORCH_EXTENSIONS_DIR={shared_cache / 'torch_extensions'}",
            f"TRITON_CACHE_DIR={remote_cache}",
            (
                f"C_INCLUDE_PATH={self.remote_root / 'python-dev/usr/include/python3.10'}:"
                f"{self.remote_root / 'python-dev/usr/include'}"
            ),
        ]

    def _rsync_file(
        self, local_path: Path, remote_path: PurePosixPath
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                "rsync",
                "-az",
                "-e",
                "ssh -o BatchMode=yes",
                str(local_path),
                f"{self.host}:{remote_path}",
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=120,
            check=False,
        )

    def _run_remote(
        self,
        command: list[str],
        *,
        timeout: int,
        cwd: PurePosixPath | None = None,
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


def parse_nsys_json(output: str) -> list[dict[str, Any]]:
    decoder = json.JSONDecoder()
    for index, character in enumerate(output):
        if character != "[":
            continue
        try:
            value, _ = decoder.raw_decode(output[index:])
        except json.JSONDecodeError:
            continue
        if isinstance(value, list) and all(isinstance(item, dict) for item in value):
            if not value or any("Name" in item for item in value):
                return value
    return []


def _parse_json_object(output: str) -> dict[str, Any]:
    decoder = json.JSONDecoder()
    for index, character in enumerate(output):
        if character != "{":
            continue
        try:
            value, _ = decoder.raw_decode(output[index:])
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            return value
    return {}


def _optional_int(value: object) -> int | None:
    return int(value) if isinstance(value, (int, float)) and value >= 0 else None


def _optional_float(value: object) -> float | None:
    return float(value) if isinstance(value, (int, float)) and value >= 0 else None
