# ops locate c1 checkpoint run eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_locate-c1-checkpoint-run-eval_20260519T002933_result.json`
- **Structured JSON:** [`cba36bedb194d9ec7277.json`](../../sessions/cb/cba36bedb194d9ec7277.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

- **Checkpoint 位置**：westd-34887，`/root/distill_sparse_swiglu/checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt`（152MB）。westd-41718 目录为空。
- **41718 eval 状态**：已失败（`FileNotFoundError`，找不到 checkpoint）。
- **34887 eval 状态**：已在 cuda:1 成功启动（nohup），正常运行中：
  - WikiText-2 PPL = **9.4463** (已完成)
  - arc_challenge 25-shot 评估中，当前进度 ~29%（345/1172），速度 ~47 it/s
  - 后续还有 winogrande, mmlu, gsm8k
  - 全部跑完预计还需 30-40 分钟
- **exp_id**: `c1_ablation_30pct_s42_eval`，日志在 `/root/runs/distill_sparse_swiglu/c1_ablation_30pct_s42_eval_34887.log`

---
