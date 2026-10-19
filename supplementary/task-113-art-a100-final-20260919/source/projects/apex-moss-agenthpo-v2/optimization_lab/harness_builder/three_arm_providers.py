from __future__ import annotations

import hashlib
import json
import os
import tempfile
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from .adapters.compilergym import LLVM_ACTION_FLAGS, frozen_contract
from .adapters.compilergym_subprocess import CompilerGymSubprocessAdapter
from .adapters.lcbench import LCBenchAdapter, LCBenchTask
from .adapters.swebench_verified import (
    SWEBENCH_VERIFIED_DATASET_SHA256,
    SWEBenchVerifiedRemoteAdapter,
    SWEBenchVerifiedTask,
)
from .contract_compatibility import SWEBENCH_VERIFIED_CAPABILITY
from .evaluation import (
    CompilerGymEvaluationBackend,
    LCBenchEvaluationBackend,
    SWEBenchVerifiedEvaluationBackend,
)
from .formal import FormalTaskBinding
from .lcbench_canary import (
    LCBENCH_DATA_COMMIT,
    LCBENCH_SELECTED_INSTANCES,
    LCBENCH_SOURCE_HASHES,
)
from .solutions import (
    CompilerGymSolutionCodec,
    LCBenchSolutionCodec,
    SWEBenchVerifiedSolutionCodec,
)
from .three_arm import ThreeArmStreamItem


COMPILERGYM_SELECTED_TASKS = (
    "dijkstra",
    "crc32",
    "stringsearch2",
    "susan",
    "qsort",
    "bitcount",
    "blowfish",
    "bzip2",
)
SWEBENCH_VERIFIED_V1R8_SELECTED_TASKS = (
    "sphinx-doc__sphinx-8459",
    "django__django-14500",
    "scikit-learn__scikit-learn-14983",
    "pylint-dev__pylint-7080",
    "matplotlib__matplotlib-25479",
    "astropy__astropy-14309",
    "sympy__sympy-15599",
    "pytest-dev__pytest-5262",
)
SWEBENCH_VERIFIED_V1R9_PREFIX_TASKS = (
    "sphinx-doc__sphinx-8459",
    "django__django-14500",
)
SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS = (
    "pytest-dev__pytest-7205",
    "matplotlib__matplotlib-25775",
    "pydata__xarray-4356",
    "sympy__sympy-21930",
    "astropy__astropy-13977",
    "pylint-dev__pylint-4604",
)
SWEBENCH_VERIFIED_V1R9_SELECTED_TASKS = (
    SWEBENCH_VERIFIED_V1R9_PREFIX_TASKS + SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS
)
# Backward-compatible name used by the immutable v1r8 preparation path.
SWEBENCH_VERIFIED_SELECTED_TASKS = SWEBENCH_VERIFIED_V1R8_SELECTED_TASKS

SWEBENCH_VERIFIED_SELECTION_MODE_V1R8 = "v1r8-full"
SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE = "v1r9-active"
SWEBENCH_VERIFIED_SELECTION_DOMAIN = (
    b"HB-GEN-1:SWE-bench_Verified:metadata-id-only:repo-diverse-8:v1\0"
)
SWEBENCH_VERIFIED_V1R9_EXCLUDED_REPOSITORIES = (
    "sphinx-doc/sphinx",
    "django/django",
    "psf/requests",
)
SWEBENCH_VERIFIED_V1R9_EXCLUDED_INSTANCE_IDS = (
    "scikit-learn__scikit-learn-14983",
)
SWEBENCH_VERIFIED_V1R9_MIN_FAIL_TO_PASS = 6
SWEBENCH_VERIFIED_V1R9_MIN_RATIO_NUMERATOR = 1
SWEBENCH_VERIFIED_V1R9_MIN_RATIO_DENOMINATOR = 100
_SWEBENCH_VERIFIED_POPULATION_ROWS = 500
_SWEBENCH_SELECTION_V1_SCHEMA = "swebench_verified_metadata_id_selection.v1"
_SWEBENCH_SELECTION_V2_SCHEMA = "swebench_verified_coverage_selection.v2"
_SWEBENCH_IMAGE_LOCK_V1_SCHEMA = "swebench_verified_image_lock.v1"
_SWEBENCH_IMAGE_LOCK_V2_SCHEMA = "swebench_verified_image_lock.v2"


def _canonical_bytes(payload: object) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=True,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _binding_sha(payload: object) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _pretty_bytes(payload: object) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=False,
            allow_nan=False,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    ).encode("utf-8")


def _write_once(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != content:
            raise ValueError(f"refusing to overwrite SWE-bench lock: {path.name}")
        return
    descriptor, temporary = tempfile.mkstemp(
        dir=path.parent, suffix=".swebench-v1r9-lock"
    )
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(temporary).replace(path)
    except Exception:
        Path(temporary).unlink(missing_ok=True)
        raise


def _selection_rank(instance_id: str) -> str:
    return hashlib.sha256(
        SWEBENCH_VERIFIED_SELECTION_DOMAIN + instance_id.encode("utf-8")
    ).hexdigest()


def _scored_test_count(raw: object, *, field: str, instance_id: str) -> int:
    if isinstance(raw, str):
        try:
            raw = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"SWE-bench {field} is not a JSON list for {instance_id}"
            ) from exc
    if (
        not isinstance(raw, list)
        or any(not isinstance(value, str) or not value for value in raw)
        or len(raw) != len(set(raw))
    ):
        raise ValueError(f"SWE-bench {field} differs for {instance_id}")
    return len(raw)


