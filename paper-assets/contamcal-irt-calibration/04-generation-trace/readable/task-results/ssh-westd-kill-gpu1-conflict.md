# ssh westd kill gpu1 conflict

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-kill-gpu1-conflict_20260519T122906_result.json`
- **Structured JSON:** [`7f8b8f39eac1fe95f811.json`](../../sessions/7f/7f8b8f39eac1fe95f811.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

- **GPU 1 已释放**：0MiB 显存，无进程
- **d050 输出目录为空**（GPU 1 的 d050 刚启动，未写入数据，无污染）
- **GPU 3** (PID 169634) 继续独占跑 d050，不受影响
- **GPU 0** (PID 168549) 在跑 d005，正常
- **d025 结果完整**（`.done` 标记存在，5 个文件齐全）

---
