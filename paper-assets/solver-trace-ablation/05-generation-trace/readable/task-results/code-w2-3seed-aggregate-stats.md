# code w2 3seed aggregate stats

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w2-3seed-aggregate-stats_20260520T102229_result.json`
- **Structured JSON:** [`ea6885d8fc5b83826d64.json`](../../sessions/ea/ea6885d8fc5b83826d64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

写入完成: `artifacts/3seed_aggregate_stats.md`

核心数据:

**500-step (3 seeds)**:
- PR = 0.68 +- 0.47, ISR = 0.23 +- 0.30
- Pooled genuine = 5.9% (12/204), hacking = 94.1%
- 极大 seed variance: s42 CE-dominant, s43 collapsed (PR=13%), s44 TS-dominant

**1000-step (3 seeds)**:
- PR = 0.95 +- 0.05, ISR = 0.179 +- 0.305 (s43 ISR 是 TS artifact)
- Pooled genuine = 0% (strict), 1.0% counting H1-near
- **所有 3 seeds 在 1000 步均达 0% genuine** — hacking mode 不同 (s42=CE, s43=TS, s44=CE+PG)，但 genuine collapse 是跨 seed 不变量

---
