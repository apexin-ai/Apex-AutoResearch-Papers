# ops full status check director

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_status_check_director_20260516T110445_result.json`
- **Structured JSON:** [`f4b10d730d112251d931.json`](../../sessions/f4/f4b10d730d112251d931.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全面状态汇总

### GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | 80.4/95.6 GB | 99% |
| cuda:1 | 69.9/95.6 GB | 100% |

### 各实验状态

| 实验 | PID | 状态 | GPU | 进度 |
|------|-----|------|-----|------|
| **Qwen 主链** | 337267 (wrapper) → 134514 (train) | ALIVE | cuda:0, 50.8GB | dataflow_aware_s44, step 1000/2816, epoch 1 |
| **Qwen Watcher** | 966920 | ALIVE (sleeping) | — | 等待主链完成，supplement 未触发 |
| **StarCoder** | 519791 (wrapper) → 129747 (train) | ALIVE | cuda:1, 53.9GB | embedding_distance_s43, step 1000/2810, epoch 1 |
| **UniXcoder s43 chain** | 167371 (wrapper) → 173092 (train) | ALIVE | cuda:0, 13.5GB | random_s43 已完成 (R@1=0.577), 正在跑 embedding_distance_s43 (刚启动) |
| **D062 eval** | 158647 | ALIVE (3h13m) | cuda:1, 16GB×2 procs | 6/14 完成，正在评估 random_s44_best_by_recall_at_1 |

### Qwen 主链进度
已完成 subruns: random_s42, random_s43, random_s44, embedding_distance_s43, embedding_distance_s44, dataflow_aware_s43 (6/9 完成)
当前: **dataflow_aware_s44** — step 1000/~2816, loss=0.2142, eval@500 R@1=0.5701

### StarCoder 进度
已完成: random_s42, random_s43, random_s44, embedding_distance_s42 (4/9 完成)
当前: **embedding_distance_s43** — step 1000/~2810, loss=0.3949, eval@1000 R@1=0.4885

### UniXcoder s43 chain 进度
刚完成 **random_s43**: R@1=0.577, R@5=0.977, val_loss=0.429
正在跑 **embedding_distance_s43** (刚启动，epoch 1)
s44 系列尚未开始

### D062 Eval 结果 (5/14 已出)

| Checkpoint | R@1 | R@5 | R@10 |
|-----------|-----|-----|------|
| random_s42_best_by_val_loss | 0.2302 | 0.6250 | 0.8016 |
| random_s42_best_by_recall_at_1 | 0.2302 | 0.6250 | 0.8016 |
| random_s43_best_by_val_loss | 0.3413 | 0.7500 | 0.8849 |
| **random_s43_best_by_recall_at_1** | **0.5040** | **0.8790** | **0.9623** |
| random_s44_best_by_val_loss | 0.3532 | 0.7500 | 0.8929 |

s42 两个 checkpoint 结果相同（R@1=0.230）。s43 的 best_by_recall_at_1 明显优于 best_by_val_loss（0.504 vs 0.341）。D062 正在加载 random_s44_best_by_recall_at_1，还有 8 个待评估（含全部 embedding_distance 和 dataflow_aware）。

---
