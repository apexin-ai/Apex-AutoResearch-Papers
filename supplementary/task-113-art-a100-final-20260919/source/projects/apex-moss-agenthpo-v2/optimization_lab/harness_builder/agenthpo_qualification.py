"""Static, zero-entitlement qualification contract for AgentHPOBench.

The checked-in artifact freezes source and Q7 evaluator inputs, but this module
cannot launch a task, model, or evaluator.  Moss now has a zero-call strict
intervention codec, mechanical derivation for the pinned scalar spaces, and
typed request receipts.  Those local artifacts are not formal authority: the
free-form Agent-Lightning task still needs a separate codec or fresh split,
and future execution needs formal provider dispatch plus one trusted transport
ledger that proves no provider request was omitted.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
import os
from pathlib import Path
import stat
from typing import Any, Mapping, Sequence


DEFAULT_AGENTHPO_QUALIFICATION_MANIFEST = (
    Path(__file__).with_name("data") / "agenthpo_qualification_canary_v1.json"
)

_HEX = set("0123456789abcdef")
_Q_TASKS = (
    {
        "anchor": 90.4,
        "baseline": 38.960774325,
        "category": "NLP",
        "direction": "higher",
        "files": {
            "tasks/main/modernbert_mnli_accuracy/baseline.json": "4b3b1254a0897b96ce804b076843ebe799c0b406b44047be154f71ae0fe0feea",
            "tasks/main/modernbert_mnli_accuracy/eval_modernbert_mnli.py": "8c43f867d1b8b64f7d890a8f8de6570286f9d4a8e02ce4d99897f4671b23bfba",
            "tasks/main/modernbert_mnli_accuracy/run_formal_modernbert_mnli_agent.py": "57ee526cd4d62a236b80149ef2bbe288c5c00317260bfe1cf55d15cfe9a4b404",
        },
        "task_id": "modernbert_mnli_accuracy",
        "upstream_revision": "c6d942312f1b0b24d423628b8e477a3e97c7038f",
    },
    {
        "anchor": 94.01,
        "baseline": 89.0899956226,
        "category": "CV",
        "direction": "higher",
        "files": {
            "tasks/main/cifar10_airbench94/baseline.json": "f236bb625702ffeb4956c36790bd4e3961e4952fb77371c7e19daf7ca46b96fc",
            "tasks/main/cifar10_airbench94/eval_cifar10_airbench94.py": "a78446bf4068bad76310c8a8a70f28ccacfff640c393a43a04cb8201fa981cc6",
            "tasks/main/cifar10_airbench94/run_formal_cifar10_airbench94_agent.py": "cc48d09ca74d4eec22c7ba1236229d34da4ae496ed58774e9f4ead43c473909b",
        },
        "task_id": "cifar10_airbench94",
        "upstream_revision": "4c1b6d1e3889b037efadcfd5c0ea65b246592362",
    },
    {
        "anchor": 0.314,
        "baseline": 0.340816259516,
        "category": "TS",
        "direction": "lower",
        "files": {
            "tasks/main/sparsetsf_ettm1_96_mse/baseline.json": "b0986ad0c080d32c9a225d4b9d766065033219d405ab6c3a609cae1bd7f5023c",
            "tasks/main/sparsetsf_ettm1_96_mse/eval_sparsetsf_ettm1.py": "d964b9631ef945df82dbdfb12723de99a1c667563f8e31ac77628789127cd493",
            "tasks/main/sparsetsf_ettm1_96_mse/run_formal_sparsetsf_agent.py": "dd90c27861ca6ed2afcf3bc17cd1e3cf4d7e8e7b809919bb7ff43293c22afc57",
        },
        "task_id": "sparsetsf_ettm1_96_mse",
        "upstream_revision": "b8c2740eecc84d8095ffce49ba5acafe68e53bb8",
    },
    {
        "anchor": 71.06,
        "baseline": 70.0000047684,
        "category": "Graph",
        "direction": "higher",
        "files": {
            "tasks/main/noisygl_cora_uniform30_gcn/baseline.json": "c1cfa98dce53fbd4e30e177000d497aee4293d14efc274af2a61092cc177e782",
            "tasks/main/noisygl_cora_uniform30_gcn/eval_noisygl_cora_gcn.py": "a8b45148183f08bf3c64189bb15ee073407fc275285d3a05f5e6afe7747f781c",
            "tasks/main/noisygl_cora_uniform30_gcn/run_formal_noisygl_cora_gcn_agent.py": "8f8434d1c92f87e7c058bafd114a564727b71ef9166b78c9bf039c7ef51546af",
        },
        "task_id": "noisygl_cora_uniform30_gcn",
        "upstream_revision": "b6ac057fe8c45a1475a32dba823971372186e445",
    },
    {
        "anchor": 0.6,
        "baseline": 0.0,
        "category": "RL",
        "direction": "higher",
        "files": {
            "tasks/main/art_2048_win_rate/baseline.json": "1d0db178e318aede0aa5cc15b1ead87dedf658bcb3d7582ade4b64f03aa6518f",
            "tasks/main/art_2048_win_rate/eval_art_2048_win_rate.py": "5e098b011d7e6a7a2f8e3fbfc7261009a96c2a7d7130d272ca46c7546194492d",
            "tasks/main/art_2048_win_rate/run_formal_art_2048_win_rate_agent.py": "3ed7756d1b93660d59cfe3353004f539f7074125e8ee80cdadd4da1d0d6d59c6",
        },
        "task_id": "art_2048_win_rate",
        "upstream_revision": "4cbfa15dc161269720b12b0768ff84754f4a4331",
    },
    {
        "anchor": 34.4,
        "baseline": 15.8,
        "category": "LLM",
        "direction": "higher",
        "files": {
            "tasks/main/simple_rl_reason_qwen25_05b_math500/baseline.json": "6ed136e35620fdbbda04317821970050b2b5f4b347aa3fc19095b750ecee785d",
            "tasks/main/simple_rl_reason_qwen25_05b_math500/run_formal_simple_rl_reason_qwen25_05b_math500_agent.py": "1555218bae01c7e66d42bf92d88a3353da951218e9edc0e17dbffe8198a8a855",
        },
        "patch_sha256": "4dab81c185aa9a2e0f46012f956ac55b3243840e53ce51a1c33db8806eaf2767",
        "task_id": "simple_rl_reason_qwen25_05b_math500",
        "upstream_revision": "cf1c7858bfc145a27aa733e75d930d34f0d318a6",
    },
    {
        "anchor": 0.86,
        "baseline": 1.48707354069,
        "category": "SL",
        "direction": "lower",
        "files": {
            "tasks/main/vbll_yacht_rmse/baseline.json": "77882fa02672525ea25336c6dc7a2a1d13bf52ac6af5afe9fcdacc53855eb231",
            "tasks/main/vbll_yacht_rmse/eval_vbll_yacht.py": "a22e91905ed18df63a3fcb0db6a39bc519f32d92fad1f262ccd26831a866145a",
            "tasks/main/vbll_yacht_rmse/run_formal_vbll_yacht_agent.py": "4c8d40f0b3ca5095e7f7a838963f7426f29bb12b094f3343394c0b3e7778730e",
        },
        "task_id": "vbll_yacht_rmse",
        "upstream_revision": "142f21edd606c1584a15b003bbfb732b4ba2affc",
    },
)

_CONTROL_FILES = {
    "agenthpobench/agents/api_decision_client.py": "717e1bd0f19dfe0d75210d7184a53c8b4dcda70c0d079452d8e8e70bc204850b",
    "agenthpobench/evaluation/metrics.py": "8a348e8405a59db37b37ed85c274df3d155432792959a5a1708095da7a4a2abc",
    "agenthpobench/evaluation/result_integrity.py": "cde22e0f7c4c932c422cd4c176e74ea5fa836a7100d651748c3b66c4aaca3e0f",
    "analysis/summarize_multiseed.py": "c847cf3dd9aaec9bdd37f0f83a1154090477fadbaca835fe51a457f7ad07aa00",
    "analysis/validate_results.py": "cd98e5072aee3df7f6eb5ded36642df0f0a9f91ced62f5d3e62a24f5d991f2e3",
    "configs/repositories.json": "6f847dc2da4bfe90e61d47006e1148eee36202bfd0f1ef2ba91bd83e23dd0eca",
    "configs/scoring_reference.tsv": "c17ad42d27aee047611ab824446dae539724d09b61bf9fa945932bfb17201308",
    "configs/tasks.json": "e2fc5c9ec93018f3e148bfaf79e7bbb12dd5c7a14dafc9267c2578709e1fe2b7",
    "tasks/main/_budget_agent_common.py": "2558d4f445f6275e401eec41b7fcd287873a031cc21734b61969f7a328ad23f5",
    "tasks/main/run_strict_space_agent.py": "275a2dc8f5a508be4af41f4aba2c255dae582b4c922f4684e2867436329a26ac",
    "tasks/main/space_manifest.json": "68d466bc0069908ad178f9a5921e618077545b7aa44d5f64f65cb77cbb88f7de",
}

_BLOCKERS = (
    "agenthpobench_free_form_prompt_codec_or_fresh_split_required",
    "agenthpobench_formal_intervention_dispatch_integration_missing",
    "agenthpobench_trusted_transport_ledger_missing",
    "agenthpobench_upstream_repositories_absent",
    "agenthpobench_datasets_checkpoints_and_models_absent",
    "agenthpobench_target_gpu_environment_unverified",
    "agenthpobench_reference_negative_isolation_canary_pending",
)
_ZERO_ENTITLEMENT = {
    "cpu_evaluator_seconds": 0,
    "evaluator_transactions": 0,
    "gpu_exclusive_seconds": 0,
    "max_parallel": 0,
    "model_calls": 0,
}
_PUBLIC_FIELDS = (
    "bounded_normalized_score",
    "validity",
    "coarse_reason_codes",
)
_METRIC_KEYS = {
    "art_2048_win_rate": ("win_rate", "score"),
    "cifar10_airbench94": ("accuracy_percent", "test_accuracy", "accuracy"),
    "modernbert_mnli_accuracy": ("accuracy_percent", "validation_accuracy"),
    "noisygl_cora_uniform30_gcn": (
        "test_accuracy_percent",
        "accuracy_percent",
        "test_accuracy",
        "accuracy",
    ),
    "simple_rl_reason_qwen25_05b_math500": (
        "math500_accuracy_percent",
        "accuracy_percent",
        "accuracy",
    ),
    "sparsetsf_ettm1_96_mse": ("test_mse_at_best_val", "test_mse", "mse"),
    "vbll_yacht_rmse": ("test_rmse", "rmse"),
}


class AgentHPOQualificationError(ValueError):
    """The AgentHPOBench qualification artifact is unsafe or has drifted."""


@dataclass(frozen=True)
class AgentHPOAdapterResult:
    """Bounded planner-visible output and controller-private raw evidence."""

    public_projection: Mapping[str, object]
    private_evidence: Mapping[str, object]


def _reject_constant(value: str) -> None:
    raise AgentHPOQualificationError(f"result JSON contains {value}")


def _reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    payload: dict[str, Any] = {}
    for key, value in pairs:
        if key in payload:
            raise AgentHPOQualificationError(f"JSON repeats field {key!r}")
        payload[key] = value
    return payload


def canonical_agenthpo_qualification_bytes(payload: object) -> bytes:
    """Return the only accepted encoding for the checked-in contract."""

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
    except (TypeError, ValueError) as exc:
        raise AgentHPOQualificationError(
            "AgentHPOBench qualification payload is not canonical JSON"
        ) from exc


def _expected_contract() -> dict[str, object]:
    tasks = []
    for item in _Q_TASKS:
        tasks.append(
            {
                "anchor": item["anchor"],
                "baseline": item["baseline"],
                "category": item["category"],
                "direction": item["direction"],
                "files": item["files"],
                **(
                    {"patch_sha256": item["patch_sha256"]}
                    if "patch_sha256" in item
                    else {}
                ),
                "task_id": item["task_id"],
                "upstream_revision": item["upstream_revision"],
            }
        )
    return {
        "adapter_contract": {
            "accepted_result_protocol": {
                "decision_count": 5,
                "fallback_decision_count": 0,
                "final_intervention_scored": True,
                "raw_response_count": 5,
                "trace_length_including_baseline": 6,
            },
            "input_encoding": "controller_private_strict_result_envelope_v1",
            "metric_normalization": "directional_baseline_anchor_then_clip_minus1_plus1",
            "private_evidence_fields": [
                "decisions",
                "history",
                "logs",
                "raw_responses",
                "result_json",
            ],
            "public_projection_fields": list(_PUBLIC_FIELDS),
        },
        "canary_plan": {
            "q7_baseline_replay": {
                "planned_evaluator_transactions": 14,
                "repeat_count": 2,
                "task_count": 7,
            },
            "future_gate_only": True,
            "negative_candidates": {
                "kinds": [
                    "unknown_key",
                    "out_of_range_value",
                    "no_operational_change",
                ],
                "required_disposition": "strict_codec_reject_before_evaluator",
            },
            "total_planned_evaluator_transactions": 14,
        },
        "capability": {
            "blockers": list(_BLOCKERS),
            "execution_ready": False,
            "status": "BLOCKED_CAPABILITY",
        },
        "contract_id": "moss-agenthpobench-qualification-canary-v1",
        "execution_authority": "NOT_GRANTED",
        "execution_entitlement": dict(_ZERO_ENTITLEMENT),
        "qualification_tasks": tasks,
        "schema_version": 1,
        "source_lock": {
            "control_file_sha256": dict(_CONTROL_FILES),
            "git_commit": "6d8d90071cdb16b06f0db866480ecaae48880fba",
            "git_index_sha256": "89164675d5ad2aa1decda95881091bd71d598d5adda688f265e255eed8b24f7c",
            "repository": "https://github.com/OpenMOSS/AgentHPOBench",
            "root_tree": "1acedca0a63252deea57a51878b4ddfd002aa507",
        },
    }


def _load_contract(path: Path) -> dict[str, Any]:
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise AgentHPOQualificationError(
            f"cannot read AgentHPOBench qualification contract: {exc}"
        ) from exc
    try:
        payload = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_reject_duplicates,
            parse_constant=_reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise AgentHPOQualificationError(
            "AgentHPOBench qualification contract is not strict JSON"
        ) from exc
    if not isinstance(payload, dict):
        raise AgentHPOQualificationError("qualification contract must be an object")
    if raw != canonical_agenthpo_qualification_bytes(payload):
        raise AgentHPOQualificationError(
            "AgentHPOBench qualification contract is not canonically encoded"
        )
    return payload


def verify_agenthpo_qualification(
    manifest_path: str | Path = DEFAULT_AGENTHPO_QUALIFICATION_MANIFEST,
    *,
    observed_source_lock: Mapping[str, object] | None = None,
    request_execution: bool = False,
) -> dict[str, Any]:
    """Validate immutable source bindings without granting resources."""

    payload = _load_contract(Path(manifest_path))
    expected = _expected_contract()
    if payload != expected:
        raise AgentHPOQualificationError(
            "AgentHPOBench qualification fields or source bindings differ"
        )
    if observed_source_lock is not None and dict(observed_source_lock) != dict(
        expected["source_lock"]  # type: ignore[arg-type]
    ):
        raise AgentHPOQualificationError("observed source lock drifted")
    if request_execution:
        raise AgentHPOQualificationError(
            "AgentHPOBench contract has no execution authority or entitlement"
        )
    return payload


def verify_agenthpo_source_checkout(
    source_root: str | Path,
    *,
    observed_git_commit: str,
    observed_root_tree: str,
) -> dict[str, object]:
    """Rehash the frozen Q7/control inputs in a clean, explicit checkout."""

    root = Path(source_root)
    if not root.is_absolute():
        raise AgentHPOQualificationError("source root must be absolute")
    if _path_has_symlink(root):
        raise AgentHPOQualificationError("source root may not contain symlinks")
    try:
        resolved = root.resolve(strict=True)
    except OSError as exc:
        raise AgentHPOQualificationError(f"source root does not resolve: {exc}") from exc
    if resolved != root or not resolved.is_dir():
        raise AgentHPOQualificationError("source root is not its explicit real directory")
    expected = _expected_contract()
    lock = expected["source_lock"]
    assert isinstance(lock, dict)
    if observed_git_commit != lock["git_commit"]:
        raise AgentHPOQualificationError("observed source commit drifted")
    if observed_root_tree != lock["root_tree"]:
        raise AgentHPOQualificationError("observed source tree drifted")

    required: dict[str, str] = dict(lock["control_file_sha256"])
    for task in expected["qualification_tasks"]:  # type: ignore[index]
        required.update(task["files"])
    observed: dict[str, str] = {}
    for relative, digest in sorted(required.items()):
        candidate = resolved / relative
        if _path_has_symlink(candidate):
            raise AgentHPOQualificationError(
                f"source input may not contain symlinks: {relative}"
            )
        try:
            actual = candidate.resolve(strict=True)
        except OSError as exc:
            raise AgentHPOQualificationError(
                f"required source input missing: {relative}"
            ) from exc
        if actual != candidate or not actual.is_file():
            raise AgentHPOQualificationError(
                f"source input is not its explicit regular file: {relative}"
            )
        observed_digest = _sha256_regular_file(actual)
        if observed_digest != digest:
            raise AgentHPOQualificationError(f"source input hash drifted: {relative}")
        observed[relative] = observed_digest
    return {
        "file_count": len(observed),
        "git_commit": observed_git_commit,
        "root_tree": observed_root_tree,
        "verified": True,
    }


def _valid_sha256(value: object) -> bool:
    return isinstance(value, str) and len(value) == 64 and not (set(value) - _HEX)


def _path_has_symlink(path: Path) -> bool:
    current = path
    while True:
        try:
            if stat.S_ISLNK(os.lstat(current).st_mode):
                return True
        except OSError as exc:
            raise AgentHPOQualificationError(
                f"cannot inspect path component {current}: {exc}"
            ) from exc
        parent = current.parent
        if parent == current:
            return False
        current = parent


def _sha256_regular_file(path: Path) -> str:
    flags = os.O_RDONLY
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        descriptor = os.open(path, flags)
    except OSError as exc:
        raise AgentHPOQualificationError(f"cannot open file safely: {exc}") from exc
    digest = hashlib.sha256()
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            raise AgentHPOQualificationError("bound path is not a regular file")
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
    finally:
        os.close(descriptor)
    return digest.hexdigest()


def verify_result_artifact(
    result_path: str | Path | None,
    *,
    expected_sha256: str,
    allowed_root: str | Path,
) -> dict[str, object]:
    """Bind one controller-private result JSON by realpath and content hash."""

    if result_path is None or str(result_path).strip() == "":
        raise AgentHPOQualificationError("result path must be explicit")
    path = Path(result_path)
    root = Path(allowed_root)
    if not path.is_absolute() or not root.is_absolute():
        raise AgentHPOQualificationError("result and allowed root must be absolute")
    if path.suffix != ".json":
        raise AgentHPOQualificationError("result must be one JSON file")
    if not _valid_sha256(expected_sha256):
        raise AgentHPOQualificationError("result SHA256 binding is invalid")
    if _path_has_symlink(path) or _path_has_symlink(root):
        raise AgentHPOQualificationError("result path may not contain symlinks")
    try:
        resolved = path.resolve(strict=True)
        resolved_root = root.resolve(strict=True)
    except OSError as exc:
        raise AgentHPOQualificationError(f"result path does not resolve: {exc}") from exc
    if resolved != path or resolved_root != root:
        raise AgentHPOQualificationError("result paths must be explicit realpaths")
    if not (resolved == resolved_root or resolved.is_relative_to(resolved_root)):
        raise AgentHPOQualificationError("result is outside the allowed root")
    observed = _sha256_regular_file(resolved)
    if observed != expected_sha256:
        raise AgentHPOQualificationError("result content hash drifted")
    return {
        "result_realpath": str(resolved),
        "result_sha256": observed,
        "size_bytes": resolved.stat().st_size,
    }


def _strict_single_json_object(raw: bytes) -> dict[str, Any]:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise AgentHPOQualificationError("result is not UTF-8 JSON") from exc
    decoder = json.JSONDecoder(
        object_pairs_hook=_reject_duplicates,
        parse_constant=_reject_constant,
    )
    try:
        payload, end = decoder.raw_decode(text.lstrip())
    except json.JSONDecodeError as exc:
        raise AgentHPOQualificationError("result is not one strict JSON object") from exc
    if text.lstrip()[end:].strip():
        raise AgentHPOQualificationError("result contains data after its JSON object")
    if not isinstance(payload, dict):
        raise AgentHPOQualificationError("result must be a JSON object")
    return payload


def _task_spec(task_id: str) -> Mapping[str, object]:
    try:
        return next(task for task in _Q_TASKS if task["task_id"] == task_id)
    except StopIteration as exc:
        raise AgentHPOQualificationError("task is outside the frozen Q7 slice") from exc


def _finite_number(value: object, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise AgentHPOQualificationError(f"{label} must be numeric")
    numeric = float(value)
    if not math.isfinite(numeric):
        raise AgentHPOQualificationError(f"{label} must be finite")
    return numeric


def _container(payload: Mapping[str, object], keys: Sequence[str]) -> object:
    current: object = payload
    for key in keys:
        if not isinstance(current, Mapping):
            return None
        current = current.get(key)
    return current


def _final_metric(task_id: str, final: Mapping[str, object]) -> float | None:
    direct = final.get("metric_value")
    if not isinstance(direct, bool) and isinstance(direct, (int, float)):
        numeric = float(direct)
        if math.isfinite(numeric):
            return numeric
    containers = (final, final.get("metrics"), final.get("final_metrics"))
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        for key in _METRIC_KEYS[task_id]:
            value = container.get(key)
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                continue
            numeric = float(value)
            if math.isfinite(numeric):
                if key in {"accuracy", "test_accuracy"} and abs(numeric) <= 1.0:
                    numeric *= 100.0
                return numeric
    return None


def adapt_agenthpo_result(
    task_id: str,
    raw_result: bytes | str,
) -> AgentHPOAdapterResult:
    """Project one already-completed strict result through a bounded boundary."""

    spec = _task_spec(task_id)
    raw = raw_result.encode("utf-8") if isinstance(raw_result, str) else raw_result
    payload = _strict_single_json_object(raw)
    reasons: list[str] = []

    history = payload.get("history")
    if history is None:
        history = payload.get("chunk_summaries")
    if not isinstance(history, list) or len(history) != 6:
        reasons.append("trace_contract_invalid")
    decisions = payload.get("decisions")
    if decisions is None:
        decisions = payload.get("decision_history")
    if not isinstance(decisions, list) or len(decisions) != 5:
        reasons.append("decision_contract_invalid")
    raw_responses = payload.get("raw_responses")
    raw_response_count = payload.get("raw_response_count")
    has_embedded_responses = (
        isinstance(raw_responses, list)
        and len(raw_responses) == 5
        and all(isinstance(value, str) and value.strip() for value in raw_responses)
    )
    has_bound_response_count = (
        not isinstance(raw_response_count, bool) and raw_response_count == 5
    )
    if not (has_embedded_responses or has_bound_response_count):
        reasons.append("raw_response_contract_invalid")
    fallbacks = payload.get("fallback_decision_count")
    if isinstance(fallbacks, bool) or fallbacks != 0:
        reasons.append("fallback_decision_present")
    replicate_seed = payload.get("replicate_seed")
    if replicate_seed is None:
        replicate_seed = _container(payload, ("provenance", "replicate_seed"))
    if replicate_seed is None:
        reasons.append("seed_provenance_missing")
    model = next(
        (
            value
            for value in (
                payload.get("model"),
                payload.get("model_id"),
                payload.get("model_name"),
                _container(payload, ("provenance", "model")),
            )
            if isinstance(value, str) and value.strip()
        ),
        None,
    )
    if model is None:
        reasons.append("model_provenance_missing")
    if any(payload.get(key) not in (None, "", False) for key in (
        "error",
        "task_error",
        "execution_error",
        "failure_reason",
    )):
        reasons.append("task_execution_error")

    score = -1.0
    if history and isinstance(history, list) and len(history) == 6:
        final = history[-1]
        if not isinstance(final, dict):
            reasons.append("final_intervention_metric_missing")
        else:
            value = _final_metric(task_id, final)
            if value is None:
                reasons.append("final_intervention_metric_missing")
            else:
                baseline = float(spec["baseline"])
                anchor = float(spec["anchor"])
                denominator = abs(anchor - baseline)
                normalized = (
                    (value - baseline) / denominator
                    if spec["direction"] == "higher"
                    else (baseline - value) / denominator
                )
                score = min(1.0, max(-1.0, normalized))
    reasons = list(dict.fromkeys(reasons))
    public = {
        "bounded_normalized_score": score,
        "validity": "valid" if not reasons else "invalid",
        "coarse_reason_codes": reasons,
    }
    return AgentHPOAdapterResult(
        public_projection=public,
        private_evidence={"result_json": payload},
    )


def verify_future_canary_results(
    *,
    baseline_replay: Mapping[str, Sequence[float]],
    negative_dispositions: Mapping[str, Sequence[str]],
) -> dict[str, object]:
    """Validate future evidence without providing any execution path."""

    task_ids = {str(item["task_id"]) for item in _Q_TASKS}
    if set(baseline_replay) != task_ids:
        raise AgentHPOQualificationError("future replay task set differs from Q7")
    expected_negative = {
        "unknown_key",
        "out_of_range_value",
        "no_operational_change",
    }
    if set(negative_dispositions) != expected_negative:
        raise AgentHPOQualificationError("future negative kinds differ")
    for task in _Q_TASKS:
        task_id = str(task["task_id"])
        values = baseline_replay[task_id]
        if isinstance(values, (str, bytes)) or len(values) != 2:
            raise AgentHPOQualificationError(
                f"future baseline replay for {task_id} must contain two scores"
            )
        observed = [
            _finite_number(value, "future baseline score") for value in values
        ]
        if observed[0] != observed[1]:
            raise AgentHPOQualificationError(
                f"future baseline replay for {task_id} is nondeterministic"
            )
        if not math.isclose(
            observed[0], float(task["baseline"]), rel_tol=0.0, abs_tol=1e-12
        ):
            raise AgentHPOQualificationError(
                f"future baseline replay for {task_id} drifted"
            )
    for kind, dispositions in negative_dispositions.items():
        if isinstance(dispositions, (str, bytes)) or len(dispositions) != 7:
            raise AgentHPOQualificationError(
                f"future negative {kind} must contain seven dispositions"
            )
        if any(value != "strict_codec_reject_before_evaluator" for value in dispositions):
            raise AgentHPOQualificationError(
                f"future negative {kind} did not fail before evaluator"
            )
    return {
        "baseline_evaluator_transactions": 14,
        "negative_evaluator_transactions": 0,
        "passed": True,
        "total_evaluator_transactions": 14,
    }
