# analysis kl sparsity30 s42 v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kl_sparsity30_s42_v2_20260515T210900_result.json`
- **Structured JSON:** [`b877539ef79f62cce8e9.json`](../../sessions/b8/b877539ef79f62cce8e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。

## kl_sparsity30_s42_v2 训练结果分析

### Conclusion: **success** (训练完成，sparsity 收敛；但缺少 eval PPL 数据)

### 关键指标

| 指标 | 值 |
|------|-----|
| 最终 loss | 0.1465 |
| 最终 kl_norm | 0.1465 |
| 最终 sparsity | **0.281** (target=0.30, margin=0.02, 在可接受范围 [0.28, 0.32] 内) |
| 最终 lambda | 1000.00 (已达 cap) |
| 最终 tau | 0.100 |
| constraint | 0.000 (收敛) |
| 训练步数 | 1000/1000 |
| 训练时间 | ~36 min (04:30 → 05:06) |
| trainable params | 75.96M / 8.03B (0.946%) |
| checkpoint | `/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s42/predictor_kl_normalized.pt` (145MB) |
| log | `~/runs/distill_sparse_swiglu/kl_sparsity30_s42_v2.log` |
| W&B | offline mode, run ID `i1rrewz9`，无法远程查询 |
| warnings/errors | 无（`use_cache=True` 兼容性提示为正常行为） |

### Sparsity 收敛轨迹

```
Step   1: 0.406 (初始高 sparsity)
Step 100: 0.348 (逐步下降)
Step 130: 0.289 (进入目标附近)
Step 150: 0.258 (过冲, lambda spike → 327.68)
Step 160: 0.324 (反弹)
Step 270: 0.270 (再次过冲, lambda → 500 → 1000)
Step 330+: 0.281-0.293 稳定震荡, lambda 饱和在 1000
Step 1000: 0.281
```

### Lambda 行为

Lambda 在训练中段经历剧烈震荡：从 0.01 快速增长到 327.68（step 150），经多次 growth/decay 循环后，~step 330 饱和在 cap=1000 并保持至训练结束。Lambda 饱和说明 Lagrangian 机制尝试推高 sparsity 但模型倾向于更低的 sparsity（~0.281），cap 阻止了进一步推高。实际收敛值（0.281）在 margin 内，训练是稳定的。

### 缺失数据

**没有 eval PPL 数据。** 训练脚本未包含自动评估，checkpoint 目录下也无 eval 日志。无法直接与 50% baseline 对比以下指标：
- eval/true_dense_ppl
- eval/predictor_hard_mask_ppl
- eval/teal_sparse_ppl

### 与 50% baseline 初步对比

| | 30% (本次) | 50% (plan_001 baseline) |
|---|---|---|
| target sparsity | 0.30 | 0.50 |
| actual sparsity | 0.281 | 0.498 |
| final train loss | 0.1465 | — |
| predictor_hard_mask_ppl | **需要 eval** | 9.15 |
| teal_sparse_ppl | **需要 eval** | 11.99 |

### 对 plan_008 sparsity sweep 的判断

训练成功收敛，但**必须先跑 eval 才能出有意义的结论**。预期 30% sparsity（保留 70% 神经元）的 PPL 应显著优于 50% sparsity baseline。建议下一步：用保存的 checkpoint 跑 eval 脚本，获取 true_dense_ppl / predictor_hard_mask_ppl / teal_sparse_ppl 三项指标。

---
