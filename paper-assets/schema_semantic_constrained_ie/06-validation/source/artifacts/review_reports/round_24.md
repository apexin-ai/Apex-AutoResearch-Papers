---
round: 24
review_mode: fresh
overall_score: 3.5 (Borderline Conference)
timestamp: 2026-05-23T09:39:48.859779+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 24 审稿报告 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

**Venue**: EMNLP 2026 (ARR) · Long Paper · Deadline 2026-05-25
**Reviewer 编排**: R1 (方法严谨性+实验设计) · R2 (新颖性+完整性+写作)
**流程**: Round 1 独立初审 → 交叉分享 [AGREE]/[REBUT] → 收敛 → 报告

---

## Summary

论文提出 OntoCoDec，将 IE 本体约束编译为两层 token 级解码约束：grammar 层（CFG/XGrammar）强制结构和词汇有效性，semantic 层通过动态 entity registry 运行时 logit masking 强制 domain/range 类型约束。评估涵盖 SciERC (7 rels)、DocRED (96 rels)、WikiEvents (EE pilot)，3 个 8B 模型 + 1 个 70B 模型。核心结果：LoRA + greedy S1 将 DR 降至 <0.1% (R-F1 41–47%)，beam k=4 消除所有违规类型 (1.54× latency)。论文提供了三级类型约束可判定性分类和系统消融。

---

## Strengths

1. **问题定义清晰且有实践价值**：DR/CF/RV/ET 四类违规分类体系化，violation landscape 量化分析（SciERC 15.4%, DocRED 18.5% baseline DR）直接motivate了约束解码的必要性。

2. **五路消融设计系统**：Table 1 的 unconstrained / grammar-only / GCD-equiv / semantic-only / S1 / S2 清晰隔离了各层贡献。"Empirical enabling dependency"（grammar 3% + semantic 24% → 组合 94%）是有信息量的 empirical finding。

3. **三级可判定性分类有架构指导意义**：context-free / prefix-decidable with state / non-local 的分类为约束解码系统设计提供了概念框架——明确了哪些约束用 CFG、哪些需有状态运行时、哪些无法在线解决。[R1-S1]

4. **统计方法论在核心实验上严谨**：Bootstrap CIs (10,000 iterations, document-level resampling)、Bonferroni 校正 (k=4, α_adj=0.0125)、Cohen's d (all δ≥3.0)、vLLM 外部验证。[R1-S3]

5. **分析诚实度高**：坦诚 CF 引入（zero-shot 0→9.82pp, fine-tuned +1.18pp）、WikiEvents pilot 限制（n=20, MDE≈±5pp）、GoLLIE 对比不可行原因、κ 统计效力不足。30 页附录覆盖近乎所有 reviewer concern。[R1-S4, R2-S3]

6. **工程贡献实用**：grammar-first fallback 保持 JSON 完整性；continuation masking 跨 3 个 tokenizer family 工作；runtime overhead 合理（fine-tuned S1 仅 +10%）；INT4 quantization 不影响 enforcement。[R1-S5, R2-S5-6]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical] **Proposition 1 的呈现定位过高，理论-实践 gap 桥接不充分**
- R1-N1 + R2-N1，交叉回应后达成部分共识。
- Proposition 1 证明无界实体集下 domain/range 约束非 context-free——证明技术本身是标准的（pumping lemma），论文自称 "well-known intuition" 的形式化。"Engineering applicability" 段用 DFA 状态数 $O(|\mathcal{E}|^{|\text{entities}|}) > 10^{17}$ 桥接有界场景，但 (a) 这是复杂度论证而非形式不可能性；(b) 未给出 DFA 可行的边界条件（如 SciERC: 6 types, ~10 entities → $6^{10} \approx 6 \times 10^7$，可能可行）；(c) proof sketch 在正文中仅 3 行，读者需翻 Appendix O 才能评估。
- **R1 与 R2 分歧**：R2 认为 Prop 1 trivial，整体降格为纯工程贡献；R1 认为三级分类法有架构指导价值，Prop 1 的应用意义超过证明技术本身。
- **Director 判定**：R1 的 rebuttal 有说服力——三级分类法确实为约束解码架构设计提供了有用的概念框架，论文贡献并非仅 Proposition 1 一个定理。但当前呈现方式确实将 Prop 1 过度包装为 "theoretical grounding"（§1 Contribution 1）。此问题属于 **framing/呈现**，非实质缺陷。
- **建议**：(1) §3 明确区分理论不可能性（无界）与工程不可行性（有界指数级），给出 DFA 可行边界；(2) 将 Prop 1 定位为 "formalizing a known intuition for the IE setting" 而非暗示全新理论发现；(3) 扩展 proof sketch 引用 pumping lemma 核心直觉。

