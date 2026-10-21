# analysis plan 031 entropy and rssm provenance

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_031_entropy_and_rssm_provenance_20260526T033810_result.json`
- **Structured JSON:** [`9bdd82c49f59e7397ae6.json`](../../sessions/9b/9bdd82c49f59e7397ae6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是完整结果。

---

## 子任务 A：RSSM 数据来源厘清

### 文件总览

共发现 **5 个** RSSM 相关 JSON 文件 + 1 个检测器验证文件：

| # | 文件路径 | 域 | 模型数 | n_samples |
|---|---------|---|--------|-----------|
| 1 | `logdir/analysis_rssm_prediction_quality.json` | Cheetah | 3 | 未记录 |
| 2 | `logdir/analysis_rssm_walker_fidelity.json` | Walker | 3 | 600 |
| 3 | `./analysis_rssm_fidelity_v2.json` | Walker | 4 | 800 |
| 4 | `logdir/exp_063_rssm_fidelity/results.json` | Cheetah | 2 | 未记录 |
| 5 | `logdir/exp_066b_timeseries_rssm_fidelity_s1/fidelity_timeseries.json` | 时序分析 | 1 | 4980/step |
| 6 | `./detector_validation_v3.json` | — | — | CiVO 检测器验证，非 RSSM |

### 数据明细表

**文件 1: `analysis_rssm_prediction_quality.json`** (Cheetah)

| 模型类别 | exp_id | gate | dt_embed | dt1 obs_MSE | dt2 obs_MSE | obs_ratio | dt1 rew_MAE | dt2 rew_MAE | rew_ratio |
|----------|--------|------|----------|-------------|-------------|-----------|-------------|-------------|-----------|
| baseline | baseline_s1 (无显式exp_id) | off | 32 | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |
| trained_dt_emb | exp_008d_subsample_on_h8 (无显式exp_id) | on | 32 | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | 2.78x |
| no_dt_emb | exp_008f_no_dt_embed_subsample_on_h8 (无显式exp_id) | on | 0 | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |

> **注意**：此文件 config 中无 experiment 字段、无 checkpoint 路径、无分析步数。

**文件 2: `analysis_rssm_walker_fidelity.json`** (Walker, n=600)

| 模型类别 | exp_id | gate | dt_embed | dt1 obs_MSE | dt2 obs_MSE | obs_ratio | dt1 rew_MAE | dt2 rew_MAE | rew_ratio |
|----------|--------|------|----------|-------------|-------------|-----------|-------------|-------------|-----------|
| baseline | exp_009d_baseline_walker_s1 | off | 0 | 16.07 | 23.49 | **1.46x** | 0.0453 | 0.0587 | 1.30x |
| collapsed_civo | exp_008d_civo_trigger_s4 | on | 32 | 9.96 | 13.20 | **1.33x** | 0.0392 | 0.1219 | 3.11x |
| frozen_dt_emb | exp_057_frozen_dt_emb_walker_s2 | on | 32 | 11.14 | 14.95 | **1.34x** | 0.0678 | 0.1330 | 1.96x |

**文件 3: `analysis_rssm_fidelity_v2.json`** (Walker, n=800, 增加了 no_dt_emb 和 frozen)

| 模型类别 | exp_id | gate | dt_embed | dt1 obs_MSE | dt2 obs_MSE | obs_ratio | dt1 rew_MAE | dt2 rew_MAE | rew_ratio |
|----------|--------|------|----------|-------------|-------------|-----------|-------------|-------------|-----------|
| baseline | exp_009d_baseline_walker_s1 | off | 0 | 15.08 | 23.40 | **1.55x** | 0.0463 | 0.0631 | 1.36x |
| trained_dt_emb | exp_008d_civo_trigger_s4 | on | 32 | 12.37 | 17.80 | **1.44x** | 0.0554 | 0.0829 | 1.50x |
| no_dt_emb | exp_009c_no_dt_emb_s2 | on | 0 | 21.33 | 26.34 | **1.23x** | 0.0689 | 0.0800 | 1.16x |
| frozen_dt_emb | exp_084_frozen_dt_emb_walker_s0 | on | 32 | 17.26 | 24.05 | **1.39x** | 0.0663 | 0.0908 | 1.37x |

**文件 4: `exp_063_rssm_fidelity/results.json`** — 与文件1部分重叠（baseline_s1 + exp_008d），但 baseline config 标记为 dt_embed_dim=0（文件1标记为32），可能是不同版本的分析。

**文件 5: `exp_066b_timeseries_rssm_fidelity_s1/fidelity_timeseries.json`** — 追踪 exp_008d 在训练过程中 fidelity gap 随 step 的变化（10k-65k），obs_ratio 从 0.99(10k) 增长到 1.20(65k)。

### Checkpoint 状况

所有 RSSM 分析 JSON **均未记录 checkpoint 路径和分析步数**。westd 上仅 `exp_008d_civo_trigger_s4` 保留了 `latest.pt` checkpoint (231MB)，其余实验目录只有 metrics.jsonl 或分析结果。原始分析是在 bjb1 上执行的，checkpoint 信息未持久化到 JSON 中。

---

## 子任务 B：Actor Entropy

### 可用实验

| 实验 | 类型 | metrics.jsonl | actor_entropy | 数据范围 |
|------|------|---------------|---------------|----------|
| exp_092_cheetah_no_dt_emb_s1 | no_dt_emb | 145行 | **有** | 5k-105k (11点) |
| exp_093_cheetah_no_dt_emb_s2 | no_dt_emb | 145行 | **有** | 5k-105k (11点) |
| exp_097_cheetah_008d_s3 | trained_dt_emb | 22行 | **有** | 5k-15k (2点，训练中) |
| exp_100_walker_008a_s1 | walker_008a | 5行 | **无** | — |
| exp_008d_civo_trigger_s4 | trained_dt_emb (walker) | 无 | — | — |
| exp_009c/009d/084 | walker variants | 无 | — | — |

### Actor Entropy 数据

**exp_092_cheetah_no_dt_emb_s1:**
```
step     entropy
5000     8.156
15000    1.031
25000   -0.212
35000    0.203
45000   -1.244
55000   -3.030
65000   -3.137
75000   -2.387
85000   -1.522
95000   -1.476
105000  -1.593
```

**exp_093_cheetah_no_dt_emb_s2:**
```
step     entropy
5000     8.108
15000    1.002
25000   -2.688
35000   -3.998
45000   -3.857
55000   -4.052
65000   -3.696
75000   -3.248
85000   -2.599
95000   -2.431
105000  -2.875
```

**exp_097_cheetah_008d_s3 (trained_dt_emb, 训练中):**
```
step     entropy
5000     8.198
15000   -0.759
```

### 趋势对比

| 阶段 | no_dt_emb s1 | no_dt_emb s2 | trained_dt_emb s3 |
|------|-------------|-------------|-------------------|
| 5k (初始) | 8.16 | 8.11 | 8.20 |
| 15k | 1.03 | 1.00 | -0.76 |
| 25-35k | -0.2~0.2 | -2.7~-4.0 | (无数据) |
| 55-65k | -3.0~-3.1 | -3.7~-4.1 | — |
| 95-105k (末期) | -1.5~-1.6 | -2.4~-2.9 | — |

**观察**：
- 两组 no_dt_emb 趋势一致：初始 ~8 → 快速下降 → 45-65k 触底 → 后期轻微回升
- s2 的 entropy 始终低于 s1 约 1-1.5 个单位（更确定性的策略）
- trained_dt_emb (s3) 仅 2 个点，但 15k 时 entropy 已降到 -0.76（同步骤 no_dt_emb 约 +1.0），下降更快
- **缺少 trained_dt_emb 的完整训练曲线进行直接对比**，需要等 exp_097 训练完成或从其他来源获取历史数据

---
