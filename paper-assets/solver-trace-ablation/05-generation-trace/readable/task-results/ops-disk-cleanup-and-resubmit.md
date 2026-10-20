# ops disk cleanup and resubmit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-and-resubmit_20260514T013754_result.json`
- **Structured JSON:** [`d8c109e3cb96bc65b01f.json`](../../sessions/d8/d8c109e3cb96bc65b01f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

1. **磁盘清理**：删除 8 个 completions 目录 + 8 个 checkpoints + 2 个失败实验目录，释放 171GB（32% → 172G 可用）
2. **脚本修复**：`log_completions=True` → `False`，不再生成 completions parquet
3. **实验提交**：plan013-r4（cuda:0）和 plan001-s43-r4（cuda:1）均已正常训练，无 completions 目录生成，磁盘稳定

---
