# Director coordination — Part 2 of 2

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination.md) · [Structured JSON](../../../sessions/58/584d2f2da6363b58e0dc.json)

## Round 27

### User

_source line 407 · 2026-05-25T21:23:58.819107+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 方法严谨性审查

### Summary

本文对三个多语言 LLM（Llama-3.1-8B、Qwen3-8B、Gemma-2-9B-IT）的残差流进行探测，研究英中跨语言知识冲突信号的可检测性、迁移不对称性及因果干预效果。主要发现：(1) 冲突信号在两种语言中均线性可分；(2) ZH→EN 迁移优势（~7pp）与 XNLI 非冲突基线一致，反映通用跨语言结构而非冲突特异编码；(3) 仅 Llama L13 层的 steering 产生因果效应，Qwen/Gemma steering 失败，据此提出"detection ≠ decision"论断。

---

### Strengths

**S1. 三模型设计提供跨架构证据。** 使用三个参数量相当但架构不同的模型（Llama/Qwen/Gemma），且模型间问题重叠仅 3.5%，构成近似独立复制。方向一致性的二项检验（p = 0.016）是合理的统计策略。

**S2. XNLI 非冲突基线控制得当。** 用相同 pipeline 在 XNLI 上运行探测，证明不对称性并非冲突特异，是本文最有说服力的控制实验之一。

**S3. EN-DE 类型学控制巧妙。** 德语词汇重叠率约为中文的 4 倍（14.8% vs 3.8%），但 EN↔DE 不对称性接近零（Δ = +1.2pp, n.s.），有效排除了 token overlap 混淆。

**S4. Selectivity control 规范。** 置换标签控制（N=131–201）产生近机会准确率（49.2–51.0%），selectivity gap 达 21–40pp，证实探测信号非任意线性可分。

**S5. Steering 随机控制设计合理。** 注入等幅随机向量 r ~ N(0,I) 作为对照，将方向效应与幅度效应分离，方法上较先前工作有改进。

**S6. Limitations 诚实。** 明确承认单 split 局限性并承诺 camera-ready 补充 5-fold CV，以及 steering 仅在 Llama 成功。

---

### Weaknesses

**W1 [critical] "Detection ≠ Decision" 核心论断证据不足，存在过度概括。**
- 具体位置：Abstract ("these findings indicate that linear detectability does not imply causal relevance")、Section 5 Discussion、Section 6 Conclusion
- 问题：正面因果证据仅来自**一个模型（Llama）的一个层（L13）**。Qwen 和 Gemma 的负面结果可被多种替代假设解释：(a) 非线性因果通路（论文自己承认）；(b) 因果窗口在不同层（Llama 中因果窗口仅 ~4 层宽/L13-L16，但 Qwen 仅测 L14、Gemma 仅测 L17，遗漏相邻层的可能性大）；(c) 样本量不足（Qwen n=131、Gemma n=171，对微弱效应的检验功效有限）；(d) 线性 steering 本身的方法局限。Absence of evidence ≠ evidence of absence——论文将两个模型的 null result 提升为跨模型的一般性结论，逻辑跳跃过大。
- 为什么影响接收：这是论文的第三个贡献点（Contribution 3），也是 abstract 和 conclusion 的核心 takeaway。如果此论断不成立，论文的新颖贡献大幅缩水，仅剩描述性发现（跨语言可检测性 + 不对称性）。
- 建议修改方向：(1) 将 claim 降级为 Llama 特有观察，明确声明无法推广到其他架构；(2) 对 Qwen/Gemma 在至少 3-5 个相邻层进行 steering（而非仅 1 层），以确认负面结果的鲁棒性；(3) 补充 activation patching 实验作为线性 steering 的对照。

**W2 [critical] Qwen 不对称性 CI 包含零，但被当作支持证据处理。**
- 具体位置：Section 4.3, Table 1 — Qwen Δ_asym = +7.2, CI [−0.6, 13.7]
- 问题：Qwen 的 95% CI 跨越零，意味着该模型的不对称性在 α=0.05 水平不显著。但论文在 Section 4.3 中写 "the asymmetry is consistent in direction across all three architectures" 并将 Qwen 与 Llama/Gemma 同等对待。进一步，如果对三个模型的不对称性检验做 Bonferroni 校正（阈值 0.017），Llama (p=0.038) 也不再显著，仅 Gemma (p=0.006) 幸存。
- 为什么影响接收：不对称性的跨模型一致性是 Contribution 2 的基础。三个模型中两个不显著（校正后），严重削弱"一致"的论断。
- 建议修改方向：(1) 明确报告 Qwen 不显著，不要用模糊的 "marginally includes zero"；(2) 讨论对三模型做多重比较校正后的结果；(3) 更多依赖方向一致性的二项检验（p=0.016）和 XNLI 的独立复制，而非个体模型的点估计。

**W3 [critical] COMET tercile 分析严重欠功效，无法有效排除翻译质量混淆。**
- 具体位置：Section 4.5, Table 2
- 问题：论文自己报告 MDE = 25.3pp at 80% power（n≈56 per tercile）——即只有翻译质量造成 >25pp 的准确率差异时才能检测到。这使得该分析对中等大小的混淆效应完全不敏感。更令人担忧的是，Gemma 显示 Δ = +10.3pp 在混淆方向（高 COMET → 高准确率），虽然 p=0.278，但在这种低功效下不显著并不等于无效应。论文将此结果描述为 "non-significant trend"（Section 4.5），但一个 10pp 的点估计在混淆方向上是实质性的。
- 为什么影响接收：如果翻译质量确实影响跨语言探测准确率，则 ZH→EN 不对称性可能是 artifact。COMET tercile 分析本应排除此混淆，但因欠功效而无法完成此任务。
- 建议修改方向：(1) 增加样本量或使用连续回归（COMET score 作为连续变量 vs. 探测准确率），而非三分位比较，以提升功效；(2) 对 Gemma 的 +10.3pp 趋势做更深入调查；(3) 如果无法增加功效，诚实声明翻译质量混淆未被排除。

**W4 [warning] TOST 等价性检验功效仅 1.4%，无信息量。**
- 具体位置：Section 4.4 — "TOST equivalence tests (±2 pp margin) are non-significant (p > 0.36, power = 1.4%)"
- 问题：1.4% 的功效意味着即使冲突不对称性与 XNLI 不对称性完全相同，该检验也几乎不可能检测到等价性。±2pp 的等价边界过于严格（考虑到各个 CI 宽度 >10pp）。报告一个注定失败的检验并用 "reflecting insufficient power" 一笔带过，有空洞分析之嫌。
- 建议：要么选择合理的等价边界（如 ±5pp）并报告所需样本量，要么删除 TOST 分析，改用 CI 重叠的定性论证。

**W5 [warning] 单 train/test split 贯穿全文，bootstrap CI 仅捕获 split 内变异性。**
- 具体位置：Section 4.1, Limitations
- 问题：所有探测结果基于单一 80/20 split。Bootstrap resampling（n=2,000）估计的 CI 是条件于该 split 的——它不能告诉我们换一个 split 结果会怎样。论文在 Limitations 中承认 seed 复制显示 peak layer 可能偏移（Qwen ±1.90%），但未在主要结果中使用 k-fold CV。论文承诺 camera-ready 补充 5-fold CV，但当前版本缺乏此验证。
- 建议：至少报告 3-fold CV 的主要结果（Table 1），或在当前版本就完成 5-fold CV。

**W6 [warning] 翻译模型（Qwen3-8B）同时作为实验对象。**
- 具体位置：Section 3.2, Section 4.1
- 问题：Qwen3-8B 既是翻译 pipeline 又是三个被探测模型之一。虽然论文指出 Llama/Gemma（与翻译模型架构独立）也显示相同模式以缓解担忧，但 Qwen 特有的翻译偏差可能使 Qwen 的跨语言迁移结果不可靠。
- 建议：在正文中更显著地标注此利益冲突，或使用独立翻译模型（如 NLLB）作为额外验证。

**W7 [warning] 全文多重假设检验缺乏整体 FWER 控制。**
- 具体位置：全文
- 问题：粗略统计，全文约 100+ 假设检验：12 个探测二项检验、6 个不对称性检验、3 个 TOST、5 个混淆检验、~78 个 steering 检验等。Bonferroni 仅应用于 steering 实验（per-layer k=10 或 30-test 校正），但探测二项检验、不对称性检验、混淆检验均未做多重比较校正。虽然不同分析模块可视为独立研究问题，但 Section 4.3 的三个不对称性检验属于同一族。
- 建议：至少对同族检验（如三模型不对称性）应用 Bonferroni/Holm 校正并报告校正后结果。

**W8 [warning] Steering 仅在英文 test data 上评估，未测试跨语言因果干预。**
- 具体位置：Section 3.6 — "Steering evaluation uses only the conflict-condition subset of the English test data"
- 问题：一篇关于跨语言冲突机制的论文，其因果干预实验仅在英文输入上进行。ZH→EN 探测不对称性是核心发现，但从未测试在中文输入上进行 steering 是否产生不同的因果模式。
- 建议：至少在 Llama L13（已知有效的层）上测试中文输入的 steering 效果。

**W9 [info] Fisher's exact test 用于 paired data 可能不当。**
- 具体位置：Section 3.6, Section 4.6
- 问题：Steering 实验中，相同测试样本分别接受 probe-direction 和 random-direction 注入。这是配对数据，但 Fisher's exact test 假设独立样本。McNemar's test 更适合配对二分类数据。在正相关情况下（容易翻转的样本在两种条件下都容易翻转），Fisher's test 可能是保守的，但这应予以说明。
- 建议：补充 McNemar's test 结果，或论证 Fisher's exact test 的保守性。

---

### Questions to Authors

**Q1.** Llama 中因果窗口仅 ~4 层宽（L13-L16）。对 Qwen 和 Gemma，你们仅测试了 1 个层（L14/L17）。如果因果窗口同样窄，遗漏相邻层完全可能。是否有 Appendix F 以外的多层 steering 结果？Appendix F 的 Table 6 是否覆盖了每个模型至少 3 个相邻层？

**Q2.** Table 1 中 Δ_asym 脚注指出 "Δ_asym is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies"。以 Llama 为例：ZH→EN (70.6) − EN→ZH (59.6) = 11.0pp，但 bootstrap Δ_asym = +7.3pp。这 3.7pp 差异的来源是什么？这是否意味着 peak layer 在不同 bootstrap 样本中发生偏移？如果是，这本身就说明单 split 结果不稳定。

**Q3.** Gemma COMET tercile Δ = +10.3pp 在混淆方向。你们将此归因于 "near-chance baseline accuracy of the EN→ZH probe at L17 (58.8%)"，但 58.8% 仍显著高于 chance（binomial p < 0.05 for n≈56）。能否提供 Gemma COMET score 与探测准确率的散点图或连续回归结果？

**Q4.** Qwen3-8B 同时作为翻译模型和实验对象。你们是否验证过：在 Qwen 上，用外部翻译模型（如 NLLB）的翻译是否产生相似的跨语言迁移模式？

**Q5.** Section 4.6 报告 L13 steering 的 all-position injection 与 last-token injection 产生 "identical results"。能否提供具体数字？"Identical" 是指 p-value 和 flip rate 完全相同，还是方向一致但幅度不同？

---

### Missing References

无明显遗漏。论文引用了该领域的主要相关工作（Zhao et al. 2024/2026, Basu et al. 2026, Hewitt & Liang 2019, Belinkov 2022, Marks & Tegmark 2024 等）。

---

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 2.5/5 | 核心因果论断证据不足（W1），不对称性统计证据不一致（W2），混淆排除欠功效（W3）。描述性发现（可检测性、XNLI 基线）较为扎实。 |
| **Excitement** | 3/5 | 跨语言冲突机制解释是有意义的研究方向，"detection ≠ decision" 观察如能充分支撑会很有启发，但当前证据使其更像初步观察而非成熟结论。 |
| **Reproducibility** | 3.5/5 | 超参（C=1.0）、硬件（RTX PRO 6000）、bootstrap n=2000 均有报告；匿名 repo 已提供。不足：主实验随机种子未明确报告；单 split 无 CV。 |

---

### Overall Assessment

**Overall: 3.0 — Findings**

本文在跨语言冲突信号可检测性和迁移不对称性方面提供了有价值的描述性发现，XNLI 基线和 EN-DE 控制设计得当。但论文的核心机制性贡献（"detection ≠ decision"）基于一个模型一个层的正面证据和两个模型的方法学上可疑的负面证据，无法支撑 abstract 和 conclusion 中的概括性论断。不对称性的统计证据在三模型中不一致（Qwen CI 包含零，Bonferroni 校正后仅 Gemma 显著），混淆排除分析欠功效（COMET tercile MDE = 25.3pp）。这些方法论问题叠加后，使论文的 soundness 低于主会议标准。修改后适合 Findings。

### Confidence

