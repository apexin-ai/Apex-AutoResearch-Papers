# diagnose exp 015b

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_015b_20260515T120747_result.json`
- **Structured JSON:** [`ab0cfd840d61a0514566.json`](../../sessions/ab/ab0cfd840d61a0514566.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 根因
**`CUDA error: invalid device ordinal`** — 脚本指定 `--device cuda:1`，但启动时 cuda:1 不可用。

关键 traceback：
```
File "/root/autodl-tmp/event-gated-adaptive-horizon/networks.py", line 111, in __init__
    torch.zeros((1, self._deter), device=torch.device(self._device)),
torch.AcceleratorError: CUDA error: invalid device ordinal
```

### 状态
- **训练步数**: 0（仅完成 prefill，模型初始化阶段就崩了）
- **metrics.jsonl**: 只有 4 行 step=0 的 prefill 数据，无训练 metrics
- **不是代码 bug**，不是 OOM，不是 `--dt_emb_freeze` 逻辑问题——纯粹是 GPU 设备不可达

### 当前 GPU 状态
服务器现在有 2 块 GPU：
- cuda:0: NVIDIA RTX PRO 6000 Blackwell (96GB)
- cuda:1: NVIDIA RTX PRO 6000 Blackwell (96GB)

当时启动时可能 `CUDA_VISIBLE_DEVICES` 只暴露了 1 块 GPU，或 cuda:1 被其他进程独占。

### 修复
直接重新运行 `submit_plan015b.sh` 即可。当前两块 GPU 都可用。由于 step=0 没有任何 checkpoint，需要从头开始。建议先清空旧 logdir 或用新目录名。

---
