# eval lm eval kl s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_lm_eval_kl_s42_20260515T234524_result.json`
- **Structured JSON:** [`5378329faa248cc043b0.json`](../../sessions/53/5378329faa248cc043b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整评估已提交。

**总结：**
- 脚本 `/root/distill_sparse_swiglu/src/lm_eval_sparse.py` 已部署，复用 evaluate.py 的 TEAL mask 逻辑（含 per-layer mean normalization），通过 HFLM 包装传入 lm-eval
- Dry-run 验证通过：model-level sparsity=0.500，arc_challenge --limit 10 输出正常
- 完整评估 (arc_challenge, winogrande, mmlu, gsm8k) 已通过 `submit_training_job` 提交到 westd-34887 cuda:1
- Registry: `lm_eval_kl_s42` → RUNNING
- 日志：`~/runs/distill_sparse_swiglu/lm_eval_kl_s42.log`
- 结果输出：`/root/distill_sparse_swiglu/results/lm_eval_kl_s42/`

---
