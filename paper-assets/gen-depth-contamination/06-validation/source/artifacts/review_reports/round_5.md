---
round: 5
overall_score: 3.0 (Findings)
timestamp: 2026-05-18T07:34:22.738505+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 7（EMNLP 2026 圆桌审稿）

**论文**: Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary
**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**审稿编排**: 2 名 Reviewer（R1: 方法严谨性 + 实验有效性; R2: 新颖性 + 完整性 + 定位）
**审稿轮次**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT）→ 收敛汇总

---

## Summary

本文定义并测量了递归合成文本的代际深度可区分边界 K*_empirical，使用 15 维统计特征和 OBD-LightGBM 分类器，在 8 种模型配置（5 个架构家族，1B-8B）、3 个源域、4 种解码策略下实验。核心发现：一般网页文本 K*=2（7/8 配置），学术文本 K*=3（5 模型），Wikipedia K*=1。跨模型迁移率 80-92%（continuation 模式），下游 binary filtering 在 100% synthetic 设置下减少 MMLU 退化约 50%。

论文的实验覆盖面和统计方法论在同类工作中属上乘，但存在若干关键缺陷：核心术语 "model-free" 与实际 scorer 依赖性矛盾、Related Work 遗漏重要文献、核心发现（web text K*=2）的 negative result 性质未被正面讨论、下游验证仅限单一模型且在真实污染比例下效果极小。

---

## Strengths

**S1. 研究问题新颖且定义清晰** [R1, R2 共识]
代际深度的可区分边界此前未被系统测量。K*_empirical = max{k ≥ 1: AUC_{k-1,k} > θ} 是简洁有效的形式化，threshold justification 通过三条独立证据线（Cohen's h heuristic、permutation test、empirical discontinuity）充分支持。

**S2. 实验覆盖面广且统计方法论严谨** [R1, R2 强共识]
8 种模型配置 × 5 架构家族 × 4 解码策略 × 3 域，每配置 30,000 文档。OBD 分类器 + GroupKFold 防泄漏 + bootstrap CI + permutation test + ANOVA。消融涵盖特征子集、self_BLEU 独立性、scorer confound、dose-response、neural probe、LLM zero-shot baseline。在审过的论文中属于方法论范例。

**S3. 域序不变性是有价值的发现** [R1, R2 共识]
arXiv (K*=3) > C4 (K*=2) > Wikipedia (K*=1) 跨 6 模型、4 架构家族一致。Mistral 的 cross-domain 反转（C4 K*=1 但 arXiv K*=3）有力证明 domain structure 而非 model identity 是 K* 的主要决定因素。

**S4. 写作质量好** [R2]
无 em-dash/en-dash AI 痕迹，无 -ing phrase ending 模式，无 leverage/utilize/delve 等 AI 用词（仅 Ethics Statement 一处 "facilitate"）。叙事连贯，符号使用一致。

**S5. Limitations 诚实且详尽** [R1, R2]
7 个维度的正文 Limitations + Appendix 展开。Marginal boundaries（Qwen-cont CI lower +0.002, LLaMA-8B 1/5 folds below θ）如实报告。

**S6. 格式合规** [R2]
正文恰好 8 页，\usepackage[review]{acl}，anonymous author，Limitations 和 Ethics Statement 为 unnumbered sections。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1. [Critical] "Model-free" 术语误导，与 cross-scorer 结果内部矛盾** [R1 发现, R2 AGREE]

15D 特征中 9 维属于 surprisal 家族，全部依赖外部 scorer LM 计算 token-level log-probabilities。称 "model-free" 字面不准确。更严重的是，cross-scorer validation（Table S13）显示 Qwen-cont K* 从 2 降至 1（AUC < 0.60 with Pythia/OLMo scorers），直接证明 K* 对 scorer 选择敏感。ANOVA（Table 24）Scorer 显著（p < .001, η²_p = 0.19），虽相对 Depth-Pair 较小，但可改变 K* 的离散取值。Abstract 和 Contribution (c) 的 "Model-free" 与这些结果构成内部矛盾。

→ **建议**: 改为 "generator-agnostic"/"generator-independent"。Section 3.2 明确说明特征依赖固定 scorer。Discussion 增加段落讨论 scorer 依赖性。

**N2. [Critical] Related Work 遗漏 3 篇重要直接相关文献** [R2 发现, R1 AGREE]

