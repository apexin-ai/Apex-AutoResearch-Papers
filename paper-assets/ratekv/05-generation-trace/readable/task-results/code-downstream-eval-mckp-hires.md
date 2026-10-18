# code downstream eval mckp hires

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_downstream_eval_mckp_hires_20260514T071342_result.json`
- **Structured JSON:** [`9f80edf633a2362bf15c.json`](../../sessions/9f/9f80edf633a2362bf15c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**mckp_hires 条件已完成**，三个条件全部有数据。allocation 来自 `exp_e_results.json` -> `constrained_allocation`，bit 分布 {8:4, 4:100, 2:8} 与 hires_reeval 确认的完全一致。

结果（使用 acc_norm，WinoGrande 用 acc）：

| Task | Baseline bf16 | Uniform 4-bit | MCKP Hires | Δ (MCKP vs Uniform) |
|------|--------------|---------------|------------|---------------------|
| ARC-C | 0.4957 | 0.4821 | 0.5137 | **+0.0316** |
| HellaSwag | 0.7818 | 0.7284 | 0.7684 | **+0.0400** |
| PIQA | 0.7922 | 0.7661 | 0.7786 | **+0.0125** |
| WinoGrande | 0.7119 | 0.6622 | 0.6819 | **+0.0197** |
| **Average** | **0.6954** | **0.6597** | **0.6857** | **+0.0260** |

关键数据点：
- Uniform 4-bit 相对 baseline 平均下降 3.57 pp
- MCKP hires 恢复了 2.60 pp，**recovery rate = 72.8%**
- MCKP 在所有 4 个 task 上一致优于 uniform，ARC-C 甚至**超过 baseline**（+1.8 pp）
- 这些结果与 PPL 趋势一致（baseline 9.81 → uniform 15.45 → MCKP 10.91）

---
