from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from optimization_lab.generation import GeneratedCandidate, InvalidCandidate

from .adapters.compilergym import ActionSequenceCandidate, CandidatePolicyError
from .adapters.kernel_candidate_policy import (
    RestrictedKernelCandidateError,
    RestrictedKernelCandidatePolicy,
)
from .adapters.lcbench import LCBenchCandidatePolicyError, LCBenchQueryBatch
from .adapters.sweperf import PatchContractError, validate_unified_diff
from .contract_compatibility import (
    ContractCompatibilityError,
    SWEBENCH_VERIFIED_CAPABILITY,
    compilergym_capability,
    lcbench_capability,
    normalize_swebench_verified_response,
    patch_contract_reason_code,
)


_SAFE_COMPONENT = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")
_SAFE_CELL = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_PYTHON_FENCE = re.compile(
    r"\s*```(?:python|py)?\s*\n(.*?)```\s*", re.DOTALL | re.IGNORECASE
)
_JSON_FENCE = re.compile(r"\s*```(?:json)?\s*\n(.*?)```\s*", re.DOTALL | re.IGNORECASE)
_DIFF_FENCE = re.compile(
    r"\s*```(?:diff|patch)?\s*\n(.*?)```\s*", re.DOTALL | re.IGNORECASE
)
_KERNELBENCHX_DATASET_SEPARATOR = "#" * 146


class SolutionContractError(ValueError):
    """A model response cannot become one formal solution artifact."""

    def __init__(self, message: str, *, reason_code: str | None = None) -> None:
        super().__init__(message)
        self.reason_code = reason_code or patch_contract_reason_code(message)


@dataclass(frozen=True)
class SolutionArtifact:
    raw_response: str
    text: str
    sha256: str
    structural_signature: str
    extension: str
    artifact_kind: str
    compatibility_trace: dict[str, Any] | None = None


class KernelBenchSolutionCodec:
    """Freeze and statically gate one restricted KernelBench candidate."""

    output_mode = "python_candidate"

    def __init__(self, *, task_id: str | None = None) -> None:
        self._task_id = task_id
        self._policy = RestrictedKernelCandidatePolicy()

    def parse(self, raw_response: str) -> SolutionArtifact:
        try:
            candidate = GeneratedCandidate.from_response(raw_response)
        except InvalidCandidate as exc:
            raise SolutionContractError(str(exc)) from exc
        try:
            self._policy.validate(candidate.code, task_id=self._task_id)
        except RestrictedKernelCandidateError as exc:
            raise SolutionContractError(str(exc)) from exc
        tree = ast.parse(candidate.code)
        imports = sorted(
            {
                alias.name.split(".", 1)[0]
                for node in ast.walk(tree)
                if isinstance(node, ast.Import)
                for alias in node.names
            }
            | {
                (node.module or "").split(".", 1)[0]
                for node in ast.walk(tree)
                if isinstance(node, ast.ImportFrom)
            }
        )
        calls = sorted(
            {
                node.func.id
                if isinstance(node.func, ast.Name)
                else node.func.attr
                if isinstance(node.func, ast.Attribute)
                else "dynamic"
                for node in ast.walk(tree)
                if isinstance(node, ast.Call)
            }
        )
        classes = sorted(
            node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)
        )
        return SolutionArtifact(
            raw_response=raw_response,
            text=candidate.code,
            sha256=candidate.sha256,
            structural_signature=_structure_sha(
                {
                    "classes": classes,
                    "imports": imports,
                    "calls": calls,
                }
            ),
            extension=".py",
            artifact_kind="kernelbench_modelnew_python",
        )


@dataclass(frozen=True)
class StoredSolution:
    cell_id: str
    candidate_id: str
    artifact_sha256: str
    artifact_path: Path
    raw_response_path: Path
    metadata_path: Path


