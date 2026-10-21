# analysis exp 041 folio204 results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-041-folio204-results_20260518T202043_result.json`
- **Structured JSON:** [`a95f964b38318771b9ef.json`](../../sessions/a9/a95f964b38318771b9ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated, cron already cleared.

## exp-041 结果

实验实际完成，结果存于 `exp036_qwen25_14b_folio204/` 目录（之前被 auto-monitor 误判为 failed）。

| 指标 | exp-041 (westd-16639) | exp-026 (westd-25068) |
|---|---|---|
| SICA | 75.49% (154/204) | 74.51% |
| SC | 77.45% (158/204) | 75.00% |
| delta | **-1.96pp** | -0.49pp |
| McNemar p | **0.0455** (显著) | — |
| extraction_rate | 0.9800 | — |
| contradiction_rate | 0.0097 | — |
| discordant | sica_only=0, sc_only=4 | — |

**结论：negative。** Capability trap 方向一致（SC > SICA），且在 westd-16639 上 delta 更大、McNemar 达到显著（p=0.0455）。SC baseline 更高 (+2.45pp)，说明不同服务器环境存在 variance，但 SICA 始终未能超越 SC。不支持可复现性中的"数值一致"，但支持"结论一致"。

---
