# ops westb cuda1 random eval sft

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_cuda1_random_eval_sft_20260517T112531_result.json`
- **Structured JSON:** [`04cc5a860c98145fec4f.json`](../../sessions/04/04cc5a860c98145fec4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 710618 是另一个实验（cka_only_20 eval on GPU 0），不相关。

## 结果汇报

**Random post-prune accuracy (GSM8K N=200)**: **34.0%** (68/200, stderr=0.033, greedy)
- EOS rate: 45.5%（109/200 truncated at 4096 tokens）

**Random SFT 已启动**:
- 主进程 PID: **710278** (python), 父进程 710272 (bash wrapper, PPID=1)
- GPU 1: **24762MiB** 已分配（model 12374MiB × 2 进程: 710113 + 710278）
- 当前阶段: 数据集预处理（CPU 568%, GPU-Util 0%），训练即将开始
- 日志: `/root/autodl-tmp/recovery_aware_struct_prune/results/sft_random_20.log`
- 输出: `/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20/`
- 参数: `--save_strategy no --seed 42`

**注意**: 发现之前有另一个 Worker 在 GPU 0 启动的 random SFT (PID 708727) 在检查期间自行消亡（输出目录不存在，疑似父 SSH session 断开导致），已确认当前启动的是唯一在跑的 random SFT。

---
