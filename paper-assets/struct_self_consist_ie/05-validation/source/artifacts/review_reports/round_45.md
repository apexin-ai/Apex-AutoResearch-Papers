---
round: 45
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-24T23:21:56.517621+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

## Round 45 审稿报告

**论文**: When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审稿模式**: Fresh（全新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性/实验评估; R2: 新颖性/相关工作/完整性）
**轮次**: 1 轮（交叉回应后达成共识，无需 Round 2）

---

### Summary

论文系统研究 test-time compute scaling（self-consistency, best-of-N）在 NER 上的表现。核心发现是"correlation-selection gap"：质量估计信号能预测输出质量（AUROC 达 0.82），但实例级选择无法带来可检测的 F1 增益（<1pp，CI 跨零）。诊断框架识别 degeneracy 和 signal alignment collapse 两个共现条件。Entity-level construction 作为探索性贡献在 Few-NERD 3-epoch 训练下获 +1.40pp 条件性增益（全局 Holm p_adj=0.055，suggestive）。实验覆盖 4 个 NER 数据集、2 个微调模型族（Qwen3-8B, LLaMA-3.1-8B）、57 项统计检验，附 46 页 appendix。

---

### Strengths

**S1. Correlation-selection gap 概念具有原创性和跨任务价值。** 群体水平高相关性无法转化为实例级选择增益——这一现象此前未被系统识别和诊断。对任何使用 confidence-based reranking 的结构化预测任务都有警示意义。[R1-S2, R2-S1 共识]

**S2. 统计方法论在 NLP 实证分析中属于标杆水准。** 57 项检验的 Holm-Bonferroni 校正、bootstrap CI、TOST 等价性检验、post-hoc power analysis、Cohen's d 效应量、置换检验。同时报告 global 和 per-family 校正，诚实标注 p_adj=0.055 的边界状态。[R1-S1, R2-S4 共识]

**S3. 分析覆盖面极其全面。** 46 页 appendix 包含 N-scaling、温度敏感性、cross-dataset transfer、free-form decoding ablation、epoch convergence、per-entity-type analysis、calibration analysis 等。几乎所有潜在混淆因素均被系统排查。[R1-S3, R2-S2 共识]

**S4. 声称限定诚实恰当。** Entity construction 始终标记为 "exploratory"，negative claims 使用 "no detectable gains" + CI 限定。Limitations 涵盖英语限定、模型规模限定、统计功效限定。[R1-S5, R2 共识]

**S5. 可复现性高。** 训练配置完整（Table 22），超参数详尽，承诺公开代码/checkpoint/seed 级结果。[R1-S6]

**S6. 形式化贡献有价值。** Proposition 1 将 entity construction 形式化为 MBR 解码，Proposition 2 的 degeneracy decomposition 提供可验证 bound（16 种配置全部成立）。[R1-S4]

---

### Weaknesses

#### Must-Fix（两位 Reviewer 共识）

**[MUST-FIX] W1. 模型覆盖面过窄，普适性声称超出证据范围 [R45-N1]**

主实验仅用 2 个模型族（Qwen3-8B, LLaMA-3.1-8B），均为 ~8B 参数微调。72B zero-shot probe 和 few-shot 实验被论文自身标注为 exploratory。关键证据：Table 43 显示 degeneracy 是 model-family-dependent（Qwen2.5 在 Few-NERD 上 31.7%–46.2%，显著高于 Qwen3 的 13.0%），Table 44 跨家族（Claude, Gemini, GPT, DeepSeek）差异巨大。标题"When Self-Consistency Fails for NER"暗示一般性结论，但证据仅支持"在 7-14B 微调模型 + 4 个英文数据集上"。

- R1 Must-Fix (N2), R2 AGREE
- **建议**：收紧 title/abstract 的普适性表述，显式限定为测试模型区间（"7–14B fine-tuned open-weight models"）；或增加 ≥1 个模型家族的完整微调实验。R2 倾向前者（camera-ready 阶段增加新实验不现实），Director 同意。

#### Should-Fix（影响评分）

**[SHOULD-FIX] W2. Entity construction 统计边际且在 abstract/Figure 1 中展示权重过高 [R45-W1]**

全局 Holm-Bonferroni 校正下 p_adj=0.055，不满足 α=0.05。Per-family p_adj=0.006 依赖未预注册的 family 划分，构成研究者自由度。Entity construction 仅在 Few-NERD 上有正增益（+1.0pp conditional），ScieERC −0.12pp，CoNLL −0.5pp。Figure 1 中 "+1.4pp" 是单个配置结果而非聚合数据。一个 p_adj=0.055 的结果不应作为论文三大贡献之一呈现。

- R1 AGREE (W3), R2-W3 提出, 双方共识
- **建议**：(a) 降低 entity construction 在 abstract/Figure 1 中的突出程度，与 "exploratory" 定位匹配；(b) Figure 1 标注 "+1.4pp" 为单个配置而非聚合效果；(c) 主文报告全局 Holm p 值并标注 "marginally significant under global correction"

