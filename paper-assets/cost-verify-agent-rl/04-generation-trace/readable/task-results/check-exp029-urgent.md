# check exp029 urgent

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp029_urgent_20260516T122205_result.json`
- **Structured JSON:** [`ea5edf41b10dcc9737c5.json`](../../sessions/ea/ea5edf41b10dcc9737c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp029 状态：已崩溃

**进程**: PID 855369 已死。

**GPU**: 两块 RTX PRO 6000 (96GB) 均空闲，0% 利用率，0 MiB 占用。

**崩溃原因**: vLLM 初始化时内存不足：

```
ValueError: Free memory on device cuda:0 (39.47/94.97 GiB) on startup is less than 
desired GPU memory utilization (0.5, 47.49 GiB). Decrease GPU memory utilization or 
reduce GPU memory used by other processes.
```

启动时 cuda:0 只有 39.47 GiB 可用（95 GiB 总量），而 vLLM 要求 50% = 47.49 GiB。说明启动时有其他进程占了约 55 GiB 显存。

**当前状态**: GPU 现在已完全空闲（可能是那些占用进程已结束），可以重新启动实验。

**修复方向**: 
1. 现在 GPU 已空闲，直接重启即可
2. 或降低 `gpu_memory_utilization` 参数（如 0.4）作为保险

---
