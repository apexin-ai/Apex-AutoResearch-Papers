# ops resubmit bjb2 28827 timeout16

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_resubmit-bjb2-28827-timeout16_20260518T212458_result.json`
- **Structured JSON:** [`e5acbd34d62a2778a889.json`](../../sessions/e5/e5acbd34d62a2778a889.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| 任务 | 状态 | 详情 |
|------|------|------|
| 1. Kill obs_only_norm003_seed44 | ✓ | session `eval-obs-only-object-norm003-seed44-bjb2` 已终止 |
| 2. 重提交 obs_only norm003 seed44 | ✓ | cuda:2, timeout 16h, session `eval-obs-only-norm003-seed44-t16` |
| 3. 重提交 perdof norm03 seed43 | ✓ | cuda:5, timeout 16h, session `eval-perdof-norm03-seed43-t16` |

**当前 GPU 空闲情况**：10 个 tmux session 运行中 + 刚提交 2 个 = 12 个。6 张 GPU 全部在用，无空闲 slot。

---
