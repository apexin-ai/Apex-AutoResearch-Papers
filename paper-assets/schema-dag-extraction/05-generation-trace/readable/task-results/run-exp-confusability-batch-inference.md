# run exp confusability batch inference

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp_confusability_batch_inference_20260516T063940_result.json`
- **Structured JSON:** [`29e67a8c52803d331082.json`](../../sessions/29/29e67a8c52803d331082.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Inference is running. Condition 1/17 (`confusability_aware`), batch 1/8 (`confusability_aware_batch_0`), 120 samples being processed. GPU at 100% utilization, 89.4 GB memory used.

Summary:
- **Residual process**: cleaned
- **flashinfer version mismatch**: bypassed with `FLASHINFER_DISABLE_VERSION_CHECK=1`
- **Model**: Qwen3-32B-FP8 loaded (32 GiB), KV cache allocated (~57 GiB)
- **Status**: Inference running — condition 1/17 (confusability_aware), batch 1/8
- **PID**: 375859 on cqa1-38874
- **Log**: `/tmp/exp018_extract.log`
- **Registry**: updated to RUNNING

17 conditions total (1 confusability_aware + 15 random seeds + 1 single_pass), 960 samples. Each condition processes 8 batches of 120 samples each (except single_pass: 1 batch of 960).

---
