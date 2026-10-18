# kill cqa1 zombie 537176

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_kill_cqa1-zombie-537176_20260525T181403_result.json`
- **Structured JSON:** [`fe92bd3657271199d7fd.json`](../../sessions/fe/fe92bd3657271199d7fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：**

- PID 537176 已成功 kill，GPU0 已释放（原本该进程跑在 GPU0 上）

**当前 GPU 占用状态：**

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 1 MiB | 0% | **空闲可用** |
| 1 | 10279 MiB | 45% | 占用（PID 431242） |
| 2 | 1 MiB | 0% | **空闲可用** |
| 3 | 10591 MiB | 35% | 占用（PID 537521） |

GPU0 和 GPU2 空闲可用。

---
