# analyze eval rsft ced s45

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_rsft_ced_s45_20260516T042237_result.json`
- **Structured JSON:** [`c457e5c3fb915646ec0d.json`](../../sessions/c4/c457e5c3fb915646ec0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval_rsft_ced_s45 结果

| 指标 | 值 |
|------|------|
| **F1** | **0.4514** |
| Ign-F1 | 0.4416 |
| Precision | 0.4718 |
| Recall | 0.4326 |
| Evi-F1 | 0.8174 |
| EDCR | 0.6550 |
| Evi-F1 (joint) | 0.3558 |
| Format OK | 100% (985/985) |
| Truncated | 206/985 |

F1=0.4514 > 0.40 阈值，标记 success。与 flat-NLI s42 (0.4539) 基本持平（差 0.0025）。

Registry 已更新为 DONE，产出已注册。等 s42/s43/s44 的 CED 结果确认后即可做 paired t-test。

---
