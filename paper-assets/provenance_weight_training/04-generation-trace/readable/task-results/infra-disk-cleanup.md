# infra disk cleanup

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_disk_cleanup_20260514T140250_result.json`
- **Structured JSON:** [`1cc9cc4d54300978cdfc.json`](../../sessions/1c/1cc9cc4d54300978cdfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**结果：**

| 分区 | 清理前 | 清理后 |
|------|--------|--------|
| 根分区 `/` | 75% (23G/30G) | **45% (14G/30G)** |
| 数据盘 `/root/autodl-tmp` | 20% (49G/250G) | 20% (49G/250G) |

**清理内容：**
1. 9 个已完成实验的中间 checkpoint（checkpoint-6000, checkpoint-6103）— 实际在数据盘 symlink 上，释放了数据盘约 19.8G
2. `/tmp/adaptive_dryrun` — dry-run 残留，释放根分区 **9G**（根分区占满的真正原因）
3. conda 包缓存 — 释放根分区 ~107MB

所有实验的 `final/`、`config.json`、`step_metrics.jsonl` 均保留完好。RUNNING 实验未触碰。

---
