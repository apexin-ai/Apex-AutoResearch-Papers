# analysis exp020 final results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp020-final-results_20260517T093126_result.json`
- **Structured JSON:** [`a57c4d1de2361baf9f54.json`](../../sessions/a5/a57c4d1de2361baf9f54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-020-llama8b-folio-204 状态报告

**状态：运行中** — 33/204 完成，ETA ~105 min

### 当前中间统计 (n=32, 结果文件写入)

| 指标 | 值 |
|------|------|
| SICA accuracy | 65.62% (21/32) |
| SC accuracy | **71.88% (23/32)** |
| **Delta** | **-6.25pp (SC领先)** |
| McNemar p | 0.5000 |
| Bootstrap 95% CI | [-15.62, 0.00] |
| Discordant pairs | 0 SICA wins, 2 SC wins |
| Avg time/problem | 36.8s |
| Wall time elapsed | ~20 min |

### 日志实时 (33题已启动)

SICA 判定：21 correct (V), 11 incorrect (X) → 约 65.6%

### 关键信号

**SC 目前领先 SICA 6.25pp**。仅完成 15.7%，样本量太小（仅 2 个 discordant pairs），统计上无法下结论。但方向令人警惕。

需要等待全部 204 题完成（约 105 分钟后，~19:15 UTC）才能得到可靠结论。是否需要我到时候再检查一次？

---
