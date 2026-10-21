# analysis threshold 25k window

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_threshold-25k-window_20260515T104734_result.json`
- **Structured JSON:** [`675912d01c0b885ce390.json`](../../sessions/67/675912d01c0b885ce390.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**确认的 25K NVE 值（6/9 有数据）：**

| 实验 | 组别 | nve @25K |
|---|---|---|
| 008d (s1) | trained dt_emb | 1.78 |
| 009b (s2) | trained dt_emb | 2.05 |
| 008e_v3 (s1) | trained dt_emb | **1.93** (已确认) |
| 008e_v3 (s2) | trained dt_emb | 1.64 |
| 008f (s1) | no dt_emb | 1.02 |
| 009c (s2) | no dt_emb | 1.26 |

006、008a、008c 在 registry 中无 25K value-mean 数据。

**关键发现：** 008e_v3 (s1)（35K+ 的 false negative，max nve=0.94）在 25K 处 nve=1.93，远超 1.5x。这是一个早期 transient spike，35K 后消退。在有数据的 6 个实验中，1.5x threshold @25K 达到 4/4 TP + 2/2 TN = 100% accuracy，但受限于 6/9 覆盖率和小分母噪声放大。

两份报告（`artifacts/analysis/` 和 `artifacts/_project/report/`）已同步添加 §4.1。

---
