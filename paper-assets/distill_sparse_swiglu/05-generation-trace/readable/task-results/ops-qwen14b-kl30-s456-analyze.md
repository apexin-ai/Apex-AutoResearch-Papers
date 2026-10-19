# ops qwen14b kl30 s456 analyze

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen14b-kl30-s456-analyze_20260519T084001_result.json`
- **Structured JSON:** [`08c87b26a87ffa4f1ec2.json`](../../sessions/08/08c87b26a87ffa4f1ec2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 进程正常启动，模型已加载，正在计算 TEAL global masks。

**总结：**

| 项目 | 状态 |
|------|------|
| **qwen14b_kl30_s456 训练** | DONE (success) — loss=0.309, KL_norm=0.272, sparsity=27.7%, 1000 steps |
| **qwen14b_kl30_s456_eval** | RUNNING (PID 93278) — 7 任务 (WikiText-2 PPL + ARC/WG/HS/PIQA/MMLU/GSM8K), TEAL uniform 30%, cuda:1 |
| **Log** | `~/runs/distill_sparse_swiglu/qwen14b_kl30_s456_eval.log` |

注意：任务提供的参数名（`--predictor_path`, `--eval_tasks`, `--few_shot_config`, `--allocation_mode`）与 `benchmark_eval.py` 实际接口不符，已修正为 `--checkpoint`, `--tasks`, `--allocation`。few-shot counts 已内置于脚本 `LM_EVAL_DEFAULTS` 中。

---
