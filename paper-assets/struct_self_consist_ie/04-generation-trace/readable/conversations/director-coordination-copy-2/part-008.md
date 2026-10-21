# Director coordination — Part 8 of 16

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[← Part 7](part-007.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 9 →](part-009.md) · [Structured JSON](../../../sessions/6a/6a5a1a2f9a2bf6bdf404.json)

## Round 168

### User

_source line 2236 · 2026-05-19T03:31:26.740685+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

主要发现摘要：

**Overall: 3.0/5（建议 Findings）**

三个 Critical 问题：
1. **正文超页约 2 页**（10 页 vs 8 页限制），desk reject 风险
2. **"Correlation-selection gap" 缺乏理论深度**，停留在实证描述层面
3. **标题暗示纯 negative result，但 §4.7 有显著 positive construction result**，叙事不统一

五个 Warning 问题：Abstract 缩写未展开（LP, AUROC）、与 Yao et al. 2026 区分不够锐利、gating protocol 用 test set 做 probe、SciERC 主实验仅 1 seed 且 sensitivity 高、entity-level construction 本质是 entity majority voting 新颖性有限。

写作质量方面通过了 AI 风格检查：无 em-dash、无黑名单词汇、无 -ing 短语结尾模式。引用验证通过（68 条全部有对应 cite，无 orphan/missing）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2237 · 2026-05-19T03:31:33.441757+00:00_

Reviewer 2 意见已收到。等待 Reviewer 1 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 169

## Round 169

6 recorded events


### User

_source line 2238 · 2026-05-19T03:42:30.070744+00:00_

[Reviewer 1 审稿意见]:
## Round 1 审稿意见 — Reviewer 1（方法严谨性 + 实验设计）

**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Improve LLM-Based Named Entity Recognition

---

## Summary

本文系统评估 5 种 confidence signal（投票、log-probability、共识）能否通过质量估计（QE）或样本选择改善 LLM-based NER。核心发现为"correlation-selection gap"：所有信号可靠预测输出质量，但没有信号能在选择任务上持续超越 greedy decoding。论文将此归因于 instance degeneracy 和 LP alignment compression。研究极其彻底（4 数据集、2 模型族、3 seed、5-fold CV、22 页附录），为结构化预测中 self-consistency 的局限提供了有价值的负面结论。

---

## 总体评分

**Overall**: 3/5（Findings: could be accepted to the Findings of the ACL）
**一句话总结**: 方法论严谨、实验极度充分的负面结果论文，但核心发现在高性能数据集上部分同义反复，适用范围局限于 LoRA 微调中小规模模型，且标题的普遍性声明超出实验支撑范围。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨，统计方法得当（TOST、bootstrap、BH correction），但实体匹配标准定义缺失影响核心方法的可复现性，SciERC 统计功效存疑 |
| Excitement | 2.5/5 | QE-selection 分解是有用的概念框架，但负面结论在高 F1 数据集上部分可预期；诊断有价值但未指向新方法或解决方案 |
| Reproducibility | 4/5 | 超参数详尽记录（Appendix H），使用公开数据集和具名模型，承诺代码开源 |
| Confidence | 4/5 | 通读全文 36 页（含全部附录），熟悉 self-consistency、MBR decoding、NER 和 LLM calibration 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **正文主体超出 8 页限制**
- 具体位置：全文结构，Sections 1–6
- 问题：正文主体（Sections 1–6 Conclusion）延伸至约第 10 页中部，Limitations 从第 10 页底部开始。ACL/ARR 长文要求正文 ≤8 页（Limitations、Ethics Statement、References、Appendix 不计入）。当前正文约 9.5 页，超出约 1.5 页。主因是 Section 5（Discussion）单独占约 2 页，包含 LP compression mechanisms、capability-diversity tension、from diagnosis to practice 等大量分析性内容。
- 为什么影响接收：超页限可能触发 desk rejection，且审稿人会质疑论文的 space efficiency。
- 建议修改方向：将 Section 5 中诊断细节（LP compression mechanisms 小节、capability-diversity tension 小节）移至附录，正文仅保留核心诊断结论（degeneracy + compression 两句话总结）和实践建议（selective prediction、entity-level construction 可用性）。Discussion 压缩至约 0.5 页即可。

**N2** [critical] **实体匹配标准未精确定义——核心方法论缺陷**
- 具体位置：Section 3.2，EVC 与 Soft Jaccard 的定义
- 问题：EVC 计算中"其他 sample 是否包含匹配实体"的"匹配"含义未定义。Soft Jaccard（Eq. 2）使用 |M|（matched set）但未定义 M 的成员条件。具体而言未说明：(a) 是否需要精确文本 + 精确类型？(b) span 边界是否需完全一致？(c) 是否允许部分重叠？(d) 是否做模糊匹配？NER 中 span 边界天然模糊（如 "New York" vs. "New York City"），匹配标准的选择直接影响 EVC/SJ 的数值和诊断力。
- 为什么影响接收：这是 5 个信号中 2 个的核心定义缺失，影响方法可复现性和结论可信度。审稿人无法判断 EVC/SJ 的信号质量是否因匹配标准偏紧/偏松而人为偏高/偏低。
- 建议修改方向：在 Section 3.2 明确给出实体匹配的数学定义（例如 $e_i = e_j \iff \text{span}(e_i) = \text{span}(e_j) \land \text{type}(e_i) = \text{type}(e_j)$），并在附录中消融不同匹配严格度（exact vs. partial overlap vs. type-only）对信号质量的影响。

**N3** [critical] **核心 claim 在高性能数据集上存在循环论证风险，且 entity-level 结果与标题矛盾**
- 具体位置：Section 4.2（CoNLL results）, Section 4.3（degeneracy analysis）, Table 48（Appendix Z.4）
- 问题分两层：
  - **循环论证**：CoNLL greedy F1≈0.907，degeneracy ≥65%。"信号无法改善选择"在此设置下近乎同义反复——65% 的 instance 所有 N 个样本完全相同（无选择空间），剩余 35% 的 instance 也接近性能上限（改善空间极小）。这不是"信号失败"，而是"场景不需要信号"。论文未充分区分"信号本身无信息量"与"任务已无改善余地"。
  - **与标题矛盾**：Table 48（p.36）显示 entity-level majority voting 在 SciERC 上改善 +1.57 pp（Recovery +11.9%），但在 CoNLL 上恶化 -0.38 pp。这表明 confidence signal 在低 F1 的困难任务上实际有效。但论文标题 "Why Confidence Signals **Fail** to Improve LLM-Based NER" 做出了普遍性否定声明，与 SciERC 上的正面结果矛盾。
- 为什么影响接收：核心 claim 的精确性直接决定论文贡献的可信度。过于宽泛的否定声明会被审稿人视为 overclaim。
- 建议修改方向：(1) 将 claim 精确限定为"在 LoRA 微调的高性能 NER 设置下（greedy F1 > 0.75），instance-level sample selection 无法受益于 confidence signals"；(2) 标题修改为突出 gap 而非失败，如 "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based NER"；(3) 正文 Section 5 中明确讨论 ceiling effect 与信号失效的交互作用，将 SciERC entity-level 正面结果作为对照证据而非边缘附录发现。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **最关键的鲁棒性证据埋在附录中**
- 具体位置：Appendix N（Table 39, p.30）vs. Section 4.5
- 问题：Appendix N 显示 T=1.0 时 degeneracy 从 ~68% 降至 ~15%，但 selection 仍不超过 greedy。这是证明结论非 T=0.6 人为导致的最关键证据。然而 Section 4.5 仅讨论信号稳定性，未突出"低 degeneracy 条件下 selection 仍失败"这一关键发现。
- 建议：在 Section 4.5 增加一句："Even at T=1.0 where degeneracy drops to ~15%, LP-based selection still fails to exceed greedy (Table 39)." 这比 22 页附录中的结论更有说服力。

**W2** [warning] **仅测试 LoRA 微调，但标题和摘要做出不限定的 claim**
- 具体位置：Title, Abstract, Section 4.1
- 问题：alignment compression（LP 范围压缩）可能是 LoRA 特有现象。LoRA 仅修改低秩子空间的权重，可能比全量微调更强地压缩 output distribution 的 LP variance。论文的所有实验均使用 LoRA，但标题说"LLM-Based NER"暗示普遍性。In-context learning（无微调）和全量微调的 LP 分布特性可能完全不同。
- 建议：Abstract 中限定 claim 为"LoRA fine-tuned LLMs"，或增加至少一个 in-context learning baseline（无需全量微调，ICL 实验成本低）以验证结论的迁移性。

**W3** [warning] **SciERC（n=529）统计功效可能不足以支撑等价性声明**
- 具体位置：Section 4.1, Appendix F（TOST test）
- 问题：SciERC 仅 529 test instances。5-fold CV 下每折约 106 个 test instances。TOST 等价检验（δ=0.5 pp）在此样本量下的 power 取决于效应量和方差，但论文未报告功效分析。"selection 与 greedy 等价"的结论可能反映检验功效不足（Type II error），而非真正的效应缺失。对比 Few-NERD（n=32,565），同样的 TOST 在大样本上功效充分，但在 SciERC 上可能 power < 0.5。
- 建议：报告 SciERC 上 TOST 的 post-hoc power 分析，或至少说明在 n=529、观测方差下，可检测的最小效应量（minimum detectable effect）是多少。

**W4** [warning] **Oracle 分析未回答核心问题：信号在哪里具体失败？**
- 具体位置：Section 4.2, Appendix F
- 问题：Oracle selection 在 SciERC 上可获得显著改善，证明 N 个 sample 中确实存在可选择的 variation。但论文未分析：oracle 选择了哪些 instance 的不同 sample？这些 instance 与 signal-selected instance 有何区别？哪些实体类型/句子长度/结构特征使 oracle 有效但 signal 失效？这类 error analysis 是理解信号失败模式的关键。
- 建议：增加 oracle-selected vs. signal-selected 的 instance-level 对比分析（例如按实体类型、句子长度、实体密度分层），以提供可操作的改进方向。

**W5** [warning] **"Soft Jaccard" 命名与标准指标混淆**
- 具体位置：Section 3.2, Eq.(2)
- 问题：Eq.(2) 的公式结构使用 min/max 归一化，与标准 Jaccard index |A∩B|/|A∪B| 不同。"Soft" 一词在信息检索和 NLP 中有其他含义（如 soft matching、soft attention）。当前命名可能误导读者认为这是标准 Jaccard 的某种 soft 版本。
- 建议：明确说明与标准 Jaccard 的区别，或考虑更精确的命名。

---

## Questions（需要作者澄清）

Q1. EVC 和 Soft Jaccard 中的实体"匹配"标准具体是什么？是精确 span 文本 + 精确实体类型的完全匹配，还是允许 span 边界的部分重叠？

Q2. TOST 等价检验使用的等价边界 δ 的具体值是多少？该值的选择依据是什么？0.5 pp 作为 NER F1 的"实质等价"阈值是否有先例支持？

Q3. Table 48 显示 entity-level majority voting 在 SciERC 上改善 +1.57 pp 但在 CoNLL 上恶化 -0.38 pp。作者如何调和此不对称结果与论文"信号失败"的普遍性结论？

Q4. Greedy baseline 使用 T=0（argmax）。单个 T=0.6 样本的平均 F1 与 greedy 相比如何？如果单样本 F1 已显著低于 greedy，则 selection 面对的是"从 N 个较弱样本中选最好的 vs. 一个强样本"的比较，这与"信号无信息量"是不同的 claim。

Q5. Supervised combination（LR, MLP, RF）的训练/测试划分如何实现？是否在 5-fold CV 内部嵌套了独立的 held-out set 用于信号权重训练？是否存在 signal 训练与 F1 评估之间的数据泄露风险？

Q6. Appendix H 提到禁用了 Qwen3 的 thinking mode。能否确认 LP 计算完全排除了 thinking tokens？如果 training 阶段的 thinking tokens 影响了模型的 LP distribution，即使 inference 时禁用，LP 信号仍可能受训练时 thinking 行为的残余影响。

---

## Missing References

引用覆盖总体良好（68 条 bib entries, 109 次引用, 0 orphan, 0 missing）。以下方向可加强：

1. **LLM 校准文献**：Kadavath et al. (2022) "Language Models (Mostly) Know What They Know" 直接研究 LLM 的自我评估能力与 log-probability 的关系，与本文的 LP-based QE 高度相关但未引用。
2. **结构化预测中的 uncertainty**：如存在针对序列标注/信息抽取的 uncertainty estimation 工作（非分类任务），应补充引用以强化 related work 中"structured vs. discrete"的论述。
3. 引用核查结果：4 条引用在 OpenAlex 中未找到（hobelsberger2025, lightman2024, venktesh2025, aggarwal2023），5 条存在轻微不匹配（feng2025, snell2025, muller2021, park2024, chen2025twofailures）。经检查均为近期 preprint 或索引延迟导致，不像幻觉引用，但建议复核这 9 条 BibTeX entry 的年份和 venue 信息准确性。特别是 lightman2024（"Let's Verify Step by Step"）是知名论文，可能存在年份标注错误（原为 2023 ICLR 投稿）。

---

## Minor Issues

1. Abstract 称"F1 gains ≤ 0.42 pp"，但 Table 48 (Appendix Z.4) 显示 SciERC entity-level voting 获得 +1.57 pp。需澄清 0.42 pp 是否仅指 instance-level selection（非 entity-level construction），否则存在数据不一致。
2. "N-scaling" 与 "sample size scaling" 两种术语混用，建议统一。
3. "Confidence signal" 作为 5 种不同性质指标（投票频率、log-probability、agreement measure）的总称在概念上不够精确。EMV/EVC 是投票频率而非校准概率，MBR/SJ 是一致性度量。建议使用更中性的总称如 "quality signal" 或在 Section 3 开头明确说明 "confidence signal" 在本文的操作定义。
4. 部分 Figure（如 Figure 3 scatter plots）在会议打印尺寸下标签可能难以辨认，建议增大字体或简化数据点标注。
5. 提交前务必检查正文页数。建议在 \section{6} Conclusion 末尾手动检查页码是否 ≤8。

---

## 主要优势

1. **QE-selection 分解框架**：将 self-consistency 解构为"预测质量"和"利用预测选择"两个独立任务，是清晰且可迁移的概念贡献。
2. **实验极度充分**：22 页附录涵盖温度、N-scaling、模型规模、模型族、监督组合、hidden state probe、free-form 格式、OOD 评估、epoch confound 等，远超典型负面结果论文的标准。
3. **统计方法高于平均水准**：TOST 等价检验、bootstrap CI、sign test、BH 多重比较校正的使用在 NER 论文中不常见，值得肯定。
4. **诊断分析可操作**：instance degeneracy 和 alignment compression 的识别为后续工作指明了方向（何时 reranking 可能有效：低 degeneracy + 未压缩的 LP 分布）。
5. **Thinking token confound 的诚实处理**（Appendix H/J）：主动记录 Qwen3 thinking token 的处理方式，体现了实验设计的严谨性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2239 · 2026-05-19T03:43:12.439378+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n# Reviewer 2 审稿意见 — Round 1\n\n## 审查侧重：新颖性 + 叙事完整性 + 写作质量\n\n**Overall**: 3.0 / 5（Findings）\n\n## Summary\n\n本文系统评估了五种置信信号在 LLM NER 任务上的质量估计（QE）和样本选择（selection）能力，发现所有信号在 QE 上表现可靠（ρ 高达 0.45, AUROC 高达 0.82），但在 best-of-N selection 上普遍失败。论文诊断出两个失败机制——instance degeneracy 和 LP compression——并提出 entity-level construction 作为替代方案。实验在 4 个 NER benchmark、2 个模型家族上进行，统计分析全面。\n\n## Strengths\n\n**S1.** 实验设计和统计严谨性出色。\n**S2.** QE-selection 分离的 framing 有价值。\n**S3.** 诊断分析有深度。\n**S4.** Entity-level construction 提供了可操作的正面结果。\n**S5.** 写作质量在 AI 风格检查上表现优秀。\n\n## Weaknesses — Must-Fix\n\n**N1** [critical] **正文严重超页：约 10 页 vs 8 页限制**\nDiscussion 单独占约 2 页是主因。建议 Discussion 降级为 Experiments subsection 并大幅压缩；Hidden state probe (§4.6) 和 Robustness (§4.5) 细节移入 appendix。\n\n**N2** [critical] **核心概念 \"correlation-selection gap\" 缺乏足够的理论深度**\n本质上是实证观察而非理论贡献。未提供形式化分析来解释为什么 QE 相关性高不等于 selection 有效。建议提供在 degeneracy 率 d 和 alignment ρ 已知时 best-of-N expected gain 的 bound。\n\n**N3** [critical] **标题与内容的 framing 不一致**\n标题 \"Why Confidence Signals Fail\" 暗示纯 negative result，但 §4.7 entity-level construction 给出显著 positive result。建议标题反映完整故事弧。\n\n## Weaknesses — Should-Fix\n\n**W1** [warning] Abstract 中 LP 和 AUROC 缩写未展开。\n**W2** [warning] 与 Yao et al. (2026) 的区分可以更锐利。\n**W3** [warning] LP-alignment gating protocol 用 test set 做 probe，方法论问题。\n**W4** [warning] SciERC 主实验仅用 1 seed，σ=0.48 pp。\n**W5** [warning] Entity-level construction 本质是 entity majority voting，新颖性有限。\n**W6** [warning] \"the correct self-consistency analogy\" 措辞过于绝对。\n\n## Questions\nQ1. SciERC greedy F1 四值不一致，能否统一为 canonical configuration？\nQ2. Few-NERD LP selection 成功是否本质上是 under-training 的结果？\nQ3. within-instance ρ(LP, F1) 跨数据集与 LP gain 的相关性数据？\nQ4. Entity construction 阈值 θ 在 SciERC 用 θ=2/N（post-hoc）vs 其他用 CV，为何不一致？\n\n## Missing References\n1. Wan et al. (2024) — NER/IE LLM survey\n2. Xie et al. (2023) — self-evaluation beam search\n3. Sun et al. (2023) — LLM calibration for text classification\n4. Ensemble-based IE methods 讨论缺失\n\n## Minor Issues\n1. \"a alignment-based\" → \"an alignment-based\"（冠词错误）\n2. Abstract 最后一句过长\n3. Figure 2 caption 应指明具体哪条线\n4. \\citep 和 \\cite 混用"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n# Reviewer 2 审稿意见 — Round 1\n\n## 审查侧重：新颖性 + 叙事完整性 + 写作质量\n\n**Overall**: 3.0 / 5（Findings）\n\n## Summary\n\n本文系统评估了五种置信信号在 LLM NER 任务上的质量估计（QE）和样本选择（selection）能力，发现所有信号在 QE 上表现可靠（ρ 高达 0.45, AUROC 高达 0.82），但在 best-of-N selection 上普遍失败。论文诊断出两个失败机制——instance degeneracy 和 LP compression——并提出 entity-level construction 作为替代方案。实验在 4 个 NER benchmark、2 个模型家族上进行，统计分析全面。\n\n## Strengths\n\n**S1.** 实验设计和统计严谨性出色。\n**S2.** QE-selection 分离的 framing 有价值。\n**S3.** 诊断分析有深度。\n**S4.** Entity-level construction 提供了可操作的正面结果。\n**S5.** 写作质量在 AI 风格检查上表现优秀。\n\n## Weaknesses — Must-Fix\n\n**N1** [critical] **正文严重超页：约 10 页 vs 8 页限制**\nDiscussion 单独占约 2 页是主因。建议 Discussion 降级为 Experiments subsection 并大幅压缩；Hidden state probe (§4.6) 和 Robustness (§4.5) 细节移入 appendix。\n\n**N2** [critical] **核心概念 \"correlation-selection gap\" 缺乏足够的理论深度**\n本质上是实证观察而非理论贡献。未提供形式化分析来解释为什么 QE 相关性高不等于 selection 有效。建议提供在 degeneracy 率 d 和 alignment ρ 已知时 best-of-N expected gain 的 bound。\n\n**N3** [critical] **标题与内容的 framing 不一致**\n标题 \"Why Confidence Signals Fail\" 暗示纯 negative result，但 §4.7 entity-level construction 给出显著 positive result。建议标题反映完整故事弧。\n\n## Weaknesses — Should-Fix\n\n**W1** [warning] Abstract 中 LP 和 AUROC 缩写未展开。\n**W2** [warning] 与 Yao et al. (2026) 的区分可以更锐利。\n**W3** [warning] LP-alignment gating protocol 用 test set 做 probe，方法论问题。\n**W4** [warning] SciERC 主实验仅用 1 seed，σ=0.48 pp。\n**W5** [warning] Entity-level construction 本质是 entity majority voting，新颖性有限。\n**W6** [warning] \"the correct self-consistency analogy\" 措辞过于绝对。\n\n## Questions\nQ1. SciERC greedy F1 四值不一致，能否统一为 canonical configuration？\nQ2. Few-NERD LP selection 成功是否本质上是 under-training 的结果？\nQ3. within-instance ρ(LP, F1) 跨数据集与 LP gain 的相关性数据？\nQ4. Entity construction 阈值 θ 在 SciERC 用 θ=2/N（post-hoc）vs 其他用 CV，为何不一致？\n\n## Missing References\n1. Wan et al. (2024) — NER/IE LLM survey\n2. Xie et al. (2023) — self-evaluation beam search\n3. Sun et al. (2023) — LLM calibration for text classification\n4. Ensemble-based IE methods 讨论缺失\n\n## Minor Issues\n1. \"a alignment-based\" → \"an alignment-based\"（冠词错误）\n2. Abstract 最后一句过长\n3. Figure 2 caption 应指明具体哪条线\n4. \\citep 和 \\cite 混用"
  }
}
```

</details>

---


### Tool result

_source line 2240 · 2026-05-19T03:43:30.789295+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18349
}
```

</details>

---


### Tool call

_source line 2241 · 2026-05-19T03:43:31.004368+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n# Reviewer 1 审稿意见 — Round 1\n\n## 审查侧重：方法严谨性 + 实验设计\n\n**Overall**: 3/5（Findings）\n\n## Summary\n\n本文系统评估 5 种 confidence signal 能否通过 QE 或样本选择改善 LLM-based NER。核心发现为\"correlation-selection gap\"。论文将此归因于 instance degeneracy 和 LP alignment compression。研究极其彻底（4 数据集、2 模型族、3 seed、5-fold CV、22 页附录）。\n\n## Must-Fix\n\n**N1** [critical] **正文主体超出 8 页限制（约 9.5 页）**\nSection 5 Discussion 单独占约 2 页。建议将 Discussion 中诊断细节移至附录，正文仅保留核心结论。\n\n**N2** [critical] **实体匹配标准未精确定义——核心方法论缺陷**\nEVC 和 Soft Jaccard 中\"匹配\"含义未定义：(a) 是否需精确文本+精确类型？(b) span 边界是否需完全一致？(c) 是否允许部分重叠？这是 5 个信号中 2 个的核心定义缺失。建议给出数学定义并消融不同匹配严格度。\n\n**N3** [critical] **核心 claim 在高性能数据集上存在循环论证风险，且 entity-level 结果与标题矛盾**\n两层问题：\n- CoNLL degeneracy ≥65%，\"信号无法改善选择\"近乎同义反复——场景不需要信号，而非信号失败\n- 标题 \"Why Confidence Signals Fail\" 做出普遍性否定，但 SciERC entity-level construction +1.57 pp 是正面结果\n建议将 claim 精确限定为特定设置，标题突出 gap 而非 failure。\n\n## Should-Fix\n\n**W1** [warning] 最关键的鲁棒性证据（T=1.0 低 degeneracy 下 selection 仍失败）埋在附录中。\n**W2** [warning] 仅测试 LoRA 微调，但标题做出不限定的 claim。建议限定为 \"LoRA fine-tuned LLMs\" 或增加 ICL baseline。\n**W3** [warning] SciERC n=529 统计功效可能不足以支撑等价性声明，未报告 TOST post-hoc power。\n**W4** [warning] Oracle 分析未回答：信号在哪些 instance 具体失败？缺少 instance-level error analysis。\n**W5** [warning] \"Soft Jaccard\" 命名与标准 Jaccard index 混淆。\n\n## Questions\nQ1. EVC 和 SJ 中实体\"匹配\"的具体标准？\nQ2. TOST 等价边界 δ 的具体值和选择依据？\nQ3. Entity-level voting 在 SciERC +1.57 pp vs CoNLL -0.38 pp 的不对称如何调和？\nQ4. Greedy (T=0) 与单个 T=0.6 样本的 F1 比较？\nQ5. Supervised combination 的 5-fold CV 是否存在数据泄露？\nQ6. LP 计算是否排除了 thinking tokens？\n\n## Missing References\n1. Kadavath et al. (2022) \"Language Models Know What They Know\" — LLM self-evaluation\n2. 结构化预测 uncertainty estimation 工作\n3. 9 条 bib entry 需复核年份/venue（hobelsberger2025, lightman2024 等）\n\n## Minor Issues\n1. \"Confidence signal\" 作为总称不够精确，建议用 \"quality signal\"\n2. Figure 3 打印尺寸下标签可能难辨\n3. \"N-scaling\" vs \"sample size scaling\" 术语不统一"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n# Reviewer 1 审稿意见 — Round 1\n\n## 审查侧重：方法严谨性 + 实验设计\n\n**Overall**: 3/5（Findings）\n\n## Summary\n\n本文系统评估 5 种 confidence signal 能否通过 QE 或样本选择改善 LLM-based NER。核心发现为\"correlation-selection gap\"。论文将此归因于 instance degeneracy 和 LP alignment compression。研究极其彻底（4 数据集、2 模型族、3 seed、5-fold CV、22 页附录）。\n\n## Must-Fix\n\n**N1** [critical] **正文主体超出 8 页限制（约 9.5 页）**\nSection 5 Discussion 单独占约 2 页。建议将 Discussion 中诊断细节移至附录，正文仅保留核心结论。\n\n**N2** [critical] **实体匹配标准未精确定义——核心方法论缺陷**\nEVC 和 Soft Jaccard 中\"匹配\"含义未定义：(a) 是否需精确文本+精确类型？(b) span 边界是否需完全一致？(c) 是否允许部分重叠？这是 5 个信号中 2 个的核心定义缺失。建议给出数学定义并消融不同匹配严格度。\n\n**N3** [critical] **核心 claim 在高性能数据集上存在循环论证风险，且 entity-level 结果与标题矛盾**\n两层问题：\n- CoNLL degeneracy ≥65%，\"信号无法改善选择\"近乎同义反复——场景不需要信号，而非信号失败\n- 标题 \"Why Confidence Signals Fail\" 做出普遍性否定，但 SciERC entity-level construction +1.57 pp 是正面结果\n建议将 claim 精确限定为特定设置，标题突出 gap 而非 failure。\n\n## Should-Fix\n\n**W1** [warning] 最关键的鲁棒性证据（T=1.0 低 degeneracy 下 selection 仍失败）埋在附录中。\n**W2** [warning] 仅测试 LoRA 微调，但标题做出不限定的 claim。建议限定为 \"LoRA fine-tuned LLMs\" 或增加 ICL baseline。\n**W3** [warning] SciERC n=529 统计功效可能不足以支撑等价性声明，未报告 TOST post-hoc power。\n**W4** [warning] Oracle 分析未回答：信号在哪些 instance 具体失败？缺少 instance-level error analysis。\n**W5** [warning] \"Soft Jaccard\" 命名与标准 Jaccard index 混淆。\n\n## Questions\nQ1. EVC 和 SJ 中实体\"匹配\"的具体标准？\nQ2. TOST 等价边界 δ 的具体值和选择依据？\nQ3. Entity-level voting 在 SciERC +1.57 pp vs CoNLL -0.38 pp 的不对称如何调和？\nQ4. Greedy (T=0) 与单个 T=0.6 样本的 F1 比较？\nQ5. Supervised combination 的 5-fold CV 是否存在数据泄露？\nQ6. LP 计算是否排除了 thinking tokens？\n\n## Missing References\n1. Kadavath et al. (2022) \"Language Models Know What They Know\" — LLM self-evaluation\n2. 结构化预测 uncertainty estimation 工作\n3. 9 条 bib entry 需复核年份/venue（hobelsberger2025, lightman2024 等）\n\n## Minor Issues\n1. \"Confidence signal\" 作为总称不够精确，建议用 \"quality signal\"\n2. Figure 3 打印尺寸下标签可能难辨\n3. \"N-scaling\" vs \"sample size scaling\" 术语不统一"
  }
}
```

</details>

---


### Tool result

_source line 2242 · 2026-05-19T03:43:32.612760+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1608
}
```

</details>

---


### Assistant

_source line 2243 · 2026-05-19T03:43:35.117315+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 170

## Round 170

2 recorded events


### User

_source line 2244 · 2026-05-19T03:43:37.879450+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

审稿要点总结：

- **Overall 3/5**（Findings level），Soundness 3.5/5，Excitement 2.5/5
- **3 个 critical 问题**：(1) 正文超 8 页限约 1.5 页；(2) EVC/Soft Jaccard 实体匹配标准未定义，属核心方法论缺陷；(3) 高 F1 数据集上发现存在循环论证风险，且 Table 48 中 SciERC entity-level voting +1.57pp 的正面结果与标题的普遍性否定声明矛盾
- **5 个 warning 问题**：关键鲁棒性证据埋在附录、仅测试 LoRA 微调但 claim 不限定、SciERC 统计功效不足、oracle 分析不够深入、Soft Jaccard 命名误导
- **引用核查**：68 条引用，0 orphan/0 missing，4 条未在线验证（均为近期 preprint），5 条轻微不匹配
- **主要肯定**：QE-selection 分解框架、实验极度充分（22 页附录）、统计方法高于平均、诊断分析可操作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2245 · 2026-05-19T03:43:53.040337+00:00_

两位 Reviewer 的初审均已确认提交，交叉分享任务已分发。等待两位 Reviewer 的 [AGREE]/[REBUT] 交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 171

## Round 171

2 recorded events


### User

_source line 2246 · 2026-05-19T03:46:35.734730+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix Issues

**[AGREE] R2-N1: 正文超页限（~10 页 vs 8 页限制）**
完全同意。我在 R1-N1 中独立提出了相同问题并估算超出约 1.5 页。R2 建议将 Discussion 降级为 Experiments subsection 并压缩是合理的，但我有补充建议：与其将 Discussion 降级（概念上仍是独立的分析贡献），不如保留 Section 5 标题但仅保留核心诊断结论（degeneracy + compression，各一段），将 LP compression mechanisms、capability-diversity tension 等展开分析移至附录。Hidden state probe (§4.6) 和 Robustness (§4.5) 移入附录我也同意——这两部分是支撑性证据，不是核心叙事。

**[PARTIALLY AGREE] R2-N2: "correlation-selection gap" 缺乏理论深度**
同意这本质上是实证观察而非理论贡献。但我认为将其列为 critical 过于严格。理由：(1) 本文定位为 empirical analysis paper 而非理论论文，EMNLP Findings 接受高质量实证分析；(2) R2 建议的 "在 degeneracy 率 d 和 alignment ρ 已知时 best-of-N expected gain 的 bound" 虽然理想，但这本身可能是一篇独立的理论工作；(3) 论文在 22 页附录中已提供了 exhaustive 的经验证据替代形式化分析。建议降为 warning：在 Section 4.3 增加一个简化的分析框架（例如：当 degeneracy 率 d > 0.5 时，expected selection gain 的上界为 (1-d) × oracle_gap，解释为什么 d=0.65 时 gain 被压缩至可忽略水平），无需完整理论证明。

**[AGREE] R2-N3: 标题与内容 framing 不一致**
完全同意，与我的 R1-N3 独立发现一致。补充证据：Table 48 (Appendix Z.4) 显示 SciERC entity-level majority voting 改善 +1.57 pp（recovery +11.9%），这是 substantive positive result，与标题 "Fail to Improve" 直接矛盾。R2 建议标题反映完整故事弧是对的。我的具体标题建议："Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based NER"——保留了核心 finding（gap）而非单纯否定（fail）。

---

### Should-Fix Issues

**[AGREE] R2-W1: Abstract 中 LP 和 AUROC 缩写未展开**
同意。重新阅读 Abstract 确认：AUROC 未展开（应为 "Area Under the Receiver Operating Characteristic curve"），LP 在 Abstract 中首次出现时可能未展开（正文 Section 3.2 才定义）。ACL 格式要求 Abstract 内的缩写自包含定义。这虽是小问题但容易修复。

**[PARTIALLY AGREE] R2-W2: 与 Yao et al. (2026) 的区分**
同意应更明确定位。但我未在参考文献中找到 Yao et al. (2026) 的具体引用，无法独立评估区分的锐利程度。如果 Yao et al. (2026) 是近期直接竞品（同样做 LLM NER 的 self-consistency），则需在 Related Work 中明确说明本文的 delta（例如：Yao 做了什么但没做什么，本文填补了什么）。建议作者在 Rebuttal 中明确这一定位。

**[AGREE] R2-W3: LP-alignment gating protocol 使用 test set 做 probe**
同意这是方法论问题。如果论文在 test set 上检查 LP-F1 相关性，然后基于该检查决定是否推荐 LP-based selection，这是用 test-set 信息指导评估方案的循环论证。虽然 LP 信号本身不从 test labels 训练，但"何时推荐 LP selection"这个决策如果依赖 test-set correlation，就存在 information leakage。这与我在 R1 中对 entity construction 阈值选择（Q6, supervised combination 训练/测试划分）的关切一致。建议：所有 gating/threshold 决策应在 validation fold 上做出，然后在 held-out test fold 上评估。

**[AGREE] R2-W4: SciERC 主实验仅用 1 seed**
如果属实，这直接加剧我在 R1-W3 中提出的 SciERC 统计功效问题。n=529 已经偏小，仅 1 seed 意味着结果可能高度依赖随机初始化。σ=0.48 pp 的方差在仅 1 seed 下无法与噪声区分。建议：SciERC 至少补充到 3 seeds 以确认结论的稳定性。如果 3 seeds 的 σ 仍为 0.48 pp 量级，则该不确定性应在 main text 中明确报告。

补充：Section 4.1 (p.5) 声称 "5-fold CV, 3 seeds"，但 R2 指出 SciERC 主实验可能实际仅用 1 seed。如果存在 general claim (3 seeds) 与 specific implementation (SciERC 1 seed) 的不一致，这本身就是一个 reporting clarity 问题。

**[PARTIALLY REBUT] R2-W5: Entity-level construction 新颖性有限**
部分反驳。R2 说 entity-level construction "本质是 entity majority voting" 是对的——方法本身并非新颖。但论文并未将其作为方法论贡献（contribution list 中未包含"新方法"），而是作为诊断性分析的一部分：在 instance-level selection 失败后，entity-level aggregation 作为替代方案的可行性验证。作为"分析发现"而非"方法贡献"，新颖性要求应该更低。

但我也同意 R2 的潜在关切：如果论文过度强调 entity-level construction 的效果（例如在 Abstract 或 Contribution 中），则需要 temper expectations——这确实是已知技术的应用，而非方法创新。建议作者在叙事中明确定位：entity construction 是已有技术在本文框架下的验证，而非本文的原创贡献。

**[AGREE] R2-W6: "the correct self-consistency analogy" 措辞过于绝对**
同意。"Correct" 暗示其他 analogy 都是错误的，这在学术写作中过于强势。建议改为 "a more appropriate analogy" 或 "a closer analogy"。Self-consistency 的 "正确" 形式取决于任务特性和评估目标，不存在唯一正确答案。

---

### Questions

**[AGREE] R2-Q1: SciERC greedy F1 四值不一致**
这是数据一致性的直接问题。我在 R1 审查中也关注了跨表格数字一致性，但因图像分辨率限制未能精确核实每个值。如果 SciERC greedy F1 在不同表格中出现四个不同数值，作者必须澄清哪些差异来自 seed/fold variation，哪些是配置差异，并确定一个 canonical configuration 作为 main text 的基准。

**[AGREE] R2-Q2: Few-NERD LP selection 成功是否为 under-training 结果**
这是一个有洞察力的假设。如果 Few-NERD 模型 under-trained（LP 分布未被充分压缩），LP-based selection 的"成功"可能只是反映了模型在 Few-NERD 上的 calibration 尚未被 LoRA 微调破坏，而非信号真正有效。这与论文的 "alignment compression" 诊断一致——compression 程度越低（即 training 越少），LP selection 越可能有效。但这反过来暗示 LP selection 的"失败"不是信号本身的问题，而是 LoRA training 的副作用。作者应直接用 Few-NERD 训练曲线上不同 checkpoint 的 LP compression 数据回答此问题。

**[AGREE] R2-Q3: within-instance ρ(LP, F1) 跨数据集与 LP gain 的相关性**
同意这是有价值的补充分析。如果 within-instance LP-F1 相关性能预测 LP selection gain 的大小，则可为 practitioners 提供一个先验判断工具：在部署前用小量 labeled data 估计 within-instance ρ，决定是否值得做 multi-sample selection。

**[AGREE] R2-Q4: Entity construction 阈值 θ 不一致**
同意。SciERC 用 post-hoc θ=2/N 而其他数据集用 CV 选择阈值，这是方法论不一致。Post-hoc 阈值选择有 data snooping 风险——如果 θ=2/N 恰好在 SciERC test set 上最优，则 +1.57 pp 的改善可能被夸大。所有数据集应统一使用 CV 选择阈值。这与 R2-W3（test set probe）和我的 R1 Q5-Q6（supervised combination 数据泄露）构成同一类方法论关切。

---

### Missing References

**[AGREE]** R2 提出的四类缺失引用我全部同意：
1. **Wan et al. (2024) — NER/IE LLM survey**：Related Work 应引用最新的综合 survey 以展示领域覆盖。
2. **Xie et al. (2023) — self-evaluation beam search**：与本文的 LP-based selection 直接相关，是 self-evaluation 用于 generation 质量的先例。
3. **Sun et al. (2023) — LLM calibration for text classification**：补强 calibration 相关文献。我在 R1 中也独立建议补充 Kadavath et al. (2022) "Language Models (Mostly) Know What They Know"。
4. **Ensemble-based IE methods**：同意。NER 领域有大量 ensemble 和 committee-based 方法（Nguyen et al., NAACL 2019 等），Related Work 应讨论这些方法与 self-consistency 的关系。

---

### Minor Issues

**[AGREE] R2-Minor-1**: "a alignment-based" → "an alignment-based"，冠词错误应修正。
**[AGREE] R2-Minor-2**: Abstract 最后一句过长，同意拆分以提高可读性。
**[AGREE] R2-Minor-3**: Figure 2 caption 应指明具体哪条线对应哪个信号，当前描述可能不够自包含。
**[AGREE] R2-Minor-4**: \citep 和 \cite 混用是格式不一致，应统一。ACL 模板建议所有括号引用用 \citep，行内引用用 \citet。

---

### 与 R1 审稿的交叉确认

两位 Reviewer 独立发现的共同问题：
1. **超页限**（R1-N1 = R2-N1）：一致认为是 critical
2. **标题/framing 与内容矛盾**（R1-N3 ≈ R2-N3）：一致认为需修正
3. **SciERC 统计功效/稳定性**（R1-W3 ≈ R2-W4）：R2 补充了"仅 1 seed"的具体信息，加强了 R1 的 power 担忧
4. **Entity construction 阈值 data snooping 风险**（R1 Q6 ≈ R2-Q4 ≈ R2-W3）：三处独立关切指向同一方法论问题

R2 提出而 R1 未涉及的有价值新问题：
- N2（理论深度不足）：我部分同意，建议降为 warning 并增加简化分析框架
- W2（与 Yao et al. 2026 区分）：需进一步信息
- Q2（Few-NERD under-training 假说）：有洞察力，值得追查

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2247 · 2026-05-19T03:46:44.883392+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 审稿意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 172

## Round 172

8 recorded events


### User

_source line 2248 · 2026-05-19T03:46:46.044728+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见逐条回应

---

## Must-Fix 问题

**[AGREE] R1-N1: 正文超页（约 9.5–10 页 vs 8 页限制）**
同意。我在独立审稿中将此列为最高优先级问题（我的 N1）。PDF 第 10 页右栏仍包含 Section 6 Conclusion 正文。这是 desk reject 级别违规，需大幅压缩。

R1 建议将 Discussion 细节移至附录、正文仅保留核心结论，我认为可行。补充建议：§4.5 Robustness 中 scale ablation / LoRA-rank ablation / supervised combination 的细节也适合移入附录，每项在正文仅保留一句结论。§4.6 Hidden state probe 的 setup 细节（mean-pooled hidden state, d=4096, MLP dim=256）同理。

---

**[REBUT] R1-N2: 实体匹配标准未精确定义**
R1 称 EVC 和 SJ 的"匹配"含义未定义，但 §3.2 中实际上给出了完整定义：

- **VC (§3.2 line 44)**: 明确使用 "unique (text, type) tuples"，即精确文本 + 精确类型。freq(e) = |{i : e ∈ yᵢ}| / N，其中 e 是 (text, type) tuple。匹配标准 = 完全一致。
- **SJ (§3.2 line 35)**: 明确说明 "group extractions by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU)"。这回答了 R1 的三个子问题：(a) 按类型分组后匹配，不要求精确文本；(b) span 边界通过 token-level IoU 度量，不要求完全一致；(c) 允许部分重叠，IoU 连续度量重叠程度。
- **FK (§3.2 line 26)**: "items are unique (text, type) tuples"，与 VC 相同的精确匹配。论文还在 line 32 明确说 "Unlike structural signals, FK relies on exact string matching"，暗示 SJ 不依赖精确匹配。
- **EM (§3.2 line 20-22)**: 定义为 "proportion of samples producing the most common output"，即整个输出的精确匹配。

定义确实分散在各 signal 的段落中，但并非缺失。不过，我同意论文可以在一处统一对比各 signal 的匹配标准（如一个小表格），提升可读性。R1 建议"消融不同匹配严格度"有参考价值，但考虑到正文已超页，这更适合作为 future work 而非 must-fix。

---

**[PARTIALLY AGREE] R1-N3: CoNLL 循环论证 + 标题矛盾**

关于 **标题矛盾**：**同意**。我在独立审稿中将此列为 N3（critical），理由完全一致：标题暗示纯 negative result，但 §4.7 entity-level construction 给出了显著 positive result。叙事主线需要调整。

关于 **CoNLL 循环论证**：**部分反驳**。R1 称 "CoNLL degeneracy ≥65%，'信号无法改善选择'近乎同义反复"。但论文明确将 CoNLL 定位为 "ceiling-effect control where limited oracle headroom constrains selection gains"（§4.1 line 11），而非作为 gap 的核心证据。核心诊断建立在 SciERC（17.8% degeneracy, 13 pp headroom）和 Few-NERD（13.8% degeneracy, 12.4 pp headroom）上，这两个数据集有充足的 non-degenerate headroom 可供信号利用，但信号仍然失败或仅提供微弱改善。CoNLL 在论文叙事中的角色是补全难度梯度的一端，而非核心 claim 的支柱。

不过，R1 的批评有一个有效延伸：论文标题 "Why Confidence Signals **Fail**" 的普遍性措辞确实让 CoNLL 上的 "failure" 显得像循环论证。如果标题限定为 specific settings，这个问题会缓解。

---

## Should-Fix 问题

**[REBUT] R1-W1: 关键鲁棒性证据（T=1.0 低 degeneracy 下 selection 仍失败）埋在附录**
R1 称此证据仅在附录中，但实际上 Discussion §5 "Regime boundaries" 段落（main text）明确写道："at T=1.2, degeneracy drops to 14.9% yet LP does not improve because alignment remains weak (ρ=0.225 vs. Few-NERD ~0.5–0.7; Table 35)"。核心结论在正文中，仅支持性数据表（Table 35）在附录。这是标准的 main-text-conclusion + appendix-evidence 结构。

但我注意到 R1 说的是 "T=1.0 低 degeneracy 下 selection 仍失败"，而论文的温度消融是 T=1.2。如果 R1 指的是 Few-NERD（T=1.0, degeneracy 13.8%）上 structural signals 仍然 degrade selection，那这个结论确实在 §4.4 (Table 3) 主文中。

---

**[PARTIALLY AGREE] R1-W2: 仅测试 LoRA 微调，但标题做出不限定的 claim**
R1 建议限定为 "LoRA fine-tuned LLMs" 或增加 ICL baseline。

标题 "LLM-Based Named Entity Recognition" 确实涵盖面较广。不过，Discussion §5 最后一段 "When would consistency-based selection work?" 明确讨论了 ICL 设置可能恢复 selection headroom 的理由（更大 diversity、更低 degeneracy），且 Limitations 也承认 "whether the gap holds for ... closed-source APIs is untested"。

我认为在标题中加入 "fine-tuned" 是合理的建议（"... Fine-Tuned LLM-Based NER"），但标记为 critical 过重。论文的核心贡献（QE-selection gap 的诊断框架和 entity-level construction）不依赖于 fine-tuning 特定假设。

---

**[AGREE] R1-W3: SciERC n=529 统计功效可能不足，未报告 TOST post-hoc power**
同意。我在独立审稿中将 SciERC seed sensitivity 列为 W4。论文在 §4.3 footnote 中报告了 MDE ≈ 1.5 pp at 80% power，但 Appendix E（Table 9）的 TOST 分析未报告 post-hoc power。在 SciERC NER 上，δ=±2 pp 时 FK 和 EM 不通过 TOST，但 R1 正确指出我们不知道在这个 n 下 TOST 是否有足够 power 来拒绝等价假设。

补充：Few-NERD（n=32,565）提供了远超 SciERC 的统计 power（MDE ≈ 0.22 pp），论文在 §4.3 中也明确指出 "Few-NERD provides the definitive test"。核心结论不依赖 SciERC 的等价性检验。

---

**[PARTIALLY AGREE] R1-W4: 缺少 instance-level error analysis**
论文有一些 instance-level 分析（Appendix 中的 conditional decomposition、per-entity-type analysis、VC quartile analysis），但确实没有提供一个系统的 "信号在哪些具体 instance 上失败及为什么" 的分析。这对理解 gap 的来源有价值。

不过，§4.6 Hidden state probe 的结果（MLP ρ=0.388 vs LP 0.283，但 selection gap closure -5.1%）从另一个角度回答了这个问题：即使拥有更丰富的 instance-level 信息，selection 仍然失败，说明瓶颈不在于识别哪些 instance 失败，而在于 inter-sample F1 差异太小（"diminishing marginal returns"）。

---

**[REBUT] R1-W5: "Soft Jaccard" 命名与标准 Jaccard 混淆**
"Soft Jaccard" 的命名是恰当的：它保留了 Jaccard 的集合交集/并集结构（分子=匹配相似度之和，分母=最大集合大小），但将 exact match 替换为 token-level IoU（continuous similarity）。"Soft" 恰好传达了这个关键区别。这是计算语言学中常见的命名模式（如 "soft attention" vs "hard attention", "soft alignment" vs "hard alignment"）。论文在 §3.2 中给出了完整公式（Eq. 4），读者不会混淆。

---

## Questions

**[REBUT] R1-Q1: EVC 和 SJ 中实体"匹配"的具体标准**
见上方 N2 回应。VC 使用 exact (text, type) tuple match；SJ 使用 type-grouped Hungarian matching with token-level IoU。两个定义在 §3.2 中是完整的。

**[REBUT] R1-Q2: TOST 等价边界 δ 的具体值和选择依据**
Appendix E（Table 9）给出了三组 δ：±2, ±3, ±5 pp，并将每个 δ 对照 oracle headroom 做了比例解释（δ=5 pp ≈ 28–38% of headroom）。论文还承认了这个对照的循环性（Appendix E line 374），并补充了三个外部锚定 margin：(1) δ_SEM = bootstrapped SE of single-sample F1 (0.43–1.33 pp)；(2) δ_practical = 0.5 pp (Ratinov & Roth 2009 NER 可忽略差异阈值)；(3) δ_literature = 1.0 pp (Berg-Kirkpatrick et al. 2012 NLP 显著性阈值)。R1 的问题在论文中有详尽回答。

**[REBUT] R1-Q3: Entity-level voting SciERC +1.67 pp vs CoNLL -0.39 pp 不对称**
论文在 §4.7 line 256 明确说明："CoNLL shows no significant gain (−0.39 pp), consistent with ceiling-regime degeneracy." 机制是 recall-driven：construction 通过聚合低频 correct entities 提升 recall。在 CoNLL（greedy F1 ≈ 0.91）上，greedy 已捕获大部分 entities，额外聚合反而引入 false positives。§5 "Capability-diversity tension" 对此有系统性讨论。

**[AGREE] R1-Q4: Greedy (T=0) 与单个 T=0.6 样本的 F1 比较**
论文未提供这个比较，但它对理解 temperature 对 single-sample quality 的影响有参考价值。

**[REBUT] R1-Q5: Supervised combination 的 5-fold CV 是否存在数据泄露**
§4.5 line 183 描述 "5-fold CV, 3-seed mean"。5-fold CV 在 instance 层面切分，每个 fold 的 test instances 不出现在该 fold 的 train set 中。由于信号是 per-instance 计算的（不依赖其他 instances），fold 之间不存在 information leakage。DeBERTa verifier（line 185-186）也使用 5-fold CV。这是标准的 CV 设计。

**[REBUT] R1-Q6: LP 计算是否排除了 thinking tokens**
Appendix I（§ Thinking Token Impact Analysis）提供了三部分论证：(1) LP shift 仅 0.001 nats/token（占 median LP range 的 2.68%），影响 <1.5% instances 的 selection；(2) 所有 N 个 samples 共享相同的 thinking token offset，within-instance rankings 不变；(3) CoNLL control group（无 thinking tokens）显示更高而非更低的 tied fraction（86.8% vs SciERC 60.3%），直接否定 thinking token 假设。

---

## Missing References

**[REBUT] R1-Missing-1: Kadavath et al. (2022) "Language Models Know What They Know"**
该论文已被引用。References.bib 中有完整条目 `kadavath2022language`，在 Related Work §2 line 19（"P(True) [Kadavath et al., 2022]"）和 Limitations line 13 均有 cite。R1 可能遗漏了。

**[PARTIALLY AGREE] R1-Missing-2: 结构化预测 uncertainty estimation 工作**
论文在 Related Work §2 line 14 引用了 Culotta & McCallum (2004), Mejer & Crammer (2010), Fomicheva et al. (2020) 作为 "confidence for structured prediction" 的前序工作。覆盖面可能不够全面，但基础覆盖存在。

**[AGREE] R1-Missing-3: 9 条 bib entry 需复核年份/venue**
引用验证工具显示 4 条 not_found（hobelsberger2025, lightman2024, venktesh2025, aggarwal2023——均为真实论文，OpenAlex 覆盖不完整）和 5 条 mismatch（多为 first_author 格式差异或 year 偏移，如 chen2025twofailures bib year=2025 vs API year=2023）。建议作者核查这些条目的 venue 和 year 是否反映最终发表版而非 arXiv 版。

---

## Minor Issues

**[REBUT] R1-Minor-1: "Confidence signal" 应改为 "quality signal"**
"Confidence signal" 在论文语境中是准确的：5 个信号中 4 个基于 consistency/agreement（即 confidence 的操作化定义），1 个是 log-probability（模型 confidence 的直接度量）。"Quality signal" 的语义更广，可能让读者误以为包含 learned verifiers 或 reward models，而这正是论文认为缺失的。标题中 "confidence signals" 与 Related Work 中的 "confidence estimation" 文献保持术语一致。

**[AGREE] R1-Minor-2: Figure 3 打印尺寸下标签可能难辨**
需要检查渲染后的 PDF，但 scatter plot 在单栏宽度下确实容易出现标签重叠。

**[AGREE] R1-Minor-3: "N-scaling" vs "sample size scaling" 术语不统一**
同意。论文在 §4.5 用 "sublinear N-scaling gains"，在 Appendix 中用 "Sample size scaling" 和 "Diminishing returns of N-scaling"，应统一。


---

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

要点总结：
- **14 条中 11 条 AGREE**（含 3 条 partial agree），**1 条 PARTIALLY REBUT**（W5 entity-level construction 新颖性——论文定位为分析发现而非方法贡献）
- 两位 Reviewer 独立发现 4 个共同问题：超页限、标题矛盾、SciERC 统计稳定性、阈值 data snooping
- R2-N2（理论深度）我建议从 critical 降为 warning，增加简化分析框架即可
- R2-Q2（Few-NERD under-training 假说）是有价值的新视角，与 alignment compression 诊断一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2249 · 2026-05-19T03:47:24.490295+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "450",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "450",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2250 · 2026-05-19T03:47:24.540973+00:00_

450	    first_raised_round: 21
451	    last_seen_round: 21
452	    action_items:
453	      - round: 21
454	        action: "改写 experiments:183, discussion:20, introduction:18"
455	        assigned_to: paper_agent
456	        status: done
457	    resolution: "3 处改写完成。Reviewer PASS。"
458	    resolution_round: 21
459	
460	  - id: "R21-MR1"
461	    summary: "缺失引用: Farquhar et al., Chen et al. pass@k"
462	    category: format
463	    severity: warning
464	    status: resolved
465	    first_raised_round: 21
466	    last_seen_round: 21
467	    action_items:
468	      - round: 21
469	        action: "补 3 类引用"
470	        assigned_to: paper_agent
471	        status: done
472	    resolution: "Farquhar et al. + Chen et al. pass@k 已补入 Related Work。第三类未指定，视为完成。"
473	    resolution_round: 21
474	
475	  - id: "R21-Q3"
476	    summary: "Per-entity-type ρ=-0.881 effective df 问题"
477	    category: experiment
478	    severity: info
479	    status: resolved
480	    first_raised_round: 21
481	    last_seen_round: 21
482	    action_items:
483	      - round: 21
484	        action: "计算 effective df=4 时 p-value"
485	        assigned_to: agent
486	        status: done
487	      - round: 21
488	        action: "Appendix 加 conservative df=4 caveat (p=0.033)"
489	        assigned_to: paper_agent
490	        status: done
491	    resolution: "Appendix L1229 已有 'Under a conservative df=4 adjustment, p=0.033'。"
492	    resolution_round: 21

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2251 · 2026-05-19T03:49:38.514498+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n  # ===== 历史 resolved issues（保留记录）=====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance: LP selection viable when ρ≈0.3, otherwise greedy + QE selective prediction。D154 within/cross 区分增强诊断价值。\"\n    resolution_round: 21\n\n  - id: \"R2-W3\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-6 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison: 3-epoch SciERC ρ=0.319 vs Few-NERD ~0.5, 确认 LP alignment 驱动跨数据集差异。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'（footnote + L91），SciERC 为 diagnosis site，MDE 已注明。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix (L1388)。ε sweep (L560-588) + LOO τ sensitivity (L1396-1398) 均已呈现。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化为 'first systematic empirical characterization of when and why LP-based selection succeeds or fails for structured prediction'。D154 within/cross 区分 + ρ=0.052 negative result 增强新颖性。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文 11 处统一使用 0.205，0.215 从未出现。D145 决策保持 mean_LP 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。Reviewer PASS: 信息完整性通过，degeneracy 定义移入 Method §3.3。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。Reviewer PASS。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认 exp_025/exp_027 不存在于 .tex 文件中。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"正文无 'capability trap' 残留，已统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。Reviewer PASS。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Farquhar et al. + Chen et al. pass@k 已补入 Related Work。第三类未指定，视为完成。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix L1229 已有 'Under a conservative df=4 adjustment, p=0.033'。\"\n    resolution_round: 21\n\n  # ===== Round 22 新增 issues =====\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页 (约 10 页 vs 8 页限制)\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R21-C1 曾 resolved，但当前版本再次超页。两位 Reviewer 独立确认。Discussion §5 + §4.5/§4.6 细节是主因。Desk reject 风险。\"\n    action_items:\n      - round: 22\n        action: \"Discussion §5 压缩至 ~0.5 页（仅保留核心诊断结论）；§4.5 Robustness 和 §4.6 Hidden state probe 细节移入 appendix；Figure 1+2 考虑合并或缩小\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result，与 §4.7 entity-level construction 正面结果矛盾\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"标题 'Why Confidence Signals Fail to Improve' vs §4.7 entity-level construction +1.67 pp (p=0.004)。叙事主线不统一。两位 Reviewer 独立确认。\"\n    action_items:\n      - round: 22\n        action: \"修改标题反映完整故事弧（如 'The Correlation-Selection Gap in LLM-Based NER' 或类似）；确保 Abstract/Introduction/Conclusion 主线统一\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度，停留在实证描述层面\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R2 列为 critical，R1 建议降为 warning 并增加简化分析框架。共识：增加一个简化的 expected gain bound（如 (1-d) * oracle_gap）即可，无需完整理论证明。\"\n    action_items:\n      - round: 22\n        action: \"在 §4.3 或 §5 增加简化分析框架：degeneracy 率 d 和 alignment ρ 如何约束 expected selection gain\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"LP 在 Abstract line 5 首次出现未定义；AUROC 在 line 4 未展开。ACL 规范要求 Abstract 内缩写自包含定义。\"\n    action_items:\n      - round: 22\n        action: \"Abstract 中展开 LP → 'log-probability (LP)' 和 AUROC → 'area under the ROC curve (AUROC)'\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe，存在 information leakage\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"§4.7 line 266 承认 'probe instances are drawn from the test set'。仅 3 个数据集验证。与 entity construction 阈值选择（SciERC θ=2/N post-hoc）构成同一类方法论关切。\"\n    action_items:\n      - round: 22\n        action: \"用 validation split 重做 gating 实验，或弱化 claim 为 preliminary proof-of-concept；统一所有数据集的阈值选择为 CV\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-W4\"\n    summary: \"SciERC 主实验 seed sensitivity 高 (σ=0.48 pp)，1 primary seed 不够稳健\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"SciERC LP selection 3-seed mean +0.04±0.48 pp（Limitations line 14），但 main text 主要引用 1-seed 结果。n=529 已偏小，1 seed 加剧不确定性。\"\n    action_items:\n      - round: 22\n        action: \"SciERC 主文中更显著地报告 multi-seed 结果和 seed sensitivity，而非仅在 Limitations 提到\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致 (SciERC post-hoc θ=2/N vs 其他 CV)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"§4.7: SciERC 用 post-hoc θ=2/N，Few-NERD/CoNLL 用 5-fold CV。Post-hoc 阈值有 data snooping 风险，可能高估 SciERC 的 construction gain。\"\n    action_items:\n      - round: 22\n        action: \"SciERC 也统一用 CV 选择阈值，或明确标注 θ=2/N 为 post-hoc 探索性选择\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Contribution 3 (Introduction line 40) 和 Abstract line 7 使用 'the correct'。仅在 NER 上验证，CoNLL 上不 work。\"\n    action_items:\n      - round: 22\n        action: \"改为 'a more effective' 或 'a natural' self-consistency analogy\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但标题和 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。LP compression 可能是 LoRA 特有现象。Discussion §5 讨论了 ICL 可能不同，但标题/Abstract 未限定。\"\n    action_items:\n      - round: 22\n        action: \"Abstract/标题中限定为 fine-tuned LLMs，或增加 ICL baseline 以验证结论迁移性\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中，缺乏统一展示\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R1 列为 critical (定义缺失)，R2 提供证据反驳 (定义存在但分散)。交叉回应后降为 info：定义完整但建议统一展示。\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"conclusion.tex line 5: 'a alignment-based' → 'an alignment-based'。\\\\citep 和 \\\\cite 混用需统一。\"\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023, Wan et al. 2024\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Related Work 缺少 ensemble-based NER methods 讨论（与 entity-level construction 直接相关）。Xie et al. 2023 self-evaluation beam search 和 Wan et al. 2024 IE survey 未引用。9 条 bib entry 年份/venue 需复核。\"\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"单栏宽度下标签可能重叠。建议增大字体或简化数据点标注。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n  # ===== 历史 resolved issues（保留记录）=====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance: LP selection viable when ρ≈0.3, otherwise greedy + QE selective prediction。D154 within/cross 区分增强诊断价值。\"\n    resolution_round: 21\n\n  - id: \"R2-W3\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-6 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison: 3-epoch SciERC ρ=0.319 vs Few-NERD ~0.5, 确认 LP alignment 驱动跨数据集差异。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'（footnote + L91），SciERC 为 diagnosis site，MDE 已注明。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix (L1388)。ε sweep (L560-588) + LOO τ sensitivity (L1396-1398) 均已呈现。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化为 'first systematic empirical characterization of when and why LP-based selection succeeds or fails for structured prediction'。D154 within/cross 区分 + ρ=0.052 negative result 增强新颖性。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文 11 处统一使用 0.205，0.215 从未出现。D145 决策保持 mean_LP 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。Reviewer PASS: 信息完整性通过，degeneracy 定义移入 Method §3.3。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。Reviewer PASS。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认 exp_025/exp_027 不存在于 .tex 文件中。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"正文无 'capability trap' 残留，已统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。Reviewer PASS。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Farquhar et al. + Chen et al. pass@k 已补入 Related Work。第三类未指定，视为完成。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix L1229 已有 'Under a conservative df=4 adjustment, p=0.033'。\"\n    resolution_round: 21\n\n  # ===== Round 22 新增 issues =====\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页 (约 10 页 vs 8 页限制)\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R21-C1 曾 resolved，但当前版本再次超页。两位 Reviewer 独立确认。Discussion §5 + §4.5/§4.6 细节是主因。Desk reject 风险。\"\n    action_items:\n      - round: 22\n        action: \"Discussion §5 压缩至 ~0.5 页（仅保留核心诊断结论）；§4.5 Robustness 和 §4.6 Hidden state probe 细节移入 appendix；Figure 1+2 考虑合并或缩小\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result，与 §4.7 entity-level construction 正面结果矛盾\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"标题 'Why Confidence Signals Fail to Improve' vs §4.7 entity-level construction +1.67 pp (p=0.004)。叙事主线不统一。两位 Reviewer 独立确认。\"\n    action_items:\n      - round: 22\n        action: \"修改标题反映完整故事弧（如 'The Correlation-Selection Gap in LLM-Based NER' 或类似）；确保 Abstract/Introduction/Conclusion 主线统一\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度，停留在实证描述层面\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R2 列为 critical，R1 建议降为 warning 并增加简化分析框架。共识：增加一个简化的 expected gain bound（如 (1-d) * oracle_gap）即可，无需完整理论证明。\"\n    action_items:\n      - round: 22\n        action: \"在 §4.3 或 §5 增加简化分析框架：degeneracy 率 d 和 alignment ρ 如何约束 expected selection gain\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"LP 在 Abstract line 5 首次出现未定义；AUROC 在 line 4 未展开。ACL 规范要求 Abstract 内缩写自包含定义。\"\n    action_items:\n      - round: 22\n        action: \"Abstract 中展开 LP → 'log-probability (LP)' 和 AUROC → 'area under the ROC curve (AUROC)'\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe，存在 information leakage\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"§4.7 line 266 承认 'probe instances are drawn from the test set'。仅 3 个数据集验证。与 entity construction 阈值选择（SciERC θ=2/N post-hoc）构成同一类方法论关切。\"\n    action_items:\n      - round: 22\n        action: \"用 validation split 重做 gating 实验，或弱化 claim 为 preliminary proof-of-concept；统一所有数据集的阈值选择为 CV\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-W4\"\n    summary: \"SciERC 主实验 seed sensitivity 高 (σ=0.48 pp)，1 primary seed 不够稳健\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"SciERC LP selection 3-seed mean +0.04±0.48 pp（Limitations line 14），但 main text 主要引用 1-seed 结果。n=529 已偏小，1 seed 加剧不确定性。\"\n    action_items:\n      - round: 22\n        action: \"SciERC 主文中更显著地报告 multi-seed 结果和 seed sensitivity，而非仅在 Limitations 提到\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致 (SciERC post-hoc θ=2/N vs 其他 CV)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"§4.7: SciERC 用 post-hoc θ=2/N，Few-NERD/CoNLL 用 5-fold CV。Post-hoc 阈值有 data snooping 风险，可能高估 SciERC 的 construction gain。\"\n    action_items:\n      - round: 22\n        action: \"SciERC 也统一用 CV 选择阈值，或明确标注 θ=2/N 为 post-hoc 探索性选择\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Contribution 3 (Introduction line 40) 和 Abstract line 7 使用 'the correct'。仅在 NER 上验证，CoNLL 上不 work。\"\n    action_items:\n      - round: 22\n        action: \"改为 'a more effective' 或 'a natural' self-consistency analogy\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但标题和 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。LP compression 可能是 LoRA 特有现象。Discussion §5 讨论了 ICL 可能不同，但标题/Abstract 未限定。\"\n    action_items:\n      - round: 22\n        action: \"Abstract/标题中限定为 fine-tuned LLMs，或增加 ICL baseline 以验证结论迁移性\"\n        assigned_to: paper_agent\n        status: pending\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中，缺乏统一展示\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R1 列为 critical (定义缺失)，R2 提供证据反驳 (定义存在但分散)。交叉回应后降为 info：定义完整但建议统一展示。\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"conclusion.tex line 5: 'a alignment-based' → 'an alignment-based'。\\\\citep 和 \\\\cite 混用需统一。\"\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023, Wan et al. 2024\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Related Work 缺少 ensemble-based NER methods 讨论（与 entity-level construction 直接相关）。Xie et al. 2023 self-evaluation beam search 和 Wan et al. 2024 IE survey 未引用。9 条 bib entry 年份/venue 需复核。\"\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"单栏宽度下标签可能重叠。建议增大字体或简化数据点标注。\""
  }
}
```

</details>

---


### Tool result

_source line 2252 · 2026-05-19T03:49:38.617382+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 16211}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2253 · 2026-05-19T03:51:49.907499+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "struct_self_consist_ie",
  "report": "# 审稿报告 — Round 22（Fresh Review）\n\n**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Improve LLM-Based Named Entity Recognition\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**Deadline**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+叙事完整性+写作质量）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）\n\n---\n\n## Summary\n\n本文系统评估 5 种 confidence signal（4 种 consistency-based + log-probability）在 LLM NER 上的质量估计（QE）和样本选择能力。核心发现为\"correlation-selection gap\"：所有信号可靠预测输出质量（ρ 高达 0.45, AUROC 高达 0.82），但在 best-of-N selection 上无法持续超越 greedy decoding。论文将此归因于 instance degeneracy 和 LP-quality alignment weakness，并提出 entity-level construction 作为替代方案（SciERC +1.67 pp, Few-NERD +0.88 pp）。实验覆盖 4 个 NER benchmark、2 个模型家族、4B ablation、22 页附录，统计分析极度充分。\n\n---\n\n## Strengths\n\n**S1. 实验设计和统计严谨性远超平均水准。** 4 数据集难度梯度、2 模型家族 + 4B ablation、3-seed stability、bootstrap CI、TOST equivalence testing、power analysis（MDE）、Bonferroni correction。22 页附录涵盖温度消融、N-scaling、epoch confound、free-form 格式、hidden state probe、supervised combination 等。这种严谨程度在 NLP 实证论文中罕见。[R1, R2 共识]\n\n**S2. QE-selection 分离的概念框架有实际指导价值。** 明确区分 quality estimation 和 sample selection 两个任务（§3.1），并实证证明 QE 强不等于 selection 强。Instance-level signal 无法 rank per-sample candidates 的 \"by construction\" 论证清晰。对部署决策有直接参考意义。[R1, R2 共识]\n\n**S3. 诊断分析链条完整。** Instance degeneracy → LP compression → capability-diversity tension 的诊断逻辑自洽。温度消融（Table 35）提供了更干净的因果测试。Hidden state probe（§4.6）确认信息瓶颈不在 feature engineering 层面，而在 selection 的 diminishing marginal returns。[R2-S3, R1 同意]\n\n**S4. Entity-level construction 提供可操作的正面结果。** LP-weighted entity aggregation 在 SciERC (+1.67 pp, p=0.004) 和 Few-NERD (+0.88 pp, p<0.001) 上显著优于 greedy，提供了 selective prediction 之外的实用方案。Alignment-based gating protocol 虽为初步验证，但方向正确。[R2-S4, R1 同意]\n\n**S5. 写作质量通过 AI 风格硬检查。** 全文无 em-dash (—) 或解释性 en-dash (–)；无 AI 黑名单词汇；无 -ing 短语结尾模式；无过度分段。\\textendash 仅用于数值范围，用法正确。[R2-S5]\n\n**S6. Thinking token confound 的诚实处理。** 主动记录 Qwen3 SciERC checkpoint 的 thinking token 问题，并提供三部分反驳论证（LP shift magnitude, constant prefix cancellation, CoNLL control）。[R1-S5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**R22-N1 [critical] 正文再次超页约 2 页（约 10 页 vs 8 页限制）**\n- Section 6 Conclusion 结束于 PDF 第 10 页右栏，Limitations 从同页底部开始。ACL ARR 规定正文 ≤ 8 页，当前超出约 1.5–2 页。\n- **主因**：Discussion §5 单独占约 2 页；§4.5 Robustness 和 §4.6 Hidden state probe 包含过多细节。\n- **注意**：R21-C1 曾 resolved（\"Sections 1-6 + Limitations 在 page 8 结束\"），但当前版本再次超页，说明后续修改引入了新内容。\n- **风险**：Desk reject。ARR 政策明确拒绝超页论文。\n- **建议**：Discussion §5 压缩至 ~0.5 页（仅保留核心诊断结论）；§4.5/§4.6 细节移入 appendix；Figure 1+2 考虑合并或缩小。\n- [R1, R2 独立发现，交叉一致]\n\n**R22-N2 [critical] 标题与 positive construction result 的叙事矛盾**\n- 标题 \"Why Confidence Signals **Fail** to Improve LLM-Based NER\" 暗示纯 negative result。\n- §4.7 entity-level construction 给出显著 positive result：SciERC +1.67 pp (p=0.004), Few-NERD +0.88 pp (p<0.001)。\n- Conclusion 也以 construction 和 gating protocol 作为积极贡献结尾。\n- 标题与正文之间的矛盾会让审稿人质疑核心贡献定位。\n- **建议**：标题应反映完整故事弧。如 \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based NER\" 或 \"From Selection to Construction: ...\"。\n- [R1, R2 独立发现，交叉一致]\n\n### Should-Fix（影响评分但不一票否决）\n\n**R22-W1 [warning] correlation-selection gap 概念缺乏理论支撑**\n- 本质上是实证观察而非理论贡献。未提供形式化分析解释为什么 QE ρ 高不等于 selection 有效。\n- R2 列为 critical，R1 建议降为 warning 并增加简化分析框架。交叉后共识为 warning。\n- **建议**：增加简化的 expected gain bound（如在 degeneracy 率 d 下，expected selection gain ≤ (1-d) × oracle_gap），无需完整理论证明。\n\n**R22-W2 [warning] Abstract 中 LP 和 AUROC 缩写未展开**\n- LP 在 Abstract line 5 首次出现未定义；AUROC 在 line 4 未展开。\n- ACL 规范要求 Abstract 内缩写自包含定义。\n- **修复**：\"log-probability (LP)\", \"area under the ROC curve (AUROC)\"。\n- [R2 提出，R1 交叉同意]\n\n**R22-W3 [warning] LP-alignment gating protocol 使用 test set 做 probe**\n- §4.7 line 266 承认 \"probe instances are drawn from the test set for simplicity\"。\n- 仅 3 个数据集验证 gating 效果。\n- Entity construction 阈值 θ 在 SciERC 上也为 post-hoc (θ=2/N) vs 其他 CV。\n- 构成同一类方法论关切：评估与选择之间的 information leakage。\n- **建议**：用 validation split 重做，或弱化 claim 为 preliminary proof-of-concept；统一阈值选择为 CV。\n- [R2-W3, R1 交叉同意; 与 R22-W5 相关]\n\n**R22-W4 [warning] SciERC 主实验 seed sensitivity 高，统计推断力受限**\n- SciERC LP selection 3-seed mean: +0.04±0.48 pp（Limitations line 14），但 main text 主要引用 1-seed 结果。\n- n=529, MDE ≈ 1.5 pp at 80% power。TOST 未报告 post-hoc power。\n- 核心结论不依赖 SciERC 等价性检验（Few-NERD n=32,565 提供 definitive test），但 SciERC 作为 primary test bed 的 positioning 与其统计功效不匹配。\n- **建议**：主文更显著地报告 multi-seed 结果和 seed sensitivity。\n- [R1-W3, R2-W4 交叉一致]\n\n**R22-W5 [warning] Entity construction 阈值 θ 跨数据集不一致**\n- SciERC 用 post-hoc θ=2/N，Few-NERD/CoNLL 用 5-fold CV。\n- Post-hoc 阈值有 data snooping 风险，可能高估 SciERC 的 construction gain。\n- **建议**：统一为 CV 或明确标注为 exploratory。\n- [R2-Q4, R1 交叉同意]\n\n**R22-W6 [warning] \"the correct self-consistency analogy\" 措辞过于绝对**\n- Contribution 3 和 Abstract 使用 \"the correct\"。仅在 NER 上验证，CoNLL 上不 work (-0.39 pp)。\n- **建议**：改为 \"a more effective\" 或 \"a natural\"。\n- [R2-W6, R1 交叉同意]\n\n**R22-W7 [warning] 仅测试 LoRA 微调但 claim 范围不限定**\n- 所有实验均为 LoRA fine-tuned models。LP compression 可能是 LoRA 特有现象。\n- Discussion §5 讨论了 ICL 可能不同，Limitations 承认未测试，但标题/Abstract 未限定。\n- **建议**：标题或 Abstract 中限定为 fine-tuned LLMs。\n- [R1-W2, R2 交叉部分同意]\n\n**R22-MR1 [warning] 缺失引用**\n- Related Work 缺少 ensemble-based NER methods 讨论（与 entity-level construction 直接相关）。\n- Xie et al. (2023) self-evaluation beam search、Wan et al. (2024) IE survey 未引用。\n- 9 条 bib entry 年份/venue 需复核（hobelsberger2025, lightman2024 等）。\n- [R1, R2 分别提出]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题双方独立发现并在交叉后确认一致：\n\n1. **超页限** — 正文约 10 页 vs 8 页限制，desk reject 风险。[R1-N1 = R2-N1]\n2. **标题叙事矛盾** — \"Fail\" vs entity-level construction positive result。[R1-N3 ≈ R2-N3]\n3. **SciERC 统计功效/seed sensitivity** — n=529, 1 primary seed, σ=0.48 pp。[R1-W3 ≈ R2-W4]\n4. **Gating/threshold data snooping** — test set probe + post-hoc θ。[R1 Q5-Q6 ≈ R2-W3 ≈ R2-Q4]\n5. **实验设计和统计严谨性是核心优势** — 22 页附录、TOST、bootstrap、power analysis。[S1]\n6. **QE-selection 分离框架有社区价值** — 可操作的概念贡献。[S2]\n7. **定位为 Findings 更合适** — Main Conference 需要更强的正面结果或理论深度。[双方 3.0/5]\n\n---\n\n## Reviewer Divergence [REBUT]\n\n1. **R1-N2 实体匹配标准是否缺失**：R1 列为 critical（定义缺失），R2 反驳称定义完整但分散在 §3.2 各段落中（VC: exact (text, type) tuple; SJ: type-grouped Hungarian matching with token-level IoU; FK: exact string matching; EM: complete output exact match）。R1 未对此反驳进一步回应。**Director 判断**：R2 的证据令人信服，定义确实存在但可读性不佳。降级为 info (R22-I1)，建议增加统一展示表格。\n\n2. **R2-N2 理论深度 critical vs warning**：R2 列为 critical，R1 建议降为 warning（论文定位为 empirical analysis, Findings 接受高质量实证分析）。**Director 判断**：采纳 R1 建议，降为 warning (R22-W1)。增加简化分析框架即可。\n\n3. **R2-W5 Entity-level construction 新颖性**：R2 认为本质是 majority voting，新颖性有限。R1 部分反驳：论文将其定位为分析发现而非方法贡献，新颖性要求应更低。**Director 判断**：R1 的论点合理，但 Abstract 和 Contribution 3 的措辞确实有 overclaim 风险（\"the correct analogy\"），需调整语气。已包含在 R22-W6。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Few-NERD LP selection 成功是否本质上是 under-training 的结果？如果 Few-NERD 模型 under-trained（3 epochs vs 5），LP compression 尚未充分发生，LP selection 的 \"成功\" 可能仅反映模型 calibration 尚未被破坏。Epoch ablation 显示 5-epoch 控制组 LP gains 减半——这是否暗示 LP selection 是 training 不充分的 artifact 而非 dataset 特性？[R2-Q2, R1 交叉同意为有洞察力的假设]\n\n**Q2.** within-instance ρ(LP, F1) 跨数据集能否量化地预测 LP gain？论文宣称 LP-quality alignment 是 primary predictor，但未给出 alignment-gain 的跨数据集相关性数据。如果有 3+ 个数据点的 ρ_within vs Δ_LP 关系，将大幅增强诊断框架的说服力。[R2-Q3]\n\n**Q3.** Greedy (T=0) 与单个 T=1.0 样本的平均 F1 比较如何？如果 T=1.0 单样本 F1 显著低于 greedy，则 selection 面对的是\"从 N 个较弱样本中选最好的 vs 一个强样本\"的比较，这与\"信号无信息量\"是不同的 claim。[R1-Q4]\n\n**Q4.** Oracle selection 在哪些类型的 instance 上成功？按实体类型、句子长度、实体密度分层的 oracle-selected vs signal-selected 对比分析，可提供可操作的改进方向。[R1-W4]\n\n---\n\n## Missing References\n\n1. **Ensemble-based IE methods**（如 multi-model voting for NER）——与 entity-level construction 直接相关，Related Work 应讨论。[R1, R2 共识]\n2. **Xie et al. (2023)** \"Self-Evaluation Guided Beam Search for Reasoning\" (NeurIPS 2023)——另一种 per-sample scoring method。[R2]\n3. **Wan et al. (2024)** Knowledge Extraction in Low-Resource Scenarios survey (ACL 2024 Findings)——NER/IE LLM 综述。[R2]\n4. **9 条 bib entry 需复核年份/venue**：hobelsberger2025, lightman2024, venktesh2025, aggarwal2023 在 OpenAlex 中未找到；feng2025, snell2025, muller2021, park2024, chen2025twofailures 存在轻微不匹配。均可能为索引延迟，但建议核查。[R1]\n\n注：R1 提出的 Kadavath et al. (2022) 已在论文中引用（Related Work §2 line 19, Limitations line 13）。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。\n\n---\n\n## Overall Assessment\n\n**评分：weak reject（Main Conference）/ borderline accept（Findings）**\n**置信度：4/5**\n\n| 维度 | 分数 | 说明 |\n|------|------|------|\n| Soundness | 3.5/5 | 实验方法论扎实，统计严谨，但 gating protocol test-set leak 和 SciERC seed sensitivity 削弱部分结论 |\n| Excitement | 2.5/5 | QE-selection gap 的诊断有启发性但缺理论深度；entity construction 增量偏小；诊断性论文定位 Findings 更合适 |\n| Reproducibility | 4/5 | 超参数、训练配置、seed 协议详尽，承诺 code release。缺总 GPU hours |\n| Overall | 3.0/5 | 实证工作扎实但核心贡献停留在实证描述层面，EMNLP Main 需要更锐利的贡献或更强的正面结果 |\n\n**核心判断**：这是一篇实验极度充分、统计严谨的诊断性论文。QE-selection 分离的概念框架和 entity-level construction 方案对社区有实际价值。但三个因素限制了 Main Conference 竞争力：\n\n1. **格式违规**（超页 ~2 页）是首要障碍，必须在提交前解决。\n2. **叙事不统一**（标题暗示纯 negative，但有显著 positive result）会让审稿人困惑核心定位。\n3. **Excitement gap**：correlation-selection gap 停留在实证描述层面，缺乏理论支撑；entity construction 是已知技术的应用而非方法创新。\n\n**建议路径**：(A) 修复超页和标题后投 Findings（最稳妥）；(B) 增加简化理论框架 + 限定 claim scope 后投 Main Conference（有竞争力但需要更精确的 positioning）。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- LP 和 AUROC 缩写需展开 [R22-W2]\n- \"the correct self-consistency analogy\" → \"a more effective\" [R22-W6]\n- 最后一句过长（~50 words），建议拆分 [R2-Minor-2]\n\n### Introduction\n- 标题暗示纯 negative result，但 Contribution 3 是 positive [R22-N2]\n- Contribution 3 \"correct\" 措辞需弱化 [R22-W6]\n- 与 Yao et al. (2026) 的 3-4 个关键差异应更明确 [R2-W2]\n\n### Method (§3)\n- 实体匹配标准分散在各段落中，建议增加统一对比表格 [R22-I1]\n- \"Soft Jaccard\" 命名与标准 Jaccard 有区别，应更明确说明 [R1-W5, R2 反驳认为命名合理，minor]\n\n### Experiments (§4)\n- §4.5 Robustness 和 §4.6 Hidden state probe 细节建议移入 appendix 以节省页数 [R22-N1]\n- §4.7 gating protocol 应用 validation split 而非 test set [R22-W3]\n- Entity construction θ 应统一为 CV [R22-W5]\n- SciERC multi-seed 结果应在 main text 显著报告 [R22-W4]\n\n### Discussion (§5)\n- 当前约 2 页，是超页主因。建议压缩至 ~0.5 页 [R22-N1]\n- 增加简化的 expected selection gain bound [R22-W1]\n\n### Conclusion (§6)\n- \"a alignment-based\" → \"an alignment-based\" [R22-I2]\n\n### Limitations\n- LoRA 限定应更显著 [R22-W7]\n\n### References\n- 9 条 bib entry 年份/venue 需复核 [R22-MR1]\n- 补充 ensemble-based IE methods 等引用 [R22-MR1]\n\n### Formatting\n- \\citep 和 \\cite 混用需统一 [R22-I2]\n- Figure 3 标签在打印尺寸下可能难辨 [R22-I3]",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "report": "# 审稿报告 — Round 22（Fresh Review）\n\n**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Improve LLM-Based Named Entity Recognition\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**Deadline**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+叙事完整性+写作质量）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）\n\n---\n\n## Summary\n\n本文系统评估 5 种 confidence signal（4 种 consistency-based + log-probability）在 LLM NER 上的质量估计（QE）和样本选择能力。核心发现为\"correlation-selection gap\"：所有信号可靠预测输出质量（ρ 高达 0.45, AUROC 高达 0.82），但在 best-of-N selection 上无法持续超越 greedy decoding。论文将此归因于 instance degeneracy 和 LP-quality alignment weakness，并提出 entity-level construction 作为替代方案（SciERC +1.67 pp, Few-NERD +0.88 pp）。实验覆盖 4 个 NER benchmark、2 个模型家族、4B ablation、22 页附录，统计分析极度充分。\n\n---\n\n## Strengths\n\n**S1. 实验设计和统计严谨性远超平均水准。** 4 数据集难度梯度、2 模型家族 + 4B ablation、3-seed stability、bootstrap CI、TOST equivalence testing、power analysis（MDE）、Bonferroni correction。22 页附录涵盖温度消融、N-scaling、epoch confound、free-form 格式、hidden state probe、supervised combination 等。这种严谨程度在 NLP 实证论文中罕见。[R1, R2 共识]\n\n**S2. QE-selection 分离的概念框架有实际指导价值。** 明确区分 quality estimation 和 sample selection 两个任务（§3.1），并实证证明 QE 强不等于 selection 强。Instance-level signal 无法 rank per-sample candidates 的 \"by construction\" 论证清晰。对部署决策有直接参考意义。[R1, R2 共识]\n\n**S3. 诊断分析链条完整。** Instance degeneracy → LP compression → capability-diversity tension 的诊断逻辑自洽。温度消融（Table 35）提供了更干净的因果测试。Hidden state probe（§4.6）确认信息瓶颈不在 feature engineering 层面，而在 selection 的 diminishing marginal returns。[R2-S3, R1 同意]\n\n**S4. Entity-level construction 提供可操作的正面结果。** LP-weighted entity aggregation 在 SciERC (+1.67 pp, p=0.004) 和 Few-NERD (+0.88 pp, p<0.001) 上显著优于 greedy，提供了 selective prediction 之外的实用方案。Alignment-based gating protocol 虽为初步验证，但方向正确。[R2-S4, R1 同意]\n\n**S5. 写作质量通过 AI 风格硬检查。** 全文无 em-dash (—) 或解释性 en-dash (–)；无 AI 黑名单词汇；无 -ing 短语结尾模式；无过度分段。\\textendash 仅用于数值范围，用法正确。[R2-S5]\n\n**S6. Thinking token confound 的诚实处理。** 主动记录 Qwen3 SciERC checkpoint 的 thinking token 问题，并提供三部分反驳论证（LP shift magnitude, constant prefix cancellation, CoNLL control）。[R1-S5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**R22-N1 [critical] 正文再次超页约 2 页（约 10 页 vs 8 页限制）**\n- Section 6 Conclusion 结束于 PDF 第 10 页右栏，Limitations 从同页底部开始。ACL ARR 规定正文 ≤ 8 页，当前超出约 1.5–2 页。\n- **主因**：Discussion §5 单独占约 2 页；§4.5 Robustness 和 §4.6 Hidden state probe 包含过多细节。\n- **注意**：R21-C1 曾 resolved（\"Sections 1-6 + Limitations 在 page 8 结束\"），但当前版本再次超页，说明后续修改引入了新内容。\n- **风险**：Desk reject。ARR 政策明确拒绝超页论文。\n- **建议**：Discussion §5 压缩至 ~0.5 页（仅保留核心诊断结论）；§4.5/§4.6 细节移入 appendix；Figure 1+2 考虑合并或缩小。\n- [R1, R2 独立发现，交叉一致]\n\n**R22-N2 [critical] 标题与 positive construction result 的叙事矛盾**\n- 标题 \"Why Confidence Signals **Fail** to Improve LLM-Based NER\" 暗示纯 negative result。\n- §4.7 entity-level construction 给出显著 positive result：SciERC +1.67 pp (p=0.004), Few-NERD +0.88 pp (p<0.001)。\n- Conclusion 也以 construction 和 gating protocol 作为积极贡献结尾。\n- 标题与正文之间的矛盾会让审稿人质疑核心贡献定位。\n- **建议**：标题应反映完整故事弧。如 \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based NER\" 或 \"From Selection to Construction: ...\"。\n- [R1, R2 独立发现，交叉一致]\n\n### Should-Fix（影响评分但不一票否决）\n\n**R22-W1 [warning] correlation-selection gap 概念缺乏理论支撑**\n- 本质上是实证观察而非理论贡献。未提供形式化分析解释为什么 QE ρ 高不等于 selection 有效。\n- R2 列为 critical，R1 建议降为 warning 并增加简化分析框架。交叉后共识为 warning。\n- **建议**：增加简化的 expected gain bound（如在 degeneracy 率 d 下，expected selection gain ≤ (1-d) × oracle_gap），无需完整理论证明。\n\n**R22-W2 [warning] Abstract 中 LP 和 AUROC 缩写未展开**\n- LP 在 Abstract line 5 首次出现未定义；AUROC 在 line 4 未展开。\n- ACL 规范要求 Abstract 内缩写自包含定义。\n- **修复**：\"log-probability (LP)\", \"area under the ROC curve (AUROC)\"。\n- [R2 提出，R1 交叉同意]\n\n**R22-W3 [warning] LP-alignment gating protocol 使用 test set 做 probe**\n- §4.7 line 266 承认 \"probe instances are drawn from the test set for simplicity\"。\n- 仅 3 个数据集验证 gating 效果。\n- Entity construction 阈值 θ 在 SciERC 上也为 post-hoc (θ=2/N) vs 其他 CV。\n- 构成同一类方法论关切：评估与选择之间的 information leakage。\n- **建议**：用 validation split 重做，或弱化 claim 为 preliminary proof-of-concept；统一阈值选择为 CV。\n- [R2-W3, R1 交叉同意; 与 R22-W5 相关]\n\n**R22-W4 [warning] SciERC 主实验 seed sensitivity 高，统计推断力受限**\n- SciERC LP selection 3-seed mean: +0.04±0.48 pp（Limitations line 14），但 main text 主要引用 1-seed 结果。\n- n=529, MDE ≈ 1.5 pp at 80% power。TOST 未报告 post-hoc power。\n- 核心结论不依赖 SciERC 等价性检验（Few-NERD n=32,565 提供 definitive test），但 SciERC 作为 primary test bed 的 positioning 与其统计功效不匹配。\n- **建议**：主文更显著地报告 multi-seed 结果和 seed sensitivity。\n- [R1-W3, R2-W4 交叉一致]\n\n**R22-W5 [warning] Entity construction 阈值 θ 跨数据集不一致**\n- SciERC 用 post-hoc θ=2/N，Few-NERD/CoNLL 用 5-fold CV。\n- Post-hoc 阈值有 data snooping 风险，可能高估 SciERC 的 construction gain。\n- **建议**：统一为 CV 或明确标注为 exploratory。\n- [R2-Q4, R1 交叉同意]\n\n**R22-W6 [warning] \"the correct self-consistency analogy\" 措辞过于绝对**\n- Contribution 3 和 Abstract 使用 \"the correct\"。仅在 NER 上验证，CoNLL 上不 work (-0.39 pp)。\n- **建议**：改为 \"a more effective\" 或 \"a natural\"。\n- [R2-W6, R1 交叉同意]\n\n**R22-W7 [warning] 仅测试 LoRA 微调但 claim 范围不限定**\n- 所有实验均为 LoRA fine-tuned models。LP compression 可能是 LoRA 特有现象。\n- Discussion §5 讨论了 ICL 可能不同，Limitations 承认未测试，但标题/Abstract 未限定。\n- **建议**：标题或 Abstract 中限定为 fine-tuned LLMs。\n- [R1-W2, R2 交叉部分同意]\n\n**R22-MR1 [warning] 缺失引用**\n- Related Work 缺少 ensemble-based NER methods 讨论（与 entity-level construction 直接相关）。\n- Xie et al. (2023) self-evaluation beam search、Wan et al. (2024) IE survey 未引用。\n- 9 条 bib entry 年份/venue 需复核（hobelsberger2025, lightman2024 等）。\n- [R1, R2 分别提出]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题双方独立发现并在交叉后确认一致：\n\n1. **超页限** — 正文约 10 页 vs 8 页限制，desk reject 风险。[R1-N1 = R2-N1]\n2. **标题叙事矛盾** — \"Fail\" vs entity-level construction positive result。[R1-N3 ≈ R2-N3]\n3. **SciERC 统计功效/seed sensitivity** — n=529, 1 primary seed, σ=0.48 pp。[R1-W3 ≈ R2-W4]\n4. **Gating/threshold data snooping** — test set probe + post-hoc θ。[R1 Q5-Q6 ≈ R2-W3 ≈ R2-Q4]\n5. **实验设计和统计严谨性是核心优势** — 22 页附录、TOST、bootstrap、power analysis。[S1]\n6. **QE-selection 分离框架有社区价值** — 可操作的概念贡献。[S2]\n7. **定位为 Findings 更合适** — Main Conference 需要更强的正面结果或理论深度。[双方 3.0/5]\n\n---\n\n## Reviewer Divergence [REBUT]\n\n1. **R1-N2 实体匹配标准是否缺失**：R1 列为 critical（定义缺失），R2 反驳称定义完整但分散在 §3.2 各段落中（VC: exact (text, type) tuple; SJ: type-grouped Hungarian matching with token-level IoU; FK: exact string matching; EM: complete output exact match）。R1 未对此反驳进一步回应。**Director 判断**：R2 的证据令人信服，定义确实存在但可读性不佳。降级为 info (R22-I1)，建议增加统一展示表格。\n\n2. **R2-N2 理论深度 critical vs warning**：R2 列为 critical，R1 建议降为 warning（论文定位为 empirical analysis, Findings 接受高质量实证分析）。**Director 判断**：采纳 R1 建议，降为 warning (R22-W1)。增加简化分析框架即可。\n\n3. **R2-W5 Entity-level construction 新颖性**：R2 认为本质是 majority voting，新颖性有限。R1 部分反驳：论文将其定位为分析发现而非方法贡献，新颖性要求应更低。**Director 判断**：R1 的论点合理，但 Abstract 和 Contribution 3 的措辞确实有 overclaim 风险（\"the correct analogy\"），需调整语气。已包含在 R22-W6。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Few-NERD LP selection 成功是否本质上是 under-training 的结果？如果 Few-NERD 模型 under-trained（3 epochs vs 5），LP compression 尚未充分发生，LP selection 的 \"成功\" 可能仅反映模型 calibration 尚未被破坏。Epoch ablation 显示 5-epoch 控制组 LP gains 减半——这是否暗示 LP selection 是 training 不充分的 artifact 而非 dataset 特性？[R2-Q2, R1 交叉同意为有洞察力的假设]\n\n**Q2.** within-instance ρ(LP, F1) 跨数据集能否量化地预测 LP gain？论文宣称 LP-quality alignment 是 primary predictor，但未给出 alignment-gain 的跨数据集相关性数据。如果有 3+ 个数据点的 ρ_within vs Δ_LP 关系，将大幅增强诊断框架的说服力。[R2-Q3]\n\n**Q3.** Greedy (T=0) 与单个 T=1.0 样本的平均 F1 比较如何？如果 T=1.0 单样本 F1 显著低于 greedy，则 selection 面对的是\"从 N 个较弱样本中选最好的 vs 一个强样本\"的比较，这与\"信号无信息量\"是不同的 claim。[R1-Q4]\n\n**Q4.** Oracle selection 在哪些类型的 instance 上成功？按实体类型、句子长度、实体密度分层的 oracle-selected vs signal-selected 对比分析，可提供可操作的改进方向。[R1-W4]\n\n---\n\n## Missing References\n\n1. **Ensemble-based IE methods**（如 multi-model voting for NER）——与 entity-level construction 直接相关，Related Work 应讨论。[R1, R2 共识]\n2. **Xie et al. (2023)** \"Self-Evaluation Guided Beam Search for Reasoning\" (NeurIPS 2023)——另一种 per-sample scoring method。[R2]\n3. **Wan et al. (2024)** Knowledge Extraction in Low-Resource Scenarios survey (ACL 2024 Findings)——NER/IE LLM 综述。[R2]\n4. **9 条 bib entry 需复核年份/venue**：hobelsberger2025, lightman2024, venktesh2025, aggarwal2023 在 OpenAlex 中未找到；feng2025, snell2025, muller2021, park2024, chen2025twofailures 存在轻微不匹配。均可能为索引延迟，但建议核查。[R1]\n\n注：R1 提出的 Kadavath et al. (2022) 已在论文中引用（Related Work §2 line 19, Limitations line 13）。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。\n\n---\n\n## Overall Assessment\n\n**评分：weak reject（Main Conference）/ borderline accept（Findings）**\n**置信度：4/5**\n\n| 维度 | 分数 | 说明 |\n|------|------|------|\n| Soundness | 3.5/5 | 实验方法论扎实，统计严谨，但 gating protocol test-set leak 和 SciERC seed sensitivity 削弱部分结论 |\n| Excitement | 2.5/5 | QE-selection gap 的诊断有启发性但缺理论深度；entity construction 增量偏小；诊断性论文定位 Findings 更合适 |\n| Reproducibility | 4/5 | 超参数、训练配置、seed 协议详尽，承诺 code release。缺总 GPU hours |\n| Overall | 3.0/5 | 实证工作扎实但核心贡献停留在实证描述层面，EMNLP Main 需要更锐利的贡献或更强的正面结果 |\n\n**核心判断**：这是一篇实验极度充分、统计严谨的诊断性论文。QE-selection 分离的概念框架和 entity-level construction 方案对社区有实际价值。但三个因素限制了 Main Conference 竞争力：\n\n1. **格式违规**（超页 ~2 页）是首要障碍，必须在提交前解决。\n2. **叙事不统一**（标题暗示纯 negative，但有显著 positive result）会让审稿人困惑核心定位。\n3. **Excitement gap**：correlation-selection gap 停留在实证描述层面，缺乏理论支撑；entity construction 是已知技术的应用而非方法创新。\n\n**建议路径**：(A) 修复超页和标题后投 Findings（最稳妥）；(B) 增加简化理论框架 + 限定 claim scope 后投 Main Conference（有竞争力但需要更精确的 positioning）。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- LP 和 AUROC 缩写需展开 [R22-W2]\n- \"the correct self-consistency analogy\" → \"a more effective\" [R22-W6]\n- 最后一句过长（~50 words），建议拆分 [R2-Minor-2]\n\n### Introduction\n- 标题暗示纯 negative result，但 Contribution 3 是 positive [R22-N2]\n- Contribution 3 \"correct\" 措辞需弱化 [R22-W6]\n- 与 Yao et al. (2026) 的 3-4 个关键差异应更明确 [R2-W2]\n\n### Method (§3)\n- 实体匹配标准分散在各段落中，建议增加统一对比表格 [R22-I1]\n- \"Soft Jaccard\" 命名与标准 Jaccard 有区别，应更明确说明 [R1-W5, R2 反驳认为命名合理，minor]\n\n### Experiments (§4)\n- §4.5 Robustness 和 §4.6 Hidden state probe 细节建议移入 appendix 以节省页数 [R22-N1]\n- §4.7 gating protocol 应用 validation split 而非 test set [R22-W3]\n- Entity construction θ 应统一为 CV [R22-W5]\n- SciERC multi-seed 结果应在 main text 显著报告 [R22-W4]\n\n### Discussion (§5)\n- 当前约 2 页，是超页主因。建议压缩至 ~0.5 页 [R22-N1]\n- 增加简化的 expected selection gain bound [R22-W1]\n\n### Conclusion (§6)\n- \"a alignment-based\" → \"an alignment-based\" [R22-I2]\n\n### Limitations\n- LoRA 限定应更显著 [R22-W7]\n\n### References\n- 9 条 bib entry 年份/venue 需复核 [R22-MR1]\n- 补充 ensemble-based IE methods 等引用 [R22-MR1]\n\n### Formatting\n- \\citep 和 \\cite 混用需统一 [R22-I2]\n- Figure 3 标签在打印尺寸下可能难辨 [R22-I3]",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 2254 · 2026-05-19T03:51:54.496303+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4588
}
```

</details>

---


### Assistant

_source line 2255 · 2026-05-19T03:52:02.252873+00:00_

审稿报告已投递至 Research Director。

**Round 22 审稿完成。** 汇总：

- **评分**：weak reject (Main Conference) / borderline accept (Findings)，3.0/5
- **2 个 critical**：正文超页 ~2 页（desk reject 风险）；标题与 positive construction result 叙事矛盾
- **7 个 warning**：理论深度不足、Abstract 缩写未展开、gating test-set leak、SciERC seed sensitivity、construction 阈值不一致、"correct" 措辞过强、LoRA claim 范围不限定
- **3 个 info**：匹配标准展示可读性、冠词/引用格式、Figure 3 标签
- **建议路径**：修复超页和标题后投 Findings（最稳妥），或增加简化理论框架 + 限定 claim scope 后投 Main Conference

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 173

## Round 173

2 recorded events


### User

_source line 2256 · 2026-05-19T03:52:05.035493+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **AGREE（6 项）**：N1 超页、N3 标题矛盾部分、W3 TOST power、W4 instance-level error analysis 部分、Q4 T=0.6 对比缺失、Minor-2/3
- **REBUT（8 项）**：N2 实体匹配定义实际存在于 §3.2、W1 关键证据在 Discussion 正文中、W5 Soft Jaccard 命名合理、Q1/Q2/Q3/Q5/Q6 论文中有充分回答、Missing-1 Kadavath 已被引用、Minor-1 confidence signal 术语准确
- **PARTIALLY AGREE（3 项）**：N3 CoNLL 循环论证（CoNLL 定位为 control 而非核心证据）、W2 仅 LoRA（Discussion 已讨论 ICL）、Missing-2 结构化预测 uncertainty 覆盖

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2257 · 2026-05-19T03:52:15.094382+00:00_

审稿报告已投递至 Research Director。

**Round 22 审稿完成。** 最终结论：

- **评分**：weak reject（Main Conference）/ borderline accept（Findings）
- **2 个 critical**：正文超页 ~2 页（desk reject 风险）、标题与 positive result 叙事矛盾
- **7 个 warning**：correlation-selection gap 缺理论支撑、Abstract 缩写未展开、gating test-set leak、SciERC seed sensitivity、entity construction θ 不一致、"correct" 措辞过强、LoRA claim 不限定
- **建议路径**：修复超页和标题后投 Findings（最稳妥），或增加简化理论框架后投 Main Conference

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 174

## Round 174

76 recorded events


### User

_source line 2258 · 2026-05-19T04:48:55.114937+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2259 · 2026-05-19T04:49:01.108095+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2260 · 2026-05-19T04:49:01.159083+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2261 · 2026-05-19T04:49:03.919645+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2262 · 2026-05-19T04:49:03.920034+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2263 · 2026-05-19T04:49:10.263826+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 2264 · 2026-05-19T04:49:10.364701+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2265 · 2026-05-19T04:49:12.723144+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 2266 · 2026-05-19T04:49:13.726960+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (166 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_llama_fewnerd_inference** (success): LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness. ← 基于 exp_llama_fewnerd_lora\n- **exp_entity_construction** (success): Entity-level majority vote construction is the correct self-consistency analogy for structured IE: instead of selecting the best instance-level output, assemble a better output from entity-level consensus across N samples. Construction should outperform both greedy and best-of-N selection.\n- **exp_lp_alignment_gating** (success): Within-instance LP-F1 alignment score (adjusted by valid_ratio for degeneracy) can automatically gate whether LP selection should be applied to a dataset. A small probe sample (50-100 instances) suffices for a stable gating decision.\n\n## 趋势\n成功 101 / 负向 33 / 失败 4 / 共 166\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\nautodl-5090-b: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\nautodl-5090-c: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\
…[truncated 1355 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 2267 · 2026-05-19T04:49:13.727505+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 2268 · 2026-05-19T04:49:15.266853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 2269 · 2026-05-19T04:49:15.317444+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Diagnosing and Fixing Self-Consistency for Named Entity Recognition}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\section*{Responsible NLP Research Checklist}
47	\input{sections/checklist}
48	
49	\bibliography{references}
50	
51	\appendix
52	\input{sections/appendix}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2270 · 2026-05-19T04:49:24.198444+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the search results, here's a summary of the key EMNLP 2026 Call for Papers submission guidelines and author instructions:

## Paper Types and Content

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. EMNLP 2026 has a goal of curating a diverse technical program—in addition to tradit
…[truncated 2093 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 10470
}
```

</details>

---


### Tool call

_source line 2271 · 2026-05-19T04:49:31.273829+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format guidelines page limit long short paper template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format guidelines page limit long short paper template"
  }
}
```

</details>

---


### Tool call

_source line 2272 · 2026-05-19T04:49:33.683121+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 2273 · 2026-05-19T04:49:34.135184+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2274 · 2026-05-19T04:49:34.469645+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 2275 · 2026-05-19T04:49:37.580380+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format guidelines page limit long short paper template"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, I've found the ACL Rolling Review 2026 submission format guidelines. Here's the key information:

## Page Limits

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages). More specifically:

- **Long Papers**: Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references.
- **Short Pape
…[truncated 1201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 6306
}
```

</details>

---


### Tool result

_source line 2276 · 2026-05-19T04:49:37.580907+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: '2026-05-14T21:00:00.000Z'\\n  total_papers: 55\\ncategories: []\\npapers:\\n  wang2023selfconsistency:\\n    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models\\n    authors:\\n    - Xuezhi Wang\\n    - Jason Wei\\n    - Dale Schuurmans\\n    - Quoc Le\\n    - Ed Chi\\n    - Sharan Narang\\n    - Aakanksha Chowdhery\\n    - Denny Zhou\\n    year: 2023\\n    venue: ICLR 2023\\n    url: https://arxiv.org/abs/2203.11171\\n    doi: ''\\n    bibtex_key: wang2023selfconsistency\\n    category: self_consistency_reasoning\\n    role: foundation\\n    relevance: 'Foundation paper: introduces self-consistency voting over diverse reasoning paths. We extend this paradigm\\n      from closed-form answers to structured IE outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  taubenfeld2025cisc:\\n    title: Confidence Improves Self-Consistency in LLMs\\n    authors:\\n    - Amir Taubenfeld\\n    - Tom Sheffer\\n    - Eran Ofek\\n    - Amir Feder\\n    - Ariel Goldstein\\n    - Zorik Gekhman\\n    - Gal Yona\\n    year: 2025\\n    venue: ACL Findings 2025\\n    url: https://arxiv.org/abs/2502.06233\\n    doi: 10.18653/v1/2025.findings-acl.1030\\n    bibtex_key: taubenfeld2025cisc\\n    category: self_consistency_reasoning\\n    role: direct-competitor\\n    relevance: 'CISC: confidence-weighted majority vote reduces required samples by 40%. Direct competitor — we address the\\n      same \\\"strong predictor, weak selector\\\" gap but for structured outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  kang2025selfcertainty:\\n    title: 
…[truncated 3614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 3111
}
```

</details>

---


### Tool call

_source line 2277 · 2026-05-19T04:49:43.858069+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 2278 · 2026-05-19T04:49:43.958965+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2279 · 2026-05-19T04:49:46.167639+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2280 · 2026-05-19T04:49:46.168003+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using fine-tuned 4B\textendash 8B models.
4	All signals achieve reliable QE ($\rho$ up to 0.45, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
5	For instance-level selection, log-probability (LP) achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) where LP-quality alignment is strong, but gains are absent elsewhere despite ${\sim}$13~pp oracle headroom (the \textbf{correlation-selection gap}).
6	We diagnose two causes: instance degeneracy (13\textendash 87\%) and weak LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction ($\rho{=}0.052$, 23 configurations).
7	A more effective self-consistency analogy for structured outputs is entity-level \textit{construction}: aggregating entities across samples improves F1 by $+0.88$ to $+1.67$\,pp ($p{<}0.005$) on datasets where instance-level selection fails or is marginal. Construction and LP selection are complementary, governed by LP-quality alignment; an alignment-based gating protocol correctly routes all three evaluated datasets.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2281 · 2026-05-19T04:49:46.619901+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2282 · 2026-05-19T04:49:47.523426+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
8	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we provide the first systematic empirical characterization of \textit{when and why} LP-based selection succeeds or fails for structured prediction, diagnosing degeneracy and compression as the two blocking mechanisms.
9	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.
10	
11	A key distinction structures our analysis: four of five signals (Soft Jaccard, voting confidence, Fleiss' $\kappa$, exact match) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction.
13	For selection, LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) in settings where both low inst
…[truncated 4435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 2283 · 2026-05-19T04:49:47.574108+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2284 · 2026-05-19T04:49:47.674950+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} rely on answer-level agreement.
6	Adaptive variants gate on answer agreement \cite{aggarwal2023adaptive}, input difficulty \cite{wang2025make, feng2025optimal}, or response confidence \cite{kim2026reasc}; \citet{chen2025twofailures} diagnose SC failure modes without proposing gating.
7	All target discrete-answer reasoning; structured prediction requires different gating signals because degeneracy operates at the entity-set level.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation alone does not ensure selection gains, diagnosing degeneracy and compression as blocking mechanisms.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\S\ref{sec:robustness_main}).
12	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
13	Ensemble approaches aggregate predictions from multiple models or prompts \cite{xiao2025el4ner}; our entity-level construction similarly aggregates across samples from a single model, without requiring model diversity.
14	Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting, xie2024selfimproving} and constrained decoding \cite{willard2023guided, dong2024xgrammar, park2024grammar, schall2025hidden}.
15
…[truncated 1948 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2285 · 2026-05-19T04:49:47.725586+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2286 · 2026-05-19T04:49:47.776308+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Throughout, entity matching uses exact span and type match (a predicted entity is correct iff its character offsets and type label both match a gold entity).
12	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
13	
14	\paragraph{Log-probability (model-internal, per-sample).}
15	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
16	\begin{equation}\label{eq:logprob}
17	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
18	\end{equation}
19	
20	\paragraph{Exact match voting (surface, instance-level).}
21	The proportion of samples producing the most common output:
22	\begin{equation}\label{eq:em}
23	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
24	\end{equation}
25	
26	\paragraph{Fleiss' $\kappa$ (surface, insta
…[truncated 3790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2287 · 2026-05-19T04:49:51.690463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2288 · 2026-05-19T04:49:52.192855+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (training details in Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others due to earlier convergence; Appendix~\ref{app:epoch_confound}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\ref{app:n_scaling}).
17	
18	%% ============================================================
19	\subsection{Quality Estimation Results}
20	\label{sec:qe_results}
21	
22	\begin{table*}[t]
23	\centering
24	\small
25	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
26	\label{tab:quality_estimation}
27	\begin{tabular}{ll cc cc cc}
28	\topr
…[truncated 16461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2289 · 2026-05-19T04:49:52.193317+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2290 · 2026-05-19T04:49:52.695209+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; effective selection likely requires content-aware verifiers \cite{cobbe2021verifiers, venktesh2025trust}.
4	Two factors constrain selection: instance degeneracy (17.8--48.4\%) eliminates headroom, and LP compression (within-instance $\rho$ 0.262--0.667) prevents exploiting the remainder; within non-degenerate instances, MBR utility correlates positively with F1 (SJ median $\rho{=}0.524$) \cite{eikema2022sampling}.
5	Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), within-instance $\rho$ rises to 0.39 and LP selection yields $+2.9$~pp ($p{=}0.004$; Table~\ref{tab:nontied_main}).
6	Temperature disentangles the two factors: at $T{=}1.2$, degeneracy drops to 14.9\% yet LP does not improve ($\rho{=}0.225$ vs.\ Few-NERD ${\sim}$0.5--0.7; Table~\ref{tab:t_degeneracy}); degeneracy rises with model scale and training convergence (Tables~\ref{tab:scale_ablation}, \ref{tab:epoch_confound}), so the selection window narrows as models improve \cite{wang2023selfconsistency, snell2025scaling}.
7	
8	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
9	Entity-level construction bypasses both failure mechanisms ($+1.67$\,pp SciERC, $+0.88$\,pp Few-NERD; Table~\ref{tab:entity_construction}), complementary with LP selection and governed by LP-quality alignment (\S\ref{sec:prescriptive}).
10	Alternative strategies (DALS, MBR, DGS) fail to reliably beat greedy (Appendix~\ref{app:dals}).
11	Our negative results are specific to fine-tuned models with constrained decoding; settings with greater output diversity may restore selection headroom (Appendix~\ref{app:when_selection_works}).
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 2291 · 2026-05-19T04:49:52.745758+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2292 · 2026-05-19T04:49:53.197798+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	Five confidence signals achieve reliable NER quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
4	Instance-level selection fails due to degeneracy and LP compression, but a more effective self-consistency analogy for structured outputs is entity-level construction: LP-weighted entity aggregation yields $+1.67$\,pp on SciERC ($p{=}0.004$) and $+0.88$\,pp on Few-NERD ($p{<}0.001$).
5	Construction and LP selection are complementary, governed by LP-quality alignment; an alignment-based gating protocol routes the appropriate method per dataset.
6	For practitioners: use QE-based selective prediction when deployment requires reliability guarantees; apply entity construction when multi-sample generation is feasible; assess LP-alignment via held-out validation to choose between construction and LP selection.
7	As models improve, degeneracy rises and the selection window narrows; content-aware verifiers \cite{cobbe2021verifiers} may be needed to close the remaining gap.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2293 · 2026-05-19T04:49:53.198308+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2294 · 2026-05-19T04:49:53.248835+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and these two factors may shift in opposite directions.
3	Our supervised approaches (DeBERTa verifier, hidden state probes, MLP/RF on signal combinations) all fail to close the oracle gap; whether content-aware verifiers with access to task-specific structure could succeed remains open.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{lin2022teaching, tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app
…[truncated 1951 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2295 · 2026-05-19T04:49:59.069644+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool call

_source line 2296 · 2026-05-19T04:49:59.120292+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 2297 · 2026-05-19T04:49:59.170956+00:00_

1	% Responsible NLP Research Checklist
2	% Following the ACL Rolling Review guidelines:
3	% https://aclrollingreview.org/responsibleNLPresearch/
4	
5	\subsection*{A\hspace{0.5em} For Every Submission}
6	
7	\begin{enumerate}
8	\item[A1.] \textbf{Did you discuss the limitations of your work?}\\
9	Yes. See the Limitations section after the Conclusion.
10	
11	\item[A2.] \textbf{Did you discuss any potential risks of your work?}\\
12	Yes. See the Ethics Statement. This work analyzes existing confidence signals for NER and identifies when they fail; the findings reduce risk of deploying unreliable confidence-based selection in production systems. No dual-use concerns.
13	
14	\item[A3.] \textbf{Do the abstract and introduction summarize the paper's main claims?}\\
15	Yes. The Abstract and Section~\ref{sec:introduction} (3 enumerated contributions) summarize all main claims with supporting evidence pointers.
16	\end{enumerate}
17	
18	\subsection*{B\hspace{0.5em} Did you use or create scientific artifacts?}
19	
20	Yes. We use existing datasets and pre-trained models.
21	
22	\begin{enumerate}
23	\item[B1.] \textbf{Did you cite the creators of artifacts you used?}\\
24	Yes. All datasets are cited: SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, Few-NERD \cite{ding2021fewnerd}, WNUT-17 \cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \cite{zheng2024llamafactory}. Constrained decoding: XGrammar \cite{dong2024xgrammar}. See Sections~\ref{sec:introduction}, \ref{sec:evaluation}, and Appendix~\ref{app:training}.
25	
26	\item[B2.] \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\\
27	Partially. The Ethics Statement notes that CoNLL-2003 is derived from the Reuters RCV1 corpus, available under a NIST agreement for research. SciERC, Few-NERD, and WNUT-17 are publicly available research benchmarks. Qwen3 and LLaMA-3.1 are open-weight models released under their r
…[truncated 4168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2298 · 2026-05-19T04:49:59.773531+00:00_

File content (40360 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 2299 · 2026-05-19T04:50:04.894701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2300 · 2026-05-19T04:50:04.945457+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $
…[truncated 13589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2301 · 2026-05-19T04:50:08.859940+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "200",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "200",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2302 · 2026-05-19T04:50:08.910772+00:00_

200	EM ranks first across all four tested conditional configurations: SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$). This holds despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
201	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
202	On the conditional set, where the model demonstrably produces varied outputs, exact agreement becomes the strongest quality signal.
203	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
204	
205	\paragraph{WNUT-17 full signal analysis.}
206	Table~\ref{tab:wnut} reports all five signals on WNUT-17 with full-set and conditional $\rho$.
207	
208	\begin{table}[t]
209	\centering
210	\small
211	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\rho$ reflects binary success prediction; conditional $\rho$ measures quality gradation. LP's conditional $\rho$ is highest despite negative full-set $\rho$.}
212	\label{tab:wnut}
213	\begin{tabular}{lcccc}
214	\toprule
215	Signal & $\rho$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
216	\midrule
217	VC      & .724 & .913 & .038 & .487 \\
218	FK      & .125 & .555 & .169 & .002 \\
219	SJ      & .089 & .517 & .288 & ${<}$1e-7 \\
220	EM      & .050 & .487 & .333 & ${<}$1e-9 \\
221	LP & $-$.410 & .219 & .350 & ${<}$1e-10 \\
222	\bottomrule
223	\end{tabular}
224	\end{table}
225	The full-set $p$-values are: VC ${<}$1e-112, FK $p{=}0.001$, SJ $p{=}0.020$, EM $p{=}0.194$, LP ${<}$1e-28.
226	VC's high full-set $\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditio
…[truncated 14570 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2303 · 2026-05-19T04:50:12.792286+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "400",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "400",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2304 · 2026-05-19T04:50:12.843220+00:00_

400	
401	\paragraph{External equivalence margins.}
402	The oracle-headroom anchors above introduce circularity, as a reviewer correctly noted: $\delta$ is calibrated against the very quantity it contextualizes.
403	To resolve this, we supplement with three externally grounded margins:
404	(1) $\delta_{\mathrm{SEM}}$: the bootstrapped standard error of single-sample F1 (0.43--1.33~pp depending on configuration), which represents measurement noise;
405	(2) $\delta_{\mathrm{practical}}{=}0.5$~pp, the threshold below which NER differences are considered negligible \cite{ratinov2009design};
406	(3) $\delta_{\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \cite{bergkirkpatrick2012empirical}.
407	
408	Results under these external anchors diverge sharply by configuration.
409	On LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\Delta|{\leq}0.1$~pp) and tight CIs at this sample size.
410	On Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\delta$: selection F1 degrades by 0.9--1.5~pp relative to single-sample, which exceeds even $\delta_{\mathrm{literature}}$.
411	On SciERC NER ($n{=}529$), only SJ passes at $\delta_{\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.
412	These external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to single-sample under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.
413	
414	\paragraph{Multiple comparison considerations.}\label{app:multiple_comparisons}
415	Our primary selection analysis involves ${\sim}$20 comparisons (5 signals $\times$ 3--4 configurations).
416	Since all primary selection results are non-significant ($p{>}0.05$), applying Benjamini-Hochberg correction 
…[truncated 13967 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2305 · 2026-05-19T04:50:16.584580+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "600",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "600",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 2306 · 2026-05-19T04:50:16.635590+00:00_

600	0.05 & 60.3\% \\
601	0.1  & ${\sim}$84\% \\
602	0.5  & ${\sim}$99\% \\
603	\bottomrule
604	\end{tabular}
605	\end{table}
606	
607	\paragraph{Non-tied subset.}
608	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms single-sample ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
609	As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability. LP carries information, but compression limits its exploitation.
610	A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
611	
612	\paragraph{$\varepsilon$ sensitivity sweep (post-hoc exploratory).}
613	Table~\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\varepsilon{=}0.01$ to $0.20$ as a post-hoc exploratory analysis characterizing how selection gain varies with compression severity.
614	The tied fraction increases smoothly with no cliff or discontinuity, and the selection gain $\Delta$ grows monotonically as the non-tied subset narrows to progressively higher-spread instances.
615	$\varepsilon{=}0.05$ yields the strongest statistical separation ($p{=}0.004$); at $\varepsilon{\geq}0.15$, the non-tied subset becomes too small for reliable inference ($n{\leq}36$).
616	
617	\begin{table}[t]
618	\centering
619	\small
620	\caption{$\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\%'' = fraction with within-instance LP range ${<}\varepsilon$. $\Delta$: selection F1 gain over single-sample on 
…[truncated 17697 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2307 · 2026-05-19T04:50:23.611176+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2308 · 2026-05-19T04:50:24.113328+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2309 · 2026-05-19T04:50:25.217556+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 2310 · 2026-05-19T04:50:25.619404+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2311 · 2026-05-19T04:50:26.121490+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 2312 · 2026-05-19T04:50:27.025279+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 2313 · 2026-05-19T04:50:27.126000+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2314 · 2026-05-19T04:50:27.277373+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2315 · 2026-05-19T04:50:30.088330+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 2316 · 2026-05-19T04:50:30.590279+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 2317 · 2026-05-19T04:50:30.590590+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2318 · 2026-05-19T04:50:31.042663+00:00_

1	issues:
2	  # ===== 历史 resolved issues（保留记录）=====
3	  - id: "R1-W1"
4	    summary: "Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应"
5	    category: experiment
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 1
9	    last_seen_round: 19
10	    resolution: "Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。"
11	    resolution_round: 19
12	
13	  - id: "R1-W2"
14	    summary: "\"Two jointly necessary conditions\" 因果性表述过强"
15	    category: framing
16	    severity: critical
17	    status: resolved
18	    first_raised_round: 1
19	    last_seen_round: 21
20	    resolution: "全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。"
21	    resolution_round: 21
22	
23	  - id: "R2-N1"
24	    summary: "Contribution 1 'methodological premise' 是定义推论"
25	    category: framing
26	    severity: critical
27	    status: resolved
28	    first_raised_round: 1
29	    last_seen_round: 19
30	    resolution: "Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。"
31	    resolution_round: 19
32	
33	  - id: "R2-N2"
34	    summary: "与 MBR 文献差异化定位不够锐利"
35	    category: framing
36	    severity: warning
37	    status: resolved
38	    first_raised_round: 1
39	    last_seen_round: 19
40	    resolution: "Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。"
41	    resolution_round: 19
42	
43	  - id: "R2-N4"
44	    summary: "模型规模 3B-8B，70B+ 未知"
45	    category: experiment
46	    severity: info
47	    status: resolved
48	    first_raised_round: 1
49	    last_seen_round: 19
50	    resolution: "Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。"
51	    resolution_round: 19
52	
53	  - id: "R1-W3"
54	    summary: "2-seed 统计效力不足"
55	    category: experiment
56	    severity: warning
57	    status: resolved
58	    first_raised_round: 1
59	    last_seen_round: 19
60	    resolution: "Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。"
61	    resolution_round: 19
62	
63	  - id: "R1-W4"
64	    summary: "P
…[truncated 17767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2319 · 2026-05-19T04:50:31.193478+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2320 · 2026-05-19T04:50:31.244056+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{vijayakumar2018diverse,
4	  title = {Diverse Beam Search for Improved Description of Complex Scenes},
5	  author = {Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and Sun, Qing and Lee, Stefan and Crandall, David J. and Batra, Dhruv},
6	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
7	  year = {2018},
8	  url = {https://arxiv.org/abs/1610.02424}
9	}
10	
11	@inproceedings{shi2022mbr,
12	  title = {Natural Language to Code Translation with Execution},
13	  author = {Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and Wang, Sida I.},
14	  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
15	  pages = {3533--3546},
16	  year = {2022},
17	  url = {https://arxiv.org/abs/2204.11454}
18	}
19	
20	@article{eisenstein2023helping,
21	  title = {Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking},
22	  author = {Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D'Amour, Alex and Dvijotham, DJ and Fisch, Adam and Heller, Katherine and Pfohl, Stephen and Ramachandran, Deepak and Shaw, Peter and Berant, Jonathan},
23	  journal = {arXiv preprint arXiv:2312.09244},
24	  year = {2023},
25	  url = {https://arxiv.org/abs/2312.09244}
26	}
27	
28	@article{brown2024monkeys,
29	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
30	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
31	  journal = {arXiv preprint arXiv:2407.21787},
32	  year = {2024},
33	  url = {https://arxiv.org/abs/2407.21787}
34	}
35	
36	@inproceedings{chen2024usc,
37	  title = {Universal Self-Consistency for Large Language Model Generation},
38	  author = {Chen, Xinyun and Aksitov, Renat and Alon, 
…[truncated 3112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2321 · 2026-05-19T04:50:37.367923+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i config | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i config | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 2322 · 2026-05-19T04:50:37.418509+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/pending_approval_notifications.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2323 · 2026-05-19T04:50:40.894769+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
  "description": "Find project-level yaml files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
    "description": "Find project-level yaml files"
  }
}
```

</details>

---


### Tool result

_source line 2324 · 2026-05-19T04:50:40.946458+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2325 · 2026-05-19T04:50:45.259938+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/ /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/*.yaml 2>/dev/null | head -10",
  "description": "Check for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/ /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/*.yaml 2>/dev/null | head -10",
    "description": "Check for external review config"
  }
}
```

</details>

---


### Tool result

_source line 2326 · 2026-05-19T04:50:45.310608+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2327 · 2026-05-19T04:51:20.790658+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2328 · 2026-05-19T04:51:20.841232+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2329 · 2026-05-19T04:51:47.035197+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重：方法严谨性 + 实验设计**\n\n### 论文信息\n- **标题**: Strong Predictors, Weak Selectors: Diagnosing and Fixing Self-Consistency for Named Entity Recognition\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（各 section 在 `sections/` 子目录）\n- **目标 venue**: EMNLP 2026 Main Conference（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，正文上限 8 页（不含 references 和 limitations），double-blind\n\n### 你的审查重点\n\n1. **实验设计合理性**\n   - 数据集选择和角色分配（SciERC 作为 primary test bed、Few-NERD 作为 contrast 等）是否合理\n   - 模型选择（Qwen3-8B、LLaMA-3.1-8B、Qwen3-4B ablation）覆盖度是否充分\n   - N=8 primary / N=16 扩展的样本量设置\n   - 训练配置（LoRA fine-tuning、epoch 选择等）是否有混淆因素\n\n2. **统计方法与报告**\n   - 显著性检验方法（paired bootstrap、sign test、TOST）是否恰当\n   - 多重比较校正是否充分\n   - Multi-seed 报告（3 seeds）是否足够，seed sensitivity 处理\n   - MDE（minimum detectable effect）的使用是否正确\n   - Confidence intervals 和 p-values 的报告是否一致\n\n3. **数据一致性**\n   - 同一指标跨表数值是否一致（如 SciERC greedy F1 有 4 个值、LP ρ 值等）\n   - 数据集过滤标准（gold-filtered vs full set）是否清晰一致\n   - 论文中引用的数据是否与表格匹配\n\n4. **方法论关切**\n   - Instance degeneracy 的定义和度量是否严谨\n   - LP compression 分析的 ε 阈值选择（post-hoc exploratory）\n   - Entity-level construction 的阈值 θ=2/N 是否有 data snooping 风险\n   - LP-alignment gating 使用 test set 做 probe 的 information leakage 问题\n   - Expected selection gain bound 的形式化程度\n\n5. **消融实验充分性**\n   - 温度、N-scaling、模型规模消融是否充分\n   - LoRA rank ablation 的覆盖度\n   - Free-form vs constrained decoding 的对比\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n- **Summary**: 论文概述（2-3 句）\n- **Strengths**: 优点（逐条）\n- **Weaknesses**: 缺点（逐条，按 critical / warning / info 分级，每条给出具体证据和建议）\n- **Questions**: 需要作者澄清的问题\n- **Missing References**: 方法/实验相关的遗漏引用\n- **Overall Assessment**: 评分（strong reject / weak reject / borderline / weak accept / strong accept）+ 置信度 + 简要理由",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重：方法严谨性 + 实验设计**\n\n### 论文信息\n- **标题**: Strong Predictors, Weak Selectors: Diagnosing and Fixing Self-Consistency for Named Entity Recognition\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（各 section 在 `sections/` 子目录）\n- **目标 venue**: EMNLP 2026 Main Conference（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，正文上限 8 页（不含 references 和 limitations），double-blind\n\n### 你的审查重点\n\n1. **实验设计合理性**\n   - 数据集选择和角色分配（SciERC 作为 primary test bed、Few-NERD 作为 contrast 等）是否合理\n   - 模型选择（Qwen3-8B、LLaMA-3.1-8B、Qwen3-4B ablation）覆盖度是否充分\n   - N=8 primary / N=16 扩展的样本量设置\n   - 训练配置（LoRA fine-tuning、epoch 选择等）是否有混淆因素\n\n2. **统计方法与报告**\n   - 显著性检验方法（paired bootstrap、sign test、TOST）是否恰当\n   - 多重比较校正是否充分\n   - Multi-seed 报告（3 seeds）是否足够，seed sensitivity 处理\n   - MDE（minimum detectable effect）的使用是否正确\n   - Confidence intervals 和 p-values 的报告是否一致\n\n3. **数据一致性**\n   - 同一指标跨表数值是否一致（如 SciERC greedy F1 有 4 个值、LP ρ 值等）\n   - 数据集过滤标准（gold-filtered vs full set）是否清晰一致\n   - 论文中引用的数据是否与表格匹配\n\n4. **方法论关切**\n   - Instance degeneracy 的定义和度量是否严谨\n   - LP compression 分析的 ε 阈值选择（post-hoc exploratory）\n   - Entity-level construction 的阈值 θ=2/N 是否有 data snooping 风险\n   - LP-alignment gating 使用 test set 做 probe 的 information leakage 问题\n   - Expected selection gain bound 的形式化程度\n\n5. **消融实验充分性**\n   - 温度、N-scaling、模型规模消融是否充分\n   - LoRA rank ablation 的覆盖度\n   - Free-form vs constrained decoding 的对比\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n- **Summary**: 论文概述（2-3 句）\n- **Strengths**: 优点（逐条）\n- **Weaknesses**: 缺点（逐条，按 critical / warning / info 分级，每条给出具体证据和建议）\n- **Questions**: 需要作者澄清的问题\n- **Missing References**: 方法/实验相关的遗漏引用\n- **Overall Assessment**: 评分（strong reject / weak reject / borderline / weak accept / strong accept）+ 置信度 + 简要理由",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2330 · 2026-05-19T04:52:04.108651+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17073
}
```

</details>

---


### Tool call

_source line 2331 · 2026-05-19T04:52:04.210329+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重：新颖性 + 完整性 + 格式合规**\n\n### 论文信息\n- **标题**: Strong Predictors, Weak Selectors: Diagnosing and Fixing Self-Consistency for Named Entity Recognition\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（各 section 在 `sections/` 子目录）\n- **目标 venue**: EMNLP 2026 Main Conference（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，正文上限 8 页（不含 references 和 limitations），double-blind\n\n### 你的审查重点\n\n1. **新颖性评估**\n   - 相对于 Wang et al. 2023 (self-consistency)、Taubenfeld et al. 2025 (CISC)、Kang et al. 2025 (self-certainty)、Yao et al. 2026 (consistency for IE) 等直接竞争者，本文增量贡献是否足够\n   - \"correlation-selection gap\" 概念是否有足够理论深度，还是仅仅是实证观察的包装\n   - Entity-level construction 相对于 ensemble NER / entity-level majority voting 的新颖性\n   - 负面结果（selection fails）的诊断价值评估\n\n2. **叙事统一性**\n   - 标题 → Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否形成一条连贯主线\n   - 标题是否准确反映论文完整故事（诊断 + 修复两部分）\n   - Contributions 列表是否与实验结果对应\n   - 正面结果（construction）和负面结果（selection fails）的平衡\n\n3. **Related Work 质量**\n   - 分类和组织是否清晰\n   - 是否充分覆盖：self-consistency methods、structured IE confidence、MBR decoding、BoN with verifiers\n   - 与本文的 positioning 是否清楚\n   - 引用密度是否符合 EMNLP 水平\n\n4. **格式合规**\n   - 正文是否在 8 页内（检查 section 内容量估算）\n   - ACL 匿名规则（检查 \\author{Anonymous}）\n   - Limitations 节位置和内容\n   - Responsible NLP Research Checklist 是否认真填写\n   - 缩写首次使用是否展开（特别是 Abstract 内的缩写）\n\n5. **写作质量**\n   - AI 写作痕迹检查（dash、-ing phrases、过度分段、用词黑名单）\n   - 专有名词首次出现是否有定义\n   - 图表 caption 是否自包含\n   - 引用格式一致性（\\cite vs \\citep）\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n- **Summary**: 论文概述（2-3 句）\n- **Strengths**: 优点（逐条）\n- **Weaknesses**: 缺点（逐条，按 critical / warning / info 分级，每条给出具体证据和建议）\n- **Questions**: 需要作者澄清的问题\n- **Missing References**: 相关工作/引用方面的遗漏\n- **Overall Assessment**: 评分（strong reject / weak reject / borderline / weak accept / strong accept）+ 置信度 + 简要理由",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重：新颖性 + 完整性 + 格式合规**\n\n### 论文信息\n- **标题**: Strong Predictors, Weak Selectors: Diagnosing and Fixing Self-Consistency for Named Entity Recognition\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（各 section 在 `sections/` 子目录）\n- **目标 venue**: EMNLP 2026 Main Conference（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，正文上限 8 页（不含 references 和 limitations），double-blind\n\n### 你的审查重点\n\n1. **新颖性评估**\n   - 相对于 Wang et al. 2023 (self-consistency)、Taubenfeld et al. 2025 (CISC)、Kang et al. 2025 (self-certainty)、Yao et al. 2026 (consistency for IE) 等直接竞争者，本文增量贡献是否足够\n   - \"correlation-selection gap\" 概念是否有足够理论深度，还是仅仅是实证观察的包装\n   - Entity-level construction 相对于 ensemble NER / entity-level majority voting 的新颖性\n   - 负面结果（selection fails）的诊断价值评估\n\n2. **叙事统一性**\n   - 标题 → Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否形成一条连贯主线\n   - 标题是否准确反映论文完整故事（诊断 + 修复两部分）\n   - Contributions 列表是否与实验结果对应\n   - 正面结果（construction）和负面结果（selection fails）的平衡\n\n3. **Related Work 质量**\n   - 分类和组织是否清晰\n   - 是否充分覆盖：self-consistency methods、structured IE confidence、MBR decoding、BoN with verifiers\n   - 与本文的 positioning 是否清楚\n   - 引用密度是否符合 EMNLP 水平\n\n4. **格式合规**\n   - 正文是否在 8 页内（检查 section 内容量估算）\n   - ACL 匿名规则（检查 \\author{Anonymous}）\n   - Limitations 节位置和内容\n   - Responsible NLP Research Checklist 是否认真填写\n   - 缩写首次使用是否展开（特别是 Abstract 内的缩写）\n\n5. **写作质量**\n   - AI 写作痕迹检查（dash、-ing phrases、过度分段、用词黑名单）\n   - 专有名词首次出现是否有定义\n   - 图表 caption 是否自包含\n   - 引用格式一致性（\\cite vs \\citep）\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n- **Summary**: 论文概述（2-3 句）\n- **Strengths**: 优点（逐条）\n- **Weaknesses**: 缺点（逐条，按 critical / warning / info 分级，每条给出具体证据和建议）\n- **Questions**: 需要作者澄清的问题\n- **Missing References**: 相关工作/引用方面的遗漏\n- **Overall Assessment**: 评分（strong reject / weak reject / borderline / weak accept / strong accept）+ 置信度 + 简要理由",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2332 · 2026-05-19T04:52:05.669855+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1459
}
```

</details>

---


### Assistant

_source line 2333 · 2026-05-19T04:52:10.034976+00:00_

Round 1 审稿任务已派发：
- **Reviewer 1**（方法严谨性 + 实验设计）— 已触发
- **Reviewer 2**（新颖性 + 完整性 + 格式合规）— 已触发

等待两位 Reviewer 返回独立初审意见。收到后将进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 175

## Round 175

2 recorded events


### User

_source line 2334 · 2026-05-19T04:58:05.662331+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 1 审稿意见

**论文**: Strong Predictors, Weak Selectors: Diagnosing and Fixing Self-Consistency for Named Entity Recognition
**Venue**: EMNLP 2026 Main Conference (ARR May 2026)
**审查侧重**: 方法严谨性 + 实验设计

---

## 总体评分

**Overall**: 3 / 5 (Findings)
**Confidence**: 4 / 5
**一句话总结**: 扎实的诊断性实证研究，"correlation-selection gap" 的刻画有价值，但核心方法贡献（entity construction）新颖性有限，且存在若干方法论问题（test-set leakage、post-hoc 阈值优化、非形式化 bound），削弱了 prescriptive claims 的可信度。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5 / 5 | 实验设计整体合理，统计方法恰当，但 LP-alignment gating 存在 test-set information leakage，ε=0.05 non-tied subset 为 post-hoc 最优切点，expected selection gain bound 缺乏形式化推导 |
| **Excitement** | 3 / 5 | 诊断框架有用（negative result 本身有信息量），但 entity-level construction 本质是标准 ensemble 聚合，新颖性有限；4B-8B scale 限制了影响力 |
| **Reproducibility** | 4 / 5 | 训练配置详尽（Appendix C），代码承诺 release，超参完整报告，但部分实验 seed 数量不统一（2-seed vs 3-seed）增加复现难度 |

---

## Must-Fix 问题（影响接收决定）

### N1 [critical] LP-alignment gating 使用 test set 构成 information leakage

- **具体位置**: §4.5 (Prescriptive Results), "LP-alignment gating" 段落
- **问题**: Gating protocol 使用 50 个 test set instances 估计 within-instance ρ(LP, F1)，然后基于该估计选择方法（construction vs LP selection）应用于同一 test set。这构成 information leakage：gating decision 依赖了 test set 的 gold labels（计算 F1 需要 gold），再用该 decision 评估同一 test set 上的性能。
- **论文自述**: "probe instances are drawn from the test set for simplicity; in deployment, a held-out validation set should be used"，但仍 claim "correctly routes all three evaluated datasets"。
- **为什么影响接收**: 这是 prescriptive contribution 的核心（Contribution 3），如果 gating 的 "correct routing" 是 test-set-informed 的，则该 claim 的可信度大幅下降。"Adjusted ρ scores differ by >0.15 across all dataset pairs" 是间接证据，但不能替代正确的 held-out evaluation。
- **建议修改方向**: (a) 在每个 dataset 上用真正的 held-out validation set 重新验证 gating，或 (b) 做 leave-one-dataset-out cross-validation（只有 3 个 dataset 但至少是 clean evaluation），或 (c) 将 gating 降级为 "illustrative proof of concept" 而非 prescriptive claim，并从 Contribution 3 中移除 "correctly routes" 的措辞。

### N2 [critical] Non-tied subset ε=0.05 是 post-hoc 最优切点，叙事权重过高

- **具体位置**: §5 Discussion (Table 6 / tab:nontied_main)；Appendix D.4 (Table 10 / tab:epsilon_sweep)
- **问题**: ε sweep（Table 10）显示 ε=0.05 恰好是 p-value 最小的切点（p=0.004），相邻切点 ε=0.03 (p=0.079) 和 ε=0.10 (p=0.034) 的显著性明显更弱。论文在 Limitations 中称 ε=0.05 为 "post-hoc exploratory choice"，但在主文 Discussion 中将 non-tied subset 结果 (+2.9pp, p=0.004) 作为 LP 携带有用信号的核心证据，还声明该结果 "survives Bonferroni correction over 5 signal comparisons"。
- **为什么影响接收**: Bonferroni 校正应该覆盖 ε sweep 的多重比较（7 个阈值），而非仅覆盖 5 个 signal。校正后 p≈0.028，仍显著但远不如 0.004 convincing。更重要的是，一个 post-hoc 优化的 subset 结果不应作为 narrative 的支柱。
- **建议修改方向**: (a) 对 ε sweep 做 Bonferroni 或 BH 校正并报告校正后 p-value，(b) 在主文中明确标注 ε=0.05 是 sweep 中的最优切点而非独立选择，(c) 降低该结果在叙事中的权重——作为 supportive evidence 而非 primary evidence。

### N3 [critical] Expected selection gain "bound" 缺乏形式化

- **具体位置**: §4.3 "Expected selection gain decomposition"
- **问题**: 论文给出 E[ΔF1] ≤ (1-d) · Δ_oracle · g(ρ_within)，其中 g(·) 被描述为 "monotonically increasing function" 但从未定义。没有定理、引理或证明结构。论文称 "This decomposition is consistent with the observed data"，这是 descriptive fit 而非 predictive bound。
- **为什么影响接收**: 这个 "bound" 在论文中承担重要叙事功能——解释为什么 SciERC selection 失败而 Few-NERD 成功。如果它只是事后的 curve fitting，其解释力有限。使用 "≤" 和 "bounded by" 的语言暗示了比实际更强的理论保证。
- **建议修改方向**: (a) 给出 g(·) 的具体形式并推导 bound（即使是 under simplifying assumptions），或 (b) 将措辞从 "bounded by" 改为 "decomposed as" 或 "heuristically approximated by"，明确说明这是 descriptive framework 而非 formal bound。

---

## Should-Fix 问题（影响评分但不一票否决）

### W1 [warning] Entity construction θ=2/N "tuning-free" claim 证据不充分

- **具体位置**: §4.5, Table 4 (tab:entity_construction)
- **问题**: 论文称 θ=2/N 是 "tuning-free across all datasets"，但没有展示 θ 的 sensitivity analysis。Appendix H.2 (Table 19) 仅对比了 majority voting (k=N/2)，未做 θ 的系统 sweep。如果 θ=2/N 是基于这几个 dataset 的性能选择的，那就是 data snooping。
- **建议**: 补充 θ ∈ {1/N, 2/N, 3/N, ..., (N-1)/N} 的 sweep，展示结果对 θ 的 sensitivity。或者提供 principled justification（如信息论或统计学依据）说明为什么 θ=2/N 是自然选择。

### W2 [warning] SciERC greedy F1 出现 4 个值，协议不统一

- **具体位置**: §3.2 (Evaluation Framework); Tables 2, 3, 4, 14
- **问题**: 同一指标在不同表格中出现 0.640, 0.644, 0.645, 0.650 四个值。论文在 §3.2 给出了解释（seed、epoch、filtering 差异），但这本身说明实验协议不统一。Table 2 用 "2-seed mean"，Table 3 用 "single-seed" (SciERC) 和 "3-seed means" (Few-NERD/CoNLL)，Table 7 (multi-seed) 用 3 seeds。为什么 Table 2 用 2 个 seed 而非 3 个？
- **建议**: (a) 统一 primary analysis 的 seed 数量，(b) 在 Table 2 caption 中解释为什么用 2-seed 而非 3-seed，(c) 考虑在所有主表中使用同一评估协议。

### W3 [warning] 3-seed 统计功效不足以支撑 ranking stability claims

- **具体位置**: §4.4 (Robustness), Table 9 (tab:ranking-stability)
- **问题**: Kendall's W=1.0 基于 m=3 raters，exact p≈0.028。论文称 "interpret with caution given low m"（正确），但主文仍以 "Signal rankings are stable across seeds" 作为 robustness 的关键证据。SciERC LP selection 的 σ=0.48pp（3-seed）相对于效应量（+0.04pp mean）极大，表明 SciERC 结果高度 seed-sensitive。
- **建议**: 增加 seed 数量（至少 5 个），或在主文中更明确地 hedge ranking stability claims。

### W4 [warning] Complementarity claim 基于仅 3 个 dataset

- **具体位置**: §4.5, "Construction and LP selection are complementary"
- **问题**: "Construction and LP selection are complementary, governed by LP-quality alignment" 这一 claim 以及 gating protocol 的 "correct routing" 均基于 3 个 dataset（SciERC, Few-NERD, CoNLL）。3 个数据点不足以支撑 general prescriptive claim。CoNLL 是 ceiling regime，实际上只有 SciERC（construction wins）和 Few-NERD（LP wins）两个 informative data points。
- **建议**: (a) 增加更多 dataset（如 OntoNotes, ACE），或 (b) 将 claim 降级为 "preliminary observation" 而非 prescriptive guideline，或 (c) 在 Contribution 3 中明确标注 dataset 数量限制。

### W5 [warning] 模型规模覆盖仅 3B-8B，claims 表述过于一般化

- **具体位置**: Abstract, Introduction (Contributions), §5 Discussion
- **问题**: Abstract 说 "fine-tuned 4B-8B models"（正确），但 Contribution 2 说 "diagnosing degeneracy and compression as the two blocking mechanisms" 没有限定 scale。Discussion 说 "degeneracy rises with model capability"，但证据仅覆盖 3B-8B。70B+ 模型可能表现出完全不同的 degeneracy-alignment trade-off。
- **建议**: 在 abstract 和 contributions 中加入 "within the 3B-8B range" 的限定。

---

## 小问题（不影响接收）

- **Table D.1 (diversity) "Identical" vs 正文 "Constant F1"**: 概念不同（11% vs 17.8% on SciERC），但容易混淆。建议在 Table D.1 caption 中说明与 degeneracy 定义的区别。
- **Table 4 (entity construction) 缺少 multi-seed ±σ**: Tables 2-3 报告了 ±σ，但 Table 4 没有。补充有助于一致性。
- **WNUT-17 under-analyzed**: Introduction 将其定位为 "signal-collapse boundary"，但在主文中几乎没有出现（仅在 §4.2 提及一句）。建议删除 Introduction 中的角色定位，或在主文中加入适当分析。
- **Figure 1 caption ρ=0.39 vs abstract ρ=0.45**: Figure 1 caption 说 "ρ up to 0.39"，abstract 说 "ρ up to 0.45"。这是因为 Figure 1 只展示 SciERC 而 abstract 覆盖所有 dataset，但对于 "Overview" figure 这一不一致令人困惑。建议在 caption 中说明 scope。
- **Appendix 体量过大**: 1525 行 appendix vs ~220 行主文（不含 table/figure），比例约 7:1。部分分析的信息量有限（如 SJ normalizer comparison Δρ<0.01）。建议精简。

---

## Questions（需要作者澄清）

**Q1**: Table 2 使用 "2-seed mean" 而 Table 3/7 使用 "3-seed"，为什么 selection analysis 的 seed 数量少于 QE analysis？是否有特定原因排除了第 3 个 seed？

**Q2**: Entity construction 的 θ=2/N 是如何确定的？是在看到实验结果之前基于先验理由选择的，还是在多个候选阈值中基于性能选择的？

**Q3**: LP-alignment gating 的 within-instance ρ(LP, F1) 使用了 test set gold labels。如果改用 held-out validation set（不接触 test set gold），routing decision 是否仍然 correct？能否提供这一验证？

**Q4**: Expected selection gain decomposition 中 g(·) 的具体形式是什么？是否有 closed-form 表达式，或是任意满足单调性的函数？

**Q5**: 论文多处使用 "macro F1"（instance-averaged），但 §3.2 evaluation framework 未详细说明计算方式。是 per-instance span-level F1 的 macro average，还是 micro F1？对于只有 1-2 个 gold entities 的 instance，per-instance F1 的方差会很大——这是否影响了 degeneracy 的定义（不同 entity sets 可能碰巧得到相同 F1 值）？

---

## Missing References

- **Minimum Bayes Risk 在 structured prediction 中的应用**: 论文引用了 Eikema et al. (2022, 2025) 和 Freitag et al. (2022)，但遗漏了 MBR 在 NER/IE 任务上的直接应用（如有）。建议搜索 MBR + NER 或 MBR + structured prediction 的近期工作。
- **Entity-level aggregation/ensemble 在 IE 中的先行工作**: Entity construction 本质上是 entity-level ensemble。应引用 NER ensemble 方法（如 Florian et al. 2003, "Named Entity Recognition through Classifier Combination"）以明确增量。
- **Selective prediction 在 NLP 中的应用**: 论文引用了 Geifman & El-Yaniv (2017) 但未引用近期 NLP selective prediction 工作（如 Varshney et al. 2022 已引用，但可补充 Kamath et al. 2020 "Selective Question Answering under Domain Shift"）。

---

## 主要优势

- **诊断框架设计精良**: "Correlation-selection gap" 概念清晰，instance degeneracy 和 LP compression 的双因素分析结构明确。将 QE 和 selection 显式分离是对该领域的有用贡献。
- **实验覆盖广泛**: 5 个 signal、4 个 dataset、3 个 model scale、多个 N 值和 temperature，消融充分（LoRA rank、epoch、free-form decoding、supervised combination、hidden state probes）。
- **Negative results 有价值**: 系统性地证明 selection 失败（包括 supervised combination、DeBERTa verifier、hidden state probes 均失败）比仅报告 positive results 更有信息量。
- **统计方法整体恰当**: MDE 的使用、TOST equivalence testing with external margins、bootstrap CIs 的报告，方法论意识强于多数 NLP 论文。
- **透明度高**: 论文主动解释了 greedy F1 的 4 个值、thinking token confound、epoch confound 等，尽管这些本身是弱点，但透明处理值得肯定。

---

## Overall Assessment

**评分: 3 / 5 (Findings)**
**Confidence: 4 / 5**

这是一篇扎实的诊断性实证研究。"Correlation-selection gap" 的系统刻画对理解 self-consistency 在 structured prediction 中的局限性有真实贡献。但 prescriptive 部分（entity construction + gating）存在方法论问题（N1: test-set leakage, N2: post-hoc threshold, N3: informal bound），且 entity-level construction 本质是标准 ensemble 聚合，新颖性有限。如果作者能修复 N1-N3 并将 prescriptive claims 调整到与证据匹配的强度，可以是一篇好的 Findings 论文。Conference main track 需要更强的方法贡献或更广的 scale 覆盖（70B+）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2335 · 2026-05-19T04:58:13.016449+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 176

## Round 176

2 recorded events


### User

_source line 2336 · 2026-05-19T04:58:26.519770+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿摘要**:

- **Overall: 3/5 (Findings)**，Soundness 3.5，Excitement 3，Confidence 4

**3 个 Critical 问题**:
1. LP-alignment gating 使用 test set gold labels 估计 ρ(LP,F1) 再在同一 test set 上评估，构成 information leakage
2. Non-tied subset 的 ε=0.05 是 ε sweep 中 p-value 最优切点，但叙事中作为核心证据使用且 Bonferroni 校正未覆盖 ε 的多重比较
3. Expected selection gain "bound" 中 g(·) 未定义，无形式化推导，实为 descriptive heuristic 而非 bound

**5 个 Warning 问题**: θ=2/N "tuning-free" 缺证据、greedy F1 四值协议不统一、3-seed 统计功效不足、complementarity claim 仅基于 3 dataset、scale 覆盖仅 3B-8B 但 claims 过于一般化

**主要优势**: 诊断框架设计精良、实验覆盖广、negative results 有价值、统计方法整体恰当、透明度高

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2337 · 2026-05-19T04:58:37.064323+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成审稿后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 177

## Round 177

6 recorded events


### User

_source line 2338 · 2026-05-19T04:59:46.649912+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**论文**: Strong Predictors, Weak Selectors: Diagnosing and Fixing Self-Consistency for Named Entity Recognition
**Venue**: EMNLP 2026 Main Conference (ARR May 2026)
**审查侧重**: 新颖性 + 叙事统一性 + Related Work 质量 + 格式合规 + 写作质量

---

## 总体评分

**Overall**: 3/5 (Findings)
**Confidence**: 4/5 (Quite sure)
**一句话总结**: 实验设计严谨、分析透彻的实证研究，但核心贡献（诊断 + entity-level construction）的新颖性增量有限，不足以支撑 EMNLP main conference。

---

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 4/5 | 实验设计严谨：多种统计检验（bootstrap CI、paired sign test、TOST equivalence、Bonferroni correction），多 seed 验证，消融充分。少数统计问题（见 W2、W3）。 |
| **Excitement** | 2/5 | 核心发现在概念层面缺乏意外性：4/5 signal 是 instance-level 因此不能 rank candidates（定义性而非经验性）；entity-level construction 本质是 entity-level majority voting（已有大量 ensemble NER 工作）。 |
| **Reproducibility** | 4/5 | 训练配置、prompt template、超参数均详细报告（Appendix Table 8）；数据集全部公开可用；constrained decoding 工具已注明。代码承诺 upon acceptance 发布。 |

---

## Summary

本文研究 self-consistency 方法在 NER 任务上的适用性。作者评估了 5 种 confidence signal 在 quality estimation（QE）和 sample selection 两个维度上的表现，发现 QE 表现良好（ρ up to 0.45, AUROC up to 0.82）但 instance-level selection 普遍失败。作者将此命名为 "correlation-selection gap"，归因于两个机制：instance degeneracy（13–87%）和 LP compression。最终提出 entity-level construction（跨 sample 聚合 entity）作为替代方案，在 SciERC (+1.67pp) 和 Few-NERD (+0.88pp) 上取得显著改进。

---

## Strengths

**S1. 实验严谨度高于同类工作。**
多 seed 稳定性分析（Table 7）、bootstrap CI（Appendix Table 5）、TOST equivalence testing（Appendix Table 6）、外部 equivalence margin 分析、MDE 计算——统计方法论层面做到了高水准。在 NER 领域的 self-consistency/confidence 研究中，这种统计严谨度是少见的。

**S2. 系统性的消融设计。**
temperature（4 点）、N-scaling（5 点，N=2 到 32）、model scale（3B/4B/8B）、epoch confound（2–3 点 curve）、LoRA rank、constrained vs. free-form decoding、supervised combination、hidden state probes——每个维度都有对应消融，形成完整的证据网络。

**S3. 问题分解清晰。**
将 quality estimation 和 sample selection 明确分离是一个好的框架选择；correlation-selection gap 的命名虽然在概念上不够新（见 W1），但作为一个具体现象的操作化定义是有用的。

**S4. 负面结果的透明度。**
论文如实报告了大量负面结果（supervised combination 失败、hidden state probe 失败、DALS 效果有限、VerbConf 过度自信），没有隐藏或淡化。Limitations section 覆盖全面（15+ 条限制），这是值得肯定的科学态度。

**S5. 写作质量整体良好。**
无明显 AI 写作痕迹（无 em-dash、无 -ing phrase 结尾、无 "Furthermore/Moreover" 堆叠、无黑名单用词）。技术写作清晰紧凑，术语使用一致。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1** [critical] **Entity-level construction 的新颖性不足**
- 具体位置：§5.5 (Prescriptive Results), Table 4
- 问题：Entity-level construction 本质是 entity-level majority voting：对每个 unique entity mention 统计跨 sample 出现频率，保留超过阈值 θ=2/N 的 entity。这是一个自然且直接的想法，与 ensemble NER（如 Xiao et al. 2025 EL4NER、Naderi et al. 2021 等已有工作）在机制上高度相似——区别仅在于 ensemble 跨模型聚合，本文跨同模型 sample 聚合。LP-weighted 变体相对 uniform voting 的增量极小（SciERC: +1.67 vs +1.54pp; N=16 时两者 converge），说明 LP weighting 的贡献有限。
- 为什么影响接收：这是论文的两大贡献之一（"Fixing" 部分）。如果这部分不具备足够新颖性，论文的 contribution 主要就是诊断性的负面结果，对 main conference 而言贡献量级不够。
- 建议修改方向：更清晰地 articulate entity-level construction 相对于 ensemble NER entity voting 的技术区别（例如：单模型多 sample vs 多模型，是否有不同的 diversity 特征？LP weighting 在 ensemble 设定下是否可行？）。或将 construction 定位为 "applying known technique to confirm it works"，但那就需要 diagnostic 部分有更强的理论贡献来补偿。

**N2** [critical] **Correlation-selection gap 的概念深度有限**
- 具体位置：§4.2 (The Correlation-Selection Gap), §1 Introduction ¶5
- 问题：论文将 4/5 信号是 instance-level（对同一 input 的所有 N 个 candidate 赋同一分数）作为 selection 失败的一个关键原因。但这是这些信号的 **定义性质**，不是经验发现——instance-level signal 按定义不能区分 candidate。论文在 §3.1 已明确指出 "This distinction is consequential for selection"，但随后仍将其作为 "gap" 的组成部分来报告，混淆了定义性限制和经验性发现。真正的经验性发现是：LP（唯一的 per-sample signal）也未能有效 select——这才是 gap 的实质，但它被 4 个 instance-level signal 的"失败"稀释了。
- 为什么影响接收：如果审稿人认为核心发现可归约为 "instance-level metrics 不能 rank candidates（tautological）+ LP 在 constrained decoding 下被压缩（已知现象，Yun et al. 2025, Schall et al. 2025）"，论文的诊断贡献将大幅缩水。
- 建议修改方向：在 framing 上将 instance-level signal 的失败作为 **背景/动机**（"4/5 signals are instance-level and thus cannot rank by construction; LP is the only viable selector"），然后将分析聚焦在 LP selection 为何失败的两个机制上。这样 gap 的概念会更有深度——从 "5 个信号都不行" 变为 "唯一有可能的信号也受限于 degeneracy 和 compression"。

**N3** [critical] **Gating protocol 的 evaluation 使用 test set 作为 probe source**
- 具体位置：§5.5 LP-alignment gating 段落
- 问题：论文承认 "probe instances are drawn from the test set for simplicity; in deployment, a held-out validation set should be used"。但这意味着 gating protocol 的准确性（"correctly routes all three evaluated datasets"）是在 test set 上 evaluated 的，存在信息泄漏。虽然 probe 只用 50 个 instance，且作者指出 adjusted ρ 差距 >0.15，但这仍然是一个方法论上的瑕疵。更重要的是，gating 仅在 3 个 dataset 上验证，且 3 个 dataset 的 ρ 差距很大（SciERC ~0.26, Few-NERD ~0.5-0.7），routing decision 的"正确性"可能只是因为差距足够大，而非 protocol 本身 robust。
- 为什么影响接收：这是 prescriptive contribution 的一部分（"how to decide between construction and LP selection"）。在 3 个 dataset 上用 test set 验证的 gating protocol 的 generalizability 存疑。
- 建议修改方向：至少用 cross-validation 或 development set 重新验证 gating，或明确标注这是 "proof of concept" 而非 deployable protocol（论文已部分这样做，但在 contribution list 中仍然列为贡献之一）。

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **SciERC greedy F1 值不一致，增加理解负担**
- 具体位置：§3.3 最后一段，跨 Tables 1-4
- 问题：论文报告了 4 个不同的 SciERC greedy F1 值（0.640, 0.644, 0.645, 0.650），归因于 "protocol variants: primary seed vs. multi-seed mean, 5-epoch vs. 3-epoch checkpoint, and gold-filtered vs. full test set"。虽然 §3.3 末尾有解释，但读者需要在多个表格间追踪不同的 protocol 才能理解数字差异，显著增加了认知负担。
- 建议：统一使用一个 primary protocol 报告 SciERC 核心结果，将 protocol variant 的差异集中在一个 appendix 表格中说明。

**W2** [warning] **Few-NERD 3-epoch vs 5-epoch 的 confound 未完全消解**
- 具体位置：§4.1 ¶2, Appendix §H (epoch_confound)
- 问题：Few-NERD 使用 3 epochs（其他 dataset 使用 5 epochs），论文的解释是 "earlier convergence"。这引入了一个重要的 confound：LP selection 在 Few-NERD 上的成功可能部分归因于更早的 early stopping 导致的低 degeneracy。Appendix 提供了 2-point ablation（3 vs 5 epoch），但 (a) 5-epoch LP 仍然 positive (+0.62pp)，说明效果方向不变，这是好的；(b) 但 SciERC 的 3-epoch model degeneracy 仅 6.4% 却 LP selection 仍然失败（−1.24pp），说明 degeneracy 不是唯一因素。论文的结论（LP-quality alignment 是主要因素）是合理的，但 Few-NERD 和 SciERC 之间的 epoch 差异仍然是一个混淆变量。
- 建议：在 Limitations 或 Discussion 中更明确地讨论：是否有可能在 matched epoch 条件下比较 Few-NERD 和 SciERC（例如都用 3 epoch）。

**W3** [warning] **Abstract 信息密度过高**
- 具体位置：Abstract（8 行）
- 问题：Abstract 包含 ρ=0.45, AUROC 0.82, +5–8pp, +1.39pp, p<0.001, 13–87%, ρ=0.052, 23 configurations, +0.88, +1.67pp, p<0.005 等大量数字。这使得 Abstract 读起来像实验报告的压缩版，而非论文故事的精炼概述。审稿人在 30 秒内难以从这些数字中提取核心 message。
- 建议：保留 2-3 个关键数字（如 construction 的增益和 p-value），将其余数字移入正文。

**W4** [warning] **Selective prediction 贡献的定位不清晰**
- 具体位置：§5.5 Selective prediction 段落, Contribution #1
- 问题：Selective prediction（基于 QE score 过滤低置信度 instance，80% coverage 下 +5–8pp）在 Contribution #1 中被列出，但这本质是 QE signal 的直接应用，不是本文的方法创新。任何能预测 instance quality 的 signal 都可以做 selective prediction。将此列为贡献会稀释真正的贡献点。
- 建议：将 selective prediction 作为 QE signal 实用性的一个 demonstration，而非独立贡献。

**W5** [warning] **模型规模范围有限（4B–8B），对结论普适性的影响**
- 具体位置：Limitations ¶2
- 问题：论文仅覆盖 3B–8B 规模的 fine-tuned models，且 Discussion §5 指出 "degeneracy rises with model capability"，暗示 70B+ 模型可能情况更糟（degeneracy 更高）。但同时，更大模型可能有更好的 LP-quality alignment，这两个因素的交互效应未知。论文在 Limitations 中承认了这一点，但这限制了结论的适用范围。
- 建议：在 Limitations 中增加对 70B+/closed-source API 场景的具体讨论（例如：closed-source API 通常不提供 LP，因此 construction 可能是唯一可行方案——这实际上强化了 construction 的贡献）。

---

## Questions（需要作者澄清）

**Q1.** Entity-level construction 中 θ=2/N 是 "tuning-free" 的，但 θ=0.5（majority voting baseline）的结果在 Appendix 中。能否提供 θ 在 [1/N, 1] 范围内的敏感性分析？θ=2/N 在 N=8 时等于 0.25，这比 majority voting 的 0.5 低很多。这个较低的阈值本质上是在 boost recall 的同时可能降低 precision——能否提供 construction 的 precision/recall 分解来验证？

**Q2.** 论文在 §1 中声称提供 "the first systematic empirical characterization of when and why LP-based selection succeeds or fails for structured prediction"。但 Yao et al. 2026 已经研究了 consistency-accuracy correlation for entity and relation extraction，且 Vashurin et al. 2025 (CoCoA) 结合了 confidence 和 consistency。能否更精确地界定 "first" 的 scope？

**Q3.** Qwen3-8B SciERC checkpoint 使用了空的 `&lt;think>&lt;/think>` blocks（Appendix §E）。虽然论文通过三个论证排除了影响，但这本身是一个不理想的实验设计。为什么不重新训练一个 clean checkpoint？

**Q4.** Within-instance LP-quality alignment（ρ≈0.26 on SciERC vs ≈0.5-0.7 on Few-NERD）的差异是否可能由 entity type 数量差异驱动（SciERC 6 types vs Few-NERD 8 types）？或者由 train/test distribution shift 驱动？

---

## Missing References

1. **Entity-level aggregation in NER**: 论文引用了 Xiao et al. 2025 (EL4NER) 作为 ensemble NER 的代表，但缺少对 entity-level voting 机制本身的更广泛文献覆盖。例如：
   - Ratinov & Roth 2009 讨论了 NER 的 ensemble strategies（论文在 appendix 中引用了此文但未在 entity-level voting 的语境下讨论）
   - Luo et al. 2023 (Zero-shot NER with ChatGPT) 中的 self-annotation + voting 机制

2. **MBR decoding for structured prediction**: Eikema et al. 2025 已被引用，但 Wiher et al. 2022 ("On Decoding Strategies for Neural Text Generators") 提供了 MBR 与 MAP decoding 在多种 NLG 任务上的对比，对 selection-gap 的讨论有补充价值。

3. **Test-time compute scaling 的最新进展**: 考虑引用 Muennighoff et al. 2025 ("s1: Simple Test-Time Scaling") 或 Qu et al. 2025 ("Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning")，因为这些工作进一步探讨了 test-time scaling 在不同任务上的适用性。

---

## 格式合规检查

| 检查项 | 状态 | 备注 |
|--------|------|------|
| ACL 模板 (`\usepackage[review]{acl}`) | ✅ | 正确使用 review 模式 |
| 匿名 (`\author{Anonymous}`) | ✅ | |
| 正文 ≤8 页 | ⚠️ | 需要确认。正文包含 Abstract + 5 sections + Limitations，其中 Experiments 和 Introduction 都包含大表格和图表。内容密度极高，可能在边界。Discussion 仅 11 行 tex，Conclusion 仅 7 行——这些被压缩以腾出空间给 Experiments，说明正文空间非常紧张。 |
| Limitations section | ✅ | 在 Conclusion 之后，内容全面（15+ 条限制） |
| Ethics Statement | ✅ | |
| Responsible NLP Checklist | ✅ | 认真填写，无全 N/A |
| 行号 | ✅ | `[review]` 选项启用 |
| 缩写定义（Abstract 内） | ✅ | NER, QE, AUROC, LP 均在 Abstract 内展开定义 |
| 引用格式 | ✅ | `\cite` 和 `\citep`/`\citet` 使用一致（parenthetical vs textual） |
| 引用覆盖 | ✅ | 73 条 bib 条目，69 条被引用；4 条 orphan bib entries（eisenstein2023helping, li2025llms, naderi2021ensemble, sarcinelli2025local）不影响论文 |
| 引用真实性 | ✅ | OpenAlex 验证：64 条 verified，4 条 not found（可能为最新 preprint），5 条 minor mismatch（first_author 格式差异或 year 差异）。无 fake citation。 |

---

## 写作质量检查

| 检查项 | 状态 | 备注 |
|--------|------|------|
| Em-dash (—) | ✅ | 仅在 .bib 注释中出现一次，正文无 |
| En-dash 解释性用法 ( – ) | ✅ | 无 |
| \textendash | ✅ | 仅用于数值范围（4B–8B, 13–87%），用法正确 |
| -ing phrase 结尾 | ✅ | 未检出 |
| 过度分段 | ✅ | 段落长度适中 |
| 黑名单用词 (leverage/utilize/delve/myriad/plethora) | ✅ | 未检出 |
| 连续过渡词 (Furthermore/Moreover/Additionally) | ✅ | 未检出 |

---

## 主要优势总结

1. 统计方法论严谨度在 NER/IE 领域罕见（多重检验校正、equivalence testing、外部 margin 等）
2. 消融设计系统完整，形成闭环的证据网络
3. 负面结果的透明报告（6+ negative experiments: supervised combination, hidden probes, DeBERTa verifier, DALS, VerbConf, calibration baseline）
4. 写作质量高，无 AI 痕迹，技术表述清晰
5. Limitations section 堪称范例（覆盖全面、诚实、有具体建议）

---

## Overall Assessment

**3/5 — Findings**

本文是一篇高质量的实证分析论文，实验设计和统计方法论的严谨度远高于同类工作。核心问题（self-consistency 如何适用于 structured IE）有实际意义。

但两个核心贡献的新颖性存在疑虑：
- **Diagnostic**: correlation-selection gap 的概念中，4/5 signal 的失败是定义性的（instance-level signal 不能 rank candidates），LP 在 constrained decoding 下的压缩是已知现象。Instance degeneracy 的 operationalization 有价值，但概念层面并不 surprising。
- **Prescriptive**: entity-level construction 本质是 entity-level majority voting（well-known in ensemble NER），LP weighting 的增量贡献微小。

论文更适合 Findings track：分析透彻、实验扎实、对 practitioner 有直接参考价值，但概念创新不足以进入 main conference。如果作者能在 rebuttal 中 (a) 更清晰地 differentiate entity-level construction 与已有 ensemble NER voting，(b) 提供 gating protocol 的 proper validation（non-test-set probe），(c) 深化 correlation-selection gap 的理论解释（而非仅仅是 "degeneracy + compression" 的实证组合），评分有上调空间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2339 · 2026-05-19T05:00:23.674219+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你与 Reviewer 2 在以下问题上是否存在分歧：\n- Entity-level construction 的新颖性评估（R2-N1 vs 你的立场）\n- Correlation-selection gap 的概念深度（R2-N2）\n- Selective prediction 是否应列为独立贡献（R2-W4）\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Must-Fix 问题\n\n**N1** [critical] **Entity-level construction 的新颖性不足**\n- Entity-level construction 本质是 entity-level majority voting：对每个 unique entity mention 统计跨 sample 出现频率，保留超过阈值 θ=2/N 的 entity。与 ensemble NER（如 Xiao et al. 2025 EL4NER、Naderi et al. 2021）在机制上高度相似——区别仅在于 ensemble 跨模型聚合，本文跨同模型 sample 聚合。LP-weighted 变体相对 uniform voting 的增量极小（SciERC: +1.67 vs +1.54pp; N=16 时两者 converge），说明 LP weighting 的贡献有限。\n- 这是论文的两大贡献之一（\"Fixing\" 部分）。如果不具备足够新颖性，论文的 contribution 主要就是诊断性的负面结果，对 main conference 而言贡献量级不够。\n\n**N2** [critical] **Correlation-selection gap 的概念深度有限**\n- 4/5 信号是 instance-level（对同一 input 的所有 N 个 candidate 赋同一分数），这是定义性质而非经验发现。论文在 §3.1 已指出 \"This distinction is consequential for selection\"，但随后仍作为 \"gap\" 的组成部分报告。真正的经验性发现是：LP（唯一的 per-sample signal）也未能有效 select。\n- 建议将 instance-level signal 的失败作为背景/动机，然后将分析聚焦在 LP selection 为何失败的两个机制上。\n\n**N3** [critical] **Gating protocol 使用 test set 作为 probe source**\n- 与你的 N1 一致。\n\n### Should-Fix 问题\n\n**W1** [warning] SciERC greedy F1 值不一致（4 个值），增加理解负担\n**W2** [warning] Few-NERD 3-epoch vs 5-epoch confound 未完全消解\n**W3** [warning] Abstract 信息密度过高，读起来像实验报告压缩版\n**W4** [warning] Selective prediction 是 QE 的直接应用，不应列为独立贡献\n**W5** [warning] 模型规模 4B–8B，结论普适性受限\n\n### 主要优势\nS1. 统计严谨度高于同类; S2. 消融系统完整; S3. 问题分解清晰; S4. 负面结果透明; S5. 写作质量好\n\n### Overall: 3/5 (Findings), Confidence 4/5",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你与 Reviewer 2 在以下问题上是否存在分歧：\n- Entity-level construction 的新颖性评估（R2-N1 vs 你的立场）\n- Correlation-selection gap 的概念深度（R2-N2）\n- Selective prediction 是否应列为独立贡献（R2-W4）\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Must-Fix 问题\n\n**N1** [critical] **Entity-level construction 的新颖性不足**\n- Entity-level construction 本质是 entity-level majority voting：对每个 unique entity mention 统计跨 sample 出现频率，保留超过阈值 θ=2/N 的 entity。与 ensemble NER（如 Xiao et al. 2025 EL4NER、Naderi et al. 2021）在机制上高度相似——区别仅在于 ensemble 跨模型聚合，本文跨同模型 sample 聚合。LP-weighted 变体相对 uniform voting 的增量极小（SciERC: +1.67 vs +1.54pp; N=16 时两者 converge），说明 LP weighting 的贡献有限。\n- 这是论文的两大贡献之一（\"Fixing\" 部分）。如果不具备足够新颖性，论文的 contribution 主要就是诊断性的负面结果，对 main conference 而言贡献量级不够。\n\n**N2** [critical] **Correlation-selection gap 的概念深度有限**\n- 4/5 信号是 instance-level（对同一 input 的所有 N 个 candidate 赋同一分数），这是定义性质而非经验发现。论文在 §3.1 已指出 \"This distinction is consequential for selection\"，但随后仍作为 \"gap\" 的组成部分报告。真正的经验性发现是：LP（唯一的 per-sample signal）也未能有效 select。\n- 建议将 instance-level signal 的失败作为背景/动机，然后将分析聚焦在 LP selection 为何失败的两个机制上。\n\n**N3** [critical] **Gating protocol 使用 test set 作为 probe source**\n- 与你的 N1 一致。\n\n### Should-Fix 问题\n\n**W1** [warning] SciERC greedy F1 值不一致（4 个值），增加理解负担\n**W2** [warning] Few-NERD 3-epoch vs 5-epoch confound 未完全消解\n**W3** [warning] Abstract 信息密度过高，读起来像实验报告压缩版\n**W4** [warning] Selective prediction 是 QE 的直接应用，不应列为独立贡献\n**W5** [warning] 模型规模 4B–8B，结论普适性受限\n\n### 主要优势\nS1. 统计严谨度高于同类; S2. 消融系统完整; S3. 问题分解清晰; S4. 负面结果透明; S5. 写作质量好\n\n### Overall: 3/5 (Findings), Confidence 4/5",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2340 · 2026-05-19T05:00:47.980871+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24306
}
```

</details>

---


### Tool call

_source line 2341 · 2026-05-19T05:00:48.232202+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你与 Reviewer 1 在以下问题上是否存在分歧：\n- ε=0.05 non-tied subset 的叙事权重（R1-N2）——你是否认为这是同等严重的问题？\n- Expected selection gain bound 的形式化程度（R1-N3）——你对 \"bound\" vs \"heuristic\" 的判断？\n- θ=2/N \"tuning-free\" claim（R1-W1）——你是否同意需要 sensitivity sweep？\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Must-Fix 问题\n\n**N1** [critical] **LP-alignment gating 使用 test set 构成 information leakage**\n- Gating protocol 使用 50 个 test set instances 估计 within-instance ρ(LP, F1)，然后基于该估计选择方法应用于同一 test set。Gold labels 参与了 gating decision。\n- 建议：(a) held-out validation set 重新验证，或 (b) leave-one-dataset-out CV，或 (c) 降级为 \"illustrative proof of concept\"。\n\n**N2** [critical] **Non-tied subset ε=0.05 是 post-hoc 最优切点，叙事权重过高**\n- ε sweep（Table 10）显示 ε=0.05 恰好是 p-value 最小的切点（p=0.004），相邻切点显著性更弱。Bonferroni 校正应覆盖 ε sweep 的多重比较（7 个阈值），而非仅覆盖 5 个 signal。\n- 建议：对 ε sweep 做 Bonferroni/BH 校正，降低该结果在叙事中的权重。\n\n**N3** [critical] **Expected selection gain \"bound\" 缺乏形式化**\n- E[ΔF1] ≤ (1-d) · Δ_oracle · g(ρ_within)，其中 g(·) 被描述为 \"monotonically increasing function\" 但从未定义。没有定理、引理或证明。\n- 建议：给出 g(·) 具体形式并推导，或将 \"bounded by\" 改为 \"decomposed as\"/\"heuristically approximated by\"。\n\n### Should-Fix 问题\n\n**W1** [warning] Entity construction θ=2/N \"tuning-free\" claim 缺证据——无 θ sensitivity sweep\n**W2** [warning] SciERC greedy F1 出现 4 个值，协议不统一（Table 2 用 2-seed vs Table 3/7 用 3-seed）\n**W3** [warning] 3-seed 统计功效不足以支撑 ranking stability claims（Kendall's W=1.0, m=3）\n**W4** [warning] Complementarity claim 仅基于 3 个 dataset（实际仅 2 个 informative data points）\n**W5** [warning] 模型规模覆盖仅 3B-8B，claims 表述过于一般化\n\n### 小问题\n- Table D.1 diversity \"Identical\" vs \"Constant F1\" 概念混淆\n- Table 4 缺少 multi-seed ±σ\n- WNUT-17 under-analyzed\n- Figure 1 caption ρ=0.39 vs Abstract ρ=0.45 scope 不一致\n- Appendix 体量过大（7:1 ratio）\n\n### 主要优势\n诊断框架设计精良; 实验覆盖广; negative results 有价值; 统计方法恰当; 透明度高\n\n### Overall: 3/5 (Findings), Confidence 4/5",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你与 Reviewer 1 在以下问题上是否存在分歧：\n- ε=0.05 non-tied subset 的叙事权重（R1-N2）——你是否认为这是同等严重的问题？\n- Expected selection gain bound 的形式化程度（R1-N3）——你对 \"bound\" vs \"heuristic\" 的判断？\n- θ=2/N \"tuning-free\" claim（R1-W1）——你是否同意需要 sensitivity sweep？\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Must-Fix 问题\n\n**N1** [critical] **LP-alignment gating 使用 test set 构成 information leakage**\n- Gating protocol 使用 50 个 test set instances 估计 within-instance ρ(LP, F1)，然后基于该估计选择方法应用于同一 test set。Gold labels 参与了 gating decision。\n- 建议：(a) held-out validation set 重新验证，或 (b) leave-one-dataset-out CV，或 (c) 降级为 \"illustrative proof of concept\"。\n\n**N2** [critical] **Non-tied subset ε=0.05 是 post-hoc 最优切点，叙事权重过高**\n- ε sweep（Table 10）显示 ε=0.05 恰好是 p-value 最小的切点（p=0.004），相邻切点显著性更弱。Bonferroni 校正应覆盖 ε sweep 的多重比较（7 个阈值），而非仅覆盖 5 个 signal。\n- 建议：对 ε sweep 做 Bonferroni/BH 校正，降低该结果在叙事中的权重。\n\n**N3** [critical] **Expected selection gain \"bound\" 缺乏形式化**\n- E[ΔF1] ≤ (1-d) · Δ_oracle · g(ρ_within)，其中 g(·) 被描述为 \"monotonically increasing function\" 但从未定义。没有定理、引理或证明。\n- 建议：给出 g(·) 具体形式并推导，或将 \"bounded by\" 改为 \"decomposed as\"/\"heuristically approximated by\"。\n\n### Should-Fix 问题\n\n**W1** [warning] Entity construction θ=2/N \"tuning-free\" claim 缺证据——无 θ sensitivity sweep\n**W2** [warning] SciERC greedy F1 出现 4 个值，协议不统一（Table 2 用 2-seed vs Table 3/7 用 3-seed）\n**W3** [warning] 3-seed 统计功效不足以支撑 ranking stability claims（Kendall's W=1.0, m=3）\n**W4** [warning] Complementarity claim 仅基于 3 个 dataset（实际仅 2 个 informative data points）\n**W5** [warning] 模型规模覆盖仅 3B-8B，claims 表述过于一般化\n\n### 小问题\n- Table D.1 diversity \"Identical\" vs \"Constant F1\" 概念混淆\n- Table 4 缺少 multi-seed ±σ\n- WNUT-17 under-analyzed\n- Figure 1 caption ρ=0.39 vs Abstract ρ=0.45 scope 不一致\n- Appendix 体量过大（7:1 ratio）\n\n### 主要优势\n诊断框架设计精良; 实验覆盖广; negative results 有价值; 统计方法恰当; 透明度高\n\n### Overall: 3/5 (Findings), Confidence 4/5",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2342 · 2026-05-19T05:00:49.749905+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1517
}
```

</details>

---


### Assistant

_source line 2343 · 2026-05-19T05:00:52.155207+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 178

## Round 178

2 recorded events


### User

_source line 2344 · 2026-05-19T05:00:54.817227+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3/5 (Findings)**。

三个 critical 问题：
1. Entity-level construction 的新颖性有限——本质是 entity-level majority voting，与已有 ensemble NER 工作（EL4NER 等）机制高度相似，LP-weighting 增量微小
2. Correlation-selection gap 概念的深度不够——4/5 signal 的失败是定义性的（instance-level 不能 rank candidates），LP compression 是已知现象
3. Gating protocol 使用 test set probe + 仅 3 dataset 验证，方法论上有瑕疵

主要优势：统计严谨度在同领域罕见，消融设计系统完整，负面结果透明报告，写作质量高（无 AI 痕迹），格式合规无问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2345 · 2026-05-19T05:01:00.723531+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 179

## Round 179

2 recorded events


### User

_source line 2346 · 2026-05-19T05:01:48.121924+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 交叉回应 — 针对 Reviewer 2 审稿意见

---

## Must-Fix 问题回应

### [AGREE] R2-N1: Entity-level construction 的新颖性不足

同意 R2 的核心判断。我在自己的审稿中也将 entity construction 的新颖性列为 excitement 降分的主要原因。

补充几点支撑：
- 论文自身在 Related Work §2 承认 "Ensemble approaches aggregate predictions from multiple models or prompts (Xiao et al. 2025); our entity-level construction similarly aggregates across samples from a single model, without requiring model diversity"。这等于作者自己承认机制相似，区别仅在 sample source。
- Table 4 的数据进一步支持 R2 的论点：LP-weighted vs Uniform 在 SciERC 上仅差 0.13pp（1.67 vs 1.54），在 N=16 时 converge（§4.5 最后一段明确写道 "at N=16, LP-weighting and uniform converge"）。这说明 LP weighting 的贡献确实 marginal。
- 不过我认为 R2 的判断 "contribution 主要就是诊断性的负面结果" 稍有低估——诊断框架本身（QE vs selection 的显式分离、degeneracy 和 compression 的双因素刻画）是有价值的方法论贡献，即使 "fix" 部分新颖性不足。一篇以诊断为主的论文可以是好的 Findings 论文，但 main conference 确实需要更强的解决方案。

### [AGREE with nuance] R2-N2: Correlation-selection gap 的概念深度有限

部分同意。R2 指出 4/5 signal 是 instance-level 这一事实是定义性质而非经验发现——这个观察是正确的。论文在 §3.1 已经建立了 per-sample vs instance-level 的区分，所以 instance-level signal 无法 rank candidates 是逻辑推论，不应作为 "gap" 的核心内容。

但我认为 R2 略微低估了以下经验性发现的价值：
1. **LP 也失败**是非 trivial 的经验发现。LP 是 per-sample signal，理论上可以 rank candidates，但在 SciERC 上效应量仅 +0.2pp（§4.3, Table 2）。这不是定义推出的。
2. **Instance degeneracy 和 LP compression 的交互**是经验性的：Table 6 (tab:t_degeneracy) 显示 temperature 可以降低 degeneracy（41.4%→14.9%）但不能改善 LP-quality alignment（ρ=0.225 vs Few-NERD ~0.5），从而 disentangle 了两个因素。这是有信息量的实验设计。
3. **Degeneracy 不能跨 dataset 预测 LP 方向**（ρ=0.052, 23 configurations, Figure 3）也是经验性的，反驳了 "降低 degeneracy 就能恢复 selection" 的直觉假设。

建议的调整方向与 R2 一致：将 instance-level signal 失败作为背景动机（因为是定义推论），将分析焦点放在 LP 为何失败（compression + alignment）上。这样 "gap" 的 framing 更诚实。

### [AGREE] R2-N3: Gating protocol 使用 test set

完全同意，与我的 N1 一致。不再赘述。

---

## Should-Fix 问题回应

### [AGREE] R2-W1: SciERC greedy F1 值不一致

与我的 W2 一致。4 个值（0.640, 0.644, 0.645, 0.650）虽有解释（§3.2），但本身反映协议不统一。特别是 Table 2 用 "2-seed mean" 而 Table 3 用 "single-seed"/"3-seed means" 的不一致缺乏解释。

### [REBUT] R2-W2: Few-NERD 3-epoch vs 5-epoch confound 未完全消解

不完全同意。论文在 Appendix E (Table 13, tab:epoch_confound) 提供了充分的消解分析：
- **3-epoch 选择有明确依据**: 论文指出 evaluation loss 在 epoch 3 后上升（0.032→0.041 at epoch 5），best checkpoint by validation loss 在 step 32,000（约 epoch 3.9）。这是标准 early stopping practice，不是 arbitrary choice。
- **5-epoch ablation 结果方向一致**: 5-epoch 模型 LP selection 仍然 positive（+0.62pp vs 3-epoch +1.37pp），只是因为 degeneracy 升高（11.1%→31.3%）而效应量减半。这恰好支持了论文的 degeneracy 叙事。
- **SciERC 提供了 3-point epoch curve**（Table 15, tab:epoch_scierc）：3/5/10 epochs 的 degeneracy 单调递增（6.4%→17.8%→47.8%），within-instance alignment 同步退化（median ρ: 0.319→0.262→0.112），展示了清晰的 convergence-degeneracy gradient。

我认为 epoch confound 已经 adequately addressed。如果有不足，是 CoNLL epoch variation 未验证（论文在 Appendix E limitations 段承认了这一点），但这不影响 Few-NERD 的主要结论。

### [AGREE with nuance] R2-W3: Abstract 信息密度过高

同意 abstract 信息密度偏高——数字过多（ρ=0.45, AUROC=0.82, +5-8pp, +1.39pp, 13-87%, ρ=0.052, +0.88 to +1.67pp, p<0.005），读起来确实像实验报告压缩版。按 CLAUDE.md paper-writing-norms §2.1，abstract 应 "用最少篇幅讲完故事"，"最多引用 2-3 个关键数字"。当前 abstract 引用了约 10 个数字。

但我也注意到 abstract 确实回答了 "四个必答问题"（问题、重要性、方法、结果），结构是正确的。问题在于数字堆砌，不在于叙事逻辑。

### [REBUT] R2-W4: Selective prediction 不应列为独立贡献

不同意。仔细看 Contribution 1 的原文（§1）：

> "Five signals from three families evaluated on four NER benchmarks, two model families, and a 4B ablation, achieving reliable quality estimation (ρ up to 0.45, AUROC up to 0.82). QE enables selective prediction: filtering low-confidence instances at 80% coverage yields +5--8 pp F1"

Selective prediction 不是独立的 Contribution——它是 Contribution 1 (Quality Estimation Framework) 的一部分，作为 QE 的实际应用价值论证。论文没有将 selective prediction 单列为 Contribution 2 或 3。从叙事角度看，包含 selective prediction 是合理的：如果 QE 信号可靠但不能用于任何 downstream task，那 QE 的价值就大打折扣。Selective prediction (+5-8pp at 80% coverage, Table 8/cross_selection) 证明 QE 有实用价值，即使 selection 失败。

R2 的建议 "不应列为独立贡献" 似乎基于对 contribution 结构的误读——selective prediction 在原文中已经是 Contribution 1 的子项而非独立贡献。

### [AGREE] R2-W5: 模型规模 4B-8B，结论普适性受限

与我的 W5 一致。特别是 Discussion 中 "degeneracy rises with model capability" 的 trend claim（§5, Tables 5/13/15）仅基于 3B-8B 的证据，如果要外推到 70B+，需要更多 hedging。

---

## 综合判断

与 R2 的 overall assessment 一致：**3/5 (Findings), Confidence 4/5**。

关键分歧：
1. **R2-W2 (epoch confound)**: 我认为已 adequately addressed，R2 可能未充分考虑 Appendix E 的 3-point SciERC curve。
2. **R2-W4 (selective prediction)**: R2 似乎误将 selective prediction 视为独立贡献，但原文中它是 Contribution 1 的子项。
3. **R2-N2 (gap 概念深度)**: 我部分同意但认为 R2 低估了 LP 失败的经验价值和 degeneracy-alignment disentanglement 的实验设计贡献。

共识点：N1 (construction novelty)、N3 (test-set leakage)、W1 (greedy F1 inconsistency)、W3 (abstract density)、W5 (scale limitation) 均一致。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2347 · 2026-05-19T05:01:52.295572+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 180

## Round 180

2 recorded events


### User

_source line 2348 · 2026-05-19T05:02:02.309025+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心判断：

- **3 项共识**: construction 新颖性不足 (N1)、test-set leakage (N3)、scale 限制 (W5)
- **2 项分歧**: epoch confound 我认为已充分消解 (W2 REBUT)；selective prediction 在原文中并非独立贡献而是 Contribution 1 的子项 (W4 REBUT)
- **1 项 nuance**: correlation-selection gap 的概念深度——instance-level signal 失败确实是定义推论，但 LP 失败和 degeneracy-alignment disentanglement 是非 trivial 的经验发现 (N2 部分同意)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2349 · 2026-05-19T05:02:07.695467+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 181

## Round 181

8 recorded events


### User

_source line 2350 · 2026-05-19T05:02:41.668688+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1 的审稿意见

---

### Must-Fix 问题回应

**[AGREE] R1-N1: LP-alignment gating 使用 test set 构成 information leakage**

同意。这与我的 N3 完全一致。§5.5 LP-alignment gating 段落承认 "probe instances are drawn from the test set for simplicity"，但论文仍将 gating protocol 列为 Contribution #3 的一部分（"an alignment-based gating protocol correctly routes all three evaluated datasets"）。Gold F1 labels 参与了 gating decision，这不仅是 information leakage，更是让 gating 的"正确性"无法被信任。

补充：论文自己写了三条 caveats (a)(b)(c)，实际上已经承认了这个问题。建议同 R1：要么用 proper validation set 重新验证，要么在 Contribution list 中明确降级为 "proof of concept"，不作为独立贡献列出。

---

**[AGREE] R1-N2: Non-tied subset ε=0.05 是 post-hoc 最优切点，叙事权重过高**

同意这是一个真实问题，但我对严重程度的判断与 R1 略有不同。

**同意的部分**：Table 10（ε sweep）确实显示 ε=0.05 恰好是 p-value 最小的切点（p=0.004），且论文在 Appendix §F 已标注这是 "post-hoc exploratory analysis"。但主文 §4.2 中的措辞（"the sole positive finding, non-tied LP subset +2.9pp p=0.004, survives Bonferroni correction"）中的 Bonferroni correction 仅覆盖 5 个 signal comparisons，未覆盖 ε sweep 的 7 个阈值。如果做 7×5=35 的 Bonferroni correction，p_adj = 0.004 × 35 = 0.14，不再显著。R1 的批评在统计层面是正确的。

**不完全同意的部分**：论文在 §F 第一段已明确将 ε=0.05 定义为 "post-hoc exploratory choice"，且 Table 9 的 ε robustness 分析显示 selection F1 本身在 ε ∈ [0, 0.2] 范围内变化不大（consistency signals ≤1.09pp）。所以这个结果的叙事功能更多是 "characterizing the compression phenomenon" 而非 "demonstrating a tuned selection strategy"——论文的 Limitations section 第11段已明确这一点。问题不在于结果本身，而在于主文 §4.2 的措辞（"survives Bonferroni correction"）给读者一种该结果已经充分校正的印象。

**建议**：(a) 将主文中 "survives Bonferroni correction" 改为明确说明 Bonferroni 范围（仅 5 signals，未含 ε sweep）；(b) 将 non-tied subset 的讨论从 §4.2 移至 Discussion 或 Appendix，降低叙事权重；(c) 补充 ε sweep 的 BH correction 结果。

---

**[AGREE with reservation] R1-N3: Expected selection gain "bound" 缺乏形式化**

同意方向，但对严重程度的判断比 R1 宽容。

**同意的部分**：§4.2 中的 E[ΔF1] ≤ (1-d) · Δ_oracle · g(ρ_within) 确实不是一个形式化的 bound。g(·) 被描述为 "monotonically increasing function" 但从未给出具体形式或推导。在数学上，一个包含未定义函数的不等式不构成 bound——它更接近一个 conceptual decomposition。

**保留意见**：这个 "bound" 在论文中的角色是 **组织叙事**而非提供理论保证。它帮助读者理解三个因素（degeneracy、oracle headroom、LP alignment）如何交互影响 selection gain，并且论文确实用 3 个 dataset 的实际数据验证了 decomposition 的一致性（§4.2 第101行）。如果将 "bounded by" 改为 "decomposed as" 或 "heuristically characterized by"，这个框架的诊断价值不变。与 R1 不同的是，我不认为这需要正式定理/证明——这是一篇实证论文，不是理论论文。要求形式化推导可能超出了论文的 scope。

**建议**：将 "bounded by" 改为 "heuristically decomposed as"，并在脚注中说明 g(·) 的具体假设（例如 g(0)=0, g(1)=1，或引用 decision-theoretic framework 来 justify monotonicity）。

---

### Should-Fix 问题回应

**[AGREE] R1-W1: Entity construction θ=2/N "tuning-free" claim 缺乏 θ sensitivity sweep**

同意。这也是我在 Q1 中提出的问题。§5.5 声称 θ=2/N 是 "tuning-free across all datasets"，但仅提供了 θ=0.5（majority baseline）作为对比（提及 Appendix），没有展示 θ 在 [1/N, 1] 范围内的 sensitivity curve。θ=2/N 在 N=8 时等于 0.25，比 majority voting 的 0.5 低很多——这本质上是在大幅 boost recall（任何在 ≥2/8 个 sample 中出现的 entity 都被保留），可能在某些 high-noise 场景下引入大量 false positives。没有 precision/recall 分解和 θ sweep，"tuning-free" 的 claim 不成立。

---

**[AGREE] R1-W2: SciERC greedy F1 的 4 个值增加理解负担**

同意，与我的 W1 一致。§3.3 末尾的解释（"protocol variants: primary seed vs. multi-seed mean, 5-epoch vs. 3-epoch checkpoint, and gold-filtered vs. full test set"）虽然存在，但分散在正文最后，而非在第一次出现不一致数值时就说明。建议统一一个 primary protocol，差异集中在 appendix 说明。

---

**[AGREE] R1-W3: 3-seed 统计功效不足以支撑 ranking stability claims**

同意。Appendix Table 12 报告 Kendall's W=1.0（m=3 raters），论文自己也注明 "interpret with caution given low m; exact p≈0.028"。但 m=3 时 W=1.0 的含义仅仅是 3 个 seed 碰巧给出了相同排名——这在很大程度上可能是偶然的，尤其是在 top signals（VC vs SJ）差距很小（Δρ=0.019，bootstrap CI 跨零；Appendix Table 5）的情况下。论文应将这一结果明确标注为 "descriptive" 而非 "robust stability evidence"。

---

**[AGREE] R1-W4: Complementarity claim 仅基于 3 个 dataset（实际仅 2 个 informative data points）**

同意。CoNLL 因 ceiling effect 两种方法都不 work，不构成 informative data point。实际上 complementarity 的证据来自 2 个 dataset：SciERC（construction 好）和 Few-NERD（LP selection 好）。2 个 data point 不足以支撑 "complementarity governed by LP-quality alignment" 的 general claim——可能只是两个不同 dataset 上的巧合。但这个 limitation 在论文中已有 partial acknowledgment（gating 的 caveat (b)），所以问题更多是措辞力度而非实验缺陷。

---

**[AGREE] R1-W5: 模型规模覆盖仅 3B-8B**

同意，与我的 W5 一致。论文的 claims（如标题 "Diagnosing and Fixing Self-Consistency for NER"）暗示了比实验覆盖更广的适用范围。但 70B+ 规模下的行为可能根本不同：(a) degeneracy 可能更高（论文自己的 scale ablation 显示 8B > 4B > 3B 的 degeneracy），(b) 但 LP-quality alignment 可能也更强，(c) 更大模型可能根本不需要 multi-sample improvement 因为 greedy 已经很好。建议将 claims 限定为 "4B–8B fine-tuned models" 范围。

---

### 小问题回应

**[AGREE] Table D.1 diversity "Identical" vs "Constant F1" 概念混淆**

同意。Table D.1 的 "Identical" 定义为 "fraction of instances with all N outputs identical"（string-level），而主文中的 "instance degeneracy" 定义为 "constant F1"（F1-level）。两个概念不同（相同 F1 不意味着相同 output），但交替使用可能误导读者。例如 Qwen/SciERC "Identical"=11% vs "Constant F1"=17.8%（Table D.2）——差异 6.8pp 说明确实有 output 不同但 F1 相同的 instances。

**[AGREE] Table 4 缺少 multi-seed ±σ**

同意。Table 4 的 entity construction 结果仅用 single seed 报告，但论文在 Table 3 中用 2-seed，Table 7 中用 3-seed。Prescriptive 贡献理应有更强的统计支撑。

**[AGREE] WNUT-17 under-analyzed**

同意。WNUT-17 在 §4.1 仅被简要提及（"signal-collapse boundary"），完整分析在 Appendix Table 3。作为 4 个 benchmark 之一，正文分析不足。但鉴于 WNUT-17 的 52% zero-F1 rate 使其成为 boundary case，不给予过多正文空间是合理的。

**[AGREE] Figure 1 caption ρ=0.39 vs Abstract ρ=0.45 scope 不一致**

同意这会造成困惑。Figure 1 caption 报 ρ=0.39 是 SciERC VC 的值，Abstract 报 ρ=0.45 是 CoNLL EM 的值（Table 1）。两个都正确，但 scope 不同且未在 caption 中说明。

**[REBUT] Appendix 体量过大（7:1 ratio）**

不完全同意。ARR 对 appendix 长度没有明确限制（reviewers are not required to read appendix, but it can be included），且本文 appendix 的内容几乎都是 robustness checks、ablations、negative experiments 的完整报告——这恰恰是正文无法容纳但对 reproducibility 和 soundness 至关重要的材料。如果删减 appendix 以降低 ratio，反而会削弱论文的透明度和可验证性。问题不在 appendix 的量，而在正文是否 self-contained（答案是 yes：正文的核心 claim 不依赖 appendix 的具体数字）。

---

### 总结

与 R1 在 8/12 个问题上完全一致（N1, W1, W2, W3, W4, W5, 以及 3 个小问题）。在 3 个问题上部分一致但对严重程度有不同判断：

1. **ε=0.05（R1-N2）**：同意统计问题真实存在（Bonferroni 未覆盖 ε sweep），但论文已在 Limitations 和 Appendix 中做了适当 hedging。需要修改的是主文 §4.2 的措辞，而非删除该分析。建议从 critical 降为 warning。

2. **Expected selection gain bound（R1-N3）**：同意 "bounded by" 措辞不当（g(·) 未定义），但不认为需要形式化定理。这是一个有用的 conceptual decomposition，在实证论文中降级措辞即可。建议从 critical 降为 warning。

3. **Appendix 体量**：不同意这是问题。Appendix 材料对 reproducibility 有价值，且正文 self-contained。

维持 Overall 3/5 (Findings) 评分不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2351 · 2026-05-19T05:03:16.041860+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 2352 · 2026-05-19T05:03:16.092445+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2353 · 2026-05-19T05:06:21.483629+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n  # ===== 历史 resolved issues（保留记录）=====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance: LP selection viable when ρ≈0.3, otherwise greedy + QE selective prediction。D154 within/cross 区分增强诊断价值。\"\n    resolution_round: 21\n\n  - id: \"R2-W3\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-6 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison: 3-epoch SciERC ρ=0.319 vs Few-NERD ~0.5, 确认 LP alignment 驱动跨数据集差异。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'（footnote + L91），SciERC 为 diagnosis site，MDE 已注明。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix (L1388)。ε sweep (L560-588) + LOO τ sensitivity (L1396-1398) 均已呈现。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化为 'first systematic empirical characterization of when and why LP-based selection succeeds or fails for structured prediction'。D154 within/cross 区分 + ρ=0.052 negative result 增强新颖性。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文 11 处统一使用 0.205，0.215 从未出现。D145 决策保持 mean_LP 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。Reviewer PASS: 信息完整性通过，degeneracy 定义移入 Method §3.3。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。Reviewer PASS。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认 exp_025/exp_027 不存在于 .tex 文件中。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"正文无 'capability trap' 残留，已统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。Reviewer PASS。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Farquhar et al. + Chen et al. pass@k 已补入 Related Work。第三类未指定，视为完成。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix L1229 已有 'Under a conservative df=4 adjustment, p=0.033'。\"\n    resolution_round: 21\n\n  # ===== Round 22 issues（保留历史状态）=====\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页 (约 10 页 vs 8 页限制)\"\n    category: format\n    severity: critical\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R21-C1 曾 resolved，但当前版本再次超页。两位 Reviewer 独立确认。Discussion §5 + §4.5/§4.6 细节是主因。Desk reject 风险。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"本轮未专门检查页数，但正文内容量大（Experiments §4 含 6 个 subsection + 大量表格/图），Discussion 仅 11 行——说明空间已极度压缩。需确认编译后是否在 8 页内。\"\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result，与 §4.7 entity-level construction 正面结果矛盾\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"标题 'Why Confidence Signals Fail to Improve' vs §4.7 entity-level construction +1.67 pp (p=0.004)。叙事主线不统一。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"当前标题 'Strong Predictors, Weak Selectors: Diagnosing and Fixing Self-Consistency for NER' 已修复——包含了 diagnosing（负面）和 fixing（正面）两部分。本轮无 Reviewer 再提此问题。标记为可能已修复，待确认。\"\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度，停留在实证描述层面\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R2 列为 critical，R1 建议降为 warning。共识：增加简化分析框架即可。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"本轮 R2 再次列为 critical (N2)，R1 部分同意但认为 LP 失败和 degeneracy-alignment disentanglement 有经验价值。§4.3 新增 expected gain decomposition，但 g(·) 未定义（见 R23-N3）。概念深度问题仍在——instance-level signal 失败是定义性的，非经验发现。\"\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"LP 在 Abstract line 5 首次出现未定义；AUROC 在 line 4 未展开。\"\n      - round: 23\n        reviewers: [2]\n        note: \"R2 格式检查标注 'NER, QE, AUROC, LP 均在 Abstract 内展开定义'——可能已修复，待确认。\"\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe，存在 information leakage\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"§4.7 line 266 承认 'probe instances are drawn from the test set'。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"本轮两位 Reviewer 均独立列为 critical (R1-N1, R2-N3)。§4.5 已增加三条 caveats，但仍 claim 'correctly routes all three evaluated datasets'。Contribution 3 仍包含 gating 的 correct routing claim。交叉回应后共识维持 critical。\"\n\n  - id: \"R22-W4\"\n    summary: \"SciERC 主实验 seed sensitivity 高 (σ=0.48 pp)，1 primary seed 不够稳健\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"SciERC LP selection 3-seed mean +0.04±0.48 pp，但 main text 主要引用 1-seed 结果。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Table 2 用 2-seed mean，Table 3 用 single-seed (SciERC)，Table 7 用 3-seed。协议不统一。R1 提出 'Why Table 2 uses 2-seed not 3-seed?' 未见解释。\"\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致 (SciERC post-hoc θ=2/N vs 其他 CV)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Post-hoc 阈值有 data snooping 风险。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"本轮两位 Reviewer 再次提出（R1-W1, R2 交叉 AGREE）：θ=2/N 'tuning-free' claim 缺少 θ sensitivity sweep。Appendix 仅对比 θ=0.5 majority baseline。无 precision/recall 分解。\"\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"仅在 NER 上验证，CoNLL 上不 work。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"当前 Abstract line 7 使用 'A more effective self-consistency analogy'——已从 'the correct' 改为 'a more effective'。可能已修复。\"\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但标题和 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。LP compression 可能是 LoRA 特有现象。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1-W5 和 R2-W5 再次提出 scale 限制。Abstract 说 'fine-tuned 4B-8B models'（正确），但 Contribution 2 无 scale 限定。标题 'for NER' 未限定 fine-tuned。Discussion 说 'degeneracy rises with model capability' 但证据仅 3B-8B。\"\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中，缺乏统一展示\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"定义完整但分散，建议统一展示。\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"conclusion.tex line 5: 'a alignment-based' → 'an alignment-based'。\"\n      - round: 23\n        reviewers: [2]\n        note: \"R2 写作检查标注引用格式 '\\\\cite 和 \\\\citep/\\\\citet 使用一致'——可能已修复。\"\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023, Wan et al. 2024\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Related Work 缺少 ensemble-based NER methods 讨论。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 提出缺少 Florian et al. 2003 (NER ensemble), Kamath et al. 2020 (selective QA)。R2 提出缺少 Luo et al. 2023 (Zero-shot NER voting), Wiher et al. 2022 (MBR decoding strategies), Muennighoff et al. 2025 / Qu et al. 2025 (test-time scaling)。Entity construction 与已有 ensemble NER voting 的差异化讨论仍不足。\"\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n\n  - id: \"R22-FIG1\"\n    summary: \"fig_overview 缺少 Construction 贡献 + 残留 RE 文字\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [director]\n        note: \"fig_overview 只展示 QE 和 Selection，不展示 Construction。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Figure 1 caption 现在描述三列布局 (Left: QE, Center: selection bottleneck, Right: construction)。R1 注意到 caption ρ=0.39 vs Abstract ρ=0.45 scope 不一致。可能已部分修复但 scope 标注仍需确认。\"\n\n  - id: \"R22-FIG2\"\n    summary: \"fig_selection_gap caption 仍引用旧双面板格式\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 22\n\n  # ===== Round 23 新增 issues =====\n\n  - id: \"R23-N1\"\n    summary: \"Entity-level construction 新颖性不足——本质是 entity-level majority voting，与 ensemble NER 机制高度相似\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立列为 critical 并在交叉回应中完全一致。论文自身在 Related Work §2 承认机制相似 ('similarly aggregates across samples from a single model')。LP-weighted vs Uniform 增量极小 (SciERC +1.67 vs +1.54pp; N=16 converge)。作为论文两大贡献之一 ('Fixing' 部分)，新颖性不足严重影响 main conference 定位。\"\n    action_items:\n      - round: 23\n        action: \"选项 A: 更清晰地 differentiate entity-level construction vs ensemble NER voting（单模型多 sample 的 diversity 特征差异、LP weighting 在 ensemble 设定下不可行等）。选项 B: 将 construction 降级为已有方法在新设定下的验证，strengthened diagnostic contribution 补偿。\"\n        assigned_to: research_director\n        status: pending\n\n  - id: \"R23-N2\"\n    summary: \"Correlation-selection gap 概念深度有限——4/5 signal 失败是定义性的，非经验发现\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 critical，R1 部分同意但认为 LP 失败（非 trivial 经验发现）和 degeneracy-alignment disentanglement（温度实验 Table 6）有价值。交叉回应后方向共识：应将 instance-level signal 失败作为背景/动机（定义推论），聚焦于 LP 为何失败的 compression + alignment 机制。当前 framing 混淆了定义性限制和经验性发现。\"\n    action_items:\n      - round: 23\n        action: \"重构 §4.2 framing：instance-level signal 不能 rank candidates 作为 setup/motivation，correlation-selection gap 聚焦于 LP 的 compression 和 alignment 问题。\"\n        assigned_to: research_director\n        status: pending\n\n  - id: \"R23-N3\"\n    summary: \"Expected selection gain 'bound' 中 g(·) 未定义，无形式化推导\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 列为 critical，R2 同意方向但建议降为 warning（实证论文不需要形式化定理）。交叉回应后共识：'bounded by' 措辞不当，g(·) 未定义使 '≤' 无意义。建议改为 'heuristically decomposed as' 并给出 g(·) 的假设条件。无需正式证明。\"\n    action_items:\n      - round: 23\n        action: \"§4.3: 'bounded by' → 'heuristically decomposed as'；脚注说明 g(·) 的单调性假设和边界条件 (g(0)=0, g(1)=1)。\"\n        assigned_to: research_director\n        status: pending\n\n  - id: \"R23-W1\"\n    summary: \"ε=0.05 non-tied subset 是 post-hoc 最优切点，Bonferroni 未覆盖 ε sweep\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 列为 critical，R2 同意统计问题但建议降为 warning（论文已在 Limitations 做 hedging）。交叉回应后共识降为 warning。核心问题：主文 §4.2 'survives Bonferroni correction' 仅覆盖 5 signal，未覆盖 ε sweep 的 7 个阈值。7×5=35 Bonferroni 后 p_adj=0.14。\"\n    action_items:\n      - round: 23\n        action: \"§4.2: 修改 'survives Bonferroni correction' 为明确说明 correction 范围；降低 non-tied subset 在叙事中的权重。\"\n        assigned_to: research_director\n        status: pending\n\n  - id: \"R23-W2\"\n    summary: \"Complementarity claim 仅基于 3 dataset (实际 2 个 informative data points)\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"CoNLL 为 ceiling regime，两种方法都不 work。实际仅 SciERC（construction wins）和 Few-NERD（LP wins）两个 informative data points。2 个数据点不足以支撑 general prescriptive claim。R1 列为 warning，R2 交叉 AGREE。\"\n    action_items:\n      - round: 23\n        action: \"Contribution 3 和 §4.5 中明确标注 dataset 数量限制；将 claim 从 prescriptive guideline 降级为 preliminary observation。\"\n        assigned_to: research_director\n        status: pending\n\n  - id: \"R23-W3\"\n    summary: \"Abstract 信息密度过高，约 10 个数字，读起来像实验报告压缩版\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 warning，R1 交叉 AGREE with nuance（叙事结构正确但数字过多）。当前 Abstract 含 ρ=0.45, AUROC=0.82, +5-8pp, +1.39pp, p<0.001, 13-87%, ρ=0.052, 23 configurations, +0.88, +1.67pp, p<0.005 等约 10 个数字。\"\n    action_items:\n      - round: 23\n        action: \"精简 Abstract 至 2-3 个关键数字，其余移入正文。\"\n        assigned_to: research_director\n        status: pending\n\n  - id: \"R23-W4\"\n    summary: \"Table 4 (entity construction) 缺少 multi-seed ±σ\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Tables 2-3 报告 ±σ，但 Table 4 没有。Prescriptive contribution 理应有更强统计支撑。R1 列为 info，R2 交叉 AGREE。\"\n\n  - id: \"R23-I1\"\n    summary: \"Figure 1 caption ρ=0.39 vs Abstract ρ=0.45 scope 不一致\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Figure 1 caption ρ up to 0.39（SciERC VC），Abstract ρ up to 0.45（CoNLL EM）。两个数字正确但 scope 不同，未在 caption 中说明。\"\n\n  - id: \"R23-I2\"\n    summary: \"WNUT-17 正文分析不足——Introduction 定位为 signal-collapse boundary 但主文几乎未分析\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1]\n        note: \"Introduction 定位 WNUT-17 为 'signal-collapse boundary'，但 §4.2 仅一句提及，完整分析在 Appendix Table 3。建议删除 Introduction 中的角色定位或增加正文分析。\"\n\n  - id: \"R23-MR1\"\n    summary: \"缺失引用: entity-level ensemble NER (Florian et al. 2003), selective QA (Kamath et al. 2020), zero-shot NER voting (Luo et al. 2023), MBR decoding strategies (Wiher et al. 2022)\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1: Florian et al. 2003 (NER ensemble), Kamath et al. 2020 (selective QA under domain shift)。R2: Luo et al. 2023 (zero-shot NER self-annotation + voting), Wiher et al. 2022 (MBR vs MAP), Muennighoff et al. 2025 / Qu et al. 2025 (test-time scaling)。Entity construction 与 ensemble NER 的差异化讨论仍不足。\"\n    action_items:\n      - round: 23\n        action: \"补充引用并在 Related Work 中讨论 entity-level construction 与 ensemble NER voting 的区别。\"\n        assigned_to: research_director\n        status: pending"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n  # ===== 历史 resolved issues（保留记录）=====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance: LP selection viable when ρ≈0.3, otherwise greedy + QE selective prediction。D154 within/cross 区分增强诊断价值。\"\n    resolution_round: 21\n\n  - id: \"R2-W3\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-6 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison: 3-epoch SciERC ρ=0.319 vs Few-NERD ~0.5, 确认 LP alignment 驱动跨数据集差异。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'（footnote + L91），SciERC 为 diagnosis site，MDE 已注明。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix (L1388)。ε sweep (L560-588) + LOO τ sensitivity (L1396-1398) 均已呈现。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化为 'first systematic empirical characterization of when and why LP-based selection succeeds or fails for structured prediction'。D154 within/cross 区分 + ρ=0.052 negative result 增强新颖性。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文 11 处统一使用 0.205，0.215 从未出现。D145 决策保持 mean_LP 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。Reviewer PASS: 信息完整性通过，degeneracy 定义移入 Method §3.3。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。Reviewer PASS。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认 exp_025/exp_027 不存在于 .tex 文件中。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"正文无 'capability trap' 残留，已统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。Reviewer PASS。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Farquhar et al. + Chen et al. pass@k 已补入 Related Work。第三类未指定，视为完成。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix L1229 已有 'Under a conservative df=4 adjustment, p=0.033'。\"\n    resolution_round: 21\n\n  # ===== Round 22 issues（保留历史状态）=====\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页 (约 10 页 vs 8 页限制)\"\n    category: format\n    severity: critical\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R21-C1 曾 resolved，但当前版本再次超页。两位 Reviewer 独立确认。Discussion §5 + §4.5/§4.6 细节是主因。Desk reject 风险。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"本轮未专门检查页数，但正文内容量大（Experiments §4 含 6 个 subsection + 大量表格/图），Discussion 仅 11 行——说明空间已极度压缩。需确认编译后是否在 8 页内。\"\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result，与 §4.7 entity-level construction 正面结果矛盾\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"标题 'Why Confidence Signals Fail to Improve' vs §4.7 entity-level construction +1.67 pp (p=0.004)。叙事主线不统一。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"当前标题 'Strong Predictors, Weak Selectors: Diagnosing and Fixing Self-Consistency for NER' 已修复——包含了 diagnosing（负面）和 fixing（正面）两部分。本轮无 Reviewer 再提此问题。标记为可能已修复，待确认。\"\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度，停留在实证描述层面\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R2 列为 critical，R1 建议降为 warning。共识：增加简化分析框架即可。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"本轮 R2 再次列为 critical (N2)，R1 部分同意但认为 LP 失败和 degeneracy-alignment disentanglement 有经验价值。§4.3 新增 expected gain decomposition，但 g(·) 未定义（见 R23-N3）。概念深度问题仍在——instance-level signal 失败是定义性的，非经验发现。\"\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"LP 在 Abstract line 5 首次出现未定义；AUROC 在 line 4 未展开。\"\n      - round: 23\n        reviewers: [2]\n        note: \"R2 格式检查标注 'NER, QE, AUROC, LP 均在 Abstract 内展开定义'——可能已修复，待确认。\"\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe，存在 information leakage\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"§4.7 line 266 承认 'probe instances are drawn from the test set'。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"本轮两位 Reviewer 均独立列为 critical (R1-N1, R2-N3)。§4.5 已增加三条 caveats，但仍 claim 'correctly routes all three evaluated datasets'。Contribution 3 仍包含 gating 的 correct routing claim。交叉回应后共识维持 critical。\"\n\n  - id: \"R22-W4\"\n    summary: \"SciERC 主实验 seed sensitivity 高 (σ=0.48 pp)，1 primary seed 不够稳健\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"SciERC LP selection 3-seed mean +0.04±0.48 pp，但 main text 主要引用 1-seed 结果。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Table 2 用 2-seed mean，Table 3 用 single-seed (SciERC)，Table 7 用 3-seed。协议不统一。R1 提出 'Why Table 2 uses 2-seed not 3-seed?' 未见解释。\"\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致 (SciERC post-hoc θ=2/N vs 其他 CV)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Post-hoc 阈值有 data snooping 风险。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"本轮两位 Reviewer 再次提出（R1-W1, R2 交叉 AGREE）：θ=2/N 'tuning-free' claim 缺少 θ sensitivity sweep。Appendix 仅对比 θ=0.5 majority baseline。无 precision/recall 分解。\"\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"仅在 NER 上验证，CoNLL 上不 work。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"当前 Abstract line 7 使用 'A more effective self-consistency analogy'——已从 'the correct' 改为 'a more effective'。可能已修复。\"\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但标题和 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。LP compression 可能是 LoRA 特有现象。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1-W5 和 R2-W5 再次提出 scale 限制。Abstract 说 'fine-tuned 4B-8B models'（正确），但 Contribution 2 无 scale 限定。标题 'for NER' 未限定 fine-tuned。Discussion 说 'degeneracy rises with model capability' 但证据仅 3B-8B。\"\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中，缺乏统一展示\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"定义完整但分散，建议统一展示。\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"conclusion.tex line 5: 'a alignment-based' → 'an alignment-based'。\"\n      - round: 23\n        reviewers: [2]\n        note: \"R2 写作检查标注引用格式 '\\\\cite 和 \\\\citep/\\\\citet 使用一致'——可能已修复。\"\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023, Wan et al. 2024\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Related Work 缺少 ensemble-based NER methods 讨论。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 提出缺少 Florian et al. 2003 (NER ensemble), Kamath et al. 2020 (selective QA)。R2 提出缺少 Luo et al. 2023 (Zero-shot NER voting), Wiher et al. 2022 (MBR decoding strategies), Muennighoff et al. 2025 / Qu et al. 2025 (test-time scaling)。Entity construction 与已有 ensemble NER voting 的差异化讨论仍不足。\"\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n\n  - id: \"R22-FIG1\"\n    summary: \"fig_overview 缺少 Construction 贡献 + 残留 RE 文字\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [director]\n        note: \"fig_overview 只展示 QE 和 Selection，不展示 Construction。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Figure 1 caption 现在描述三列布局 (Left: QE, Center: selection bottleneck, Right: construction)。R1 注意到 caption ρ=0.39 vs Abstract ρ=0.45 scope 不一致。可能已部分修复但 scope 标注仍需确认。\"\n\n  - id: \"R22-FIG2\"\n    summary: \"fig_selection_gap caption 仍引用旧双面板格式\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 22\n\n  # ===== Round 23 新增 issues =====\n\n  - id: \"R23-N1\"\n    summary: \"Entity-level construction 新颖性不足——本质是 entity-level majority voting，与 ensemble NER 机制高度相似\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立列为 critical 并在交叉回应中完全一致。论文自身在 Related Work §2 承认机制相似 ('similarly aggregates across samples from a single model')。LP-weighted vs Uniform 增量极小 (SciERC +1.67 vs +1.54pp; N=16 converge)。作为论文两大贡献之一 ('Fixing' 部分)，新颖性不足严重影响 main conference 定位。\"\n    action_items:\n      - round: 23\n        action: \"选项 A: 更清晰地 differentiate entity-level construction vs ensemble NER voting（单模型多 sample 的 diversity 特征差异、LP weighting 在 ensemble 设定下不可行等）。选项 B: 将 construction 降级为已有方法在新设定下的验证，strengthened diagnostic contribution 补偿。\"\n        assigned_to: research_director\n        status: pending\n\n  - id: \"R23-N2\"\n    summary: \"Correlation-selection gap 概念深度有限——4/5 signal 失败是定义性的，非经验发现\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 critical，R1 部分同意但认为 LP 失败（非 trivial 经验发现）和 degeneracy-alignment disentanglement（温度实验 Table 6）有价值。交叉回应后方向共识：应将 instance-level signal 失败作为背景/动机（定义推论），聚焦于 LP 为何失败的 compression + alignment 机制。当前 framing 混淆了定义性限制和经验性发现。\"\n    action_items:\n      - round: 23\n        action: \"重构 §4.2 framing：instance-level signal 不能 rank candidates 作为 setup/motivation，correlation-selection gap 聚焦于 LP 的 compression 和 alignment 问题。\"\n        assigned_to: research_director\n        status: pending\n\n  - id: \"R23-N3\"\n    summary: \"Expected selection gain 'bound' 中 g(·) 未定义，无形式化推导\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 列为 critical，R2 同意方向但建议降为 warning（实证论文不需要形式化定理）。交叉回应后共识：'bounded by' 措辞不当，g(·) 未定义使 '≤' 无意义。建议改为 'heuristically decomposed as' 并给出 g(·) 的假设条件。无需正式证明。\"\n    action_items:\n      - round: 23\n        action: \"§4.3: 'bounded by' → 'heuristically decomposed as'；脚注说明 g(·) 的单调性假设和边界条件 (g(0)=0, g(1)=1)。\"\n        assigned_to: research_director\n        status: pending\n\n  - id: \"R23-W1\"\n    summary: \"ε=0.05 non-tied subset 是 post-hoc 最优切点，Bonferroni 未覆盖 ε sweep\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 列为 critical，R2 同意统计问题但建议降为 warning（论文已在 Limitations 做 hedging）。交叉回应后共识降为 warning。核心问题：主文 §4.2 'survives Bonferroni correction' 仅覆盖 5 signal，未覆盖 ε sweep 的 7 个阈值。7×5=35 Bonferroni 后 p_adj=0.14。\"\n    action_items:\n      - round: 23\n        action: \"§4.2: 修改 'survives Bonferroni correction' 为明确说明 correction 范围；降低 non-tied subset 在叙事中的权重。\"\n        assigned_to: research_director\n        status: pending\n\n  - id: \"R23-W2\"\n    summary: \"Complementarity claim 仅基于 3 dataset (实际 2 个 informative data points)\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"CoNLL 为 ceiling regime，两种方法都不 work。实际仅 SciERC（construction wins）和 Few-NERD（LP wins）两个 informative data points。2 个数据点不足以支撑 general prescriptive claim。R1 列为 warning，R2 交叉 AGREE。\"\n    action_items:\n      - round: 23\n        action: \"Contribution 3 和 §4.5 中明确标注 dataset 数量限制；将 claim 从 prescriptive guideline 降级为 preliminary observation。\"\n        assigned_to: research_director\n        status: pending\n\n  - id: \"R23-W3\"\n    summary: \"Abstract 信息密度过高，约 10 个数字，读起来像实验报告压缩版\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 warning，R1 交叉 AGREE with nuance（叙事结构正确但数字过多）。当前 Abstract 含 ρ=0.45, AUROC=0.82, +5-8pp, +1.39pp, p<0.001, 13-87%, ρ=0.052, 23 configurations, +0.88, +1.67pp, p<0.005 等约 10 个数字。\"\n    action_items:\n      - round: 23\n        action: \"精简 Abstract 至 2-3 个关键数字，其余移入正文。\"\n        assigned_to: research_director\n        status: pending\n\n  - id: \"R23-W4\"\n    summary: \"Table 4 (entity construction) 缺少 multi-seed ±σ\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Tables 2-3 报告 ±σ，但 Table 4 没有。Prescriptive contribution 理应有更强统计支撑。R1 列为 info，R2 交叉 AGREE。\"\n\n  - id: \"R23-I1\"\n    summary: \"Figure 1 caption ρ=0.39 vs Abstract ρ=0.45 scope 不一致\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Figure 1 caption ρ up to 0.39（SciERC VC），Abstract ρ up to 0.45（CoNLL EM）。两个数字正确但 scope 不同，未在 caption 中说明。\"\n\n  - id: \"R23-I2\"\n    summary: \"WNUT-17 正文分析不足——Introduction 定位为 signal-collapse boundary 但主文几乎未分析\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1]\n        note: \"Introduction 定位 WNUT-17 为 'signal-collapse boundary'，但 §4.2 仅一句提及，完整分析在 Appendix Table 3。建议删除 Introduction 中的角色定位或增加正文分析。\"\n\n  - id: \"R23-MR1\"\n    summary: \"缺失引用: entity-level ensemble NER (Florian et al. 2003), selective QA (Kamath et al. 2020), zero-shot NER voting (Luo et al. 2023), MBR decoding strategies (Wiher et al. 2022)\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1: Florian et al. 2003 (NER ensemble), Kamath et al. 2020 (selective QA under domain shift)。R2: Luo et al. 2023 (zero-shot NER self-annotation + voting), Wiher et al. 2022 (MBR vs MAP), Muennighoff et al. 2025 / Qu et al. 2025 (test-time scaling)。Entity construction 与 ensemble NER 的差异化讨论仍不足。\"\n    action_items:\n      - round: 23\n        action: \"补充引用并在 Related Work 中讨论 entity-level construction 与 ensemble NER voting 的区别。\"\n        assigned_to: research_director\n        status: pending"
  }
}
```

</details>

---


### Tool result

_source line 2354 · 2026-05-19T05:06:21.584943+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 23097}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2355 · 2026-05-19T05:08:34.288256+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 23\n\n**论文**: Strong Predictors, Weak Selectors: Diagnosing and Fixing Self-Consistency for Named Entity Recognition\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+格式合规）\n**审稿模式**: 重新审稿（fresh），1 轮独立审稿 + 1 轮交叉回应\n\n---\n\n## Summary\n\n本文研究 self-consistency 在 NER 上的适用性，评估 5 种 confidence signal 的 quality estimation（QE）和 sample selection 能力。论文发现 QE 表现良好（ρ up to 0.45, AUROC up to 0.82）但 instance-level selection 普遍失败，将此命名为 \"correlation-selection gap\"，归因于 instance degeneracy 和 LP compression。最终提出 entity-level construction 作为替代方案，在 SciERC (+1.67pp) 和 Few-NERD (+0.88pp) 上取得显著改进。\n\n---\n\n## Strengths\n\n1. **统计方法论严谨度在 NER/IE 领域罕见**：bootstrap CI、paired bootstrap、TOST equivalence testing with external margins、MDE 计算、Bonferroni correction。方法论意识远高于同类工作。\n\n2. **消融设计系统完整**：temperature（4 点）、N-scaling（N=2 到 32）、model scale（3B/4B/8B）、epoch confound（2-3 点 curve）、LoRA rank、constrained vs free-form decoding、supervised combination、hidden state probes、DeBERTa verifier。形成闭环证据网络。\n\n3. **负面结果的透明报告**：6+ 个 negative experiments（supervised combination、hidden probes、DeBERTa verifier、DALS、VerbConf、calibration baseline）如实报告。Limitations section 覆盖 15+ 条限制，堪称范例。\n\n4. **问题分解清晰**：将 QE 和 sample selection 显式分离是有用的框架选择。QE → selective prediction 的实用价值论证完整。\n\n5. **写作质量高**：无 AI 写作痕迹（无 em-dash、无 -ing phrase 结尾、无过度分段、无黑名单用词）。技术表述清晰紧凑。格式合规（ACL 模板、review 模式、匿名、checklist 认真填写）。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[N1] Entity-level construction 新颖性不足** [critical, 共识]\n- Entity-level construction 本质是 entity-level majority voting，与 ensemble NER（EL4NER, Naderi et al. 2021）机制高度相似，区别仅在于跨同模型 sample 而非跨模型聚合。论文自身在 Related Work §2 承认 \"our entity-level construction similarly aggregates across samples from a single model, without requiring model diversity\"。\n- LP-weighted vs Uniform 增量极小（SciERC: +1.67 vs +1.54pp; N=16 时两者 converge），说明 LP weighting 贡献有限。\n- 作为论文两大贡献之一（\"Fixing\" 部分），新颖性不足严重影响 main conference 定位。\n\n**[N2] Correlation-selection gap 概念深度有限** [critical, 基本共识]\n- 4/5 signal 是 instance-level，按定义不能 rank candidates——这是定义性质而非经验发现。论文在 §3.1 已建立 per-sample vs instance-level 区分，instance-level signal 无法 rank 是逻辑推论。\n- 真正的经验性发现是 LP（唯一 per-sample signal）也失败，以及 degeneracy-alignment disentanglement（温度实验）和 degeneracy 不能跨 dataset 预测 LP 方向（ρ=0.052）。但这些被 4 个 instance-level signal 的 \"失败\" 稀释了。\n- R1 认为 LP 失败和 disentanglement 有经验价值（部分同意），但当前 framing 混淆了定义性限制和经验性发现。\n\n**[N3] LP-alignment gating 使用 test set 构成 information leakage** [critical, 共识]\n- Gating protocol 使用 50 个 test set instances 估计 within-instance ρ(LP, F1)（需要 gold labels），再将 routing decision 应用于同一 test set。论文自述 \"probe instances are drawn from the test set for simplicity\"，但仍 claim \"correctly routes all three evaluated datasets\"。\n- §4.5 已增加三条 caveats（(a) test set probe, (b) only 3 datasets, (c) proof of concept），但 Contribution #3 仍包含 gating 的 correct routing claim。\n- 仅 3 个 dataset 验证（实际 2 个 informative data points），且 dataset 间 ρ 差距很大（>0.15），routing \"正确性\" 可能只是因为差距足够大。\n\n### Should-Fix（影响评分但不一票否决）\n\n**[W1] ε=0.05 non-tied subset 是 post-hoc 最优切点，Bonferroni 未覆盖 ε sweep** [warning, 共识]\n- ε sweep（Table 10）显示 ε=0.05 恰好是 p-value 最小的切点（p=0.004），相邻切点显著性更弱。主文 §4.2 \"survives Bonferroni correction\" 仅覆盖 5 signal comparisons，未覆盖 ε sweep 的 7 个阈值。7×5=35 Bonferroni 后 p_adj=0.14。\n- 论文已在 Limitations 标注 \"post-hoc exploratory choice\"，但主文叙事权重过高。\n\n**[W2] Expected selection gain \"bound\" 中 g(·) 未定义** [warning, 共识]\n- §4.3: E[ΔF1] ≤ (1-d) · Δ_oracle · g(ρ_within)，g(·) 描述为 \"monotonically increasing function\" 但从未定义。包含未定义函数的不等式不构成 bound。\n- 两位 Reviewer 共识：不需要形式化定理，但 \"bounded by\" 应改为 \"heuristically decomposed as\"，并给出 g(·) 的假设条件。\n\n**[W3] θ=2/N \"tuning-free\" claim 缺乏 θ sensitivity sweep** [warning, 共识]\n- §4.5 称 θ=2/N 是 \"tuning-free across all datasets\"，但仅对比了 θ=0.5 majority baseline。无 θ ∈ [1/N, 1] 的 sensitivity curve，无 precision/recall 分解。θ=2/N 在 N=8 时等于 0.25，大幅 boost recall，可能在 high-noise 场景引入 false positives。\n\n**[W4] SciERC greedy F1 出现 4 个值，协议不统一** [warning, 共识]\n- 0.640, 0.644, 0.645, 0.650 四个值跨 Tables 1-4 出现。§3.2 末尾有解释，但 Table 2 用 2-seed、Table 3 用 single-seed/3-seed、Table 7 用 3-seed 的不统一缺乏解释。\n\n**[W5] Complementarity claim 仅基于 3 dataset（2 个 informative data points）** [warning, 共识]\n- CoNLL 为 ceiling regime，两种方法都不 work。实际仅 SciERC（construction wins）和 Few-NERD（LP wins）两个 informative data points。\n\n**[W6] 模型规模 4B-8B，claims 表述过于一般化** [warning, 共识]\n- 标题 \"for NER\" 和 Contribution 2 无 scale 限定。Discussion \"degeneracy rises with model capability\" 仅基于 3B-8B。70B+ 行为未知。\n\n**[W7] Abstract 信息密度过高** [warning, 共识]\n- 约 10 个数字，读起来像实验报告压缩版。建议精简至 2-3 个关键数字。\n\n**[W8] Table 4 (entity construction) 缺少 multi-seed ±σ** [warning, 共识]\n- Prescriptive 贡献应有更强统计支撑。\n\n### Info（小问题）\n\n- [I1] Figure 1 caption ρ=0.39 vs Abstract ρ=0.45 scope 不一致（SciERC vs CoNLL）\n- [I2] WNUT-17 正文分析不足——Introduction 定位为 \"signal-collapse boundary\" 但主文仅一句提及\n- [I3] Table D.1 \"Identical\" vs 正文 \"Constant F1\" 概念不同（11% vs 17.8%），易混淆\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Overall 评分一致**：两位 Reviewer 独立给出 3/5 (Findings)，交叉回应后维持不变。\n2. **Entity construction 新颖性不足**：两位 Reviewer 均独立列为 critical 并在交叉回应中完全一致。\n3. **Test-set leakage in gating**：两位 Reviewer 均独立列为 critical 并完全一致。\n4. **θ=2/N、greedy F1 不一致、complementarity 仅 3 dataset、scale 限制**：全部共识。\n5. **统计严谨度和写作质量**：均给予高度肯定。\n\n## Reviewer Divergence [REBUT]\n\n1. **ε=0.05 严重度**：R1 列为 critical（Bonferroni 应覆盖 ε sweep），R2 同意统计问题但建议降为 warning（论文已做 hedging）。→ **最终判定：warning**（论文在 Limitations 和 Appendix 已承认 post-hoc 性质，需修改的是主文措辞而非删除分析）。\n\n2. **Expected gain bound 形式化**：R1 列为 critical（g(·) 未定义则 bound 无意义），R2 建议降为 warning（实证论文不需要定理）。→ **最终判定：warning**（修改措辞即可，无需正式证明）。\n\n3. **Epoch confound (Few-NERD 3-epoch)**：R2 列为 warning（未完全消解），R1 REBUT（Appendix E 提供了 3-point curve，5-epoch LP 仍 positive，已 adequately addressed）。→ **最终判定：不列入报告**（R1 反驳有理有据，Appendix 的 epoch ablation 覆盖充分）。\n\n4. **Selective prediction 定位**：R2 列为 warning（不应列为独立贡献），R1 REBUT（原文中是 Contribution 1 的子项而非独立贡献）。→ **最终判定：不列入报告**（R1 对原文结构的阅读准确）。\n\n5. **Appendix 体量**：R1 列为 info（7:1 ratio），R2 REBUT（ARR 无限制，材料对 reproducibility 有价值）。→ **最终判定：不列入报告**。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Entity-level construction 相对于 ensemble NER entity voting 的技术区别是什么？单模型多 sample vs 多模型是否产生不同的 diversity 特征？LP weighting 在 ensemble 设定下是否可行？\n\n**Q2.** Table 2 使用 \"2-seed mean\" 而 Table 3/7 使用 \"3-seed\"，为什么 selection analysis 的 seed 数量少于 QE analysis？\n\n**Q3.** LP-alignment gating 如果改用 held-out validation set（不接触 test set gold），routing decision 是否仍然 correct？\n\n**Q4.** §4.3 Expected selection gain decomposition 中 g(·) 的具体形式或假设条件是什么？\n\n**Q5.** θ=2/N 是如何确定的——先验理由还是基于性能选择？能否提供 θ 在 [1/N, 1] 范围内的 sensitivity curve 和 precision/recall 分解？\n\n**Q6.** §1 中 \"the first systematic empirical characterization\" 的 scope——相对于 Yao et al. 2026 和 Vashurin et al. 2025 (CoCoA)，\"first\" 具体指什么？\n\n**Q7.** Within-instance LP-quality alignment 的 SciERC vs Few-NERD 差异（ρ≈0.26 vs ≈0.5-0.7）是否可能由 entity type 数量（6 vs 8）或 domain shift 驱动？\n\n---\n\n## Missing References\n\n1. **Entity-level ensemble NER**: Florian et al. 2003 (\"Named Entity Recognition through Classifier Combination\")——entity-level construction 的最直接先行工作，应引用并讨论区别。\n2. **Zero-shot NER voting**: Luo et al. 2023 (Zero-shot NER with ChatGPT, self-annotation + voting)——与 entity-level construction 机制相关。\n3. **MBR decoding strategies**: Wiher et al. 2022 (\"On Decoding Strategies for Neural Text Generators\")——对 selection-gap 讨论有补充价值。\n4. **Selective prediction under domain shift**: Kamath et al. 2020 (\"Selective Question Answering under Domain Shift\")——补充 selective prediction 引用。\n5. **Test-time scaling 最新进展**: Muennighoff et al. 2025 (\"s1: Simple Test-Time Scaling\") 和/或 Qu et al. 2025 (\"Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning\")。\n\n---\n\n## Overall Assessment\n\n**评分: Weak Accept (Findings) / Borderline (Main Conference)**\n**置信度: 4/5 (High)**\n\n两位 Reviewer 一致评价为 3/5，推荐 Findings track。\n\n**核心判断**：这是一篇高质量的实证分析论文。统计方法论严谨度、消融覆盖广度、负面结果透明度均远高于同类工作。QE vs selection 的显式分离和 degeneracy/compression 双因素诊断框架有真实贡献。\n\n**制约因素**：\n- Entity-level construction 新颖性有限（本质是 entity-level majority voting），作为论文 \"Fixing\" 部分的核心贡献不足以支撑 main conference。\n- Correlation-selection gap 的概念中，4/5 signal 失败是定义性的，真正的经验贡献（LP 失败 + disentanglement）被稀释。\n- Gating protocol 存在 test-set leakage + 仅 3 dataset 验证。\n- Prescriptive claims（complementarity、gating、θ tuning-free）的证据强度与 claim 力度不匹配。\n\n**修复路径**：\n1. 在 Contribution framing 上将 entity construction 定位为 \"applying known technique to a new setting\" 而非方法创新，同时 strengthen diagnostic contribution 的叙事价值。\n2. 重构 correlation-selection gap：instance-level signal 失败作为 setup，聚焦 LP compression/alignment。\n3. Gating 降级为 proof of concept 或用 proper validation set 重新验证。\n4. 修复 g(·) 措辞、ε Bonferroni 范围说明、Abstract 数字精简、θ sensitivity sweep。\n\n如果以上修复到位，论文适合 **EMNLP Findings**。Main conference 需要更强的方法贡献（如理论化的 selection bound）或更广的 scale 覆盖。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度过高（~10 个数字），精简至 2-3 个关键数字\n- AUROC/LP 缩写定义需确认是否已展开\n\n### Introduction\n- Contribution 2 和标题需加入 \"fine-tuned / 4B-8B\" scope 限定\n- \"first systematic empirical characterization\" 需相对于 Yao et al. 2026 / CoCoA 更精确界定 scope\n- WNUT-17 的 \"signal-collapse boundary\" 角色定位与正文覆盖不匹配\n\n### Related Work\n- 缺少 entity-level ensemble NER 的覆盖（Florian et al. 2003 等）\n- 缺少 selective prediction 和 test-time scaling 的最新引用\n\n### Method\n- Entity matching 标准分散在 §3.2 各段落，建议统一展示\n- Expected selection gain decomposition (§4.3): \"bounded by\" → \"heuristically decomposed as\"\n\n### Experiments\n- Table 2 vs 3 vs 7 的 seed 数量不统一需解释\n- Table 4 缺少 multi-seed ±σ\n- §4.2 \"survives Bonferroni correction\" 需说明 correction 范围\n\n### Discussion\n- 篇幅极短（11 行），与 Experiments 的体量不成比例\n- 正文空间可能紧张——需确认编译后 ≤8 页\n\n### Conclusion\n- 实用建议（LP selection when ρ≈0.3, otherwise construction）清晰有用\n\n### Limitations\n- 覆盖全面，堪称范例\n\n### Appendix\n- 体量大但内容对 reproducibility 有价值\n- Figure 1 caption scope 需与 Abstract 一致",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak accept (findings) / borderline (main conference)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 23\n\n**论文**: Strong Predictors, Weak Selectors: Diagnosing and Fixing Self-Consistency for Named Entity Recognition\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+格式合规）\n**审稿模式**: 重新审稿（fresh），1 轮独立审稿 + 1 轮交叉回应\n\n---\n\n## Summary\n\n本文研究 self-consistency 在 NER 上的适用性，评估 5 种 confidence signal 的 quality estimation（QE）和 sample selection 能力。论文发现 QE 表现良好（ρ up to 0.45, AUROC up to 0.82）但 instance-level selection 普遍失败，将此命名为 \"correlation-selection gap\"，归因于 instance degeneracy 和 LP compression。最终提出 entity-level construction 作为替代方案，在 SciERC (+1.67pp) 和 Few-NERD (+0.88pp) 上取得显著改进。\n\n---\n\n## Strengths\n\n1. **统计方法论严谨度在 NER/IE 领域罕见**：bootstrap CI、paired bootstrap、TOST equivalence testing with external margins、MDE 计算、Bonferroni correction。方法论意识远高于同类工作。\n\n2. **消融设计系统完整**：temperature（4 点）、N-scaling（N=2 到 32）、model scale（3B/4B/8B）、epoch confound（2-3 点 curve）、LoRA rank、constrained vs free-form decoding、supervised combination、hidden state probes、DeBERTa verifier。形成闭环证据网络。\n\n3. **负面结果的透明报告**：6+ 个 negative experiments（supervised combination、hidden probes、DeBERTa verifier、DALS、VerbConf、calibration baseline）如实报告。Limitations section 覆盖 15+ 条限制，堪称范例。\n\n4. **问题分解清晰**：将 QE 和 sample selection 显式分离是有用的框架选择。QE → selective prediction 的实用价值论证完整。\n\n5. **写作质量高**：无 AI 写作痕迹（无 em-dash、无 -ing phrase 结尾、无过度分段、无黑名单用词）。技术表述清晰紧凑。格式合规（ACL 模板、review 模式、匿名、checklist 认真填写）。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[N1] Entity-level construction 新颖性不足** [critical, 共识]\n- Entity-level construction 本质是 entity-level majority voting，与 ensemble NER（EL4NER, Naderi et al. 2021）机制高度相似，区别仅在于跨同模型 sample 而非跨模型聚合。论文自身在 Related Work §2 承认 \"our entity-level construction similarly aggregates across samples from a single model, without requiring model diversity\"。\n- LP-weighted vs Uniform 增量极小（SciERC: +1.67 vs +1.54pp; N=16 时两者 converge），说明 LP weighting 贡献有限。\n- 作为论文两大贡献之一（\"Fixing\" 部分），新颖性不足严重影响 main conference 定位。\n\n**[N2] Correlation-selection gap 概念深度有限** [critical, 基本共识]\n- 4/5 signal 是 instance-level，按定义不能 rank candidates——这是定义性质而非经验发现。论文在 §3.1 已建立 per-sample vs instance-level 区分，instance-level signal 无法 rank 是逻辑推论。\n- 真正的经验性发现是 LP（唯一 per-sample signal）也失败，以及 degeneracy-alignment disentanglement（温度实验）和 degeneracy 不能跨 dataset 预测 LP 方向（ρ=0.052）。但这些被 4 个 instance-level signal 的 \"失败\" 稀释了。\n- R1 认为 LP 失败和 disentanglement 有经验价值（部分同意），但当前 framing 混淆了定义性限制和经验性发现。\n\n**[N3] LP-alignment gating 使用 test set 构成 information leakage** [critical, 共识]\n- Gating protocol 使用 50 个 test set instances 估计 within-instance ρ(LP, F1)（需要 gold labels），再将 routing decision 应用于同一 test set。论文自述 \"probe instances are drawn from the test set for simplicity\"，但仍 claim \"correctly routes all three evaluated datasets\"。\n- §4.5 已增加三条 caveats（(a) test set probe, (b) only 3 datasets, (c) proof of concept），但 Contribution #3 仍包含 gating 的 correct routing claim。\n- 仅 3 个 dataset 验证（实际 2 个 informative data points），且 dataset 间 ρ 差距很大（>0.15），routing \"正确性\" 可能只是因为差距足够大。\n\n### Should-Fix（影响评分但不一票否决）\n\n**[W1] ε=0.05 non-tied subset 是 post-hoc 最优切点，Bonferroni 未覆盖 ε sweep** [warning, 共识]\n- ε sweep（Table 10）显示 ε=0.05 恰好是 p-value 最小的切点（p=0.004），相邻切点显著性更弱。主文 §4.2 \"survives Bonferroni correction\" 仅覆盖 5 signal comparisons，未覆盖 ε sweep 的 7 个阈值。7×5=35 Bonferroni 后 p_adj=0.14。\n- 论文已在 Limitations 标注 \"post-hoc exploratory choice\"，但主文叙事权重过高。\n\n**[W2] Expected selection gain \"bound\" 中 g(·) 未定义** [warning, 共识]\n- §4.3: E[ΔF1] ≤ (1-d) · Δ_oracle · g(ρ_within)，g(·) 描述为 \"monotonically increasing function\" 但从未定义。包含未定义函数的不等式不构成 bound。\n- 两位 Reviewer 共识：不需要形式化定理，但 \"bounded by\" 应改为 \"heuristically decomposed as\"，并给出 g(·) 的假设条件。\n\n**[W3] θ=2/N \"tuning-free\" claim 缺乏 θ sensitivity sweep** [warning, 共识]\n- §4.5 称 θ=2/N 是 \"tuning-free across all datasets\"，但仅对比了 θ=0.5 majority baseline。无 θ ∈ [1/N, 1] 的 sensitivity curve，无 precision/recall 分解。θ=2/N 在 N=8 时等于 0.25，大幅 boost recall，可能在 high-noise 场景引入 false positives。\n\n**[W4] SciERC greedy F1 出现 4 个值，协议不统一** [warning, 共识]\n- 0.640, 0.644, 0.645, 0.650 四个值跨 Tables 1-4 出现。§3.2 末尾有解释，但 Table 2 用 2-seed、Table 3 用 single-seed/3-seed、Table 7 用 3-seed 的不统一缺乏解释。\n\n**[W5] Complementarity claim 仅基于 3 dataset（2 个 informative data points）** [warning, 共识]\n- CoNLL 为 ceiling regime，两种方法都不 work。实际仅 SciERC（construction wins）和 Few-NERD（LP wins）两个 informative data points。\n\n**[W6] 模型规模 4B-8B，claims 表述过于一般化** [warning, 共识]\n- 标题 \"for NER\" 和 Contribution 2 无 scale 限定。Discussion \"degeneracy rises with model capability\" 仅基于 3B-8B。70B+ 行为未知。\n\n**[W7] Abstract 信息密度过高** [warning, 共识]\n- 约 10 个数字，读起来像实验报告压缩版。建议精简至 2-3 个关键数字。\n\n**[W8] Table 4 (entity construction) 缺少 multi-seed ±σ** [warning, 共识]\n- Prescriptive 贡献应有更强统计支撑。\n\n### Info（小问题）\n\n- [I1] Figure 1 caption ρ=0.39 vs Abstract ρ=0.45 scope 不一致（SciERC vs CoNLL）\n- [I2] WNUT-17 正文分析不足——Introduction 定位为 \"signal-collapse boundary\" 但主文仅一句提及\n- [I3] Table D.1 \"Identical\" vs 正文 \"Constant F1\" 概念不同（11% vs 17.8%），易混淆\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Overall 评分一致**：两位 Reviewer 独立给出 3/5 (Findings)，交叉回应后维持不变。\n2. **Entity construction 新颖性不足**：两位 Reviewer 均独立列为 critical 并在交叉回应中完全一致。\n3. **Test-set leakage in gating**：两位 Reviewer 均独立列为 critical 并完全一致。\n4. **θ=2/N、greedy F1 不一致、complementarity 仅 3 dataset、scale 限制**：全部共识。\n5. **统计严谨度和写作质量**：均给予高度肯定。\n\n## Reviewer Divergence [REBUT]\n\n1. **ε=0.05 严重度**：R1 列为 critical（Bonferroni 应覆盖 ε sweep），R2 同意统计问题但建议降为 warning（论文已做 hedging）。→ **最终判定：warning**（论文在 Limitations 和 Appendix 已承认 post-hoc 性质，需修改的是主文措辞而非删除分析）。\n\n2. **Expected gain bound 形式化**：R1 列为 critical（g(·) 未定义则 bound 无意义），R2 建议降为 warning（实证论文不需要定理）。→ **最终判定：warning**（修改措辞即可，无需正式证明）。\n\n3. **Epoch confound (Few-NERD 3-epoch)**：R2 列为 warning（未完全消解），R1 REBUT（Appendix E 提供了 3-point curve，5-epoch LP 仍 positive，已 adequately addressed）。→ **最终判定：不列入报告**（R1 反驳有理有据，Appendix 的 epoch ablation 覆盖充分）。\n\n4. **Selective prediction 定位**：R2 列为 warning（不应列为独立贡献），R1 REBUT（原文中是 Contribution 1 的子项而非独立贡献）。→ **最终判定：不列入报告**（R1 对原文结构的阅读准确）。\n\n5. **Appendix 体量**：R1 列为 info（7:1 ratio），R2 REBUT（ARR 无限制，材料对 reproducibility 有价值）。→ **最终判定：不列入报告**。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Entity-level construction 相对于 ensemble NER entity voting 的技术区别是什么？单模型多 sample vs 多模型是否产生不同的 diversity 特征？LP weighting 在 ensemble 设定下是否可行？\n\n**Q2.** Table 2 使用 \"2-seed mean\" 而 Table 3/7 使用 \"3-seed\"，为什么 selection analysis 的 seed 数量少于 QE analysis？\n\n**Q3.** LP-alignment gating 如果改用 held-out validation set（不接触 test set gold），routing decision 是否仍然 correct？\n\n**Q4.** §4.3 Expected selection gain decomposition 中 g(·) 的具体形式或假设条件是什么？\n\n**Q5.** θ=2/N 是如何确定的——先验理由还是基于性能选择？能否提供 θ 在 [1/N, 1] 范围内的 sensitivity curve 和 precision/recall 分解？\n\n**Q6.** §1 中 \"the first systematic empirical characterization\" 的 scope——相对于 Yao et al. 2026 和 Vashurin et al. 2025 (CoCoA)，\"first\" 具体指什么？\n\n**Q7.** Within-instance LP-quality alignment 的 SciERC vs Few-NERD 差异（ρ≈0.26 vs ≈0.5-0.7）是否可能由 entity type 数量（6 vs 8）或 domain shift 驱动？\n\n---\n\n## Missing References\n\n1. **Entity-level ensemble NER**: Florian et al. 2003 (\"Named Entity Recognition through Classifier Combination\")——entity-level construction 的最直接先行工作，应引用并讨论区别。\n2. **Zero-shot NER voting**: Luo et al. 2023 (Zero-shot NER with ChatGPT, self-annotation + voting)——与 entity-level construction 机制相关。\n3. **MBR decoding strategies**: Wiher et al. 2022 (\"On Decoding Strategies for Neural Text Generators\")——对 selection-gap 讨论有补充价值。\n4. **Selective prediction under domain shift**: Kamath et al. 2020 (\"Selective Question Answering under Domain Shift\")——补充 selective prediction 引用。\n5. **Test-time scaling 最新进展**: Muennighoff et al. 2025 (\"s1: Simple Test-Time Scaling\") 和/或 Qu et al. 2025 (\"Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning\")。\n\n---\n\n## Overall Assessment\n\n**评分: Weak Accept (Findings) / Borderline (Main Conference)**\n**置信度: 4/5 (High)**\n\n两位 Reviewer 一致评价为 3/5，推荐 Findings track。\n\n**核心判断**：这是一篇高质量的实证分析论文。统计方法论严谨度、消融覆盖广度、负面结果透明度均远高于同类工作。QE vs selection 的显式分离和 degeneracy/compression 双因素诊断框架有真实贡献。\n\n**制约因素**：\n- Entity-level construction 新颖性有限（本质是 entity-level majority voting），作为论文 \"Fixing\" 部分的核心贡献不足以支撑 main conference。\n- Correlation-selection gap 的概念中，4/5 signal 失败是定义性的，真正的经验贡献（LP 失败 + disentanglement）被稀释。\n- Gating protocol 存在 test-set leakage + 仅 3 dataset 验证。\n- Prescriptive claims（complementarity、gating、θ tuning-free）的证据强度与 claim 力度不匹配。\n\n**修复路径**：\n1. 在 Contribution framing 上将 entity construction 定位为 \"applying known technique to a new setting\" 而非方法创新，同时 strengthen diagnostic contribution 的叙事价值。\n2. 重构 correlation-selection gap：instance-level signal 失败作为 setup，聚焦 LP compression/alignment。\n3. Gating 降级为 proof of concept 或用 proper validation set 重新验证。\n4. 修复 g(·) 措辞、ε Bonferroni 范围说明、Abstract 数字精简、θ sensitivity sweep。\n\n如果以上修复到位，论文适合 **EMNLP Findings**。Main conference 需要更强的方法贡献（如理论化的 selection bound）或更广的 scale 覆盖。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度过高（~10 个数字），精简至 2-3 个关键数字\n- AUROC/LP 缩写定义需确认是否已展开\n\n### Introduction\n- Contribution 2 和标题需加入 \"fine-tuned / 4B-8B\" scope 限定\n- \"first systematic empirical characterization\" 需相对于 Yao et al. 2026 / CoCoA 更精确界定 scope\n- WNUT-17 的 \"signal-collapse boundary\" 角色定位与正文覆盖不匹配\n\n### Related Work\n- 缺少 entity-level ensemble NER 的覆盖（Florian et al. 2003 等）\n- 缺少 selective prediction 和 test-time scaling 的最新引用\n\n### Method\n- Entity matching 标准分散在 §3.2 各段落，建议统一展示\n- Expected selection gain decomposition (§4.3): \"bounded by\" → \"heuristically decomposed as\"\n\n### Experiments\n- Table 2 vs 3 vs 7 的 seed 数量不统一需解释\n- Table 4 缺少 multi-seed ±σ\n- §4.2 \"survives Bonferroni correction\" 需说明 correction 范围\n\n### Discussion\n- 篇幅极短（11 行），与 Experiments 的体量不成比例\n- 正文空间可能紧张——需确认编译后 ≤8 页\n\n### Conclusion\n- 实用建议（LP selection when ρ≈0.3, otherwise construction）清晰有用\n\n### Limitations\n- 覆盖全面，堪称范例\n\n### Appendix\n- 体量大但内容对 reproducibility 有价值\n- Figure 1 caption scope 需与 Abstract 一致",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak accept (findings) / borderline (main conference)"
  }
}
```

</details>

---


### Tool result

_source line 2356 · 2026-05-19T05:08:38.251450+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3963
}
```

</details>

---


### Assistant

_source line 2357 · 2026-05-19T05:08:46.067726+00:00_

审稿报告已投递至 Research Director。

---

**本轮审稿完成总结**：

- **评分**: Weak Accept (Findings) / Borderline (Main Conference)
- **2 名 Reviewer 独立评审 + 交叉回应**，在核心评判上高度一致
- **3 个 Critical 问题**：entity construction 新颖性不足、correlation-selection gap 概念深度有限、gating protocol test-set leakage
- **8 个 Warning 问题**：ε Bonferroni 范围、g(·) 未定义、θ sensitivity、greedy F1 不一致、complementarity 仅 3 dataset、scale 限定、Abstract 密度、Table 4 缺 ±σ
- **5 条缺失引用**
- **Issue Tracker 已同步更新**（`artifacts/review_issues.yaml`）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 182

## Round 182

2 recorded events


### User

_source line 2358 · 2026-05-19T05:08:48.714794+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

与 R1 在绝大多数问题上达成共识（8/12 完全一致），在 3 个问题上对严重程度有不同判断：
- **ε=0.05 non-tied subset**：同意统计瑕疵，但论文已有 hedging，建议降为 warning
- **Expected selection gain bound**：同意措辞不当，但不需要形式化定理，降级措辞即可
- **Appendix 体量**：不同意是问题，正文 self-contained，appendix 对 reproducibility 有价值

两位 reviewer 均给出 3/5 (Findings)，核心共识：实验严谨但新颖性不足以进入 main conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2359 · 2026-05-19T05:09:00.918385+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结**：

- **评分**: Weak Accept (Findings) / Borderline (Main Conference)
- **两位 Reviewer 独立评分一致**: 3/5，交叉回应后维持不变
- **3 个 Critical 共识**: entity construction 新颖性不足、correlation-selection gap 概念深度有限、gating test-set leakage
- **8 个 Warning**: ε Bonferroni 范围、g(·) 未定义、θ sensitivity、greedy F1 不一致、complementarity 仅 2 data points、scale 限制、Abstract 数字过多、Table 4 缺 ±σ
- **核心判断**: 统计严谨度和消融覆盖远高于同类工作，但方法创新不足以支撑 main conference；修复 prescriptive claims 后适合 Findings track

Issue Tracker 已同步更新（`artifacts/review_issues.yaml`），含 Round 23 全部新增 issue 和历史 issue 状态追踪。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 183

## Round 183

2 recorded events


### User

_source line 2360 · 2026-05-19T05:17:15.652878+00:00_

[RESET REQUEST] Research Reviewer 达到硬限
  触发原因：运行时长 16h19m
  本轮累计 124 条消息 / 16h 19min

⚠️ 你自己的 context 状态：已 124 条消息 / 16h 19min

请回复：
  [RESET AGENT]     只重置 Research Reviewer，你继续
  [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛）
  [DEFER Xm]        Xm 后再说
  [DENY <原因>]     不重置，让 Research Reviewer 继续带着上下文工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 2361 · 2026-05-19T05:17:26.501931+00:00_

审稿报告已成功提交，所有流程已完成。

**[RESET BOTH]**

本轮圆桌审稿已收敛并投递：
- 2 位 Reviewer 独立审稿 + 交叉回应全部完成
- Issue Tracker 已同步（Round 23 新增 8 open issues）
- 最终报告已通过 `submit_review_report_to_research_director` 投递
- Overall: **Weak Accept (Findings) / Borderline (Main Conference)**

无未完成工作，推荐双方都重置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 184

## Round 184

2 recorded events


### User

_source line 2362 · 2026-05-19T05:30:00.790510+00:00_

[SYSTEM] Research Reviewer 刚完成 context rotation (Loop 16)，已读取 handoff 并就绪。如有待办任务请立即分配。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 2363 · 2026-05-19T05:30:11.506390+00:00_

审稿报告已于本轮提交完成，无待办任务需要分配给 Research Reviewer。

当前状态：
- Round 23 审稿报告已通过 `submit_review_report_to_research_director` 投递
- Issue Tracker (`review_issues.yaml`) 已同步更新
- 两位 Reviewer 的独立审稿 + 交叉回应均已完成并收敛
- 评分：**Weak Accept (Findings) / Borderline (Main Conference)**

审稿阶段工作已全部完成，等待 Research Director 处理报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 185

## Round 185

116 recorded events


### User

_source line 2364 · 2026-05-19T06:06:55.852779+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2365 · 2026-05-19T06:07:02.756287+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2366 · 2026-05-19T06:07:02.756917+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2367 · 2026-05-19T06:07:05.517588+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2368 · 2026-05-19T06:07:05.568177+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2369 · 2026-05-19T06:07:10.383802+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 2370 · 2026-05-19T06:07:10.434376+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2371 · 2026-05-19T06:07:14.248064+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 2372 · 2026-05-19T06:07:14.399078+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2373 · 2026-05-19T06:07:17.360094+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 2374 · 2026-05-19T06:07:18.012971+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (166 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_llama_fewnerd_inference** (success): LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness. ← 基于 exp_llama_fewnerd_lora\n- **exp_entity_construction** (success): Entity-level majority vote construction is the correct self-consistency analogy for structured IE: instead of selecting the best instance-level output, assemble a better output from entity-level consensus across N samples. Construction should outperform both greedy and best-of-N selection.\n- **exp_lp_alignment_gating** (success): Within-instance LP-F1 alignment score (adjusted by valid_ratio for degeneracy) can automatically gate whether LP selection should be applied to a dataset. A small probe sample (50-100 instances) suffices for a stable gating decision.\n\n## 趋势\n成功 101 / 负向 33 / 失败 4 / 共 166\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\nautodl-5090-b: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\nautodl-5090-c: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\
…[truncated 1355 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 2375 · 2026-05-19T06:07:18.013585+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool result

_source line 2376 · 2026-05-19T06:07:25.303894+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"}]

Based on the search results, here's the key information about EMNLP 2026:

## Submission Deadline

The ARR submission deadline for long and short papers is May 25, 2026.

## Important Dates

Additional key dates include: reviewer registration deadline for all authors on M
…[truncated 1251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7290
}
```

</details>

---


### Tool call

_source line 2377 · 2026-05-19T06:07:30.274577+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 page limit template format ACL Rolling Review submission guidelines long paper short paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 page limit template format ACL Rolling Review submission guidelines long paper short paper"
  }
}
```

</details>

---


### Tool call

_source line 2378 · 2026-05-19T06:07:31.930456+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2379 · 2026-05-19T06:07:31.981396+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Diagnosing and Resolving Self-Consistency for Named Entity Recognition}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\section*{Responsible NLP Research Checklist}
47	\input{sections/checklist}
48	
49	\bibliography{references}
50	
51	\appendix
52	\input{sections/appendix}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2380 · 2026-05-19T06:07:35.795413+00:00_

Web search results for query: "EMNLP 2026 page limit template format ACL Rolling Review submission guidelines long paper short paper"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"}]

Based on the search results, here's information about EMNLP 2026 submission guidelines regarding page limits, template format, and ACL Rolling Review requirements:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

## Template and Format

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences, available at github.com/acl-org/acl-style-files.

## Limitations Section

The mandatory Limitations section is required, placed after the conclusion.

## ACL Rolling Review Submission

All submissions go through ACL Rol
…[truncated 380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5520
}
```

</details>

---


### Tool call

_source line 2381 · 2026-05-19T06:07:46.613875+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read all paper sections",
  "subagent_type": "Explore",
  "prompt": "Read all the following files completely and return their full contents. These are sections of an academic paper:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex\n4. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex\n5. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex\n6. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex\n7. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex\n8. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex\n9. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex\n10. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex\n11. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib\n\nReturn the FULL content of each file, labeled clearly by filename. Do not summarize or truncate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Read all paper sections",
    "subagent_type": "Explore",
    "prompt": "Read all the following files completely and return their full contents. These are sections of an academic paper:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex\n4. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex\n5. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex\n6. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex\n7. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex\n8. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex\n9. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex\n10. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex\n11. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib\n\nReturn the FULL content of each file, labeled clearly by filename. Do not summarize or truncate."
  }
}
```

</details>

---


### Tool call

_source line 2382 · 2026-05-19T06:07:47.065750+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool call

_source line 2383 · 2026-05-19T06:07:48.219534+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2384 · 2026-05-19T06:07:48.370314+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using fine-tuned 4B\textendash 8B models.
4	All signals achieve reliable QE ($\rho$ up to 0.45, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
5	For instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \textbf{correlation-selection gap}).
6	We diagnose two causes: instance degeneracy and weak LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction.
7	The diagnostic naturally motivates entity-level \textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC (multi-seed mean, $p{<}0.005$). Construction and LP selection are complementary, governed by LP-quality alignment.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2385 · 2026-05-19T06:07:48.521247+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2386 · 2026-05-19T06:07:48.571841+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
8	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we provide the first systematic empirical characterization of \textit{when and why} LP-based selection succeeds or fails for structured prediction, diagnosing degeneracy and compression as the two blocking mechanisms.
9	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.
10	
11	A key distinction structures our analysis: four of five signals (Soft Jaccard, voting confidence, Fleiss' $\kappa$, exact match) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction.
13	For selection, LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) in settings where both low inst
…[truncated 4606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2387 · 2026-05-19T06:07:48.572278+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2388 · 2026-05-19T06:07:48.823450+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} rely on answer-level agreement.
6	Adaptive variants gate on answer agreement \cite{aggarwal2023adaptive}, input difficulty \cite{wang2025make, feng2025optimal}, or response confidence \cite{kim2026reasc}; \citet{chen2025twofailures} diagnose SC failure modes without proposing gating.
7	All target discrete-answer reasoning; structured prediction requires different gating signals because degeneracy operates at the entity-set level.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation alone does not ensure selection gains, diagnosing degeneracy and compression as blocking mechanisms.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\S\ref{sec:robustness_main}).
12	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
13	Ensemble approaches aggregate predictions from multiple models or prompts \cite{florian2003named, xiao2025el4ner}; our entity-level construction similarly aggregates across samples from a single model, without requiring model diversity.
14	Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting, xie2024selfimproving} and constrained decoding \cite{willard2023guided, dong2024xgrammar, park2024grammar, sch
…[truncated 1966 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2389 · 2026-05-19T06:07:48.823816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2390 · 2026-05-19T06:07:49.225483+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Throughout, entity matching uses exact span and type match (a predicted entity is correct iff its character offsets and type label both match a gold entity).
12	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
13	
14	\paragraph{Log-probability (model-internal, per-sample).}
15	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
16	\begin{equation}\label{eq:logprob}
17	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
18	\end{equation}
19	
20	\paragraph{Exact match voting (surface, instance-level).}
21	The proportion of samples producing the most common output:
22	\begin{equation}\label{eq:em}
23	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
24	\end{equation}
25	
26	\paragraph{Fleiss' $\kappa$ (surface, insta
…[truncated 4000 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2391 · 2026-05-19T06:07:49.225844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2392 · 2026-05-19T06:07:49.426860+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (training details in Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others due to earlier convergence; Appendix~\ref{app:epoch_confound}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\ref{app:n_scaling}).
17	
18	%% ============================================================
19	\subsection{Quality Estimation Results}
20	\label{sec:qe_results}
21	
22	\begin{table*}[t]
23	\centering
24	\small
25	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
26	\label{tab:quality_estimation}
27	\begin{tabular}{ll cc cc cc}
28	\topr
…[truncated 16694 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2393 · 2026-05-19T06:07:49.427304+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2394 · 2026-05-19T06:07:49.628297+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; effective selection likely requires content-aware verifiers \cite{cobbe2021verifiers, venktesh2025trust}.
4	Two factors constrain selection: instance degeneracy (17.8--48.4\%) eliminates headroom, and LP compression (within-instance $\rho$ 0.262--0.667) prevents exploiting the remainder; within non-degenerate instances, MBR utility correlates positively with F1 (SJ median $\rho{=}0.524$) \cite{eikema2022sampling}.
5	Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP selection yields $+2.9$~pp ($p{=}0.004$, surviving Bonferroni across 5 signals; Table~\ref{tab:nontied_main}). However, $\varepsilon{=}0.05$ is selected post-hoc from a 7-point sweep (Appendix~\ref{app:epsilon_robustness}); joint correction across thresholds and signals yields $p_{\text{adj}}{=}0.14$, so this finding is exploratory evidence for LP compression's role in the selection bottleneck.
6	Temperature disentangles the two factors: at $T{=}1.2$, degeneracy drops to 14.9\% yet LP does not improve ($\rho{=}0.225$ vs.\ Few-NERD ${\sim}$0.5--0.7; Table~\ref{tab:t_degeneracy}); degeneracy rises with model scale and training convergence (Tables~\ref{tab:scale_ablation}, \ref{tab:epoch_confound}), so the selection window narrows as models improve \cite{wang2023selfconsistency, snell2025scaling}.
7	
8	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
9	Entity-level construction bypasses both failure mechanisms ($+1.40$\,pp Few-NERD, $+1.02$\,pp SciERC, multi-seed mean; Table~\ref{tab:entity_construction}), complementary with LP selection and governed by LP-quality alignment (\S\ref{sec:prescriptive}).
10	Alternative strategies (DALS, MBR, DGS) fail to reliably beat greedy (Appendix~\ref{app:dals}).
11	Our negative results are specific to fine-tuned models with constrained decoding; settings with greater outp
…[truncated 90 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 2395 · 2026-05-19T06:07:49.628661+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2396 · 2026-05-19T06:07:49.829589+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	Five confidence signals achieve reliable NER quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
4	Instance-level selection fails due to degeneracy and LP compression, but the diagnostic naturally motivates entity-level construction, adapting entity voting to stochastic sampling: LP-weighted aggregation yields $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC (multi-seed mean, $p{<}0.005$).
5	Construction and LP selection are complementary on two informative datasets (SciERC and Few-NERD; CoNLL operates in a ceiling regime), governed by LP-quality alignment.
6	For practitioners: use QE-based selective prediction when deployment requires reliability guarantees; apply entity construction when multi-sample generation is feasible; assess LP-alignment via held-out validation to choose between construction and LP selection.
7	As models improve, degeneracy rises and the selection window narrows; content-aware verifiers \cite{cobbe2021verifiers} may be needed to close the remaining gap.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 2397 · 2026-05-19T06:07:49.829966+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2398 · 2026-05-19T06:07:50.030994+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and these two factors may shift in opposite directions.
3	Our supervised approaches (DeBERTa verifier, hidden state probes, MLP/RF on signal combinations) all fail to close the oracle gap; whether content-aware verifiers with access to task-specific structure could succeed remains open.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{lin2022teaching, tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app
…[truncated 1951 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2399 · 2026-05-19T06:07:50.081740+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 2400 · 2026-05-19T06:07:50.283340+00:00_

1	% Responsible NLP Research Checklist
2	% Following the ACL Rolling Review guidelines:
3	% https://aclrollingreview.org/responsibleNLPresearch/
4	
5	\subsection*{A\hspace{0.5em} For Every Submission}
6	
7	\begin{enumerate}
8	\item[A1.] \textbf{Did you discuss the limitations of your work?}\\
9	Yes. See the Limitations section after the Conclusion.
10	
11	\item[A2.] \textbf{Did you discuss any potential risks of your work?}\\
12	Yes. See the Ethics Statement. This work analyzes existing confidence signals for NER and identifies when they fail; the findings reduce risk of deploying unreliable confidence-based selection in production systems. No dual-use concerns.
13	
14	\item[A3.] \textbf{Do the abstract and introduction summarize the paper's main claims?}\\
15	Yes. The Abstract and Section~\ref{sec:introduction} (3 enumerated contributions) summarize all main claims with supporting evidence pointers.
16	\end{enumerate}
17	
18	\subsection*{B\hspace{0.5em} Did you use or create scientific artifacts?}
19	
20	Yes. We use existing datasets and pre-trained models.
21	
22	\begin{enumerate}
23	\item[B1.] \textbf{Did you cite the creators of artifacts you used?}\\
24	Yes. All datasets are cited: SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, Few-NERD \cite{ding2021fewnerd}, WNUT-17 \cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \cite{zheng2024llamafactory}. Constrained decoding: XGrammar \cite{dong2024xgrammar}. See Sections~\ref{sec:introduction}, \ref{sec:evaluation}, and Appendix~\ref{app:training}.
25	
26	\item[B2.] \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\\
27	Partially. The Ethics Statement notes that CoNLL-2003 is derived from the Reuters RCV1 corpus, available under a NIST agreement for research. SciERC, Few-NERD, and WNUT-17 are publicly available research benchmarks. Qwen3 and LLaMA-3.1 are open-weight models released under their r
…[truncated 4168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2401 · 2026-05-19T06:07:50.283818+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2402 · 2026-05-19T06:07:50.635462+00:00_

File content (41711 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2403 · 2026-05-19T06:07:50.686089+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 2404 · 2026-05-19T06:07:50.887390+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{vijayakumar2018diverse,
4	  title = {Diverse Beam Search for Improved Description of Complex Scenes},
5	  author = {Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and Sun, Qing and Lee, Stefan and Crandall, David J. and Batra, Dhruv},
6	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
7	  year = {2018},
8	  url = {https://arxiv.org/abs/1610.02424}
9	}
10	
11	@inproceedings{shi2022mbr,
12	  title = {Natural Language to Code Translation with Execution},
13	  author = {Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and Wang, Sida I.},
14	  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
15	  pages = {3533--3546},
16	  year = {2022},
17	  url = {https://arxiv.org/abs/2204.11454}
18	}
19	
20	@article{eisenstein2023helping,
21	  title = {Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking},
22	  author = {Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D'Amour, Alex and Dvijotham, DJ and Fisch, Adam and Heller, Katherine and Pfohl, Stephen and Ramachandran, Deepak and Shaw, Peter and Berant, Jonathan},
23	  journal = {arXiv preprint arXiv:2312.09244},
24	  year = {2023},
25	  url = {https://arxiv.org/abs/2312.09244}
26	}
27	
28	@article{brown2024monkeys,
29	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
30	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
31	  journal = {arXiv preprint arXiv:2407.21787},
32	  year = {2024},
33	  url = {https://arxiv.org/abs/2407.21787}
34	}
35	
36	@inproceedings{chen2024usc,
37	  title = {Universal Self-Consistency for Large Language Model Generation},
38	  author = {Chen, Xinyun and Aksitov, Renat and Alon, 
…[truncated 32874 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2405 · 2026-05-19T06:07:53.670678+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "5000",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "5000",
    "offset": "0"
  }
}
```

</details>

---


### Tool result

_source line 2406 · 2026-05-19T06:07:54.078788+00:00_

File content (41711 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 408
}
```

</details>

---


### Tool call

_source line 2407 · 2026-05-19T06:07:54.079263+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "5000",
  "offset": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "5000",
    "offset": "5000"
  }
}
```

</details>

---


### Tool result

_source line 2408 · 2026-05-19T06:07:54.332319+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (5000). The file has 1572 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 2409 · 2026-05-19T06:07:54.332671+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "5000",
  "offset": "10000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "5000",
    "offset": "10000"
  }
}
```

</details>

---


### Tool result

_source line 2410 · 2026-05-19T06:07:54.734444+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (10000). The file has 1572 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2411 · 2026-05-19T06:07:54.734790+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "5000",
  "offset": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "5000",
    "offset": "15000"
  }
}
```

</details>

---


### Tool result

_source line 2412 · 2026-05-19T06:07:54.885599+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (15000). The file has 1572 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2413 · 2026-05-19T06:07:55.136878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "5000",
  "offset": "20000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "5000",
    "offset": "20000"
  }
}
```

</details>

---


### Tool result

_source line 2414 · 2026-05-19T06:07:55.337996+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (20000). The file has 1572 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2415 · 2026-05-19T06:07:55.539154+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "5000",
  "offset": "25000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "5000",
    "offset": "25000"
  }
}
```

</details>

---


### Tool result

_source line 2416 · 2026-05-19T06:07:55.740387+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (25000). The file has 1572 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2417 · 2026-05-19T06:07:55.740781+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "5000",
  "offset": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "5000",
    "offset": "30000"
  }
}
```

</details>

---


### Tool result

_source line 2418 · 2026-05-19T06:07:56.142827+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (30000). The file has 1572 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2419 · 2026-05-19T06:07:56.143287+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "5000",
  "offset": "35000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "5000",
    "offset": "35000"
  }
}
```

</details>

---


### Tool result

_source line 2420 · 2026-05-19T06:07:56.144335+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (35000). The file has 1572 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 2421 · 2026-05-19T06:07:57.598839+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex\""
  }
}
```

</details>

---


### Tool result

_source line 2422 · 2026-05-19T06:07:57.749535+00:00_

1571 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2423 · 2026-05-19T06:07:59.305432+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex\" 2>&1 | head -n 400"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex\" 2>&1 | head -n 400"
  }
}
```

</details>

---


### Tool result

_source line 2424 · 2026-05-19T06:07:59.557319+00:00_

&lt;persisted-output>
Output too large (29.7KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/9f2c1894-7971-40f3-8763-3fcf305a1aad/tool-results/byi7pwnbe.txt

Preview (first 2KB):
\section{Notation}\label{app:notation}

Table~\ref{tab:notation} summarizes the notation used throughout the paper.

\begin{table}[h]
\centering
\small
\begin{tabular}{cl}
\toprule
Symbol & Meaning \\
\midrule
$\mathcal{M}$ & Language model \\
$x$ & Input instance \\
$y_i$ & $i$-th stochastic sample \\
$N$ & Number of samples \\
$T$ & Sampling temperature \\
$c(\cdot)$ & Confidence signal \\
SJ & Soft Jaccard similarity \\
FK & Fleiss' $\kappa$ \\
EM & Exact-match voting rate \\
VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
\bottomrule
\end{tabular}
\caption{Notation used throughout the paper.}
\label{tab:notation}
\end{table}

\section{Robustness Analysis}\label{app:robustness}

We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.

\begin{table}[t]
\centering
\small
\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
\label{tab:robustness}
\begin{tabular}{llcc}
\toprule
& & NER $\rho$ & RE $\rho$ \\
\midrule
\multicolumn{4}
…[truncated 322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2425 · 2026-05-19T06:07:59.557733+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex\" 2>&1 | tail -n 1200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex\" 2>&1 | tail -n 1200"
  }
}
```

</details>

---


### Tool result

_source line 2426 · 2026-05-19T06:07:59.608148+00:00_

&lt;persisted-output>
Output too large (79.8KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/9f2c1894-7971-40f3-8763-3fcf305a1aad/tool-results/b48aexb1c.txt

Preview (first 2KB):
Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to single-sample within a bound $\delta$.
The $\delta$ values are contextualized against oracle headroom (12--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
These proportions use the same test data that defines the headroom, introducing circularity: $\delta$ is anchored to the very quantity it contextualizes.
We address this below with externally anchored equivalence margins.
The breakpoint $\delta^*$, the minimum equivalence margin at which each signal passes TOST, ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.

\begin{table}[t]
\centering
\small
\caption{TOST equivalence testing: signals vs.\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ single-sample).
…[truncated 285 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2427 · 2026-05-19T06:08:01.313365+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex\""
  }
}
```

</details>

---


### Tool result

_source line 2428 · 2026-05-19T06:08:01.365316+00:00_

&lt;persisted-output>
Output too large (107.1KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/9f2c1894-7971-40f3-8763-3fcf305a1aad/tool-results/bv0gotcnl.txt

Preview (first 2KB):
\section{Notation}\label{app:notation}

Table~\ref{tab:notation} summarizes the notation used throughout the paper.

\begin{table}[h]
\centering
\small
\begin{tabular}{cl}
\toprule
Symbol & Meaning \\
\midrule
$\mathcal{M}$ & Language model \\
$x$ & Input instance \\
$y_i$ & $i$-th stochastic sample \\
$N$ & Number of samples \\
$T$ & Sampling temperature \\
$c(\cdot)$ & Confidence signal \\
SJ & Soft Jaccard similarity \\
FK & Fleiss' $\kappa$ \\
EM & Exact-match voting rate \\
VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
\bottomrule
\end{tabular}
\caption{Notation used throughout the paper.}
\label{tab:notation}
\end{table}

\section{Robustness Analysis}\label{app:robustness}

We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.

\begin{table}[t]
\centering
\small
\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
\label{tab:robustness}
\begin{tabular}{llcc}
\toprule
& & NER $\rho$ & RE $\rho$ \\
\midrule
\multicolumn{4
…[truncated 323 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2429 · 2026-05-19T06:08:04.244931+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/9f2c1894-7971-40f3-8763-3fcf305a1aad/tool-results/bv0gotcnl.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/9f2c1894-7971-40f3-8763-3fcf305a1aad/tool-results/bv0gotcnl.txt"
  }
}
```

</details>

---


### Tool result

_source line 2430 · 2026-05-19T06:08:04.546208+00:00_

File content (41711 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2431 · 2026-05-19T06:08:06.503511+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -c 100000 \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "head -c 100000 \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex\""
  }
}
```

</details>

---


### Tool result

_source line 2432 · 2026-05-19T06:08:06.554112+00:00_

&lt;persisted-output>
Output too large (97.7KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/9f2c1894-7971-40f3-8763-3fcf305a1aad/tool-results/bcbpq73rf.txt

Preview (first 2KB):
\section{Notation}\label{app:notation}

Table~\ref{tab:notation} summarizes the notation used throughout the paper.

\begin{table}[h]
\centering
\small
\begin{tabular}{cl}
\toprule
Symbol & Meaning \\
\midrule
$\mathcal{M}$ & Language model \\
$x$ & Input instance \\
$y_i$ & $i$-th stochastic sample \\
$N$ & Number of samples \\
$T$ & Sampling temperature \\
$c(\cdot)$ & Confidence signal \\
SJ & Soft Jaccard similarity \\
FK & Fleiss' $\kappa$ \\
EM & Exact-match voting rate \\
VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
\bottomrule
\end{tabular}
\caption{Notation used throughout the paper.}
\label{tab:notation}
\end{table}

\section{Robustness Analysis}\label{app:robustness}

We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.

\begin{table}[t]
\centering
\small
\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
\label{tab:robustness}
\begin{tabular}{llcc}
\toprule
& & NER $\rho$ & RE $\rho$ \\
\midrule
\multicolumn{4}
…[truncated 322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2433 · 2026-05-19T06:08:17.643649+00:00_

Let me read the actual saved file which contains the full appendix:

Based on the successful reads I've already completed and the file saved by bash, here is the full content of all the requested files:

## 1. abstract.tex

```latex
\begin{abstract}
Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using fine-tuned 4B\textendash 8B models.
All signals achieve reliable QE ($\rho$ up to 0.45, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80% coverage).
For instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \textbf{correlation-selection gap}).
We diagnose two causes: instance degeneracy and weak LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction.
The diagnostic naturally motivates entity-level \textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC (multi-seed mean, $p{<}0.005$). Construction and LP selection are complementary, governed by LP-quality alignment.
\end{abstract}
```

## 2. introduction.tex

(Full content as read - 44 lines)

## 3. related_work.tex

(Full content as read - 26 lines)

## 4. method.tex

(Full content as read - 66 lines)

## 5. experiments.tex

(Full content as read - 227 lines)

## 6. discussion.tex

(Full content as read - 12 lines)

## 7. conclusion.tex

(Full content as read - 7 lines)

## 8. limitations.tex

(Full content as read - 16 lines)

## 9. checklist.tex

(Full content as read - 70 lines)

## 10. appendix.tex

The appendix file is very large (41,711 to
…[truncated 1241 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Agent",
  "elapsed_ms": 31029
}
```

</details>

---


### Tool result

_source line 2434 · 2026-05-19T06:08:17.644202+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: '2026-05-14T21:00:00.000Z'\\n  total_papers: 55\\ncategories: []\\npapers:\\n  wang2023selfconsistency:\\n    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models\\n    authors:\\n    - Xuezhi Wang\\n    - Jason Wei\\n    - Dale Schuurmans\\n    - Quoc Le\\n    - Ed Chi\\n    - Sharan Narang\\n    - Aakanksha Chowdhery\\n    - Denny Zhou\\n    year: 2023\\n    venue: ICLR 2023\\n    url: https://arxiv.org/abs/2203.11171\\n    doi: ''\\n    bibtex_key: wang2023selfconsistency\\n    category: self_consistency_reasoning\\n    role: foundation\\n    relevance: 'Foundation paper: introduces self-consistency voting over diverse reasoning paths. We extend this paradigm\\n      from closed-form answers to structured IE outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  taubenfeld2025cisc:\\n    title: Confidence Improves Self-Consistency in LLMs\\n    authors:\\n    - Amir Taubenfeld\\n    - Tom Sheffer\\n    - Eran Ofek\\n    - Amir Feder\\n    - Ariel Goldstein\\n    - Zorik Gekhman\\n    - Gal Yona\\n    year: 2025\\n    venue: ACL Findings 2025\\n    url: https://arxiv.org/abs/2502.06233\\n    doi: 10.18653/v1/2025.findings-acl.1030\\n    bibtex_key: taubenfeld2025cisc\\n    category: self_consistency_reasoning\\n    role: direct-competitor\\n    relevance: 'CISC: confidence-weighted majority vote reduces required samples by 40%. Direct competitor — we address the\\n      same \\\"strong predictor, weak selector\\\" gap but for structured outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  kang2025selfcertainty:\\n    title: 
…[truncated 3614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 30578
}
```

</details>

---


### Tool call

_source line 2435 · 2026-05-19T06:08:21.373297+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2436 · 2026-05-19T06:08:21.875445+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using fine-tuned 4B\textendash 8B models.
4	All signals achieve reliable QE ($\rho$ up to 0.45, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
5	For instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \textbf{correlation-selection gap}).
6	We diagnose two causes: instance degeneracy and weak LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction.
7	The diagnostic naturally motivates entity-level \textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC (multi-seed mean, $p{<}0.005$). Construction and LP selection are complementary, governed by LP-quality alignment.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2437 · 2026-05-19T06:08:21.875865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2438 · 2026-05-19T06:08:22.328073+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
8	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we provide the first systematic empirical characterization of \textit{when and why} LP-based selection succeeds or fails for structured prediction, diagnosing degeneracy and compression as the two blocking mechanisms.
9	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.
10	
11	A key distinction structures our analysis: four of five signals (Soft Jaccard, voting confidence, Fleiss' $\kappa$, exact match) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction.
13	For selection, LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) in settings where both low inst
…[truncated 4606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2439 · 2026-05-19T06:08:22.328568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2440 · 2026-05-19T06:08:22.830151+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} rely on answer-level agreement.
6	Adaptive variants gate on answer agreement \cite{aggarwal2023adaptive}, input difficulty \cite{wang2025make, feng2025optimal}, or response confidence \cite{kim2026reasc}; \citet{chen2025twofailures} diagnose SC failure modes without proposing gating.
7	All target discrete-answer reasoning; structured prediction requires different gating signals because degeneracy operates at the entity-set level.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation alone does not ensure selection gains, diagnosing degeneracy and compression as blocking mechanisms.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\S\ref{sec:robustness_main}).
12	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
13	Ensemble approaches aggregate predictions from multiple models or prompts \cite{florian2003named, xiao2025el4ner}; our entity-level construction similarly aggregates across samples from a single model, without requiring model diversity.
14	Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting, xie2024selfimproving} and constrained decoding \cite{willard2023guided, dong2024xgrammar, park2024grammar, sch
…[truncated 1966 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 2441 · 2026-05-19T06:08:22.830527+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2442 · 2026-05-19T06:08:23.733326+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Throughout, entity matching uses exact span and type match (a predicted entity is correct iff its character offsets and type label both match a gold entity).
12	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
13	
14	\paragraph{Log-probability (model-internal, per-sample).}
15	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
16	\begin{equation}\label{eq:logprob}
17	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
18	\end{equation}
19	
20	\paragraph{Exact match voting (surface, instance-level).}
21	The proportion of samples producing the most common output:
22	\begin{equation}\label{eq:em}
23	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
24	\end{equation}
25	
26	\paragraph{Fleiss' $\kappa$ (surface, insta
…[truncated 4000 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 902
}
```

</details>

---


### Tool call

_source line 2443 · 2026-05-19T06:08:23.733678+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2444 · 2026-05-19T06:08:24.235431+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (training details in Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others due to earlier convergence; Appendix~\ref{app:epoch_confound}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\ref{app:n_scaling}).
17	
18	%% ============================================================
19	\subsection{Quality Estimation Results}
20	\label{sec:qe_results}
21	
22	\begin{table*}[t]
23	\centering
24	\small
25	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
26	\label{tab:quality_estimation}
27	\begin{tabular}{ll cc cc cc}
28	\topr
…[truncated 16694 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 2445 · 2026-05-19T06:08:24.235875+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2446 · 2026-05-19T06:08:24.687540+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; effective selection likely requires content-aware verifiers \cite{cobbe2021verifiers, venktesh2025trust}.
4	Two factors constrain selection: instance degeneracy (17.8--48.4\%) eliminates headroom, and LP compression (within-instance $\rho$ 0.262--0.667) prevents exploiting the remainder; within non-degenerate instances, MBR utility correlates positively with F1 (SJ median $\rho{=}0.524$) \cite{eikema2022sampling}.
5	Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP selection yields $+2.9$~pp ($p{=}0.004$, surviving Bonferroni across 5 signals; Table~\ref{tab:nontied_main}). However, $\varepsilon{=}0.05$ is selected post-hoc from a 7-point sweep (Appendix~\ref{app:epsilon_robustness}); joint correction across thresholds and signals yields $p_{\text{adj}}{=}0.14$, so this finding is exploratory evidence for LP compression's role in the selection bottleneck.
6	Temperature disentangles the two factors: at $T{=}1.2$, degeneracy drops to 14.9\% yet LP does not improve ($\rho{=}0.225$ vs.\ Few-NERD ${\sim}$0.5--0.7; Table~\ref{tab:t_degeneracy}); degeneracy rises with model scale and training convergence (Tables~\ref{tab:scale_ablation}, \ref{tab:epoch_confound}), so the selection window narrows as models improve \cite{wang2023selfconsistency, snell2025scaling}.
7	
8	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
9	Entity-level construction bypasses both failure mechanisms ($+1.40$\,pp Few-NERD, $+1.02$\,pp SciERC, multi-seed mean; Table~\ref{tab:entity_construction}), complementary with LP selection and governed by LP-quality alignment (\S\ref{sec:prescriptive}).
10	Alternative strategies (DALS, MBR, DGS) fail to reliably beat greedy (Appendix~\ref{app:dals}).
11	Our negative results are specific to fine-tuned models with constrained decoding; settings with greater outp
…[truncated 90 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2447 · 2026-05-19T06:08:24.687899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2448 · 2026-05-19T06:08:24.989099+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	Five confidence signals achieve reliable NER quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
4	Instance-level selection fails due to degeneracy and LP compression, but the diagnostic naturally motivates entity-level construction, adapting entity voting to stochastic sampling: LP-weighted aggregation yields $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC (multi-seed mean, $p{<}0.005$).
5	Construction and LP selection are complementary on two informative datasets (SciERC and Few-NERD; CoNLL operates in a ceiling regime), governed by LP-quality alignment.
6	For practitioners: use QE-based selective prediction when deployment requires reliability guarantees; apply entity construction when multi-sample generation is feasible; assess LP-alignment via held-out validation to choose between construction and LP selection.
7	As models improve, degeneracy rises and the selection window narrows; content-aware verifiers \cite{cobbe2021verifiers} may be needed to close the remaining gap.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2449 · 2026-05-19T06:08:24.989454+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2450 · 2026-05-19T06:08:25.039923+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and these two factors may shift in opposite directions.
3	Our supervised approaches (DeBERTa verifier, hidden state probes, MLP/RF on signal combinations) all fail to close the oracle gap; whether content-aware verifiers with access to task-specific structure could succeed remains open.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{lin2022teaching, tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app
…[truncated 1951 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2451 · 2026-05-19T06:08:30.457713+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 2452 · 2026-05-19T06:08:30.909430+00:00_

1	% Responsible NLP Research Checklist
2	% Following the ACL Rolling Review guidelines:
3	% https://aclrollingreview.org/responsibleNLPresearch/
4	
5	\subsection*{A\hspace{0.5em} For Every Submission}
6	
7	\begin{enumerate}
8	\item[A1.] \textbf{Did you discuss the limitations of your work?}\\
9	Yes. See the Limitations section after the Conclusion.
10	
11	\item[A2.] \textbf{Did you discuss any potential risks of your work?}\\
12	Yes. See the Ethics Statement. This work analyzes existing confidence signals for NER and identifies when they fail; the findings reduce risk of deploying unreliable confidence-based selection in production systems. No dual-use concerns.
13	
14	\item[A3.] \textbf{Do the abstract and introduction summarize the paper's main claims?}\\
15	Yes. The Abstract and Section~\ref{sec:introduction} (3 enumerated contributions) summarize all main claims with supporting evidence pointers.
16	\end{enumerate}
17	
18	\subsection*{B\hspace{0.5em} Did you use or create scientific artifacts?}
19	
20	Yes. We use existing datasets and pre-trained models.
21	
22	\begin{enumerate}
23	\item[B1.] \textbf{Did you cite the creators of artifacts you used?}\\
24	Yes. All datasets are cited: SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, Few-NERD \cite{ding2021fewnerd}, WNUT-17 \cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \cite{zheng2024llamafactory}. Constrained decoding: XGrammar \cite{dong2024xgrammar}. See Sections~\ref{sec:introduction}, \ref{sec:evaluation}, and Appendix~\ref{app:training}.
25	
26	\item[B2.] \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\\
27	Partially. The Ethics Statement notes that CoNLL-2003 is derived from the Reuters RCV1 corpus, available under a NIST agreement for research. SciERC, Few-NERD, and WNUT-17 are publicly available research benchmarks. Qwen3 and LLaMA-3.1 are open-weight models released under their r
…[truncated 4168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2453 · 2026-05-19T06:08:30.960021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2454 · 2026-05-19T06:08:31.411806+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $
…[truncated 13589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2455 · 2026-05-19T06:08:31.562614+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2456 · 2026-05-19T06:08:31.663494+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{vijayakumar2018diverse,
4	  title = {Diverse Beam Search for Improved Description of Complex Scenes},
5	  author = {Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and Sun, Qing and Lee, Stefan and Crandall, David J. and Batra, Dhruv},
6	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
7	  year = {2018},
8	  url = {https://arxiv.org/abs/1610.02424}
9	}
10	
11	@inproceedings{shi2022mbr,
12	  title = {Natural Language to Code Translation with Execution},
13	  author = {Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and Wang, Sida I.},
14	  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
15	  pages = {3533--3546},
16	  year = {2022},
17	  url = {https://arxiv.org/abs/2204.11454}
18	}
19	
20	@article{eisenstein2023helping,
21	  title = {Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking},
22	  author = {Eisenstein, Jacob and Nagpal, Chirag and Agarwal, Alekh and Beirami, Ahmad and D'Amour, Alex and Dvijotham, DJ and Fisch, Adam and Heller, Katherine and Pfohl, Stephen and Ramachandran, Deepak and Shaw, Peter and Berant, Jonathan},
23	  journal = {arXiv preprint arXiv:2312.09244},
24	  year = {2023},
25	  url = {https://arxiv.org/abs/2312.09244}
26	}
27	
28	@article{brown2024monkeys,
29	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
30	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
31	  journal = {arXiv preprint arXiv:2407.21787},
32	  year = {2024},
33	  url = {https://arxiv.org/abs/2407.21787}
34	}
35	
36	@inproceedings{chen2024usc,
37	  title = {Universal Self-Consistency for Large Language Model Generation},
38	  author = {Chen, Xinyun and Aksitov, Renat and Alon, 
…[truncated 3112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2457 · 2026-05-19T06:08:36.943248+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "200",
  "limit": "400"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "200",
    "limit": "400"
  }
}
```

</details>

---


### Tool result

_source line 2458 · 2026-05-19T06:08:37.314931+00:00_

200	EM ranks first across all four tested conditional configurations: SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$). This holds despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
201	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
202	On the conditional set, where the model demonstrably produces varied outputs, exact agreement becomes the strongest quality signal.
203	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
204	
205	\paragraph{WNUT-17 full signal analysis.}
206	Table~\ref{tab:wnut} reports all five signals on WNUT-17 with full-set and conditional $\rho$.
207	
208	\begin{table}[t]
209	\centering
210	\small
211	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\rho$ reflects binary success prediction; conditional $\rho$ measures quality gradation. LP's conditional $\rho$ is highest despite negative full-set $\rho$.}
212	\label{tab:wnut}
213	\begin{tabular}{lcccc}
214	\toprule
215	Signal & $\rho$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
216	\midrule
217	VC      & .724 & .913 & .038 & .487 \\
218	FK      & .125 & .555 & .169 & .002 \\
219	SJ      & .089 & .517 & .288 & ${<}$1e-7 \\
220	EM      & .050 & .487 & .333 & ${<}$1e-9 \\
221	LP & $-$.410 & .219 & .350 & ${<}$1e-10 \\
222	\bottomrule
223	\end{tabular}
224	\end{table}
225	The full-set $p$-values are: VC ${<}$1e-112, FK $p{=}0.001$, SJ $p{=}0.020$, EM $p{=}0.194$, LP ${<}$1e-28.
226	VC's high full-set $\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditio
…[truncated 30746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 371
}
```

</details>

---


### Tool call

_source line 2459 · 2026-05-19T06:08:41.982691+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "600",
  "limit": "400"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "600",
    "limit": "400"
  }
}
```

</details>

---


### Tool result

_source line 2460 · 2026-05-19T06:08:41.983361+00:00_

600	0.05 & 60.3\% \\
601	0.1  & ${\sim}$84\% \\
602	0.5  & ${\sim}$99\% \\
603	\bottomrule
604	\end{tabular}
605	\end{table}
606	
607	\paragraph{Non-tied subset.}
608	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms single-sample ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
609	As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability. LP carries information, but compression limits its exploitation.
610	A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
611	
612	\paragraph{$\varepsilon$ sensitivity sweep (post-hoc exploratory).}
613	Table~\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\varepsilon{=}0.01$ to $0.20$ as a post-hoc exploratory analysis characterizing how selection gain varies with compression severity.
614	The tied fraction increases smoothly with no cliff or discontinuity, and the selection gain $\Delta$ grows monotonically as the non-tied subset narrows to progressively higher-spread instances.
615	$\varepsilon{=}0.05$ yields the strongest statistical separation ($p{=}0.004$); at $\varepsilon{\geq}0.15$, the non-tied subset becomes too small for reliable inference ($n{\leq}36$).
616	
617	\begin{table}[t]
618	\centering
619	\small
620	\caption{$\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\%'' = fraction with within-instance LP range ${<}\varepsilon$. $\Delta$: selection F1 gain over single-sample on 
…[truncated 23241 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2461 · 2026-05-19T06:08:48.406421+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1000",
  "limit": "600"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1000",
    "limit": "600"
  }
}
```

</details>

---


### Tool call

_source line 2462 · 2026-05-19T06:08:48.658258+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2463 · 2026-05-19T06:08:48.909694+00:00_

1000	\toprule
1001	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
1002	\midrule
1003	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
1004	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
1005	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
1006	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
1007	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
1008	\bottomrule
1009	\end{tabular}
1010	\end{table}
1011	
1012	\begin{table}[t]
1013	\centering
1014	\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
1015	\label{tab:sigma-comparison}
1016	\small
1017	\begin{tabular}{l cc cc}
1018	\toprule
1019	 & \multicolumn{2}{c}{\textbf{NER} $\sigma_\rho$} & \multicolumn{2}{c}{\textbf{RE} $\sigma_\rho$} \\
1020	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
1021	Signal & $N\!=\!8$ & $N\!=\!16$ & $N\!=\!8$ & $N\!=\!16$ \\
1022	\midrule
1023	SJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\
1024	FK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\
1025	VC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\
1026	EM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\
1027	LP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\
1028	\midrule
1029	Mean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\
1030	\bottomrule
1031	\end{tabular}
1032	\end{table}
1033	
1034	Signal rankings are consistent across our 3 seeds (Kendall's $W{=}1.000$ for NER at $N{=}8$, both models), dropping to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}); however, with only $n{=}3$ seeds statistical power is insufficient to confirm stability, and additional seeds may reveal ranking changes.
1035	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER); additional samples stabilize structural signals more than LP.
1036	
1037	\paragraph{$N$-scalin
…[truncated 41100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool result

_source line 2464 · 2026-05-19T06:08:48.910070+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2465 · 2026-05-19T06:08:57.358221+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2466 · 2026-05-19T06:08:57.860603+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 160\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 1441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2467 · 2026-05-19T06:08:58.763798+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 2468 · 2026-05-19T06:08:59.117308+00:00_

&lt;persisted-output>
Output too large (59.8KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/9f2c1894-7971-40f3-8763-3fcf305a1aad/tool-results/toolu_01WdzrY6mwtjtqj54hzy42ks.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_14.md:185:外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md:163:外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_12.md:176:未配置外部审稿 (paperreview.ai disabled)。
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_10.md:166:项目未配置 paperreview.ai 外部审稿（external_review.paperreview_ai.enabled 未启用）。外部审稿：未请求。
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_2.md:156:外部审稿：未配置（项目未启用 `external_review.paperreview_ai.enabled`）。
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_21.md:165:外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7.md:138:External review not configured (paperreview_ai.enabled not set). Status: not_requested.
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:151:`director_get_proj
…[truncated 332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 2469 · 2026-05-19T06:09:04.687989+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/ 2>/dev/null | tail -5",
  "description": "List recent review report files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/ 2>/dev/null | tail -5",
    "description": "List recent review report files"
  }
}
```

</details>

---


### Tool result

_source line 2470 · 2026-05-19T06:09:05.140014+00:00_

-rw-r--r--   1 ubuntu ubuntu 14121 May 15 08:08 round_5.md
-rw-r--r--   1 ubuntu ubuntu 14108 May 15 09:05 round_6.md
-rw-r--r--   1 ubuntu ubuntu 11867 May 15 12:37 round_7.md
-rw-r--r--   1 ubuntu ubuntu 10201 May 15 12:54 round_7_consistency.md
-rw-r--r--   1 ubuntu ubuntu 10579 May 15 15:19 round_9.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2471 · 2026-05-19T06:09:05.140474+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null | head -80",
  "description": "Read current review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null | head -80",
    "description": "Read current review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2472 · 2026-05-19T06:09:05.191023+00:00_

issues:
  # ===== 历史 resolved issues（保留记录）=====
  - id: "R1-W1"
    summary: "Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。"
    resolution_round: 19

  - id: "R1-W2"
    summary: "\"Two jointly necessary conditions\" 因果性表述过强"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 21
    resolution: "全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。"
    resolution_round: 21

  - id: "R2-N1"
    summary: "Contribution 1 'methodological premise' 是定义推论"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。"
    resolution_round: 19

  - id: "R2-N2"
    summary: "与 MBR 文献差异化定位不够锐利"
    category: framing
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。"
    resolution_round: 19

  - id: "R2-N4"
    summary: "模型规模 3B-8B，70B+ 未知"
    category: experiment
    severity: info
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。"
    resolution_round: 19

  - id: "R1-W3"
    summary: "2-seed 统计效力不足"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。"
    resolution_round: 19

  - id: "R1-W4"
    summary: "Per-entity-type non-independence"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: 
…[truncated 302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2473 · 2026-05-19T06:09:08.224781+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "description": "Count lines in review issues file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "description": "Count lines in review issues file"
  }
}
```

</details>

---


### Tool result

_source line 2474 · 2026-05-19T06:09:08.275394+00:00_

717 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2475 · 2026-05-19T06:09:56.299487+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## 论文信息\n- 标题: \"Strong Predictors, Weak Selectors: Diagnosing and Resolving Self-Consistency for Named Entity Recognition\"\n- 路径: `projects/struct_self_consist_ie/docs/paper/main.tex`（modular: `sections/` 下各文件）\n- 目标 venue: **EMNLP 2026 Main Conference** (via ACL Rolling Review)\n- 截止: 2026-05-25 (AoE)\n- 格式: ACL style, long paper 8页正文, double-blind, mandatory Limitations + Checklist\n- 附录: ~1571 行，包含大量补充实验\n\n## 你的审查侧重\n\n### 1. 方法定义与信号合理性\n- 5 个 confidence signal 的数学定义是否严谨？\n- instance-level vs per-sample 的区分是否准确？4/5 信号确实无法做 sample selection 是定义推论还是实证发现？\n- Soft Jaccard 的匹配/归一化是否存在 edge case？\n- Entity construction 的 threshold θ=2/N 是否真的 tuning-free？\n\n### 2. 实验设计与统计\n- 多 seed 实验设计是否充分（3 seeds 够吗？seed sensitivity 如何？）\n- Bootstrap、TOST、sign test 等统计方法是否正确使用？\n- p 值报告是否考虑多重比较？\n- \"correlation-selection gap\" 的因果推断链是否成立？degeneracy 和 LP compression 是独立因素还是 confounded？\n- Epoch confound (Few-NERD 3 vs SciERC 5) 的控制实验是否充分？\n- Oracle headroom 定义是否存在 cherry-picking 风险？\n\n### 3. 实验覆盖与可复现性\n- 4B-8B scale 的结论对 70B+ 的外推是否合理？\n- 4 个 NER 数据集 + 1 个 RE 数据集是否足够？\n- constrained decoding 对 LP compression 的贡献是否充分量化？\n- 训练配置、评估 protocol 是否清晰到足以复现？\n\n### 4. 页数与格式\n- 主体是否在 8 页以内？\n- Figure/Table 是否紧凑高效？\n- 附录中的内容是否在正文中有恰当引用？\n\n请按以下结构输出审稿报告：\n1. Summary (2-3句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/warning/info)\n4. Questions for Authors\n5. Missing References (如有)\n6. Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 置信度)\n7. Detailed Comments (逐 section)",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## 论文信息\n- 标题: \"Strong Predictors, Weak Selectors: Diagnosing and Resolving Self-Consistency for Named Entity Recognition\"\n- 路径: `projects/struct_self_consist_ie/docs/paper/main.tex`（modular: `sections/` 下各文件）\n- 目标 venue: **EMNLP 2026 Main Conference** (via ACL Rolling Review)\n- 截止: 2026-05-25 (AoE)\n- 格式: ACL style, long paper 8页正文, double-blind, mandatory Limitations + Checklist\n- 附录: ~1571 行，包含大量补充实验\n\n## 你的审查侧重\n\n### 1. 方法定义与信号合理性\n- 5 个 confidence signal 的数学定义是否严谨？\n- instance-level vs per-sample 的区分是否准确？4/5 信号确实无法做 sample selection 是定义推论还是实证发现？\n- Soft Jaccard 的匹配/归一化是否存在 edge case？\n- Entity construction 的 threshold θ=2/N 是否真的 tuning-free？\n\n### 2. 实验设计与统计\n- 多 seed 实验设计是否充分（3 seeds 够吗？seed sensitivity 如何？）\n- Bootstrap、TOST、sign test 等统计方法是否正确使用？\n- p 值报告是否考虑多重比较？\n- \"correlation-selection gap\" 的因果推断链是否成立？degeneracy 和 LP compression 是独立因素还是 confounded？\n- Epoch confound (Few-NERD 3 vs SciERC 5) 的控制实验是否充分？\n- Oracle headroom 定义是否存在 cherry-picking 风险？\n\n### 3. 实验覆盖与可复现性\n- 4B-8B scale 的结论对 70B+ 的外推是否合理？\n- 4 个 NER 数据集 + 1 个 RE 数据集是否足够？\n- constrained decoding 对 LP compression 的贡献是否充分量化？\n- 训练配置、评估 protocol 是否清晰到足以复现？\n\n### 4. 页数与格式\n- 主体是否在 8 页以内？\n- Figure/Table 是否紧凑高效？\n- 附录中的内容是否在正文中有恰当引用？\n\n请按以下结构输出审稿报告：\n1. Summary (2-3句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/warning/info)\n4. Questions for Authors\n5. Missing References (如有)\n6. Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 置信度)\n7. Detailed Comments (逐 section)",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2476 · 2026-05-19T06:10:09.622720+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13323
}
```

</details>

---


### Tool call

_source line 2477 · 2026-05-19T06:10:09.975332+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 叙事完整性 + 写作质量 + Related Work positioning**。\n\n## 论文信息\n- 标题: \"Strong Predictors, Weak Selectors: Diagnosing and Resolving Self-Consistency for Named Entity Recognition\"\n- 路径: `projects/struct_self_consist_ie/docs/paper/main.tex`（modular: `sections/` 下各文件）\n- 目标 venue: **EMNLP 2026 Main Conference** (via ACL Rolling Review)\n- 截止: 2026-05-25 (AoE)\n- 格式: ACL style, long paper 8页正文, double-blind, mandatory Limitations + Checklist\n- 附录: ~1571 行，包含大量补充实验\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献度\n- \"correlation-selection gap\" 概念的新颖性如何？instance-level 信号无法做 selection 是否本就显而易见？\n- Entity-level construction 本质上是对 ensemble NER 的 entity voting 的直接迁移，新颖性如何评估？\n- 相比 Yao et al. (2026), Taubenfeld et al. (2025), Kang et al. (2025) 等直接竞争对手，增量是否显著？\n- 负结果（selection 失败）是否足以支撑一篇 EMNLP Main 论文？\n\n### 2. 叙事结构与故事线\n- Abstract → Introduction → Method → Experiments → Discussion → Conclusion 的主线是否统一？\n- 是否存在\"实验报告风格\"而非\"故事驱动\"？\n- Introduction 的 5 段结构是否完整？问题重要性论证是否充分？\n- Contribution 列表与正文内容是否对应？\n\n### 3. 写作质量（按 CLAUDE.md paper-writing-norms 严格检查）\n- 有无 AI 写作痕迹？（em-dash/en-dash, -ing phrases, 过度分段, 用词黑名单）\n- 专有名词是否全部有定义？Abstract 中缩写是否展开？\n- 过渡词使用是否自然？段落长度是否合理？\n- 图表 caption 是否自包含？知识密度是否足够？\n\n### 4. Related Work Positioning\n- 文献调研是否充分？有无遗漏的重要相关工作？\n- 与 MBR decoding、structured prediction 文献的定位是否清晰？\n- 引用密度是否匹配 EMNLP 近年录用论文？\n\n### 5. 格式与投稿规范\n- ACL style 是否正确使用？\n- Limitations section 是否充分？\n- Responsible NLP Checklist 是否认真填写？\n\n请按以下结构输出审稿报告：\n1. Summary (2-3句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/warning/info)\n4. Questions for Authors\n5. Missing References (如有)\n6. Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 置信度)\n7. Detailed Comments (逐 section)",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 叙事完整性 + 写作质量 + Related Work positioning**。\n\n## 论文信息\n- 标题: \"Strong Predictors, Weak Selectors: Diagnosing and Resolving Self-Consistency for Named Entity Recognition\"\n- 路径: `projects/struct_self_consist_ie/docs/paper/main.tex`（modular: `sections/` 下各文件）\n- 目标 venue: **EMNLP 2026 Main Conference** (via ACL Rolling Review)\n- 截止: 2026-05-25 (AoE)\n- 格式: ACL style, long paper 8页正文, double-blind, mandatory Limitations + Checklist\n- 附录: ~1571 行，包含大量补充实验\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献度\n- \"correlation-selection gap\" 概念的新颖性如何？instance-level 信号无法做 selection 是否本就显而易见？\n- Entity-level construction 本质上是对 ensemble NER 的 entity voting 的直接迁移，新颖性如何评估？\n- 相比 Yao et al. (2026), Taubenfeld et al. (2025), Kang et al. (2025) 等直接竞争对手，增量是否显著？\n- 负结果（selection 失败）是否足以支撑一篇 EMNLP Main 论文？\n\n### 2. 叙事结构与故事线\n- Abstract → Introduction → Method → Experiments → Discussion → Conclusion 的主线是否统一？\n- 是否存在\"实验报告风格\"而非\"故事驱动\"？\n- Introduction 的 5 段结构是否完整？问题重要性论证是否充分？\n- Contribution 列表与正文内容是否对应？\n\n### 3. 写作质量（按 CLAUDE.md paper-writing-norms 严格检查）\n- 有无 AI 写作痕迹？（em-dash/en-dash, -ing phrases, 过度分段, 用词黑名单）\n- 专有名词是否全部有定义？Abstract 中缩写是否展开？\n- 过渡词使用是否自然？段落长度是否合理？\n- 图表 caption 是否自包含？知识密度是否足够？\n\n### 4. Related Work Positioning\n- 文献调研是否充分？有无遗漏的重要相关工作？\n- 与 MBR decoding、structured prediction 文献的定位是否清晰？\n- 引用密度是否匹配 EMNLP 近年录用论文？\n\n### 5. 格式与投稿规范\n- ACL style 是否正确使用？\n- Limitations section 是否充分？\n- Responsible NLP Checklist 是否认真填写？\n\n请按以下结构输出审稿报告：\n1. Summary (2-3句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/warning/info)\n4. Questions for Authors\n5. Missing References (如有)\n6. Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 置信度)\n7. Detailed Comments (逐 section)",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2478 · 2026-05-19T06:10:11.843810+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1868
}
```

</details>

---


### Assistant

_source line 2479 · 2026-05-19T06:10:21.179899+00:00_

Round 1 审稿任务已分配：

- **Reviewer 1** (方法严谨性 + 实验设计) — 已派出
- **Reviewer 2** (新颖性 + 叙事完整性 + 写作质量) — 已派出

等待两位 Reviewer 返回独立审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 186

## Round 186

2 recorded events


### User

_source line 2480 · 2026-05-19T06:16:54.251752+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告 — Round 1

**论文**: "Strong Predictors, Weak Selectors: Diagnosing and Resolving Self-Consistency for Named Entity Recognition"
**Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review)
**审查侧重**: 新颖性 + 叙事完整性 + 写作质量 + Related Work positioning

---

## 总体评分

**Overall**: 3.0 / 5 (Borderline)
**一句话总结**: 实验扎实、诊断细致的 empirical study，但核心新颖性有限，positive contribution（entity construction）增量小且源自已知技术的直接迁移，负结果虽有价值但主线在 diagnostic 与 prescriptive 之间摇摆。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨、统计方法充分（bootstrap CI, MDE, TOST, 多种校正），但几个核心发现依赖 post-hoc 分析（ε=0.05），confound（thinking token）虽被 address 但增加了不确定性 |
| Excitement | 2.5/5 | 诊断有价值但结论部分可预测（instance-level 信号无法 within-instance 选择几乎是 by construction）；positive contribution 增量小（~1pp），对领域推进有限 |
| Reproducibility | 4.0/5 | 超参、prompt、训练配置详尽（Appendix Table 7），承诺代码开源，所有 benchmark 公开可用，多 seed 报告 |
| Confidence | 4/5 | 本人熟悉 NER/IE、test-time scaling 和 MBR decoding 文献 |

---

## Strengths

**S1. 统计严谨性超越同类工作。** 全文贯穿 paired bootstrap tests, MDE 分析, TOST 等价性检验, Bonferroni/BH 校正, 以及 multi-seed stability 报告。对 SciERC 的 MDE≈1.5pp 限制有明确声明（Section 4.3, footnote 6），这在 NLP 经验研究中很少见。

**S2. 诊断框架清晰。** QE 与 selection 的显式分离（Section 3.1 的 per-sample vs. instance-level 信号分类）是有效的概念贡献。Expected selection gain decomposition 虽非严格推导，但在三个 dataset 上方向一致，具有启发性。

**S3. 实验覆盖面广。** 4 个 NER benchmark 形成难度梯度（WNUT-17 signal collapse → SciERC medium → Few-NERD low degeneracy → CoNLL ceiling），各自承担明确的实验角色。附录约 1571 行，几乎每个可能的混淆因素都有 ablation。

**S4. 诚实的负结果呈现。** 坦率承认 supervised combinations、hidden state probes、DeBERTa verifier 均无法关闭 selection gap，并清楚区分 exploratory 与 confirmatory findings。

**S5. 写作质量整体良好。** 无 em-dash/en-dash AI 写作痕迹，无黑名单词汇。术语定义完整。段落长度合理，过渡自然。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **"Correlation-selection gap" 的新颖性存疑：instance-level 信号无法做 within-instance selection 是结构性事实，非实证发现。**
- 具体位置：Section 3.1, Section 4.3
- 4/5 个信号是 instance-level aggregate（"assign identical scores to all N candidates"），这是信号定义的直接结果——不需要实验验证。实际需要验证的只是 LP 的 selection 失败。LP 在 Few-NERD 成功、SciERC 失败的归因——"LP-quality alignment" 接近同义反复（LP 选得好当且仅当 LP 与 quality 对齐好）。
- 建议：更清晰区分 by-construction 与 empirical findings。核心贡献聚焦 LP compression 量化（median 0.041 nats）、degeneracy-convergence 因果关系、跨 dataset alignment 差异。

**N2** [critical] **Entity-level construction 本质是 Florian et al. (2003) entity voting 的直接应用，新颖性增量有限。**
- 具体位置：Section 4.6, Introduction Contribution #3
- 论文自承 "adapting entity voting from ensemble NER to stochastic sampling"。LP-weighted vs. uniform 差异仅 +0.3-0.7pp。对于 EMNLP Main，将已有技术的 threshold 从 majority 调整到 θ=2/N 加 LP weighting 不构成 significant contribution。
- 建议：需 stochastic sampling + entity voting 与 multi-model ensemble + entity voting 的 direct comparison，或更深入的理论分析。

**N3** [critical] **负结果的 scope 限制过强，削弱诊断贡献的 generalizability。**
- 具体位置：Discussion Section 5, Limitations
- 核心负结果仅在 fine-tuned 4B-8B + constrained decoding 下成立。Appendix free-form ablation 展示 RE LP selection 反转（-0.68pp → +1.69pp）。70B+/closed-source APIs 未测试。
- 建议：至少需一个非 fine-tuned 设置的验证，或在 title/abstract 中更清楚限定 scope。

---

## Should-Fix 问题

**W1** [warning] SciERC n=529 作为 primary test bed 统计功效不足（MDE≈1.5pp），建议以 Few-NERD 为 primary。

**W2** [warning] Expected selection gain decomposition 缺乏理论基础，仅有 3 个 data points 验证方向一致性。

**W3** [warning] Gating protocol 仅在 3 个 easily separable dataset 上验证，不具备 practical robustness 证据。

**W4** [warning] Related Work 偏短（~1 column），缺少与 Taubenfeld/Kang 的技术差异对比，Li et al. 2025 在 bib 中但未 cite。

**W5** [warning] Greedy F1 在不同 table 中出现 4 个值（0.640-0.650），虽有解释但反映 protocol 不统一。

---

## 小问题

- M1: Abstract "LP" 首次出现未展开
- M2: \textendash 在 abstract/limitations 中使用，确认 ACL style 兼容性
- M3: 8 个 orphan bib entries 应清理
- M4: Table 2 中 EM/VC 的 p 值标 "---" 但应标注具体值（它们低于 greedy）
- M5: Checklist E1 AI assistant 声明过于笼统

---

## Questions for Authors

Q1. Table 4 的 cross-instance LP ρ (0.220) 与 Appendix Table 12 的 within-instance ρ (0.667) 差异巨大，请澄清为何 cross-instance ρ 不能预测 selection 而 within-instance ρ 可以。

Q2. Entity construction 在 CoNLL 上降低 F1 (-0.39pp)。如果 gating 将 CoNLL 路由到 construction（dev ρ=0.065 < 0.3），是否 cause harm？

Q3. Free-form decoding 使 RE LP selection 反转但 NER 不变，这是否说明 constrained decoding 是 failure 的根本原因？

Q4. 是否测试过 Self-Certainty (Kang et al. 2025) 或 P(True)？这些 per-sample signals 的缺失是否削弱 "no per-sample signal works" 的结论？

---

## Missing References

- Li et al. (2025) "LLMs Can Generate a Better Answer by Aggregating Their Own Responses"——在 bib 中但未 cite
- Lafferty et al. (2001) CRF——structured prediction confidence 的经典基础
- Muennighoff et al. (2025) s1——在 bib 中但未 cite

---

## Overall Assessment

**3.0 / 5 — Borderline**，置信度 4/5

论文的 strength 在于实验严谨性和诚实的负结果呈现。但三个 critical 问题共同削弱了 EMNLP Main 的 case：(1) 核心概念新颖性不足（"correlation-selection gap" 部分 by construction）；(2) positive contribution 增量过小（entity voting 的直接迁移，~1pp gains）；(3) scope 限制严重（结论可能是 fine-tuned + constrained decoding setup 的 artifact）。

如果 sharpen novelty framing（聚焦 LP compression + alignment 作为独立发现），增加非 fine-tuned 验证，并对 entity construction 与 ensemble voting 做 direct comparison，可升至 weak accept。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2481 · 2026-05-19T06:17:00.417499+00:00_

Reviewer 2 的审稿意见已收到。等待 Reviewer 1 的报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 187

## Round 187

2 recorded events


### User

_source line 2482 · 2026-05-19T06:17:04.873945+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**核心结论**：Overall 3.0/5 (Borderline)。三个 critical 问题：

1. **"Correlation-selection gap" 新颖性有限**——4/5 信号的 selection 失败是信号定义的直接结果（它们 by construction 对同一 input 的所有 sample 给相同分数），不是 empirical discovery。真正的 empirical contribution（LP compression、degeneracy-convergence 因果关系）被 umbrella term 模糊了。

2. **Entity construction 增量过小**——+1.0-1.4pp 来自 Florian et al. (2003) entity voting 的直接迁移加 LP weighting，对 EMNLP Main 方法贡献不够。

3. **Scope 太窄**——负结果仅限于 fine-tuned 4B-8B + constrained decoding，论文自身的 free-form ablation 已展示 RE 方向反转，暗示结论可能是 setup-specific。

写作质量方面无 AI 写作痕迹，统计处理在 NLP 论文中属于上乘水平，这是论文的主要优势。引用核查通过（78 entries, 69 verified, 8 orphan 应清理）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2483 · 2026-05-19T06:17:11.107564+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 完成独立初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 188

## Round 188

6 recorded events


### User

_source line 2484 · 2026-05-19T06:18:01.128765+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：方法严谨性 + 实验设计

**论文**: "Strong Predictors, Weak Selectors: Diagnosing and Resolving Self-Consistency for Named Entity Recognition"
**目标 venue**: EMNLP 2026 Main Conference (via ACL Rolling Review)
**审查侧重**: 方法定义与信号合理性、实验设计与统计、实验覆盖与可复现性、页数与格式

---

## 总体评分

**Overall**: 3.5/5 (介于 Findings acceptance 和 Conference acceptance 之间)
**一句话总结**: 扎实的诊断性实证研究，实验覆盖和统计处理在 NLP 论文中属上乘，但核心分析框架（分解公式和因果推断链）存在方法论弱点，且解决方案（entity construction）的实际增益较小，narrative 上的 "resolution" 略显过度。

---

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 信号定义严谨，统计方法正确且透明，但核心分解公式属启发式（3 个数据点拟合），因果推断链有循环性问题 |
| Excitement | 3/5 | Correlation-selection gap 概念有洞察力，但结论偏 negative（主要说明哪些方法不 work），entity construction 增益小 |
| Reproducibility | 4/5 | 训练配置完整（Table 9），prompt 模板给出，多 seed 报告，代码承诺释放；但 SciERC thinking token confound 增加不确定性 |
| Confidence | 4/5 | 该领域与本 reviewer 研究方向接近，仔细阅读了全文及附录 |

---

## 1. Summary

本文系统评估了 5 种置信度信号在 NER 任务上的 quality estimation (QE) 和 sample selection 效果，在 4 个 NER 数据集 + 2 个模型上进行了大量实验。核心发现：(1) 所有信号都能可靠估计实例质量（ρ up to 0.45），支持 selective prediction；(2) 4/5 信号因 instance-level 本质无法做 sample selection，唯一的 per-sample 信号 LP 也仅在特定条件下有效（correlation-selection gap）；(3) 诊断出 degeneracy 和 LP compression 两个瓶颈因素；(4) 提出 entity-level construction 作为解决方案。

---

## 2. Strengths

**S1. 问题形式化清晰且重要。** QE vs. selection 的区分（Section 3.1）是一个被忽视但关键的概念贡献。Instance-level vs. per-sample signal 的分类法（Section 3.2）有助于理解为何 4/5 信号必然无法做 selection——这是定义推论而非实证发现，论文正确地标注了这一点（"by construction"）。

**S2. 实验覆盖异常全面。** 在我审过的同类论文中，这是最彻底的之一：5 信号 × 4 NER 数据集 × 2 模型家族 × 4B scale ablation × 温度消融 × epoch 消融 × N-scaling (2-32) × LoRA rank 消融 × supervised 组合 × hidden state probes × DeBERTa verifier × verbalized confidence × free-form decoding 消融 × calibration baseline × OOD 分析。附录约 1571 行，每个潜在混淆变量都有对应分析。

**S3. 统计方法正确且透明度高。** Bootstrap CI、paired sign test、TOST 等均适用于对应场景。论文主动识别并报告了多重比较问题（Appendix D: ε=0.05 post-hoc 选择 → p_adj=0.14 → 标记为 exploratory），MDE 分析（SciERC n=529 → MDE≈1.5 pp），以及 3 seed 的统计功效局限性。这种自我约束在 NLP 论文中罕见。

**S4. Negative results 的诚实报告。** 论文的核心贡献之一是系统的 negative results（selection 失败），且不试图掩饰或弱化这些发现，而是将其作为诊断框架的基础。这对领域有价值。

**S5. 混淆变量控制充分。** Thinking token confound (Appendix J: 3-part analysis)、epoch confound (Appendix S: Few-NERD 2-point + SciERC 3-point)、SJ normalizer robustness (Table 6: |Δρ|<0.01)、FK independence (Appendix B: permutation test)、length-LP correlation (正向非负向，排除 length penalty confound) 均有对应分析。

---

## 3. Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [critical] 核心分解公式是 underdetermined 启发式**
- 具体位置：Section 4.3, Eq. after line 100-103
- 问题：Expected selection gain 分解 E[ΔF1] ≈ (1-d) · Δ_oracle · g(ρ_within) 中，g 被"assumed monotonically increasing"但无理论推导。该公式用 3 个数据点（SciERC, Few-NERD, CoNLL）验证"consistency"——但任何单调函数都能拟合 3 个点。论文声称"consistent with the observed data"，但这不构成验证。
- 为什么影响接收：这是论文核心诊断框架的数学基础。如果分解公式缺乏理论支撑或充分的实证验证，"degeneracy + alignment 两因素" narrative 的因果推断力就被削弱。
- 建议修改方向：(a) 明确标注此公式为"descriptive heuristic"而非"decomposition"；(b) 删除"consistent with"的验证措辞，改为"illustrates the interplay"；(c) 如果有 23 个 configurations 的数据（Fig 3），在这些配置上验证分解公式的预测精度，而非仅用 3 个 macro-level 数据点。

**N2 [critical] Within-instance ρ(LP, F1) 作为因果预测因子具有循环性**
- 具体位置：Section 4.3, Section 5.4, Table in Appendix E (Table 14)
- 问题：论文的核心因果声明是"LP-quality alignment (within-instance ρ) 是 LP selection 成功的 primary predictor"。但 within-instance ρ(LP, F1) 需要 gold labels 才能计算，因此它只是回顾性诊断，不是前瞻性预测器。Section 5.4 的 gating protocol 试图用 50 个 validation instances 估计 adjusted ρ，但：(a) 50 instances 的 bootstrap SE 未报告；(b) 仅在 3 个数据集（"large inter-dataset margins"）上验证 → 不清楚 margins 窄的情况下 routing 是否仍可靠；(c) 0.3 threshold 的选择未说明来源。
- 为什么影响接收：如果核心诊断因子在实践中不可用（需要 gold labels），且仅有的前瞻近似方法（gating protocol）未经充分验证，那么 "from diagnosis to practice" 的链条就不完整。
- 建议修改方向：(a) 报告 50-instance adjusted ρ 的 bootstrap CI；(b) 讨论 threshold 0.3 的敏感性；(c) 明确 gating 方法的局限性（仅 3 数据点验证，不是 validated protocol）。

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] "Tuning-free" threshold 声明不准确**
- 具体位置：Section 5.4 ("This threshold is tuning-free across all datasets"), Appendix S (Table 28)
- 问题：θ=2/N 被描述为 "tuning-free"，但 Table 28 的 sweep 表明不同数据集的最优 θ 不同（SciERC: 0.30-0.35, Few-NERD: 0.25, CoNLL: 0.30）。θ=2/N=0.25 是在观察所有数据集结果后选择的 "works reasonably well" 值，不是从先验原则推导的。真正的 tuning-free 应该不依赖于任何测试集观察。
- 建议：改为 "default threshold" 或 "heuristic threshold that requires no per-dataset tuning"，并在文中注明该选择是基于对多个数据集的观察。

**W2 [warning] Entity construction 增益的 narrative framing 过强**
- 具体位置：Title ("Resolving"), Section 5.4, Contribution 3 ("principled resolution")
- 问题：+1.40 pp (Few-NERD) 和 +1.02 pp (SciERC) 是显著的但实际增益较小——SciERC 上仅恢复 oracle headroom 的约 8%（1.02/13.0），Few-NERD 约 11%（1.40/12.4）。Title 中的 "Resolving" 和 Contribution 列表中的 "principled resolution" 暗示问题已被有效解决，但实际上 90% 的 oracle gap 仍然存在。
- 建议：将 "Resolving" 改为 "Addressing" 或 "Mitigating"；将 "principled resolution" 改为 "partial mitigation"；在正文中加入 recovery percentage 使读者对实际增益有准确预期。

**W3 [warning] SciERC Thinking Token Confound**
- 具体位置：Appendix J, Section 4.1 footnote
- 问题：SciERC 的 Qwen3-8B checkpoint 训练时注入了 empty &lt;think>&lt;/think> blocks（4-5 tokens），而 CoNLL/WNUT 没有。虽然 3-part analysis 论证了影响很小（LP shift 0.001 nats = 2.68% of median range），但这本质上是一个训练-推理不一致的 confound。更根本的是，这个 confound 是无意引入的（LLaMA Factory 0.9.4 default），反映了实验管控的疏忽。
- 建议：在正文而非仅附录中明确声明这一 confound，并讨论是否需要重训一个 clean checkpoint 做验证。

**W4 [warning] 3 seeds 的统计功效有限**
- 具体位置：Appendix F (Table 17), Limitations section
- 问题：论文多次使用 3-seed statistics，并正确声明功效有限。但一些关键结论依赖于 seed-level consistency（如 "LP-weighted positive across all seeds" in Table 5, 7 seed-dataset combinations）。SciERC LP selection 的 σ=0.48 pp（3 seeds）几乎等于 effect size 本身（+0.04 pp mean），说明在 SciERC 上 LP selection 方向 是 seed-dependent 的。
- 建议：在正文中更明确地标注哪些结论在当前 seed count 下是 robust 的（Few-NERD: σ=0.04 pp, robust）vs. 不确定的（SciERC: σ=0.48 pp, inconclusive）。

**W5 [warning] English-only + NER-heavy 的泛化局限性**
- 具体位置：Limitations section
- 问题：4 个 NER 数据集 + 1 个 RE 数据集，全部英文。RE 仅 SciERC 一个数据集，标记为 exploratory。论文在 Limitations 中讨论了 scale 泛化但未提及语言泛化。
- 建议：在 Limitations 中加入语言覆盖限制的讨论。

### 小问题（不影响接收）

- **M1**: F1 metric 在论文中有多种用法（instance-level macro, span-level micro, per-sample），Table 2 caption 说 "macro F1" 但 Section 3.3 说 "per-instance macro-F1"。需统一术语。
- **M2**: Table 3 的 SciERC LP 报告了单 seed 结果 (+0.61 pp)，但 3-seed mean 是 +0.04±0.48 pp (Table 17)。单 seed 值在 footnote 中提及但表格本身有误导性。
- **M3**: 8 个 orphan bib entries（未被引用但在 .bib 文件中），建议清理。
- **M4**: Appendix D 的 "as a reviewer correctly noted" 措辞暗示之前的审稿历史，如果这是首次投稿应删除。
- **M5**: Figure 1 caption 引用了 Table 1 的数据 (ρ up to 0.45 on CoNLL)，但 Table 1 中 CoNLL 最高是 EM ρ=0.451。Figure 和 Table 的交叉引用无误，但 abstract 中的 "ρ up to 0.45" 取自 CoNLL EM，而 SciERC 上最高仅 0.379——应明确这个上限来自 CoNLL 而非所有数据集一致。

---

## 4. Questions for Authors

**Q1**: 分解公式 E[ΔF1] ≈ (1-d) · Δ_oracle · g(ρ_within) 能否在 23 个 configurations (Fig 3) 上做回归验证，而不是仅用 3 个 macro-level 数据点？如果将 23 个点代入分解，predicted gain 与 actual gain 的相关性是多少？

**Q2**: LP-alignment gating protocol 的 50 instances 是如何选择的？是随机采样还是 stratified？Bootstrap CI 是什么？如果将 threshold 从 0.3 移到 0.2 或 0.4，routing 决策是否改变？

**Q3**: 论文认为 "degeneracy rises with model capability"（8B > 4B）。但这也可能是因为 8B 在相同 epoch 数下训练更充分（更接近收敛）。是否有 matched-convergence 的 scale 对比（如 8B 3-epoch vs 4B 5-epoch）？

**Q4**: Entity construction 是 recall-driven（聚合低频但正确的 entity）。那么 precision 变化如何？是否存在 precision-recall trade-off 数据？

**Q5**: Constrained decoding 强制 JSON 格式输出，这显然限制了 per-sample diversity。如果使用 unconstrained decoding + post-hoc parsing，是否有更多 headroom 可供 selection？Free-form ablation (Appendix L) 对 NER 显示"comparable"结果，但 RE 有显著改善——如何解释这种 task asymmetry？

---

## 5. Missing References

论文引用覆盖较充分（78 bib entries, 70 cited），无明显遗漏。以下可考虑补充：
- Jiang et al. (2023), "LLM-Blender: Ensembling Large Language Models with Pairwise Ranking and Generative Fusion" — 相关于 BoN + ensembling 在生成任务上的工作
- Ravaut et al. (2022), "SummaReranker" — MBR + reranking 在 summarization 上的应用

---

## 6. Overall Assessment

**Rating**: 3.5/5 — Borderline accept，倾向 Findings acceptance

**置信度**: 4/5

**理由**: 这是一篇实验覆盖和统计严谨性上乘的诊断性实证研究。Correlation-selection gap 的概念和 instance-level vs. per-sample signal 的区分对领域有价值。但核心分析框架的两个弱点（启发式分解公式的验证不足、within-instance alignment 作为因果预测因子的循环性）影响了论文的分析深度。Entity construction 作为 "resolution" 的增益偏小（约 1 pp）且 narrative framing 过强。如果作者能修复 N1 和 N2（加强分解公式验证 + gating protocol 的 robustness 分析），本文可上升至 weak accept for main conference。

---

## 7. Detailed Comments (逐 Section)

### Abstract
- 信息密集且准确，但 "ρ up to 0.45" 取自 CoNLL EM（easiest dataset），容易给读者过于乐观的印象。建议加注 dataset context 或报告 median performance。
- "LP-weighted aggregation improves F1 by +1.40 pp on Few-NERD and +1.02 pp on SciERC (multi-seed mean, p<0.005)" — 准确但缺少 oracle recovery percentage，读者无法判断增益的实际意义。

### Introduction
- 叙事结构清晰：从 self-consistency 的 discrete-answer 成功 → NER 的 structural difference → QE vs. selection 区分 → gap 诊断 → construction 解决。
- Line 8: "Unlike Yao et al. (2026), who demonstrate that self-consistency correlates with task accuracy" — 这是一个有效的 positioning。
- Line 16: MBR comparison with Eikema et al. (2025) 是有价值的 framing。
- Contribution list 清晰但 Contribution 3 的 "principled resolution" framing 需降调（见 W2）。

### Method (Section 3)
- 5 个信号的数学定义严谨完整。
- Soft Jaccard (Eq 4): Hungarian matching + token IoU + max normalizer 是合理的设计选择，且 normalizer robustness 在 Table 6 (Appendix) 中验证。
- FK adaptation (Eq 3): 二元 present/absent rating matrix 是对 Fleiss' κ 的合理扩展。Independence check (Appendix B) 排除了 marginal-rate artifacts。
- **Edge case**: E_∪ = ∅ 时 VC = 0 (footnote)，但 SJ 的分母 max(|g_i|, |g_j|) 也可能为 0（两个样本都不含某类型 entity）。论文未明确讨论此边界情况。

### Experiments (Section 4)
- **数据集选择有策略性**：difficulty gradient (WNUT→SciERC→Few-NERD→CoNLL) 使得不同 regime 下的 signal 行为得以对比。每个数据集有明确的 experimental role。
- **QE 结果 (Table 1)** 可信：structural signals > LP 在 SciERC 上显著（Appendix C: bootstrap CI 不含 0），在 CoNLL 上差距收窄。
- **Selection 结果 (Table 2)**: SciERC 所有信号 vs greedy 无显著差异，这是可靠的 negative result。p 值报告正确。
- **Few-NERD contrast (Table 3)**: LP +1.39 pp (p<0.001) 是论文中最强的 positive result。Bootstrap CI [+1.18, +1.53] (Table 20) 不含 0，在 n=32,565 上是有力的证据。

### Discussion (Section 5)
- 内容密度极高但空间压缩严重（不到一页）。核心因果分析、practical prescription、和 entity construction 都被压缩在一起。
- Non-tied subset analysis (+2.9 pp, p=0.004 但 p_adj=0.14) 的 exploratory 标注是正确的。

### Conclusion (Section 6)
- 准确总结了主要发现，未超出实证支持范围。

### Limitations
- 异常全面：scale, seed count, supervised approaches, N-scaling, thinking token, temperature, verbalized confidence, entity LP decomposition, supervised combination 都被覆盖。这在 NLP 论文中是 best practice。
- 缺少语言覆盖的讨论（W5）。

### 页数与格式
- 正文 8 页以内（Discussion 和 Conclusion 在第 8 页中部，Limitations 从第 8 页底部开始，不计入限制）。符合 ACL long paper 要求。
- 使用 `\usepackage[review]{acl}` 且 `\author{Anonymous}`，double-blind 合规。
- Figure/Table 紧凑高效，无明显空间浪费。Figure 1 信息量充分。

### 引用审计
- 78 个 bib entries，70 个被引用，0 个 missing。
- 4 个 not_found (hobelsberger2025, lightman2024verify, venktesh2025trust, aggarwal2023adaptive) 可能是极新预印本，OpenAlex 尚未收录——非论文问题。
- 5 个 mismatch 为作者姓名格式差异（如 bib 用 last name 而 API 返回 first name），非实质错误。
- **建议清理 8 个 orphan bib entries**（在 .bib 中但未被引用）。

---

## 主要优势总结

1. 实验覆盖在 NLP 论文中属顶尖水平，几乎每个潜在混淆变量都有对应消融/控制分析
2. 统计方法正确使用且主动标注了探索性/确认性分析的边界
3. Correlation-selection gap 概念对 structured prediction 领域的 self-consistency 研究有指导意义
4. QE vs. selection 的概念区分和 instance-level vs. per-sample signal 的分类法是重要的方法论贡献
5. Negative results 的诚实报告为后续研究节省了大量探索空间


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2485 · 2026-05-19T06:18:43.011967+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告 — Round 1\n\n**Overall**: 3.0 / 5 (Borderline)\n\n### Strengths\nS1. 统计严谨性超越同类工作。\nS2. 诊断框架清晰（QE vs selection 分离）。\nS3. 实验覆盖面广（4 NER benchmark 形成难度梯度）。\nS4. 诚实的负结果呈现。\nS5. 写作质量整体良好，无 AI 写作痕迹。\n\n### Must-Fix (Critical)\nN1. \"Correlation-selection gap\" 新颖性存疑：4/5 信号的 selection 失败是信号定义的直接结果（by construction 对同一 input 给相同分数），非 empirical discovery。真正的 empirical contribution（LP compression、degeneracy-convergence）被 umbrella term 模糊了。LP-quality alignment 接近同义反复。\nN2. Entity-level construction 本质是 Florian et al. (2003) entity voting 的直接应用，新颖性增量有限。+1.0-1.4pp 来自已有技术迁移 + LP weighting。\nN3. 负结果的 scope 限制过强：仅在 fine-tuned 4B-8B + constrained decoding 下成立。Free-form ablation 已展示 RE LP selection 反转（-0.68pp → +1.69pp）。70B+/closed-source APIs 未测试。\n\n### Should-Fix (Warning)\nW1. SciERC n=529 统计功效不足（MDE≈1.5pp），应以 Few-NERD 为 primary。\nW2. Expected selection gain decomposition 缺乏理论基础，仅 3 data points。\nW3. Gating protocol 仅 3 个 easily separable dataset 验证。\nW4. Related Work 偏短（~1 column），缺少与 Taubenfeld/Kang 技术差异对比。\nW5. Greedy F1 在不同 table 出现 4 个值（0.640-0.650）。\n\n### Minor\nM1-M5: Abstract LP 未展开, \\textendash 兼容性, orphan bib entries, Table 2 p-values, Checklist E1 声明。\n\n### Questions\nQ1. Cross-instance LP ρ (0.220) vs within-instance ρ (0.667) 差异巨大，为何 cross-instance 不能预测 selection？\nQ2. Entity construction 在 CoNLL 降 F1 (-0.39pp)，gating 是否 cause harm？\nQ3. Free-form 使 RE LP 反转但 NER 不变，constrained decoding 是否是 failure 根本原因？\nQ4. 是否测试 Self-Certainty/P(True)？缺失是否削弱 \"no per-sample signal works\" 结论？\n\n### Missing References\n- Li et al. (2025) 在 bib 但未 cite\n- Lafferty et al. (2001) CRF\n- Muennighoff et al. (2025) s1 在 bib 但未 cite",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告 — Round 1\n\n**Overall**: 3.0 / 5 (Borderline)\n\n### Strengths\nS1. 统计严谨性超越同类工作。\nS2. 诊断框架清晰（QE vs selection 分离）。\nS3. 实验覆盖面广（4 NER benchmark 形成难度梯度）。\nS4. 诚实的负结果呈现。\nS5. 写作质量整体良好，无 AI 写作痕迹。\n\n### Must-Fix (Critical)\nN1. \"Correlation-selection gap\" 新颖性存疑：4/5 信号的 selection 失败是信号定义的直接结果（by construction 对同一 input 给相同分数），非 empirical discovery。真正的 empirical contribution（LP compression、degeneracy-convergence）被 umbrella term 模糊了。LP-quality alignment 接近同义反复。\nN2. Entity-level construction 本质是 Florian et al. (2003) entity voting 的直接应用，新颖性增量有限。+1.0-1.4pp 来自已有技术迁移 + LP weighting。\nN3. 负结果的 scope 限制过强：仅在 fine-tuned 4B-8B + constrained decoding 下成立。Free-form ablation 已展示 RE LP selection 反转（-0.68pp → +1.69pp）。70B+/closed-source APIs 未测试。\n\n### Should-Fix (Warning)\nW1. SciERC n=529 统计功效不足（MDE≈1.5pp），应以 Few-NERD 为 primary。\nW2. Expected selection gain decomposition 缺乏理论基础，仅 3 data points。\nW3. Gating protocol 仅 3 个 easily separable dataset 验证。\nW4. Related Work 偏短（~1 column），缺少与 Taubenfeld/Kang 技术差异对比。\nW5. Greedy F1 在不同 table 出现 4 个值（0.640-0.650）。\n\n### Minor\nM1-M5: Abstract LP 未展开, \\textendash 兼容性, orphan bib entries, Table 2 p-values, Checklist E1 声明。\n\n### Questions\nQ1. Cross-instance LP ρ (0.220) vs within-instance ρ (0.667) 差异巨大，为何 cross-instance 不能预测 selection？\nQ2. Entity construction 在 CoNLL 降 F1 (-0.39pp)，gating 是否 cause harm？\nQ3. Free-form 使 RE LP 反转但 NER 不变，constrained decoding 是否是 failure 根本原因？\nQ4. 是否测试 Self-Certainty/P(True)？缺失是否削弱 \"no per-sample signal works\" 结论？\n\n### Missing References\n- Li et al. (2025) 在 bib 但未 cite\n- Lafferty et al. (2001) CRF\n- Muennighoff et al. (2025) s1 在 bib 但未 cite",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2486 · 2026-05-19T06:19:01.909756+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18897
}
```

</details>

---


### Tool call

_source line 2487 · 2026-05-19T06:19:02.612677+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告 — Round 1\n\n**Overall**: 3.5/5 (Borderline accept, 倾向 Findings)\n\n### Strengths\nS1. 问题形式化清晰且重要（QE vs selection, instance-level vs per-sample 分类法）。\nS2. 实验覆盖异常全面（5 signal × 4 datasets × 2 models × scale/temp/epoch/N ablations + supervised/hidden probe/DeBERTa/verbalized confidence/free-form/calibration/OOD）。\nS3. 统计方法正确且透明度高（bootstrap CI, TOST, MDE, 多重比较标注）。\nS4. Negative results 诚实报告。\nS5. 混淆变量控制充分（thinking token, epoch, SJ normalizer, FK independence, length-LP）。\n\n### Must-Fix (Critical)\nN1. 核心分解公式 E[ΔF1] ≈ (1-d)·Δ_oracle·g(ρ_within) 是 underdetermined 启发式：g 无理论推导，仅 3 data points \"验证\"。23 个 configurations (Fig 3) 的数据未用于验证分解公式预测精度。\nN2. Within-instance ρ(LP, F1) 作为因果预测因子具有循环性：需 gold labels 才能计算，仅为回顾性诊断。Gating protocol (50 instances, threshold 0.3) 验证不足：(a) bootstrap SE 未报告；(b) 仅 3 dataset with large margins；(c) 0.3 threshold 来源不明。\n\n### Should-Fix (Warning)\nW1. \"Tuning-free\" threshold 不准确：θ=2/N 是观察所有数据集后选择的，非先验原则。\nW2. Entity construction 的 \"Resolving\" framing 过强：实际仅恢复 8-11% oracle headroom。\nW3. SciERC Thinking Token Confound：无意引入的训练-推理不一致，应在正文中明确声明。\nW4. 3 seeds 统计功效有限：SciERC LP selection σ=0.48pp ≈ effect size 本身。\nW5. English-only + NER-heavy 泛化局限未讨论语言覆盖。\n\n### Minor\nM1-M5: F1 metric 用法不一致, Table 3 单 seed 误导, orphan bib, \"as a reviewer correctly noted\" 措辞, Figure 1 caption ρ up to 0.45 来源。\n\n### Questions\nQ1. 分解公式能否在 23 configurations 上做回归验证？Predicted vs actual gain 相关性？\nQ2. Gating 的 50 instances 选择方式？Bootstrap CI？Threshold 0.3 敏感性？\nQ3. Degeneracy rises with capability (8B>4B) 是否因 convergence 差异？有无 matched-convergence 对比？\nQ4. Entity construction precision-recall trade-off 数据？\nQ5. Constrained decoding + post-hoc parsing 是否有更多 headroom？Task asymmetry (NER vs RE) 解释？\n\n### Missing References\n- Jiang et al. (2023) LLM-Blender\n- Ravaut et al. (2022) SummaReranker",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告 — Round 1\n\n**Overall**: 3.5/5 (Borderline accept, 倾向 Findings)\n\n### Strengths\nS1. 问题形式化清晰且重要（QE vs selection, instance-level vs per-sample 分类法）。\nS2. 实验覆盖异常全面（5 signal × 4 datasets × 2 models × scale/temp/epoch/N ablations + supervised/hidden probe/DeBERTa/verbalized confidence/free-form/calibration/OOD）。\nS3. 统计方法正确且透明度高（bootstrap CI, TOST, MDE, 多重比较标注）。\nS4. Negative results 诚实报告。\nS5. 混淆变量控制充分（thinking token, epoch, SJ normalizer, FK independence, length-LP）。\n\n### Must-Fix (Critical)\nN1. 核心分解公式 E[ΔF1] ≈ (1-d)·Δ_oracle·g(ρ_within) 是 underdetermined 启发式：g 无理论推导，仅 3 data points \"验证\"。23 个 configurations (Fig 3) 的数据未用于验证分解公式预测精度。\nN2. Within-instance ρ(LP, F1) 作为因果预测因子具有循环性：需 gold labels 才能计算，仅为回顾性诊断。Gating protocol (50 instances, threshold 0.3) 验证不足：(a) bootstrap SE 未报告；(b) 仅 3 dataset with large margins；(c) 0.3 threshold 来源不明。\n\n### Should-Fix (Warning)\nW1. \"Tuning-free\" threshold 不准确：θ=2/N 是观察所有数据集后选择的，非先验原则。\nW2. Entity construction 的 \"Resolving\" framing 过强：实际仅恢复 8-11% oracle headroom。\nW3. SciERC Thinking Token Confound：无意引入的训练-推理不一致，应在正文中明确声明。\nW4. 3 seeds 统计功效有限：SciERC LP selection σ=0.48pp ≈ effect size 本身。\nW5. English-only + NER-heavy 泛化局限未讨论语言覆盖。\n\n### Minor\nM1-M5: F1 metric 用法不一致, Table 3 单 seed 误导, orphan bib, \"as a reviewer correctly noted\" 措辞, Figure 1 caption ρ up to 0.45 来源。\n\n### Questions\nQ1. 分解公式能否在 23 configurations 上做回归验证？Predicted vs actual gain 相关性？\nQ2. Gating 的 50 instances 选择方式？Bootstrap CI？Threshold 0.3 敏感性？\nQ3. Degeneracy rises with capability (8B>4B) 是否因 convergence 差异？有无 matched-convergence 对比？\nQ4. Entity construction precision-recall trade-off 数据？\nQ5. Constrained decoding + post-hoc parsing 是否有更多 headroom？Task asymmetry (NER vs RE) 解释？\n\n### Missing References\n- Jiang et al. (2023) LLM-Blender\n- Ravaut et al. (2022) SummaReranker",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2488 · 2026-05-19T06:19:04.326447+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1713
}
```

</details>

---


### Assistant

_source line 2489 · 2026-05-19T06:19:07.578262+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 189

## Round 189

2 recorded events


### User

_source line 2490 · 2026-05-19T06:19:10.351347+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**3.5/5，Borderline accept，倾向 Findings**。论文在实验覆盖和统计透明度上表现优秀，但有两个 critical 问题：(1) 核心分解公式仅用 3 个数据点验证，属 underdetermined 启发式；(2) within-instance ρ(LP, F1) 需 gold labels 计算，作为"因果预测因子"有循环性，且 gating protocol 仅 50 instances / 3 数据集验证不充分。Entity construction 增益约 1 pp（恢复 oracle headroom 的 ~10%），"Resolving" 的 framing 过强。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2491 · 2026-05-19T06:19:15.474466+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 190

## Round 190

2 recorded events


### User

_source line 2492 · 2026-05-19T06:20:59.088197+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的交叉回应

### Strengths
- [AGREE] R1-S1 到 R1-S5：全部同意。与我的独立评价一致。补充：S1 中 instance-level vs per-sample 分类有效，但 instance-level 信号不能做 within-instance selection 是分类法的直接推论（by construction）。

### Must-Fix
- [AGREE] R1-N1：分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 确实 underdetermined。补充：23 configurations（Figure 3）的数据完全可以做 predicted vs actual 的回归验证但论文未做，是明显遗漏。g(·) 无函数形式使得验证不可能。
- [AGREE] R1-N2：within-instance ρ(LP,F1) 需 gold labels，仅为回顾性诊断——比我对 gating 的评价（仅指出 margin 过大）更本质。Gating 的 50 instances 无 bootstrap SE、0.3 threshold 来源不明、仅 3 dataset trivially separable。

### Should-Fix
- [AGREE] R1-W1："Tuning-free" 不准确。Appendix Table 25 的 θ sweep 说明 θ=2/N 是 post-hoc observation。
- [AGREE] R1-W2："Resolving" framing 过强。Entity construction 仅恢复 7.8-11.3% oracle headroom。我在 N2 中从新颖性角度提出了同样关切。
- [REBUT] R1-W3：Thinking token confound 的严重程度被高估。Appendix F 三方面论证（LP shift 仅 2.68% of range, constant prefix cancellation, CoNLL 控制组反驳假说）组合起来有说服力。已在 footnote 和 Limitations 中提及。
- [AGREE] R1-W4：3 seeds 功效有限，但 Few-NERD σ=0.04pp（50× more stable），关键 positive result 是 robust 的。
- [AGREE] R1-W5：English-only 泛化局限未在 Limitations 中讨论，是遗漏。

### Minor
- [AGREE] R1-M1/M2/M3/M5：F1 用法不一致、Table 3 单 seed、orphan bib、Figure 1 caption ρ 近似值。
- [REBUT] R1-M4："as a reviewer correctly noted" 如果是首次提交则应删除，但这是措辞问题非实质问题。

### Questions
- [AGREE] R1-Q1/Q2/Q3/Q5：分解公式定量验证、gating 细节、matched-convergence、task asymmetry 解释均合理。
- [REBUT] R1-Q4：论文已说明 construction 是 recall-driven（Section 4.6 line 211），P/R 表是合理但非 critical 的补充。

### Missing References
- [AGREE] LLM-Blender (Jiang et al. 2023) 是 significant omission——output fusion pipeline 直接相关。
- [REBUT] SummaReranker (Ravaut et al. 2022) 相关性较弱，论文已有 learned verifier 引用覆盖。

### 综合
R1 给 3.5/5 倾向 Findings，我给 3.0/5 Borderline。核心分歧不大。R1 在分解公式和 gating 循环性上的分析比我更深入。我比 R1 更关切 entity construction 新颖性和 scope 限制。维持 3.0/5，如定位为 Findings 可接受 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2493 · 2026-05-19T06:21:04.963504+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 191

## Round 191

12 recorded events


### User

_source line 2494 · 2026-05-19T06:21:07.816378+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心判断：与 R1 在大部分问题上 converge。R1 的分解公式批评（N1）和 gating 循环性分析（N2）比我更具体，我在 entity construction 新颖性和 scope 限制上比 R1 更严格。在 thinking token confound（W3）和 SummaReranker 引用上有分歧，均非重大分歧。两人评分差距 0.5 分（3.0 vs 3.5），如定位 Findings 可 converge 到 3.5。

---

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Strengths 回应

**[AGREE] R2-S1 (统计严谨性)**: 完全同意。我在自己的审稿中也将此列为主要优势（S3）。论文主动标注 post-hoc 分析（ε=0.05 → p_adj=0.14, Appendix D/App K）、报告 MDE（Section 4.3 footnote: ≈1.5pp at 80% power）、以及 3-seed 功效局限性（Appendix F），在 NLP 论文中属最佳实践。

**[AGREE] R2-S2 (QE vs selection 分离)**: 同意。这是论文最重要的概念贡献之一，我在 S1 中也强调了这一点。

**[AGREE] R2-S3 (难度梯度)**: 同意。4 个数据集各有明确实验角色（Section 4.1: SciERC=primary medium-difficulty, Few-NERD=low-degeneracy contrast, CoNLL=ceiling control, WNUT=signal-collapse boundary），实验设计有策略性。

**[AGREE] R2-S4 (诚实负结果)**: 同意。

**[AGREE] R2-S5 (写作质量)**: 同意。论文叙事紧凑，无明显 AI 写作标志。

---

## Must-Fix 回应

**[REBUT] R2-N1 (Correlation-selection gap 新颖性存疑)**

R2 的论点有合理之处但过于绝对。需要拆分讨论：

(a) "4/5 信号 selection 失败是 by construction"——这一点 R2 说得对，论文自己也明确承认（Section 3.1: "by construction"; Section 4.3 第一段）。但 R2 忽略了论文在此基础上做的两件事：第一，将 4 个信号转换为 MBR consensus-proximity 进行 per-sample ranking（Section 3.2 SJ 定义处: "consensus-proximity converts this to per-sample utility"），然后实证验证这些 MBR variants 也不 work（Table 2）——这 **不是** by construction 能推出的，因为 consensus-proximity **确实** 给不同 sample 赋予不同分数；第二，LP 作为唯一 natively per-sample signal 也失败——这完全是 empirical discovery。

(b) "LP-quality alignment 接近同义反复"——我部分同意这个批评，在自己的审稿 N2 中也指出了循环性问题。但 R2 说"接近同义反复"过于笼统：论文的贡献不是说"alignment 高则 selection 好"（确实近乎同义反复），而是诊断出 **两个具体机制**（degeneracy + LP compression）阻碍 alignment，并用温度消融（Table 16: T=1.2 degeneracy 14.9% 但 ρ=0.225）和 epoch 消融（Table 22: SciERC 3-point curve）分离了二者。这些机制的识别和分离不是同义反复。

(c) "umbrella term 模糊了真正的 empirical contribution"——同意此批评的方向。建议作者将 "correlation-selection gap" 更多作为现象描述而非方法论贡献来定位，将重心放在 degeneracy/compression 的因果分析上。

**综合判断**：R2-N1 的核心批评（by construction 部分不算 discovery）有道理，但将整个 correlation-selection gap 概念定性为非新颖则过度了。论文有实质的 empirical 贡献（MBR conversion 失败、LP 在不同 regime 下的行为差异、degeneracy-convergence 的因果关系），只是被 umbrella framing 弱化了。建议作者重新组织 narrative emphasis，而非否定贡献本身。**不构成 reject 理由。**

---

**[AGREE] R2-N2 (Entity construction 新颖性有限)**

同意 R2 的判断。我在自己的审稿 W2 中也指出了类似问题。具体证据：

- 论文自己引用了 Florian et al. (2003) 并承认 entity construction "adapts entity voting from ensemble NER to stochastic sampling"（Section 1 Contribution 3, Section 5.4）
- 新增量仅为：(a) 从 multi-model ensemble 迁移到 single-model stochastic sampling；(b) LP weighting vs uniform weighting（Table 5: LP-weighted +1.02 vs Uniform +0.74 on SciERC，差异 0.28pp）
- LP weighting 的增量在 SciERC 上仅 0.28pp，在 Few-NERD 上 0.66pp——这些差异本身可能在 seed noise 范围内（Few-NERD σ=0.51pp for LP-weighted）

但我不认为这应该是 critical/must-fix：论文的核心贡献是诊断框架（Contribution 1-2），construction 是 "the diagnostic naturally motivates" 的自然推论。如果将 construction 降级为 "straightforward application motivated by our diagnostic"，论文仍然成立。建议作者调整 narrative 强度（同我的 W2），而非将 construction 视为主要贡献。

---

**[REBUT] R2-N3 (负结果 scope 限制过强)**

R2 的批评方向合理但严重程度被高估了：

(a) "仅在 fine-tuned 4B-8B + constrained decoding 下成立"——论文在 Limitations 和 Appendix L 中明确声明了这些 scope 限制（Limitations 第 1-2 段, Appendix P: "Our negative results are specific to fine-tuned models with constrained decoding"）。这不是隐瞒，而是诚实的 scope declaration。

(b) "Free-form RE LP selection 反转"——R2 说的是对的（Appendix L, Table 13 Panel B: -0.68pp → +1.69pp），但论文已经在附录中充分讨论了这一发现，且明确标注 RE 为 "exploratory single-benchmark analysis"（Appendix M 开头）。更重要的是，NER 在 free-form 下 selection 仍不 work（Panel B: +0.59pp → +0.18pp, Section 4.3），所以 R2 挑出 RE 反转来质疑整体结论是 cherry-picking。

(c) "70B+ 未测试"——论文在 Limitations 第 2 段已明确声明："whether the gap holds for 70B+ models or closed-source APIs is untested"。每篇论文都有 scale 限制，这不应成为 critical 问题，除非 reviewer 认为存在强先验理由表明 70B+ 会有质性不同的行为。论文还分析了 degeneracy 随 scale 增加的趋势（Table 4: 8B 17.8% vs 4B 10.4%），暗示 70B+ 的 degeneracy 可能更高，使选择更困难而非更容易。

**综合判断**：R2 将 scope 限制列为 critical/must-fix 不合理。论文的 scope 声明已经足够清晰和诚实。Fine-tuned models + constrained decoding 是当前 production NER 的主流范式（Section 1: "the dominant deployment paradigm for production NER"），在此范式下的发现有充分的实践价值。建议降级为 warning。

---

## Should-Fix 回应

**[AGREE] R2-W1 (SciERC 功效不足)**

同意。SciERC n=529 的 MDE≈1.5pp（Section 4.3 footnote）确实太大。论文 claim LP selection 不 work on SciERC，但实际上是 underpowered to detect。Few-NERD (n=32,565, MDE≈0.22pp) 是更 definitive 的测试，论文也这样说了（"Few-NERD provides the definitive test"）。建议作者在正文中更明确地标注 SciERC 的 selection 结果为 "underpowered" 而非 "no effect"。

但需要注意：SciERC 在 QE 分析和 entity construction 上仍然是 informative dataset（n=529 对于 Spearman ρ 和 bootstrap CI 是足够的）。R2 建议"以 Few-NERD 为 primary"是合理的实验设计建议，但不意味着 SciERC 的结果无价值。

---

**[AGREE] R2-W2 (分解公式缺乏理论基础)**

完全同意。我在自己的审稿 N1 中将此列为 critical issue。E[ΔF1] ≈ (1-d) · Δ_oracle · g(ρ_within) 中 g 是"assumed monotonically increasing"，用 3 个数据点验证 consistency 是 underdetermined。R2 和我的判断一致。

---

**[AGREE] R2-W3 (Gating protocol 验证不足)**

同意。我在 N2 中也提出了相同批评。50 instances、3 datasets with large inter-dataset margins、threshold 0.3 的来源未说明。

---

**[REBUT] R2-W4 (Related Work 偏短)**

部分不同意。Related Work 虽仅约 1 column，但覆盖了 4 个清晰的主题块：(a) self-consistency + test-time scaling, (b) consistency for structured IE, (c) uncertainty estimation + MBR, (d) BoN + learned verifiers。引用密度合理（70 个引用中大部分分布在此 section 和 Introduction）。

但 R2 关于 "缺少与 Taubenfeld/Kang 技术差异对比" 的具体批评有道理。论文引用了 Taubenfeld et al. (2025, CISC) 和 Kang et al. (2025, Self-Certainty) 但仅在 Related Work 中一句带过（Section 2 line 5: "reward-free selectors"），未讨论它们为何不适用于 structured prediction。尤其是 Self-Certainty 在 Limitations 中被列为 "not evaluated" 的 per-sample signal（Limitations 第 13 段），应该在 Related Work 中解释为何未测试。

**综合判断**：Related Work 长度本身不是问题（ACL 对 RW 长度无硬性要求），但 Taubenfeld/Kang 的技术对比确实缺失。同意 R2 的具体批评，不同意泛泛的"偏短"判断。

---

**[AGREE] R2-W5 (Greedy F1 多值问题)**

同意这是一个 presentation 问题。论文在 Section 3.3 中解释了 4 个 SciERC greedy F1 值（0.640, 0.644, 0.645, 0.650）的来源（"protocol variants: primary seed vs. multi-seed mean, 5-epoch vs. 3-epoch checkpoint, and gold-filtered vs. full test set"），且"each table specifies its protocol"。但这仍然给读者增加了不必要的认知负担。建议在某个表格中统一列出所有 protocol variants 及其对应 F1 值。

---

## Minor 回应

**[AGREE] R2-M1**: Abstract 中 LP 缩写确实未在 Abstract 内展开（仅写 "log-probability (LP)"——等等，我重新检查：Abstract line 5 写的是 "log-probability (LP)"，这**已经展开了**。R2 的批评可能不成立。需要 R2 澄清指的是哪个缩写。

**[AGREE] R2-M2**: `\textendash` 兼容性是排版细节，不影响内容。

**[AGREE] R2-M3**: Orphan bib entries 应清理。

**[AGREE] R2-M4**: Table 2 中 EM 和 VC 的 p-values 显示为 "---" 而非数值，原因可能是它们显著低于 greedy（EM 0.637 < greedy 0.645, VC 0.623 < greedy 0.645），所以 one-sided p-value 为 1.0 或未计算。论文应统一报告所有 p-values。

**[AGREE] R2-M5**: Checklist E1 的声明是 minimal compliance。

---

## Questions 回应

**[AGREE with nuance] R2-Q1 (Cross-instance vs within-instance ρ 差异)**

好问题。Few-NERD cross-instance LP ρ=0.220（Table 3）远低于 within-instance ρ=0.667（Table 14）。这并不矛盾：cross-instance ρ 衡量的是"across different inputs, LP 是否预测 F1"，而 within-instance ρ 衡量的是"within the same input, LP 是否区分好坏 sample"。两者度量不同的东西。一个信号可以在 instance 内有好的排序能力但在 instance 间的绝对分数上与 F1 相关性弱。论文在 Section 3.3 和 4.3 中暗示了这一区别但未明确阐述。建议作者加一句解释。

但这也反映了论文的一个更深层问题：cross-instance ρ（QE metric）和 within-instance ρ（selection metric）的关系被论文描述为 "decoupling"（Section 5 第一句），但这种 decoupling 的数学条件未被讨论。

---

**[AGREE] R2-Q2 (Entity construction 在 CoNLL 降 F1)**

合理担忧。Table 5 CoNLL: construction -0.39pp (n.s.)。Section 5.4 的 gating protocol 通过 adjusted ρ<0.3 将 CoNLL 路由到 construction 而非 LP selection——但如果 construction 本身在 CoNLL 上有害，那 gating 应该路由到"什么都不做"（即 stick with greedy），而非 construction。论文的 gating protocol 似乎只在 LP selection vs construction 之间选择，没有 "neither" option。这是 gating protocol 的设计缺陷。

---

**[REBUT] R2-Q3 (Constrained decoding 是否是 failure 根本原因)**

不同意这一推断。论文在 Appendix L (Table 13) 中展示了：
- NER: constrained +0.59pp → free-form +0.18pp，两种 regime 下 selection 均无效
- RE: constrained -0.68pp → free-form +1.69pp，反转

NER 是论文的主要任务，在 NER 上 constrained decoding **不是** failure 的根本原因——free-form 同样不 work。RE 反转是一个有趣的 task-specific interaction，但 RE 在本文中是 exploratory extension（Appendix M: "exploratory single-benchmark analysis"）。

更重要的是，free-form decoding 的 LP distribution 与 constrained 几乎相同（Table 13 Panel A: within-instance std ratio 0.97×, tied fraction 59.7% vs 57.7%）。这表明 LP compression 是 model-intrinsic 而非 decoding-regime artifact。

---

**[AGREE] R2-Q4 (Self-Certainty/P(True) 未测试)**

同意这是一个局限。论文在 Limitations 第 13 段提到了 Self-Certainty (Kang et al., 2025) 和 P(True) (Kadavath et al., 2022) 作为未测试的 per-sample signals，并承认 "whether they suffer from similar compression under fine-tuning is unknown"。

但 R2 说这削弱了 "no per-sample signal works" 结论——需要澄清：论文的结论不是 "no per-sample signal works in general"，而是 "LP, the sole per-sample signal **in our study**, fails on most configurations"。论文还测试了 verbalized confidence 作为第二个 per-sample signal（Appendix T: 同样失败，甚至更差），以及 hidden state probes（Appendix G: correlation 更高但 selection 更差）。所以结论是 "our evaluated per-sample signals don't work"，不是 universal claim。但确实，Self-Certainty 作为一个明确设计用于 BoN selection 的信号，缺失是一个实验覆盖 gap。

---

## Missing References 回应

**[AGREE] Li et al. (2025) 和 Muennighoff et al. (2025, s1)**: 确认这两个在 bib 中但未被引用（8 个 orphan entries 之二）。应要么引用要么删除。

**[REBUT] Lafferty et al. (2001) CRF**: 不同意这是 missing reference。本文研究的是 LLM-based generative NER，不使用 CRF/sequence labeling 架构。CRF 在 structured prediction confidence 方面有历史相关性，但 Culotta and McCallum (2004) 已经被引用且涵盖了 structured prediction confidence 的早期工作。要求引用 CRF 原论文相当于要求每篇 NER 论文都引用 HMM 原论文——过于宽泛。

---

## 总结

与 R2 的主要分歧点：
1. **N1 severity**: R2 认为 correlation-selection gap 整体新颖性存疑（critical），我认为 by-construction 部分确实不算 discovery 但 LP compression/degeneracy 的因果分析有实质贡献（warning level）。
2. **N3 severity**: R2 认为 scope 限制是 critical，我认为论文的 scope declaration 已经足够清晰且覆盖了主流 deployment paradigm（应降为 warning）。
3. **Q3 推断**: R2 暗示 constrained decoding 可能是 failure 根本原因，但 NER free-form 数据（Table 13）直接反驳了这一推断。

与 R2 一致的判断：
1. Entity construction 新颖性有限（N2），但可通过 narrative 调整缓解
2. 分解公式验证不足（W2）——我也列为 critical
3. Gating protocol 验证不足（W3）——我也列为 critical
4. Self-Certainty/P(True) 缺失是实验覆盖 gap（Q4）


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2495 · 2026-05-19T06:21:47.999248+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 2496 · 2026-05-19T06:21:48.100089+00:00_

1	issues:
2	  # ===== 历史 resolved issues（保留记录）=====
3	  - id: "R1-W1"
4	    summary: "Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应"
5	    category: experiment
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 1
9	    last_seen_round: 19
10	    resolution: "Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。"
11	    resolution_round: 19
12	
13	  - id: "R1-W2"
14	    summary: "\"Two jointly necessary conditions\" 因果性表述过强"
15	    category: framing
16	    severity: critical
17	    status: resolved
18	    first_raised_round: 1
19	    last_seen_round: 21
20	    resolution: "全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。"
21	    resolution_round: 21
22	
23	  - id: "R2-N1"
24	    summary: "Contribution 1 'methodological premise' 是定义推论"
25	    category: framing
26	    severity: critical
27	    status: resolved
28	    first_raised_round: 1
29	    last_seen_round: 19
30	    resolution: "Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。"
31	    resolution_round: 19
32	
33	  - id: "R2-N2"
34	    summary: "与 MBR 文献差异化定位不够锐利"
35	    category: framing
36	    severity: warning
37	    status: resolved
38	    first_raised_round: 1
39	    last_seen_round: 19
40	    resolution: "Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。"
41	    resolution_round: 19
42	
43	  - id: "R2-N4"
44	    summary: "模型规模 3B-8B，70B+ 未知"
45	    category: experiment
46	    severity: info
47	    status: resolved
48	    first_raised_round: 1
49	    last_seen_round: 19
50	    resolution: "Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2497 · 2026-05-19T06:21:51.332686+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "50",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "50",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2498 · 2026-05-19T06:21:51.333346+00:00_

50	    resolution: "Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。"
51	    resolution_round: 19
52	
53	  - id: "R1-W3"
54	    summary: "2-seed 统计效力不足"
55	    category: experiment
56	    severity: warning
57	    status: resolved
58	    first_raised_round: 1
59	    last_seen_round: 19
60	    resolution: "Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。"
61	    resolution_round: 19
62	
63	  - id: "R1-W4"
64	    summary: "Per-entity-type non-independence"
65	    category: experiment
66	    severity: warning
67	    status: resolved
68	    first_raised_round: 1
69	    last_seen_round: 19
70	    resolution: "Reviewer PASS: appendix ICC=-0.004 written。"
71	    resolution_round: 19
72	
73	  - id: "R1-W5"
74	    summary: "\"Supervised verifier\" framing 误导"
75	    category: framing
76	    severity: warning
77	    status: resolved
78	    first_raised_round: 1
79	    last_seen_round: 19
80	    resolution: "Reviewer PASS: 'supervised verifier' 0 matches。"
81	    resolution_round: 19
82	
83	  - id: "R1-W6"
84	    summary: "Degeneracy 定义需区分"
85	    category: writing
86	    severity: warning
87	    status: resolved
88	    first_raised_round: 1
89	    last_seen_round: 19
90	    resolution: "Round 20 检查 PASS: introduction.tex 有完整定义。"
91	    resolution_round: 19
92	
93	  - id: "R1-W7"
94	    summary: "SciERC greedy F1 不一致"
95	    category: experiment
96	    severity: info
97	    status: resolved
98	    first_raised_round: 1
99	    last_seen_round: 19
100	    resolution: "Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。"
101	    resolution_round: 19
102	
103	  - id: "R2-W1"
104	    summary: "Abstract 数字过载"
105	    category: writing
106	    severity: warning
107	    status: resolved
108	    first_raised_round: 1
109	    last_seen_round: 19
110	    resolution: "Reviewer PASS: Abstract 含 3 个数字 (≤3)。"
111	    resolution_round: 19
112	
113	  - id: "R2-W2"
114	    summary: "Actionable contribution 偏薄"
115	    category: framing
116	    severity: warning
117	    statu
…[truncated 4029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2499 · 2026-05-19T06:21:54.956094+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "250",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "250",
    "limit": "500"
  }
}
```

</details>

---


### Tool result

_source line 2500 · 2026-05-19T06:21:55.007822+00:00_

250	    resolution: "Few-NERD 定位为 'definitive test'（footnote + L91），SciERC 为 diagnosis site，MDE 已注明。"
251	    resolution_round: 21
252	
253	  - id: "R21-W3"
254	    summary: "DALS 定位与诊断性论文冲突 + ε data-snooping"
255	    category: framing
256	    severity: warning
257	    status: resolved
258	    first_raised_round: 21
259	    last_seen_round: 21
260	    resolution: "DALS 已移入 appendix (L1388)。ε sweep (L560-588) + LOO τ sensitivity (L1396-1398) 均已呈现。"
261	    resolution_round: 21
262	
263	  - id: "R21-W4"
264	    summary: "新颖性增量需更精确定位"
265	    category: framing
266	    severity: warning
267	    status: resolved
268	    first_raised_round: 21
269	    last_seen_round: 21
270	    resolution: "Intro L8 强化为 'first systematic empirical characterization of when and why LP-based selection succeeds or fails for structured prediction'。D154 within/cross 区分 + ρ=0.052 negative result 增强新颖性。"
271	    resolution_round: 21
272	
273	  - id: "R21-W5"
274	    summary: "LP ρ 跨表不一致 (0.205 vs 0.215)"
275	    category: experiment
276	    severity: warning
277	    status: resolved
278	    first_raised_round: 21
279	    last_seen_round: 21
280	    resolution: "审计确认论文全文 11 处统一使用 0.205，0.215 从未出现。D145 决策保持 mean_LP 0.205。"
281	    resolution_round: 21
282	
283	  - id: "R21-W6"
284	    summary: "Table 3 的 7 个连续脚注"
285	    category: writing
286	    severity: warning
287	    status: resolved
288	    first_raised_round: 21
289	    last_seen_round: 21
290	    resolution: "7→2 脚注。Reviewer PASS: 信息完整性通过，degeneracy 定义移入 Method §3.3。"
291	    resolution_round: 21
292	
293	  - id: "R21-W7"
294	    summary: "Greedy F1 多表数值不一致 (4 values)"
295	    category: experiment
296	    severity: warning
297	    status: resolved
298	    first_raised_round: 21
299	    last_seen_round: 21
300	    resolution: "Method §3.3 列出 4 值 + 3 类 protocol variants。Reviewer PASS。"
301	    resolution_round: 21
302	
303	  - id: "R21-I1"
304	    summary: "Appendix 残留实验标识"
305	    category: format
306	    severity: info
307	    status: reso
…[truncated 18378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2501 · 2026-05-19T06:25:05.908112+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n  # ===== 历史 resolved issues（保留记录）=====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance。\"\n    resolution_round: 21\n\n  - id: \"R2-W3\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-6 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文统一使用 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认无残留。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"已补入 Related Work。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix 已有 df=4 adjustment。\"\n    resolution_round: 21\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Multiple compression rounds completed. ≤8 pages confirmed.\"\n    resolution_round: 23\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Title updated to cover both diagnostic and resolving contributions.\"\n    resolution_round: 23\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R2 列为 critical，R1 建议降为 warning。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"§4.3 新增 expected gain decomposition。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 共识：(a) 4/5 信号 selection 失败是 by construction（定义推论），但 MBR conversion 失败和 LP regime 分析是真实 empirical contribution（R1 rebuttal 有效）；(b) 分解公式仅 3 data points 验证，23 configurations 数据未用（两位 Reviewer 共识 critical）；(c) 建议：将 by-construction 部分明确标为 definitional，聚焦 LP compression + degeneracy-alignment disentanglement 作为 empirical core。\"\n    action_items:\n      - round: 24\n        action: \"分解公式需在 23 configurations 上做 predicted vs actual 回归验证，或明确降级为 descriptive heuristic。\"\n        assigned_to: research_director\n        status: open\n      - round: 24\n        action: \"正文重组 narrative：by-construction 部分简化为 1 段 setup，LP failure + degeneracy/compression 分析作为 empirical core。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"LP and AUROC expanded in Abstract.\"\n    resolution_round: 23\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Dev set gating implemented.\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"SciERC seed sensitivity 高 (σ=0.48 pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Switched to multi-seed reporting throughout.\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Post-hoc 阈值有 data snooping 风险。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"θ=2/N shown as optimal with [0.15, 0.35] plateau.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 共识：'tuning-free' 仍不准确。θ=2/N 是观察所有数据集后选择的 works-reasonably-well 值，非先验推导。建议改为 'default heuristic threshold'。\"\n    action_items:\n      - round: 24\n        action: \"将 'tuning-free' 改为 'default threshold' 或 'heuristic threshold that requires no per-dataset tuning'。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Changed to 'a more effective self-consistency analogy'.\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Introduction qualified with 'fine-tuned 4B-8B models'.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24：scope 声明在 Introduction 和 Limitations 中已存在。R1 认为 fine-tuned+constrained 是主流 deployment paradigm，scope 声明充分。R2 仍认为应更突出。维持 warning/in_progress。\"\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"定义完整但分散。\"\n      - round: 24\n        reviewers: []\n        note: \"本轮未提及，可能已非优先。\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Fixed.\"\n    resolution_round: 23\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Related Work 缺少 ensemble-based NER methods 讨论。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Florian 2003 + EL4NER 2025 added.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 新增建议：LLM-Blender (Jiang et al. 2023) 与 output fusion 直接相关。Taubenfeld/Kang 技术差异对比仍缺。8 个 orphan bib entries 待清理。\"\n    action_items:\n      - round: 24\n        action: \"补充 Taubenfeld/Kang 技术差异对比。补充或删除 LLM-Blender。清理 orphan bib entries。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R22-FIG1\"\n    summary: \"fig_overview 缺少 Construction 贡献 + 残留 RE 文字\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"fig_overview regenerated as three-column layout.\"\n    resolution_round: 23\n\n  - id: \"R22-FIG2\"\n    summary: \"fig_selection_gap caption 仍引用旧双面板格式\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Regenerated as single-panel NER-only.\"\n    resolution_round: 23\n\n  - id: \"R23-N1\"\n    summary: \"Entity-level construction 新颖性不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 24\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立列为 critical。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 共识：entity construction = Florian et al. (2003) entity voting 迁移到 stochastic sampling + LP weighting。LP weighting 增量仅 0.28-0.66pp。R1 建议降级为 'straightforward application motivated by diagnostic'，不作为主要贡献。R2 维持 critical。Director 判断：作为独立方法贡献确实不足以支撑 EMNLP Main，但作为诊断的自然推论可接受——前提是 narrative 不将其作为核心卖点。\"\n    action_items:\n      - round: 24\n        action: \"将 entity construction 从 'principled resolution' 降级为 'diagnostic-motivated mitigation'。Title 中 'Resolving' 改为 'Addressing' 或 'Mitigating'。Contribution 3 降调。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R23-N2\"\n    summary: \"Correlation-selection gap 部分 by construction\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 24\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 critical，R1 部分同意。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 交叉后：R1 rebuttal 有效——MBR consensus-proximity 确实给不同 sample 赋不同分数，其失败是 empirical finding（非 by construction）。LP 失败和 degeneracy/compression 机制识别是真实贡献。但 'correlation-selection gap' umbrella term 模糊了 by-construction 与 empirical 的边界。建议：正文更清晰区分。\"\n\n  - id: \"R23-N3\"\n    summary: \"Expected selection gain 'bound' 中 g(·) 未定义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Changed to 'approximately factored as'. Framed as heuristic.\"\n    resolution_round: 23\n\n  - id: \"R23-W1\"\n    summary: \"ε=0.05 non-tied subset 是 post-hoc 最优切点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"标记为 exploratory。\"\n    resolution_round: 23\n\n  - id: \"R23-W2\"\n    summary: \"Complementarity claim 仅基于 2 informative data points\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Softened scope.\"\n    resolution_round: 23\n\n  - id: \"R23-W3\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Reduced to 4 key numbers.\"\n    resolution_round: 23\n\n  - id: \"R23-W4\"\n    summary: \"Table 4 (entity construction) 缺少 multi-seed ±σ\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Updated with multi-seed mean±σ.\"\n    resolution_round: 23\n\n  - id: \"R23-I1\"\n    summary: \"Figure 1 caption ρ scope 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Caption updated.\"\n    resolution_round: 23\n\n  - id: \"R23-I2\"\n    summary: \"WNUT-17 正文分析不足\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n\n  - id: \"R23-MR1\"\n    summary: \"缺失引用: Florian 2003, Luo 2023, Wiher 2022\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 24\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Core citations added. Luo 2023 pending.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"合并到 R22-MR1 统一跟踪。\"\n\n  # ===== Round 24 new issues =====\n\n  - id: \"R24-N1\"\n    summary: \"分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 仅 3 macro-level data points 验证，23 configurations 数据未用\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识 critical。g(·) 无函数形式，无理论推导。任何单调函数都能拟合 3 点。23 configurations (Fig 3) 完全可做回归验证但论文未做。需明确标注为 'descriptive heuristic' 或在 23 configs 上验证。\"\n    action_items:\n      - round: 24\n        action: \"在 23 configurations 上做 predicted vs actual gain 回归，或将分解公式降级为纯 illustration 并删除 'consistent with the observed data' 验证措辞。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R24-N2\"\n    summary: \"Gating protocol 循环性 + 验证不足：within-instance ρ(LP,F1) 需 gold labels，dev probe 仅 50 instances / 3 dataset / threshold 0.3 来源不明\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识 critical。(a) within-instance ρ 需 gold labels，仅为回顾性诊断；(b) dev probe 50 instances 无 bootstrap SE；(c) 0.3 threshold 来源未说明；(d) 仅 3 dataset with 'large inter-dataset margins'，不清楚 margins 窄时是否可靠；(e) gating 在 LP selection 与 construction 间选择但无 'neither'(greedy) option——CoNLL construction 有害时 gating 仍路由到 construction。\"\n    action_items:\n      - round: 24\n        action: \"报告 dev 50-instance adjusted ρ 的 bootstrap CI。讨论 threshold 0.3 敏感性（0.2-0.4 range）。Gating 增加 'greedy fallback' option（当 construction 也无效时）。明确 gating 为 preliminary protocol（非 validated），降低 narrative 权重。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R24-W1\"\n    summary: \"'Resolving' framing 过强：entity construction 仅恢复 8-11% oracle headroom (~1pp)\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识。SciERC 1.02/13.0≈8%, Few-NERD 1.40/12.4≈11%。Title 'Resolving' 和 Contribution 3 'principled resolution' 暗示问题已有效解决，但 90% oracle gap 仍在。\"\n    action_items:\n      - round: 24\n        action: \"Title: 'Resolving' → 'Addressing'/'Mitigating'。Contribution 3: 'principled resolution' → 'partial mitigation motivated by the diagnostic'。正文加 oracle recovery percentage。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R24-W2\"\n    summary: \"SciERC selection 结果 underpowered (n=529, MDE≈1.5pp) 但未明确标注\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"论文说 'Few-NERD provides the definitive test' 但 SciERC 仍是 primary test bed。SciERC LP σ=0.48pp ≈ effect size，方向 seed-dependent。建议正文更明确标注 SciERC selection 为 'underpowered/inconclusive'。\"\n    action_items:\n      - round: 24\n        action: \"在 SciERC selection 结果处明确标注 'underpowered to detect effects below 1.5pp'。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R24-W3\"\n    summary: \"Related Work 缺少与 Taubenfeld (CISC) / Kang (Self-Certainty) 的技术差异对比\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"两者在 Related Work 仅一句带过 ('reward-free selectors')，未讨论为何不适用于 structured prediction。Self-Certainty 在 Limitations 列为未测试但 RW 未解释为何不测。\"\n    action_items:\n      - round: 24\n        action: \"在 Related Work self-consistency paragraph 中增加 2-3 句，说明 CISC 和 Self-Certainty 依赖 answer-level equivalence grouping，在 entity-set partial overlap 场景下不直接适用。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R24-W4\"\n    summary: \"English-only + NER-heavy 泛化局限未在 Limitations 中讨论语言覆盖\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"4 NER + 1 RE，全部英文。Limitations 讨论了 scale 但未提及语言。\"\n    action_items:\n      - round: 24\n        action: \"Limitations 增加 1 句语言覆盖限制。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R24-W5\"\n    summary: \"Self-Certainty (Kang 2025) 和 P(True) (Kadavath 2022) 未测试，削弱 per-sample signal 结论的完整性\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"论文结论非 'no per-sample signal works in general'，而是 'our evaluated signals don't work'。但 Self-Certainty 是明确设计用于 BoN 的 per-sample signal，缺失是覆盖 gap。Verbalized confidence + hidden probes 已测但同样失败。\"\n\n  - id: \"R24-W6\"\n    summary: \"Appendix D 'as a reviewer correctly noted' 暗示审稿历史，首次提交应删除\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1]\n        note: \"如果这是首次投稿，此措辞泄露了内部审稿过程。\"\n    action_items:\n      - round: 24\n        action: \"删除 'as a reviewer correctly noted'，改为直接陈述。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R24-I1\"\n    summary: \"Table 2 中 EM/VC 的 p 值标 '---' 应报告具体数值\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"EM/VC 低于 greedy，p=1.0 或类似值应明确报告而非用 ---。\"\n\n  - id: \"R24-I2\"\n    summary: \"F1 metric 术语不统一 (instance-level macro / span-level micro / per-sample)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1]\n        note: \"Table 2 caption 说 'macro F1' 但 §3.3 说 'per-instance macro-F1'。需统一。\"\n\n  - id: \"R24-I3\"\n    summary: \"8 个 orphan bib entries 待清理\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"在 .bib 中但未被 cite。应清理或 cite。\"\n\n  - id: \"R24-I4\"\n    summary: \"SJ 分母 max(|g_i|, |g_j|) 当两 sample 都不含某类型 entity 时为 0 的边界情况未讨论\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1]\n        note: \"E_∪=∅ 时 VC=0 已有 footnote，但 SJ 的分母边界情况未提及。\"\n\n  - id: \"R24-I5\"\n    summary: \"Abstract ρ up to 0.45 取自 CoNLL EM（最易数据集），易给读者过于乐观印象\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"SciERC 上最高仅 0.379。建议加注 dataset context 或报告 median。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n  # ===== 历史 resolved issues（保留记录）=====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance。\"\n    resolution_round: 21\n\n  - id: \"R2-W3\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-6 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文统一使用 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认无残留。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"已补入 Related Work。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix 已有 df=4 adjustment。\"\n    resolution_round: 21\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Multiple compression rounds completed. ≤8 pages confirmed.\"\n    resolution_round: 23\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Title updated to cover both diagnostic and resolving contributions.\"\n    resolution_round: 23\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R2 列为 critical，R1 建议降为 warning。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"§4.3 新增 expected gain decomposition。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 共识：(a) 4/5 信号 selection 失败是 by construction（定义推论），但 MBR conversion 失败和 LP regime 分析是真实 empirical contribution（R1 rebuttal 有效）；(b) 分解公式仅 3 data points 验证，23 configurations 数据未用（两位 Reviewer 共识 critical）；(c) 建议：将 by-construction 部分明确标为 definitional，聚焦 LP compression + degeneracy-alignment disentanglement 作为 empirical core。\"\n    action_items:\n      - round: 24\n        action: \"分解公式需在 23 configurations 上做 predicted vs actual 回归验证，或明确降级为 descriptive heuristic。\"\n        assigned_to: research_director\n        status: open\n      - round: 24\n        action: \"正文重组 narrative：by-construction 部分简化为 1 段 setup，LP failure + degeneracy/compression 分析作为 empirical core。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"LP and AUROC expanded in Abstract.\"\n    resolution_round: 23\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Dev set gating implemented.\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"SciERC seed sensitivity 高 (σ=0.48 pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Switched to multi-seed reporting throughout.\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Post-hoc 阈值有 data snooping 风险。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"θ=2/N shown as optimal with [0.15, 0.35] plateau.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 共识：'tuning-free' 仍不准确。θ=2/N 是观察所有数据集后选择的 works-reasonably-well 值，非先验推导。建议改为 'default heuristic threshold'。\"\n    action_items:\n      - round: 24\n        action: \"将 'tuning-free' 改为 'default threshold' 或 'heuristic threshold that requires no per-dataset tuning'。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Changed to 'a more effective self-consistency analogy'.\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Introduction qualified with 'fine-tuned 4B-8B models'.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24：scope 声明在 Introduction 和 Limitations 中已存在。R1 认为 fine-tuned+constrained 是主流 deployment paradigm，scope 声明充分。R2 仍认为应更突出。维持 warning/in_progress。\"\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"定义完整但分散。\"\n      - round: 24\n        reviewers: []\n        note: \"本轮未提及，可能已非优先。\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Fixed.\"\n    resolution_round: 23\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Related Work 缺少 ensemble-based NER methods 讨论。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Florian 2003 + EL4NER 2025 added.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 新增建议：LLM-Blender (Jiang et al. 2023) 与 output fusion 直接相关。Taubenfeld/Kang 技术差异对比仍缺。8 个 orphan bib entries 待清理。\"\n    action_items:\n      - round: 24\n        action: \"补充 Taubenfeld/Kang 技术差异对比。补充或删除 LLM-Blender。清理 orphan bib entries。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R22-FIG1\"\n    summary: \"fig_overview 缺少 Construction 贡献 + 残留 RE 文字\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"fig_overview regenerated as three-column layout.\"\n    resolution_round: 23\n\n  - id: \"R22-FIG2\"\n    summary: \"fig_selection_gap caption 仍引用旧双面板格式\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Regenerated as single-panel NER-only.\"\n    resolution_round: 23\n\n  - id: \"R23-N1\"\n    summary: \"Entity-level construction 新颖性不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 24\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立列为 critical。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 共识：entity construction = Florian et al. (2003) entity voting 迁移到 stochastic sampling + LP weighting。LP weighting 增量仅 0.28-0.66pp。R1 建议降级为 'straightforward application motivated by diagnostic'，不作为主要贡献。R2 维持 critical。Director 判断：作为独立方法贡献确实不足以支撑 EMNLP Main，但作为诊断的自然推论可接受——前提是 narrative 不将其作为核心卖点。\"\n    action_items:\n      - round: 24\n        action: \"将 entity construction 从 'principled resolution' 降级为 'diagnostic-motivated mitigation'。Title 中 'Resolving' 改为 'Addressing' 或 'Mitigating'。Contribution 3 降调。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R23-N2\"\n    summary: \"Correlation-selection gap 部分 by construction\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 24\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 critical，R1 部分同意。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 交叉后：R1 rebuttal 有效——MBR consensus-proximity 确实给不同 sample 赋不同分数，其失败是 empirical finding（非 by construction）。LP 失败和 degeneracy/compression 机制识别是真实贡献。但 'correlation-selection gap' umbrella term 模糊了 by-construction 与 empirical 的边界。建议：正文更清晰区分。\"\n\n  - id: \"R23-N3\"\n    summary: \"Expected selection gain 'bound' 中 g(·) 未定义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Changed to 'approximately factored as'. Framed as heuristic.\"\n    resolution_round: 23\n\n  - id: \"R23-W1\"\n    summary: \"ε=0.05 non-tied subset 是 post-hoc 最优切点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"标记为 exploratory。\"\n    resolution_round: 23\n\n  - id: \"R23-W2\"\n    summary: \"Complementarity claim 仅基于 2 informative data points\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Softened scope.\"\n    resolution_round: 23\n\n  - id: \"R23-W3\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Reduced to 4 key numbers.\"\n    resolution_round: 23\n\n  - id: \"R23-W4\"\n    summary: \"Table 4 (entity construction) 缺少 multi-seed ±σ\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Updated with multi-seed mean±σ.\"\n    resolution_round: 23\n\n  - id: \"R23-I1\"\n    summary: \"Figure 1 caption ρ scope 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Caption updated.\"\n    resolution_round: 23\n\n  - id: \"R23-I2\"\n    summary: \"WNUT-17 正文分析不足\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n\n  - id: \"R23-MR1\"\n    summary: \"缺失引用: Florian 2003, Luo 2023, Wiher 2022\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 24\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Core citations added. Luo 2023 pending.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"合并到 R22-MR1 统一跟踪。\"\n\n  # ===== Round 24 new issues =====\n\n  - id: \"R24-N1\"\n    summary: \"分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 仅 3 macro-level data points 验证，23 configurations 数据未用\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识 critical。g(·) 无函数形式，无理论推导。任何单调函数都能拟合 3 点。23 configurations (Fig 3) 完全可做回归验证但论文未做。需明确标注为 'descriptive heuristic' 或在 23 configs 上验证。\"\n    action_items:\n      - round: 24\n        action: \"在 23 configurations 上做 predicted vs actual gain 回归，或将分解公式降级为纯 illustration 并删除 'consistent with the observed data' 验证措辞。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R24-N2\"\n    summary: \"Gating protocol 循环性 + 验证不足：within-instance ρ(LP,F1) 需 gold labels，dev probe 仅 50 instances / 3 dataset / threshold 0.3 来源不明\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识 critical。(a) within-instance ρ 需 gold labels，仅为回顾性诊断；(b) dev probe 50 instances 无 bootstrap SE；(c) 0.3 threshold 来源未说明；(d) 仅 3 dataset with 'large inter-dataset margins'，不清楚 margins 窄时是否可靠；(e) gating 在 LP selection 与 construction 间选择但无 'neither'(greedy) option——CoNLL construction 有害时 gating 仍路由到 construction。\"\n    action_items:\n      - round: 24\n        action: \"报告 dev 50-instance adjusted ρ 的 bootstrap CI。讨论 threshold 0.3 敏感性（0.2-0.4 range）。Gating 增加 'greedy fallback' option（当 construction 也无效时）。明确 gating 为 preliminary protocol（非 validated），降低 narrative 权重。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R24-W1\"\n    summary: \"'Resolving' framing 过强：entity construction 仅恢复 8-11% oracle headroom (~1pp)\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识。SciERC 1.02/13.0≈8%, Few-NERD 1.40/12.4≈11%。Title 'Resolving' 和 Contribution 3 'principled resolution' 暗示问题已有效解决，但 90% oracle gap 仍在。\"\n    action_items:\n      - round: 24\n        action: \"Title: 'Resolving' → 'Addressing'/'Mitigating'。Contribution 3: 'principled resolution' → 'partial mitigation motivated by the diagnostic'。正文加 oracle recovery percentage。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R24-W2\"\n    summary: \"SciERC selection 结果 underpowered (n=529, MDE≈1.5pp) 但未明确标注\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"论文说 'Few-NERD provides the definitive test' 但 SciERC 仍是 primary test bed。SciERC LP σ=0.48pp ≈ effect size，方向 seed-dependent。建议正文更明确标注 SciERC selection 为 'underpowered/inconclusive'。\"\n    action_items:\n      - round: 24\n        action: \"在 SciERC selection 结果处明确标注 'underpowered to detect effects below 1.5pp'。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R24-W3\"\n    summary: \"Related Work 缺少与 Taubenfeld (CISC) / Kang (Self-Certainty) 的技术差异对比\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"两者在 Related Work 仅一句带过 ('reward-free selectors')，未讨论为何不适用于 structured prediction。Self-Certainty 在 Limitations 列为未测试但 RW 未解释为何不测。\"\n    action_items:\n      - round: 24\n        action: \"在 Related Work self-consistency paragraph 中增加 2-3 句，说明 CISC 和 Self-Certainty 依赖 answer-level equivalence grouping，在 entity-set partial overlap 场景下不直接适用。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R24-W4\"\n    summary: \"English-only + NER-heavy 泛化局限未在 Limitations 中讨论语言覆盖\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"4 NER + 1 RE，全部英文。Limitations 讨论了 scale 但未提及语言。\"\n    action_items:\n      - round: 24\n        action: \"Limitations 增加 1 句语言覆盖限制。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R24-W5\"\n    summary: \"Self-Certainty (Kang 2025) 和 P(True) (Kadavath 2022) 未测试，削弱 per-sample signal 结论的完整性\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"论文结论非 'no per-sample signal works in general'，而是 'our evaluated signals don't work'。但 Self-Certainty 是明确设计用于 BoN 的 per-sample signal，缺失是覆盖 gap。Verbalized confidence + hidden probes 已测但同样失败。\"\n\n  - id: \"R24-W6\"\n    summary: \"Appendix D 'as a reviewer correctly noted' 暗示审稿历史，首次提交应删除\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1]\n        note: \"如果这是首次投稿，此措辞泄露了内部审稿过程。\"\n    action_items:\n      - round: 24\n        action: \"删除 'as a reviewer correctly noted'，改为直接陈述。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R24-I1\"\n    summary: \"Table 2 中 EM/VC 的 p 值标 '---' 应报告具体数值\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"EM/VC 低于 greedy，p=1.0 或类似值应明确报告而非用 ---。\"\n\n  - id: \"R24-I2\"\n    summary: \"F1 metric 术语不统一 (instance-level macro / span-level micro / per-sample)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1]\n        note: \"Table 2 caption 说 'macro F1' 但 §3.3 说 'per-instance macro-F1'。需统一。\"\n\n  - id: \"R24-I3\"\n    summary: \"8 个 orphan bib entries 待清理\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"在 .bib 中但未被 cite。应清理或 cite。\"\n\n  - id: \"R24-I4\"\n    summary: \"SJ 分母 max(|g_i|, |g_j|) 当两 sample 都不含某类型 entity 时为 0 的边界情况未讨论\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1]\n        note: \"E_∪=∅ 时 VC=0 已有 footnote，但 SJ 的分母边界情况未提及。\"\n\n  - id: \"R24-I5\"\n    summary: \"Abstract ρ up to 0.45 取自 CoNLL EM（最易数据集），易给读者过于乐观印象\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"SciERC 上最高仅 0.379。建议加注 dataset context 或报告 median。\""
  }
}
```

</details>

---


### Tool result

_source line 2502 · 2026-05-19T06:25:06.059482+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 25538}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2503 · 2026-05-19T06:26:58.942201+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 24\n\n**论文**: \"Strong Predictors, Weak Selectors: Diagnosing and Resolving Self-Consistency for Named Entity Recognition\"\n**Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May cycle)\n**Deadline**: 2026-05-25 (AoE)\n**Reviewer**: R1 (方法严谨性 + 实验设计) + R2 (新颖性 + 叙事 + 写作)\n**圆桌轮次**: 1 轮（关键问题达成共识，无重大未解决矛盾）\n\n---\n\n## Summary\n\n本文系统评估了 5 种置信度信号在 NER 任务上的质量估计 (QE) 和样本选择效果，使用 fine-tuned 4B-8B 模型在 4 个 NER benchmark 上进行实验。核心发现：所有信号可靠估计实例质量（ρ up to 0.45, AUROC up to 0.82），但 instance-level selection 失败——论文诊断出 instance degeneracy 和 LP compression 两个瓶颈，并提出 entity-level construction 作为部分缓解（+1.40pp Few-NERD, +1.02pp SciERC）。\n\n---\n\n## Strengths\n\n**S1. 统计严谨性在 NLP 论文中属上乘水平。** [共识] 贯穿 paired bootstrap tests, MDE 分析 (SciERC n=529 → MDE≈1.5pp), TOST 等价性检验, Bonferroni/BH 校正, 以及 multi-seed stability 报告。Post-hoc 分析（ε=0.05 → p_adj=0.14）主动标注为 exploratory。\n\n**S2. QE vs Selection 的概念区分是有效贡献。** [共识] Instance-level vs per-sample signal 分类法清晰且对 structured prediction 领域有指导意义。\n\n**S3. 实验覆盖异常全面。** [共识] 5 信号 × 4 NER 数据集（难度梯度：WNUT→SciERC→Few-NERD→CoNLL）× 2 模型家族 × 4B scale ablation × 温度/epoch/N/LoRA-rank 消融 × supervised 组合 × hidden state probes × DeBERTa verifier × verbalized confidence × free-form decoding × calibration baseline × OOD 分析。附录约 1571 行。\n\n**S4. 诚实的负结果呈现。** [共识] 坦率承认 supervised combinations、hidden state probes、DeBERTa verifier 均无法关闭 selection gap。清楚区分 exploratory 与 confirmatory findings。\n\n**S5. 写作质量良好，无 AI 写作痕迹。** [共识] 无 em-dash/en-dash 滥用，无黑名单词汇，术语定义完整，段落长度合理。\n\n**S6. 混淆变量控制充分。** [共识] Thinking token confound (Appendix J: 3-part analysis), epoch confound (Appendix S), SJ normalizer (Table 6: |Δρ|<0.01), FK independence (permutation test), length-LP correlation (正向，排除 length penalty confound) 均有对应分析。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1. [Critical] 分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 验证严重不足。** [R1 critical + R2 agree]\n- g(·) 被 \"assumed monotonically increasing\" 但无理论推导，无函数形式\n- 仅用 3 个 macro-level 数据点（SciERC, Few-NERD, CoNLL）验证 \"consistency\"——任何单调函数都能拟合 3 个点\n- Figure 3 中 23 个 configurations 的数据完全可做 predicted vs actual 的回归验证，但论文未做\n- **修改方向**: (a) 在 23 configurations 上做回归验证并报告 predicted-actual correlation；或 (b) 删除 \"consistent with the observed data\" 验证措辞，明确标注为 \"descriptive heuristic / illustration\"\n\n**W2. [Critical] Gating protocol 循环性 + 验证不足。** [R1 critical + R2 agree]\n- Within-instance ρ(LP, F1) 需 gold labels 才能计算，仅为回顾性诊断而非前瞻性预测器\n- Dev probe: 仅 50 held-out instances，bootstrap SE 未报告\n- Threshold 0.3 来源未说明，敏感性分析缺失\n- 仅 3 dataset 验证，inter-dataset margins 大（SciERC 0.167, CoNLL 0.065, Few-NERD 0.516），不清楚 margins 窄时是否可靠\n- Gating 在 LP selection 与 construction 间选择但无 \"greedy fallback\" option——CoNLL construction 有害 (-0.39pp) 时 gating 仍可能路由到 construction\n- **修改方向**: 报告 bootstrap CI、讨论 threshold 敏感性、增加 greedy fallback、明确 gating 为 preliminary protocol\n\n### Should-Fix（影响评分但不一票否决）\n\n**W3. [Warning] Entity construction 新颖性有限 + \"Resolving\" framing 过强。** [R2 critical → R1 agree on substance, disagree on severity]\n- 本质是 Florian et al. (2003) entity voting 从 multi-model ensemble 迁移到 single-model stochastic sampling + LP weighting\n- LP weighting vs uniform 增量仅 0.28pp (SciERC) 和 0.66pp (Few-NERD)\n- 实际恢复 oracle headroom 仅 8-11%（SciERC 1.02/13.0≈8%, Few-NERD 1.40/12.4≈11%）\n- Title \"Resolving\" 和 Contribution 3 \"principled resolution\" 暗示问题已有效解决\n- **R1 rebuttal**: 作为诊断的自然推论可接受，不应作为主要贡献；建议降级 narrative\n- **修改方向**: Title \"Resolving\" → \"Addressing\"/\"Mitigating\"；Contribution 3 降级为 \"diagnostic-motivated mitigation\"；正文加 oracle recovery percentage\n\n**W4. [Warning] Correlation-selection gap 概念：by-construction vs empirical 边界模糊。** [R2 critical → R1 partial rebut]\n- 4/5 信号的 selection 失败是信号定义的直接结果（by construction），非 empirical discovery\n- **R1 有效 rebuttal**: MBR consensus-proximity 确实给不同 sample 赋不同分数，其失败是 empirical finding；LP 失败和 degeneracy/compression 的机制识别不是同义反复\n- **Director 判断**: R1 的分析更有说服力——umbrella term 模糊了 by-construction 与 empirical 边界，但不等于整个概念无价值。降级为 warning\n- **修改方向**: 正文更清晰区分 definitional limitation（1 段 setup）与 empirical findings（LP failure, degeneracy-compression disentanglement 作为核心）\n\n**W5. [Warning] SciERC selection 结果 underpowered (n=529, MDE≈1.5pp, σ=0.48pp)。** [共识]\n- SciERC LP selection 3-seed mean +0.04±0.48pp，方向 seed-dependent\n- 论文说 \"Few-NERD provides the definitive test\" 但 SciERC 仍是 primary test bed\n- **修改方向**: 正文明确标注 SciERC selection 为 \"underpowered to detect effects below 1.5pp\"\n\n**W6. [Warning] \"Tuning-free\" threshold 声明不准确。** [共识]\n- θ=2/N 是观察所有数据集 sweep 后选择的 \"works reasonably well\" 值，非先验推导\n- **修改方向**: 改为 \"default heuristic threshold\"\n\n**W7. [Warning] Related Work 缺少与 Taubenfeld (CISC) / Kang (Self-Certainty) 的技术差异对比。** [共识]\n- 两者在 RW 仅一句带过 (\"reward-free selectors\")，未讨论为何不适用于 structured prediction\n- Self-Certainty 在 Limitations 列为未测试的 per-sample signal，但 RW 未解释为何不测\n- **修改方向**: RW 增加 2-3 句技术差异对比\n\n**W8. [Warning] English-only + NER-heavy 泛化局限未在 Limitations 中讨论语言覆盖。** [共识]\n\n**W9. [Warning] Appendix D \"as a reviewer correctly noted\" 暗示审稿历史，应删除。** [R1 raises, R2 agrees is minor]\n\n### Minor Issues\n\n- **M1**: Table 2 中 EM/VC 的 p 值标 \"---\" 应报告具体值\n- **M2**: F1 metric 术语不统一 (macro F1 / per-instance macro-F1)\n- **M3**: 8 个 orphan bib entries 待清理（Li et al. 2025, Muennighoff et al. 2025 等在 bib 但未 cite）\n- **M4**: SJ 分母 max(|g_i|,|g_j|)=0 的边界情况未讨论\n- **M5**: Abstract \"ρ up to 0.45\" 取自 CoNLL EM（最易数据集），SciERC 最高仅 0.379，易给读者过于乐观印象\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **实验覆盖和统计透明度是论文最大优势**——在 NLP empirical studies 中属顶尖水平\n2. **分解公式验证不足是核心方法论弱点**——3 data points, no regression on 23 configs\n3. **Gating protocol 需要更充分验证**——循环性、bootstrap CI、threshold 敏感性\n4. **Entity construction 新颖性有限**——直接迁移 + 小增量，narrative 需降调\n5. **\"Resolving\" framing 过强**——实际仅恢复 8-11% oracle headroom\n6. **负结果对领域有价值**——系统排除了多种 selection 方法的有效性\n7. **写作质量良好**——无 AI 痕迹，统计声明诚实\n\n## Reviewer Divergence [REBUT]\n\n1. **Correlation-selection gap 新颖性**: R2 认为整体 critical（by construction），R1 成功 rebut 指出 MBR conversion 失败和 LP regime 分析是真实 empirical contributions。**Director 采纳 R1 立场：降级为 warning，但需 narrative 重组。**\n\n2. **Scope 限制严重程度**: R2 认为 critical（fine-tuned + constrained decoding specific），R1 rebut 指出 scope 声明清晰且 NER free-form 数据显示 constrained decoding 非根本原因（Table 13 Panel B）。**Director 采纳 R1 立场：scope 声明已足够，fine-tuned + constrained 是主流 deployment paradigm。降级为 existing warning (W8 语言覆盖 + 已有 Limitations 覆盖)。**\n\n3. **Thinking token confound 严重程度**: R1 列为 warning，R2 rebut 认为 3-part analysis 有说服力。**Director 采纳 R2 立场：non-issue，已在 Appendix 充分处理。**\n\n---\n\n## Questions for Authors\n\nQ1. 分解公式能否在 23 configurations (Fig 3) 上做回归验证？Predicted vs actual gain 的 R² 或 Spearman ρ 是多少？\n\nQ2. Gating protocol 的 50 dev instances 是随机采样还是 stratified？Bootstrap 95% CI 是什么？Threshold 从 0.3 移到 0.2 或 0.4，routing 是否改变？\n\nQ3. Entity construction 的 precision-recall trade-off 数据？Construction 是 recall-driven，precision 变化如何？\n\nQ4. Degeneracy rises with capability (8B>4B) 是否因 convergence 差异？有无 matched-convergence scale 对比（如 8B 3-epoch vs 4B 5-epoch）？\n\nQ5. Cross-instance LP ρ (0.220 on Few-NERD) vs within-instance ρ (0.667) 的关系需要更明确解释——为何 cross-instance ρ 不能预测 selection 而 within-instance ρ 可以？\n\n---\n\n## Missing References\n\n- **LLM-Blender** (Jiang et al. 2023): output fusion pipeline 直接相关 [R1 agree, R2 agree]\n- **Taubenfeld/Kang 技术差异对比**: 非 missing citation 但 RW 对比不足 [共识]\n- **8 orphan bib entries**: 应 cite 或删除 [共识]\n\n---\n\n## External Review\n\n外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。\n\n---\n\n## Overall Assessment\n\n**Score: Borderline (3.25/5)**\n- R1: 3.5/5 (Borderline accept, 倾向 Findings)\n- R2: 3.0/5 (Borderline)\n- Director 综合: 3.25/5\n\n**置信度: 4/5**（两位 Reviewer 均熟悉相关领域，交叉后在关键问题上达成共识）\n\n**判断依据**:\n\n论文的**核心优势**在于实验覆盖和统计严谨性——这在 NLP 论文中极为罕见，值得肯定。QE vs selection 的概念区分、degeneracy/compression 的机制诊断、以及诚实的负结果对领域有真实价值。\n\n论文的**核心弱点**在于：(1) 分析框架的数学基础（分解公式 3 点验证、gating 循环性）不够扎实；(2) positive contribution 增量过小（entity construction ~1pp, 恢复 ~10% oracle headroom）且基于已知技术迁移；(3) \"Resolving\" framing 与实际增益不匹配。\n\n**建议**:\n- **Main Conference 接收面临挑战**: 核心新颖性（entity construction）增量不足以支撑 Main Conference 标准。如果能在分解公式上做 23-config 回归验证证明其 predictive power，或增加非 fine-tuned 设置的实验，竞争力会显著提升。\n- **Findings 接收可期**: 论文作为 systematic empirical study 有充分价值——诊断框架、全面的负结果、以及统计最佳实践均值得发表。\n- **修改优先级**: W1 (分解公式) > W2 (gating) > W3 (construction framing) > W4 (gap narrative) > W5-W9 (presentation)\n\n---\n\n## Detailed Comments (逐 Section)\n\n### Abstract\n- 信息密集但准确。\"ρ up to 0.45\" 取自 CoNLL EM，SciERC 最高仅 0.379——建议加注 dataset context。缺少 oracle recovery percentage，读者无法判断 construction 增益的实际意义。\n\n### Introduction\n- 叙事结构清晰：self-consistency → NER structural difference → QE/selection 区分 → gap 诊断 → construction。\n- MBR 差异化定位 (L16) 有效。\n- Contribution 3 \"principled resolution\" 需降调。\n\n### Related Work\n- 覆盖 4 个主题块，引用密度合理（70 citations）。\n- 缺少 Taubenfeld (CISC) / Kang (Self-Certainty) 的技术差异对比——需解释为何不适用于 structured prediction。\n\n### Method (Section 3)\n- 5 个信号数学定义严谨。SJ normalizer robustness (Table 6) 和 FK independence (permutation test) 是好的实践。\n- SJ 分母 E_∪=∅ 边界情况未讨论。\n- Instance-level vs per-sample 区分清晰且重要。\n\n### Experiments (Section 4)\n- 数据集选择策略性强（难度梯度 + 各有实验角色）。\n- QE 结果可信（structural > LP 在 SciERC 上显著，bootstrap CI 不含 0）。\n- Selection 结果：SciERC 无显著差异是可靠 negative result。Few-NERD LP +1.39pp (p<0.001, CI [+1.18, +1.53]) 是最强 positive result。\n- 分解公式验证不足（见 W1）。\n\n### Discussion (Section 5)\n- 压缩严重但信息密度高。Non-tied subset analysis 的 exploratory 标注正确。\n- Entity construction 作为 \"resolution\" 的 narrative 需降调。\n\n### Conclusion\n- 准确，未超出实证支持范围。Practitioner guidance 有价值。\n\n### Limitations\n- 异常全面。缺少语言覆盖讨论。\n\n### 格式\n- 正文 ≤8 页，`\\usepackage[review]{acl}`, `\\author{Anonymous}`，double-blind 合规。\n- Figure/Table 紧凑高效。\n- Responsible NLP Checklist 认真填写。",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 24\n\n**论文**: \"Strong Predictors, Weak Selectors: Diagnosing and Resolving Self-Consistency for Named Entity Recognition\"\n**Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May cycle)\n**Deadline**: 2026-05-25 (AoE)\n**Reviewer**: R1 (方法严谨性 + 实验设计) + R2 (新颖性 + 叙事 + 写作)\n**圆桌轮次**: 1 轮（关键问题达成共识，无重大未解决矛盾）\n\n---\n\n## Summary\n\n本文系统评估了 5 种置信度信号在 NER 任务上的质量估计 (QE) 和样本选择效果，使用 fine-tuned 4B-8B 模型在 4 个 NER benchmark 上进行实验。核心发现：所有信号可靠估计实例质量（ρ up to 0.45, AUROC up to 0.82），但 instance-level selection 失败——论文诊断出 instance degeneracy 和 LP compression 两个瓶颈，并提出 entity-level construction 作为部分缓解（+1.40pp Few-NERD, +1.02pp SciERC）。\n\n---\n\n## Strengths\n\n**S1. 统计严谨性在 NLP 论文中属上乘水平。** [共识] 贯穿 paired bootstrap tests, MDE 分析 (SciERC n=529 → MDE≈1.5pp), TOST 等价性检验, Bonferroni/BH 校正, 以及 multi-seed stability 报告。Post-hoc 分析（ε=0.05 → p_adj=0.14）主动标注为 exploratory。\n\n**S2. QE vs Selection 的概念区分是有效贡献。** [共识] Instance-level vs per-sample signal 分类法清晰且对 structured prediction 领域有指导意义。\n\n**S3. 实验覆盖异常全面。** [共识] 5 信号 × 4 NER 数据集（难度梯度：WNUT→SciERC→Few-NERD→CoNLL）× 2 模型家族 × 4B scale ablation × 温度/epoch/N/LoRA-rank 消融 × supervised 组合 × hidden state probes × DeBERTa verifier × verbalized confidence × free-form decoding × calibration baseline × OOD 分析。附录约 1571 行。\n\n**S4. 诚实的负结果呈现。** [共识] 坦率承认 supervised combinations、hidden state probes、DeBERTa verifier 均无法关闭 selection gap。清楚区分 exploratory 与 confirmatory findings。\n\n**S5. 写作质量良好，无 AI 写作痕迹。** [共识] 无 em-dash/en-dash 滥用，无黑名单词汇，术语定义完整，段落长度合理。\n\n**S6. 混淆变量控制充分。** [共识] Thinking token confound (Appendix J: 3-part analysis), epoch confound (Appendix S), SJ normalizer (Table 6: |Δρ|<0.01), FK independence (permutation test), length-LP correlation (正向，排除 length penalty confound) 均有对应分析。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1. [Critical] 分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 验证严重不足。** [R1 critical + R2 agree]\n- g(·) 被 \"assumed monotonically increasing\" 但无理论推导，无函数形式\n- 仅用 3 个 macro-level 数据点（SciERC, Few-NERD, CoNLL）验证 \"consistency\"——任何单调函数都能拟合 3 个点\n- Figure 3 中 23 个 configurations 的数据完全可做 predicted vs actual 的回归验证，但论文未做\n- **修改方向**: (a) 在 23 configurations 上做回归验证并报告 predicted-actual correlation；或 (b) 删除 \"consistent with the observed data\" 验证措辞，明确标注为 \"descriptive heuristic / illustration\"\n\n**W2. [Critical] Gating protocol 循环性 + 验证不足。** [R1 critical + R2 agree]\n- Within-instance ρ(LP, F1) 需 gold labels 才能计算，仅为回顾性诊断而非前瞻性预测器\n- Dev probe: 仅 50 held-out instances，bootstrap SE 未报告\n- Threshold 0.3 来源未说明，敏感性分析缺失\n- 仅 3 dataset 验证，inter-dataset margins 大（SciERC 0.167, CoNLL 0.065, Few-NERD 0.516），不清楚 margins 窄时是否可靠\n- Gating 在 LP selection 与 construction 间选择但无 \"greedy fallback\" option——CoNLL construction 有害 (-0.39pp) 时 gating 仍可能路由到 construction\n- **修改方向**: 报告 bootstrap CI、讨论 threshold 敏感性、增加 greedy fallback、明确 gating 为 preliminary protocol\n\n### Should-Fix（影响评分但不一票否决）\n\n**W3. [Warning] Entity construction 新颖性有限 + \"Resolving\" framing 过强。** [R2 critical → R1 agree on substance, disagree on severity]\n- 本质是 Florian et al. (2003) entity voting 从 multi-model ensemble 迁移到 single-model stochastic sampling + LP weighting\n- LP weighting vs uniform 增量仅 0.28pp (SciERC) 和 0.66pp (Few-NERD)\n- 实际恢复 oracle headroom 仅 8-11%（SciERC 1.02/13.0≈8%, Few-NERD 1.40/12.4≈11%）\n- Title \"Resolving\" 和 Contribution 3 \"principled resolution\" 暗示问题已有效解决\n- **R1 rebuttal**: 作为诊断的自然推论可接受，不应作为主要贡献；建议降级 narrative\n- **修改方向**: Title \"Resolving\" → \"Addressing\"/\"Mitigating\"；Contribution 3 降级为 \"diagnostic-motivated mitigation\"；正文加 oracle recovery percentage\n\n**W4. [Warning] Correlation-selection gap 概念：by-construction vs empirical 边界模糊。** [R2 critical → R1 partial rebut]\n- 4/5 信号的 selection 失败是信号定义的直接结果（by construction），非 empirical discovery\n- **R1 有效 rebuttal**: MBR consensus-proximity 确实给不同 sample 赋不同分数，其失败是 empirical finding；LP 失败和 degeneracy/compression 的机制识别不是同义反复\n- **Director 判断**: R1 的分析更有说服力——umbrella term 模糊了 by-construction 与 empirical 边界，但不等于整个概念无价值。降级为 warning\n- **修改方向**: 正文更清晰区分 definitional limitation（1 段 setup）与 empirical findings（LP failure, degeneracy-compression disentanglement 作为核心）\n\n**W5. [Warning] SciERC selection 结果 underpowered (n=529, MDE≈1.5pp, σ=0.48pp)。** [共识]\n- SciERC LP selection 3-seed mean +0.04±0.48pp，方向 seed-dependent\n- 论文说 \"Few-NERD provides the definitive test\" 但 SciERC 仍是 primary test bed\n- **修改方向**: 正文明确标注 SciERC selection 为 \"underpowered to detect effects below 1.5pp\"\n\n**W6. [Warning] \"Tuning-free\" threshold 声明不准确。** [共识]\n- θ=2/N 是观察所有数据集 sweep 后选择的 \"works reasonably well\" 值，非先验推导\n- **修改方向**: 改为 \"default heuristic threshold\"\n\n**W7. [Warning] Related Work 缺少与 Taubenfeld (CISC) / Kang (Self-Certainty) 的技术差异对比。** [共识]\n- 两者在 RW 仅一句带过 (\"reward-free selectors\")，未讨论为何不适用于 structured prediction\n- Self-Certainty 在 Limitations 列为未测试的 per-sample signal，但 RW 未解释为何不测\n- **修改方向**: RW 增加 2-3 句技术差异对比\n\n**W8. [Warning] English-only + NER-heavy 泛化局限未在 Limitations 中讨论语言覆盖。** [共识]\n\n**W9. [Warning] Appendix D \"as a reviewer correctly noted\" 暗示审稿历史，应删除。** [R1 raises, R2 agrees is minor]\n\n### Minor Issues\n\n- **M1**: Table 2 中 EM/VC 的 p 值标 \"---\" 应报告具体值\n- **M2**: F1 metric 术语不统一 (macro F1 / per-instance macro-F1)\n- **M3**: 8 个 orphan bib entries 待清理（Li et al. 2025, Muennighoff et al. 2025 等在 bib 但未 cite）\n- **M4**: SJ 分母 max(|g_i|,|g_j|)=0 的边界情况未讨论\n- **M5**: Abstract \"ρ up to 0.45\" 取自 CoNLL EM（最易数据集），SciERC 最高仅 0.379，易给读者过于乐观印象\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **实验覆盖和统计透明度是论文最大优势**——在 NLP empirical studies 中属顶尖水平\n2. **分解公式验证不足是核心方法论弱点**——3 data points, no regression on 23 configs\n3. **Gating protocol 需要更充分验证**——循环性、bootstrap CI、threshold 敏感性\n4. **Entity construction 新颖性有限**——直接迁移 + 小增量，narrative 需降调\n5. **\"Resolving\" framing 过强**——实际仅恢复 8-11% oracle headroom\n6. **负结果对领域有价值**——系统排除了多种 selection 方法的有效性\n7. **写作质量良好**——无 AI 痕迹，统计声明诚实\n\n## Reviewer Divergence [REBUT]\n\n1. **Correlation-selection gap 新颖性**: R2 认为整体 critical（by construction），R1 成功 rebut 指出 MBR conversion 失败和 LP regime 分析是真实 empirical contributions。**Director 采纳 R1 立场：降级为 warning，但需 narrative 重组。**\n\n2. **Scope 限制严重程度**: R2 认为 critical（fine-tuned + constrained decoding specific），R1 rebut 指出 scope 声明清晰且 NER free-form 数据显示 constrained decoding 非根本原因（Table 13 Panel B）。**Director 采纳 R1 立场：scope 声明已足够，fine-tuned + constrained 是主流 deployment paradigm。降级为 existing warning (W8 语言覆盖 + 已有 Limitations 覆盖)。**\n\n3. **Thinking token confound 严重程度**: R1 列为 warning，R2 rebut 认为 3-part analysis 有说服力。**Director 采纳 R2 立场：non-issue，已在 Appendix 充分处理。**\n\n---\n\n## Questions for Authors\n\nQ1. 分解公式能否在 23 configurations (Fig 3) 上做回归验证？Predicted vs actual gain 的 R² 或 Spearman ρ 是多少？\n\nQ2. Gating protocol 的 50 dev instances 是随机采样还是 stratified？Bootstrap 95% CI 是什么？Threshold 从 0.3 移到 0.2 或 0.4，routing 是否改变？\n\nQ3. Entity construction 的 precision-recall trade-off 数据？Construction 是 recall-driven，precision 变化如何？\n\nQ4. Degeneracy rises with capability (8B>4B) 是否因 convergence 差异？有无 matched-convergence scale 对比（如 8B 3-epoch vs 4B 5-epoch）？\n\nQ5. Cross-instance LP ρ (0.220 on Few-NERD) vs within-instance ρ (0.667) 的关系需要更明确解释——为何 cross-instance ρ 不能预测 selection 而 within-instance ρ 可以？\n\n---\n\n## Missing References\n\n- **LLM-Blender** (Jiang et al. 2023): output fusion pipeline 直接相关 [R1 agree, R2 agree]\n- **Taubenfeld/Kang 技术差异对比**: 非 missing citation 但 RW 对比不足 [共识]\n- **8 orphan bib entries**: 应 cite 或删除 [共识]\n\n---\n\n## External Review\n\n外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。\n\n---\n\n## Overall Assessment\n\n**Score: Borderline (3.25/5)**\n- R1: 3.5/5 (Borderline accept, 倾向 Findings)\n- R2: 3.0/5 (Borderline)\n- Director 综合: 3.25/5\n\n**置信度: 4/5**（两位 Reviewer 均熟悉相关领域，交叉后在关键问题上达成共识）\n\n**判断依据**:\n\n论文的**核心优势**在于实验覆盖和统计严谨性——这在 NLP 论文中极为罕见，值得肯定。QE vs selection 的概念区分、degeneracy/compression 的机制诊断、以及诚实的负结果对领域有真实价值。\n\n论文的**核心弱点**在于：(1) 分析框架的数学基础（分解公式 3 点验证、gating 循环性）不够扎实；(2) positive contribution 增量过小（entity construction ~1pp, 恢复 ~10% oracle headroom）且基于已知技术迁移；(3) \"Resolving\" framing 与实际增益不匹配。\n\n**建议**:\n- **Main Conference 接收面临挑战**: 核心新颖性（entity construction）增量不足以支撑 Main Conference 标准。如果能在分解公式上做 23-config 回归验证证明其 predictive power，或增加非 fine-tuned 设置的实验，竞争力会显著提升。\n- **Findings 接收可期**: 论文作为 systematic empirical study 有充分价值——诊断框架、全面的负结果、以及统计最佳实践均值得发表。\n- **修改优先级**: W1 (分解公式) > W2 (gating) > W3 (construction framing) > W4 (gap narrative) > W5-W9 (presentation)\n\n---\n\n## Detailed Comments (逐 Section)\n\n### Abstract\n- 信息密集但准确。\"ρ up to 0.45\" 取自 CoNLL EM，SciERC 最高仅 0.379——建议加注 dataset context。缺少 oracle recovery percentage，读者无法判断 construction 增益的实际意义。\n\n### Introduction\n- 叙事结构清晰：self-consistency → NER structural difference → QE/selection 区分 → gap 诊断 → construction。\n- MBR 差异化定位 (L16) 有效。\n- Contribution 3 \"principled resolution\" 需降调。\n\n### Related Work\n- 覆盖 4 个主题块，引用密度合理（70 citations）。\n- 缺少 Taubenfeld (CISC) / Kang (Self-Certainty) 的技术差异对比——需解释为何不适用于 structured prediction。\n\n### Method (Section 3)\n- 5 个信号数学定义严谨。SJ normalizer robustness (Table 6) 和 FK independence (permutation test) 是好的实践。\n- SJ 分母 E_∪=∅ 边界情况未讨论。\n- Instance-level vs per-sample 区分清晰且重要。\n\n### Experiments (Section 4)\n- 数据集选择策略性强（难度梯度 + 各有实验角色）。\n- QE 结果可信（structural > LP 在 SciERC 上显著，bootstrap CI 不含 0）。\n- Selection 结果：SciERC 无显著差异是可靠 negative result。Few-NERD LP +1.39pp (p<0.001, CI [+1.18, +1.53]) 是最强 positive result。\n- 分解公式验证不足（见 W1）。\n\n### Discussion (Section 5)\n- 压缩严重但信息密度高。Non-tied subset analysis 的 exploratory 标注正确。\n- Entity construction 作为 \"resolution\" 的 narrative 需降调。\n\n### Conclusion\n- 准确，未超出实证支持范围。Practitioner guidance 有价值。\n\n### Limitations\n- 异常全面。缺少语言覆盖讨论。\n\n### 格式\n- 正文 ≤8 页，`\\usepackage[review]{acl}`, `\\author{Anonymous}`，double-blind 合规。\n- Figure/Table 紧凑高效。\n- Responsible NLP Checklist 认真填写。",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 2504 · 2026-05-19T06:27:03.223896+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4281
}
```

</details>

---


### Assistant

_source line 2505 · 2026-05-19T06:28:33.834445+00:00_

Round 24 审稿流程已全部完成。

- 审稿报告已通过 `submit_review_report_to_research_director` 投递（总评 3.25/5，Borderline）
- Issue Tracker (`review_issues.yaml`) 已同步更新，含 R24 全部新发现（2 critical、7 warnings、5 minor）
- 内部圆桌共识已达成，无未解决分歧

等待 Research Director 下一步指令。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 192

## Round 192

2 recorded events


### User

_source line 2506 · 2026-05-19T06:28:35.348161+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。主要分歧在 3 点：

1. **N1 (correlation-selection gap 新颖性)**: R2 认为整体新颖性存疑，我认为 by-construction 部分确实不算 discovery，但 MBR conversion 失败的实证验证、LP compression/degeneracy 的因果分离（温度消融 Table 16、epoch 消融 Table 22）有实质贡献，应降为 warning。
2. **N3 (scope 限制)**: R2 列为 critical，我认为论文的 scope declaration 已足够清晰，且 fine-tuned + constrained decoding 是 production NER 主流范式，应降为 warning。
3. **Q3 (constrained decoding 是否是根本原因)**: NER free-form 数据（Appendix L Table 13）直接反驳——LP compression 在两种 regime 下几乎相同。

与 R2 一致的主要判断：entity construction 新颖性有限 (N2)、分解公式验证不足 (W2)、gating protocol 验证不足 (W3)、Self-Certainty 缺失是实验覆盖 gap (Q4)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2507 · 2026-05-19T06:28:53.251350+00:00_

R1 的交叉回应已在之前纳入汇总。审稿流程全部完成：

- 圆桌会议已收敛（R1 3.5/5, R2 3.0/5, 综合 3.25/5）
- R1 提出的 3 点分歧已由 Director 裁决并写入最终报告（N1 和 N3 降为 warning，Q3 采纳 R1 立场）
- Issue tracker (`review_issues.yaml`) 已更新至 Round 24
- 审稿报告已通过 `submit_review_report_to_research_director` 投递

本轮审稿无待办事项。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 193

## Round 193

84 recorded events


### User

_source line 2508 · 2026-05-20T12:44:47.173738+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (Main Conference via ARR May)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2509 · 2026-05-20T12:44:53.480851+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2510 · 2026-05-20T12:44:53.582597+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2511 · 2026-05-20T12:44:59.802746+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2512 · 2026-05-20T12:44:59.853298+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2513 · 2026-05-20T12:45:02.792411+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2514 · 2026-05-20T12:45:02.854930+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 62
}
```

</details>

---


### Tool call

_source line 2515 · 2026-05-20T12:45:07.163386+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 2516 · 2026-05-20T12:45:07.414671+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2517 · 2026-05-20T12:45:14.891446+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 2518 · 2026-05-20T12:45:15.042317+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2519 · 2026-05-20T12:45:21.014225+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 2520 · 2026-05-20T12:45:22.318621+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (187 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_b1_scd_threshold_ablation | Construction threshold sweep for SCD pseudo-label generation on FewNERD: θ∈{1/N, 2/N, 3/N, 0.5}. Higher θ = more conservative pseudo-labels (higher precision, lower recall). Optimal θ balances pseudo-label quality vs quantity for SCD training effectiveness. | — | — | — |\n| exp_b1_scd_fewnerd_curriculum_q | Q variant SCD with curriculum ordering: use B2 entity verifier confidence to stratify pseudo-labels (conf>0.8→Round1, 0.5-0.8→Round2, conf<0.5→discard). Curriculum by verifier confidence improves SCD convergence and final greedy F1 vs standard flat SCD on FewNERD. | — | — | — |\n| exp_b1_scd_fewnerd_standard | Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs. | — | — | — |\n\n## 待处理\n- exp_b3_prompted_diversity: Structurally diverse prompt templates (role framing, output format variants, few-shot exemplar diversity) increase in
…[truncated 1741 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1304
}
```

</details>

---


### Tool call

_source line 2521 · 2026-05-20T12:45:22.469493+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2522 · 2026-05-20T12:45:23.222317+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	
24	\graphicspath{{figures/}}
25	
26	\title{Strong Predictors, Weak Selectors:\\ Addressing the Correlation-Selection Gap in Self-Consistency for Named Entity Recognition}
27	
28	\author{Anonymous}
29	
30	\begin{document}
31	\maketitle
32	
33	\input{sections/abstract}
34	\input{sections/introduction}
35	\input{sections/background}
36	\input{sections/diagnostic}
37	\input{sections/single_signal}
38	\input{sections/adaptive}
39	\input{sections/theory}
40	\input{sections/experiments_main}
41	\input{sections/discussion}
42	\input{sections/conclusion}
43	
44	\section*{Limitations}
45	\input{sections/limitations}
46	
47	\section*{Ethics Statement}
48	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
49	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
50	No new human data was collected or annotated for this study.
51	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
52	Code and data will be released upon acceptance at [anonymized URL].
53	
54	\section*{Responsible NLP Research Checklist}
55	\input{sections/checklist}
56	
57	\bibliography{references}
58	
59	\appendix
60	\input{sections/appendix}
61	
62
…[truncated 19 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 752
}
```

</details>

---


### Tool call

_source line 2523 · 2026-05-20T12:45:23.272891+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2524 · 2026-05-20T12:45:24.278343+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if paper PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2525 · 2026-05-20T12:45:24.429306+00:00_

-rw-r--r-- 1 ubuntu ubuntu 908772 May 20 12:44 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool result

_source line 2526 · 2026-05-20T12:45:29.697801+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"}]

Based on the web search results, I f
…[truncated 1547 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 6424
}
```

</details>

---


### Tool call

_source line 2527 · 2026-05-20T12:45:33.348160+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"
  }
}
```

</details>

---


### Tool call

_source line 2528 · 2026-05-20T12:45:33.800101+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR commitment"
  }
}
```

</details>

---


### Tool call

_source line 2529 · 2026-05-20T12:45:34.352562+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR May 2026 submission deadline aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR May 2026 submission deadline aclrollingreview.org"
  }
}
```

</details>

---


### Tool result

_source line 2530 · 2026-05-20T12:45:38.220171+00:00_

Web search results for query: "ARR May 2026 submission deadline aclrollingreview.org"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, I found information about ARR submission deadlines. However, the results show that the submission deadline is always the 15th of the month. Since you asked specifically about the May 2026 submission deadline, this would mean the deadline falls on **May 15, 2026**.

Additionally, all deadlines are at 11:59PM UTC-12:00 ("anywhere on Earth").

The search results also indicate that the new schedule with 10-week cycles started in May 2025, and this pattern would continue through May 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 3867
}
```

</details>

---


### Tool result

_source line 2531 · 2026-05-20T12:45:39.223907+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"}]

Based on the search results, here's the information about EMNLP 2026's call for papers submission deadline and ARR commitment:

## Key Deadlines

The ARR submission deadline for lo
…[truncated 909 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5423
}
```

</details>

---


### Tool result

_source line 2532 · 2026-05-20T12:45:39.776286+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.02279v1"}]

Based on the search results, here are the key ACL Rolling Review 2026 submission guidelines regarding page limits and formatting requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

## Formatting Requirements

Paper submissions 
…[truncated 1209 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 6428
}
```

</details>

---


### Tool call

_source line 2533 · 2026-05-20T12:45:44.643893+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org calls main conference papers submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org calls main conference papers submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 2534 · 2026-05-20T12:45:44.995706+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool call

_source line 2535 · 2026-05-20T12:45:45.949544+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_REVIEW_ISSUES_FILE\"",
  "description": "Check for existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_REVIEW_ISSUES_FILE\"",
    "description": "Check for existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2536 · 2026-05-20T12:45:53.449466+00:00_

Web search results for query: "site:2026.emnlp.org calls main conference papers submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"}]

I found the EMNLP 2026 Call for Main Conference Papers. Based on the search results, here are the key submission guidelines:

**Submission Process:**
Papers must be submitted through the ARR (Acknowledgment Review Report) Call for Papers, with submissions required by the ARR 2026 May cycle at the latest.

**Conference Commitment:**
Papers that have received reviews and a meta-review from ARR (whether from the ARR 2026 May cycle or an earlier ARR cycle) may be committed to EMNLP via the commitment link.

**New ARR 2026 May Policy:**
Authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026—ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

**Reviewer Obligations:**
All authors are expected to sign up to review, or serve as an Area Chair or Senior Area Chair, with assignments subsequently based on qualifications.

For more detailed guidelines, you can visit the official page at https://2026.emnlp.org/calls/main_conference_papers/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 8805
}
```

</details>

---


### Tool result

_source line 2537 · 2026-05-20T12:45:53.450395+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 193\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 10901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 8454
}
```

</details>

---


### Tool result

_source line 2538 · 2026-05-20T12:45:53.562885+00:00_

issues:
  # ===== 历史 resolved issues（保留记录）=====
  - id: "R1-W1"
    summary: "Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。"
    resolution_round: 19

  - id: "R1-W2"
    summary: "\"Two jointly necessary conditions\" 因果性表述过强"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 21
    resolution: "全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。"
    resolution_round: 21

  - id: "R2-N1"
    summary: "Contribution 1 'methodological premise' 是定义推论"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。"
    resolution_round: 19

  - id: "R2-N2"
    summary: "与 MBR 文献差异化定位不够锐利"
    category: framing
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。"
    resolution_round: 19

  - id: "R2-N4"
    summary: "模型规模 3B-8B，70B+ 未知"
    category: experiment
    severity: info
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。"
    resolution_round: 19

  - id: "R1-W3"
    summary: "2-seed 统计效力不足"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。"
    resolution_round: 19

  - id: "R1-W4"
    summary: "Per-entity-type non-independence"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: 
…[truncated 21264 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 7613
}
```

</details>

---


### Tool call

_source line 2539 · 2026-05-20T12:45:59.538721+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2540 · 2026-05-20T12:46:00.924980+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1386
}
```

</details>

---


### Tool call

_source line 2541 · 2026-05-20T12:46:01.477647+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | grep -A 10 \"external_review\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | grep -A 10 \"external_review\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2542 · 2026-05-20T12:46:02.280899+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 2543 · 2026-05-20T12:46:02.381743+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/",
  "description": "List paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/",
    "description": "List paper sections"
  }
}
```

</details>

---


### Tool result

_source line 2544 · 2026-05-20T12:46:02.432440+00:00_

abstract.tex
adaptive.tex
appendix.tex
background.tex
checklist.tex
conclusion.tex
diagnostic.tex
discussion.tex
experiments.tex
experiments_main.tex
introduction.tex
limitations.tex
method.tex
related_work.tex
single_signal.tex
theoretical.tex
theory.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2545 · 2026-05-20T12:46:05.649311+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config header"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config header"
  }
}
```

</details>

---


### Tool result

_source line 2546 · 2026-05-20T12:46:05.750473+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2547 · 2026-05-20T12:46:08.661195+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 2548 · 2026-05-20T12:46:08.762215+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2549 · 2026-05-20T12:46:12.876503+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 3 -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -10",
  "description": "Find config files in workspace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 3 -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -10",
    "description": "Find config files in workspace"
  }
}
```

</details>

---


### Tool result

_source line 2550 · 2026-05-20T12:46:13.027524+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2551 · 2026-05-20T12:46:18.394960+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
  "description": "Find yaml files in workspace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
    "description": "Find yaml files in workspace"
  }
}
```

</details>

---


### Tool result

_source line 2552 · 2026-05-20T12:46:18.495789+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/pending_approval_notifications.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2553 · 2026-05-20T12:46:21.606991+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/ 2>/dev/null | head -10",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/ 2>/dev/null | head -10",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 2554 · 2026-05-20T12:46:22.058822+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2555 · 2026-05-20T12:46:22.211308+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/workspace.yaml 2>/dev/null | grep -A 20 \"struct_self_consist\"",
  "description": "Check workspace config for project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/workspace.yaml 2>/dev/null | grep -A 20 \"struct_self_consist\"",
    "description": "Check workspace config for project"
  }
}
```

</details>

---


### Tool result

_source line 2556 · 2026-05-20T12:46:22.261952+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2557 · 2026-05-20T12:46:26.226167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2558 · 2026-05-20T12:46:27.180098+00:00_

1	\begin{abstract}
2	Test-time compute scaling---repeated sampling with selection or aggregation---yields large gains on discrete-answer reasoning and code generation, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where standard aggregation mechanisms break down.
3	We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks across fine-tuned 4B\textendash 8B and zero-shot 72B models.
4	All signals achieve reliable QE ($\rho$ up to 0.45 on CoNLL-2003, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
5	For instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \textbf{correlation-selection gap}).
6	We diagnose three structural failure modes---instance degeneracy, limited oracle headroom, and LP compression---that persist at 72B zero-shot scale, providing the first systematic characterization of when test-time scaling succeeds or fails for structured prediction.
7	The diagnostic motivates entity-level \textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC under fine-tuning (multi-seed mean, $p{<}0.005$). Construction and LP selection are complementary, governed by LP-quality alignment; a degeneracy decomposition confirms that SC gain vanishes when degeneracy exceeds 70\%.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 2559 · 2026-05-20T12:46:27.180615+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2560 · 2026-05-20T12:46:27.682960+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling has emerged as a complement to model scaling \cite{snell2025scaling}: repeated sampling with majority voting \citep{wang2023selfconsistency}, best-of-$N$ with learned verifiers \cite{cobbe2021verifiers, brown2024monkeys}, and extended chain-of-thought \cite{muennighoff2025s1} yield large gains on reasoning and code generation, but the evidence concentrates on tasks with discrete answers or execution-based verification.
4	Named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	This challenge generalizes to any \textit{set-valued} structured prediction task where outputs admit partial but not exact overlap.
6	
7	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
8	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
9	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we provide the first systematic empirical characterization of \textit{when and why} test-time scaling via LP-based selection succeeds or fails for structured prediction, diagnosing degeneracy and compression as the two blocking mechanisms.
10	
11	A key distinction structures our analysis: four of five signals (Soft Jaccard, voting confidence, Fleiss' $\kappa$, exact match) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	All signals achieve reliable quality estimation ($\rho$ up to 
…[truncated 3540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2561 · 2026-05-20T12:46:27.733732+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 2562 · 2026-05-20T12:46:27.984882+00:00_

1	\section{Background \& Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling.}
4	Test-time compute scaling encompasses three families: (a) extended chain-of-thought reasoning \cite{muennighoff2025s1}, (b) repeated sampling with majority voting (self-consistency; \citealp{wang2023selfconsistency}) and its extensions to free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}, and (c) best-of-$N$ selection via compute-optimal allocation \cite{snell2025scaling, brown2024monkeys}.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} and adaptive gating variants \cite{aggarwal2023adaptive, wang2025make, feng2025optimal, kim2026reasc} reduce inference cost; \citet{chen2025twofailures} diagnose failure modes.
6	All target discrete-answer reasoning; structured prediction requires different aggregation mechanisms because degeneracy operates at the entity-set level.
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation alone does not ensure selection gains, diagnosing degeneracy and compression as blocking mechanisms.
10	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\S\ref{sec:robustness_main}).
11	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
12	Ensemble approaches aggregate predictions from multiple models or prompts \cite{florian2003named, xiao2025el4ner}; \citet{xie2023zeroshot} propose two-stage entity voting for zero-shot NER, the closest prior work to our entity-level construction.
13	LLM-Blender \cite{jiang2023llmblender} fuses outputs from multiple LLMs via pairwise ranking, whereas our single-model stochastic sampling derives di
…[truncated 2774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2563 · 2026-05-20T12:46:27.985309+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
  }
}
```

</details>

---


### Tool result

_source line 2564 · 2026-05-20T12:46:28.035805+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
8	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
9	When LP fails---as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling})---no alternative per-sample signal exists.
10	
11	\subsection{Confidence Signals}\label{sec:signals}
12	
13	Entity matching uses exact span and type match.
14	We evaluate four \textit{consistency signals}---\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK])---and log-probability [LP] as the sole \textit{model-internal}, per-sample signal.
15	
16	\paragraph{Log-probability (per-sample).}
17	$c_{\text{lp}}(y_i) = |y_i|^{-1} \sum_{j} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)$.
18	
19	\paragraph{Soft Jaccard (structural, instance-level).}
20	For samples $y_i, y_j$, we group by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU):
21	\begin{equation}\label{eq:sj}
22	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
23	\end{equation}
24	Instance-level QE averages over all pairs: $c_{\text{sj}}(x) = \binom{N}{2}^{-1} \sum_{i<j} \text{SJ}(y_i, y_
…[truncated 1482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2565 · 2026-05-20T12:46:36.933646+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---


### Tool result

_source line 2566 · 2026-05-20T12:46:36.984300+00:00_

1	\section{Why Single-Signal Selection Fails}\label{sec:selection_gap}
2	
3	Four of five signals assign identical scores to all candidates from the same input by construction (\S\ref{sec:formulation}); they estimate quality across instances but cannot rank candidates within an instance.
4	LP selection effectiveness depends on LP-quality alignment rather than degeneracy alone.
5	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
6	
7	\begin{table}[t]
8	\centering
9	\small
10	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
11	\label{tab:selection}
12	\begin{tabular}{lcc}
13	\toprule
14	Method & NER F1 & $p$ \\
15	\midrule
16	Oracle & $0.775 \pm 0.001$ & --- \\
17	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
18	\midrule
19	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
20	SJ           & $0.646 \pm 0.002$ & .67 \\
21	FK           & $0.646 \pm 0.001$ & .79 \\
22	EM           & $0.637 \pm 0.001$ & n/a$^\dagger$ \\
23	VC           & $0.623 \pm 0.004$ & n/a$^\dagger$ \\
24	\midrule
25	Random       & $0.610 \pm 0.003$ & --- \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	\begin{figure}[t]
31	\centering
32	\includegraphics[width=\columnwidth]{fig_selection_gap}
33	\caption{Correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: QE $\rho$; line: $\Delta$F1 vs.\ greedy (3-seed mean). Despite $\rho$ up to 0.38, no signal outperforms greedy ($p{>}0.05$). Dashed green: oracle ($+13.0$\,pp); dotted gray: random.}
34	\label{fig:selection_gap}
35	\end{figure}
36	
37	Despite $\rho$ up to 0.38, no signal outperforms greedy on SciERC (Table~\ref{tab:selection}; Figure~\ref{fig:selection_gap}); the oracle reveals 13.0\,pp headroom, b
…[truncated 1065 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2567 · 2026-05-20T12:46:37.385935+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
  }
}
```

</details>

---


### Tool result

_source line 2568 · 2026-05-20T12:46:38.337931+00:00_

1	\section{Adaptive Methods}\label{sec:adaptive}
2	
3	Since instance-level selection fails (\S\ref{sec:selection_gap}), we present approaches that extract value from multi-sample generation beyond single-signal sample ranking.
4	
5	\subsection{Cross-Model Self-Consistency}\label{sec:cross_model}
6	
7	Diversity from stochastic sampling within a single model is limited by architecture-specific degeneracy (\S\ref{sec:selection_gap}).
8	Mixing samples from architecturally distinct models---which produce complementary error patterns---can partially bypass this bottleneck.
9	
10	In preliminary experiments combining 4 samples each from Qwen3-8B and LLaMA-3.1-8B (both fine-tuned on SciERC), LP-weighted entity construction yields $+0.42$\,pp over pure LLaMA sampling ($p{<}0.001$, 95\% CI $[0.27, 0.58]$; $N{=}8$ total), suggesting cross-architecture diversity can partially compensate for within-model degeneracy.
11	
12	\subsection{Trained Verifiers: High Discrimination, Low Transfer}\label{sec:verifier}
13	
14	A LightGBM entity-level classifier (5 features: agreement count, LP, VC, SJ, FK) achieves AUC${=}0.923{\pm}0.002$ under out-of-fold evaluation, confirming that entity correctness is learnable from the available signals.
15	Yet this discrimination translates poorly to F1: OOF construction yields only $+0.30$\,pp overall, with per-dataset gains of $+1.28$\,pp on SciERC, $+0.55$\,pp on CoNLL, and $+0.02$\,pp on Few-NERD.
16	The near-zero Few-NERD gain despite AUC${>}0.92$ reveals that frequency-based threshold construction (\S\ref{sec:prescriptive}) already captures most of the verifier's signal; SciERC---with low degeneracy and diverse entity-level errors---is the exception where learned discrimination adds value beyond majority vote.
17	Cross-dataset transfer remains negative (B2-v2: $-0.76$\,pp; B2-v3: $-1.02$\,pp on Few-NERD; Appendix~\ref{app:verifier_transfer}), confirming dataset-specific feature mappings.
18	Even a trained discriminator with near-perfect entity cla
…[truncated 921 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 951
}
```

</details>

---


### Tool call

_source line 2569 · 2026-05-20T12:46:38.338311+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 2570 · 2026-05-20T12:46:38.589387+00:00_

1	\section{Theory \& Scaling Law}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Entity-level construction (\S\ref{sec:prescriptive}) is a special case of minimum Bayes risk (MBR) decoding \cite{kumar2004minimum, eikema2020map}, extended from candidate selection ($\arg\max_{y \in \{y_1,\ldots,y_N\}}$) to construction over all subsets of $E_\cup{=}\bigcup_i y_i$.
6	
7	\begin{proposition}[Entity construction as MBR for balanced set-overlap]\label{prop:construction_mbr}
8	Under entity-wise independence with utility $u(\hat{y}, y') = |\hat{y} \cap y'| - \alpha|\hat{y} \setminus y'|$ ($\alpha \geq 1$), the MBR-optimal constructed set is
9	\begin{equation}\label{eq:mbr_construction}
10	\hat{y}_{\textup{MBR}} \!=\! \bigl\{e \!{\in}\! E_\cup \!:\! \hat{p}(e) \!>\! \tfrac{\alpha}{\alpha{+}1}\bigr\},\; \hat{p}(e) \!=\! \tfrac{1}{N} \textstyle\sum\nolimits_{i} \mathbf{1}[e \!{\in}\! y_i]
11	\end{equation}
12	The special case $\alpha{=}1$ yields $\hat{p}(e) > \tfrac{1}{2}$, the majority-vote threshold used throughout (proof in Appendix~\ref{app:mbr_proof}).
13	\end{proposition}
14	
15	\noindent\textbf{Remark.}
16	Set-level F1 is non-linear and admits no closed-form threshold rule \cite{dembczynski2011exact}. We use balanced linear utility ($\alpha{=}1$ throughout); balanced set-overlap and F1 induce similar optimal thresholds for typical NER output sizes ($|E_\cup| \leq 30$).
17	
18	Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$.
19	Weighted MBR improves when $w_i$ correlates with $u(y_i, y^*)$ within instances; when this correlation is weak (LP on SciERC: $\rho{\approx}0.2$; few-shot: \S\ref{sec:scaling}), weighting degrades (\S\ref{sec:prescriptive}).
20	
21	\subsection{Scaling Behavior}\label{sec:scaling}
22	
23	We test whether the gap persists across scales and model families using Qwen2.5 (7B fine-tuned, 72B zero-shot and few-shot) a
…[truncated 4189 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2571 · 2026-05-20T12:46:39.041218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2572 · 2026-05-20T12:46:39.041737+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	\subsection{Experimental Setup}\label{sec:setup}
4	
5	\paragraph{Datasets.}
6	We evaluate on four English NER benchmarks spanning a difficulty gradient.
7	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
8	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
9	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
10	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary.
11	
12	\paragraph{Models and sampling.}
13	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
14	$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N{=}16$ for scaling (Appendix~\ref{app:n_scaling}).
15	
16	%% ============================================================
17	\subsection{Quality Estimation Results}\label{sec:qe_results}
18	
19	\begin{table*}[t]
20	\centering
21	\small
22	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \textbf{bold}. RE in Appendix~\ref{app:re_extension}; $N{=}16$ in Table~\ref{tab:robustness}.}
23	\label{tab:quality_estimation}
24	\begin{tabular}{ll cc cc cc}
25	\toprule
26	& & \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
27	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}

…[truncated 7989 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2573 · 2026-05-20T12:46:43.055055+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2574 · 2026-05-20T12:46:44.008346+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	Structured IE exhibits oracle scaling comparable to reasoning ($c{\approx}0.5$; \S\ref{sec:scaling}), but aggregation cannot close the gap: degeneracy (17.8--67.9\%), limited headroom, and LP-quality alignment ($\rho$ 0.043--0.667) constrain it.
4	Temperature disentangles these at $T{=}1.2$ (degeneracy 14.9\%, LP $\rho{=}0.225$; Table~\ref{tab:t_degeneracy}).
5	
6	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
7	Entity-level construction bypasses both failure mechanisms, with gains positive when degeneracy ${<}22$\% and absent when ${>}31$\% (all $p{<}0.01$; Appendix~\ref{app:epoch_confound}). Under 72B few-shot, construction fails yet QE remains effective (SJ $\rho$ 0.29--0.44; Appendix~\ref{app:fs_error}).
8	Alternative strategies (DALS, MBR, DGS) and supervised mixtures fail to beat greedy (Appendix~\ref{app:dals}, \ref{app:supervised_combination}, \ref{app:when_selection_works}).
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 2575 · 2026-05-20T12:46:44.009078+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2576 · 2026-05-20T12:46:44.462289+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	Structured IE exhibits oracle scaling comparable to reasoning ($c{\approx}0.5$) but aggregation fails: a degeneracy decomposition ($\theta_{\text{crit}}{=}0.70$; \S\ref{sec:theory}) formalizes when SC becomes futile.
4	Entity-level construction partially closes the gap ($+1.40$\,pp Few-NERD, $+1.02$\,pp SciERC); a trained verifier achieves AUC${=}0.92$ but yields only $+0.30$\,pp via OOF construction, with negative cross-dataset transfer---content-aware methods \cite{cobbe2021verifiers} may bridge this.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 2577 · 2026-05-20T12:46:44.462621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2578 · 2026-05-20T12:46:44.864414+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	All experiments use English-language datasets; cross-lingual generalization remains untested.
3	Entity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\% F1${=}0$), this precondition fails and construction cannot improve over greedy.
4	We cover 4B\textendash 8B fine-tuned and 72B zero-shot; the gap persists at 72B but behavior with closed-source APIs or 72B fine-tuning is untested.
5	The 72B zero-shot comparison simultaneously varies model family (Qwen3$\to$Qwen2.5), training regime (fine-tuned$\to$zero-shot), and quantization (FP16$\to$AWQ 4-bit); these factors cannot be fully disentangled.
6	Our supervised approaches (DeBERTa verifier, hidden state probes, MLP/RF on signal combinations) all fail to close the oracle gap; whether content-aware verifiers with access to task-specific structure could succeed remains open.
7	
8	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
9	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
10	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
11	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
12	We tested verbalized confidence \cite{lin2022teaching, tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_conf
…[truncated 2344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2579 · 2026-05-20T12:46:44.914988+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2580 · 2026-05-20T12:46:44.965888+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $
…[truncated 13210 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2581 · 2026-05-20T12:47:04.398013+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom PyPDF2 import PdfReader\nr = PdfReader('/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf')\nprint(f'Total pages: {len(r.pages)}')\n\" 2>/dev/null || python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || echo \"Cannot determine page count\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom PyPDF2 import PdfReader\nr = PdfReader('/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf')\nprint(f'Total pages: {len(r.pages)}')\n\" 2>/dev/null || python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || echo \"Cannot determine page count\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 2582 · 2026-05-20T12:47:04.749527+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Wed May 20 12:44:20 2026 UTC
ModDate:         Wed May 20 12:44:20 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           38
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       908772 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2583 · 2026-05-20T12:47:04.800099+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 2584 · 2026-05-20T12:47:04.801548+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{vijayakumar2018diverse,
4	  title = {Diverse Beam Search for Improved Description of Complex Scenes},
5	  author = {Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and Sun, Qing and Lee, Stefan and Crandall, David J. and Batra, Dhruv},
6	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
7	  year = {2018},
8	  url = {https://arxiv.org/abs/1610.02424}
9	}
10	
11	@inproceedings{shi2022mbr,
12	  title = {Natural Language to Code Translation with Execution},
13	  author = {Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and Wang, Sida I.},
14	  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
15	  pages = {3533--3546},
16	  year = {2022},
17	  url = {https://arxiv.org/abs/2204.11454}
18	}
19	
20	@article{brown2024monkeys,
21	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
22	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
23	  journal = {arXiv preprint arXiv:2407.21787},
24	  year = {2024},
25	  url = {https://arxiv.org/abs/2407.21787}
26	}
27	
28	@inproceedings{chen2024usc,
29	  title = {Universal Self-Consistency for Large Language Model Generation},
30	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
31	  booktitle = {ICML 2024 Workshop on In-Context Learning},
32	  year = {2024},
33	  url = {https://arxiv.org/abs/2311.17311}
34	}
35	
36	@article{cobbe2021verifiers,
37	  title = {Training Verifiers to Solve Math Word Problems},
38	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Two
…[truncated 622 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 2585 · 2026-05-20T12:47:23.531273+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 2586 · 2026-05-20T12:47:44.693026+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21161
}
```

</details>

---


### Tool call

_source line 2587 · 2026-05-20T12:47:44.894246+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 Main Conference (Long Paper via ARR May 2026)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 ≤ 8 页，参考文献不限。Limitations 和 Ethics Statement 不计入页数\n- **模板**: ACL style template（double-blind）\n- **匿名规则**: double-blind\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n- Sections 目录: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/`\n\n## 审查侧重\n\n请重点审查以下方面：\n\n1. **方法论严谨性**：\n   - Diagnostic framework 的设计是否自洽？五种 confidence signals 的选择是否合理、覆盖是否充分？\n   - Soft Jaccard 公式（Eq. 1）和 MBR construction（Proposition 1）的数学正确性\n   - \"Correlation-selection gap\" 概念是否有 by-construction 的成分——即部分发现是否属于定义推论而非 empirical finding？\n   - Degeneracy decomposition (§5.3) 的 bound 是否有意义（bound 松紧度、实际 ratio 3-12%）\n\n2. **实验设计**：\n   - 数据集选择（4 个 NER + SciERC RE 探索性）是否充分？统计检验是否恰当？\n   - Sample size 和 seed 数量：Few-NERD 3-seed、SciERC 单 seed（σ=0.48pp）——统计效力是否足够？\n   - 23 configurations 的 cross-dataset 分析（ρ=0.052, p=0.81）——是否 underpowered？\n   - Entity construction 的 gain（+1.40pp FewNERD, +1.02pp SciERC）：效果大小、oracle recovery 比例、Holm-Bonferroni 校正后的显著性\n   - Gating protocol：dev set probe（50 instances），threshold τ=0.3 的选择依据和稳定性\n   - 72B zero-shot vs 8B fine-tuned 比较中同时变化了 model family + regime + quantization，能否得出有意义的结论？\n\n3. **统计分析**：\n   - Bootstrap CI 的使用是否恰当？paired bootstrap 的假设是否满足？\n   - p 值报告是否完整（特别是 Table 2 中的 n/a 标注）\n   - Multiple testing correction (Holm-Bonferroni k=57) 是否合理？校正后 SciERC p_adj=0.20 的解读\n   - 正文 vs appendix 的数字一致性\n\n请按以下格式输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 severity: critical/warning/info）\n4. Questions（需要作者回答的）\n5. Missing References（如有）\n6. Overall Assessment + 评分 + 置信度"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 Main Conference (Long Paper via ARR May 2026)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 ≤ 8 页，参考文献不限。Limitations 和 Ethics Statement 不计入页数\n- **模板**: ACL style template（double-blind）\n- **匿名规则**: double-blind\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n- Sections 目录: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/`\n\n## 审查侧重\n\n请重点审查以下方面：\n\n1. **方法论严谨性**：\n   - Diagnostic framework 的设计是否自洽？五种 confidence signals 的选择是否合理、覆盖是否充分？\n   - Soft Jaccard 公式（Eq. 1）和 MBR construction（Proposition 1）的数学正确性\n   - \"Correlation-selection gap\" 概念是否有 by-construction 的成分——即部分发现是否属于定义推论而非 empirical finding？\n   - Degeneracy decomposition (§5.3) 的 bound 是否有意义（bound 松紧度、实际 ratio 3-12%）\n\n2. **实验设计**：\n   - 数据集选择（4 个 NER + SciERC RE 探索性）是否充分？统计检验是否恰当？\n   - Sample size 和 seed 数量：Few-NERD 3-seed、SciERC 单 seed（σ=0.48pp）——统计效力是否足够？\n   - 23 configurations 的 cross-dataset 分析（ρ=0.052, p=0.81）——是否 underpowered？\n   - Entity construction 的 gain（+1.40pp FewNERD, +1.02pp SciERC）：效果大小、oracle recovery 比例、Holm-Bonferroni 校正后的显著性\n   - Gating protocol：dev set probe（50 instances），threshold τ=0.3 的选择依据和稳定性\n   - 72B zero-shot vs 8B fine-tuned 比较中同时变化了 model family + regime + quantization，能否得出有意义的结论？\n\n3. **统计分析**：\n   - Bootstrap CI 的使用是否恰当？paired bootstrap 的假设是否满足？\n   - p 值报告是否完整（特别是 Table 2 中的 n/a 标注）\n   - Multiple testing correction (Holm-Bonferroni k=57) 是否合理？校正后 SciERC p_adj=0.20 的解读\n   - 正文 vs appendix 的数字一致性\n\n请按以下格式输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 severity: critical/warning/info）\n4. Questions（需要作者回答的）\n5. Missing References（如有）\n6. Overall Assessment + 评分 + 置信度"
  }
}
```

</details>

---


### Tool result

_source line 2588 · 2026-05-20T12:48:05.308897+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20414
}
```

</details>

---
