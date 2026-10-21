# ops batch status 25068 v2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_batch-status-25068-v2_20260519T224607_result.json`
- **Structured JSON:** [`fbf9bf5e32960ccd5e5c.json`](../../sessions/fb/fbf9bf5e32960ccd5e5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成。汇总：

---

## 实验状态汇总 (westd-25068)

### GPU
| GPU | 显存占用 | 利用率 | 用途 |
|-----|---------|--------|------|
| 0 | 89889 MiB | 0% | 空闲 (exp-080 已完成) |
| 1 | 90677 MiB | 96% | exp-084 运行中 |
| 2 | 89733 MiB | 100% | exp-085 运行中 |
| 3 | 90571 MiB | 0% | 空闲 |

### exp-080 Contrastive×LogiQA s42 — **DONE (negative)**
- 进程已退出，200/200 全部完成
- **contrastive_accuracy: 45.5%** vs **sc_accuracy: 50.0%** → **Δ = -4.5pp**
- wall_time: 6645.9s (~111min)
- degenerate_count: 42/200 (21%)
- Registry 已修复：原被 CRON 误标为 `failed`（"process dead 5×"），实际完整跑完。已更新 conclusion=negative + metrics

### exp-084 Debate×LogiQA s123 — **RUNNING (~8/200)**
- cuda:1, port 8001, 最近日志时间 06:46:27
- 刚启动 ~12min，进度约 4%
- Registry 修复：PREPARING → RUNNING（经过 QUEUED 中转）

### exp-085 Contrastive×LogiQA s123 — **RUNNING (~14/200)**
- cuda:2, port 8002, 最近日志时间 06:46:27
- 刚启动 ~10min，进度约 7%
- Registry 修复：PREPARING → RUNNING（同上）

### CRON 误报原因
exp-084/085 一直卡在 `PREPARING` 状态（未正确转为 RUNNING），CRON 检测进程存活时触发了 "process dead 5×" 自动 failed 逻辑。根源是提交 job 后没有走完 PREPARING → QUEUED → RUNNING 状态机。已手动修复。

---