**[SHOULD-FIX] W3. 与 Landesberg (2026) 并行发现的差异化论述不够充分 [R45-W2]**

Correlation-selection gap 存在并行发现。当前 §2 末尾的 "Concurrent work" 段过于简短，不足以让读者理解本文的增量贡献（诊断框架 + 形式化结果 vs. gap 发现本身）。

- R2-W1 提出, R1 AGREE
- R1 补充：论文的核心增量是 *diagnosing* the gap（四种 failure mode、Proposition 1-2、多信号/多数据集系统比较），而非 *discovering* the gap。需在 Introduction 中显式分离这两个层面。
- **建议**：Introduction 增加一段明确说明与 Landesberg 的关系，强调增量贡献是诊断框架，而非 gap 本身的发现

**[SHOULD-FIX] W4. Failure mode 四种模式的层次化关系未显式形式化 [R45-W3]**

Degeneracy 在逻辑上蕴含 signal collapse（若所有输出相同，信号必然相同），但定义层面未显式建立蕴含关系。四种模式未覆盖 actively misleading signals（Table 4 中 FK 在 CoNLL 上 ρ=−0.05）。

- R1 Must-Fix (N1), R2 REBUT（降为 Should-Fix——隐式层次已存在于 Figure 1 + §4 + Appendix ae 诊断协议）
- **Director 判定**：降为 Should-Fix。R2 指出隐式层次已存在且 ρ=−0.05 统计上与零无异。但 R1 关于显式形式化的建议有价值——从业者操作化使用需要明确层次。
- **建议**：Section 3.3 或 4 开头加 1-2 句显式声明顺序诊断逻辑

**[SHOULD-FIX] W5. 3-seed 局限性在主文 Table 2/4 中未充分注明 [R45-W4]**

训练 seed 仅 3 个，cross-seed 变异分析仅 3 个数据点。此限制同样适用于主选择结果（Table 2, Table 4），但 3-seed 局限仅在 Limitations 部分提及。

- R1-W2 提出, R2 AGREE（3-seed 在 NER fine-tuning 中是常见做法，成本约束合理）
- **建议**：在 Table 2/4 caption 或正文中显式注明 3-seed 局限性

**[SHOULD-FIX] W6. Table 1 novelty comparison 维度选择偏向本文 [R45-W5]**

6 个维度中 "Diagnostics" 和 "Prescriptive" 恰好是本文强项，缺少 Landesberg 等工作可能更强的维度（Model Scale Range, Task Diversity）。

- R2-W2 提出, R1 AGREE 但非 must-fix
- **建议**：caption/脚注承认维度选择局限，或增加 1-2 个本文较弱维度

**[SHOULD-FIX] W7. 实践指导在主文可见性不足 [R45-W6]**

Appendix ah（10 条 Q&A 式建议）和 Appendix ae（cost-benefit 分析）包含实质内容，但主文 Section 8 缺乏 actionable summary。

- R2-W4 提出, R1 REBUT（内容存在但埋得太深）
- **Director 判定**：核心问题是可见性而非缺失。Appendix 内容扎实，但审稿人和读者首先看主文。
- **建议**：Section 8 增加 "Practical Implications" 段落（3-4 句），提炼 Appendix ah 核心建议

#### Minor Issues

- **M1**: Figure 2 标记点小、线条细，打印尺寸下难以区分 [R1-M1, R2 AGREE]
- **M2**: MBR 在 abstract/introduction 中使用但未展开全称，首次完整展开在 Section 6.1 [R1-M2, R2 AGREE]
- **M3**: Table 1 列头 "Yao+ 2026"/"Ours" 首次阅读不直观，建议更具描述性标签 [R1-M4, R2 AGREE]

---

### Questions

**Q1** [R1-Q1]: Proposition 1 entity-wise independence 假设的敏感性如何？相邻实体存在依赖关系（如嵌套实体），最优 θ 可能受 entity correlation 影响。[R2 AGREE]

**Q2** [R1-Q2]: Correlation-selection gap 在不同数据集上机制不同（ScieERC/CoNLL 以 degeneracy 为主，Few-NERD 以 signal collapse 为主），是否真是单一现象还是多种不同失效模式的共同症状？[R2 REBUT——统一框架是 feature 不是 bug，类似"发烧"是统一诊断信号但病因各异]

**Q3** [R1-Q3]: Free-form decoding ablation 仅在 Few-NERD/ScieERC 上测试，"LP compression is model-intrinsic" 结论能否推广到 CoNLL/WNUT？[R2 AGREE——完整 4-dataset ablation 更有说服力]

**Q4** [R1-Q5]: Table 2 主选择结果的 post-hoc power analysis 缺失。给定 test instances 数量、3 seeds、α=0.05，minimum detectable effect size 是多少？[R2 AGREE]

