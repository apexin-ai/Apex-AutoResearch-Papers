# ops gpu0 cleanup and frozen ext

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu0-cleanup-and-frozen-ext_20260527T085423_result.json`
- **Structured JSON:** [`23f4ceddedf08cf3611e.json`](../../sessions/23/23f4ceddedf08cf3611e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| GPU | 显存占用 | 空闲 | 总量 | 利用率 |
|-----|---------|------|------|--------|
| 0 | 49176 MiB | **48077 MiB** | 97887 MiB | 0% |
| 1 | 3276 MiB | 93977 MiB | 97887 MiB | 22% |

**GPU 0 状况：**
- 49176 MiB 显存被驱动级泄漏占用（无进程持有），PID 612905 已不存在，无 tmux session `exp_hopper_frozen_s0`
- GPU reset 和 persistence mode 切换均被 AutoDL 阻止，无法释放泄漏显存
- 剩余 **48077 MiB (47 GB) 可用且已验证**（成功分配 37.3 GB 测试张量）

GPU 0 可正常使用，可用显存 47 GB 足够运行实验。如需完全释放 49 GB 泄漏显存，需重启 AutoDL 实例。

---
