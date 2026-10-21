# analyze qwen17b retry s1 check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_qwen17b-retry-s1-check_20260514T215900_result.json`
- **Structured JSON:** [`c4ddada5fca4b4762b0c.json`](../../sessions/c4/c4ddada5fca4b4762b0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**plan-002-qwen17b-retry-s1: failed**

- 进程被 SIGHUP 终止 (EXIT_CODE=129)，仅完成 29% (144/498 seeds)
- 产出 693 条记录（远低于 2000 阈值），148 unique seeds
- Depth 分布 `{0:148, 1:145, 2:142, 3:132, 4:126}`，分布本身合理但数据不完整
- Registry 已更新 conclusion=failed 及 failure_reason

---