def build_swebench_verified_v1r9_active_selection(
    rows: Sequence[Mapping[str, object]],
) -> dict[str, object]:
    """Mechanically replay the approved coverage-conditioned v1r9 suffix.

    Only test-list cardinalities are retained.  Test names, issue text, gold
    patches, and test patches never enter the returned receipt.
    """

    if len(rows) != _SWEBENCH_VERIFIED_POPULATION_ROWS:
        raise ValueError(
            "SWE-bench v1r9 selector requires the frozen 500-row population"
        )
    ids: list[str] = []
    eligible: list[tuple[str, str, str, int, int]] = []
    excluded_repositories = set(SWEBENCH_VERIFIED_V1R9_EXCLUDED_REPOSITORIES)
    excluded_ids = set(SWEBENCH_VERIFIED_V1R9_EXCLUDED_INSTANCE_IDS)
    for row in rows:
        if not isinstance(row, Mapping) or not {
            "instance_id",
            "repo",
            "FAIL_TO_PASS",
            "PASS_TO_PASS",
        } <= set(row):
            raise ValueError("SWE-bench v1r9 selector row fields differ")
        instance_id = row["instance_id"]
        repo = row["repo"]
        if not isinstance(instance_id, str) or not instance_id:
            raise ValueError("SWE-bench v1r9 selector instance ID differs")
        if not isinstance(repo, str) or not repo or "/" not in repo:
            raise ValueError("SWE-bench v1r9 selector repository differs")
        ids.append(instance_id)
        f2p_total = _scored_test_count(
            row["FAIL_TO_PASS"], field="FAIL_TO_PASS", instance_id=instance_id
        )
        p2p_total = _scored_test_count(
            row["PASS_TO_PASS"], field="PASS_TO_PASS", instance_id=instance_id
        )
        total = f2p_total + p2p_total
        if repo in excluded_repositories or instance_id in excluded_ids:
            continue
        if f2p_total < SWEBENCH_VERIFIED_V1R9_MIN_FAIL_TO_PASS or total <= 0:
            continue
        if (
            f2p_total * SWEBENCH_VERIFIED_V1R9_MIN_RATIO_DENOMINATOR
            < total * SWEBENCH_VERIFIED_V1R9_MIN_RATIO_NUMERATOR
        ):
            continue
        eligible.append(
            (_selection_rank(instance_id), instance_id, repo, f2p_total, p2p_total)
        )
    if len(ids) != len(set(ids)):
        raise ValueError("SWE-bench v1r9 selector requires unique instance IDs")

    selected: list[dict[str, object]] = []
    seen_repositories: set[str] = set()
    for rank, instance_id, repo, f2p_total, p2p_total in sorted(eligible):
        if repo in seen_repositories:
            continue
        seen_repositories.add(repo)
        selected.append(
            {
                "instance_id": instance_id,
                "repo": repo,
                "rank_sha256": rank,
                "fail_to_pass_total": f2p_total,
                "pass_to_pass_total": p2p_total,
            }
        )
        if len(selected) == len(SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS):
            break
    if (
        tuple(item["instance_id"] for item in selected)
        != SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS
    ):
        raise ValueError("SWE-bench v1r9 mechanical selection differs from approval")

    return {
        "schema": _SWEBENCH_SELECTION_V2_SCHEMA,
        "selection_input_columns": [
            "instance_id",
            "repo",
            "FAIL_TO_PASS",
            "PASS_TO_PASS",
        ],
        "population_rows": len(ids),
        "population_unique_ids": len(set(ids)),
        "excluded_repositories": list(
            SWEBENCH_VERIFIED_V1R9_EXCLUDED_REPOSITORIES
        ),
        "excluded_instance_ids": list(
            SWEBENCH_VERIFIED_V1R9_EXCLUDED_INSTANCE_IDS
        ),
        "minimum_fail_to_pass": SWEBENCH_VERIFIED_V1R9_MIN_FAIL_TO_PASS,
        "minimum_fail_to_pass_ratio": {
            "numerator": SWEBENCH_VERIFIED_V1R9_MIN_RATIO_NUMERATOR,
            "denominator": SWEBENCH_VERIFIED_V1R9_MIN_RATIO_DENOMINATOR,
        },
        "algorithm": (
            "exclude frozen prefix repositories, environment-incompatible "
            "repositories, and contaminated instance IDs; keep F2P>=6 and "
            "F2P/(F2P+P2P)>=1/100; sort SHA256(domain || "
            "UTF-8 instance_id); take the first eligible instance from each "
            "distinct repository until six"
        ),
        "domain_hex": SWEBENCH_VERIFIED_SELECTION_DOMAIN.hex(),
        "eligible_rows": len(eligible),
        "eligible_repositories": len({item[2] for item in eligible}),
        "selected": selected,
    }


