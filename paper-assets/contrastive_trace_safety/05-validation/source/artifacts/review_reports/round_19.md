---
round: 19
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-19T14:10:54.466388+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# Round 19 审稿报告

**论文**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: EMNLP 2026 (ARR May 2026 cycle), Long paper
**审稿日期**: 2026-05-19
**Reviewer 编排**: R1（方法严谨性）, R2（新颖性/完整性）
**交叉回应**: R2 对 R1 的 8/8 问题 [AGREE]；R1 对 R2 的 6/7 问题 [AGREE]，1 个 [REBUT]（R2-N1 novelty）
**收敛轮次**: 1 轮（关键问题已充分收敛）

---

## Summary

本文研究了 reasoning model（chain-of-thought）在自我越狱场景下，hidden-state (HS) probes 与 text probes 检测 safety commitment point (CP) 的能力对比。核心方法论发现：layer selection metric 的选择可以完全逆转 HS vs. text 的比较结论——crossing-rate composite metric 因浅层表征压缩而系统性选择浅层，掩盖了深层存在的 HS advantage。在 4 个 reasoning models（2 架构、2 scale）上的实验表明，HS advantage 在 7-8B scale 上经 nested CV 验证，在 32B 上仅为探索性，且随 text encoder 质量提升而衰减（384d: 4/4 HB → 1024d: 1/4 HB）。系统性负面结果排除了 7 种替代检测方法。

---

## Strengths

**S1. Layer selection sensitivity 是一个扎实的方法论发现。**
Table 2 和 Figure 1 清楚展示了 CR-composite（选 L2/L10）vs threshold-based（选 L63）的 59 层差距如何逆转 32B 的 HS advantage 结论。Random-label decomposition（Appendix B.1）独立证明浅层偏差是 label-independent 的几何性质，cosine volatility analysis（Appendix C）提供了 mechanistic explanation。这一发现对所有使用 hidden-state probing 的研究有直接 actionable 的警示价值。[R1, R2 共识]

**S2. 统计方法和报告透明度远超该领域平均水平。**
HB 校正、BCa bootstrap、exact permutation test、nested CV、multi-seed stability、control task selectivity、PCA capacity matching、random projection——多个正交控制从不同角度验证 signal 真实性。Bug disclosure（Appendix G）、garden-of-forking-paths acknowledgment（Section 3.3）、evidence gradient 分级、32B † 标记——论文的 intellectual honesty 使审稿人可以准确评估每个 claim 的证据强度。[R1, R2 共识]

**S3. 系统性负面结果有指导价值。**
Table 5 排除了 BOCPD/CUSUM/Mahalanobis/RepE/MLP/CCS/cross-transfer 7 种方法，每种失败模式提供了关于 commitment signal 性质的信息（directional, gradual, model-specific, linearly separable）。这对后续研究的方法选择有实际指导意义。[R1, R2 共识]

**S4. Nested CV（7-8B）提供可靠验证。**
10/10 folds 一致支持 HS advantage，shrinkage 在可接受范围内（13-25%），对 7-8B 的 claim 提供了坚实支撑。[R1, R2 共识]

**S5. Random-label decomposition 设计巧妙。**
Appendix B.1 将 metric disagreement 分离为几何 artifact（crossing rate 侧）和真实安全信号（threshold-based 侧），是论文中最有说服力的实验设计。[R2 提出, R1 共识]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [R1-N1] Bootstrap 重采样单元错误：step-level 重采样违反独立性假设** [R1 提出, R2 AGREE]

Section 3.5 明确采用 step-level resampling，但同一 trace 内 steps 存在强时间自相关（probe scores 在 CP 附近近似单调递增）。Step-level bootstrap 人为膨胀有效样本量，导致 CI 过窄、p-values 过于乐观。

- 32B 有 exact permutation test（trace-level, Appendix C）部分缓解，p-values 与 bootstrap 一致
- 7-8B（R1-8B n=43, OT-7B n=47）缺少 trace-level permutation test
- R1-8B FPR（rank 12/12, p=0.044, 3/5 seeds HB）是最可能在 trace-level bootstrap 下翻转的结果
- Nested CV（Appendix N）在 trace level 操作，间接提供 trace-level 证据，但测试的是不同假设

