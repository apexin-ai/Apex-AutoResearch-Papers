---
round: 15
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T09:10:59.464065+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 17 (Fresh Review)

**论文**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation
**Venue**: EMNLP 2026 (ARR Long Paper)
**Reviewers**: R1 (方法严谨性/统计框架/实验设计) + R2 (新颖性/完整性/写作质量)
**日期**: 2026-05-23

---

## Summary

本文提出 Controlled Style Decomposition (CSD)，一种黑盒诊断方法，通过 NLI-gated content control、per-axis style decomposition 和 position-controlled pairwise comparison 量化 LLM judge 对表层风格特征的敏感度。核心发现为 Likert Blindspot：在相同数据上，pairwise comparison 检测到统计显著的风格偏好（BT 63–77%, p < 0.001），而 Likert scoring 在所有七种统计方法下均失败（p > 0.17）。GEE conditional decomposition 揭示了 per-axis 的 confound structure 差异：verbosity 为 style-dominated (Style OR 8–13)，formality 为 conditional effect。实验覆盖 4 个 target judges（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）、1 个 low-sensitivity reference（Claude Sonnet 4）、3 个 benchmark、2 个 primary + 1 个 exploratory style axis。

---

## Strengths

**S1. 核心定性发现扎实且有实践意义** [AGREE: R1, R2]
Likert Blindspot 在 4 judges × 2 primary axes × 3 benchmarks 上复现。n=355 scaled replication 证实 Likert d→0 是结构性衰减而非 power 不足。七种统计方法的一致性排除 test-specific artifact。对依赖 Likert ATE 的框架（如 RATE）有直接校正价值。

**S2. GEE per-axis decomposition 是真正的方法论贡献** [AGREE: R1, R2]
将 aggregate BT preference 拆解为 Style OR 和 Originality OR 揭示了 per-axis 质性差异（verbosity style-dominated vs formality conditional），是该领域新的诊断层。Claude 在 AEval 的 case（aggregate BT ~70% 但 Style OR n.s., Orig OR 9–12）示范了为什么 aggregate BT 不足以归因 bias。R1 和 R2 在交叉回应中就 GEE 是否为"纯工程贡献"存在分歧（见 Divergence），但均认可其实用诊断价值。

**S3. 实验设计的 transparency 和 self-correction 罕见地好** [AGREE: R1, R2]
n=355 replication 主动暴露 49% OR 缩水；三种 Blindspot 解释的 agnostic framing；100-pair human annotation（AC₁=0.96）；NLI threshold sweep（≤3pp variation）。R2 特别指出 Limitations 章节"几乎没有 reviewer 需要补充的未提及限制"——在 NLP 论文中非常少见。

**S4. Related Work 覆盖全面且定位准确** [AGREE: R1, R2]
对 RATE 的分析基于实证而非稻草人；对 Comparative Trap 的直接回应承认 format amplification 的可能性。

**S5. 统计方法论透明** [AGREE: R1, R2]
FWER 控制、exploratory vs confirmatory 分类、GEE model diagnostics（correlation structure robustness, interaction tests）、bootstrap CI 计算细节充分。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [AGREE: R1, R2] n=88 的 GEE OR 系统性膨胀（~50%）未传播到主要结论**
- Qwen3-32B formality Style OR 从 4.20 (n=88) 缩水至 2.15 (n=355)，-49%。Table 2 其他 11 个 n=88 cell 以 face value 呈现。Verbosity Style OR 8–13 在 ~50% shrinkage 下预计为 4–6.5——论文做了文字推演但未提供 shrinkage-adjusted 估计。CI 极宽（如 GPT-4o verbosity 11.34 [4.93, 26.10]）。
- **Action**: (1) Table 2 caption 明确标注 n=88 OR 为上界估计；(2) 提供 verbosity shrinkage-adjusted projected ORs；(3) 更突出展示 CIs。

