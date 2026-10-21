---
round: 1
overall_score: borderline
timestamp: 2026-05-15T12:13:13.727276+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 1

**论文**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains
**目标 venue**: EMNLP 2026 Main Conference (via ARR May cycle)
**截止日期**: 2026-05-25
**审稿人**: Reviewer 1 (方法严谨性 + 实验有效性), Reviewer 2 (新颖性 + 相关工作 + 写作质量)
**审稿轮次**: Round 1 (独立初审 + 交叉分享，1 轮收敛)

---

## Summary

本文提出 ordinal generation depth estimation——将文本分类为人写 (gen-0)、一次生成 (gen-1) 或多次递归生成 (gen-2+)——超越了现有的二分类检测范式。核心经验发现为 differential depth response：中心趋势和词汇多样性特征（entropy mean、TTR、hapax ratio）随生成深度单调漂移，而分布形状特征（entropy std、tail decay）保持近稳态。基于此的 7 特征 XGBoost 集成在 6 个生成器（3 个模型族，0.6B–8.2B）的 LOGO 评估中达到 macro-F1 = 0.79，跨生成器一致性（CI width 1.4pp）远优于单一检测器基线（CI width 18–26pp）。论文同时报告负面发现：基于深度的数据筛选不优于随机采样，定位 depth fingerprinting 为诊断工具而非数据治疗工具。

---

## Strengths

- **S1: 任务定义新颖且有实际意义 [共识]。** 从二分类到有序三分类的 framing 填补了 binary detection 和完整溯源之间的空白。三分类方案在实用性和可行性之间取得合理平衡（5 分类 F1 降至 0.50）。

- **S2: 评估协议全面严谨 [共识]。** LOGO + LOFO 交叉验证系统检验跨模型和跨架构泛化；多种统计检验（McNemar、paired bootstrap）；5 种随机种子稳定性验证（std=0.0009）；3 种分类器对比（Appendix F）。评估设计达到 EMNLP 标准。

- **S3: Differential depth response 是有洞察力的经验发现 [共识]。** 漂移/稳态特征的二分法不是先验显然的。其与 OOD 检测文献中 location shift vs shape preservation 的类比（Section 5）提供了有价值的理论视角。

- **S4: 负面发现报告诚实且有信息价值 [共识]。** 深度感知数据筛选无效的结果（random 2.367 vs depth-stratified 2.387）可节省后续研究者构建无效 pipeline 的成本。

- **S5: 长度混淆控制充分 [共识]。** 三重验证（Spearman |ρ|<0.14、长度归一化后信号增强、长度匹配 F1 +0.041）有效排除长度伪因。

- **S6: 消融分析系统 [共识]。** Feature ablation（Table 2）、LOFO（Appendix D）、cross-family reference model、alternative classifier（Appendix F）系统验证结论鲁棒性。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [Critical/Major — 共识]: Baseline 比较结构性不公平**
论文将 7 特征集成与 4 个单分数 baseline 比较（Table 3），每个 baseline 仅用 1 个 score 作为 XGBoost 输入。7 特征 vs 1 特征不是公平比较。缺失关键实验：将 4 个 baseline 分数组合为 4-feature ensemble，只有这个比较才能分离"特征数量优势"和"特征类型互补性"。建议补充三组对比：(a) 4-baseline ensemble, (b) 4-baseline + TTR + hapax (6特征), (c) 论文7特征。
- R1: Critical; R2: Major（论文核心贡献在任务定义而非方法优越性，且 4 个 baseline 高度相关可能限制 ensemble 提升空间）
- **交叉后共识：必须补充实验，严重程度分歧保留**

**W2 [Critical/Major — 共识]: 大模型泛化 claim 证据不足**
Qwen3-8B (8.2B) held-out F1=0.683，远低于 ≤2.8B 生成器的 0.76–0.86（Table 1），降幅 11–17pp。从 0.6B 到 8.2B 的性能趋势呈下降，暗示 frontier 模型（70B+）上可能进一步退化。但正文和 abstract 仍使用"cross-scale generalization"等措辞，与 Limitations 中"frontier models remain untested"的承认不一致。实际 web contamination 主要来自 frontier 模型，若方法在此失效，实用价值大打折扣。
- R1: Critical; R2: Major（Limitations 已坦承，Findings 轨道要求相对宽松）
- **交叉后共识：正文 claim 必须与 Limitations 对齐，降低措辞强度**

