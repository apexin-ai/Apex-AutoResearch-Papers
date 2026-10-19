from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import pytest

from optimization_lab.harness_builder.three_arm import ThreeArmStreamItem
from optimization_lab.harness_builder.three_arm_providers import (
    CompilerGymFormalSuiteProviderV2,
    LCBenchFormalSuiteProvider,
    SWEBENCH_VERIFIED_SELECTION_DOMAIN,
    SWEBENCH_VERIFIED_V1R8_SELECTED_TASKS,
    SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS,
    SWEBENCH_VERIFIED_V1R9_PREFIX_TASKS,
    SWEBENCH_VERIFIED_V1R9_SELECTED_TASKS,
    SWEBenchVerifiedFormalSuiteProvider,
    _validate_swebench_remote_execution_contract,
    build_swebench_verified_v1r9_active_selection,
    build_swebench_verified_v1r9_active_task_lock,
    validate_swebench_verified_selection,
)


def _item(*, suite: str, task_id: str) -> ThreeArmStreamItem:
    return ThreeArmStreamItem(
        stream_index=0,
        block_index=0,
        suite=suite,
        task_id=task_id,
        arm_order=("A", "B-frozen", "B-online"),
        learning_mode="online",
    )


def test_lcbench_task_card_spells_out_non_optional_top_level_json(
    tmp_path: Path,
) -> None:
    settings = tmp_path / "lcbench-config.yaml"
    settings.write_text("fixture: true\n", encoding="utf-8")
    provider = object.__new__(LCBenchFormalSuiteProvider)
    provider.staging_plan_sha256 = "a" * 64
    provider.canary_summary_sha256 = "b" * 64
    provider.data_root = tmp_path
    provider.settings_path = settings
    provider.python_executable = Path(sys.executable)
    provider.settings_sha256 = "c" * 64

    binding = provider.bind(_item(suite="yahpo-lcbench", task_id="167168"))

    assert "exactly three top-level keys" in binding.task_card
    assert (
        '{"schema_version":1,"instance_id":"167168","queries":['
        in binding.task_card
    )
    assert "Do not return a queries-only object" in binding.task_card


def test_compilergym_task_card_spells_out_non_optional_top_level_json(
    tmp_path: Path,
) -> None:
    for name in ("site-data", "cache", "compat-libs"):
        (tmp_path / name).mkdir()
    provider = object.__new__(CompilerGymFormalSuiteProviderV2)
    provider.staging_plan_sha256 = "a" * 64
    provider.canary_summary_sha256 = "b" * 64
    provider.python_executable = Path(sys.executable)
    provider.project_root = tmp_path
    provider.site_data_root = tmp_path / "site-data"
    provider.cache_root = tmp_path / "cache"
    provider.compatibility_library_root = tmp_path / "compat-libs"

    binding = provider.bind(_item(suite="compilergym-cbench", task_id="dijkstra"))

    assert "exactly three top-level keys" in binding.task_card
    assert (
        '{"schema_version":1,"benchmark_uri":"benchmark://cbench-v1/dijkstra",'
        '"actions":[' in binding.task_card
    )
    assert "Do not return an actions-only object" in binding.task_card


def _coverage_row(
    instance_id: str,
    repo: str,
    fail_to_pass: int,
    pass_to_pass: int,
) -> dict[str, object]:
    return {
        "instance_id": instance_id,
        "repo": repo,
        "base_commit": "a" * 40,
        "version": "1.0",
        "environment_setup_commit": "b" * 40,
        "difficulty": "fixture",
        "created_at": "2020-01-01T00:00:00Z",
        "patch": f"SECRET-GOLD-PATCH-{instance_id}",
        "test_patch": f"SECRET-GOLD-TEST-PATCH-{instance_id}",
        "problem_statement": f"SECRET-PROBLEM-{instance_id}",
        "hints_text": f"SECRET-HINTS-{instance_id}",
        "FAIL_TO_PASS": json.dumps([f"f{index}" for index in range(fail_to_pass)]),
        "PASS_TO_PASS": json.dumps([f"p{index}" for index in range(pass_to_pass)]),
    }


def _v1r9_selection_rows() -> list[dict[str, object]]:
    counts = {
        "pytest-dev__pytest-7205": ("pytest-dev/pytest", 10, 16),
        "matplotlib__matplotlib-25775": ("matplotlib/matplotlib", 7, 89),
        "pydata__xarray-4356": ("pydata/xarray", 8, 604),
        "sympy__sympy-21930": ("sympy/sympy", 6, 45),
        "astropy__astropy-13977": ("astropy/astropy", 20, 322),
        "pylint-dev__pylint-4604": ("pylint-dev/pylint", 21, 0),
    }
    rows = [
        _coverage_row(instance_id, repo, fail_to_pass, pass_to_pass)
        for instance_id, (repo, fail_to_pass, pass_to_pass) in counts.items()
    ]
    # The production selector is frozen to the 500-row Verified population.
    # These rows are all below the F2P threshold and cannot affect selection.
    rows.extend(
        _coverage_row(f"dummy__repo-{index}", f"dummy/repo-{index}", 1, 20)
        for index in range(494)
    )
    return rows


