# ops fix gpu1 duplicate

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-gpu1-duplicate_20260516T025759_result.json`
- **Structured JSON:** [`7d9df05869d495aeba25.json`](../../sessions/7d/7d9df05869d495aeba25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**操作完成，汇总：**

| 项目 | 结果 |
|------|------|
| PID 726977 (旧) | 已 kill，SIGTERM 成功 |
| Checkpoint 完整性 | output_dir 仅有 `config.json`，无 checkpoint，无损坏 |
| PID 728887 (新) | 继续运行，GPU 1 占用 16256 MiB |

GPU 1 当前两个进程：
- **PID 708166** — 6601 MiB（其他实验）
- **PID 728887** — 16256 MiB（v5_div_reg_seed2，正常运行中）

旧进程已清理，728887 无 checkpoint 冲突，正常继续训练。

---
