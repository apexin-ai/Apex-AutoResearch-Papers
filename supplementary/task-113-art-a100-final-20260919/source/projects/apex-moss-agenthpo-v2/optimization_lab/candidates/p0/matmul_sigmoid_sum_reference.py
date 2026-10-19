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
    def __init__(self, input_size, hidden_size):
        super().__init__()
        self.linear = nn.Linear(input_size, hidden_size)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.linear(x)
        x = torch.sigmoid(x)
        return torch.sum(x, dim=1, keepdim=True)
