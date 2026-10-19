from __future__ import annotations

from pathlib import Path
import stat

import pytest

from optimization_lab.harness_builder.adapters.kernelbench_meta_isolation import (
    build_kernelbench_meta_namespace,
    build_kernelbench_meta_worker_command,
    stage_kernelbench_meta_runtime,
)
from optimization_lab.harness_builder.adapters.kernelbenchx_isolation import (
    BubblewrapSpec,
    SandboxContractError,
    hash_immutable_tree,
)


def _spec(tmp_path: Path) -> BubblewrapSpec:
    repository = tmp_path / "repository"
    candidate = tmp_path / "candidate.py"
    output = tmp_path / "untrusted-output"
    scratch = tmp_path / "scratch"
    cache = tmp_path / "cache"
    python_prefix = tmp_path / "python"
    headers = tmp_path / "headers"
    for directory in (
        repository / "scripts",
        output,
        scratch,
        cache,
        python_prefix / "bin",
        headers / "python3.10",
        headers / "x86_64-linux-gnu/python3.10",
    ):
        directory.mkdir(parents=True)
    (repository / "scripts/run_eval_from_files.sh").write_text(
        "#!/bin/sh\nexit 0\n", encoding="utf-8"
    )
    candidate.write_text("class ModelNew: pass\n", encoding="utf-8")
    python = python_prefix / "bin/python"
    python.write_text("fake\n", encoding="utf-8")
    python.chmod(0o755)
    (headers / "python3.10/Python.h").write_text("/* fixed */\n", encoding="utf-8")
    (headers / "x86_64-linux-gnu/python3.10/pyconfig.h").write_text(
        "/* fixed */\n", encoding="utf-8"
    )
    return BubblewrapSpec(
        bwrap_path=Path("/usr/bin/bwrap"),
        repository_snapshot=repository,
        candidate_snapshot=candidate,
        output_dir=output,
        worker_tmp_dir=scratch,
        cache_dir=cache,
        python_prefix=python_prefix,
        python_executable=python,
        python_include=headers,
        python_include_sha256=hash_immutable_tree(headers),
        gpu="4",
        system_roots=(Path("/usr"), Path("/lib")),
        gpu_devices=(Path("/dev/nvidia4"), Path("/dev/nvidiactl")),
    )


def _pairs(argv: tuple[str, ...], option: str) -> list[tuple[str, str]]:
    return [
        (argv[index + 1], argv[index + 2])
        for index, value in enumerate(argv)
        if value == option
    ]


def test_meta_namespace_is_one_gpu_read_only_no_network_and_has_no_result_channel(
    tmp_path: Path,
) -> None:
    spec = _spec(tmp_path)
    boundary = build_kernelbench_meta_namespace(spec)
    argv = boundary.argv_prefix
    environment = {
        argv[index + 1]: argv[index + 2]
        for index, value in enumerate(argv)
        if value == "--setenv"
    }

    assert "--unshare-all" in argv
    assert "--unshare-net" in argv
    assert "--clearenv" in argv
    assert "--cap-drop" in argv
    assert environment["CUDA_VISIBLE_DEVICES"] == "0"
    assert environment["CPATH"] == (
        "/opt/hb-python-include/python3.10:/opt/hb-python-include"
    )
    assert (str(spec.repository_snapshot), "/sandbox/repository") in _pairs(
        argv, "--ro-bind"
    )
    assert (str(spec.candidate_snapshot), boundary.candidate_mount) in _pairs(
        argv, "--ro-bind"
    )
    assert ("/dev/nvidia4", "/dev/nvidia4") in _pairs(argv, "--dev-bind")
    assert ("/dev/nvidia0", "/dev/nvidia0") not in _pairs(argv, "--dev-bind")
    assert str(spec.python_include) in argv
    assert boundary.worker_uid == 65534
    assert boundary.worker_gid == 65534
    assert "/bin/bash" not in argv
    assert "run_and_check.py" not in "\0".join(argv)
    assert str(tmp_path / "private/result-nonce.json") not in "\0".join(argv)


def _runtime_source(root: Path) -> None:
    for relative in (
        "optimization_lab/harness_builder/adapters/kernel_candidate_policy.py",
        "optimization_lab/harness_builder/adapters/kernel_candidate_invocation.py",
        "optimization_lab/harness_builder/adapters/kernelbench_meta_worker.py",
    ):
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"# fixed {relative}\n", encoding="utf-8")


def test_meta_runtime_tree_is_read_only_but_traversable_by_remapped_worker(
    tmp_path: Path,
) -> None:
    project = tmp_path / "project"
    _runtime_source(project)
    runtime = stage_kernelbench_meta_runtime(
        project_root=project, staging_root=tmp_path / "staged-runtime"
    )

    assert stat.S_IMODE(runtime.root.stat().st_mode) == 0o555
    assert all(
        stat.S_IMODE(path.stat().st_mode) in {0o444, 0o555}
        for path in runtime.root.rglob("*")
    )


def test_meta_worker_command_preserves_only_canonical_fd3_and_mounts_runtime_ro(
    tmp_path: Path,
) -> None:
    project = tmp_path / "project"
    _runtime_source(project)
    runtime = stage_kernelbench_meta_runtime(
        project_root=project, staging_root=tmp_path / "staged-runtime"
    )
    command = build_kernelbench_meta_worker_command(
        spec=_spec(tmp_path / "sandbox"),
        runtime=runtime,
        result_fd=3,
        worker_arguments=("--health-only",),
    )
    argv = command.launch.argv

    assert (str(runtime.root), "/opt/hb-kernelbench-meta-runtime") in _pairs(
        argv, "--ro-bind"
    )
    preserve = argv.index("--preserve-fds")
    assert argv[preserve + 1] == "1"
    assert argv[-2:] == ("--result-fd", "3")
    assert "/bin/bash" not in argv

    with pytest.raises(SandboxContractError, match="canonical fd 3"):
        build_kernelbench_meta_worker_command(
            spec=_spec(tmp_path / "other-sandbox"),
            runtime=runtime,
            result_fd=4,
            worker_arguments=("--health-only",),
        )
