# code seed stratification

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_seed-stratification_20260517T001255_result.json`
- **Structured JSON:** [`ab7ad19ea9c7dc01461b.json`](../../sessions/ab/ab7ad19ea9c7dc01461b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `/root/gen-depth-fingerprint/experiments/seed_stratification/seed_stratification_results.json`。

**结论：`seed_independent`**

各组 F1 差异极小：
| Group | Binary F1 | Multiclass F1 |
|-------|-----------|---------------|
| low_complexity | 0.6847 | 0.7724 |
| medium | 0.6950 | 0.7779 |
| high_complexity | 0.6953 | 0.7792 |

- 最大组间差异 (binary): **1.06pp** (远低于 5pp 阈值)
- 最大组间差异 (multiclass): **0.68pp**

Depth fingerprint 的判别能力不依赖 seed 文本的词汇复杂度。

---
