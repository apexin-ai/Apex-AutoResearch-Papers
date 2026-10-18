# ops kill westd27271 duplicates

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-westd27271-duplicates_20260520T175127_result.json`
- **Structured JSON:** [`87cf6a5135a36fb4524e.json`](../../sessions/87/87cf6a5135a36fb4524e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**Kill 结果**：4 个进程全部清除
- pid 17634 (random prune seed43 eval k=0.7) — killed
- pid 43505 (L2 norm eval k=0.5) — killed
- pid 65532 (sweep 自动启动的下一轮 random prune k=0.5) — killed
- pid 65607 (sweep 自动启动的下一轮 L2 norm k=0.3) — killed
- 父 bash sweep 进程 (924086, 935716) 已自行退出

**当前 GPU 状态**：
| GPU | 显存占用 | 状态 |
|-----|---------|------|
| GPU 0 (A8) | 0 / 98GB | **空闲，可接新任务** |
| GPU 1 (B8) | 42GB / 98GB | M32 VTC-only 训练运行中 |

**M32 训练** (pid=921279) 确认存活，已运行 7h+。

---
