from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import pytest

from optimization_lab.harness_builder.three_arm_prepare import THREE_ARM_SUITES
from optimization_lab.harness_builder.three_arm_report import (
    generate_three_arm_composite_report,
    generate_three_arm_report,
)


ARMS = ("A", "B-frozen", "B-online")


def _write(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _build_campaign(artifact_root: Path, *, task_count: int = 24) -> None:
    stream_index = 0
    for suite_index, suite in enumerate(THREE_ARM_SUITES):
        for task_index in range(8):
            if stream_index >= task_count:
                return
            task_id = f"task-{task_index + 1:02d}"
            instance_id = f"{suite}:{task_id}"
            root = (
                artifact_root
                / "formal"
                / "instances"
                / f"{stream_index:03d}-{hashlib.sha256(instance_id.encode()).hexdigest()}"
            )
            item = {
                "stream_index": stream_index,
                "block_index": task_index,
                "suite": suite,
                "task_id": task_id,
                "instance_id": instance_id,
                "arm_order": list(ARMS),
                "learning_mode": "online" if task_index < 6 else "sealed",
            }
            frozen_score = float((suite_index + 1) * 10)
            arm_receipt_sha256s: dict[str, str] = {}
            for arm in ARMS:
                if arm == "A":
                    score = frozen_score - 1.0
                elif arm == "B-frozen":
                    score = frozen_score
                else:
                    score = frozen_score + task_index + 1.0
                rounds = [
                    {
                        "score": score,
                        "running_best": score,
                        "correct": True,
                        "rule_id": "discipline",
                    }
                    for _ in range(8)
                ]
                # One invalid attempt remains in the reliability denominator but must
                # not enter the valid-only performance mean.
                if suite_index == 0 and task_index == 7 and arm == "B-online":
                    rounds[0]["score"] = None
                    rounds[0]["correct"] = False
                numeric_scores = [
                    float(point["score"])
                    for point in rounds
                    if point["correct"] and point["score"] is not None
                ]
                arm_path = root / "arms" / f"{arm}.json"
                _write(
                    arm_path,
                    {
                        "curve": {
                            "initial_score": rounds[0]["score"],
                            "final_best": max(numeric_scores),
                            "evolution_gain": 0.0,
                            "cross_instance_record_ids": [],
                            "rounds": rounds,
                        }
                    },
                )
                arm_receipt_sha256s[arm] = _sha256(arm_path)
            _write(
                root / "instance_receipt.json",
                {
                    "stream_item": item,
                    "arm_receipt_sha256s": arm_receipt_sha256s,
                },
            )
            stream_index += 1


def test_report_uses_valid_only_task_means_and_suite_growth(tmp_path: Path) -> None:
    artifact_root = tmp_path / "campaign"
    _build_campaign(artifact_root)

    summary = generate_three_arm_report(
        artifact_root=artifact_root, output_root=tmp_path / "report"
    )

    assert summary["task_count"] == 24
    assert summary["task_mean_definition"]["valid_only"] is True
    assert summary["validity_policy"]["minimum_valid_rounds_per_arm"] == 4
    assert summary["validity_policy"]["minimum_paired_learning_tasks"] == 5
    assert len(summary["task_results"]) == 24
    yahpo = summary["benchmarks"][0]
    assert yahpo["suite"] == THREE_ARM_SUITES[0]
    assert yahpo["learning"]["mean_online_minus_frozen"] == pytest.approx(3.5)
    assert yahpo["learning"]["online_advantage_slope_per_task"] == pytest.approx(1.0)
    assert yahpo["learning"]["first_to_sixth_advantage_change"] == pytest.approx(5.0)
    # Sealed task 8 has seven valid scores of 18 and one invalid attempt. The
    # invalid attempt remains visible but does not shrink the performance value.
    assert summary["task_results"][7]["B-online_valid_mean"] == pytest.approx(18.0)
    assert summary["task_results"][7]["B-online_best_score"] == pytest.approx(18.0)
    assert summary["task_results"][7]["B-online_valid_rounds"] == 7
    assert summary["task_results"][7]["online_minus_frozen"] == pytest.approx(8.0)
    assert summary["cross_benchmark"]["raw_scores_combined"] is False
    assert summary["cross_benchmark"]["comparison_metric"] == "relative_online_advantage"
    assert {
        path.name for path in (tmp_path / "report").iterdir()
    } == {
        "score_curve.html",
        "score_curve.json",
        "summary.json",
        "summary.md",
        "results.csv",
    }


def _set_valid_rounds(
    artifact_root: Path, *, suite: str, task_index: int, arm: str, valid: int
) -> None:
    for receipt_path in (artifact_root / "formal" / "instances").glob(
        "*/instance_receipt.json"
    ):
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        item = receipt["stream_item"]
        if item["suite"] == suite and int(item["block_index"]) + 1 == task_index:
            arm_path = receipt_path.parent / "arms" / f"{arm}.json"
            payload = json.loads(arm_path.read_text(encoding="utf-8"))
            for index, point in enumerate(payload["curve"]["rounds"]):
                if index >= valid:
                    point["score"] = None
                    point["correct"] = False
            _write(arm_path, payload)
            return
    raise AssertionError("fixture task not found")


def test_report_requires_four_valid_rounds_and_five_paired_learning_tasks(
    tmp_path: Path,
) -> None:
    artifact_root = tmp_path / "campaign"
    _build_campaign(artifact_root)
    suite = THREE_ARM_SUITES[0]
    _set_valid_rounds(
        artifact_root, suite=suite, task_index=1, arm="B-frozen", valid=3
    )
    _set_valid_rounds(
        artifact_root, suite=suite, task_index=2, arm="B-online", valid=3
    )

    summary = generate_three_arm_report(
        artifact_root=artifact_root, output_root=tmp_path / "report"
    )

    first, second = summary["task_results"][:2]
    assert first["B-frozen_validity_status"] == "insufficient_validity"
    # Descriptive values remain visible even below the 4/8 inferential gate.
    assert first["B-frozen_valid_mean"] == pytest.approx(10.0)
    assert first["B-frozen_best_score"] == pytest.approx(10.0)
    assert first["online_minus_frozen"] is None
    assert second["B-online_validity_status"] == "insufficient_validity"
    assert second["B-online_valid_mean"] == pytest.approx(12.0)
    learning = summary["benchmarks"][0]["learning"]
    assert learning["paired_valid_task_count"] == 4
    assert learning["validity_status"] == "insufficient_validity"
    assert learning["mean_online_minus_frozen"] is None
    assert learning["online_advantage_slope_per_task"] is None


def test_report_refuses_partial_campaign_before_writing_outputs(tmp_path: Path) -> None:
    artifact_root = tmp_path / "campaign"
    output_root = tmp_path / "report"
    _build_campaign(artifact_root, task_count=23)

    with pytest.raises(RuntimeError, match="fully sealed"):
        generate_three_arm_report(artifact_root=artifact_root, output_root=output_root)

    assert not output_root.exists()


def _build_composition_manifest(
    tmp_path: Path,
) -> tuple[Path, dict[str, Path], dict[str, object]]:
    prefix_root = tmp_path / "v1r8"
    successor_root = tmp_path / "v1r9"
    # Both fixtures contain a complete tree so the test also proves that the
    # report follows the manifest rather than scanning or copying either root.
    _build_campaign(prefix_root)
    _build_campaign(successor_root)
    segment_roots = {
        "v1r8-prefix": prefix_root,
        "v1r9-successor": successor_root,
    }
    instances: list[dict[str, object]] = []
    for stream_index in range(24):
        segment = "v1r8-prefix" if stream_index < 6 else "v1r9-successor"
        root = segment_roots[segment]
        receipt_path = next(
            path
            for path in (root / "formal" / "instances").glob(
                "*/instance_receipt.json"
            )
            if json.loads(path.read_text(encoding="utf-8"))["stream_item"][
                "stream_index"
            ]
            == stream_index
        )
        instances.append(
            {
                "stream_index": stream_index,
                "source_segment": segment,
                "instance_receipt": {
                    "relative_path": receipt_path.relative_to(root).as_posix(),
                    "sha256": _sha256(receipt_path),
                },
            }
        )
    payload: dict[str, object] = {
        "schema_version": 1,
        "kind": "three_arm_composition_manifest",
        "prefix_length": 6,
        "segments": [
            {"segment_id": "v1r8-prefix", "role": "source_prefix"},
            {"segment_id": "v1r9-successor", "role": "successor_suffix"},
        ],
        "instances": instances,
        "excluded_consumed_tail": [
            {
                "source_segment": "v1r8-prefix",
                "instance_id": "swebench-verified:scikit-learn-14983",
                "reason": "excluded_abandoned_successor_tail",
                "model_calls": 3,
                "evaluator_transactions": 0,
                "learning_import": False,
                "performance_import": False,
            }
        ],
    }
    manifest_path = tmp_path / "composition_manifest.json"
    _write(manifest_path, payload)
    return manifest_path, segment_roots, payload


def test_composite_report_references_two_segments_and_emits_72_arm_rows(
    tmp_path: Path,
) -> None:
    manifest_path, segment_roots, _payload = _build_composition_manifest(tmp_path)
    output_root = tmp_path / "report"

    summary = generate_three_arm_composite_report(
        composition_manifest_path=manifest_path,
        segment_roots=segment_roots,
        output_root=output_root,
    )

    assert summary["task_count"] == 24
    assert summary["arm_result_count"] == 72
    assert summary["total_round_count"] == 576
    assert len(summary["task_results"]) == 24
    assert len(summary["arm_results"]) == 72
    assert [row["source_segment"] for row in summary["task_results"][:7]] == [
        "v1r8-prefix",
        "v1r8-prefix",
        "v1r8-prefix",
        "v1r8-prefix",
        "v1r8-prefix",
        "v1r8-prefix",
        "v1r9-successor",
    ]
    assert all(
        len(str(row["instance_receipt_sha256"])) == 64
        for row in summary["task_results"]
    )
    assert summary["excluded_consumed_tail"][0]["instance_id"].endswith(
        "scikit-learn-14983"
    )
    assert not any(
        "scikit-learn-14983" in str(row["instance_id"])
        for row in summary["task_results"]
    )
    with (output_root / "results.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 72
    assert {row["arm"] for row in rows} == set(ARMS)
    # The composition output contains references and metrics, never copied
    # source receipts or arm artifacts.
    assert not (output_root / "formal").exists()


def test_composite_report_shows_descriptive_values_below_validity_gate(
    tmp_path: Path,
) -> None:
    manifest_path, segment_roots, payload = _build_composition_manifest(tmp_path)
    entry = payload["instances"][6]
    receipt_ref = entry["instance_receipt"]
    receipt_path = (
        segment_roots[entry["source_segment"]] / receipt_ref["relative_path"]
    )
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    arm_path = receipt_path.parent / "arms" / "B-online.json"
    arm_payload = json.loads(arm_path.read_text(encoding="utf-8"))
    for point in arm_payload["curve"]["rounds"][3:]:
        point["score"] = None
        point["correct"] = False
    _write(arm_path, arm_payload)
    receipt["arm_receipt_sha256s"]["B-online"] = _sha256(arm_path)
    _write(receipt_path, receipt)
    receipt_ref["sha256"] = _sha256(receipt_path)
    _write(manifest_path, payload)

    summary = generate_three_arm_composite_report(
        composition_manifest_path=manifest_path,
        segment_roots=segment_roots,
        output_root=tmp_path / "report",
    )

    row = summary["task_results"][6]
    assert row["B-online_valid_rounds"] == 3
    assert row["B-online_validity_status"] == "insufficient_validity"
    assert row["B-online_valid_mean"] == pytest.approx(17.0)
    assert row["B-online_best_score"] == pytest.approx(17.0)
    assert row["online_minus_frozen"] is None


@pytest.mark.parametrize(
    ("mutation", "match"),
    [
        (lambda payload: payload["instances"].pop(), "exactly 24"),
        (
            lambda payload: payload["instances"][6].__setitem__(
                "source_segment", "v1r8-prefix"
            ),
            "source/successor boundary",
        ),
        (
            lambda payload: payload["instances"][0]["instance_receipt"].__setitem__(
                "sha256", "0" * 64
            ),
            "receipt hash mismatch",
        ),
    ],
)
def test_composite_report_fails_closed_on_incomplete_boundary_or_hash_drift(
    tmp_path: Path, mutation: object, match: str
) -> None:
    manifest_path, segment_roots, payload = _build_composition_manifest(tmp_path)
    mutation(payload)
    _write(manifest_path, payload)
    output_root = tmp_path / "report"

    with pytest.raises(RuntimeError, match=match):
        generate_three_arm_composite_report(
            composition_manifest_path=manifest_path,
            segment_roots=segment_roots,
            output_root=output_root,
        )

    assert not output_root.exists()


def test_composite_report_verifies_arm_receipt_hashes(tmp_path: Path) -> None:
    manifest_path, segment_roots, payload = _build_composition_manifest(tmp_path)
    entry = payload["instances"][0]
    receipt_path = (
        segment_roots[entry["source_segment"]]
        / entry["instance_receipt"]["relative_path"]
    )
    arm_path = receipt_path.parent / "arms" / "A.json"
    arm_payload = json.loads(arm_path.read_text(encoding="utf-8"))
    arm_payload["curve"]["rounds"][0]["score"] = 999.0
    _write(arm_path, arm_payload)

    with pytest.raises(RuntimeError, match="arm receipt hash mismatch"):
        generate_three_arm_composite_report(
            composition_manifest_path=manifest_path,
            segment_roots=segment_roots,
            output_root=tmp_path / "report",
        )
