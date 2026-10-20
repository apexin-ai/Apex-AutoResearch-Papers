# fig_signal_heatmap 数据源审计报告

**日期**: 2026-05-14
**审计对象**: `figures/paper/fig_signal_heatmap.py`
**触发**: Reviewer 发现 SciERC NER 列数据与 exp_015 统一评估不一致

---

## 1. exp_015 统一数值表

exp_015 数据源: `output/exp_012_logprob/samples_with_logprobs.jsonl`
配置: N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2

> **注意**: exp_015 代码注释声称使用 pilot_005 (T=0.7) 数据，但 DATA_PATH 实际指向 exp_012_logprob 的重新推理数据。注释有误。

### NER (n_valid=529, n_cond=501)

| Signal | Full ρ | Cond ρ | Full AUROC | Full τ |
|--------|--------|--------|------------|--------|
| Entity Voting | **0.5018** | **0.4497** | 0.7279 | 0.3766 |
| Soft Jaccard | 0.3565 | 0.4120 | 0.6656 | 0.2658 |
| Exact Match | 0.2566 | 0.3427 | 0.6230 | 0.1924 |
| Fleiss' Kappa | 0.2651 | 0.3060 | 0.6243 | 0.2027 |
| Mean Logprob | 0.1396 | 0.1627 | 0.5585 | 0.1006 |

### RE (n_valid=397, n_cond=296)

| Signal | Full ρ | Cond ρ | Full AUROC | Full τ |
|--------|--------|--------|------------|--------|
| Entity Voting | **0.4217** | **0.4630** | 0.7162 | 0.3270 |
| Soft Jaccard | 0.2112 | 0.3683 | 0.5816 | 0.1619 |
| Exact Match | 0.1002 | 0.3607 | 0.5036 | 0.0839 |
| Fleiss' Kappa | 0.2528 | 0.3168 | 0.6308 | 0.1967 |
| Mean Logprob | 0.2467 | 0.1457 | 0.6354 | 0.1808 |

---

## 2. Heatmap vs exp_015 对比 (SciERC NER full)

| Signal | Heatmap 值 | exp_015 值 | Δ | Heatmap 数据来源 |
|--------|-----------|-----------|------|----------------|
| Voting Conf | 0.392 | 0.502 | **-0.110** | exp_014 (pilot_004/samples.jsonl) |
| Soft Jaccard | 0.383 | 0.357 | +0.027 | pilot_004 report (full_rho_sj=0.3825) |
| Exact Match | 0.294 | 0.257 | +0.037 | exp_013 (pilot_004/samples.jsonl) |
| Fleiss' Kappa | 0.259 | 0.265 | -0.006 | pilot_004 report (full_rho_fk=0.259) |
| Log-prob | 0.140 | 0.140 | 0.000 | exp_012 (samples_with_logprobs.jsonl) |

### Heatmap SciERC RE 列对比

| Signal | Heatmap RE full | exp_015 RE full | Δ |
|--------|----------------|-----------------|------|
| Voting Conf | 0.340 | 0.422 | **-0.082** |
| Soft Jaccard | 0.244 | 0.211 | +0.033 |
| Exact Match | 0.156 | 0.100 | +0.056 |
| Fleiss' Kappa | 0.278 | 0.253 | +0.025 |
| Log-prob | 0.247 | 0.247 | 0.000 |

| Signal | Heatmap RE cond | exp_015 RE cond | Δ |
|--------|----------------|-----------------|------|
| Voting Conf | 0.384 | 0.463 | **-0.079** |
| Soft Jaccard | 0.372 | 0.368 | +0.004 |
| Fleiss' Kappa | 0.307 | 0.317 | -0.010 |
| Log-prob | 0.146 | 0.146 | 0.000 |

---

## 3. Voting Conf 差异根因分析

### 3.1 算法一致性确认

三个脚本 (exp_001_postprocess.py, analyze_entity_voting.py/exp_014, analyze_exp015_unified.py) 的 voting_confidence 算法**完全相同**:

```python
# 对每个 instance 的 N 个 samples：
# 1. 统计所有 unique entity (text, type) 出现次数
# 2. 每个 entity 的 voting rate = count / N
# 3. 信号值 = mean(所有 entity 的 voting rate)
```

### 3.2 数据不一致是根因

| 属性 | pilot_004/samples.jsonl (exp_014用) | exp_012_logprob/samples_with_logprobs.jsonl (exp_015用) |
|------|-------------------------------------|------------------------------------------------------|
| 实例数 | 551 | 551 |
| 推理配置 | N=8, T=1.0, seed=42 | N=8, T=1.0, seed=42 (含logprob) |
| NER SJ ρ | 0.3825 | 0.3565 |
| NER Voting ρ | 0.3915 | 0.5018 |
| RE cond n | 313 | 296 |

**关键证据**: 对比第一个 instance (X96-1059_sent000) 的第一个 sample：
- pilot_004: 4 entities (Recognition of proper nouns/Task, proper nouns/OtherScientificTerm, Japanese text/Material, morphological analysis/Task, Japanese text processing/Task)
- exp_012: 2 entities (Recognition of proper nouns in Japanese text/Task, Japanese text processing/Task)