**MF2** [critical] **κ-DR 相关性 n=3, p=0.138 在正文和 Abstract 中呈现不当**
- R1-N2 + R2 AGREE（完全共识）。
- §4 标注了 "descriptive (n=3, p=0.138)"，但 Abstract 第 3 段仍用 "rates correlate with schema restrictiveness"，§1 Contribution 2 同样暗示因果关联。附录回归线拟合 3 个点无统计意义。
- **建议**：Abstract/§1 将 "correlate" 统一替换为 "observed pattern across three schemas, insufficient for statistical inference"；附录回归线标注 "illustrative only, n=3" 或移除。

**MF3** [critical] **70B 验证单一模型族 + 无 FP16 基线，Contribution 2 "4 models" 表述误导**
- R1-N3 + R2 AGREE（完全共识）。
- 70B 仅 Llama-3.1-70B-Instruct (AWQ INT4)。无 Qwen-70B 或其他族验证。S2 在 70B 退化 -8.45pp 的解释（"over-constraining"）是 post-hoc 的，缺乏机制性证据。Contribution 2 声称 "4 models spanning 8B–70B" 实为 3×8B FP16 + 1×70B INT4，misrepresent 了验证范围。
- **建议**：(1) 将 70B 定位为 "preliminary single-family validation"；(2) Contribution 2 拆分 8B/70B 声明层级；(3) 为 S2 退化提供机制性解释或标注 "requires further investigation"。

### Should-Fix（影响评分但不一票否决）

**SF1** [warning] **缺乏与强 baseline 的明确定位声明**
- R2-N2，R1 rebut 认为已有 GCD-equiv/post-hoc filtering/GoLLIE 三类对比。Director 判定 R1 rebuttal 部分成立——论文确实提供了多层对比，但正文未明确声明 OntoCoDec 是约束执行方法而非 IE 系统。
- **建议**：§1 或 §5 增加定位声明："OntoCoDec is a constraint enforcement method, complementary to training-based schema-aware approaches"；考虑增加 post-hoc type repair（修复而非丢弃）baseline。

**SF2** [warning] **R-F1 41–47% 在正文中缺乏上下文**
- R2-N3，R1 rebut 有效（task setting 不同，supervised span-based 方法不可比）。但正文（§5 Setup）完全未提及 LLM-based generative RE 的典型 F1 范围，仅在 Appendix 有 SOTA 参考。
- **建议**：§5 Setup 增加 1-2 句定位说明。

**SF3** [warning] **WikiEvents pilot Table 3 正文位置具误导性**
- R1-W2 + R2-W1（完全共识）。n=20, MDE≈±5pp, 所有对比未达显著性。Table 3 在正文中与 Table 1/2（551/998 docs 完整评估）等位呈现。
- **建议**：Table 3 移至 Appendix，正文用 1-2 句概述 pilot 结论。

**SF4** [warning] **First-seen semantics 级联错误影响未量化**
- R1-W1 + R2 AGREE（完全共识）。245 CF violations 中多少源于 first-seen 错误 vs 合法类型歧义（Generic↔X）未分离。
- **建议**：增加统计——多次出现实体中 first-seen type 与 gold type 不一致比例及其导致的 CF 数。

**SF5** [warning] **§7 Discussion 仅 8 行过于压缩**
- R2-W3 + R1 隐含同意。缺少 DR↔CF trade-off 定量讨论、与 training-based enforcement 互补关系、per-triple vs global enforcement 根本张力。
- **建议**：压缩 §6 Related Work（当前约 1.5 页偏长）释放空间，§7 扩展至少 3 段。

**SF6** [warning] **Contribution 2 过度打包**
- R2-W5 + R1 AGREE（完全共识）。一个 bullet 包含 4 models × 2 precisions × 2 datasets + pilot + scale interaction。
- **建议**：拆分为 2-3 条聚焦的贡献。

**SF7** [warning] **LoRA 超参从 SciERC 直接转移到 DocRED 缺乏论证**
- R1-W4 + R2 AGREE（完全共识）。SciERC (7 rels, 551 短句) vs DocRED (96 rels, 998 长文档) 差异大。
- **建议**：Appendix 增加 DocRED LoRA rank/α 敏感性分析（至少 2-3 配置）；或正文承认超参转移可能低估 DocRED 潜力。

**SF8** [warning] **Beam search 作为 CF 解决方案的实用性讨论不足**
- R1-W5 + R2-W2（共识）。k=4 1.54× latency，但未讨论 k=2 是否足够、70B 内存开销、fine-tuned 下 CF 已低时 beam 边际收益。
- **建议**：增加 beam width sensitivity 讨论和 fine-tuned 下边际收益评估。

### Minor（不影响接收）