def build_swebench_verified_v1r9_active_task_lock(
    rows: Sequence[Mapping[str, object]],
    *,
    selection: Mapping[str, object],
    selection_sha256: str,
) -> dict[str, object]:
    """Bind the six active rows without copying gold or test names."""

    validate_swebench_verified_selection(
        selection,
        rows,
        selection_mode=SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE,
        expected_task_ids=SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS,
    )
    if (
        len(selection_sha256) != 64
        or any(character not in "0123456789abcdef" for character in selection_sha256)
    ):
        raise ValueError("SWE-bench v1r9 selection SHA-256 differs")
    rows_by_id = {str(row.get("instance_id")): row for row in rows}
    tasks: list[dict[str, object]] = []
    sealed_fields = (
        "patch",
        "test_patch",
        "problem_statement",
        "hints_text",
        "FAIL_TO_PASS",
        "PASS_TO_PASS",
    )
    public_fields = (
        "instance_id",
        "repo",
        "base_commit",
        "version",
        "environment_setup_commit",
        "difficulty",
        "created_at",
    )
    raw_selected = selection.get("selected")
    if not isinstance(raw_selected, list):  # pragma: no cover - validator guard.
        raise ValueError("SWE-bench v1r9 task-lock selection differs")
    for selected in raw_selected:
        if not isinstance(selected, dict):  # pragma: no cover - validator guard.
            raise ValueError("SWE-bench v1r9 task-lock selection entry differs")
        instance_id = selected["instance_id"]
        row = rows_by_id.get(str(instance_id))
        if row is None:
            raise ValueError("SWE-bench v1r9 task-lock row is missing")
        if any(field not in row for field in public_fields + sealed_fields):
            raise ValueError("SWE-bench v1r9 task-lock row fields differ")
        if any(not isinstance(row[field], str) for field in sealed_fields):
            raise ValueError("SWE-bench v1r9 task-lock sealed field differs")
        f2p_total = _scored_test_count(
            row["FAIL_TO_PASS"],
            field="FAIL_TO_PASS",
            instance_id=str(instance_id),
        )
        p2p_total = _scored_test_count(
            row["PASS_TO_PASS"],
            field="PASS_TO_PASS",
            instance_id=str(instance_id),
        )
        if (
            selected.get("fail_to_pass_total") != f2p_total
            or selected.get("pass_to_pass_total") != p2p_total
        ):
            raise ValueError("SWE-bench v1r9 task-lock score counts differ")
        task = {field: row[field] for field in public_fields}
        task.update(
            {
                "task_sha256": hashlib.sha256(_canonical_bytes(dict(row))).hexdigest(),
                "fail_to_pass_total": f2p_total,
                "pass_to_pass_total": p2p_total,
                "sealed_content_sha256": {
                    field: hashlib.sha256(str(row[field]).encode("utf-8")).hexdigest()
                    for field in sealed_fields
                },
            }
        )
        tasks.append(task)
    return {
        "schema": "swebench_verified_active_task_lock.v2",
        "dataset_sha256": SWEBENCH_VERIFIED_DATASET_SHA256,
        "selection_sha256": selection_sha256,
        "selection_mode": SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE,
        "canonical_task_sha256_encoding": (
            "UTF-8 JSON plus newline, ensure_ascii=true, sort_keys=true, "
            "separators=(',', ':')"
        ),
        "public_columns": list(public_fields),
        "selection_count_columns": [
            "fail_to_pass_total",
            "pass_to_pass_total",
        ],
        "sealed_columns_exposed_only_as_sha256": list(sealed_fields),
        "tasks": tasks,
    }


def prepare_swebench_verified_v1r9_active_locks(
    *,
    dataset_path: Path,
    selection_path: Path,
    task_lock_path: Path,
) -> dict[str, str]:
    """Write the v1r9 selection and task locks without network or model access."""

    dataset_path = dataset_path.resolve(strict=True)
    selection_path = selection_path.absolute()
    task_lock_path = task_lock_path.absolute()
    if _sha(dataset_path) != SWEBENCH_VERIFIED_DATASET_SHA256:
        raise ValueError("SWE-bench v1r9 lock dataset digest differs")
    try:
        import pyarrow.parquet as pq
    except ImportError as exc:  # pragma: no cover - production dependency gate.
        raise RuntimeError("pyarrow is required for SWE-bench v1r9 locks") from exc
    rows = pq.read_table(dataset_path).to_pylist()
    selection = build_swebench_verified_v1r9_active_selection(rows)
    selection_bytes = _pretty_bytes(selection)
    _write_once(selection_path, selection_bytes)
    selection_sha256 = hashlib.sha256(selection_bytes).hexdigest()
    task_lock = build_swebench_verified_v1r9_active_task_lock(
        rows,
        selection=selection,
        selection_sha256=selection_sha256,
    )
    task_lock_bytes = _pretty_bytes(task_lock)
    _write_once(task_lock_path, task_lock_bytes)
    return {
        "dataset_sha256": SWEBENCH_VERIFIED_DATASET_SHA256,
        "selection_path": str(selection_path),
        "selection_sha256": selection_sha256,
        "task_lock_path": str(task_lock_path),
        "task_lock_sha256": hashlib.sha256(task_lock_bytes).hexdigest(),
    }