**MF2. [AGREE: R1, R2] GPT-4o formality Style OR 在 FK readability control 下失去显著性（p=.132）**
- GPT-4o 是论文叙事的锚点 judge（Intro opening example, Table 1 第一行）。FK grade 作为 GEE 协变量后 Style OR 从 2.70→2.15 (p=.132)，仅在 Appendix 一段话带过。Qwen3 (p=.014) 和 Llama-70B (p=.037) 仍显著。
- **关键 nuance**（R2 补充，R1 同意）：FK grade 可能是 mediator（formality→FK→judge score）而非 confounder。如果是 mediator，控制 FK 是 over-controlling (bad control, Pearl 2009)，true effect 在 [2.15, 2.70] 之间。论文的 DAG (Figure 2) 没有 FK 中介节点——需明确立场。
- **Action**: (1) Section 5.2/5.3 正文讨论；(2) 明确 mediator vs confounder 论据；(3) 给出 GPT-4o Style OR 范围。

**MF3. [AGREE: R1, R2] Claude "low-sensitivity reference" 证据链每条单独不成立，且 AEval verbosity 直接矛盾**
- 四条 convergent evidence 逐一审视：(i) TOST 在 Δ=10pp underpowered (power ~42%); (ii) GEE MDE=1.56 无法排除 small effects; (iii) Bayesian BF₀₁=0.80 inconclusive; (iv) AEval verbosity Style OR=4.76 (p<.001) 与 "low-sensitivity" 标签直接矛盾。Section 5.4 第(ii)项 "(Claude low-sensitivity reference (Style OR n.s.))" 选择性引用 LLMBar formality。
- **Action**: (1) 降级为 "lower-sensitivity judge" (relative, benchmark-dependent); (2) 更新 Section 5.4 描述; (3) AEval verbosity OR=4.76 讨论提升到正文。

**MF4. [AGREE: R1(qualified), R2] 新颖性定位过度宣称——三个 "LLM-specific distinctions" 中 (a) 和 (c) 被经典框架解释**
- (a) Per-axis structure: 经典 IRT 中 item-level discriminability variation 是标准现象。
- (c) Binary divergence: Figure 4 power analysis 完全解释（Likert power < 20% 时 binary failure 是经典预测）。
- (b) GEE source decomposition: R1 REBUT R2——GEE 在 LLM judge bias 领域确实是新的分析层（prior work 均未做 per-axis confound decomposition），不等同于 factor analysis/SEM（见 Reviewer Divergence）。
- **Action**: (a) "complements" 而非 "surpasses" classical framework; (c) 删除 "sharper than classical theory predicts"; (b) "not standard practice in LLM judge evaluation" 而非 "absent from classical framework"。

**MF5. [AGREE: R1(qualified), R2] "Consistently divergent" claim 过强**
- 仅 2 primary + 1 exploratory axis，选择了已知 bias-prone 的轴（formality, verbosity）。Gemini formality 明显较弱（Style OR 1.64, n.s., BT 57.4%）。Abstract/Conclusion 的 "across four judges" 未 qualify Gemini 的异质性。
- R1 nuance: "consistently" 修饰的是 across judges（4/4 target judges 在 formality/verbosity 上均显示 Blindspot），这是成立的。但 axis coverage 不足。
- **Action**: Abstract 改为更精确措辞（如 "across two primary and one exploratory style axes, with varying effect sizes across judges"）。

**MF6. [DIVERGENCE: R2 AGREE, R1 partial REBUT] Title "Blindspot" 预设 Likert attenuation 解释**
- "Blindspot" 语义预设 Likert 遗漏真实信号。在 pairwise amplification 或 construct divergence 下，Likert 没有 "盲点"。Title/Conclusion 偏向 attenuation 解释。
- R1 REBUT: "Blindspot" 有操作性定义（Section 1 第5行），保留标题但更早 qualify。
- **Action**: 见 Reviewer Divergence。建议保留 Title 但在 Abstract 第 2–3 行更早引入操作性定义和三种解释的 qualification。

### Should-Fix（影响评分但不一票否决）

**SF1. [AGREE: R1, R2] Evaluator-producer overlap 仅用一个替代 rewriter 验证**
- Qwen3-32B rewriter=judge overlap 仅用 GPT-4o 验证（verbosity OR 降 22%, formality BT 降 2.1pp）。缺 rule-based rewriter。Formality 替代 rewriter 未报告 GEE。仅影响 Qwen3-32B（其他 3 judges 使用独立 rewriter）。
- **Action**: Limitations 讨论 22% 为 lower bound; rule-based rewriter 作为 future work; 理想情况补充 formality alt-rewriter GEE。

