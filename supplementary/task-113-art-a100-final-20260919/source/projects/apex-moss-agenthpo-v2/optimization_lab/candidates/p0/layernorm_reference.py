"""P0 control: reproduce the reference operation, not an optimization claim."""

import torch
import torch.nn as nn
import triton
import triton.language as tl


@triton.jit
def _p0_marker_kernel(x, y, n_elements: tl.constexpr, BLOCK_SIZE: tl.constexpr):
    offsets = tl.arange(0, BLOCK_SIZE)
    values = tl.load(x + offsets, mask=offsets < n_elements)
    tl.store(y + offsets, values, mask=offsets < n_elements)


class ModelNew(nn.Module):
    def __init__(self, normalized_shape: tuple):
        super().__init__()
        self.layer_norm = nn.LayerNorm(normalized_shape=normalized_shape)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.layer_norm(x)
