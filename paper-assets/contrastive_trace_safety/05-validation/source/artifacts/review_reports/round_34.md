---
round: 34
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-23T14:49:50.279003+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 34 (Fresh Review)

**论文**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: EMNLP 2026 (ARR Long Paper)
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）
**审稿模式**: Fresh（重新审稿，无历史轮次记忆）

---

## Summary

本文研究推理模型中 hidden-state safety probe 的 layer selection 敏感性问题。作者定义 Safety Commitment Point (CP) 作为推理过程中安全审议永久停止的首个步骤，在 4 个推理 LLM（3 Qwen, 1 Llama）上比较 HS 与 text probe 的 CP 检测能力。核心发现是 layer selection metric 的选择（crossing-rate composite vs. threshold-based）可以完全反转 HS 优势结论——CR-composite 选择浅层（HS ≈ Text, p=0.83），threshold-based 选择深层（HS >> Text, +20pp, p<0.005）。论文通过 cosine compression 机制解释此偏差，提供 AdvBench 跨数据集复制，并报告七种替代方法均不及监督探针。

---

## Strengths

**S1. 核心方法论发现重要且可靠。** 同一数据上 p=0.83 vs. p<0.005 的定性逆转（Table 2）是 striking 的，且在 AdvBench 上复制（31.7pp divergence, p=0.015）。Layer selection metric 作为 uncontrolled specification choice 影响安全结论——这对 safety probing 社区有直接实践指导价值。[R1 S1, R2 S1, 共识]

**S2. 统计框架远超同类论文水平。** Nested 5-fold CV（7-8B）, exact permutation tests（32B）, BCa bootstrap CIs（10,000 resamples, trace-level clustering）, Holm-Bonferroni step-down 校正（12 tests）, 后验功效分析（Table 42）, Cohen's d 效应量报告。这是探针类论文中罕见的统计严谨度。[R1 S2, R2 S2, 共识]

**S3. 证据分级诚实透明。** 确认性（cross-validated, 7-8B）、显著性（significant, QwQ-32B†）、探索性（exploratory, R1-32B†）三级划分明确，†标记全文一致。Bug disclosure（Section M）高度透明。[R1 S3+S5, R2 S3, 共识]

**S4. Cosine compression 机制提供可检验的几何解释。** Table 8 定量展示浅层 inter-step cosine distances 比深层小 1.4-2.7×，将 CR-composite 的浅层偏好归因于表征压缩导致的噪声交叉。Random-label controls（Section A.1, Tables 6-7）进一步证实浅层选择是 geometric artifact 而非 information-bearing selection。[R1 S6, R2 S3, 共识]

**S5. 附录极为详尽。** 24 节，~20 页，覆盖 random-label decomposition、cosine volatility、selectivity、multi-seed stability、position residualization、power analysis 等。几乎每个潜在质疑都有对应消融。[R1 S4, R2 S4, 共识]

**S6. 负面结果系统报告。** Section 4.6 和 Appendix P 系统报告 BOCPD/CUSUM/RepE/CCS/MLP 等七种方法的失败，附录 J 提供详细 failure analysis，节省后续研究者试错成本。[R2 S6]

---

## Weaknesses

### Must-Fix (Critical)

**W1 [critical, consensus] 单一数据集 + 小样本严重限制 C2/C3 的外部效度。**
所有 CP-dependent claims（C2: HS advantage magnitude, C3: negative results）完全依赖 HarmThoughts 一个数据集。测试集仅 43（R1-8B）、47（OT-7B）、19-20（32B）个 traces。AdvBench 仅验证 C1（layer selection pattern），未验证 C2。HarmThoughts 和 AdvBench 均为 binary safety taxonomy（jailbreak/safe），未覆盖细粒度 safety categories。+20-22pp HS advantage 基于 43-47 个样本，bootstrap CI 部分缓解但无法弥补外部效度缺失。[R1-N1 critical, R2-W4 warning, 共识升级为 critical]

**W2 [critical, consensus] 32B 结果 underpowered 但在主文中占据过多篇幅。**
R1-32B residualized gap +1.9pp 远低于 MDE 8.6-9.5pp（Table 42）——当前数据无法对 R1-32B 的 HS advantage 做出任何推断。QwQ-32B lead time 为负（-1.2 到 +1.9 steps），意味着探针在 CP 后才检测到。Section 4.3 在主文中占约半栏，Abstract 中"+15 to +19pp at 32B"与 7-8B 结果并列呈现可能误导读者。论文的†标记是诚实的，但空间分配与证据强度不匹配。[R1-N4 warning, R2-W2 critical, 共识]