**W3 [Major — 共识]: Topic drift 作为未控制的混淆因素**
Continuation chain（"Continue the following text"）天然导致 topic drift。TTR 和 hapax ratio 对 topic narrowing 敏感——递归生成导致主题收窄可能直接降低词汇多样性，与 depth signal 混淆。论文控制了 length confound 但完全未讨论 topic drift。Appendix B 的 drift rate 梯度（continuation 16.9% > rewriting 6.1% > elaboration 1.4%）与 topic constraint 强度对齐，构成间接支持证据。
- R1 提出, R2 交叉后 AGREE（承认自己遗漏）
- **建议：计算相邻深度间语义相似度，控制 topic drift 后重新评估特征判别力**

**W4 [Major — 共识]: 遗漏直接相关的 multi-class 检测工作**
论文声称"no existing method addresses this task directly"（Section 1），但未讨论：(1) Cheng et al. (WWW 2025) "Beyond Binary"——多分类 AI 文本检测（source attribution 维度）；(2) SemEval-2024 Task 8——包含多分类归因 subtask；(3) "Tracing the Data Trail"（arXiv 2601.14311, 2026）——LLM 数据 provenance 综述；(4) "Machine-generated text detection prevents language model collapse"（arXiv 2502.15654）——检测与 collapse 交互。
- R2 提出, R1 交叉后 AGREE（但指出这些工作地址的是 source attribution，与 depth estimation 是不同分类轴）
- **建议：引用并明确区分，将 "no existing method" 限定为 "no existing method addresses ordinal depth estimation in non-paraphrastic chains"**

### Should-Fix（显著提升论文质量）

**W5 [Major — 共识]: 下游实验规模过小，不足以支撑 Contribution 3**
负面发现是三大贡献之一，但支撑实验仅用 1 个下游模型（OLMo-2-0425-1B）、1 个指标（perplexity）、极小数据量（n=3,951 size-matched）。Perplexity 差异仅 0.020（2.367 vs 2.387），"data quantity dominates depth composition" 的声明在此规模下推广性存疑。
- R1: Major; R2: 初审 Minor → 交叉后升级为 Major
- **建议：扩大实验范围（多任务/多模型/更大数据量）或将 Contribution 3 降级为 additional finding**

**W6 [Major — 分歧]: 方法新颖性有限**
所有 7 个特征均为已知量（TTR、hapax ratio、NLL 统计量），XGBoost 无定制，Random Forest 达到几乎相同 F1（0.790 vs 0.789）。"Differential depth response" 是经验观察，其中 diversity decline 和 perplexity compression 已在 model collapse / text diversity 文献中有记录。
- R2: Major（贡献偏向 "application of existing tools to a new framing"）
- R1: REBUT（task formulation + empirical characterization 本身是有价值的贡献类型，method novelty ≠ excitement）
- **分歧保留：R1 Excitement 3.5/5, R2 Excitement 2.5/5**

**W7 [Major/Minor — 轻微分歧]: entropy_min 归类不一致且冗余**
entropy_min 在 Section 3.3 被列在 "Surface features" 下但实际用 reference model 计算。LOFO 分析（Appendix D）显示其完全冗余（Δ=+0.01pp）。一个占 7 特征中 1/7 的冗余特征影响 feature engineering 可信度。
- R1: Major; R2: Minor
- **建议：移至 reference features 分组，或从 ensemble 中移除并报告 6 特征结果**

**W8 [Minor/Major — 轻微分歧]: 缺少特征选择论证**
未讨论为何排除句法特征、重复性指标（self-BLEU）、连贯性特征、NLL 偏度/峰度等自然候选。7 个特征的选择缺乏系统性 feature search 过程。
- R1: Major; R2: Minor（论文定位为 empirical finding 而非 optimal feature set）
- **建议：在 Method 或 Discussion 中补充特征选择 rationale**

### Minor（建议改进）

**W9 [Minor — 共识]: CI 报告异常**
Table 3 中 ensemble CI [0.786, 0.800] 上界恰好等于点估计，在 bootstrap CI 中不寻常。需作者验证 bootstrap 实现。

**W10 [Minor — 共识]: Abstract CI 描述有误导性**
"confidence intervals spanning 0.41–0.82" 是跨检测器 CI 端点范围，非任何单个检测器的 CI 宽度。建议改为 "individual detector CIs span up to 26 pp"。

