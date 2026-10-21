# check exp029 progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp029_progress_20260516T122117_result.json`
- **Structured JSON:** [`01a3027e253eb4535de3.json`](../../sessions/01/01a3027e253eb4535de3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp029_episode_level 状态报告

**进程: 已死亡** — PID 855369 不存在，EXIT_CODE=1。

**GPU: 空闲** — cuda:0 和 cuda:1 均 0% 利用率，0 MiB 显存占用。

**失败原因: vLLM 显存不足**

```
ValueError: Free memory on device cuda:0 (39.07/94.97 GiB) on startup is less than 
desired GPU memory utilization (0.5, 47.49 GiB).
```

vLLM rollout worker 初始化时，cuda:0 上只有 39 GiB 空闲（95 GiB 总量），而配置要求 `gpu_memory_utilization=0.5`（即 47.49 GiB）。说明启动时有其他进程占用了 ~56 GiB 显存（大概率是 FSDP actor/ref 模型先加载占用了显存）。

**当前 step:** 未到达任何训练 step，在模型初始化阶段即崩溃。

**val_before_train:** 未执行。

**W&B run:** 未创建（崩溃太早）。

**根因分析:** 2-GPU 配置下，FSDP actor 和 vLLM rollout 共享 cuda:0，actor 模型加载后剩余显存不足以满足 vLLM 的 50% 预留要求。需要：
1. 降低 `gpu_memory_utilization`（如设为 0.3 或 0.4），或
2. 调整 worker 分配让 vLLM rollout 独占一张卡，或
3. 启用 `param_offload` 减少 actor 在 GPU 上的驻留显存。

---
