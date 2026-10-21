---
round: 15
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T10:30:30.239957+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 18 (Fresh)

**论文**: Beyond Self-Consistency: Self-Extracted Constraints Do Not Improve LLM Logical Reasoning
**Venue**: EMNLP 2026 via ARR | **Deadline**: 2026-05-25
**Reviewer 编排**: R1（方法严谨性 + 实验设计）, R2（新颖性 + 完整性 + 写作质量）
**交叉分享**: 完成，关键问题高度收敛

---

## Summary

论文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理 trace 中提取逻辑约束并通过 MAX-SAT 选择答案。核心发现为负面结果：自提取约束因 "symbolic confirmation bias"（SCB）系统性对齐模型多数票答案，使 SICA 退化为多数投票。论文在 6 个开源模型 (7B–32B) + 5 个 frontier 模型、3 个核心数据集、27 种 training-free 修复策略上验证了这一现象，提供了理论分析（Proposition 1, Remark 1）和诊断框架（C₀, K_eff, BR），并展示 cross-architecture verification 作为初步 escape path。

---

## Strengths

**S1. 实验覆盖度和系统性极高 [R1, R2 共识]。** 6 个开源模型 + 5 个 frontier 模型的 cross-model extraction，3 个核心 + 3 个辅助数据集，27 种修复策略的系统排除，multi-seed replication (3-seed/4-seed)，oracle control 验证 MAX-SAT 机制 soundness (+29.90pp FOLIO, +17.17pp PW)。这种覆盖度在 negative-result 论文中极为罕见。

**S2. 统计方法论严谨 [R1, R2 共识]。** McNemar exact test + BH correction (m=16)、TOST equivalence test (±1/±2/±3pp sensitivity analysis)、bootstrap CI (10,000 resamples)、permutation null model (1,000 permutations)。论文坦诚报告 10/16 conditions underpowered，透明度值得肯定。

**S3. 诊断框架有实用价值 [R1, R2 共识]。** 三个 zero-cost diagnostics (C₀, K_eff, BR) 在全部 60 个测试条件上正确表征失败模式，并在两个 held-out model families (LLaMA-3.1-8B, Qwen3-14B) 上前瞻性验证。可直接被从业者采用。

**S4. Oracle control 设计精良 [R1]。** Gold annotations 替代自提取约束，干净分离 "MAX-SAT 机制是否 sound" 和 "自提取约束是否有效" 两个问题。

**S5. Permutation null model 验证 BR [R1]。** BR_null ≈ BR_obs (p > 0.7) 证实 bias ratio 由 trace-count base rate 解释——反而加强了论文核心论点（bias 是结构性的）。

**S6. Related Work 覆盖全面 [R2]。** 结构清晰的分类（specification-generation / program-generation / trace-extraction），与 Huang et al. (2024) 和 Wan et al. (2025) 的区分在概念上成立。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [critical, R1+R2 共识] 标题 "Do Not Improve" 与统计证据不匹配**
标题是全称否定命题，但 10/16 条件 underpowered（MDE 1.86–4.84pp, observed power < 21%），仅 4 条件通过 TOST 等价检验。论文自身承认 "Absence of evidence is not evidence of absence for small effects"（§4），与标题矛盾。Abstract 中 "find no evidence" 更审慎但标题未反映。R1 建议 "Provide No Detectable Improvement"，R2 建议 "Show No Evidence of Improving"——两种表述均优于现标题。

**W2 [critical, R1 提出 + R2 共识] Proposition 1 形式化不严谨**
假设 (i) 使用 |C^∖| ≈ 0 而非精确条件；假设 (iii) "approximately uniform constraint yield" 无数学定义（CV < δ?）且未直接验证（论文给出 extraction rate 但未展示每 trace 约束数量分布）；证明全程使用 ≈ 而非 =。结论通过 >90% 经验一致性支撑而非严格推导。作为论文理论核心支柱，应降格为 Empirical Observation 或给出误差界。R2 补充：配合 Remark 1 的 DPI 论证，即使降格核心论点仍成立。

**W3 [critical, R2 提出 + R1 部分共识] SCB 相对于 Huang et al. (2024) 增量新颖性论证不足**
论文定位为 "independent evidence consistent with" Huang et al.——风险是降级为 case study。§2 对 CoT bias（trace level）和 SCB（aggregation level）的区分是概念性的，缺少实证证据证明两者可分离（如控制 trace faithfulness 后 SCB 是否仍存在）。R1 指出论文实际贡献超出 case study（形式化、诊断框架、27 变体排除），但 "consistent with" 措辞自我降级，应改为 "extends"。