(1) **Shi et al. (NeurIPS 2025 Spotlight)** "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective" — entropy decline 刻画 collapse + entropy-based data selection，与本文 DPI/JSD framing 和 Section 5 curation 直接相关。(2) **Gambetta et al.** "Surplexity for Mitigating Model Collapse" — surprisal-based measures 直接刻画 collapse，与本文 surprisal features 高度重叠，不引用是审稿红旗。(3) **Amin et al. (NeurIPS 2025)** "Escaping Collapse: The Strength of Weak Data" — curation 理论框架。前两篇 severity = Critical，Amin = Major。

→ **建议**: Related Work 分别加入一句。明确 15D features vs surplexity 的区别（多阶统计量 + cross-model transfer 验证 vs 单一 surprisal 指标）。

**N3. [Critical] 下游验证仅单一模型 + 效果量在真实场景下极小** [R1 N2 + R2 W5, 交叉升级为共识 Critical]

Section 5 仅在 Qwen2.5-1.5B-Instruct + LoRA rank=8 上验证。100% synthetic 下 binary-ours MMLU 改善仅 0.77pp；Appendix dose-response 在 10% contamination 时差异仅 0.21pp（0.6079 vs 0.6058），30% 时 0.13pp，practically negligible。论文在 Conclusion 中给出 "concrete prescription"，但单模型 + 微小效果量不支撑此强度的一般性声明。

→ **建议**: 方案 A: 增加至少 1 个不同规模/家族的模型做 filtering 实验。方案 B: 将 filtering 明确降级为 "illustrative validation of K*=2"，Discussion/Limitations 中承认 practical significance 限制。

**N4. [Critical] 核心发现 K\*=2 的 "negative result" 性质未被正面讨论** [R2 发现, R1 AGREE with nuance]

Web text K*=2 意味着 depth estimation 在最常见域退化为 binary detection，论文的 "concrete prescription" 也是 binary filtering，与 Drayson et al. (2025) 策略实质等价。论文将此框架为 "first measurement" 的正面贡献，但未面对关键张力：depth estimation 相对 binary detectors 的增量价值是什么？

R1 补充 nuance：arXiv K*=3 和 retrain-chain K*≥4 表明这不是纯 negative result，但 web text 场景下的 tension 需直接面对。

→ **建议**: Discussion 增加段落正面讨论：(1) K*=2 作为 measurement 的科学价值（bounding a previously unbounded question），(2) arXiv K*=3 表明 beyond-binary 域存在，(3) K* 作为 domain-dependent diagnostic 的定位。

### Should-Fix（影响评分但不一票否决）

**W1. [Major] 论文定位不清：detection / measurement / curation 三重身份** [R2 W1, R1 部分 AGREE]

Contribution (a)(b) 是 measurement，(c) 是 detection/transfer，Section 5 是 curation。三方向各自深度不足以单独成文，合在一起缺乏统一主线。R1 认为核心是 measurement，filtering 和 transfer 应定位为 measurement 结论的应用验证。

→ **建议**: 统一叙事主线为 measurement paper。将 filtering 降级为 downstream validation，transfer 定位为 K* 的 practical property。

**W2. [Major] 与 Drayson et al. (2025) 区分不足** [R2 W2, R1 AGREE]

论文在 Related Work 中将 Drayson 定位为 "special case when K*=1"，但 Section 5 最终建议也是 binary filtering。在 web text 场景下，本文的 actionable output 与 Drayson 等价。需显式说明增量贡献。

→ **建议**: Related Work 或 Discussion 用 2-3 句明确：K*=2 为 Drayson 的策略选择提供了理论依据 + domain ordering 提供了域级指导。

**W3. [Major] 对 model collapse theory 的 over-claim** [R2 W3, R1 AGREE]

K* 是 classifier-dependent 的 discrimination boundary，不是 information-theoretic quantity。Neural probe K*=3 vs 15D K*=2 + cross-scorer K* 变化证明 K* 随表示变化。Conclusion "empirical anchor for information loss curve" 过强。

→ **建议**: 改为 "representation-dependent lower bound on discriminable depth"。Conclusion 注明 K*_empirical 与 K*_theory 之间的 gap。

**W4. [Major] Mistral-7B K\*=1 例外缺乏机制解释** [R1 W1, R2 AGREE + 补充]

1/8 配置 K*=1（12.5%），未讨论架构/训练数据原因。R2 补充：cross-domain 反转（C4 K*=1, arXiv K*=3）排除 architecture-level explanation，指向 generation quality proximity（0v1 AUC=0.930）。