- GCD-equiv 等价性仅 Qwen3-8B 验证（R1-W3, R2 AGREE severity 低）——建议脚注说明
- 约束来源（训练数据 vs 形式本体）在 §2/§5 区分不够明确（R2-W4, R1 部分 rebut）——建议增加区分说明
- Abstract "Composed with LoRA fine-tuning" 认知负担高——建议调整语序
- Table 1 caption "F1 ×100" 易被忽略——建议表头标注 "F1 (%)"
- "Engineering applicability" 段与 proof sketch 之间缺过渡（R1 minor 4）

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识 [AGREE]：
1. κ-DR n=3 相关性在正文中呈现方式不当（MF2）
2. 70B 验证范围不足以支撑 "scale robustness" claim（MF3）
3. WikiEvents pilot Table 3 应移出正文或加强 caveat（SF3）
4. First-seen semantics 级联错误缺乏量化（SF4）
5. §7 Discussion 过于压缩（SF5）
6. Contribution 2 过度打包（SF6）
7. LoRA 超参跨数据集转移缺乏论证（SF7）
8. Beam search CF 缓解实用性讨论不足（SF8）

## Reviewer Divergence

以下问题存在分歧，各方理由记录：

**D1: Proposition 1 的 novelty 价值**
- R2 (3.0): Trivial——PDA 无法随机访问是基础知识，论文降格为纯工程贡献
- R1 (3.5): 三级分类法有架构指导价值——Prop 1 在 IE 设定下的应用意义超过证明技术本身
- Director：R1 rebuttal 部分有效。分类法确有贡献，但呈现定位过高。纳入 MF1 但核心是呈现问题。

**D2: 强 baseline 是否充分**
- R2: 仅与 grammar-only strawman 比较，缺 GoLLIE/KnowCoder 可比实验
- R1: 论文已有 GCD-equiv + post-hoc filtering + GoLLIE 三层对比；OntoCoDec 是约束执行方法非 IE 系统，要求 R-F1 对标是范畴错误
- Director：R1 rebuttal 大部分有效。论文定位声明缺失是主因，非实质缺少对比。降为 SF1。

**D3: R-F1 41–47% 的绝对质量**
- R2: 与 SOTA (50%+/60%+) 差距大，削弱约束执行的实际意义
- R1: Task setting 完全不同（generative LLM vs supervised span-based），41–47% 在 LLM-based generative RE 中合理
- Director：R1 rebuttal 有效。Supervised 对标不恰当。但正文确需上下文定位。降为 SF2。

---

## Questions（需作者澄清）

1. **Q1**: Proposition 1 proof sketch 中 position-based indexing 的简化不影响结论——能否提供更正式的论证说明 name-based referencing 不会使语言变为 context-free？[R1-Q1; R2 代论文 rebut 但应由作者确认]

2. **Q2**: Fine-tuned 设置下 fallback triple 的 precision 是多少？如果 fallback 总导致错误输出，0.46% 触发率意味着 ~6% 文档受影响。[R1-Q4]

3. **Q3**: 70B S2 退化 -8.45pp 的机制性原因？是否与 INT4 量化加剧过约束有关？8B 上 FP16 vs INT4 的 S2 表现是否有差异？[R1-Q3, R2 AGREE]

4. **Q4**: Per-relation κ 分层 DR reduction 分析——低 κ 时 semantic layer 的边际效果是否系统性减弱？EVALUATE-FOR (κ=0.361) 的非零 violation 是否代表了一个系统性边界？[R1-Q5, R2 AGREE]

---

## Missing References

两位 Reviewer 共提出 7 条 missing reference，经交叉验证后：

**需要验证并考虑引用的**：
1. KG-Trie (arXiv:2410.13080) — Trie 编码 KG 约束到解码过程 [R2]
2. Dialogue Ontology RE via Constrained CoT (arXiv:2408.02361) — ontology 约束 + CoT [R2]
3. Outlines 2024-2025 更新 — regex-based constraints + jump-forward optimization [R1; R2 认为核心仍是 CFG，影响较小]

**可能不存在/需进一步确认的**：
4. SciDC (arXiv:2604.06603, Apr 2026) — 2026 年 4 月论文，可能是 concurrent work [R2; 需验证真实性]
5. Format Tax (arXiv:2604.03616, 2026) — 需核实是否与已引用 FormaTax 为同一工作 [R2]
6. NuneroPlan (Zhu et al., 2024) — R2 搜索未找到，**可能是 R1 hallucinated reference** [R1; R2 REBUT]
7. Dong et al. (2024) RAG schema-compliant IE — R2 找到最接近匹配为 arXiv:2505.08690 (2025)，**出处无法验证** [R1; R2 REBUT]

---

## External Review

**状态**：未配置。项目未启用 paperreview.ai 外部审稿。

---

## Visual Layout Check（非评分项）

**状态**：已完成（4 warnings, 0 critical, 12 info）