def _resolve_swebench_selection_contract(
    *, selection_mode: str, expected_task_ids: Sequence[str] | None
) -> tuple[tuple[str, ...], frozenset[str]]:
    if selection_mode == SWEBENCH_VERIFIED_SELECTION_MODE_V1R8:
        frozen_ids = SWEBENCH_VERIFIED_V1R8_SELECTED_TASKS
        online_ids = frozenset(frozen_ids[:6])
    elif selection_mode == SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE:
        frozen_ids = SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS
        online_ids = frozenset(SWEBENCH_VERIFIED_V1R9_SELECTED_TASKS[:6])
    else:
        raise ValueError("unsupported SWE-bench selection mode")
    observed_ids = (
        frozen_ids if expected_task_ids is None else tuple(expected_task_ids)
    )
    if observed_ids != frozen_ids:
        raise ValueError("SWE-bench expected task IDs differ from selection mode")
    return frozen_ids, online_ids


def validate_swebench_verified_selection(
    selection: object,
    rows: Sequence[Mapping[str, object]],
    *,
    selection_mode: str,
    expected_task_ids: Sequence[str] | None = None,
) -> tuple[str, ...]:
    frozen_ids, _online_ids = _resolve_swebench_selection_contract(
        selection_mode=selection_mode,
        expected_task_ids=expected_task_ids,
    )
    if not isinstance(selection, dict):
        raise ValueError("SWE-bench selection is not an object")
    if selection_mode == SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE:
        expected = build_swebench_verified_v1r9_active_selection(rows)
        if selection != expected:
            raise ValueError("SWE-bench v1r9 mechanical selection differs")
        return frozen_ids

    population_ids = tuple(
        row.get("instance_id") if isinstance(row, Mapping) else None for row in rows
    )
    selected = selection.get("selected")
    if (
        len(population_ids) != _SWEBENCH_VERIFIED_POPULATION_ROWS
        or len(population_ids) != len(set(population_ids))
        or any(not isinstance(instance_id, str) for instance_id in population_ids)
        or selection.get("schema") != _SWEBENCH_SELECTION_V1_SCHEMA
        or selection.get("population_rows") != _SWEBENCH_VERIFIED_POPULATION_ROWS
        or selection.get("population_unique_ids")
        != _SWEBENCH_VERIFIED_POPULATION_ROWS
        or selection.get("selection_input_columns") != ["instance_id"]
        or selection.get("domain_hex") != SWEBENCH_VERIFIED_SELECTION_DOMAIN.hex()
        or not isinstance(selected, list)
        or tuple(
            item.get("instance_id") if isinstance(item, dict) else None
            for item in selected
        )
        != frozen_ids
        or any(
            not isinstance(item, dict)
            or item.get("rank_sha256") != _selection_rank(frozen_ids[index])
            for index, item in enumerate(selected)
        )
        or any(instance_id not in population_ids for instance_id in frozen_ids)
    ):
        raise ValueError("SWE-bench v1r8 frozen selection differs")
    return frozen_ids


def _validate_swebench_image_lock(
    image_lock: object,
    *,
    selection_mode: str,
    expected_task_ids: tuple[str, ...],
) -> dict[str, tuple[str, str]]:
    expected_schema = (
        _SWEBENCH_IMAGE_LOCK_V1_SCHEMA
        if selection_mode == SWEBENCH_VERIFIED_SELECTION_MODE_V1R8
        else _SWEBENCH_IMAGE_LOCK_V2_SCHEMA
    )
    if (
        not isinstance(image_lock, dict)
        or image_lock.get("schema") != expected_schema
    ):
        raise ValueError("SWE-bench Verified image lock version differs")
    raw_images = image_lock.get("images")
    if not isinstance(raw_images, list):
        raise ValueError("SWE-bench Verified image lock entries differ")
    if tuple(
        item.get("instance_id") if isinstance(item, dict) else None
        for item in raw_images
    ) != expected_task_ids:
        raise ValueError("SWE-bench Verified image lock set differs")
    images: dict[str, tuple[str, str]] = {}
    for item in raw_images:
        if not isinstance(item, dict):  # pragma: no cover - guarded above.
            raise ValueError("SWE-bench Verified image lock entry differs")
        instance_id = item["instance_id"]
        locked = item.get("locked_reference")
        mutable = item.get("mutable_reference")
        manifest = item.get("manifest_sha256")
        if (
            not isinstance(locked, str)
            or not isinstance(mutable, str)
            or not isinstance(manifest, str)
            or any(character.isspace() for character in locked + mutable)
            or "@sha256:" not in locked
            or ":" not in mutable
            or locked.rsplit("@sha256:", 1)[-1] != manifest
            or len(manifest) != 64
            or any(character not in "0123456789abcdef" for character in manifest)
        ):
            raise ValueError("SWE-bench Verified image lock binding differs")
        images[instance_id] = (locked, mutable)
    return images


