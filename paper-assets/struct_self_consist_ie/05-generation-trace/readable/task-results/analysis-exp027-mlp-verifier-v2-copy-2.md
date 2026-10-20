# analysis exp027 mlp verifier v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp027_mlp_verifier_v2_20260518T160242_result.json`
- **Structured JSON:** [`e52735807f6004c5e3c9.json`](../../sessions/e5/e52735807f6004c5e3c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Feature bottleneck 确认。** 已有 exp_027 结果直接复用，无需重跑（脚本+数据+结果完整）。

核心结论：

| 对比 | 值 |
|------|-----|
| Best supervised AUROC | LR 5feat = 0.6522 |
| Best single signal AUROC | EM = 0.6476 |
| Best supervised Sel F1 | LR 5feat = 0.6407 |
| Best unsup Sel F1 | LP = 0.6470 |
| Greedy F1 | 0.6441 |
| Oracle F1 | 0.8231 |

- MLP (0.6393) < LR (0.6522)，nonlinear model 在 5 个弱信号上过拟合
- 15-feat interactions 无帮助：MLP 15feat (0.6322) < MLP 5feat (0.6393)
- 所有 supervised models 的 selection F1 都低于 best unsupervised (LP=0.6470)
- Oracle gap 巨大 (0.8231 vs 0.6470)：好 sample 存在但 5 个 QE signals 无法识别

报告已写入 `artifacts/exp027_mlp_v2/mlp_verifier_results.md` 并注册。

---
