# ops cqa1 disk emergency cleanup

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-disk-emergency-cleanup_20260513T090139_result.json`
- **Structured JSON:** [`e8c48c30f04b1a396f81.json`](../../sessions/e8/e8c48c30f04b1a396f81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| 步骤 | 操作 | 释放空间 |
|------|------|---------|
| Step 1 | 删除 checkpoints/models/m2_*_data/ | **~14.6 GB** |
| Step 2 | 清理 9 个已完成 repo 克隆 + codeql_db | **~19.7 GB** |
| **合计** | | **~34.3 GB** |

**最终磁盘状态**: 127GB used / 43GB free（75%），从 95% → 75%

| 项目 | 状态 |
|------|------|
| m1_repos/ | 314MB（新 repo 正在被克隆） |
| m1_extraction/ | 5.6GB 产出数据 |
| M1 提取进程 577864 | 存活，已运行 12h15m |
| 自动清理守护进程 580662 | 存活，每 10 分钟清理已完成 repo |

---
