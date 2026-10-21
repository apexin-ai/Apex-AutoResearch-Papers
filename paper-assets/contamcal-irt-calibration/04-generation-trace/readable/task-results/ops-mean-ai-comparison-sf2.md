# ops mean ai comparison sf2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mean_ai_comparison_sf2_20260517T180920_result.json`
- **Structured JSON:** [`3968c3ca084328e057b2.json`](../../sessions/39/3968c3ca084328e057b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

### a_i (Item Discrimination) 对比

| 组别 | n | Mean ± SD | Median | IQR |
|------|---|-----------|--------|-----|
| All 14042 items | 14042 | 1.611 ± 0.569 | 1.830 | [1.064, 2.055] |
| RRF-300 subset | 300 | 1.666 ± 0.566 | 1.847 | [1.149, 2.070] |
| excl00-2000 subset | 2000 | 1.610 ± 0.570 | 1.824 | [1.017, 2.061] |

### 统计检验

| 对比 | Mann-Whitney p | t-test p | Cohen's d |
|------|---------------|----------|-----------|
| RRF-300 vs excl00-2000 | 0.076 | 0.114 | 0.098 |
| RRF-300 vs Complement (13742) | 0.051 | 0.094 | 0.098 |

### RRF exposure 与 a_i 的相关性

- Pearson r = -0.013 (p=0.13), Spearman ρ = -0.001 (p=0.92)
- 高/低 exposure quintile 的 a_i 无显著差异 (p=0.41)

### 结论

**RRF 没有系统性选出高 discrimination items。**

1. 两组 a_i 差异不显著（所有 p > 0.05，Cohen's d ≈ 0.10 属于 negligible effect）
2. RRF exposure 与 a_i 几乎零相关（r ≈ -0.01）
3. 关键注意：**两组 items 都是随机子采样**（seed=42），代码中的 "RRF" 指的是 IRT 模型中使用 RRF 信号作为 exposure covariate，不是基于 RRF 得分选择 items。RRF-300 略高的均值 (1.666 vs 1.610) 仅是随机波动。

---
