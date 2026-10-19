"""Fail-closed production composition for HB-GEN-1 formal suite providers.

This module has no runtime side effects.  It reads and verifies frozen
source/canary artifacts, may seal one content-addressed local compatibility
receipt, and constructs provider objects only after their suite gate closes.
It never invokes a model, evaluator, Docker, SSH, network, or a GPU.

The three-suite :class:`StagingBoundFormalProviderFactory` has no public
constructor.  ``compose_formal_provider_factory()`` is its only authority and
requires the staging contract *and* every suite gate to be ready.  In the
current revision SWE-Perf cannot satisfy that condition because its candidate
outcome is still produced in-process by untrusted patch code.
"""

from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import stat
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from .adapters.compilergym import (
    ADVERSARIAL_CANARY_IDS as COMPILERGYM_ADVERSARIAL_IDS,
    CBENCH_BENCHMARK_URIS,
    COMPILER_GYM_RELEASE_COMMIT,
    CompilerGymCbenchAdapter,
    frozen_contract as compilergym_frozen_contract,
)
from .adapters.kernelbenchx import (
    ADVERSARIAL_CANARY_IDS as KERNELBENCHX_ADVERSARIAL_IDS,
    KERNELBENCHX_REPOSITORY_COMMIT,
    KernelBenchXAdapter,
    KernelBenchXTask,
)
from .evaluation import CompilerGymEvaluationBackend, KernelBenchXEvaluationBackend
from .events import JournalIntegrityError, verify_operation_journal
from .formal import (
    FormalCampaignContract,
    FormalProviderFactory,
    FormalSuiteProvider,
    FormalTaskBinding,
)
from .schema import BenchmarkPool, CandidateInstance, PilotManifest
from .solutions import CompilerGymSolutionCodec, KernelBenchXSolutionCodec
from .stream import StreamItem, build_stream
from .sweperf_wrapper.trusted_result import result_channel_capability_verdict


_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_COMMIT = re.compile(r"[0-9a-f]{40}\Z")
_PRIVATE_TEXT = re.compile(
    r"(?:/home/|/data\d*/|private[_ -]evaluator|private[_ -]log)",
    re.IGNORECASE,
)
_MAX_JSON_BYTES = 16 * 1024 * 1024
_CANARY_SUMMARY_KEYS = {
    "schema_version",
    "status",
    "suite",
    "code_revision",
    "cases",
    "committed_usage",
    "operation_event_count",
    "operation_journal_head_sha256",
}
_CASE_KEYS = {"name", "result_sha256", "status"}
_RESOURCE_KEYS = {
    "model_calls",
    "evaluator_transactions",
    "gpu_exclusive_seconds",
    "cpu_evaluator_seconds",
}
_KERNELBENCHX_PUBLIC_RESULT_KEYS = {
    "attempt_id",
    "canary_id",
    "candidate_runtime_ms",
    "candidate_sha256",
    "case",
    "compiled",
    "correct",
    "elapsed_seconds",
    "gpu_seconds",
    "hardware",
    "passed",
    "private_result_sha256",
    "reference_runtime_ms",
    "status",
    "task_id",
}
_COMPILERGYM_CANARY_REVISION = "edd202bb6bf4baadba70dfe745a9169f0a1dc597"
_COMPILERGYM_ADAPTER_PATH = (
    "optimization_lab/harness_builder/adapters/compilergym.py"
)
_EVALUATION_PATH = "optimization_lab/harness_builder/evaluation.py"
_SOLUTIONS_PATH = "optimization_lab/harness_builder/solutions.py"
_EVENTS_PATH = "optimization_lab/harness_builder/events.py"
_EVALUATION_AST_NAMES = {
    "_PRIVATE_PATH",
    "_canonical_sha",
    "_public_text",
    "NormalizedEvaluation",
    "CompilerGymEvaluationBackend",
}
_SOLUTION_AST_NAMES = {
    "_JSON_FENCE",
    "SolutionContractError",
    "SolutionArtifact",
    "_structure_sha",
    "CompilerGymSolutionCodec",
}
_RESOURCE_AST_NAMES = {"ResourceVector"}
_COMPILERGYM_OLD_SOURCE_SHA256S = {
    _COMPILERGYM_ADAPTER_PATH: (
        "d2af38f3bc2b8ced4189ccb30a0a88cb08ad5fd7030c26ae2fe5007a16d40776"
    ),
    _EVALUATION_PATH: (
        "616b2fc2203c67cb1e455c60c7fc3af46f4b5f5b39910eba5742c15beb5fa3d6"
    ),
    _SOLUTIONS_PATH: (
        "94dc5618e620f6ac2d644f9aa4f2c25b922bebdec83dbeac33275914cda5aab8"
    ),
    _EVENTS_PATH: (
        "57ff5532469e623d85a836bfcee051caca49516b31beee1099dc5a0141cc9648"
    ),
}


class FormalProviderCompositionBlocked(RuntimeError):
    """The formal production provider factory cannot be minted."""


def _canonical_bytes(payload: Mapping[str, Any]) -> bytes:
    return json.dumps(
        payload,
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _strict_object(raw: bytes, *, label: str) -> dict[str, Any]:
    if not raw or len(raw) > _MAX_JSON_BYTES:
        raise ValueError(f"{label} size is outside the bound")

    def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"{label} contains a duplicate key")
            result[key] = value
        return result

    try:
        payload = json.loads(raw.decode("utf-8"), object_pairs_hook=unique)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{label} is not strict UTF-8 JSON") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"{label} must be one object")
    return payload


def _read_regular(path: Path, *, label: str, max_bytes: int = _MAX_JSON_BYTES) -> bytes:
    path = Path(path)
    try:
        metadata = path.lstat()
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            raise ValueError(f"{label} must be a regular non-symlink file")
        descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
        with os.fdopen(descriptor, "rb") as stream:
            opened = os.fstat(stream.fileno())
            if not stat.S_ISREG(opened.st_mode):
                raise ValueError(f"{label} must be a regular non-symlink file")
            raw = stream.read(max_bytes + 1)
    except ValueError:
        raise
    except OSError as exc:
        raise ValueError(f"{label} is unavailable") from exc
    if len(raw) > max_bytes:
        raise ValueError(f"{label} is too large")
    return raw


def _public_text(value: str, *, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} cannot be empty")
    if _PRIVATE_TEXT.search(value):
        raise ValueError(f"{label} contains a private path")
    return value