**Confidence: 4/5** — 统计方法论和 probing/steering 实验设计是我的专长领域，仔细阅读了全文及附录。对论文所涉的具体模型架构细节稍不确定。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-25T21:24:48.063079+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Weaknesses 和关键论点：对每条用 [AGREE] 表示同意（简述理由），或 [REBUT] 表示反驳（引用具体 Section/Table/Figure 提供证据）。\n\n---\n\n# Reviewer 2 审稿意见：新颖性与完整性\n\n## Summary\n\n本文将知识冲突信号的 probing 分析从单语（Zhao et al. 2024）扩展到跨语言（英-中）设置，使用三个 LLM（Llama-3.1-8B-Instruct��Qwen2.5-8B、Gemma-2-9B-IT）进行残差流探测、XNLI 非冲突基线对照、COMET 混淆因素排除和因果 steering 实验。主要发现：(1) 冲突信号在所有模型和方向上线性可检测；(2) ZH→EN 迁移优势约 7pp，与 XNLI 基线一致，反映一般跨语言结构而非冲突特异性；(3) 因果 steering 仅在 Llama L13（41% 深度）成功，Qwen/Gemma 无显著因果效应，表明检测不蕴含因果相关性。\n\n## Strengths\n\n**S1. 混淆因素控制设计出色。** COMET 翻译质量分层 + XNLI 非冲突基线的组合是一个真正的方法论贡献（Section 3.5, 4.4-4.5）。用 XNLI 作为非冲突对照来区分冲突特异性 vs. 一般跨语言不对称性，思路清晰且可复用。\n\n**S2. 多模型验证增强泛化性。** 三个架构差异显著的模型（Llama/Qwen/Gemma）在检测能力上一致，强化了\"冲突信号线性可检测\"这一结论的可信度（Table 1, Figure 3）。\n\n**S3. 统计方法规范。** Bootstrap CI（n=2000）、Bonferroni 校正（l=10 to α values）、Fisher 精确检验、matched-condition 控制，统计实践达到 top-venue 标准。\n\n**S4. 诚实报告负面结果。** Qwen/Gemma steering 失败（Table 3）、asymmetry 非冲突特异性（Section 4.4）——这些负面结果的如实报告值得肯定，优于很多只报积极结果的论文。\n\n**S5. Seed replication 加强因果 claim。** Appendix C 用独立 seed 复现了 Llama L13 steering 效果（N=201, 独立 train/test split），排除了单次 split 偶然性的可能。\n\n## Weaknesses\n\n### Must-Fix 问题\n\n**N1 [critical] \"Detection ≠ Decision\" 核心 claim 支撑不足，且与 Basu et al. (2026) 差异化不清晰。**\n- Basu et al. (2026) 已在单语设置中建立了 detection-steering 的 dissociation。本文跨语言扩展未清晰阐述相比单语设置的增量发现。\n- Steering 仅在 Llama L13 产生显著因果效应，2/3 模型不支持任何因果影响。\n- 相邻 L16 已无效（p>0.12），因果窗口极窄，可能是 fragile artifact。\n- 将\"steering 在 2/3 模型失败\"框架为支持 dissociation，但也可能是 steering 方法太粗糙。\n\n**N2 [critical] \"General Cross-Lingual Asymmetries\" 泛化声称仅基于单一语言对。**\n- 标题声称 \"General Cross-Lingual Asymmetries\"，但实验仅覆盖英-中一个语言对。EN-DE 仅用于混淆因素检查，未作完整探测实验。\n\n**N3 [critical] Contribution 2（asymmetry = general structure）本质是 null result 被包装为正面贡献。**\n- 发现不对称性与 XNLI 基线一致 = 不是冲突特异的 = null result。将其列为独立贡献膨胀了贡献计数。\n\n### Should-Fix 问题\n\n**W1 [warning] 四个贡献的权重严重不均衡。**\n**W2 [warning] 单一 train/test split，缺乏交叉验证。**\n**W3 [warning] Steering 分析样本量小、多重比较负担重。**\n**W4 [warning] 机制深度偏浅——定位偏 empirical probing，非 mechanistic interpretability。**\n**W5 [warning] Related Work 缺少跨语言知识编辑文献。**\n**W6 [info] 缺少独立 Conclusion 章节。**\n\n## Missing References\n\n1. \"Editing Across Languages: A Survey of Multilingual Knowledge Editing\" (2025)\n2. CLM-Bench (2026)\n3. BMIKE-53\n\n## Overall Assessment: 3.0/5 (Findings)\n\n---\n\n请逐条回应上述 Weaknesses（N1-N3, W1-W6）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Weaknesses 和关键论点：对每条用 [AGREE] 表示同意（简述理由），或 [REBUT] 表示反驳（引用具体 Section/Table/Figure 提供证据）。\n\n---\n\n# Reviewer 2 审稿意见：新颖性与完整性\n\n## Summary\n\n本文将知识冲突信号的 probing 分析从单语（Zhao et al. 2024）扩展到跨语言（英-中）设置，使用三个 LLM（Llama-3.1-8B-Instruct��Qwen2.5-8B、Gemma-2-9B-IT）进行残差流探测、XNLI 非冲突基线对照、COMET 混淆因素排除和因果 steering 实验。主要发现：(1) 冲突信号在所有模型和方向上线性可检测；(2) ZH→EN 迁移优势约 7pp，与 XNLI 基线一致，反映一般跨语言结构而非冲突特异性；(3) 因果 steering 仅在 Llama L13（41% 深度）成功，Qwen/Gemma 无显著因果效应，表明检测不蕴含因果相关性。\n\n## Strengths\n\n**S1. 混淆因素控制设计出色。** COMET 翻译质量分层 + XNLI 非冲突基线的组合是一个真正的方法论贡献（Section 3.5, 4.4-4.5）。用 XNLI 作为非冲突对照来区分冲突特异性 vs. 一般跨语言不对称性，思路清晰且可复用。\n\n**S2. 多模型验证增强泛化性。** 三个架构差异显著的模型（Llama/Qwen/Gemma）在检测能力上一致，强化了\"冲突信号线性可检测\"这一结论的可信度（Table 1, Figure 3）。\n\n**S3. 统计方法规范。** Bootstrap CI（n=2000）、Bonferroni 校正（l=10 to α values）、Fisher 精确检验、matched-condition 控制，统计实践达到 top-venue 标准。\n\n**S4. 诚实报告负面结果。** Qwen/Gemma steering 失败（Table 3）、asymmetry 非冲突特异性（Section 4.4）——这些负面结果的如实报告值得肯定，优于很多只报积极结果的论文。\n\n**S5. Seed replication 加强因果 claim。** Appendix C 用独立 seed 复现了 Llama L13 steering 效果（N=201, 独立 train/test split），排除了单次 split 偶然性的可能。\n\n## Weaknesses\n\n### Must-Fix 问题\n\n**N1 [critical] \"Detection ≠ Decision\" 核心 claim 支撑不足，且与 Basu et al. (2026) 差异化不清晰。**\n- Basu et al. (2026) 已在单语设置中建立了 detection-steering 的 dissociation。本文跨语言扩展未清晰阐述相比单语设置的增量发现。\n- Steering 仅在 Llama L13 产生显著因果效应，2/3 模型不支持任何因果影响。\n- 相邻 L16 已无效（p>0.12），因果窗口极窄，可能是 fragile artifact。\n- 将\"steering 在 2/3 模型失败\"框架为支持 dissociation，但也可能是 steering 方法太粗糙。\n\n**N2 [critical] \"General Cross-Lingual Asymmetries\" 泛化声称仅基于单一语言对。**\n- 标题声称 \"General Cross-Lingual Asymmetries\"，但实验仅覆盖英-中一个语言对。EN-DE 仅用于混淆因素检查，未作完整探测实验。\n\n**N3 [critical] Contribution 2（asymmetry = general structure）本质是 null result 被包装为正面贡献。**\n- 发现不对称性与 XNLI 基线一致 = 不是冲突特异的 = null result。将其列为独立贡献膨胀了贡献计数。\n\n### Should-Fix 问题\n\n**W1 [warning] 四个贡献的权重严重不均衡。**\n**W2 [warning] 单一 train/test split，缺乏交叉验证。**\n**W3 [warning] Steering 分析样本量小、多重比较负担重。**\n**W4 [warning] 机制深度偏浅——定位偏 empirical probing，非 mechanistic interpretability。**\n**W5 [warning] Related Work 缺少跨语言知识编辑文献。**\n**W6 [info] 缺少独立 Conclusion 章节。**\n\n## Missing References\n\n1. \"Editing Across Languages: A Survey of Multilingual Knowledge Editing\" (2025)\n2. CLM-Bench (2026)\n3. BMIKE-53\n\n## Overall Assessment: 3.0/5 (Findings)\n\n---\n\n请逐条回应上述 Weaknesses（N1-N3, W1-W6）。"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-25T21:25:10.664482+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22601
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-25T21:25:10.865670+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完��审稿意见。请逐条回应其 Weaknesses 和关键论点：对每条用 [AGREE] 表示��意（简述理由），或 [REBUT] 表示反驳��引用具体 Section/Table/Figure 提供证据）���\n\n---\n\n# Reviewer 1 — 方法严谨性审查\n\n## Summary\n\n本文对三个多语言 LLM（Llama-3.1-8B、Qwen3-8B、Gemma-2-9B-IT）的残差流进行探测，研究英中跨语言知识冲突信号的可检测性、迁移不对称性及因果干预效果。主要发现：(1) 冲突信号在两种语言中均线性可分；(2) ZH→EN 迁移优势（~7pp）与 XNLI 基线一致，反映通用跨语言结构而非冲突特异编码；(3) 仅 Llama L13 层的 steering 产生因果效应，Qwen/Gemma steering 失败，据此提出\"detection ≠ decision\"论断。\n\n## Strengths\n\n**S1.** 三模型设计提供跨架构证据（3.5% 问题重叠，近独立复制）。\n**S2.** XNLI 非冲突基线控制得当。\n**S3.** EN-DE 类型学控制巧妙（14.8% vs 3.8% Jaccard，Δ = +1.2pp n.s.）。\n**S4.** Selectivity control 规范（selectivity gap 21–40pp）。\n**S5.** Steering 随机控制设计合理（等幅 r ~ N(0,I) 对照）。\n**S6.** Limitations 诚实。\n\n## Weaknesses\n\n**W1 [critical] \"Detection ≠ Decision\" 核心论断证据不足，存在过度概括。**\n- 正面因果证据仅来自一个模型的一个层。Qwen/Gemma 负面结果有多种替代解释：非线性通路、因果窗口在不同层（Qwen 仅测 L14、Gemma 仅测 L17）、样本量不足（n=131/171）、线性 steering 方法局限。\n- Absence of evidence ≠ evidence of absence。\n\n**W2 [critical] Qwen 不对称性 CI 包含零，但被当作支持证据。**\n- Qwen Δ_asym = +7.2, CI [−0.6, 13.7]，95% CI 跨越零。\n- Bonferroni 校正后（阈值 0.017），Llama (p=0.038) 也不再显著，仅 Gemma (p=0.006) 幸存。\n- 三模型中两个不显著（校正后），严重削弱\"一致\"论断。\n\n**W3 [critical] COMET tercile 分析严重欠功效（MDE=25.3pp），无法排除翻译质量混淆。**\n- Gemma Δ = +10.3pp 在混淆方向，低功效下 p=0.278 不能排除实质效应。\n- 翻译质量混淆未被有效排除。\n\n**W4 [warning] TOST 等价检验功效仅 1.4%，无信息量。**\n- ±2pp 边界过严，检验注定失败。\n\n**W5 [warning] 单 train/test split，bootstrap CI 仅捕获 split 内变异性。**\n\n**W6 [warning] 翻译模型 Qwen3-8B 同时作为实验对象。**\n\n**W7 [warning] 全文多重假设检验缺乏整体 FWER 控制。**\n- 全文 ~100+ 假设检验，仅 steering 做了 per-layer Bonferroni。三模型不对称性检验属同一族但未校正。\n\n**W8 [warning] Steering 仅在英文数据上评估，未测试跨语言因果干预。**\n\n**W9 [info] Fisher's exact test 用于 paired data 可能不当（应用 McNemar's test）。**\n\n## Overall Assessment: 3.0 (Findings)\n## Confidence: 4/5\n\n---\n\n请逐条回应上述 Weaknesses（W1-W9）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完��审稿意见。请逐条回应其 Weaknesses 和关键论点：对每条用 [AGREE] 表示��意（简述理由），或 [REBUT] 表示反驳��引用具体 Section/Table/Figure 提供证据）���\n\n---\n\n# Reviewer 1 — 方法严谨性审查\n\n## Summary\n\n本文对三个多语言 LLM（Llama-3.1-8B、Qwen3-8B、Gemma-2-9B-IT）的残差流进行探测，研究英中跨语言知识冲突信号的可检测性、迁移不对称性及因果干预效果。主要发现：(1) 冲突信号在两种语言中均线性可分；(2) ZH→EN 迁移优势（~7pp）与 XNLI 基线一致，反映通用跨语言结构而非冲突特异编码；(3) 仅 Llama L13 层的 steering 产生因果效应，Qwen/Gemma steering 失败，据此提出\"detection ≠ decision\"论断。\n\n## Strengths\n\n**S1.** 三模型设计提供跨架构证据（3.5% 问题重叠，近独立复制）。\n**S2.** XNLI 非冲突基线控制得当。\n**S3.** EN-DE 类型学控制巧妙（14.8% vs 3.8% Jaccard，Δ = +1.2pp n.s.）。\n**S4.** Selectivity control 规范（selectivity gap 21–40pp）。\n**S5.** Steering 随机控制设计合理（等幅 r ~ N(0,I) 对照）。\n**S6.** Limitations 诚实。\n\n## Weaknesses\n\n**W1 [critical] \"Detection ≠ Decision\" 核心论断证据不足，存在过度概括。**\n- 正面因果证据仅来自一个模型的一个层。Qwen/Gemma 负面结果有多种替代解释：非线性通路、因果窗口在不同层（Qwen 仅测 L14、Gemma 仅测 L17）、样本量不足（n=131/171）、线性 steering 方法局限。\n- Absence of evidence ≠ evidence of absence。\n\n**W2 [critical] Qwen 不对称性 CI 包含零，但被当作支持证据。**\n- Qwen Δ_asym = +7.2, CI [−0.6, 13.7]，95% CI 跨越零。\n- Bonferroni 校正后（阈值 0.017），Llama (p=0.038) 也不再显著，仅 Gemma (p=0.006) 幸存。\n- 三模型中两个不显著（校正后），严重削弱\"一致\"论断。\n\n**W3 [critical] COMET tercile 分析严重欠功效（MDE=25.3pp），无法排除翻译质量混淆。**\n- Gemma Δ = +10.3pp 在混淆方向，低功效下 p=0.278 不能排除实质效应。\n- 翻译质量混淆未被有效排除。\n\n**W4 [warning] TOST 等价检验功效仅 1.4%，无信息量。**\n- ±2pp 边界过严，检验注定失败。\n\n**W5 [warning] 单 train/test split，bootstrap CI 仅捕获 split 内变异性。**\n\n**W6 [warning] 翻译模型 Qwen3-8B 同时作为实验对象。**\n\n**W7 [warning] 全文多重假设检验缺乏整体 FWER 控制。**\n- 全文 ~100+ 假设检验，仅 steering 做了 per-layer Bonferroni。三模型不对称性检验属同一族但未校正。\n\n**W8 [warning] Steering 仅在英文数据上评估，未测试跨语言因果干预。**\n\n**W9 [info] Fisher's exact test 用于 paired data 可能不当（应用 McNemar's test）。**\n\n## Overall Assessment: 3.0 (Findings)\n## Confidence: 4/5\n\n---\n\n请逐条回应上述 Weaknesses（W1-W9）。"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-25T21:25:12.272793+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1407
}
```

</details>

---


### Assistant

_source line 412 · 2026-05-25T21:25:16.233259+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 28

## Round 28

2 recorded events


### User

_source line 413 · 2026-05-25T21:25:18.806186+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3.0（Findings）**。

主要问题集中在三点：
1. **"Detection ≠ Decision" 论断过度概括**——正面因果证据仅来自 Llama L13 一层，Qwen/Gemma 各仅测 1 层的 null result 不足以支撑跨架构的一般性结论
2. **不对称性统计不一致**——Qwen CI 包含零，Bonferroni 校正后仅 Gemma 显著，三模型"一致"的论断被削弱
3. **COMET tercile 混淆排除严重欠功效**（MDE = 25.3pp），无法有效排除翻译质量混淆，Gemma 还显示 +10.3pp 的混淆方向趋势

论文的描述性发现（跨语言可检测性、XNLI 基线控制、EN-DE 类型学控制）设计得当，修改后适合 Findings 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 414 · 2026-05-25T21:25:24.331237+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 29

## Round 29

2 recorded events


### User

_source line 415 · 2026-05-25T21:27:14.211784+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应：Reviewer 1 Weaknesses 逐条评议

---

## [AGREE] R1-W1: "Detection ≠ Decision" 核心论断证据不足

完全同意。这与我 N1 的判断一致。补充两点：

(1) R1 指出 "absence of evidence ≠ evidence of absence" 非常精准。论文将 Qwen/Gemma steering 失败解读为支持 dissociation 叙事，但 R1 正确列举了替代解释（非线性通路、不同因果窗口、样本量不足、线性 steering 局限）。从论文 Table 3 来看，Qwen 仅报告了 L14、Gemma 仅报告了 L17 层的 steering 结果，并未系统搜索所有层的因果窗口——这与 Llama 的 L13 精确定位是不对等的实验设计。

(2) 我在 N1 中额外指出了 Basu et al. (2026) "Interpretability without actionability" 已在单语设置中建立了 detection-steering dissociation，进一步削弱了本文在该 claim 上的新颖性。R1 未提及这一文献重叠，但两个问题叠加后，该 claim 的支撑更加薄弱。

---

## [AGREE] R1-W2: Qwen 不对称性 CI 包含零

同意，且认为这是我审稿中的一个遗漏。R1 的分析很有说服力：

- Qwen Δ_asym = +7.2, CI [−0.6, 13.7] 确实跨越零
- Bonferroni 校正阈值 0.05/3 = 0.017 下，Llama (p=0.038) 也不显著，仅 Gemma (p=0.006) 幸存
- 论文 Section 4.3 称"all three models show a consistent directional trend"——但从统计严格性看，校正后仅 1/3 模型显著支持该 "consistent" 断言

这直接影响 Contribution 2（asymmetry reflects general structure）的可信度。如果不对称性本身在多数模型中不显著，那么将其与 XNLI 基线匹配并声称反映"一般跨语言结构"就更加站不住。这强化了我 N3 的判断（该 contribution 本质是 null result）。

---

## [AGREE（部分）] R1-W3: COMET tercile 分析功效不足

同意核心论点，但认为需要在论文的多层控制框架中评估。

R1 的功效分析（MDE=25.3pp）是正确的——COMET tercile 分析单独来看确实无法排除翻译质量混淆。Gemma Δ=+10.3pp（Section 4.5, Table 2）在混淆方向，低功效下 p=0.278 完全可能是 type II error。

但我要指出，论文的混淆排除不只依赖 tercile 分析——它是一个多层设计：
1. COMET tercile stratification（R1 正确指出功效不足）
2. XNLI 非冲突基线（Section 4.4）——这是独立于翻译质量的控制
3. Token overlap / Jaccard 分析（Section 4.4）——EN-DE 控制 Jaccard 仅 3.8%
4. EN-DE 类型学控制（R1 自己在 S3 肯定了这一点：14.8% vs 3.8% Jaccard, Δ=+1.2pp n.s.）

因此，COMET tercile 分析是最薄弱的一环，R1 的批评有效。但翻译质量混淆并非完全未被控制——XNLI 基线和 EN-DE 控制提供了部分独立证据。建议作者增大 tercile 分析的样本量或使用连续回归替代分层分析。

---

## [AGREE] R1-W4: TOST 等价检验功效仅 1.4%

同意。±2pp 等价边界对于 balanced accuracy 来说过窄。在 n~200 的样本量和约 5-8pp 的 bootstrap SE 下，这个检验注定失败。论文应要么使用更合理的等价边界（如 ±5pp），要么删除这个 uninformative 的检验结果，避免给读者造成"已验证等价性"的错误印象。

---

## [AGREE] R1-W5: 单 train/test split

完全同意，与我 W2 一致。Bootstrap CI 仅捕获 within-split sampling variability，不捕获 split selection variability。作者承诺 camera-ready 提供 5-fold CV，但当前版本的所有 probe accuracy 数字都有 split 敏感性风险。

---

## [REBUT] R1-W6: 翻译模型 Qwen3-8B 同时作为实验对象

不完全同意。需要区分：

- 翻译模型：**Qwen3-8B**（Section 3.2）
- 实验探测对象：**Qwen2.5-8B**（Section 4.1）

这是不同代际的模型（Qwen3 vs Qwen2.5），虽属同一模型家族，但架构和训练数据存在代际差异。R1 的担忧（同家族共享 tokenizer/分布偏好可能造成 Qwen2.5 probing 结果的系统性偏差）有一定道理，但：

1. 翻译质量由 COMET（独立于 Qwen 的指标）验证，Section 3.2 明确提到 back-translation 质量校验
2. 如果 Qwen 家族共享的偏好造成了系统性偏差，我们应该观察到 Qwen2.5 的 probing 结果系统性高于 Llama/Gemma——但 Table 1 显示 Qwen 的 probe accuracy 在三模型中并非系统性最高（EN→EN: Llama 77.6%, Qwen 75.0%, Gemma 88.9%）
3. Qwen2.5 的 asymmetry CI 包含零（R1-W2），恰恰不支持 Qwen 家族偏好造成系统性优势的假说

该担忧值得在 Limitations 中提及，但不构成对结论的实质性威胁。

---

## [AGREE（部分）] R1-W7: 多重假设检验缺乏整体 FWER 控制

部分同意。R1 指出全文 ~100+ 假设检验缺乏统一 FWER 控制是正确的。特别是：

- 三模型不对称性检验属同一 hypothesis family，应做校正（如 R1-W2 所示，校正后仅 Gemma 显著）
- Probing accuracy 的 binomial tests（4 方向 × 3 模型 = 12 tests）也属同一族

但我认为要求全文所有检验做统一 FWER 控制过于严格——这在当前 NLP 实证文献中几乎从未执行。更务实的建议是：(1) 对 asymmetry 做三模型 Bonferroni（如 R1 所建议）；(2) 对 steering 保留现有 per-layer Bonferroni；(3) 明确报告哪些结论在校正后仍然成立、哪些不成立。

---

## [AGREE] R1-W8: Steering 仅在英文数据上评估

同意，这是我审稿中未显式提出的一个重要遗漏。

论文声称研究"跨语言知识冲突"，但 Section 4.6 的 steering 实验仅评估英文侧数据的 flip rate。如果核心主题是跨语言，则应至少测试：(1) 用 ZH→EN probe 对中文输入做 steering；(2) 用 EN→ZH probe 对英文输入做 cross-lingual steering。缺少这些实验使得 steering 部分与论文的跨语言定位脱节。

这进一步削弱了 detection-decision dissociation 的跨语言意义（我 N1 的延伸）。

---

## [AGREE] R1-W9: Fisher's exact test 用于 paired data

同意这是一个技术性改进点。Section 4.6 的 steering 评估对同一组样本进行 steering vs. random control 比较——这是 paired within-subject design，McNemar's test 比 Fisher's exact test 更合适。Fisher's test 假设两组独立，会低估统计功效。

不过，考虑到 steering 效应在 Llama L13 的 p 值已经很小（p=0.002），切换到 McNemar's 不太可能改变该结论方向。但对 borderline 结果（如 Qwen/Gemma 某些层）可能有影响。建议作者在修改稿中统一使用 McNemar's test。

---

## 综合评议

R1 和我在 3 个核心问题上高度一致：
1. **Detection ≠ decision claim 支撑不足**（R1-W1 ↔ 我 N1）
2. **Asymmetry 的 "consistent" 断言统计不充分**（R1-W2 ↔ 我 N3）
3. **单 split 限制可靠性**（R1-W5 ↔ 我 W2）

R1 在统计细节上更深入（W2 的 Bonferroni 校正分析、W3 的 MDE 计算、W4 的 TOST 功效、W9 的配对检验），这些补充了我审稿中的方法论盲点。

R1 唯一我有分歧的是 **W6（翻译模型=实验对象）**——翻译模型 Qwen3-8B 和实验模型 Qwen2.5-8B 是不同代际，且实验数据不支持系统性偏差假说。

**维持我的评分：Overall 3.0 (Findings)**。R1 的统计批评进一步强化了我的判断——论文的方法论基础扎实但统计推断的严谨性有改进空间，核心新颖性不足以达到主会议水平。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 416 · 2026-05-25T21:27:31.247082+00:00_

R2 交叉回应已收到。等待 R1 对 R2 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 30

## Round 30

10 recorded events


### User

_source line 417 · 2026-05-25T21:27:32.315226+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

与 Reviewer 1 在 3 个核心问题上高度一致（detection≠decision 支撑不足、asymmetry "consistent" 断言统计不充分、单 split 限制），唯一分歧在 W6（翻译模型问题）——Qwen3-8B 和 Qwen2.5-8B 是不同代际模型，实验数据不支持系统性偏差假说。维持 Overall 3.0 (Findings) 评分。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### N1 [critical] "Detection ≠ Decision" 核心 claim 支撑不足，与 Basu et al. (2026) 差异化不清晰

**[AGREE] R2-N1**

同意此为论文最大弱点。我在自己的 W1 中提出了几乎相同的判断。补充几点：

1. **与 Basu et al. 的增量**：Section 5 第三段仅用一句话区分："our L13 succeeds because we steer at mid-layer rather than probe-peak, while our three-model design isolates architecture。" 这个差异化论述过于单薄。公平地说，跨语言维度和三模型对比确实是增量，但核心 dissociation 观察（高 probe accuracy ≠ steering success）Basu et al. 已建立，本文的增量主要在于：(a) 跨语言设定、(b) 三模型对比、(c) 层级定位（mid-layer vs probe-peak），但 (a)(b) 是 setting 扩展而非 insight 扩展，(c) 是有趣的但仅基于 Llama 一个模型。

2. **因果窗口窄的 fragility 问题**：R2 指出 L16 已无效（p>0.12），因果窗口极窄。我的补充证据来自 Appendix Table 4（boundary replication），L14 p=0.002, L16 p=0.005，到 L18 已不显著——这是约 4 层（~12% depth）的窗口。在 Qwen/Gemma 仅测 1 层（L14/L17）的情况下，遗漏相邻层的可能性确实存在。

3. **方法粗糙 vs 真正 dissociation**：完全同意 R2 的判断——"steering 方法太粗糙" 是 Qwen/Gemma null result 的合理替代解释。Section 5 第二段虽列举了三个假设（non-linear interactions / superposition / architectural differences），但均未提供任何鉴别证据。

---

### N2 [critical] "General Cross-Lingual Asymmetries" 泛化声称仅基于单一语言对

**[REBUT] R2-N2**

部分反驳。R2 的批评基于对标题中 "general" 的语义理解偏差。

标题原文是 "English-Chinese Knowledge Conflict Signals **Are Consistent With** General Cross-Lingual Asymmetries"——这里 "general" 修饰的是 asymmetries 的性质（一般跨语言结构 vs 冲突特异性），而非声称实验覆盖了多语言对。标题的 claim 是：EN-ZH 上观察到的不对称性**与已知的一般跨语言结构一致**，证据是 Section 4.4 的 XNLI 非冲突基线（6 个数据点：3 模型 × 2 任务，方向全部一致，binomial p = 0.016）。

但我承认 R2 的担忧有部分道理：
- 仅 EN-ZH 一对确实限制了泛化性。XNLI 基线证明的是 "EN-ZH 不对称性不是冲突特异的"，但不能证明"同样的模式会出现在 EN-AR 或 EN-JA 上"。
- EN-DE 控制（Section 4.5, Table 2）仅用于混淆排除，未做完整探测实验。如果在 EN-DE 上也做完整四方向探测并观察到 Δ_asym ≈ 0（因为两种语言与英语的跨语言对齐程度相似），会更有说服力。

总结：标题的语义学上没有过度声称，但实验覆盖确实有限。建议作者在 Limitations 中明确单语言对的泛化边界。

---

### N3 [critical] Contribution 2 本质是 null result 被包装为正面贡献

**[REBUT] R2-N3**

不同意将此定性为"膨胀贡献计数"。

在 probing 和可解释性研究中，区分 task-specific encoding 与 general structural property 是一个有实质意义的发现。具体而言：
- **无 XNLI 基线时**：读者会自然推断 ZH→EN 迁移优势是冲突编码的特有属性，可能据此设计冲突特异的干预策略。
- **有 XNLI 基线后**：不对称性被归因于一般跨语言结构，改变了后续研究的方向——跨语言冲突干预不应从 asymmetry 入手，而应关注底层的语言对齐机制。

这种 "ruling out" 型贡献在 NLP 中有先例：Hewitt & Liang (2019) 的 selectivity 控制本身是一个 "null result"（好的 probe 在置换标签下应失败），但它改变了整个 probing 方法论。

然而，我同意此贡献的**统计证据不够强**——这是我自己 W2 和 W4 提出的：Qwen CI 包含零、TOST 功效仅 1.4%。如果统计证据更扎实（例如所有三个模型的 conflict 和 XNLI Δ_asym CI 都 exclude zero，且 TOST 通过合理等价边界），这个贡献就毫无争议了。当前状态下，Contribution 2 的 claim 比证据能支撑的更强。

---

### W1 [warning] 四个贡献的权重严重不均衡

**[AGREE] R2-W1**

同意。Contribution 1（跨语言可检测性）本质上是将 Zhao et al. (2024) 的方法扩展到 EN-ZH——是必要的基础工作但增量有限。Contribution 4（混淆排除 pipeline）更像方法论组件而非独立贡献。论文的核心价值集中在 Contribution 2 和 3，但前者统计证据不足（我的 W2），后者因果证据薄弱（我的 W1 / R2 的 N1）。

---

### W2 [warning] 单一 train/test split，缺乏交叉验证

**[AGREE] R2-W2**

完全同意，这也是我的 W5。补充一个 R2 未提及的技术点：Table 1 脚注指出 "Δ_asym is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies"。以 Llama 为例，算术差 = 70.6 − 59.6 = 11.0pp，但 bootstrap Δ_asym = +7.3pp，差距 3.7pp。这暗示 peak layer 在 bootstrap 样本间可能发生偏移，进一步说明单 split 结果不够稳定。

---

### W3 [warning] Steering 分析样本量小、多重比较负担重

**[AGREE] R2-W3**

同意。我在 W1 和 W7 中分别从样本量和全文 FWER 两个角度提出了相同担忧。Qwen n=131、Gemma n=171 的样本量对于检测微弱因果效应的功效有限。论文的 Bonferroni 校正仅限于 steering 内部（per-layer k=10），但跨分析模块的 ~100+ 检验未做整体校正。

---

### W4 [warning] 机制深度偏浅

**[AGREE] R2-W4**

部分同意。论文使用 logistic regression probing + linear steering，这在 mechanistic interpretability 谱系中属于较浅的方法。Section 5 Discussion 自己承认 "definitive validation requires activation patching"（第二段末），但未实际执行。论文更准确地说是 **probing-based analysis with causal validation attempt**，而非 full mechanistic interpretability。

不过，我不认为这构成 rejection 理由——probing + steering 的组合在当前文献中已是 accepted practice（Li et al. 2023, Turner et al. 2023, Marks & Tegmark 2024）。问题不在于方法深度，而在于从有限的 steering 结果中过度概括（回到 N1）。

---

### W5 [warning] Related Work 缺少跨语言知识编辑文献

**[REBUT] R2-W5**

部分反驳。Related Work（Section 2）第三段已引用了跨语言 steering 的近期工作：Pokharel et al. (2026) 的 training-free cross-lingual activation steering、Sundar et al. (2025) 的 cross-lingual alignment shifts、Gurgurov et al. (2026) 的 CLASBench。

R2 建议补充的三篇参考文献（Editing Across Languages survey / CLM-Bench / BMIKE-53）属于 **knowledge editing** 方向，而本文是 **probing + steering** 方向。两者虽有联系但方法论不同——knowledge editing（ROME, MEMIT 等）修改模型参数，steering 不修改参数而是在推理时干预激活。在 8 页限制下，不加区分地引用 editing 文献可能混淆读者对论文定位的理解。

但如果 R2 建议的文献中有直接分析跨语言冲突信号表征的工作，则应该引用。建议作者在 camera-ready 中选择性引用最相关的 1-2 篇。

---

### W6 [info] 缺少独立 Conclusion 章节

**[REBUT] R2-W6**

R2 事实判断有误。论文有独立的 Section 6 Conclusion（PDF 第 8 页底部），包含两句话的总结。该章节确实简短（仅 2 句），但它存在。R2 可能因其篇幅过短而忽略了它，或将 Discussion（Section 5）与 Conclusion（Section 6）混淆。

---

### 总结

与 R2 在核心判断上高度一致：**N1（detection ≠ decision 论断证据不足）** 是论文最大的弱点，我们两位 reviewer 独立达成了相同结论。N2（标题泛化性）我认为 R2 对标题语义有误读，但实验覆盖有限的担忧是合理的。N3（null result 作为贡献）我持不同意见——排除冲突特异性是有意义的发现，但当前统计证据确实偏弱。

我维持自己的 **Overall 3.0 (Findings)** 评分不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-25T21:28:07.179941+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "clkc_mech_interp"
  }
}
```

