# harvest westd41074 completed 0527

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_westd41074_completed_0527_20260527T031404_result.json`
- **Structured JSON:** [`ca0c2536eeca0b565b4d.json`](../../sessions/ca/ca0c2536eeca0b565b4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。最终汇总：

---

### 1. π0.5 Random k=0.85 Long strict
- **seed42: SR = 45.2%** (226/500)
- **seed43: SR = 45.6%** (228/500)  
- **平均: 45.4%**

Per-task (seed42): 42% | 56% | 64% | 70% | 18% | 24% | 36% | 52% | 14% | 76%

对比原始非 strict 结果 44.4% → strict 45.2%，差异不大（+0.8pp）。

### 2. OpenVLA Attn k=0.75 Long (libero_10)
- **超时失败** (EXIT_CODE=124)，完成 8/10 tasks
- 部分 SR: 159/400 = 39.75% (前 8 个 task)
- 需要重跑或估算

### 3. OpenVLA Random k=0.75 Long (libero_10)
- **仍在运行** (GPU 1, PID 856656)
- 当前进度: Task 9/10, ep 10/50
- 前 8 task: 178/400 = 44.5%
- 预计 ~1.5h 完成

### westd-41074 当前 GPU 状态
| GPU | 占用 | 实验 |
|---|---|---|
| 0 | 15.8 GB | OpenVLA Random k=0.95 Long seed42 |
| 1 | 15.8 GB | OpenVLA Random k=0.75 Long seed42 |
| 2 | 空闲 | — |
| 3 | 空闲 | — |

---
