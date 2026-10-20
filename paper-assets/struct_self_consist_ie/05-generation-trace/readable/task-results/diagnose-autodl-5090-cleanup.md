# diagnose autodl 5090 cleanup

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_autodl-5090-cleanup_20260518T010051_result.json`
- **Structured JSON:** [`7154db6adc471fd4a676.json`](../../sessions/71/7154db6adc471fd4a676.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。核心发现：

**两个实验已自行恢复，正在正常运行，无需任何干预。**

- **磁盘**: `/root/autodl-tmp` 有 149G 空闲，非空间问题。原 I/O 错误推测为 RAID 瞬时抖动。
- **GPU**: 旧 vLLM PID 416808 已不存在。当前 GPU 0/1 各跑一个训练任务，GPU 2/3 空闲。
- **Checkpoint**: 两个 checkpoint-100 均完整保存（1015M，含 adapter + optimizer）。
- **训练进度**: 3-epoch 已过半(51%)，10-epoch 在 14.5%，loss 曲线正常。
- **预计完成**: 3-epoch ~8min，10-epoch ~40min。

报告已写入 `artifacts/exp_029a/report/server_diagnostic.md`。

---
