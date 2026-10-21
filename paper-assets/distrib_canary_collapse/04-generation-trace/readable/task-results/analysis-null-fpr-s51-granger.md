# analysis null fpr s51 granger

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_null_fpr_s51_granger_20260525T001345_result.json`
- **Structured JSON:** [`4b847204482296137039.json`](../../sessions/4b/4b847204482296137039.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。关键数字：

**s51 分析结果 (α=0.00, null seed)**
| 方法 | Forward FDR | Reverse FDR |
|------|-------------|-------------|
| PermG | **0/8** | 0/8 |
| DiffXCorr | 5/8 | 5/8 |
| NaiveXCorr (D111) | 2/8 | — |
| ThresholdOnset | 7/8 | — |
| TY Granger | 1/8 | — |
| K≥3 | **0/8** | — |

**合并 FPR (PermG, Clopper-Pearson CI)**

| | FP | Total | FPR | 95% CI |
|---|---|---|---|---|
| 9-seed (旧) | 4 | 54 | 7.4% | [2.1%, 17.9%] |
| **10-seed (新)** | **4** | **60** | **6.7%** | **[1.8%, 16.2%]** |

- FPR: 7.4% → 6.7%
- CI 上界: 17.9% → 16.2% (收窄 1.7pp)
- 0 FP seeds: 7/9 → 8/10
- K≥3 FPR 仍然 0/60 = 0%

---
