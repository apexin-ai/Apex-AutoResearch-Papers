"""Build the frozen BigCodeBench-Hard hidden-verification canary.

The five task IDs are inherited from the earlier full-visibility canary. The only
calibration variable is the preregistered visible-test level (V0/V1/V2). Official
canonical solutions are used for import-time validation and never written under
benchmarks/.
"""

import argparse
import ast
import hashlib
import importlib.metadata
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

try:
    from scripts.import_bigcodebench_hard_canary import (
        CHOSEN,
        CONFIG,
        DATASET,
        SPLIT,
        TEST_TEMPLATE,
        build_solution,
        fetch_rows,
        run_pytest,
        select_rows,
    )
except ModuleNotFoundError:  # Direct execution: python scripts/this_file.py
    from import_bigcodebench_hard_canary import (  # type: ignore[no-redef]
        CHOSEN,
        CONFIG,
        DATASET,
        SPLIT,
        TEST_TEMPLATE,
        build_solution,
        fetch_rows,
        run_pytest,
        select_rows,
    )

try:
    from scripts.mutate_bugfix_hidden import (
        MUTATION_SEED,
        OPERATOR_ORDER,
        select_accepted_mutation,
    )
except ModuleNotFoundError:  # Direct execution: python scripts/this_file.py
    from mutate_bugfix_hidden import (  # type: ignore[no-redef]
        MUTATION_SEED,
        OPERATOR_ORDER,
        select_accepted_mutation,
    )

LEVELS = {"V0": 0, "V1": 1, "V2": 2}
SIDE_EFFECT_BLACKLIST = {
    "subprocess",
    "socket",
    "ftplib",
    "smtplib",
    "telnetlib",
    "requests",
    "flask",
    "django",
    "selenium",
    "tkinter",
    "turtle",
    "multiprocessing",
}
DATASET_COMMIT = "298d2cc7b96612e15e47313c3603ee124cee0c1f"
PARQUET_SHA256 = "73a4270b43feb81abefad7bb1b592937c768ea45c3263bedc1cabd30a9a6ce79"
PARQUET_URL = (
    "https://huggingface.co/datasets/bigcode/bigcodebench-hard/resolve/"
    f"{DATASET_COMMIT}/data/v0.1.4-00000-of-00001.parquet"
)
OUT = (
    Path(__file__).resolve().parent.parent
    / "benchmarks"
    / "tddgen_hidden"
    / "canary"
)
MANIFEST = OUT / "_manifest.json"

SMOKE_TEMPLATE = """import pytest
import solution

pytestmark = pytest.mark.timeout(20)


def test_solution_imports_and_entry_point_is_callable():
    assert callable(solution.{entry_point})
"""


def _is_testcase_class(node: ast.ClassDef) -> bool:
    for base in node.bases:
        if isinstance(base, ast.Name) and base.id == "TestCase":
            return True
        if isinstance(base, ast.Attribute) and base.attr == "TestCase":
            return True
    return False


def fetch_rows_from_frozen_parquet() -> list[dict]:
    """Read the content-addressed official file when the rows service is down."""
    with urllib.request.urlopen(PARQUET_URL, timeout=60) as response:
        payload = response.read()
    digest = hashlib.sha256(payload).hexdigest()
    if digest != PARQUET_SHA256:
        raise ValueError(
            f"official parquet sha256 mismatch: expected {PARQUET_SHA256}, "
            f"got {digest}"
        )
    try:
        import pyarrow as pa
        import pyarrow.parquet as pq
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "the rows service is unavailable; install pinned pyarrow==18.1.0 "
            "to read the frozen official parquet fallback"
        ) from exc
    return pq.read_table(pa.BufferReader(payload)).to_pylist()


def fetch_official_rows() -> list[dict]:
    try:
        return fetch_rows()
    except (urllib.error.HTTPError, urllib.error.URLError):
        return fetch_rows_from_frozen_parquet()


def _behavior_methods(tree: ast.Module) -> list[tuple[ast.ClassDef, ast.AST]]:
    methods = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef) or not _is_testcase_class(node):
            continue
        for child in node.body:
            if (
                isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef))
                and child.name.startswith("test_")
            ):
                methods.append((node, child))
    return sorted(methods, key=lambda item: item[1].lineno)


def list_behavior_tests(source: str) -> list[str]:
    tree = ast.parse(source)
    return [
        f"{class_node.name}.{method.name}"
        for class_node, method in _behavior_methods(tree)
    ]


