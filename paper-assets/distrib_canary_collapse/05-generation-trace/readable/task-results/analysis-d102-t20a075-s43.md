# analysis d102 t20a075 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d102-t20a075-s43_20260522T123100_result.json`
- **Structured JSON:** [`d63b73b9538b68986e79.json`](../../sessions/d6/d63b73b9538b68986e79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D102 分析完成，registry 已更新为 DONE (success)。

## 结果汇总

| 指标 | s43 | s42 | 一致性 |
|------|-----|-----|--------|
| **PermG forward (FDR)** | **6/8** | 6/8 | ✓ 完全一致 |
| PermG reverse | 0/8 | 0/8 | ✓ |
| Robust pairs (≥3/5) | 7/8 | - | - |
| Threshold onset | 6/8 | - | - |
| TY forward | 5/8 | - | - |

**显著 pairs (6/8):** te→d1, te→d2, te→d3, ece→d1, ece→d2, ece→d3

**非显著 pairs (2/8):** te→mauve, ece→mauve（mauve 系列在 T=20 下信号不足以通过 PermG FDR 校正）

Cross-seed validation 确认：T=20 α=0.75 的 6/8 ceiling 是 seed-independent 的。

---
