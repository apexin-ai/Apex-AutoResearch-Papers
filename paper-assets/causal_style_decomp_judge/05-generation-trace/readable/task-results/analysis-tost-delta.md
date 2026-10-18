# analysis tost delta

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tost-delta_20260522T035524_result.json`
- **Structured JSON:** [`a7c5160db50be628ac5c.json`](../../sessions/a7/a7c5160db50be628ac5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**TOST Minimum Detectable Equivalence Margin 结果**:

**Proportions TOST**（实际分析所用方法，win-rate 检验）:

| 参数 | 值 |
|------|---|
| n | 87 pairs |
| α | 0.05 (one-sided) |
| SE(p=0.5) | 0.0536 |
| **Δ_min (80% power)** | **0.157** |
| Equivalence region | [0.343, 0.657] |

**关键发现**: 实际分析用 Δ=0.10 时 power 仅 **17.5%**——严重 underpowered。要达到 80% power 需要 Δ≥0.157。

**Margin-Power 对照**:

| Margin Δ | Power | Region |
|----------|-------|--------|
| 0.10 | 17.5% | [0.40, 0.60] |
| 0.157 | 80% | [0.343, 0.657] |
| 0.176 | 90% | [0.324, 0.676] |

**论文用句**: "With n≈87 pairs and α=0.05, the TOST procedure achieves 80% power to reject non-equivalence only when the equivalence margin is Δ≥0.157 (win-rate within [0.343, 0.657]); at the pre-registered margin Δ=0.10, achieved power is only 17.5%."

---