### Should-Fix（影响评分但不一票否决）

**W4 [major, R1 提出 + R2 共识] Remark 1 (DPI) 与 Figure 3 间存在 claim 升级**
I(C;Y) ≤ I(T;Y) 对任何确定性后处理 C = f(T) 成立，接近 trivial。真正有价值的 claim 是 Figure 3 DAG 中隐含的 C ⊥ Y | A——约束在给定答案后不携带关于真值的额外信息——但这个更强的条件独立性声明未被形式化证明。R2 补充：需在 Proposition 1 条件下显式证明 I(C;Y) ≤ I(A;Y)，将 trivial DPI 和 non-trivial C ⊥ Y | A 明确区分。

**W5 [major, R1 提出 + R2 共识] BR 指标的 by-construction 循环性**
Source-attribution scoring 下，多数 trace 产生 a_M → 多数约束 support a_M → BR > 1 几乎 tautological。Permutation test (BR_null ≈ BR_obs, p > 0.7) 证实 BR 完全由 trace-count base rate 解释。56.4% 零变量重叠使约束无法跨答案判别。R2 洞察：BR_excess ≈ 0 意味着 SCB 的 "bias" 完全来自结构性 source-attribution——这反而强化 Proposition 1 的 degeneration 论点，但需将 BR 从 "bias 度量" 重新框定为 "degeneration 度量"。建议报告 BR_excess = BR_obs - BR_null。

**W6 [major, R1+R2 共识] Cross-architecture escape (§6) 证据过弱**
(a) Spearman ρ=1.0 基于 n=6，Table 3 中 3 个 generator 的 Δ 在 0.50–0.83pp 几乎无差异，monotonicity 由 Mistral-7B 单个 outlier 驱动——实质是二元判断（generator 低于/高于 verifier）而非连续 pattern。
(b) Zero-shot DeBERTa 仅在最弱 generator (Mistral-7B, SC=39.33%) 上显著；domain-adapted verifier 引入 training 与论文 training-free 主线矛盾，混淆了 independence 和 supervision 两个因素。
(c) 仅 ProofWriter 一个数据集。
作为三个 contribution 之一，evidence base 不足。建议降级为 preliminary finding。

**W7 [major, R2 提出 + R1 共识] Scope 震荡**
标题说通用（"Self-Extracted Constraints Do Not Improve LLM Logical Reasoning"）；Contribution 1 说 SICA-specific（"Z3 verification becomes vacuous under self-extraction"）；Discussion 扩展到 "any self-verification method"。Proposition 1 假设是 SICA 设计选择（degeneration, source-attribution, uniform yield），非所有 self-extraction pipeline 共性。Remark 1 的 DPI bound 更通用但接近 trivial。需在 §1/§5/§7 明确区分 SICA-specific 结论（Proposition 1）和一般性结论（Remark 1）。

**W8 [moderate, R2 提出 + R1 AGREE 降级] "LLM Logical Reasoning" 标题范围与实验覆盖不匹配**
实际测试包含 FOLIO/PW（FOL）、LogiQA（NL 逻辑）、StrategyQA（常识）、GSM8K/AIME（数学），但 GSM8K/AIME 在 degenerate regime (C₀ < 5%)，StrategyQA 仅一个模型。核心有效测试集中在 FOLIO 和 ProofWriter。R1 认为严重性低于 major——核心机制不依赖推理类型。建议标题去掉 "Logical"。

**W9 [moderate, R2 提出 + R1 共识] K_eff 缺少直觉解释**
Eq. 1 后应加一句 "K_eff measures how many effectively independent votes K correlated traces contribute"。Abstract 中 K_eff 首次出现时也需括号解释（如 "effective independent sample count"）。修改成本极低。

**W10 [moderate, R1 提出, R2 部分 REBUT] TOST ±2pp margin 选择依据**
R1 认为 FOLIO 近二分类，1pp/class 阈值不适用。R2 REBUT：FOLIO 实为三分类 (True/False/Unknown)，±2pp ≈ ±0.67pp/class 在三分类上合理。共识：需在 §4 区分二分类 (ProofWriter) 和三分类 (FOLIO) 数据集的 margin 适用性。

### Nice-to-Have

