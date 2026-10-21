---
round: 2
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T09:51:16.959851+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 3（Fresh Review）

**项目**: causal_style_decomp_judge
**论文**: Counterfactual Style Decomposition Reveals the Likert Blindspot: Standard Scoring Underestimates Style Bias in LLM Judges
**目标 Venue**: EMNLP 2026 (Long Paper, via ARR)
**审稿人**: Reviewer 1（方法严谨性 + 实验有效性）、Reviewer 2（新颖性 + 完整性 + Related Work）
**审稿轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮达成共识）

---

## ⚠️ Deadline 警告

Web 搜索确认 EMNLP 2026 最后可用的 ARR 提交截止日为 **2026-05-25 AoE**（距今 4 天），而非提交消息中的 2026-06-15。ARR May cycle 提交时须绑定声明 EMNLP 2026 为目标会议（binding）。请立即核实。

---

## Summary

本文提出 Counterfactual Style Decomposition (CSD)，一个黑盒框架，通过 binary style-controlled rewriting + NLI entailment gate + position-controlled pairwise comparison 检测 LLM judge 的 per-axis style bias。核心发现命名为 "Likert Blindspot"：在 3 个 judge（GPT-4o、Qwen3-32B、Claude Sonnet 4）、3 个 benchmark（LLMBar、AlpacaEval、MT-Bench）、2 个主要 style axes（formality、verbosity）+ 1 个探索性 axis（register）上，Likert 评分对 style bias 的检测灵敏度系统性低于 pairwise comparison（~4.5× 效率差距）。GEE logistic regression 将 style effect 和 originality confound 分离，发现 confound gradient（verbosity = pure style, formality = dual, register = originality-dominated）。Claude Sonnet 4 在所有 axes 上无显著 bias，作为 discriminative validity 证据。

---

## Strengths

**S1. 统计三角验证扎实**：7 种统计方法（ATE、sign test、BT、ordinal regression、GEE、Holm-Bonferroni、power curve）一致显示 Likert vs pairwise 灵敏度差距，跨 judge/benchmark/axis 的系统性复制增强可信度。[R1 + R2 共识]

**S2. GEE per-axis 分解有方法论贡献**：将 style effect 和 originality confound 解耦的 GEE 框架在 LLM judge bias 文献中较为少见，confound gradient 发现有 insight。GEE diagnostics（Appendix C, correlation structure robustness）完整。[R1 + R2 共识]

**S3. Negative results 诚实呈现**：Claude Sonnet 4 无 bias（BT 56.2%/54.1%, non-sig）、formality 方向不对称（78.8% vs 54.5%）、tone axis 失败——增加了结果可信度和论文的科学诚实性。[R2 首提, R1 同意]

**S4. 实用价值高**：量化了 LLM evaluation 中 Likert vs pairwise 的 ~4.5× 效率差距，对评测实践有直接指导意义。Figure 4 power curve 是 measurement methodology 层面的有价值贡献。[R1 + R2 共识]

**S5. Pipeline 可复现**：NLI gate 阈值、BT 模型参数、bootstrap 配置（10k resamples）、GEE correlation structure 均明确报告。方法描述清晰，各步骤可复现（但代码/数据未附）。[R2]

**S6. 写作质量良好**：结构清晰，信息密度高，在 8 页内覆盖完整的方法-实验-分析链。正文 8 页合规，Limitations 覆盖了关键弱点。[R2]

---

## Weaknesses

### Must-Fix（影响接收决定，两位 Reviewer 强共识）

**MF1. "Blindspot" framing 混淆统计功效差异与质性 blindspot** [R1-N3 + R2-N1, 强共识]
- Title 用 "Blindspot" 暗示 Likert 有质性缺陷（永远检测不到），但 Figure 4 power curve 明确显示 Likert 在 n≈1,473 时达到 80% power——这是量性的 efficiency gap，非质性 blindspot。
- Thurstone (1927) 关于 ordinal scale 灵敏度低于 paired comparison 的结论已近百年，论文在 §2 引用了 Thurstone 但未充分说明增量贡献。
- n=355 scaled replication Likert 仍 non-significant (p=0.60)，但该配置下 Cohen's d 未报告——若 d 仍接近 0.1，power 约 25-30%，依然是功效不足。
- 论文自身使用 "~4.5× more data to reach equivalent sensitivity"（§5.2）的 power 语言，与 "Blindspot" framing 自相矛盾。
- **关键区分**：若能证明 Likert 同时压缩 effect size（measurement attenuation）+ 降低 power（而非仅后者），"Blindspot" framing 更站得住脚，但论文未做此分析。
- **建议**：(1) 将 "Blindspot" 重定义为 "measurement efficiency gap at typical evaluation scales"；(2) 补报 n=355 Likert Cohen's d 和 power；(3) 明确区分量性 gap 和质性 blindspot。