**SF2. [AGREE: R1, R2(升级)] Cross-benchmark replication 选择性——24 cells 仅填 6 个**
- Appendix T 自认 "targeting the strongest effects"。主文 "replicate across benchmarks" 暗示更广泛复制。Gemini 完全缺失。两个 ‡ rows（both BT and Likert significant）实际削弱 Blindspot claim。
- **Action**: 承认选择性；补充弱信号 cell 或讨论缺失影响。

**SF3. [AGREE: R1, R2] TOST equivalence margin 缺乏先验依据**
- 5 个 margin 测试无 a priori justification。12pp 作为 headline result 是 post-hoc 选择。应基于 SESOI（smallest effect size of interest）。
- **Action**: 提供 practical significance 论据（如 RLHF downstream impact）。

**SF4. [AGREE: R1, R2] GEE 模型仅含 2 个 predictors，omitted variable bias 未讨论**
- 可能遗漏 text length, lexical complexity, topic domain 等。GEE 目标是 decomposition 而非 causal ID，两个 predictors 足够 parsimonious，但应声明假设。
- **Action**: Section 5.2 或 Limitations 增加 identification assumptions disclaimer。

**SF5. [AGREE: R1, R2] 与 Comparative Trap 的关系处理不够——未量化 amplification factor**
- 六项 controls "bound" 但不能 "exclude" amplification。论文承认无法 definitively resolve，但未量化 amplification 可能范围。Debiased prompting 降 5.7/13.1pp 可解释为 amplification lower bound，但论文未做此连接。
- **Action**: 量化 amplification 范围或明确 bounding analysis 局限性；讨论 amplification-dominant 情景下的 practical implications。

### Minor（不影响接收）

- **m1**: Table 1 "n=88 except where noted" 与 verbosity 实际 n=86 不一致 [AGREE: R1, R2]
- **m2**: Figure 2 DAG orange dashed S→Q path 灰度打印不可辨 [AGREE: R1, R2]
- **m3**: BT `choix` library "default regularization" 未说明具体形式 [AGREE: R1, R2]
- **m4**: Section 3.1 "constitutes a binary intervention" 建议改为 "approximates" [R1 AGREE, R2 partial REBUT]
- **m5**: Appendix Table 3 QIC 值显示 "---" 无实际数值 [AGREE: R1, R2]
- **m6**: Abstract GEE 描述对不熟悉 GEE 的读者不友好 [R2 提出]
- **m7**: Section 2 RLHF format-specific biases 段落（3 行）未充分发展 [R2 提出, R1 AGREE]
- **m8**: Rewriting temperature 0.7 无选择依据 [R2 提出, R1 AGREE]
- **m9**: Tone axis pilot 应在 Method 中提及 CSD scope boundary [R2 提出, R1 AGREE]

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键问题上达成完全共识：

1. **核心定性发现扎实**：Likert Blindspot 作为现象存在，跨 4 judges、3 benchmarks 复现。
2. **GEE decomposition 有诊断价值**：per-axis confound structure（verbosity style-dominated vs formality conditional）是有信息量的发现。
3. **定量 claims 需要 tightening**：n=88 OR 膨胀、GPT-4o FK control、Claude reference 矛盾——这三个问题均可通过文字修改和补充分析解决，不需要新实验。
4. **新颖性需重新定位**：从 "beyond classical framework" 降级为 "empirical characterization in a new domain + novel diagnostic layer"。
5. **"Consistently divergent" 需 qualify**：axis coverage（2+1）和 Gemini 异质性应在 Abstract/Conclusion 明确。
6. **Comparative Trap 的关系需加强**：amplification 不可排除，bounding analysis 有局限性。

---

## Reviewer Divergence

**D1. Title "Blindspot"（R2-N3 vs R1 反驳）**
- **R2**: "Blindspot" 预设 attenuation 解释，建议改为中性标题（如 "Measurement-Mode Divergence" 或 "The Likert-Pairwise Gap"）。
- **R1**: "Blindspot" 有操作性定义（Section 1 第5行），学术传播需要 memorable label；建议保留但在 Abstract 更早 qualify。
- **Director 判断**: 两位均同意 Title 与正文 nuanced discussion 存在张力。分歧在于解决方案（改标题 vs 更早 qualify）。建议采用 R1 方案（保留 Title + 更早 qualify），因为 (a) "Blindspot" 已在论文中被操作性定义，(b) 正文充分讨论了三种竞争解释，(c) 标题的 communicative value 不应被牺牲——但前提是 Abstract 前 2–3 行必须同时引入操作性定义和 amplification/construct divergence 解释。

