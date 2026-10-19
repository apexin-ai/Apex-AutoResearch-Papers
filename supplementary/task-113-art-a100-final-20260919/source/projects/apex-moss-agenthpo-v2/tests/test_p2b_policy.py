from __future__ import annotations

import json

import pytest

from optimization_lab.p2b_policy import (
    InvalidP2bPolicy,
    P2bPolicyVersion,
    ScoreTrend,
    initial_policy,
)


def _response(**overrides: object) -> str:
    data: dict[str, object] = {
        "mode": "architecture_reset",
        "base_candidate_id": "reference",
        "diagnostic_level": "full",
        "observed_evidence": ["当前正确候选为 3.0x，连续两轮没有超过历史最好。"],
        "primary_hypothesis": "当前线程分工让归约路径保留了过多中间状态。",
        "score_assessment": "本轮比上一轮慢 4%，且比历史最好慢 7%，不是噪声改善。",
        "direction_change_reason": "原路线连续没有可信提升，因此放弃原分块并从参考语义重新设计。",
        "mutation_scope": ["kernel_count", "reduction_structure", "thread_mapping"],
        "enabled_skills": [
            "score_trend",
            "architecture_rebuild",
            "compiler_resource_analysis",
            "novelty_check",
        ],
        "tool_plan": ["score", "static_structure", "nsys_timeline"],
        "memory_views": ["historical_best", "recent", "structurally_novel"],
        "workflow_steps": [
            "Compare the latest score with the previous and historical best.",
            "Inspect the requested evidence and separate observation from hypothesis.",
            "Choose a meaningfully different base and Kernel structure.",
            "Generate exactly one complete candidate.",
        ],
        "avoid_repeats": ["不再只调整 num_warps"],
        "kernel_instructions": [
            "重新决定单核或双核结构。",
            "先保证固定输入形状上的数值正确性。",
        ],
        "force_restart": True,
        "structural_change": True,
    }
    data.update(overrides)
    return json.dumps(data, ensure_ascii=False)


def test_policy_requires_real_direction_change_when_score_does_not_improve() -> None:
    current = initial_policy(
        strategy="profile_exploit",
        starting_candidate_id="p2-best",
    )
    changed = P2bPolicyVersion.from_response(
        version_id="v002",
        parent=current,
        response=_response(),
        allowed_base_candidate_ids={"p2-best", "reference", "round-1"},
        require_direction_change=True,
        require_structural_change=True,
        require_restart=True,
    )

    assert changed.policy.mode == "architecture_reset"
    assert changed.policy.base_candidate_id == "reference"
    assert changed.policy.force_restart
    assert changed.policy.structural_change

    unchanged = _response(
        mode=current.policy.mode,
        base_candidate_id=current.policy.base_candidate_id,
        mutation_scope=list(current.policy.mutation_scope),
        enabled_skills=list(current.policy.enabled_skills),
        tool_plan=list(current.policy.tool_plan),
        memory_views=list(current.policy.memory_views),
        workflow_steps=list(current.policy.workflow_steps),
        force_restart=False,
    )
    with pytest.raises(InvalidP2bPolicy, match="change direction"):
        P2bPolicyVersion.from_response(
            version_id="v002",
            parent=current,
            response=unchanged,
            allowed_base_candidate_ids={"p2-best", "reference"},
            require_direction_change=True,
        )


def test_policy_rejects_private_paths_unknown_bases_and_unstructured_text() -> None:
    current = initial_policy(
        strategy="counterfactual",
        starting_candidate_id="p2-best",
    )
    with pytest.raises(InvalidP2bPolicy, match="absolute path"):
        P2bPolicyVersion.from_response(
            version_id="v002",
            parent=current,
            response=_response(observed_evidence=["read /tmp/private/raw.log"]),
            allowed_base_candidate_ids={"p2-best", "reference"},
        )
    with pytest.raises(InvalidP2bPolicy, match="base candidate"):
        P2bPolicyVersion.from_response(
            version_id="v002",
            parent=current,
            response=_response(base_candidate_id="other-lane-secret"),
            allowed_base_candidate_ids={"p2-best", "reference"},
        )
    with pytest.raises(InvalidP2bPolicy, match="JSON"):
        P2bPolicyVersion.from_response(
            version_id="v002",
            parent=current,
            response="try something faster",
            allowed_base_candidate_ids={"p2-best", "reference"},
        )


def test_policy_accepts_one_json_fence_without_repair_model_call() -> None:
    current = initial_policy(
        strategy="profile_exploit",
        starting_candidate_id="p2-best",
    )
    version = P2bPolicyVersion.from_response(
        version_id="v002",
        parent=current,
        response=f"```json\n{_response()}\n```",
        allowed_base_candidate_ids={"p2-best", "reference"},
        require_direction_change=True,
    )

    assert version.policy.base_candidate_id == "reference"


def test_score_trend_exposes_raw_score_and_marks_sub_two_percent_as_noise() -> None:
    trend = ScoreTrend.build(
        current_score=4.04,
        previous_score=4.0,
        historical_best=4.1,
        starting_score=3.8,
    )

    assert trend.current_score == 4.04
    assert trend.delta_vs_previous_pct == pytest.approx(1.0)
    assert trend.delta_vs_best_pct == pytest.approx(-1.4634146)
    assert trend.delta_vs_start_pct == pytest.approx(6.3157894)
    assert trend.in_noise_band
    assert not trend.significant_improvement
