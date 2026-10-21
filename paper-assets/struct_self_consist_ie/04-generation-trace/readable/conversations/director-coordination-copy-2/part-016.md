# Director coordination — Part 16 of 16

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[← Part 15](part-015.md) · [Transcript overview](../director-coordination-copy-2.md) · [Structured JSON](../../../sessions/6a/6a5a1a2f9a2bf6bdf404.json)

## Round 375

### Tool call

_source line 4920 · 2026-05-25T22:41:22.621363+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每一条 Must-Fix、Should-Fix、Minor 问题，用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n**一句话总结**: 扎实的诊断性研究，correlation-selection gap 概念有价值，但 concurrent work（Landesberg 2026）显著削弱新颖性，全局统计显著性边缘（Holm p_adj=0.055），SQL 跨任务证据过于薄弱。\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 诊断框架方法论合理，4数据集×2模型×5信号的实验设计完整；但核心建设性 claim（LP selection gain）全局 Holm 校正 p_adj=0.055 未达 0.05 显著性；SQL 仅有一个退化率统计量无法支撑跨任务验证声明 |\n| Excitement | 3.0/5 | Correlation-selection gap 是有用的诊断概念，degeneracy + signal alignment collapse 的分解提供了超越简单观察的机制性理解；但 Landesberg (2026) 已独立发现该 gap，实际可操作建议有限（框架自称 primarily diagnostic），entity-level construction 增益边缘且大多数配置下呈 inverse scaling |\n| Reproducibility | 4.0/5 | 提供匿名代码/数据链接，附录详细记录实验设置（Table 21 超参数、Table 5 符号表），使用多 seed（3-seed），信号定义明确 |\n\n### Must-Fix 问题\n\n**N1** [critical] SQL 跨任务证据严重不足，与 abstract 声明不匹配\n- 具体位置：Abstract 第5句 \"Cross-task pilots on relation extraction (RE) and SQL parsing confirm task-specific failure modes\"; §7.1 提及 SQL n=196, 87.2% degeneracy; Appendix ah \"O1\" 段仅一句话\n- 问题：Abstract 和 Introduction 将 SQL 并列为跨任务验证证据，但整篇论文对 SQL 的分析仅限于一个退化率统计量（87.2%）。没有对 SQL 进行任何信号分析、selection 实验、或诊断框架验证。相比之下 RE 有完整的 Appendix q（LP selection、pairwise overlap、flip instances、free-form decoding comparison），SQL 的深度完全不在同一水平。\n- 为什么影响接收：这构成了 claim 与 evidence 的不匹配。\"confirm task-specific failure modes\" 暗示对 SQL 做了诊断性分析，但实际只有一个数字。审稿人会认为这是 overclaiming。\n- 建议修改方向：(a) 降级 SQL 为 \"anecdotal evidence\" 或从 abstract 中移除；或 (b) 补充 SQL 的信号分析和 selection 实验使其与 RE 的分析深度匹配。\n\n**N2** [critical] 全局统计显著性边缘，核心建设性 claim 未达常规阈值\n- 具体位置：§7.2 \"reaches p_adj=0.055\"; Limitations 段 \"the strongest construction claim reaches p_adj=0.055\"；Table 4 LP selection gains\n- 问题：LP selection 的增益是论文中唯一超越 diagnostic 的 actionable contribution。在 Holm-Bonferroni 全局校正下 p_adj=0.055，未达到 α=0.05。论文在 Limitations 中披露了这一点（值得肯定），但 §7.2、Table 4 和 abstract 的叙述方式并未充分强调这一局限性。Abstract 中 \"+1.40 percentage points [pp] on Few-NERD\" 作为唯一具体数字被突出，给读者造成该增益是稳健可靠的印象。\n- 为什么影响接收：在 EMNLP main conference 标准下，核心 constructive claim 需要强统计支撑。p_adj=0.055 在边缘——本身不致命，但结合该 claim 是论文唯一可操作贡献，需要更显著的支撑或更谨慎的 framing。\n- 建议修改方向：(a) 在 abstract 中明确标注该增益在全局校正下为 marginal significance；(b) 在 Discussion（§8）中对这一点进行更充分的讨论；(c) 考虑增加 seed 数量以提升统计功效。\n\n### Should-Fix 问题\n\n**W1** [warning] 与 Landesberg (2026) 的差异化论述不够充分，Table 1 维度选择可能存在偏向\n- §2 末尾 \"Concurrent work\" 段仅4行；Table 1 的6个比较维度大多选取了本文占优的角度。缺少对 Landesberg 可能占优的维度的讨论。\n- 建议：扩展 concurrent work 讨论至至少一个完整段落，明确陈述 Landesberg (2026) 在哪些方面做得更好或更深入。\n\n**W2** [warning] 论文结构中实验结果分散在 §4 和 §7，逻辑连接不够清晰\n- §4 已经报告了大量实验结果，§7 又报告了更多实验结果。读者难以区分哪些结果属于 \"诊断发现\" 哪些属于 \"方法验证\"。\n- 建议：在 §4 和 §7 开头明确定位。\n\n**W3** [warning] Entity-level construction 的 inverse scaling 问题未被充分解释\n- 论文多次提到 entity-level construction 在 \"most configurations\" 下呈现 inverse scaling，但对其原因的分析不够深入。如果方法在大多数情况下是有害的，作为 \"建设性贡献\" 的价值需要质疑。\n- 建议：对 inverse scaling 给出更详细的归因分析，或明确将 entity-level construction 定位为 preliminary exploration。\n\n**W4** [warning] Related work 缺少 NER ensemble learning 经典文献\n- 完全没有提及 Florian et al. (2003) 的 NER ensemble。Diverse beam search（Vijayakumar et al., 2018）也值得讨论。\n\n### Minor\n- **M1**: Abstract \"+1.40 pp\" 与正文 \"+1.39pp\" 微小不一致。\n- **M2**: §4 第2段连续 10+ 个统计量，信息密度过高。\n- **M3**: Figure 1 \"+1.4 pp\" 在全局校正下为边缘显著，放在 overview figure 中可能造成误导。\n- **M4**: Appendix 36 页，部分关键分析需在正文中更明确引导。\n- **M5**: §3.1 符号首次出现时定义不够直观。\n\n### Questions\nQ1: 增加 seed 数量后 Holm p_adj 是否有望降至 0.05 以下？\nQ2: Landesberg (2026) 是否覆盖了 NER？\nQ3: Entity-level construction 在 Few-NERD 上表现最好，是否与 fine-grained entity type 有关？\nQ4: SQL 87.2% degeneracy 是否有计划补充完整诊断？"
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
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每一条 Must-Fix、Should-Fix、Minor 问题，用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n**一句话总结**: 扎实的诊断性研究，correlation-selection gap 概念有价值，但 concurrent work（Landesberg 2026）显著削弱新颖性，全局统计显著性边缘（Holm p_adj=0.055），SQL 跨任务证据过于薄弱。\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 诊断框架方法论合理，4数据集×2模型×5信号的实验设计完整；但核心建设性 claim（LP selection gain）全局 Holm 校正 p_adj=0.055 未达 0.05 显著性；SQL 仅有一个退化率统计量无法支撑跨任务验证声明 |\n| Excitement | 3.0/5 | Correlation-selection gap 是有用的诊断概念，degeneracy + signal alignment collapse 的分解提供了超越简单观察的机制性理解；但 Landesberg (2026) 已独立发现该 gap，实际可操作建议有限（框架自称 primarily diagnostic），entity-level construction 增益边缘且大多数配置下呈 inverse scaling |\n| Reproducibility | 4.0/5 | 提供匿名代码/数据链接，附录详细记录实验设置（Table 21 超参数、Table 5 符号表），使用多 seed（3-seed），信号定义明确 |\n\n### Must-Fix 问题\n\n**N1** [critical] SQL 跨任务证据严重不足，与 abstract 声明不匹配\n- 具体位置：Abstract 第5句 \"Cross-task pilots on relation extraction (RE) and SQL parsing confirm task-specific failure modes\"; §7.1 提及 SQL n=196, 87.2% degeneracy; Appendix ah \"O1\" 段仅一句话\n- 问题：Abstract 和 Introduction 将 SQL 并列为跨任务验证证据，但整篇论文对 SQL 的分析仅限于一个退化率统计量（87.2%）。没有对 SQL 进行任何信号分析、selection 实验、或诊断框架验证。相比之下 RE 有完整的 Appendix q（LP selection、pairwise overlap、flip instances、free-form decoding comparison），SQL 的深度完全不在同一水平。\n- 为什么影响接收：这构成了 claim 与 evidence 的不匹配。\"confirm task-specific failure modes\" 暗示对 SQL 做了诊断性分析，但实际只有一个数字。审稿人会认为这是 overclaiming。\n- 建议修改方向：(a) 降级 SQL 为 \"anecdotal evidence\" 或从 abstract 中移除；或 (b) 补充 SQL 的信号分析和 selection 实验使其与 RE 的分析深度匹配。\n\n**N2** [critical] 全局统计显著性边缘，核心建设性 claim 未达常规阈值\n- 具体位置：§7.2 \"reaches p_adj=0.055\"; Limitations 段 \"the strongest construction claim reaches p_adj=0.055\"；Table 4 LP selection gains\n- 问题：LP selection 的增益是论文中唯一超越 diagnostic 的 actionable contribution。在 Holm-Bonferroni 全局校正下 p_adj=0.055，未达到 α=0.05。论文在 Limitations 中披露了这一点（值得肯定），但 §7.2、Table 4 和 abstract 的叙述方式并未充分强调这一局限性。Abstract 中 \"+1.40 percentage points [pp] on Few-NERD\" 作为唯一具体数字被突出，给读者造成该增益是稳健可靠的印象。\n- 为什么影响接收：在 EMNLP main conference 标准下，核心 constructive claim 需要强统计支撑。p_adj=0.055 在边缘——本身不致命，但结合该 claim 是论文唯一可操作贡献，需要更显著的支撑或更谨慎的 framing。\n- 建议修改方向：(a) 在 abstract 中明确标注该增益在全局校正下为 marginal significance；(b) 在 Discussion（§8）中对这一点进行更充分的讨论；(c) 考虑增加 seed 数量以提升统计功效。\n\n### Should-Fix 问题\n\n**W1** [warning] 与 Landesberg (2026) 的差异化论述不够充分，Table 1 维度选择可能存在偏向\n- §2 末尾 \"Concurrent work\" 段仅4行；Table 1 的6个比较维度大多选取了本文占优的角度。缺少对 Landesberg 可能占优的维度的讨论。\n- 建议：扩展 concurrent work 讨论至至少一个完整段落，明确陈述 Landesberg (2026) 在哪些方面做得更好或更深入。\n\n**W2** [warning] 论文结构中实验结果分散在 §4 和 §7，逻辑连接不够清晰\n- §4 已经报告了大量实验结果，§7 又报告了更多实验结果。读者难以区分哪些结果属于 \"诊断发现\" 哪些属于 \"方法验证\"。\n- 建议：在 §4 和 §7 开头明确定位。\n\n**W3** [warning] Entity-level construction 的 inverse scaling 问题未被充分解释\n- 论文多次提到 entity-level construction 在 \"most configurations\" 下呈现 inverse scaling，但对其原因的分析不够深入。如果方法在大多数情况下是有害的，作为 \"建设性贡献\" 的价值需要质疑。\n- 建议：对 inverse scaling 给出更详细的归因分析，或明确将 entity-level construction 定位为 preliminary exploration。\n\n**W4** [warning] Related work 缺少 NER ensemble learning 经典文献\n- 完全没有提及 Florian et al. (2003) 的 NER ensemble。Diverse beam search（Vijayakumar et al., 2018）也值得讨论。\n\n### Minor\n- **M1**: Abstract \"+1.40 pp\" 与正文 \"+1.39pp\" 微小不一致。\n- **M2**: §4 第2段连续 10+ 个统计量，信息密度过高。\n- **M3**: Figure 1 \"+1.4 pp\" 在全局校正下为边缘显著，放在 overview figure 中可能造成误导。\n- **M4**: Appendix 36 页，部分关键分析需在正文中更明确引导。\n- **M5**: §3.1 符号首次出现时定义不够直观。\n\n### Questions\nQ1: 增加 seed 数量后 Holm p_adj 是否有望降至 0.05 以下？\nQ2: Landesberg (2026) 是否覆盖了 NER？\nQ3: Entity-level construction 在 Few-NERD 上表现最好，是否与 fine-grained entity type 有关？\nQ4: SQL 87.2% degeneracy 是否有计划补充完整诊断？"
  }
}
```

</details>

---


### Tool result

_source line 4921 · 2026-05-25T22:42:01.877237+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 39255
}
```

</details>

---


### Tool call

