# ops plan 013 analyze

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan_013_analyze_20260515T234816_result.json`
- **Structured JSON:** [`2c37907b8330c473736f.json`](../../sessions/2c/2c37907b8330c473736f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集完毕。以下是完整报告。

---

## Phase 3: 完整结果

### 条件汇总表

| Condition | Mean PPL | Std | n_samples |
|-----------|----------|-----|-----------|
| unfiltered | 15.7761 | 0.0663 | 10000 |
| rf_strict | 15.8098 | 0.0611 | 2496 |
| rf_moderate | 15.7555 | 0.0563 | 4940 |
| rf_soft | 15.7334 | 0.0375 | 4422 |
| oracle_strict | 15.8785 | 0.1282 | 2500 |
| oracle_moderate | 15.8092 | 0.1025 | 5000 |
| random_strict | 16.2387 | 0.1654 | 2496 |
| random_moderate | 15.9979 | 0.0899 | 4940 |

### 统计检验表（各 condition vs unfiltered baseline，paired t-test）

| Comparison | Δ PPL | t | p | Cohen's d | Significant? |
|------------|-------|---|---|-----------|-------------|
| rf_strict vs unfiltered | -0.0337 | -0.5571 | 0.6071 | -0.5283 | No |
| rf_moderate vs unfiltered | +0.0205 | 0.7562 | 0.4916 | 0.3339 | No |
| rf_soft vs unfiltered | +0.0427 | 0.9265 | 0.4067 | 0.7923 | No |
| oracle_strict vs unfiltered | -0.1025 | -1.4695 | 0.2156 | -1.0038 | No |
| oracle_moderate vs unfiltered | -0.0331 | -0.7685 | 0.4851 | -0.3836 | No |
| random_strict vs unfiltered | -0.4626 | -4.2188 | 0.0135 | -3.6710 | **Yes** |
| random_moderate vs unfiltered | -0.2219 | -3.3529 | 0.0285 | -2.8091 | **Yes** |

（Δ 为正=condition PPL 更低=更好）

### Reviewer 指定的跨条件对比（paired t-test）

| Comparison | Δ PPL (ours) | t (ours) | p (ours) | Reviewer Δ | Reviewer t | Reviewer p | 偏差 |
|------------|-------------|----------|----------|------------|------------|------------|------|
| rf_strict vs random_strict | +0.429 | -7.052 | 0.0021 | 0.429 | -7.15 | <0.002 | Δ 完全一致；t 偏差 1.4%，p 边际差异 |
| rf_moderate vs random_moderate | +0.242 | -3.770 | 0.0196 | 0.229 | -5.58 | ≈0.005 | **Δ 偏差 5.7%，t 值显著偏差（-3.77 vs -5.58），p 偏差大（0.020 vs 0.005）** |
| rf_soft vs unfiltered | +0.043 | 0.927 | 0.407 | — | 0.93 | ≈0.41 | 完全一致 |
| random_strict vs unfiltered | -0.463 | 4.219 | 0.0135 | — | -4.56 | ≈0.01 | t 幅度偏差 7.5%（符号为方向约定差异）|

### 交叉核对结论

1. **定性一致**：所有对比的显著性判定完全吻合——rf_strict vs random_strict (显著)、rf_moderate vs random_moderate (显著)、rf_soft vs unfiltered (不显著)、random_strict vs unfiltered (显著)

2. **定量偏差**：
   - 3/4 对比的 t/p 值与 Reviewer 接近（偏差 <8%）
   - **rf_moderate vs random_moderate 有实质性偏差**：我们的 t=-3.77 (p=0.020) vs Reviewer 的 t=-5.58 (p=0.005)。检查了 independent t-test (t=-4.57, p=0.002) 也不匹配。可能原因：Reviewer 手算的中间值有四舍五入累积误差，或使用了不同的 pooled variance 公式。我们的值直接从原始数据计算，是权威结果。

3. **核心发现**：
   - RF curation 条件（strict/moderate/soft）均未显著优于 unfiltered baseline（p>0.40）
   - Random filtering 显著劣于 unfiltered（strict: p=0.014, moderate: p=0.029）
   - RF 筛选显著优于同等力度的 random 筛选（strict: p=0.002, moderate: p=0.020），说明 RF 保留了对下游任务有价值的样本
   - Oracle 筛选也未优于 unfiltered——oracle_strict 反而劣化（Δ=-0.10），暗示纯按 depth 筛选可能过度移除了有用的多样性

---
