# kill duplicate westd38929 gpu1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_kill-duplicate-westd38929-gpu1_20260523T211716_result.json`
- **Structured JSON:** [`737dc37fa7268b2d7eb6.json`](../../sessions/73/737dc37fa7268b2d7eb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理结果：

- **GPU 1**: 已清理干净，1 MiB / 0% 利用率
- **GPU 0**: PID 844866 已不存在。但 GPU 3 上有 PID 844403 在运行（4853 MiB），这可能是同一实验迁移后的进程
- **GPU 0/1/2**: 全部空闲（1 MiB）

注意：GPU 0 上的 PID 844866 已经不在了，当前唯一活跃进程是 GPU 3 上的 PID 844403。可能 eval_xvla_random_k05_goal_seed43 已经被调度到了 GPU 3，或者 GPU 0 的实验已经结束/被其他操作终止。需要确认 GPU 3 上的 844403 是否是目标实验。

---
