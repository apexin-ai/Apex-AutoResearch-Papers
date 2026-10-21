# fix bjb2 40593 k2 tau overlap

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bjb2-40593-k2-tau-overlap_20260525T004500_result.json`
- **Structured JSON:** [`2330146cdf5edb76f442.json`](../../sessions/23/2330146cdf5edb76f442.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个新任务已正常加载模型：

- **cuda:0**: 6211 MiB, 18% util → eval-k2-tau015-spatial-s42-r2 运行中
- **cuda:1**: 4624 MiB, 17% util → eval-k2-tau035-spatial-s42 运行中（chained from tau030）
- **cuda:2**: 6211 MiB, 18% util → eval-k2-tau010-spatial-s42-r3 运行中

---

**汇总**：

| 操作 | 结果 |
|---|---|
| bjb2-40593 tau010-r2 | 已杀（确认会超时，3/10 tasks in 78 min vs 2h limit） |
| bjb2-40593 tau015 | 已超时退出（EXIT_CODE=124，完成 4/10 tasks，无 JSON） |
| tau030 (bjb2-28827) | 完成 ✓ SR=80.0%, trigger_rate=16.9% |
| tau035 (bjb2-28827 cuda:1) | 继续运行中（chained，task 3/10） |
| **新提交** tau015-r2 | bjb2-28827 cuda:0, timeout=14400s |
| **新提交** tau010-r3 | bjb2-28827 cuda:2, timeout=14400s |

**根因**：原 timeout 7200s 不够（每 task ~26 min，10 tasks 需 ~4.3h）。加上 bjb2-40593 单 GPU 双开导致更慢。现在独立 GPU + 14400s timeout 应该足够。

**bjb2-40593 cuda:0 现已空闲**，可用于其他任务。

---
