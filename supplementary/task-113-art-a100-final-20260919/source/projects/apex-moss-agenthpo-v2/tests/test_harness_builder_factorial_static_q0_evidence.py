from __future__ import annotations

import hashlib
import os
from pathlib import Path
import subprocess

import pytest

from optimization_lab.harness_builder.agenthpo_qualification import (
    AgentHPOQualificationError,
)
from optimization_lab.harness_builder.factorial_static_q0_evidence import (
    FactorialStaticQ0Evidence,
    FactorialStaticQ0EvidenceError,
    build_factorial_static_q0_evidence,
    verify_factorial_static_q0_evidence,
)


_AGENT = Path(
    os.environ.get(
        "MOSS_TEST_AGENTHPO_CHECKOUT",
        "/tmp/moss-bench-qual.rYRM8Q/agenthpobench",
    )
)
_GDP = Path(
    os.environ.get(
        "MOSS_TEST_GDPEVO_CHECKOUT",
        "/tmp/moss-bench-qual.rYRM8Q/gdpevo",
    )
)
_Q7 = (
    "modernbert_mnli_accuracy",
    "cifar10_airbench94",
    "sparsetsf_ettm1_96_mse",
    "noisygl_cora_uniform30_gcn",
    "art_2048_win_rate",
    "simple_rl_reason_qwen25_05b_math500",
    "vbll_yacht_rmse",
)
_Q6 = (
    "task_group_006",
    "task_group_024",
    "task_group_015",
    "task_group_007",
    "task_group_001",
    "task_group_014",
)


def _require_sources() -> tuple[Path, Path]:
    if not _AGENT.is_dir() or not _GDP.is_dir():
        pytest.skip("pinned factorial qualification checkouts are unavailable")
    return _AGENT.resolve(), _GDP.resolve()


@pytest.fixture(scope="module")
def evidence() -> FactorialStaticQ0Evidence:
    agent, gdpevo = _require_sources()
    return build_factorial_static_q0_evidence(
        agenthpo_checkout=agent,
        gdpevo_checkout=gdpevo,
    )


def test_static_q0_evidence_is_canonical_content_addressed_and_zero_authority(
    evidence: FactorialStaticQ0Evidence,
) -> None:
    payload = evidence.to_dict()
    assert evidence.sha256 == hashlib.sha256(evidence.canonical_bytes).hexdigest()
    with pytest.raises(
        FactorialStaticQ0EvidenceError, match="trusted source replay"
    ):
        FactorialStaticQ0Evidence(evidence.canonical_bytes)
    assert payload["execution_authority"] == "NOT_GRANTED"
    assert payload["execution_entitlement"] == {
        "cpu_evaluator_seconds": 0,
        "evaluator_transactions": 0,
        "gpu_exclusive_seconds": 0,
        "max_parallel": 0,
        "model_calls": 0,
    }
    assert payload["scope_boundary"] == {
        "benchmark_runtime_called": False,
        "evaluator_called": False,
        "formal_execution_ready": False,
        "is_environment_canary": False,
        "is_isolation_canary": False,
        "is_reference_canary": False,
        "model_called": False,
        "private_gdpevo_gold_content_read": False,
    }
    agent, gdpevo = _require_sources()
    assert verify_factorial_static_q0_evidence(
        evidence.canonical_bytes,
        agenthpo_checkout=agent,
        gdpevo_checkout=gdpevo,
    ) == evidence
    with pytest.raises(FactorialStaticQ0EvidenceError, match="no execution authority"):
        verify_factorial_static_q0_evidence(
            evidence,
            agenthpo_checkout=agent,
            gdpevo_checkout=gdpevo,
            request_execution=True,
        )


def test_agenthpo_replays_q7_and_actually_rejects_all_twenty_one_negatives(
    evidence: FactorialStaticQ0Evidence,
) -> None:
    suite = evidence.to_dict()["agenthpobench"]
    assert suite["source_checkout"] == {
        "file_count": 31,
        "git_commit": "6d8d90071cdb16b06f0db866480ecaae48880fba",
        "root_tree": "1acedca0a63252deea57a51878b4ddfd002aa507",
        "verified": True,
    }
    assert tuple(task["task_id"] for task in suite["tasks"]) == _Q7
    assertions = [
        assertion
        for task in suite["tasks"]
        for assertion in task["negative_assertions"]
    ]
    assert len(assertions) == 21
    assert {
        kind: sum(item["negative_kind"] == kind for item in assertions)
        for kind in (
            "unknown_key",
            "out_of_range_value",
            "no_operational_change",
        )
    } == {
        "unknown_key": 7,
        "out_of_range_value": 7,
        "no_operational_change": 7,
    }
    assert all(
        item["disposition"] == "STRICT_CODEC_REJECT_BEFORE_EVALUATOR"
        and item["evaluator_called"] is False
        and item["evaluator_transaction_debit"] == 0
        and hashlib.sha256(item["candidate_canonical_json"].encode()).hexdigest()
        == item["candidate_sha256"]
        for item in assertions
    )
    assert {item["rejection_code"] for item in assertions} == {
        "UNKNOWN_KEY",
        "OUT_OF_RANGE_VALUE",
        "NO_OPERATIONAL_CHANGE",
    }


