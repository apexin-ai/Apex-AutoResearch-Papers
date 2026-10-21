# ops deploy bjb2 28827 cuda2 and bjb1 18228 cuda3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-bjb2-28827-cuda2-and-bjb1-18228-cuda3_20260518T210712_result.json`
- **Structured JSON:** [`2f269e7b68c35a85e1e1.json`](../../sessions/2f/2f269e7b68c35a85e1e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台都已成功启动，正在加载环境。

## 汇报

| 任务 | 服务器 | GPU | 实验 | tmux session | 状态 |
|------|--------|-----|------|-------------|------|
| 1 | bjb2-28827 | cuda:2 | obs_only ε=0.03 seed44 | `eval-obs-only-object-norm003-seed44-bjb2` | CRM 已加载，正在加载 LIBERO object 环境 |
| 2 | bjb1-18228 | cuda:3 | obs_only ε=0.03 seed49 | `eval-obs-only-object-norm003-seed49` | CRM 已加载，正在加载 LIBERO object 环境 |

bjb1-18228 cuda:3 原有 perdof seed43 仍在运行，显存 2410 MiB 足够共存。输出文件已按要求区分命名。

---
