# ops mistral dense version check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mistral-dense-version-check_20260519T061822_result.json`
- **Structured JSON:** [`daa2a980df0cd3094138.json`](../../sessions/da/daa2a980df0cd3094138.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job is running. HellaSwag eval is ~52% through (5232/10042 samples at ~234 it/s).

**Summary:**

1. **Model version: Mistral-7B-v0.3**
   - `architectures`: `MistralForCausalLM`
   - `vocab_size`: 32768 (v0.3 extended from v0.1's 32000)
   - `rope_theta`: 1000000.0 (v0.1 = 10000.0)
   - `sliding_window`: null (v0.1 = 4096)
   - `num_key_value_heads`: 8 (GQA)

2. **Experiment submitted:**
   - `exp_id`: `mistral_dense_hellaswag_piqa`
   - PID: 84284
   - Server: westd-34887, cuda:0
   - Registry status: RUNNING
   - Log: `/root/distill_sparse_swiglu/logs/mistral_dense_hellaswag_piqa.log`

---
