# check r7n2 data size ablation status

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_r7n2-data-size-ablation-status_20260516T013627_result.json`
- **Structured JSON:** [`10777edcd4b13d7a6001.json`](../../sessions/10/10777edcd4b13d7a6001.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## r7n2-data-size-ablation 状态

**进程**: PID 921548 已死亡。**替代进程 PID 920406 存活**，已运行 ~29 分钟。
- 命令: `python src/ablation_data_size.py --seeds 42 43 44 --batch_size 4 --output_dir results/ablation_data_size`
- GPU: RTX 5090，13103 MiB / 32607 MiB，28% 利用率

### 进度

代码定义 5 个 scale × 3 seeds = **15 个 run**：

| Scale | seed 42 | seed 43 | seed 44 |
|-------|---------|---------|---------|
| 25pct | done | done | **training** |
| 50pct | - | - | - |
| 100pct | - | - | - |
| 2x | - | - | - |
| 4x | - | - | - |

当前完成 **2/15**，正在第 3 个。

### 已完成结果（有问题）

两个完成的 run 结果一致：

| | seed 42 | seed 43 |
|---|---------|---------|
| **balanced_acc** | **0.500** | **0.500** |
| deterministic_recall | 0.0 | 0.0 |
| internal_recall | 1.0 | 1.0 |
| n_train | 433 | 433 |
| pred_distribution | all internal (305/305) | all internal (305/305) |
| true_distribution | 275 det / 30 int | 275 det / 30 int |

模型将所有样本预测为 `internal`，导致 deterministic_recall = 0，balanced_acc 恰好 0.5。这是典型的模型 collapse——没有学到区分信号。

### 预计剩余时间

每个 run ~10 分钟（25pct scale），更大 scale 会更慢（2x/4x 数据量翻倍）。粗略估计还需 **2-3 小时**完成全部 15 个 run。

### 结果路径

- `results/ablation_data_size/` — 主输出目录
- 最终汇总会写入 `results/ablation_data_size/summary.json`

---