→ **建议**: Discussion 补充 2-3 句可能解释。

**W5. [Major] arXiv 样本量差异 (n=2,200 vs C4 n=5,000) 未控制** [R1 W3, R2 AGREE (severity minor)]

更小训练集可能导致 CV 过拟合。R2 认为多模型交叉验证 + cross-scorer 非系统性膨胀降低了 severity。建议做 C4 下采样控制。

**W6. [Minor] 多个缩写未定义** [R2 W4, R1 部分 AGREE]

AUC, JSD, CI, LLM 首次使用未展开。MMLU, HellaSwag 未说明。R1 认为 severity 为 minor（ACL 社区标准），但 JSD/LLM 必须定义。

**W7. [Minor] 序列长度 256 tokens 限制** [R1 W4, R2 AGREE]

Table S11 显示 512 tokens 时 CI lower bound < θ，暗示 K* 可能随 segment length 变化。Limitations 已提及但 Discussion 未展开 deployment 影响。

---

## Reviewer Consensus [AGREE]

| 问题 | R1 | R2 | 状态 |
|------|----|----|------|
| "Model-free" 术语需修正 | Critical (N1) | AGREE | **共识** |
| Related Work 遗漏 Shi/Gambetta/Amin | AGREE | Critical (N1) | **共识** |
| 下游 filtering 单模型 + 效果量小 | Critical (N2) | AGREE (升级) | **强共识** |
| K*=2 negative result 需正面讨论 | AGREE (with nuance) | Critical (N2) | **共识** |
| 论文定位三重身份 | Partially AGREE | Major (W1) | **共识** |
| Drayson 区分不足 | AGREE | Major (W2) | **共识** |
| Model collapse over-claim | AGREE | Major (W3) | **共识** |
| Mistral 机制解释 | Major (W1) | AGREE + 补充 | **共识** |
| arXiv 样本量控制 | Major (W3) | AGREE (降 minor) | **共识** |
| 缩写未定义 | Partially AGREE (降 minor) | Major (W4) | **共识** (severity 分歧) |

## Reviewer Divergence [分歧]

| 问题 | R1 | R2 | 评估 |
|------|----|----|------|
| Cohen's h 映射假设 | Major (W2) | REBUT（θ 有更强独立支撑） | R2 论证更有说服力：permutation test + empirical gap 足以支撑 θ=0.60，Cohen's h 仅为 heuristic motivation |
| 分类器选择消融 | Minor (W5) | Partial REBUT（已有 ordinal LR + neural probe + LLM） | R2 论证成立：已有多种方法交叉验证 K*=2 不是 classifier artifact |
| "One-wash laundering" 措辞 | Minor (W6) | REBUT（学术文献有 precedent，precise + evocative） | Style preference，无需强制修改 |
| 缺失引用方向 | Watermarking/extraction | Model collapse/surprisal | R2 方向更切题：Shi/Gambetta 与本文核心 feature space 和 framing 直接相关，watermarking 属不同 paradigm |

---

## Questions for Authors

1. **K\* 的增量价值**: 既然 web text 建议是 binary filtering，K* 相对 Drayson et al. 的实际增量是什么？是 diagnostic 价值还是 operational 价值？
2. **Surplexity 对比**: 15D surprisal features 与 Gambetta et al. 的 surplexity 的区别和优势？
3. **K\*=2 的 classifier dependence**: 更强的 feature set（如 fine-tuned LLM embeddings）是否可能给出更高的 K*？K*=2 在多大程度上是 text property vs. feature set property？
4. **Scale extrapolation**: 0v1 AUC 随 scale 下降。13B+ 或 frontier models 是否可能 K*=1 甚至 K*=0？
5. **Retrain-chain K\*=4**: 仅 Pythia-1.4B LoRA 一个模型。如何解读与 prompt-chain K*=2 的差异？是否需要更多模型验证？
6. **Scorer sensitivity**: Cross-scorer 下 Qwen-cont K* 从 2 降至 1。K* 是否应报告为 K* ∈ {1,2} with scorer-dependent variation？

---

## Missing References

