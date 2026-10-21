# ops 72b status and paper check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_72b_status_and_paper_check_20260522T125912_result.json`
- **Structured JSON:** [`1322789d20ee16f9b5e1.json`](../../sessions/13/1322789d20ee16f9b5e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Clean compilation. Here's the summary:

---

## Part 1: 72B 下载状态

| 指标 | 值 |
|------|-----|
| **Safetensors** | 27/37 (73%) |
| **已下载** | ~100GB / 140GB |
| **活跃下载** | shard 28 (57%), shard 33 (11%) |
| **下载速度** | ~300-350 kB/s (ModelScope, 2路并行) |
| **Watchdog v3** | PID 249737 存活，正常轮询中 |
| **推理** | 未启动（预期行为） |
| **磁盘** | 299GB/350GB used (52GB free，够用) |
| **ETA** | 剩余 ~40GB，以 ~600kB/s 合计速度算，**约 18-20 小时**（明天下午左右） |

Watchdog 运行正常，无需干预。下载完成后会自动启动 TP=4 推理。

## Part 2: 论文完整性

| 指标 | 结果 |
|------|------|
| **bib 条目总数** | 46 |
| **Orphan（在 bib 中未被引用）** | 1: `embretson2000irt` |
| **Missing（在 tex 中引用但 bib 缺失）** | 0 |
| **编译状态** | 无 warning，无 error，main.pdf up-to-date |

唯一问题：`embretson2000irt` 是 orphan entry，在 bib 中存在但未被任何 tex 文件引用。可以删除或找个地方引用它。

---
