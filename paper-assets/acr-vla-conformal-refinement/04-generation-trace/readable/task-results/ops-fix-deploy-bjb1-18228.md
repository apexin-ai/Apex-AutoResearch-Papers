# ops fix deploy bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-deploy-bjb1-18228_20260518T191328_result.json`
- **Structured JSON:** [`143a4f9f4aab96282b6d.json`](../../sessions/14/143a4f9f4aab96282b6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

| 操作 | 状态 |
|------|------|
| Kill PID 855051 (GPU 2 重复 perdof norm003 seed44) | 已 kill，仅剩 PID 853864 |
| GPU 0: `eval-obs-only-object-norm003-seed47` | RUNNING，GPU 0 上 5645MiB |
| GPU 0: `eval-perdof-object-norm03-seed48` | RUNNING，GPU 0 上 5645MiB |
| GPU 3: `eval-obs-only-object-norm01-seed48` | RUNNING，GPU 3 上 5645MiB |

4 张 GPU 全部满载（GPU 0/1/2 各 2 进程，GPU 3 2 进程）。

---
