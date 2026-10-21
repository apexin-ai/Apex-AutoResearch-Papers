# diag exp054 exit check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp054-exit-check_20260519T024240_result.json`
- **Structured JSON:** [`2963c21a3eda0b88f9d5.json`](../../sessions/29/2963c21a3eda0b88f9d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:2 已释放（0MiB, 49W idle）。

## exp-054 结果总结

| 指标 | 值 |
|---|---|
| 状态 | **完成 (204/204)** |
| 结论 | **negative** |
| SICA accuracy | 55.4% (113/204) |
| SC accuracy | 54.9% (112/204) |
| delta | **+0.49pp** (统计不显著) |
| discordant_b (SICA only) | 5 |
| discordant_c (SC only) | 4 |
| McNemar chi2 | 0.1111 |
| McNemar p | **0.7389** |
| extraction rate | 97.3% |
| contradiction rate | 3.0% |
| wall time | 83 min |

T=1.0 相比 parent exp-033 (T=0.7, delta=+4.9pp)，delta 大幅缩小至 +0.49pp 且 p=0.74 完全不显著。提高温度未能增大 SICA 优势，反而基本抹平了差异。cuda:2 已释放。

---
