# fix backup 25k chkpt

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_backup_25k_chkpt_20260528T021428_result.json`
- **Structured JSON:** [`f469ae701084e0fcf290.json`](../../sessions/f4/f469ae701084e0fcf290.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

| 项目 | 结果 |
|------|------|
| Backup 大小 | **15G** |
| Watch 脚本 PID | **48594** |
| 原始 25000_chkpt | 存在 |
| Backup | 存在 |
| 训练进程 47162 | 运行中 |

Watch 脚本每 30 秒检查一次，若 25000_chkpt 被轮转删除会自动从 backup 恢复，训练结束后自动退出。

---