_source line 4922 · 2026-05-25T22:42:02.028235+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每一条 Must-Fix、Should-Fix、Minor 问题，用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n**一句话总结**: 一篇方法论严谨的诊断性实证研究，清晰地识别了 correlation-selection gap 作为 NER self-consistency 失败的核心障碍，但理论贡献偏薄（bound 数学上是 trivial 的），且实验范围限制在 7-14B 模型使得结论的外推性存疑。\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法使用规范，诊断框架设计合理；但退化分解上界数学上几乎是定义推导，MBR 连接是已有结论的直接应用 |\n| Excitement | 3/5 | 问题重要且实际，correlation-selection gap 概念清晰有用，但核心 insight 一旦说出并不令人意外，论文主要是解释失败而非提出有效解决方案 |\n| Reproducibility | 4/5 | 代码和数据已公开，超参数详尽，实验协议可复现；但仅 2-3 seeds 限制了独立验证的置信度 |\n\n### Must-Fix 问题\n\n**N1** [critical] 模型规模限制削弱了广泛性声明的支撑\n- 标题 \"When Self-Consistency Fails for NER\" 暗示了对 NER 上 SC 的普遍诊断，但所有实验证据仅来自 7-14B fine-tuned 模型。论文自身证据表明退化率是 scale-dependent 的：Few-NERD 低退化率下获得 +1.40pp 增益；Appendix v (Table 44) 显示 72B 模型 headroom 为 8.1pp 远高于 8B 的 1.2pp；Limitations 承认 \"frontier models exhibit markedly different degeneracy profiles (8.5-24%)\"。这构成内在张力——诊断框架预测低退化模型应从 SC 获益，但论文既没有在低退化模型上验证，也没有在标题/摘要中限定 scope。\n- 建议：（a）至少在一个 30B+ 或 proprietary model 上验证；或（b）明确限定 framing 为 \"fine-tuned 7-14B open-weight models\"。\n\n**N2** [critical] 退化分解上界（§6.3）作为理论贡献的定位不当\n- 上界 $E[\\Delta F1] \\leq (1-D) \\cdot G_{nd} \\cdot \\alpha$ 本质上是 partition 论证：将实例分为退化和非退化两组，非退化组增益不超过 oracle gap 乘以信号对齐质量。这在数学上几乎是 trivially true。Recovery ratio 3-12% 说明 bound 比实际值宽松 8-33 倍。\n- 建议：重新定位为 empirical decomposition framework 而非 theorem。移除 Theorem/Corollary 形式化框架，改为文字叙述。\n\n### Should-Fix 问题\n\n**W1** [warning] Few-NERD 的正面结果与全文 narrative 的张力未被充分利用\n- Few-NERD 在退化率 23.4%（最低）时 LP 选择获得 +1.39pp，实际上是诊断框架最有力的验证。但论文 framing 偏向 \"SC fails\"，未充分利用这一正面验证。\n- 建议：在 §8 Discussion 中将 Few-NERD 定位为框架预测能力的正面验证。\n\n**W2** [warning] 2-3 seeds 的统计推断力有限\n- Table 11 显示 LP 在 SciERC 上 95% CI 为 [-0.41, +2.34]——跨零点。\n- 建议：至少在一个核心配置上运行 5 seeds。\n\n**W3** [warning] Holm-Bonferroni 校正的 k 值选择讨论不足\n- 论文使用 global k=57 和 family-wise k=21 两种策略，未充分讨论选择标准。对于以 negative result 为主要贡献的论文，过度保守的校正导致 type II error 增加。\n- 建议：增加讨论说明 family vs. global 校正的选择标准。\n\n**W4** [warning] MBR 连接（§6.1, Proposition 1）的 novelty 声明过高\n- Proposition 1 将 entity-level majority vote 与 MBR decoding 等价性建立联系，但 MBR 在 structured prediction 中的应用是已知的，entity-wise independence 假设下的推导是 straightforward application。\n- 建议：将 Proposition 1 明确定位为 \"connecting existing MBR theory to the NER entity construction setting\"。\n\n### Minor\n- §3.1 \"capability ceiling\" 中 N≤16 的选择缺乏 justification。\n- §1 脚注 1 匿名代码链接格式正确。\n- \"MDE = 1.5pp\" 应在 §7 或 §4 中首次出现时明确说明。\n- Table 3 密集，考虑用 bar chart 替代。\n- Figure 1 右侧 \"+1.4 pp\" 仅适用于 Few-NERD，可能误导。\n\n### Questions\nQ1: 是否可以人工构造 \"低退化\" 测试场景验证框架的预测方向？\nQ2: 72B 模型的退化率是多少？\nQ3: 使用 full evaluation set（包含 zero-entity 实例）退化率会如何变化？\nQ4: Table 32 中有多少配置低于 critical degeneracy threshold？"
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
    "project": "struct_self_consist_ie",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每一条 Must-Fix、Should-Fix、Minor 问题，用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n**一句话总结**: 一篇方法论严谨的诊断性实证研究，清晰地识别了 correlation-selection gap 作为 NER self-consistency 失败的核心障碍，但理论贡献偏薄（bound 数学上是 trivial 的），且实验范围限制在 7-14B 模型使得结论的外推性存疑。\n\n### 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法使用规范，诊断框架设计合理；但退化分解上界数学上几乎是定义推导，MBR 连接是已有结论的直接应用 |\n| Excitement | 3/5 | 问题重要且实际，correlation-selection gap 概念清晰有用，但核心 insight 一旦说出并不令人意外，论文主要是解释失败而非提出有效解决方案 |\n| Reproducibility | 4/5 | 代码和数据已公开，超参数详尽，实验协议可复现；但仅 2-3 seeds 限制了独立验证的置信度 |\n\n### Must-Fix 问题\n\n**N1** [critical] 模型规模限制削弱了广泛性声明的支撑\n- 标题 \"When Self-Consistency Fails for NER\" 暗示了对 NER 上 SC 的普遍诊断，但所有实验证据仅来自 7-14B fine-tuned 模型。论文自身证据表明退化率是 scale-dependent 的：Few-NERD 低退化率下获得 +1.40pp 增益；Appendix v (Table 44) 显示 72B 模型 headroom 为 8.1pp 远高于 8B 的 1.2pp；Limitations 承认 \"frontier models exhibit markedly different degeneracy profiles (8.5-24%)\"。这构成内在张力——诊断框架预测低退化模型应从 SC 获益，但论文既没有在低退化模型上验证，也没有在标题/摘要中限定 scope。\n- 建议：（a）至少在一个 30B+ 或 proprietary model 上验证；或（b）明确限定 framing 为 \"fine-tuned 7-14B open-weight models\"。\n\n**N2** [critical] 退化分解上界（§6.3）作为理论贡献的定位不当\n- 上界 $E[\\Delta F1] \\leq (1-D) \\cdot G_{nd} \\cdot \\alpha$ 本质上是 partition 论证：将实例分为退化和非退化两组，非退化组增益不超过 oracle gap 乘以信号对齐质量。这在数学上几乎是 trivially true。Recovery ratio 3-12% 说明 bound 比实际值宽松 8-33 倍。\n- 建议：重新定位为 empirical decomposition framework 而非 theorem。移除 Theorem/Corollary 形式化框架，改为文字叙述。\n\n### Should-Fix 问题\n\n**W1** [warning] Few-NERD 的正面结果与全文 narrative 的张力未被充分利用\n- Few-NERD 在退化率 23.4%（最低）时 LP 选择获得 +1.39pp，实际上是诊断框架最有力的验证。但论文 framing 偏向 \"SC fails\"，未充分利用这一正面验证。\n- 建议：在 §8 Discussion 中将 Few-NERD 定位为框架预测能力的正面验证。\n\n**W2** [warning] 2-3 seeds 的统计推断力有限\n- Table 11 显示 LP 在 SciERC 上 95% CI 为 [-0.41, +2.34]——跨零点。\n- 建议：至少在一个核心配置上运行 5 seeds。\n\n**W3** [warning] Holm-Bonferroni 校正的 k 值选择讨论不足\n- 论文使用 global k=57 和 family-wise k=21 两种策略，未充分讨论选择标准。对于以 negative result 为主要贡献的论文，过度保守的校正导致 type II error 增加。\n- 建议：增加讨论说明 family vs. global 校正的选择标准。\n\n**W4** [warning] MBR 连接（§6.1, Proposition 1）的 novelty 声明过高\n- Proposition 1 将 entity-level majority vote 与 MBR decoding 等价性建立联系，但 MBR 在 structured prediction 中的应用是已知的，entity-wise independence 假设下的推导是 straightforward application。\n- 建议：将 Proposition 1 明确定位为 \"connecting existing MBR theory to the NER entity construction setting\"。\n\n### Minor\n- §3.1 \"capability ceiling\" 中 N≤16 的选择缺乏 justification。\n- §1 脚注 1 匿名代码链接格式正确。\n- \"MDE = 1.5pp\" 应在 §7 或 §4 中首次出现时明确说明。\n- Table 3 密集，考虑用 bar chart 替代。\n- Figure 1 右侧 \"+1.4 pp\" 仅适用于 Few-NERD，可能误导。\n\n### Questions\nQ1: 是否可以人工构造 \"低退化\" 测试场景验证框架的预测方向？\nQ2: 72B 模型的退化率是多少？\nQ3: 使用 full evaluation set（包含 zero-entity 实例）退化率会如何变化？\nQ4: Table 32 中有多少配置低于 critical degeneracy threshold？"
  }
}
```

</details>

---


### Tool result

_source line 4923 · 2026-05-25T22:42:03.493432+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1465
}
```

</details>

---


### Tool call

_source line 4924 · 2026-05-25T22:42:17.691960+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "270",
  "reason": "等待 Reviewer 1 和 Reviewer 2 完成交叉回应",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: struct_self_consist_ie\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: Main Conference (ARR)\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "270",
    "reason": "等待 Reviewer 1 和 Reviewer 2 完成交叉回应",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: struct_self_consist_ie\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: Main Conference (ARR)\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 4925 · 2026-05-25T22:42:17.743299+00:00_