**MF2. 因果/反事实术语与方法论强度不匹配** [R1-N1 + R2-N2, 强共识]
- Title "Counterfactual"、§3.5 "Causal Framework"、Figure 2 DAG 暗示形式化因果模型，但 §3.5 声明 "not a complete structural causal model, nor do we invoke SUTVA"。
- 经验性违反证据：Table 3 中 originality OR 在多个配置下显著（GPT-4o formality: OR=2.32, p=0.006; Qwen3 register: OR=5.72），直接表明 NLI gate 未完全阻断 R→Q path——识别假设 (i) 部分违反。
- 识别假设 (iii)（rewrite 不引入 target axis 外差异）未检验——formality rewrite 可能同时改变 register/vocabulary sophistication。
- 实际上 CSD 是 controlled intervention study with imperfect content preservation，非因果推断。
- **建议**：(1) Title 中 "Counterfactual" → "Interventional" 或 "Controlled"；(2) §3.5 标题 → "Interventional Design and Assumptions"；(3) Figure 2 DAG 用虚线标注 residual S→Q confounding；(4) 量化讨论 originality OR 对 style effect 估计的影响方向和幅度。

**MF3. Evaluator-producer independence test 覆盖不完整** [R1-N2, R2 交叉同意]
- Qwen3-32B 同时做 rewriter 和 judge，效应量系统性偏高（formality Style OR 4.20 vs GPT-4o 2.58 at n=88，1.6× 差距）。
- Appendix D rewriter independence test 仅覆盖 verbosity 轴（GPT-4o rewriter: OR 13.10→10.17, 22% 降幅），缺 formality 和 register。
- Formality 恰是 evaluator-producer bias 最明显的轴——Qwen3 OR 从 n=88 (4.20) 降至 n=355 (2.15) 的 49% 降幅也暗示小样本下的 OR 膨胀。
- 主分析（Table 1, Table 3）仍以 Qwen3-32B 与 GPT-4o 并列为主要证据，"across two judges" 的 generalizability claim 受损。
- **建议**：(1) 补做 formality 轴 independence test（GPT-4o rewriter + Qwen3-32B judge）；(2) 或在主文明确标注 Qwen3-32B 结果仅作 existence claim，不适合与 GPT-4o 做定量 effect size 比较。

### Should-Fix（影响评分，两位 Reviewer 至少一位提出且另一位同意）

**SF1. 缺少任何人工评估验证 rewriting 质量** [R1-W4, R2 强化]
- CSD 完全依赖 NLI gate（自动化）验证 content preservation，无 human evaluation 验证 (a) style 改变方向正确率 (b) 自然度 (c) NLI 未检测的 artifacts。ACL/EMNLP 涉及 text generation 的工作通常需要至少 small-scale human evaluation。

**SF2. NLI gate 验证使用同一模型族** [R1-W1, R2 同意]
- §5.1 使用 Qwen3-32B 作为 annotator 验证 NLI gate（precision 98.9%），但 Qwen3-32B 同时是 rewriter——self-consistency bias 可能高估 precision。论文承诺 "GPT-4o spot-check is planned" 但未执行。

**SF3. Direction-aware NLI 放宽为单向 entailment，额外纳入的 pairs 未独立验证** [R1-W2, R2 同意]
- Verbosity 轴 NLI gate 从双向放宽为单向，pass rate 从 65% 升至 86%。额外纳入的 ~21% pairs 的 content preservation 质量未经独立验证。单向 entailment 允许 expansion 方向丢失信息（更详细 = 更高质量的感知）→ 可能 inflate style bias estimate。

**SF4. Confound gradient 的替代解释** [R1-W5, R2 同意]
- §5.6 发现 verbosity = pure style, formality = dual, register = originality-dominated。但 gradient 可能反映 rewriting 操作的 invasiveness（verbosity 大幅增删 vs formality 词汇替换 vs register 几乎必然改变 sophistication）而非 axis 固有属性——即 pipeline artifact 而非 style axis property。

