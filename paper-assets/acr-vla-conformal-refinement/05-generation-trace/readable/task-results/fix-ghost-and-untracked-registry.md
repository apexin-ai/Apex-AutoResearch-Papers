# fix ghost and untracked registry

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_ghost-and-untracked-registry_20260517T133100_result.json`
- **Structured JSON:** [`f3cbd8ac6bb65ed17a27.json`](../../sessions/f3/f3cbd8ac6bb65ed17a27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个子任务全部完成。

**汇总：**

| 子任务 | 结果 |
|--------|------|
| 1. Ghost 修复 eval-obs-only-object-norm01-seed45 | ✅ DONE/failed |
| 2a. eval-obs-only-object-norm005-seed43-r2 (bjb1-32546) | ✅ RUNNING + cron |
| 2b. eval-obs-only-object-norm003-seed43 (bjb1-18228) | ⚠️ PID 621127 已死，标记 DONE/failed |
| 2c. eval-perdof-object-norm02-seed47 (bjb2-28827) | ✅ RUNNING + cron |
| 2d. eval-random-selection-object-seed42 (bjb2-40593) | ✅ RUNNING + cron |
| 3. 部署 perdof ε=0.2 seed45 (bjb1-18228 cuda:0) | ✅ PID 632167 运行中，模型加载中 |

**需要关注：**
1. `eval-obs-only-object-norm003-seed43` (PID 621127) 已死，需要重新部署
2. bjb1-18228 上还有一个未在任务列表中的 `eval-perdof-object-norm02-seed45-r2` (PID 631702, cuda:1)，可能也需要注册追踪

---
