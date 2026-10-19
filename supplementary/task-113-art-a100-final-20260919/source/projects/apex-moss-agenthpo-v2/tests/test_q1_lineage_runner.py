"""Offline contract tests for independent Q1 lineage orchestration."""

from pathlib import Path

import pytest

import scripts.q1_lineage_runner as runner


ROOT = Path(__file__).resolve().parent.parent


def test_offline_smoke_accepts_generic_and_specialized_harnesses():
    for harness in (
        ROOT / "harnesses" / "tddgen_hidden" / "v001" / "harness.py",
        ROOT / "harnesses" / "tddgen_hidden" / "v005" / "harness.py",
    ):
        result = runner.offline_smoke(harness)
        assert result["steps"] > 0
        assert result["tokens"] > 0
        assert isinstance(result["messages"], list)


def test_independent_lineages_start_byte_identical_to_v001():
    start = (
        ROOT / "harnesses" / "tddgen_hidden" / "v001" / "harness.py"
    ).read_bytes()
    for name in runner.LINEAGES:
        assert (
            ROOT / "harnesses" / name / "v001" / "harness.py"
        ).read_bytes() == start


def test_strict_smoke_requires_write_guard_and_actual_tool_pairing():
    specialized = (
        ROOT / "harnesses" / "tddgen_hidden" / "v005" / "harness.py"
    )
    generic = (
        ROOT / "harnesses" / "tddgen_hidden" / "v001" / "harness.py"
    )

    assert runner.offline_smoke(specialized, strict=True)["steps"] > 0
    with pytest.raises(ValueError, match="tool_use|forbidden write"):
        runner.offline_smoke(generic, strict=True)


def test_generic_smoke_error_removes_run_specific_forbidden_path():
    error = runner._generic_smoke_error(
        ValueError(
            "strict smoke dispatched forbidden write(s): "
            "['/tmp/q1-secret-123/test_solution.py']"
        )
    )

    assert "/tmp/" not in error
    assert "solution_path" in error


def test_enforce_generated_contract_repairs_using_only_generic_error(
    monkeypatch, tmp_path
):
    root = tmp_path
    harness = root / "harnesses" / "lineage" / "v002" / "harness.py"
    harness.parent.mkdir(parents=True)
    harness.write_text("broken")
    smoke_calls = []
    repair_calls = []
    archived = []

    monkeypatch.setattr(runner, "ROOT", root)

    def fake_smoke(path, *, strict=False):
        smoke_calls.append((path, strict))
        if path.read_text() == "broken":
            raise ValueError(
                "strict smoke dispatched forbidden write(s): "
                "['/tmp/private/test_solution.py']"
            )
        return {"steps": 1, "tokens": 1, "messages": []}

    def fake_repair(family_dir, candidate, error):
        repair_calls.append((family_dir, candidate, error))
        return "repaired", "same mechanism, contract fixed", "raw"

    monkeypatch.setattr(runner, "offline_smoke", fake_smoke)
    monkeypatch.setattr(runner, "repair_candidate", fake_repair)
    monkeypatch.setattr(runner, "validate_harness", lambda code: None)
    monkeypatch.setattr(runner, "validate_sandbox_contract", lambda code: None)
    monkeypatch.setattr(runner, "_archive", archived.append)

    mechanism = runner.enforce_generated_contract(
        "lineage", "v002", "original mechanism"
    )

    assert mechanism == "same mechanism, contract fixed"
    assert harness.read_text() == "repaired"
    assert "/tmp/private" not in repair_calls[0][2]
    assert "original mechanism" in repair_calls[0][1]
    assert len(smoke_calls) == 2
    assert archived[0]["event"] == "contract_repair"
    assert archived[0]["repair_attempts"] == 1


def test_enforce_generated_contract_allows_second_strict_repair(
    monkeypatch, tmp_path
):
    root = tmp_path
    harness = root / "harnesses" / "lineage" / "v002" / "harness.py"
    harness.parent.mkdir(parents=True)
    harness.write_text("broken-0")
    repairs = []
    archived = []

    monkeypatch.setattr(runner, "ROOT", root)

    def fake_smoke(path, *, strict=False):
        if path.read_text() != "repaired-2":
            raise ValueError(
                "strict smoke dispatched forbidden write(s): "
                "['/tmp/private/test_solution.py']"
            )
        return {"steps": 1, "tokens": 1, "messages": []}

    def fake_repair(family_dir, candidate, error):
        repairs.append((candidate, error))
        number = len(repairs)
        return f"repaired-{number}", f"mechanism-{number}", "raw"

    monkeypatch.setattr(runner, "offline_smoke", fake_smoke)
    monkeypatch.setattr(runner, "repair_candidate", fake_repair)
    monkeypatch.setattr(runner, "validate_harness", lambda code: None)
    monkeypatch.setattr(runner, "validate_sandbox_contract", lambda code: None)
    monkeypatch.setattr(runner, "_archive", archived.append)

    mechanism = runner.enforce_generated_contract(
        "lineage", "v002", "original mechanism"
    )

    assert mechanism == "mechanism-2"
    assert harness.read_text() == "repaired-2"
    assert len(repairs) == 2
    assert archived[0]["repair_attempts"] == 2
