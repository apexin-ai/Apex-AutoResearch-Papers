# ops grpo unpruned v2 diagnose

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_grpo-unpruned-v2-diagnose_20260516T014929_result.json`
- **Structured JSON:** [`84ad294c94cfdf588c28.json`](../../sessions/84/84ad294c94cfdf588c28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：训练仍在运行

PID 74579（启动器/父进程）已退出，但实际训练子进程 **PID 75381 仍然存活**，正在 cuda:1 上正常运行。

### 详细状态

| 项目 | 状态 |
|------|------|
| PID 74579 | DEAD（父/wrapper 进程） |
| PID 75381 | **ALIVE**，Rl 状态，已运行 1m49s |
| 命令 | `train_grpo_v5.py --gpu 0 ...` |
| 当前进度 | **Step 2/100**，~31s/step，预计总耗时 ~50min |
| Checkpoints | 暂无（save_steps=5，step 5 时出首个） |
| WandB run | `nhsx0bt2` — https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/nhsx0bt2 |
| 日志 | 36 行，最后记录到 step 2/100 |

### GPU 状态

| GPU | PID | 任务 | 显存占用 | 利用率 |
|-----|-----|------|---------|--------|
| cuda:0 | 74134 | eval_gsm8k.py（SFT baseline 评估） | 17,654 MiB | 90% |
| cuda:1 | 75381 | grpo_unpruned_v2 训练 | 83,192 MiB | 93% |

### 磁盘
`/root/autodl-tmp`: 110G/250G（44%），充足。

### 结论
**训练未退出，正在正常运行。** PID 74579 可能是 nohup/bash wrapper，退出不影响子进程。实际训练进程 75381 健康运行中，无需干预。

---
