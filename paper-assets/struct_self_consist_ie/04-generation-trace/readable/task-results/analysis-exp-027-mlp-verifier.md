# analysis exp 027 mlp verifier

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_027_mlp_verifier_20260516T133606_result.json`
- **Structured JSON:** [`f5a687812583321638ac.json`](../../sessions/f5/f5a687812583321638ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结论：

**特征是瓶颈，不是模型容量。**

| Model | Features | AUROC | Selection F1 |
|-------|----------|-------|-------------|
| Best single (EM) | 1 | 0.6476 | 0.6470 (LP) |
| LR | 5 | **0.6522** | **0.6406** |
| MLP | 5 | 0.6393 | 0.6377 |
| RF | 5 | 0.5868 | 0.6133 |
| MLP | 15 | 0.6322 | 0.6339 |
| RF | 15 | 0.6043 | 0.6143 |

- MLP ≈ LR（Δ=-0.013），RF 更差（过拟合）
- 15-feat interactions 无增益
- LR 仅比最佳单信号高 +0.005 AUROC
- 所有 supervised verifier 的 selection F1 都没超过 unsupervised LP baseline（0.647）

输出已保存到 `/root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_verifier/`（results.json, report.md, train_mlp_verifier.py）并注册为 artifact。

---
