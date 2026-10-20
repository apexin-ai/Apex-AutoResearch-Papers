# train cwm8b v5 resume

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_cwm8b-v5-resume_20260515T175051_result.json`
- **Structured JSON:** [`96064fc7966b300f473c.json`](../../sessions/96/96064fc7966b300f473c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Resume confirmed. Progress bar jumped to 78% (5201/6633), training is actively running on cuda:2.

## 汇报

| 项目 | 值 |
|------|-----|
| **PID** | 400279 (bash) / 400280 (python) |
| **GPU** | cuda:2, 24293 MiB, 98% util |
| **当前 step** | 5201/6633 (从 ckpt-5200 resume 成功) |
| **剩余** | 1432 steps |
| **速度** | ~12 s/step (含 eval, 参考 v2 log) |
| **预计完成** | ~4.8h, 约 06:45 服务器时间 (UTC+8) |
| **日志** | `~/runs/exec-sim-repair-verifier/repo-level-cwm-8b-conda-v5.log` |
| **Registry** | `repo-level-cwm-8b-conda-v5` → RUNNING, parent=v4 |

无 timeout 限制，nohup 后台运行。

---