def _swebench_remote_execution_contract(
    *,
    host_alias: str,
    remote_python: str,
    remote_project_root: str,
    remote_swebench_source_root: str,
) -> dict[str, str]:
    return {
        "host_alias": host_alias,
        "remote_python": remote_python.rstrip("/"),
        "remote_project_root": remote_project_root.rstrip("/"),
        "remote_swebench_source_root": remote_swebench_source_root.rstrip("/"),
    }


def _validate_swebench_remote_execution_contract(
    canary: Mapping[str, Any],
    *,
    host_alias: str,
    remote_python: str,
    remote_project_root: str,
    remote_swebench_source_root: str,
) -> None:
    expected = _swebench_remote_execution_contract(
        host_alias=host_alias,
        remote_python=remote_python,
        remote_project_root=remote_project_root,
        remote_swebench_source_root=remote_swebench_source_root,
    )
    if canary.get("remote_execution_contract") != expected:
        raise ValueError("SWE-bench Verified remote execution contract differs")


class LCBenchFormalSuiteProvider:
    suite = "yahpo-lcbench"

    def __init__(
        self,
        *,
        staging_plan_sha256: str,
        canary_summary_path: Path,
        data_root: Path,
        settings_path: Path,
        python_executable: Path,
    ) -> None:
        self.staging_plan_sha256 = staging_plan_sha256
        self.canary_summary_path = canary_summary_path.resolve(strict=True)
        self.data_root = data_root.resolve(strict=True)
        self.settings_path = settings_path.resolve(strict=True)
        self.python_executable = python_executable.absolute()
        summary = json.loads(self.canary_summary_path.read_text(encoding="utf-8"))
        if (
            not isinstance(summary, dict)
            or summary.get("passed") is not True
            or summary.get("suite") != self.suite
            or tuple(summary.get("online_instances", ()))
            + tuple(summary.get("sealed_instances", ()))
            != LCBENCH_SELECTED_INSTANCES
            or summary.get("data_commit") != LCBENCH_DATA_COMMIT
            or summary.get("source_hashes") != LCBENCH_SOURCE_HASHES
        ):
            raise ValueError("LCBench canary summary differs from the frozen suite")
        self.canary_summary_sha256 = _sha(self.canary_summary_path)
        self.settings_sha256 = _sha(self.settings_path)

    def bind(self, item: ThreeArmStreamItem) -> FormalTaskBinding:
        if item.suite != self.suite or item.task_id not in LCBENCH_SELECTED_INSTANCES:
            raise ValueError("LCBench provider cannot bind this stream item")
        expected_position = LCBENCH_SELECTED_INSTANCES.index(item.task_id)
        if (item.learning_mode == "online") != (expected_position < 6):
            raise ValueError("LCBench online/sealed task binding differs")
        task = LCBenchTask(
            instance_id=item.task_id,
            data_root=self.data_root,
            settings_path=self.settings_path,
            python_executable=self.python_executable,
            model_sha256=LCBENCH_SOURCE_HASHES["model.onnx"],
            config_space_sha256=LCBENCH_SOURCE_HASHES["config_space.json"],
            encoding_sha256=LCBENCH_SOURCE_HASHES["encoding.json"],
            settings_sha256=self.settings_sha256,
        )
        candidate_contract = {
            "schema_version": 1,
            "instance_id": item.task_id,
            "queries": {
                "exact_count": 16,
                "unique": True,
                "fields": {
                    "batch_size": "integer [16,512]",
                    "learning_rate": "float [0.00010000000000000009,0.10000000000000002]",
                    "max_dropout": "float [0,1]",
                    "max_units": "integer [64,1024]",
                    "momentum": "float [0.1,0.99]",
                    "num_layers": "integer [1,5]",
                    "weight_decay": "float [0.00001,0.1]",
                },
            },
            "fixed_by_evaluator": {"OpenML_task_id": item.task_id, "epoch": 52},
        }
        reference = {
            "benchmark": "YAHPO Gym / LCBench",
            "objective": "maximize val_balanced_accuracy",
            "feedback": "best validation score and best query index from this 16-query batch",
            "private_final_metric": "test_balanced_accuracy is retained by the evaluator and never shown during search",
            "candidate_contract": candidate_contract,
        }
        binding_core = {
            "staging_plan_sha256": self.staging_plan_sha256,
            "canary_summary_sha256": self.canary_summary_sha256,
            "suite": self.suite,
            "task_id": item.task_id,
            "data_commit": LCBENCH_DATA_COMMIT,
            "source_hashes": LCBENCH_SOURCE_HASHES,
            "settings_sha256": self.settings_sha256,
            "candidate_contract": candidate_contract,
        }
        return FormalTaskBinding(
            suite=self.suite,
            task_id=item.task_id,
            instance_id=item.instance_id,
            task_binding_sha256=_binding_sha(binding_core),
            task_card=(
                "Optimize the fixed LCBench dataset instance by returning exactly 16 "
                "distinct legal hyperparameter configurations. The evaluator fixes epoch=52, "
                "scores the whole batch immediately, and exposes only the best validation "
                "balanced accuracy. Return one bare JSON object with exactly three top-level "
                'keys: "schema_version", "instance_id", and "queries". The response must '
                "start from this literal template: "
                f'{{"schema_version":1,"instance_id":"{item.task_id}","queries":['
                "...16 query objects...]}. Do not return a queries-only object and do not "
                "omit schema_version or instance_id. Every query object must contain exactly "
                "these fields and obey these ranges: "
                + json.dumps(
                    candidate_contract["queries"]["fields"],
                    ensure_ascii=True,
                    sort_keys=True,
                    separators=(",", ":"),
                )
            ),
            reference_artifact=json.dumps(reference, indent=2, sort_keys=True),
            instance_descriptors=(
                self.suite,
                "hyperparameter-optimization",
                "tabular-surrogate",
                "classification",
            ),
            solution_codec=LCBenchSolutionCodec(instance_id=item.task_id),
            evaluator=LCBenchEvaluationBackend(adapter=LCBenchAdapter(task=task)),
        )