| 论文 | Venue | 相关性 | Severity | 共识 |
|------|-------|--------|----------|------|
| Shi et al., "A Closer Look at Model Collapse: Generalization-to-Memorization" | NeurIPS 2025 Spotlight | entropy-based collapse + data selection，与 DPI/JSD framing 直接对应 | Critical | R1+R2 AGREE |
| Gambetta et al., "Surplexity for Mitigating Model Collapse" | arXiv 2025 | surprisal-based collapse metric，与 15D features 高度重叠 | Critical | R1+R2 AGREE |
| Amin et al., "Escaping Collapse: Strength of Weak Data" | NeurIPS 2025 | synthetic data curation 理论框架 | Major | R1+R2 AGREE |

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目配置中未找到 external_review 设置）。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**R1**: 3.0 (Findings) — Soundness 3/5, Excitement 3/5, Confidence 4/5
**R2**: 3.5 (Borderline Conference) — Soundness 4/5, Excitement 2.5/5, Confidence 4/5

**Director 综合评估**: 3.0 (Findings)

**理由**: 论文在研究问题定义和实验方法论上具有显著优势，统计严谨性和消融实验的充分程度在同类工作中突出。域序不变性是有价值的 empirical contribution。但存在四个共识 Critical 问题：(1) "model-free" 术语与实际 scorer 依赖性矛盾，(2) 遗漏 3 篇重要直接相关文献（含 NeurIPS 2025 Spotlight），(3) 下游验证仅单一模型且真实场景效果极小，(4) web text K*=2 的 negative result 性质未被正面讨论。此外，方法论创新有限（标准 ML pipeline），excitement 偏低。

**修订后潜力**: 若能解决 (1) 术语修正 + scorer sensitivity 充分讨论，(2) 补充缺失文献并明确 positioning，(3) 增加 filtering 模型或诚实降级 claim，(4) 正面讨论 negative result tension，评分可提升至 3.5 (Borderline Conference)。Domain ordering 的 cross-model consistency 和统计方法论的严谨性是论文的核心竞争力，建议围绕 measurement 主线重组叙事。

---

## Detailed Comments

### Abstract
- "Model-free statistical features" → 改为 "generator-agnostic statistical features"
- 数字密度适中（~130 words），但 "one-wash laundering" 概念出现在 abstract 之外，建议保留

### Section 1 (Introduction)
- L10: 4 个分号 + 6 引用的长句建议拆分为 2 句
- Contribution (c) "Model-free" 需修正
- 缺乏对 K*=2 意味着 "binary suffices for web text" 的正面讨论

### Section 2 (Related Work)
- 遗漏 Shi et al., Gambetta et al., Amin et al.（详见 N2）
- 与 Drayson et al. 的增量贡献需更显式化

### Section 3 (Method)
- Cohen's h mapping (Footnote 1) 建议降级为 "motivating analogy" 而非 "justification"（R1 Major, R2 REBUT — 不影响结论但措辞可更精确）
- Section 3.2: 应明确说明 surprisal features 依赖固定 scorer LM

### Section 4 (Experiments)
- Section 4.1: LLaMA-8B 和 Mistral-7B 的 borderline cases 报告诚实，但 Mistral 例外需机制性讨论
- Section 4.2: "model-free cross-model transfer" 标题需改为 "generator-agnostic"
- Section 4.5: arXiv n=2,200 vs C4 n=5,000 的样本量差异需讨论或控制实验

### Section 5 (Filtering)
- 单模型验证不足以支撑 "concrete prescription"
- Dose-response 效果衰减需在 Discussion 中正面讨论 practical vs. statistical significance

### Section 6 (Discussion)
- "One-wash laundering" 保留（R1 建议改，R2 REBUT — 分歧未解决，属 style preference）
- "Representation dependence" 段应更明确承认 K* 是 classifier/feature-dependent
- 缺乏对 Mistral 例外的机制性讨论
- 缺乏对 segment length 对 deployment 影响的讨论

### Section 7 (Conclusion)
- "empirical anchor for information loss curve" 过强 → "representation-dependent lower bound"
- "concrete prescription" 需限定条件或降级

### Limitations
- 覆盖充分（7 个维度），仅需补充 scorer sensitivity 对 K* 离散取值的影响

### Ethics Statement
- "facilitate" → "support"/"enable"

### References
- 31 篇基本合理，但缺 Shi/Gambetta/Amin 是显著缺口
- 引用格式需核实 first-author consistency (alemohammad2024, mehta2025)

### Appendix
- 内容充实，消融覆盖全面
- Table S12 caption 需标注 same-family scoring（FR6-OBS-2，此前已标注为 resolved）