from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from optimization_lab.harness_builder.factorial_contract import (
    DEFAULT_FACTORIAL_MANIFEST,
    FactorialContractError,
    canonical_factorial_bytes,
    factorial_contract_digest,
    factorial_main_arm_variant_projections,
    factorial_main_arm_variant_sha256s,
    factorial_main_matrix_projection,
    verify_factorial_contract,
)
from optimization_lab.harness_builder.qualification import (
    DEFAULT_QUALIFICATION_MANIFEST,
)


def _payload() -> dict[str, object]:
    return json.loads(DEFAULT_FACTORIAL_MANIFEST.read_text(encoding="utf-8"))


def _seal(payload: dict[str, object]) -> dict[str, object]:
    payload["contract_digest"] = factorial_contract_digest(payload)
    return payload


def _write(tmp_path: Path, payload: object, *, canonical: bool = True) -> Path:
    path = tmp_path / "factorial.json"
    if canonical:
        path.write_bytes(canonical_factorial_bytes(payload))
    else:
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def _main_benchmark(
    payload: dict[str, object], benchmark_id: str
) -> dict[str, object]:
    main = payload["main_experiment"]
    assert isinstance(main, dict)
    benchmarks = main["benchmarks"]
    assert isinstance(benchmarks, list)
    return next(item for item in benchmarks if item["benchmark_id"] == benchmark_id)


def test_checked_in_contract_freezes_four_arms_wide_invariants_and_two_suites() -> None:
    payload = verify_factorial_contract()
    assert payload["execution_authority"] == "NOT_GRANTED"
    assert not any(payload["execution_entitlement"].values())
    assert payload["implementation_status"] == {
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
    }
    assert payload["harness_axes"] == [
        "role_graph",
        "memory_views",
        "tools",
        "parent_strategy",
        "workflow",
        "scheduler_mode",
        "recovery_mode",
    ]

    main = payload["main_experiment"]
    arms = {arm["arm_id"]: arm for arm in main["arms"]}
    assert list(arms) == [
        "A-fixed-feedback",
        "S-reflection-skill",
        "B-targeted",
        "B-frozen-wide",
    ]
    assert all(arm["solver_native_feedback"] for arm in arms.values())
    assert all(arm["cross_task_state"] == "NONE" for arm in arms.values())
    assert arms["A-fixed-feedback"]["arm_update_policy"] == "fixed_feedback_v1"
    assert all(
        arm["arm_update_policy_status"]
        == "TYPED_VALIDATION_READY_FORMAL_DISPATCH_NOT_READY"
        for arm in arms.values()
    )
    assert all(
        arm["runtime_adaptation_policy_namespace"] == "BUILDER_VARIANT"
        for arm in arms.values()
    )
    assert arms["A-fixed-feedback"]["runtime_adaptation_policy"] == (
        "conditional_any_v1"
    )
    assert arms["A-fixed-feedback"]["architecture_axes"] == "FROZEN"
    assert arms["S-reflection-skill"]["arm_update_policy"] == (
        "reflection_skill_only_v1"
    )
    assert arms["S-reflection-skill"]["runtime_adaptation_policy"] == (
        "conditional_any_v1"
    )
    assert arms["S-reflection-skill"]["text_skill_state"] == (
        "TASK_LOCAL_RESET_AFTER_TASK"
    )
    assert arms["B-targeted"]["arm_update_policy"] == (
        "targeted_any_change_v1"
    )
    assert arms["B-targeted"]["runtime_adaptation_policy"] == (
        "targeted_any_change_v1"
    )
    assert arms["B-targeted"]["minimum_material_axis_changes_after_v001"] == 1
    wide = arms["B-frozen-wide"]
    assert wide["arm_update_policy"] == "wide_all_fields_recompile_v1"
    assert wide["runtime_adaptation_policy"] == "wide_all_fields_recompile_v1"
    assert wide["minimum_material_axis_changes_after_v001"] == 7
    assert wide["fresh_component_instances_after_v001"] is True
    assert wide["lineage_fingerprint_unique"] is True
    assert main["shared_v001"] == {
        "arm_specific_v001_execution": "NONE",
        "arm_specific_compile_receipts_identical": False,
        "arm_specific_receipt_binding": "REFERENCE_TRUNK_SHA256_AND_BIND_ARM_ID",
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
    }
    accounting = main["logical_budget_accounting"]
    assert accounting["shared_v001_per_task_seed"] == {
        "evaluator_transactions": 1,
        "harness_builder_model_calls": 1,
        "solution_model_calls": 1,
    }
    assert accounting["post_v001_per_task_seed_round"]["A-fixed-feedback"] == {
        "arm_update_model_calls": 0,
        "arm_update_operation": "NONE_NO_SHAM_CALL",
        "evaluator_transactions": 1,
        "solution_model_calls": 1,
    }
    assert main["wide_transition_invariants"]["material_change_axes"] == payload[
        "harness_axes"
    ]
    assert main["primary_outcome"] == (
        "post_v001_itt_native_raw_auc_by_benchmark"
    )
    assert main["score_boundary"] == {
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
    }
    assert main["task_local_skill"]["architecture_axes"] == "FROZEN_V001"
    assert main["task_local_skill"]["formal_dispatch"] == "NOT_READY"
    assert main["task_local_skill"]["typed_artifact_validation"] == "READY"

    benchmarks = {
        benchmark["benchmark_id"]: benchmark for benchmark in main["benchmarks"]
    }
    assert benchmarks["agenthpobench"]["task_count"] == 12
    assert benchmarks["agenthpobench"]["rounds"] == 6
    assert benchmarks["agenthpobench"]["seed_count"] == 3
    assert benchmarks["gdpevo"]["task_count"] == 30
    assert len(benchmarks["gdpevo"]["task_units"]) == 6
    assert benchmarks["gdpevo"]["tasks_per_unit"] == 5
    assert benchmarks["gdpevo"]["rounds"] == 3
    assert benchmarks["gdpevo"]["seed_count"] == 3
    assert main["logical_budget"] == {
        "evaluator_transactions": 1566,
        "logical_model_calls": 2772,
    }
    assert payload["schema_version"] == 3


