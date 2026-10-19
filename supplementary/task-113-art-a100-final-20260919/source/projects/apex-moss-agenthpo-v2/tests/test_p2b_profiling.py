from __future__ import annotations

from pathlib import Path

import pytest

from optimization_lab.feedback import FeedbackCard
from optimization_lab.profiling import (
    FakeProfiler,
    InvalidProfileSummary,
    ProfileSummary,
    static_structure_signature,
)
from optimization_lab.task_spec import TaskSpec


def _task() -> TaskSpec:
    return TaskSpec(
        task_id="kernelbench_layernorm",
        display_name="LayerNorm",
        level=1,
        problem_id=40,
        task_path="KernelBench/level1/40_LayerNorm.py",
        task_sha256="a" * 64,
        repository_commit="b" * 40,
        target_gpu="A100",
        gpu_arch="Ampere",
    )


def _card() -> FeedbackCard:
    return FeedbackCard(
        task_id="kernelbench_layernorm",
        candidate_id="candidate-v001",
        outcome="valid",
        valid_run=True,
        stage_reached="performance",
        compiled=True,
        correct=True,
        speedup_vs_eager=4.0,
        candidate_runtime_ms=2.0,
        reference_runtime_ms=8.0,
        error_summary="",
        next_action="compare",
        gpu_seconds=2.0,
        hardware="A100",
    )


def test_profile_summary_cannot_fabricate_unavailable_hardware_counters() -> None:
    with pytest.raises(InvalidProfileSummary, match="unavailable"):
        ProfileSummary(
            task_id="kernelbench_layernorm",
            candidate_id="candidate-v001",
            candidate_sha256="c" * 64,
            level="full",
            status="complete",
            candidate_runtime_ms=2.0,
            reference_runtime_ms=8.0,
            speedup=4.0,
            structural_signature="sig",
            achieved_occupancy_pct=80.0,
            missing_metrics=("achieved_occupancy_pct",),
        )

    summary = ProfileSummary(
        task_id="kernelbench_layernorm",
        candidate_id="candidate-v001",
        candidate_sha256="c" * 64,
        level="full",
        status="partial",
        candidate_runtime_ms=2.0,
        reference_runtime_ms=8.0,
        speedup=4.0,
        structural_signature="sig",
        registers_per_thread=48,
        missing_metrics=(
            "achieved_occupancy_pct",
            "dram_throughput_pct",
            "l2_hit_rate_pct",
            "warp_stall_summary",
        ),
    )
    public = summary.to_public_dict()
    assert public["registers_per_thread"] == 48
    assert public["achieved_occupancy_pct"] is None
    assert "/" not in str(public)


def test_fake_profiler_and_static_signature_are_deterministic(tmp_path: Path) -> None:
    candidate = tmp_path / "candidate.py"
    candidate.write_text(
        """import triton
import triton.language as tl

@triton.jit
def kernel(x):
    return

class ModelNew:
    pass
""",
        encoding="utf-8",
    )
    signature = static_structure_signature(candidate.read_text(encoding="utf-8"))
    assert signature["triton_kernel_count"] == 1
    assert signature["uses_autotune"] is False

    template = ProfileSummary(
        task_id="kernelbench_layernorm",
        candidate_id="template",
        candidate_sha256="d" * 64,
        level="light",
        status="complete",
        candidate_runtime_ms=2.0,
        reference_runtime_ms=8.0,
        speedup=4.0,
        structural_signature="sig",
    )
    profiler = FakeProfiler(template)
    result = profiler.profile(
        task=_task(),
        candidate_path=candidate,
        candidate_id="candidate-v001",
        feedback=_card(),
        level="light",
        private_log_dir=tmp_path / "private",
    )

    assert result.candidate_id == "candidate-v001"
    assert result.candidate_sha256 != template.candidate_sha256
    assert result.level == "light"
    assert len(profiler.calls) == 1
