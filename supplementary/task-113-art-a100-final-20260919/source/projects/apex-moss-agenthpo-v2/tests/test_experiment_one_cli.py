from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts import run_moss_experiment_one as cli


POSITIONS = {
    "edgebench": {
        "A": "apple_incremental_game",
        "B": "molecular_self_assembly",
        "C": "treant_forest",
    },
    "alebench": {"A": "ahc024", "B": "ahc026", "C": "ahc011"},
}


def _output(capsys: pytest.CaptureFixture[str]) -> dict[str, object]:
    return json.loads(capsys.readouterr().out)


def test_frozen_manifests_define_the_exact_shared_contract() -> None:
    manifests = {
        suite: cli.load_frozen_manifest(path)
        for suite, path in cli.DEFAULT_MANIFESTS.items()
    }

    for suite, manifest in manifests.items():
        assert manifest.suite == suite
        assert manifest.rounds == 8
        assert manifest.seeds == ("S1", "S2", "S3")
        assert {target.position: target.task_id for target in manifest.targets} == POSITIONS[
            suite
        ]
        assert len({target.task_id for target in manifest.targets}) == 3
        assert manifest.builder_model == manifest.solver_model
        assert manifest.builder_model.model == "gpt-5.6-sol"
        assert manifest.builder_model.reasoning_effort == "high"
        assert manifest.builder_model.api_family == "responses"
        assert manifest.resources.gpu_count == 0

    assert manifests["edgebench"].h0 == manifests["alebench"].h0
    solver_prompt = manifests["edgebench"].h0["spec"]["nodes"][0]["prompt"]
    assert "no status update, plan, analysis, preamble, or trailing explanation" in solver_prompt
    assert "first character of the required candidate" in solver_prompt
    assert manifests["alebench"].official.evolution_evaluator == "public_eval"
    assert manifests["alebench"].official.cross_test_evaluator == "public_eval"


def test_v2_manifests_are_explicit_and_keep_v1_as_the_default() -> None:
    parser = cli.build_parser()
    default_args = parser.parse_args(
        ["preflight", "--suite", "edgebench", "--root", "artifacts"]
    )
    v2_args = parser.parse_args(
        [
            "preflight",
            "--suite",
            "edgebench",
            "--harness-version",
            "v2",
            "--root",
            "artifacts",
        ]
    )

    assert default_args.harness_version == "v1"
    assert v2_args.harness_version == "v2"
    v1 = cli.load_frozen_manifest(cli.DEFAULT_MANIFESTS["edgebench"])
    v2 = cli.load_frozen_manifest(
        cli.V2_MANIFESTS["edgebench"], expected_harness_version=2
    )
    assert v1.task_harness_schema_version == 1
    assert v2.task_harness_schema_version == 2
    assert v1.sha256 != v2.sha256


def test_v2_manifest_cannot_be_loaded_as_v1(tmp_path: Path) -> None:
    payload = json.loads(cli.V2_MANIFESTS["alebench"].read_text(encoding="utf-8"))
    path = tmp_path / "v2-as-v1.json"
    path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match="requested version"):
        cli.load_frozen_manifest(path, expected_harness_version=1)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("rounds", 7, "exactly eight"),
        ("seeds", ["S1", "S2"], "S1/S2/S3"),
    ],
)
def test_manifest_rejects_changes_to_the_formal_contract(
    tmp_path: Path, field: str, value: object, message: str
) -> None:
    payload = json.loads(cli.DEFAULT_MANIFESTS["edgebench"].read_text(encoding="utf-8"))
    payload[field] = value
    path = tmp_path / "changed.json"
    path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match=message):
        cli.load_frozen_manifest(path)


def test_manifest_rejects_position_or_model_changes(tmp_path: Path) -> None:
    payload = json.loads(cli.DEFAULT_MANIFESTS["alebench"].read_text(encoding="utf-8"))
    payload["targets"][0]["task_id"] = "ahc027"
    path = tmp_path / "changed-target.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError, match="frozen A/B/C mapping"):
        cli.load_frozen_manifest(path)

    payload = json.loads(cli.DEFAULT_MANIFESTS["alebench"].read_text(encoding="utf-8"))
    payload["models"]["solver"]["reasoning_effort"] = "medium"
    path = tmp_path / "changed-model.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError, match="gpt-5.6-sol/high Responses"):
        cli.load_frozen_manifest(path)


