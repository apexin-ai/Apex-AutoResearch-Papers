from __future__ import annotations

import argparse
import ast
import json
import re
import subprocess
from pathlib import Path
from typing import Any


def candidate_kernel_names(source_path: Path) -> list[str]:
    tree = ast.parse(source_path.read_text(encoding="utf-8"))
    names = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        decorators = [ast.unparse(item) for item in node.decorator_list]
        if any(item.endswith("triton.jit") or item.endswith("triton.autotune") for item in decorators):
            names.append(node.name)
    return sorted(set(names))


def parse_resource_usage(output: str) -> dict[str, dict[str, int]]:
    resources: dict[str, dict[str, int]] = {}
    current: str | None = None
    for line in output.splitlines():
        match = re.match(r"\s*Function\s+(.+?):\s*$", line)
        if match:
            current = match.group(1).strip()
            continue
        if current is None:
            continue
        values = {
            key: int(value)
            for key, value in re.findall(r"\b(REG|STACK|SHARED|LOCAL):(\d+)", line)
        }
        if values:
            resources[current] = {
                "registers_per_thread": values.get("REG", 0),
                "stack_bytes": values.get("STACK", 0),
                "static_shared_bytes": values.get("SHARED", 0),
                "local_bytes": values.get("LOCAL", 0),
            }
            current = None
    return resources


def summarize_cache(cache_root: Path, source_path: Path) -> dict[str, Any]:
    expected_names = candidate_kernel_names(source_path)
    metadata = []
    resource_rows = []
    for path in cache_root.rglob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        name = data.get("name") if isinstance(data, dict) else None
        if not isinstance(name, str) or not _matches_expected(name, expected_names):
            continue
        metadata.append(
            {
                "name": name,
                "num_warps": _positive_int(data.get("num_warps")),
                "num_stages": _positive_int(data.get("num_stages")),
                "shared_memory_bytes": _nonnegative_int(data.get("shared")),
            }
        )
        cubin = path.with_suffix(".cubin")
        if cubin.is_file():
            process = subprocess.run(
                ["cuobjdump", "--dump-resource-usage", str(cubin)],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=60,
                check=False,
            )
            if process.returncode == 0:
                for function, row in parse_resource_usage(process.stdout).items():
                    if _matches_expected(function, expected_names):
                        resource_rows.append({"name": function, **row})
    registers = [row["registers_per_thread"] for row in resource_rows if row["registers_per_thread"] > 0]
    shared = [
        max(
            int(row.get("static_shared_bytes") or 0),
            int(next((item["shared_memory_bytes"] for item in metadata if item["name"] == row["name"]), 0) or 0),
        )
        for row in resource_rows
    ]
    shared.extend(
        int(item["shared_memory_bytes"])
        for item in metadata
        if item["shared_memory_bytes"] is not None
    )
    warps = [int(item["num_warps"]) for item in metadata if item["num_warps"]]
    stages = [int(item["num_stages"]) for item in metadata if item["num_stages"]]
    occupancy = []
    for item in metadata:
        name = str(item["name"])
        resource = next((row for row in resource_rows if row["name"] == name), None)
        if resource and item["num_warps"]:
            occupancy.append(
                theoretical_a100_occupancy(
                    num_warps=int(item["num_warps"]),
                    registers_per_thread=int(resource["registers_per_thread"]),
                    shared_memory_bytes=int(item["shared_memory_bytes"] or 0),
                )
            )
    return {
        "kernel_names": expected_names,
        "metadata": metadata,
        "resources": resource_rows,
        "registers_per_thread": max(registers) if registers else None,
        "local_memory_bytes": max((row["local_bytes"] for row in resource_rows), default=None),
        "shared_memory_bytes": max(shared) if shared else None,
        "num_warps": max(warps) if warps else None,
        "num_stages": max(stages) if stages else None,
        "theoretical_occupancy_pct": min(occupancy) if occupancy else None,
    }


def theoretical_a100_occupancy(
    *, num_warps: int, registers_per_thread: int, shared_memory_bytes: int
) -> float:
    threads = num_warps * 32
    if threads <= 0:
        return 0.0
    limits = [32, 2048 // threads]
    if registers_per_thread > 0:
        limits.append(65_536 // (registers_per_thread * threads))
    if shared_memory_bytes > 0:
        limits.append(163_840 // shared_memory_bytes)
    blocks = max(0, min(limits))
    return min(100.0, blocks * threads / 2048 * 100.0)


def _matches_expected(name: str, expected: list[str]) -> bool:
    return any(item in name for item in expected)


def _positive_int(value: object) -> int | None:
    return int(value) if isinstance(value, int) and value > 0 else None


def _nonnegative_int(value: object) -> int | None:
    return int(value) if isinstance(value, int) and value >= 0 else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache-root", type=Path, required=True)
    parser.add_argument("--candidate-source", type=Path, required=True)
    args = parser.parse_args()
    print(
        json.dumps(
            summarize_cache(args.cache_root, args.candidate_source),
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