def test_online_pilot_isolates_o0_memory_policy_archive_and_stages() -> None:
    online = verify_factorial_contract()["online_pilot"]
    mechanisms = {
        mechanism["mechanism_id"]: mechanism
        for mechanism in online["mechanisms"]
    }
    assert list(mechanisms) == ["O0", "OM", "OP", "OA"]
    assert mechanisms["O0"]["state_kind"] == "NONE"
    assert mechanisms["OM"]["state_kind"] == (
        "CONTENT_ADDRESSED_META_MEMORY"
    )
    assert mechanisms["OP"]["state_kind"] == "TYPED_VERSIONED_META_POLICY"
    assert mechanisms["OA"]["state_kind"] == (
        "TYPED_HARNESS_POPULATION_ARCHIVE"
    )
    assert len(
        {
            mechanism["state_root"]
            for mechanism in mechanisms.values()
            if mechanism["mechanism_id"] != "O0"
        }
    ) == 3
    assert online["isolation"] == {
        "hybrid_allowed": False,
        "intermechanism_reads": False,
        "learned_mechanism_updater_counts_equal": True,
        "separate_checkpoints": True,
        "separate_ledgers": True,
        "shared_source_order_and_visibility": True,
    }
    assert online["seed_count"] == 2
    stages = {stage["stage_id"]: stage for stage in online["stages"]}
    assert stages["O1"]["evaluator_transactions_cumulative"] == 252
    assert stages["O1"]["logical_model_calls_cumulative"] == 588
    assert stages["O2"]["evaluator_transactions_incremental"] == 480
    assert stages["O2"]["logical_model_calls_incremental"] == 960
    assert stages["O2"]["execution_condition"] == (
        "O1_PREREGISTERED_GATE_REQUIRED"
    )


