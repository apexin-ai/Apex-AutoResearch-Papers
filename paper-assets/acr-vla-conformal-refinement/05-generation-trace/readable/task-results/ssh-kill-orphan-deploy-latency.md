# ssh kill orphan deploy latency

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-orphan-deploy-latency_20260520T055922_result.json`
- **Structured JSON:** [`18f6093c5d4c1a62c444.json`](../../sessions/18/18f6093c5d4c1a62c444.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`profile_latency.py` 不存在——本地和远程都没有这个脚本。

**汇报：**

| 步骤 | 结果 |
|------|------|
| Kill 孤儿进程 | 成功。PID 660279 (`calibrate_crm_signal.py`) 已终止，GPU 0 完全释放 (0 MiB, 0%) |
| 部署 Latency Profiling | **失败**。`src/profile_latency.py` 在服务器和本地项目中均不存在 |

需要先创建 `profile_latency.py` 脚本，或者指定正确的脚本路径。请确认脚本来源。

---
