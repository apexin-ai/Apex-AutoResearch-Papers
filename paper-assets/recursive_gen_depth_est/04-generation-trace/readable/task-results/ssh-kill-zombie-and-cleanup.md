# ssh kill zombie and cleanup

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_zombie_and_cleanup_20260514T224136_result.json`
- **Structured JSON:** [`9879e6c5301f537aa47c.json`](../../sessions/98/9879e6c5301f537aa47c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无 tmux sessions 需要清理。

---

**清理结果汇总：**

| 项目 | 结果 |
|------|------|
| PID 193689 (dcol_deberta_001 子进程) | 已 kill -9，显存释放 |
| PID 208941 (gpt2xl_temp09 extract_features) | kill 前已自行退出 |
| PID 210106 (dcol_deberta_002) | 确认已死（OOM 崩溃） |
| cuda:0 显存 | **0 MiB / 97887 MiB** — 完全释放 |
| cuda:1 | 207537 (olmo_temp09) 占 9964 MiB，正常运行中 |
| tmux sessions | 无残留 session |

cuda:0 已完全可用。

---