def test_gdpevo_replays_only_pinned_git_trees_and_marks_manifest_unverified(
    evidence: FactorialStaticQ0Evidence,
) -> None:
    suite = evidence.to_dict()["gdpevo"]
    assert suite["source_checkout"] == {
        "git_commit": "0999c0d1e6f59b1cb8464cac4e5ed856b5dcb9e4",
        "root_tree": "983742f806f4bf6c4043d5ebea62dc4095be4c0d",
        "task_groups_tree": "2949144b022e5028ee8b48f4bb27355496df19de",
        "verified": True,
    }
    assert tuple(group["group_id"] for group in suite["qualification_groups"]) == _Q6
    assert all(
        group["group_object_type"] == "tree"
        and group["environment_object_type"] == "tree"
        and group["test_tasks_object_type"] == "tree"
        and group["test_task_subtree_count"] == 5
        for group in suite["qualification_groups"]
    )
    assert suite["file_manifest_replay"] == {
        "expected_contract_projection_sha256": (
            "6a3e3de6876757f00c4dcc634de39a6cf05ff08b3c377fe126a0b506b8f054a5"
        ),
        "mechanically_recomputed": False,
        "private_file_content_read": False,
        "status": "UNVERIFIED_NO_FROZEN_REPLAY_ALGORITHM",
    }
    raw = evidence.canonical_bytes
    assert b"/output/" not in raw
    assert b"/eval/" not in raw
    assert b"gold.json" not in raw


def test_forged_negative_disposition_cannot_pass_trusted_evidence(
    evidence: FactorialStaticQ0Evidence,
) -> None:
    forged = evidence.to_dict()
    forged["agenthpobench"]["tasks"][0]["negative_assertions"][0][
        "disposition"
    ] = "ACCEPTED"
    agent, gdpevo = _require_sources()
    with pytest.raises(FactorialStaticQ0EvidenceError):
        verify_factorial_static_q0_evidence(
            forged,
            agenthpo_checkout=agent,
            gdpevo_checkout=gdpevo,
        )


def test_self_rehashed_source_claim_cannot_pass_trusted_replay(
    evidence: FactorialStaticQ0Evidence,
) -> None:
    forged_payload = evidence.to_dict()
    forged_payload["gdpevo"]["source_checkout"]["root_tree"] = "f" * 40
    agent, gdpevo = _require_sources()
    with pytest.raises(FactorialStaticQ0EvidenceError):
        verify_factorial_static_q0_evidence(
            forged_payload,
            agenthpo_checkout=agent,
            gdpevo_checkout=gdpevo,
        )


@pytest.mark.parametrize(
    ("target", "replacement"),
    [
        (("agenthpobench", "tasks", 0, "intervention_space_sha256"), "f" * 64),
        (("gdpevo", "qualification_groups", 0, "group_tree"), "f" * 40),
        (
            (
                "agenthpobench",
                "tasks",
                0,
                "negative_assertions",
                0,
                "candidate_canonical_json",
            ),
            "{}",
        ),
    ],
)
def test_self_rehashed_nested_claim_cannot_pass_trusted_replay(
    evidence: FactorialStaticQ0Evidence,
    target: tuple[object, ...],
    replacement: str,
) -> None:
    forged = evidence.to_dict()
    cursor: object = forged
    for key in target[:-1]:
        cursor = cursor[key]  # type: ignore[index]
    cursor[target[-1]] = replacement  # type: ignore[index]
    if target[-1] == "candidate_canonical_json":
        cursor["candidate_sha256"] = hashlib.sha256(  # type: ignore[index]
            replacement.encode()
        ).hexdigest()
    agent, gdpevo = _require_sources()
    with pytest.raises(FactorialStaticQ0EvidenceError):
        verify_factorial_static_q0_evidence(
            forged,
            agenthpo_checkout=agent,
            gdpevo_checkout=gdpevo,
        )


def test_gdpevo_private_worktree_bytes_are_not_static_evidence_inputs(
    tmp_path: Path,
    evidence: FactorialStaticQ0Evidence,
) -> None:
    agent, gdpevo = _require_sources()
    private_dirty = tmp_path / "gdpevo-private-dirty"
    subprocess.run(
        ("git", "clone", "--shared", str(gdpevo), str(private_dirty)),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    private_answer = (
        private_dirty
        / "data/task_groups/task_group_006/test_tasks/001/output/answer.json"
    )
    private_answer.write_text(
        "private worktree bytes must be ignored\n", encoding="utf-8"
    )
    rebuilt = build_factorial_static_q0_evidence(
        agenthpo_checkout=agent,
        gdpevo_checkout=private_dirty.resolve(),
    )
    assert rebuilt == evidence


def test_source_commit_drift_fails_before_static_evidence(
    tmp_path: Path,
) -> None:
    agent, gdpevo = _require_sources()
    drifted = tmp_path / "agenthpo-drifted"
    subprocess.run(
        ("git", "clone", "--shared", str(agent), str(drifted)),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    marker = drifted / "STATIC_Q0_DRIFT_MARKER"
    marker.write_text("tracked source drift\n", encoding="utf-8")
    subprocess.run(
        ("git", "-C", str(drifted), "add", marker.name),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    environment = dict(os.environ)
    environment.update(
        {
            "GIT_AUTHOR_EMAIL": "static-q0@example.invalid",
            "GIT_AUTHOR_NAME": "Static Q0 Test",
            "GIT_COMMITTER_EMAIL": "static-q0@example.invalid",
            "GIT_COMMITTER_NAME": "Static Q0 Test",
        }
    )
    subprocess.run(
        ("git", "-C", str(drifted), "commit", "-m", "static q0 drift"),
        check=True,
        env=environment,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    with pytest.raises(AgentHPOQualificationError, match="commit drifted"):
        build_factorial_static_q0_evidence(
            agenthpo_checkout=drifted.resolve(),
            gdpevo_checkout=gdpevo,
        )
