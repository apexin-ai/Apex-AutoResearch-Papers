# ops check crm k1 train session bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-crm-k1-train-session-bjb2-28827_20260517T223806_result.json`
- **Structured JSON:** [`30eb7dc2fbfb19abb6fe.json`](../../sessions/30/30eb7dc2fbfb19abb6fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **`train-crm-k1-v2` session 已不存在** — tmux 报 "can't find pane"，当前只有 3 个其他 session（mag_obs_only_norm01_seed46/47, mag_perdof_norm02_seed43_r3）
- **GPU0 被其他进程占用** — PID 476536 (python) 占 5645 MiB，属于当前运行的其他实验，非 CRM K=1 训练残留

### 产出
- 训练是否已完成：**是**（session 已不存在，训练早已结束）
- tmux session 已关闭：**是**（已被之前清理或自动退出）
- GPU0 显存释放量：**0 MiB**（当前 GPU0 的 5645 MiB 占用来自其他实验 PID 476536，不是 CRM K=1 残留）

无需额外操作。

---
