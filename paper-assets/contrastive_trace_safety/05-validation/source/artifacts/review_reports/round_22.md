---
round: 22
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-20T16:26:45.484923+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 22 (Fresh)

**Paper**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: EMNLP 2026 via ARR May 2026 (deadline: 2026-05-25)
**Reviewers**: R1 (方法严谨性), R2 (新颖性/完整性)
**Rounds**: 1 (converged after cross-sharing)

---

## Summary

本文研究了隐状态安全探针在推理模型上的层选择敏感性。在 4 个推理 LLM（R1-8B/Llama, OT-7B/QwQ-32B/R1-32B 均为 Qwen）上使用 HarmThoughts 数据集，论文发现 crossing-rate composite 指标因 cosine compression 导致浅层噪声膨胀而系统性选择浅层，threshold-based 指标选择深层，且层选择度量的选择可完全逆转 HS 对 text probe 的优势结论。论文提供了详尽的统计验证和 18 页附录，但自身统计方案的校正范围与其倡导的 "researcher degrees of freedom" 叙事存在张力。

---

## Strengths

**S1 [consensus]. 重要的方法论警示。** Layer selection metric 作为 researcher degree of freedom 的识别对 safety probing 社区有直接实践价值。Crossing-rate 几何偏差的具体机制（cosine compression → noise floor → inflated crossings, Table 8）超越了"probe 设计很重要"的泛化认知。

**S2 [consensus]. 异常详尽的统计检验。** HB 校正、BCa bootstrap (10,000 resamples)、exact sign-flip permutation test、nested 5-fold CV、split-half validation、position residualization（线性+二次）——层层递进的验证体系在 NLP 会议论文中罕见。

**S3 [consensus]. 诚实的证据呈现。** Evidence tier 分类（cross-validated / significant / exploratory）、负面结果坦诚报告（7 种 baseline 系统失败, Section 4.6）、M002 bug 主动披露（Appendix N）体现高度学术诚信。

**S4 [consensus]. 可复现性极好。** 30 页 PDF 含 ~34 个表格 + 5 个 figure，超参数/数据/split 比例详尽。代码和数据承诺公开。Reproducibility: 4/5。

**S5 [consensus]. 建设性产出。** 5-metric audit protocol（Section 5）和 multi-metric ensemble（Appendix Z.1）提供具体可操作的方法论指南。

---

## Weaknesses

### Must-Fix（5 个，影响接收决定）

**N1 [critical, consensus] HB 校正范围严重低估实际搜索空间**
- 位置：Section 3.5, Section 7, Appendix W
- 上游探索空间 5 metrics × 7 windows × 28-64 layers ≈ 980-2,240 configs/model。HB 校正仅覆盖 12 个 final tests。论文在 Section 7 自承此局限，但一篇以 researcher degrees of freedom 为核心叙事的论文自身存在同类漏洞，构成对核心主张可信度的根本矛盾。
- Nested CV/split-half 仅覆盖 7-8B 模型；32B（n=19-20，最需保护）无此 safeguard。
- 建议：量化全搜索空间 effective degrees of freedom；对 32B 提供 permutation-based FWER 或将 32B 结论在 abstract 中显式降级为 hypothesis-generating。

**N2 [critical, consensus] Abstract 对 position confound 选择性报告**
- 位置：Abstract, Section 4.3, Appendix Table 29
- Abstract 报告 "3/4 models retain significant non-positional HS advantage"（linear residualization）。Quadratic 下 QwQ-32B 优势被完全吸收（Table 29），降为 2/4。Abstract 完全未提及。
- 与 N4 (encoder-quality) 形成交叉——HS 优势同时对 position control 方法和 encoder 选择敏感，双重条件性使核心 claim 适用范围远窄于 abstract 暗示。
- 建议：Abstract 写明 "under linear residualization 3/4, under quadratic 2/4"。

**N3 [critical, consensus] Random-label control 泛化不足**
- 位置：Appendix B.1, Table 7, Section 6
- Random-label control 仅在 QwQ-32B 上执行，但 Section 6 声称 "Contribution 1 generalizes geometrically" 且 "architecture-independent"。缺少 Llama (R1-8B) 验证。
- 缓解因素：Figure 1 显示 4 模型 crossing-rate 均选浅层；cosine volatility 在所有模型上一致。但 random-label control 作为因果论证需跨架构验证。
- 建议：在 R1-8B 上补充 random-label control；或将声明降级为 "consistent across Qwen-family models"。

**N4 [critical, near-consensus] Encoder-quality 发现反向削弱 HS 优势叙事**
- 位置：Section 4.3, Table 3, Appendix S
- BGE-1024d 下仅 OT-7B (1/4) 保留 HS 优势（HB corrected）。自然解读：HS "优势"部分是弱 text encoder 的 artifact。论文已将此作为 "encoder-quality boundary" 报告（Contribution 2），但 abstract/introduction 叙事仍暗示 HS 优势的普适性。
- R1 认为论文 framing 已部分缓解（这是 contribution 而非 bug），但同意 abstract 需更显著反映限制。
- 建议：坦诚重构 Contribution 2 为双刃发现；abstract 前置 encoder-quality 条件。

