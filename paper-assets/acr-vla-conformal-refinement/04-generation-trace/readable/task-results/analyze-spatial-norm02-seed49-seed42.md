# analyze spatial norm02 seed49 seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_spatial-norm02-seed49-seed42_20260520T151735_result.json`
- **Structured JSON:** [`6e13455116645240021d.json`](../../sessions/6e/6e13455116645240021d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

```
eval-obs-only-spatial-norm02-seed49: SR=32%, total_rollouts=100  ✓ (在 30-38% 预期范围内)
eval-obs-only-spatial-norm02-seed42: ⚠️ 未完成 — 仅跑了 2/10 tasks 后进程被终止，JSON 未生成
```

**seed49 per-task 详情：**
| Task | SR |
|------|-----|
| between_plate_ramekin | 90% |
| next_to_ramekin | 90% |
| next_to_cookie_box | 80% |
| on_cookie_box | 30% |
| next_to_plate | 20% |
| top_drawer_cabinet | 10% |
| table_center | 0% |
| on_ramekin | 0% |
| on_stove | 0% |
| on_wooden_cabinet | 0% |

**seed42 问题诊断：** 日志只记录到 task 1 完成（between_plate_ramekin=90%, next_to_ramekin=100%），`~/runs/` 日志显示 EXIT_CODE=0 但输出被截断，JSON 从未写入。进程可能被 OOM 或 GPU 资源竞争 kill。需要重跑 seed42。

---
