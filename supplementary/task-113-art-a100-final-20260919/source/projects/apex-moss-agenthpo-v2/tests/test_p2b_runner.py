from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from optimization_lab.adapters.base import EvaluationResult, EvaluationStatus
from optimization_lab.adapters.fake import FakeAdapter
from optimization_lab.generation import GenerationResult
from optimization_lab.p2b_dashboard import P2bDashboard
from optimization_lab.p2b_plan import FrozenCandidate, P2bPlan
from optimization_lab.p2b_runner import P2bCampaignRunner
from optimization_lab.profiling import FakeProfiler, ProfileSummary
from optimization_lab.registry import ExperimentRegistry
from optimization_lab.task_spec import TaskSpec


TASKS = ("kernelbench_layernorm", "kernelbench_matmul_sigmoid_sum")


class CandidateGenerator:
    def __init__(self) -> None:
        self.calls: list[str] = []

    def estimated_api_cost_usd(self) -> float:
        return 0.0

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        self.calls.append(prompt)
        match = re.search(r"candidate_id: ([A-Za-z0-9._-]+)", prompt)
        assert match
        candidate_id = match.group(1)
        return GenerationResult(
            raw_response=(
                "```python\n"
                "class ModelNew:\n"
                f"    candidate_id = {candidate_id!r}\n"
                "```\n"
            ),
            provider="fake-candidate",
        )


class PolicyGenerator:
    def __init__(self) -> None:
        self.calls: list[str] = []

    def estimated_api_cost_usd(self) -> float:
        return 0.0

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        self.calls.append(prompt)
        match = re.search(
            r"MACHINE_CONSTRAINTS_JSON\n```json\n(.*?)\n```", prompt, re.DOTALL
        )
        assert match
        constraints = json.loads(match.group(1))
        current = constraints["current_policy"]
        allowed = constraints["allowed_base_candidate_ids"]
        alternatives = [item for item in allowed if item != current["base_candidate_id"]]
        base = alternatives[0] if constraints["require_restart"] else current["base_candidate_id"]
        modes = [
            "profile_exploit",
            "architecture_reset",
            "counterfactual",
            "recombinant_frontier",
        ]
        mode = modes[(modes.index(current["mode"]) + 1) % len(modes)]
        response = {
            "mode": mode,
            "base_candidate_id": base,
            "diagnostic_level": "light",
            "observed_evidence": [
                "The current score and its deltas were inspected before choosing this policy."
            ],
            "primary_hypothesis": "The previous dataflow is not using the fixed shape efficiently.",
            "score_assessment": "There is no two-percent improvement over the relevant best score.",
            "direction_change_reason": "Change the outer search direction instead of repeating local launch tuning.",
            "mutation_scope": ["kernel_count", "reduction_structure", "thread_mapping"],
            "enabled_skills": [
                "task_semantics",
                "score_trend",
                "architecture_rebuild",
                "novelty_check",
            ],
            "tool_plan": ["score", "static_structure"],
            "memory_views": [
                "starting_point",
                "historical_best",
                "structurally_novel",
                "disproved_ideas",
            ],
            "workflow_steps": [
                "Inspect the current score and historical deltas.",
                "Change the bottleneck hypothesis and Kernel structure.",
                "Generate one complete candidate and send it through the gates.",
            ],
            "avoid_repeats": ["Do not only change num_warps or num_stages."],
            "kernel_instructions": [
                "Change the Kernel's primary dataflow.",
                "Preserve task semantics and numerical correctness.",
            ],
            "force_restart": constraints["require_restart"],
            "structural_change": constraints["require_structural_change"],
        }
        return GenerationResult(
            raw_response=json.dumps(response), provider="fake-policy"
        )


def _task(task_id: str, level: int, problem_id: int) -> TaskSpec:
    return TaskSpec(
        task_id=task_id,
        display_name=task_id,
        level=level,
        problem_id=problem_id,
        task_path=f"KernelBench/level{level}/task.py",
        task_sha256="a" * 64,
        repository_commit="b" * 40,
        target_gpu="A100",
        gpu_arch="Ampere",
    )


