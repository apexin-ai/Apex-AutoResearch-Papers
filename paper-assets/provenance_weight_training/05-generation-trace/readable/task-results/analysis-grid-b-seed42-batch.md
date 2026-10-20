# analysis grid b seed42 batch

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grid_b_seed42_batch_20260514T220645_result.json`
- **Structured JSON:** [`8d9420dbd9a99b0dc209.json`](../../sessions/8d/8d9420dbd9a99b0dc209.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 6 个 final checkpoint 确认存在。日志中无 eval_ppl，因为脚本未传 `--eval_data_path`。

## grid_b_seed42_batch 实验结果

| b | train_loss | train_runtime_s | eval_ppl_holdout | checkpoint_path |
|---|-----------|----------------|-----------------|----------------|
| 0.5 | 9.598 | 13,036 | **缺失** | `output/models/grid_b0_5_seed42/final/` |
| 1.0 | 10.223 | 12,968 | **缺失** | `output/models/grid_b1_0_seed42/final/` |
| 1.5 | 10.485 | 14,789 | **缺失** | `output/models/grid_b1_5_seed42/final/` |
| 2.0 | 10.621 | 13,034 | **缺失** | `output/models/grid_b2_0_seed42/final/` |
| 3.0 | 10.754 | 13,036 | **缺失** | `output/models/grid_b3_0_seed42/final/` |
| 5.0 | 10.858 | 13,115 | **缺失** | `output/models/grid_b5_0_seed42/final/` |

### 关键发现

1. **全部 6 个 b 值缺失 eval_ppl_holdout** — `run_grid_b_seed42.sh` 没有传 `--eval_data_path` 和 `--eval_steps` 参数，训练过程中未执行 evaluation。需要单独跑 eval 才能获得 holdout perplexity。

2. **train_loss 随 b 递增** — 符合预期：b 越大，高质量数据权重越高，weighted loss 越大（因为惩罚低质量样本更重）。

3. **b=1.5 训练时间异常偏长**（14,789s vs 其他 ~13,000s），可能是 I/O 波动或 GPU throttling。

4. **与 seed123 对比**：seed123 的 eval_ppl 在 b=0.5 时最优（17.638 vs uniform 17.69）。seed42 需要补跑 eval 才能对比。

### 下一步
需要对 6 个 final checkpoint 跑 holdout eval 以获得 eval_ppl_holdout，才能与 uniform_seed42（17.69）和 seed123 结果做有效对比。

---
