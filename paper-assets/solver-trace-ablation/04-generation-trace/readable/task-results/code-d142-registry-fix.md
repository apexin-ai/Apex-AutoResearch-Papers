# code d142 registry fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d142-registry-fix_20260519T135843_result.json`
- **Structured JSON:** [`0f8a2f2c32eb1822c84e.json`](../../sessions/0f/0f8a2f2c32eb1822c84e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验的 registry metrics 已更新完成。汇总：

| | s55 | s56 | s57 |
|---|---|---|---|
| prove_rate | 1.0 | 0.36 | 0.88 |
| isr | 0.525 | 0.2925 | 0.4497 |
| TS_pct | 82 | 0 | 1 |
| CE_pct | 0 | 0 | 20 |
| PG_pct | 15 | 83 | 15 |
| CI_pct | 0 | 75 | 0 |
| genuine_pct | 3 | 17 | 64 |

主要修正：s55 的 CE/PG 被互换了（CE 18→0, PG 0→15）；s56 的 PG 从 91→83，新增 CI=75；s57 的 PG 从 73→15，CE 从 27→20，genuine 从 0→64。

---
