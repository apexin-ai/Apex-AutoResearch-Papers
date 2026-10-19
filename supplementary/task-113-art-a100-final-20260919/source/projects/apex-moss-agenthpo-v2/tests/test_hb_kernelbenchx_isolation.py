from __future__ import annotations

import os
import signal
import subprocess
from pathlib import Path

import pytest

from optimization_lab.harness_builder.adapters.kernelbenchx_isolation import (
    BubblewrapSpec,
    SandboxContractError,
    build_bubblewrap_command,
    ensure_process_group_quiescent,
    hash_immutable_tree,
    run_bubblewrap_process,
    stage_git_worker_inputs,
)


def _tree(tmp_path: Path) -> dict[str, Path]:
    repository = tmp_path / "staged-repository"
    candidate = tmp_path / "staged-candidate.py"
    output = tmp_path / "worker-output"
    worker_tmp = tmp_path / "worker-tmp"
    cache = tmp_path / "worker-cache"
    python_prefix = tmp_path / "python-prefix"
    python_include = tmp_path / "python-include"
    for directory in (
        repository,
        output,
        worker_tmp,
        cache,
        python_prefix / "bin",
        python_include / "python3.10",
        python_include / "x86_64-linux-gnu/python3.10",
    ):
        directory.mkdir(parents=True)
    (repository / "scripts").mkdir()
    (repository / "scripts/run_eval_from_files.sh").write_text(
        "#!/bin/sh\nexit 0\n", encoding="utf-8"
    )
    candidate.write_text("def kernel_function(x): return x\n", encoding="utf-8")
    python = python_prefix / "bin/python"
    python.write_text("fake executable\n", encoding="utf-8")
    python.chmod(0o755)
    (python_include / "python3.10/Python.h").write_text(
        "/* frozen */\n", encoding="utf-8"
    )
    (python_include / "x86_64-linux-gnu/python3.10/pyconfig.h").write_text(
        "/* frozen multiarch */\n", encoding="utf-8"
    )
    return {
        "repository": repository,
        "candidate": candidate,
        "output": output,
        "worker_tmp": worker_tmp,
        "cache": cache,
        "python_prefix": python_prefix,
        "python": python,
        "python_include": python_include,
    }


def _spec(tmp_path: Path) -> BubblewrapSpec:
    tree = _tree(tmp_path)
    return BubblewrapSpec(
        bwrap_path=Path("/usr/bin/bwrap"),
        repository_snapshot=tree["repository"],
        candidate_snapshot=tree["candidate"],
        output_dir=tree["output"],
        worker_tmp_dir=tree["worker_tmp"],
        cache_dir=tree["cache"],
        python_prefix=tree["python_prefix"],
        python_executable=tree["python"],
        python_include=tree["python_include"],
        python_include_sha256=hash_immutable_tree(tree["python_include"]),
        gpu="4",
        system_roots=(Path("/usr"), Path("/lib")),
        gpu_devices=(Path("/dev/nvidia4"), Path("/dev/nvidiactl")),
    )


def _mount_pairs(argv: tuple[str, ...], option: str) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for index, value in enumerate(argv):
        if value == option:
            pairs.append((argv[index + 1], argv[index + 2]))
    return pairs


def test_bubblewrap_command_has_real_permission_and_namespace_boundaries(
    tmp_path: Path,
) -> None:
    spec = _spec(tmp_path)
    launch = build_bubblewrap_command(spec)
    argv = launch.argv

    assert argv[0] == "/usr/bin/bwrap"
    assert "--unshare-all" in argv
    assert "--unshare-net" in argv
    assert "--die-with-parent" in argv
    assert "--new-session" in argv
    assert argv[argv.index("--uid") + 1] == "65534"
    assert argv[argv.index("--gid") + 1] == "65534"
    assert (str(spec.repository_snapshot), "/sandbox/repository") in _mount_pairs(
        argv, "--ro-bind"
    )
    assert (str(spec.candidate_snapshot), launch.candidate_mount) in _mount_pairs(
        argv, "--ro-bind"
    )
    assert (str(spec.output_dir), "/sandbox/output") in _mount_pairs(argv, "--bind")
    assert (str(spec.worker_tmp_dir), "/sandbox/work") in _mount_pairs(argv, "--bind")
    assert (str(spec.cache_dir), "/sandbox/cache") in _mount_pairs(argv, "--bind")
    assert ("/", "/") not in _mount_pairs(argv, "--ro-bind")
    assert "--clearenv" in argv
    assert "--cap-drop" in argv
    assert launch.cwd == spec.worker_tmp_dir
    assert launch.worker_uid == 65534
    assert launch.worker_gid == 65534


def test_single_physical_gpu_is_renumbered_to_worker_logical_gpu_zero(
    tmp_path: Path,
) -> None:
    spec = _spec(tmp_path)
    launch = build_bubblewrap_command(spec)
    environment = {
        launch.argv[index + 1]: launch.argv[index + 2]
        for index, value in enumerate(launch.argv)
        if value == "--setenv"
    }

    assert environment["CUDA_VISIBLE_DEVICES"] == "0"
    assert ("/dev/nvidia4", "/dev/nvidia4") in _mount_pairs(
        launch.argv, "--dev-bind"
    )
    assert ("/dev/nvidia0", "/dev/nvidia0") not in _mount_pairs(
        launch.argv, "--dev-bind"
    )
    assert launch.argv[-1] == "0"


