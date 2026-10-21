# ops timeout and step20 monitor

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_timeout-and-step20-monitor_20260514T112333_result.json`
- **Structured JSON:** [`bd9399e07e6cd3c228c0.json`](../../sessions/bd/bd9399e07e6cd3c228c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Part 1 结果：Timeout 已修正。**

- 发现 `timeout 21600` (6h) 包裹训练进程
- 已 `kill -9` 掉 timeout 进程 (PID 39555)
- 训练进程 (PID 39556) 已 reparent 到 init (PID 1)，4 GPU worker 全部正常运行
- 训练不再受 6h 限制

**已有 metrics 预览（令人担忧）：**
- Step 5: loss=2.87×10⁸, reward=0.246
- Step 10: loss=0.34, kl=4.80, reward=0.284
- Step 15: loss=2.19×10¹⁰, kl=3.40×10¹¹, reward=0.415

交替出现的巨大 loss/KL 尖刺可能与 `num_iterations=2` 的奇偶迭代有关。等 step 20 数据后给完整报告。

---
