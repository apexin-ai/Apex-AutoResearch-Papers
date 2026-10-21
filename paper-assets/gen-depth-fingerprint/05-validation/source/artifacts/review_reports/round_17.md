---
round: 17
overall_score: 3.0
timestamp: 2026-05-18T10:39:02.463437+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 18

**论文**: Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains
**Venue**: EMNLP 2026 via ARR May 2026 cycle (deadline: 2026-05-25)
**Reviewer 编排**: R1（方法严谨性 + 实验设计）+ R2（新颖性 + 完整性 + 写作质量）
**交叉回应**: 已完成（R1 ↔ R2 全部逐条回应）

---

## Summary

本文提出 generation depth classification，将 LLM 递归生成文本检测从 binary (real vs. synthetic) 推进到 3-class (gen-0 / gen-1 / gen-2+)。核心发现是 Differential Depth Response (DDR)：7 个标准统计特征在递归生成中呈现三分响应模式（3 drifting / 1 intermediate / 3 near-stationary），使用 XGBoost 在 8 个 base model 生成器的 Leave-One-Generator-Out 评估下达到 leak-free binary F1 = 0.694。论文实验设计严谨、消融全面，但方法论新颖性有限、DDR 被过度包装为 "framework"、标题与实际能力不匹配、且仅限 base model 的约束严重限制实际影响力。

---

## Strengths

**S1. 问题定义新颖且有意义。** Generation depth classification 是对 binary detection 的自然且有价值的推进。在数据溯源和合成数据管理中有潜在应用价值。没有 prior depth-classification 方法存在，方向确实是新的。[R1, R2 共识]

**S2. 严谨的实验设计和统计方法。** LOGO 交叉验证设计合理；8 个生成器覆盖 5 个模型族；bootstrap CIs、Bonferroni correction、TOST equivalence testing、class-balanced subsampling 等统计工具使用规范。主动识别并处理 gen-0 seed sharing 问题（采用 binary F1 作为 primary metric）。[R1, R2 共识]

**S3. 全面且诚实的消融分析。** 12 页附录覆盖 length confound、prompt type、5-class granularity、QLoRA、LOFO、classifier sensitivity、robustness to perturbation、cross-domain、error analysis、downstream utility、feature distributions、cross-temperature 等。每个消融有明确目的且在正文中有引用。[R1, R2 共识]

**S4. 坦诚的 Limitations。** 主动承认 base-model restriction、instruction-tuning degradation (F1=0.338)、temperature sensitivity、3-class ceiling、reference model dependency 等限制。在同类论文中不常见。[R1, R2 共识]

**S5. Concurrent work 定位清晰。** §2.2 对 Broken Telephone 和 Markovian Chains 的区分论述有效（open-ended continuation vs. paraphrastic/feedback loop），且指出两个独立工作收敛于 ~3 class ceiling 的互补解释。[R1 Strength 6]

**S6. 写作质量合格。** AI 痕迹不明显（无 em-dash 滥用、-ing phrase 结尾少、过渡词使用适度），格式基本合规（8 页正文、匿名、行号、ACL template）。[R2 写作检查]

---

## Weaknesses

### Must-Fix（3 项，影响接收决定）

**MF1 [critical, consensus] DDR "framework" overclaim + 阈值论证不足**
- R1-N1 提出，R2 AGREE
- |ρ| > 0.60 / |ρ| < 0.10 的分组阈值缺乏理论依据（Cohen d benchmarks 不适用于 Spearman ρ）
- N=7 特征分成 3/1/3，intermediate 仅 entropy_std 一个成员，不足以建立 "framework"
- Levene test 拒绝等方差但论文用 CV shift 辩护，需要 TOST equivalence testing（论文在 Appendix M 已对 downstream 使用 TOST，可一致化）
- **要求**：(a) 对 ρ 阈值做 sensitivity analysis (±0.10)；(b) 对 near-stationary 特征用 TOST；(c) 将 DDR 从 "framework" 降级为 "empirical pattern"

**MF2 [critical, consensus] "Fingerprinting" 标题与 3-class 实际能力不匹配**
- R1-N3 提出，R2 AGREE（R2 自身 W1 同点）
- Binary F1 = 0.694 意味着 ~30% 错分率；per-generator F1 跨度 0.633-0.724；5-class F1 仅 0.50（gen-2/gen-3 各 0.259）
- "Fingerprinting" 在安全/取证语境意味着高可靠性识别，与实际性能不符
- Conclusion "three classes = practical ceiling" 与标题矛盾
- **要求**：将 "Fingerprinting" 改为更准确的措辞（如 "Depth Classification" / "Depth Profiling"）；在 Abstract 声明 3-class 粒度限制

