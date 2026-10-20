# code fix gar rope

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_gar_rope_20260518T050818_result.json`
- **Structured JSON:** [`83a5c79383b314ccf9a6.json`](../../sessions/83/83a5c79383b314ccf9a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks passed with the real Qwen2.5-0.5B model on CPU. Summary of changes:

**gar.py** (rewritten):
- Replaced `register_forward_pre_hook` with `register_forward_hook` that captures the model's native attention weights (`output[1]`) which already include RoPE
- Removed manual Q/K projection, causal masking, and softmax computation from both `compute_gar` and `compute_gar_differentiable`
- Added warning when `attn_implementation != "eager"` (SDPA/Flash don't return weights)
- All public API signatures and return formats preserved

**turn_utils.py** (line 105-106): Removed dead `if ids_list[i] == im_end_id: pass` block.

**verify_gar_fix.py** (new): Verification script with mock fallback; confirmed with real Qwen2.5-0.5B that attention rows sum to 1.0, shapes are correct, and GAR values are in [0, 1].

---