def test_contract_binds_qualification_hash_and_exact_split_members() -> None:
    payload = verify_factorial_contract()
    assert payload["qualification_binding"]["sha256"] == (
        "ba415a2466e7b5e1b5e4b43f50f59dbb13cd7ff93d20bc616f71e658d5e7bafd"
    )
    agent = _main_benchmark(payload, "agenthpobench")
    assert agent["task_units"] == [
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
    ]
    gdpevo = _main_benchmark(payload, "gdpevo")
    assert gdpevo["task_units"] == [
        "task_group_003",
        "task_group_023",
        "task_group_005",
        "task_group_018",
        "task_group_012",
        "task_group_017",
    ]


def test_contract_expands_exact_main_matrix_and_hashes_complete_arm_variants() -> None:
    payload = verify_factorial_contract()
    matrix = factorial_main_matrix_projection(payload)
    assert len(matrix) == 126
    assert matrix[0] == {
        "benchmark_id": "agenthpobench",
        "final_version": 6,
        "instance_id": "hyperboliccv_cifar100_accuracy",
        "seed": 2026081201,
        "seed_index": 0,
        "task_index": 0,
        "task_ordinal": 1,
        "task_unit": "hyperboliccv_cifar100_accuracy",
    }
    assert next(
        item
        for item in matrix
        if item["benchmark_id"] == "gdpevo"
    ) == {
        "benchmark_id": "gdpevo",
        "final_version": 3,
        "instance_id": "task_group_003:test_1",
        "seed": 2026081201,
        "seed_index": 0,
        "task_index": 0,
        "task_ordinal": 1,
        "task_unit": "task_group_003",
    }
    assert len(
        {
            (item["benchmark_id"], item["instance_id"], item["seed"])
            for item in matrix
        }
    ) == 126

    projections = factorial_main_arm_variant_projections(payload)
    hashes = factorial_main_arm_variant_sha256s(payload)
    assert tuple(item["arm_id"] for item in projections) == tuple(hashes)
    assert len(set(hashes.values())) == 4
    for projection in projections:
        changed = copy.deepcopy(projection)
        changed["solver_native_feedback"] = not changed["solver_native_feedback"]
        assert canonical_factorial_bytes(changed) != canonical_factorial_bytes(
            projection
        )


def test_noncanonical_unknown_and_digest_drift_fail(tmp_path: Path) -> None:
    with pytest.raises(FactorialContractError, match="not canonical"):
        verify_factorial_contract(
            _write(tmp_path, _payload(), canonical=False)
        )

    payload = _payload()
    payload["unexpected"] = True
    _seal(payload)
    with pytest.raises(FactorialContractError, match="fields or values differ"):
        verify_factorial_contract(_write(tmp_path, payload))

    payload = _payload()
    payload["contract_digest"] = "0" * 64
    with pytest.raises(FactorialContractError, match="digest differs"):
        verify_factorial_contract(_write(tmp_path, payload))


def test_wide_axis_or_fresh_instance_weakening_fails(tmp_path: Path) -> None:
    payload = _payload()
    main = payload["main_experiment"]
    assert isinstance(main, dict)
    arms = main["arms"]
    assert isinstance(arms, list)
    wide = next(arm for arm in arms if arm["arm_id"] == "B-frozen-wide")
    wide["minimum_material_axis_changes_after_v001"] = 6
    wide["fresh_component_instances_after_v001"] = False
    _seal(payload)
    with pytest.raises(FactorialContractError, match="fields or values differ"):
        verify_factorial_contract(_write(tmp_path, payload))


def test_runtime_policy_trunk_or_executor_readiness_drift_fails(
    tmp_path: Path,
) -> None:
    payload = _payload()
    main = payload["main_experiment"]
    assert isinstance(main, dict)
    arms = main["arms"]
    assert isinstance(arms, list)
    arms[0]["runtime_adaptation_policy"] = "fixed_feedback_v1"
    _seal(payload)
    with pytest.raises(FactorialContractError, match="fields or values differ"):
        verify_factorial_contract(_write(tmp_path, payload))

    payload = _payload()
    shared = payload["main_experiment"]["shared_v001"]
    shared["arm_specific_compile_receipts_identical"] = True
    _seal(payload)
    with pytest.raises(FactorialContractError, match="fields or values differ"):
        verify_factorial_contract(_write(tmp_path, payload))

    payload = _payload()
    payload["implementation_status"]["formal_executor"] = "READY"
    _seal(payload)
    with pytest.raises(FactorialContractError, match="fields or values differ"):
        verify_factorial_contract(_write(tmp_path, payload))


