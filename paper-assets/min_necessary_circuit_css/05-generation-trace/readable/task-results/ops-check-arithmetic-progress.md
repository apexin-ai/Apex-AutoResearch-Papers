# ops check arithmetic progress

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-arithmetic-progress_20260513T031253_result.json`
- **Structured JSON:** [`ffb18c4364f4a9f9a13d.json`](../../sessions/ff/ffb18c4364f4a9f9a13d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态：`mvp_arithmetic_gpt2_k3`

### 进程状态
**存活** — PID 900223，已运行 1h08m，RSS 2.3 GB

### 当前 Phase 及进度

| Phase | 状态 | 耗时 |
|-------|------|------|
| Phase A: EAP-IG | 已完成 | ~9s |
| Phase B: Edge Pruning | 已完成 | ~4s |
| Phase B: ACDC | **进行中** | ~54m+ |

ACDC 共 5 个阈值，当前在第 4 个（τ=0.07）：

| 阈值 τ | 状态 | 耗时 |
|--------|------|------|
| 0.01 | 完成 | 18:00 |
| 0.03 | 完成 | 17:48 |
| 0.05 | 完成 | 17:48 |
| **0.07** | **28746/32491 (88.5%)** | ~14:01 |
| 0.09 | 待运行 | — |

### GPU 利用率（cuda:5）
- GPU 计算利用率：**97%**
- 显存带宽利用率：**99%**
- 显存占用：2609 MiB / 24564 MiB (10.6%)
- 温度：59°C

GPU 利用率很高，没有问题。显存占用低但计算利用率高，符合 ACDC 特征：大量小 batch forward pass，计算密集但模型本身小（GPT-2 small ~124M 参数）。

内层迭代速度在 5~20 it/s 之间波动，是正常现象 — ACDC 反向遍历边时，越靠近输入端的边测试代价越高（需要更长的前向路径）。

### 预计剩余时间
- τ=0.07 剩余：**~3-4 分钟**
- τ=0.09（最后一个）：**~18 分钟**
- ACDC 后续 CSS 分析：**~1-2 分钟**（纯计算比较，不涉及 GPU 密集操作）
- **总计剩余：~22-24 分钟**

---
