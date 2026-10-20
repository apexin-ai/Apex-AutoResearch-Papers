# train ablation lf holdout v2

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_ablation-lf-holdout-v2_20260514T143516_result.json`
- **Structured JSON:** [`5bdea7f8feada164bdba.json`](../../sessions/5b/5bdea7f8feada164bdba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交。

- **exp_id**: `ablation-lf-holdout-v2`
- **PID**: 61243
- **GPU**: cuda:1
- **日志**: `~/runs/agent_progress_probe/ablation-lf-holdout-v2.log`

三个变体（no_cmd_rep → no_file_diff → no_ob）串行跑，预计 15-20 分钟完成。结果汇总写入 `lf_holdout_results.json`，每个变体的 checkpoint 分别保存在 `checkpoints_holdout_no_cmd_rep/`、`checkpoints_holdout_no_file_diff/`、`checkpoints_holdout_no_ob/`。

---
