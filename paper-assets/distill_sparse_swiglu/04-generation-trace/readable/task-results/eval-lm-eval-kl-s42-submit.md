# eval lm eval kl s42 submit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_lm_eval_kl_s42_submit_20260515T234515_result.json`
- **Structured JSON:** [`6303b4367f6a195e5264.json`](../../sessions/63/6303b4367f6a195e5264.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交 `lm_eval_kl_s42`，状态 RUNNING。

- **服务器**: westd-34887, cuda:0
- **tmux session**: `lm_eval_kl_s42`
- **日志**: `/tmp/lm_eval_kl_s42.log`
- **命令**: `CUDA_VISIBLE_DEVICES=0 python -u src/eval_benchmark.py --condition kl_s42 --tasks lm_eval --skip_ppl --gpu 0 --batch_size 4`
- **Checkpoint**: `mvp_kl_norm_v2_s42/predictor_kl_normalized.pt`
- **评估任务**: arc_challenge, winogrande, mmlu, gsm8k

---
