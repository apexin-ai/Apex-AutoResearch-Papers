import json
from pathlib import Path

import pytest

from optimization_lab.feedback import FeedbackCard
from optimization_lab.generation import (
    CandidateArchive,
    GeneratedCandidate,
    GenerationRequest,
    InvalidCandidate,
)


VALID_RESPONSE = """I used one fused Triton kernel.
```python
import torch
import torch.nn as nn

class ModelNew(nn.Module):
    def forward(self, x):
        return x
```
"""


def _feedback(task_id: str = "kernelbench_layernorm") -> FeedbackCard:
    return FeedbackCard(
        task_id=task_id,
        candidate_id="r00-v001",
        outcome="compile_failed",
        valid_run=True,
        stage_reached="compile",
        compiled=False,
        correct=False,
        speedup_vs_eager=None,
        candidate_runtime_ms=None,
        reference_runtime_ms=None,
        error_summary=(
            "failure in /home/private/private_evaluator/r00-v001/raw.log: syntax error"
        ),
        next_action="repair syntax",
        gpu_seconds=3.0,
        hardware="A100",
    )


def test_generated_candidate_extracts_one_complete_python_block() -> None:
    candidate = GeneratedCandidate.from_response(VALID_RESPONSE)

    assert "class ModelNew" in candidate.code
    assert len(candidate.sha256) == 64
    assert candidate.raw_response == VALID_RESPONSE


@pytest.mark.parametrize(
    "response, message",
    [
        ("no code here", "exactly one"),
        (VALID_RESPONSE + "\n```python\npass\n```", "exactly one"),
        ("```python\nclass Other: pass\n```", "ModelNew"),
        ("```python\nclass ModelNew(:\n```", "syntax"),
    ],
)
def test_generated_candidate_rejects_ambiguous_or_invalid_output(
    response: str,
    message: str,
) -> None:
    with pytest.raises(InvalidCandidate, match=message):
        GeneratedCandidate.from_response(response)


def test_generation_request_contains_only_short_sanitized_feedback() -> None:
    request = GenerationRequest(
        task_id="kernelbench_layernorm",
        lane_id="p2:kernelbench_layernorm:r00",
        harness_text="# specialist harness",
        task_card="# LayerNorm task card",
        reference_source="class Model: pass",
        feedback_history=(_feedback(),),
        previous_candidate="class ModelNew: pass",
    )

    prompt = request.to_prompt()

    assert "# specialist harness" in prompt
    assert "# LayerNorm task card" in prompt
    assert "class Model: pass" in prompt
    assert "compile_failed" in prompt
    assert "<private-path>" in prompt
    assert "/home/private" not in prompt
    assert "raw.log" not in prompt


def test_generation_request_rejects_feedback_from_another_task() -> None:
    with pytest.raises(ValueError, match="feedback task"):
        GenerationRequest(
            task_id="kernelbench_layernorm",
            lane_id="lane",
            harness_text="harness",
            task_card="card",
            reference_source="source",
            feedback_history=(_feedback("other_task"),),
        )


def test_candidate_archive_is_idempotent_and_refuses_overwrite(tmp_path: Path) -> None:
    archive = CandidateArchive(tmp_path, "lineages/kernelbench_layernorm/r00")
    candidate = GeneratedCandidate.from_response(VALID_RESPONSE)

    first = archive.store("r00-v001", candidate)
    second = archive.store("r00-v001", candidate)

    assert first == second
    assert Path(first["candidate_path"]).read_text() == candidate.code
    assert Path(first["raw_response_path"]).read_text() == VALID_RESPONSE
    metadata = json.loads(Path(first["metadata_path"]).read_text())
    assert metadata["candidate_sha256"] == candidate.sha256

    changed = GeneratedCandidate.from_response(
        VALID_RESPONSE.replace("return x", "return x + 1")
    )
    with pytest.raises(ValueError, match="different content"):
        archive.store("r00-v001", changed)


def test_candidate_archive_rejects_unsafe_scope_and_candidate_id(
    tmp_path: Path,
) -> None:
    with pytest.raises(ValueError, match="scope"):
        CandidateArchive(tmp_path, "../../outside")
    archive = CandidateArchive(tmp_path, "lineages/task/r00")

    with pytest.raises(ValueError, match="candidate id"):
        archive.store("../outside", GeneratedCandidate.from_response(VALID_RESPONSE))