Next wakeup scheduled for 22:47:00 (in 282s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 4926 · 2026-05-25T22:42:20.492827+00:00_

交叉分享已完成：
- Reviewer 1 已收到 Reviewer 2 的完整审稿意见，要求逐条 [AGREE]/[REBUT]
- Reviewer 2 已收到 Reviewer 1 的完整审稿意见，要求逐条 [AGREE]/[REBUT]

等待交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 376

## Round 376

4 recorded events


### User

_source line 4927 · 2026-05-25T22:43:32.783573+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

### Must-Fix

**[AGREE] R1-N1: 模型规模限制削弱广泛性声明**
同意这是一个实质性问题。标题 "When Self-Consistency Fails for NER" 确实暗示了普遍性结论，但所有核心证据来自 7-14B fine-tuned 模型。论文自身数据构成内在张力：Table 44（Appendix v）显示 72B 模型 oracle headroom 为 8.1pp（远高于 8B 的 1.2pp），Limitations 承认 frontier models 退化率仅 8.5-24%。诊断框架的逻辑本身就预测低退化模型应从 SC 获益——但论文没有在这些模型上验证该预测。我在自己的审稿中也注意到这一点（我的 Q3 问到 Few-NERD fine-grained entity type 对结果的影响），但 R1 的 framing 更精确：这是 claim scope 与 evidence scope 的不匹配。R1 的建议（限定标题/摘要 scope 或补充大模型实验）合理且可操作。

**[AGREE] R1-N2: 退化分解上界作为理论贡献的定位不当**
同意。上界 $E[\Delta F1] \leq (1-D) \cdot G_{nd} \cdot \alpha$ 本质上是一个分组恒等式加上 trivial 的上界约束：退化实例增益为零，非退化实例增益不超过 oracle gap × 信号对齐质量。Recovery ratio 仅 3-12%（Table 32, Appendix r.4）说明 bound 极度宽松。以 Theorem/Corollary 形式呈现让读者预期非平凡的理论贡献，但实际数学深度不支持这一预期。不过我要补充：虽然 bound 本身是 trivial 的，但将增益分解为 (1-D)、G_nd、α 三个可独立量化的因子在**诊断层面**是有用的——它让研究者知道该去改善哪个因子。所以问题不在于分解本身没有价值，而在于用 Theorem 格式 overclaim 了数学贡献的层次。同意 R1 的建议：重新定位为 empirical decomposition framework。

---

### Should-Fix

**[AGREE] R1-W1: Few-NERD 正面结果与全文 narrative 的张力**
同意。这其实是论文的一个叙事失误。Few-NERD（退化率最低 23.4%，Table 14/Appendix c）上 LP 获得 +1.39pp（Table 4），是诊断框架预测能力的最佳正面验证：框架预测低退化 + 较好信号对齐 → SC 应该有效，Few-NERD 验证了这一预测。但论文的 framing 过度偏向 "SC fails" 叙事，把 Few-NERD 当作例外而非验证。如果在 §8 Discussion 中将其重构为 "框架不仅诊断失败，也预测成功"，会显著增强论文的说服力。

**[AGREE] R1-W2: 2-3 seeds 统计推断力有限**
完全同意。这也是我在自己审稿中指出的问题（我的 N2、Q1）。Table 11 的 LP on SciERC 95% CI [-0.41, +2.34] 跨零点，说明 2-3 seeds 下的 bootstrap CI 无法可靠区分真实增益和噪声。对于一篇以统计严谨性为卖点的论文（Holm-Bonferroni 校正、TOST equivalence testing、bootstrap CI），仅 2-3 seeds 的基础设计与上层统计方法的精密度之间存在不匹配。R1 的建议（至少一个核心配置 5 seeds）是合理的最低要求。

**[REBUT] R1-W3: Holm-Bonferroni k 值选择讨论不足**
部分不同意 R1 的推理方向。R1 认为 "对于以 negative result 为主要贡献的论文，过度保守的校正导致 type II error 增加"——但这个论点是双刃剑。论文的核心 claim 实际上包含两类：(a) negative claim（SC 不改善 NER），(b) positive claim（LP selection 在特定条件下有效）。对于 (a)，论文已使用 TOST equivalence testing（Appendix c, Table 15）来直接论证 null effect，这不依赖于 Holm 校正。对于 (b)，k=57 的全局校正是保守的，但 family-wise k=21 得到 SJ +LP p=0.013（§7.2），已经提供了 within-family 的显著性证据。论文同时报告了两种校正策略（§7.2 和 Appendix c），我认为这是合理的——它让读者自行判断哪个 granularity 的 multiplicity 校正更合适。真正的问题不在 k 值选择，而在 seed 数量（W2），因为即使放松校正也无法弥补 power 不足。

**[AGREE] R1-W4: MBR 连接 novelty 声明过高**
同意。Proposition 1 建立的 entity-level MV 与 MBR 等价性，在 entity-wise independence 假设下是标准 MBR 理论（Eikema and Aziz, 2022; Kumar and Byrne, 2004）的直接应用。该连接在概念上有用（帮助理解为什么 entity construction 在某些条件下有效），但不构成独立的理论贡献。同意 R1 的建议：定位为 "connecting existing MBR theory to the NER entity construction setting" 而非原创理论结果。

---

### Minor

**[AGREE] R1-M1: N≤16 justification**
同意。§3.1 提到 N≤16 作为 "realistic sample budgets" 但没有给出为什么 16 是 realistic 的上限。考虑到 Figure 5 和 Appendix aj（Table 40, 42）分析了 N 最大到 64 的 scaling，§3.1 应该解释 N=16 的选择依据（计算成本？收益饱和点？）。

**[AGREE] R1-M2: MDE 定义位置**
同意。MDE≈1.5pp 是理解论文统计 power 的关键参数，应在 §4 或 §7 首次出现时定义，而非仅在 Limitations 中出现。

**[REBUT] R1-M3: Table 3 密集，建议用 bar chart 替代**
不同意。Table 3 包含 5 signals × 4 datasets × 3 metrics 的细粒度数据，bar chart 在这种高维度比较中会损失信息密度且占用更多版面。当前 table 格式对专业读者更高效。不过可以考虑在 table 中用颜色/粗体突出关键数字以提高可读性。

**[AGREE] R1-M4: Figure 1 "+1.4 pp" 范围**
同意。这也是我在自己的审稿中指出的（我的 M3）。Figure 1 右侧面板标注 "+1.4 pp" 但这仅适用于 Few-NERD 的 LP selection，在 overview figure 中不加限定地展示可能误导读者认为这是普遍增益。

---

### 对 R1 Questions 的补充

R1-Q2 问 72B 退化率——这个数据应该在 Table 44（Appendix v）中，论文提到 72B headroom 为 8.1pp 但退化率数据是否完整报告值得确认。

R1-Q4 问 Table 32 中有多少配置低于 critical degeneracy threshold——这是一个好问题。Table 32 验证了所有配置的 recovery ratio 为 3-12%，但没有直接报告有多少配置的 D < D_crit。如果大多数配置都在 D_crit 之上，这进一步支持论文的 negative conclusion；反之则需要解释为什么 bound 依然如此宽松。

---

### 总结

与 R1 在大方向上高度一致：论文是扎实的诊断性工作，但存在 claim scope 与 evidence scope 的不匹配（N1）、理论贡献 overclaimed（N2），以及统计 power 不足（W2）。我的额外关切是 SQL 跨任务证据过于薄弱（我的 N1）和全局 Holm p_adj=0.055（我的 N2），这些与 R1 的关切互补。综合来看，论文需要在 framing（收窄 claim scope）和统计（增加 seeds）上做实质性修订才能达到 main conference 水平；当前状态适合 Findings。

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

_source line 4928 · 2026-05-25T22:43:57.952508+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "180",
  "reason": "等待 Reviewer 1 完成对 Reviewer 2 的交叉回应",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: struct_self_consist_ie\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: Main Conference (ARR)\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "180",
    "reason": "等待 Reviewer 1 完成对 Reviewer 2 的交叉回应",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: struct_self_consist_ie\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: Main Conference (ARR)\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 4929 · 2026-05-25T22:43:58.003090+00:00_

Next wakeup scheduled for 22:47:00 (in 182s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 4930 · 2026-05-25T22:44:20.659822+00:00_

Reviewer 2 交叉回应已收到。与 R1 高度一致（5 AGREE / 1 REBUT on should-fix）。唯一分歧点：R1-W3（Holm k 值讨论）——R2 认为真正问题在 seed 数量而非 k 值选择。

等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 377

## Round 377

18 recorded events


### User

_source line 4931 · 2026-05-25T22:44:21.732279+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R2-N1: SQL 跨任务证据严重不足**

同意 R2 的判断。我在审稿中虽未将此列为独立 issue，但回顾论文确认 R2 的观察是准确的：Abstract 第 5 句 "Cross-task pilots on relation extraction (RE) and SQL parsing **confirm** task-specific failure modes" 中 "confirm" 一词暗示了系统性验证，但 SQL 的实际证据仅为 §7.1 中一个退化率统计量（87.2%, n=196）和 Appendix ah "O1" 中一句话。与 RE 的完整分析（Appendix q 有 LP selection、pairwise overlap、flip instances、free-form decoding comparison）相比，SQL 的分析深度不成比例。

R2 的修改建议合理——将 SQL 降级为 "anecdotal evidence" 或从 abstract 中移除是最小成本修改。补充完整分析更好但工作量大。

补充一点 R2 未提及的：Appendix ah "O1" 仅引用了一个外部结果（Spider SQL, GPT-3.5），而非本文的 fine-tuned 模型。这意味着 SQL 的退化率不能与本文 NER 实验中的退化率直接对比（不同模型、不同 prompting 策略），进一步削弱了其作为跨任务验证的证据力。

---

**[REBUT] R2-N2: 全局统计显著性边缘——严重程度被高估**

R2 将此列为 critical must-fix，我认为严重程度应降级为 **should-fix**。理由如下：

**1. 论文的核心贡献是诊断性的，非建设性的。** 论文的主要 contribution 是 correlation-selection gap 的识别和诊断框架（§3），而非 LP selection 增益。§8 Discussion 的定位是 "primarily diagnostic"（原文 Appendix ae 明确定位为 "prescriptive protocol"），+1.40pp 是框架预测能力的验证而非论文的核心 claim。R2 称其为 "论文唯一可操作贡献" 忽略了诊断协议本身（Appendix ae 三步协议）的可操作性。

**2. Family-wise 校正下该结果是 significant 的。** 论文在 §7.2 提及 "Under seed-replication Holm-Bonferroni correction (k=3 seeds), the SJ > LP advantage reaches p_adj=0.013"。Table 12 (Appendix f) 的 family-wise k 值远小于 global k=57，在 family 层面 LP 的选择增益是 significant 的。Global k=57 校正将 57 个不同性质的检验合并——包括跨信号、跨数据集、跨任务等完全不同的比较——是否过度保守，本身就值得讨论（我自己的 W3 也提出了这一点）。

**3. 但 framing 确实需要更谨慎。** 我同意 R2 指出的 abstract 中 "+1.40 percentage points" 作为唯一具体数字被突出的问题。建议在 abstract 中加入 qualifier（如 "marginally significant under global correction"），并在 §7.2 正文中更显著地标注。

综上：这是一个 framing/presentation issue（should-fix），而非 evidence insufficiency issue（must-fix）。论文的核心 claim——SC 在高退化条件下失效——由 TOST 等效性检验充分支持（Table 15），不依赖于 +1.40pp 增益的显著性。

---

### Should-Fix 问题

**[AGREE] R2-W1: 与 Landesberg (2026) 的差异化讨论不足**

同意。§2 末尾的 concurrent work 段确实过短（约 4 行）。Table 1 的 6 个比较维度（instance-level diagnostics, prompt-level decomposition, degeneracy analysis, LP connection, free-form comparison, prescriptive protocol）均为本文占优的角度，没有展示 Landesberg 在哪些方面可能做得更好或更深入。这种单方面比较容易让审稿人质疑客观性。

R2 建议扩展至至少一个完整段落并陈述 Landesberg 的优势，我支持这一建议。

---

**[REBUT] R2-W2: 实验结果分散在 §4 和 §7 的结构问题**

部分不同意。§4 和 §7 的分工在我的阅读中是清晰的：

- §4 "Single-Signal Selection Results" 报告的是**单一信号的诊断发现**——在 SciERC 主配置上各信号的 AUROC、Spearman ρ 和选择增益（Table 2, Figure 2），目的是建立 "信号能估计质量但无法提升选择" 的核心发现。
- §7 "Cross-Dataset Experiments" 报告的是**诊断框架的外部验证**——在 CoNLL、Few-NERD、WNUT-17 上验证核心发现的一致性（Table 4），以及退化-LP 相关性（§7.1）、seed replication（§7.4）等 robustness 检查。

这种 "建立核心发现 → 外部验证" 的结构在 empirical NLP 论文中是常见的。但 R2 的感受可能代表了部分读者的体验，建议在 §4 和 §7 开头各加一句定位性声明（如 "This section establishes the core diagnostic findings on our primary configuration" 和 "This section validates the generality of the diagnostic framework"）。这是 minor revision 而非 should-fix 级别。

---

**[AGREE] R2-W3: Entity-level construction 的 inverse scaling 问题**

同意。这与我自己审稿中的观察一致。论文在 Table 3 (page 6) 列出 entity construction（EC）在多个配置下的表现，在 Table 4 中 EC 跨数据集结果为 ΔF1=+0.42 (Few-NERD) 但 SciERC 为 -0.42、CoNLL 仅 -1.02 (Table 3 中 cross-model)。§6.2 提到 "Few-best selection advantage transitions from +1.5pp (compressed) to +4.6pp (non-compressed; Appendix o)"，但在大部分标准配置下 construction gains 是 negative 或 negligible。

如果 entity-level construction 在大多数配置下是 harmful 的，将其作为论文的 constructive contribution 需要更强的 qualification。R2 建议 "明确将 entity-level construction 定位为 preliminary exploration" 是合理的。

---

**[REBUT] R2-W4: Related work 缺少 NER ensemble learning 经典文献**

部分不同意。

- **Florian et al. (2003)** 是 supervised NER ensemble 工作，使用不同特征集/模型的组合。本文研究的是 **同一模型多次采样的 self-consistency**，属于 inference-time 策略而非 training-time ensemble。两者的 aggregation 机制、假设和适用场景有本质差异。引用可以但不是必要的。

- **Diverse beam search (Vijayakumar et al., 2018)** 更相关，因为它涉及 decoding 阶段的多样性，与 self-consistency 的 diversity 问题直接相关。但本文使用 temperature sampling 而非 beam search 来生成多样化样本——§3 和 Appendix b (Table 6) 的 temperature robustness 分析已经覆盖了采样多样性问题。Vijayakumar et al. 可作为 additional reference 但不是 gap。

建议：在 Related Work 中用一句话提及 supervised NER ensemble 和 diverse decoding 作为更广泛的 context，但这是 minor issue 而非 should-fix。

---

### Minor 问题

**[AGREE] R2-M1**: +1.40pp vs +1.39pp 不一致。数值差异来自四舍五入（1.395 → 1.40 in abstract, 1.39 in text），应统一。

**[AGREE] R2-M2**: §4 第 2 段确实信息密度过高。建议将部分统计量移至 Table。

**[AGREE] R2-M3**: Figure 1 中 "+1.4 pp" 在全局校正下为边缘显著，放在 overview figure 中确实可能误导。这与 N2 的 framing 问题相关——如果 +1.4pp 不作为核心 claim，就不应在 Figure 1 中突出。

**[AGREE] R2-M4**: Appendix 36 页，正文对关键 appendix 分析的引导确实不足。特别是 Appendix i (self-verification)、Appendix s (free-form decoding)、Appendix x (cross-dataset OOD) 包含重要分析，但正文中的指引较隐蔽。

**[AGREE] R2-M5**: §3.1 符号定义可改善，首次出现时缺乏直觉解释。Table 5 (symbol table) 在 Appendix 而非正文，读者需来回翻阅。

---

### 对 R2 Questions 的意见

**Q1 (增加 seed 后 Holm p_adj 是否降至 0.05 以下)**: 这是一个合理的问题。Appendix ad.2 (Table 61) 的功效分析显示 n=5 seeds 在 ρ=0.3 时达到 80% power，增加到 5 seeds 可能足以使 p_adj 降至显著水平。但这取决于效应量是否稳定。

**Q2 (Landesberg 是否覆盖 NER)**: 论文 §2 末尾提到 Landesberg (2026) 是 concurrent work，但未明确说明其是否覆盖 NER。Table 1 的比较暗示 Landesberg 覆盖了部分相同的任务但分析角度不同。这个信息应该在论文中明确说明。

**Q3 (Few-NERD 与 fine-grained entity type 的关系)**: 这与我自己的 Q1 呼应。Few-NERD 的 66 个 fine-grained entity types 可能导致模型预测的多样性更高、退化率更低。这是论文应该深入分析的方向。

**Q4 (SQL 完整诊断)**: 同意 R2 的关切。如果保留 SQL 作为跨任务证据，必须补充完整诊断。


---

[Reviewer 2 审稿结果]:
交叉回应已提交。与 R1 在核心问题上高度一致（模型规模限制 N1、理论 overclaim N2、统计 power 不足 W2），仅在 Holm k 值选择（W3）和 Table 3 格式（M3）上持不同意见。我补充了 R1 未覆盖的两个关切：SQL 跨任务证据不足和全局 p_adj=0.055 的边缘显著性问题。综合判断维持 3.5（Borderline Conference），建议 Findings 可接收。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **R2-N1 (SQL证据不足)**: [AGREE]，SQL 仅一个退化率数字，abstract 用 "confirm" 过度声明
- **R2-N2 (Holm p=0.055)**: [REBUT]，严重程度应降为 should-fix——论文核心贡献是诊断性的而非建设性的，family-wise 校正下结果显著，但同意 abstract framing 需更谨慎
- **R2-W1 (Landesberg对比不足)**: [AGREE]
- **R2-W2 (§4/§7结构)**: [REBUT]，分工逻辑清晰，但建议加定位声明
- **R2-W3 (construction inverse scaling)**: [AGREE]，大多数配置下 harmful，不宜作为核心建设性贡献
- **R2-W4 (缺少ensemble文献)**: [REBUT]，Florian et al. 是 supervised ensemble 而非 SC，领域不同；Vijayakumar 可加但非必要
- **M1-M5**: 全部 [AGREE]

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

_source line 4932 · 2026-05-25T22:45:04.010835+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

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
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 4933 · 2026-05-25T22:45:04.312363+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T22:31:20.896765+00:00\", \"completed_at\": \"2026-05-25T22:36:21.116592+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent timed out after 300s\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 4934 · 2026-05-25T22:45:04.312700+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

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
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 4935 · 2026-05-25T22:45:04.413322+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 4936 · 2026-05-25T22:45:11.484291+00:00_

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

_source line 4937 · 2026-05-25T22:45:11.585059+00:00_

No matching deferred tools found

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

_source line 4938 · 2026-05-25T22:45:15.950191+00:00_

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

_source line 4939 · 2026-05-25T22:45:16.101225+00:00_

issues:
# ===== ROUND 45 MUST-FIX (CONSENSUS) =====
- id: R45-N1
  summary: "模型覆盖面过窄（仅 2 个 ~8B 模型族），标题/摘要普适性声称超出证据范围"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 43
  last_seen_round: 45
  mentions:
    - round: 43
      reviewers: [1, 2]
      note: "R43-W5 作为 warning 提出，已通过 Limitations 声明部分解决"
    - round: 45
      reviewers: [1, 2]
      note: "R1 升级为 Must-Fix (N2)。R2 AGREE。Table 43 显示 degeneracy 是 model-family-dependent。"
  action_items:
    - round: 45
      action: "收紧 title/abstract/intro 的普适性表述，显式限定为 7-14B fine-tuned models"
      assigned_to: paper_agent
      status: in_progress

# ===== ROUND 45 SHOULD-FIX =====
- id: R45-W1
  summary: "Entity construction 统计边际（global Holm p_adj=0.055）且在 abstract/Figure 1 中展示权重过高"
  category: method
  severity: warning
  status: in_progress
  first_raised_round: 34
  last_seen_round: 45
  mentions:
    - round: 43
      reviewers: [1, 2]
      note: "R43-N4 prescriptive→exploratory 重定位已解决"
    - round: 45
      reviewers: [1, 2]
      note: "R2-W3 提出全局 Holm 不显著。R1 strongly AGREE。Figure 1 '+1.4pp' 是单个配置非聚合。"
  action_items:
    - round: 45
      action: "降低 entity construction 在 abstract/Figure 1 中的突出程度；Figure 1 标注 '+1.4pp' 为单配置结果"
      assigned_to: paper_agent
      status: in_progress

- id: R45-W2
  summary: "与 Landesberg (2026) 并行发现的差异化论述不够充分"
  category: framing
  severity: warning
  status: in_progress
  first_raised_round: 39
  last_seen_round: 45
  mentions:
    - round: 42
      reviewers: [1, 2]
      note: "R41-N4 通过 §2 四维度对比解决"
    - round: 45
      reviewers: [1, 2]
      note: "R2-W1 重新提出。R1 AGREE。§2 末尾 concurrent work 段过于简短。"
  action_items:
    - round: 45
      action: "Introduction 中增加一段明确说明与 Landesberg 的关系，强调增量贡献是诊断框架而非 gap 发现本身"
      assigned_to: paper_agent
      status: in_progress

- id: R45-W3
  summary: "Failure mode 四种模式的层次化关系未显式形式化"
  category: method
  severity: warning
  status: in_progress
  first_raised_round: 45
  last_seen_round: 45
  mentions:

…[truncated 297 chars]

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

_source line 4940 · 2026-05-25T22:45:20.568037+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null | wc -l",
  "description": "Count total lines in review_issues.yaml"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null | wc -l",
    "description": "Count total lines in review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 4941 · 2026-05-25T22:45:20.669368+00:00_

367

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

_source line 4942 · 2026-05-25T22:45:25.286940+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "0",
  "limit": "367"
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
    "offset": "0",
    "limit": "367"
  }
}
```

</details>

---


### Tool result

_source line 4943 · 2026-05-25T22:45:25.337844+00:00_

0	issues:
1	# ===== ROUND 45 MUST-FIX (CONSENSUS) =====
2	- id: R45-N1
3	  summary: "模型覆盖面过窄（仅 2 个 ~8B 模型族），标题/摘要普适性声称超出证据范围"
4	  category: experiment
5	  severity: critical
6	  status: in_progress
7	  first_raised_round: 43
8	  last_seen_round: 45
9	  mentions:
10	    - round: 43
11	      reviewers: [1, 2]
12	      note: "R43-W5 作为 warning 提出，已通过 Limitations 声明部分解决"
13	    - round: 45
14	      reviewers: [1, 2]
15	      note: "R1 升级为 Must-Fix (N2)。R2 AGREE。Table 43 显示 degeneracy 是 model-family-dependent。"
16	  action_items:
17	    - round: 45
18	      action: "收紧 title/abstract/intro 的普适性表述，显式限定为 7-14B fine-tuned models"
19	      assigned_to: paper_agent
20	      status: in_progress
21	
22	# ===== ROUND 45 SHOULD-FIX =====
23	- id: R45-W1
24	  summary: "Entity construction 统计边际（global Holm p_adj=0.055）且在 abstract/Figure 1 中展示权重过高"
25	  category: method
26	  severity: warning
27	  status: in_progress
28	  first_raised_round: 34
29	  last_seen_round: 45
30	  mentions:
31	    - round: 43
32	      reviewers: [1, 2]
33	      note: "R43-N4 prescriptive→exploratory 重定位已解决"
34	    - round: 45
35	      reviewers: [1, 2]
36	      note: "R2-W3 提出全局 Holm 不显著。R1 strongly AGREE。Figure 1 '+1.4pp' 是单个配置非聚合。"
37	  action_items:
38	    - round: 45
39	      action: "降低 entity construction 在 abstract/Figure 1 中的突出程度；Figure 1 标注 '+1.4pp' 为单配置结果"
40	      assigned_to: paper_agent
41	      status: in_progress
42	
43	- id: R45-W2
44	  summary: "与 Landesberg (2026) 并行发现的差异化论述不够充分"
45	  category: framing
46	  severity: warning
47	  status: in_progress
48	  first_raised_round: 39
49	  last_seen_round: 45
50	  mentions:
51	    - round: 42
52	      reviewers: [1, 2]
53	      note: "R41-N4 通过 §2 四维度对比解决"
54	    - round: 45
55	      reviewers: [1, 2]
56	      note: "R2-W1 重新提出。R1 AGREE。§2 末尾 concurrent work 段过于简短。"
57	  action_items:
58	    - round: 45
59	      action: "Introduction 中增加一段明确说明与 Landesberg 的关系，强调增量贡献是诊断框架而非 gap 发现本身"
60	      assigned_to: paper_agent
61	      status: in_progress
6
…[truncated 8712 chars]

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

_source line 4944 · 2026-05-25T22:47:45.067944+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== ROUND 46 MUST-FIX (CONSENSUS) =====\n- id: R45-N1\n  summary: \"模型覆盖面过窄（仅 2 个 ~8B 模型族），标题/摘要普适性声称超出证据范围\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 43\n  last_seen_round: 46\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-W5 作为 warning 提出，已通过 Limitations 声明部分解决\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1 升级为 Must-Fix (N2)。R2 AGREE。Table 43 显示 degeneracy 是 model-family-dependent。\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R1-N1 再次提出。R2 AGREE。论文自身数据构成内在张力：Table 44 显示 72B headroom 8.1pp，Limitations 承认 frontier degeneracy 8.5-24%，但框架预测低退化→SC 有效的方向未在大模型上验证。\"\n  action_items:\n    - round: 45\n      action: \"收紧 title/abstract/intro 的普适性表述，显式限定为 7-14B fine-tuned models\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 46\n      action: \"标题/摘要明确限定为 fine-tuned 7-14B open-weight models；或补充至少一个 30B+/proprietary 模型验证\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R46-N2\n  summary: \"退化分解上界（§6.3）数学上 trivial（partition 定义直接推出），以 Theorem/Corollary 形式 overclaim 理论贡献\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 38\n  last_seen_round: 46\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-N2 通过三阶段重构解决，bound 不再独立贡献。标记 resolved。\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R1-N2 重新提出。R2 AGREE。上界本质是分组恒等式+trivial 约束，recovery ratio 3-12% 极度宽松。但 R2 补充：分解为 (1-D)·G_nd·α 三个可独立量化因子在诊断层面有用，问题在于用 Theorem 格式 overclaim 数学贡献。\"\n  action_items:\n    - round: 46\n      action: \"将 §6.3 从 Theorem/Corollary 形式重新定位为 empirical decomposition framework；移除形式化证明框架，改用文字叙述分解的诊断价值\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R46-N3\n  summary: \"SQL 跨任务证据仅一个退化率数字（87.2%），与 abstract 'confirm task-specific failure modes' 声明严重不匹配\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 37\n  last_seen_round: 46\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-W2 通过 abstract 加 'preliminary cross-task pilots' 限定词解决。标记 resolved。\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2-N1 重新提出，R1 AGREE 并补充：Appendix ah SQL 引用的是外部结果（GPT-3.5）而非本文 fine-tuned 模型，不能与 NER 退化率直接对比。Abstract 用 'confirm' 一词暗示系统性验证，但 SQL 实际证据仅一个统计量。\"\n  action_items:\n    - round: 46\n      action: \"将 SQL 从 abstract 中移除或降级为 'anecdotal observation'；或补充 SQL 的完整信号分析和 selection 实验\"\n      assigned_to: paper_agent\n      status: open\n\n# ===== ROUND 46 SHOULD-FIX =====\n- id: R46-W1\n  summary: \"Few-NERD 正面结果（+1.39pp）未被充分利用为诊断框架预测能力的正面验证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 46\n  last_seen_round: 46\n  mentions:\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R1-W1 提出，R2 AGREE。Few-NERD 退化率最低(13%)时 LP 获得 +1.39pp，是框架 '低退化→SC 有效' 预测的最佳正面验证。但论文 framing 偏向 'SC fails'，把 Few-NERD 当作例外而非验证。\"\n  action_items:\n    - round: 46\n      action: \"在 §8 Discussion 中将 Few-NERD 重构为框架预测能力的正面验证（'框架不仅诊断失败，也预测成功'）；补充 Few-NERD 低退化原因分析\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R46-W2\n  summary: \"Entity construction +1.40pp 在全局 Holm 校正下 p_adj=0.055，abstract/Figure 1 中 framing 过于突出\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 34\n  last_seen_round: 46\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-N4 通过 prescriptive→exploratory 重定位解决\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2-W3 重提，R1 AGREE\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2 列为 Must-Fix(N2)，但 R1 REBUT 降级为 should-fix：核心贡献是诊断性的非建设性的，family-wise k=21 下 p=0.013 是 significant 的。Director 判定 should-fix——R1 论据充分（核心 claim 由 TOST 支撑，+1.40pp 是框架验证非核心 claim），但 abstract framing 确实需更谨慎。\"\n  action_items:\n    - round: 46\n      action: \"Abstract 中为 +1.40pp 加 qualifier（如 'marginally significant under global correction'）；Figure 1 标注 '+1.4pp' 为单配置/单数据集结果\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R45-W2\n  summary: \"与 Landesberg (2026) 并行发现的差异化论述不够充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 39\n  last_seen_round: 46\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R41-N4 通过 §2 四维度对比解决\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2-W1 重新提出。R1 AGREE。§2 末尾 concurrent work 段过于简短。\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2-W1 再次提出，R1 AGREE。§2 concurrent work 段仍仅约4行，Table 1 维度选择单方面偏向本文。需扩展至完整段落并承认 Landesberg 优势。\"\n  action_items:\n    - round: 45\n      action: \"Introduction 中增加一段明确说明与 Landesberg 的关系\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 46\n      action: \"§2 concurrent work 扩展至至少一个完整段落，明确陈述 Landesberg 在哪些方面更深入，以及本文在哪些方面互补\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R45-W4\n  summary: \"2-3 seeds 统计推断力有限，seed-level variance 估计基础不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 40\n  last_seen_round: 46\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-N1 通过 power-aware negative claims 解决\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1-W2。R2 AGREE。cross-seed 变异分析仅 3 个数据点。\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R1-W2 再次提出，R2 AGREE。Table 11 LP on SciERC 95% CI [-0.41, +2.34] 跨零点。2-3 seeds 的基础设计与上层统计方法的精密度之间存在不匹配。\"\n  action_items:\n    - round: 46\n      action: \"至少在一个核心配置（如 SciERC Qwen3-8B）上运行 5 seeds，验证 bootstrap CI 稳定性\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R46-W5\n  summary: \"MBR 连接（§6.1, Proposition 1）novelty 声明过高，本质是已知 MBR 理论的直接应用\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 46\n  last_seen_round: 46\n  mentions:\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 AGREE。Proposition 1 在 entity-wise independence 假设下是标准 MBR 理论的直接应用。概念上有用但不构成独立理论贡献。\"\n  action_items:\n    - round: 46\n      action: \"将 Proposition 1 定位为 'connecting existing MBR theory to NER entity construction' 而非原创理论结果；正文中说明 entity-wise independence 局限性\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R46-W6\n  summary: \"Entity-level construction 在大多数配置下呈 inverse scaling，作为建设性贡献价值存疑\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 46\n  last_seen_round: 46\n  mentions:\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2-W3 提出，R1 AGREE。40/58 transitions 呈 inverse scaling，但归因分析不够深入。如果方法在大多数配置下有害，'建设性贡献'定位需更强 qualification。\"\n  action_items:\n    - round: 46\n      action: \"对 inverse scaling 给出更详细归因分析；或明确将 entity-level construction 定位为 preliminary exploration\"\n      assigned_to: paper_agent\n      status: open\n\n# ===== ROUND 46 MINOR =====\n- id: R46-M1\n  summary: \"Abstract '+1.40pp' 与正文 '+1.39pp' 四舍五入不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 46\n  last_seen_round: 46\n  mentions:\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2-M1，R1 AGREE。\"\n\n- id: R46-M2\n  summary: \"§4 第2段信息密度过高（10+统计量连续出现）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 46\n  last_seen_round: 46\n  mentions:\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2-M2，R1 AGREE。\"\n\n- id: R46-M3\n  summary: \"Figure 1 '+1.4pp' 仅适用于 Few-NERD，在 overview figure 中不加限定可能误导\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 45\n  last_seen_round: 46\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R45-M1 相关\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2-M3 和 R1 Minor 均提出。在全局校正下为边缘显著，overview figure 中不限定数据集可能误导。\"\n\n- id: R46-M4\n  summary: \"Appendix 36 页，正文对关键 appendix 分析的引导不足\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 46\n  last_seen_round: 46\n  mentions:\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2-M4，R1 AGREE。特别是 Appendix i/s/x 包含重要分析但正文指引隐蔽。\"\n\n- id: R46-M5\n  summary: \"§3.1 符号首次出现时定义不够直观，Table 5 符号表在 Appendix 较远\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 46\n  mentions:\n    - round: 43\n      reviewers: [2]\n      note: \"R43-M4\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2-M5，R1 AGREE。\"\n\n- id: R46-M6\n  summary: \"MDE≈1.5pp 应在 §4 或 §7 首次出现时定义，而非仅在 Limitations 中\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 46\n  last_seen_round: 46\n  mentions:\n    - round: 46\n      reviewers: [1]\n      note: \"R1 Minor。\"\n\n- id: R46-M7\n  summary: \"§3.1 'capability ceiling' 中 N≤16 缺乏选择依据说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 46\n  last_seen_round: 46\n  mentions:\n    - round: 46\n      reviewers: [1]\n      note: \"R1 Minor。Appendix n 分析了 N 到 32，应在正文解释 N=16 的选择理由。\"\n\n# ===== ROUND 45 遗留（本轮未提及） =====\n- id: R45-W3\n  summary: \"Failure mode 四种模式的层次化关系未显式形式化\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1-N1 (critical)。R2 REBUT 降级为 should-fix。Director 判定 should-fix。\"\n    - round: 46\n      reviewers: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n\n- id: R45-W5\n  summary: \"Table 1 novelty comparison 维度选择偏向本文\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 43\n  last_seen_round: 46\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2-W2 重提。R1 AGREE。\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"合并入 R45-W2 (Landesberg 差异化)，R2-W1 再次提出 Table 1 偏向问题。\"\n\n- id: R45-W6\n  summary: \"实践指导（Appendix ah/ae）在主文可见性不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2-W4 提出缺乏实践指导。R1 REBUT——可见性问题非缺失问题。\"\n    - round: 46\n      reviewers: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n\n- id: R45-M1\n  summary: \"Figure 2 标记点小、线条细\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 46\n      reviewers: []\n      note: \"本轮未提及\"\n\n- id: R45-M2\n  summary: \"MBR 缩写在 abstract/introduction 中未展开全称\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 46\n      reviewers: []\n      note: \"本轮未提及\"\n\n- id: R43-M1\n  summary: \"Footnote 1 (RE F1 confound) 建议提升到正文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 46\n      reviewers: []\n      note: \"本轮未提及\"\n\n- id: R43-M3\n  summary: \"§3 应在首段明确提及 diagnostic sequence 而非 causal chain\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 46\n      reviewers: []\n      note: \"本轮未提及，可能已修复\"\n\n# ===== EARLIER ROUNDS — RESOLVED (精简保留) =====\n- id: R43-N1\n  summary: \"2-3 seeds 统计推断力不足，核心 negative claims 无法区分真无效应和检测力不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 43\n  resolution: \"全文 negative claims 改为 'yields no detectable gains'，加 MDE ~1.5pp/CI 限定。\"\n  resolution_round: 43\n\n- id: R43-N3\n  summary: \"观察性设计下因果措辞系统性过强\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 43\n  resolution: \"全文因果措辞替换为关联/观察性表述。\"\n  resolution_round: 43\n\n- id: R43-N5\n  summary: \"标题 'Why SC Fails for NER' 与正文 conditional success 结论不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 43\n  resolution: \"标题改 'When Self-Consistency Fails for NER'。\"\n  resolution_round: 43\n\n- id: R43-W1\n  summary: \"Few-NERD 3-epoch vs 5-epoch 混淆未充分解决\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 43\n  resolution: \"Greedy 0.748 vs 0.798 说明已加。\"\n  resolution_round: 43\n\n- id: R43-W3\n  summary: \"正文数字密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 37\n  last_seen_round: 43\n  resolution: \"Abstract 精简为 6 个关键数字。\"\n  resolution_round: 43\n\n- id: R43-M2\n  summary: \"Mechanistic evidence 在 Appendix 却作为正文贡献点列出\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 43\n  resolution: \"三阶段结构不再将 mechanistic evidence 列为独立贡献。\"\n  resolution_round: 43"
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
    "issues_yaml": "issues:\n# ===== ROUND 46 MUST-FIX (CONSENSUS) =====\n- id: R45-N1\n  summary: \"模型覆盖面过窄（仅 2 个 ~8B 模型族），标题/摘要普适性声称超出证据范围\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 43\n  last_seen_round: 46\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-W5 作为 warning 提出，已通过 Limitations 声明部分解决\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1 升级为 Must-Fix (N2)。R2 AGREE。Table 43 显示 degeneracy 是 model-family-dependent。\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R1-N1 再次提出。R2 AGREE。论文自身数据构成内在张力：Table 44 显示 72B headroom 8.1pp，Limitations 承认 frontier degeneracy 8.5-24%，但框架预测低退化→SC 有效的方向未在大模型上验证。\"\n  action_items:\n    - round: 45\n      action: \"收紧 title/abstract/intro 的普适性表述，显式限定为 7-14B fine-tuned models\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 46\n      action: \"标题/摘要明确限定为 fine-tuned 7-14B open-weight models；或补充至少一个 30B+/proprietary 模型验证\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R46-N2\n  summary: \"退化分解上界（§6.3）数学上 trivial（partition 定义直接推出），以 Theorem/Corollary 形式 overclaim 理论贡献\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 38\n  last_seen_round: 46\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-N2 通过三阶段重构解决，bound 不再独立贡献。标记 resolved。\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R1-N2 重新提出。R2 AGREE。上界本质是分组恒等式+trivial 约束，recovery ratio 3-12% 极度宽松。但 R2 补充：分解为 (1-D)·G_nd·α 三个可独立量化因子在诊断层面有用，问题在于用 Theorem 格式 overclaim 数学贡献。\"\n  action_items:\n    - round: 46\n      action: \"将 §6.3 从 Theorem/Corollary 形式重新定位为 empirical decomposition framework；移除形式化证明框架，改用文字叙述分解的诊断价值\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R46-N3\n  summary: \"SQL 跨任务证据仅一个退化率数字（87.2%），与 abstract 'confirm task-specific failure modes' 声明严重不匹配\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 37\n  last_seen_round: 46\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-W2 通过 abstract 加 'preliminary cross-task pilots' 限定词解决。标记 resolved。\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2-N1 重新提出，R1 AGREE 并补充：Appendix ah SQL 引用的是外部结果（GPT-3.5）而非本文 fine-tuned 模型，不能与 NER 退化率直接对比。Abstract 用 'confirm' 一词暗示系统性验证，但 SQL 实际证据仅一个统计量。\"\n  action_items:\n    - round: 46\n      action: \"将 SQL 从 abstract 中移除或降级为 'anecdotal observation'；或补充 SQL 的完整信号分析和 selection 实验\"\n      assigned_to: paper_agent\n      status: open\n\n# ===== ROUND 46 SHOULD-FIX =====\n- id: R46-W1\n  summary: \"Few-NERD 正面结果（+1.39pp）未被充分利用为诊断框架预测能力的正面验证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 46\n  last_seen_round: 46\n  mentions:\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R1-W1 提出，R2 AGREE。Few-NERD 退化率最低(13%)时 LP 获得 +1.39pp，是框架 '低退化→SC 有效' 预测的最佳正面验证。但论文 framing 偏向 'SC fails'，把 Few-NERD 当作例外而非验证。\"\n  action_items:\n    - round: 46\n      action: \"在 §8 Discussion 中将 Few-NERD 重构为框架预测能力的正面验证（'框架不仅诊断失败，也预测成功'）；补充 Few-NERD 低退化原因分析\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R46-W2\n  summary: \"Entity construction +1.40pp 在全局 Holm 校正下 p_adj=0.055，abstract/Figure 1 中 framing 过于突出\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 34\n  last_seen_round: 46\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-N4 通过 prescriptive→exploratory 重定位解决\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2-W3 重提，R1 AGREE\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2 列为 Must-Fix(N2)，但 R1 REBUT 降级为 should-fix：核心贡献是诊断性的非建设性的，family-wise k=21 下 p=0.013 是 significant 的。Director 判定 should-fix——R1 论据充分（核心 claim 由 TOST 支撑，+1.40pp 是框架验证非核心 claim），但 abstract framing 确实需更谨慎。\"\n  action_items:\n    - round: 46\n      action: \"Abstract 中为 +1.40pp 加 qualifier（如 'marginally significant under global correction'）；Figure 1 标注 '+1.4pp' 为单配置/单数据集结果\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R45-W2\n  summary: \"与 Landesberg (2026) 并行发现的差异化论述不够充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 39\n  last_seen_round: 46\n  mentions:\n    - round: 42\n      reviewers: [1, 2]\n      note: \"R41-N4 通过 §2 四维度对比解决\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2-W1 重新提出。R1 AGREE。§2 末尾 concurrent work 段过于简短。\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2-W1 再次提出，R1 AGREE。§2 concurrent work 段仍仅约4行，Table 1 维度选择单方面偏向本文。需扩展至完整段落并承认 Landesberg 优势。\"\n  action_items:\n    - round: 45\n      action: \"Introduction 中增加一段明确说明与 Landesberg 的关系\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 46\n      action: \"§2 concurrent work 扩展至至少一个完整段落，明确陈述 Landesberg 在哪些方面更深入，以及本文在哪些方面互补\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R45-W4\n  summary: \"2-3 seeds 统计推断力有限，seed-level variance 估计基础不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 40\n  last_seen_round: 46\n  mentions:\n    - round: 43\n      reviewers: [1, 2]\n      note: \"R43-N1 通过 power-aware negative claims 解决\"\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1-W2。R2 AGREE。cross-seed 变异分析仅 3 个数据点。\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R1-W2 再次提出，R2 AGREE。Table 11 LP on SciERC 95% CI [-0.41, +2.34] 跨零点。2-3 seeds 的基础设计与上层统计方法的精密度之间存在不匹配。\"\n  action_items:\n    - round: 46\n      action: \"至少在一个核心配置（如 SciERC Qwen3-8B）上运行 5 seeds，验证 bootstrap CI 稳定性\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R46-W5\n  summary: \"MBR 连接（§6.1, Proposition 1）novelty 声明过高，本质是已知 MBR 理论的直接应用\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 46\n  last_seen_round: 46\n  mentions:\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 AGREE。Proposition 1 在 entity-wise independence 假设下是标准 MBR 理论的直接应用。概念上有用但不构成独立理论贡献。\"\n  action_items:\n    - round: 46\n      action: \"将 Proposition 1 定位为 'connecting existing MBR theory to NER entity construction' 而非原创理论结果；正文中说明 entity-wise independence 局限性\"\n      assigned_to: paper_agent\n      status: open\n\n- id: R46-W6\n  summary: \"Entity-level construction 在大多数配置下呈 inverse scaling，作为建设性贡献价值存疑\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 46\n  last_seen_round: 46\n  mentions:\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2-W3 提出，R1 AGREE。40/58 transitions 呈 inverse scaling，但归因分析不够深入。如果方法在大多数配置下有害，'建设性贡献'定位需更强 qualification。\"\n  action_items:\n    - round: 46\n      action: \"对 inverse scaling 给出更详细归因分析；或明确将 entity-level construction 定位为 preliminary exploration\"\n      assigned_to: paper_agent\n      status: open\n\n# ===== ROUND 46 MINOR =====\n- id: R46-M1\n  summary: \"Abstract '+1.40pp' 与正文 '+1.39pp' 四舍五入不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 46\n  last_seen_round: 46\n  mentions:\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2-M1，R1 AGREE。\"\n\n- id: R46-M2\n  summary: \"§4 第2段信息密度过高（10+统计量连续出现）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 46\n  last_seen_round: 46\n  mentions:\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2-M2，R1 AGREE。\"\n\n- id: R46-M3\n  summary: \"Figure 1 '+1.4pp' 仅适用于 Few-NERD，在 overview figure 中不加限定可能误导\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 45\n  last_seen_round: 46\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R45-M1 相关\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2-M3 和 R1 Minor 均提出。在全局校正下为边缘显著，overview figure 中不限定数据集可能误导。\"\n\n- id: R46-M4\n  summary: \"Appendix 36 页，正文对关键 appendix 分析的引导不足\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 46\n  last_seen_round: 46\n  mentions:\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2-M4，R1 AGREE。特别是 Appendix i/s/x 包含重要分析但正文指引隐蔽。\"\n\n- id: R46-M5\n  summary: \"§3.1 符号首次出现时定义不够直观，Table 5 符号表在 Appendix 较远\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 46\n  mentions:\n    - round: 43\n      reviewers: [2]\n      note: \"R43-M4\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"R2-M5，R1 AGREE。\"\n\n- id: R46-M6\n  summary: \"MDE≈1.5pp 应在 §4 或 §7 首次出现时定义，而非仅在 Limitations 中\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 46\n  last_seen_round: 46\n  mentions:\n    - round: 46\n      reviewers: [1]\n      note: \"R1 Minor。\"\n\n- id: R46-M7\n  summary: \"§3.1 'capability ceiling' 中 N≤16 缺乏选择依据说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 46\n  last_seen_round: 46\n  mentions:\n    - round: 46\n      reviewers: [1]\n      note: \"R1 Minor。Appendix n 分析了 N 到 32，应在正文解释 N=16 的选择理由。\"\n\n# ===== ROUND 45 遗留（本轮未提及） =====\n- id: R45-W3\n  summary: \"Failure mode 四种模式的层次化关系未显式形式化\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R1-N1 (critical)。R2 REBUT 降级为 should-fix。Director 判定 should-fix。\"\n    - round: 46\n      reviewers: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n\n- id: R45-W5\n  summary: \"Table 1 novelty comparison 维度选择偏向本文\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 43\n  last_seen_round: 46\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2-W2 重提。R1 AGREE。\"\n    - round: 46\n      reviewers: [1, 2]\n      note: \"合并入 R45-W2 (Landesberg 差异化)，R2-W1 再次提出 Table 1 偏向问题。\"\n\n- id: R45-W6\n  summary: \"实践指导（Appendix ah/ae）在主文可见性不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 45\n      reviewers: [1, 2]\n      note: \"R2-W4 提出缺乏实践指导。R1 REBUT——可见性问题非缺失问题。\"\n    - round: 46\n      reviewers: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n\n- id: R45-M1\n  summary: \"Figure 2 标记点小、线条细\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 46\n      reviewers: []\n      note: \"本轮未提及\"\n\n- id: R45-M2\n  summary: \"MBR 缩写在 abstract/introduction 中未展开全称\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 45\n  last_seen_round: 45\n  mentions:\n    - round: 46\n      reviewers: []\n      note: \"本轮未提及\"\n\n- id: R43-M1\n  summary: \"Footnote 1 (RE F1 confound) 建议提升到正文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 46\n      reviewers: []\n      note: \"本轮未提及\"\n\n- id: R43-M3\n  summary: \"§3 应在首段明确提及 diagnostic sequence 而非 causal chain\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 43\n  last_seen_round: 43\n  mentions:\n    - round: 46\n      reviewers: []\n      note: \"本轮未提及，可能已修复\"\n\n# ===== EARLIER ROUNDS — RESOLVED (精简保留) =====\n- id: R43-N1\n  summary: \"2-3 seeds 统计推断力不足，核心 negative claims 无法区分真无效应和检测力不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 43\n  resolution: \"全文 negative claims 改为 'yields no detectable gains'，加 MDE ~1.5pp/CI 限定。\"\n  resolution_round: 43\n\n- id: R43-N3\n  summary: \"观察性设计下因果措辞系统性过强\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 43\n  resolution: \"全文因果措辞替换为关联/观察性表述。\"\n  resolution_round: 43\n\n- id: R43-N5\n  summary: \"标题 'Why SC Fails for NER' 与正文 conditional success 结论不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 40\n  last_seen_round: 43\n  resolution: \"标题改 'When Self-Consistency Fails for NER'。\"\n  resolution_round: 43\n\n- id: R43-W1\n  summary: \"Few-NERD 3-epoch vs 5-epoch 混淆未充分解决\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 38\n  last_seen_round: 43\n  resolution: \"Greedy 0.748 vs 0.798 说明已加。\"\n  resolution_round: 43\n\n- id: R43-W3\n  summary: \"正文数字密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 37\n  last_seen_round: 43\n  resolution: \"Abstract 精简为 6 个关键数字。\"\n  resolution_round: 43\n\n- id: R43-M2\n  summary: \"Mechanistic evidence 在 Appendix 却作为正文贡献点列出\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 43\n  last_seen_round: 43\n  resolution: \"三阶段结构不再将 mechanistic evidence 列为独立贡献。\"\n  resolution_round: 43"
  }
}
```

