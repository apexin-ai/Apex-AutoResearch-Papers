# infra fix and launch

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix-and-launch_20260514T072932_result.json`
- **Structured JSON:** [`e88228499042b50a7d06.json`](../../sessions/e8/e88228499042b50a7d06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 汇报

| 项目 | 状态 |
|------|------|
| **Perplexity padding 修复** | 已应用。`labels = input_ids.clone()`, `labels[attention_mask == 0] = -100`, `labels=labels` 三处确认存在（行 233-238） |
| **verify_gen01 清理** | 已删除。`results/mvp/` 下剩余：`rep_42_v1_partial`, `rep_43_v1_partial`（历史残留） |
| **GPU** | 空闲，无计算进程 |
| **残留进程** | 无 iterative_train 进程 |
| **磁盘** | `/root/autodl-tmp/` 250G 可用 245G（使用 3%），充足 |

服务器就绪，可启动全量实验。`results/mvp/` 下有两个 partial 目录，如需一并清理请告知。

---