---

### Missing References

1. **Florian et al. (2003)** NER 集成学习——best-of-N selection 的自然历史对照（model-level diversity vs. sample-level diversity）[R2 提出, R1 AGREE]
2. **代码生成中的 self-consistency**——结构化输出的 SC 对比文献，可为 correlation-selection gap 的任务特异性提供上下文 [R1 提出, R2 AGREE]
3. **Diversity-promoting decoding 文献**（如 Diverse Beam Search）——与 degeneracy 概念有概念联系，DBS 本质上是通过解码策略降低 degeneracy [R2 提出, R1 PARTIALLY AGREE]

---

### External Review

外部审稿：未请求。

---

### Visual Layout Check（非评分项）

**状态**: ✅ 完成（18 info, 0 critical, 0 warning）

**主要发现**：
- **排版质量**: 双栏格式符合 ACL 模板，全文无 margin 溢出、无 LaTeX 错误、无未解析引用
- **视觉密度**: 8 页主文含 6 figures + 5 tables = 11 个 display items（~1.4/页），密度优秀，text-figure-table 交替节奏良好
- **Figure 1**: 全宽 overview，三阶段 pipeline 用颜色区分清晰，caption 自包含，信息密度高——优秀的视觉锚点
- **首页**: 无视觉锚点（纯文本 Abstract + Introduction），第一个 display item 在 page 2。建议考虑前移一个简图或核心数字到 page 1
- **图表一致性**: 蓝/橙/绿/红在 Figures 2-6 中语义统一，色盲友好
- **小尺寸图表**: Figure 4 两个 subfigure、Figure 5、Figure 6 偏小，打印后可读性接近下限
- **表格**: 全部使用 booktabs 风格，最优结果加粗，小数精度一致
- **Limitations**: 简洁（~1/3 页，3 个要点），符合 EMNLP 规范
- **Appendix**: Page 14 较密集（3 个 display items 挤一页），Figure 9 subfigure 字号偏小

---

### Overall Assessment

**Overall: 3.0 / 5 (Findings)**

| 维度 | R1 | R2 | Director |
|------|----|----|----------|
| Overall | 3.5 | 3.0 | **3.0** |
| Soundness | 3.5 | 4.0 | 3.5 |
| Excitement | 3.0 | 3.0 | 3.0 |
| Confidence | 4.0 | 4.0 | 4.0 |

**Director 评分理由**：

论文的核心优势——correlation-selection gap 概念的原创性、标杆级统计方法论、极其全面的分析覆盖——使其在方法论严谨性上达到了很高水准。然而三个结构性弱点限制了其 impact：

1. **模型覆盖面过窄**（唯一 Must-Fix 共识）：仅 2 个 ~8B 模型族，且 Table 43 明确显示 degeneracy 是 model-family-dependent，直接削弱普适性声称。
2. **唯一的建设性贡献统计边际**：Entity construction 全局 Holm p_adj=0.055，仅在 1/3 数据集上有正增益，不足以支撑三大贡献之一的定位。
3. **并行发现降低新颖性溢价**：Landesberg (2026) 的 concurrent discovery 使 gap 本身不再是独占性发现，论文需要更强地论证诊断框架的增量价值。

论文以负面结果为主（"SC 对 NER 无效"），建设性部分弱。负面结果论文要达到 Conference 水准需要更广的适用范围或更强的机制洞见来补偿 impact 不足。当前的 2-model-family + single-dataset-conditional-gain 组合不足以达到这一门槛。

**Findings 定位合理**：诊断分析本身扎实、统计透明度极高、可复现性强，适合作为 Findings 论文为后续工作（如扩展到更多模型家族、其他结构化预测任务）提供基础。

---

### Detailed Comments

**分歧解决记录**：

| Issue | R1 | R2 | Director 判定 |
|-------|----|----|--------------|
| R1-N1 Failure mode 层次化 | Must-Fix | REBUT→Should-Fix | **Should-Fix** (W4)。隐式层次已存在，显式化是 editorial 改进 |
| R1-W1 Bound 过松 | Should-Fix | REBUT→Minor | **不列入 weakness**。Bound 作为 necessary condition 确认负面结果，looseness IS the point |
| R2-W4 实践指导 | REBUT | Should-Fix | **Should-Fix** (W7)。内容存在但可见性不足 |
| R1-W4 Abstract >200 词 | Should-Fix | AGREE | **撤销**。Director 验证 abstract ~172 词，在 200 词限制内。两位 Reviewer 的视觉估计有误 |

**格式合规检查**：
- ✅ Abstract ≤200 词（~172 词）
- ✅ 主文 8 页（符合 EMNLP 2026 限制）
- ✅ Limitations 在正文中（非 Appendix）
- ✅ 双栏 ACL 模板
- ✅ 匿名审稿（author 为 "Anonymous"）