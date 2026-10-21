# diag check mistral ckpt

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_check_mistral_ckpt_20260525T091900_result.json`
- **Structured JSON:** [`23233f1ff749ab263336.json`](../../sessions/23/23233f1ff749ab263336.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

### Mistral 模型

**Base 模型**: `/root/autodl-tmp/models/mistral-7b/` (Mistral-7B, 3 shard safetensors)

**Checkpoints** (distilled):
| 路径 | 说明 |
|------|------|
| `checkpoints/mistral_kl_s42` | KL (默认 sparsity), seed 42 |
| `checkpoints/mistral_kl30_s42` | KL 30%, seed 42 |
| `checkpoints/mistral_kl30_s123` | KL 30%, seed 123 |
| `checkpoints/mistral_kl30_s456` | KL 30%, seed 456 |
| `checkpoints/mistral_kl70_s42` | KL 70%, seed 42 |

### Qwen 14B Checkpoints

| Checkpoint | 说明 |
|-----------|------|
| `qwen14b_kl30_s42` | KL 30%, seed 42 |
| `qwen14b_kl30_s123` | KL 30%, seed 123 |
| `qwen14b_kl30_s456` | KL 30%, seed 456 |
| `qwen14b_bce30_s42` | BCE 30%, seed 42 |

**Qwen14b boolq 结果: 不存在。** 没有任何 `*qwen14b*boolq*` 的 benchmark 结果文件。

### benchmark_eval.py 支持的 tasks

| Task | num_fewshot |
|------|------------|
| arc_challenge | 25 |
| winogrande | 5 |
| mmlu | 5 |
| gsm8k | 8 |
| hellaswag | 10 |
| piqa | 0 |
| **boolq** | **0** |
| longbench (+ 各子集) | 0 |

### 推荐 cuda:1 任务

Qwen14b boolq 结果完全缺失，且 `benchmark_eval.py` 已支持 boolq (0-shot)。建议在 cuda:1 上跑 Qwen14b KL 30% 三个 seed (s42/s123/s456) 的 boolq eval。Qwen14b 约 14B 参数，单卡能跑 inference (不需要训练)。如果同时要补 Mistral，可以串行排在后面——Mistral 7B 更小更快。

---
