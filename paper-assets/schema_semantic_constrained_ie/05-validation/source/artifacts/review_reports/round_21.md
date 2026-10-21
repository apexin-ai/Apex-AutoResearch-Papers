---
round: 21
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T03:04:52.379392+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# Round 21 审稿报告 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

**Target Venue**: EMNLP 2026 via ARR May 2026
**Reviewers**: R1（方法严谨性 + 实验设计 + 统计检验）、R2（新颖性 + Related Work + 写作质量）
**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT）→ 收敛

---

## Summary

论文提出 OntoCoDec，将 IE 本体编译为可组合的 token 级解码约束。两层架构：grammar layer（CFG，保证 JSON 结构和词汇约束）+ semantic layer（有状态实体注册表，运行时执行 domain/range 类型检查）。Proposition 1 形式化证明 domain/range 约束非 context-free，为二层分离提供理论基础。实验覆盖 3 个数据集（SciERC, DocRED, WikiEvents）、3 个 8B 模型 + 70B 验证、zero-shot 与 fine-tuning，展示 DR 降至 <0.1%（fine-tuned）。评估规模罕见（38 页 47+ 表格），分析深度突出（CF↔DR trade-off、组合性分析、error taxonomy）。

---

## Strengths

**S1. 理论基础严谨** [R1+R2 共识]
Proposition 1 使用泵引理正式证明 domain/range 约束对无界实体集不是 context-free，Appendix O 完整证明逻辑链无可挑剔。这为 grammar 层之上需要第二层提供了不可简化的形式论据，解释了为什么 GCD/BoostCD 等纯 CFG 方法仅能达到 ~3% DR reduction。

**S2. 约束组合框架设计精巧** [R1+R2 共识]
§4 Eq. 2 的非对称合取 M_final(t) = M_grammar(t) ∩ M_semantic(t)，配合 grammar-first fallback（S(t)∩G(t)=∅ 时 fallback 到 G(t)），在理论完备性和工程可行性之间取得正确平衡。

**S3. 评估规模在约束解码文献中罕见** [R1+R2 共识]
38 页 47+ 表格，覆盖 5-way zero-shot ablation、4-way fine-tuning composability、跨数据集/跨模型/跨规模验证、beam search 兼容性、runtime profiling、error taxonomy、schema ambiguity analysis 等。

**S4. 诊断指标体系设计良好** [R1]
DR/CF/RoV/ET/RV 提供了比 F1 更细粒度的约束执行评估，使读者能精确定位各约束层的贡献。

**S5. 统计报告有亮点** [R1+R2 共识]
Fine-tuning 结果正确使用 Bonferroni 校正（k=4, α=0.0125），诚实报告 R-F1 改善在校正后不显著，而 DR reduction 均显著（all p < 0.003）。这种透明度在该领域不常见。

**S6. 组合性分析框架有独立价值** [R1+R2 共识]
双因素定量分析（Figure 2）揭示 schema tightness (κ̄) × baseline violation rate 共同支配 DR reduction，R²=0.886，为实践者提供可操作指导。（但 n=6 统计可靠性有限——见 W5。）

**S7. 错误分析深入且诚实** [R1]
Appendix J 的 error taxonomy + Appendix K 的 lucky violation 分析 + Appendix N 的 schema ambiguity 分析展示了对问题的深入理解和科学严谨性。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. Abstract 对 CF 副作用的选择性报告** [R2-W1, Major; R1 AGREE]
Abstract 报告 "up to 1.18% under greedy decoding on well-calibrated models"，选择了 CF 的最优情况。Table 1 显示 CF 实际范围为 0.08–12.02%（DocRED, Qwen, zero-shot S2 配置可达 ~10%；Limitations 承认 "up to 12.02%"）。通过限定 "well-calibrated models" 和 "greedy decoding" 两个条件选择性报告最低值，误导读者对方法代价的第一印象。
- **两位 Reviewer 共识**：Abstract 应呈现 CF 的完整范围（如 "0.46–12.02% depending on model calibration"），保留 beam search 和 fine-tuning 作为缓解方案的描述。
- **严重程度**：这是一个信任度问题。从 Round 15 至今（7 轮）反复出现的持续性问题——每轮修改后仍被审稿人标记。

### Should-Fix（影响评分）

