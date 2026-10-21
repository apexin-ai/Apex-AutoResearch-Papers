# diagnose rsft ced s43 train r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_rsft_ced_s43_train_r2_20260516T002202_result.json`
- **Structured JSON:** [`f22eab3fc98f010ac393.json`](../../sessions/f2/f22eab3fc98f010ac393.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**根因：外部 SIGTERM，非 OOM/磁盘满。**

r2 在 step 95/510 (epoch 0.53) 训练正常时被 SIGTERM 杀死（exit code 143），loss=0.63，metrics 全部正常。

**时间线**：
- 08:10 r2 启动 → 08:19 r2 被 kill → 08:21 r3 在同一 GPU 上启动

**r3 已在运行**，PID 277315，GPU 1 占用 28GB/99% util。r3 参数与 r2 不同：`batch=4, grad_accum=4`（有效 batch 不变=16，但单步吞吐更高）。

**不需要重试**——r3 就是 r2 的替代品，当前正常训练中。监控 r3 进度即可。

---
