# ops fix m2 qwen restart

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_m2_qwen_restart_20260513T171748_result.json`
- **Structured JSON:** [`697db0efa193ba426e1f.json`](../../sessions/69/697db0efa193ba426e1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果汇报

### 三项验证：❌ 失败

| 验证项 | 结果 | 详情 |
|--------|------|------|
| PID 71387 kill | ✅ KILLED | 进程已终止 |
| tmux m2_qwen | ❌ TMUX_DEAD | 脚本不存在导致 session 退出 |
| GPU cuda:0 训练进程 | ❌ 无进程 | cuda:0 上没有训练进程 |
| 日志内容 | ❌ 脚本缺失 | `bash: scripts/run_m2_full_qwen.sh: No such file or directory` |
| cuda:1 StarCoder | ✅ 未受影响 | PID 72399 在 GPU 1 上运行，11426 MiB，正常 |

### 失败原因

`/root/structfuse/scripts/run_m2_full_qwen.sh` **不存在**。scripts 目录下实际可用的相关脚本：
- `run_full_m2_training.sh` — 最可能是对应脚本
- `run_m2_pilot.sh`
- `schedule_m2_runs.sh`

按指示，不自行修复。请确认应使用哪个脚本重启训练。

---