**W11 [Minor — 共识]: Abstract 混用不同评估设置的指标**
F1=0.79 来自 6-gen LOGO（Table 1），CI width 1.4pp 来自 5-gen LOGO（Table 3）。建议在同一设置下报告或明确标注来源。

**W12 [Minor — 共识]: 形状特征稳定性假说缺乏实验验证**
Section 5 提出 shape 由 sampling mechanism 决定的假说但标记为 speculative。在不同 temperature/top-p 下测试是直接可行的验证实验。

**W13 [Minor — 共识]: 单一 prompt 类型用于主实验**
主实验仅用 continuation prompt。Appendix B 的 cross-prompt 验证仅限 Pythia-2.8B 一个生成器。Prompt type × generator 交互效应未评估。

**W14 [Minor — 共识]: 代码和数据未提及开源计划**
对于提出新任务和 benchmark 的论文，数据可用性对可复现性和后续研究至关重要。

**W15 [Minor — 共识]: entropy_max/entropy_min 未被归入 drift/stationary 分类**
Contribution 2 的核心是 differential depth response 的 drift/stationary 分离，但 7 个特征中 2 个未被明确归类。entropy_max 在 LOFO 中影响最大（-1.5pp）却未报告 Spearman ρ。

**W16 [Minor — 共识]: 可复现性细节缺失**
XGBoost 超参数配置和下游 fine-tuning 超参数（lr, epochs, batch size）均未报告。

---

## Reviewer Consensus（交叉后共识，5 项）

1. **规模泛化 claim 过度** — 8.2B 性能已显著退化，正文措辞需降级 [R1-W2, R2-W3]
2. **entropy_min 归类/冗余问题** — 需修正分组或移除 [R1-W5, R2-W5]
3. **CI 报告/描述问题** — Abstract 表述需精确化，Table 3 CI 需验证 [R1-W7/W8, R2-W4]
4. **下游实验不足** — 实验 scope 与 Contribution 3 定位不匹配 [R1-W4, R2-W7]
5. **形状稳定性需验证** — 不同 sampling 参数下的实验可直接检验假说 [R1 Detailed, R2-W6]

## Reviewer Divergence（保留分歧，1 项）

**Excitement 评分分歧（R1: 3.5/5, R2: 2.5/5）**
- R1 认为 task formulation 和 empirical characterization 本身构成有价值的贡献，method novelty 不应过度惩罚 excitement。引用 ACL/EMNLP 接受大量 empirical contributions paper 的先例。
- R2 认为方法层面是已有工具的组合应用，"Beyond Binary"（WWW 2025）的存在进一步削弱 novelty claim，excitement 应反映技术创新程度。
- **Director 判断：两种评估视角均有合理性。任务定义确有贡献，但方法创新确实有限。综合取 Excitement 3/5。**

---

## Questions（需要作者澄清）

1. 将 4 个 baseline 分数组合为多特征 XGBoost 的 LOGO F1 是多少？（W1 的核心验证）
2. entropy_max 和 entropy_min 的 Spearman depth 相关系数是多少？它们属于 drift 还是 stationary？（W15）
3. 是否有控制语义相似度后 depth features 判别力保持的数据？（W3）
4. 下游 fine-tuning 超参数（learning rate, epochs, batch size）？（W16）
5. Table 3 中 CI 上界=点估计（0.800）的 bootstrap 实现是否正确？（W9）
6. XGBoost 的具体超参数配置？（W16）

---

## Missing References

1. **Cheng et al. (WWW 2025)** — "Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement" [共识: 必须引用]
2. **Wang et al. (SemEval 2024)** — "SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection" [共识: 应引用]
3. **arXiv 2601.14311 (2026)** — "Tracing the Data Trail: A Survey of Data Provenance, Transparency and Traceability in LLMs" [共识: 应引用]
4. **Zhang et al. (arXiv 2502.15654, 2025)** — "Machine-generated text detection prevents language model collapse" [共识: 应引用]

---

## Overall Assessment

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3/5 | 3.5/5 | **3/5** — baseline 不公平和 topic drift confound 是实质性方法论问题 |
| Excitement | 3.5/5 | 2.5/5 | **3/5** — 任务定义有价值，但方法创新有限 |
| Reproducibility | 3/5 | 4/5 | **3.5/5** — 方法描述基本充分，缺超参数和开源计划 |
| Overall | 3/5 | 3/5 | **3/5 — Borderline** |
| Confidence | 4/5 | 4/5 | **4/5** |

