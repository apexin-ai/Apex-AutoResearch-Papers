# ssh d049 kill orphan 128666

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d049-kill-orphan-128666_20260513T092519_result.json`
- **Structured JSON:** [`9e004dba918d59126cb8.json`](../../sessions/9e/9e004dba918d59126cb8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**汇报：**

1. **PID 128666** — 已 kill（普通 SIGTERM 即成功，无需 SIGKILL）
2. **Checkpoint** — `/root/autodl-tmp/checkpoints_repo_cwm_seed123/` 已删除
3. **cuda:2 进程** — 仅剩 PID 130031（CWM v11 子进程），占用 13466 MiB，孤儿进程已清除
4. **CWM v11 状态** — PID 130026 存活，已运行 1h05m34s，GPU 利用率 97%，显存 13475/32607 MiB（释放了约 19GB，比预期还多）

cuda:2 已干净，CWM v11 正常运行。

---
