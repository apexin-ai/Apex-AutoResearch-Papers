# analysis perlayer kl k2 s123 result

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perlayer_kl_k2_s123_result_20260523T082515_result.json`
- **Structured JSON:** [`9187188d61dde7a83651.json`](../../sessions/91/9187188d61dde7a83651.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

**K=2 s123** — 训练成功
- 1000/1000 steps 完成，最终 avg_kl = **0.0373**，avg_sparsity = **0.307**
- Final checkpoint: `predictor_perlayer_kl_k4.pt` (145 MB)
- 训练耗时 ~1839s (~30.6 min)

**K=2 s456** — 训练成功
- 1000/1000 steps 完成，最终 avg_kl 与 s123 接近（Layer 31 avg_kl=0.0763）
- Final checkpoint: `predictor_perlayer_kl_k4.pt` (145 MB)

两个 registry 均已更新为 DONE/success。

---
