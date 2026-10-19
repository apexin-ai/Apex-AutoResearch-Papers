from __future__ import annotations

import fcntl
import hashlib
import json
from dataclasses import replace
from pathlib import Path

from optimization_lab.harness_builder.historical_import import (
    HISTORICAL_POLICY_ID,
    HistoricalImportContract,
    prepare_historical_trajectories,
)
from optimization_lab.harness_builder.meta_train import (
    MetaTrainContract,
    MetaTrainTrajectory,
)
from optimization_lab.harness_evolution import HarnessArchive
from optimization_lab.p2b_policy import P2bPolicyArchive, initial_policy


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "optimization_lab/harness_builder/data"


def test_historical_import_manifest_freezes_all_lanes_without_winner_selection() -> None:
    contract = HistoricalImportContract.from_json(
        DATA / "historical_trajectory_sources_v1.json"
    )

    assert contract.policy_id == HISTORICAL_POLICY_ID
    assert contract.source_order == ("pilot:P1", "pilot:P2", "p2b:P2B")
    assert contract.winner_selection is False
    assert contract.pilot.ledger_sha256 == (
        "2b1048012857c50a487830da5c380a04c7d19954996dc7538b70ef7686c120c0"
    )
    assert contract.pilot.plan_sha256 == (
        "cbade2206737952dc981709c56c3159871cce3a507ce2e0a45e045046b37d452"
    )
    assert contract.p2b.ledger_sha256 == (
        "da5d862309d31a1135ca5df16603b66d76a62bf3f54fd2edea443f96767472f6"
    )
    assert contract.p2b.plan_sha256 == (
        "a83580b2c226e5631b1bd3bfb9fb66ff672f27d8e064e4ca0f877cab35b8773c"
    )
    assert contract.pilot.event_count == 548
    assert contract.p2b.event_count == 402
    assert tuple(task.source_instance_id for task in contract.tasks) == (
        "kernelbench:level1/40_LayerNorm.py",
        "kernelbench:level2/56_Matmul_Sigmoid_Sum.py",
    )


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _write_ledger(path: Path, events: list[dict[str, object]]) -> None:
    path.write_text(
        "".join(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n" for event in events),
        encoding="utf-8",
    )


def _event(event_type: str, event_id: str, payload: dict[str, object]) -> dict[str, object]:
    return {
        "event_id": event_id,
        "event_type": event_type,
        "payload": payload,
        "recorded_at": "2026-08-02T00:00:00+00:00",
    }


def _candidate(root: Path, scope: Path, candidate_id: str) -> tuple[Path, Path, str]:
    candidate_path = root / scope / "candidates" / f"{candidate_id}.py"
    candidate_path.parent.mkdir(parents=True, exist_ok=True)
    candidate_path.write_text("class ModelNew:\n    pass\n", encoding="utf-8")
    candidate_sha = hashlib.sha256(candidate_path.read_bytes()).hexdigest()
    metadata_path = root / scope / "metadata" / f"{candidate_id}.json"
    _write_json(
        metadata_path,
        {
            "schema_version": 1,
            "candidate_id": candidate_id,
            "candidate_sha256": candidate_sha,
            "candidate_path": str(candidate_path),
            "metadata_path": str(metadata_path),
        },
    )
    return candidate_path, metadata_path, candidate_sha


def _feedback(
    task_id: str,
    candidate_id: str,
    *,
    correct: bool,
    speedup: float | None,
) -> dict[str, object]:
    return {
        "candidate_id": candidate_id,
        "compiled": True,
        "correct": correct,
        "gpu_seconds": 1.0,
        "outcome": "valid" if correct else "incorrect",
        "speedup_vs_eager": speedup,
        "stage_reached": "performance" if correct else "correctness",
        "task_id": task_id,
        "valid_run": True,
    }


def _fixture_sources(
    tmp_path: Path,
) -> tuple[Path, Path, MetaTrainContract, HistoricalImportContract, Path]:
    pilot_root = tmp_path / "pilot"
    p2b_root = tmp_path / "p2b"
    pilot_root.mkdir()
    p2b_root.mkdir()
    (pilot_root / ".ledger.lock").touch()
    (p2b_root / ".ledger.lock").touch()
    (p2b_root / ".p2b-runner.lock").touch()
    meta = MetaTrainContract.from_json(DATA / "experience_bank_v1.json")
    legacy_ids = ("kernelbench_layernorm", "kernelbench_matmul_sigmoid_sum")
    seed_path = ROOT / "optimization_lab/harnesses/seeds/specialist_v001.md"
    seed_text = seed_path.read_text(encoding="utf-8")
    seed_sha = hashlib.sha256(seed_path.read_bytes()).hexdigest()
    p1_harness = ROOT / "optimization_lab/harnesses/seeds/generic_zero_shot.md"
    p1_harness_sha = hashlib.sha256(p1_harness.read_bytes()).hexdigest()
    campaign_baselines = []
    campaign_lineages = []
    pilot_events: list[dict[str, object]] = [
        _event("phase_changed", "phase:P1:started", {"phase": "P1", "status": "in_progress"})
    ]
    task_fixture: list[dict[str, object]] = []
    first_candidate_path: Path | None = None
    for legacy, source in zip(legacy_ids, meta.historical_sources, strict=True):
        p1_lane = f"p1:{legacy}:fixture"
        p2_lane = f"p2:{legacy}:r00"
        p2b_lane = f"p2b:{legacy}:architecture_reset"
        task_fixture.append(
            {
                "legacy": legacy,
                "source": source,
                "p1_lane": p1_lane,
                "p2_lane": p2_lane,
                "p2b_lane": p2b_lane,
            }
        )
        campaign_baselines.append(
            {
                "lane_id": p1_lane,
                "task_id": legacy,
                "kind": "generic_zero_shot",
                "harness_path": str(p1_harness.relative_to(ROOT)),
                "harness_sha256": p1_harness_sha,
                "workflow": ["read_reference", "generate_candidate", "evaluate_once"],
                "allow_harness_mutation": False,
            }
        )
        p1_id = f"p1-{legacy.removeprefix('kernelbench_').replace('_', '-')}-v001"
        candidate_path, metadata_path, candidate_sha = _candidate(
            pilot_root, Path("baselines") / legacy / "fixture", p1_id
        )
        first_candidate_path = first_candidate_path or candidate_path
        feedback = _feedback(legacy, p1_id, correct=True, speedup=1.1)
        pilot_events.extend(
            [
                _event(
                    "candidate_generated",
                    f"generated:{p1_id}",
                    {
                        "api_cost_usd": 0.0,
                        "archive": {
                            "candidate_path": str(candidate_path),
                            "metadata_path": str(metadata_path),
                        },
                        "candidate_id": p1_id,
                        "candidate_sha256": candidate_sha,
                        "lane_id": p1_lane,
                        "task_id": legacy,
                    },
                ),
                _event(
                    "candidate_evaluated",
                    f"evaluated:{p1_id}",
                    {
                        "candidate_sha256": candidate_sha,
                        "feedback": feedback,
                        "task": {
                            "task_id": legacy,
                            "task_sha256": source.source_sha256,
                            "repository_commit": meta.repository_commit,
                        },
                    },
                ),
                _event(
                    "lane_candidate_completed",
                    f"completed:{p1_id}",
                    {
                        "candidate_id": p1_id,
                        "candidate_sha256": candidate_sha,
                        "feedback": feedback,
                        "lane_id": p1_lane,
                        "task_id": legacy,
                    },
                ),
            ]
        )
    pilot_events.append(
        _event("phase_changed", "phase:P1:completed", {"phase": "P1", "status": "completed"})
    )
    pilot_events.append(
        _event("phase_changed", "phase:P2:started", {"phase": "P2", "status": "in_progress"})
    )
    for item in task_fixture:
        legacy = str(item["legacy"])
        source = item["source"]
        p2_lane = str(item["p2_lane"])
        scope = Path("lineages") / legacy / "r00"
        HarnessArchive(pilot_root / scope).store_seed(seed_text, expected_sha256=seed_sha)
        campaign_lineages.append(
            {
                "lineage_id": "r00",
                "task_id": legacy,
                "seed_path": str(seed_path.relative_to(ROOT)),
                "seed_sha256": seed_sha,
                "history_scope": str(scope),
                "max_rounds": 8,
                "allow_harness_mutation": True,
            }
        )
        p2_id = f"p2-{legacy.removeprefix('kernelbench_').replace('_', '-')}-r00-v001"
        candidate_path, metadata_path, candidate_sha = _candidate(
            pilot_root, scope, p2_id
        )
        feedback = _feedback(legacy, p2_id, correct=True, speedup=1.2)
        pilot_events.extend(
            [
                _event(
                    "candidate_generated",
                    f"generated:{p2_id}",
                    {
                        "api_cost_usd": 0.0,
                        "archive": {
                            "candidate_path": str(candidate_path),
                            "metadata_path": str(metadata_path),
                        },
                        "candidate_id": p2_id,
                        "candidate_sha256": candidate_sha,
                        "lane_id": p2_lane,
                        "task_id": legacy,
                    },
                ),
                _event(
                    "candidate_evaluated",
                    f"evaluated:{p2_id}",
                    {
                        "candidate_sha256": candidate_sha,
                        "feedback": feedback,
                        "task": {
                            "task_id": legacy,
                            "task_sha256": source.source_sha256,
                            "repository_commit": meta.repository_commit,
                        },
                    },
                ),
                _event(
                    "p2_candidate_completed",
                    f"candidate-completed:{p2_id}",
                    {
                        "candidate_id": p2_id,
                        "candidate_sha256": candidate_sha,
                        "feedback": feedback,
                        "harness_sha256": seed_sha,
                        "harness_version_id": "v001",
                        "lane_id": p2_lane,
                        "task_id": legacy,
                    },
                ),
                _event(
                    "p2_lineage_round_completed",
                    f"round:{p2_id}",
                    {
                        "candidate_id": p2_id,
                        "feedback": feedback,
                        "harness_sha256": seed_sha,
                        "harness_version_id": "v001",
                        "lane_id": p2_lane,
                        "lineage_id": "r00",
                        "round_number": 1,
                        "task_id": legacy,
                    },
                ),
                _event(
                    "p2_lineage_completed",
                    f"lineage:{legacy}",
                    {"lane_id": p2_lane, "task_id": legacy},
                ),
            ]
        )
    pilot_events.append(
        _event("phase_changed", "phase:P2:completed", {"phase": "P2", "status": "completed"})
    )
    campaign = {
        "schema_version": 1,
        "artifact_root": str(pilot_root),
        "execution_ready": True,
        "baselines": campaign_baselines,
        "lineages": campaign_lineages,
    }
    _write_json(pilot_root / "campaign_plan.json", campaign)
    _write_ledger(pilot_root / "ledger.jsonl", pilot_events)

    p2b_events: list[dict[str, object]] = [
        _event(
            "p2b_phase_changed",
            "p2b-phase:started",
            {"phase": "P2B", "status": "in_progress"},
        )
    ]
    p2b_lanes = []
    for item in task_fixture:
        legacy = str(item["legacy"])
        source = item["source"]
        lane_id = str(item["p2b_lane"])
        scope = Path("lineages") / legacy / "architecture_reset"
        seed = initial_policy(strategy="architecture_reset", starting_candidate_id="reference")
        P2bPolicyArchive(p2b_root / scope).store_seed(seed)
        p2b_lanes.append(
            {
                "lane_id": lane_id,
                "task_id": legacy,
                "strategy": "architecture_reset",
                "history_scope": str(scope),
                "starting_candidate_id": "reference",
                "starting_score": 1.0,
                "allowed_frozen_candidate_ids": [],
                "max_rounds": 8,
            }
        )
        candidate_id = (
            f"p2b-{legacy.removeprefix('kernelbench_').replace('_', '-')}"
            "-architecture-reset-v001"
        )
        candidate_path, _metadata_path, candidate_sha = _candidate(
            p2b_root, scope, candidate_id
        )
        call_id = candidate_id
        feedback = _feedback(legacy, candidate_id, correct=False, speedup=None)
        p2b_events.extend(
            [
                _event(
                    "p2b_model_call_started",
                    f"model-start:{call_id}",
                    {
                        "call_id": call_id,
                        "call_kind": "candidate",
                        "lane_id": lane_id,
                        "task_id": legacy,
                    },
                ),
                _event(
                    "p2b_candidate_generated",
                    f"generated:{candidate_id}",
                    {
                        "api_cost_usd": 0.0,
                        "call_id": call_id,
                        "candidate_id": candidate_id,
                        "candidate_path": str(candidate_path),
                        "candidate_sha256": candidate_sha,
                        "lane_id": lane_id,
                        "policy_sha256": seed.sha256,
                        "policy_version_id": "v001",
                        "round_number": 1,
                        "task_id": legacy,
                    },
                ),
                _event(
                    "candidate_evaluated",
                    f"evaluated:{candidate_id}",
                    {
                        "candidate_sha256": candidate_sha,
                        "feedback": feedback,
                        "task": {
                            "task_id": legacy,
                            "task_sha256": source.source_sha256,
                            "repository_commit": meta.repository_commit,
                        },
                    },
                ),
                _event(
                    "p2b_round_completed",
                    f"round:{candidate_id}",
                    {
                        "candidate_id": candidate_id,
                        "candidate_sha256": candidate_sha,
                        "feedback": feedback,
                        "lane_id": lane_id,
                        "novelty": "new",
                        "policy": seed.policy.to_dict(),
                        "policy_sha256": seed.sha256,
                        "policy_version_id": "v001",
                        "profile": None,
                        "round_number": 1,
                        "score_trend": {"in_noise_band": False},
                        "task_id": legacy,
                    },
                ),
            ]
        )
        failed_call = candidate_id.replace("v001", "v002-harness")
        p2b_events.extend(
            [
                _event(
                    "p2b_model_call_started",
                    f"model-start:{failed_call}",
                    {
                        "call_id": failed_call,
                        "call_kind": "policy",
                        "lane_id": lane_id,
                        "task_id": legacy,
                    },
                ),
                _event(
                    "p2b_policy_generation_failed",
                    f"policy-failed:{legacy}",
                    {
                        "call_id": failed_call,
                        "lane_id": lane_id,
                        "round_number": 2,
                        "task_id": legacy,
                    },
                ),
                _event(
                    "p2b_lane_model_artifact_stopped",
                    f"artifact-stopped:{legacy}",
                    {"lane_id": lane_id, "task_id": legacy},
                ),
                _event(
                    "p2b_lane_completed",
                    f"lane-completed:{legacy}",
                    {"lane_id": lane_id, "task_id": legacy},
                ),
            ]
        )
    p2b_events.append(
        _event(
            "p2b_phase_changed",
            "p2b-phase:completed",
            {"phase": "P2B", "status": "completed"},
        )
    )
    p2b_plan = {
        "schema_version": 1,
        "artifact_root": str(p2b_root),
        "source_artifact_root": str(pilot_root),
        "execution_ready": True,
        "frozen_candidates": [],
        "lanes": p2b_lanes,
    }
    _write_json(p2b_root / "p2b_plan.json", p2b_plan)
    _write_ledger(p2b_root / "ledger.jsonl", p2b_events)
    source_manifest = {
        "schema_version": 1,
        "policy_id": HISTORICAL_POLICY_ID,
        "selection_policy": {
            "aggregate_unit": "one_all_lanes_trajectory_per_task",
            "include_terminal_artifact_failures": True,
            "source_order": ["pilot:P1", "pilot:P2", "p2b:P2B"],
            "terminal_fact_policy": (
                "all_public_terminal_attempts_and_rounds_in_append_only_ledger_order"
            ),
            "winner_selection": False,
        },
        "sources": {
            "pilot": {
                "event_count": len(pilot_events),
                "ledger_filename": "ledger.jsonl",
                "ledger_sha256": hashlib.sha256(
                    (pilot_root / "ledger.jsonl").read_bytes()
                ).hexdigest(),
                "plan_filename": "campaign_plan.json",
                "plan_sha256": hashlib.sha256(
                    (pilot_root / "campaign_plan.json").read_bytes()
                ).hexdigest(),
                "terminal_event_ids": ["phase:P1:completed", "phase:P2:completed"],
            },
            "p2b": {
                "event_count": len(p2b_events),
                "ledger_filename": "ledger.jsonl",
                "ledger_sha256": hashlib.sha256(
                    (p2b_root / "ledger.jsonl").read_bytes()
                ).hexdigest(),
                "plan_filename": "p2b_plan.json",
                "plan_sha256": hashlib.sha256(
                    (p2b_root / "p2b_plan.json").read_bytes()
                ).hexdigest(),
                "terminal_event_ids": ["p2b-phase:completed"],
            },
        },
        "tasks": [
            {
                "expected_terminal_summary_counts": {"P1": 1, "P2": 1, "P2B": 2},
                "instance_descriptor": ["kernelbench", f"level-{source.level}"],
                "legacy_task_id": legacy,
                "p1_lane_ids": [str(item["p1_lane"])],
                "p2_lane_ids": [str(item["p2_lane"])],
                "p2b_lane_ids": [str(item["p2b_lane"])],
                "source_instance_id": source.instance_id,
                "source_sha256": source.source_sha256,
            }
            for legacy, source, item in (
                (str(item["legacy"]), item["source"], item) for item in task_fixture
            )
        ],
    }
    source_path = tmp_path / "historical_sources.json"
    _write_json(source_path, source_manifest)
    source_contract = HistoricalImportContract.from_json(source_path)
    meta = replace(
        meta,
        historical_source_manifest_sha256=source_contract.manifest_sha256,
    )
    assert first_candidate_path is not None
    return pilot_root, p2b_root, meta, source_contract, first_candidate_path


def test_historical_import_aggregates_every_lane_and_artifact_failure_offline(
    tmp_path: Path,
) -> None:
    pilot, p2b, meta, source_contract, _candidate_path = _fixture_sources(tmp_path)
    output = tmp_path / "output"

    outcome = prepare_historical_trajectories(
        project_root=ROOT,
        pilot_root=pilot,
        p2b_root=p2b,
        output_root=output,
        meta_train_contract=meta,
        source_contract=source_contract,
    )

    assert outcome.report["status"] == "ready"
    assert len(outcome.trajectories) == 2
    for trajectory in outcome.trajectories:
        assert [item["phase"] for item in trajectory.round_summaries] == [
            "P1",
            "P2",
            "P2B",
            "P2B",
        ]
        assert trajectory.round_summaries[-1]["failure_reason"] == "invalid_policy_artifact"
        assert any(
            event_id.startswith("candidate-completed:p2-")
            for event_id in trajectory.provenance_event_ids
        )
        assert len(trajectory.initial_harness_structure) == 3
        encoded = trajectory.canonical_bytes.decode("utf-8")
        assert str(tmp_path) not in encoded
        assert "private_evaluator" not in encoded
        object_path = output / "trajectories/objects" / f"{trajectory.sha256}.json"
        assert MetaTrainTrajectory.from_json(object_path) == trajectory
    assert outcome.report["model_calls_started"] == 0
    assert outcome.report["evaluator_transactions_started"] == 0
    assert outcome.report["network_requests_started"] == 0


def test_historical_import_emits_only_blocked_prepare_when_candidate_hash_differs(
    tmp_path: Path,
) -> None:
    pilot, p2b, meta, source_contract, candidate_path = _fixture_sources(tmp_path)
    candidate_path.write_text("class ModelNew:\n    changed = True\n", encoding="utf-8")

    outcome = prepare_historical_trajectories(
        project_root=ROOT,
        pilot_root=pilot,
        p2b_root=p2b,
        output_root=tmp_path / "blocked-output",
        meta_train_contract=meta,
        source_contract=source_contract,
    )

    assert outcome.report["status"] == "blocked"
    assert outcome.report["blockers"] == ["historical_candidate_artifact_hash_differs"]
    assert outcome.trajectories == ()
    assert not (tmp_path / "blocked-output/trajectories").exists()
    assert (tmp_path / "blocked-output" / outcome.report_relative_path).is_file()


def test_historical_import_fails_closed_while_p2b_writer_lock_is_held(
    tmp_path: Path,
) -> None:
    pilot, p2b, meta, source_contract, _candidate_path = _fixture_sources(tmp_path)
    with (p2b / ".p2b-runner.lock").open("r", encoding="utf-8") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        outcome = prepare_historical_trajectories(
            project_root=ROOT,
            pilot_root=pilot,
            p2b_root=p2b,
            output_root=tmp_path / "locked-output",
            meta_train_contract=meta,
            source_contract=source_contract,
        )

    assert outcome.report["status"] == "blocked"
    assert outcome.report["blockers"] == ["p2b_runner_lock_unavailable"]
    assert outcome.trajectories == ()
