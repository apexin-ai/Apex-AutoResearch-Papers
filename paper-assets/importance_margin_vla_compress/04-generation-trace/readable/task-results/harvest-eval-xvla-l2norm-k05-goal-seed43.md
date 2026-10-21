# harvest eval xvla l2norm k05 goal seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval_xvla_l2norm_k05_goal_seed43_20260523T225441_result.json`
- **Structured JSON:** [`43a642d8d9fac15c5599.json`](../../sessions/43/43a642d8d9fac15c5599.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 收割完成

**X-VLA L2norm k=0.5 Goal seed43 结果：**

| | seed42 | seed43 | Δ |
|---|---|---|---|
| SR | 59.0% | 60.2% | +1.2pp |
| 95% CI | — | [55.8%, 64.4%] | — |

**CV 结论**：两 seed 高度一致，L2norm k=0.5 Goal ≈ 59-60%。对比 Random k=0.5 Goal = 67.2%，L2norm 低 ~7-8pp，**确认 L2 在 X-VLA Goal 上的 anti-informativeness 可复现**。conclusion = negative。

**GPU 状态**：westd-38929 GPU 0 已空闲（0% utilization, 1 MiB）。无 QUEUED 实验排队。GPU 0 可用于新任务。

---
