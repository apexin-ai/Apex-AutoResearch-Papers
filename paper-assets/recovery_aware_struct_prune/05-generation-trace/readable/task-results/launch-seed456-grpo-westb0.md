# launch seed456 grpo westb0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_seed456_grpo_westb0_20260522T123544_result.json`
- **Structured JSON:** [`46123cf2e5f945393f6a.json`](../../sessions/46/46123cf2e5f945393f6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GRPO seed456 已成功启动，数据集准备中，训练即将开始。

## 汇总

| 项目 | 值 |
|------|-----|
| **Bash PID** | 205665 |
| **Python PID** | 205670 |
| **GPU** | cuda:0 (RTX PRO 6000, 12326MiB / 97887MiB) |
| **命令** | `train_grpo.py --model_path sft_random_20 --output_dir grpo_random_20_seed456 --seed 456 --per_device_train_batch_size 1 --num_train_epochs 3` |
| **磁盘** | `/root/autodl-tmp/` 14GB 可用 (95%) |
| **日志** | `/root/recovery_aware_struct_prune/results/train_grpo_random_20_seed456.log` |

**注意**: 原始命令中的 `--max_steps 100` 和 `--save_only_model true` 不是该脚本的有效参数，已去掉。脚本通过 `--num_train_epochs`（默认 3）控制训练量。

**日志进度**:
1. `20:37:35` - 开始加载剪枝模型
2. `20:37:36` - 检测到非均匀 MLP (intermediate_size 11508-17592) 和 attention (heads 7-28)
3. `20:39:27` - 模型成功加载到 cuda:0
4. `20:39:27` - 准备 GSM8K 训练数据集（进行中）

---