**W3 [critical, consensus] 架构同质性（3/4 Qwen）限制泛化性。**
4 个模型中 3 个共享 Qwen 架构。Section A.1 承认 geometric bias 是 Qwen-specific 的。Gemma-2 的 cross-architecture 验证（Section B.3）仅验证 C1 的 crossing-rate pattern。R2 补充了重要 nuance：C1 的现象（metric divergence）在 Llama 上同样成立但通过不同机制（label-dependent vs. label-independent），这实际上加强了 C1 的 generalizability。但 C2 和 C3 缺乏非 Qwen 架构验证。[R1-N2 critical, R2 agrees with nuance, 共识]

### Should-Fix (Warning)

**W4 [warning, divergence → 倾向 R2] 核心发现的新颖性相对于已知 probing methodology 文献增量有限。**
C1（metric-induced layer selection bias）本质上是 "probing conclusions are sensitive to methodological choices"（Belinkov 2022 综述 Section 4-5）在 safety probing 领域的具体实例化。Voita & Titov (2020) MDL probing 正是为解决 metric 选择影响结论而提出的。R1 REBUT 提出三点增量贡献：(1) metric→layer→conclusion 级联效应是新的（prior work 讨论 metric sensitivity at a fixed layer）；(2) cosine compression 机制是 novel geometric explanation；(3) 定性逆转的严重程度（14-61 层 divergence）远超 prior work。R1 的论点有一定说服力，但论文当前的 framing 未充分 articulate 这些增量贡献。**Director 评估：C1 的执行质量（统计严谨性、几何机制、跨数据集复制）使其超越 simple domain replication，但概念层面的增量贡献确实有限。论文需要更明确地定位 novelty layer。** [R2-W1 critical, R1 REBUT, 分歧点]

**W5 [warning, consensus] HS advantage 在更强控制条件下大幅削弱，但 framing 未充分反映。**
递进削弱模式：384d encoder: 4/4 sig → quadratic residualization: 2/4 sig → BGE-large 1024d: 1/4 HB sig。**关键缺失实验：BGE-large + quadratic residualization 叠加条件未报告（Table 27 和 Table 30-31 分别报告但未交叉）。** 如果叠加后 0/4 models 保留 HS advantage，C2 的结论将实质性改变——HS advantage 可能主要来自 weak encoder ceiling + position proxy。Abstract/Intro 的 framing 偏重 384d 正面结果，1024d 退化处于从属地位。[R1-N3 warning, R2 agrees, 共识]

**W6 [warning, consensus] "Confound" 术语过度表述因果关系。**
论文所有证据均为 correlational（不同 metrics → 不同层 → 不同结论），但使用因果性术语 "uncontrolled confound"。统计学中 confound 指同时影响自变量和因变量的变量，论文展示的更准确地描述为 "researcher degree of freedom"（Simmons et al., 2011）或 "specification sensitivity"。存在内部不一致：标题用 "Sensitivity"（准确）但 abstract 用 "confound"。[R1-N5 warning, R2-W3 warning, 共识]

**W7 [warning, consensus] CP 标注缺乏 human-human inter-annotator agreement。**
Table 21 仅报告 LLM vs. human agreement（κ=0.606, CP position exact match 37%），缺少人类标注者间的正式 reliability 评估。±1 step perturbation BA<2.5pp（Table 20）提供间接 robustness evidence，但不等同于正式 IAA。如果 human-human agreement 也低，CP 概念的操作化本身存疑。[R1-W1 warning, R2-W5 warning, 共识]

### Minor (Info)

**W8 [info] Discussion + Conclusion 极度压缩（~3-4 句），缺 C1 对现有文献的影响讨论、实践指南、MDL probing 深入对比。** [R1-W2, R2 agrees]

**W9 [info] Negative results (C3) 主文归因过于简略，未充分指向 Appendix J/P 的详细 failure analysis。** [R2-W6, R1 partial REBUT — appendix 有详细分析但主文指引不足]

**W10 [info] 术语密度较高（crossing rate, CR-composite, FCP 等），首次阅读学习曲线偏陡。** [R2-W7, R1 agrees]

**W11 [info] Figure 2 colormap red-green gradient 不利于色盲读者；字号偏小（~6-7pt）。** [R2-W8, R1 agrees, visual check 确认]

---

## Reviewer Consensus

以下问题 R1 和 R2 达成共识 [AGREE]：

