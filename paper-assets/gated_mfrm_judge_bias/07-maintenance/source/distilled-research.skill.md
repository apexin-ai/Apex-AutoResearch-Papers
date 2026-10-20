---
name: judge-bias-contamination-research
description: LLM judge bias与benchmark contamination领域的实验设计共识、竞品定位、方法论趋势——12篇论文蒸馏
type: skill
---

## Benchmark 与指标共识

- **Judge bias 研究**用 MT-Bench（4/12）+ Arena-Hard（3/12）。Contamination 研究用 GSM8K+MMLU+ARC-C+HellaSwag 四件套（3/12）。G-MFRM 需覆盖两组。**置信度 高**
- **Human reference** 是必要验证：zheng2023 用 3K expert + 3K crowd votes，UDA 用 100 条，CyclicJudge 用 panel mean 作 proxy。**置信度 高**
- **核心指标**：Inter-judge std/Var(X̄)↓（CyclicJudge,UDA）| Agreement/Pearson r with human↑（zheng2023,UDA）| Rater parameter→0（wang2025）| Detection rate/δ̂（ConStat）| Kendall τ↑（PSN-IRT）。G-MFRM 需同时报 θ-RMSE + Kendall τ + judge/contamination 指标。

## 方法论趋势

**上升**：(1) Psychometric models 迁移至 LLM（MFRM, 4PL IRT, DG-IRT）(2) Multi-judge panels + 统计方法处理 judge variance (3) Performance-based contamination 定义取代 information-flow（ConStat: r²=0.94）。**置信度 高**

**消退**：Perplexity-based 污染检测易绕过（ConStat 89% vs Shi 21.7%）；单 judge 已不可接受。**置信度 中**

## G-MFRM 竞品定位

| 竞品 | Judge Bias | Contamination | 可解释 | G-MFRM 优势 |
|------|:-:|:-:|:-:|------|
| CyclicJudge | ✓ | ✗ | ✓ | 联合建模 |
| UDA | ✓ | ✗ | ✗ | 可解释+contamination |
| DCR | ✗ | ✓ | 部分 | judge facet |
| ConStat | ✗ | ✓ | ✓ | judge facet |
| PSN-IRT | ✗ | 间接 | ✓ | multi-facet+judge |

**核心空白（0/12篇）**：无论文同时建模 judge severity 与 contamination 的 confounding。CyclicJudge 证明 judge bias 占 >94% variance 但忽略 contamination；DCR 调整 accuracy 但忽略 judge。**置信度 高**

## 实验设计经验

- **Judge panel**：5-10 judges from ≥3 families（CyclicJudge, UDA, wang2025）**置信度 中**
- **Position swap**：pairwise evaluation 标准操作（zheng2023）**置信度 高**
- **显著性检验**：Bootstrap + BH 校正（ConStat, preference_leakage）或 paired Wilcoxon **置信度 高**
- **Self-preference**：judge 自评偏高是 universal pattern（CyclicJudge: Qwen 自评第一但共识排最后；UDA: [-21%,+56%] deviation）——G-MFRM 的 d_j 应捕获 **置信度 高**

## 共同局限 → G-MFRM 卖点

1. Judge bias 和 contamination 分别处理（6/12）→ joint estimation
2. 无 confounding 分析（0/12）→ ρ(d_j, c_n·e_i) 实验
3. 小规模验证（wang2025: 30人, CyclicJudge: 5 judges）→ 更大规模
4. 闭源模型训练数据不透明（4/12）→ black-box compatible
