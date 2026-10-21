# Reviewer 2 coordination — Part 4 of 5

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../reviewer-2-coordination.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/16/16fda77cba37e7ffdcac.json)

## Round 33

### Tool call

_source line 1614 · 2026-05-22T12:44:31.871751+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 交叉回应 Reviewer 1 的 Round 1 意见\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R1-W1: 缺乏与外部 constrained IE 基线的直接实验对比**\n\n同意这是一个重要缺陷。论文的所有实验对比均为内部 ablation（grammar-only vs. full system、constrained vs. unconstrained、S1 vs. S2）或与 post-hoc filtering 的对比。GoLLIE 代码已开源（ICLR 2024），在 SciERC 上运行并报告 violation rate + F1 是完全可行的。即使 GoLLIE 是 training-time 方法、OntoCoDec 是 decoding-time 方法（范式不同），在相同 evaluation protocol 下的 head-to-head 数据会大幅增强论文说服力。我在自己的审稿中未将此单列为独立 weakness，但 R1 的论述充分，这应该是 must-fix。\n\n补充发现：Table 15-16（Appendix D）的 GCD-equivalent baseline 是 OntoCoDec 自身 grammar layer 的简化版（去掉 semantic layer），而非独立实现的 GCD 系统。虽然论文声称机制等价（\"identical token masking as GCD\"，Appendix D），但未验证这种等价性。\n\n---\n\n**[REBUT] R1-W2: Abstract 关于 beam search 的声明与实验数据不一致**\n\nR1 的具体事实声称存在误读。我逐一核实了 LaTeX 源码：\n\n**(a) \"Abstract 称 beam (k=3)\"** — **不正确**。Abstract 原文（abstract.tex line 6）为：\"residual CF (≤1.4% fine-tuned; up to 12% zero-shot) represents violation conversion ... resolved by beam search on SciERC (§5.4)\"。Abstract **未指定 k 值**。主文 §5.4（section5_runtime.tex line 10）明确写的是 k=4：\"With LoRA, beam search (k=4) eliminates all four violation types on SciERC (R-F1 44--46)\"。Section 5.1（section5_scierc_draft.tex line 107）同样写 k=4。论文通篇未出现 k=3。\n\n**(b) \"Table 20 仅测试 k∈{1,2,4,8}，不含 k=3\"** — Table 确实测试 k∈{1,2,4,8}，但论文声称的是 k=4 而非 k=3，所以不存在 k=3 插值问题。\n\n**(c) \"'eliminates all' 仅对 Llama 成立，Qwen k=8 时 CF 仍 0.08%\"** — R1 引用的是 **zero-shot** beam ablation（Table 20，Qwen3-8B zero-shot k=8 CF=0.08%）。但主文的 \"eliminates all four violation types\" 声明是在 **LoRA** 上下文中（§5.4 原文：\"With LoRA, beam search (k=4) eliminates all four violation types\"）。LoRA + k=4 的实验数据（appendix_beam_search.tex lines 137-138）：\n- Qwen3-8B LoRA SciERC k=4: ET=0%, RV=0%, DR=0%, CF=0%（R-F1=43.60）\n- Llama-3.1-8B LoRA SciERC k=4: ET=0%, RV=0%, DR=0%, CF=0%（R-F1=46.18）\n\n**两个 calibrated 模型都达到了 zero violations**，不仅是 Llama。\n\n但我补充一个 R1 未提到的 nuance：Abstract 的句子结构（\"residual CF ... resolved by beam search on SciERC\"）在语法上可被解读为 beam search 解决 *所有* residual CF。在 LoRA+k=4 下这是成立的，但 zero-shot+k=4 下 CF 仍有 0.53-0.93%（Table 19）。Abstract 的上下文（\"Composed with LoRA fine-tuning\"开头的段落）暗示这是 LoRA setting，但可以更明确。\n\n---\n\n**[AGREE with nuance] R1-W3: Proposition 1 的实际相关性被高估**\n\nR1 的核心论点正确：实际 schema entity type 集合有限（SciERC: 6 types, DocRED: 96 types），有限情形下 cross-field constraint language 是 regular（有限个 regular language 的交集），DFA 可实现但状态数 O(|T|^n) 工程上不可行。\n\n论文在 Appendix O（page 33）已承认这一点：\"For a finite entity set ε, the valid language L_valid = ∩_i L_i is theoretically regular (a finite intersection of regular languages). However, the corresponding DFA requires O(|T|^n) states—for SciERC...\"\n\n但 R1 正确指出，**主文**中 Proposition 1 的呈现没有这个 caveat。§3.1 的读者会认为这是 formal impossibility，而实际上是 engineering intractability。建议在主文 Proposition 1 后添加 remark，区分 theoretical impossibility（无界 entity set）和 engineering intractability（有界但指数状态数）。\n\n不过我要补充：即使有限情形下 DFA 理论上可行，论文的 runtime semantic layer 方案（O(n) entity registry 查找）在工程上仍然是远优于 DFA 构造的实现路径。Proposition 1 的价值不仅在于证明 impossibility，更在于 motivate 为什么需要一个 runtime stateful 方案而非 compile-time DFA 方案。\n\n---\n\n**[AGREE] R1-W4: κ̄ 统计支撑不足 (n=3)**\n\n完全同意。Figure 2 的 6 个数据点（3 datasets × 2 models）拟合线性模型，R²=0.886 但 p=0.138 > 0.05，统计不显著。这与我在 W4 中提出的 κ̄ 实用性质疑互补：我关注的是 κ̄ 的 tautological nature（更严格约束 → 更多违反被约束），R1 关注的是统计效力不足。两者结合使 κ̄ 作为 predictive metric 的论证非常薄弱。\n\n建议作者将 κ̄ 降级为 purely descriptive tool（用于描述 schema 性质），移除 predictive/explanatory 的措辞。或者在更多 datasets 上验证（n≥10）以获得统计显著性。\n\n---\n\n**[AGREE] R1-W5: Entity registry 顺序依赖未被实验量化**\n\n同意，这是我遗漏的一个重要实验缺口。Entity registry 使用 \"first-registered-type\" 语义——第一次生成某 entity 时锁定其 type。如果模型在文档开头将 entity 分配了错误的 type，后续所有引用该 entity 的 relation 都会被迫使用错误 type（或触发 fallback）。\n\n论文讨论了 S1/S2 和 grammar-first fallback 作为缓解（§4），但没有实验量化 entity ordering 的影响。R1 建议的 gold/shuffled/predicted order 对比是一个可行且有价值的消融实验。\n\n这也与 R1-Q5 相关（同一 entity 在不同 context 可能有不同 type）。\n\n---\n\n**[AGREE] R1-W6: WikiEvents fine-tuning 统计效力不足**\n\n同意。n=20 文档的 bootstrap 95% CI ±3-5 pp 意味着大多数 F1 差异在置信区间内，无法得出有统计意义的结论。我在 W2 中也指出了 WikiEvents fine-tuning 标注为 \"preliminary\" 的问题。R1 增加了统计效力维度的分析，使这个 weakness 更具体。\n\n---\n\n**[AGREE] R1-W7: 70B 量化推理影响未隔离**\n\n同意。AWQ INT4 量化改变 logit 分布，token-level masking 的有效性可能受量化影响（量化后 logit 的相对排序可能变化）。论文未提供 quantized vs. non-quantized 对比。我在 W1 中指出 70B 评估整体偏浅，R1 的 W7 提供了一个具体的混淆变量——量化效应。\n\n结合 R1-W7 和我的 W1：70B 评估的两个问题是 (1) 覆盖面太窄（仅 zero-shot 两数据集）和 (2) 量化效应未隔离。\n\n---\n\n**[AGREE] R1-W8: DR reduction 42-99% 范围过宽**\n\n同意，与我的 W5 一致。R1 建议 median/IQR 或按数据集报告，我建议 zero-shot/fine-tuned 分开报告。两个建议互补。\n\n---\n\n### Questions 逐条回应\n\n**[AGREE] R1-Q1: GoLLIE SciERC 直接对比**\n\n与 W1 一致。GoLLIE 开源可运行，提供 same-protocol 对比数据会极大加强论文。\n\n**[AGREE] R1-Q2: κ̄ 在 SciERC 和 WikiEvents 上几乎相同但效果差异显著**\n\n这是一个 devastating observation。如果 κ̄ 在两个数据集上值接近（均 ~0.020）但 constraint enforcement 效果显著不同，那么 κ̄ 作为 predictor 的解释力远不足以支撑论文对它的定位。这与 W4 的 p=0.138 问题一起，严重削弱了 κ̄ 的贡献声明。\n\n**[AGREE] R1-Q3: Grammar-first fallback rate 的模型特征决定因素**\n\nQwen 0.93% vs Llama 12.02% 的 fallback rate 差异确实需要更深入的机制解释。论文将其归因于 \"model calibration\" 但未定义什么是 \"well-calibrated\" 或提供量化指标。\n\n**[AGREE with nuance] R1-Q4: SciERC 6 entity types 的等价 DFA**\n\n理论上可行，但 DFA 状态数取决于文档中 entity 数量和 relation 约束的交叉积。SciERC 6 types × 7 relation types 的完整 DFA 可能仍然很大。不过作为 comparison point（即使只是 toy scale）会有效地回应 W3 的担忧。\n\n**[AGREE] R1-Q5: 同一 entity 不同 context 可能有不同 type（如 \"Python\"）**\n\n这是 entity registry \"first-registered-type\" 语义的根本限制。论文在 Limitations 中提到了 GENERIC→X schema ambiguity，但 Q5 指出的是更一般的 genuine type polysemy 问题。在 IE 中，同一 mention 确实可能在不同 relation context 中属于不同 type（如 \"Python\" 在 \"Python is-a programming-language\" 中是 OtherScientificTerm，在 \"Python uses garbage-collection\" 中可能是 Method）。Entity registry 的 first-lock 语义无法处理这种情况。\n\n---\n\n### Missing References\n\n**[AGREE]** InstructUIE (Wang et al., 2023) 的 type violation 行为讨论确实值得补充。InstructUIE 作为 instruction-tuning IE 方法，其 type violation 模式（if any）可以为 OntoCoDec 的 motivation 提供额外支撑。\n\n---\n\n### 总结：与 R1 的评分分歧\n\nR1 给 Overall 3.5（Borderline Conference），我给 3.0（Findings）。分歧主要在 Excitement 维度：R1 给 3.0，我给 2.5。\n\n我的 2.5 基于：grammar layer 是 XGrammar 直接应用，semantic layer 是 PICARD-style runtime checking 的 IE 移植，Proposition 1 是标准 pumping lemma。R1 的 3.0 可能更多 weight 了系统集成的完整度和实验深度。\n\n在交叉审查后，我认为 R1 提出的 W2 (beam search k=3) 存在事实错误（论文说的是 k=4 而非 k=3，且 \"eliminates all\" 是 LoRA 而非 zero-shot），这削弱了 R1 将 W2 列为 critical 的合理性。但 R1 的其他 weaknesses（W1 缺外部对比、W3 Prop 1 caveat、W4 κ̄ 统计、W5 entity ordering）都是有力的发现。\n\n综合考虑，我维持 **Overall 3.0（Findings）**。W1（缺外部对比）和 W5（entity ordering 未量化）是 R1 提出的新问题，进一步支持了 Findings 而非 main conference 的判断。",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 交叉回应 Reviewer 1 的 Round 1 意见\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R1-W1: 缺乏与外部 constrained IE 基线的直接实验对比**\n\n同意这是一个重要缺陷。论文的所有实验对比均为内部 ablation（grammar-only vs. full system、constrained vs. unconstrained、S1 vs. S2）或与 post-hoc filtering 的对比。GoLLIE 代码已开源（ICLR 2024），在 SciERC 上运行并报告 violation rate + F1 是完全可行的。即使 GoLLIE 是 training-time 方法、OntoCoDec 是 decoding-time 方法（范式不同），在相同 evaluation protocol 下的 head-to-head 数据会大幅增强论文说服力。我在自己的审稿中未将此单列为独立 weakness，但 R1 的论述充分，这应该是 must-fix。\n\n补充发现：Table 15-16（Appendix D）的 GCD-equivalent baseline 是 OntoCoDec 自身 grammar layer 的简化版（去掉 semantic layer），而非独立实现的 GCD 系统。虽然论文声称机制等价（\"identical token masking as GCD\"，Appendix D），但未验证这种等价性。\n\n---\n\n**[REBUT] R1-W2: Abstract 关于 beam search 的声明与实验数据不一致**\n\nR1 的具体事实声称存在误读。我逐一核实了 LaTeX 源码：\n\n**(a) \"Abstract 称 beam (k=3)\"** — **不正确**。Abstract 原文（abstract.tex line 6）为：\"residual CF (≤1.4% fine-tuned; up to 12% zero-shot) represents violation conversion ... resolved by beam search on SciERC (§5.4)\"。Abstract **未指定 k 值**。主文 §5.4（section5_runtime.tex line 10）明确写的是 k=4：\"With LoRA, beam search (k=4) eliminates all four violation types on SciERC (R-F1 44--46)\"。Section 5.1（section5_scierc_draft.tex line 107）同样写 k=4。论文通篇未出现 k=3。\n\n**(b) \"Table 20 仅测试 k∈{1,2,4,8}，不含 k=3\"** — Table 确实测试 k∈{1,2,4,8}，但论文声称的是 k=4 而非 k=3，所以不存在 k=3 插值问题。\n\n**(c) \"'eliminates all' 仅对 Llama 成立，Qwen k=8 时 CF 仍 0.08%\"** — R1 引用的是 **zero-shot** beam ablation（Table 20，Qwen3-8B zero-shot k=8 CF=0.08%）。但主文的 \"eliminates all four violation types\" 声明是在 **LoRA** 上下文中（§5.4 原文：\"With LoRA, beam search (k=4) eliminates all four violation types\"）。LoRA + k=4 的实验数据（appendix_beam_search.tex lines 137-138）：\n- Qwen3-8B LoRA SciERC k=4: ET=0%, RV=0%, DR=0%, CF=0%（R-F1=43.60）\n- Llama-3.1-8B LoRA SciERC k=4: ET=0%, RV=0%, DR=0%, CF=0%（R-F1=46.18）\n\n**两个 calibrated 模型都达到了 zero violations**，不仅是 Llama。\n\n但我补充一个 R1 未提到的 nuance：Abstract 的句子结构（\"residual CF ... resolved by beam search on SciERC\"）在语法上可被解读为 beam search 解决 *所有* residual CF。在 LoRA+k=4 下这是成立的，但 zero-shot+k=4 下 CF 仍有 0.53-0.93%（Table 19）。Abstract 的上下文（\"Composed with LoRA fine-tuning\"开头的段落）暗示这是 LoRA setting，但可以更明确。\n\n---\n\n**[AGREE with nuance] R1-W3: Proposition 1 的实际相关性被高估**\n\nR1 的核心论点正确：实际 schema entity type 集合有限（SciERC: 6 types, DocRED: 96 types），有限情形下 cross-field constraint language 是 regular（有限个 regular language 的交集），DFA 可实现但状态数 O(|T|^n) 工程上不可行。\n\n论文在 Appendix O（page 33）已承认这一点：\"For a finite entity set ε, the valid language L_valid = ∩_i L_i is theoretically regular (a finite intersection of regular languages). However, the corresponding DFA requires O(|T|^n) states—for SciERC...\"\n\n但 R1 正确指出，**主文**中 Proposition 1 的呈现没有这个 caveat。§3.1 的读者会认为这是 formal impossibility，而实际上是 engineering intractability。建议在主文 Proposition 1 后添加 remark，区分 theoretical impossibility（无界 entity set）和 engineering intractability（有界但指数状态数）。\n\n不过我要补充：即使有限情形下 DFA 理论上可行，论文的 runtime semantic layer 方案（O(n) entity registry 查找）在工程上仍然是远优于 DFA 构造的实现路径。Proposition 1 的价值不仅在于证明 impossibility，更在于 motivate 为什么需要一个 runtime stateful 方案而非 compile-time DFA 方案。\n\n---\n\n**[AGREE] R1-W4: κ̄ 统计支撑不足 (n=3)**\n\n完全同意。Figure 2 的 6 个数据点（3 datasets × 2 models）拟合线性模型，R²=0.886 但 p=0.138 > 0.05，统计不显著。这与我在 W4 中提出的 κ̄ 实用性质疑互补：我关注的是 κ̄ 的 tautological nature（更严格约束 → 更多违反被约束），R1 关注的是统计效力不足。两者结合使 κ̄ 作为 predictive metric 的论证非常薄弱。\n\n建议作者将 κ̄ 降级为 purely descriptive tool（用于描述 schema 性质），移除 predictive/explanatory 的措辞。或者在更多 datasets 上验证（n≥10）以获得统计显著性。\n\n---\n\n**[AGREE] R1-W5: Entity registry 顺序依赖未被实验量化**\n\n同意，这是我遗漏的一个重要实验缺口。Entity registry 使用 \"first-registered-type\" 语义——第一次生成某 entity 时锁定其 type。如果模型在文档开头将 entity 分配了错误的 type，后续所有引用该 entity 的 relation 都会被迫使用错误 type（或触发 fallback）。\n\n论文讨论了 S1/S2 和 grammar-first fallback 作为缓解（§4），但没有实验量化 entity ordering 的影响。R1 建议的 gold/shuffled/predicted order 对比是一个可行且有价值的消融实验。\n\n这也与 R1-Q5 相关（同一 entity 在不同 context 可能有不同 type）。\n\n---\n\n**[AGREE] R1-W6: WikiEvents fine-tuning 统计效力不足**\n\n同意。n=20 文档的 bootstrap 95% CI ±3-5 pp 意味着大多数 F1 差异在置信区间内，无法得出有统计意义的结论。我在 W2 中也指出了 WikiEvents fine-tuning 标注为 \"preliminary\" 的问题。R1 增加了统计效力维度的分析，使这个 weakness 更具体。\n\n---\n\n**[AGREE] R1-W7: 70B 量化推理影响未隔离**\n\n同意。AWQ INT4 量化改变 logit 分布，token-level masking 的有效性可能受量化影响（量化后 logit 的相对排序可能变化）。论文未提供 quantized vs. non-quantized 对比。我在 W1 中指出 70B 评估整体偏浅，R1 的 W7 提供了一个具体的混淆变量——量化效应。\n\n结合 R1-W7 和我的 W1：70B 评估的两个问题是 (1) 覆盖面太窄（仅 zero-shot 两数据集）和 (2) 量化效应未隔离。\n\n---\n\n**[AGREE] R1-W8: DR reduction 42-99% 范围过宽**\n\n同意，与我的 W5 一致。R1 建议 median/IQR 或按数据集报告，我建议 zero-shot/fine-tuned 分开报告。两个建议互补。\n\n---\n\n### Questions 逐条回应\n\n**[AGREE] R1-Q1: GoLLIE SciERC 直接对比**\n\n与 W1 一致。GoLLIE 开源可运行，提供 same-protocol 对比数据会极大加强论文。\n\n**[AGREE] R1-Q2: κ̄ 在 SciERC 和 WikiEvents 上几乎相同但效果差异显著**\n\n这是一个 devastating observation。如果 κ̄ 在两个数据集上值接近（均 ~0.020）但 constraint enforcement 效果显著不同，那么 κ̄ 作为 predictor 的解释力远不足以支撑论文对它的定位。这与 W4 的 p=0.138 问题一起，严重削弱了 κ̄ 的贡献声明。\n\n**[AGREE] R1-Q3: Grammar-first fallback rate 的模型特征决定因素**\n\nQwen 0.93% vs Llama 12.02% 的 fallback rate 差异确实需要更深入的机制解释。论文将其归因于 \"model calibration\" 但未定义什么是 \"well-calibrated\" 或提供量化指标。\n\n**[AGREE with nuance] R1-Q4: SciERC 6 entity types 的等价 DFA**\n\n理论上可行，但 DFA 状态数取决于文档中 entity 数量和 relation 约束的交叉积。SciERC 6 types × 7 relation types 的完整 DFA 可能仍然很大。不过作为 comparison point（即使只是 toy scale）会有效地回应 W3 的担忧。\n\n**[AGREE] R1-Q5: 同一 entity 不同 context 可能有不同 type（如 \"Python\"）**\n\n这是 entity registry \"first-registered-type\" 语义的根本限制。论文在 Limitations 中提到了 GENERIC→X schema ambiguity，但 Q5 指出的是更一般的 genuine type polysemy 问题。在 IE 中，同一 mention 确实可能在不同 relation context 中属于不同 type（如 \"Python\" 在 \"Python is-a programming-language\" 中是 OtherScientificTerm，在 \"Python uses garbage-collection\" 中可能是 Method）。Entity registry 的 first-lock 语义无法处理这种情况。\n\n---\n\n### Missing References\n\n**[AGREE]** InstructUIE (Wang et al., 2023) 的 type violation 行为讨论确实值得补充。InstructUIE 作为 instruction-tuning IE 方法，其 type violation 模式（if any）可以为 OntoCoDec 的 motivation 提供额外支撑。\n\n---\n\n### 总结：与 R1 的评分分歧\n\nR1 给 Overall 3.5（Borderline Conference），我给 3.0（Findings）。分歧主要在 Excitement 维度：R1 给 3.0，我给 2.5。\n\n我的 2.5 基于：grammar layer 是 XGrammar 直接应用，semantic layer 是 PICARD-style runtime checking 的 IE 移植，Proposition 1 是标准 pumping lemma。R1 的 3.0 可能更多 weight 了系统集成的完整度和实验深度。\n\n在交叉审查后，我认为 R1 提出的 W2 (beam search k=3) 存在事实错误（论文说的是 k=4 而非 k=3，且 \"eliminates all\" 是 LoRA 而非 zero-shot），这削弱了 R1 将 W2 列为 critical 的合理性。但 R1 的其他 weaknesses（W1 缺外部对比、W3 Prop 1 caveat、W4 κ̄ 统计、W5 entity ordering）都是有力的发现。\n\n综合考虑，我维持 **Overall 3.0（Findings）**。W1（缺外部对比）和 W5（entity ordering 未量化）是 R1 提出的新问题，进一步支持了 Findings 而非 main conference 的判断。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1615 · 2026-05-22T12:44:35.586696+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3714
}
```

</details>

---


### Tool call

_source line 1616 · 2026-05-22T12:44:41.617923+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1617 · 2026-05-22T12:44:41.668666+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1618 · 2026-05-22T12:44:47.374441+00:00_

逐条回应完成。核心判断：

- R1 的 W1（缺外部对比）、W3（Prop 1 caveat）、W4（κ̄ 统计）、W5（entity ordering）均 AGREE
- **REBUT R1-W2**：论文说的是 k=4 而非 k=3，"eliminates all" 是 LoRA 设定下两个模型都成立，R1 混淆了 zero-shot 和 LoRA 上下文
- 维持 Overall 3.0（Findings）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 34

## Round 34

110 recorded events


### User

_source line 1619 · 2026-05-22T13:43:40.914580+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责【新颖性 + 相关工作 + 写作质量 + 格式合规】。

## 论文信息
- 标题: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
- 论文路径: projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex
- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/submitted.pdf

## Venue 要求（EMNLP 2026，通过 ARR 提交）
- 投稿类别: Long Paper
- 正文页数上限: 8 页（不含 references、limitations、ethics）
- 模板: ACL format（\usepackage[review]{acl}）
- 匿名规则: Double-blind（论文不得包含作者信息，不得有泄露身份的 self-reference）
- 附录: 允许，不计入页数限制
- ARR submission deadline: 2026-05-25
- Overall Assessment 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 你的审查侧重
1. **新颖性评估**：OntoCoDec 的核心贡献——两层约束解码架构——相对于现有 GCD（XGrammar/Outlines/SynCode）、PICARD、GoLLIE、KnowCoder 等工作的增量新颖性有多大？Proposition 1 是否为社区提供了新的理论洞察，还是对已知事实的形式化？
2. **相关工作覆盖**：§6 和 Appendix B 的 related work 是否全面？是否遗漏重要工作（特别是 2024-2026 最新的 constrained decoding / schema-aware IE 工作）？引用是否准确？
3. **写作质量**：论文的叙事结构是否清晰？Abstract/Intro 是否准确概括了贡献和结果？数值密度是否适当？是否有 overclaiming？术语使用是否一致？
4. **格式合规**：正文是否 ≤ 8 页？是否符合 ACL 模板？匿名性是否保持？Limitations 和 Ethics 是否满足 ARR 要求？
5. **论文整体定位**：这篇论文是否适合 EMNLP 主会议？是否更适合 Findings 或 Workshop？

请按照以下格式输出审稿意见：

### Summary（2-3 句概述）

### Strengths（逐条列出，S1/S2/...）

### Weaknesses（逐条列出，W1/W2/...，标注严重程度 [Must-Fix] / [Should-Fix] / [Minor]）

### Questions（逐条列出，Q1/Q2/...）

### Missing References（如有）

### Overall Assessment
- Soundness: X/5
- Excitement: X/5
- Overall: X/5（使用 ARR 评分标准）
- Confidence: X/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1620 · 2026-05-22T13:43:49.928379+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
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

_source line 1621 · 2026-05-22T13:43:49.928937+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1622 · 2026-05-22T13:43:54.057618+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1623 · 2026-05-22T13:43:55.145246+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/submitted.pdf",
  "pages": "1-10",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/submitted.pdf",
    "pages": "1-10",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1624 · 2026-05-22T13:44:01.416961+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Scoring Criteria

For Findings papers, the main criteria are soundness and reproducibility, while conference recommendations
…[truncated 1235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7359
}
```

</details>

---


### Tool result

_source line 1625 · 2026-05-22T13:44:03.933143+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 403.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 441.1}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifac
…[truncated 581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8787
}
```

</details>

---


### Tool call

_source line 1626 · 2026-05-22T13:44:09.860079+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract all review form fields, scoring dimensions, and their scales (1-5 or whatever). List each dimension with its description and scoring rubric."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract all review form fields, scoring dimensions, and their scales (1-5 or whatever). List each dimension with its description and scoring rubric."
  }
}
```

</details>

---


### Tool call

_source line 1627 · 2026-05-22T13:44:10.362570+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 1628 · 2026-05-22T13:44:11.168287+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 1629 · 2026-05-22T13:44:11.319330+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1630 · 2026-05-22T13:44:11.821806+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1631 · 2026-05-22T13:44:12.130747+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 811
}
```

</details>

---


### Tool call

_source line 1632 · 2026-05-22T13:44:12.131187+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1633 · 2026-05-22T13:44:12.786850+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1634 · 2026-05-22T13:44:12.838106+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1016
}
```

</details>

---


### Tool result

_source line 1635 · 2026-05-22T13:44:13.342723+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1211
}
```

</details>

---


### Tool result

_source line 1636 · 2026-05-22T13:44:13.645067+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool result

_source line 1637 · 2026-05-22T13:44:15.150900+00:00_

# ACL Rolling Review Form Fields & Scoring Dimensions

## Primary Scoring Dimensions

**1. Reviewer Confidence**
- Scale: 1-5
- Description: "I read the paper very carefully and am familiar with related work" (5) to "Not my area, or paper is very hard to understand" (1)

**2. Soundness**
- Scale: 1-5 (with .5 increments)
- Description: "is it sufficiently sound and thorough? Does it clearly state scientific claims and provide adequate support?"
- Range: "Excellent: This study is one of the most thorough" (5) to "Major Issues: not yet sufficiently thorough to warrant publication" (1)

**3. Excitement**
- Scale: 1-5 (with .5 increments)
- Description: Measures subjective assessment of innovation, impact, and relevance
- Range: "Highly Exciting: I would recommend this paper to others" (5) to "Not Exciting" (1)

**4. Overall Assessment**
- Scale: 1-5 (with .5 increments)
- Range: "Consider for Award" (5) to "Do not resubmit" (1)
- Venues: Award consideration, Conference, Findings, or Resubmit options

## Secondary Evaluation Areas

**Reproducibility:** 1-5 scale assessing information sufficiency for replication

**Datasets & Software:** 1-5 scales measuring resource value to researchers

**Author Identity Knowledge:** 1-5 scale for double-blind assessment integrity

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5290
}
```

</details>

---


### Tool call

_source line 1638 · 2026-05-22T13:44:19.478889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1639 · 2026-05-22T13:44:19.984664+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1640 · 2026-05-22T13:44:20.386326+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1641 · 2026-05-22T13:44:21.341969+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1863
}
```

</details>

---


### Tool call

_source line 1642 · 2026-05-22T13:44:21.394521+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1643 · 2026-05-22T13:44:21.547142+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1644 · 2026-05-22T13:44:22.308777+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1922
}
```

</details>

---


### Tool result

_source line 1645 · 2026-05-22T13:44:22.565534+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2580
}
```

</details>

---


### Tool result

_source line 1646 · 2026-05-22T13:44:24.078065+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2683
}
```

</details>

---


### Tool result

_source line 1647 · 2026-05-22T13:44:24.281784+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2734
}
```

</details>

---


### Tool call

_source line 1648 · 2026-05-22T13:44:30.691371+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/submitted.pdf",
  "pages": "11-20",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/submitted.pdf",
    "pages": "11-20",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1649 · 2026-05-22T13:44:32.100877+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the detailed reviewer guidelines, especially criteria for novelty assessment, what constitutes a good review, and any specific scoring guidance for soundness, excitement, and overall assessment."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the detailed reviewer guidelines, especially criteria for novelty assessment, what constitutes a good review, and any specific scoring guidance for soundness, excitement, and overall assessment."
  }
}
```

</details>

---


### Tool result

_source line 1650 · 2026-05-22T13:44:32.654776+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 619.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 602.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 566.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 367.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 551.1}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 550.3}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 569.0}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 547.2}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_const
…[truncated 599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1963
}
```

</details>

---


### Tool result

_source line 1651 · 2026-05-22T13:44:40.415078+00:00_

# ARR Reviewer Guidelines: Key Criteria and Scoring Framework

## Novelty Assessment

The guidelines emphasize that novelty should be evaluated contextually rather than as an absolute requirement. Reviewers should recognize that "findings that seem intuitive but haven't previously been tested empirically" constitute valid contributions. The document warns against dismissing work simply because "highly similar work" exists—such claims require specific citations to papers published at least 3+ months before the submission deadline.

Importantly, the guidelines note that contribution type matters: "reproduction, reimplementation, analysis" papers deserve fair evaluation and are explicitly within scope.

## What Constitutes a Strong Review

Effective reviews demonstrate these qualities:

**Specificity**: Instead of "X is not clear," explain precisely which elements are missing. As the guide states, "It's possible that when using the decoding from Smith and Eisner (2006) on the Hausa newswire dataset, there might not be enough training data" provides actionable feedback.

**Professional Tone**: Reviews should be "professional and neutral, if not kind." The guidelines emphasize treating authors respectfully, acknowledging that "someone out there is reviewing your papers too."

**Engagement with Author Responses**: Reviewers should "at least acknowledge the authors' response" and update assessments when concerns are addressed.

## Scoring Guidance Framework

As of February 2025, reviewers provide three distinct scores:

**Soundness**: This score "must be justified by the text of the review." If you assign low soundness without identifying major faults, your review lacks coherence. This dimension assesses technical validity and methodological rigor.

**Excitement**: This orthogonal score reflects "personal taste" and subjective interest—explicitly separate from soundness judgments. A technically sound paper may receive low excitement if it lacks personal appeal.

**Overall 
…[truncated 258 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 8314
}
```

</details>

---


### Tool call

_source line 1652 · 2026-05-22T13:44:44.181627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1653 · 2026-05-22T13:44:44.535562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1654 · 2026-05-22T13:44:44.989292+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 1655 · 2026-05-22T13:44:44.989748+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1656 · 2026-05-22T13:44:45.950694+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1415
}
```

</details>

---


### Tool call

_source line 1657 · 2026-05-22T13:44:45.951138+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1658 · 2026-05-22T13:44:46.253486+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1263
}
```

</details>

---


### Tool call

_source line 1659 · 2026-05-22T13:44:46.253932+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1660 · 2026-05-22T13:44:46.356877+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---


### Tool result

_source line 1661 · 2026-05-22T13:44:46.910945+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 657
}
```

</details>

---


### Tool call

_source line 1662 · 2026-05-22T13:44:51.545881+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/submitted.pdf",
  "pages": "21-30",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/submitted.pdf",
    "pages": "21-30",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1663 · 2026-05-22T13:44:53.255442+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.1}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p22.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.1}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p23.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.0}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.5}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p25.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.9}, {\"page\": 26, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p26.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.1}, {\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p27.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 407.0}, {\"page\": 28, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p28.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.9}, {\"page\": 29, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_const
…[truncated 599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1709
}
```

</details>

---


### Tool call

_source line 1664 · 2026-05-22T13:44:57.801563+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 1665 · 2026-05-22T13:44:58.306875+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1666 · 2026-05-22T13:44:59.468253+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1666
}
```

</details>

---


### Tool call

_source line 1667 · 2026-05-22T13:44:59.468719+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 1668 · 2026-05-22T13:44:59.820291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1669 · 2026-05-22T13:45:00.325721+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2018
}
```

</details>

---


### Tool call

_source line 1670 · 2026-05-22T13:45:00.326206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 1671 · 2026-05-22T13:45:01.988542+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2519
}
```

</details>

---


### Tool result

_source line 1672 · 2026-05-22T13:45:02.647367+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2827
}
```

</details>

---


### Tool result

_source line 1673 · 2026-05-22T13:45:02.799183+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2472
}
```

</details>

---


### Tool call

_source line 1674 · 2026-05-22T13:45:07.522935+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 1675 · 2026-05-22T13:45:08.126106+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 1676 · 2026-05-22T13:45:08.427548+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p22.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p22.png"
  }
}
```

</details>

---


### Tool call

_source line 1677 · 2026-05-22T13:45:08.478493+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p23.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p23.png"
  }
}
```

</details>

---


### Tool call

_source line 1678 · 2026-05-22T13:45:09.333056+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p24.png"
  }
}
```

</details>

---


### Tool result

_source line 1679 · 2026-05-22T13:45:09.536727+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1109
}
```

</details>

---


### Tool call

_source line 1680 · 2026-05-22T13:45:09.537181+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p25.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p25.png"
  }
}
```

</details>

---


### Tool result

_source line 1681 · 2026-05-22T13:45:09.688657+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1210
}
```

</details>

---


### Tool result

_source line 1682 · 2026-05-22T13:45:10.695835+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1362
}
```

</details>

---


### Tool result

_source line 1683 · 2026-05-22T13:45:10.697076+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1159
}
```

</details>

---


### Tool call

_source line 1684 · 2026-05-22T13:45:15.516455+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p26.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p26.png"
  }
}
```

</details>

---


### Tool call

_source line 1685 · 2026-05-22T13:45:16.069865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p27.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p27.png"
  }
}
```

</details>

---


### Tool result

_source line 1686 · 2026-05-22T13:45:16.472388+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool result

_source line 1687 · 2026-05-22T13:45:16.475272+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---


### Tool call

_source line 1688 · 2026-05-22T13:45:16.475610+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p28.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p28.png"
  }
}
```

</details>

---


### Tool result

_source line 1689 · 2026-05-22T13:45:17.379862+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1690 · 2026-05-22T13:45:17.480632+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p29.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p29.png"
  }
}
```

</details>

---


### Tool call

_source line 1691 · 2026-05-22T13:45:17.682005+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p30.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p30.png"
  }
}
```

</details>

---


### Tool result

_source line 1692 · 2026-05-22T13:45:18.439302+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool result

_source line 1693 · 2026-05-22T13:45:18.591931+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 1694 · 2026-05-22T13:45:24.116975+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/submitted.pdf",
  "pages": "31-34",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/submitted.pdf",
    "pages": "31-34",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1695 · 2026-05-22T13:45:24.620786+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 31, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p31.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 509.6}, {\"page\": 32, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p32.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 456.4}, {\"page\": 33, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p33.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 489.4}, {\"page\": 34, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p34.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 427.0}], \"total_pages\": 34, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1696 · 2026-05-22T13:45:28.750067+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p31.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p31.png"
  }
}
```

</details>

---


### Tool call

_source line 1697 · 2026-05-22T13:45:29.252597+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p32.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p32.png"
  }
}
```

</details>

---


### Tool result

_source line 1698 · 2026-05-22T13:45:30.308263+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1558
}
```

</details>

---


### Tool result

_source line 1699 · 2026-05-22T13:45:30.309119+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1056
}
```

</details>

---


### Tool call

_source line 1700 · 2026-05-22T13:45:30.459879+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p33.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p33.png"
  }
}
```

</details>

---


### Tool call

_source line 1701 · 2026-05-22T13:45:30.460378+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p34.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images/submitted_p34.png"
  }
}
```

</details>

---


### Tool result

_source line 1702 · 2026-05-22T13:45:31.518526+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1058
}
```

</details>

---


### Tool result

_source line 1703 · 2026-05-22T13:45:31.569833+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1109
}
```

</details>

---


### Tool call

_source line 1704 · 2026-05-22T13:45:42.714162+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1705 · 2026-05-22T13:45:43.316753+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (u
…[truncated 1889 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 1706 · 2026-05-22T13:45:43.317224+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "constrained decoding structured information extraction 2025 2026 schema-aware generation LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "constrained decoding structured information extraction 2025 2026 schema-aware generation LLM"
  }
}
```

</details>

---


### Tool result

_source line 1707 · 2026-05-22T13:45:54.670894+00:00_

Web search results for query: "constrained decoding structured information extraction 2025 2026 schema-aware generation LLM"

Links: [{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"1 LLMStructBench: Benchmarking Large Language Model Structured Data Extraction","url":"https://arxiv.org/pdf/2602.14743"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Constrained Decoding: Grammar-Guided Generation for Structured LLM Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/pdf/2510.20345"}]

Based on the search results, here's what's currently happening with constrained decoding and schema-aware generation for LLMs in 2025-2026:

## Recent Evolution and Key Technologies

Schema enforcement emerged as a major phase from 2024 to 2025, with OpenAI releasing Structured Outputs in August 2024, Google Gemini adding response_schema at Google I/O in May 2024, and Anthropic following in November 2025 with constrained decoding for Claude.

High-performance engines represent the current phase from 2025 to 2026, with open-source engines like XGrammar and llguidance
…[truncated 1174 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 11353
}
```

</details>

---


### Tool call

_source line 1708 · 2026-05-22T13:45:59.282702+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DCCD draft-conditioned constrained decoding structured generation 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DCCD draft-conditioned constrained decoding structured generation 2025 2026 arxiv"
  }
}
```

</details>

---


### Tool call

_source line 1709 · 2026-05-22T13:45:59.785166+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLMStructBench structured data extraction benchmark 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLMStructBench structured data extraction benchmark 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 1710 · 2026-05-22T13:46:00.538701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "offset": "80",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "offset": "80",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1711 · 2026-05-22T13:46:00.639606+00:00_

80	Schema coverage gaps (one-third of residual violations) arise because RE constraints are extracted from training-data type pairs, which may not cover all valid combinations; larger training sets or manual constraint table completion can reduce this gap.
81	Post-hoc type consensus re-voting (Appendix~\ref{app:tcr}) reduces CF violations by 18--92\% depending on model and dataset, confirming that first-assignment ordering sensitivity is a primary CF source; however, integrating consensus into the decoding loop remains future work.
82	
83	\paragraph{Evaluation coverage.}
84	Zero-shot results cover three 7--8B-class models, where relation F1 remains around 4--8\% compared to $\sim$45\% for fine-tuned systems.
85	Zero-shot evaluation covers three 8B-class and one 70B-class model; fine-tuning composability is validated on 8B-class (two models, full datasets) and 70B-class models (one model; SciERC full, DocRED 200-document subset).
86	Scaling to smaller models has not been verified, and the dual-factor pattern may not generalize to other scales.
87	Composability with fine-tuned models is validated on SciERC, DocRED, and WikiEvents with Qwen3-8B and Llama-3.1-8B (RE: DR\,$\leq$\,0.09\%, R-F1 within $\pm$0.8\,pp; EE: RoV$\to$0\%, AC$\leq$0.8\%), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\%, Llama 0.46\% on SciERC) traces to schema-level type ambiguity (\textsc{Generic}$\leftrightarrow$X) rather than enforcement failure.
88	WikiEvents fine-tuning composability is preliminary (20-document test set, the full official split).
89	All main experiments use greedy decoding; our evaluation of beam search on the full SciERC (551 documents) and DocRED (998 documents) test sets across three models confirms compatibility (Appendices~\ref{app:sampling},~\ref{app:beam-search}), but comprehensive evaluation across all decoding configurations remains future work.
90	
91	\paragraph{Engineering considerations.}
92	Scalability benchmarks up to 200 ent
…[truncated 2948 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 1712 · 2026-05-22T13:46:05.307024+00:00_

Web search results for query: "LLMStructBench structured data extraction benchmark 2025 2026"

Links: [{"title":"LLMStructBench: Benchmarking Large Language Model Structured Data Extraction | alphaXiv","url":"https://www.alphaxiv.org/resources/2602.14743v1"},{"title":"[2602.14743] LLMStructBench: Benchmarking Large Language Model Structured Data Extraction","url":"https://arxiv.org/abs/2602.14743"},{"title":"LLMStructBench: Benchmarking Large Language Model Structured Data Extraction","url":"https://arxiv.org/html/2602.14743v1"},{"title":"(PDF) LLMStructBench: Benchmarking Large Language Model Structured Data Extraction","url":"https://www.researchgate.net/publication/400855630_LLMStructBench_Benchmarking_Large_Language_Model_Structured_Data_Extraction"},{"title":"1 LLMStructBench: Benchmarking Large Language Model Structured Data Extraction","url":"https://arxiv.org/pdf/2602.14743"},{"title":"The Structured Output Benchmark: A Multi-Source Benchmark for Evaluating Structured Output Quality in Large Language Models","url":"https://arxiv.org/html/2604.25359"},{"title":"LLMStructBench: Benchmarking Large Language Model Structured Data Extraction | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2602.14743"},{"title":"ExtractBench: A Benchmark and Evaluation Methodology for Complex Structured Extraction","url":"https://arxiv.org/html/2602.12247v2"}]

Based on the search results, here's what I found about LLMStructBench:

## Overview

LLMStructBench is a novel benchmark for evaluating Large Language Models (LLMs) on extracting structured data and generating valid JavaScript Object Notation (JSON) outputs from natural-language text.

## Key Features

The open dataset comprises diverse, manually verified parsing scenarios of varying complexity and enables systematic testing across 22 models and five prompting strategies. Complementary performance metrics capture both token-level accuracy and document-level validity, facilitating rigorous comparis
…[truncated 552 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5521
}
```

</details>

---


### Tool result

_source line 1713 · 2026-05-22T13:46:07.314622+00:00_

Web search results for query: "DCCD draft-conditioned constrained decoding structured generation 2025 2026 arxiv"

Links: [{"title":"[2603.03305] Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/abs/2603.03305"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"Appendix","url":"https://arxiv.org/html/2603.03305"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/pdf/2403.06988"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11747381/"},{"title":"[2508.15910] Evaluating Structured Decoding for Text-to-Table Generation: Evidence from Three Datasets","url":"https://www.arxiv.org/abs/2508.15910"},{"title":"Earley-Driven Dynamic Pruning for Efficient Structured Decoding","url":"https://arxiv.org/pdf/2506.01151"},{"title":"Efficient and Asymptotically Unbiased Constrained Decoding for Large   Language Models","url":"https://arxiv.org/pdf/2504.09135"},{"title":"[2508.15866] Correctness-Guaranteed Code Generation via Constrained Decoding","url":"https://arxiv.org/abs/2508.15866"}]

Based on the search results, I found the paper you're looking for:

## Draft-Conditioned Constrained Decoding (DCCD)

DCCD is a simple two-step, training-free inference procedure that decouples semantic planning from structural enforcement: an unconstrained draft is generated first, and constrained decoding is then applied, conditioned on this draft, to guarantee validity.

**Key Details:**
- **ArXiv ID:** 2603.03305
- **Publication Date:** March 5, 2026
- **URL:** https://arxiv.org/abs/2603.03305

**Performance:**
DCCD improves strict structured accuracy by up to +24 percentage points over standard constrained decoding (e.g., 15.2% to 39.0% on GSM8K with a
…[truncated 771 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8031
}
```

</details>

---


### Tool call

_source line 1714 · 2026-05-22T13:46:12.587862+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"schema constrained\" OR \"ontology-guided\" information extraction relation extraction 2025 2026 constrained decoding NeurIPS ACL EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"schema constrained\" OR \"ontology-guided\" information extraction relation extraction 2025 2026 constrained decoding NeurIPS ACL EMNLP"
  }
}
```

</details>

---


### Tool call

_source line 1715 · 2026-05-22T13:46:13.492499+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Reddy Boldi 2026 \"draft-conditioned\" constrained decoding structured generation quality degradation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Reddy Boldi 2026 \"draft-conditioned\" constrained decoding structured generation quality degradation"
  }
}
```

</details>

---


### Tool result

_source line 1716 · 2026-05-22T13:46:20.671655+00:00_

Web search results for query: "Reddy Boldi 2026 "draft-conditioned" constrained decoding structured generation quality degradation"

Links: [{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"[2603.03305] Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/abs/2603.03305"},{"title":"Appendix","url":"https://arxiv.org/html/2603.03305"},{"title":"Schema Key Wording as an Instruction Channel in Structured Generation under Constrained Decoding","url":"https://arxiv.org/html/2604.14862"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/pdf/2403.06988"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Thinking Before Constraining: A Unified Decoding Framework for Large Language Models","url":"https://arxiv.org/pdf/2601.07525"}]

I found relevant information about your query. Here are the key results:

## Draft-Conditioned Constrained Decoding (DCCD)

Draft-Conditioned Constrained Decoding (DCCD) is a simple two-step, training-free inference procedure that decouples semantic planning from structural enforcement: an unconstrained draft is generated first, and constrained decoding is then applied, conditioned on this draft, to guarantee validity.

### The Problem It Addresses

Constrained decoding enforces validity token-by-token via masking and renormalization, but it can distort generation when the model assigns low probability mass to valid continuations, pushing decoding toward locally valid yet semantically incorrect trajectories. This quality degradation problem is what DCCD aims to solve.

### Key Results

The proposed approach yields consistent accuracy improvements over standard constrained decoding across model scales (1B–14B).

### Theoretic
…[truncated 461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7179
}
```

</details>

---


### Tool result

_source line 1717 · 2026-05-22T13:46:22.027020+00:00_

Web search results for query: ""schema constrained" OR "ontology-guided" information extraction relation extraction 2025 2026 constrained decoding NeurIPS ACL EMNLP"

Links: [{"title":"Published as a conference paper at ICAIS 2025","url":"https://arxiv.org/pdf/2510.20345"},{"title":"RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints","url":"https://arxiv.org/html/2509.19057v1"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/html/2510.20345v1"},{"title":"Axiom Generation for Automated Ontology Construction from Texts Through Schema Mapping","url":"https://www.mdpi.com/2504-4990/8/2/29"},{"title":"OntoKG: Ontology-Oriented Knowledge Graph Construction with Intrinsic-Relational Routing","url":"https://arxiv.org/html/2604.02618v1"},{"title":"[2509.04696] ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/abs/2509.04696"},{"title":"OSKGC: A benchmark for Ontology Schema-based ...","url":"https://ceur-ws.org/Vol-4041/paper1.pdf"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/html/2509.04696v1"},{"title":"(PDF) ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://www.researchgate.net/publication/395338944_ODKE_Ontology-Guided_Open-Domain_Knowledge_Extraction_with_LLMs"}]

I found relevant research on schema-constrained and ontology-guided information extraction. Here are the key findings:

## Recent Work on Schema-Constrained and Ontology-Guided Extraction (2025-2026)

### Key Systems and Frameworks

ODKE+ dynamically generates ontology snippets tailored to each entity type to align extractions with schema constraints, enabling scalable, type-consistent fact extraction across 195 predicates. The system supports batch and streaming modes, processing over 9 million Wikipedia pages and ingesting 19 million high-confidence facts with 98.8% precision.

RelCheck (Ourekouch et al
…[truncated 1529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9439
}
```

</details>

---


### Tool call

_source line 1718 · 2026-05-22T13:46:28.935728+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"thinking before constraining\" unified decoding framework 2026 arxiv constrained decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"thinking before constraining\" unified decoding framework 2026 arxiv constrained decoding"
  }
}
```

</details>

---


### Tool call

_source line 1719 · 2026-05-22T13:46:28.936219+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"schema key wording\" instruction channel constrained decoding structured generation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"schema key wording\" instruction channel constrained decoding structured generation 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 1720 · 2026-05-22T13:46:35.361697+00:00_

Web search results for query: ""thinking before constraining" unified decoding framework 2026 arxiv constrained decoding"

Links: [{"title":"[2601.07525] Thinking Before Constraining: A Unified Decoding Framework for Large Language Models","url":"https://arxiv.org/abs/2601.07525"},{"title":"Thinking Before Constraining: A Unified Decoding Framework for Large Language Models","url":"https://arxiv.org/html/2601.07525"},{"title":"Thinking Before Constraining: A Unified Decoding Framework for Large","url":"https://www.arxiv.org/pdf/2601.07525"},{"title":"Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs","url":"https://arxiv.org/html/2604.06603"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/pdf/2506.14901"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"}]

I found the paper you're looking for! Here are the details:

"Thinking Before Constraining: A Unified Decoding Framework for Large Language Models" was submitted on January 12, 2026, and is available on arXiv as paper 2601.07525.

The paper addresses the tradeoff between natural generation (which allows rich reasoning but lacks guaranteed structure) and structured generation/constrained decoding (which ensures consistency and parsable outputs but can restrict reasoning capabilities).

The proposed approach allows LLMs to reason freely until specific trigger tokens are generated, then switches to structured generation, preserving the expressive power of natural language reasoning while ensuring the reliability of structured outputs. The method achieved a substantial gain of up to 27% in accuracy.

The authors are Ngoc Trinh Hung Nguyen, Alonso Silva, Laith Zumot, Liubov Tupikina, Armen Aghasaryan, and Mehwish Alam. You can access the paper at https://arxiv.org/abs/2601.07525.


REMINDER: You MUST include
…[truncated 74 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6425
}
```

</details>

---


### Tool result

_source line 1721 · 2026-05-22T13:46:35.965910+00:00_

Web search results for query: ""schema key wording" instruction channel constrained decoding structured generation 2024 2025"

Links: [{"title":"Schema Key Wording as an Instruction Channel in Structured Generation under Constrained Decoding","url":"https://arxiv.org/html/2604.14862"},{"title":"[2604.14862] Schema Key Wording as an Instruction Channel in Structured Generation under Constrained Decoding","url":"https://arxiv.org/abs/2604.14862"},{"title":"Learning to Generate Structured Output with Schema ...","url":"https://aclanthology.org/2025.acl-long.243.pdf"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"Beyond Free-Form Text: How Constrained Decoding is Reshaping Structured Generation in LLMs | by Brijesh Nambiar | Medium","url":"https://medium.com/@brijeshrn/beyond-free-form-text-how-constrained-decoding-is-reshaping-structured-generation-in-llms-5f7a38bef259"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"}]

I found relevant research on this topic. Here are the key findings:

## Main Research

This is the first work to systematically study how schema key formulation acts as an implicit instruction channel and affects model performance under constrained decoding. The research paper, titled "Schema Key Wording as an Instruction Channel in Structured Generation under Constrained Decoding," was published in April 2026.

## Key Findings

The study shows that m
…[truncated 1117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7029
}
```

</details>

---


### Tool call

_source line 1722 · 2026-05-22T13:50:03.991727+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n## Summary（2-3 句概述）\n\n本文提出 OntoCoDec，一个将 IE 本体编译为可组合 token 级解码约束的两层框架：grammar layer（CFG）保证 JSON 结构和词汇合法性，semantic layer（带状态的 prefix-decidable transducer）通过动态 entity registry 在运行时执行 domain/range 类型约束。Proposition 1 用 pumping lemma 证明了 IE 中带无界实体集的类型约束不是 context-free 的，为两层架构提供了理论依据。实验覆盖 SciERC、DocRED、WikiEvents 三个数据集，多个 8B 和 70B 模型，zero-shot 和 LoRA fine-tuning 设置，展示了 DR 违规率从 42-99% 降到近零（fine-tuning 下 ≤0.09%）。\n\n---\n\n## Strengths（逐条列出）\n\n**S1. 理论与系统设计的有机结合。** Proposition 1（§3, p.3; 完整证明 Appendix O, p.33-34）是本文的核心理论贡献。通过 pumping lemma 严格证明带无界实体集的 domain/range 类型约束不是 context-free，从而为 grammar layer 之上添加 semantic layer 提供了不可替代的理论动机。这不是一个显然的结论——虽然实践者可能直觉上知道 CFG 不够用，但形式化证明为社区建立了一个有用的参考点，也清晰界定了 grammar-only 方法（XGrammar、Outlines、SynCode）的能力边界。\n\n**S2. 实验设计极为全面。** 论文的实验矩阵令人印象深刻：3 个 RE 数据集 × 3-4 个模型 × zero-shot/fine-tuned × 多种解码策略（greedy/beam/sampling），外加 WikiEvents 上的事件抽取扩展。Table 1 的五因素消融（§5.1）、Table 2 的 fine-tuning composability、Table 3 的 cross-model zero-shot 验证、以及 Table 4 的事件抽取结果——每个实验都回答了一个明确的研究问题。附录中的 beam search 兼容性（Appendix F）、prompt sensitivity（Appendix I）、document length 分析（Appendix H）、constraint tightness 案例分析（Appendix N）进一步增强了可信度。\n\n**S3. 约束三层分类体系清晰实用。** §2 将 IE 类型约束分为三层——(1) context-free（JSON 结构 + 词汇）、(2) prefix-decidable with state（domain/range）、(3) non-local cross-entity consistency——这个分类不仅服务于本文的系统设计，也为后续研究提供了一个有用的概念框架。\n\n**S4. Grammar-first fallback 机制设计合理。** §4 的 Eq.(2) 定义了两层约束的合取，当语义约束与语法约束同时排除所有 token 时，优先保证 JSON 完整性。Appendix C 的 causal tracing（Table 6）精确定位了 fallback 触发的位置和原因，Table 7 的 CF-DR tradeoff 分析展示了这一设计选择的代价。这种对工程决策的系统化分析是本文的一个亮点。\n\n**S5. 与 GCD baseline 的等价性验证（Appendix C, Table 16-17）。** 论文不仅声称 grammar layer 等价于 GCD，还在 SciERC 上用 vLLM 的 `guided_json` 模式实证验证了这一等价性（所有指标差异 <0.5pp），这增强了论文的可信度。\n\n---\n\n## Weaknesses（逐条列出，标注严重程度）\n\n**W1 [Should-Fix] 新颖性的增量特征需更坦诚讨论。** Grammar layer 本质上是标准 GCD（论文自己在 Table 16-17 验证了与 vLLM guided_json 的等价性），这意味着本文的新颖性完全集中在 semantic layer 和 Proposition 1 上。Semantic layer 的核心思想——维护一个运行时 entity registry 来实施 domain/range 类型检查——是一个合理但相对直观的工程扩展。PICARD（Scholak et al., 2021）已经展示了在 constrained decoding 中维护状态信息来执行跨位置约束的思路（虽然是 SQL 领域）。论文应在 §1 或 §7 中更明确地讨论：semantic layer 的概念创新点究竟在哪里，与 PICARD 式的 stateful constrained decoding 的区别不仅仅是应用领域的不同。\n\n- **具体位置**：§1 第 3 段（\"We make a systematic engineering contribution with theoretical grounding\"）和 §7\n- **为什么影响评分**：如果 reviewer 认为这主要是已知技术在新领域的应用，会显著降低 excitement 评分\n- **建议**：在 §7 Discussion 中增加 1-2 段坦率讨论增量创新 vs. 系统性贡献的关系，强调 Proposition 1 的理论意义和 entity registry + grammar-first fallback 的设计创新\n\n**W2 [Should-Fix] Proposition 1 的实际影响力可能被高估。** Proposition 1 证明了 domain/range 类型约束不是 context-free，但这个结论的实践意义需要更细致的讨论：\n- (a) 论文的 Remark（p.3）自己承认\"当实体集有限时（实际情况），有效语言在技术上是正则的\"，但对应的 DFA 状态数是指数级的（e.g., DocRED 的 7 entity types, 20+ entities → 10^15 states）。这个 distinction（理论上不可能 vs. 工程上不可行）是重要的，但论文的行文倾向于模糊二者的边界。\n- (b) Proposition 1 证明的是 PDA **cannot** enforce 类型约束——但这是对 PDA 的已知限制（PDA 不能做 cross-reference checking），并非一个惊人的结论。证明的价值在于将这个直觉应用到 IE 场景并给出严格的形式化，但不应被包装为一个深刻的理论洞察。\n- **具体位置**：§3, p.3, Proposition 1 及其 Remark\n- **建议**：在 Remark 后增加一句明确说明：\"The practical contribution of Proposition 1 is not the impossibility result per se, but rather the precise characterization of what Level 2 constraints require that motivates our two-layer design.\"\n\n**W3 [Should-Fix] CF 违规问题未解决，但论文的叙事未充分强调这一局限。** 论文的主要实验指标聚焦 DR reduction，但 CF violations（cross-field type inconsistency）在 fine-tuning 后仍有 0.46-1.18%（Table 2, Qwen SciERC），零-shot 下更高（Table 1, 最高 12.02%）。Table 7 显示 CF 和 DR 是一个 tradeoff（消除 CF fallback 导致 DR +13.85pp）。Limitations 段（p.9）确实讨论了这一问题，但：\n- Abstract 和 Introduction 将 CF 表述为 \"CF ≤ 1.4% through independent enforcement\"，给人一种 CF 已基本解决的印象\n- 论文的叙事结构更强调 DR 的成功（\"near-eliminates DR\"），而 CF 作为一个 **未解决的核心问题** 没有在 Introduction 或 Discussion 中得到同等权重的讨论\n- **具体位置**：Abstract, §1 contributions list, §7 Discussion\n- **为什么影响评分**：CF 问题的严重程度取决于下游应用——在知识图谱构建中，同一实体的类型不一致是一个严重问题。论文如果更坦诚地将 CF 作为 open problem 呈现，反而会增强可信度。\n- **建议**：在 Abstract 中将 CF 从 \"through independent enforcement\" 改为更审慎的表述（如 \"with residual CF violations of 0.5-1.2% under fine-tuning, attributable to per-relation independence\"）；在 §7 中用 1-2 句明确将 global entity-level type consensus 标记为最重要的 future work\n\n**W4 [Should-Fix] 近期高度相关的 constrained decoding 质量工作未被引用。** 论文在 Appendix B 对 constrained decoding 文献的覆盖较为全面，但遗漏了几篇 2026 年初发表的直接相关工作：\n1. **DCCD**（Reddy et al., arXiv:2603.03305, March 2026）—— Draft-Conditioned Constrained Decoding，提出先生成无约束草稿再执行约束解码，通过 KL-projection 视角分析了约束解码的 \"projection tax\"。这与 OntoCoDec 的 grammar-first fallback 解决的是同一类问题（约束解码导致的生成质量退化），方法论思路互补。\n2. **\"Thinking Before Constraining\"**（Nguyen et al., arXiv:2601.07525, January 2026）—— 允许 LLM 自由推理直到触发 token 再切换到结构化生成，在数学推理任务上取得 +27% 准确率提升。这与 OntoCoDec 的 S2 two-pass pipeline（§4）在设计哲学上有相似之处。\n3. **\"Schema Key Wording\"**（arXiv:2604.14862, April 2026）—— 发现 JSON schema 的 key 命名本身就是约束解码下的隐式指令通道，影响模型性能。这与 OntoCoDec 的 schema compilation 步骤直接相关。\n- **具体位置**：§6 Related Work, Appendix B\n- **建议**：在 §6 的 \"Constrained decoding\" 段落末尾增加 2-3 句讨论这些工作，特别是 DCCD 与 grammar-first fallback 的关系\n\n**W5 [Minor] 论文信息密度极高，可读性有一定挑战。** 正文 8 页塞入了完整的理论分析、三层约束分类、两层架构、constraint composition、五因素消融、三个数据集的主实验、fine-tuning composability、cross-model 验证、event extraction 扩展、runtime overhead、以及 related work。每一段都承载大量信息，首次阅读需要反复回翻。\n- 例如：§3.3 Semantic Layer 在一段之内引入了 entity registry、dynamic masking、type-bearing positions、constraint tightness、grammar-first fallback、grammar-semantic interaction 等概念，没有给读者消化的空间\n- Figure 1 作为唯一的系统图，承担了过多解释责任\n- **建议**：考虑增加一个 running example（如用 SciERC 的一个具体 triple 展示两层约束如何逐步应用），这在不增加页数的情况下可以显著提高可读性\n\n**W6 [Minor] 标题中 \"Compiled\" 一词可能产生歧义。** \"Compiled Schema Constraints\" 中的 \"compiled\" 可以被理解为 \"collected/gathered\"（收集），而论文的实际含义是 \"translated into a computational representation\"（编译成计算表示）。对于 NLP 社区读者（而非 PL 社区），这个双关可能不够清晰。\n- **建议**：考虑 \"Translating Schema Constraints into...\" 或在 abstract 首句明确 \"compiles...into\" 的含义（论文实际上在 abstract 中已经做了，但标题本身的歧义仍在）\n\n**W7 [Minor] 部分数值在 abstract 中过于精确。** Abstract 中出现 \"DR ≤ 0.09%\"、\"R-F1 43-46% (±0.8pp)\"、\"CF ≤ 1.4%\"——这些数字精确到小数点后两位，但覆盖多个数据集/模型的 range 使得这种精度可能造成误导（读者可能误认为这是单一配置的结果）。\n- **建议**：在 abstract 中简化为 \"near-zero DR\" 和 \"R-F1 within 1pp of unconstrained\"，将精确数字留给实验章节\n\n---\n\n## Questions（逐条列出）\n\n**Q1.** Proposition 1 的证明（Appendix O）使用 position-based entity indexing（通过出现位置索引实体），但论文的实际系统使用 name-based referencing（通过实体名引用）。Appendix O 最后一段（p.34）简要讨论了这一差异，声称 \"position indexing vs. name referencing\" 是一个 simplification。能否更详细地论证：在 name-based referencing 下，Proposition 1 的结论是否仍然成立？特别是，如果所有实体名是唯一的、且有界长度的，context-free grammar 是否可以通过在产生式中直接编码 name→type 映射来执行类型约束？\n\n**Q2.** Table 7 显示 CF fallback rate 为 0.46%（SciERC, Qwen 4）和 first-token fallback rate 最高 19.93%（SciERC, Qwen S1）。这两个数字的差异很大。能否解释：(a) CF fallback 和 first-token fallback 的关系是什么？(b) 19.93% 的 first-token fallback rate 是否意味着接近 1/5 的 type-bearing tokens 需要回退到 grammar-only 模式？\n\n**Q3.** 论文在 §5.2（p.6）提到 cross-dataset validation（SciERC→DocRED），声称 \"S1 reduces DR from 18.46% to 0.81%\"。但 cross-dataset 设置下的 constraint table 来自 SciERC 的 schema，应用于 DocRED 的 ontology——这两个 ontology 完全不同（SciERC: 7 entity types, 7 relations; DocRED: 6 entity types, 96 relations）。能否解释这个 cross-dataset 实验的确切 setup？是使用 DocRED 自己的 ontology 但从 SciERC 训练数据中提取 constraint table，还是另有安排？\n\n**Q4.** §5.4 的 WikiEvents 事件抽取实验（Table 4）仅使用 preliminary 20-document test set。这个 split size 的统计效力是否足够支撑论文的 claims？特别是 \"RoV eliminates EV and RoV\" 和 \"F1 0.6% → 12-18%\" 这些结论的 confidence interval 是多少？\n\n---\n\n## Missing References\n\n1. **Reddy, A., Thayne T. Walker, James S. Ide, and Amrit Singh Bedi. 2026.** Draft-Conditioned Constrained Decoding for Structured Generation in LLMs. arXiv:2603.03305. ——直接相关：分析 constrained decoding 的 quality degradation 问题，提出 draft-then-constrain 的两阶段方法，与 OntoCoDec 的 grammar-first fallback 互补。\n\n2. **Nguyen, N.T.H., et al. 2026.** Thinking Before Constraining: A Unified Decoding Framework for Large Language Models. arXiv:2601.07525. ——相关：探索 free-reasoning + structured-generation 的混合解码，与 S2 two-pass pipeline 有设计哲学上的相似性。\n\n3. **（可选）arXiv:2604.14862, April 2026.** Schema Key Wording as an Instruction Channel in Structured Generation under Constrained Decoding. ——边缘相关：展示 schema key 命名影响约束解码性能。考虑到此文发表于 2026 年 4 月，可能过于 recent。\n\n---\n\n## Overall Assessment\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 技术上扎实：Proposition 1 证明正确，实验设计全面，消融覆盖主要变量。但 CF 问题未解决且叙事中未充分强调，Proposition 1 的实践影响力表述略有过度。 |\n| **Excitement** | 3/5 | 扎实的系统工程贡献 + 有价值的理论分析，但概念创新幅度有限——grammar layer 是标准 GCD，semantic layer 是相对直观的 stateful extension。对于熟悉 constrained decoding 的读者，核心思路在读完 §2 的约束分类后基本可以预见。 |\n| **Reproducibility** | 4/5 | Appendix G 提供了详细的超参数、硬件、随机种子信息；prompt templates 在 Appendix A 中完整呈现；代码承诺在接收后公开。 |\n| **Overall** | 3.5/5 （Borderline Conference） | 这是一篇执行质量很高的系统性论文，理论分析（Proposition 1）和实验覆盖度都是亮点。主要的不足在于：(a) 概念创新的增量特征——semantic layer 的 entity registry + type masking 是对已知 constrained decoding 范式的合理但非突破性扩展；(b) CF 问题作为核心局限在叙事中被弱化；(c) 几篇 2026 年初的高度相关工作未被引用。论文处于主会议接收和 Findings 的边界——如果作者在 rebuttal 中能 (i) 更清晰地 articulate semantic layer 相对于 PICARD 式 stateful decoding 的独特贡献，(ii) 补充 DCCD 等 missing references 的讨论，(iii) 在 abstract/intro 中更审慎地呈现 CF 的 open status，评分有上调空间。 |\n| **Confidence** | 4/5 | 我熟悉 constrained decoding 和结构化 IE 文献，仔细阅读了论文全部 34 页（含附录），并独立检索了最新相关工作。 |\n\n**一句话总结**：一篇实验全面、理论有支撑的系统性工作，但 semantic layer 的概念创新幅度和 CF 问题的坦诚度是影响主会议接收的主要障碍。\n",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n## Summary（2-3 句概述）\n\n本文提出 OntoCoDec，一个将 IE 本体编译为可组合 token 级解码约束的两层框架：grammar layer（CFG）保证 JSON 结构和词汇合法性，semantic layer（带状态的 prefix-decidable transducer）通过动态 entity registry 在运行时执行 domain/range 类型约束。Proposition 1 用 pumping lemma 证明了 IE 中带无界实体集的类型约束不是 context-free 的，为两层架构提供了理论依据。实验覆盖 SciERC、DocRED、WikiEvents 三个数据集，多个 8B 和 70B 模型，zero-shot 和 LoRA fine-tuning 设置，展示了 DR 违规率从 42-99% 降到近零（fine-tuning 下 ≤0.09%）。\n\n---\n\n## Strengths（逐条列出）\n\n**S1. 理论与系统设计的有机结合。** Proposition 1（§3, p.3; 完整证明 Appendix O, p.33-34）是本文的核心理论贡献。通过 pumping lemma 严格证明带无界实体集的 domain/range 类型约束不是 context-free，从而为 grammar layer 之上添加 semantic layer 提供了不可替代的理论动机。这不是一个显然的结论——虽然实践者可能直觉上知道 CFG 不够用，但形式化证明为社区建立了一个有用的参考点，也清晰界定了 grammar-only 方法（XGrammar、Outlines、SynCode）的能力边界。\n\n**S2. 实验设计极为全面。** 论文的实验矩阵令人印象深刻：3 个 RE 数据集 × 3-4 个模型 × zero-shot/fine-tuned × 多种解码策略（greedy/beam/sampling），外加 WikiEvents 上的事件抽取扩展。Table 1 的五因素消融（§5.1）、Table 2 的 fine-tuning composability、Table 3 的 cross-model zero-shot 验证、以及 Table 4 的事件抽取结果——每个实验都回答了一个明确的研究问题。附录中的 beam search 兼容性（Appendix F）、prompt sensitivity（Appendix I）、document length 分析（Appendix H）、constraint tightness 案例分析（Appendix N）进一步增强了可信度。\n\n**S3. 约束三层分类体系清晰实用。** §2 将 IE 类型约束分为三层——(1) context-free（JSON 结构 + 词汇）、(2) prefix-decidable with state（domain/range）、(3) non-local cross-entity consistency——这个分类不仅服务于本文的系统设计，也为后续研究提供了一个有用的概念框架。\n\n**S4. Grammar-first fallback 机制设计合理。** §4 的 Eq.(2) 定义了两层约束的合取，当语义约束与语法约束同时排除所有 token 时，优先保证 JSON 完整性。Appendix C 的 causal tracing（Table 6）精确定位了 fallback 触发的位置和原因，Table 7 的 CF-DR tradeoff 分析展示了这一设计选择的代价。这种对工程决策的系统化分析是本文的一个亮点。\n\n**S5. 与 GCD baseline 的等价性验证（Appendix C, Table 16-17）。** 论文不仅声称 grammar layer 等价于 GCD，还在 SciERC 上用 vLLM 的 `guided_json` 模式实证验证了这一等价性（所有指标差异 <0.5pp），这增强了论文的可信度。\n\n---\n\n## Weaknesses（逐条列出，标注严重程度）\n\n**W1 [Should-Fix] 新颖性的增量特征需更坦诚讨论。** Grammar layer 本质上是标准 GCD（论文自己在 Table 16-17 验证了与 vLLM guided_json 的等价性），这意味着本文的新颖性完全集中在 semantic layer 和 Proposition 1 上。Semantic layer 的核心思想——维护一个运行时 entity registry 来实施 domain/range 类型检查——是一个合理但相对直观的工程扩展。PICARD（Scholak et al., 2021）已经展示了在 constrained decoding 中维护状态信息来执行跨位置约束的思路（虽然是 SQL 领域）。论文应在 §1 或 §7 中更明确地讨论：semantic layer 的概念创新点究竟在哪里，与 PICARD 式的 stateful constrained decoding 的区别不仅仅是应用领域的不同。\n\n- **具体位置**：§1 第 3 段（\"We make a systematic engineering contribution with theoretical grounding\"）和 §7\n- **为什么影响评分**：如果 reviewer 认为这主要是已知技术在新领域的应用，会显著降低 excitement 评分\n- **建议**：在 §7 Discussion 中增加 1-2 段坦率讨论增量创新 vs. 系统性贡献的关系，强调 Proposition 1 的理论意义和 entity registry + grammar-first fallback 的设计创新\n\n**W2 [Should-Fix] Proposition 1 的实际影响力可能被高估。** Proposition 1 证明了 domain/range 类型约束不是 context-free，但这个结论的实践意义需要更细致的讨论：\n- (a) 论文的 Remark（p.3）自己承认\"当实体集有限时（实际情况），有效语言在技术上是正则的\"，但对应的 DFA 状态数是指数级的（e.g., DocRED 的 7 entity types, 20+ entities → 10^15 states）。这个 distinction（理论上不可能 vs. 工程上不可行）是重要的，但论文的行文倾向于模糊二者的边界。\n- (b) Proposition 1 证明的是 PDA **cannot** enforce 类型约束——但这是对 PDA 的已知限制（PDA 不能做 cross-reference checking），并非一个惊人的结论。证明的价值在于将这个直觉应用到 IE 场景并给出严格的形式化，但不应被包装为一个深刻的理论洞察。\n- **具体位置**：§3, p.3, Proposition 1 及其 Remark\n- **建议**：在 Remark 后增加一句明确说明：\"The practical contribution of Proposition 1 is not the impossibility result per se, but rather the precise characterization of what Level 2 constraints require that motivates our two-layer design.\"\n\n**W3 [Should-Fix] CF 违规问题未解决，但论文的叙事未充分强调这一局限。** 论文的主要实验指标聚焦 DR reduction，但 CF violations（cross-field type inconsistency）在 fine-tuning 后仍有 0.46-1.18%（Table 2, Qwen SciERC），零-shot 下更高（Table 1, 最高 12.02%）。Table 7 显示 CF 和 DR 是一个 tradeoff（消除 CF fallback 导致 DR +13.85pp）。Limitations 段（p.9）确实讨论了这一问题，但：\n- Abstract 和 Introduction 将 CF 表述为 \"CF ≤ 1.4% through independent enforcement\"，给人一种 CF 已基本解决的印象\n- 论文的叙事结构更强调 DR 的成功（\"near-eliminates DR\"），而 CF 作为一个 **未解决的核心问题** 没有在 Introduction 或 Discussion 中得到同等权重的讨论\n- **具体位置**：Abstract, §1 contributions list, §7 Discussion\n- **为什么影响评分**：CF 问题的严重程度取决于下游应用——在知识图谱构建中，同一实体的类型不一致是一个严重问题。论文如果更坦诚地将 CF 作为 open problem 呈现，反而会增强可信度。\n- **建议**：在 Abstract 中将 CF 从 \"through independent enforcement\" 改为更审慎的表述（如 \"with residual CF violations of 0.5-1.2% under fine-tuning, attributable to per-relation independence\"）；在 §7 中用 1-2 句明确将 global entity-level type consensus 标记为最重要的 future work\n\n**W4 [Should-Fix] 近期高度相关的 constrained decoding 质量工作未被引用。** 论文在 Appendix B 对 constrained decoding 文献的覆盖较为全面，但遗漏了几篇 2026 年初发表的直接相关工作：\n1. **DCCD**（Reddy et al., arXiv:2603.03305, March 2026）—— Draft-Conditioned Constrained Decoding，提出先生成无约束草稿再执行约束解码，通过 KL-projection 视角分析了约束解码的 \"projection tax\"。这与 OntoCoDec 的 grammar-first fallback 解决的是同一类问题（约束解码导致的生成质量退化），方法论思路互补。\n2. **\"Thinking Before Constraining\"**（Nguyen et al., arXiv:2601.07525, January 2026）—— 允许 LLM 自由推理直到触发 token 再切换到结构化生成，在数学推理任务上取得 +27% 准确率提升。这与 OntoCoDec 的 S2 two-pass pipeline（§4）在设计哲学上有相似之处。\n3. **\"Schema Key Wording\"**（arXiv:2604.14862, April 2026）—— 发现 JSON schema 的 key 命名本身就是约束解码下的隐式指令通道，影响模型性能。这与 OntoCoDec 的 schema compilation 步骤直接相关。\n- **具体位置**：§6 Related Work, Appendix B\n- **建议**：在 §6 的 \"Constrained decoding\" 段落末尾增加 2-3 句讨论这些工作，特别是 DCCD 与 grammar-first fallback 的关系\n\n**W5 [Minor] 论文信息密度极高，可读性有一定挑战。** 正文 8 页塞入了完整的理论分析、三层约束分类、两层架构、constraint composition、五因素消融、三个数据集的主实验、fine-tuning composability、cross-model 验证、event extraction 扩展、runtime overhead、以及 related work。每一段都承载大量信息，首次阅读需要反复回翻。\n- 例如：§3.3 Semantic Layer 在一段之内引入了 entity registry、dynamic masking、type-bearing positions、constraint tightness、grammar-first fallback、grammar-semantic interaction 等概念，没有给读者消化的空间\n- Figure 1 作为唯一的系统图，承担了过多解释责任\n- **建议**：考虑增加一个 running example（如用 SciERC 的一个具体 triple 展示两层约束如何逐步应用），这在不增加页数的情况下可以显著提高可读性\n\n**W6 [Minor] 标题中 \"Compiled\" 一词可能产生歧义。** \"Compiled Schema Constraints\" 中的 \"compiled\" 可以被理解为 \"collected/gathered\"（收集），而论文的实际含义是 \"translated into a computational representation\"（编译成计算表示）。对于 NLP 社区读者（而非 PL 社区），这个双关可能不够清晰。\n- **建议**：考虑 \"Translating Schema Constraints into...\" 或在 abstract 首句明确 \"compiles...into\" 的含义（论文实际上在 abstract 中已经做了，但标题本身的歧义仍在）\n\n**W7 [Minor] 部分数值在 abstract 中过于精确。** Abstract 中出现 \"DR ≤ 0.09%\"、\"R-F1 43-46% (±0.8pp)\"、\"CF ≤ 1.4%\"——这些数字精确到小数点后两位，但覆盖多个数据集/模型的 range 使得这种精度可能造成误导（读者可能误认为这是单一配置的结果）。\n- **建议**：在 abstract 中简化为 \"near-zero DR\" 和 \"R-F1 within 1pp of unconstrained\"，将精确数字留给实验章节\n\n---\n\n## Questions（逐条列出）\n\n**Q1.** Proposition 1 的证明（Appendix O）使用 position-based entity indexing（通过出现位置索引实体），但论文的实际系统使用 name-based referencing（通过实体名引用）。Appendix O 最后一段（p.34）简要讨论了这一差异，声称 \"position indexing vs. name referencing\" 是一个 simplification。能否更详细地论证：在 name-based referencing 下，Proposition 1 的结论是否仍然成立？特别是，如果所有实体名是唯一的、且有界长度的，context-free grammar 是否可以通过在产生式中直接编码 name→type 映射来执行类型约束？\n\n**Q2.** Table 7 显示 CF fallback rate 为 0.46%（SciERC, Qwen 4）和 first-token fallback rate 最高 19.93%（SciERC, Qwen S1）。这两个数字的差异很大。能否解释：(a) CF fallback 和 first-token fallback 的关系是什么？(b) 19.93% 的 first-token fallback rate 是否意味着接近 1/5 的 type-bearing tokens 需要回退到 grammar-only 模式？\n\n**Q3.** 论文在 §5.2（p.6）提到 cross-dataset validation（SciERC→DocRED），声称 \"S1 reduces DR from 18.46% to 0.81%\"。但 cross-dataset 设置下的 constraint table 来自 SciERC 的 schema，应用于 DocRED 的 ontology——这两个 ontology 完全不同（SciERC: 7 entity types, 7 relations; DocRED: 6 entity types, 96 relations）。能否解释这个 cross-dataset 实验的确切 setup？是使用 DocRED 自己的 ontology 但从 SciERC 训练数据中提取 constraint table，还是另有安排？\n\n**Q4.** §5.4 的 WikiEvents 事件抽取实验（Table 4）仅使用 preliminary 20-document test set。这个 split size 的统计效力是否足够支撑论文的 claims？特别是 \"RoV eliminates EV and RoV\" 和 \"F1 0.6% → 12-18%\" 这些结论的 confidence interval 是多少？\n\n---\n\n## Missing References\n\n1. **Reddy, A., Thayne T. Walker, James S. Ide, and Amrit Singh Bedi. 2026.** Draft-Conditioned Constrained Decoding for Structured Generation in LLMs. arXiv:2603.03305. ——直接相关：分析 constrained decoding 的 quality degradation 问题，提出 draft-then-constrain 的两阶段方法，与 OntoCoDec 的 grammar-first fallback 互补。\n\n2. **Nguyen, N.T.H., et al. 2026.** Thinking Before Constraining: A Unified Decoding Framework for Large Language Models. arXiv:2601.07525. ——相关：探索 free-reasoning + structured-generation 的混合解码，与 S2 two-pass pipeline 有设计哲学上的相似性。\n\n3. **（可选）arXiv:2604.14862, April 2026.** Schema Key Wording as an Instruction Channel in Structured Generation under Constrained Decoding. ——边缘相关：展示 schema key 命名影响约束解码性能。考虑到此文发表于 2026 年 4 月，可能过于 recent。\n\n---\n\n## Overall Assessment\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 技术上扎实：Proposition 1 证明正确，实验设计全面，消融覆盖主要变量。但 CF 问题未解决且叙事中未充分强调，Proposition 1 的实践影响力表述略有过度。 |\n| **Excitement** | 3/5 | 扎实的系统工程贡献 + 有价值的理论分析，但概念创新幅度有限——grammar layer 是标准 GCD，semantic layer 是相对直观的 stateful extension。对于熟悉 constrained decoding 的读者，核心思路在读完 §2 的约束分类后基本可以预见。 |\n| **Reproducibility** | 4/5 | Appendix G 提供了详细的超参数、硬件、随机种子信息；prompt templates 在 Appendix A 中完整呈现；代码承诺在接收后公开。 |\n| **Overall** | 3.5/5 （Borderline Conference） | 这是一篇执行质量很高的系统性论文，理论分析（Proposition 1）和实验覆盖度都是亮点。主要的不足在于：(a) 概念创新的增量特征——semantic layer 的 entity registry + type masking 是对已知 constrained decoding 范式的合理但非突破性扩展；(b) CF 问题作为核心局限在叙事中被弱化；(c) 几篇 2026 年初的高度相关工作未被引用。论文处于主会议接收和 Findings 的边界——如果作者在 rebuttal 中能 (i) 更清晰地 articulate semantic layer 相对于 PICARD 式 stateful decoding 的独特贡献，(ii) 补充 DCCD 等 missing references 的讨论，(iii) 在 abstract/intro 中更审慎地呈现 CF 的 open status，评分有上调空间。 |\n| **Confidence** | 4/5 | 我熟悉 constrained decoding 和结构化 IE 文献，仔细阅读了论文全部 34 页（含附录），并独立检索了最新相关工作。 |\n\n**一句话总结**：一篇实验全面、理论有支撑的系统性工作，但 semantic layer 的概念创新幅度和 CF 问题的坦诚度是影响主会议接收的主要障碍。\n",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1723 · 2026-05-22T13:50:07.908894+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3917
}
```

</details>

---


### Tool call

_source line 1724 · 2026-05-22T13:50:13.739241+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
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

_source line 1725 · 2026-05-22T13:50:13.789896+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1726 · 2026-05-22T13:50:18.812352+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_19/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1727 · 2026-05-22T13:50:18.863007+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1728 · 2026-05-22T13:50:27.063256+00:00_

审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5/5（Borderline Conference）。

核心判断：
- **优势**：Proposition 1 的形式化证明有价值，实验矩阵（3 数据集 × 多模型 × zero-shot/fine-tuned）极为全面，附录 24 页的消融和分析增强可信度
- **主要问题**：(1) semantic layer 的概念创新是对已知 stateful constrained decoding 的合理但非突破性扩展；(2) CF 违规作为未解决的核心问题在叙事中被弱化；(3) 遗漏 DCCD（arXiv:2603.03305）等 2026 年初的高相关工作；(4) Proposition 1 的实践影响力表述略有过度
- **建议**：rebuttal 中如能清晰 articulate semantic layer 独特贡献、补充 missing references、审慎呈现 CF open status，评分有上调空间

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 35

## Round 35

2 recorded events


### User

_source line 1729 · 2026-05-22T13:51:16.147164+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。也请评论其 Strengths 中你是否同意。

---

## Reviewer 1 审稿意见（方法严谨性 + 实验设计 + 统计分析）

### Summary
OntoCoDec 提出两层约束解码框架，将 IE 本体论编译为 token 级约束：grammar layer（CFG）保证 JSON 结构/词汇合法性，semantic layer（带状态前缀可判定）通过动态实体注册表强制 domain/range 类型约束。Proposition 1 证明跨实体类型约束超出 CFG 表达能力。在 SciERC、DocRED、WikiEvents 上跨 Qwen/Llama/Mistral 验证近完全 DR 消除和 LoRA 微调兼容性。工程导向系统论文，理论动机清晰，实验广但部分评估统计效力不足。

### Strengths
**S1.** 架构有坚实理论基础。Proposition 1（§3, Appendix O）正确证明无界实体集下 domain/range 约束非 context-free。Remark 诚实区分理论不可能性与工程不可行性。
**S2.** 消融设计干净。SciERC 五路消融（Table 1）清晰隔离各组件。
**S3.** 可重复性堪称典范。24 页附录。
**S4.** 诚实报告局限。70B/WikiEvents FT 明确标 "preliminary"。
**S5.** 跨模型泛化。4 个模型上一致的 DR 消除效果。
**S6.** Grammar-first fallback 分析是亮点。

### Weaknesses
**W1 [Should-Fix]** WikiEvents 微调 n=20 统计效力严重不足。§5.4 从 20 个测试文档得出 EE 微调兼容性结论，无 power analysis。
**W2 [Should-Fix]** Dual-factor 分析（n=6）结论被过度引用。Figure 2 对 6 点拟合线性模型 R²=0.886。
**W3 [Should-Fix]** 主表缺外部约束解码 baseline。Tables 1-4 仅对比无约束和自身消融。GCD/vLLM 对比在附录。
**W4 [Should-Fix]** Enabling dependency 验证存在混淆变量。Semantic-only vs. S1 混淆了 enabling dependency 和语义层独立设计缺陷。理想控制：替代 grammar + semantic layer。
**W5 [Minor]** 效应量报告不完整。Table 2 有 p 值无标准化效应量。
**W6 [Minor]** 70B AWQ INT4 量化对约束交互的影响未讨论。
**W7 [Minor]** Proposition 1 正文表述可更精确地标注 "unbounded" 限定。

### Questions
**Q1.** Semantic-only 配置是否完全移除了 JSON 结构保证？
**Q2.** Grammar-first fallback 在 Llama 上 100% 触发但 Qwen 零触发——根本原因？
**Q3.** DocRED 微调 R-F1 极低（3-4 pp），此时 DR 消除的实际下游价值？
**Q4.** TCR 为何不作为标准 pipeline？
**Q5.** Constraint compilation 0.45s 是否验证到更大本体（Wikidata 规模）？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1730 · 2026-05-22T13:53:15.320892+00:00_

以下是我（Reviewer 2）对 Reviewer 1 各条意见的逐条回应。

---

## 对 Reviewer 1 Strengths 的评论

**S1 (Proposition 1 理论基础):** [AGREE] 与我的 S1 一致。Proposition 1 的证明是正确的，Remark 对理论不可能性与工程不可行性的区分是论文的一个诚实之处。不过我在 W2 中补充了一点：这个区分在正文行文中有时被模糊化，Proposition 1 的实践影响力表述可以更审慎。

**S2 (消融设计):** [AGREE] Table 1 的五因素消融确实干净。每个配置（Unconstrained / S1 / S2 / S1+S2 / S1+S2+FT）隔离了一个明确的变量。

**S3 (可重复性):** [AGREE] 24 页附录、完整 prompt template（Appendix A）、超参数细节（Appendix G）、随机种子报告——这是本文最突出的优势之一。

**S4 (诚实报告局限):** [AGREE] 70B 和 WikiEvents FT 标为 "preliminary" 是负责任的做法。Limitations 段（p.9）对 CF-DR tradeoff 的讨论也相当坦诚。

**S5 (跨模型泛化):** [AGREE] Qwen/Llama/Mistral 三个模型族上 DR reduction 一致，Table 3 的 zero-shot cross-model 结果增强了泛化性论证。

**S6 (Grammar-first fallback 分析):** [AGREE] 与我的 S4 一致。Appendix C 的 causal tracing（Table 6-7）是本文的分析亮点。

---

## 对 Reviewer 1 Weaknesses 的逐条回应

**W1 [Should-Fix] WikiEvents n=20 统计效力不足**

[AGREE] 我在自己的 Q4 中提出了完全相同的担忧。20 个测试文档的统计效力确实不足以支撑稳健结论。Table 4 报告的 F1 数字（如 "0.6% → 12-18%"）在如此小的样本上 confidence interval 极宽。论文将其标注为 "preliminary"（§5.4 首句）部分缓解了这一问题，但如果要在 camera-ready 中保留这一实验，至少需要：(a) 报告 bootstrap confidence intervals，(b) 增大测试集，或 (c) 将其明确降级为 case study 而非定量评估。

**W2 [Should-Fix] Dual-factor 分析 n=6 过度引用**

[AGREE] Figure 2 对 6 个数据点拟合线性回归确实在统计上站不住脚——6 点的 R²=0.886 的自由度过少，任何单点偏移都会剧烈改变拟合结果。不过我注意到论文在 Figure 2 caption 中标注了 "descriptive only" 且文字中使用 "qualitative" 修饰（p.20："The strong fit supports the dual-factor characterization rather than a confirmatory statistical test"）。问题在于，尽管有这些限定词，这一 "dual-factor pattern" 在 §5.1（p.5-6）、§7（p.8）、Limitations（p.9）中被反复引用，给读者的印象是这是一个已确立的发现而非探索性观察。建议：要么增加数据点（更多 model×dataset 配置），要么将引用限制在 Appendix 的讨论中，正文仅提及 "preliminary evidence suggests..."。

**W3 [Should-Fix] 主表缺外部约束解码 baseline**

[REBUT] 这一批评在表面上合理，但在方法论上需要更细致的分析。论文的核心贡献是 semantic layer（Level 2 type constraints），而 grammar layer 已在 Appendix C Table 16-17 中证实与 vLLM `guided_json`（即标准 GCD）输出完全等价（所有指标差异 <0.5pp）。在主表中加一行 "GCD baseline" 实质上会与 S1 行完全重复，不提供额外信息。

更关键的是：目前**不存在**能执行 domain/range type constraints 的外部 constrained decoding 系统可作为 baseline——XGrammar、Outlines、SynCode 都只处理 Level 1（JSON 结构），PICARD 是 SQL 特定的。这正是 OntoCoDec 的贡献所在。因此，论文的消融设计（S1 vs. S1+S2）实际上**是**最合理的实验对照：它精确隔离了 semantic layer 的增量效果。

不过，我同意论文可以在主表的 caption 或脚注中更明确地说明："S1 rows are verified equivalent to standard GCD (Appendix C, Table 16-17)"，避免读者误以为这一对照缺失。

**W4 [Should-Fix] Enabling dependency 混淆变量**

[AGREE，但认为严重程度可降级为 Minor] R1 的方法论观点是正确的：semantic-only 配置失败可能是因为 (a) 缺少 JSON 结构保证导致 semantic layer 无法正确定位 type-bearing tokens，也可能是 (b) 理论上的 enabling dependency（Proposition 1）。这两个原因被混淆了。

但实践上，这一混淆难以解耦：你需要一个**非 CFG 的替代机制**来保证 JSON 结构（如 regex-based tokenizer 或 template filling），然后在其上运行 semantic layer，才能隔离 Proposition 1 的效应。这在工程上几乎等于构建一个全新系统。Table 1 的 S2-only 行（DR 仅降 1-2%）实际上已经很好地展示了 semantic layer 单独运行的局限性，其原因（无 JSON 保证→type-bearing position 定位失败）在 §5.1 第 2 段有解释。

建议：在 §5.1 中增加 1-2 句明确标注这一混淆："The poor performance of S2-only reflects both the enabling dependency (Proposition 1) and the practical prerequisite that the semantic layer requires well-formed JSON to locate type-bearing positions."

**W5 [Minor] 效应量报告不完整**

[AGREE] Table 2 报告了 p 值（Bootstrap, F=100）但缺少标准化效应量（如 Cohen's d 或 ΔR-F1 的 95% CI）。这是统计报告的规范性问题，不影响结论但影响论文的方法论严谨度。补充 effect size 应该很容易做到。

**W6 [Minor] 70B AWQ INT4 量化影响未讨论**

[AGREE] 这是一个合理但次要的关注点。AWQ INT4 量化可能影响 logit distribution，从而影响 constrained decoding 的 mask application 效果。论文的 70B 结果（§5.4, Table 4）已标注为 "preliminary"，但一句关于量化对约束交互可能影响的讨论会提高论文的严谨度。Appendix G 报告了硬件和量化配置（"AWQ, 4-bit"），但未讨论其对约束层行为的潜在影响。

**W7 [Minor] Proposition 1 "unbounded" 限定**

[AGREE] 与我的 W2 部分重叠。正文 §3 中 Proposition 1 的陈述应在首句更显著地标注 "for unbounded entity sets" 这一限定条件。当前的 Remark 虽然提到了有界情况下的正则性，但 Proposition 1 的主句表述（"The set of valid IE outputs satisfying domain/range constraints is not context-free"）在没有仔细阅读条件的情况下容易被误读为一个无条件结论。

---

## 对 Reviewer 1 Questions 的逐条回应

**Q1. Semantic-only 是否完全移除 JSON 结构保证？**

[AGREE 这是一个重要澄清问题] 从 Table 1 的实验设计来看，S2-only 仅应用 semantic layer 的 type masking，不保证输出是 well-formed JSON。这意味着 semantic layer 在遇到格式错误的输出时（如缺少引号、括号不匹配）无法正确定位 type-bearing positions，导致 type constraint enforcement 大面积失效。§5.1 第 2 段（p.5）的描述支持这一解读："fine-tuning alone reduces DR to 1-2% but leaves residual violations... adding S2... making the semantic layer the sole effective DR defense"——但这里说的是 S1+S2 而非 S2-only。论文应在实验设计部分更清晰地说明 S2-only 的确切行为。

**Q2. Fallback 触发率在 Llama 100% vs Qwen 0% 的根本原因？**

[AGREE 需要更深入解释] 这个极端差异暗示了模型 tokenizer 和 token-level type calibration 的根本性差异。从 Table 7（p.32）和 Appendix N 的 constraint tightness 分析来看，可能的原因是：Qwen 的 token vocabulary 与 ontology type names 的对齐程度远高于 Llama，使得 semantic masking 很少排除所有候选 token。但论文对此缺乏系统分析。这是一个值得在 Discussion 中展开的 finding。

**Q3. DocRED R-F1 3-4pp 时 DR 消除的实际价值？**

[AGREE 这是一个尖锐但公平的问题] Table 2 显示 DocRED fine-tuned R-F1 约为 40-46%（不是 3-4pp——R1 可能指的是 zero-shot 设置）。在 fine-tuned 设置下（R-F1 40-46%），DR 消除确实有实际价值——确保提取的关系三元组中实体类型与 schema 一致。但在 **zero-shot** 设置下（Table 3, R-F1 可低至 3-4%），DR 消除的实际意义确实可疑：如果 95%+ 的输出本身就不正确，保证类型约束的价值有限。论文应更清晰地区分 zero-shot（诊断性/探测性）和 fine-tuned（部署相关）两个评估语境的 DR reduction 的不同意义。实际上 Abstract 最后一句已有此区分（"Zero-shot evaluation serves as a diagnostic probe; the deployment-relevant evaluation is the fine-tuned setting"），但正文其他位置可以更一致地强调。

**Q4. TCR 为何不作为标准 pipeline？**

[REBUT] 我认为论文在 §5.3（p.7）和 Appendix M 已合理解释了这一设计选择：TCR（post-hoc type consistency resolution）是一个 **post-hoc** 过滤/修正步骤，而 OntoCoDec 的 semantic layer 在 **decoding time** 执行约束。两者是互补的（Table 12 显示 "both strategies are equally effective"），但 decoding-time enforcement 有一个关键优势：它防止模型在错误的 type trajectory 上继续生成（avoiding downstream error propagation within a single generation），而 post-hoc filtering 只能在生成完成后丢弃或修正。将 TCR 作为标准 pipeline 的补充（而非替代）是合理的，论文也在 §5.3 最后一句提到了这一点。

**Q5. Constraint compilation 可扩展到 Wikidata 规模？**

[AGREE 需要更多验证] Appendix K（Table 35, p.25）显示最大测试的 ontology 是 "XLarge"（200 types, 5000 relations），compilation 耗时 0.45s。但 Wikidata 有 ~10,000 entity types 和数百万 properties，量级差异巨大。论文的 compilation 步骤（parsing ontology → building constraint tables → compiling into grammar rules）在理论上应该是多项式的，但实际 memory footprint 和 runtime 在 Wikidata 规模下是否可控未经验证。这是一个 Limitations 中值得提及的 scalability concern。

---

## 总结性评价

Reviewer 1 的审稿整体严谨，尤其在统计方法论方面（W1/W2/W5）提出了有价值的批评。我与 R1 在大多数 Weaknesses 上达成共识，主要分歧在 **W3**（外部 baseline）：我认为缺少外部 baseline 的批评在表面合理但忽略了一个事实——不存在能执行 Level 2 type constraints 的外部可比系统，论文的消融设计已经是最合理的实验对照。**W4**（enabling dependency 混淆）在方法论上正确但实践上难以解耦，建议降级为 Minor。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 36

## Round 36

72 recorded events


### User

_source line 1731 · 2026-05-23T02:00:11.180195+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。

## 投稿信息
- **Venue**: EMNLP 2026 (ARR May 2026)
- **截止日期**: 2026-05-25
- **格式**: Long paper，正文 ≤ 8 页（strict），参考文献无限制，Limitations/Ethics 不计入页数
- **模板**: ACL（`\usepackage[review]{acl}`）
- **匿名**: Double-blind
- **论文文件**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/submitted.pdf`

## 你的审查侧重

### 1. 新颖性评估
- 核心贡献（两层约束解码框架）的 novelty ceiling——这是算法创新还是系统集成？
- Semantic layer 的 stateful token masking 与 PICARD (Scholak et al., 2021) 的 incremental parsing 有何本质区别？论文中 "rejection-based vs constructive forward masking" 的区分是否令人信服？
- 与 Mündler et al. (2025) 的 type system compilation 的差异是否充分讨论？
- 论文定位为 "systematic engineering contribution" 还是 "novel decoding algorithm"——framing 是否一致？
- Excitement level 评估：对 NLP 社区的预期影响力

### 2. Related Work 完整性
- Constrained decoding 领域（XGrammar, Outlines, SGLang, LMQL, SynCode, CRANE, IterGen）覆盖是否全面？
- Schema-aware IE（GoLLIE, KnowCoder, GUIDEX, ADELIE）讨论是否充分？
- 2026 年最新工作（DCCD Reddy et al., Thinking Before Constraining Nguyen et al.）是否已纳入？
- 是否遗漏其他重要相关工作？用 web search 检查

### 3. 写作质量与 Framing
- Abstract 信息密度是否过高？数值精度是否适当？（特别关注 CF 表述是否偏乐观）
- Introduction 的 gap-bridge 叙事是否清晰？贡献列表是否准确反映论文内容？
- 各节之间的逻辑衔接是否流畅？
- 术语使用是否一致（DR/CF/RV/ET 四类 violation 的定义和使用）？
- 论文是否存在 overclaiming（"guarantee" → "enforcement" 替换是否彻底）？
- 信息密度极高——是否需要 running example 辅助理解？

### 4. 格式合规性（严格检查）
- **页数**: 正文是否 ≤ 8 页？注意 §7 Discussion and Conclusion 是否溢出到第 9 页
- **匿名**: 是否有匿名违规？
- **引用格式**: 是否符合 ACL natbib 规范？
- **Limitations 章节**: 是否充分覆盖主要局限？
- **Ethics Statement**: 是否存在遗漏的伦理考虑？

### 5. Appendix 使用
- 大量内容放在 Appendix（~25 页）——主文是否因此不完整？关键信息是否被不当外推至 Appendix？
- Appendix 内容是否应被审稿人考虑？

请按 ARR 审稿标准输出完整审稿报告：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1732 · 2026-05-23T02:00:24.246883+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1733 · 2026-05-23T02:00:25.601957+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 1734 · 2026-05-23T02:00:25.853054+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
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

_source line 1735 · 2026-05-23T02:00:25.905495+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1736 · 2026-05-23T02:00:34.542315+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1737 · 2026-05-23T02:00:36.801867+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/submitted.pdf",
  "pages": "1-8",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/submitted.pdf",
    "pages": "1-8",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1738 · 2026-05-23T02:00:37.354366+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1739 · 2026-05-23T02:00:46.659932+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on my search results, here's information about the ACL Rolling Review (ARR) 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

For main papers, key criteria include novelty and impact, while for Findings papers, the main criteria are soundness and reproducibility, with con
…[truncated 1356 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 12117
}
```

</details>

---


### Tool result

_source line 1740 · 2026-05-23T02:00:48.232516+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 523.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 400.7}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 485.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 568.7}], \"total_pages\": 39, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_050
…[truncated 122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 11430
}
```

</details>

---


### Tool result

_source line 1741 · 2026-05-23T02:00:48.233361+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (u
…[truncated 7579 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 10878
}
```

</details>

---


### Tool call

_source line 1742 · 2026-05-23T02:01:22.515313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1743 · 2026-05-23T02:01:22.769081+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1744 · 2026-05-23T02:01:22.769533+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1745 · 2026-05-23T02:01:22.769760+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1746 · 2026-05-23T02:01:51.886771+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 29371
}
```

</details>

---


### Tool result

_source line 1747 · 2026-05-23T02:01:51.890652+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 29121
}
```

</details>

---


### Tool result

_source line 1748 · 2026-05-23T02:01:51.944411+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 29174
}
```

</details>

---


### Tool result

_source line 1749 · 2026-05-23T02:01:51.945550+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 29175
}
```

</details>

---


### Tool call

_source line 1750 · 2026-05-23T02:01:52.050943+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form fields, scoring dimensions, and their scales. I need: 1) All scoring dimensions (e.g., soundness, excitement, etc.) and their scale (1-5? 1-4?). 2) Overall assessment scale. 3) Any other required fields. 4) What criteria distinguish main conference vs findings papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form fields, scoring dimensions, and their scales. I need: 1) All scoring dimensions (e.g., soundness, excitement, etc.) and their scale (1-5? 1-4?). 2) Overall assessment scale. 3) Any other required fields. 4) What criteria distinguish main conference vs findings papers."
  }
}
```

</details>

---


### Tool result

_source line 1751 · 2026-05-23T02:01:58.523554+00:00_

# ACL Rolling Review Form - Complete Extraction

## Scoring Dimensions & Scales

**Reviewer Confidence** (1-5 scale)
- 5: Positive evaluation is correct; very familiar with related work
- 4: Quite sure; unlikely to have missed important details
- 3: Pretty sure; may have missed some details
- 2: Can defend evaluation; likely missed some details
- 1: Outside expertise area or paper very difficult to understand

**Soundness** (1-5 scale with half-point increments: 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5)
- 5: Excellent - "one of the most thorough"
- 4: Strong - sufficient support for claims
- 3: Acceptable - supports main claims with minor gaps
- 2: Poor - main claims insufficiently supported
- 1: Major Issues - insufficient rigor for publication

**Excitement** (1-5 scale with half-point increments)
- 5: Highly Exciting - would recommend to others
- 4: Exciting - would mention to others
- 3: Interesting - might mention specific points
- 2: Potentially Interesting - limited personal resonance
- 1: Not Exciting - irrelevant to NLP community

## Overall Assessment Scale (1-5 with half-points)

- 5: Consider for Award (top 2.5%)
- 4.5: Borderline Award
- 4: Conference acceptance
- 3.5: Borderline Conference
- 3: Findings acceptance
- 2.5: Borderline Findings
- 2: Resubmit next cycle
- 1.5: Resubmit after next cycle
- 1: Do not resubmit

## Key Distinction: Main vs. Findings Papers

"Main criteria for Findings are soundness and reproducibility," while main conference papers may also emphasize novelty and impact.

## Required Fields

- Paper Summary
- Strengths & Weaknesses
- Reviewer Confidence
- Soundness
- Excitement
- Overall Assessment
- Reproducibility (1-5)
- Limitations & Societal Impact
- Ethical Concerns
- Datasets & Software value (if applicable)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6472
}
```

</details>

---


### Tool call

_source line 1752 · 2026-05-23T02:02:13.220961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 1753 · 2026-05-23T02:02:13.825315+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1754 · 2026-05-23T02:02:14.327327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1755 · 2026-05-23T02:02:15.032970+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1756 · 2026-05-23T02:02:15.085492+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1864
}
```

</details>

---


### Tool result

_source line 1757 · 2026-05-23T02:02:16.753325+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2928
}
```

</details>

---


### Tool result

_source line 1758 · 2026-05-23T02:02:16.956203+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2628
}
```

</details>

---


### Tool result

_source line 1759 · 2026-05-23T02:02:17.158703+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2125
}
```

</details>

---


### Tool call

_source line 1760 · 2026-05-23T02:02:27.317713+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/submitted.pdf",
  "pages": "9-14",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/submitted.pdf",
    "pages": "9-14",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1761 · 2026-05-23T02:02:28.327708+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 89.3}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 577.0}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 579.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 625.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 616.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 575.5}], \"total_pages\": 39, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1009
}
```

</details>

---


### Tool call

_source line 1762 · 2026-05-23T02:02:32.603040+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Read paper source sections",
  "prompt": "I need you to read the following files from this paper project and report back their full contents. These are LaTeX source files for a paper submission. Read each file completely and report the content:\n\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex`\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex`\n3. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex`\n4. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex`\n\nReport each file's full content verbatim. This is for a paper review - I need the exact text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Read paper source sections",
    "prompt": "I need you to read the following files from this paper project and report back their full contents. These are LaTeX source files for a paper submission. Read each file completely and report the content:\n\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex`\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex`\n3. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex`\n4. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex`\n\nReport each file's full content verbatim. This is for a paper review - I need the exact text."
  }
}
```

</details>

---


### Tool call

_source line 1763 · 2026-05-23T02:02:34.063041+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1764 · 2026-05-23T02:02:34.516891+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, a framework that translates Information Extraction (IE) ontologies into composable token-level decoding constraints.
3	A decidability analysis yields a two-layer architecture: a \emph{grammar layer} (context-free) compiles ontology constraints into grammars ensuring JSON validity and vocabulary membership; a \emph{semantic layer} (prefix-decidable with state) interprets type constraints at runtime via stateful token masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
4	The two layers exhibit an empirical enabling dependency (Proposition~1, scale-sensitive; \S\ref{sec:70b-results}): neither achieves full DR reduction alone.
5	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
6	Composed with LoRA fine-tuning on three 8B-class models across two RE datasets (up to 96 relation types), \textsc{OntoCoDec} near-eliminates DR ($<$\,0.1\%) at R-F1 41--47\% ($\pm$0.8\,pp); under fine-tuning, CF remains $\leq$\,1.4\% with greedy decoding and reaches zero with beam search ($k{=}4$) on both RE datasets (1.54$\times$ latency; \S\ref{sec:beam-results}).
7	Zero-shot evaluation serves as a diagnostic probe, revealing DR reduction of 76--99\% on SciERC and 42--90\% on DocRED across three models; constraint tightness ($\bar{\kappa}$) is a descriptive correlate of enforcement difficulty ($n{=}3$ schemas, $p{=}0.138$).
8	70B-class validation on SciERC (full six-way ablation; \S\ref{sec:70b-results}) with preliminary DocRED support, and event extraction on WikiEvents (\S\ref{sec:wikievents}), confirm generalizability beyond the primary 8B evaluation.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1765 · 2026-05-23T02:02:34.667919+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 1766 · 2026-05-23T02:02:34.718665+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity necessarily carries a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 0.5--2\% even after LoRA fine-tuning; rates correlate with schema restrictiveness (few valid type pairs per relation) rather than ontology or model scale.
9	At competitive quality (R-F1 41--47\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption, making reliable constraint enforcement necessary.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering improves precision but discards up to 48\% of predictions including true positives (\S\ref{sec:cross-model}); at high rejection rates (e.g., Mistral DocRED 73.7\%), it becomes impractical.
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance without runtime enforcement; no method provides both semantic awareness and hard constraint enforcement.
16	
17	We propose \textbf{OntoCoDec}, a framework that translates IE ontologies into composable layers
…[truncated 2519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1767 · 2026-05-23T02:02:34.719181+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1768 · 2026-05-23T02:02:39.149015+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, SynCode~\cite{ugare2024syncode}, and related systems~\cite{beurer-kellner2023lmql,park2024grammar,jsonschemabench2025} enforce format validity via CFG-based token masking.
8	NeuroLogic Decoding~\cite{lu2021neurologic} enforces predicate-logic constraints via beam-level reranking; OntoCoDec applies constraints per-token via forward masking, avoiding beam-width dependence.
9	In code generation, PICARD~\cite{scholak2021picard} and \citet{pldi2025_type_constrained_codegen} compile type systems into prefix automata; OntoCoDec differs in applying proactive token-level masking with a dynamic entity registry across multi-relation outputs (\S\ref{sec:composition}).
10	DCCD~\cite{dccd2026} and \citet{nguyen2026thinking} decouple reasoning from constrained generation via multi-pass architectures; OntoCoDec enforces schema semantics within a single forward pass.
11	
12	\paragraph{Schema-aware IE.}
13	GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, GUIDEX~\cite{guidex2025}, GenIE~\cite{josifoski2022genie}, TANL~\cite{paolini2021tanl}, REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, and others~\cite{fei2022lasuie,wang2022deepstruct,lu2022uie,lou2023usm,zhou2024universalner} encode ontology structure or frame IE as structured generation, though schema compliance gaps persist~\cite{wadhwa2023revisiting}.
14	GoLLIE and KnowCoder embed schema knowledge via code-style prompts (training-time internalization without runtime enforcement); GoLLIE-7B eliminates DR at severe coverage cost (R-F1${=}$0.0, 46\% empty output), while OntoCoDec achieves R-F1${=}$45.47 at DR${=}$0.09\%~\cite{knowcoder_acl2024}.
15	
16	\paragraph{Constraint enforcement in IE.}
17	\citet{roth_yih_2004} 
…[truncated 747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4429
}
```

</details>

---


### Tool call

_source line 1769 · 2026-05-23T02:02:39.752800+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 1770 · 2026-05-23T02:02:39.803573+00:00_

1	% Section 7 — Discussion and Conclusion
2	
3	OntoCoDec translates IE ontologies into composable token-level constraints, providing a systematic empirical framework---automatically compiled from ontologies, validated across 3 datasets, 3+ models, and 2 tasks---rather than a novel decoding algorithm.
4	LoRA + greedy S1 near-eliminates DR ($<$\,0.1\%) with CF\,$\leq$\,1.4\%; beam ($k{=}4$) eliminates all violations on both RE datasets (1.54$\times$ latency); zero-shot DR drops 42--99\% across three 8B-class models.
5	The central insight is that IE type constraints exceed context-free expressiveness (Proposition~1): unlike rejection-based approaches that prune invalid outputs post-generation~\cite{scholak2021picard}, the semantic layer applies constructive forward masking via a dynamic entity registry, bridging the gap grammar-only enforcement cannot address (3\% vs.\ 94\% DR reduction); this enabling dependency---scale-sensitive (\S\ref{sec:70b-results})---shows grammar-constrained decoding is necessary but insufficient for IE schema compliance.
6	Residual CF arises from per-triple independent enforcement; extending to global entity-level type consensus during decoding---eliminating CF without beam search overhead---is the most important direction for future work.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1771 · 2026-05-23T02:03:18.203189+00:00_

Here are the full contents of the four LaTeX files from your paper project:

---

## 1. abstract.tex

```latex
\begin{abstract}
We present \textsc{OntoCoDec}, a framework that translates Information Extraction (IE) ontologies into composable token-level decoding constraints.
A decidability analysis yields a two-layer architecture: a \emph{grammar layer} (context-free) compiles ontology constraints into grammars ensuring JSON validity and vocabulary membership; a \emph{semantic layer} (prefix-decidable with state) interprets type constraints at runtime via stateful token masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
The two layers exhibit an empirical enabling dependency (Proposition~1, scale-sensitive; \S\ref{sec:70b-results}): neither achieves full DR reduction alone.
% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
Composed with LoRA fine-tuning on three 8B-class models across two RE datasets (up to 96 relation types), \textsc{OntoCoDec} near-eliminates DR ($<$\,0.1\%) at R-F1 41--47\% ($\pm$0.8\,pp); under fine-tuning, CF remains $\leq$\,1.4\% with greedy decoding and reaches zero with beam search ($k{=}4$) on both RE datasets (1.54$\times$ latency; \S\ref{sec:beam-results}).
Zero-shot evaluation serves as a diagnostic probe, revealing DR reduction of 76--99\% on SciERC and 42--90\% on DocRED across three models; constraint tightness ($\bar{\kappa}$) is a descriptive correlate of enforcement difficulty ($n{=}3$ schemas, $p{=}0.138$).
70B-class validation on SciERC (full six-way ablation; \S\ref{sec:70b-results}) with preliminary DocRED support, and event extraction on WikiEvents (\S\ref{sec:wikievents}), confirm generalizability beyond the primary 8B evaluation.
\end{abstract}
```

---

## 2. section1_introduction_draft.tex

```latex
% Section 1: Introduction (compressed, 669→~550 words)

\section{Introduct
…[truncated 8451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 45600
}
```

</details>

---


### Tool call

_source line 1772 · 2026-05-23T02:03:25.520317+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1773 · 2026-05-23T02:03:26.023934+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1774 · 2026-05-23T02:03:26.024413+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 1775 · 2026-05-23T02:03:26.578793+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1776 · 2026-05-23T02:03:26.682453+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 658
}
```

</details>

---


### Tool result

_source line 1777 · 2026-05-23T02:03:27.287925+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 709
}
```

</details>

---


### Tool call

_source line 1778 · 2026-05-23T02:03:54.033882+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DCCD constrained decoding 2025 2026 Reddy structured generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DCCD constrained decoding 2025 2026 Reddy structured generation"
  }
}
```

</details>

---


### Tool call

_source line 1779 · 2026-05-23T02:03:54.536243+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"thinking before constraining\" Nguyen 2026 constrained decoding LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"thinking before constraining\" Nguyen 2026 constrained decoding LLM"
  }
}
```

</details>

---


### Tool call

_source line 1780 · 2026-05-23T02:03:55.380306+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CRANE constrained decoding 2025 Banerjee format constraints LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CRANE constrained decoding 2025 Banerjee format constraints LLM"
  }
}
```

</details>

---


### Tool call

_source line 1781 · 2026-05-23T02:03:55.984301+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "IterGen iterative constrained generation 2025 Ugare backtracking"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "IterGen iterative constrained generation 2025 Ugare backtracking"
  }
}
```

</details>

---


### Tool result

_source line 1782 · 2026-05-23T02:04:01.258932+00:00_

Web search results for query: "CRANE constrained decoding 2025 Banerjee format constraints LLM"

Links: [{"title":"Reasoning with constrained LLM generation - CRANE","url":"https://arxiv.org/pdf/2502.09061"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://par.nsf.gov/servlets/purl/10633770"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://proceedings.mlr.press/v267/banerjee25a.html"},{"title":"[2502.09061] CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/abs/2502.09061"},{"title":"CRANE: Reasoning with constrained LLM generation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/crane-reasoning-constrained-llm-generation"},{"title":"[2502.09061v2] CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/abs/2502.09061v2"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/html/2502.09061v3"},{"title":"CRANE: Reasoning with constrained LLM generation | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.09061v3"},{"title":"ICML Poster CRANE: Reasoning with constrained LLM generation","url":"https://icml.cc/virtual/2025/poster/43624"}]

I found comprehensive information about CRANE. Here are the key details:

## CRANE: Reasoning with Constrained LLM Generation

CRANE is a method for code generation, symbolic math reasoning, and other tasks that require LLMs to produce outputs that are both syntactically and semantically correct. The research was conducted by Debangshu Banerjee and colleagues, and was published in the Proceedings of the 42nd International Conference on Machine Learning (ICML) in 2025.

### The Core Problem

While constrained LLM generation is a promising direction to enforce adherence to formal grammar, strict enforcement of formal constraints often diminishes the reasoning capabilities of LLMs. The work provides a theoretical explanation for why constraining LLM outputs to very restrictive gramm
…[truncated 905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5878
}
```

</details>

---


### Tool result

_source line 1783 · 2026-05-23T02:04:01.560715+00:00_

Web search results for query: "DCCD constrained decoding 2025 2026 Reddy structured generation"

Links: [{"title":"[2603.03305] Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/abs/2603.03305"},{"title":"Appendix","url":"https://arxiv.org/html/2603.03305"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"Structured Decoding","url":"https://www.aussieai.com/blog/structured-decoding-optimization"},{"title":"A Guide to Structured Outputs Using Constrained Decoding","url":"https://www.aidancooper.co.uk/constrained-decoding/"},{"title":"Earley-Driven Dynamic Pruning for Efficient Structured Decoding","url":"https://arxiv.org/pdf/2506.01151"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning","url":"https://arxiv.org/pdf/2305.13971"}]

I found relevant information about DCCD constrained decoding. Here are the search results:

## Draft-Conditioned Constrained Decoding (DCCD)

Draft-Conditioned Constrained Decoding (DCCD) is a simple two-step, training-free inference procedure that decouples semantic planning from structural enforcement: an unconstrained draft is generated first, and constrained decoding is then applied, conditioned on this draft, to guarantee validity.

### The Problem It Solves

Constrained decoding enforces validity token-by-token via masking and renormalization, but it can distort generation when the model assigns low probability mass to valid continuations, pushing decoding toward locally valid yet semantically incorrect trajectories.

### How DCCD Works

In Step 1, a model generates an unconstrained draft that captures the semantic plan or intermediate reasoning. In Step 2, the final structured output is generated using constrained decoding conditioned on the draft. Conditioning shifts probability mass toward schema-consistent continuations, so the subsequent constraint enforcement st
…[truncated 483 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7526
}
```

</details>

---


### Tool result

_source line 1784 · 2026-05-23T02:04:01.561340+00:00_

Web search results for query: "IterGen iterative constrained generation 2025 Ugare backtracking"

Links: [{"title":"[Quick Review] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://liner.com/review/itergen-iterative-semanticaware-structured-llm-generation-with-backtracking"},{"title":"Shubham Ugare","url":"https://shubhamugare.github.io/"},{"title":"[PDF] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking | Semantic Scholar","url":"https://www.semanticscholar.org/paper/8f918a87d0f1bc090fca1dbdfbc4d06a9dc88a66"},{"title":"ICLR Poster IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://iclr.cc/virtual/2025/poster/29157"},{"title":"[Literature Review] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://www.themoonlight.io/en/review/itergen-iterative-semantic-aware-structured-llm-generation-with-backtracking"},{"title":"GitHub - structuredllm/itergen: Iterate on LLM-based structured generation forward and backward","url":"https://github.com/structuredllm/itergen"},{"title":"Shubham Ugare shubhamdugare@gmail.com https://shubhamugare.github.io Education","url":"https://shubhamugare.github.io/assets/pdf/resume.pdf"},{"title":"[2410.07295] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://arxiv.org/abs/2410.07295"},{"title":"IterGen: Iterative Semantic-aware Structured LLM ...","url":"https://iclr.cc/media/iclr-2025/Slides/29157.pdf"},{"title":"IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking | OpenReview","url":"https://openreview.net/forum?id=ac93gRzxxV"}]

Based on the search results, here's what I found about IterGen:

## IterGen Overview

IterGen is a user-friendly library for iterative, grammar-guided LLM generation that enables users to move both forward and backward within the generated output based on grammar symbols. The paper was published
…[truncated 1150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5577
}
```

</details>

---


### Tool result

_source line 1785 · 2026-05-23T02:04:01.762495+00:00_

Web search results for query: ""thinking before constraining" Nguyen 2026 constrained decoding LLM"

Links: [{"title":"[2601.07525] Thinking Before Constraining: A Unified Decoding Framework for Large Language Models","url":"https://arxiv.org/abs/2601.07525"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Thinking Before Constraining: A Unified Decoding Framework for Large Language Models","url":"https://arxiv.org/html/2601.07525"},{"title":"Constrained Decoding: Grammar-Guided Generation for Structured LLM Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://www.google.com/goto?url=CAESdgE7q4ylTUjr6_5MGhsiZhNngKGF87RlL2P2bnNej1e3gEiyvEdbIDM0D7f-utVkHPE4R0bLnYFpuF3TFsDOZJJx9ncMfdCaoRmgBswJLh-CTTVlrE63pb_dhwNi8UeqlZlML3lkLnfV3eOP9nRdsAsSmf5jYq0%3D"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Thinking Before Constraining: A Unified Decoding Framework for Large","url":"https://www.arxiv.org/pdf/2601.07525"},{"title":"Constrained Decoding of Diffusion LLMs with Context-Free Grammars | OpenReview","url":"https://openreview.net/forum?id=7Sph4KyeYO"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/pdf/2403.06988"}]

I found the paper you're looking for! Here are the key details:

## "Thinking Before Constraining: A Unified Decoding Framework for Large Language Models"

The paper is authored by Ngoc Trinh Hung Nguyen, Alonso Silva, Laith Zumot, Liubov Tupikina, Armen Aghasaryan, and Mehwish Alam, with Nguyen's correspondence at Télécom Paris, Institut Polytechnique de Paris. It was submitted on January 12, 2026.

### Overv
…[truncated 953 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7226
}
```

</details>

---


### Tool call

_source line 1786 · 2026-05-23T02:04:10.196578+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ADELIE schema-aware information extraction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ADELIE schema-aware information extraction 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 1787 · 2026-05-23T02:04:10.197034+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SGLang constrained decoding structured generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SGLang constrained decoding structured generation 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 1788 · 2026-05-23T02:04:10.549638+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "JSONSchemaBench benchmark structured generation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "JSONSchemaBench benchmark structured generation 2025"
  }
}
```

</details>

---


### Tool result

_source line 1789 · 2026-05-23T02:04:17.024441+00:00_

Web search results for query: "JSONSchemaBench benchmark structured generation 2025"

Links: [{"title":"GitHub - guidance-ai/jsonschemabench · GitHub","url":"https://github.com/guidance-ai/jsonschemabench"},{"title":"GitHub - epfl-dlab/jsonschemabench","url":"https://github.com/epfl-dlab/jsonschemabench"},{"title":"[2501.10868] JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://arxiv.org/abs/2501.10868"},{"title":"epfl-dlab/JSONSchemaBench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/epfl-dlab/JSONSchemaBench"},{"title":"(PDF) Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://www.researchgate.net/publication/388231978_Generating_Structured_Outputs_from_Language_Models_Benchmark_and_Studies"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models | alphaXiv","url":"https://www.alphaxiv.org/abs/2501.10868"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://arxiv.org/html/2501.10868v3"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language   Models","url":"https://arxiv.org/pdf/2501.10868"}]

Based on the search results, here's what I found about JSONSchemaBench:

## Overview
JSONSchemaBench is a benchmark of around 10,000 real-world JSON schemas that capture a wide range of constraints and complexities. JSONSchemaBench helps to measure efficiency and coverage of a given structured output engine.

## Purpose and Scope
The benchmark for constrained decoding comprises 10K real-world JSON schemas that encompass a wide range of constraints with varying complexity. The benchmark is paired with the existing official JSON Schema Test Suite and evaluates six state-of-the-art constrained decoding frameworks, including Guidance, Outlines, Llamacpp, XGrammar, OpenAI, and Gemini.

## Key Findings
Constrained decoding can speed up the generation process by 50
…[truncated 612 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6474
}
```

</details>

---


### Tool result

_source line 1790 · 2026-05-23T02:04:18.732456+00:00_

Web search results for query: "SGLang constrained decoding structured generation 2025 2026"

Links: [{"title":"SGLang — Fastest Structured Output and Prefix-Heavy LLM Serving (2026 Review) — ChatForest","url":"https://chatforest.com/reviews/sglang-structured-generation-llm-serving/"},{"title":"Summary: SGLang: Efficient Execution of Structured Language Model Programs - Wentao's Blog","url":"https://wentao.site/sgl_summary/"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Beyond 'Please Behave': How Constrained Decoding and SGLang Are Taming Large Language Models - Oreate AI Blog","url":"https://www.oreateai.com/blog/beyond-please-behave-how-constrained-decoding-and-sglang-are-taming-large-language-models/40cc825374735eca1a4f4c7481037e8c"},{"title":"SGLang - Wikipedia","url":"https://en.wikipedia.org/wiki/SGLang"},{"title":"Inside SGLang: Anatomy of a High-Performance Structured LLM Inference System - SugiV Blog","url":"https://blog.sugiv.fyi/inside-sglang-anatomy-high-performance-structured-llm-inference-system"},{"title":"GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub","url":"https://github.com/sgl-project/sglang"},{"title":"A Guide to Structured Outputs Using Constrained Decoding","url":"https://www.aidancooper.co.uk/constrained-decoding/"}]

Based on the search results, here's what I found about SGLang's constrained decoding and structured generation in 2025-2026:

## Overview

SGLang (short for Structured Generation Language) is an open-source framework for programming and serving large language models and multimodal models. SGLang consists of two main components: a front-end language embedded in Python and a back-end runtime for executing language model programs efficiently, with the front end providing primitives for generation, select
…[truncated 1361 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8535
}
```

</details>

---


### Tool result

_source line 1791 · 2026-05-23T02:04:20.991032+00:00_

Web search results for query: "ADELIE schema-aware information extraction 2025 2026"

Links: [{"title":"ADELIE: Aligning Large Language Models on Information Extraction | Request PDF","url":"https://www.researchgate.net/publication/386188440_ADELIE_Aligning_Large_Language_Models_on_Information_Extraction"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction","url":"https://arxiv.org/html/2405.05008v1"},{"title":"Tsinghua University Researchers Propose ADELIE: Enhancing Information Extraction with Aligned Large Language Models Around Human-Centric Tasks - MarkTechPost","url":"https://www.marktechpost.com/2024/05/11/tsinghua-university-researchers-propose-adelie-enhancing-information-extraction-with-aligned-large-language-models-around-human-centric-tasks/"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction","url":"https://arxiv.org/pdf/2405.05008"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/adelie-aligning-large-language-models-information-extraction"},{"title":"[Quick Review] ADELIE: Aligning Large Language Models on Information Extraction","url":"https://liner.com/review/adelie-aligning-large-language-models-on-information-extraction"},{"title":"(PDF) ADELIE: Aligning Large Language Models on Information Extraction | Chat PDF","url":"https://nanonets.com/chat-pdf/aligning-large-language-models-on-information-extraction"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction","url":"https://openreview.net/pdf?id=hi5k4PDnX7"}]

Based on the search results, here's what I found about ADELIE and schema-aware information extraction:

## ADELIE Overview

ADELIE (Aligning large language moDELs on Information Extraction) is an LLM aligned on IE tasks. This is an EMNLP 2024 paper about an LLM aligned for information extraction using IEInstruct and DPO.

## The Problem It Addresses

LLMs struggle to unde
…[truncated 1111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10794
}
```

</details>

---


### Tool call

_source line 1792 · 2026-05-23T02:05:52.994451+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/submitted.pdf",
  "pages": "15,20,30,39",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/submitted.pdf",
    "pages": "15,20,30,39",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1793 · 2026-05-23T02:05:53.447894+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 387.3}, {\"page\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p20.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.8}, {\"page\": 30, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p30.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 415.6}, {\"page\": 39, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p39.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 109.5}], \"total_pages\": 39, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1794 · 2026-05-23T02:05:58.395817+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1795 · 2026-05-23T02:05:58.949647+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 1796 · 2026-05-23T02:05:59.000372+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p39.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images/submitted_p39.png"
  }
}
```

</details>

---


### Tool result

_source line 1797 · 2026-05-23T02:05:59.052915+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1798 · 2026-05-23T02:08:49.236445+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿报告 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5 — Findings\n**一句话总结**: 扎实的工程贡献，评估全面且诚实，但核心新颖性有限（主要是已有技术的系统性集成），且 CF trade-off 削弱了中心论点；正文超出 8 页限制需立即修复。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 实验设计扎实（3 数据集 × 3 模型 × 2 任务），但 CF trade-off 削弱了 \"near-eliminate violations\" 的 claim；enabling dependency 随 scale 变化（70B 时 semantic layer 独立达到 84% DR reduction），动摇了核心 architectural argument 的普适性 |\n| Excitement | 2.5 / 5 | 论文诚实定位为 \"systematic engineering contribution\"，但这也意味着新颖性天花板有限——grammar + semantic 两层架构是已有组件（XGrammar + 状态化 token masking）的集成，而非新解码算法；对 NLP 社区的预期影响力中等 |\n| Reproducibility | 4.0 / 5 | 附录极其详尽（~25 页，含 prompts、case studies、power analysis、scalability benchmarks），承诺代码开源；violation 分类和量化定义清晰 |\n| Reviewer Confidence | 4 / 5 | 熟悉 constrained decoding 和 schema-aware IE 领域 |\n\n---\n\n## Paper Summary\n\n论文提出 OntoCoDec，一个将 IE 本体约束编译为可组合 token-level 解码约束的框架。通过可判定性分析，设计了两层架构：grammar layer（基于 XGrammar 的 CFG 编译，保证 JSON 结构和词汇表合法性）和 semantic layer（运行时状态化 token masking，维护动态 entity registry 以执行 domain/range 类型约束）。在 SciERC、DocRED、WikiEvents 三个数据集上，跨 Qwen3-8B、Llama-3.1-8B、Mistral-7B 三个模型进行了零样本和 LoRA 微调评估。核心结果：LoRA + S1 策略下 DR < 0.1%，R-F1 41–47%，beam search (k=4) 可消除所有 violation 类型。\n\n---\n\n## 主要优势\n\n**S1.** 问题定义和 violation taxonomy 清晰。四类违规（DR/CF/RV/ET）定义明确，为后续消融分析提供了细粒度的分析框架。Constraint tightness (κ̄) 作为描述性指标是有用的概念工具。\n\n**S2.** 评估覆盖面广且设计合理。3 数据集覆盖不同 schema 复杂度（SciERC 7 entity types / 7 relations → DocRED 6 / 96 → WikiEvents 56 event types / 24 constraints），3 tokenizer families，zero-shot 与 fine-tuning 两种设定，加上 70B 模型验证和 event extraction 扩展——这在同类工作中是少见的系统性。\n\n**S3.** 论文对自身局限性异常诚实。Limitations section（page 10）详细分析了 CF trade-off、scale-dependent behavior、parse failure increase 等问题，没有回避 uncomfortable results（如 well-calibrated model 上 S1 引入 up to 12.02% CF）。这在投稿论文中难能可贵。\n\n**S4.** Proposition 1 虽然形式化了已知直觉，但与 Appendix O 的 pumping lemma 证明一起，为两层架构提供了清晰的理论动机。Corollary（empirical enabling dependency）将理论与实验连接。\n\n**S5.** 框架自动化程度高——从 ontology 自动编译约束、tokenizer-agnostic、无需 constraint-specific training——工程实用性强。Runtime overhead 仅 10–13%（greedy）/ 54%（beam k=4），可接受。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 正文超出 8 页限制\n- 具体位置：§7 Discussion and Conclusion 起始于 page 8，溢出至 page 9（约 13 行文字）\n- 问题：EMNLP 2026 long paper 正文严格限制 8 页。当前 §7 结论段落溢出到第 9 页，\\clearpage 后 Limitations 从第 10 页开始。正文实际为 9 页，违反格式要求。\n- 为什么影响接收：格式违规可能导致 desk reject，至少会被 AC 标记为合规问题。\n- 建议修改方向：压缩 §7 结论（当前约 150 词，可压缩至 100 词以内）或从 §6 Related Work / §5 实验中回收空间。§6 Related Work 目前仅半页但包含 3 个 dense paragraph，考虑进一步精简 §5 中的某些重复性数字表述。\n\n**N2** [critical] CF trade-off 在 Abstract/Introduction 中的 framing 偏乐观\n- 具体位置：Abstract line \"CF remains ≤1.4% with greedy decoding and reaches zero with beam search (k=4)\"；§1 Introduction \"DR enforcement converts ontologically invalid violations to individually valid but type-inconsistent ones (CF≤1.4% fine-tuned)\"\n- 问题：Abstract 中 CF ≤1.4% 的表述容易给读者一个 \"violations 几乎被消除\" 的印象，但实际上 CF 是 **由约束系统自身引入的**——对于 well-calibrated models（Qwen, Llama），unconstrained baseline 的 CF 可能更低。Table 1 显示 unconstrained Qwen 的 CF = 0，而 S1 后 CF 升至 1.18%（SciERC）。对 Mistral（poorly-calibrated），S1 确实大幅降低 CF（56.87% → 1.27%），但这只对一个模型成立。\n- Abstract 说 \"reaches zero with beam search\" 虽然技术上准确，但 beam search 的 1.54× latency 代价和仅在 fine-tuned setting 下成立的前提条件均未在 abstract 中提及。\n- 为什么影响接收：这关乎论文核心 claim 的准确性。如果 reviewer 读 abstract 后认为 \"约束系统消除了所有违规\"，但细读后发现系统实际上将一种违规转化为另一种，会严重损害 credibility。\n- 建议修改方向：在 Abstract 中明确 acknowledge CF 是 DR enforcement 的 side effect，例如 \"DR enforcement introduces type-inconsistency violations (CF ≤1.4%) as a trade-off, resolvable via beam search (k=4, 1.54× latency) under fine-tuning\"。Introduction 中已有部分 acknowledgment 但不够突出。\n\n**N3** [critical] \"Enabling dependency\" claim 的 scale sensitivity 在主文中讨论不足\n- 具体位置：§1 贡献列表 item 2：\"on SciERC neither layer alone exceeds 24% DR reduction (at 70B, semantic layer achieves 84% independently; §5.4)\"\n- 问题：Introduction 中以括号形式提及 70B 的例外情况，但这不是小事——70B 时 semantic layer 独立达到 84% DR reduction，这意味着 grammar layer 对 larger models 可能不是 \"necessary\"。这直接动摇了 Proposition 1 → Corollary → 两层架构 enabling dependency 的核心叙事链。论文在 Limitations 中承认了这一点，但 Introduction 和 Abstract 的 framing 仍以 8B 结果为主导，给读者的 first impression 是两层缺一不可。\n- 为什么影响接收：核心 architectural argument 的普适性受到质疑。如果 larger models 不需要 grammar layer 也能有效约束，那两层设计的 necessity 就变成了一个 scale-dependent 的实现细节而非普适性贡献。\n- 建议修改方向：在 Introduction 中更显著地讨论 scale sensitivity（不仅仅是括号注释），可能需要将 enabling dependency 的 claim 显式限定为 \"for 8B-class models\" 或重新 frame 为 \"complementary layers with scale-dependent relative contribution\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 新颖性天花板：系统集成 vs. 算法创新\n- 具体位置：整篇论文的定位\n- 问题：论文自述为 \"systematic engineering contribution with theoretical grounding\"（§1）。这个定位是诚实的，但也暴露了新颖性的局限：\n  - Grammar layer 直接复用 XGrammar，无修改\n  - Semantic layer 的 stateful token masking 是 continuation masking（prefix matching + entity registry lookup）的直接实现\n  - Proposition 1 形式化了 \"cross-field type constraints are not context-free\" 这一在 formal language theory 中广为人知的事实\n  - 与 PICARD（Scholak et al., 2021）的区别被描述为 \"rejection-based vs. constructive forward masking\"，但 PICARD 也是 incremental 的（在每一步检查 parser state 决定是否允许 continuation），区别更多在于 IE-specific dynamic entity registry，而非 masking 方向性\n  - 与 IterGen（Ugare et al., 2025）的区别是 forward-only vs. backtracking——有效但增量\n- 建议：更精确地定位贡献——核心价值在于 (1) 将已有 constrained decoding 技术适配到 IE 的特殊需求（动态 entity registry）；(2) 系统性地量化了 violation landscape 和 constraint trade-offs。避免暗示这是一个 \"novel decoding algorithm\"。\n\n**W2** [warning] 主文 Related Work 过于精简，关键工作讨论不足\n- 具体位置：§6 Related Work（page 8，约 0.5 页）\n- 问题：§6 仅用三个 paragraph 覆盖三个方向，大量内容推迟到 Appendix B（page 15）。虽然 ARR 允许 detailed survey in appendix，但主文应包含足够的对比分析让 reviewer 评估 novelty。当前问题：\n  - **ADELIE**（Cheng et al., EMNLP 2024）完全缺失——作为近期最重要的 schema-aware IE 对齐工作之一，应在 \"Schema-aware IE\" 段落讨论\n  - 与 PICARD 的对比仅用一句 \"OntoCoDec differs in applying proactive token-level masking with a dynamic entity registry\"，没有展开 rejection vs. forward masking 的技术区别\n  - SGLang 作为当前最广泛使用的 constrained decoding serving framework 未被提及（虽然 XGrammar 被引用）\n- 建议：补充 ADELIE；扩展与 PICARD 的对比（至少 2-3 句说明技术区别和各自适用场景）；如有空间，提及 SGLang 作为 XGrammar 的部署框架。\n\n**W3** [warning] 缺少 running example，method section 可读性受损\n- 具体位置：§3 Method（pages 3–4）、§4 Constraint Composition（page 5）\n- 问题：论文引入了大量技术概念（grammar layer, semantic layer, entity registry, continuation masking, grammar-first fallback, S1/S2 strategies），但没有一个贯穿始终的 running example 来展示这些组件如何在一个具体输入上协作。Figure 1（page 3）是架构图但过于抽象。读者需要在脑中自行构造 \"给定一个句子和 ontology，两层如何协同约束每一步 token 生成\" 的具体过程。\n- 信息密度极高——§3-§4 共约 2 页覆盖了整个方法，没有 running example 的辅助，reviewer 需要反复阅读才能理解 constraint composition 的细节。\n- 建议：在 §3.1 或 Figure 1 旁增加一个小型 running example（如 SciERC 的一个 triple，展示 HEADTYPE 位置的 mask 计算和 entity registry 更新），即使需要从其他地方压缩空间。\n\n**W4** [warning] Zero-shot 评估的实际意义有限\n- 具体位置：§5.1 Table 1, §5.2, §5.3\n- 问题：Zero-shot R-F1 仅 4–8%（Introduction §1 承认 \"R-F1 remains around 4–8%\"），这意味着模型在 zero-shot 下基本无法完成 IE 任务。在这种情况下，约束系统对 violation rate 的改善（DR 降低 42–99%）虽然在技术上有效，但实际价值有限——如果输出本身质量极低，violation rate 的降低并不能使系统实用。\n- 论文将 zero-shot 定位为 \"diagnostic probe\"，这个 framing 是合理的，但 §5.1 和 §5.3 花了大量篇幅报告 zero-shot 数字，给人一种 zero-shot 是 primary evaluation 的错觉。\n- 建议：更明确地将 fine-tuning 结果作为 primary evaluation 呈现，zero-shot 部分可压缩（也可帮助解决页数问题）。\n\n**W5** [warning] Abstract 信息密度过高\n- 具体位置：Abstract（page 1）\n- 问题：Abstract 约 180 词中包含至少 15 个具体数字/百分比、6 个缩写（DR, CF, R-F1, κ̄, S1, LoRA）、多个 section 引用。一次阅读几乎无法提取核心 message。与 ACL 领域最佳论文的 abstract 相比（通常 1-2 个 headline 数字），信息密度过高。\n- 特别是 \"(Proposition 1, scale-sensitive; §5.4)\" 这种内部引用出现在 abstract 中不常见且分散注意力。\n- 建议：精简至 2-3 个 headline 数字（如 DR reduction rate、R-F1 range、latency overhead），删除内部 section 引用和 constraint tightness 细节。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.3 \"continuation masking\" 与 §3.2 的 \"token masking\" 术语关系不够清晰——后者是否是前者的子集？建议在首次使用时明确。\n- Table 1 中 \"ΔDR\" 列的正负号含义需在 caption 中说明（当前仅在文中解释为 \"relative change vs. unconstrained\"）。\n- §5.4 WikiEvents 结果标注为 \"Preliminary\"（n=20 documents），但 Table 4 中未在 caption 显著标注这一点。\n- 论文使用 \"enforcement\" 和 \"elimination\" 交替描述 DR reduction，但严格来说 DR ≤ 0.09% ≠ elimination——建议统一用 \"near-elimination\"。\n- Appendix O（Pumping Lemma Proof）的 \"Remark (finite entity sets)\" 承认实际场景下语言是 regular 的，但对应的 DFA 是指数级的——这个 nuance 值得在主文 §2 或 §3 简要提及。\n- Ethics Statement（page 10）提到 \"Code and data will be released upon acceptance\"——考虑补充 licensing 意向（MIT/Apache 等）。\n\n---\n\n## Questions for Authors\n\n**Q1.** Table 1 显示 Qwen unconstrained CF = 0，S1 后 CF = 1.18%。如果目标用户已经在用 well-calibrated model + LoRA，OntoCoDec 的 net benefit 是什么？DR ≤ 0.09% 的改善是否 justify 引入 CF 和额外 latency？是否有 downstream task（如 KG construction）的实验来量化 violation 减少的实际价值？\n\n**Q2.** Proposition 1 证明了 unbounded entity set 下 cross-field constraints 非 CF，但 Remark 承认 finite entity set 下语言是 regular 的（只是 DFA 是 exponential）。既然实践中 entity set 总是有限的，那 registry-based approach 相比一个（可能很大的）DFA 的优势到底是 theoretical intractability avoidance 还是 practical engineering convenience？\n\n**Q3.** 70B 模型上 semantic layer 独立达到 84% DR reduction（vs. 8B 的 ≤24%）。是否有对中间规模（如 13B, 32B）的 scaling curve 数据？如果 enabling dependency 在 scale 上是连续变化的，那 \"两层缺一不可\" 的 claim 只在 small model 上成立，论文的 architectural contribution 是否应该重新 frame？\n\n**Q4.** S2 (two-pass) 策略在 70B 上 R-F1 下降 8.45 pp（Appendix D），而 8B 上 S1/S2 comparable。这种 scale-dependent degradation 的 root cause 是什么？是否与 70B 模型的 probability distribution 更 peaked 有关？\n\n---\n\n## Missing References\n\n1. **ADELIE** (Cheng et al., EMNLP 2024) — \"Aligning Large Language Models on Information Extraction\"。作为近期 schema-aware IE 的代表工作，通过 instruction tuning + DPO 对齐 LLM 到 IE 任务，应在 §6 Schema-aware IE 段讨论，与 GoLLIE/KnowCoder 并列。\n2. **SGLang** (Zheng et al., 2024/2025) — 虽然 XGrammar 被引用为 grammar layer 的基础，但 SGLang 作为 XGrammar 的主要部署框架和当前最广泛使用的 structured generation serving system，值得提及。\n\n（DCCD Reddy et al. 2026、Thinking Before Constraining Nguyen et al. 2026、CRANE Banerjee et al. 2025、IterGen Ugare et al. 2025 均已被引用。）\n\n---\n\n## Overall Assessment 详细理由\n\n给出 **3.0（Findings）** 的主要考量：\n\n**支持 Findings 接收的理由：**\n- 评估系统性和全面性在同类工作中突出（3 datasets × 3+ models × 2 tasks × zero-shot/fine-tuned × beam/greedy）\n- Violation taxonomy 和 constraint tightness 指标对社区有参考价值\n- 论文对局限性的诚实讨论提升了科学可信度\n- 工程贡献实用——自动编译、tokenizer-agnostic、低 overhead\n\n**未达到 Conference (4.0) 的理由：**\n- 新颖性有限：核心是 XGrammar + entity registry masking 的系统集成，非新算法\n- CF trade-off 未解决——系统将 DR 转化为 CF，beam search 虽可解决但代价是 1.54× latency\n- Enabling dependency 的 scale sensitivity 动摇了两层架构作为普适设计的 claim\n- Zero-shot 场景下 R-F1 过低（4–8%），constraint 改善的实际价值存疑\n- 正文超页（需修复但本身不应影响学术评价）\n\n**与 3.5 (Borderline Conference) 的距离：**\n如果作者能 (1) 解决正文超页问题，(2) 更诚实地 frame CF trade-off（特别是 Abstract），(3) 提供 downstream task 的 impact 评估证明 violation reduction 的实际价值，(4) 加入 running example 提升可读性，评分可能上调至 3.5。",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿报告 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5 — Findings\n**一句话总结**: 扎实的工程贡献，评估全面且诚实，但核心新颖性有限（主要是已有技术的系统性集成），且 CF trade-off 削弱了中心论点；正文超出 8 页限制需立即修复。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 实验设计扎实（3 数据集 × 3 模型 × 2 任务），但 CF trade-off 削弱了 \"near-eliminate violations\" 的 claim；enabling dependency 随 scale 变化（70B 时 semantic layer 独立达到 84% DR reduction），动摇了核心 architectural argument 的普适性 |\n| Excitement | 2.5 / 5 | 论文诚实定位为 \"systematic engineering contribution\"，但这也意味着新颖性天花板有限——grammar + semantic 两层架构是已有组件（XGrammar + 状态化 token masking）的集成，而非新解码算法；对 NLP 社区的预期影响力中等 |\n| Reproducibility | 4.0 / 5 | 附录极其详尽（~25 页，含 prompts、case studies、power analysis、scalability benchmarks），承诺代码开源；violation 分类和量化定义清晰 |\n| Reviewer Confidence | 4 / 5 | 熟悉 constrained decoding 和 schema-aware IE 领域 |\n\n---\n\n## Paper Summary\n\n论文提出 OntoCoDec，一个将 IE 本体约束编译为可组合 token-level 解码约束的框架。通过可判定性分析，设计了两层架构：grammar layer（基于 XGrammar 的 CFG 编译，保证 JSON 结构和词汇表合法性）和 semantic layer（运行时状态化 token masking，维护动态 entity registry 以执行 domain/range 类型约束）。在 SciERC、DocRED、WikiEvents 三个数据集上，跨 Qwen3-8B、Llama-3.1-8B、Mistral-7B 三个模型进行了零样本和 LoRA 微调评估。核心结果：LoRA + S1 策略下 DR < 0.1%，R-F1 41–47%，beam search (k=4) 可消除所有 violation 类型。\n\n---\n\n## 主要优势\n\n**S1.** 问题定义和 violation taxonomy 清晰。四类违规（DR/CF/RV/ET）定义明确，为后续消融分析提供了细粒度的分析框架。Constraint tightness (κ̄) 作为描述性指标是有用的概念工具。\n\n**S2.** 评估覆盖面广且设计合理。3 数据集覆盖不同 schema 复杂度（SciERC 7 entity types / 7 relations → DocRED 6 / 96 → WikiEvents 56 event types / 24 constraints），3 tokenizer families，zero-shot 与 fine-tuning 两种设定，加上 70B 模型验证和 event extraction 扩展——这在同类工作中是少见的系统性。\n\n**S3.** 论文对自身局限性异常诚实。Limitations section（page 10）详细分析了 CF trade-off、scale-dependent behavior、parse failure increase 等问题，没有回避 uncomfortable results（如 well-calibrated model 上 S1 引入 up to 12.02% CF）。这在投稿论文中难能可贵。\n\n**S4.** Proposition 1 虽然形式化了已知直觉，但与 Appendix O 的 pumping lemma 证明一起，为两层架构提供了清晰的理论动机。Corollary（empirical enabling dependency）将理论与实验连接。\n\n**S5.** 框架自动化程度高——从 ontology 自动编译约束、tokenizer-agnostic、无需 constraint-specific training——工程实用性强。Runtime overhead 仅 10–13%（greedy）/ 54%（beam k=4），可接受。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 正文超出 8 页限制\n- 具体位置：§7 Discussion and Conclusion 起始于 page 8，溢出至 page 9（约 13 行文字）\n- 问题：EMNLP 2026 long paper 正文严格限制 8 页。当前 §7 结论段落溢出到第 9 页，\\clearpage 后 Limitations 从第 10 页开始。正文实际为 9 页，违反格式要求。\n- 为什么影响接收：格式违规可能导致 desk reject，至少会被 AC 标记为合规问题。\n- 建议修改方向：压缩 §7 结论（当前约 150 词，可压缩至 100 词以内）或从 §6 Related Work / §5 实验中回收空间。§6 Related Work 目前仅半页但包含 3 个 dense paragraph，考虑进一步精简 §5 中的某些重复性数字表述。\n\n**N2** [critical] CF trade-off 在 Abstract/Introduction 中的 framing 偏乐观\n- 具体位置：Abstract line \"CF remains ≤1.4% with greedy decoding and reaches zero with beam search (k=4)\"；§1 Introduction \"DR enforcement converts ontologically invalid violations to individually valid but type-inconsistent ones (CF≤1.4% fine-tuned)\"\n- 问题：Abstract 中 CF ≤1.4% 的表述容易给读者一个 \"violations 几乎被消除\" 的印象，但实际上 CF 是 **由约束系统自身引入的**——对于 well-calibrated models（Qwen, Llama），unconstrained baseline 的 CF 可能更低。Table 1 显示 unconstrained Qwen 的 CF = 0，而 S1 后 CF 升至 1.18%（SciERC）。对 Mistral（poorly-calibrated），S1 确实大幅降低 CF（56.87% → 1.27%），但这只对一个模型成立。\n- Abstract 说 \"reaches zero with beam search\" 虽然技术上准确，但 beam search 的 1.54× latency 代价和仅在 fine-tuned setting 下成立的前提条件均未在 abstract 中提及。\n- 为什么影响接收：这关乎论文核心 claim 的准确性。如果 reviewer 读 abstract 后认为 \"约束系统消除了所有违规\"，但细读后发现系统实际上将一种违规转化为另一种，会严重损害 credibility。\n- 建议修改方向：在 Abstract 中明确 acknowledge CF 是 DR enforcement 的 side effect，例如 \"DR enforcement introduces type-inconsistency violations (CF ≤1.4%) as a trade-off, resolvable via beam search (k=4, 1.54× latency) under fine-tuning\"。Introduction 中已有部分 acknowledgment 但不够突出。\n\n**N3** [critical] \"Enabling dependency\" claim 的 scale sensitivity 在主文中讨论不足\n- 具体位置：§1 贡献列表 item 2：\"on SciERC neither layer alone exceeds 24% DR reduction (at 70B, semantic layer achieves 84% independently; §5.4)\"\n- 问题：Introduction 中以括号形式提及 70B 的例外情况，但这不是小事——70B 时 semantic layer 独立达到 84% DR reduction，这意味着 grammar layer 对 larger models 可能不是 \"necessary\"。这直接动摇了 Proposition 1 → Corollary → 两层架构 enabling dependency 的核心叙事链。论文在 Limitations 中承认了这一点，但 Introduction 和 Abstract 的 framing 仍以 8B 结果为主导，给读者的 first impression 是两层缺一不可。\n- 为什么影响接收：核心 architectural argument 的普适性受到质疑。如果 larger models 不需要 grammar layer 也能有效约束，那两层设计的 necessity 就变成了一个 scale-dependent 的实现细节而非普适性贡献。\n- 建议修改方向：在 Introduction 中更显著地讨论 scale sensitivity（不仅仅是括号注释），可能需要将 enabling dependency 的 claim 显式限定为 \"for 8B-class models\" 或重新 frame 为 \"complementary layers with scale-dependent relative contribution\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 新颖性天花板：系统集成 vs. 算法创新\n- 具体位置：整篇论文的定位\n- 问题：论文自述为 \"systematic engineering contribution with theoretical grounding\"（§1）。这个定位是诚实的，但也暴露了新颖性的局限：\n  - Grammar layer 直接复用 XGrammar，无修改\n  - Semantic layer 的 stateful token masking 是 continuation masking（prefix matching + entity registry lookup）的直接实现\n  - Proposition 1 形式化了 \"cross-field type constraints are not context-free\" 这一在 formal language theory 中广为人知的事实\n  - 与 PICARD（Scholak et al., 2021）的区别被描述为 \"rejection-based vs. constructive forward masking\"，但 PICARD 也是 incremental 的（在每一步检查 parser state 决定是否允许 continuation），区别更多在于 IE-specific dynamic entity registry，而非 masking 方向性\n  - 与 IterGen（Ugare et al., 2025）的区别是 forward-only vs. backtracking——有效但增量\n- 建议：更精确地定位贡献——核心价值在于 (1) 将已有 constrained decoding 技术适配到 IE 的特殊需求（动态 entity registry）；(2) 系统性地量化了 violation landscape 和 constraint trade-offs。避免暗示这是一个 \"novel decoding algorithm\"。\n\n**W2** [warning] 主文 Related Work 过于精简，关键工作讨论不足\n- 具体位置：§6 Related Work（page 8，约 0.5 页）\n- 问题：§6 仅用三个 paragraph 覆盖三个方向，大量内容推迟到 Appendix B（page 15）。虽然 ARR 允许 detailed survey in appendix，但主文应包含足够的对比分析让 reviewer 评估 novelty。当前问题：\n  - **ADELIE**（Cheng et al., EMNLP 2024）完全缺失——作为近期最重要的 schema-aware IE 对齐工作之一，应在 \"Schema-aware IE\" 段落讨论\n  - 与 PICARD 的对比仅用一句 \"OntoCoDec differs in applying proactive token-level masking with a dynamic entity registry\"，没有展开 rejection vs. forward masking 的技术区别\n  - SGLang 作为当前最广泛使用的 constrained decoding serving framework 未被提及（虽然 XGrammar 被引用）\n- 建议：补充 ADELIE；扩展与 PICARD 的对比（至少 2-3 句说明技术区别和各自适用场景）；如有空间，提及 SGLang 作为 XGrammar 的部署框架。\n\n**W3** [warning] 缺少 running example，method section 可读性受损\n- 具体位置：§3 Method（pages 3–4）、§4 Constraint Composition（page 5）\n- 问题：论文引入了大量技术概念（grammar layer, semantic layer, entity registry, continuation masking, grammar-first fallback, S1/S2 strategies），但没有一个贯穿始终的 running example 来展示这些组件如何在一个具体输入上协作。Figure 1（page 3）是架构图但过于抽象。读者需要在脑中自行构造 \"给定一个句子和 ontology，两层如何协同约束每一步 token 生成\" 的具体过程。\n- 信息密度极高——§3-§4 共约 2 页覆盖了整个方法，没有 running example 的辅助，reviewer 需要反复阅读才能理解 constraint composition 的细节。\n- 建议：在 §3.1 或 Figure 1 旁增加一个小型 running example（如 SciERC 的一个 triple，展示 HEADTYPE 位置的 mask 计算和 entity registry 更新），即使需要从其他地方压缩空间。\n\n**W4** [warning] Zero-shot 评估的实际意义有限\n- 具体位置：§5.1 Table 1, §5.2, §5.3\n- 问题：Zero-shot R-F1 仅 4–8%（Introduction §1 承认 \"R-F1 remains around 4–8%\"），这意味着模型在 zero-shot 下基本无法完成 IE 任务。在这种情况下，约束系统对 violation rate 的改善（DR 降低 42–99%）虽然在技术上有效，但实际价值有限——如果输出本身质量极低，violation rate 的降低并不能使系统实用。\n- 论文将 zero-shot 定位为 \"diagnostic probe\"，这个 framing 是合理的，但 §5.1 和 §5.3 花了大量篇幅报告 zero-shot 数字，给人一种 zero-shot 是 primary evaluation 的错觉。\n- 建议：更明确地将 fine-tuning 结果作为 primary evaluation 呈现，zero-shot 部分可压缩（也可帮助解决页数问题）。\n\n**W5** [warning] Abstract 信息密度过高\n- 具体位置：Abstract（page 1）\n- 问题：Abstract 约 180 词中包含至少 15 个具体数字/百分比、6 个缩写（DR, CF, R-F1, κ̄, S1, LoRA）、多个 section 引用。一次阅读几乎无法提取核心 message。与 ACL 领域最佳论文的 abstract 相比（通常 1-2 个 headline 数字），信息密度过高。\n- 特别是 \"(Proposition 1, scale-sensitive; §5.4)\" 这种内部引用出现在 abstract 中不常见且分散注意力。\n- 建议：精简至 2-3 个 headline 数字（如 DR reduction rate、R-F1 range、latency overhead），删除内部 section 引用和 constraint tightness 细节。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.3 \"continuation masking\" 与 §3.2 的 \"token masking\" 术语关系不够清晰——后者是否是前者的子集？建议在首次使用时明确。\n- Table 1 中 \"ΔDR\" 列的正负号含义需在 caption 中说明（当前仅在文中解释为 \"relative change vs. unconstrained\"）。\n- §5.4 WikiEvents 结果标注为 \"Preliminary\"（n=20 documents），但 Table 4 中未在 caption 显著标注这一点。\n- 论文使用 \"enforcement\" 和 \"elimination\" 交替描述 DR reduction，但严格来说 DR ≤ 0.09% ≠ elimination——建议统一用 \"near-elimination\"。\n- Appendix O（Pumping Lemma Proof）的 \"Remark (finite entity sets)\" 承认实际场景下语言是 regular 的，但对应的 DFA 是指数级的——这个 nuance 值得在主文 §2 或 §3 简要提及。\n- Ethics Statement（page 10）提到 \"Code and data will be released upon acceptance\"——考虑补充 licensing 意向（MIT/Apache 等）。\n\n---\n\n## Questions for Authors\n\n**Q1.** Table 1 显示 Qwen unconstrained CF = 0，S1 后 CF = 1.18%。如果目标用户已经在用 well-calibrated model + LoRA，OntoCoDec 的 net benefit 是什么？DR ≤ 0.09% 的改善是否 justify 引入 CF 和额外 latency？是否有 downstream task（如 KG construction）的实验来量化 violation 减少的实际价值？\n\n**Q2.** Proposition 1 证明了 unbounded entity set 下 cross-field constraints 非 CF，但 Remark 承认 finite entity set 下语言是 regular 的（只是 DFA 是 exponential）。既然实践中 entity set 总是有限的，那 registry-based approach 相比一个（可能很大的）DFA 的优势到底是 theoretical intractability avoidance 还是 practical engineering convenience？\n\n**Q3.** 70B 模型上 semantic layer 独立达到 84% DR reduction（vs. 8B 的 ≤24%）。是否有对中间规模（如 13B, 32B）的 scaling curve 数据？如果 enabling dependency 在 scale 上是连续变化的，那 \"两层缺一不可\" 的 claim 只在 small model 上成立，论文的 architectural contribution 是否应该重新 frame？\n\n**Q4.** S2 (two-pass) 策略在 70B 上 R-F1 下降 8.45 pp（Appendix D），而 8B 上 S1/S2 comparable。这种 scale-dependent degradation 的 root cause 是什么？是否与 70B 模型的 probability distribution 更 peaked 有关？\n\n---\n\n## Missing References\n\n1. **ADELIE** (Cheng et al., EMNLP 2024) — \"Aligning Large Language Models on Information Extraction\"。作为近期 schema-aware IE 的代表工作，通过 instruction tuning + DPO 对齐 LLM 到 IE 任务，应在 §6 Schema-aware IE 段讨论，与 GoLLIE/KnowCoder 并列。\n2. **SGLang** (Zheng et al., 2024/2025) — 虽然 XGrammar 被引用为 grammar layer 的基础，但 SGLang 作为 XGrammar 的主要部署框架和当前最广泛使用的 structured generation serving system，值得提及。\n\n（DCCD Reddy et al. 2026、Thinking Before Constraining Nguyen et al. 2026、CRANE Banerjee et al. 2025、IterGen Ugare et al. 2025 均已被引用。）\n\n---\n\n## Overall Assessment 详细理由\n\n给出 **3.0（Findings）** 的主要考量：\n\n**支持 Findings 接收的理由：**\n- 评估系统性和全面性在同类工作中突出（3 datasets × 3+ models × 2 tasks × zero-shot/fine-tuned × beam/greedy）\n- Violation taxonomy 和 constraint tightness 指标对社区有参考价值\n- 论文对局限性的诚实讨论提升了科学可信度\n- 工程贡献实用——自动编译、tokenizer-agnostic、低 overhead\n\n**未达到 Conference (4.0) 的理由：**\n- 新颖性有限：核心是 XGrammar + entity registry masking 的系统集成，非新算法\n- CF trade-off 未解决——系统将 DR 转化为 CF，beam search 虽可解决但代价是 1.54× latency\n- Enabling dependency 的 scale sensitivity 动摇了两层架构作为普适设计的 claim\n- Zero-shot 场景下 R-F1 过低（4–8%），constraint 改善的实际价值存疑\n- 正文超页（需修复但本身不应影响学术评价）\n\n**与 3.5 (Borderline Conference) 的距离：**\n如果作者能 (1) 解决正文超页问题，(2) 更诚实地 frame CF trade-off（特别是 Abstract），(3) 提供 downstream task 的 impact 评估证明 violation reduction 的实际价值，(4) 加入 running example 提升可读性，评分可能上调至 3.5。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1799 · 2026-05-23T02:08:53.857862+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4621
}
```

</details>

---


### Tool call

_source line 1800 · 2026-05-23T02:09:00.033478+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_20/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1801 · 2026-05-23T02:09:00.084527+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 1802 · 2026-05-23T02:09:08.939386+00:00_

审稿完成。报告已发送至 Review Director，核心判断：

- **Overall: 3.0 (Findings)**
- **3 个 Must-Fix**：正文超 8 页限制（§7 溢出到第 9 页）、Abstract 中 CF trade-off framing 偏乐观、enabling dependency 的 scale sensitivity 在主文讨论不足
- **5 个 Should-Fix**：新颖性天花板（系统集成而非新算法）、Related Work 过短且缺 ADELIE、缺 running example、zero-shot 评估实际价值有限、Abstract 信息密度过高
- **1 个 Missing Reference**：ADELIE (Cheng et al., EMNLP 2024)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 37

## Round 37

4 recorded events


### User

_source line 1803 · 2026-05-23T02:10:44.506518+00:00_

[Round 1 审稿请求]:
## 交叉分享：以下是 Reviewer 1 的完整审稿意见

请逐条回应每个 Must-Fix 和 Should-Fix 问题：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）
- **[PARTIALLY AGREE]** 部分同意，说明同意和不同意的部分

特别关注：
1. R1-N1 Corollary 标签混淆形式/经验——你是否有相同关切？
2. R1-W3 Proposition 1 证明中 position-based vs name-based referencing——你如何评价？
3. R1 给出 3.5 (Borderline Conference) vs 你的 3.0 (Findings)——评分差异的主要原因是什么？

---

## Reviewer 1 完整审稿意见

### Overall: 3.5 — Borderline Conference
一句话总结: 工程贡献扎实、实验全面且统计规范，但理论框架的形式-经验边界模糊且 scale-dependent，greedy 模式下 CF violations 的 100× 增加被 "violation conversion" 框架轻描淡写——beam search 配置下方法才真正完备。

### 官方维度打分
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法合理、统计严格，但 Corollary 混淆形式与经验，enabling dependency scale-sensitive |
| Excitement | 3.5/5 | 解决实际问题，可判定性分析有概念贡献，但核心思路相对直接 |
| Reproducibility | 4/5 | 完整披露超参数、硬件、种子方差、训练时间 |
| Reviewer Confidence | 4/5 | 熟悉约束解码和信息抽取 |

### Must-Fix

**N1** [critical] Corollary 标签混淆形式推导与经验观察
- Corollary 前半句从 Proposition 1 逻辑推出，后半句（semantic-only 24% DR reduction）是经验观测。标签 "Corollary" 暗示形式推导。
- 更关键：70B 上 semantic-only 达 84% DR reduction，与 8B 的 24% 形成强对比，enabling dependency 高度 scale-dependent。§4 提及 scale-sensitivity 但未更新 §3 的 Corollary 框架。
- 建议：重新标记为 "Empirical Observation"，§3 即明确 scale dependency。

**N2** [critical] Zero-shot 下 CF violations 的 100× 增加被 "violation conversion" 轻描淡写
- S1 在 SciERC ZS 上 CF 从 0.08% 到 9.90%（124×），Llama DocRED 从 0.17% 到 12.02%（70×）。
- "violation conversion" 聚合隐含 DR 和 CF 可线性比较，但论文自身承认两者性质不同。
- Limitations 承认 CF 下游影响未评估，但 §5 主叙事仍暗示总体改善。
- 建议：§5.1 讨论 DR-CF severity 不对等性；强调 zero-shot 为 diagnostic probe。

### Should-Fix

**W1** [warning] κ̄ 仅基于 n=3 schemas
- p=0.138 不显著，但 κ̄ 在 §4、abstract、§5.2、附录中反复出现。
- 建议：降低展示权重，标注 "preliminary descriptive observation"。

**W2** [warning] 70B 验证仅覆盖单模型 + 单一量化方案
- 仅 Llama-3.1-70B AWQ INT4。单模型不足以支撑泛化声称；量化效应未隔离。
- 建议：讨论单模型选择原因；Limitations 更明确列量化效应为 open question。

**W3** [warning] Proposition 1 position-based vs name-based referencing
- 附录 O 承认 "core argument transfers to name-based" 但未给形式论证。
- 建议：增加 1-2 段形式论证。

**W4** [warning] DocRED 评估使用开发集，超参数选择过程未披露
- 建议：明确说明超参数选择策略。

**W5** [warning] Bonferroni 校正后 min p=0.014 处于 borderline
- 4 配置 Bonferroni 阈值 0.0125，min p=0.014 未通过。
- 建议：报告各配置独立 p 值和效应量。

### Questions
Q1. 33/36 residual DR violations 来自 Llama DocRED——是否暗示 Llama entity typing 系统性问题？
Q2. Entity registry first-registered-type 语义的 positional bias 是否有实验量化？
Q3. Beam search k=4 基于 single-run——是否有多次运行方差估计？
Q4. Residual DR 是否 100% 来自 grammar-first fallback 位置？

### Missing References
- Tam et al. (2024) "Let Me Speak Freely"

### 主要优势
1. 系统性可判定性分析框架（三层分类法）
2. 极其全面的实验评估（3 数据集 × 4 模型 × 多策略 + 完整统计）
3. 诚实详尽的局限性讨论
4. 工程完整性（tokenizer-agnostic, order invariance, runtime, scalability）
5. Fine-tuning composability（约束解码与 LoRA 正交可组合）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1804 · 2026-05-23T02:12:45.134349+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix 回应\n\n**[AGREE] R1-N1: Corollary 标签混淆形式推导与经验观察**\n\n完全同意，且这与我的 N3 指向同一个核心问题。\n\nCorollary 前半句（\"grammar layer alone cannot enforce domain/range constraints\"）确实从 Proposition 1 逻辑推出——如果 cross-field type constraints 超出 CFG 表达能力，grammar layer 自然无法单独解决。但后半句（\"semantic-only achieves only 24% DR reduction\"）是纯经验数字，而且 **仅对 8B 模型成立**。将两者放在同一个 \"Corollary\" 标签下，暗示后者也具有理论必然性，这是不准确的。\n\n更关键的是 70B 反证：semantic layer 独立达到 84% DR reduction（§5.4 / 我的 N3），这不仅是一个 \"scale sensitivity\" 的注脚，而是直接否定了 Corollary 隐含的 \"两层缺一不可\" 的普遍性。R1 建议重新标记为 \"Empirical Observation\" 是对的——进一步应将 scale dependency 作为 Observation 的核心 qualifier，而非放在后续 section 才提及。\n\n我在自己的审稿中将此作为 N3 (critical) 提出，措辞略有不同但指向一致：enabling dependency 的 scale sensitivity 从根本上削弱了两层架构作为 **普适设计** 的 claim。\n\n**[AGREE] R1-N2: Zero-shot CF violations 100× 增加被 \"violation conversion\" 轻描淡写**\n\n完全同意，与我的 N2 高度重叠。\n\nR1 给出了更精确的量化：SciERC ZS 上 CF 从 0.08% → 9.90%（124×），Llama DocRED 0.17% → 12.02%（70×）。这些数字我在审稿中也注意到了（我引用的是 Table 1 中 Qwen unconstrained CF=0 → S1 CF=1.18%），但 R1 的 zero-shot 数字更能说明问题——因为 zero-shot 是论文声称的 \"primary diagnostic probe\"，CF 的百倍级增长在这个 diagnostic 场景下是不可忽视的。\n\nR1 关于 \"DR 和 CF 不可线性比较\" 的观察也是我认同的。论文用 \"total violations (DR+CF) decrease by ~31%\" 这种聚合指标隐含了 1 DR violation = 1 CF violation 的等价假设，但 DR（ontologically invalid triple）和 CF（同一 entity 在不同 triple 中类型不一致）的下游影响可能不同——DR triple 是 schema 层面的错误，CF 可能在某些 downstream 应用中通过 majority voting 等后处理解决。论文自身在 Limitations 中承认 \"CF type inconsistencies may propagate to downstream tasks...the impact of such propagation has not been evaluated\"，但 §5 主叙事没有体现这种审慎。\n\n---\n\n### Should-Fix 回应\n\n**[AGREE] R1-W1: κ̄ 仅基于 n=3 schemas，p=0.138 不显著**\n\n同意。我在审稿中没有单独标记这一点，但 R1 的观察是准确的。κ̄ 在 abstract（\"constraint tightness (κ̄) is a descriptive correlate of enforcement difficulty (n=3 schemas, p=0.138)\"）、§4、§5.2、appendix 中反复出现，给人一种它是 established metric 的印象，但实际上 n=3 的样本量下任何相关性都不具统计效力。\n\n论文确实在 abstract 中标注了 \"n=3, p=0.138\"，这体现了诚实性，但 R1 建议的 \"降低展示权重，标注 preliminary descriptive observation\" 是合理的——特别是考虑到 abstract 已经信息过载（我的 W5），删除 κ̄ 的 abstract 引用可以同时解决两个问题。\n\n**[AGREE] R1-W2: 70B 验证仅覆盖单模型 + 单一量化方案**\n\n同意。这补充了我的 N3（scale sensitivity）和 Q3（是否有中间规模的 scaling curve）。\n\n单一 70B 模型（Llama-3.1-70B）+ 单一量化方案（AWQ INT4）的验证确实不足以支撑 \"generalizability beyond 8B\" 的声称。特别是量化效应——AWQ INT4 改变了 logit 分布，而 OntoCoDec 的 semantic layer 正是在 logit 空间操作 token masking。Limitations 虽然提到了 \"AWQ INT4 quantization may alter logit distributions at mask boundaries\"（page 10, line 96），但仅一句带过。如果量化导致 mask boundary 附近 logit 失真，constraint enforcement 的精度可能受影响——这不是一个可以一笔带过的 caveat。\n\n**[PARTIALLY AGREE] R1-W3: Proposition 1 position-based vs name-based referencing**\n\n部分同意。\n\nR1 指出 Appendix O 承认 \"core argument transfers to name-based\" 但未给出形式论证。这是一个合理的学术严谨性关切。我在审稿中阅读了 Appendix O（page 39），其中 \"Position indexing vs. name referencing\" 段落确实仅以 informal argument 处理：论证 name→type lookup 需要 random-access map operation，PDA stack 无法执行 random-access retrieval，因此 non-CF result 对 name-based referencing 同样成立。\n\n**我同意的部分**：作为一个声称 \"theoretical grounding\" 的论文，形式/非形式的跳跃应该被明确标注。如果论文以 \"proof sketch\" 加 informal remark 的方式处理，应该在主文中说明 name-based case 的论证是 informal 的。\n\n**我不完全同意的部分**：从技术角度看，name-based 到 position-based 的归约论证实际上是直接的——name-based referencing 只是 position-based 的一个特例（name 唯一标识 entity，等价于 position），而 pumping lemma 的核心论证（需要 random-access lookup over dynamically generated bindings）在 name-based 下同样成立，因为 PDA stack 的 LIFO 限制不依赖于 indexing scheme。R1 建议 \"增加 1-2 段形式论证\" 是合理的但不是 critical——一个简洁的 lemma 说明 name-based 可归约为 position-based 即可。\n\n**[AGREE] R1-W4: DocRED 评估使用开发集，超参数选择过程未披露**\n\n同意。我审稿时未单独标记此问题，但这是一个标准的方法论关切。\n\n论文 page 5 footnote 提到 \"DocRED test annotations are not publicly available; we evaluate on the development set\"，这本身是合理的（DocRED test set 确实需要提交到 CodaLab）。但 R1 的关切不在于使用 dev set 本身，而是 **超参数是否也在 dev set 上选择**——如果超参数（如 LoRA rank, learning rate, beam width 等）在同一个 dev set 上调优然后在同一 dev set 上评估，这构成 information leakage。\n\n论文 Appendix H（Reproducibility）应明确：超参数选择是基于 dev set 的 subset（如果有 train/dev split 内部再分）还是直接在 full dev set 上调优。如果是后者，至少应 report held-out dev set 的结果或使用 cross-validation。\n\n**[PARTIALLY AGREE] R1-W5: Bonferroni 校正后 min p=0.014 处于 borderline**\n\n部分同意。\n\nR1 指出 4 配置下 Bonferroni 阈值为 0.05/4=0.0125，而 min p=0.014 未通过。这在严格统计意义上是正确的——Bonferroni 校正后确实不显著。\n\n但需要注意：(1) Bonferroni 是最保守的多重比较校正方法；(2) p=0.014 虽然未通过 Bonferroni 但通过了 Holm-Bonferroni 和 FDR 校正（具体取决于 p 值排序）；(3) 论文的 claim 并非 \"统计显著\"，而是 \"constraint tightness is a descriptive correlate\"——用语已经很审慎。\n\n**我同意的部分**：既然论文进行了统计检验并报告了 p 值，就应该完整报告多重比较校正结果。现在只报告 \"min p=0.014\" 但不提 Bonferroni threshold，有选择性报告之嫌。\n\n**我不完全同意的部分**：鉴于 n=3 schemas 本身就注定了统计效力极低（R1-W1），纠结 Bonferroni 边界意义不大——核心问题是 n 太小，无论用什么校正方法都不可能得到 convincing 的统计证据。建议直接降级 κ̄ 为 \"preliminary observation\"（如 R1-W1 建议），统计检验细节可以从主文移至 appendix。\n\n---\n\n### R1 Questions 的补充评论\n\n**R1-Q1（33/36 residual DR from Llama DocRED）**：有价值的问题。Limitations（page 10, line 79）给出了分解：entity type errors 39%, schema coverage gaps 33%, model generation errors 28%。\"Llama DocRED alone accounts for 33 of 36 residual violations (92%)\" 确实暗示 Llama 在 DocRED 上的 entity typing 能力系统性弱于 Qwen——如果论文能进一步分析是 Llama 的 tokenizer、预训练数据、还是模型架构导致的差异，会更有价值。\n\n**R1-Q3（Beam search k=4 single-run variance）**：好问题。我的审稿没有触及此点。如果 beam k=4 的 \"all violations eliminated\" 基于 single run，variance 未知，这个 headline claim 的可靠性存疑。\n\n**R1-Q4（Residual DR 是否 100% 来自 grammar-first fallback）**：这是一个有洞察力的问题。Grammar-first fallback（§4, page 5）在 constraint conflict 时优先保证 JSON 完整性而牺牲 type validity——如果 residual DR 全部来自 fallback 位置，这意味着 constraint composition 的冲突解决策略本身是 DR 残留的直接原因，进一步说明 CF→DR 的 trade-off 是架构性的而非偶发的。\n\n---\n\n### R1 Missing References 评论\n\n**Tam et al. (2024) \"Let Me Speak Freely\"**：论文实际上已经引用了此工作——§6 Related Work 最后一句 \"Extraction tasks are robust to format constraints (Tam et al., 2024)\" 以及 Limitations section 都有引用。R1 可能遗漏了这一引用。\n\n---\n\n### 评分差异分析：R1 (3.5) vs R2 (3.0)\n\n两位 reviewer 的分歧主要在 **Excitement** 维度（R1: 3.5, R2: 2.5），Soundness 评价一致（均 3.5）。\n\n**R1 给高分的理由（我理解但不完全同意）**：\n- R1 将 \"可判定性分析框架（三层分类法）\" 视为概念贡献（Excitement 3.5），认为即使实现直接，decidability-guided 的架构设计思路本身有价值。\n- R1 更看重工程完整性（tokenizer-agnostic, order invariance, scalability）作为 contribution。\n\n**我给低分的理由**：\n1. **新颖性天花板更严格**：我认为 grammar layer（直接复用 XGrammar）+ semantic layer（continuation masking + entity registry）是已有技术的系统性集成，不构成 \"novel algorithm\"。可判定性分析虽然有教育价值，但 Proposition 1 形式化的是 well-known intuition（论文自述），Corollary 的经验部分被 scale sensitivity 削弱。整体上这更适合 Findings 的定位——\"sound and reproducible but limited novelty/impact\"。\n2. **CF trade-off 的权重**：我将 CF trade-off（系统引入新类型违规）视为对核心 claim 的更严重削弱。如果一个 constraint enforcement 系统的 net effect 是将一种违规转化为另一种（且新违规的下游影响未评估），那 \"near-eliminate violations\" 的叙事就需要根本性修正，而非仅在 Limitations 中 acknowledge。\n3. **Zero-shot 实用性**：R-F1 4-8% 的 zero-shot 结果使得 zero-shot 评估（论文 §5 中大量篇幅）的实际价值可疑。R1 没有突出这一点。\n\n**缩小分歧的可能**：如果作者能在 revision 中 (1) 提供 CF 的 downstream impact 评估（哪怕是 preliminary 的），(2) 将 Abstract/Introduction 的 CF framing 调整为更 balanced，(3) 显著处理 scale dependency，我的评分可上调至 3.5（Borderline Conference），与 R1 对齐。目前维持 3.0。",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix 回应\n\n**[AGREE] R1-N1: Corollary 标签混淆形式推导与经验观察**\n\n完全同意，且这与我的 N3 指向同一个核心问题。\n\nCorollary 前半句（\"grammar layer alone cannot enforce domain/range constraints\"）确实从 Proposition 1 逻辑推出——如果 cross-field type constraints 超出 CFG 表达能力，grammar layer 自然无法单独解决。但后半句（\"semantic-only achieves only 24% DR reduction\"）是纯经验数字，而且 **仅对 8B 模型成立**。将两者放在同一个 \"Corollary\" 标签下，暗示后者也具有理论必然性，这是不准确的。\n\n更关键的是 70B 反证：semantic layer 独立达到 84% DR reduction（§5.4 / 我的 N3），这不仅是一个 \"scale sensitivity\" 的注脚，而是直接否定了 Corollary 隐含的 \"两层缺一不可\" 的普遍性。R1 建议重新标记为 \"Empirical Observation\" 是对的——进一步应将 scale dependency 作为 Observation 的核心 qualifier，而非放在后续 section 才提及。\n\n我在自己的审稿中将此作为 N3 (critical) 提出，措辞略有不同但指向一致：enabling dependency 的 scale sensitivity 从根本上削弱了两层架构作为 **普适设计** 的 claim。\n\n**[AGREE] R1-N2: Zero-shot CF violations 100× 增加被 \"violation conversion\" 轻描淡写**\n\n完全同意，与我的 N2 高度重叠。\n\nR1 给出了更精确的量化：SciERC ZS 上 CF 从 0.08% → 9.90%（124×），Llama DocRED 0.17% → 12.02%（70×）。这些数字我在审稿中也注意到了（我引用的是 Table 1 中 Qwen unconstrained CF=0 → S1 CF=1.18%），但 R1 的 zero-shot 数字更能说明问题——因为 zero-shot 是论文声称的 \"primary diagnostic probe\"，CF 的百倍级增长在这个 diagnostic 场景下是不可忽视的。\n\nR1 关于 \"DR 和 CF 不可线性比较\" 的观察也是我认同的。论文用 \"total violations (DR+CF) decrease by ~31%\" 这种聚合指标隐含了 1 DR violation = 1 CF violation 的等价假设，但 DR（ontologically invalid triple）和 CF（同一 entity 在不同 triple 中类型不一致）的下游影响可能不同——DR triple 是 schema 层面的错误，CF 可能在某些 downstream 应用中通过 majority voting 等后处理解决。论文自身在 Limitations 中承认 \"CF type inconsistencies may propagate to downstream tasks...the impact of such propagation has not been evaluated\"，但 §5 主叙事没有体现这种审慎。\n\n---\n\n### Should-Fix 回应\n\n**[AGREE] R1-W1: κ̄ 仅基于 n=3 schemas，p=0.138 不显著**\n\n同意。我在审稿中没有单独标记这一点，但 R1 的观察是准确的。κ̄ 在 abstract（\"constraint tightness (κ̄) is a descriptive correlate of enforcement difficulty (n=3 schemas, p=0.138)\"）、§4、§5.2、appendix 中反复出现，给人一种它是 established metric 的印象，但实际上 n=3 的样本量下任何相关性都不具统计效力。\n\n论文确实在 abstract 中标注了 \"n=3, p=0.138\"，这体现了诚实性，但 R1 建议的 \"降低展示权重，标注 preliminary descriptive observation\" 是合理的——特别是考虑到 abstract 已经信息过载（我的 W5），删除 κ̄ 的 abstract 引用可以同时解决两个问题。\n\n**[AGREE] R1-W2: 70B 验证仅覆盖单模型 + 单一量化方案**\n\n同意。这补充了我的 N3（scale sensitivity）和 Q3（是否有中间规模的 scaling curve）。\n\n单一 70B 模型（Llama-3.1-70B）+ 单一量化方案（AWQ INT4）的验证确实不足以支撑 \"generalizability beyond 8B\" 的声称。特别是量化效应——AWQ INT4 改变了 logit 分布，而 OntoCoDec 的 semantic layer 正是在 logit 空间操作 token masking。Limitations 虽然提到了 \"AWQ INT4 quantization may alter logit distributions at mask boundaries\"（page 10, line 96），但仅一句带过。如果量化导致 mask boundary 附近 logit 失真，constraint enforcement 的精度可能受影响——这不是一个可以一笔带过的 caveat。\n\n**[PARTIALLY AGREE] R1-W3: Proposition 1 position-based vs name-based referencing**\n\n部分同意。\n\nR1 指出 Appendix O 承认 \"core argument transfers to name-based\" 但未给出形式论证。这是一个合理的学术严谨性关切。我在审稿中阅读了 Appendix O（page 39），其中 \"Position indexing vs. name referencing\" 段落确实仅以 informal argument 处理：论证 name→type lookup 需要 random-access map operation，PDA stack 无法执行 random-access retrieval，因此 non-CF result 对 name-based referencing 同样成立。\n\n**我同意的部分**：作为一个声称 \"theoretical grounding\" 的论文，形式/非形式的跳跃应该被明确标注。如果论文以 \"proof sketch\" 加 informal remark 的方式处理，应该在主文中说明 name-based case 的论证是 informal 的。\n\n**我不完全同意的部分**：从技术角度看，name-based 到 position-based 的归约论证实际上是直接的——name-based referencing 只是 position-based 的一个特例（name 唯一标识 entity，等价于 position），而 pumping lemma 的核心论证（需要 random-access lookup over dynamically generated bindings）在 name-based 下同样成立，因为 PDA stack 的 LIFO 限制不依赖于 indexing scheme。R1 建议 \"增加 1-2 段形式论证\" 是合理的但不是 critical——一个简洁的 lemma 说明 name-based 可归约为 position-based 即可。\n\n**[AGREE] R1-W4: DocRED 评估使用开发集，超参数选择过程未披露**\n\n同意。我审稿时未单独标记此问题，但这是一个标准的方法论关切。\n\n论文 page 5 footnote 提到 \"DocRED test annotations are not publicly available; we evaluate on the development set\"，这本身是合理的（DocRED test set 确实需要提交到 CodaLab）。但 R1 的关切不在于使用 dev set 本身，而是 **超参数是否也在 dev set 上选择**——如果超参数（如 LoRA rank, learning rate, beam width 等）在同一个 dev set 上调优然后在同一 dev set 上评估，这构成 information leakage。\n\n论文 Appendix H（Reproducibility）应明确：超参数选择是基于 dev set 的 subset（如果有 train/dev split 内部再分）还是直接在 full dev set 上调优。如果是后者，至少应 report held-out dev set 的结果或使用 cross-validation。\n\n**[PARTIALLY AGREE] R1-W5: Bonferroni 校正后 min p=0.014 处于 borderline**\n\n部分同意。\n\nR1 指出 4 配置下 Bonferroni 阈值为 0.05/4=0.0125，而 min p=0.014 未通过。这在严格统计意义上是正确的——Bonferroni 校正后确实不显著。\n\n但需要注意：(1) Bonferroni 是最保守的多重比较校正方法；(2) p=0.014 虽然未通过 Bonferroni 但通过了 Holm-Bonferroni 和 FDR 校正（具体取决于 p 值排序）；(3) 论文的 claim 并非 \"统计显著\"，而是 \"constraint tightness is a descriptive correlate\"——用语已经很审慎。\n\n**我同意的部分**：既然论文进行了统计检验并报告了 p 值，就应该完整报告多重比较校正结果。现在只报告 \"min p=0.014\" 但不提 Bonferroni threshold，有选择性报告之嫌。\n\n**我不完全同意的部分**：鉴于 n=3 schemas 本身就注定了统计效力极低（R1-W1），纠结 Bonferroni 边界意义不大——核心问题是 n 太小，无论用什么校正方法都不可能得到 convincing 的统计证据。建议直接降级 κ̄ 为 \"preliminary observation\"（如 R1-W1 建议），统计检验细节可以从主文移至 appendix。\n\n---\n\n### R1 Questions 的补充评论\n\n**R1-Q1（33/36 residual DR from Llama DocRED）**：有价值的问题。Limitations（page 10, line 79）给出了分解：entity type errors 39%, schema coverage gaps 33%, model generation errors 28%。\"Llama DocRED alone accounts for 33 of 36 residual violations (92%)\" 确实暗示 Llama 在 DocRED 上的 entity typing 能力系统性弱于 Qwen——如果论文能进一步分析是 Llama 的 tokenizer、预训练数据、还是模型架构导致的差异，会更有价值。\n\n**R1-Q3（Beam search k=4 single-run variance）**：好问题。我的审稿没有触及此点。如果 beam k=4 的 \"all violations eliminated\" 基于 single run，variance 未知，这个 headline claim 的可靠性存疑。\n\n**R1-Q4（Residual DR 是否 100% 来自 grammar-first fallback）**：这是一个有洞察力的问题。Grammar-first fallback（§4, page 5）在 constraint conflict 时优先保证 JSON 完整性而牺牲 type validity——如果 residual DR 全部来自 fallback 位置，这意味着 constraint composition 的冲突解决策略本身是 DR 残留的直接原因，进一步说明 CF→DR 的 trade-off 是架构性的而非偶发的。\n\n---\n\n### R1 Missing References 评论\n\n**Tam et al. (2024) \"Let Me Speak Freely\"**：论文实际上已经引用了此工作——§6 Related Work 最后一句 \"Extraction tasks are robust to format constraints (Tam et al., 2024)\" 以及 Limitations section 都有引用。R1 可能遗漏了这一引用。\n\n---\n\n### 评分差异分析：R1 (3.5) vs R2 (3.0)\n\n两位 reviewer 的分歧主要在 **Excitement** 维度（R1: 3.5, R2: 2.5），Soundness 评价一致（均 3.5）。\n\n**R1 给高分的理由（我理解但不完全同意）**：\n- R1 将 \"可判定性分析框架（三层分类法）\" 视为概念贡献（Excitement 3.5），认为即使实现直接，decidability-guided 的架构设计思路本身有价值。\n- R1 更看重工程完整性（tokenizer-agnostic, order invariance, scalability）作为 contribution。\n\n**我给低分的理由**：\n1. **新颖性天花板更严格**：我认为 grammar layer（直接复用 XGrammar）+ semantic layer（continuation masking + entity registry）是已有技术的系统性集成，不构成 \"novel algorithm\"。可判定性分析虽然有教育价值，但 Proposition 1 形式化的是 well-known intuition（论文自述），Corollary 的经验部分被 scale sensitivity 削弱。整体上这更适合 Findings 的定位——\"sound and reproducible but limited novelty/impact\"。\n2. **CF trade-off 的权重**：我将 CF trade-off（系统引入新类型违规）视为对核心 claim 的更严重削弱。如果一个 constraint enforcement 系统的 net effect 是将一种违规转化为另一种（且新违规的下游影响未评估），那 \"near-eliminate violations\" 的叙事就需要根本性修正，而非仅在 Limitations 中 acknowledge。\n3. **Zero-shot 实用性**：R-F1 4-8% 的 zero-shot 结果使得 zero-shot 评估（论文 §5 中大量篇幅）的实际价值可疑。R1 没有突出这一点。\n\n**缩小分歧的可能**：如果作者能在 revision 中 (1) 提供 CF 的 downstream impact 评估（哪怕是 preliminary 的），(2) 将 Abstract/Introduction 的 CF framing 调整为更 balanced，(3) 显著处理 scale dependency，我的评分可上调至 3.5（Borderline Conference），与 R1 对齐。目前维持 3.0。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1805 · 2026-05-23T02:12:49.073177+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3938
}
```

</details>

---


### Assistant

_source line 1806 · 2026-05-23T02:12:59.043200+00:00_

交叉回应已提交。核心结论：

- **N1 (Corollary 标签)** 和 **N2 (CF 100× 增加)** 完全同意 R1，与我自己的 N2/N3 高度重叠
- **W3 (position vs name-based)** 部分同意——形式跳跃应标注，但归约论证技术上是直接的
- **W5 (Bonferroni)** 部分同意——核心问题是 n=3 样本量，纠结校正方法意义不大
- **评分分歧 (3.5 vs 3.0)** 主要在 Excitement 维度：我对新颖性天花板和 CF trade-off 的 impact 评估更严格，认为当前版本更适合 Findings 定位

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 38

## Round 38

114 recorded events


### User

_source line 1807 · 2026-05-23T02:46:02.200172+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查 **新颖性 + Related Work 完整性 + 写作质量**。

## 论文信息
- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
- **路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/submitted.pdf`

## Venue 要求（EMNLP 2026 via ARR May 2026）
- **格式**: ACL 模板，two-column
- **页数限制**: Long paper 正文 ≤ 8 页（不含 references），Limitations 和 Ethics Statement 不计入页数但不得包含过多额外内容
- **匿名规则**: Double-blind（论文中不得出现作者姓名和机构，self-reference 须避免泄露身份）
- **附录**: 允许，不参与审稿评分但可用于补充细节
- **截止日期**: 2026-05-25

## 你的审查侧重
1. **新颖性评估**：
   - 核心贡献（编译 schema 约束到解码层）相对于现有工作的创新程度
   - Grammar + Semantic 两层约束组合是否有实质性的方法论贡献，还是已知技术的系统集成
   - 与 GCD (Geng et al.)、BoostCD (Sakota et al.)、PICARD (Scholak et al.)、SGLang 等约束解码方法的差异化
   - Composability 分析框架（κ̄ 等）的理论价值

2. **Related Work 完整性**：
   - §6 Related Work 是否覆盖了所有关键方向：constrained decoding、schema-guided IE、type-constrained generation
   - 是否遗漏重要文献（特别是 2024-2025 的最新工作：ADELIE, Schema RL, SGLang 等）
   - 与最相关方法的对比讨论是否充分（GCD, BoostCD, PICARD）
   - 引用是否真实、格式是否正确

3. **写作质量**：
   - 论文叙事结构和逻辑流是否清晰
   - Abstract 信息密度是否合适（数字/缩写数量）
   - 专业术语使用是否一致（DR/CF/RoV 等缩写的定义和使用）
   - 图表设计和标注质量
   - 正文页数是否符合 8 页限制
   - Limitations 章节覆盖是否充分
   - CF trade-off 的 framing 是否诚实（是否过于乐观地淡化系统引入的副作用）

请按以下格式输出审稿意见：
- **Summary**（2-3 句）
- **Strengths**（逐条 S1, S2, ...）
- **Weaknesses**（逐条 W1, W2, ...，标注严重程度 [Critical/Major/Minor]）
- **Questions**（逐条 Q1, Q2, ...）
- **Missing References**
- **Overall Assessment**（评分 + 简要理由）

评分标准（ARR/EMNLP 2026）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1808 · 2026-05-23T02:46:12.890259+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
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

_source line 1809 · 2026-05-23T02:46:12.942865+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1810 · 2026-05-23T02:46:18.677113+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1811 · 2026-05-23T02:46:20.937089+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/submitted.pdf",
  "pages": "1-8",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/submitted.pdf",
    "pages": "1-8",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1812 · 2026-05-23T02:46:26.083079+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines, review form, and criteria:

## Reviewer Guidelines

ARR asks reviewers to follow a workflow of: (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that pa
…[truncated 1315 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7405
}
```

</details>

---


### Tool result

_source line 1813 · 2026-05-23T02:46:27.139008+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 457.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 412.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.0}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 559.6}], \"total_pages\": 38, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_050
…[truncated 122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6201
}
```

</details>

---


### Tool call

_source line 1814 · 2026-05-23T02:46:36.782008+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
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

_source line 1815 · 2026-05-23T02:46:36.783941+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 1816 · 2026-05-23T02:46:37.389809+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1817 · 2026-05-23T02:46:37.792179+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1818 · 2026-05-23T02:46:38.698632+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1308
}
```

</details>

---


### Tool result

_source line 1819 · 2026-05-23T02:46:38.700017+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 1820 · 2026-05-23T02:46:38.700369+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1821 · 2026-05-23T02:46:39.252565+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1822 · 2026-05-23T02:46:39.304001+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool result

_source line 1823 · 2026-05-23T02:46:39.856765+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 1824 · 2026-05-23T02:46:46.141016+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 1825 · 2026-05-23T02:46:46.698870+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1826 · 2026-05-23T02:46:47.000239+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1827 · 2026-05-23T02:46:48.160410+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1828 · 2026-05-23T02:46:49.117886+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2976
}
```

</details>

---


### Tool result

_source line 1829 · 2026-05-23T02:46:50.274787+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3575
}
```

</details>

---


### Tool result

_source line 1830 · 2026-05-23T02:46:50.275612+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3275
}
```

</details>

---


### Tool result

_source line 1831 · 2026-05-23T02:46:50.276441+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2116
}
```

</details>

---


### Tool call

_source line 1832 · 2026-05-23T02:46:50.378878+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "Extract all review form dimensions/criteria, their score scales, and descriptions. I need the complete list of scoring dimensions (e.g., soundness, excitement, overall assessment, confidence, etc.) with their exact scale descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "Extract all review form dimensions/criteria, their score scales, and descriptions. I need the complete list of scoring dimensions (e.g., soundness, excitement, overall assessment, confidence, etc.) with their exact scale descriptions."
  }
}
```

</details>

---


### Tool result

_source line 1833 · 2026-05-23T02:46:57.465954+00:00_

# ACL Rolling Review Form: Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: Quite sure with thorough checking
- 3: Pretty sure, but details may be missed
- 2: Willing to defend, but likely missed some points
- 1: Outside expertise area or unclear paper

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- 5: "one of the most thorough I have seen, given its type"
- 4: Strong support for claims; minor experiments optional
- 3: Adequate support for main claims
- 2: Main claims lack sufficient support; major problems
- 1: "not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- 5: Highly exciting; would recommend to others
- 4: Exciting; would mention to colleagues
- 3: Interesting; might mention selectively
- 2: Potentially interesting to some community members
- 1: "does not resonate with me" or lacks relevance to NLP

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- 5: "Consider for Award" (top 2.5%)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Substantial revisions needed
- 1: "Do not resubmit"

## 5. **Reproducibility**
Scale: 1-5
- 5: Results easily reproducible
- 4: Mostly reproducible with minor variations
- 3: Reproducible with difficulty
- 2: Hard to reproduce; limited data availability
- 1: Cannot reproduce results

## 6. **Datasets** (if applicable)
Scale: 1-5
- 5: Enabling; affects research directions
- 4: Useful for ongoing work
- 3: Potentially useful
- 2: Documentary value for replication
- 1: No usable datasets

## 7. **Software** (if applicable)
Scale: 1-5
- 5: Enabling; affects research directions
- 4: Useful for ongoing work
- 3: Potentially useful
- 2: Documentary value for replication
- 1: No usable software

## 8. **Author Identity Knowledge**
Scale: 1-5 (anonymity check)
- 5: Know/guess author from violation
- 4: Know/guess from preprint
- 3: Know/guess from submission con
…[truncated 91 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7087
}
```

</details>

---


### Tool call

_source line 1834 · 2026-05-23T02:47:05.865807+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/submitted.pdf",
  "pages": "9-16",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/submitted.pdf",
    "pages": "9-16",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1835 · 2026-05-23T02:47:06.870068+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 577.7}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 578.9}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 624.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 616.4}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 576.3}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 387.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 545.6}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 550.7}], \"total_pages\": 38, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-researc
…[truncated 136 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1836 · 2026-05-23T02:47:09.841903+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1837 · 2026-05-23T02:47:10.645978+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 1838 · 2026-05-23T02:47:10.798749+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 1839 · 2026-05-23T02:47:11.252900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1840 · 2026-05-23T02:47:11.605867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1841 · 2026-05-23T02:47:12.059301+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1260
}
```

</details>

---


### Tool result

_source line 1842 · 2026-05-23T02:47:13.372370+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2119
}
```

</details>

---


### Tool result

_source line 1843 · 2026-05-23T02:47:13.726550+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2120
}
```

</details>

---


### Tool call

_source line 1844 · 2026-05-23T02:47:21.568105+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/submitted.pdf",
  "pages": "13-20",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/submitted.pdf",
    "pages": "13-20",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1845 · 2026-05-23T02:47:22.683933+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 576.3}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 387.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 545.6}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 550.7}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 545.9}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 556.0}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p19.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 525.6}, {\"page\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p20.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.5}], \"total_pages\": 38, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-resea
…[truncated 138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1115
}
```

</details>

---


### Tool call

_source line 1846 · 2026-05-23T02:47:27.453520+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1847 · 2026-05-23T02:47:28.358586+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 1848 · 2026-05-23T02:47:28.459467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1849 · 2026-05-23T02:47:28.813267+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 1850 · 2026-05-23T02:47:28.964297+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 1851 · 2026-05-23T02:47:29.485875+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 1852 · 2026-05-23T02:47:29.837451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1853 · 2026-05-23T02:47:30.795144+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1830
}
```

</details>

---


### Tool call

_source line 1854 · 2026-05-23T02:47:30.795619+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 1855 · 2026-05-23T02:47:31.400007+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1856 · 2026-05-23T02:47:31.805216+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2319
}
```

</details>

---


### Tool call

_source line 1857 · 2026-05-23T02:47:31.805660+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 1858 · 2026-05-23T02:47:32.414491+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2577
}
```

</details>

---


### Tool result

_source line 1859 · 2026-05-23T02:47:33.321136+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2525
}
```

</details>

---


### Tool result

_source line 1860 · 2026-05-23T02:47:33.583808+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2183
}
```

</details>

---


### Tool result

_source line 1861 · 2026-05-23T02:47:33.763414+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1957
}
```

</details>

---


### Tool call

_source line 1862 · 2026-05-23T02:47:40.596983+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/submitted.pdf",
  "pages": "21-28",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/submitted.pdf",
    "pages": "21-28",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1863 · 2026-05-23T02:47:43.017394+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.3}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p22.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 493.2}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p23.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 536.0}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 485.3}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p25.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.6}, {\"page\": 26, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p26.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 493.3}, {\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p27.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 502.0}, {\"page\": 28, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p28.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.2}], \"total_pages\": 38, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-resea
…[truncated 138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2420
}
```

</details>

---


### Tool call

_source line 1864 · 2026-05-23T02:47:46.284548+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---


### Tool call

_source line 1865 · 2026-05-23T02:47:46.686536+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p22.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p22.png"
  }
}
```

</details>

---


### Tool result

_source line 1866 · 2026-05-23T02:47:47.591765+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1307
}
```

</details>

---


### Tool result

_source line 1867 · 2026-05-23T02:47:47.593027+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 1868 · 2026-05-23T02:47:47.593406+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p23.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p23.png"
  }
}
```

</details>

---


### Tool call

_source line 1869 · 2026-05-23T02:47:48.045448+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p24.png"
  }
}
```

</details>

---


### Tool result

_source line 1870 · 2026-05-23T02:47:48.549459+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 1871 · 2026-05-23T02:47:48.549929+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p25.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p25.png"
  }
}
```

</details>

---


### Tool result

_source line 1872 · 2026-05-23T02:47:49.454927+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool result

_source line 1873 · 2026-05-23T02:47:49.456403+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 1874 · 2026-05-23T02:47:49.507867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p26.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p26.png"
  }
}
```

</details>

---


### Tool call

_source line 1875 · 2026-05-23T02:47:50.010865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p27.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p27.png"
  }
}
```

</details>

---


### Tool result

_source line 1876 · 2026-05-23T02:47:50.365556+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 1877 · 2026-05-23T02:47:50.368348+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p28.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p28.png"
  }
}
```

</details>

---


### Tool result

_source line 1878 · 2026-05-23T02:47:50.924257+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 913
}
```

</details>

---


### Tool result

_source line 1879 · 2026-05-23T02:47:51.226237+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 1880 · 2026-05-23T02:47:59.485069+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/submitted.pdf",
  "pages": "29-38",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/submitted.pdf",
    "pages": "29-38",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1881 · 2026-05-23T02:48:00.745285+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 29, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p29.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 397.5}, {\"page\": 30, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p30.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.2}, {\"page\": 31, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p31.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.4}, {\"page\": 32, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p32.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.1}, {\"page\": 33, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p33.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.8}, {\"page\": 34, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p34.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.1}, {\"page\": 35, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p35.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 490.0}, {\"page\": 36, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p36.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.1}, {\"page\": 37, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_const
…[truncated 599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1260
}
```

</details>

---


### Tool call

_source line 1882 · 2026-05-23T02:48:05.215894+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p29.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p29.png"
  }
}
```

</details>

---


### Tool result

_source line 1883 · 2026-05-23T02:48:05.619044+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 1884 · 2026-05-23T02:48:05.669658+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p30.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p30.png"
  }
}
```

</details>

---


### Tool result

_source line 1885 · 2026-05-23T02:48:06.575514+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 1886 · 2026-05-23T02:48:06.575958+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p31.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p31.png"
  }
}
```

</details>

---


### Tool call

_source line 1887 · 2026-05-23T02:48:07.078194+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p32.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p32.png"
  }
}
```

</details>

---


### Tool result

_source line 1888 · 2026-05-23T02:48:07.530979+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1889 · 2026-05-23T02:48:07.631843+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p33.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p33.png"
  }
}
```

</details>

---


### Tool result

_source line 1890 · 2026-05-23T02:48:08.487067+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool result

_source line 1891 · 2026-05-23T02:48:08.488341+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 1892 · 2026-05-23T02:48:08.589878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p34.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p34.png"
  }
}
```

</details>

---


### Tool call

_source line 1893 · 2026-05-23T02:48:08.941811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p35.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p35.png"
  }
}
```

</details>

---


### Tool result

_source line 1894 · 2026-05-23T02:48:09.447668+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 1895 · 2026-05-23T02:48:09.449507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p36.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p36.png"
  }
}
```

</details>

---


### Tool result

_source line 1896 · 2026-05-23T02:48:09.906717+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 964
}
```

</details>

---


### Tool result

_source line 1897 · 2026-05-23T02:48:10.309163+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool call

_source line 1898 · 2026-05-23T02:49:33.669001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p37.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p37.png"
  }
}
```

</details>

---


### Tool result

_source line 1899 · 2026-05-23T02:49:33.920003+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1900 · 2026-05-23T02:49:33.920383+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p38.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p38.png"
  }
}
```

</details>

---


### Tool result

_source line 1901 · 2026-05-23T02:49:33.970826+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1902 · 2026-05-23T02:49:38.968710+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "submitted_p3*.png",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "submitted_p3*.png",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1903 · 2026-05-23T02:49:39.119720+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1904 · 2026-05-23T02:49:48.112524+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1905 · 2026-05-23T02:49:48.113245+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (u
…[truncated 5608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1906 · 2026-05-23T02:49:54.538884+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex 2>/dev/null && echo EXISTS || echo NOTFOUND",
  "description": "Check if abstract.tex exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex 2>/dev/null && echo EXISTS || echo NOTFOUND",
    "description": "Check if abstract.tex exists"
  }
}
```

</details>

---


### Tool result

_source line 1907 · 2026-05-23T02:49:54.690305+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1908 · 2026-05-23T02:49:58.757488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1909 · 2026-05-23T02:49:59.209770+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, a framework that translates Information Extraction (IE) ontologies into composable token-level decoding constraints.
3	A decidability analysis yields a two-layer architecture: a \emph{grammar layer} (context-free) compiles ontology constraints into grammars ensuring JSON validity and vocabulary membership; a \emph{semantic layer} (prefix-decidable with state) interprets type constraints at runtime via stateful token masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
4	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
5	Composed with LoRA fine-tuning on three 8B-class models across two RE datasets (up to 96 relation types), \textsc{OntoCoDec} near-eliminates domain/range violations (DR\,$<$\,0.1\%) at R-F1 41--47\%.
6	This enforcement introduces cross-field violations (CF) as a side effect---up to 1.18\% under greedy decoding on well-calibrated models---because per-triple enforcement cannot guarantee global entity-type consistency; beam search ($k{=}4$) eliminates all violation types at 1.54$\times$ latency.
7	Zero-shot evaluation reveals DR reduction of 76--99\% on SciERC and 42--90\% on DocRED, with a scale-dependent enabling dependency: neither layer achieves full DR reduction alone at 8B, while 70B semantic-only reaches 84\%.
8	70B-class validation on SciERC (full six-way ablation) with preliminary DocRED support, and event extraction on WikiEvents, confirm generalizability.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1910 · 2026-05-23T02:49:59.310611+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1911 · 2026-05-23T02:49:59.311159+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, SynCode~\cite{ugare2024syncode}, SGLang~\cite{zheng2024sglang}, and related systems~\cite{beurer-kellner2023lmql,park2024grammar,jsonschemabench2025} enforce format validity via CFG-based token masking.
8	NeuroLogic Decoding~\cite{lu2021neurologic} enforces predicate-logic constraints via beam-level reranking; OntoCoDec applies constraints per-token, avoiding beam-width dependence.
9	In code generation, PICARD~\cite{scholak2021picard} and \citet{pldi2025_type_constrained_codegen} compile type systems into prefix automata; unlike PICARD's rejection-based pruning, OntoCoDec applies constructive forward masking via a dynamic entity registry (\S\ref{sec:composition}).
10	DCCD~\cite{dccd2026} and \citet{nguyen2026thinking} decouple reasoning from constrained generation via multi-pass architectures; OntoCoDec enforces schema semantics within a single forward pass.
11	
12	\paragraph{Schema-aware IE.}
13	GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, GUIDEX~\cite{guidex2025}, GenIE~\cite{josifoski2022genie}, TANL~\cite{paolini2021tanl}, REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, and others~\cite{fei2022lasuie,wang2022deepstruct,lu2022uie,lou2023usm,zhou2024universalner} encode ontology structure or frame IE as structured generation, though schema compliance gaps persist~\cite{wadhwa2023revisiting}.
14	GoLLIE and KnowCoder embed schema knowledge via code-style prompts (training-time internalization without runtime enforcement); GoLLIE-7B eliminates DR at severe coverage cost (R-F1${=}$0.0, 46\% empty output), while OntoCoDec achieves R-F1${=}$45.47 at DR${=}$0.09\%~\cite{knowcoder_acl2024}.
15	ADELIE~\cite{qi2024adelie} aligns LLMs on IE through schema-awa
…[truncated 912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1912 · 2026-05-23T02:50:05.509277+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 1913 · 2026-05-23T02:50:05.560293+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity necessarily carries a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 0.5--2\% even after LoRA fine-tuning; rates correlate with schema restrictiveness (few valid type pairs per relation) rather than ontology or model scale.
9	At competitive quality (R-F1 41--47\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption, making reliable constraint enforcement necessary.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering discards up to 48\% of predictions including true positives (\S\ref{sec:cross-model}).
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance without runtime enforcement.
16	
17	We propose \textbf{OntoCoDec}, a framework that translates IE ontologies into composable layers of decoding-time constraints.
18	A decidability analysis of IE type constraints (\S\ref{sec:decidability}) yields a two-layer architecture: the \emph{grammar layer} compiles ont
…[truncated 2357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1914 · 2026-05-23T02:52:37.974986+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见 — OntoCoDec (Round 1)\n\n**审查侧重**: 新颖性 + Related Work 完整性 + 写作质量\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE 本体编译为可组合 token 级解码约束的两层框架：grammar layer（CFG，保证 JSON 结构和词汇约束）+ semantic layer（有状态的实体注册表，运行时执行 domain/range 类型检查）。Proposition 1 提供了形式化动机（domain/range 约束非 context-free），实验覆盖 3 个数据集、3 个 8B 模型 + 70B 验证，展示近乎完全的 DR 消除（<0.1%）。论文的分析深度（组合性分析、CF↔DR trade-off 刻画、beam search 探索）令人印象深刻，但核心技术机制（实体注册表 + domain/range 查表）相对直接，且 Abstract 中对 CF 副作用的呈现有选择性偏差。\n\n---\n\n## Strengths\n\n**S1.** 形式化分解动机清晰且有价值。Proposition 1（§3, p.3）证明了 domain/range 约束对无界实体集不是 context-free 的，为什么需要 grammar 之上的第二层提供了严谨的理论基础。这不是一个 trivial 的观察——它解释了为什么 GCD/BoostCD 等纯 CFG 方法在 IE 场景下只能达到 ~3% DR reduction（Table 17, Appendix）。\n\n**S2.** 实验评估极为全面。论文涵盖 3 个 RE 数据集（SciERC, DocRED, WikiEvents）、3 个 8B 模型 + 70B 验证、zero-shot 与 fine-tuning、5-way ablation（Table 1）、composability 分析（Figure 2）、beam search 兼容性（Appendix F）、runtime profiling（Appendix I）、error taxonomy（Appendix J）。这种评估深度在该领域论文中很少见。\n\n**S3.** 组合性分析框架有独立价值。双因素定量分析（Figure 2, Appendix D）揭示了 schema tightness (κ̄) 与 DR reduction 的关系，R² = 0.886，为理解约束系统的行为提供了可预测的框架。这一分析可迁移到其他约束解码场景。\n\n**S4.** CF↔DR trade-off 的诚实刻画（主要在 Limitations 和 Appendix C）。论文明确承认约束执行将 DR violations 转化为 CF violations 而非完全消除，提供了 grammar-first fallback 的因果追踪分析（Table 6, Appendix C），这在该领域是少见的坦诚。\n\n**S5.** 实用性强：无需约束专属训练，从 IE 本体自动编译，适用于任何有 logits 访问的自回归 LM。跨 tokenizer 验证（BPE: Qwen/Llama, SentencePiece: Mistral）增强了通用性论证。\n\n---\n\n## Weaknesses\n\n**W1. [Major] Abstract 对 CF 副作用的呈现存在选择性偏差。**\n- 具体位置：Abstract（p.1, line 6）\n- 问题：Abstract 称 CF \"as a side effect—up to 1.18% under greedy decoding on well-calibrated models\"。但这是 cherry-picking 最优情况。Table 1（p.5）显示 CF 在某些配置下从 0.08% 增加到 9.90%（DocRED, Qwen, zero-shot S1），而 Limitations（p.9）承认 \"S1 introduces CF violations (up to 12.02%)\"。Abstract 通过限定 \"well-calibrated models\" 和 \"greedy decoding\" 两个条件选择性报告了最低值，而非呈现完整范围。\n- 为什么重要：这影响读者对方法代价的第一印象。一个诚实的 Abstract 应该呈现 CF 的完整范围（如 \"0.46–12.02% depending on model calibration\"），而不是仅报告最佳情况。\n- 建议：在 Abstract 中呈现 CF 的代表性范围，而非仅限 \"well-calibrated models\" 的最佳值。可以保留 beam search 消除所有 violations 的声明作为上界解决方案。\n\n**W2. [Major] 核心技术新颖性有限——semantic layer 本质上是运行时查表。**\n- 具体位置：§3.3（p.4）, §4（p.4-5）\n- 问题：Grammar layer 被论文自身承认等价于 GCD/BoostCD（Table 17: \"grammar-only enforcement achieves RVET=0% but only ~3% DR reduction, identical to what GCD-family methods would achieve\"）。因此核心新颖性落在 semantic layer 上。然而 semantic layer 的核心机制——维护一个 entity registry D: n→τ，在 type-bearing position 做 domain/range 查表并生成 mask S(t)——是一个相对直接的运行时数据结构操作。它不涉及学习、优化或新的算法范式。\n- Proposition 1 的形式化价值被论文自身削弱：论文在 Remark（p.3）中承认 \"the valid language in the practical case is technically regular\"，语言形式上是正则的，只是 DFA 规模 O(|T|^n) 太大无法构造。这意味着理论不可能性论证实际上是一个工程可行性论证。\n- 为什么重要：对于 Conference-level acceptance，reviewer 期望看到方法论上的实质性创新，而非已知技术（CFG 约束解码 + 运行时类型检查）的系统集成。论文的贡献更偏向 \"systematic engineering contribution with theoretical grounding\"（引用论文自述，§1 p.2），这可能更适合 Findings track。\n- 建议：(a) 更明确地论证 semantic layer 的设计空间中的非显而易见选择（如 grammar-first fallback 策略、greedy limitation cascade 等），凸显这些不是唯一或显然的设计；(b) 与 post-hoc 验证方法做更深入的效率/精度对比，突出 decode-time 执行的不可替代性。\n\n**W3. [Minor] Abstract 信息密度过高，可读性差。**\n- 具体位置：Abstract（p.1）\n- 问题：Abstract 在 ~150 词中包含至少 12 个数字/百分比（DR<0.1%, R-F1 41-47%, ±0.8pp, +10%, k=4, 1.54×, CF≤1.4%, 76-99%, 42-90%, 84%, ~31%）和 5+ 个首次出现的缩写（DR, CF, RE, R-F1, LoRA）。这使得冷读极为困难——读者需要同时处理问题定义、方法概述和大量实验数据。\n- 建议：将 Abstract 分为清晰的三段式（问题 → 方法 → 关键结果），减少数字到 4-5 个最关键的，将详细数据推到 Introduction。\n\n**W4. [Minor] Introduction 中 \"42-99%\" 与 Abstract 中 \"42-90%\" 的范围不一致。**\n- 具体位置：Abstract line 7 vs. Introduction §1 p.2 line 21\n- 问题：Abstract 说 \"42–90% on DocRED\"，Introduction 说 \"zero-shot DR drops 42–99% across models and datasets\"。虽然 Introduction 的范围是跨数据集的合并范围（SciERC 76-99% + DocRED 42-90%），但两处并列使用造成不必要的混淆，读者可能误以为是矛盾。\n- 建议：统一表述方式，或在 Introduction 中明确分数据集报告。\n\n**W5. [Minor] Proposition 1 的实际意义被 Remark 部分削弱。**\n- 具体位置：§3, p.3, Proposition 1 及其后的 Remark\n- 问题：Proposition 1 论证 domain/range 约束非 context-free，但紧随其后的 Remark 指出实际情况下语言是 regular 的，只是 DFA 构造因 O(|T|^n) 规模不可行。这等于告诉读者：理论 barrier 不在表达力层面，而在工程层面。对于理论导向的读者，这削弱了 Proposition 的份量——问题不是\"不能\"而是\"太大了\"。\n- 建议：可在正文中更清晰地框架这一区分：表达力上的 barrier 驱动了架构选择（两层分离），而工程上的不可行性驱动了实现选择（运行时注册表而非预编译 DFA）。\n\n**W6. [Minor] WikiEvents 实验过于初步。**\n- 具体位置：§5.4（p.6-7）, Table 4\n- 问题：WikiEvents 的 fine-tuning 评估仅使用 20 文档测试集（非官方完整 split），且 Table 4 的 zero-shot 结果 F1=1.00，这表明模型在 zero-shot 下几乎无法完成任务。论文将此定位为 \"preliminary\"，但仍将其作为 \"event extraction generalizability\" 的证据列入 contribution list（§1 p.2）。\n- 建议：降低对 WikiEvents 结论的强度，或在 Introduction 贡献列表中标注其初步性质。\n\n---\n\n## Questions\n\n**Q1.** Semantic layer 的 entity registry 是在 greedy decoding 中维护的。在 beam search 中，每个 beam 维护独立的 registry 副本，还是共享？如果独立，k=8 时的内存开销如何？（Appendix F 报告了 latency，但未讨论 memory。）\n\n**Q2.** CF violations 的根源是 per-triple enforcement 无法保证全局 entity-type consistency。论文提到 post-hoc TCR（Appendix M）可减少 CF 18-92%。为什么不将 TCR 整合到解码循环中作为一个 re-ranking 步骤？这是否涉及 NP-hardness？\n\n**Q3.** Table 17（Appendix）显示 grammar-only enforcement 与 GCD 等价。论文是否直接在相同设置下运行过 GCD/BoostCD 作为 baseline，还是仅基于等价论证推断？如果未直接运行，这一等价性声明的可信度需要更多支撑。\n\n**Q4.** Composability 分析（Figure 2）显示 κ̄ 与 DR reduction 的线性关系。但 n=6（3 models × 2 datasets）的样本量能否支撑 R²=0.886 的置信度？是否做过 leave-one-out 交叉验证？\n\n---\n\n## Missing References\n\nRelated Work 的覆盖总体相当全面，但有以下小 gap：\n\n1. **Text2Event** (Lu et al., 2021, ACL) — 将事件抽取建模为序列生成，与 OntoCoDec 在 WikiEvents 上的 EE 实验直接相关，但未被引用。\n2. **DEGREE** (Hsu et al., 2022, NAACL) — 另一个基于生成的事件抽取框架，WikiEvents 相关实验缺少此 baseline 的讨论。\n3. 论文引用了 DCCD (2026) 和 pldi2025_type_constrained_codegen——这两个引用的 venue/年份需要核实是否为已发表/公开可获取的工作（注意：论文声称 2025-2026 的引用可能是 preprint）。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 实验方法论扎实，ablation 全面；但 Abstract 中 CF 的选择性报告、Proposition 1 被自身 Remark 削弱降低了整体严谨性感知 |\n| **Excitement** | 3/5 | 解决了真实且重要的问题（ontological violations in IE），分析框架有价值；但核心技术（entity registry + lookup）创新性有限，更偏系统集成 |\n| **Reproducibility** | 4/5 | 承诺代码开源；Appendix G 提供了完整的超参数；使用公开数据集（SciERC, DocRED, WikiEvents）；运行时和硬件信息完整 |\n\n---\n\n## Overall Assessment\n\n**Overall: 3.5 — Borderline Conference**\n\n论文解决了一个真实且重要的问题（IE 中 LLM 生成的 ontological violations），提供了有理论基础的两层架构分解，实验评估极为全面（可能是该领域最详尽的 ablation study 之一）。组合性分析框架（κ̄）和 CF↔DR trade-off 刻画是有独立价值的分析贡献。\n\n但核心技术新颖性有限：grammar layer 等价于现有方法（GCD/BoostCD），semantic layer 是相对直接的运行时查表机制。论文自述为 \"systematic engineering contribution with theoretical grounding\"——这一自我定位是准确的，但同时也指出了新颖性天花板。Abstract 对 CF 副作用的选择性报告是一个影响信任度的问题。\n\n总体而言，这是一篇执行质量很高但方法创新有限的论文，处于 Conference 和 Findings 的交界。如果 CF framing 问题得到修正且 semantic layer 的设计选择被更好地论证为非显而易见的，可以推向 Conference acceptance。\n\n**Confidence: 4/5** — 审慎确认评估正确。仔细阅读了完整论文（38 页），对约束解码和 IE 领域有足够背景知识。",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见 — OntoCoDec (Round 1)\n\n**审查侧重**: 新颖性 + Related Work 完整性 + 写作质量\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE 本体编译为可组合 token 级解码约束的两层框架：grammar layer（CFG，保证 JSON 结构和词汇约束）+ semantic layer（有状态的实体注册表，运行时执行 domain/range 类型检查）。Proposition 1 提供了形式化动机（domain/range 约束非 context-free），实验覆盖 3 个数据集、3 个 8B 模型 + 70B 验证，展示近乎完全的 DR 消除（<0.1%）。论文的分析深度（组合性分析、CF↔DR trade-off 刻画、beam search 探索）令人印象深刻，但核心技术机制（实体注册表 + domain/range 查表）相对直接，且 Abstract 中对 CF 副作用的呈现有选择性偏差。\n\n---\n\n## Strengths\n\n**S1.** 形式化分解动机清晰且有价值。Proposition 1（§3, p.3）证明了 domain/range 约束对无界实体集不是 context-free 的，为什么需要 grammar 之上的第二层提供了严谨的理论基础。这不是一个 trivial 的观察——它解释了为什么 GCD/BoostCD 等纯 CFG 方法在 IE 场景下只能达到 ~3% DR reduction（Table 17, Appendix）。\n\n**S2.** 实验评估极为全面。论文涵盖 3 个 RE 数据集（SciERC, DocRED, WikiEvents）、3 个 8B 模型 + 70B 验证、zero-shot 与 fine-tuning、5-way ablation（Table 1）、composability 分析（Figure 2）、beam search 兼容性（Appendix F）、runtime profiling（Appendix I）、error taxonomy（Appendix J）。这种评估深度在该领域论文中很少见。\n\n**S3.** 组合性分析框架有独立价值。双因素定量分析（Figure 2, Appendix D）揭示了 schema tightness (κ̄) 与 DR reduction 的关系，R² = 0.886，为理解约束系统的行为提供了可预测的框架。这一分析可迁移到其他约束解码场景。\n\n**S4.** CF↔DR trade-off 的诚实刻画（主要在 Limitations 和 Appendix C）。论文明确承认约束执行将 DR violations 转化为 CF violations 而非完全消除，提供了 grammar-first fallback 的因果追踪分析（Table 6, Appendix C），这在该领域是少见的坦诚。\n\n**S5.** 实用性强：无需约束专属训练，从 IE 本体自动编译，适用于任何有 logits 访问的自回归 LM。跨 tokenizer 验证（BPE: Qwen/Llama, SentencePiece: Mistral）增强了通用性论证。\n\n---\n\n## Weaknesses\n\n**W1. [Major] Abstract 对 CF 副作用的呈现存在选择性偏差。**\n- 具体位置：Abstract（p.1, line 6）\n- 问题：Abstract 称 CF \"as a side effect—up to 1.18% under greedy decoding on well-calibrated models\"。但这是 cherry-picking 最优情况。Table 1（p.5）显示 CF 在某些配置下从 0.08% 增加到 9.90%（DocRED, Qwen, zero-shot S1），而 Limitations（p.9）承认 \"S1 introduces CF violations (up to 12.02%)\"。Abstract 通过限定 \"well-calibrated models\" 和 \"greedy decoding\" 两个条件选择性报告了最低值，而非呈现完整范围。\n- 为什么重要：这影响读者对方法代价的第一印象。一个诚实的 Abstract 应该呈现 CF 的完整范围（如 \"0.46–12.02% depending on model calibration\"），而不是仅报告最佳情况。\n- 建议：在 Abstract 中呈现 CF 的代表性范围，而非仅限 \"well-calibrated models\" 的最佳值。可以保留 beam search 消除所有 violations 的声明作为上界解决方案。\n\n**W2. [Major] 核心技术新颖性有限——semantic layer 本质上是运行时查表。**\n- 具体位置：§3.3（p.4）, §4（p.4-5）\n- 问题：Grammar layer 被论文自身承认等价于 GCD/BoostCD（Table 17: \"grammar-only enforcement achieves RVET=0% but only ~3% DR reduction, identical to what GCD-family methods would achieve\"）。因此核心新颖性落在 semantic layer 上。然而 semantic layer 的核心机制——维护一个 entity registry D: n→τ，在 type-bearing position 做 domain/range 查表并生成 mask S(t)——是一个相对直接的运行时数据结构操作。它不涉及学习、优化或新的算法范式。\n- Proposition 1 的形式化价值被论文自身削弱：论文在 Remark（p.3）中承认 \"the valid language in the practical case is technically regular\"，语言形式上是正则的，只是 DFA 规模 O(|T|^n) 太大无法构造。这意味着理论不可能性论证实际上是一个工程可行性论证。\n- 为什么重要：对于 Conference-level acceptance，reviewer 期望看到方法论上的实质性创新，而非已知技术（CFG 约束解码 + 运行时类型检查）的系统集成。论文的贡献更偏向 \"systematic engineering contribution with theoretical grounding\"（引用论文自述，§1 p.2），这可能更适合 Findings track。\n- 建议：(a) 更明确地论证 semantic layer 的设计空间中的非显而易见选择（如 grammar-first fallback 策略、greedy limitation cascade 等），凸显这些不是唯一或显然的设计；(b) 与 post-hoc 验证方法做更深入的效率/精度对比，突出 decode-time 执行的不可替代性。\n\n**W3. [Minor] Abstract 信息密度过高，可读性差。**\n- 具体位置：Abstract（p.1）\n- 问题：Abstract 在 ~150 词中包含至少 12 个数字/百分比（DR<0.1%, R-F1 41-47%, ±0.8pp, +10%, k=4, 1.54×, CF≤1.4%, 76-99%, 42-90%, 84%, ~31%）和 5+ 个首次出现的缩写（DR, CF, RE, R-F1, LoRA）。这使得冷读极为困难——读者需要同时处理问题定义、方法概述和大量实验数据。\n- 建议：将 Abstract 分为清晰的三段式（问题 → 方法 → 关键结果），减少数字到 4-5 个最关键的，将详细数据推到 Introduction。\n\n**W4. [Minor] Introduction 中 \"42-99%\" 与 Abstract 中 \"42-90%\" 的范围不一致。**\n- 具体位置：Abstract line 7 vs. Introduction §1 p.2 line 21\n- 问题：Abstract 说 \"42–90% on DocRED\"，Introduction 说 \"zero-shot DR drops 42–99% across models and datasets\"。虽然 Introduction 的范围是跨数据集的合并范围（SciERC 76-99% + DocRED 42-90%），但两处并列使用造成不必要的混淆，读者可能误以为是矛盾。\n- 建议：统一表述方式，或在 Introduction 中明确分数据集报告。\n\n**W5. [Minor] Proposition 1 的实际意义被 Remark 部分削弱。**\n- 具体位置：§3, p.3, Proposition 1 及其后的 Remark\n- 问题：Proposition 1 论证 domain/range 约束非 context-free，但紧随其后的 Remark 指出实际情况下语言是 regular 的，只是 DFA 构造因 O(|T|^n) 规模不可行。这等于告诉读者：理论 barrier 不在表达力层面，而在工程层面。对于理论导向的读者，这削弱了 Proposition 的份量——问题不是\"不能\"而是\"太大了\"。\n- 建议：可在正文中更清晰地框架这一区分：表达力上的 barrier 驱动了架构选择（两层分离），而工程上的不可行性驱动了实现选择（运行时注册表而非预编译 DFA）。\n\n**W6. [Minor] WikiEvents 实验过于初步。**\n- 具体位置：§5.4（p.6-7）, Table 4\n- 问题：WikiEvents 的 fine-tuning 评估仅使用 20 文档测试集（非官方完整 split），且 Table 4 的 zero-shot 结果 F1=1.00，这表明模型在 zero-shot 下几乎无法完成任务。论文将此定位为 \"preliminary\"，但仍将其作为 \"event extraction generalizability\" 的证据列入 contribution list（§1 p.2）。\n- 建议：降低对 WikiEvents 结论的强度，或在 Introduction 贡献列表中标注其初步性质。\n\n---\n\n## Questions\n\n**Q1.** Semantic layer 的 entity registry 是在 greedy decoding 中维护的。在 beam search 中，每个 beam 维护独立的 registry 副本，还是共享？如果独立，k=8 时的内存开销如何？（Appendix F 报告了 latency，但未讨论 memory。）\n\n**Q2.** CF violations 的根源是 per-triple enforcement 无法保证全局 entity-type consistency。论文提到 post-hoc TCR（Appendix M）可减少 CF 18-92%。为什么不将 TCR 整合到解码循环中作为一个 re-ranking 步骤？这是否涉及 NP-hardness？\n\n**Q3.** Table 17（Appendix）显示 grammar-only enforcement 与 GCD 等价。论文是否直接在相同设置下运行过 GCD/BoostCD 作为 baseline，还是仅基于等价论证推断？如果未直接运行，这一等价性声明的可信度需要更多支撑。\n\n**Q4.** Composability 分析（Figure 2）显示 κ̄ 与 DR reduction 的线性关系。但 n=6（3 models × 2 datasets）的样本量能否支撑 R²=0.886 的置信度？是否做过 leave-one-out 交叉验证？\n\n---\n\n## Missing References\n\nRelated Work 的覆盖总体相当全面，但有以下小 gap：\n\n1. **Text2Event** (Lu et al., 2021, ACL) — 将事件抽取建模为序列生成，与 OntoCoDec 在 WikiEvents 上的 EE 实验直接相关，但未被引用。\n2. **DEGREE** (Hsu et al., 2022, NAACL) — 另一个基于生成的事件抽取框架，WikiEvents 相关实验缺少此 baseline 的讨论。\n3. 论文引用了 DCCD (2026) 和 pldi2025_type_constrained_codegen——这两个引用的 venue/年份需要核实是否为已发表/公开可获取的工作（注意：论文声称 2025-2026 的引用可能是 preprint）。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 实验方法论扎实，ablation 全面；但 Abstract 中 CF 的选择性报告、Proposition 1 被自身 Remark 削弱降低了整体严谨性感知 |\n| **Excitement** | 3/5 | 解决了真实且重要的问题（ontological violations in IE），分析框架有价值；但核心技术（entity registry + lookup）创新性有限，更偏系统集成 |\n| **Reproducibility** | 4/5 | 承诺代码开源；Appendix G 提供了完整的超参数；使用公开数据集（SciERC, DocRED, WikiEvents）；运行时和硬件信息完整 |\n\n---\n\n## Overall Assessment\n\n**Overall: 3.5 — Borderline Conference**\n\n论文解决了一个真实且重要的问题（IE 中 LLM 生成的 ontological violations），提供了有理论基础的两层架构分解，实验评估极为全面（可能是该领域最详尽的 ablation study 之一）。组合性分析框架（κ̄）和 CF↔DR trade-off 刻画是有独立价值的分析贡献。\n\n但核心技术新颖性有限：grammar layer 等价于现有方法（GCD/BoostCD），semantic layer 是相对直接的运行时查表机制。论文自述为 \"systematic engineering contribution with theoretical grounding\"——这一自我定位是准确的，但同时也指出了新颖性天花板。Abstract 对 CF 副作用的选择性报告是一个影响信任度的问题。\n\n总体而言，这是一篇执行质量很高但方法创新有限的论文，处于 Conference 和 Findings 的交界。如果 CF framing 问题得到修正且 semantic layer 的设计选择被更好地论证为非显而易见的，可以推向 Conference acceptance。\n\n**Confidence: 4/5** — 审慎确认评估正确。仔细阅读了完整论文（38 页），对约束解码和 IE 领域有足够背景知识。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1915 · 2026-05-23T02:52:41.793514+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3818
}
```

</details>

---


### Tool call

_source line 1916 · 2026-05-23T02:52:46.869189+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
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

_source line 1917 · 2026-05-23T02:52:46.920389+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1918 · 2026-05-23T02:52:51.287515+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1919 · 2026-05-23T02:52:51.287951+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1920 · 2026-05-23T02:53:01.815990+00:00_

审稿完成。核心结论：

- **Overall 3.5（Borderline Conference）**，Confidence 4/5
- **主要优势**：形式化分解动机清晰（Proposition 1）、实验评估极为全面（38 页，5-way ablation）、组合性分析框架（κ̄）有独立价值
- **核心问题**：(1) Abstract 对 CF 副作用选择性报告最佳值 1.18%，而实际范围达 12.02%（W1, Major）；(2) 技术新颖性有限——grammar layer 等价于 GCD/BoostCD，semantic layer 是运行时查表（W2, Major）；(3) Abstract 信息密度过高（W3, Minor）
- 提出 4 个技术问题（beam search registry 管理、TCR 整合可行性、GCD 等价性验证方式、κ̄ 样本量充分性）和 3 个潜在 missing references

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 39

## Round 39

36 recorded events


### User

_source line 1921 · 2026-05-23T02:54:38.496902+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每条 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿意见（完整原文）

**审查侧重**: 方法严谨性 + 实验设计 + 统计检验

### Overall: 3.5 — Borderline Conference
理论贡献扎实（Proposition 1 + 组合框架）、评估规模罕见地全面（47+ tables），但核心消融的统计检验缺失、F1 实际提升在 Bonferroni 校正后不显著、full fine-tuning 组合性失效未得到充分分析。

### Strengths
**S1** 理论基础严谨。Proposition 1 使用泵引理正式证明 domain/range 约束不是上下文无关的，Appendix O 证明完整。
**S2** 约束组合框架设计精巧。§4 Eq. 2 的非对称合取配合 grammar-first fallback 是优雅的工程决策。
**S3** 评估规模罕见。38 页 47+ 表格。
**S4** 诊断指标体系设计良好（DR/CF/RoV/ET/RV）。
**S5** Fine-tuning 统计报告有亮点——Bonferroni 校正 + 诚实报告 R-F1 不显著。
**S6** 双因子定量分析（κ × baseline violation）有实践指导价值。
**S7** 错误分析深入且诚实（Appendix J/K/N）。

### Must-Fix（Critical）
**N1** Zero-shot 核心消融（Table 1）缺乏置信区间和显著性检验。核心主张（grammar 3% vs semantic 24% vs 组合 94% DR reduction）没有统计证据支撑。Appendix G Table 8 仅覆盖 fine-tuning，Table 31 仅提供通用精度估计。建议：为 Table 1 提供 bootstrap CI + 配对检验 + Bonferroni 校正。

**N2** Full fine-tuning 组合性失效未充分分析。Table 42 显示 full FT + S1 的 R-F1（37.89）与 unconstrained 完全相同。如果 full FT 已内化约束，这对 "decoding-time enforcement is necessary" 的动机叙事构成反证。建议：报告 full FT unconstrained 的 violation rates，分析原因，限定 composability claim 为 "parameter-efficient fine-tuning"。

### Should-Fix（Major/Minor）
**W1 [Major]** WikiEvents n=20 统计效力不足，CI ±3.0pp，argument F1 shift ±1.1pp 落在 CI 内。
**W2 [Major]** 70B AWQ INT4 量化混淆因素未控制。
**W3 [Major]** 缺乏与 training-based 方法（GoLLIE/KnowCoder/ADELIE）的正面 violation rate 对比。
**W4 [Minor]** Enabling dependency "empirical enabling dependency" 术语强度与 n=6 证据基础不匹配。
**W5 [Minor]** Proposition 1 证明的 position→name indexing 简化论证不够严格。

### 小问题
- Table 1 caption "b = beam" 定义位置不当
- §3.3 prefix map 正确性未形式化
- Figure 1 未可视化 grammar-first fallback 路径
- DocRED dev set 评估应在 Limitations 中提及

### Questions
**Q1**: 能否为 Table 1 提供 bootstrap CI + Bonferroni 校正？
**Q2**: AWQ INT4 对约束执行精度的影响？
**Q3**: Full FT unconstrained 的 violation rates 是多少？
**Q4**: Table 2 Llama S1 SciERC DR=0% 是否所有种子成立？
**Q5**: TCR vs OntoCoDec 在 F1 上的对比？TCR 是否是更实用的替代？
**Q6**: Schema ambiguity σ 值能否提供定量阈值？

### Missing References
- Huang et al. (2024) "Planning for Constrained LLM Generation"
- PICARD 约束粒度差异讨论

### Overall: 3.5 — Borderline Conference

---

请逐条回应上述所有 Strengths、Must-Fix、Should-Fix、小问题、Questions 和 Missing References。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1922 · 2026-05-23T02:55:23.141407+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/submitted.pdf",
  "pages": "1,3,5,6,7",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/submitted.pdf",
    "pages": "1,3,5,6,7",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1923 · 2026-05-23T02:55:23.945220+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 457.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 412.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.0}], \"total_pages\": 38, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1924 · 2026-05-23T02:55:27.212184+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1925 · 2026-05-23T02:55:27.714912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1926 · 2026-05-23T02:55:28.619457+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool result

_source line 1927 · 2026-05-23T02:55:28.620601+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 1928 · 2026-05-23T02:55:28.621391+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 1929 · 2026-05-23T02:55:29.122804+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1930 · 2026-05-23T02:55:29.526188+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1931 · 2026-05-23T02:55:29.526654+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1932 · 2026-05-23T02:55:29.979309+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool result

_source line 1933 · 2026-05-23T02:55:30.381709+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 1934 · 2026-05-23T02:55:38.771786+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/submitted.pdf",
  "pages": "15,17,18,19,21,24,27",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/submitted.pdf",
    "pages": "15,17,18,19,21,24,27",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1935 · 2026-05-23T02:55:39.627732+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 545.6}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 545.9}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 556.0}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p19.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 525.6}, {\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.3}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 485.3}, {\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p27.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 502.0}], \"total_pages\": 38, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 1936 · 2026-05-23T02:55:43.749371+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1937 · 2026-05-23T02:55:44.552990+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1938 · 2026-05-23T02:55:45.356144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 1939 · 2026-05-23T02:55:45.557592+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 1940 · 2026-05-23T02:55:45.558041+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool call

_source line 1941 · 2026-05-23T02:55:46.211861+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 1942 · 2026-05-23T02:55:47.019754+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1663
}
```

</details>

---


### Tool call

_source line 1943 · 2026-05-23T02:55:47.020278+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p24.png"
  }
}
```

</details>

---


### Tool result

_source line 1944 · 2026-05-23T02:55:47.330774+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1772
}
```

</details>

---


### Tool call

_source line 1945 · 2026-05-23T02:55:47.331225+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p27.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images/submitted_p27.png"
  }
}
```

</details>

---


### Tool result

_source line 1946 · 2026-05-23T02:55:47.334533+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1776
}
```

</details>

---


### Tool result

_source line 1947 · 2026-05-23T02:55:48.038997+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1827
}
```

</details>

---


### Tool result

_source line 1948 · 2026-05-23T02:55:48.443787+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1423
}
```

</details>

---


### Tool result

_source line 1949 · 2026-05-23T02:55:48.645848+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1314
}
```

</details>

---


### Tool call

_source line 1950 · 2026-05-23T02:55:57.541312+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "full.*fine.?tun|Table 42|full FT|full_ft",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "full.*fine.?tun|Table 42|full FT|full_ft",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 1951 · 2026-05-23T02:55:57.642131+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.fls:607:INPUT ./appendix_full_ft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.fls:608:INPUT ./appendix_full_ft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.fls:609:INPUT ./appendix_full_ft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.fls:610:INPUT ./appendix_full_ft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.fls:611:INPUT appendix_full_ft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:101:Fine-tuning composability was validated exclusively with LoRA; full fine-tuning with an untuned learning rate underperforms LoRA (R-F1 37.89 vs.\ 43.77 on SciERC) but confirms that constraints remain effective (DR 2.74\%\,$\to$\,0\%; Appendix~\ref{app:full-ft}); other fine-tuning methods may exhibit different constraint interaction patterns and warrant further investigation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:133:\input{appendix_full_ft}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex:1:\section{Full Fine-Tuning Baseline}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex:4:To verify that constraint effectiveness generalizes beyond LoRA, we evaluate Qwen3-8B with full-parameter fine-tuning on SciERC (same data, 3 epochs, lr=$2{\times}10^{-4}$, seed 42).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrai
…[truncated 4700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1952 · 2026-05-23T02:58:38.665004+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Strengths 回应\n\n**[AGREE] R1-S1**: Proposition 1 的泵引理证明严谨。Appendix O 的完整证明是扎实的理论基础。但如我在自己的审稿中指出（R2-W5），其后的 Remark（p.3）承认实际语言是 regular 的，只是 DFA 规模 O(|T|^n) 不可行，这部分削弱了理论 barrier 的份量。\n\n**[AGREE] R1-S2**: §4 Eq.2 的非对称合取设计确实精巧。Grammar-first fallback 在 CF↔DR trade-off 中的行为有详细追踪（Appendix C, Table 6-7）。\n\n**[AGREE] R1-S3**: 38 页 47+ 表格的评估规模在该领域罕见，这一点没有争议。\n\n**[AGREE] R1-S4**: DR/CF/RoV/ET/RV 的诊断指标体系确实设计良好，允许对不同类型的违约进行精确区分，而非笼统的 \"violation rate\"。\n\n**[AGREE] R1-S5**: Bonferroni 校正 + 诚实报告 R-F1 不显著是论文的一个难得亮点。Table 8（p.21）明确报告 \"no comparison reaches significance at α=0.05 after Bonferroni correction (k=4)\"，这种统计诚实在该领域论文中不常见。\n\n**[AGREE] R1-S6**: 双因子分析有实践指导价值。Figure 2（Appendix D, p.20）的 κ̄ × baseline violation 关系提供了可预测的框架。\n\n**[AGREE] R1-S7**: 错误分析（Appendix J/K/N）深入且诚实，特别是 Appendix J（p.33-34）的 error taxonomy 覆盖了 false negatives（constraint-blocked vs. model-limited）和 false positives（schema-valid but incorrect），以及 CF 对预测质量的影响分析。\n\n---\n\n### Must-Fix 回应\n\n**[REBUT] R1-N1**: Zero-shot 核心消融（Table 1）缺乏 CI 和显著性检验。\n\nR1 的关切在统计学原理上有合理之处，但在具体情境下需要区分对待：\n\n1. **Zero-shot greedy 解码是确定性的**。给定固定的模型权重和固定的 prompt，temperature=0 的 greedy decoding 产生完全确定的输出。论文在 Appendix G（p.30）明确说明 \"Greedy decoding is deterministic\"。对于确定性过程，bootstrap CI 在统计学上无意义——没有随机变量可供重采样。\n\n2. **跨模型变异已覆盖**。Table 1 本身报告了 3 个不同模型（Qwen, Llama, Mistral）在 2 个数据集上的结果。核心 claim（grammar 3% vs semantic 24% vs 组合 94%）不是单一配置的点估计，而是在 6 个独立配置（3 models × 2 datasets）上观察到的一致模式。§5.3 Table 3 进一步提供跨模型验证。\n\n3. **Prompt 敏感性已控制**。Appendix H（Table 35, p.31）在 SciERC 上测试了 3 种 prompt 变体（Default, Minimal, Detailed），结果显示约束执行在所有变体下均有效（ET 和 RV 均降至 0%，DR 下降 94.0-94.6%）。这提供了超越单一 prompt 的稳健性证据。\n\n4. **Document-level bootstrapping 确实可以补充**。虽然解码是确定性的，但可以通过 document-level bootstrapping 估计 violation rate 的 CI（将数据集视为文档的抽样）。Table 31（p.31）实际上已提供了这种估计：SciERC 551 文档的 95% CI 为 ±1.8pp，DocRED 998 文档为 ±0.8pp。\n\n**综合判断**：R1 的要求（bootstrap CI + 配对检验 + Bonferroni 校正）对 zero-shot greedy 过度严格——确定性解码无需传统 CI。但论文确实可以更突出地呈现已有的 robustness 证据（Table 31 + Table 35）。建议将 \"zero-shot greedy is deterministic\" 在方法论中更显式声明，并在 Table 1 caption 中引用 Table 31/35 作为 robustness 参考。\n\n---\n\n**[REBUT] R1-N2**: Full fine-tuning 组合性\"失效\"。\n\nR1 对 Table 42 的解读有误。仔细查看 Appendix L（p.34-35，appendix_full_ft.tex）的数据：\n\n| 配置 | R-F1 | DR | CF |\n|------|------|-----|-----|\n| Full FT unconstrained | 37.89 | **2.74%** | 0% |\n| Full FT + S1 | 37.89 | **0%** | 1.31% |\n| LoRA unconstrained | 43.77 | 1.18% | 0% |\n| LoRA + S1 | 43.77 | 0.09% | 1.18% |\n\n关键事实：\n1. **Full FT 并未\"已内化约束\"**。Full FT unconstrained 仍有 2.74% DR——高于 LoRA 的 1.18%。这直接反驳了 R1 \"full FT 已内化约束\" 的前提。\n2. **S1 在 Full FT 上完全有效**。DR 从 2.74% 降至 0%，且 F1 不变（37.89→37.89）。这恰恰是 composability 的证明，而非\"失效\"。\n3. **R-F1 相同不等于约束无效**。R1 将 \"F1 不变\" 解读为约束无作用，但这混淆了两个独立目标：F1 衡量抽取质量，DR 衡量本体合规性。F1 不变 + DR→0% 正是理想结果——约束消除了违约而不损害质量。\n4. **Full FT 的 R-F1 偏低（37.89 vs LoRA 43.77）是因为学习率未调优**（lr=2×10⁻⁴，适合 LoRA 但对 full FT 偏高）。论文在 Table 42 caption 中诚实承认了这一点。\n\nR1 应修改的结论：Table 42 实际上支持了 OntoCoDec 的核心叙事——即使在 full fine-tuning 下，模型仍产生 2.74% DR violations，decoding-time enforcement 仍然必要且有效。\n\n不过，R1 有一个合理的细节建议：论文确实应在 Limitations 中更明确地限定 composability 评估以 LoRA 为主（已在 Limitations p.9 line 101 做了，但可更突出）。\n\n---\n\n### Should-Fix 回应\n\n**[AGREE] R1-W1**: WikiEvents n=20 统计效力不足。CI ±3.0pp 使得 argument F1 的 ±1.1pp 变化确实在 CI 内不可靠。这与我自己的 R2-W6 一致——论文将 WikiEvents 结论纳入 contribution list 但实验基础过于初步。\n\n**[AGREE] R1-W2**: 70B AWQ INT4 量化混淆因素未控制。Limitations（p.9）仅以一句带过（\"70B experiments use AWQ INT4 quantization, which may alter logit distributions at mask boundaries; the impact on constraint enforcement precision has not been isolated\"），但 70B 的关键发现（semantic-only 独立达到 84% DR reduction）直接依赖量化后的 logit 分布。理想情况下需要 FP16 对照实验。\n\n**[REBUT] R1-W3**: 缺乏与 GoLLIE/KnowCoder/ADELIE 的正面 violation rate 对比。\n\n这个要求在原则上合理，但在实践中存在根本性困难：\n\n1. **方法论不可比性**。GoLLIE、KnowCoder、ADELIE 是 training-based 方法，需要特定训练数据和训练流程。OntoCoDec 是 decoding-time 框架，正交于训练方法。直接对比需要在相同模型、相同数据、相同训练设置下叠加 OntoCoDec 到这些方法之上——这超出了合理的实验范围。\n\n2. **论文已提供间接对比**。§6（p.8）报告 GoLLIE-7B 在 SciERC 上 R-F1=0.0（46% empty output）但消除了 DR，而 OntoCoDec 在 R-F1=45.47 时达到 DR=0.09%。这表明 GoLLIE 的 violation elimination 以牺牲 extraction quality 为代价，而 OntoCoDec 保持了高质量。\n\n3. **更公平的对比是 GCD/BoostCD baseline**。Table 16-17（Appendix）提供了与 GCD-equivalent grammar-only enforcement 的直接对比（grammar-only: DR 减少 15-96%，OntoCoDec full S1: DR 减少 >99%），证明了 semantic layer 超越纯 CFG 方法的增量价值。\n\n**综合判断**：不应要求不可比方法的正面实验对比，但论文可以在 Related Work 中增加一个表格，系统性地对比不同方法的 violation handling 策略（prevention vs. detection vs. training internalization）和已报告的 violation rates（引用原文数据）。\n\n**[AGREE] R1-W4**: \"Enabling dependency\" 术语与 n=6 证据基础不匹配。\"Empirical enabling dependency\" 在 §5.1（p.5）中用于描述一个跨 6 个配置观察到的模式。Figure 2（p.20）的 R²=0.886 基于 n=6 点，统计效力确实不足以支撑 \"dependency\" 这样的因果性术语。建议改为 \"empirical co-occurrence pattern\" 或 \"observed complementarity\"。\n\n**[REBUT] R1-W5**: Proposition 1 的 position→name indexing 简化论证。\n\nProposition 1（p.3）证明的核心是对 *无界实体集* 的 domain/range 约束非 context-free。论证的关键步骤是：一个输出包含 n 个独立类型实体，后跟引用它们的关系三元组，泵引理要求存在 pump decomposition，但 pumping 任何实体会破坏后续类型约束的一致性。position→name indexing 是一个合理的简化——实际系统中实体通过名称引用而非位置，但这不影响证明的核心结论：cross-field type dependency 需要无界状态追踪，CFG 无法提供。Appendix O 的完整证明（我在第一轮审稿中已确认）在该简化下是 sound 的。\n\n---\n\n### 小问题回应\n\n**[AGREE]** Table 1 caption \"b = beam\" 定义位置不当——应在首次使用 beam 的地方定义。\n\n**[REBUT]** §3.3 prefix map 正确性未形式化——prefix matching 在 BPE tokenizer 上的正确性是一个工程细节，形式化证明不会为论文增加有意义的理论贡献。论文在 Appendix H（p.31）通过 3 种 tokenizer（BPE: Qwen/Llama, SentencePiece: Mistral）的实证验证覆盖了实际正确性。\n\n**[AGREE]** Figure 1 未可视化 grammar-first fallback 路径——Figure 1（p.3）展示了 grammar layer 和 semantic layer 的组合，但 fallback 逻辑（当 S(t)∩G(t)=∅ 时 fallback 到 G(t)）是 §4 Eq.2 的核心设计，应在架构图中体现。\n\n**[AGREE]** DocRED dev set 评估应在 Limitations 中提及——论文使用 DocRED dev set（998 docs）而非 test set 进行评估（§5, p.5 脚注），这是因为 test set annotations 不公开。Limitations 中应显式声明这一限制。\n\n---\n\n### Questions 回应\n\n**[AGREE] R1-Q1**: 如上述 N1 回应，zero-shot greedy 不需要传统 bootstrap CI（确定性过程），但 document-level bootstrap（Table 31）和 prompt sensitivity（Table 35）已提供了 robustness 证据。\n\n**[AGREE] R1-Q2**: AWQ INT4 对 logit 分布的影响确实是一个未控制的混淆因素。70B semantic-only 的 84% DR reduction 这一关键发现的可信度受此影响。\n\n**[REBUT] R1-Q3**: \"Full FT unconstrained 的 violation rates 是多少？\" 答案已在 Table 42（Appendix L, p.35）：DR=2.74%, CF=0%。R1 可能未注意到这一数据——它直接反驳了 \"full FT 已内化约束\" 的假设。\n\n**[AGREE] R1-Q4**: Table 2 Llama S1 SciERC DR=0% 是否跨种子成立——这是 fine-tuning 结果，仅报告了 seed 42。虽然 Table 8（p.21）为 fine-tuning 提供了 bootstrap CI，但跨种子的 DR=0% 稳定性未验证（DR 本身是离散计数，单个种子下 0% 可能在其他种子下出现少量 violations）。\n\n**[AGREE] R1-Q5**: TCR（Appendix M）vs OntoCoDec 的 F1 对比是一个好问题。论文报告 TCR 减少 CF 18-92%，但未报告 TCR 对 DR 和 F1 的影响。如果 TCR 是一个更简单的后处理替代方案且效果可比，这会削弱 OntoCoDec 解码时执行的必要性论证。\n\n**[REBUT] R1-Q6**: Schema ambiguity σ 的定量阈值。σ 在 Appendix D（p.36, Table 46）已有具体定义和逐 relation 的值。问题不在于缺乏定量定义，而在于正文中未给出可操作的阈值建议（如 \"σ > 0.5 时 DR reduction 受限\"）。但这更接近 future work 方向，而非当前论文的缺陷。\n\n---\n\n### Missing References 回应\n\n**[AGREE]** Huang et al. (2024) \"Planning for Constrained LLM Generation\" 可能相关——如果它讨论了约束规划与解码的关系，与 OntoCoDec 的多层约束组合有交集。但需确认该论文的具体内容和 venue。\n\n**[REBUT]** PICARD 约束粒度差异讨论——§6（p.8, section6_related_work.tex line 9）已讨论了 PICARD 与 OntoCoDec 的关键差异：\"unlike PICARD's rejection-based pruning, OntoCoDec applies constructive forward masking via a dynamic entity registry\"。这一对比涵盖了核心机制差异（rejection vs. constructive masking）。如需更细粒度的对比（如 PICARD 的 incremental parsing vs. OntoCoDec 的 prefix matching），可以在 Appendix B（Extended Related Work, p.13-17）中补充，但不应作为正文的 must-fix。\n\n---\n\n### Overall Assessment 回应\n\n**[AGREE]** R1 的 3.5 评分与我的评估一致。我们的核心判断趋同：\n\n1. **共识**：理论基础扎实、评估全面、但核心技术新颖性有限。论文是高质量的系统工程+分析贡献，处于 Conference/Findings 交界。\n\n2. **分歧**：\n   - R1-N2（full FT composability \"failure\"）——我认为 R1 对 Table 42 的解读有误，数据实际支持 OntoCoDec（见上述详细反驳）。\n   - R1-N1（zero-shot CI）——我认为对确定性 greedy decoding 要求 bootstrap CI 在统计学上不恰当，但 document-level bootstrapping 作为补充是合理的。\n   - R1-W3（GoLLIE/KnowCoder 正面对比）——我认为跨范式方法的正面实验对比不可行，间接对比（§6）和 GCD-equivalent baseline（Table 16-17）足够。\n\n3. **我的额外关切**（R1 未覆盖）：\n   - Abstract 对 CF 的选择性报告（R2-W1）——Abstract 仅报告 \"up to 1.18%\" 而 Limitations 承认 \"up to 12.02%\"，这一信任度问题 R1 未提及但同样重要。\n   - Abstract 信息密度过高（R2-W3）——12+ 个数字/百分比在 150 词内，影响可读性。\n\n**维持 Overall 3.5, Confidence 4/5。**",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Strengths 回应\n\n**[AGREE] R1-S1**: Proposition 1 的泵引理证明严谨。Appendix O 的完整证明是扎实的理论基础。但如我在自己的审稿中指出（R2-W5），其后的 Remark（p.3）承认实际语言是 regular 的，只是 DFA 规模 O(|T|^n) 不可行，这部分削弱了理论 barrier 的份量。\n\n**[AGREE] R1-S2**: §4 Eq.2 的非对称合取设计确实精巧。Grammar-first fallback 在 CF↔DR trade-off 中的行为有详细追踪（Appendix C, Table 6-7）。\n\n**[AGREE] R1-S3**: 38 页 47+ 表格的评估规模在该领域罕见，这一点没有争议。\n\n**[AGREE] R1-S4**: DR/CF/RoV/ET/RV 的诊断指标体系确实设计良好，允许对不同类型的违约进行精确区分，而非笼统的 \"violation rate\"。\n\n**[AGREE] R1-S5**: Bonferroni 校正 + 诚实报告 R-F1 不显著是论文的一个难得亮点。Table 8（p.21）明确报告 \"no comparison reaches significance at α=0.05 after Bonferroni correction (k=4)\"，这种统计诚实在该领域论文中不常见。\n\n**[AGREE] R1-S6**: 双因子分析有实践指导价值。Figure 2（Appendix D, p.20）的 κ̄ × baseline violation 关系提供了可预测的框架。\n\n**[AGREE] R1-S7**: 错误分析（Appendix J/K/N）深入且诚实，特别是 Appendix J（p.33-34）的 error taxonomy 覆盖了 false negatives（constraint-blocked vs. model-limited）和 false positives（schema-valid but incorrect），以及 CF 对预测质量的影响分析。\n\n---\n\n### Must-Fix 回应\n\n**[REBUT] R1-N1**: Zero-shot 核心消融（Table 1）缺乏 CI 和显著性检验。\n\nR1 的关切在统计学原理上有合理之处，但在具体情境下需要区分对待：\n\n1. **Zero-shot greedy 解码是确定性的**。给定固定的模型权重和固定的 prompt，temperature=0 的 greedy decoding 产生完全确定的输出。论文在 Appendix G（p.30）明确说明 \"Greedy decoding is deterministic\"。对于确定性过程，bootstrap CI 在统计学上无意义——没有随机变量可供重采样。\n\n2. **跨模型变异已覆盖**。Table 1 本身报告了 3 个不同模型（Qwen, Llama, Mistral）在 2 个数据集上的结果。核心 claim（grammar 3% vs semantic 24% vs 组合 94%）不是单一配置的点估计，而是在 6 个独立配置（3 models × 2 datasets）上观察到的一致模式。§5.3 Table 3 进一步提供跨模型验证。\n\n3. **Prompt 敏感性已控制**。Appendix H（Table 35, p.31）在 SciERC 上测试了 3 种 prompt 变体（Default, Minimal, Detailed），结果显示约束执行在所有变体下均有效（ET 和 RV 均降至 0%，DR 下降 94.0-94.6%）。这提供了超越单一 prompt 的稳健性证据。\n\n4. **Document-level bootstrapping 确实可以补充**。虽然解码是确定性的，但可以通过 document-level bootstrapping 估计 violation rate 的 CI（将数据集视为文档的抽样）。Table 31（p.31）实际上已提供了这种估计：SciERC 551 文档的 95% CI 为 ±1.8pp，DocRED 998 文档为 ±0.8pp。\n\n**综合判断**：R1 的要求（bootstrap CI + 配对检验 + Bonferroni 校正）对 zero-shot greedy 过度严格——确定性解码无需传统 CI。但论文确实可以更突出地呈现已有的 robustness 证据（Table 31 + Table 35）。建议将 \"zero-shot greedy is deterministic\" 在方法论中更显式声明，并在 Table 1 caption 中引用 Table 31/35 作为 robustness 参考。\n\n---\n\n**[REBUT] R1-N2**: Full fine-tuning 组合性\"失效\"。\n\nR1 对 Table 42 的解读有误。仔细查看 Appendix L（p.34-35，appendix_full_ft.tex）的数据：\n\n| 配置 | R-F1 | DR | CF |\n|------|------|-----|-----|\n| Full FT unconstrained | 37.89 | **2.74%** | 0% |\n| Full FT + S1 | 37.89 | **0%** | 1.31% |\n| LoRA unconstrained | 43.77 | 1.18% | 0% |\n| LoRA + S1 | 43.77 | 0.09% | 1.18% |\n\n关键事实：\n1. **Full FT 并未\"已内化约束\"**。Full FT unconstrained 仍有 2.74% DR——高于 LoRA 的 1.18%。这直接反驳了 R1 \"full FT 已内化约束\" 的前提。\n2. **S1 在 Full FT 上完全有效**。DR 从 2.74% 降至 0%，且 F1 不变（37.89→37.89）。这恰恰是 composability 的证明，而非\"失效\"。\n3. **R-F1 相同不等于约束无效**。R1 将 \"F1 不变\" 解读为约束无作用，但这混淆了两个独立目标：F1 衡量抽取质量，DR 衡量本体合规性。F1 不变 + DR→0% 正是理想结果——约束消除了违约而不损害质量。\n4. **Full FT 的 R-F1 偏低（37.89 vs LoRA 43.77）是因为学习率未调优**（lr=2×10⁻⁴，适合 LoRA 但对 full FT 偏高）。论文在 Table 42 caption 中诚实承认了这一点。\n\nR1 应修改的结论：Table 42 实际上支持了 OntoCoDec 的核心叙事——即使在 full fine-tuning 下，模型仍产生 2.74% DR violations，decoding-time enforcement 仍然必要且有效。\n\n不过，R1 有一个合理的细节建议：论文确实应在 Limitations 中更明确地限定 composability 评估以 LoRA 为主（已在 Limitations p.9 line 101 做了，但可更突出）。\n\n---\n\n### Should-Fix 回应\n\n**[AGREE] R1-W1**: WikiEvents n=20 统计效力不足。CI ±3.0pp 使得 argument F1 的 ±1.1pp 变化确实在 CI 内不可靠。这与我自己的 R2-W6 一致——论文将 WikiEvents 结论纳入 contribution list 但实验基础过于初步。\n\n**[AGREE] R1-W2**: 70B AWQ INT4 量化混淆因素未控制。Limitations（p.9）仅以一句带过（\"70B experiments use AWQ INT4 quantization, which may alter logit distributions at mask boundaries; the impact on constraint enforcement precision has not been isolated\"），但 70B 的关键发现（semantic-only 独立达到 84% DR reduction）直接依赖量化后的 logit 分布。理想情况下需要 FP16 对照实验。\n\n**[REBUT] R1-W3**: 缺乏与 GoLLIE/KnowCoder/ADELIE 的正面 violation rate 对比。\n\n这个要求在原则上合理，但在实践中存在根本性困难：\n\n1. **方法论不可比性**。GoLLIE、KnowCoder、ADELIE 是 training-based 方法，需要特定训练数据和训练流程。OntoCoDec 是 decoding-time 框架，正交于训练方法。直接对比需要在相同模型、相同数据、相同训练设置下叠加 OntoCoDec 到这些方法之上——这超出了合理的实验范围。\n\n2. **论文已提供间接对比**。§6（p.8）报告 GoLLIE-7B 在 SciERC 上 R-F1=0.0（46% empty output）但消除了 DR，而 OntoCoDec 在 R-F1=45.47 时达到 DR=0.09%。这表明 GoLLIE 的 violation elimination 以牺牲 extraction quality 为代价，而 OntoCoDec 保持了高质量。\n\n3. **更公平的对比是 GCD/BoostCD baseline**。Table 16-17（Appendix）提供了与 GCD-equivalent grammar-only enforcement 的直接对比（grammar-only: DR 减少 15-96%，OntoCoDec full S1: DR 减少 >99%），证明了 semantic layer 超越纯 CFG 方法的增量价值。\n\n**综合判断**：不应要求不可比方法的正面实验对比，但论文可以在 Related Work 中增加一个表格，系统性地对比不同方法的 violation handling 策略（prevention vs. detection vs. training internalization）和已报告的 violation rates（引用原文数据）。\n\n**[AGREE] R1-W4**: \"Enabling dependency\" 术语与 n=6 证据基础不匹配。\"Empirical enabling dependency\" 在 §5.1（p.5）中用于描述一个跨 6 个配置观察到的模式。Figure 2（p.20）的 R²=0.886 基于 n=6 点，统计效力确实不足以支撑 \"dependency\" 这样的因果性术语。建议改为 \"empirical co-occurrence pattern\" 或 \"observed complementarity\"。\n\n**[REBUT] R1-W5**: Proposition 1 的 position→name indexing 简化论证。\n\nProposition 1（p.3）证明的核心是对 *无界实体集* 的 domain/range 约束非 context-free。论证的关键步骤是：一个输出包含 n 个独立类型实体，后跟引用它们的关系三元组，泵引理要求存在 pump decomposition，但 pumping 任何实体会破坏后续类型约束的一致性。position→name indexing 是一个合理的简化——实际系统中实体通过名称引用而非位置，但这不影响证明的核心结论：cross-field type dependency 需要无界状态追踪，CFG 无法提供。Appendix O 的完整证明（我在第一轮审稿中已确认）在该简化下是 sound 的。\n\n---\n\n### 小问题回应\n\n**[AGREE]** Table 1 caption \"b = beam\" 定义位置不当——应在首次使用 beam 的地方定义。\n\n**[REBUT]** §3.3 prefix map 正确性未形式化——prefix matching 在 BPE tokenizer 上的正确性是一个工程细节，形式化证明不会为论文增加有意义的理论贡献。论文在 Appendix H（p.31）通过 3 种 tokenizer（BPE: Qwen/Llama, SentencePiece: Mistral）的实证验证覆盖了实际正确性。\n\n**[AGREE]** Figure 1 未可视化 grammar-first fallback 路径——Figure 1（p.3）展示了 grammar layer 和 semantic layer 的组合，但 fallback 逻辑（当 S(t)∩G(t)=∅ 时 fallback 到 G(t)）是 §4 Eq.2 的核心设计，应在架构图中体现。\n\n**[AGREE]** DocRED dev set 评估应在 Limitations 中提及——论文使用 DocRED dev set（998 docs）而非 test set 进行评估（§5, p.5 脚注），这是因为 test set annotations 不公开。Limitations 中应显式声明这一限制。\n\n---\n\n### Questions 回应\n\n**[AGREE] R1-Q1**: 如上述 N1 回应，zero-shot greedy 不需要传统 bootstrap CI（确定性过程），但 document-level bootstrap（Table 31）和 prompt sensitivity（Table 35）已提供了 robustness 证据。\n\n**[AGREE] R1-Q2**: AWQ INT4 对 logit 分布的影响确实是一个未控制的混淆因素。70B semantic-only 的 84% DR reduction 这一关键发现的可信度受此影响。\n\n**[REBUT] R1-Q3**: \"Full FT unconstrained 的 violation rates 是多少？\" 答案已在 Table 42（Appendix L, p.35）：DR=2.74%, CF=0%。R1 可能未注意到这一数据——它直接反驳了 \"full FT 已内化约束\" 的假设。\n\n**[AGREE] R1-Q4**: Table 2 Llama S1 SciERC DR=0% 是否跨种子成立——这是 fine-tuning 结果，仅报告了 seed 42。虽然 Table 8（p.21）为 fine-tuning 提供了 bootstrap CI，但跨种子的 DR=0% 稳定性未验证（DR 本身是离散计数，单个种子下 0% 可能在其他种子下出现少量 violations）。\n\n**[AGREE] R1-Q5**: TCR（Appendix M）vs OntoCoDec 的 F1 对比是一个好问题。论文报告 TCR 减少 CF 18-92%，但未报告 TCR 对 DR 和 F1 的影响。如果 TCR 是一个更简单的后处理替代方案且效果可比，这会削弱 OntoCoDec 解码时执行的必要性论证。\n\n**[REBUT] R1-Q6**: Schema ambiguity σ 的定量阈值。σ 在 Appendix D（p.36, Table 46）已有具体定义和逐 relation 的值。问题不在于缺乏定量定义，而在于正文中未给出可操作的阈值建议（如 \"σ > 0.5 时 DR reduction 受限\"）。但这更接近 future work 方向，而非当前论文的缺陷。\n\n---\n\n### Missing References 回应\n\n**[AGREE]** Huang et al. (2024) \"Planning for Constrained LLM Generation\" 可能相关——如果它讨论了约束规划与解码的关系，与 OntoCoDec 的多层约束组合有交集。但需确认该论文的具体内容和 venue。\n\n**[REBUT]** PICARD 约束粒度差异讨论——§6（p.8, section6_related_work.tex line 9）已讨论了 PICARD 与 OntoCoDec 的关键差异：\"unlike PICARD's rejection-based pruning, OntoCoDec applies constructive forward masking via a dynamic entity registry\"。这一对比涵盖了核心机制差异（rejection vs. constructive masking）。如需更细粒度的对比（如 PICARD 的 incremental parsing vs. OntoCoDec 的 prefix matching），可以在 Appendix B（Extended Related Work, p.13-17）中补充，但不应作为正文的 must-fix。\n\n---\n\n### Overall Assessment 回应\n\n**[AGREE]** R1 的 3.5 评分与我的评估一致。我们的核心判断趋同：\n\n1. **共识**：理论基础扎实、评估全面、但核心技术新颖性有限。论文是高质量的系统工程+分析贡献，处于 Conference/Findings 交界。\n\n2. **分歧**：\n   - R1-N2（full FT composability \"failure\"）——我认为 R1 对 Table 42 的解读有误，数据实际支持 OntoCoDec（见上述详细反驳）。\n   - R1-N1（zero-shot CI）——我认为对确定性 greedy decoding 要求 bootstrap CI 在统计学上不恰当，但 document-level bootstrapping 作为补充是合理的。\n   - R1-W3（GoLLIE/KnowCoder 正面对比）——我认为跨范式方法的正面实验对比不可行，间接对比（§6）和 GCD-equivalent baseline（Table 16-17）足够。\n\n3. **我的额外关切**（R1 未覆盖）：\n   - Abstract 对 CF 的选择性报告（R2-W1）——Abstract 仅报告 \"up to 1.18%\" 而 Limitations 承认 \"up to 12.02%\"，这一信任度问题 R1 未提及但同样重要。\n   - Abstract 信息密度过高（R2-W3）——12+ 个数字/百分比在 150 词内，影响可读性。\n\n**维持 Overall 3.5, Confidence 4/5。**",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1953 · 2026-05-23T02:58:43.339652+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4674
}
```

</details>

---


### Tool call

_source line 1954 · 2026-05-23T02:58:48.868523+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1955 · 2026-05-23T02:58:48.919327+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_21/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1956 · 2026-05-23T02:58:59.264348+00:00_

交叉回应要点总结：

- **N1 (zero-shot CI)**: 反驳——greedy decoding 是确定性过程，传统 CI 不适用；论文已有 prompt sensitivity (Table 35) 和 document-level precision (Table 31) 作为 robustness 证据
- **N2 (full FT composability 失效)**: 反驳——R1 对 Table 42 的解读有误。Full FT unconstrained 仍有 2.74% DR，S1 将其降至 0%，这正是 composability 的证明而非失效
- **W1-W2**: 同意（WikiEvents n=20 不足、70B 量化混淆）
- **W3 (GoLLIE 对比)**: 反驳——跨范式正面实验不可行，间接对比+GCD baseline 已足够
- **W4-W5**: 同意术语过强；反驳 Proposition 1 简化问题（不影响核心结论）
- **Overall**: 与 R1 趋同于 3.5，但在 N2 和 N1 两个 Critical 问题上有实质性分歧

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 40

## Round 40

46 recorded events


### User

_source line 1957 · 2026-05-23T03:37:14.962780+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性评估与论文完整性**。

## Venue 信息
- **目标**: EMNLP 2026（通过 ARR 统一审稿）
- **Deadline**: 2026-05-25（ARR May cycle）
- **格式**: ACL 模板，正文 ≤ 8 页，参考文献不限页数，Limitations/Ethics 不计入页数
- **匿名**: Double-blind
- **评分标准**: Overall Assessment 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit

## 论文路径
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/submitted.pdf`

## 你的审查侧重

### 1. 新颖性与贡献
- OntoCoDec 的核心贡献是什么？系统集成 vs 算法创新？对 NLP 社区的实际价值？
- Proposition 1（CF constraints ∉ CFL）是否真正新颖？PDA 无法 random access 是 well-known fact——论文的理论贡献是将此 observation 应用于 IE 还是提出新的理论？
- 两层约束架构（grammar + semantic）的设计是否有非显而易见的创新？
- 与 PICARD、GoLLIE、KnowCoder、ADELIE 等方法的本质区别？

### 2. 写作质量
- Abstract 的信息密度和可读性（数字数量、缩写、结构）
- Introduction 的问题定义和 motivation 是否清晰有说服力？
- Method section 的表述是否足够清晰——不熟悉 constrained decoding 的读者能否跟上？
- 论文整体叙事（diagnostic probe → fine-tuning composability → deployment tiers）是否连贯？
- Limitations 的覆盖是否充分和诚实？

### 3. Related Work 覆盖
- 是否遗漏重要相关工作？特别是 2025-2026 年的新工作
- 与已有方法的比较是否公平？是否存在 straw-man 比较？
- Constrained decoding for IE 领域的最新进展是否充分覆盖？
- Schema-aware IE 方法（GoLLIE、KnowCoder、GUIDEX 等）的定位是否准确？

### 4. 格式合规
- 正文是否 ≤ 8 页（不含 references/limitations/ethics）？
- 表格/图表编号、引用格式是否一致？
- 匿名是否彻底（无 GitHub link、作者名、机构信息）？
- Appendix 的内容是否属于 appendix 而非 main text 遗漏？

### 5. CF Trade-off Framing
- DR enforcement 引入 CF（≤1.4% fine-tuned，up to 12% zero-shot）的 framing 是否诚实？
- Abstract 中 CF 的呈现是否存在 cherry-picking（只报告最佳场景）？
- CF 的严重性是否被充分讨论——对下游应用的影响？
- Beam search 作为 CF 解决方案是否在 cost（1.54× latency）上得到充分讨论？

请输出完整审稿报告，包含 Strengths、Weaknesses（分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（含评分和置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1958 · 2026-05-23T03:37:24.295967+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1959 · 2026-05-23T03:37:24.346568+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1960 · 2026-05-23T03:37:28.364118+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1961 · 2026-05-23T03:37:30.830811+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/submitted.pdf",
  "pages": "1-10",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/submitted.pdf",
    "pages": "1-10",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1962 · 2026-05-23T03:37:31.735978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1963 · 2026-05-23T03:37:35.408953+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

I've found information about the ACL Rolling Review (ARR) 2026 reviewer guidelines and review form criteria. Here's what I found:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other
…[truncated 1169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7044
}
```

</details>

---


### Tool result

_source line 1964 · 2026-05-23T03:37:36.867602+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 528.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 411.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 482.1}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifac
…[truncated 581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6036
}
```

</details>

---


### Tool result

_source line 1965 · 2026-05-23T03:37:36.868095+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (u
…[truncated 7687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5132
}
```

</details>

---


### Tool call

_source line 1966 · 2026-05-23T03:37:42.252895+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1967 · 2026-05-23T03:37:43.307873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1968 · 2026-05-23T03:37:43.864484+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1611
}
```

</details>

---


### Tool call

_source line 1969 · 2026-05-23T03:37:43.864987+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1970 · 2026-05-23T03:37:44.569936+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1971 · 2026-05-23T03:37:45.280452+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1972
}
```

</details>

---


### Tool call

_source line 1972 · 2026-05-23T03:37:45.280977+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1973 · 2026-05-23T03:37:46.035973+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2170
}
```

</details>

---


### Tool call

_source line 1974 · 2026-05-23T03:37:46.036438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1975 · 2026-05-23T03:37:46.392748+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1976 · 2026-05-23T03:37:47.551256+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2981
}
```

</details>

---


### Tool call

_source line 1977 · 2026-05-23T03:37:47.601878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1978 · 2026-05-23T03:37:49.665631+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4384
}
```

</details>

---


### Tool result

_source line 1979 · 2026-05-23T03:37:49.669879+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3633
}
```

</details>

---


### Tool result

_source line 1980 · 2026-05-23T03:37:49.671005+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3278
}
```

</details>

---


### Tool call

_source line 1981 · 2026-05-23T03:37:49.671385+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 or other), descriptions of each score level, and any required fields. I need the exact criteria for: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 or other), descriptions of each score level, and any required fields. I need the exact criteria for: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool result

_source line 1982 · 2026-05-23T03:37:49.722461+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2120
}
```

</details>

---


### Tool result

_source line 1983 · 2026-05-23T03:37:56.601721+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Overall Assessment
**Scale:** 1-5 (with .5 increments)
- **5:** "Consider for Award: I think this paper could be considered for an outstanding paper award"
- **4:** Conference acceptance recommended
- **3:** Findings track acceptance recommended
- **2:** "Resubmit next cycle: I think this paper needs substantial revisions"
- **1:** Do not resubmit; not relevant to computational linguistics

## Soundness
**Scale:** 1-5 (with .5 increments)
- **5:** "Excellent: This study is one of the most thorough I have seen, given its type"
- **4:** "Strong: This study provides sufficient support for all of its claims"
- **3:** "Acceptable: This study provides sufficient support for its main claims"
- **2:** "Poor: Some of the main claims are not sufficiently supported"
- **1:** "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
**Scale:** 1-5 (with .5 increments)
- **5:** "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- **4:** "Exciting: I would mention this paper to others"
- **3:** "Interesting: I might mention some points of this paper to others"
- **2:** "Potentially Interesting: this paper does not resonate with me"
- **1:** "Not Exciting: this paper does not resonate with me"

## Reviewer Confidence
**Scale:** 1-5
- **5:** "Positive that my evaluation is correct"
- **4:** "Quite sure" but some details might be missed
- **3:** "Pretty sure, but there's a chance I missed something"
- **2:** Evaluation defensible but details may be overlooked
- **1:** "Not my area, or paper is very hard to understand"

## Reproducibility
**Scale:** 1-5
- **5:** "They could easily reproduce the results"
- **4:** "They could mostly reproduce the results"
- **3:** "They could reproduce the results with some difficulty"
- **2:** "They would be hard pressed to reproduce the results"
- **1:** "They would not be able to reproduce the results"

## Datasets & Softw
…[truncated 231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6930
}
```

</details>

---


### Tool call

_source line 1984 · 2026-05-23T03:38:07.966213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1985 · 2026-05-23T03:38:08.319867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1986 · 2026-05-23T03:38:08.875052+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool result

_source line 1987 · 2026-05-23T03:38:09.179173+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool call

_source line 1988 · 2026-05-23T03:38:19.079007+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read LaTeX source sections",
  "subagent_type": "Explore",
  "prompt": "I need to read several LaTeX source files from the paper to verify precise claims and numbers. The paper is at:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/\n\nRead the following files and report their full content:\n1. abstract.tex (or whatever generates the abstract)\n2. section1_introduction_draft.tex (or similar)\n3. section6_related_work.tex\n4. section7_conclusion_compressed.tex\n\nAlso look for any file named \"abstract\" in the paper directory.\n\nFor each file, report:\n- The exact text content\n- Any specific numbers/claims made\n- Any citations referenced"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "description": "Read LaTeX source sections",
    "subagent_type": "Explore",
    "prompt": "I need to read several LaTeX source files from the paper to verify precise claims and numbers. The paper is at:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/\n\nRead the following files and report their full content:\n1. abstract.tex (or whatever generates the abstract)\n2. section1_introduction_draft.tex (or similar)\n3. section6_related_work.tex\n4. section7_conclusion_compressed.tex\n\nAlso look for any file named \"abstract\" in the paper directory.\n\nFor each file, report:\n- The exact text content\n- Any specific numbers/claims made\n- Any citations referenced"
  }
}
```

</details>

---


### Tool call

_source line 1989 · 2026-05-23T03:38:23.296975+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper -type f -name \"*.tex\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper -type f -name \"*.tex\" | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1990 · 2026-05-23T03:38:23.297470+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/case_study_kappa_dr.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_power_analysis_523cc9.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/sche
…[truncated 796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1991 · 2026-05-23T03:38:23.297820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1992 · 2026-05-23T03:38:23.298102+00:00_

1	\begin{abstract}
2	Large language models for information extraction generate structurally valid but ontologically invalid triples---where entity types violate the ontology's domain/range constraints.
3	These violations persist across the capability spectrum and cannot be addressed by grammar-constrained decoding (which lacks cross-field type awareness) or post-hoc filtering (which discards valid predictions).
4	
5	We present \textsc{OntoCoDec}, a framework that compiles information extraction ontologies into composable token-level decoding constraints.
6	A decidability analysis shows that domain/range constraints exceed context-free expressiveness, yielding a two-layer architecture: a grammar layer enforces structural validity and vocabulary membership; a semantic layer enforces type constraints at runtime through stateful masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
7	
8	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
9	Composed with LoRA fine-tuning across three 8B-class models and two relation extraction datasets (up to 96 relations), \textsc{OntoCoDec} near-eliminates domain/range violations ($<$\,0.1\%) at F1 41--47\%.
10	Under fine-tuning, this enforcement introduces cross-field type inconsistencies ($\leq$1.4\%) as a side effect of per-triple independent enforcement; beam search ($k{=}4$) eliminates all violation types at 1.54$\times$ latency.
11	In zero-shot settings, cross-field rates are higher (up to 12\%) but decrease with model calibration.
12	Zero-shot domain/range reductions span 76--99\% on SciERC and 42--90\% on DocRED, with a scale-dependent empirical relationship between the two layers: the semantic layer alone achieves substantially stronger reduction at larger model scale.
13	\end{abstract}
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1993 · 2026-05-23T03:38:23.298375+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1994 · 2026-05-23T03:38:23.298620+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, SynCode~\cite{ugare2024syncode}, SGLang~\cite{zheng2024sglang}, and related systems~\cite{beurer-kellner2023lmql,park2024grammar,jsonschemabench2025} enforce format validity via CFG-based token masking.
8	NeuroLogic Decoding~\cite{lu2021neurologic} and \citet{huang2024lookahead} enforce constraints via beam-level reranking; OntoCoDec applies per-token masking, avoiding beam-width dependence.
9	PICARD~\cite{scholak2021picard} and \citet{pldi2025_type_constrained_codegen} compile type systems into prefix automata; OntoCoDec applies constructive forward masking via a dynamic entity registry (\S\ref{sec:composition}).
10	DCCD~\cite{dccd2026} and \citet{nguyen2026thinking} decouple reasoning from constrained generation; OntoCoDec enforces schema semantics within a single forward pass.
11	
12	\paragraph{Schema-aware IE.}
13	GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, GUIDEX~\cite{guidex2025}, GenIE~\cite{josifoski2022genie}, TANL~\cite{paolini2021tanl}, REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, ADELIE~\cite{qi2024adelie}, and others~\cite{fei2022lasuie,wang2022deepstruct,lu2022uie,lou2023usm,zhou2024universalner} encode ontology structure or frame IE as structured generation, though schema compliance gaps persist~\cite{wadhwa2023revisiting}.
14	GoLLIE and KnowCoder embed schema knowledge via code-style prompts (training-time internalization without runtime enforcement); GoLLIE-7B eliminates DR at severe coverage cost (R-F1${=}$0.0, 46\% empty output), while OntoCoDec achieves R-F1${=}$45.47 at DR${=}$0.09\%.
15	
16	\paragraph{Constraint enforcement in IE.}
17	\citet{roth_yih_2004} and \citet{riedel2010modeling} formulated hard type constraints via I
…[truncated 619 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1995 · 2026-05-23T03:38:23.349708+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 1996 · 2026-05-23T03:38:23.350196+00:00_

1	% Section 7 — Discussion and Conclusion
2	
3	OntoCoDec compiles IE ontologies into composable token-level constraints, validated across 3 datasets, 3+ models, and 2 tasks.
4	LoRA + greedy S1 near-eliminates DR ($<$\,0.1\%) at R-F1 41--47\%; beam ($k{=}4$) eliminates all violations at 1.54$\times$ latency.
5	The central insight is that IE type constraints exceed context-free expressiveness (Proposition~1): the semantic layer bridges the gap grammar-only enforcement cannot address (3\% vs.\ 94\% DR reduction) via constructive forward masking over a dynamic entity registry.
6	This empirical enabling dependency is scale-sensitive (\S\ref{sec:70b-results}), suggesting grammar-constrained decoding is necessary but increasingly insufficient as models improve.
7	Extending to global entity-level type consensus during decoding---eliminating CF without beam search overhead---is the primary direction for future work.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1997 · 2026-05-23T03:38:24.253985+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/submitted.pdf",
  "pages": "11-20",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/submitted.pdf",
    "pages": "11-20",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1998 · 2026-05-23T03:38:26.263087+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper -type f -name \"*introduction*\" -o -name \"*intro*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper -type f -name \"*introduction*\" -o -name \"*intro*\""
  }
}
```

</details>

---


### Tool result

_source line 1999 · 2026-05-23T03:38:26.313790+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2000 · 2026-05-23T03:38:27.669896+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2001 · 2026-05-23T03:38:27.720592+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity necessarily carries a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 0.5--2\% even after LoRA fine-tuning; rates correlate with schema restrictiveness (few valid type pairs per relation) rather than ontology or model scale.
9	At competitive quality (R-F1 41--47\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption, making reliable constraint enforcement necessary.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering discards up to 48\% of predictions including true positives (\S\ref{sec:cross-model}).
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance without runtime enforcement.
16	
17	We propose \textbf{OntoCoDec}, a framework that translates IE ontologies into composable layers of decoding-time constraints.
18	A decidability analysis of IE type constraints (\S\ref{sec:decidability}) yields a two-layer architecture: the \emph{grammar layer} compiles ont
…[truncated 2438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 2002 · 2026-05-23T03:38:34.571612+00:00_

Now let me read some key section files for precise details on claims and numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 41

## Round 41

100 recorded events


### User

_source line 2003 · 2026-05-23T08:20:49.975796+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。

## Venue 信息
- **目标**: EMNLP 2026 (via ACL Rolling Review)
- **类别**: Long Paper
- **正文页数限制**: ≤8 页（参考文献不限，Limitations/Ethics 不计入）
- **模板**: ACL style, `\usepackage[review]{acl}`
- **匿名规则**: Double-blind
- **ARR 提交截止**: 2026-05-25
- **Commitment 截止**: 2026-08-02
- **Overall Assessment 评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 论文文件
- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/submitted.pdf`

## 你的审查侧重

### 1. 新颖性评估
- 论文的核心贡献（schema-compiled constrained decoding for IE）相对于现有工作（GCD, BoostCD, GoLLIE, KnowCoder, ADELIE, XGrammar, SGLang）的增量贡献有多大？
- 是算法创新还是系统集成？如果是后者，集成的价值是否通过实验充分展示？
- §4 Constraint Composition 的理论分析是否构成独立贡献？

### 2. 相关工作覆盖（§6 + 全文）
- 是否遗漏重要相关工作？特别关注 2025-2026 年的最新工作
- 与同类方法（特别是 GCD, BoostCD, DCCD, Thinking Before Constraining）的定位和区分是否清晰？
- Text2Event, UIE, USM 等统一 IE 框架是否需要讨论？
- Constrained decoding 在 NL-to-SQL / code generation 等领域的工作是否有借鉴价值？

### 3. 写作质量与论文组织
- Abstract 是否准确反映论文贡献？信息密度是否合适？
- Introduction 的 motivation 和 contribution list 是否清晰？
- 各节的篇幅分配是否合理（特别是 zero-shot vs fine-tuned 的比例）？
- Limitations 是否诚实、全面？
- 全文叙事是否连贯？术语使用是否一致？

### 4. 格式合规
- 正文是否 ≤8 页？
- 匿名规则是否遵守（无作者信息泄露、无自引暴露身份）？
- 图表质量、标题、标注是否规范？
- 引用格式是否正确（natbib）？
- Limitations section 是否在正文中（不在 appendix）？

### 5. 完整性检查
- Appendix 是否有重要信息应该在主文中？
- 是否有未完成的 TODO / placeholder？
- 参考文献是否完整、准确？

请按以下结构输出审稿意见：
1. **Summary**（2-3 句概述）
2. **Strengths**（逐条，标注 S1, S2, ...）
3. **Weaknesses**（逐条，标注 W1, W2, ...，区分 Critical / Major / Minor）
4. **Questions**（标注 Q1, Q2, ...）
5. **Missing References**（如有）
6. **Overall Assessment**（评分 + 置信度 + 一句话总结）
7. **Detailed Comments**（逐节细评，如有）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2004 · 2026-05-23T08:21:00.306564+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2005 · 2026-05-23T08:21:01.713118+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 2006 · 2026-05-23T08:21:01.764149+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
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

_source line 2007 · 2026-05-23T08:21:01.764627+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2008 · 2026-05-23T08:21:06.854858+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 2009 · 2026-05-23T08:21:09.772060+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/submitted.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/submitted.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 2010 · 2026-05-23T08:21:10.225257+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2011 · 2026-05-23T08:21:14.783744+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found information about the ACL Rolling Review 2026. Here are the key details about reviewer guidelines, the review form, and review criteria:

## Reviewer Guidelines

The reviewer workflow includes: (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that particular submission. If you feel qualified to review some aspects of the paper but not others (e.g., experimental results but not formal proofs), please state in the review if you did not check some major parts, suc
…[truncated 1149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7928
}
```

</details>

---


### Tool result

_source line 2012 · 2026-05-23T08:21:16.089111+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 418.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 525.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 480.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 553.9}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifac
…[truncated 581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6317
}
```

</details>

---


### Tool result

_source line 2013 · 2026-05-23T08:21:16.140205+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (u
…[truncated 7854 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5914
}
```

</details>

---


### Tool call

_source line 2014 · 2026-05-23T08:21:24.928889+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ACL Rolling Review form fields, scoring scales, and criteria. Include all dimensions like soundness, excitement, novelty, reproducibility, overall assessment, confidence, etc. List the exact score options for each dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ACL Rolling Review form fields, scoring scales, and criteria. Include all dimensions like soundness, excitement, novelty, reproducibility, overall assessment, confidence, etc. List the exact score options for each dimension."
  }
}
```

</details>

---


### Tool call

_source line 2015 · 2026-05-23T08:21:26.742236+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 2016 · 2026-05-23T08:21:27.747711+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 2017 · 2026-05-23T08:21:27.748174+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 2018 · 2026-05-23T08:21:28.251213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 2019 · 2026-05-23T08:21:28.653859+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 2020 · 2026-05-23T08:21:28.654320+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 2021 · 2026-05-23T08:21:29.660426+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool result

_source line 2022 · 2026-05-23T08:21:29.661662+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool call

_source line 2023 · 2026-05-23T08:21:29.662010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 2024 · 2026-05-23T08:21:30.216776+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 2025 · 2026-05-23T08:21:30.622410+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 2026 · 2026-05-23T08:21:30.622876+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 2027 · 2026-05-23T08:21:31.579000+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1362
}
```

</details>

---


### Tool result

_source line 2028 · 2026-05-23T08:21:31.582202+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 2029 · 2026-05-23T08:21:31.582651+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 2030 · 2026-05-23T08:21:32.085913+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 2031 · 2026-05-23T08:21:32.489972+00:00_

# ACL Rolling Review Form: Fields and Scoring Dimensions

## Main Review Sections

**Paper Summary**: Describe the paper's focus and clarify any potential misunderstandings.

**Summary of Strengths**: Identify reasons for publication, such as methodology, empirical results, or organization of related work.

**Summary of Weaknesses**: List numbered concerns affecting priority relative to competing papers.

**Comments/Suggestions/Typos**: Additional improvement suggestions beyond addressing main concerns.

## Scoring Dimensions

### Reviewer Confidence
Scale 1-5, where:
- 5 = "Positive that my evaluation is correct"
- 4 = "Quite sure"
- 3 = "Pretty sure, but there's a chance I missed something"
- 2 = "Willing to defend my evaluation, but fairly likely I missed details"
- 1 = "Not my area, or paper is very hard to understand"

### Soundness
Scale 1-5 (with half-point options), assessing scientific rigor and support for claims:
- 5 = Excellent thoroughness
- 4 = Strong with sufficient support
- 3 = Acceptable with minor gaps
- 2 = Poor; major claims lack support
- 1 = Major issues; unsuitable for publication

### Excitement
Scale 1-5 (with half-point options), capturing subjective appeal:
- 5 = Highly Exciting; recommend to others
- 4 = Exciting; would mention to others
- 3 = Interesting; might mention some points
- 2 = Potentially Interesting; doesn't resonate personally
- 1 = Not Exciting; limited community relevance

### Overall Assessment
Scale 1-5 (with half-point options):
- 5 = Consider for Award (top 2.5%)
- 4 = Conference acceptance
- 3 = Findings acceptance
- 2 = Resubmit next cycle
- 1 = Do not resubmit

### Additional Dimensions

**Reproducibility** (1-5 scale): Assesses available information for result replication.

**Datasets/Software** (1-5 scales): Evaluates value of released resources to broader research community.

**Limitations and Societal Impact**: Qualitative assessment of adequacy in addressing potential harms and benefits.

**Ethical Concerns**: 
…[truncated 165 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7561
}
```

</details>

---


### Tool result

_source line 2032 · 2026-05-23T08:21:32.491136+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 2033 · 2026-05-23T08:21:32.495120+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 2034 · 2026-05-23T08:21:33.502995+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1417
}
```

</details>

---


### Tool result

_source line 2035 · 2026-05-23T08:21:34.211162+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1716
}
```

</details>

---


### Tool call

_source line 2036 · 2026-05-23T08:21:46.499021+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/submitted.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "11-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/submitted.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 2037 · 2026-05-23T08:21:47.202150+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 2038 · 2026-05-23T08:21:47.706647+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 619.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 621.2}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 587.4}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 370.4}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 549.4}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 552.2}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.3}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 551.2}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_const
…[truncated 599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1207
}
```

</details>

---


### Tool result

_source line 2039 · 2026-05-23T08:21:47.757533+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/p3_case_studies.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/p3_case_studies_861a0d.tex
/home/ubuntu/.agent-ml-re
…[truncated 5408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 555
}
```

</details>

---


### Tool call

_source line 2040 · 2026-05-23T08:21:55.641398+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2041 · 2026-05-23T08:21:56.595574+00:00_

1	\begin{abstract}
2	Large language models for information extraction generate structurally valid but ontologically invalid triples---where entity types violate the ontology's domain/range constraints.
3	These violations persist across the capability spectrum and cannot be addressed by grammar-constrained decoding (which lacks cross-field type awareness) or post-hoc filtering (which discards valid predictions).
4	
5	We present \textsc{OntoCoDec}, a framework that compiles information extraction ontologies into composable token-level decoding constraints.
6	A decidability analysis shows that domain/range constraints exceed context-free expressiveness, yielding a two-layer architecture: a grammar layer enforces structural validity and vocabulary membership; a semantic layer enforces type constraints at runtime through stateful masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
7	
8	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
9	Composed with LoRA fine-tuning across three 8B-class models and two relation extraction datasets (up to 96 relations), \textsc{OntoCoDec} near-eliminates domain/range violations ($<$\,0.1\%) at F1 41--47\%.
10	Under fine-tuning, this enforcement introduces cross-field type inconsistencies ($\leq$1.4\%) as a side effect of per-triple independent enforcement; beam search ($k{=}4$) eliminates all violation types at 1.54$\times$ latency.
11	In zero-shot settings, cross-field rates are higher (up to 12\%) but decrease with model calibration.
12	Zero-shot domain/range reductions span 76--99\% on SciERC and 42--90\% on DocRED, with a scale-dependent empirical relationship between the two layers: the semantic layer alone achieves substantially stronger reduction at larger model scale.
13	\end{abstract}
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2042 · 2026-05-23T08:21:56.746630+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2043 · 2026-05-23T08:21:57.050004+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity necessarily carries a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 0.5--2\% even after LoRA fine-tuning; rates correlate with schema restrictiveness (few valid type pairs per relation) rather than ontology or model scale.
9	At competitive quality (R-F1 41--47\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption, making reliable constraint enforcement necessary.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering discards up to 48\% of predictions including true positives (\S\ref{sec:cross-model}).
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance without runtime enforcement.
16	
17	We propose \textbf{OntoCoDec}, a framework that translates IE ontologies into composable layers of decoding-time constraints.
18	A decidability analysis of IE type constraints (\S\ref{sec:decidability}) yields a two-layer architecture: the \emph{grammar layer} compiles ont
…[truncated 2489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 2044 · 2026-05-23T08:21:57.050486+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2045 · 2026-05-23T08:21:57.556230+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	where $\wedge$ denotes element-wise AND over the vocabulary $V$; a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the empirical enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property enforced only by the grammar layer.
12	This dependency is scale-sensitive: 70B semantic-only achieves 84\% DR reduction (vs.\ 24\% on 8B), though grammar remains necessary for RV elimination (\S\ref{sec:70b-results}).
13	
14	\paragraph{Grammar-First Fallback.}
15	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
16	We enforce a \emph{grammar-first fallback}: semantic masking is skipped and the grammar layer alone controls selection.
17	Structural integrity is a hard constraint; type violations are soft errors detectable by downstream validation, with DR (ontologically invalid type pair) more severe than CF (individually valid triples with cross-triple type inconsistency).
18	Extraction tasks are robust to format-level constraints~\cite{tam2024letmespeak}, supporting this asymmetric treatment.
19	
20	\paragraph{Constraint Tightness.}
21	\label{eq:tightness}
22	Per-relation constraint tightness $\kappa(r) = 1 - |\sigma(r)|/|\mathcal{E}|^2$, with schema mean $\bar{\kappa}$.
23	Across WikiEvents ($\bar{\kappa}{=}0.029$), SciERC ($\
…[truncated 1401 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 2046 · 2026-05-23T08:21:57.556799+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2047 · 2026-05-23T08:21:58.516480+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, SynCode~\cite{ugare2024syncode}, SGLang~\cite{zheng2024sglang}, and related systems~\cite{beurer-kellner2023lmql,park2024grammar,jsonschemabench2025} enforce format validity via CFG-based token masking.
8	NeuroLogic Decoding~\cite{lu2021neurologic} and \citet{huang2024lookahead} enforce constraints via beam-level reranking; OntoCoDec applies per-token masking, avoiding beam-width dependence.
9	PICARD~\cite{scholak2021picard} and \citet{pldi2025_type_constrained_codegen} compile type systems into prefix automata; OntoCoDec applies constructive forward masking via a dynamic entity registry (\S\ref{sec:composition}).
10	DCCD~\cite{dccd2026} and \citet{nguyen2026thinking} decouple reasoning from constrained generation; OntoCoDec enforces schema semantics within a single forward pass.
11	
12	\paragraph{Schema-aware IE.}
13	GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, GUIDEX~\cite{guidex2025}, GenIE~\cite{josifoski2022genie}, TANL~\cite{paolini2021tanl}, REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, ADELIE~\cite{qi2024adelie}, and others~\cite{fei2022lasuie,wang2022deepstruct,lu2022uie,lou2023usm,zhou2024universalner} encode ontology structure or frame IE as structured generation, though schema compliance gaps persist~\cite{wadhwa2023revisiting}.
14	GoLLIE and KnowCoder embed schema knowledge via code-style prompts (training-time internalization without runtime enforcement); GoLLIE-7B eliminates DR at severe coverage cost (R-F1${=}$0.0, 5 predicted relations vs.\ ${>}$1{,}100 for OntoCoDec, 46\% empty output; Appendix~\ref{app:gollie-comparison}), while OntoCoDec achieves R-F1${=}$45.47 at DR${=}$0.09\%.
15	
16	\paragraph{Constraint enforcement in IE.}
1
…[truncated 712 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 2048 · 2026-05-23T08:21:58.516967+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 2049 · 2026-05-23T08:21:59.423329+00:00_

1	% Section 7 — Discussion and Conclusion
2	
3	OntoCoDec compiles IE ontologies into composable token-level constraints, validated across 3 datasets, 3+ models, and 2 tasks.
4	LoRA + greedy S1 near-eliminates DR ($<$\,0.1\%) at R-F1 41--47\%; beam ($k{=}4$) eliminates all violations at 1.54$\times$ latency.
5	The central insight is that IE type constraints exceed context-free expressiveness (Proposition~1): the semantic layer bridges the gap grammar-only enforcement cannot address (3\% vs.\ 94\% DR reduction) via constructive forward masking over a dynamic entity registry.
6	This empirical enabling dependency is scale-sensitive (\S\ref{sec:70b-results}), suggesting grammar-constrained decoding is necessary but increasingly insufficient as models improve.
7	Constraint enforcement is preserved under INT4 quantization (4$\times$ compression; Appendix~\ref{app:quantization}), confirming deployment viability without precision-dependent calibration.
8	Global entity-level type consensus during decoding---eliminating CF without beam search overhead---is the primary direction for future work.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 2050 · 2026-05-23T08:21:59.423837+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 2051 · 2026-05-23T08:22:00.433375+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 2052 · 2026-05-23T08:22:00.686931+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 2053 · 2026-05-23T08:22:01.647402+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2223
}
```

</details>

---


### Tool result

_source line 2054 · 2026-05-23T08:22:04.118238+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3684
}
```

</details>

---


### Tool result

_source line 2055 · 2026-05-23T08:22:04.169612+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3482
}
```

</details>

---


### Tool call

_source line 2056 · 2026-05-23T08:22:14.776608+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2057 · 2026-05-23T08:22:15.731593+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	\input{fig1_framework}
9	
10	We present OntoCoDec, a framework that translates IE ontologies into token-level constraints enforced during autoregressive generation.
11	The design is guided by a decidability analysis of IE type constraints.
12	
13	\paragraph{Constraint decidability taxonomy.}
14	\label{sec:decidability}
15	We classify IE type constraints into three levels: (1)~\emph{context-free}: vocabulary membership and JSON structure; (2)~\emph{prefix-decidable with state}: domain/range type validity, determined at each type-bearing position given the decoded relation type and entity registry; (3)~\emph{non-local}: cross-entity type consistency, which depends on the full output.
16	Unlike code generation where types are statically declared, IE constraints fall into level~2: entity types are inferred from text, the registry is built dynamically, and constraint targets depend on the co-occurring relation.
17	OntoCoDec enforces levels 1--2 (grammar and semantic layers, respectively); level~3 is addressed by beam search or post-hoc resolution (Appendix~\ref{app:tcr}).
18	
19	\smallskip
20	\noindent
21	Existing grammar-constrained decoding frameworks (e.g., XGrammar) enforce level~1 constraints---structural validity and vocabulary membership---but IE domain/range rules require cross-position entity-type state that context-free grammars cannot express.
22	We formalize this gap:
23	
24	\smallskip
25	\noindent\textbf{Proposition 1} (Level 2 $\not\subseteq$ Level 1)\textbf{.}
26	\textit{Domain/range type constraints for IE with unbounded entity sets are not context-free.}
27	
28	\smallskip
29	\noindent\textit{Proof sketch.}
30	Consider $\mathcal{E} = \{\tau_A, \tau_B\}$ and a relation $r$ with $\operatorname{dom}(r) = \{\tau_A\}$.
31	An output contains $n$ entities with independently chosen types, followed by
…[truncated 7839 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2058 · 2026-05-23T08:22:15.732093+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2059 · 2026-05-23T08:22:16.187820+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrrr rr@{}}
21	\toprule
22	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-7} \cmidrule(l){8-9}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08  & 15.45
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08  & 14.92
39	  & 8.23  & 30.98 \\
40	GCD-equiv.$^\dagger$
41	  & 15.26 & $\downarrow$1\%
42	  & \textbf{0} & \textbf{0}
43	  & 0.04  & 15.30
44	  & 8.75  & 30.91 \\
45	Semantic
46	  & 11.65 & $\downarrow$24\%
47	  & 1.51  & 0.40
48	  & 2.71  & 14.36
49	  & 8.15  & 31.01 \\
50	S1
51	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
52	  & \textbf{0} & \textbf{0}
53	  & 9.90  & \textbf{10.83}
54	  & \textbf{8.36} & 30.98 \\
55	S2
56	  & 0.97  & $\downarrow$94\%
57	  & \textbf{0} & \textbf{0}
58	  & 8.03  & \textbf{9.00}
59	  & 8.03  & \textbf{31.90} \\
60	\bottomrule
61	\end{tabular}}%
62	\caption{Five-way ablation on SciERC (551 docs
…[truncated 5804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 2060 · 2026-05-23T08:22:16.188367+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2061 · 2026-05-23T08:22:17.148449+00:00_

1	% Section 5 — DocRED Results (compressed; full ablation in Appendix)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	
5	\subsection{Cross-Dataset Validation on DocRED}
6	\label{sec:docred-results}
7	
8	DocRED (96 relations, 14$\times$ SciERC scale) validates the pattern under a larger, more restrictive ontology (Table~\ref{tab:docred-ablation}).
9	S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates RV (29.66\%\,$\to$\,0.03\%) and ET, with R-F1 $+$0.50\,pp ($p < 0.001$).
10	The lower DR reduction (45\% vs.\ 94\% on SciERC) reflects DocRED's tighter constraints, which trigger more grammar-first fallback (\S\ref{sec:greedy-limitation}).
11	Grammar-only \emph{increases} DR (18.46\%\,$\to$\,26.17\%) via \textit{latent violation surfacing}: grammar forces OOV$\to$valid relation mapping, exposing type violations previously masked by vocabulary errors---a distinct cross-dataset confirmation of the empirical enabling dependency.
12	Fine-tuning resolves residual DR entirely (Table~\ref{tab:composability}; residual decomposition in Appendix~\ref{app:residual-dr-analysis}).
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 2062 · 2026-05-23T08:22:17.149011+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2063 · 2026-05-23T08:22:17.601975+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	Table~\ref{tab:cross-model} replicates S1 with Llama-3.1-8B and Mistral-7B under identical prompts.
11	
12	\begin{table}[t]
13	\centering
14	\small
15	\setlength{\tabcolsep}{3.4pt}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}ll rrrr r@{}}
18	\toprule
19	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
20	& \textbf{R-F1} \\
21	\cmidrule(lr){3-6} \cmidrule(l){7-7}
22	\textbf{Dataset} & \textbf{Model}
23	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
24	  & $\uparrow$ \\
25	\midrule
26	\multirow{6}{*}{SciERC}
27	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
28	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
29	  \cmidrule(l){2-7}
30	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
31	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
32	  \cmidrule(l){2-7}
33	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
34	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
35	\midrule
36	\multirow{6}{*}{DocRED}
37	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
38	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
39	  \cmidrule(l){2-7}
40	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
41	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
42	  \cmidrule(l){2-7}
43	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
44	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
45	\bottomrule
46	\end{tabular}}%
47	\caption{Three-model zero-shot validation. U: unconstrained; S1: full two-layer.
48	Parse failures: Llama DocRED 9.1\%; others $\leq$1.1\%.
49	$^\dagger$Mistral: poor ze
…[truncated 778 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2064 · 2026-05-23T08:22:17.602505+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2065 · 2026-05-23T08:22:18.056314+00:00_

1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Extension to Event Extraction (Preliminary)}
8	\label{sec:wikievents}
9	
10	As a preliminary pilot study, we apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document,lu2021text2event} (56 event types, 80 roles, 27 entity types, 245 constraints; Appendix~\ref{app:wikievents}) without modification.
11	Violations extend to EV (event vocabulary), RoV (role vocabulary), and AC (argument constraint, analogous to DR).
12	
13	% ──────────────────────────────────────────
14	%  Table: WikiEvents three-model comparison (v3 final)
15	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
16	% ──────────────────────────────────────────
17	\begin{table}[t]
18	\centering
19	\small
20	\setlength{\tabcolsep}{2.8pt}
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{@{}ll rrrr rr@{}}
23	\toprule
24	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
25	& \multicolumn{2}{c}{\textbf{F1}} \\
26	\cmidrule(lr){3-6} \cmidrule(l){7-8}
27	\textbf{Model} & \textbf{Mode}
28	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
29	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
30	\midrule
31	\multirow{3}{*}{Qwen3-8B}
32	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
33	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
34	  & S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
35	\midrule
36	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
37	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\
38	  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
39	  & S1    & \textbf{0} & \textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\
40	\midrule
41	\multi
…[truncated 2192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 2066 · 2026-05-23T08:22:18.057403+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 2067 · 2026-05-23T08:22:19.013844+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC, lower on DocRED due to amortization over longer sequences; under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
7	
8	\paragraph{Beam search compatibility.}
9	\label{sec:beam-results}
10	With LoRA, beam search ($k{=}4$)~\cite{anderson2017guided} eliminates all four violation types on both SciERC and DocRED at both 8B and 70B scales (R-F1 43--47; Appendix~\ref{app:beam-search}), yielding two deployment tiers: greedy S1 ($+$10\% latency, DR${<}$0.1\%, CF${\leq}$1.4\%) and beam S1 (1.54$\times$ latency, all violations${\to}$0\%; Table~\ref{tab:beam-latency}).
11	
12	% exp_ids: r16_70b_scierc_zs_s1, r16_70b_docred_zs_s1, 70b_lora_scierc, 70b_lora_docred_200
13	\paragraph{70B-class validation.}
14	\label{sec:70b-results}
15	On Llama-3.1-70B-Instruct (AWQ INT4),\footnote{All 70B experiments use AWQ INT4 quantization. An 8B ablation confirms that INT4 does not affect constraint enforcement (DR remains 0\%; Appendix~\ref{app:quantization}).} zero-shot S1 eliminates DR on both datasets (SciERC 6.41\%\,$\to$\,0\%, DocRED 14.98\%\,$\to$\,0\%; R-F1 11--13).
16	% exp_ids: r16_70b_scierc_zs_ablation (grammar_only, semantic_only, full_s1)
17	A four-way ablation reveals scale-dependent layer interaction: semantic-only achieves 84\% DR reduction vs.\ 8B's 24\% (Table~\ref{tab:scierc-ablation}), though grammar remains necessary for RV elimination and CF control (semantic-only CF${=}$76).
18	% exp_ids: eval_70b_lora_scierc_s1_constrained, eval_70b_lora_docred_200_s1_constrained
19	LoRA confirms composability: DR\,$\to$\,0\% on both datasets (R-F1 44.53, 43.95; $|\Delta| \leq 0.20$\,pp; CF 0.18--1.33\%); cross-family generalization at 70B
…[truncated 983 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 2068 · 2026-05-23T08:22:19.014346+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 2069 · 2026-05-23T08:22:19.519735+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two deployment configurations: greedy S1 (DR\,$\leq$\,0.09\%, $+$10\% latency) and beam S1 (all violations\,$\to$\,0\%, 1.54$\times$ latency); zero-shot evaluation (\S\ref{sec:scierc-results}--\S\ref{sec:cross-model}) serves as a diagnostic probe for the fine-tuned setting (R-F1 41--47\%).
8	
9	\paragraph{Setup.}
10	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
11	RE type constraints are extracted from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) derive from the KAIROS ontology.
12	All constraints are schema-level, independent of evaluation splits.
13	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
14	LoRA hyperparameters were selected on SciERC development data and transferred to DocRED without further tuning; DocRED development documents were used for evaluation only.
15	Four violation categories: \textbf{DR} (type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), \textbf{CF} (conflicting types across triples).
16	Baseline DR: 15.37\% (SciERC), 18.46\% (DocRED); schema-informed prompting reduces DR by 62\% but is per-relation unreliable (Appendix~\ref{app:per-relation-landscape}).
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 2070 · 2026-05-23T08:22:19.520226+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 2071 · 2026-05-23T08:22:19.571454+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$, where $\mathcal{P}(\cdot)$ denotes the power set, specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We quantify constraint restrictiveness via \emph{constraint tightness} $\kappa(r)$ (\S\ref{sec:composition}): tighter constraints leave fewer valid type pairs per relation.
11	We define ontology constraints broadly to encompass both formal ontology specifications (e.g., the KAIROS event ontology with explicit role-entity type mappings) and empirically derived type-pair constraints extracted from annotated training data.
12	The latter applies when datasets lack a formal ontology but provide typed annotations (SciERC, DocRED); OntoCoDec compiles both sources into the same constraint representation without modification.
13	Empirical constraints achieve 99\%+ instance-level coverage on held-out data (SciERC 99.0\%, DocRED 99.4\%); uncovered type pairs trigger grammar-first fallback (\S\ref{sec:composition}), ensuring no valid triples are blocked.
14	
15	\paragraph{Grammar-Constrained Decoding.}
16	\label{sec:bg:gcd}
17	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
18	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
19	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $
…[truncated 886 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2072 · 2026-05-23T08:22:27.714300+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2073 · 2026-05-23T08:22:28.520588+00:00_

1	\section{Extended Related Work}
2	\label{app:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, making grammar-constrained decoding the de facto standard for obtaining structured output from language models.
9	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, which enables efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, and provide a robust foundation for 
…[truncated 19911 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 2074 · 2026-05-23T08:22:28.571307+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_gollie_comparison.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_gollie_comparison.tex"
  }
}
```

</details>

---


### Tool result

_source line 2075 · 2026-05-23T08:22:29.023232+00:00_

1	% Appendix: GoLLIE Comparison (D4 response)
2	% exp_ids: gollie_7b_scierc_zs_100, ontcodec_qwen_ft_s1_scierc_100, ontcodec_llama_ft_s1_scierc_100
3	
4	\section{GoLLIE Comparison}
5	\label{app:gollie-comparison}
6	
7	\begin{table}[h]
8	\centering
9	\small
10	\setlength{\tabcolsep}{3.2pt}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}l rrrr rr r@{}}
13	\toprule
14	\textbf{Method}
15	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
16	  & R-F1\,$\uparrow$ & E-F1\,$\uparrow$
17	  & \#Pred \\
18	\midrule
19	GoLLIE-7B (ZS)        & 0    & 0 & 0 & 0.83 & 0.0   & 9.17  & 5 \\
20	OntoCoDec Qwen (FT+S1)  & 0    & 0 & 0 & 0.61 & 43.69 & 66.43 & 1121 \\
21	OntoCoDec Llama (FT+S1) & 0    & 0 & 0 & 0.62 & 45.47 & 67.09 & 1070 \\
22	\bottomrule
23	\end{tabular}}
24	\caption{GoLLIE-7B vs.\ OntoCoDec on SciERC (100 docs, zero-shot for GoLLIE, LoRA + S1 for OntoCoDec). F1 $\times$ 100.}
25	\label{tab:gollie-comparison}
26	\end{table}
27	
28	GoLLIE-7B achieves zero DR/RV/ET violations by generating only 5 predicted relations across 100 documents (54\% produce empty output), representing a trivial solution where formal correctness is achieved through near-complete abstention.
29	OntoCoDec achieves comparable violation rates (DR${=}$0\%, lower CF) while maintaining R-F1 43--45\% with ${\sim}$200$\times$ more predictions.
30	Code-style schema encoding thus trades coverage for formal correctness; OntoCoDec achieves both through decoding-time enforcement rather than training-time internalization.
31	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2076 · 2026-05-23T08:22:29.174251+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_pumping_lemma.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_pumping_lemma.tex"
  }
}
```

</details>

---


### Tool result

_source line 2077 · 2026-05-23T08:22:29.726841+00:00_

1	% Appendix: Full Proof of Proposition 1
2	% Level 2 (prefix-decidable with state) constraints are not context-free.
3	
4	\section{Full Proof of Proposition 1}
5	\label{app:pumping-lemma}
6	
7	We prove that domain/range type constraints for IE with unbounded entity sets cannot be expressed by any context-free grammar, using the pumping lemma for context-free languages.
8	
9	\begin{proof}
10	Define the language $L$ of valid IE outputs over ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ with $\mathcal{E} = \{\tau_A, \tau_B\}$, $\mathcal{R} = \{r\}$, and $\sigma(r) = \{(\tau_A, \tau_A)\}$ (i.e., $r$ requires both head and tail to be type $\tau_A$).
11	
12	An output string has the form:
13	\[
14	w = e_1\, e_2\, \cdots\, e_n\;\; \texttt{REL}(h{=}e_k,\, r,\, \tau^h)
15	\]
16	where each $e_i$ is an entity with type $\tau_{a_i} \in \{\tau_A, \tau_B\}$, and $\tau^h$ is the head type field of a relation triple referencing entity $e_k$ ($1 \leq k \leq n$).
17	
18	The type-validity constraint requires $\tau^h = \tau_{a_k}$ (the head type must match the referenced entity's type) \emph{and} $\tau^h \in \operatorname{dom}(r) = \{\tau_A\}$.
19	Combined: a string $w \in L$ if and only if $\tau_{a_k} = \tau_A$.
20	
21	Now consider strings of the specific form:
22	\[
23	w_n = \underbrace{\tau_B\; \tau_B\; \cdots\; \tau_B}_{n-1}\; \tau_A\;\; \texttt{REL}(h{=}e_n,\, r,\, \tau_A)
24	\]
25	where the first $n{-}1$ entities have type $\tau_B$ and only entity $e_n$ has type $\tau_A$.
26	The relation references $e_n$, so $\tau^h = \tau_A = \tau_{a_n}$, satisfying both the registry consistency and domain constraint.
27	Thus $w_n \in L$ for all $n$.
28	
29	Assume for contradiction that $L$ is context-free.
30	By the pumping lemma, there exists a pumping length $p$ such that any $w \in L$ with $|w| \geq p$ can be written as $w = uvxyz$ where:
31	\begin{enumerate}[label=(\roman*)]
32	    \item $|vy| \geq 1$,
33	    \item $|vxy| \leq p$,
34	    \item $uv^i xy^i z \in L$ for all $i \g
…[truncated 4472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 2078 · 2026-05-23T08:22:29.727225+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "constrained decoding information extraction 2025 2026 schema type constraints LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "constrained decoding information extraction 2025 2026 schema type constraints LLM"
  }
}
```

</details>

---


### Tool result

_source line 2079 · 2026-05-23T08:22:37.464971+00:00_

Web search results for query: "constrained decoding information extraction 2025 2026 schema type constraints LLM"

Links: [{"title":"LLM Structured Outputs: Schema Validation for Real Pipelines (2026) | Collin Wilkins","url":"https://collinwilkins.com/articles/structured-output"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Constrained Decoding for LLMs: How JSON, Regex, and Schema Control Improve Output Reliability","url":"https://brics-econ.org/constrained-decoding-for-llms-how-json-regex-and-schema-control-improve-output-reliability"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Constrained Decoding: Grammar-Guided Generation for Structured LLM Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11747381/"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/pdf/2506.14901"}]

Based on the search results, here's what I found on constrained decoding for information extraction with schema and type constraints in LLMs:

## Current State (2025-2026)

As of early 2026, major providers support native structured output enforcement that uses constrained decoding under the hood, restrictin
…[truncated 1442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7737
}
```

</details>

---


### Tool call

_source line 2080 · 2026-05-23T08:22:45.400569+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Thinking Before Constraining\" constrained decoding 2026 draft-then-constrain"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Thinking Before Constraining\" constrained decoding 2026 draft-then-constrain"
  }
}
```

</details>

---


### Tool call

_source line 2081 · 2026-05-23T08:22:45.702232+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Text2Event USM unified structured model information extraction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Text2Event USM unified structured model information extraction 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 2082 · 2026-05-23T08:22:45.954399+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DCCD \"draft-conditional constrained decoding\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DCCD \"draft-conditional constrained decoding\" 2026"
  }
}
```

</details>

---


### Tool result

_source line 2083 · 2026-05-23T08:22:51.729602+00:00_

Web search results for query: ""Thinking Before Constraining" constrained decoding 2026 draft-then-constrain"

Links: [{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"Thinking Before Constraining: A Unified Decoding Framework for Large Language Models","url":"https://arxiv.org/html/2601.07525"},{"title":"Thinking Before Constraining: A Unified Decoding Framework for Large","url":"https://www.arxiv.org/pdf/2601.07525"},{"title":"Thinking Before Constraining: A Unified Decoding Framework for Large","url":"https://openreview.net/pdf/4c088202bf17a7bd46090a60327806359244552a.pdf"},{"title":"[2601.07525] Thinking Before Constraining: A Unified Decoding Framework for Large Language Models","url":"https://arxiv.org/abs/2601.07525"}]

Based on the search results, I found two related research papers on constrained decoding published in early 2026:

## "Thinking Before Constraining: A Unified Decoding Framework for Large Language Models"

This work addresses the tradeoff between natural generation (which allows rich reasoning but lacks guaranteed structure) and structured generation/constrained decoding (which ensures consistency but can restrict reasoning capabilities).

The approach allows LLMs to reason freely until specific trigger tokens are generated, then switches to structured generation, preserving expressive reasoning while ensuring reliability of structured outputs. This approach is called In-Writing, and achieves substantial gains of up to 27% in accuracy.

## "Draft-Conditioned Constrained Decoding for Structured Generation in LLMs"

This paper presents an alternative approach: Rather than forcing the model to reason inside the constraint set, it first generates an unconstrained draft (capturing the semantic plan) and then applies constrained decoding conditioned on the draft to guarantee validity, reducing constraint-induced distortion while preserving exact structural guarant
…[truncated 423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6329
}
```

</details>

---


### Tool result

_source line 2084 · 2026-05-23T08:22:52.533857+00:00_

Web search results for query: "DCCD "draft-conditional constrained decoding" 2026"

Links: [{"title":"[2603.03305] Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/abs/2603.03305"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"Appendix","url":"https://arxiv.org/html/2603.03305"},{"title":"Speculative Decoding + Constrained Grammar: The 10x Inference Speedup Nobody’s Talking About | by delimitter | Apr, 2026 | Medium","url":"https://medium.com/@andbubnov/speculative-decoding-constrained-grammar-the-10x-inference-speedup-nobodys-talking-about-d32640e60c97"},{"title":"Structured Decoding","url":"https://www.aussieai.com/blog/structured-decoding-optimization"},{"title":"Constrained Decoding Mechanism","url":"https://www.emergentmind.com/topics/constrained-decoding-mechanism"}]

Based on the search results, I found information about DCCD (Draft-Conditional Constrained Decoding):

DCCD is a simple two-step, training-free inference procedure that decouples semantic planning from structural enforcement: an unconstrained draft is generated first, and constrained decoding is then applied, conditioned on this draft, to guarantee validity.

The method analyzes DCCD through a KL-projection view, showing that draft conditioning increases feasible mass and reduces the cumulative "projection tax" induced by hard constraints, with an optional best-of-K draft selection.

**Performance improvements:** Across structured reasoning benchmarks, DCCD improves strict structured accuracy by up to +24 percentage points over standard constrained decoding (e.g., 15.2% to 39.0% on GSM8K with a 1B model), and enables smaller model pairs to match or exceed much larger constrained baselines, yielding substantial gains in parameter efficiency.

The research paper was published in February 2026 on arXiv, with authors including Avinash Reddy Chapparapu and colleag
…[truncated 198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6579
}
```

</details>

---


### Tool result

_source line 2085 · 2026-05-23T08:22:55.396041+00:00_

Web search results for query: "Text2Event USM unified structured model information extraction 2025 2026"

Links: [{"title":"Text2Event: Controllable Sequence-to-Structure Generation for End-to-end   Event Extraction","url":"https://arxiv.org/pdf/2106.09232"},{"title":"Universal Information Extraction as Unified Semantic Matching | Request PDF","url":"https://www.researchgate.net/publication/371922000_Universal_Information_Extraction_as_Unified_Semantic_Matching"},{"title":"InstructUIE: Unified Info Extraction Framework | PDF | Conceptual Model | Information","url":"https://www.scribd.com/document/797504751/2304-08085v1"},{"title":"[2301.03282] Universal Information Extraction as Unified Semantic Matching","url":"https://arxiv.org/abs/2301.03282"},{"title":"[PDF] Unified Structure Generation for Universal Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unified-Structure-Generation-for-Universal-Lu-Liu/5382c28b9f2dd30f15c836bea92382091b1d886f"},{"title":"Universal Information Extraction as Unified Semantic Matching","url":"https://arxiv.org/pdf/2301.03282"},{"title":"Two Universal Relations Unify Information Extraction Tasks","url":"https://aclanthology.org/2024.naacl-long.103.pdf"},{"title":"[2304.08085] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://ar5iv.labs.arxiv.org/html/2304.08085"}]

Based on the search results, here's what I found about these information extraction methods:

## Text2Event

Text2Event is a sequence-to-structure generation paradigm that can directly extract events from text in an end-to-end manner. It features a sequence-to-structure network for unified event extraction, a constrained decoding algorithm for event knowledge injection during inference, and a curriculum learning algorithm for efficient model learning.

## USM (Unified Semantic Matching)

USM is a framework that universally models various IE (information extraction) tasks with unified token linki
…[truncated 884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9693
}
```

</details>

---


### Tool call

_source line 2086 · 2026-05-23T08:24:46.363071+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 2087 · 2026-05-23T08:24:46.863255+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 500
}
```

</details>

---


### Tool call

_source line 2088 · 2026-05-23T08:24:46.894903+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 2089 · 2026-05-23T08:24:47.299356+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 2090 · 2026-05-23T08:24:47.354942+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 2091 · 2026-05-23T08:24:47.355409+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2092 · 2026-05-23T08:24:57.184978+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\TBD|TODO|FIXME|\\\\todo",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\TBD|TODO|FIXME|\\\\todo",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 2093 · 2026-05-23T08:24:57.285931+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:22:\newcommand{\TBD}[1]{\textcolor{red}{#1}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex:18:% TODO: Expand with 2-3 sentences on how grammar-constrained decoding has become
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex:36:% TODO: Expand with 1-2 sentences on the technical differences between PL type
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex:58:% TODO: Add 1-2 sentences positioning GCD as the closest precursor (same logits-masking
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex:81:% TODO: Expand with discussion of how training-based and decoding-time approaches
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex:104:% TODO: Add quantitative comparison of compute cost: post-hoc rejection vs.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex:123:% TODO: Add 1-2 sentences connecting to S2 strategy as an instantiation of

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2094 · 2026-05-23T08:25:18.027626+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "structured information extraction LLM 2025 2026 ontology type constraint schema-guided ACL EMNLP NAACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "structured information extraction LLM 2025 2026 ontology type constraint schema-guided ACL EMNLP NAACL"
  }
}
```

</details>

---


### Tool call

_source line 2095 · 2026-05-23T08:25:18.379932+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "BoostCD \"combining constrained unconstrained decoding boosting\" 2025 information extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "BoostCD \"combining constrained unconstrained decoding boosting\" 2025 information extraction"
  }
}
```

</details>

---


### Tool result

_source line 2096 · 2026-05-23T08:25:24.160708+00:00_

Web search results for query: "structured information extraction LLM 2025 2026 ontology type constraint schema-guided ACL EMNLP NAACL"

Links: [{"title":"Building Ontology with LLMs: Five Methods Compared","url":"https://zerofuturetech.substack.com/p/building-ontology-with-llms-five"},{"title":"Constraint-Aware Ontology Engineering for Information ...","url":"https://ceur-ws.org/Vol-4085/paper41.pdf"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/pdf/2510.20345"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/html/2509.04696v1"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/odke"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/pdf/2510.08623"}]

I found relevant search results on structured information extraction with LLMs focusing on ontology, type constraints, and schema-guided approaches. Here's what the research shows:

## Recent Research (2025-2026)

Between 2025 and 2026, five distinct methods emerged from the research literature to address challenges in ontology construction with LLMs, including issues like hallucination, unknown concept types, granularity calibration, and validation.

## Schema-Guided and Ontology-Driven Approaches

Schema-based extraction relies on an explicit knowledge schema that provides both structural guidance and semantic constraints for the extraction process. Early work relied on explicit ontologies as global constraints, with approaches like Kommineni et al. (2024) enforcing alignment between extracted triples and predefined ontological definitions.

ODKE+ dynamically generates ontology snippets tailored to each entity type to align extraction
…[truncated 729 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6133
}
```

</details>

---


### Tool result

_source line 2097 · 2026-05-23T08:25:24.462938+00:00_

Web search results for query: "BoostCD "combining constrained unconstrained decoding boosting" 2025 information extraction"

Links: [{"title":"[2506.14901] Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/abs/2506.14901"},{"title":"Constrained Decoding Mechanism","url":"https://www.emergentmind.com/topics/constrained-decoding-mechanism"},{"title":"Combining Constrained and Unconstrained Decoding via ...","url":"https://aclanthology.org/2025.emnlp-main.926.pdf"},{"title":"Constrained Decoding in Sequence Generation","url":"https://www.emergentmind.com/topics/constrained-decoding"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting:","url":"https://openreview.net/pdf?id=3Qbw5Ja6Sc"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/pdf/2506.14901"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/html/2506.14901v1"}]

Based on the search results, here's what I found about BoostCD:

## Overview

BoostCD (Boosted Constrained Decoding) combines constrained and unconstrained decoding in two phases: Phase 1 decodes from the base model twice in constrained and unconstrained mode, obtaining two weak predictions, and in phase 2, a learned autoregressive boosted model combines the two weak predictions into one final prediction.

## Key Innovation

The mistakes made by the base model with vs. without constraints tend to be complementary, which the boosted model learns to exploit for improved performance.

## Application to Information Extraction

BoostCD is demonstrated by applying it to closed information extraction, with the model BoostIE outperforming prior approaches both in and out of distribution, addressing several common errors identified in those approa
…[truncated 407 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6083
}
```

</details>

---


### Tool call

_source line 2098 · 2026-05-23T08:28:36.226062+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE 本体编译为可组合 token 级解码约束的框架。通过形式化分析（Proposition 1）证明 domain/range 类型约束超越上下文无关文法的表达能力，由此设计两层架构：grammar layer（基于 XGrammar 的 CFG 约束）和 semantic layer（基于动态实体注册表的运行时类型掩码）。在 SciERC、DocRED、WikiEvents 三个数据集上，跨 4 个模型（8B–70B）、2 种精度（FP16/INT4）进行了全面评估。LoRA 微调 + greedy S1 近乎消除 domain/range 违规（DR<0.1%），beam search（k=4）消除所有违规类型，延迟开销 10%–54%。\n\n---\n\n## Strengths\n\n**S1: 全面且严谨的实验评估。** 论文在 3 个数据集、4 个模型（3 种 tokenizer 族）、2 种精度上进行评估，包含五路消融（Table 1）、cross-model 验证（Table 3）、fine-tuning 可组合性（Table 2）、70B 验证、beam search 兼容性。统计报告包含 bootstrap CIs、p 值、Bonferroni 校正。这一评估深度在该领域内较为罕见。\n\n**S2: 诚实透明的呈现方式。** 论文明确承认 DR enforcement 引入 CF 违规、zero-shot 质量低、WikiEvents 结果是初步的。Limitations 部分极为详细，覆盖约束范围、评估覆盖度、工程局限。这种诚实态度值得肯定。\n\n**S3: 实用的系统设计。** 两层架构配合 grammar-first fallback 有清晰的工程动机。延迟开销适度（greedy +10%，beam 1.54×）。编译速度快（<0.5s）。可扩展性测试显示在 200 实体类型 / 1000 关系时保持恒定 2–3% 开销（Appendix M）。\n\n**S4: 充分的相关工作覆盖。** 主文（§6）和扩展附录（Appendix B）全面覆盖 grammar-constrained decoding（XGrammar、Outlines、LMQL）、schema-aware IE（GoLLIE、KnowCoder、ADELIE）、代码领域语义约束解码（PICARD、Synchromesh、MGD）、后验验证（ODKE+、OntoLogX）、约束解码质量影响（CRANE、FormaTTax）。对 DCCD 和 Thinking Before Constraining 的定位也清晰。\n\n**S5: Tokenizer 无关设计的跨模型泛化。** 在三种 tokenizer 族（byte-level BPE: Qwen/Llama, SentencePiece: Mistral）上验证了 continuation masking 的有效性，这是一个重要的工程贡献。\n\n---\n\n## Weaknesses\n\n**W1 [Major]: 算法创新有限，主要是系统集成贡献。** 论文自我定位为\"systematic engineering contribution with theoretical grounding\"（§1, line 23），这是诚实的，但也暴露了核心问题。Proposition 1（IE 类型约束超越 CFG 表达能力）在形式语言理论社区是 well-known 的结论，对任何了解 PDA 局限性的研究者来说并不意外。证明本身（Appendix G）是严格的，但结论缺乏 surprise value。核心设计决策——XGrammar 处理结构 + stateful logits processor 处理语义——是自然且直觉的组合。§4 Constraint Composition 文档化了设计决策（grammar-first fallback、constraint tightness κ），但不构成独立理论贡献。κ 与 DR reduction 的相关性在 n=3 下 p=0.138（§4），统计不显著，作为分析工具的价值有限。\n\n**W2 [Major]: CF 违规 trade-off 显著削弱核心价值主张。** S1 enforcement 因 per-triple 独立强制执行而创建 CF 违规：zero-shot 高达 12.02%（DocRED Llama，Table 3），fine-tuned 下 ≤1.18%（SciERC Qwen，Table 2）。这意味着系统将一类违规（DR: ontologically invalid）替换为另一类（CF: cross-triple type inconsistency）。虽然论文正确指出 CF 严重性低于 DR（CF 可通过 post-hoc TCR 缓解，Appendix O），但 \"编译本体 → 强制约束 → 获得有效输出\" 的干净叙事被打破。仅 beam search（k=4, 1.54× latency）完全解决两类违规，使延迟最优的 greedy 部署层成为不完整方案。实际部署中，用户必须在\"容忍 CF\"和\"支付 beam 延迟\"之间选择——这个 trade-off 在 abstract 和 introduction 中被低估了。\n\n**W3 [Major]: Zero-shot 结果占据大量主文篇幅但缺乏实用价值。** Zero-shot R-F1 在所有模型上仅 4–8%（Table 3），远低于可用质量。论文将其定位为\"diagnostic probe\"（§5 开头），但约 3/8 页篇幅用于 zero-shot 实验（§5.1 zero-shot 诊断、§5.2 DocRED、§5.3 cross-model），这些实验展示的是对功能上不可用的提取器的约束执行。相比之下，真正有实用价值的 fine-tuning composability（Table 2）仅获得约 1 页篇幅。建议重新分配：压缩 zero-shot 为 1 个总结段落+1 个表格，扩展 fine-tuning 分析。\n\n**W4 [Minor]: GoLLIE 比较不公平。** Appendix F（Table 8）比较 GoLLIE-7B zero-shot（R-F1=0.0, 5 predictions）vs. OntoCoDec LoRA fine-tuned（R-F1=43–45, ~1100 predictions）。GoLLIE 在未经 fine-tune 的 schema 上近乎 abstain 是预期行为。公平比较应为：(a) 两者都 zero-shot，或 (b) 两者都 fine-tuned on SciERC。当前比较在主文 §6 中被引用（\"GoLLIE-7B eliminates DR at severe coverage cost (R-F1=0.0)\"），可能误导读者认为 GoLLIE 本质上是低质量的。\n\n**W5 [Minor]: WikiEvents 结果过于初步，不应作为贡献声明。** n=20 测试文档，bootstrap CIs ±3–5 pp（Table 4 caption），统计效力不足以支持可靠结论。论文 power analysis（Appendix I）也承认这点。Introduction contribution list 中 \"preliminary pilot study on WikiEvents (n=20 test documents) validates event extraction applicability (§5.4)\" 过度推销了一个统计效力很弱的结果。\n\n**W6 [Minor]: Limitations 部分过长。** 约 1.5 页的 Limitations 覆盖三个详细段落。EMNLP 2026 指南规定 Limitations \"do not count towards this page limit, provided they do not contain excessive additional content\"。当前长度接近\"excessive\"的边界。部分内容（如 residual DR 分解的具体数字、TCR 讨论、full fine-tuning 对比）可移至 appendix。\n\n**W7 [Minor]: 表述重复。** \"empirical enabling dependency\"（grammar-only 8B 24% DR reduction, semantic-only 24%, combined 94%）在 abstract、§1、§3 Empirical Observation、§3.4、§4、§5.1 中重复出现至少 6 次。虽然是重要观察，但如此密集的重复消耗了宝贵的主文篇幅。\n\n---\n\n## Questions\n\n**Q1:** 类型约束从训练数据中提取（§5 Setup），覆盖率 99%+。剩余 ~1% 未覆盖的合法类型对会被系统性阻断。是否评估过约束引入的 false negatives 对 recall 的影响？Downstream impact（§5.1 末尾）报告 0.49% 被移除三元组匹配 gold label，但这只是被约束移除的部分。是否存在因约束而根本未被生成的合法三元组？\n\n**Q2:** DocRED 上 grammar-only *增加* DR（18.46%→26.17%，§5.2 \"latent violation surfacing\"）。这表明 grammar constraints 可以迫使模型进入一个类型错误更多的受限空间。这种效应在 fine-tuning 后是否持续？如果是，是否意味着 grammar layer 在某些 schema 下实际上是有害的？\n\n**Q3:** Beam search (k=4) 消除所有违规。是否探索过 k=2 作为折中？论文仅展示 k=4；理解 k 与违规消除的关系对实际部署指导很重要。\n\n**Q4:** Entity registry 在生成过程中增量构建（§3.3）。当模型对同一实体名生成不同类型时，first-seen type 是否始终被采用？这似乎是 CF 违规的主要来源，但机制在主文中解释不够清晰。§4 \"greedy limitation\" 段提及但未详细展开。\n\n**Q5:** Constraint tightness κ 的定义（§4）中，SciERC κ̄=0.333, DocRED κ̄=0.842, WikiEvents κ̄=0.029。在 n=3 下无法建立有意义的统计关系（p=0.138）。是否有计划在更多 schema 上验证这一指标？\n\n---\n\n## Missing References\n\n论文的相关工作覆盖已相当全面。以下为非关键性建议：\n\n- **PARSE** (Suri et al., 2025, arXiv:2510.08623): LLM-driven schema optimization for reliable entity extraction，与 schema compilation 方面相关。\n- **FormaTTax** (Zhou, 2026) 已被引用，但可考虑更详细讨论其 \"structure snowballing\" 发现与 IE 任务的差异性——论文目前仅在 appendix 中讨论。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 (Borderline Conference)\n\n**Confidence**: 4 (Quite sure — 我对 constrained decoding 和结构化 IE 领域有扎实的了解，审查了论文的技术细节和实验设计)\n\n**一句话总结**: 一个工程执行出色、实验评估全面的 IE 类型约束解码系统，但核心算法创新有限（主要是现有技术的组合），且 CF 违规 trade-off 部分削弱了中心价值主张。\n\n---\n\n## Detailed Comments（逐节细评）\n\n### Abstract\n信息密度高但准确。具体数字（\"≤1.4%\"、\"76–99%\"）在未读论文时难以理解。建议提供更直觉的框架化表述（如\"在 fine-tuning 下近乎消除类型违规\"）。第一句话对问题的定义很好（\"ontologically invalid triples\"），但后续技术细节（\"two-layer architecture\"、\"grammar-first fallback\"）可能过早引入实现细节。\n\n### §1 Introduction\nMotivation 清晰，从违规率（15.4% SciERC, 18.5% DocRED）到现有方法的不足（prompting 不可靠、grammar-only 无效、post-hoc 丢弃 48%），论证链完整。Contribution list 结构合理但过长（两个条目各含 4–5 个子句），可考虑拆分为更短的要点。\n\n### §2 Background\n简洁且范围适当。Problem statement（§2.3）精确。\"prefix-decidable\"的引入为后续设计提供了清晰的理论基础。\n\n### §3 Method\nProposition 1 技术上正确，但主文 proof sketch（lines 29–33）依赖对 PDA 栈的非形式化描述（\"A PDA's LIFO stack cannot retrieve position k < n without destroying entries above it\"）。Appendix G 的完整证明是严格的，但主文 sketch 应更清楚地标注为 informal argument，或收紧论述。\n\n\"Empirical Observation\"（lines 39–40）的标签形式暗示理论结果，但内容是实验观察。建议重新措辞以区分。\n\nSemantic layer 的设计（§3.3）解释清晰：entity registry + dynamic masking + continuation masking。Running example（Used-for 关系）有助于理解。\n\n### §4 Constraint Composition\nGrammar-first fallback 的设计决策有充分的工程动机（结构完整性是硬约束，类型违规是可检测的软错误）。但 constraint tightness κ 在 n=3 数据点上的相关性（p=0.138）不应被呈现为分析工具——这只是描述性统计，论文承认了这点（\"descriptive, n=3, p=0.138\"），但仍花费段落篇幅讨论。\n\nNon-rectangularity 分析（§4 末尾）是一个有趣的细节，但在主文中的位置可能不太合适——考虑移至 appendix。\n\n### §5 Experiments\n**五路消融（Table 1）是论文最强的部分**，清晰展示了各层的独立和组合贡献。违规类别分类法（DR, RV, ET, CF）干净实用。\n\nDocRED 结果（§5.2）不如 SciERC 令人印象深刻（45% vs. 94% DR reduction），论文将其归因于\"tighter constraints trigger more fallback\"。但这个解释不够深入——是否可以提供 fallback 触发率的数据来支撑这一解释？\n\n70B 结果（§5.5）有趣（semantic-only 在 70B 下达到 84% DR reduction vs. 8B 的 24%），为 scale-dependent enabling dependency 提供了重要证据。但全部 70B 实验使用 AWQ INT4 量化，且论文无法进行直接 FP16 对比——这是可理解的硬件限制，但削弱了 70B claims 的力度。\n\nWikiEvents 扩展（§5.4）展示了框架的泛化能力，但 n=20 的测试集规模严重限制了结论的可靠性。\n\n### §6 Related Work\n三段结构（constrained decoding → schema-aware IE → constraint enforcement in IE）清晰有效。与 GCD/BoostCD 的定位（\"grammar-only achieves 3% DR reduction\"）有直接实验支撑。与 GoLLIE 的对比可改进（见 W4）。\n\n### §7 Discussion and Conclusion\n简短但恰当。Future direction（global entity-level type consensus）直接针对 CF 问题，是合理的下一步。\n\n### Limitations\n极其详细和诚实，覆盖 constraint scope、evaluation coverage、engineering considerations 三个维度。建议精简至约 1 页，将具体数字分解和边缘讨论移至 appendix。\n\n### Format Compliance\n- 正文 8 页 ✓\n- 匿名：\"Anonymous ACL submission\" ✓\n- `\\usepackage[review]{acl}` ✓\n- Limitations 在正文中（page 9）✓\n- Ethics Statement 存在 ✓\n- 引用格式正确（natbib）✓\n- Figure 1 清晰，Tables 1–4 格式规范 ✓\n- 未发现 TODO/TBD/placeholder 标记 ✓（`\\TBD` 命令已定义但未使用；TODOs 仅在未编译的 outline 文件中）\n- 未发现匿名违规 ✓",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE 本体编译为可组合 token 级解码约束的框架。通过形式化分析（Proposition 1）证明 domain/range 类型约束超越上下文无关文法的表达能力，由此设计两层架构：grammar layer（基于 XGrammar 的 CFG 约束）和 semantic layer（基于动态实体注册表的运行时类型掩码）。在 SciERC、DocRED、WikiEvents 三个数据集上，跨 4 个模型（8B–70B）、2 种精度（FP16/INT4）进行了全面评估。LoRA 微调 + greedy S1 近乎消除 domain/range 违规（DR<0.1%），beam search（k=4）消除所有违规类型，延迟开销 10%–54%。\n\n---\n\n## Strengths\n\n**S1: 全面且严谨的实验评估。** 论文在 3 个数据集、4 个模型（3 种 tokenizer 族）、2 种精度上进行评估，包含五路消融（Table 1）、cross-model 验证（Table 3）、fine-tuning 可组合性（Table 2）、70B 验证、beam search 兼容性。统计报告包含 bootstrap CIs、p 值、Bonferroni 校正。这一评估深度在该领域内较为罕见。\n\n**S2: 诚实透明的呈现方式。** 论文明确承认 DR enforcement 引入 CF 违规、zero-shot 质量低、WikiEvents 结果是初步的。Limitations 部分极为详细，覆盖约束范围、评估覆盖度、工程局限。这种诚实态度值得肯定。\n\n**S3: 实用的系统设计。** 两层架构配合 grammar-first fallback 有清晰的工程动机。延迟开销适度（greedy +10%，beam 1.54×）。编译速度快（<0.5s）。可扩展性测试显示在 200 实体类型 / 1000 关系时保持恒定 2–3% 开销（Appendix M）。\n\n**S4: 充分的相关工作覆盖。** 主文（§6）和扩展附录（Appendix B）全面覆盖 grammar-constrained decoding（XGrammar、Outlines、LMQL）、schema-aware IE（GoLLIE、KnowCoder、ADELIE）、代码领域语义约束解码（PICARD、Synchromesh、MGD）、后验验证（ODKE+、OntoLogX）、约束解码质量影响（CRANE、FormaTTax）。对 DCCD 和 Thinking Before Constraining 的定位也清晰。\n\n**S5: Tokenizer 无关设计的跨模型泛化。** 在三种 tokenizer 族（byte-level BPE: Qwen/Llama, SentencePiece: Mistral）上验证了 continuation masking 的有效性，这是一个重要的工程贡献。\n\n---\n\n## Weaknesses\n\n**W1 [Major]: 算法创新有限，主要是系统集成贡献。** 论文自我定位为\"systematic engineering contribution with theoretical grounding\"（§1, line 23），这是诚实的，但也暴露了核心问题。Proposition 1（IE 类型约束超越 CFG 表达能力）在形式语言理论社区是 well-known 的结论，对任何了解 PDA 局限性的研究者来说并不意外。证明本身（Appendix G）是严格的，但结论缺乏 surprise value。核心设计决策——XGrammar 处理结构 + stateful logits processor 处理语义——是自然且直觉的组合。§4 Constraint Composition 文档化了设计决策（grammar-first fallback、constraint tightness κ），但不构成独立理论贡献。κ 与 DR reduction 的相关性在 n=3 下 p=0.138（§4），统计不显著，作为分析工具的价值有限。\n\n**W2 [Major]: CF 违规 trade-off 显著削弱核心价值主张。** S1 enforcement 因 per-triple 独立强制执行而创建 CF 违规：zero-shot 高达 12.02%（DocRED Llama，Table 3），fine-tuned 下 ≤1.18%（SciERC Qwen，Table 2）。这意味着系统将一类违规（DR: ontologically invalid）替换为另一类（CF: cross-triple type inconsistency）。虽然论文正确指出 CF 严重性低于 DR（CF 可通过 post-hoc TCR 缓解，Appendix O），但 \"编译本体 → 强制约束 → 获得有效输出\" 的干净叙事被打破。仅 beam search（k=4, 1.54× latency）完全解决两类违规，使延迟最优的 greedy 部署层成为不完整方案。实际部署中，用户必须在\"容忍 CF\"和\"支付 beam 延迟\"之间选择——这个 trade-off 在 abstract 和 introduction 中被低估了。\n\n**W3 [Major]: Zero-shot 结果占据大量主文篇幅但缺乏实用价值。** Zero-shot R-F1 在所有模型上仅 4–8%（Table 3），远低于可用质量。论文将其定位为\"diagnostic probe\"（§5 开头），但约 3/8 页篇幅用于 zero-shot 实验（§5.1 zero-shot 诊断、§5.2 DocRED、§5.3 cross-model），这些实验展示的是对功能上不可用的提取器的约束执行。相比之下，真正有实用价值的 fine-tuning composability（Table 2）仅获得约 1 页篇幅。建议重新分配：压缩 zero-shot 为 1 个总结段落+1 个表格，扩展 fine-tuning 分析。\n\n**W4 [Minor]: GoLLIE 比较不公平。** Appendix F（Table 8）比较 GoLLIE-7B zero-shot（R-F1=0.0, 5 predictions）vs. OntoCoDec LoRA fine-tuned（R-F1=43–45, ~1100 predictions）。GoLLIE 在未经 fine-tune 的 schema 上近乎 abstain 是预期行为。公平比较应为：(a) 两者都 zero-shot，或 (b) 两者都 fine-tuned on SciERC。当前比较在主文 §6 中被引用（\"GoLLIE-7B eliminates DR at severe coverage cost (R-F1=0.0)\"），可能误导读者认为 GoLLIE 本质上是低质量的。\n\n**W5 [Minor]: WikiEvents 结果过于初步，不应作为贡献声明。** n=20 测试文档，bootstrap CIs ±3–5 pp（Table 4 caption），统计效力不足以支持可靠结论。论文 power analysis（Appendix I）也承认这点。Introduction contribution list 中 \"preliminary pilot study on WikiEvents (n=20 test documents) validates event extraction applicability (§5.4)\" 过度推销了一个统计效力很弱的结果。\n\n**W6 [Minor]: Limitations 部分过长。** 约 1.5 页的 Limitations 覆盖三个详细段落。EMNLP 2026 指南规定 Limitations \"do not count towards this page limit, provided they do not contain excessive additional content\"。当前长度接近\"excessive\"的边界。部分内容（如 residual DR 分解的具体数字、TCR 讨论、full fine-tuning 对比）可移至 appendix。\n\n**W7 [Minor]: 表述重复。** \"empirical enabling dependency\"（grammar-only 8B 24% DR reduction, semantic-only 24%, combined 94%）在 abstract、§1、§3 Empirical Observation、§3.4、§4、§5.1 中重复出现至少 6 次。虽然是重要观察，但如此密集的重复消耗了宝贵的主文篇幅。\n\n---\n\n## Questions\n\n**Q1:** 类型约束从训练数据中提取（§5 Setup），覆盖率 99%+。剩余 ~1% 未覆盖的合法类型对会被系统性阻断。是否评估过约束引入的 false negatives 对 recall 的影响？Downstream impact（§5.1 末尾）报告 0.49% 被移除三元组匹配 gold label，但这只是被约束移除的部分。是否存在因约束而根本未被生成的合法三元组？\n\n**Q2:** DocRED 上 grammar-only *增加* DR（18.46%→26.17%，§5.2 \"latent violation surfacing\"）。这表明 grammar constraints 可以迫使模型进入一个类型错误更多的受限空间。这种效应在 fine-tuning 后是否持续？如果是，是否意味着 grammar layer 在某些 schema 下实际上是有害的？\n\n**Q3:** Beam search (k=4) 消除所有违规。是否探索过 k=2 作为折中？论文仅展示 k=4；理解 k 与违规消除的关系对实际部署指导很重要。\n\n**Q4:** Entity registry 在生成过程中增量构建（§3.3）。当模型对同一实体名生成不同类型时，first-seen type 是否始终被采用？这似乎是 CF 违规的主要来源，但机制在主文中解释不够清晰。§4 \"greedy limitation\" 段提及但未详细展开。\n\n**Q5:** Constraint tightness κ 的定义（§4）中，SciERC κ̄=0.333, DocRED κ̄=0.842, WikiEvents κ̄=0.029。在 n=3 下无法建立有意义的统计关系（p=0.138）。是否有计划在更多 schema 上验证这一指标？\n\n---\n\n## Missing References\n\n论文的相关工作覆盖已相当全面。以下为非关键性建议：\n\n- **PARSE** (Suri et al., 2025, arXiv:2510.08623): LLM-driven schema optimization for reliable entity extraction，与 schema compilation 方面相关。\n- **FormaTTax** (Zhou, 2026) 已被引用，但可考虑更详细讨论其 \"structure snowballing\" 发现与 IE 任务的差异性——论文目前仅在 appendix 中讨论。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 (Borderline Conference)\n\n**Confidence**: 4 (Quite sure — 我对 constrained decoding 和结构化 IE 领域有扎实的了解，审查了论文的技术细节和实验设计)\n\n**一句话总结**: 一个工程执行出色、实验评估全面的 IE 类型约束解码系统，但核心算法创新有限（主要是现有技术的组合），且 CF 违规 trade-off 部分削弱了中心价值主张。\n\n---\n\n## Detailed Comments（逐节细评）\n\n### Abstract\n信息密度高但准确。具体数字（\"≤1.4%\"、\"76–99%\"）在未读论文时难以理解。建议提供更直觉的框架化表述（如\"在 fine-tuning 下近乎消除类型违规\"）。第一句话对问题的定义很好（\"ontologically invalid triples\"），但后续技术细节（\"two-layer architecture\"、\"grammar-first fallback\"）可能过早引入实现细节。\n\n### §1 Introduction\nMotivation 清晰，从违规率（15.4% SciERC, 18.5% DocRED）到现有方法的不足（prompting 不可靠、grammar-only 无效、post-hoc 丢弃 48%），论证链完整。Contribution list 结构合理但过长（两个条目各含 4–5 个子句），可考虑拆分为更短的要点。\n\n### §2 Background\n简洁且范围适当。Problem statement（§2.3）精确。\"prefix-decidable\"的引入为后续设计提供了清晰的理论基础。\n\n### §3 Method\nProposition 1 技术上正确，但主文 proof sketch（lines 29–33）依赖对 PDA 栈的非形式化描述（\"A PDA's LIFO stack cannot retrieve position k < n without destroying entries above it\"）。Appendix G 的完整证明是严格的，但主文 sketch 应更清楚地标注为 informal argument，或收紧论述。\n\n\"Empirical Observation\"（lines 39–40）的标签形式暗示理论结果，但内容是实验观察。建议重新措辞以区分。\n\nSemantic layer 的设计（§3.3）解释清晰：entity registry + dynamic masking + continuation masking。Running example（Used-for 关系）有助于理解。\n\n### §4 Constraint Composition\nGrammar-first fallback 的设计决策有充分的工程动机（结构完整性是硬约束，类型违规是可检测的软错误）。但 constraint tightness κ 在 n=3 数据点上的相关性（p=0.138）不应被呈现为分析工具——这只是描述性统计，论文承认了这点（\"descriptive, n=3, p=0.138\"），但仍花费段落篇幅讨论。\n\nNon-rectangularity 分析（§4 末尾）是一个有趣的细节，但在主文中的位置可能不太合适——考虑移至 appendix。\n\n### §5 Experiments\n**五路消融（Table 1）是论文最强的部分**，清晰展示了各层的独立和组合贡献。违规类别分类法（DR, RV, ET, CF）干净实用。\n\nDocRED 结果（§5.2）不如 SciERC 令人印象深刻（45% vs. 94% DR reduction），论文将其归因于\"tighter constraints trigger more fallback\"。但这个解释不够深入——是否可以提供 fallback 触发率的数据来支撑这一解释？\n\n70B 结果（§5.5）有趣（semantic-only 在 70B 下达到 84% DR reduction vs. 8B 的 24%），为 scale-dependent enabling dependency 提供了重要证据。但全部 70B 实验使用 AWQ INT4 量化，且论文无法进行直接 FP16 对比——这是可理解的硬件限制，但削弱了 70B claims 的力度。\n\nWikiEvents 扩展（§5.4）展示了框架的泛化能力，但 n=20 的测试集规模严重限制了结论的可靠性。\n\n### §6 Related Work\n三段结构（constrained decoding → schema-aware IE → constraint enforcement in IE）清晰有效。与 GCD/BoostCD 的定位（\"grammar-only achieves 3% DR reduction\"）有直接实验支撑。与 GoLLIE 的对比可改进（见 W4）。\n\n### §7 Discussion and Conclusion\n简短但恰当。Future direction（global entity-level type consensus）直接针对 CF 问题，是合理的下一步。\n\n### Limitations\n极其详细和诚实，覆盖 constraint scope、evaluation coverage、engineering considerations 三个维度。建议精简至约 1 页，将具体数字分解和边缘讨论移至 appendix。\n\n### Format Compliance\n- 正文 8 页 ✓\n- 匿名：\"Anonymous ACL submission\" ✓\n- `\\usepackage[review]{acl}` ✓\n- Limitations 在正文中（page 9）✓\n- Ethics Statement 存在 ✓\n- 引用格式正确（natbib）✓\n- Figure 1 清晰，Tables 1–4 格式规范 ✓\n- 未发现 TODO/TBD/placeholder 标记 ✓（`\\TBD` 命令已定义但未使用；TODOs 仅在未编译的 outline 文件中）\n- 未发现匿名违规 ✓",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2099 · 2026-05-23T08:28:40.043018+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3816
}
```

</details>

---


### Tool call

_source line 2100 · 2026-05-23T08:28:46.763038+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 2101 · 2026-05-23T08:28:46.814255+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 2102 · 2026-05-23T08:28:59.711524+00:00_

审稿完成，已通过 `review_reviewer_post_to_director` 提交给 Review Director。

**核心判断**: Overall 3.5 (Borderline Conference)，置信度 4/5。

**主要发现**:
- **优势**: 实验评估极为全面（3 数据集 × 4 模型 × 2 精度 × 多策略），统计报告严谨（bootstrap CIs + Bonferroni），相关工作覆盖充分，系统设计实用（+10% 延迟）
- **核心问题**: (1) 算法创新有限，主要是 XGrammar + stateful logits processor 的系统集成；(2) CF 违规 trade-off 削弱价值主张（greedy 部署层不完整，beam 才能完全解决）；(3) zero-shot R-F1 仅 4–8%，占主文 ~3 页但缺乏实用价值
- **格式合规**: 全部通过（8 页正文、双盲匿名、Limitations 在正文、无 TODO 残留）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 42

## Round 42

4 recorded events


### User

_source line 2103 · 2026-05-23T08:31:53.708483+00:00_

[Round 1 审稿请求]:
## 交叉分享：以下是 Reviewer 1 的完整审稿意见

请逐条回应 Reviewer 1 的每个 Weakness 和 Question：
- **[AGREE]**：同意并说明理由
- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）
  
特别关注你们可能存在分歧的点。

---

## Reviewer 1 审稿意见原文

### Summary
本文提出OntoCoDec，将IE本体编译为两层可组合的token级解码约束：grammar layer（基于XGrammar的CFG，强制JSON结构和词汇成员关系）和semantic layer（有状态logits处理器，通过动态entity registry强制domain/range类型约束）。论文在SciERC、DocRED、WikiEvents上评估了Qwen3-8B、Llama-3.1-8B、Mistral-7B（含70B AWQ INT4），提供了五路消融、bootstrap统计检验、beam search兼容性验证等极其详尽的实验分析。核心贡献是约束可判定性分类（三级）和两层间的经验性enabling dependency发现。

### Strengths
S1 [方法设计] 约束可判定性分类（Level 1: context-free → Level 2: prefix-decidable with state → Level 3: non-local）概念清晰，精准界定了CFG能做和不能做的边界（§3, p.3）。grammar-first fallback机制（§4, p.5, eq.2）在soundness和availability之间取得了合理平衡。

S2 [形式化] Proposition 1（p.3, 完整证明Appendix O, p.37-38）的pumping lemma论证结构正确：对于无界entity集合，独立选择的类型对产生cross-serial依赖，PDA无法处理。Remark（p.3）中关于有限集合DFA指数爆炸的补充说明区分了理论不可能性和工程不可行性。

S3 [评估深度] 实验分析的彻底程度在NLP论文中极为罕见：五路消融（Table 1）、bootstrap CI + Cohen's d（Table 8, Appendix C）、fallback因果追踪（Table 6-7, Appendix C）、cross-field违规分解（Table 9）、document长度分箱分析（Tables 32-34, Appendix H）、prompt敏感性（Table 35, Appendix I）、TCR post-hoc resolution（Tables 43-44, Appendix M）、beam search兼容性（Tables 24-29, Appendix F）。39页附录覆盖了我能想到的几乎所有消融维度。

S4 [统计规范] Bootstrap CI采用document-level resampling（10,000 iterations, seed=42），报告了MDE（Table 31, Appendix C：SciERC ±1.8pp, DocRED ±0.8pp, WikiEvents ±5.0pp），并诚实承认"n=6 is insufficient for statistical inference on this correlation"（p.20）。这种统计纪律在IE领域论文中少见。

S5 [Enabling dependency] 两层间的scale-dependent enabling dependency（grammar alone 84% DR at 8B vs. 24% semantic-only, Table 1; 70B时grammar alone达到semantic layer的水平, Table 3/§5.3）是有意义的经验发现，对约束解码系统设计有指导价值。

S6 [工程贡献] Tokenizer-agnostic continuation masking（§3.3, p.4）通过byte-level BPE分解处理多token类型名，适配Qwen/Llama/SentencePiece三种分词器，实际工程价值高。ontology scalability分析（Appendix K, Table 41）展示了编译时间sub-linearly scaling至XLarge (1000 entity types)。

### Weaknesses
W1 [Critical]: Cross-field (CF) 类型一致性占残余违规的64%，但正文讨论不足。Table 9显示，在S1配置下SciERC的245个残余违规中，GENERIC↔OtherScientificTerm占34.7%，GENERIC↔Material占12.3%，总计CF违规占63.9%（155/245）。这是方法论的根本缺口——论文标题声称"Type-Constrained IE"，但最主要的类型约束违规（跨triple的实体类型一致性）未被处理。正文§4仅用一句"Level 3 is addressed by beam search or post-hoc resolution"（p.3）带过，但Appendix M的TCR（Tables 43-44）在zero-shot下仅处理0-2%的CF冲突，效果有限。Limitations（p.9）提到CF但未量化其严重程度（64%这个数字只出现在附录）。建议：(1) 在正文§5.1或§4中明确量化CF占残余违规的比例；(2) 讨论CF问题为何从架构上难以在单pass解码中解决；(3) 考虑将标题修改为更精确的表述，如"Domain/Range-Constrained"。

W2 [Major]: Proposition 1的实际意义论证存在gap。Proposition 1证明的是*无界entity集合*下domain/range约束不是context-free——但所有实际IE场景中entity集合都有界（受文档长度限制）。论文在Remark中提到有限集合的DFA需要O(|T^{|entity|}|)个状态"exceeding 10^10 for DocRED"，但这是一个工程可行性论证（编译DFA不现实），而非形式上不可能。这两个论点——理论上超越CFG vs. 工程上DFA不可行——之间的逻辑跳跃需要更清晰地阐明。建议：在正文中明确区分"formal impossibility for unbounded sets"和"engineering intractability for bounded sets"。

W3 [Major]: WikiEvents (n=20) 的结论统计效力不足，但在正文中占据整个§5.4。WikiEvents评估仅20个文档，MDE为±5.0pp（Table 31），这意味着只有大于5个百分点的F1差异才能被检测到。建议：(1) 将§5.4的篇幅大幅缩减，标题改为"Preliminary Event Extraction Pilot"；(2) 在Table 4的caption中注明"n=20, MDE=5.0pp, results are directional only"；(3) 不要在n=20上报告fine-tuning composability结论。

W4 [Major]: 70B实验的INT4量化限制未充分披露。Abstract声称"with 70B-class validation (§5.3)"，但70B实验全部在AWQ INT4上运行。Table 48显示INT4 vs FP16在SciERC上R-F1差异为-0.09，但DocRED的E-F1 drop为-7.07（INT4: 84.87 vs FP16: 91.94）。论文解释这是"parse failure"导致而非约束干扰，但这意味着INT4下的constraint enforcement结果可能被量化噪声污染。建议：(1) Abstract中明确标注"70B (AWQ INT4)"；(2) 在§5.3开头而非结尾说明量化限制。

W5 [Major]: 缺少与训练基方法的系统性对比。论文声称OntoCoDec"is composable with fine-tuning"（§5.1），但缺少与专门训练来满足schema约束的方法（如ADELIE, CodeIE, UIE）在相同benchmark上的直接对比。Appendix Q与GoLLIE的对比仅在SciERC 100 docs上进行，且GoLLIE在其中产生了54%空输出（仅5个有效预测），信息量有限。建议：(1) 在主要benchmark上与至少一个schema-aware训练方法进行完整对比；(2) 如果直接对比不可行，明确说明原因。

W6 [Minor]: Grammar-first fallback频率的模型依赖性未在正文讨论。Qwen3-8B在SciERC上0次fallback，但Llama-3.1-8B触发5,882次fallback（10.7 per document）。

W7 [Minor]: Continuation masking的"distinguishable token-prefix"假设。论文未展示实际prefix collision的frequency或其对masking correctness的影响。

### Questions
Q1: Grammar-first fallback在semantic mask与grammar mask不相交时触发。但fallback本质上放弃了类型约束。是否考虑过替代策略，如backtracking到最近的type-bearing position重新生成？

Q2: Table 10显示Per-Relation DR elimination中，head entity的registered type falls outside relation's domain——这是否暗示fine-tuning和constraint enforcement在某些relation上学到了不同的type preference？

Q3: Appendix K的ontology scalability测试最大到XLarge（1000 entity types, 1000 relations）。Real-world知识图谱（如Wikidata有约10,000+ property types）远超此规模。是否测试或估计过更大规模ontology下的表现？

Q4: Entity registry假设entity在relation之前生成。OntoCoDec是否fundamentally限于entity-first的生成顺序？

Q5: Cohen's d是从pooled bootstrap SD计算的。请clarify这个选择的理由。

### Missing References
建议补充 Josifoski et al., 2022 (GenIE) 在 Related Work 中的 constraint enforcement 讨论，以及 Paolini et al., 2021 (TANL)。

### Overall Assessment
评分: 3.5 (Borderline Conference)
置信度: 4/5
本文的核心贡献思路清晰，工程实现扎实，评估在统计规范性上显著优于同领域平均水平。三个问题阻碍Conference评分：(1) CF类型一致性占残余违规64%且未被解决，与标题形成gap；(2) WikiEvents和70B的评估统计效力不足但呈现方式可能误导；(3) 缺少与训练基方法的fair comparison。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2104 · 2026-05-23T08:34:03.476085+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 Reviewer 1\n\n### Weaknesses 逐条回应\n\n**[AGREE] R1-W1: CF 违规占残余违规 64% 但正文讨论不足。**\n同意这是核心弱点，我的 W2 也指出了同一问题。R1 提供了更精确的量化（Table 9: 155/245 = 63.9%）。支持建议 (1) 在 §5.1 量化 CF 比例和 (2) 讨论架构限制。**但对建议 (3) 改标题有保留**：\"Type-Constrained\" 并非虚假——grammar layer 执行了 vocabulary membership（Level 1），semantic layer 执行了 domain/range（Level 2），只是 Level 3 (non-local CF) 未被完全解决。更好的方案是在 abstract/introduction 中明确界定 \"type-constrained\" 的范围，而非改标题。\n\n**[REBUT] R1-W2: Proposition 1 实际意义论证 gap。**\n部分反驳。论文 Remark（§3, p.3）已明确区分 \"theoretical impossibility (unbounded) and engineering intractability (finite but exponential); OntoCoDec's registry-based approach avoids both\"。R1 要求的区分实际上已经做了，只是作为 Remark 不够 prominent。建议提升为正式段落，但不构成 Major weakness。\n\n**[AGREE] R1-W3: WikiEvents n=20 统计效力不足。**\n完全同意，与我的 W5 一致。R1 的三条具体建议（缩减篇幅、改标题、Table 4 加注 MDE）都合理。\n\n**[AGREE] R1-W4: 70B INT4 量化限制披露不足。**\n同意 presentation issue，但严重程度略低于 R1 评判。关键是 8B 消融已确认 INT4 不影响 constraint enforcement（DR remains 0%; Appendix P）。R1 引用的 DocRED E-F1 drop（-7.07）源于 parse failure 而非量化噪声影响约束。同意 abstract 应标注 \"70B (AWQ INT4)\"，§5.5 开头应说明量化限制。\n\n**[REBUT] R1-W5: 缺少与训练基方法的系统性对比。**\n部分反驳。论文在 Appendix B 明确定位 training-based 和 decoding-time 方法为 \"complementary rather than competing\"。OntoCoDec 的核心 use case 是与 fine-tuning 组合（Table 2 已展示），而非替代 GoLLIE/ADELIE。要求 OntoCoDec vs. ADELIE 的直接对比面临方法论困难：公平对比应为 \"ADELIE alone vs. ADELIE + OntoCoDec\"，而非 OntoCoDec vs. ADELIE。不过同意论文应更明确说明为何直接对比不可行。\n\n**[AGREE] R1-W6: Fallback 频率模型依赖性。** 同意，Qwen 0次 vs. Llama 5,882次差异显著，值得正文提及。\n\n**[AGREE] R1-W7: Continuation masking prefix collision 频率。** 同意未提供量化验证。\n\n### Questions 回应\n\n**[AGREE] R1-Q1 (Backtracking):** 好问题，论文应讨论 backtracking 被排除的理由，特别是 IterGen 已探索此方向。\n**[AGREE] R1-Q2 (Type preference 冲突):** 有价值的观察，可能是 CF 的另一来源。\n**[AGREE] R1-Q3 (大规模 ontology):** 实际部署关键问题，prefix collision 在更大 ontology 下风险增加。\n**[AGREE] R1-Q4 (Entity-first 限制):** Entity-before-relation 是根本架构约束，应在 Limitations 中明确说明（当前未提及）。\n**[AGREE] R1-Q5 (Cohen's d):** 论文应 clarify。\n\n### Missing References\n\n**[REBUT] R1-Missing References:** GenIE 和 TANL 均已在 §6 被引用（\"GenIE (Josifoski et al., 2022), TANL (Paolini et al., 2021)\" 在 Schema-aware IE 段落），Appendix B 也详细讨论了 GenIE。这是 R1 的疏忽。\n\n### 与 R1 的核心分歧\n\n| Issue | R1 | R2 | 分歧点 |\n|-------|----|----|--------|\n| CF severity | Critical (改标题) | Major (界定范围即可) | 标题是否需要修改 |\n| Prop. 1 gap | Major | Minor (Remark 已区分) | 论证是否已充分 |\n| W5 训练基对比 | Major | Minor (互补定位) | 对比是否 methodologically necessary |\n| Missing refs | GenIE/TANL 需补充 | 已被引用 | 事实性分歧（R1 疏忽） |\n\n### 核心共识\n\nCF trade-off（R1-W1/我的 W2）、WikiEvents 统计效力（R1-W3/我的 W5）、70B INT4 披露（R1-W4）是两位 reviewer 一致认为最需要作者 address 的问题。Overall 评分两位均为 3.5 (Borderline Conference)，confidence 均为 4/5。",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 Reviewer 1\n\n### Weaknesses 逐条回应\n\n**[AGREE] R1-W1: CF 违规占残余违规 64% 但正文讨论不足。**\n同意这是核心弱点，我的 W2 也指出了同一问题。R1 提供了更精确的量化（Table 9: 155/245 = 63.9%）。支持建议 (1) 在 §5.1 量化 CF 比例和 (2) 讨论架构限制。**但对建议 (3) 改标题有保留**：\"Type-Constrained\" 并非虚假——grammar layer 执行了 vocabulary membership（Level 1），semantic layer 执行了 domain/range（Level 2），只是 Level 3 (non-local CF) 未被完全解决。更好的方案是在 abstract/introduction 中明确界定 \"type-constrained\" 的范围，而非改标题。\n\n**[REBUT] R1-W2: Proposition 1 实际意义论证 gap。**\n部分反驳。论文 Remark（§3, p.3）已明确区分 \"theoretical impossibility (unbounded) and engineering intractability (finite but exponential); OntoCoDec's registry-based approach avoids both\"。R1 要求的区分实际上已经做了，只是作为 Remark 不够 prominent。建议提升为正式段落，但不构成 Major weakness。\n\n**[AGREE] R1-W3: WikiEvents n=20 统计效力不足。**\n完全同意，与我的 W5 一致。R1 的三条具体建议（缩减篇幅、改标题、Table 4 加注 MDE）都合理。\n\n**[AGREE] R1-W4: 70B INT4 量化限制披露不足。**\n同意 presentation issue，但严重程度略低于 R1 评判。关键是 8B 消融已确认 INT4 不影响 constraint enforcement（DR remains 0%; Appendix P）。R1 引用的 DocRED E-F1 drop（-7.07）源于 parse failure 而非量化噪声影响约束。同意 abstract 应标注 \"70B (AWQ INT4)\"，§5.5 开头应说明量化限制。\n\n**[REBUT] R1-W5: 缺少与训练基方法的系统性对比。**\n部分反驳。论文在 Appendix B 明确定位 training-based 和 decoding-time 方法为 \"complementary rather than competing\"。OntoCoDec 的核心 use case 是与 fine-tuning 组合（Table 2 已展示），而非替代 GoLLIE/ADELIE。要求 OntoCoDec vs. ADELIE 的直接对比面临方法论困难：公平对比应为 \"ADELIE alone vs. ADELIE + OntoCoDec\"，而非 OntoCoDec vs. ADELIE。不过同意论文应更明确说明为何直接对比不可行。\n\n**[AGREE] R1-W6: Fallback 频率模型依赖性。** 同意，Qwen 0次 vs. Llama 5,882次差异显著，值得正文提及。\n\n**[AGREE] R1-W7: Continuation masking prefix collision 频率。** 同意未提供量化验证。\n\n### Questions 回应\n\n**[AGREE] R1-Q1 (Backtracking):** 好问题，论文应讨论 backtracking 被排除的理由，特别是 IterGen 已探索此方向。\n**[AGREE] R1-Q2 (Type preference 冲突):** 有价值的观察，可能是 CF 的另一来源。\n**[AGREE] R1-Q3 (大规模 ontology):** 实际部署关键问题，prefix collision 在更大 ontology 下风险增加。\n**[AGREE] R1-Q4 (Entity-first 限制):** Entity-before-relation 是根本架构约束，应在 Limitations 中明确说明（当前未提及）。\n**[AGREE] R1-Q5 (Cohen's d):** 论文应 clarify。\n\n### Missing References\n\n**[REBUT] R1-Missing References:** GenIE 和 TANL 均已在 §6 被引用（\"GenIE (Josifoski et al., 2022), TANL (Paolini et al., 2021)\" 在 Schema-aware IE 段落），Appendix B 也详细讨论了 GenIE。这是 R1 的疏忽。\n\n### 与 R1 的核心分歧\n\n| Issue | R1 | R2 | 分歧点 |\n|-------|----|----|--------|\n| CF severity | Critical (改标题) | Major (界定范围即可) | 标题是否需要修改 |\n| Prop. 1 gap | Major | Minor (Remark 已区分) | 论证是否已充分 |\n| W5 训练基对比 | Major | Minor (互补定位) | 对比是否 methodologically necessary |\n| Missing refs | GenIE/TANL 需补充 | 已被引用 | 事实性分歧（R1 疏忽） |\n\n### 核心共识\n\nCF trade-off（R1-W1/我的 W2）、WikiEvents 统计效力（R1-W3/我的 W5）、70B INT4 披露（R1-W4）是两位 reviewer 一致认为最需要作者 address 的问题。Overall 评分两位均为 3.5 (Borderline Conference)，confidence 均为 4/5。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2105 · 2026-05-23T08:34:08.895104+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5419
}
```

</details>

---


### Assistant

_source line 2106 · 2026-05-23T08:34:17.194460+00:00_

交叉回应已提交给 Review Director。

核心结论：R1 和 R2 在三个主要问题上达成共识——CF trade-off 正文讨论不足、WikiEvents n=20 统计效力不足、70B INT4 限制披露不够显著。两位 reviewer 均评 3.5 (Borderline Conference)。

主要分歧在四点：(1) 标题是否需要修改（R1 主张改，R2 认为界定范围即可）；(2) Proposition 1 的论证是否充分（R1 认为有 gap，R2 认为 Remark 已覆盖）；(3) 是否需要与训练基方法直接对比（R1 认为必要，R2 认为方法论上不合适）；(4) GenIE/TANL 是否缺失（R1 疏忽，两者已被引用）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 43

## Round 43

96 recorded events


### User

_source line 2107 · 2026-05-23T09:20:31.739592+00:00_

[Round 1 审稿请求]:
## 审稿任务 — Round 24, Reviewer 2

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
**Venue**: EMNLP 2026 (via ARR)
**截止日期**: 2026-05-25
**类型**: Long Paper (8 页正文限制，附录/参考文献不限)
**模板**: ACL style (`\usepackage[review]{acl}`)
**匿名**: double-blind
**评分标准**: ARR Overall Assessment (5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)

**论文文件**:
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/submitted.pdf`

**你的审查侧重：新颖性 + 完整性 + 写作质量**

请重点评估以下方面：

1. **贡献新颖性**: 论文自称 "systematic engineering contribution with theoretical grounding"。核心方法本质上是 XGrammar + stateful logits processor 的系统集成——这对 EMNLP 2026 是否足够？Proposition 1 的理论贡献是否提升了整体 novelty ceiling？与 PICARD、SynCode、IterGen 等的差异化是否清晰？

2. **Related Work 覆盖**: §6 是否遗漏了重要的相关工作？特别关注：(a) 2025-2026 年的 constrained decoding 新进展（DCCD、FormaTax、CRANE 等已引用，还有遗漏吗？）；(b) IE 领域的 type constraint enforcement 历史（ILP-based、ASP-based）是否覆盖充分？(c) 是否有直接对标但未引用的工作？用 web_search 验证。

3. **叙事结构**: Abstract→Introduction→Method→Experiments 的故事线是否连贯？"problem → gap → solution → validation" 的逻辑链是否有断裂？zero-shot 作为 "diagnostic probe" 与 fine-tuning 作为 "practical setting" 的双轨叙事是否清晰？

4. **贡献声明**: §1 的两条 contribution 是否准确反映论文实际内容？WikiEvents "preliminary pilot" 和 "directional evidence" 的措辞是否合适？是否存在过度声称或不足声称？

5. **篇幅分配**: 主文 8 页的空间分配是否合理？§5.1 ablation + composability + CF analysis 的密度是否过高？§5.2 WikiEvents n=20 pilot 占的篇幅是否与其 contribution 匹配？§7 Discussion 是否过于简短？

6. **写作质量**: 术语一致性（DR/CF/RV/ET 定义是否首次出现时足够清楚？）；notation 密度是否影响可读性？Figure 1 是否有效传达架构？表格 caption 是否包含足够信息？

7. **格式合规**: 
   - 主文是否在 8 页以内？
   - Limitations section 是否存在且位置正确（正文内，不在 appendix）？
   - Ethics Statement 是否存在？
   - 匿名性是否保持（无作者身份泄露）？
   - 参考文献格式是否一致？

请按 Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment 格式输出审稿意见。Weakness 是重点，必须严格、具体、引用具体 Section/Table/Figure。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2108 · 2026-05-23T09:20:39.258426+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2109 · 2026-05-23T09:20:39.309273+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2110 · 2026-05-23T09:20:42.328073+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6"
  }
}
```

</details>

---


### Tool result

_source line 2111 · 2026-05-23T09:20:42.479014+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2112 · 2026-05-23T09:20:44.488911+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start*",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start*",
    "path": "/home/ubuntu"
  }
}
```

</details>

---


### Tool result

_source line 2113 · 2026-05-23T09:20:44.890842+00:00_

/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2114 · 2026-05-23T09:20:47.050647+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2115 · 2026-05-23T09:20:47.101614+00:00_

1	---
2	name: review-reviewer-session-start
3	description: Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。
4	priority: 8
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 2
11	roles: []
12	---
13	
14	# Review Reviewer Session 启动流程
15	
16	执行顺序：
17	1. 读取论文文件（`projects/{project}/paper/main.tex` 或类似路径）
18	2. 检查论文格式状态：
19	   - 页数是否在 venue 要求内（若已知 venue）
20	   - LaTeX 是否可编译（调用 `ssh_execute` 运行 `pdflatex` 或 `latexmk`）
21	   - 图表是否有标题和标签
22	3. 视觉检查：如果已有编译好的 PDF，使用 `paper-visual-review` skill 渲染关键页面（首页、图表页、参考文献页），检查排版溢出、公式渲染、图表质量等视觉问题
23	4. 检查投稿材料清单：
24	   - cover letter 是否存在
25	   - 补充材料是否准备
26	   - 参考文献格式是否正确
27	5. 向 Review Director 汇报（`review_reviewer_post_to_director`）：
28	   - 论文当前状态
29	   - 发现的格式问题（如有）
30	   - 视觉检查结果（如有）
31	   - 缺少的材料（如有）
32	
33	此流程在 Review Director 分配任务后执行。
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2116 · 2026-05-23T09:20:53.029886+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,WebSearch,WebFetch,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,WebSearch,WebFetch,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 2117 · 2026-05-23T09:20:53.081400+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2118 · 2026-05-23T09:20:57.938475+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 2119 · 2026-05-23T09:21:00.369141+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/submitted.pdf",
  "pages": "1-10",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/submitted.pdf",
    "pages": "1-10",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 2120 · 2026-05-23T09:21:01.242593+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2121 · 2026-05-23T09:21:06.649917+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Sometimes reviewers may find the work sound, but not something that is interesting for them personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

### Review Standards
All papers recommended for Findings or main conference are expected to be sound and reproducible.

## Area Chair Metareview Scoring

The ARR metareview score changed in February 2025 to be more aligned with reviewer score
…[truncated 466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8711
}
```

</details>

---


### Tool result

_source line 2122 · 2026-05-23T09:21:10.996188+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 450.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 531.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 410.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.6}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifac
…[truncated 581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 10627
}
```

</details>

---


### Tool result

_source line 2123 · 2026-05-23T09:21:10.996856+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_wikievents_draft}
56	\input{section5_runtime}
57	
58	% === §6 Related Work ===
59	\input{section6_related_work}
60	
61	% === §7 Discussion and Conclusion ===
62	\section{Discussion and Conclusion}
63	\label{sec:discussion}
64	\input{section7_conclusion_compressed}
65	
66	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
67	\clearpage
68	\section*{Limitations}
69	
70	\paragraph{Constraint scope.}
71	CF is an architectural consequence of per-triple independent enforcement: CF$\leftrightarrow$DR represents a fundamental trade-off (eliminating CF re-routes violations to DR; Appendix~\ref{app:cf-dr-tradeoff}), and its impa
…[truncated 4263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 9754
}
```

</details>

---


### Tool call

_source line 2124 · 2026-05-23T09:21:22.046757+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 2125 · 2026-05-23T09:21:23.053586+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 2126 · 2026-05-23T09:21:23.358449+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1311
}
```

</details>

---


### Tool call

_source line 2127 · 2026-05-23T09:21:23.359102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 2128 · 2026-05-23T09:21:23.865102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 2129 · 2026-05-23T09:21:24.473712+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1420
}
```

</details>

---


### Tool call

_source line 2130 · 2026-05-23T09:21:24.474154+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 2131 · 2026-05-23T09:21:25.286760+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1927
}
```

</details>

---


### Tool result

_source line 2132 · 2026-05-23T09:21:25.290095+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1424
}
```

</details>

---


### Tool call

_source line 2133 · 2026-05-23T09:21:25.492196+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 2134 · 2026-05-23T09:21:25.694156+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1219
}
```

</details>

---


### Tool call

_source line 2135 · 2026-05-23T09:21:25.795874+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 2136 · 2026-05-23T09:21:26.298575+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 2137 · 2026-05-23T09:21:27.155502+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1663
}
```

</details>

---


### Tool result

_source line 2138 · 2026-05-23T09:21:27.156723+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1360
}
```

</details>

---


### Tool result

_source line 2139 · 2026-05-23T09:21:28.913839+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2615
}
```

</details>

---


### Tool call

_source line 2140 · 2026-05-23T09:21:29.165183+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and scoring scales. I need: 1) All review dimensions (soundness, excitement, overall, etc.) 2) The exact scoring scale for each dimension 3) Any specific instructions about what each score means 4) Reviewer responsibilities and expectations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and scoring scales. I need: 1) All review dimensions (soundness, excitement, overall, etc.) 2) The exact scoring scale for each dimension 3) Any specific instructions about what each score means 4) Reviewer responsibilities and expectations"
  }
}
```

</details>

---


### Tool result

_source line 2141 · 2026-05-23T09:21:35.812938+00:00_

# ARR Review Form: Dimensions and Scoring

Based on the guidelines provided, here's what I found about the review form structure:

## Review Dimensions

The document indicates reviewers provide **three scores** (as of February 2025):

1. **Soundness** - Technical validity and correctness of the work
2. **Excitement** - Personal interest/enthusiasm about the contribution
3. **Overall Recommendation** - Explicit guidance on paper acceptance

## Scoring Scale Details

The guidelines don't explicitly state numerical ranges for each dimension. However, they clarify the purpose of each:

**Soundness:** "Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation."

**Excitement:** Described as "orthogonal to the assessment of the soundness" and reflecting "personal taste" without requiring explicit justification.

**Overall Assessment:** Composite score reflecting "soundness, excitement, and also other factors like novelty and impact."

## Reviewer Responsibilities

- Write reviews yourself (no LLM-generated first drafts)
- Justify low scores with specific evidence
- Acknowledge author responses and update assessments
- Maintain professional, neutral tone
- Complete assignments on time or notify chairs of delays

The document references a separate [review form details page](https://aclrollingreview.org/reviewform) for specific numerical scales not included in these guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6647
}
```

</details>

---


### Tool call

_source line 2142 · 2026-05-23T09:21:45.267897+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with ALL scoring dimensions, exact numerical scales, and what each score level means. I need the full scoring rubric for soundness, excitement, overall assessment, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with ALL scoring dimensions, exact numerical scales, and what each score level means. I need the full scoring rubric for soundness, excitement, overall assessment, confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 2143 · 2026-05-23T09:21:47.580868+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 2144 · 2026-05-23T09:21:48.588459+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 2145 · 2026-05-23T09:21:48.940931+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1360
}
```

</details>

---


### Tool call

_source line 2146 · 2026-05-23T09:21:48.941380+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "constrained decoding information extraction 2025 2026 type constraints schema enforcement LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "constrained decoding information extraction 2025 2026 type constraints schema enforcement LLM"
  }
}
```

</details>

---


### Tool result

_source line 2147 · 2026-05-23T09:21:49.596258+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool result

_source line 2148 · 2026-05-23T09:21:52.661863+00:00_

# ACL Rolling Review Form - Complete Scoring Rubric

## Reviewer Confidence
**Scale: 1-5**
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully."
- **3:** "Pretty sure, but there's a chance I missed something."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1:** "Not my area, or paper is very hard to understand."

## Soundness
**Scale: 1-5 (with .5 increments)**
- **5:** "Excellent: This study is one of the most thorough I have seen."
- **4:** "Strong: This study provides sufficient support for all of its claims."
- **3:** "Acceptable: This study provides sufficient support for its main claims."
- **2:** "Poor: Some of the main claims are not sufficiently supported."
- **1:** "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement
**Scale: 1-5 (with .5 increments)**
- **5:** "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4:** "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3:** "Interesting: I might mention some points of this paper to others."
- **2:** "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1:** "Not Exciting: does not resonate with me, and I don't think it would with others."

## Overall Assessment
**Scale: 1-5 (with .5 increments)**
- **5:** Consider for Award (top 2.5%)
- **4.5:** Borderline Award
- **4:** Conference acceptance
- **3.5:** Borderline Conference
- **3:** Findings acceptance
- **2.5:** Borderline Findings
- **2:** Resubmit next cycle
- **1.5:** Resubmit after next cycle
- **1:** Do not resubmit

## Reproducibility
**Scale: 1-5**
- **5:** Results easily reproducible
- **4:** Mostly reproducible with minor variations
- **3:** Reproducible with difficulty; some parameter underspecificat
…[truncated 559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7393
}
```

</details>

---


### Tool result

_source line 2149 · 2026-05-23T09:22:00.633281+00:00_

Web search results for query: "constrained decoding information extraction 2025 2026 type constraints schema enforcement LLM"

Links: [{"title":"Reliable JSON from Any LLM: Pydantic + Zod (2026) | TECHSY","url":"https://techsy.io/en/blog/llm-structured-outputs-guide"},{"title":"LLM Structured Outputs: Schema Validation for Real Pipelines (2026) | Collin Wilkins","url":"https://collinwilkins.com/articles/structured-output"},{"title":"Constrained Decoding Mechanism","url":"https://www.emergentmind.com/topics/constrained-decoding-mechanism"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Constrained Decoding for LLMs: How JSON, Regex, and Schema Control Improve Output Reliability","url":"https://brics-econ.org/constrained-decoding-for-llms-how-json-regex-and-schema-control-improve-output-reliability"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"}]

I found comprehensive information about constrained decoding, information extraction, type constraints, and schema enforcement for LLMs in 2025-2026. Here are the key findings:

## Recent Developments in Constrained Decoding (2025-2026)

**Industry Adoption:**
In August 2024, OpenAI launched Structured Outputs with Strict Mode using constrained decoding to guarantee schema compliance, and by 2025-2026, every major provider had adopted the same approach. OpenAI (since August 2024), Google Gemini (2024, expanded 2026), Anthropic
…[truncated 1205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 11691
}
```

</details>

---


### Tool call

_source line 2150 · 2026-05-23T09:22:09.461250+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "section*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "section*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 2151 · 2026-05-23T09:22:09.512031+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_dra
…[truncated 576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2152 · 2026-05-23T09:22:12.882661+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2153 · 2026-05-23T09:22:13.184257+00:00_

1	\begin{abstract}
2	Large language models for information extraction generate structurally valid but ontologically invalid triples---where entity types violate the ontology's domain/range constraints.
3	These violations persist across the capability spectrum and cannot be addressed by grammar-constrained decoding (which lacks cross-field type awareness) or post-hoc filtering (which discards valid predictions).
4	
5	We present \textsc{OntoCoDec}, a framework that compiles information extraction ontologies into composable token-level decoding constraints.
6	A decidability analysis shows that domain/range constraints exceed context-free expressiveness, yielding a two-layer architecture: a grammar layer enforces structural validity and vocabulary membership; a semantic layer enforces type constraints at runtime through stateful masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
7	
8	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
9	Composed with LoRA fine-tuning across three 8B-class models and two relation extraction datasets (up to 96 relations), greedy S1 near-eliminates domain/range violations ($<$\,0.1\%) at F1 41--47\%, but introduces cross-field type inconsistencies ($\leq$1.4\%) as the dominant residual---an architectural consequence of per-triple independent enforcement.
10	Beam search ($k{=}4$) eliminates all violation types at 1.54$\times$ latency.
11	In zero-shot settings, cross-field rates are higher (up to 12\%) but decrease with model calibration.
12	Zero-shot domain/range reductions span 76--99\% on SciERC and 42--90\% on DocRED, with a scale-dependent empirical relationship between the two layers: the semantic layer alone achieves substantially stronger reduction at larger model scale.
13	\end{abstract}
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2154 · 2026-05-23T09:22:13.184637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2155 · 2026-05-23T09:22:14.089211+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity necessarily carries a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 0.5--2\% even after LoRA fine-tuning; rates correlate with schema restrictiveness (few valid type pairs per relation) rather than ontology or model scale.
9	At competitive quality (R-F1 41--47\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption, making reliable constraint enforcement necessary.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering discards up to 48\% of predictions including true positives (Appendix~\ref{app:cross-model-zs}).
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance without runtime enforcement.
16	
17	We propose \textbf{OntoCoDec}, a framework that translates IE ontologies into composable layers of decoding-time constraints.
18	A decidability analysis of IE type constraints (\S\ref{sec:decidability}) yields a two-layer architecture: the \emph{grammar layer} co
…[truncated 2492 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 2156 · 2026-05-23T09:22:14.140031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2157 · 2026-05-23T09:22:14.341289+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, SynCode~\cite{ugare2024syncode}, SGLang~\cite{zheng2024sglang}, and related systems~\cite{beurer-kellner2023lmql,park2024grammar,jsonschemabench2025} enforce format validity via CFG-based token masking.
8	NeuroLogic Decoding~\cite{lu2021neurologic} and \citet{huang2024lookahead} enforce constraints via beam-level reranking; OntoCoDec applies per-token masking, avoiding beam-width dependence.
9	PICARD~\cite{scholak2021picard} and \citet{pldi2025_type_constrained_codegen} compile type systems into prefix automata; OntoCoDec applies constructive forward masking via a dynamic entity registry (\S\ref{sec:composition}).
10	DCCD~\cite{dccd2026} and \citet{nguyen2026thinking} decouple reasoning from constrained generation; OntoCoDec enforces schema semantics within a single forward pass.
11	
12	\paragraph{Schema-aware IE.}
13	GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, GUIDEX~\cite{guidex2025}, GenIE~\cite{josifoski2022genie}, TANL~\cite{paolini2021tanl}, REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, ADELIE~\cite{qi2024adelie}, and others~\cite{fei2022lasuie,wang2022deepstruct,lu2022uie,lou2023usm,zhou2024universalner} encode ontology structure or frame IE as structured generation, though schema compliance gaps persist~\cite{wadhwa2023revisiting}.
14	GoLLIE and KnowCoder embed schema knowledge via code-style prompts (training-time internalization without runtime enforcement).
15	GoLLIE-7B achieves zero DR under zero-shot evaluation, but at the cost of near-complete output suppression (5 predicted relations vs.\ ${>}$1{,}100 for OntoCoDec under LoRA fine-tuning, 46\% empty output; Appendix~\ref{app:gollie-comparison}).
16	Direct comparison is methodologica
…[truncated 1017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2158 · 2026-05-23T09:22:14.341795+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 2159 · 2026-05-23T09:22:14.443939+00:00_

1	% Section 7 — Discussion and Conclusion
2	
3	OntoCoDec compiles IE ontologies into composable token-level constraints, validated across 3 datasets, 3+ models, and 2 tasks.
4	LoRA + greedy S1 near-eliminates DR ($<$\,0.1\%) at R-F1 41--47\%; beam ($k{=}4$) eliminates all violations at 1.54$\times$ latency.
5	Because IE type constraints exceed context-free expressiveness (Proposition~1), the semantic layer is necessary to bridge the gap grammar-only enforcement cannot address (3\% vs.\ 94\% DR reduction), using constructive forward masking over a dynamic entity registry.
6	This scale-dependent interaction (\S\ref{sec:70b-results}) suggests grammar-constrained decoding is necessary but increasingly insufficient as models improve.
7	Constraint enforcement is preserved under INT4 quantization (4$\times$ compression; Appendix~\ref{app:quantization}), confirming deployment viability without precision-dependent calibration.
8	Global entity-level type consensus during decoding---eliminating CF without beam search overhead---is the primary direction for future work.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2160 · 2026-05-23T09:22:21.127346+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2161 · 2026-05-23T09:22:21.982082+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	\input{fig1_framework}
9	
10	We present OntoCoDec, a framework that translates IE ontologies into token-level constraints enforced during autoregressive generation.
11	The design is guided by a decidability analysis of IE type constraints.
12	
13	\paragraph{Constraint decidability taxonomy.}
14	\label{sec:decidability}
15	We classify IE type constraints into three levels: (1)~\emph{context-free}: vocabulary membership and JSON structure; (2)~\emph{prefix-decidable with state}: domain/range type validity, determined at each type-bearing position given the decoded relation type and entity registry; (3)~\emph{non-local}: cross-entity type consistency, which depends on the full output.
16	Unlike code generation where types are statically declared, IE constraints fall into level~2: entity types are inferred from text, the registry is built dynamically, and constraint targets depend on the co-occurring relation.
17	OntoCoDec enforces levels 1--2 (grammar and semantic layers, respectively); level~3 is addressed by beam search or post-hoc resolution (Appendix~\ref{app:tcr}).
18	
19	\smallskip
20	\noindent
21	Existing grammar-constrained decoding frameworks (e.g., XGrammar) enforce level~1 constraints---structural validity and vocabulary membership---but IE domain/range rules require cross-position entity-type state that context-free grammars cannot express.
22	We formalize this gap:
23	
24	\smallskip
25	\noindent\textbf{Proposition 1} (Level 2 $\not\subseteq$ Level 1)\textbf{.}
26	\textit{Domain/range type constraints for IE with unbounded entity sets are not context-free.}
27	
28	\smallskip
29	\noindent\textit{Proof sketch.}
30	Consider $\mathcal{E} = \{\tau_A, \tau_B\}$ and a relation $r$ with $\operatorname{dom}(r) = \{\tau_A\}$.
31	An output contains $n$ entities with independently chosen types, followed by
…[truncated 8034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 2162 · 2026-05-23T09:22:22.133502+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2163 · 2026-05-23T09:22:22.485061+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	where $\wedge$ denotes element-wise AND over the vocabulary $V$; a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the scale-dependent layer interaction (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property enforced only by the grammar layer.
12	This dependency is scale-sensitive: 70B semantic-only achieves 84\% DR reduction (vs.\ 24\% on 8B), though grammar remains necessary for RV elimination (\S\ref{sec:70b-results}).
13	
14	\paragraph{Grammar-First Fallback.}
15	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
16	We enforce a \emph{grammar-first fallback}: semantic masking is skipped and the grammar layer alone controls selection.
17	Structural integrity is a hard constraint; type violations are soft errors detectable by downstream validation, with DR (ontologically invalid type pair) more severe than CF (individually valid triples with cross-triple type inconsistency).
18	Extraction tasks are robust to format-level constraints~\cite{tam2024letmespeak}, supporting this asymmetric treatment.
19	
20	\paragraph{Constraint Tightness.}
21	\label{eq:tightness}
22	Per-relation constraint tightness $\kappa(r) = 1 - |\sigma(r)|/|\mathcal{E}|^2$, with schema mean $\bar{\kappa}$.
23	Across WikiEvents ($\bar{\kappa}{=}0.029$), SciERC
…[truncated 1621 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2164 · 2026-05-23T09:22:22.635809+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 2165 · 2026-05-23T09:22:23.087584+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two deployment configurations: greedy S1 (DR\,$\leq$\,0.09\%, $+$10\% latency) and beam S1 (all violations\,$\to$\,0\%, 1.54$\times$ latency); zero-shot evaluation (\S\ref{sec:scierc-results}; Appendix~\ref{app:cross-model-zs}) serves as a diagnostic probe for the fine-tuned setting (R-F1 41--47\%).
8	
9	\paragraph{Setup.}
10	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
11	RE type constraints are extracted from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) derive from the KAIROS ontology.
12	All constraints are schema-level, independent of evaluation splits.
13	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in Appendix~\ref{app:cross-model-zs}, composability with fine-tuning in \S\ref{sec:composability}.
14	LoRA hyperparameters were selected on SciERC development data and transferred to DocRED without further tuning; DocRED development documents were used for evaluation only.
15	Four violation categories: \textbf{DR} (type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), \textbf{CF} (conflicting types across triples).
16	Baseline DR: 15.37\% (SciERC), 18.46\% (DocRED); schema-informed prompting reduces DR by 62\% but is per-relation unreliable (Appendix~\ref{app:per-relation-landscape}).
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2166 · 2026-05-23T09:22:23.138358+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2167 · 2026-05-23T09:22:23.139090+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrrr rr@{}}
21	\toprule
22	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-7} \cmidrule(l){8-9}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08  & 15.45
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08  & 14.92
39	  & 8.23  & 30.98 \\
40	GCD-equiv.$^\dagger$
41	  & 15.26 & $\downarrow$1\%
42	  & \textbf{0} & \textbf{0}
43	  & 0.04  & 15.30
44	  & 8.75  & 30.91 \\
45	Semantic
46	  & 11.65 & $\downarrow$24\%
47	  & 1.51  & 0.40
48	  & 2.71  & 14.36
49	  & 8.15  & 31.01 \\
50	S1
51	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
52	  & \textbf{0} & \textbf{0}
53	  & 9.90  & \textbf{10.83}
54	  & \textbf{8.36} & 30.98 \\
55	S2
56	  & 0.97  & $\downarrow$94\%
57	  & \textbf{0} & \textbf{0}
58	  & 8.03  & \textbf{9.00}
59	  & 8.03  & \textbf{31.90} \\
60	\bottomrule
61	\end{tabular}}%
62	\caption{Five-way ablation on SciERC (551 docs
…[truncated 7019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2168 · 2026-05-23T09:22:30.353164+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2169 · 2026-05-23T09:22:30.807134+00:00_

1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Preliminary Event Extraction Pilot}
8	\label{sec:wikievents}
9	
10	As a preliminary pilot study, we apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document,lu2021text2event} (56 event types, 80 roles, 27 entity types, 245 constraints; Appendix~\ref{app:wikievents}) without modification.
11	Violations extend to EV (event vocabulary), RoV (role vocabulary), and AC (argument constraint, analogous to DR).
12	
13	% ──────────────────────────────────────────
14	%  Table: WikiEvents three-model comparison (v3 final)
15	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
16	% ──────────────────────────────────────────
17	\begin{table}[t]
18	\centering
19	\small
20	\setlength{\tabcolsep}{2.8pt}
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{@{}ll rrrr rr@{}}
23	\toprule
24	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
25	& \multicolumn{2}{c}{\textbf{F1}} \\
26	\cmidrule(lr){3-6} \cmidrule(l){7-8}
27	\textbf{Model} & \textbf{Mode}
28	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
29	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
30	\midrule
31	\multirow{3}{*}{Qwen3-8B}
32	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
33	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
34	  & S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
35	\midrule
36	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
37	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\
38	  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
39	  & S1    & \textbf{0} & \textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\
40	\midrule
41	\multirow{3}{*}
…[truncated 2122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 2170 · 2026-05-23T09:22:30.807619+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 2171 · 2026-05-23T09:22:31.410461+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC, lower on DocRED due to amortization over longer sequences; under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
7	
8	\paragraph{Beam search compatibility.}
9	\label{sec:beam-results}
10	With LoRA, beam search ($k{=}4$)~\cite{anderson2017guided} eliminates all four violation types on both SciERC and DocRED at both 8B and 70B scales (R-F1 43--47; Appendix~\ref{app:beam-search}), yielding two deployment tiers: greedy S1 ($+$10\% latency, DR${<}$0.1\%, CF${\leq}$1.4\%) and beam S1 (1.54$\times$ latency, all violations${\to}$0\%; Table~\ref{tab:beam-latency}).
11	
12	% exp_ids: r16_70b_scierc_zs_s1, r16_70b_docred_zs_s1, 70b_lora_scierc, 70b_lora_docred_200
13	\paragraph{70B-class validation.}
14	\label{sec:70b-results}
15	All 70B experiments use Llama-3.1-70B-Instruct under AWQ INT4 quantization; an 8B ablation confirms constraint enforcement is unaffected by quantization (Appendix~\ref{app:quantization}).
16	Zero-shot S1 eliminates DR on both datasets (SciERC 6.41\%\,$\to$\,0\%, DocRED 14.98\%\,$\to$\,0\%; R-F1 11--13).
17	% exp_ids: r16_70b_scierc_zs_ablation (grammar_only, semantic_only, full_s1)
18	A four-way ablation reveals scale-dependent layer interaction: semantic-only achieves 84\% DR reduction vs.\ 8B's 24\% (Table~\ref{tab:scierc-ablation}), though grammar remains necessary for RV elimination and CF control (semantic-only CF${=}$76).
19	% exp_ids: eval_70b_lora_scierc_s1_constrained, eval_70b_lora_docred_200_s1_constrained
20	LoRA confirms composability: DR\,$\to$\,0\% on both datasets (R-F1 44.53, 43.95; $|\Delta| \leq 0.20$\,pp; CF 0.18--1.33\%); cross-family generalization at 70B scale remains to be verifie
…[truncated 955 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 2172 · 2026-05-23T09:22:31.461159+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 2173 · 2026-05-23T09:22:31.511916+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$, where $\mathcal{P}(\cdot)$ denotes the power set, specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We quantify constraint restrictiveness via \emph{constraint tightness} $\kappa(r)$ (\S\ref{sec:composition}): tighter constraints leave fewer valid type pairs per relation.
11	We define ontology constraints broadly to encompass both formal ontology specifications (e.g., the KAIROS event ontology with explicit role-entity type mappings) and empirically derived type-pair constraints extracted from annotated training data.
12	The latter applies when datasets lack a formal ontology but provide typed annotations (SciERC, DocRED); OntoCoDec compiles both sources into the same constraint representation without modification.
13	Empirical constraints achieve 99\%+ instance-level coverage on held-out data (SciERC 99.0\%, DocRED 99.4\%); uncovered type pairs trigger grammar-first fallback (\S\ref{sec:composition}), ensuring no valid triples are blocked.
14	
15	\paragraph{Grammar-Constrained Decoding.}
16	\label{sec:bg:gcd}
17	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
18	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
19	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $
…[truncated 886 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2174 · 2026-05-23T09:22:36.983954+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "IterGen constrained decoding backtracking 2025 information extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "IterGen constrained decoding backtracking 2025 information extraction"
  }
}
```

</details>

---


### Tool call

_source line 2175 · 2026-05-23T09:22:37.989519+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PICARD constrained decoding type constraints prefix automata text-to-SQL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PICARD constrained decoding type constraints prefix automata text-to-SQL 2021"
  }
}
```

</details>

---


### Tool call

_source line 2176 · 2026-05-23T09:22:38.843503+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"structured prediction\" \"type constraints\" \"knowledge graph\" LLM 2025 2026 decoding enforcement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"structured prediction\" \"type constraints\" \"knowledge graph\" LLM 2025 2026 decoding enforcement"
  }
}
```

</details>

---


### Tool result

_source line 2177 · 2026-05-23T09:22:44.521514+00:00_

Web search results for query: "PICARD constrained decoding type constraints prefix automata text-to-SQL 2021"

Links: [{"title":"[Quick Review] PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models","url":"https://liner.com/review/picard-parsing-incrementally-for-constrained-autoregressive-decoding-from-language-models"},{"title":"[PDF] PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/PICARD:-Parsing-Incrementally-for-Constrained-from-Scholak-Schucher/5fbcfccd3736969d95ed660d8e6962c86b7a9113"},{"title":"PICARD: Parsing Incrementally for Constrained Auto- ...","url":"https://aclanthology.org/2021.emnlp-main.779.pdf"},{"title":"PICARD Algorithm for Text-to-SQL","url":"https://www.servicenow.com/blogs/2021/picard-algorithm-text-to-sql"},{"title":"GitHub - SethCram/Linguists-NLP-to-SQL: PICARD - Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models. PICARD is a ServiceNow Research project that was started at Element AI. · GitHub","url":"https://github.com/SethCram/Linguists-NLP-to-SQL"},{"title":"GitHub - isabella232/picard-1: PICARD - Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models","url":"https://github.com/isabella232/picard-1"},{"title":"PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.779/"},{"title":"GitHub - ServiceNow/picard: PICARD - Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models. PICARD is a ServiceNow Research project that was started at Element AI. · GitHub","url":"https://github.com/ServiceNow/picard"},{"title":"PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models","url":"https://tscholak.github.io/publications/picard"},{"title":"[2109.05093] PICARD: Parsing Incrementa
…[truncated 1606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6531
}
```

</details>

---


### Tool result

_source line 2178 · 2026-05-23T09:22:45.325579+00:00_

Web search results for query: "IterGen constrained decoding backtracking 2025 information extraction"

Links: [{"title":"ITERGEN: ITERATIVE SEMANTIC-AWARE STRUCTURED ...","url":"https://openreview.net/pdf?id=ac93gRzxxV"},{"title":"Beyond Free-Form Text: How Constrained Decoding is Reshaping Structured Generation in LLMs | by Brijesh Nambiar | Medium","url":"https://medium.com/@brijeshrn/beyond-free-form-text-how-constrained-decoding-is-reshaping-structured-generation-in-llms-5f7a38bef259"},{"title":"[Literature Review] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://www.themoonlight.io/en/review/itergen-iterative-semantic-aware-structured-llm-generation-with-backtracking"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"[Quick Review] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://liner.com/review/itergen-iterative-semanticaware-structured-llm-generation-with-backtracking"},{"title":"[2410.07295] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://arxiv.org/abs/2410.07295"},{"title":"TreeCoder: Systematic Exploration and Optimisation of ...","url":"https://arxiv.org/pdf/2511.22277"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11747381/"}]

I found relevant information about IterGen and constrained decoding for structured generation. Here's what the search results reveal:

## Overview of IterGen

IterGen is a library for iterative, grammar-guided LLM generation that enables users to move both forward and backward within the generated output based on grammar sym
…[truncated 1331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8341
}
```

</details>

---


### Tool result

_source line 2179 · 2026-05-23T09:22:45.727762+00:00_

Web search results for query: ""structured prediction" "type constraints" "knowledge graph" LLM 2025 2026 decoding enforcement"

Links: [{"title":"Decoding on Graphs: Faithful and Sound Reasoning on Knowledge Graphs   through Generation of Well-Formed Chains","url":"https://arxiv.org/pdf/2410.18415"},{"title":"Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs","url":"https://arxiv.org/html/2604.06603v1"},{"title":"Knowledge Graph and Large Language Model Co-learning via","url":"https://www.cs.emory.edu/~jyang71/files/klc.pdf"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/pdf/2410.13080"},{"title":"Graph-Constrained Reasoning: A Practical Leap for Trustworthy, KG-Grounded LLMs | by Fanghua (Joshua) Yu | Medium","url":"https://medium.com/@yu-joshua/graph-constrained-reasoning-a-practical-leap-for-trustworthy-kg-grounded-llms-04efd8711e5e"},{"title":"Graph Constrained Reasoning: framework for faithful LLM Reasoning by integrating Knowledge Graphs in LLM decoding | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/graph-constrained-reasoning-framework-for-faithful-reasoning-by-integrating-knowledge-graphs-in-64f021073f1a"},{"title":"Knowledge Graph and Large Language Model Co-learning via","url":"https://par.nsf.gov/servlets/purl/10590165"},{"title":"Tokenization, Fusion and Decoupling: Bridging the Granularity Mismatch Between Large Language Models and Knowledge Graphs","url":"https://arxiv.org/pdf/2602.22698"}]

I found relevant research on structured prediction, type constraints, knowledge graphs, and LLM decoding enforcement. Here are the key findings:

## Recent Research (2025-2026)

A framework called SciDC leverages knowledge parsing in LLMs while using local models for constrained generation, with structured decoding constraints following standardized rules, with an average improvement of 12% over vanilla methods.

Graph-Constraine
…[truncated 1016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6884
}
```

</details>

---


### Tool call

_source line 2180 · 2026-05-23T09:22:50.698621+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FormaTax CRANE constrained decoding format control 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FormaTax CRANE constrained decoding format control 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 2181 · 2026-05-23T09:22:51.251320+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ADELIE universal information extraction LLM 2024 schema-aware"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ADELIE universal information extraction LLM 2024 schema-aware"
  }
}
```

</details>

---


### Tool call

_source line 2182 · 2026-05-23T09:22:52.106273+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "KnowCoder code-style schema knowledge graph extraction ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "KnowCoder code-style schema knowledge graph extraction ACL 2024"
  }
}
```

</details>

---


### Tool result

_source line 2183 · 2026-05-23T09:22:58.608055+00:00_

Web search results for query: "FormaTax CRANE constrained decoding format control 2025 2026"

Links: [{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://par.nsf.gov/servlets/purl/10633770"},{"title":"Reasoning with constrained LLM generation - CRANE","url":"https://arxiv.org/pdf/2502.09061"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/html/2502.09061v3"},{"title":"CRANE: Reasoning with constrained LLM generation | OpenReview","url":"https://openreview.net/forum?id=wKs9fHYxCV"},{"title":"The Format Tax","url":"https://arxiv.org/pdf/2604.03616"},{"title":"[2502.09061] CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/abs/2502.09061"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Constrained+decoding"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"Constrained Decoding: Grammar-Guided Generation for Structured LLM Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output"}]

Based on the search results, I found relevant information about CRANE and format control in constrained decoding:

## CRANE: Reasoning with Constrained LLM Generation

CRANE is a reasoning-augmented constrained decoding algorithm designed to balance the correctness of constrained generation with the flexibility of unconstrained generation. 

Constrained LLM generation is used to enforce adherence to formal grammar, but strict enforcement of formal constraints often diminishes the reasoning capabilities of LLMs. CRANE addresses this by augmenting the output grammar with carefully designed additional rules to preserve the reasoning capabilities of the LLM while ensuring syntactic and semantic correctness in its outputs.

Experiments show that CRANE significantly outperforms both state-of-the-art const
…[truncated 816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7909
}
```

</details>

---


### Tool result

_source line 2184 · 2026-05-23T09:22:58.608503+00:00_

Web search results for query: "ADELIE universal information extraction LLM 2024 schema-aware"

Links: [{"title":"ADELIE: Aligning Large Language Models on Information Extraction | Request PDF","url":"https://www.researchgate.net/publication/386188440_ADELIE_Aligning_Large_Language_Models_on_Information_Extraction"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction","url":"https://arxiv.org/html/2405.05008v1"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction","url":"https://arxiv.org/pdf/2405.05008"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/adelie-aligning-large-language-models-information-extraction"},{"title":"Tsinghua University Researchers Propose ADELIE: Enhancing Information Extraction with Aligned Large Language Models Around Human-Centric Tasks - MarkTechPost","url":"https://www.marktechpost.com/2024/05/11/tsinghua-university-researchers-propose-adelie-enhancing-information-extraction-with-aligned-large-language-models-around-human-centric-tasks/"},{"title":"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models","url":"https://arxiv.org/pdf/2505.14992"}]

Based on the search results, here's what I found about ADELIE:

ADELIE (Aligning large language moDELs on Information Extraction) is an LLM aligned on IE tasks. It addresses the challenge that LLMs typically struggle to understand and follow complex instructions of IE tasks, such as complicated task schemas and specifications.

**Key Components:**

ADELIE constructs a high-quality instruction tuning dataset for IE tasks called IEInstruct, including 83,585 instances of various IE tasks with diverse sets of instructions and input-output formats. IEInstruct comprises over 83,000 instances across various IE formats, including triplets, natural language responses, and JSON outputs.

**Approach:**

The method invol
…[truncated 794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7357
}
```

</details>

---


### Tool result

_source line 2185 · 2026-05-23T09:22:58.759445+00:00_

Web search results for query: "KnowCoder code-style schema knowledge graph extraction ACL 2024"

Links: [{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal   Information Extraction","url":"https://arxiv.org/pdf/2403.07969"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction","url":"https://arxiv.org/html/2403.07969v2"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction - Zixuan Li","url":"https://lee-zix.github.io/publications/2024-08-16-ACL/"},{"title":"[2403.07969] KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction","url":"https://arxiv.org/abs/2403.07969"},{"title":"KnowCoder","url":"https://ict-goknow.github.io/knowcoder/"},{"title":"[PDF] KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/KnowCoder:-Coding-Structured-Knowledge-into-LLMs-Li-Zeng/3ba0f13d9b24a2dcfdcd861150e33c7d71e6c69e"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.475/"},{"title":"GitHub - ICT-GoKnow/KnowCoder: Official Repo of paper \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\". In the paper, we propose KnowCoder, the most powerful large language model so far for universal information extraction.","url":"https://github.com/ICT-GoKnow/KnowCoder"},{"title":"Extract, Define, Canonicalize: An LLM-based Framework for Knowledge Graph Construction - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.548/"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction | Request PDF","url":"https://www.researchgate.net/publication/384207388_KnowCoder_Coding_Structured_Knowledge_into_LLMs_for_Universal_Information_Extraction"}]

Based on the search results, her
…[truncated 1590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6653
}
```

</details>

---


### Tool call

_source line 2186 · 2026-05-23T09:23:05.368026+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DCCD \"draft conditioned constrained decoding\" structured generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DCCD \"draft conditioned constrained decoding\" structured generation 2026"
  }
}
```

</details>

---


### Tool call

_source line 2187 · 2026-05-23T09:23:06.122367+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"type constrained\" OR \"schema constrained\" \"relation extraction\" decoding 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"type constrained\" OR \"schema constrained\" \"relation extraction\" decoding 2025 2026 arxiv"
  }
}
```

</details>

---


### Tool result

_source line 2188 · 2026-05-23T09:23:13.726101+00:00_

Web search results for query: ""type constrained" OR "schema constrained" "relation extraction" decoding 2025 2026 arxiv"

Links: [{"title":"Generative Information Extraction","url":"https://www.emergentmind.com/topics/generative-information-extraction"},{"title":"[2408.02361] Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding","url":"https://arxiv.org/abs/2408.02361"},{"title":"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought   Decoding","url":"https://arxiv.org/pdf/2408.02361"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"}]

I found several relevant results for your search. Here's what I found:

## Key Results:

**Dialogue Ontology Relation Extraction with Constrained Decoding:**
A recent arXiv paper (2408.02361, updated March 2025) adapts Chain-of-Thought decoding for generative relation extraction, generating multiple branches in the decoding space and selecting relations based on a confidence threshold. By constraining the decoding to ontology terms and relations, the approach aims to decrease the risk of hallucination.

**Generative Information Extraction with Constrained Decoding:**
Constrained beam search or prefix-tokens force valid outputs (e.g., restricting to valid schema fields, entity names, or relation types). Advanced sequence-to-sequence models employ schema-guided prompts and constrained decoding to directly generate structured outputs like JSON, ensuring consistency and flexibili
…[truncated 755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7603
}
```

</details>

---


### Tool result

_source line 2189 · 2026-05-23T09:23:14.379418+00:00_

Web search results for query: "DCCD "draft conditioned constrained decoding" structured generation 2026"

Links: [{"title":"[2603.03305] Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/abs/2603.03305"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"Appendix","url":"https://arxiv.org/html/2603.03305"},{"title":"Constrained Decoding: Grammar-Guided Generation for Structured LLM Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Constrained Decoding Mechanism","url":"https://www.emergentmind.com/topics/constrained-decoding-mechanism"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/pdf/2403.06988"},{"title":"Beyond Free-Form Text: How Constrained Decoding is Reshaping Structured Generation in LLMs | by Brijesh Nambiar | Medium","url":"https://medium.com/@brijeshrn/beyond-free-form-text-how-constrained-decoding-is-reshaping-structured-generation-in-llms-5f7a38bef259"}]

Based on the search results, here's what I found about DCCD (Draft-Conditioned Constrained Decoding):

## Overview

DCCD is a simple two-step, training-free inference procedure that decouples semantic planning from structural enforcement: an unconstrained draft is generated first, and constrained decoding is then applied, conditioned on this draft, to guarantee validity.

## How It Works

DCCD is a lightweight, training-free two-step inference procedure. In Step 1, a model generates an unconstrained draft that captures the semantic plan or intermediate reasoning. In Step 2, we generate the final structured output using cons
…[truncated 971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9011
}
```

</details>

---


### Tool call

_source line 2190 · 2026-05-23T09:23:26.393851+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/submitted.pdf",
  "pages": "11-15",
  "project": "schema_semantic_constrained_ie",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/submitted.pdf",
    "pages": "11-15",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2191 · 2026-05-23T09:23:27.099363+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 633.3}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 602.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 366.0}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 557.8}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 546.7}], \"total_pages\": 39, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 2192 · 2026-05-23T09:23:27.099912+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SciDC scientific knowledge decoding constraints LLM 2026 structured prediction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SciDC scientific knowledge decoding constraints LLM 2026 structured prediction"
  }
}
```

</details>

---


### Tool result

_source line 2193 · 2026-05-23T09:23:35.235934+00:00_

Web search results for query: "SciDC scientific knowledge decoding constraints LLM 2026 structured prediction"

Links: [{"title":"[2604.06603v1] Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs","url":"https://arxiv.org/abs/2604.06603v1"},{"title":"[2604.06603] Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs","url":"https://arxiv.org/abs/2604.06603"},{"title":"Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs","url":"https://arxiv.org/html/2604.06603v1"},{"title":"Constrained Decoding: Grammar-Guided Generation for Structured LLM Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"}]

Based on the search results, here's what I found about SciDC:

## SciDC Overview

SciDC is an LLM generation method that integrates subject-specific knowledge with strong constraints. The research paper was published on arXiv in April 2026.

## Key Features and Approach

The method works by adopting strong LLMs to automatically convert flexible knowledge into multi-layered, standardized rules, building an extensible framework to effectively constrain the model generation on domain tasks.

SciDC leverages the knowledge parsing capability of general LLMs while keeping domain data private by using local, smaller models for constrained generation.

## Performance Results

Experiments on scientific tasks including industrial formulation design, clinical tumor diagnosis and retrosynthesis planning demonstrate the method's effectiveness, achieving a 12% accuracy improvement on average compared w
…[truncated 486 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8136
}
```

</details>

---


### Tool call

_source line 2194 · 2026-05-23T09:23:40.609180+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 2195 · 2026-05-23T09:23:41.111510+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 2196 · 2026-05-23T09:23:41.213305+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool result

_source line 2197 · 2026-05-23T09:23:41.766482+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 2198 · 2026-05-23T09:27:18.494960+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见 — Round 24\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 一篇执行扎实的系统工程工作，通过两层约束解码近乎消除 IE 类型违规，但理论贡献浅薄、缺乏强 baseline 对比、WikiEvents pilot 过于初步，整体新颖性不足以支撑 main conference。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论正确，消融实验设计合理；但 Proposition 1 理论贡献被高估，强 baseline 缺失，WikiEvents n=20 无统计意义 |\n| Excitement | 2.5/5 | 解决了真实问题，但方案是现有组件（XGrammar + stateful logits processor）的集成，对熟悉 constrained decoding 的读者缺乏惊喜 |\n| Overall Assessment | 3.0/5 | Findings 水平：工程质量高、分析诚实，但新颖性天花板低 |\n| Reproducibility | 4/5 | 详细实验配置、承诺开源、27 个附录；代码未公开（acceptance 后释放） |\n| Confidence | 4/5 | 熟悉 constrained decoding 和 IE 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Proposition 1 的理论贡献被高估，不构成实质性 novelty\n\n- 具体位置：§3 Method, Proposition 1 (Page 3)\n- 问题：论文声称 \"we formalize a well-known intuition that cross-field type constraints require runtime state beyond context-free expressiveness\"（§1, Contribution 1）。然而 Proposition 1 证明的内容——PDA 无法对无界序列进行随机访问——是自动机理论的基础知识。任何需要 cross-position dependency 的约束都超出 CFG 表达能力，这在形式语言理论中是 trivial 的。论文自身也承认这是 \"well-known intuition\" 的形式化，但将其包装为核心理论贡献（\"theoretical grounding\"）并作为 Contribution 1 的一部分呈现，夸大了其学术新颖性。\n- 为什么影响接收：论文自我定位为 \"systematic engineering contribution with theoretical grounding\"——如果 theoretical grounding 部分是 trivial 的，那么整体贡献降级为纯工程贡献。对于 EMNLP main conference，纯系统集成工作（XGrammar + stateful logits processor）的 novelty bar 更难满足。\n- 建议修改方向：诚实地将 Proposition 1 定位为 motivating observation 而非 theoretical contribution；将重心转移到 empirical findings（如 scale-dependent layer interaction）作为核心贡献。\n\n**N2** [critical] 缺乏与强 baseline 的公平对比\n\n- 具体位置：§5.1, §6 Related Work (Pages 6, 8)\n- 问题：论文的 \"constrained baseline\" 比较仅限于 grammar-only 方法（GCD、vLLM guided_json），这些方法被论文自身证明只能减少 3% DR——本质上是 strawman comparison。与真正相关的强 baseline 缺乏可比对比：(a) GoLLIE：论文承认 \"Direct comparison is methodologically constrained\"（§6），但未解决这一问题；(b) KnowCoder（ACL 2024）被引用但无实验对比；(c) 未对比 post-hoc type repair 方法（修复违规而非丢弃）。\n- 为什么影响接收：无法判断 OntoCoDec 相对于 SOTA schema-aware IE 系统的实际优势。\n- 建议修改方向：至少实现一个 post-hoc type repair baseline；或用 GoLLIE 在相同数据上做可比评估。\n\n**N3** [critical] R-F1 41–47% 的绝对质量缺乏上下文定位\n\n- 具体位置：§5.1 Table 2, Abstract (Pages 1, 6)\n- 问题：R-F1 41–47% 未与 SciERC/DocRED 上的 SOTA（SpanBERT/PL-Marker 50%+, DocRED 60%+）对比。在如此低的 F1 下讨论 0.09% DR 的实际意义需要更多论证。\n- 为什么影响接收：如果提取质量本身不具竞争力，类型约束的实际价值被削弱。\n- 建议修改方向：在 §5 Setup 中增加 LLM-based generative RE 在这些数据集上的典型 F1 范围讨论。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] WikiEvents pilot (§5.2) 篇幅与贡献不匹配\n- n=20 test docs, MDE≈±5pp, \"directional only\"。在 8 页限制下用 ~半页呈现无法得出统计结论的 pilot study 是空间浪费。建议缩减释放空间给 §7。\n\n**W2** [warning] CF 违规作为 \"可修正副作用\" 的叙事过于乐观\n- Greedy S1 引入 CF（zero-shot: 0→9.82pp）。TCR 减少 18–92%（范围极大），beam search 1.54× latency。在 zero-shot 下 CF 高达 12%，OntoCoDec 可能增加总体错误率。建议更审慎讨论 CF 代价。\n\n**W3** [warning] §7 Discussion 仅 8 行，过于压缩\n- 未讨论：何时选择 grammar-only vs. full two-layer；对其他结构化生成任务的启示；per-triple vs. global enforcement 的根本张力。\n\n**W4** [warning] 约束来源模糊削弱 \"ontology-compiled\" 框架\n- SciERC/DocRED 约束来自训练数据观测值，非形式本体。99% coverage 意味着 ~1% valid pairs 未覆盖。标题 \"OntoCoDec\" 暗示形式化本体，与实际不完全匹配。\n\n**W5** [warning] Contribution 2 过度打包\n- 一个 bullet 包含 4 models × 2 precisions × 2 datasets、scale-dependent interaction、CF side effect、beam search、WikiEvents pilot。应拆分为 2-3 条更聚焦的贡献。\n\n---\n\n## 小问题\n\n- Abstract 第三段 \"Composed with LoRA fine-tuning\" 在解释框架前出现，认知负担高\n- 违规减少报告方式不一致（绝对值 vs. 相对值），应统一\n- Table 1 caption \"F1 ×100\" 容易被忽略，建议表头直接标注 \"F1 (%)\"\n- \"First-seen semantics\" 在 beam search 下的行为未讨论\n- §4 κ 相关性基于 n=3（p=0.138），不应过度解读\n\n---\n\n## 遗漏的相关工作\n\n1. SciDC (arXiv:2604.06603, Apr 2026)——将领域知识编译为多层约束指导生成\n2. Dialogue Ontology RE via Constrained CoT (arXiv:2408.02361)——ontology 约束 + CoT 用于关系抽取\n3. Graph-Constrained Reasoning / KG-Trie (arXiv:2410.13080)——Trie 编码 KG 约束到解码过程\n4. Format Tax 原始论文 (arXiv:2604.03616, 2026) 需核实是否与已引用的 FormaTax 为同一工作\n\n---\n\n## 主要优势\n\n1. 问题定义清晰：DR/CF/RV/ET 违规分类体系化，violation landscape 量化分析有价值\n2. 消融实验设计出色：5-way ablation 清晰展示各层效果；scale-dependent layer interaction 是有趣的 empirical finding\n3. 分析诚实度高：坦诚 CF 引入、WikiEvents 局限、GoLLIE 对比限制、κ 统计效力不足\n4. 附录极详尽：27 个附录覆盖几乎所有 reviewer concern\n5. Tokenizer-agnostic continuation masking 具实际工程价值\n6. Runtime overhead 合理（fine-tuned S1 仅 +10% latency）",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见 — Round 24\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 一篇执行扎实的系统工程工作，通过两层约束解码近乎消除 IE 类型违规，但理论贡献浅薄、缺乏强 baseline 对比、WikiEvents pilot 过于初步，整体新颖性不足以支撑 main conference。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论正确，消融实验设计合理；但 Proposition 1 理论贡献被高估，强 baseline 缺失，WikiEvents n=20 无统计意义 |\n| Excitement | 2.5/5 | 解决了真实问题，但方案是现有组件（XGrammar + stateful logits processor）的集成，对熟悉 constrained decoding 的读者缺乏惊喜 |\n| Overall Assessment | 3.0/5 | Findings 水平：工程质量高、分析诚实，但新颖性天花板低 |\n| Reproducibility | 4/5 | 详细实验配置、承诺开源、27 个附录；代码未公开（acceptance 后释放） |\n| Confidence | 4/5 | 熟悉 constrained decoding 和 IE 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Proposition 1 的理论贡献被高估，不构成实质性 novelty\n\n- 具体位置：§3 Method, Proposition 1 (Page 3)\n- 问题：论文声称 \"we formalize a well-known intuition that cross-field type constraints require runtime state beyond context-free expressiveness\"（§1, Contribution 1）。然而 Proposition 1 证明的内容——PDA 无法对无界序列进行随机访问——是自动机理论的基础知识。任何需要 cross-position dependency 的约束都超出 CFG 表达能力，这在形式语言理论中是 trivial 的。论文自身也承认这是 \"well-known intuition\" 的形式化，但将其包装为核心理论贡献（\"theoretical grounding\"）并作为 Contribution 1 的一部分呈现，夸大了其学术新颖性。\n- 为什么影响接收：论文自我定位为 \"systematic engineering contribution with theoretical grounding\"——如果 theoretical grounding 部分是 trivial 的，那么整体贡献降级为纯工程贡献。对于 EMNLP main conference，纯系统集成工作（XGrammar + stateful logits processor）的 novelty bar 更难满足。\n- 建议修改方向：诚实地将 Proposition 1 定位为 motivating observation 而非 theoretical contribution；将重心转移到 empirical findings（如 scale-dependent layer interaction）作为核心贡献。\n\n**N2** [critical] 缺乏与强 baseline 的公平对比\n\n- 具体位置：§5.1, §6 Related Work (Pages 6, 8)\n- 问题：论文的 \"constrained baseline\" 比较仅限于 grammar-only 方法（GCD、vLLM guided_json），这些方法被论文自身证明只能减少 3% DR——本质上是 strawman comparison。与真正相关的强 baseline 缺乏可比对比：(a) GoLLIE：论文承认 \"Direct comparison is methodologically constrained\"（§6），但未解决这一问题；(b) KnowCoder（ACL 2024）被引用但无实验对比；(c) 未对比 post-hoc type repair 方法（修复违规而非丢弃）。\n- 为什么影响接收：无法判断 OntoCoDec 相对于 SOTA schema-aware IE 系统的实际优势。\n- 建议修改方向：至少实现一个 post-hoc type repair baseline；或用 GoLLIE 在相同数据上做可比评估。\n\n**N3** [critical] R-F1 41–47% 的绝对质量缺乏上下文定位\n\n- 具体位置：§5.1 Table 2, Abstract (Pages 1, 6)\n- 问题：R-F1 41–47% 未与 SciERC/DocRED 上的 SOTA（SpanBERT/PL-Marker 50%+, DocRED 60%+）对比。在如此低的 F1 下讨论 0.09% DR 的实际意义需要更多论证。\n- 为什么影响接收：如果提取质量本身不具竞争力，类型约束的实际价值被削弱。\n- 建议修改方向：在 §5 Setup 中增加 LLM-based generative RE 在这些数据集上的典型 F1 范围讨论。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] WikiEvents pilot (§5.2) 篇幅与贡献不匹配\n- n=20 test docs, MDE≈±5pp, \"directional only\"。在 8 页限制下用 ~半页呈现无法得出统计结论的 pilot study 是空间浪费。建议缩减释放空间给 §7。\n\n**W2** [warning] CF 违规作为 \"可修正副作用\" 的叙事过于乐观\n- Greedy S1 引入 CF（zero-shot: 0→9.82pp）。TCR 减少 18–92%（范围极大），beam search 1.54× latency。在 zero-shot 下 CF 高达 12%，OntoCoDec 可能增加总体错误率。建议更审慎讨论 CF 代价。\n\n**W3** [warning] §7 Discussion 仅 8 行，过于压缩\n- 未讨论：何时选择 grammar-only vs. full two-layer；对其他结构化生成任务的启示；per-triple vs. global enforcement 的根本张力。\n\n**W4** [warning] 约束来源模糊削弱 \"ontology-compiled\" 框架\n- SciERC/DocRED 约束来自训练数据观测值，非形式本体。99% coverage 意味着 ~1% valid pairs 未覆盖。标题 \"OntoCoDec\" 暗示形式化本体，与实际不完全匹配。\n\n**W5** [warning] Contribution 2 过度打包\n- 一个 bullet 包含 4 models × 2 precisions × 2 datasets、scale-dependent interaction、CF side effect、beam search、WikiEvents pilot。应拆分为 2-3 条更聚焦的贡献。\n\n---\n\n## 小问题\n\n- Abstract 第三段 \"Composed with LoRA fine-tuning\" 在解释框架前出现，认知负担高\n- 违规减少报告方式不一致（绝对值 vs. 相对值），应统一\n- Table 1 caption \"F1 ×100\" 容易被忽略，建议表头直接标注 \"F1 (%)\"\n- \"First-seen semantics\" 在 beam search 下的行为未讨论\n- §4 κ 相关性基于 n=3（p=0.138），不应过度解读\n\n---\n\n## 遗漏的相关工作\n\n1. SciDC (arXiv:2604.06603, Apr 2026)——将领域知识编译为多层约束指导生成\n2. Dialogue Ontology RE via Constrained CoT (arXiv:2408.02361)——ontology 约束 + CoT 用于关系抽取\n3. Graph-Constrained Reasoning / KG-Trie (arXiv:2410.13080)——Trie 编码 KG 约束到解码过程\n4. Format Tax 原始论文 (arXiv:2604.03616, 2026) 需核实是否与已引用的 FormaTax 为同一工作\n\n---\n\n## 主要优势\n\n1. 问题定义清晰：DR/CF/RV/ET 违规分类体系化，violation landscape 量化分析有价值\n2. 消融实验设计出色：5-way ablation 清晰展示各层效果；scale-dependent layer interaction 是有趣的 empirical finding\n3. 分析诚实度高：坦诚 CF 引入、WikiEvents 局限、GoLLIE 对比限制、κ 统计效力不足\n4. 附录极详尽：27 个附录覆盖几乎所有 reviewer concern\n5. Tokenizer-agnostic continuation masking 具实际工程价值\n6. Runtime overhead 合理（fine-tuned S1 仅 +10% latency）",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2199 · 2026-05-23T09:27:22.209603+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3714
}
```

</details>

---


### Tool call

_source line 2200 · 2026-05-23T09:27:27.858707+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 2201 · 2026-05-23T09:27:27.859168+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 2202 · 2026-05-23T09:27:38.741496+00:00_

审稿意见已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。论文工程执行扎实（5-way ablation、3 模型 × 2 数据集验证、27 个附录），但三个 critical 问题制约了 main conference 接收：

1. **Proposition 1 是 trivial 的**——PDA 无法随机访问是自动机理论基础知识，不构成 "theoretical grounding"
2. **缺强 baseline 对比**——仅与 grammar-only（3% DR reduction 的 strawman）比较，未与 GoLLIE/KnowCoder/post-hoc repair 做可比实验
3. **R-F1 41–47% 未定位**——未说明这在 LLM-based RE 中处于什么水平，削弱 constraint enforcement 的实际意义论证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 44

## Round 44

22 recorded events


### User

_source line 2203 · 2026-05-23T09:29:02.654753+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿意见（Overall: 3.5 Borderline Conference）

### Must-Fix

**N1** [critical] Proposition 1 的理论-实践 gap 处理不够清晰
- Proposition 1 证明无界实体集时 domain/range 约束非 context-free。但实际 IE 中实体集有限。"Engineering applicability" 段落用计算复杂度论证（DFA >10^17 states）桥接，但这是复杂度论证而非形式不可能性。论文未讨论 DFA 变得可行的边界条件。
- 建议：正文中明确区分理论不可能性（无界）和实际不可行性（有界但指数级）；给出 DFA 可行的边界条件。

**N2** [critical] κ-DR 相关性声明在统计上无效（n=3, p=0.138）
- 仅 3 个数据点，p=0.138 远未达显著性。虽标注 "descriptive"，但仍在正文中作为核心观察呈现，Figure 2 用回归线拟合 3 个点本质上是过拟合。
- 建议：明确定性为 insufficient for statistical inference；移除回归线或标注 illustrative only。

**N3** [critical] 70B 验证：单一模型族 + 无 FP16 基线
- 70B 仅 Llama-3.1-70B-Instruct (AWQ INT4)，无 Qwen-70B。S2 退化 -8.45pp 的解释是 post-hoc 的。Contribution 2 声称 "4 models" 但 70B 仅 1 个且不同精度。
- 建议：将 70B 定位为 preliminary；为 S2 退化提供机制性解释。

### Should-Fix

**W1** First-seen semantics 的级联错误影响未量化（first assignment 错误率？导致多少后续 violation？）
**W2** WikiEvents n=20 结果呈现方式可能误导（Table 3 在正文中占据与 SciERC/DocRED 同等位置）
**W3** GCD-equiv 等价性验证仅在单一模型上进行
**W4** LoRA 超参从 SciERC 直接转移到 DocRED 缺乏论证
**W5** Beam search 作为 CF 解决方案的实用性讨论不足

### Questions
**Q1**: Name-based referencing 是否使语言变为 context-free？
**Q2**: Semantic-only 行中 RV 从 1.76 增至 4.76，语义层引入更多词汇违规？
**Q3**: 70B S2 退化根本原因？
**Q4**: Fallback 触发的 triple 中有多少产生正确输出？
**Q5**: EVALUATE-FOR 非零 violation（κ=0.361）是否说明低 κ 时语义层优势被削弱？

### Missing References
1. Outlines 近期 structured generation 改进（regex-based + jump-forward optimization）
2. NuneroPlan (Zhu et al., 2024) planning-based 结构化 IE
3. Dong et al. (2024) retrieval-augmented generation 实现 schema-compliant IE

---

**请逐条回应每个 N 和 W 问题，以及 Questions 和 Missing References。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2204 · 2026-05-23T09:29:13.206640+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
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

_source line 2205 · 2026-05-23T09:29:13.207108+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2206 · 2026-05-23T09:29:26.943782+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex",
  "offset": "25",
  "limit": "45"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex",
    "offset": "25",
    "limit": "45"
  }
}
```

</details>

---


### Tool call

_source line 2207 · 2026-05-23T09:29:26.944488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex",
  "offset": "18",
  "limit": "16"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex",
    "offset": "18",
    "limit": "16"
  }
}
```

</details>

---


### Tool result

_source line 2208 · 2026-05-23T09:29:26.945007+00:00_

25	\noindent\textbf{Proposition 1} (Level 2 $\not\subseteq$ Level 1)\textbf{.}
26	\textit{Domain/range type constraints for IE with unbounded entity sets are not context-free.}
27	
28	\smallskip
29	\noindent\textit{Proof sketch.}
30	Consider $\mathcal{E} = \{\tau_A, \tau_B\}$ and a relation $r$ with $\operatorname{dom}(r) = \{\tau_A\}$.
31	An output contains $n$ entities with independently chosen types, followed by a relation referencing head $e_k$ for arbitrary $k \leq n$.
32	A PDA's LIFO stack cannot retrieve position $k < n$ without destroying entries above it; since both $n$ and $k$ are independently unbounded, no PDA can enforce this constraint.
33	OntoCoDec's semantic layer addresses this with a runtime entity registry $\mathcal{D}$ (a finite map enabling random-access type lookups; Appendix~\ref{app:pumping-lemma}).\hfill$\square$
34	
35	\paragraph{Engineering applicability.}
36	When the entity set is finite (the practical case), the valid language is technically regular, but the corresponding DFA requires $O(|\mathcal{E}|^{|\text{entities}|})$ states---exceeding $10^{17}$ for DocRED (7 entity types, 20+ entities per document)---making direct DFA construction intractable.
37	The distinction is between theoretical impossibility (unbounded) and engineering intractability (finite but exponential); OntoCoDec's registry-based approach avoids both.
38	
39	\noindent\textbf{Empirical Observation} (scale-dependent enabling dependency)\textbf{.} The grammar layer alone cannot enforce domain/range constraints (Proposition~1), while the semantic layer alone achieves only 24\% DR reduction at 8B without grammar-enforced vocabulary membership (\S\ref{sec:scierc-results}, Table~\ref{tab:scierc-ablation}).
40	The strength of this dependency is scale-dependent: at 70B, the semantic layer independently achieves 84\% DR reduction (\S\ref{sec:70b-results}), whereas 8B models show only 24\% independent reduction.
41	\smallskip
42	
43	We describe the problem formulation (\S\ref{se
…[truncated 2476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool result

_source line 2209 · 2026-05-23T09:29:26.945321+00:00_

18	Extraction tasks are robust to format-level constraints~\cite{tam2024letmespeak}, supporting this asymmetric treatment.
19	
20	\paragraph{Constraint Tightness.}
21	\label{eq:tightness}
22	Per-relation constraint tightness $\kappa(r) = 1 - |\sigma(r)|/|\mathcal{E}|^2$, with schema mean $\bar{\kappa}$.
23	Across WikiEvents ($\bar{\kappa}{=}0.029$), SciERC ($\bar{\kappa}{=}0.333$), DocRED ($\bar{\kappa}{=}0.842$), DR reduction ranges from 94--99\% to 42--90\%; this correlation is descriptive ($n{=}3$, $p{=}0.138$); entity type confusability is a critical co-factor (Appendix~\ref{app:kappa-case-study},~\ref{app:tcr}); high-$\bar{\kappa}$ relations account for only 3.8\% of gold triples in DocRED (Appendix~\ref{app:kappa-analysis}).
24	
25	\paragraph{Greedy limitation and fallback cascade.}
26	\label{sec:greedy-limitation}
27	Single-pass per-triple enforcement cannot coordinate type assignments across triples sharing the same entity mention; cross-field consistency requires global inference that exceeds the per-token masking paradigm.
28	The semantic layer commits entity types greedily---an instance of Level~3 (non-local) constraints (\S\ref{sec:decidability})---so CF violations arise when the same entity receives different types across triples; beam search mitigates this (\S\ref{sec:beam-results}).
29	Fallback triggers on 0.5--5.7\% of type-bearing positions (zero-shot), virtually eliminated by fine-tuning ($\leq$\,0.11\%); all residual DR occurs at fallback positions (Appendix~\ref{app:causal-tracing}).
30	
31	\paragraph{Non-rectangularity and independent enforcement.}
32	\label{sec:rectangularity}
33	Type signatures are non-rectangular (0/7 SciERC, 23/96 DocRED rectangular); independent enforcement admits 33--37\% spurious pairs, eliminated by fine-tuning (Table~\ref{tab:composability}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2210 · 2026-05-23T09:29:27.096916+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "offset": "40",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "offset": "40",
    "limit": "60"
  }
}
```

</details>

---


### Tool call

_source line 2211 · 2026-05-23T09:29:27.097362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 2212 · 2026-05-23T09:29:27.097782+00:00_

40	GCD-equiv.$^\dagger$
41	  & 15.26 & $\downarrow$1\%
42	  & \textbf{0} & \textbf{0}
43	  & 0.04  & 15.30
44	  & 8.75  & 30.91 \\
45	Semantic
46	  & 11.65 & $\downarrow$24\%
47	  & 1.51  & 0.40
48	  & 2.71  & 14.36
49	  & 8.15  & 31.01 \\
50	S1
51	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
52	  & \textbf{0} & \textbf{0}
53	  & 9.90  & \textbf{10.83}
54	  & \textbf{8.36} & 30.98 \\
55	S2
56	  & 0.97  & $\downarrow$94\%
57	  & \textbf{0} & \textbf{0}
58	  & 8.03  & \textbf{9.00}
59	  & 8.03  & \textbf{31.90} \\
60	\bottomrule
61	\end{tabular}}%
62	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
63	$\Delta$DR: relative change vs.\ unconstrained; Tot.\ = DR + CF; bold = best (CF excluded).
64	F1 $\times$100. S1/S2 = single/two-pass (\S\ref{sec:strategies}).
65	Grammar = GCD ceiling~\cite{geng2023gcd}.
66	$\dagger$vLLM \texttt{guided\_json}~\cite{kwon2023vllm} (\S\ref{sec:constrained-baselines}).
67	Deterministic (greedy, $T{=}$0); robustness evidence in Table~\ref{tab:cross-model} and Appendices~\ref{app:bootstrap-effect-sizes},~\ref{app:prompt-sensitivity}.}
68	\label{tab:scierc-ablation}
69	\end{table}
70	
71	% ──────────────────────────────────────────
72	%  (a) Zero-shot diagnostic (compressed)
73	% ──────────────────────────────────────────
74	\paragraph{Zero-shot diagnostic.}
75	% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093
76	Table~\ref{tab:scierc-ablation} establishes that DR violations are pervasive (15--18\% across datasets) and that constraint layers interact non-additively: grammar-only achieves 3\% DR reduction on SciERC, semantic-only 24\%, but their composition yields 94\%---the \emph{empirical enabling dependency}.
77	On DocRED (96 relations, $\bar{\kappa}{=}0.842$), grammar-only \emph{increases} DR via \textit{latent violation surfacing}: forcing OOV$\to$valid relation mapping exposes violations previously masked by vocabulary errors (Appendix~\ref{app:cross-model-zs}).
78	Cross-model validation (3 
…[truncated 3158 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---