1. **单一数据集 + 小样本**是核心局限——C1 的证据充分（per-layer sweep, 跨数据集复制），但 C2/C3 完全依赖 HarmThoughts
2. **32B 结果**证据强度不足以支撑其在主文中的篇幅分配，应大幅压缩至附录
3. **"Confound"术语**不精确，应改为 "specification sensitivity" 或 "researcher degree of freedom"
4. **CP 标注**缺正式 human-human IAA
5. **HS advantage 递进削弱**是重要发现但 framing 不够突出
6. **BGE-large + quadratic residualization 叠加测试**是关键缺失实验
7. **统计框架**极为出色，远超同类论文水平
8. **证据分级和透明度**（†标记、bug disclosure）值得肯定

---

## Reviewer Divergence

**主要分歧：Novelty 评估（W4）**

| 维度 | R1 (3.5) | R2 (3.0) |
|------|----------|----------|
| C1 增量 | Novel metric→layer→conclusion 级联 + geometric mechanism + safety-critical domain | Known probing sensitivity 的 domain-specific instantiation |
| Excitement | 3/5 — important cautionary tale | 2.5/5 — limited novelty ceiling |
| 条件性接受 | C1 足以支撑 Borderline Conference | 需要更清晰的 novelty articulation 才能考虑上调 |

**Director 判断**：R2 的 novelty concern 更为根本——即使 C1 的执行质量优秀，其概念层面的贡献是将已知的 probing methodology 问题（metric sensitivity affects conclusions）在 safety probing 领域进行了高质量的 empirical demonstration。R1 关于 cosine compression mechanism 和 severity 的论点有力，但不足以将概念贡献提升到 Conference 水平。C2（HS advantage）在更强控制条件下的脆弱性（W5）进一步支持 Findings 而非 Conference 定位——如果论文的 secondary contribution 在 BGE-large + position control 下可能完全消失，整篇论文更接近 "methodological caution note" 而非 "positive contribution"。

---

## Questions

**Q1.** [R1-Q1, R2 agrees critical] BGE-large (1024d) + quadratic position residualization 叠加后，HS precision advantage 是否仍然显著？当前 Table 27 和 Table 30-31 分别报告但未交叉。这是决定 C2 最终定位的关键实验。

**Q2.** [R2-Q1] C1 相对于 Belinkov (2022) 和 Voita & Titov (2020) 的增量贡献是什么？请明确区分：是首次在 safety domain 的 empirical confirmation，还是揭示了 safety-specific 的新机制？

**Q3.** [R1-Q3, R2 supplements] Qwen 架构的哪个具体特性导致 geometric bias 是 Qwen-specific 的？Section A.1 承认这一点但未解释 why。候选因素包括 layer count (64 vs. 32) 和 RMSNorm vs. LayerNorm。

**Q4.** [R2-Q2] Human-human inter-annotator agreement for CP position 是多少？如果仅有单人标注，请在 Limitations 中说明。

**Q5.** [R1-Q5, R2 agrees] Ensemble（3-layer average, Table 43, p≤0.002 all 4 models）为什么不被定位为 C1 的直接解决方案？当前 "preliminary exploration" 定位是否过于保守？

**Q6.** [R1-Q2] CP 标注扰动 ±1 步对 HS-text precision *差异*（而非 absolute BA）的影响有多大？如果 text probe 对 CP boundary 更鲁棒，扰动可能不对称地削弱 HS advantage。

---

## Missing References

**R2 建议（R1 同意）：**
1. Tenney et al. (2019), "BERT Rediscovers the Classical NLP Pipeline" — layer-wise probing 的系统性研究
2. Ravichander et al. (2021), "Probing the Probing Paradigm" — probing methodology 的系统性批评，与 C1 直接相关

**R2 建议（R1 认为可选）：**
3. Gurnee & Tegmark (2024), "Language Models Represent Space and Time Across Scales" — per-layer representation geometry 随 scale 变化

---

## External Review (Stanford Agentic Reviewer)

未配置，未请求。

---

## Visual Layout Check（非评分项）

**状态**: 已完成（2026-05-23 14:28 → 14:32, ~4min）
**结果**: 0 critical, 1 warning, 11 info

**Warning:**
- pp.4-5 连续 2 页纯文本（Section 3 方法 + Section 4 实验起始），无任何 display item 穿插。方法部分有 temporal windowing、classification formulation 等概念，可考虑提取 display equation 或示意图

**Info 摘要:**
- Figure 1 概念图在 p3，语义清晰，caption 自包含，效果好 ✓
- Table 1 (p2) 和 Table 3 (p7) booktabs 风格规范 ✓
- Figure 3 forest plot 清晰度良好，CI 标注专业 ✓
- Figure 2 (p6) 字号偏小 (~6-7pt)，配色红绿渐变不利色盲
- Figures 4 & 5 (p8) 尺寸较小，轴标签约正文 60-65%
- 主文正好 8 页，Limitations 在 p8 右栏，References p9-11 ✓
- 无 [?] 未解析引用 ✓

