# ssh exp009 incremental write fix

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp009_incremental_write_fix_20260522T010329_result.json`
- **Structured JSON:** [`c02080c79028c05fed33.json`](../../sessions/c0/c02080c79028c05fed33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程 PID=112923 已在 GPU 0 上运行。等 ~4.5 分钟后检查 CSV 增量写入是否成功。

**已完成的改动摘要：**

| 位置 | 原代码 | 改为 |
|------|--------|------|
| L4 docstring | `x 100 seeds` | `x 50 seeds` |
| L208 Part A flush | 每 5 pairs 写一次 (`len(buf) >= 10`) | 每个 pair 立即写入 |
| L354 Part B flush | 每 5 seeds 写一次 (`(i+1) % 5 == 0`) | 每个 seed 立即写入 |

断点续跑逻辑（`_completed_pairs_a` / `_completed_seeds_b`）原本已有，无需修改。核心问题只是 flush 粒度太粗，崩溃时最多丢 5 个 seed 的结果。现在改为每完成一个就 flush，最多丢当前正在跑的那个。

---
