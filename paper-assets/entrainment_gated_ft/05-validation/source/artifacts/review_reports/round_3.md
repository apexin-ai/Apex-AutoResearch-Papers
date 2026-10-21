---
round: 3
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-20T10:35:07.673081+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告：Task-Specific Convergence and Per-Example Predictive Multiplicity in Hybrid Recurrent Architectures

**目标 venue**: EMNLP 2026 (ARR May 2026 cycle)
**投稿类别**: Long Paper
**审稿人**: Reviewer 1 (方法严谨性+实验设计+统计分析), Reviewer 2 (新颖性+完整性+相关工作+论文组织)
**审稿轮次**: 1 轮独立审稿 + 交叉分享，关键问题已收敛

---

## Summary

本文使用 Wang et al. (2025) 的 controlled model zoo（GatedDeltaNet, RetNet, HGRN2 三种线性循环架构 × 5 种 attention ratio × 2 种 scale: 340M/1.3B），在 10 个 benchmark 上分析 attention 对跨架构一致性的影响，在 LAMBADA (N=5,153) 和 ARC-Easy (N=2,376) 上做 per-example 分析。三个发现：(1) aggregate convergence 仅在 LAMBADA 上出现 (ρ=−1.0, Bonferroni-adjusted p=.100)；(2) convergence 依赖 scale（1.3B 完全，340M 非单调）；(3) per-example predictive multiplicity 普遍存在（α≈0.21-0.30），与 aggregate convergence 解耦。

## Strengths

**S1. Controlled experimental design** [R1-S1, R2 同意]
利用统一训练条件的 model zoo 隔离架构差异为唯一变量，实验设计优于 ad-hoc 模型比较。

**S2. Two-level analysis with decoupling** [R1-S2]
Aggregate convergence 与 per-example divergence 的 decoupling（§4.4）是本文最有价值的贡献——aggregate σ 下降 79% 而 per-example Jaccard 在 4% attention 即饱和，两者时间尺度分离。对部署决策有实际意义。

**S3. Transparent statistical reporting** [R1-S3, R2 同意]
主动报告 adjusted p 不显著、bootstrap CI 局限、Bonferroni/BH 校正细节。Limitations section 诚实全面，覆盖统计功效、scope、scale、架构覆盖等。

**S4. Thorough appendix** [R1-S5, R2 同意]
10+ 子分析覆盖 normalized Jaccard ES、within-arch stability、cross-scale comparison、Transformer entrainment、confidence margin 等。

**S5. Per-example decomposition framework** [R2]
Helped/hurt/unchanged 分类 + Jaccard overlap + ambiguity α 组合提供了有方法论参考价值的分析框架。

## Weaknesses

### Must-Fix（影响接收决定）

**[W-CITE] wang2025hybrid 引用 arXiv ID 与实际论文不匹配** [Critical, R2 发现, R1 [AGREE]]
references.bib 中 arXiv:2507.06457 的标题为 "Scaling Laws for Hybrid Language Models" (Junxiong Wang et al.)，但实际该 arXiv ID 对应 "A Systematic Analysis of Hybrid Linear Attention" (Dustin Wang, Rui-Jie Zhu et al.)——标题和第一作者均不匹配。OpenAlex 验证为 not_found。全文引用 8 次，是全部 30 个模型配置的数据来源。**严重影响可追溯性和可复现性。**

**[W-CHECKLIST] 缺少 ARR Responsible NLP Research Checklist** [Critical, R2 发现, R1 [AGREE]]
ARR 自 2024 年 12 月起强制要求 Responsible NLP Checklist 作为提交的一部分。论文有 Limitations 和 Ethics Statement，但不能替代 checklist。缺失直接触发 desk rejection。