def _write_content_addressed(path: Path, raw: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    if path.parent.is_symlink() or not path.parent.is_dir():
        raise ValueError("component rebind root is unsafe")
    if path.exists() or path.is_symlink():
        if path.is_symlink() or path.read_bytes() != raw:
            raise ValueError("component rebind evidence is already rebound")
        return
    descriptor, name = tempfile.mkstemp(
        prefix=".formal-rebind-", suffix=".tmp", dir=path.parent
    )
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temporary, 0o444)
        os.replace(temporary, path)
        directory = os.open(path.parent, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise


def _git_blob(project_root: Path, revision: str, relative: str) -> bytes:
    expected = _COMPILERGYM_OLD_SOURCE_SHA256S.get(relative)
    if revision != _COMPILERGYM_CANARY_REVISION or expected is None:
        raise ValueError("CompilerGym rebind source revision is not frozen")
    observed = subprocess.run(
        ["git", "-C", str(project_root), "show", f"{revision}:{relative}"],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        timeout=30,
        check=False,
    )
    if observed.returncode != 0 or _sha256(observed.stdout) != expected:
        raise ValueError("CompilerGym frozen source blob is unavailable or changed")
    return observed.stdout


def _ast_node_name(node: ast.AST) -> str | None:
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return node.name
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(
        node.targets[0], ast.Name
    ):
        return node.targets[0].id
    if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
        return node.target.id
    return None


def _canonical_ast_segment(
    raw: bytes,
    names: set[str],
    *,
    label: str,
    compatibility_normalizer: ast.NodeTransformer | None = None,
) -> str:
    try:
        tree = ast.parse(raw.decode("utf-8"))
    except (UnicodeDecodeError, SyntaxError) as exc:
        raise ValueError(f"{label} is not parseable Python") from exc
    selected = [node for node in tree.body if _ast_node_name(node) in names]
    if {_ast_node_name(node) for node in selected} != names:
        raise ValueError(f"{label} canonical AST segment is incomplete")
    if compatibility_normalizer is not None:
        selected = [compatibility_normalizer.visit(node) for node in selected]
        ast.fix_missing_locations(tree)
    return _sha256(
        _canonical_bytes(
            {
                "label": label,
                "names": sorted(names),
                "ast": [ast.dump(node, include_attributes=False) for node in selected],
            }
        )
    )


class _JournalCompatibilityNormalizer(ast.NodeTransformer):
    """Normalize reviewed changes that cannot alter the frozen ledger replay.

    Besides the cell-id broadening, the current governor has a fail-closed
    callback immediately before *future* reservations.  The historical
    CompilerGym receipt only replays an already terminal 36-event ledger, so
    that callback is outside the receipt's semantics.  Its import, parameter,
    validation, assignment, and lock-scoped invocation are nevertheless
    removed only when every node has the exact reviewed shape and location.
    """

    def __init__(self) -> None:
        self._callable_imports = 0
        self._guard_parameters = 0
        self._guard_initializers = 0
        self._guard_invocations = 0

    @staticmethod
    def _same_ast(left: ast.AST, right: ast.AST) -> bool:
        return ast.dump(left, include_attributes=False) == ast.dump(
            right, include_attributes=False
        )

    def visit_ImportFrom(self, node: ast.ImportFrom) -> ast.AST:  # noqa: N802
        if node.module == "typing":
            kept: list[ast.alias] = []
            for name in node.names:
                if name.name == "Callable":
                    if name.asname is not None:
                        raise ValueError("unexpected Callable import alias")
                    self._callable_imports += 1
                    continue
                kept.append(name)
            node.names = kept
        return self.generic_visit(node)

    def _normalize_resource_governor(self, node: ast.ClassDef) -> None:
        initializers = [
            child
            for child in node.body
            if isinstance(child, ast.FunctionDef) and child.name == "__init__"
        ]
        reservations = [
            child
            for child in node.body
            if isinstance(child, ast.FunctionDef) and child.name == "reserve"
        ]
        if len(initializers) != 1 or len(reservations) != 1:
            raise ValueError("ResourceGovernor methods differ from reviewed shape")

        initializer = initializers[0]
        parameter_indexes = [
            index
            for index, argument in enumerate(initializer.args.kwonlyargs)
            if argument.arg == "pre_reserve_guard"
        ]
        if parameter_indexes != [len(initializer.args.kwonlyargs) - 1]:
            raise ValueError("pre-reserve guard parameter differs from reviewed shape")
        parameter_index = parameter_indexes[0]
        expected_parameter = ast.parse(
            "def placeholder(*, pre_reserve_guard: Callable[[], None] | None = None):\n"
            "    pass\n"
        ).body[0]
        assert isinstance(expected_parameter, ast.FunctionDef)
        if (
            not self._same_ast(
                initializer.args.kwonlyargs[parameter_index],
                expected_parameter.args.kwonlyargs[0],
            )
            or not self._same_ast(
                initializer.args.kw_defaults[parameter_index],
                expected_parameter.args.kw_defaults[0],
            )
        ):
            raise ValueError("pre-reserve guard annotation differs from reviewed shape")
        del initializer.args.kwonlyargs[parameter_index]
        del initializer.args.kw_defaults[parameter_index]
        self._guard_parameters += 1

        expected_initializer = ast.parse(
            "if pre_reserve_guard is not None and not callable(pre_reserve_guard):\n"
            "    raise ValueError('pre-reserve guard must be callable')\n"
            "self.pre_reserve_guard = pre_reserve_guard\n"
        ).body
        initializer_matches = [
            index
            for index in range(len(initializer.body) - 1)
            if self._same_ast(initializer.body[index], expected_initializer[0])
            and self._same_ast(initializer.body[index + 1], expected_initializer[1])
        ]
        if initializer_matches != [2]:
            raise ValueError("pre-reserve guard initializer differs from reviewed shape")
        initializer_index = initializer_matches[0]
        del initializer.body[initializer_index : initializer_index + 2]
        self._guard_initializers += 1

        reservation = reservations[0]
        with_nodes = [child for child in reservation.body if isinstance(child, ast.With)]
        if len(with_nodes) != 1:
            raise ValueError("ResourceGovernor reservation lock differs")
        try_nodes = [child for child in with_nodes[0].body if isinstance(child, ast.Try)]
        if len(try_nodes) != 1 or not try_nodes[0].body:
            raise ValueError("ResourceGovernor reservation transaction differs")
        expected_invocation = ast.parse(
            "if self.pre_reserve_guard is not None:\n"
            "    self.pre_reserve_guard()\n"
        ).body[0]
        if not self._same_ast(try_nodes[0].body[0], expected_invocation):
            raise ValueError("pre-reserve guard invocation differs from reviewed shape")
        del try_nodes[0].body[0]
        self._guard_invocations += 1

    def visit_Module(self, node: ast.Module) -> ast.Module:  # noqa: N802
        kept = [
            child
            for child in node.body
            if _ast_node_name(child)
            not in {"_SAFE_CELL_IDENTIFIER", "_safe_cell_identifier"}
        ]
        node.body = kept
        normalized = self.generic_visit(node)
        if (
            self._callable_imports,
            self._guard_parameters,
            self._guard_initializers,
            self._guard_invocations,
        ) != (1, 1, 1, 1):
            raise ValueError("current pre-reserve guard is absent or duplicated")
        return normalized

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.AST:  # noqa: N802
        if node.name == "ResourceGovernor":
            self._normalize_resource_governor(node)
        return self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> ast.AST:  # noqa: N802
        node = self.generic_visit(node)
        if isinstance(node.func, ast.Name) and node.func.id == "_safe_cell_identifier":
            if len(node.args) != 1 or node.keywords:
                raise ValueError("unexpected current cell-id validator call")
            return ast.copy_location(
                ast.Call(
                    func=ast.Name(id="_safe_identifier", ctx=ast.Load()),
                    args=[node.args[0], ast.Constant(value="cell id")],
                    keywords=[],
                ),
                node,
            )
        return node


class _CompilerGymCodecCompatibilityNormalizer(ast.NodeTransformer):
    """Remove only reviewed diagnostic/prompt-surface metadata additions.

    These additions expose typed rejection reasons, carry an optional SWE
    compatibility trace, and bind a capability card for Harness prompting.
    None changes CompilerGym candidate parsing, normalization, or evaluator
    semantics.  Structurally different additions fail closed.
    """

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.AST:  # noqa: N802
        if node.name == "SolutionContractError":
            expected = ast.parse(
                """
def __init__(self, message: str, *, reason_code: str | None = None) -> None:
    super().__init__(message)
    self.reason_code = reason_code or patch_contract_reason_code(message)
"""
            ).body[0]
            kept: list[ast.stmt] = []
            removed = 0
            for child in node.body:
                if isinstance(child, ast.FunctionDef) and child.name == "__init__":
                    if ast.dump(child, include_attributes=False) != ast.dump(
                        expected, include_attributes=False
                    ):
                        raise ValueError(
                            "unexpected SolutionContractError diagnostic binding"
                        )
                    removed += 1
                    continue
                kept.append(child)
            if removed != 1:
                raise ValueError(
                    "SolutionContractError diagnostic binding is absent or duplicated"
                )
            node.body = kept
            return self.generic_visit(node)
        if node.name == "SolutionArtifact":
            expected = ast.parse(
                """
class Placeholder:
    compatibility_trace: dict[str, Any] | None = None
"""
            ).body[0].body[0]
            kept = []
            removed = 0
            for child in node.body:
                if (
                    isinstance(child, ast.AnnAssign)
                    and isinstance(child.target, ast.Name)
                    and child.target.id == "compatibility_trace"
                ):
                    if ast.dump(child, include_attributes=False) != ast.dump(
                        expected, include_attributes=False
                    ):
                        raise ValueError(
                            "unexpected SolutionArtifact compatibility trace"
                        )
                    removed += 1
                    continue
                kept.append(child)
            if removed != 1:
                raise ValueError(
                    "SolutionArtifact compatibility trace is absent or duplicated"
                )
            node.body = kept
            return self.generic_visit(node)
        if node.name != "CompilerGymSolutionCodec":
            return self.generic_visit(node)
        removed = 0
        for child in node.body:
            if not isinstance(child, ast.FunctionDef) or child.name != "__init__":
                continue
            kept: list[ast.stmt] = []
            for statement in child.body:
                if (
                    isinstance(statement, ast.Assign)
                    and len(statement.targets) == 1
                    and isinstance(statement.targets[0], ast.Attribute)
                    and isinstance(statement.targets[0].value, ast.Name)
                    and statement.targets[0].value.id == "self"
                    and statement.targets[0].attr == "capability_card"
                ):
                    value = statement.value
                    if not (
                        isinstance(value, ast.Call)
                        and isinstance(value.func, ast.Name)
                        and value.func.id == "compilergym_capability"
                        and len(value.args) == 1
                        and isinstance(value.args[0], ast.Name)
                        and value.args[0].id == "benchmark_uri"
                        and not value.keywords
                    ):
                        raise ValueError(
                            "unexpected CompilerGym capability-card binding"
                        )
                    removed += 1
                    continue
                kept.append(statement)
            child.body = kept
        if removed != 1:
            raise ValueError("CompilerGym capability-card binding is absent or duplicated")
        return self.generic_visit(node)


def _normalized_events_ast(raw: bytes, *, current: bool) -> tuple[str, str]:
    try:
        tree = ast.parse(raw.decode("utf-8"))
    except (UnicodeDecodeError, SyntaxError) as exc:
        raise ValueError("events verifier source is not parseable Python") from exc
    original_sha = _sha256(ast.dump(tree, include_attributes=False).encode("utf-8"))
    if current:
        tree = _JournalCompatibilityNormalizer().visit(tree)
        ast.fix_missing_locations(tree)
    normalized_sha = _sha256(
        ast.dump(tree, include_attributes=False).encode("utf-8")
    )
    return original_sha, normalized_sha


def _journal_projection(replay: Any) -> dict[str, Any]:
    operations: dict[str, Any] = {}
    for operation_id, operation in sorted(replay.operations.items()):
        terminal = operation.event_for("operation_completed")
        operations[operation_id] = {
            "cell_id": operation.cell_id,
            "operation_kind": operation.operation_kind,
            "state": operation.state,
            "reservation": operation.reservation.to_dict(),
            "committed_usage": operation.committed_usage.to_dict(),
            "artifact_sha256": terminal.payload["artifact_sha256"],
            "event_sha256s": [event.event_sha256 for event in operation.events],
        }
    return {
        "event_count": replay.event_count,
        "head_sha256": replay.head_sha256,
        "operations": operations,
    }


def _prepare_compilergym_rebind(
    *,
    project_root: Path,
    rebind_root: Path,
    canary_root: Path,
    old_summary_sha256: str,
    old_code_revision: str,
    current_code_revision: str,
    staging_plan_sha256: str,
    manifest_sha256: str,
) -> str:
    """Bind the exact old canary segment to unchanged current components.

    This is deliberately not a claim that ``events.py`` is globally equivalent.
    It proves only that (a) the complete CompilerGym adapter is byte-identical,
    (b) the normalizer and codec dependency ASTs are identical, and (c) the
    journal-verifier cell-id broadening plus the exact current-only reservation
    guard normalize to the old AST.  The guard cannot affect replay of the
    already terminal segment and remains active for every future reservation.
    Every cell ID in the exact frozen 36-event ledger must also belong to the
    old/new accepted intersection.  The current independent verifier remains
    the authority for event hashes, resources, states, terminal artifact hashes,
    and the external head anchor.
    """

    if old_code_revision != _COMPILERGYM_CANARY_REVISION:
        raise ValueError("CompilerGym old canary revision is not frozen")
    if not _COMMIT.fullmatch(current_code_revision):
        raise ValueError("CompilerGym current code revision is invalid")
    project_root = Path(project_root)
    if _inspect_clean_code_revision(project_root) != current_code_revision:
        raise ValueError("CompilerGym current clean revision differs before rebind")
    old_sources = {
        relative: _git_blob(project_root, old_code_revision, relative)
        for relative in _COMPILERGYM_OLD_SOURCE_SHA256S
    }
    current_sources = {
        relative: _read_regular(
            project_root / relative,
            label=f"current {Path(relative).name}",
            max_bytes=4 * 1024 * 1024,
        )
        for relative in _COMPILERGYM_OLD_SOURCE_SHA256S
    }
    if old_sources[_COMPILERGYM_ADAPTER_PATH] != current_sources[_COMPILERGYM_ADAPTER_PATH]:
        raise ValueError("CompilerGym adapter bytes changed since canary")

    ast_segments: dict[str, dict[str, str]] = {}
    for label, relative, names in (
        ("evaluation_backend", _EVALUATION_PATH, _EVALUATION_AST_NAMES),
        ("solution_codec", _SOLUTIONS_PATH, _SOLUTION_AST_NAMES),
        ("resource_vector", _EVENTS_PATH, _RESOURCE_AST_NAMES),
    ):
        old_ast = _canonical_ast_segment(
            old_sources[relative], names, label=label
        )
        current_ast = _canonical_ast_segment(
            current_sources[relative],
            names,
            label=label,
            compatibility_normalizer=(
                _CompilerGymCodecCompatibilityNormalizer()
                if label == "solution_codec"
                else None
            ),
        )
        if old_ast != current_ast:
            raise ValueError(f"CompilerGym {label} AST changed since canary")
        ast_segments[label] = {"old": old_ast, "current": current_ast}

    old_events_ast, old_normalized = _normalized_events_ast(
        old_sources[_EVENTS_PATH], current=False
    )
    current_events_ast, current_normalized = _normalized_events_ast(
        current_sources[_EVENTS_PATH], current=True
    )
    if old_normalized != current_normalized:
        raise ValueError("journal verifier changed beyond reviewed cell-id broadening")

    replay = verify_operation_journal(
        Path(canary_root) / "journal" / "operation_ledger.jsonl",
        anchor_path=Path(canary_root) / "trusted-head.json",
    )
    projection = _journal_projection(replay)
    if replay.event_count != 36 or len(replay.operations) != 12:
        raise ValueError("CompilerGym canary journal cardinality differs")
    old_cell = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:/+-]{0,255}\Z")
    cell_ids = sorted({event.cell_id for event in replay.events})
    if not cell_ids or any(
        old_cell.fullmatch(cell_id) is None
        or ".." in cell_id
        or "//" in cell_id
        or cell_id.endswith("/")
        for cell_id in cell_ids
    ):
        raise ValueError("CompilerGym canary uses a cell id outside verifier intersection")

    core: dict[str, Any] = {
        "schema_version": 1,
        "artifact_kind": "hb-gen1-compilergym-component-segment-rebind",
        "status": "passed",
        "scope": "exact_compilergym_canary_36_event_segment_only",
        "old_code_revision": old_code_revision,
        "current_code_revision": current_code_revision,
        "staging_plan_sha256": staging_plan_sha256,
        "manifest_sha256": manifest_sha256,
        "old_canary_summary_sha256": old_summary_sha256,
        "component_proofs": {
            "adapter_byte_sha256": _sha256(
                current_sources[_COMPILERGYM_ADAPTER_PATH]
            ),
            "canonical_ast_segments": ast_segments,
        },
        "journal_compatibility": {
            "old_source_sha256": _COMPILERGYM_OLD_SOURCE_SHA256S[_EVENTS_PATH],
            "old_full_ast_sha256": old_events_ast,
            "current_full_ast_sha256": current_events_ast,
            "reviewed_normalized_ast_sha256": old_normalized,
            "current_only_pre_reserve_guard": {
                "resource_governor_ast_sha256": _canonical_ast_segment(
                    current_sources[_EVENTS_PATH],
                    {"ResourceGovernor"},
                    label="current_resource_governor",
                ),
                "affects_frozen_replay": False,
                "remains_active_for_future_reservations": True,
            },
            "accepted_cell_ids": cell_ids,
            "replay_projection_sha256": _sha256(_canonical_bytes(projection)),
            "event_count": replay.event_count,
            "head_sha256": replay.head_sha256,
        },
        "external_actions": {
            "model_invoked": False,
            "evaluator_invoked": False,
            "gpu_used": False,
            "docker_invoked": False,
            "ssh_invoked": False,
            "network_used": False,
        },
    }
    content_id = _sha256(_canonical_bytes(core))
    payload = {**core, "content_id": content_id}
    raw = _canonical_bytes(payload) + b"\n"
    evidence_path = (
        Path(rebind_root) / "compilergym-cbench" / f"{content_id}.json"
    )
    _write_content_addressed(evidence_path, raw)
    if _inspect_clean_code_revision(project_root) != current_code_revision:
        raise ValueError("CompilerGym current clean revision changed during rebind")
    # The suite receipt binds both the old summary and the reviewed rebind,
    # rather than pretending the old summary was authored by the current code.
    return _sha256(
        _canonical_bytes(
            {
                "old_canary_summary_sha256": old_summary_sha256,
                "component_rebind_content_id": content_id,
            }
        )
    )