**Warnings**：
1. 前两页纯文本无 display item，Figure 1 到第 3 页才出现——建议提前至第 2 页加速认知锚定
2. 主文 8 页仅 4 个 display items（1 fig + 3 tables），对实证论文偏少（推荐 5-8 个）——缺少主结果可视化图表（如 DR/F1 trade-off bar chart）
3. Page 4-5 连续两页纯文本（Method §3.2-3.4 + §4），视觉节奏单调——建议插入约束组合示例图或伪代码
4. Page 8 Related Work + Discussion 纯文本，审稿人快速扫描易疲劳

**Info highlights**：Table 1/2 排版质量良好；Figure 1 架构图清晰；Limitations 长度适中符合 EMNLP 规范；无 LaTeX 错误残留或未解析引用。

---

## Overall Assessment

**评分**: 3.5 / 5 (Borderline Conference)
**置信度**: 4 / 5

**评分理由**：

论文提出了一个有清晰理论动机和系统实验验证的两层约束解码框架。核心贡献——将 IE 本体约束编译为可组合的 token 级解码约束——新颖且有实践价值。三级可判定性分类为 IE 约束解码架构提供了有用的概念框架。五路消融设计系统，统计方法论在核心实验上严谨，30 页附录展现高度科学诚实度。

主要顾虑：
1. **Novelty 天花板**（R1/R2 分歧焦点）：核心方法是 XGrammar + stateful logits processor 的系统集成。Proposition 1 的证明技术标准，分类法有指导价值但不构成深层理论创新。R2 认为不足以进入 main conference (3.0)，R1 认为系统贡献 + 分类法超过 Findings (3.5)。Director 认为整体贡献（分类法 + 系统设计 + 全面实证）在 Borderline Conference 水平。
2. **统计声明**：κ-DR n=3 相关性呈现不当（MF2）；WikiEvents n=20 underpowered（SF3）。
3. **验证覆盖度**：70B 单一模型族 + 单一精度（MF3）；LoRA 超参未跨数据集调优（SF7）。
4. **CF trade-off 讨论不足**：greedy S1 引入 CF 作为 DR elimination 的副作用，Discussion 中讨论不充分（SF5/SF8）。

**可修改性**：所有 Must-Fix 和 Should-Fix 均为呈现/分析/定位问题，无需新实验（除 SF7 LoRA 敏感性）。如果 MF1-MF3 + SF1-SF2 在 revision 中得到充分回应，评分可上调至 **4.0 (Conference)**。

**R1 vs R2 评分差异说明**：R1 (3.5) 认为方法论贡献超过 Findings 门槛，R2 (3.0) 认为 novelty 不足。核心分歧在于对 "系统集成 + 形式化分析" 的 novelty 判断标准。Director 倾向 R1 立场——三级分类法对领域有概念指导价值，全面消融和诚实的局限性分析体现了高标准的实证研究，整体超过 Findings 但尚未稳定进入 Conference 水平。

---

## Detailed Comments（逐节）

### Abstract
- "rates correlate with schema restrictiveness" → 替换为 "observed pattern" (MF2)
- "Composed with LoRA fine-tuning" 在框架解释前出现，认知负担高 → 调整语序

### §1 Introduction
- Contribution 1："theoretical grounding" 定位过高 → 改为 "formalizing a known intuition" (MF1)
- Contribution 2：过度打包 → 拆分 2-3 条 (SF6)
- 增加明确定位声明："constraint enforcement method, complementary to training-based approaches" (SF1)

### §2 Background
- 更明确区分形式本体 (KAIROS) vs 训练数据推导 schema (SciERC/DocRED) (Minor)

### §3 Method
- Proposition 1 proof sketch 扩展：引用 pumping lemma 核心直觉 (MF1)
- "Engineering applicability" 给出 DFA 可行边界条件 (MF1)
- First-seen semantics：增加级联错误量化 (SF4)

### §4 Constraint Composition
- κ 相关性：统一 "observed pattern" 措辞 (MF2)
- 附录回归线标注 "illustrative only" (MF2)

### §5 Experiments
- Setup：增加 LLM-based generative RE 典型 F1 范围 (SF2)
- §5.1：R-F1 上下文定位 (SF2)
- §5.2 WikiEvents：Table 3 移至 Appendix (SF3)
- 70B：标注 "preliminary single-family validation" (MF3)
- Beam search：增加 beam width sensitivity + fine-tuned 边际收益讨论 (SF8)

### §6 Related Work
- 考虑检查 KG-Trie、Dialogue Ontology RE via Constrained CoT 是否需要引用
- 可适当压缩释放空间给 §7

### §7 Discussion
- 扩展至少 3 段：DR↔CF trade-off 定量 + training-based 互补 + per-triple vs global (SF5)