- **M1 [minor, R2 提出, R1 REBUT]** Abstract 信息密度高但 R1 认为适合 ACL/EMNLP venue。共识：在 Abstract 中给 K_eff 加括号解释即可。
- **M2 [minor, R1]** Table 1 中 Mistral-7B multi-seed 行间关系需在 caption/脚注说明（s123/s456/s789 vs. 3s aggregated）。
- **M3 [minor, R1]** 56.4% 零变量重叠的计算粒度需说明（per-problem? per-dataset?）。
- **M4 [minor, R1+R2]** Appendix Y (Extended Discussion) 中 SCB evaluation framework 内容有价值但缺乏主文指引。
- **M5 [minor, R2 提出, R1 REBUT]** "Symbolic Mirage" 作为 Section 标题——R2 认为稍 dramatic，R1 REBUT 认为准确且 ACL 常见。保留。
- **M6 [minor, R2 提出, R1 REBUT]** Limitations 仅约 50 词——R2 认为偏短，R1 认为符合 EMNLP 规则（3 点即可）。R1 判断合规。
- **M7 [minor, R1]** Z3 3.4% rejection rate 应在 Method/Results 开头更早指出 vacuous verification。

---

## Reviewer Consensus

以下问题两位 Reviewer 独立达成 [AGREE] 共识：

1. **标题 overclaiming** [W1]：最高优先级修改项。"Do Not Improve" → "Provide No Detectable Improvement" 或类似表述。
2. **Proposition 1 形式化不足** [W2]：降格为 Empirical Observation 或补充误差界。
3. **Cross-architecture escape 证据不足** [W6]：降级为 preliminary finding，n=6 的 Spearman ρ=1.0 是 outlier-driven。
4. **BR 循环性** [W5]：重新框定为 degeneration 度量，报告 BR_excess。
5. **Remark 1 trivial + claim 升级** [W4]：区分 DPI bound (trivial) 和 C ⊥ Y | A (non-trivial but unproven)。
6. **SCB 新颖性论证** [W3]：避免 "consistent with" 自我降级，明确独立贡献。
7. **Scope 震荡** [W7]：区分 SICA-specific 和 general 结论。
8. **K_eff 直觉解释** [W9]：加一句自然语言解释。

## Reviewer Divergence

仅在以下 minor 问题上存在轻微分歧，不影响评分：

1. **TOST margin** [W10]：R1 认为 FOLIO 不适用 ±2pp；R2 REBUT 称三分类合理。共识：区分数据集类型。
2. **Abstract 密度** [M1]：R2 认为过载；R1 认为适合 venue。共识：加 K_eff 括号解释。
3. **"Symbolic Mirage" 标题** [M5]：R2 建议更中性；R1 认为 metaphor 准确。保留。
4. **Limitations 长度** [M6]：R2 认为偏短；R1 认为合规。不修改。

---

## Questions for Authors

**Q1.** [R1] Proposition 1 假设 (iii) "approximately uniform constraint yield"：能否提供每 trace 约束数量分布（均值、标准差、CV）？CV 大时 Proposition 1 结论的误差有多大？

**Q2.** [R1] 56.4% 零变量重叠 vs 43.6% 有重叠：有重叠子集的 Z3 拒绝率和 SICA 表现是否不同？

**Q3.** [R1] Capability-gap pattern 仅在 ProofWriter 验证。FOLIO 上用 DeBERTa-NLI 做 cross-architecture verification 的结果如何？

**Q4.** [R1] 27 种修复策略中是否尝试过 prompt 层面打破 source-attribution（如要求提取与答案无关的结构性约束）？

**Q5.** [R1] α 的 ≥99% insensitivity 意味着 α 作为设计参数是多余的。为什么不默认 α=0？

**Q6.** [R2] §2 区分 trace-level bias (CoT) 和 aggregation-level bias (SCB) 是概念性的——是否可设计实验控制 trace faithfulness 后测试 SCB 是否独立存在？

---

## Missing References

论文引用覆盖度已较全面。建议补充：
- Xie et al. (2023) Self-Evaluation Guided Beam Search [R2 提出, R1 AGREE]
- 检查 LATS (Zhou et al.) 引用年份一致性 [R2]
- Lightman et al. (2024) "Let's Verify Step by Step" 在 process-level verification 方面的方法论对比可更详细 [R1]

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 项目未配置外部审稿。

---

## Visual Layout Check（非评分项）

**状态：已完成** (耗时约 4 分钟)

| 严重性 | 数量 |
|--------|------|
| Critical | 0 |
| Warning | 1 |
| Info | 12 |

**Warning findings:**
- Page 5, Table 1（主结果表）：数据字号偏小（约 7-8pt），gold ICL / bold / † 等符号系统认知负荷高。

