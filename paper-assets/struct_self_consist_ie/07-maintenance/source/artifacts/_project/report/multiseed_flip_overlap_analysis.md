# Multi-seed RE LP Selection Flip Instance Overlap Analysis

## 数据可用性

| 数据类型 | seed42 | seed123 | seed456 |
|----------|--------|---------|---------|
| Constrained (N=8) | `exp_012_rerun_1024/samples_with_logprobs.jsonl` | `exp_018_qwen_scierc_seed123/samples.jsonl` | `exp_018_qwen_scierc_seed456/samples.jsonl` |
| Free-form (N=8) | `results/exp_freeform_ablation/samples.jsonl` | ❌ 不存在 | ❌ 不存在 |

- 每个文件 551 instances（Qwen SciERC）
- Free-form 仅 seed42，无法做跨 seed flip overlap 分析
- **替代方案**: 用 constrained 三种子做 LP failure instance 稳定性分析

---

## 1. Constrained LP Selection Failure 概览

| Seed | Failure | LP Better | Equal | Total |
|------|---------|-----------|-------|-------|
| seed42 | 83 | 38 | 430 | 551 |
| seed123 | 67 | 42 | 442 | 551 |
| seed456 | 66 | 46 | 439 | 551 |

"Failure" = LP-selected sample 的 RE F1 < greedy RE F1。

### 排除 0-gold-relation instances 后

154 instances 的 gold relation 数 = 0（greedy 正确不输出关系得 F1=1.0，LP 选的 sample 可能输出了伪关系得 F1=0.0）。

| Seed | Failure (有 rels) | Better | Equal |
|------|-------------------|--------|-------|
| seed42 | 59 | 36 | 302 |
| seed123 | 47 | 42 | 308 |
| seed456 | 47 | 41 | 309 |

---

## 2. Pairwise Jaccard Similarity 矩阵

### 全部 instances

| Pair | Jaccard | |Intersection| | |Union| |
|------|---------|----------------|---------|
| seed42 vs seed123 | **0.456** | 47 | 103 |
| seed42 vs seed456 | **0.380** | 41 | 108 |
| seed123 vs seed456 | **0.430** | 40 | 93 |
| **Average** | **0.422** | — | — |

- 3-way 交集: 34 instances（占 any-fail 的 27.9%）
- Any-seed 并集: 122 instances

### 排除 0-gold-relation instances 后

| Pair | Jaccard |
|------|---------|
| seed42 vs seed123 | **0.452** |
| seed42 vs seed456 | **0.359** |
| seed123 vs seed456 | **0.424** |
| **Average** | **0.412** |

- Stable failures (有 rels): 24 instances
- Any-fail (有 rels): 88 instances

---

## 3. Stable Failure Instance 特征

### 按失败稳定性分组

| 组 | N | Avg gold_rels | Avg gold_ents | Avg greedy_F1 | Avg LP_F1 | Avg Δ |
|----|---|---------------|---------------|---------------|-----------|-------|
| Stable fail (3 seeds) | 34 | 2.12 | 3.50 | 0.688 | 0.189 | -0.499 |
| Fail 2+ seeds | 26 | 2.46 | 3.58 | 0.774 | 0.323 | -0.450 |
| Fail 1 seed only | 62 | 2.32 | 3.76 | 0.692 | 0.453 | -0.239 |
| Never fail | 429 | 1.62 | 2.89 | 0.429 | 0.471 | +0.041 |

核心发现:
- **失败 instances 的 gold relation 数更多**（2.1-2.5 vs 1.6），greedy F1 更高（0.69-0.77 vs 0.43）
- LP 在 greedy 已经表现好的 instance 上反而选错

### Gold Relation Count 与 Failure Rate 的关系

| Gold Rels | N | Avg 3-seed Failure Rate |
|-----------|---|------------------------|
| 1 | 148 | 4.3% |
| 2 | 110 | 13.9% |
| 3 | 58 | 20.7% |
| 4 | 31 | 20.4% |
| 5 | 21 | 25.4% |
| 6 | 14 | 26.2% |
| 7+ | 15 | ~15% |

**清晰的正相关**: 更多 gold relations → 更高 LP failure rate。复杂 instances 的 sample 多样性更大，LP 难以选到最优。

### 0-Gold-Relation Stable Failures

10/34 stable failures 是 0-gold-relation instances。这些 instances 的 greedy 正确输出空关系（F1=1.0），但 LP 系统性地偏好生成了虚假关系的 samples。LP 有 "verbose bias"——倾向选择输出更丰富的 sample。

---

## 4. Flip Instance 分析 (seed42)

**定义**: Constrained LP failure ∩ Free-form LP success。

| 指标 | 值 |
|------|-----|
| Constrained failures (seed42) | 83 |
| Free-form LP better (seed42) | 48 |
| **Flip instances** | **6** (5 有 gold rels) |