def _result_artifact(root: Path, suite: str, name: str) -> Path:
    if suite == "compilergym-cbench":
        return root / "private" / f"{name}.supervisor.json"
    if suite == "kernelbenchx":
        return root / "results" / f"{name}.json"
    raise ValueError("unknown formal canary suite")


@dataclass(frozen=True)
class FormalProviderCompositionConfig:
    """Offline inputs used to verify and compose formal suite providers.

    Paths are operator-only data.  They are deliberately never serialized into
    :class:`FormalProviderPreflight` so a preflight report cannot disclose host
    layout or a private evaluator path.
    """

    project_root: Path
    staging_plan_path: Path
    manifest_path: Path
    kernelbenchx_repository: Path
    kernelbenchx_supervisor: Path
    kernelbenchx_scratch_root: Path
    kernelbenchx_gpu: str
    kernelbenchx_canary_root: Path
    compilergym_canary_root: Path
    sweperf_source_lock_receipt: Path
    component_rebind_root: Path
    sweperf_canary_root: Path | None = None
    require_full_stream: bool = True


@dataclass(frozen=True)
class SuiteProviderPreflight:
    suite: str
    ready: bool
    blocker_codes: tuple[str, ...]
    gate_receipt_sha256: str | None
    task_binding_core_sha256s: Mapping[str, str] = field(
        default_factory=lambda: MappingProxyType({}), repr=False
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            "suite": self.suite,
            "ready": self.ready,
            "blocker_codes": list(self.blocker_codes),
            "gate_receipt_sha256": self.gate_receipt_sha256,
            "task_binding_core_sha256s": dict(
                sorted(self.task_binding_core_sha256s.items())
            ),
        }


