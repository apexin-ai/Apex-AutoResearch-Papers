# analysis detect remove baseline seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_detect_remove_baseline_seed42_20260516T052102_result.json`
- **Structured JSON:** [`2873c871182720ec81fe.json`](../../sessions/28/2873c871182720ec81fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

---

## detect_remove_baseline_seed42 结果汇总

| 指标 | 值 |
|------|-----|
| train_loss | 11.003 |
| total_steps | 6,103 |
| train_runtime | 13,248s (~3h 41m) |
| **eval_ppl_holdout** | **17.29** |
| eval_loss_holdout | 2.8499 |
| eval_holdout_tokens | 4,077,068 |
| checkpoint | `output/models/detect_remove_baseline_seed42/final` |

### Baseline 对比

| 实验 | eval_ppl | Δ vs detect-remove |
|------|----------|-------------------|
| **detect_remove_baseline_seed42** | **17.29** | — |
| grid_b0.3_seed42 | 17.640 | +0.35 |
| grid_b0.5_seed42 | 17.651 | +0.36 |
| adaptive_fix_seed42 | 17.653 | +0.36 |
| golden_ratio_seed42 | 17.654 | +0.36 |
| uniform_seed42 | 17.694 | +0.40 |

### 分析

Detect-and-remove (PPL=17.29) **大幅优于**所有 adaptive reweighting 方案。这对论文 claim 不利——简单过滤 q>0.5 后 uniform 训练就能达到最好效果，说明 adaptive reweighting 在已过滤数据上没有额外增益。

但需注意一个关键混淆因素：filtered 数据集只有 153K 条，训练 200M tokens 意味着 ~0.64 epoch（数据没有重复），而 uniform_seed42 用全部 ~371K 条数据也跑 200M tokens。两者的 effective data diversity 不同，这个差异需要在论文 experiment section 中说明。

---
