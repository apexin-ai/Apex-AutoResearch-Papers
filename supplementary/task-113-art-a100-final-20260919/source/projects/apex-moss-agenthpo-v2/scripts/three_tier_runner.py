"""Offline protocol primitives for the three-tier optimizer qualification.

This module deliberately contains no model dispatch.  It owns the deterministic
pieces that must be frozen and tested before P3 can authorize any API call:
snapshot construction, proposer visibility boundaries, exact selector/final
gates, instance-conditioned source checks, and sealed-test state transitions.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import unicodedata
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


PROTOCOL_NAME = "moss-three-tier-qualification-v1"
ALLOWED_TASK_FILES = (
    "solution.py",
    "test_solution.py",
    "_hidden/test_hidden.py",
)
TRAIN_SIZE = 16
VALIDATION_SIZE = 20
TEST_SIZE = 34


class ProtocolError(RuntimeError):
    """A deterministic protocol contract was violated."""


def _sha_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _sha_text(value: str) -> str:
    return _sha_bytes(value.encode("utf-8"))


def _canonical_json(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8")


def _atomic_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=path.parent, delete=False
    ) as handle:
        handle.write(encoded)
        handle.flush()
        os.fsync(handle.fileno())
        temporary = Path(handle.name)
    temporary.replace(path)
    directory_fd = os.open(path.parent, os.O_DIRECTORY)
    try:
        os.fsync(directory_fd)
    finally:
        os.close(directory_fd)


def accept_selector(
    *,
    candidate_train: int,
    parent_train: int,
    candidate_validation: int,
    seed_validation: int,
    parent_validation: int,
) -> bool:
    """The quick selector: strict train improvement and fixed one-task epsilon."""
    return (
        candidate_train >= parent_train + 1
        and candidate_validation >= max(seed_validation, parent_validation) - 1
    )


def _population_variance(counts: tuple[int, int, int], denominator: int) -> Fraction:
    values = tuple(Fraction(value, denominator) for value in counts)
    mean = sum(values, Fraction()) / len(values)
    return sum((value - mean) ** 2 for value in values) / len(values)


@dataclass(frozen=True)
class PretestDecision:
    train_gain: Fraction
    validation_gain: Fraction
    passed: bool
    reason: str | None


def pretest_gate(
    *,
    seed_train: tuple[int, int, int],
    final_train: tuple[int, int, int],
    seed_validation: tuple[int, int, int],
    final_validation: tuple[int, int, int],
) -> PretestDecision:
    """Apply §1.5/§6.1 formal gates without float rounding."""
    if any(not 0 <= count <= TRAIN_SIZE for count in (*seed_train, *final_train)):
        raise ProtocolError("training count outside frozen benchmark size")
    if any(
        not 0 <= count <= VALIDATION_SIZE
        for count in (*seed_validation, *final_validation)
    ):
        raise ProtocolError("validation count outside frozen benchmark size")
    train_gain = Fraction(sum(final_train) - sum(seed_train), TRAIN_SIZE * 3)
    validation_gain = Fraction(
        sum(final_validation) - sum(seed_validation), VALIDATION_SIZE * 3
    )
    if train_gain < Fraction(3, 20):
        return PretestDecision(train_gain, validation_gain, False, "training_gain")
    largest_variance = max(
        _population_variance(seed_train, TRAIN_SIZE),
        _population_variance(final_train, TRAIN_SIZE),
    )
    if train_gain * train_gain <= largest_variance:
        return PretestDecision(
            train_gain, validation_gain, False, "training_repeat_variation"
        )
    if validation_gain < -Fraction(1, 20):
        return PretestDecision(
            train_gain, validation_gain, False, "validation_tolerance"
        )
    return PretestDecision(train_gain, validation_gain, True, None)


class InstanceLinter:
    """Frozen lexical guard against explicit benchmark-instance conditioning."""

    def __init__(
        self,
        *,
        task_ids: Iterable[str],
        basenames: Iterable[str],
        unique_symbols: Iterable[str],
    ) -> None:
        self.exact_tokens = tuple(
            sorted({self._normalise(value) for value in (*task_ids, *basenames, *unique_symbols)})
        )
        ids = {
            item.rsplit("/", 1)[-1]
            for item in task_ids
            if item.rsplit("/", 1)[-1].isdigit()
        }
        self.id_patterns = tuple(
            re.compile(
                rf"\b(?:task|instance|problem|bigcodebench)\s*[#:/_-]?\s*{re.escape(identifier)}\b"
            )
            for identifier in sorted(ids)
        )

    @staticmethod
    def _normalise(value: str) -> str:
        return unicodedata.normalize("NFKC", value).lower()

    def match(self, source: str) -> str | None:
        value = self._normalise(source)
        for token in self.exact_tokens:
            if token and token in value:
                return token
        for pattern in self.id_patterns:
            found = pattern.search(value)
            if found:
                return found.group(0)
        return None


def source_identity(source: str) -> tuple[str, str]:
    """Return byte and AST semantic identities; syntax errors are contract failures."""
    try:
        semantic = ast.dump(
            ast.parse(source), annotate_fields=True, include_attributes=False
        )
    except SyntaxError as exc:
        raise ProtocolError(f"candidate is not valid Python: {exc.msg}") from exc
    return _sha_text(source), _sha_text(semantic)


def _task_files(task: Path) -> dict[str, dict[str, object]]:
    if task.is_symlink():
        raise ProtocolError(f"task directory must not be a symlink: {task}")
    actual = {
        path.relative_to(task).as_posix()
        for path in task.rglob("*")
        if path.is_file()
    }
    if actual != set(ALLOWED_TASK_FILES):
        raise ProtocolError(f"unexpected task files in {task}: {sorted(actual)}")
    output: dict[str, dict[str, object]] = {}
    for relative in ALLOWED_TASK_FILES:
        path = task / relative
        if path.is_symlink():
            raise ProtocolError(f"task file must not be a symlink: {path}")
        payload = path.read_bytes()
        output[relative] = {"sha256": _sha_bytes(payload), "size": len(payload)}
    return output


def _assert_persistent_artifact_root(artifact_root: Path) -> Path:
    resolved = artifact_root.resolve()
    if ".claude-manager/worktrees" in resolved.as_posix():
        raise ProtocolError("artifact root must be outside disposable worktrees")
    return resolved


def build_protocol_snapshot(
    *,
    source_root: Path,
    pools: dict[str, tuple[str, ...]],
    artifact_root: Path,
    experiment_id: str,
    seed_bytes: bytes,
) -> dict:
    """Copy a read-only three-pool snapshot and write its content-addressed manifest.

    ``source_root/<role>/<task_id>`` is intentionally generic so the real builder
    can stage historical q1/q2 views without mutating their frozen locations.
    """
    expected_roles = {"training", "validation", "test"}
    if set(pools) != expected_roles:
        raise ProtocolError("pools must contain exactly training, validation, test")
    seen: set[str] = set()
    for role, task_ids in pools.items():
        repeated = seen.intersection(task_ids)
        if repeated:
            raise ProtocolError(f"pools must be disjoint; overlap: {sorted(repeated)}")
        seen.update(task_ids)
        if not task_ids:
            raise ProtocolError(f"{role} pool is empty")
    root = _assert_persistent_artifact_root(artifact_root) / experiment_id
    if root.exists():
        raise ProtocolError(f"refusing to overwrite existing experiment root: {root}")
    snapshot = root / "snapshot"
    entries: dict[str, dict] = {}
    for role, task_ids in pools.items():
        role_entries = []
        for task_id in task_ids:
            source = source_root / role / task_id
            if role == "training" and not source.exists():
                # Existing benchmark trees use the legacy filesystem spelling.
                source = source_root / "train" / task_id
            if not source.is_dir():
                raise ProtocolError(f"missing source task: {source}")
            target = snapshot / role / task_id
            shutil.copytree(source, target, symlinks=False)
            role_entries.append({
                "task_id": task_id,
                "basename": source.name,
                "path": target.relative_to(root).as_posix(),
                "files": _task_files(target),
            })
        ordered = sorted(
            task_ids,
            key=lambda item: _sha_bytes(
                b"moss-three-tier-report-block-v1\0" + item.encode("utf-8")
            ),
        )
        block_cut = (len(ordered) + 1) // 2
        entries[role] = {
            "task_ids": list(task_ids),
            "entries": role_entries,
            "report_block_a": ordered[:block_cut] if role == "test" else [],
            "report_block_b": ordered[block_cut:] if role == "test" else [],
        }
    manifest = {
        "protocol": PROTOCOL_NAME,
        "experiment_id": experiment_id,
        "seed_sha256": _sha_bytes(seed_bytes),
        "pools": entries,
        "allowed_files": list(ALLOWED_TASK_FILES),
    }
    manifest["manifest_digest"] = _sha_bytes(_canonical_json(manifest))
    _atomic_json(root / "protocol_manifest.json", manifest)
    return manifest


def verify_protocol_snapshot(manifest_path: Path) -> dict:
    manifest_path = manifest_path.resolve()
    root = manifest_path.parent
    manifest = json.loads(manifest_path.read_text())
    digest_payload = dict(manifest)
    expected_digest = digest_payload.pop("manifest_digest", None)
    actual_digest = _sha_bytes(_canonical_json(digest_payload))
    if actual_digest != expected_digest:
        raise ProtocolError("protocol manifest digest mismatch")
    pool_sets = [set(manifest["pools"][role]["task_ids"]) for role in ("training", "validation", "test")]
    if pool_sets[0] & pool_sets[1] or pool_sets[0] & pool_sets[2] or pool_sets[1] & pool_sets[2]:
        raise ProtocolError("protocol pools are not disjoint")
    for pool in manifest["pools"].values():
        for entry in pool["entries"]:
            task = root / entry["path"]
            if _task_files(task) != entry["files"]:
                raise ProtocolError(f"snapshot hash mismatch: {task}")
    return manifest


def _copy_task(source: Path, target: Path) -> None:
    """Copy a frozen task only after verifying its exact three-file contract."""
    _task_files(source)
    shutil.copytree(source, target, symlinks=False)
    _task_files(target)


def _write_reserve_task(target: Path, artifact: dict[str, str]) -> None:
    expected = {"solution", "visible", "hidden"}
    if set(artifact) != expected or not all(isinstance(artifact[key], str) for key in expected):
        raise ProtocolError("reserve artifact has an invalid importer schema")
    (target / "_hidden").mkdir(parents=True)
    (target / "solution.py").write_text(artifact["solution"])
    (target / "test_solution.py").write_text(artifact["visible"])
    (target / "_hidden" / "test_hidden.py").write_text(artifact["hidden"])
    _task_files(target)


def build_real_pool_snapshot(
    *,
    repo_root: Path,
    artifact_root: Path,
    experiment_id: str,
    seed_bytes: bytes,
    reserve_artifacts: dict[str, dict[str, str]],
) -> dict:
    """Assemble the frozen 16/20/34 view without modifying historical pools.

    The caller must obtain ``reserve_artifacts`` through the pinned importer and
    its oracle/flaky gates.  Keeping that potentially slow operation outside this
    function makes its input auditable and lets this assembly remain offline-testable.
    """
    q1_root = repo_root / "benchmarks" / "q1_external"
    q2_root = repo_root / "benchmarks" / "q2_paired"
    q1 = json.loads((q1_root / "_manifest.json").read_text())
    q2 = json.loads((q2_root / "_manifest.json").read_text())
    training_ids = tuple(q1["canary"] + q1["val"])
    validation_ids = tuple(item["task_id"] for item in q2["tasks"])
    test_ids = tuple(q1["reserve"])
    if (len(training_ids), len(validation_ids), len(test_ids)) != (
        TRAIN_SIZE, VALIDATION_SIZE, TEST_SIZE
    ):
        raise ProtocolError("frozen pool sizes do not match the qualification protocol")
    if set(reserve_artifacts) != set(test_ids):
        raise ProtocolError("reserve artifacts must contain exactly every frozen test task")
    all_ids = (*training_ids, *validation_ids, *test_ids)
    if len(set(all_ids)) != len(all_ids):
        raise ProtocolError("historical sources are not pairwise disjoint")
    q1_entries = {item["task_id"]: item for item in q1["tasks"]}
    q2_entries = {item["task_id"]: item for item in q2["tasks"]}
    if set(training_ids) != set(q1_entries) or set(validation_ids) != set(q2_entries):
        raise ProtocolError("source manifest entries do not exactly cover declared pools")

    with tempfile.TemporaryDirectory(prefix="moss-three-tier-stage-") as temporary:
        stage = Path(temporary)
        for task_id in training_ids:
            entry = q1_entries[task_id]
            _copy_task(
                q1_root / entry["split"] / entry["name"],
                stage / "training" / task_id,
            )
        for task_id in validation_ids:
            entry = q2_entries[task_id]
            source_split = f"{entry['block']}_val_v1"
            _copy_task(
                q2_root / source_split / entry["name"],
                stage / "validation" / task_id,
            )
        for task_id in test_ids:
            _write_reserve_task(stage / "test" / task_id, reserve_artifacts[task_id])
        return build_protocol_snapshot(
            source_root=stage,
            pools={
                "training": training_ids,
                "validation": validation_ids,
                "test": test_ids,
            },
            artifact_root=artifact_root,
            experiment_id=experiment_id,
            seed_bytes=seed_bytes,
        )


def rebuild_reserve_artifacts(repo_root: Path) -> dict[str, dict[str, str]]:
    """Re-run the pinned V1 oracle/flaky gate for every fresh Q1 reserve task."""
    from scripts.import_bigcodebench_hidden import (
        DATASET,
        DATASET_COMMIT,
        PARQUET_SHA256,
        fetch_official_rows,
        validate_row,
    )

    q1_manifest = json.loads(
        (repo_root / "benchmarks" / "q1_external" / "_manifest.json").read_text()
    )
    expected = {
        "dataset": DATASET,
        "dataset_commit": DATASET_COMMIT,
        "dataset_parquet_sha256": PARQUET_SHA256,
        "visibility_level": "V1",
    }
    mismatch = {
        key: (q1_manifest.get(key), value)
        for key, value in expected.items()
        if q1_manifest.get(key) != value
    }
    if mismatch:
        raise ProtocolError(f"Q1 source manifest is not the pinned import: {mismatch}")
    rows = {row["task_id"]: row for row in fetch_official_rows()}
    reserve = tuple(q1_manifest["reserve"])
    if len(reserve) != TEST_SIZE or len(set(reserve)) != TEST_SIZE:
        raise ProtocolError("Q1 reserve is not the frozen 34-task test pool")
    missing = set(reserve) - set(rows)
    if missing:
        raise ProtocolError(f"pinned dataset misses reserve tasks: {sorted(missing)}")
    artifacts: dict[str, dict[str, str]] = {}
    for task_id in reserve:
        data = validate_row(rows[task_id], "V1")
        artifacts[task_id] = {
            "solution": data["solution"],
            "visible": data["visible"],
            "hidden": data["hidden"],
        }
    return artifacts


def freeze_forbidden_instance_tokens(manifest_path: Path) -> dict:
    """Mechanically derive the static linter rule set from all frozen stubs."""
    manifest = verify_protocol_snapshot(manifest_path)
    root = manifest_path.resolve().parent
    task_ids: list[str] = []
    basenames: list[str] = []
    symbols: dict[str, set[str]] = {}
    for pool in manifest["pools"].values():
        for entry in pool["entries"]:
            task_id = entry["task_id"]
            task_ids.append(task_id)
            basenames.append(entry["basename"])
            source = (root / entry["path"] / "solution.py").read_text()
            try:
                tree = ast.parse(source)
            except SyntaxError as exc:
                raise ProtocolError(f"cannot parse frozen stub {task_id}") from exc
            for node in tree.body:
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    symbols.setdefault(node.name, set()).add(task_id)
    unique_symbols = sorted(
        symbol for symbol, owners in symbols.items() if len(owners) == 1
    )
    payload = {
        "normalization": "Unicode NFKC then lowercase",
        "task_ids": sorted(task_ids),
        "basenames": sorted(basenames),
        "unique_symbols": unique_symbols,
        "allowed_generic_filenames": ["solution.py", "test_solution.py"],
        "allowlist": [],
    }
    payload["linter_digest"] = _sha_bytes(_canonical_json(payload))
    _atomic_json(root / "forbidden_instance_tokens.json", payload)
    return payload


def build_proposer_payload(
    *, parent_source: str, visible_artifacts: Iterable[Path], family_description: str
) -> dict:
    """Construct the fixed training-only proposal schema, refusing private paths."""
    artifacts = []
    for path in visible_artifacts:
        resolved = path.resolve()
        parts = {part.lower() for part in resolved.parts}
        if {"private", "test", "selector"} & parts:
            raise ProtocolError("private selector/test artifact supplied to proposer")
        if not resolved.is_file():
            raise ProtocolError(f"visible artifact is missing: {resolved}")
        artifacts.append({"name": resolved.name, "content": resolved.read_text()})
    return {
        "schema": "three-tier-proposer-visible-v1",
        "family_description": family_description,
        "parent_source": parent_source,
        "training_artifacts": artifacts,
    }


class TestMatrix:
    """Durable test-once scheduler used only after a global final registry exists."""

    def __init__(self, *, root: Path, matrix_id: str, jobs: Iterable[str], max_in_flight: int) -> None:
        if max_in_flight != 3:
            raise ProtocolError("sealed test max_in_flight is frozen at 3")
        self.path = root / f"{matrix_id}.json"
        self.matrix_id = matrix_id
        self.jobs = tuple(sorted(jobs))
        self.max_in_flight = max_in_flight
        if self.path.exists():
            raise ProtocolError(f"test matrix already exists: {self.path}")
        _atomic_json(self.path, {
            "matrix_id": matrix_id, "status": "sealed", "registry_digest": None,
            "jobs": {job: "pending" for job in self.jobs}, "max_in_flight": max_in_flight,
        })

    def state(self) -> dict:
        return json.loads(self.path.read_text())

    def _write(self, value: dict) -> None:
        _atomic_json(self.path, value)

    def unseal(self, *, registry_digest: str | None) -> None:
        if not registry_digest:
            raise ProtocolError("global final registry is required before unseal")
        state = self.state()
        if state["status"] != "sealed":
            raise ProtocolError("test matrix has already been unsealed")
        state["status"] = "unsealed_running"
        state["registry_digest"] = registry_digest
        self._write(state)

    def claim(self) -> str | None:
        state = self.state()
        if state["status"] != "unsealed_running":
            return None
        if sum(value == "started" for value in state["jobs"].values()) >= self.max_in_flight:
            return None
        for job in self.jobs:
            if state["jobs"][job] == "pending":
                state["jobs"][job] = "started"
                self._write(state)
                return job
        return None

    def mark_lost(self, job: str) -> None:
        state = self.state()
        if state["jobs"].get(job) != "started":
            raise ProtocolError("only a durable started job can become lost")
        state["jobs"][job] = "lost"
        for key, value in state["jobs"].items():
            if value == "pending":
                state["jobs"][key] = "cancelled"
        state["status"] = "aborted_incomplete"
        self._write(state)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Prepare (but never dispatch) the three-tier qualification snapshot."
    )
    parser.add_argument("--prepare", action="store_true")
    parser.add_argument("--artifact-root", type=Path)
    parser.add_argument("--experiment-id", default="three-tier-qualification-20260728")
    parser.add_argument(
        "--seed",
        type=Path,
        default=Path("harnesses/tddgen_hidden/v001/harness.py"),
    )
    args = parser.parse_args()
    if not args.prepare:
        parser.error("only --prepare is available before P3 authorization")
    if args.artifact_root is None:
        parser.error("--artifact-root is required and must be outside a worktree")
    repo_root = REPO_ROOT
    seed = args.seed if args.seed.is_absolute() else repo_root / args.seed
    if not seed.is_file():
        raise ProtocolError(f"frozen v001 seed is missing: {seed}")
    reserve = rebuild_reserve_artifacts(repo_root)
    manifest = build_real_pool_snapshot(
        repo_root=repo_root,
        artifact_root=args.artifact_root,
        experiment_id=args.experiment_id,
        seed_bytes=seed.read_bytes(),
        reserve_artifacts=reserve,
    )
    root = args.artifact_root.resolve() / args.experiment_id
    linter = freeze_forbidden_instance_tokens(root / "protocol_manifest.json")
    print(json.dumps({
        "status": "prepared_no_model_calls",
        "manifest_digest": manifest["manifest_digest"],
        "linter_digest": linter["linter_digest"],
        "artifact_root": str(root),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
