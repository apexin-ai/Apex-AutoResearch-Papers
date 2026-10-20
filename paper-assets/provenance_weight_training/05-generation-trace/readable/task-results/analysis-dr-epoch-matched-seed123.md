# analysis dr epoch matched seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dr_epoch_matched_seed123_20260521T233436_result.json`
- **Structured JSON:** [`19a80e754f1432e159d1.json`](../../sessions/19/19a80e754f1432e159d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**两个实验训练均已完成**，但 eval 不完整：

| 实验 | 训练状态 | train_loss | holdout_ppl | holdout_loss | owt_ppl | wiki_ppl |
|------|---------|-----------|-------------|-------------|---------|---------|
| dr_epoch_matched_seed123 | 2533/2533 完成 | 2.831 | 未评估 | 未评估 | 未评估 | 未评估 |
| detect_remove_q05_v2_seed123 | 24414/24414 完成 | 2.760 | **17.366** | **2.854** | 未评估 | 未评估 |

**Epoch confound gap 无法计算** — dr_epoch_matched_seed123 的 eval 完全缺失。

detect_remove_q05_v2_seed123 的 holdout_ppl=17.366 与 seed42 的 17.285 差 +0.081，seed 间变异合理。

**需要补跑的 eval**：
1. dr_epoch_matched_seed123：holdout + OOD (owt, wiki)
2. detect_remove_q05_v2_seed123：OOD (owt, wiki)

是否现在启动这些 eval？

---