def test_manifest_override_cannot_change_h0_or_resources(tmp_path: Path) -> None:
    payload = json.loads(cli.DEFAULT_MANIFESTS["edgebench"].read_text(encoding="utf-8"))
    payload["h0"]["spec"]["nodes"][0]["role"] = "different-role"
    path = tmp_path / "changed-h0.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError, match="differs from the checked-in frozen manifest"):
        cli.load_frozen_manifest(path)

    payload = json.loads(cli.DEFAULT_MANIFESTS["edgebench"].read_text(encoding="utf-8"))
    payload["resources"]["minimum_memory_gib"] = 1
    path = tmp_path / "changed-resources.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError, match="differs from the checked-in frozen manifest"):
        cli.load_frozen_manifest(path)


@pytest.mark.parametrize("command", ["canary", "evolve", "freeze", "cross-test", "resume"])
def test_mutating_commands_are_read_only_without_execute(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
    command: str,
) -> None:
    def forbidden_factory(_context: cli.ExecutionContext) -> object:
        raise AssertionError("controller must not be constructed during a dry run")

    monkeypatch.setattr(cli, "create_production_controller", forbidden_factory)
    argv = [command, "--suite", "edgebench", "--root", str(tmp_path / "artifacts")]
    if command in {"canary", "evolve", "freeze", "resume"}:
        argv.extend(["--position", "A"])

    assert cli.main(argv) == 0
    report = _output(capsys)
    assert report["status"] == "planned"
    assert report["executed"] is False
    assert report["requires_execute"] is True
    assert not (tmp_path / "artifacts").exists()