**D2. GEE decomposition 的新颖性级别（R2-N1b vs R1 反驳）**
- **R2**: GEE 是成熟统计工具，应用于 style/quality 分解是工程贡献，经典 factor analysis/SEM 承担类似功能。Excitement 3/5。
- **R1**: GEE 在此处的目标（binary outcome 下分离 observed predictors 的条件贡献）与 factor analysis/SEM（latent variable modeling）不同。Prior work（RATE, FairJudge, CASSE）均未做 per-axis confound decomposition。不是纯工程贡献。Excitement 3.5/5。
- **Director 判断**: R1 的反驳有技术依据——GEE conditional decomposition 确实与 FA/SEM 的目标和结构不同。但 R2 的更广泛观点（GEE 本身不是新方法）也成立。论文应将 GEE 定位为 "novel application of established statistical tool to a problem that prior work has not addressed"，而非 "methodological innovation absent from classical framework"。

**D3. 信息密度（R2-W3 vs R1 反驳）**
- **R2**: 8 页承载过多维度，核心 narrative 被稀释。建议将 7 种统计方法、TOST、Bayesian equivalence 全部移至附录。
- **R1**: 论文的信息分层（正文核心 + 13 页 Appendix）是恰当的。核心 narrative 的逻辑链清晰。
- **Director 判断**: 采用 R1 观点。对于 empirical methodology 论文，主文需同时呈现方法、主要发现和 robustness evidence。当前分层合理。但 Section 5.1 的单个段落确实过于密集（TOST + GEE + BF₀₁ 同时出现），建议拆分为更小的段落以提高可读性。

---

## Questions to Authors

1. **[R1-Q1, R2-Q3, 共识]** Verbosity axis 做 n=355 scaled replication 后，Style OR（当前 8–13）预期缩水多少？是否改变 style-dominated 的 regime classification？这是最重要的 missing experiment。
2. **[R1-Q2, R2 补充, 共识]** FK grade 在 formality 中是 mediator 还是 confounder？请提供 DAG 层面的论据。如果是 mediator，GPT-4o Style OR [2.15, 2.70] 中哪个端点更接近 true effect？
3. **[R1-Q3, R2-W2, 共识]** AEval verbosity 上 Claude Style OR=4.76 (p<.001) 如何调和 "low-sensitivity reference"？是否有 AEval 数据分布的特殊性解释？
4. **[R2-Q1, R1 支持]** 如果 pairwise amplification 是主要机制（而非 Likert attenuation），论文的 practical implications 如何改变？"添加 pairwise 模式" 的建议是否反而引入 false positives？
5. **[R2-Q2, R1 支持]** 为什么不包含 human evaluation 来 ground-truth 两种测量模式？论文多次提到这是 "the key next step"——缺乏解释为什么当前工作没有做。
6. **[R2-Q4]** Verbosity FK grade d=0.50 的 60% mediation by sentence length——这是否意味着 verbosity "style bias" 部分是 readability bias？

---

## Missing References

R2 建议补充：
1. Kocmi & Federmann (2023) — GEMBA: Using GPT Models for Reference-Free MT Evaluation（涉及 Likert vs pairwise 比较）
2. 确认 Reber et al. (2025) RATE 和 Jeong et al. (2025) Comparative Trap 引用是否为最新版本（arXiv preprint 可能已被接收）

R1 对此评价 NEUTRAL——相关性有限，建议 authors 自行判断。

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: error — 视觉审查 Agent 因 API 限额耗尽而失败（"You've hit your limit · resets May 25, 8am UTC"）。无法完成 PDF 渲染和排版检查。用户可在限额重置后重新触发。

---

## Overall Assessment

### 评分

**Overall: 3.5 / 5 — Borderline Conference**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5 | 4.0 | 3.75 |
| Excitement | 3.5 | 3.0 | 3.25 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| **Overall** | **3.5** | **3.5** | **3.5** |

### 置信度
4 / 5 — 两位 Reviewer 均有高置信度（4/5），核心判断一致。

### 评分理由

