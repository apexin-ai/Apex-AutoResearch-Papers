"""Trusted zero-call static Q0 evidence for the factorial benchmarks.

This module records only facts that can be reproduced without a model,
benchmark runtime, evaluator, container, GPU, or private GDPevo gold data.
For AgentHPOBench it replays the pinned Q7 checkout, derives each exact scalar
space, and executes three strict-codec negative assertions per task.  For
GDPevo it resolves only known Git tree objects from the pinned object database.

The artifact is deliberately *not* a reference, environment, or isolation
canary.  It cannot grant execution authority or resource entitlement.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
import hashlib
import json
import math
import os
from pathlib import Path
import re
import stat
import subprocess
from typing import Any, Mapping

from .agenthpo_intervention import (
    AgentHPOInterventionError,
    DiscreteInterventionSpace,
    derive_pinned_discrete_intervention_space,
    parse_strict_intervention,
)
from .agenthpo_qualification import (
    canonical_agenthpo_qualification_bytes,
    verify_agenthpo_qualification,
    verify_agenthpo_source_checkout,
)
from .gdpevo_qualification import (
    canonical_gdpevo_qualification_bytes,
    verify_gdpevo_qualification,
)


_AUTHORITY = "NOT_GRANTED"
_ZERO_SHA256 = "0" * 64
_SHA256 = re.compile(r"[0-9a-f]{64}")
_GIT_OID = re.compile(r"[0-9a-f]{40}")
_NEGATIVE_KINDS = (
    "unknown_key",
    "out_of_range_value",
    "no_operational_change",
)
_NEGATIVE_DISPOSITION = "STRICT_CODEC_REJECT_BEFORE_EVALUATOR"
_AGENTHPO_SOURCE_CHECKOUT = {
    "file_count": 31,
    "git_commit": "6d8d90071cdb16b06f0db866480ecaae48880fba",
    "root_tree": "1acedca0a63252deea57a51878b4ddfd002aa507",
    "verified": True,
}
_GDPEVO_SOURCE_CHECKOUT = {
    "git_commit": "0999c0d1e6f59b1cb8464cac4e5ed856b5dcb9e4",
    "root_tree": "983742f806f4bf6c4043d5ebea62dc4095be4c0d",
    "task_groups_tree": "2949144b022e5028ee8b48f4bb27355496df19de",
    "verified": True,
}
_ZERO_ENTITLEMENT = {
    "cpu_evaluator_seconds": 0,
    "evaluator_transactions": 0,
    "gpu_exclusive_seconds": 0,
    "max_parallel": 0,
    "model_calls": 0,
}
_EXPECTED_TOP_FIELDS = {
    "agenthpobench",
    "artifact_id",
    "artifact_kind",
    "execution_authority",
    "execution_entitlement",
    "gdpevo",
    "schema_version",
    "scope_boundary",
    "status",
}
_TRUSTED_CONSTRUCTION_TOKEN = object()
_MAX_EVIDENCE_BYTES = 4 * 1024 * 1024
_TASK_FIELDS = {
    "intervention_space_sha256",
    "negative_assertions",
    "source_receipt_sha256",
    "space_binding_sha256",
    "task_id",
    "task_source_sha256",
}
_ASSERTION_FIELDS = {
    "assertion_id",
    "candidate_canonical_json",
    "candidate_sha256",
    "disposition",
    "evaluator_called",
    "evaluator_transaction_debit",
    "negative_kind",
    "parser",
    "proposed_key",
    "rejection_code",
}
_GROUP_FIELDS = {
    "env_tree",
    "environment_object_type",
    "group_id",
    "group_object_type",
    "group_tree",
    "test_task_subtree_count",
    "test_tasks_object_type",
    "test_tasks_tree",
}


class FactorialStaticQ0EvidenceError(ValueError):
    """Static Q0 evidence is malformed, drifted, or asked to execute work."""


def _reject_constant(value: str) -> None:
    raise FactorialStaticQ0EvidenceError(
        f"static Q0 evidence contains non-finite constant {value}"
    )


def _reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise FactorialStaticQ0EvidenceError(
                f"static Q0 evidence repeats field {key!r}"
            )
        result[key] = value
    return result


def canonical_factorial_static_q0_evidence_bytes(payload: object) -> bytes:
    """Return the sole accepted canonical representation."""

    try:
        return (
            json.dumps(
                payload,
                allow_nan=False,
                ensure_ascii=False,
                separators=(",", ":"),
                sort_keys=True,
            )
            + "\n"
        ).encode("utf-8")
    except (TypeError, ValueError, UnicodeError) as exc:
        raise FactorialStaticQ0EvidenceError(
            "static Q0 evidence is not canonical JSON"
        ) from exc


def _canonical_candidate(payload: Mapping[str, object]) -> bytes:
    return json.dumps(
        dict(payload),
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _load_canonical(raw: bytes) -> dict[str, Any]:
    if not isinstance(raw, bytes) or not raw or len(raw) > _MAX_EVIDENCE_BYTES:
        raise FactorialStaticQ0EvidenceError(
            "static Q0 evidence byte length is invalid"
        )
    try:
        payload = json.loads(
            raw.decode("utf-8", errors="strict"),
            object_pairs_hook=_reject_duplicates,
            parse_constant=_reject_constant,
        )
    except FactorialStaticQ0EvidenceError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise FactorialStaticQ0EvidenceError(
            "static Q0 evidence is not strict JSON"
        ) from exc
    if not isinstance(payload, dict):
        raise FactorialStaticQ0EvidenceError(
            "static Q0 evidence must be a JSON object"
        )
    if raw != canonical_factorial_static_q0_evidence_bytes(payload):
        raise FactorialStaticQ0EvidenceError(
            "static Q0 evidence is not canonically encoded"
        )
    return payload


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _validate_payload(payload: Mapping[str, Any]) -> None:
    if set(payload) != _EXPECTED_TOP_FIELDS:
        raise FactorialStaticQ0EvidenceError("static Q0 evidence fields differ")
    if (
        payload["schema_version"] != 1
        or payload["artifact_id"] != "moss-factorial-static-q0-evidence-v1"
        or payload["artifact_kind"]
        != "PINNED_SOURCE_AND_STRICT_CODEC_STATIC_EVIDENCE_ONLY"
        or payload["status"] != "STATIC_FACTS_VERIFIED_EXECUTION_BLOCKED"
        or payload["execution_authority"] != _AUTHORITY
        or payload["execution_entitlement"] != _ZERO_ENTITLEMENT
    ):
        raise FactorialStaticQ0EvidenceError(
            "static Q0 evidence identity or zero-authority contract differs"
        )
    scope = payload["scope_boundary"]
    if not isinstance(scope, dict) or scope != {
        "benchmark_runtime_called": False,
        "evaluator_called": False,
        "formal_execution_ready": False,
        "is_environment_canary": False,
        "is_isolation_canary": False,
        "is_reference_canary": False,
        "model_called": False,
        "private_gdpevo_gold_content_read": False,
    }:
        raise FactorialStaticQ0EvidenceError(
            "static Q0 evidence scope overclaims canary execution"
        )
    agent = payload["agenthpobench"]
    if (
        not isinstance(agent, dict)
        or agent.get("task_count") != 7
        or agent.get("negative_assertion_count") != 21
        or agent.get("space_variant") != "original"
        or agent.get("source_checkout") != _AGENTHPO_SOURCE_CHECKOUT
        or not isinstance(agent.get("tasks"), list)
        or len(agent["tasks"]) != 7
    ):
        raise FactorialStaticQ0EvidenceError(
            "AgentHPO static Q0 evidence coverage differs"
        )
    agent_qualification = verify_agenthpo_qualification()
    expected_agent_ids = tuple(
        task["task_id"] for task in agent_qualification["qualification_tasks"]
    )
    if agent.get("qualification_sha256") != _sha256_bytes(
        canonical_agenthpo_qualification_bytes(agent_qualification)
    ):
        raise FactorialStaticQ0EvidenceError(
            "AgentHPO static qualification binding differs"
        )
    task_ids: list[str] = []
    for task in agent["tasks"]:
        if (
            not isinstance(task, dict)
            or set(task) != _TASK_FIELDS
            or not isinstance(task.get("task_id"), str)
            or any(
                _SHA256.fullmatch(str(task.get(field))) is None
                for field in (
                    "intervention_space_sha256",
                    "source_receipt_sha256",
                    "space_binding_sha256",
                    "task_source_sha256",
                )
            )
        ):
            raise FactorialStaticQ0EvidenceError(
                "AgentHPO static task evidence is malformed"
            )
        task_ids.append(task["task_id"])
        assertions = task.get("negative_assertions")
        if not isinstance(assertions, list) or len(assertions) != 3:
            raise FactorialStaticQ0EvidenceError(
                "AgentHPO static negative coverage differs"
            )
        for kind, assertion in zip(_NEGATIVE_KINDS, assertions, strict=True):
            if not isinstance(assertion, dict) or set(assertion) != _ASSERTION_FIELDS:
                raise FactorialStaticQ0EvidenceError(
                    "AgentHPO static negative assertion is malformed"
                )
            candidate_text = assertion.get("candidate_canonical_json")
            if (
                not isinstance(candidate_text, str)
                or not candidate_text
                or len(candidate_text.encode("utf-8")) > 4096
            ):
                raise FactorialStaticQ0EvidenceError(
                    "AgentHPO static negative candidate is malformed"
                )
            try:
                candidate = json.loads(
                    candidate_text,
                    object_pairs_hook=_reject_duplicates,
                    parse_constant=_reject_constant,
                )
            except (json.JSONDecodeError, FactorialStaticQ0EvidenceError) as exc:
                raise FactorialStaticQ0EvidenceError(
                    "AgentHPO static negative candidate is not strict JSON"
                ) from exc
            proposed_key = assertion.get("proposed_key")
            expected_rejection = {
                "unknown_key": "UNKNOWN_KEY",
                "out_of_range_value": "OUT_OF_RANGE_VALUE",
                "no_operational_change": "NO_OPERATIONAL_CHANGE",
            }[kind]
            if (
                not isinstance(candidate, dict)
                or len(candidate) != 1
                or _canonical_candidate(candidate).decode("utf-8") != candidate_text
                or not isinstance(proposed_key, str)
                or tuple(candidate) != (proposed_key,)
                or assertion.get("assertion_id")
                != f"agenthpobench:q7:{task['task_id']}:{kind}"
                or assertion.get("disposition") != _NEGATIVE_DISPOSITION
                or assertion.get("evaluator_called") is not False
                or assertion.get("evaluator_transaction_debit") != 0
                or assertion.get("parser") != "parse_strict_intervention"
                or assertion.get("negative_kind") != kind
                or assertion.get("rejection_code") != expected_rejection
                or _SHA256.fullmatch(str(assertion.get("candidate_sha256"))) is None
                or _sha256_bytes(candidate_text.encode("utf-8"))
                != assertion.get("candidate_sha256")
                or (
                    kind == "unknown_key"
                    and candidate != {"__moss_unknown_parameter__": 0}
                )
            ):
                raise FactorialStaticQ0EvidenceError(
                    "AgentHPO static negative disposition differs"
                )
    if tuple(task_ids) != expected_agent_ids:
        raise FactorialStaticQ0EvidenceError(
            "AgentHPO static task identities or order differ"
        )
    gdpevo = payload["gdpevo"]
    if (
        not isinstance(gdpevo, dict)
        or gdpevo.get("qualification_group_count") != 6
        or gdpevo.get("source_checkout") != _GDPEVO_SOURCE_CHECKOUT
        or not isinstance(gdpevo.get("qualification_groups"), list)
        or len(gdpevo["qualification_groups"]) != 6
    ):
        raise FactorialStaticQ0EvidenceError(
            "GDPevo static Q0 evidence coverage differs"
        )
    manifest = gdpevo.get("file_manifest_replay")
    if manifest != {
        "expected_contract_projection_sha256": manifest.get(
            "expected_contract_projection_sha256"
        )
        if isinstance(manifest, dict)
        else None,
        "mechanically_recomputed": False,
        "private_file_content_read": False,
        "status": "UNVERIFIED_NO_FROZEN_REPLAY_ALGORITHM",
    } or _SHA256.fullmatch(
        str(manifest.get("expected_contract_projection_sha256"))
        if isinstance(manifest, dict)
        else ""
    ) is None:
        raise FactorialStaticQ0EvidenceError(
            "GDPevo file-manifest replay must remain explicitly unverified"
        )
    gdpevo_qualification = verify_gdpevo_qualification()
    if gdpevo.get("qualification_sha256") != _sha256_bytes(
        canonical_gdpevo_qualification_bytes(gdpevo_qualification)
    ):
        raise FactorialStaticQ0EvidenceError(
            "GDPevo static qualification binding differs"
        )
    expected_groups = gdpevo_qualification["qualification_groups"]
    group_ids: list[str] = []
    for group, expected_group in zip(
        gdpevo["qualification_groups"], expected_groups, strict=True
    ):
        if not isinstance(group, dict) or set(group) != _GROUP_FIELDS:
            raise FactorialStaticQ0EvidenceError(
                "GDPevo static group evidence is malformed"
            )
        group_ids.append(str(group.get("group_id")))
        if (
            group.get("group_object_type") != "tree"
            or group.get("environment_object_type") != "tree"
            or group.get("test_tasks_object_type") != "tree"
            or group.get("test_task_subtree_count") != 5
            or group.get("group_id") != expected_group["group_id"]
            or group.get("group_tree") != expected_group["trees"]["group_tree"]
            or group.get("env_tree") != expected_group["trees"]["env_tree"]
            or group.get("test_tasks_tree")
            != expected_group["trees"]["test_tasks_tree"]
            or any(
                _GIT_OID.fullmatch(str(group.get(field))) is None
                for field in ("group_tree", "env_tree", "test_tasks_tree")
            )
        ):
            raise FactorialStaticQ0EvidenceError(
                "GDPevo static group-tree evidence differs"
            )
    if tuple(group_ids) != tuple(item["group_id"] for item in expected_groups):
        raise FactorialStaticQ0EvidenceError(
            "GDPevo static group identities repeat"
        )


@dataclass(frozen=True, init=False)
class FactorialStaticQ0Evidence:
    """Source-rederived static evidence, never a caller-validated DTO.

    Construction is intentionally private.  Persisted bytes must be consumed
    through :func:`verify_factorial_static_q0_evidence`, which rebuilds all
    source and codec facts before it returns this type.
    """

    canonical_bytes: bytes

    def __init__(self, canonical_bytes: bytes, *, _trusted_token: object = None):
        if _trusted_token is not _TRUSTED_CONSTRUCTION_TOKEN:
            raise FactorialStaticQ0EvidenceError(
                "static Q0 evidence requires trusted source replay"
            )
        _validate_payload(_load_canonical(canonical_bytes))
        object.__setattr__(self, "canonical_bytes", canonical_bytes)

    @classmethod
    def _from_trusted_payload(
        cls, payload: Mapping[str, Any]
    ) -> "FactorialStaticQ0Evidence":
        if not isinstance(payload, Mapping):
            raise FactorialStaticQ0EvidenceError(
                "static Q0 evidence payload must be a mapping"
            )
        return cls(
            canonical_factorial_static_q0_evidence_bytes(dict(payload)),
            _trusted_token=_TRUSTED_CONSTRUCTION_TOKEN,
        )

    @property
    def sha256(self) -> str:
        return _sha256_bytes(self.canonical_bytes)

    def to_dict(self) -> dict[str, Any]:
        return deepcopy(_load_canonical(self.canonical_bytes))


def _explicit_checkout(path_value: str | Path, *, label: str) -> Path:
    path = Path(path_value)
    if not path.is_absolute():
        raise FactorialStaticQ0EvidenceError(f"{label} must be absolute")
    current = path
    while True:
        try:
            if stat.S_ISLNK(os.lstat(current).st_mode):
                raise FactorialStaticQ0EvidenceError(
                    f"{label} may not contain symlinks"
                )
        except OSError as exc:
            raise FactorialStaticQ0EvidenceError(
                f"cannot inspect {label} path"
            ) from exc
        parent = current.parent
        if parent == current:
            break
        current = parent
    try:
        resolved = path.resolve(strict=True)
    except OSError as exc:
        raise FactorialStaticQ0EvidenceError(f"{label} does not resolve") from exc
    if resolved != path or not resolved.is_dir():
        raise FactorialStaticQ0EvidenceError(
            f"{label} is not its explicit real directory"
        )
    return resolved


def _git(root: Path, *args: str) -> str:
    environment = dict(os.environ)
    environment["GIT_OPTIONAL_LOCKS"] = "0"
    try:
        completed = subprocess.run(
            ("git", "-C", os.fspath(root), *args),
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=15,
            env=environment,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise FactorialStaticQ0EvidenceError(
            "cannot verify pinned Git object database"
        ) from exc
    return completed.stdout.strip()


def _require_clean_tracked_checkout(root: Path) -> None:
    if _git(
        root,
        "--no-optional-locks",
        "status",
        "--porcelain=v1",
        "--untracked-files=no",
    ):
        raise FactorialStaticQ0EvidenceError("pinned tracked checkout is dirty")


def _tree_oid(root: Path, git_path: str) -> str:
    oid = _git(root, "rev-parse", "--verify", f"HEAD:{git_path}")
    if _GIT_OID.fullmatch(oid) is None or _git(root, "cat-file", "-t", oid) != "tree":
        raise FactorialStaticQ0EvidenceError(
            f"pinned Git path is not a tree: {git_path}"
        )
    return oid


def _test_task_subtree_count(root: Path, git_path: str) -> int:
    lines = _git(root, "ls-tree", f"HEAD:{git_path}").splitlines()
    expected_names = {f"{index:03d}" for index in range(1, 6)}
    names: set[str] = set()
    for line in lines:
        try:
            metadata, name = line.split("\t", 1)
            mode, object_type, oid = metadata.split(" ", 2)
        except ValueError as exc:
            raise FactorialStaticQ0EvidenceError(
                "GDPevo test-task tree listing is malformed"
            ) from exc
        if mode != "040000" or object_type != "tree" or _GIT_OID.fullmatch(oid) is None:
            raise FactorialStaticQ0EvidenceError(
                "GDPevo test-task entry is not a committed tree"
            )
        names.add(name)
    if names != expected_names:
        raise FactorialStaticQ0EvidenceError(
            "GDPevo qualification test-task tree does not contain 001-005"
        )
    return len(names)


def _out_of_range_candidate(
    space: DiscreteInterventionSpace,
) -> tuple[str, None | bool | int | float | str]:
    for key in sorted(space.allowed_values):
        concrete = tuple(value for value in space.allowed_values[key] if value is not None)
        if not concrete:
            continue
        value_type = type(concrete[0])
        if value_type is int:
            candidate = max(value for value in concrete if type(value) is int) + 1
            while any(type(value) is int and value == candidate for value in concrete):
                candidate += 1
            return key, candidate
        if value_type is float:
            numeric = [value for value in concrete if type(value) is float]
            candidate = max(numeric) + max(1.0, max(abs(value) for value in numeric))
            while not math.isfinite(candidate) or any(
                type(value) is float and value == candidate for value in concrete
            ):
                candidate = (candidate / 2.0) + 0.123456789
            return key, candidate
        if value_type is str:
            candidate = "__moss_static_q0_out_of_range__"
            if candidate not in concrete:
                return key, candidate
    raise FactorialStaticQ0EvidenceError(
        "Q7 space has no same-type scalar axis for out-of-range evidence"
    )


def _negative_assertion(
    *,
    task_id: str,
    kind: str,
    raw: bytes,
    proposed_key: str,
    expected_message: str,
    rejection_code: str,
    space: DiscreteInterventionSpace,
) -> dict[str, Any]:
    try:
        parse_strict_intervention(raw, space=space)
    except AgentHPOInterventionError as exc:
        if expected_message not in str(exc):
            raise FactorialStaticQ0EvidenceError(
                f"AgentHPO negative {kind} rejected for the wrong reason"
            ) from exc
    else:
        raise FactorialStaticQ0EvidenceError(
            f"AgentHPO negative {kind} unexpectedly passed strict codec"
        )
    return {
        "assertion_id": f"agenthpobench:q7:{task_id}:{kind}",
        "candidate_canonical_json": raw.decode("utf-8", errors="strict"),
        "candidate_sha256": _sha256_bytes(raw),
        "disposition": _NEGATIVE_DISPOSITION,
        "evaluator_called": False,
        "evaluator_transaction_debit": 0,
        "negative_kind": kind,
        "parser": "parse_strict_intervention",
        "proposed_key": proposed_key,
        "rejection_code": rejection_code,
    }


def _agenthpo_task_evidence(
    root: Path, task_id: str
) -> dict[str, Any]:
    space, binding, receipt = derive_pinned_discrete_intervention_space(
        root,
        task_id=task_id,
        space_variant="original",
        current_config=None,
        previous_outcome_sha256=_ZERO_SHA256,
    )
    unknown_raw = _canonical_candidate({"__moss_unknown_parameter__": 0})
    out_key, out_value = _out_of_range_candidate(space)
    out_raw = _canonical_candidate({out_key: out_value})
    no_op_key = sorted(space.current_config)[0]
    no_op_raw = _canonical_candidate({no_op_key: space.current_config[no_op_key]})
    assertions = [
        _negative_assertion(
            task_id=task_id,
            kind="unknown_key",
            raw=unknown_raw,
            proposed_key="__moss_unknown_parameter__",
            expected_message="contains unknown keys",
            rejection_code="UNKNOWN_KEY",
            space=space,
        ),
        _negative_assertion(
            task_id=task_id,
            kind="out_of_range_value",
            raw=out_raw,
            proposed_key=out_key,
            expected_message="is outside the allowlist",
            rejection_code="OUT_OF_RANGE_VALUE",
            space=space,
        ),
        _negative_assertion(
            task_id=task_id,
            kind="no_operational_change",
            raw=no_op_raw,
            proposed_key=no_op_key,
            expected_message="makes no operational configuration change",
            rejection_code="NO_OPERATIONAL_CHANGE",
            space=space,
        ),
    ]
    return {
        "intervention_space_sha256": space.sha256,
        "negative_assertions": assertions,
        "source_receipt_sha256": receipt.sha256,
        "space_binding_sha256": binding.sha256,
        "task_id": task_id,
        "task_source_sha256": space.task_source_sha256,
    }


def _gdpevo_evidence(root: Path, qualification: Mapping[str, Any]) -> dict[str, Any]:
    lock = qualification["source_lock"]
    commit = _git(root, "rev-parse", "--verify", "HEAD^{commit}")
    root_tree = _git(root, "rev-parse", "--verify", "HEAD^{tree}")
    task_groups_tree = _tree_oid(root, "data/task_groups")
    if (
        commit != lock["git_commit"]
        or root_tree != lock["root_tree"]
        or task_groups_tree != lock["task_groups_tree"]
    ):
        raise FactorialStaticQ0EvidenceError("GDPevo pinned source identity drifted")
    groups = []
    for group in qualification["qualification_groups"]:
        group_id = group["group_id"]
        prefix = f"data/task_groups/{group_id}"
        group_tree = _tree_oid(root, prefix)
        env_tree = _tree_oid(root, f"{prefix}/env")
        test_tasks_tree = _tree_oid(root, f"{prefix}/test_tasks")
        expected = group["trees"]
        if (
            group_tree != expected["group_tree"]
            or env_tree != expected["env_tree"]
            or test_tasks_tree != expected["test_tasks_tree"]
        ):
            raise FactorialStaticQ0EvidenceError(
                f"GDPevo pinned Q6 tree drifted: {group_id}"
            )
        groups.append(
            {
                "env_tree": env_tree,
                "environment_object_type": "tree",
                "group_id": group_id,
                "group_object_type": "tree",
                "group_tree": group_tree,
                "test_task_subtree_count": _test_task_subtree_count(
                    root, f"{prefix}/test_tasks"
                ),
                "test_tasks_object_type": "tree",
                "test_tasks_tree": test_tasks_tree,
            }
        )
    file_manifests = qualification["file_manifests"]
    return {
        "file_manifest_replay": {
            "expected_contract_projection_sha256": _sha256_bytes(
                canonical_factorial_static_q0_evidence_bytes(file_manifests)
            ),
            "mechanically_recomputed": False,
            "private_file_content_read": False,
            "status": "UNVERIFIED_NO_FROZEN_REPLAY_ALGORITHM",
        },
        "qualification_group_count": len(groups),
        "qualification_groups": groups,
        "qualification_sha256": _sha256_bytes(
            canonical_gdpevo_qualification_bytes(qualification)
        ),
        "source_checkout": {
            "git_commit": commit,
            "root_tree": root_tree,
            "task_groups_tree": task_groups_tree,
            "verified": True,
        },
    }


def build_factorial_static_q0_evidence(
    *,
    agenthpo_checkout: str | Path,
    gdpevo_checkout: str | Path,
) -> FactorialStaticQ0Evidence:
    """Recompute static source/codec facts without any execution authority."""

    agent_root = _explicit_checkout(agenthpo_checkout, label="AgentHPO checkout")
    gdpevo_root = _explicit_checkout(gdpevo_checkout, label="GDPevo checkout")
    _require_clean_tracked_checkout(agent_root)
    # GDPevo evidence is derived exclusively from committed tree objects.  Do
    # not run whole-worktree status here: it may inspect/hash evaluator or gold
    # files that are explicitly outside this static evidence boundary.
    agent_qualification = verify_agenthpo_qualification()
    gdpevo_qualification = verify_gdpevo_qualification()
    agent_lock = agent_qualification["source_lock"]
    commit = _git(agent_root, "rev-parse", "--verify", "HEAD^{commit}")
    root_tree = _git(agent_root, "rev-parse", "--verify", "HEAD^{tree}")
    source_checkout = verify_agenthpo_source_checkout(
        agent_root,
        observed_git_commit=commit,
        observed_root_tree=root_tree,
    )
    task_evidence = [
        _agenthpo_task_evidence(agent_root, task["task_id"])
        for task in agent_qualification["qualification_tasks"]
    ]
    payload = {
        "agenthpobench": {
            "negative_assertion_count": sum(
                len(task["negative_assertions"]) for task in task_evidence
            ),
            "qualification_sha256": _sha256_bytes(
                canonical_agenthpo_qualification_bytes(agent_qualification)
            ),
            "source_checkout": dict(source_checkout),
            "space_variant": "original",
            "task_count": len(task_evidence),
            "tasks": task_evidence,
        },
        "artifact_id": "moss-factorial-static-q0-evidence-v1",
        "artifact_kind": "PINNED_SOURCE_AND_STRICT_CODEC_STATIC_EVIDENCE_ONLY",
        "execution_authority": _AUTHORITY,
        "execution_entitlement": dict(_ZERO_ENTITLEMENT),
        "gdpevo": _gdpevo_evidence(gdpevo_root, gdpevo_qualification),
        "schema_version": 1,
        "scope_boundary": {
            "benchmark_runtime_called": False,
            "evaluator_called": False,
            "formal_execution_ready": False,
            "is_environment_canary": False,
            "is_isolation_canary": False,
            "is_reference_canary": False,
            "model_called": False,
            "private_gdpevo_gold_content_read": False,
        },
        "status": "STATIC_FACTS_VERIFIED_EXECUTION_BLOCKED",
    }
    if commit != agent_lock["git_commit"] or root_tree != agent_lock["root_tree"]:
        raise FactorialStaticQ0EvidenceError("AgentHPO pinned source identity drifted")
    return FactorialStaticQ0Evidence._from_trusted_payload(payload)


def verify_factorial_static_q0_evidence(
    artifact: FactorialStaticQ0Evidence | Mapping[str, Any] | bytes | None = None,
    *,
    agenthpo_checkout: str | Path,
    gdpevo_checkout: str | Path,
    request_execution: bool = False,
) -> FactorialStaticQ0Evidence:
    """Trusted entry: rederive sources/assertions and compare exact bytes."""

    if request_execution:
        raise FactorialStaticQ0EvidenceError(
            "static Q0 evidence has no execution authority or entitlement"
        )
    expected = build_factorial_static_q0_evidence(
        agenthpo_checkout=agenthpo_checkout,
        gdpevo_checkout=gdpevo_checkout,
    )
    if artifact is None:
        return expected
    if isinstance(artifact, FactorialStaticQ0Evidence):
        observed_bytes = artifact.canonical_bytes
    elif isinstance(artifact, bytes):
        _validate_payload(_load_canonical(artifact))
        observed_bytes = artifact
    elif isinstance(artifact, Mapping):
        observed_bytes = canonical_factorial_static_q0_evidence_bytes(
            dict(artifact)
        )
        _validate_payload(_load_canonical(observed_bytes))
    else:
        raise FactorialStaticQ0EvidenceError(
            "unsupported static Q0 evidence artifact type"
        )
    if observed_bytes != expected.canonical_bytes:
        raise FactorialStaticQ0EvidenceError(
            "static Q0 evidence differs from trusted source replay"
        )
    return expected


__all__ = [
    "FactorialStaticQ0Evidence",
    "FactorialStaticQ0EvidenceError",
    "build_factorial_static_q0_evidence",
    "canonical_factorial_static_q0_evidence_bytes",
    "verify_factorial_static_q0_evidence",
]
