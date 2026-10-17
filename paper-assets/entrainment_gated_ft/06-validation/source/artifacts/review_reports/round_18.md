---
round: 18
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-24T12:17:42.273362+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# Round 18 审稿报告

**Venue**: EMNLP 2026 via ARR (May cycle) | **Deadline**: 2026-05-25 | **Reviewers**: 2 (方法严谨性 + 新颖性/完整性)

---

## Summary

论文研究混合线性循环架构（GDN、RetNet、HGRN2）在 aggregate benchmark 上表现相近时的 per-example 预测差异。使用 Wang et al. (2025) 的 controlled model zoo（3 架构 × 5 attention 比例 × 2 规模），在 10 个 benchmark 上分析 30 个配置，发现：(1) 跨架构 per-example Jaccard overlap 仅 ~0.10（约为独立基线 2 倍），在 4% attention 即饱和；(2) multiplicity 幅度取决于任务类型（α = 0.14–0.30）而非 attention 剂量；(3) confidence-based routing 仅在 LAMBADA 上有效（+5.2pp），其余 benchmark 无效或负效。

---

## Strengths

- **S1**: 研究问题定位精准——per-example multiplicity 在 hybrid recurrent 架构中此前未被系统研究，填补了 aggregate benchmark 分析与 per-example 效应之间的空白
- **S2**: 实验设计系统化——controlled model zoo 固定训练数据/tokenizer/hyperparameters，纯粹改变 architecture + attention ratio，是该问题的理想框架
- **S3**: 分析透明度高——诚实报告 p = .170 未 cherry-pick，21 页含丰富 sensitivity analysis（bootstrap CI、GDN exclusion、seed calibration、5-arch validation、complementarity decomposition）
- **S4**: Per-example saturation at 4% attention 是非平凡发现——仅需最少量 attention 即锁定 per-example 分化 pattern，对 hybrid 架构设计有直接指导意义
- **S5**: 五架构验证扩展（GLA + DeltaNet，10 pairwise comparisons，all J ≤ 0.14，all p < .01）增强了核心发现的鲁棒性
- **S6**: 写作质量好，figures 可读性高（特别是 Figure 1 的 aggregate-vs-per-example 对比），方法描述清晰

---

## Weaknesses

### Critical（影响接收决定）

**C1** [AGREE: R1-N1 + R2-N1] **Aggregate convergence 叙事无统计支撑，构成 framing 硬伤**

论文核心框架 "aggregate convergence masks per-example divergence" 需要 aggregate convergence 成立，但 Bonferroni-adjusted p = .170（n = 5 Spearman），10/10 benchmarks 均未达统计显著。LAMBADA 的 ρ = −1.0 是唯一单调下降但校正后仍不显著。n = 5 下 Spearman 的 power 极低——仅 |ρ| = 1.0 才能达到 p < .05，even moderate effect sizes 无法检测。

然而论文在多处将 underpowered 结果用于推断：§4.2 标题 "Aggregate Trends and Per-Example Independence" 暗示确定性结论；Conclusion 用 "aggregate metrics converge on LAMBADA"；Abstract/Introduction 间歇性使用确认性语言。

**修复方向**：重构叙事为 "architectures interchangeable by aggregate metrics actually differ substantially at per-example level"——不强调统计不显著的 convergence trend，而是强调 aggregate 分数的不可区分性（overlapping CIs）。这是更弱的前提但有更强的证据支撑。

**C2** [AGREE: R1-N2 + R2-N2] **单次训练 run 无法分离 architecture vs seed 效应**

每配置仅 1 次训练（seed 42）。论文声称 "architectural variation produces per-example multiplicity"，但无法排除 seed 效应为主要驱动因素。Appendix W 的 Pythia 70M seed calibration 存在三重 mismatch：scale（70M vs 340M/1.3B）、architecture family（Transformer vs hybrid）、accuracy regime（0.17 vs 0.50）。

R2 纠正了 R1 的数据误读：论文报告的 within-seed J = 0.273 和 J = 0.293 均为 Pythia within-seed 值（helped 和 hurt 子集），cross-architecture reference 是 J ≈ 0.10。实际 within-seed vs cross-arch 差距是 2.7×（非 R1 声称的 0.02），部分支持架构效应的独立性。但 calibration 可迁移性仍然有限。

**修复方向**：对至少一个 hybrid 架构（如 RetNet 或 HGRN2）训练 3+ 个不同 seed，直接量化 within-architecture per-example 变异。若无法实现，需大幅弱化因果归因语言。

**C3** [AGREE: R1-N3, R2 补充确认] **Bootstrap CI 基于 n = 3 架构不可靠**

