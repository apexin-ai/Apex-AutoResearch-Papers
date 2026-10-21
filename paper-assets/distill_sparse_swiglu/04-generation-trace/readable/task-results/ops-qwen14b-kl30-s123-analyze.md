# ops qwen14b kl30 s123 analyze

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen14b-kl30-s123-analyze_20260519T083954_result.json`
- **Structured JSON:** [`8b8d2d43d1cb1887c666.json`](../../sessions/8b/8b8d2d43d1cb1887c666.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**训练结果 (qwen14b_kl30_s123)**
| Metric | Value |
|---|---|
| Final KL loss | 0.326 |
| Sparsity | 0.277 (target 0.30) |
| Constraint | 0.037 |
| Lambda | 5000 (hit cap) |
| Steps | 1000/1000 |
| Trainable params | 117M (0.793%) |
| Checkpoint | 224MB, saved successfully |

**Benchmark eval (qwen14b_kl30_s123_eval)** 已提交：
- PID: 93137, westd-34887 cuda:0
- Mode: `teal_global`, allocation: `uniform`, sparsity: 0.3
- Tasks: wikitext2, arc_challenge, winogrande, hellaswag, piqa, mmlu, gsm8k
- Log: `~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval.log`
- Registry 状态: RUNNING

注意：任务描述中的 `benchmark_eval.py` 参数与实际脚本接口不一致，已按实际接口修正（`--checkpoint` / `--tasks` / `--exp_id` / `--allocation uniform` / `--sparsity_mode teal_global`）。few-shot 配置使用脚本内置默认值，与指定值一致。

---
