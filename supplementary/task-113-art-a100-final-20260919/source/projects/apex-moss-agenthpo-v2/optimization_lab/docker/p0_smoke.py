"""Minimal GPU and torch.compile check for the isolated P0 container."""

from __future__ import annotations

import json

import torch
import triton


def main() -> None:
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is not available inside the P0 container")
    if torch.cuda.device_count() != 1:
        raise RuntimeError(
            f"expected exactly one visible GPU, found {torch.cuda.device_count()}"
        )

    @torch.compile
    def add_one(value: torch.Tensor) -> torch.Tensor:
        return value + 1

    value = torch.ones(64, device="cuda")
    result = add_one(value)
    torch.cuda.synchronize()
    if result.sum().item() != 128.0:
        raise RuntimeError("torch.compile smoke calculation returned the wrong result")

    print(
        json.dumps(
            {
                "compile_smoke": True,
                "device_count": torch.cuda.device_count(),
                "gpu": torch.cuda.get_device_name(0),
                "torch": torch.__version__,
                "triton": triton.__version__,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