@dataclass(frozen=True)
class FormalProviderPreflight:
    staging_plan_sha256: str | None
    manifest_sha256: str | None
    staging_execution_ready: bool
    provider_factory_ready: bool
    blocker_codes: tuple[str, ...]
    suites: tuple[SuiteProviderPreflight, ...]
    model_calls_started: int = 0
    evaluator_transactions_started: int = 0

    def to_dict(self) -> dict[str, Any]:
        payload = {
            "schema_version": 1,
            "phase": "hb-gen1-formal-provider-composition",
            "staging_plan_sha256": self.staging_plan_sha256,
            "manifest_sha256": self.manifest_sha256,
            "staging_execution_ready": self.staging_execution_ready,
            "provider_factory_ready": self.provider_factory_ready,
            "blocker_codes": list(self.blocker_codes),
            "suites": [suite.to_dict() for suite in self.suites],
            "model_calls_started": self.model_calls_started,
            "evaluator_transactions_started": self.evaluator_transactions_started,
            "external_actions": {
                "model_invoked": False,
                "evaluator_invoked": False,
                "gpu_used": False,
                "docker_invoked": False,
                "ssh_invoked": False,
                "network_used": False,
            },
            "no_next_phase": True,
        }
        encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True)
        if _PRIVATE_TEXT.search(encoded):
            raise ValueError("formal provider preflight leaked a private path")
        return payload


@dataclass(frozen=True)
class _CompositionState:
    contract: FormalCampaignContract | None
    manifest: PilotManifest | None
    staging_payload: dict[str, Any] | None
    manifest_sha256: str | None
    preflight: FormalProviderPreflight
    suite_receipt_sha256s: Mapping[str, str]


def _manifest_pool(manifest: PilotManifest, suite: str) -> BenchmarkPool:
    matches = tuple(pool for pool in manifest.benchmarks if pool.suite == suite)
    if len(matches) != 1:
        raise ValueError("formal manifest suite pool differs")
    return matches[0]


def _candidate(pool: BenchmarkPool, task_id: str) -> CandidateInstance:
    matches = tuple(value for value in pool.candidates if value.task_id == task_id)
    if len(matches) != 1 or task_id not in pool.selected_heldout:
        raise ValueError("formal task is not one frozen held-out candidate")
    return matches[0]


def _binding_core_sha(
    *,
    staging_sha256: str,
    manifest_sha256: str,
    suite_receipt_sha256: str,
    pool: BenchmarkPool,
    candidate: CandidateInstance,
    evaluator_contract: Mapping[str, Any],
) -> str:
    return _sha256(
        _canonical_bytes(
            {
                "schema_version": 1,
                "staging_plan_sha256": staging_sha256,
                "manifest_sha256": manifest_sha256,
                "suite_gate_receipt_sha256": suite_receipt_sha256,
                "suite": pool.suite,
                "repository_commit": pool.repository_commit,
                "dataset_commit": pool.dataset_commit,
                "evaluator": pool.evaluator,
                "task_id": candidate.task_id,
                "category": candidate.category,
                "source_path": candidate.source_path,
                "source_sha256": candidate.source_sha256,
                "selection_digest": candidate.selection_digest,
                "evaluator_contract": evaluator_contract,
            }
        )
    )


