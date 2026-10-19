"""Fail-closed static contract for the next cross-benchmark qualification.

This module deliberately does not prepare an environment, download benchmark
data, mint resource entitlement, or import an earlier Moss result.  It only
verifies the immutable source and cluster-level split declaration.  A separate
capability receipt and execution authority are required before any runner may
start.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence


DEFAULT_QUALIFICATION_MANIFEST = (
    Path(__file__).with_name("data") / "benchmark_qualification_v1.json"
)

_SHA256 = set("0123456789abcdef")
_TOP_FIELDS = {
    "benchmarks",
    "contract_id",
    "execution_authority",
    "execution_entitlement",
    "history_boundary",
    "schema_version",
}
_BENCHMARK_FIELDS = {
    "benchmark_id",
    "capability",
    "entitlement",
    "evaluator_mode",
    "selection",
    "source",
}
_CAPABILITY_FIELDS = {"blockers", "execution_ready", "status"}
_ENTITLEMENT_FIELDS = {
    "cpu_evaluator_seconds",
    "evaluator_transactions",
    "gpu_exclusive_seconds",
    "model_calls",
}
_HISTORY_FIELDS = {
    "experience_bank_initial_state",
    "forbidden_phase_ids",
    "prior_result_import",
    "prior_result_references",
}
_SELECTION_FIELDS = {
    "algorithm",
    "category_source",
    "cluster_level",
    "salt",
    "selector_digest",
    "split_order",
    "split_sizes",
    "splits",
}
_SOURCE_FIELDS = {"dataset_revision", "git_commit", "repository", "source_kind"}
_SPLIT_NAMES = ("Q_qual", "D_bank", "T_fresh", "T_final")
_ZERO_ENTITLEMENT = {
    "cpu_evaluator_seconds": 0,
    "evaluator_transactions": 0,
    "gpu_exclusive_seconds": 0,
    "model_calls": 0,
}
_FORBIDDEN_PHASE_IDS = (
    "hb-three-arm-live-v1r8",
    "hb-three-arm-live-v1r9",
)

_AGENTHPO_UNITS = (
    "llm_c_fineweb10b",
    "torch_conv_kan_cifar10",
    "open_r1_math500",
    "agent_lightning_room_selector",
    "uni2ts_lsf_etth1",
    "timesfm_etth1_long_horizon",
    "modernbert_mnli_accuracy",
    "cifar10_airbench94",
    "noisygl_cora_uniform30_gcn",
    "tabmini_molecular_biology_promoters_auc",
    "binary_diffusion_adult_rf",
    "xlstm_parity",
    "vbll_yacht_rmse",
    "tabm_california_rmse",
    "timexer_pjm_168_24_mse",
    "ablkit_hwf_reasoning_accuracy",
    "tunedgnn_cora_gcn_accuracy",
    "verl_grpo_gsm8k",
    "forest_diffusion_iris_f1fake",
    "var_imagenet256",
    "align_anything_ragen_bandit",
    "chronos_t5_tiny_monash_weather_wql",
    "hyperboliccv_cifar100_accuracy",
    "itransformer_ettm2_96_mse",
    "timemixer_ettm2_96_mse",
    "art_2048_win_rate",
    "open_r1_multimodal_mathvista_accuracy",
    "rankup_utkface_mae",
    "sparsetsf_ettm1_96_mse",
    "simple_rl_reason_qwen25_05b_math500",
)
_AGENTHPO_CATEGORIES: dict[str, tuple[str, ...]] = {
    "NLP": (
        "llm_c_fineweb10b",
        "modernbert_mnli_accuracy",
        "xlstm_parity",
    ),
    "CV": (
        "torch_conv_kan_cifar10",
        "cifar10_airbench94",
        "var_imagenet256",
        "hyperboliccv_cifar100_accuracy",
        "rankup_utkface_mae",
    ),
    "TS": (
        "uni2ts_lsf_etth1",
        "timesfm_etth1_long_horizon",
        "timexer_pjm_168_24_mse",
        "chronos_t5_tiny_monash_weather_wql",
        "itransformer_ettm2_96_mse",
        "timemixer_ettm2_96_mse",
        "sparsetsf_ettm1_96_mse",
    ),
    "Graph": (
        "noisygl_cora_uniform30_gcn",
        "tunedgnn_cora_gcn_accuracy",
    ),
    "RL": (
        "agent_lightning_room_selector",
        "align_anything_ragen_bandit",
        "art_2048_win_rate",
    ),
    "LLM": (
        "open_r1_math500",
        "verl_grpo_gsm8k",
        "open_r1_multimodal_mathvista_accuracy",
        "simple_rl_reason_qwen25_05b_math500",
    ),
    "SL": (
        "tabmini_molecular_biology_promoters_auc",
        "binary_diffusion_adult_rf",
        "vbll_yacht_rmse",
        "tabm_california_rmse",
        "ablkit_hwf_reasoning_accuracy",
        "forest_diffusion_iris_f1fake",
    ),
}
_AGENTHPO_CATEGORY_SOURCE = {
    "path": "configs/scoring_reference.tsv",
    "sha256": "c17ad42d27aee047611ab824446dae539724d09b61bf9fa945932bfb17201308",
}
_GDPEVO_UNITS = tuple(f"task_group_{index:03d}" for index in range(1, 25))

_EXPECTED_BENCHMARKS: dict[str, dict[str, Any]] = {
    "agenthpobench": {
        "source": {
            "dataset_revision": None,
            "git_commit": "6d8d90071cdb16b06f0db866480ecaae48880fba",
            "repository": "https://github.com/OpenMOSS/AgentHPOBench",
            "source_kind": "git",
        },
        "evaluator_mode": "no_gold",
        "capability_status": "BLOCKED_CAPABILITY",
        "blockers": [
            "agenthpobench_environment_canary_pending",
            "agenthpobench_evaluator_canary_pending",
            "agenthpobench_reference_negative_canaries_pending",
        ],
        "salt": "moss-benchmark-qualification-v1:agenthpobench",
        "algorithm": "category_stratified_sha256_q7_then_lexicographic_v1",
        "category_source": _AGENTHPO_CATEGORY_SOURCE,
        "categories": _AGENTHPO_CATEGORIES,
        "cluster_level": "repository_task",
        "split_order": ["Q_qual", "D_bank", "T_fresh"],
        "split_sizes": {"Q_qual": 7, "D_bank": 11, "T_fresh": 12, "T_final": 0},
        "units": _AGENTHPO_UNITS,
    },
    "gdpevo": {
        "source": {
            "dataset_revision": None,
            "git_commit": "0999c0d1e6f59b1cb8464cac4e5ed856b5dcb9e4",
            "repository": "https://github.com/Prism-Shadow/GDPevo",
            "source_kind": "git",
        },
        "evaluator_mode": "public_evaluator_gold_model_isolated",
        "capability_status": "BLOCKED_CAPABILITY",
        "blockers": [
            "gdpevo_evaluator_isolation_canary_pending",
            "gdpevo_reference_negative_canaries_pending",
        ],
        "salt": "moss-benchmark-qualification-v1:gdpevo",
        "algorithm": "sha256_lexicographic_v1",
        "category_source": None,
        "cluster_level": "task_group",
        "split_order": ["Q_qual", "D_bank", "T_fresh", "T_final"],
        "split_sizes": {"Q_qual": 6, "D_bank": 6, "T_fresh": 6, "T_final": 6},
        "units": _GDPEVO_UNITS,
    },
    "bird-interact": {
        "source": {
            "dataset_revision": "f7881a9c2b9630cc4fc13b0c39279740b0a2fd87",
            "git_commit": "451fe2c3518ee1cf908d8139e2913483bd519381",
            "repository": "https://github.com/bird-bench/BIRD-Interact",
            "source_kind": "git_plus_huggingface_private_bundle",
        },
        "evaluator_mode": "private_bundle_required",
        "capability_status": "BLOCKED_PRIVATE_BUNDLE",
        "blockers": ["bird_interact_private_bundle_unavailable"],
        "salt": "moss-benchmark-qualification-v1:bird-interact",
        "algorithm": "sha256_lexicographic_v1",
        "category_source": None,
        "cluster_level": "database",
        "split_order": ["Q_qual", "D_bank", "T_fresh", "T_final"],
        "split_sizes": {"Q_qual": 0, "D_bank": 0, "T_fresh": 0, "T_final": 0},
        "units": (),
    },
}


class QualificationContractError(ValueError):
    """The static qualification declaration is not safe to consume."""


def _reject_json_constant(value: str) -> None:
    raise QualificationContractError(f"qualification JSON contains {value}")


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise QualificationContractError(
                f"qualification JSON repeats field {key!r}"
            )
        value[key] = item
    return value


def canonical_qualification_bytes(payload: object) -> bytes:
    """Return the sole accepted serialization for this contract."""

    try:
        return (
            json.dumps(
                payload,
                allow_nan=False,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            )
            + "\n"
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise QualificationContractError(
            "qualification payload is not canonical JSON"
        ) from exc


def selector_digest(selection: Mapping[str, Any]) -> str:
    """Bind the selector inputs, universe, and complete split assignment."""

    projection = dict(selection)
    projection.pop("selector_digest", None)
    return hashlib.sha256(canonical_qualification_bytes(projection)).hexdigest()


def _exact_object(value: object, fields: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != fields:
        raise QualificationContractError(f"{label} schema differs")
    return value


def _exact_string_list(value: object, label: str) -> list[str]:
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item for item in value
    ):
        raise QualificationContractError(f"{label} must be a string list")
    return value


def _verify_entitlement(value: object, label: str) -> dict[str, int]:
    entitlement = _exact_object(value, _ENTITLEMENT_FIELDS, label)
    if any(type(item) is not int or item < 0 for item in entitlement.values()):
        raise QualificationContractError(
            f"{label} values must be non-negative integers"
        )
    return entitlement  # type: ignore[return-value]


def _derived_splits(
    units: Sequence[str],
    *,
    salt: str,
    split_order: Sequence[str],
    split_sizes: Mapping[str, int],
) -> dict[str, list[str]]:
    ordered = sorted(
        units,
        key=lambda unit_id: (
            hashlib.sha256(f"{salt}\0{unit_id}".encode("utf-8")).hexdigest(),
            unit_id,
        ),
    )
    cursor = 0
    result = {name: [] for name in _SPLIT_NAMES}
    for name in split_order:
        size = split_sizes[name]
        result[name] = ordered[cursor : cursor + size]
        cursor += size
    if cursor != len(ordered):
        raise QualificationContractError("selector sizes do not consume the universe")
    return result


def _derived_agenthpo_splits(
    units: Sequence[str],
    *,
    salt: str,
    split_sizes: Mapping[str, int],
    categories: Mapping[str, Sequence[str]],
) -> dict[str, list[str]]:
    def key(unit_id: str) -> tuple[str, str]:
        return (
            hashlib.sha256(f"{salt}\0{unit_id}".encode("utf-8")).hexdigest(),
            unit_id,
        )

    category_order = ("NLP", "CV", "TS", "Graph", "RL", "LLM", "SL")
    if tuple(categories) != category_order:
        raise QualificationContractError("AgentHPO category order differs")
    flattened = [unit for category in category_order for unit in categories[category]]
    if set(flattened) != set(units) or len(flattened) != len(units):
        raise QualificationContractError("AgentHPO categories do not partition tasks")
    q_qual = [min(categories[category], key=key) for category in category_order]
    remaining = sorted(set(units) - set(q_qual), key=key)
    d_size = split_sizes["D_bank"]
    return {
        "Q_qual": q_qual,
        "D_bank": remaining[:d_size],
        "T_fresh": remaining[d_size:],
        "T_final": [],
    }


def _verify_selection(
    value: object, *, benchmark_id: str, expected: Mapping[str, Any]
) -> None:
    selection = _exact_object(
        value, _SELECTION_FIELDS, f"{benchmark_id} selection"
    )
    if selection["algorithm"] != expected["algorithm"]:
        raise QualificationContractError(f"{benchmark_id} selector algorithm differs")
    if selection["category_source"] != expected["category_source"]:
        raise QualificationContractError(
            f"{benchmark_id} selector category source differs"
        )
    if selection["cluster_level"] != expected["cluster_level"]:
        raise QualificationContractError(
            f"{benchmark_id} selector cluster level differs"
        )
    if selection["salt"] != expected["salt"]:
        raise QualificationContractError(f"{benchmark_id} selector salt differs")
    split_order = _exact_string_list(
        selection["split_order"], f"{benchmark_id} split order"
    )
    if split_order != expected["split_order"] or len(set(split_order)) != len(
        split_order
    ):
        raise QualificationContractError(f"{benchmark_id} split order differs")

    sizes = _exact_object(
        selection["split_sizes"], set(_SPLIT_NAMES), f"{benchmark_id} split sizes"
    )
    if any(type(size) is not int or size < 0 for size in sizes.values()):
        raise QualificationContractError(f"{benchmark_id} split sizes are invalid")
    if sizes != expected["split_sizes"]:
        raise QualificationContractError(f"{benchmark_id} split sizes differ")

    splits = _exact_object(
        selection["splits"], set(_SPLIT_NAMES), f"{benchmark_id} splits"
    )
    observed_assignment: dict[str, list[str]] = {}
    unit_ids = list(expected["units"])
    assigned_units: list[str] = []
    assigned_clusters: set[str] = set()
    for name in _SPLIT_NAMES:
        members = _exact_string_list(
            splits[name], f"{benchmark_id} split {name}"
        )
        if len(members) != sizes[name] or len(set(members)) != len(members):
            raise QualificationContractError(f"{benchmark_id} split {name} differs")
        for unit_id in members:
            if unit_id not in unit_ids:
                raise QualificationContractError(
                    f"{benchmark_id} split {name} contains an unknown unit"
                )
            if unit_id in assigned_clusters:
                raise QualificationContractError(
                    f"{benchmark_id} cluster crosses qualification boundaries"
                )
            assigned_clusters.add(unit_id)
        assigned_units.extend(members)
        observed_assignment[name] = members
    if set(assigned_units) != set(unit_ids) or len(assigned_units) != len(unit_ids):
        raise QualificationContractError(
            f"{benchmark_id} splits do not partition the universe"
        )
    expected_assignment = (
        _derived_agenthpo_splits(
            unit_ids,
            salt=expected["salt"],
            split_sizes=sizes,
            categories=expected["categories"],
        )
        if benchmark_id == "agenthpobench"
        else _derived_splits(
            unit_ids,
            salt=expected["salt"],
            split_order=split_order,
            split_sizes=sizes,
        )
    )
    if observed_assignment != expected_assignment:
        raise QualificationContractError(
            f"{benchmark_id} split assignment differs from the selector"
        )
    digest = selection["selector_digest"]
    if (
        not isinstance(digest, str)
        or len(digest) != 64
        or any(character not in _SHA256 for character in digest)
        or digest != selector_digest(selection)
    ):
        raise QualificationContractError(f"{benchmark_id} selector digest differs")


def _load_canonical(path: Path) -> dict[str, Any]:
    resolved = path.resolve(strict=True)
    if resolved.is_symlink() or not resolved.is_file():
        raise QualificationContractError(
            "qualification manifest must be a regular file"
        )
    raw = resolved.read_bytes()
    try:
        payload = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_json_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise QualificationContractError(
            "qualification manifest is invalid JSON"
        ) from exc
    if not isinstance(payload, dict) or canonical_qualification_bytes(payload) != raw:
        raise QualificationContractError("qualification manifest is not canonical")
    return payload


def verify_benchmark_qualification(
    manifest_path: Path = DEFAULT_QUALIFICATION_MANIFEST,
    *,
    request_execution: bool | Sequence[str] = False,
    observed_source_pins: Mapping[str, Mapping[str, Any]] | None = None,
    prior_result_references: Sequence[str | Path] = (),
) -> dict[str, Any]:
    """Verify the frozen selection without granting or performing execution.

    ``request_execution`` exists to make the authority boundary mechanical.  It
    fails for the checked-in v1 contract because all capability states are
    blocked and every entitlement is zero.
    """

    if prior_result_references:
        raise QualificationContractError(
            "prior Moss results may not enter the fresh qualification"
        )
    payload = _load_canonical(manifest_path)
    _exact_object(payload, _TOP_FIELDS, "qualification manifest")
    if payload["schema_version"] != 1 or type(payload["schema_version"]) is not int:
        raise QualificationContractError("qualification schema version differs")
    if payload["contract_id"] != "moss-cross-benchmark-qualification-v1":
        raise QualificationContractError("qualification contract id differs")
    if payload["execution_authority"] != "NOT_GRANTED":
        raise QualificationContractError("qualification execution authority differs")
    if (
        _verify_entitlement(payload["execution_entitlement"], "global entitlement")
        != _ZERO_ENTITLEMENT
    ):
        raise QualificationContractError("qualification must start with zero entitlement")

    history = _exact_object(
        payload["history_boundary"], _HISTORY_FIELDS, "history boundary"
    )
    if (
        history["experience_bank_initial_state"] != "EMPTY"
        or history["prior_result_import"] != "FORBIDDEN"
        or history["prior_result_references"] != []
        or history["forbidden_phase_ids"] != list(_FORBIDDEN_PHASE_IDS)
    ):
        raise QualificationContractError("historical result boundary differs")

    raw_benchmarks = payload["benchmarks"]
    if not isinstance(raw_benchmarks, list):
        raise QualificationContractError("benchmarks must be a list")
    benchmark_by_id: dict[str, dict[str, Any]] = {}
    for index, raw_benchmark in enumerate(raw_benchmarks):
        benchmark = _exact_object(
            raw_benchmark, _BENCHMARK_FIELDS, f"benchmark {index}"
        )
        benchmark_id = benchmark["benchmark_id"]
        if not isinstance(benchmark_id, str) or benchmark_id in benchmark_by_id:
            raise QualificationContractError("benchmark ids must be unique strings")
        benchmark_by_id[benchmark_id] = benchmark
    if set(benchmark_by_id) != set(_EXPECTED_BENCHMARKS):
        raise QualificationContractError("qualification benchmark set differs")
    if [item["benchmark_id"] for item in raw_benchmarks] != sorted(
        _EXPECTED_BENCHMARKS
    ):
        raise QualificationContractError("qualification benchmark order differs")

    entitlement_total = {field: 0 for field in _ENTITLEMENT_FIELDS}
    for benchmark_id, expected in _EXPECTED_BENCHMARKS.items():
        benchmark = benchmark_by_id[benchmark_id]
        source = _exact_object(
            benchmark["source"], _SOURCE_FIELDS, f"{benchmark_id} source"
        )
        if source != expected["source"]:
            raise QualificationContractError(f"{benchmark_id} source pin differs")
        if benchmark["evaluator_mode"] != expected["evaluator_mode"]:
            raise QualificationContractError(f"{benchmark_id} evaluator mode differs")
        capability = _exact_object(
            benchmark["capability"], _CAPABILITY_FIELDS, f"{benchmark_id} capability"
        )
        blockers = _exact_string_list(
            capability["blockers"], f"{benchmark_id} capability blockers"
        )
        if (
            capability["status"] != expected["capability_status"]
            or capability["execution_ready"] is not False
            or blockers != expected["blockers"]
        ):
            raise QualificationContractError(f"{benchmark_id} capability differs")
        entitlement = _verify_entitlement(
            benchmark["entitlement"], f"{benchmark_id} entitlement"
        )
        if entitlement != _ZERO_ENTITLEMENT:
            raise QualificationContractError(
                f"{benchmark_id} blocked capability must have zero entitlement"
            )
        for field in _ENTITLEMENT_FIELDS:
            entitlement_total[field] += entitlement[field]
        _verify_selection(
            benchmark["selection"], benchmark_id=benchmark_id, expected=expected
        )
    if entitlement_total != payload["execution_entitlement"]:
        raise QualificationContractError("global entitlement arithmetic differs")

    if observed_source_pins is not None:
        if set(observed_source_pins) != set(_EXPECTED_BENCHMARKS):
            raise QualificationContractError("observed source benchmark set differs")
        for benchmark_id, benchmark in benchmark_by_id.items():
            observed = observed_source_pins[benchmark_id]
            expected_pin = {
                "dataset_revision": benchmark["source"]["dataset_revision"],
                "git_commit": benchmark["source"]["git_commit"],
            }
            if not isinstance(observed, Mapping) or dict(observed) != expected_pin:
                raise QualificationContractError(
                    f"{benchmark_id} observed source drifted"
                )

    if request_execution is True:
        requested = set(benchmark_by_id)
    elif request_execution is False:
        requested = set()
    elif isinstance(request_execution, Sequence) and not isinstance(
        request_execution, (str, bytes)
    ):
        requested = set(request_execution)
        if not requested or not requested <= set(benchmark_by_id):
            raise QualificationContractError("execution request benchmark set is invalid")
    else:
        raise QualificationContractError(
            "execution request must be boolean or benchmark ids"
        )
    if requested:
        if payload["execution_authority"] != "GRANTED":
            raise QualificationContractError("qualification has no execution authority")
        for benchmark_id in requested:
            benchmark = benchmark_by_id[benchmark_id]
            capability = benchmark["capability"]
            if (
                capability["status"] != "READY"
                or capability["execution_ready"] is not True
            ):
                raise QualificationContractError(
                    f"{benchmark_id} capability is not ready for execution"
                )
            if sum(benchmark["entitlement"].values()) <= 0:
                raise QualificationContractError(
                    f"{benchmark_id} has no execution entitlement"
                )

    return payload


__all__ = [
    "DEFAULT_QUALIFICATION_MANIFEST",
    "QualificationContractError",
    "canonical_qualification_bytes",
    "selector_digest",
    "verify_benchmark_qualification",
]
