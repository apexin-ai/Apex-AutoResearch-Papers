"""Static, fail-closed contract for the wide-Harness factorial experiments.

The checked-in contract describes planned logical work, not execution
entitlement.  It binds the qualification split by content hash, freezes the
four main arms and three isolated B-online state mechanisms, and mechanically
checks all published call-count arithmetic.  This module never invokes a
model, evaluator, benchmark environment, or resource allocator.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from optimization_lab.harness_builder.factorial_policies import (
    ARM_IDS,
    ARM_POLICY_SPECS,
)
from optimization_lab.harness_builder.qualification import (
    DEFAULT_QUALIFICATION_MANIFEST,
    verify_benchmark_qualification,
)
from optimization_lab.harness_builder.factorial_score import score_contract_for


DEFAULT_FACTORIAL_MANIFEST = (
    Path(__file__).with_name("data") / "wide_meta_factorial_v1.json"
)

_QUALIFICATION_SHA256 = (
    "ba415a2466e7b5e1b5e4b43f50f59dbb13cd7ff93d20bc616f71e658d5e7bafd"
)
_ZERO_ENTITLEMENT = {
    "cpu_evaluator_seconds": 0,
    "evaluator_transactions": 0,
    "gpu_exclusive_seconds": 0,
    "model_calls": 0,
}
_AXES = (
    "role_graph",
    "memory_views",
    "tools",
    "parent_strategy",
    "workflow",
    "scheduler_mode",
    "recovery_mode",
)
_MAIN_SEEDS = (2026081201, 2026081202, 2026081203)
_ONLINE_SEEDS = _MAIN_SEEDS[:2]
_FORBIDDEN_PHASE_IDS = (
    "hb-three-arm-live-v1r8",
    "hb-three-arm-live-v1r9",
)

_AGENTHPO_T12 = (
    "hyperboliccv_cifar100_accuracy",
    "agent_lightning_room_selector",
    "llm_c_fineweb10b",
    "tunedgnn_cora_gcn_accuracy",
    "verl_grpo_gsm8k",
    "uni2ts_lsf_etth1",
    "xlstm_parity",
    "ablkit_hwf_reasoning_accuracy",
    "rankup_utkface_mae",
    "binary_diffusion_adult_rf",
    "timexer_pjm_168_24_mse",
    "open_r1_multimodal_mathvista_accuracy",
)
_AGENTHPO_D4 = (
    "timesfm_etth1_long_horizon",
    "align_anything_ragen_bandit",
    "tabm_california_rmse",
    "forest_diffusion_iris_f1fake",
)
_GDPEVO_T6 = (
    "task_group_003",
    "task_group_023",
    "task_group_005",
    "task_group_018",
    "task_group_012",
    "task_group_017",
)


class FactorialContractError(ValueError):
    """The experiment-factor declaration is unsafe or internally inconsistent."""


def _reject_json_constant(value: str) -> None:
    raise FactorialContractError(f"factorial JSON contains {value}")


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise FactorialContractError(f"factorial JSON repeats field {key!r}")
        value[key] = item
    return value


def canonical_factorial_bytes(payload: object) -> bytes:
    """Return the only accepted byte serialization of a factorial contract."""

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
        raise FactorialContractError("factorial payload is not canonical JSON") from exc


def factorial_contract_digest(payload: Mapping[str, Any]) -> str:
    """Hash every contract field except the digest field itself."""

    projection = dict(payload)
    projection.pop("contract_digest", None)
    return hashlib.sha256(canonical_factorial_bytes(projection)).hexdigest()


def _factorial_projection_sha256(payload: object) -> str:
    return hashlib.sha256(canonical_factorial_bytes(payload)).hexdigest()


def _arm(
    arm_id: str,
    arm_update_policy: str,
    runtime_adaptation_policy: str,
    *,
    architecture_axes: str,
    fresh: bool,
    minimum_changes: int,
    fingerprint_unique: bool,
    text_skill_state: str,
) -> dict[str, Any]:
    return {
        "arm_update_policy": arm_update_policy,
        "arm_update_policy_status": (
            "TYPED_VALIDATION_READY_FORMAL_DISPATCH_NOT_READY"
        ),
        "architecture_axes": architecture_axes,
        "arm_id": arm_id,
        "cross_task_state": "NONE",
        "fresh_component_instances_after_v001": fresh,
        "lineage_fingerprint_unique": fingerprint_unique,
        "minimum_material_axis_changes_after_v001": minimum_changes,
        "runtime_adaptation_policy": runtime_adaptation_policy,
        "runtime_adaptation_policy_namespace": "BUILDER_VARIANT",
        "solver_native_feedback": True,
        "text_skill_state": text_skill_state,
    }


def _expected_projection() -> dict[str, Any]:
    main_benchmarks = [
        {
            "benchmark_id": "agenthpobench",
            "logical_budget": {
                "evaluator_transactions": 756,
                "logical_model_calls": 1332,
            },
            "rounds": 6,
            "seed_count": 3,
            "seeds": list(_MAIN_SEEDS),
            "selection_split": "T_fresh",
            "task_count": 12,
            "task_partition": "repository_task",
            "task_units": list(_AGENTHPO_T12),
            "tasks_per_unit": 1,
        },
        {
            "benchmark_id": "gdpevo",
            "logical_budget": {
                "evaluator_transactions": 810,
                "logical_model_calls": 1440,
            },
            "rounds": 3,
            "seed_count": 3,
            "seeds": list(_MAIN_SEEDS),
            "selection_split": "T_fresh",
            "task_count": 30,
            "task_partition": "official_test_tasks_1_through_5",
            "task_units": list(_GDPEVO_T6),
            "tasks_per_unit": 5,
        },
    ]
    online_benchmarks = [
        {
            "benchmark_id": "agenthpobench",
            "heldout": {
                "rounds": 6,
                "selection_split": "T_fresh",
                "task_count": 8,
                "task_partition": "repository_task",
                "task_units": list(_AGENTHPO_T12[:8]),
                "tasks_per_unit": 1,
            },
            "source": {
                "rounds": 6,
                "selection_split": "D_bank",
                "task_count": 4,
                "task_partition": "repository_task",
                "task_units": list(_AGENTHPO_D4),
                "tasks_per_unit": 1,
            },
        },
        {
            "benchmark_id": "gdpevo",
            "heldout": {
                "rounds": 3,
                "selection_split": "T_fresh",
                "task_count": 10,
                "task_partition": "official_test_tasks_1_through_5",
                "task_units": list(_GDPEVO_T6[:2]),
                "tasks_per_unit": 5,
            },
            "source": {
                "rounds": 3,
                "selection_split": "T_fresh",
                "task_count": 10,
                "task_partition": "official_train_tasks_1_through_5",
                "task_units": list(_GDPEVO_T6[:2]),
                "tasks_per_unit": 5,
            },
        },
    ]
    return {
        "contract_id": "moss-wide-meta-factorial-v1",
        "execution_authority": "NOT_GRANTED",
        "execution_entitlement": dict(_ZERO_ENTITLEMENT),
        "implementation_status": {
            "formal_executor": "NOT_READY",
            "formal_executor_entrypoint": "NONE",
            "formal_arm_update_policy_dispatch": "NOT_READY",
            "known_missing_bindings": [
                "FOUR_ARM_FORMAL_PROVIDER_ORCHESTRATOR",
                "POST_V001_NATIVE_CONTEXT_AND_TRUSTED_COMPILE_DISPATCH",
                "TASK_LOCAL_SKILL_FORMAL_DISPATCH",
                (
                    "SCORE_BOUNDARY_OPERATION_LEDGER_PROVIDER_EVALUATOR_"
                    "OPTIMIZER_AND_REPORT_DISPATCH"
                ),
                "AGENTHPO_FREE_FORM_CODEC_OR_FRESH_SPLIT",
                "AGENTHPO_TRUSTED_TRANSPORT_LEDGER_AND_FORMAL_DISPATCH",
                "BENCHMARK_PROVIDER_AND_BUDGET_AUTHORITY",
                "BENCHMARK_CANARY_EXECUTION_AND_FORMAL_TASK_SMOKE",
                "ONLINE_TASK_AUTHORITY_PROVIDER_AND_STAGE_GATE_DISPATCH",
            ],
            "arm_update_policy_validation": "READY",
            "canary_readiness": (
                "EXACT_ZERO_CALL_SCHEDULE_READY_"
                "ENVIRONMENT_EXECUTION_NOT_READY"
            ),
            "exact_attempt_coverage": (
                "EXACT_1566_SLOT_SET_READY_"
                "OPERATION_LEDGER_COVERAGE_NOT_READY"
            ),
            "online_pilot_zero_call_plan": (
                "EXACT_732_ATTEMPT_84_UPDATE_PLAN_READY_"
                "ONLINE_TASK_AUTHORITY_NOT_READY"
            ),
            "score_boundary_artifact_validation": "READY",
            "score_boundary_formal_binding": (
                "EXACT_1566_SLOT_SET_AND_ITT_ARTIFACT_READY_"
                "OPERATION_LEDGER_PROVIDER_EVALUATOR_OPTIMIZER_"
                "AND_REPORT_DISPATCH_NOT_READY"
            ),
            "shared_v001_schema_and_archive": (
                "SOURCE_BOUND_TRUSTED_V001_RECOMPILATION_READY_"
                "NO_EXECUTION_AUTHORITY"
            ),
            "static_contract_validation": "READY",
            "task_seed_barrier_and_recovery": (
                "EXACT_SOURCE_AUTHORITY_BUNDLE_PLAN_BARRIER_AND_"
                "V001_CONTEXT_DISPATCH_READY_"
                "POST_V001_CONTEXT_DISPATCH_NOT_READY"
            ),
            "task_local_skill_artifact_validation": "READY",
            "task_local_skill_formal_dispatch": "NOT_READY",
            "runtime_adaptation_policy_validation": "READY",
            "zero_authority_precheck_controller": (
                "FIXTURE_AND_EXACT_MATRIX_BARRIERS_READY_"
                "NO_EXECUTION_AUTHORITY"
            ),
        },
        "harness_axes": list(_AXES),
        "history_boundary": {
            "experience_bank_initial_state": "EMPTY",
            "forbidden_phase_ids": list(_FORBIDDEN_PHASE_IDS),
            "prior_result_import": "FORBIDDEN",
            "prior_result_references": [],
        },
        "main_experiment": {
            "arms": [
                _arm(
                    "A-fixed-feedback",
                    "fixed_feedback_v1",
                    "conditional_any_v1",
                    architecture_axes="FROZEN",
                    fresh=False,
                    minimum_changes=0,
                    fingerprint_unique=False,
                    text_skill_state="NONE",
                ),
                _arm(
                    "S-reflection-skill",
                    "reflection_skill_only_v1",
                    "conditional_any_v1",
                    architecture_axes="FROZEN",
                    fresh=False,
                    minimum_changes=0,
                    fingerprint_unique=False,
                    text_skill_state="TASK_LOCAL_RESET_AFTER_TASK",
                ),
                _arm(
                    "B-targeted",
                    "targeted_any_change_v1",
                    "targeted_any_change_v1",
                    architecture_axes="MUTABLE",
                    fresh=True,
                    minimum_changes=1,
                    fingerprint_unique=False,
                    text_skill_state="NONE",
                ),
                _arm(
                    "B-frozen-wide",
                    "wide_all_fields_recompile_v1",
                    "wide_all_fields_recompile_v1",
                    architecture_axes="MUTABLE",
                    fresh=True,
                    minimum_changes=7,
                    fingerprint_unique=True,
                    text_skill_state="NONE",
                ),
            ],
            "benchmarks": main_benchmarks,
            "logical_budget": {
                "evaluator_transactions": 1566,
                "logical_model_calls": 2772,
            },
            "logical_budget_accounting": {
                "post_v001_per_task_seed_round": {
                    "A-fixed-feedback": {
                        "arm_update_model_calls": 0,
                        "arm_update_operation": "NONE_NO_SHAM_CALL",
                        "evaluator_transactions": 1,
                        "solution_model_calls": 1,
                    },
                    "B-frozen-wide": {
                        "arm_update_model_calls": 1,
                        "arm_update_operation": "HARNESS_BUILDER_UPDATE",
                        "evaluator_transactions": 1,
                        "solution_model_calls": 1,
                    },
                    "B-targeted": {
                        "arm_update_model_calls": 1,
                        "arm_update_operation": "HARNESS_BUILDER_UPDATE",
                        "evaluator_transactions": 1,
                        "solution_model_calls": 1,
                    },
                    "S-reflection-skill": {
                        "arm_update_model_calls": 1,
                        "arm_update_operation": "REFLECTION_SKILL_UPDATE",
                        "evaluator_transactions": 1,
                        "solution_model_calls": 1,
                    },
                },
                "shared_v001_per_task_seed": {
                    "evaluator_transactions": 1,
                    "harness_builder_model_calls": 1,
                    "solution_model_calls": 1,
                },
            },
            "primary_outcome": "post_v001_itt_native_raw_auc_by_benchmark",
            "score_boundary": {
                "artifact_validation": "TYPED_READY",
                "contract_sha256s": {
                    "agenthpobench": (
                        "18ef58786d5390819694065e521cdf2093db4d3938aa2895486dace8c24f96c3"
                    ),
                    "gdpevo": (
                        "9534a00c33dcbe17fe8c67e81393ebe793fcef6fd96d62901a8e8f3bd9cea782"
                    ),
                },
                "formal_binding": (
                    "EXACT_ITT_ARTIFACT_READY_"
                    "RESERVATION_EVALUATOR_OPTIMIZER_"
                    "AND_REPORT_DISPATCH_NOT_READY"
                ),
                "invalid_itt_floor_policy": (
                    "BENCHMARK_NATIVE_RAW_MINIMUM_BOUND"
                ),
                "invalid_itt_scope": (
                    "TYPED_INVALID_SCORE_RECEIPT_"
                    "ALL_RESERVED_ATTEMPT_COVERAGE_NOT_READY"
                ),
                "itt_policy_schema": "factorial_itt_policy_v1",
                "itt_reporting_metric": "ITT_NATIVE_RAW_SCORE_ONLY",
                "optimization_utility_scope": "AFFINE_POSITIVE_INTERNAL_ONLY",
                "reporting_metric": "RAW_SCORE_ONLY",
            },
            "shared_v001": {
                "arm_specific_v001_execution": "NONE",
                "arm_specific_compile_receipts_identical": False,
                "arm_specific_receipt_binding": (
                    "REFERENCE_TRUNK_SHA256_AND_BIND_ARM_ID"
                ),
                "arms_fork_after_feedback": True,
                "counting": "ONCE_PER_TASK_SEED",
                "semantic_identity_fields": [
                    "task_seed_key_sha256",
                    "context_binding_sha256",
                    "decision_sha256",
                    "compiled_harness_semantic_sha256",
                    "solution_prompt_sha256",
                    "solution_artifact_sha256",
                    "attempt_artifact_sha256",
                    "evaluation_artifact_sha256",
                ],
                "semantic_identity_required": True,
                "trunk_decision_shared_by_reference": True,
                "trunk_solver_artifact_shared_by_reference": True,
                "trunk_receipt_implementation_status": (
                    "TYPED_AUDIT_REPLAY_AND_TRUSTED_SOURCE_BOUND_"
                    "RECOMPILATION_READY_NO_EXECUTION_AUTHORITY"
                ),
                "trunk_receipt_addressing": "CONTENT_SHA256",
                "trunk_receipt_scope": "ARM_INDEPENDENT_TASK_SEED_V001",
            },
            "task_local_skill": {
                "architecture_axes": "FROZEN_V001",
                "arm_id": "S-reflection-skill",
                "artifact_schema": "task_local_reflection_skill_v1",
                "cross_task_reads": "FORBIDDEN",
                "formal_dispatch": "NOT_READY",
                "solver_projection_fields": [
                    "diagnosis",
                    "preserve",
                    "avoid",
                    "next_actions",
                ],
                "state_scope": "TASK_SEED_ONLY_RESET_AFTER_TASK",
                "typed_artifact_validation": "READY",
                "updates_after_v001": "ONE_PER_NEXT_ROUND",
            },
            "statistics": {
                "benchmark_scores_mixed": False,
                "gdpevo_cluster_unit": "task_group",
                "multiple_comparison": "HOLM_WITHIN_PREREGISTERED_CONTRASTS",
                "preregistered_contrasts": [
                    "B-frozen-wide_minus_A-fixed-feedback",
                    "B-targeted_minus_S-reflection-skill",
                    "B-frozen-wide_minus_B-targeted",
                    "S-reflection-skill_minus_A-fixed-feedback",
                ],
            },
            "wide_transition_invariants": {
                "active_component_instances": "ALL_FRESH",
                "compile_receipt_before_solution": True,
                "lineage_operational_fingerprint": "UNIQUE",
                "material_change_axes": list(_AXES),
                "rejected_transition": (
                    "ITT_FLOOR_NO_SOLUTION_NO_EVALUATOR_NO_RETRY"
                ),
            },
        },
        "online_pilot": {
            "benchmark_designs": online_benchmarks,
            "isolation": {
                "hybrid_allowed": False,
                "intermechanism_reads": False,
                "learned_mechanism_updater_counts_equal": True,
                "separate_checkpoints": True,
                "separate_ledgers": True,
                "shared_source_order_and_visibility": True,
            },
            "mechanisms": [
                {
                    "mechanism_id": "O0",
                    "state_kind": "NONE",
                    "state_root": "NONE",
                    "updater_calls_per_source_task": 0,
                },
                {
                    "mechanism_id": "OM",
                    "state_kind": "CONTENT_ADDRESSED_META_MEMORY",
                    "state_root": "online/OM/meta-memory",
                    "updater_calls_per_source_task": 1,
                },
                {
                    "mechanism_id": "OP",
                    "state_kind": "TYPED_VERSIONED_META_POLICY",
                    "state_root": "online/OP/meta-policy",
                    "updater_calls_per_source_task": 1,
                },
                {
                    "mechanism_id": "OA",
                    "state_kind": "TYPED_HARNESS_POPULATION_ARCHIVE",
                    "state_root": "online/OA/harness-archive",
                    "updater_calls_per_source_task": 1,
                },
            ],
            "seed_count": 2,
            "seeds": list(_ONLINE_SEEDS),
            "stages": [
                {
                    "evaluator_transactions_cumulative": 108,
                    "evaluator_transactions_incremental": 108,
                    "execution_condition": "CAPABILITY_AND_ENTITLEMENT_REQUIRED",
                    "logical_model_calls_cumulative": 300,
                    "logical_model_calls_incremental": 300,
                    "stage_id": "source",
                },
                {
                    "evaluator_transactions_cumulative": 252,
                    "evaluator_transactions_incremental": 144,
                    "execution_condition": "SEALED_SOURCE_SNAPSHOTS_REQUIRED",
                    "logical_model_calls_cumulative": 588,
                    "logical_model_calls_incremental": 288,
                    "stage_id": "O1",
                },
                {
                    "evaluator_transactions_cumulative": 732,
                    "evaluator_transactions_incremental": 480,
                    "execution_condition": "O1_PREREGISTERED_GATE_REQUIRED",
                    "logical_model_calls_cumulative": 1548,
                    "logical_model_calls_incremental": 960,
                    "stage_id": "O2",
                },
            ],
        },
        "qualification_binding": {
            "contract_id": "moss-cross-benchmark-qualification-v1",
            "path": (
                "optimization_lab/harness_builder/data/"
                "benchmark_qualification_v1.json"
            ),
            "sha256": _QUALIFICATION_SHA256,
        },
        "schema_version": 3,
    }


def _load_canonical(path: Path) -> tuple[dict[str, Any], bytes]:
    resolved = path.resolve(strict=True)
    if resolved.is_symlink() or not resolved.is_file():
        raise FactorialContractError("factorial manifest must be a regular file")
    raw = resolved.read_bytes()
    try:
        payload = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_json_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise FactorialContractError("factorial manifest is invalid JSON") from exc
    if not isinstance(payload, dict) or canonical_factorial_bytes(payload) != raw:
        raise FactorialContractError("factorial manifest is not canonical")
    return payload, raw


def _benchmark_by_id(
    payload: Mapping[str, Any] | Sequence[Mapping[str, Any]],
) -> dict[str, Mapping[str, Any]]:
    benchmarks = payload["benchmarks"] if isinstance(payload, Mapping) else payload
    return {item["benchmark_id"]: item for item in benchmarks}


def _verify_main_arithmetic(main: Mapping[str, Any]) -> None:
    accounting = main["logical_budget_accounting"]
    shared = accounting["shared_v001_per_task_seed"]
    post_v001 = accounting["post_v001_per_task_seed_round"]
    shared_eval = shared["evaluator_transactions"]
    shared_model = (
        shared["harness_builder_model_calls"]
        + shared["solution_model_calls"]
    )
    post_eval = sum(
        arm["evaluator_transactions"] for arm in post_v001.values()
    )
    post_model = sum(
        arm["arm_update_model_calls"] + arm["solution_model_calls"]
        for arm in post_v001.values()
    )
    expected_eval = 0
    expected_model = 0
    for benchmark in main["benchmarks"]:
        seeds = benchmark["seed_count"]
        tasks = benchmark["task_count"]
        rounds = benchmark["rounds"]
        evaluator_transactions = seeds * tasks * (
            shared_eval + post_eval * (rounds - 1)
        )
        logical_model_calls = seeds * tasks * (
            shared_model + post_model * (rounds - 1)
        )
        if benchmark["logical_budget"] != {
            "evaluator_transactions": evaluator_transactions,
            "logical_model_calls": logical_model_calls,
        }:
            raise FactorialContractError(
                f"{benchmark['benchmark_id']} main logical budget is inconsistent"
            )
        expected_eval += evaluator_transactions
        expected_model += logical_model_calls
    if main["logical_budget"] != {
        "evaluator_transactions": expected_eval,
        "logical_model_calls": expected_model,
    }:
        raise FactorialContractError("main logical budget is inconsistent")


def _verify_online_arithmetic(online: Mapping[str, Any]) -> None:
    seed_count = online["seed_count"]
    learned_mechanisms = sum(
        mechanism["updater_calls_per_source_task"]
        for mechanism in online["mechanisms"]
    )
    mechanism_count = len(online["mechanisms"])
    source_eval = sum(
        seed_count * design["source"]["task_count"] * design["source"]["rounds"]
        for design in online["benchmark_designs"]
    )
    source_updates = sum(
        seed_count * design["source"]["task_count"] * learned_mechanisms
        for design in online["benchmark_designs"]
    )
    source_model = 2 * source_eval + source_updates
    o1_eval = sum(
        mechanism_count * seed_count * design["heldout"]["task_count"]
        for design in online["benchmark_designs"]
    )
    o1_model = 2 * o1_eval
    o2_eval = sum(
        mechanism_count
        * seed_count
        * design["heldout"]["task_count"]
        * (design["heldout"]["rounds"] - 1)
        for design in online["benchmark_designs"]
    )
    o2_model = 2 * o2_eval
    expected = [
        (source_eval, source_model, source_eval, source_model),
        (o1_eval, o1_model, source_eval + o1_eval, source_model + o1_model),
        (
            o2_eval,
            o2_model,
            source_eval + o1_eval + o2_eval,
            source_model + o1_model + o2_model,
        ),
    ]
    for stage, (eval_inc, model_inc, eval_total, model_total) in zip(
        online["stages"], expected, strict=True
    ):
        if (
            stage["evaluator_transactions_incremental"] != eval_inc
            or stage["logical_model_calls_incremental"] != model_inc
            or stage["evaluator_transactions_cumulative"] != eval_total
            or stage["logical_model_calls_cumulative"] != model_total
        ):
            raise FactorialContractError(
                f"online stage {stage['stage_id']} logical budget is inconsistent"
            )


def _verify_split_references(
    payload: Mapping[str, Any], qualification: Mapping[str, Any]
) -> None:
    selected = _benchmark_by_id(qualification)
    main = _benchmark_by_id(payload["main_experiment"])
    online = _benchmark_by_id(payload["online_pilot"]["benchmark_designs"])
    agent_splits = selected["agenthpobench"]["selection"]["splits"]
    gdpevo_splits = selected["gdpevo"]["selection"]["splits"]
    if main["agenthpobench"]["task_units"] != agent_splits["T_fresh"]:
        raise FactorialContractError("AgentHPO main tasks drifted from T_fresh")
    if main["gdpevo"]["task_units"] != gdpevo_splits["T_fresh"]:
        raise FactorialContractError("GDPevo main groups drifted from T_fresh")
    if online["agenthpobench"]["source"]["task_units"] != agent_splits[
        "D_bank"
    ][:4]:
        raise FactorialContractError("AgentHPO online source drifted from D_bank")
    if online["agenthpobench"]["heldout"]["task_units"] != agent_splits[
        "T_fresh"
    ][:8]:
        raise FactorialContractError("AgentHPO online holdout drifted from T_fresh")
    for partition in ("source", "heldout"):
        if online["gdpevo"][partition]["task_units"] != gdpevo_splits[
            "T_fresh"
        ][:2]:
            raise FactorialContractError(
                f"GDpevo online {partition} groups drifted from T_fresh"
            )


def _main_arm_map(payload: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    main = payload.get("main_experiment")
    if not isinstance(main, Mapping):
        raise FactorialContractError("factorial main experiment differs")
    arms = main.get("arms")
    if not isinstance(arms, list) or any(
        not isinstance(item, Mapping) for item in arms
    ):
        raise FactorialContractError("factorial main arm declarations differ")
    result: dict[str, Mapping[str, Any]] = {}
    for arm in arms:
        arm_id = arm.get("arm_id")
        if not isinstance(arm_id, str) or arm_id in result:
            raise FactorialContractError("factorial main arm identities differ")
        result[arm_id] = arm
    if tuple(result) != ARM_IDS:
        raise FactorialContractError("factorial main arm order differs")
    return result


def _verify_typed_arm_policies(payload: Mapping[str, Any]) -> None:
    """Bind the manifest arm declarations to the executable typed validators."""

    arms = _main_arm_map(payload)
    for arm_id in ARM_IDS:
        arm = arms[arm_id]
        policy = ARM_POLICY_SPECS[arm_id]
        expected = {
            "architecture_frozen": arm["architecture_axes"] == "FROZEN",
            "minimum_material_axis_changes": arm[
                "minimum_material_axis_changes_after_v001"
            ],
            "require_lineage_unique": arm["lineage_fingerprint_unique"],
            "update_policy": arm["arm_update_policy"],
        }
        actual = {
            "architecture_frozen": policy.architecture_frozen,
            "minimum_material_axis_changes": policy.minimum_material_axis_changes,
            "require_lineage_unique": policy.require_lineage_unique,
            "update_policy": policy.update_policy,
        }
        if actual != expected:
            raise FactorialContractError(
                f"typed arm policy for {arm_id} differs from the manifest"
            )


def _verify_itt_policies(payload: Mapping[str, Any]) -> None:
    """Bind native-floor ITT policies to this exact factorial contract."""

    main = payload.get("main_experiment")
    if not isinstance(main, Mapping):
        raise FactorialContractError("factorial main experiment differs")
    try:
        benchmark_ids = tuple(
            benchmark["benchmark_id"] for benchmark in main["benchmarks"]
        )
        boundary = main["score_boundary"]
    except (KeyError, TypeError) as exc:
        raise FactorialContractError("factorial ITT boundary differs") from exc
    if (
        boundary.get("invalid_itt_floor_policy")
        != "BENCHMARK_NATIVE_RAW_MINIMUM_BOUND"
        or boundary.get("invalid_itt_scope")
        != (
            "TYPED_INVALID_SCORE_RECEIPT_"
            "ALL_RESERVED_ATTEMPT_COVERAGE_NOT_READY"
        )
        or boundary.get("itt_policy_schema") != "factorial_itt_policy_v1"
        or boundary.get("itt_reporting_metric")
        != "ITT_NATIVE_RAW_SCORE_ONLY"
    ):
        raise FactorialContractError("factorial ITT policy declaration differs")
    for benchmark_id in benchmark_ids:
        contract = score_contract_for(benchmark_id)
        try:
            declared_sha = boundary["contract_sha256s"][benchmark_id]
        except (KeyError, TypeError) as exc:
            raise FactorialContractError("factorial score contract map differs") from exc
        if (
            declared_sha != contract.sha256
            or contract.utility_from_raw(contract.raw_min) != contract.utility_min
        ):
            raise FactorialContractError(
                f"{benchmark_id} factorial ITT policy projection differs"
            )


def factorial_main_arm_variant_projections(
    payload: Mapping[str, Any],
) -> tuple[dict[str, Any], ...]:
    """Return the complete frozen main-arm declarations in canonical order.

    In the factorial contract an arm declaration is the immutable variant
    contract consumed by the later formal provider factory.  Hashing every
    field avoids a hand-maintained projection silently omitting a new arm
    semantic.  ``verify_factorial_contract`` must run before callers rely on
    these projections.
    """

    arms = _main_arm_map(payload)
    return tuple(dict(arms[arm_id]) for arm_id in ARM_IDS)


def factorial_main_arm_variant_sha256s(
    payload: Mapping[str, Any],
) -> dict[str, str]:
    """Hash each complete frozen main-arm variant declaration."""

    return {
        arm["arm_id"]: _factorial_projection_sha256(arm)
        for arm in factorial_main_arm_variant_projections(payload)
    }


def factorial_main_matrix_projection(
    payload: Mapping[str, Any],
) -> tuple[dict[str, Any], ...]:
    """Expand the exact checked-in main task×seed matrix.

    GDPevo task groups expand to the five official test tasks with stable
    instance ids ``task_group_NNN:test_1`` through ``:test_5``.  The returned
    order is benchmark declaration, seed declaration, task-unit declaration,
    then within-unit task ordinal.  It is an audit projection only and grants
    no calls or evaluator transactions.
    """

    main = payload.get("main_experiment")
    if not isinstance(main, Mapping) or not isinstance(
        main.get("benchmarks"), list
    ):
        raise FactorialContractError("factorial main benchmark declarations differ")
    result: list[dict[str, Any]] = []
    for benchmark in main["benchmarks"]:
        if not isinstance(benchmark, Mapping):
            raise FactorialContractError("factorial main benchmark differs")
        benchmark_id = benchmark.get("benchmark_id")
        seeds = benchmark.get("seeds")
        task_units = benchmark.get("task_units")
        tasks_per_unit = benchmark.get("tasks_per_unit")
        rounds = benchmark.get("rounds")
        if (
            not isinstance(benchmark_id, str)
            or not isinstance(seeds, list)
            or not isinstance(task_units, list)
            or type(tasks_per_unit) is not int
            or tasks_per_unit < 1
            or type(rounds) is not int
            or rounds < 1
        ):
            raise FactorialContractError("factorial main benchmark matrix differs")
        for seed_index, seed in enumerate(seeds):
            if type(seed) is not int:
                raise FactorialContractError("factorial main seed differs")
            task_index = 0
            for task_unit in task_units:
                if not isinstance(task_unit, str):
                    raise FactorialContractError("factorial main task unit differs")
                for task_ordinal in range(1, tasks_per_unit + 1):
                    instance_id = (
                        task_unit
                        if tasks_per_unit == 1
                        else f"{task_unit}:test_{task_ordinal}"
                    )
                    result.append(
                        {
                            "benchmark_id": benchmark_id,
                            "final_version": rounds,
                            "instance_id": instance_id,
                            "seed": seed,
                            "seed_index": seed_index,
                            "task_index": task_index,
                            "task_ordinal": task_ordinal,
                            "task_unit": task_unit,
                        }
                    )
                    task_index += 1
        expected_count = benchmark.get("task_count")
        if expected_count != len(task_units) * tasks_per_unit:
            raise FactorialContractError(
                f"{benchmark_id} factorial task expansion count differs"
            )
    return tuple(result)


def verify_factorial_contract(
    manifest_path: Path = DEFAULT_FACTORIAL_MANIFEST,
    *,
    qualification_manifest_path: Path = DEFAULT_QUALIFICATION_MANIFEST,
    request_execution: bool = False,
    prior_result_references: Sequence[str | Path] = (),
) -> dict[str, Any]:
    """Verify the factors and budgets without granting or performing execution."""

    if prior_result_references:
        raise FactorialContractError(
            "prior Moss results may not enter the fresh factorial experiment"
        )
    payload, _ = _load_canonical(manifest_path)
    digest = payload.get("contract_digest")
    if not isinstance(digest, str) or digest != factorial_contract_digest(payload):
        raise FactorialContractError("factorial contract digest differs")
    projection = dict(payload)
    projection.pop("contract_digest")
    if projection != _expected_projection():
        raise FactorialContractError("factorial contract fields or values differ")

    qualification_raw = qualification_manifest_path.resolve(strict=True).read_bytes()
    if hashlib.sha256(qualification_raw).hexdigest() != _QUALIFICATION_SHA256:
        raise FactorialContractError("qualification manifest SHA256 differs")
    qualification = verify_benchmark_qualification(qualification_manifest_path)
    if qualification["contract_id"] != payload["qualification_binding"]["contract_id"]:
        raise FactorialContractError("qualification contract binding differs")

    if payload["execution_entitlement"] != _ZERO_ENTITLEMENT:
        raise FactorialContractError("factorial execution entitlement must be zero")
    _verify_split_references(payload, qualification)
    _verify_main_arithmetic(payload["main_experiment"])
    _verify_online_arithmetic(payload["online_pilot"])
    _verify_typed_arm_policies(payload)
    _verify_itt_policies(payload)
    # Force exact matrix expansion during every verification so a future
    # partition/count change cannot bypass the formal plan factory.
    factorial_main_matrix_projection(payload)

    if request_execution:
        if payload["implementation_status"]["formal_executor"] != "READY":
            raise FactorialContractError(
                "factorial formal executor is not ready and has no execution authority"
            )
        if payload["execution_authority"] != "GRANTED":
            raise FactorialContractError("factorial contract has no execution authority")
        if not any(payload["execution_entitlement"].values()):
            raise FactorialContractError("factorial contract has no execution entitlement")
    return payload


__all__ = [
    "DEFAULT_FACTORIAL_MANIFEST",
    "FactorialContractError",
    "canonical_factorial_bytes",
    "factorial_contract_digest",
    "factorial_main_arm_variant_projections",
    "factorial_main_arm_variant_sha256s",
    "factorial_main_matrix_projection",
    "verify_factorial_contract",
]
