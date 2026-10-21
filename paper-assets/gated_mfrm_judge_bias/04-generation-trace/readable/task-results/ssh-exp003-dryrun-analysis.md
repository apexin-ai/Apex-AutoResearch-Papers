# ssh exp003 dryrun analysis

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp003_dryrun_analysis_20260522T172823_result.json`
- **Structured JSON:** [`7dd11ab709a8ab70f0d3.json`](../../sessions/7d/7dd11ab709a8ab70f0d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已全部读取。全量结果已完成（01:22写入），以下是完整分析。

---

## 1. JSON 输出格式

```
results.json
├── convergence          # per-method: r_hat, ess, divergences
├── arena_correlation    # per-method: kendall_tau/p, spearman_rho/p, matched_models
├── cross_method         # 方法两两对比: kendall_tau, spearman_rho
├── parameters
│   ├── raw_average      # theta_ranking, theta_values
│   ├── mfrm_only        # theta_ranking/values, d_ranking/values
│   ├── sequential       # theta_ranking/values, c_ranking/values, d_ranking/values
│   ├── joint_gmfrm      # theta_ranking/values, c_ranking/values, d_ranking/values
│   ├── top_exposure_items    # (item_id, exposure_score) × 10
│   └── bottom_exposure_items # (item_id, exposure_score) × 10
└── data_summary         # N=8 models, I=176 items, J=9 judges, n_obs=5661
```

附加文件：4 个 PNG（theta_comparison, contamination_c, judge_severity, theta_vs_elo）+ 各方法的 .npy 文件。

---

## 2. Dry-run vs 全量对比

### Convergence

| Method | Dry-run (r_hat / ESS) | Full (r_hat / ESS) | 状态 |
|--------|----------------------|---------------------|------|
| raw_average | NaN / NaN | NaN / NaN | 非MCMC，正常 |
| mfrm_only | NaN / 12 | **1.00 / 2220** | 收敛良好 |
| sequential | NaN / 9 | **1.01 / 395** | 收敛OK |
| joint_gmfrm | NaN / 5 | **1.73 / 6** | **未收敛** |

**joint_gmfrm 严重未收敛**（r_hat=1.73 远超 1.1 阈值，ESS=6 几乎无有效样本）。dry-run ESS=5 已预示了这个问题。

### Arena Correlation (Kendall-τ)

| Method | Dry-run τ | Full τ | p-value |
|--------|-----------|--------|---------|
| raw_average | 0.786 | 0.786 | 0.006 |
| mfrm_only | 0.786 | 0.786 | 0.006 |
| sequential | 0.786 | 0.786 | 0.006 |
| joint_gmfrm | **0.857** | **0.857** | 0.002 |

Dry-run 和全量的 τ 值完全一致——说明 ranking 已稳定，不受 warmup/samples 数量影响。

---

## 3. 全量结果关键信号

### θ ranking（模型能力排名，各方法一致）

| Rank | Model | raw_avg | mfrm_only | sequential | joint_gmfrm |
|------|-------|---------|-----------|------------|-------------|
| 1 | gpt-4o | 0.249 | 1.592 | 1.638 | 2.007 |
| 2 | qwen2.5-72b | 0.207 | 1.212 | 1.195 | 1.167 |
| 3 | gpt-4o-mini | 0.193 | 1.064 | 1.126 | 1.452 |
| 4 | llama-3.3-70b | 0.110 | 0.518 | 0.525 | 0.534 |
| 5 | qwen3-8b | 0.050 | 0.207 | 0.267 | 0.528 |
| 6 | gemma-2-9b | -0.104 | -0.660 | -0.645 | -0.492 |
| 7 | gpt-4-0613 | -0.273 | -1.444 | -1.518 | -1.894 |
| 8 | gpt-3.5-turbo | -0.431 | -2.488 | -2.589 | -3.303 |

raw_average、mfrm_only、sequential 产生**完全相同的排名**（cross-method τ=1.0）。joint_gmfrm 唯一的差异是 gpt-4o-mini 和 qwen2.5-72b 交换了 2/3 位。

### c_n（contamination 估计）

**joint_gmfrm 的 c 值**（全部为正，scale 大）：

| Model | c (joint) | c (sequential) |
|-------|-----------|----------------|
| gpt-3.5-turbo | **5.69** | 0.55 |
| gpt-4-0613 | **4.25** | 0.42 |
| qwen2.5-72b | 3.02 | 0.14 |
| llama-3.3-70b | 2.50 | 0.03 |
| gemma-2-9b | 1.61 | -0.01 |
| qwen3-8b | 1.11 | -0.23 |
| gpt-4o-mini | 0.84 | -0.24 |
| gpt-4o | **0.79** | -0.18 |

两种方法趋势一致：旧模型（gpt-3.5, gpt-4-0613）contamination 最高，新模型（gpt-4o）最低。但 joint 的 c 值 scale 非常大（与未收敛相关），sequential 的 c 值更合理。

### d_j（judge severity，正=严格）

| Judge | mfrm_only | sequential | joint_gmfrm |
|-------|-----------|------------|-------------|
| claude-opus-4.7 | 0.461 | 0.462 | 0.598 |
| gpt-5.5 | 0.410 | 0.410 | 0.535 |
| deepseek-v4-pro | 0.330 | 0.329 | 0.311 |
| claude-sonnet-4.6 | 0.010 | 0.012 | 0.139 |
| gemini-2.5-pro | -0.020 | -0.021 | -0.035 |
| qwen3-235b | -0.069 | -0.069 | -0.038 |
| qwen2.5-72b | -0.239 | -0.239 | -0.350 |
| llama-3.3-70b | -0.379 | -0.380 | -0.419 |
| mistral-large-2 | **-0.504** | **-0.505** | **-0.741** |

三种方法高度一致。Claude Opus 和 GPT-5.5 最严格，Mistral-large-2 最宽松。

---

## 4. 关键问题和全量结果展望

### 问题
1. **joint_gmfrm 未收敛是核心问题**——r_hat=1.73，ESS=6，结果不可信。需要调参（更多 warmup、重参数化、或拆分 c 的先验）
2. **三种非 joint 方法排名完全一致**——说明当前数据中 MFRM 的 bias correction 和 sequential 的 contamination correction 都没有改变最终排名
3. joint_gmfrm 的 τ 更高（0.857 vs 0.786）是否因为它 overfit 了噪声（ESS=6 意味着只有几个有效样本）

### 全量结果已完成
`results/` 目录已有完整输出（与上述分析已一致），包含：
- `results.json`（已分析完毕）
- 4 个 PNG plots
- 各方法的 .npy 文件

下一步建议：**修复 joint_gmfrm 的收敛问题**是首要任务，否则论文核心方法的结果不可用。

---