def test_worker_uses_explicit_compiler_paths_without_etc_alternatives(
    tmp_path: Path,
) -> None:
    launch = build_bubblewrap_command(_spec(tmp_path))
    environment = {
        launch.argv[index + 1]: launch.argv[index + 2]
        for index, value in enumerate(launch.argv)
        if value == "--setenv"
    }

    assert environment["CC"] == "/usr/bin/x86_64-linux-gnu-gcc-12"
    assert environment["CXX"] == "/usr/bin/x86_64-linux-gnu-g++-12"
    assert not any(
        source == "/etc/alternatives"
        for source, _target in _mount_pairs(launch.argv, "--ro-bind")
    )


def test_worker_mounts_a_content_bound_python_header_snapshot(
    tmp_path: Path,
) -> None:
    spec = _spec(tmp_path)
    launch = build_bubblewrap_command(spec)
    environment = {
        launch.argv[index + 1]: launch.argv[index + 2]
        for index, value in enumerate(launch.argv)
        if value == "--setenv"
    }

    assert environment["CPATH"] == (
        "/opt/hb-python-include/python3.10:/opt/hb-python-include"
    )
    assert (
        str(spec.python_include),
        "/opt/hb-python-include",
    ) in _mount_pairs(launch.argv, "--ro-bind")

    (spec.python_include / "Python.h").write_text("/* changed */\n", encoding="utf-8")
    with pytest.raises(SandboxContractError, match="header snapshot"):
        build_bubblewrap_command(spec)


def test_worker_rejects_a_hash_valid_snapshot_without_multiarch_pyconfig(
    tmp_path: Path,
) -> None:
    spec = _spec(tmp_path)
    (spec.python_include / "x86_64-linux-gnu/python3.10/pyconfig.h").unlink()
    spec = BubblewrapSpec(
        **{
            **spec.__dict__,
            "python_include_sha256": hash_immutable_tree(spec.python_include),
        }
    )

    with pytest.raises(SandboxContractError, match="required Python header"):
        build_bubblewrap_command(spec)


def test_immutable_tree_hash_has_a_fixed_domain_separated_vector(
    tmp_path: Path,
) -> None:
    (tmp_path / "Python.h").write_text("/* frozen */\n", encoding="utf-8")

    assert hash_immutable_tree(tmp_path) == (
        "3f2a3ad6c6bf8fa6cc4806f4da6f100331a1160f04521aeba471c8128832e472"
    )


def test_bubblewrap_worker_never_receives_host_repository_or_private_result(
    tmp_path: Path,
) -> None:
    spec = _spec(tmp_path)
    host_repository = tmp_path / "private-host-repository"
    private_result = tmp_path / "private/supervisor-result.json"
    launch = build_bubblewrap_command(spec)
    serialized = "\0".join(launch.argv) + "\0" + "\0".join(
        f"{key}={value}" for key, value in launch.host_environment_items
    )

    assert str(host_repository) not in serialized
    assert str(private_result) not in serialized
    assert "/sandbox/repository/scripts/run_eval_from_files.sh" in launch.argv
    assert launch.candidate_mount in launch.argv
    assert "/sandbox/output" in launch.argv


@pytest.mark.parametrize(
    "unsafe_root",
    [Path("/"), Path("/home"), Path("/tmp"), Path("/data3")],
)
def test_bubblewrap_rejects_broad_or_private_runtime_mounts(
    tmp_path: Path, unsafe_root: Path
) -> None:
    spec = _spec(tmp_path)
    spec = BubblewrapSpec(
        **{
            **spec.__dict__,
            "system_roots": (*spec.system_roots, unsafe_root),
        }
    )
    with pytest.raises(SandboxContractError, match="runtime root"):
        build_bubblewrap_command(spec)


def test_quiescence_always_sends_sigkill_then_observes_missing_group() -> None:
    signals: list[tuple[int, int]] = []
    probes = iter((True, False))

    def killpg(pgid: int, sig: int) -> None:
        signals.append((pgid, sig))

    assert ensure_process_group_quiescent(
        4242,
        killpg=killpg,
        group_exists=lambda _pgid: next(probes),
        sleep=lambda _seconds: None,
        timeout_seconds=1.0,
    )
    assert signals == [(4242, signal.SIGKILL)]


