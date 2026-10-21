# ops fix a025 corruption

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-a025-corruption_20260514T210319_result.json`
- **Structured JSON:** [`442600e7e7836b3e9618.json`](../../sessions/44/442600e7e7836b3e9618.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**事后分析结论：**

- `alpha_sweep_a025_s42_v2` 的 exit file 显示 exit code **137**（= 128 + 9 = **SIGKILL**），时间 21:03:38Z — 这是 v2 进程 (PID 48454) 被 kill_job 杀掉的记录
- 但 **旧进程 PID 46802**（v1，即 `alpha_sweep_a025_s42`）的 tmux session 被 kill_job 杀掉时，`kill_job` 只杀了 tmux session，子进程 PID 46802 逃脱了 — 这是已知问题：**kill_job 通过 `tmux kill-session` 杀 session，但 python 子进程如果已 detach（orphaned）就不受影响**
- 根因：v1 被 kill_job 处理时，tmux session 被销毁，但 python 进程（PID 46802）变成了孤儿进程继续运行，与后来启动的 v2 (PID 48454) 同时写入同一 output_dir

---

### 执行总结

| Step | 状态 |
|------|------|
| Kill PID 46802 & 48454 | ALL_DEAD |
| 删除损坏数据 a025_s42/ | CLEAN |
| 重启 v3 | PID 53069/53074, cuda:1, 单进程确认 |
| Registry v2 | conclusion=failed, failure_reason 已记录 |
| Registry v3 | spec 已写入 |
| a000_s42 | 运行中, Gen 5/10, PID 46716 |
| 事后分析 | kill_job 用了 SIGKILL(137)，但只杀 tmux session，旧 python 子进程逃脱成孤儿进程导致数据损坏 |

---
