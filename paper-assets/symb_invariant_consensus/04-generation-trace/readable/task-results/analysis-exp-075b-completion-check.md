# analysis exp 075b completion check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-075b-completion-check_20260519T210608_result.json`
- **Structured JSON:** [`a0ad7a6e0b6e46d450b3.json`](../../sessions/a0/a0ad7a6e0b6e46d450b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (negative)。

**exp-075b 结果（Contrastive × Mistral × FOLIO-204, seed=42, normalization 修复后）：**

| 指标 | 值 |
|------|-----|
| SC accuracy | 0.5686 (116/204) |
| Contrastive accuracy | 0.4755 (97/204) |
| **Delta** | **-0.0931** |
| n_samples | 204 |
| Degenerate | 41/204 (20.1%) |
| Wall time | 193.6 min |

Negative result — normalization 修复后 contrastive 方法仍然比 SC baseline 低 ~9.3 个百分点。无错误，干净完成。

---