def _structure_sha(payload: dict[str, Any]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    return hashlib.sha256(encoded).hexdigest()


class KernelBenchXSolutionCodec:
    output_mode = "python_candidate"

    def __init__(self, *, task_id: str) -> None:
        if not task_id.endswith(".py") or task_id.startswith("/") or ".." in task_id:
            raise ValueError("unsafe KernelBenchX task id")
        self.task_id = task_id
        self.expected_entrypoint = Path(task_id).stem

    def parse(self, raw_response: str) -> SolutionArtifact:
        if not isinstance(raw_response, str) or len(raw_response) > 1_048_576:
            raise SolutionContractError("KernelBenchX response is empty or too large")
        match = _PYTHON_FENCE.fullmatch(raw_response)
        if match is None:
            raise SolutionContractError(
                "KernelBenchX code fence must occupy the whole response"
            )
        return self._parse_code(match.group(1), raw_response=raw_response)

    def reference_canary_from_frozen_task_source(
        self,
        task_source: str,
        *,
        expected_task_sha256: str,
    ) -> SolutionArtifact:
        """Derive one implementation-only canary through the formal codec.

        KernelBenchX dataset files contain both the oracle implementation and
        public tests.  They are task specifications, not candidate artifacts.
        The evaluator canary may mechanically extract the implementation only
        after binding the complete source to its frozen digest; the extracted
        bytes then pass through the same parser used for model output.
        """

        if not isinstance(task_source, str) or len(task_source) > 1_048_576:
            raise SolutionContractError("KernelBenchX task source is empty or too large")
        try:
            encoded = task_source.encode("utf-8")
        except UnicodeEncodeError as exc:
            raise SolutionContractError("KernelBenchX task source is not UTF-8") from exc
        if not re.fullmatch(r"[0-9a-f]{64}", expected_task_sha256):
            raise SolutionContractError("KernelBenchX task source hash is invalid")
        if hashlib.sha256(encoded).hexdigest() != expected_task_sha256:
            raise SolutionContractError("KernelBenchX task source hash differs")
        if task_source.count(_KERNELBENCHX_DATASET_SEPARATOR) != 1:
            raise SolutionContractError(
                "KernelBenchX frozen task must have one dataset separator"
            )
        implementation, public_tests = task_source.split(
            _KERNELBENCHX_DATASET_SEPARATOR, 1
        )
        if "def test_" not in public_tests or "test_results" not in public_tests:
            raise SolutionContractError(
                "KernelBenchX frozen task lacks the public test contract"
            )
        raw_response = f"```python\n{implementation.strip()}\n```"
        return self.parse(raw_response)

    def _parse_code(self, value: str, *, raw_response: str) -> SolutionArtifact:
        code = value.strip() + "\n"
        if _KERNELBENCHX_DATASET_SEPARATOR in code:
            raise SolutionContractError("dataset separator and embedded tests are forbidden")
        try:
            tree = ast.parse(code)
        except SyntaxError as exc:
            raise SolutionContractError(f"KernelBenchX Python syntax error: {exc.msg}") from exc
        functions = [
            node
            for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]
        if not any(
            node.name in {"kernel_function", self.expected_entrypoint}
            for node in functions
        ):
            raise SolutionContractError(
                "KernelBenchX candidate lacks the frozen top-level entrypoint"
            )
        imports = sorted(
            {
                alias.name.split(".", 1)[0]
                for node in ast.walk(tree)
                if isinstance(node, ast.Import)
                for alias in node.names
            }
            | {
                (node.module or "").split(".", 1)[0]
                for node in ast.walk(tree)
                if isinstance(node, ast.ImportFrom)
            }
        )
        calls = sorted(
            {
                node.func.id
                if isinstance(node.func, ast.Name)
                else node.func.attr
                if isinstance(node.func, ast.Attribute)
                else "dynamic"
                for node in ast.walk(tree)
                if isinstance(node, ast.Call)
            }
        )
        signature = _structure_sha(
            {
                "functions": sorted(node.name for node in functions),
                "imports": imports,
                "calls": calls,
                "function_count": len(functions),
            }
        )
        return SolutionArtifact(
            raw_response=raw_response,
            text=code,
            sha256=hashlib.sha256(code.encode("utf-8")).hexdigest(),
            structural_signature=signature,
            extension=".py",
            artifact_kind="kernelbenchx_python",
        )


class CompilerGymSolutionCodec:
    output_mode = "plain_text"

    def __init__(self, *, benchmark_uri: str) -> None:
        self.benchmark_uri = benchmark_uri
        self.capability_card = compilergym_capability(benchmark_uri)

    def parse(self, raw_response: str) -> SolutionArtifact:
        if not isinstance(raw_response, str) or not raw_response.strip():
            raise SolutionContractError("CompilerGym response cannot be empty")
        stripped = raw_response.strip()
        fenced = _JSON_FENCE.fullmatch(stripped)
        if fenced:
            stripped = fenced.group(1).strip()
        elif not (stripped.startswith("{") and stripped.endswith("}")):
            raise SolutionContractError(
                "CompilerGym JSON must occupy the whole response"
            )
        try:
            candidate = ActionSequenceCandidate.from_bytes(
                stripped.encode("utf-8"),
                expected_benchmark_uri=self.benchmark_uri,
            )
        except CandidatePolicyError as exc:
            raise SolutionContractError(str(exc)) from exc
        text = json.dumps(
            candidate.to_dict(), ensure_ascii=True, sort_keys=True, separators=(",", ":")
        ) + "\n"
        return SolutionArtifact(
            raw_response=raw_response,
            text=text,
            sha256=hashlib.sha256(text.encode("utf-8")).hexdigest(),
            structural_signature=_structure_sha(
                {
                    "actions": list(candidate.actions),
                    "unique_actions": sorted(set(candidate.actions)),
                    "action_count": len(candidate.actions),
                }
            ),
            extension=".json",
            artifact_kind="compilergym_action_sequence",
        )


class LCBenchSolutionCodec:
    """Freeze one task-bound, bounded LCBench query batch as canonical JSON."""

    output_mode = "plain_text"

    def __init__(self, *, instance_id: str) -> None:
        if not instance_id.isdigit():
            raise ValueError("LCBench instance_id must be numeric")
        self.instance_id = instance_id
        self.capability_card = lcbench_capability(instance_id)

    def parse(self, raw_response: str) -> SolutionArtifact:
        if not isinstance(raw_response, str) or not raw_response.strip():
            raise SolutionContractError("LCBench response cannot be empty")
        stripped = raw_response.strip()
        fenced = _JSON_FENCE.fullmatch(stripped)
        if fenced:
            stripped = fenced.group(1).strip()
        elif not (stripped.startswith("{") and stripped.endswith("}")):
            raise SolutionContractError("LCBench JSON must occupy the whole response")
        try:
            candidate = LCBenchQueryBatch.from_bytes(
                stripped.encode("utf-8"), expected_instance_id=self.instance_id
            )
        except LCBenchCandidatePolicyError as exc:
            raise SolutionContractError(str(exc)) from exc
        payload = candidate.to_dict()
        text = json.dumps(
            payload,
            ensure_ascii=True,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ) + "\n"
        return SolutionArtifact(
            raw_response=raw_response,
            text=text,
            sha256=hashlib.sha256(text.encode("utf-8")).hexdigest(),
            structural_signature=_structure_sha(
                {
                    "query_count": len(candidate.queries),
                    "query_keys": sorted(candidate.queries[0]),
                    "unique_batch_sizes": sorted(
                        {int(query["batch_size"]) for query in candidate.queries}
                    ),
                    "unique_layer_counts": sorted(
                        {int(query["num_layers"]) for query in candidate.queries}
                    ),
                }
            ),
            extension=".json",
            artifact_kind="yahpo_lcbench_query_batch",
        )


class SWEPerfSolutionCodec:
    output_mode = "plain_text"

    def parse(self, raw_response: str) -> SolutionArtifact:
        if not isinstance(raw_response, str) or not raw_response.strip():
            raise SolutionContractError("SWE-Perf response cannot be empty")
        stripped = raw_response.strip()
        fenced = _DIFF_FENCE.fullmatch(stripped)
        if fenced:
            patch = fenced.group(1)
        elif stripped.startswith("diff --git "):
            patch = stripped
        else:
            raise SolutionContractError(
                "SWE-Perf unified diff must occupy the whole response"
            )
        patch = patch.rstrip("\n") + "\n"
        try:
            summary = validate_unified_diff(patch)
        except PatchContractError as exc:
            raise SolutionContractError(str(exc)) from exc
        signature = _structure_sha(
            {
                "file_paths": list(summary.file_paths),
                "hunk_count": summary.hunk_count,
                "added_lines": summary.added_lines,
                "deleted_lines": summary.deleted_lines,
            }
        )
        return SolutionArtifact(
            raw_response=raw_response,
            text=patch,
            sha256=summary.sha256,
            structural_signature=signature,
            extension=".patch",
            artifact_kind="sweperf_unified_diff",
        )


class SWEBenchVerifiedSolutionCodec:
    """Accept one bounded canonical Git diff for a SWE-bench Verified task."""

    output_mode = "plain_text"
    capability_card = SWEBENCH_VERIFIED_CAPABILITY

    def parse(self, raw_response: str) -> SolutionArtifact:
        try:
            normalized = normalize_swebench_verified_response(raw_response)
        except ContractCompatibilityError as exc:
            raise SolutionContractError(
                str(exc), reason_code=exc.reason_code
            ) from exc
        artifact = SWEPerfSolutionCodec().parse(normalized.text)
        return SolutionArtifact(
            raw_response=raw_response,
            text=artifact.text,
            sha256=artifact.sha256,
            structural_signature=artifact.structural_signature,
            extension=artifact.extension,
            artifact_kind="swebench_verified_unified_diff",
            compatibility_trace=normalized.trace,
        )


def _write_once(path: Path, content: bytes) -> None:
    if path.exists():
        if path.read_bytes() != content:
            raise ValueError("refusing to overwrite different content")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, suffix=".solution.tmp")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(name).replace(path)
    except Exception:
        Path(name).unlink(missing_ok=True)
        raise