</details>

---


### Tool result

_source line 4945 · 2026-05-25T22:47:45.169275+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 12073}, \"error\": \"\"}"}

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

_source line 4946 · 2026-05-25T22:50:15.998644+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "report": "# Round 46 审稿报告 — struct_self_consist_ie\n\n**论文**: \"When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap\"\n**目标 Venue**: EMNLP 2026 Main Conference via ARR (May 2026 cycle)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量）\n**轮次**: 1 轮（交叉分享后关键问题达成共识，无需 Round 2）\n\n---\n\n## Summary\n\n本文研究 self-consistency（SC）在 NER 任务上的效用，在 4 个 NER 数据集上用 fine-tuned 7-14B 模型定义了 5 种质量估计信号，发现这些信号虽能有效估计输出质量（AUROC 最高 0.82），但无法转化为选择增益——称为 **correlation-selection gap**。通过诊断框架识别两个共现条件：**退化**（12-68% 实例输出相同）和**信号对齐塌缩**（per-sample 信号无法区分候选）。Entity-level construction 在 Few-NERD 上获得 +1.40pp 条件性增益，但大多数配置下呈 inverse scaling。跨任务扩展（RE、SQL）确认结构化输出上的失败模式。\n\n---\n\n## Strengths\n\n1. **Correlation-selection gap 概念清晰有力**：将质量估计能力与选择增益之间的脱节命名并系统分析，为理解 structured SC 的失败提供了 reusable 的诊断框架。比简单报告 \"SC doesn't work for NER\" 有更高的分析价值。[R1, R2 共识]\n\n2. **统计方法论达到同行评审标准上限**：TOST 等效性检验支持 negative claims、paired bootstrap 估计效应量、Holm-Bonferroni 多重比较校正。Table 12 完整枚举 k=57 个统计检验的做法值得推广。Limitations 中主动披露 Holm p_adj=0.055、MDE≈1.5pp 等不利统计细节，透明度极高。[R1, R2 共识]\n\n3. **5 信号分类学设计周密**：覆盖 per-sample vs instance-level、structural vs probabilistic 的二维空间，使不同信号的失败模式可被独立分析。LP 作为唯一产生正面选择增益的信号的发现有实际指导意义。[R1]\n\n4. **实验覆盖度高**：45 页 appendix 提供极为详尽的消融分析（温度敏感性、N-scaling、cross-dataset OOD、free-form decoding、calibration、entity-level verifier transfer、few-shot 对比等）。几乎每一个合理的质疑都能在 appendix 中找到对应分析。[R1, R2 共识]\n\n5. **高可复现性**：匿名代码/数据链接、超参数详尽记录（Table 21）、信号定义明确。[R1, R2 共识; Reproducibility 4.0/5]\n\n6. **三步诊断协议（Appendix ae）具有实践价值**：测量退化 → 评估信号对齐 → 选择聚合策略，为 practitioners 提供 actionable guidance。[R1]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）— 3 项共识\n\n**N1 [critical, consensus]** 模型规模限制削弱广泛性声明\n- 标题 \"When Self-Consistency Fails for NER\" 暗示普遍诊断，但所有核心证据仅来自 Qwen3-8B 和 LLaMA-3.1-8B（7-14B fine-tuned）。论文自身数据构成内在张力：Table 44 显示 72B headroom 为 8.1pp（远高于 8B 的 1.2pp），Limitations 承认 frontier models 退化率 8.5-24%。诊断框架预测低退化→SC 有效，但未在大模型上验证。\n- **建议**：(a) 标题/摘要/引言明确限定为 \"fine-tuned 7-14B open-weight models\"；或 (b) 至少补充一个 30B+ 或 proprietary 模型验证。\n- **跨轮追踪**：该问题自 Round 43 (R43-W5) 持续存在，Round 45 升级为 Must-Fix，Round 46 仍未解决。\n\n**N2 [critical, consensus]** 退化分解上界（§6.3）理论贡献定位不当\n- 上界 $E[\\Delta F1] \\leq (1-D) \\cdot G_{nd} \\cdot \\alpha$ 本质是 partition 恒等式加 trivial 约束。Recovery ratio 仅 3-12%（Table 32），bound 比实际值宽松 8-33 倍。以 Theorem/Corollary 形式呈现让读者预期非平凡理论贡献，但实际数学深度不支持。\n- R2 补充：分解本身在诊断层面有用（三因子可独立量化），问题在于用 Theorem 格式 overclaim 数学贡献层次。\n- **建议**：重新定位为 empirical decomposition framework；移除 Theorem/Corollary 形式化框架，改用文字叙述。\n- **跨轮追踪**：Round 43 (R43-N2) 曾通过三阶段重构标记 resolved，Round 46 以更精确角度重新提出。\n\n**N3 [critical, consensus]** SQL 跨任务证据严重不足\n- Abstract \"Cross-task pilots on RE and SQL parsing **confirm** task-specific failure modes\" 中 \"confirm\" 暗示系统性验证，但 SQL 实际证据仅一个退化率统计量（87.2%, n=196）。RE 有完整 Appendix q 分析（LP selection、flip instances、free-form comparison），SQL 深度完全不匹配。R1 补充：Appendix ah SQL 引用的是外部 GPT-3.5 结果，非本文 fine-tuned 模型。\n- **建议**：(a) SQL 从 abstract 移除或降级为 \"anecdotal observation\"；或 (b) 补充完整诊断。\n\n### Should-Fix（影响评分但不一票否决）— 6 项\n\n**W1 [warning, consensus]** Few-NERD 正面结果未被充分利用为框架验证\n- Few-NERD 退化率最低（13%）时 LP 获得 +1.39pp，是框架 \"低退化→SC 有效\" 预测的最佳正面验证。论文 framing 偏向 \"SC fails\"，将 Few-NERD 当作例外而非验证。\n- **建议**：§8 Discussion 中重构为框架预测能力的正面验证；补充 Few-NERD 低退化原因分析。\n\n**W2 [warning, Director 判定]** Entity construction +1.40pp 在全局 Holm 校正下为 marginal significance\n- p_adj=0.055（global k=57），未达 α=0.05。Abstract 中作为唯一具体数字被突出。\n- R2 列为 Must-Fix，R1 REBUT：核心贡献是诊断性的非建设性的，family-wise k=21 下 p=0.013 显著，核心 negative claim 由 TOST 支撑。\n- **Director 判定**：降级为 Should-Fix。R1 论据充分——论文价值主要在诊断框架而非建设性增益。但 abstract/Figure 1 的 framing 需更谨慎。\n- **建议**：Abstract 加 qualifier（\"marginally significant under global correction\"）；Figure 1 标注为单配置/单数据集结果。\n\n**W3 [warning, consensus]** 与 Landesberg (2026) 差异化论述不足\n- §2 concurrent work 段仅约 4 行，Table 1 维度选择单方面偏向本文。\n- **建议**：扩展至完整段落，承认 Landesberg 优势并说明互补关系。\n- **跨轮追踪**：自 Round 39 持续存在。\n\n**W4 [warning, consensus]** 2-3 seeds 统计推断力有限\n- Table 11 LP on SciERC 95% CI [-0.41, +2.34] 跨零点。2-3 seeds 的基础设计与上层统计方法精密度不匹配。\n- **建议**：至少一个核心配置运行 5 seeds。\n- **跨轮追踪**：自 Round 40 持续存在。\n\n**W5 [warning, consensus]** MBR 连接 novelty 声明过高\n- Proposition 1 在 entity-wise independence 假设下是标准 MBR 理论的直接应用。概念上有用但非独立理论贡献。\n- **建议**：定位为 \"connecting existing MBR theory to NER\" 而非原创理论结果。\n\n**W6 [warning, consensus]** Entity-level construction 的 inverse scaling 未充分解释\n- 40/58 transitions 呈 inverse scaling，归因分析不够深入。如果方法在大多数配置下有害，\"建设性贡献\"定位需更强 qualification。\n- **建议**：补充归因分析或明确定位为 preliminary exploration。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键判断上达成共识：\n1. Correlation-selection gap 是有价值的诊断概念 [AGREE]\n2. 模型规模 scope 与 evidence 不匹配 [AGREE, N1]\n3. 退化分解上界应重新定位为 empirical framework [AGREE, N2]\n4. SQL 证据不足以支撑 \"confirm\" 声明 [AGREE, N3]\n5. Few-NERD 正面结果应重构为框架验证 [AGREE, W1]\n6. 2-3 seeds 统计推断力不足 [AGREE, W4]\n7. MBR Proposition 1 novelty overclaimed [AGREE, W5]\n8. Entity construction inverse scaling 需更好解释 [AGREE, W6]\n\n## Reviewer Divergence [REBUT]\n\n**分歧 1**: R2-N2（Holm p_adj=0.055 严重程度）\n- R2: Must-Fix——核心建设性 claim 未达显著性阈值\n- R1: Should-Fix——核心贡献是诊断性的，+1.40pp 不是核心 claim，family-wise 显著\n- **Director 判定**：Should-Fix。R1 论据更有说服力，论文价值在诊断框架而非建设性增益。\n\n**分歧 2**: R2-W2（§4/§7 结构分散）\n- R2: Should-Fix——读者难以区分诊断发现和方法验证\n- R1: Minor——\"建立核心发现→外部验证\"结构在 empirical NLP 中常见，加定位声明即可\n- **Director 判定**：Minor。R1 的结构分析合理，加定位声明足够。\n\n**分歧 3**: R2-W4（缺少 NER ensemble 文献）\n- R2: Should-Fix——Florian et al. (2003) 和 Diverse Beam Search 是重要遗漏\n- R1: Minor——Florian 是 supervised ensemble 而非 SC，领域不同；DBS 可加但非 gap\n- **Director 判定**：Minor。两者与 SC 的核心假设不同，用一句话提及即可。\n\n---\n\n## Questions（需要作者澄清）\n\n1. Few-NERD 退化率（13%）显著低于其他数据集，是否与 fine-grained entity type（66 types）特性有关？低退化的原因分析是否可以增强诊断框架的 prescriptive value？\n2. 72B 模型的退化率具体是多少？如果确实更低，这将直接验证论文核心机制。\n3. 如果增加 seed 数量（从 3 到 5 或 10），Holm 校正后 p_adj 是否有望降至 0.05 以下？\n4. SQL 87.2% degeneracy 是否有计划补充完整诊断框架验证？\n5. Table 32 中有多少配置的 D 低于 critical degeneracy threshold $D_{crit}$？如果大多数配置远高于阈值，bound 的 prescriptive value 有多大？\n6. 使用 full evaluation set（包含 zero-entity 实例）时，退化率和 gap 如何变化？\n7. Landesberg (2026) 是否覆盖了 NER？本文 \"NER-specific\" 角度的独特性有多强？\n\n---\n\n## Missing References\n\n1. **Florian et al. (2003)** — NER ensemble learning，虽与 SC（单模型多采样）机制不同，但作为多输出聚合的自然历史对照值得提及。[R2 提出, R1 认为 minor]\n2. **Vijayakumar et al. (2018)** — Diverse Beam Search，与降低 degeneracy 的概念联系值得一句话提及。[R2 提出, R1 部分同意]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目配置未启用外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: Agent 超时（300s 后无结果返回）。视觉审查未能完成。用户可选择重新触发 `dispatch_visual_check()`。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 (Findings)**\n**置信度: 4/5**\n\n**评分理由**：\n\n论文的核心诊断贡献——correlation-selection gap 的识别和 degeneracy + signal alignment collapse 的分解——是扎实且有用的。统计方法论严谨（TOST、bootstrap、Holm-Bonferroni），实验覆盖全面（4 数据集 × 2 模型 × 5 信号 + 45 页 appendix），透明度极高。\n\n但以下问题累积使论文未达 Main Conference 水平：\n\n1. **Scope-evidence 不匹配**（N1）：标题暗示普遍诊断，但证据仅限 7-14B fine-tuned 模型，且论文自身数据显示退化率是 model-family-dependent 的。这是自 Round 43 以来持续未解决的核心问题。\n\n2. **理论贡献定位偏差**（N2）：退化分解上界的数学 trivialness 与 Theorem 形式的 expectation 不匹配。MBR 连接也是已有理论的直接应用。论文的理论贡献声明整体偏高。\n\n3. **SQL 跨任务证据空洞**（N3）：Abstract 声称 \"confirm\"，但仅有一个数字。\n\n4. **Concurrent work 削弱新颖性**（W3）：Landesberg (2026) 独立发现了 correlation-selection gap，差异化论述不足。\n\n5. **统计 power 基础薄弱**（W4）：2-3 seeds 不足以支撑论文的统计精密度声明。\n\n**Findings 推荐理由**：诊断框架对 structured prediction + SC 的研究社区有实际参考价值，实验设计全面严谨，方法论上可以作为该方向研究的参考标准。在修复 framing 问题（限定 scope、降级 SQL、重定位 bound）后，Findings 水平的贡献是明确的。\n\n**升级至 Main Conference 所需**：(1) 至少一个大模型验证框架预测；(2) 增加 seed 数量提升统计 power；(3) Landesberg 差异化论述大幅加强。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"+1.40pp on Few-NERD\" 作为唯一具体数字被突出，但在全局 Holm 校正下仅 p_adj=0.055，需加 qualifier。\n- \"+1.40pp\" 与正文 \"+1.39pp\" 不一致（四舍五入），应统一。\n- \"Cross-task pilots on RE and SQL parsing confirm task-specific failure modes\" 中 \"confirm\" 对 SQL 而言 overclaiming，建议改为 \"suggest\" 或移除 SQL。\n- 字数需确认是否在 200 words 以内（EMNLP 2026 要求）。\n\n### §1 Introduction\n- 三阶段结构（Discover/Diagnose/Construct）清晰有效。\n- 脚注 1 匿名代码链接格式正确。\n- 但标题/引言的 framing 需限定模型 scope。\n\n### §2 Related Work\n- Table 1 novelty comparison 维度选择偏向本文，需增加本文较弱维度或在 caption 中承认局限。\n- Concurrent work（Landesberg 2026）讨论仅约 4 行，需扩展至完整段落。\n- 缺少 NER ensemble（Florian et al., 2003）和 diverse decoding（Vijayakumar et al., 2018）的简要提及。\n\n### §3 Diagnostic Framework\n- 问题形式化严谨，per-sample vs instance-level 信号的区分是重要洞察。\n- §3.1 \"capability ceiling\" 中 N≤16 缺乏选择依据。\n- 符号首次出现时定义不够直观。\n\n### §4 Single-Signal Selection Results\n- 核心发现（信号能估计质量但无法提升选择）证据充分。\n- 第 2 段信息密度过高（10+ 统计量），建议精简关键数字到正文，其余移至 table/appendix。\n\n### §5 Adaptive Methods\n- 9 种方法覆盖全面，Table 3 设计有效。\n- Cross-model self-consistency（§5.1）仅单数据集，需注明 preliminary。\n\n### §6 Threshold Regime Analysis\n- §6.1 MBR 连接概念有用，但 Proposition 1 novelty 声明应降级。\n- §6.3 退化分解上界应从 Theorem 重定位为 empirical decomposition。\n- Inverse scaling（40/58 transitions 为负）是重要发现但归因分析不足。\n\n### §7 Cross-Dataset Experiments\n- 跨数据集验证设计合理。\n- Few-NERD 正面结果（+1.39pp）应被重构为框架预测能力的正面验证。\n- Entity construction 在大多数配置下有害，§7.5 需更强 qualification。\n\n### §8 Discussion\n- 过短，应增加 Few-NERD 作为框架正面验证的讨论。\n- \"Primarily diagnostic\" 定位与 abstract 突出 +1.40pp 之间存在张力。\n\n### Limitations\n- 内容充分，主动披露不利统计细节（p_adj=0.055、MDE≈1.5pp）。\n- 符合 EMNLP 2026 要求（正文末尾、references 之前）。\n- MDE≈1.5pp 应在 §4 或 §7 首次出现。\n\n### Appendix\n- 36 页，覆盖极为详尽，但正文对关键 appendix 的引导不足。特别是 Appendix i（self-verification）、s（free-form decoding）、x（cross-dataset OOD）包含重要分析。\n\n### 格式合规\n- ✅ ACL template（`\\usepackage[review]{acl}`）\n- ✅ Double-blind（`\\author{Anonymous}`）\n- ✅ Limitations section 在正文中\n- ⚠️ 正文页数需确认是否在 8 页以内（从 TeX 结构看包含 8 个 \\input sections + limitations）"
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
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "report": "# Round 46 审稿报告 — struct_self_consist_ie\n\n**论文**: \"When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap\"\n**目标 Venue**: EMNLP 2026 Main Conference via ARR (May 2026 cycle)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量）\n**轮次**: 1 轮（交叉分享后关键问题达成共识，无需 Round 2）\n\n---\n\n## Summary\n\n本文研究 self-consistency（SC）在 NER 任务上的效用，在 4 个 NER 数据集上用 fine-tuned 7-14B 模型定义了 5 种质量估计信号，发现这些信号虽能有效估计输出质量（AUROC 最高 0.82），但无法转化为选择增益——称为 **correlation-selection gap**。通过诊断框架识别两个共现条件：**退化**（12-68% 实例输出相同）和**信号对齐塌缩**（per-sample 信号无法区分候选）。Entity-level construction 在 Few-NERD 上获得 +1.40pp 条件性增益，但大多数配置下呈 inverse scaling。跨任务扩展（RE、SQL）确认结构化输出上的失败模式。\n\n---\n\n## Strengths\n\n1. **Correlation-selection gap 概念清晰有力**：将质量估计能力与选择增益之间的脱节命名并系统分析，为理解 structured SC 的失败提供了 reusable 的诊断框架。比简单报告 \"SC doesn't work for NER\" 有更高的分析价值。[R1, R2 共识]\n\n2. **统计方法论达到同行评审标准上限**：TOST 等效性检验支持 negative claims、paired bootstrap 估计效应量、Holm-Bonferroni 多重比较校正。Table 12 完整枚举 k=57 个统计检验的做法值得推广。Limitations 中主动披露 Holm p_adj=0.055、MDE≈1.5pp 等不利统计细节，透明度极高。[R1, R2 共识]\n\n3. **5 信号分类学设计周密**：覆盖 per-sample vs instance-level、structural vs probabilistic 的二维空间，使不同信号的失败模式可被独立分析。LP 作为唯一产生正面选择增益的信号的发现有实际指导意义。[R1]\n\n4. **实验覆盖度高**：45 页 appendix 提供极为详尽的消融分析（温度敏感性、N-scaling、cross-dataset OOD、free-form decoding、calibration、entity-level verifier transfer、few-shot 对比等）。几乎每一个合理的质疑都能在 appendix 中找到对应分析。[R1, R2 共识]\n\n5. **高可复现性**：匿名代码/数据链接、超参数详尽记录（Table 21）、信号定义明确。[R1, R2 共识; Reproducibility 4.0/5]\n\n6. **三步诊断协议（Appendix ae）具有实践价值**：测量退化 → 评估信号对齐 → 选择聚合策略，为 practitioners 提供 actionable guidance。[R1]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）— 3 项共识\n\n**N1 [critical, consensus]** 模型规模限制削弱广泛性声明\n- 标题 \"When Self-Consistency Fails for NER\" 暗示普遍诊断，但所有核心证据仅来自 Qwen3-8B 和 LLaMA-3.1-8B（7-14B fine-tuned）。论文自身数据构成内在张力：Table 44 显示 72B headroom 为 8.1pp（远高于 8B 的 1.2pp），Limitations 承认 frontier models 退化率 8.5-24%。诊断框架预测低退化→SC 有效，但未在大模型上验证。\n- **建议**：(a) 标题/摘要/引言明确限定为 \"fine-tuned 7-14B open-weight models\"；或 (b) 至少补充一个 30B+ 或 proprietary 模型验证。\n- **跨轮追踪**：该问题自 Round 43 (R43-W5) 持续存在，Round 45 升级为 Must-Fix，Round 46 仍未解决。\n\n**N2 [critical, consensus]** 退化分解上界（§6.3）理论贡献定位不当\n- 上界 $E[\\Delta F1] \\leq (1-D) \\cdot G_{nd} \\cdot \\alpha$ 本质是 partition 恒等式加 trivial 约束。Recovery ratio 仅 3-12%（Table 32），bound 比实际值宽松 8-33 倍。以 Theorem/Corollary 形式呈现让读者预期非平凡理论贡献，但实际数学深度不支持。\n- R2 补充：分解本身在诊断层面有用（三因子可独立量化），问题在于用 Theorem 格式 overclaim 数学贡献层次。\n- **建议**：重新定位为 empirical decomposition framework；移除 Theorem/Corollary 形式化框架，改用文字叙述。\n- **跨轮追踪**：Round 43 (R43-N2) 曾通过三阶段重构标记 resolved，Round 46 以更精确角度重新提出。\n\n**N3 [critical, consensus]** SQL 跨任务证据严重不足\n- Abstract \"Cross-task pilots on RE and SQL parsing **confirm** task-specific failure modes\" 中 \"confirm\" 暗示系统性验证，但 SQL 实际证据仅一个退化率统计量（87.2%, n=196）。RE 有完整 Appendix q 分析（LP selection、flip instances、free-form comparison），SQL 深度完全不匹配。R1 补充：Appendix ah SQL 引用的是外部 GPT-3.5 结果，非本文 fine-tuned 模型。\n- **建议**：(a) SQL 从 abstract 移除或降级为 \"anecdotal observation\"；或 (b) 补充完整诊断。\n\n### Should-Fix（影响评分但不一票否决）— 6 项\n\n**W1 [warning, consensus]** Few-NERD 正面结果未被充分利用为框架验证\n- Few-NERD 退化率最低（13%）时 LP 获得 +1.39pp，是框架 \"低退化→SC 有效\" 预测的最佳正面验证。论文 framing 偏向 \"SC fails\"，将 Few-NERD 当作例外而非验证。\n- **建议**：§8 Discussion 中重构为框架预测能力的正面验证；补充 Few-NERD 低退化原因分析。\n\n**W2 [warning, Director 判定]** Entity construction +1.40pp 在全局 Holm 校正下为 marginal significance\n- p_adj=0.055（global k=57），未达 α=0.05。Abstract 中作为唯一具体数字被突出。\n- R2 列为 Must-Fix，R1 REBUT：核心贡献是诊断性的非建设性的，family-wise k=21 下 p=0.013 显著，核心 negative claim 由 TOST 支撑。\n- **Director 判定**：降级为 Should-Fix。R1 论据充分——论文价值主要在诊断框架而非建设性增益。但 abstract/Figure 1 的 framing 需更谨慎。\n- **建议**：Abstract 加 qualifier（\"marginally significant under global correction\"）；Figure 1 标注为单配置/单数据集结果。\n\n**W3 [warning, consensus]** 与 Landesberg (2026) 差异化论述不足\n- §2 concurrent work 段仅约 4 行，Table 1 维度选择单方面偏向本文。\n- **建议**：扩展至完整段落，承认 Landesberg 优势并说明互补关系。\n- **跨轮追踪**：自 Round 39 持续存在。\n\n**W4 [warning, consensus]** 2-3 seeds 统计推断力有限\n- Table 11 LP on SciERC 95% CI [-0.41, +2.34] 跨零点。2-3 seeds 的基础设计与上层统计方法精密度不匹配。\n- **建议**：至少一个核心配置运行 5 seeds。\n- **跨轮追踪**：自 Round 40 持续存在。\n\n**W5 [warning, consensus]** MBR 连接 novelty 声明过高\n- Proposition 1 在 entity-wise independence 假设下是标准 MBR 理论的直接应用。概念上有用但非独立理论贡献。\n- **建议**：定位为 \"connecting existing MBR theory to NER\" 而非原创理论结果。\n\n**W6 [warning, consensus]** Entity-level construction 的 inverse scaling 未充分解释\n- 40/58 transitions 呈 inverse scaling，归因分析不够深入。如果方法在大多数配置下有害，\"建设性贡献\"定位需更强 qualification。\n- **建议**：补充归因分析或明确定位为 preliminary exploration。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键判断上达成共识：\n1. Correlation-selection gap 是有价值的诊断概念 [AGREE]\n2. 模型规模 scope 与 evidence 不匹配 [AGREE, N1]\n3. 退化分解上界应重新定位为 empirical framework [AGREE, N2]\n4. SQL 证据不足以支撑 \"confirm\" 声明 [AGREE, N3]\n5. Few-NERD 正面结果应重构为框架验证 [AGREE, W1]\n6. 2-3 seeds 统计推断力不足 [AGREE, W4]\n7. MBR Proposition 1 novelty overclaimed [AGREE, W5]\n8. Entity construction inverse scaling 需更好解释 [AGREE, W6]\n\n## Reviewer Divergence [REBUT]\n\n**分歧 1**: R2-N2（Holm p_adj=0.055 严重程度）\n- R2: Must-Fix——核心建设性 claim 未达显著性阈值\n- R1: Should-Fix——核心贡献是诊断性的，+1.40pp 不是核心 claim，family-wise 显著\n- **Director 判定**：Should-Fix。R1 论据更有说服力，论文价值在诊断框架而非建设性增益。\n\n**分歧 2**: R2-W2（§4/§7 结构分散）\n- R2: Should-Fix——读者难以区分诊断发现和方法验证\n- R1: Minor——\"建立核心发现→外部验证\"结构在 empirical NLP 中常见，加定位声明即可\n- **Director 判定**：Minor。R1 的结构分析合理，加定位声明足够。\n\n**分歧 3**: R2-W4（缺少 NER ensemble 文献）\n- R2: Should-Fix——Florian et al. (2003) 和 Diverse Beam Search 是重要遗漏\n- R1: Minor——Florian 是 supervised ensemble 而非 SC，领域不同；DBS 可加但非 gap\n- **Director 判定**：Minor。两者与 SC 的核心假设不同，用一句话提及即可。\n\n---\n\n## Questions（需要作者澄清）\n\n1. Few-NERD 退化率（13%）显著低于其他数据集，是否与 fine-grained entity type（66 types）特性有关？低退化的原因分析是否可以增强诊断框架的 prescriptive value？\n2. 72B 模型的退化率具体是多少？如果确实更低，这将直接验证论文核心机制。\n3. 如果增加 seed 数量（从 3 到 5 或 10），Holm 校正后 p_adj 是否有望降至 0.05 以下？\n4. SQL 87.2% degeneracy 是否有计划补充完整诊断框架验证？\n5. Table 32 中有多少配置的 D 低于 critical degeneracy threshold $D_{crit}$？如果大多数配置远高于阈值，bound 的 prescriptive value 有多大？\n6. 使用 full evaluation set（包含 zero-entity 实例）时，退化率和 gap 如何变化？\n7. Landesberg (2026) 是否覆盖了 NER？本文 \"NER-specific\" 角度的独特性有多强？\n\n---\n\n## Missing References\n\n1. **Florian et al. (2003)** — NER ensemble learning，虽与 SC（单模型多采样）机制不同，但作为多输出聚合的自然历史对照值得提及。[R2 提出, R1 认为 minor]\n2. **Vijayakumar et al. (2018)** — Diverse Beam Search，与降低 degeneracy 的概念联系值得一句话提及。[R2 提出, R1 部分同意]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目配置未启用外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: Agent 超时（300s 后无结果返回）。视觉审查未能完成。用户可选择重新触发 `dispatch_visual_check()`。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 (Findings)**\n**置信度: 4/5**\n\n**评分理由**：\n\n论文的核心诊断贡献——correlation-selection gap 的识别和 degeneracy + signal alignment collapse 的分解——是扎实且有用的。统计方法论严谨（TOST、bootstrap、Holm-Bonferroni），实验覆盖全面（4 数据集 × 2 模型 × 5 信号 + 45 页 appendix），透明度极高。\n\n但以下问题累积使论文未达 Main Conference 水平：\n\n1. **Scope-evidence 不匹配**（N1）：标题暗示普遍诊断，但证据仅限 7-14B fine-tuned 模型，且论文自身数据显示退化率是 model-family-dependent 的。这是自 Round 43 以来持续未解决的核心问题。\n\n2. **理论贡献定位偏差**（N2）：退化分解上界的数学 trivialness 与 Theorem 形式的 expectation 不匹配。MBR 连接也是已有理论的直接应用。论文的理论贡献声明整体偏高。\n\n3. **SQL 跨任务证据空洞**（N3）：Abstract 声称 \"confirm\"，但仅有一个数字。\n\n4. **Concurrent work 削弱新颖性**（W3）：Landesberg (2026) 独立发现了 correlation-selection gap，差异化论述不足。\n\n5. **统计 power 基础薄弱**（W4）：2-3 seeds 不足以支撑论文的统计精密度声明。\n\n**Findings 推荐理由**：诊断框架对 structured prediction + SC 的研究社区有实际参考价值，实验设计全面严谨，方法论上可以作为该方向研究的参考标准。在修复 framing 问题（限定 scope、降级 SQL、重定位 bound）后，Findings 水平的贡献是明确的。\n\n**升级至 Main Conference 所需**：(1) 至少一个大模型验证框架预测；(2) 增加 seed 数量提升统计 power；(3) Landesberg 差异化论述大幅加强。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"+1.40pp on Few-NERD\" 作为唯一具体数字被突出，但在全局 Holm 校正下仅 p_adj=0.055，需加 qualifier。\n- \"+1.40pp\" 与正文 \"+1.39pp\" 不一致（四舍五入），应统一。\n- \"Cross-task pilots on RE and SQL parsing confirm task-specific failure modes\" 中 \"confirm\" 对 SQL 而言 overclaiming，建议改为 \"suggest\" 或移除 SQL。\n- 字数需确认是否在 200 words 以内（EMNLP 2026 要求）。\n\n### §1 Introduction\n- 三阶段结构（Discover/Diagnose/Construct）清晰有效。\n- 脚注 1 匿名代码链接格式正确。\n- 但标题/引言的 framing 需限定模型 scope。\n\n### §2 Related Work\n- Table 1 novelty comparison 维度选择偏向本文，需增加本文较弱维度或在 caption 中承认局限。\n- Concurrent work（Landesberg 2026）讨论仅约 4 行，需扩展至完整段落。\n- 缺少 NER ensemble（Florian et al., 2003）和 diverse decoding（Vijayakumar et al., 2018）的简要提及。\n\n### §3 Diagnostic Framework\n- 问题形式化严谨，per-sample vs instance-level 信号的区分是重要洞察。\n- §3.1 \"capability ceiling\" 中 N≤16 缺乏选择依据。\n- 符号首次出现时定义不够直观。\n\n### §4 Single-Signal Selection Results\n- 核心发现（信号能估计质量但无法提升选择）证据充分。\n- 第 2 段信息密度过高（10+ 统计量），建议精简关键数字到正文，其余移至 table/appendix。\n\n### §5 Adaptive Methods\n- 9 种方法覆盖全面，Table 3 设计有效。\n- Cross-model self-consistency（§5.1）仅单数据集，需注明 preliminary。\n\n### §6 Threshold Regime Analysis\n- §6.1 MBR 连接概念有用，但 Proposition 1 novelty 声明应降级。\n- §6.3 退化分解上界应从 Theorem 重定位为 empirical decomposition。\n- Inverse scaling（40/58 transitions 为负）是重要发现但归因分析不足。\n\n### §7 Cross-Dataset Experiments\n- 跨数据集验证设计合理。\n- Few-NERD 正面结果（+1.39pp）应被重构为框架预测能力的正面验证。\n- Entity construction 在大多数配置下有害，§7.5 需更强 qualification。\n\n### §8 Discussion\n- 过短，应增加 Few-NERD 作为框架正面验证的讨论。\n- \"Primarily diagnostic\" 定位与 abstract 突出 +1.40pp 之间存在张力。\n\n### Limitations\n- 内容充分，主动披露不利统计细节（p_adj=0.055、MDE≈1.5pp）。\n- 符合 EMNLP 2026 要求（正文末尾、references 之前）。\n- MDE≈1.5pp 应在 §4 或 §7 首次出现。\n\n### Appendix\n- 36 页，覆盖极为详尽，但正文对关键 appendix 的引导不足。特别是 Appendix i（self-verification）、s（free-form decoding）、x（cross-dataset OOD）包含重要分析。\n\n### 格式合规\n- ✅ ACL template（`\\usepackage[review]{acl}`）\n- ✅ Double-blind（`\\author{Anonymous}`）\n- ✅ Limitations section 在正文中\n- ⚠️ 正文页数需确认是否在 8 页以内（从 TeX 结构看包含 8 个 \\input sections + limitations）"
  }
}
```

</details>

---


### Tool result

_source line 4947 · 2026-05-25T22:50:20.167354+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4168
}
```

</details>

---


### Assistant

_source line 4948 · 2026-05-25T22:50:32.762941+00:00_

---

**Round 46 审稿完成。**

**审稿结果摘要**：

- **Overall: 3.0 (Findings)**
- **Reviewer 共识**: R1 和 R2 均给出 3.5（Borderline Conference），交叉分享后在 8 项关键判断上达成共识，3 项分歧由 Director 裁定
- **3 个 Must-Fix（共识）**:
  1. 模型规模 scope 与标题/摘要不匹配（自 R43 持续未解决）
  2. 退化分解上界数学 trivial，应从 Theorem 重定位为 empirical decomposition
  3. SQL 跨任务证据空洞，abstract "confirm" overclaiming
- **6 个 Should-Fix**: Few-NERD 未被利用为正面验证、p_adj=0.055 framing 过突出、Landesberg 差异化不足、2-3 seeds 统计 power 不够、MBR novelty overclaimed、inverse scaling 未解释
- **升级至 Main Conference 所需**: 大模型验证 + 增加 seeds + 加强 Landesberg 差异化

报告已投递至 Research Director。Issue Tracker 已更新（`review_issues.yaml`）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---
