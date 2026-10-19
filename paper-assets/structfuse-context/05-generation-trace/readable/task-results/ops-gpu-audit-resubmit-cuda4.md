# ops gpu audit resubmit cuda4

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-resubmit-cuda4_20260513T020958_result.json`
- **Structured JSON:** [`e74bf7d9bb4be1ec671e.json`](../../sessions/e7/e74bf7d9bb4be1ec671e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:4 被一个**不同的**实验占用。以下是完整审计结果：

```
=== GPU 审计 ===
GPU 0: RTX 4090 D, 17109/24564 MiB, 100% util
GPU 1: RTX 4090 D, 0/24564 MiB, 0% util (空闲)
GPU 2: RTX 4090 D, 22101/24564 MiB, 17% util
GPU 3: RTX 4090 D, 22099/24564 MiB, 73% util
GPU 4: RTX 4090 D, 9269/24564 MiB, 100% util ← 被占用
GPU 5: RTX 4090 D, 2609/24564 MiB, 77% util

=== cuda:4 占用进程 ===
PID: 795791 (python, 9260 MiB)
启动时间: 2026-05-13 09:55 (今天)
命令: python training/train.py --train-file m2_pilot_data/train_random.jsonl ...
这是一个旧版 M2 pilot 实验（m2_pilot_data，非 m2_early_pilot_data），
参数也不同：--num-negatives 3 --max-seq-length 1024
环境: CUDA_VISIBLE_DEVICES=4, WANDB_MODE=offline

=== tmux sessions ===
仅有 hgate-dpo003-merged（来自其他项目，窗口为空）

=== wrapper 脚本 ===
run_m2_early_pilot.sh 所有关键修复均已到位：
✓ WANDB_MODE=offline
✓ TRANSFORMERS_OFFLINE=1 + HF_HUB_OFFLINE=1
✓ 本地模型路径 /root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B
✓ --batch-size 2
```

**cuda:4 当前无法使用**——被 PID 795791（旧版 m2_pilot 实验）占用，显存 9260 MiB，利用率 100%。

需要你确认：是否终止 PID 795791 以释放 cuda:4 来提交 m2_early_pilot_v4？这个旧实验使用的是不同数据集和参数，看起来是之前的遗留进程。

---