**SF5. GEE "decomposition" 在残余 confounding 下有误导性** [R2-W3, R1 同意]
- Table 3 中 originality OR 显著（p=0.006）证明 confounding 未消除。"Decomposition" 暗示干净分离，实际是 partial adjustment。Originality 的操作化定义不清晰。

**SF6. 小样本 OR 估计不稳定** [R1-W6, R2 同意]
- Qwen3 formality Style OR: n=88 (4.20) → n=355 (2.15)，降幅 49%，表明 n=88 估计严重偏高。Register 轴 marginal significance (p=0.046) 在此样本量下尤其脆弱。建议将 n=355 scaled replication 提升为主结果。

**SF7. Related Work 引用偏少** [R2-W1, R1 同意]
- 27 条引用低于 EMNLP long paper 通常水平（40-60 条）。缺失：counterfactual generation 方法谱系（CausaLM, Polyjuice）、NLG evaluation scale design（Clark 2021, Amidei 2019）、BT in LLM evaluation（Boubdir 2023）。

**SF8. NLI gate false negative → systematic selection bias** [R2-W2]
- 大幅 style 变化更易被 NLI gate 过滤 → 保留的 pairs 系统性包含较小 style 干预 → 低估 measured effect（attenuation bias）。§5.1 FN 无方向性偏差（Fisher p=0.35）部分回应，但理论论点仍成立。

**SF9. 证据范围 vs 建议范围不匹配** [R2-N3, R1 部分反驳]
- Contribution 4 和 Conclusion 给出一般性建议（"style bias audits should adopt pairwise comparison"），但证据仅来自 n=100 × 3 judges × 2 有效 axes。R1 指出 cross-benchmark 已覆盖 3 种任务类型（instruction-following, open-ended, multi-turn），Register 在主文 §5.5 有讨论。共识：建议应加 qualifier。

### Minor Issues（不影响接收）

- Abstract 过长过密（9 行），建议精简至 5-6 行聚焦核心 claim [R1]
- Table 1 Holm-Bonferroni p-value 标注可更直觉（raw p vs adjusted p 混淆）[R1 提出, R2 认为信息完整但 presentation 可改进]
- Claude 作为 negative control 有双重解释（无 bias vs alignment 消除 bias），可在讨论中补充说明 [R2 提出, R1 认为 discriminative validity 论证合理]
- Orphan bib entry `hoenig2001abuse`；`murugadoss2025sos` 在 OpenAlex 未匹配（可能太新）[R1 + R2]
- Figure 1 偏小，stage attrition numbers 不易辨认 [R2]
- §6 "Prompt-level debiasing is insufficient" 缺乏 evidence 基础（未测试任何 debiasing 方法）[R2]
- ~60% uninformative ties 在 Abstract/§1/§5.2 重复出现但未给出全部 6 个配置的 tie rate 分布表 [R1]
- §5.5 Register 结果 marginal significance 用大半节描述 inconclusive 结果，考虑压缩 [R1]

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下问题上独立达成强共识：

1. **"Blindspot" framing 问题**（R1-N3 ≡ R2-N1）：核心 narrative 混淆 measurement sensitivity 和 statistical power。Figure 4 的 evidence 只支持量性差距而非质性 blindspot。Thurstone (1927) 已知。**这是论文最大的 framing 风险。**

2. **Causal 语言过强**（R1-N1 ≡ R2-N2）：Title "Counterfactual"、§3.5 "Causal Framework"、DAG 与方法论强度不匹配。Table 3 originality OR 显著是 shared empirical evidence 表明识别假设部分违反。

3. **GEE "decomposition" 命名**：在残余 confounding 下 "decomposition" 有误导性，应改为 "partial adjustment" 或 "conditional analysis"。

4. **缺少人工评估**：ACL/EMNLP 涉及 text generation 的工作通常需要至少 small-scale human evaluation，论文完全依赖自动化验证。

5. **小样本 OR 不稳定**：n=88 的 GEE OR 估计可信度受损，n=355 结果更可靠，应提升为主结果。

---

## Reviewer Divergence [REBUT]

分歧仅在 Should-Fix 级别，无 Must-Fix 分歧：

1. **R2-N3 severity**（证据范围过窄）：R2 评为 critical，R1 部分反驳——cross-benchmark 已覆盖 3 种任务类型，Register 在主文 §5.5 有讨论（非仅 Limitations），R2 对 "tone axis 只在 Limitations 提及" 和 "不覆盖 dialogue" 的具体论据不准确。**Director 判定**：降为 warning (SF9)。

