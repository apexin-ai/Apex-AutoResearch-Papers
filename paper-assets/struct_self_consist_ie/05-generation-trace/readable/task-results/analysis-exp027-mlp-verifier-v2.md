# analysis exp027 mlp verifier v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp027_mlp_verifier_v2_20260518T162244_result.json`
- **Structured JSON:** [`44a29e017e0d91f0da02.json`](../../sessions/44/44a29e017e0d91f0da02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Feature bottleneck 结论完全稳定：**

| 模型 | AUROC (3-seed) | Selection F1 |
|------|---------------|-------------|
| LR_5 | **0.6681** | **0.6406** |
| MLP_5 | 0.6579 | 0.6367 |
| RF_5 | 0.6101 | 0.6140 |
| MLP_20 | 0.6633 | 0.6329 |
| Greedy | -- | 0.6441 |
| Best unsup (FK) | -- | 0.6469 |

关键发现：
- **LR > MLP > RF**（AUROC 排序不变）
- **所有 supervised models < greedy selection F1**（0.6406 < 0.6441）
- **20-feat interactions 无帮助**
- `early_stopping=True` 缩小了 MLP 与 LR 的差距（-0.0102 vs 原版 -0.0129），但不改变结论

报告已注册：`artifacts/exp_027_mlp_v2/report/mlp_verifier_results.md`

---