**MF3 [critical, consensus] 方法论新颖性不足 + 贡献定位需调整**
- R2-N1 提出，R1 AGREE
- 7 个特征均为标准统计量（NLL 基本矩/分位数 + 经典 stylometry），XGBoost 无改进
- Baseline 均为 binary detection 方法（无 prior depth classification method 可比较），限制了 competitive comparison 的意义
- R1 补充：贡献定位应为 "empirical discovery + feasibility demonstration"，问题定义的新颖性有价值
- **要求**：明确定位为 empirical study / phenomenon paper，降低方法创新声称；在 §1 contribution list 中区分 "task formulation" 和 "empirical finding"

### Should-Fix（7 项，影响评分但不一票否决）

**SF1 [critical, consensus] Base-model-only 约束限制实际影响力，scope 声明不足**
- R2-N2 (Must-Fix) + R1-W2，两位均标记
- OLMo-Instruct LOGO F1 = 0.338 接近 random；instruction tuning reverses ρ from -0.6 to +0.2~+0.5
- Abstract 未提及 base-model restriction；Introduction §1 L15 有提及但位置偏后
- 现实中递归生成更可能发生在 instruction-tuned models 上
- **要求**：Abstract 中声明 base-model restriction；正文纳入 instruction-tuned 实验结果（非仅 Limitations 一句话）；论证 base-model 场景的重要性

**SF2 [warning, consensus] Temperature sensitivity 未充分限定 DDR 普遍性声明**
- R1-W1 提出，R2 AGREE
- t=0.9 时 Pythia -26pp, Qwen -18.5pp；cross-temperature Qwen F1 0.810→0.418
- DDR "property of recursive generation" 声明需限定 temperature/sampling 条件
- **要求**：在 Abstract 和所有 DDR 普遍性声明处加条件限定

**SF3 [warning, consensus] Downstream utility 结果弱化论文动机**
- R2-W3 提出，R1 AGREE
- Appendix L TOST 确认 depth-aware 与 random subsampling 在 perplexity 上等价
- Introduction 以 data curation 为动机，但实验表明 depth 信息不影响 downstream performance
- **要求**：调整动机叙事（从 data quality filtering 转为 provenance transparency/audit），或找到更有说服力的应用场景

**SF4 [warning, consensus] Baseline 4-det ensemble 优于所提方法，需更直接承认**
- R1-N2 提出（原判 critical），R2 REBUT 纠正数据错误
- R2 纠正：3-class F1 gap 是 2.1pp（0.785 vs 0.774），非 R1 引用的 6.1pp；论文明确说 "contextualize not claim advantage"
- R2 认可效率差异（2.4× inference + 3.2× GPU memory）在大规模场景有意义
- 两位均同意应更直接承认 4-det ensemble 在 3-class 准确性上更优
- **要求**：§4.3 更明确承认性能差距；效率论证聚焦 large-scale batch processing 场景

**SF5 [warning, consensus] Cross-reference model 声明过强**
- R1-W5 提出，R2 AGREE
- Spread ≤ 0.013 仅说明 features 对 reference model 选择鲁棒 ≠ "DDR 是递归生成内在属性"
- **要求**：区分 "robustness to implementation choice" 和 "fundamental property claim"

**SF6 [warning, consensus] Stylometry 引用 + data contamination/provenance 文献线缺失**
- R2-W4 + R2-W5 提出，R1 均 AGREE
- TTR/hapax 是 2/7 核心特征但 stylometry 仅 3 篇 survey，缺 MATTR/HD-D 变体
- 以 data provenance 为动机但 Related Work 缺 contamination detection 文献
- **要求**：§2.3 增加 lexical richness 文献；§2 增加 data provenance/contamination paragraph

**SF7 [info→warning, partial consensus] Gen-0 seed sharing + XGBoost 超参数**
- R1-W3（gen-0 膨胀）：R2 partial REBUT，论文已处理（binary F1 as primary metric），但 Table 1/2 展示可改进
- R1-W4（XGBoost 超参数）：R2 AGREE with caveat（Appendix H classifier alternatives 部分缓解）
- **建议**：Table 1/2 caption 更突出 gen-0 影响提醒；报告 XGBoost 超参数选择来源

---

## Reviewer Consensus

以下问题两位 Reviewer 明确达成共识：

1. **[AGREE] DDR 应定位为 empirical observation 而非 general framework** (R1-N1 + R2-N3)
2. **[AGREE] "Fingerprinting" 标题需修改** (R1-N3 + R2-W1)
3. **[AGREE] Base-model-only 是核心实际限制** (R1-W2 + R2-N2)
4. **[AGREE] 方法论新颖性有限，贡献在于 task formulation + empirical finding** (R2-N1 + R1 AGREE)
5. **[AGREE] Downstream utility 弱化动机** (R2-W3 + R1 AGREE)
6. **[AGREE] Temperature sensitivity 需更强限定** (R1-W1 + R2 AGREE)
7. **[AGREE] Depth 2-4 merge 限制 framing** (R1-W6 + R2-W1)
8. **[AGREE] Missing references: stylometry 变体 + data provenance** (R2-W4/W5 + R1 AGREE)
9. **[AGREE] Cross-reference 声明需降级** (R1-W5 + R2 AGREE)

