# analysis acc qw batch1 8k

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acc_qw_batch1_8k_20260516T010914_result.json`
- **Structured JSON:** [`3793215261fc494d1f16.json`](../../sessions/37/3793215261fc494d1f16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成分析，registry 和 artifacts 已更新。

## QW Accuracy Eval Batch1 (8k) 结果摘要

| 指标 | dense | importance_s020 |
|------|-------|-----------------|
| **Accuracy** | **44.0% (22/50)** | **26.0% (13/50)** |
| 截断率 | 2.0% (1/50) | 2.0% (1/50) |
| 平均生成长度 | 759.7 tokens | 722.1 tokens |
| 最大生成长度 | 8192 (截断) | 8192 (截断) |
| 总耗时 | 681.8s | 729.1s |

**关键发现：**
- s020 相对 dense 的 accuracy 降幅为 **-18pp**（44% → 26%），相对下降 **40.9%**
- 截断率极低（各仅 1 条），说明 8192 token 预算充足，之前 2048 的截断问题已修复
- s020 旧数据约 34%，现在 batch1 (n=50) 为 26%，差异可能来自题目子集不同或旧数据 rescore 版本差异

---
