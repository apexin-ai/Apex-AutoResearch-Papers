# ssh ram monitor 3parallel v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_ram-monitor-3parallel-v2_20260520T013027_result.json`
- **Structured JSON:** [`243f981d0a0258ad5e7b.json`](../../sessions/24/243f981d0a0258ad5e7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

有问题。两个 Qwen 训练还没上 GPU。

## 状态总结

### RAM: **76.9 GiB — SAFE**
(82,568,937,472 bytes / 1,073,741,824 = 76.9 GiB，远低于 300 GiB 红线)

### PID 存活: 3/3 ✓
| PID | RSS | Uptime |
|-----|-----|--------|
| 885624 (DeepSeek GPU2) | 2.1 GiB | 7:21 |
| 886273 (Qwen s123-v4 GPU0) | 3.5 MB | 3:53 |
| 886347 (Qwen s456-v3 GPU3) | 3.5 MB | 3:51 |

### GPU 状态
| GPU | Util | VRAM Used | Status |
|-----|------|-----------|--------|
| 0 | 0% | 0 / 32607 MiB | **空闲 — Qwen s123-v4 未上 GPU** |
| 1 | 100% | 0 / 32607 MiB | 异常：100% util 但 0 VRAM |
| 2 | 89% | 16709 / 32607 MiB | ✓ DeepSeek 正常运行 |
| 3 | 100% | 0 / 32607 MiB | **异常：100% util 但 0 VRAM** |

### 训练日志
两个 Qwen 训练日志都停在数据加载完成（`Class weights: fail=1.7009, pass=0.2991`），**模型尚未加载到 GPU**。已经 ~4 分钟了，可能还在 CPU 侧加载模型权重，也可能卡住了。

GPU 1 和 GPU 3 显示 100% utilization 但 0 VRAM 很可疑——nvidia-smi compute apps 只显示 pid 885624 在 GPU 2 上。

建议再等 2 分钟看日志是否有新输出，确认 Qwen 训练是在加载模型还是已经卡死。要继续监控吗？

---
