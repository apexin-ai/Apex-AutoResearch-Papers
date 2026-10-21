# analysis rho02 tau08 log

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rho02_tau08_log_20260517T223731_result.json`
- **Structured JSON:** [`d9fb00292a56c636d48d.json`](../../sessions/d9/d9fb00292a56c636d48d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。结果汇总：

## rho02_adaptive_tau08_seed42 实验结果

### 训练指标
| 指标 | 值 |
|------|-----|
| train_loss (HF avg) | 11.68 |
| total_steps | 6103 |
| train_runtime | 14598.9s (4h03m) |
| epoch | 0.47 |

### Eval Holdout 指标
| 指标 | �� |
|------|-----|
| **eval_ppl_holdout** | **17.382** |
| **eval_loss_holdout** | **2.8555** |
| eval_holdout_tokens | 4,077,068 |
| eval_elapsed | 193.2s |

### Weighting 统计 (训练末期 step 6100-6102)
- τ_batch = 0.8 (固定)
- b* 分布：约 40-50% batch 中 b=0（uniform fallback），其余 b∈[0.2, 15.6]
- alpha_eff 多数在 0.7-0.8 区间
- ESS 在 2.0-4.0 之间波动（b=0 时 ESS=4 即全 batch）

### 与基准对比
| 实验 | PPL | 结论 |
|------|-----|------|
| rho02_uniform_seed42 | 17.336 | baseline |
| **rho02_adaptive_tau08_seed42** | **17.382** | +0.046, 略差于 uniform |
| rho02_adaptive_tau09_r5 | 17.450 | τ=0.9 负面 |

### 结论

**τ=0.8 的 PPL (17.382) > uniform baseline (17.336)**，差距 +0.046。虽然比 τ=0.9 (17.45) 好，但仍未能超越 uniform baseline。Claim 3 在 ρ=0.2 条件下暂不成立——adaptive weighting 在低污染率下未带来增益。

---
