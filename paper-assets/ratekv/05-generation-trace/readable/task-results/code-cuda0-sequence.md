# code cuda0 sequence

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cuda0_sequence_20260514T005232_result.json`
- **Structured JSON:** [`83000bfea5622914912c.json`](../../sessions/83/83000bfea5622914912c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已完成。

### 实验 1: compounding_sweep_k10_12
- k=10: PPL=11.50, k=12: PPL=11.42
- 完整曲线: k=8→11.23, k=10→11.50, k=12→11.42, k=16→11.81
- **k=8 确认为 U 型曲线极值点**

### 实验 2: ratequant_greedy_comparison
- Greedy PPL=**32.45** vs MCKP PPL=**11.23**，差距 +21.22
- Greedy 把 68/112 个 head 降到 2-bit（MCKP 只降 8 个），同时保留 10 个 16-bit head
- 证明离散 {2,4,8,16} 的非均匀步长破坏 polymatroid 结构，greedy 严重次优
- Cardinality constraint 是 greedy 无法自动发现的关键约束

---