def _expected_compilergym_cases(pool: BenchmarkPool) -> tuple[tuple[str, str], ...]:
    references = tuple((f"reference-{task_id}", "valid") for task_id in pool.selected_heldout)
    adversarial = tuple(
        (name, status)
        for name, status in zip(
            COMPILERGYM_ADVERSARIAL_IDS,
            ("policy_rejected", "policy_rejected", "no_effect", "policy_rejected"),
            strict=True,
        )
    )
    return references + adversarial


def _kernelbenchx_reference_case(task_id: str) -> str:
    return "reference-" + task_id.removesuffix(".py").replace("/", "-")


def _expected_kernelbenchx_cases(pool: BenchmarkPool) -> tuple[tuple[str, str], ...]:
    references = tuple(
        (_kernelbenchx_reference_case(task_id), "valid")
        for task_id in pool.selected_heldout
    )
    # Adversarial statuses are constrained by their result payload below.  The
    # summary status remains an exact public copy rather than a trusted oracle.
    return references + tuple((name, "candidate_rejected") for name in KERNELBENCHX_ADVERSARIAL_IDS)


def _verify_summary_common(
    *,
    root: Path,
    suite: str,
    expected_case_names: tuple[str, ...],
) -> tuple[dict[str, Any], dict[str, dict[str, Any]], str]:
    summary_raw = _read_regular(root / "summary.json", label=f"{suite} canary summary")
    summary = _strict_object(summary_raw, label=f"{suite} canary summary")
    if set(summary) != _CANARY_SUMMARY_KEYS:
        raise ValueError(f"{suite} canary summary fields differ")
    if (
        summary["schema_version"] != 1
        or summary["status"] != "passed"
        or summary["suite"] != suite
    ):
        raise ValueError(f"{suite} canary summary binding differs")
    if not _COMMIT.fullmatch(str(summary["code_revision"])):
        raise ValueError(f"{suite} canary code revision is invalid")
    usage = summary["committed_usage"]
    if not isinstance(usage, dict) or set(usage) != _RESOURCE_KEYS:
        raise ValueError(f"{suite} canary usage fields differ")
    cases = summary["cases"]
    if not isinstance(cases, list) or any(
        not isinstance(case, dict) or set(case) != _CASE_KEYS for case in cases
    ):
        raise ValueError(f"{suite} canary cases are invalid")
    if tuple(case["name"] for case in cases) != expected_case_names:
        raise ValueError(f"{suite} canary cases differ from the frozen plan")
    result_payloads: dict[str, dict[str, Any]] = {}
    result_hashes: list[str] = []
    for case in cases:
        name = case["name"]
        result_sha = case["result_sha256"]
        if not isinstance(result_sha, str) or not _SHA256.fullmatch(result_sha):
            raise ValueError(f"{suite} canary result hash is invalid")
        result_raw = _read_regular(
            _result_artifact(root, suite, name), label=f"{suite} canary result"
        )
        if _sha256(result_raw) != result_sha:
            raise ValueError(f"{suite} canary result hash differs")
        payload = _strict_object(result_raw, label=f"{suite} canary result")
        if payload.get("status") != case["status"]:
            raise ValueError(f"{suite} canary result status differs")
        result_payloads[name] = payload
        result_hashes.append(result_sha)

    replay = verify_operation_journal(
        root / "journal" / "operation_ledger.jsonl",
        anchor_path=root / "trusted-head.json",
    )
    if (
        summary["operation_event_count"] != replay.event_count
        or summary["operation_journal_head_sha256"] != replay.head_sha256
        or len(replay.operations) != len(cases)
        or any(operation.state != "completed" for operation in replay.operations.values())
    ):
        raise ValueError(f"{suite} canary journal differs from its summary")
    terminal_hashes = sorted(
        operation.event_for("operation_completed").payload["artifact_sha256"]
        for operation in replay.operations.values()
    )
    if terminal_hashes != sorted(result_hashes):
        raise ValueError(f"{suite} canary journal artifact bindings differ")
    return summary, result_payloads, _sha256(summary_raw)


def _verify_compilergym_gate(
    *,
    root: Path,
    pool: BenchmarkPool,
    code_revision: str,
    staging_plan_sha256: str,
    manifest_sha256: str,
    project_root: Path,
    rebind_root: Path,
) -> str:
    expected = _expected_compilergym_cases(pool)
    summary, results, receipt_sha = _verify_summary_common(
        root=root,
        suite=pool.suite,
        expected_case_names=tuple(name for name, _status in expected),
    )
    case_statuses = {case["name"]: case["status"] for case in summary["cases"]}
    if case_statuses != dict(expected):
        raise ValueError("CompilerGym canary status matrix differs")
    for task_id in pool.selected_heldout:
        name = f"reference-{task_id}"
        result = results[name]
        uri = f"benchmark://cbench-v1/{task_id}"
        contract = compilergym_frozen_contract(uri)
        if (
            result.get("status") != "valid"
            or result.get("correct") is not True
            or result.get("replay_verified") is not True
            or result.get("reward_validated") is not True
            or result.get("semantics_validated") is not True
            or result.get("contract") != contract
            or result.get("contract_sha256") != _sha256(_canonical_bytes(contract))
        ):
            raise ValueError("CompilerGym reference canary contract differs")
    for name in COMPILERGYM_ADVERSARIAL_IDS:
        result = results[name]
        expected_correct = name == "no-effect"
        if result.get("correct") is not expected_correct:
            raise ValueError("CompilerGym adversarial canary verdict differs")
    summary_revision = summary["code_revision"]
    if summary_revision == code_revision:
        return receipt_sha
    if summary_revision != _COMPILERGYM_CANARY_REVISION:
        raise ValueError("CompilerGym canary revision is neither current nor rebindable")
    return _prepare_compilergym_rebind(
        project_root=project_root,
        rebind_root=rebind_root,
        canary_root=root,
        old_summary_sha256=receipt_sha,
        old_code_revision=summary_revision,
        current_code_revision=code_revision,
        staging_plan_sha256=staging_plan_sha256,
        manifest_sha256=manifest_sha256,
    )


def _verify_kernelbenchx_gate(
    *, root: Path, pool: BenchmarkPool, code_revision: str
) -> str:
    expected = _expected_kernelbenchx_cases(pool)
    summary, results, receipt_sha = _verify_summary_common(
        root=root,
        suite=pool.suite,
        expected_case_names=tuple(name for name, _status in expected),
    )
    if summary["code_revision"] != code_revision:
        raise ValueError("KernelBenchX canary revision differs from staging")
    for task_id in pool.selected_heldout:
        name = _kernelbenchx_reference_case(task_id)
        result = results[name]
        if (
            set(result) != _KERNELBENCHX_PUBLIC_RESULT_KEYS
            or result.get("case") != name
            or result.get("canary_id") != "reference"
            or result.get("task_id") != task_id
            or result.get("status") != "valid"
            or result.get("compiled") is not True
            or result.get("correct") is not True
            or result.get("passed") is not True
        ):
            raise ValueError("KernelBenchX reference canary binding differs")
        for key in ("candidate_sha256", "private_result_sha256"):
            if not isinstance(result.get(key), str) or not _SHA256.fullmatch(result[key]):
                raise ValueError("KernelBenchX reference canary hash is invalid")
    adversarial_task_ids: set[str] = set()
    for name in KERNELBENCHX_ADVERSARIAL_IDS:
        result = results[name]
        if (
            set(result) != _KERNELBENCHX_PUBLIC_RESULT_KEYS
            or result.get("case") != name
            or result.get("canary_id") != name
            or result.get("task_id") not in pool.selected_heldout
            or result.get("correct") is not False
            or result.get("passed") is not True
            or result.get("status") not in {
                "compile_failed",
                "incorrect",
                "policy_rejected",
            }
        ):
            raise ValueError("KernelBenchX adversarial canary binding differs")
        adversarial_task_ids.add(result["task_id"])
    if len(adversarial_task_ids) != 1:
        raise ValueError("KernelBenchX adversarial canaries must share one frozen task")
    return receipt_sha