class CompilerGymFormalSuiteProviderV2:
    suite = "compilergym-cbench"

    def __init__(
        self,
        *,
        staging_plan_sha256: str,
        canary_summary_path: Path,
        python_executable: Path,
        project_root: Path,
        site_data_root: Path,
        cache_root: Path,
        compatibility_library_root: Path,
    ) -> None:
        self.staging_plan_sha256 = staging_plan_sha256
        self.canary_summary_path = canary_summary_path.resolve(strict=True)
        canary = json.loads(self.canary_summary_path.read_text(encoding="utf-8"))
        if (
            not isinstance(canary, dict)
            or canary.get("passed") is not True
            or canary.get("suite") != self.suite
            or tuple(canary.get("selected_instances", ()))
            != COMPILERGYM_SELECTED_TASKS
        ):
            raise ValueError("CompilerGym canary summary differs")
        self.canary_summary_sha256 = _sha(self.canary_summary_path)
        self.python_executable = python_executable.absolute()
        self.project_root = project_root.resolve(strict=True)
        self.site_data_root = site_data_root.resolve(strict=True)
        self.cache_root = cache_root.resolve(strict=True)
        self.compatibility_library_root = compatibility_library_root.resolve(
            strict=True
        )

    def bind(self, item: ThreeArmStreamItem) -> FormalTaskBinding:
        if item.suite != self.suite or item.task_id not in COMPILERGYM_SELECTED_TASKS:
            raise ValueError("CompilerGym provider cannot bind this stream item")
        expected_position = COMPILERGYM_SELECTED_TASKS.index(item.task_id)
        if (item.learning_mode == "online") != (expected_position < 6):
            raise ValueError("CompilerGym online/sealed task binding differs")
        uri = f"benchmark://cbench-v1/{item.task_id}"
        contract = frozen_contract(uri)
        candidate_contract = {
            "schema_version": 1,
            "benchmark_uri": uri,
            "actions": {
                "minimum": 1,
                "maximum": 64,
                "allowlist": list(LLVM_ACTION_FLAGS),
            },
        }
        binding_core = {
            "staging_plan_sha256": self.staging_plan_sha256,
            "canary_summary_sha256": self.canary_summary_sha256,
            "suite": self.suite,
            "task_id": item.task_id,
            "evaluator_contract": contract,
            "candidate_contract": candidate_contract,
        }
        adapter = CompilerGymSubprocessAdapter(
            benchmark_uri=uri,
            python_executable=self.python_executable,
            project_root=self.project_root,
            site_data_root=self.site_data_root,
            cache_root=self.cache_root,
            compatibility_library_root=self.compatibility_library_root,
        )
        return FormalTaskBinding(
            suite=self.suite,
            task_id=item.task_id,
            instance_id=item.instance_id,
            task_binding_sha256=_binding_sha(binding_core),
            task_card=(
                f"Optimize frozen CompilerGym cBench program {item.task_id}. Return one bare "
                "JSON object with exactly three top-level keys: \"schema_version\", "
                '"benchmark_uri", and "actions". The response must start from this literal '
                "template: "
                f'{{"schema_version":1,"benchmark_uri":"{uri}","actions":['
                '"-example-pass",...]}. Do not return an actions-only object and do not omit '
                "schema_version or benchmark_uri. The actions array must contain 1 to 64 "
                "strings drawn only from this frozen allowlist: "
                + json.dumps(
                    list(LLVM_ACTION_FLAGS),
                    ensure_ascii=True,
                    separators=(",", ":"),
                )
                + ". Fresh replay and all frozen ordinary semantic validators must pass. "
                "The score is initial IR instruction count divided by final IR instruction "
                "count."
            ),
            reference_artifact=json.dumps(
                {
                    "candidate_contract": candidate_contract,
                    "evaluator_contract": contract,
                },
                indent=2,
                sort_keys=True,
            ),
            instance_descriptors=(
                self.suite,
                "compiler-optimization",
                "llvm-pass-sequence",
                item.task_id,
            ),
            solution_codec=CompilerGymSolutionCodec(benchmark_uri=uri),
            evaluator=CompilerGymEvaluationBackend(adapter=adapter),
        )