</details>

---


### Tool call

_source line 419 · 2026-05-25T21:28:07.330981+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "clkc_mech_interp"
  }
}
```

</details>

---


### Tool result

_source line 420 · 2026-05-25T21:28:07.331462+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T21:15:20.063962+00:00\", \"completed_at\": \"2026-05-25T21:18:51.933693+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"单页堆叠 3 个 display items（Figure 3 + Table 1 + Figure 4），每个尺寸偏小；Figure 3 的 axis label 和 legend 字号接近可读下限，建议适当放大或拆分到两页\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"末页（appendix）底部约 35% 空白，可考虑调整 appendix 内容分布以充分利用空间\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"纯文本页（Experimental Setup），虽未违反连续纯文本规则（P4 有 Figure 2 间隔），但该页信息密度高，可考虑将部分 setup 细节移至 appendix 以腾出空间给主文 display items\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 3}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-25T21:28:07.381985+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-25T21:30:46.816512+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "clkc_mech_interp",
  "issues_yaml": "issues:\n# === Round 4 — RECURRING ISSUES (from Round 3, still present) ===\n\n- id: \"R3-N2\"\n  summary: \"COMET tercile 消融 MDD=25.3pp 混淆排除功效不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 认为'本质上无效'，R2 部分反驳——多证据链部分弥补\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 再次标记为 critical (W3)，R2 部分同意但指出多层控制框架(XNLI+EN-DE)部分缓解。Gemma +10.3pp 混淆方向趋势仍未解决。\"\n  action_items:\n    - round: 3\n      action: \"§4.5 重构：论证重心从 COMET tercile 转向 token overlap + EN-DE 对照\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"增加连续回归分析(COMET score vs probe acc)替代 tercile；或增大样本量；对 Gemma +10.3pp 做深入调查\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"因果证据仅限 Llama L13 单模型单层，detection≠decision claim 过度概括\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Contribution 暗示跨架构发现，实为 1正2负\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W1 和 R2-N1 独立提出相同判断并在交叉回应中 AGREE。Qwen/Gemma 各仅测1层(L14/L17)，替代解释未排除(非线性通路、不同因果窗口、样本量不足)。与 Basu et al. 2026 差异化不清晰。\"\n  action_items:\n    - round: 3\n      action: \"Contribution 重写限定为 Llama-specific + 三层解离证据\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"(1) Abstract/Conclusion 进一步降级 claim 为 Llama-specific observation；(2) 对 Qwen/Gemma 补充至少 3 层 steering；(3) 强化 Basu et al. 差异化论述(跨语言+三模型+层定位)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1\"\n  summary: \"单一 train/test split 缺乏 k-fold cross-validation\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Belinkov 2022 推荐 CV 为标准做法\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W5 和 R2-W2 再次标记。Bootstrap CI 仅捕获 split 内变异。Δ_asym arithmetic diff (11.0pp) vs bootstrap mean (7.3pp) 差距暗示 peak layer 偏移。\"\n  action_items:\n    - round: 3\n      action: \"Limitations 加 k-fold CV 承诺 + camera-ready 计划\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"在当前版本完成至少 3-fold CV 主要结果(Table 1)，不再仅承诺 camera-ready\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2\"\n  summary: \"Qwen3-8B 同时作为翻译模型和实验对象的双重角色\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Qwen EN→ZH transfer accuracy 最高(67.3%)，与 aligned 假设方向一致\"\n    - round: 4\n      reviewers: [1]\n      note: \"R1-W6 再次提出。R2 反驳称 Qwen3 vs Qwen2.5 是不同代际，但论文实际使用 Qwen3-8B 做两者(Section 3.2 + 4.1)，R2 事实判断有误。Llama/Gemma 独立验证相同 pattern 部分缓解。\"\n  action_items:\n    - round: 3\n      action: \"Limitations 增强 Qwen dual role 讨论\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"正文中更显著标注此利益冲突；或用独立翻译模型(如 NLLB)做额外验证\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W6\"\n  summary: \"Discussion 三个 mechanistic 假说全部 untested\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [2, 1]\n      note: \"建议至少验证一个\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W4 指出机制深度偏浅(probing-level 非 circuit-level)。R1 交叉 AGREE(部分)——probing+steering 是 accepted practice 但不应从中过度概括。Discussion 仍仅列假说未验证。\"\n  action_items:\n    - round: 3\n      action: \"MLP probe 数据验证假说1 + registry 数据验证假说2/3\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"考虑 activation patching 验证至少一个假说；或在 framing 中重定位为 empirical probing study\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-NOV\"\n  summary: \"新颖性被 Basu et al. (2026) 先行发现削弱\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"detection≠decision 已被 Basu 部分 preempt\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-N1 再次标记，R1 在交叉中 AGREE 并补充：Section 5 仅一句差异化论述过于单薄。增量在 setting 扩展(跨语言+三模型)而非 insight 扩展。\"\n  action_items:\n    - round: 3\n      action: \"Contribution 合并 + Basu 差异化写入 discussion\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"Section 2 或 Section 5 增加与 Basu et al. 的逐点对比段落(≥3 差异点)；重新定位为'跨语言设定下的 replication + extension'而非独立发现\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 4 — NEW ISSUES ===\n\n- id: \"R4-N1\"\n  summary: \"Qwen 不对称性 CI 包含零；Bonferroni 校正后仅 Gemma 显著\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W2 首次提出，R2 交叉 AGREE。Qwen CI [-0.6, 13.7] 跨零。三模型 Bonferroni 阈值 0.017 下 Llama p=0.038 也不显著。仅 Gemma p=0.006 幸存。'Consistent across all three' 论断统计不充分。\"\n  action_items:\n    - round: 4\n      action: \"(1) 明确报告 Qwen 不显著而非'marginally includes zero'；(2) 报告 Bonferroni 校正后结果；(3) 依赖方向一致性 binomial test(p=0.016) + XNLI 独立复制作为主要论据\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W1\"\n  summary: \"全文多重假设检验缺乏整体 FWER 控制\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W7 提出，R2 部分同意。全文 ~100+ 检验仅 steering 做了 per-layer Bonferroni。三模型 asymmetry 属同一族未校正。建议至少对同族检验做校正并报告。\"\n  action_items:\n    - round: 4\n      action: \"对 asymmetry 三模型检验做 Bonferroni/Holm 校正并报告校正后结果；明确标注哪些结论校正后仍成立\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W2\"\n  summary: \"Steering 仅在英文数据评估，未测试跨语言因果干预\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W8 提出，R2 AGREE。论文主题是跨语言冲突，但 steering 实验仅用英文 test data。未测试中文输入 steering 或 cross-lingual steering(ZH→EN probe 对 ZH 输入)。\"\n  action_items:\n    - round: 4\n      action: \"至少在 Llama L13 上测试中文输入 steering + ZH→EN probe cross-lingual steering\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W3\"\n  summary: \"TOST 等价检验功效 1.4%，uninformative\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 AGREE。±2pp 边界对 n~200 和 SE~5-8pp 过窄，检验注定失败。报告 uninformative 检验有空洞分析之嫌。\"\n  action_items:\n    - round: 4\n      action: \"要么使用合理等价边界(±5pp)重做 TOST；要么删除 TOST，改用 CI 重叠 + binomial direction consistency 的定性论证\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W4\"\n  summary: \"贡献权重不均衡；Contribution 2(asymmetry)定位有争议\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W1/N3 提出(null result 包装为贡献)，R1 REBUT(ruling-out 有方法论价值)但同意统计证据不够强。分歧：C2 是否应为独立贡献。共识：当前证据力度不足以支撑该 claim 的强度。\"\n  action_items:\n    - round: 4\n      action: \"考虑将 C2 并入 C1 作为分析组成部分，或保留但降低措辞强度(consistent with → preliminary evidence consistent with)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-I1\"\n  summary: \"Fisher's exact test 用于 paired steering data，应为 McNemar's\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W9 提出，R2 AGREE。Same samples receive both steering and random control = paired within-subject design。Fisher 假设独立样本。对 Llama L13 (p=0.002) 不影响结论方向，但对 borderline 结果可能有影响。\"\n  action_items:\n    - round: 4\n      action: \"补充 McNemar's test 结果或论证 Fisher 在此 setting 的保守性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 3 RESOLVED (confirmed in Round 4) ===\n\n- id: \"R3-N1\"\n  summary: \"标题 'Mirror' 等价性主张与 TOST 功效不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"建议改 Mirror→Consistent With\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"标题已改为 'Are Consistent With'。R1 在交叉回应中确认标题语义无过度声称。\"\n  action_items:\n    - round: 3\n      action: \"标题 Mirror→Consistent With\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"标题已改为 'English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries'。R4 Reviewer 确认。\"\n  resolution_round: 4\n\n- id: \"R3-W3\"\n  summary: \"Probe selectivity 未正式评估\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"引用 Hewitt & Liang 2019 但未执行\"\n  action_items:\n    - round: 3\n      action: \"Random labels selectivity control\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Selectivity control 完成，R4 R1 在 S4 确认(49.2-51.0% chance, gap 21-40pp)。\"\n  resolution_round: 4\n\n- id: \"R3-W4\"\n  summary: \"缺少 AUROC 阈值无关评估指标\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AUROC 对 Gemma 尤其有意义\"\n  action_items:\n    - round: 3\n      action: \"AUROC 计算 + Appendix\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"AUROC 完成(Llama 0.981, Gemma 0.931, Qwen 0.771)。R4 未再标记。\"\n  resolution_round: 4\n\n- id: \"R3-W5\"\n  summary: \"Steering α 值选择缺乏理论依据\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"α∈{±20,±10,±5,±2,±1} 无规范化\"\n  action_items:\n    - round: 3\n      action: \"Method 加入 α 选择理由 + Turner/Marks 引用\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Section 4.6 已引用 Turner 2023 和 Marks 2024 作为 α sweep 惯例。R4 未再标记。\"\n  resolution_round: 4\n\n- id: \"R3-M1\"\n  summary: \"COMET 版本号未标注\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"需标注具体版本\"\n  action_items:\n    - round: 3\n      action: \"加入 wmt22-comet-da\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Section 4.1 已标注 'wmt22-comet-da'。R4 未再标记。\"\n  resolution_round: 4\n\n- id: \"R3-M2\"\n  summary: \"Token overlap 仅用 Jaccard 粗粒度指标\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"EN-ZH 字符系统不同使 3-4% 已足够\"\n  action_items:\n    - round: 3\n      action: \"加入 floor imposed by distinct writing systems\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Section 4.5 已加入解释。R4 R1-S3 确认 EN-DE 控制(14.8% vs 3.8%)有效。\"\n  resolution_round: 4\n\n- id: \"R3-M4\"\n  summary: \"Random direction control 仅为最低标准\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"更强 control 方向\"\n  action_items:\n    - round: 3\n      action: \"Limitations 提及更强 control 方向\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Limitations 已提及。R4 R1-S5 确认 random control 设计合理(等幅 r~N(0,I))。\"\n  resolution_round: 4\n\n- id: \"R3-M5\"\n  summary: \"Figure 3 灰色带暗示 TOST 有效但功效不支持\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"±2pp 灰色带视觉暗示 meaningful zone\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Figure caption 已改为 'exploratory equivalence margin' + TOST power 1.4% 标注。R4 未标记视觉误导问题(仅标记 TOST 本身 uninformative)。\"\n  action_items:\n    - round: 3\n      action: \"Figure caption 改为 exploratory\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Caption 已修改。视觉误导问题解决。TOST uninformative 性质已单独列为 R4-W3。\"\n  resolution_round: 4\n\n# === PREVIOUSLY RESOLVED (Rounds 1-2, confirmed stable) ===\n\n- id: \"R2-W2\"\n  summary: \"标题仅测试 EN-ZH 一个语言对构成 overclaiming\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"标题应加限定\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"升级为 Must-Fix\"\n  action_items:\n    - round: 2\n      action: \"标题加入 English-Chinese 限定\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"标题已限定为 English-Chinese。R4 R1 在 N2 rebut 中确认标题语义正确。\"\n  resolution_round: 3\n\n- id: \"MF-2\"\n  summary: \"标题 Inherit 因果措辞仅有相关性证据\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"Inherit→Mirror→Consistent With\"\n  action_items:\n    - round: 2\n      action: \"全文替换\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS. R4 确认标题用 'Consistent With'。\"\n  resolution_round: 3\n\n- id: \"R1-N2\"\n  summary: \"Detection ≠ Decision 因果声明仅在 Llama 成立\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"最核心局限\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"升级为 MF-3\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Contribution 重写限定，但根本问题未解\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"合并至 R3-N3。四轮持续存在的核心问题。\"\n  action_items:\n    - round: 2\n      action: \"Reframe 为 architecture-dependent\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M3\"\n  summary: \"无代码/数据可用性声明\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"double-blind 可用匿名链接\"\n  action_items:\n    - round: 3\n      action: \"加入声明\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"匿名代码仓库已提供。R4 确认。\"\n  resolution_round: 3\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "clkc_mech_interp",
    "issues_yaml": "issues:\n# === Round 4 — RECURRING ISSUES (from Round 3, still present) ===\n\n- id: \"R3-N2\"\n  summary: \"COMET tercile 消融 MDD=25.3pp 混淆排除功效不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 认为'本质上无效'，R2 部分反驳——多证据链部分弥补\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 再次标记为 critical (W3)，R2 部分同意但指出多层控制框架(XNLI+EN-DE)部分缓解。Gemma +10.3pp 混淆方向趋势仍未解决。\"\n  action_items:\n    - round: 3\n      action: \"§4.5 重构：论证重心从 COMET tercile 转向 token overlap + EN-DE 对照\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"增加连续回归分析(COMET score vs probe acc)替代 tercile；或增大样本量；对 Gemma +10.3pp 做深入调查\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"因果证据仅限 Llama L13 单模型单层，detection≠decision claim 过度概括\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Contribution 暗示跨架构发现，实为 1正2负\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W1 和 R2-N1 独立提出相同判断并在交叉回应中 AGREE。Qwen/Gemma 各仅测1层(L14/L17)，替代解释未排除(非线性通路、不同因果窗口、样本量不足)。与 Basu et al. 2026 差异化不清晰。\"\n  action_items:\n    - round: 3\n      action: \"Contribution 重写限定为 Llama-specific + 三层解离证据\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"(1) Abstract/Conclusion 进一步降级 claim 为 Llama-specific observation；(2) 对 Qwen/Gemma 补充至少 3 层 steering；(3) 强化 Basu et al. 差异化论述(跨语言+三模型+层定位)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W1\"\n  summary: \"单一 train/test split 缺乏 k-fold cross-validation\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Belinkov 2022 推荐 CV 为标准做法\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W5 和 R2-W2 再次标记。Bootstrap CI 仅捕获 split 内变异。Δ_asym arithmetic diff (11.0pp) vs bootstrap mean (7.3pp) 差距暗示 peak layer 偏移。\"\n  action_items:\n    - round: 3\n      action: \"Limitations 加 k-fold CV 承诺 + camera-ready 计划\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"在当前版本完成至少 3-fold CV 主要结果(Table 1)，不再仅承诺 camera-ready\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W2\"\n  summary: \"Qwen3-8B 同时作为翻译模型和实验对象的双重角色\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Qwen EN→ZH transfer accuracy 最高(67.3%)，与 aligned 假设方向一致\"\n    - round: 4\n      reviewers: [1]\n      note: \"R1-W6 再次提出。R2 反驳称 Qwen3 vs Qwen2.5 是不同代际，但论文实际使用 Qwen3-8B 做两者(Section 3.2 + 4.1)，R2 事实判断有误。Llama/Gemma 独立验证相同 pattern 部分缓解。\"\n  action_items:\n    - round: 3\n      action: \"Limitations 增强 Qwen dual role 讨论\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"正文中更显著标注此利益冲突；或用独立翻译模型(如 NLLB)做额外验证\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W6\"\n  summary: \"Discussion 三个 mechanistic 假说全部 untested\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [2, 1]\n      note: \"建议至少验证一个\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W4 指出机制深度偏浅(probing-level 非 circuit-level)。R1 交叉 AGREE(部分)——probing+steering 是 accepted practice 但不应从中过度概括。Discussion 仍仅列假说未验证。\"\n  action_items:\n    - round: 3\n      action: \"MLP probe 数据验证假说1 + registry 数据验证假说2/3\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"考虑 activation patching 验证至少一个假说；或在 framing 中重定位为 empirical probing study\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-NOV\"\n  summary: \"新颖性被 Basu et al. (2026) 先行发现削弱\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"detection≠decision 已被 Basu 部分 preempt\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-N1 再次标记，R1 在交叉中 AGREE 并补充：Section 5 仅一句差异化论述过于单薄。增量在 setting 扩展(跨语言+三模型)而非 insight 扩展。\"\n  action_items:\n    - round: 3\n      action: \"Contribution 合并 + Basu 差异化写入 discussion\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"Section 2 或 Section 5 增加与 Basu et al. 的逐点对比段落(≥3 差异点)；重新定位为'跨语言设定下的 replication + extension'而非独立发现\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 4 — NEW ISSUES ===\n\n- id: \"R4-N1\"\n  summary: \"Qwen 不对称性 CI 包含零；Bonferroni 校正后仅 Gemma 显著\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W2 首次提出，R2 交叉 AGREE。Qwen CI [-0.6, 13.7] 跨零。三模型 Bonferroni 阈值 0.017 下 Llama p=0.038 也不显著。仅 Gemma p=0.006 幸存。'Consistent across all three' 论断统计不充分。\"\n  action_items:\n    - round: 4\n      action: \"(1) 明确报告 Qwen 不显著而非'marginally includes zero'；(2) 报告 Bonferroni 校正后结果；(3) 依赖方向一致性 binomial test(p=0.016) + XNLI 独立复制作为主要论据\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W1\"\n  summary: \"全文多重假设检验缺乏整体 FWER 控制\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W7 提出，R2 部分同意。全文 ~100+ 检验仅 steering 做了 per-layer Bonferroni。三模型 asymmetry 属同一族未校正。建议至少对同族检验做校正并报告。\"\n  action_items:\n    - round: 4\n      action: \"对 asymmetry 三模型检验做 Bonferroni/Holm 校正并报告校正后结果；明确标注哪些结论校正后仍成立\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W2\"\n  summary: \"Steering 仅在英文数据评估，未测试跨语言因果干预\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W8 提出，R2 AGREE。论文主题是跨语言冲突，但 steering 实验仅用英文 test data。未测试中文输入 steering 或 cross-lingual steering(ZH→EN probe 对 ZH 输入)。\"\n  action_items:\n    - round: 4\n      action: \"至少在 Llama L13 上测试中文输入 steering + ZH→EN probe cross-lingual steering\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W3\"\n  summary: \"TOST 等价检验功效 1.4%，uninformative\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W4 提出，R2 AGREE。±2pp 边界对 n~200 和 SE~5-8pp 过窄，检验注定失败。报告 uninformative 检验有空洞分析之嫌。\"\n  action_items:\n    - round: 4\n      action: \"要么使用合理等价边界(±5pp)重做 TOST；要么删除 TOST，改用 CI 重叠 + binomial direction consistency 的定性论证\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W4\"\n  summary: \"贡献权重不均衡；Contribution 2(asymmetry)定位有争议\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W1/N3 提出(null result 包装为贡献)，R1 REBUT(ruling-out 有方法论价值)但同意统计证据不够强。分歧：C2 是否应为独立贡献。共识：当前证据力度不足以支撑该 claim 的强度。\"\n  action_items:\n    - round: 4\n      action: \"考虑将 C2 并入 C1 作为分析组成部分，或保留但降低措辞强度(consistent with → preliminary evidence consistent with)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-I1\"\n  summary: \"Fisher's exact test 用于 paired steering data，应为 McNemar's\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1-W9 提出，R2 AGREE。Same samples receive both steering and random control = paired within-subject design。Fisher 假设独立样本。对 Llama L13 (p=0.002) 不影响结论方向，但对 borderline 结果可能有影响。\"\n  action_items:\n    - round: 4\n      action: \"补充 McNemar's test 结果或论证 Fisher 在此 setting 的保守性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 3 RESOLVED (confirmed in Round 4) ===\n\n- id: \"R3-N1\"\n  summary: \"标题 'Mirror' 等价性主张与 TOST 功效不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"建议改 Mirror→Consistent With\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"标题已改为 'Are Consistent With'。R1 在交叉回应中确认标题语义无过度声称。\"\n  action_items:\n    - round: 3\n      action: \"标题 Mirror→Consistent With\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"标题已改为 'English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries'。R4 Reviewer 确认。\"\n  resolution_round: 4\n\n- id: \"R3-W3\"\n  summary: \"Probe selectivity 未正式评估\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"引用 Hewitt & Liang 2019 但未执行\"\n  action_items:\n    - round: 3\n      action: \"Random labels selectivity control\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Selectivity control 完成，R4 R1 在 S4 确认(49.2-51.0% chance, gap 21-40pp)。\"\n  resolution_round: 4\n\n- id: \"R3-W4\"\n  summary: \"缺少 AUROC 阈值无关评估指标\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AUROC 对 Gemma 尤其有意义\"\n  action_items:\n    - round: 3\n      action: \"AUROC 计算 + Appendix\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"AUROC 完成(Llama 0.981, Gemma 0.931, Qwen 0.771)。R4 未再标记。\"\n  resolution_round: 4\n\n- id: \"R3-W5\"\n  summary: \"Steering α 值选择缺乏理论依据\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"α∈{±20,±10,±5,±2,±1} 无规范化\"\n  action_items:\n    - round: 3\n      action: \"Method 加入 α 选择理由 + Turner/Marks 引用\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Section 4.6 已引用 Turner 2023 和 Marks 2024 作为 α sweep 惯例。R4 未再标记。\"\n  resolution_round: 4\n\n- id: \"R3-M1\"\n  summary: \"COMET 版本号未标注\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"需标注具体版本\"\n  action_items:\n    - round: 3\n      action: \"加入 wmt22-comet-da\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Section 4.1 已标注 'wmt22-comet-da'。R4 未再标记。\"\n  resolution_round: 4\n\n- id: \"R3-M2\"\n  summary: \"Token overlap 仅用 Jaccard 粗粒度指标\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"EN-ZH 字符系统不同使 3-4% 已足够\"\n  action_items:\n    - round: 3\n      action: \"加入 floor imposed by distinct writing systems\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Section 4.5 已加入解释。R4 R1-S3 确认 EN-DE 控制(14.8% vs 3.8%)有效。\"\n  resolution_round: 4\n\n- id: \"R3-M4\"\n  summary: \"Random direction control 仅为最低标准\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"更强 control 方向\"\n  action_items:\n    - round: 3\n      action: \"Limitations 提及更强 control 方向\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Limitations 已提及。R4 R1-S5 确认 random control 设计合理(等幅 r~N(0,I))。\"\n  resolution_round: 4\n\n- id: \"R3-M5\"\n  summary: \"Figure 3 灰色带暗示 TOST 有效但功效不支持\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"±2pp 灰色带视觉暗示 meaningful zone\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Figure caption 已改为 'exploratory equivalence margin' + TOST power 1.4% 标注。R4 未标记视觉误导问题(仅标记 TOST 本身 uninformative)。\"\n  action_items:\n    - round: 3\n      action: \"Figure caption 改为 exploratory\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Caption 已修改。视觉误导问题解决。TOST uninformative 性质已单独列为 R4-W3。\"\n  resolution_round: 4\n\n# === PREVIOUSLY RESOLVED (Rounds 1-2, confirmed stable) ===\n\n- id: \"R2-W2\"\n  summary: \"标题仅测试 EN-ZH 一个语言对构成 overclaiming\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [2, 1]\n      note: \"标题应加限定\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"升级为 Must-Fix\"\n  action_items:\n    - round: 2\n      action: \"标题加入 English-Chinese 限定\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"标题已限定为 English-Chinese。R4 R1 在 N2 rebut 中确认标题语义正确。\"\n  resolution_round: 3\n\n- id: \"MF-2\"\n  summary: \"标题 Inherit 因果措辞仅有相关性证据\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2, 1]\n      note: \"Inherit→Mirror→Consistent With\"\n  action_items:\n    - round: 2\n      action: \"全文替换\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Reviewer PASS. R4 确认标题用 'Consistent With'。\"\n  resolution_round: 3\n\n- id: \"R1-N2\"\n  summary: \"Detection ≠ Decision 因果声明仅在 Llama 成立\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"最核心局限\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"升级为 MF-3\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Contribution 重写限定，但根本问题未解\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"合并至 R3-N3。四轮持续存在的核心问题。\"\n  action_items:\n    - round: 2\n      action: \"Reframe 为 architecture-dependent\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-M3\"\n  summary: \"无代码/数据可用性声明\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"double-blind 可用匿名链接\"\n  action_items:\n    - round: 3\n      action: \"加入声明\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"匿名代码仓库已提供。R4 确认。\"\n  resolution_round: 3\n"
  }
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-25T21:30:46.917742+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_issues.yaml\", \"bytes\": 14254}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-25T21:33:12.649644+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 4 审稿报告 — clkc_mech_interp\n\n**Target Venue**: EMNLP 2026 (via ARR) | **Deadline**: 2026-06-15\n**Paper**: \"English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries\"\n**Reviewers**: R1 (方法严谨性) + R2 (新颖性/完整性) | **Cross-sharing**: 完成\n\n---\n\n## Summary\n\n本文将知识冲突信号的 probing 分析从单语扩展到英-中跨语言设置，在三个 LLM（Llama-3.1-8B-Instruct、Qwen3-8B、Gemma-2-9B-IT）上训练残差流探针、构建 XNLI 非冲突基线、执行 COMET/token overlap/EN-DE 混淆排除、并进行因果 steering 实验。主要发现：(1) 冲突信号在所有模型和方向上线性可检测；(2) ZH→EN ~7pp 迁移优势与 XNLI 一致，反映一般跨语言结构；(3) 仅 Llama L13 (41% depth) steering 成功，Qwen/Gemma 无效，据此提出 detection≠decision dissociation。\n\n---\n\n## Strengths\n\n1. **混淆因素控制设计出色**：COMET 翻译质量分层 + XNLI 非冲突基线 + EN-DE 类型学控制的三层设计是可复用的方法论贡献。EN-DE Jaccard 14.8% vs EN-ZH 3.8% 但 Δ≈0 有效排除 token overlap。[R1-S2/S3, R2-S1]\n2. **多模型验证**：三个架构差异显著的模型仅 3.5% 问题重叠，构成近似独立复制。方向一致性 binomial p = 0.016。[R1-S1, R2-S2]\n3. **统计方法规范**：Bootstrap CI (n=2000)、Bonferroni 校正、Fisher 精确检验、selectivity control (gap 21-40pp)、matched-condition 控制均达标。[R1-S4/S5, R2-S3]\n4. **诚实报告负面结果**：Qwen/Gemma steering 失败、asymmetry 非冲突特异性的如实报告优于领域平均水平。[R2-S4]\n5. **Seed replication**：独立 seed 复现 Llama L13 因果效应 (N=201)，排除单次 split 偶然性。[R2-S5]\n6. **代码可用 + AI 使用声明透明**：匿名代码仓库提供，AI 辅助使用明确标注。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**[C1] Detection ≠ Decision 核心 claim 过度概括（R1-W1, R2-N1; 双方 AGREE）**\n- 正面因果证据仅来自 Llama L13 一层。Qwen (L14) 和 Gemma (L17) 各仅测 1 层即宣告 null，但 Llama 自身因果窗口仅 ~4 层 (L13-L16)，遗漏相邻层完全可能。\n- 替代解释未排除：非线性因果通路、不同因果窗口位置、样本量功效不足 (n=131/171)、线性 steering 方法本身的局限性。\n- Basu et al. (2026) \"Interpretability without actionability\" 已在单语中建立 detection-steering dissociation。本文差异化论述仅 Section 5 一句话，过于单薄。\n- **Action required**: (1) Qwen/Gemma 补充至少 3 层相邻层 steering；(2) 若无法执行，将 claim 严格限定为 Llama-specific observation；(3) 增加与 Basu et al. 的逐点差异化段落。\n\n**[C2] Asymmetry \"consistent across all three models\" 统计不充分（R1-W2; R2 交叉 AGREE）**\n- Qwen Δ_asym = +7.2pp, CI [-0.6, 13.7] 跨越零，α=0.05 下不显著。\n- 三模型 Bonferroni 校正（阈值 0.017）：Llama p=0.038 不显著、Gemma p=0.006 显著、Qwen n.s.——仅 1/3 模型通过校正。\n- Section 4.3 \"consistent in direction across all three architectures\" 措辞超越了证据能支撑的范围。\n- **Action required**: (1) 明确报告 Qwen 不显著；(2) 报告 Bonferroni 校正后结果；(3) 主要论据改为方向一致性 binomial test (p=0.016) + XNLI 六点复制。\n\n**[C3] COMET tercile 混淆排除欠功效，Gemma 趋势未解释（R1-W3; R2 部分 AGREE）**\n- MDE = 25.3pp at 80% power，对中等效应完全不敏感。\n- Gemma Δ = +10.3pp 在混淆方向，p=0.278 在低功效下不排除实质效应。\n- 多层控制（XNLI + EN-DE）部分缓解，但 COMET 分析作为独立证据线本质无效。\n- **Action required**: 增加连续回归 (COMET score vs probe accuracy) 替代 tercile；对 Gemma 趋势深入调查。\n\n### Warning（影响评分）\n\n**[W1] 单一 train/test split 贯穿全文（R1-W5, R2-W2; 双方 AGREE）**\n- Bootstrap CI 仅捕获 split 内变异。Δ_asym arithmetic diff (11.0pp) vs bootstrap mean (7.3pp) 差距 3.7pp 暗示 peak layer 不稳定。\n- **Action**: 当前版本完成至少 3-fold CV 主要结果。\n\n**[W2] TOST 等价检验功效 1.4%，uninformative（R1-W4; R2 AGREE）**\n- ±2pp 边界对 n~200、SE~5-8pp 注定失败。报告无信息量检验有空洞分析之嫌。\n- **Action**: 删除 TOST 或用合理边界 (±5pp) 重做。\n\n**[W3] Steering 仅英文数据，未测试跨语言因果干预（R1-W8; R2 AGREE）**\n- 论文主题是跨语言冲突，但因果实验仅用英文侧。缺少 ZH 输入 steering 和 cross-lingual steering。\n- **Action**: 至少在 Llama L13 测试中文输入 steering。\n\n**[W4] 全文多重假设检验缺乏整体 FWER 控制（R1-W7; R2 部分 AGREE）**\n- ~100+ 检验仅 steering per-layer Bonferroni。Asymmetry 三模型属同一族未校正。\n- **Action**: 对 asymmetry 做 Bonferroni/Holm 校正并报告。\n\n**[W5] Qwen3-8B 同时作为翻译模型和实验对象（R1-W6; 分歧）**\n- R2 反驳称不同代际（Qwen3 vs Qwen2.5），但论文 Section 3.2 和 4.1 均为 Qwen3-8B——R2 事实判断有误，R1 担忧成立。\n- Llama/Gemma 独立验证相同 pattern 部分缓解。\n- **Action**: 正文更显著标注；或用独立翻译模型验证。\n\n**[W6] 贡献权重不均衡 / C2 定位争议（R2-W1/N3 vs R1 REBUT; 分歧）**\n- R2 认为 C2 (asymmetry = general structure) 是 null result 包装为贡献；R1 反驳 ruling-out 有方法论价值。\n- **共识**：不论定位，当前统计证据 (Qwen CI 含零、TOST 无效) 不足以支撑 claim 的强度。\n- **Action**: 降低措辞强度或并入 C1。\n\n**[W7] 机制深度偏浅（R2-W4; R1 部分 AGREE）**\n- Logistic regression probing + linear steering 在 mechanistic interpretability 谱系中属浅层。Discussion 列三个假说均未验证。\n- **Action**: 重新定位为 empirical probing study 或补充 activation patching。\n\n### Info\n\n**[I1] Fisher's exact test 用于 paired steering data（R1-W9; R2 AGREE）**\n- Steering vs random control 是 paired design，McNemar's test 更合适。对 L13 (p=0.002) 不改变结论，但应在修改稿中统一。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 状态 |\n|------|----|----|------|\n| Detection≠decision 过度概括 | W1 [critical] | N1 [critical] | **[AGREE]** |\n| Qwen CI 含零 / Bonferroni 后仅 Gemma 显著 | W2 [critical] | 交叉 AGREE | **[AGREE]** |\n| COMET tercile 欠功效 | W3 [critical] | 部分 AGREE（多层设计部分缓解）| **[AGREE-partial]** |\n| 单 split 无 CV | W5 [warning] | W2 [warning] | **[AGREE]** |\n| TOST 1.4% uninformative | W4 [warning] | AGREE | **[AGREE]** |\n| Steering 仅英文 | W8 [warning] | AGREE | **[AGREE]** |\n| Global FWER | W7 [warning] | 部分 AGREE | **[AGREE-partial]** |\n| Fisher on paired data | W9 [info] | AGREE | **[AGREE]** |\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 分歧本质 |\n|------|----|----|----------|\n| 标题 \"General\" overclaim | REBUT（标题说 \"Consistent With\" 无问题）| N2 [critical] | 语义解读差异；R1 认为标题准确，R2 认为实验覆盖不足 |\n| C2 是否为 null result | REBUT（ruling-out 有价值）| N3 [critical] | 方法论哲学差异；共识是证据力度不足 |\n| Qwen 翻译模型双重角色 | W6 [warning] | REBUT（不同代际）| R2 事实判断有误（论文确为同一模型 Qwen3-8B）|\n| 跨语言知识编辑文献 | REBUT（不同方向）| W5 [warning] | 相关性判断差异；R1 认为 editing ≠ probing/steering |\n\n---\n\n## Questions to Authors（汇总，去重后 10 条）\n\n1. Basu et al. (2026) 已建立单语 detection-steering dissociation。本文跨语言设定具体揭示了哪些单语无法观察到的现象？\n2. Qwen/Gemma 是否测试了目标层 ±2 层范围？如果 Llama 因果窗口仅 4 层宽，仅测 1 层的 null 能否排除存在因果位点？\n3. Qwen Δ_asym CI [-0.6, 13.7] 包含零。三模型 Bonferroni 校正后仅 Gemma 显著。如何维护 \"consistent\" 论断？\n4. Table 1 Δ_asym (bootstrap mean 7.3pp) 与算术差 (11.0pp) 差距 3.7pp 的来源？是否暗示 peak layer 在 bootstrap 样本间偏移？\n5. Gemma COMET tercile Δ=+10.3pp 在混淆方向——能否提供 COMET score 与 probe accuracy 的连续回归结果？\n6. EN-DE 已翻译完成（Section 3.5）——为何不做完整四方向探测实验以直接支持泛化 claim？\n7. Steering 为何仅在英文数据评估？中文输入 + ZH→EN probe steering 的结果？\n8. 如果选择 ±5pp 等价边界重做 TOST，预计结论是否改变？\n9. 论文称 Gemma ConflictQA 保留 1590 样本，但 probe accuracy 最高 (88.9% at L17)。保留率最高+准确率最高是否暗示 probe 捕获了 task-irrelevant 信号？\n10. All-position injection 与 last-token injection 在 L13 产生 \"identical results\"——具体数字？\n\n---\n\n## Missing References\n\n**R2 建议（R1 部分反驳）**：\n- \"Editing Across Languages: A Survey of Multilingual Knowledge Editing\" (2025)\n- CLM-Bench (2026)\n- BMIKE-53 (53-language knowledge editing benchmark)\n\nR1 认为 knowledge editing (参数修改) 与 probing/steering (推理时干预) 方法论不同，8 页限制下引用需选择性。建议选择性引用最相关的 1 篇。\n\n---\n\n## External Review\n\n**状态**: 未配置（项目未启用 paperreview.ai）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成 | 0 critical, 0 warning, 3 info\n\n排版质量良好，仅有三个建议性意见：\n1. **Page 6**: 单页堆叠 3 个 display items (Figure 3 + Table 1 + Figure 4)，每个尺寸偏小，Figure 3 axis label 和 legend 字号接近可读下限\n2. **Page 12**: 末页 appendix 底部约 35% 空白\n3. **Page 5**: 纯文本高密度页（Experimental Setup），可考虑将部分细节移至 appendix\n\n---\n\n## Overall Assessment\n\n### 评分: 3.0 — Findings\n\n**R1**: 3.0 (Findings) | Confidence 4/5\n**R2**: 3.0 (Findings) | Confidence 4/5\n**Director 综合**: **3.0 (Findings)**\n\n### 评分理由\n\n**为什么不是 3.5 (Borderline Conference)**：\n- 核心因果贡献 (detection≠decision) 仅 1/3 模型 1/32 层支持，替代解释未排除\n- 与 Basu et al. (2026) 差异化不清晰——核心 insight 已被单语工作建立\n- Asymmetry \"consistency\" 统计不充分（Bonferroni 后仅 1/3 模型显著）\n- 四个贡献中两个薄弱（C2 统计不足、C3 证据单薄）\n\n**为什么不是 2.5 (Borderline Findings)**：\n- 混淆因素控制设计 (XNLI + EN-DE + COMET) 是真正可复用的方法论贡献\n- 三模型 × 两任务方向一致性 (binomial p=0.016) 提供跨架构描述性证据\n- 统计方法总体规范（bootstrap、Bonferroni、selectivity control）\n- 诚实报告负面结果 + 代码公开\n- Seed replication 增强 Llama L13 因果 claim 可信度\n\n**一句话总结**：方法论控制设计出色的跨语言 probing 研究，描述性发现扎实，但核心因果 claim 证据单薄且新颖性被 Basu et al. (2026) 部分消解。修改后适合 Findings 接收。\n\n---\n\n## Detailed Comments（逐节）\n\n**Abstract**: 约 164 words，符合 ≤200 要求。\"these findings indicate that linear detectability does not imply causal relevance\" 措辞需降级——这仅在 Llama 观察到，不构成三模型的一般性结论。\n\n**Introduction**: Figure 1 有效传达核心问题。三个 RQ 设置清晰。但 Contributions 4→3 是否更诚实（将 C2 并入 C1）值得考虑。\n\n**Related Work**: 覆盖充分（Zhao/Basu/Hewitt/Belinkov/Li/Turner/Marks/Pokharel/Sundar/Gurgurov 均已引用）。Basu et al. 差异化可更突出。跨语言 knowledge editing 方向可选择性引用 1 篇。\n\n**Method**: 清晰规范。COMET back-translation 验证、selectivity control、random direction control 设计得当。Bonferroni 阈值说明清楚。\n\n**Experiments 4.1-4.2**: 检测结果扎实，三模型一致。\n\n**Experiments 4.3-4.4**: Asymmetry + XNLI baseline 是论文亮点，但需修正统计措辞（Qwen 不显著、报告校正后结果）。\n\n**Experiments 4.5**: COMET tercile 作为辅助证据可保留，但需明确标注功效限制 + 对 Gemma 趋势做进一步分析。\n\n**Experiments 4.6**: Steering 是论文核心贡献所在，Llama L13 证据（含 seed replication）可信。但跨模型 null result 的解释需更审慎。\n\n**Discussion**: 三个假说框架合理，但未验证任何一个。重新定位为开放问题而非论文贡献。\n\n**Conclusion**: 存在但过于简短（2 句）。核心 takeaway 的措辞需与 Weaknesses 修改同步调整。\n\n**Limitations**: 诚实且覆盖主要局限。CV 承诺 + Qwen dual role + steering 方法局限均已提及。\n\n**Appendix**: Boundary replication (N=201)、seed replication、AUROC、matched-condition 均有价值。\n\n---\n\n## 格式合规\n\n| 检查项 | 结果 |\n|--------|------|\n| 正文 ≤ 8 页 | ✓ |\n| Limitations 存在且位置正确 | ✓ (p.9, 正文后) |\n| Abstract ≤ 200 words | ✓ (~164 words) |\n| Double-blind 匿名化 | ✓ |\n| ACL 模板 | ✓ (\\usepackage[review]{acl}) |\n| 代码可用性声明 | ✓ (anonymous.4open.science) |\n| AI 使用声明 | ✓ (Appendix A) |\n\n---\n\n## Issue Tracker 更新摘要\n\n- **Round 3 resolved in R4**: R3-N1 (Mirror→Consistent With), R3-W3 (selectivity), R3-W4 (AUROC), R3-W5 (α justification), R3-M1 (COMET version), R3-M2 (Jaccard floor), R3-M4 (random control), R3-M5 (Figure 3 band)\n- **Round 3 still open in R4**: R3-N2 (COMET power), R3-N3/R1-N2 (detection≠decision), R3-W1 (single split), R3-W2 (Qwen dual role), R3-W6 (hypotheses untested), R3-NOV (Basu novelty)\n- **New in R4**: R4-N1 (Qwen CI zero + Bonferroni), R4-W1 (FWER), R4-W2 (EN-only steering), R4-W3 (TOST), R4-W4 (contribution weight), R4-I1 (Fisher paired)\n",
  "project": "clkc_mech_interp",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 4 审稿报告 — clkc_mech_interp\n\n**Target Venue**: EMNLP 2026 (via ARR) | **Deadline**: 2026-06-15\n**Paper**: \"English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries\"\n**Reviewers**: R1 (方法严谨性) + R2 (新颖性/完整性) | **Cross-sharing**: 完成\n\n---\n\n## Summary\n\n本文将知识冲突信号的 probing 分析从单语扩展到英-中跨语言设置，在三个 LLM（Llama-3.1-8B-Instruct、Qwen3-8B、Gemma-2-9B-IT）上训练残差流探针、构建 XNLI 非冲突基线、执行 COMET/token overlap/EN-DE 混淆排除、并进行因果 steering 实验。主要发现：(1) 冲突信号在所有模型和方向上线性可检测；(2) ZH→EN ~7pp 迁移优势与 XNLI 一致，反映一般跨语言结构；(3) 仅 Llama L13 (41% depth) steering 成功，Qwen/Gemma 无效，据此提出 detection≠decision dissociation。\n\n---\n\n## Strengths\n\n1. **混淆因素控制设计出色**：COMET 翻译质量分层 + XNLI 非冲突基线 + EN-DE 类型学控制的三层设计是可复用的方法论贡献。EN-DE Jaccard 14.8% vs EN-ZH 3.8% 但 Δ≈0 有效排除 token overlap。[R1-S2/S3, R2-S1]\n2. **多模型验证**：三个架构差异显著的模型仅 3.5% 问题重叠，构成近似独立复制。方向一致性 binomial p = 0.016。[R1-S1, R2-S2]\n3. **统计方法规范**：Bootstrap CI (n=2000)、Bonferroni 校正、Fisher 精确检验、selectivity control (gap 21-40pp)、matched-condition 控制均达标。[R1-S4/S5, R2-S3]\n4. **诚实报告负面结果**：Qwen/Gemma steering 失败、asymmetry 非冲突特异性的如实报告优于领域平均水平。[R2-S4]\n5. **Seed replication**：独立 seed 复现 Llama L13 因果效应 (N=201)，排除单次 split 偶然性。[R2-S5]\n6. **代码可用 + AI 使用声明透明**：匿名代码仓库提供，AI 辅助使用明确标注。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**[C1] Detection ≠ Decision 核心 claim 过度概括（R1-W1, R2-N1; 双方 AGREE）**\n- 正面因果证据仅来自 Llama L13 一层。Qwen (L14) 和 Gemma (L17) 各仅测 1 层即宣告 null，但 Llama 自身因果窗口仅 ~4 层 (L13-L16)，遗漏相邻层完全可能。\n- 替代解释未排除：非线性因果通路、不同因果窗口位置、样本量功效不足 (n=131/171)、线性 steering 方法本身的局限性。\n- Basu et al. (2026) \"Interpretability without actionability\" 已在单语中建立 detection-steering dissociation。本文差异化论述仅 Section 5 一句话，过于单薄。\n- **Action required**: (1) Qwen/Gemma 补充至少 3 层相邻层 steering；(2) 若无法执行，将 claim 严格限定为 Llama-specific observation；(3) 增加与 Basu et al. 的逐点差异化段落。\n\n**[C2] Asymmetry \"consistent across all three models\" 统计不充分（R1-W2; R2 交叉 AGREE）**\n- Qwen Δ_asym = +7.2pp, CI [-0.6, 13.7] 跨越零，α=0.05 下不显著。\n- 三模型 Bonferroni 校正（阈值 0.017）：Llama p=0.038 不显著、Gemma p=0.006 显著、Qwen n.s.——仅 1/3 模型通过校正。\n- Section 4.3 \"consistent in direction across all three architectures\" 措辞超越了证据能支撑的范围。\n- **Action required**: (1) 明确报告 Qwen 不显著；(2) 报告 Bonferroni 校正后结果；(3) 主要论据改为方向一致性 binomial test (p=0.016) + XNLI 六点复制。\n\n**[C3] COMET tercile 混淆排除欠功效，Gemma 趋势未解释（R1-W3; R2 部分 AGREE）**\n- MDE = 25.3pp at 80% power，对中等效应完全不敏感。\n- Gemma Δ = +10.3pp 在混淆方向，p=0.278 在低功效下不排除实质效应。\n- 多层控制（XNLI + EN-DE）部分缓解，但 COMET 分析作为独立证据线本质无效。\n- **Action required**: 增加连续回归 (COMET score vs probe accuracy) 替代 tercile；对 Gemma 趋势深入调查。\n\n### Warning（影响评分）\n\n**[W1] 单一 train/test split 贯穿全文（R1-W5, R2-W2; 双方 AGREE）**\n- Bootstrap CI 仅捕获 split 内变异。Δ_asym arithmetic diff (11.0pp) vs bootstrap mean (7.3pp) 差距 3.7pp 暗示 peak layer 不稳定。\n- **Action**: 当前版本完成至少 3-fold CV 主要结果。\n\n**[W2] TOST 等价检验功效 1.4%，uninformative（R1-W4; R2 AGREE）**\n- ±2pp 边界对 n~200、SE~5-8pp 注定失败。报告无信息量检验有空洞分析之嫌。\n- **Action**: 删除 TOST 或用合理边界 (±5pp) 重做。\n\n**[W3] Steering 仅英文数据，未测试跨语言因果干预（R1-W8; R2 AGREE）**\n- 论文主题是跨语言冲突，但因果实验仅用英文侧。缺少 ZH 输入 steering 和 cross-lingual steering。\n- **Action**: 至少在 Llama L13 测试中文输入 steering。\n\n**[W4] 全文多重假设检验缺乏整体 FWER 控制（R1-W7; R2 部分 AGREE）**\n- ~100+ 检验仅 steering per-layer Bonferroni。Asymmetry 三模型属同一族未校正。\n- **Action**: 对 asymmetry 做 Bonferroni/Holm 校正并报告。\n\n**[W5] Qwen3-8B 同时作为翻译模型和实验对象（R1-W6; 分歧）**\n- R2 反驳称不同代际（Qwen3 vs Qwen2.5），但论文 Section 3.2 和 4.1 均为 Qwen3-8B——R2 事实判断有误，R1 担忧成立。\n- Llama/Gemma 独立验证相同 pattern 部分缓解。\n- **Action**: 正文更显著标注；或用独立翻译模型验证。\n\n**[W6] 贡献权重不均衡 / C2 定位争议（R2-W1/N3 vs R1 REBUT; 分歧）**\n- R2 认为 C2 (asymmetry = general structure) 是 null result 包装为贡献；R1 反驳 ruling-out 有方法论价值。\n- **共识**：不论定位，当前统计证据 (Qwen CI 含零、TOST 无效) 不足以支撑 claim 的强度。\n- **Action**: 降低措辞强度或并入 C1。\n\n**[W7] 机制深度偏浅（R2-W4; R1 部分 AGREE）**\n- Logistic regression probing + linear steering 在 mechanistic interpretability 谱系中属浅层。Discussion 列三个假说均未验证。\n- **Action**: 重新定位为 empirical probing study 或补充 activation patching。\n\n### Info\n\n**[I1] Fisher's exact test 用于 paired steering data（R1-W9; R2 AGREE）**\n- Steering vs random control 是 paired design，McNemar's test 更合适。对 L13 (p=0.002) 不改变结论，但应在修改稿中统一。\n\n---\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 状态 |\n|------|----|----|------|\n| Detection≠decision 过度概括 | W1 [critical] | N1 [critical] | **[AGREE]** |\n| Qwen CI 含零 / Bonferroni 后仅 Gemma 显著 | W2 [critical] | 交叉 AGREE | **[AGREE]** |\n| COMET tercile 欠功效 | W3 [critical] | 部分 AGREE（多层设计部分缓解）| **[AGREE-partial]** |\n| 单 split 无 CV | W5 [warning] | W2 [warning] | **[AGREE]** |\n| TOST 1.4% uninformative | W4 [warning] | AGREE | **[AGREE]** |\n| Steering 仅英文 | W8 [warning] | AGREE | **[AGREE]** |\n| Global FWER | W7 [warning] | 部分 AGREE | **[AGREE-partial]** |\n| Fisher on paired data | W9 [info] | AGREE | **[AGREE]** |\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 分歧本质 |\n|------|----|----|----------|\n| 标题 \"General\" overclaim | REBUT（标题说 \"Consistent With\" 无问题）| N2 [critical] | 语义解读差异；R1 认为标题准确，R2 认为实验覆盖不足 |\n| C2 是否为 null result | REBUT（ruling-out 有价值）| N3 [critical] | 方法论哲学差异；共识是证据力度不足 |\n| Qwen 翻译模型双重角色 | W6 [warning] | REBUT（不同代际）| R2 事实判断有误（论文确为同一模型 Qwen3-8B）|\n| 跨语言知识编辑文献 | REBUT（不同方向）| W5 [warning] | 相关性判断差异；R1 认为 editing ≠ probing/steering |\n\n---\n\n## Questions to Authors（汇总，去重后 10 条）\n\n1. Basu et al. (2026) 已建立单语 detection-steering dissociation。本文跨语言设定具体揭示了哪些单语无法观察到的现象？\n2. Qwen/Gemma 是否测试了目标层 ±2 层范围？如果 Llama 因果窗口仅 4 层宽，仅测 1 层的 null 能否排除存在因果位点？\n3. Qwen Δ_asym CI [-0.6, 13.7] 包含零。三模型 Bonferroni 校正后仅 Gemma 显著。如何维护 \"consistent\" 论断？\n4. Table 1 Δ_asym (bootstrap mean 7.3pp) 与算术差 (11.0pp) 差距 3.7pp 的来源？是否暗示 peak layer 在 bootstrap 样本间偏移？\n5. Gemma COMET tercile Δ=+10.3pp 在混淆方向——能否提供 COMET score 与 probe accuracy 的连续回归结果？\n6. EN-DE 已翻译完成（Section 3.5）——为何不做完整四方向探测实验以直接支持泛化 claim？\n7. Steering 为何仅在英文数据评估？中文输入 + ZH→EN probe steering 的结果？\n8. 如果选择 ±5pp 等价边界重做 TOST，预计结论是否改变？\n9. 论文称 Gemma ConflictQA 保留 1590 样本，但 probe accuracy 最高 (88.9% at L17)。保留率最高+准确率最高是否暗示 probe 捕获了 task-irrelevant 信号？\n10. All-position injection 与 last-token injection 在 L13 产生 \"identical results\"——具体数字？\n\n---\n\n## Missing References\n\n**R2 建议（R1 部分反驳）**：\n- \"Editing Across Languages: A Survey of Multilingual Knowledge Editing\" (2025)\n- CLM-Bench (2026)\n- BMIKE-53 (53-language knowledge editing benchmark)\n\nR1 认为 knowledge editing (参数修改) 与 probing/steering (推理时干预) 方法论不同，8 页限制下引用需选择性。建议选择性引用最相关的 1 篇。\n\n---\n\n## External Review\n\n**状态**: 未配置（项目未启用 paperreview.ai）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成 | 0 critical, 0 warning, 3 info\n\n排版质量良好，仅有三个建议性意见：\n1. **Page 6**: 单页堆叠 3 个 display items (Figure 3 + Table 1 + Figure 4)，每个尺寸偏小，Figure 3 axis label 和 legend 字号接近可读下限\n2. **Page 12**: 末页 appendix 底部约 35% 空白\n3. **Page 5**: 纯文本高密度页（Experimental Setup），可考虑将部分细节移至 appendix\n\n---\n\n## Overall Assessment\n\n### 评分: 3.0 — Findings\n\n**R1**: 3.0 (Findings) | Confidence 4/5\n**R2**: 3.0 (Findings) | Confidence 4/5\n**Director 综合**: **3.0 (Findings)**\n\n### 评分理由\n\n**为什么不是 3.5 (Borderline Conference)**：\n- 核心因果贡献 (detection≠decision) 仅 1/3 模型 1/32 层支持，替代解释未排除\n- 与 Basu et al. (2026) 差异化不清晰——核心 insight 已被单语工作建立\n- Asymmetry \"consistency\" 统计不充分（Bonferroni 后仅 1/3 模型显著）\n- 四个贡献中两个薄弱（C2 统计不足、C3 证据单薄）\n\n**为什么不是 2.5 (Borderline Findings)**：\n- 混淆因素控制设计 (XNLI + EN-DE + COMET) 是真正可复用的方法论贡献\n- 三模型 × 两任务方向一致性 (binomial p=0.016) 提供跨架构描述性证据\n- 统计方法总体规范（bootstrap、Bonferroni、selectivity control）\n- 诚实报告负面结果 + 代码公开\n- Seed replication 增强 Llama L13 因果 claim 可信度\n\n**一句话总结**：方法论控制设计出色的跨语言 probing 研究，描述性发现扎实，但核心因果 claim 证据单薄且新颖性被 Basu et al. (2026) 部分消解。修改后适合 Findings 接收。\n\n---\n\n## Detailed Comments（逐节）\n\n**Abstract**: 约 164 words，符合 ≤200 要求。\"these findings indicate that linear detectability does not imply causal relevance\" 措辞需降级——这仅在 Llama 观察到，不构成三模型的一般性结论。\n\n**Introduction**: Figure 1 有效传达核心问题。三个 RQ 设置清晰。但 Contributions 4→3 是否更诚实（将 C2 并入 C1）值得考虑。\n\n**Related Work**: 覆盖充分（Zhao/Basu/Hewitt/Belinkov/Li/Turner/Marks/Pokharel/Sundar/Gurgurov 均已引用）。Basu et al. 差异化可更突出。跨语言 knowledge editing 方向可选择性引用 1 篇。\n\n**Method**: 清晰规范。COMET back-translation 验证、selectivity control、random direction control 设计得当。Bonferroni 阈值说明清楚。\n\n**Experiments 4.1-4.2**: 检测结果扎实，三模型一致。\n\n**Experiments 4.3-4.4**: Asymmetry + XNLI baseline 是论文亮点，但需修正统计措辞（Qwen 不显著、报告校正后结果）。\n\n**Experiments 4.5**: COMET tercile 作为辅助证据可保留，但需明确标注功效限制 + 对 Gemma 趋势做进一步分析。\n\n**Experiments 4.6**: Steering 是论文核心贡献所在，Llama L13 证据（含 seed replication）可信。但跨模型 null result 的解释需更审慎。\n\n**Discussion**: 三个假说框架合理，但未验证任何一个。重新定位为开放问题而非论文贡献。\n\n**Conclusion**: 存在但过于简短（2 句）。核心 takeaway 的措辞需与 Weaknesses 修改同步调整。\n\n**Limitations**: 诚实且覆盖主要局限。CV 承诺 + Qwen dual role + steering 方法局限均已提及。\n\n**Appendix**: Boundary replication (N=201)、seed replication、AUROC、matched-condition 均有价值。\n\n---\n\n## 格式合规\n\n| 检查项 | 结果 |\n|--------|------|\n| 正文 ≤ 8 页 | ✓ |\n| Limitations 存在且位置正确 | ✓ (p.9, 正文后) |\n| Abstract ≤ 200 words | ✓ (~164 words) |\n| Double-blind 匿名化 | ✓ |\n| ACL 模板 | ✓ (\\usepackage[review]{acl}) |\n| 代码可用性声明 | ✓ (anonymous.4open.science) |\n| AI 使用声明 | ✓ (Appendix A) |\n\n---\n\n## Issue Tracker 更新摘要\n\n- **Round 3 resolved in R4**: R3-N1 (Mirror→Consistent With), R3-W3 (selectivity), R3-W4 (AUROC), R3-W5 (α justification), R3-M1 (COMET version), R3-M2 (Jaccard floor), R3-M4 (random control), R3-M5 (Figure 3 band)\n- **Round 3 still open in R4**: R3-N2 (COMET power), R3-N3/R1-N2 (detection≠decision), R3-W1 (single split), R3-W2 (Qwen dual role), R3-W6 (hypotheses untested), R3-NOV (Basu novelty)\n- **New in R4**: R4-N1 (Qwen CI zero + Bonferroni), R4-W1 (FWER), R4-W2 (EN-only steering), R4-W3 (TOST), R4-W4 (contribution weight), R4-I1 (Fisher paired)\n",
    "project": "clkc_mech_interp",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "review_chat_id": "oc_8b9aa92fafaf69b48d2c44b41c2fe9d9"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-25T21:33:16.815166+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6951eb3869a0070e3ae607ab60c90dad:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4165
}
```

