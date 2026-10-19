# check qwen s44 eval1500 v2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen-s44-eval1500-v2_20260515T000859_result.json`
- **Structured JSON:** [`13aed41912ebcc967c99.json`](../../sessions/13/13aed41912ebcc967c99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**random_s44 已完成** — eval@1500 刚刚结束（~08:10），early stopping 触发。

### eval@1500 结果

| Step | val_loss | R@1 | R@5 | R@10 |
|------|----------|-----|-----|------|
| 500 **(best)** | **0.4252** | **0.6009** | 0.9583 | 1.0 |
| 1000 | 0.4695 | 0.5638 | 0.9524 | 1.0 |
| 1500 | 0.4918 | 0.5592 | 0.9504 | 1.0 |

- **Early stopping 触发**：patience=2，val_loss 连续 2 次未改善（step 1000、1500 均劣于 step 500）
- Best checkpoint 保存在 step 500（val_loss=0.4252, R@1=0.6009）

### 下一个 run 状态

- **embedding_distance_s43 尚未启动**：PID 504138 仍是 random_s44 进程（在做 wandb 清理），GPU 0 占用 51532 MiB / 100%
- 脚本会自动继续，embedding_distance_s43 应在几秒到几分钟内启动

### 并行训练

- **StarCoder (GPU 1)**：random_s43 @ step 1100，正常训练中（PID 519805, 53918 MiB, 100%）

---