class SWEBenchVerifiedFormalSuiteProvider:
    suite = "swebench-verified"

    def __init__(
        self,
        *,
        staging_plan_sha256: str,
        canary_summary_path: Path,
        dataset_path: Path,
        selection_path: Path,
        image_lock_path: Path,
        host_alias: str,
        remote_python: str,
        remote_project_root: str,
        remote_swebench_source_root: str,
        remote_attempt_root: str,
        selection_mode: str = SWEBENCH_VERIFIED_SELECTION_MODE_V1R8,
        expected_task_ids: Sequence[str] | None = None,
    ) -> None:
        self.staging_plan_sha256 = staging_plan_sha256
        self.selection_mode = selection_mode
        self.expected_task_ids, self.online_task_ids = (
            _resolve_swebench_selection_contract(
                selection_mode=selection_mode,
                expected_task_ids=expected_task_ids,
            )
        )
        self.canary_summary_path = canary_summary_path.resolve(strict=True)
        self.dataset_path = dataset_path.resolve(strict=True)
        self.selection_path = selection_path.resolve(strict=True)
        self.image_lock_path = image_lock_path.resolve(strict=True)
        if _sha(self.dataset_path) != SWEBENCH_VERIFIED_DATASET_SHA256:
            raise ValueError("SWE-bench Verified dataset digest differs")
        try:
            import pyarrow.parquet as pq
        except ImportError as exc:  # pragma: no cover - production dependency gate.
            raise RuntimeError(
                "pyarrow is required for the frozen SWE-bench data"
            ) from exc
        selection_columns = (
            ["instance_id"]
            if selection_mode == SWEBENCH_VERIFIED_SELECTION_MODE_V1R8
            else ["instance_id", "repo", "FAIL_TO_PASS", "PASS_TO_PASS"]
        )
        selection_rows = pq.read_table(
            self.dataset_path, columns=selection_columns
        ).to_pylist()
        selection = json.loads(self.selection_path.read_text(encoding="utf-8"))
        validate_swebench_verified_selection(
            selection,
            selection_rows,
            selection_mode=selection_mode,
            expected_task_ids=self.expected_task_ids,
        )
        image_lock = json.loads(self.image_lock_path.read_text(encoding="utf-8"))
        self.images = _validate_swebench_image_lock(
            image_lock,
            selection_mode=selection_mode,
            expected_task_ids=self.expected_task_ids,
        )
        selection_sha256 = _sha(self.selection_path)
        image_lock_sha256 = _sha(self.image_lock_path)
        canary = json.loads(self.canary_summary_path.read_text(encoding="utf-8"))
        if (
            not isinstance(canary, dict)
            or canary.get("passed") is not True
            or canary.get("suite") != self.suite
            or tuple(canary.get("selected_instances", ()))
            != self.expected_task_ids
            or canary.get("dataset_sha256") != SWEBENCH_VERIFIED_DATASET_SHA256
            or canary.get("selection_sha256") != selection_sha256
            or canary.get("image_lock_sha256") != image_lock_sha256
            or (
                selection_mode == SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE
                and (
                    canary.get("schema_version") != 2
                    or canary.get("selection_mode") != selection_mode
                )
            )
        ):
            raise ValueError("SWE-bench Verified canary summary differs")
        if selection_mode == SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE:
            _validate_swebench_remote_execution_contract(
                canary,
                host_alias=host_alias,
                remote_python=remote_python,
                remote_project_root=remote_project_root,
                remote_swebench_source_root=remote_swebench_source_root,
            )
        self.canary_summary_sha256 = _sha(self.canary_summary_path)
        self.selection_sha256 = selection_sha256
        self.image_lock_sha256 = image_lock_sha256
        table = pq.read_table(self.dataset_path)
        rows = {
            row["instance_id"]: row
            for row in table.to_pylist()
            if row["instance_id"] in self.expected_task_ids
        }
        if set(rows) != set(self.expected_task_ids):
            raise ValueError("SWE-bench Verified selected task rows are missing")
        self.rows = rows
        self.host_alias = host_alias
        self.remote_python = remote_python
        self.remote_project_root = remote_project_root
        self.remote_swebench_source_root = remote_swebench_source_root
        self.remote_attempt_root = remote_attempt_root

    def bind(self, item: ThreeArmStreamItem) -> FormalTaskBinding:
        if item.suite != self.suite or item.task_id not in self.expected_task_ids:
            raise ValueError("SWE-bench Verified provider cannot bind this item")
        if (item.learning_mode == "online") != (item.task_id in self.online_task_ids):
            raise ValueError("SWE-bench Verified online/sealed task binding differs")
        row = dict(self.rows[item.task_id])
        task_sha = hashlib.sha256(_canonical_bytes(row)).hexdigest()
        locked_ref, mutable_ref = self.images[item.task_id]
        task = SWEBenchVerifiedTask(
            instance=row,
            task_sha256=task_sha,
            locked_image_ref=locked_ref,
            mutable_image_ref=mutable_ref,
        )
        binding_core = {
            "staging_plan_sha256": self.staging_plan_sha256,
            "canary_summary_sha256": self.canary_summary_sha256,
            "dataset_sha256": SWEBENCH_VERIFIED_DATASET_SHA256,
            "selection_sha256": self.selection_sha256,
            "selection_mode": self.selection_mode,
            "image_lock_sha256": self.image_lock_sha256,
            "task_sha256": task_sha,
            "image_manifest_sha256": locked_ref.rsplit("@sha256:", 1)[1],
            "candidate_compatibility_policy": (
                SWEBENCH_VERIFIED_CAPABILITY.public_payload()
            ),
        }
        adapter = SWEBenchVerifiedRemoteAdapter(
            task=task,
            host_alias=self.host_alias,
            remote_python=self.remote_python,
            remote_project_root=self.remote_project_root,
            remote_swebench_source_root=self.remote_swebench_source_root,
            remote_attempt_root=self.remote_attempt_root,
        )
        public_reference = {
            "instance_id": item.task_id,
            "repository": row["repo"],
            "base_commit": row["base_commit"],
            "version": row["version"],
            "problem_statement": row["problem_statement"],
            "candidate_contract": (
                "Return one complete canonical Git unified diff only; no prose, "
                "renames, binary patches, mode-only changes, or fuzzy application."
            ),
            "candidate_contract_capability": (
                SWEBENCH_VERIFIED_CAPABILITY.public_payload()
            ),
            "score_contract": (
                "Laplace-smoothed fraction of official FAIL_TO_PASS and PASS_TO_PASS "
                "tests passing; resolved remains the official all-tests criterion."
            ),
            "trust_grade": "official_standard_candidate_visible_test_process",
        }
        return FormalTaskBinding(
            suite=self.suite,
            task_id=item.task_id,
            instance_id=item.instance_id,
            task_binding_sha256=_binding_sha(binding_core),
            task_card=(
                f"Fix the frozen SWE-bench Verified issue in {row['repo']} at the supplied "
                "base commit. Return only one exact Git diff and no prose or extra files. "
                "Every modified regular-file section must use this literal order:\n"
                "diff --git a/<path> b/<path>\n"
                "index <old-hex>..<new-hex> 100644  # optional metadata\n"
                "--- a/<path>\n+++ b/<path>\n"
                "@@ -<old-start>,<old-count> +<new-start>,<new-count> @@\n"
                " <context>\n-<deleted>\n+<added>\n"
                "If the non-semantic index line is omitted, the trusted controller may insert "
                "it deterministically; it never repairs paths, hunks, context, or patch/test "
                "semantics. The official repository tests run immediately after each accepted "
                "patch; use only bounded public score/count and exact contract-stage feedback "
                "to improve the next patch.\n\n" + str(row["problem_statement"])
            ),
            reference_artifact=json.dumps(public_reference, indent=2, sort_keys=True),
            instance_descriptors=(
                self.suite,
                "software-repair",
                str(row["repo"]),
                str(row["version"]),
            ),
            solution_codec=SWEBenchVerifiedSolutionCodec(),
            evaluator=SWEBenchVerifiedEvaluationBackend(adapter=adapter),
        )


