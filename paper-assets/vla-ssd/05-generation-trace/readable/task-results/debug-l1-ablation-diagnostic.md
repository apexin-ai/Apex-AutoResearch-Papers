# debug l1 ablation diagnostic

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_l1_ablation_diagnostic_20260517T142940_result.json`
- **Structured JSON:** [`40a45739e360e9bbac69.json`](../../sessions/40/40a45739e360e9bbac69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Diagnostic results are clear. Let me summarize the key findings:

## Diagnostic Results

### 1. INST_START = 257: Correct
`input_ids` has 22 text tokens, but the model prepends 256 image tokens internally, making the actual attention seq_len ~278. INST_START=257 is the first text token position in the attention layer. The diagnostic's "Correct: No" is a false alarm (it checked `input_ids.shape` instead of attention seq_len).

### 2. Monkey-patch mechanism: WORKING
Despite section 5 reporting "BUG CONFIRMED", this is a **false alarm**. The `@deprecate_kwarg` decorator in transformers 4.57.6 wraps `forward`, so `type(attn_mod).forward.__globals__` points to the wrapper's module (`transformers.utils.deprecation`). But the original `forward` code still executes with `modeling_llama`'s globals, so patching `llama_mod.eager_attention_forward` DOES reach the original function.

Proof from section 3:
- Ablated heads inst attention: **0.000000** (was 0.029116 baseline)
- Control heads preserved: 0.020751 (unchanged)
- L1 hidden state cosine sim: **0.972655** (significant change)
- L2 distance: **1.507398**

### 3. Root cause of 1.0 accuracy: Not a bug
The ablation IS working, but:
- Baseline readout→inst attention is already small (0.027)
- 8 control heads still carry instruction signal (0.021 each)
- Residual connection from layer 0 preserves instruction info
- 10-way classification is easy enough that degraded-but-not-destroyed signal suffices

**The 1.0 accuracy is a genuine result, not a bug.** The L1 instruction-attending heads are not the sole bottleneck for instruction discrimination.

---