**[W-OVERCLAIM] 核心 convergence claim 未通过多重检验校正，framing 与 evidence 存在系统性落差** [Critical, R1-W1≡R2-N3, 双方 [AGREE]]
- LAMBADA convergence: Bonferroni-adjusted p = .100 > α = .05; BH-adjusted p = .102 类似。排除 GDN 后 ρ 从 −1.0 降至 −0.7 (p = .233)。
- n=5 × Bonferroni 6-way 在数学上不可能达到 α = .05（最小可达 adjusted p = 0.100），这是分析框架的根本性设计约束。
- n=3 architecture-level bootstrap CI（至多 27 unique resamples, 11.25% degenerate）Appendix B.1 自称 "heuristic indicators"，但 abstract 将 "BCa 95% CI [−1.0, −0.7]" 呈现为标准推断证据。
- 标题 "Task-Specific Convergence" 和 Introduction 以 "79% reduction" 为 hook，暗示已确认发现。
- **论文统计报告本身诚实（§4.1 明确写了 adjusted p 不显著），问题在 abstract/title 的 framing 层面。**

**[W-GENERAL] "General property" claim 基础过窄** [Critical, R1-W2≡R2-W3, 双方 [AGREE]]
- Abstract/Conclusion 声称 "predictive multiplicity is a general property of hybrid architectures"，但仅基于 2 benchmark × 3 架构 × 1 model zoo。
- R2 指出 benchmark 选择可能存在 selection bias：LAMBADA 是 10 个中唯一有 convergence 的（便于展示 decoupling），ARC-Easy 在 mixed 类别中 σ ratio 最高 (7.70)。
- Jamba/RWKV-6/Hymba/Mamba-3 使用不同 mixing strategy，可能产生不同 pattern。Limitations 承认但 abstract/conclusion 未弱化。

### Should-Fix

**[W-GDN] GDN head-count confound 实质性影响核心结果** [Major, R1-W4≡R2-W4, 双方 [AGREE]]
GDN h3-1 使用 16 attention heads（其他配置为 32）。移除 GDN 后 LAMBADA ρ 降至 −0.7，且 MMLU ρ 从 −0.7 反转为 +0.6（R2 补充），说明 confound 影响不限于 LAMBADA。§4.5 Robustness 部分缓解（RetNet-HGRN2 pair 保留 decoupling），但关键 sensitivity 数据仅在 appendix 报告。

**[W-NOVELTY] 新颖性有限** [Major, R2-W1, R1 [PARTIALLY AGREE]]
核心贡献是将 Marx et al. (2020) predictive multiplicity 从 seed variation 扩展到 architectural variation。与 D'Amour et al. (2022)、Fehlauer et al. (2025) 相比概念增量有限。没有新度量、新方法或新理论。R1 部分反驳：§4.4 decoupling 发现本身有一定新颖性，揭示了 hybrid model 文献中此前未注意到的现象。

**[W-REFS] 遗漏多篇重要近期相关工作** [Major, R2-W2, R1 [AGREE]]
见 Missing References 部分。特别是 "Cross-Model Disagreement as Label-Free Correctness Signal" 与 §4.3 高度重叠，"Hidden Attention of Mamba Models" 与 Appendix D 直接相关。

**[W-ZOO] 完全依赖单一外部 model zoo** [Major, R1-W6, R2 [REBUT: 有争议]]
30 个模型全部来自 Wang et al.，论文未训练任何模型。R2 反驳：controlled design 本身是方法论优势（隔离架构差异），D'Amour et al. 和 MultiBERTs 也使用预定义 model suite。最终判断：使用 model zoo 是合理选择，但应更明确讨论此设计选择的 trade-off。

**[W-BINARY] Binary helped/hurt 分类丢失概率信息** [Major→Minor 有争议, R1-W5, R2 [REBUT]]
R1 认为概率从 0.49→0.51 与 0.01→0.99 被同等对待是 Major 问题。R2 反驳降为 Minor：Appendix J 已有连续概率分析（Cohen's d = 0.73-0.92）与 binary 结论一致；Marx et al. 框架本身基于 discrete disagreement。建议添加 probability-gap-weighted Jaccard 作为 robustness check。

## Reviewer Consensus [AGREE]

1. **Overall 3.0 (Findings)** — 两位 Reviewer 独立给出相同评分
2. 统计 overclaiming 是最核心问题（Bonferroni p=.100 + n=3 bootstrap + framing 张力）
3. Generality claim 基础过窄（2 benchmark × 3 架构）
4. wang2025hybrid 引用错误严重影响可追溯性
5. 缺少 ARR checklist 可能触发 desk rejection
6. GDN confound 应在正文讨论而非仅 appendix
7. 方向有价值，decoupling 有一定学术贡献
8. 统计报告本身透明诚实，问题在 abstract/title framing

