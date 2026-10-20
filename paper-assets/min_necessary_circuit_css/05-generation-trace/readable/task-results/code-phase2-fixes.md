# code phase2 fixes

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase2-fixes_20260512T232116_result.json`
- **Structured JSON:** [`2bcdfb7d13febfc99694.json`](../../sessions/2b/2bcdfb7d13febfc99694.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both fixes validated. Summary:

### (a) circus.py — 2D anti-chain config_bag
- **Changed**: `config_bag()` now derives two independent scoring dimensions: node importance (max |edge_score| per source) and raw edge importance (|score|). Generates B configurations along an anti-diagonal — as node_threshold rises, edge_threshold falls.
- **Why**: Old 1D percentile sweep produced strictly nested circuits (45/90 pairs nested). New 2D approach reduces nesting to 8/90 (91% reduction), ensuring the CIRCUS ensemble captures genuinely diverse circuits.
- **Interface**: Same signature and return type — `run_circus` and downstream code unaffected.

### (b) edge_pruning_l0.py — per-edge mask granularity
- **Changed**: `_build_edge_index()` now enumerates attention edges as `(src, dst_layer, head, qkv_idx)` with independent masks. `attn_lookup` key changed from `dst_layer` to `(dst_layer, head, qkv_idx)`. `_masked_forward()` computes per-(head, qkv) residual inputs, each going through its own LayerNorm → projection path.
- **Why**: Old (src, dst_layer) granularity forced all H×QKV edges to share one mask, losing the per-edge resolution that EAP-IG provides. New approach gives each of the 31,320 attention edges (GPT-2 small) its own learnable mask.
- **Interface**: Output `Dict[str, float]` format unchanged — same edge name strings, but values are now independently optimized.

---
