# analysis exp 025 n32

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_025_n32_20260516T142721_result.json`
- **Structured JSON:** [`a57e1a636620058ce0bd.json`](../../sessions/a5/a57e1a636620058ce0bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果如下：

## N=32 数据行

| Regime | N | Degeneracy% | LP_range | Oracle_F1 | Greedy_F1 | Oracle_gap | LP_Δ | SJ_Δ | FK_Δ | EM_Δ | VC_Δ | Best_Δ |
|--------|---|-------------|----------|-----------|-----------|------------|------|------|------|------|------|--------|
| rank32 | 32 | 4.0 | 0.0807 | 0.8061 | 0.5880 | 0.2181 | +3.53 | +2.95 | +3.24 | +2.83 | -1.56 | +3.53 |

## 各信号绝对 Selection F1

| Signal | F1 | Δ vs Greedy |
|--------|------|-------------|
| LP | 0.6232 | +3.53 |
| FK | 0.6204 | +3.24 |
| SJ | 0.6175 | +2.95 |
| EM | 0.6163 | +2.83 |
| VC | 0.5723 | -1.56 |

## 特殊发现

**信号排序变化**：N=16 时 FK > LP > SJ > EM > VC，N=32 时 **LP 重新超过 FK** 成为最佳信号。说明随 N 增大，LP 的区分度优势（LP_range 从 0.054→0.081）重新压过了 FK 在中等 N 时的一致性优势。

另外 Degeneracy 从 N=16 的 11.5% 降至 4.0%，Oracle gap 从 0.175 扩大到 0.218——N=32 提供了更大的选择空间，但 VC 信号反而变为负 delta，表明其在高 N 时退化严重。

---