def _inspect_kernelbenchx_sources(repository: Path, pool: BenchmarkPool) -> None:
    repository = Path(repository)
    if repository.is_symlink() or not repository.is_dir():
        raise ValueError("KernelBenchX checkout is unavailable")
    observed = subprocess.run(
        ["git", "-C", str(repository), "rev-parse", "HEAD"],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        timeout=30,
        check=False,
    )
    if (
        observed.returncode != 0
        or observed.stdout.strip() != KERNELBENCHX_REPOSITORY_COMMIT
        or pool.repository_commit != KERNELBENCHX_REPOSITORY_COMMIT
    ):
        raise ValueError("KernelBenchX checkout commit differs")
    root = repository.resolve(strict=True)
    for task_id in pool.selected_heldout:
        candidate = _candidate(pool, task_id)
        path = repository / candidate.source_path
        raw = _read_regular(path, label="KernelBenchX task source", max_bytes=1_048_576)
        try:
            resolved = path.resolve(strict=True)
        except OSError as exc:
            raise ValueError("KernelBenchX task source is unavailable") from exc
        if not resolved.is_relative_to(root) or _sha256(raw) != candidate.source_sha256:
            raise ValueError("KernelBenchX task source binding differs")


def _inspect_clean_code_revision(project_root: Path) -> str:
    project_root = Path(project_root)
    if project_root.is_symlink() or not project_root.is_dir():
        raise ValueError("formal project root is unavailable")
    revision = subprocess.run(
        ["git", "-C", str(project_root), "rev-parse", "HEAD"],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        timeout=30,
        check=False,
    )
    status = subprocess.run(
        [
            "git",
            "-C",
            str(project_root),
            "status",
            "--porcelain",
            "--untracked-files=no",
        ],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        timeout=30,
        check=False,
    )
    value = revision.stdout.strip()
    if (
        revision.returncode != 0
        or status.returncode != 0
        or status.stdout.strip()
        or not _COMMIT.fullmatch(value)
    ):
        raise ValueError("formal code revision is not one clean full commit")
    return value


def _sweperf_blockers(path: Path) -> tuple[str, ...]:
    """Interpret only the current blocked prepare artifact.

    A future runnable WrapperSourceLock and a separately trusted canary receipt
    require a new reviewed implementation.  The old worker-authored report is
    never accepted as a compatibility path.
    """

    try:
        raw = _read_regular(path, label="SWE-Perf source-lock receipt")
        payload = _strict_object(raw, label="SWE-Perf source-lock receipt")
    except ValueError:
        return ("sweperf_source_lock_receipt_invalid",)
    if payload.get("content_id") != _sha256(
        _canonical_bytes({key: value for key, value in payload.items() if key != "content_id"})
    ):
        return ("sweperf_source_lock_content_hash_mismatch",)
    if (
        payload.get("artifact_kind") != "hb-gen1-sweperf-source-lock-prepare"
        or payload.get("status") != "blocked"
        or payload.get("runnable_wrapper_source_lock") is not False
    ):
        return ("sweperf_runnable_source_lock_unverified",)
    raw_blockers = payload.get("blockers")
    if not isinstance(raw_blockers, list):
        return ("sweperf_source_lock_receipt_invalid",)
    codes = {
        value.get("code")
        for value in raw_blockers
        if isinstance(value, dict) and isinstance(value.get("code"), str)
    }
    # Only the new capability verdict is recognized as the current trust-boundary
    # diagnosis.  An old worker_authored_report_untrusted artifact remains blocked
    # but is deliberately classified as obsolete rather than silently upgraded.
    command_trust = payload.get("command_trust")
    expected_verdict = result_channel_capability_verdict().to_dict()
    if (
        "in_process_candidate_outcome_unattestable" in codes
        and isinstance(command_trust, dict)
        and command_trust.get("status") == "blocked"
        and command_trust.get("reason_code")
        == "in_process_candidate_outcome_unattestable"
        and command_trust.get("capability_verdict") == expected_verdict
    ):
        return ("sweperf_in_process_candidate_outcome_unattestable",)
    return ("sweperf_source_lock_receipt_obsolete_or_blocked",)


def _common_state(
    config: FormalProviderCompositionConfig,
) -> tuple[
    FormalCampaignContract | None,
    PilotManifest | None,
    dict[str, Any] | None,
    str | None,
    list[str],
]:
    blockers: list[str] = []
    contract: FormalCampaignContract | None = None
    manifest: PilotManifest | None = None
    staging_payload: dict[str, Any] | None = None
    manifest_sha: str | None = None
    try:
        staging_raw = _read_regular(config.staging_plan_path, label="formal staging plan")
        contract = FormalCampaignContract.from_staging_bytes(
            staging_raw, require_full_stream=config.require_full_stream
        )
        staging_payload = _strict_object(staging_raw, label="formal staging plan")
    except (OSError, ValueError):
        blockers.append("staging_plan_invalid")
    else:
        if not contract.execution_ready:
            blockers.extend(
                f"staging:{value}" for value in (contract.blockers or ("not_ready",))
            )
    try:
        manifest_raw = _read_regular(config.manifest_path, label="formal manifest")
        manifest_sha = _sha256(manifest_raw)
        manifest = PilotManifest.from_json(config.manifest_path)
        if _read_regular(config.manifest_path, label="formal manifest") != manifest_raw:
            raise ValueError("formal manifest changed while it was parsed")
    except (OSError, ValueError, json.JSONDecodeError):
        blockers.append("manifest_invalid")
    if contract is not None and manifest is not None and staging_payload is not None:
        source_hashes = staging_payload.get("source_hashes")
        expected_stream = tuple(build_stream(manifest))
        if (
            not isinstance(source_hashes, dict)
            or source_hashes.get("manifest") != manifest_sha
            or staging_payload.get("phase_id") != manifest.phase_id
            or contract.model != manifest.executor_model
            or contract.stream != expected_stream
        ):
            blockers.append("manifest_staging_binding_mismatch")
        code_revision = staging_payload.get("code_revision")
        try:
            observed_revision = _inspect_clean_code_revision(config.project_root)
        except ValueError:
            blockers.append("current_code_revision_unverified")
        else:
            if observed_revision != code_revision:
                blockers.append("current_code_revision_mismatch")
    return contract, manifest, staging_payload, manifest_sha, blockers


