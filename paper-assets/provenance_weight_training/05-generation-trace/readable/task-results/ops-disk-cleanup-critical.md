# ops disk cleanup critical

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_critical_20260524T164353_result.json`
- **Structured JSON:** [`e8a34b000c7e6de55ec0.json`](../../sessions/e8/e8a34b000c7e6de55ec0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**释放空间**：删除 29 个 checkpoint 目录，释放约 **85GB**（多数为 3.4GB 的 Qwen checkpoint + 少量 1.2G 的 GPT-2 checkpoint）。

**当前磁盘**：
```
/dev/md0  250G  140G  111G  56%  /root/autodl-tmp
```
从 100% 降到 56%，有 111GB 可用。

**random_subset_epoch_seed42 状态**：
- tmux session 存活 ✓
- GPU 0: 100% utilization, 74127 MiB VRAM 占用 ✓
- 当前 step: **3999**（日志最后记录），训练正常进行中

---
