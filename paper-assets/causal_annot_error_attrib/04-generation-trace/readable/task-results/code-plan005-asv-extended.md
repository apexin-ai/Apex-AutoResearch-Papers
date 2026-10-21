# code plan005 asv extended

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan005-asv-extended_20260520T135157_result.json`
- **Structured JSON:** [`7062cf8f6ca5c37641c0.json`](../../sessions/70/7062cf8f6ca5c37641c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`plan005_asv_extended` 已注册完成，状态 DONE (success)。

关键结果：
- **M-bias**: ASV = None（误分类 collider A 不影响 T→Y 估计，反而减少了虚假 M-bias）
- **IV**: ASV_magnitude = 0（Wald 估计量对误分类立即敏感，C 直接缩放 first-stage）
- **Front-door**: ASV_magnitude = 0.064–0.387（中等敏感度，依赖 C₀ 结构）
- Envelope 单调性 0 violations，MC coverage 100%，Type I 接近 nominal

---
