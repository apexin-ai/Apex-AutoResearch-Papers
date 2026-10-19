from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from optimization_lab.harness_builder.adapters.lcbench import (
    LCBenchAdapter,
    LCBenchTask,
)
from optimization_lab.harness_builder.evaluation import LCBenchEvaluationBackend
from optimization_lab.harness_builder.solutions import (
    LCBenchSolutionCodec,
    SolutionContractError,
)


INSTANCE_ID = "167168"


def _queries() -> list[dict[str, int | float]]:
    return [
        {
            "batch_size": 16 + index,
            "learning_rate": 0.00010000000000000009 * (index + 1),
            "max_dropout": index / 20,
            "max_units": 64 + index,
            "momentum": 0.1 + index / 100,
            "num_layers": 1 + index % 5,
            "weight_decay": 0.00001 * (index + 1),
        }
        for index in range(16)
    ]


def _candidate(*, instance_id: str = INSTANCE_ID) -> str:
    return json.dumps(
        {
            "schema_version": 1,
            "instance_id": instance_id,
            "queries": _queries(),
        }
    )


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _task(tmp_path: Path) -> LCBenchTask:
    data_root = tmp_path / "lcbench"
    data_root.mkdir()
    model = data_root / "model.onnx"
    config = data_root / "config_space.json"
    encoding = data_root / "encoding.json"
    model.write_bytes(b"pinned-model")
    config.write_text("{}\n", encoding="utf-8")
    encoding.write_text("{}\n", encoding="utf-8")
    settings = tmp_path / "yahpo.yaml"
    settings.write_text(f"data_path: {tmp_path}\n", encoding="utf-8")
    return LCBenchTask(
        instance_id=INSTANCE_ID,
        data_root=data_root,
        settings_path=settings,
        python_executable=Path("/usr/bin/python3"),
        model_sha256=_sha(model),
        config_space_sha256=_sha(config),
        encoding_sha256=_sha(encoding),
        settings_sha256=_sha(settings),
    )


def test_lcbench_codec_accepts_only_one_bound_canonical_query_batch() -> None:
    codec = LCBenchSolutionCodec(instance_id=INSTANCE_ID)
    artifact = codec.parse(f"```json\n{_candidate()}\n```")

    payload = json.loads(artifact.text)
    assert artifact.extension == ".json"
    assert payload["instance_id"] == INSTANCE_ID
    assert len(payload["queries"]) == 16
    assert "epoch" not in payload["queries"][0]

    with pytest.raises(SolutionContractError, match="instance"):
        codec.parse(_candidate(instance_id="34539"))

    duplicate = json.loads(_candidate())
    duplicate["queries"][1] = duplicate["queries"][0]
    with pytest.raises(SolutionContractError, match="unique"):
        codec.parse(json.dumps(duplicate))

    out_of_range = json.loads(_candidate())
    out_of_range["queries"][0]["batch_size"] = 8
    with pytest.raises(SolutionContractError, match="batch_size"):
        codec.parse(json.dumps(out_of_range))

    injected_fidelity = json.loads(_candidate())
    injected_fidelity["queries"][0]["epoch"] = 1
    with pytest.raises(SolutionContractError, match="keys"):
        codec.parse(json.dumps(injected_fidelity))


def test_lcbench_adapter_scores_trusted_batch_and_keeps_test_metric_private(
    tmp_path: Path,
) -> None:
    task = _task(tmp_path)
    artifact = LCBenchSolutionCodec(instance_id=INSTANCE_ID).parse(_candidate())
    artifact_path = tmp_path / "candidate.json"
    artifact_path.write_text(artifact.text, encoding="utf-8")
    observed: list[dict[str, object]] = []

    def objective(configs: list[dict[str, object]]) -> list[dict[str, float]]:
        observed.extend(configs)
        return [
            {
                "time": 10.0 + index,
                "val_accuracy": 50.0 + index,
                "val_cross_entropy": 1.0,
                "val_balanced_accuracy": 0.50 + index / 100,
                "test_cross_entropy": 1.1,
                "test_balanced_accuracy": 0.49 + index / 100,
            }
            for index in range(len(configs))
        ]

    adapter = LCBenchAdapter(task=task, objective=objective)
    result = adapter.evaluate(artifact_path, tmp_path / "private.json")

    assert len(observed) == 16
    assert all(config["OpenML_task_id"] == INSTANCE_ID for config in observed)
    assert all(config["epoch"] == 52 for config in observed)
    assert result.correct is True
    assert result.best_validation_score == pytest.approx(0.65)
    assert result.best_test_score == pytest.approx(0.64)
    private = json.loads((tmp_path / "private.json").read_text(encoding="utf-8"))
    assert private["best_test_score"] == pytest.approx(0.64)

    normalized = LCBenchEvaluationBackend(adapter=adapter).evaluate(
        artifact_path, tmp_path / "round-private"
    )
    assert normalized.correct is True
    assert normalized.score == pytest.approx(0.65)
    assert normalized.public_feedback["best_validation_score"] == pytest.approx(0.65)
    assert "best_test_score" not in normalized.public_feedback


def test_lcbench_adapter_fails_closed_on_source_drift(tmp_path: Path) -> None:
    task = _task(tmp_path)
    (task.data_root / "model.onnx").write_bytes(b"drifted-model")
    artifact = LCBenchSolutionCodec(instance_id=INSTANCE_ID).parse(_candidate())
    artifact_path = tmp_path / "candidate.json"
    artifact_path.write_text(artifact.text, encoding="utf-8")

    adapter = LCBenchAdapter(task=task, objective=lambda _: [])
    with pytest.raises(RuntimeError, match="model.onnx digest"):
        adapter.evaluate(artifact_path, tmp_path / "private.json")
