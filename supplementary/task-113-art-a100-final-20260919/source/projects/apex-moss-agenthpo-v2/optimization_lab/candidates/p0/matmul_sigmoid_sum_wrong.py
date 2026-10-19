"""P0 negative control: compiles and runs but deliberately returns zeros."""

import torch
import torch.nn as nn
import triton
import triton.language as tl


@triton.jit
def _zero_kernel(output, n_elements, BLOCK_SIZE: tl.constexpr):
    offsets = tl.program_id(0) * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE)
    tl.store(output + offsets, 0.0, mask=offsets < n_elements)


class ModelNew(nn.Module):
    def __init__(self, input_size, hidden_size):
        super().__init__()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        output = torch.empty((x.shape[0], 1), device=x.device, dtype=x.dtype)
        _zero_kernel[(1,)](output, output.numel(), BLOCK_SIZE=128)
        return output