---

## Overall Assessment

**Overall: 3.0 (Findings)**

**评分理由：**

C1（metric-induced layer selection bias）是本文的 robust finding——在 4 个模型、2 个数据集、额外 Gemma-2 验证上均成立，cosine compression 提供了可检验的几何机制，统计框架远超同类论文。这一发现对 safety probing 社区有直接实践指导价值，足以支撑 Findings 级别接收。

但三个因素阻碍 Conference 推荐：
1. **Novelty ceiling**：C1 在概念层面是已知 probing methodology 问题的 safety-domain 实例化（R1/R2 分歧点，Director 倾向 R2）
2. **C2 脆弱性**：HS advantage 在 BGE-large (1024d) 和 quadratic position 控制下大幅削弱（4/4 → 1-2/4），叠加测试未报告但可能 0/4——secondary contribution 不够 robust
3. **Evidence scope 有限**：单一 CP 数据集（HarmThoughts）, 架构同质性（3/4 Qwen）, 32B underpowered（MDE >> observed effect）

**Rebuttal 可改善的条件（可能上调至 3.5）：**
- 报告 BGE-large + quadratic residualization 叠加结果
- 更清晰地 articulate C1 vs. Belinkov/Voita 的增量 novelty
- 将 32B 分析移至附录，扩展 Discussion

| 维度 | R1 | R2 | Director |
|------|----|----|----------|
| Soundness | 4/5 | 3.5/5 | 4/5 |
| Excitement | 3/5 | 2.5/5 | 2.5/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 3.5 | 3.0 | **3.0** |
| Confidence | 4/5 | 4/5 | 4/5 |

---

## Detailed Comments

### Section-by-Section

**Abstract (~180 words, 合规 ✓)**
- 信息密度高但可读。32B 结果与 7-8B 并列呈现可能高估 32B 的证据强度。建议将"+15 to +19pp at 32B (exploratory†, n≤20)"的 qualifier 更加突出。
- "uncontrolled confound" → 建议改为 "unexamined specification choice"。

**Section 1 Introduction (~1.5 pages)**
- 叙事流畅：problem → gap → contributions。Figure 1 概念图有效。
- C1-C3 三个 contributions 定义清晰。但 C1 相对于 Belinkov (2022) 的增量需要更明确的定位语句。
- Table 1 模型信息清晰完整。

**Section 2 Related Work (~0.7 pages)**
- 覆盖五个方向：safety probing, hidden-state detection, layer selection, multi-layer probing, alternative approaches。引用 70+ 篇，覆盖面良好。
- 建议增加 Tenney et al. (2019) 和 Ravichander et al. (2021)。

**Section 3 Method (~1.5 pages)**
- CP 定义（Section 3.1）清晰但 binary formulation 的 limitation 讨论不足。
- Metric taxonomy（Section 3.3-3.5）技术上严密，但首次阅读时术语密度高。建议 Section 3 开头增加 metric taxonomy overview。

**Section 4 Experiments (~3 pages)**
- Section 4.1 Layer Selection Results: 核心证据充分（Table 2, Figure 2）。
- Section 4.2 HS vs. Text: 384d 结果 solid；position and encoder robustness 分析在同一节内但 framing 偏向正面。
- Section 4.3 32B Analysis: 建议大幅压缩移至附录。
- Section 4.4 Ensemble: 有潜力但当前 "preliminary" 定位合理。

**Section 5 Discussion and Conclusion (~4 sentences)**
- 过度压缩。缺：C1 对现有文献的具体影响、推荐的 layer selection protocol、与 MDL probing 的深入对比。建议利用压缩 Section 4.3 释放的空间扩展。

**Limitations (~0.25 pages)**
- 覆盖 3 点（CP-dependent claims, single dataset, correlational evidence），简洁合适，符合 EMNLP 要求。可增加：human-human IAA gap。

**Appendix (~20 pages)**
- 极为详尽，覆盖所有主要消融。Bug disclosure（Section M）透明度出色。

### 格式合规检查
- ✅ 主文 8 页（Sections 1-5 within p8, Limitations p8 右栏）
- ✅ 匿名性：无作者信息泄露、无非匿名链接
- ✅ Abstract ~180-190 words（限制 200）
- ✅ ACL 模板 [review] 选项
- ✅ References 格式统一，无 [?] 未解析引用
- ⚠️ Figure 2 colormap 不利色盲（建议改用 viridis）