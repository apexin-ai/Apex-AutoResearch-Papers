# research ece search

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ece_search_20260521T100603_result.json`
- **Structured JSON:** [`7edb7ce2e1654ee15eab.json`](../../sessions/7e/7edb7ce2e1654ee15eab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下（N=371,499，15-bin ECE）：

| Detector | AUC | ECE |
|----------|-----|-----|
| TF-IDF | 0.9377 | 0.0478 |
| GPT-2 PPL | 0.9130 | **0.1314** |
| N-gram PPL | 0.7312 | **0.0685** |

GPT-2 PPL 的 ECE 较高（0.1314），说明其 q_score 校准较差——这符合预期，因为它的 q_score 是通过 percentile-rank 从 PPL 转换而来，未做 temperature scaling。N-gram PPL 的 ECE 为 0.0685，TF-IDF 最低为 0.0478。

---