**要求**：改用 cluster bootstrap（trace 为重采样单元）重新计算所有 CI 和 p-values；为 7-8B 补充 trace-level permutation test；报告两种方案的结果差异。

**MF2. [R1-N2] Threshold-based metric 收敛证据被系统性高估** [R1 提出, R2 AGREE（部分）]

Precision、inverse FPR、additive composite 共享同一 2×2 混淆矩阵（2 自由度），论文自身承认（Section 3.3）但随后仍在 Section 4.2 反复强调 "three of four metrics excluding crossing rate consistently select deep layers"，给读者造成三条独立证据的印象。

- 实际独立来源 = 2：BA（threshold-free）+ 一个 threshold-based metric
- BA 在 60/20/20 下确实也选了 deep layers（QwQ-32B: L63, R1-32B: L46），layer selection finding 本身成立
- 但论证强度被高估：应重构为 "threshold-based metrics converge (sharing confusion matrix) and BA independently confirms"

**要求**：明确承认 threshold-based metrics 间的数学依赖；重构论证为 BA 独立确认 + threshold-based 收敛。

**MF3. [R1-N3] 32B 验证集极端小样本下超参数选择可靠性** [R1 提出, R2 AGREE]

验证集 per-class 仅 4-9 个样本，从 64 layers × 7 W = 448+ 配置中选最优。LOO-CV 选层跨越 24 层（QwQ: L39-L63）。R1-32B 仅 W=1 显著（coverage 25%, 5/20 traces），缺 joint (layer, W) stability 分析。

**要求**：对 R1-32B 补充 joint (layer, W) stability；报告 L55-L63 range 变异；更显著降低 32B claim 强度。

**MF4. [R2-N1] 核心贡献新颖性边际** [R2 提出, R1 REBUT — 未解决分歧]

R2 认为 "layer selection matters" 已有广泛认知（Tenney 2019, Jawahar 2019, Belinkov 2022），crossing rate 偏差范围窄，遗漏 Pais et al. 2026（multi-layer ensembling）同期工作。R1 反驳：具体机制（crossing rate × 浅层压缩可逆转结论）此前未被表征，random-label control 证明可推广性，problem diagnosis 与 solution 互补而非替代。

**Director 判断**：R1 的反驳有一定道理——"可逆转结论的方法论陷阱"与"不同层有不同信息"确实有实质差距。但 R2 对贡献范围窄度的担忧也合理。综合评估：Contribution 1 的新颖性足以支撑 Findings 但不够 Conference 主会议，除非在更多任务/数据集上验证普遍性。

**MF5. [R2-N2] 单一数据集严重限制泛化性** [R2 提出, R1 AGREE]

所有实验仅用 HarmThoughts 一个数据集，无 IAA，无 category 分层。"Establish the observational foundation" 声明过于强大。R1 补充：layer selection sensitivity 对数据集依赖较低（来自 representation geometry），Contribution 1 泛化性应强于 Contribution 2。

**要求**：降低 foundational claim 力度；明确区分两个 contribution 的泛化条件。

**MF6. [R2-N3] 架构同质性削弱 "across architectures" 声明** [R2 提出, R1 AGREE]

4 模型中 3 个基于 Qwen。Abstract 有 caveat 但 "spanning two architectures" 仍过强。

**要求**：修改 framing 为 "primarily Qwen-based, with one Llama model for limited cross-architecture evidence"。

### Should-Fix（影响评分但不一票否决）

**SF1. [R1-W1] Nested CV 与 main-text layer selection 不一致** [共识]
OT-7B nested CV 选 L21-27 vs main text L16，shrinkage 25%。应在 main text 讨论，报告 shrunk estimates。

**SF2. [R1-W2] HB 校正范围不足** [共识]
HB 仅校正最终 12 个测试，未覆盖 layer metric/W/K/evidence tier 选择的累积 researcher degrees of freedom。应更明确区分 confirmatory vs exploratory findings。

**SF3. [R1-W3] Position residualization 仅线性** [共识]
仅回归 t/T，CP 附近可能有非线性效应。3/4 模型线性 residualization 后仍显著（+3.7 to +6.9pp HB），严重性中等。建议补充二次项或 spline basis。

