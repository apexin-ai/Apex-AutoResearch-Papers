# analysis exp 058 ddr causality

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_058_ddr_causality_20260520T075058_result.json`
- **Structured JSON:** [`680a6458de4fd1e5b6bf.json`](../../sessions/68/680a6458de4fd1e5b6bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有更新完成。

---

## exp_058_ddr_causality 分析摘要

**结论: SUCCESS** — Hypothesis 成立，DDR 特征对 depth 有因果预测力，超越相关性。

### 1. Permutation Importance
- Baseline F1 = 0.7714
- **Drifting 组** avg importance = 0.158，**Stationary 组** = 0.030（**5.3x 差距**）
- 排序: hapax_ratio (0.235) > entropy_mean (0.170) > ttr (0.156) > entropy_max (0.070) > entropy_std (0.057) > entropy_min (0.019) > tail_decay (0.014)
- 两组均独立贡献，drifting 主导

### 2. Granger Causality (panel N=29,095, lag=1)
- **6/7 特征显著** (p < 0.05)，唯一例外 entropy_min (p=0.538)
- 最大效应: entropy_std ΔR²=0.031 (F=1338)
- 方向一致: hapax_ratio/ttr 随 depth **递增**，entropy 系列 **递减**
- Fisher combined 跨 8 generator 验证: 6/7 显著，entropy_min 仍不显著 (p=0.375)

### 3. Intervention
- 所有 7 特征干预后 F1 均下降（0.6–2.0pp）
- 最大: entropy_max (−2.0pp)，其次 entropy_mean (−1.1pp)，entropy_std (−0.95pp)
- entropy_max 干预效果最大但 permutation importance 仅排第 4，说明其因果贡献具有特异性

### 注意事项
- entropy_min 是最弱特征：Granger 不显著、permutation 最低（0.019），但仍有干预效果（0.6pp）
- T=5 depth chain 限制只能用 lag=1，per-seed Granger 不可行，结果依赖 pooled panel regression
- Mistral-7B 的 per-generator Granger 在 hapax_ratio/ttr 上不显著（p>0.4），但 Fisher combined 仍显著——表明这两个特征的 Granger 信号不是所有 generator 均匀贡献的

---
