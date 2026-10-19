# exp empirical annotations

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_empirical____annotations_20260524T054948_result.json`
- **Structured JSON:** [`3f8460f2c4870593e7df.json`](../../sessions/3f/3f8460f2c4870593e7df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All gaps filled. Here's the final summary:

**Completed**: 36/36 `.jsonl` files + 36/36 `.npz` confusion matrices across all 3 datasets × 4 models × 3 prompts.

**What was done this session:**

| Task | Status |
|------|--------|
| qwen2.5-7b × humaid × zero-shot | 1500 samples, 56.4% acc, 99.8% coverage |
| qwen2.5-7b × humaid × few-shot-3 | 1500 samples, 64.0% acc, 99.6% coverage |
| qwen2.5-7b × humaid × few-shot-5 | 1500 samples, 64.5% acc, 99.8% coverage |
| VAST qwen2.5-7b zero-shot `.npz` | Regenerated (48.0% acc, 99.9% coverage) |

**Previously reported issues resolved:**
- qwen3 HumAID 402 errors — false alarm, data was clean (402 was a sample index, not HTTP error)
- All datasets (HumAID K=10, VAST K=3, CivilComments K=2) now have complete annotations for all 4 models (deepseek, llama4, qwen3, qwen2.5-7b) × 3 prompt strategies.

---
