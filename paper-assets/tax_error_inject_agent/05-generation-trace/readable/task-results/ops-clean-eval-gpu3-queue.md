# ops clean eval gpu3 queue

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_clean-eval-gpu3-queue_20260516T111048_result.json`
- **Structured JSON:** [`b64dcd4a8ba5a3532c43.json`](../../sessions/b6/b64dcd4a8ba5a3532c43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

7/47。进度正常。由于 eval 流程需要长时间等待，我总结目前状态：

---

**已完成的 eval 结果：**

| Eval | Success Rate | Recovery Rate | Detection Rate |
|------|-------------|---------------|----------------|
| Recovery Random s0 | 0.553 | 0.553 | 0.0 |
| **LLaMA Random s42 Clean** | **0.766** | N/A (clean) | N/A (clean) |

**进行中：**
- TaxEI s7 recovery eval: 7/47 (PID 270658, GPU 3)

**待执行队列：**
- Random s1 → Random s7 → Random s123

每个 eval 完成后，我会自动收集结果并启动下一个。TaxEI s7 预计还需约 50 分钟。

---