def test_a_post_v001_solution_only_budget_assumption_is_bound(tmp_path: Path) -> None:
    payload = _payload()
    accounting = payload["main_experiment"]["logical_budget_accounting"]
    a_round = accounting["post_v001_per_task_seed_round"]["A-fixed-feedback"]
    a_round["arm_update_model_calls"] = 1
    _seal(payload)
    with pytest.raises(FactorialContractError, match="fields or values differ"):
        verify_factorial_contract(_write(tmp_path, payload))


@pytest.mark.parametrize(
    ("benchmark_id", "budget_field"),
    [
        ("agenthpobench", "evaluator_transactions"),
        ("gdpevo", "logical_model_calls"),
    ],
)
def test_main_budget_or_task_split_drift_fails(
    tmp_path: Path, benchmark_id: str, budget_field: str
) -> None:
    payload = _payload()
    benchmark = _main_benchmark(payload, benchmark_id)
    budget = benchmark["logical_budget"]
    assert isinstance(budget, dict)
    budget[budget_field] += 1
    _seal(payload)
    with pytest.raises(FactorialContractError, match="fields or values differ"):
        verify_factorial_contract(_write(tmp_path, payload))

    payload = _payload()
    agent = _main_benchmark(payload, "agenthpobench")
    agent["task_units"][0], agent["task_units"][1] = (
        agent["task_units"][1],
        agent["task_units"][0],
    )
    _seal(payload)
    with pytest.raises(FactorialContractError, match="fields or values differ"):
        verify_factorial_contract(_write(tmp_path, payload))


def test_online_budget_and_mechanism_isolation_drift_fail(tmp_path: Path) -> None:
    payload = _payload()
    online = payload["online_pilot"]
    assert isinstance(online, dict)
    stages = online["stages"]
    assert isinstance(stages, list)
    stages[1]["logical_model_calls_cumulative"] = 589
    _seal(payload)
    with pytest.raises(FactorialContractError, match="fields or values differ"):
        verify_factorial_contract(_write(tmp_path, payload))

    payload = _payload()
    online = payload["online_pilot"]
    assert isinstance(online, dict)
    mechanisms = online["mechanisms"]
    assert isinstance(mechanisms, list)
    mechanisms[2]["state_root"] = mechanisms[1]["state_root"]
    _seal(payload)
    with pytest.raises(FactorialContractError, match="fields or values differ"):
        verify_factorial_contract(_write(tmp_path, payload))


def test_old_results_and_execution_requests_fail_closed(tmp_path: Path) -> None:
    with pytest.raises(FactorialContractError, match="prior Moss results"):
        verify_factorial_contract(
            prior_result_references=[
                Path("results/optimization_lab/hb-three-arm-live-v1r9")
            ]
        )
    with pytest.raises(FactorialContractError, match="no execution authority"):
        verify_factorial_contract(request_execution=True)

    payload = copy.deepcopy(_payload())
    history = payload["history_boundary"]
    assert isinstance(history, dict)
    history["prior_result_import"] = "ALLOW_V1R8"
    _seal(payload)
    with pytest.raises(FactorialContractError, match="fields or values differ"):
        verify_factorial_contract(_write(tmp_path, payload))


def test_qualification_byte_drift_fails_even_if_json_is_valid(tmp_path: Path) -> None:
    qualification_copy = tmp_path / "qualification.json"
    payload = json.loads(
        DEFAULT_QUALIFICATION_MANIFEST.read_text(encoding="utf-8")
    )
    history = payload["history_boundary"]
    assert isinstance(history, dict)
    history["experience_bank_initial_state"] = "STILL_EMPTY_BUT_DRIFTED"
    qualification_copy.write_text(
        json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(FactorialContractError, match="SHA256 differs"):
        verify_factorial_contract(
            qualification_manifest_path=qualification_copy
        )
