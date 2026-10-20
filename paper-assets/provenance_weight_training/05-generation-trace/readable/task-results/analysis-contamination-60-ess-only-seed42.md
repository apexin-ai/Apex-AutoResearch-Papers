# analysis contamination 60 ess only seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_contamination_60_ess_only_seed42_20260516T031139_result.json`
- **Structured JSON:** [`97b7f0ffb2a32adbcdee.json`](../../sessions/97/97b7f0ffb2a32adbcdee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Metrics

| 指标 | 值 |
|------|-----|
| **train_loss** | 9.8424 |
| **train_runtime_seconds** | 13151.78 (≈3h38m) |
| **train_samples_per_second** | 7.425 |
| **train_steps_per_second** | 0.464 |
| **total_steps** | 6103 |
| **epoch** | 0.26 |
| **checkpoint_path** | `/root/provenance_weight_training/output/models/contamination_60_ess_only_seed42/final/` (~1.1GB model.safetensors) |

Checkpoints: `checkpoint-5500`, `checkpoint-6000`, `checkpoint-6103`, `final`

## Weighting Stats (ESS-only method)

- **ESS 目标达成**: ESS 值稳定在 ~2.0（所有 step 的 ESS 均在 2.000–2.015 范围内）
- **b\* 分布**: 范围很广，0.42–10.5，方差大——这是 ESS-only 方法特征（b* 完全由 ESS 约束驱动，无 grid/adaptive 平滑）
- **alpha_eff 分布**: 0.03–0.98，跨越全范围
- **mean_q**: 0.29–0.99
- **weighted_loss vs unweighted_loss**: weighted_loss 普遍高于 unweighted_loss（权重放大了高 provenance 样本的损失）

## eval_ppl_holdout / eval_loss_holdout

**日志中无 eval metrics。需要手动跑 eval。**

Eval 脚本存在：
- `/root/provenance_weight_training/eval_perplexity.py`
- `/root/provenance_weight_training/eval_standalone.py`
- holdout 数据：`/root/provenance_weight_training/data/human/eval_holdout.jsonl`

其他实验（uniform, grid_b0_5）已有 eval 结果 JSON，但 ess_only_seed42 尚未跑 eval。

---