def split_behavior_tests(source: str, keep: int) -> tuple[str, list[str]]:
    """Keep the first k unittest methods while preserving fixtures and helpers."""
    if keep < 0:
        raise ValueError("visible test count must be non-negative")
    tree = ast.parse(source)
    methods = _behavior_methods(tree)
    kept_nodes = {id(method) for _, method in methods[:keep]}
    kept_names = [
        f"{class_node.name}.{method.name}"
        for class_node, method in methods[:keep]
    ]
    for class_node in {
        id(node): node for node, _ in methods
    }.values():
        class_node.body = [
            child for child in class_node.body
            if not (
                isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef))
                and child.name.startswith("test_")
                and id(child) not in kept_nodes
            )
        ]
    ast.fix_missing_locations(tree)
    source = ast.unparse(tree)
    return source.rstrip() + "\n", kept_names


def _wrap_tests(raw_tests: str) -> str:
    normalized = "\n".join(
        line.rstrip() for line in raw_tests.lstrip().rstrip().splitlines()
    )
    return TEST_TEMPLATE.format(tests=normalized)


def build_visible_test(row: dict, level: str) -> tuple[str, list[str]]:
    if level not in LEVELS:
        raise ValueError(f"unknown visibility level: {level}")
    k = LEVELS[level]
    if k == 0:
        return (
            SMOKE_TEMPLATE.format(entry_point=row["entry_point"]),
            [],
        )
    raw_tests, names = split_behavior_tests(row["test"], k)
    if len(names) != k:
        raise ValueError(
            f"{row['task_id']}: expected at least {k} unittest test methods, "
            f"found {len(names)}"
        )
    return _wrap_tests(raw_tests), names


def build_hidden_test(row: dict) -> tuple[str, list[str]]:
    names = list_behavior_tests(row["test"])
    if not names:
        raise ValueError(f"{row['task_id']}: no unittest behavior tests found")
    return _wrap_tests(row["test"]), names


def _output_tail(result) -> str:
    return (result.stdout + result.stderr)[-2000:]


def validate_row(row: dict, level: str) -> dict:
    visible, visible_names = build_visible_test(row, level)
    hidden, hidden_names = build_hidden_test(row)
    stub = build_solution(row)
    oracle = build_solution(row, oracle=True)

    stub_hidden = run_pytest(stub, hidden)
    if stub_hidden.returncode == 0:
        raise ValueError(f"{row['task_id']}: stub unexpectedly passes hidden suite")

    oracle_hidden_first = run_pytest(oracle, hidden)
    oracle_hidden_second = run_pytest(oracle, hidden)
    if (
        oracle_hidden_first.returncode != 0
        or oracle_hidden_second.returncode != 0
    ):
        raise ValueError(
            f"{row['task_id']}: oracle fails hidden suite\n"
            f"{_output_tail(oracle_hidden_first)}\n"
            f"{_output_tail(oracle_hidden_second)}"
        )
    if oracle_hidden_first.returncode != oracle_hidden_second.returncode:
        raise ValueError(f"{row['task_id']}: hidden suite outcome is flaky")

    oracle_visible = run_pytest(oracle, visible)
    if oracle_visible.returncode != 0:
        raise ValueError(
            f"{row['task_id']}: oracle fails visible suite\n"
            f"{_output_tail(oracle_visible)}"
        )

    return {
        "solution": stub,
        "visible": visible,
        "hidden": hidden,
        "visible_tests": visible_names,
        "hidden_tests": hidden_names,
    }


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def partition_qualified_rows(
        rows) -> tuple[list[dict], list[dict], str]:
    ordered = sorted(
        list(rows),
        key=lambda row: hashlib.sha256(row["task_id"].encode()).hexdigest(),
    )
    order_text = "\n".join(row["task_id"] for row in ordered) + "\n"
    return ordered[::2], ordered[1::2], _sha256(order_text)


def choose_family_sizes(n_family_a: int, n_family_b: int) -> tuple[int, int]:
    if min(n_family_a, n_family_b) >= 22:
        return 10, 12
    if min(n_family_a, n_family_b) >= 18:
        return 8, 10
    raise ValueError(
        "formal pool has fewer than 18 qualified tasks in at least one family"
    )