class SolutionArchive:
    def __init__(self, root: Path, *, cell_id: str) -> None:
        if not isinstance(cell_id, str) or not _SAFE_CELL.fullmatch(cell_id) or ".." in cell_id:
            raise ValueError("unsafe solution cell id")
        self.root = root.resolve()
        self.cell_id = cell_id
        digest = hashlib.sha256(cell_id.encode("utf-8")).hexdigest()
        self.cell_root = self.root / f"cell-{digest}"

    def store(self, candidate_id: str, artifact: SolutionArtifact) -> StoredSolution:
        if not _SAFE_COMPONENT.fullmatch(candidate_id):
            raise ValueError("unsafe solution candidate id")
        artifact_path = self.cell_root / "artifacts" / f"{candidate_id}{artifact.extension}"
        raw_path = self.cell_root / "raw_responses" / f"{candidate_id}.txt"
        metadata_path = self.cell_root / "metadata" / f"{candidate_id}.json"
        stored = StoredSolution(
            cell_id=self.cell_id,
            candidate_id=candidate_id,
            artifact_sha256=artifact.sha256,
            artifact_path=artifact_path,
            raw_response_path=raw_path,
            metadata_path=metadata_path,
        )
        metadata = {
            "schema_version": 2,
            "cell_id": self.cell_id,
            "candidate_id": candidate_id,
            "artifact_kind": artifact.artifact_kind,
            "artifact_sha256": artifact.sha256,
            "structural_signature": artifact.structural_signature,
            "extension": artifact.extension,
            "raw_response_sha256": hashlib.sha256(
                artifact.raw_response.encode("utf-8")
            ).hexdigest(),
            "compatibility_trace": artifact.compatibility_trace,
        }
        encoded_metadata = (
            json.dumps(metadata, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        ).encode("utf-8")
        if metadata_path.exists():
            if metadata_path.read_bytes() != encoded_metadata:
                raise ValueError("candidate id is already bound to different content")
            if (
                not artifact_path.is_file()
                or hashlib.sha256(artifact_path.read_bytes()).hexdigest()
                != artifact.sha256
                or not raw_path.is_file()
            ):
                raise ValueError("stored solution archive is incomplete")
            return stored
        _write_once(artifact_path, artifact.text.encode("utf-8"))
        _write_once(raw_path, artifact.raw_response.encode("utf-8"))
        _write_once(metadata_path, encoded_metadata)
        return stored
