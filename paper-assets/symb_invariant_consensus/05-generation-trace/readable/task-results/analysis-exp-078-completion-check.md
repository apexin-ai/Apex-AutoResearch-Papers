# analysis exp 078 completion check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-078-completion-check_20260519T222708_result.json`
- **Structured JSON:** [`b83dd8c84847d20f7f9d.json`](../../sessions/b8/b83dd8c84847d20f7f9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/negative。

**exp-078 结果汇报：**

| 指标 | 值 |
|------|-----|
| SC accuracy | 0.5000 (100/200) |
| Debate accuracy | 0.2700 (54/200) |
| **Delta** | **-0.2300** |
| n_samples | 200/200 |
| Wall time | 211.5 min |
| Fallbacks | 16/200 |

Debate 在 Mistral×LogiQA 上大幅劣于 SC（-23pp），假设被否定。Debate 不仅没有纠正错误，反而让模型在多轮辩论中偏离正确答案。

---