## Reviewer Divergence [REBUT]

1. **Binary classification severity** — R1: Major (主方法论应整合概率信息); R2: Minor (Appendix 已有连续分析且 Marx 框架基于 discrete)
2. **Model zoo dependency** — R1: Major weakness (无独立验证); R2: 优势兼限制 (controlled design 是方法论优势)

两个分歧均为严重级别判断，非实质性分歧。

## Questions for Authors

1. Table 1 LAMBADA p=.017 × 6 = .102，论文报告 .100。请澄清是四舍五入还是不同校正。[R1-Q1, R2 [AGREE]]
2. Jaccard 统计显著（p < .0001, z > 5.9）但 normalized ES 仅 5-7% of achievable maximum——如何协调统计显著性与如此小的实际效应量？[R1-Q2, R2 [AGREE]: significance 和 ES 回答不同问题，但正文对此张力处理不足]
3. Transformer entrainment Δ = 0.005-0.029 极小，是否在 noise range 内？有无 effect size 解释？[R1-Q3, R2 [AGREE]]
4. lm-evaluation-harness default prompts 是否在所有架构和 attention ratio 间保持一致？有无 prompt-sensitivity check？[R1-Q4, R2 [AGREE]: per-example 分类可能对 prompt 敏感]
5. Model zoo checkpoints 是否来自独立训练 run？若每配置仅 1 checkpoint，无法区分 architecture effect 和 seed effect。[R1-Q5, R2 [AGREE]: 直接影响核心论点]

## Missing References

| 论文 | 相关性 | Reviewer |
|------|--------|----------|
| Reconciling Model Multiplicity for Downstream Decision Making (ICLR 2025) | 直接处理 predictive multiplicity 决策后果 | R2 |
| Resolving Predictive Multiplicity for the Rashomon Set (arXiv 2601.09071, 2026) | Rashomon set 理论进展 | R2 |
| Cross-Model Disagreement as Label-Free Correctness Signal (arXiv 2603.25450, 2026) | 跨模型 per-example 分歧应用，与 §4.3 高度重叠 | R2, R1 特别支持 |
| The Hidden Attention of Mamba Models (ACL 2025) | SSM attention 分析，Appendix D 不引用不合理 | R2, R1 特别支持 |
| Mamba-3 (ICLR 2026) | 最新 hybrid architecture | R2 |

## External Review (Stanford Agentic Reviewer)

未配置外部审稿（项目未启用 `external_review.paperreview_ai`）。

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 7 info）：

**Warnings:**
- **页 3-5**：连续 3 页纯文本（Related Work + Method），无 display item。Method 部分的 model zoo 设计或 per-example decomposition 流程可用示意图打破纯文本节奏。
- **页 1-8**：主文仅 4 个 display items（2 figure + 2 table），对于涵盖 10 benchmarks × 3 architectures × 5 ratios × 2 scales 的实证论文偏少。§4.3 Per-Example Divergence 和 §4.4 Decoupling 核心发现缺少可视化支撑。

**Info:**
- Figure 1 axis tick labels 字号偏小（约正文 60-65%）
- Figure 2 数据点 marker 区分度一般，建议颜色编码 task category
- Table 2 缺少最优值加粗标注
- Appendix 单页堆叠 4+ 表格，部分可合并
- 主文无 display-math equation，核心度量 inline 呈现，形式化定义用 display equation 更清晰
- 末页约 40% 空白

## Overall Assessment

**Overall Score: 3.0 — Findings（可被 Findings 接收）**
**置信度: 4/5**

| 维度 | R1 | R2 | 共识 |
|------|-----|-----|------|
| Soundness | 2.5/5 | 3/5 | 2.75 |
| Excitement | 2.5/5 | 2/5 | 2.25 |
| Reproducibility | 4/5 | 4/5 | 4.0 |
| Confidence | 4/5 | 4/5 | 4.0 |