def filter_candidate_rows(
        rows: list[dict], allowed_libs: set[str]
) -> tuple[list[dict], list[dict]]:
    eligible = []
    excluded = []
    for row in rows:
        task_id = row["task_id"]
        libs = set(_libs(row))
        if task_id in CHOSEN:
            excluded.append({"task_id": task_id, "reason": "canary"})
            continue
        blacklisted = sorted(libs & SIDE_EFFECT_BLACKLIST)
        if blacklisted:
            excluded.append({
                "task_id": task_id,
                "reason": f"side_effect_blacklist:{','.join(blacklisted)}",
            })
            continue
        unavailable = sorted(libs - allowed_libs)
        if unavailable:
            excluded.append({
                "task_id": task_id,
                "reason": f"unavailable_libs:{','.join(unavailable)}",
            })
            continue
        eligible.append(row)
    return eligible, excluded


def _libs(row: dict) -> list[str]:
    value = row["libs"]
    return ast.literal_eval(value) if isinstance(value, str) else value


def environment_contract() -> tuple[set[str], dict]:
    packages = {}
    for distribution in importlib.metadata.distributions():
        name = distribution.metadata.get("Name")
        if name:
            packages[name] = distribution.version
    top_level = set(importlib.metadata.packages_distributions())
    allowed = (
        set(sys.stdlib_module_names) | top_level
    ) - SIDE_EFFECT_BLACKLIST
    return allowed, {
        "python": sys.version.split()[0],
        "packages": dict(sorted(packages.items(), key=lambda item: item[0].lower())),
        "allowed_libs": sorted(allowed),
        "allowed_libs_sha256": _sha256("\n".join(sorted(allowed)) + "\n"),
        "side_effect_blacklist": sorted(SIDE_EFFECT_BLACKLIST),
    }


def qualify_formal_rows(
        rows: list[dict], level: str
) -> tuple[list[dict], dict[str, dict], list[dict]]:
    qualified = []
    artifacts = {}
    excluded = []
    for index, row in enumerate(rows, 1):
        task_id = row["task_id"]
        try:
            artifacts[task_id] = validate_row(row, level)
        except Exception as exc:
            reason = str(exc).splitlines()[0][:300]
            excluded.append({
                "task_id": task_id,
                "reason": f"quality_gate:{type(exc).__name__}:{reason}",
            })
            print(
                f"SKIP quality {task_id}: {type(exc).__name__}: {reason}",
                flush=True,
            )
            continue
        qualified.append(row)
        print(
            f"QUALIFIED {index}/{len(rows)} {task_id}",
            flush=True,
        )
    return qualified, artifacts, excluded


def _task_entry(
        row: dict,
        artifacts: dict,
        split: str,
        solution: str,
        solution_kind: str,
        mutation=None,
) -> dict:
    entry = {
        "task_id": row["task_id"],
        "name": row["task_id"].replace("/", "_").lower(),
        "split": split,
        "entry_point": row["entry_point"],
        "score": row["score"],
        "libs": _libs(row),
        "solution_kind": solution_kind,
        "visible_tests": artifacts["visible_tests"],
        "hidden_tests": artifacts["hidden_tests"],
        "sha256": {
            "solution.py": _sha256(solution),
            "test_solution.py": _sha256(artifacts["visible"]),
            "_hidden/test_hidden.py": _sha256(artifacts["hidden"]),
        },
    }
    if mutation is not None:
        entry["mutation"] = {
            "operator": mutation.operator,
            "location": mutation.location,
            "seed": MUTATION_SEED,
        }
    return entry


def _write_family(
        family: str,
        train_rows: list,
        val_rows: list,
        reserve_rows: list,
        artifacts: dict[str, dict],
        solutions: dict[str, tuple[str, object | None]],
        common: dict,
        *,
        solution_kind: str,
        family_specific: dict,
) -> dict:
    root = Path(__file__).resolve().parent.parent / "benchmarks" / family
    for split in ("train", "val"):
        if (root / split).exists():
            raise ValueError(
                f"refusing to overwrite frozen formal split: {root / split}"
            )

    task_entries = []
    for split, rows in (("train", train_rows), ("val", val_rows)):
        for row in rows:
            task_id = row["task_id"]
            solution, mutation = solutions[task_id]
            data = artifacts[task_id]
            name = task_id.replace("/", "_").lower()
            task_dir = root / split / name
            hidden_dir = task_dir / "_hidden"
            hidden_dir.mkdir(parents=True)
            (task_dir / "solution.py").write_text(solution)
            (task_dir / "test_solution.py").write_text(data["visible"])
            (hidden_dir / "test_hidden.py").write_text(data["hidden"])
            task_entries.append(_task_entry(
                row,
                data,
                split,
                solution,
                solution_kind,
                mutation,
            ))

    manifest = {
        **common,
        "family": family,
        "solution_kind": solution_kind,
        "train_size": len(train_rows),
        "val_size": len(val_rows),
        "train": [row["task_id"] for row in train_rows],
        "val": [row["task_id"] for row in val_rows],
        "reserve": [row["task_id"] for row in reserve_rows],
        "tasks": task_entries,
        **family_specific,
    }
    root.mkdir(parents=True, exist_ok=True)
    (root / "_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n"
    )
    return manifest


