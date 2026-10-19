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
    def __init__(self, in_features, out_features, subtract_value, multiply_value):
        super().__init__()
        self.out_features = out_features

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        output = torch.empty(
            (x.shape[0], self.out_features), device=x.device, dtype=x.dtype
        )
        n_elements = output.numel()
        _zero_kernel[(triton.cdiv(n_elements, 256),)](output, n_elements, BLOCK_SIZE=256)
        return output
