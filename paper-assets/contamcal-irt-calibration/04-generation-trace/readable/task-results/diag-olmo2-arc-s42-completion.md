# diag olmo2 arc s42 completion

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_olmo2-arc-s42-completion_20260520T180106_result.json`
- **Structured JSON:** [`068862c5f29c5c9372d0.json`](../../sessions/06/068862c5f29c5c9372d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。Cron `eval_olmo2_arc_s42` 不存在（可能已被清理）。

**汇总：OLMo-2 ARC eval_olmo2_arc_s42 — SUCCESS**

| Dosage | s42 | s123 |
|--------|-----|------|
| d000 | 76.11% | 76.88% |
| d005 | 76.62% | 77.22% |
| d025 | 78.16% | 76.62% |
| d050 | 79.61% | 79.18% |
| d100 | 80.03% | 79.78% |

- **s42 Δ = +3.92pp**, s123 Δ = +2.90pp
- **双种子均值 Δ = +3.41pp (Benefit)**
- 与 MMLU 三种子均值 +1.35pp 方向一致，ARC contamination effect 约 2.5× MMLU
- s42 单调递增趋势比 s123 更干净（s123 在 d025 有回落，s42 没有）

---
