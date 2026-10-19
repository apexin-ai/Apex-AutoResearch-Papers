# ops d062 data verify and watcher check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d062_data_verify_and_watcher_check_20260516T093518_result.json`
- **Structured JSON:** [`6c738c9af5e9d066a993.json`](../../sessions/6c/6c738c9af5e9d066a993.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Part 1: D062 [1/14] 数据完整性

**JSON 有效。** 第一次 d062 eval (PID 155973) 在 [1/14] 的 300/504 处 ERROR，但已有一个重试进程 (PID 158652, `/tmp/d062_eval.log`) 成功重跑了 [1/14] 全部 504 query。

**`selection_random_s42_best_by_val_loss.json`:**
- total: 504 ✓ (完整)
- R@1=0.2302, R@5=0.625, R@10=0.8016

**`selection_random_s42_best_by_recall_at_1.json`:**
- total: 504 ✓ (完整)
- R@1=0.2302, R@5=0.625, R@10=0.8016

**两个 JSON 不完全相同** — metrics 数值一致，但 `ckpt_dir` 字段不同（分别指向 `best_by_val_loss` 和 `best_by_recall_at_1`）。说明 random_s42 的两个 checkpoint 在 selection set 上表现完全一致（可能最优 val_loss 和最优 recall@1 出现在同一 step）。

**当前进度：2/14 完成**，[3/14] (`random_s43_best_by_val_loss`) 正在跑（PID 164287, 已运行 ~45min）。

---

### Part 2: Qwen Watcher 状态

**PID 966920 存活** — 已运行 1d18h，进程为 `bash /root/structfuse/watch_and_chain_qwen_s42.sh`。

Qwen 主链当前状态：
- PID 134885: 正在训练 `dataflow_aware_s44`（已跑 ~6h41m），这是 Qwen 主链最后一批 subrun 之一
- 主链跑完 dataflow_aware_s44 后 watcher 应会触发 embed_s42 + dataflow_s42 + bm25_s42

无需干预，两条线都在正常推进。

---
