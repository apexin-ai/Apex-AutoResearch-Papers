# analysis prior sensitivity j16 final read

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prior-sensitivity-j16-final-read_20260521T195210_result.json`
- **Structured JSON:** [`d70fc1be69afb31fd074.json`](../../sessions/d7/d70fc1be69afb31fd074.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册 (`art_20260521_2c1a1e`)。

**结果摘要：**

| Prior | σ | γ̂ | P(γ<0) | 过 Bonferroni? |
|-------|---|------|--------|---------------|
| Tight | 0.5 | −0.541 | 99.35% | **No** (差 0.025pp) |
| Baseline | 1.0 | −0.627 | 99.68% | Yes |
| Loose | 2.0 | −0.654 | 99.85% | Yes |

**Option A 失败。** Tight prior 差 0.025pp 未过 99.375% Bonferroni 阈值。三组诊断均正常（0 divergences, R̂≤1.008, ESS≥1373）。Baseline 与 §5.7 主分析完全一致（γ̂=−0.627, P(γ<0)≈99.68%），确认可复现。

→ 转 Option B。

---
