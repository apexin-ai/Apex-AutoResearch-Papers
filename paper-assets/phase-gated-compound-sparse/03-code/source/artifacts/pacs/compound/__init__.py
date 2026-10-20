# Compound sparsity: simultaneous attention head masking + KV cache eviction.

from .head_selector import HeadSelector, HeadMask, group_heads_by_kv
from .kv_evictor import KVEvictor, KVMask
from .compound_forward import CompoundSparseForward, compute_compound_ppl

__all__ = [
    "HeadSelector",
    "HeadMask",
    "group_heads_by_kv",
    "KVEvictor",
    "KVMask",
    "CompoundSparseForward",
    "compute_compound_ppl",
]