### Flip Instance 详情

| Instance | Gold Rels | C greedy | C LP | FF greedy | FF LP | Stability |
|----------|-----------|----------|------|-----------|-------|-----------|
| A97-1020_sent001 | 8 | 0.400 | 0.333 | 0.400 | 0.875 | 1-seed |
| ECCV_2006_13_abs_sent004 | 5 | 0.444 | 0.200 | 0.250 | 0.800 | 3-seed stable |
| H01-1049_sent003 | 0 | 1.000 | 0.000 | 0.000 | 1.000 | 2+-seed |
| ICML_2006_119_abs_sent005 | 1 | 0.667 | 0.000 | 0.667 | 1.000 | 2+-seed |
| ICML_2016_18_abs_sent000 | 6 | 0.909 | 0.375 | 0.800 | 0.857 | 2+-seed |
| N06-1037_sent000 | 2 | 0.400 | 0.333 | 0.400 | 1.000 | 2+-seed |

Flip instances 特征:
- **平均 gold_rels = 3.67** (远高于全局 1.86)
- Constrained 中 LP 大幅选错 (Δ = -0.430)
- Free-form 中 LP 大幅选对 (Δ = +0.503)
- 5/6 是 ≥2-seed failure，说明这些 instance 的 constrained LP 失败是 systematic 的

### Flip vs Stable Failure 重叠

- Flip ∩ Stable failure (3-seed): 1/6 = 16.7%
- Flip ∩ ≥2-seed failure: 5/6 = 83.3%

### Reverse Flip (Constrained LP better + Free-form LP failure)

仅 2 instances。LP 在 constrained 下成功但 free-form 下失败的情况极少。

---

## 5. Constrained vs Free-form LP Delta 相关性

| 指标 | 值 |
|------|-----|
| Pearson correlation | **0.522** |
| Both fail | 28 |
| Both better | 20 |
| Flip (C-fail, FF-better) | 5 |
| Reverse (C-better, FF-fail) | 2 |
| One/both neutral | 342 |

r=0.52 表明 constrained 和 free-form 下 LP 的行为是中等相关的。两种模式下 LP 对相同 instances 的倾向一致。

---

## 6. LP 选择一致性

### LP 选择的 Sample Index 跨种子一致性

| 一致性 | 比例 |
|--------|------|
| 3 seeds 选同一 sample | 8/551 = 1.5% |
| ≥2 seeds 选同一 sample | 195/551 = 35.4% |

LP 在 sample level 极不稳定（仅 1.5% 完全一致），但 failure pattern level 有中等稳定性（Jaccard ~0.42）。说明特定 instances 的 LP 选错是因为 **该 instance 的 sample 分布特性**（多样性大，logprob 区分度低），而非某个特定 bad sample。

### LP Logprob Gap (seed42, 有 rels)

| 组 | N | Median gap | Mean gap |
|----|---|------------|----------|
| LP failure | 59 | -0.002 | -0.002 |
| LP success | 36 | -0.001 | +0.003 |

LP 失败时的 logprob gap 极小，说明 LP 在边界情况下选错。

---

## 7. 结论与论文建议

### 核心发现

1. **Jaccard ~0.42**: 中等稳定性。LP failure pattern 部分是 systematic（不是纯噪声），但也不够 robust（不是强 deterministic pattern）
2. **驱动因素**: Instance 复杂度（gold relation 数）是最强信号。更多 relations → 更高 failure rate
3. **LP verbose bias**: LP 系统性偏好输出更丰富的 samples，在 0-gold-relation instances 上表现为稳定失败
4. **Flip 极少**: 仅 5-6 个 flip instances，不足以支撑独立论点
5. **LP 在 sample 级别高度不稳定** (1.5% 一致)，但在 instance 级别中等稳定 (Jaccard 0.42)

### Section 5 措辞建议

**不建议**: 强措辞如 "LP selection failures are robust and predictable across seeds"

**建议**: 中等措辞，例如:
> "LP selection failures are partially systematic: instances with more gold relations and higher sample diversity are consistently more likely to suffer from LP mis-selection across seeds (average pairwise Jaccard = 0.42). However, LP picks different optimal samples under different seeds (only 1.5% full agreement), suggesting the failures stem from inherent instance-level difficulty rather than a deterministic failure mode."

**关于 flip instances**: 数量太少 (5-6)，不适合作为独立的 subsection 或强论点。可以作为一个 illustrative example 在讨论中提及:
> "In rare cases (5/397 instances with gold relations), LP selection flips from failure under constrained decoding to success under free-form decoding, typically on complex instances (avg 3.67 gold relations) where free-form generation better preserves relational structure."

**适合放 appendix**: 完整 Jaccard 矩阵、stable failure instance 列表、gold-rel vs failure rate 表。