</details>

---


### Assistant

_source line 426 · 2026-05-25T21:33:27.933007+00:00_

---

**Round 4 审稿完成。**

报告已投递 Research Director。核心结论：

**Overall: 3.0 (Findings)**

两位 Reviewer 一致判断，3 个 critical 问题阻止主会议接收：
1. **Detection≠decision claim 过度概括**——正面证据仅 Llama L13，Qwen/Gemma 各测 1 层的 null 不充分，且 Basu et al. 2026 已在单语中建立
2. **Asymmetry "consistent" 统计不充分**——Bonferroni 校正后仅 Gemma (1/3) 显著
3. **COMET tercile 欠功效** (MDE=25.3pp)——Gemma +10.3pp 混淆方向趋势未排除

论文的描述性发现和控制设计（XNLI + EN-DE + selectivity control）扎实，修改后适合 Findings 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---


## Round 31

## Round 31

2 recorded events


### User

_source line 427 · 2026-05-25T21:33:29.438835+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。核心判断：

- **N1**（detection ≠ decision 证据不足）：[AGREE]，与我的 W1 完全一致
- **N2**（标题泛化性）：[REBUT]，"general" 修饰 asymmetry 性质而非语言覆盖
- **N3**（null result 包装为贡献）：[REBUT]，ruling out conflict-specificity 有实质意义，但统计证据偏弱
- **W1-W4**：基本 AGREE
- **W5**（缺 references）：[REBUT]，knowledge editing ≠ probing/steering
- **W6**（缺 Conclusion）：[REBUT]，Section 6 Conclusion 存在，R2 事实判断有误

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 428 · 2026-05-25T21:33:41.637398+00:00_

审稿报告已于上一轮投递至 Research Director。本轮圆桌审稿完成。

**Round 4 审稿结论摘要：**

- **Overall: 3.0 (Findings)**，R1 和 R2 一致
- **3 个 Critical 共识**：(1) detection≠decision 仅 Llama L13 支持，过度概括；(2) asymmetry "consistent" 论断 Bonferroni 后仅 Gemma 显著；(3) COMET tercile MDE=25.3pp 无法有效排除混淆
- **7 个 Warning**：单 split 无 CV、TOST 无效、steering 仅英文、FWER 未控制、Qwen 双重角色、贡献权重、机制深度
- **分歧（已记录）**：标题 "General" 语义（R1 认为无问题/R2 认为实验不足）、C2 定位（ruling-out 价值 vs null result）
- **R3 已解决 8 项**：Mirror→Consistent With、selectivity control、AUROC、α justification、COMET 版本等
- **Issue Tracker 已更新**，报告已投递

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director"
}
```

</details>

---
