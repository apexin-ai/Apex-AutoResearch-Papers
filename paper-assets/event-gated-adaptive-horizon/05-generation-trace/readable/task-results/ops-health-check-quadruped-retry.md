# ops health check quadruped retry

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_health-check-quadruped-retry_20260528T225706_result.json`
- **Structured JSON:** [`96172479a73b145deb70.json`](../../sessions/96/96172479a73b145deb70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Quadruped Walk 再次失败，同样的 EGL 错误。**

结果汇总：

| 实验 | 状态 | 详情 |
|------|------|------|
| Quadruped (PID 27003) | **已崩溃** | `ImportError: Cannot initialize a headless EGL display.` — 与上次完全相同的错误 |
| Humanoid (PID 25955) | **正常运行** | step 16000，train_return 0.8~1.7，fps 10.3 |

**GPU 负载：**
- GPU 0: 21% 利用率, 4692 MiB 显存（Humanoid）
- nvidia-smi 只返回了一行，**可能只有一张卡**

**关键问题：** nvidia-smi 只显示 1 张 GPU。Quadruped 被提交到 `cuda:1`，但如果机器只有一张卡，EGL device 1 不存在，初始化必然失败。需要确认这台机器的 GPU 数量——如果确实只有一张卡，Quadruped 需要排队等 Humanoid 跑完后在 `cuda:0` 上跑，或者改为共享 GPU。

---
