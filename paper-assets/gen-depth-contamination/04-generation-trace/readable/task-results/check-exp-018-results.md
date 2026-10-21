# check exp 018 results

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_018_results_20260516T154954_result.json`
- **Structured JSON:** [`e2520efaa72e0c16a43b.json`](../../sessions/e2/e2520efaa72e0c16a43b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp-018 LLaMA-8B 实验已成功完成，cron 误判为 failed。** 所有结果文件于 2026-05-16 23:27 写入完毕，pipeline 正常退出 (return_code=0)。

---

## 完整结果

### K* = 2（确认）

定义：max depth where AUC > 0.60。

### Pairwise AUC（5-fold CV，mean ± std）

| Pair | AUC | std | Per-fold |
|------|-----|-----|----------|
| **0 vs 1** | **0.9225** | 0.0036 | [0.9196, 0.9194, 0.9280, 0.9200, 0.9257] |
| **1 vs 2** | **0.6123** | 0.0130 | [0.6362, 0.6072, 0.5975, 0.6067, 0.6140] |
| 2 vs 3 | 0.5274 | 0.0131 | [0.5345, 0.5442, 0.5342, 0.5141, 0.5101] |
| 3 vs 4 | 0.5169 | 0.0108 | [0.5185, 0.5292, 0.4968, 0.5175, 0.5222] |
| 4 vs 5 | 0.5162 | 0.0096 | [0.5089, 0.5225, 0.5321, 0.5103, 0.5072] |

AUC 在 depth 2 之后快速饱和至 ~0.52（接近随机），1v2 是最后一个显著高于 chance 的 pair。

### Pairwise JSD

| Pair | JSD |
|------|-----|
| 0 vs 1 | 0.076925 |
| 1 vs 2 | 0.012301 |
| 2 vs 3 | 0.004631 |
| 3 vs 4 | 0.004292 |
| 4 vs 5 | 0.003572 |

JSD 同样在 depth 1→2 后急剧衰减（6× drop from 0v1 to 1v2, 再 2.7× drop from 1v2 to 2v3）。

### Ordinal Classification（6-class, 5-fold CV）

- MAE = 1.3146
- Accuracy = 0.3269

### Top-10 Feature Importance

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | surp_d1_skew | 8758.6 |
| 2 | freq_entropy | 8621.8 |
| 3 | surp_d2_mean | 8361.2 |
| 4 | surp_std | 8254.2 |
| 5 | surp_d1_mean | 8162.0 |
| 6 | surp_mean | 8063.4 |
| 7 | freq_kurtosis | 7788.4 |
| 8 | surp_kurt | 7401.2 |
| 9 | surp_skew | 7080.8 |
| 10 | surp_d1_std | 6133.2 |

### 进程状态

进程已正常退出，不在运行。

---

**结论**：实验完整成功，ROADMAP 中 K\*=2 的记录正确。Cron auto-resolve 为 failed 是误判（可能进程在 cron 检测窗口之间已结束，sentinel/W&B 未配置导致 cron 无法确认成功）。日志中无 bootstrap CI——结果文件里只有 per-fold std，没有单独的 bootstrap 置信区间输出。

---
