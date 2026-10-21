# ops auto eval watcher

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_auto-eval-watcher_20260514T073513_result.json`
- **Structured JSON:** [`1ec7772595773092caf1.json`](../../sessions/1e/1ec7772595773092caf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Watcher 工作正常：

- **grid_b0_5_seed42** eval 完成：loss=2.8708, perplexity=17.65 (166s)
- **grid_b1_0_seed42** eval 已自动开始

Watcher 会持续在后台运行，每 60s 扫描新 checkpoint。后续 b=1.5/2.0/3.0/5.0 (seed42) 和 b=0.5/1.0/1.5 (seed123) 训练完成后会自动触发 eval，结果保存到 `output/eval_results/{exp_id}_eval.json`。

---
