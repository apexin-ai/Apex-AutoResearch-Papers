from pathlib import Path


def test_p0_container_image_is_pinned_and_contains_build_requirements() -> None:
    root = Path(__file__).parents[1]
    dockerfile = (
        root / "optimization_lab/docker/Dockerfile.p0"
    ).read_text(encoding="utf-8")

    assert "ubuntu@sha256:" in dockerfile
    assert "python3.10" in dockerfile
    assert "python3.10-dev" in dockerfile
    assert "build-essential" in dockerfile
    assert "nvidia-container-toolkit" not in dockerfile
    assert "apt-get clean" in dockerfile


def test_p0_container_smoke_requires_one_gpu_and_torch_compile() -> None:
    root = Path(__file__).parents[1]
    smoke = (root / "optimization_lab/docker/p0_smoke.py").read_text(
        encoding="utf-8"
    )

    assert "torch.cuda.device_count() != 1" in smoke
    assert "@torch.compile" in smoke
    assert '"compile_smoke": True' in smoke