**SF1. WikiEvents 评估统计效力不足** [R1-W1, Major; R2-W6, Minor; 共识]
WikiEvents 仅 20 篇文档（n=246 gold triples），Table 31 CI 为 ±3.0pp，§5.4 报告的 argument F1 shift ±1.1pp 完全在噪声范围内。论文自称 "preliminary" 但仍在 §5 中作为四大实验之一呈现，并列入 contribution list。
- 建议：(1) 从 Abstract 删除 WikiEvents 数据；(2) contribution list 中标注初步性质；(3) 正文中明确定位为 pilot study。

**SF2. 70B AWQ INT4 量化混淆因素未控制** [R1-W2, Major; R2 AGREE]
所有 70B 实验使用 AWQ INT4 量化（仅 Llama-3.1-70B），约束解码直接操作 logit 分布，量化可能在 mask 边界处扭曲 logits。Limitations 中仅一句带过。70B semantic-only 的 84% DR reduction 这一关键发现的可信度受此影响。
- 建议：在 8B 上对比 FP16 vs INT4 的 DR/CF 指标，量化 quantization artifact 影响。即使小规模实验也能大幅增强 70B 结论可信度。

**SF3. Abstract 信息密度过高** [R2-W3, Minor; R1 AGREE]
Abstract ~150 词中包含 12+ 数字/百分比和 5+ 首次出现缩写（DR, CF, RE, R-F1, LoRA），冷读极为困难。顶会 Abstract 最佳实践：≤3-5 个关键数字 + 定性描述。
- 建议：三段式结构（问题 → 方法 → 关键结果），减至 4-5 个 headline 数字。

**SF4. Abstract/Intro DR 范围不一致** [R2-W4, Minor; R1 AGREE]
Abstract "42–90% on DocRED" vs Introduction "42–99% across models and datasets"——虽然后者是跨数据集合并范围，但并列造成不必要混淆。

**SF5. "Enabling dependency" 术语过强** [R1-W4, Minor; R2 AGREE]
"Empirical enabling dependency" 在 §5.1 中用于描述 n=6 配置的观察。R²=0.886 基于 6 个点可能严重过拟合。
- 建议：改为 "observed complementarity pattern"；补充 adjusted R² 或 leave-one-out CV。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 达成完全共识：

1. **Overall 3.5 Borderline Conference**——理论扎实、评估全面，但 novelty ceiling 和统计检验问题制约接收信心
2. **Abstract CF 选择性报告是信任度问题**（MF1）
3. **WikiEvents n=20 统计效力不足**（SF1），不应在 Abstract/contribution 中引用
4. **70B AWQ INT4 是未控制的混淆因素**（SF2）
5. **Abstract 信息密度过高**（SF3）
6. **DR 范围数值不一致需修正**（SF4）
7. **κ̄/enabling dependency 术语过强**（SF5）
8. **Figure 1 应可视化 grammar-first fallback 路径**
9. **DocRED dev set 评估应在 Limitations 中声明**
10. **评估规模和诊断指标体系是论文亮点**

---

## Reviewer Divergence [REBUT]

以下问题存在分歧，各方理由如下：

### D1. Zero-shot 核心消融（Table 1）是否需要统计检验
- **R1 立场** [Critical Must-Fix]：Table 1 的 5 配置 × 2 模型 × 3 数据集消融仅有点估计，无 CI/显著性检验/效应量。Enabling dependency 主张缺乏统计证据。Fine-tuning 部分（Table 8）已正确使用 Bonferroni 校正，与 zero-shot 部分形成不一致。
- **R2 立场** [REBUT]：Zero-shot greedy 解码是确定性过程（temperature=0，固定权重+prompt），bootstrap CI 在统计学上无意义。跨模型变异（3 models × 2 datasets）已提供 robustness。Table 31 (document-level CI) + Table 35 (prompt sensitivity) 已覆盖。建议在 Table 1 caption 中声明确定性并引用 robustness 参考。
- **Director 判断**：R2 的 rebuttal 在统计学原理上有道理——确定性过程确实不需要传统 CI。但 R1 的关切也有效——读者可能期望一致的统计标准。折中方案：声明确定性 + 引用已有 robustness 证据 + 可选补充 document-level bootstrap。降级为 Should-Fix。

