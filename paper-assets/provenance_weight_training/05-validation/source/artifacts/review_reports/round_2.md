---
round: 2
review_mode: fresh
overall_score: weak reject
timestamp: 2026-05-19T04:48:27.029870+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 3 (Fresh Review)

**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining
**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026)
**审稿日期**: 2026-05-19
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验统计，R2: 新颖性+Related Work+写作格式）
**轮次**: 1 轮 + 交叉评审（关键问题达成共识，无需 Round 2）

---

## Summary

本文提出 Minimum Intervention Reweighting，一个双约束框架，从 batch 级别的检测器分数自动推导 reweighting exponent b*：通过 α_eff(b) ≥ τ（质量下限）和 ESS(b) ≥ n_min（稳定上限）两个约束选取满足条件的最小 b。在 Qwen3-0.6B continued pretraining（132M FineWeb tokens, 40% 合成污染）上，adaptive b* 的 PPL 接近 grid search 最优值（3-seed: 17.651 vs 17.620, 95% CI [-0.039, 0.101]），ablation 确认 detector signal 和 minimum intervention 缺一不可。Epoch-matched 控制实验揭示 D&R 的表面 PPL 优势完全来自 multi-epoch exposure。

---

## Strengths

**S1. Epoch-matched control 实验设计** [R1+R2 共识]
Table 2 通过控制 content epochs 将 D&R 的 0.360 PPL 表面优势分解为 multi-epoch effect (Δ=0.006 within seed variance)，3-seed 验证 (17.657±0.006 vs 17.651±0.007)。这一分析方法论对领域有独立价值，即使方法本身不被采纳。

**S2. Ablation 层次清晰** [R1+R2 共识]
Random < ESS-only < Uniform < Adaptive 的层级在 ρ=0.4 和 ρ=0.6 两个水平上跨 3 seeds 一致复现（Table 1, Table 8），令人信服地分离了 detector signal 和 minimum intervention 两个要素。ESS-only 的反直觉失败（17.737 vs Uniform 17.694）支撑了 dual constraint 的必要性。

**S3. Detector signal type 发现** [R1+R2 共识]
Discriminative detector (TF-IDF+LR, AUC=0.94) 成功而两个 generative detectors (GPT-2 AUC=0.91, N-gram AUC=0.73) 均失败（Table 7），揭示 AUC 不是决定因素，signal type 才是关键。有实用指导价值，但 3 个 detector 不足以区分 type effect 和 calibration effect。

**S4. 写作质量** [R1+R2 共识]
叙事主线一致，无 AI 写作痕迹（无 em-dash/en-dash 滥用），排版符合 ACL 模板，正文恰好 8 页，Limitations section 坦诚讨论了主要弱点。

**S5. 方法描述清晰**
Algorithm 1 提供完整伪代码，数学推导干净，两个超参数有明确默认值。Reproducibility 评分较高（除代码/数据未公开外）。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1. 统计支撑不足，核心 claim 过强** [R1+R2 共识, critical]
- Adaptive vs Grid-best: 95% CI [-0.039, 0.101] 跨越零，上界 0.101 是效果量 0.043 的 2.3 倍。Abstract 称 "competitive with grid-searched optimum" 是过度表述。
- N=3 的 paired t-test assumptions 无法验证，Wilcoxon signed-rank 在 N=3 下无法给出 p<0.05。
- 效果量 0.043 PPL (0.24% relative) 在 5.3-point continued pretraining drop 中仅占 0.8%。
- Downstream benchmarks 4/5 任务 Adaptive 略差于 Uniform (Table 5)，可能为 distribution matching artifact——PPL 评估集是同源的 human-only FineWeb。
- **修复方向**: 弱化 Abstract/Conclusion claim 措辞（承认 CI 包含 degradation）；增加 seeds 或添加 downstream caveat。

**N2. 理论-经验断联：τ 非 "principled"** [R1+R2 共识, critical]
- Wang 2026 收敛理论假设已知精确 α，但本文的 τ 是经验超参（seed 42 单 seed sweep, Table 3）。
- "Principled defaults" (Section 3.5 L124) 暗示比实际更强的理论保证。
- τ 最优值随 ρ 变化（0.8→0.7, Figure 4），削弱 "zero validation cost" claim (Abstract L5)。
- **修复方向**: "principled" → "empirically robust"；承认 τ 选择替代了 b search，量化搜索空间缩减。

