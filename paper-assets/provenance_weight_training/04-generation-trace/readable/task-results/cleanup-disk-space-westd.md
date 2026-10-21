# cleanup disk space westd

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_disk_space_westd_20260523T031637_result.json`
- **Structured JSON:** [`6e8107dc3c26a5031a1d.json`](../../sessions/6e/6e8107dc3c26a5031a1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**结果汇总：**
- 释放空间：**~97G**（250G → 153G，可用 98G，使用率 62%）
- 删除内容：9 个已完成实验的 27 个中间 checkpoint + 1 个损坏 checkpoint + 2 个可弃 checkpoint
- **保留完好：** 4 个崩溃实验的恢复 checkpoint 全部在位：
  - rho03_adaptive_seed456/checkpoint-1000 ✓
  - rho03_uniform_seed456/checkpoint-1000 ✓
  - bs8_nmin4_adaptive_seed123/checkpoint-{500,1000} ✓
  - bs8_nmin4_uniform_seed123/checkpoint-{500,1000} ✓
- 所有 final 目录未触及

磁盘现在有 **98G 可用**，可以重启训练。

---