def write_formal_benchmarks(level: str = "V1") -> tuple[dict, dict]:
    if level != "V1":
        raise ValueError("formal protocol was frozen at V1")

    rows = fetch_official_rows()
    allowed_libs, environment = environment_contract()
    candidates, filter_excluded = filter_candidate_rows(rows, allowed_libs)
    qualified, artifacts, quality_excluded = qualify_formal_rows(
        candidates, level
    )
    family_a, family_b, order_hash = partition_qualified_rows(qualified)
    train_size, val_size = choose_family_sizes(
        len(family_a), len(family_b)
    )
    needed = train_size + val_size

    common = {
        "dataset": DATASET,
        "config": CONFIG,
        "split": SPLIT,
        "dataset_commit": DATASET_COMMIT,
        "dataset_parquet_sha256": PARQUET_SHA256,
        "protocol": "hidden-final-verification",
        "visibility_level": level,
        "visible_behavior_tests": LEVELS[level],
        "hidden_suite": "complete official suite",
        "selection_algorithm": (
            "filter before model runs; sha256(task_id) ascending; odd positions "
            "family A, even positions family B; family-local first train then val"
        ),
        "qualified_order_sha256": order_hash,
        "qualified_order": [
            row["task_id"] for row in sorted(
                qualified,
                key=lambda row: hashlib.sha256(
                    row["task_id"].encode()
                ).hexdigest(),
            )
        ],
        "canary_excluded": CHOSEN,
        "filter_excluded": filter_excluded,
        "quality_excluded": quality_excluded,
        "environment": environment,
        "size_rule": {
            "requested": {"train": 10, "val": 12},
            "selected": {"train": train_size, "val": val_size},
            "minimum": {"train": 8, "val": 10},
        },
    }

    selected_a = family_a[:needed]
    solutions_a = {
        row["task_id"]: (artifacts[row["task_id"]]["solution"], None)
        for row in family_a
    }

    accepted_mutations = []
    rejected_mutations = []
    canonical_solutions = {}
    for index, row in enumerate(family_b, 1):
        task_id = row["task_id"]
        canonical = build_solution(row, oracle=True)
        mutation = select_accepted_mutation(
            canonical,
            artifacts[task_id]["visible"],
            artifacts[task_id]["hidden"],
        )
        if mutation is None:
            rejected_mutations.append({
                "task_id": task_id,
                "reason": "no_visible_pass_hidden_fail_mutation",
            })
            print(
                f"NO MUTATION {index}/{len(family_b)} {task_id}",
                flush=True,
            )
            continue
        accepted_mutations.append(row)
        canonical_solutions[task_id] = (mutation.source, mutation)
        print(
            f"MUTATED {index}/{len(family_b)} {task_id}: "
            f"{mutation.operator}@{mutation.location}",
            flush=True,
        )

    if len(accepted_mutations) >= needed:
        family_b_name = "bugfix_hidden"
        selected_b = accepted_mutations[:needed]
        artifacts_b = artifacts
        solutions_b = canonical_solutions
        solution_kind_b = "deterministic_ast_mutation"
        fallback = None
        reserve_b = accepted_mutations[needed:]
    else:
        family_b_name = "specgen_hidden"
        selected_b = family_b[:needed]
        if len(selected_b) < needed:
            raise ValueError("family B is below the preregistered minimum size")
        artifacts_b = dict(artifacts)
        solutions_b = {}
        for row in family_b:
            task_id = row["task_id"]
            visible, visible_names = build_visible_test(row, "V0")
            oracle_visible = run_pytest(
                build_solution(row, oracle=True), visible
            )
            if oracle_visible.returncode != 0:
                raise ValueError(
                    f"{task_id}: oracle fails specgen V0 smoke"
                )
            artifacts_b[task_id] = {
                **artifacts[task_id],
                "visible": visible,
                "visible_tests": visible_names,
            }
            solutions_b[task_id] = (build_solution(row), None)
        solution_kind_b = "stub"
        fallback = (
            "bugfix mutation pipeline produced fewer than the required "
            f"{needed} tasks; preregistered specgen_hidden V0 fallback"
        )
        reserve_b = family_b[needed:]

    manifest_a = _write_family(
        "tddgen_hidden",
        selected_a[:train_size],
        selected_a[train_size:needed],
        family_a[needed:],
        artifacts,
        solutions_a,
        common,
        solution_kind="stub",
        family_specific={
            "assigned_pool": [row["task_id"] for row in family_a],
        },
    )
    manifest_b = _write_family(
        family_b_name,
        selected_b[:train_size],
        selected_b[train_size:needed],
        reserve_b,
        artifacts_b,
        solutions_b,
        {
            **common,
            "visibility_level": (
                "V1" if family_b_name == "bugfix_hidden" else "V0"
            ),
            "visible_behavior_tests": (
                1 if family_b_name == "bugfix_hidden" else 0
            ),
        },
        solution_kind=solution_kind_b,
        family_specific={
            "assigned_pool": [row["task_id"] for row in family_b],
            "mutation_seed": MUTATION_SEED,
            "mutation_operator_order": OPERATOR_ORDER,
            "mutation_rejected": rejected_mutations,
            "fallback": fallback,
        },
    )
    return manifest_a, manifest_b


