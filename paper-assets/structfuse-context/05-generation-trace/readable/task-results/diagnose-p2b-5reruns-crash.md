# diagnose p2b 5reruns crash

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_p2b_5reruns_crash_20260512T191730_result.json`
- **Structured JSON:** [`9b9a50cc1923cb14a544.json`](../../sessions/9b/9b9a50cc1923cb14a544.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练没有崩溃，已全部正常完成。**

日志显示 `All 9 runs complete — Wed May 13 02:51:20 CST 2026`，退出码 `EXIT_CODE=0`。

### 9/9 runs 全部完成，汇总结果：

| 策略 | Seed | val_loss | recall@1 |
|------|------|----------|----------|
| **random** | 42 | 0.0347 | **0.9843** |
| **random** | 123 | 0.0446 | **0.9843** |
| **random** | 456 | 0.0188 | **0.9921** |
| embedding_distance | 42 | 0.1876 | 0.8740 |
| embedding_distance | 123 | 0.1461 | 0.8740 |
| embedding_distance | 456 | 0.1281 | 0.8819 |
| dataflow_aware | 42 | 0.1878 | 0.8740 |
| dataflow_aware | 123 | 0.1460 | 0.8740 |
| dataflow_aware | 456 | 0.1278 | 0.8819 |

磁盘正常（根分区 41%，数据盘 81%）。9 个 checkpoint 目录均已写入。GPU 空闲是因为训练跑完了，不是崩溃。

---