**支持接收的因素**：
- 核心定性发现（Likert Blindspot）在 4 judges × 3 benchmarks 上有可靠复现
- GEE per-axis decomposition 是该领域的真正方法论推进
- 实验设计的严谨程度和 self-correction 的透明度明显高于同领域平均水平
- Limitations 章节异常全面诚实
- 对 RLHF/DPO pipeline 的 style bias audit 有直接实践指导价值

**阻碍给出 4.0（Conference）的因素**：
- 核心发现是 Thurstone (1927) 以来经典结论的 domain transfer，新颖性定位有过度宣称
- 定量估计（GEE OR）受 n=88 小样本偏差系统性影响（~50%），且仅一个 cell 有 scaled validation
- Claude negative control 证据链每条单独不成立，AEval verbosity 直接矛盾
- GPT-4o formality——论文锚点——在 FK readability control 下失去显著性
- 无法区分 attenuation 和 amplification 是根本限制，且 Title "Blindspot" 与此不一致

### 改进路径

如果 authors 能在 rebuttal/revision 中：
1. 重新定位新颖性（"empirical characterization + novel diagnostic layer" 而非 "beyond classical framework"）
2. 标注 n=88 OR 为上界估计并提供 projected ranges
3. 正文讨论 GPT-4o FK control 结果及 mediator/confounder 分析
4. 降级 Claude 为 "lower-sensitivity judge"，更新 Section 5.4
5. Qualify "consistently divergent" 的 axis coverage 和 Gemini 异质性

评分可提升至 **4.0 (Conference)** 或至少 **3.5+ (strong Findings)**。上述修改均为文字调整和框架重组，不需要新实验。

---

## Detailed Comments

### Section-by-Section

**Abstract**: 信息密集但关键数字准确。需更早引入 "Blindspot" 的操作性定义和三种竞争解释。"consistently divergent sensitivity across tested surface-level style axes" 需 qualify（2 primary + 1 exploratory）。

**Introduction**: Opening example 有 pedagogical value 但是 cherry-picked 的单个 instance。三个 "LLM-specific distinctions" 中 (a) 和 (c) 的新颖性宣称需要降级。Power analysis 引用（"4–206× the sample size"）是 illustrative 的，不应暗示 post-hoc power 是 primary evidence。

**Related Work**: 覆盖全面且组织有序。对 RATE 的定位基于实证（"vulnerability"）是恰当的。最后一段 RLHF format-specific biases 论点有趣但未充分发展——这是一个 underexploited motivation。

**Method (Section 3)**: NLI gate 的 direction-aware 设计（verbosity expansion 只检查 backward entailment）有技术创意。DAG (Figure 2) 清晰但灰度打印时 orange dashed line 不可辨。Section 3.1 "constitutes a binary intervention" 建议改为 "approximates"。Section 3.5 Design Rationale 的因果 disclaimer 恰当。

**Experiments (Section 4)**: 统计框架（Section 4.1）的 FWER 控制和 exploratory/confirmatory 分类是 good practice。Table 1 清晰但 "n=88 except where noted" 与 verbosity n=86 不一致。Forest plot (Figure 3) 有效传达了跨 judge 模式。

**Analysis (Section 5)**: 最密集的部分。Section 5.1 的三种解释讨论是 genuinely agnostic，但单个段落内 TOST + GEE + BF₀₁ 过密。Section 5.2 GEE decomposition 是论文最强的分析贡献——Table 2 的 verbosity vs formality 对比清晰有力。Section 5.3 cross-judge replication 扎实但 "replicate across benchmarks" (Section 5.3 第157行) 对选择性 replication 不够诚实。Section 5.4 六项 amplification controls 是 good-faith bounding 但不构成 exclusion。

**Conclusion**: 简洁恰当。"single-format audits risk systematic blind spots" 仍偏向 attenuation 解释——在 amplification-dominant 情景下这条建议可能引入 false positives。

**Limitations**: 异常全面——quality-style confounding, evaluator-producer bias, scope boundaries, validation methodology 均有讨论。两位 Reviewer 几乎没有需要补充的遗漏限制。

**Appendix**: 13 页附录覆盖了所有 robustness checks、diagnostics、和 sensitivity analyses。组织合理（A*–V）。Table 3 的 QIC "---" 应补充实际数值。