**SF4. [R1-W4 / R2-W3] Encoder-quality boundary framing 不足** [强共识]
MiniLM 4/4 HB → E5 2/4 HB → BGE 1/4 HB 单调递减。Discussion 坦诚但 title/abstract/intro 过度强调 HS advantage。应在 abstract 中更早、更显著地呈现 encoder-quality boundary。

**SF5. [R1-W5] Evidence gradient 术语不一致** [共识]
Section 4 "strong/moderate/qualified" vs abstract "confirmed/significant-but-position-competitive/exploratory"，三套术语造成困惑。应全文统一，定义明确分级标准。

**SF6. [R2-W1] 遗漏重要相关工作** [共识]
Pais et al. 2026（multi-layer ensembling）, HiddenDetect (Jiang et al., ACL 2025), SafeInt (EMNLP 2025 Findings), RCS (ACL 2026)。特别是 Pais et al. 提供了互补的解决方案视角。

**SF7. [R2-W2] Abstract/Conclusion claims 过强** [共识]
探索性 32B 结果（†, n≤20）与 confirmed 7-8B 并列；† 含义仅在 Section 4.1 定义；R1-8B "confirmed" 不准确（FPR 3/5 HB）。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致：
- [AGREE] Bootstrap 重采样单元需要修正（MF1）
- [AGREE] Threshold-based metric 收敛证据被高估，但 BA 独立确认 deep-layer selection（MF2）
- [AGREE] 32B 超参数选择不可靠，结论应更保守（MF3）
- [AGREE] 单一数据集是严重局限（MF5）
- [AGREE] 架构同质性高估了多样性声明（MF6）
- [AGREE] Encoder-quality boundary 削弱 HS advantage，framing 需调整（SF4）
- [AGREE] Evidence gradient 术语应统一（SF5）
- [AGREE] 缺失相关工作应补充（SF6）
- [AGREE] Claims 与 evidence 强度应更匹配（SF7）

## Reviewer Divergence

**MF4. 贡献新颖性**（唯一未解决分歧）：
- **R2（3.0）**：crossing rate 偏差范围窄，"don't use a bad metric" 不够主会议新颖性
- **R1（3.5）**：具体机制此前未表征，"可逆转结论的陷阱"有独立价值，random-label control 支持推广性
- **Director 判断**：分歧合理，综合评估为 Findings 水平。如能在更多任务上验证普遍性可升至 Borderline Conference。

---

## Questions

1. 如果改用 trace-level cluster bootstrap 重新计算，R1-8B FPR（当前 p=0.044）是否仍然显著？
2. OT-7B 在 nested CV 独立选择 L21-27 而非 L16——如果 main text 改用 nested CV 选层报告结果，precision advantage 的 shrinkage 幅度是否改变结论方向？
3. 非线性 position residualization（如 t² 或 spline）后，QwQ-32B 的 +3.7pp residualized gap 是否仍然显著？
4. Pais et al. 2026 的 multi-layer ensembling 方法应用于本文的 safety commitment detection 时，是否能消除 layer selection sensitivity 问题？

---

## Missing References

以下由 R2 通过 web search 发现，R1 确认相关性：
1. **Pais et al. (2026)** "Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling" (arXiv:2604.13386) — deception directions 在层间旋转，multi-layer ensembling 解决单层 probe 脆弱性
2. **HiddenDetect** (Jiang et al., ACL 2025, arXiv:2502.14744) — VLM hidden state jailbreak 检测，安全信号在中-深层
3. **SafeInt** (EMNLP 2025 Findings, arXiv:2502.15594) — representation intervention jailbreak 防御，涉及 layer-specific safety probe
4. **RCS** (Representational Contrastive Scoring, ACL 2026, arXiv:2512.12069) — 内部表征对比方法 jailbreak 检测，包括 Mahalanobis-based 检测器

---

## External Review (Stanford Agentic Reviewer)

外部审稿：**未配置**（项目无 external_review.paperreview_ai.enabled 设置）

---

## Visual Layout Check（非评分项）

视觉审查：**未启动**（review_paper_pdf_path 未配置，无编译 PDF 可用）

建议：编译论文 PDF 后配置路径，下轮审稿可派发视觉审查。

---

## Overall Assessment

**评分：3.0 — Findings**
**置信度：4/5**（两位 Reviewer 在方法论和 presentation 问题上高度一致，唯一分歧为新颖性评估，Director 综合判断倾向 R2）

