from __future__ import annotations

from optimization_lab.adapters.ssh_kernelbench import SSHKernelBenchAdapter


def test_cache_environment_exposes_kernelbench_src_package() -> None:
    adapter = SSHKernelBenchAdapter(
        host="moss-h200",
        remote_repository="/data/moss-p0/KernelBench",
        remote_root="/data/moss-kbdual",
        gpu_index=0,
        remote_uv="/data/moss-p0/uv-shim",
    )

    assert "PYTHONPATH=/data/moss-p0/KernelBench/src" in adapter._cache_env()
