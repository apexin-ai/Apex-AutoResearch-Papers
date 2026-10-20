# ops disk cleanup westd39279

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-westd39279_20260514T053423_result.json`
- **Structured JSON:** [`982c45f5e0444f0640f1.json`](../../sessions/98/982c45f5e0444f0640f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

释放成功。磁盘从 6.4G → **172G 可用**（释放约 165G）。

### 剩余空间分布

| 路径 | 大小 |
|------|------|
| `/root/autodl-tmp/outputs/` | 61G（5个目录） |
| └ grpo_exec_only | 15G |
| └ grpo_exec_sta | 15G |
| └ plan001_exec_only_s42 | 15G |
| └ plan005_sta_low_s42 | 15G |
| └ plan002_additive_b01_s42 | 4K（空） |
| `/root/autodl-tmp/models/` | 16G |
| `/root/autodl-tmp/gpt2-small/` | 526M |
| **总使用** | **79G / 250G** |

172G 空闲，足够跑多轮 1000 步实验。

---
