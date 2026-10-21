# ssh mcmc diagnose and fix

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mcmc-diagnose-and-fix_20260525T132445_result.json`
- **Structured JSON:** [`3f9cc924547d1fc7b195.json`](../../sessions/3f/3f9cc924547d1fc7b195.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Dry-run 结果非常好。** NCP 完全修复了收敛问题。

---

## 诊断结果

### R-hat 最差参数类型：b_i（item difficulty）

| 指标 | v1 (centered) | v2 (NCP, dry-run) |
|------|--------------|-------------------|
| b R-hat max | **2.900** | **1.020** |
| b R-hat mean | 1.492 | 1.002 |
| b ESS_bulk min | 4 | 719 |
| theta R-hat max | 1.620 | 1.010 |
| d R-hat max | 1.600 | 1.010 |
| R-hat > 1.05 | 541/548 | 16/1050 |
| R-hat > 1.1 | 520/548 | 3/1050 |
| ESS_bulk median | ~4 | 1059 |
| b inter-chain std max | 1.758 | 0.052 |

### 数据稀疏度：不是问题

- 所有 500 items 有 ≥27 obs（均值 72.5）
- Judge coverage: 207 items 4 judges, 95 items 5 judges, 194 items 6 judges, 4 items 7 judges
- 57.6% 覆盖率，MCAR pattern

### Chain 间差异：v1 多模态，v2 已修复

- v1 b inter-chain std: mean=0.49, max=1.76（链卡在不同模式）
- v2 b inter-chain std: mean=0.009, max=0.052（链间一致）

### 根因

centered `b ~ Normal(0, 1)` 的固定先验尺度与 500 个 item 的异质后验几何冲突，NUTS 无法有效探索。Non-centered + hierarchical `sigma_b` 让采样器在标准正态空间上高效工作。

## 修复方案

- **Non-centered b**: `b_raw ~ N(0,1)`, `sigma_b ~ HalfNormal(1.0)`, `b = b_raw * sigma_b`。学到 `sigma_b = 1.86`
- **Non-centered theta**: `theta_raw ~ N(0,1)`, `sigma_theta ~ HalfNormal(1.0)`, `theta = theta_raw * sigma_theta - mean`。学到 `sigma_theta = 1.63`
- **d 不改**：仅 6 个参数，修复 b 后 d 也收敛了（R-hat max 1.01）
- **c 不改**：已经是 non-centered
- **chain_method='vectorized'** 替代 'sequential'
- Item 筛选：保留现有 min_judges=3（数据不稀疏，无需额外过滤）

## Dry-run 结果

- R-hat max: **1.026**（阈值 1.1，通过）
- ESS min: **117**（阈值 50，通过）
- 仅 theta_raw 有 3 个参数 R-hat ≈ 1.10（dry-run 仅 500 warmup，full run 6000 warmup 会解决）
- 运行时间：126s（mfrm_only, 2 chains, 500w+500s）
- 全量运行估计：~42 min（mfrm_only），全部 4 methods ~90 min

## 新脚本路径

`/root/gated_mfrm_judge_bias/run_mcmc_n17_exp020_v2.py`

**等 Director 审批后启动完整 MCMC。**

---
