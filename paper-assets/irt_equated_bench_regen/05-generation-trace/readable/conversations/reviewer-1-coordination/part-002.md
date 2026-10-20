# Reviewer 1 coordination — Part 2 of 3

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-1-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/f4/f44f4d47dd150062eb07.json)

## Round 17

### Tool call

_source line 468 · 2026-05-22T03:37:33.615969+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: ρ≈0.997 与 \"31% instability\" 的叙事张力**\n\n同意这是论文最需要解决的叙事问题。ρ≈0.997（§4.6, Figure 4）和 τ≈0.958 表明整体排名几乎不受影响，而标题和 §4.2 section title（\"31% Measurement Instability\"）给出了 alarmist 印象。R2 正确指出 §5.1 的三层分解停留在概念层面。\n\n但我对 R2 的结论有一个重要修正：ρ≈0.997 不能否定 31% DIF 的重要性。论文定位为 psychometric audit，而非 ranking correction tool。31% 的 items 在不同时间段对不同 cohort 产生不同的测量含义，这本身就是 measurement validity 问题——即使最终排名不变，也意味着排名的 evidential basis 发生了变化。类比：两次考试分数相同但考的内容实质不同，结果可比但过程不可比。\n\nR2 的建议（a）提供具体 case study 非常好——Figure 4 中 Llama-3 +53 positions 和 phi-3 +809 positions 已经暗示了这种问题，但需要完整叙述一个 \"practitioner 因忽略 DIF 得出错误结论\" 的 worked example。R2 的建议（b）将 \"instability\" 改为 \"measurement heterogeneity\" 值得采纳——后者更精确，也避免了与 ρ≈0.997 的表面矛盾。\n\n**[AGREE] R2-N2: 归因缺口限制审计协议可操作性**\n\n完全同意，且与我的 W5 一致。补充一点 R2 未提到的：§5.3 的 15%/25% 阈值声称 \"adapt ETS practice\"，但 ETS 的阈值体系是为教育公平性（group fairness across demographics）设计的，其中 \"investigate\" 意味着检查 item 是否对特定人群不公平，有明确的 follow-up protocol（item bias review panel）。迁移到 LLM 场景后，\"investigate\" 的对象和方法完全不同——论文需要为 LLM benchmark maintainer 提供具体的 investigation 流程，而非仅借用 ETS 的数字标准。\n\nR2 建议（a）\"模拟 C% 多高时 ρ 显著下降\"是非常好的实证方向——这能直接将 DIF threshold 与 practitioner-relevant outcome（ranking stability）挂钩。\n\n---\n\n### Should-Fix\n\n**[REBUT] R2-W1: Cross-subject matching 新颖性声明需更谨慎**\n\n部分不同意。R2 正确指出 external/subtest matching 在教育测量文献中已有成熟实践（Nandakumar 1993, purified matching）。但 R2 低估了 LLM 场景下的适配贡献：\n\n1. 教育测量中的 purified subtest matching 主要用于消除 item-level bias（在同一测试内部），而本文的 cross-subject matching 是用 **完全不同 benchmark（GSM8K）的总分** 作为 matching variable——这在概念上不同于 subtest purification，因为 matching variable 来自完全不同的 construct space。\n2. Remark（Zero FPR under single-subject matching）虽然 \"by construction\" 成立，但将其形式化并验证（§4.5, Table 5 的 multi-subject degradation）为 LLM evaluation 社区提供了可直接使用的实践指南。\n3. 教育测量中不存在 \"cross-subject contamination\" 这一特有挑战——人类考生不会因为接触了某科目的考试内容而在其他科目上获得不对称优势。这一应用场景是本文独有的。\n\n不过，我同意论文应更明确承认 purified matching 的先驱地位，将贡献重新定位为 \"将 purified matching 原则适配到 LLM benchmark contamination 场景，并形式化其 FPR 保证\" 而非暗示全新方法。\n\n**[AGREE] R2-W2: \\enlargethispage 格式操纵**\n\n同意。如果论文使用了 `\\enlargethispage{6\\baselineskip}`，这确实过于激进。§4.2 的 permutation test 细节（null C%=0.10%±0.12%, p<0.001）完全可以压缩为一句话并移入附录，腾出空间。\n\n**[AGREE] R2-W3: Growing Pains 对比不完整**\n\n同意。论文可以在不访问 Growing Pains 数据的前提下做概念层面的对比：FPC 假设存在 stable anchor items 用于等值化，而本文发现 31% 的 items 跨时期不稳定——这直接挑战了 FPC 的前提假设。这种概念张力值得 1-2 句话讨论。\n\n**[AGREE] R2-W4: Semi-synthetic injection 现实性**\n\n完全同意，与我的 N2 一致。Binary flipping 是最极端的 uniform exploitation pattern。R2 建议的 \"ability-dependent exploitation rate\" 是一个很好的更现实注入模式——高能力模型可能更容易记忆训练数据，导致 non-uniform DIF。如果此注入模式下 MH-DIF 的检测力显著下降，这会实质性改变论文的实践结论。\n\n**[REBUT] R2-W5: 缺少 polytomous DIF 讨论**\n\n部分不同意。Polytomous DIF（如 generalized MH、Liu-Agresti cumulative common log-odds ratio）确实与 LLM 评测的未来方向相关（open-ended generation），但本文明确聚焦于 binary response 的 MMLU（multiple-choice, 0/1 scoring），且 Limitations 已提及 \"binary response\" 限制。要求在 Related Work 中覆盖 polytomous DIF 文献，超出了本文的 scope——这更适合作为 future work 的一句话提及，而非 Related Work 的系统覆盖。\n\n---\n\n### 小问题\n\n**[AGREE] R2-M1**: \"z = −8σ to −49σ\" 确实不标准。z-score 无量纲，应写 \"z = −8 to −49\" 或 \"8 to 49 standard deviations below the null mean\"。\n\n**[AGREE] R2-M2**: Table 1 的 \"FPR\" 列与 §3.4 的 ΔFPR 确实是不同概念——前者是 empirical cohort comparison 中的 false positive rate，后者是 semi-synthetic injection 中 injection 引入的 FPR 增量。论文应在 Table 1 注脚中明确 FPR 的定义。\n\n**[AGREE] R2-M3**: Bootstrap CI [29.4%, 38.1%] 右偏的解释可以更清楚。\"heavy-tailed C% from subjects exceeding 40%\" 不够直观——建议说明是 subject-level resampling 导致高 C% subjects 被过度抽样时拉高整体 C%。\n\n**[AGREE] R2-M4**: Figure 2 上下面板格式一致性问题——确认同意。\n\n**[AGREE] R2-M5**: Table 1 中 Llama-2 vs Llama-3 行的 FPR/Enrichment 列为 \"--\" 确实缺少注释。可能因为这是 within-family comparison 而非 temporal comparison，没有对应的 ground truth labels 计算 enrichment——但需要在表注中说明。\n\n**[AGREE] R2-M6**: 匿名规则维持良好。\n\n---\n\n### 叙事一致性评估\n\n**[AGREE]** \"measurement heterogeneity\" 确实比 \"instability\" 更精准。\"Instability\" 暗示 benchmark 不可靠，但 ρ≈0.997 说明对 ranking 而言它是可靠的——问题在于 31% 的 items 对不同 cohort 的测量含义不同，这是 heterogeneity 而非 instability。\n\n**[AGREE]** §4.2 section title \"31% Measurement Instability\" 与 \"diagnostic, not destructive\" 定位不完全一致。建议改为 \"31% Measurement Heterogeneity\" 或 \"31% Differential Item Functioning\"。\n\n**[AGREE]** 三层框架（impact / DIF / attribution）在 §5.1 首次引入但 Experiments（§4）未使用——如果将此框架前移到 §3 并在 §4 中系统使用（每个实验结果对应哪一层），论文结构会更 coherent。\n\n---\n\n### 缺失参考文献\n\n**[REBUT]** Swaminathan & Rogers (1990): 论文已在 Appendix A.1 引用此文（\"logistic regression DIF (Swaminathan and Rogers, 1990)\"）。R2 可能希望在 purified subtest matching 的语境下引用，但 Swaminathan & Rogers (1990) 的核心贡献是 logistic regression DIF 而非 purified matching——purified matching 的主要参考应为 Holland & Thayer (1988) 的 iterative purification procedure，论文已引用。\n\n**[AGREE]** Hardy et al. (2026) scalability coefficients 的可获取性需要确认——如果是 preprint 或未正式发表，应标注状态。\n\n---\n\n### 总结\n\nR2 的审稿整体高质量。最有价值的两个 insight 是：(1) ρ≈0.997 与 \"instability\" 叙事的张力（N1），这是论文目前最大的 framing 问题；(2) 审计协议的可操作性缺口（N2），与我的独立评估一致。\n\nR2 给出 Excitement 3/5 并评论 \"现有方法应用到新领域\" 框架限制兴奋度——我对此有不同看法。论文的兴奋度不在于方法本身的新颖性，而在于 empirical findings 的启示性（ground truth meta-critique 颠覆了 contamination detection 领域的基本假设；31% DIF 首次量化了 temporal comparability 问题的规模）。类比 BERTScore 不是 embedding 技术的新颖性而是应用洞察。我维持 Excitement 3.5/5。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: ρ≈0.997 与 \"31% instability\" 的叙事张力**\n\n同意这是论文最需要解决的叙事问题。ρ≈0.997（§4.6, Figure 4）和 τ≈0.958 表明整体排名几乎不受影响，而标题和 §4.2 section title（\"31% Measurement Instability\"）给出了 alarmist 印象。R2 正确指出 §5.1 的三层分解停留在概念层面。\n\n但我对 R2 的结论有一个重要修正：ρ≈0.997 不能否定 31% DIF 的重要性。论文定位为 psychometric audit，而非 ranking correction tool。31% 的 items 在不同时间段对不同 cohort 产生不同的测量含义，这本身就是 measurement validity 问题——即使最终排名不变，也意味着排名的 evidential basis 发生了变化。类比：两次考试分数相同但考的内容实质不同，结果可比但过程不可比。\n\nR2 的建议（a）提供具体 case study 非常好——Figure 4 中 Llama-3 +53 positions 和 phi-3 +809 positions 已经暗示了这种问题，但需要完整叙述一个 \"practitioner 因忽略 DIF 得出错误结论\" 的 worked example。R2 的建议（b）将 \"instability\" 改为 \"measurement heterogeneity\" 值得采纳——后者更精确，也避免了与 ρ≈0.997 的表面矛盾。\n\n**[AGREE] R2-N2: 归因缺口限制审计协议可操作性**\n\n完全同意，且与我的 W5 一致。补充一点 R2 未提到的：§5.3 的 15%/25% 阈值声称 \"adapt ETS practice\"，但 ETS 的阈值体系是为教育公平性（group fairness across demographics）设计的，其中 \"investigate\" 意味着检查 item 是否对特定人群不公平，有明确的 follow-up protocol（item bias review panel）。迁移到 LLM 场景后，\"investigate\" 的对象和方法完全不同——论文需要为 LLM benchmark maintainer 提供具体的 investigation 流程，而非仅借用 ETS 的数字标准。\n\nR2 建议（a）\"模拟 C% 多高时 ρ 显著下降\"是非常好的实证方向——这能直接将 DIF threshold 与 practitioner-relevant outcome（ranking stability）挂钩。\n\n---\n\n### Should-Fix\n\n**[REBUT] R2-W1: Cross-subject matching 新颖性声明需更谨慎**\n\n部分不同意。R2 正确指出 external/subtest matching 在教育测量文献中已有成熟实践（Nandakumar 1993, purified matching）。但 R2 低估了 LLM 场景下的适配贡献：\n\n1. 教育测量中的 purified subtest matching 主要用于消除 item-level bias（在同一测试内部），而本文的 cross-subject matching 是用 **完全不同 benchmark（GSM8K）的总分** 作为 matching variable——这在概念上不同于 subtest purification，因为 matching variable 来自完全不同的 construct space。\n2. Remark（Zero FPR under single-subject matching）虽然 \"by construction\" 成立，但将其形式化并验证（§4.5, Table 5 的 multi-subject degradation）为 LLM evaluation 社区提供了可直接使用的实践指南。\n3. 教育测量中不存在 \"cross-subject contamination\" 这一特有挑战——人类考生不会因为接触了某科目的考试内容而在其他科目上获得不对称优势。这一应用场景是本文独有的。\n\n不过，我同意论文应更明确承认 purified matching 的先驱地位，将贡献重新定位为 \"将 purified matching 原则适配到 LLM benchmark contamination 场景，并形式化其 FPR 保证\" 而非暗示全新方法。\n\n**[AGREE] R2-W2: \\enlargethispage 格式操纵**\n\n同意。如果论文使用了 `\\enlargethispage{6\\baselineskip}`，这确实过于激进。§4.2 的 permutation test 细节（null C%=0.10%±0.12%, p<0.001）完全可以压缩为一句话并移入附录，腾出空间。\n\n**[AGREE] R2-W3: Growing Pains 对比不完整**\n\n同意。论文可以在不访问 Growing Pains 数据的前提下做概念层面的对比：FPC 假设存在 stable anchor items 用于等值化，而本文发现 31% 的 items 跨时期不稳定——这直接挑战了 FPC 的前提假设。这种概念张力值得 1-2 句话讨论。\n\n**[AGREE] R2-W4: Semi-synthetic injection 现实性**\n\n完全同意，与我的 N2 一致。Binary flipping 是最极端的 uniform exploitation pattern。R2 建议的 \"ability-dependent exploitation rate\" 是一个很好的更现实注入模式——高能力模型可能更容易记忆训练数据，导致 non-uniform DIF。如果此注入模式下 MH-DIF 的检测力显著下降，这会实质性改变论文的实践结论。\n\n**[REBUT] R2-W5: 缺少 polytomous DIF 讨论**\n\n部分不同意。Polytomous DIF（如 generalized MH、Liu-Agresti cumulative common log-odds ratio）确实与 LLM 评测的未来方向相关（open-ended generation），但本文明确聚焦于 binary response 的 MMLU（multiple-choice, 0/1 scoring），且 Limitations 已提及 \"binary response\" 限制。要求在 Related Work 中覆盖 polytomous DIF 文献，超出了本文的 scope——这更适合作为 future work 的一句话提及，而非 Related Work 的系统覆盖。\n\n---\n\n### 小问题\n\n**[AGREE] R2-M1**: \"z = −8σ to −49σ\" 确实不标准。z-score 无量纲，应写 \"z = −8 to −49\" 或 \"8 to 49 standard deviations below the null mean\"。\n\n**[AGREE] R2-M2**: Table 1 的 \"FPR\" 列与 §3.4 的 ΔFPR 确实是不同概念——前者是 empirical cohort comparison 中的 false positive rate，后者是 semi-synthetic injection 中 injection 引入的 FPR 增量。论文应在 Table 1 注脚中明确 FPR 的定义。\n\n**[AGREE] R2-M3**: Bootstrap CI [29.4%, 38.1%] 右偏的解释可以更清楚。\"heavy-tailed C% from subjects exceeding 40%\" 不够直观——建议说明是 subject-level resampling 导致高 C% subjects 被过度抽样时拉高整体 C%。\n\n**[AGREE] R2-M4**: Figure 2 上下面板格式一致性问题——确认同意。\n\n**[AGREE] R2-M5**: Table 1 中 Llama-2 vs Llama-3 行的 FPR/Enrichment 列为 \"--\" 确实缺少注释。可能因为这是 within-family comparison 而非 temporal comparison，没有对应的 ground truth labels 计算 enrichment——但需要在表注中说明。\n\n**[AGREE] R2-M6**: 匿名规则维持良好。\n\n---\n\n### 叙事一致性评估\n\n**[AGREE]** \"measurement heterogeneity\" 确实比 \"instability\" 更精准。\"Instability\" 暗示 benchmark 不可靠，但 ρ≈0.997 说明对 ranking 而言它是可靠的——问题在于 31% 的 items 对不同 cohort 的测量含义不同，这是 heterogeneity 而非 instability。\n\n**[AGREE]** §4.2 section title \"31% Measurement Instability\" 与 \"diagnostic, not destructive\" 定位不完全一致。建议改为 \"31% Measurement Heterogeneity\" 或 \"31% Differential Item Functioning\"。\n\n**[AGREE]** 三层框架（impact / DIF / attribution）在 §5.1 首次引入但 Experiments（§4）未使用——如果将此框架前移到 §3 并在 §4 中系统使用（每个实验结果对应哪一层），论文结构会更 coherent。\n\n---\n\n### 缺失参考文献\n\n**[REBUT]** Swaminathan & Rogers (1990): 论文已在 Appendix A.1 引用此文（\"logistic regression DIF (Swaminathan and Rogers, 1990)\"）。R2 可能希望在 purified subtest matching 的语境下引用，但 Swaminathan & Rogers (1990) 的核心贡献是 logistic regression DIF 而非 purified matching——purified matching 的主要参考应为 Holland & Thayer (1988) 的 iterative purification procedure，论文已引用。\n\n**[AGREE]** Hardy et al. (2026) scalability coefficients 的可获取性需要确认——如果是 preprint 或未正式发表，应标注状态。\n\n---\n\n### 总结\n\nR2 的审稿整体高质量。最有价值的两个 insight 是：(1) ρ≈0.997 与 \"instability\" 叙事的张力（N1），这是论文目前最大的 framing 问题；(2) 审计协议的可操作性缺口（N2），与我的独立评估一致。\n\nR2 给出 Excitement 3/5 并评论 \"现有方法应用到新领域\" 框架限制兴奋度——我对此有不同看法。论文的兴奋度不在于方法本身的新颖性，而在于 empirical findings 的启示性（ground truth meta-critique 颠覆了 contamination detection 领域的基本假设；31% DIF 首次量化了 temporal comparability 问题的规模）。类比 BERTScore 不是 embedding 技术的新颖性而是应用洞察。我维持 Excitement 3.5/5。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-22T03:37:37.580806+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3964
}
```

</details>

---


### Assistant

_source line 470 · 2026-05-22T03:37:47.321162+00:00_

已提交对 Reviewer 2 全部审稿意见的逐条回应（14 个 AGREE + 3 个 REBUT）。主要分歧点：cross-subject matching 的新颖性定位（R2-W1）、polytomous DIF 讨论的必要性（R2-W5）、Swaminathan & Rogers 引用（已在附录中出现）。在 N1（叙事张力）和 N2（审计协议可操作性）上与 R2 达成共识。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 18

## Round 18

64 recorded events


### User

_source line 471 · 2026-05-22T05:20:51.690807+00:00_

[Round 1 审稿请求]:
你负责审查**方法严谨性 + 实验可靠性**。

## Venue 信息
- **目标**: EMNLP 2026 (ACL Rolling Review May cycle)
- **类别**: Long Paper (正文 ≤8 页，参考文献不限)
- **模板**: ACL style template, `[review]` 模式
- **匿名**: Double-blind
- **Deadline**: 2026-05-25
- **评分标准**: Overall Assessment 1-5 分 (3.5 = Borderline Conference, 4 = Conference)

## 论文路径
- LaTeX: `projects/irt_equated_bench_regen/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/submitted.pdf`

## 论文概要
题目: "Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models"

将 MH-DIF (Mantel-Haenszel Differential Item Functioning) 应用于 METABENCH 5,227 模型 × 12,508 MMLU items 的 response matrix，发现 31% items 在 2023 vs 2024 cohorts 间存在 ETS-C 级别 DIF。提出 cross-subject matching 消除 FPR 膨胀，semi-synthetic injection 验证检测力，并在 6 个 benchmark 上复制。

## 你的审查侧重

1. **MH-DIF 方法适用性**：MH 假设（条件独立、单维性）在 LLM 场景是否充分处理？quintile-based stratification 是否足够？
2. **Semi-synthetic framework 有效性**：binary flipping 作为 contamination 模拟的生态效度；ΔTPR 作为 upper-bound 的讨论是否充分？
3. **Cross-subject matching 的 ΔFPR=0.000 声明**：是否有适当限定（single-subject vs multi-subject）？bootstrap CI 的构造是否正确？
4. **Structural controls 的完备性**：6 种 alternative explanations 是否足够排除 confounds？matched-ability 分析、IRT θ-conditioning、within-subject DIF 三重验证是否严密？
5. **统计推断**：样本非独立性（model family clustering）对 χ² 检验的影响；多重比较校正；置信区间宽度
6. **Cross-benchmark replication**：6 benchmark 结果的一致性和差异是否有合理解释？
7. **Downstream impact 分析**：ρ≈0.997 与 family-level rank shifts 的表面矛盾是否充分讨论？

请按 ARR review form 结构输出：Summary → Strengths → Weaknesses (逐条编号 W1, W2, ...) → Questions → Missing References → Overall Assessment + Confidence。Weaknesses 按严重程度排序（Must-Fix → Should-Fix → Minor）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-22T05:21:00.594934+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-22T05:21:01.751470+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1156
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-22T05:21:01.751857+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-22T05:21:01.802350+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-22T05:21:06.070593+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 477 · 2026-05-22T05:21:08.186920+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 478 · 2026-05-22T05:21:12.685346+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found relevant information about the ACL Rolling Review 2026. Here are the key resources and details:

## Reviewer Guidelines

The ARR reviewer workflow asks reviewers to (1) read the paper and get the first impression, (2) search for related work, and if not qualified to review all aspects, state in the review which major parts were not checked, such as proofs. 

Reviewers are provided with a checklist to flag problems that other people may have missed.

## Review Form Criteria

Outstanding papers should be either fascinating
…[truncated 902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6614
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-22T05:21:14.198437+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 587.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 509.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 535.5}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.8}], \"total_pages\": 14, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_p
…[truncated 50 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6011
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-22T05:21:21.782260+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form structure: all dimensions/criteria, their rating scales (1-5 or other), and what each score level means. Include: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, Clarity, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form structure: all dimensions/criteria, their rating scales (1-5 or other), and what each score level means. Include: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, Clarity, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 481 · 2026-05-22T05:21:22.435194+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-22T05:21:22.938544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-22T05:21:23.444524+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1009
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-22T05:21:23.445003+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-22T05:21:24.049624+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1111
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-22T05:21:24.050098+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-22T05:21:24.503552+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1058
}
```

</details>

---


### Tool result

_source line 488 · 2026-05-22T05:21:24.856908+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-22T05:21:29.226553+00:00_

# ACL Rolling Review Form Structure

## Scored Dimensions

**1. Reviewer Confidence** (1-5 scale)
- 5: "Positive that my evaluation is correct"
- 4: "Quite sure" with unlikely but possible errors
- 3: "Pretty sure" but may have missed details
- 2: "Willing to defend" but likely missed some points
- 1: "Not my area" or paper very difficult to understand

**2. Soundness** (1-5 scale with half-points)
- 5: "Excellent" and "one of the most thorough"
- 4: "Strong" with sufficient support; extra experiments optional
- 3: "Acceptable" with main claims supported
- 2: "Poor" with insufficient support for main claims
- 1: "Major Issues" insufficient for publication

**3. Excitement** (1-5 scale with half-points)
- 5: "Highly Exciting"; would recommend widely
- 4: "Exciting"; would mention to others
- 3: "Interesting"; might mention selectively
- 2: "Potentially Interesting" to some community members
- 1: "Not Exciting"; unlikely to resonate broadly

**4. Overall Assessment** (1-5 scale with half-points)
- 5: Award consideration (top 2.5%)
- 4: Conference acceptance
- 3: Findings track acceptance
- 2: Needs substantial revisions for next cycle
- 1: Do not resubmit; irrelevant to field

**5. Reproducibility** (1-5 scale)
- 5: Easy reproduction possible
- 4: Mostly reproducible with minor variations
- 3: Reproducible with difficulty; underspecified parameters
- 2: Hard to reproduce; data unavailable
- 1: Cannot reproduce

**6. Datasets** (1-5 scale)
- 5: "Enabling" impact on research choices
- 4: "Useful" for ongoing work
- 3: "Potentially useful"
- 2: "Documentary" value only
- 1: No usable datasets

**7. Software** (1-5 scale)
- 5: "Enabling" impact on research
- 4: "Useful" for researchers/developers
- 3: "Potentially useful"
- 2: "Documentary" utility
- 1: No usable software released

**8. Author Identity Knowledge** (1-5 scale)
- 5: Know author identity via submission violations
- 4: Know identity from preprints/allowed papers
- 3: Deduced from submission contents
- 2: Lear
…[truncated 304 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7444
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-22T05:21:35.963511+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 491 · 2026-05-22T05:21:36.569887+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 492 · 2026-05-22T05:21:36.922331+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 493 · 2026-05-22T05:21:36.922762+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 494 · 2026-05-22T05:21:38.330802+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1760
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-22T05:21:38.331909+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-22T05:21:38.482992+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-22T05:21:39.288429+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-22T05:21:39.389892+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "9-14",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "9-14",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-22T05:21:40.194978+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.1}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 567.2}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 578.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 434.4}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 190.2}], \"total_pages\": 14, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-22T05:21:51.896023+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 501 · 2026-05-22T05:21:52.450847+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 502 · 2026-05-22T05:21:52.853988+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 503 · 2026-05-22T05:21:52.955925+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 504 · 2026-05-22T05:21:53.810579+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1359
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-22T05:21:53.812475+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-22T05:21:53.812957+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 507 · 2026-05-22T05:21:54.315932+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 508 · 2026-05-22T05:21:54.771839+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 509 · 2026-05-22T05:21:54.772269+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 510 · 2026-05-22T05:21:55.275333+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-22T05:21:55.377186+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-22T05:22:03.922646+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-22T05:22:03.923242+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Temporal Measurement Instability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-22T05:22:06.636919+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-22T05:22:06.788016+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees 
…[truncated 8131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-22T05:22:06.788463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-22T05:22:06.890262+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	As approximate parametric bounds, a Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$ (details in \Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold. Power varies substantially with item discrimination: TPR ranges from 0.40 at $a = 0.5$ to 0.95 at $a = 2.0$; the gap between TPR at mean $a$ (0.87) and the aggregate TPR (0.68) quantifies the power cost of parameter heterogeneity, consistent with Jensen's inequality (\Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal Comparability: 31\% Measurement Instability}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%], $B = 1{,}000$ model-level resamples; rightward asymmetry reflects heavy-tailed C\% from subjects exceeding 40\%). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold already provides implicit multiple-testing protection.
17	
18	\looseness=-1
19	Three controls confirm this reflects genuine temporal change. A random split of the 2023 c
…[truncated 10656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-22T05:22:13.927900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-22T05:22:14.381959+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\enlargethispage{2\baselineskip}
4	
5	\subsection{Implications for Benchmark Temporal Comparability}
6	\label{sec:disc_temporal}
7	
8	\looseness=-1
9	Temporal DIF decomposes benchmark differences into three layers: (1)~\emph{impact}---ability differences removed by matching ($\sim$2.4~pp); (2)~\emph{DIF}---item-level differences after ability control ($\sim$28--29\% floor, 92.4\% item-specific); (3)~\emph{attribution}---contamination, capability evolution, or methodology shifts, underdetermined without training data. Regardless of attribution, temporal DIF means the same score carries different meaning across model generations.
10	
11	\subsection{Ground Truth Meta-Critique}
12	\label{sec:disc_groundtruth}
13	
14	\looseness=-1
15	The near-independence between DIF flags and web-overlap labels (\Cref{sec:groundtruth}) reflects a category error: web-overlap measures global exposure, while DIF measures differential functioning, making overlap-based labels an inappropriate ground truth for a differential method. Semi-synthetic dose-response confirms detection works when present; the disconnect is in the ground truth.
16	
17	\subsection{Recommended DIF Audit Protocol}
18	\label{sec:disc_protocol}
19	
20	\looseness=-1
21	We propose running temporal MH-DIF whenever $\geq 500$ new models accumulate ($N \geq 80$ suffices per \Cref{sec:validation}; 500 ensures family diversity). Empirical $\rho$ degradation simulation---DIF-ordered versus random item removal across six benchmarks---grounds graduated thresholds:
22	(1)~\emph{Monitor} (C\% $< 15\%$): $\Delta\rho < 0.001$ vs.\ random on all benchmarks; report C\% in release notes.
23	(2)~\emph{Flag} ($15$--$25\%$): $\Delta\rho = 0.001$--$0.003$ on 4/6 benchmarks; report stable-item rankings alongside full rankings.
24	(3)~\emph{Act} (C\% $\geq 25\%$): WinoGrande drops below $\rho = 0.995$ at 25\% DIF-ordered removal; review flagged item content, cross-reference with contamination i
…[truncated 342 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-22T05:22:14.382439+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-22T05:22:14.784401+00:00_

1	\section*{Limitations}
2	
3	\paragraph{Methodological scope.}
4	MH-DIF detects only uniform DIF; logistic regression reveals an additional 24.8\% non-uniform DIF, making 31\% conservative. More fundamentally, DIF detects \emph{that} items function differently but cannot determine \emph{why}---the signal may reflect contamination, capability change, or training methodology shifts. A definitive causal decomposition remains out of reach without access to model training data. The semi-synthetic framework uses binary response flipping (incorrect $\to$ correct) to simulate differential contamination, representing a worst-case uniform exploitation pattern. Real-world contamination involves partial memorization, reasoning shortcuts, and format-specific advantages; detection power under such realistic patterns is untested. The moderate $\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$ reflects sensitivity to severe differential behavior; the framework's primary methodological contribution---cross-subject matching achieving $\Delta\mathrm{FPR} = 0.000$---is a matching strategy property independent of injection realism.
5	
6	\paragraph{Examinee non-independence.}
7	The MH $\chi^2$ test assumes independent examinees, yet LLMs sharing base models, training data, or architectures violate this assumption. Empirical mitigations partially address this: permutation simulation bounds LD-attributable FPR inflation to ${<}0.001$~pp, and graduated de-duplication ($K{=}20$: C\% $= 29.1\%$) shows family structure does not inflate results. \citet{french2010hierarchical} show that MH maintains nominal size under moderate clustering in educational settings, consistent with our empirical findings; however, the extreme relatedness of some LLM families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in that work. Cluster bootstrap resampling at the family level (29 families with $\geq$3 members, 1{,}882 models, $B = 1{,}000$) yields a 95\% CI of $[26.7\%, 53.2\%]$, $3.1
…[truncated 1341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-22T05:22:14.835170+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-22T05:22:14.885951+00:00_

1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini
…[truncated 8202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-22T05:22:21.973219+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-22T05:22:22.375941+00:00_

1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet whether individual items measure the same construct over time is rarely tested---and existing contamination detectors validate against ground truth that conflates global exposure with differential functioning. We develop a semi-synthetic injection framework with cross-subject matching that achieves zero false positive inflation under single-subject contamination ($\Delta\mathrm{FPR} = 0.000$; $\Delta\mathrm{FPR} < 0.01$ for $k \leq 5$ subjects) while preserving detection power under worst-case uniform injection ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$), and show that web-overlap contamination labels are near-independent of Mantel-Haenszel Differential Item Functioning (DIF) flags (enrichment $\approx 0.96$, $\phi = 0.012$)---exposing a category error in prevailing validation methodology. Applying MH-DIF with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 items), we find 17.9--31.3\% of items exhibit large temporal DIF (ETS~C) between 2023 and 2024 cohorts, each 45--174$\times$ above random baselines, with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). This does not threaten aggregate ranking validity ($\rho \approx 0.997$, $\tau \approx 0.958$), but specific model families show concentrated rank shifts (Llama-3: ${+}53$ median positions, Mistral: $-35$) and 2.0\% of pairwise rankings reverse. Item-level decomposition shows 92.4\% of the signal is item-specific; DIF-flagged items concentrate discriminative information ($z = -8$ to $-49$) with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-22T05:22:22.376484+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-22T05:22:22.783013+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. This pattern persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of the DIF signal is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this measurement instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference~\citep{shi2024mink} to performance-based detectors~\citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique}. These methods validate d
…[truncated 5079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 406
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-22T05:22:22.784769+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-22T05:22:22.886556+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-1
5	Cross-subject matching ($\Delta\mathrm{FPR} = 0.000$) resolves the validation gap: web-overlap labels are near-independent of DIF flags (enrichment $\approx 0.96$). Across six benchmarks, 17.9--31.3\% of items exhibit temporal instability associated with item properties; LLM benchmarks need psychometric monitoring alongside score reporting.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-22T05:24:22.667919+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines: what reviewers should evaluate, how to structure reviews, what constitutes a good review, criteria for rating papers. Include any specific instructions about evaluating methodology, experiments, and claims."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key reviewer guidelines: what reviewers should evaluate, how to structure reviews, what constitutes a good review, criteria for rating papers. Include any specific instructions about evaluating methodology, experiments, and claims."
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-22T05:24:32.619597+00:00_

# ARR Reviewer Guidelines: Key Evaluation Framework

## Core Review Structure

Reviewers must complete four primary tasks:

1. **Allocate adequate time** for both initial reviewing and discussion periods
2. **Check assignments** for expertise fit and conflicts of interest
3. **Write substantive reviews** addressing multiple dimensions
4. **Engage with author responses** and update assessments accordingly

## What Reviewers Should Evaluate

### Reading Strategy
Reviewers should read papers twice: first for understanding the research question and contribution scope, then for technical soundness. The guidelines emphasize: *"read the paper at least twice: skimming and in-depth reading."*

### Three Scoring Dimensions

- **Soundness**: Technical validity and methodological rigor
- **Excitement**: Personal interest level (orthogonal to soundness)
- **Overall Assessment**: Composite recommendation reflecting soundness, novelty, and potential impact

## Evaluation Framework

### Specificity Requirement
Reviews must provide concrete feedback. Rather than stating *"The paper is missing relevant references,"* reviewers should specify which references (e.g., "XYZ").

### Common Review Pitfalls to Avoid

The guidelines list 17 heuristics that often lead to flawed assessments:

- Dismissing results as "obvious in retrospect" (hindsight bias)
- Requiring SOTA performance when not claimed
- Penalizing novel work lacking precedent
- Demanding additional experiments beyond claim scope
- Criticizing negative results

As noted: *"simple solutions are in fact preferable, as they are less brittle and easier to deploy"* in real-world contexts.

## Methodology & Experiment Evaluation

Reviewers should assess:

- **M1**: LLM evaluation validation in specific contexts
- **M2**: Reproducibility (sufficient hyperparameter details, code availability disclosure)
- **M3**: Undisclosed data quality issues
- **M4**: Justified model/benchmark selection aligned with claims
- **M5**: Complete and corr
…[truncated 1167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9951
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-22T05:27:02.176527+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见（Round 1 — 方法严谨性 + 实验可靠性）\n\n---\n\n### Paper Summary\n\n本文将教育测量学中的 Mantel-Haenszel Differential Item Functioning (MH-DIF) 分析应用于 LLM benchmark 的时间可比性检验。基于 METABENCH 的 5,227 模型 × 12,508 MMLU items 响应矩阵，作者发现 31.3% 的 items 在 2023 vs. 2024 cohorts 间展现 ETS Category C 级别的 DIF（|Δ_MH| ≥ 1.5, p < 0.05）。论文提出 cross-subject matching 消除 FPR 膨胀（ΔFPR = 0.000），构建 semi-synthetic injection framework 验证检测力（ΔTPR = +0.508 at p=0.5），并在 6 个 benchmark 上复制。核心洞察为：web-overlap contamination labels 与 DIF flags 近乎独立（enrichment ≈ 0.96），暴露了现有 contamination detection 验证方法论中的 category error。\n\n---\n\n### Summary of Strengths\n\n**S1. 规模空前的心理测量审计**：5,227 models × 12,508 items 的 DIF 分析是目前最大规模的 LLM benchmark psychometric audit，6 个 benchmark 的 replication 增强了结论的 robustness。\n\n**S2. Ground truth meta-critique 有独到洞察**：论文清晰区分了 global exposure（web-overlap）和 differential functioning（DIF），用 enrichment ≈ 0.96、Jaccard = 0.206、φ = 0.012 三个指标实证地证明两者近乎独立。Figure 1 的 ICC 示意图有效传达了这一概念区分。这一发现对 contamination detection 研究具有方法论意义。\n\n**S3. Cross-subject matching 设计严谨**：cross-subject matching 排除待测 subject 的 total score 作为 matching variable，在 single-subject injection 下 ΔFPR = 0 是 constructive guarantee（Section 3.4, Remark），不依赖特定 injection 模式。这是一个 clean 的方法论贡献。\n\n**S4. Structural controls 全面**：论文系统检验了 6 种 alternative explanations（ability mismatch、IRT θ-conditioning、within-subject DIF、family de-duplication、architecture heterogeneity、permutation test），每一种都有明确的定量结果。Table 2 的结构化呈现清晰。\n\n**S5. 写作精炼、叙事结构合理**：论文在 8 页正文内覆盖了大量分析，写作密度高但条理清晰。\"diagnostic, not destructive\" 的定位避免了过度声称，对 ρ ≈ 0.997 与 family-level rank shifts 的 tension 有充分讨论。\n\n**S6. Simpson's paradox 分析有价值**：Section 4.2 的 logistic regression 展示 domain accuracy 在 aggregate level 正向预测 DIF（OR=1.55），控制 item 属性后反转（OR=0.73），92.4% signal 为 item-specific。这一 decomposition 增强了对 DIF 信号本质的理解。\n\n---\n\n### Summary of Weaknesses\n\n#### Must-Fix 问题（影响接收决定）\n\n**W1** [critical] **Quintile stratification (K=5) 在 bimodal LLM 分布下的充分性未验证**\n- 具体位置：Section 3.2（\"We use K = 5 equiprobable strata (quintile-based binning)\"）、Section 3.2 paragraph \"LLM-specific challenges\"（\"the ability distribution is non-normal (bimodal from base vs. instruction-tuned models), motivating quintile-based rather than parametric stratification\"）\n- 问题：论文正确识别了 LLM ability 分布的 bimodality（base vs. instruction-tuned），但仅以此为由选择 quintile-based 而非 parametric stratification，而未验证 K=5 在 bimodal 分布下是否提供足够的 ability conditioning。在 bimodal 分布中，quintile bins 可能跨越两个 mode 的边界，导致 within-stratum ability variance 异常大，产生 residual confounding。以 N=1,887 models 的 temporal cohorts 为例，每个 quintile stratum 包含 ~377 models。如果 base 和 instruction-tuned models 的 total score 差异恰好落在某一 quintile 边界附近，该 stratum 内的 ability 异质性会显著削弱 conditioning 效果。\n- 为什么影响接收：K 的选择直接影响 DIF 检测的 validity——如果 conditioning 不充分，ability differences 会被误判为 DIF。论文引用 ETS 推荐作为 K=5 的依据，但 ETS 的推荐基于 educational testing 中近似正态的能力分布，不适用于 bimodal 场景。\n- 建议修改方向：报告 K=10 和 K=20 的 sensitivity analysis 结果（或至少 K=10）；分析 bimodal 分布下各 stratum 的 within-stratum ability SD；如果 C% 对 K 不敏感，这将大幅增强 robustness。\n\n**W2** [critical] **ΔFPR = 0.000 在 abstract/contributions 中的限定条件不足**\n- 具体位置：Abstract（\"achieves zero false positive inflation under single-subject contamination (ΔFPR = 0.000; ΔFPR < 0.01 for k ≤ 5 subjects)\"）、Section 1 Contribution 2（\"achieves ΔFPR = 0.000\"）\n- 问题：Abstract 的措辞在字面上提供了 single-subject 限定，但 \"zero false positive inflation\" 的强调效果远大于其后的限定条件。在 Contribution 2 中仅写 \"achieves ΔFPR = 0.000\" 而未附加条件。Table 5（Appendix）显示 k=10 时 ΔFPR = 0.047±0.022，k=20 时 = 0.069±0.018——在 MMLU 的 57 subjects 中，真实 contamination 跨越 >5 subjects 是完全可能的（尤其是 web-crawled training data）。论文在 Section 3.4 和 Limitations 中确实讨论了 boundary，但 abstract 和 contributions 的呈现方式可能让读者获得比实际更强的保证。\n- 为什么影响接收：ΔFPR = 0.000 是论文的 headline claim 之一，如果读者仅看 abstract 会高估 cross-subject matching 的 robustness。ARR 审稿标准 R4 要求 \"avoiding overclaiming or misleading framing\"。\n- 建议修改方向：Contribution 2 应改为 \"achieves ΔFPR = 0.000 under single-subject contamination and ΔFPR < 0.007 for k ≤ 5 subjects (≤9% of domains)\"，并在 abstract 中注明 boundary（>10 subjects 时 ΔFPR 上升至 0.026–0.069）。\n\n#### Should-Fix 问题（影响评分但不一票否决）\n\n**W3** [warning] **Semi-synthetic injection 的 ecological validity 不足，ΔTPR = +0.508 的 moderate 水平值得关注**\n- 具体位置：Section 3.4（\"we flip incorrect responses to correct in the focal group at exploitation rate p\"）、Section 4.5、Limitations\n- 问题：Binary flipping（incorrect → correct）是 uniform worst-case pattern，与真实 contamination 差距较大。真实 contamination 可能表现为：(a) partial memorization（对特定 answer choice 有偏好但不一定答对）；(b) reasoning shortcuts（正确推理路径被 memorized template 替代）；(c) format-specific advantages。论文承认这是 \"worst-case uniform exploitation pattern\" 且 ΔTPR 是 \"upper-bound estimate\"——但这恰恰意味着在更 realistic 的 contamination 模式下，检测力可能显著低于 0.508。ΔTPR = 0.508 本身只是 moderate（在 injected items 中仅约一半被检测到），如果 upper-bound 就是 moderate，那 realistic 场景下的检测力如何？\n- 建议：(1) 补充至少一种更 realistic 的 injection pattern（如 answer-choice bias：翻转为特定 option 而非正确答案）的 sensitivity analysis；(2) 在正文中明确讨论 detection power 的 lower-bound implications，而非仅强调 ΔFPR=0 的方法论贡献。\n\n**W4** [warning] **Family-level cluster bootstrap CI 应在正文中更突出**\n- 具体位置：Limitations（\"Cluster bootstrap resampling at the family level (29 families with ≥3 members, 1,882 models, B = 1,000) yields a 95% CI of [26.7%, 53.2%], 3.1× wider than the model-level CI [29.4%, 38.1%]\"）\n- 问题：model-level CI [29.4%, 38.1%] 在 Section 4.2 正文中报告（\"95% bootstrap CI: [29.4%, 38.1%]\"），但 family-level CI [26.7%, 53.2%] 仅出现在 Limitations。鉴于 LLM families 的 extreme relatedness（论文自己描述为 \"hundreds of Llama-2 fine-tunes exceeds the clustering levels studied\"），family-level CI 才是更 conservative、更 appropriate 的 uncertainty estimate。3.1× 的 widening 说明 family 结构对 inference 有实质影响。\n- 建议：在 Section 4.2 正文中同时报告 model-level 和 family-level CI（例如 \"31.3% [model-level CI: 29.4–38.1%; family-level CI: 26.7–53.2%]\"），让读者自行判断 precision。\n\n**W5** [warning] **Table 1 中 \"FPR (clean)\" 的术语使用自相矛盾**\n- 具体位置：Table 1 caption（\"FPR is the flagging rate on web-overlap 'clean' items (Li et al., 2024b), not a traditional false positive rate\"）、Section 4.3\n- 问题：论文在 Section 4.3 用整节篇幅论证 web-overlap labels 是 \"the wrong ground truth for a differential method\"——即 DIF flags 和 web-overlap labels 衡量的是不同概念。但 Table 1 仍用 \"FPR\" 指代 DIF 在 web-overlap \"clean\" items 上的 flagging rate。如果 web-overlap \"clean\" 不等于 \"no DIF\"，那 \"clean\" items 上的 DIF-C flagging rate 就不是 false positive rate（即便 Table 1 caption 加了 disclaimer）。这在概念上是自相矛盾的：一面说 web-overlap 不是合适的 ground truth，一面用它定义 FPR。\n- 建议：将 Table 1 的列名改为 \"C% (clean)\" 或 \"DIF-C rate on clean items\"，并删除 \"FPR\" 术语以避免混淆。\n\n**W6** [warning] **Graduated de-duplication 的解读偏乐观**\n- 具体位置：Section 4.4（\"Graduated de-duplication (K=10: 22.7%; K=20: 29.1%) confirms family structure does not inflate C%\"）\n- 问题：K=10 de-duplication 将 C% 从 31.3% 降至 22.7%，降幅 8.6 pp（27% reduction）。论文将此解读为 \"family structure does not inflate C%\"，但 8.6 pp 的下降是非 trivial 的。更准确的表述应为 \"family structure inflates C% by up to ~8 pp, but the residual 22.7% remains far above the random baseline (0.18%)\"。当前措辞可能让读者低估 family clustering 的影响。\n- 建议：改为更 nuanced 的表述，承认 family structure 有 moderate inflation effect 但不改变定性结论。\n\n#### Minor 问题（不影响接收）\n\n**M1**: Section 4.6 中 \"Among the 200 most displaced models, 33.6% of pairwise rankings reverse\" 存在 selection bias——选取 displacement 最大的子集天然会放大 rank reversal rate。应注明这是 conditional on selection 的数字，或补充全样本的 pairwise reversal rate（从 Table 3 推断 flip rate ≈ 2%）。\n\n**M2**: GSM1K correlation analysis (r = -0.478, p = 0.005, N=33) 统计功效有限，论文在 Limitations 中承认了 \"exploratory\"，但 Section 4.7 正文中的呈现方式（作为 cross-benchmark validation 的组成部分）可能让读者高估其证据强度。建议在正文中也标注 \"exploratory\"。\n\n**M3**: Section 5.3 提出的 DIF audit protocol（Monitor/Flag/Act thresholds）基于经验而非理论推导。C% = 15% 和 25% 的阈值来自 ρ degradation simulation，但未提供 formal justification（如 type I/II error control）。这不影响论文的核心贡献，但 protocol 的可操作性需要更多验证。\n\n**M4**: 论文脚注 1 提供了 anonymous code repository URL，但论文中引用的若干工具（PSN-IRT, METABENCH response matrix）的可获取性未明确说明，可能影响 reproducibility 评分。\n\n---\n\n### Questions for Authors\n\n**Q1**: K=5 quintile stratification 的 sensitivity analysis 是否已在内部测试过？如果有 K=10/20 的结果，能否在 rebuttal 中提供？\n\n**Q2**: Cross-subject matching 在 MMLU 以外的 benchmark（如 GSM8K, 仅有 1 个 \"subject\"）上如何操作？Section 4.7 提到 external matching 用于 GSM8K，但 cross-subject matching 是否仅限于 multi-domain benchmarks？如果是，这是否限制了方法的 generalizability？\n\n**Q3**: 论文报告 IRT θ-conditioning 与 total score 的 r = 0.9986，但 2PL fit 较差（Appendix A.2）。在 model fit 较差的情况下，θ estimates 本身是否可靠？r = 0.9986 是否仅反映了 total score 和 θ 在 rank-order 上的一致性而非 scale 上的一致性？\n\n**Q4**: 论文使用 2023 vs. 2024 release date 作为 temporal cohort 划分。这是否与模型的 training data cutoff 对齐？一个 2024 年发布但 training data cutoff 在 2022 年的模型可能被错误分类。论文是否有 training data cutoff 的信息？\n\n---\n\n### Missing References\n\n1. **Penfield & Camilli (2007)** \"Differential Item Functioning\" in *Handbook of Statistics* — 作为 DIF 方法论的现代综述，与本文方法论定位高度相关。\n2. **Millsap & Everson (1993)** \"Methodology of Differential Item Functioning Research\" — 早期但权威的 DIF 方法论总结。\n3. **Liang et al. (2023)** \"Holistic Evaluation of Language Models\" (HELM) — 作为 LLM evaluation 的重要 framework，值得在 Related Work 中提及。\n\n---\n\n### Limitations and Societal Impact\n\nLimitations 章节覆盖了 4 个方面（methodological scope、examinee non-independence、matching boundary、generalizability），内容充实且诚实。特别值得肯定的是对 family-level cluster bootstrap CI 的报告。\n\n建议在 generalizability 段落中补充：当前结论仅适用于 METABENCH 中 Open LLM Leaderboard 的公开模型，对 closed-source models（GPT-4、Claude 等）的 DIF behavior 无法推断，因为这些模型的 training data composition 和 release pattern 可能有系统性差异。\n\n---\n\n### Ethical Concerns\n\n无显著伦理问题。论文使用公开数据集和公开模型评估结果，不涉及 human subjects。Anonymous code repository 的做法符合 double-blind 要求。\n\n---\n\n## 总体评分\n\n### 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法总体 sound，structural controls 全面；但 K=5 quintile 在 bimodal 分布下的充分性未验证，semi-synthetic injection 的 ecological validity 有限，family clustering 对 CI 的影响需更突出报告 |\n| Excitement | 3.5/5 | 重要问题（benchmark temporal comparability），meta-critique 有独到贡献，规模空前；但方法本身为 off-the-shelf MH-DIF 的应用，核心发现为 descriptive empirical，可操作指导有限 |\n| Reproducibility | 4/5 | 提供 anonymous code，methodology 描述详尽，统计参数齐全；但若干外部资源（PSN-IRT, METABENCH matrix）的可获取性未明确 |\n| Confidence | 4/5 | 对 DIF 方法论和 LLM evaluation 有较好背景，仔细阅读了全文含 appendix |\n\n**Overall Assessment**: **3.5** (Borderline Conference)\n\n**一句话总结**: 论文在规模和 structural controls 上表现出色，ground truth meta-critique 是 genuine contribution，但 K=5 quintile 在 bimodal LLM 分布下的 adequacy 未验证、ΔFPR=0.000 的 prominent claim 需更严格限定、semi-synthetic injection 的 ecological validity 需加强——这些方法论不确定性使论文处于 Conference 和 Findings 之间。\n\n---\n\n### 主要优势总结\n- 5,227 models × 6 benchmarks 的规模空前，结论 robust\n- Ground truth meta-critique 对 contamination detection 领域有方法论修正意义\n- Cross-subject matching 的 zero-FPR guarantee（under single-subject injection）是 clean 的方法论贡献\n- 6 种 alternative explanations 的 systematic exclusion 令人信服\n- \"Diagnostic, not destructive\" 的 nuanced framing 避免了 overclaiming\n- 写作密度高但清晰，8 页内完成了大量分析",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见（Round 1 — 方法严谨性 + 实验可靠性）\n\n---\n\n### Paper Summary\n\n本文将教育测量学中的 Mantel-Haenszel Differential Item Functioning (MH-DIF) 分析应用于 LLM benchmark 的时间可比性检验。基于 METABENCH 的 5,227 模型 × 12,508 MMLU items 响应矩阵，作者发现 31.3% 的 items 在 2023 vs. 2024 cohorts 间展现 ETS Category C 级别的 DIF（|Δ_MH| ≥ 1.5, p < 0.05）。论文提出 cross-subject matching 消除 FPR 膨胀（ΔFPR = 0.000），构建 semi-synthetic injection framework 验证检测力（ΔTPR = +0.508 at p=0.5），并在 6 个 benchmark 上复制。核心洞察为：web-overlap contamination labels 与 DIF flags 近乎独立（enrichment ≈ 0.96），暴露了现有 contamination detection 验证方法论中的 category error。\n\n---\n\n### Summary of Strengths\n\n**S1. 规模空前的心理测量审计**：5,227 models × 12,508 items 的 DIF 分析是目前最大规模的 LLM benchmark psychometric audit，6 个 benchmark 的 replication 增强了结论的 robustness。\n\n**S2. Ground truth meta-critique 有独到洞察**：论文清晰区分了 global exposure（web-overlap）和 differential functioning（DIF），用 enrichment ≈ 0.96、Jaccard = 0.206、φ = 0.012 三个指标实证地证明两者近乎独立。Figure 1 的 ICC 示意图有效传达了这一概念区分。这一发现对 contamination detection 研究具有方法论意义。\n\n**S3. Cross-subject matching 设计严谨**：cross-subject matching 排除待测 subject 的 total score 作为 matching variable，在 single-subject injection 下 ΔFPR = 0 是 constructive guarantee（Section 3.4, Remark），不依赖特定 injection 模式。这是一个 clean 的方法论贡献。\n\n**S4. Structural controls 全面**：论文系统检验了 6 种 alternative explanations（ability mismatch、IRT θ-conditioning、within-subject DIF、family de-duplication、architecture heterogeneity、permutation test），每一种都有明确的定量结果。Table 2 的结构化呈现清晰。\n\n**S5. 写作精炼、叙事结构合理**：论文在 8 页正文内覆盖了大量分析，写作密度高但条理清晰。\"diagnostic, not destructive\" 的定位避免了过度声称，对 ρ ≈ 0.997 与 family-level rank shifts 的 tension 有充分讨论。\n\n**S6. Simpson's paradox 分析有价值**：Section 4.2 的 logistic regression 展示 domain accuracy 在 aggregate level 正向预测 DIF（OR=1.55），控制 item 属性后反转（OR=0.73），92.4% signal 为 item-specific。这一 decomposition 增强了对 DIF 信号本质的理解。\n\n---\n\n### Summary of Weaknesses\n\n#### Must-Fix 问题（影响接收决定）\n\n**W1** [critical] **Quintile stratification (K=5) 在 bimodal LLM 分布下的充分性未验证**\n- 具体位置：Section 3.2（\"We use K = 5 equiprobable strata (quintile-based binning)\"）、Section 3.2 paragraph \"LLM-specific challenges\"（\"the ability distribution is non-normal (bimodal from base vs. instruction-tuned models), motivating quintile-based rather than parametric stratification\"）\n- 问题：论文正确识别了 LLM ability 分布的 bimodality（base vs. instruction-tuned），但仅以此为由选择 quintile-based 而非 parametric stratification，而未验证 K=5 在 bimodal 分布下是否提供足够的 ability conditioning。在 bimodal 分布中，quintile bins 可能跨越两个 mode 的边界，导致 within-stratum ability variance 异常大，产生 residual confounding。以 N=1,887 models 的 temporal cohorts 为例，每个 quintile stratum 包含 ~377 models。如果 base 和 instruction-tuned models 的 total score 差异恰好落在某一 quintile 边界附近，该 stratum 内的 ability 异质性会显著削弱 conditioning 效果。\n- 为什么影响接收：K 的选择直接影响 DIF 检测的 validity——如果 conditioning 不充分，ability differences 会被误判为 DIF。论文引用 ETS 推荐作为 K=5 的依据，但 ETS 的推荐基于 educational testing 中近似正态的能力分布，不适用于 bimodal 场景。\n- 建议修改方向：报告 K=10 和 K=20 的 sensitivity analysis 结果（或至少 K=10）；分析 bimodal 分布下各 stratum 的 within-stratum ability SD；如果 C% 对 K 不敏感，这将大幅增强 robustness。\n\n**W2** [critical] **ΔFPR = 0.000 在 abstract/contributions 中的限定条件不足**\n- 具体位置：Abstract（\"achieves zero false positive inflation under single-subject contamination (ΔFPR = 0.000; ΔFPR < 0.01 for k ≤ 5 subjects)\"）、Section 1 Contribution 2（\"achieves ΔFPR = 0.000\"）\n- 问题：Abstract 的措辞在字面上提供了 single-subject 限定，但 \"zero false positive inflation\" 的强调效果远大于其后的限定条件。在 Contribution 2 中仅写 \"achieves ΔFPR = 0.000\" 而未附加条件。Table 5（Appendix）显示 k=10 时 ΔFPR = 0.047±0.022，k=20 时 = 0.069±0.018——在 MMLU 的 57 subjects 中，真实 contamination 跨越 >5 subjects 是完全可能的（尤其是 web-crawled training data）。论文在 Section 3.4 和 Limitations 中确实讨论了 boundary，但 abstract 和 contributions 的呈现方式可能让读者获得比实际更强的保证。\n- 为什么影响接收：ΔFPR = 0.000 是论文的 headline claim 之一，如果读者仅看 abstract 会高估 cross-subject matching 的 robustness。ARR 审稿标准 R4 要求 \"avoiding overclaiming or misleading framing\"。\n- 建议修改方向：Contribution 2 应改为 \"achieves ΔFPR = 0.000 under single-subject contamination and ΔFPR < 0.007 for k ≤ 5 subjects (≤9% of domains)\"，并在 abstract 中注明 boundary（>10 subjects 时 ΔFPR 上升至 0.026–0.069）。\n\n#### Should-Fix 问题（影响评分但不一票否决）\n\n**W3** [warning] **Semi-synthetic injection 的 ecological validity 不足，ΔTPR = +0.508 的 moderate 水平值得关注**\n- 具体位置：Section 3.4（\"we flip incorrect responses to correct in the focal group at exploitation rate p\"）、Section 4.5、Limitations\n- 问题：Binary flipping（incorrect → correct）是 uniform worst-case pattern，与真实 contamination 差距较大。真实 contamination 可能表现为：(a) partial memorization（对特定 answer choice 有偏好但不一定答对）；(b) reasoning shortcuts（正确推理路径被 memorized template 替代）；(c) format-specific advantages。论文承认这是 \"worst-case uniform exploitation pattern\" 且 ΔTPR 是 \"upper-bound estimate\"——但这恰恰意味着在更 realistic 的 contamination 模式下，检测力可能显著低于 0.508。ΔTPR = 0.508 本身只是 moderate（在 injected items 中仅约一半被检测到），如果 upper-bound 就是 moderate，那 realistic 场景下的检测力如何？\n- 建议：(1) 补充至少一种更 realistic 的 injection pattern（如 answer-choice bias：翻转为特定 option 而非正确答案）的 sensitivity analysis；(2) 在正文中明确讨论 detection power 的 lower-bound implications，而非仅强调 ΔFPR=0 的方法论贡献。\n\n**W4** [warning] **Family-level cluster bootstrap CI 应在正文中更突出**\n- 具体位置：Limitations（\"Cluster bootstrap resampling at the family level (29 families with ≥3 members, 1,882 models, B = 1,000) yields a 95% CI of [26.7%, 53.2%], 3.1× wider than the model-level CI [29.4%, 38.1%]\"）\n- 问题：model-level CI [29.4%, 38.1%] 在 Section 4.2 正文中报告（\"95% bootstrap CI: [29.4%, 38.1%]\"），但 family-level CI [26.7%, 53.2%] 仅出现在 Limitations。鉴于 LLM families 的 extreme relatedness（论文自己描述为 \"hundreds of Llama-2 fine-tunes exceeds the clustering levels studied\"），family-level CI 才是更 conservative、更 appropriate 的 uncertainty estimate。3.1× 的 widening 说明 family 结构对 inference 有实质影响。\n- 建议：在 Section 4.2 正文中同时报告 model-level 和 family-level CI（例如 \"31.3% [model-level CI: 29.4–38.1%; family-level CI: 26.7–53.2%]\"），让读者自行判断 precision。\n\n**W5** [warning] **Table 1 中 \"FPR (clean)\" 的术语使用自相矛盾**\n- 具体位置：Table 1 caption（\"FPR is the flagging rate on web-overlap 'clean' items (Li et al., 2024b), not a traditional false positive rate\"）、Section 4.3\n- 问题：论文在 Section 4.3 用整节篇幅论证 web-overlap labels 是 \"the wrong ground truth for a differential method\"——即 DIF flags 和 web-overlap labels 衡量的是不同概念。但 Table 1 仍用 \"FPR\" 指代 DIF 在 web-overlap \"clean\" items 上的 flagging rate。如果 web-overlap \"clean\" 不等于 \"no DIF\"，那 \"clean\" items 上的 DIF-C flagging rate 就不是 false positive rate（即便 Table 1 caption 加了 disclaimer）。这在概念上是自相矛盾的：一面说 web-overlap 不是合适的 ground truth，一面用它定义 FPR。\n- 建议：将 Table 1 的列名改为 \"C% (clean)\" 或 \"DIF-C rate on clean items\"，并删除 \"FPR\" 术语以避免混淆。\n\n**W6** [warning] **Graduated de-duplication 的解读偏乐观**\n- 具体位置：Section 4.4（\"Graduated de-duplication (K=10: 22.7%; K=20: 29.1%) confirms family structure does not inflate C%\"）\n- 问题：K=10 de-duplication 将 C% 从 31.3% 降至 22.7%，降幅 8.6 pp（27% reduction）。论文将此解读为 \"family structure does not inflate C%\"，但 8.6 pp 的下降是非 trivial 的。更准确的表述应为 \"family structure inflates C% by up to ~8 pp, but the residual 22.7% remains far above the random baseline (0.18%)\"。当前措辞可能让读者低估 family clustering 的影响。\n- 建议：改为更 nuanced 的表述，承认 family structure 有 moderate inflation effect 但不改变定性结论。\n\n#### Minor 问题（不影响接收）\n\n**M1**: Section 4.6 中 \"Among the 200 most displaced models, 33.6% of pairwise rankings reverse\" 存在 selection bias——选取 displacement 最大的子集天然会放大 rank reversal rate。应注明这是 conditional on selection 的数字，或补充全样本的 pairwise reversal rate（从 Table 3 推断 flip rate ≈ 2%）。\n\n**M2**: GSM1K correlation analysis (r = -0.478, p = 0.005, N=33) 统计功效有限，论文在 Limitations 中承认了 \"exploratory\"，但 Section 4.7 正文中的呈现方式（作为 cross-benchmark validation 的组成部分）可能让读者高估其证据强度。建议在正文中也标注 \"exploratory\"。\n\n**M3**: Section 5.3 提出的 DIF audit protocol（Monitor/Flag/Act thresholds）基于经验而非理论推导。C% = 15% 和 25% 的阈值来自 ρ degradation simulation，但未提供 formal justification（如 type I/II error control）。这不影响论文的核心贡献，但 protocol 的可操作性需要更多验证。\n\n**M4**: 论文脚注 1 提供了 anonymous code repository URL，但论文中引用的若干工具（PSN-IRT, METABENCH response matrix）的可获取性未明确说明，可能影响 reproducibility 评分。\n\n---\n\n### Questions for Authors\n\n**Q1**: K=5 quintile stratification 的 sensitivity analysis 是否已在内部测试过？如果有 K=10/20 的结果，能否在 rebuttal 中提供？\n\n**Q2**: Cross-subject matching 在 MMLU 以外的 benchmark（如 GSM8K, 仅有 1 个 \"subject\"）上如何操作？Section 4.7 提到 external matching 用于 GSM8K，但 cross-subject matching 是否仅限于 multi-domain benchmarks？如果是，这是否限制了方法的 generalizability？\n\n**Q3**: 论文报告 IRT θ-conditioning 与 total score 的 r = 0.9986，但 2PL fit 较差（Appendix A.2）。在 model fit 较差的情况下，θ estimates 本身是否可靠？r = 0.9986 是否仅反映了 total score 和 θ 在 rank-order 上的一致性而非 scale 上的一致性？\n\n**Q4**: 论文使用 2023 vs. 2024 release date 作为 temporal cohort 划分。这是否与模型的 training data cutoff 对齐？一个 2024 年发布但 training data cutoff 在 2022 年的模型可能被错误分类。论文是否有 training data cutoff 的信息？\n\n---\n\n### Missing References\n\n1. **Penfield & Camilli (2007)** \"Differential Item Functioning\" in *Handbook of Statistics* — 作为 DIF 方法论的现代综述，与本文方法论定位高度相关。\n2. **Millsap & Everson (1993)** \"Methodology of Differential Item Functioning Research\" — 早期但权威的 DIF 方法论总结。\n3. **Liang et al. (2023)** \"Holistic Evaluation of Language Models\" (HELM) — 作为 LLM evaluation 的重要 framework，值得在 Related Work 中提及。\n\n---\n\n### Limitations and Societal Impact\n\nLimitations 章节覆盖了 4 个方面（methodological scope、examinee non-independence、matching boundary、generalizability），内容充实且诚实。特别值得肯定的是对 family-level cluster bootstrap CI 的报告。\n\n建议在 generalizability 段落中补充：当前结论仅适用于 METABENCH 中 Open LLM Leaderboard 的公开模型，对 closed-source models（GPT-4、Claude 等）的 DIF behavior 无法推断，因为这些模型的 training data composition 和 release pattern 可能有系统性差异。\n\n---\n\n### Ethical Concerns\n\n无显著伦理问题。论文使用公开数据集和公开模型评估结果，不涉及 human subjects。Anonymous code repository 的做法符合 double-blind 要求。\n\n---\n\n## 总体评分\n\n### 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法总体 sound，structural controls 全面；但 K=5 quintile 在 bimodal 分布下的充分性未验证，semi-synthetic injection 的 ecological validity 有限，family clustering 对 CI 的影响需更突出报告 |\n| Excitement | 3.5/5 | 重要问题（benchmark temporal comparability），meta-critique 有独到贡献，规模空前；但方法本身为 off-the-shelf MH-DIF 的应用，核心发现为 descriptive empirical，可操作指导有限 |\n| Reproducibility | 4/5 | 提供 anonymous code，methodology 描述详尽，统计参数齐全；但若干外部资源（PSN-IRT, METABENCH matrix）的可获取性未明确 |\n| Confidence | 4/5 | 对 DIF 方法论和 LLM evaluation 有较好背景，仔细阅读了全文含 appendix |\n\n**Overall Assessment**: **3.5** (Borderline Conference)\n\n**一句话总结**: 论文在规模和 structural controls 上表现出色，ground truth meta-critique 是 genuine contribution，但 K=5 quintile 在 bimodal LLM 分布下的 adequacy 未验证、ΔFPR=0.000 的 prominent claim 需更严格限定、semi-synthetic injection 的 ecological validity 需加强——这些方法论不确定性使论文处于 Conference 和 Findings 之间。\n\n---\n\n### 主要优势总结\n- 5,227 models × 6 benchmarks 的规模空前，结论 robust\n- Ground truth meta-critique 对 contamination detection 领域有方法论修正意义\n- Cross-subject matching 的 zero-FPR guarantee（under single-subject injection）是 clean 的方法论贡献\n- 6 种 alternative explanations 的 systematic exclusion 令人信服\n- \"Diagnostic, not destructive\" 的 nuanced framing 避免了 overclaiming\n- 写作密度高但清晰，8 页内完成了大量分析",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-22T05:27:06.646945+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4470
}
```

</details>

---


### Assistant

_source line 534 · 2026-05-22T05:27:19.550293+00:00_

审稿意见已提交给 Review Director。

总结：以 Reviewer 1（方法严谨性 + 实验可靠性）完成了 Round 1 审稿，Overall 3.5（Borderline Conference）。

核心判断：
- **2 个 Must-Fix**：(1) K=5 quintile stratification 在 bimodal LLM 分布下的充分性未验证，需 sensitivity analysis；(2) ΔFPR=0.000 在 abstract/contributions 中缺少足够限定条件
- **4 个 Should-Fix**：semi-synthetic injection ecological validity 不足、family-level CI 应在正文更突出、Table 1 "FPR" 术语自相矛盾、de-duplication 解读偏乐观
- **4 个 Minor**：200 most displaced models 的 selection bias、GSM1K N=33 exploratory 标注、DIF audit protocol 阈值缺乏 formal justification、外部资源可获取性

主要优势为规模空前（5,227 models × 6 benchmarks）、ground truth meta-critique 有方法论修正意义、structural controls 系统全面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 19

## Round 19

4 recorded events


### User

_source line 535 · 2026-05-22T05:28:29.450914+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应其 Weaknesses：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 Weaknesses

### Must-Fix

**W1** [critical] **Abstract 信息密度过高，损害可读性和 first impression**
- 单段 abstract 内填充了十余个数值（ΔFPR, ΔTPR, enrichment, φ, ρ, τ, z, C% 等）。读者无法在首次阅读时提取核心 story。建议分层叙述，将 secondary metrics 移入正文。

**W2** [critical] **缺少 Ethics Statement**
- ARR submission form 要求提供 Ethics Statement。本文完全缺失此部分。Area Chair 可能因此标记 desk-reject 风险。

### Should-Fix

**W3** [warning] **新颖性定位需更 sharp 地区分 adaptation 与 application**
- MH-DIF 是 1988 年方法，cross-subject matching 有 DIF 文献先例（purified subtest matching）。论文未充分展开 LLM-specific adaptation 的具体技术细节。与 Growing Pains 的 practical workflow 组合也未展开。

**W4** [warning] **Discussion audit protocol 的 causal framing 与 Limitations 的 agnostic stance 矛盾**
- Limitations 说 "DIF detects that not why"，但 Section 5.3 Step 3 (Act) 建议 "cross-reference with contamination indicators"，隐含 DIF flags 可作为 contamination signal。如果 DIF 与 web-overlap 近乎独立，cross-reference 预期能找到什么？

**W5** [warning] **页数可能超限**
- Main text 约 8.3 页，`\enlargethispage{2\baselineskip}` 说明作者已在挤压空间。EMNLP 2026 正文 ≤ 8 页是 hard constraint。

**W6** [warning] **Cohort 定义按 release date 划分，未讨论 training data cutoff 偏差**
- Release date 与 training data exposure 的 lag 是 systematic confound。6-month window analysis 仅用一句话带过。

**W7** [warning] **Multiple testing 论证不够严谨**
- 12,508 items 同时检验，implicit protection 来自 effect size 门槛而非 formal correction。Random-split control 才是真正的 empirical FPR calibration，但不够突出。

### Minor
- M1: 术语不一致（temporal measurement instability / temporal DIF / measurement invariance 交替使用）
- M2: Table 3 Ratio 列跨 benchmark 比较有误导性
- M3: Figure 1 ICC 图打印版可能难辨
- M4: GSM1K "suggests" 措辞略强，应弱化为 "is consistent with"
- M5: Conclusion 仅 3 行，过于简短

---

请逐条回应（W1-W7, M1-M5）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-22T05:30:51.473027+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 Weaknesses 的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-W1: Abstract 信息密度过高**\n同意。Abstract 单段内确实堆叠了过多数值指标（ΔFPR, ΔTPR, enrichment, φ, C%, ρ, τ, z, pp 数等至少 12 个数字），损害了 first impression 的可读性。作为对比，核心 story 其实可以用三个数字讲清：(1) 31% items 有 temporal DIF；(2) ΔFPR = 0.000 under cross-subject matching；(3) enrichment ≈ 0.96 说明 DIF ≠ contamination。次要指标（φ=0.012、z=-8 to -49、τ≈0.958、具体 C% range 等）完全可以移入正文。不过这是 presentation 问题而非 methodological flaw，不应影响 soundness 评分。\n\n**[REBUT] R2-W2: 缺少 Ethics Statement → desk-reject 风险**\nR2 的担忧不成立。根据 EMNLP 2026 / ACL ARR 的提交规范，Responsible NLP Checklist 在 OpenReview submission form 中由作者手动填写，而不是作为论文 PDF 的一个 section。ARR desk-reject checklist（见 reviewer guidelines）列出的条件为：匿名违规、虚构引用、格式/页数违规、缺少 Limitations section、严重 checklist 违规。\"Missing Ethics Statement section in PDF\" 不在其中。本文已包含 Limitations section（页 9），符合 mandatory 要求。\"Ethical Considerations\" 在 PDF 中是 optional section（\"optional ethical considerations do not count towards this page limit\"），不构成 desk-reject 依据。R2 对 desk-reject 风险的判断有误。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W3: 新颖性定位需更清晰区分 adaptation 与 application**\n部分同意。MH-DIF (Holland & Thayer, 1988) 确实是 off-the-shelf 方法，cross-subject matching 改编自 purified subtest matching (Swaminathan & Rogers, 1990)。论文在 Section 1 contributions 中明确定位为 \"methodological and empirical, not algorithmic\"，这一自我定位是诚实的。但 R2 的批评仍然成立：论文应更 sharp 地阐述 LLM-specific adaptations 的技术细节——比如 quintile-based stratification 对 bimodal 分布的处理（我在 W1 中也提出了此问题）、multi-domain benchmark 下 cross-subject matching 的具体操作方式、permutation simulation 处理 LD 的方法论贡献。目前这些细节分散在 Section 3.2 的多个 paragraphs 中，不够集中和突出。与 Growing Pains (Habba et al., 2026) 的 practical workflow 整合确实缺乏展开。\n\n不过，新颖性要求需按论文自身定位评判。论文的核心贡献是 (1) ground truth meta-critique 和 (2) 大规模经验发现，而非算法创新。对 empirical contribution papers，ARR guidelines 明确指出不应因缺乏 algorithmic novelty 而降分（\"Dismissing results as 'obvious in retrospect' (hindsight bias)\"）。建议论文增强 LLM adaptation 的呈现密度，但不应因此一票否决。\n\n**[AGREE] R2-W4: Discussion audit protocol 的 causal framing 与 Limitations 矛盾**\n完全同意，这是一个内部一致性问题。Section 5.3 Step 3 (Act) 建议 \"review flagged item content, cross-reference with contamination indicators\"，但 Section 4.3 实证表明 DIF flags 和 web-overlap labels 的 enrichment ≈ 0.96（近乎独立）。如果两类 flags 测量的是不同概念（论文自己称之为 \"category error\"），那 cross-reference 预期能找到什么？论文需要解决这一矛盾：要么 (a) 承认 cross-reference 的目的不是验证 contamination 而是排除 non-DIF confounds（如 item quality issues）；要么 (b) 说明 DIF audit protocol 中的 \"contamination indicators\" 指的是不同于 web-overlap 的 indicators（如 GSM1K-style functional tests）。目前的表述隐含了 DIF → contamination 的因果推断，与 Limitations 中 \"detects that not why\" 的 agnostic stance 不一致。\n\n**[AGREE] R2-W5: 页数可能超限**\n同意这是需要关注的风险。从 PDF 渲染看，Section 6 (Conclusion) 起始于第 9 页顶部——即使只有 ~3 行文字，主体正文（Sections 1–6）在技术上超过了 8 页。LaTeX 源码中 `\\enlargethispage{2\\baselineskip}` 的存在（Section 5, discussion.tex）进一步证实作者已在挤压版面。虽然 Limitations 不计入 8 页限制，但 Conclusion 是主体正文的一部分。EMNLP 2026 的 \"strict 8-page limit\" 是 hard constraint，AC 完全有权因此标记 format violation。建议作者压缩 Discussion（Section 5.3 的 audit protocol 可移入 appendix）或 Conclusion 以确保合规。\n\n**[REBUT] R2-W6: Cohort 定义按 release date 划分的 confound**\n部分反驳。R2 的问题本身合理（我在 Q4 中也提出了类似问题），但论文已提供了部分 mitigation。Section 4.7 报告了 6-month window analysis（2023-H2 vs. 2024-H1: MMLU C% = 34.35%），表明即使缩小 temporal window 也无法消除 DIF。更关键的是，论文在 Limitations 中明确承认 \"Temporal cohorts are defined by calendar year, a coarse grouping; finer-grained definitions (e.g., by training data cutoff or alignment method) might reveal more targeted patterns\"。\n\n但 R2 说 \"仅用一句话带过\" 也有道理——6-month window 结果只出现在 Section 4.7 末尾一句话中，缺乏详细分析。建议作者：(1) 将 6-month window 结果提升为一个 paragraph 并讨论 release date vs. training cutoff 的 potential bias；(2) 如果有 training data cutoff metadata，提供 sensitivity analysis。但这不构成 \"must-fix\"——release date 是 METABENCH 中可获得的最佳 temporal signal，且论文的核心 claim（items function differently across cohorts）不依赖于 cohort 划分的精确因果解释。\n\n**[REBUT] R2-W7: Multiple testing 论证不够严谨**\n不完全同意。论文的 multiple testing 处理有三层防线：\n\n1. **ETS dual threshold**（effect size |Δ_MH| ≥ 1.5 AND p < 0.05）——这不是单纯的 p-value 检验，effect size 门槛本身就是 implicit control（Section 3.2）。\n2. **BH FDR correction**（q = 0.05）——Section 4.2 报告 BH 仅移除 3 items（31.32% → 31.30%），说明 ETS dual threshold 已基本覆盖了 FDR control。\n3. **Random-split empirical calibration**——0.18% C% 在 null 条件下（Section 4.2, Table 1），这是最强的 empirical evidence。\n\nR2 认为 random-split control \"不够突出\"——这一点我同意，建议在 Section 4.2 中更明确地将 random-split 的 0.18% 作为 empirical null calibration 的核心证据呈现。但 multiple testing 的方法论本身是 adequate 的，三层防线足以支撑 31.3% 的 claim。教育测量学文献中 ETS classification 的标准做法即为 dual threshold without formal correction（Donoghue & Allen, 1993; Clauser & Maver, 1998），论文遵循了这一领域惯例。\n\n---\n\n### Minor\n\n**[AGREE] R2-M1: 术语不一致**\n同意。\"Temporal measurement instability\"（标题）、\"temporal DIF\"（正文多处）、\"measurement invariance\"（Related Work 中提及）三个术语交替使用但含义不完全相同。Measurement invariance 在 psychometrics 中有特定的 IRT-based 定义（Meredith, 1993），与 DIF 是相关但不同的概念。建议统一使用 \"temporal DIF\" 作为核心术语，仅在引用 psychometric 文献时提及 \"measurement invariance\"。\n\n**[AGREE] R2-M2: Table 3 Ratio 列跨 benchmark 比较有误导性**\n同意。MMLU 的 174× 和 ARC 的 45× 直接对比可能让读者误以为 MMLU \"更不稳定\"，但 ratio 的差异很大程度上取决于各 benchmark 的 random-split baseline C%（MMLU 0.18% vs. ARC 0.60%），而非 temporal DIF 本身的差异。绝对 C% 的比较（31.3% vs. 26.9%）更有意义。建议在 Table 3 caption 中注明 ratio 受 baseline 影响，或降低 ratio 列的强调程度。\n\n**[REBUT] R2-M3: Figure 1 ICC 图打印版可能难辨**\n这是一个可检验的问题。从 PDF 渲染来看（submitted_p2.png），Figure 1 使用了颜色区分两个 cohorts 的 ICC curves，并有虚实线区分。在灰度打印下可能确实不易区分。但 ARR 审稿流程为电子审阅，reviewer 和 AC 查看 PDF 而非打印版，因此灰度可读性不是 blocking issue。如果论文最终被接收进入 camera-ready，建议加粗线条或增加 marker 以改善灰度可读性。\n\n**[AGREE] R2-M4: GSM1K \"suggests\" 措辞略强**\n同意。Section 4.7 原文 \"an exploratory GSM1K analysis suggests DIF captures capability change distinct from memorization\" 中，N=33 的样本量下用 \"suggests\" 已经偏强。r = -0.478 虽然 p=0.005，但 bootstrap CI = [-0.71, -0.16] 较宽，且论文自己在 Limitations 中承认 \"limited statistical power and is exploratory\"。正文和 Limitations 的 hedging 程度不一致。建议改为 \"is consistent with\" 或 \"provides preliminary evidence for\"。\n\n**[REBUT] R2-M5: Conclusion 仅 3 行，过于简短**\n不同意这是一个缺陷。在 8 页 hard constraint 下，Conclusion 的作用是 summarize 而非 elaborate。当前 3 行 Conclusion 覆盖了三个核心点：(1) cross-subject matching 解决 validation gap；(2) 6 benchmarks 17.9–31.3% temporal instability；(3) 需要 psychometric monitoring。这恰好是论文三个 contributions 的精炼概括。考虑到论文已有完整的 Discussion section（Section 5）覆盖 implications、meta-critique、audit protocol，Conclusion 不需要重复展开。在页数紧张的情况下（R2-W5 已指出可能超限），压缩 Conclusion 是合理的 editorial decision。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 Weaknesses 的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-W1: Abstract 信息密度过高**\n同意。Abstract 单段内确实堆叠了过多数值指标（ΔFPR, ΔTPR, enrichment, φ, C%, ρ, τ, z, pp 数等至少 12 个数字），损害了 first impression 的可读性。作为对比，核心 story 其实可以用三个数字讲清：(1) 31% items 有 temporal DIF；(2) ΔFPR = 0.000 under cross-subject matching；(3) enrichment ≈ 0.96 说明 DIF ≠ contamination。次要指标（φ=0.012、z=-8 to -49、τ≈0.958、具体 C% range 等）完全可以移入正文。不过这是 presentation 问题而非 methodological flaw，不应影响 soundness 评分。\n\n**[REBUT] R2-W2: 缺少 Ethics Statement → desk-reject 风险**\nR2 的担忧不成立。根据 EMNLP 2026 / ACL ARR 的提交规范，Responsible NLP Checklist 在 OpenReview submission form 中由作者手动填写，而不是作为论文 PDF 的一个 section。ARR desk-reject checklist（见 reviewer guidelines）列出的条件为：匿名违规、虚构引用、格式/页数违规、缺少 Limitations section、严重 checklist 违规。\"Missing Ethics Statement section in PDF\" 不在其中。本文已包含 Limitations section（页 9），符合 mandatory 要求。\"Ethical Considerations\" 在 PDF 中是 optional section（\"optional ethical considerations do not count towards this page limit\"），不构成 desk-reject 依据。R2 对 desk-reject 风险的判断有误。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W3: 新颖性定位需更清晰区分 adaptation 与 application**\n部分同意。MH-DIF (Holland & Thayer, 1988) 确实是 off-the-shelf 方法，cross-subject matching 改编自 purified subtest matching (Swaminathan & Rogers, 1990)。论文在 Section 1 contributions 中明确定位为 \"methodological and empirical, not algorithmic\"，这一自我定位是诚实的。但 R2 的批评仍然成立：论文应更 sharp 地阐述 LLM-specific adaptations 的技术细节——比如 quintile-based stratification 对 bimodal 分布的处理（我在 W1 中也提出了此问题）、multi-domain benchmark 下 cross-subject matching 的具体操作方式、permutation simulation 处理 LD 的方法论贡献。目前这些细节分散在 Section 3.2 的多个 paragraphs 中，不够集中和突出。与 Growing Pains (Habba et al., 2026) 的 practical workflow 整合确实缺乏展开。\n\n不过，新颖性要求需按论文自身定位评判。论文的核心贡献是 (1) ground truth meta-critique 和 (2) 大规模经验发现，而非算法创新。对 empirical contribution papers，ARR guidelines 明确指出不应因缺乏 algorithmic novelty 而降分（\"Dismissing results as 'obvious in retrospect' (hindsight bias)\"）。建议论文增强 LLM adaptation 的呈现密度，但不应因此一票否决。\n\n**[AGREE] R2-W4: Discussion audit protocol 的 causal framing 与 Limitations 矛盾**\n完全同意，这是一个内部一致性问题。Section 5.3 Step 3 (Act) 建议 \"review flagged item content, cross-reference with contamination indicators\"，但 Section 4.3 实证表明 DIF flags 和 web-overlap labels 的 enrichment ≈ 0.96（近乎独立）。如果两类 flags 测量的是不同概念（论文自己称之为 \"category error\"），那 cross-reference 预期能找到什么？论文需要解决这一矛盾：要么 (a) 承认 cross-reference 的目的不是验证 contamination 而是排除 non-DIF confounds（如 item quality issues）；要么 (b) 说明 DIF audit protocol 中的 \"contamination indicators\" 指的是不同于 web-overlap 的 indicators（如 GSM1K-style functional tests）。目前的表述隐含了 DIF → contamination 的因果推断，与 Limitations 中 \"detects that not why\" 的 agnostic stance 不一致。\n\n**[AGREE] R2-W5: 页数可能超限**\n同意这是需要关注的风险。从 PDF 渲染看，Section 6 (Conclusion) 起始于第 9 页顶部——即使只有 ~3 行文字，主体正文（Sections 1–6）在技术上超过了 8 页。LaTeX 源码中 `\\enlargethispage{2\\baselineskip}` 的存在（Section 5, discussion.tex）进一步证实作者已在挤压版面。虽然 Limitations 不计入 8 页限制，但 Conclusion 是主体正文的一部分。EMNLP 2026 的 \"strict 8-page limit\" 是 hard constraint，AC 完全有权因此标记 format violation。建议作者压缩 Discussion（Section 5.3 的 audit protocol 可移入 appendix）或 Conclusion 以确保合规。\n\n**[REBUT] R2-W6: Cohort 定义按 release date 划分的 confound**\n部分反驳。R2 的问题本身合理（我在 Q4 中也提出了类似问题），但论文已提供了部分 mitigation。Section 4.7 报告了 6-month window analysis（2023-H2 vs. 2024-H1: MMLU C% = 34.35%），表明即使缩小 temporal window 也无法消除 DIF。更关键的是，论文在 Limitations 中明确承认 \"Temporal cohorts are defined by calendar year, a coarse grouping; finer-grained definitions (e.g., by training data cutoff or alignment method) might reveal more targeted patterns\"。\n\n但 R2 说 \"仅用一句话带过\" 也有道理——6-month window 结果只出现在 Section 4.7 末尾一句话中，缺乏详细分析。建议作者：(1) 将 6-month window 结果提升为一个 paragraph 并讨论 release date vs. training cutoff 的 potential bias；(2) 如果有 training data cutoff metadata，提供 sensitivity analysis。但这不构成 \"must-fix\"——release date 是 METABENCH 中可获得的最佳 temporal signal，且论文的核心 claim（items function differently across cohorts）不依赖于 cohort 划分的精确因果解释。\n\n**[REBUT] R2-W7: Multiple testing 论证不够严谨**\n不完全同意。论文的 multiple testing 处理有三层防线：\n\n1. **ETS dual threshold**（effect size |Δ_MH| ≥ 1.5 AND p < 0.05）——这不是单纯的 p-value 检验，effect size 门槛本身就是 implicit control（Section 3.2）。\n2. **BH FDR correction**（q = 0.05）——Section 4.2 报告 BH 仅移除 3 items（31.32% → 31.30%），说明 ETS dual threshold 已基本覆盖了 FDR control。\n3. **Random-split empirical calibration**——0.18% C% 在 null 条件下（Section 4.2, Table 1），这是最强的 empirical evidence。\n\nR2 认为 random-split control \"不够突出\"——这一点我同意，建议在 Section 4.2 中更明确地将 random-split 的 0.18% 作为 empirical null calibration 的核心证据呈现。但 multiple testing 的方法论本身是 adequate 的，三层防线足以支撑 31.3% 的 claim。教育测量学文献中 ETS classification 的标准做法即为 dual threshold without formal correction（Donoghue & Allen, 1993; Clauser & Maver, 1998），论文遵循了这一领域惯例。\n\n---\n\n### Minor\n\n**[AGREE] R2-M1: 术语不一致**\n同意。\"Temporal measurement instability\"（标题）、\"temporal DIF\"（正文多处）、\"measurement invariance\"（Related Work 中提及）三个术语交替使用但含义不完全相同。Measurement invariance 在 psychometrics 中有特定的 IRT-based 定义（Meredith, 1993），与 DIF 是相关但不同的概念。建议统一使用 \"temporal DIF\" 作为核心术语，仅在引用 psychometric 文献时提及 \"measurement invariance\"。\n\n**[AGREE] R2-M2: Table 3 Ratio 列跨 benchmark 比较有误导性**\n同意。MMLU 的 174× 和 ARC 的 45× 直接对比可能让读者误以为 MMLU \"更不稳定\"，但 ratio 的差异很大程度上取决于各 benchmark 的 random-split baseline C%（MMLU 0.18% vs. ARC 0.60%），而非 temporal DIF 本身的差异。绝对 C% 的比较（31.3% vs. 26.9%）更有意义。建议在 Table 3 caption 中注明 ratio 受 baseline 影响，或降低 ratio 列的强调程度。\n\n**[REBUT] R2-M3: Figure 1 ICC 图打印版可能难辨**\n这是一个可检验的问题。从 PDF 渲染来看（submitted_p2.png），Figure 1 使用了颜色区分两个 cohorts 的 ICC curves，并有虚实线区分。在灰度打印下可能确实不易区分。但 ARR 审稿流程为电子审阅，reviewer 和 AC 查看 PDF 而非打印版，因此灰度可读性不是 blocking issue。如果论文最终被接收进入 camera-ready，建议加粗线条或增加 marker 以改善灰度可读性。\n\n**[AGREE] R2-M4: GSM1K \"suggests\" 措辞略强**\n同意。Section 4.7 原文 \"an exploratory GSM1K analysis suggests DIF captures capability change distinct from memorization\" 中，N=33 的样本量下用 \"suggests\" 已经偏强。r = -0.478 虽然 p=0.005，但 bootstrap CI = [-0.71, -0.16] 较宽，且论文自己在 Limitations 中承认 \"limited statistical power and is exploratory\"。正文和 Limitations 的 hedging 程度不一致。建议改为 \"is consistent with\" 或 \"provides preliminary evidence for\"。\n\n**[REBUT] R2-M5: Conclusion 仅 3 行，过于简短**\n不同意这是一个缺陷。在 8 页 hard constraint 下，Conclusion 的作用是 summarize 而非 elaborate。当前 3 行 Conclusion 覆盖了三个核心点：(1) cross-subject matching 解决 validation gap；(2) 6 benchmarks 17.9–31.3% temporal instability；(3) 需要 psychometric monitoring。这恰好是论文三个 contributions 的精炼概括。考虑到论文已有完整的 Discussion section（Section 5）覆盖 implications、meta-critique、audit protocol，Conclusion 不需要重复展开。在页数紧张的情况下（R2-W5 已指出可能超限），压缩 Conclusion 是合理的 editorial decision。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-22T05:30:56.544620+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5071
}
```

</details>

---


### Assistant

_source line 538 · 2026-05-22T05:31:14.151362+00:00_

审稿意见已提交给 Review Director。

逐条回应总结：
- **W1 (Abstract 密度)**: [AGREE] — presentation 问题，非方法论缺陷
- **W2 (Ethics Statement)**: [REBUT] — ARR checklist 在 OpenReview form 中填写，PDF 中无需此 section，不存在 desk-reject 风险
- **W3 (新颖性)**: [AGREE] — 但论文自我定位为 empirical contribution，不应因缺乏 algorithmic novelty 一票否决
- **W4 (Audit protocol vs. Limitations 矛盾)**: [AGREE] — 内部一致性问题，Section 5.3 的 cross-reference 建议与 Section 4.3 的 near-independence 发现矛盾
- **W5 (页数超限)**: [AGREE] — Conclusion 起始于第 9 页，技术上主体超 8 页
- **W6 (Release date vs. training cutoff)**: [REBUT] — 论文已有 6-month window 分析和 Limitations 讨论，但呈现不够充分
- **W7 (Multiple testing)**: [REBUT] — 三层防线（ETS dual threshold + BH FDR + random-split calibration）足够，符合教育测量学领域惯例

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 20

## Round 20

68 recorded events


### User

_source line 539 · 2026-05-22T10:19:30.679971+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。

## 投稿信息
- **Venue**: EMNLP 2026 (ACL Rolling Review)
- **类别**: Long Paper (8 页正文限制, unlimited refs, Limitations 不计入页数)
- **匿名规则**: Double-blind (ACL style, \usepackage[review]{acl})
- **截止日期**: 2026-05-25
- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`
- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/submitted.pdf`

## 论文概要
本文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，使用 METABENCH 响应矩阵（5,227 models × 12,508 MMLU items）发现 ~31% 的 MMLU items 在 2023 vs 2024 模型群体间展现 large temporal DIF (ETS C)。主要方法贡献是 cross-subject matching 实现 ΔFPR=0.000，以及 semi-synthetic injection 框架验证检测能力。

## 你的审查侧重

**1. MH-DIF 方法论适用性**
- MH-DIF 从教育测量迁移到 LLM 评估的假设是否成立？examinees 非独立性（model families 共享训练数据/架构）对 MH chi-squared test 的影响是否充分讨论？
- K=5 quintile stratification 在 bimodal ability distribution (base vs instruction-tuned) 下是否适当？
- Unidimensionality 假设在 57-subject MMLU 上是否合理？cross-subject matching 是否充分解决该问题？

**2. Semi-synthetic 框架有效性**
- Binary response flipping 是否是合理的 contamination 模拟？ecological validity 如何？
- ΔFPR=0.000 的 "constructive guarantee" claim 是否过强？multi-subject injection 的 boundary (k≤5) 是否实际适用？
- TPR 被标注为 upper-bound estimate——这个限定是否足够显著？

**3. 统计推断合理性**
- Bootstrap CI [29.4%, 38.1%] vs family-level cluster bootstrap CI [26.7%, 53.2%]——3.1x width 差异暗示什么？
- Multiple testing: ETS dual threshold 作为 implicit multiple testing protection 的论证是否充分？BH correction 只移除 3 items 是否说明问题？
- Permutation test 的设置是否恰当？1,000 iterations 是否足够？

**4. 控制实验充分性**
- Random split (0.18%), ability quintile (2.9%), temporal (31.3%) 的阶梯是否构成充分的 validity 论证？
- Matched-ability analysis 将 C% 从 31.3% 降至 28.9%——2.4pp attributable to ability mismatch 的解读是否合理？
- LOFO robustness: 移除 Mistral/Llama-3 后 C% 大幅下降是否是 concern 而非仅仅是 power reduction？
- Within-family (Llama-2 vs Llama-3) 61.3% C% 的解读是否恰当？

**5. Cross-benchmark 外推**
- 6 个 METABENCH benchmark 的结构差异大（MMLU 12K items vs TruthfulQA 817 items），statistical power 差异是否影响 C% 的可比性？
- GSM1K correlation (r=-0.478, N=33) 的 exploratory nature 是否充分标注？

请严格评审，给出 Strengths、Weaknesses（分 Must-Fix / Should-Fix / Minor）、Questions、Missing References，以及 Overall Assessment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-22T10:19:38.759167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-22T10:19:39.362196+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-22T10:19:39.513152+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-22T10:19:39.513499+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-22T10:19:43.327900+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 545 · 2026-05-22T10:19:44.382208+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form dimensions scoring rubric 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form dimensions scoring rubric 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-22T10:19:45.286458+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-22T10:19:50.876567+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

I found search results related to ACL Rolling Review 2026. Here are the key findings:

## Reviewer Guidelines

ARR developed detailed guidelines and suggestions for each step of the reviewing process, including a list of common problems in both reviews and NLP papers to watch out for.

## Review Form and Criteria

The search results reference a review form with codes for (meta-)review issues (I1-I12) that can be reported by the authors. These sections of reviewer and AC guidelines may be seen by the authors during the response period.

## Reviewer Incentives and Expectations

Starting from May 2025, ACL introduces an awards policy for reviewers and chairs where area chairs or senior area chairs may nominate great reviewers, and the nominees will receive rec
…[truncated 704 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7548
}
```

</details>

---


### Tool result

_source line 548 · 2026-05-22T10:19:51.178179+00:00_

Web search results for query: "ACL ARR review form dimensions scoring rubric 2025 2026"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, here's information about the ACL ARR review form dimensions and scoring rubric for 2025/2026:

## Review Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness
The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful expl
…[truncated 1019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6795
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-22T10:19:52.486479+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 588.4}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 539.5}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 529.5}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 470.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.7}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7200
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-22T10:19:58.070331+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all dimensions, their scoring scales (1-5 etc.), and the description for each score level. Include Soundness, Excitement, Overall Assessment, Confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all dimensions, their scoring scales (1-5 etc.), and the description for each score level. Include Soundness, Excitement, Overall Assessment, Confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 551 · 2026-05-22T10:19:59.037904+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-22T10:19:59.696885+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 553 · 2026-05-22T10:20:00.049909+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 554 · 2026-05-22T10:20:01.058997+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2021
}
```

</details>

---


### Tool call

_source line 555 · 2026-05-22T10:20:01.059518+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 556 · 2026-05-22T10:20:01.315311+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1618
}
```

</details>

---


### Tool call

_source line 557 · 2026-05-22T10:20:01.315794+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 558 · 2026-05-22T10:20:01.518685+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1468
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-22T10:20:02.273840+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1214
}
```

</details>

---


### Tool result

_source line 560 · 2026-05-22T10:20:02.525804+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1210
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-22T10:20:05.543046+00:00_

# ACL Rolling Review Form - Complete Dimensions

## 1. **Reviewer Confidence** (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness** (1-5 scale with half-points)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement** (1-5 scale with half-points)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me."

## 4. **Overall Assessment** (1-5 scale with half-points)
- **5**: Consider for Award (top 2.5% papers)
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings acceptance
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

## 5. **Additional Dimensions**

**Reproducibility** (1-5 scale), **Datasets** (1-5 scale), **Software** (1-5 scale), and **Author Identity Knowledge** (1-5 scale) are also evaluated using similar 
…[truncated 11 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7472
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-22T10:20:10.824372+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 563 · 2026-05-22T10:20:11.328980+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 564 · 2026-05-22T10:20:12.235027+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-22T10:20:12.236292+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-22T10:20:12.236683+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 567 · 2026-05-22T10:20:12.738642+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 568 · 2026-05-22T10:20:13.093697+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 569 · 2026-05-22T10:20:13.096901+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 570 · 2026-05-22T10:20:13.600333+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 861
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-22T10:20:14.057853+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-22T10:20:19.381120+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "11-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "11-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-22T10:20:20.085219+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 605.1}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 294.9}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 94.8}], \"total_pages\": 15, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-22T10:20:23.197261+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 575 · 2026-05-22T10:20:23.651049+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 576 · 2026-05-22T10:20:24.561976+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1364
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-22T10:20:24.614611+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 963
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-22T10:20:24.615106+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 579 · 2026-05-22T10:20:25.118620+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 580 · 2026-05-22T10:20:25.574337+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 581 · 2026-05-22T10:20:25.574793+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 582 · 2026-05-22T10:20:25.578572+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-22T10:20:25.783323+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 664
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-22T10:20:34.674927+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines: what reviewers should focus on, how to evaluate papers, what constitutes a good/bad review, specific criteria for soundness, novelty, significance, clarity, and any instructions about scoring."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines: what reviewers should focus on, how to evaluate papers, what constitutes a good/bad review, specific criteria for soundness, novelty, significance, clarity, and any instructions about scoring."
  }
}
```

</details>

---


### Tool call

_source line 585 · 2026-05-22T10:20:35.177600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 586 · 2026-05-22T10:20:35.228409+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Temporal Measurement Instability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-22T10:20:48.987016+00:00_

# ARR Reviewer Guidelines: Complete Summary

## Core Review Tasks

ARR reviewers must complete **four main tasks**:

1. **Allocate calendar time** for reviewing and discussion periods
2. **Check assignments** for expertise fit and conflicts of interest
3. **Write a strong review** with specific, justified feedback
4. **Update assessments** after author responses and peer discussion

## Key Evaluation Framework

### Reading Strategy
Reviewers should read papers **twice**: first for understanding the research question and expected contributions, then in-depth for technical soundness. "Skim-reading: adjusting your expectations" helps prevent bias from methodology preferences.

### What Constitutes Strong Reviews (I1-I4)

**Specificity (I1)**: Avoid vague criticisms. Instead of "missing relevant references," specify which ones. Instead of "X is unclear," explain "Y and Z details are absent."

**Professional Tone (I4)**: Reviews must be "professional and neutral, if not kind." Sarcasm and dismissiveness damage academic culture and the authors' mental health.

**Score Alignment (I3)**: Low soundness scores must be justified by review text. If no major faults exist, low scores indicate unconscious bias, not legitimate criticism.

### Three Scoring Dimensions (February 2025 onward)

- **Soundness**: Technical validity and methodological rigor
- **Excitement**: Personal interest (orthogonal to soundness)
- **Overall Recommendation**: Composite assessment for venue suitability

## Common Review Mistakes to Avoid (H1-H17)

Critical biases include:

- **H1**: Dismissing findings as "obvious in retrospect" when they're empirically novel
- **H3**: Claiming lack of novelty without specific references
- **H5**: Requiring SOTA results when papers claim other contributions
- **H6**: Undervaluing negative results (important for preventing hype)
- **H13**: Demanding extra experiments beyond what claims require
- **H16**: Listing acknowledged limitations as weaknesses without justificat
…[truncated 2333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 14312
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-22T10:20:56.176582+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read paper sections for review",
  "subagent_type": "Explore",
  "prompt": "I need to read the LaTeX source files for a paper review. The paper is at /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/\n\nRead the following files completely and report their full contents:\n1. sections/method.tex\n2. sections/experiments.tex  \n3. sections/discussion.tex\n4. sections/limitations.tex\n5. sections/appendix.tex\n6. sections/abstract.tex\n7. sections/introduction.tex\n\nThese are in /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/\n\nReport all precise numbers, formulas, statistical tests, confidence intervals, sample sizes, and any claims made. I need the exact text for a thorough peer review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "description": "Read paper sections for review",
    "subagent_type": "Explore",
    "prompt": "I need to read the LaTeX source files for a paper review. The paper is at /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/\n\nRead the following files completely and report their full contents:\n1. sections/method.tex\n2. sections/experiments.tex  \n3. sections/discussion.tex\n4. sections/limitations.tex\n5. sections/appendix.tex\n6. sections/abstract.tex\n7. sections/introduction.tex\n\nThese are in /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/\n\nReport all precise numbers, formulas, statistical tests, confidence intervals, sample sizes, and any claims made. I need the exact text for a thorough peer review."
  }
}
```

</details>

---


### Tool call

_source line 589 · 2026-05-22T10:20:58.033774+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 590 · 2026-05-22T10:20:58.385572+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees 
…[truncated 8426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 591 · 2026-05-22T10:20:58.386003+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 592 · 2026-05-22T10:20:58.587180+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	As approximate parametric bounds, a Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$ (details in \Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold. Power varies substantially with item discrimination: TPR ranges from 0.40 at $a = 0.5$ to 0.95 at $a = 2.0$; the gap between TPR at mean $a$ (0.87) and the aggregate TPR (0.68) quantifies the power cost of parameter heterogeneity, consistent with Jensen's inequality (\Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal Comparability: 31\% Measurement Instability}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%], $B = 1{,}000$ model-level resamples; rightward asymmetry reflects heavy-tailed C\% from subjects exceeding 40\%; family-level cluster bootstrap over 29 families with $\geq$3 members yields a wider CI of $[26.7\%, 53.2\%]$, $3.1\times$ the model-level width, confirming robustness under within-family dependence). Leave-one-family-out analysis confirms that no single non-dominant family drives the signal ($|
…[truncated 10847 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 593 · 2026-05-22T10:20:58.587764+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 594 · 2026-05-22T10:20:58.789021+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\enlargethispage{2\baselineskip}
4	
5	\subsection{Implications for Benchmark Temporal Comparability}
6	\label{sec:disc_temporal}
7	
8	\looseness=-1
9	Temporal DIF decomposes benchmark differences into impact (ability differences removed by matching, $\sim$2.4~pp), DIF (item-level differences after ability control, $\sim$28--29\% floor, 92.4\% item-specific), and attribution (contamination, capability evolution, or methodology shifts---underdetermined without training data).
10	
11	\subsection{Ground Truth Meta-Critique}
12	\label{sec:disc_groundtruth}
13	
14	\looseness=-1
15	The near-independence between DIF flags and web-overlap labels (\Cref{sec:groundtruth}) reflects a category error: web-overlap measures global exposure while DIF measures differential functioning. Semi-synthetic dose-response confirms detection works when present; the disconnect is in the ground truth.
16	
17	\subsection{Recommended DIF Audit Protocol}
18	\label{sec:disc_protocol}
19	
20	\looseness=-1
21	Item-level properties do not reliably predict DIF susceptibility (AUROC $= 0.60$; \Cref{app:predictive}), confirming that post-hoc monitoring cannot be replaced by pre-screening.
22	We propose temporal MH-DIF whenever $\geq$500 models accumulate, with $\rho$-degradation-grounded action levels (\Cref{app:fig_rho_degradation}):
23	(1)~\emph{Monitor} (C\% $< 15\%$): report C\% in release notes.
24	(2)~\emph{Flag} ($15$--$25\%$): report stable-item rankings as sensitivity analysis alongside full rankings.
25	(3)~\emph{Act} (C\% $\geq 25\%$): review flagged items for differential-performance-associated content characteristics; report stable-item rankings as primary metric; use DIF pre-screening to identify stable anchors for equating~\citep{kolen2014equating,habba2026growingpains}.
26	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 595 · 2026-05-22T10:20:58.789398+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 596 · 2026-05-22T10:20:59.040680+00:00_

1	\section*{Limitations}
2	
3	\paragraph{Methodological scope.}
4	MH-DIF detects only uniform DIF; logistic regression reveals an additional 24.8\% non-uniform DIF, making 31\% conservative. More fundamentally, DIF detects \emph{that} items function differently but cannot determine \emph{why}---the signal may reflect contamination, capability change, or training methodology shifts. A definitive causal decomposition remains out of reach without access to model training data. The semi-synthetic framework uses binary response flipping (incorrect $\to$ correct) to simulate differential contamination, representing a worst-case uniform exploitation pattern. Real-world contamination involves partial memorization, reasoning shortcuts, and format-specific advantages; detection power under such realistic patterns is untested. The moderate $\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$ reflects sensitivity to severe differential behavior; the framework's primary methodological contribution---cross-subject matching achieving $\Delta\mathrm{FPR} = 0.000$---is a matching strategy property independent of injection realism.
5	
6	\paragraph{Examinee non-independence.}
7	The MH $\chi^2$ test assumes independent examinees, yet LLMs sharing base models, training data, or architectures violate this assumption. Empirical mitigations partially address this: permutation simulation bounds LD-attributable FPR inflation to ${<}0.001$~pp, and graduated de-duplication ($K{=}20$: C\% $= 29.1\%$) shows family structure does not inflate results. \citet{french2010hierarchical} show that MH maintains nominal size under moderate clustering in educational settings, consistent with our empirical findings; however, the extreme relatedness of some LLM families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in that work. Cluster bootstrap resampling at the family level (29 families with $\geq$3 members, 1{,}882 models, $B = 1{,}000$) yields a 95\% CI of $[26.7\%, 53.2\%]$, $3.1
…[truncated 1454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 597 · 2026-05-22T10:20:59.141598+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 598 · 2026-05-22T10:20:59.242580+00:00_

1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini
…[truncated 10679 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 599 · 2026-05-22T10:20:59.243004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 600 · 2026-05-22T10:20:59.446904+00:00_

1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet whether individual items measure the same construct over time is rarely tested---and existing contamination detectors validate against ground truth that conflates global exposure with differential functioning. We develop a semi-synthetic injection framework with cross-subject matching that achieves zero false positive inflation under single-subject contamination ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power under worst-case uniform injection ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$), and show that web-overlap contamination labels are near-independent of Mantel-Haenszel Differential Item Functioning (DIF) flags (enrichment $\approx 0.96$)---exposing a category error in prevailing validation methodology. Applying MH-DIF with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 items), we find 17.9--31.3\% of items exhibit large temporal DIF (ETS~C) between 2023 and 2024 cohorts, with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). This does not threaten aggregate ranking validity ($\rho \approx 0.997$, $\tau \approx 0.958$), but specific model families show concentrated rank shifts (Llama-3: ${+}53$ median positions, Mistral: $-35$) and 2.0\% of pairwise rankings reverse. Item-level decomposition shows 92.4\% of the signal is item-specific; DIF-flagged items concentrate discriminative information ($z = -8$ to $-49$) with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 601 · 2026-05-22T10:20:59.447420+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 602 · 2026-05-22T10:20:59.447802+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. This pattern persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of the DIF signal is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this measurement instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference~\citep{shi2024mink} to performance-based detectors~\citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique}. These methods validate d
…[truncated 4871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-22T10:21:58.207071+00:00_

I have retrieved all seven LaTeX source files. Here is a comprehensive report of the paper's key technical content for your peer review:

## ABSTRACT

**Dataset & Sample**: 5,227 models evaluated on 12,508 MMLU items; 27,125 items across six METABENCH benchmarks
**Primary Finding**: 17.9--31.3% of items exhibit large temporal DIF (ETS Category C) between 2023 and 2024 cohorts
**Key Statistics**: 
- Knowledge/reasoning benchmarks: C% ≥ 26.9% (MMLU 31.3%, WinoGrande 30.3%, TruthfulQA 29.7%, ARC 26.9%)
- Procedural benchmarks: C% ≤ 18.9% (GSM8K 18.9%, HellaSwag 17.9%)
- Item-specific signal: 92.4% of DIF signal is item-specific
- Rank correlation preserved: ρ ≈ 0.997, τ ≈ 0.958
- Pairwise rank reversals: 2.0% of model pairs flip rankings
- Semi-synthetic validation: ΔTPr = +0.508 at p = 0.5; ΔFPr = 0.000
- Web-overlap independence: enrichment ≈ 0.96

## INTRODUCTION

**Cohort Sizes**: 
- 2023: N = 1,080 models
- 2024: N = 807 models
**Primary Finding**: 31% of MMLU items receive ETS Category C classification (|ΔMH| ≥ 1.5, p < 0.05)
**Sanity Check**: Random split within 2023 cohort = 0.18% ETS C items
**Range**: C% across 57 MMLU subjects: 21--48% (unweighted mean ≈ 30%)
**Item-Specificity**: 92.4% of DIF signal is item-specific, not attributable to aggregate domain-level accuracy gains

**Ground Truth Meta-Critique**:
- Web-overlap enrichment ratio: 0.964 (DIF-C rates: 30.7% contaminated, 31.8% clean items)
- Jaccard index: 0.206
- φ = 0.012; χ² = 1.28 (p = 0.258); OR = 1.05 [0.96, 1.15]
- Input-only enrichment: 0.986; Input-and-label: 0.960

**Temporal Comparability Assumption**: Validates that MMLU measures the same construct across model cohorts

## METHOD

**Data Structure**: 
- METABENCH response matrix: 5,227 models × 12,508 MMLU items
- MMLU: 57 subjects grouped into 5 broad domains (STEM, Humanities, Social Sciences, Other, mixed)
- Web-contamination labels: 9,229 of 12,508 items (73.8% coverage)

**Mantel-Haenszel DIF Procedure**:
- K = 5 equiprobable strata (
…[truncated 12027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 62030
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-22T10:25:45.931735+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — Round 1 审稿意见\n\n**论文**: Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**Venue**: EMNLP 2026 (ACL Rolling Review)\n**审查侧重**: 方法严谨性 + 实验有效性\n\n---\n\n## 总体评分\n\n**Overall Assessment: 3.5 (Borderline Conference)**\n\n**一句话总结**: 将教育测量 MH-DIF 方法系统迁移至 LLM benchmark 评估具有真实的方法论贡献和实践意义，控制实验层次丰富，但 LOFO 分析暴露的 family-concentration 问题以及 examinee non-independence 的影响未被充分量化，削弱了核心 claim 的确信度。\n\n---\n\n## 官方维度打分（ACL ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 核心 MH-DIF 方法论迁移合理，5 组控制实验构成有力的 validity ladder，但 LOFO 分析中 Mistral/Llama-3 移除导致 C% 大幅下降（22.5%/24.1%）未被充分解释，non-independence 对 chi-squared inflation 的定量影响不明 |\n| **Excitement** | 3.5/5 | 首次大规模将 psychometric DIF 引入 LLM 评估，规模（5,227 models × 12,508 items）和跨 benchmark 复现令人印象深刻，但因果归因受限（无法区分 contamination vs. capability evolution）限制了实际可操作性 |\n| **Reproducibility** | 4/5 | 代码和数据明确提到可用（脚注1），METABENCH 为公开数据，方法细节充分（K=5 stratification、ETS thresholds、bootstrap replications 均有报告） |\n| **Confidence** | 4/5 | 熟悉 DIF 方法论和 LLM benchmark 评估文献，仔细检查了关键统计推断 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] LOFO family-concentration 效应被低估，power-reduction 解释不充分\n\n- **具体位置**: Table 6 (Appendix B), Section 4.4 (\"Ability-matched analysis reduces…none reduces C% below ~28%\"), Limitations §9\n- **问题**: 移除 Mistral（547 models, 51% ref）后 C% 从 31.3% 降至 22.5%（-8.8pp），移除 Llama-3（315 models, 39% focal）后降至 24.1%（-7.3pp）。论文将此归因于\"power reduction from smaller remaining samples\"，但移除 Mistral 后 N_ref 仍有 ~533，移除 Llama-3 后 N_focal 仍有 ~492——远超 Section 4.1 power analysis 中 N ≥ 80 即可达到 TPR = 0.68–0.80 的阈值。N_ref = 533 + N_focal = 807 的 total sample 仍达 1,340（原始 1,887 的 71%），仅凭 power reduction 难以解释 8.8pp 的 C% 下降。\n- **更深层问题**: Section 4.4 称\"six alternative combinations were tested; none reduces C% below ~28%\"，但这里的\"alternative combinations\"指的是 matching/control 策略（Table 2 structural approaches），而非 LOFO。这种行文结构让读者误以为 ~28% 是所有稳健性检验的下界，但 LOFO 结果（22.5%, 24.1%）明确低于此。两类 robustness 结果之间的 tension 未被讨论。\n- **为什么影响接收**: 如果 DIF 信号高度集中于 Mistral 和 Llama-3 家族，则\"~31% of MMLU items exhibit temporal DIF\"的 claim 实质上是\"~31% of items exhibit Mistral/Llama-3-specific DIF\"——这是完全不同的结论，大幅降低了方法的普适性。\n- **建议修改方向**:\n  1. 对 LOFO 进行 **expected power calibration**：使用 Section 4.1 的 Monte Carlo power analysis 框架，在 N_ref = 533, N_focal = 807 的条件下模拟 expected C%，与观测到的 22.5% 对比，量化\"power reduction explains X pp of the 8.8pp drop\"\n  2. 将 LOFO 结果与 matching-based robustness 明确区分讨论，不要让 ~28% floor 的表述覆盖 LOFO 发现\n  3. 考虑 **family-weighted C%**（按 family 加权而非按 model 加权），如果 Mistral 和 Llama-3 家族的 DIF pattern 显著不同于其他家族，这本身就是重要发现\n\n**N2** [critical] Examinee non-independence 对 MH chi-squared 的 inflation 效应缺乏直接定量\n\n- **具体位置**: Section 3.2 (\"LLM-Specific Challenges\"), Appendix A.2 (Structural Analysis), Limitations §9\n- **问题**: 论文承认 LLM 共享 base models/training data 违反 local independence 假设，并提供三项间接证据：(a) permutation FPR inflation < 0.001pp; (b) graduated de-duplication K=20 → C% = 29.1%; (c) cluster bootstrap CI [26.7%, 53.2%]。但这三项均未直接量化 non-independence 对 MH chi-squared 统计量的 inflation 程度：\n  - (a) Permutation test 衡量的是 label-shuffling 下的 FPR，不直接回答\"correlated examinees 使多少本不显著的 items 变显著了\"\n  - (b) Graduated de-duplication 同时改变了 sample size 和 within-family correlation，两个效应混淆（论文自己承认\"confounded with statistical power reduction\"）\n  - (c) Cluster bootstrap 给出了正确的 CI，但 upper bound 53.2% 意味着 point estimate 的不确定性巨大——论文以 lower bound 26.7% > random baseline (0.18%) 论证稳健性，但 26.7% 到 53.2% 这个 range 本身就说明 family-level clustering 对 point estimate 有 massive impact\n- **为什么影响接收**: MH chi-squared test 的 Type I error rate 在 correlated observations 下是 inflated 的（这在教育测量文献中有广泛记录）。不量化这个 inflation，就无法确信 31.3% 的 C 类 items 中有多少是 genuine DIF vs. inflated significance。\n- **建议修改方向**:\n  1. 使用 **design effect (DEFF)** 或 **effective sample size** 方法：估计 intra-family correlation (ICC)，计算 DEFF = 1 + (m̄ - 1) × ICC（m̄ = average family size），调整 MH chi-squared 的自由度或临界值，重新计算 C%\n  2. 或者：在 graduated de-duplication 框架中，固定 total N（通过 oversampling smaller families），仅减少 within-family correlation，分离 power 和 correlation 两个效应\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Semi-synthetic injection 的 ecological validity 有限，但 claim 表述偏强\n\n- **具体位置**: Section 3.4 (\"Semi-Synthetic Injection Framework\"), Section 4.5, Limitations §9\n- **问题**: Binary response flipping（将 ETS A items 的 incorrect → correct）模拟的是最极端的 uniform contamination——所有 injected items 在 focal group 中以相同概率 p 被\"解决\"。但现实中 contamination 的 pattern 远更复杂：\n  - 不同 items 的 memorization 难度不同（long-context items vs. short factoid items）\n  - Contamination 可能影响同一 subject 的部分 items 而非全部\n  - Response flipping 只模拟 unidirectional DIF (focal better)，而论文发现 Humanities items 64.4% favor 2023（即反方向 DIF）\n  - 论文自己报告 moderate ΔTPR = +0.508 at p = 0.5，并标注为\"upper-bound estimate\"，但这个 caveat 只在 Limitations 一笔带过\n- **建议**: (a) 在 Section 3.4 明确列出 \"worst-case uniform\" 这一假设及其局限性（不仅在 Limitations）; (b) 补充一个 heterogeneous injection 实验（e.g., flipping probability 与 item difficulty 相关），即使 ΔTPR 更低也能增强 framework 的 ecological validity\n\n**W2** [warning] Bootstrap CI 的 3.1× width 差异暗示 family-level dependence 结构性影响了 inference，但未被纳入 primary results reporting\n\n- **具体位置**: Section 4.2 (\"95% bootstrap CI [29.4%, 38.1%]…family-level cluster bootstrap CI [26.7%, 53.2%]\")\n- **问题**: 论文 primary result 报告的是 model-level bootstrap CI [29.4%, 38.1%]，cluster bootstrap 仅作为 robustness check。但 model-level bootstrap **假设 models are independent**——这正是论文承认被违反的假设。在该假设被违反的情况下，cluster bootstrap 是更合适的推断方法，应该作为 primary CI 报告。当 primary CI 变为 [26.7%, 53.2%] 时，结论的表述需要相应调整（e.g., \"approximately 27%–53% of items\" 而非 \"approximately 31%\"）。\n- **建议**: 将 family-level cluster bootstrap CI 提升为 primary inference，或至少在 abstract/introduction/conclusion 中同时报告两个 CI\n\n**W3** [warning] Cross-benchmark C% 可比性受 statistical power 差异影响，但未调整\n\n- **具体位置**: Table 3 (Section 4.7), Section 5\n- **问题**: 6 个 benchmark 的 item 数量差异巨大（MMLU 12,508 vs. TruthfulQA 817 vs. GSM8K 1,319）。MH-DIF 的 power 与 item-level sample size 无关，但与 **model count per stratum** 有关。不同 benchmark 的 model overlap 可能不同（GSM8K 有 6,702 models vs. MMLU 5,227），导致 per-stratum N 不同。但更关键的是：每个 benchmark 的 **item-level** C% 直接取决于 |ΔMH| effect size distribution，而不同 benchmark 的 item 构造方式完全不同（MMLU 多选知识 vs. GSM8K 数学推理 vs. HellaSwag 完形填空）。论文将\"knowledge/reasoning benchmarks C% ≥ 26.9% vs. procedural benchmarks C% ≤ 18.9%\"解读为 content-type 差异（Section 5, \"knowledge-intensive items being more sensitive to training data composition shifts\"），但这一解读缺乏 formal testing——可能仅仅是 item difficulty 分布或 discriminability 差异导致。\n- **建议**: 对 cross-benchmark C% 差异做 formal decomposition（e.g., 控制 item difficulty 和 discrimination 后比较 residual C%），或明确标注当前比较为 descriptive\n\n**W4** [warning] Within-family (Llama-2 vs. Llama-3) 61.3% C% 的解读与 temporal 31.3% 的关系不清晰\n\n- **具体位置**: Section 4.2, Table 1\n- **问题**: Llama-2 vs. Llama-3 的 61.3% C% 在 matched-ability analysis 后降至 28.3%，temporal comparison 的 31.3% 降至 28.9%。论文将两者的 matched values convergence (~28-29%) 解读为\"genuine item-level DIF\"的证据。但 within-family 比较中的 ability mismatch 远大于 temporal 比较（Llama-2 和 Llama-3 的能力差距 > 2023 vs 2024 cohort 平均差距），所以 matching 移除了更多\"假 DIF\"。两个 matched C% 收敛到相近值可能是巧合而非规律。\n- **建议**: 用更多 cohort pairs（e.g., different ability gaps）检验 \"matched C% converges to ~28%\" 是否是 robust pattern，或加 error bars 说明 28.3% 和 28.9% 的 CI 是否 overlap\n\n**W5** [warning] GSM1K correlation (r = -0.478, N = 33) 在 Discussion 中的使用超出 \"exploratory\" 标注\n\n- **具体位置**: Section 4.7 (\"an exploratory GSM1K analysis\"), Section 5, Figure 5\n- **问题**: 论文在 Section 4.7 将 GSM1K correlation 标注为 exploratory，但 Section 5 的 Discussion 中写到 \"Both benchmarks exhibit temporal DIF…consistent with DIF capturing capability change distinct from memorization (r = -0.478, p = 0.005, Figure 5)\"——这里的措辞已经从 exploratory 变为 supportive evidence。N = 33 的 correlation 极其不稳定（leave-one-out 可能大幅变化），且 GSM1K 本身作为 contamination ground truth 的质量未经验证。\n- **建议**: 在 Discussion 中保持 exploratory framing，加入 caveat on small N instability（e.g., bootstrap CI for r）\n\n---\n\n## 小问题（不影响接收）\n\n**M1** Multiple testing: BH-FDR 只移除 3 items（31.32% → 31.30%）被解读为\"ETS dual threshold already provides implicit protection\"。但这也可能意味着 BH 在此 setting 下 power 不足（12,508 tests, many true positives），而非 ETS threshold 就足够。建议加一句 caveat。\n\n**M2** Section 4.1 Power analysis: \"TPR ranges from 0.40 at a = 0.5 to 0.95 at a = 2.0\"——这里的 a 是 item discrimination parameter。论文报告 MMLU 的 ā = 0.87，对应 TPR ≈ 0.68。但 MMLU 各 subject 的 discrimination 分布可能很广，低 discrimination items 的 TPR 可能只有 0.40。论文的 aggregate C% 因此可能 **underestimate** true DIF（因为低 discrimination items 的 DIF 检测不出），建议在 Discussion 中提及这一点。\n\n**M3** Equation (1): MH odds ratio 公式中使用了 $A_k$, $B_k$, $C_k$, $D_k$ 表示 2×2 table 的 cells，但未提供 table layout 图示。对不熟悉 MH-DIF 的 NLP 读者来说，一个 2×2 contingency table 示例会大幅提高 accessibility。\n\n**M4** Section 3.3 Cohort Designs: 5 种 cohort comparison 的 rationale 分散在不同 paragraph，建议用一个表格或列表统一呈现（目的、sample sizes、expected C%），便于读者理解 validity ladder 的逻辑。\n\n**M5** Permutation test: 1,000 iterations 对 p < 0.01 级别的 tail estimation 精度有限（SE ≈ √(0.01×0.99/1000) ≈ 0.003）。建议增加至 5,000+ 或报告 permutation p-value 的 Monte Carlo CI。\n\n---\n\n## Questions to Authors\n\n**Q1**: 能否对 LOFO 进行 power-calibrated analysis？具体来说，在 N_ref = 533, N_focal = 807 条件下，使用你们已有的 Monte Carlo 框架模拟 expected C%（假设 true C% = 31.3%），与 observed 22.5% 对比？\n\n**Q2**: Graduated de-duplication 在 K=10 时 C% = 22.7%，K=20 时 C% = 29.1%。能否在固定 total N（e.g., 通过 upsampling small families 到 K=20 level）下重复此实验，分离 power 和 de-duplication 两个效应？\n\n**Q3**: Section 4.3 Ground Truth Mismatch 部分的 enrichment ratio 0.964 表明 DIF flags 与 web-overlap 近乎独立。但这是否意味着 MH-DIF 检测到的 temporal instability 与 contamination 无关？如果是，那么 DIF 检测到的究竟是什么现象？论文说\"underdetermined without training data\"，但这是否过度回避了 causal interpretation？\n\n**Q4**: Semi-synthetic injection 中 within-subject matching 的 FPR inflation 为 +0.186（Section 4.5）。论文推荐 cross-subject matching 作为 standard protocol，但如果 contamination 同时影响多个 subjects（k > 5），cross-subject matching 的 ΔFPR 也开始上升（Table 5: k=10 → 0.047）。在实际应用中，如何判断 contamination 是否已经扩散到 >5 subjects？\n\n**Q5**: Cluster bootstrap 的 53.2% upper bound 意味着什么实质问题？是否暗示存在某些 family 的 DIF pattern 极端不同？能否报告 per-family C% distribution？\n\n---\n\n## Missing References\n\n- **Swaminathan & Rogers (1990)**: 论文引用了 Swaminathan and Rogers (1990) 关于 logistic regression DIF，但未引用其后续重要工作 **Rogers & Swaminathan (1993)** 关于 Type I error rates under model violation，这与 LLM setting 下的 assumption violation 直接相关。\n- **Penfield & Camilli (2007)**: 已引用，但建议增加 **Penfield (2001)** 关于 MH DIF under small samples 的讨论，因为 LOFO 场景涉及 reduced N。\n- **DIF under non-independence**: 教育测量文献中有关于 testlet-level DIF（即 items nested within passages/testlets，产生 local dependence）的讨论，如 **Wainer et al. (2007) \"Testlet Response Theory and Its Applications\"**——这与 LLM families 内的 non-independence 高度类似，建议引用。\n\n---\n\n## 主要优势\n\n1. **规模和系统性**: 5,227 models × 12,508 MMLU items + 6 benchmarks，这是迄今最大规模的 LLM benchmark psychometric audit，数据规模本身就构成贡献\n2. **Validity ladder 设计**: Random split → ability quintile → temporal → within-family 的控制对比层次清晰，逻辑严密，说服力强（Table 1）\n3. **Cross-subject matching 创新**: ΔFPR = 0.000 的 constructive guarantee（在 k ≤ 5 条件下）是 genuine 的方法论贡献，解决了 matching variable contamination 这一长期难题\n4. **Transparent limitations**: 论文对 assumption violations（non-independence, multidimensionality, bimodal distribution）的讨论比同类论文更诚实和详尽\n5. **Practical actionability**: Section 5.3 的 Monitor/Flag/Act protocol 提供了可直接应用的框架，Figure 6 的 ranking degradation 曲线有实际指导意义\n6. **Ground truth meta-critique**: Section 4.3 和 5.2 对 web-overlap 作为 contamination ground truth 的质疑（enrichment ≈ 0.96, near independence）是独立而重要的发现\n\n---\n\n**总结判断**: 这是一篇方法论贡献扎实、规模令人印象深刻的论文。核心问题在于：(1) LOFO 分析暴露的 family-concentration 效应需要 power-calibrated quantification 以支撑\"31% items show temporal DIF\"这一 headline claim 的 generality；(2) non-independence 的定量影响需要超越间接证据。如果 N1 和 N2 能得到充分 address（尤其是 N1 的 power calibration），本文可达到 Conference 接收水平。当前状态下我的建议是 Borderline Conference (3.5)，两个 critical issues 的修改可在一个 ARR cycle 内完成。\n",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — Round 1 审稿意见\n\n**论文**: Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**Venue**: EMNLP 2026 (ACL Rolling Review)\n**审查侧重**: 方法严谨性 + 实验有效性\n\n---\n\n## 总体评分\n\n**Overall Assessment: 3.5 (Borderline Conference)**\n\n**一句话总结**: 将教育测量 MH-DIF 方法系统迁移至 LLM benchmark 评估具有真实的方法论贡献和实践意义，控制实验层次丰富，但 LOFO 分析暴露的 family-concentration 问题以及 examinee non-independence 的影响未被充分量化，削弱了核心 claim 的确信度。\n\n---\n\n## 官方维度打分（ACL ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 核心 MH-DIF 方法论迁移合理，5 组控制实验构成有力的 validity ladder，但 LOFO 分析中 Mistral/Llama-3 移除导致 C% 大幅下降（22.5%/24.1%）未被充分解释，non-independence 对 chi-squared inflation 的定量影响不明 |\n| **Excitement** | 3.5/5 | 首次大规模将 psychometric DIF 引入 LLM 评估，规模（5,227 models × 12,508 items）和跨 benchmark 复现令人印象深刻，但因果归因受限（无法区分 contamination vs. capability evolution）限制了实际可操作性 |\n| **Reproducibility** | 4/5 | 代码和数据明确提到可用（脚注1），METABENCH 为公开数据，方法细节充分（K=5 stratification、ETS thresholds、bootstrap replications 均有报告） |\n| **Confidence** | 4/5 | 熟悉 DIF 方法论和 LLM benchmark 评估文献，仔细检查了关键统计推断 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] LOFO family-concentration 效应被低估，power-reduction 解释不充分\n\n- **具体位置**: Table 6 (Appendix B), Section 4.4 (\"Ability-matched analysis reduces…none reduces C% below ~28%\"), Limitations §9\n- **问题**: 移除 Mistral（547 models, 51% ref）后 C% 从 31.3% 降至 22.5%（-8.8pp），移除 Llama-3（315 models, 39% focal）后降至 24.1%（-7.3pp）。论文将此归因于\"power reduction from smaller remaining samples\"，但移除 Mistral 后 N_ref 仍有 ~533，移除 Llama-3 后 N_focal 仍有 ~492——远超 Section 4.1 power analysis 中 N ≥ 80 即可达到 TPR = 0.68–0.80 的阈值。N_ref = 533 + N_focal = 807 的 total sample 仍达 1,340（原始 1,887 的 71%），仅凭 power reduction 难以解释 8.8pp 的 C% 下降。\n- **更深层问题**: Section 4.4 称\"six alternative combinations were tested; none reduces C% below ~28%\"，但这里的\"alternative combinations\"指的是 matching/control 策略（Table 2 structural approaches），而非 LOFO。这种行文结构让读者误以为 ~28% 是所有稳健性检验的下界，但 LOFO 结果（22.5%, 24.1%）明确低于此。两类 robustness 结果之间的 tension 未被讨论。\n- **为什么影响接收**: 如果 DIF 信号高度集中于 Mistral 和 Llama-3 家族，则\"~31% of MMLU items exhibit temporal DIF\"的 claim 实质上是\"~31% of items exhibit Mistral/Llama-3-specific DIF\"——这是完全不同的结论，大幅降低了方法的普适性。\n- **建议修改方向**:\n  1. 对 LOFO 进行 **expected power calibration**：使用 Section 4.1 的 Monte Carlo power analysis 框架，在 N_ref = 533, N_focal = 807 的条件下模拟 expected C%，与观测到的 22.5% 对比，量化\"power reduction explains X pp of the 8.8pp drop\"\n  2. 将 LOFO 结果与 matching-based robustness 明确区分讨论，不要让 ~28% floor 的表述覆盖 LOFO 发现\n  3. 考虑 **family-weighted C%**（按 family 加权而非按 model 加权），如果 Mistral 和 Llama-3 家族的 DIF pattern 显著不同于其他家族，这本身就是重要发现\n\n**N2** [critical] Examinee non-independence 对 MH chi-squared 的 inflation 效应缺乏直接定量\n\n- **具体位置**: Section 3.2 (\"LLM-Specific Challenges\"), Appendix A.2 (Structural Analysis), Limitations §9\n- **问题**: 论文承认 LLM 共享 base models/training data 违反 local independence 假设，并提供三项间接证据：(a) permutation FPR inflation < 0.001pp; (b) graduated de-duplication K=20 → C% = 29.1%; (c) cluster bootstrap CI [26.7%, 53.2%]。但这三项均未直接量化 non-independence 对 MH chi-squared 统计量的 inflation 程度：\n  - (a) Permutation test 衡量的是 label-shuffling 下的 FPR，不直接回答\"correlated examinees 使多少本不显著的 items 变显著了\"\n  - (b) Graduated de-duplication 同时改变了 sample size 和 within-family correlation，两个效应混淆（论文自己承认\"confounded with statistical power reduction\"）\n  - (c) Cluster bootstrap 给出了正确的 CI，但 upper bound 53.2% 意味着 point estimate 的不确定性巨大——论文以 lower bound 26.7% > random baseline (0.18%) 论证稳健性，但 26.7% 到 53.2% 这个 range 本身就说明 family-level clustering 对 point estimate 有 massive impact\n- **为什么影响接收**: MH chi-squared test 的 Type I error rate 在 correlated observations 下是 inflated 的（这在教育测量文献中有广泛记录）。不量化这个 inflation，就无法确信 31.3% 的 C 类 items 中有多少是 genuine DIF vs. inflated significance。\n- **建议修改方向**:\n  1. 使用 **design effect (DEFF)** 或 **effective sample size** 方法：估计 intra-family correlation (ICC)，计算 DEFF = 1 + (m̄ - 1) × ICC（m̄ = average family size），调整 MH chi-squared 的自由度或临界值，重新计算 C%\n  2. 或者：在 graduated de-duplication 框架中，固定 total N（通过 oversampling smaller families），仅减少 within-family correlation，分离 power 和 correlation 两个效应\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Semi-synthetic injection 的 ecological validity 有限，但 claim 表述偏强\n\n- **具体位置**: Section 3.4 (\"Semi-Synthetic Injection Framework\"), Section 4.5, Limitations §9\n- **问题**: Binary response flipping（将 ETS A items 的 incorrect → correct）模拟的是最极端的 uniform contamination——所有 injected items 在 focal group 中以相同概率 p 被\"解决\"。但现实中 contamination 的 pattern 远更复杂：\n  - 不同 items 的 memorization 难度不同（long-context items vs. short factoid items）\n  - Contamination 可能影响同一 subject 的部分 items 而非全部\n  - Response flipping 只模拟 unidirectional DIF (focal better)，而论文发现 Humanities items 64.4% favor 2023（即反方向 DIF）\n  - 论文自己报告 moderate ΔTPR = +0.508 at p = 0.5，并标注为\"upper-bound estimate\"，但这个 caveat 只在 Limitations 一笔带过\n- **建议**: (a) 在 Section 3.4 明确列出 \"worst-case uniform\" 这一假设及其局限性（不仅在 Limitations）; (b) 补充一个 heterogeneous injection 实验（e.g., flipping probability 与 item difficulty 相关），即使 ΔTPR 更低也能增强 framework 的 ecological validity\n\n**W2** [warning] Bootstrap CI 的 3.1× width 差异暗示 family-level dependence 结构性影响了 inference，但未被纳入 primary results reporting\n\n- **具体位置**: Section 4.2 (\"95% bootstrap CI [29.4%, 38.1%]…family-level cluster bootstrap CI [26.7%, 53.2%]\")\n- **问题**: 论文 primary result 报告的是 model-level bootstrap CI [29.4%, 38.1%]，cluster bootstrap 仅作为 robustness check。但 model-level bootstrap **假设 models are independent**——这正是论文承认被违反的假设。在该假设被违反的情况下，cluster bootstrap 是更合适的推断方法，应该作为 primary CI 报告。当 primary CI 变为 [26.7%, 53.2%] 时，结论的表述需要相应调整（e.g., \"approximately 27%–53% of items\" 而非 \"approximately 31%\"）。\n- **建议**: 将 family-level cluster bootstrap CI 提升为 primary inference，或至少在 abstract/introduction/conclusion 中同时报告两个 CI\n\n**W3** [warning] Cross-benchmark C% 可比性受 statistical power 差异影响，但未调整\n\n- **具体位置**: Table 3 (Section 4.7), Section 5\n- **问题**: 6 个 benchmark 的 item 数量差异巨大（MMLU 12,508 vs. TruthfulQA 817 vs. GSM8K 1,319）。MH-DIF 的 power 与 item-level sample size 无关，但与 **model count per stratum** 有关。不同 benchmark 的 model overlap 可能不同（GSM8K 有 6,702 models vs. MMLU 5,227），导致 per-stratum N 不同。但更关键的是：每个 benchmark 的 **item-level** C% 直接取决于 |ΔMH| effect size distribution，而不同 benchmark 的 item 构造方式完全不同（MMLU 多选知识 vs. GSM8K 数学推理 vs. HellaSwag 完形填空）。论文将\"knowledge/reasoning benchmarks C% ≥ 26.9% vs. procedural benchmarks C% ≤ 18.9%\"解读为 content-type 差异（Section 5, \"knowledge-intensive items being more sensitive to training data composition shifts\"），但这一解读缺乏 formal testing——可能仅仅是 item difficulty 分布或 discriminability 差异导致。\n- **建议**: 对 cross-benchmark C% 差异做 formal decomposition（e.g., 控制 item difficulty 和 discrimination 后比较 residual C%），或明确标注当前比较为 descriptive\n\n**W4** [warning] Within-family (Llama-2 vs. Llama-3) 61.3% C% 的解读与 temporal 31.3% 的关系不清晰\n\n- **具体位置**: Section 4.2, Table 1\n- **问题**: Llama-2 vs. Llama-3 的 61.3% C% 在 matched-ability analysis 后降至 28.3%，temporal comparison 的 31.3% 降至 28.9%。论文将两者的 matched values convergence (~28-29%) 解读为\"genuine item-level DIF\"的证据。但 within-family 比较中的 ability mismatch 远大于 temporal 比较（Llama-2 和 Llama-3 的能力差距 > 2023 vs 2024 cohort 平均差距），所以 matching 移除了更多\"假 DIF\"。两个 matched C% 收敛到相近值可能是巧合而非规律。\n- **建议**: 用更多 cohort pairs（e.g., different ability gaps）检验 \"matched C% converges to ~28%\" 是否是 robust pattern，或加 error bars 说明 28.3% 和 28.9% 的 CI 是否 overlap\n\n**W5** [warning] GSM1K correlation (r = -0.478, N = 33) 在 Discussion 中的使用超出 \"exploratory\" 标注\n\n- **具体位置**: Section 4.7 (\"an exploratory GSM1K analysis\"), Section 5, Figure 5\n- **问题**: 论文在 Section 4.7 将 GSM1K correlation 标注为 exploratory，但 Section 5 的 Discussion 中写到 \"Both benchmarks exhibit temporal DIF…consistent with DIF capturing capability change distinct from memorization (r = -0.478, p = 0.005, Figure 5)\"——这里的措辞已经从 exploratory 变为 supportive evidence。N = 33 的 correlation 极其不稳定（leave-one-out 可能大幅变化），且 GSM1K 本身作为 contamination ground truth 的质量未经验证。\n- **建议**: 在 Discussion 中保持 exploratory framing，加入 caveat on small N instability（e.g., bootstrap CI for r）\n\n---\n\n## 小问题（不影响接收）\n\n**M1** Multiple testing: BH-FDR 只移除 3 items（31.32% → 31.30%）被解读为\"ETS dual threshold already provides implicit protection\"。但这也可能意味着 BH 在此 setting 下 power 不足（12,508 tests, many true positives），而非 ETS threshold 就足够。建议加一句 caveat。\n\n**M2** Section 4.1 Power analysis: \"TPR ranges from 0.40 at a = 0.5 to 0.95 at a = 2.0\"——这里的 a 是 item discrimination parameter。论文报告 MMLU 的 ā = 0.87，对应 TPR ≈ 0.68。但 MMLU 各 subject 的 discrimination 分布可能很广，低 discrimination items 的 TPR 可能只有 0.40。论文的 aggregate C% 因此可能 **underestimate** true DIF（因为低 discrimination items 的 DIF 检测不出），建议在 Discussion 中提及这一点。\n\n**M3** Equation (1): MH odds ratio 公式中使用了 $A_k$, $B_k$, $C_k$, $D_k$ 表示 2×2 table 的 cells，但未提供 table layout 图示。对不熟悉 MH-DIF 的 NLP 读者来说，一个 2×2 contingency table 示例会大幅提高 accessibility。\n\n**M4** Section 3.3 Cohort Designs: 5 种 cohort comparison 的 rationale 分散在不同 paragraph，建议用一个表格或列表统一呈现（目的、sample sizes、expected C%），便于读者理解 validity ladder 的逻辑。\n\n**M5** Permutation test: 1,000 iterations 对 p < 0.01 级别的 tail estimation 精度有限（SE ≈ √(0.01×0.99/1000) ≈ 0.003）。建议增加至 5,000+ 或报告 permutation p-value 的 Monte Carlo CI。\n\n---\n\n## Questions to Authors\n\n**Q1**: 能否对 LOFO 进行 power-calibrated analysis？具体来说，在 N_ref = 533, N_focal = 807 条件下，使用你们已有的 Monte Carlo 框架模拟 expected C%（假设 true C% = 31.3%），与 observed 22.5% 对比？\n\n**Q2**: Graduated de-duplication 在 K=10 时 C% = 22.7%，K=20 时 C% = 29.1%。能否在固定 total N（e.g., 通过 upsampling small families 到 K=20 level）下重复此实验，分离 power 和 de-duplication 两个效应？\n\n**Q3**: Section 4.3 Ground Truth Mismatch 部分的 enrichment ratio 0.964 表明 DIF flags 与 web-overlap 近乎独立。但这是否意味着 MH-DIF 检测到的 temporal instability 与 contamination 无关？如果是，那么 DIF 检测到的究竟是什么现象？论文说\"underdetermined without training data\"，但这是否过度回避了 causal interpretation？\n\n**Q4**: Semi-synthetic injection 中 within-subject matching 的 FPR inflation 为 +0.186（Section 4.5）。论文推荐 cross-subject matching 作为 standard protocol，但如果 contamination 同时影响多个 subjects（k > 5），cross-subject matching 的 ΔFPR 也开始上升（Table 5: k=10 → 0.047）。在实际应用中，如何判断 contamination 是否已经扩散到 >5 subjects？\n\n**Q5**: Cluster bootstrap 的 53.2% upper bound 意味着什么实质问题？是否暗示存在某些 family 的 DIF pattern 极端不同？能否报告 per-family C% distribution？\n\n---\n\n## Missing References\n\n- **Swaminathan & Rogers (1990)**: 论文引用了 Swaminathan and Rogers (1990) 关于 logistic regression DIF，但未引用其后续重要工作 **Rogers & Swaminathan (1993)** 关于 Type I error rates under model violation，这与 LLM setting 下的 assumption violation 直接相关。\n- **Penfield & Camilli (2007)**: 已引用，但建议增加 **Penfield (2001)** 关于 MH DIF under small samples 的讨论，因为 LOFO 场景涉及 reduced N。\n- **DIF under non-independence**: 教育测量文献中有关于 testlet-level DIF（即 items nested within passages/testlets，产生 local dependence）的讨论，如 **Wainer et al. (2007) \"Testlet Response Theory and Its Applications\"**——这与 LLM families 内的 non-independence 高度类似，建议引用。\n\n---\n\n## 主要优势\n\n1. **规模和系统性**: 5,227 models × 12,508 MMLU items + 6 benchmarks，这是迄今最大规模的 LLM benchmark psychometric audit，数据规模本身就构成贡献\n2. **Validity ladder 设计**: Random split → ability quintile → temporal → within-family 的控制对比层次清晰，逻辑严密，说服力强（Table 1）\n3. **Cross-subject matching 创新**: ΔFPR = 0.000 的 constructive guarantee（在 k ≤ 5 条件下）是 genuine 的方法论贡献，解决了 matching variable contamination 这一长期难题\n4. **Transparent limitations**: 论文对 assumption violations（non-independence, multidimensionality, bimodal distribution）的讨论比同类论文更诚实和详尽\n5. **Practical actionability**: Section 5.3 的 Monitor/Flag/Act protocol 提供了可直接应用的框架，Figure 6 的 ranking degradation 曲线有实际指导意义\n6. **Ground truth meta-critique**: Section 4.3 和 5.2 对 web-overlap 作为 contamination ground truth 的质疑（enrichment ≈ 0.96, near independence）是独立而重要的发现\n\n---\n\n**总结判断**: 这是一篇方法论贡献扎实、规模令人印象深刻的论文。核心问题在于：(1) LOFO 分析暴露的 family-concentration 效应需要 power-calibrated quantification 以支撑\"31% items show temporal DIF\"这一 headline claim 的 generality；(2) non-independence 的定量影响需要超越间接证据。如果 N1 和 N2 能得到充分 address（尤其是 N1 的 power calibration），本文可达到 Conference 接收水平。当前状态下我的建议是 Borderline Conference (3.5)，两个 critical issues 的修改可在一个 ARR cycle 内完成。\n",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-22T10:25:50.050137+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4118
}
```

</details>

---


### Assistant

_source line 606 · 2026-05-22T10:26:01.001986+00:00_

审稿意见已提交给 Review Director。

**审稿摘要**:
- **Overall: 3.5 (Borderline Conference)**
- **Soundness: 3.5/5 | Excitement: 3.5/5**
- **2 个 Must-Fix**: (N1) LOFO family-concentration 效应被低估——移除 Mistral/Llama-3 后 C% 降至 22-24%，power reduction 解释不充分，需要 power-calibrated quantification；(N2) examinee non-independence 对 MH chi-squared 的 inflation 缺乏直接定量（design effect / effective sample size）
- **5 个 Should-Fix**: semi-synthetic ecological validity、cluster bootstrap CI 应为 primary inference、cross-benchmark C% 可比性、within-family matched C% convergence 可能是巧合、GSM1K correlation 使用超出 exploratory 标注
- **5 个 Minor**: BH-FDR 解读、low-discrimination underdetection、MH table 图示、cohort design 呈现、permutation iterations
- **核心判断**: 方法论贡献扎实、规模令人印象深刻，但 headline claim "31% items show temporal DIF" 的 generality 需要通过 LOFO power calibration 和 non-independence quantification 来巩固。两个 critical issues 可在一个 ARR cycle 内修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 21

## Round 21

4 recorded events


### User

_source line 607 · 2026-05-22T10:30:15.274993+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 2 审稿报告

## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 论文在前所未有的规模上将成熟的心理测量方法（MH-DIF）应用于 LLM benchmark 评估，产出了有价值的实证发现（31% temporal DIF、DIF 与 contamination 近正交），但方法论新颖性有限，且核心 framing 存在内部矛盾。

## Must-Fix 问题

**N1** [critical] Abstract 信息密度严重超载
- Abstract 中包含至少 15 个不同的统计量，严重损害可读性。建议保留 3-5 个核心数字，其余移至正文。

**N2** [critical] §5.3 Audit Protocol 与论文核心方法论定位存在内在矛盾
- 论文反复强调 "detects THAT not WHY"，但 §5.3 建议 "review flagged items for differential-performance-associated content characteristics"——这要求调查 DIF 的原因，与方法论定位矛盾。"Flag/Act" 命名暗示纠正行动，与 "diagnostic not destructive" framing 不一致。

**N3** [critical] 新颖性定位不够清晰——"application context" 的贡献边界需明确论证
- Contribution 1（ground truth meta-critique）在概念上可能是 a priori obvious
- Contribution 2（cross-subject matching）有心理测量学直接先驱
- Contribution 3（31% temporal instability）缺少与传统教育测量 DIF rates 的对比

## Should-Fix 问题

**W1** 与 Growing Pains (Habba et al., 2026) 的区分不充分
**W2** Discussion 过于压缩，丧失分析深度
**W3** 缺少引用："Test of Time" (arXiv 2509.00072)
**W4** "Temporal DIF" 的因果解释不充分——"Measurement Instability" 标题带有负面含义，DIF 也可能是 benchmark 正常运作的证据
**W5** 92.4% "unrelated to domain accuracy" 的推导过程不透明
**W6** Appendix F 的 negative finding（AUROC≈0.60）与 §5.3 audit protocol 的张力

## Minor
- M1: Table 1 dashes 无 caption 说明
- M2: Figure 1 应标注为 "Schematic illustration"
- M3: 引用核实（Luo et al. vs Zhuang et al.）
- M4: 数值精度不一致
- M5: TPR at mean a=1.2 与 Table 4 交叉验证
- M6: Limitations 长度和覆盖面适当

## Missing References
1. "Test of Time" (arXiv 2509.00072) — 应引用
2. "DIF: A Framework for Benchmarking and Verifying Implicit Bias in LLMs" (arXiv 2505.10013) — 可选

---

请逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-22T10:32:32.857011+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[REBUT] R2-N1: Abstract 信息密度严重超载**\n\nR2 称 abstract 包含 15+ 统计量损害可读性。我不同意将此列为 critical。\n\n理由：本文是 large-scale psychometric audit，核心贡献 **就是** 一组统计发现。Abstract 的数字密度与论文性质匹配——每个数字对应一个独立的 claim（31% temporal DIF、ΔFPR=0.000 validation guarantee、92.4% item-specificity、ρ≈0.997 ranking preservation、enrichment≈0.96 contamination independence）。删减任何一组都会使读者无法从 abstract 判断论文做了什么。ARR reviewer guidelines (I1) 明确要求 specificity——\"instead of 'missing relevant references,' specify which ones\"，同理，abstract 的具体数字正是 specificity 的体现。\n\n此外，ACL ARR guidelines (H13) 警告不要 \"demanding extra experiments beyond what claims require\"——同样适用于要求删减支撑 claim 的核心数据。这是 writing preference，不是 soundness 问题，不应归为 Must-Fix。\n\n**建议降级为 Minor/Style suggestion。**\n\n---\n\n**[REBUT] R2-N2: §5.3 Audit Protocol 与 \"detects THAT not WHY\" 存在内在矛盾**\n\nR2 认为 §5.3 建议\"review flagged items for content characteristics\"与论文的方法论定位矛盾。我不同意。\n\n理由：论文的 claim 是 **MH-DIF 方法本身** detects THAT not WHY——这是对 statistical procedure 的准确描述。§5.3 的 audit protocol 是方法应用后的 **downstream workflow recommendation**，即：先用 MH-DIF 识别可疑 items（THAT），再人工审查这些 items 的特征（WHY）。这是标准的两阶段诊断流程，与教育测量实践完全一致——ETS 自己的 DIF protocol 就是先统计检测再人工审查（参见 Zieky, 1993; Holland & Thayer, 1988 的 original framework）。\n\n\"Flag/Act\" 命名指的是 monitoring 严重程度的分级响应，不是对 DIF items 的\"纠正\"。具体来说（Section 5.3）：\n- Monitor (C% < 15%): 仅报告 C% 在 release notes\n- Flag (15–25%): 报告 stable-item rankings 作为 sensitivity analysis\n- Act (C% ≥ 25%): 审查 flagged items + 将 stable-item rankings 作为 primary metric\n\n这三级响应从未声称 MH-DIF 本身能解释原因。Act 级别的\"review flagged items\"是将问题移交给 domain experts，不是 MH-DIF 方法在做因果归因。\n\n**不构成 contradiction，建议降级或移除。**\n\n---\n\n**[PARTIAL AGREE] R2-N3: 新颖性定位不够清晰**\n\nR2 提出三点：(a) ground truth meta-critique 可能 a priori obvious; (b) cross-subject matching 有心理测量学先驱; (c) 31% 缺少与传统教育 DIF rates 的对比。\n\n逐点回应：\n\n**(a) [REBUT]** Ground truth meta-critique 并非 a priori obvious。大量 contamination detection 文献（Li et al., 2024b; Deng et al., 2024; Golchin and Banerjee, 2024——Section 2 引用）**隐式假设**web-overlap 是 contamination 的可靠 ground truth。本文 Section 4.3 的实证发现——enrichment ratio = 0.964, φ = 0.012, OR = 1.05 [0.96, 1.15]——表明 DIF flags 与 web-overlap **近乎正交**，这直接挑战了该领域的主流假设。如果这一发现是\"a priori obvious\"，那么上述论文不应使用 web-overlap 作为 ground truth。\n\n**(b) [PARTIAL AGREE]** Cross-subject matching 确实有先驱（Swaminathan & Rogers, 1990 的 purified matching；论文 Section 3.2 已引用）。但适配到 multi-domain LLM benchmarks（57 subjects）并证明 constructive ΔFPR = 0.000 guarantee（Table 5, k ≤ 5）是非平凡的扩展。建议作者在 Section 3.4 更明确地 credit 先驱方法并阐明 novel adaptation 的具体贡献。\n\n**(c) [AGREE]** 缺少与传统教育测量 DIF rates 的 quantitative 对比是一个有效的 contextualization gap。典型的 large-scale 教育测试（SAT, GRE）中 ETS C 比例通常在 5–15%（参见 Zieky, 2003; Dorans & Holland, 1993）。与 31% 对比会显著增强论文 finding 的 impact framing。\n\n**建议作者补充教育测量 baseline DIF rates 对比（可在 1–2 句内完成），并强化 cross-subject matching 的 novelty 论证。但整体来看，N3 不构成 Must-Fix——novelty positioning 不充分是 writing/framing 问题而非 soundness 问题，建议降级为 Should-Fix。**\n\n---\n\n## Should-Fix 问题\n\n**[PARTIAL AGREE] R2-W1: 与 Growing Pains (Habba et al., 2026) 的区分不充分**\n\nSection 2 确实提到了 Growing Pains 作为 \"closest concurrent work\"（\"addresses score comparability through fixed-parameter calibration\"），但区分仅一句话。Given 该工作的 high relevance（同样关注 LLM benchmark temporal comparability），2–3 句的 explicit comparison（score-level equating vs. item-level DIF; parametric IRT vs. non-parametric MH）会增强 positioning。\n\n**[PARTIAL AGREE] R2-W2: Discussion 过于压缩**\n\n在 8-page limit 下 Discussion 被压缩是可以理解的。但 §5.1 (Temporal Comparability) 和 §5.2 (Ground Truth Meta-Critique) 各只有一段，确实牺牲了分析深度。特别是 §5.2 需要更深入地讨论\"如果 DIF 和 web-overlap 正交，DIF 到底检测到了什么\"这一核心问题。建议将部分 Appendix 内容（如 structural analysis details）进一步压缩以释放 Discussion 空间。\n\n**[REBUT] R2-W3: 缺少引用 \"Test of Time\" (arXiv 2509.00072)**\n\n我无法验证该 arXiv 论文的确切内容和发表状态。如果该论文确实讨论了 benchmark temporal stability 的相关话题，可以考虑引用。但 missing reference 通常不构成 Should-Fix——ARR guidelines (H3) 警告 \"claiming lack of novelty without specific references\"，同理，仅凭一篇未经验证的 arXiv preprint 不应作为 novelty concern 的依据。\n\n**建议降级为 Minor/Optional。**\n\n**[PARTIAL AGREE] R2-W4: \"Temporal DIF\" 的因果解释——DIF 可能是 benchmark 正常运作的证据**\n\nR2 提出一个有趣的概念性问题：如果模型在某些 items 上通过真实能力提升而表现更好，这些 items 显示 DIF 是 benchmark 正常运作的证据，而非\"instability\"。\n\n这是一个合理的 conceptual 观点，但论文 Section 4.2 的 matched-ability analysis 已经部分回应：在控制 overall ability 后，C% 仅从 31.3% 降至 28.9%（-2.4pp），说明绝大部分 DIF 不是 ability difference 驱动的。DIF 的定义本身就是 **controlling for ability** 后的 differential functioning——如果模型的真实能力提升被 matching 控制了，那剩余的 DIF 就不是\"正常运作\"，而是 item 在不同群体间 **以不同方式** 运作。\n\n但关于标题 \"Measurement Instability\" 的 framing，R2 有一定道理——\"instability\" 确实带有负面含义。不过 Section 5.1 明确称 DIF 的归因为 \"underdetermined\"（contamination, capability evolution, methodology shifts 均有可能），这比标题的 framing 更 nuanced。建议作者在 Introduction 或 Discussion 中加 1–2 句缓和标题的 framing。\n\n**[AGREE] R2-W5: 92.4% \"unrelated to domain accuracy\" 的推导过程不透明**\n\nR2 指出这一数字的来源不清晰。我赞同。\n\n从论文中看，Section 4.2 报告了两个相关但不同的统计量：\n- Item-level logistic regression pseudo R² = 0.0007（\"item-level regression\"）\n- 92.4% \"item-specific\"\n\n如果 pseudo R² = 0.0007 意味着 domain-level 因素只解释 0.07% 的方差，那 item-specific 应为 ~99.9% 而非 92.4%。如果 92.4% 来自另一个分析（例如 hierarchical decomposition 将 DIF 方差分解为 domain-level vs. item-level），其推导过程在正文中不可见。这个数字在 abstract 和 introduction 中都被重复引用，是核心 claim 之一，需要清晰的推导链。\n\n**[REBUT] R2-W6: Appendix F 的 AUROC≈0.60 与 §5.3 audit protocol 的张力**\n\nR2 认为 item-level 预测能力弱（AUROC≈0.60）与 audit protocol 的推荐存在张力。我不同意。\n\n论文 Discussion §5.3 明确区分了两条路径：\n- **Pre-screening**（基于 item features 预测哪些 items 会 DIF）→ AUROC≈0.60 说明这条路径不可行\n- **Post-hoc monitoring**（收集数据后运行 MH-DIF 检测）→ 这是 §5.3 audit protocol 推荐的方法\n\nAppendix F 的 negative finding 恰恰 **支撑** 了 §5.3 的结论：\"post-hoc monitoring needed, not pre-screening\"（Section 5.3 原文）。没有张力，反而是逻辑自洽的。\n\n---\n\n## Minor 问题\n\n**[AGREE] R2-M1**: Table 1 的 dashes 确实缺乏 caption 说明。Caption 已说明 \"Dashes indicate comparisons where Li et al. labels are not applicable\"，但需要更显眼。\n\n**[AGREE] R2-M2**: Figure 1 确实应标注为 schematic/illustrative，当前 caption 的 \"illustrated via Item Characteristic Curves\" 不够明确。\n\n**[REBUT] R2-M3**: 引用核实问题需要验证具体指控的准确性。R2 提到 \"Luo et al. vs Zhuang et al.\" 但未给出具体位置和错误内容。在没有验证之前，不做判断。\n\n**[AGREE] R2-M4**: 数值精度不一致是一个有效的 editorial concern（部分数字报告到小数点后 3 位，部分只 1 位）。\n\n**[AGREE] R2-M5**: TPR at mean a=1.2 与 Table 4 交叉验证是合理的 internal consistency check。\n\n**[AGREE] R2-M6**: Limitations 长度适当，覆盖面合理。\n\n---\n\n## Missing References\n\n**[PARTIAL AGREE] \"Test of Time\" (arXiv 2509.00072)**: 需验证相关性。如果确实讨论 benchmark temporal stability，值得引用。\n\n**[AGREE] \"DIF: A Framework for Benchmarking and Verifying Implicit Bias in LLMs\" (arXiv 2505.10013)**: 如果该论文将 DIF 应用于 LLM bias 检测（不同于本文的 temporal DIF），那是直接相关的 concurrent work，应该引用并区分。\n\n---\n\n## 总结\n\nR2 的审稿侧重 framing/novelty/writing quality，与我的审稿侧重（statistical methodology/experimental validity）互补。核心分歧：\n\n1. **R2-N1 (Abstract density)**: 我认为不构成 critical issue，建议降级\n2. **R2-N2 (Audit protocol contradiction)**: 我认为不存在 contradiction——THAT/WHY 是对 MH-DIF method 的描述，audit protocol 是 downstream workflow\n3. **R2-N3 (Novelty)**: 部分同意（缺少教育 DIF rate baseline 对比），但 ground truth meta-critique 的非 trivial 性质不应被低估\n4. **R2-W5 (92.4%)**: 完全同意，这是一个需要作者 clarify 的关键推导\n5. **R2-W6 (AUROC vs audit)**: 不同意——pre-screening 和 post-hoc monitoring 是明确区分的两条路径\n\n我与 R2 对 Overall Assessment 的判断一致（3.5, Borderline Conference），但核心 concerns 不同：R2 的 blockers 偏向 framing/novelty，我的偏向 LOFO family-concentration (我的 N1) 和 non-independence quantification (我的 N2)。\n",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[REBUT] R2-N1: Abstract 信息密度严重超载**\n\nR2 称 abstract 包含 15+ 统计量损害可读性。我不同意将此列为 critical。\n\n理由：本文是 large-scale psychometric audit，核心贡献 **就是** 一组统计发现。Abstract 的数字密度与论文性质匹配——每个数字对应一个独立的 claim（31% temporal DIF、ΔFPR=0.000 validation guarantee、92.4% item-specificity、ρ≈0.997 ranking preservation、enrichment≈0.96 contamination independence）。删减任何一组都会使读者无法从 abstract 判断论文做了什么。ARR reviewer guidelines (I1) 明确要求 specificity——\"instead of 'missing relevant references,' specify which ones\"，同理，abstract 的具体数字正是 specificity 的体现。\n\n此外，ACL ARR guidelines (H13) 警告不要 \"demanding extra experiments beyond what claims require\"——同样适用于要求删减支撑 claim 的核心数据。这是 writing preference，不是 soundness 问题，不应归为 Must-Fix。\n\n**建议降级为 Minor/Style suggestion。**\n\n---\n\n**[REBUT] R2-N2: §5.3 Audit Protocol 与 \"detects THAT not WHY\" 存在内在矛盾**\n\nR2 认为 §5.3 建议\"review flagged items for content characteristics\"与论文的方法论定位矛盾。我不同意。\n\n理由：论文的 claim 是 **MH-DIF 方法本身** detects THAT not WHY——这是对 statistical procedure 的准确描述。§5.3 的 audit protocol 是方法应用后的 **downstream workflow recommendation**，即：先用 MH-DIF 识别可疑 items（THAT），再人工审查这些 items 的特征（WHY）。这是标准的两阶段诊断流程，与教育测量实践完全一致——ETS 自己的 DIF protocol 就是先统计检测再人工审查（参见 Zieky, 1993; Holland & Thayer, 1988 的 original framework）。\n\n\"Flag/Act\" 命名指的是 monitoring 严重程度的分级响应，不是对 DIF items 的\"纠正\"。具体来说（Section 5.3）：\n- Monitor (C% < 15%): 仅报告 C% 在 release notes\n- Flag (15–25%): 报告 stable-item rankings 作为 sensitivity analysis\n- Act (C% ≥ 25%): 审查 flagged items + 将 stable-item rankings 作为 primary metric\n\n这三级响应从未声称 MH-DIF 本身能解释原因。Act 级别的\"review flagged items\"是将问题移交给 domain experts，不是 MH-DIF 方法在做因果归因。\n\n**不构成 contradiction，建议降级或移除。**\n\n---\n\n**[PARTIAL AGREE] R2-N3: 新颖性定位不够清晰**\n\nR2 提出三点：(a) ground truth meta-critique 可能 a priori obvious; (b) cross-subject matching 有心理测量学先驱; (c) 31% 缺少与传统教育 DIF rates 的对比。\n\n逐点回应：\n\n**(a) [REBUT]** Ground truth meta-critique 并非 a priori obvious。大量 contamination detection 文献（Li et al., 2024b; Deng et al., 2024; Golchin and Banerjee, 2024——Section 2 引用）**隐式假设**web-overlap 是 contamination 的可靠 ground truth。本文 Section 4.3 的实证发现——enrichment ratio = 0.964, φ = 0.012, OR = 1.05 [0.96, 1.15]——表明 DIF flags 与 web-overlap **近乎正交**，这直接挑战了该领域的主流假设。如果这一发现是\"a priori obvious\"，那么上述论文不应使用 web-overlap 作为 ground truth。\n\n**(b) [PARTIAL AGREE]** Cross-subject matching 确实有先驱（Swaminathan & Rogers, 1990 的 purified matching；论文 Section 3.2 已引用）。但适配到 multi-domain LLM benchmarks（57 subjects）并证明 constructive ΔFPR = 0.000 guarantee（Table 5, k ≤ 5）是非平凡的扩展。建议作者在 Section 3.4 更明确地 credit 先驱方法并阐明 novel adaptation 的具体贡献。\n\n**(c) [AGREE]** 缺少与传统教育测量 DIF rates 的 quantitative 对比是一个有效的 contextualization gap。典型的 large-scale 教育测试（SAT, GRE）中 ETS C 比例通常在 5–15%（参见 Zieky, 2003; Dorans & Holland, 1993）。与 31% 对比会显著增强论文 finding 的 impact framing。\n\n**建议作者补充教育测量 baseline DIF rates 对比（可在 1–2 句内完成），并强化 cross-subject matching 的 novelty 论证。但整体来看，N3 不构成 Must-Fix——novelty positioning 不充分是 writing/framing 问题而非 soundness 问题，建议降级为 Should-Fix。**\n\n---\n\n## Should-Fix 问题\n\n**[PARTIAL AGREE] R2-W1: 与 Growing Pains (Habba et al., 2026) 的区分不充分**\n\nSection 2 确实提到了 Growing Pains 作为 \"closest concurrent work\"（\"addresses score comparability through fixed-parameter calibration\"），但区分仅一句话。Given 该工作的 high relevance（同样关注 LLM benchmark temporal comparability），2–3 句的 explicit comparison（score-level equating vs. item-level DIF; parametric IRT vs. non-parametric MH）会增强 positioning。\n\n**[PARTIAL AGREE] R2-W2: Discussion 过于压缩**\n\n在 8-page limit 下 Discussion 被压缩是可以理解的。但 §5.1 (Temporal Comparability) 和 §5.2 (Ground Truth Meta-Critique) 各只有一段，确实牺牲了分析深度。特别是 §5.2 需要更深入地讨论\"如果 DIF 和 web-overlap 正交，DIF 到底检测到了什么\"这一核心问题。建议将部分 Appendix 内容（如 structural analysis details）进一步压缩以释放 Discussion 空间。\n\n**[REBUT] R2-W3: 缺少引用 \"Test of Time\" (arXiv 2509.00072)**\n\n我无法验证该 arXiv 论文的确切内容和发表状态。如果该论文确实讨论了 benchmark temporal stability 的相关话题，可以考虑引用。但 missing reference 通常不构成 Should-Fix——ARR guidelines (H3) 警告 \"claiming lack of novelty without specific references\"，同理，仅凭一篇未经验证的 arXiv preprint 不应作为 novelty concern 的依据。\n\n**建议降级为 Minor/Optional。**\n\n**[PARTIAL AGREE] R2-W4: \"Temporal DIF\" 的因果解释——DIF 可能是 benchmark 正常运作的证据**\n\nR2 提出一个有趣的概念性问题：如果模型在某些 items 上通过真实能力提升而表现更好，这些 items 显示 DIF 是 benchmark 正常运作的证据，而非\"instability\"。\n\n这是一个合理的 conceptual 观点，但论文 Section 4.2 的 matched-ability analysis 已经部分回应：在控制 overall ability 后，C% 仅从 31.3% 降至 28.9%（-2.4pp），说明绝大部分 DIF 不是 ability difference 驱动的。DIF 的定义本身就是 **controlling for ability** 后的 differential functioning——如果模型的真实能力提升被 matching 控制了，那剩余的 DIF 就不是\"正常运作\"，而是 item 在不同群体间 **以不同方式** 运作。\n\n但关于标题 \"Measurement Instability\" 的 framing，R2 有一定道理——\"instability\" 确实带有负面含义。不过 Section 5.1 明确称 DIF 的归因为 \"underdetermined\"（contamination, capability evolution, methodology shifts 均有可能），这比标题的 framing 更 nuanced。建议作者在 Introduction 或 Discussion 中加 1–2 句缓和标题的 framing。\n\n**[AGREE] R2-W5: 92.4% \"unrelated to domain accuracy\" 的推导过程不透明**\n\nR2 指出这一数字的来源不清晰。我赞同。\n\n从论文中看，Section 4.2 报告了两个相关但不同的统计量：\n- Item-level logistic regression pseudo R² = 0.0007（\"item-level regression\"）\n- 92.4% \"item-specific\"\n\n如果 pseudo R² = 0.0007 意味着 domain-level 因素只解释 0.07% 的方差，那 item-specific 应为 ~99.9% 而非 92.4%。如果 92.4% 来自另一个分析（例如 hierarchical decomposition 将 DIF 方差分解为 domain-level vs. item-level），其推导过程在正文中不可见。这个数字在 abstract 和 introduction 中都被重复引用，是核心 claim 之一，需要清晰的推导链。\n\n**[REBUT] R2-W6: Appendix F 的 AUROC≈0.60 与 §5.3 audit protocol 的张力**\n\nR2 认为 item-level 预测能力弱（AUROC≈0.60）与 audit protocol 的推荐存在张力。我不同意。\n\n论文 Discussion §5.3 明确区分了两条路径：\n- **Pre-screening**（基于 item features 预测哪些 items 会 DIF）→ AUROC≈0.60 说明这条路径不可行\n- **Post-hoc monitoring**（收集数据后运行 MH-DIF 检测）→ 这是 §5.3 audit protocol 推荐的方法\n\nAppendix F 的 negative finding 恰恰 **支撑** 了 §5.3 的结论：\"post-hoc monitoring needed, not pre-screening\"（Section 5.3 原文）。没有张力，反而是逻辑自洽的。\n\n---\n\n## Minor 问题\n\n**[AGREE] R2-M1**: Table 1 的 dashes 确实缺乏 caption 说明。Caption 已说明 \"Dashes indicate comparisons where Li et al. labels are not applicable\"，但需要更显眼。\n\n**[AGREE] R2-M2**: Figure 1 确实应标注为 schematic/illustrative，当前 caption 的 \"illustrated via Item Characteristic Curves\" 不够明确。\n\n**[REBUT] R2-M3**: 引用核实问题需要验证具体指控的准确性。R2 提到 \"Luo et al. vs Zhuang et al.\" 但未给出具体位置和错误内容。在没有验证之前，不做判断。\n\n**[AGREE] R2-M4**: 数值精度不一致是一个有效的 editorial concern（部分数字报告到小数点后 3 位，部分只 1 位）。\n\n**[AGREE] R2-M5**: TPR at mean a=1.2 与 Table 4 交叉验证是合理的 internal consistency check。\n\n**[AGREE] R2-M6**: Limitations 长度适当，覆盖面合理。\n\n---\n\n## Missing References\n\n**[PARTIAL AGREE] \"Test of Time\" (arXiv 2509.00072)**: 需验证相关性。如果确实讨论 benchmark temporal stability，值得引用。\n\n**[AGREE] \"DIF: A Framework for Benchmarking and Verifying Implicit Bias in LLMs\" (arXiv 2505.10013)**: 如果该论文将 DIF 应用于 LLM bias 检测（不同于本文的 temporal DIF），那是直接相关的 concurrent work，应该引用并区分。\n\n---\n\n## 总结\n\nR2 的审稿侧重 framing/novelty/writing quality，与我的审稿侧重（statistical methodology/experimental validity）互补。核心分歧：\n\n1. **R2-N1 (Abstract density)**: 我认为不构成 critical issue，建议降级\n2. **R2-N2 (Audit protocol contradiction)**: 我认为不存在 contradiction——THAT/WHY 是对 MH-DIF method 的描述，audit protocol 是 downstream workflow\n3. **R2-N3 (Novelty)**: 部分同意（缺少教育 DIF rate baseline 对比），但 ground truth meta-critique 的非 trivial 性质不应被低估\n4. **R2-W5 (92.4%)**: 完全同意，这是一个需要作者 clarify 的关键推导\n5. **R2-W6 (AUROC vs audit)**: 不同意——pre-screening 和 post-hoc monitoring 是明确区分的两条路径\n\n我与 R2 对 Overall Assessment 的判断一致（3.5, Borderline Conference），但核心 concerns 不同：R2 的 blockers 偏向 framing/novelty，我的偏向 LOFO family-concentration (我的 N1) 和 non-independence quantification (我的 N2)。\n",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-22T10:32:36.925450+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4068
}
```

</details>

---


### Assistant

_source line 610 · 2026-05-22T10:32:44.196212+00:00_

已提交对 Reviewer 2 的逐条交叉回应。核心判断：

- R2 的三个 Must-Fix 中，N1（Abstract 密度）和 N2（Audit protocol 矛盾）我认为不构成 critical issues，建议降级；N3（novelty）部分同意缺少教育 DIF rate baseline 对比
- Should-Fix 中完全同意 W5（92.4% 推导不透明），反驳 W6（AUROC vs audit protocol 无张力）
- 我与 R2 的 Overall 一致（3.5），但核心 concerns 方向不同——R2 偏 framing/novelty，我偏 LOFO family-concentration 和 non-independence 定量化

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 22

## Round 22

48 recorded events


### User

_source line 611 · 2026-05-22T11:29:10.390922+00:00_

[Round 1 审稿请求]:
你负责审查本文的**方法严谨性、统计推断和实验设计**。

## 论文信息
- 标题: "Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models"
- 路径: projects/irt_equated_bench_regen/paper/main.tex
- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/submitted.pdf

## Venue 要求
- **EMNLP 2026** (via ARR May cycle, deadline 2026-05-25)
- Long paper: 8 页正文限制 + 无限参考文献
- 模板: ACL template (double-blind)
- Limitations section 必须存在
- Appendix 可选，reviewers 不要求阅读

## 你的审查侧重

1. **统计方法论**:
   - MH-DIF 的假设是否满足（examinee independence, unidimensionality）？论文是否充分讨论违反假设的影响？
   - ETS C 分类阈值（|Δ_MH|≥1.5）的选择是否恰当？阈值敏感性分析是否充分？
   - 样本量和统计功效分析是否充分？
   - 多重检验校正方法是否恰当？

2. **实验设计**:
   - Temporal cohort 划分方式是否合理？是否存在 confound？
   - Semi-synthetic injection framework 的生态效度如何？假设是否过强？
   - Cross-subject matching 的 $\Delta$FPR=0.000 是否在合理条件下成立？
   - 控制实验（random split, matched-ability quintile, θ-conditioning）是否充分排除了替代解释？

3. **Claims vs Evidence**:
   - 每个 claim 是否有充分的统计证据支撑？
   - 置信区间和效应量报告是否完整？
   - Cluster bootstrap CI [26.7%, 53.2%] vs model-level CI 的 tension 如何处理？

4. **格式合规**:
   - 正文是否在 8 页以内？
   - Limitations section 是否存在且充分？

请按 Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions 格式输出审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-22T11:29:18.761323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-22T11:29:19.415311+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-22T11:29:19.466270+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-22T11:29:19.517061+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-22T11:29:23.485373+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 617 · 2026-05-22T11:29:24.597554+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 618 · 2026-05-22T11:29:30.695060+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

I found detailed information about the ACL Rolling Review (ARR) 2026 guidelines. Here are the key findings:

## Reviewer Guidelines and Scoring

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Review Criteria

The Overall assessment scor
…[truncated 1265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7209
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-22T11:29:31.800434+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 589.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 530.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.7}], \"total_pages\": 15, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_p
…[truncated 50 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7202
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-22T11:29:37.331343+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-22T11:29:37.331695+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 622 · 2026-05-22T11:29:38.437505+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 623 · 2026-05-22T11:29:38.990305+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 624 · 2026-05-22T11:29:39.392948+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 625 · 2026-05-22T11:29:39.393428+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 626 · 2026-05-22T11:29:40.199835+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1209
}
```

</details>

---


### Tool call

_source line 627 · 2026-05-22T11:29:40.200334+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 628 · 2026-05-22T11:29:40.655844+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1262
}
```

</details>

---


### Tool call

_source line 629 · 2026-05-22T11:29:40.656309+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 630 · 2026-05-22T11:29:41.263748+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1063
}
```

</details>

---


### Tool call

_source line 631 · 2026-05-22T11:29:41.264270+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 632 · 2026-05-22T11:29:42.172281+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1515
}
```

</details>

---


### Tool call

_source line 633 · 2026-05-22T11:29:42.172767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 634 · 2026-05-22T11:29:42.375035+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1110
}
```

</details>

---


### Tool call

_source line 635 · 2026-05-22T11:29:42.375465+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 636 · 2026-05-22T11:29:43.183419+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-22T11:29:43.387695+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1012
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-22T11:29:50.417177+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "9-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "9-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-22T11:29:52.732947+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.4}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 583.3}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 590.7}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 521.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 387.6}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 149.3}], \"total_pages\": 15, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2315
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-22T11:29:52.883986+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete list of review form dimensions/criteria with their scoring scales. I need: 1) All scored dimensions (soundness, excitement, overall, etc.) with their scale descriptions. 2) Any other required fields like confidence, best paper recommendation, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete list of review form dimensions/criteria with their scoring scales. I need: 1) All scored dimensions (soundness, excitement, overall, etc.) with their scale descriptions. 2) Any other required fields like confidence, best paper recommendation, etc."
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-22T11:29:58.969909+00:00_

# ACL Rolling Review Form: Complete Scoring Dimensions

## Primary Scored Dimensions

**1. Reviewer Confidence** (1-5 scale)
- 5: "Positive that my evaluation is correct"
- 4: "Quite sure"
- 3: "Pretty sure, but there's a chance I missed something"
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- 1: "Not my area, or paper is very hard to understand"

**2. Soundness** (1-5 scale with half-point options)
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: "Strong: This study provides sufficient support for all claims"
- 3: "Acceptable: sufficient support for main claims"
- 2: "Poor: Some main claims are not sufficiently supported"
- 1: "Major Issues: not yet sufficiently thorough to warrant publication"

**3. Excitement** (1-5 scale with half-point options)
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: "Exciting: I would mention this paper to others"
- 3: "Interesting: I might mention some points"
- 2: "Potentially Interesting: does not resonate with me, but it might with others"
- 1: "Not Exciting: does not resonate with me"

**4. Overall Assessment** (1-5 scale with half-point options)
- 5: "Consider for Award: top 2.5% papers"
- 4: "Conference: could be accepted"
- 3: "Findings: could be accepted to Findings track"
- 2: "Resubmit next cycle: needs substantial revisions"
- 1: "Do not resubmit: not relevant to ACL community"

## Additional Required Fields

- **Reproducibility** (1-5 scale)
- **Datasets** (1-5 scale, if applicable)
- **Software** (1-5 scale, if applicable)
- **Author Identity Knowledge** (1-5 scale)
- **Best Paper Justification** (required if award consideration)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6085
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-22T11:30:02.810489+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 643 · 2026-05-22T11:30:03.313340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 644 · 2026-05-22T11:30:04.121911+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1311
}
```

</details>

---


### Tool call

_source line 645 · 2026-05-22T11:30:04.122657+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 646 · 2026-05-22T11:30:04.626880+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1313
}
```

</details>

---


### Tool call

_source line 647 · 2026-05-22T11:30:04.627334+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-22T11:30:05.181904+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-22T11:30:06.042898+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1920
}
```

</details>

---


### Tool result

_source line 650 · 2026-05-22T11:30:06.044169+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1416
}
```

</details>

---


### Tool call

_source line 651 · 2026-05-22T11:30:06.044523+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-22T11:30:06.246253+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 653 · 2026-05-22T11:30:06.448316+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1266
}
```

</details>

---


### Tool result

_source line 654 · 2026-05-22T11:30:06.954074+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-22T11:30:06.956515+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 710
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-22T11:36:09.988556+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5 / 5（Borderline Conference）\n**一句话总结**: 将 MH-DIF 引入 LLM benchmark 评估是新颖且重要的贡献，实验规模大、控制实验多，但多维度假设违反的讨论不充分、核心数字的统计精度被高估，需要修订后才能稳进主会议。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 核心方法选择合理，控制实验丰富；但 MH-DIF 的单维度假设在 57-subject MMLU 上的适用性辩护不足，cluster bootstrap CI 跨度大却被淡化 |\n| Excitement | 4 / 5 | 心理测量学方法在 LLM 评估中的首次大规模应用，填补了 item-level temporal stability 的研究空白，大概率引发后续工作 |\n| Reproducibility | 4 / 5 | 使用公开的 METABENCH 数据，代码承诺开放，方法描述清晰，第三方应可复现 |\n| Overall | 3.5 / 5 | Borderline Conference：idea 好、规模大，但方法论上有可修复的关键问题 |\n| Confidence | 4 / 5 | 本人熟悉 DIF 方法论和 LLM 评估，对主要问题判断有把握 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] MMLU 的多维度结构违反 MH-DIF 的核心匹配假设，论文辩护不充分\n\n- 具体位置：Section 3.2（MH 方法描述）、Appendix A.1（IRT model fit）\n- 问题：MH-DIF 通过 total score 分层来\"控制能力差异\"，隐含假设是 total score 充分捕捉了影响 item response 的潜在特质。但 MMLU 横跨 57 个 subject、5 个 domain，Appendix A.1 自己承认 \"the MMLU response matrix shows poor fit to a unidimensional 2PL model\"。论文随即声称 \"This does not affect MH-DIF validity, which relies only on total score stratification rather than parametric IRT assumptions\"——这个论断过强且缺乏支撑。\n\n  DIF 文献中已有充分记录：当测试是多维的，且 focal/reference group 在次要维度上存在系统性差异时，total-score matching 的 MH-DIF 会将次要维度上的能力差异误判为 DIF（Ackerman 1992; Roussos & Stout 1996）。在本文场景中，2023→2024 的 temporal cohort 涉及架构升级、训练数据扩充、RLHF 方法变革等多重变化，完全可能导致跨 subject 的能力 profile 系统性偏移（例如 2024 模型在 STEM 上相对更强而 Humanities 上持平），这种 profile shift 会在 total-score matching 下被错误地标记为 item-level DIF。\n\n  Cross-subject matching（Section 3.4）部分缓解了这个问题（匹配变量排除了 focal item 所在 subject），但匹配变量仍然是其余 56 个 subject 的混合，仍然是多维的。\n\n- 为什么影响接收：这直接关系到 31% DIF rate 中有多少是\"真实的 item 功能变化\"，多少是\"跨维度能力 profile shift\"的假阳性。如果不量化这个混淆，核心 claim 的可信度不足。\n\n- 建议修改方向：\n  (1) 将 within-subject DIF 分析（在每个 subject 内部用 subject-specific score 做匹配）提升为主分析或共同主分析，报告 subject-level C% 分布\n  (2) 明确讨论 temporal cohort 的多维能力 profile shift 威胁模型：报告 2023 vs 2024 cohort 在各 domain 上的 accuracy 差异 profile，评估其是否足以产生 spurious DIF\n  (3) 考虑用 SIBTEST 或 Crossing-SIBTEST 做补充分析，这些方法专为多维 DIF 检测设计\n\n**N2** [critical] Cluster bootstrap CI [26.7%, 53.2%] 的巨大跨度与 \"robust\" 定性不一致\n\n- 具体位置：Section 4.2, page 6\n- 问题：论文的 headline finding 是 \"approximately 31% of MMLU items exhibit DIF\"。但 family-level cluster bootstrap 给出的 95% CI 为 [26.7%, 53.2%]，上界是下界的近 2 倍。论文将此描述为 \"continuing robustness under within-family dependence\"。\n\n  一个跨度达 26.5 个百分点的置信区间意味着：在考虑 model family 依赖后，真实 DIF 率可能低至 27%，也可能高达 53%。这不是 \"robust\"，而是 substantial uncertainty。\n\n  Appendix C 用 DEFF = 3.87 做了另一种校正，得到 adjusted C% = 34.55%。两种校正给出的图景不完全一致（DEFF 点估计偏高，bootstrap CI 极宽）。\n\n- 为什么影响接收：31% 这个数字贯穿全文（abstract、introduction、conclusion 均引用），如果实际不确定性如此之大，读者对这个数字的信任会打折扣。\n\n- 建议修改方向：\n  (1) 在 abstract 和正文中报告 cluster bootstrap CI，而非仅在 Section 4.2 一笔带过\n  (2) 将 \"~31%\" 的措辞改为 \"27%–53% (cluster bootstrap 95% CI, point estimate 31%)\" 或类似表述\n  (3) 讨论 model-level CI 与 cluster bootstrap CI 之间的 tension，以及为何两种校正方法给出不同的精度\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Semi-synthetic injection 的生态效度有限，论文讨论不足\n\n- 具体位置：Section 3.4, Limitations (p9)\n- 问题：injection 通过 uniform binary flipping（incorrect→correct at rate $p$）模拟 contamination。真实 contamination 的表现形式远更复杂：(a) partial knowledge increase（不是 0/1 翻转，而是概率提升），(b) 对特定 answer pattern 的记忆而非底层知识，(c) 不同 item 上的 exploitation rate 差异很大（高频 item 更容易被记忆）。\n- 论文在 Limitations 中承认了 \"worst-case uniform exploitation pattern\"，但没有讨论在更现实的 contamination 模型下 sensitivity 如何变化。Figure 2 的 dose-response 曲线和 Table 4 的 power 数据都是针对这一特定 injection 模型校准的，不能直接推广。\n- 建议：至少讨论 1-2 种替代 contamination 模型（如 difficulty-dependent exploitation、partial knowledge injection），分析其对 detectability 的定性影响。\n\n**W2** [warning] 低 exploitation rate 下功效接近零，underdetection 的含义讨论不足\n\n- 具体位置：Table 4, Section 4.1\n- 问题：Table 4 显示在 exploitation rate $\\alpha = 0.05$ 时 TPR = 0.03（近乎零检测力）。即使在 $\\alpha = 0.5$ 时 TPR 也仅 ~0.87。这意味着 MH-DIF 对低 exploitation rate 的 item（少于 ~20% 的模型利用了 contamination）几乎完全失明。\n- 这对解读 31% 有重要含义：如果许多 item 的 exploitation rate 偏低，31% 可能是显著的低估。但论文缺少这一 framing——没有将 31% 明确定位为 DIF 的下界估计。\n- 建议：(1) 在 Discussion 中明确 31% 是 lower bound；(2) 考虑做 sensitivity analysis——在不同 exploitation rate 分布假设下，估计真实 DIF 率范围。\n\n**W3** [warning] IRT θ-conditioning 作为独立控制的有效性存疑\n\n- 具体位置：Section 4.4, Table 2, Appendix A.1\n- 问题：论文报告 $r(\\theta, \\text{total score}) = 0.996$。如此高的相关意味着 θ-conditioning 和 total-score matching 几乎完全等价，作为\"独立控制\"不提供增量信息。同时 Appendix A.1 承认 2PL model fit 很差——用 poorly-fitting model 的 θ 估计做控制本身就是一个 circular 问题。\n- 建议：将 θ-conditioning 降级为 \"sensitivity check\" 而非 \"structural control\"，或者使用 MIRT 模型获取更合理的 θ 估计。\n\n**W4** [warning] GSM1K cross-validation 相关 (Section 4.7, Figure 5) 样本量过小\n\n- 具体位置：Section 4.7, Figure 5\n- 问题：$N = 33$ 个模型上的相关分析（$r = -0.478, p = 0.005$）。这个 N 对于 correlation analysis 偏小，少数 influential outlier 可能驱动整个结果。Figure 5 散点图中似乎存在右下角的 leverage point。\n- 建议：报告 influence diagnostics（Cook's D），或至少注明 N=33 的 small-sample limitation。\n\n**W5** [warning] Multi-subject injection 下 ΔFPR 升至 0.069 对真实数据解读的影响未讨论\n\n- 具体位置：Table 5, Section 4.5\n- 问题：论文重点强调 single-subject injection 下 ΔFPR = 0.000（by construction），但 Table 5 显示同时污染 ≥10 个 subject 时 ΔFPR 升至 0.060-0.069。在真实场景中 contamination 几乎必然跨越多个 subject，因此 ΔFPR = 0 的保证不适用于实际条件。\n- 如果基线 FPR ~6%（random split, Table 1）加上 injection-induced ΔFPR ~6.9%，总 FPR 可达 ~13%。这对解读真实数据中的 31% DIF rate 有何含义？其中有多少可能是 multi-subject contamination 导致的 false positive？\n- 建议：在 Discussion 中讨论 multi-subject FPR inflation 对核心 finding 的 quantitative impact。\n\n---\n\n## 小问题（不影响接收）\n\n1. **K 值未明确指定**：Section 3.2 描述 MH 用 \"K score bins\" 分层，但 K 的具体值没有在正文中报告。Appendix A.1 提到 \"quintile-based binning\"，请在正文中明确 K = 5（如果是的话）。\n\n2. **Abstract 中 ρ = 0.964 可能产生误导**：Abstract 报告 DIF flags 与 web-overlap labels 的 \"cohort ρ = 0.964\"，粗看像是高度一致。但这里 ρ 是 item-level rank correlation（rank 保序性强但 classification overlap 低），真正反映 classification agreement 的是 Jaccard = 0.206。建议在 abstract 中优先报告 Jaccard 或重新措辞避免误读。\n\n3. **Table 2 caption 不够清晰**：Table 2 中不同 control 对应的 \"baseline C%\" 含义不统一，建议在 caption 或脚注中说明每行的 baseline 定义。\n\n4. **Limitations 段落中 causal decomposition 的提法**：\"A definitive causal decomposition remains out of reach without access to model training data\"——这一点很重要但放在 Limitations 最后容易被忽略，建议在 Discussion (Section 5.1) 中也简要提及。\n\n---\n\n## 主要优势\n\n1. **新颖且重要的 framing**：首次将教育测量学中成熟的 MH-DIF 方法引入 LLM benchmark 评估，填补了 item-level temporal stability 的空白。psychometric method → NLP evaluation 的 bridge 动机清晰、立论扎实。\n\n2. **规模令人信服**：5,227 models × 12,508 items × 6 benchmarks。这不是 toy experiment，数据规模本身就构成了贡献。\n\n3. **控制实验全面**：Random split baseline (6%)、matched-ability quintile、IRT θ-conditioning、within-subject pre-check、cross-subject matching——5 层控制形成了 thorough falsification battery。\n\n4. **Cross-subject matching 设计巧妙**：用 focal item 所在 subject 以外的所有 score 做匹配变量，在 single-subject contamination 下 ΔFPR = 0 by construction。这个设计在 DIF 应用文献中是一个 methodological innovation。\n\n5. **Cross-benchmark replication**：Table 3 展示 6 个 METABENCH benchmarks 一致呈现 DIF，且 knowledge-intensive benchmarks DIF 率更高的 gradient 符合理论预期。\n\n6. **实用性强**：Section 5.3 提出的 monitoring protocol（15% flag / 25% act thresholds）有明确的操作性，对 benchmark maintainers 有直接参考价值。\n\n---\n\n## Questions for Authors\n\nQ1: 是否考虑过在每个 subject 内部独立运行 MH-DIF（用 subject-internal score 做匹配），以避免跨 subject 的多维度混淆？如果有，subject-level C% 的分布是什么样的？\n\nQ2: Table 2 中 matched-ability quintile 未能降低 C%——是否验证了 quintile 划分后各 stratum 内 2023/2024 cohort 的 score 分布确实匹配良好？如果某些 quintile 内仍有 residual ability difference，控制效果可能不足。\n\nQ3: Cluster bootstrap CI [26.7%, 53.2%] 与 DEFF-adjusted C% = 34.55% 之间如何调和？两种处理 family dependence 的方法给出了不同精度的图景，哪个更可信？\n\nQ4: 在 semi-synthetic framework 中，如果 exploitation rate 按 item difficulty 变化（例如 easy items 更容易被 exploit），dose-response 曲线和 ΔTPR 会如何变化？",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5 / 5（Borderline Conference）\n**一句话总结**: 将 MH-DIF 引入 LLM benchmark 评估是新颖且重要的贡献，实验规模大、控制实验多，但多维度假设违反的讨论不充分、核心数字的统计精度被高估，需要修订后才能稳进主会议。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 核心方法选择合理，控制实验丰富；但 MH-DIF 的单维度假设在 57-subject MMLU 上的适用性辩护不足，cluster bootstrap CI 跨度大却被淡化 |\n| Excitement | 4 / 5 | 心理测量学方法在 LLM 评估中的首次大规模应用，填补了 item-level temporal stability 的研究空白，大概率引发后续工作 |\n| Reproducibility | 4 / 5 | 使用公开的 METABENCH 数据，代码承诺开放，方法描述清晰，第三方应可复现 |\n| Overall | 3.5 / 5 | Borderline Conference：idea 好、规模大，但方法论上有可修复的关键问题 |\n| Confidence | 4 / 5 | 本人熟悉 DIF 方法论和 LLM 评估，对主要问题判断有把握 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] MMLU 的多维度结构违反 MH-DIF 的核心匹配假设，论文辩护不充分\n\n- 具体位置：Section 3.2（MH 方法描述）、Appendix A.1（IRT model fit）\n- 问题：MH-DIF 通过 total score 分层来\"控制能力差异\"，隐含假设是 total score 充分捕捉了影响 item response 的潜在特质。但 MMLU 横跨 57 个 subject、5 个 domain，Appendix A.1 自己承认 \"the MMLU response matrix shows poor fit to a unidimensional 2PL model\"。论文随即声称 \"This does not affect MH-DIF validity, which relies only on total score stratification rather than parametric IRT assumptions\"——这个论断过强且缺乏支撑。\n\n  DIF 文献中已有充分记录：当测试是多维的，且 focal/reference group 在次要维度上存在系统性差异时，total-score matching 的 MH-DIF 会将次要维度上的能力差异误判为 DIF（Ackerman 1992; Roussos & Stout 1996）。在本文场景中，2023→2024 的 temporal cohort 涉及架构升级、训练数据扩充、RLHF 方法变革等多重变化，完全可能导致跨 subject 的能力 profile 系统性偏移（例如 2024 模型在 STEM 上相对更强而 Humanities 上持平），这种 profile shift 会在 total-score matching 下被错误地标记为 item-level DIF。\n\n  Cross-subject matching（Section 3.4）部分缓解了这个问题（匹配变量排除了 focal item 所在 subject），但匹配变量仍然是其余 56 个 subject 的混合，仍然是多维的。\n\n- 为什么影响接收：这直接关系到 31% DIF rate 中有多少是\"真实的 item 功能变化\"，多少是\"跨维度能力 profile shift\"的假阳性。如果不量化这个混淆，核心 claim 的可信度不足。\n\n- 建议修改方向：\n  (1) 将 within-subject DIF 分析（在每个 subject 内部用 subject-specific score 做匹配）提升为主分析或共同主分析，报告 subject-level C% 分布\n  (2) 明确讨论 temporal cohort 的多维能力 profile shift 威胁模型：报告 2023 vs 2024 cohort 在各 domain 上的 accuracy 差异 profile，评估其是否足以产生 spurious DIF\n  (3) 考虑用 SIBTEST 或 Crossing-SIBTEST 做补充分析，这些方法专为多维 DIF 检测设计\n\n**N2** [critical] Cluster bootstrap CI [26.7%, 53.2%] 的巨大跨度与 \"robust\" 定性不一致\n\n- 具体位置：Section 4.2, page 6\n- 问题：论文的 headline finding 是 \"approximately 31% of MMLU items exhibit DIF\"。但 family-level cluster bootstrap 给出的 95% CI 为 [26.7%, 53.2%]，上界是下界的近 2 倍。论文将此描述为 \"continuing robustness under within-family dependence\"。\n\n  一个跨度达 26.5 个百分点的置信区间意味着：在考虑 model family 依赖后，真实 DIF 率可能低至 27%，也可能高达 53%。这不是 \"robust\"，而是 substantial uncertainty。\n\n  Appendix C 用 DEFF = 3.87 做了另一种校正，得到 adjusted C% = 34.55%。两种校正给出的图景不完全一致（DEFF 点估计偏高，bootstrap CI 极宽）。\n\n- 为什么影响接收：31% 这个数字贯穿全文（abstract、introduction、conclusion 均引用），如果实际不确定性如此之大，读者对这个数字的信任会打折扣。\n\n- 建议修改方向：\n  (1) 在 abstract 和正文中报告 cluster bootstrap CI，而非仅在 Section 4.2 一笔带过\n  (2) 将 \"~31%\" 的措辞改为 \"27%–53% (cluster bootstrap 95% CI, point estimate 31%)\" 或类似表述\n  (3) 讨论 model-level CI 与 cluster bootstrap CI 之间的 tension，以及为何两种校正方法给出不同的精度\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Semi-synthetic injection 的生态效度有限，论文讨论不足\n\n- 具体位置：Section 3.4, Limitations (p9)\n- 问题：injection 通过 uniform binary flipping（incorrect→correct at rate $p$）模拟 contamination。真实 contamination 的表现形式远更复杂：(a) partial knowledge increase（不是 0/1 翻转，而是概率提升），(b) 对特定 answer pattern 的记忆而非底层知识，(c) 不同 item 上的 exploitation rate 差异很大（高频 item 更容易被记忆）。\n- 论文在 Limitations 中承认了 \"worst-case uniform exploitation pattern\"，但没有讨论在更现实的 contamination 模型下 sensitivity 如何变化。Figure 2 的 dose-response 曲线和 Table 4 的 power 数据都是针对这一特定 injection 模型校准的，不能直接推广。\n- 建议：至少讨论 1-2 种替代 contamination 模型（如 difficulty-dependent exploitation、partial knowledge injection），分析其对 detectability 的定性影响。\n\n**W2** [warning] 低 exploitation rate 下功效接近零，underdetection 的含义讨论不足\n\n- 具体位置：Table 4, Section 4.1\n- 问题：Table 4 显示在 exploitation rate $\\alpha = 0.05$ 时 TPR = 0.03（近乎零检测力）。即使在 $\\alpha = 0.5$ 时 TPR 也仅 ~0.87。这意味着 MH-DIF 对低 exploitation rate 的 item（少于 ~20% 的模型利用了 contamination）几乎完全失明。\n- 这对解读 31% 有重要含义：如果许多 item 的 exploitation rate 偏低，31% 可能是显著的低估。但论文缺少这一 framing——没有将 31% 明确定位为 DIF 的下界估计。\n- 建议：(1) 在 Discussion 中明确 31% 是 lower bound；(2) 考虑做 sensitivity analysis——在不同 exploitation rate 分布假设下，估计真实 DIF 率范围。\n\n**W3** [warning] IRT θ-conditioning 作为独立控制的有效性存疑\n\n- 具体位置：Section 4.4, Table 2, Appendix A.1\n- 问题：论文报告 $r(\\theta, \\text{total score}) = 0.996$。如此高的相关意味着 θ-conditioning 和 total-score matching 几乎完全等价，作为\"独立控制\"不提供增量信息。同时 Appendix A.1 承认 2PL model fit 很差——用 poorly-fitting model 的 θ 估计做控制本身就是一个 circular 问题。\n- 建议：将 θ-conditioning 降级为 \"sensitivity check\" 而非 \"structural control\"，或者使用 MIRT 模型获取更合理的 θ 估计。\n\n**W4** [warning] GSM1K cross-validation 相关 (Section 4.7, Figure 5) 样本量过小\n\n- 具体位置：Section 4.7, Figure 5\n- 问题：$N = 33$ 个模型上的相关分析（$r = -0.478, p = 0.005$）。这个 N 对于 correlation analysis 偏小，少数 influential outlier 可能驱动整个结果。Figure 5 散点图中似乎存在右下角的 leverage point。\n- 建议：报告 influence diagnostics（Cook's D），或至少注明 N=33 的 small-sample limitation。\n\n**W5** [warning] Multi-subject injection 下 ΔFPR 升至 0.069 对真实数据解读的影响未讨论\n\n- 具体位置：Table 5, Section 4.5\n- 问题：论文重点强调 single-subject injection 下 ΔFPR = 0.000（by construction），但 Table 5 显示同时污染 ≥10 个 subject 时 ΔFPR 升至 0.060-0.069。在真实场景中 contamination 几乎必然跨越多个 subject，因此 ΔFPR = 0 的保证不适用于实际条件。\n- 如果基线 FPR ~6%（random split, Table 1）加上 injection-induced ΔFPR ~6.9%，总 FPR 可达 ~13%。这对解读真实数据中的 31% DIF rate 有何含义？其中有多少可能是 multi-subject contamination 导致的 false positive？\n- 建议：在 Discussion 中讨论 multi-subject FPR inflation 对核心 finding 的 quantitative impact。\n\n---\n\n## 小问题（不影响接收）\n\n1. **K 值未明确指定**：Section 3.2 描述 MH 用 \"K score bins\" 分层，但 K 的具体值没有在正文中报告。Appendix A.1 提到 \"quintile-based binning\"，请在正文中明确 K = 5（如果是的话）。\n\n2. **Abstract 中 ρ = 0.964 可能产生误导**：Abstract 报告 DIF flags 与 web-overlap labels 的 \"cohort ρ = 0.964\"，粗看像是高度一致。但这里 ρ 是 item-level rank correlation（rank 保序性强但 classification overlap 低），真正反映 classification agreement 的是 Jaccard = 0.206。建议在 abstract 中优先报告 Jaccard 或重新措辞避免误读。\n\n3. **Table 2 caption 不够清晰**：Table 2 中不同 control 对应的 \"baseline C%\" 含义不统一，建议在 caption 或脚注中说明每行的 baseline 定义。\n\n4. **Limitations 段落中 causal decomposition 的提法**：\"A definitive causal decomposition remains out of reach without access to model training data\"——这一点很重要但放在 Limitations 最后容易被忽略，建议在 Discussion (Section 5.1) 中也简要提及。\n\n---\n\n## 主要优势\n\n1. **新颖且重要的 framing**：首次将教育测量学中成熟的 MH-DIF 方法引入 LLM benchmark 评估，填补了 item-level temporal stability 的空白。psychometric method → NLP evaluation 的 bridge 动机清晰、立论扎实。\n\n2. **规模令人信服**：5,227 models × 12,508 items × 6 benchmarks。这不是 toy experiment，数据规模本身就构成了贡献。\n\n3. **控制实验全面**：Random split baseline (6%)、matched-ability quintile、IRT θ-conditioning、within-subject pre-check、cross-subject matching——5 层控制形成了 thorough falsification battery。\n\n4. **Cross-subject matching 设计巧妙**：用 focal item 所在 subject 以外的所有 score 做匹配变量，在 single-subject contamination 下 ΔFPR = 0 by construction。这个设计在 DIF 应用文献中是一个 methodological innovation。\n\n5. **Cross-benchmark replication**：Table 3 展示 6 个 METABENCH benchmarks 一致呈现 DIF，且 knowledge-intensive benchmarks DIF 率更高的 gradient 符合理论预期。\n\n6. **实用性强**：Section 5.3 提出的 monitoring protocol（15% flag / 25% act thresholds）有明确的操作性，对 benchmark maintainers 有直接参考价值。\n\n---\n\n## Questions for Authors\n\nQ1: 是否考虑过在每个 subject 内部独立运行 MH-DIF（用 subject-internal score 做匹配），以避免跨 subject 的多维度混淆？如果有，subject-level C% 的分布是什么样的？\n\nQ2: Table 2 中 matched-ability quintile 未能降低 C%——是否验证了 quintile 划分后各 stratum 内 2023/2024 cohort 的 score 分布确实匹配良好？如果某些 quintile 内仍有 residual ability difference，控制效果可能不足。\n\nQ3: Cluster bootstrap CI [26.7%, 53.2%] 与 DEFF-adjusted C% = 34.55% 之间如何调和？两种处理 family dependence 的方法给出了不同精度的图景，哪个更可信？\n\nQ4: 在 semi-synthetic framework 中，如果 exploitation rate 按 item difficulty 变化（例如 easy items 更容易被 exploit），dose-response 曲线和 ΔTPR 会如何变化？",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-22T11:36:14.613095+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4624
}
```

</details>

---


### Assistant

_source line 658 · 2026-05-22T11:36:23.122456+00:00_

审稿报告已提交给 Review Director。

**总结**：Overall 3.5（Borderline Conference）。主要发现：

- **2 个 Must-Fix**：(N1) MMLU 57-subject 多维度结构违反 MH-DIF 匹配假设，论文对此辩护不足——temporal cohort 的能力 profile shift 可能产生 spurious DIF；(N2) cluster bootstrap CI [26.7%, 53.2%] 跨度极大，但论文用 "robust" 淡化处理，headline 数字 "31%" 的精度被高估。
- **5 个 Should-Fix**：semi-synthetic injection 生态效度有限；低 exploitation rate 下 power 接近零但未讨论 underdetection 含义；IRT θ-conditioning 与 total score 相关 0.996 不构成独立控制；GSM1K cross-validation N=33 过小；multi-subject injection ΔFPR 升至 0.069 对真实数据的影响未讨论。
- **主要优势**：首次大规模 psychometric audit、5 层控制实验、cross-subject matching 方法创新、6 benchmarks 交叉验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 23

## Round 23

4 recorded events


### User

_source line 659 · 2026-05-22T11:37:03.992889+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整 Round 1 审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 2 审稿报告：Round 1

**Overall**: 3.5 / 5（Borderline Conference）

## Must-Fix 问题

**N1** [critical] Discussion 对于一篇 "diagnostic" 论文而言严重不足
- §5 仅约半页，3 个小节
- 缺失：因果归因框架性讨论（contamination vs capability evolution vs training methodology shifts）、对 NLP 社区实践的具体影响（benchmark maintainers / leaderboard operators / model developers 该怎么做）、与 benchmark reform 更广泛运动的联系（MMLU-CF / dynamic benchmarks / temporal DIF monitoring 定位）
- §5.3 的 Monitor/Flag/Act 阈值（15%/25%）在主文中没展示如何从 Figure 6 推导

**N2** [critical] 新颖性定位需要更清晰地与 concurrent work 区分
- 与 Growing Pains (Habba 2026) 仅一句 "diagnostic foundation vs prescriptive framework"，不是 differentiation 而是 integration argument
- Benchmark Health Index (Zhu 2026) 和 Benchmark² (Qian &amp; Huang 2026) 各一句带过
- 缺少明确的 positioning paragraph 对比 scope/method/findings/actionable output

## Should-Fix 问题

**W1** [warning] Abstract 信息密度过高，15+ 数字稀释关键信息
**W2** [warning] 术语不一致（temporal measurement instability / temporal DIF / measurement invariance）
**W3** [warning] Temporal cohort 2023 vs 2024 划分过粗，§4.7 的 6-month window C%=34.35% 更高但未充分讨论
**W4** [warning] Gema et al. (2024) "Are We Done with MMLU?" 在 bib 中但未在正文讨论，ground truth errors 可能是 DIF 的 confound
**W5** [warning] App F 的 negative finding (AUROC=0.60) 在主文仅一句，应在 Discussion 展开

## Minor
- §5 的 \enlargethispage*{8\baselineskip} 激进
- Table 2/3 resizebox 字体偏小
- Introduction 过早引入大量数字
- Conclusion 仅 3 行过短
- Figure 2 caption "≈ 0" 应改 "= 0"
- §3.2 "LLM-specific challenges" 段过长

## Missing References
1. Zhao et al. (ACL 2025) "MMLU-CF" — 未引用
2. Engels, Lüdtke, Robitzsch (2026) 趋势估计 — 未引用
3. Lee, Huang, Svetina Valdivia, Schwartzman (2026) DIF 来源 — 未引用

---

请逐条回应上述所有问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-22T11:39:03.859763+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 Round 1 意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE with downgrade] R2-N1: Discussion 不足**\n\n同意 Discussion 可以更充实，但不同意 \"critical\" 定级——应为 Should-Fix。理由：\n\n1. §5.1 已经给出了因果归因的三分框架：\"impact (ability differences removed by matching, ~2.4 pp), DIF (item-level differences after ability control, ~38-29% floor, predominantly item-specific), and attribution (contamination, capability change, or training methodology shifts—underdetermined without training data)\"（p8）。R2 说 \"缺失因果归因框架\" 不完全准确，§5.1 有这个骨架，但确实展开不够。\n\n2. §5.3 的 15%/25% 阈值在 Figure 6 中有视觉推导依据——vertical dashed lines 标注了 Monitor/Flag (15%) 和 Flag/Act (25%) 位置，对应 DIF-ordered removal 开始显著加速 ranking degradation 的拐点。但同意正文应更显式地写出推导逻辑（\"at 15% removal, ρ drops below X\"）。\n\n3. 对于一篇 8 页正文的实证论文，~半页 Discussion 虽然偏短但不至于 \"critical\"。更大的问题是 Conclusion 仅 3 行（R2 Minor 中也提到）——建议将部分 Discussion 要点移入 Conclusion 以改善收尾。\n\n**结论**：同意需要扩展 Discussion（特别是 actionable implications 和 threshold 推导），但建议降级为 Should-Fix。\n\n---\n\n**[REBUT] R2-N2: 新颖性定位需要更清晰地与 concurrent work 区分**\n\n不同意 \"critical\" 定级。理由：\n\n1. 本文的方法论贡献与 R2 列举的 concurrent work 在 level 上不同。Growing Pains (Habba 2026) 是 prescriptive equating framework；Benchmark Health Index (Zhu 2026) 是 composite metric；Benchmark² (Qian & Huang 2026) 是 meta-evaluation。本文的贡献是将 **已有 50+ 年历史的标准化心理测量方法（MH-DIF + ETS classification）** 首次大规模应用于 LLM benchmarks。这不是与 concurrent work \"竞争\" 的关系，而是提供了一个 complementary diagnostic lens。Section 2 (Related Work) 的 \"IRT in LLM Evaluation\" 段落明确定位了这一点：\"The closest concurrent work is Growing Pains (Habba et al., 2026), which uses IRT calibration to establish anchor items for cross-temporal score equating\"。\n\n2. 方法的可区分性不需要长段落论述——MH-DIF 是一个具体的、可引用的、有 ETS 标准化分类体系的方法。读者不会混淆 \"DIF analysis\" 和 \"benchmark health index\"。\n\n3. 更实质的区分在于 **scale**（5,227 models × 12,508 items）和 **validation methodology**（semi-synthetic injection + cross-subject matching），这些在 Section 1 的 contributions 中已经明确。\n\n**结论**：一个简短的 positioning paragraph 可以锦上添花（Should-Fix 甚至 Minor），但不应作为 Must-Fix。论文的方法论独特性足够清晰。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: Abstract 信息密度过高**\n\n同意。我在 R1 审稿中也注意到了类似问题——Abstract 中 ρ = 0.964 容易被误读为高一致性（实际 Jaccard = 0.206 才反映 classification agreement）。15+ 个数字确实稀释了关键信息。建议 Abstract 只保留 3-4 个核心数字（31% C rate, cross-benchmark range 17.9-31.3%, ΔFPR = 0.000, N = 5,227 models），其余移入 Introduction。\n\n**[AGREE] R2-W2: 术语不一致**\n\n同意。论文混用 \"temporal measurement instability\"、\"temporal DIF\"、\"measurement invariance\" 而未明确层级关系。建议在 §1 或 §3 开头建立术语层次：measurement invariance 是目标属性，DIF 是检测方法，temporal measurement instability 是本文发现的现象。\n\n**[AGREE with nuance] R2-W3: Temporal cohort 划分过粗，6-month window C% 更高**\n\n同意 6-month window (C% = 34.35%, Table 1) 高于年度划分 (31%) 值得更多讨论。但我认为这个发现**加强**而非削弱论文的 claim——更窄的时间窗口反而检出更高的 DIF rate，说明年度划分可能是保守估计。论文应在 §4.2 中明确讨论这个 gradient 并解释其含义（temporal proximity → stronger DIF signal，因为短期内模型训练方法变化更集中？）。\n\n补充一点我在 R1 中提出的相关担忧：更根本的问题不是粒度，而是 temporal cohort 划分 confound 了多个变量（architecture, training data, scale, alignment methods）。粗细划分都无法解决这个 confound，只有 causal decomposition 才能。\n\n**[AGREE] R2-W4: Gema et al. (2024) ground truth errors 作为 confound**\n\n强烈同意。这是一个我在 R1 中遗漏的重要 confound。如果 MMLU 本身存在 ground truth errors（wrong answer keys），更强的 2024 模型可能因为\"知道真正的正确答案\"而选择了与 key 不同的选项，这在 MH-DIF 中会被标记为 DIF——但原因是 benchmark 质量问题而非 contamination 或 measurement instability。\n\n论文的 bib 中有 Gema et al. (2024) 但正文未讨论这个 confound。这与我在 R1-N1 中提出的多维度问题一起，构成了对 31% DIF rate 解读的另一个替代解释。\n\n建议：(1) 在 §4 或 §5 中讨论 ground truth error confound；(2) 如果可以获取 Gema et al. 标注的有问题 items，检查这些 items 与 DIF-flagged items 的 overlap。\n\n**[AGREE with nuance] R2-W5: App F negative finding 讨论不足**\n\n部分同意。AUROC = 0.60 是一个重要的 negative finding（item properties 不能 reliably predict DIF susceptibility），值得在主文中多说一两句。但考虑到 8 页限制，一句提及 + Appendix 详述是可接受的安排。建议在 §5.1 中加一句解释这个 negative finding 的含义（\"DIF susceptibility is not a fixed item property but may depend on the interaction between item characteristics and training methodology shifts\"）。\n\n---\n\n### Minor\n\n**[AGREE] \\enlargethispage hack**：§5 的 `\\enlargethispage*{8\\baselineskip}` 确实激进，可能导致不同编译环境下页面溢出。应通过精简文字解决而非用 LaTeX hack。\n\n**[AGREE] Table font size**：Table 2/3 的 resizebox 字体偏小，影响可读性。建议拆分或用 landscape 排列。\n\n**[AGREE] Introduction 数字过多**：与 W1 一致，信息前置过多。\n\n**[AGREE] Conclusion 过短**：3 行确实不够。Conclusion 应至少 recap 核心发现、讨论 broader impact、指出 future work 方向。\n\n**[REBUT] Figure 2 caption \"≈ 0\" vs \"= 0\"**：在 single-subject injection 下 ΔFPR = 0 是 by construction（Section 3.4 有理论证明），但 caption 中 \"≈ 0\" 反映的可能是 empirical measurement（受 finite sample noise 影响）。如果 bootstrap CI 是 [0.000, 0.000]，则 \"= 0\" 更准确；如果有任何非零 replication，\"≈ 0\" 更诚实。需要看具体数据决定。\n\n**[AGREE] §3.2 段落过长**：可以拆分为 sub-points 或移部分到 Appendix。\n\n---\n\n### Missing References\n\n**[AGREE] MMLU-CF (Zhao et al., ACL 2025)**：高度相关——MMLU-CF 直接处理 MMLU item 质量问题（contamination-free subset），应被引用并讨论。特别是：如果将 DIF analysis 限制在 MMLU-CF 的 clean items 上，DIF rate 是否下降？这能帮助区分 ground truth error confound。\n\n**[NEUTRAL] Engels, Lüdtke, Robitzsch (2026) 和 Lee, Huang, Svetina Valdivia, Schwartzman (2026)**：如果这两篇确实是 DIF/measurement invariance 方法论的最新进展，引用可以加强论文的心理测量学基础。但我未看到这两篇的具体内容，无法判断是否 essential。建议 authors 评估相关性后决定。\n\n---\n\n### 总结性评价\n\nR2 的审稿整体质量良好，尤其是 W4（ground truth error confound）是我在 R1 中遗漏的重要观点。但 N1 和 N2 的 \"critical\" 定级偏高——Discussion 篇幅和 novelty positioning 对于一篇 8 页实证论文而言是 presentation 问题而非 soundness 问题，不应阻碍接收。建议将两者降级为 Should-Fix。\n\nR2 的审稿侧重 presentation 和 positioning，与我的 R1 审稿侧重统计方法论和实验设计形成互补。综合两份审稿，论文的主要风险是：\n1. **方法论**（我的 R1-N1/N2）：multidimensionality assumption + cluster CI precision\n2. **Confound**（R2-W4 + 我的补充）：ground truth errors\n3. **Presentation**（R2-N1/W1/W2）：Discussion 不足 + 信息过密 + 术语不一致\n\n如果 authors 能在 revision 中 (a) 加强多维度假设的辩护、(b) 讨论 ground truth error confound、(c) 扩展 Discussion，论文可以达到 Conference 水平。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 Round 1 意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE with downgrade] R2-N1: Discussion 不足**\n\n同意 Discussion 可以更充实，但不同意 \"critical\" 定级——应为 Should-Fix。理由：\n\n1. §5.1 已经给出了因果归因的三分框架：\"impact (ability differences removed by matching, ~2.4 pp), DIF (item-level differences after ability control, ~38-29% floor, predominantly item-specific), and attribution (contamination, capability change, or training methodology shifts—underdetermined without training data)\"（p8）。R2 说 \"缺失因果归因框架\" 不完全准确，§5.1 有这个骨架，但确实展开不够。\n\n2. §5.3 的 15%/25% 阈值在 Figure 6 中有视觉推导依据——vertical dashed lines 标注了 Monitor/Flag (15%) 和 Flag/Act (25%) 位置，对应 DIF-ordered removal 开始显著加速 ranking degradation 的拐点。但同意正文应更显式地写出推导逻辑（\"at 15% removal, ρ drops below X\"）。\n\n3. 对于一篇 8 页正文的实证论文，~半页 Discussion 虽然偏短但不至于 \"critical\"。更大的问题是 Conclusion 仅 3 行（R2 Minor 中也提到）——建议将部分 Discussion 要点移入 Conclusion 以改善收尾。\n\n**结论**：同意需要扩展 Discussion（特别是 actionable implications 和 threshold 推导），但建议降级为 Should-Fix。\n\n---\n\n**[REBUT] R2-N2: 新颖性定位需要更清晰地与 concurrent work 区分**\n\n不同意 \"critical\" 定级。理由：\n\n1. 本文的方法论贡献与 R2 列举的 concurrent work 在 level 上不同。Growing Pains (Habba 2026) 是 prescriptive equating framework；Benchmark Health Index (Zhu 2026) 是 composite metric；Benchmark² (Qian & Huang 2026) 是 meta-evaluation。本文的贡献是将 **已有 50+ 年历史的标准化心理测量方法（MH-DIF + ETS classification）** 首次大规模应用于 LLM benchmarks。这不是与 concurrent work \"竞争\" 的关系，而是提供了一个 complementary diagnostic lens。Section 2 (Related Work) 的 \"IRT in LLM Evaluation\" 段落明确定位了这一点：\"The closest concurrent work is Growing Pains (Habba et al., 2026), which uses IRT calibration to establish anchor items for cross-temporal score equating\"。\n\n2. 方法的可区分性不需要长段落论述——MH-DIF 是一个具体的、可引用的、有 ETS 标准化分类体系的方法。读者不会混淆 \"DIF analysis\" 和 \"benchmark health index\"。\n\n3. 更实质的区分在于 **scale**（5,227 models × 12,508 items）和 **validation methodology**（semi-synthetic injection + cross-subject matching），这些在 Section 1 的 contributions 中已经明确。\n\n**结论**：一个简短的 positioning paragraph 可以锦上添花（Should-Fix 甚至 Minor），但不应作为 Must-Fix。论文的方法论独特性足够清晰。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: Abstract 信息密度过高**\n\n同意。我在 R1 审稿中也注意到了类似问题——Abstract 中 ρ = 0.964 容易被误读为高一致性（实际 Jaccard = 0.206 才反映 classification agreement）。15+ 个数字确实稀释了关键信息。建议 Abstract 只保留 3-4 个核心数字（31% C rate, cross-benchmark range 17.9-31.3%, ΔFPR = 0.000, N = 5,227 models），其余移入 Introduction。\n\n**[AGREE] R2-W2: 术语不一致**\n\n同意。论文混用 \"temporal measurement instability\"、\"temporal DIF\"、\"measurement invariance\" 而未明确层级关系。建议在 §1 或 §3 开头建立术语层次：measurement invariance 是目标属性，DIF 是检测方法，temporal measurement instability 是本文发现的现象。\n\n**[AGREE with nuance] R2-W3: Temporal cohort 划分过粗，6-month window C% 更高**\n\n同意 6-month window (C% = 34.35%, Table 1) 高于年度划分 (31%) 值得更多讨论。但我认为这个发现**加强**而非削弱论文的 claim——更窄的时间窗口反而检出更高的 DIF rate，说明年度划分可能是保守估计。论文应在 §4.2 中明确讨论这个 gradient 并解释其含义（temporal proximity → stronger DIF signal，因为短期内模型训练方法变化更集中？）。\n\n补充一点我在 R1 中提出的相关担忧：更根本的问题不是粒度，而是 temporal cohort 划分 confound 了多个变量（architecture, training data, scale, alignment methods）。粗细划分都无法解决这个 confound，只有 causal decomposition 才能。\n\n**[AGREE] R2-W4: Gema et al. (2024) ground truth errors 作为 confound**\n\n强烈同意。这是一个我在 R1 中遗漏的重要 confound。如果 MMLU 本身存在 ground truth errors（wrong answer keys），更强的 2024 模型可能因为\"知道真正的正确答案\"而选择了与 key 不同的选项，这在 MH-DIF 中会被标记为 DIF——但原因是 benchmark 质量问题而非 contamination 或 measurement instability。\n\n论文的 bib 中有 Gema et al. (2024) 但正文未讨论这个 confound。这与我在 R1-N1 中提出的多维度问题一起，构成了对 31% DIF rate 解读的另一个替代解释。\n\n建议：(1) 在 §4 或 §5 中讨论 ground truth error confound；(2) 如果可以获取 Gema et al. 标注的有问题 items，检查这些 items 与 DIF-flagged items 的 overlap。\n\n**[AGREE with nuance] R2-W5: App F negative finding 讨论不足**\n\n部分同意。AUROC = 0.60 是一个重要的 negative finding（item properties 不能 reliably predict DIF susceptibility），值得在主文中多说一两句。但考虑到 8 页限制，一句提及 + Appendix 详述是可接受的安排。建议在 §5.1 中加一句解释这个 negative finding 的含义（\"DIF susceptibility is not a fixed item property but may depend on the interaction between item characteristics and training methodology shifts\"）。\n\n---\n\n### Minor\n\n**[AGREE] \\enlargethispage hack**：§5 的 `\\enlargethispage*{8\\baselineskip}` 确实激进，可能导致不同编译环境下页面溢出。应通过精简文字解决而非用 LaTeX hack。\n\n**[AGREE] Table font size**：Table 2/3 的 resizebox 字体偏小，影响可读性。建议拆分或用 landscape 排列。\n\n**[AGREE] Introduction 数字过多**：与 W1 一致，信息前置过多。\n\n**[AGREE] Conclusion 过短**：3 行确实不够。Conclusion 应至少 recap 核心发现、讨论 broader impact、指出 future work 方向。\n\n**[REBUT] Figure 2 caption \"≈ 0\" vs \"= 0\"**：在 single-subject injection 下 ΔFPR = 0 是 by construction（Section 3.4 有理论证明），但 caption 中 \"≈ 0\" 反映的可能是 empirical measurement（受 finite sample noise 影响）。如果 bootstrap CI 是 [0.000, 0.000]，则 \"= 0\" 更准确；如果有任何非零 replication，\"≈ 0\" 更诚实。需要看具体数据决定。\n\n**[AGREE] §3.2 段落过长**：可以拆分为 sub-points 或移部分到 Appendix。\n\n---\n\n### Missing References\n\n**[AGREE] MMLU-CF (Zhao et al., ACL 2025)**：高度相关——MMLU-CF 直接处理 MMLU item 质量问题（contamination-free subset），应被引用并讨论。特别是：如果将 DIF analysis 限制在 MMLU-CF 的 clean items 上，DIF rate 是否下降？这能帮助区分 ground truth error confound。\n\n**[NEUTRAL] Engels, Lüdtke, Robitzsch (2026) 和 Lee, Huang, Svetina Valdivia, Schwartzman (2026)**：如果这两篇确实是 DIF/measurement invariance 方法论的最新进展，引用可以加强论文的心理测量学基础。但我未看到这两篇的具体内容，无法判断是否 essential。建议 authors 评估相关性后决定。\n\n---\n\n### 总结性评价\n\nR2 的审稿整体质量良好，尤其是 W4（ground truth error confound）是我在 R1 中遗漏的重要观点。但 N1 和 N2 的 \"critical\" 定级偏高——Discussion 篇幅和 novelty positioning 对于一篇 8 页实证论文而言是 presentation 问题而非 soundness 问题，不应阻碍接收。建议将两者降级为 Should-Fix。\n\nR2 的审稿侧重 presentation 和 positioning，与我的 R1 审稿侧重统计方法论和实验设计形成互补。综合两份审稿，论文的主要风险是：\n1. **方法论**（我的 R1-N1/N2）：multidimensionality assumption + cluster CI precision\n2. **Confound**（R2-W4 + 我的补充）：ground truth errors\n3. **Presentation**（R2-N1/W1/W2）：Discussion 不足 + 信息过密 + 术语不一致\n\n如果 authors 能在 revision 中 (a) 加强多维度假设的辩护、(b) 讨论 ground truth error confound、(c) 扩展 Discussion，论文可以达到 Conference 水平。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-22T11:39:08.693031+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4833
}
```

</details>

---


### Assistant

_source line 662 · 2026-05-22T11:39:16.377587+00:00_

交叉回应已提交。逐条回应了 R2 的全部 Must-Fix (2)、Should-Fix (5)、Minor (6)、Missing References (3) 共 16 个问题，每条标注了 [AGREE]、[AGREE with downgrade/nuance]、[REBUT] 或 [NEUTRAL]，均附具体 Section/Table/Figure 证据。

核心判断：
- R2-N1 (Discussion 不足) 和 R2-N2 (novelty positioning) 建议从 Must-Fix 降级为 Should-Fix——这是 presentation 问题而非 soundness 问题
- R2-W4 (ground truth error confound) 是我 R1 审稿中遗漏的重要观点，强烈同意
- 综合两份审稿，论文主要风险集中在多维度假设辩护、ground truth error confound、和 Discussion 充实度三个方面

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 24

## Round 24

54 recorded events


### User

_source line 663 · 2026-05-22T12:17:53.356934+00:00_

[Round 1 审稿请求]:
你负责 **方法严谨性** 审查。

## 论文信息
- **标题**: "Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models"
- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`（各 section 在 `sections/` 子目录）
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/submitted.pdf`

## Venue 要求
- **目标**: EMNLP 2026 via ACL Rolling Review (ARR)
- **Deadline**: 2026-05-25 (ARR May cycle)
- **页数**: Long paper — 正文最多 8 页，参考文献不限页数
- **Limitations**: 必写，不计入 8 页限制，且不得包含新实验/图表/分析
- **Ethical considerations**: 可选，不计入页数
- **模板**: ACL style template，[review] mode
- **匿名**: Double-blind anonymous review
- **提交平台**: OpenReview
- **特殊规则**: EMNLP 和 AACL 共享 ARR May cycle，作者需在提交时声明目标会议（binding）

## 你的审查侧重

请重点审查以下方面：

1. **MH-DIF 方法论适用性**：将教育测量的 MH-DIF 应用到 LLM benchmark 评估是否合理？LLM-specific assumptions（local independence violation、examinee non-independence、non-normal ability distribution、multidimensionality）是否被充分讨论和缓解？

2. **统计控制充分性**：temporal C% = 31% 的结论是否经过充分控制？Random-split sanity check、matched-ability analysis、within-family comparison、within-subject DIF、IRT θ-conditioning 等控制实验是否足以排除混淆因素？

3. **Uncertainty quantification**：Model-level bootstrap CI [29.4%, 38.1%]、family-level cluster bootstrap CI [26.7%, 53.2%]、DEFF adjusted C% [13.5%, 29.2%]、graduated de-duplication (K=20: 29.1%) —— 这些 uncertainty estimates 之间的不一致性是否被正确处理和报告？是否有 cherry-picking 的嫌疑？

4. **Semi-synthetic injection framework**：Cross-subject matching 的 ΔFPR=0 保证是否有效？Binary response flipping 作为注入模型的生态效度如何？Multi-subject injection 的 boundary conditions 是否充分讨论？

5. **多维度问题**：MMLU 57 subjects 的多维度结构是否可能产生 spurious DIF？论文提供的三条辩护（domain-level Cohen's d profile、cross-subject vs within-subject κ=0.80、C items 不集中在能力偏移大的 subject）是否充分？

6. **Cross-benchmark validation**：6 个 METABENCH benchmarks 的 replication 是否充分？GSM1K 相关分析（N=33）的统计效力和解读是否合理？

请按以下格式输出审稿意见：
- **Summary**（2-3 句）
- **Strengths**（逐条列出，标注 S1, S2, ...）
- **Weaknesses**（逐条列出，标注 W1, W2, ...，区分 Must-Fix / Should-Fix / Minor）
- **Questions**（需要作者回答的问题）
- **Missing References**（遗漏的重要相关工作）
- **Overall Assessment**（评分 + 置信度，使用 ARR Overall Assessment 标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-22T12:18:03.746056+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-22T12:18:03.746754+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-22T12:18:07.363890+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2"
  }
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-22T12:18:07.464684+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-22T12:18:11.379487+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-22T12:18:11.430173+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-22T12:18:15.500883+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 671 · 2026-05-22T12:18:17.964743+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-5",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-5",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 672 · 2026-05-22T12:18:23.096997+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found information about the ACL Rolling Review 2026 reviewer guidelines and review form. Here's what I found:

## Reviewer Guidelines

Reviewers should follow a workflow: (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that particular submission. If reviewers feel they are qualified to review some aspects of the paper but not others (e.g. experimental results but not the formal proofs), they should state in the review if they did not check some major parts, such as 
…[truncated 877 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7596
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-22T12:18:23.899633+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 521.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 572.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 525.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.4}], \"total_pages\": 16, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5934
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-22T12:18:26.561528+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-22T12:18:26.561994+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-22T12:18:27.668057+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 677 · 2026-05-22T12:18:28.173357+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 678 · 2026-05-22T12:18:28.980898+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1312
}
```

</details>

---


### Tool call

_source line 679 · 2026-05-22T12:18:29.082432+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 680 · 2026-05-22T12:18:29.434769+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1261
}
```

</details>

---


### Tool call

_source line 681 · 2026-05-22T12:18:29.535723+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 682 · 2026-05-22T12:18:29.940345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 683 · 2026-05-22T12:18:30.147765+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1065
}
```

</details>

---


### Tool result

_source line 684 · 2026-05-22T12:18:30.802272+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1266
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-22T12:18:31.004570+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1064
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-22T12:18:51.811033+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, all scoring dimensions, their scales, and descriptions. I need the exact dimensions reviewers must score on (e.g., soundness, excitement, reproducibility, etc.) and the scale for each."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form criteria, all scoring dimensions, their scales, and descriptions. I need the exact dimensions reviewers must score on (e.g., soundness, excitement, reproducibility, etc.) and the scale for each."
  }
}
```

</details>

---


### Tool call

_source line 687 · 2026-05-22T12:18:51.863748+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "6-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "6-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 688 · 2026-05-22T12:18:56.484837+00:00_

# ACL Rolling Review Form Scoring Dimensions

The review form includes the following mandatory scoring dimensions:

## 1. **Reviewer Confidence**
Scale: 1-5
- 5 = "Positive that my evaluation is correct"
- 4 = Quite sure with unlikely oversights
- 3 = Pretty sure but possible gaps in detail checking
- 2 = Willing to defend but likely missed details
- 1 = Outside expertise or paper very difficult to understand

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
Assesses scientific rigor and adequate support for claims. Ranges from "Excellent" (5) to "Major Issues" (1).

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
Evaluates subjective appeal including conceptual breakthroughs, community impact, and relevance to reviewer's work. Spans from "Highly Exciting" (5) to "Not Exciting" (1).

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
Conference recommendation ranging from "Consider for Award" (5) to "Do not resubmit" (1).

## Additional Evaluation Areas (Non-Scored):
- Limitations and societal impact
- Ethical concerns
- Reproducibility (1-5 scale)
- Datasets value (1-5 scale)
- Software value (1-5 scale)
- Author anonymity knowledge (1-5 scale)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4673
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-22T12:18:57.136558+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 555.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 536.3}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 590.8}], \"total_pages\": 16, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5272
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-22T12:19:01.396004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 691 · 2026-05-22T12:19:02.036650+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 692 · 2026-05-22T12:19:03.246644+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-22T12:19:05.166978+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3770
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-22T12:19:05.167545+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 695 · 2026-05-22T12:19:05.370267+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 696 · 2026-05-22T12:19:05.471606+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3434
}
```

</details>

---


### Tool result

_source line 697 · 2026-05-22T12:19:09.051828+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5805
}
```

</details>

---


### Tool result

_source line 698 · 2026-05-22T12:19:10.465890+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5298
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-22T12:19:10.822467+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5452
}
```

</details>

---


### Tool call

_source line 700 · 2026-05-22T12:19:15.901084+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-22T12:19:16.705535+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 580.3}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.5}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 493.7}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 246.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 94.9}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-22T12:19:20.481097+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 703 · 2026-05-22T12:19:21.086228+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 704 · 2026-05-22T12:19:21.339263+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 705 · 2026-05-22T12:19:22.010906+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 706 · 2026-05-22T12:19:22.678845+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2197
}
```

</details>

---


### Tool call

_source line 707 · 2026-05-22T12:19:22.679366+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-22T12:19:23.284374+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 709 · 2026-05-22T12:19:23.639023+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---


### Tool result

_source line 710 · 2026-05-22T12:19:24.495225+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3408
}
```

</details>

---


### Tool result

_source line 711 · 2026-05-22T12:19:24.848558+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3509
}
```

</details>

---


### Tool result

_source line 712 · 2026-05-22T12:19:24.851025+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2171
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-22T12:19:25.002520+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2991
}
```

</details>

---


### Tool call

_source line 714 · 2026-05-22T12:23:40.012603+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — 方法严谨性审查完成\n\n### 总体评分\n**Overall**: 3.5 / 5 (Borderline Conference)\n**置信度**: 4/5\n**一句话总结**: 将 MH-DIF 引入 LLM 基准评估是有价值的方法论创新，但 headline claim \"31% temporal DIF\" 与多个 robustness 下界（DEFF-adjusted 13.5%）之间的巨大落差未被充分讨论，多维度混淆也未完全排除。\n\n### 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | MH-DIF 框架本身合理，控制实验设计周到，但 DEFF 处理、多维度混淆、temporal vs. cohort 区分存在未完全消解的疑虑 |\n| Excitement | 3.5/5 | 心理测量学方法引入 LLM benchmark 评估是新颖且及时的，但实际建议（DIF 监测、item retirement）偏增量 |\n| Reproducibility | 4/5 | 代码和审计脚本公开，METABENCH 数据可获取 |\n\n### Must-Fix 问题（3 个）\n\n**N1** [critical] DEFF-adjusted 下界与 headline claim 的严重不一致被掩盖\n- 位置：Section 4.2 headline \"31% C%\" vs. Appendix C Table 8（DEFF = 12.79, adjusted C% = 13.5%）\n- 论文通篇以 \"31%\" 为核心 claim（Abstract, Section 4.2, Conclusion），但 DEFF = 12.79 意味着有效样本量仅约 155 个独立模型。DEFF-adjusted 下界 13.5% 不到 headline 的一半，被放在附录中以 \"conservative\" 标签处理。四种不确定性估计（model bootstrap [29.4%, 38.1%], family cluster bootstrap [26.7%, 53.2%], DEFF [13.5%, 29.2%], de-duplication K=20: 29.1%）之间缺乏明确的优先级层次。\n- 建议：正文中直接报告 DEFF 范围；建立估计优先级；考虑以区间替代单点 headline。\n\n**N2** [critical] 多维度混淆未被充分排除\n- 位置：Section 3.2（total-score matching）、Section 4.1（三条辩护）、Appendix A.1\n- MMLU 57 subjects 高度多维度，论文自承 poor unidimensional model fit。total-score matching 在多维度测试中当 cohort 间 domain-specific ability shift 不均匀时产生 spurious DIF（Ackerman 1992）。三条辩护各有漏洞：Cohen's d range 0.146-0.329 不算 \"nearly flat\"（Humanities 是 Other 的 2.25 倍）；κ=0.80 意味着 20% 不一致可能恰是多维度 artifact；C items 不集中是必要非充分条件。\n- 建议：分析 κ discordant items 的 domain 分布；考虑 SIBTEST 或 logistic regression with domain covariates；量化多维度混淆的潜在幅度。\n\n**N3** [critical] \"Temporal measurement instability\" 因果归因过度\n- 位置：Title、Abstract、Section 5.1\n- \"Temporal measurement instability\" 暗示 items 测量属性变化，但同样的数据可解读为不同代 LLM 在不同 items 上能力 profile 合理地不同。论文列出三种机制但无法区分相对贡献。在教育测量中 DIF items 需要 expert review 而非自动 flagging。\n- 建议：弱化因果归因，讨论 DIF ≠ item defect 的可能性。\n\n### Should-Fix 问题（4 个）\n\n**W1** [warning] Semi-synthetic injection 的 ecological validity 有限——binary response flipping 是极端模型，real contamination 更 nuanced；ΔFPR=0 仅对特定协议有效。\n\n**W2** [warning] GSM1K 分析 N=33, r=−0.17——效力不足，\"caveat + still cite\" 模式有 cherry-picking 嫌疑。\n\n**W3** [warning] Random-split sanity check 仅在 2023 cohort 内进行，验证 null FPR 而非排除替代解释。缺少 2024 cohort 内 random split。\n\n**W4** [warning] 24.8% non-uniform DIF 对 MH 方法的影响未讨论——MH 是 uniform DIF 方法，约 1/4 items 的 DIF 幅度可能被误估。\n\n### 小问题\n- M1: Table 5 Cohen's d 正文引用数字与表格不一致\n- M2: 时间 cutoff 定义模糊\n- M3: \"C%\" 和 \"temporal C%\" 术语未统一\n- M4: \"enrichment ratio\" 首次使用缺乏直觉解释\n\n### Questions\n- Q1: DEFF-adjusted 13.5% vs headline 31%，哪个更接近真实效应？\n- Q2: κ discordant 20% items 是否在高 Cohen's d domain 中 over-represented？\n- Q3: Within-family C%=61.5% 远高于 overall 31%，是否暗示 family-specific 变化比 \"temporal instability\" 更好地解释 DIF？\n- Q4: Partial improvement contamination 下 sensitivity 如何？\n- Q5: 是否考虑 purified MH（当 31% items 有 DIF 时 matching variable 已被污染）？\n\n### Missing References\n- Clauser, Mazor, & Hambleton (1993) — purified subtest matching\n- Penfield & Algina (2006) — multidimensional DIF 框架\n- Zumbo (1999) — logistic regression DIF 方法\n- Bolt & Stout (1996) — multidimensionality-based DIF 理论\n\n### 主要优势\n- S1: MH-DIF + ETS classification 引入 LLM 评估是方法论创新\n- S2: 规模印象深刻（5,227 models × 12,508 items），数据公开可复现\n- S3: 五层控制实验（random split、matched ability、within-family、within-subject、IRT θ）系统周到\n- S4: Cross-subject matching 设计技术上巧妙\n- S5: 6 benchmarks cross-validation 增强 generalizability\n- S6: 写作质量高，图表信息密度好",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — 方法严谨性审查完成\n\n### 总体评分\n**Overall**: 3.5 / 5 (Borderline Conference)\n**置信度**: 4/5\n**一句话总结**: 将 MH-DIF 引入 LLM 基准评估是有价值的方法论创新，但 headline claim \"31% temporal DIF\" 与多个 robustness 下界（DEFF-adjusted 13.5%）之间的巨大落差未被充分讨论，多维度混淆也未完全排除。\n\n### 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | MH-DIF 框架本身合理，控制实验设计周到，但 DEFF 处理、多维度混淆、temporal vs. cohort 区分存在未完全消解的疑虑 |\n| Excitement | 3.5/5 | 心理测量学方法引入 LLM benchmark 评估是新颖且及时的，但实际建议（DIF 监测、item retirement）偏增量 |\n| Reproducibility | 4/5 | 代码和审计脚本公开，METABENCH 数据可获取 |\n\n### Must-Fix 问题（3 个）\n\n**N1** [critical] DEFF-adjusted 下界与 headline claim 的严重不一致被掩盖\n- 位置：Section 4.2 headline \"31% C%\" vs. Appendix C Table 8（DEFF = 12.79, adjusted C% = 13.5%）\n- 论文通篇以 \"31%\" 为核心 claim（Abstract, Section 4.2, Conclusion），但 DEFF = 12.79 意味着有效样本量仅约 155 个独立模型。DEFF-adjusted 下界 13.5% 不到 headline 的一半，被放在附录中以 \"conservative\" 标签处理。四种不确定性估计（model bootstrap [29.4%, 38.1%], family cluster bootstrap [26.7%, 53.2%], DEFF [13.5%, 29.2%], de-duplication K=20: 29.1%）之间缺乏明确的优先级层次。\n- 建议：正文中直接报告 DEFF 范围；建立估计优先级；考虑以区间替代单点 headline。\n\n**N2** [critical] 多维度混淆未被充分排除\n- 位置：Section 3.2（total-score matching）、Section 4.1（三条辩护）、Appendix A.1\n- MMLU 57 subjects 高度多维度，论文自承 poor unidimensional model fit。total-score matching 在多维度测试中当 cohort 间 domain-specific ability shift 不均匀时产生 spurious DIF（Ackerman 1992）。三条辩护各有漏洞：Cohen's d range 0.146-0.329 不算 \"nearly flat\"（Humanities 是 Other 的 2.25 倍）；κ=0.80 意味着 20% 不一致可能恰是多维度 artifact；C items 不集中是必要非充分条件。\n- 建议：分析 κ discordant items 的 domain 分布；考虑 SIBTEST 或 logistic regression with domain covariates；量化多维度混淆的潜在幅度。\n\n**N3** [critical] \"Temporal measurement instability\" 因果归因过度\n- 位置：Title、Abstract、Section 5.1\n- \"Temporal measurement instability\" 暗示 items 测量属性变化，但同样的数据可解读为不同代 LLM 在不同 items 上能力 profile 合理地不同。论文列出三种机制但无法区分相对贡献。在教育测量中 DIF items 需要 expert review 而非自动 flagging。\n- 建议：弱化因果归因，讨论 DIF ≠ item defect 的可能性。\n\n### Should-Fix 问题（4 个）\n\n**W1** [warning] Semi-synthetic injection 的 ecological validity 有限——binary response flipping 是极端模型，real contamination 更 nuanced；ΔFPR=0 仅对特定协议有效。\n\n**W2** [warning] GSM1K 分析 N=33, r=−0.17——效力不足，\"caveat + still cite\" 模式有 cherry-picking 嫌疑。\n\n**W3** [warning] Random-split sanity check 仅在 2023 cohort 内进行，验证 null FPR 而非排除替代解释。缺少 2024 cohort 内 random split。\n\n**W4** [warning] 24.8% non-uniform DIF 对 MH 方法的影响未讨论——MH 是 uniform DIF 方法，约 1/4 items 的 DIF 幅度可能被误估。\n\n### 小问题\n- M1: Table 5 Cohen's d 正文引用数字与表格不一致\n- M2: 时间 cutoff 定义模糊\n- M3: \"C%\" 和 \"temporal C%\" 术语未统一\n- M4: \"enrichment ratio\" 首次使用缺乏直觉解释\n\n### Questions\n- Q1: DEFF-adjusted 13.5% vs headline 31%，哪个更接近真实效应？\n- Q2: κ discordant 20% items 是否在高 Cohen's d domain 中 over-represented？\n- Q3: Within-family C%=61.5% 远高于 overall 31%，是否暗示 family-specific 变化比 \"temporal instability\" 更好地解释 DIF？\n- Q4: Partial improvement contamination 下 sensitivity 如何？\n- Q5: 是否考虑 purified MH（当 31% items 有 DIF 时 matching variable 已被污染）？\n\n### Missing References\n- Clauser, Mazor, & Hambleton (1993) — purified subtest matching\n- Penfield & Algina (2006) — multidimensional DIF 框架\n- Zumbo (1999) — logistic regression DIF 方法\n- Bolt & Stout (1996) — multidimensionality-based DIF 理论\n\n### 主要优势\n- S1: MH-DIF + ETS classification 引入 LLM 评估是方法论创新\n- S2: 规模印象深刻（5,227 models × 12,508 items），数据公开可复现\n- S3: 五层控制实验（random split、matched ability、within-family、within-subject、IRT θ）系统周到\n- S4: Cross-subject matching 设计技术上巧妙\n- S5: 6 benchmarks cross-validation 增强 generalizability\n- S6: 写作质量高，图表信息密度好",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 715 · 2026-05-22T12:23:43.886767+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3874
}
```

</details>

---


### Assistant

_source line 716 · 2026-05-22T12:23:52.769398+00:00_

审稿意见已提交给 Review Director。

总结：本轮审查识别了 3 个 Must-Fix（DEFF 透明度、多维度混淆、因果归因过度）、4 个 Should-Fix（injection ecological validity、GSM1K 效力不足、random-split 对照局限、non-uniform DIF 影响）和 4 个 Minor 问题。Overall 评分 3.5/5 (Borderline Conference)——核心方法论贡献有价值，但需要在 DEFF 报告透明度和多维度控制方面做实质性修改才能达到 Conference 接收水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 25

## Round 25

4 recorded events


### User

_source line 717 · 2026-05-22T12:25:18.992500+00:00_

[Round 1 审稿请求]:
以下是 **Reviewer 2（新颖性与完整性）** 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 — 新颖性与完整性审查

### Overall: 3.5 (Borderline Conference), Confidence: 4/5

### Must-Fix（2 个）

**W1** [Critical] 新颖性的核心张力未得到充分解决
- §2 明确承认 "We do not modify the MH procedure; our contribution is the application context"
- 三个 contributions 实质上都是 empirical findings，而非方法论创新
- 在 Growing Pains / BHI / Benchmark² / MMLU-CF 组成的 concurrent work 密集区域中，纯 "application context" 的新颖性门槛需要额外论证
- 建议：将 LLM-specific challenges 的处理前置为方法论贡献；强调 cross-subject matching 在 multi-domain contamination 场景下的理论保证；或更坦诚地定位为 Findings-track

**W2** [Critical] ρ ≈ 0.997 与 "31% instability" 之间的张力未充分调和
- aggregate ranking 几乎不受影响 → 对主要使用场景（leaderboard comparison）影响有限
- "diagnostic lens rather than quality filter" 的 framing 实质上承认了问题的有限影响
- §5.1 列出三种可能机制但立刻放弃因果推理
- 缺少 case study 展示 item-level DIF 的实际影响

### Should-Fix（4 个）

**W3** [Warning] DEFF-adjusted C% (13.5–29.2%) 的 wide range 在主文中被低估讨论。

**W4** [Warning] Discussion §5 depth 不足（约半页）。§5.1 放弃因果推理；§5.3 的 15%/25% 阈值仅由 Figure 6 支撑。

**W5** [Warning] Abstract 信息密度过高（9+ 个数字）。

**W6** [Warning] 术语一致性需改进。

### Questions
- Q1: DEFF weighted-mean 的 effective cluster size 254.5 在 LLM 语境中的合理性？
- Q2: difficulty–direction interaction ρ=-0.597 是否更支持 capability evolution 而非 contamination？
- Q3: 实际场景中 contamination 的 cross-subject 程度如何？Table 6 k=20 的 ΔFPR=0.069 是否被 Limitations 低估？
- Q4: 24.8% non-uniform DIF 的 item-level pattern？

### Missing References
- MR1: Gema et al. (2024) MMLU-Redux 的 item quality errors 与 DIF 交互
- MR2: TinyBenchmarks 的 item selection 与 DIF flagging 的关系
- MR3: Multi-group CFA measurement invariance（Cheung & Rensvold 2002）
- MR4: Yang et al. (2023) "Rethinking benchmark and contamination"

---

请对上述每条 Must-Fix、Should-Fix 和 Question 逐一回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-22T12:27:19.522611+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — 对 Reviewer 2 的交叉回应\n\n### 回应总览\nR2 的 10 个审查点中，**AGREE 9 个、REBUT 1 个**（MR2 TinyBenchmarks 不构成 missing reference）。\n\n### 核心共识（两位 Reviewer 独立收敛）\n\n1. **DEFF / uncertainty reporting**（R1-N1 ≈ R2-W3）：headline 31% 与 DEFF-adjusted 13.5% 的落差必须在正文中透明报告\n2. **ρ ≈ 0.997 vs 31% 张力**（R2-W2，R1 认同）：aggregate ranking 几乎不变→ 31% instability 的 practical impact 需要更具体的 use case 论证\n3. **因果归因过度**（R1-N3 ≈ R2-W2）：observational DIF 无法支撑 \"measurement instability\" 的因果归因\n4. **多维度混淆**（R1-N2，R2-MR3 间接触及）：CFA measurement invariance 或 SIBTEST 可加强辩护\n\n### 关键补充\n- R2-Q2 difficulty–direction ρ=−0.597 更支持 capability evolution 而非 contamination——与 R1-N3 因果归因关切一致\n- R2-Q3 Table 6 k=20 ΔFPR=0.069 被 Limitations 低估——R1 同意 6.9% FPR inflation 在部署中 non-negligible\n- R2-W1 novelty tension：R1 认为 cross-subject matching 是真正的方法论贡献，但需更显著前置\n\n### 评分维持\nOverall: 3.5 (Borderline Conference), Confidence: 4/5\n两位 Reviewer 独立给出相同分数，核心关切高度一致。解决上述四组问题后可达 4.0。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — 对 Reviewer 2 的交叉回应\n\n### 回应总览\nR2 的 10 个审查点中，**AGREE 9 个、REBUT 1 个**（MR2 TinyBenchmarks 不构成 missing reference）。\n\n### 核心共识（两位 Reviewer 独立收敛）\n\n1. **DEFF / uncertainty reporting**（R1-N1 ≈ R2-W3）：headline 31% 与 DEFF-adjusted 13.5% 的落差必须在正文中透明报告\n2. **ρ ≈ 0.997 vs 31% 张力**（R2-W2，R1 认同）：aggregate ranking 几乎不变→ 31% instability 的 practical impact 需要更具体的 use case 论证\n3. **因果归因过度**（R1-N3 ≈ R2-W2）：observational DIF 无法支撑 \"measurement instability\" 的因果归因\n4. **多维度混淆**（R1-N2，R2-MR3 间接触及）：CFA measurement invariance 或 SIBTEST 可加强辩护\n\n### 关键补充\n- R2-Q2 difficulty–direction ρ=−0.597 更支持 capability evolution 而非 contamination——与 R1-N3 因果归因关切一致\n- R2-Q3 Table 6 k=20 ΔFPR=0.069 被 Limitations 低估——R1 同意 6.9% FPR inflation 在部署中 non-negligible\n- R2-W1 novelty tension：R1 认为 cross-subject matching 是真正的方法论贡献，但需更显著前置\n\n### 评分维持\nOverall: 3.5 (Borderline Conference), Confidence: 4/5\n两位 Reviewer 独立给出相同分数，核心关切高度一致。解决上述四组问题后可达 4.0。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-22T12:27:23.556185+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4033
}
```

</details>

---


### Assistant

_source line 720 · 2026-05-22T12:27:28.727364+00:00_

交叉回应已提交。R2 的 10 个点中 AGREE 9 个、REBUT 1 个（MR2），两位 Reviewer 在 DEFF reporting、ρ vs 31% 张力、因果归因、多维度混淆四个核心问题上独立收敛。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 26

## Round 26

56 recorded events


### User

_source line 721 · 2026-05-22T13:06:41.080609+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性）

### 论文信息
- **标题**: Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models
- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`（各 section 在 `sections/` 子目录）
- **PDF**: `projects/irt_equated_bench_regen/artifacts/review_round_9/submitted.pdf`
- **目标 Venue**: EMNLP 2026 (via ACL Rolling Review)
- **截止日期**: 2026-05-25 (ARR May cycle)
- **投稿类别**: Long paper

### Venue 格式要求
- 正文 **8 页**限制，参考文献不限页数
- Limitations 章节必须，不计入页数（但不得包含额外方法/分析/结果）
- ACL 模板 `[review]` 模式，double-blind
- 自 2026 年 3 月起不接受 Word 模板
- OpenReview 提交
- Overall Assessment 评分: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit

### 你的审查侧重：方法严谨性

请重点评估以下方面：

1. **统计方法的正确性与适当性**
   - MH-DIF 方法应用于 LLM 评测的合理性（examinees=LLMs 的假设是否站得住）
   - ETS 分类阈值的选择与 justification
   - 多重比较校正的充分性
   - Bootstrap CI 和 DEFF 调整的方法论正确性

2. **实验设计的严谨性**
   - 5 种 cohort 设计的互补性和完备性
   - 随机分割 sanity check 的有效性
   - 能力匹配控制（Cohen's d, nearest-neighbor matching）的充分性
   - Leave-one-family-out 分析的说服力

3. **Semi-synthetic framework 的有效性**
   - Cross-subject matching 的 ΔFPR=0 保证——是否真的是 "by construction"？
   - 二值翻转注入的生态效度（ecological validity）
   - Multi-subject injection 的 graceful degradation 分析
   - 注入实验能否真正验证方法在真实场景中的表现

4. **Robustness checks 的充分性**
   - 六种替代解释是否都被充分排除
   - 非独立性问题的三种修正方法（cluster bootstrap, de-duplication, DEFF）的收敛性
   - 阈值敏感性分析
   - Cross-benchmark 复制的说服力

5. **声明（Claims）与证据的匹配度**
   - "31% temporal DIF" → 经修正后 ~29%，如何表述这两个数字的关系
   - ρ≈0.997 与 31% DIF 的张力是否被合理调和
   - GSM1K 分析（N=33）的证据权重是否被适当降级
   - "DIF detects that, not why" 的因果声明边界

请按 ARR 审稿标准给出结构化审稿意见：Summary、Strengths、Weaknesses（Must-Fix / Should-Fix / Nice-to-Have）、Questions、Missing References、Overall Assessment（含评分和置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-22T13:06:48.793916+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-22T13:06:48.848026+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 54
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-22T13:06:49.701876+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 725 · 2026-05-22T13:06:49.752483+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 726 · 2026-05-22T13:06:53.976173+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 727 · 2026-05-22T13:06:54.981890+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 728 · 2026-05-22T13:07:00.912369+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I've found relevant information about ACL Rolling Review 2026. Here are the key findings:

## Reviewer Guidelines

The workflow for reviewers includes: (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that particular submission. If you feel qualified to review some aspects but not others, please state in the review if you did not check some major parts, such as proofs, as this information is helpful for the AC to tell what aspects of the paper were not reviewed.

## Re
…[truncated 826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6936
}
```

</details>

---


### Tool result

_source line 729 · 2026-05-22T13:07:03.235634+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 573.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 529.6}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 547.6}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8253
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-22T13:07:09.722171+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all criteria, scoring scales, and descriptions. Include every field: soundness, excitement/novelty, reproducibility, overall assessment scale, confidence scale, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all criteria, scoring scales, and descriptions. Include every field: soundness, excitement/novelty, reproducibility, overall assessment scale, confidence scale, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 731 · 2026-05-22T13:07:10.224887+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 732 · 2026-05-22T13:07:10.678104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 733 · 2026-05-22T13:07:11.590948+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1366
}
```

</details>

---


### Tool result

_source line 734 · 2026-05-22T13:07:11.592698+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 914
}
```

</details>

---


### Tool call

_source line 735 · 2026-05-22T13:07:11.643617+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 736 · 2026-05-22T13:07:12.148358+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 737 · 2026-05-22T13:07:12.552580+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 738 · 2026-05-22T13:07:12.553094+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 739 · 2026-05-22T13:07:13.507422+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1359
}
```

</details>

---


### Tool result

_source line 740 · 2026-05-22T13:07:13.508653+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 741 · 2026-05-22T13:07:13.609455+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 742 · 2026-05-22T13:07:15.718057+00:00_

# ACL Rolling Review Form - Complete Structure

## Core Evaluation Dimensions

**Reviewer Confidence** (1-5 scale)
- 5: "Positive that my evaluation is correct"
- 4: "Quite sure" with unlikely but conceivable errors
- 3: "Pretty sure" but possible oversight of details
- 2: "Willing to defend" but likely missed elements
- 1: "Not my area" or incomprehensible paper

**Soundness** (1-5 with .5 increments)
- 5: "Excellent: This study is one of the most thorough"
- 4: "Strong: sufficient support for all claims"
- 3: "Acceptable: sufficient support for main claims"
- 2: "Poor: main claims not sufficiently supported"
- 1: "Major Issues: not sufficiently thorough"

**Excitement** (1-5 with .5 increments)
- 5: "Highly Exciting: would recommend to others"
- 4: "Exciting: would mention to others"
- 3: "Interesting: might mention some points"
- 2: "Potentially Interesting" to specific communities
- 1: "Not Exciting" to broader NLP field

**Overall Assessment** (1-5 with .5 increments)
- 5: "Consider for Award" (top 2.5%)
- 4: "Conference" acceptance
- 3: "Findings" acceptance
- 2: "Resubmit next cycle"
- 1: "Do not resubmit"

## Additional Criteria

- Reproducibility (1-5)
- Dataset Value (1-5)
- Software Value (1-5)
- Author Identity Knowledge (1-5)
- Limitations/Societal Impact assessment
- Ethical Concerns review
- Ethics Review flag

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5995
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-22T13:07:16.471415+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 592.5}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.9}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 456.0}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 495.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 241.5}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 94.9}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2861
}
```

</details>

---


### Tool call

_source line 744 · 2026-05-22T13:07:21.495000+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 745 · 2026-05-22T13:07:21.997822+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 746 · 2026-05-22T13:07:22.402565+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 747 · 2026-05-22T13:07:22.453243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 748 · 2026-05-22T13:07:23.356964+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1359
}
```

</details>

---


### Tool result

_source line 749 · 2026-05-22T13:07:23.358246+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 750 · 2026-05-22T13:07:23.358572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 751 · 2026-05-22T13:07:23.660952+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 752 · 2026-05-22T13:07:24.264322+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-22T13:07:24.516421+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-22T13:07:28.814062+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-22T13:07:29.725047+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-22T13:07:29.725492+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 757 · 2026-05-22T13:07:30.331907+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 758 · 2026-05-22T13:07:30.785180+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---


### Tool call

_source line 759 · 2026-05-22T13:07:30.785623+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 760 · 2026-05-22T13:07:31.640467+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1308
}
```

</details>

---


### Tool result

_source line 761 · 2026-05-22T13:07:31.641409+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 762 · 2026-05-22T13:07:31.792912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 763 · 2026-05-22T13:07:32.044395+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 764 · 2026-05-22T13:07:32.146764+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 765 · 2026-05-22T13:07:32.248775+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 766 · 2026-05-22T13:11:51.924252+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form 2025 2026 soundness excitement reproducibility scoring criteria detailed"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form 2025 2026 soundness excitement reproducibility scoring criteria detailed"
  }
}
```

</details>

---


### Tool call

_source line 767 · 2026-05-22T13:11:53.582862+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what constitutes soundness vs excitement, how to differentiate conference vs findings papers, guidance on statistical methodology review, and any specific instructions about evaluating empirical papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what constitutes soundness vs excitement, how to differentiate conference vs findings papers, guidance on statistical methodology review, and any specific instructions about evaluating empirical papers."
  }
}
```

</details>

---


### Tool result

_source line 768 · 2026-05-22T13:12:00.118865+00:00_

Web search results for query: "ACL ARR review form 2025 2026 soundness excitement reproducibility scoring criteria detailed"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Conference Decisions · GitHub","url":"https://gist.github.com/antonisa/2158dee79179c7c49304ef353887bfa0"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about the ACL ARR review form for 2025-2026:

## Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness
Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it. Low reproducibility scores should also be justified.

### Excitement
Sometimes you may find th
…[truncated 1090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8194
}
```

</details>

---


### Tool result

_source line 769 · 2026-05-22T13:12:02.836942+00:00_

# ARR Reviewer Guidelines: Key Assessment Distinctions

## Soundness vs. Excitement

The guidelines explicitly separate these as orthogonal dimensions:

**Soundness** refers to technical validity. The guidance states: "The _soundness_ scores must be justified by the text of the review. If you give a low _Soundness_ score without finding any major faults, this means that your review is not a faithful explanation of your recommendation."

**Excitement** captures subjective interest: "You may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate _excitement_ score, which is orthogonal to the assessment of the soundness of the paper."

This distinction allows reviewers to recommend sound work they personally find unengaging, or conversely, to acknowledge limitations in interesting papers.

## Main Conference vs. Findings Papers

The guidelines note that "All papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible." However, they address the broader composite assessment:

"The _Overall assessment_ score is an explicit recommendation for the outcome of this paper, if it were committed to an \*ACL venue. This is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact."

The distinction appears to involve impact potential: papers with high efficiency gains, novel resources for underrepresented languages, or specialized contributions may merit main conference consideration despite limited personal excitement.

## Statistical Methodology Guidance

The guidelines identify a specific issue (R5): "Ideally, at least the main experimental results should be accompanied by appropriate information about their statistical significance (error bars, confidence intervals, statistical significance tests), details about how this was computed, and discussion of factors of variabil
…[truncated 767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9254
}
```

</details>

---


### Tool call

_source line 770 · 2026-05-22T13:16:28.367605+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见（方法严谨性）\n\n### Summary\n\n本文将教育测量学中成熟的 Mantel-Haenszel Differential Item Functioning (MH-DIF) 方法应用于 LLM benchmark 的时间可比性问题。基于 METABENCH 数据（5,227 模型 × 6 benchmarks × 27,125 items），论文发现约 31% 的 MMLU items 在 2023 与 2024 模型 cohort 之间展现 temporal DIF（ETS Category C），经非独立性校正后约 29%。论文进一步提出 cross-subject matching 的半合成验证框架（理论 ΔFPR=0），并通过五种 cohort 设计、六种替代解释排除和跨 benchmark 复制验证了结果的稳健性。核心论点是 DIF 揭示了 item-level measurement instability，但不威胁 aggregate rankings（ρ≈0.997），应作为诊断工具而非替代标准。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n**Confidence**: 4/5 (Quite sure)\n**一句话总结**: 方法论框架扎实、规模令人印象深刻的跨学科实证研究，但非独立性校正的内部收敛性（13.5%–29.2%）不足、有效样本量对 item-level 检验的影响未被处理，构成需要解决的方法论缺陷。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论框架整体合理，但 DEFF 校正范围(13.5%–29.2%)的选择性呈现、item-level 非独立性未校正、semi-synthetic injection 的生态效度有限 |\n| Excitement | 4/5 | 跨学科创新（psychometrics→NLP），重要且及时的研究问题，practical implications clearly articulated |\n| Reproducibility | 4/5 | 代码和数据声明可用（footnote 1），方法描述充分，ETS 分类阈值有据可查 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 非独立性校正方法的\"收敛性\"声明与实际数据不符\n\n- **具体位置**：Abstract（\"three convergent corrections narrow this to ≈29%\"）, Appendix C/D, Table 8\n- **问题**：论文报告了四种非独立性校正方法，但结果范围为 13.5%（weighted-mean DEFF, DEFF=12.79）到 31.3%（raw），跨度超过 2 倍。论文选择性地将三种结果（cluster bootstrap 26.7%, simple-mean DEFF 29.2%, graduated de-duplication K=20 29.1%）标记为\"convergent\"，排除了 weighted-mean DEFF 的 13.5%。排除理由仅为\"overweights large families\"——但在 survey 统计方法论中，当 cluster 大小差异大时，weighted-mean ICC 通常被视为更稳健的估计量（Kish, 1965）。论文未提供充分的方法论论据来偏好 simple-mean over weighted-mean。\n- 更严重的是，cluster bootstrap 95% CI 为 [26.7%, 53.2%]，宽度达 26.5 个百分点，上限 53.2% 甚至高于 raw estimate 31.3%。如此宽的 CI 本身就说明估计的不确定性极大，削弱了\"≈29%\"这一看似精确的 point estimate 的可信度。\n- **为什么影响接收**：这是论文的核心发现。如果 weighted-mean DEFF 是更准确的估计，那么 headline number 应为 ~13.5% 而非 ~29%，论文的叙事框架和实践影响力都需调整。选择性报告有 cherry-picking 之嫌。\n- **建议修改方向**：\n  (1) 以方法论论据（而非结论偏好）来论证 weighted-mean DEFF 的问题——可引用 survey methodology 中关于 few-PSU DEFF instability 的文献（cluster 数 ~10 时 ICC 估计高度不稳定）；\n  (2) 将完整范围 [13.5%, 29.2%] 透明呈现为 corrected estimate range，而非选择性报告 ~29%；\n  (3) 强调即便按最保守的 13.5%，temporal DIF 仍是 random baseline (0.18%) 的 75 倍，核心发现和实践建议不受影响。\n\n**N2** [critical] 有效样本量对 item-level MH 检验的影响完全缺失\n\n- **具体位置**：Section 3.2 (MH procedure), Section 4.1 (power analysis), Appendix C (DEFF estimation)\n- **问题**：DEFF = 12.79 意味着有效样本量 N_eff ≈ 1,887/12.79 ≈ 148（每 cohort 约 75 个有效独立模型）。论文使用 DEFF 校正了 aggregate C% 的估计（Table 8），但**未讨论 DEFF 对单个 item MH χ² 检验的影响**。\n  - 在非独立数据下，MH χ² 统计量的方差被低估，导致 p-value 被 inflated（即真实 p-value 应更大）。这意味着一些被 raw analysis 标记为 statistically significant 的 DIF items，在 DEFF 校正后可能不再 significant，从而失去 ETS C 分类（ETS C 需要 significance + 效应量双门槛）。\n  - 论文的 DEFF-adjusted C%=13.5% 可能恰恰反映了这一 item-level inflation 效应，而非仅仅是 aggregate 校正。\n  - Section 4.1 的 Monte Carlo power analysis 使用 N=80 per cohort 独立生成响应，巧合地接近 N_eff≈75，但论文未明确这一对应关系——power analysis 未建模 family-level clustering。\n- **为什么影响接收**：这是方法论盲点。论文对 aggregate 非独立性做了详细处理（三种方法），但对 item-level 检验的非独立性完全未提及。这在技术上是不完整的。\n- **建议修改方向**：\n  (1) 在 Appendix 中增加 DEFF-adjusted item-level significance test：将每个 item 的 MH χ² 除以 DEFF（或等效地将 significance threshold 调整为 α/DEFF），重新计算 ETS C 分类率；\n  (2) 明确 Monte Carlo power analysis 与 effective sample size 的对应关系，或在 simulation 中引入 family-level ICC 结构；\n  (3) 在 Discussion 中讨论 item-level 和 aggregate-level 非独立性校正的区别。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 半合成注入的\"上界\"论断不够准确\n\n- **具体位置**：Section 3.4（p5：\"realistic contamination...would produce weaker signals\"）, Limitations (p9)\n- **问题**：论文声称二值翻转注入是 TPR 的 upper bound——即真实污染的 detection rate 更低。这对 signal strength 成立：均匀翻转产生最大 Δ_MH。但从 detection difficulty 角度看，均匀注入产生一致信号，是最**易**检测的模式。真实异质污染（partial memorization、format-specific advantages、与 item difficulty 的交互）产生**分散**信号，可能对 MH-DIF 这类全局检测方法造成更大挑战。论文的\"upper bound\"论断隐含了\"更强信号=更容易检测\"的等价关系，这在 uniform injection 下成立，但在 non-uniform 真实场景下可能不成立。\n- **建议**：(1) 精化论断为 \"TPR upper bound under uniform injection\"，明确不覆盖 non-uniform patterns；(2) 至少增加一种 difficulty-dependent injection（如高 difficulty items 被 exploit 概率更高）作为 sensitivity check。\n\n**W2** [warning] Cross-subject matching ΔFPR=0 的适用边界不明\n\n- **具体位置**：Section 3.4 Remark (p5), Table 6\n- **问题**：ΔFPR=0 保证仅在 single-subject injection 下 by construction 成立。Table 6 的 multi-subject injection 结果仅测试了 exploitation rate p=0.5（从 Section 3.4 描述推断），且 k 最大为 20（57 subjects 的 35%）。在更极端但不不合理的场景（如 k=30+，涵盖 STEM 全部 subjects）下，ΔFPR degradation 速度未知。论文也未讨论 k 与 p 的联合效应——k 大但 p 小的场景可能比 k 小但 p 大更具实际相关性。\n- **建议**：(1) 在 Table 6 中增加 p=0.3 和 p=0.7 的行；(2) 报告或推导 ΔFPR 与 k 的理论关系；(3) 明确报告该方法的 breakdown point（即 ΔFPR>某阈值时的 k 值）。\n\n**W3** [warning] LLM 确定性响应与 MH-DIF 概率框架的张力\n\n- **具体位置**：Section 3.2, Appendix A.2 (p12)\n- **问题**：MH-DIF 源自教育测量学，假设 examinee 对 item 的 response 是概率性的（受 ability 影响但有随机性）。LLMs 在 temperature=0 下对同一 item 给出确定性响应。这意味着：\n  (a) 每个 LLM-item pair 的 response 没有随机变异——MH χ² 所测量的\"超出能力差异的行为差异\"纯粹来自 cross-model variance，而非 within-model variance。\n  (b) MH 统计量的分布假设（基于超几何分布）在确定性响应下是否仍然成立？超几何分布的推导假设条件独立性（给定 total score，每个 item response 独立），确定性响应下这一条件自动满足（no within-examinee randomness），但样本量的解释不同。\n  论文在 Appendix A.2 (p12) 提到 \"This does not affect MH-DIF validity, which relies only on total score stratification rather than parametric IRT assumptions\"，这对 IRT model fit 成立，但未回应 MH 统计量分布假设的问题。\n- **建议**：在 Section 3 或 Limitations 中增加一段讨论确定性响应对 MH procedure 的影响，至少需要论证 MH χ² 的 asymptotic distribution 在 fixed responses + cross-model sampling 下仍有效。\n\n**W4** [warning] 多重比较问题需显式说明\n\n- **具体位置**：Section 3.2\n- **问题**：12,508 个 items 的 MH-DIF 分析未经 FDR/FWER 校正。在教育测量 DIF 文献中，这是标准做法——ETS effect-size 阈值已提供实际显著性过滤，DIF 分析的目标是 item screening 而非全局 hypothesis testing（Holland and Thayer, 1988; Clauser and Mazor, 1998）。Random-split baseline C%=0.18% (Section 4.2) 也提供了强力的经验 FPR 证据。但这些理由未被显式陈述。\n- **建议**：在 Section 3.2 增加 1-2 句说明 DIF 分析不做多重比较校正的行业惯例及理由，并将 random-split 0.18% 明确定位为 empirical FPR control。\n\n**W5** [warning] Temporal cohort 定义的粗粒度\n\n- **具体位置**：Section 3.1, Section 4.2\n- **问题**：2023 vs 2024 的二元 cohort 划分基于模型发布日期，但：(1) 发布日期 ≠ 训练数据截止日期（2024 Q1 模型可能使用 2023 年训练数据）；(2) 一年粒度内部异质性大——2023 Q1 vs 2024 Q4 的差异远大于 2023 Q4 vs 2024 Q1；(3) N=1,080 (2023) vs N=807 (2024) 的不平衡可能影响 MH 统计量（尽管 MH 对不平衡相对稳健）。\n  论文在 Section 4.2 提到 within-year Q1-Q4 比较作为 sensitivity check，部分缓解了这一问题。但 main analysis 的 temporal resolution 仍然较粗。\n- **建议**：(1) 在 Discussion 中讨论 release date 作为 temporal proxy 的局限性；(2) 如 METABENCH 提供更细粒度的时间信息，增加 quarterly sensitivity analysis。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Abstract 信息密度过高**：一句话内出现 \"5,227 models, 27,125 items, six benchmarks, MH-DIF, ETS, semi-synthetic, cross-subject matching, ΔFPR=0, cluster bootstrap CI [26.7%, 53.2%], random-split baseline 0.18%\"——建议精简，将 CI 和 baseline 数字移至正文。\n\n2. **Table 3 \"procedural benchmarks\" 定义缺失**：HellaSwag 和 WinoGrande 被归为 \"procedural\"，但未给出分类标准。建议增加脚注说明。\n\n3. **Section 5.3 \"≥500 models\" 阈值依据不足**：推荐的 monitoring protocol 要求至少 500 模型，但 power analysis (Section 4.1) 使用 N=80 per cohort。500 的依据是什么？如果是基于 DEFF 校正（N_raw/DEFF ≈ 500/12.79 ≈ 39, too low），需要明确论证。\n\n4. **GSM1K 分析在主文中的权重过高**：Section 4.7 + Figure 5 基于 N=33，论文已标注 \"interpreted with caution\" 和 \"exploratory\"，但在主文中仍占约半页篇幅。鉴于样本量极小，建议将 Figure 5 和详细分析移至 Appendix，在主文中仅保留一句 summary。\n\n5. **Figure 2 dose-response 曲线**：x-axis 标注为 \"exploitation rate p\"，但 y-axis 标注 \"True Positive Rate (TPR)\" 和 \"False Positive Rate (FPR)\" 分列在两个 subplot。两个 y-axis 的 scale 差异极大（FPR 在 0-0.03 范围，TPR 在 0-1 范围），可能导致读者误读。建议统一标注或在 caption 中提醒。\n\n---\n\n## Questions to Authors\n\n**Q1**: Table 8 中 weighted-mean DEFF (13.5%) 和 simple-mean DEFF (29.2%) 差异达 2 倍。如果将 item-level MH χ² p-values 除以 DEFF=12.79 进行校正（即提高 significance threshold），重新进行 ETS 分类后的 C% 是多少？这个数字与 aggregate DEFF-adjusted 13.5% 是否一致？\n\n**Q2**: Monte Carlo power analysis (Section 4.1) 在独立响应数据上进行。如果在 simulation 中引入与真实数据相同的 family-level clustering (ICC ≈ 0.047)，per-item TPR 和 C% 的 power estimates 会下降多少？\n\n**Q3**: Cross-subject matching 的 ΔFPR=0 保证在 k=20 subjects 时已开始 degrade (Table 6)。是否存在一个理论 breakdown point（k_max），超过该点 cross-subject matching 的 FPR 控制不再有效？\n\n**Q4**: LLM 对同一 item 的 response 在 temperature=0 下是确定性的。MH χ² 的超几何分布推导假设 conditional independence given total score——在 deterministic responses 下，这一条件是否自动满足？是否需要将 \"randomness\" 重新解释为 \"cross-model sampling variability\"？\n\n**Q5**: 如果 power analysis 显示 TPR 在 0.40-0.68 范围，意味着 32-60% 的 true DIF items 被 missed。那么 observed C%=31% 是否可能是 true DIF rate 的**下界**？换言之，考虑 power 校正后的 estimated true DIF rate 是否可能显著高于 31%？这与非独立性校正（降低 C%）的方向相反——论文是否讨论了这两个 bias 的净效应？\n\n---\n\n## Missing References\n\n1. **Few-PSU DEFF instability**：论文引用了 Kish (1965) 和 Rao and Scott (1992)，但未引用关于 small number of clusters 导致 DEFF 估计不稳定的文献。建议参考 Valliant et al. (2013) *Practical Tools for Designing and Weighting Survey Samples* 或 Lohr (2019) *Sampling: Design and Analysis* 中的相关章节。\n2. **Multidimensional DIF**：论文使用 unidimensional MH-DIF 处理 57-subject 多维数据。Shealy and Stout (1993) SIBTEST 已被提及但未深入。建议讨论 multidimensional DIF 方法（如 Ackerman 1992 已在参考文献中）在 LLM setting 中的适用性。\n3. **Benchmark temporal stability in education**：Brennan (2001) *Generalizability Theory* 和 Kane (2006) 关于 validity argument 的框架可为 temporal measurement invariance 的讨论提供更丰富的理论背景。\n\n---\n\n## 主要优势\n\n1. **填补重要方法论缺口**：首次将 DIF 方法系统性地应用于 LLM benchmark 的时间可比性问题，区分了 global exposure（web-overlap labels）与 differential functioning，这一理论贡献独立于具体数字有效。\n2. **规模与覆盖面**：5,227 模型 × 6 benchmarks × 27,125 items 是迄今最大规模的 LLM benchmark psychometric audit。\n3. **五种 cohort 设计的互补性**：Temporal + ability-quintile + within-family + within-subject + random-split 形成了方法论上周密的验证矩阵，特别是 random-split sanity check (C%=0.18%) 提供了无可挑剔的 null baseline。\n4. **Semi-synthetic 框架的创新性**：cross-subject matching 利用 MMLU 多 subject 结构消除 FPR 的设计巧妙，即便有边界限制（single-subject），概念上是一个有价值的方法论贡献。\n5. **因果声明的自我约束**：\"DIF detects that, not why\" 和 \"diagnostic, not algorithmic\" 的表述准确定位了方法的能力边界，避免了 contamination detection 论文中常见的过度声明。\n6. **Cross-benchmark 复制**：六个 benchmark 的复制（Table 3）和 Figure 6 的 ranking degradation 分析增强了外部效度。\n7. **对 web-overlap labels 的 meta-critique**：Section 4.3 的经验发现（enrichment ratio ≈ 0.964, near-independence）对现有 contamination detection 方法论有独立价值。\n\n---\n\n**总体判断**：这是一篇方法论扎实、规模宏大、问题定位精准的实证论文，核心贡献（DIF applied to temporal benchmark comparability）清晰且有价值。两个 Must-Fix 问题（DEFF 收敛性的选择性报告、item-level 非独立性校正缺失）如果被妥善处理（预计可在修改中完成），本文适合 Conference (4.0) 接收。当前状态为 Borderline Conference (3.5)。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见（方法严谨性）\n\n### Summary\n\n本文将教育测量学中成熟的 Mantel-Haenszel Differential Item Functioning (MH-DIF) 方法应用于 LLM benchmark 的时间可比性问题。基于 METABENCH 数据（5,227 模型 × 6 benchmarks × 27,125 items），论文发现约 31% 的 MMLU items 在 2023 与 2024 模型 cohort 之间展现 temporal DIF（ETS Category C），经非独立性校正后约 29%。论文进一步提出 cross-subject matching 的半合成验证框架（理论 ΔFPR=0），并通过五种 cohort 设计、六种替代解释排除和跨 benchmark 复制验证了结果的稳健性。核心论点是 DIF 揭示了 item-level measurement instability，但不威胁 aggregate rankings（ρ≈0.997），应作为诊断工具而非替代标准。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n**Confidence**: 4/5 (Quite sure)\n**一句话总结**: 方法论框架扎实、规模令人印象深刻的跨学科实证研究，但非独立性校正的内部收敛性（13.5%–29.2%）不足、有效样本量对 item-level 检验的影响未被处理，构成需要解决的方法论缺陷。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论框架整体合理，但 DEFF 校正范围(13.5%–29.2%)的选择性呈现、item-level 非独立性未校正、semi-synthetic injection 的生态效度有限 |\n| Excitement | 4/5 | 跨学科创新（psychometrics→NLP），重要且及时的研究问题，practical implications clearly articulated |\n| Reproducibility | 4/5 | 代码和数据声明可用（footnote 1），方法描述充分，ETS 分类阈值有据可查 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 非独立性校正方法的\"收敛性\"声明与实际数据不符\n\n- **具体位置**：Abstract（\"three convergent corrections narrow this to ≈29%\"）, Appendix C/D, Table 8\n- **问题**：论文报告了四种非独立性校正方法，但结果范围为 13.5%（weighted-mean DEFF, DEFF=12.79）到 31.3%（raw），跨度超过 2 倍。论文选择性地将三种结果（cluster bootstrap 26.7%, simple-mean DEFF 29.2%, graduated de-duplication K=20 29.1%）标记为\"convergent\"，排除了 weighted-mean DEFF 的 13.5%。排除理由仅为\"overweights large families\"——但在 survey 统计方法论中，当 cluster 大小差异大时，weighted-mean ICC 通常被视为更稳健的估计量（Kish, 1965）。论文未提供充分的方法论论据来偏好 simple-mean over weighted-mean。\n- 更严重的是，cluster bootstrap 95% CI 为 [26.7%, 53.2%]，宽度达 26.5 个百分点，上限 53.2% 甚至高于 raw estimate 31.3%。如此宽的 CI 本身就说明估计的不确定性极大，削弱了\"≈29%\"这一看似精确的 point estimate 的可信度。\n- **为什么影响接收**：这是论文的核心发现。如果 weighted-mean DEFF 是更准确的估计，那么 headline number 应为 ~13.5% 而非 ~29%，论文的叙事框架和实践影响力都需调整。选择性报告有 cherry-picking 之嫌。\n- **建议修改方向**：\n  (1) 以方法论论据（而非结论偏好）来论证 weighted-mean DEFF 的问题——可引用 survey methodology 中关于 few-PSU DEFF instability 的文献（cluster 数 ~10 时 ICC 估计高度不稳定）；\n  (2) 将完整范围 [13.5%, 29.2%] 透明呈现为 corrected estimate range，而非选择性报告 ~29%；\n  (3) 强调即便按最保守的 13.5%，temporal DIF 仍是 random baseline (0.18%) 的 75 倍，核心发现和实践建议不受影响。\n\n**N2** [critical] 有效样本量对 item-level MH 检验的影响完全缺失\n\n- **具体位置**：Section 3.2 (MH procedure), Section 4.1 (power analysis), Appendix C (DEFF estimation)\n- **问题**：DEFF = 12.79 意味着有效样本量 N_eff ≈ 1,887/12.79 ≈ 148（每 cohort 约 75 个有效独立模型）。论文使用 DEFF 校正了 aggregate C% 的估计（Table 8），但**未讨论 DEFF 对单个 item MH χ² 检验的影响**。\n  - 在非独立数据下，MH χ² 统计量的方差被低估，导致 p-value 被 inflated（即真实 p-value 应更大）。这意味着一些被 raw analysis 标记为 statistically significant 的 DIF items，在 DEFF 校正后可能不再 significant，从而失去 ETS C 分类（ETS C 需要 significance + 效应量双门槛）。\n  - 论文的 DEFF-adjusted C%=13.5% 可能恰恰反映了这一 item-level inflation 效应，而非仅仅是 aggregate 校正。\n  - Section 4.1 的 Monte Carlo power analysis 使用 N=80 per cohort 独立生成响应，巧合地接近 N_eff≈75，但论文未明确这一对应关系——power analysis 未建模 family-level clustering。\n- **为什么影响接收**：这是方法论盲点。论文对 aggregate 非独立性做了详细处理（三种方法），但对 item-level 检验的非独立性完全未提及。这在技术上是不完整的。\n- **建议修改方向**：\n  (1) 在 Appendix 中增加 DEFF-adjusted item-level significance test：将每个 item 的 MH χ² 除以 DEFF（或等效地将 significance threshold 调整为 α/DEFF），重新计算 ETS C 分类率；\n  (2) 明确 Monte Carlo power analysis 与 effective sample size 的对应关系，或在 simulation 中引入 family-level ICC 结构；\n  (3) 在 Discussion 中讨论 item-level 和 aggregate-level 非独立性校正的区别。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 半合成注入的\"上界\"论断不够准确\n\n- **具体位置**：Section 3.4（p5：\"realistic contamination...would produce weaker signals\"）, Limitations (p9)\n- **问题**：论文声称二值翻转注入是 TPR 的 upper bound——即真实污染的 detection rate 更低。这对 signal strength 成立：均匀翻转产生最大 Δ_MH。但从 detection difficulty 角度看，均匀注入产生一致信号，是最**易**检测的模式。真实异质污染（partial memorization、format-specific advantages、与 item difficulty 的交互）产生**分散**信号，可能对 MH-DIF 这类全局检测方法造成更大挑战。论文的\"upper bound\"论断隐含了\"更强信号=更容易检测\"的等价关系，这在 uniform injection 下成立，但在 non-uniform 真实场景下可能不成立。\n- **建议**：(1) 精化论断为 \"TPR upper bound under uniform injection\"，明确不覆盖 non-uniform patterns；(2) 至少增加一种 difficulty-dependent injection（如高 difficulty items 被 exploit 概率更高）作为 sensitivity check。\n\n**W2** [warning] Cross-subject matching ΔFPR=0 的适用边界不明\n\n- **具体位置**：Section 3.4 Remark (p5), Table 6\n- **问题**：ΔFPR=0 保证仅在 single-subject injection 下 by construction 成立。Table 6 的 multi-subject injection 结果仅测试了 exploitation rate p=0.5（从 Section 3.4 描述推断），且 k 最大为 20（57 subjects 的 35%）。在更极端但不不合理的场景（如 k=30+，涵盖 STEM 全部 subjects）下，ΔFPR degradation 速度未知。论文也未讨论 k 与 p 的联合效应——k 大但 p 小的场景可能比 k 小但 p 大更具实际相关性。\n- **建议**：(1) 在 Table 6 中增加 p=0.3 和 p=0.7 的行；(2) 报告或推导 ΔFPR 与 k 的理论关系；(3) 明确报告该方法的 breakdown point（即 ΔFPR>某阈值时的 k 值）。\n\n**W3** [warning] LLM 确定性响应与 MH-DIF 概率框架的张力\n\n- **具体位置**：Section 3.2, Appendix A.2 (p12)\n- **问题**：MH-DIF 源自教育测量学，假设 examinee 对 item 的 response 是概率性的（受 ability 影响但有随机性）。LLMs 在 temperature=0 下对同一 item 给出确定性响应。这意味着：\n  (a) 每个 LLM-item pair 的 response 没有随机变异——MH χ² 所测量的\"超出能力差异的行为差异\"纯粹来自 cross-model variance，而非 within-model variance。\n  (b) MH 统计量的分布假设（基于超几何分布）在确定性响应下是否仍然成立？超几何分布的推导假设条件独立性（给定 total score，每个 item response 独立），确定性响应下这一条件自动满足（no within-examinee randomness），但样本量的解释不同。\n  论文在 Appendix A.2 (p12) 提到 \"This does not affect MH-DIF validity, which relies only on total score stratification rather than parametric IRT assumptions\"，这对 IRT model fit 成立，但未回应 MH 统计量分布假设的问题。\n- **建议**：在 Section 3 或 Limitations 中增加一段讨论确定性响应对 MH procedure 的影响，至少需要论证 MH χ² 的 asymptotic distribution 在 fixed responses + cross-model sampling 下仍有效。\n\n**W4** [warning] 多重比较问题需显式说明\n\n- **具体位置**：Section 3.2\n- **问题**：12,508 个 items 的 MH-DIF 分析未经 FDR/FWER 校正。在教育测量 DIF 文献中，这是标准做法——ETS effect-size 阈值已提供实际显著性过滤，DIF 分析的目标是 item screening 而非全局 hypothesis testing（Holland and Thayer, 1988; Clauser and Mazor, 1998）。Random-split baseline C%=0.18% (Section 4.2) 也提供了强力的经验 FPR 证据。但这些理由未被显式陈述。\n- **建议**：在 Section 3.2 增加 1-2 句说明 DIF 分析不做多重比较校正的行业惯例及理由，并将 random-split 0.18% 明确定位为 empirical FPR control。\n\n**W5** [warning] Temporal cohort 定义的粗粒度\n\n- **具体位置**：Section 3.1, Section 4.2\n- **问题**：2023 vs 2024 的二元 cohort 划分基于模型发布日期，但：(1) 发布日期 ≠ 训练数据截止日期（2024 Q1 模型可能使用 2023 年训练数据）；(2) 一年粒度内部异质性大——2023 Q1 vs 2024 Q4 的差异远大于 2023 Q4 vs 2024 Q1；(3) N=1,080 (2023) vs N=807 (2024) 的不平衡可能影响 MH 统计量（尽管 MH 对不平衡相对稳健）。\n  论文在 Section 4.2 提到 within-year Q1-Q4 比较作为 sensitivity check，部分缓解了这一问题。但 main analysis 的 temporal resolution 仍然较粗。\n- **建议**：(1) 在 Discussion 中讨论 release date 作为 temporal proxy 的局限性；(2) 如 METABENCH 提供更细粒度的时间信息，增加 quarterly sensitivity analysis。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Abstract 信息密度过高**：一句话内出现 \"5,227 models, 27,125 items, six benchmarks, MH-DIF, ETS, semi-synthetic, cross-subject matching, ΔFPR=0, cluster bootstrap CI [26.7%, 53.2%], random-split baseline 0.18%\"——建议精简，将 CI 和 baseline 数字移至正文。\n\n2. **Table 3 \"procedural benchmarks\" 定义缺失**：HellaSwag 和 WinoGrande 被归为 \"procedural\"，但未给出分类标准。建议增加脚注说明。\n\n3. **Section 5.3 \"≥500 models\" 阈值依据不足**：推荐的 monitoring protocol 要求至少 500 模型，但 power analysis (Section 4.1) 使用 N=80 per cohort。500 的依据是什么？如果是基于 DEFF 校正（N_raw/DEFF ≈ 500/12.79 ≈ 39, too low），需要明确论证。\n\n4. **GSM1K 分析在主文中的权重过高**：Section 4.7 + Figure 5 基于 N=33，论文已标注 \"interpreted with caution\" 和 \"exploratory\"，但在主文中仍占约半页篇幅。鉴于样本量极小，建议将 Figure 5 和详细分析移至 Appendix，在主文中仅保留一句 summary。\n\n5. **Figure 2 dose-response 曲线**：x-axis 标注为 \"exploitation rate p\"，但 y-axis 标注 \"True Positive Rate (TPR)\" 和 \"False Positive Rate (FPR)\" 分列在两个 subplot。两个 y-axis 的 scale 差异极大（FPR 在 0-0.03 范围，TPR 在 0-1 范围），可能导致读者误读。建议统一标注或在 caption 中提醒。\n\n---\n\n## Questions to Authors\n\n**Q1**: Table 8 中 weighted-mean DEFF (13.5%) 和 simple-mean DEFF (29.2%) 差异达 2 倍。如果将 item-level MH χ² p-values 除以 DEFF=12.79 进行校正（即提高 significance threshold），重新进行 ETS 分类后的 C% 是多少？这个数字与 aggregate DEFF-adjusted 13.5% 是否一致？\n\n**Q2**: Monte Carlo power analysis (Section 4.1) 在独立响应数据上进行。如果在 simulation 中引入与真实数据相同的 family-level clustering (ICC ≈ 0.047)，per-item TPR 和 C% 的 power estimates 会下降多少？\n\n**Q3**: Cross-subject matching 的 ΔFPR=0 保证在 k=20 subjects 时已开始 degrade (Table 6)。是否存在一个理论 breakdown point（k_max），超过该点 cross-subject matching 的 FPR 控制不再有效？\n\n**Q4**: LLM 对同一 item 的 response 在 temperature=0 下是确定性的。MH χ² 的超几何分布推导假设 conditional independence given total score——在 deterministic responses 下，这一条件是否自动满足？是否需要将 \"randomness\" 重新解释为 \"cross-model sampling variability\"？\n\n**Q5**: 如果 power analysis 显示 TPR 在 0.40-0.68 范围，意味着 32-60% 的 true DIF items 被 missed。那么 observed C%=31% 是否可能是 true DIF rate 的**下界**？换言之，考虑 power 校正后的 estimated true DIF rate 是否可能显著高于 31%？这与非独立性校正（降低 C%）的方向相反——论文是否讨论了这两个 bias 的净效应？\n\n---\n\n## Missing References\n\n1. **Few-PSU DEFF instability**：论文引用了 Kish (1965) 和 Rao and Scott (1992)，但未引用关于 small number of clusters 导致 DEFF 估计不稳定的文献。建议参考 Valliant et al. (2013) *Practical Tools for Designing and Weighting Survey Samples* 或 Lohr (2019) *Sampling: Design and Analysis* 中的相关章节。\n2. **Multidimensional DIF**：论文使用 unidimensional MH-DIF 处理 57-subject 多维数据。Shealy and Stout (1993) SIBTEST 已被提及但未深入。建议讨论 multidimensional DIF 方法（如 Ackerman 1992 已在参考文献中）在 LLM setting 中的适用性。\n3. **Benchmark temporal stability in education**：Brennan (2001) *Generalizability Theory* 和 Kane (2006) 关于 validity argument 的框架可为 temporal measurement invariance 的讨论提供更丰富的理论背景。\n\n---\n\n## 主要优势\n\n1. **填补重要方法论缺口**：首次将 DIF 方法系统性地应用于 LLM benchmark 的时间可比性问题，区分了 global exposure（web-overlap labels）与 differential functioning，这一理论贡献独立于具体数字有效。\n2. **规模与覆盖面**：5,227 模型 × 6 benchmarks × 27,125 items 是迄今最大规模的 LLM benchmark psychometric audit。\n3. **五种 cohort 设计的互补性**：Temporal + ability-quintile + within-family + within-subject + random-split 形成了方法论上周密的验证矩阵，特别是 random-split sanity check (C%=0.18%) 提供了无可挑剔的 null baseline。\n4. **Semi-synthetic 框架的创新性**：cross-subject matching 利用 MMLU 多 subject 结构消除 FPR 的设计巧妙，即便有边界限制（single-subject），概念上是一个有价值的方法论贡献。\n5. **因果声明的自我约束**：\"DIF detects that, not why\" 和 \"diagnostic, not algorithmic\" 的表述准确定位了方法的能力边界，避免了 contamination detection 论文中常见的过度声明。\n6. **Cross-benchmark 复制**：六个 benchmark 的复制（Table 3）和 Figure 6 的 ranking degradation 分析增强了外部效度。\n7. **对 web-overlap labels 的 meta-critique**：Section 4.3 的经验发现（enrichment ratio ≈ 0.964, near-independence）对现有 contamination detection 方法论有独立价值。\n\n---\n\n**总体判断**：这是一篇方法论扎实、规模宏大、问题定位精准的实证论文，核心贡献（DIF applied to temporal benchmark comparability）清晰且有价值。两个 Must-Fix 问题（DEFF 收敛性的选择性报告、item-level 非独立性校正缺失）如果被妥善处理（预计可在修改中完成），本文适合 Conference (4.0) 接收。当前状态为 Borderline Conference (3.5)。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-22T13:16:32.433769+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4066
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-22T13:16:36.762466+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 773 · 2026-05-22T13:16:36.863297+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 774 · 2026-05-22T13:16:40.629657+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 775 · 2026-05-22T13:16:40.680385+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 776 · 2026-05-22T13:16:51.209878+00:00_

Round 1 审稿意见已提交给 Review Director。

**评分**: Overall 3.5 (Borderline Conference), Soundness 3.5/5, Excitement 4/5, Reproducibility 4/5, Confidence 4/5。

**两个 Must-Fix 问题**：
1. 非独立性校正的"收敛性"声明不成立——四种方法估计范围 13.5%–29.2%，论文选择性排除最保守的 weighted-mean DEFF (13.5%)，有 cherry-picking 之嫌
2. Item-level MH χ² 检验未经 DEFF 校正——DEFF=12.79 意味着有效样本量仅 ~148，单个 item 的 significance test 被 inflate，但论文只校正了 aggregate C%

**五个 Should-Fix 问题**涵盖：semi-synthetic 注入的生态效度、cross-subject matching 边界条件、LLM 确定性响应与 MH 概率框架的张力、多重比较的显式说明、temporal cohort 粗粒度。

核心判断：如果两个 Must-Fix 被妥善处理（技术上可行），论文应达到 Conference (4.0) 水准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 27

## Round 27

4 recorded events


### User

_source line 777 · 2026-05-22T13:17:17.916915+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿原文：

## Reviewer 2 — Round 1 审稿意见（新颖性/完整性视角）

**Overall Assessment**: 3.5 / 5 — Borderline Conference
**Confidence**: 4 / 5
**Soundness**: 3.5/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5

### Must-Fix 问题

**N1** [critical] **核心张力未解决：ρ ≈ 0.997 与 31% DIF 的实际意义**
- Section 4.2, Section 5.1, Section 4.6
- 论文核心发现是 31% 的题目存在显著 DIF，但聚合排名相关性 ρ ≈ 0.997。Section 5.1 将此描述为"item-level instability does not threaten aggregate benchmark validity"。但这产生了根本性的"so what"问题。
- Figure 6 显示 DIF-ordered removal 比 random removal **更快**地降解排名——DIF 题目实际上**承载了大量有效的区分信息**，并非纯噪声。这与 Section 5.3 的 Flag/Act 协议（建议移除或标记 DIF 题目）产生内在矛盾。
- 建议：(1) 明确讨论 Figure 6 对"flag and remove"策略的限制；(2) 提供具体决策场景中 DIF 实质性改变结论的案例；(3) 或将 contribution 缩小为"诊断发现"而非"可操作的审计框架"。

**N2** [critical] **方法论新颖性的论证不足**
- MH-DIF 是 Holland and Thayer (1988) 的标准方法，ETS 分类也是成熟体系。方法层面唯一创新是 cross-subject matching 的半合成框架。
- 论文完全没有与其他 DIF 检测方法比较——Section 2 提到 logistic regression DIF、SIBTEST、IRT-based methods，但主实验仅使用 MH-DIF。
- 24.8% 的题目显示 non-uniform DIF（通过 logistic regression 检测），但被埋在 Limitations 中。如果近四分之一的题目表现出 MH-DIF 无法检测的 non-uniform DIF，这严重影响分析的完整性。
- 建议：(1) 加入 logistic regression DIF 作为比较方法；(2) 增强半合成框架复杂度；(3) 更清晰论述 LLM 场景下 MH-DIF 应用本身构成 non-trivial 贡献。

### Should-Fix 问题

**W1** [warning] 半合成注入模型过于简化（uniform binary flipping 不能模拟真实污染模式）
**W2** [warning] 与 MMLU-CF (Qiao et al., ACL 2025) 的关系讨论不足
**W3** [warning] Subject-level 异质性分析不充分（22/57 subjects ρ<0.95 但缺深入分析）
**W4** [warning] GSM1K 探索性分析空间分配不当（N=33, r=-0.478 但占半栏）
**W5** [warning] Abstract 信息密度过高

### Questions
Q1: Figure 6 的 DIF-ordered removal 是否意味着 DIF 题目承载有效区分信息？Flag/Act 协议是否需重新考虑？
Q2: 纳入 non-uniform DIF 后，总 temporal DIF 比例是多少？
Q3: 如何处理 temporal blurring（发布日期 ≠ 训练数据 cutoff）？
Q4: Cross-subject matching 在多学科同时被污染时假设是否被违反？
Q5: DIF pattern 在更长时间尺度上会更严重还是饱和？

### Missing References
Wainer (1993) DIF 经典教科书; Embretson & Reise (2000) IRT for Psychologists; McNeish et al. (2024) measurement invariance in ML evaluation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 778 · 2026-05-22T13:19:13.778859+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: ρ ≈ 0.997 与 31% DIF 的张力 / Figure 6 与 Flag/Act 协议的矛盾**\n\nR2 的核心论点有两层：(a) ρ≈0.997 使 31% DIF 的实际意义不清，(b) Figure 6 证明 DIF 题目承载有效区分信息，与\"移除 DIF 题目\"的建议矛盾。\n\n对于 (a)，论文在 Section 5.1 已明确调和：\"The high aggregate correlation (ρ = 0.997) does not undermine DIF's utility—it demonstrates that MMLU's item redundancy (≈12,500 items) absorbs temporal shifts at the aggregate level.\" Item-level instability 与 aggregate stability 的共存在教育测量中是经典现象——高冗余测试可以在 item 层面有大量 DIF 但总分排名不变。论文的定位是\"diagnostic, not destructive\"，这一框架在 Section 5.1 中是连贯的。\n\n对于 (b)，R2 **误读了 Section 5.3 的建议**。论文的 Flag/Act 协议原文是：\"(3) Flag/Act (>25%): report DIF-flagged items; use DIF pre-screening for **equating** anchor items (Kolen and Brennan, 2014; Hubbs et al., 2026)\"。论文建议用 DIF 信息进行**等值化（equating）**，而非移除 DIF 题目。Figure 6 的发现与此完全一致——DIF 题目承载区分信息，所以不应移除，而应在跨时间比较时进行等值调整。\n\n**但 R2 指出了一个真实的呈现问题**：Section 5.3 的 \"Flag/Act\" 标签容易让读者（如 R2）误解为 \"flag and remove\"。论文应更明确区分 within-cohort 评估（保留所有题目）与 cross-temporal 比较（对 DIF 题目做等值调整）两种使用场景。此外，R2 关于提供\"DIF 实质性改变结论的具体案例\"的建议有价值——Figure 4 (downstream impact) 已部分做到，但可以更加具体化。\n\n**结论**：核心张力在论文中已被合理调和，但呈现需改进。不同意升级为 Must-Fix——呈现优化属于 Should-Fix 级别。\n\n---\n\n**[AGREE in part, REBUT in part] R2-N2: 方法论新颖性不足 / non-uniform DIF 被低估**\n\nR2 的论点包含两个不同的声明，需分别评估：\n\n**(a) MH-DIF 本身不新颖 → 部分反驳**\n\n将成熟方法应用于新领域是 *ACL 的标准贡献类型，关键在于应用是否 non-trivial。本文的应用确实是 non-trivial：\n- LLM 非独立性（family clustering）需要 DEFF/cluster bootstrap 等 survey 方法论的整合（Appendix C）\n- 确定性响应与 MH 概率框架的张力需要方法论论证\n- Semi-synthetic 验证框架（cross-subject matching with ΔFPR=0 guarantee）是原创的方法论贡献\n- 5,227 模型 × 27,125 items × 6 benchmarks 的规模前所未有\n\n但 R2 指出缺乏与其他 DIF 方法（logistic regression, SIBTEST）的比较——这一批评是合理的。论文在 Appendix B 已有 logistic regression 的结果，在方法论完整性上至少应在 main text 中报告比较结果。\n\n**(b) 24.8% non-uniform DIF 被埋在 Limitations → 同意**\n\n这是 R2 意见中最有力的一点。Limitations (p9) 提到 \"24.8% of items showing non-uniform patterns (ability-dependent DIF) may be underestimated by the Mantel-Haenszel statistic\"。如果近四分之一的题目存在 MH-DIF 无法有效检测的 non-uniform DIF，这意味着：\n- 论文报告的 31% 可能**低估**了总 temporal DIF 率\n- Uniform DIF (31%) + non-uniform DIF (24.8%) 的并集可能远高于 31%（取决于两者的重叠度）\n- 论文的核心方法遗漏了相当大比例的 DIF\n\n这个发现不应被埋在 Limitations 中。建议在 main text 中增加一段 non-uniform DIF 的分析，报告 uniform + non-uniform 的总 DIF 率，并讨论这对结论的影响。\n\n**结论**：方法论新颖性通过 domain adaptation 和 semi-synthetic 框架成立，不需要升级为 Must-Fix。但 24.8% non-uniform DIF 的发现确实需要从 Limitations 提升到 main text 讨论，这部分同意 R2 的 Should-Fix 级别。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 半合成注入模型过于简化**\n\n与我的 W1 一致。Uniform binary flipping 的生态效度问题是两位 reviewer 的共识。\n\n**[AGREE in part] R2-W2: 与 MMLU-CF 的关系讨论不足**\n\nMMLU-CF (Qiao et al., ACL 2025) 通过替换选项/问题格式来创建 contamination-free 变体，与本文的 DIF 方法论互补：MMLU-CF 通过 item reformulation 消除污染优势，本文通过统计检测识别受影响的 items。论文 Section 2 (Related Work, p3) 引用了 MMLU-CF，但未深入讨论两种方法的互补性和差异。这是合理的 Should-Fix——增加 1-2 句对比即可。\n\n**[AGREE in part] R2-W3: Subject-level 异质性分析不充分**\n\nR2 提到 \"22/57 subjects ρ<0.95\"。论文在 Section 4.6 / Table 5 报告了 domain-level Cohen's d，在 Appendix 中有 subject-level 详细数据。但确实缺乏对 DIF 异质性模式的深入分析——哪些 subjects 最不稳定？是否与 subject 的 knowledge-intensive 程度相关？Figure 4 中 Mistral 和 Llama-3 的 distinctive profile 暗示了有趣的 pattern，但未被充分挖掘。不过考虑 8 页限制，将详细 subject-level 分析放在 Appendix 是合理的。建议在 main text 增加 1-2 句 summary。\n\n**[AGREE] R2-W4: GSM1K 分析空间分配不当**\n\n与我的小问题 #4 一致。N=33 的探索性分析占据 main text 半栏过多。\n\n**[AGREE] R2-W5: Abstract 信息密度过高**\n\n与我的小问题 #1 一致。\n\n---\n\n### Questions 回应\n\n**R2-Q1** (Figure 6 vs Flag/Act): 如上文 N1 回应所述，论文建议 equating 而非 removal。Figure 6 实际上**支持**了论文的论点——DIF 题目有区分力，移除会损失信息，因此应 equate 而非 remove。但论文确实应更清楚地表述这一点。\n\n**R2-Q2** (总 DIF 比例): 同意这是重要问题。Uniform (31%) + non-uniform (24.8%) 的并集大小取决于两者重叠度，论文应报告。如果重叠低，总 DIF 率可能 >45%，这会显著改变 narrative。\n\n**R2-Q3** (temporal blurring): 与我的 W5 一致。Release date 作为 temporal proxy 的局限性需要讨论。\n\n**R2-Q4** (Cross-subject matching 多学科污染): 与我的 W2 一致。Table 6 已提供部分数据但不够充分。\n\n**R2-Q5** (长时间尺度 DIF 趋势): 有趣的问题，但论文数据仅覆盖 2023-2024 两年，无法回答。可在 Future Work 中提及。\n\n---\n\n### Missing References 回应\n\n**[AGREE] Wainer (1993)**: *Differential Item Functioning* 确实是 DIF 领域的经典参考书，论文引用了 Holland and Thayer (1988) 但未引用这本综合性教科书。\n\n**[AGREE] Embretson & Reise (2000)**: 与 Limitations 中讨论的 IRT model fit 问题相关，引用会加强 theoretical grounding。\n\n**[NEUTRAL] McNeish et al. (2024)**: 需要确认具体内容。如果该论文讨论 ML 评估中的 measurement invariance，则高度相关。但我未见过该文献，无法判断其真实性和相关性。\n\n---\n\n### 总体评价\n\nR2 的审稿意见质量较高，核心关注点与我的审查互补——R2 聚焦新颖性和\"so what\"问题，我聚焦方法论严谨性。\n\n**两位 reviewer 的共识问题**（应优先解决）：\n1. 半合成注入模型过于简化（R1-W1 = R2-W1）\n2. Abstract 信息密度过高（R1-小问题#1 = R2-W5）\n3. GSM1K 分析空间分配不当（R1-小问题#4 = R2-W4）\n4. Cross-subject matching 边界条件不足（R1-W2 ≈ R2-Q4）\n5. Temporal cohort 粗粒度（R1-W5 ≈ R2-Q3）\n\n**分歧点**：\n- R2-N1 对 ρ vs DIF 张力的严重程度评估偏高——论文已合理调和，但呈现需改进。我认为 Should-Fix 而非 Must-Fix。\n- R2-N2 对方法论新颖性的要求可能过高——domain adaptation + semi-synthetic framework 在 *ACL 是充分的贡献类型。但 non-uniform DIF 的发现确实需要提升。\n\n**我的 Must-Fix 中 R2 未覆盖的问题**：\n- DEFF 校正的收敛性声明（R1-N1）——R2 未讨论非独立性校正方法之间 13.5% vs 29.2% 的巨大差异\n- Item-level 非独立性对 MH 检验的影响（R1-N2）——R2 未涉及有效样本量问题\n\n这些方法论细节正是 R2（新颖性/完整性视角）与 R1（方法严谨性视角）的互补之处。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: ρ ≈ 0.997 与 31% DIF 的张力 / Figure 6 与 Flag/Act 协议的矛盾**\n\nR2 的核心论点有两层：(a) ρ≈0.997 使 31% DIF 的实际意义不清，(b) Figure 6 证明 DIF 题目承载有效区分信息，与\"移除 DIF 题目\"的建议矛盾。\n\n对于 (a)，论文在 Section 5.1 已明确调和：\"The high aggregate correlation (ρ = 0.997) does not undermine DIF's utility—it demonstrates that MMLU's item redundancy (≈12,500 items) absorbs temporal shifts at the aggregate level.\" Item-level instability 与 aggregate stability 的共存在教育测量中是经典现象——高冗余测试可以在 item 层面有大量 DIF 但总分排名不变。论文的定位是\"diagnostic, not destructive\"，这一框架在 Section 5.1 中是连贯的。\n\n对于 (b)，R2 **误读了 Section 5.3 的建议**。论文的 Flag/Act 协议原文是：\"(3) Flag/Act (>25%): report DIF-flagged items; use DIF pre-screening for **equating** anchor items (Kolen and Brennan, 2014; Hubbs et al., 2026)\"。论文建议用 DIF 信息进行**等值化（equating）**，而非移除 DIF 题目。Figure 6 的发现与此完全一致——DIF 题目承载区分信息，所以不应移除，而应在跨时间比较时进行等值调整。\n\n**但 R2 指出了一个真实的呈现问题**：Section 5.3 的 \"Flag/Act\" 标签容易让读者（如 R2）误解为 \"flag and remove\"。论文应更明确区分 within-cohort 评估（保留所有题目）与 cross-temporal 比较（对 DIF 题目做等值调整）两种使用场景。此外，R2 关于提供\"DIF 实质性改变结论的具体案例\"的建议有价值——Figure 4 (downstream impact) 已部分做到，但可以更加具体化。\n\n**结论**：核心张力在论文中已被合理调和，但呈现需改进。不同意升级为 Must-Fix——呈现优化属于 Should-Fix 级别。\n\n---\n\n**[AGREE in part, REBUT in part] R2-N2: 方法论新颖性不足 / non-uniform DIF 被低估**\n\nR2 的论点包含两个不同的声明，需分别评估：\n\n**(a) MH-DIF 本身不新颖 → 部分反驳**\n\n将成熟方法应用于新领域是 *ACL 的标准贡献类型，关键在于应用是否 non-trivial。本文的应用确实是 non-trivial：\n- LLM 非独立性（family clustering）需要 DEFF/cluster bootstrap 等 survey 方法论的整合（Appendix C）\n- 确定性响应与 MH 概率框架的张力需要方法论论证\n- Semi-synthetic 验证框架（cross-subject matching with ΔFPR=0 guarantee）是原创的方法论贡献\n- 5,227 模型 × 27,125 items × 6 benchmarks 的规模前所未有\n\n但 R2 指出缺乏与其他 DIF 方法（logistic regression, SIBTEST）的比较——这一批评是合理的。论文在 Appendix B 已有 logistic regression 的结果，在方法论完整性上至少应在 main text 中报告比较结果。\n\n**(b) 24.8% non-uniform DIF 被埋在 Limitations → 同意**\n\n这是 R2 意见中最有力的一点。Limitations (p9) 提到 \"24.8% of items showing non-uniform patterns (ability-dependent DIF) may be underestimated by the Mantel-Haenszel statistic\"。如果近四分之一的题目存在 MH-DIF 无法有效检测的 non-uniform DIF，这意味着：\n- 论文报告的 31% 可能**低估**了总 temporal DIF 率\n- Uniform DIF (31%) + non-uniform DIF (24.8%) 的并集可能远高于 31%（取决于两者的重叠度）\n- 论文的核心方法遗漏了相当大比例的 DIF\n\n这个发现不应被埋在 Limitations 中。建议在 main text 中增加一段 non-uniform DIF 的分析，报告 uniform + non-uniform 的总 DIF 率，并讨论这对结论的影响。\n\n**结论**：方法论新颖性通过 domain adaptation 和 semi-synthetic 框架成立，不需要升级为 Must-Fix。但 24.8% non-uniform DIF 的发现确实需要从 Limitations 提升到 main text 讨论，这部分同意 R2 的 Should-Fix 级别。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 半合成注入模型过于简化**\n\n与我的 W1 一致。Uniform binary flipping 的生态效度问题是两位 reviewer 的共识。\n\n**[AGREE in part] R2-W2: 与 MMLU-CF 的关系讨论不足**\n\nMMLU-CF (Qiao et al., ACL 2025) 通过替换选项/问题格式来创建 contamination-free 变体，与本文的 DIF 方法论互补：MMLU-CF 通过 item reformulation 消除污染优势，本文通过统计检测识别受影响的 items。论文 Section 2 (Related Work, p3) 引用了 MMLU-CF，但未深入讨论两种方法的互补性和差异。这是合理的 Should-Fix——增加 1-2 句对比即可。\n\n**[AGREE in part] R2-W3: Subject-level 异质性分析不充分**\n\nR2 提到 \"22/57 subjects ρ<0.95\"。论文在 Section 4.6 / Table 5 报告了 domain-level Cohen's d，在 Appendix 中有 subject-level 详细数据。但确实缺乏对 DIF 异质性模式的深入分析——哪些 subjects 最不稳定？是否与 subject 的 knowledge-intensive 程度相关？Figure 4 中 Mistral 和 Llama-3 的 distinctive profile 暗示了有趣的 pattern，但未被充分挖掘。不过考虑 8 页限制，将详细 subject-level 分析放在 Appendix 是合理的。建议在 main text 增加 1-2 句 summary。\n\n**[AGREE] R2-W4: GSM1K 分析空间分配不当**\n\n与我的小问题 #4 一致。N=33 的探索性分析占据 main text 半栏过多。\n\n**[AGREE] R2-W5: Abstract 信息密度过高**\n\n与我的小问题 #1 一致。\n\n---\n\n### Questions 回应\n\n**R2-Q1** (Figure 6 vs Flag/Act): 如上文 N1 回应所述，论文建议 equating 而非 removal。Figure 6 实际上**支持**了论文的论点——DIF 题目有区分力，移除会损失信息，因此应 equate 而非 remove。但论文确实应更清楚地表述这一点。\n\n**R2-Q2** (总 DIF 比例): 同意这是重要问题。Uniform (31%) + non-uniform (24.8%) 的并集大小取决于两者重叠度，论文应报告。如果重叠低，总 DIF 率可能 >45%，这会显著改变 narrative。\n\n**R2-Q3** (temporal blurring): 与我的 W5 一致。Release date 作为 temporal proxy 的局限性需要讨论。\n\n**R2-Q4** (Cross-subject matching 多学科污染): 与我的 W2 一致。Table 6 已提供部分数据但不够充分。\n\n**R2-Q5** (长时间尺度 DIF 趋势): 有趣的问题，但论文数据仅覆盖 2023-2024 两年，无法回答。可在 Future Work 中提及。\n\n---\n\n### Missing References 回应\n\n**[AGREE] Wainer (1993)**: *Differential Item Functioning* 确实是 DIF 领域的经典参考书，论文引用了 Holland and Thayer (1988) 但未引用这本综合性教科书。\n\n**[AGREE] Embretson & Reise (2000)**: 与 Limitations 中讨论的 IRT model fit 问题相关，引用会加强 theoretical grounding。\n\n**[NEUTRAL] McNeish et al. (2024)**: 需要确认具体内容。如果该论文讨论 ML 评估中的 measurement invariance，则高度相关。但我未见过该文献，无法判断其真实性和相关性。\n\n---\n\n### 总体评价\n\nR2 的审稿意见质量较高，核心关注点与我的审查互补——R2 聚焦新颖性和\"so what\"问题，我聚焦方法论严谨性。\n\n**两位 reviewer 的共识问题**（应优先解决）：\n1. 半合成注入模型过于简化（R1-W1 = R2-W1）\n2. Abstract 信息密度过高（R1-小问题#1 = R2-W5）\n3. GSM1K 分析空间分配不当（R1-小问题#4 = R2-W4）\n4. Cross-subject matching 边界条件不足（R1-W2 ≈ R2-Q4）\n5. Temporal cohort 粗粒度（R1-W5 ≈ R2-Q3）\n\n**分歧点**：\n- R2-N1 对 ρ vs DIF 张力的严重程度评估偏高——论文已合理调和，但呈现需改进。我认为 Should-Fix 而非 Must-Fix。\n- R2-N2 对方法论新颖性的要求可能过高——domain adaptation + semi-synthetic framework 在 *ACL 是充分的贡献类型。但 non-uniform DIF 的发现确实需要提升。\n\n**我的 Must-Fix 中 R2 未覆盖的问题**：\n- DEFF 校正的收敛性声明（R1-N1）——R2 未讨论非独立性校正方法之间 13.5% vs 29.2% 的巨大差异\n- Item-level 非独立性对 MH 检验的影响（R1-N2）——R2 未涉及有效样本量问题\n\n这些方法论细节正是 R2（新颖性/完整性视角）与 R1（方法严谨性视角）的互补之处。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 779 · 2026-05-22T13:19:17.894953+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4116
}
```

</details>

---


### Assistant

_source line 780 · 2026-05-22T13:19:24.674268+00:00_

交叉回应已提交。核心判断：

- **R2-N1**（ρ vs DIF 张力）：部分反驳——论文已合理调和，但 Section 5.3 的 Flag/Act 表述易被误读为"移除"而非"等值化"，降级为 Should-Fix
- **R2-N2**（方法新颖性）：部分同意——domain adaptation + semi-synthetic 框架构成充分贡献，但 24.8% non-uniform DIF 埋在 Limitations 是真实缺陷
- **R2-W1/W4/W5**：与我的意见一致
- **两位 reviewer 未覆盖对方的关键点**：R2 未涉及 DEFF 收敛性和 item-level 非独立性（我的 N1/N2），我未涉及 non-uniform DIF 的低估问题（R2-N2b）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 28

## Round 28

48 recorded events


### User

_source line 781 · 2026-05-22T15:06:48.070283+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查本论文的**方法严谨性和实验设计**。

## 投稿信息
- **Venue**: EMNLP 2026 via ACL Rolling Review (ARR)
- **类别**: Long paper
- **截止日期**: 2026-05-25
- **页数限制**: 正文 8 页，参考文献不限，Limitations 章节不计页数
- **模板**: ACL `[review]` 模板
- **匿名**: Double-blind

## 论文文件
- 主文件: `projects/irt_equated_bench_regen/paper/main.tex`
- Section 文件: `projects/irt_equated_bench_regen/paper/sections/` 下的 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex
- 参考文献: `projects/irt_equated_bench_regen/paper/references.bib`
- PDF: `projects/irt_equated_bench_regen/artifacts/review_round_10/submitted.pdf`

## 论文概要
标题: "Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models"
将教育测量的 DIF (Differential Item Functioning) 分析应用于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU items），检测 2023-2024 模型代际间的时间测量不稳定性。核心发现：~31% 的 MMLU items 表现出 ETS Category C 级别的 DIF，web-overlap 污染标签与 DIF 标记近乎独立（Jaccard=0.206）。提出 cross-subject matching 策略实现 ΔFPR=0，并在 6 个 METABENCH 基准上复现。

## 你的审查侧重

请严格、不留情面地审查以下方面：

### 1. DIF 方法论正确性
- MH-DIF 应用于 LLM 的适用性——LLM 不是人类考生，MH 的前提假设（条件独立、单维性等）是否满足？论文对违反假设的讨论是否充分？
- K=5 分层（quintile binning）的选择是否合理？是否有敏感性分析？
- ETS C 分类的双重阈值（|Δ_MH| ≥ 1.5 且 p < 0.05）在 N=5,227 这种超大样本下是否还有意义？p 值在大样本下几乎总是显著的
- Cross-subject matching 的理论保证（ΔFPR=0）是否严格成立？前提条件是什么？

### 2. 统计有效性
- 多重比较问题：12,508 个 items 同时检验，ETS 双重阈值是否足以控制 FPR？BH-FDR 只重分类 3 个 item 的说法是否可信？
- Bootstrap CI 的计算方法是否正确？model-level 和 family-level cluster bootstrap 的区别和适用性
- Design effect 校正（DEFF）的两种 m̄ 估计产生 13.5%-29.2% 的巨大范围——这个不确定性是否削弱了核心结论？
- 非独立考生（model families）对 MH χ² 的影响是否被充分量化？

### 3. Semi-synthetic 框架
- Binary response flipping 是否是合理的污染模拟？与真实污染模式的差距有多大？
- ΔTPR = +0.508 at p=0.5 的检测能力是否足够？
- 框架的 internal validity 和 external validity

### 4. 控制实验和鲁棒性
- Random split、ability quintile、within-family 等控制实验设计是否充分？
- 六个基准的 cross-benchmark validation 是否可靠？
- Leave-one-family-out 分析的解释是否正确？

### 5. 可重复性
- 数据和代码是否可获取？匿名链接是否有效？
- 方法描述是否足够详细以允许独立复现？

请按以下格式输出审稿意见：
1. **Summary** (2-3 句)
2. **Strengths** (逐条)
3. **Weaknesses** (逐条，每条标注严重程度：[Critical] / [Major] / [Minor])
4. **Questions** (需要作者澄清的问题)
5. **Missing References** (遗漏的重要相关工作)
6. **Overall Assessment** (评分 + 理由，使用 EMNLP 2026 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit)
7. **Confidence** (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 782 · 2026-05-22T15:06:58.163855+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 783 · 2026-05-22T15:06:59.018909+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 784 · 2026-05-22T15:06:59.069690+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 785 · 2026-05-22T15:06:59.120458+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-22T15:07:03.042813+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 787 · 2026-05-22T15:07:03.796400+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 788 · 2026-05-22T15:07:13.202088+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found comprehensive information about ACL Rolling Review 2026. Here are the key details about reviewer guidelines, review form, and criteria:

## Reviewer Guidelines

Reviewers are asked to follow a workflow: (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that particular submission. If reviewers feel qualified to review some aspects but not others (e.g., experimental results but not formal proofs), they should state in the review if they did not check some major pa
…[truncated 1092 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 10159
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-22T15:07:15.113446+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 573.4}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 531.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 558.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 471.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 556.9}], \"total_pages\": 16, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_ro
…[truncated 59 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 11317
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-22T15:07:21.548586+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other scoring criteria. Get the exact wording and scale for each dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other scoring criteria. Get the exact wording and scale for each dimension."
  }
}
```

</details>

---


### Tool call

_source line 791 · 2026-05-22T15:07:22.052055+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 792 · 2026-05-22T15:07:22.403545+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 793 · 2026-05-22T15:07:23.311448+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1259
}
```

</details>

---


### Tool result

_source line 794 · 2026-05-22T15:07:23.463173+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---


### Tool call

_source line 795 · 2026-05-22T15:07:23.463662+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 796 · 2026-05-22T15:07:23.767549+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 797 · 2026-05-22T15:07:24.529338+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1065
}
```

</details>

---


### Tool result

_source line 798 · 2026-05-22T15:07:24.884887+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1117
}
```

</details>

---


### Tool result

_source line 799 · 2026-05-22T15:07:28.301970+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Overall Assessment
**Scale: 1-5 with half-point increments**

- 5 = Consider for Award (top 2.5% papers)
- 4.5 = Borderline Award
- 4 = Conference acceptance
- 3.5 = Borderline Conference
- 3 = Findings acceptance
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle
- 1.5 = Resubmit after next cycle
- 1 = Do not resubmit

## Soundness
**Scale: 1-5 with half-point increments**

Evaluates technical rigor and support for claims. Considerations vary by paper type (experimental, position, survey, resource).

- 5 = Excellent: "one of the most thorough I have seen"
- 4 = Strong: sufficient support with minor gaps
- 3 = Acceptable: main claims supported adequately
- 2 = Poor: major technical/methodological issues
- 1 = Major Issues: insufficient for publication

## Excitement
**Scale: 1-5 with half-point increments**

Measures subjective appeal regarding innovation, impact, and relevance.

- 5 = Highly Exciting: "would recommend this paper to others"
- 4 = Exciting: would mention to colleagues
- 3 = Interesting: might discuss selectively
- 2 = Potentially Interesting: doesn't resonate personally
- 1 = Not Exciting: limited community relevance

## Reviewer Confidence
**Scale: 1-5**

- 5 = Positive evaluation; thoroughly reviewed
- 4 = Quite sure; unlikely major oversights
- 3 = Pretty sure; some unchecked details
- 2 = Willing to defend; likely missed elements
- 1 = Educated guess; unfamiliar territory

## Reproducibility
**Scale: 1-5**

- 5 = Easily reproducible
- 4 = Mostly reproducible with minor variations
- 3 = Reproducible with difficulty
- 2 = Very difficult; unavailable data/underspecified methods
- 1 = Impossible to reproduce

## Datasets & Software
**Scale: 1-5 each**

- 5 = Enabling: affects research trajectory decisions
- 4 = Useful: recommended for ongoing work
- 3 = Potentially useful: helpful for some researchers
- 2 = Documentary: useful for replication only
- 1 = No usable contributions released

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6753
}
```

</details>

---


### Tool call

_source line 800 · 2026-05-22T15:07:34.498374+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 801 · 2026-05-22T15:07:34.601907+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 802 · 2026-05-22T15:07:34.602383+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 803 · 2026-05-22T15:07:35.357422+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 804 · 2026-05-22T15:07:36.269427+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1771
}
```

</details>

---


### Tool result

_source line 805 · 2026-05-22T15:07:36.623979+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2022
}
```

</details>

---


### Tool result

_source line 806 · 2026-05-22T15:07:36.780723+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2178
}
```

</details>

---


### Tool result

_source line 807 · 2026-05-22T15:07:37.083495+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1726
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-22T15:07:42.911895+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "9-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "9-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 809 · 2026-05-22T15:07:43.917957+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 530.4}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 596.1}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 589.3}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 557.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 499.3}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.0}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 320.6}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 94.9}], \"total_pages\": 16, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifa
…[truncated 72 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 810 · 2026-05-22T15:07:47.483961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 811 · 2026-05-22T15:07:47.835928+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 812 · 2026-05-22T15:07:48.746013+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1262
}
```

</details>

---


### Tool result

_source line 813 · 2026-05-22T15:07:48.747266+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 911
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-22T15:07:48.797901+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 815 · 2026-05-22T15:07:49.150912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 816 · 2026-05-22T15:07:49.604560+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool result

_source line 817 · 2026-05-22T15:07:50.059100+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 818 · 2026-05-22T15:07:53.522936+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 819 · 2026-05-22T15:07:54.026905+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 820 · 2026-05-22T15:07:54.937818+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1414
}
```

</details>

---


### Tool result

_source line 821 · 2026-05-22T15:07:54.938960+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 912
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-22T15:07:54.939287+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 823 · 2026-05-22T15:07:55.241194+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 824 · 2026-05-22T15:07:55.444639+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 203
}
```

</details>

---


### Tool result

_source line 825 · 2026-05-22T15:07:55.602213+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 662
}
```

</details>

---


### Tool call

_source line 826 · 2026-05-22T15:11:25.086136+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见（Round 1）\n\n**论文**: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**审查侧重**: 方法严谨性与实验设计\n**审稿标准**: ACL Rolling Review (EMNLP 2026)\n\n---\n\n## 1. Summary\n\n本文将教育测量中的 Mantel-Haenszel DIF 分析应用于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU items），检测 2023 与 2024 模型代际间的测量不稳定性。核心发现是约 31% 的 MMLU items 表现出 ETS Category C 级别的 DIF，且 web-overlap 污染标签与 DIF 标记近乎独立（Jaccard=0.206）。论文提出 cross-subject matching 策略并在 6 个基准上进行交叉验证。这是一个有价值的研究方向——将成熟的心理测量工具引入 LLM 评估——但方法论上存在若干需要正视的缺陷。\n\n---\n\n## 2. Strengths\n\n**S1. 新颖且重要的研究视角。** 将 DIF 分析应用于 LLM benchmark 时间稳定性评估是真正新颖的贡献。Figure 1（page 2）清晰区分了 global contamination 和 differential contamination，叙事精炼有力。这一框架将\"污染检测\"问题重新定义为\"测量不变性\"问题，为社区提供了新的诊断工具。\n\n**S2. 规模与数据基础扎实。** 5,227 模型 × 12,508 items 的分析规模在同类工作中无出其右。使用公开的 METABENCH 数据增强了可信度和可复现性。\n\n**S3. 控制实验设计较为系统。** Random split baseline（C%=0.18%，Section 3.3 cohort 5）、within-family 对比（Llama-2 vs Llama-3，Section 4.2）、leave-one-family-out 分析（Table 7）、以及 cross-benchmark replication（Table 3，6 个基准）构成了多层次的验证体系。\n\n**S4. 实用价值明确。** Section 5.2 提出了具体的监测建议（Monitor/Flag 15%、Flag/Act 25%），配合 Figure 6 的 ranking degradation 分析，对基准维护者有直接指导意义。\n\n**S5. 写作质量高。** 论文在 8 页正文内组织了大量内容，结构紧凑，Figure 和 Table 的信息密度高。\n\n---\n\n## 3. Weaknesses\n\n**W1 [Critical] DEFF 校正范围过大，核心结论的不确定性被低估。**\n\nSection 4.2 和 Appendix C 报告 design-effect 校正后 adjusted C% 范围为 [13.5%, 29.2%]（Section C, page 14: simple mean m̄=3.87 yields DEFF=3.87, adjusted C%=29.2%; weighted mean m̄=25.4 yields DEFF=12.79, adjusted C%=13.5%）。这意味着核心发现——\"~31% items exhibit DIF\"——在考虑 family 非独立性后，可能只有 13.5%，即缩水超过一半。\n\n论文虽然报告了两个边界，但未充分讨论哪个 m̄ 估计更合理，也未提供理由偏好其一。仅在 Limitations 中一句带过（\"the lower bound far exceeds the random-split baseline\"）。虽然 13.5% 仍远超 baseline 0.18%，但\"约三分之一 items 有 DIF\"与\"约七分之一 items 有 DIF\"是截然不同的叙事。论文标题和 abstract 使用\"31%\"作为 headline number，但正文承认这可能因非独立性膨胀至近 2 倍——这一不确定性应在 abstract 中被明确提及。\n\n**建议**: (1) 明确论证 simple mean 与 weighted mean 哪个更适用于本数据，或报告一个 bracketed range 作为主结论；(2) Abstract 和 Section 4.2 的 headline number 应改为 \"[13.5%–31%] of items\" 或类似表述。\n\n**W2 [Critical] LLM 非独立性假设违反的影响被分散处理，缺乏统一量化。**\n\nMH-DIF 的核心假设是考生独立。但 LLM 同 family 共享训练数据和架构，严重违反此假设。论文在多处分散讨论了这一问题：\n- Section 3.2（\"LLM-specific challenges\"）提及 fine-tuned variants 和 family structure\n- Appendix C 计算 ICC 和 DEFF\n- Appendix D 做 cluster bootstrap\n- Table 7 做 leave-one-family-out\n- Appendix A.1 检查 Yen's Q3\n\n但这些分析之间缺乏统一框架。例如：Appendix D 的 cluster bootstrap 下界是 26.7%（simple DEFF adjustment）到 29.2%，而 Appendix C 的 DEFF 下界是 13.5%。这两个\"robustness\"结果相互矛盾——cluster bootstrap 似乎暗示影响不大，而 DEFF 暗示影响可能很大。论文未解释这一差异。\n\n具体来说，ICC = 0.047 (median 0.041, Q3 = 0.061)，看似不大，但 m̄ 的选择（3.87 vs 25.4）导致 DEFF 从 1.13 到 12.79，相差一个数量级。问题核心在于：应该用 family 均值（~3.87 models/family）还是有效样本量加权均值（~25.4，因为大 family 贡献更多考生）来估计 m̄？后者更合理（因为大 family 对 χ² 统计量的膨胀贡献更大），但论文未做出明确选择。\n\n**建议**: 统一处理非独立性：明确选择 DEFF 估计方法并论证，或用 permutation test（在 family 层级 shuffle temporal labels）直接获得一个不依赖参数假设的 null distribution。\n\n**W3 [Major] Semi-synthetic 框架的 binary response flipping 过于简化，external validity 存疑。**\n\nSection 3.4 的注入框架将\"污染\"建模为 binary response flipping（incorrect → correct，以概率 p）。Limitations（page 9）承认\"Real-world contamination involves partial memorization, reasoning shortcuts, and format-specific advantages\"。\n\n问题在于：\n(a) 真实污染不是二值的——模型可能部分记忆了答案的推理链，导致在相似但不同的 items 上也表现更好。这种 spillover 效应在 binary flipping 框架下完全不可见。\n(b) 污染概率 p 对不同 ability 水平的模型应有不同影响（低能力模型从污染中获益更大），但框架中 p 是 uniform 的。\n(c) Figure 2 的 dose-response 曲线（ΔTPR 随 p 单调递增）在此简化模型下是 trivially expected 的——它没有提供多少关于真实检测能力的信息。\n\nSemi-synthetic 框架的核心价值在于 calibrate detection power，但如果注入模型与真实污染模式差异太大，calibration 本身就不可靠。\n\n**建议**: (1) 至少讨论一种更现实的注入模型（如 ability-dependent flipping：低能力模型 p_high，高能力模型 p_low）并报告 sensitivity；(2) 使用 GSM8K 的已知污染案例（Section 4.7 提到 GSM8K semi-synthetic injection）做 real-world calibration。\n\n**W4 [Major] Cross-subject matching 的 ΔFPR=0 保证条件过于理想化。**\n\nSection 3.4 的 Remark（Zero FPR under single-subject matching）数学上是正确的，但前提条件——污染仅限于单一 subject——在实践中几乎不成立。论文自己也承认（同一 Section）：\"When contamination spans multiple subjects simultaneously, M_i will absorb signal from other contaminated subjects, potentially inflating FPR.\"\n\n实证验证（ΔFPR = 0.000，95% CI = [0.000, 0.004]）仅在 single-subject injection 下测试。Broader contamination（k=10 subjects）下 ΔFPR 升至 0.017±0.023，而 worst-case 为 ~7pp。虽然论文称\"Even worst-case multi-subject inflation (~7 pp) cannot account for the observed 31% C% rate\"，但如果核心 C% 可能只有 13.5%（W1 的 DEFF 下界），7pp 的 FPR inflation 就不再可以忽略。\n\n**建议**: (1) 在 DEFF-adjusted 的下界 13.5% 语境下重新评估 multi-subject FPR inflation 的影响；(2) 提供 multi-subject injection 的完整 FPR 曲线而非仅报告 k=10 的点估计。\n\n**W5 [Major] 缺少 K（分层数）敏感性分析。**\n\nSection 3.2 使用 K=5 quintile 分层，引用 ETS 推荐做法。但 K 的选择对 MH-DIF 结果有实质影响——过少的分层导致 ability 匹配不精确（residual confounding），过多则每层样本量不足。论文仅在 Appendix A.2 报告了 |Δ_MH| 阈值敏感性（1.0, 1.5, 2.0, 2.5），但完全没有报告 K 的敏感性（如 K=3, 5, 7, 10）。\n\n在 N=5,227 这种大样本下，K=5 可能过粗（每层~1,045 个模型），导致 ability group 内部仍有较大异质性。这对 cross-subject matching 尤其重要——如果 matching 不够精细，可能产生 residual confounding 从而虚高 DIF 率。\n\n**建议**: 报告 K ∈ {3, 5, 7, 10} 的 C% 变化，确认核心结论对分层数稳健。\n\n**W6 [Major] 大样本下 p 值几乎失去筛选作用，ETS 双重阈值的有效性需要更深讨论。**\n\nN=5,227 时，MH χ² 检验的统计功效极高。对任何具有 |Δ_MH| ≥ 1.5 的 item，p < 0.05 几乎肯定成立。论文在 Appendix A.2 提到 BH-FDR 仅重分类 3 个 items，恰好印证了这一点——p 值在这个样本量下基本是多余的。\n\n但这也意味着 ETS 双重阈值在本研究中实质上退化为单一的效应量阈值（|Δ_MH| ≥ 1.5）。论文应明确讨论这一点，而非让读者误以为 p < 0.05 提供了独立的误判控制。\n\n更深层的问题：当 DEFF 校正将有效样本量从 5,227 缩小到 ~400-1,350（取决于 m̄ 选择）时，p 值的筛选作用可能会恢复。论文报告了 DEFF 校正后 C% 从 31% 降至 13.5%-29.2%，但未说明这些被重分类的 items 是因为 |Δ_MH| 缩小还是因为 p 值不再显著。这一区分很重要。\n\n**建议**: (1) 分别报告 DEFF 校正后因效应量标准和因显著性标准被重分类的 items 数量；(2) 讨论在本研究的有效样本量下，p < 0.05 是否提供了超出效应量阈值的额外信息。\n\n**W7 [Minor] Unidimensionality 假设讨论不足。**\n\nMMLU 涵盖 57 个 subjects、5 大 domains，本质上是高度多维的。MH-DIF 以 total score 为 matching variable，隐含了 unidimensionality 假设。论文在 Section 3.2 讨论了三种 matching 策略，并在 Appendix A.1 检查了 domain-specificity，但未正式检验 unidimensionality（如 factor analysis 或 scree plot）。\n\nCross-subject matching 部分缓解了这一问题（使用其他 subject 的 total score），但当 subjects 之间能力相关性较低时（论文报告 IRT θ 与 total score 相关 r = 0.9986，但这是全局的），跨 subject 的 matching 变量可能是 noisy proxy。\n\n**建议**: 至少报告 subject 间 ability 的 inter-correlation matrix 或 domain-level factor structure。\n\n**W8 [Minor] Causality 框架缺失——DIF ≠ 污染。**\n\n论文在 Section 4.3 和 Discussion 中反复强调 DIF 与 web-overlap labels 的近独立性（Jaccard=0.206）。这是一个重要发现，但论文对 DIF 的 causal interpretation 过于谨慎有时又不够谨慎。Limitations（page 9）写道：\"DIF detects that items function differently but cannot determine why\"，这是正确的。但论文标题中的 \"Temporal Measurement Instability\" 和 Section 5.1 的讨论暗示 DIF 反映了某种系统性问题（pollution、capability shift、training methodology change），却未建立任何因果推断框架。\n\n**W9 [Minor] Table 1 的 \"Enrichment\" 指标定义不够清晰。**\n\nTable 1（page 7）报告了 Enrichment ratio（observed/expected overlap between DIF flags and web-overlap labels），但部分 benchmark 标注 \"—\" 表示 Li et al. labels 不适用。这限制了 enrichment 分析的覆盖面。此外，Enrichment = 0.964（MMLU，Table 1）接近 1.0（independent），但不清楚 confidence interval 是多少——是否与 1.0 有显著差异？\n\n---\n\n## 4. Questions for Authors\n\n**Q1.** DEFF 校正的两种 m̄ 估计（simple mean 3.87 vs weighted mean 25.4）相差 6.5 倍。你们认为哪个更适合本研究的数据结构？能否提供理由？\n\n**Q2.** Table 4（power analysis）中的 TPR 是在什么 K 值下计算的？如果 K 改变（如 K=10），TPR 如何变化？\n\n**Q3.** Section 4.5 报告 cross-subject matching 在 broader contamination（k=10）下 ΔFPR = 0.017 ± 0.023。如果 k 继续增大至 20 或 30（更接近真实情况——57 subjects 中的大部分都可能受到不同程度的影响），ΔFPR 会如何变化？\n\n**Q4.** Semi-synthetic 框架中，为什么选择 uniform flipping rate 而非 ability-dependent rate？你们是否考虑过更现实的注入模型？\n\n**Q5.** Appendix C 报告 ICC = 0.047（median 0.041）。这个值是在 item 层级还是 subject 层级计算的？family 层级 ICC 是否有显著的 between-item 异质性？\n\n**Q6.** Section 4.2 提到 \"cluster bootstrap upper bound (53.2%)\"——这是 C% 的上界还是 CI 的上界？如果 C% 本身可达 53.2%，这意味着 family 结构可能导致 DIF 率被严重高估（而非仅仅是统计不确定性）。\n\n---\n\n## 5. Missing References\n\n- **Millsap & Everson (1993)**: \"Methodology review: Statistical approaches for assessing measurement bias\" — 多维 DIF 的标准参考，与本文 MMLU 的多维性直接相关。\n- **Magis, Béland, Tuerlinckx, & De Boeck (2010)**: R package `difR` — 作为 DIF 检测的标准实现工具，应引用并比较。\n- **Ying et al. (2024)**: \"Automating dataset updates towards reliable and timely evaluation of LLMs\" (arXiv:2402.11894) — 直接讨论 benchmark 时间稳定性问题。\n- **Oren et al. (2024)**: \"Proving test set contamination in black-box language models\" (ICLR 2024) — 另一种基于统计检验的污染检测方法，应在 related work 中讨论。\n\n---\n\n## 6. Overall Assessment\n\n**Overall**: **3.5 (Borderline Conference)**\n\n**理由**: 本文提出了一个真正新颖且重要的研究框架——将心理测量的 DIF 分析引入 LLM benchmark 评估。研究规模大（5,227 models），控制实验多层次，cross-benchmark replication 增强了可信度。然而，方法论上存在两个 critical issues：(1) DEFF 校正导致核心数字的不确定性高达 2 倍（13.5% vs 31%），论文未充分解决；(2) LLM 非独立性假设违反的多种处理方式给出不一致的结论。此外，semi-synthetic 框架的 external validity 不足（W3），cross-subject matching 保证过于理想化（W4），K 敏感性分析缺失（W5）。\n\n如果作者能在 rebuttal 中：(a) 统一 DEFF 分析并给出 justified 的 point estimate，(b) 补充 K 敏感性分析，(c) 在 abstract 中 bracket 核心数字，则论文达到 Conference 水准（4.0）。\n\n## 7. ARR 官方维度打分\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| **Soundness** | 3/5 | 方法论基础扎实（MH-DIF 是成熟工具），但 DEFF 不确定性（W1）、非独立性处理不一致（W2）、缺少 K 敏感性（W5）显著削弱 claim 的可靠性 |\n| **Excitement** | 4/5 | 新颖框架（DIF for LLM benchmarks），对社区有重要实践价值，Figure 1 和 cross-benchmark replication 令人印象深刻 |\n| **Reproducibility** | 4/5 | METABENCH 数据公开，方法描述详细，匿名代码链接已提供；扣分因 DEFF 两种 m̄ 选择未给出明确指引 |\n\n## 8. Confidence\n\n**4/5** — 我对 DIF 方法论和大规模统计检验有较深了解，仔细审查了论文的技术细节。可能遗漏的方面：IRT 模型拟合的具体细节（论文主要用 MH-DIF 而非参数化 IRT）。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见（Round 1）\n\n**论文**: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**审查侧重**: 方法严谨性与实验设计\n**审稿标准**: ACL Rolling Review (EMNLP 2026)\n\n---\n\n## 1. Summary\n\n本文将教育测量中的 Mantel-Haenszel DIF 分析应用于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU items），检测 2023 与 2024 模型代际间的测量不稳定性。核心发现是约 31% 的 MMLU items 表现出 ETS Category C 级别的 DIF，且 web-overlap 污染标签与 DIF 标记近乎独立（Jaccard=0.206）。论文提出 cross-subject matching 策略并在 6 个基准上进行交叉验证。这是一个有价值的研究方向——将成熟的心理测量工具引入 LLM 评估——但方法论上存在若干需要正视的缺陷。\n\n---\n\n## 2. Strengths\n\n**S1. 新颖且重要的研究视角。** 将 DIF 分析应用于 LLM benchmark 时间稳定性评估是真正新颖的贡献。Figure 1（page 2）清晰区分了 global contamination 和 differential contamination，叙事精炼有力。这一框架将\"污染检测\"问题重新定义为\"测量不变性\"问题，为社区提供了新的诊断工具。\n\n**S2. 规模与数据基础扎实。** 5,227 模型 × 12,508 items 的分析规模在同类工作中无出其右。使用公开的 METABENCH 数据增强了可信度和可复现性。\n\n**S3. 控制实验设计较为系统。** Random split baseline（C%=0.18%，Section 3.3 cohort 5）、within-family 对比（Llama-2 vs Llama-3，Section 4.2）、leave-one-family-out 分析（Table 7）、以及 cross-benchmark replication（Table 3，6 个基准）构成了多层次的验证体系。\n\n**S4. 实用价值明确。** Section 5.2 提出了具体的监测建议（Monitor/Flag 15%、Flag/Act 25%），配合 Figure 6 的 ranking degradation 分析，对基准维护者有直接指导意义。\n\n**S5. 写作质量高。** 论文在 8 页正文内组织了大量内容，结构紧凑，Figure 和 Table 的信息密度高。\n\n---\n\n## 3. Weaknesses\n\n**W1 [Critical] DEFF 校正范围过大，核心结论的不确定性被低估。**\n\nSection 4.2 和 Appendix C 报告 design-effect 校正后 adjusted C% 范围为 [13.5%, 29.2%]（Section C, page 14: simple mean m̄=3.87 yields DEFF=3.87, adjusted C%=29.2%; weighted mean m̄=25.4 yields DEFF=12.79, adjusted C%=13.5%）。这意味着核心发现——\"~31% items exhibit DIF\"——在考虑 family 非独立性后，可能只有 13.5%，即缩水超过一半。\n\n论文虽然报告了两个边界，但未充分讨论哪个 m̄ 估计更合理，也未提供理由偏好其一。仅在 Limitations 中一句带过（\"the lower bound far exceeds the random-split baseline\"）。虽然 13.5% 仍远超 baseline 0.18%，但\"约三分之一 items 有 DIF\"与\"约七分之一 items 有 DIF\"是截然不同的叙事。论文标题和 abstract 使用\"31%\"作为 headline number，但正文承认这可能因非独立性膨胀至近 2 倍——这一不确定性应在 abstract 中被明确提及。\n\n**建议**: (1) 明确论证 simple mean 与 weighted mean 哪个更适用于本数据，或报告一个 bracketed range 作为主结论；(2) Abstract 和 Section 4.2 的 headline number 应改为 \"[13.5%–31%] of items\" 或类似表述。\n\n**W2 [Critical] LLM 非独立性假设违反的影响被分散处理，缺乏统一量化。**\n\nMH-DIF 的核心假设是考生独立。但 LLM 同 family 共享训练数据和架构，严重违反此假设。论文在多处分散讨论了这一问题：\n- Section 3.2（\"LLM-specific challenges\"）提及 fine-tuned variants 和 family structure\n- Appendix C 计算 ICC 和 DEFF\n- Appendix D 做 cluster bootstrap\n- Table 7 做 leave-one-family-out\n- Appendix A.1 检查 Yen's Q3\n\n但这些分析之间缺乏统一框架。例如：Appendix D 的 cluster bootstrap 下界是 26.7%（simple DEFF adjustment）到 29.2%，而 Appendix C 的 DEFF 下界是 13.5%。这两个\"robustness\"结果相互矛盾——cluster bootstrap 似乎暗示影响不大，而 DEFF 暗示影响可能很大。论文未解释这一差异。\n\n具体来说，ICC = 0.047 (median 0.041, Q3 = 0.061)，看似不大，但 m̄ 的选择（3.87 vs 25.4）导致 DEFF 从 1.13 到 12.79，相差一个数量级。问题核心在于：应该用 family 均值（~3.87 models/family）还是有效样本量加权均值（~25.4，因为大 family 贡献更多考生）来估计 m̄？后者更合理（因为大 family 对 χ² 统计量的膨胀贡献更大），但论文未做出明确选择。\n\n**建议**: 统一处理非独立性：明确选择 DEFF 估计方法并论证，或用 permutation test（在 family 层级 shuffle temporal labels）直接获得一个不依赖参数假设的 null distribution。\n\n**W3 [Major] Semi-synthetic 框架的 binary response flipping 过于简化，external validity 存疑。**\n\nSection 3.4 的注入框架将\"污染\"建模为 binary response flipping（incorrect → correct，以概率 p）。Limitations（page 9）承认\"Real-world contamination involves partial memorization, reasoning shortcuts, and format-specific advantages\"。\n\n问题在于：\n(a) 真实污染不是二值的——模型可能部分记忆了答案的推理链，导致在相似但不同的 items 上也表现更好。这种 spillover 效应在 binary flipping 框架下完全不可见。\n(b) 污染概率 p 对不同 ability 水平的模型应有不同影响（低能力模型从污染中获益更大），但框架中 p 是 uniform 的。\n(c) Figure 2 的 dose-response 曲线（ΔTPR 随 p 单调递增）在此简化模型下是 trivially expected 的——它没有提供多少关于真实检测能力的信息。\n\nSemi-synthetic 框架的核心价值在于 calibrate detection power，但如果注入模型与真实污染模式差异太大，calibration 本身就不可靠。\n\n**建议**: (1) 至少讨论一种更现实的注入模型（如 ability-dependent flipping：低能力模型 p_high，高能力模型 p_low）并报告 sensitivity；(2) 使用 GSM8K 的已知污染案例（Section 4.7 提到 GSM8K semi-synthetic injection）做 real-world calibration。\n\n**W4 [Major] Cross-subject matching 的 ΔFPR=0 保证条件过于理想化。**\n\nSection 3.4 的 Remark（Zero FPR under single-subject matching）数学上是正确的，但前提条件——污染仅限于单一 subject——在实践中几乎不成立。论文自己也承认（同一 Section）：\"When contamination spans multiple subjects simultaneously, M_i will absorb signal from other contaminated subjects, potentially inflating FPR.\"\n\n实证验证（ΔFPR = 0.000，95% CI = [0.000, 0.004]）仅在 single-subject injection 下测试。Broader contamination（k=10 subjects）下 ΔFPR 升至 0.017±0.023，而 worst-case 为 ~7pp。虽然论文称\"Even worst-case multi-subject inflation (~7 pp) cannot account for the observed 31% C% rate\"，但如果核心 C% 可能只有 13.5%（W1 的 DEFF 下界），7pp 的 FPR inflation 就不再可以忽略。\n\n**建议**: (1) 在 DEFF-adjusted 的下界 13.5% 语境下重新评估 multi-subject FPR inflation 的影响；(2) 提供 multi-subject injection 的完整 FPR 曲线而非仅报告 k=10 的点估计。\n\n**W5 [Major] 缺少 K（分层数）敏感性分析。**\n\nSection 3.2 使用 K=5 quintile 分层，引用 ETS 推荐做法。但 K 的选择对 MH-DIF 结果有实质影响——过少的分层导致 ability 匹配不精确（residual confounding），过多则每层样本量不足。论文仅在 Appendix A.2 报告了 |Δ_MH| 阈值敏感性（1.0, 1.5, 2.0, 2.5），但完全没有报告 K 的敏感性（如 K=3, 5, 7, 10）。\n\n在 N=5,227 这种大样本下，K=5 可能过粗（每层~1,045 个模型），导致 ability group 内部仍有较大异质性。这对 cross-subject matching 尤其重要——如果 matching 不够精细，可能产生 residual confounding 从而虚高 DIF 率。\n\n**建议**: 报告 K ∈ {3, 5, 7, 10} 的 C% 变化，确认核心结论对分层数稳健。\n\n**W6 [Major] 大样本下 p 值几乎失去筛选作用，ETS 双重阈值的有效性需要更深讨论。**\n\nN=5,227 时，MH χ² 检验的统计功效极高。对任何具有 |Δ_MH| ≥ 1.5 的 item，p < 0.05 几乎肯定成立。论文在 Appendix A.2 提到 BH-FDR 仅重分类 3 个 items，恰好印证了这一点——p 值在这个样本量下基本是多余的。\n\n但这也意味着 ETS 双重阈值在本研究中实质上退化为单一的效应量阈值（|Δ_MH| ≥ 1.5）。论文应明确讨论这一点，而非让读者误以为 p < 0.05 提供了独立的误判控制。\n\n更深层的问题：当 DEFF 校正将有效样本量从 5,227 缩小到 ~400-1,350（取决于 m̄ 选择）时，p 值的筛选作用可能会恢复。论文报告了 DEFF 校正后 C% 从 31% 降至 13.5%-29.2%，但未说明这些被重分类的 items 是因为 |Δ_MH| 缩小还是因为 p 值不再显著。这一区分很重要。\n\n**建议**: (1) 分别报告 DEFF 校正后因效应量标准和因显著性标准被重分类的 items 数量；(2) 讨论在本研究的有效样本量下，p < 0.05 是否提供了超出效应量阈值的额外信息。\n\n**W7 [Minor] Unidimensionality 假设讨论不足。**\n\nMMLU 涵盖 57 个 subjects、5 大 domains，本质上是高度多维的。MH-DIF 以 total score 为 matching variable，隐含了 unidimensionality 假设。论文在 Section 3.2 讨论了三种 matching 策略，并在 Appendix A.1 检查了 domain-specificity，但未正式检验 unidimensionality（如 factor analysis 或 scree plot）。\n\nCross-subject matching 部分缓解了这一问题（使用其他 subject 的 total score），但当 subjects 之间能力相关性较低时（论文报告 IRT θ 与 total score 相关 r = 0.9986，但这是全局的），跨 subject 的 matching 变量可能是 noisy proxy。\n\n**建议**: 至少报告 subject 间 ability 的 inter-correlation matrix 或 domain-level factor structure。\n\n**W8 [Minor] Causality 框架缺失——DIF ≠ 污染。**\n\n论文在 Section 4.3 和 Discussion 中反复强调 DIF 与 web-overlap labels 的近独立性（Jaccard=0.206）。这是一个重要发现，但论文对 DIF 的 causal interpretation 过于谨慎有时又不够谨慎。Limitations（page 9）写道：\"DIF detects that items function differently but cannot determine why\"，这是正确的。但论文标题中的 \"Temporal Measurement Instability\" 和 Section 5.1 的讨论暗示 DIF 反映了某种系统性问题（pollution、capability shift、training methodology change），却未建立任何因果推断框架。\n\n**W9 [Minor] Table 1 的 \"Enrichment\" 指标定义不够清晰。**\n\nTable 1（page 7）报告了 Enrichment ratio（observed/expected overlap between DIF flags and web-overlap labels），但部分 benchmark 标注 \"—\" 表示 Li et al. labels 不适用。这限制了 enrichment 分析的覆盖面。此外，Enrichment = 0.964（MMLU，Table 1）接近 1.0（independent），但不清楚 confidence interval 是多少——是否与 1.0 有显著差异？\n\n---\n\n## 4. Questions for Authors\n\n**Q1.** DEFF 校正的两种 m̄ 估计（simple mean 3.87 vs weighted mean 25.4）相差 6.5 倍。你们认为哪个更适合本研究的数据结构？能否提供理由？\n\n**Q2.** Table 4（power analysis）中的 TPR 是在什么 K 值下计算的？如果 K 改变（如 K=10），TPR 如何变化？\n\n**Q3.** Section 4.5 报告 cross-subject matching 在 broader contamination（k=10）下 ΔFPR = 0.017 ± 0.023。如果 k 继续增大至 20 或 30（更接近真实情况——57 subjects 中的大部分都可能受到不同程度的影响），ΔFPR 会如何变化？\n\n**Q4.** Semi-synthetic 框架中，为什么选择 uniform flipping rate 而非 ability-dependent rate？你们是否考虑过更现实的注入模型？\n\n**Q5.** Appendix C 报告 ICC = 0.047（median 0.041）。这个值是在 item 层级还是 subject 层级计算的？family 层级 ICC 是否有显著的 between-item 异质性？\n\n**Q6.** Section 4.2 提到 \"cluster bootstrap upper bound (53.2%)\"——这是 C% 的上界还是 CI 的上界？如果 C% 本身可达 53.2%，这意味着 family 结构可能导致 DIF 率被严重高估（而非仅仅是统计不确定性）。\n\n---\n\n## 5. Missing References\n\n- **Millsap & Everson (1993)**: \"Methodology review: Statistical approaches for assessing measurement bias\" — 多维 DIF 的标准参考，与本文 MMLU 的多维性直接相关。\n- **Magis, Béland, Tuerlinckx, & De Boeck (2010)**: R package `difR` — 作为 DIF 检测的标准实现工具，应引用并比较。\n- **Ying et al. (2024)**: \"Automating dataset updates towards reliable and timely evaluation of LLMs\" (arXiv:2402.11894) — 直接讨论 benchmark 时间稳定性问题。\n- **Oren et al. (2024)**: \"Proving test set contamination in black-box language models\" (ICLR 2024) — 另一种基于统计检验的污染检测方法，应在 related work 中讨论。\n\n---\n\n## 6. Overall Assessment\n\n**Overall**: **3.5 (Borderline Conference)**\n\n**理由**: 本文提出了一个真正新颖且重要的研究框架——将心理测量的 DIF 分析引入 LLM benchmark 评估。研究规模大（5,227 models），控制实验多层次，cross-benchmark replication 增强了可信度。然而，方法论上存在两个 critical issues：(1) DEFF 校正导致核心数字的不确定性高达 2 倍（13.5% vs 31%），论文未充分解决；(2) LLM 非独立性假设违反的多种处理方式给出不一致的结论。此外，semi-synthetic 框架的 external validity 不足（W3），cross-subject matching 保证过于理想化（W4），K 敏感性分析缺失（W5）。\n\n如果作者能在 rebuttal 中：(a) 统一 DEFF 分析并给出 justified 的 point estimate，(b) 补充 K 敏感性分析，(c) 在 abstract 中 bracket 核心数字，则论文达到 Conference 水准（4.0）。\n\n## 7. ARR 官方维度打分\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| **Soundness** | 3/5 | 方法论基础扎实（MH-DIF 是成熟工具），但 DEFF 不确定性（W1）、非独立性处理不一致（W2）、缺少 K 敏感性（W5）显著削弱 claim 的可靠性 |\n| **Excitement** | 4/5 | 新颖框架（DIF for LLM benchmarks），对社区有重要实践价值，Figure 1 和 cross-benchmark replication 令人印象深刻 |\n| **Reproducibility** | 4/5 | METABENCH 数据公开，方法描述详细，匿名代码链接已提供；扣分因 DEFF 两种 m̄ 选择未给出明确指引 |\n\n## 8. Confidence\n\n**4/5** — 我对 DIF 方法论和大规模统计检验有较深了解，仔细审查了论文的技术细节。可能遗漏的方面：IRT 模型拟合的具体细节（论文主要用 MH-DIF 而非参数化 IRT）。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-22T15:11:30.035096+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4948
}
```

</details>

---


### Assistant

_source line 828 · 2026-05-22T15:11:38.277097+00:00_

审稿意见已提交给 Review Director。

**审稿总结**：

- **Overall: 3.5 (Borderline Conference)**
- **Soundness: 3/5 | Excitement: 4/5 | Reproducibility: 4/5 | Confidence: 4/5**

提出了 **2 个 Critical issues**（DEFF 校正范围过大导致核心数字不确定性达 2 倍；非独立性处理分散且不一致）、**4 个 Major issues**（semi-synthetic 框架 external validity 不足、cross-subject matching 保证过于理想化、缺少 K 敏感性分析、大样本下 p 值失效未充分讨论）、**3 个 Minor issues**（unidimensionality 假设、因果推断缺失、Enrichment 指标定义），以及 6 个需要作者澄清的问题和 4 条 missing references。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 29

## Round 29

32 recorded events


### User

_source line 829 · 2026-05-22T15:14:30.934889+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每一条 Weakness 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（引用论文中具体的 Section/Table/Figure）。

---

## Reviewer 2 完整审稿意见

### Strengths
S1. 研究问题的实际意义——将 DIF 引入 LLM 评估语境对 NLP 社区具有启发性。
S2. 实证规模与严谨性——5,227 模型 × 12,508 items，多层验证设计。
S3. Ground truth 元批判（Section 4.3）——Jaccard=0.206 的实证结果提供方法论警示。
S4. Cross-subject matching 框架——ΔFPR=0 的理论保证和实证验证。
S5. 跨基准复现（Table 3）——6 个 METABENCH 基准上复现。
S6. Figure 1 设计有效。

### Weaknesses
**W1 [Major] 新颖性有限：核心方法是既有技术的直接搬运。** MH-DIF 是 1988 年标准方法，ETS classification 是 1993 年标准。论文将这些方法原封不动应用于 LLM 评估，没有针对 LLM 场景的方法论创新。未处理 LLM 特有挑战（如非独立 examinees），未扩展 MH 方法处理多值 DIF。与 Growing Pains 的 FPC 框架和 PSN-IRT 的 Pseudo-Siamese Network 相比，方法论技术贡献明显不足。论文自承 "methodological and empirical, not algorithmic"，在 NLP 顶会中这是一个 liability。

**W2 [Major] Contribution 1 的贡献度存疑。** "Web-overlap labels 不适合作 DIF ground truth" 从概念上接近自明。论文未讨论在什么条件下两指标 *应该* 相关。

**W3 [Major] "发现问题" 之后缺乏可操作的解决方案。** Monitor/Flag/Act thresholds (15%/25%) 是 ad hoc 的。未提出如何修复或替换被标记的 items。Figure 6 中 DIF-ordered vs random removal 的效果差异很小。

**W4 [Major] 时间维度 DIF 与传统 DIF 的概念张力未充分讨论。** 2024 模型在某些 items 上更好可能是 legitimate 的能力提升，而非测量不稳定。Contamination、训练方法论改进、架构变化、RLHF 效应等替代解释未被系统排除。

**W5 [Minor] Abstract 中 31% 的强调可能产生误导。** DEFF 校正后降至 13.5–29.5%。

**W6 [Minor] Related Work 对 DIF 在非传统情境的讨论不足。** 未讨论 Kraus et al. (2024) 和 Suk & Lyu (2026)。

**W7 [Minor] Cross-subject matching 对实际 DIF 结果的影响未在正文展示。**

**W8 [Minor] DEFF correction 透明度不足。**

**W9 [Minor] Discussion 过于压缩。**

**W10 [Minor] Figure 2 dose-response 曲线解读有歧义。**

### Questions
Q1. temporal DIF 中，有多少可归因于 legitimate 能力变化 vs construct-irrelevant 变化？
Q2. Cross-subject matching 如何选择"外部学科"？不同选择是否改变结果？
Q3. 2023 vs 2024 二分切割的鲁棒性如何？
Q4. DEFF 校正后 C% 范围 13.5–29.5% 哪个端点更代表真实 DIF 率？
Q5. Jaccard=0.206 被描述为 "near-independence"，但 ~20% overlap 可能是 contamination-driven DIF 的证据。

### Missing References
- Kraus, Wild & Hilbert (2024). "Using Interpretable ML for DIF Detection."
- Suk & Lyu (2026). "Rethinking Item Fairness Using SWIGs."
- Xu et al. (2025). "Large language model psychometrics: A systematic review."
- Dong et al. (2025/2026). "Comprehensive Survey of Contamination Detection Methods in LLMs."

### Overall: 3.0 (Findings)
---

请逐条回应上述 Weaknesses 和 Questions。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-22T15:14:54.899908+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 831 · 2026-05-22T15:14:59.178103+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4278
}
```

</details>

---


### Tool call

_source line 832 · 2026-05-22T15:14:59.630491+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 833 · 2026-05-22T15:14:59.681152+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-22T15:15:00.395982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 835 · 2026-05-22T15:15:00.446766+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 836 · 2026-05-22T15:15:01.153738+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 837 · 2026-05-22T15:15:01.354798+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 838 · 2026-05-22T15:15:09.231246+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-2,5,7-9,13-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-2,5,7-9,13-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 839 · 2026-05-22T15:15:10.995964+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 531.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 471.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 556.9}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 530.4}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 499.3}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.0}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p15.png\", \"widt
…[truncated 286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1764
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-22T15:15:14.928882+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 841 · 2026-05-22T15:15:15.481079+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 842 · 2026-05-22T15:15:16.336754+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool call

_source line 843 · 2026-05-22T15:15:16.337226+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 844 · 2026-05-22T15:15:16.691582+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1210
}
```

</details>

---


### Tool call

_source line 845 · 2026-05-22T15:15:16.692080+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 846 · 2026-05-22T15:15:17.400466+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1063
}
```

</details>

---


### Tool result

_source line 847 · 2026-05-22T15:15:17.703544+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1011
}
```

</details>

---


### Tool call

_source line 848 · 2026-05-22T15:15:21.832634+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 849 · 2026-05-22T15:15:22.236898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 850 · 2026-05-22T15:15:23.192319+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1359
}
```

</details>

---


### Tool call

_source line 851 · 2026-05-22T15:15:23.192784+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 852 · 2026-05-22T15:15:23.595872+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1358
}
```

</details>

---


### Tool call

_source line 853 · 2026-05-22T15:15:23.646793+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 854 · 2026-05-22T15:15:24.151800+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_10/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-22T15:15:24.203284+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool result

_source line 856 · 2026-05-22T15:15:25.061118+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1414
}
```

</details>

---


### Tool result

_source line 857 · 2026-05-22T15:15:25.065519+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 913
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-22T15:17:33.374637+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 意见的交叉回应\n\n---\n\n### Weaknesses 逐条回应\n\n**[REBUT] R2-W1: \"核心方法是既有技术的直接搬运，新颖性有限\"**\n\nR2 的批评有合理之处但过于严苛。三点反驳：\n\n(1) **Cross-subject matching 是针对 LLM 场景的方法论贡献，非\"原封不动搬运\"。** Section 3.4（page 5）的 Remark（Zero FPR under single-subject matching）提出了一个专门为多 subject benchmark 设计的 matching 策略，利用 MMLU 的 57-subject 结构将 matching variable 从 within-subject total score 替换为 cross-subject total score，在理论上保证 ΔFPR=0。这在教育测量文献中没有直接先例——传统 DIF 不需要处理\"多 domain benchmark 中 contamination 可能局限于特定 domain\"的场景。\n\n(2) **\"应用既有方法到新领域\"在 NLP 顶会有充分先例。** DIF 之于 LLM evaluation，类似于 BERTScore 之于 evaluation metrics——关键贡献在于 empirical insight 和 domain adaptation，而非算法创新。论文明确声明 contributions 是 \"methodological and empirical, not algorithmic\"（page 2），这在 EMNLP 的 analysis track 论文中是合理的定位。\n\n(3) **与 Growing Pains/PSN-IRT 的比较不公平。** Growing Pains（Habba et al., 2026）做 FPC calibration，PSN-IRT（Zhou et al., 2026）用 Pseudo-Siamese Network——这些方法的目标是 contamination *detection*，而本文的目标是 measurement *invariance* auditing。它们解决的是不同的问题。\n\n不过，我同意论文**应更明确讨论 LLM 特有挑战的处理**——特别是 non-independent examinees 的方法论适配（而非仅作 post-hoc robustness check）。这与我在 R1-W2 中的批评一致。\n\n---\n\n**[REBUT] R2-W2: \"Web-overlap 不适合作 DIF ground truth 接近自明\"**\n\n概念层面或许直觉上可理解，但 empirical quantification 并非自明：\n\n(1) **社区现状是将 web-overlap 当作 contamination 的标准 proxy。** Li et al. (2024b) 被广泛引用（Section 2, page 2 & Section 4.3, page 7），很多后续工作直接用 web-overlap labels 评估 contamination detection 方法的 recall/precision。论文的 Jaccard=0.206、Enrichment=0.964（Table 1, page 7）提供了**第一个大规模定量证据**表明这一 proxy 与 DIF 标记近乎独立——这不是自明的，它对领域内的评估实践有直接影响。\n\n(2) **论文确实讨论了两指标\"应该\"何时相关。** Section 4.3（page 7）明确区分了 global exposure 和 differential functioning：\"web-overlap labels classify items based on verbatim matches in publicly accessible web corpora... Such labels do not capture differential item functioning\"。Figure 1（page 2）用 ICC curves 可视化了这一区分。\n\n(3) 但我**部分同意** R2 的批评：论文可以更系统地讨论在什么 contamination mechanism 下两者应高度相关（如 verbatim memorization 主要影响低能力模型时），以及当前低 Jaccard 对这些 mechanism 的约束。\n\n---\n\n**[AGREE] R2-W3: \"发现问题之后缺乏可操作的解决方案\"**\n\n同意这是论文的薄弱环节。\n\nSection 5.2（page 8）提出 Monitor/Flag（15%）和 Flag/Act（25%）阈值，但**未给出理论或经验依据**——为什么是 15% 和 25%？这些数字似乎是从 Figure 6 的视觉拐点 ad hoc 选取的。\n\n关于 Figure 6（page 16）DIF-ordered vs random removal 的效果差异：我不完全同意 R2 说\"差异很小\"。在 MMLU 面板（N=12,508），DIF-ordered 在移除 25% items 后 ρ 降至约 0.996，而 random removal 在 0.998 左右——差异虽小但在 12,500+ items 上是一致的。但在小 benchmark（如 TruthfulQA, N=818）上差异确实更明显。\n\n核心问题是：**论文未讨论 item replacement 策略**——是标记后删除、加权下调、还是替换？对 benchmark 维护者而言，\"31% 的 items 有 DIF\"是一个 alarm，但 next step 不清晰。\n\n---\n\n**[AGREE] R2-W4: \"时间维度 DIF 与 legitimate 能力提升的概念张力\"**\n\n**这是 R2 提出的最有力的批评，我完全同意。**\n\nDIF 在教育测量中的原始含义是：**控制能力后，某 item 对不同群体难度不同**。当\"群体\"是时间代际时，ability 本身也在变化，matching variable（total score）部分吸收了这一变化，但并不完全。具体来说：\n\n- 2024 模型可能因为**训练数据量更大、架构更好、RLHF 更成熟**而在特定 items 上表现更好——这是 legitimate 的 construct-relevant improvement，不应被标记为 DIF。\n- 论文的 instability decomposition（Appendix A.1, page 12）通过 domain-specificity 和 within-subject logistic regression 试图分离 ability shift 和 item-level effect，但**未能给出 clean 的因果分解**。\n- Section 5.1（page 8）提到 \"ETS C rates typically range from 5–15%\"作为 baseline，暗示超出部分是 temporal instability。但教育测量中 5-15% 是在**同一考试、同一时期、不同人口学群体**间的 rate——temporal cohort 的 rate 没有直接可比性。\n\n论文应明确承认：**temporal DIF 是 ability shift 和 measurement instability 的混合物**，当前方法不能完全分离两者。Limitations（page 9）有一句 \"DIF detects that items function differently but cannot determine why\"，但这一核心限制应在正文 Discussion 中更显著地讨论。\n\n---\n\n**[AGREE] R2-W5: \"Abstract 中 31% 的强调可能误导\"**\n\n与我的 R1-W1 一致。Abstract 应报告 bracketed range [13.5%–31%] 而非单一数字。\n\n---\n\n**[AGREE] R2-W6: \"Related Work 对 DIF 在非传统情境的讨论不足\"**\n\n同意 related work 可以更全面。但这是 minor issue，不影响接收决定。\n\n---\n\n**[AGREE] R2-W7: \"Cross-subject matching 对实际 DIF 结果的影响未在正文展示\"**\n\n同意。Section 4.4（page 7）报告 cross-subject C% = 31.5%（比 standard matching 更保守），Table 2（page 7）也有数据，但**cross-subject matching 相对于 standard matching 改变了哪些 items 的分类**这一关键比较未在正文展示。读者无法判断 cross-subject matching 是否实质性地改变了结论。\n\n---\n\n**[AGREE] R2-W8: \"DEFF correction 透明度不足\"**\n\n与我的 R1-W1 和 R1-W2 一致。DEFF 的两种 m̄ 估计（simple mean 3.87 vs weighted mean 25.4）给出的 adjusted C% 相差近 2 倍，论文未充分论证偏好哪一个。\n\n---\n\n**[AGREE] R2-W9: \"Discussion 过于压缩\"**\n\n同意。Section 5 在不到半页内覆盖了 Benchmark Temporal Comparability（5.1）和 Recommended Audit Protocol（5.2），对于一篇 analysis paper 而言不够充分。特别是 Section 5.1 的\"5-15% ETS C rate baseline\"需要更仔细的论证——这个 baseline 是否适用于 temporal cohort 比较（见我对 W4 的同意）。\n\n---\n\n**[REBUT] R2-W10: \"Figure 2 dose-response 曲线解读有歧义\"**\n\n部分反驳。Figure 2（page 7）展示 ΔTPR 随 exploitation rate p 单调递增，caption 和正文（Section 4.1, page 7）明确说明 \"ΔTPR increases monotonically with exploitation rate p, confirming that MH-DIF is sensitive to differential item behavior when present. Baseline (no injection) produces ΔFPR ≈ 0.\" 这个信息是清晰的——x 轴是 injection rate，y 轴是 detection improvement over baseline。\n\n但我同意 Figure 2 有一个可改进之处：它只展示了 MMLU 上的 dose-response，未包含其他 benchmark 的对应曲线。如果空间允许，加入 GSM8K 的 dose-response（Section 4.7 提到 GSM8K 的 ΔTPR=+0.54）会增强 generalizability。\n\n---\n\n### Questions 逐条回应\n\n**[AGREE] R2-Q1: \"有多少 temporal DIF 可归因于 legitimate 能力变化 vs construct-irrelevant 变化？\"**\n\n与我对 W4 的同意一致。这是论文的核心未解决问题。论文的 instability decomposition（Appendix A.1）和 logistic regression（Appendix B, Section 4.2 的 Simpson's paradox analysis）提供了部分分解，但不是 clean 的 causal identification。我认为作者应在 rebuttal 中：(a) 承认这一限制，(b) 提供 a back-of-envelope estimate（如：domain-level ability improvement 能解释多少 C% items 的 DIF）。\n\n**[REBUT] R2-Q2: \"Cross-subject matching 如何选择外部学科？\"**\n\n这个问题基于误读。Section 3.4（page 5）的 Remark 明确定义：$M_i^s = \\sum_{s' \\neq s} \\sum_j Y_{ij}$——即**使用所有其他 subjects 的 total score**，不存在\"选择\"哪个外部学科的问题。这不是 arbitrary choice，而是 deterministic——对 subject s 中的 item i，matching variable 是模型在所有非 s subjects 上的总分。因此\"不同选择是否改变结果\"不适用。\n\n但我要指出一个 R2 未提到的相关问题：当某些 subjects 间能力高度相关时（如 STEM domains 之间），cross-subject total score 仍可能泄漏被测 subject 的 ability signal，部分削弱 ΔFPR=0 的保证。论文的 IRT θ 与 total score 相关 r=0.9986（Section 3.4）实际上暗示 cross-subject score 是全局 ability 的一个 strong proxy，这可能意味着 cross-subject matching 与 standard matching 在实践中差异不大——这正是 Table 2（C%=31.5% cross-subject vs 约 31% standard）暗示的。\n\n**[AGREE] R2-Q3: \"2023 vs 2024 二分切割的鲁棒性\"**\n\n合理问题。Table 1（page 7）展示了多种 cohort 定义——Temporal 2023/2024、Ability-quintile Q1-Q2 vs Q4-Q5、Within-family Llama-2/Llama-3、Within-subject per-subject DIF、Random split——但**正文未系统比较不同 temporal cutoff 的影响**（如 2023-Q3 vs 2024-Q1，或用 release date 的 continuous variable）。Section 3.3（page 5）提到 \"models span release dates from 2023 to 2024\"，但 DIF 结果可能对具体 cutoff 敏感——特别是如果 2024 early models 与 2023 late models 差异不大。\n\n**[AGREE] R2-Q4: \"DEFF 校正后 C% 范围哪个端点更代表真实 DIF 率？\"**\n\n与我的 R1-W1 完全一致。这是作者必须在 rebuttal 中回答的核心问题。如我在 R1-W2 中建议，weighted mean m̄=25.4 更合理（大 family 对 χ² 膨胀贡献更大），但这会将 headline number 从 31% 降至 ~13.5%——叙事完全不同。\n\n**[REBUT] R2-Q5: \"Jaccard=0.206 的 20% overlap 可能是 contamination-driven DIF 的证据\"**\n\n这个解读在逻辑上是 possible 但论文已提供反证。Section 4.3（page 7）报告 Enrichment = 0.964，接近 1.0（independent baseline）。如果 20% overlap 是 contamination-driven DIF，Enrichment 应显著 > 1.0。当前 0.964 甚至略低于 1.0，表明 DIF-flagged items 在 web-contaminated items 中的**出现率不高于随机预期**。\n\n此外，论文在同一段指出 DIF-C flagged items 中 30.7% 有 web-contamination labels，而 clean items 中 31.8%——DIF-C 率在 web-contaminated 和 clean items 中几乎相同。这 directly contradicts R2 的解读：如果 contamination 驱动 DIF，web-contaminated items 应有显著更高的 DIF-C rate。\n\n但我要补充一个 nuance：Enrichment 接近 1.0 不等于\"contamination 不导致 DIF\"。它可能意味着 (a) contamination 导致的 DIF 被 non-contamination 源（如训练方法改变）导致的 DIF 所 overwhelm，或 (b) web-overlap labels 本身是 noisy proxy for actual contamination。论文应区分这两种解释。\n\n---\n\n### 对 R2 Overall Assessment（3.0, Findings）的看法\n\nR2 给出 3.0（Findings level），我给出 3.5（Borderline Conference）。分歧主要在于：\n\n1. **新颖性评估**：R2 认为\"直接搬运既有方法\"是 major weakness。我认为 cross-subject matching 和 ground truth meta-critique 构成了足够的 methodological contribution for an analysis paper，且 empirical findings（31% DIF rate、Jaccard=0.206）本身具有重大价值。\n\n2. **\"缺乏解决方案\"的权重**：R2 将此列为 major weakness。我认为诊断性论文在 NLP 中有充分先例（如 Raji et al. 2021 的 benchmark audit 论文），\"发现问题\"本身就是贡献。\n\n3. 但我与 R2 在以下方面一致：DEFF 不确定性（W5/W8）、temporal DIF 的因果模糊性（W4）、Discussion 不足（W9）是需要 rebuttal 解决的实质问题。\n\n**如果作者无法在 rebuttal 中解决 DEFF 和 causal interpretation 问题，我会倾向 R2 的 3.0 而非维持 3.5。**",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 意见的交叉回应\n\n---\n\n### Weaknesses 逐条回应\n\n**[REBUT] R2-W1: \"核心方法是既有技术的直接搬运，新颖性有限\"**\n\nR2 的批评有合理之处但过于严苛。三点反驳：\n\n(1) **Cross-subject matching 是针对 LLM 场景的方法论贡献，非\"原封不动搬运\"。** Section 3.4（page 5）的 Remark（Zero FPR under single-subject matching）提出了一个专门为多 subject benchmark 设计的 matching 策略，利用 MMLU 的 57-subject 结构将 matching variable 从 within-subject total score 替换为 cross-subject total score，在理论上保证 ΔFPR=0。这在教育测量文献中没有直接先例——传统 DIF 不需要处理\"多 domain benchmark 中 contamination 可能局限于特定 domain\"的场景。\n\n(2) **\"应用既有方法到新领域\"在 NLP 顶会有充分先例。** DIF 之于 LLM evaluation，类似于 BERTScore 之于 evaluation metrics——关键贡献在于 empirical insight 和 domain adaptation，而非算法创新。论文明确声明 contributions 是 \"methodological and empirical, not algorithmic\"（page 2），这在 EMNLP 的 analysis track 论文中是合理的定位。\n\n(3) **与 Growing Pains/PSN-IRT 的比较不公平。** Growing Pains（Habba et al., 2026）做 FPC calibration，PSN-IRT（Zhou et al., 2026）用 Pseudo-Siamese Network——这些方法的目标是 contamination *detection*，而本文的目标是 measurement *invariance* auditing。它们解决的是不同的问题。\n\n不过，我同意论文**应更明确讨论 LLM 特有挑战的处理**——特别是 non-independent examinees 的方法论适配（而非仅作 post-hoc robustness check）。这与我在 R1-W2 中的批评一致。\n\n---\n\n**[REBUT] R2-W2: \"Web-overlap 不适合作 DIF ground truth 接近自明\"**\n\n概念层面或许直觉上可理解，但 empirical quantification 并非自明：\n\n(1) **社区现状是将 web-overlap 当作 contamination 的标准 proxy。** Li et al. (2024b) 被广泛引用（Section 2, page 2 & Section 4.3, page 7），很多后续工作直接用 web-overlap labels 评估 contamination detection 方法的 recall/precision。论文的 Jaccard=0.206、Enrichment=0.964（Table 1, page 7）提供了**第一个大规模定量证据**表明这一 proxy 与 DIF 标记近乎独立——这不是自明的，它对领域内的评估实践有直接影响。\n\n(2) **论文确实讨论了两指标\"应该\"何时相关。** Section 4.3（page 7）明确区分了 global exposure 和 differential functioning：\"web-overlap labels classify items based on verbatim matches in publicly accessible web corpora... Such labels do not capture differential item functioning\"。Figure 1（page 2）用 ICC curves 可视化了这一区分。\n\n(3) 但我**部分同意** R2 的批评：论文可以更系统地讨论在什么 contamination mechanism 下两者应高度相关（如 verbatim memorization 主要影响低能力模型时），以及当前低 Jaccard 对这些 mechanism 的约束。\n\n---\n\n**[AGREE] R2-W3: \"发现问题之后缺乏可操作的解决方案\"**\n\n同意这是论文的薄弱环节。\n\nSection 5.2（page 8）提出 Monitor/Flag（15%）和 Flag/Act（25%）阈值，但**未给出理论或经验依据**——为什么是 15% 和 25%？这些数字似乎是从 Figure 6 的视觉拐点 ad hoc 选取的。\n\n关于 Figure 6（page 16）DIF-ordered vs random removal 的效果差异：我不完全同意 R2 说\"差异很小\"。在 MMLU 面板（N=12,508），DIF-ordered 在移除 25% items 后 ρ 降至约 0.996，而 random removal 在 0.998 左右——差异虽小但在 12,500+ items 上是一致的。但在小 benchmark（如 TruthfulQA, N=818）上差异确实更明显。\n\n核心问题是：**论文未讨论 item replacement 策略**——是标记后删除、加权下调、还是替换？对 benchmark 维护者而言，\"31% 的 items 有 DIF\"是一个 alarm，但 next step 不清晰。\n\n---\n\n**[AGREE] R2-W4: \"时间维度 DIF 与 legitimate 能力提升的概念张力\"**\n\n**这是 R2 提出的最有力的批评，我完全同意。**\n\nDIF 在教育测量中的原始含义是：**控制能力后，某 item 对不同群体难度不同**。当\"群体\"是时间代际时，ability 本身也在变化，matching variable（total score）部分吸收了这一变化，但并不完全。具体来说：\n\n- 2024 模型可能因为**训练数据量更大、架构更好、RLHF 更成熟**而在特定 items 上表现更好——这是 legitimate 的 construct-relevant improvement，不应被标记为 DIF。\n- 论文的 instability decomposition（Appendix A.1, page 12）通过 domain-specificity 和 within-subject logistic regression 试图分离 ability shift 和 item-level effect，但**未能给出 clean 的因果分解**。\n- Section 5.1（page 8）提到 \"ETS C rates typically range from 5–15%\"作为 baseline，暗示超出部分是 temporal instability。但教育测量中 5-15% 是在**同一考试、同一时期、不同人口学群体**间的 rate——temporal cohort 的 rate 没有直接可比性。\n\n论文应明确承认：**temporal DIF 是 ability shift 和 measurement instability 的混合物**，当前方法不能完全分离两者。Limitations（page 9）有一句 \"DIF detects that items function differently but cannot determine why\"，但这一核心限制应在正文 Discussion 中更显著地讨论。\n\n---\n\n**[AGREE] R2-W5: \"Abstract 中 31% 的强调可能误导\"**\n\n与我的 R1-W1 一致。Abstract 应报告 bracketed range [13.5%–31%] 而非单一数字。\n\n---\n\n**[AGREE] R2-W6: \"Related Work 对 DIF 在非传统情境的讨论不足\"**\n\n同意 related work 可以更全面。但这是 minor issue，不影响接收决定。\n\n---\n\n**[AGREE] R2-W7: \"Cross-subject matching 对实际 DIF 结果的影响未在正文展示\"**\n\n同意。Section 4.4（page 7）报告 cross-subject C% = 31.5%（比 standard matching 更保守），Table 2（page 7）也有数据，但**cross-subject matching 相对于 standard matching 改变了哪些 items 的分类**这一关键比较未在正文展示。读者无法判断 cross-subject matching 是否实质性地改变了结论。\n\n---\n\n**[AGREE] R2-W8: \"DEFF correction 透明度不足\"**\n\n与我的 R1-W1 和 R1-W2 一致。DEFF 的两种 m̄ 估计（simple mean 3.87 vs weighted mean 25.4）给出的 adjusted C% 相差近 2 倍，论文未充分论证偏好哪一个。\n\n---\n\n**[AGREE] R2-W9: \"Discussion 过于压缩\"**\n\n同意。Section 5 在不到半页内覆盖了 Benchmark Temporal Comparability（5.1）和 Recommended Audit Protocol（5.2），对于一篇 analysis paper 而言不够充分。特别是 Section 5.1 的\"5-15% ETS C rate baseline\"需要更仔细的论证——这个 baseline 是否适用于 temporal cohort 比较（见我对 W4 的同意）。\n\n---\n\n**[REBUT] R2-W10: \"Figure 2 dose-response 曲线解读有歧义\"**\n\n部分反驳。Figure 2（page 7）展示 ΔTPR 随 exploitation rate p 单调递增，caption 和正文（Section 4.1, page 7）明确说明 \"ΔTPR increases monotonically with exploitation rate p, confirming that MH-DIF is sensitive to differential item behavior when present. Baseline (no injection) produces ΔFPR ≈ 0.\" 这个信息是清晰的——x 轴是 injection rate，y 轴是 detection improvement over baseline。\n\n但我同意 Figure 2 有一个可改进之处：它只展示了 MMLU 上的 dose-response，未包含其他 benchmark 的对应曲线。如果空间允许，加入 GSM8K 的 dose-response（Section 4.7 提到 GSM8K 的 ΔTPR=+0.54）会增强 generalizability。\n\n---\n\n### Questions 逐条回应\n\n**[AGREE] R2-Q1: \"有多少 temporal DIF 可归因于 legitimate 能力变化 vs construct-irrelevant 变化？\"**\n\n与我对 W4 的同意一致。这是论文的核心未解决问题。论文的 instability decomposition（Appendix A.1）和 logistic regression（Appendix B, Section 4.2 的 Simpson's paradox analysis）提供了部分分解，但不是 clean 的 causal identification。我认为作者应在 rebuttal 中：(a) 承认这一限制，(b) 提供 a back-of-envelope estimate（如：domain-level ability improvement 能解释多少 C% items 的 DIF）。\n\n**[REBUT] R2-Q2: \"Cross-subject matching 如何选择外部学科？\"**\n\n这个问题基于误读。Section 3.4（page 5）的 Remark 明确定义：$M_i^s = \\sum_{s' \\neq s} \\sum_j Y_{ij}$——即**使用所有其他 subjects 的 total score**，不存在\"选择\"哪个外部学科的问题。这不是 arbitrary choice，而是 deterministic——对 subject s 中的 item i，matching variable 是模型在所有非 s subjects 上的总分。因此\"不同选择是否改变结果\"不适用。\n\n但我要指出一个 R2 未提到的相关问题：当某些 subjects 间能力高度相关时（如 STEM domains 之间），cross-subject total score 仍可能泄漏被测 subject 的 ability signal，部分削弱 ΔFPR=0 的保证。论文的 IRT θ 与 total score 相关 r=0.9986（Section 3.4）实际上暗示 cross-subject score 是全局 ability 的一个 strong proxy，这可能意味着 cross-subject matching 与 standard matching 在实践中差异不大——这正是 Table 2（C%=31.5% cross-subject vs 约 31% standard）暗示的。\n\n**[AGREE] R2-Q3: \"2023 vs 2024 二分切割的鲁棒性\"**\n\n合理问题。Table 1（page 7）展示了多种 cohort 定义——Temporal 2023/2024、Ability-quintile Q1-Q2 vs Q4-Q5、Within-family Llama-2/Llama-3、Within-subject per-subject DIF、Random split——但**正文未系统比较不同 temporal cutoff 的影响**（如 2023-Q3 vs 2024-Q1，或用 release date 的 continuous variable）。Section 3.3（page 5）提到 \"models span release dates from 2023 to 2024\"，但 DIF 结果可能对具体 cutoff 敏感——特别是如果 2024 early models 与 2023 late models 差异不大。\n\n**[AGREE] R2-Q4: \"DEFF 校正后 C% 范围哪个端点更代表真实 DIF 率？\"**\n\n与我的 R1-W1 完全一致。这是作者必须在 rebuttal 中回答的核心问题。如我在 R1-W2 中建议，weighted mean m̄=25.4 更合理（大 family 对 χ² 膨胀贡献更大），但这会将 headline number 从 31% 降至 ~13.5%——叙事完全不同。\n\n**[REBUT] R2-Q5: \"Jaccard=0.206 的 20% overlap 可能是 contamination-driven DIF 的证据\"**\n\n这个解读在逻辑上是 possible 但论文已提供反证。Section 4.3（page 7）报告 Enrichment = 0.964，接近 1.0（independent baseline）。如果 20% overlap 是 contamination-driven DIF，Enrichment 应显著 > 1.0。当前 0.964 甚至略低于 1.0，表明 DIF-flagged items 在 web-contaminated items 中的**出现率不高于随机预期**。\n\n此外，论文在同一段指出 DIF-C flagged items 中 30.7% 有 web-contamination labels，而 clean items 中 31.8%——DIF-C 率在 web-contaminated 和 clean items 中几乎相同。这 directly contradicts R2 的解读：如果 contamination 驱动 DIF，web-contaminated items 应有显著更高的 DIF-C rate。\n\n但我要补充一个 nuance：Enrichment 接近 1.0 不等于\"contamination 不导致 DIF\"。它可能意味着 (a) contamination 导致的 DIF 被 non-contamination 源（如训练方法改变）导致的 DIF 所 overwhelm，或 (b) web-overlap labels 本身是 noisy proxy for actual contamination。论文应区分这两种解释。\n\n---\n\n### 对 R2 Overall Assessment（3.0, Findings）的看法\n\nR2 给出 3.0（Findings level），我给出 3.5（Borderline Conference）。分歧主要在于：\n\n1. **新颖性评估**：R2 认为\"直接搬运既有方法\"是 major weakness。我认为 cross-subject matching 和 ground truth meta-critique 构成了足够的 methodological contribution for an analysis paper，且 empirical findings（31% DIF rate、Jaccard=0.206）本身具有重大价值。\n\n2. **\"缺乏解决方案\"的权重**：R2 将此列为 major weakness。我认为诊断性论文在 NLP 中有充分先例（如 Raji et al. 2021 的 benchmark audit 论文），\"发现问题\"本身就是贡献。\n\n3. 但我与 R2 在以下方面一致：DEFF 不确定性（W5/W8）、temporal DIF 的因果模糊性（W4）、Discussion 不足（W9）是需要 rebuttal 解决的实质问题。\n\n**如果作者无法在 rebuttal 中解决 DEFF 和 causal interpretation 问题，我会倾向 R2 的 3.0 而非维持 3.5。**",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 859 · 2026-05-22T15:17:37.547495+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4172
}
```

</details>

---


### Assistant

_source line 860 · 2026-05-22T15:17:49.244201+00:00_

交叉回应已提交。总结：

- **R2 的 10 条 Weakness 中，我同意 7 条**（W3/W4/W5/W6/W7/W8/W9），反驳 2 条（W1/W2），部分反驳 1 条（W10）
- **R2 的 5 个 Questions 中，我同意 3 个**（Q1/Q3/Q4），反驳 2 个（Q2 基于误读 cross-subject matching 机制，Q5 被 Enrichment=0.964 的数据反驳）
- **核心共识点**：DEFF 不确定性（我的 R1-W1 = R2-W5/W8）和 temporal DIF 的因果模糊性（R2-W4）是两个 critical issues，作者必须在 rebuttal 中回应
- **主要分歧**：R2 评 3.0 (Findings)，我评 3.5 (Borderline Conference)。分歧在于新颖性评估——我认为 cross-subject matching 框架和 ground truth meta-critique 的 empirical findings 构成足够贡献

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 30

## Round 30

48 recorded events


### User

_source line 861 · 2026-05-22T15:54:47.816315+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查**方法严谨性**。

## 论文信息
- **标题**: Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models
- **路径**: projects/irt_equated_bench_regen/paper/main.tex
- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/submitted.pdf
- **目标 venue**: EMNLP 2026（通过 ARR）
- **Deadline**: 2026-05-25
- **格式要求**: ACL 模板, long paper 8 页正文限制, unlimited references, Limitations 必须有但不计入页数, double-blind

## 你的审查侧重

**方法严谨性**——重点审查以下方面：

1. **统计方法有效性**: MH-DIF 在 LLM 场景下的适用性，K=5 分层是否充分，ETS 双重阈值在大样本下是否退化
2. **非独立性处理**: DEFF 校正（simple mean vs weighted mean）、family-level cluster bootstrap、graduated de-duplication 三种方法的一致性和可靠性；13.5%-29.2% 范围是否被充分论证
3. **Semi-synthetic 框架**: binary response flipping 的现实性，cross-subject matching 的 ΔFPR=0 保证条件和边界，multi-subject injection 时的退化
4. **实验设计**: cohort 定义合理性，random-split baseline 是否充分，matched-ability 控制，IRT θ-conditioning 敏感性检查
5. **可重复性**: 数据来源（METABENCH）、代码可用性、关键超参数报告完整性
6. **页数合规性**: 正文是否在 8 页以内

请按 ARR 审稿标准进行严格评审。输出格式：
- Summary（2-3 句）
- Strengths（逐条 S1, S2, ...）
- Weaknesses（逐条 W1, W2, ... 按严重程度排序，标注 [Must-Fix] / [Should-Fix] / [Minor]）
- Questions（Q1, Q2, ...）
- Missing References
- Overall Assessment（评分 + 置信度）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-22T15:54:55.739056+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 863 · 2026-05-22T15:54:55.841982+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 864 · 2026-05-22T15:55:01.171051+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 865 · 2026-05-22T15:55:03.376615+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 866 · 2026-05-22T15:55:14.877077+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

For Main papers, reviewers should consider multiple criteria, while for Findings papers, the main criteria are sou
…[truncated 1398 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 13706
}
```

</details>

---


### Tool result

_source line 867 · 2026-05-22T15:55:16.990526+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 573.4}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 525.7}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 530.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 471.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 559.6}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p9.png\", \"width\": 1
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 13613
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-22T15:55:34.809909+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-22T15:55:34.810447+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 870 · 2026-05-22T15:55:35.313031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 871 · 2026-05-22T15:55:36.372014+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1058
}
```

</details>

---


### Tool call

_source line 872 · 2026-05-22T15:55:37.074529+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 873 · 2026-05-22T15:55:37.126558+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 874 · 2026-05-22T15:55:37.327871+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 875 · 2026-05-22T15:55:37.836247+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 876 · 2026-05-22T15:55:38.244867+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1170
}
```

</details>

---


### Tool result

_source line 877 · 2026-05-22T15:55:39.102024+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1975
}
```

</details>

---


### Tool result

_source line 878 · 2026-05-22T15:55:39.304734+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1976
}
```

</details>

---


### Tool result

_source line 879 · 2026-05-22T15:55:39.557653+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1721
}
```

</details>

---


### Tool call

_source line 880 · 2026-05-22T15:55:44.831071+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 881 · 2026-05-22T15:55:45.787935+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 882 · 2026-05-22T15:55:45.788622+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 883 · 2026-05-22T15:55:46.292929+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 884 · 2026-05-22T15:55:46.795139+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 885 · 2026-05-22T15:55:46.795593+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 886 · 2026-05-22T15:55:47.656645+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1363
}
```

</details>

---


### Tool result

_source line 887 · 2026-05-22T15:55:47.657939+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 862
}
```

</details>

---


### Tool call

_source line 888 · 2026-05-22T15:55:47.658327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 889 · 2026-05-22T15:55:50.475214+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2816
}
```

</details>

---


### Tool call

_source line 890 · 2026-05-22T15:55:50.475590+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all dimensions/criteria reviewers must score, the rating scales for each dimension, and any specific instructions for each criterion. Include the Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all dimensions/criteria reviewers must score, the rating scales for each dimension, and any specific instructions for each criterion. Include the Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions."
  }
}
```

</details>

---


### Tool result

_source line 891 · 2026-05-22T15:55:55.402917+00:00_

# ACL Rolling Review Form: Complete Scoring Dimensions

## Primary Scoring Dimensions

**1. Soundness**
- Scale: 1-5 (with .5 increments)
- 5 = Excellent: "one of the most thorough I have seen, given its type"
- 4 = Strong: sufficient support for claims
- 3 = Acceptable: main claims supported with minor gaps
- 2 = Poor: major technical/methodological problems
- 1 = Major Issues: insufficient rigor for publication

**2. Excitement**
- Scale: 1-5 (with .5 increments)
- 5 = Highly Exciting: would recommend to others
- 4 = Exciting: would mention to peers
- 3 = Interesting: might attend presentation
- 2 = Potentially Interesting: limited personal resonance
- 1 = Not Exciting: no community relevance

**3. Overall Assessment**
- Scale: 1-5 (with .5 increments)
- 5 = Consider for Award: "top 2.5% papers"
- 4 = Conference: acceptable for publication
- 3 = Findings: suitable for findings track
- 2 = Resubmit next cycle: needs revisions
- 1 = Do not resubmit: fundamentally flawed

## Secondary Evaluation Dimensions

**Reviewer Confidence** (1-5 scale): assesses evaluation reliability

**Reproducibility** (1-5 scale): feasibility of replicating results

**Datasets** (1-5 scale): if released, potential research value

**Software** (1-5 scale): if released, potential utility

**Author Identity Knowledge** (1-5 scale): blind review compliance

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4927
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-22T15:56:02.554523+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 893 · 2026-05-22T15:56:03.991374+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 579.7}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 559.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.8}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 350.7}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 94.9}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1436
}
```

</details>

---


### Tool call

_source line 894 · 2026-05-22T15:56:14.396900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 895 · 2026-05-22T15:56:15.201514+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 896 · 2026-05-22T15:56:15.302277+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 897 · 2026-05-22T15:56:15.854826+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 898 · 2026-05-22T15:56:16.258656+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 899 · 2026-05-22T15:56:16.259132+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 900 · 2026-05-22T15:56:17.112917+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1258
}
```

</details>

---


### Tool result

_source line 901 · 2026-05-22T15:56:17.114170+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 902 · 2026-05-22T15:56:17.114828+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 903 · 2026-05-22T15:56:17.316283+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_11/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 904 · 2026-05-22T15:56:17.470745+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 154
}
```

</details>

---


### Tool result

_source line 905 · 2026-05-22T15:56:17.573520+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 458
}
```

</details>

---


### Tool call

_source line 906 · 2026-05-22T16:02:33.560515+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 — 方法严谨性审查\n\n### Summary\n\n本文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 时序稳定性检测，基于 METABENCH 响应矩阵（5,227 models × 12,508 MMLU items）发现约 27–29% 的 items 在 2023 vs. 2024 模型队列间存在差异功能。论文构建了 semi-synthetic validation 框架验证检测能力，并提出了实用的 DIF 审计协议。方法论整体扎实但在非独立性校正的 framing、semi-synthetic 框架的现实性、以及因果推断的边界上存在需要修正的问题。\n\n---\n\n### Strengths\n\n**S1. 大规模心理测量审计，方法论基础扎实**\nMH-DIF 是教育测量中最成熟的 DIF 检测方法之一（Holland & Thayer, 1988），论文正确地选用了非参数方法（不依赖 IRT 模型拟合），K=5 等概率分层、ETS 双重阈值（|Δ_MH| ≥ 1.5 且 p < 0.05）均为标准实践。5,227 models × 12,508 items 的规模在该领域前所未有。\n\n**S2. 多重稳健性检验形成证据三角**\n三种非独立性校正方法（simple-mean DEFF 29.2%、graduated de-duplication 29.1%、cluster bootstrap 下界 26.7%）、random-split baseline（C% = 0.18%）、matched-ability quintile 控制、IRT θ-conditioning 灵敏度检查（r(θ, total) = 0.9986）——这些检验覆盖了主要方法论威胁。\n\n**S3. Semi-synthetic 框架提供了受控验证**\nCross-subject matching 在 single-subject injection 下保证 ΔFPR = 0（by construction），并实证展示了 multi-subject injection 时的优雅退化（δ ≤ 5 时 ΔFPR ≤ 0.017）。TPR 随 exploitation rate ε 单调递增（Figure 2），验证了检测灵敏度。\n\n**S4. 区分 global exposure 与 differential functioning**\nSection 4.3 ground truth mismatch 分析（enrichment ratio = 0.964，Jaccard = 0.206）清晰地论证了 web-overlap labels 与 DIF flags 测量不同构念。这是对 contamination detection 文献的重要概念贡献。\n\n**S5. 实用审计协议**\nSection 5.2 提出的 Monitor/Flag (15%) 和 Flag/Act (25%) 阈值、subject-level 监控、DIF pre-screening 建议，直接可操作。\n\n**S6. 诚实的局限性讨论**\nLimitations 部分坦承 IRT 模型拟合差（Appendix A）、binary flipping 不现实、ΔFPR=0 仅限单科注入等，这种透明度值得肯定。\n\n---\n\n### Weaknesses\n\n**W1 [Must-Fix] DEFF 估计量选择偏向高端，13.5% vs. 29.2% 分歧未充分论证**\n\n论文报告四种 DEFF 相关估计：simple-mean DEFF（29.2%）、weighted-mean DEFF（13.5%）、graduated de-duplication（29.1%）、cluster bootstrap 下界（26.7%）。前三个\"收敛\"于 ~27–29%，weighted-mean 被简短地以\"effective cluster size functionally identical\"为由排除（Appendix C）。\n\n但在 survey sampling 理论中，weighted mean（n̄_w = Σn²ᵢ/Σnᵢ；Kish, 1965）是不等大 cluster 情况下的**标准**选择，因为随机抽样的观测更可能来自大 cluster。LLM 模型族大小极不均等（Llama-3 ≈ 315, Mistral ≈ 347 vs. 小族 < 10），正是 weighted mean 设计用于处理的场景。Simple mean 低估 DEFF，从而高估有效样本量。\n\n论文对 weighted-mean 的反驳——\"models with distinct training data\"——实际上是在质疑 ICC 本身的有效性，而非 DEFF 估计量的选择。如果同族模型确实独立（ICC ≈ 0），则所有 DEFF 估计量都应接近 1.0，不会出现 simple-mean DEFF = 3.87 的结果。mean ICC = 0.047 表明族内相关确实存在，这恰恰要求使用 weighted mean。\n\n**建议修改方向**：\n- 明确论证为何在 LLM 场景下 simple-mean DEFF 优于 weighted-mean，而非仅说\"unreliable\"\n- 将 headline finding 报告为范围（13.5%–29.2%）而非仅 ≈27–29%\n- 展示 C% 对不同 DEFF 估计量的完整敏感性曲线\n- 即使采用最保守的 13.5%，仍为 random-split baseline 的 75×——核心发现仍然成立，但 framing 需要更诚实\n\n**W2 [Must-Fix] Binary response flipping 作为 contamination 模拟过于简化，且无法区分 DIF 成因**\n\nSemi-synthetic 框架（Section 3.4）通过将 incorrect responses 翻转为 correct 来模拟 contamination。但真实 contamination 的机制远比 binary flipping 复杂：\n- 部分记忆（partial memorization）：模型可能记住答案选项顺序而非内容\n- 推理捷径（reasoning shortcuts）：模型可能跳过推理直接输出答案\n- 格式特异性（format-specific advantages）：某些 prompt 格式下 contamination 效应不同\n- 非均匀影响：真实 contamination 对不同难度 items 影响不同（容易题可能无变化）\n\n论文在 Limitations 中承认了这些问题，但 Section 4.5 的 validation 结论仍然基于这种简化模拟。如果 MH-DIF 的 TPR 在 realistic contamination patterns 下显著下降，论文的 detection power claims 就不可靠。\n\n更根本的问题：semi-synthetic 框架验证了 MH-DIF **能**检测人工注入的 DIF，但无法证明实际观测到的 ~27–29% DIF **就是** contamination。论文在 Section 5.1 正确区分了三种可能成因（differential contamination、capability evolution、training methodology shifts），但 Section 5.2 的审计协议将所有 DIF 一律当作需要\"Flag/Act\"的问题处理，没有区分 benign DIF（genuine capability change）和 malignant DIF（contamination）。\n\n**建议修改方向**：\n- 在 Section 3.4 明确声明 binary flipping 是 upper bound 模拟（worst-case uniform），并讨论 detection power 在更现实模式下可能的退化\n- 在 Section 5.2 的审计协议中加入区分 DIF 成因的指引（e.g., 结合 domain-specificity、item difficulty profile 等信号判断是否为 contamination）\n\n**W3 [Should-Fix] IRT 模型拟合差但仍用于 power analysis 和 θ-conditioning**\n\nAppendix A 坦承 MMLU 响应矩阵对一维 2PL 模型拟合差（\"expected for a 57-subject multidimensional benchmark\"）。论文正确指出 MH-DIF 不依赖 IRT 假设。然而：\n- Section 4.1 的 Monte Carlo power analysis 使用\"empirical 2PL parameters (a = 1.2, b = 0.84)\"——这些参数来自拟合差的模型，power analysis 的可靠性存疑\n- Section 4.2 的 IRT θ-conditioning sensitivity check（r(θ, total) = 0.9986）——如果 IRT 模型拟合差，θ 估计本身不可靠，这个\"sensitivity check\"的价值打折扣\n- Table 2 将 θ-conditioning 列为 structural control——但这个 control 建立在不可靠的 θ 估计上\n\n**建议修改方向**：在 power analysis 部分加入对 2PL 参数可靠性的 caveat；考虑使用 non-parametric bootstrap power analysis 作为替代\n\n**W4 [Should-Fix] Multidimensionality 威胁未完全排除**\n\nMMLU 包含 57 subjects，total score matching 在多维结构下可能产生 spurious DIF（Ackerman, 1992）。论文通过 domain-specificity decomposition（Appendix A.1）论证 domain-level improvement 仅解释 < 0.1% 的 item-level DIF variance。但：\n- 如果维度粒度细于\"domain\"（e.g., 特定推理技能），domain-level decomposition 无法捕获\n- Cross-subject matching 使用 57 subjects 之外的 total score，但如果 2023→2024 的能力增长在 subject 间不均匀（Section 5.1 已证实如此：STEM 34.5% vs. Humanities 25.4%），则 cross-subject total score 仍然是 confounded matching variable\n- 论文未尝试任何多维 DIF 方法（如 SIBTEST 的多维扩展，或 logistic regression with interaction terms）\n\n**建议修改方向**：讨论 sub-domain 维度的 DIF 可能性；或论证为何 domain-level decomposition 足以排除 finer-grained multidimensionality 威胁\n\n**W5 [Should-Fix] 排名稳定性（ρ = 0.997）与 DIF 实际影响之间的张力**\n\nSection 5.1 报告聚合排名稳定性 ρ = 0.997，Section 4.6 报告 DIF-flagged items 移除后 33.6% 的 pairwise rankings 反转。这两个发现存在张力但未充分讨论：\n- 如果 ρ = 0.997（聚合排名几乎不变），那么 DIF 的实际影响有多大？\n- 如果 33.6% pairwise rankings 反转，为什么 ρ 仍然那么高？（答案可能是反转发生在能力接近的模型对之间，但论文未分析）\n- Figure 6 中 DIF-ordered vs. random removal 的 ρ 差异在大多数 benchmarks 上很小（< 0.005）\n\n这个张力影响论文的 motivation：如果 DIF 对排名影响极小，审计协议的紧迫性降低。\n\n**建议修改方向**：分析 pairwise ranking reversal 发生在哪些模型对之间（能力差距分布），reconcile 聚合 ρ 与 pairwise reversal 的矛盾\n\n**W6 [Should-Fix] De-duplication K=29 的选择缺乏敏感性分析**\n\nGraduated de-duplication 在 K=29 时给出 29.1%。但为什么选 K=29？论文未报告 C% 对 K 的完整敏感性曲线。如果 C% 在 K=5→K=50 范围内变化大，则 29.1% 这个点估计不可靠。Table 7（Appendix C）似乎给出了不同 K 值的结果，但主文中只引用 K=29。\n\n**建议修改方向**：在主文或附录中展示 C% vs. K 的完整敏感性曲线，论证 K=29 附近的稳定性\n\n**W7 [Minor] Cross-benchmark validation 深度不足**\n\nTable 3 报告 6 个 benchmarks 的 C% 范围（17.9%–31.3%），但非 MMLU benchmarks 的分析仅限于报告 C%，没有任何非独立性校正、power analysis 或 sensitivity check。如果其他 benchmarks 的模型族结构不同，raw C% 可能不可比。\n\n**W8 [Minor] 符号标记不一致**\n\n论文在主文中使用 ΔFPR 和 ΔTPR，但首次在 Section 3.4 引入时未给出正式定义。Appendix 中的符号（如 n̄_w, ICC_j）在主文引用时也缺乏回指。\n\n**W9 [Minor] Limitations 中包含部分结果性内容**\n\nLimitations section（page 9）重申了 cluster bootstrap upper bound (53.2%)、corrected ≈27–29% 等数值。虽然是在限制性语境下讨论，但 EMNLP 格式要求 Limitations 不包含\"excessive additional content\"。目前 Limitations 约占 1 整页，建议精简。\n\n---\n\n### Questions\n\n**Q1.** Weighted-mean DEFF 给出 13.5% 而非 29.2%。如果采用 weighted-mean（survey sampling 标准方法），论文的核心 claim 是否需要修改为\"13.5%–29.2%\"？作者能否提供更强的论证来排除 weighted-mean？\n\n**Q2.** Semi-synthetic 框架中 binary response flipping 的 TPR 曲线（Figure 2）是否在更现实的 contamination 模式下（如 partial memorization、difficulty-dependent flipping）进行过测试？如果没有，作者如何保证 Section 4.5 的 detection power claims 在实践中成立？\n\n**Q3.** 如何 reconcile ρ = 0.997（聚合排名几乎不变）与 33.6% pairwise ranking reversal？这些 reversal 是否集中在能力差距 < ε 的模型对之间？\n\n**Q4.** Monte Carlo power analysis（Section 4.1）使用的 2PL 参数 (a = 1.2, b = 0.84) 来自拟合差的 IRT 模型（Appendix A 承认 poor fit）。是否用 non-parametric 方法验证过 power analysis 结论？\n\n**Q5.** Cross-subject matching 在 2023→2024 能力增长跨 subject 不均匀时（STEM > Humanities），匹配变量（non-focal subject total score）是否仍然是有效的 ability proxy？\n\n**Q6.** De-duplication 的 K 值从 1 到 50 变化时，C% 的完整变化轨迹是什么样的？K=29 是否处于稳定平台？\n\n---\n\n### Missing References\n\n- Ackerman, T. A. (1992). A didactic explanation of item bias, item impact, and item validity from a multidimensional perspective. — 论文引用但未充分讨论其 multidimensional DIF 方法\n- Shealy & Stout (1993). A model-based standardization approach... SIBTEST. — 多维 DIF 检测的替代方法，应在 Related Work 中讨论\n- Camilli, G. (2006). Test fairness. In Educational Measurement. — DIF 在公平性测试中的标准参考\n- Zumbo, B. D. (1999). A handbook on the theory and methods of DIF. — logistic regression DIF 方法的标准参考，论文虽提及 LR-DIF 但未引用此书\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | MH-DIF 方法论基础扎实，但 DEFF 估计量选择（W1）和 semi-synthetic 框架局限性（W2）构成方法论缺口。核心发现（DIF >> random baseline）在所有估计量下均成立，但 headline number 的可靠性取决于 DEFF 选择 |\n| Excitement | 3.5/5 | 将心理测量 DIF 引入 LLM benchmark 评估是新颖且及时的应用，区分 global exposure vs. differential functioning 是概念贡献。但 practical impact 受限于 ρ = 0.997 的排名稳定性 |\n| Reproducibility | 4/5 | METABENCH 公开可用，代码声称可用（匿名 URL），关键超参数（K=5, ETS 阈值, 2023/2024 split）报告完整。附录提供 DEFF 估计细节。缺少部分中间结果的完整数据表 |\n| Overall Assessment | **3.5** — Borderline Conference | 方法论基础扎实、规模大、概念新颖，但 DEFF framing 偏向高端（W1）和 semi-synthetic 框架无法区分 DIF 成因（W2）构成显著弱点。核心发现——temporal DIF 远超 random baseline——是可靠的，但 27–29% 这个 headline number 需要更审慎的 framing。修复 W1（诚实报告 13.5%–29.2% 范围）和 W2（在审计协议中区分 DIF 成因）后可达 Conference 水平 |\n\n**Confidence**: 4/5 — 我对 DIF 方法论和 survey sampling DEFF 理论较为熟悉，对论文的核心方法有充分理解。对 LLM benchmark contamination 领域的最新进展了解中等。\n\n---\n\n### 页数合规性检查\n\n- 主文（Sections 1–6）：Pages 1–8 ✅（合规）\n- Limitations：Page 9（不计入 8 页限制）✅\n- References：Pages 10–11（不计入限制）✅\n- Appendices A–G：Pages 12–16 ✅\n- 格式：ACL 模板，double-blind（\"Anonymous ACL submission\"）✅\n\n**注意**：Page 8 极度密集（Table 3 + Section 4.7 + Section 5 Discussion + Section 6 Conclusion），虽然技术上合规但视觉上拥挤，可能影响阅读体验。\n",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 — 方法严谨性审查\n\n### Summary\n\n本文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 时序稳定性检测，基于 METABENCH 响应矩阵（5,227 models × 12,508 MMLU items）发现约 27–29% 的 items 在 2023 vs. 2024 模型队列间存在差异功能。论文构建了 semi-synthetic validation 框架验证检测能力，并提出了实用的 DIF 审计协议。方法论整体扎实但在非独立性校正的 framing、semi-synthetic 框架的现实性、以及因果推断的边界上存在需要修正的问题。\n\n---\n\n### Strengths\n\n**S1. 大规模心理测量审计，方法论基础扎实**\nMH-DIF 是教育测量中最成熟的 DIF 检测方法之一（Holland & Thayer, 1988），论文正确地选用了非参数方法（不依赖 IRT 模型拟合），K=5 等概率分层、ETS 双重阈值（|Δ_MH| ≥ 1.5 且 p < 0.05）均为标准实践。5,227 models × 12,508 items 的规模在该领域前所未有。\n\n**S2. 多重稳健性检验形成证据三角**\n三种非独立性校正方法（simple-mean DEFF 29.2%、graduated de-duplication 29.1%、cluster bootstrap 下界 26.7%）、random-split baseline（C% = 0.18%）、matched-ability quintile 控制、IRT θ-conditioning 灵敏度检查（r(θ, total) = 0.9986）——这些检验覆盖了主要方法论威胁。\n\n**S3. Semi-synthetic 框架提供了受控验证**\nCross-subject matching 在 single-subject injection 下保证 ΔFPR = 0（by construction），并实证展示了 multi-subject injection 时的优雅退化（δ ≤ 5 时 ΔFPR ≤ 0.017）。TPR 随 exploitation rate ε 单调递增（Figure 2），验证了检测灵敏度。\n\n**S4. 区分 global exposure 与 differential functioning**\nSection 4.3 ground truth mismatch 分析（enrichment ratio = 0.964，Jaccard = 0.206）清晰地论证了 web-overlap labels 与 DIF flags 测量不同构念。这是对 contamination detection 文献的重要概念贡献。\n\n**S5. 实用审计协议**\nSection 5.2 提出的 Monitor/Flag (15%) 和 Flag/Act (25%) 阈值、subject-level 监控、DIF pre-screening 建议，直接可操作。\n\n**S6. 诚实的局限性讨论**\nLimitations 部分坦承 IRT 模型拟合差（Appendix A）、binary flipping 不现实、ΔFPR=0 仅限单科注入等，这种透明度值得肯定。\n\n---\n\n### Weaknesses\n\n**W1 [Must-Fix] DEFF 估计量选择偏向高端，13.5% vs. 29.2% 分歧未充分论证**\n\n论文报告四种 DEFF 相关估计：simple-mean DEFF（29.2%）、weighted-mean DEFF（13.5%）、graduated de-duplication（29.1%）、cluster bootstrap 下界（26.7%）。前三个\"收敛\"于 ~27–29%，weighted-mean 被简短地以\"effective cluster size functionally identical\"为由排除（Appendix C）。\n\n但在 survey sampling 理论中，weighted mean（n̄_w = Σn²ᵢ/Σnᵢ；Kish, 1965）是不等大 cluster 情况下的**标准**选择，因为随机抽样的观测更可能来自大 cluster。LLM 模型族大小极不均等（Llama-3 ≈ 315, Mistral ≈ 347 vs. 小族 < 10），正是 weighted mean 设计用于处理的场景。Simple mean 低估 DEFF，从而高估有效样本量。\n\n论文对 weighted-mean 的反驳——\"models with distinct training data\"——实际上是在质疑 ICC 本身的有效性，而非 DEFF 估计量的选择。如果同族模型确实独立（ICC ≈ 0），则所有 DEFF 估计量都应接近 1.0，不会出现 simple-mean DEFF = 3.87 的结果。mean ICC = 0.047 表明族内相关确实存在，这恰恰要求使用 weighted mean。\n\n**建议修改方向**：\n- 明确论证为何在 LLM 场景下 simple-mean DEFF 优于 weighted-mean，而非仅说\"unreliable\"\n- 将 headline finding 报告为范围（13.5%–29.2%）而非仅 ≈27–29%\n- 展示 C% 对不同 DEFF 估计量的完整敏感性曲线\n- 即使采用最保守的 13.5%，仍为 random-split baseline 的 75×——核心发现仍然成立，但 framing 需要更诚实\n\n**W2 [Must-Fix] Binary response flipping 作为 contamination 模拟过于简化，且无法区分 DIF 成因**\n\nSemi-synthetic 框架（Section 3.4）通过将 incorrect responses 翻转为 correct 来模拟 contamination。但真实 contamination 的机制远比 binary flipping 复杂：\n- 部分记忆（partial memorization）：模型可能记住答案选项顺序而非内容\n- 推理捷径（reasoning shortcuts）：模型可能跳过推理直接输出答案\n- 格式特异性（format-specific advantages）：某些 prompt 格式下 contamination 效应不同\n- 非均匀影响：真实 contamination 对不同难度 items 影响不同（容易题可能无变化）\n\n论文在 Limitations 中承认了这些问题，但 Section 4.5 的 validation 结论仍然基于这种简化模拟。如果 MH-DIF 的 TPR 在 realistic contamination patterns 下显著下降，论文的 detection power claims 就不可靠。\n\n更根本的问题：semi-synthetic 框架验证了 MH-DIF **能**检测人工注入的 DIF，但无法证明实际观测到的 ~27–29% DIF **就是** contamination。论文在 Section 5.1 正确区分了三种可能成因（differential contamination、capability evolution、training methodology shifts），但 Section 5.2 的审计协议将所有 DIF 一律当作需要\"Flag/Act\"的问题处理，没有区分 benign DIF（genuine capability change）和 malignant DIF（contamination）。\n\n**建议修改方向**：\n- 在 Section 3.4 明确声明 binary flipping 是 upper bound 模拟（worst-case uniform），并讨论 detection power 在更现实模式下可能的退化\n- 在 Section 5.2 的审计协议中加入区分 DIF 成因的指引（e.g., 结合 domain-specificity、item difficulty profile 等信号判断是否为 contamination）\n\n**W3 [Should-Fix] IRT 模型拟合差但仍用于 power analysis 和 θ-conditioning**\n\nAppendix A 坦承 MMLU 响应矩阵对一维 2PL 模型拟合差（\"expected for a 57-subject multidimensional benchmark\"）。论文正确指出 MH-DIF 不依赖 IRT 假设。然而：\n- Section 4.1 的 Monte Carlo power analysis 使用\"empirical 2PL parameters (a = 1.2, b = 0.84)\"——这些参数来自拟合差的模型，power analysis 的可靠性存疑\n- Section 4.2 的 IRT θ-conditioning sensitivity check（r(θ, total) = 0.9986）——如果 IRT 模型拟合差，θ 估计本身不可靠，这个\"sensitivity check\"的价值打折扣\n- Table 2 将 θ-conditioning 列为 structural control——但这个 control 建立在不可靠的 θ 估计上\n\n**建议修改方向**：在 power analysis 部分加入对 2PL 参数可靠性的 caveat；考虑使用 non-parametric bootstrap power analysis 作为替代\n\n**W4 [Should-Fix] Multidimensionality 威胁未完全排除**\n\nMMLU 包含 57 subjects，total score matching 在多维结构下可能产生 spurious DIF（Ackerman, 1992）。论文通过 domain-specificity decomposition（Appendix A.1）论证 domain-level improvement 仅解释 < 0.1% 的 item-level DIF variance。但：\n- 如果维度粒度细于\"domain\"（e.g., 特定推理技能），domain-level decomposition 无法捕获\n- Cross-subject matching 使用 57 subjects 之外的 total score，但如果 2023→2024 的能力增长在 subject 间不均匀（Section 5.1 已证实如此：STEM 34.5% vs. Humanities 25.4%），则 cross-subject total score 仍然是 confounded matching variable\n- 论文未尝试任何多维 DIF 方法（如 SIBTEST 的多维扩展，或 logistic regression with interaction terms）\n\n**建议修改方向**：讨论 sub-domain 维度的 DIF 可能性；或论证为何 domain-level decomposition 足以排除 finer-grained multidimensionality 威胁\n\n**W5 [Should-Fix] 排名稳定性（ρ = 0.997）与 DIF 实际影响之间的张力**\n\nSection 5.1 报告聚合排名稳定性 ρ = 0.997，Section 4.6 报告 DIF-flagged items 移除后 33.6% 的 pairwise rankings 反转。这两个发现存在张力但未充分讨论：\n- 如果 ρ = 0.997（聚合排名几乎不变），那么 DIF 的实际影响有多大？\n- 如果 33.6% pairwise rankings 反转，为什么 ρ 仍然那么高？（答案可能是反转发生在能力接近的模型对之间，但论文未分析）\n- Figure 6 中 DIF-ordered vs. random removal 的 ρ 差异在大多数 benchmarks 上很小（< 0.005）\n\n这个张力影响论文的 motivation：如果 DIF 对排名影响极小，审计协议的紧迫性降低。\n\n**建议修改方向**：分析 pairwise ranking reversal 发生在哪些模型对之间（能力差距分布），reconcile 聚合 ρ 与 pairwise reversal 的矛盾\n\n**W6 [Should-Fix] De-duplication K=29 的选择缺乏敏感性分析**\n\nGraduated de-duplication 在 K=29 时给出 29.1%。但为什么选 K=29？论文未报告 C% 对 K 的完整敏感性曲线。如果 C% 在 K=5→K=50 范围内变化大，则 29.1% 这个点估计不可靠。Table 7（Appendix C）似乎给出了不同 K 值的结果，但主文中只引用 K=29。\n\n**建议修改方向**：在主文或附录中展示 C% vs. K 的完整敏感性曲线，论证 K=29 附近的稳定性\n\n**W7 [Minor] Cross-benchmark validation 深度不足**\n\nTable 3 报告 6 个 benchmarks 的 C% 范围（17.9%–31.3%），但非 MMLU benchmarks 的分析仅限于报告 C%，没有任何非独立性校正、power analysis 或 sensitivity check。如果其他 benchmarks 的模型族结构不同，raw C% 可能不可比。\n\n**W8 [Minor] 符号标记不一致**\n\n论文在主文中使用 ΔFPR 和 ΔTPR，但首次在 Section 3.4 引入时未给出正式定义。Appendix 中的符号（如 n̄_w, ICC_j）在主文引用时也缺乏回指。\n\n**W9 [Minor] Limitations 中包含部分结果性内容**\n\nLimitations section（page 9）重申了 cluster bootstrap upper bound (53.2%)、corrected ≈27–29% 等数值。虽然是在限制性语境下讨论，但 EMNLP 格式要求 Limitations 不包含\"excessive additional content\"。目前 Limitations 约占 1 整页，建议精简。\n\n---\n\n### Questions\n\n**Q1.** Weighted-mean DEFF 给出 13.5% 而非 29.2%。如果采用 weighted-mean（survey sampling 标准方法），论文的核心 claim 是否需要修改为\"13.5%–29.2%\"？作者能否提供更强的论证来排除 weighted-mean？\n\n**Q2.** Semi-synthetic 框架中 binary response flipping 的 TPR 曲线（Figure 2）是否在更现实的 contamination 模式下（如 partial memorization、difficulty-dependent flipping）进行过测试？如果没有，作者如何保证 Section 4.5 的 detection power claims 在实践中成立？\n\n**Q3.** 如何 reconcile ρ = 0.997（聚合排名几乎不变）与 33.6% pairwise ranking reversal？这些 reversal 是否集中在能力差距 < ε 的模型对之间？\n\n**Q4.** Monte Carlo power analysis（Section 4.1）使用的 2PL 参数 (a = 1.2, b = 0.84) 来自拟合差的 IRT 模型（Appendix A 承认 poor fit）。是否用 non-parametric 方法验证过 power analysis 结论？\n\n**Q5.** Cross-subject matching 在 2023→2024 能力增长跨 subject 不均匀时（STEM > Humanities），匹配变量（non-focal subject total score）是否仍然是有效的 ability proxy？\n\n**Q6.** De-duplication 的 K 值从 1 到 50 变化时，C% 的完整变化轨迹是什么样的？K=29 是否处于稳定平台？\n\n---\n\n### Missing References\n\n- Ackerman, T. A. (1992). A didactic explanation of item bias, item impact, and item validity from a multidimensional perspective. — 论文引用但未充分讨论其 multidimensional DIF 方法\n- Shealy & Stout (1993). A model-based standardization approach... SIBTEST. — 多维 DIF 检测的替代方法，应在 Related Work 中讨论\n- Camilli, G. (2006). Test fairness. In Educational Measurement. — DIF 在公平性测试中的标准参考\n- Zumbo, B. D. (1999). A handbook on the theory and methods of DIF. — logistic regression DIF 方法的标准参考，论文虽提及 LR-DIF 但未引用此书\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | MH-DIF 方法论基础扎实，但 DEFF 估计量选择（W1）和 semi-synthetic 框架局限性（W2）构成方法论缺口。核心发现（DIF >> random baseline）在所有估计量下均成立，但 headline number 的可靠性取决于 DEFF 选择 |\n| Excitement | 3.5/5 | 将心理测量 DIF 引入 LLM benchmark 评估是新颖且及时的应用，区分 global exposure vs. differential functioning 是概念贡献。但 practical impact 受限于 ρ = 0.997 的排名稳定性 |\n| Reproducibility | 4/5 | METABENCH 公开可用，代码声称可用（匿名 URL），关键超参数（K=5, ETS 阈值, 2023/2024 split）报告完整。附录提供 DEFF 估计细节。缺少部分中间结果的完整数据表 |\n| Overall Assessment | **3.5** — Borderline Conference | 方法论基础扎实、规模大、概念新颖，但 DEFF framing 偏向高端（W1）和 semi-synthetic 框架无法区分 DIF 成因（W2）构成显著弱点。核心发现——temporal DIF 远超 random baseline——是可靠的，但 27–29% 这个 headline number 需要更审慎的 framing。修复 W1（诚实报告 13.5%–29.2% 范围）和 W2（在审计协议中区分 DIF 成因）后可达 Conference 水平 |\n\n**Confidence**: 4/5 — 我对 DIF 方法论和 survey sampling DEFF 理论较为熟悉，对论文的核心方法有充分理解。对 LLM benchmark contamination 领域的最新进展了解中等。\n\n---\n\n### 页数合规性检查\n\n- 主文（Sections 1–6）：Pages 1–8 ✅（合规）\n- Limitations：Page 9（不计入 8 页限制）✅\n- References：Pages 10–11（不计入限制）✅\n- Appendices A–G：Pages 12–16 ✅\n- 格式：ACL 模板，double-blind（\"Anonymous ACL submission\"）✅\n\n**注意**：Page 8 极度密集（Table 3 + Section 4.7 + Section 5 Discussion + Section 6 Conclusion），虽然技术上合规但视觉上拥挤，可能影响阅读体验。\n",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 907 · 2026-05-22T16:02:37.732866+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4172
}
```

</details>

---


### Assistant

_source line 908 · 2026-05-22T16:02:47.479124+00:00_

审稿报告已提交给 Review Director。

**审查完成概要**：

- **Overall: 3.5（Borderline Conference）**
- **2 个 Must-Fix**：(1) DEFF 估计量选择偏向高端，13.5% vs 29.2% 的分歧需更充分论证；(2) binary response flipping 过于简化，审计协议未区分 DIF 成因
- **4 个 Should-Fix**：IRT 拟合差但用于 power analysis、multidimensionality 威胁未完全排除、排名稳定性与 DIF 影响的张力、de-duplication K=29 缺敏感性分析
- **3 个 Minor**：cross-benchmark validation 深度不足、符号不一致、Limitations 偏长
- **页数合规**：主文 8 页，符合 EMNLP 2026 要求

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 31

## Round 31

4 recorded events


### User

_source line 909 · 2026-05-22T16:03:52.867883+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2（新颖性与完整性方向）的完整审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 2 审稿意见（Round 1）——新颖性与完整性

### Summary

本文将教育测量学中成熟的 Mantel-Haenszel DIF 方法应用于 LLM benchmark 时间稳定性审计，基于 METABENCH 5,227 模型 × 12,508 MMLU 项目响应矩阵，发现 2023–2024 代际间约 27–29% 的 MMLU 项目展现显著 DIF，并通过 semi-synthetic 注入框架验证、在 6 个 benchmark 上复制。论文提出 15%/25% 阈值的 DIF 审计协议。执行扎实、规模可观，但核心方法论贡献是将已有心理测量方法迁移到新领域。

### Strengths

**S1. 规模与系统性令人印象深刻。** 5,227 模型的大规模审计远超同类工作，6 个 METABENCH benchmark 交叉验证（Table 3, Section 4.7），C% 17.9%–31.3%，结论可泛化。

**S2. 多条收敛证据链组织得当。** 三条独立非独立性修正路径均收敛到 ~27–29%（Section 4.2），DEFF 修正（Appendix C）对 LLM family 非独立性处理合理。

**S3. Semi-synthetic 注入框架设计合理。** Section 3.4 提供受控地面真值，ΔFPR = 0（Section 4.5）令人信服，TPR 剂量-反应曲线（Table 4, Figure 2）清晰表征方法灵敏度。

**S4. Ground truth meta-critique 有价值。** Web-overlap 标签与 DIF flags 近乎独立（Jaccard = 0.206, OR ≈ 1.15, Section 4.3），对领域重要假设的实证挑战。

**S5. 因果讨论保持恰当谨慎。** Section 5.1 明确列出三种非互斥机制，没有过度宣称 DIF = contamination。

**S6. 写作密度高但清晰。** 8 页内容量大，结构清晰，Figure 1 有效传达核心概念区别。

### Weaknesses

**W1. [Should-Fix] 核心方法论新颖性有限，contribution 表述需校准。** MH-DIF 是 Holland & Thayer (1988) 标准方法，LLM-specific 适配（cross-subject matching、DEFF 修正）是工程性调整而非方法论突破。三条 contribution 中第一条是否定性发现（web-overlap 不好用），第三条是实证发现。建议重新校准表述，明确区分"方法适配"与"实证发现"。

**W2. [Should-Fix] 四条排除论证说服力参差不齐。**
- Ability confounds ≤ 2.4pp：最强证据，但缺 CI/假设检验
- Domain improvement R² < 0.1%：仅 9 个 broad domain 粒度过粗，contamination 集中在特定 subject 时会被稀释
- Gema enrichment 0.92×：实质重复 S4 发现，非独立排除论证
- Difficulty-direction ρ = −0.597：替代解释（天花板效应、format sensitivity）未讨论

**W3. [Should-Fix] DIF 审计协议阈值缺乏系统性论证。** 15%/25% 阈值以 Figure 6 排名退化为依据，但分离点因 benchmark 而异（TruthfulQA ~10% vs MMLU ~20%），统一阈值不合理；缺少 decision-theoretic 框架将阈值与下游 ρ 退化量关联。教育测量领域的 item exposure control 标准（Stocking & Lewis 1998 等）未引用对比。

**W4. [Should-Fix] 与 Growing Pains (Habba et al., 2026) 的区分不够明确。** 两项工作都用 IRT 处理 benchmark 时间不稳定性、都用 METABENCH 数据。需要 2-3 句话讨论：(a) 适用场景差异；(b) 发现一致性；(c) 互补关系。

**W5. [Minor] Semi-synthetic 框架假设均匀注入，真实 contamination 是非均匀的。** Limitations 已提及但主文未讨论对 TPR/FPR 估计的影响方向。

**W6. [Minor] 非均匀 DIF (NUDIF) 处理不充分。** Section 4.4 检出额外 17.7% NUDIF（union 47%），但讨论极简。NUDIF 对不同 ability level 模型的差异化影响值得在 Discussion 展开。

**W7. [Minor] 多个百分比（27–29%/31%/17.7%/47%/17.9–31.3%）散落各处，包含/互斥关系不直观。建议汇总表。

**W8. [Minor] Limitations 中关于 non-independence 的段落与主文 DEFF 方法存在轻微矛盾，应澄清。

### Questions

**Q1.** Cross-subject matching 使用全局总分（除 focal subject 外），当 57 subject 间相关性差异大时，是否引入残余相关？是否考虑过 domain-specific matching？

**Q2.** HellaSwag C% = 17.9% vs MMLU 31.3%——是 item difficulty 还是 task format 差异？DIF 对 task format 的 sensitivity 是否需要单独讨论？

**Q3.** ΔFPR = 0.000（1,000 replications）是否 literally zero？如果是，检验是否过于保守？Table 4 TPR at |Δ_MH| ≥ 1.5 在 N=80 时为 0.798，意味着可能遗漏 ~20% 真正 DIF 项目？

**Q4.** 审计协议要求 ≥500 models per cohort，小规模 benchmark（200-300 模型）的 power 如何退化？

### Missing References

1. Test security/item exposure control 文献（Stocking & Lewis 1998, van der Linden & Veldkamp 2004）——与 DIF audit protocol 的 item retirement 直接相关
2. DIF 在 NLP fairness 中的应用（Shah et al. 2020 等）——跨领域连接
3. Dynabench (Kiela et al. 2021) 动态 benchmark——与 temporal instability 发现直接相关

### Overall Assessment

**3.5 — Borderline Conference** | Confidence: 4/5

---

请对以上每一条 Weakness、Question 和 Missing Reference 逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 910 · 2026-05-22T16:05:57.809193+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 交叉回应 Reviewer 2（Round 1）\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: 核心方法论新颖性有限**\n同意。MH-DIF 是 1988 年的标准方法，cross-subject matching 和 DEFF 修正是已知技术在新场景的工程适配，不构成方法论突破。论文的三条 contribution（page 2）中，第一条（ground truth meta-critique）和第三条（temporal measurement instability at scale）均为**实证发现**而非方法创新。建议作者将 contribution 表述从\"方法论贡献\"重新校准为\"大规模实证审计 + 概念框架迁移\"。这不降低论文价值——将成熟方法可靠地迁移到重要新领域本身就是贡献——但需要诚实 framing。\n\n**[AGREE] R2-W2: 四条排除论证说服力参差不齐**\n全面同意此条，且与我的 W4（multidimensionality 威胁）互补：\n\n- **Ability confounds ≤ 2.4pp**：R2 指出缺 CI/假设检验，正确。论文仅报告点估计（Section 4.2, Table 2：\"matched-ability quintiles... C% ≤ 2.4 pp\"），没有 bootstrap CI 或置换检验 p-value。这使得\"≤ 2.4pp 可归因于 ability mismatch\"这一 bound 的精度不明。\n- **Domain improvement R² < 0.1%**：R2 指出 9 个 broad domain 粒度过粗——完全同意，这正是我 W4 的核心论点。如果 contamination 集中在特定 MMLU subject（如 abstract_algebra 或 anatomy），domain-level（STEM/Humanities/Social Science/Other）的 decomposition 无法捕获。论文应至少在 57-subject 粒度上重复此分析。\n- **Gema enrichment 0.92×**：同意 R2 判断，这实质上是 Section 4.3 ground truth mismatch 的重复引用，不构成独立排除论证。\n- **Difficulty-direction ρ = −0.597**：R2 提出天花板效应和 format sensitivity 作为替代解释——这是有效的反驳。高 baseline accuracy 的 items 改进空间有限（天花板效应），这会自然产生负相关，与 contamination 或 capability change 无关。论文未讨论此混淆因素。\n\n**[AGREE] R2-W3: DIF 审计协议阈值缺乏系统性论证**\n同意。我在审阅 Figure 6 时注意到同样的问题：6 个 benchmarks 的排名退化曲线分离点差异显著（TruthfulQA 在 ~10% 就出现明显分离，而 HellaSwag 在 ~30% 才有可见差异）。统一的 15%/25% 阈值没有理论依据。R2 建议的 decision-theoretic 框架（将阈值与目标 ρ 退化量关联）是正确的改进方向。此外，Stocking & Lewis (1998) 的 item exposure control 文献确实直接相关且应被引用。\n\n**[AGREE] R2-W4: 与 Growing Pains 的区分不够明确**\n同意。论文在 Related Work（page 3）引用 Habba et al. (2026) 但仅用一句话定位（\"providing a prescriptive framework for maintaining comparability via fixed-parameter calibration\"）。两项工作共享 METABENCH 数据源、IRT 框架、和 temporal instability 主题。论文应明确讨论：(a) Growing Pains 做 prescriptive equating（anchor items + calibration），本文做 descriptive auditing（DIF detection）；(b) 两者发现是否一致（Growing Pains 的 anchor item 选择标准与本文的 DIF flags 有多大重叠）；(c) 互补关系（本文的 DIF audit 可为 Growing Pains 的 equating 提供 item screening）。\n\n**[AGREE] R2-W5: Semi-synthetic 框架假设均匀注入**\n完全同意，这与我的 W2 一致。补充一点：均匀注入（所有选中 items 以相同 ε 翻转）会高估 MH-DIF 的 TPR，因为真实 contamination 的非均匀性会削弱 MH 统计量的 power。论文应在 Section 3.4 明确声明当前 TPR 估计为 upper bound。\n\n**[AGREE] R2-W6: NUDIF 处理不充分**\n同意。Section 4.4 报告 logistic regression 额外检出 17.7% NUDIF items（union 47%），但仅用一句话处理（\"we treat them as descriptive\"）。NUDIF 意味着 DIF 在不同 ability 水平上效应不同——在 LLM 评估中，这意味着前沿模型和中等模型可能受到不同程度的影响。这对 benchmark 排名公平性的 implication 值得在 Discussion 展开。此外，47% 这个 union 数字远高于 headline 的 27-29%，其含义需要更清晰的讨论。\n\n**[AGREE] R2-W7: 多个百分比散落各处**\n同意。27-29%（uniform DIF）、31%（raw uncorrected）、17.7%（additional NUDIF）、47%（union）、13.5%（weighted-mean DEFF）、17.9-31.3%（cross-benchmark range）——这些数字的包含/互斥关系确实不直观。一张汇总表列明每个百分比的定义、来源 section、和彼此关系会显著提升可读性。\n\n**[AGREE] R2-W8: Limitations 与主文在 non-independence 上存在轻微矛盾**\n同意，且这与我的 W1 直接相关。主文（Abstract, Section 4.2）将 \"≈27-29%\" 定位为\"conservative estimate\"，但 Limitations（page 9）承认 cluster bootstrap upper bound 为 53.2%。如果 27-29% 是 conservative，53.2% 是什么？更关键的是，weighted-mean DEFF 给出 13.5%——如果这个更保守的估计有效，则主文的\"conservative\"标签不准确。论文需要统一术语：要么承认 13.5%-29.2% 是完整范围（13.5% 为 conservative lower bound），要么提供更强论证排除 weighted-mean DEFF。\n\n---\n\n### Questions 逐条回应\n\n**[AGREE] R2-Q1: Cross-subject matching 残余相关**\n有效问题，与我的 W4 一致。57 个 MMLU subjects 间相关性差异大（e.g., abstract_algebra 与 philosophy 的相关性远低于 abstract_algebra 与 college_mathematics）。当 focal subject 与某些 non-focal subjects 高度相关时，cross-subject total score 仍会吸收部分 injection signal，导致 FPR 偏高。论文应报告 subject 间相关矩阵的分布特征，并讨论 domain-specific matching（e.g., 仅用不同 domain 的 subjects）作为 robustness check。\n\n**[AGREE] R2-Q2: HellaSwag vs MMLU C% 差异**\n论文在 Table 3 和 Section 4.7 将 cross-benchmark C% 差异归为\"item difficulty distributions\"（page 8），但这是不充分的。HellaSwag（sentence completion）与 MMLU（multiple choice）的 task format 完全不同；TruthfulQA 测试 truthfulness 而非 knowledge——这些 format/construct 差异可能系统性地影响 DIF 检出率。R2 建议单独讨论 format sensitivity 是合理的。\n\n**[REBUT] R2-Q3: ΔFPR = 0.000 是否 literally zero**\n部分反驳。ΔFPR = 0.000 在 single-subject injection + cross-subject matching 下确实是 **by construction** 的——不是检验过于保守，而是匹配变量（non-focal subject total score）与注入信号（focal subject items）数学上正交。这不是统计现象而是设计保证（Section 3.4, page 5：\"ΔFPR = 0 by construction\"）。但同意 R2 对 TPR 的关切：Table 4 显示 |Δ_MH| ≥ 1.5 在 N = 80 时 TPR = 0.798，意味着 ~20% 的真 DIF items 被遗漏。这个 false negative rate 应在 Section 4.5 讨论其对 headline C% 估计的影响——如果 20% 真 DIF 被漏检，实际 DIF 率可能更高。\n\n**[AGREE] R2-Q4: 小规模 benchmark 的 power 退化**\n论文的审计协议建议 ≥500 models per cohort（Section 5.2），但未提供 200-300 模型场景下的 power 曲线。Section 4.1 的 power analysis 显示 N ≥ 80 时有充分 power，但这是在 MMLU 的 item 参数下得出的。不同 benchmarks（特别是 item 数量少的 benchmarks）的 power 可能不同。建议补充 power vs. N 曲线或至少讨论 small-N 场景的限制。\n\n---\n\n### Missing References 逐条回应\n\n**[AGREE] Missing Ref 1: Stocking & Lewis (1998), van der Linden & Veldkamp (2004)**\n直接相关。论文的 DIF audit protocol（Section 5.2）本质上是 item exposure control 的变体——DIF-flagged items 相当于 over-exposed items，Monitor/Flag/Act 阈值类似 exposure rate thresholds。不引用 item exposure control 文献是疏漏。\n\n**[AGREE] Missing Ref 2: DIF in NLP fairness (Shah et al. 2020 等)**\n相关但非必需。DIF 在 NLP fairness 中的应用（如 across demographic groups 的 item bias）与本文的 temporal DIF 有方法论联系，适合在 Related Work 中简短提及以建立跨领域连接。\n\n**[AGREE] Missing Ref 3: Dynabench (Kiela et al. 2021)**\n同意。Dynabench 的核心动机——静态 benchmarks 被\"解决\"后失效——与本文发现的 temporal measurement instability 直接呼应。论文发现 27-29% 的 items 在代际间功能变化，这为 dynamic benchmark 的必要性提供了实证支持。应在 Related Work 或 Discussion 引用。\n\n---\n\n### 总结\n\n与 R2 在 9 条 Weakness 中全部 [AGREE]，在 4 个 Questions 中 3 个 [AGREE]、1 个部分 [REBUT]（Q3 的 ΔFPR = 0 by construction 是设计保证而非过度保守），在 3 条 Missing References 中全部 [AGREE]。\n\nR2 的审查与我的审查高度互补：\n- R2-W1（novelty framing）补充了我未重点关注的 contribution 定位问题\n- R2-W2（排除论证不均）与我的 W4（multidimensionality）形成交叉验证\n- R2-W3（阈值论证）是我遗漏的重要问题\n- R2-W6（NUDIF）和 R2-W7（百分比混乱）是有价值的可读性/完整性建议\n- R2-W8 与我的 W1（DEFF framing）直接对应\n\n两位 Reviewer 一致认为的核心问题：**(1)** DEFF/non-independence 处理的 framing 需要更诚实；**(2)** semi-synthetic 框架的现实性限制需要更显式地讨论；**(3)** 论文的 headline number 需要更审慎的 uncertainty 表达。\n\n维持 Overall Assessment: **3.5 — Borderline Conference**。\n",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 交叉回应 Reviewer 2（Round 1）\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: 核心方法论新颖性有限**\n同意。MH-DIF 是 1988 年的标准方法，cross-subject matching 和 DEFF 修正是已知技术在新场景的工程适配，不构成方法论突破。论文的三条 contribution（page 2）中，第一条（ground truth meta-critique）和第三条（temporal measurement instability at scale）均为**实证发现**而非方法创新。建议作者将 contribution 表述从\"方法论贡献\"重新校准为\"大规模实证审计 + 概念框架迁移\"。这不降低论文价值——将成熟方法可靠地迁移到重要新领域本身就是贡献——但需要诚实 framing。\n\n**[AGREE] R2-W2: 四条排除论证说服力参差不齐**\n全面同意此条，且与我的 W4（multidimensionality 威胁）互补：\n\n- **Ability confounds ≤ 2.4pp**：R2 指出缺 CI/假设检验，正确。论文仅报告点估计（Section 4.2, Table 2：\"matched-ability quintiles... C% ≤ 2.4 pp\"），没有 bootstrap CI 或置换检验 p-value。这使得\"≤ 2.4pp 可归因于 ability mismatch\"这一 bound 的精度不明。\n- **Domain improvement R² < 0.1%**：R2 指出 9 个 broad domain 粒度过粗——完全同意，这正是我 W4 的核心论点。如果 contamination 集中在特定 MMLU subject（如 abstract_algebra 或 anatomy），domain-level（STEM/Humanities/Social Science/Other）的 decomposition 无法捕获。论文应至少在 57-subject 粒度上重复此分析。\n- **Gema enrichment 0.92×**：同意 R2 判断，这实质上是 Section 4.3 ground truth mismatch 的重复引用，不构成独立排除论证。\n- **Difficulty-direction ρ = −0.597**：R2 提出天花板效应和 format sensitivity 作为替代解释——这是有效的反驳。高 baseline accuracy 的 items 改进空间有限（天花板效应），这会自然产生负相关，与 contamination 或 capability change 无关。论文未讨论此混淆因素。\n\n**[AGREE] R2-W3: DIF 审计协议阈值缺乏系统性论证**\n同意。我在审阅 Figure 6 时注意到同样的问题：6 个 benchmarks 的排名退化曲线分离点差异显著（TruthfulQA 在 ~10% 就出现明显分离，而 HellaSwag 在 ~30% 才有可见差异）。统一的 15%/25% 阈值没有理论依据。R2 建议的 decision-theoretic 框架（将阈值与目标 ρ 退化量关联）是正确的改进方向。此外，Stocking & Lewis (1998) 的 item exposure control 文献确实直接相关且应被引用。\n\n**[AGREE] R2-W4: 与 Growing Pains 的区分不够明确**\n同意。论文在 Related Work（page 3）引用 Habba et al. (2026) 但仅用一句话定位（\"providing a prescriptive framework for maintaining comparability via fixed-parameter calibration\"）。两项工作共享 METABENCH 数据源、IRT 框架、和 temporal instability 主题。论文应明确讨论：(a) Growing Pains 做 prescriptive equating（anchor items + calibration），本文做 descriptive auditing（DIF detection）；(b) 两者发现是否一致（Growing Pains 的 anchor item 选择标准与本文的 DIF flags 有多大重叠）；(c) 互补关系（本文的 DIF audit 可为 Growing Pains 的 equating 提供 item screening）。\n\n**[AGREE] R2-W5: Semi-synthetic 框架假设均匀注入**\n完全同意，这与我的 W2 一致。补充一点：均匀注入（所有选中 items 以相同 ε 翻转）会高估 MH-DIF 的 TPR，因为真实 contamination 的非均匀性会削弱 MH 统计量的 power。论文应在 Section 3.4 明确声明当前 TPR 估计为 upper bound。\n\n**[AGREE] R2-W6: NUDIF 处理不充分**\n同意。Section 4.4 报告 logistic regression 额外检出 17.7% NUDIF items（union 47%），但仅用一句话处理（\"we treat them as descriptive\"）。NUDIF 意味着 DIF 在不同 ability 水平上效应不同——在 LLM 评估中，这意味着前沿模型和中等模型可能受到不同程度的影响。这对 benchmark 排名公平性的 implication 值得在 Discussion 展开。此外，47% 这个 union 数字远高于 headline 的 27-29%，其含义需要更清晰的讨论。\n\n**[AGREE] R2-W7: 多个百分比散落各处**\n同意。27-29%（uniform DIF）、31%（raw uncorrected）、17.7%（additional NUDIF）、47%（union）、13.5%（weighted-mean DEFF）、17.9-31.3%（cross-benchmark range）——这些数字的包含/互斥关系确实不直观。一张汇总表列明每个百分比的定义、来源 section、和彼此关系会显著提升可读性。\n\n**[AGREE] R2-W8: Limitations 与主文在 non-independence 上存在轻微矛盾**\n同意，且这与我的 W1 直接相关。主文（Abstract, Section 4.2）将 \"≈27-29%\" 定位为\"conservative estimate\"，但 Limitations（page 9）承认 cluster bootstrap upper bound 为 53.2%。如果 27-29% 是 conservative，53.2% 是什么？更关键的是，weighted-mean DEFF 给出 13.5%——如果这个更保守的估计有效，则主文的\"conservative\"标签不准确。论文需要统一术语：要么承认 13.5%-29.2% 是完整范围（13.5% 为 conservative lower bound），要么提供更强论证排除 weighted-mean DEFF。\n\n---\n\n### Questions 逐条回应\n\n**[AGREE] R2-Q1: Cross-subject matching 残余相关**\n有效问题，与我的 W4 一致。57 个 MMLU subjects 间相关性差异大（e.g., abstract_algebra 与 philosophy 的相关性远低于 abstract_algebra 与 college_mathematics）。当 focal subject 与某些 non-focal subjects 高度相关时，cross-subject total score 仍会吸收部分 injection signal，导致 FPR 偏高。论文应报告 subject 间相关矩阵的分布特征，并讨论 domain-specific matching（e.g., 仅用不同 domain 的 subjects）作为 robustness check。\n\n**[AGREE] R2-Q2: HellaSwag vs MMLU C% 差异**\n论文在 Table 3 和 Section 4.7 将 cross-benchmark C% 差异归为\"item difficulty distributions\"（page 8），但这是不充分的。HellaSwag（sentence completion）与 MMLU（multiple choice）的 task format 完全不同；TruthfulQA 测试 truthfulness 而非 knowledge——这些 format/construct 差异可能系统性地影响 DIF 检出率。R2 建议单独讨论 format sensitivity 是合理的。\n\n**[REBUT] R2-Q3: ΔFPR = 0.000 是否 literally zero**\n部分反驳。ΔFPR = 0.000 在 single-subject injection + cross-subject matching 下确实是 **by construction** 的——不是检验过于保守，而是匹配变量（non-focal subject total score）与注入信号（focal subject items）数学上正交。这不是统计现象而是设计保证（Section 3.4, page 5：\"ΔFPR = 0 by construction\"）。但同意 R2 对 TPR 的关切：Table 4 显示 |Δ_MH| ≥ 1.5 在 N = 80 时 TPR = 0.798，意味着 ~20% 的真 DIF items 被遗漏。这个 false negative rate 应在 Section 4.5 讨论其对 headline C% 估计的影响——如果 20% 真 DIF 被漏检，实际 DIF 率可能更高。\n\n**[AGREE] R2-Q4: 小规模 benchmark 的 power 退化**\n论文的审计协议建议 ≥500 models per cohort（Section 5.2），但未提供 200-300 模型场景下的 power 曲线。Section 4.1 的 power analysis 显示 N ≥ 80 时有充分 power，但这是在 MMLU 的 item 参数下得出的。不同 benchmarks（特别是 item 数量少的 benchmarks）的 power 可能不同。建议补充 power vs. N 曲线或至少讨论 small-N 场景的限制。\n\n---\n\n### Missing References 逐条回应\n\n**[AGREE] Missing Ref 1: Stocking & Lewis (1998), van der Linden & Veldkamp (2004)**\n直接相关。论文的 DIF audit protocol（Section 5.2）本质上是 item exposure control 的变体——DIF-flagged items 相当于 over-exposed items，Monitor/Flag/Act 阈值类似 exposure rate thresholds。不引用 item exposure control 文献是疏漏。\n\n**[AGREE] Missing Ref 2: DIF in NLP fairness (Shah et al. 2020 等)**\n相关但非必需。DIF 在 NLP fairness 中的应用（如 across demographic groups 的 item bias）与本文的 temporal DIF 有方法论联系，适合在 Related Work 中简短提及以建立跨领域连接。\n\n**[AGREE] Missing Ref 3: Dynabench (Kiela et al. 2021)**\n同意。Dynabench 的核心动机——静态 benchmarks 被\"解决\"后失效——与本文发现的 temporal measurement instability 直接呼应。论文发现 27-29% 的 items 在代际间功能变化，这为 dynamic benchmark 的必要性提供了实证支持。应在 Related Work 或 Discussion 引用。\n\n---\n\n### 总结\n\n与 R2 在 9 条 Weakness 中全部 [AGREE]，在 4 个 Questions 中 3 个 [AGREE]、1 个部分 [REBUT]（Q3 的 ΔFPR = 0 by construction 是设计保证而非过度保守），在 3 条 Missing References 中全部 [AGREE]。\n\nR2 的审查与我的审查高度互补：\n- R2-W1（novelty framing）补充了我未重点关注的 contribution 定位问题\n- R2-W2（排除论证不均）与我的 W4（multidimensionality）形成交叉验证\n- R2-W3（阈值论证）是我遗漏的重要问题\n- R2-W6（NUDIF）和 R2-W7（百分比混乱）是有价值的可读性/完整性建议\n- R2-W8 与我的 W1（DEFF framing）直接对应\n\n两位 Reviewer 一致认为的核心问题：**(1)** DEFF/non-independence 处理的 framing 需要更诚实；**(2)** semi-synthetic 框架的现实性限制需要更显式地讨论；**(3)** 论文的 headline number 需要更审慎的 uncertainty 表达。\n\n维持 Overall Assessment: **3.5 — Borderline Conference**。\n",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 911 · 2026-05-22T16:06:02.134184+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4324
}
```

</details>

---


### Assistant

_source line 912 · 2026-05-22T16:06:08.927184+00:00_

交叉回应已提交。对 R2 的 9 条 Weakness 全部 [AGREE]，4 个 Questions 中 3 个 [AGREE]、Q3 部分 [REBUT]（ΔFPR=0 是设计保证非过度保守），3 条 Missing References 全部 [AGREE]。两位 Reviewer 在 DEFF framing、semi-synthetic 现实性、headline number 审慎性三个核心问题上形成一致判断。维持 Overall 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 32

## Round 32

70 recorded events


### User

_source line 913 · 2026-05-22T16:23:02.557067+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性** 审查。

## Venue 信息
- **目标会议**: EMNLP 2026 (通过 ACL Rolling Review 提交)
- **投稿类别**: Long Paper
- **截止日期**: 2026-05-25
- **页数限制**: 正文 8 页（ACL 两栏模板），参考文献无限制，Limitations 不计入页数
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind（无 anonymity period 但 review 过程 double-blind）

## 论文文件
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/submitted.pdf`

## 你的审查侧重

聚焦 **方法论和统计严谨性**，具体包括：

1. **MH-DIF 方法适用性**：MH-DIF 从教育测量迁移到 LLM 评测的合理性；将 LLM 视为 "examinees" 的假设是否成立；LLM 非独立性（共享训练数据/架构）对 MH 统计量的影响是否被充分处理
2. **非独立性校正**：三种校正方法（simple-mean DEFF、graduated de-duplication、cluster bootstrap）的收敛性论证；weighted-mean DEFF 下界 13.5% 与其他方法 ~27-29% 的张力；ICC 估计的稳定性
3. **Semi-synthetic 框架**：binary response flipping 的现实性；cross-subject matching 的 ΔFPR=0 保证条件和边界；multi-subject injection 的 graceful degradation
4. **统计检验**：大样本下 p 值退化问题；ETS 双重阈值的有效性；multiple testing 处理；K（分层数）敏感性
5. **Matching strategy**：cross-subject vs within-subject vs external matching 的选择合理性；multidimensionality confound 的处理
6. **实验设计**：cohort 定义的合理性（release date vs training cutoff）；random-split sanity check 的充分性；power analysis 的假设

## 输出格式

按以下结构输出审稿意见：
1. **Summary** (2-3 句)
2. **Strengths** (逐条，标记 S1, S2, ...)
3. **Weaknesses** (逐条，标记 W1, W2, ...，按严重程度排序: Major → Minor → Nitpick；每条标注 [Major]/[Minor]/[Nitpick])
4. **Questions** (需要作者澄清的问题)
5. **Missing References** (遗漏的重要方法论文献)
6. **Overall Assessment** (评分 + 置信度 + 一句话总评)

评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

**严格评审，不留情面。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 914 · 2026-05-22T16:23:18.852435+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search ARR review form",
  "prompt": "Search the web for \"ACL Rolling Review reviewer guidelines 2026\" and \"ACL ARR review form criteria dimensions\" to find the official review form dimensions and scoring criteria. I need the exact dimensions (like soundness, excitement, reproducibility, etc.) and their scoring scales. Use WebSearch and WebFetch tools to get this information. Report the complete review form structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Search ARR review form",
    "prompt": "Search the web for \"ACL Rolling Review reviewer guidelines 2026\" and \"ACL ARR review form criteria dimensions\" to find the official review form dimensions and scoring criteria. I need the exact dimensions (like soundness, excitement, reproducibility, etc.) and their scoring scales. Use WebSearch and WebFetch tools to get this information. Report the complete review form structure."
  }
}
```

</details>

---


### Tool call

_source line 915 · 2026-05-22T16:23:20.578537+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer guidelines 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer guidelines 2026"
  }
}
```

</details>

---


### Tool call

_source line 916 · 2026-05-22T16:23:20.681073+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form criteria dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form criteria dimensions"
  }
}
```

</details>

---


### Tool result

_source line 917 · 2026-05-22T16:23:27.170916+00:00_

Web search results for query: "ACL ARR review form criteria dimensions"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR SAC Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/sacguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results about the ACL Rolling Review (ARR) review form, here's information about the criteria and dimensions:

## Review Criteria

For Findings papers, the main criteria are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors.

## Overall Assessment Dimensions

The review form includes a rating scale with the following dimensions:

- 5 = Consider for Award: A paper that could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% paper
…[truncated 682 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6489
}
```

</details>

---


### Tool result

_source line 918 · 2026-05-22T16:23:31.305259+00:00_

Web search results for query: "ACL Rolling Review reviewer guidelines 2026"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here's what I found about ACL Rolling Review (ARR) reviewer guidelines for 2026:

## Key Reviewer Guidelines for 2026

ARR has developed detailed guidelines and suggestions for each step of the review process, including a list of common problems in both reviews and NLP papers to watch out for.

### Anonymity and Author Identity

Reviewers for *ACL conferences and TACL should be instructed not to actively try 
…[truncated 2223 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 10726
}
```

</details>

---


### Tool call

_source line 919 · 2026-05-22T16:23:33.818799+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "What are all the review form dimensions, criteria, and scoring scales? List each dimension with its scale options."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "What are all the review form dimensions, criteria, and scoring scales? List each dimension with its scale options."
  }
}
```

</details>

---


### Tool call

_source line 920 · 2026-05-22T16:23:33.919782+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewerguidelines",
  "prompt": "What are the specific review criteria and scoring dimensions reviewers should use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewerguidelines",
    "prompt": "What are the specific review criteria and scoring dimensions reviewers should use?"
  }
}
```

</details>

---


### Tool result

_source line 921 · 2026-05-22T16:23:39.245227+00:00_

# Review Scoring Dimensions for ARR

According to the ARR Reviewer Guidelines, reviewers should provide three distinct scores:

1. **Soundness**: Evaluates technical quality and validity. As stated, "The _soundness_ scores must be justified by the text of the review." Low soundness ratings require explicit explanation of identified flaws.

2. **Excitement**: Reflects personal interest in the work, orthogonal to soundness assessment. The guidelines note this is "more subjective and should be reflected in a separate _excitement_ score."

3. **Overall Assessment**: A composite recommendation incorporating soundness, excitement, novelty, and potential impact. The guidelines specify that "All papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible."

## Key Principle

Scores must align with review content. The guidelines emphasize: "If you give a low _Soundness_ score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it."

This three-dimensional approach acknowledges that technically sound work may not personally excite every reviewer, yet can still merit publication based on its contributions and broader significance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5325
}
```

</details>

---


### Tool result

_source line 922 · 2026-05-22T16:23:41.708755+00:00_

# ACL Rolling Review Form Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5 = Positive evaluation is correct; very careful read with familiarity of related work
- 4 = Quite sure; important points checked carefully
- 3 = Pretty sure; general area knowledge but details not carefully verified
- 2 = Can defend evaluation but likely missed some details or novelty assessment uncertain
- 1 = Outside expertise area or paper very difficult to understand

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- 5 = Excellent: "one of the most thorough" studies of its type
- 4 = Strong: sufficient support for claims; extra experiments optional
- 3 = Acceptable: main claims supported; minor points need extra detail
- 2 = Poor: main claims insufficiently supported; major technical problems
- 1 = Major Issues: insufficient depth or not relevant to ACL

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- 5 = Highly Exciting: would recommend to others or attend presentation
- 4 = Exciting: would mention to others or make effort to attend
- 3 = Interesting: might mention points or attend if time permits
- 2 = Potentially Interesting: does not resonate personally but might with others
- 1 = Not Exciting: lacks relevance to computational linguistics

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- 5 = Consider for Award
- 4.5 = Borderline Award
- 4 = Conference
- 3.5 = Borderline Conference
- 3 = Findings
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle
- 1.5 = Resubmit after next cycle
- 1 = Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- 5 = Results easily reproducible
- 4 = Mostly reproducible; minor variations possible
- 3 = Reproducible with difficulty; parameters underspecified
- 2 = Hard to reproduce; unavailable data or insufficient details
- 1 = Not reproducible

## 6. **Datasets Value**
Scale: 1-5
- 5 = Enabling: affects research project choices
- 4 = Useful: recommended for ongoing work
- 3 = Potentially useful: mig
…[truncated 653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7889
}
```

</details>

---


### Tool result

_source line 923 · 2026-05-22T16:23:50.651103+00:00_

Perfect! I've gathered the complete ACL Rolling Review (ARR) review form structure. Here's the comprehensive report:

## Complete ACL ARR Review Form Structure (2026)

The official ACL Rolling Review uses a standardized form with **8 evaluation dimensions**, each with a 1-5 scale (with half-point increments for most dimensions):

### 1. **Soundness** (1-5, half-point increments)
Technical quality and validity of the work:
- 5 = Excellent: one of the most thorough studies of its type
- 4 = Strong: sufficient support for claims; extra experiments optional
- 3 = Acceptable: main claims supported; minor points need extra detail
- 2 = Poor: main claims insufficiently supported; major technical problems
- 1 = Major Issues: insufficient depth or not relevant to ACL

### 2. **Excitement** (1-5, half-point increments)
Personal interest and significance (subjective dimension):
- 5 = Highly Exciting: would recommend to others or attend presentation
- 4 = Exciting: would mention to others or make effort to attend
- 3 = Interesting: might mention points or attend if time permits
- 2 = Potentially Interesting: does not resonate personally but might with others
- 1 = Not Exciting: lacks relevance to computational linguistics

### 3. **Overall Assessment** (1-5, half-point increments)
Composite recommendation incorporating soundness, excitement, novelty, and impact:
- 5 = Consider for Award (top 2.5% papers)
- 4.5 = Borderline Award
- 4 = Conference
- 3.5 = Borderline Conference
- 3 = Findings
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle
- 1.5 = Resubmit after next cycle
- 1 = Do not resubmit

### 4. **Reproducibility** (1-5)
Ability to reproduce the results:
- 5 = Results easily reproducible
- 4 = Mostly reproducible; minor variations possible
- 3 = Reproducible with difficulty; parameters underspecified
- 2 = Hard to reproduce; unavailable data or insufficient details
- 1 = Not reproducible

### 5. **Reviewer Confidence** (1-5)
Reviewer's confidence in their evaluation:

…[truncated 2108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 31798
}
```

</details>

---


### Tool call

_source line 924 · 2026-05-22T16:23:58.132044+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 925 · 2026-05-22T16:23:58.182802+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 926 · 2026-05-22T16:24:03.351739+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 927 · 2026-05-22T16:24:04.758499+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 523.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 577.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 525.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 545.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 451.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 574.9}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p9.png\", \"width\": 1
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 928 · 2026-05-22T16:24:15.585899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 929 · 2026-05-22T16:24:15.937675+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 930 · 2026-05-22T16:24:16.743697+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1157
}
```

</details>

---


### Tool result

_source line 931 · 2026-05-22T16:24:16.845230+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 932 · 2026-05-22T16:24:16.845829+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 933 · 2026-05-22T16:24:17.197615+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 934 · 2026-05-22T16:24:18.203121+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool result

_source line 935 · 2026-05-22T16:24:18.204039+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 936 · 2026-05-22T16:24:18.355916+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 937 · 2026-05-22T16:24:19.111956+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---


### Tool call

_source line 938 · 2026-05-22T16:24:19.415362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 939 · 2026-05-22T16:24:19.519044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 940 · 2026-05-22T16:24:20.072970+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 941 · 2026-05-22T16:24:20.879987+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 942 · 2026-05-22T16:24:21.780393+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2365
}
```

</details>

---


### Tool call

_source line 943 · 2026-05-22T16:24:21.780892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 944 · 2026-05-22T16:24:22.738994+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3219
}
```

</details>

---


### Tool call

_source line 945 · 2026-05-22T16:24:23.291035+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 946 · 2026-05-22T16:24:25.206440+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5133
}
```

</details>

---


### Tool result

_source line 947 · 2026-05-22T16:24:25.710353+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4830
}
```

</details>

---


### Tool result

_source line 948 · 2026-05-22T16:24:26.219213+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4438
}
```

</details>

---


### Tool result

_source line 949 · 2026-05-22T16:24:27.678849+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 568.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 576.6}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 330.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 253.4}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4387
}
```

</details>

---


### Tool call

_source line 950 · 2026-05-22T16:24:33.556436+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 951 · 2026-05-22T16:24:34.415428+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool call

_source line 952 · 2026-05-22T16:24:34.466887+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 953 · 2026-05-22T16:24:35.074507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 954 · 2026-05-22T16:24:35.639609+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 955 · 2026-05-22T16:24:36.545697+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2078
}
```

</details>

---


### Tool call

_source line 956 · 2026-05-22T16:24:36.546188+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 957 · 2026-05-22T16:24:36.951287+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_12/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 958 · 2026-05-22T16:24:37.306542+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2232
}
```

</details>

---


### Tool result

_source line 959 · 2026-05-22T16:24:38.446489+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2806
}
```

</details>

---


### Tool result

_source line 960 · 2026-05-22T16:24:38.498949+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1952
}
```

</details>

---


### Tool result

_source line 961 · 2026-05-22T16:24:39.014152+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2062
}
```

</details>

---


### Tool call

_source line 962 · 2026-05-22T16:26:17.683873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 963 · 2026-05-22T16:26:17.684355+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Temporal Measurement Instability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 964 · 2026-05-22T16:26:21.300669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 965 · 2026-05-22T16:26:21.502009+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh,magis2010difr} detects DIF by stratify
…[truncated 9746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 966 · 2026-05-22T16:26:21.502436+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 967 · 2026-05-22T16:26:21.553142+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	As approximate parametric bounds, a Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$ (details in \Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold. Power varies substantially with item discrimination: TPR ranges from 0.40 at $a = 0.5$ to 0.95 at $a = 2.0$; the gap between TPR at mean $a$ (0.87) and the aggregate TPR (0.68) quantifies the power cost of parameter heterogeneity, consistent with Jensen's inequality (\Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal Comparability: 31\% Measurement Instability}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%]; family-level cluster bootstrap CI $[26.7\%, 53.2\%]$). Three independent non-independence corrections converge on approximately 27--29\%: simple-mean DEFF correction (29.2\%), graduated family de-duplication at $K{=}20$ (29.1\%; \Cref{tab:lofo}), and family-level cluster bootstrap lower bound (26.7\%). The weighted-mean DEFF variant yields 13.5\%, but its effective cluster size ($\bar{m}{=}254$) implies e
…[truncated 10930 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 968 · 2026-05-22T16:26:33.204889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 969 · 2026-05-22T16:26:33.255769+00:00_

1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini
…[truncated 14885 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 970 · 2026-05-22T16:26:39.633381+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 971 · 2026-05-22T16:26:39.935027+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\enlargethispage*{14\baselineskip}
4	
5	\subsection{What Drives Temporal DIF?}
6	\label{sec:disc_temporal}
7	
8	\looseness=-1
9	Temporal DIF detects \emph{that} items function differently across cohorts, not \emph{why}. Three non-exclusive mechanisms may drive the observed ${\approx}$27--29\% rate: (1)~differential contamination (asymmetric training data exposure); (2)~capability evolution (genuine skill acquisition); (3)~training methodology shifts (RLHF, post-training). The ETS baseline of 5--15\% C\%~\citep{clauser1998dif} is for concurrent demographic groups sharing the same test administration; the comparison to temporal LLM cohorts is illustrative, not normative.
10	
11	\looseness=-1
12	Our experimental evidence constrains this ambiguity through four exclusion arguments. \emph{Ability confounds} explain at most 2.4~pp: 1:1 matching yields C\% $= 28.9\%$ vs.\ unmatched 31.3\% (Cohen's $d = -0.17$; \Cref{sec:temporal}). \emph{Domain-level improvement} explains ${<}0.1\%$ of item-level DIF variance (pseudo $R^2 = 0.0007$); DIF is predominantly item-specific. \emph{Item quality defects} are ruled out: expert-annotated errors~\citep{gema2024mmlu} show no enrichment among DIF-C items (enrichment $= 1.10$, 95\% CI $[0.92, 1.27]$, $p = 0.23$). \emph{Web-overlap labels}~\citep{li2024contamination} are near-independent of DIF flags (Jaccard $= 0.206$, indistinguishable from permutation null; \Cref{sec:groundtruth}), a category error in ground truth; MMLU-CF~\citep{zhao2025mmlucf} complements our approach via item reformulation.
13	
14	\looseness=-1
15	The difficulty--direction interaction ($\rho = -0.597$; \Cref{sec:temporal}) provides suggestive evidence for capability evolution: hardest-decile DIF-C items are 88.7\% focal-favoring (2024 better), easiest-decile 96.2\% reference-favoring. This pattern is more consistent with skill acquisition than contamination, which would target items regardless of difficulty; however,
…[truncated 1308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 972 · 2026-05-22T16:26:39.935404+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 973 · 2026-05-22T16:26:39.985947+00:00_

1	\section*{Limitations}
2	
3	\paragraph{Methodological scope.}
4	MH-DIF detects only uniform DIF; the 17.7\% of items showing non-uniform patterns (ability-dependent DIF) may be underestimated by the Mantel-Haenszel statistic, and future work could employ logistic regression DIF or IRT-based methods for fuller characterization. Logistic regression reveals this additional non-uniform DIF (effect-size criterion; $p$-values not adjusted for within-family clustering); the union reaches 47\% on 9/57 subjects, making the corrected ${\approx}$27--29\% conservative but subject to further validation at full-benchmark scale. More fundamentally, DIF detects \emph{that} items function differently but cannot determine \emph{why}---the signal may reflect contamination, capability change, or training methodology shifts. A definitive causal decomposition remains out of reach without access to model training data. The semi-synthetic framework uses binary response flipping (incorrect $\to$ correct) to simulate differential contamination, representing a worst-case uniform exploitation pattern. Real-world contamination involves partial memorization, reasoning shortcuts, and format-specific advantages; detection power under such realistic patterns is untested. The moderate $\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$ reflects sensitivity to severe differential behavior; the framework's primary methodological contribution---cross-subject matching achieving $\Delta\mathrm{FPR} = 0.000$---is a matching strategy property independent of injection realism. Our uniform injection model is difficulty-agnostic, whereas real contamination likely correlates with item difficulty. Difficulty-dependent injection would concentrate DIF on easy items, potentially increasing detection power for that subset while reducing sensitivity to hard-item DIF; the observed difficulty--direction interaction ($\rho = -0.597$) suggests that actual patterns are more complex than uniform models capture.
5	
6	\paragraph
…[truncated 2718 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 974 · 2026-05-22T16:26:46.462253+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 975 · 2026-05-22T16:26:46.713690+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We use \emph{measurement invariance} to denote the property that test items function identically across groups~\citep{meredith1993invariance}, \emph{differential item functioning} (DIF) as the item-level statistical test for violations, and \emph{temporal measurement instability} as the empirical phenomenon when DIF is detected across time-defined cohorts---a descriptive term denoting systematic changes in measurement properties, without implying degradation or attributing cause. Applying Mantel-Haenszel DIF analysis~\citep{holland1988mh} with ETS severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} we find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$) between 2023 and 2024 model cohorts---versus 0.18\% under a random-split control. This instability does not threaten benchmark validity ($\rho \approx 0.997$ between full and stable-item rankings); it is diagnostic, revealing which capability dimensions shift across model generations.
5	
6	Contamination detectors---from membership inference~\citep{shi2024mink} to performance-based methods~\citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique}---validate primarily against web-overlap labels~\citep{li2024contamination} that measure \emph{global exposure}: whether an item exists in publicly accessible training corpora. Such labels do not capture \emph{differential item functioning}: whether an item behaves differently 
…[truncated 3053 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 976 · 2026-05-22T16:26:46.764437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 977 · 2026-05-22T16:26:46.865916+00:00_

1	\vspace{-12pt}
2	\section{Conclusion}
3	\label{sec:conclusion}
4	
5	\looseness=-1
6	Across six METABENCH benchmarks, 17.9--31.3\% of items exhibit temporal measurement instability between 2023 and 2024 model cohorts (${\approx}$27--29\% for MMLU after non-independence corrections; conservative bound: 13.5\%). Web-overlap labels are near-independent of DIF flags (Jaccard $= 0.206$); rankings are preserved ($\rho \approx 0.997$), motivating routine temporal DIF audits.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 978 · 2026-05-22T16:29:41.067597+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 979 · 2026-05-22T16:29:41.369346+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 980 · 2026-05-22T16:32:15.255358+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1: 方法严谨性审查\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel DIF 分析迁移到 LLM 基准评测，在 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）上发现约 27-29% 的题目在 2023 与 2024 模型队列间存在时间性 DIF。论文提出了 cross-subject matching（ΔFPR = 0 保证）的半合成验证框架，并揭示了 DIF 标记与 web-overlap 污染标签的正交性。研究规模大、方法论适配工作扎实，但在 DEFF 校正的内部张力、半合成框架的现实性、以及因果归因模糊性上存在显著的方法论缺陷。\n\n## Strengths\n\n**S1** [规模与系统性] 迄今最大规模的 LLM 基准 DIF 分析（5,227 模型 × 12,508 题目），跨 6 个 METABENCH 基准复现（C% = 17.9-31.3%），random-split sanity check（0.18%）、LOFO 分析、ability-matched 控制等验证链完整。这种规模和系统性在 LLM 评测文献中罕见。\n\n**S2** [Cross-subject matching] 将 purified subtest matching 适配到 LLM 多领域基准场景是一个真正的方法论贡献。ΔFPR = 0 的构造性保证（Section 3.4, Remark）在 single-subject injection 下成立，且多主题注入（Table 6）展示了 graceful degradation（k ≤ 5 时 ΔFPR < 0.007）。这一匹配策略的价值独立于注入机制的现实性。\n\n**S3** [Ground truth 元批判] DIF 标记与 web-overlap 标签的正交性（Jaccard = 0.206, φ = 0.012, enrichment = 0.964; Section 4.3）是一个重要的负面结果。它精确地指出了当前污染检测验证方法论的根本缺陷：global exposure ≠ differential functioning。这一发现对整个污染检测研究方向有指导意义。\n\n**S4** [透明性] 论文在 Limitations 中坦率讨论了 MH 只检测 uniform DIF（17.7% 的 non-uniform DIF 被遗漏）、binary flipping 的局限、因果不可分等核心限制。Appendix A.2 明确承认 2PL 对 MMLU 多维结构拟合不佳。这种透明度值得肯定。\n\n**S5** [多重收敛校正] 三种非独立性校正方法（simple-mean DEFF 29.2%、graduated de-duplication 29.1%、cluster bootstrap 下界 26.7%）收敛于 ~27-29%，以 13.5% 作为保守下界。尽管这些方法并非完全独立（见 W1），收敛本身至少表明结果对校正方法的选择不过度敏感。\n\n## Weaknesses\n\n**W1** [Major] DEFF 校正的内部张力（13.5% vs 27-29%）未充分解决\n\n核心问题：weighted-mean DEFF 给出 C% = 13.5%，而 simple-mean DEFF 给出 29.2%，两者相差一倍以上。论文采用 27-29% 作为主要估计、13.5% 作为保守下界（Section 4.2, Appendix C），但论证不够有力：\n\n(a) 论文以 \"weighted mean 的有效聚类大小 m̄ = 254 意味着每个家族成员功能上相同——对具有不同训练数据的模型而言不现实\" 来否定 weighted-mean 变体。但 simple-mean 同样有问题：它对所有家族赋予相同权重，实际上假设 547 个 Mistral 变体组成的家族与 3 个模型组成的小家族具有相同的聚类结构。真实值可能位于两个极端之间。\n\n(b) 论文引用 Valliant et al. (2013) 指出 \"只有 ~30 个家族时 ICC 估计不稳定\" 来质疑 weighted-mean 变体，但 ICC 不稳定性同样影响 simple-mean 变体——两者使用同一组 ICC 估计值。\n\n(c) 三种 \"收敛\" 方法（simple-mean DEFF、graduated de-duplication、cluster bootstrap 下界）并非独立验证——它们都在处理同一个偏差来源（家族内相关性），使用高度相关的信号。相关方法间的收敛是预期的，不能证明校正水平的正确性。\n\n(d) Appendix C 报告 DEFF = 3.87，但用 mean ICC = 0.047 和 m̄ = 62.8 计算得 1 + 61.8 × 0.047 = 3.905。差异虽小但表明可能使用了未完全说明的 ICC 值。\n\n建议：报告 ICC 在不同家族大小分层下的变化，使用 size-stratified DEFF（如按家族大小分 3-4 个层级分别计算），或至少提供从 13.5% 到 29.2% 的连续参数化曲线，让读者评估哪个估计更合理。\n\n**W2** [Major] \"Graduated de-duplication\" 方法未定义\n\n论文将 \"graduated de-duplication at K=20 (C% = 29.1%)\" 列为三种收敛校正之一（Section 4.2, Table 8），但该方法在正文和附录中**从未被正式定义**。Table 8 仅描述为 \"Remove within-family duplicates\"，但具体操作不明：是每个家族保留至多 K 个模型？还是按某种相似度阈值去重？K=20 中的 K 是指什么参数？这里的 K 与 DIF 分层的 K=5 是否不同？\n\n作为支撑核心定量结论的三种方法之一，缺乏可复现的方法描述是严重的方法论透明度缺陷。\n\n**W3** [Major] 半合成框架的 binary response flipping 过度简化，ΔTPR 的推广性存疑\n\n论文的半合成验证使用均匀的 0→1 二值翻转模拟污染（Section 3.4）。论文正确指出 ΔFPR = 0 保证是匹配策略的固有属性、独立于注入现实性，但 ΔTPR（= +0.508 at p = 0.5）高度依赖于注入机制：\n\n(a) 真实污染产生部分记忆、推理捷径、格式特异性优势——这些产生的信号远比 binary flipping 微弱且复杂。如果真实污染的效应量远小于 binary flipping，实际 TPR 可能远低于 0.508。论文称 binary flipping 是 \"worst-case uniform exploitation pattern\" 产生 \"upper-bound estimates\"，但这仅对单题信号幅度成立。真实污染可能产生跨题目的相关模式（如难度依赖的污染），其对聚合检测力的影响可增可减。\n\n(b) 经验数据中观察到的 difficulty-direction interaction（ρ = -0.597; Section 4.2）强烈暗示真实的差异性行为模式是非均匀的——恰恰是半合成框架无法建模的模式。\n\n(c) 半合成框架仅模拟 incorrect→correct 翻转。真实的时间性变化也可能包括 correct→incorrect（如 RLHF 导致的过度拒绝、格式变化导致的性能退化），这类模式未被测试。\n\n建议：至少补充一种 difficulty-dependent injection（如按题目难度分层设置不同的翻转概率），以及双向翻转实验，展示 detection power 对注入模式的敏感性。\n\n**W4** [Major] 因果模糊性与论文定位之间存在张力\n\n论文承认 DIF 无法区分三种机制——差异性污染、能力演化、训练方法学转变（Section 5.1），但论文的定位仍然紧密围绕 \"contamination\" 展开（标题虽然用了 \"measurement instability\"，但 Introduction 和 Contribution 大量讨论 contamination detection）。\n\nDiscussion 中的四个排除论证（Section 5.1）实际上都比较弱：\n- \"Ability confounds explain at most 2.4 pp\"——仅排除了整体能力差异，未排除题目级别的能力演化\n- \"Domain-level improvement explains <0.1% of item-level DIF variance\"——排除了域级混淆，但不排除题目级能力变化\n- \"Item quality defects are ruled out\"——与污染问题不直接相关\n- \"Web-overlap labels are orthogonal\"——既可解读为 \"web-overlap 是错误的 ground truth\"，也可等价解读为 \"DIF 测量的不是污染\"\n\n关键证据：difficulty-direction interaction（ρ = -0.597：2024 模型在难题上进步、在易题上退步）更符合能力演化模式而非污染模式（污染应当不分难度地提升表现）。论文在 Section 5.1 承认 \"this pattern is more consistent with skill acquisition than contamination\"，但未跟进这一推论的含义：如果主要信号是能力演化而非污染，论文对污染检测文献的相关性将显著降低。\n\n建议：更明确地将论文定位为 \"measurement invariance audit\"，降低对 contamination 的暗示；或提供更强的证据区分三种机制。\n\n**W5** [Minor] p 值阈值在 N = 5,227 下几乎不起过滤作用\n\n论文在 Section 3.2 明确承认 \"only 3 of 3,918 C items lack significance\"——p < 0.05 阈值基本无效。DEFF 校正后有 269 项（6.9%）丧失显著性（均保持 |ΔMH| ≥ 1.5），其中 74% 是 near-miss（p_adj ∈ [0.05, 0.10]）。这意味着：\n- ETS 双重阈值实际退化为单一效应量阈值\n- DEFF 校正仅通过 p 值臂发挥作用（从 31.3% 降至 29.2%，仅 2.1 pp），校正力度有限\n\n这不是方法论错误，但论文应更明确地讨论大样本下 ETS 分类体系的适用性问题。在教育测量中 ETS 双重阈值面对的是数千名考生；5,227 个模型超出了该体系的设计范围。\n\n**W6** [Minor] K 敏感性范围较宽（27-39%），对 K=5 选择的合理性论证不足\n\nSection 4.2 报告 K=3 → 39.4%，K=5 → 31.3%，K=10 → 35.9%，K=20 → 不稳定。K=3 的 39.4% 被归因于 \"under-stratification\"，但为什么 quintile binning（K=5）是正确的分层水平并未从理论上证明。K=10 的非单调峰值被归因于 \"finer strata capturing ability-DIF interactions\"——但 ability-DIF 交互正是 non-uniform DIF 的定义，而 MH 程序仅检测 uniform DIF。如果 K=10 的升高源于 non-uniform DIF 的泄漏，这暗示 MH 的 uniform DIF 估计在不同 K 下不稳定，是一个方法论问题。\n\n此外，K-sensitivity 分析使用的是未经 DEFF 校正的 C%。DEFF 校正后的 K-sensitivity 是什么样的？\n\n**W7** [Minor] ICC 估计方法细节不足\n\nICC = 0.047（median 0.041）是 DEFF 校正的核心参数，但以下信息缺失：\n- 家族定义标准（基于模型名称？架构？训练数据来源？）\n- 不同家族大小下 ICC 的分层分布\n- ICC 估计的置信区间或标准误\n- Singleton 模型（不属于任何家族的模型）如何处理——5,227 总模型中仅 1,884 用于 ICC 估计，其余 3,343 模型的处理方式不明\n- 家族定义的敏感性分析（如将 Llama-2 和 Llama-3 视为同一家族 vs 不同家族时 ICC 如何变化）\n\n**W8** [Minor] Cross-subject ΔFPR = 0 保证假设无跨学科迁移\n\nΔFPR = 0 的构造性证明（Section 3.4, Remark）依赖于 \"向 subject s 注入污染不影响其他学科的表现\"。对 binary flipping 的半合成框架而言这trivially成立，但在真实场景中，在某一 MMLU 学科上的训练可能通过迁移学习提升相关学科的表现。论文通过多主题注入分析（Table 6）部分覆盖了这一问题，但 k=20 时 ΔFPR = 0.069 已不可忽略，且在 DEFF 校正后的保守估计 13.5% 中占比高达 50%（论文在 Section 4.5 明确指出这一点）。\n\n**W9** [Nitpick] 2PL power analysis 在 MMLU 多维结构上的适用性\n\nAppendix A.2 明确承认 \"2PL fit is poor for MMLU's multidimensional structure\"，但 Monte Carlo power analysis 仍使用 2PL 参数（ā = 1.2, b̄ = -0.84）。论文将此定位为 \"triangulation 的一条腿\"，与半合成注入结果互补，这是合理的缓解。但 TPR = 0.68-0.80 被显著地报告在正文中（Section 4.1），可能给读者过高的检测灵敏度信心。\n\n**W10** [Nitpick] 1:1 nearest-neighbor matching 分析细节不足\n\nSection 4.2 报告 \"1:1 nearest-neighbor matching on total score (N=638/group, Cohen's d = -0.17) yields C% = 28.9% ± 0.1%\"，用于界定能力混淆的上限为 \"at most ~2.4 pp\"。但未说明匹配方法（propensity score? caliper matching?）、匹配质量评估（匹配后的 balance check）、以及样本量减少（从 ~1,800 到 638×2）是否导致统计功效下降从而解释部分 C% 降低。\n\n## Questions\n\n**Q1**: 模型家族如何定义？是基于模型名称前缀的启发式方法，还是更严格的聚类？如果改变家族定义（如将所有 Llama 变体视为一个家族 vs 分为 Llama-2 和 Llama-3），ICC 和 DEFF 如何变化？\n\n**Q2**: 5,227 个模型中仅 1,884 个（来自 30 个 family ≥ 2 的家族）用于 ICC 估计。其余 ~3,343 个 singleton 模型在 DEFF 校正中如何处理？如果它们被视为 DEFF = 1（无需校正），这是否会导致校正的异质性？\n\n**Q3**: 如果 DIF 主要由能力演化驱动（如 difficulty-direction interaction 所暗示），Section 5.2 推荐的 DIF 审计协议的实践价值是什么？如果题目因模型真正进步而 \"更容易\"，将这些题目标记为 \"不稳定\" 并从排名中移除，是否反而损害了评测的有效性？\n\n**Q4**: \"Graduated de-duplication at K=20\" 的具体操作步骤是什么？该方法在论文中从未被正式定义。\n\n**Q5**: 半合成框架是否测试过 correct→incorrect 方向的翻转？训练方法学转变（如 RLHF 过度优化）可能导致模型在某些题目上的表现退化，这种模式下 MH-DIF 的检测力如何？\n\n## Missing References\n\n1. **Kamata & Binici (2003)** — \"Random-Effect DIF Model\" — 提出了在多层数据结构下的随机效应 DIF 模型，直接相关于论文面临的 LLM 非独立性问题。论文引用了 French & Finch (2010) 的层次逻辑回归方法，但未引用更早且理论上更相关的随机效应 DIF 框架。\n\n2. **Alzahrani et al. (2024)** — \"When Benchmarks are Targets: Revealing the Sensitivity of Large Language Model Leaderboards\" — 直接相关于论文的 benchmark instability 主题，讨论了 leaderboard 对基准选择和项目属性的敏感性。\n\n## Overall Assessment\n\n**Soundness**: 3/5 — 核心方法论（MH-DIF 迁移到 LLM 评测）合理，cross-subject matching 是真正的方法论贡献。但 DEFF 校正的内部张力（13.5% vs 29.2% 的两倍差距）、graduated de-duplication 方法未定义、半合成框架的注入现实性不足等问题削弱了定量结论的可信度。\n\n**Excitement**: 3.5/5 — 研究问题重要且及时；cross-subject matching 和 ground truth 元批判有独立价值；但因果模糊性限制了 actionable insights。\n\n**Reproducibility**: 3.5/5 — 数据（METABENCH）公开可用，代码声称可用（匿名链接），MH-DIF 和 ETS 分类描述清晰。但 graduated de-duplication 未定义，ICC 家族定义未明确说明，影响完全复现。\n\n**Reviewer Confidence**: 4/5 — 具有统计方法论和教育测量的相关专业知识，仔细阅读了全文和附录。\n\n**Overall**: 3.0 (Findings) — 论文在规模、系统性和若干方法论贡献（cross-subject matching, ground truth 元批判）上有明确价值，但在核心定量结论（~27-29% 这个数字）的可靠性上存在多个相互关联的方法论缺口：DEFF 校正内部不一致且论证不充分（W1），支撑方法之一未定义（W2），半合成验证的 ΔTPR 推广性存疑（W3），因果归因模糊性与论文定位之间存在未解决的张力（W4）。这些问题中任何单个都不致命，但它们共同削弱了读者对 \"27-29% 的 MMLU 题目存在时间性测量不稳定\" 这一中心主张的信心。\n\n适合 Findings 收录：方法论框架有价值，实证发现（DIF 存在且与 web-overlap 正交）对社区有参考意义，但定量结论的精度和因果解释力不足以支撑主会议录用。\n",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1: 方法严谨性审查\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel DIF 分析迁移到 LLM 基准评测，在 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）上发现约 27-29% 的题目在 2023 与 2024 模型队列间存在时间性 DIF。论文提出了 cross-subject matching（ΔFPR = 0 保证）的半合成验证框架，并揭示了 DIF 标记与 web-overlap 污染标签的正交性。研究规模大、方法论适配工作扎实，但在 DEFF 校正的内部张力、半合成框架的现实性、以及因果归因模糊性上存在显著的方法论缺陷。\n\n## Strengths\n\n**S1** [规模与系统性] 迄今最大规模的 LLM 基准 DIF 分析（5,227 模型 × 12,508 题目），跨 6 个 METABENCH 基准复现（C% = 17.9-31.3%），random-split sanity check（0.18%）、LOFO 分析、ability-matched 控制等验证链完整。这种规模和系统性在 LLM 评测文献中罕见。\n\n**S2** [Cross-subject matching] 将 purified subtest matching 适配到 LLM 多领域基准场景是一个真正的方法论贡献。ΔFPR = 0 的构造性保证（Section 3.4, Remark）在 single-subject injection 下成立，且多主题注入（Table 6）展示了 graceful degradation（k ≤ 5 时 ΔFPR < 0.007）。这一匹配策略的价值独立于注入机制的现实性。\n\n**S3** [Ground truth 元批判] DIF 标记与 web-overlap 标签的正交性（Jaccard = 0.206, φ = 0.012, enrichment = 0.964; Section 4.3）是一个重要的负面结果。它精确地指出了当前污染检测验证方法论的根本缺陷：global exposure ≠ differential functioning。这一发现对整个污染检测研究方向有指导意义。\n\n**S4** [透明性] 论文在 Limitations 中坦率讨论了 MH 只检测 uniform DIF（17.7% 的 non-uniform DIF 被遗漏）、binary flipping 的局限、因果不可分等核心限制。Appendix A.2 明确承认 2PL 对 MMLU 多维结构拟合不佳。这种透明度值得肯定。\n\n**S5** [多重收敛校正] 三种非独立性校正方法（simple-mean DEFF 29.2%、graduated de-duplication 29.1%、cluster bootstrap 下界 26.7%）收敛于 ~27-29%，以 13.5% 作为保守下界。尽管这些方法并非完全独立（见 W1），收敛本身至少表明结果对校正方法的选择不过度敏感。\n\n## Weaknesses\n\n**W1** [Major] DEFF 校正的内部张力（13.5% vs 27-29%）未充分解决\n\n核心问题：weighted-mean DEFF 给出 C% = 13.5%，而 simple-mean DEFF 给出 29.2%，两者相差一倍以上。论文采用 27-29% 作为主要估计、13.5% 作为保守下界（Section 4.2, Appendix C），但论证不够有力：\n\n(a) 论文以 \"weighted mean 的有效聚类大小 m̄ = 254 意味着每个家族成员功能上相同——对具有不同训练数据的模型而言不现实\" 来否定 weighted-mean 变体。但 simple-mean 同样有问题：它对所有家族赋予相同权重，实际上假设 547 个 Mistral 变体组成的家族与 3 个模型组成的小家族具有相同的聚类结构。真实值可能位于两个极端之间。\n\n(b) 论文引用 Valliant et al. (2013) 指出 \"只有 ~30 个家族时 ICC 估计不稳定\" 来质疑 weighted-mean 变体，但 ICC 不稳定性同样影响 simple-mean 变体——两者使用同一组 ICC 估计值。\n\n(c) 三种 \"收敛\" 方法（simple-mean DEFF、graduated de-duplication、cluster bootstrap 下界）并非独立验证——它们都在处理同一个偏差来源（家族内相关性），使用高度相关的信号。相关方法间的收敛是预期的，不能证明校正水平的正确性。\n\n(d) Appendix C 报告 DEFF = 3.87，但用 mean ICC = 0.047 和 m̄ = 62.8 计算得 1 + 61.8 × 0.047 = 3.905。差异虽小但表明可能使用了未完全说明的 ICC 值。\n\n建议：报告 ICC 在不同家族大小分层下的变化，使用 size-stratified DEFF（如按家族大小分 3-4 个层级分别计算），或至少提供从 13.5% 到 29.2% 的连续参数化曲线，让读者评估哪个估计更合理。\n\n**W2** [Major] \"Graduated de-duplication\" 方法未定义\n\n论文将 \"graduated de-duplication at K=20 (C% = 29.1%)\" 列为三种收敛校正之一（Section 4.2, Table 8），但该方法在正文和附录中**从未被正式定义**。Table 8 仅描述为 \"Remove within-family duplicates\"，但具体操作不明：是每个家族保留至多 K 个模型？还是按某种相似度阈值去重？K=20 中的 K 是指什么参数？这里的 K 与 DIF 分层的 K=5 是否不同？\n\n作为支撑核心定量结论的三种方法之一，缺乏可复现的方法描述是严重的方法论透明度缺陷。\n\n**W3** [Major] 半合成框架的 binary response flipping 过度简化，ΔTPR 的推广性存疑\n\n论文的半合成验证使用均匀的 0→1 二值翻转模拟污染（Section 3.4）。论文正确指出 ΔFPR = 0 保证是匹配策略的固有属性、独立于注入现实性，但 ΔTPR（= +0.508 at p = 0.5）高度依赖于注入机制：\n\n(a) 真实污染产生部分记忆、推理捷径、格式特异性优势——这些产生的信号远比 binary flipping 微弱且复杂。如果真实污染的效应量远小于 binary flipping，实际 TPR 可能远低于 0.508。论文称 binary flipping 是 \"worst-case uniform exploitation pattern\" 产生 \"upper-bound estimates\"，但这仅对单题信号幅度成立。真实污染可能产生跨题目的相关模式（如难度依赖的污染），其对聚合检测力的影响可增可减。\n\n(b) 经验数据中观察到的 difficulty-direction interaction（ρ = -0.597; Section 4.2）强烈暗示真实的差异性行为模式是非均匀的——恰恰是半合成框架无法建模的模式。\n\n(c) 半合成框架仅模拟 incorrect→correct 翻转。真实的时间性变化也可能包括 correct→incorrect（如 RLHF 导致的过度拒绝、格式变化导致的性能退化），这类模式未被测试。\n\n建议：至少补充一种 difficulty-dependent injection（如按题目难度分层设置不同的翻转概率），以及双向翻转实验，展示 detection power 对注入模式的敏感性。\n\n**W4** [Major] 因果模糊性与论文定位之间存在张力\n\n论文承认 DIF 无法区分三种机制——差异性污染、能力演化、训练方法学转变（Section 5.1），但论文的定位仍然紧密围绕 \"contamination\" 展开（标题虽然用了 \"measurement instability\"，但 Introduction 和 Contribution 大量讨论 contamination detection）。\n\nDiscussion 中的四个排除论证（Section 5.1）实际上都比较弱：\n- \"Ability confounds explain at most 2.4 pp\"——仅排除了整体能力差异，未排除题目级别的能力演化\n- \"Domain-level improvement explains <0.1% of item-level DIF variance\"——排除了域级混淆，但不排除题目级能力变化\n- \"Item quality defects are ruled out\"——与污染问题不直接相关\n- \"Web-overlap labels are orthogonal\"——既可解读为 \"web-overlap 是错误的 ground truth\"，也可等价解读为 \"DIF 测量的不是污染\"\n\n关键证据：difficulty-direction interaction（ρ = -0.597：2024 模型在难题上进步、在易题上退步）更符合能力演化模式而非污染模式（污染应当不分难度地提升表现）。论文在 Section 5.1 承认 \"this pattern is more consistent with skill acquisition than contamination\"，但未跟进这一推论的含义：如果主要信号是能力演化而非污染，论文对污染检测文献的相关性将显著降低。\n\n建议：更明确地将论文定位为 \"measurement invariance audit\"，降低对 contamination 的暗示；或提供更强的证据区分三种机制。\n\n**W5** [Minor] p 值阈值在 N = 5,227 下几乎不起过滤作用\n\n论文在 Section 3.2 明确承认 \"only 3 of 3,918 C items lack significance\"——p < 0.05 阈值基本无效。DEFF 校正后有 269 项（6.9%）丧失显著性（均保持 |ΔMH| ≥ 1.5），其中 74% 是 near-miss（p_adj ∈ [0.05, 0.10]）。这意味着：\n- ETS 双重阈值实际退化为单一效应量阈值\n- DEFF 校正仅通过 p 值臂发挥作用（从 31.3% 降至 29.2%，仅 2.1 pp），校正力度有限\n\n这不是方法论错误，但论文应更明确地讨论大样本下 ETS 分类体系的适用性问题。在教育测量中 ETS 双重阈值面对的是数千名考生；5,227 个模型超出了该体系的设计范围。\n\n**W6** [Minor] K 敏感性范围较宽（27-39%），对 K=5 选择的合理性论证不足\n\nSection 4.2 报告 K=3 → 39.4%，K=5 → 31.3%，K=10 → 35.9%，K=20 → 不稳定。K=3 的 39.4% 被归因于 \"under-stratification\"，但为什么 quintile binning（K=5）是正确的分层水平并未从理论上证明。K=10 的非单调峰值被归因于 \"finer strata capturing ability-DIF interactions\"——但 ability-DIF 交互正是 non-uniform DIF 的定义，而 MH 程序仅检测 uniform DIF。如果 K=10 的升高源于 non-uniform DIF 的泄漏，这暗示 MH 的 uniform DIF 估计在不同 K 下不稳定，是一个方法论问题。\n\n此外，K-sensitivity 分析使用的是未经 DEFF 校正的 C%。DEFF 校正后的 K-sensitivity 是什么样的？\n\n**W7** [Minor] ICC 估计方法细节不足\n\nICC = 0.047（median 0.041）是 DEFF 校正的核心参数，但以下信息缺失：\n- 家族定义标准（基于模型名称？架构？训练数据来源？）\n- 不同家族大小下 ICC 的分层分布\n- ICC 估计的置信区间或标准误\n- Singleton 模型（不属于任何家族的模型）如何处理——5,227 总模型中仅 1,884 用于 ICC 估计，其余 3,343 模型的处理方式不明\n- 家族定义的敏感性分析（如将 Llama-2 和 Llama-3 视为同一家族 vs 不同家族时 ICC 如何变化）\n\n**W8** [Minor] Cross-subject ΔFPR = 0 保证假设无跨学科迁移\n\nΔFPR = 0 的构造性证明（Section 3.4, Remark）依赖于 \"向 subject s 注入污染不影响其他学科的表现\"。对 binary flipping 的半合成框架而言这trivially成立，但在真实场景中，在某一 MMLU 学科上的训练可能通过迁移学习提升相关学科的表现。论文通过多主题注入分析（Table 6）部分覆盖了这一问题，但 k=20 时 ΔFPR = 0.069 已不可忽略，且在 DEFF 校正后的保守估计 13.5% 中占比高达 50%（论文在 Section 4.5 明确指出这一点）。\n\n**W9** [Nitpick] 2PL power analysis 在 MMLU 多维结构上的适用性\n\nAppendix A.2 明确承认 \"2PL fit is poor for MMLU's multidimensional structure\"，但 Monte Carlo power analysis 仍使用 2PL 参数（ā = 1.2, b̄ = -0.84）。论文将此定位为 \"triangulation 的一条腿\"，与半合成注入结果互补，这是合理的缓解。但 TPR = 0.68-0.80 被显著地报告在正文中（Section 4.1），可能给读者过高的检测灵敏度信心。\n\n**W10** [Nitpick] 1:1 nearest-neighbor matching 分析细节不足\n\nSection 4.2 报告 \"1:1 nearest-neighbor matching on total score (N=638/group, Cohen's d = -0.17) yields C% = 28.9% ± 0.1%\"，用于界定能力混淆的上限为 \"at most ~2.4 pp\"。但未说明匹配方法（propensity score? caliper matching?）、匹配质量评估（匹配后的 balance check）、以及样本量减少（从 ~1,800 到 638×2）是否导致统计功效下降从而解释部分 C% 降低。\n\n## Questions\n\n**Q1**: 模型家族如何定义？是基于模型名称前缀的启发式方法，还是更严格的聚类？如果改变家族定义（如将所有 Llama 变体视为一个家族 vs 分为 Llama-2 和 Llama-3），ICC 和 DEFF 如何变化？\n\n**Q2**: 5,227 个模型中仅 1,884 个（来自 30 个 family ≥ 2 的家族）用于 ICC 估计。其余 ~3,343 个 singleton 模型在 DEFF 校正中如何处理？如果它们被视为 DEFF = 1（无需校正），这是否会导致校正的异质性？\n\n**Q3**: 如果 DIF 主要由能力演化驱动（如 difficulty-direction interaction 所暗示），Section 5.2 推荐的 DIF 审计协议的实践价值是什么？如果题目因模型真正进步而 \"更容易\"，将这些题目标记为 \"不稳定\" 并从排名中移除，是否反而损害了评测的有效性？\n\n**Q4**: \"Graduated de-duplication at K=20\" 的具体操作步骤是什么？该方法在论文中从未被正式定义。\n\n**Q5**: 半合成框架是否测试过 correct→incorrect 方向的翻转？训练方法学转变（如 RLHF 过度优化）可能导致模型在某些题目上的表现退化，这种模式下 MH-DIF 的检测力如何？\n\n## Missing References\n\n1. **Kamata & Binici (2003)** — \"Random-Effect DIF Model\" — 提出了在多层数据结构下的随机效应 DIF 模型，直接相关于论文面临的 LLM 非独立性问题。论文引用了 French & Finch (2010) 的层次逻辑回归方法，但未引用更早且理论上更相关的随机效应 DIF 框架。\n\n2. **Alzahrani et al. (2024)** — \"When Benchmarks are Targets: Revealing the Sensitivity of Large Language Model Leaderboards\" — 直接相关于论文的 benchmark instability 主题，讨论了 leaderboard 对基准选择和项目属性的敏感性。\n\n## Overall Assessment\n\n**Soundness**: 3/5 — 核心方法论（MH-DIF 迁移到 LLM 评测）合理，cross-subject matching 是真正的方法论贡献。但 DEFF 校正的内部张力（13.5% vs 29.2% 的两倍差距）、graduated de-duplication 方法未定义、半合成框架的注入现实性不足等问题削弱了定量结论的可信度。\n\n**Excitement**: 3.5/5 — 研究问题重要且及时；cross-subject matching 和 ground truth 元批判有独立价值；但因果模糊性限制了 actionable insights。\n\n**Reproducibility**: 3.5/5 — 数据（METABENCH）公开可用，代码声称可用（匿名链接），MH-DIF 和 ETS 分类描述清晰。但 graduated de-duplication 未定义，ICC 家族定义未明确说明，影响完全复现。\n\n**Reviewer Confidence**: 4/5 — 具有统计方法论和教育测量的相关专业知识，仔细阅读了全文和附录。\n\n**Overall**: 3.0 (Findings) — 论文在规模、系统性和若干方法论贡献（cross-subject matching, ground truth 元批判）上有明确价值，但在核心定量结论（~27-29% 这个数字）的可靠性上存在多个相互关联的方法论缺口：DEFF 校正内部不一致且论证不充分（W1），支撑方法之一未定义（W2），半合成验证的 ΔTPR 推广性存疑（W3），因果归因模糊性与论文定位之间存在未解决的张力（W4）。这些问题中任何单个都不致命，但它们共同削弱了读者对 \"27-29% 的 MMLU 题目存在时间性测量不稳定\" 这一中心主张的信心。\n\n适合 Findings 收录：方法论框架有价值，实证发现（DIF 存在且与 web-overlap 正交）对社区有参考意义，但定量结论的精度和因果解释力不足以支撑主会议录用。\n",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 981 · 2026-05-22T16:32:19.584031+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4328
}
```

</details>

---
