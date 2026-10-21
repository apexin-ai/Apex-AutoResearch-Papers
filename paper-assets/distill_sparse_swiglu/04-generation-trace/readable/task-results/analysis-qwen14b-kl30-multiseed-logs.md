# analysis qwen14b kl30 multiseed logs

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b_kl30_multiseed_logs_20260519T084025_result.json`
- **Structured JSON:** [`bc1565541fa2f77720c8.json`](../../sessions/bc/bc1565541fa2f77720c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

以下是结果汇总。

## 训练状态

两个 seed 均**正常完成**（1000/1000 步, EXIT_CODE=0, checkpoint 已保存）。

## 训练日志指标

| 指标 | s42 (参考) | s123 | s456 |
|---|---|---|---|
| steps | 1000 | 1000 | 1000 |
| final_loss (step 1000) | 0.3398 | 0.3633 | 0.3086 |
| kl_norm (step 1000) | — | 0.3262 | 0.2715 |
| training_sparsity (稳定值) | 0.281 | 0.281 | 0.281 |
| sparsity (step 1000) | — | 0.277 | 0.277 |
| lambda | 5000.00 | 5000.00 | 5000.00 |
| tau (final) | 0.100 | 0.100 | 0.100 |
| EXIT_CODE | 0 | 0 | 0 |

## Checkpoints

| Seed | 路径 | 大小 |
|---|---|---|
| s123 | `checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt` | 224M (234,191,583 bytes) |
| s456 | `checkpoints/qwen14b_kl30_s456/predictor_kl_normalized.pt` | 224M (234,191,583 bytes) |

## PPL Eval 状态：未完成

**s123 和 s456 的 PPL eval 均未成功运行：**
- `qwen14b_kl30_s123_eval.log`: 空文件（0 行），eval 脚本缺少 `--exp_id` 参数失败
- `qwen14b_kl30_s456_eval.log`: 只到模型加载和 WikiText-2 开始就中断了（使用了 `allocation=uniform`），未产出结果

以下指标**无法从现有日志提取**，需要重新跑 eval：
- dense_ppl
- predictor_hard_mask_ppl
- teal_global_ppl
- ppl_ratio_hard_mask
- ppl_ratio_teal

## 现有 qwen14b s42 eval 参考

已有的 s42 benchmark 结果（`results/benchmark/qwen14b_kl30_s42/results.json`）：
- wikitext2_ppl (KL predictor, global_topk): **7.6232**
- ARC-C acc_norm: 0.5717, WinoGrande: 0.7206, MMLU: 0.6372, GSM8K: 0.4882

需要为 s123 和 s456 运行对应的 PPL eval 和 benchmark eval 来完成三 seed 对比表。

---