**Info findings 摘要:**
- Page 1：首页无视觉锚点（纯文本），但 Figure 1 在 page 2 顶部，3 页窗口内可接受。
- Page 4, Figure 2：marker 和 legend 字号偏小，灰度打印时区分度依赖 marker shape。
- Page 7, Figure 4：策略名称文字 ≤6pt，打印后可能难以辨认。建议增大字号或 caption 中列出关键策略名。
- Page 7, Figure 3 (Causal DAG)：图小但简洁（5 节点），可读性尚可。
- Page 8, Limitations：约 6 行，覆盖 3 点，符合 EMNLP 要求，仅一个 Limitations section ✓。
- Appendix：Algorithm 1-2 格式规范；page 14 含 3 表密度极高但附录可接受；Figure 5-8 清晰可读。

**格式合规检查 ✓:**
- ACL template (`\usepackage[review]{acl}`) ✓
- Double-blind (Author: Anonymous) ✓
- 正文 ≤ 8 页 ✓
- Limitations 在正文且仅一处 ✓
- 参考文献无页数限制 ✓

---

## Overall Assessment

**评分：3.5 / 5 (Borderline Conference)**
**两位 Reviewer 一致评分：3.5，置信度 4/5**

**EMNLP 2026 ARR 对应：3.5 = Borderline Conference**

这是一篇执行质量很高的负面结果论文。实验覆盖度在同类工作中罕见（9 模型 / 7 数据集 / 27 变体 / multi-seed / oracle control），统计方法论远超领域平均水准。诊断框架 (C₀, K_eff, BR) 有直接实用价值。

降低评分的核心因素：
1. **标题 overclaiming**（全称否定 vs. 10/16 underpowered）是 soundness 层面瑕疵，两位 Reviewer 独立共识。
2. **理论贡献偏薄**——Proposition 1 形式化不够严谨（假设未定义、证明用 ≈），Remark 1 的 DPI bound 接近 trivial，两者间存在 claim 升级。
3. **SCB 新颖性论证不足**——"consistent with Huang et al." 定位有自我降级风险。
4. **Cross-architecture escape** 作为三个 contribution 之一，evidence base 不足（n=6, outlier-driven, 单数据集）。

**修改路径（可达 4.0 Conference）：**
- 标题修正为 "Provide No Detectable Improvement" 或类似
- Proposition 1 降格为 Empirical Observation 或补充误差界
- 明确 SCB 独立于 Huang et al. 的贡献（形式化 + 诊断框架 + 27 变体排除）
- Cross-architecture escape 降级为 preliminary finding
- BR 重新框定为 degeneration 度量
- K_eff 加直觉解释
- §1/§5/§7 明确 scope boundary

**当前状态：Borderline Conference，Findings 是更稳妥的归宿。修正后可达 Conference 水平。**

---

## Detailed Comments（逐节）

### Abstract
- 信息密度高但可接受。K_eff 需括号解释。BR range 1.66–4.97× 报告完整。"find no evidence" 措辞比标题更准确。

### §1 Introduction
- 三个 contribution 定位清晰但 scope 需精确化。C1 的 "provably sound Z3 verification becomes vacuous" 是 SICA-specific，不应暗示通用。C3 cross-architecture escape 应标注 "preliminary"。

### §2 Related Work
- 覆盖全面，分类（specification-generation / program-generation / trace-extraction）准确。"Distinction from CoT confirmation bias" 段概念上成立但需实证支持。建议补 Xie et al. (2023)。

### §3 Method
- SICA pipeline 描述完整。Eq. 1 (K_eff) 缺直觉解释。Eq. 5 (BR) 定义处应说明 lower bound 为 1 是 by construction。α=0.5 选择缺少讨论（Q5）。

### §4 Results
- Table 1 全面但字号偏小。Multi-seed 行间关系需说明。应标注 powered/underpowered conditions。TOST margin 需区分二/三分类数据集。

### §5 The Symbolic Mirage
- Proposition 1：形式化不足，需降格或加强。Remark 1：trivial DPI，需与 Figure 3 的 C ⊥ Y | A 显式连接。BR 讨论：permutation test 结果实际上加强了 degeneration 论点但 framing 需调整。27 变体排除系统但 scope boundary 需声明。

### §6 Escaping the Bottleneck
- n=6 证据不足。Capability-gap 描述应从 "structural property" 降为 "preliminary observation"。Domain-adapted verifier 与 training-free 主线存在张力。

### §7 Discussion and Conclusion
- 过于简短。"consistent with Huang et al." 措辞自我降级。Scope 从 SICA 扩展到 "any self-verification method" 缺乏论证。

### Limitations
- 简短但合规（3 点：模型规模、英文、统计功效）。

### Appendix
- 体量大（16 页）但信息丰富。关键内容（power analysis, oracle control, SCB evaluation framework）需主文指引。