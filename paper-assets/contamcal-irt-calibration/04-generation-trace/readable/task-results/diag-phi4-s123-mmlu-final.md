# diag phi4 s123 mmlu final

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_phi4-s123-mmlu-final_20260520T155817_result.json`
- **Structured JSON:** [`eb9835753b055ebc198a.json`](../../sessions/eb/eb9835753b055ebc198a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phi-4 s123 MMLU eval **5/5 complete**。Registry 已更新为 DONE(success)。

| Dosage | Accuracy | vs d000 |
|--------|----------|---------|
| d000 | 76.31% | — |
| d005 | 75.92% | -0.39pp |
| d025 | 77.02% | +0.71pp |
| d050 | 77.30% | +0.98pp |
| d100 | 78.14% | **+1.83pp** |

Pattern: 与 s42 的 immune pattern(-0.17pp) 不同，s123 显示轻微正向趋势(+1.83pp at d100)。westd cuda:2 已释放。

---