def write_canary(rows: list[dict], level: str, *, validate: bool = True) -> dict:
    prepared = []
    for row in rows:
        artifacts = (
            validate_row(row, level) if validate
            else {
                "solution": build_solution(row),
                "visible": build_visible_test(row, level)[0],
                "hidden": build_hidden_test(row)[0],
                "visible_tests": build_visible_test(row, level)[1],
                "hidden_tests": build_hidden_test(row)[1],
            }
        )
        prepared.append((row, artifacts))

    manifest = {
        "dataset": DATASET,
        "config": CONFIG,
        "split": SPLIT,
        "selection": CHOSEN,
        "selection_rule": (
            "reuse the five task IDs frozen before the full-visibility canary; "
            "never eligible for formal train/val"
        ),
        "protocol": "hidden-final-verification",
        "visibility_level": level,
        "visible_behavior_tests": LEVELS[level],
        "hidden_suite": "complete official suite",
        "tasks": [],
    }
    OUT.mkdir(parents=True, exist_ok=True)
    for row, artifacts in prepared:
        name = row["task_id"].replace("/", "_").lower()
        task_dir = OUT / name
        hidden_dir = task_dir / "_hidden"
        hidden_dir.mkdir(parents=True, exist_ok=True)
        (task_dir / "solution.py").write_text(artifacts["solution"])
        (task_dir / "test_solution.py").write_text(artifacts["visible"])
        (hidden_dir / "test_hidden.py").write_text(artifacts["hidden"])
        manifest["tasks"].append({
            "task_id": row["task_id"],
            "name": name,
            "entry_point": row["entry_point"],
            "score": row["score"],
            "libs": _libs(row),
            "visible_tests": artifacts["visible_tests"],
            "hidden_tests": artifacts["hidden_tests"],
            "sha256": {
                "solution.py": _sha256(artifacts["solution"]),
                "test_solution.py": _sha256(artifacts["visible"]),
                "_hidden/test_hidden.py": _sha256(artifacts["hidden"]),
            },
        })
        print(
            f"OK {name} ({level}: {len(artifacts['visible_tests'])} visible, "
            f"{len(artifacts['hidden_tests'])} hidden)"
        )

    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=LEVELS, default="V1")
    parser.add_argument(
        "--formal",
        action="store_true",
        help="build the frozen formal train/val families after canary calibration",
    )
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="write tasks without running the offline stub/oracle gates",
    )
    args = parser.parse_args()
    if args.formal:
        if args.skip_validation:
            raise SystemExit("--skip-validation is forbidden for formal imports")
        write_formal_benchmarks(args.level)
    else:
        rows = select_rows(fetch_official_rows())
        write_canary(rows, args.level, validate=not args.skip_validation)


if __name__ == "__main__":
    main()