def _plan(tmp_path: Path) -> P2bPlan:
    source = tmp_path / "source"
    frozen = []
    for task_id in TASKS:
        for phase, name, score in (
            ("p1", "p1", 3.0),
            ("p2", "r00", 3.5),
            ("p2", "r01", 4.0),
            ("p2", "r02", 3.8),
        ):
            candidate_id = f"{task_id.removeprefix('kernelbench_')}-{name}"
            path = source / f"{candidate_id}.py"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                f"class ModelNew:\n    source = {candidate_id!r}\n",
                encoding="utf-8",
            )
            frozen.append(
                FrozenCandidate(
                    task_id=task_id,
                    source_phase=phase,
                    candidate_id=candidate_id,
                    source_path=str(path),
                    source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                    speedup=score,
                )
            )
    return P2bPlan.build(
        artifact_root=tmp_path / "p2b",
        source_artifact_root=source,
        executor_model="fixed-model",
        frozen_candidates=tuple(frozen),
    )


def _common(tmp_path: Path) -> tuple[P2bPlan, dict[str, object]]:
    plan = _plan(tmp_path)
    root = Path(plan.artifact_root)
    plan.write(root / "p2b_plan.json")
    candidate_generator = CandidateGenerator()
    policy_generator = PolicyGenerator()
    adapter = FakeAdapter(
        EvaluationResult(
            status=EvaluationStatus.VALID,
            compiled=True,
            correct=True,
            candidate_runtime_ms=2.0,
            reference_runtime_ms=4.0,
            gpu_seconds=1.0,
            hardware="fake A100",
        )
    )
    profile_template = ProfileSummary(
        task_id="kernelbench_layernorm",
        candidate_id="template",
        candidate_sha256="c" * 64,
        level="light",
        status="partial",
        candidate_runtime_ms=2.0,
        reference_runtime_ms=4.0,
        speedup=2.0,
        structural_signature="template",
        missing_metrics=(
            "registers_per_thread",
            "register_spills",
            "shared_memory_bytes",
            "achieved_occupancy_pct",
            "dram_throughput_pct",
            "l2_hit_rate_pct",
            "warp_stall_summary",
        ),
        gpu_seconds=0.25,
    )
    profiler = FakeProfiler(profile_template)
    tasks = {
        "kernelbench_layernorm": _task("kernelbench_layernorm", 1, 40),
        "kernelbench_matmul_sigmoid_sum": _task(
            "kernelbench_matmul_sigmoid_sum", 2, 56
        ),
    }
    common: dict[str, object] = {
        "plan": plan,
        "registry": ExperimentRegistry(root),
        "dashboard": P2bDashboard(root / "dashboard.html"),
        "candidate_generator": candidate_generator,
        "policy_generator": policy_generator,
        "adapter": adapter,
        "profiler": profiler,
        "tasks": tasks,
        "task_cards": {task_id: "task card" for task_id in tasks},
        "reference_sources": {task_id: "class Model: pass" for task_id in tasks},
    }
    return plan, common


