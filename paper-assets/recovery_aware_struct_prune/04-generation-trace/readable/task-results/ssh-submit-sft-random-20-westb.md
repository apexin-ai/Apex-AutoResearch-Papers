# ssh submit sft random 20 westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_submit_sft_random_20_westb_20260523T231539_result.json`
- **Structured JSON:** [`7df50d52f184e546fe1d.json`](../../sessions/7d/7df50d52f184e546fe1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交，进程正在加载模型（尚未占 GPU 显存，处于 CPU 加载阶段）。

**汇报：**
- **PID**: 335348（python 主进程）
- **tmux session**: `eval_sft_random_20_v3`
- **GPU 0**: 模型加载中（当前 3MiB，加载完成后会占用 ~15GB）
- **Checkpoint**: `/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20/model.safetensors`（12GB）
- **输出**: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_random_20_fixed_v3.json`
- **日志**: `/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_random_20_fixed_v3.log`
- GPU 1 上的 grpo_random_20 eval（PID 330254）不受影响，继续运行

---
