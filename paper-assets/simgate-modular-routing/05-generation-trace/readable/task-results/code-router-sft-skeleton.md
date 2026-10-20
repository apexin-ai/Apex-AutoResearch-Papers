# code router sft skeleton

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_router-sft-skeleton_20260513T183141_result.json`
- **Structured JSON:** [`60da6b762d65674977da.json`](../../sessions/60/60da6b762d65674977da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`--help` 和 `--dry_run` 均通过。

脚本已写入 `/root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py` 并验证。核心设计：

- **数据**：从 `results/plan_c/*/labeled_steps.jsonl` 加载，过滤 tie，按 task_type 分层 80/20 split
- **模型**：Qwen3-1.7B + LoRA (r=16, target q/k/v/o_proj) → 2-way sequence classification
- **Prompt**：`<|system|>...<|user|>Observation + Action history (最近5步)<|end|>`
- **评估**：per-class P/R/F1、per-task accuracy、confusion matrix → `eval_report.json`
- **输出**：LoRA adapter checkpoint + W&B logging

---
