# ops check unixcoder s42 results

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_unixcoder_s42_results_20260516T093038_result.json`
- **Structured JSON:** [`91d5fbced50a94a3c12f.json`](../../sessions/91/91d5fbced50a94a3c12f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. UniXcoder s42 Checkpoints — 全部就绪 ✓

每个策略目录 30MB，结构完整：

| 策略 | best_by_val_loss | best_by_recall_at_1 | final | train.log |
|------|:---:|:---:|:---:|:---:|
| random_s42 | ✓ | ✓ | ✓ | ✓ |
| embedding_distance_s42 | ✓ | ✓ | ✓ | ✓ |
| dataflow_aware_s42 | ✓ | ✓ | ✓ | ✓ |

每个 checkpoint 包含：`model.pt` (5.5MB) + tokenizer 文件 + `training_config.json`

### 2. UniXcoder s42 进程 — 已结束 ✓

无 UniXcoder 相关进程在运行。

### 3. GPU 占用状态

| GPU | 显存占用 | 总量 | 进程 |
|-----|---------|------|------|
| cuda:0 | 66,850 MiB | 97,887 MiB | PID 134514 (Qwen dataflow_aware_s44 训练) + PID 164287/165674 (evaluate_pool50 评估) |
| cuda:1 | 69,936 MiB | 97,887 MiB | PID 129747 (StarCoder2 embedding_distance_s43 训练) |

**cuda:0 当前被占用**，运行的是：
- Qwen2.5-Coder-3B `dataflow_aware_s44` 训练
- 两个 `evaluate_pool50.py` 评估任务（random_s43 best_by_val_loss）

### 4. s43/s44 脚本 — 就绪 ✓

两个脚本均存在且可执行：
- `/root/structfuse/scripts/run_unixcoder_3strategies_s43.sh` (2734B, 2026-05-16 15:59)
- `/root/structfuse/scripts/run_unixcoder_3strategies_s44.sh` (2734B, 2026-05-16 15:59)

**注意**：cuda:0 目前被 Qwen s44 训练 + 评估任务占满（~67GB），启动 UniXcoder s43/s44 需等当前任务完成或使用其他 GPU。

---
