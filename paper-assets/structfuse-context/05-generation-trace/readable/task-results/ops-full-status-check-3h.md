# ops full status check 3h

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_status_check_3h_20260516T155508_result.json`
- **Structured JSON:** [`aa2174ec0f708068a597.json`](../../sessions/aa/aa2174ec0f708068a597.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全状态报告 — 2026-05-16 ~23:00

### 实验状态总览

| 实验 | 进程 | GPU | 状态 | 进度 |
|------|------|-----|------|------|
| **Qwen 训练链** | 134514 (train) | GPU 0, 50.8 GB | ✅ 运行中 | **6/7**, 当前 dataflow_aware_s44 |
| **StarCoder 训练链** | 129747 (train) | GPU 1, 54.2 GB | ⚠️ 刚 early stop | **5/9**, embedding_distance_s43 @step 1500 early stopped |
| **UniXcoder 训练链** | 191314 (train) | GPU 0, 13.5 GB | ✅ 运行中 | **4/6**, 当前 embedding_distance_s44 (step 850, R@1=0.607) |
| **D062 Eval** | 183027 (eval) | GPU 0, 13.9 GB | ✅ 运行中 | **6/14 selection**, 1/? test |
| **Watcher** | 966920 | — | ✅ 运行中 | 2d 0h |

### GPU 占用

| GPU | 利用率 | VRAM 已用/总量 | 空闲 |
|-----|--------|---------------|------|
| GPU 0 | 100% | 78,265 / 97,887 MiB | ~19.2 GB |
| GPU 1 | 100% | 54,247 / 97,887 MiB | **~42.6 GB** 🔴 |

### D062 Eval 详情 — 未完成 (6/14)

已完成 selection 文件（全部 random 策略）：

| Tag | Selection R@1 | Selection R@5 |
|-----|-------------|-------------|
| random_s42_best_by_val_loss | 0.2302 | 0.625 |
| random_s42_best_by_recall_at_1 | 0.2302 | 0.625 |
| random_s43_best_by_val_loss | 0.3413 | 0.750 |
| **random_s43_best_by_recall_at_1** | **0.5040** | **0.879** |
| random_s44_best_by_val_loss | 0.3532 | 0.750 |
| random_s44_best_by_recall_at_1 | 0.3532 | 0.750 |

**Best so far**: random_s43_best_by_recall_at_1 → Test R@1=0.489, Test R@5=0.852, Test R@10=0.948

剩余 8 个 selection eval: embedding_distance (s43/s44 × 2) + dataflow_aware (s43/s44 × 2) = 8。当前正在跑 test set eval。按每个 selection eval ~1h 估算，D062 还需 **~8-10 小时**完成全部。

### 各链详细进度

**Qwen (7 task chain)**: 已完成 random_s42/s43/s44, embedding_distance_s43/s44, dataflow_aware_s43。当前 dataflow_aware_s44 训练中 — **最后 1 个任务**。

**StarCoder (9 task chain)**: 已完成 random_s42/s43/s44, embedding_distance_s42/s43。embedding_distance_s43 刚 early stop @step 1500 (best val_loss=0.523, best R@1=0.489)。进程还没退出。剩余 4 个: embedding_distance_s44, dataflow_aware_s42/s43/s44。

**UniXcoder (6 task chain)**: 已完成 s43 全部 3 策略 + random_s44。当前 embedding_distance_s44 (step 850/~1400, epoch 2)。剩余: dataflow_aware_s44。

### 🔴 异常

1. **StarCoder PID 129747 early stop 后仍占 GPU 1 (54 GB)** — 日志已显示 "Early stopping triggered at step 1500" 但进程未退出，已运行 13h51m。可能是 wandb 上传或 checkpoint 保存卡住。若持续不退出需人工干预 (`kill 129747`)，链会自动启动下一个 embedding_distance_s44。

2. **GPU 1 有 42.6 GB 空闲** — StarCoder 单训练只用 54 GB。一旦当前训练退出并启动下一个，空闲部分不变。如果 StarCoder 进程卡死，这 42 GB 白白浪费。

### 建议

- 监控 StarCoder PID 129747，如 30 分钟内仍不退出，考虑手动 kill 让链继续推进
- D062 分析需等全部 14 selection 完成，预计明天上午可跑

---