def test_p2b_dashboard_renders_incorrect_round_without_profile(
    tmp_path: Path,
) -> None:
    root = tmp_path / "p2b"
    root.mkdir()
    lane_id = "p2b:kernelbench_layernorm:architecture_reset"
    (root / "p2b_plan.json").write_text(
        json.dumps(
            {
                "lanes": [
                    {
                        "lane_id": lane_id,
                        "task_id": "kernelbench_layernorm",
                        "strategy": "architecture_reset",
                        "starting_score": 1.0,
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    registry = ExperimentRegistry(root)
    registry.append(
        "p2b_round_completed",
        {
            "lane_id": lane_id,
            "round_number": 1,
            "candidate_id": "layernorm-v001",
            "feedback": {
                "correct": True,
                "gpu_seconds": 1.0,
                "speedup_vs_eager": 2.0,
            },
            "score_trend": {"delta_vs_best_pct": 100.0},
            "profile": {"level": "full"},
        },
        event_id="round:correct-with-profile",
    )
    registry.append(
        "p2b_round_completed",
        {
            "lane_id": lane_id,
            "round_number": 2,
            "candidate_id": "layernorm-v002",
            "feedback": {
                "correct": False,
                "gpu_seconds": 1.0,
                "speedup_vs_eager": None,
            },
            "score_trend": {"delta_vs_best_pct": None},
            "profile": None,
        },
        event_id="round:incorrect-without-profile",
    )
    registry.append(
        "p2b_candidate_generated",
        {
            "lane_id": lane_id,
            "round_number": 3,
            "candidate_id": "layernorm-v003",
            "policy_version_id": "v003",
        },
        event_id="candidate:generated-before-interruption",
    )
    registry.append(
        "candidate_evaluated",
        {
            "feedback": {
                "candidate_id": "layernorm-v003",
                "correct": True,
                "gpu_seconds": 1.0,
                "speedup_vs_eager": 3.0,
            },
        },
        event_id="candidate:scored-before-interruption",
    )

    output_path = root / "dashboard.html"
    P2bDashboard(output_path).render(registry)

    page = output_path.read_text(encoding="utf-8")
    assert "2 / 8" in page
    assert "<td>—</td>" in page
    assert "Harness 逐轮分数曲线" in page
    assert 'data-round="0" data-score="1.000000"' in page
    assert 'data-round="1" data-score="2.000000"' in page
    assert 'data-round="2" data-outcome="incorrect"' in page
    assert 'data-round="3" data-score="3.000000"' in page
    assert "layernorm-v001" in page
    assert "layernorm-v002" in page
    assert "layernorm-v003" in page
    assert "评分已保存；轮次未封存" in page


def test_p2b_runs_eight_broad_search_lanes_and_stops_before_p3(
    tmp_path: Path,
) -> None:
    plan, common = _common(tmp_path)
    summary = P2bCampaignRunner(**common).run()

    assert summary == {
        "lane_count": 8,
        "round_count": 64,
        "correct_count": 64,
        "candidate_model_calls": 64,
        "policy_model_calls": 56,
        "profile_count": 64,
    }
    assert len(common["candidate_generator"].calls) == 64  # type: ignore[union-attr]
    assert len(common["policy_generator"].calls) == 56  # type: ignore[union-attr]
    assert len(common["adapter"].calls) == 64  # type: ignore[union-attr]
    assert len(common["profiler"].calls) == 64  # type: ignore[union-attr]

    events = common["registry"].read_events()  # type: ignore[union-attr]
    completed = [event for event in events if event["event_type"] == "p2b_lane_completed"]
    assert len(completed) == 8
    assert {event["payload"]["rounds"] for event in completed} == {8}
    assert not any(event["event_type"].startswith("p3") for event in events)
    restarts = [
        event
        for event in events
        if event["event_type"] == "p2b_policy_generated"
        and event["payload"]["policy"]["force_restart"]
    ]
    assert len(restarts) == 6
    assert {event["payload"]["round_number"] for event in restarts} == {6}
    structural = [
        event
        for event in events
        if event["event_type"] == "p2b_round_completed"
        and event["payload"]["policy"]["structural_change"]
    ]
    assert len(structural) >= 8 * 4
    assert all(
        "score_trend" in event["payload"]["policy"]["enabled_skills"]
        for event in structural
    )

    page = (Path(plan.artifact_root) / "dashboard.html").read_text(encoding="utf-8")
    assert "P2B 已完成，P3 待授权" in page
    assert page.count("8 / 8") == 8
    assert "120 / 120" in page


def test_p2b_resume_makes_no_new_model_gpu_or_profiler_calls(tmp_path: Path) -> None:
    plan, common = _common(tmp_path)
    first = P2bCampaignRunner(**common).run()

    resumed_candidates = CandidateGenerator()
    resumed_policies = PolicyGenerator()
    resumed_adapter = FakeAdapter(common["adapter"].result)  # type: ignore[union-attr]
    resumed_profiler = FakeProfiler(common["profiler"].template)  # type: ignore[union-attr]
    resumed = P2bCampaignRunner(
        **{
            **common,
            "candidate_generator": resumed_candidates,
            "policy_generator": resumed_policies,
            "adapter": resumed_adapter,
            "profiler": resumed_profiler,
        }
    )

    assert resumed.run() == first
    assert resumed_candidates.calls == []
    assert resumed_policies.calls == []
    assert resumed_adapter.calls == []
    assert resumed_profiler.calls == []


def test_p2b_policy_prompt_always_contains_current_score_trend(tmp_path: Path) -> None:
    _, common = _common(tmp_path)
    P2bCampaignRunner(**common).run()

    prompts = common["policy_generator"].calls  # type: ignore[union-attr]
    assert prompts
    assert all('"current_score": 2.0' in prompt for prompt in prompts)
    assert all('"starting_score"' in prompt for prompt in prompts)
    assert all("If the score did not improve" in prompt for prompt in prompts)
    assert all("private_evaluator" not in prompt for prompt in prompts)
