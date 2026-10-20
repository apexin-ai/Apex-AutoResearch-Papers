# code grpo v7 oom fix

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo_v7_oom_fix_20260515T140350_result.json`
- **Structured JSON:** [`a8f34ece67d74088bf71.json`](../../sessions/a8/a8f34ece67d74088bf71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程都活着且在大量消耗 CPU：
- RASP (PID 526823): 481% CPU, 15.3 GB RSS
- Standard (PID 526899): 435% CPU, 15.1 GB RSS

正处于 CPU 端模型加载/数据集准备阶段，GPU 尚未分配显存。日志不更新是 Python stdout 缓冲的问题，属正常现象。模型上 GPU 后（~11 GB bf16 × 2 模型 = ~22 GB/卡）日志会刷新。

训练已在正常推进中。后续可用以下命令检查进度：
```bash
# 日志
tail -50 /root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_rasp_v7.log
tail -50 /root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_standard_v7.log

# GPU 显存
nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader
```

---
