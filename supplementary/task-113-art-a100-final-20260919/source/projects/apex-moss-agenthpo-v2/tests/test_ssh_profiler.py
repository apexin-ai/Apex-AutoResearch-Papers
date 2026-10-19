from __future__ import annotations

import json
from pathlib import Path

import pytest

from optimization_lab.adapters.profile_cache_summary import (
    parse_resource_usage,
    summarize_cache,
)
from optimization_lab.adapters.ssh_profiler import parse_nsys_json


def test_parse_resource_usage_extracts_registers_and_local_memory() -> None:
    parsed = parse_resource_usage(
        """Resource usage:
 Common:
  GLOBAL:11 CONSTANT[4]:8
 Function _kernel:
  REG:48 STACK:0 SHARED:1024 LOCAL:16 CONSTANT[0]:400 TEXTURE:0
"""
    )

    assert parsed == {
        "_kernel": {
            "registers_per_thread": 48,
            "stack_bytes": 0,
            "static_shared_bytes": 1024,
            "local_bytes": 16,
        }
    }


def test_cache_summary_reports_compiler_resources_and_theoretical_occupancy(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source = tmp_path / "candidate.py"
    source.write_text(
        """import triton

@triton.jit
def _kernel(x):
    return

class ModelNew:
    pass
""",
        encoding="utf-8",
    )
    cache = tmp_path / "cache/hash"
    cache.mkdir(parents=True)
    (cache / "_kernel.json").write_text(
        json.dumps(
            {
                "name": "_kernel",
                "num_warps": 4,
                "num_stages": 3,
                "shared": 1024,
            }
        ),
        encoding="utf-8",
    )
    (cache / "_kernel.cubin").write_bytes(b"fake")

    class Result:
        returncode = 0
        stdout = (
            "Function _kernel:\n"
            " REG:48 STACK:0 SHARED:1024 LOCAL:0 CONSTANT[0]:400\n"
        )

    monkeypatch.setattr(
        "optimization_lab.adapters.profile_cache_summary.subprocess.run",
        lambda *args, **kwargs: Result(),
    )

    summary = summarize_cache(cache.parent, source)

    assert summary["kernel_names"] == ["_kernel"]
    assert summary["registers_per_thread"] == 48
    assert summary["shared_memory_bytes"] == 1024
    assert summary["num_warps"] == 4
    assert summary["num_stages"] == 3
    assert 0 < summary["theoretical_occupancy_pct"] <= 100


def test_parse_nsys_json_ignores_processing_preamble() -> None:
    output = """Processing report...\n[
  {"Name": "_kernel", "Instances": 10, "Total Time (ns)": 5000, "Avg (ns)": 500}
]\n"""

    assert parse_nsys_json(output) == [
        {
            "Name": "_kernel",
            "Instances": 10,
            "Total Time (ns)": 5000,
            "Avg (ns)": 500,
        }
    ]
