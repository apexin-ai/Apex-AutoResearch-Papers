# exp bce ste s42 collect and eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_bce_ste_s42_collect_and_eval_20260520T115723_result.json`
- **Structured JSON:** [`92e935120e7862c73257.json`](../../sessions/92/92e935120e7862c73257.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

**BCE+STE 训练 (westd-41718)** — 已完成
- 最终: loss=0.6410, bce=0.6398, reg=0.0012, sparsity=0.512
- 1000 步, 1045s, 1.05s/step
- Checkpoint: `/root/distill_sparse_swiglu/checkpoints/bce_ste_s42/predictor_bce.pt` (145MB)

**BCE+STE Eval (westd-41718:cuda:0)** — 运行中 (PID 249688)
- WikiText-2 PPL = **60.54** ✓
- arc_challenge (25-shot) ✓ (3m36s)
- 当前: winogrande + mmlu (5-shot) 进行中
- 待跑: gsm8k, hellaswag, piqa
- 预计还需 ~15-20 分钟

**40% Global Eval v2 (westd-34887:cuda:0)** — 运行中 (PID 205789)
- 当前 batch: 84% (33833/40168), ~26 it/s
- 该 batch 约 4 分钟完成，但后续可能还有更多 tasks

两个 eval 都在跑，无需干预。要等结果出来还是先做别的？

---