def test_preflight_is_read_only_and_reports_exact_routes(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    root = tmp_path / "never-created"
    monkeypatch.setattr(
        cli,
        "inspect_host",
        lambda _root, _manifest: {
            "ready": True,
            "checks": {"cpu": True, "memory": True, "disk": True},
        },
    )

    assert cli.main(["preflight", "--suite", "edgebench", "--root", str(root)]) == 0
    report = _output(capsys)
    assert report["status"] == "ready"
    assert report["executed"] is False
    assert report["model"] == {
        "api_family": "responses",
        "builder": "gpt-5.6-sol",
        "reasoning_effort": "high",
        "solver": "gpt-5.6-sol",
    }
    assert Path(report["layout"]["lineage_root"]) == (
        root / "formal" / "edgebench" / "S1" / "lineages" / "A"
    ).resolve()
    assert not root.exists()


class _RecordingController:
    def __init__(self, context: cli.ExecutionContext, calls: list[tuple[str, str | None]]) -> None:
        self.context = context
        self.calls = calls

    def run_canary(self, position: str) -> dict[str, object]:
        self.calls.append(("canary", position))
        return {"receipt_sha256": "a" * 64}

    def evolve(self, position: str) -> dict[str, object]:
        self.calls.append(("evolve", position))
        return {"rounds_completed": 8}

    def freeze(self, position: str) -> dict[str, object]:
        self.calls.append(("freeze", position))
        return {"freeze_receipt_sha256": "b" * 64}

    def cross_test(self) -> dict[str, object]:
        self.calls.append(("cross-test", None))
        return {"valid_cells": 9}

    def resume(self, position: str | None) -> dict[str, object]:
        self.calls.append(("resume", position))
        return {"resumed": True}


@pytest.mark.parametrize(
    ("command", "extra", "expected_call"),
    [
        ("canary", ["--position", "B"], ("canary", "B")),
        ("evolve", ["--position", "C"], ("evolve", "C")),
        ("freeze", ["--position", "A"], ("freeze", "A")),
        ("cross-test", [], ("cross-test", None)),
        ("resume", ["--position", "B"], ("resume", "B")),
    ],
)
def test_execute_dispatches_to_the_production_controller_boundary(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
    command: str,
    extra: list[str],
    expected_call: tuple[str, str | None],
) -> None:
    calls: list[tuple[str, str | None]] = []
    contexts: list[cli.ExecutionContext] = []

    def factory(context: cli.ExecutionContext) -> _RecordingController:
        contexts.append(context)
        return _RecordingController(context, calls)

    monkeypatch.setattr(cli, "create_production_controller", factory)
    monkeypatch.setattr(cli, "require_execution_environment", lambda _manifest: None)
    argv = [
        command,
        "--suite",
        "alebench",
        "--root",
        str(tmp_path / "artifacts"),
        "--seed",
        "S2",
        *extra,
        "--execute",
    ]

    assert cli.main(argv) == 0
    report = _output(capsys)
    assert report["status"] == "completed"
    assert report["executed"] is True
    assert calls == [expected_call]
    assert contexts[0].manifest.rounds == 8
    assert contexts[0].seed_id == "S2"
    assert contexts[0].formal_seed_root == (
        tmp_path / "artifacts" / "formal" / "alebench" / "S2"
    ).resolve()


def test_report_reads_status_without_constructing_a_controller(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    root = tmp_path / "artifacts"
    status = root / "formal" / "edgebench" / "S1" / "status"
    status.mkdir(parents=True)
    (status / "evolve-A.json").write_text(
        json.dumps({"command": "evolve", "status": "completed", "rounds_completed": 8}),
        encoding="utf-8",
    )
    monkeypatch.setattr(
        cli,
        "create_production_controller",
        lambda _context: (_ for _ in ()).throw(AssertionError("report is filesystem-only")),
    )

    assert cli.main(["report", "--suite", "edgebench", "--root", str(root)]) == 0
    report = _output(capsys)
    assert report["status"] == "reported"
    assert report["executed"] is False
    assert report["records"] == [
        {"command": "evolve", "rounds_completed": 8, "status": "completed"}
    ]


def test_execute_rejects_wrong_environment_before_controller_construction(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("LLM_API_KEY", "present-but-never-read")
    monkeypatch.setenv("LLM_BASE_URL", "https://api.example.invalid/v1")
    monkeypatch.setenv("LLM_MODEL", "some-other-model")
    monkeypatch.setenv("LLM_REASONING_EFFORT", "high")
    monkeypatch.setenv("MOSS_EDGEBENCH_IMAGE_DIGEST", f"sha256:{'c' * 64}")
    monkeypatch.setattr(
        cli,
        "create_production_controller",
        lambda _context: (_ for _ in ()).throw(AssertionError("wrong route must fail first")),
    )

    with pytest.raises(ValueError, match="LLM_MODEL must be gpt-5.6-sol"):
        cli.main(
            [
                "evolve",
                "--suite",
                "edgebench",
                "--root",
                str(tmp_path),
                "--position",
                "A",
                "--execute",
            ]
        )


def test_execute_requires_a_pinned_image_digest(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest = cli.load_frozen_manifest(cli.DEFAULT_MANIFESTS["alebench"])
    monkeypatch.setenv("LLM_API_KEY", "present-but-never-read")
    monkeypatch.setenv("LLM_BASE_URL", "https://api.example.invalid/v1")
    monkeypatch.setenv("LLM_MODEL", "gpt-5.6-sol")
    monkeypatch.setenv("LLM_REASONING_EFFORT", "high")
    monkeypatch.delenv("MOSS_ALEBENCH_IMAGE_DIGEST", raising=False)

    with pytest.raises(ValueError, match="MOSS_ALEBENCH_IMAGE_DIGEST"):
        cli.require_execution_environment(manifest)


def test_default_context_has_instance_only_builder_memory(tmp_path: Path) -> None:
    context = cli._load_context(
        cli.build_parser().parse_args(
            ["preflight", "--suite", "edgebench", "--root", str(tmp_path)]
        )
    )
    assert context.builder_memory_config.public_payload() == {
        "mode": "instance_only",
        "cross_task_records": [],
        "snapshot_sha256": None,
    }


def test_instance_only_rejects_cross_task_memory_arguments(tmp_path: Path) -> None:
    args = cli.build_parser().parse_args(
        [
            "preflight", "--suite", "edgebench", "--root", str(tmp_path),
            "--cross-task-memory-root", str(tmp_path / "memory"),
        ]
    )
    with pytest.raises(ValueError, match="instance_only"):
        cli._load_context(args)


def test_online_memory_requires_root_and_source_order(tmp_path: Path) -> None:
    args = cli.build_parser().parse_args(
        [
            "preflight", "--suite", "edgebench", "--root", str(tmp_path),
            "--builder-memory-mode", "cross_task_online",
        ]
    )
    with pytest.raises(ValueError, match="cross-task-memory-root"):
        cli._load_context(args)


def test_online_memory_rejects_missing_memory_root_without_creating_it(
    tmp_path: Path,
) -> None:
    memory_root = tmp_path / "missing-memory"
    args = cli.build_parser().parse_args(
        [
            "evolve", "--suite", "edgebench", "--root", str(tmp_path / "artifacts"),
            "--position", "B", "--builder-memory-mode", "cross_task_online",
            "--cross-task-memory-root", str(memory_root), "--source-order", "2",
            "--memory-arm", "B-online",
        ]
    )

    with pytest.raises(ValueError, match="existing directory"):
        cli._load_context(args)

    assert not memory_root.exists()


def test_online_memory_rejects_file_memory_root(tmp_path: Path) -> None:
    memory_root = tmp_path / "memory-file"
    memory_root.write_text("not a directory", encoding="utf-8")
    args = cli.build_parser().parse_args(
        [
            "evolve", "--suite", "edgebench", "--root", str(tmp_path / "artifacts"),
            "--position", "B", "--builder-memory-mode", "cross_task_online",
            "--cross-task-memory-root", str(memory_root), "--source-order", "2",
            "--memory-arm", "B-online",
        ]
    )

    with pytest.raises(ValueError, match="directory"):
        cli._load_context(args)


def test_online_memory_rejects_symlink_memory_root(tmp_path: Path) -> None:
    real_root = tmp_path / "real-memory"
    real_root.mkdir()
    memory_root = tmp_path / "memory-link"
    try:
        memory_root.symlink_to(real_root, target_is_directory=True)
    except (OSError, NotImplementedError) as exc:
        pytest.skip(f"directory symlinks unavailable: {exc}")
    args = cli.build_parser().parse_args(
        [
            "evolve", "--suite", "edgebench", "--root", str(tmp_path / "artifacts"),
            "--position", "B", "--builder-memory-mode", "cross_task_online",
            "--cross-task-memory-root", str(memory_root), "--source-order", "2",
            "--memory-arm", "B-online",
        ]
    )

    with pytest.raises(ValueError, match="symlink"):
        cli._load_context(args)


def test_online_memory_dry_run_has_no_storage_side_effects(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    memory_root = tmp_path / "memory"
    memory_root.mkdir()
    artifact_root = tmp_path / "artifacts"

    exit_code = cli.main(
        [
            "evolve", "--suite", "edgebench", "--root", str(artifact_root),
            "--position", "B", "--builder-memory-mode", "cross_task_online",
            "--cross-task-memory-root", str(memory_root), "--source-order", "2",
            "--memory-arm", "B-online",
        ]
    )

    assert exit_code == 0
    assert json.loads(capsys.readouterr().out)["status"] == "planned"
    assert sorted(path.name for path in memory_root.iterdir()) == []
    assert not artifact_root.exists()


def test_online_memory_requires_explicit_b_online_arm_and_position_b(
    tmp_path: Path,
) -> None:
    args = cli.build_parser().parse_args(
        [
            "evolve", "--suite", "edgebench", "--root", str(tmp_path),
            "--position", "A", "--builder-memory-mode", "cross_task_online",
            "--cross-task-memory-root", str(tmp_path / "memory"),
            "--source-order", "2", "--memory-arm", "B-online",
        ]
    )
    with pytest.raises(ValueError, match="position B"):
        cli._load_context(args)


def test_online_memory_without_b_online_arm_is_rejected(tmp_path: Path) -> None:
    args = cli.build_parser().parse_args(
        [
            "evolve", "--suite", "edgebench", "--root", str(tmp_path),
            "--position", "B", "--builder-memory-mode", "cross_task_online",
            "--cross-task-memory-root", str(tmp_path / "memory"),
            "--source-order", "2",
        ]
    )
    with pytest.raises(ValueError, match="B-online"):
        cli._load_context(args)


def test_base_report_contains_memory_identity_without_rule_text(tmp_path: Path) -> None:
    context = cli.ExecutionContext(
        manifest=cli.load_frozen_manifest(cli.DEFAULT_MANIFESTS["edgebench"]),
        artifact_root=tmp_path,
        seed_id="S1",
    )
    report = cli._base_report(
        command="preflight", context=context, position=None, executed=False
    )
    assert report["builder_memory"] == {
        "arm": "B-Frozen",
        "mode": "instance_only",
        "snapshot_sha256": None,
        "record_count": 0,
        "provenance": [],
    }
