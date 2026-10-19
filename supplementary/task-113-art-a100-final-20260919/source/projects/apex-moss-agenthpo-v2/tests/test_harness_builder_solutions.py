from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from optimization_lab.harness_builder.solutions import (
    CompilerGymSolutionCodec,
    KernelBenchXSolutionCodec,
    SolutionArchive,
    SolutionContractError,
    SWEPerfSolutionCodec,
)


def test_kernelbenchx_codec_requires_one_whole_python_artifact_and_entrypoint() -> None:
    codec = KernelBenchXSolutionCodec(task_id="Quantization/matmul_w8a8.py")
    response = """```python
import torch

def matmul_w8a8(input, weight):
    return torch.matmul(input, weight)
```"""
    artifact = codec.parse(response)

    assert artifact.extension == ".py"
    assert artifact.text.startswith("import torch")
    assert artifact.structural_signature

    with pytest.raises(SolutionContractError, match="whole response"):
        codec.parse("Here is the answer\n" + response)
    with pytest.raises(SolutionContractError, match="entrypoint"):
        codec.parse("```python\ndef unrelated(x):\n    return x\n```")


def test_kernelbenchx_reference_canary_uses_only_the_formal_candidate_segment() -> None:
    codec = KernelBenchXSolutionCodec(task_id="Quantization/matmul_w8a8.py")
    separator = "#" * 146
    source = (
        "import torch\n\n"
        "def matmul_w8a8(input, weight):\n"
        "    return torch.matmul(input, weight)\n\n"
        f"{separator}\n\n"
        "def test_matmul_w8a8():\n"
        "    return matmul_w8a8(1, 1)\n\n"
        "test_results = test_matmul_w8a8()\n"
    )
    source_sha256 = hashlib.sha256(source.encode("utf-8")).hexdigest()

    artifact = codec.reference_canary_from_frozen_task_source(
        source,
        expected_task_sha256=source_sha256,
    )

    assert separator not in artifact.text
    assert "def test_matmul_w8a8" not in artifact.text
    assert artifact.text.endswith("return torch.matmul(input, weight)\n")
    assert artifact.sha256 != source_sha256
    # The generated canary must satisfy the exact same parser as model output.
    assert codec.parse(artifact.raw_response) == artifact

    with pytest.raises(SolutionContractError, match="task source hash"):
        codec.reference_canary_from_frozen_task_source(
            source,
            expected_task_sha256="0" * 64,
        )


def test_compilergym_codec_emits_canonical_bounded_action_json() -> None:
    codec = CompilerGymSolutionCodec(benchmark_uri="benchmark://cbench-v1/qsort")
    artifact = codec.parse(
        json.dumps(
            {
                "schema_version": 1,
                "benchmark_uri": "benchmark://cbench-v1/qsort",
                "actions": ["-mem2reg", "-instcombine"],
            }
        )
    )
    assert artifact.extension == ".json"
    assert json.loads(artifact.text)["actions"] == ["-mem2reg", "-instcombine"]

    wrong = json.dumps(
        {
            "schema_version": 1,
            "benchmark_uri": "benchmark://cbench-v1/blowfish",
            "actions": ["-mem2reg"],
        }
    )
    with pytest.raises(SolutionContractError, match="lane"):
        codec.parse(wrong)


def test_sweperf_codec_accepts_only_a_whole_canonical_unified_diff() -> None:
    codec = SWEPerfSolutionCodec()
    patch = """diff --git a/pkg/module.py b/pkg/module.py
index 1111111..2222222 100644
--- a/pkg/module.py
+++ b/pkg/module.py
@@ -1 +1 @@
-old = 1
+new = 2
"""
    artifact = codec.parse(f"```diff\n{patch}```")
    assert artifact.extension == ".patch"
    assert artifact.text == patch
    assert artifact.structural_signature

    with pytest.raises(SolutionContractError, match="whole response"):
        codec.parse("explanation\n" + patch)


def test_solution_archive_is_append_only_and_hash_bound(tmp_path: Path) -> None:
    codec = CompilerGymSolutionCodec(benchmark_uri="benchmark://cbench-v1/qsort")
    first = codec.parse(
        json.dumps(
            {
                "schema_version": 1,
                "benchmark_uri": "benchmark://cbench-v1/qsort",
                "actions": ["-mem2reg"],
            }
        )
    )
    archive = SolutionArchive(tmp_path / "solutions", cell_id="suite:task:A")
    stored = archive.store("v001", first)
    assert stored == archive.store("v001", first)
    assert stored.artifact_path.is_file()
    assert stored.raw_response_path.is_file()

    second = codec.parse(
        json.dumps(
            {
                "schema_version": 1,
                "benchmark_uri": "benchmark://cbench-v1/qsort",
                "actions": ["-instcombine"],
            }
        )
    )
    with pytest.raises(ValueError, match="different content"):
        archive.store("v001", second)
