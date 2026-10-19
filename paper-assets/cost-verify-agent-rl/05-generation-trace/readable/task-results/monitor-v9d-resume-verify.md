# monitor v9d resume verify

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v9d_resume_verify_20260520T052255_result.json`
- **Structured JSON:** [`238016589059adc6d5da.json`](../../sessions/23/238016589059adc6d5da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**DEAD** — 进程已崩溃，`EXIT_CODE=1`。

**崩溃原因**：vLLM KV cache 内存不足：
```
ValueError: No available memory for the cache blocks.
Try increasing `gpu_memory_utilization` when initializing the engine.
```

vLLM rollout 初始化时，模型权重加载到 GPU 后剩余显存不足以分配 KV cache blocks。4 张卡每张 ~5GB 已用（加载模型权重），但 96GB 卡理论上应该够用——可能是 `gpu_memory_utilization` 设置过低，或者 FSDP actor 和 vLLM rollout 共用 GPU 时内存冲突。

checkpoint 路径不存在，无法确认是否从 step 5 恢复（进程在恢复/val_before_train 之前就崩了）。

磁盘：102GB 可用（/root/autodl-tmp 60% used）。

---
