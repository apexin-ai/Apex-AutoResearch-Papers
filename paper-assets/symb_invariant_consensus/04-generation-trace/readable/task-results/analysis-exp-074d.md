# analysis exp 074d

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-074d_20260519T214428_result.json`
- **Structured JSON:** [`ce0907aa21e052a1ede8.json`](../../sessions/ce/ce0907aa21e052a1ede8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。汇总：

**exp-074d (seed=456) 结果**

| 指标 | 值 |
|------|-----|
| SC accuracy | 55.88% (114/204) |
| ICG accuracy | 54.90% (112/204) |
| Delta | -0.98pp |
| Wall time | 57.3 min |
| Conclusion | negative |

**3-seed 汇总 (ICG × Mistral-7B × FOLIO-204)**

| Seed | SC | ICG | Δ |
|------|-----|-----|-----|
| 42 | 53.92% | 51.96% | -1.96pp |
| 123 | 57.35% | 58.82% | +1.47pp |
| 456 | 55.88% | 54.90% | -0.98pp |
| **Mean** | **55.72%** | **55.23%** | **-0.49pp** |
| **Std** | | | **1.77pp** |

ICG 在 FOLIO-204 上跨 3 seed 均值 Δ=-0.49pp±1.77pp，效果不显著且方向不一致（2 negative, 1 positive），确认 negative。

---
