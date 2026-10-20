# analysis nve sensitivity

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nve_sensitivity_20260515T125303_result.json`
- **Structured JSON:** [`81364387ee261c90b661.json`](../../sessions/81/81364387ee261c90b661.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

- **AUROC = 0.944**（3 正类 vs 6 负类，max NVE 作为连续分数）
- **最优阈值 NVE ≥ 1.5x**：
  - 单次触发：accuracy 88.9%, recall 100%, precision 75%（唯一 FP 是 008e_v3_s2 的 late-onset collapse）
  - ≥2 连续 checkpoint 触发：accuracy 88.9%, **precision 100%**, recall 66.7%（唯一 FN 是 009b，它自行恢复了）
- 正类 NVE 范围 1.29–4.83，负类（除 008e_v3_s2 外）NVE 范围 0.30–1.14，分离度很好
- 008e_v3_s2 是唯一的 edge case：NVE 在 85K 前始终 ≤1.06，95K 突然跳到 1.34 再到 105K 的 3.78，consecutive ≥1.5 准则可正确排除

报告已写入 `artifacts/nve_sensitivity_analysis.md` 并注册。

---