**N5 [Must-Fix, consensus] 正文超 8 页限制**
- 位置：Section 6 (Conclusion), page 9
- Conclusion 约 2-3 行溢出到 page 9。EMNLP 2026 正文严格限 8 页。格式违规可导致 desk rejection。
- R2 最初列为 Minor，R1 在交叉回应中主动升级为 Must-Fix。
- 建议：压缩正文确保 Sections 1-6 在 8 页以内。

### Should-Fix（8 个）

**W1 [consensus] 32B 小样本过度推断**
- n=19-20, MDE=8.6-9.5pp。R1-32B position-residualized +1.9pp (p=0.914)。Table 4 仍暗示实用价值；Section 4.4 使用 "detects" 等确定性语言。
- 建议："detects" → "suggests"；32B 数字附 CI width 和 MDE。

**W2 [consensus] 单数据集外部效度**
- CP-dependent 分析仅在 HarmThoughts 上。AdvBench 仅做 cosine volatility 验证。
- 建议：至少在一个子集做 layer selection → selected layer 一致性检查。

**W3 [consensus] CP 标注缺 IAA**
- HarmThoughts 无 IAA；AdvBench LLM IAA κ=0.606 (moderate), CP position MAD=8.3 steps。
- 建议：至少在 HarmThoughts 子集做 human IAA。

**W4 [R2 critical→R1 downgrade] Framing 不一致**
- Introduction monitoring 叙事 vs. Section 3.5 retrospective classification。R1 指出论文有显式 scope 声明，建议降级。
- 建议：Introduction 第一段末尾即声明 retrospective characterization scope。

**W5 [consensus] "Cross-validated" 术语非标准**
- 论文定义为 "passes nested 5-fold CV"，与 ML 标准用法偏差。
- 建议：改为 "validated via nested CV" 或首次使用时标注操作定义。

**W6 [consensus] 5-metric 分类 post-hoc**
- 论文自述 "empirical observation, not a priori"。缺 robustness check。
- 建议：增加 a priori prediction 论述（given geometric explanation, threshold-crossing metrics would exhibit shallow bias）。

**W7 [consensus] Chan & Yong (2025) 处理不充分**
- Section 2 仅一句话。应讨论 probe 方法差异、是否观察到 layer sensitivity、implications。

**W8 [consensus, reduced severity] GRU vs LR 对比不公平**
- 不同 split (70/30 vs 60/20/20)、不同训练协议。但 GRU 非核心论证路径。
- 建议：明确声明 GRU 为 supplementary evidence with different protocol。

### Minor（9 个）

**M1** [consensus] Abstract 信息密度过高
**M2** [consensus] Figure 1 色觉障碍友好性（建议 viridis/cividis）
**M3** [consensus] Table 2 过于密集
**M4** [R1] Table 2 p-value 格式不一致（两组不同检验 p 值混在同一表）
**M5** [consensus] geiger2025causal 年份不匹配（bib=2025, JMLR=2023）
**M6** [consensus] Figure 2 标签尺寸偏小
**M7** [consensus] \cite/\citet/\citep 混用
**M8** [R1] "7-8B models" 混合指代不够精确
**M9** [consensus] K=5 是否应 model-dependent

---

## Reviewer Consensus

以下问题两位 Reviewer 达成一致 [AGREE]：
1. **HB 校正范围** (N1)：12 final tests 远不覆盖 ~2,240 configuration 搜索空间。核心叙事自相矛盾。
2. **Abstract position confound** (N2)：linear 3/4 vs quadratic 2/4 差异未呈现，属选择性报告。
3. **Random-label control** (N3)：仅在 QwQ-32B 上做，不足以支撑 architecture-independent 声明。
4. **Encoder-quality conditionality** (N4)：BGE-1024d 下 3/4 HS 优势消失。R1 部分同意。
5. **页面溢出** (N5)：格式违规，desk rejection 风险。
6. **统计方法论质量高** (S1-S2)：两位均认可远超平均水平。
7. **学术诚信** (S3)：evidence tiers、negative results、bug disclosure 值得肯定。

## Reviewer Divergence

**[DIVERGENCE] 核心贡献增量新颖性**
- **R2 (3.0)**: 中心信息是 Belinkov (2022)/Hewitt & Liang (2019)/Voita & Titov (2020) 已确立认知在 safety 领域的实例化。Excitement 2.5/5。
- **R1 (3.5)**: Crossing-rate 几何偏差机制此前未被记录，5-metric audit protocol 提供可操作指南。Excitement 3/5。
- **Director 判断**: R1 的区分有道理——具体机制识别超越泛化认知。但 meta-level message 与文献一致，核心受众（safety probing + probing methodology）对后者而言增量有限。偏 Findings 级别。

---

## Questions（需要作者澄清）