3 个架构重采样仅 3³ = 27 种组合，排除退化（same-architecture triplicates）后更少。报告的 95% CI = [−1.0, −0.7] 传递与 n = 3 不匹配的虚假精度感。BCa acceleration parameter 基于仅 3 个 jackknife 值。

**修复方向**：改用 exact permutation test（3! = 6 排列）或直接报告 3 个数据点让读者自行判断。明确标注所有 bootstrap CI 为 heuristic。

### Major（影响评分但不一票否决）

**M1** [AGREE: R1-W1 + R2-W3] **Routing 作为 contribution 过于单薄**

10 benchmark 中仅 LAMBADA 有效（+5.2pp），PIQA 显著负效（−0.49pp，p = .006），HellaSwag 无效。缺少最自然的 baseline：average logits ensemble。Section 5 的 practical implications 基于 n = 1 的泛化。方法本身（confidence-based hard selection）过于简单，缺乏与 learned routing 或 calibrated ensembling 的比较。应降级为 preliminary exploration，不作为 main contribution。

**M2** [AGREE: R1-W2, R2 交叉确认] **任务分类法存在 evaluation format confound**

LAMBADA 是唯一 free-form generation task，同时显示唯一单调 σ 下降、最高 α = 0.30、唯一有效 routing。无法区分 task type vs evaluation format 的驱动作用。Multiple-choice format 机械性约束答案空间，可能降低 divergence 上界。HellaSwag 使用 acc_norm 进一步模糊与其他 Reasoning benchmark 的比较。§3.2 按 cognitive demand 分类但未讨论 evaluation format 这一混淆变量。

**M3** [分歧: R2-W1, R1 REBUT] **新颖性为增量贡献**

R2 认为核心贡献是已知框架（predictive multiplicity + ecological fallacy）在新 domain 的直接应用，方法论无创新。R1 反驳：4% saturation 和 aggregate-vs-per-example 解耦是非平凡经验发现；controlled model zoo 设定在 multiplicity 文献中罕见；Findings 不要求方法论创新。

**Director 判断**：R1 的 REBUT 有理。论文的经验贡献——特别是 4% saturation 的发现和 systematic task-dependent variation——在 Findings 标准下足够。但论文应更清楚地定位为 empirical contribution。

**M4** [AGREE: R1-W3] **Scale robustness claim 过强**

仅 340M 和 1.3B 两个 scale 点，不足以支撑 "scale-robust"。应改为 "consistent across the two scales examined"。Limitations 已提到 7B+ 但 Conclusion 的 practitioner implications 用不加限定的一般性语言。

**M5** [R2-W2, R1 部分 AGREE] **Related Work 遗漏**

- **Model Soups** (Wortsman et al., 2022 ICML)：weight-space interpolation vs architecture-space multiplicity 有直接对话关系 [R1+R2 AGREE]
- **Jiang et al. (2024)** "On the Predictive Multiplicity of Foundation Models"：将 multiplicity 扩展到 foundation models [R1 独立提出, R2 AGREE]
- MoE 文献 (Shazeer et al., 2017) 与 routing 方案有间接关联 [R2 提出, R1 AGREE with nuance]
- Fort et al. (2019) 已在论文中引用——R2 的 "missing" 指控不成立 [R1 纠正]

**M6** [R2-W4, R1 AGREE with nuance] **Abstract 过度拥挤**

~180 words 中数字密度过高（Jaccard, p, α, pp 等），降低传播效果。R2 指出第三句可能有句法拼接问题；R1 认为语法完整但同意需精简。建议保留 3–4 个关键数值，用直觉描述替代部分统计细节。

### Minor

- **m1** [R1-W4]: 5-architecture validation 仅覆盖 LAMBADA + h3-1 + 340M，应至少扩展到 HellaSwag 或 ARC-Easy
- **m2** [R1-W5, R2 AGREE]: Permutation test null baseline 不排除 example difficulty confound——attention-friendly examples 可产生 above-random Jaccard 而无需 architecture-specific 效应。建议讨论 example difficulty 作为 alternative explanation
- **m3** [R1-M1]: Abstract "approximately twice the independence baseline" 过于模糊，建议给出具体数值
- **m4** [R1-M2]: Figure 1 shaded bands (n = 3) 传达不恰当的精度感
- **m5** [R1-M4]: Table 1 confirmatory vs exploratory benchmark 缺乏视觉区分
- **m6** [R2-M4]: Limitations 未讨论 benchmark 代表性（全为 zero-shot 分类/检索，无 generation task）

---

## Reviewer Consensus [AGREE]