### 评分依据

**支撑 Findings 的因素：**
- Layer selection sensitivity 是一个真实且有价值的方法论发现，对 probing 社区有 actionable 警示
- 统计方法和报告透明度远超领域平均，体现优秀的科学实践
- 系统性负面结果对后续研究有指导价值
- 7-8B 的 HS advantage 经 nested CV 验证是可靠的

**阻碍 Conference 的因素：**
- Bootstrap 重采样单元选择存在基础性统计问题（MF1）
- 单一数据集 + 无 IAA + 无 category 分层限制泛化性（MF5）
- 3/4 模型同一架构，cross-architecture 证据不足（MF6）
- Encoder-quality boundary 显示 HS advantage 是当前 text encoder 限制的产物而非内在模态优势（SF4）
- 32B 结果在当前样本量下仅为探索性，但 framing 不够保守（MF3, SF7）
- Contribution 1 的具体新颖性范围窄（MF4，分歧项）

### 改进路径

若以下修正到位，可升至 **3.5 (Borderline Conference)**：
1. 修正 bootstrap 重采样单元（MF1）且核心结论不变
2. 重构 metric 收敛论证（MF2）
3. 降低 32B claim 强度至 evidence 匹配水平（MF3）
4. Abstract/Conclusion 更诚实地反映 encoder-quality boundary 和架构同质性（MF6, SF4, SF7）
5. 补充缺失相关工作（SF6）

---

## Detailed Comments

### Section 1 (Introduction)
- "spanning two architectures" → 改为 "primarily Qwen-based (3/4 models), with one Llama model"
- "establish the observational foundation" → 降低为 "provide initial characterization" 或 "characterize on one benchmark"
- +19.2pp (QwQ†) 与 +20.1/+21.9pp (7-8B) 并列给读者等价印象，建议拆分为 confirmed 和 exploratory 两句

### Section 3.3 (Layer Selection Sensitivity)
- "the ablation diagnoses which aspect drives layer selection bias" — 应明确承认 precision/inv-FPR/additive 非独立
- Garden-of-forking-paths acknowledgment 良好，但应量化或至少列出完整的 researcher degrees of freedom 清单

### Section 3.5 (Evaluation Protocol)
- "resampling at the step level within each trace" — 这是需要修正的核心统计问题
- 建议改为 trace-level cluster bootstrap，同时报告 step-level 结果供比较

### Section 4.1 (Layer Selection Results)
- "Three of four metrics excluding crossing rate consistently select deep layers" — 重构论证（见 MF2）
- Table 2 caption 中的 p-values 应移入表格本身

### Section 4.2 (HS vs Text)
- Table 3 的 CI 基于 step-level bootstrap，修正后需更新
- R1-8B "confirmed" 标签需按 metric 细化（precision/BA confirmed, FPR fragile）
- 18/20 model-seed pass 掩盖了 R1-8B FPR 的系统性弱点

### Section 4.3 (32B Analysis)
- R1-32B residualized gap +1.9pp (p=0.914) 远低于 MDE (9.5pp) → 应更突出此限制
- QwQ-32B position margin +4.5pp (p=0.133) 同样 underpowered

### Section 5 (Discussion)
- "We propose—but have not validated—a multi-metric audit protocol" — 未验证的提议不应计为贡献
- Encoder-quality boundary 讨论坦诚，但 implication（HS advantage 可能是暂时的工程限制）应在 abstract 中反映

### Section 7 (Limitations)
- 全面且诚实。建议增加：(1) step-level bootstrap 的独立性假设问题；(2) threshold-based metrics 间的数学依赖

### Appendix
- Figure 1 (heatmap) 单栏宽度过小，4×5 grid 标签难读 → 建议 full-width
- Table 3 caption 过密（7 行 + 4 脚注）→ 建议拆分为 table note
- 代码建议在 submission 阶段提供 anonymous repository

### Minor Issues
- `geiger2025causal` 标注 year=2025，但 JMLR 发表于 2023 → 核实并更正
- Section 4 para 1 定义 "strong, moderate, qualified" 三级，但 "moderate" 在全文未被使用
- Section 3.1 定义 CP 为永久性的 binary transition，但 Section 7 承认有 oscillating patterns → 应说明这些 traces 的处理方式