### D2. Full FT 组合性是否"失效"（Table 42）
- **R1 立场** [Critical Must-Fix]：Full FT + S1 的 R-F1（37.89）与 unconstrained 完全相同，约束"零贡献"。如果 full FT 已内化约束，对 "decoding-time enforcement is necessary" 构成反证。
- **R2 立场** [REBUT with data]：Table 42 数据显示 full FT unconstrained 仍有 DR=2.74%（高于 LoRA 的 1.18%），S1 使 DR→0% 且 F1 不变。R1 将"F1 不变"误读为"约束无效"，但 DR→0% 恰恰是约束有效的证明。F1 不变 + DR→0% 是理想结果。
- **Director 判断**：R2 的 rebuttal 有数据支撑，R1 的解读确实混淆了 F1 不变与约束无效。但论文可在 Appendix L 中更显式突出 full FT 的 DR 数据。降级为 info。

### D3. 核心技术新颖性评判
- **R2 立场** [Major]：Grammar layer 等价于 GCD/BoostCD（Table 17 确认），semantic layer 本质是运行时查表。Proposition 1 被 Remark 削弱（实际语言 regular，只是 DFA 太大）。论文自述 "systematic engineering contribution with theoretical grounding"——novelty ceiling 有限，更适合 Findings。
- **R1 立场** [Partial REBUT]：Semantic layer 非简单查表——动态 entity registry 需解决 greedy commitment、fallback cascade、跨三元组类型一致性。Proposition 1 的 Remark 不削弱核心结论（CFG 不充分），而是补充 DFA 工程不可行性。但同意 novelty ceiling 存在。评价应为 "moderate novelty with strong execution"。
- **Director 判断**：两方均有合理成分。核心技术确实是已知组件的组合（CFG + 运行时类型检查），但组合框架（Eq. 2 + fallback + composability）的设计选择非 trivial。论文自身 "systematic engineering contribution" 定位诚实。最终判断：novelty 处于 moderate 水平，不足以独立支撑 Conference acceptance，但强执行和分析深度弥补了部分 novelty 不足。

### D4. 是否需要 GoLLIE/KnowCoder 正面对比
- **R1 立场** [Major]：应在同一 benchmark 上对比 violation rates 或 F1。GoLLIE 在 SciERC、KnowCoder 在 DocRED 有公开结果。
- **R2 立场** [REBUT]：跨范式（decoding-time vs training-based）正面实验对比不可行（不同训练流程/模型/prompt）。§6 已有间接对比（GoLLIE R-F1=0.0），Table 16-17 有 GCD-equivalent baseline。
- **Director 判断**：R2 的可行性论点合理——完整复现 GoLLIE/KnowCoder 超出合理实验范围。但论文可在 Related Work 中增加系统性对比表格（引用原文数据），列出不同方法的 violation handling 策略。降级为可选改进。

---

## Questions

1. **Beam search registry 管理**：k=8 时每个 beam 独立 registry 的内存开销是多少？Appendix F 报告了 latency 但未量化 memory。[R2-Q1, R1 AGREE]
2. **TCR 整合可行性**：为什么不将 post-hoc TCR 整合到解码循环中？是否涉及 NP-hardness 的搜索空间问题？[R2-Q2, R1 AGREE]
3. **GCD/BoostCD 运行方式**：Table 16-17 的对比是直接运行 GCD/BoostCD 代码，还是基于等价论证推断？[R2-Q3, R1 AGREE]
4. **DR=0% 跨种子稳定性**：Table 2 Llama S1 SciERC DR=0% 是否仅 seed=42？其他种子是否仍 0%？[R1-Q4, R2 AGREE]
5. **TCR vs OntoCoDec F1 对比**：TCR 减少 CF 18-92%，但对 DR 和 F1 影响未报告。TCR 是否是更实用的后处理替代？[R1-Q5, R2 AGREE]

---

## Missing References

两位 Reviewer 提出的参考文献补充建议：
1. **Text2Event** (Lu et al., 2021, ACL) — 序列生成事件抽取，与 WikiEvents 实验相关 [R2 提出, R1 部分同意]
2. **Huang et al. (2024)** "Planning for Constrained LLM Generation" — look-ahead 约束解码，与 beam search 分析相关 [R1 提出]
3. **DCCD (2026) 和 pldi2025_type_constrained_codegen** — venue/年份需核实是否已发表 [R2 提出, R1 同意]
4. DEGREE (Hsu et al., 2022, NAACL) — R2 提出但 R1 认为非必要（不涉及 constrained decoding）