def _evaluate_composition(
    config: FormalProviderCompositionConfig,
) -> _CompositionState:
    contract, manifest, staging_payload, manifest_sha, blockers = _common_state(config)
    suite_results: list[SuiteProviderPreflight] = []
    receipt_hashes: dict[str, str] = {}
    if contract is None or manifest is None or staging_payload is None or manifest_sha is None:
        for suite in ("kernelbenchx", "compilergym-cbench", "swe-perf"):
            suite_results.append(
                SuiteProviderPreflight(
                    suite=suite,
                    ready=False,
                    blocker_codes=("common_contract_unavailable",),
                    gate_receipt_sha256=None,
                )
            )
    else:
        code_revision = staging_payload.get("code_revision")
        if not isinstance(code_revision, str) or not _COMMIT.fullmatch(code_revision):
            blockers.append("staging_code_revision_invalid")
            code_revision = ""
        for suite in ("kernelbenchx", "compilergym-cbench"):
            suite_blockers: list[str] = []
            receipt_sha: str | None = None
            binding_hashes: dict[str, str] = {}
            try:
                pool = _manifest_pool(manifest, suite)
                if suite == "kernelbenchx":
                    _inspect_kernelbenchx_sources(config.kernelbenchx_repository, pool)
                    supervisor = Path(config.kernelbenchx_supervisor)
                    metadata = supervisor.lstat()
                    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
                        raise ValueError("KernelBenchX supervisor is unavailable")
                    receipt_sha = _verify_kernelbenchx_gate(
                        root=Path(config.kernelbenchx_canary_root),
                        pool=pool,
                        code_revision=code_revision,
                    )
                    evaluator_contracts = {
                        task_id: {
                            "evaluator": pool.evaluator,
                            "repository_commit": pool.repository_commit,
                            "dataset_commit": pool.dataset_commit,
                            "task_sha256": _candidate(pool, task_id).source_sha256,
                            "supervisor_sha256": _sha256(
                                _read_regular(
                                    supervisor,
                                    label="KernelBenchX supervisor",
                                    max_bytes=2 * 1024 * 1024,
                                )
                            ),
                        }
                        for task_id in pool.selected_heldout
                    }
                else:
                    receipt_sha = _verify_compilergym_gate(
                        root=Path(config.compilergym_canary_root),
                        pool=pool,
                        code_revision=code_revision,
                        staging_plan_sha256=contract.staging_plan_sha256,
                        manifest_sha256=manifest_sha,
                        project_root=config.project_root,
                        rebind_root=config.component_rebind_root,
                    )
                    evaluator_contracts = {
                        task_id: compilergym_frozen_contract(
                            f"benchmark://cbench-v1/{task_id}"
                        )
                        for task_id in pool.selected_heldout
                    }
                for task_id in pool.selected_heldout:
                    binding_hashes[task_id] = _binding_core_sha(
                        staging_sha256=contract.staging_plan_sha256,
                        manifest_sha256=manifest_sha,
                        suite_receipt_sha256=receipt_sha,
                        pool=pool,
                        candidate=_candidate(pool, task_id),
                        evaluator_contract=evaluator_contracts[task_id],
                    )
            except (OSError, ValueError, JournalIntegrityError, subprocess.SubprocessError):
                suite_blockers.append(f"{suite}_gate_invalid_or_incomplete")
            if receipt_sha is not None:
                receipt_hashes[suite] = receipt_sha
            suite_results.append(
                SuiteProviderPreflight(
                    suite=suite,
                    ready=not suite_blockers,
                    blocker_codes=tuple(suite_blockers),
                    gate_receipt_sha256=receipt_sha,
                    task_binding_core_sha256s=MappingProxyType(binding_hashes),
                )
            )
        swe_blockers = _sweperf_blockers(config.sweperf_source_lock_receipt)
        suite_results.append(
            SuiteProviderPreflight(
                suite="swe-perf",
                ready=False,
                blocker_codes=swe_blockers,
                gate_receipt_sha256=None,
            )
        )

    for suite in suite_results:
        blockers.extend(f"suite:{suite.suite}:{code}" for code in suite.blocker_codes)
    blockers = sorted(set(blockers))
    ready = bool(
        contract is not None
        and contract.execution_ready
        and not blockers
        and all(suite.ready for suite in suite_results)
    )
    preflight = FormalProviderPreflight(
        staging_plan_sha256=(
            contract.staging_plan_sha256 if contract is not None else None
        ),
        manifest_sha256=manifest_sha,
        staging_execution_ready=bool(contract is not None and contract.execution_ready),
        provider_factory_ready=ready,
        blocker_codes=tuple(blockers),
        suites=tuple(suite_results),
    )
    return _CompositionState(
        contract=contract,
        manifest=manifest,
        staging_payload=staging_payload,
        manifest_sha256=manifest_sha,
        preflight=preflight,
        suite_receipt_sha256s=MappingProxyType(receipt_hashes),
    )


def preflight_formal_providers(
    config: FormalProviderCompositionConfig,
) -> FormalProviderPreflight:
    """Verify all formal suite composition inputs without invoking a runtime."""

    return _evaluate_composition(config).preflight


def compose_verified_suite_provider(
    config: FormalProviderCompositionConfig,
    suite: str,
) -> FormalSuiteProvider:
    """Construct one individually verified provider without authorizing a campaign.

    This helper exists so each evaluator family can complete its own Gate 1 and
    expose a task binding for offline inspection.  It is *not* a
    :class:`FormalProviderFactory`; :class:`FormalCampaignRunner` still requires
    the all-suite factory minted by :func:`compose_formal_provider_factory`.
    """

    state = _evaluate_composition(config)
    if (
        state.contract is None
        or state.manifest is None
        or state.manifest_sha256 is None
        or any(
            not (code.startswith("suite:") or code.startswith("staging:"))
            for code in state.preflight.blocker_codes
        )
    ):
        raise FormalProviderCompositionBlocked(
            "formal staging/manifest binding is unavailable"
        )
    suite_state = next(
        (value for value in state.preflight.suites if value.suite == suite), None
    )
    if suite_state is None or not suite_state.ready:
        codes = suite_state.blocker_codes if suite_state is not None else ("unknown_suite",)
        raise FormalProviderCompositionBlocked(
            f"formal suite provider {suite!r} is blocked: {', '.join(codes)}"
        )
    receipt_sha = state.suite_receipt_sha256s[suite]
    pool = _manifest_pool(state.manifest, suite)
    if suite == "kernelbenchx":
        adapter = KernelBenchXAdapter(
            repository=config.kernelbenchx_repository,
            supervisor=config.kernelbenchx_supervisor,
            scratch_root=config.kernelbenchx_scratch_root,
            gpu=config.kernelbenchx_gpu,
        )
        return KernelBenchXFormalSuiteProvider(
            staging_plan_sha256=state.contract.staging_plan_sha256,
            manifest_sha256=state.manifest_sha256,
            suite_receipt_sha256=receipt_sha,
            pool=pool,
            repository=config.kernelbenchx_repository,
            adapter=adapter,
        )
    if suite == "compilergym-cbench":
        return CompilerGymFormalSuiteProvider(
            staging_plan_sha256=state.contract.staging_plan_sha256,
            manifest_sha256=state.manifest_sha256,
            suite_receipt_sha256=receipt_sha,
            pool=pool,
        )
    raise FormalProviderCompositionBlocked(
        "SWE-Perf trusted suite provider is not implemented"
    )