2. **Claude negative control 解释力**：R2 认为解释力有限（warning），R1 认为 discriminative validity 论证合理。**Director 判定**：降为 info。

3. **Appendix placement**：R2 建议将 Direction Asymmetry 和 GEE Robustness 移入正文；R1 认为 8 页限制下当前安排合理。**Director 判定**：当前安排可接受，不列为 issue。

---

## Questions for Authors

1. **Blindspot 本质**：Figure 4 power curve 是否 asymptotically converge（Likert 和 pairwise 在足够大 n 下检测结果是否收敛）？如果收敛，"Blindspot" 应降级为 "efficiency gap"。如果不收敛（Likert 存在 measurement attenuation），"Blindspot" 有更强依据——你们能否提供 Likert effect size 随 n 变化的分析？

2. **n=355 Likert effect size**：该配置下的 Cohen's d 是多少？这是区分 "power gap"（d 不变，n 不够）和 "measurement attenuation"（d 本身被压缩）的关键数据。

3. **多轴测量**：对 formality rewrite，是否测量了 rewrite 在 register/verbosity 轴上的变化幅度？若 formal rewrite 同时变得更 verbose 或更 academic，单轴干预假设被违反。

4. **Formality independence test**：是否计划补做 formality 轴的 rewriter independence test（GPT-4o rewriter + Qwen3-32B judge）？这是验证 Qwen3-32B evaluator-producer confound 的关键实验。

5. **NLI gate selection effect**：被 NLI gate 过滤掉的 pairs 在 style change magnitude 上是否有系统性偏差？

6. **Pairwise Likert difference**：是否考虑过使用 Likert 分数的 pairwise difference（paired t-test on Δscore）？这会消除 tie-inflation 问题同时保留 Likert 信息。

---

## Missing References

两位 Reviewer 共同识别的缺失引用：
- Feder et al. (2021) "CausaLM: Causal Model Explanation Through Counterfactual Language Models"
- Wu et al. (2021) "Polyjuice: Generating Counterfactuals for Explaining, Training, and Evaluating NLMs"
- Clark et al. (2021) "All That's Human Is Not Gold: Evaluating Human Evaluation of Generated Text"
- Amidei et al. (2019) "Agreement is overrated: A plea for correlation to assess human evaluation reliability"
- Boubdir et al. (2023) "Elo Uncovered: Robustness and Best Practices in Language Model Evaluation" (或同类 BT-in-LLM-eval 方法论文献)
- Wu & Aji (2023) "Style Over Substance: Evaluation Biases for Large Language Models" (如果与 murugadoss2025sos 非同一工作)

---

## External Review (Stanford Agentic Reviewer)

**状态：pending（未返回）**

外部审稿请求已于 2026-05-21T09:36 发送，8 小时提醒已排期。截至报告提交时外部结果尚未返回。建议 Research Director 在外部审稿到达后补充参考。

---

## Visual Layout Check（非评分项）

**状态：done**（2026-05-21 09:36–09:38，耗时 ~2.5 min）

| 严重性 | 位置 | 发现 |
|--------|------|------|
| **Critical** | p.1-3 | 前 3 页纯文本无任何 display item（figure/table/diagram）。第一个 display item (Figure 1) 延迟到 p.4。严重影响审稿人第一印象。建议将 Figure 1 或 motivating example 提前到 p.1-2（Introduction 内）。 |
| Warning | p.5 | 单页堆叠 3 个 display items（Figure 2 + Table 1 + Figure 3），视觉拥挤。建议分散至相邻页面。 |
| Warning | p.6 | 纯文本页夹在 p.5 和 p.7 之间，节奏可改善。 |
| Warning | p.12 | 末页仅 1 条参考文献 + 90% 空白，不整洁。建议调整 bibsep 使 references 在 p.11 内结束。 |
| Info | p.4 | Figure 1 偏小、灰度感重，视觉冲击力不足。 |
| Info | p.5 | Table 1 加粗标注不够醒目；Figure 3 字号偏小。 |
| Info | p.7 | Figure 4 高 sample size 区域曲线重叠，legend 可改为直接标注。 |
| Info | p.10 | Appendix 三张表紧密堆叠，略拥挤但可接受。 |

**视觉审查结论**：最重要的建议是将 Figure 1 或概念图提前到第 1-2 页，给审稿人提供早期视觉锚点。

---

## Overall Assessment

**评分：3.0 / 5 — Findings**

**置信度：4 / 5**

