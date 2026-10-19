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
    def __init__(self, normalized_shape: tuple):
        super().__init__()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        output = torch.empty_like(x)
        n_elements = output.numel()
        _zero_kernel[(triton.cdiv(n_elements, 256),)](output, n_elements, BLOCK_SIZE=256)
        return output
