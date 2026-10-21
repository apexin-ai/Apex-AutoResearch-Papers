# collect grid b seed42 eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_grid_b_seed42_eval_20260514T171714_result.json`
- **Structured JSON:** [`e4c9b983633dffe6f9e7.json`](../../sessions/e4/e4c9b983633dffe6f9e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

b=3.0 at step 4242/6103 (70%). Here's the full summary:

## Grid-b seed42 eval_ppl_holdout

| b | eval_ppl_holdout | eval_loss | 状态 | 备注 |
|---|---|---|---|---|
| 0.5 | **17.651** | 2.8708 | 完成 | |
| 1.0 | 17.692 | 2.8731 | 完成 | |
| 1.5 | 17.718 | 2.8746 | 完成 | |
| 2.0 | 17.741 | 2.8759 | 完成 | |
| 3.0 | — | — | 训练中 | step 4242/6103 (70%), 预计还需 ~66 min |
| 5.0 | — | — | 未开始 | 排在 b=3.0 后面串行 |

**Best-b (目前): b=0.5, PPL=17.651**

PPL 随 b 单调递增（0.5 → 2.0），趋势明显。

### eval_data_path 检查
- 训练脚本 `run_grid_b_seed42.sh` **未用** `--eval_data_path`（训练期间无 eval）
- 所有 eval 由 `auto_eval_watcher.py` 自动执行，使用 `data/human/eval_holdout.jsonl` ✓
- b=3.0 和 b=5.0 训练完成后会被 watcher 自动 eval，无需手动补跑

---
