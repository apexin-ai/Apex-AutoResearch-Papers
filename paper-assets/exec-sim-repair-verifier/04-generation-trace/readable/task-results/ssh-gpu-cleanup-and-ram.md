# ssh gpu cleanup and ram

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-cleanup-and-ram_20260519T225533_result.json`
- **Structured JSON:** [`3b63c600162b3a9a164b.json`](../../sessions/3b/3b63c600162b3a9a164b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**GPU 状态**

| GPU | Memory | Util | 状态 |
|-----|--------|------|------|
| 0 | 0MiB / 32607MiB | 0% | 干净 |
| 1 | 0MiB / 32607MiB | **100%** | 显存已释放但 util 仍卡 100%，容器不支持 GPU reset，无法通过软件恢复 |
| 2 | 29615MiB / 32607MiB | 85% | 有进程在跑 (PID 833672, python) |
| 3 | 0MiB / 32607MiB | 0% | 干净 |

**GPU 1 异常**: 显存 0MiB 但 GPU-Util 100%、P0 功耗 111W — 这是 GPU 卡死状态（hung context），容器内无法 reset。只有重启实例或联系平台才能恢复。

**GPU 2**: 有训练进程占用约 29.6GB，未在清理范围内，保持不动。

**RAM 基线**

| 指标 | 值 |
|------|-----|
| cgroup current | 68.4 GiB |
| cgroup max | 360 GiB |
| MemTotal | 754 GiB |
| MemAvailable | 700 GiB |
| MemFree | 466 GiB |
| Swap | 0 (无) |

GPU 3 已清理干净。GPU 1 需要实例重启才能恢复正常。

---
