# fix kill old crm object eval

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill-old-crm-object-eval_20260522T171918_result.json`
- **Structured JSON:** [`0d70f6ab5c8e16084a4e.json`](../../sessions/0d/0d70f6ab5c8e16084a4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**结果：**
- 3 个旧 eval 进程（seed42/43/44）及其子进程已全部 kill
- cuda:0/1/2 已释放（均 1 MiB）
- cuda:3 上的 CRM r4 训练未受影响（542 MiB）
- Registry 已更新：3 个实验均标记为 `conclusion=killed, status=DONE`

---
