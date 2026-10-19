# infra prep bce v3 s42 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_prep_bce_v3_s42_eval_20260518T010609_result.json`
- **Structured JSON:** [`e478ceb6bfd3674ccd10.json`](../../sessions/e4/e478ceb6bfd3674ccd10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 项检查通过：

| 检查项 | 状态 |
|--------|------|
| checkpoint 存在 | `predictor_bce.pt` 145MB, 2026-05-16 13:25 |
| benchmark_eval import | OK |
| wikitext 缓存 | OK |
| arc_challenge 缓存 | OK (`allenai___ai2_arc`) |
| winogrande 缓存 | OK (`allenai___winogrande`) |
| mmlu 缓存 | OK (`cais___mmlu`) |
| gsm8k 缓存 | OK (`openai___gsm8k`) |

**就绪的提交命令：**

```bash
cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id bce_isocompute_v3_s42 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/bce_isocompute_v3_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0
```

按 C002 约束，实际提交时需用 `nohup` 包裹并重定向日志。等 14B eval 跑完释放 cuda:0 后即可提交。

---
