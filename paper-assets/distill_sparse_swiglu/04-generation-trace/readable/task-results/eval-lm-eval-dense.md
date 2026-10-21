# eval lm eval dense

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_lm_eval_dense_20260515T234505_result.json`
- **Structured JSON:** [`3b31e8f6df2e6300abe6.json`](../../sessions/3b/3b31e8f6df2e6300abe6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交，运行中。

**状态汇总：**
- lm-eval 0.4.12 已安装，无需额外安装
- Dry-run 确认模型在 cuda:0 加载正常
- 完整评估已提交：tmux session `lm_eval_dense`，PID 177099，log 在 `~/runs/distill_sparse_swiglu/lm_eval_dense.log`
- 评估任务：arc_challenge, winogrande, mmlu, gsm8k
- 结果输出到 `/root/distill_sparse_swiglu/results/lm_eval_dense/`

**Registry 注意：** `lm_eval_dense` 已处于 DONE 状态（含预填 metrics），无法回退到 RUNNING。实际评估完成后需对比预填值（arc=0.5819, wino=0.7814, mmlu=0.6532, gsm8k=0.5004），确认是否一致，再决定是否更新 metrics。

---
