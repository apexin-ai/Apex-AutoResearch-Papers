# code fix rrf skip patterns

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-rrf-skip-patterns_20260516T024651_result.json`
- **Structured JSON:** [`726e56695fe12ae494dc.json`](../../sessions/72/726e56695fe12ae494dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果正确：

- **SKIP (5个)**: 4个 alpha=16 旧目录 + 1个已标 DEPRECATED 的
- **KEEP**: 全部 0.5B/1.5B (8个) + 3B s123 (2个) + `_v3_` (1个) + `_a32_` (1个) — 无误排除

修改内容：`exp003/rrf_aggregation.py` 第 42-49 行新增 `ALPHA16_BLOCKLIST` set，第 233 行过滤条件加上 `or model_id in ALPHA16_BLOCKLIST`。

---
