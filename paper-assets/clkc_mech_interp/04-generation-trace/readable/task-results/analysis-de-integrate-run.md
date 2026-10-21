# analysis de integrate run

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_de-integrate-run_20260523T070627_result.json`
- **Structured JSON:** [`70ec3db8cd234c293866.json`](../../sessions/70/70ec3db8cd234c293866.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 屏幕输出 — 4 方向表格

| Direction | Peak Layer | Bal Acc (mean) | 95% CI |
|-----------|-----------|----------------|--------|
| EN→EN | 18 | 0.7709 | [0.7463, 0.7978] |
| DE→DE | 13 | 0.7626 | [0.7390, 0.7868] |
| EN→DE | 16 | 0.6923 | [0.6324, 0.7390] |
| DE→EN | 13 | 0.7047 | [0.6654, 0.7426] |

### Δ_asym

- **Δ_DE** = (DE→EN) − (EN→DE) = **+1.24pp**, 95% CI [−4.78, 8.09], p = 0.4045 (**不显著**)

### 跨语言对比

| Metric | EN-ZH | EN-DE |
|--------|-------|-------|
| Δ_asym (pp) | +7.3 [0.4, 14.0] p=0.038 | +1.24 [−4.78, 8.09] p=0.4045 |
| Token overlap (%) | 3.4% | 14.77% |

### Scenario 判定：**Scenario A**

DE 的 token overlap 高达 14.77%（远高于 ZH 的 3.4%），但不对称性反而不显著（p=0.40），说明 token overlap 不是驱动 EN-ZH 不对称性的原因。

JSON summary 已保存至 `data/llama31/de_integration_summary.json`，内容与上述一致，`"scenario": "A"`。

---
