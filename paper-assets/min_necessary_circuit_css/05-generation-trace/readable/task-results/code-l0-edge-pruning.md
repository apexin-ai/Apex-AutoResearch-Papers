# code l0 edge pruning

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_l0-edge-pruning_20260512T120903_result.json`
- **Structured JSON:** [`abc8f565d8354e339db7.json`](../../sessions/ab/abc8f565d8354e339db7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both files are correct. Summary of what was done:

**Created `edge_pruning_l0.py`** with:
- `HardConcreteMask` — Hard Concrete distribution (Louizos 2018) for differentiable L0 regularization
- `_build_edge_index` — enumerates edges at (src → attn_layer) and (src → mlp_layer) granularity
- `_masked_forward` — cascading forward pass: reconstructs each component's input as a masked sum of upstream outputs, applies LN/attention/MLP, and propagates masked outputs to later layers
- `run_edge_pruning_l0` — main entry point: optimizes masks over `n_epochs`, outputs per-Q/K/V/head edge scores in TransformerLens format (compatible with CSS pipeline)

**Updated `circuit_discovery.py`**:
- `run_edge_pruning` now calls `run_edge_pruning_l0` instead of the subprocess placeholder
- `_normalize_edge_pruning_edge` simplified to `strip()` since L0 outputs TL-format names directly

Key design decisions:
- **Cascading** (not clean-activation): later layers see masked outputs from earlier layers, giving more accurate circuit identification
- **Per-layer attention masks** internally (all heads share masked residual at each layer), expanded to per-Q/K/V/head in output for CSS compatibility — avoids O(n_heads) LN applications per layer
- Attention biases (`b_O`) accumulated and included as unmasked constants at each destination

---