**N3. 1.7B claim 不充分** [R1+R2 共识, critical]
- 单 seed, Δ=-0.01 (13.26 vs 13.26)，效果从 0.6B 的 0.043 缩小 4 倍。
- Abstract/Conclusion 称 "transfers without degradation"，但 Limitations 更谨慎地说 "does not demonstrate a clear advantage"。
- **修复方向**: Abstract/Conclusion 加 "single-seed" qualifier，或补充 multi-seed 1.7B。

**N4. 新颖性不足以支撑 Main Conference** [R2 critical, R1 partial rebut → 共识 Findings 级别]
- 核心公式 w=(1-q)^b 完全来自 Drayson 2025。
- α_eff（加权平均）和 ESS (Kish 1965) 均为标准工具。
- "Minimum intervention principle" 是标准约束优化的 infimum 求解。
- R1 认为 ESS-only ablation 的非平凡失败和 epoch-matched analysis 有独立价值，Excitement 应为 3/5 而非 2/5。
- **两位 Reviewer 共识**: 贡献为 Findings 级别，不足以支撑 Main。
- **修复方向**: 投 Findings，或提供更强理论结果（如 minimum intervention 的 regret bound）。

**N5. 实验规模与论文动机严重脱节** [R1+R2 共识, critical]
- Introduction 以 "web corpora 20-60% machine-generated text" 开篇，framing 为 web-scale 问题。
- 实验仅 0.6B model + 132M tokens，与 web-scale (1T+ tokens) 差 4 个数量级。
- EMNLP data curation 论文 (DataComp-LM, DoReMi) 通常在 billions of tokens 上验证。
- **修复方向**: 缩窄 Introduction framing 至 continued pretraining 场景，或补充 ≥1B tokens 实验。

### Should-Fix（影响评分但不一票否决）

**W1. 自污染外部有效性** [R1+R2 共识]
Qwen3-0.6B 生成 + 训练的自污染设定不代表真实 multi-source web contamination。方法在异质污染下行为未知。Llama-3.2-3B cross-model 结果仅在 Limitations 文本中，无 table。

**W2. Abstract 超长且数据密集** [R2 raised, R1 partial agree]
~280 words，超 250 word 惯例。列举了过多具体数字（PPL, CI, Δ, ablation 排序），读起来像 Results 缩写而非 story。R1 认为数字服务 claim 不算堆砌，但同意应精简至 230-250 words。