## Reviewer Divergence

**D1. DDR vs model collapse 增量 (R2-N3 vs R1 partial REBUT)**
- R2 认为 DDR 仅是 "naming existing phenomena"
- R1 反驳：DDR 与 model collapse 有实质机制区别（fixed params, reversible, shape stability ≠ 不可逆参数退化）；shape stability (d < 0.10) 非先验可预期
- **共识部分**：两位均同意 DDR 的 analytical contribution 有限，应定位为 empirical observation
- **未解决**：DDR 是否提供了超越 model collapse 文献的真正新洞察——R1 认为有（机制区别），R2 认为有限

**D2. Baseline comparison severity (R1-N2 vs R2 REBUT)**
- R1 原判 critical (gap 6.1pp)
- R2 纠正数据错误 (实际 2.1pp)，指出论文明确说 contextualize not compete
- **已解决**：降为 warning (SF4)，两位均同意需更直接承认 4-det ensemble 优势

**D3. Gen-0 seed sharing severity (R1-W3 vs R2 partial REBUT)**
- R1 认为 Table 1/2 展示误导
- R2 认为论文已有缓解措施（binary F1 as primary），gen-0 高分部分源于任务固有可区分性
- **已解决**：非关键问题，改进 caption 即可

---

## Questions（需作者回答）

**Q1.** DDR 阈值 |ρ| > 0.60 / |ρ| < 0.10 的 sensitivity 如何？如果变动 ±0.10，三分法是否还成立？[R1-Q1, R2-Q2]

**Q2.** LOGO 中 Pythia-1B 和 Pythia-2.8B 是同时 held out 还是分别？如果分别，同 family 不同 size 的模型在 train set 中是否导致 family-level 信息泄漏？[R1-Q2]

**Q3.** Downstream utility 实验显示 depth-aware 与 random subsampling 等价（TOST confirmed）。如果 depth 信息不影响 downstream performance，depth classification 的主要应用场景是什么？[R1-Q3, R2-Q4]

**Q4.** Instruction-tuned model 上 F1 降至 0.338 的原因：是 depth signal 本身消失，还是 instruction tuning 引入新 confound 使特征不再 discriminative？[R2-Q5]

**Q5.** 方法在混合 prompt type 条件下的表现如何？实际递归生成可能混合不同 prompt types。[R1-Q6, R2-Q3]

**Q6.** Table 2 中 4-detector ensemble 在 3-class F1 上优于 7-feature method。作者如何定位方法的 practical value proposition？[R1-Q5]

---

## Missing References

1. **Lexical richness measures**: McCarthy & Jarvis (2010) "MTLD, vocd-D, and HD-D"; Covington & McFall (2010) "MATTR" [R2-W4]
2. **Data contamination detection**: Oren et al. (2024) "Proving test set contamination in black box language models"; Golchin & Surdeanu (2024) "Time Travel in LLMs" [R2-W5]
3. **Data provenance**: Longpre et al. (2024) "Data Authenticity, Consent, and Provenance for AI Are All Broken" [R2-W5]
4. **Iterative generation analysis**: Huang et al. (2023) "Large Language Models Cannot Self-Correct Reasoning Yet Without External Feedback" [R2 suggested]

---

## External Review (Stanford Agentic Reviewer)

外部审稿未配置（`external_review.paperreview_ai.enabled` 未设置），本轮无外部审稿结果。

---

## Overall Assessment

**Overall Score: 3.0 — Findings**

**EMNLP 2026 评分标准**: 3 = Findings（可被 Findings 接收）

**两位 Reviewer 独立评分**:
- R1: 3.0 (Findings), Soundness 3/5, Excitement 3/5, Reproducibility 3.5/5, Confidence 4/5
- R2: 3.0 (Findings), Soundness 3.5/5, Excitement 2.5/5, Reproducibility 4/5, Confidence 4/5

**综合评分**:
| 维度 | 综合分 | 理由 |
|------|--------|------|
| Soundness | 3.25/5 | 实验设计和统计方法严谨，但 DDR 阈值论证不足，baseline 实际更优 |
| Excitement | 2.75/5 | 问题定义新颖，但方法仅用标准特征，base-model-only 限制实际兴趣 |
| Reproducibility | 3.75/5 | 特征定义和实验参数清晰，但代码未开源，XGBoost 超参数来源不明 |
| Confidence | 4/5 | 两位 Reviewer 独立收敛到相同评分和高度重合的核心关切 |

