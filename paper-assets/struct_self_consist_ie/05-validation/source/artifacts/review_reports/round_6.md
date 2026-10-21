---
round: 6
overall_score: borderline
timestamp: 2026-05-15T09:05:31.196025+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 合并审稿报告 — Round 6

**论文**: Strong Predictors, Weak Selectors: Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding
**目标 Venue**: EMNLP 2026 Findings
**Reviewer 1 侧重**: 方法严谨性 + 实验设计 | **Reviewer 2 侧重**: 新颖性 + 完整性 + 相关工作
**Reviewer 1 评分**: 3.0/5 | **Reviewer 2 评分**: 3.0/5

---

## Summary

论文在 constrained decoding 下系统比较了 5 种 confidence signals（VC, SJ, FK, EM, logprob）用于 structured IE（NER + RE）的 quality estimation 和 sample selection。核心发现是 correlation-selection gap：信号是有效的 quality estimator（ρ=0.38, AUROC=0.75），但无法做 best-of-N selection（p>0.39）。机制诊断追溯到 constrained decoding 下的 logprob score compression。

---

## Strengths

1. **统计分析严谨度远超同类论文**：Bootstrap CI、TOST 等价检验、Cohen's d、multi-seed stability analysis、diversity stratification、conditional filtering——两位 Reviewer 独立给出 4/5 Reproducibility，一致认为统计实践为 IE 领域少见的高标准。[AGREE R1+R2]

2. **Logprob 压缩诊断是论文最有价值的贡献**：Non-tied subset analysis（+2.9pp, p=0.01, within-instance ρ: 0.08→0.39）不仅报告了 selection failure，还提供了 actionable 的机制解释——constrained decoding 压缩 logprob resolution 是主要瓶颈。两位 Reviewer 一致认为这是论文的核心洞察。[AGREE R1+R2]

3. **Quality estimation vs. sample selection 的概念区分**：此前 IE 文献经常混淆这两个目标。论文清晰分离了 instance-level quality prediction 和 per-sample candidate ranking，为后续研究提供了有价值的框架。[AGREE R1+R2]

4. **Difficulty gradient 设计合理**：三个 NER 数据集跨越 easy (CoNLL, 91% F1) → hard (SciERC) → boundary (WNUT-17, 52% zero F1)。WNUT-17 的 logprob 负相关（ρ=−0.410）和 conditional collapse（ρ=0.038, n.s.）是非显然发现。[AGREE R1+R2]

5. **Limitations 的诚实程度值得肯定**：覆盖 RE 单数据集、模型规模限制、N-scaling 范围、thinking mode confound、logprob temperature gap。[AGREE R1+R2]

---

## Weaknesses（按严重度排序）

### Must-Fix（影响接收决定）

**[MF-1] Correlation-selection gap 的叙事结构需根本性重构** [共识 R1+R2]
- **问题**：论文将 "4/5 signals fail at selection" 与 logprob failure 并列呈现为同一现象（gap）。但 4/5 信号的 selection failure 是 **定义的直接推论**（instance-level 信号给同一 input 的所有 N 个 sample 相同分数），不需要实验验证。Discussion Section 5 自己承认了 "Layer 1 (definitional)"，但 Abstract 和 Introduction 仍将其包装为实证发现。
- **真正的实证贡献**是两个点：(a) consensus-proximity / MBR selection 也失败（Table 2: SJ selection 0.645 vs greedy 0.644）；(b) logprob（唯一 per-sample signal）因 score compression 失败。当前 framing 用 "5 signals all fail" 的统一叙事掩盖了这两个更有深度的发现。
- **修改要求**：Abstract 和 Introduction 重构——先一句话 dismiss instance-level 信号的 selection potential（"by definition, not empirically"），然后聚焦 consensus-proximity/MBR failure 和 logprob compression 作为核心贡献。Contribution 2 应以 logprob compression + MBR failure 为重心。

**[MF-2] Contribution 1 framing 过度——benchmark 应用研究被呈现为 primary contribution** [共识 R1+R2]
- **问题**：将 "systematic multi-family comparison of 5 signals" 列为第一条 Contribution，给读者印象是论文的主要贡献。但本质是将已知 confidence signals（logprob, exact match, Fleiss' κ 等）应用于新任务设置——engineering benchmark 而非 new principle discovery。SJ 的 type-aware bipartite matching 有方法新意，但应被呈现为 methodology 而非独立 contribution。
- **修改要求**：Contribution 1 降级为 setup/methodology；Contribution 2（gap + logprob 压缩诊断）提升为核心。去掉 "first" claim（通过堆叠修饰词确保 "first" 成立属于 scope engineering）。

