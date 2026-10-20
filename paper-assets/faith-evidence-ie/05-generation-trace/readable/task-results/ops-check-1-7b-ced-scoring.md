# ops check 1 7b ced scoring

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_1_7b_ced_scoring_20260517T013800_result.json`
- **Structured JSON:** [`a27faf2c8ad30338533e.json`](../../sessions/a2/a27faf2c8ad30338533e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**任务仍在运行中，尚未完成。**

状态摘要：
- **进度**: 8500/24216 records scored (~35%)，最后一条日志 09:38:08
- **速率**: 约 500 records / 2.5 min，预计剩余 ~79 min（约 10:57 完成）
- **进程**: PID 395619，正常运行，CPU 109%

**GPU 使用情况**:
| GPU | 显存占用 | 利用率 | 状态 |
|-----|----------|--------|------|
| cuda:0 | 12332/32607 MiB | 87% | CED scoring (PID 395619) + 另一进程 (PID 396338) |
| cuda:1 | 11119/32607 MiB | 53% | 占用 (PID 390436) |
| cuda:2 | 0/32607 MiB | 0% | **空闲** |
| cuda:3 | 28067/32607 MiB | 72% | 占用 (PID 349387) |

只有 **cuda:2 完全空闲**，其余均被占用。

不更新 registry，等任务完成后再处理。

---