**评分理由**:

本文的核心价值在于 **问题定义**（generation depth classification 是新方向）和 **实证发现**（DDR 三分模式作为 empirical observation 有价值）。实验设计严谨、消融全面、Limitations 坦诚，这些都是优点。

阻止进入主会议的关键问题：
1. **方法论贡献有限**：7 个标准特征 + XGBoost，无技术创新，贡献停留在 "把已有工具组合用于新任务"
2. **DDR overclaim**：将 7 个特征的描述性分组提升为 "framework"，阈值缺乏理论基础
3. **标题误导**："Fingerprinting" 暗示高可靠性，实际 F1=0.694 且仅 3-class 粒度
4. **适用范围极窄**：仅 base model + t ≤ 0.7，instruction-tuned models 上近乎失效

作为 **Findings paper**，论文有足够价值：新任务定义 + 系统性实证分析 + 诚实的限制讨论。但需要修正 overclaiming（标题、DDR framework 定位、baseline 对比 framing）以匹配实际贡献水平。

**提升至 Borderline Conference (3.5) 的条件**:
1. 修正标题和 DDR 定位（从 framework 降级为 empirical pattern）
2. Abstract 中声明 base-model restriction 和 3-class 粒度限制
3. 对 DDR 阈值做 sensitivity analysis + TOST
4. 正文纳入 instruction-tuned 实验结果并分析 depth signal 退化原因
5. 调整动机叙事（从 data curation 转为 provenance audit）
6. 补充 missing references

---

## Detailed Comments

### Abstract
- 四个必答问题基本覆盖 ✓
- DDR/LLM 缩写已定义 ✓
- 数据密度适当（R17 修改后从 ~8 降至 4 个数字）✓
- **缺失**：未声明 base-model restriction——读者可能误以为方法适用于所有 LLM [SF1]
- **缺失**：未声明 temperature 条件依赖 [SF2]

### Introduction
- 叙事线基本连贯：recursive chains as dynamical system → binary detection insufficient → depth classification → DDR
- R18 restructure 有改善（dynamical system framing leads, base-model restriction at L15）
- **问题**：7-17% LLM content 引用（Liang et al.）描述 instruction-tuned models 影响，与 base-model scope 存在 tension [SF1]
- **问题**：从 binary detection 到 "why depth matters" 的论证仍有跳跃——downstream utility null result 弱化了 data curation 动机 [SF3]
- Contribution list 需区分 task formulation 和 empirical finding [MF3]

### Related Work
- §2.1 Detection 覆盖充分 ✓
- §2.2 Model Collapse + concurrent work 区分有效（R1 Strength 6）✓
- §2.3 Stylometry 偏薄，缺 TTR 变体文献 [SF6]
- §2.4 Data provenance/contamination 文献线缺失 [SF6]

### Method
- Task formulation 清晰，generation chain construction 详细 ✓
- Feature extraction 动机合理（interpretable statistics for DDR analysis）✓
- LOGO 和 cross-model chain 协议设计严谨 ✓
- XGBoost 超参数来源不明 [SF7]
- Temperature 固定 t=0.7 justification 不足 [SF2]

### Results
- Table 1 清晰，bootstrap CIs ✓
- DDR 数据呈现紧凑 ✓
- §4.3 contextualization framing 合理但需更直接承认 4-det advantage [SF4]
- Feature complementarity 论述偏粗略 [R2]
- Cross-reference 声明需降级 [SF5]

### Discussion
- 覆盖了 instruction tuning、temperature、prompt type、resolution ceiling ✓
- 篇幅受限（8 页约束），各点深度不够
- DDR vs model collapse 区分已有改善，但可进一步强化可逆性 + shape stability 论证 [R17-W5]

### Conclusion
- 简洁诚实 ✓
- "Three classes = practical ceiling" 与标题矛盾 [MF2]

### Limitations
- 覆盖全面：base-model, instruction-tuning, temperature, prompt-type, scale, domain, reference model ✓
- 在同类论文中属于高质量 Limitations section

### Ethics
- 覆盖 dual-use, privacy, licenses, compute budget ✓

### Format Compliance
| 项目 | 状态 |
|------|------|
| 正文 ≤ 8 页 | ✓ |
| ACL template [review] | ✓ |
| 匿名化 | ✓ |
| 行号 | ✓ |
| Limitations section | ✓ |
| Ethics Statement | ✓ |
| Responsible NLP Checklist | ⚠️ 未在 PDF 中发现，可能通过 ARR 系统单独提交 |
| 图表字体 ≥ 7pt | ✓ |
| Bib 格式 | ⚠️ 部分条目需验证 |