**W3. 引用覆盖不足** [R1+R2 共识]
~39 条引用，低于 EMNLP 长文 50-60+ 惯例。遗漏: DCLM (Li 2024), QuRating (Wettig 2024), OLMo (Groeneveld 2024), LESS (Xia 2024), Gerstgrasser 2024 (Is Model Collapse Inevitable?), Gururangan 2020 (Don't Stop Pretraining), Tale of Tails (Dohmatob 2024)。Related Work "Data Mixing" 段过密（一段 12 引用）。

**W4. Discussion 过于单薄** [R1+R2 共识]
~20 行，基本重述 Results。缺少: 失败条件分析、PSIS/Pareto-k 理论连接、soft vs hard filtering 信息论视角、部署指导（何时用 adaptive/D&R/不干预）。

**W5. "Minimum Intervention Principle" framing 过度** [R2 raised, R1 partial rebut]
R2 认为标准约束优化不应命名为 "principle"。R1 认为有先例但应加 qualifier。折中: "empirically motivated minimum intervention strategy"。

**W6. ρ=0.2 失效机制未讨论** [R1 raised, R2 agrees]
Limitations 一行带过 (+0.046 PPL)。机制不清: τ=0.8 时大部分 batch 应 b*=0，为什么 PPL 反而更差？可能 false-positive driven 过度干预。应在 Discussion 或 Appendix 分析。

**W7. Micro-batch B=4 粗糙度** [R1 raised, R2 agrees]
B=4 时 α_eff 仅 5 个离散值 (MAE=0.114)，b* 本质上是 5-way 分类，与 "continuous adaptive selection" framing 不一致。PPL 差异 <0.01 across B∈{4,8,16} 部分缓解，但 micro-batch vs effective-batch 设计选择未充分论证。

**W8. Proposition 1 proof sketch 误导** [R1 raised, R2 agrees]
r_i = 1[q_i ≤ 0.5] 使 Cov(r_i, ln(1-q_i)) ≥ 0 是定义恒等式，不依赖 detector quality。"Better-than-random discrimination" 条件是多余的，误导读者以为单调性依赖检测器质量。不影响方法正确性，影响呈现诚实性。

### Minor

- **M1** [R2]: Responsible NLP Research Checklist 缺失，ACL ARR 要求，可能 desk reject
- **M2** [R1+R2 cross]: Hybrid method (q>0.95 + adaptive, PPL 17.514) 比 pure adaptive 好 0.139 但未在主文讨论/推荐
- **M3** [R1]: 检测器训练细节不足（TF-IDF features, LR 超参, calibration set size, 合成数据生成参数）
- **M4** [R1+R2]: Llama-3.2-3B 结果无 table，仅 Limitations 文本，不可验证
- **M5** [R1]: lin2017focal bib type 错误（article→inproceedings），vehtari2024psis 年份与 OpenAlex 不一致
- **M6** [R1+R2]: ECE 缩写多处使用未定义
- **M7** [R1+R2]: 无代码/数据公开承诺
- **M8** [R2]: 少量 -ing 分词短语结尾 ("confirming that...", "suggesting that...")
- **M9** [R1]: D&R q>0.3 post-hoc oracle 未在 Table 1 注释中标注
- **M10** [R1]: Golden Ratio baseline 仅单 seed，与 3-seed 方法不对称

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 完全一致:

1. **核心 claim 统计支撑不足** (N1): CI 包含 degradation, N=3 power 极低, 效果量微弱
2. **理论-经验断联** (N2): τ 是经验超参但 framing 为 "principled"
3. **1.7B claim 过强** (N3): 单 seed, Δ≈0, Abstract/Conclusion 过度表述
4. **实验规模脱节** (N5): 0.6B/132M vs web-scale framing
5. **适合 Findings 而非 Main** (N4): 方法 novelty 为 incremental，核心公式来自 Drayson 2025
6. **自污染外部有效性** (W1): 不代表真实 multi-source contamination
7. **引用不足** (W3): ~39 条，遗漏多篇重要工作
8. **Discussion 单薄** (W4): 缺少深入分析
9. **ρ=0.2 失效** (W6): 机制未解释
10. **Proposition 1 tautological** (W8): proof sketch 误导
11. **Epoch-matched control 是亮点** (S1): 对领域有独立贡献

---

## Reviewer Divergence [分歧]

| 问题 | R1 | R2 | 折中 |
|------|----|----|------|
| Excitement | 3/5 (epoch-matched + detector-type 有启发性) | 2.0→2.5/5 (自动调参 novelty 不足) | **2.5/5** |
| Overall | 3.0/5 (Findings) | 2.5/5 (Findings/borderline reject) | **3.0/5 (Findings)** |
| Abstract 数据堆砌 | 数字服务 claim，非堆砌 | 读起来像 Results 缩写 | 保留关键数字，精简至 250 words |
| MIP 命名 | "Principle" 有先例，加 qualifier | 标准优化不应称 "principle" | 加 "empirically motivated" qualifier |

---

## Questions to Authors

1. ρ=0.2 时，如果大部分 batch α_eff(0) ≈ 0.8 ≥ τ 且 b*=0，为什么 PPL 比 uniform 更差 (+0.046)？请提供 ρ=0.2 的 b* 分布和 constraint regime 分解。
2. 为什么选择 micro-batch (B=4) 而非 effective batch (B=16) 计算 b*？是否有 B=16 计算的 ablation？
3. Hybrid method (q>0.95 + adaptive, 17.514) 比 pure adaptive 好 0.139 PPL。为什么不推荐 hybrid 作为默认方法？
4. τ 最优从 0.8 (ρ=0.4) 到 0.7 (ρ=0.6)。如果 ρ 未知，能否从 batch-level α_eff(0) 分布反推 ρ 估计来自适应选择 τ？
5. Downstream 4/5 任务略差。如果评估集换成非 FineWeb 来源的 human text，PPL 改善是否仍然存在？
6. Llama-3.2-3B cross-model 的完整结果（PPL, per-task breakdown）能否补充到 Appendix？

---

## Missing References

**高优先级（直接相关，必须引用）:**
- Gerstgrasser et al. (2024) "Is Model Collapse Inevitable?" — 挑战 model collapse inevitability claim
- Gururangan et al. (2020) "Don't Stop Pretraining" — continued pretraining 经典工作

**中优先级（加强 Related Work 覆盖）:**
- Li et al. (2024) DCLM — classifier-based data curation benchmark
- Wettig et al. (2024) QuRating — LLM-based data quality scoring
- Groeneveld et al. (2024) OLMo — 开源 pretraining data pipeline
- Xia et al. (2024) LESS — influence-function data selection
- Dohmatob et al. (2024) "A Tale of Tails" — model collapse heavy-tail analysis

---

## Overall Assessment

**评分: weak reject (for Main) / borderline accept (for Findings)**
**综合分数: 3.0/5**
**置信度: 4/5**

本文解决了一个实际问题（detect-and-reweight 的超参数选择），方法正确，写作诚实。Epoch-matched control 和 detector-type 发现对领域有贡献价值。

但五个 critical 问题限制了 Main Conference 的 acceptance case:
1. 核心 claim 的 CI 包含 degradation，N=3 统计力度不足
2. "Principled" framing 超出了理论实际提供的保证
3. 1.7B 单 seed 结果不支持 scale transfer claim
4. 核心公式来自 Drayson 2025，dual constraint 是标准 IS 工具组合
5. 0.6B/132M tokens 实验与 web-scale framing 脱节 4 个数量级

**建议**: 投 Findings track。如冲击 Main，需要: (a) ≥1B scale multi-seed 实验，(b) downstream 改善的统计证据，(c) 更强理论贡献（如 minimum intervention optimality bound），(d) cross-generator contamination 实验。

---

## Detailed Comments by Section

### Abstract
- ~280 words，建议精简至 ≤250。保留核心数字 (3-seed mean, CI)，删除 ablation 细节和 τ range。
- "Competitive with grid-searched optimum" → "comparable in magnitude to grid-searched values, while eliminating the search cost"。
- 补充一句 downstream caveat。

### Introduction
- 叙事结构完整 (background → gap → insight → method → results → contributions)。
- 开头 "web corpora" framing 与实验规模不匹配——建议聚焦 "continued pretraining on potentially contaminated data"。
- Contribution 3 (detector signal type) 在 Introduction 中铺垫不足。

### Related Work
- 结构合理（4 个主题段）。与 Drayson 2025 的区分清晰。
- "Data Mixing" 段过密（一段 12 引用），建议拆分为 domain-level 和 instance-level。
- 引用量 (~39) 偏少，遗漏见上文。

### Method
- 数学推导干净，Algorithm 1 可直接实现。
- "Principled defaults" → "empirically robust defaults"。
- Proposition 1 proof sketch 需修正（去除 misleading "better-than-random" condition）。
- Micro-batch vs effective-batch 设计选择需论证。

### Experiments
- 训练配置基本完整。检测器细节不足。
- 方法列表完整（6 种 + epoch-matched）。
- 合成数据生成参数（decoding temperature, prompt format）缺失。

### Results
- 最强部分。Epoch-matched control (Table 2) 是实验设计亮点。
- Grid-b trend (Figure 1) 有效可视化了 adaptive vs ESS-only 的定位。
- 统计 claim 需弱化（见 N1）。

### Discussion
- 太短 (~20 行)，大部分重述 Results。需增加失败条件分析、理论连接、部署指导。

### Conclusion
- 1.7B claim 需加 qualifier。

### Limitations
- 坦诚且全面。唯一缺漏: ρ=0.2 失效机制应展开。

### Appendix
- 内容丰富（proofs, grid search, τ sweep, regime, τ-ρ, hybrid, downstream, ρ=0.6, α_eff validation, detector comparison）。
- D&R threshold table (Table 8) 和 dual curve (Figure 5) 是重要补充材料。
- α_eff proxy validation (Table 6) 有效回应了上轮审稿意见。