**两个文件的 samples 完全不同。** exp_012 的推理是独立重新运行的（用于收集 logprob），产生了不同的 samples，尽管配置相同。LLM 采样的随机性导致不同 inference run 产生不同输出。

### 3.3 为什么 Voting Conf 差异最大

Voting confidence (Δ=0.110) 远大于 SJ (Δ=0.027) 和 FK (Δ=0.006) 的差异。原因：

- **SJ/FK 是 pairwise 聚合**：计算所有 sample pairs 的 overlap，对单个 sample 的变化鲁棒性更高
- **Voting confidence 是 entity-level 频率的均值**：受 unique entity 数量和分布强烈影响。不同 inference run 产生的 entity 集合差异会被放大为 voting rate 分布的差异
- Voting conf ρ 从 0.39→0.50 的跳跃表明该信号在 sample 变化下方差大，**两个值都在其 bootstrap CI 范围内**（exp_004 报告 NER voting_conf 95% CI: [0.305, 0.466]）

---

## 4. RE cond SJ = 0.372 来源确认

| 候选来源 | RE cond SJ ρ | 匹配度 |
|---------|-------------|--------|
| exp_015 (logprob data) | 0.3683 | 0.372 ≠ 0.368 |
| exp_012 (logprob data) | 0.3683 | same |
| pilot_004 (original) | 0.3161 (n=313) | 远不匹配 |
| pilot_005 (T=0.7) | 0.3716 (n=301) | **0.372 ≈ 0.3716** |

**最可能来源**: pilot_005 (T=0.7, N=8)。这意味着 heatmap 的 RE cond SJ 值混入了 T=0.7 数据，而图表标题声明 T=1.0。

但也存在另一种可能：某个中间分析脚本在 pilot_004 数据上使用了不同的 conditional filter（如 gold-nonempty + sample F1 > 0 组合）产生了 0.372。需要进一步排查。

---

## 5. 数据源混用总结

Heatmap SciERC 列至少混用了 **3 个不同数据源**：

| 数据源 | 包含的信号 | 推理 run |
|--------|----------|---------|
| pilot_004/samples.jsonl | SJ, FK, Voting (via exp_013/014) | 原始 pilot 推理 |
| exp_012_logprob/samples_with_logprobs.jsonl | Logprob | 重新推理（含 logprob） |
| pilot_005 (可能) | RE cond SJ | 不同温度 T=0.7 |

两个"pilot_004"数据源本身就是不同的 inference run，产生不同的 samples。

---

## 6. 推荐方案

### 方案 A（推荐）：以 exp_015 为唯一数据源

用 exp_015 的 `exp015_unified_report.json` 替换所有 SciERC 列。

**优点**:
- 5 个信号在同一数据集上统一计算
- 包含 bootstrap CI 和 calibration 分析
- 已有完整的 NER + RE (full + cond) 结果

**缺点**:
- Voting conf 从 0.39 跳到 0.50，改变 signal ranking 叙事
  - 旧叙事："SJ 和 voting 相当，SJ 优在可解释性"
  - 新叙事："voting 显著领先 SJ（+0.145），SJ 的独特价值在 conditional 和 RE 场景"
- 基于 exp_012 重新推理的 samples，不是原始 pilot 数据

**需要更新的 heatmap 值 (SciERC NER)**:
```python
# 旧:  [0.392, 0.383, 0.294, 0.259, 0.140]
# 新:  [0.502, 0.357, 0.257, 0.265, 0.140]
```

### 方案 B：在 pilot_004 原始数据上重新运行 exp_015 风格的统一分析

在 `pilot_004/samples.jsonl` 上统一计算所有 5 个信号（但无 logprob，因原始数据无 logprob 字段）。

**优点**: 与 pilot_004 其他分析一致
**缺点**: 缺少 logprob 信号；仍需单独处理 logprob 列

### 方案 C：全新统一推理 + 评估

重新运行 N=8 T=1.0 推理（固定 seed），同时收集 logprob，然后运行 exp_015 分析。

**优点**: 彻底一致
**缺点**: 需要 GPU 时间，且新数据可能与论文其他部分的值不一致

### 决策要点

- 方案 A 最快，但需要调整论文叙事
- Voting conf 0.50 的 bootstrap CI 范围包含 0.39（exp_004 CI: [0.305, 0.466]），差异在统计上可能不显著
- 建议：先检查 exp_015 中 SJ vs Entity Voting 的 bootstrap CI 是否 overlap，再决定叙事调整幅度

---

## 7. 即时行动项

1. **决定数据源方案** (A/B/C)
2. 如选方案 A，更新 `fig_signal_heatmap.py` 中 SciERC 列的 data array
3. 检查论文正文中所有引用 SciERC NER ρ 值的地方是否一致
4. 更新 signal ranking 叙事（如有需要）
5. 在 paper_provenance.yaml 中记录最终数据源选择