**判断依据：**

研究问题有价值——hybrid recurrent architecture 中 attention 如何影响 per-example 行为是实际部署决策问题。Controlled model zoo 实验设计合理，aggregate-vs-per-example decoupling 发现有一定学术贡献。但存在多个阻碍 Conference (4.0) 接收的问题：

1. **统计 claims 与 evidence 系统性落差**：核心 convergence claim 在 Bonferroni 和 BH 校正下均不显著（p≈.100），且 n=5 × 6-way correction 在结构上无法达到 α=.05。Bootstrap CI 基于 n=3 无形式化保证。Abstract/title 的 framing 与 §4.1 的诚实报告不一致。
2. **Generality claim 证据不足**：2 benchmark × 3 架构 × 1 model zoo，benchmark 选择可能存在 selection bias。
3. **关键引用错误**：wang2025hybrid arXiv ID 对应不同论文，影响全文核心数据源的可追溯性。
4. **格式合规缺陷**：缺少 ARR 强制 Responsible NLP Checklist，desk rejection 风险。
5. **新颖性有限**：主要是已知框架（predictive multiplicity）在新场景（architectural variation）的 application。

**修改建议优先级：**
1. [紧急] 修复 wang2025hybrid 引用 + 填写 ARR checklist（desk rejection 风险）
2. [核心] 显著弱化 convergence/generality claims 的 framing（abstract、title、introduction）
3. [重要] GDN sensitivity 关键数据纳入正文
4. [建议] 补充 5 篇遗漏引用 + 补充更多 benchmark per-example 分析

如能修复引用和 checklist、显著弱化 claims，可达 Findings 接收水平。达到 Conference (4.0) 需要更 substantial 的方法论创新（如新 multiplicity metric）或更广泛的实验验证（更多 benchmark/架构）。

## Detailed Comments

### §1 Introduction
- 开篇以 "79% reduction" 为 hook 强劲有效，但需在首次提及时即 qualify adjusted p 不显著
- Contribution 列表清晰，但第三条 "general property" 需弱化措辞

### §2 Related Work
- 六个 paragraph 覆盖全面，分组合理
- 遗漏 5 篇重要近期工作（见 Missing References）
- Ensemble Diversity paragraph 与主论点关联可更紧密

### §3 Method
- Model zoo 描述清晰，task taxonomy 有价值
- Bootstrap CI caveat 应更 prominent（目前在 §3.5 最后一段）
- 结构性限制（n=5 无法通过 Bonferroni at k=6）应在此处明确而非仅在 Limitations

### §4 Experiments
- §4.1: Table 1 是论文最有信息量的 display item。建议脚注解释 p=.017→adjusted .100 的计算
- §4.2: "Preliminary observation" 措辞正确，与 Introduction 措辞需保持一致
- §4.3: Per-example decomposition 分析扎实。Cross-task generalization 到 ARC-Easy 是重要补充
- §4.4: Decoupling 是核心贡献。缺少可视化（仅靠 Figure 1 和文字描述），建议增加 per-example Jaccard trajectory 图
- §4.5: Robustness 应包含 GDN exclusion 关键数据（目前仅引用 Appendix）

### §5 Conclusion
- 合理总结三个发现
- "General property" 和 ensemble 建议需基于更充分的证据 qualify

### Limitations
- 六个 limitation 全面诚实
- "Statistical power" paragraph 应升级为承认结构性设计约束

### Appendix
- 10 section 分析详尽，是论文的重要资产
- Appendix J (Confidence Margin) 值得在正文给更多篇幅
- 建议合并部分小表格优化排版

### References
- [Critical] wang2025hybrid arXiv ID 不匹配，必须修复
- damour2022underspecification 年份应为 2020
- gao2024lmeval 引用格式不规范（@misc），建议使用 Zenodo DOI

---

⚠️ **Deadline 告警**：提交信息称 "ARR June 2026, deadline June 15"，但 EMNLP 2026 官方 CFP 要求通过 **ARR May 2026 cycle** 提交（deadline: May 25, 2026），且 2026 年 ARR 不存在 June cycle。请核实。