**综合评分：Borderline（介于 Findings acceptance 和 borderline main conference 之间）**

**推荐处置：**
- 当前版本适合 **Findings 轨道**
- 解决 W1（baseline 公平性实验）和 W3（topic drift 定量分析）后，如果结论不变（即论文特征集确实优于 baseline ensemble，且 depth signal 独立于 topic drift），论文质量可达 **main conference borderline accept** 水平
- W2（规模泛化 claim 调整）和 W4（补充 missing references）是必要的修订，但不改变论文核心贡献
- W5（下游实验扩展或降级 Contribution 3）会显著改善论文的贡献-证据匹配度

**一句话总结：任务定义新颖、评估严谨、负面发现诚实，但 baseline 比较的结构性不公平、topic drift 未控制、规模泛化 claim 过度是三个必须解决的问题——解决后论文具备 EMNLP main conference 竞争力。**

---

## Detailed Comments

### Section 1 (Introduction)
- "no existing method addresses this task directly"（line 15）需限定为"no existing method addresses ordinal depth estimation in non-paraphrastic chains"，以 acknowledge Beyond Binary (WWW 2025) 和 SemEval-2024 Task 8 等 multi-class 方向 [共识]
- "confidence intervals spanning 0.41–0.82"（line 16）改为更精确表述 [共识]
- Contribution list 中 drifting + stationary features 的互补性 claim 需更清晰解释 stationary features 的分类贡献机制——如果不随 depth 变化，为何有助分类？[R1]
- "0.6B–8.2B parameters" 的规模范围描述应附带对 8.2B 性能退化的 caveat [共识]

### Section 2 (Related Work)
- 2.1 节缺少 Beyond Binary (Cheng et al. WWW 2025) 和 SemEval-2024 Task 8 的讨论 [共识]
- 2.4 节应引用 "Tracing the Data Trail" provenance 综述 [共识]
- 建议增加一段明确区分 source attribution（按生成器分类）vs depth estimation（按递归深度分类）的讨论 [R1]

### Section 3 (Method)
- 3.3: entropy_min 的 surface features 归类不一致，建议移至 reference features 或移除 [共识]
- 3.3: tail_decay 定义中 C_0 需明确是所有 gen-0 文本还是特定子集 [R1]
- 3.4: "The same hyperparameter configuration is used across all experiments" 需给出具体值 [共识]
- 缺少特征选择 rationale——为何这 7 个特征而非其他候选？[R1 Major, R2 Minor]

### Section 4 (Results)
- 4.1: "adding Qwen3-8B data improves classification on the original five generators (+1.1pp)" 需控制训练集大小来区分是数据量增加还是 cross-scale diversity 的贡献 [R1]
- 4.2: Spearman ρ=-0.558 (hapax) 和 ρ=-0.475 (entropy_mean) 称为 "strong monotonic trends" 可能过度，建议用 "moderate-to-strong" [R1]
- 4.2: entropy_max 和 entropy_min 的 Spearman ρ 未报告，drift/stationary 归类缺失 [共识]
- 4.3: 7 vs 1 特征的比较需补充 4-baseline ensemble [共识]
- 4.4: fine-tuning 超参数未报告 [共识]
- 4.4: Depth 0 only (n=797) 行的信息价值有限（数据量差异过大） [R1]

### Section 5 (Discussion)
- Shape stationarity 假说标记为 speculative 是恰当的，但建议加一句：varying τ/top-p 可检验此假说 [共识]
- "Connection to model collapse" 区分 inference chain vs training loop 恰当 [共识]
- 建议增加对 topic drift 的讨论 [R1]

### Limitations & Ethics
- 覆盖充分，涵盖规模、prompt 类型、单生成器链、downstream 任务范围 [共识]
- Ethics statement 适当，但可增加对 depth estimation 被用于审查的讨论 [R2]

### 格式合规 [R2 验证]
- ✅ ACL 模板 (`\usepackage[review]{acl}`)
- ✅ Double-blind 合规（\author{Anonymous}，正文无身份泄露）
- ✅ 正文 ≤ 8 页
- ✅ 引用格式正确
- ✅ Limitations 和 Ethics Statement 存在且充分
- ⚠️ 2 处 minor bib 格式问题（self_consuming_mad 第一作者差异、Qwen3 团队 vs 个人作者）