def test_swebench_v1r9_selection_is_versioned_and_mechanically_replayable() -> None:
    receipt = build_swebench_verified_v1r9_active_selection(
        _v1r9_selection_rows()
    )

    assert SWEBENCH_VERIFIED_V1R8_SELECTED_TASKS[:2] == (
        "sphinx-doc__sphinx-8459",
        "django__django-14500",
    )
    assert SWEBENCH_VERIFIED_V1R9_PREFIX_TASKS == (
        "sphinx-doc__sphinx-8459",
        "django__django-14500",
    )
    assert SWEBENCH_VERIFIED_V1R9_SELECTED_TASKS == (
        SWEBENCH_VERIFIED_V1R9_PREFIX_TASKS
        + SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS
    )
    assert receipt["schema"] == "swebench_verified_coverage_selection.v2"
    assert receipt["selection_input_columns"] == [
        "instance_id",
        "repo",
        "FAIL_TO_PASS",
        "PASS_TO_PASS",
    ]
    assert receipt["minimum_fail_to_pass"] == 6
    assert receipt["minimum_fail_to_pass_ratio"] == {
        "numerator": 1,
        "denominator": 100,
    }
    assert receipt["excluded_repositories"] == [
        "sphinx-doc/sphinx",
        "django/django",
        "psf/requests",
    ]
    assert receipt["excluded_instance_ids"] == [
        "scikit-learn__scikit-learn-14983"
    ]
    assert [item["instance_id"] for item in receipt["selected"]] == list(
        SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS
    )
    expected_ranks = {
        task_id: hashlib.sha256(
            SWEBENCH_VERIFIED_SELECTION_DOMAIN + task_id.encode("utf-8")
        ).hexdigest()
        for task_id in SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS
    }
    assert {
        item["instance_id"]: item["rank_sha256"] for item in receipt["selected"]
    } == expected_ranks


def test_swebench_v1r9_selection_rejects_nonmechanical_or_old_receipt() -> None:
    rows = _v1r9_selection_rows()
    receipt = build_swebench_verified_v1r9_active_selection(rows)
    validate_swebench_verified_selection(
        receipt,
        rows,
        selection_mode="v1r9-active",
        expected_task_ids=SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS,
    )

    tampered = json.loads(json.dumps(receipt))
    tampered["selected"][0]["fail_to_pass_total"] = 7
    with pytest.raises(ValueError, match="mechanical selection"):
        validate_swebench_verified_selection(
            tampered,
            rows,
            selection_mode="v1r9-active",
            expected_task_ids=SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS,
        )

    old = {
        "selected": [
            {"instance_id": task_id}
            for task_id in SWEBENCH_VERIFIED_V1R8_SELECTED_TASKS
        ]
    }
    with pytest.raises(ValueError, match="v1r9"):
        validate_swebench_verified_selection(
            old,
            rows,
            selection_mode="v1r9-active",
            expected_task_ids=SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS,
        )


def test_swebench_v1r9_task_lock_contains_counts_and_hashes_but_no_gold() -> None:
    rows = _v1r9_selection_rows()
    selection = build_swebench_verified_v1r9_active_selection(rows)
    lock = build_swebench_verified_v1r9_active_task_lock(
        rows,
        selection=selection,
        selection_sha256="d" * 64,
    )

    assert lock["schema"] == "swebench_verified_active_task_lock.v2"
    assert [item["instance_id"] for item in lock["tasks"]] == list(
        SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS
    )
    assert [item["fail_to_pass_total"] for item in lock["tasks"]] == [
        10,
        7,
        8,
        6,
        20,
        21,
    ]
    serialized = json.dumps(lock, sort_keys=True)
    assert "SECRET-GOLD" not in serialized
    assert "SECRET-PROBLEM" not in serialized
    assert "SECRET-HINTS" not in serialized


def test_swebench_v1r9_provider_rejects_prefix_and_preserves_sealed_positions() -> None:
    provider = object.__new__(SWEBenchVerifiedFormalSuiteProvider)
    provider.expected_task_ids = SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS
    provider.online_task_ids = frozenset(SWEBENCH_VERIFIED_V1R9_SELECTED_TASKS[:6])

    with pytest.raises(ValueError, match="cannot bind"):
        provider.bind(_item(suite="swebench-verified", task_id="sphinx-doc__sphinx-8459"))

    sealed = _item(suite="swebench-verified", task_id="astropy__astropy-13977")
    with pytest.raises(ValueError, match="online/sealed"):
        provider.bind(sealed)


def test_swebench_remote_execution_contract_binds_formal_to_canary_runtime() -> None:
    canary = {
        "remote_execution_contract": {
            "host_alias": "a100jump",
            "remote_python": "/remote/venv/bin/python",
            "remote_project_root": "/remote/runtime/Moss-commit",
            "remote_swebench_source_root": "/remote/SWE-bench",
        }
    }
    _validate_swebench_remote_execution_contract(
        canary,
        host_alias="a100jump",
        remote_python="/remote/venv/bin/python",
        remote_project_root="/remote/runtime/Moss-commit",
        remote_swebench_source_root="/remote/SWE-bench",
    )
    with pytest.raises(ValueError, match="remote execution"):
        _validate_swebench_remote_execution_contract(
            canary,
            host_alias="a100jump",
            remote_python="/remote/venv/bin/python",
            remote_project_root="/remote/runtime/Moss-other",
            remote_swebench_source_root="/remote/SWE-bench",
        )
