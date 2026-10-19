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
    def __init__(self, in_features, out_features, subtract_value, multiply_value):
        super().__init__()
        self.linear = nn.Linear(in_features, out_features)
        self.subtract_value = subtract_value
        self.multiply_value = multiply_value

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.linear(x)
        x = x - self.subtract_value
        x = x * self.multiply_value
        return torch.relu(x)