def test_process_result_fails_closed_when_process_group_is_not_quiescent(
    tmp_path: Path,
) -> None:
    launch = build_bubblewrap_command(_spec(tmp_path))
    popen_calls: list[dict[str, object]] = []

    class FakeProcess:
        pid = 9191
        returncode = 0

        def wait(self, timeout: float | None = None) -> int:
            return 0

    def popen(argv, **kwargs):
        popen_calls.append({"argv": tuple(argv), **kwargs})
        return FakeProcess()

    stdout_path = tmp_path / "stdout"
    stderr_path = tmp_path / "stderr"
    outcome = run_bubblewrap_process(
        launch,
        stdout_path=stdout_path,
        stderr_path=stderr_path,
        timeout_seconds=10.0,
        popen=popen,
        quiesce=lambda _pgid: False,
    )

    assert outcome.returncode == 125
    assert outcome.quiescent is False
    assert outcome.timed_out is False
    assert popen_calls[0]["start_new_session"] is True
    assert popen_calls[0]["stdin"] is subprocess.DEVNULL
    assert popen_calls[0]["cwd"] == launch.cwd


def test_process_timeout_is_killed_and_never_reported_as_normal_exit(
    tmp_path: Path,
) -> None:
    launch = build_bubblewrap_command(_spec(tmp_path))
    quiesced: list[int] = []

    class FakeProcess:
        pid = 8181
        returncode = None

        def wait(self, timeout: float | None = None) -> int:
            if timeout is not None:
                raise subprocess.TimeoutExpired(launch.argv, timeout)
            self.returncode = -signal.SIGKILL
            return self.returncode

    outcome = run_bubblewrap_process(
        launch,
        stdout_path=tmp_path / "stdout",
        stderr_path=tmp_path / "stderr",
        timeout_seconds=1.0,
        popen=lambda *_args, **_kwargs: FakeProcess(),
        quiesce=lambda pgid: quiesced.append(pgid) is None,
    )

    assert outcome.returncode == 124
    assert outcome.timed_out is True
    assert outcome.quiescent is True
    assert quiesced == [8181]


def test_runtime_mounts_do_not_leak_parent_environment(tmp_path: Path) -> None:
    launch = build_bubblewrap_command(_spec(tmp_path))
    environment = dict(launch.host_environment_items)
    assert environment == {"LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "PATH": "/usr/bin:/bin"}
    assert "HOME" not in environment
    assert all("TOKEN" not in key and "KEY" not in key for key in environment)


def test_staging_uses_only_frozen_git_tree_and_never_exposes_host_checkout(
    tmp_path: Path,
) -> None:
    repository = tmp_path / "host-repository"
    repository.mkdir()
    subprocess.run(("git", "init", "-q", str(repository)), check=True)
    subprocess.run(
        ("git", "-C", str(repository), "config", "user.name", "HB Test"), check=True
    )
    subprocess.run(
        ("git", "-C", str(repository), "config", "user.email", "hb@example.invalid"),
        check=True,
    )
    tracked = repository / "scripts/run_eval_from_files.sh"
    tracked.parent.mkdir()
    tracked.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
    subprocess.run(("git", "-C", str(repository), "add", "."), check=True)
    subprocess.run(
        ("git", "-C", str(repository), "commit", "-qm", "fixture"), check=True
    )
    commit = subprocess.run(
        ("git", "-C", str(repository), "rev-parse", "HEAD"),
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()
    # An untracked poison file must never enter the worker snapshot.
    (repository / "sitecustomize.py").write_text("raise SystemExit(99)\n", encoding="utf-8")
    candidate = tmp_path / "matmul_w8a8.py"
    candidate.write_text("def matmul_w8a8(x, y): return x @ y\n", encoding="utf-8")

    staged = stage_git_worker_inputs(
        repository=repository,
        commit=commit,
        candidate=candidate,
        staging_root=tmp_path / "trusted-staging",
    )

    assert staged.repository_snapshot != repository
    assert (staged.repository_snapshot / "scripts/run_eval_from_files.sh").is_file()
    assert not (staged.repository_snapshot / ".git").exists()
    assert not (staged.repository_snapshot / "sitecustomize.py").exists()
    assert staged.candidate_snapshot.name == candidate.name
    assert staged.candidate_snapshot.read_bytes() == candidate.read_bytes()
    assert staged.repository_snapshot.stat().st_mode & 0o222 == 0
    assert staged.candidate_snapshot.stat().st_mode & 0o222 == 0


def test_staging_rejects_symlink_from_frozen_tree(tmp_path: Path) -> None:
    repository = tmp_path / "host-repository"
    repository.mkdir()
    subprocess.run(("git", "init", "-q", str(repository)), check=True)
    subprocess.run(
        ("git", "-C", str(repository), "config", "user.name", "HB Test"), check=True
    )
    subprocess.run(
        ("git", "-C", str(repository), "config", "user.email", "hb@example.invalid"),
        check=True,
    )
    (repository / "escape").symlink_to("/etc/passwd")
    subprocess.run(("git", "-C", str(repository), "add", "."), check=True)
    subprocess.run(
        ("git", "-C", str(repository), "commit", "-qm", "fixture"), check=True
    )
    commit = subprocess.run(
        ("git", "-C", str(repository), "rev-parse", "HEAD"),
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()
    candidate = tmp_path / "candidate.py"
    candidate.write_text("def kernel_function(x): return x\n", encoding="utf-8")

    with pytest.raises(SandboxContractError, match="symlink"):
        stage_git_worker_inputs(
            repository=repository,
            commit=commit,
            candidate=candidate,
            staging_root=tmp_path / "trusted-staging",
        )
