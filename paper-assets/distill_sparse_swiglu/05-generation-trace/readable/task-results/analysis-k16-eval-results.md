# analysis k16 eval results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k16_eval_results_20260523T132639_result.json`
- **Structured JSON:** [`22993b205f3ad09f8925.json`](../../sessions/22/22993b205f3ad09f8925.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I can see the task pipeline. Both have completed arc_challenge, winogrande+mmlu, gsm8k, and are currently running hellaswag (10042×4 = 40168 loglikelihood requests). After hellaswag, piqa and wikitext2 remain.

## K=16 s123 eval
状态: **RUNNING**
当前: hellaswag — 24% (9681/40168), ~20.75 it/s
已完成: arc_challenge, winogrande+mmlu, gsm8k
待运行: piqa (~3 min), wikitext2 (~5-10 min)
预计剩余: **~35 min**

## K=16 s456 eval
状态: **RUNNING**
当前: hellaswag — 16% (6601/40168), ~19.48 it/s
已完成: arc_challenge, winogrande+mmlu, gsm8k
待运行: piqa (~3 min), wikitext2 (~5-10 min)
预计剩余: **~40 min**

---
