# analysis gradient cka summary

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient_cka_summary_20260524T194411_result.json`
- **Structured JSON:** [`1f67c76e2550c218d145.json`](../../sessions/1f/1f67c76e2550c218d145.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。结构化摘要写入 `artifacts/gradient_cka_summary.md` 并注册（`art_20260524_2230d8`）。

摘要包含三个部分：
- **A. 梯度分析**：global norms（Detach=4% of Vanilla, Full OCC/Random≈1×）、per-layer conflict（DINOv2 全层正交 ~50%, SigLIP late layers 降至 ~25%）、Detach 低方差签名
- **B. CKA 分析**：5 条件对比表、Detach+LN Paradox（CKA 完全恢复但 CAR 仍低 1.5pp → BN 是表征漂移 100% 原因，梯度流有非表征通道的行为贡献）
- **C. 综合**：H1（gradient diversity → representation → safety）部分否定；H2（implicit regularization → prevent collapse）成立；H3（BN stats → drift）成立；双机制模型 56%/44% 分解

---
