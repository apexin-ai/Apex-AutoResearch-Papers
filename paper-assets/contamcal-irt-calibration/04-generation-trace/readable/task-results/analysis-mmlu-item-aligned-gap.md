# analysis mmlu item aligned gap

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mmlu_item_aligned_gap_20260514T201711_result.json`
- **Structured JSON:** [`1b64ee4a7c78d13a3e47.json`](../../sessions/1b/1b64ee4a7c78d13a3e47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

### 1.5B d100
| 指标 | 值 |
|------|------|
| Full original (14042) | 0.5933 |
| Item-aligned original (6596) | 0.5963 |
| Paraphrase (6596) | 0.6252 |
| 原始 gap (misaligned) | **-3.19pp** |
| 修正 gap (item-aligned) | **-2.90pp** |
| QC selection bias | +0.56pp (QC-passed items 在 original 上略容易) |

### 3B d100
| 指标 | 值 |
|------|------|
| Full original (14042) | 0.6417 |
| Item-aligned original (6596) | 0.6413 |
| Paraphrase (6596) | 0.6763 |
| 原始 gap (misaligned) | **-3.46pp** |
| 修正 gap (item-aligned) | **-3.50pp** |
| QC selection bias | -0.08pp (几乎为零) |

### 结论

Item alignment 对 gap 的修正幅度极小（1.5B: 0.29pp, 3B: 0.04pp）。QC filter 的 selection bias 不是 gap 反转的原因——即使在完全相同的 6596 items 上比较，paraphrase 仍显著优于 original，gap 反转持续存在。

Reviewer #17 的 item mismatch concern 方法论上成立，但修正后结论不变。

---