class KernelBenchXFormalSuiteProvider:
    suite = "kernelbenchx"

    def __init__(
        self,
        *,
        staging_plan_sha256: str,
        manifest_sha256: str,
        suite_receipt_sha256: str,
        pool: BenchmarkPool,
        repository: Path,
        adapter: KernelBenchXAdapter,
    ) -> None:
        self.staging_plan_sha256 = staging_plan_sha256
        self.manifest_sha256 = manifest_sha256
        self.suite_receipt_sha256 = suite_receipt_sha256
        self.pool = pool
        self.repository = Path(repository)
        self.adapter = adapter

    def bind(self, item: StreamItem) -> FormalTaskBinding:
        if item.suite != self.suite:
            raise ValueError("KernelBenchX provider cannot bind another suite")
        candidate = _candidate(self.pool, item.task_id)
        task = KernelBenchXTask.from_task_id(item.task_id)
        if candidate.source_sha256 != task.task_sha256:
            raise ValueError("KernelBenchX manifest and adapter task hashes differ")
        raw = _read_regular(
            self.repository / candidate.source_path,
            label="KernelBenchX task source",
            max_bytes=1_048_576,
        )
        if _sha256(raw) != candidate.source_sha256:
            raise ValueError("KernelBenchX task source changed after provider preflight")
        try:
            reference = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise ValueError("KernelBenchX task source must be UTF-8") from exc
        _public_text(reference, label="KernelBenchX reference artifact")
        task_card = _public_text(
            (
                f"Optimize frozen KernelBenchX task {item.task_id}. Preserve the public "
                "call contract and exact numerical correctness, then minimize candidate "
                "runtime against the frozen reference."
            ),
            label="KernelBenchX task card",
        )
        evaluator_contract = {
            "evaluator": self.pool.evaluator,
            "repository_commit": self.pool.repository_commit,
            "dataset_commit": self.pool.dataset_commit,
            "task_sha256": task.task_sha256,
            "supervisor_sha256": _sha256(
                _read_regular(
                    self.adapter.supervisor,
                    label="KernelBenchX supervisor",
                    max_bytes=2 * 1024 * 1024,
                )
            ),
        }
        binding_sha = _binding_core_sha(
            staging_sha256=self.staging_plan_sha256,
            manifest_sha256=self.manifest_sha256,
            suite_receipt_sha256=self.suite_receipt_sha256,
            pool=self.pool,
            candidate=candidate,
            evaluator_contract=evaluator_contract,
        )
        return FormalTaskBinding(
            suite=self.suite,
            task_id=item.task_id,
            instance_id=item.instance_id,
            task_binding_sha256=binding_sha,
            task_card=task_card,
            reference_artifact=reference,
            instance_descriptors=(
                self.suite,
                candidate.category,
                "gpu-kernel",
                "mixed-precision",
            ),
            solution_codec=KernelBenchXSolutionCodec(task_id=item.task_id),
            evaluator=KernelBenchXEvaluationBackend(adapter=self.adapter, task=task),
        )


class CompilerGymFormalSuiteProvider:
    suite = "compilergym-cbench"

    def __init__(
        self,
        *,
        staging_plan_sha256: str,
        manifest_sha256: str,
        suite_receipt_sha256: str,
        pool: BenchmarkPool,
    ) -> None:
        self.staging_plan_sha256 = staging_plan_sha256
        self.manifest_sha256 = manifest_sha256
        self.suite_receipt_sha256 = suite_receipt_sha256
        self.pool = pool

    def bind(self, item: StreamItem) -> FormalTaskBinding:
        if item.suite != self.suite:
            raise ValueError("CompilerGym provider cannot bind another suite")
        candidate = _candidate(self.pool, item.task_id)
        uri = f"benchmark://cbench-v1/{item.task_id}"
        if uri not in CBENCH_BENCHMARK_URIS or candidate.source_path != uri:
            raise ValueError("CompilerGym task URI differs from the frozen adapter")
        contract = compilergym_frozen_contract(uri)
        task_card = _public_text(
            (
                f"Optimize frozen CompilerGym cBench instance {item.task_id}. Return one "
                "bounded LLVM action sequence. Fresh replay and every frozen ordinary "
                "semantic validator must pass before instruction-count speedup is valid."
            ),
            label="CompilerGym task card",
        )
        reference = json.dumps(
            {
                "task": uri,
                "frozen_evaluator_contract": contract,
                "candidate_contract": {
                    "schema_version": 1,
                    "benchmark_uri": uri,
                    "actions": "1..64 entries from the frozen LLVM action allowlist",
                },
            },
            ensure_ascii=True,
            indent=2,
            sort_keys=True,
        )
        binding_sha = _binding_core_sha(
            staging_sha256=self.staging_plan_sha256,
            manifest_sha256=self.manifest_sha256,
            suite_receipt_sha256=self.suite_receipt_sha256,
            pool=self.pool,
            candidate=candidate,
            evaluator_contract=contract,
        )
        adapter = CompilerGymCbenchAdapter(benchmark_uri=uri)
        return FormalTaskBinding(
            suite=self.suite,
            task_id=item.task_id,
            instance_id=item.instance_id,
            task_binding_sha256=binding_sha,
            task_card=task_card,
            reference_artifact=reference,
            instance_descriptors=(
                self.suite,
                candidate.category,
                "llvm-pass-sequence",
                "cpu-program-optimization",
            ),
            solution_codec=CompilerGymSolutionCodec(benchmark_uri=uri),
            evaluator=CompilerGymEvaluationBackend(adapter=adapter),
        )


_FACTORY_AUTHORITY = object()


class StagingBoundFormalProviderFactory:
    """FormalProviderFactory minted only by the all-suite composition gate."""

    def __init__(
        self,
        authority: object,
        *,
        staging_plan_sha256: str,
        providers: Mapping[str, FormalSuiteProvider],
    ) -> None:
        if authority is not _FACTORY_AUTHORITY:
            raise TypeError("formal provider factory requires composition authority")
        expected = {"kernelbenchx", "compilergym-cbench", "swe-perf"}
        if set(providers) != expected:
            raise ValueError("formal provider factory requires all three suites")
        self.staging_plan_sha256 = staging_plan_sha256
        self._providers = MappingProxyType(dict(providers))

    def create(self, suite: str) -> FormalSuiteProvider:
        try:
            return self._providers[suite]
        except KeyError as exc:
            raise ValueError("suite is outside the frozen formal provider set") from exc


def compose_formal_provider_factory(
    config: FormalProviderCompositionConfig,
) -> FormalProviderFactory:
    """Mint the production factory only after every suite gate has passed.

    SWE-Perf deliberately has no production provider in this revision, so the
    current implementation always fails closed before constructing any adapter.
    This is an executable safety property rather than a documentation warning.
    """

    state = _evaluate_composition(config)
    if not state.preflight.provider_factory_ready:
        suffix = ", ".join(state.preflight.blocker_codes) or "provider gates not ready"
        raise FormalProviderCompositionBlocked(
            f"HB-GEN-1 formal provider composition is blocked: {suffix}"
        )
    # A future reviewed SWE-Perf trusted-result implementation must add its
    # concrete provider here.  Keeping this branch unreachable prevents a
    # synthetic or None evaluator from satisfying FormalProviderFactory.
    raise FormalProviderCompositionBlocked(
        "HB-GEN-1 SWE-Perf trusted provider is not implemented"
    )


__all__ = [
    "CompilerGymFormalSuiteProvider",
    "FormalProviderCompositionBlocked",
    "FormalProviderCompositionConfig",
    "FormalProviderPreflight",
    "KernelBenchXFormalSuiteProvider",
    "StagingBoundFormalProviderFactory",
    "SuiteProviderPreflight",
    "compose_formal_provider_factory",
    "compose_verified_suite_provider",
    "preflight_formal_providers",
]
