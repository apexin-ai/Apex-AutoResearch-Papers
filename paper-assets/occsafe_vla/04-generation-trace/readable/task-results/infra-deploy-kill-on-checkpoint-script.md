# infra deploy kill on checkpoint script

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_deploy-kill-on-checkpoint-script_20260521T063405_result.json`
- **Structured JSON:** [`e55b93660c941d2d42ae.json`](../../sessions/e5/e55b93660c941d2d42ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

| 项目 | 状态 |
|------|------|
| kill 脚本 PID | **86294** |
| s0 checkpoint | 47500_chkpt（等待 50000_chkpt） |
| s2 checkpoint | 47500_chkpt（等待 50000_chkpt） |
| s0 训练 (76998) | 运行中 |
| s2 训练 (78171) | 运行中 |
| eval trigger (85512) | 运行中 |

脚本每 60 秒检查一次 50000_chkpt 是否出现，发现后等 30 秒确认写入完成再 kill 对应进程。

---
