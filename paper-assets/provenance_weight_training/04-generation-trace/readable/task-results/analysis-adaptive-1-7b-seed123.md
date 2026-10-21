# analysis adaptive 1 7b seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_adaptive_1_7b_seed123_20260519T010709_result.json`
- **Structured JSON:** [`d353e69803d10d2b7d41.json`](../../sessions/d3/d353e69803d10d2b7d41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册 (`art_20260519_7885ea`)。

## 汇总

| 项目 | 结果 |
|------|------|
| 训练状态 | **成功** (EXIT_CODE=0, 6103/6103 steps) |
| 训练时间 | 5h 09m |
| train_loss | **9.144** (seed42 参考值: 5.36) |
| total_steps | 6103 (与 seed42 一致) |
| checkpoint | `/root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed123/final/` (3.4GB) |
| eval metrics | 无, **需要独立 eval** |

**需要关注**: train_loss 9.144 vs seed42 的 5.36, 差距很大。trainer 报告的 loss 是 weighted loss, 但 step_metrics 中 per-example weighted_loss 仅 1~3 范围。两种可能:
1. seed42 和 seed123 的 train_loss 口径不同 (unweighted vs weighted)
2. 如果口径相同, seed123 确实异常

建议先确认 seed42 日志中的 loss 口径, 然后跑 holdout eval 拿 PPL 做直接对比。

---