class ThreeArmProviderFactory:
    def __init__(
        self,
        *,
        staging_plan_sha256: str,
        providers: Mapping[str, object],
    ) -> None:
        if set(providers) != {
            "yahpo-lcbench",
            "compilergym-cbench",
            "swebench-verified",
        }:
            raise ValueError("three-arm provider factory requires all three suites")
        if any(getattr(provider, "suite", None) != suite for suite, provider in providers.items()):
            raise ValueError("three-arm provider suite binding differs")
        self.staging_plan_sha256 = staging_plan_sha256
        self._providers = MappingProxyType(dict(providers))

    def create(self, suite: str):
        try:
            return self._providers[suite]
        except KeyError as exc:
            raise ValueError("suite is outside the three-arm campaign") from exc


__all__ = [
    "COMPILERGYM_SELECTED_TASKS",
    "CompilerGymFormalSuiteProviderV2",
    "LCBenchFormalSuiteProvider",
    "SWEBENCH_VERIFIED_SELECTION_DOMAIN",
    "SWEBENCH_VERIFIED_SELECTION_MODE_V1R8",
    "SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE",
    "SWEBENCH_VERIFIED_SELECTED_TASKS",
    "SWEBENCH_VERIFIED_V1R8_SELECTED_TASKS",
    "SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS",
    "SWEBENCH_VERIFIED_V1R9_PREFIX_TASKS",
    "SWEBENCH_VERIFIED_V1R9_SELECTED_TASKS",
    "SWEBenchVerifiedFormalSuiteProvider",
    "ThreeArmProviderFactory",
    "build_swebench_verified_v1r9_active_task_lock",
    "build_swebench_verified_v1r9_active_selection",
    "prepare_swebench_verified_v1r9_active_locks",
    "validate_swebench_verified_selection",
]