1. **Overall 3.0 (Findings)**——两位 Reviewer 独立给出相同评分
2. **Aggregate convergence 叙事需重构**——不依赖统计不显著的 convergence trend，改为强调 aggregate interchangeability vs per-example divergence
3. **Seed confound 是核心弱点**——需多 seed 实验或大幅弱化因果归因
4. **Bootstrap n = 3 不可靠**——改用 exact permutation 或直接报告数据点
5. **Routing 应降级**——从 main contribution 降为 preliminary exploration
6. **Format confound 需正文讨论**——LAMBADA 的 free-form 格式可能是异常表现的驱动因素

## Reviewer Divergence [REBUT]

1. **新颖性定级**：R2 认为纯增量（已知框架在新 domain 的应用），R1 认为 empirical findings（4% saturation, decoupling）有独立贡献价值。Director 判断：R1 的 REBUT 有理——Findings 不要求方法论创新，系统性经验发现足够。

---

## Questions

1. 能否对至少一个 hybrid 架构训练 3+ 个不同 seed，直接量化 within-architecture per-example 变异？
2. 能否增加一个 free-form generation benchmark（如 TriviaQA）来解耦 task type vs evaluation format？
3. Routing 实验的 cross-validation SD 是多少？如果 SD > 3pp 则 +5.2pp 增益可能不显著。
4. 为什么不对所有 benchmark 报告 majority vote 和 average-logits ensemble baseline？
5. 4% saturation 的精度受限于最低非零配置——1–3% 处是否可能有 gradual onset？

---

## Missing References

1. **Wortsman et al. (2022)** "Model Soups: Averaging Weights of Multiple Fine-tuned Models Improves Accuracy without Increasing Inference Time." ICML. [R1+R2 AGREE]
2. **Jiang et al. (2024)** "On the Predictive Multiplicity of Foundation Models." [R1 提出, R2 AGREE]
3. **Shazeer et al. (2017)** "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer." ICLR. [R2 提出, R1 AGREE with nuance]

---

## External Review (Stanford Agentic Reviewer)

未配置。

---

## Visual Layout Check（非评分项）

视觉审查已完成（2 warning, 10 info）：
- **Warning**: Pages 3–4 连续纯文本无 display item（Method §3.1–3.5），建议加入 display math 打破视觉单调性
- **Warning**: Pages 6–7 display items 过密（6 个集中 2 页），与 pages 3–4 形成节奏突变
- **Info**: Figure 1 位置合理、caption 自包含；Tables 使用 booktabs 风格规范；正文 8 页合规；appendix 表格密度高但可接受；Figure 5/6 内部文字偏小

---

## Overall Assessment

**Overall Score: 3.0 — Findings（可被 Findings 接收）**

**置信度: 4/5 (High)**

扎实的实证研究，核心 per-example 发现（Jaccard ~0.10, 4% saturation, task-dependent α = 0.14–0.30）有价值且经过严格检验。但三个 Critical 问题——convergence framing 无统计支撑（p = .170）、seed confound（每配置单次训练）、bootstrap CI n = 3 不可靠——共同削弱 claim 强度，使论文的核心叙事框架不够稳固。新颖性在 Findings 标准下足够（系统性经验发现，非方法论创新），但 routing 贡献单薄（1/10 benchmark 有效）限制了实践价值。

**提升至 Conference (3.5) 的条件**：
1. 补充同架构多 seed 实验，直接分离 architecture vs seed 效应
2. 重构叙事框架：从 "convergence masks divergence" 到 "aggregate interchangeability vs per-example divergence"
3. 增加 format-matched 的 free-form benchmark 解耦 task type vs evaluation format
4. Bootstrap CI 改用 exact permutation 或直接报告数据点

---

## Detailed Comments

### §1 Introduction
- "adding attention affects substantially different examples per architecture" 暗示因果方向，在单次 run 下不可靠，建议改为 associative 语言
- Contributions 列表中 routing 应降级或移至 supplementary finding

### §3 Method
- §3.2 Task Taxonomy：需讨论 evaluation format（free-form vs multiple-choice）作为 confound
- §3.5 Statistical Methods：bootstrap 方法在 n = 3 下应明确标注为 heuristic

### §4 Experiments
- §4.1 routing 结果需增加 cross-validation SD 和 ensemble baseline（average logits）
- §4.2 标题 "Aggregate Trends and Per-Example Independence" 暗示确定性，建议改为 "Aggregate Variance and Per-Example Overlap"
- §4.3 "scale-robust" → "consistent across the two scales examined (340M, 1.3B)"

### §5 Conclusion
- Practical implications 中 routing 建议应大幅限定范围（仅限 high-α free-form tasks）
- "when α > 0.2, per-example audit is warranted" 的 threshold 无理论基础，建议弱化为 directional guidance

### Abstract
- 精简至 3–4 个关键数值，用直觉描述替代部分统计细节
- 检查第三句是否有句法拼接问题