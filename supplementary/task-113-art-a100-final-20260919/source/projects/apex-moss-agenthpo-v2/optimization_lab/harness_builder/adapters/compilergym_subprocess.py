from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
from dataclasses import fields
from pathlib import Path
from typing import Any

from .compilergym import SupervisorResult, frozen_contract


_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_RESULT_FIELDS = {field.name for field in fields(SupervisorResult)}


def _canonical_bytes(payload: Any) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=True,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class CompilerGymSubprocessAdapter:
    """Run the pinned Python-3.10 CompilerGym evaluator as a data-only worker."""

    def __init__(
        self,
        *,
        benchmark_uri: str,
        python_executable: Path,
        project_root: Path,
        site_data_root: Path,
        cache_root: Path,
        compatibility_library_root: Path,
    ) -> None:
        self.benchmark_uri = benchmark_uri
        self.python_executable = python_executable.absolute()
        self.project_root = project_root.resolve(strict=True)
        self.site_data_root = site_data_root.resolve(strict=True)
        self.cache_root = cache_root.resolve(strict=True)
        self.compatibility_library_root = compatibility_library_root.resolve(
            strict=True
        )
        if not self.python_executable.is_file():
            raise ValueError("CompilerGym pinned Python executable is missing")
        # Construction also rejects a URI outside the frozen cBench set.
        self.contract = frozen_contract(benchmark_uri)

    def evaluate(
        self, candidate_path: Path, supervisor_json_path: Path
    ) -> SupervisorResult:
        candidate_path = candidate_path.resolve(strict=True)
        supervisor_json_path = supervisor_json_path.absolute()
        if supervisor_json_path.exists():
            raise RuntimeError("CompilerGym supervisor result path already exists")
        supervisor_json_path.parent.mkdir(parents=True, exist_ok=True)
        command = (
            str(self.python_executable),
            "-m",
            "optimization_lab.harness_builder.adapters.compilergym",
            "evaluate",
            "--benchmark-uri",
            self.benchmark_uri,
            "--candidate",
            str(candidate_path),
            "--supervisor-json",
            str(supervisor_json_path),
        )
        completed = subprocess.run(
            command,
            cwd=self.project_root,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
            timeout=300,
            check=False,
            env={
                "PATH": "/usr/bin:/bin",
                "HOME": str(self.cache_root),
                "PYTHONNOUSERSITE": "1",
                "PYTHONPATH": str(self.project_root),
                "COMPILER_GYM_SITE_DATA": str(self.site_data_root),
                "COMPILER_GYM_CACHE": str(self.cache_root),
                "LD_LIBRARY_PATH": str(self.compatibility_library_root),
                "LANG": "C.UTF-8",
            },
        )
        if completed.returncode not in {0, 2} or not supervisor_json_path.is_file():
            raise RuntimeError(
                "CompilerGym trusted worker failed before producing evidence: "
                + " ".join(completed.stderr.split())[-500:]
            )
        raw = supervisor_json_path.read_bytes()
        try:
            payload = json.loads(raw)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise RuntimeError("CompilerGym supervisor result is invalid JSON") from exc
        if (
            not isinstance(payload, dict)
            or set(payload) != _RESULT_FIELDS
            or _canonical_bytes(payload) != raw
        ):
            raise RuntimeError("CompilerGym supervisor result schema differs")
        result = SupervisorResult(**payload)
        contract_sha = hashlib.sha256(_canonical_bytes(self.contract)).hexdigest()
        if (
            result.schema_version != 1
            or result.contract != self.contract
            or result.contract_sha256 != contract_sha
            or result.candidate_sha256 != _sha(candidate_path)
            or _SHA256.fullmatch(result.candidate_sha256) is None
        ):
            raise RuntimeError("CompilerGym supervisor result binding differs")
        expected_exit = 0 if result.status == "valid" else 2
        if completed.returncode != expected_exit:
            raise RuntimeError("CompilerGym worker exit code and result disagree")
        if result.correct != (result.status == "valid"):
            raise RuntimeError("CompilerGym correctness and status disagree")
        if result.correct and (
            result.normalized_score is None
            or result.normalized_score <= 0
            or not result.replay_verified
            or not result.reward_validated
            or not result.semantics_validated
        ):
            raise RuntimeError("CompilerGym valid result lacks replay evidence")
        return result


__all__ = ["CompilerGymSubprocessAdapter"]