---

## External Review (Stanford Agentic Reviewer)

**状态**：未配置。项目 config 中 `external_review.paperreview_ai.enabled` 未设置，本轮未请求外部审稿。

---

## Visual Layout Check（非评分项）

**状态**：done（耗时约 5 分钟）

视觉审查发现（2 warning + 4 info）：

**Warning:**
- 主文 8 页仅 1 个 figure（Figure 1 架构图），其余全为 table。缺少结果可视化图（如核心指标的 bar chart 或消融趋势图），削弱视觉印象。建议将附录中 Figure 2（DR vs Schema Restrictiveness）或 Figure 4（Beam width ablation）的关键子图提升到主文。
- Page 4 整页纯文本+公式（§3.2-3.4 + §4），在 Figure 1（p.3）和 Table 1（p.5）之间形成视觉空白页。

**Info:**
- Figure 1 内部分组件标签字号偏小，打印后可能接近可读性下限（建议 ≥ 8pt）
- Page 7 包含 Table 3 + Table 4，页面密集但未溢出
- 附录部分页面极度密集（p.25 四表、p.31 五表）
- 最后一页仅填充约 1/3，可调整分页

---

## Overall Assessment

**Overall: 3.5 — Borderline Conference**

**评分理由**：

论文解决了一个真实且重要的问题——LLM 生成的 IE 输出中 ontological violations 的系统性消除。Proposition 1 提供了严谨的理论基础（CFG 不充分），约束组合框架（Eq. 2）设计精巧，评估规模在约束解码文献中罕见。统计报告的诚实度（Bonferroni + 坦承 R-F1 不显著）是高标准的学术实践。

但以下问题制约了接收信心：
1. **Abstract CF 选择性报告**是跨 7 轮的持续性信任度问题
2. **核心技术新颖性处于 moderate 水平**——个别组件不新（CFG ≈ GCD, 类型检查 ≈ 运行时断言），论文自述 "systematic engineering contribution" 准确但指出了 novelty ceiling
3. **WikiEvents 统计效力不足**不应在 Abstract/contribution 中引用
4. **70B AWQ INT4 混淆未控制**影响 scaling 结论可信度

如果 MF1（Abstract CF framing）得到彻底修正，并补充 SF1-SF5 的改进，论文可推向 4.0（Conference）。当前状态处于 Conference 和 Findings 的交界。

**ARR 维度评分**：

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |
| Excitement | 3.5/5 | 3/5 | 3.25/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

---

## Detailed Comments

### §1 Introduction
- Contribution list 中 WikiEvents 结论应降级或标注 preliminary
- "42-99%" 范围应与 Abstract 保持一致

### §3 Method
- Proposition 1 严谨有效；Remark 补充 DFA 工程不可行性合理
- Semantic layer 的 greedy commitment 和 fallback cascade 设计选择可更显式论证其非显而易见性
- "Enabling dependency"/"Empirical Observation" 标签应匹配证据强度

### §4 Constraint Composition
- κ̄ 分析基于 n=6，需补充 adjusted R² 或 leave-one-out CV
- 术语从 "enabling dependency" 降级为 "observed complementarity pattern"

### §5 Experiments
- Table 1 应在 caption 声明 greedy 确定性并引用 robustness 参考（Table 31/35）
- WikiEvents 明确定位为 pilot study
- 70B 结论需加量化 disclaimer

### §6 Related Work
- 考虑补充 Text2Event 引用
- PICARD 对比可在 Appendix B 中深化
- 核实 DCCD/pldi2025 引用的 venue 和年份

### §7 Discussion and Conclusion
- 论文自述 "systematic engineering contribution" 定位准确，无需修改

### Limitations
- DocRED dev set 评估应显式声明
- Full FT composability 数据（DR 2.74%→0%）应更突出呈现

### 视觉建议（非评分项）
- 正文仅 1 figure，建议从附录提升一个结果可视化图
- Page 4 视觉空白，考虑提前 Table 1 或插入小型示意图
- Figure 1 组件标签确保 ≥ 8pt