Q1. 32B 模型除 threshold convergence 外，有无其他方式量化 false discovery risk？是否考虑 BH-FDR？
Q2. QwQ-32B quadratic position control 下 HS 优势完全消失——是否意味着 HS probe 在学 position 的非线性函数？
Q3. Additive composite 归为 threshold-based——若 crossing-rate 权重增大会翻转层选择吗？
Q4. K=5 对不同 trace 长度分布的模型是否同样适用？
Q5. HarmThoughts CP 标注来源？Benchmark 自带 IAA 吗？
Q6. 是否尝试了比 BGE-1024d 更强的 encoder？HS 优势随 encoder 质量单调递减意味着什么？
Q7. 层选择敏感性是否在不同有害类别间一致？

---

## Missing References

两位 Reviewer 建议考虑（需验证真实性）：
1. SafeProbing (Zhu et al., 2026, arXiv:2601.10543)
2. "A Concrete Roadmap towards Safety Cases based on Chain-of-Thought Monitoring" (arXiv:2510.19476)
3. "Probing Latent Subspaces in LLM for AI Security" (arXiv:2503.09066)
4. Stickland & Murray (2019) "BERT and PALs"
5. Liu et al. (2019) "Linguistic Knowledge and Transferability of Contextual Representations"

---

## External Review (Stanford Agentic Reviewer)

未请求外部审稿（项目配置中未启用 external_review.paperreview_ai）。

---

## Visual Layout Check（非评分项）

视觉审查已完成。主要发现：

- **[critical]** 前 3 页连续纯文本，无任何 display item。第一个 figure（Figure 1 heatmap）直到第 6 页才出现。审稿人在前 2 分钟内看不到视觉锚点，严重影响第一印象。强烈建议在第 1-2 页加入方法流程图或核心结果预览图。
- **[warning]** 主文仅 2 figure + 4 table = 6 display items / 8 页 = 0.75/页，对实证论文偏少（通常 ~1/页）。缺少 probing pipeline diagram。
- **[warning]** 第 5 页纯文本断层（Methods/Baselines/Evaluation Protocol）。
- **[warning]** 最后一页（Limitations）全为密集文本。
- **[info]** Figure 1 全宽 2×2 布局合理；Figure 2 forest plot 色盲友好。Table 格式规范（booktabs）。无 [?] 引用、margin 溢出或排版错误。

---

## Overall Assessment

**Overall Score: 3.0 — Findings**

**置信度**: 4/5

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.0 | 2.5 | 2.5 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.0 | **3.0** |

**理由**：

论文识别了 safety probing 中一个有实践价值的方法论问题（层选择度量作为 researcher degree of freedom），crossing-rate 几何偏差机制的识别和 5-metric audit protocol 对社区有用。统计验证体系远超 NLP 会议平均水平，学术诚信值得肯定。

以下因素将评估限制在 Findings：

1. **自身方法论的讽刺性缺陷**：HB 校正仅覆盖 12 final tests 而非 ~2,240 搜索空间（32B 尤其缺乏保护），与 researcher degrees of freedom 核心叙事矛盾。
2. **HS 优势双重条件性**：对 encoder 质量（BGE-1024d 下 3/4 消失）和 position control（quadratic 下 2/4 消失）同时敏感，但 abstract 仅报告最有利条件组合。
3. **泛化证据不足**：单数据集、3/4 Qwen 架构、random-label control 仅一个模型、CP 标注缺 IAA。
4. **增量新颖性争议**：meta-level message 与 probing 方法论文献一致（分歧点，但偏 Findings）。
5. **格式违规**：正文超 8 页，desk rejection 风险。

若 author response 有效回应 N1（搜索空间量化）、N2（abstract 修改）、N5（页面修复），可上调至 3.5 (Borderline Conference)。

---

## Detailed Comments

### Section 1 (Introduction)
- Monitoring 叙事与 retrospective scope 声明间距过大（scope 在 Section 3.5 才出现），建议第一段末尾声明。
- Contributions 列表中 Contribution 2 应反映 encoder-quality boundary 的双刃性质。

### Section 2 (Related Work)
- Chan & Yong (2025) 仅一句话，需扩展：probe 方法差异、layer selection 策略比较、本文发现的 implications。
- 缺少与 Voita & Titov (2020) information-theoretic probing 的深度对比。

### Section 3 (Methods)
- 5-metric 分类的 post-hoc 性质应增加 a priori prediction 论述。
- "Cross-validated" 建议改为 "validated via nested CV" 或标注操作定义。

### Section 4 (Experiments)
- Table 2 p-value 格式应区分不同统计检验；Table 密度可通过移列至 appendix 改善。
- Section 4.4 的 32B 分析语言从 "detects" → "suggests"。
- Figure 1 色彩方案改为色盲友好（viridis/cividis）。

### Section 5 (Discussion)
- 第一段应突出 what is new（crossing-rate 几何偏差机制）而非 what is known（researcher degrees of freedom 一般性问题）。
- Ensemble 的 framing 应强调 robustness guarantee 而非 performance gain。

### Section 6 (Conclusion)
- 必须压缩至 8 页以内。
- 应反映 HS 优势的双重条件性（encoder + position）。

### Appendix
- 34 个表格质量高但可考虑合并相似表格。
- GRU 实验应标注与主实验的 protocol 差异。