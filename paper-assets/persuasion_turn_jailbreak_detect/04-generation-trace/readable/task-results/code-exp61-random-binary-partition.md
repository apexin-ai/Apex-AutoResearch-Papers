# code exp61 random binary partition

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp61_random_binary_partition_20260522T164029_result.json`
- **Structured JSON:** [`96d78c19bd0c3f6e921b.json`](../../sessions/96/96d78c19bd0c3f6e921b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact registered (`art_20260522_81f242`).

## EXP-B 结果

**EXP-B: Random Binary Partition of 9 Strategy Labels** 已完成，10 个 partition，总耗时 16.1 分钟。

| 指标 | Mean ± Std |
|------|-----------|
| IID F1 | **1.0000 ± 0.0000** |
| DD OOD F1 | **1.0000 ± 0.0000** |
| AA OOD F1 | **0.9636 ± 0.1093** |

9/10 partition 全部三项指标完美，唯一异常是 **seed 7**（A=[1,4,6,7], B=[0,2,3,5,8]）的 AA F1 = 0.6356。

**关键结论**：无论如何随机二分策略标签，binary DAPT 的 OOD 泛化能力几乎不受影响。这进一步支持了"DAPT 阶段学到的是领域表征而非标签语义"的论点——即使将 9 类标签坍缩为任意二分，Stage-2 GRU 仍然能在 OOD 数据上泛化。

---

## Q2: 10-seed Scrambled TOST

10 个 scrambled permutation seeds: **42, 123, 456, 789, 1000, 2024, 2025, 2026, 314, 628**。

完整 10-seed TOST 分析已存在于 `results/exp41_tost_10seed_analysis.json`：
- **DD**: 等价（TOST p = 2.06e-9）
- **AA**: **不等价**（TOST p = 0.183, Cohen's d = 0.440）
- **FITD**: 平凡等价（两组均为 1.0）

---
