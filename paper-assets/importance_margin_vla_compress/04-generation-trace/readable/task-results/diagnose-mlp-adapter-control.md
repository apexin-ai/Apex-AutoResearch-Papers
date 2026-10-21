# diagnose mlp adapter control

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mlp_adapter_control_20260519T115543_result.json`
- **Structured JSON:** [`37dbfeba80abb3b7de8d.json`](../../sessions/37/37dbfeba80abb3b7de8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Summary:

1. **Training complete**: `train_mlp_adapter_control` finished 100K steps (checkpoint step=99999). Registry updated to DONE/success.

2. **Eval launched**: `eval_mlp_adapter_control` running in tmux session `eval_mlp_adapter_control` on westd cuda:0.
   - Suite: libero_object, 10 tasks x 50 episodes
   - Model loaded with strict match, MLPCompressor 22.14M params, M=32
   - Already processing (task 0, ep 1 SUCCESS at step 141)

3. **Fix applied**: Patched `eval_smart_compress_libero.py` line 84 to inherit `compressor.type` from checkpoint config (was hardcoded to cross-attention only).

4. **Registry**: `eval_mlp_adapter_control` registered as RUNNING, parent=`train_mlp_adapter_control`.

---
