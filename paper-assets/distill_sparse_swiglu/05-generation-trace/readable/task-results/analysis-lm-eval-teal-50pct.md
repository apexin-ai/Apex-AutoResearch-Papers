# analysis lm eval teal 50pct

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lm_eval_teal_50pct_20260516T023351_result.json`
- **Structured JSON:** [`e1e52b7fa70ca453570e.json`](../../sessions/e1/e1e52b7fa70ca453570e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。实验 `lm_eval_teal_50pct` → **DONE (success)**。

**结论**：TEAL 50% 也全面崩溃（MMLU=0.286, GSM8K=0.019），与 KL 50% 的崩溃程度相当。50% unstructured sparsity 对 SwiGLU FFN 的 downstream capability 破坏是方法无关的（universal），不是 KL predictor 特有问题。TEAL 在简单 task（ARC/WinoGrande）上甚至比 KL 更差，说明 learned predictor 至少在保留部分能力上优于 training-free 方法。

---