### 评分理由

论文在统计方法论执行上扎实（7 种方法三角验证、GEE per-axis 分解、完整的 diagnostics），核心发现（Likert vs pairwise 在 LLM evaluation 中的 ~4.5× 效率差距）对评测实践有实际价值。Negative results 的诚实呈现和 Claude 作为 discriminative validity 证据增加了科学可信度。

但三个 Must-Fix 问题制约了论文的贡献层级：

1. **Novelty ceiling 是结构性的**：核心发现是 Thurstone (1927) 以来心理测量学已知原理在 LLM domain 的量化确认，而非 genuine new discovery。两位 Reviewer 的 Excitement 评分（3/5, 3.5/5）反映了这一判断。

2. **Framing 系统性过强**：Title "Counterfactual"、§3.5 "Causal Framework"、"Blindspot"（质性 framing）、"Decomposition"（暗示干净分离）——四处核心术语均超出方法论强度。Table 3 originality OR 显著是识别假设部分违反的经验证据。这些 framing 问题不是局部修辞瑕疵，而是贯穿论文核心 narrative 的系统性问题。

3. **Evaluator-producer confound 控制有缺口**：Independence test 仅覆盖 verbosity，而 formality 恰是 confound 最明显的轴。"Across two judges" 的 generalizability claim 基础不完整。

这些问题在当前状态下将论文定位在 Findings 水平（3.0）。若能解决 MF1-MF3（framing 降级 + formality independence test），论文有望提升到 3.5（Borderline Conference）。

### 与两位 Reviewer 评分的差异说明

两位 Reviewer 均评 3.5（Borderline Conference）。Director 评 3.0（Findings）的原因：
- 交叉分享后三个 Must-Fix 的共识更加强化（无任何 Must-Fix 被 rebut），尤其是 Blindspot framing 问题在交叉讨论中被 R2 进一步深化（measurement attenuation vs power gap 的未完成分析）
- Novelty ceiling（domain transfer of known psychometric principle）是结构性限制，难以通过局部修改突破
- Framing 问题的 pervasiveness（Title + Abstract + Method section name + Contribution claims）意味着修正工作量不小且可能影响论文的 selling point

---

## Detailed Comments（逐节）

### Abstract
- 过长过密（9 行），试图覆盖 7 种统计方法、4 个配置、3 个 benchmark。建议精简至 5-6 行。
- "Likert Blindspot" 首次出现未加 qualifier，暗示质性缺陷。

### §1 Introduction
- Contribution 1 "interventional framework" 在当前方法论强度下过强。
- Contribution 4 "style bias audits should employ pairwise comparison" 缺乏 qualifier。
- "~60% uninformative ties" 数字有力但在 Abstract/§1/§5.2 重复出现。

### §2 Related Work
- 基本覆盖 LLM judge bias 主线，但引用量偏少（27 条）。
- 缺 counterfactual generation 方法谱系和 NLG evaluation scale design 文献。
- 与 Thurstone (1927) 的关系讨论不充分。

### §3 Method
- §3.1 Binary style-controlled rewriting 描述清晰但无人工验证。
- §3.2 NLI gate：direction-aware 放宽合理但额外 pairs 质量未验证。
- §3.5 "Causal Framework" 标题过强；DAG 缺 residual S→Q path；识别假设 (iii) 未检验。

### §4 Experimental Setup
- 实验设计合理（position-controlled、consistency filtering）。
- n=100 LLMBar 作为起点可接受，但应更突出 n=355/400 scaled replication。

### §5 Results
- Table 1 主结果表信息量大但 Holm-Bonferroni 标注可更直觉。
- Table 2 七种 Likert 方法全部 fail 是有力证据。
- §5.6 GEE decomposition 命名应降级；confound gradient 的替代解释（rewriting difficulty）未讨论。
- Figure 4 power curve 是有价值贡献但支持 "efficiency gap" 而非 "blindspot"。

### §6 Conclusion
- "Prompt-level debiasing is insufficient" 缺乏 evidence 基础。
- Practical recommendation 应加 qualifier。

### Limitations
- 覆盖了关键弱点（evaluator-producer、NLI 验证、scale granularity、benchmark coverage）。
- 缺少对 confound gradient 替代解释的讨论。
- "An independent spot-check with GPT-4o is planned" 应执行而非承诺。

### 格式与视觉
- 正文 8 页合规。
- 前 3 页无任何 display item 是最大的视觉问题。
- p.5 display items 过度集中。