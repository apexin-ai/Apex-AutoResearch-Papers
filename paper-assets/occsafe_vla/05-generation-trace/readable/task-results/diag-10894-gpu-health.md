# diag 10894 gpu health

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_10894-gpu-health_20260527T003125_result.json`
- **Structured JSON:** [`53b5ae57128a7faa4a3a.json`](../../sessions/53/53b5ae57128a7faa4a3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

| GPU | 状态 | 说明 |
|-----|------|------|
| GPU 0 | **healthy** | 通过大矩阵乘法测试，结果 finite，运行后 utilization 已归零 |
| GPU 1 | **healthy** | 正常 |
| GPU 2 | **healthy** | 通过大矩阵乘法测试，结果 finite，运行后 utilization 已归零 |
| GPU 3 | **healthy** | 正常 |

之前 GPU 0/2 显示 100% utilization + 0 MiB 显存是之前异常退出的进程留下的驱动层残留状态（stuck utilization counter），不是硬件故障。跑了一次 CUDA 计算后 counter 已自动恢复。

**4 张卡 (cuda:0-3) 全部可用于训练。** 无残留进程，无 tmux 会话。

---
