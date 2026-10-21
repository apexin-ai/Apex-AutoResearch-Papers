# ops check permuted score exit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_permuted_score_exit_20260524T164313_result.json`
- **Structured JSON:** [`9225fd8abcf7d320efeb.json`](../../sessions/92/9225fd8abcf7d320efeb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能在之前的 session 中已被清理或过期）。

**总结：**

- **退出原因**：磁盘满（`OSError: [Errno 28] No space left on device`），在 step 500/6103 保存 checkpoint 时崩溃
- **Registry 状态**：已标记 `DONE/failed`（之前已更新）
- **τ=0.7 重启版**：服务器上没有对应的 tmux 会话，尚未启动
- **Cron**：当前 session 无该 cron，无需删除

---
