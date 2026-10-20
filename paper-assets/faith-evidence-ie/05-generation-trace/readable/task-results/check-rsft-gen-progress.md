# check rsft gen progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_rsft_gen_progress_20260515T042640_result.json`
- **Structured JSON:** [`e48cb4eb200931a557d3.json`](../../sessions/e4/e48cb4eb200931a557d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## RSFT 生成进度汇总

所有 4 个进程均在运行中（100% CPU，~2.3GB RSS，已运行 ~2h45m）。

| Shard | 进度 | 输出行数 | 预计剩余 |
|-------|------|----------|----------|
| shard_0 | 613/682 (89.9%) | 5000 行 | ~21 min |
| shard_1 | 657/681 (96.5%) | 5360 行 | ~6 min |
| shard_2 | 654/681 (96.0%) | 5352 行 | ~10 min |
| shard_3 | 581/657 (88.4%) | 4680 行 | ~25 min |

**总体**: ~92% 完成，预计 shard_3 最晚完成（约 25 分钟后）。全部 shard 无异常，shard_0/2 有 truncation_rate >10% 的 warning 但不影响运行。

---