**[MF-3] TOST δ 选择的理据概念错配** [共识 R1+R2，R1 列 must-fix，R2 agree]
- **问题**：δ 取值 ±2/3/5pp 的唯一理由是 IAA 变异（"well-annotated NER benchmarks typically achieve inter-annotator F1 above 95%"），但 IAA 测量标注噪声天花板，与 "selector 预期增益" 是不同概念。Oracle headroom = 13-18pp，δ=5pp 意味着放弃 ~38% 的可能增益仍算"等价"。
- **修改要求**：(a) 用 SESOI 框架或 oracle headroom 比例来论证 δ；(b) 报告 breakpoint δ*（使结论翻转的最小 δ）；(c) 更突出 effect size (Cohen's d=0.038) 和 bootstrap CI [−3.0, +4.2]pp 作为主要证据，TOST 作为补充。

### Should-Fix（影响评分但不一票否决）

**[SF-1] Constrained decoding scope 限定仍不充分** [共识方向一致，严重度分歧]
- Title 已含 "under Constrained Decoding"，但 Introduction 和 Discussion 中部分措辞仍暗示 gap 是 structured IE 的固有属性。Non-tied subset +2.9pp (p=0.01) 表明 gap 主要源于 score compression 而非 IE 固有属性。
- R1 要求 free-form 对照实验（listed critical）；R2 rebut：Layer 1 definitional gap 与 decoding 策略无关，free-form IE 实用性存疑。共识：不要求 free-form 实验，但 Introduction 和 Discussion 需各加 1 句明确声明 gap 发现 specific to constrained decoding regime。

**[SF-2] Qwen3 thinking token 训练不一致** [共识 R1+R2]
- SciERC 未禁用 enable_thinking，CoNLL/WNUT 禁用。Thinking tokens 训练时影响 learned representations 可能改变 logprob 分布，进而影响 score compression 诊断（"60% instances tied" 可能在 thinking-disabled 下不同）。当前仅在 Limitations 脚注中提及。
- 修改要求：Experiments Setup §4.1 中显著声明此 confound。

**[SF-3] RE 证据标注全文不一致** [共识 R1+R2]
- Abstract 标注 "(SciERC, preliminary)" 但 Table 1/2、Figure 2-3、Discussion 大量使用 RE 结果无 preliminary 限定。238 个 non-zero F1 instances，per-relation 变异极大（Feature-Of ρ=0.004 vs Hyponym-Of ρ=0.646）。
- 修改要求：Discussion/Conclusion 每次引用 RE 结论时标注 "(preliminary, single benchmark)"；考虑将 RE selection 移入 Appendix。

**[SF-4] "cross-model" 措辞过度外推** [共识 R1+R2]
- 仅测试 2 个同规模 (8B) 模型。全文改为 "across two model families at 8B scale"。

**[SF-5] Abstract 信息密度过高** [共识 R1+R2]
- 9 行含 5 signal/3 family/4 metric/3 dataset/2 model + 新术语。精简为问题-发现-意义三段式，移除大部分具体数字和信号名。

**[SF-6] 术语不一致** [共识 R1+R2，Round 3 以来持续存在]
- VC / Voting Conf. / entity voting confidence / $c_{\text{vote}}$；LP / Log-prob / logprob / $c_{\text{lp}}$。全文统一为 VC/SJ/FK/EM/LP 五个缩写。

**[SF-7] VC 公式（Eq.6）与实现不一致** [共识 R1+R2，Round 6 新发现]
- Equation 6 无阈值（所有 entity 平均频率），但 Footnote 2 承认实现使用 majority threshold (>N/2)。两者数学不等价。"Slightly different" 但无量化。
- 修改要求：统一公式和实现；报告两种实现的 ρ 差值。

**[SF-8] 遗漏 Eikema et al. (EMNLP 2025) Structure-Conditional MBR** [R2 提出，R1 降为 should-fix]
- Discussion §5 讨论 MBR failure 但缺少结构化输出上 MBR 的最直接相关工作。应引用并讨论差异。

**[SF-9] Nédellec et al. (2026) 增量贡献应更诚实量化** [共识 R1+R2]
- 三个增量均偏弱：SJ vs EM Bonferroni 不显著，selection analysis 部分 tautological，difficulty gradient 直觉上不意外。应降低 claim 强度，强调 WNUT-17 conditional collapse + logprob ρ=−0.410 作为 non-obvious findings。

### Minor（不影响接收）

- Figure 1 caption 冗余，重复 Section 4.2/4.3 内容
- Table 1 N=16 行空白过多，建议移入 Appendix
- FK excess agreement (-0.4% to -4.0%) 未做显著性检验
- N=8 primary results 使用单一 seed=42，与 σ≤0.025 在同量级
- Semantic entropy 脚注去掉具体数字
- he2024uncertainty 引用上下文与实际论文不匹配
- Ethics Statement 应注明 CoNLL-2003 Reuters license
- Notation Table 缺 LP 缩写
- 5 处 bib 条目需核实/修正（ye2025uncertainty author, snell2024scaling year, feng2025optimal author order, hobelsberger/venktesh 确认 arXiv ID）

---

## Reviewer Consensus [AGREE]

1. **论文适合 Findings track**（3/5），但 framing 需要根本性修正——当前叙事夸大了贡献新颖性
2. **Logprob 压缩诊断是真正的核心贡献**，应取代 "multi-family comparison" 成为论文重心
3. **4/5 selection failure 是 definitional**，应与 empirical findings（MBR failure + logprob compression）明确分离
4. **统计实践是显著优势**，远超同类工作
5. **RE 证据薄弱**（单数据集、per-relation 高变异），需全文一致标注 preliminary
6. **Qwen3 thinking token 训练不一致**是未控制 confound
7. **"cross-model" 措辞过度外推**，实际仅 2 个 8B 模型
8. **术语不一致**持续 4 轮未解决

---

## Reviewer Divergence [REBUT]

1. **Free-form decoding 对照实验**：R1 列 must-fix（gap 可能是 constrained decoding artifact），R2 rebut 降为 should-fix（Layer 1 definitional gap 与 decoding 策略无关；free-form IE 实用性存疑）。**Director 判断**：降为 should-fix——论文 Title 已限定 constrained decoding，且 free-form 对照引入新 confounds（不可解析样本处理），但 Introduction/Discussion 的 scope 声明需收紧。

2. **Missing references 严重度**：R2 列 critical（Zhang et al. TTS survey + Eikema et al. Structure-Conditional MBR），R1 rebut（survey 非 critical，Eikema 降为 should-fix）。**Director 判断**：Eikema et al. 为 should-fix（与 MBR failure 直接相关），Zhang et al. 为 minor（camera-ready 补充）。

3. **Supervised verifier baseline**：R2 列 should-fix，R1 rebut（超出论文 scope，已在 Future Work 讨论）。**Director 判断**：不列为 should-fix——论文 scope 是 unsupervised signals，要求 supervised baseline 改变论文定位。

---

## Questions（需作者澄清）

1. VC 实现使用的是 Equation 6（无阈值）还是 Footnote 2 描述的 majority threshold？Table 1 报告的是哪种？
2. Qwen3 SciERC 训练时 thinking tokens 是否实际被激活？是否可以确认 SciERC checkpoint 训练日志中有/无 thinking token outputs？
3. TOST breakpoint δ*（使等价结论翻转的最小 δ）是多少？

---

## Missing References

1. **Eikema, Rutkiewicz & Giulianelli (EMNLP 2025)** "Structure-Conditional Minimum Bayes Risk Decoding"——直接研究 MBR 在结构化输出上的 utility function 失效问题，与 Discussion §5 MBR failure 高度互证 [should-fix]
2. **Zhang et al. (2025)** "A Survey on Test-Time Scaling in Large Language Models"——最全面的 TTS survey [minor, camera-ready]

---

## Overall Assessment

**评分：borderline（3/5）**
**建议：Conditional Accept for Findings（需完成 Must-Fix 修改）**
**置信度：4/5**

论文是一项方法论扎实、统计实践严谨的实证研究，对 structured IE 的 test-time scaling 提供了有价值的实证警告。Logprob 压缩诊断和 difficulty-dependent signal ranking 是实用的贡献。

但当前 framing 存在系统性问题：(a) 将定义性事实（instance-level 信号不能做 per-sample selection）包装为实证发现；(b) 将 engineering benchmark（5 信号对比）包装为 primary contribution；(c) 核心发现的 scope 未充分限定为 constrained decoding 设置。这些 framing 问题不影响实验结论的正确性，但显著降低了论文的可信度和 perceived novelty。

如果作者完成 3 项 Must-Fix 修改（叙事重构、Contribution 重排、TOST δ 理据），论文的 presentation 质量将大幅提升，适合 EMNLP 2026 Findings 接收。

---

## Detailed Comments（逐节）

### Abstract
- 信息密度过高（9 行含全部技术细节），需精简为问题-发现-意义三段式
- "four of five signals are instance-level by construction" 应一笔带过而非作为 finding 呈现

### Section 1 (Introduction)
- Contribution 1 需降级为 methodology；Contribution 2 提升为核心
- "first multi-family comparison" → 描述性表述
- MBR 在 MT 成功但 IE 失败的对比已有（line 26-27），但应更 prominently 作为 gap non-obviousness 的论证

### Section 3 (Method)
- Equation 6 (VC) 与 Footnote 2 实现不一致——统一
- FK "sufficient response diversity" → "mild negative dependence"，注明 excess agreement 的 configurations
- SJ 的 "primary structural signal" 措辞适当（非 "core"）

### Section 4 (Experiments)
- §4.1 需 prominently 声明 Qwen3 thinking token confound
- Table 1 删除 N=16 行移入 Appendix
- TOST 分析需 SESOI 论证 + breakpoint δ* 报告

### Section 5 (Discussion)
- "Layer 1 (definitional)" 已有但 Introduction/Abstract 未同步——需全文一致
- 补充 Eikema et al. (EMNLP 2025) MBR 互证
- 收紧 gap 的 scope 声明（specific to constrained decoding）

### Section 6 (Conclusion)
- "across model families" → "across two model families at 8B scale"
- RE 限定句 "RE findings rest on SciERC alone" 已有但 Discussion 中引用 RE 时缺同等标注

### Section 7 (Limitations)
- WNUT-17 logprob 负相关机制假设已加入 §4.2，Limitations 可交叉引用
- Thinking token confound 需从脚注级别提升

### References
- 5 处 bib 条目需核实修正
- 补充 Eikema et al. (EMNLP 2025)

### 术语统一（全文）
- VC / SJ / FK / EM / LP 五个缩写，表格和正文一致