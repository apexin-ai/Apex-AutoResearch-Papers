# check pid33047 identify

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_pid33047-identify_20260516T140733_result.json`
- **Structured JSON:** [`ee7a3004ebe5cb67357a.json`](../../sessions/ee/ee7a3004ebe5cb67357a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：**

| 项目 | 详情 |
|------|------|
| PID 33047 身份 | `eval_acib.py` dry run（评估 v7_contrastive checkpoint step 5000，输出到 /tmp/v7_eval_dryrun） |
| 所在 GPU | GPU 1（与 v7_seed2 PID 27427 同卡） |
| 占用显存 | 5459 MiB |
| 处理 | 已 kill（eval 残留，非 v7 训练子进程） |

**当前 GPU 状态：**
- PID 21363 — 16220 MiB（GPU 0，v7_contrastive 训练，正常）
- PID 27427 — 16218 MiB（GPU 1，v7_seed2 训练，正常）
- PID 35765 — 5996 MiB（GPU 1，未识别进程，需要时可进一步排查）

---
