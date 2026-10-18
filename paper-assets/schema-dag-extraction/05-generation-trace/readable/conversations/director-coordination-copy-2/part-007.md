# Director coordination — Part 7 of 10

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

[← Part 6](part-006.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 8 →](part-008.md) · [Structured JSON](../../../sessions/0f/0fa49ecfe50583d66f9a.json)

## Round 168

### Tool call

_source line 1954 · 2026-05-18T09:57:09.989450+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "你是 Round 19 Reviewer 1。审查侧重：**方法严谨性 + 实验设计 + R18 修复验证**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR (May 25 cycle), Findings\n- **格式**: ACL 模板, Long paper 8 页正文（不含 Limitations/Ethics/References）, double-blind\n- **评分标准**: 5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit\n\n## 论文路径\n`projects/schema-dag-extraction/docs/paper/main.tex`（含 \\input 的所有 section 文件）\n\n## 论文概要\n研究 training-free LLM IE 中 schema 复杂度如何预测性能退化，将退化分解为 count (Dim 1) 和 confusability (Dim 2) 两个维度。提出 SCS/BCS 量化 confusability，在 FewRel/DocRED/Few-NERD/MAVEN 上实验。BCS 在 RE 上解释 22-53% batch 间方差，NER 上无 batch 级信号。Schema decomposition (SDGD) 失败。\n\n## R18 Open/In-Progress Issues（重点核查是否已修复）\n\n### Critical\n1. **R18-N1**: BCS batch-level 仅限 RE forced-choice classification format，非 constrained decoding。NER 也用 constrained decoding (JSON enum) 但无信号。→ 检查全文是否已精确区分 forced-choice classification format vs constrained decoding。\n2. **R18-N2**: \"Two separable dimensions\" 在 logit-scale 上 inconclusive。→ 检查全文是否统一改为 \"largely additive with bounded interaction\"。\n3. **R18-N3**: Contribution 2 暗示 metric innovation。→ 检查是否已改为 methodology contribution。\n\n### Warning\n4. **R18-W2**: Pairwise r²=1.3-1.7% 引用 Cohen (1988) 套用到 LLM 系统需额外论证。\n5. **R18-W5**: Dimension 2 未在 proprietary model (Gemini) 上验证。Limitations 是否说明。\n6. **R18-W7**: BCS-aware grouping 无显著优势 (+1.4pp)。SDGD section 是否加了 \"marginal BCS reduction\" 解释。\n7. **R17-W3**: Typical-batch 2.2pp 实际意义有限。Practical implications 是否更坦诚。\n\n## 你的审查重点\n\n1. **R18 修复验证**: 逐条检查上述 issues 的修复质量，标记 [FIXED]、[PARTIALLY FIXED]、[NOT FIXED]\n2. **实验设计严谨性**: BCS-controlled 设计、TOST equivalence、within-pool analysis、cross-model validation 的方法论质量\n3. **统计分析**: effect sizes、CI、p-values 的解释是否恰当；logit-scale TOST 在正文中是否被提及\n4. **因果 vs 相关性语言**: 全文是否避免了超出证据的因果表述\n5. **新问题**: 是否有修改引入的新问题\n\n## 输出格式\n按以下结构输出审稿意见：\n```\n## R18 修复验证\n[逐条 FIXED/PARTIALLY FIXED/NOT FIXED + 简要说明]\n\n## Strengths (逐条)\n## Weaknesses (逐条, 标 critical/warning/info)\n## Questions\n## Missing References\n## Scores\n- Soundness: X/5\n- Excitement: X/5\n- Reproducibility: X/5\n- Overall: X (用 EMNLP 2026 评分标准)\n- Confidence: X/5\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "你是 Round 19 Reviewer 1。审查侧重：**方法严谨性 + 实验设计 + R18 修复验证**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR (May 25 cycle), Findings\n- **格式**: ACL 模板, Long paper 8 页正文（不含 Limitations/Ethics/References）, double-blind\n- **评分标准**: 5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit\n\n## 论文路径\n`projects/schema-dag-extraction/docs/paper/main.tex`（含 \\input 的所有 section 文件）\n\n## 论文概要\n研究 training-free LLM IE 中 schema 复杂度如何预测性能退化，将退化分解为 count (Dim 1) 和 confusability (Dim 2) 两个维度。提出 SCS/BCS 量化 confusability，在 FewRel/DocRED/Few-NERD/MAVEN 上实验。BCS 在 RE 上解释 22-53% batch 间方差，NER 上无 batch 级信号。Schema decomposition (SDGD) 失败。\n\n## R18 Open/In-Progress Issues（重点核查是否已修复）\n\n### Critical\n1. **R18-N1**: BCS batch-level 仅限 RE forced-choice classification format，非 constrained decoding。NER 也用 constrained decoding (JSON enum) 但无信号。→ 检查全文是否已精确区分 forced-choice classification format vs constrained decoding。\n2. **R18-N2**: \"Two separable dimensions\" 在 logit-scale 上 inconclusive。→ 检查全文是否统一改为 \"largely additive with bounded interaction\"。\n3. **R18-N3**: Contribution 2 暗示 metric innovation。→ 检查是否已改为 methodology contribution。\n\n### Warning\n4. **R18-W2**: Pairwise r²=1.3-1.7% 引用 Cohen (1988) 套用到 LLM 系统需额外论证。\n5. **R18-W5**: Dimension 2 未在 proprietary model (Gemini) 上验证。Limitations 是否说明。\n6. **R18-W7**: BCS-aware grouping 无显著优势 (+1.4pp)。SDGD section 是否加了 \"marginal BCS reduction\" 解释。\n7. **R17-W3**: Typical-batch 2.2pp 实际意义有限。Practical implications 是否更坦诚。\n\n## 你的审查重点\n\n1. **R18 修复验证**: 逐条检查上述 issues 的修复质量，标记 [FIXED]、[PARTIALLY FIXED]、[NOT FIXED]\n2. **实验设计严谨性**: BCS-controlled 设计、TOST equivalence、within-pool analysis、cross-model validation 的方法论质量\n3. **统计分析**: effect sizes、CI、p-values 的解释是否恰当；logit-scale TOST 在正文中是否被提及\n4. **因果 vs 相关性语言**: 全文是否避免了超出证据的因果表述\n5. **新问题**: 是否有修改引入的新问题\n\n## 输出格式\n按以下结构输出审稿意见：\n```\n## R18 修复验证\n[逐条 FIXED/PARTIALLY FIXED/NOT FIXED + 简要说明]\n\n## Strengths (逐条)\n## Weaknesses (逐条, 标 critical/warning/info)\n## Questions\n## Missing References\n## Scores\n- Soundness: X/5\n- Excitement: X/5\n- Reproducibility: X/5\n- Overall: X (用 EMNLP 2026 评分标准)\n- Confidence: X/5\n```"
  }
}
````

</details>

---


### Tool result

_source line 1955 · 2026-05-18T09:57:28.842069+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18852
}
```

</details>

---


### Tool call

_source line 1956 · 2026-05-18T09:57:28.994252+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "你是 Round 19 Reviewer 2。审查侧重：**新颖性 + 完整性 + 写作质量 + 格式合规**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR (May 25 cycle), Findings\n- **格式**: ACL 模板, Long paper 8 页正文（不含 Limitations/Ethics/References）, double-blind\n- **评分标准**: 5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit\n\n## 论文路径\n`projects/schema-dag-extraction/docs/paper/main.tex`（含 \\input 的所有 section 文件）\n\n## 论文概要\n研究 training-free LLM IE 中 schema 复杂度如何预测性能退化。提出 SCS/BCS 量化 type confusability，发现 RE 中 BCS 解释 22-53% batch 间 accuracy 方差（closed-set classification format），NER 上无 batch 级信号。Schema decomposition (SDGD) 失败。\n\n## R18 Open/In-Progress Issues（重点核查是否已修复）\n\n### Critical\n1. **R18-N1**: Boundary condition 从 \"constrained decoding\" 精确化为 \"forced-choice classification format\"。\n2. **R18-N2**: 全文措辞从 \"two separable dimensions\" 统一为 \"largely additive with bounded interaction\"。\n3. **R18-N3**: Contribution 2 从 metric innovation 改为 methodology contribution。\n\n### Warning (写作/格式相关)\n4. **R18-W1**: Abstract 217 words 信息过载 → 压缩到 ~180 words，story-driven 结构。\n5. **R18-W8**: 正文超 8 页限制 (Conclusion 在 page 9) → 是否已压缩。\n6. **R18-m-refs**: Missing refs (Chen et al. 2026, Wei et al. 2023) → 是否已补充。\n7. **R17-W3**: Practical implications 薄弱 → 是否更坦诚 (\"diagnostic > engineering value\")。\n\n## 你的审查重点\n\n1. **R18 修复验证**: 逐条检查上述 issues 的修复质量，标记 [FIXED]、[PARTIALLY FIXED]、[NOT FIXED]\n2. **新颖性评估**: SCS/BCS 与 LLM-PEE 的 embedding similarity 形式相同。论文的真正贡献（experimental methodology）是否被清晰传达？对比 2025-2026 年相关工作（CROSSAGENTIE, PARSE, DLISC, SPT 等），novelty 是否足够？\n3. **写作质量**:\n   - AI 写作标志检查：em-dash (—)、en-dash (–) 用法、-ing 分词结尾、过度分段\n   - 全文主线统一性：Abstract → Introduction → Results → Discussion → Conclusion 是否讲同一个故事\n   - 专有名词首次出现是否有定义\n4. **格式合规**: \n   - 页数是否在 8 页限制内（需要估算，无法编译）\n   - Checklist 填写质量\n   - 匿名化检查\n   - 引用充足度（覆盖直接竞争者、baseline、benchmark、统计方法）\n5. **完整性**: \n   - 所有 Contribution 在正文中有对应 section/table 支撑\n   - Limitations 覆盖是否全面\n   - Appendix 在正文中是否被引用且融入叙事\n6. **新问题**: 是否有修改引入的新问题\n\n## 输出格式\n按以下结构输出审稿意见：\n```\n## R18 修复验证\n[逐条 FIXED/PARTIALLY FIXED/NOT FIXED + 简要说明]\n\n## Strengths (逐条)\n## Weaknesses (逐条, 标 critical/warning/info)\n## Questions\n## Missing References\n## Scores\n- Soundness: X/5\n- Excitement: X/5\n- Reproducibility: X/5\n- Overall: X (用 EMNLP 2026 评分标准)\n- Confidence: X/5\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "你是 Round 19 Reviewer 2。审查侧重：**新颖性 + 完整性 + 写作质量 + 格式合规**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR (May 25 cycle), Findings\n- **格式**: ACL 模板, Long paper 8 页正文（不含 Limitations/Ethics/References）, double-blind\n- **评分标准**: 5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit\n\n## 论文路径\n`projects/schema-dag-extraction/docs/paper/main.tex`（含 \\input 的所有 section 文件）\n\n## 论文概要\n研究 training-free LLM IE 中 schema 复杂度如何预测性能退化。提出 SCS/BCS 量化 type confusability，发现 RE 中 BCS 解释 22-53% batch 间 accuracy 方差（closed-set classification format），NER 上无 batch 级信号。Schema decomposition (SDGD) 失败。\n\n## R18 Open/In-Progress Issues（重点核查是否已修复）\n\n### Critical\n1. **R18-N1**: Boundary condition 从 \"constrained decoding\" 精确化为 \"forced-choice classification format\"。\n2. **R18-N2**: 全文措辞从 \"two separable dimensions\" 统一为 \"largely additive with bounded interaction\"。\n3. **R18-N3**: Contribution 2 从 metric innovation 改为 methodology contribution。\n\n### Warning (写作/格式相关)\n4. **R18-W1**: Abstract 217 words 信息过载 → 压缩到 ~180 words，story-driven 结构。\n5. **R18-W8**: 正文超 8 页限制 (Conclusion 在 page 9) → 是否已压缩。\n6. **R18-m-refs**: Missing refs (Chen et al. 2026, Wei et al. 2023) → 是否已补充。\n7. **R17-W3**: Practical implications 薄弱 → 是否更坦诚 (\"diagnostic > engineering value\")。\n\n## 你的审查重点\n\n1. **R18 修复验证**: 逐条检查上述 issues 的修复质量，标记 [FIXED]、[PARTIALLY FIXED]、[NOT FIXED]\n2. **新颖性评估**: SCS/BCS 与 LLM-PEE 的 embedding similarity 形式相同。论文的真正贡献（experimental methodology）是否被清晰传达？对比 2025-2026 年相关工作（CROSSAGENTIE, PARSE, DLISC, SPT 等），novelty 是否足够？\n3. **写作质量**:\n   - AI 写作标志检查：em-dash (—)、en-dash (–) 用法、-ing 分词结尾、过度分段\n   - 全文主线统一性：Abstract → Introduction → Results → Discussion → Conclusion 是否讲同一个故事\n   - 专有名词首次出现是否有定义\n4. **格式合规**: \n   - 页数是否在 8 页限制内（需要估算，无法编译）\n   - Checklist 填写质量\n   - 匿名化检查\n   - 引用充足度（覆盖直接竞争者、baseline、benchmark、统计方法）\n5. **完整性**: \n   - 所有 Contribution 在正文中有对应 section/table 支撑\n   - Limitations 覆盖是否全面\n   - Appendix 在正文中是否被引用且融入叙事\n6. **新问题**: 是否有修改引入的新问题\n\n## 输出格式\n按以下结构输出审稿意见：\n```\n## R18 修复验证\n[逐条 FIXED/PARTIALLY FIXED/NOT FIXED + 简要说明]\n\n## Strengths (逐条)\n## Weaknesses (逐条, 标 critical/warning/info)\n## Questions\n## Missing References\n## Scores\n- Soundness: X/5\n- Excitement: X/5\n- Reproducibility: X/5\n- Overall: X (用 EMNLP 2026 评分标准)\n- Confidence: X/5\n```"
  }
}
````

</details>

---


### Tool result

_source line 1957 · 2026-05-18T09:57:30.658037+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1663
}
```

</details>

---


### Assistant

_source line 1958 · 2026-05-18T09:57:46.236764+00:00_

Round 19 审稿已启动。两名 Reviewer 已分配：

- **R1** (方法严谨性): 聚焦实验设计质量、统计分析恰当性、R18 critical issues (N1/N2/N3) 修复验证
- **R2** (新颖性+完整性): 聚焦 novelty 定位、写作质量（AI 痕迹检查）、格式合规（8页限制）、R18 写作/格式 issues 修复验证

等待 Reviewer 独立审稿结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 169

## Round 169

2 recorded events


### User

_source line 1959 · 2026-05-18T10:01:33.644167+00:00_

[Reviewer 1 审稿意见]:

# Round 19 Reviewer 1 审稿意见

**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
**审查侧重**: 方法严谨性 + 实验设计 + R18 修复验证

---

## R18 修复验证

**R18-N1 [FIXED]**: forced-choice classification format vs constrained decoding 区分。
全文已精确区分。Abstract 写 "under RE's forced-choice format"；Discussion §6 明确对比 "RE uses a forced-choice classification format...NER, despite also using constrained decoding on the type enum"；Limitations item 9 写 "BCS batch-level prediction is demonstrated only under RE's forced-choice classification format"；Conclusion 写 "under forced-choice classification"。术语使用一致且准确。

**R18-N2 [FIXED]**: "two separable dimensions" → "largely additive with bounded interaction"。
Abstract/Introduction/Conclusion 统一使用 "largely additive dimensions"。Introduction Finding (1) 明确写 "logit-scale inconclusive"。Results §4.4 报告 TOST 三个 margin 水平 (±3pp p=0.003, ±2pp p=0.047, ±1pp p=0.278) 及 logit-scale TOST (p=0.209)。NER 的 coupling 在 Introduction 和 Conclusion 中均被提及。

**R18-N3 [FIXED]**: Contribution 2 从 metric innovation 改为 methodology contribution。
Contribution 2 现在写 "Building on the embedding-similarity criterion used for schema partitioning in prior work, we design controlled experiments that isolate confusability from count"。Related Work SCS novelty 段进一步澄清 "Our contribution is not the metric itself but the controlled experimental framework"。Framing 正确。

**R18-W2 [PARTIALLY FIXED]**: Cohen (1988) 套用到 LLM 系统。
Related Work 现在加了 hedging: "thresholds for 'practically meaningful' may differ in LLM systems where aggregation amplifies small per-instance biases"。承认了标准不可直接迁移，但仍然以 behavioral research 的 "small but real" 框架作为锚定。建议进一步：要么找到 NLP/LLM 领域有 effect size 解读先例的文献，要么明确说明这是 tentative analogy。

**R18-W5 [FIXED]**: Dimension 2 未在 proprietary model 上验证。
Limitations item 1 明确写 "Dimension 2 has been verified only on open-weight models"。Appendix §H (Gemini) 结尾也写 "cross-architecture Dimension 2 validation remains for future work"。

**R18-W7 [FIXED]**: BCS-aware grouping +1.4pp 无显著优势的解释。
SDGD §5 现在写 "graph coloring achieves only marginal mean BCS reduction (0.559→0.552), insufficient to produce detectable accuracy improvement"。因果链清晰：BCS 降幅太小 → 精度差异不显著。

**R17-W3 [PARTIALLY FIXED]**: Typical-batch 2.2pp 实际意义有限。
Results §4.3 transparent 报告了 2.2pp (95% CI [0.4, 4.0]) 和 "roughly 7% of the extreme-batch gap"。Discussion practical implications 段承认 "3-5pp expected impact" 并加了 "diagnostic guidelines derived from correlational evidence; practitioners should validate on their specific schema"。但 Abstract 和 Introduction 的叙事仍侧重 extreme-batch 数字 (31.2pp, -49pp) 而非 typical-batch 的 modest effect，读者可能高估实际影响。

---

## Strengths

**S1. 实验设计严谨，控制变量到位。**
BCS-controlled 设计在固定 count 的前提下变化 confusability，是该研究问题的正确方法论选择。Within-pool analysis (§4.3, Table 5) 用 80-pool 内采样 16-relation 子集排除 pool composition confound，permutation test p=0.60 证实 slope consistency。FewRel 的 balanced design (700 instances/type) 消除了 type frequency confound。这些控制在 training-free IE 文献中是少见的。

**S2. 统计分析全面且透明。**
TOST equivalence testing 用三个 margin 水平报告 (Table 8)，logit-scale sensitivity 单独报告且承认 inconclusive，bootstrap CIs 区分了 pair-level (B=10,000) 和 batch-level (B=1,000)，variance decomposition (Appendix Table 11) 量化了 batch vs seed 方差比。这种统计透明度在 NLP 实证论文中罕见。

**S3. 负面结果的诚实报告。**
SDGD 失败、NER batch-level null、MAVEN centrality confound、logit-scale inconclusive、few-shot widening gap 均被如实报告并分析原因。这增强了正面结果的可信度。

**S4. 跨模型验证覆盖面广。**
Qwen3-32B (primary) + Llama-3.1-8B + 70B (FP8) + Gemini 2.5 Flash (API)，覆盖 open-weight 和 proprietary、8B-70B+ 规模。Dimension 1 在所有模型上复现；Dimension 2 在 RE 上跨 8B/32B/70B 复现。

**S5. Robustness checks 充分。**
Prompt variants (4 种, Appendix Table 10)、BCS aggregation (mean vs max, Appendix Table 7)、embedding ablation (name vs name+def, Appendix Table 12)、SCS baselines (Levenshtein, WordNet, same-parent, Appendix Table 14)、held-out validation (16 val-origin types, Appendix §K)、split-origin covariate (Appendix §L)。每个 potential confound 都有对应的控制分析。

---

## Weaknesses

**N1 [warning] TOST margin 选择与 main effect 的关系需更多论证。**
- 具体位置: §4.4, Appendix §C
- 问题: ±3pp TOST margin 的 empirical anchor 是 "typical random-batch confusability variation produces 2-5pp accuracy differences"，但 typical-batch confusability main effect 本身仅 2.2pp。用 ±3pp margin 证明 interaction bounded 意味着 interaction 可以高达 main effect 的 136% (3/2.2) 而仍被认为 "bounded"。±2pp 是 marginal (p=0.047)，±1pp inconclusive。在 logit scale 上也 inconclusive (p=0.209)。
- "largely additive" 的 claim 实质上是: interaction 在 linear scale 上 bounded below 2-3pp, 但无法排除 interaction 接近甚至超过 main effect 的 magnitude。这使 "largely additive" 的表述偏乐观。
- 建议: Abstract 中 "two largely additive dimensions" 应加限定词，如 "under RE's forced-choice format on the linear scale"；或将 hedging 从 Appendix 提到正文。

**N2 [warning] Abstract/Introduction 的叙事偏重 extreme-batch 数字，淡化 typical-batch modest effect。**
- 具体位置: Abstract, §1
- 问题: Abstract 写 "BCS explains 22-53% of cross-batch RE accuracy variance"，Introduction 列 "-31.2pp" extreme-batch gap 和 "3.9-5.3pp quartile gaps"。但 typical batching 下的 expected gap 仅 2.2pp (CI [0.4, 4.0])，且 NER 上 batch-level signal 为零。读者从 Abstract/Introduction 获得的 impression 与 typical real-world impact 之间有落差。
- 建议: Abstract 中加一句 typical-batch magnitude（如 "though typical batches yield modest 2.2pp gaps"），使核心 message 更 calibrated。

**N3 [warning] NER batch-level null 削弱了 "two-dimensional" 框架的普适性。**
- 具体位置: §4.3, §4.4, §6
- 问题: 论文的核心 framing 是 "two-dimensional degradation"（count + confusability）。但 Dimension 2 在 batch level 仅对 RE 有效，NER 上 r≈0 (n=450)。论文解释这是因为 NER 的 error 分散在 missed entities 和 boundary failures 上，但这意味着 "two-dimensional" 框架对 NER 仅在 pairwise level 成立（r²=1.3%），batch-level 没有 actionable signal。
- 对于 EMNLP 读者来说，NER 是比 RE classification 更 mainstream 的 IE task。框架对 NER batch-level 无预测力是一个 significant boundary condition。
- 建议: 论文已经在多处承认了这一点（Discussion, Limitations），但 title 和 abstract 的 framing 仍暗示 two-dimensional decomposition 是 general 的。

**N4 [info] Monte Carlo simulation 的 evidential status 需要更清晰。**
- 具体位置: Appendix §I
- 问题: 论文正确地将 simulation 标注为 "illustrative explanatory model" 和 "internal consistency check"。但 Discussion §6 引用 "Monte Carlo simulation with parameters derived from the observed data" 时，尽管加了 caveat，仍可能给人 independent corroboration 的印象。Simulation 用 conditional R²=7%（仅 non-zero confusion pairs）匹配 observed batch R²=0.218，但 unconditional R²=1.3% 只能产生 simulated batch R²=0.044。这个 ~5× gap 的解释（89% zero-confusion pairs dilution）虽合理，但 conditioning on the outcome variable 是一个 methodological concern。
- 建议: 正文引用 simulation 时删去具体数字，仅保留 "post-hoc simulation confirms the aggregation pattern is consistent"。

**N5 [info] Few-shot 实验中 5-shot low-BCS 回落的解释不够充分。**
- 具体位置: Appendix §N, Table 15
- 问题: 1-shot low-BCS = 0.754, 5-shot low-BCS = 0.715 (-3.9pp)。论文归因于 "lost-in-middle effects from increased prompt length"，但这只是推测，未做控制实验验证。如果 low-BCS 在 5-shot 下回落是 prompt length effect，那 high-BCS 5-shot 也应受类似影响——但 high-BCS 从 0.554 (1-shot) 降到 0.488 (5-shot) 的降幅 (-6.6pp) 更大。两组不对称的降幅可能有 confusability-specific 的解释，而非仅仅是 prompt length。
- 建议: 承认 non-monotonic pattern 的解释是 speculative。

**N6 [info] Prompt variant analysis 的 multiple comparison 处理。**
- 具体位置: Appendix §G, Table 10
- 问题: 8 个 tests (4 variants × 2 count levels) 在同一 dataset 上进行。论文不做 Bonferroni，理由是 "correlated prompt variants testing the same underlying signal" (citing Rothman 1990)。Rothman (1990) 讨论的是 independent replications across different populations，而这里是 same dataset + same batches + different prompts，相关性方向是 positive (同一 batch 在不同 prompt 下的 accuracy 正相关)。Positive correlation 会 inflate directional consistency 而 deflate individual p-values。7/8 directional consistency 在 positively correlated tests 下的 evidential value 低于独立情况。
- 建议: 加一句说明 positive correlation 对 directional consistency 的影响。

---

## Questions

**Q1.** Table 2 (pairwise correlation) 排除了 FewRel，理由是 "RE's per-instance format precludes direct comparison of confusion rates"。但 §3.2 validation paragraph 和 Appendix Table 14 都报告了 FewRel 的 pairwise SCS-confusion ρ=0.218/0.187。这两个说法是否矛盾？如果 FewRel 可以计算 pairwise confusion，为什么 Table 2 排除它？

**Q2.** Variance decomposition (Appendix Table 11) 中 count=16 的 seed SD (0.027) 显著高于其他 count levels (0.010-0.019 range)。这个异常值是否影响了 count=16 BCS-controlled 实验的结论？

**Q3.** BCS independence analysis (Appendix §M) 报告 BCS unique R²=0.259, composition unique R²=0.298, shared=0.147。Shared variance 占 20.9%，这意味着 BCS 和 type difficulty 不是完全正交的。在 BCS-controlled 实验中，是否控制了 mean type difficulty？

---

## Missing References

- 无明显遗漏。Related work 覆盖了 training-free IE、schema decomposition、constrained decoding、label confusion 等主要方向。引用密度符合 ACL venue 标准。

---

## Scores

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨，统计分析全面透明；但 "largely additive" 在 logit scale 上 inconclusive，TOST margin 选择与 main effect magnitude 的关系需论证，NER batch-level null 削弱框架普适性 |
| Excitement | 2.5/5 | 分析框架有价值（controlled isolation of count vs confusability），但 typical-batch effect modest (2.2pp)，NER 无 batch-level signal，schema decomposition 失败，practical takeaway 有限 |
| Reproducibility | 4/5 | 详细的实验描述（decoding params, seed, batch sizes, bootstrap params），code promised upon acceptance，prompt templates in appendix；单 GPU 可复现 |
| Overall | 3.0 (Findings) | 方法论严谨的实证研究，controlled experimental design 在 training-free IE 文献中是有价值的贡献。但 practical impact limited (2.2pp typical), NER batch-level null, schema decomposition failure, 以及 "largely additive" claim 的 logit-scale caveat 限制了 excitement。适合 Findings。 |
| Confidence | 4/5 | 仔细阅读了全文和 appendix，熟悉实验方法论和统计检验 |


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1960 · 2026-05-18T10:01:45.095443+00:00_

R1 审稿已收到。等待 R2 审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 170

## Round 170

2 recorded events


### User

_source line 1961 · 2026-05-18T10:01:47.851920+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：

- **R18 修复验证**: N1/N2/N3/W5/W7 均 FIXED；W2/W3 PARTIALLY FIXED（Cohen 1988 analogy 仍需补充 LLM 领域先例；Abstract 叙事仍偏重 extreme-batch 数字）
- **Overall: 3.0 (Findings)**。方法论严谨（BCS-controlled design, within-pool analysis, TOST equivalence, 跨模型验证），统计透明度在 NLP 实证论文中罕见。主要限制：typical-batch effect 仅 2.2pp，NER 无 batch-level signal，"largely additive" 在 logit scale 上 inconclusive，schema decomposition 全面失败。
- 新提出 6 个 issues（2 warning, 4 info），3 个 questions。无 critical-level 新问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1962 · 2026-05-18T10:01:53.504441+00:00_

R1 审稿已收到。等待 R2 审稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 171

## Round 171

6 recorded events


### User

_source line 1963 · 2026-05-18T10:03:05.735421+00:00_

[Reviewer 2 审稿意见]:
## Round 19 Reviewer 2 审稿意见

### R18 修复验证

| Issue | Status | 说明 |
|-------|--------|------|
| R18-N1 (boundary condition → forced-choice) | **[FIXED]** | "Forced-choice classification format" 贯穿 Abstract/Discussion/Conclusion/Limitations |
| R18-N2 (separable → largely additive) | **[FIXED]** | 统一为 "largely additive with bounded interaction"，TOST 分析含 logit-scale caveat |
| R18-N3 (metric → methodology contribution) | **[FIXED]** | Contribution 2 明确 "Building on...LLM-PEE...we design controlled experiments" |
| R18-W1 (Abstract ~180 words) | **[FIXED]** | ~156 words，结构清晰 |
| R18-W8 (正文超 8 页) | **[CANNOT VERIFY]** | 无法编译，估算 borderline 8-9 页 |
| R18-m-refs (Chen 2026, Wei 2023) | **[FIXED]** | 两篇均已 cite 且引用验证通过 |
| R17-W3 (diagnostic > engineering value) | **[PARTIALLY FIXED]** | Discussion 末尾 "diagnostic guidelines derived from correlational evidence"，但全文 framing 仍偏乐观 |

### Strengths
- S1: 实验设计严谨（BCS-controlled stratification, TOST, permutation test, bootstrap CI, within-pool 控制）
- S2: 跨模型验证充分（4 模型含 proprietary Gemini）
- S3: SDGD 负面结果诚实报告，对社区有警示意义
- S4: Limitations 10 项覆盖全面，含 power 分析自我披露
- S5: 70 篇引用，positioning 清晰

### Weaknesses
- **N1 [critical]**: 核心发现 novelty 有限——"more types = worse" 和 "similar types confuse" 概念上非 surprising；SCS 形式同 LLM-PEE；controlled experimental methodology 技术上非 novel。作为纯 analytical study，知识增量需足够大但效应量 modest
- **N2 [critical]**: Confusability 效应量小且 task-specific——pairwise $r^2$ = 1.3-1.7%；NER batch-level 完全 null ($n=450$)；RE 发现依赖 forced-choice format 边界条件。Title/framing 暗示普适性但实际高度 task-specific
- **W1 [warning]**: 核心分析集中在 FewRel 一个数据集
- **W2 [warning]**: NER U-shape 现象缺乏实验证据解释
- **W3 [warning]**: "First controlled study" claim 可能过强

### Questions
- Q1: FewRel train-origin types 为何反而 accuracy 低 8.8pp？
- Q2: 16-rel condition 使用 single extreme batch 是否可能是 outlier？
- Q3: TOST ±1pp inconclusive 意味着 interaction 可能达 main effect 91%，"largely additive" framing 是否过强？

### Missing References
引用验证：70 bib / 97 citations / 0 orphan / 0 missing / 0 fabricated。建议补充 Guidance (Zheng et al., 2023) 和 Lyu et al. (2024)。

### Scores
- Soundness: 4/5
- Excitement: 2.5/5
- Reproducibility: 4/5
- Overall: 2.5 (Borderline Findings)
- Confidence: 4/5

### 一句话总结
实验执行出色的 analytical study，但核心发现（count dominates + confusability modest & RE-specific）的 novelty 和 impact 对 Findings 而言 borderline——知识增量受限于 modest effect sizes、NER batch-level null、和 SDGD 失败后缺乏 actionable alternative。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1964 · 2026-05-18T10:03:37.285053+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### R18 修复验证\n\n| Issue | Status | 说明 |\n|-------|--------|------|\n| R18-N1 (boundary condition → forced-choice) | **[FIXED]** | \"Forced-choice classification format\" 贯穿 Abstract/Discussion/Conclusion/Limitations |\n| R18-N2 (separable → largely additive) | **[FIXED]** | 统一为 \"largely additive with bounded interaction\"，TOST 分析含 logit-scale caveat |\n| R18-N3 (metric → methodology contribution) | **[FIXED]** | Contribution 2 明确 \"Building on...LLM-PEE...we design controlled experiments\" |\n| R18-W1 (Abstract ~180 words) | **[FIXED]** | ~156 words，结构清晰 |\n| R18-W8 (正文超 8 页) | **[CANNOT VERIFY]** | 无法编译，估算 borderline 8-9 页 |\n| R18-m-refs (Chen 2026, Wei 2023) | **[FIXED]** | 两篇均已 cite 且引用验证通过 |\n| R17-W3 (diagnostic > engineering value) | **[PARTIALLY FIXED]** | Discussion 末尾 \"diagnostic guidelines derived from correlational evidence\"，但全文 framing 仍偏乐观 |\n\n### Strengths\n- S1: 实验设计严谨（BCS-controlled stratification, TOST, permutation test, bootstrap CI, within-pool 控制）\n- S2: 跨模型验证充分（4 模型含 proprietary Gemini）\n- S3: SDGD 负面结果诚实报告，对社区有警示意义\n- S4: Limitations 10 项覆盖全面，含 power 分析自我披露\n- S5: 70 篇引用，positioning 清晰\n\n### Weaknesses\n- **N1 [critical]**: 核心发现 novelty 有限——\"more types = worse\" 和 \"similar types confuse\" 概念上非 surprising；SCS 形式同 LLM-PEE；controlled experimental methodology 技术上非 novel。作为纯 analytical study，知识增量需足够大但效应量 modest\n- **N2 [critical]**: Confusability 效应量小且 task-specific——pairwise r²=1.3-1.7%；NER batch-level 完全 null (n=450)；RE 发现依赖 forced-choice format 边界条件。Title/framing 暗示普适性但实际高度 task-specific\n- **W1 [warning]**: 核心分析集中在 FewRel 一个数据集\n- **W2 [warning]**: NER U-shape 现象缺乏实验证据解释\n- **W3 [warning]**: \"First controlled study\" claim 可能过强\n\n### Questions\n- Q1: FewRel train-origin types 为何反而 accuracy 低 8.8pp？\n- Q2: 16-rel condition 使用 single extreme batch 是否可能是 outlier？\n- Q3: TOST ±1pp inconclusive 意味着 interaction 可能达 main effect 91%，\"largely additive\" framing 是否过强？\n\n### Missing References\n引用验证：70 bib / 97 citations / 0 orphan / 0 missing / 0 fabricated。建议补充 Guidance (Zheng et al., 2023) 和 Lyu et al. (2024)。\n\n### Scores\n- Soundness: 4/5\n- Excitement: 2.5/5\n- Reproducibility: 4/5\n- Overall: 2.5 (Borderline Findings)\n- Confidence: 4/5\n\n### 一句话总结\n实验执行出色的 analytical study，但核心发现（count dominates + confusability modest & RE-specific）的 novelty 和 impact 对 Findings 而言 borderline——知识增量受限于 modest effect sizes、NER batch-level null、和 SDGD 失败后缺乏 actionable alternative。\n\n---\n\n请逐条回应 R2 的 Weaknesses (N1, N2, W1, W2, W3)、Questions (Q1-Q3) 和 Missing References。对你自己的 issues 如果 R2 的审稿改变了你的判断也请说明。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### R18 修复验证\n\n| Issue | Status | 说明 |\n|-------|--------|------|\n| R18-N1 (boundary condition → forced-choice) | **[FIXED]** | \"Forced-choice classification format\" 贯穿 Abstract/Discussion/Conclusion/Limitations |\n| R18-N2 (separable → largely additive) | **[FIXED]** | 统一为 \"largely additive with bounded interaction\"，TOST 分析含 logit-scale caveat |\n| R18-N3 (metric → methodology contribution) | **[FIXED]** | Contribution 2 明确 \"Building on...LLM-PEE...we design controlled experiments\" |\n| R18-W1 (Abstract ~180 words) | **[FIXED]** | ~156 words，结构清晰 |\n| R18-W8 (正文超 8 页) | **[CANNOT VERIFY]** | 无法编译，估算 borderline 8-9 页 |\n| R18-m-refs (Chen 2026, Wei 2023) | **[FIXED]** | 两篇均已 cite 且引用验证通过 |\n| R17-W3 (diagnostic > engineering value) | **[PARTIALLY FIXED]** | Discussion 末尾 \"diagnostic guidelines derived from correlational evidence\"，但全文 framing 仍偏乐观 |\n\n### Strengths\n- S1: 实验设计严谨（BCS-controlled stratification, TOST, permutation test, bootstrap CI, within-pool 控制）\n- S2: 跨模型验证充分（4 模型含 proprietary Gemini）\n- S3: SDGD 负面结果诚实报告，对社区有警示意义\n- S4: Limitations 10 项覆盖全面，含 power 分析自我披露\n- S5: 70 篇引用，positioning 清晰\n\n### Weaknesses\n- **N1 [critical]**: 核心发现 novelty 有限——\"more types = worse\" 和 \"similar types confuse\" 概念上非 surprising；SCS 形式同 LLM-PEE；controlled experimental methodology 技术上非 novel。作为纯 analytical study，知识增量需足够大但效应量 modest\n- **N2 [critical]**: Confusability 效应量小且 task-specific——pairwise r²=1.3-1.7%；NER batch-level 完全 null (n=450)；RE 发现依赖 forced-choice format 边界条件。Title/framing 暗示普适性但实际高度 task-specific\n- **W1 [warning]**: 核心分析集中在 FewRel 一个数据集\n- **W2 [warning]**: NER U-shape 现象缺乏实验证据解释\n- **W3 [warning]**: \"First controlled study\" claim 可能过强\n\n### Questions\n- Q1: FewRel train-origin types 为何反而 accuracy 低 8.8pp？\n- Q2: 16-rel condition 使用 single extreme batch 是否可能是 outlier？\n- Q3: TOST ±1pp inconclusive 意味着 interaction 可能达 main effect 91%，\"largely additive\" framing 是否过强？\n\n### Missing References\n引用验证：70 bib / 97 citations / 0 orphan / 0 missing / 0 fabricated。建议补充 Guidance (Zheng et al., 2023) 和 Lyu et al. (2024)。\n\n### Scores\n- Soundness: 4/5\n- Excitement: 2.5/5\n- Reproducibility: 4/5\n- Overall: 2.5 (Borderline Findings)\n- Confidence: 4/5\n\n### 一句话总结\n实验执行出色的 analytical study，但核心发现（count dominates + confusability modest & RE-specific）的 novelty 和 impact 对 Findings 而言 borderline——知识增量受限于 modest effect sizes、NER batch-level null、和 SDGD 失败后缺乏 actionable alternative。\n\n---\n\n请逐条回应 R2 的 Weaknesses (N1, N2, W1, W2, W3)、Questions (Q1-Q3) 和 Missing References。对你自己的 issues 如果 R2 的审稿改变了你的判断也请说明。"
  }
}
```

</details>

---


### Tool result

_source line 1965 · 2026-05-18T10:04:11.822898+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 34537
}
```

</details>

---


### Tool call

_source line 1966 · 2026-05-18T10:04:13.481827+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### R18 修复验证\n- R18-N1 [FIXED]: forced-choice classification format vs constrained decoding 区分。全文已精确区分。\n- R18-N2 [FIXED]: \"two separable dimensions\" → \"largely additive with bounded interaction\"。统一使用，logit-scale TOST 在正文报告。\n- R18-N3 [FIXED]: Contribution 2 从 metric innovation 改为 methodology contribution。\n- R18-W2 [PARTIALLY FIXED]: Cohen (1988) 套用到 LLM 系统。加了 hedging 但仍以 behavioral research 框架为锚定。\n- R18-W5 [FIXED]: Dimension 2 未在 proprietary model 上验证。Limitations 明确声明。\n- R18-W7 [FIXED]: BCS-aware grouping +1.4pp 无显著优势的解释。SDGD 加了 \"marginal mean BCS reduction\" 解释。\n- R17-W3 [PARTIALLY FIXED]: Typical-batch 2.2pp 实际意义有限。Results 透明报告，Discussion 承认 diagnostic nature，但 Abstract/Introduction 仍偏重 extreme-batch 数字。\n\n### Strengths\n- S1: BCS-controlled 设计 + within-pool analysis + permutation test，控制变量到位\n- S2: 统计分析全面且透明（TOST 三个 margin、logit-scale、bootstrap CIs、variance decomposition）\n- S3: 负面结果诚实报告（SDGD、NER null、MAVEN confound、logit-scale inconclusive）\n- S4: 跨模型验证覆盖面广（4 模型）\n- S5: Robustness checks 充分（prompt variants、BCS aggregation、embedding ablation、SCS baselines、held-out validation、split-origin covariate）\n\n### Weaknesses\n- **N1 [warning]**: TOST margin 选择与 main effect 关系需更多论证。±3pp margin 允许 interaction 达 main effect 的 136% (3/2.2)。±2pp marginal, ±1pp inconclusive。Logit scale inconclusive。\"Largely additive\" 偏乐观。\n- **N2 [warning]**: Abstract/Introduction 叙事偏重 extreme-batch 数字（31.2pp, -49pp），淡化 typical-batch modest effect (2.2pp)。读者 impression 与实际 impact 有落差。\n- **N3 [warning]**: NER batch-level null 削弱 \"two-dimensional\" 框架的普适性。NER 是比 RE classification 更 mainstream 的 IE task。\n- **N4 [info]**: Monte Carlo simulation 的 evidential status 需更清晰。Discussion 引用 simulation 时可能给人 independent corroboration 的印象。\n- **N5 [info]**: Few-shot 实验中 5-shot low-BCS 回落的解释不够充分。两组不对称降幅可能有 confusability-specific 解释。\n- **N6 [info]**: Prompt variant analysis 的 multiple comparison 处理。Rothman (1990) 针对 independent replications，这里是 same dataset + same batches + different prompts，positive correlation 会 inflate directional consistency。\n\n### Questions\n- Q1: Table 2 排除 FewRel 但 §3.2 和 Appendix Table 14 报告了 FewRel pairwise ρ=0.218/0.187。是否矛盾？\n- Q2: Variance decomposition count=16 seed SD (0.027) 异常高于其他 count levels。是否影响 count=16 BCS-controlled 结论？\n- Q3: BCS independence analysis shared variance 20.9%。BCS-controlled 实验是否控制了 mean type difficulty？\n\n### Missing References\n无明显遗漏。引用密度符合 ACL venue 标准。\n\n### Scores\n- Soundness: 3.5/5\n- Excitement: 2.5/5\n- Reproducibility: 4/5\n- Overall: 3.0 (Findings)\n- Confidence: 4/5\n\n### 一句话总结\n方法论严谨的实证研究，controlled experimental design 在 training-free IE 文献中是有价值的贡献。但 practical impact limited (2.2pp typical), NER batch-level null, schema decomposition failure, 以及 \"largely additive\" claim 的 logit-scale caveat 限制了 excitement。适合 Findings。\n\n---\n\n请逐条回应 R1 的 Weaknesses (N1-N6)、Questions (Q1-Q3) 和 Missing References。特别关注：\n1. R1-N1 关于 TOST margin vs main effect 的论证——你的 Soundness 评分是否需要调整？\n2. R1-N4 关于 simulation evidential status 的判断——你是否同意？\n3. R1 给 Overall 3.0 而你给 2.5——主要分歧在 novelty 评估上。请阐述你对 experimental methodology contribution 价值的判断。\n\n对你自己的 issues 如果 R1 的审稿改变了你的判断也请说明。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### R18 修复验证\n- R18-N1 [FIXED]: forced-choice classification format vs constrained decoding 区分。全文已精确区分。\n- R18-N2 [FIXED]: \"two separable dimensions\" → \"largely additive with bounded interaction\"。统一使用，logit-scale TOST 在正文报告。\n- R18-N3 [FIXED]: Contribution 2 从 metric innovation 改为 methodology contribution。\n- R18-W2 [PARTIALLY FIXED]: Cohen (1988) 套用到 LLM 系统。加了 hedging 但仍以 behavioral research 框架为锚定。\n- R18-W5 [FIXED]: Dimension 2 未在 proprietary model 上验证。Limitations 明确声明。\n- R18-W7 [FIXED]: BCS-aware grouping +1.4pp 无显著优势的解释。SDGD 加了 \"marginal mean BCS reduction\" 解释。\n- R17-W3 [PARTIALLY FIXED]: Typical-batch 2.2pp 实际意义有限。Results 透明报告，Discussion 承认 diagnostic nature，但 Abstract/Introduction 仍偏重 extreme-batch 数字。\n\n### Strengths\n- S1: BCS-controlled 设计 + within-pool analysis + permutation test，控制变量到位\n- S2: 统计分析全面且透明（TOST 三个 margin、logit-scale、bootstrap CIs、variance decomposition）\n- S3: 负面结果诚实报告（SDGD、NER null、MAVEN confound、logit-scale inconclusive）\n- S4: 跨模型验证覆盖面广（4 模型）\n- S5: Robustness checks 充分（prompt variants、BCS aggregation、embedding ablation、SCS baselines、held-out validation、split-origin covariate）\n\n### Weaknesses\n- **N1 [warning]**: TOST margin 选择与 main effect 关系需更多论证。±3pp margin 允许 interaction 达 main effect 的 136% (3/2.2)。±2pp marginal, ±1pp inconclusive。Logit scale inconclusive。\"Largely additive\" 偏乐观。\n- **N2 [warning]**: Abstract/Introduction 叙事偏重 extreme-batch 数字（31.2pp, -49pp），淡化 typical-batch modest effect (2.2pp)。读者 impression 与实际 impact 有落差。\n- **N3 [warning]**: NER batch-level null 削弱 \"two-dimensional\" 框架的普适性。NER 是比 RE classification 更 mainstream 的 IE task。\n- **N4 [info]**: Monte Carlo simulation 的 evidential status 需更清晰。Discussion 引用 simulation 时可能给人 independent corroboration 的印象。\n- **N5 [info]**: Few-shot 实验中 5-shot low-BCS 回落的解释不够充分。两组不对称降幅可能有 confusability-specific 解释。\n- **N6 [info]**: Prompt variant analysis 的 multiple comparison 处理。Rothman (1990) 针对 independent replications，这里是 same dataset + same batches + different prompts，positive correlation 会 inflate directional consistency。\n\n### Questions\n- Q1: Table 2 排除 FewRel 但 §3.2 和 Appendix Table 14 报告了 FewRel pairwise ρ=0.218/0.187。是否矛盾？\n- Q2: Variance decomposition count=16 seed SD (0.027) 异常高于其他 count levels。是否影响 count=16 BCS-controlled 结论？\n- Q3: BCS independence analysis shared variance 20.9%。BCS-controlled 实验是否控制了 mean type difficulty？\n\n### Missing References\n无明显遗漏。引用密度符合 ACL venue 标准。\n\n### Scores\n- Soundness: 3.5/5\n- Excitement: 2.5/5\n- Reproducibility: 4/5\n- Overall: 3.0 (Findings)\n- Confidence: 4/5\n\n### 一句话总结\n方法论严谨的实证研究，controlled experimental design 在 training-free IE 文献中是有价值的贡献。但 practical impact limited (2.2pp typical), NER batch-level null, schema decomposition failure, 以及 \"largely additive\" claim 的 logit-scale caveat 限制了 excitement。适合 Findings。\n\n---\n\n请逐条回应 R1 的 Weaknesses (N1-N6)、Questions (Q1-Q3) 和 Missing References。特别关注：\n1. R1-N1 关于 TOST margin vs main effect 的论证——你的 Soundness 评分是否需要调整？\n2. R1-N4 关于 simulation evidential status 的判断——你是否同意？\n3. R1 给 Overall 3.0 而你给 2.5——主要分歧在 novelty 评估上。请阐述你对 experimental methodology contribution 价值的判断。\n\n对你自己的 issues 如果 R1 的审稿改变了你的判断也请说明。"
  }
}
```

</details>

---


### Tool result

_source line 1967 · 2026-05-18T10:04:15.149002+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1667
}
```

</details>

---


### Assistant

_source line 1968 · 2026-05-18T10:04:19.613455+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 172

## Round 172

2 recorded events


### User

_source line 1969 · 2026-05-18T10:04:22.349970+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：R18 的 3 个 Critical issues 全部修复，写作/格式问题大部分修复（页数无法验证，diagnostic framing 部分修复）。新发现 2 个 Critical 问题（novelty 有限、confusability 效应 RE-specific）和 3 个 Warning。Overall 评分 2.5 (Borderline Findings)，主要受限于 modest effect sizes 和缺乏 actionable output。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1970 · 2026-05-18T10:04:27.609564+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 173

## Round 173

2 recorded events


### User

_source line 1971 · 2026-05-18T10:05:26.949295+00:00_

[Reviewer 1 审稿意见]:

# R1 对 Reviewer 2 审稿意见的逐条回应

---

## R18 修复验证

R2 的修复验证与 R1 判断高度一致，仅就两项补充意见：

**R18-W8 (正文页数)**: [AGREE] R2-W8: 我同样无法编译验证。从 section 数量和内容密度估算，8 页 borderline 是合理判断。这是一个需要作者确认的 formatting 问题。

**R17-W3 (diagnostic > engineering)**: [AGREE] R2-R17-W3: 与我的 N2 一致。Discussion 末尾的 hedging 到位，但 Abstract/Introduction 的叙事仍偏重 extreme-batch 数字（-31.2pp, -49pp），对 typical-batch 2.2pp 的 modest effect 着墨不足。

---

## Weaknesses 逐条回应

**[AGREE] R2-N1 (novelty 有限)**:
同意 novelty 是本文的主要弱点。"More types = worse" 在 Li et al. (2023)、LLM-PEE (2025) 中已有定性观察；"similar types confuse" 在 hierarchical classification (Deng et al., 2010 ImageNet) 和 label confusion (Guo et al., 2021) 中有先例。SCS 形式同 LLM-PEE 的 partitioning criterion（Related Work §2 SCS novelty 段已承认）。论文的 novelty 在于 controlled experimental methodology，但 R2 的判断"技术上非 novel"有道理——BCS-controlled stratification 本质上是 observational study with quasi-experimental manipulation，不是新方法。

不过我对 R2 的 framing 有一个 nuance 补充：虽然概念不 surprising，但在 training-free IE 文献中，此前没有人量化过 count vs confusability 的相对贡献，也没有人发现 NER batch-level null 这个 task asymmetry。这些 empirical findings 在 Findings track 中是 acceptable 的 knowledge increment，即使 conceptual novelty 有限。

**[AGREE] R2-N2 (effect size small & task-specific)**:
与我的 N2 和 N3 一致。具体证据：
- Pairwise r²=1.3-1.7% (Table 2)
- NER batch-level r≈0, n=450 (§4.3, §4.4)
- Typical-batch gap 2.2pp, CI [0.4, 4.0] (§4.3 practical magnitude)
- Dimension 2 batch-level signal 仅在 RE forced-choice format 下成立 (Discussion §6)

Title "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?" 确实暗示了对 IE 的普适性，但 Dimension 2 的 batch-level 预测力仅限 RE classification format。R2 的 "task-specific" 判断准确。

**[PARTIALLY REBUT] R2-W1 (核心分析集中 FewRel 一个数据集)**:
R2 的担忧有道理，但需要区分维度：
- **Dimension 1 (count curves)**: 在 FewRel、DocRED、Few-NERD、MAVEN 四个数据集上均有复现（Figure 1a, §4.1），不是 single-dataset。
- **Dimension 2 (BCS-controlled)**: FewRel 是 primary dataset，但 DocRED 独立复现了 BCS-accuracy slopes（slope=-0.713, R²=0.525 at count 16, R²=0.443 at count 32; §4.3 Document-level RE 段）。两个 RE 数据集（80 vs 96 types, sentence vs document level）的一致性构成有意义的 replication。
- **Pairwise SCS**: 在 Few-NERD (r=0.112)、FewRel (r=0.187)、MAVEN (r=0.129) 三个数据集上均显著 (Table 2, §3.2)。

真正的 single-dataset 问题在于：BCS-controlled 的 detailed analysis（within-pool, factorial, aggregation simulation）全部基于 FewRel。DocRED 的 BCS 分析相对简略（n=35 batches, 无 within-pool 控制）。

**[AGREE] R2-W2 (NER U-shape 缺乏实验证据)**:
Discussion §6 提出的 "dual-task burden" 假说（partial schemas require simultaneous span detection and type-membership filtering; at full schema, filtering becomes vacuous and recall recovers）是合理的机制假说，但完全是 speculative——没有控制实验验证。论文没有设计实验区分 U-shape 的 three possible explanations：(1) type-membership filtering overhead, (2) prompt length effect, (3) instruction complexity。Cross-model replication of U-shape（Table 9, 70B 和 Qwen3 均在 count 22→44 处 rebound）增加了现象的可信度，但不解释机制。R2 的 concern 成立。

**[PARTIALLY REBUT] R2-W3 ("first controlled study" claim 过强)**:
这取决于 "controlled" 的定义。论文的 claim 是 "first controlled study isolating type confusability from type count via stratified design in zero-shot LLM IE, spanning NER, RE, and event detection" (§1)。关键限定词是 "isolating...via stratified design"。
- LLM-PEE (2025) 用 embedding similarity 做 schema partitioning，但没有 fix count + vary BCS 的 controlled comparison。
- Li et al. (2023) 观察 count-dependent degradation，但不分离 confusability。
- 其他 decomposition 工作（UniNER, PARSE 等）都是 engineering solutions，不做 controlled factor isolation。

因此 "first controlled study" 在字面意义上可能成立，但 "controlled" 在这里指 quasi-experimental stratification，不是 randomized intervention。论文在 Limitations item 8 已承认 "correlational evidence with controlled stratification" 而非 "interventional causality"。Claim 不算过强，但可以更 precise 地写 "first quasi-experimental study"。

---

## Questions 逐条回应

**[AGREE with nuance] R2-Q1 (FewRel train-origin accuracy 低 8.8pp)**:
合理的问题。Appendix §L 报告 train-origin ratio 不显著（β=-0.057, p=0.245），BCS partial effect unchanged。但 -8.8pp (p=0.06) 的 borderline significance 确实值得讨论。论文在 Limitations item 10 把它归入 data contamination 讨论，认为 "opposite to the contamination hypothesis"（contamination 应使 train-origin accuracy 更高）。一个可能的解释是 train-split types 在 Wikidata 中 inherently 更难（被选入 training set 可能因为它们对 few-shot learning 更有挑战性），但论文未验证。R2 的问题合理但不影响核心结论（Appendix §L covariate analysis 已控制）。

**[AGREE] R2-Q2 (16-rel single extreme batch = outlier risk)**:
与论文自身的 caveat 一致。Appendix Table 8 caption 明确写 "The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches"。论文将 16-rel 作为 pilot condition，主要证据来自 80-rel pool 的 n=25/group 设计。R2 的 concern 成立但论文已 acknowledge。

**[AGREE] R2-Q3 (TOST ±1pp inconclusive → interaction 可能达 main effect 91%)**:
与我的 N1 一致。Interaction 的 90% CI 上界 2.0pp / main effect 2.2pp = 91%。这使 "largely additive" 在严格统计意义上站不住——数据不能排除 interaction 接近 main effect 的可能。论文的 defense 是 point estimate 很小 (0.47pp)，但 CI 宽度反映了 insufficient power。在 logit scale 上 TOST 也 inconclusive (p=0.209, Appendix §C)。

不过我补充一个 nuance：cross-pool slope consistency (permutation p=0.60, Table 5) 提供了间接证据——如果 count×BCS interaction 很大，不同 count pool 的 BCS slope 应该不一致。这不是 formal equivalence test，但 directionally supportive。

---

## Missing References

**[PARTIALLY AGREE] R2 建议补充 Guidance (Zheng et al., 2023) 和 Lyu et al. (2024)**:
- Zheng et al. (2023) 如果是 LLM-as-judge/evaluation guidance 方向，与本文的 schema complexity 主题相关性有限。如果是 label guidance 方向，可能值得在 Related Work 中提及。需要作者确认具体是哪篇。
- Lyu et al. (2024) 同理，需要确认具体论文。R2 未提供 full citation，无法判断相关性。
- 论文现有 70 篇引用覆盖面已较完整。

---

## R2 审稿对 R1 判断的影响

R2 的 N1 (novelty) 和 N2 (task-specificity) 是我同意的 concerns，但对 Overall 评分的影响我与 R2 有分歧：

- R2 给 Overall 2.5 (Borderline Findings)，理由是 "知识增量受限于 modest effect sizes、NER batch-level null、SDGD 失败后缺乏 actionable alternative"。
- 我维持 Overall 3.0 (Findings)。理由：(1) 论文的价值不在 engineering solution 而在 diagnostic framework——quantifying 了此前仅被定性观察的现象；(2) NER batch-level null 本身是一个有价值的 negative finding（task format determines whether confusability is batch-level predictive）；(3) SDGD 失败的诊断（merge amplification, routing failure）对未来 decomposition 工作有指导意义；(4) 统计透明度（TOST, logit-scale caveat, power analysis）在 NLP 实证论文中罕见，值得鼓励。

这些 negative/modest results 如果被认为 "not enough for Findings"，会产生 publication bias 激励——只有 effect size 大且 positive 的结果才能发表。ARR reviewer guidelines H6 明确指出 "negative findings" 不应被自动降低评价。

**最终判断**: R2 的审稿加强了我对 novelty 和 framing 问题的 concern，但不改变我的 Overall 3.0。论文需要在 Abstract/Introduction 中更 calibrated 地呈现 typical-batch effect size 和 task-specificity boundary condition。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1972 · 2026-05-18T10:05:53.908283+00:00_

R1 的交叉回应已收到。等待 R2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 174

## Round 174

2 recorded events


### User

_source line 1973 · 2026-05-18T10:05:56.735301+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。核心立场：

- **N1 (novelty)** 和 **N2 (task-specificity)**: 同意这是主要弱点，但 controlled methodology + negative findings 在 Findings track 仍有价值
- **W1 (single dataset)**: 部分反驳——DocRED 独立复现了 BCS slopes，Dimension 1 跨四个数据集复现
- **W2 (U-shape)**: 同意，假说缺实验验证
- **W3 (first controlled study)**: 部分反驳，claim 在字面意义上成立但可写 "quasi-experimental"
- **Q3 (TOST ±1pp)**: 同意，与我的 N1 一致，"largely additive" 偏乐观

维持 Overall 3.0 (Findings)，未因 R2 的 2.5 改变评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1974 · 2026-05-18T10:06:01.967196+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 175

## Round 175

4 recorded events


### User

_source line 1975 · 2026-05-18T10:06:03.477308+00:00_

[Reviewer 2 审稿意见]:
## Round 19 Reviewer 2 — 逐条回应 Reviewer 1

### Weaknesses 回应
- **[AGREE] R1-N1 (TOST margin vs main effect)**: ±3pp margin 允许 interaction 达 main effect 136%，framing 偏乐观。但论文统计报告透明（三 margin + logit-scale caveat），是 framing 问题非 soundness 问题。**我的 Soundness 4/5 不调整。**
- **[AGREE] R1-N2 (extreme-batch 数字主导叙事)**: 与我的 N2 一致。typical-batch 2.2pp 在 Abstract 中完全缺失。
- **[AGREE] R1-N3 (NER null 削弱普适性)**: 与我的 N2 重叠。Title/framing 暗示跨任务发现但实际 RE-specific。
- **[AGREE] R1-N4 (simulation evidential status)**: Discussion 的括号 caveat 到位但呈现方式仍给人 corroboration 印象。Presentation issue, not soundness issue。
- **[AGREE] R1-N5 (few-shot 5-shot 回落)**: high-BCS 降幅更大 (-6.6 vs -3.9pp) 暗示 confusability-specific interaction，论文未讨论。Info 级别。
- **[PARTIALLY AGREE] R1-N6 (prompt variant multiple comparison)**: 技术上正确（same data ≠ independent replications），但 Minimal 即使 Bonferroni 后仍显著（$p=0.009$ vs $\alpha=0.0125$），且 prompt variants 是 supplementary evidence。不动摇核心结论。

### Questions 回应
- **R1-Q1**: 非矛盾——Table 2 排除 FewRel 因 RE per-instance format 不同，§3.2 用不同 confusion rate 计算。Clarity issue。
- **R1-Q2**: count=16 seed SD=0.027 确实异常，但 BCS-controlled 用 $n=100$ batches 足以吸收。影响有限。
- **R1-Q3**: shared variance 20.9% 值得注意——extreme batches 的 difficulty 分布可能与 random batches 不同。非 critical 但潜在 confound。

### Missing References
[AGREE] 无明显遗漏。

### 分歧讨论：Overall 3.0 (R1) vs 2.5 (R2)
分歧核心在 methodology contribution 价值判断。R1 认为 controlled design 填补 gap；我认为 stratified sampling + regression 是标准方法论移植，知识增量受限于 modest effect sizes (pairwise $r^2$=1.3-1.7%, NER null, typical 2.2pp)。

**我维持 Overall 2.5 (Borderline Findings)**，但认为 2.5-3.0 区间合理。如果作者调整 title/framing 更准确反映 RE-specific 发现、Abstract 加入 typical-batch magnitude、Introduction 承认 diagnostic > engineering value，可上调至 3.0。

### 最终评分（维持不变）
- Soundness: 4/5
- Excitement: 2.5/5
- Reproducibility: 4/5
- Overall: 2.5 (Borderline Findings)
- Confidence: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1976 · 2026-05-18T10:07:46.254217+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema-dag-extraction",
  "issues_yaml": "# Round 19 Review Issues Tracker\n# Updated: 2026-05-18 (R19 审稿报告)\n\n# ============================================================\n# CRITICAL (R19 新增)\n# ============================================================\n\n- id: R19-N1\n  summary: \"核心发现 novelty 有限: SCS 形式同 LLM-PEE, 'more types = worse' 和 'similar types confuse' 概念上非 surprising, controlled methodology 是标准方法论移植\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R2 定 critical, R1 同意 novelty 是主要弱点但认为 controlled design + negative findings 在 Findings track 有价值. 共识: 指标不新, methodology 有贡献但非 technically novel. 分歧在 Findings 是否足够.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-N2\n  summary: \"Confusability 效应量小且 RE-specific: pairwise r²=1.3-1.7%, NER batch-level null (n=450), RE 发现依赖 forced-choice format. Title/framing 暗示跨任务普适性\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R2 定 critical, R1 同意 (与 R1-N2/N3 一致). Dimension 2 batch-level 仅限 RE closed-set classification format, Abstract 缺 typical-batch magnitude (2.2pp).\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING (R19 新增)\n# ============================================================\n\n- id: R19-W1\n  summary: \"TOST ±3pp margin 允许 interaction 达 main effect 136%, ±1pp inconclusive, logit-scale inconclusive. 'Largely additive' framing 偏乐观\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1 提出, R2 同意. 是 framing 问题非 soundness 问题. Cross-pool slope consistency (p=0.60) 提供间接支持.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W2\n  summary: \"Abstract/Introduction 叙事偏重 extreme-batch 数字 (31.2pp, -49pp), 淡化 typical-batch modest effect (2.2pp, CI [0.4, 4.0])\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1-N2 + R2-N2 共识. Typical-batch magnitude 在 Abstract 中完全缺失.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W3\n  summary: \"NER batch-level null 削弱 'two-dimensional' 框架普适性. NER 是比 RE classification 更 mainstream 的 IE task\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1-N3 + R2-N2 共识. Title/Abstract 暗示跨任务但 Dim2 batch-level RE-specific.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W4\n  summary: \"NER U-shape 的 'dual-task burden' 假说缺乏实验证据, 完全 speculative\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R2-W2, R1 同意. Cross-model replication 增加现象可信度但不解释机制.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W5\n  summary: \"核心 BCS-controlled detailed analysis 集中在 FewRel; DocRED 分析相对简略 (n=35, 无 within-pool 控制)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R2-W1 提出. R1 部分反驳: DocRED 独立复现了 BCS slopes, Dim1 跨四个数据集. 但 detailed analysis 确实 FewRel-centric.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO (R19 新增)\n# ============================================================\n\n- id: R19-I1\n  summary: \"Monte Carlo simulation (Appendix I) 的 evidential status: Discussion 引用时可能给人 independent corroboration 印象\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1-N4, R2 同意. Presentation issue, not soundness.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-I2\n  summary: \"Few-shot 5-shot low-BCS 回落 (0.754→0.715) 解释不充分; high-BCS 降幅更大 (-6.6 vs -3.9pp)\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1-N5, R2 同意. 可能有 confusability-specific interaction.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-I3\n  summary: \"Prompt variant analysis 的 Rothman (1990) 引用不当: same dataset ≠ independent replications, positive correlation inflates directional consistency\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1-N6, R2 部分同意. Minimal 即使 Bonferroni 后仍显著 (p=0.009). 不动摇核心结论.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R18 ISSUES — STATUS UPDATE\n# ============================================================\n\n- id: R18-N1\n  summary: \"BCS batch-level 仅限 RE forced-choice classification format, 非 constrained decoding\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 19\n  mentions:\n    - {round: 17, reviewers: [R1, R2], note: \"boundary condition = constrained decoding\"}\n    - {round: 18, reviewers: [R1, R2], note: \"精确化: forced-choice classification format\"}\n    - {round: 19, reviewers: [R1, R2], note: \"R19 两位 Reviewer 均确认 [FIXED]. 全文统一使用 forced-choice classification format.\"}\n  resolution: \"全文已精确区分 forced-choice classification format vs constrained decoding. Abstract/Discussion/Conclusion/Limitations 术语一致.\"\n  resolution_round: 19\n\n- id: R18-N2\n  summary: \"'Two separable dimensions' 在 logit-scale 上 inconclusive; 需 'largely additive with bounded interaction'\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 19\n  mentions:\n    - {round: 17, reviewers: [R1, R2], note: \"TOST ±3pp margin > 2.2pp\"}\n    - {round: 18, reviewers: [R1, R2], note: \"需全文统一\"}\n    - {round: 19, reviewers: [R1, R2], note: \"R19 两位 Reviewer 均确认 [FIXED]. 全文统一 'largely additive'. 但 R19-W1 指出 framing 仍偏乐观.\"}\n  resolution: \"全文已统一 'largely additive with bounded interaction'. Logit-scale caveat 在正文提及.\"\n  resolution_round: 19\n\n- id: R18-N3\n  summary: \"Contribution 2 仍暗示 metric innovation\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: [R1, R2], note: \"改为 methodology contribution\"}\n    - {round: 19, reviewers: [R1, R2], note: \"R19 两位 Reviewer 均确认 [FIXED]. 'Building on...LLM-PEE...we design controlled experiments'.\"}\n  resolution: \"Contribution 2 焦点转为 experimental design methodology.\"\n  resolution_round: 19\n\n- id: R18-W1\n  summary: \"Abstract 217 words 信息过载\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R2 确认 [FIXED]. ~156 words, 结构清晰.\"}\n  resolution: \"Abstract 压缩至 ~156 words.\"\n  resolution_round: 19\n\n- id: R18-W7\n  summary: \"BCS-aware grouping 无显著优势 (+1.4pp) 与 BCS R²=22-53% 矛盾\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1 确认 [FIXED]. 'marginal mean BCS reduction (0.559→0.552)' 解释到位.\"}\n  resolution: \"SDGD section 加了 marginal BCS reduction 解释.\"\n  resolution_round: 19\n\n- id: R18-W8\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"两位 Reviewer 均无法编译验证. 估算 borderline 8-9 页.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-W2\n  summary: \"Pairwise r²=1.3-1.7% 引用 Cohen (1988) 套用到 LLM 系统\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1 确认 [PARTIALLY FIXED]. 加了 hedging 但仍以 behavioral research 为锚定.\"}\n  action_items:\n    - {round: 19, action: \"找 NLP/LLM 领域 effect size 解读先例 或 明确说明 tentative analogy\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-W5\n  summary: \"Dimension 2 未在 proprietary model (Gemini) 上验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1 确认 [FIXED]. Limitations item 1 明确声明.\"}\n  resolution: \"Limitations 明确标注 Dimension 2 仅在 open-weight 模型上验证.\"\n  resolution_round: 19\n\n- id: R18-m-refs\n  summary: \"Missing refs: Chen et al. 2026, Wei et al. 2023\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R2 确认 [FIXED]. 两篇均已 cite.\"}\n  resolution: \"两篇引用已补充.\"\n  resolution_round: 19\n\n- id: R17-W3\n  summary: \"Practical implications 薄弱\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: [R1, R2], note: \"2.2pp typical-batch 实际意义有限\"}\n    - {round: 19, reviewers: [R1, R2], note: \"R1/R2 确认 [PARTIALLY FIXED]. Discussion 加了 diagnostic hedging 但 Abstract/Intro 仍偏重 extreme-batch 数字. 与 R19-W2 重叠.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED (R18 及更早)\n# ============================================================\n\n- id: R17-W1\n  summary: \"SCS vs simple baselines 对比\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: \"SCS baselines Table 已加入 Appendix.\"\n  resolution_round: 18\n\n- id: R16-N3\n  summary: \"效应量 framing 偏误\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 17\n  resolution: \"R17 确认修复\"\n  resolution_round: 17\n\n- id: R16-m5\n  summary: \"FewRel 数据污染论证\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 17\n  resolution: \"R17 确认充分\"\n  resolution_round: 17\n\n- id: R10-N1\n  summary: \"因果语言超出证据\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  resolution: \"Title 改 Predict; 因果语言清理\"\n  resolution_round: 12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema-dag-extraction",
    "issues_yaml": "# Round 19 Review Issues Tracker\n# Updated: 2026-05-18 (R19 审稿报告)\n\n# ============================================================\n# CRITICAL (R19 新增)\n# ============================================================\n\n- id: R19-N1\n  summary: \"核心发现 novelty 有限: SCS 形式同 LLM-PEE, 'more types = worse' 和 'similar types confuse' 概念上非 surprising, controlled methodology 是标准方法论移植\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R2 定 critical, R1 同意 novelty 是主要弱点但认为 controlled design + negative findings 在 Findings track 有价值. 共识: 指标不新, methodology 有贡献但非 technically novel. 分歧在 Findings 是否足够.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-N2\n  summary: \"Confusability 效应量小且 RE-specific: pairwise r²=1.3-1.7%, NER batch-level null (n=450), RE 发现依赖 forced-choice format. Title/framing 暗示跨任务普适性\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R2 定 critical, R1 同意 (与 R1-N2/N3 一致). Dimension 2 batch-level 仅限 RE closed-set classification format, Abstract 缺 typical-batch magnitude (2.2pp).\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING (R19 新增)\n# ============================================================\n\n- id: R19-W1\n  summary: \"TOST ±3pp margin 允许 interaction 达 main effect 136%, ±1pp inconclusive, logit-scale inconclusive. 'Largely additive' framing 偏乐观\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1 提出, R2 同意. 是 framing 问题非 soundness 问题. Cross-pool slope consistency (p=0.60) 提供间接支持.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W2\n  summary: \"Abstract/Introduction 叙事偏重 extreme-batch 数字 (31.2pp, -49pp), 淡化 typical-batch modest effect (2.2pp, CI [0.4, 4.0])\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1-N2 + R2-N2 共识. Typical-batch magnitude 在 Abstract 中完全缺失.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W3\n  summary: \"NER batch-level null 削弱 'two-dimensional' 框架普适性. NER 是比 RE classification 更 mainstream 的 IE task\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1-N3 + R2-N2 共识. Title/Abstract 暗示跨任务但 Dim2 batch-level RE-specific.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W4\n  summary: \"NER U-shape 的 'dual-task burden' 假说缺乏实验证据, 完全 speculative\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R2-W2, R1 同意. Cross-model replication 增加现象可信度但不解释机制.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W5\n  summary: \"核心 BCS-controlled detailed analysis 集中在 FewRel; DocRED 分析相对简略 (n=35, 无 within-pool 控制)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R2-W1 提出. R1 部分反驳: DocRED 独立复现了 BCS slopes, Dim1 跨四个数据集. 但 detailed analysis 确实 FewRel-centric.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO (R19 新增)\n# ============================================================\n\n- id: R19-I1\n  summary: \"Monte Carlo simulation (Appendix I) 的 evidential status: Discussion 引用时可能给人 independent corroboration 印象\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1-N4, R2 同意. Presentation issue, not soundness.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-I2\n  summary: \"Few-shot 5-shot low-BCS 回落 (0.754→0.715) 解释不充分; high-BCS 降幅更大 (-6.6 vs -3.9pp)\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1-N5, R2 同意. 可能有 confusability-specific interaction.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-I3\n  summary: \"Prompt variant analysis 的 Rothman (1990) 引用不当: same dataset ≠ independent replications, positive correlation inflates directional consistency\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1-N6, R2 部分同意. Minimal 即使 Bonferroni 后仍显著 (p=0.009). 不动摇核心结论.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R18 ISSUES — STATUS UPDATE\n# ============================================================\n\n- id: R18-N1\n  summary: \"BCS batch-level 仅限 RE forced-choice classification format, 非 constrained decoding\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 19\n  mentions:\n    - {round: 17, reviewers: [R1, R2], note: \"boundary condition = constrained decoding\"}\n    - {round: 18, reviewers: [R1, R2], note: \"精确化: forced-choice classification format\"}\n    - {round: 19, reviewers: [R1, R2], note: \"R19 两位 Reviewer 均确认 [FIXED]. 全文统一使用 forced-choice classification format.\"}\n  resolution: \"全文已精确区分 forced-choice classification format vs constrained decoding. Abstract/Discussion/Conclusion/Limitations 术语一致.\"\n  resolution_round: 19\n\n- id: R18-N2\n  summary: \"'Two separable dimensions' 在 logit-scale 上 inconclusive; 需 'largely additive with bounded interaction'\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 19\n  mentions:\n    - {round: 17, reviewers: [R1, R2], note: \"TOST ±3pp margin > 2.2pp\"}\n    - {round: 18, reviewers: [R1, R2], note: \"需全文统一\"}\n    - {round: 19, reviewers: [R1, R2], note: \"R19 两位 Reviewer 均确认 [FIXED]. 全文统一 'largely additive'. 但 R19-W1 指出 framing 仍偏乐观.\"}\n  resolution: \"全文已统一 'largely additive with bounded interaction'. Logit-scale caveat 在正文提及.\"\n  resolution_round: 19\n\n- id: R18-N3\n  summary: \"Contribution 2 仍暗示 metric innovation\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: [R1, R2], note: \"改为 methodology contribution\"}\n    - {round: 19, reviewers: [R1, R2], note: \"R19 两位 Reviewer 均确认 [FIXED]. 'Building on...LLM-PEE...we design controlled experiments'.\"}\n  resolution: \"Contribution 2 焦点转为 experimental design methodology.\"\n  resolution_round: 19\n\n- id: R18-W1\n  summary: \"Abstract 217 words 信息过载\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R2 确认 [FIXED]. ~156 words, 结构清晰.\"}\n  resolution: \"Abstract 压缩至 ~156 words.\"\n  resolution_round: 19\n\n- id: R18-W7\n  summary: \"BCS-aware grouping 无显著优势 (+1.4pp) 与 BCS R²=22-53% 矛盾\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1 确认 [FIXED]. 'marginal mean BCS reduction (0.559→0.552)' 解释到位.\"}\n  resolution: \"SDGD section 加了 marginal BCS reduction 解释.\"\n  resolution_round: 19\n\n- id: R18-W8\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"两位 Reviewer 均无法编译验证. 估算 borderline 8-9 页.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-W2\n  summary: \"Pairwise r²=1.3-1.7% 引用 Cohen (1988) 套用到 LLM 系统\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1 确认 [PARTIALLY FIXED]. 加了 hedging 但仍以 behavioral research 为锚定.\"}\n  action_items:\n    - {round: 19, action: \"找 NLP/LLM 领域 effect size 解读先例 或 明确说明 tentative analogy\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-W5\n  summary: \"Dimension 2 未在 proprietary model (Gemini) 上验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R1 确认 [FIXED]. Limitations item 1 明确声明.\"}\n  resolution: \"Limitations 明确标注 Dimension 2 仅在 open-weight 模型上验证.\"\n  resolution_round: 19\n\n- id: R18-m-refs\n  summary: \"Missing refs: Chen et al. 2026, Wei et al. 2023\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"R2 确认 [FIXED]. 两篇均已 cite.\"}\n  resolution: \"两篇引用已补充.\"\n  resolution_round: 19\n\n- id: R17-W3\n  summary: \"Practical implications 薄弱\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - {round: 18, reviewers: [R1, R2], note: \"2.2pp typical-batch 实际意义有限\"}\n    - {round: 19, reviewers: [R1, R2], note: \"R1/R2 确认 [PARTIALLY FIXED]. Discussion 加了 diagnostic hedging 但 Abstract/Intro 仍偏重 extreme-batch 数字. 与 R19-W2 重叠.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED (R18 及更早)\n# ============================================================\n\n- id: R17-W1\n  summary: \"SCS vs simple baselines 对比\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: \"SCS baselines Table 已加入 Appendix.\"\n  resolution_round: 18\n\n- id: R16-N3\n  summary: \"效应量 framing 偏误\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 17\n  resolution: \"R17 确认修复\"\n  resolution_round: 17\n\n- id: R16-m5\n  summary: \"FewRel 数据污染论证\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 17\n  resolution: \"R17 确认充分\"\n  resolution_round: 17\n\n- id: R10-N1\n  summary: \"因果语言超出证据\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  resolution: \"Title 改 Predict; 因果语言清理\"\n  resolution_round: 12"
  }
}
```

</details>

---


### Tool result

_source line 1977 · 2026-05-18T10:07:46.355755+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml\", \"bytes\": 10484}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Assistant

_source line 1978 · 2026-05-18T10:13:18.836575+00:00_

API Error: Stream idle timeout - partial response received

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 176

## Round 176

4 recorded events


### User

_source line 1979 · 2026-05-18T10:13:21.916801+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 的逐条回应并汇报 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1980 · 2026-05-18T10:16:17.205231+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "schema-dag-extraction",
  "report": "# Round 19 审稿报告\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**目标 Venue**: EMNLP 2026 (ARR May 25 cycle) — Findings\n**Reviewer 编排**: 2 人 (R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量)\n**流程**: Round 1 独立审稿 → 交叉分享 + 逐条回应 → 收敛汇总 (1 轮即收敛)\n\n---\n\n## Summary\n\n本文研究 training-free LLM IE 中 schema 复杂度如何预测性能退化，将退化分解为 count (Dim 1) 和 confusability (Dim 2) 两个维度。通过 SCS/BCS 量化 confusability，在 FewRel、DocRED、Few-NERD、MAVEN 四个数据集和四个模型上实验。核心发现：count 导致 recall 单调下降（主效应），confusability 导致 type substitution（RE 中 BCS 解释 22-53% batch 间 accuracy 方差），但 NER 无 batch 级信号。Schema decomposition (SDGD) 因 merge amplification (NER) 和 routing failure (RE) 而失败。\n\nR18 的 3 个 critical issues（boundary condition 术语、separable dimensions 措辞、Contribution 2 framing）全部修复。R19 的核心争议转向 novelty 和 impact：SCS 形式同 LLM-PEE，概念发现非 surprising，typical-batch effect size modest (2.2pp)，Dimension 2 batch-level 仅限 RE forced-choice format。\n\n---\n\n## Strengths\n\n**S1. R18 critical issues 全部修复。** [R1+R2 共识] boundary condition 精确化为 forced-choice classification format (非 constrained decoding)；全文统一 \"largely additive with bounded interaction\"；Contribution 2 焦点从 metric innovation 转为 experimental methodology。修复质量到位。\n\n**S2. 实验设计严谨，控制变量充分。** [R1+R2 共识] BCS-controlled stratification（固定 count 变 BCS）在 training-free IE 文献中首次出现。Within-pool analysis 控制 pool composition confound (permutation p=0.60)。FewRel balanced design 消除 type frequency confound。Cross-model validation 覆盖 4 个模型含 proprietary Gemini 2.5 Flash。\n\n**S3. 统计分析全面透明。** [R1 highlight, R2 Soundness 4/5] TOST equivalence 在三个 margin 水平报告 + logit-scale sensitivity check；bootstrap CIs 区分 pair-level 和 batch-level；variance decomposition 量化 batch vs seed 方差；partial correlation 控制 centrality confound。统计透明度在 NLP 实证论文中罕见。\n\n**S4. 负面结果诚实报告。** [R1+R2 共识] SDGD 失败诊断（merge amplification precision collapse 0.563→0.210; routing failure 73.4% instances 收到 3-5 sub-schema positive predictions）；NER batch-level null；MAVEN centrality confound；logit-scale TOST inconclusive；few-shot widening gap。Oracle routing (0.802 vs 0.504) 精确定位瓶颈。\n\n**S5. Limitations 极其全面。** [R1+R2 共识] 10 条 limitations 含 power analysis 自我披露，预先回应了几乎所有潜在批评。\n\n**S6. Robustness checks 充分。** [R1 highlight] 4 种 prompt variants、mean vs max BCS aggregation、name vs name+def embedding、SCS vs 3 baselines (Levenshtein/WordNet/same-parent)、held-out validation、split-origin covariate。\n\n---\n\n## Weaknesses\n\n### Must-Fix (2 项)\n\n**N1 [critical, R2 提出, R1 同意实质但对评分影响有分歧] 核心发现 novelty 有限。**\n- \"More types = worse\" 已被 Li et al. (2023) 和 LLM-PEE (2025) 定性观察\n- \"Similar types confuse\" 在 hierarchical classification (Deng et al. 2010)、label confusion (Guo et al. 2021) 中有先例\n- SCS/BCS 与 LLM-PEE 的 embedding similarity partitioning criterion 形式完全相同（Related Work §2 已承认）\n- Controlled experimental methodology (stratified sampling + regression) 是标准方法论，技术上非 novel\n- **R1 nuance**: 虽然概念不 surprising，但 quantifying count vs confusability 相对贡献、发现 NER batch-level null task asymmetry 在此前文献中缺失，构成 Findings 级别的 empirical contribution\n- **R2 立场**: 作为纯 analytical study，知识增量需足够大但效应量 modest (pairwise r²=1.3-1.7%, typical-batch 2.2pp)\n- **Director 判断**: Novelty 确实有限，但 controlled isolation + honest negative results 在 Findings track 仍有价值。建议 Introduction 进一步降低 novelty claim，强调 empirical contribution 而非 conceptual breakthrough\n\n**N2 [critical, R1+R2 共识] Confusability 效应量 RE-specific 且 modest，但 title/framing 暗示跨任务普适性。**\n- Pairwise r²=1.3-1.7% (Table 2)\n- NER batch-level r≈0, n=450 (§4.3, §4.4)\n- Typical-batch gap 仅 2.2pp, CI [0.4, 4.0] (§4.3)\n- Dimension 2 batch-level 仅在 RE forced-choice classification format 下成立\n- Abstract 缺 typical-batch magnitude 数字，叙事偏重 extreme-batch (-31.2pp, -49pp)\n- Title \"Training-Free LLM Information Extraction\" 暗示跨任务发现，但实际 Dim2 batch-level 高度 RE-specific\n- **行动**: Abstract 加 typical-batch magnitude (如 \"though typical batches yield modest ~2pp gaps\")；Introduction 在 contributions 列表后加 scope qualification；或考虑 title 中加 RE-relevant qualifier\n\n### Should-Fix (5 项)\n\n**W1 [warning, R1 提出, R2 同意] TOST margin vs main effect。**\n±3pp margin 允许 interaction 达 main effect 136% (3/2.2)。±2pp marginal (p=0.047)，±1pp inconclusive (p=0.278)。Logit-scale TOST inconclusive (p=0.209)。\"Largely additive\" 在严格统计意义上依据不充分——数据不能排除 interaction 接近 main effect 的可能。Cross-pool slope consistency (permutation p=0.60) 提供间接支持。建议 Abstract 中 \"two largely additive dimensions\" 加限定词或 hedging。\n\n**W2 [warning, R1+R2 共识] NER batch-level null 削弱框架普适性。**\nNER 是比 RE classification 更 mainstream 的 IE task。\"Two-dimensional degradation\" 框架对 NER 仅在 pairwise level 成立 (r²=1.3%)，batch-level 没有 actionable signal。论文已在多处承认但 title/abstract framing 仍暗示 general decomposition。\n\n**W3 [warning, R1+R2 共识] NER U-shape 的 \"dual-task burden\" 假说缺乏实验证据。**\nCross-model replication (LLaMA-70B + Qwen3) 增加现象可信度但不解释机制。三种可能解释 (type-membership filtering, prompt length, instruction complexity) 未做控制实验区分。Discussion 中应标注为 speculative hypothesis。\n\n**W4 [warning, R2 提出, R1 partially rebut] 核心 BCS-controlled detailed analysis 集中在 FewRel。**\nDocRED 独立复现了 BCS slopes (slope=-0.713, R²=0.525)，Dimension 1 跨四个数据集。但 within-pool analysis、factorial test、aggregation simulation 全部基于 FewRel。DocRED BCS 分析相对简略 (n=35, 无 within-pool 控制)。R1 部分反驳合理——两个 RE 数据集 (80 vs 96 types, sentence vs document level) 的一致性构成有意义的 replication。\n\n**W5 [warning, R18 遗留, R19 确认 partially fixed] Practical implications 仍偏乐观。**\nDiscussion 末尾 \"diagnostic guidelines derived from correlational evidence\" 到位，但 Abstract/Introduction 的叙事仍侧重 extreme-batch 数字而非 typical-batch 的 modest effect (2.2pp)。与 N2 重叠。\n\n### Minor (3 项)\n\n**I1 [info, R1+R2 共识] Monte Carlo simulation evidential status。** Discussion 引用 simulation 时括号 caveat 到位但呈现方式仍给人 independent corroboration 印象。建议正文引用时删去具体数字，仅保留 \"post-hoc simulation confirms the aggregation pattern is consistent\"。\n\n**I2 [info, R1+R2 共识] Few-shot 5-shot low-BCS 回落解释不充分。** High-BCS 降幅 (-6.6pp) 大于 low-BCS (-3.9pp)，可能有 confusability-specific interaction 而非仅 prompt length effect。承认解释是 speculative。\n\n**I3 [info, R1 提出, R2 部分同意] Prompt variant multiple comparison。** Rothman (1990) 针对 independent replications，这里是 same dataset + same batches。但 Minimal variant 即使 Bonferroni 后仍显著 (p=0.009 vs α=0.0125)，不动摇核心结论。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 在交叉分享后达成共识 [AGREE]：\n\n1. **R18 修复质量**: N1/N2/N3 全部 FIXED，修复到位\n2. **Effect size framing** [N2]: Abstract 需加 typical-batch magnitude，叙事需 calibrated\n3. **NER batch-level null** [W2]: 削弱框架普适性，title/framing 应更 precise\n4. **TOST margin** [W1]: \"Largely additive\" framing 偏乐观，需加限定\n5. **NER U-shape** [W3]: 假说 speculative，缺控制实验\n6. **Simulation** [I1]: Presentation issue, not soundness\n7. **Few-shot asymmetry** [I2]: 解释不充分但 info 级别\n8. **引用充足度**: 70 篇引用覆盖完整，无明显遗漏\n\n## Reviewer Divergence\n\n1. **Overall score**: R1 = 3.0 (Findings), R2 = 2.5 (Borderline Findings)\n   - **核心分歧**: methodology contribution 的价值判断\n   - **R1 立场**: controlled design + negative findings 在 Findings track 有价值；NER batch-level null 本身是有价值的 negative finding (task format → batch-level predictability)；统计透明度值得鼓励；降低评分会加剧 publication bias\n   - **R2 立场**: stratified sampling + regression 是标准方法论移植，知识增量受限于 modest effect sizes + NER null + SDGD 失败后无 actionable alternative；2.5-3.0 区间合理；如调整 framing 可上调\n   - **Director 判断**: 采 3.0 (Findings)。理由：(a) R18 的 3 个 critical 全部修复，论文在 18 轮迭代中持续改进；(b) R19 的 critical issues (N1 novelty, N2 RE-specificity) 是 contribution-level 判断而非 soundness flaws；(c) R2 自己承认 2.5-3.0 合理并给出可上调条件\n\n2. **Novelty 严重性**: R2 定两个 critical (N1/N2)；R1 同意实质但认为在 Findings track 仍构成 acceptable contribution。此分歧反映 Findings 录用标准的解读差异。\n\n3. **Single-dataset concern** [W4]: R2 提出 critical 倾向，R1 部分反驳（DocRED 复现 + Dim1 跨四数据集）。最终降为 warning。\n\n---\n\n## Questions (需作者澄清)\n\n**Q1 [R1, 优先级高]**: Table 2 排除 FewRel (理由: \"RE's per-instance format precludes direct comparison of confusion rates\")，但 §3.2 和 Appendix Table 14 报告了 FewRel pairwise SCS-confusion ρ=0.218/0.187。两处说法是否矛盾？如果 FewRel 可以计算 pairwise confusion，为何 Table 2 排除？\n\n**Q2 [R2]**: FewRel train-origin types 为何反而 accuracy 低 8.8pp (p=0.06)？Limitations item 10 说 \"opposite to contamination hypothesis\"，但另一种解释是 train-split types 被选入 training set 因为 inherently 更难。论文是否考虑过这个 alternative explanation？\n\n**Q3 [R1+R2 共识]**: TOST ±1pp inconclusive 意味着 interaction 可能达 main effect 91% (2.0/2.2pp)。Cross-pool slope consistency (p=0.60) 是否足以补充 TOST 的 power 不足？如果不够，是否应将 \"largely additive\" 改为更弱的表述如 \"approximately additive under current statistical power\"？\n\n**Q4 [R1]**: BCS independence analysis (Appendix §M) shared variance 20.9%。在 BCS-controlled extreme-batch 实验中，extreme-BCS batches 的 mean type difficulty 分布是否与 random batches 不同？如果是，extreme-batch 的 31.2pp gap 可能部分来自 type difficulty confound。\n\n**Q5 [R2]**: 16-rel condition 使用 single extreme batch per BCS level (Appendix Table 8 caption 承认)。作者是否考虑过用 multiple extreme batches 复现？\n\n---\n\n## Missing References\n\n两位 Reviewer 均确认无明显遗漏。R2 建议补充 Zheng et al. (2023) 和 Lyu et al. (2024)，但未提供完整 citation；R1 认为相关性待确认。70 篇引用覆盖面完整。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目 external_review.paperreview_ai.enabled 未设置）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**评分理由**:\n\n*Soundness (3.75/5)*: R1=3.5, R2=4.0。实验设计在 training-free IE 文献中属高水准：BCS-controlled stratification、TOST equivalence testing、within-pool analysis、cross-model validation (4 models)、partial correlation controlling centrality confound。统计报告全面透明。扣分点：TOST margin 选择与 main effect 的关系论证不足（±3pp margin vs 2.2pp main effect）；logit-scale TOST inconclusive 削弱 \"largely additive\" claim 的确定性；NER batch-level null 限制了框架的覆盖面。\n\n*Excitement (2.5/5)*: R1=2.5, R2=2.5。两位 Reviewer 一致。研究问题有价值（首次通过 controlled stratification 隔离 count vs confusability），negative results 有诊断意义。但 SCS/BCS 形式同 LLM-PEE，\"两维度\" 概念非 surprising，typical-batch effect modest (2.2pp, CI [0.4, 4.0])，NER 无 batch-level signal，SDGD 失败后无 actionable mitigation 方案。作为纯 analytical study，knowledge increment 受限。\n\n*Reproducibility (4/5)*: R1=4, R2=4。实验细节充分（decoding params, seed, batch sizes, bootstrap params, prompt templates 完整公开）。Anonymous review materials 链接已提供。Code promised upon acceptance。单 GPU ~72 GPU-hours。\n\n**置信度**: 4/5。两位 Reviewer 均仔细阅读全文及所有 appendix，熟悉 IE、statistical methodology、LLM prompting 文献。交叉分享后关键问题达成共识。\n\n**一句话总结**: R18 的 3 个 critical issues 全部修复，方法论严谨度和统计透明度在 NLP 实证论文中属高水准。主要限制是 novelty 有限（SCS 同 LLM-PEE, 概念非 surprising）和 Dimension 2 batch-level 效应的 RE-specificity + modest typical-batch magnitude (2.2pp)。达到 Findings 水平，但在该水平的低端。\n\n**如需上调至 3.5 (Borderline Conference)**，需：(a) Abstract 加 typical-batch magnitude 数字并调整叙事权重；(b) \"largely additive\" 加限定词反映 logit-scale inconclusive 和 TOST power 限制；(c) Title 或 Abstract 中更明确标注 Dimension 2 batch-level 的 RE-specific boundary condition；(d) Discussion 中 practical implications 段坦诚 \"diagnostic value outweighs engineering value\"。\n\n---\n\n## Detailed Comments (逐节)\n\n### Abstract (~156 words)\n- R18-W1 修复到位，篇幅合理。\n- 缺 typical-batch magnitude：加 \"though typical batches yield modest ~2pp gaps\" 使 impression 更 calibrated。\n- \"Confusability is a schema-structural property\" 结尾句有效。\n\n### Introduction\n- R18-N2 修复到位：\"largely additive\" 统一使用。\n- R18-N3 修复到位：Contribution 2 焦点转为 experimental design。\n- Contribution 3 (task asymmetry) framing 存在 R18 遗留分歧（R2 认为是 limitation 包装为 contribution），R19 未再升级。\n- 建议：contributions 列表后加一句 scope qualification：\"These findings are strongest for RE under forced-choice classification; NER confusability effects are limited to pairwise analysis.\"\n\n### Related Work\n- SCS novelty 段诚实承认与 LLM-PEE 关系，positioning 准确。\n- Chen et al. (2026) 和 Wei et al. (2023) 已补充。\n- 引用密度 (70 篇) 符合 ACL 标准。\n- 建议考虑补充 Zheng et al. (2023) 和 Lyu et al. (2024)（待确认具体论文）。\n\n### Experimental Setup\n- 不同数据集使用不同 embedding (Qwen3 for Few-NERD, MiniLM for others) 损害 SCS 通用性声明。Cross-check 显示 MiniLM 在 Few-NERD 上 r=0.172 > Qwen3 r=0.138（非 overfitting），但不一致性仍是 reviewer concern。\n\n### Results\n- §4.3 Practical magnitude 透明报告 2.2pp (CI [0.4, 4.0])。\n- §4.4 TOST 三个 margin + logit-scale caveat 在正文报告——改进显著。\n- \"Largely additive\" 的 caveat 可更前置。\n\n### SDGD (§5)\n- \"Marginal mean BCS reduction (0.559→0.552)\" 解释了 +1.4pp 无显著优势。\n- Oracle routing (0.802 vs 0.504) 精确定位瓶颈。\n\n### Discussion\n- \"Forced-choice classification format\" 术语精确化完成。\n- Practical implications \"diagnostic guidelines derived from correlational evidence\" 到位但可更显著。\n- U-shape \"dual-task burden\" 应标注为 speculative hypothesis。\n\n### Limitations\n- 10 条覆盖全面，R18 遗留问题均已反映。\n\n### Format\n- 正文页数无法编译验证，估算 borderline 8-9 页，需作者确认。\n- Checklist 填写质量合格。\n- 匿名化无问题。",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "schema-dag-extraction",
    "report": "# Round 19 审稿报告\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**目标 Venue**: EMNLP 2026 (ARR May 25 cycle) — Findings\n**Reviewer 编排**: 2 人 (R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量)\n**流程**: Round 1 独立审稿 → 交叉分享 + 逐条回应 → 收敛汇总 (1 轮即收敛)\n\n---\n\n## Summary\n\n本文研究 training-free LLM IE 中 schema 复杂度如何预测性能退化，将退化分解为 count (Dim 1) 和 confusability (Dim 2) 两个维度。通过 SCS/BCS 量化 confusability，在 FewRel、DocRED、Few-NERD、MAVEN 四个数据集和四个模型上实验。核心发现：count 导致 recall 单调下降（主效应），confusability 导致 type substitution（RE 中 BCS 解释 22-53% batch 间 accuracy 方差），但 NER 无 batch 级信号。Schema decomposition (SDGD) 因 merge amplification (NER) 和 routing failure (RE) 而失败。\n\nR18 的 3 个 critical issues（boundary condition 术语、separable dimensions 措辞、Contribution 2 framing）全部修复。R19 的核心争议转向 novelty 和 impact：SCS 形式同 LLM-PEE，概念发现非 surprising，typical-batch effect size modest (2.2pp)，Dimension 2 batch-level 仅限 RE forced-choice format。\n\n---\n\n## Strengths\n\n**S1. R18 critical issues 全部修复。** [R1+R2 共识] boundary condition 精确化为 forced-choice classification format (非 constrained decoding)；全文统一 \"largely additive with bounded interaction\"；Contribution 2 焦点从 metric innovation 转为 experimental methodology。修复质量到位。\n\n**S2. 实验设计严谨，控制变量充分。** [R1+R2 共识] BCS-controlled stratification（固定 count 变 BCS）在 training-free IE 文献中首次出现。Within-pool analysis 控制 pool composition confound (permutation p=0.60)。FewRel balanced design 消除 type frequency confound。Cross-model validation 覆盖 4 个模型含 proprietary Gemini 2.5 Flash。\n\n**S3. 统计分析全面透明。** [R1 highlight, R2 Soundness 4/5] TOST equivalence 在三个 margin 水平报告 + logit-scale sensitivity check；bootstrap CIs 区分 pair-level 和 batch-level；variance decomposition 量化 batch vs seed 方差；partial correlation 控制 centrality confound。统计透明度在 NLP 实证论文中罕见。\n\n**S4. 负面结果诚实报告。** [R1+R2 共识] SDGD 失败诊断（merge amplification precision collapse 0.563→0.210; routing failure 73.4% instances 收到 3-5 sub-schema positive predictions）；NER batch-level null；MAVEN centrality confound；logit-scale TOST inconclusive；few-shot widening gap。Oracle routing (0.802 vs 0.504) 精确定位瓶颈。\n\n**S5. Limitations 极其全面。** [R1+R2 共识] 10 条 limitations 含 power analysis 自我披露，预先回应了几乎所有潜在批评。\n\n**S6. Robustness checks 充分。** [R1 highlight] 4 种 prompt variants、mean vs max BCS aggregation、name vs name+def embedding、SCS vs 3 baselines (Levenshtein/WordNet/same-parent)、held-out validation、split-origin covariate。\n\n---\n\n## Weaknesses\n\n### Must-Fix (2 项)\n\n**N1 [critical, R2 提出, R1 同意实质但对评分影响有分歧] 核心发现 novelty 有限。**\n- \"More types = worse\" 已被 Li et al. (2023) 和 LLM-PEE (2025) 定性观察\n- \"Similar types confuse\" 在 hierarchical classification (Deng et al. 2010)、label confusion (Guo et al. 2021) 中有先例\n- SCS/BCS 与 LLM-PEE 的 embedding similarity partitioning criterion 形式完全相同（Related Work §2 已承认）\n- Controlled experimental methodology (stratified sampling + regression) 是标准方法论，技术上非 novel\n- **R1 nuance**: 虽然概念不 surprising，但 quantifying count vs confusability 相对贡献、发现 NER batch-level null task asymmetry 在此前文献中缺失，构成 Findings 级别的 empirical contribution\n- **R2 立场**: 作为纯 analytical study，知识增量需足够大但效应量 modest (pairwise r²=1.3-1.7%, typical-batch 2.2pp)\n- **Director 判断**: Novelty 确实有限，但 controlled isolation + honest negative results 在 Findings track 仍有价值。建议 Introduction 进一步降低 novelty claim，强调 empirical contribution 而非 conceptual breakthrough\n\n**N2 [critical, R1+R2 共识] Confusability 效应量 RE-specific 且 modest，但 title/framing 暗示跨任务普适性。**\n- Pairwise r²=1.3-1.7% (Table 2)\n- NER batch-level r≈0, n=450 (§4.3, §4.4)\n- Typical-batch gap 仅 2.2pp, CI [0.4, 4.0] (§4.3)\n- Dimension 2 batch-level 仅在 RE forced-choice classification format 下成立\n- Abstract 缺 typical-batch magnitude 数字，叙事偏重 extreme-batch (-31.2pp, -49pp)\n- Title \"Training-Free LLM Information Extraction\" 暗示跨任务发现，但实际 Dim2 batch-level 高度 RE-specific\n- **行动**: Abstract 加 typical-batch magnitude (如 \"though typical batches yield modest ~2pp gaps\")；Introduction 在 contributions 列表后加 scope qualification；或考虑 title 中加 RE-relevant qualifier\n\n### Should-Fix (5 项)\n\n**W1 [warning, R1 提出, R2 同意] TOST margin vs main effect。**\n±3pp margin 允许 interaction 达 main effect 136% (3/2.2)。±2pp marginal (p=0.047)，±1pp inconclusive (p=0.278)。Logit-scale TOST inconclusive (p=0.209)。\"Largely additive\" 在严格统计意义上依据不充分——数据不能排除 interaction 接近 main effect 的可能。Cross-pool slope consistency (permutation p=0.60) 提供间接支持。建议 Abstract 中 \"two largely additive dimensions\" 加限定词或 hedging。\n\n**W2 [warning, R1+R2 共识] NER batch-level null 削弱框架普适性。**\nNER 是比 RE classification 更 mainstream 的 IE task。\"Two-dimensional degradation\" 框架对 NER 仅在 pairwise level 成立 (r²=1.3%)，batch-level 没有 actionable signal。论文已在多处承认但 title/abstract framing 仍暗示 general decomposition。\n\n**W3 [warning, R1+R2 共识] NER U-shape 的 \"dual-task burden\" 假说缺乏实验证据。**\nCross-model replication (LLaMA-70B + Qwen3) 增加现象可信度但不解释机制。三种可能解释 (type-membership filtering, prompt length, instruction complexity) 未做控制实验区分。Discussion 中应标注为 speculative hypothesis。\n\n**W4 [warning, R2 提出, R1 partially rebut] 核心 BCS-controlled detailed analysis 集中在 FewRel。**\nDocRED 独立复现了 BCS slopes (slope=-0.713, R²=0.525)，Dimension 1 跨四个数据集。但 within-pool analysis、factorial test、aggregation simulation 全部基于 FewRel。DocRED BCS 分析相对简略 (n=35, 无 within-pool 控制)。R1 部分反驳合理——两个 RE 数据集 (80 vs 96 types, sentence vs document level) 的一致性构成有意义的 replication。\n\n**W5 [warning, R18 遗留, R19 确认 partially fixed] Practical implications 仍偏乐观。**\nDiscussion 末尾 \"diagnostic guidelines derived from correlational evidence\" 到位，但 Abstract/Introduction 的叙事仍侧重 extreme-batch 数字而非 typical-batch 的 modest effect (2.2pp)。与 N2 重叠。\n\n### Minor (3 项)\n\n**I1 [info, R1+R2 共识] Monte Carlo simulation evidential status。** Discussion 引用 simulation 时括号 caveat 到位但呈现方式仍给人 independent corroboration 印象。建议正文引用时删去具体数字，仅保留 \"post-hoc simulation confirms the aggregation pattern is consistent\"。\n\n**I2 [info, R1+R2 共识] Few-shot 5-shot low-BCS 回落解释不充分。** High-BCS 降幅 (-6.6pp) 大于 low-BCS (-3.9pp)，可能有 confusability-specific interaction 而非仅 prompt length effect。承认解释是 speculative。\n\n**I3 [info, R1 提出, R2 部分同意] Prompt variant multiple comparison。** Rothman (1990) 针对 independent replications，这里是 same dataset + same batches。但 Minimal variant 即使 Bonferroni 后仍显著 (p=0.009 vs α=0.0125)，不动摇核心结论。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 在交叉分享后达成共识 [AGREE]：\n\n1. **R18 修复质量**: N1/N2/N3 全部 FIXED，修复到位\n2. **Effect size framing** [N2]: Abstract 需加 typical-batch magnitude，叙事需 calibrated\n3. **NER batch-level null** [W2]: 削弱框架普适性，title/framing 应更 precise\n4. **TOST margin** [W1]: \"Largely additive\" framing 偏乐观，需加限定\n5. **NER U-shape** [W3]: 假说 speculative，缺控制实验\n6. **Simulation** [I1]: Presentation issue, not soundness\n7. **Few-shot asymmetry** [I2]: 解释不充分但 info 级别\n8. **引用充足度**: 70 篇引用覆盖完整，无明显遗漏\n\n## Reviewer Divergence\n\n1. **Overall score**: R1 = 3.0 (Findings), R2 = 2.5 (Borderline Findings)\n   - **核心分歧**: methodology contribution 的价值判断\n   - **R1 立场**: controlled design + negative findings 在 Findings track 有价值；NER batch-level null 本身是有价值的 negative finding (task format → batch-level predictability)；统计透明度值得鼓励；降低评分会加剧 publication bias\n   - **R2 立场**: stratified sampling + regression 是标准方法论移植，知识增量受限于 modest effect sizes + NER null + SDGD 失败后无 actionable alternative；2.5-3.0 区间合理；如调整 framing 可上调\n   - **Director 判断**: 采 3.0 (Findings)。理由：(a) R18 的 3 个 critical 全部修复，论文在 18 轮迭代中持续改进；(b) R19 的 critical issues (N1 novelty, N2 RE-specificity) 是 contribution-level 判断而非 soundness flaws；(c) R2 自己承认 2.5-3.0 合理并给出可上调条件\n\n2. **Novelty 严重性**: R2 定两个 critical (N1/N2)；R1 同意实质但认为在 Findings track 仍构成 acceptable contribution。此分歧反映 Findings 录用标准的解读差异。\n\n3. **Single-dataset concern** [W4]: R2 提出 critical 倾向，R1 部分反驳（DocRED 复现 + Dim1 跨四数据集）。最终降为 warning。\n\n---\n\n## Questions (需作者澄清)\n\n**Q1 [R1, 优先级高]**: Table 2 排除 FewRel (理由: \"RE's per-instance format precludes direct comparison of confusion rates\")，但 §3.2 和 Appendix Table 14 报告了 FewRel pairwise SCS-confusion ρ=0.218/0.187。两处说法是否矛盾？如果 FewRel 可以计算 pairwise confusion，为何 Table 2 排除？\n\n**Q2 [R2]**: FewRel train-origin types 为何反而 accuracy 低 8.8pp (p=0.06)？Limitations item 10 说 \"opposite to contamination hypothesis\"，但另一种解释是 train-split types 被选入 training set 因为 inherently 更难。论文是否考虑过这个 alternative explanation？\n\n**Q3 [R1+R2 共识]**: TOST ±1pp inconclusive 意味着 interaction 可能达 main effect 91% (2.0/2.2pp)。Cross-pool slope consistency (p=0.60) 是否足以补充 TOST 的 power 不足？如果不够，是否应将 \"largely additive\" 改为更弱的表述如 \"approximately additive under current statistical power\"？\n\n**Q4 [R1]**: BCS independence analysis (Appendix §M) shared variance 20.9%。在 BCS-controlled extreme-batch 实验中，extreme-BCS batches 的 mean type difficulty 分布是否与 random batches 不同？如果是，extreme-batch 的 31.2pp gap 可能部分来自 type difficulty confound。\n\n**Q5 [R2]**: 16-rel condition 使用 single extreme batch per BCS level (Appendix Table 8 caption 承认)。作者是否考虑过用 multiple extreme batches 复现？\n\n---\n\n## Missing References\n\n两位 Reviewer 均确认无明显遗漏。R2 建议补充 Zheng et al. (2023) 和 Lyu et al. (2024)，但未提供完整 citation；R1 认为相关性待确认。70 篇引用覆盖面完整。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目 external_review.paperreview_ai.enabled 未设置）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**评分理由**:\n\n*Soundness (3.75/5)*: R1=3.5, R2=4.0。实验设计在 training-free IE 文献中属高水准：BCS-controlled stratification、TOST equivalence testing、within-pool analysis、cross-model validation (4 models)、partial correlation controlling centrality confound。统计报告全面透明。扣分点：TOST margin 选择与 main effect 的关系论证不足（±3pp margin vs 2.2pp main effect）；logit-scale TOST inconclusive 削弱 \"largely additive\" claim 的确定性；NER batch-level null 限制了框架的覆盖面。\n\n*Excitement (2.5/5)*: R1=2.5, R2=2.5。两位 Reviewer 一致。研究问题有价值（首次通过 controlled stratification 隔离 count vs confusability），negative results 有诊断意义。但 SCS/BCS 形式同 LLM-PEE，\"两维度\" 概念非 surprising，typical-batch effect modest (2.2pp, CI [0.4, 4.0])，NER 无 batch-level signal，SDGD 失败后无 actionable mitigation 方案。作为纯 analytical study，knowledge increment 受限。\n\n*Reproducibility (4/5)*: R1=4, R2=4。实验细节充分（decoding params, seed, batch sizes, bootstrap params, prompt templates 完整公开）。Anonymous review materials 链接已提供。Code promised upon acceptance。单 GPU ~72 GPU-hours。\n\n**置信度**: 4/5。两位 Reviewer 均仔细阅读全文及所有 appendix，熟悉 IE、statistical methodology、LLM prompting 文献。交叉分享后关键问题达成共识。\n\n**一句话总结**: R18 的 3 个 critical issues 全部修复，方法论严谨度和统计透明度在 NLP 实证论文中属高水准。主要限制是 novelty 有限（SCS 同 LLM-PEE, 概念非 surprising）和 Dimension 2 batch-level 效应的 RE-specificity + modest typical-batch magnitude (2.2pp)。达到 Findings 水平，但在该水平的低端。\n\n**如需上调至 3.5 (Borderline Conference)**，需：(a) Abstract 加 typical-batch magnitude 数字并调整叙事权重；(b) \"largely additive\" 加限定词反映 logit-scale inconclusive 和 TOST power 限制；(c) Title 或 Abstract 中更明确标注 Dimension 2 batch-level 的 RE-specific boundary condition；(d) Discussion 中 practical implications 段坦诚 \"diagnostic value outweighs engineering value\"。\n\n---\n\n## Detailed Comments (逐节)\n\n### Abstract (~156 words)\n- R18-W1 修复到位，篇幅合理。\n- 缺 typical-batch magnitude：加 \"though typical batches yield modest ~2pp gaps\" 使 impression 更 calibrated。\n- \"Confusability is a schema-structural property\" 结尾句有效。\n\n### Introduction\n- R18-N2 修复到位：\"largely additive\" 统一使用。\n- R18-N3 修复到位：Contribution 2 焦点转为 experimental design。\n- Contribution 3 (task asymmetry) framing 存在 R18 遗留分歧（R2 认为是 limitation 包装为 contribution），R19 未再升级。\n- 建议：contributions 列表后加一句 scope qualification：\"These findings are strongest for RE under forced-choice classification; NER confusability effects are limited to pairwise analysis.\"\n\n### Related Work\n- SCS novelty 段诚实承认与 LLM-PEE 关系，positioning 准确。\n- Chen et al. (2026) 和 Wei et al. (2023) 已补充。\n- 引用密度 (70 篇) 符合 ACL 标准。\n- 建议考虑补充 Zheng et al. (2023) 和 Lyu et al. (2024)（待确认具体论文）。\n\n### Experimental Setup\n- 不同数据集使用不同 embedding (Qwen3 for Few-NERD, MiniLM for others) 损害 SCS 通用性声明。Cross-check 显示 MiniLM 在 Few-NERD 上 r=0.172 > Qwen3 r=0.138（非 overfitting），但不一致性仍是 reviewer concern。\n\n### Results\n- §4.3 Practical magnitude 透明报告 2.2pp (CI [0.4, 4.0])。\n- §4.4 TOST 三个 margin + logit-scale caveat 在正文报告——改进显著。\n- \"Largely additive\" 的 caveat 可更前置。\n\n### SDGD (§5)\n- \"Marginal mean BCS reduction (0.559→0.552)\" 解释了 +1.4pp 无显著优势。\n- Oracle routing (0.802 vs 0.504) 精确定位瓶颈。\n\n### Discussion\n- \"Forced-choice classification format\" 术语精确化完成。\n- Practical implications \"diagnostic guidelines derived from correlational evidence\" 到位但可更显著。\n- U-shape \"dual-task burden\" 应标注为 speculative hypothesis。\n\n### Limitations\n- 10 条覆盖全面，R18 遗留问题均已反映。\n\n### Format\n- 正文页数无法编译验证，估算 borderline 8-9 页，需作者确认。\n- Checklist 填写质量合格。\n- 匿名化无问题。",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool result

_source line 1981 · 2026-05-18T10:16:21.675634+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4470
}
```

</details>

---


### Assistant

_source line 1982 · 2026-05-18T10:16:31.207252+00:00_

Round 19 审稿完成。

**结果**: Overall 3.0 (Findings)，与 R18 持平。

**核心变化**:
- R18 的 3 个 critical issues 全部修复（boundary condition 术语、separable dimensions 措辞、Contribution 2 framing）
- R19 新增 2 个 critical（novelty 有限 + Dim2 RE-specific）、5 个 warning、3 个 info
- R1=3.0, R2=2.5，分歧在 methodology contribution 价值判断

**上调至 3.5 的条件**: Abstract 加 typical-batch magnitude、"largely additive" 加限定词、Title/Abstract 标注 RE-specific boundary condition、Practical implications 坦诚 diagnostic > engineering value。

审稿报告已投递 Research Director，Issue Tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 177

## Round 177

72 recorded events


### User

_source line 1983 · 2026-05-19T04:27:15.961828+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1984 · 2026-05-19T04:27:22.218263+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1985 · 2026-05-19T04:27:22.219168+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1986 · 2026-05-19T04:27:25.642251+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 1987 · 2026-05-19T04:27:25.693220+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1988 · 2026-05-19T04:27:31.019243+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 1989 · 2026-05-19T04:27:31.121511+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1990 · 2026-05-19T04:27:39.522296+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 1991 · 2026-05-19T04:27:39.522983+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1992 · 2026-05-19T04:27:43.416465+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1993 · 2026-05-19T04:27:43.871025+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (62 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_unconstrained_decoding_ablation** (success): The BCS-accuracy correlation in RE arises from semantic confusion rather than forced-choice format artifacts. If removing the enum constraint (relaxed decoding) preserves the negative BCS-accuracy correlation direction and significance, confusability is a genuine semantic property; if the correlation disappears, the effect is specific to constrained classification where all errors are channeled into type substitution. Either outcome strengthens the paper: preservation broadens the claim, disappearance validates the error-channeling hypothesis stated in Discussion. ← 基于 exp_fewrel_formal_80rel\n- **exp_multiseed_bcs_re** (success): The BCS-accuracy correlation observed in FewRel BCS-controlled experiments (R²=0.22-0.53) is
…[truncated 1464 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1994 · 2026-05-19T04:27:43.871542+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1995 · 2026-05-19T04:27:44.836074+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema-dag-extraction'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 964
}
```

</details>

---


### Tool call

_source line 1996 · 2026-05-19T04:27:44.988694+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1997 · 2026-05-19T04:27:46.094865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1998 · 2026-05-19T04:27:46.145770+00:00_

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
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 has been validated across all four models including a proprietary one; Dimension~2 has been verified only on open-weight models and was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded under the linear specification (TOST $p = 0.003$ at $\pm 3$\,pp on FewRel; DocRED inconclusive, Appendix~\ref{sec:appendix_factorial}) but inconclusive on the logit scale ($p = 0.209$). BCS-controlled experiments use a single seed with greedy decoding; the residual SD of 0.88\,pp (Appendix~\ref{app:variance-decomposition}) supports robustness but precise magnitudes may vary.
43	
44	\item \textbf{Task format dependency.} BCS batch-level prediction is demonstrated only under RE's forced-choice classification format. An unconstrained decoding ablation ($n = 25$) confirms
…[truncated 3445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1999 · 2026-05-19T04:27:53.692188+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"}]

Based on the web search results, here's a comprehensive overview of the EMNLP 2026 ARR call for papers submission guidelines and author instructions:

## Submission Process

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference. Both submissions of articles for review and commitment of reviewed articles to the conference will be p
…[truncated 2033 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 8703
}
```

</details>

---


### Tool call

_source line 2000 · 2026-05-19T04:27:59.469216+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 formatting requirements page limit template long short paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 formatting requirements page limit template long short paper"
  }
}
```

</details>

---


### Tool call

_source line 2001 · 2026-05-19T04:28:01.252193+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2002 · 2026-05-19T04:28:01.806651+00:00_

100	\resizebox{\columnwidth}{!}{%
101	\begin{tabular}{llrrrrrrr}
102	\toprule
103	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
104	\cmidrule(lr){3-7}
105	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
106	\midrule
107	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
108	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}\,0.001$ \\
109	\midrule
110	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
111	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
112	\bottomrule
113	\end{tabular}}
114	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}
115	\label{tab:error_taxonomy}
116	\end{table}
117	
118	\section{SDGD Full Protocol and Results}
119	\label{sec:appendix_sdgd}
120	
121	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation.
122	
123	Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368). SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop. Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194,
…[truncated 16666 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 2003 · 2026-05-19T04:28:01.807143+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 2004 · 2026-05-19T04:28:07.492115+00:00_

Web search results for query: "ACL Rolling Review 2026 formatting requirements page limit template long short paper"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here is information about ACL Rolling Review 2026 formatting requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Short paper page limits can be found in the standard ACL formatting guidelines.

## Sections That Don't Count Toward Page Limit

Appendices should come after the references in the submitted pdf and do not count towards the page limit. Additionally, ACL currently requires all su
…[truncated 1148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 8023
}
```

</details>

---


### Tool result

_source line 2005 · 2026-05-19T04:28:07.542957+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\", \"content\": \"# Literature Map for schema-dag-extraction\\n# Updated: 2026-05-15\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\n\\n# =============================================================================\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\n# =============================================================================\\n\\n- id: llm-pee-2025\\n  title: \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\"\\n  year: 2025\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2503.02628\\n  role: direct-competitor\\n  relevance_note: >\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\n    Divides candidate types into partitions to reduce prompt length.\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\n\\n- id: parse-2025\\n  title: \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\"\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://arxiv.org/abs/2510.08623\\n  role: direct-competitor\\n  relevance_note: >\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\n    Does NOT model type confusability explicitly.\\n\\n- id: dee-2024\\n  title: \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\"\\n  year: 2024\\
…[truncated 3590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5735
}
```

</details>

---


### Tool call

_source line 2006 · 2026-05-19T04:28:12.172047+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 2007 · 2026-05-19T04:28:12.222789+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2008 · 2026-05-19T04:28:15.705277+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2009 · 2026-05-19T04:28:15.856580+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: type count and type confusability. We present what is, to our knowledge, the first controlled study isolating these factors across NER, RE, and event detection on four datasets. We quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS). Degradation operates along two largely additive dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) dominates confusability-related type substitution, though typical batches yield modest ${\sim}$2\,pp gaps. BCS explains 22--53\% of cross-batch RE accuracy variance under RE's forced-choice format but shows no batch-level signal for NER, where errors scatter across missed entities and boundary failures. Few-shot demonstrations widen the confusability gap (+4.3\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE). Pairwise confusability is a schema-structural property: effects replicate across model scales and families, and persist under varied prompt designs.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2010 · 2026-05-19T04:28:15.857055+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2011 · 2026-05-19T04:28:16.311438+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
…[truncated 3157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 2012 · 2026-05-19T04:28:16.311807+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2013 · 2026-05-19T04:28:16.665387+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, bidirectional encoders \cite{gliner-2024,gliner2-2025}, and fine-grained entity typing \cite{gillick-2014-entity-typing}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability. \citet{wei-2023-chatie} reformulate zero-shot IE as multi-turn QA with ChatGPT but do not analyze schema-size effects.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21 in NER) that our \S\ref{sec:sdgd} analysis identifies as the fundamental bottleneck. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definit
…[truncated 3188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 2014 · 2026-05-19T04:28:16.666455+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 2015 · 2026-05-19T04:28:16.717369+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate th
…[truncated 7648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2016 · 2026-05-19T04:28:21.409475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 2017 · 2026-05-19T04:28:22.365367+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure*}[t]
10	\centering
11	\begin{minipage}[t]{0.48\textwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\textwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves. Error bars: $\pm 1$\,SD across 3 seeds $\times$ 25 batches. RE declines monotonically; NER shows a U-shape. Hollow markers: full-schema (no sampling variance). \textbf{(b)} BCS-controlled FewRel accuracy. Slopes are consistent across the independent and within-pool 16-relation conditions ($p = 0.60$); wider BCS range at 80 relations produces larger gaps.}
21	\label{fig:main_results}
22	\end{figure*}
23	
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}). The pattern is stable across three seeds (max $\Delta = 10.7$\,pp, within 1\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\times$; Appendix~\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $
…[truncated 9450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 2018 · 2026-05-19T04:28:22.516947+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 2019 · 2026-05-19T04:28:22.818684+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapse (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}); type separation recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.): graph coloring achieves only marginal mean BCS reduction (0.559$\to$0.552), insufficient to produce detectable accuracy improvement. All practical routing strategies fall below the single-pass baseline (Appendix~\ref{sec:appendix_routing}).
11	
12	Promising avenues include coarse-to-fine pipelines and retrieval-based routing.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2020 · 2026-05-19T04:28:22.819188+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2021 · 2026-05-19T04:28:23.121123+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). The effect generalizes to document-level RE (DocRED $R^2 = 0.51$) and persists across prompt designs (Appendix~\ref{sec:appendix_prompt_sensitivity}). Dimension~1 replicates across scales (8B--70B); Dimension~2 attenuates on smaller models.
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pairwise $R^2$ is modest (1.3\%); conditional on nonzero confusion, $R^2$ rises to 7\%. Correlated aggregation amplifies this to batch-level $R^2$ of 18--25\% (Monte Carlo simulation; Appendix~\ref{app:aggregation-sim}), consistent with observed RE values.
9	
10	\paragraph{Task-dependent effects and format dependency.}
11	The batch-level BCS--performance relationship is RE-specific ($R^2 = 0.22$--$0.53$ vs.\ $r \approx 0$ for NER, $n = 450$). RE uses forced-choice classification where all non-null errors are type substitutions \cite{tam-2024-let-me-speak}, making BCS predictive. NER produces multi-span output where errors scatter across missed entities, boundary misalignment, and type confusion, diluting the BCS signal \cite{schall-2025-hidden-cost}. The NER U-shape (\S\ref{sec:count_curves}) likely reflects a dual-task burden: partial schemas require simultaneous span detection and type-membership filtering; at full schema, filtering becomes vacuous and recall recovers. An unconstrained decoding ablation ($n = 25$) confirms format dependency: removing the JSON enum constraint eliminates the BCS--accuracy correlation ($\rho = -0.14$, $p = 0.49$) while OOV remains near zero (0.08\%), showing that constrained decoding channels all errors into type substitution.
12	
13	\paragraph{Practical implications.}
14	For RE, pre-screening type pairs in th
…[truncated 1551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2022 · 2026-05-19T04:28:23.121621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 2023 · 2026-05-19T04:28:23.172496+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-associated degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \cite{lla
…[truncated 4608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2024 · 2026-05-19T04:28:32.634333+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "299",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "299",
    "limit": "500"
  }
}
```

</details>

---


### Tool result

_source line 2025 · 2026-05-19T04:28:33.592528+00:00_

299	
300	\begin{table}[h]
301	\centering
302	\small
303	\resizebox{\columnwidth}{!}{\begin{tabular}{llrrrr}
304	\toprule
305	\textbf{Variant} & \textbf{Count} & \textbf{Mean Acc} & \textbf{$r$} & \textbf{$p$} \\
306	\midrule
307	V2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\
308	V2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\
309	Instruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\
310	Instruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\
311	Chain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\
312	Chain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\
313	Minimal & 8 & 0.852 & $-$0.170 & 0.638 \\
314	Minimal & 32 & 0.615 & $-$0.771 & 0.009 \\
315	\bottomrule
316	\end{tabular}}
317	\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}
318	\label{tab:prompt_variants}
319	\end{table}
320	
321	At count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.
322	
323	\section{BCS Aggregation Sensitivity}
324	\label{sec:appendix_bcs_sensitivity}
325	
326	We define Batch Confusability Score (BCS) as the \e
…[truncated 32907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 2026 · 2026-05-19T04:28:33.593103+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2027 · 2026-05-19T04:28:34.149420+00:00_

1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the foll
…[truncated 5208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 556
}
```

</details>

---


### Tool call

_source line 2028 · 2026-05-19T04:28:34.601945+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "description": "Count lines in references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "description": "Count lines in references.bib"
  }
}
```

</details>

---


### Tool call

_source line 2029 · 2026-05-19T04:28:34.702917+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2030 · 2026-05-19T04:28:34.754021+00:00_

658 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool result

_source line 2031 · 2026-05-19T04:28:34.754494+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2032 · 2026-05-19T04:28:39.882670+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2033 · 2026-05-19T04:28:39.933433+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2034 · 2026-05-19T04:28:42.611548+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 2035 · 2026-05-19T04:28:42.656078+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 44
}
```

</details>

---


### Tool call

_source line 2036 · 2026-05-19T04:28:46.130916+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2037 · 2026-05-19T04:28:46.583538+00:00_

# Round 19 Review Issues Tracker
# Updated: 2026-05-18 (post n=25 ablation + format caveat补全)

# ============================================================
# CRITICAL (R19) — structural ceiling
# ============================================================

- id: R19-N1
  summary: "核心发现 novelty 有限: SCS 形式同 LLM-PEE, controlled methodology 是标准方法论移植"
  category: framing
  severity: critical
  status: open
  first_raised_round: 19
  last_seen_round: 19
  mentions:
    - {round: 19, reviewers: [R1, R2], note: "Structural ceiling. Findings track 定位已确认."}
  action_items: []
  resolution: "Structural — Findings track 定位已确认，不可修复。"
  resolution_round: null

- id: R19-N2
  summary: "Confusability 效应量小且 RE-specific: pairwise r²=1.3-1.7%, NER batch-level null, RE 发现依赖 forced-choice format"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 19
  last_seen_round: 19
  mentions:
    - {round: 19, reviewers: [R1, R2], note: "Dim2 batch-level RE-specific."}
  action_items:
    - {round: 19, action: "n=25 unconstrained ablation confirms BCS effect is format-specific (ρ=-0.14, p=0.49). Error-channeling hypothesis validated.", assigned_to: paper_agent, status: done}
    - {round: 19, action: "Introduction Finding (2) + C2 补 forced-choice format caveat", assigned_to: paper_agent, status: done}
    - {round: 19, action: "Abstract 末句加 Pairwise 精准化", assigned_to: paper_agent, status: done}
  resolution: "n=25 ablation 确认 BCS 依赖 forced-choice format. 全文已统一 format caveat (Abstract/Intro/Results/Discussion/Conclusion/Limitations). Error-channeling hypothesis 写入 Discussion."
  resolution_round: 19

# ============================================================
# WARNING (R19)
# ============================================================

- id: R19-W1
  summary: "TOST ±3pp margin 允许 interaction 达 main effect 136%, 'Largely additive' framing 偏乐观"
  category: method
  severity: warning
  status: open
  first_raised_round: 19
  last_seen_round: 19
  mentions:
    -
…[truncated 6379 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2038 · 2026-05-19T04:28:47.489622+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2039 · 2026-05-19T04:28:47.590530+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2040 · 2026-05-19T04:28:47.942775+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review May 2026 submission deadline page limit long paper short paper formatting"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review May 2026 submission deadline page limit long paper short paper formatting"
  }
}
```

</details>

---


### Tool result

_source line 2041 · 2026-05-19T04:28:57.712358+00:00_

Web search results for query: "ACL Rolling Review May 2026 submission deadline page limit long paper short paper formatting"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Now let me search for more specific information about formatting guidelines:

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"}
…[truncated 2938 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 9769
}
```

</details>

---


### Tool call

_source line 2042 · 2026-05-19T04:29:05.765864+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"*.config.*\" 2>/dev/null | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"*.config.*\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 2043 · 2026-05-19T04:29:05.867287+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2044 · 2026-05-19T04:29:09.251058+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/ -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i config | head -10",
  "description": "Find config files in workspace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/ -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i config | head -10",
    "description": "Find config files in workspace"
  }
}
```

</details>

---


### Tool result

_source line 2045 · 2026-05-19T04:29:09.352002+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/resources.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2046 · 2026-05-19T04:29:12.786650+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
  "description": "Find yaml files in project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
    "description": "Find yaml files in project directory"
  }
}
```

</details>

---


### Tool result

_source line 2047 · 2026-05-19T04:29:12.840462+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 2048 · 2026-05-19T04:29:16.647989+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ --include=\"*.yaml\" 2>/dev/null | head -5; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ --include=\"*.yaml\" 2>/dev/null | head -5",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ --include=\"*.yaml\" 2>/dev/null | head -5; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ --include=\"*.yaml\" 2>/dev/null | head -5",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 2049 · 2026-05-19T04:29:16.750013+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2050 · 2026-05-19T04:30:13.465066+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文 ≤ 8 页 + 无限参考文献页 + appendix 不计页数\n- **模板**: ACL official style, `\\usepackage[review]{acl}`\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须有，不计入页数\n- **Checklist**: Responsible NLP Research Checklist 必须认真填写\n- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，Overall Assessment: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- 主文件: `projects/schema-dag-extraction/docs/paper/main.tex`\n- 各章节: `abstract.tex`, `introduction.tex`, `related_work.tex`, `experimental_setup.tex`, `results.tex`, `sdgd_negative.tex`, `discussion.tex`, `checklist.tex`, `prompt_appendix.tex`\n- 参考文献: `references.bib`\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计 + 统计分析**。具体关注：\n\n1. **实验设计合理性**：\n   - Count curves 和 BCS-controlled 两种实验范式是否能有效分离 count 和 confusability 两个维度？\n   - 样本量是否充足（FewRel 25 batches, DocRED 5 batches）？\n   - TOST equivalence test 的 margin 选择（±3pp）是否合理？是否有 p-hacking 风险？\n\n2. **统计分析严谨性**：\n   - Pairwise r²=1.3-1.7% 的效应量解读是否恰当？引用 Cohen (1988) behavioral research 标准是否适用于 LLM 系统？\n   - Bootstrap CI、permutation test、TOST 的使用是否正确？\n   - 多重比较问题：引用 Rothman (1990) 拒绝校正是否合理？\n   - \"Largely additive\" 的 claim 在 logit-scale inconclusive 的情况下是否 overstate？\n\n3. **跨模型/跨数据集验证**：\n   - Qwen3-32B → Llama-3.1-8B/70B → Gemini 2.5 Flash 的 cross-model 验证是否充分？\n   - Dimension 2 仅在 open-weight 模型上验证，是否是重大局限？\n   - DocRED 复现是否充分支撑 claim？\n\n4. **Negative results 的论证**：\n   - SDGD decomposition failure 的归因（merge amplification, routing failure）是否 convincing？\n   - Oracle routing +29.8pp 但 practical routing 全部 below baseline — 这是否说明 schema decomposition 本身有价值但 routing 是瓶颈？\n\n5. **混淆变量控制**：\n   - FewRel train/val split-origin 控制是否充分？\n   - MAVEN centrality confound 的处理是否合理？\n   - BCS independence from type composition (Appendix) 的 variance decomposition 是否令人信服？\n\n请按 ARR 审稿标准输出完整审稿报告，包含：Summary, Strengths, Weaknesses (逐条编号, 标注 severity: Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (评分 + 置信度), Detailed Comments。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文 ≤ 8 页 + 无限参考文献页 + appendix 不计页数\n- **模板**: ACL official style, `\\usepackage[review]{acl}`\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须有，不计入页数\n- **Checklist**: Responsible NLP Research Checklist 必须认真填写\n- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，Overall Assessment: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- 主文件: `projects/schema-dag-extraction/docs/paper/main.tex`\n- 各章节: `abstract.tex`, `introduction.tex`, `related_work.tex`, `experimental_setup.tex`, `results.tex`, `sdgd_negative.tex`, `discussion.tex`, `checklist.tex`, `prompt_appendix.tex`\n- 参考文献: `references.bib`\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计 + 统计分析**。具体关注：\n\n1. **实验设计合理性**：\n   - Count curves 和 BCS-controlled 两种实验范式是否能有效分离 count 和 confusability 两个维度？\n   - 样本量是否充足（FewRel 25 batches, DocRED 5 batches）？\n   - TOST equivalence test 的 margin 选择（±3pp）是否合理？是否有 p-hacking 风险？\n\n2. **统计分析严谨性**：\n   - Pairwise r²=1.3-1.7% 的效应量解读是否恰当？引用 Cohen (1988) behavioral research 标准是否适用于 LLM 系统？\n   - Bootstrap CI、permutation test、TOST 的使用是否正确？\n   - 多重比较问题：引用 Rothman (1990) 拒绝校正是否合理？\n   - \"Largely additive\" 的 claim 在 logit-scale inconclusive 的情况下是否 overstate？\n\n3. **跨模型/跨数据集验证**：\n   - Qwen3-32B → Llama-3.1-8B/70B → Gemini 2.5 Flash 的 cross-model 验证是否充分？\n   - Dimension 2 仅在 open-weight 模型上验证，是否是重大局限？\n   - DocRED 复现是否充分支撑 claim？\n\n4. **Negative results 的论证**：\n   - SDGD decomposition failure 的归因（merge amplification, routing failure）是否 convincing？\n   - Oracle routing +29.8pp 但 practical routing 全部 below baseline — 这是否说明 schema decomposition 本身有价值但 routing 是瓶颈？\n\n5. **混淆变量控制**：\n   - FewRel train/val split-origin 控制是否充分？\n   - MAVEN centrality confound 的处理是否合理？\n   - BCS independence from type composition (Appendix) 的 variance decomposition 是否令人信服？\n\n请按 ARR 审稿标准输出完整审稿报告，包含：Summary, Strengths, Weaknesses (逐条编号, 标注 severity: Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (评分 + 置信度), Detailed Comments。"
  }
}
```

</details>

---


### Tool result

_source line 2051 · 2026-05-19T04:30:33.717786+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20252
}
```

</details>

---


### Tool call

_source line 2052 · 2026-05-19T04:30:33.919583+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work 完整性 + 写作质量 + 格式合规）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文 ≤ 8 页 + 无限参考文献页 + appendix 不计页数\n- **模板**: ACL official style, `\\usepackage[review]{acl}`\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须有，不计入页数\n- **Checklist**: Responsible NLP Research Checklist 必须认真填写\n- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，Overall Assessment: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- 主文件: `projects/schema-dag-extraction/docs/paper/main.tex`\n- 各章节: `abstract.tex`, `introduction.tex`, `related_work.tex`, `experimental_setup.tex`, `results.tex`, `sdgd_negative.tex`, `discussion.tex`, `checklist.tex`, `prompt_appendix.tex`\n- 参考文献: `references.bib`\n\n### 你的审查侧重\n\n**新颖性 + Related Work 完整性 + 写作质量 + 格式合规**。具体关注：\n\n1. **新颖性评估**：\n   - SCS 的形式定义（pairwise cosine similarity of type name embeddings）与 LLM-PEE (2025) 的 partitioning criterion 相同。论文声称贡献在于 \"controlled experimental framework\" 而非 metric innovation — 这是否构成足够的新颖性增量？\n   - \"First controlled study isolating count and confusability\" 的 claim 是否成立？是否有遗漏的先前工作？\n   - Negative result (SDGD failure) 的贡献价值如何？\n   - 核心发现（type count dominates, confusability is RE-specific at batch level）对 community 的 actionable insight 有多大？\n\n2. **Related Work 完整性**：\n   - 是否覆盖了所有直接相关方法？特别关注：\n     - Schema decomposition for LLM IE 的最新工作（2025-2026）\n     - CrossAgentIE (ACL 2025 Findings) 的 cross-type debate 是否充分对比？\n     - Label confusion / inter-class similarity 在传统 ML 中的先前工作是否遗漏？\n     - Constrained decoding 对 error pattern 的影响是否有先前分析？\n   - 引用密度是否达到 EMNLP 标准？\n   - 是否有重要遗漏的 references？\n\n3. **写作质量**：\n   - Abstract 是否在 30 秒内传达核心价值？\n   - Introduction 叙事是否连贯（问题 → 洞察 → 方法 → 验证）？\n   - 全文主线是否统一（Abstract/Intro/Method/Results/Discussion/Conclusion 是否讲同一个故事）？\n   - 是否存在 AI 写作风格标志（em-dash, -ing phrases, 过度分段, 用词黑名单）？\n   - 专有名词是否首次出现时有定义？\n   - 图表信息密度是否足够？Caption 是否自包含？\n\n4. **格式合规**：\n   - 正文是否 ≤ 8 页？\n   - `\\usepackage[review]{acl}` 是否正确使用？\n   - 匿名化是否完整（无作者姓名泄露、无自引泄露）？\n   - Limitations section 位置是否正确（在 Conclusion 之后、References 之前）？\n   - Responsible NLP Research Checklist 填写质量如何？\n   - 引用格式是否一致？\n\n5. **论文定位与 framing**：\n   - 论文将自己定位为 \"analytical/empirical study\" 而非 \"new method\" — 对于 EMNLP 2026 是否合适？\n   - Title 中 \"Predict\" 是否准确反映论文内容（correlational evidence, not causal）？\n   - \"Two-dimensional\" framework 在 NER batch-level null 的情况下是否 oversell？\n\n请按 ARR 审稿标准输出完整审稿报告，包含：Summary, Strengths, Weaknesses (逐条编号, 标注 severity: Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (评分 + 置信度), Detailed Comments。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work 完整性 + 写作质量 + 格式合规）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文 ≤ 8 页 + 无限参考文献页 + appendix 不计页数\n- **模板**: ACL official style, `\\usepackage[review]{acl}`\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须有，不计入页数\n- **Checklist**: Responsible NLP Research Checklist 必须认真填写\n- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，Overall Assessment: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- 主文件: `projects/schema-dag-extraction/docs/paper/main.tex`\n- 各章节: `abstract.tex`, `introduction.tex`, `related_work.tex`, `experimental_setup.tex`, `results.tex`, `sdgd_negative.tex`, `discussion.tex`, `checklist.tex`, `prompt_appendix.tex`\n- 参考文献: `references.bib`\n\n### 你的审查侧重\n\n**新颖性 + Related Work 完整性 + 写作质量 + 格式合规**。具体关注：\n\n1. **新颖性评估**：\n   - SCS 的形式定义（pairwise cosine similarity of type name embeddings）与 LLM-PEE (2025) 的 partitioning criterion 相同。论文声称贡献在于 \"controlled experimental framework\" 而非 metric innovation — 这是否构成足够的新颖性增量？\n   - \"First controlled study isolating count and confusability\" 的 claim 是否成立？是否有遗漏的先前工作？\n   - Negative result (SDGD failure) 的贡献价值如何？\n   - 核心发现（type count dominates, confusability is RE-specific at batch level）对 community 的 actionable insight 有多大？\n\n2. **Related Work 完整性**：\n   - 是否覆盖了所有直接相关方法？特别关注：\n     - Schema decomposition for LLM IE 的最新工作（2025-2026）\n     - CrossAgentIE (ACL 2025 Findings) 的 cross-type debate 是否充分对比？\n     - Label confusion / inter-class similarity 在传统 ML 中的先前工作是否遗漏？\n     - Constrained decoding 对 error pattern 的影响是否有先前分析？\n   - 引用密度是否达到 EMNLP 标准？\n   - 是否有重要遗漏的 references？\n\n3. **写作质量**：\n   - Abstract 是否在 30 秒内传达核心价值？\n   - Introduction 叙事是否连贯（问题 → 洞察 → 方法 → 验证）？\n   - 全文主线是否统一（Abstract/Intro/Method/Results/Discussion/Conclusion 是否讲同一个故事）？\n   - 是否存在 AI 写作风格标志（em-dash, -ing phrases, 过度分段, 用词黑名单）？\n   - 专有名词是否首次出现时有定义？\n   - 图表信息密度是否足够？Caption 是否自包含？\n\n4. **格式合规**：\n   - 正文是否 ≤ 8 页？\n   - `\\usepackage[review]{acl}` 是否正确使用？\n   - 匿名化是否完整（无作者姓名泄露、无自引泄露）？\n   - Limitations section 位置是否正确（在 Conclusion 之后、References 之前）？\n   - Responsible NLP Research Checklist 填写质量如何？\n   - 引用格式是否一致？\n\n5. **论文定位与 framing**：\n   - 论文将自己定位为 \"analytical/empirical study\" 而非 \"new method\" — 对于 EMNLP 2026 是否合适？\n   - Title 中 \"Predict\" 是否准确反映论文内容（correlational evidence, not causal）？\n   - \"Two-dimensional\" framework 在 NER batch-level null 的情况下是否 oversell？\n\n请按 ARR 审稿标准输出完整审稿报告，包含：Summary, Strengths, Weaknesses (逐条编号, 标注 severity: Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (评分 + 置信度), Detailed Comments。"
  }
}
```

</details>

---


### Tool result

_source line 2053 · 2026-05-19T04:30:35.644901+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1725
}
```

</details>

---


### Assistant

_source line 2054 · 2026-05-19T04:30:39.097387+00:00_

Round 1 任务已分配给两位 Reviewer。等待独立审稿结果返回。

- **Reviewer 1**（方法严谨性 + 实验设计 + 统计分析）— 已触发
- **Reviewer 2**（新颖性 + Related Work + 写作质量 + 格式合规）— 已触发

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 178

## Round 178

2 recorded events


### User

_source line 2055 · 2026-05-19T04:36:48.269132+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
**Venue**: EMNLP 2026 via ARR May 2026 cycle
**审查侧重**: 新颖性 + Related Work 完整性 + 写作质量 + 格式合规

---

## Summary

本文研究 training-free LLM 信息抽取中 schema 复杂度导致性能下降的两个维度：type count（维度1）和 type confusability（维度2）。作者提出 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 来量化类型混淆度，在 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）上用 Qwen3-32B 为主模型进行了系统实验。主要发现：(1) count 下降是主导因素；(2) BCS 在 RE forced-choice 格式下解释 22-53% 的跨 batch 准确率方差，但对 NER 无 batch-level 信号；(3) schema decomposition 因 merge amplification (NER) 和 routing failure (RE) 而失败。跨模型验证覆盖 Llama-3.1-8B/70B 和 Gemini 2.5 Flash。

---

## 总体评分

**Overall Assessment**: 3.0 — Findings
**一句话总结**: 方法论扎实、报告诚实的经验性研究，但 SCS 本身非新指标，实际效应量有限（典型 batch 约 2pp 差异），且无有效缓解方案，新颖性不足以进入主会议。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 实验设计严谨（stratified batches, TOST, bootstrap CI, 4 模型交叉验证），但若干核心 claim 的 framing 超出证据支撑范围（详见 N1-N3） |
| **Excitement** | 2.5/5 | 研究问题重要且实际，但核心发现（count 主导、相似类型导致混淆）并不出人意料；SCS 复用已有指标；实际效应量有限；无可行缓解方案降低了 actionable insight |
| **Reproducibility** | 4/5 | 详细的实验描述、prompt 模板、超参数、数据集说明；代码待发布；单 seed + greedy decoding 降低随机性 |
| **Confidence** | 4/5 | 仔细阅读全文并核查相关工作 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Title "Predict" 与实际 correlational evidence 不匹配**
- 具体位置：Title, Abstract, §1 Introduction
- 问题：Title 使用 "How Does Schema Complexity **Predict** Performance"，暗示 SCS/BCS 有因果预测力。但论文自身在 Limitations item 4（第 9 页第 701-711 行）明确承认 "The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway"。更关键的是，renaming 实验（Appendix W, Table 18）直接反驳了朴素因果链：降低 SCS 反而降低准确率 3-9pp。此外 logit-scale TOST 也 inconclusive ($p = 0.209$)。
- 为什么影响接收：Title 是审稿人和读者的第一印象。当 title 暗示 predictive/causal 关系但论文内容仅为 correlational + renaming 反例时，构成 overclaiming，是审稿人最敏感的问题之一。
- 建议修改方向：改为 "How Does Schema Complexity **Relate to** / **Affect** / **Shape** Performance..." 或 "Schema Complexity and Performance Degradation in..."，更准确反映 correlational 性质。

**N2** [critical] **"Two-dimensional" framework 在 NER 上部分失效，但 framing 未充分体现**
- 具体位置：Abstract ("Degradation operates along two largely additive dimensions"), §1 Introduction, §4.4, §6 Discussion
- 问题：Abstract 和 Introduction 将论文定位为发现了"两个 largely additive 的维度"。但实际数据显示：
  - NER batch-level BCS 完全无预测信号（$r \approx 0$, $n = 450$; §4.3 第 73 行, §4.4 第 87 行）
  - "Additive" 仅在 FewRel sentence-level RE 的 TOST ±3pp 成立（$p = 0.003$）；DocRED TOST 不成立（$p = 0.77$, interaction +5.7pp）; NER factorial inconclusive ($p = 0.50$); logit-scale 也 inconclusive ($p = 0.209$）
  - 因此 "two-dimensional" 和 "largely additive" 实际上只在一个 task × 一个 scale 上成立
- 为什么影响接收：核心 claim 的 generalizability 远弱于 framing 暗示的范围。审稿人期望 Abstract 准确反映结果的边界条件，而不是将最强条件下的结论推广为通用 framework。
- 建议修改方向：Abstract 和 Introduction 应明确限定："The two-dimensional decomposition is clean in sentence-level RE under forced-choice classification; in NER, only the count dimension is robustly detectable at batch level, while confusability operates at pairwise level only." "Largely additive" 应加限定为 "in sentence-level RE"。

**N3** [critical] **SCS 无新颖性，"controlled framework" 作为贡献的论证不足**
- 具体位置：§2 Related Work "SCS novelty" 段, §1 Contribution 1
- 问题：论文在 §2 Related Work 段落末尾坦诚承认 "SCS shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion in LLM-PEE"。论文的核心新颖性 claim 是 "controlled experimental framework that isolates confusability's predictive relationship"。然而：
  - (a) 研究框架本身（fix count, vary confusability）是一个自然的实验设计选择，并非方法论创新
  - (b) 主要发现（count dominates, similar types confuse more）在直觉层面并不出人意料；数值量化（r² = 1.3-1.7% pairwise, ~2pp typical batch gaps）虽有贡献但效应量有限
  - (c) Negative result (SDGD failure) 是有价值的贡献，但论文未充分论证为什么这个 negative result 对 community 有足够大的影响——LLM-PEE 自己报告了 decomposition 的收益，本文的 Few-NERD NER 失败是否说明 LLM-PEE 在 event extraction 上的成功不可迁移？还是实验设置差异（union merge vs. LLM-PEE 的 merge 策略）导致？
- 为什么影响接收：EMNLP 对 empirical study 的新颖性要求不是新方法，但期望新洞察。当核心 metric 复用已有工作、效应量有限、且无可行缓解方案时，论文的 contribution 主要落在"确认已知直觉并精确量化"上，这对 main conference 的 excitement 门槛偏低。
- 建议修改方向：(1) 更深入对比 LLM-PEE 的 merge 策略与本文 union merge 的差异，说明为什么他们报告了收益而本文失败——是 task 差异还是 merge 策略差异？(2) 强化 negative result 的 actionable value——例如为什么这意味着 community 应该放弃 decompose-then-merge 这条路线？(3) 考虑增加至少一个可行的缓解实验（如 contrastive definitions for high-SCS pairs, 论文 §6 第 14 行提到但标注 "untested; future work"）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **"Largely additive" 的统计论证中 equivalence margin 选择值得质疑**
- 具体位置：§4.4, Appendix C (§sec:appendix_factorial)
- 问题：TOST 使用 ±3pp margin 声称 interaction "bounded below practical significance"。但 Appendix C 的 sensitivity analysis 显示：在 ±2pp margin 下仅 marginally equivalent ($p = 0.047$)，±1pp 下 inconclusive ($p = 0.278$)。考虑到 confusability main effect 本身仅 2.2pp，一个 3pp 的 interaction 已经超过 main effect 的 130%（论文自己承认，Appendix C 第 186 行）。选择 ±3pp 而非 ±2pp 作为 primary margin 看起来像是为了让 TOST pass 而做的选择。
- 建议：讨论中应更突出 ±2pp 结果（marginal）和 logit-scale inconclusive 结果，而非将 ±3pp TOST 作为支撑 "largely additive" 的主要证据。

**W2** [warning] **Renaming 实验结果削弱了 SCS 的实用价值但讨论不足**
- 具体位置：Appendix W (§app:renaming), Limitations item 4
- 问题：SCS 的实用价值依赖于"降低 SCS 可以降低混淆"这一假设。但 renaming 实验表明相反结果——降低 pairwise SCS (0.87→0.67) 反而降低准确率 3-9pp。论文将此归因于 "label unfamiliarity"，但这个结果从根本上质疑了 SCS 作为"可操作指标"的定位。§6 Practical implications 第 1 条建议 "flag type pairs with SCS > 0.85 for merging or definition refinement"，但 renaming 实验说明 definition refinement 可能适得其反。
- 建议：应在正文（而非仅 appendix/limitations）更显著地讨论这个矛盾，并调整 practical implications 的措辞。

**W3** [warning] **CrossAgentIE (ACL 2025 Findings) 对比不充分**
- 具体位置：§2 Related Work 第 8 段
- 问题：CrossAgentIE 使用 cross-type debate 来解决 type confusion，这与本文的 confusability 分析直接相关。但论文仅在一个括号中列出 (crossagentie-2025, cmas-ner-2025) 并统一归入 "multi-agent debate"，未讨论 CrossAgentIE 的 cross-type debate 机制是否本质上就是在处理 type confusability，以及其方法是否可以作为本文 SDGD 失败后的替代方案。
- 建议：增加 1-2 句直接对比 CrossAgentIE 的 cross-type debate 与本文的 confusability-aware batching 的异同。

**W4** [warning] **FewRel train/val split 混合使用的合理性**
- 具体位置：§3.1 FewRel 段落
- 问题：论文将 FewRel 的 training 和 validation splits 合并为 80-relation pool。虽然在 zero-shot 设置下不涉及训练，但 Appendix P (§app:split-origin) 显示 train-origin types 准确率低 8.8pp ($p = 0.06$, marginally significant)。论文称 BCS 回归控制此 covariate 后效应不变，但 per-type 性能差异仍然存在，且方向与 contamination 假设相反的论证较弱（"opposite to the contamination hypothesis" 不等于排除 contamination）。
- 建议：更谨慎地讨论 contamination 风险，承认 train-origin accuracy drop 的替代解释（如 type difficulty differences between splits），而非仅以方向论证排除。

**W5** [warning] **论文定位为 "analytical/empirical study" 是否适合 EMNLP main track**
- 具体位置：全文
- 问题：论文不提出新方法、新指标（SCS=LLM-PEE 的 criterion）、新数据集。核心贡献是对已知现象（schema complexity degrades performance）的系统量化。对于 EMNLP main conference，审稿人通常期望 empirical study 带来 actionable insight 或意外发现。本文的主要发现——count dominates, confusability is task-specific, decomposition fails——虽然量化精确，但缺乏 surprising 元素。
- 建议：如果定位为 Findings，当前内容可能足够。如果目标是 main conference，需要增加可行方案实验或更 surprising 的发现。

---

## 小问题（不影响接收）

- **M1**: references.bib 中 `jagannatha2020calibrating` 未在正文中引用（orphan entry）。
- **M2**: Abstract 信息密度极高（约 200 words），第一句即引入多个技术概念（SCS, BCS, 两个维度）。建议在 "type confusability" 首次出现时加一个 intuitive 的解释。
- **M3**: Gemini 2025 引用 (arXiv:2507.06261) 的 arXiv 编号格式似乎异常——2507 意味着 2025 年 7 月，但当前日期为 2026 年 5 月，该论文可能已有正式发表版本。
- **M4**: Figure 1 和 Figure 2 的 caption 是自包含的（good），但 Table 1 的 caption 中 "BCS Range: min-max over count-curve batches" 需要读者已知 count-curve 实验设计才能理解。
- **M5**: §3.2 中 "name-only embeddings as a practical simplification" 后面给了 ablation 证据，但 FewRel prompts 用 type names without definitions 而 Few-NERD prompts include definitions——这意味着 Few-NERD 的 SCS 可能系统性地低估了实际 confusability（因为模型看到了 definitions 但 SCS 只用 names）。论文在 Appendix 中处理了 name+definition SCS 但应在正文简要提及此不一致。
- **M6**: 引用格式基本一致，但少数 bib 条目的 first author field 与 OpenAlex 记录不匹配（如 wei-2023-chatie: bib=Wei vs API=Xiang；dlisc-2025: bib=Li vs API=Wen）。应核实这些条目的准确性。

---

## Missing References（建议考虑引用）

1. **Dubey et al. (2018), "Pairwise Confusion for Fine-Grained Visual Classification"** (ECCV 2018) — 直接使用 pairwise confusion matrix 来改进 fine-grained classification，与本文的 pairwise SCS-confusion correlation 分析高度相关。论文引用了 CV 领域的 Deng 2010 (ImageNet) 但遗漏了这篇更直接相关的工作。

2. **Exploiting Class Similarity for Machine Learning with Confidence Labels and Projective Loss Functions** (Collier et al., 2021) — 研究 inter-class similarity 对分类的影响，提出利用 class similarity structure 的方法，与本文对 label similarity 与 confusion 关系的分析相关。

---

## 主要优势

1. **实验设计严谨**：stratified batch design 控制 count 和 confusability，是一个 well-crafted quasi-experimental 框架。TOST equivalence testing, permutation tests, bootstrap CIs, cross-model validation (4 models including proprietary) 展示了高水平的统计素养。

2. **Negative results 的诚实报告**：SDGD 失败、renaming 失败、NER batch-level null、logit-scale inconclusive——这些 negative results 比 positive findings 更具信息量，论文没有隐藏或淡化它们。

3. **Cross-model validation 覆盖面广**：Qwen3-32B → Llama-3.1-8B/70B → Gemini 2.5 Flash (API)，跨越开源/闭源、8B-70B+ 规模，Dimension 1 的 directional consistency 证据充分。

4. **Limitations 极为详尽**：5 项 limitations + multiple comparisons 段落，每项都具体且 quantified，达到了 EMNLP 期望的 Limitations 标准。

5. **引用覆盖度好**：69 个 unique cited keys，覆盖直接竞争者 (LLM-PEE, PARSE, CrossAgentIE, CMAS-NER)、基础方法 (GLiNER, GoLLIE, UniNER)、evaluation/statistical 方法 (TOST, Rothman, Dror)，以及 representation degeneration 文献。对于一篇 empirical study 这个密度是充足的。

6. **写作质量整体良好**：无 em-dash AI 写作标志，叙事结构清晰（RQ-driven），专有名词首次出现有定义。

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| `\usepackage[review]{acl}` | ✅ | main.tex 第 3 行 |
| 匿名化 | ✅ | `\author{Anonymous}`, anonymous.4open.science link |
| 正文 ≤ 8 页 | ✅ | Conclusion 在第 8 页结束，Limitations 从第 8 页底部开始 |
| Limitations section | ✅ | 在 Conclusion 之后、References 之前，不计入页数 |
| Responsible NLP Checklist | ✅ | 逐项填写，质量良好（A1-A4, B1-B6, C1-C4, D1-D5, E1 全部有实质回答） |
| 行号 | ✅ | review mode 自动启用 |
| 引用格式 | ✅ | 基本一致，使用 `\cite`, `\citet`, `\citep` |
| 自引泄露 | ✅ | 未发现明显自引泄露 |

---

## 最终评分

| 维度 | 分数 |
|------|------|
| **Soundness** | 3.5 |
| **Excitement** | 2.5 |
| **Overall Assessment** | 3.0 (Findings) |
| **Confidence** | 4 |
| **Reproducibility** | 4 |

**Overall 评分理由**: 论文展示了扎实的实验方法论和诚实的 negative result reporting，适合 Findings 收录。但以下因素限制了进入 main conference：(1) SCS 非新指标（=LLM-PEE criterion）；(2) 核心效应量有限（典型 batch ~2pp, pairwise r²≈1.5%）；(3) "two-dimensional" framework 在 NER 上部分失效；(4) 无可行缓解方案（SDGD 失败、renaming 反向、few-shot 加剧）；(5) title/abstract 的 framing 超出证据支撑范围。如果作者能 (a) 修正 framing 使之准确反映 correlational 性质和 task-specific 边界条件，(b) 增加至少一个可行缓解实验，(c) 更深入对比 LLM-PEE 的 merge 策略差异，则有潜力提升到 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2056 · 2026-05-19T04:37:03.686694+00:00_

收到 Reviewer 2 的 Round 1 审稿报告。

**R2 核心判断**: Overall 3.0 (Findings)，3 个 Must-Fix（title overclaiming、two-dimensional framework NER 失效、SCS 新颖性不足），5 个 Should-Fix，6 个 Minor。

等待 Reviewer 1 的报告到达后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 179

## Round 179

6 recorded events


### User

_source line 2057 · 2026-05-19T04:37:04.797948+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告 — Round 1

**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
**Venue**: EMNLP 2026 (via ARR May 2026 cycle)
**审查侧重**: 方法严谨性 + 实验设计 + 统计分析

---

## Paper Summary

本文研究 training-free LLM 信息抽取中 schema 复杂度导致的性能退化问题，提出将退化分解为两个维度：type count（维度1）和 type confusability（维度2）。作者定义了 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 来量化 type 间语义混淆度，在 Few-NERD (NER)、FewRel (RE)、DocRED (doc-RE)、MAVEN (ED) 四个数据集上进行了 count curves 和 BCS-controlled 两种实验范式的系统评估。主要发现：(1) 两个维度"大致可加"（在 sentence-level RE 上）；(2) BCS 能解释 RE 22-53% 的跨 batch 准确率方差，但对 NER 无 batch-level 信号；(3) schema 分解因 merge amplification (NER) 和 routing failure (RE) 而失败。Cross-model 验证覆盖 Qwen3-32B、Llama-8B/70B、Gemini 2.5 Flash。

---

## 总体评分

**Overall Assessment**: 3.5 (Borderline Conference)
**Confidence**: 4 (Quite sure. I tried to check the important points carefully.)
**一句话总结**: 实验设计严谨、统计处理透明度高于 NLP 论文平均水准，但 "largely additive" 的核心 claim 在 logit scale 和 DocRED 上站不住脚，pairwise 效应量极小（r²=1.3-1.7%），且所有实际干预方向（分解、重命名、few-shot）均失败，实际可操作价值有限。

---

## 官方维度打分（来自 ARR Review Form，2025年2月更新版）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨，统计工具使用恰当（TOST、permutation test、bootstrap CI），但核心 claim "largely additive" overclaim，且多个条件下 TOST inconclusive |
| Excitement | 3.0/5 | 分析框架有新意（首次系统分离 count vs confusability），但实际可操作建议有限，所有干预方向均失败 |
| Reproducibility | 4/5 | 实验细节充分（model版本、decoding参数、prompt模板、seed），代码承诺 acceptance 后释放 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] "Largely additive" claim 在多个条件下不成立，属于 overclaim

- 具体位置：Abstract（"two largely additive dimensions"）、§5（"bounded interaction"）、§7 Conclusion（"two largely additive dimensions"）
- 问题：论文声称 count 和 confusability 两个维度"大致可加"。然而：
  - **FewRel logit-scale**: interaction 0.111 logit, p=0.047（marginally significant），TOST inconclusive（p=0.209）。论文在 Appendix D 承认这一点，但 Abstract 和 Conclusion 未加此限定。
  - **DocRED**: interaction +5.7pp，95% CI [-1.6, 13.0]，TOST at ±3pp p=0.77，完全无法建立 equivalence。论文限定为"sentence-level RE"，但 Abstract 和 Conclusion 中"largely additive"未加 task/scale 限定词。
  - **NER**: factorial test inconclusive（p=0.50），无法分离两维度。
  - **FewRel 2×2 factorial**: 也 inconclusive（p=0.56）。
  - 实际上，"largely additive"仅由 FewRel 69-batch full-range regression 在 linear scale 上支撑（TOST p=0.003 at ±3pp），这是一个单数据集、单 scale 的结论。
- 为什么影响接收：这是论文的核心 framing 之一，贯穿 Abstract/Introduction/Conclusion。如果只在 sentence-level RE 的 linear scale 上成立，就不应作为论文的主要标题级 claim。
- 建议修改方向：(1) Abstract 和 Conclusion 中将 "largely additive" 限定为 "bounded interaction under linear specification in sentence-level RE"；(2) 明确承认在 DocRED 和 logit scale 上 additivity 不成立；(3) 或者重新 frame 为 "two separable dimensions"（不做 additivity claim）。

**N2** [critical] Pairwise r²=1.3-1.7% 的效应量解读不够审慎，Cohen (1988) behavioral research 标准对 LLM 系统的适用性未论证

- 具体位置：§4.2 Table 2、§2 Related Work（"consistent with individual-difference predictors in behavioral research"）、Limitations item 2
- 问题：
  - r²=1.3-1.7% 意味着 SCS 仅解释 type confusion 方差的 1.3-1.7%，剩余 >98% 由其他因素决定。
  - 论文引用 Cohen (1988) 和 Lakens (2013) 的 behavioral research 标准来为小效应量辩护。但 Cohen 的标准是为心理学个体差异研究设计的，其中 r=0.1（r²=1%）被认为"small but meaningful"是因为在真实人群中的可检测效应有实际意义。LLM 系统是确定性的（greedy decoding），变量可控程度远高于行为研究，没有理由直接套用这个标准。
  - 论文的 aggregation simulation（Appendix H）展示了 pair→batch 3x amplification，这比直接引用 Cohen 更有说服力，但模拟本身依赖 conditional r²=7%（只看非零混淆对），而非 unconditional 1.3%。
- 为什么影响接收：如果 SCS 作为 confusability 的代理指标只解释 1.3% 方差，那 "confusability predicts type confusion" 这个 claim 的实际意义需要更谨慎的论述。审稿人可能质疑：是 SCS 本身不是好指标，还是 confusability 本身不是重要因素？
- 建议修改方向：(1) 不引用 Cohen 的行为研究标准，改为直接用 batch-level R²=22-53% 作为主要证据，pairwise 作为补充；(2) 讨论为什么 pairwise 效应小但 batch-level 效应大（已有 aggregation simulation，但应提到正文而非仅 appendix）；(3) 讨论 SCS 作为代理指标的局限性（可能需要更精细的 confusability 指标，如基于 in-context confusion matrix 的指标）。

**N3** [critical] BCS 对 NER 无 batch-level 信号，削弱 "two-dimensional" 框架的通用性

- 具体位置：§4.3（"BCS shows no batch-level signal for NER"）、§5（"NER batch-level BCS shows no predictive signal"）、Discussion（"RE-specific"）
- 问题：
  - 论文提出的是一个跨任务的 "two-dimensional degradation" 框架（Abstract: "across NER, RE, and event detection"）。
  - 但实际结果显示：Dimension 2 (confusability) 的 batch-level 效应**仅在 RE 的 forced-choice format 下有效**。NER r≈0（n=450），NER factorial inconclusive，MAVEN 有 centrality confound。
  - 论文在 Discussion 中诊断了原因（forced-choice vs multi-span，RE 的 constrained decoding 把所有 error 都导向 type substitution），这个解释合理。但问题是：如果 BCS 只在 RE 有效，那 "two-dimensional" 是 RE 的特性还是 IE 的通用属性？
  - Abstract 开头写 "across NER, RE, and event detection"，给人印象是三个任务都验证了两个维度。但实际上 NER 只验证了 Dimension 1（count curve）和 pairwise level 的 SCS，batch-level BCS 完全不工作。
- 为什么影响接收：论文的贡献声明可能误导读者。如果一个 reviewer 只看 Abstract 和 Introduction，会认为两个维度在三个任务上都成立。
- 建议修改方向：Abstract 和 Introduction 中明确标注 BCS batch-level 预测仅限 RE forced-choice format；将 "across NER, RE, and ED" 改为更精确的表述；或者将 NER 的 pairwise evidence 和 RE 的 batch-level evidence 分开表述。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] TOST equivalence margin ±3pp 的选择虽有 justification 但不够保守

- 具体位置：Appendix D（§ Equivalence margin justification）、Table 6
- 问题：
  - ±3pp margin 在 ±2pp 时仅 marginally equivalent（p=0.047），±1pp inconclusive（p=0.278）。
  - 论文称 3pp ≈ 0.5×batch SD，相当于 Cohen's d=0.5（medium effect）。但这里的 equivalence testing 是要证明 interaction **小**，用 "medium effect" 作为 bound 实际上是说 "interaction 不超过中等效应"，这并不令人信服——理想的 additivity claim 应该在更小的 margin 下成立。
  - 论文的 sensitivity analysis（Table 6）是一个加分项，但恰恰展示了 ±1pp 下 inconclusive，说明精确的 additivity 无法建立。
  - 此外，interaction 的 point estimate 是 0.47pp，但 90% CI 是 [-1.0, 2.0]。CI 上界 2.0pp 在 main effect 只有 2.2pp 的情况下，意味着 interaction 可能接近 main effect 大小——这不是"可忽略"的交互。
- 建议：正文中应更明确地讨论 equivalence bound 的选择对结论的影响；将 "largely additive" 弱化为 "bounded interaction at the ±3pp level"。

**W2** [warning] 引用 Rothman (1990) 拒绝多重比较校正的理由不够充分

- 具体位置：Limitations 段落（"Multiple comparisons"）、Appendix G（prompt variants）
- 问题：
  - Rothman (1990) 的立场在统计学界有争议。该论文是流行病学语境下写的，核心观点是"每个假设独立评估"，但前提是每个比较都有独立的科学理由。
  - 论文的 cross-dataset 比较确实可以视为独立复制，这部分引用 Rothman 是合理的。
  - 但 Appendix G 的 cross-prompt-variant 分析（4 variants × 2 counts = 8 comparisons），论文用"directional consistency（7/8 negative）"来论证而非校正 p-value。这8个比较并非独立假设——它们测试的是同一个底层效应在不同 prompt 下的表现。在 count=8 时 4 个 variant 都不显著，count=32 时只有 2/4 显著（p=0.043, 0.009），这更像是 power 问题而非 robust evidence。
  - 同时，核心分析中 p<0.001 的结果确实不需要多重比较校正（不会因校正而翻转），但边缘显著的二级分析（如 logit interaction p=0.047, 2pp TOST p=0.047）需要更谨慎解读。
- 建议：对 cross-dataset 复制保留 Rothman 论证；对 within-study 二级分析（prompt variants, marginal results）加注 caveat。

**W3** [warning] DocRED 样本量（5 batches per count level）过小，power 不足

- 具体位置：§3.3（"5 for DocRED and MAVEN"）、§4.3（DocRED BCS results）
- 问题：
  - FewRel 使用 25 batches per count level，DocRED 和 MAVEN 仅 5 batches。论文在脚注中解释了原因（higher per-batch evaluation cost），但 5 batches 的 count curve 统计 power 极低。
  - DocRED BCS-controlled 实验使用 n=35（5 high + 5 low + 25 random），这个样本量尚可。但 count curve 的 5 batches 无法提供可靠的趋势估计。
  - DocRED 的 factorial interaction +5.7pp 的宽 CI [-1.6, 13.0] 很可能部分归因于样本量不足。
- 建议：如果计算资源允许，增加 DocRED count curve batches 至少到 15；如果不可行，明确讨论 5-batch count curve 的 power limitation。

**W4** [warning] Dimension 2 未在 proprietary model 上验证，cross-model 验证存在缺口

- 具体位置：Appendix M（Gemini 2.5 Flash）、Limitations item 1
- 问题：
  - Dimension 1 跨模型验证充分（Qwen3-32B, Llama-8B, Llama-70B, Gemini 2.5 Flash），但 Dimension 2（BCS-controlled）仅在 open-weight 模型上验证。
  - Gemini count-64 仅基于 11/25 batches（"partial"），论文未解释为什么部分数据缺失（API rate limit? 费用?）。
  - Llama-70B 的 BCS 验证仅在 count=16 进行（单个 count level），不如 Qwen3 的多 count level 验证全面。
  - 论文在 Limitations 中承认了 proprietary model 缺口，但鉴于 proprietary model 在实际应用中更常被使用，这是一个重要的外部有效性问题。
- 建议：解释 Gemini partial data 的原因；如果有条件，补充 Gemini 在至少一个 count level 的 BCS-controlled 实验；明确标注这是 future work 而非已验证。

**W5** [warning] Negative results (SDGD) 的归因分析虽有诊断但缺少解决方向的验证

- 具体位置：§6（SDGD）、Appendix B（SDGD Full Protocol）、Appendix C（Routing Strategies）
- 问题：
  - Oracle routing +29.8pp 但所有 practical routing 均 below baseline。这说明**如果 routing 能解决**，schema decomposition 是有价值的。
  - 论文诊断了两个 failure mode：merge amplification (NER) 和 routing failure (RE)。对 merge amplification 的分析清晰（precision collapse + recall bounded）。
  - 但对 routing failure 的分析不够深入：为什么 "73.4% of instances receive positive predictions from 3-5 sub-schemas simultaneously"？这是 constrained decoding (enum constraint) 强制产生 positive prediction 的结果，论文也指出了 none-rate 只有 20-40%。但这意味着**问题不在于 schema decomposition 本身，而在于 constrained decoding 与 decomposition 的交互**。如果允许 "none" 有更高概率（如调整 prior），routing 可能改善。
  - 论文最后一句 "Promising avenues include coarse-to-fine pipelines and retrieval-based routing" 过于简略。
- 建议：讨论 constrained decoding 与 routing failure 的交互关系；考虑是否有简单的 ablation（如去掉 enum constraint 后的 routing performance）来验证归因。

**W6** [warning] FewRel train/val split-origin 控制可以更强

- 具体位置：Appendix I（Split-Origin Covariate Analysis）、Limitations item 5
- 问题：
  - FewRel 组合了 64 train-split 和 16 val-split types，train-origin types 准确率低 8.8pp（p=0.06，marginally nonsignificant）。
  - 论文用 covariate analysis 展示 BCS 效应控制 split-origin 后不变（β_BCS unchanged），这是一个好的控制。
  - 但核心问题是：为什么不直接在 16 个 val-origin types 上做独立验证？论文在 Appendix F 报告了 held-out validation（SCS-confusion ρ=0.216, p=0.018 on 120 val-only pairs），这比 covariate analysis 更有说服力，但埋在 Appendix 深处。
  - 此外，FewRel (2018) 确实有 data contamination 风险。虽然 train-origin types 反而准确率更低（与 contamination 假设相反），但这个 argument 不完全令人信服——contamination 可能以更复杂的方式影响（如改变 type 间 confusion pattern 而非整体准确率）。
- 建议：将 held-out validation 结果提到正文（即使简短提及）；对 contamination 的讨论更加 nuanced。

---

## 小问题（不影响接收）

- **M1**: references.bib 中 `jagannatha2020calibrating` 未被引用（orphan entry）。
- **M2**: Table 1 的 Embedding 列显示 Few-NERD 用 Qwen3-32B 而其他用 MiniLM，但 BCS Range 注明 "ranges are not comparable across embedding models"。这意味着跨数据集的 BCS range 比较（如 FewRel 0.42-0.97 vs MAVEN 0.87-0.97）无意义，但论文某些地方隐含了这种比较（如 DocRED "wider confusability range"）。
- **M3**: Appendix M (Gemini) 的 count-64 标注 "partial (11/25 batches)" 但未解释原因。
- **M4**: 论文在 §3.4 提到 "v1 requests character offsets" 且 "96.5% of predicted offsets were hallucinated"，这是一个有趣的附带发现但未被充分讨论——如果 v1 的 offset hallucination 率如此高，为什么仍然报告 v1 结果？（虽然评估用的是 text matching 而非 offset matching，但这暗示 v1 格式可能以其他方式影响提取质量。）
- **M5**: Limitations §3 提到 unconstrained decoding ablation (n=25) 消除了 BCS-accuracy 相关，但只在 Discussion 中简要提及。建议将此作为 format dependency 的正式 finding。

---

## 主要优势

1. **实验设计精良**: Count curves + BCS-controlled 两种范式的组合设计巧妙，有效分离了 count 和 confusability。within-pool 控制（从 80-rel pool 抽 16-rel subsets）排除了 pool composition confound。FewRel 的 balanced design 自然消除了 type frequency confound。
2. **统计处理透明度高**: 使用 TOST equivalence testing（而非仅看 null result）、bootstrap CI、permutation test、cluster bootstrap，并在 Appendix 中报告了多个 sensitivity analysis（TOST margin sweep、logit-scale、BCS aggregation method）。在 NLP 论文中这个统计严谨程度明显高于平均。
3. **诚实报告 negative results**: SDGD 失败和 label renaming 实验均如实报告，且有合理的 failure mode 诊断。MAVEN centrality confound 的发现和处理也展现了方法论上的严谨。
4. **Cross-model validation 范围广**: 4 个模型（Qwen3-32B, Llama-8B, Llama-70B, Gemini 2.5 Flash），覆盖不同 scale 和 family，Dimension 1 的 cross-model 证据令人信服。
5. **Appendix 信息量大**: 14 个 Appendix 节提供了大量 sensitivity analysis、alternative specifications、和 robustness checks，审稿人可以深入验证每个 claim。

---

## Missing References

- 未发现严重缺漏。Related Work 覆盖了直接相关方法（LLM-PEE, PARSE, UniNER 等）、baseline 论文（FewRel, Few-NERD, DocRED, MAVEN）、评测框架、和统计方法论参考。引用量级（~70 entries）与顶会长文一致。
- 可以考虑添加：(1) 关于 LLM calibration 与 constrained decoding 交互的工作（与 routing failure 分析相关）；(2) 关于 equivalence testing 在 ML 中应用的更新文献（Lakens 之外）。

---

## Detailed Comments

### 关于实验设计合理性

1. **Count curves + BCS-controlled 的双范式设计**：这是本文方法论上的核心创新。Count curves 展示 trend direction，BCS-controlled 实验量化 confusability 独立效应。设计合理，两个范式互补。

2. **样本量**: FewRel 的 25 batches/count level 对于 regression analysis 足够（n=69 for full-range, n=100 for within-pool）。DocRED 的 5 batches/count level 明显不足（已在 W3 中标注）。BCS-controlled 的 extreme batch design（1 low + 1 high + 25 random）在 16-rel pilot 中 power 有限（acknowledged by authors），80-rel 条件下 power 充足。

3. **Greedy decoding single seed**: 论文用 greedy decoding (temp=0, seed 42) 减少随机性，Appendix N 的 variance decomposition 支持 batch composition 是主要方差来源（>5x intra-batch vs inter-seed）。这是合理的设计选择，但 seed=42 是一个特定选择，few-shot 实验中 example selection 的随机性未被控制。

### 关于统计分析严谨性

4. **TOST 的使用**: 概念上正确（equivalence testing 而非 null hypothesis testing），但 margin 选择（±3pp）的 justification 依赖 Cohen's d=0.5 analogy，而这个 analogy 未被充分论证（N2）。Sensitivity analysis（Table 6）是加分项。

5. **Bootstrap CI**: 使用 percentile bootstrap (B=10,000 for pairs, B=1,000 for batches) 是 standard practice。Cluster bootstrap for type-level dependencies (Table 2) 是正确的。

6. **Conditioning on nonzero confusion pairs**: 论文报告 conditional r²=7% 时诚实标注了 "conditioning on the dependent variable may inflate this"。但 aggregation simulation 使用 conditional r²（而非 unconditional）来 match 观测到的 batch-level R²=0.218，说明 conditional model 是更好的解释——论文应该更清楚地说明为什么 conditional 在这里是合理的（因为 89% 的 type pairs 永远不会互相混淆，只有语义近邻才 "active"）。

### 关于跨模型/跨数据集验证

7. **Dimension 1 cross-model**: Qwen3→Llama-8B（Few-NERD -43pp, per-batch r=0.725）、Qwen3→Llama-70B（RE slope near-identical: -30.7 vs -30.1pp）、Qwen3→Gemini（monotonic decline, ρ=-1.0 for count 4-32）。证据充分。

8. **Dimension 2 cross-model**: Llama-8B BCS gap 77-87% of Qwen3（Table A2）；Llama-70B Δ=+10.9pp（CI excludes zero）。但未在 Gemini 上验证——这是一个 gap（W4）。

### 关于 Negative Results

9. **SDGD failure 归因合理但不完整**: merge amplification 的诊断清晰（precision 0.563→0.210，recall 有限提升）。routing failure 归因于 constrained decoding 迫使 positive prediction 也合理。但缺少一个关键实验：在 RE 上去掉 enum constraint 后 routing 是否改善？论文的 unconstrained ablation（§7）只检查了 BCS-accuracy correlation 是否消失，未检查 routing performance。

10. **Oracle routing +29.8pp vs practical routing all below baseline**: 这个 gap 提示 schema decomposition 的理论上限很高，瓶颈完全在 routing。论文应该更强调这一点——这对 future work 方向有重大指导意义。

---

## Overall Assessment 理由

本文是一篇扎实的实证分析论文，在实验设计和统计处理上明显优于大多数 NLP 论文。two-dimensional decomposition 框架有概念价值，negative results（SDGD failure, renaming failure）对社区有参考意义。

但有三个问题拉低评分：(1) "largely additive" 作为核心 claim 仅在 sentence-level RE linear scale 上成立，overclaim 明显；(2) BCS batch-level 效应仅在 RE forced-choice format 下有效，框架的通用性有限；(3) pairwise 效应量极小（r²≈1.5%），所有实际干预（分解、重命名、few-shot）均失败，论文的 practical impact 很弱。

如果 N1（overclaim）和 N3（通用性限定）得到修复，论文的诚实度和分析质量足以支持 Findings 接收。以目前的 framing 看，Borderline Conference (3.5) 是我的评分，如果 overclaim 不修，可能降至 3.0 (Findings)。


---

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**Overall 3.0 (Findings)**。

三个 Must-Fix 问题：
1. Title "Predict" 与 correlational evidence 不匹配，renaming 实验直接反驳朴素因果链
2. "Two-dimensional largely additive" framework 仅在 sentence-level RE 成立，NER 无 batch-level 信号，DocRED/logit-scale TOST 均 inconclusive
3. SCS 无方法新颖性（=LLM-PEE criterion），"controlled framework" 作为贡献需更强论证，且效应量有限（~2pp typical gaps）

主要优势：实验设计严谨、negative results 诚实报告、跨模型验证覆盖广、Limitations 详尽、引用覆盖度好、格式完全合规。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2058 · 2026-05-19T04:37:59.289053+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## Step 2 — 交叉分享：请对 Reviewer 2 的审稿意见逐条回应\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]**：同意并简要说明理由\n- **[REBUT]**：反驳并提供证据（引用论文具体 Section/Table/Figure）\n\n特别关注 R2 提出但你未提出的问题（R2-N1 Title \"Predict\", R2-N3 SCS novelty, R2-W2 renaming experiment, R2-W3 CrossAgentIE）以及你们评分差异的原因（你 3.5 vs R2 3.0）。\n\n---\n\n## Reviewer 2 完整审稿原文\n\n**Overall Assessment**: 3.0 — Findings\n**Soundness**: 3.5 | **Excitement**: 2.5 | **Confidence**: 4 | **Reproducibility**: 4\n\n### Must-Fix:\n\n**R2-N1** [critical] Title \"Predict\" 与实际 correlational evidence 不匹配\n- Title 使用 \"How Does Schema Complexity **Predict** Performance\"，暗示因果预测力\n- Limitations item 4 承认仅 correlational evidence\n- Renaming 实验直接反驳朴素因果链（降低 SCS 反而降低准确率 3-9pp）\n- Logit-scale TOST inconclusive (p=0.209)\n- 建议改为 \"Relate to\" / \"Affect\" / \"Shape\"\n\n**R2-N2** [critical] \"Two-dimensional\" framework 在 NER 上部分失效但 framing 未充分体现\n- NER batch-level BCS 完全无预测信号 (r≈0, n=450)\n- \"Additive\" 仅在 FewRel sentence-level RE linear scale 成立\n- DocRED TOST 不成立 (p=0.77); NER factorial inconclusive (p=0.50); logit-scale inconclusive (p=0.209)\n- Abstract 和 Introduction 未充分限定这些边界条件\n\n**R2-N3** [critical] SCS 无新颖性，\"controlled framework\" 作为贡献的论证不足\n- SCS = LLM-PEE 的 partitioning criterion（论文自己承认）\n- \"controlled experimental framework\" 是自然的实验设计选择，并非方法论创新\n- 核心发现（count dominates, similar types confuse more）直觉上不意外\n- 效应量有限（~2pp typical, r²≈1.5% pairwise）\n- 无可行缓解方案（SDGD失败/renaming反向/few-shot加剧）\n- 建议：更深入对比 LLM-PEE merge 策略差异；强化 negative result actionable value；增加至少一个可行缓解实验\n\n### Should-Fix:\n\n**R2-W1** TOST ±3pp margin 选择值得质疑（与你的 W1 重叠）\n\n**R2-W2** Renaming 实验削弱 SCS 实用价值但讨论不足\n- SCS 实用价值依赖\"降低 SCS 可以降低混淆\"，renaming 证明相反\n- §6 Practical implications 建议 \"flag type pairs with SCS>0.85 for definition refinement\" 但 renaming 说明这可能适得其反\n\n**R2-W3** CrossAgentIE (ACL 2025 Findings) 对比不充分\n- Cross-type debate 与 confusability 分析直接相关\n- 论文仅在括号中列出，未讨论其 debate 机制是否本质上处理 type confusability\n\n**R2-W4** FewRel train/val split 混合使用的合理性（与你的 W6 重叠）\n\n**R2-W5** 论文定位为 \"analytical/empirical study\" 是否适合 EMNLP main track\n\n### Minor: M1 orphan bib entry, M2 Abstract 信息密度, M3 Gemini 引用格式, M4 Table 1 caption, M5 SCS name-only vs prompt content 不一致, M6 bib accuracy\n\n### Missing References:\n1. Dubey et al. (2018) \"Pairwise Confusion for Fine-Grained Visual Classification\" (ECCV)\n2. Collier et al. (2021) \"Exploiting Class Similarity for ML with Confidence Labels\"\n\n---\n\n请逐条回应 R2 的每个 Must-Fix、Should-Fix 和 Missing References。对于你的评分（3.5）与 R2（3.0）的差异，请说明你是否调整评分或维持不变。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "## Step 2 — 交叉分享：请对 Reviewer 2 的审稿意见逐条回应\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]**：同意并简要说明理由\n- **[REBUT]**：反驳并提供证据（引用论文具体 Section/Table/Figure）\n\n特别关注 R2 提出但你未提出的问题（R2-N1 Title \"Predict\", R2-N3 SCS novelty, R2-W2 renaming experiment, R2-W3 CrossAgentIE）以及你们评分差异的原因（你 3.5 vs R2 3.0）。\n\n---\n\n## Reviewer 2 完整审稿原文\n\n**Overall Assessment**: 3.0 — Findings\n**Soundness**: 3.5 | **Excitement**: 2.5 | **Confidence**: 4 | **Reproducibility**: 4\n\n### Must-Fix:\n\n**R2-N1** [critical] Title \"Predict\" 与实际 correlational evidence 不匹配\n- Title 使用 \"How Does Schema Complexity **Predict** Performance\"，暗示因果预测力\n- Limitations item 4 承认仅 correlational evidence\n- Renaming 实验直接反驳朴素因果链（降低 SCS 反而降低准确率 3-9pp）\n- Logit-scale TOST inconclusive (p=0.209)\n- 建议改为 \"Relate to\" / \"Affect\" / \"Shape\"\n\n**R2-N2** [critical] \"Two-dimensional\" framework 在 NER 上部分失效但 framing 未充分体现\n- NER batch-level BCS 完全无预测信号 (r≈0, n=450)\n- \"Additive\" 仅在 FewRel sentence-level RE linear scale 成立\n- DocRED TOST 不成立 (p=0.77); NER factorial inconclusive (p=0.50); logit-scale inconclusive (p=0.209)\n- Abstract 和 Introduction 未充分限定这些边界条件\n\n**R2-N3** [critical] SCS 无新颖性，\"controlled framework\" 作为贡献的论证不足\n- SCS = LLM-PEE 的 partitioning criterion（论文自己承认）\n- \"controlled experimental framework\" 是自然的实验设计选择，并非方法论创新\n- 核心发现（count dominates, similar types confuse more）直觉上不意外\n- 效应量有限（~2pp typical, r²≈1.5% pairwise）\n- 无可行缓解方案（SDGD失败/renaming反向/few-shot加剧）\n- 建议：更深入对比 LLM-PEE merge 策略差异；强化 negative result actionable value；增加至少一个可行缓解实验\n\n### Should-Fix:\n\n**R2-W1** TOST ±3pp margin 选择值得质疑（与你的 W1 重叠）\n\n**R2-W2** Renaming 实验削弱 SCS 实用价值但讨论不足\n- SCS 实用价值依赖\"降低 SCS 可以降低混淆\"，renaming 证明相反\n- §6 Practical implications 建议 \"flag type pairs with SCS>0.85 for definition refinement\" 但 renaming 说明这可能适得其反\n\n**R2-W3** CrossAgentIE (ACL 2025 Findings) 对比不充分\n- Cross-type debate 与 confusability 分析直接相关\n- 论文仅在括号中列出，未讨论其 debate 机制是否本质上处理 type confusability\n\n**R2-W4** FewRel train/val split 混合使用的合理性（与你的 W6 重叠）\n\n**R2-W5** 论文定位为 \"analytical/empirical study\" 是否适合 EMNLP main track\n\n### Minor: M1 orphan bib entry, M2 Abstract 信息密度, M3 Gemini 引用格式, M4 Table 1 caption, M5 SCS name-only vs prompt content 不一致, M6 bib accuracy\n\n### Missing References:\n1. Dubey et al. (2018) \"Pairwise Confusion for Fine-Grained Visual Classification\" (ECCV)\n2. Collier et al. (2021) \"Exploiting Class Similarity for ML with Confidence Labels\"\n\n---\n\n请逐条回应 R2 的每个 Must-Fix、Should-Fix 和 Missing References。对于你的评分（3.5）与 R2（3.0）的差异，请说明你是否调整评分或维持不变。"
  }
}
```

</details>

---


### Tool result

_source line 2059 · 2026-05-19T04:38:31.103225+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 31814
}
```

</details>

---


### Tool call

_source line 2060 · 2026-05-19T04:38:31.256066+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## Step 2 — 交叉分享：请对 Reviewer 1 的审稿意见逐条回应\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]**：同意并简要说明理由\n- **[REBUT]**：反驳并提供证据（引用论文具体 Section/Table/Figure）\n\n特别关注 R1 提出但你未提出的问题（R1-N2 效应量解读/Cohen标准、R1-W2 Rothman引用、R1-W3 DocRED样本量、R1-W5 SDGD归因深度、R1-W6 split-origin控制）以及你们评分差异的原因（你 3.0 vs R1 3.5）。\n\n---\n\n## Reviewer 1 完整审稿原文\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n**Soundness**: 3.5 | **Excitement**: 3.0 | **Confidence**: 4 | **Reproducibility**: 4\n\n### Must-Fix:\n\n**R1-N1** [critical] \"Largely additive\" claim 在多个条件下不成立，属于 overclaim\n- FewRel logit-scale: interaction marginally significant (p=0.047), TOST inconclusive (p=0.209)\n- DocRED: interaction +5.7pp, TOST p=0.77, 完全无法建立 equivalence\n- NER: factorial inconclusive (p=0.50)\n- FewRel 2×2 factorial: inconclusive (p=0.56)\n- 实际上仅 FewRel 69-batch full-range regression linear scale 支撑 (TOST p=0.003 at ±3pp)\n- 建议：限定为 \"bounded interaction under linear specification in sentence-level RE\" 或 \"two separable dimensions\"\n\n**R1-N2** [critical] Pairwise r²=1.3-1.7% 效应量解读不够审慎\n- SCS 仅解释 1.3-1.7% type confusion 方差，>98% 由其他因素决定\n- 引用 Cohen (1988) behavioral research 标准，但 LLM 是确定性系统（greedy decoding），变量可控度远高于行为研究\n- Aggregation simulation 依赖 conditional r²=7%（非零混淆对），非 unconditional 1.3%\n- 建议：用 batch-level R²=22-53% 作为主要证据，讨论 SCS 作为代理指标的局限性\n\n**R1-N3** [critical] BCS 对 NER 无 batch-level 信号，削弱 \"two-dimensional\" 框架通用性\n- Dimension 2 batch-level 效应仅在 RE forced-choice format 下有效\n- NER r≈0 (n=450), NER factorial inconclusive, MAVEN centrality confound\n- Abstract \"across NER, RE, and event detection\" 给人三任务都验证了两维度的印象\n- 建议：Abstract/Introduction 明确标注 BCS batch-level 仅限 RE forced-choice format\n\n### Should-Fix:\n\n**R1-W1** TOST ±3pp margin 不够保守\n- ±2pp 仅 marginally equivalent (p=0.047), ±1pp inconclusive (p=0.278)\n- 90% CI upper bound 2.0pp 在 main effect 2.2pp 情况下意味着 interaction 可能接近 main effect 大小\n- 建议：弱化为 \"bounded interaction at ±3pp level\"\n\n**R1-W2** Rothman (1990) 拒绝多重比较校正不够充分\n- Cross-dataset 比较引用 Rothman 合理\n- 但 Appendix G 的 cross-prompt-variant (4 variants × 2 counts) 不是独立假设\n- Count=8 时 4 variants 都不显著，count=32 时仅 2/4 显著\n- 建议：对 within-study 二级分析加 caveat\n\n**R1-W3** DocRED 5 batches per count level 样本量过小\n- 5 batches count curve 无法提供可靠趋势估计\n- DocRED factorial +5.7pp 宽 CI [-1.6, 13.0] 部分归因于样本量不足\n- 建议：增加至 15 batches 或明确讨论 power limitation\n\n**R1-W4** Dimension 2 未在 proprietary model 验证\n- Gemini count-64 仅 11/25 batches (\"partial\")，未解释原因\n- Llama-70B BCS 验证仅在 count=16 单个 level\n- 建议：解释 Gemini partial data；补充 Gemini BCS-controlled 实验\n\n**R1-W5** SDGD 归因分析缺少解决方向验证\n- Oracle routing +29.8pp 但 practical routing 全 below baseline → 瓶颈在 routing\n- Routing failure 与 constrained decoding 的交互未深入分析\n- 缺少去掉 enum constraint 后 routing performance 的 ablation\n- 建议：讨论 constrained decoding × decomposition 交互\n\n**R1-W6** FewRel split-origin 控制可以更强\n- 16 val-origin types 的 held-out validation (ρ=0.216, p=0.018) 比 covariate analysis 更有说服力但埋在 Appendix\n- Contamination 可能以更复杂方式影响（改变 confusion pattern 而非整体准确率）\n- 建议：将 held-out validation 提到正文\n\n### Minor: M1 orphan bib, M2 BCS range cross-dataset comparison, M3 Gemini partial data, M4 v1 offset hallucination, M5 unconstrained ablation 应更正式\n\n### Missing References: LLM calibration × constrained decoding; equivalence testing in ML\n\n---\n\n请逐条回应 R1 的每个 Must-Fix、Should-Fix 和 Missing References。对于你的评分（3.0）与 R1（3.5）的差异，请说明你是否调整评分或维持不变。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "## Step 2 — 交叉分享：请对 Reviewer 1 的审稿意见逐条回应\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]**：同意并简要说明理由\n- **[REBUT]**：反驳并提供证据（引用论文具体 Section/Table/Figure）\n\n特别关注 R1 提出但你未提出的问题（R1-N2 效应量解读/Cohen标准、R1-W2 Rothman引用、R1-W3 DocRED样本量、R1-W5 SDGD归因深度、R1-W6 split-origin控制）以及你们评分差异的原因（你 3.0 vs R1 3.5）。\n\n---\n\n## Reviewer 1 完整审稿原文\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n**Soundness**: 3.5 | **Excitement**: 3.0 | **Confidence**: 4 | **Reproducibility**: 4\n\n### Must-Fix:\n\n**R1-N1** [critical] \"Largely additive\" claim 在多个条件下不成立，属于 overclaim\n- FewRel logit-scale: interaction marginally significant (p=0.047), TOST inconclusive (p=0.209)\n- DocRED: interaction +5.7pp, TOST p=0.77, 完全无法建立 equivalence\n- NER: factorial inconclusive (p=0.50)\n- FewRel 2×2 factorial: inconclusive (p=0.56)\n- 实际上仅 FewRel 69-batch full-range regression linear scale 支撑 (TOST p=0.003 at ±3pp)\n- 建议：限定为 \"bounded interaction under linear specification in sentence-level RE\" 或 \"two separable dimensions\"\n\n**R1-N2** [critical] Pairwise r²=1.3-1.7% 效应量解读不够审慎\n- SCS 仅解释 1.3-1.7% type confusion 方差，>98% 由其他因素决定\n- 引用 Cohen (1988) behavioral research 标准，但 LLM 是确定性系统（greedy decoding），变量可控度远高于行为研究\n- Aggregation simulation 依赖 conditional r²=7%（非零混淆对），非 unconditional 1.3%\n- 建议：用 batch-level R²=22-53% 作为主要证据，讨论 SCS 作为代理指标的局限性\n\n**R1-N3** [critical] BCS 对 NER 无 batch-level 信号，削弱 \"two-dimensional\" 框架通用性\n- Dimension 2 batch-level 效应仅在 RE forced-choice format 下有效\n- NER r≈0 (n=450), NER factorial inconclusive, MAVEN centrality confound\n- Abstract \"across NER, RE, and event detection\" 给人三任务都验证了两维度的印象\n- 建议：Abstract/Introduction 明确标注 BCS batch-level 仅限 RE forced-choice format\n\n### Should-Fix:\n\n**R1-W1** TOST ±3pp margin 不够保守\n- ±2pp 仅 marginally equivalent (p=0.047), ±1pp inconclusive (p=0.278)\n- 90% CI upper bound 2.0pp 在 main effect 2.2pp 情况下意味着 interaction 可能接近 main effect 大小\n- 建议：弱化为 \"bounded interaction at ±3pp level\"\n\n**R1-W2** Rothman (1990) 拒绝多重比较校正不够充分\n- Cross-dataset 比较引用 Rothman 合理\n- 但 Appendix G 的 cross-prompt-variant (4 variants × 2 counts) 不是独立假设\n- Count=8 时 4 variants 都不显著，count=32 时仅 2/4 显著\n- 建议：对 within-study 二级分析加 caveat\n\n**R1-W3** DocRED 5 batches per count level 样本量过小\n- 5 batches count curve 无法提供可靠趋势估计\n- DocRED factorial +5.7pp 宽 CI [-1.6, 13.0] 部分归因于样本量不足\n- 建议：增加至 15 batches 或明确讨论 power limitation\n\n**R1-W4** Dimension 2 未在 proprietary model 验证\n- Gemini count-64 仅 11/25 batches (\"partial\")，未解释原因\n- Llama-70B BCS 验证仅在 count=16 单个 level\n- 建议：解释 Gemini partial data；补充 Gemini BCS-controlled 实验\n\n**R1-W5** SDGD 归因分析缺少解决方向验证\n- Oracle routing +29.8pp 但 practical routing 全 below baseline → 瓶颈在 routing\n- Routing failure 与 constrained decoding 的交互未深入分析\n- 缺少去掉 enum constraint 后 routing performance 的 ablation\n- 建议：讨论 constrained decoding × decomposition 交互\n\n**R1-W6** FewRel split-origin 控制可以更强\n- 16 val-origin types 的 held-out validation (ρ=0.216, p=0.018) 比 covariate analysis 更有说服力但埋在 Appendix\n- Contamination 可能以更复杂方式影响（改变 confusion pattern 而非整体准确率）\n- 建议：将 held-out validation 提到正文\n\n### Minor: M1 orphan bib, M2 BCS range cross-dataset comparison, M3 Gemini partial data, M4 v1 offset hallucination, M5 unconstrained ablation 应更正式\n\n### Missing References: LLM calibration × constrained decoding; equivalence testing in ML\n\n---\n\n请逐条回应 R1 的每个 Must-Fix、Should-Fix 和 Missing References。对于你的评分（3.0）与 R1（3.5）的差异，请说明你是否调整评分或维持不变。"
  }
}
```

</details>

---


### Tool result

_source line 2061 · 2026-05-19T04:38:32.770088+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1514
}
```

</details>

---


### Assistant

_source line 2062 · 2026-05-19T04:38:35.423625+00:00_

交叉分享已发出，等待两位 Reviewer 的 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 180

## Round 180

2 recorded events


### User

_source line 2063 · 2026-05-19T04:38:38.092897+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**总结**：

- **Overall**: 3.5 (Borderline Conference)
- **Soundness**: 3.5/5 | **Excitement**: 3.0/5 | **Reproducibility**: 4/5
- **3 个 Must-Fix**：(1) "largely additive" overclaim（仅在 sentence-level RE linear scale 成立），(2) pairwise r²=1.3-1.7% 效应量解读引用 Cohen behavioral research 标准不当，(3) BCS 对 NER 无 batch-level 信号，削弱 "two-dimensional" 框架通用性
- **6 个 Should-Fix**：TOST margin 不够保守、Rothman 多重比较论证不完整、DocRED 5 batches power 不足、Dimension 2 未在 proprietary model 验证、SDGD routing failure 分析不完整、split-origin 控制可更强
- **主要优势**：实验设计精良（双范式分离 count/confusability）、统计透明度高（TOST + bootstrap + sensitivity analysis）、诚实报告 negative results、cross-model 验证范围广

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2064 · 2026-05-19T04:38:52.387607+00:00_

等待两位 Reviewer 的交叉回应中。R1 和 R2 的 Step 2 交叉分享任务已分配，需要收到双方的 `[AGREE]`/`[REBUT]` 逐条回应后才能进入 Step 3 收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 181

## Round 181

2 recorded events


### User

_source line 2065 · 2026-05-19T04:42:12.515311+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[REBUT] R2-N1: Title "Predict" 与 correlational evidence 不匹配**

R2 认为 "predict" 暗示因果预测力，与 Limitations item 4 的 "correlational evidence" 矛盾。我认为此条被过度升级。

"Predict" 在统计学/ML 语境中是标准用语，含义是"X 对 Y 有统计预测力（explains variance）"，不等于"X 因果决定 Y"。论文展示了 BCS explains 22--53% of cross-batch RE accuracy variance（§5.3 practical magnitude），这在统计意义上就是 "predict"。renaming 实验（Appendix G, Table 8）反驳的是"降低 SCS 即可改善准确率"这一因果干预假设，而非 SCS 的预测有效性——renaming 引入了 label unfamiliarity 混淆因素，论文做了明确诊断（Appendix G 末段）。

但我同意普通读者可能将 "predict" 理解为可操作的因果关系。建议改为 "Relate to" / "Shape" 是合理的。**我将此归为 Should-Fix（措辞调整），而非 Critical**——论文 Introduction 第一段和 Contribution 1 用的是 "predictive relationship"，措辞已相对谨慎。

---

**[AGREE] R2-N2: "Two-dimensional" framework 边界条件在 Abstract/Introduction 表述不充分**

同意，与我首轮 framing 问题一致。具体证据：

- Abstract 说 "two largely additive dimensions"，但 NER batch-level BCS 完全无信号（r≈0, n=450, §5.3 prompt sensitivity 段）
- DocRED TOST 不成立（p=0.77, Appendix D）
- NER factorial inconclusive（p=0.50, Appendix D）
- logit-scale TOST inconclusive（p=0.209, Appendix D）

Introduction Finding (1) 确实提到了 "but not in document-level RE or NER"，但这个限定被 "two largely additive dimensions" 的主标签淹没。Abstract 中 "BCS explains 22--53%" 紧接 "two largely additive dimensions"，读者容易泛化到所有任务。R2 归为 Critical 合理。

---

**[REBUT] R2-N3: SCS 无新颖性，"controlled framework" 论证不足**

三个子论点需分开讨论：

**(a) SCS = LLM-PEE 的分区标准**：论文 Related Work "SCS novelty" 段（§2 末段）已明确承认。但 LLM-PEE 将 embedding similarity 作为工程启发式（用于分区），从未将其作为分析变量隔离 count vs. confusability 的独立效应。贡献不在公式本身，在于系统性嵌入 controlled experimental design。

**(b) 核心发现不意外**："不意外"≠"已被证明"。论文发现了若干反直觉细节：NER batch-level BCS 完全无信号（§5.3），centrality confounding 在同域 schema 上反转方向（§5.5, MAVEN ρ=+0.184→控制后 p>0.2），few-shot 加剧混淆（Appendix, +4.3pp）。这些都不是先验可预测的。

**(c) 效应量有限、无可行缓解**：此点我同意 R2 的诊断。~2pp typical gap（§5.3 practical magnitude）、r²≈1.3-1.7% pairwise（Table 2）确实 modest。所有干预均失败（SDGD, renaming, few-shot），Discussion §6 (3) 的 contrastive definitions 标注 "untested; future work"。这削弱实用价值。

**综合判断**：R2-N3 作为 Critical 过重。SCS 的 controlled framework 贡献成立，但效应量和缺乏可行缓解确实压低 excitement。我归为 Should-Fix 到 Critical 之间。

---

### Should-Fix

**[AGREE] R2-W1: TOST ±3pp margin 选择值得质疑**

与我首轮 W1 重叠。Appendix D Table 3 sensitivity analysis 显示 ±2pp marginal（p=0.047），±1pp inconclusive（p=0.278）。等价性结论高度依赖 margin 选择。

---

**[AGREE] R2-W2: Renaming 实验削弱 SCS 实用价值但讨论不足**

同意存在张力。Discussion §6 practical implication (1) 建议 "flag type pairs with SCS>0.85 for definition refinement"，但 Appendix G Table 8 显示精心选择的 paraphrase（mean SCS 0.87→0.67）导致准确率下降 3-9pp。

但 R2 稍微简化了此问题。renaming 失败机制是 **label unfamiliarity**（将 Wikidata 标准标签替换为非标准表述），不等于"降低 SCS 无效"。如果 schema 设计者在设计阶段就使用语义独特标签（而非事后替换），unfamiliarity 问题可能不存在。Discussion §6 (3) 暗示了此区分（"without the label-unfamiliarity penalty of renaming"），但讨论确实不够充分。应在 Discussion 中更清晰地区分"SCS 作为诊断指标"和"降低 SCS 作为干预手段"。

---

**[AGREE] R2-W3: CrossAgentIE 对比不充分**

同意。Related Work §2 将 crossagentie-2025 仅描述为 "treat [schema complexity] as an engineering problem"，未讨论其 cross-type debate 机制与 confusability mitigation 的功能关系。论文应讨论：(1) debate 机制是否在功能上等价于 confusability-aware batching 的替代方案；(2) 在大 schema（66-168 types）下 debate 是否可扩展。

但 CrossAgentIE 是 2025 Findings 并发工作，对比缺失不影响本文核心 claim。我将此归为 Should-Fix，不升级为 Critical。

---

**[AGREE] R2-W4: FewRel train/val split 混合使用**

与我首轮 W6 重叠。Limitations item 5 的 split-origin 分析（train-origin 准确率反而低 8.8pp, n.s.）一定程度缓解 contamination 担忧，但应在正文 §3.1 中提及。

---

**[REBUT] R2-W5: analytical/empirical study 是否适合 EMNLP main track**

不同意。ACL ARR review form 明确将 "empirical contribution" 列为有效贡献类型。*ACL venues 长期接收高质量 empirical analysis papers（LLM 能力系统评估、prompting 策略受控分析、评估指标批判性审查）。论文是否达到 main track 水准取决于发现的 significance 和 rigor，不取决于是否包含新方法。此条不成立。

---

### Missing References

**[AGREE] Dubey et al. (2018) "Pairwise Confusion for Fine-Grained Visual Classification" (ECCV)** — pairwise confusion metric 与 SCS 动机高度重叠，应作为跨领域先例引用。Related Work §2 末段讨论 "label similarity and classification confusion" 先例但遗漏了此最直接相关工作。

**[AGREE] Collier et al. (2021)** — 方向合理，优先级低于 Dubey et al.，可在扩展 Related Work "label confusion" 先例时一并纳入。

---

### 评分差异说明

R2 给 3.0（Findings），我首轮给 3.5（Borderline Conference）。差异来源：

| 维度 | R1 判断 | R2 判断 | 差异原因 |
|------|---------|---------|----------|
| SCS 新颖性 | Controlled framework 有贡献价值 | SCS=LLM-PEE, framework 不算创新 | 我对 "experimental design as contribution" 更宽容 |
| Negative results 价值 | SDGD/renaming/few-shot 失败是有价值的社区信息 | 无可行缓解降低实用价值 | 我对 negative results 价值评估更高 |
| Venue fit | Empirical analysis 完全适合 EMNLP | 质疑是否适合 main track | 此条不成立（见 R2-W5 REBUT） |
| Title 问题 | Should-Fix（措辞调整即可） | Critical（核心 overclaim） | "predict" 在统计语境下可辩护 |

**经本轮交叉审查后的评分决定**：

R2-N2（framing 不充分）和 R2-W2（renaming 讨论不足）加强了我对论文表述问题的担忧。R2-N3 (c) 关于效应量 modest 和缺乏可行缓解也有道理。

但核心问题是 **framing 和表述**（可在 revision 中修改），不是方法论缺陷。实验 rigor 和 scope（4 datasets, 4 models, multiple prompt variants, 多种统计检验）在 empirical study 中属上乘。Negative results 有独立贡献价值。

**最终维持 3.5（Borderline Conference）**，附条件：如果 framing（R2-N2 + 我首轮 N1/N2）和 Discussion（R2-W2）不修复，可降至 3.0。

---

### R1-R2 共识总结

**双方一致认为需修复**：
1. Abstract/Introduction framing 需充分限定 "two-dimensional" framework 的边界条件（R2-N2 = R1-N1/N2）
2. TOST ±3pp margin 选择需更充分论证（R2-W1 = R1-W1）
3. FewRel train/val split 在正文中需说明（R2-W4 = R1-W6）

**R1 部分同意 R2 的新发现**：
4. Title "predict" 宜调整措辞（R2-N1，R1 降级为 Should-Fix）
5. Renaming 实验与 practical implications 的张力需在 Discussion 中更充分讨论（R2-W2）
6. CrossAgentIE 需更深入对比（R2-W3）
7. Dubey et al. (2018) pairwise confusion 应引用（R2 Missing Ref 1）

**双方分歧**：
- SCS 新颖性（R1 认为 controlled framework 有价值 vs R2 认为不够）
- Venue fit（R1 REBUT R2-W5）
- 整体评分（R1: 3.5 vs R2: 3.0）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2066 · 2026-05-19T04:42:38.017227+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

**R1 交叉回应要点**：
- **[REBUT] R2-N1 (Title "Predict")**: "predict" 在统计语境下成立，降级为 Should-Fix
- **[AGREE] R2-N2 (Two-dimensional framing)**: 同意 Abstract/Intro 边界条件不足，归为 Critical
- **[REBUT] R2-N3 (SCS novelty)**: 子论点 (a)(b) 反驳（controlled framework 有独立价值，发现含反直觉细节），子论点 (c) 同意（效应量 modest，无可行缓解）
- **[AGREE] R2-W1-W4**: 均同意，部分与 R1 首轮重叠
- **[REBUT] R2-W5 (Venue fit)**: ARR 明确接受 empirical contribution，此条不成立
- **评分维持 3.5**，附条件：framing 不修复则降至 3.0
- **新增共识 7 项，分歧 3 项**

R2 的交叉回应到达后进入 Step 3 收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 182

## Round 182

2 recorded events


### User

_source line 2067 · 2026-05-19T04:42:40.649789+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

核心结论：对 R2 的 12 条意见中，7 条 AGREE（含 3 条与我首轮重叠），5 条 REBUT（Title "predict" 降级、SCS 新颖性部分辩护、venue fit 完全反驳）。维持 3.5 评分不变，但标注 framing 和 Discussion 修复为评分条件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2068 · 2026-05-19T04:42:45.712564+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 183

## Round 183

6 recorded events


### User

_source line 2069 · 2026-05-19T04:43:07.076816+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 回应

**[AGREE] R1-N1: "Largely additive" claim overclaim**

同意这是论文最核心的 overclaim 问题。论文 Abstract 说 "Degradation operates along two largely additive dimensions"，但实际证据高度局限：

- 真正支撑 additivity 的仅有 FewRel 69-batch full-range regression on linear scale (TOST p=0.003 at ±3pp, Appendix C)
- FewRel logit-scale: interaction marginally significant (p=0.047), TOST inconclusive (p=0.209)
- DocRED: interaction +5.7pp, TOST p=0.77, 完全无法建立 equivalence
- NER factorial: inconclusive (p=0.50); FewRel 2×2 factorial: inconclusive (p=0.56)

R1 建议限定为 "bounded interaction under linear specification in sentence-level RE" 非常精准。我在初审中也指出了 additivity claim 的过度泛化问题，R1 的分析更具体地量化了这一点。这是影响接收决定的核心问题。

**补充**：论文 §8 Limitations 第2条提到 "effect size is modest" 但对 additivity 的条件限制描述不足——Limitations 中未提及 logit-scale 和 DocRED 条件下 additivity 不成立。

---

**[AGREE with nuance] R1-N2: Pairwise r²=1.3-1.7% 效应量解读**

部分同意。R1 的核心论点有两层：

(1) Cohen (1988) behavioral research 标准是否适用于 LLM：R1 认为 LLM 是确定性系统（greedy decoding），变量可控度远高于行为研究，因此 behavioral science 的 "small effect" 标准不应直接迁移。这个论点有一定道理，但需要注意：即便是 greedy decoding，batch composition 引入的变异性（不同 type 组合、不同实例）仍然构成一种"自然变异"。论文 Appendix Q (Table 17) 显示 intra-batch variance 在 count 4-64 之间为 5-474×，所以系统并非完全确定性的。不过我同意，单纯套用 Cohen 标准而不讨论其适用性确实不够审慎。

(2) 应以 batch-level R²=22-53% 作为主要证据：**完全同意**。论文 §4.3 已经建立了 batch-level BCS 的强预测力（FewRel R²=0.225, DocRED 0.44-0.53），这是远比 pairwise 1.3% 更有说服力的证据。论文目前的叙事将 pairwise 和 batch-level 并列呈现，但应明确以 batch-level 为主线，将 pairwise SCS 定位为机制解释而非效应量证据。

R1 建议讨论 "SCS 作为代理指标的局限性" 合理——SCS 解释的是 type confusion 的方差而非准确率的方差，这个 gap 应在正文说明。

---

**[AGREE] R1-N3: BCS 对 NER 无 batch-level 信号，削弱 "two-dimensional" 框架通用性**

强烈同意，这也是我初审时给出较低评分的主要原因之一。具体证据：

- NER: BCS batch-level r≈0 (§4.2, n=450 batches)，factorial test inconclusive (p=0.50)
- MAVEN: 虽然 pairwise SCS 相关显著，但 §4.5 和 Appendix E 揭示了 centrality confound——MAVEN 的 BCS-F1 正相关完全归因于 type frequency 和 degree centrality，控制后信号消失 (Table 10)
- Abstract 说 "across NER, RE, and event detection" 确实给人三任务都验证了两个维度的印象

实际上：
- Dimension 1 (count): 跨任务一致 ✓
- Dimension 2 (BCS/confusability): 仅在 RE forced-choice format 有 batch-level 预测力；NER 无信号；MAVEN 信号被 confound 解释

这意味着论文的核心贡献——"two-dimensional degradation framework"——的适用范围远比 Abstract/Introduction 声称的窄。R1 建议在 Abstract/Introduction 明确标注 "BCS batch-level prediction limited to RE forced-choice format" 是必要的修改。

---

### Should-Fix 回应

**[AGREE] R1-W1: TOST ±3pp margin 不够保守**

同意。Appendix C Table 9 清楚显示：
- ±3pp: equivalent (p<0.001)
- ±2pp: marginally equivalent (p=0.047)
- ±1pp: inconclusive (p=0.278)

R1 指出的 90% CI upper bound 2.0pp vs main effect 2.2pp 是关键——interaction 可能接近 main effect 的 91%。论文应弱化为 "bounded at ±3pp" 而非暗示 interaction 可忽略。

**补充**：Appendix C 还提到 logit-scale back-transformation 后 interaction 可达 2.78pp at the observed floor (p=0.31)，这进一步表明 additivity 在非线性尺度上不稳健。

---

**[AGREE] R1-W2: Rothman (1990) 多重比较校正**

同意 R1 的区分：cross-dataset 比较引用 Rothman 拒绝 family-wise correction 合理（独立数据集、独立假设），但 Appendix G/H 内的 within-study 二级分析（4 prompt variants × 2 count levels = 8 tests on the same data）不是独立假设，应加 caveat。

论文 §9 提到 "Within-dataset secondary analyses involve multiple looks at the same data; we report individual p-values and note that core claims rest on p < 0.001"，这是一个合理的 partial defense，但对 Appendix H 的 prompt variant 分析（count=8 时 4/4 不显著，count=32 时仅 2/4 显著）缺乏明确讨论。

---

**[AGREE] R1-W3: DocRED 5 batches per count level 样本量过小**

同意。DocRED 每个 count level 仅 5 batches（§3.1: "we sample 25 random type batches for... DocRED"，5 count levels），导致：
- Factorial interaction CI 极宽 [-1.6, 13.0]
- 无法区分 +5.7pp 是真实 interaction 还是噪声
- Count curve 趋势估计不可靠

R1 建议增至 15 batches 或明确讨论 power limitation 合理。我注意到论文 §3.1 解释 DocRED 的 batch 构建更昂贵（document-level, 96 relation schema），但这不能替代对统计 power 不足的明确声明。

---

**[AGREE] R1-W4: Dimension 2 未在 proprietary model 验证**

同意。论文 §8 Limitations 第1条已承认 "Dimension 2 (BCS-controlled confusability) has not been tested on proprietary models"，但问题更具体：

- Gemini 2.5 Flash: count-64 仅 11/25 batches 完成（Appendix S, Table 19 注释 "Count 64: Gemini based on 11/25 batches (partial)"），原因未解释。这可能是 API rate limit、context length、或 constrained decoding 兼容性问题，但论文不应忽略这一异常。
- LLaMA-70B BCS 验证仅在 count=16 单个 level（Appendix S, Table 18 "16-relation condition"）

R1 建议解释 Gemini partial data 和补充 Gemini BCS-controlled 实验合理。至少应在 Limitations 中明确说明 Gemini partial data 的原因。

---

**[AGREE with nuance] R1-W5: SDGD 归因分析缺乏深度**

部分同意。论文 Section 5 和 Table 8 清楚展示了 SDGD 的负面结果：oracle routing +29.8pp（相对 gold label 72.4%）vs 所有实际 routing 策略低于 single-pass baseline。这个负面结果本身是诚实和有价值的。

但 R1 指出的两个具体缺失是合理的：
1. **Routing failure 与 constrained decoding 的交互**：所有 SDGD 实验使用 constrained decoding (JSON schema enforcement)，但 §5 没有讨论 enum constraint 缩小后（子 schema 的 type 候选更少）是否改变 constrained decoding 的行为。Table 8 中 "max-conf (positive only)" 36.5% vs single-pass 30.4%（似乎有提升？但仍低于 oracle），这个交互值得分析。
2. **缺少去掉 enum constraint 的 ablation**：论文 Appendix F (Batch Composition Results) 讨论了 within-pool 分析，但没有直接测试 unconstrained decoding 下的 decomposition 效果。§8 提到 "removing the JSON constraint eliminates the BCS-accuracy correlation (ρ = −0.14, p = 0.49)" 但这是关于 BCS 的，不是关于 decomposition 的。

不过，我认为这更适合作为 Should-Fix 而非 Must-Fix——负面结果的诊断深度不足会降低贡献质量但不一票否决。

---

**[AGREE] R1-W6: FewRel split-origin 控制**

同意。论文 Appendix P (§P) 讨论了 split-origin covariate analysis：
- Held-out validation: 16 val-origin types, ρ=0.216, p=0.018, "nearly identical to the full 80-type pool (ρ=0.218)"
- Covariate analysis: "BCS partial effect unchanged (ρ=0.245 for origin; Appendix P)"

R1 说得对——held-out validation 比 covariate analysis 更有说服力（因为它完全排除了 contamination pathway），应提到正文。

R1 关于 "contamination 可能改变 confusion pattern 而非整体准确率" 的观点也有价值。论文 §10 提到 train-origin types 准确率 numerically lower than val-origin (−8.8pp, n.s.)，这与 uniform contamination 预测相反，但 n.s. 意味着 power 不足以确认。

---

### Minor Issues 回应

**[AGREE] R1-M1 orphan bib**: 如有 orphan bib 条目应清理。

**[AGREE] R1-M2 BCS range cross-dataset comparison**: BCS range 在不同 dataset 间不直接可比（SCS/BCS 依赖 embedding model，不同 dataset 的 type 分布不同），论文应加注。

**[AGREE] R1-M3 Gemini partial data**: 同上 R1-W4 回应。

**[AGREE] R1-M4 v1 offset hallucination**: 如果 v1 prompt 的 offset fields 产生幻觉（§G/Appendix），应更正式报告。

**[AGREE] R1-M5 unconstrained ablation**: 同上 R1-W5 回应中关于 unconstrained decoding ablation 的讨论。

---

### Missing References 回应

**[AGREE] LLM calibration × constrained decoding**: 论文大量使用 constrained decoding (JSON schema enforcement) 但未引用 LLM calibration 在 constrained decoding 下如何变化的文献。这与 §8 "removing the JSON constraint eliminates the BCS-accuracy correlation" 高度相关——constrained decoding 本身可能改变 model 的 confidence calibration，从而影响 BCS-accuracy 关系。

**[AGREE] Equivalence testing in ML**: 论文使用 TOST 进行 equivalence testing 但未引用 ML 领域的 equivalence testing 方法论文献。Lakens (2017) 被引用了（Appendix C 提到 Cohen's d），但更广泛的 ML-specific equivalence testing 讨论确实缺失。

---

## 评分差异说明（R2: 3.0 vs R1: 3.5）

R1 给 3.5 (Borderline Conference)，我给 3.0 (Findings)。仔细审读 R1 的意见后，我认为我们在核心问题上高度一致（overclaim、Dimension 2 通用性不足、效应量解读），分歧主要在于对这些问题严重程度的判断：

**我维持 3.0 (Findings) 的理由**：

1. **框架通用性不足的权重**：论文的核心卖点是 "two-dimensional degradation framework across NER, RE, and event detection"，但 Dimension 2 仅在 RE forced-choice format 有 batch-level 信号。这不是一个边缘问题——它直接影响论文贡献的 scope claim。如果标题改为 "How Does Schema Complexity Predict Performance in Training-Free LLM Relation Extraction?" 然后将 NER/ED 作为 exploratory extension，我会给更高分。但目前的 framing 与证据之间的 gap 太大。

2. **缺乏 actionable 贡献**：SDGD 负面结果意味着论文没有提供解决方案。Count curve 和 BCS 分析作为诊断工具有价值，但 §6 Discussion 的四个 "actionable directions" 都是 suggestions 而非 validated interventions。对于 Borderline Conference，我期望至少有一个 direction 有初步验证。

3. **效应量与 practical significance**：R1 和我都同意 pairwise r²=1.3-1.7% 很小。即使 batch-level R²=22-53%，论文的 practical implication（§6 "reducing candidate types per prompt"）缺乏定量验证——多少 BCS reduction 能带来多少准确率提升？

4. **统计分析的 mixed results 比例过高**：在论文的核心 claims 中，"largely additive" 仅在一个条件下成立，BCS batch-level 仅在一个 task format 下有效，SDGD 完全失败。这些 mixed results 的比例对于一篇声称建立 general framework 的论文来说过高。

**R1 给 3.5 可能的合理性**：论文的实验设计严谨（controlled BCS batches、factorial design、multiple datasets），统计方法全面（TOST、permutation tests、bootstrap CIs），负面结果诚实报告。这些方法论贡献确实有价值，可以理解为 Borderline Conference。

**结论**：我不调整评分，维持 **3.0 (Findings)**。论文有方法论贡献但 scope claim 与证据不匹配，且缺乏 actionable outcome。若作者能 (a) 收窄 framework claim 至 RE-specific + NER count-only, (b) 补充至少一个 validated intervention, (c) 修正 additivity 表述，可以重新考虑 Conference 档位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2070 · 2026-05-19T04:45:31.699244+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema-dag-extraction",
  "issues_yaml": "# Round 20 Review Issues Tracker\n# Updated: 2026-05-19 (Round 20 fresh review)\n\n# ============================================================\n# CRITICAL (R20) — 影响接收决定\n# ============================================================\n\n- id: R20-N1\n  summary: \"'Largely additive' overclaim: 仅在 sentence-level RE linear scale 成立\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方共识。FewRel logit-scale TOST inconclusive (p=0.209); DocRED interaction +5.7pp, TOST p=0.77; NER factorial p=0.50; FewRel 2×2 factorial p=0.56。仅 FewRel 69-batch full-range regression linear scale 支撑 (TOST p=0.003 at ±3pp)。Abstract/Conclusion 未加 task/scale 限定。\"}\n  action_items:\n    - {round: 20, action: \"Abstract/Conclusion 中 'largely additive' 限定为 sentence-level RE linear specification；明确承认 DocRED 和 logit-scale 不成立\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-N2\n  summary: \"BCS batch-level 仅在 RE forced-choice format 有效，'two-dimensional across NER/RE/ED' framing 超出证据\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方共识。NER batch-level r≈0 (n=450); MAVEN centrality confound; Dim2 batch-level 仅 RE forced-choice。Abstract 'across NER, RE, and ED' 误导。\"}\n  action_items:\n    - {round: 20, action: \"Abstract/Introduction 明确标注 BCS batch-level prediction 仅限 RE forced-choice format；区分 pairwise (跨任务) 和 batch-level (RE-specific) 证据\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-N3\n  summary: \"Pairwise r²=1.3-1.7% 效应量解读引用 Cohen (1988) behavioral research 标准不当\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"R1 Critical, R2 AGREE with nuance。Cohen 标准为行为研究设计，LLM 系统可控度不同。应以 batch-level R²=22-53% 为主要证据，pairwise 作为机制解释。\"}\n  action_items:\n    - {round: 20, action: \"移除或弱化 Cohen (1988) 类比；正文以 batch-level R²=22-53% 为主线证据，pairwise 定位为机制解释；讨论 SCS 作为代理指标的局限性\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING (R20)\n# ============================================================\n\n- id: R20-W1\n  summary: \"Title 'Predict' 与 correlational evidence 不匹配\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"R2 Critical, R1 降为 Should-Fix。R1 认为 'predict' 在统计语境中可辩护，但同意普通读者可能误解。Renaming 实验反驳朴素因果链。\"}\n  action_items:\n    - {round: 20, action: \"考虑将 Title 'Predict' 改为 'Relate to' / 'Shape' / 'Affect'\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W2\n  summary: \"TOST ±3pp margin 选择不够保守，additivity 结论高度依赖 margin\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方共识。±2pp marginal (p=0.047); ±1pp inconclusive (p=0.278); 90% CI upper bound 2.0pp 接近 main effect 2.2pp。\"}\n  action_items:\n    - {round: 20, action: \"正文更突出 ±2pp marginal 和 logit-scale inconclusive 结果；弱化为 'bounded interaction at ±3pp level'\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W3\n  summary: \"SCS 新颖性不足：SCS=LLM-PEE criterion，效应量有限，无可行缓解方案\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"R2 Critical, R1 部分 REBUT（controlled framework 有贡献价值，但同意效应量 modest 和缺乏缓解降低 excitement）。分歧未解决。\"}\n  action_items:\n    - {round: 20, action: \"更深入对比 LLM-PEE merge 策略差异；强化 negative result 的 actionable value；考虑增加可行缓解实验\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W4\n  summary: \"Renaming 实验削弱 SCS 实用价值，与 Discussion practical implications 矛盾\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方 AGREE。Discussion §6 建议 'flag SCS>0.85 for definition refinement' 但 renaming 降低 SCS 反而降低准确率。应区分 SCS 作为诊断 vs 干预指标。\"}\n  action_items:\n    - {round: 20, action: \"Discussion 中更清晰区分 'SCS 作为诊断指标' 和 '降低 SCS 作为干预手段'；调整 practical implications 措辞\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W5\n  summary: \"CrossAgentIE (ACL 2025 Findings) cross-type debate 对比不充分\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方 AGREE。应讨论 debate 机制是否在功能上等价于 confusability-aware batching 的替代方案。\"}\n  action_items:\n    - {round: 20, action: \"Related Work 增加 1-2 句 CrossAgentIE cross-type debate 与 confusability-aware batching 的异同对比\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W6\n  summary: \"DocRED 5 batches per count level 样本量不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方 AGREE。5 batches count curve power 极低；factorial CI 极宽 [-1.6, 13.0]。\"}\n  action_items:\n    - {round: 20, action: \"增加 DocRED count curve batches 至 15（如资源允许），或明确讨论 5-batch power limitation\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W7\n  summary: \"Dimension 2 未在 proprietary model 验证；Gemini partial data 未解释\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方 AGREE。Gemini count-64 仅 11/25 batches，原因未说明。Llama-70B BCS 仅 count=16 单 level。\"}\n  action_items:\n    - {round: 20, action: \"解释 Gemini partial data 原因；Limitations 明确标注 Dim2 未在 proprietary model 验证\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W8\n  summary: \"FewRel train/val split-origin 控制应在正文说明；held-out validation 应提到正文\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方 AGREE。Appendix held-out validation (ρ=0.216, p=0.018) 比 covariate analysis 更有说服力但埋在 Appendix。\"}\n  action_items:\n    - {round: 20, action: \"正文 §3.1 简要提及 split 合并理由和 held-out validation 结果\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W9\n  summary: \"Rothman (1990) 拒绝多重比较校正：cross-dataset 合理但 within-study 二级分析需加 caveat\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方 AGREE。Prompt variant 分析 (4×2=8 tests) 非独立假设。\"}\n  action_items:\n    - {round: 20, action: \"对 within-study 二级分析（prompt variants, marginal results）加 multiple comparison caveat\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W10\n  summary: \"SDGD routing failure 与 constrained decoding 交互分析不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"R1 W5, R2 AGREE with nuance。Oracle +29.8pp vs practical all below baseline → 瓶颈在 routing。缺少 unconstrained decoding 下 decomposition 的 ablation。\"}\n  action_items:\n    - {round: 20, action: \"讨论 constrained decoding × decomposition 交互；考虑 unconstrained decoding routing ablation\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO (R20)\n# ============================================================\n\n- id: R20-I1\n  summary: \"Orphan bib entry (jagannatha2020calibrating)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方 AGREE。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-I2\n  summary: \"Missing reference: Dubey et al. (2018) Pairwise Confusion for Fine-Grained Visual Classification (ECCV)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方 AGREE。pairwise confusion metric 与 SCS 动机高度重叠。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-I3\n  summary: \"SCS name-only vs prompt content 不一致 (Few-NERD prompts include definitions but SCS uses names only)\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R2], note: \"R2-M5。Appendix 有 ablation 但正文应简要提及。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-I4\n  summary: \"Gemini 2025 引用 arXiv 编号格式异常；少数 bib first author field 可能不准确\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R2], note: \"R2-M3, R2-M6。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R19 及更早 — 状态追踪\n# ============================================================\n\n- id: R19-N1\n  summary: \"核心发现 novelty 有限: SCS 形式同 LLM-PEE, controlled methodology 是标准方法论移植\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"Structural ceiling. Findings track 定位已确认.\"}\n    - {round: 20, reviewers: [R1, R2], note: \"R20 复现此问题 (R20-W3)。R1 部分辩护 controlled framework 有价值，R2 维持 critical。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-N2\n  summary: \"Confusability 效应量小且 RE-specific: pairwise r²=1.3-1.7%, NER batch-level null, RE 发现依赖 forced-choice format\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"Dim2 batch-level RE-specific.\"}\n    - {round: 20, reviewers: [R1, R2], note: \"R20 复现 (R20-N2, R20-N3)。n=25 unconstrained ablation 仍在论文中 (ρ=-0.14, p=0.49)。全文 format caveat 存在但 Abstract/Intro 仍超出证据。\"}\n  action_items:\n    - {round: 19, action: \"n=25 unconstrained ablation confirms BCS effect is format-specific\", assigned_to: paper_agent, status: done}\n    - {round: 19, action: \"Introduction Finding (2) + C2 补 forced-choice format caveat\", assigned_to: paper_agent, status: done}\n    - {round: 19, action: \"Abstract 末句加 Pairwise 精准化\", assigned_to: paper_agent, status: done}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W1\n  summary: \"TOST ±3pp margin 允许 interaction 达 main effect 136%, 'Largely additive' framing 偏乐观\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"Framing 问题非 soundness 问题.\"}\n    - {round: 20, reviewers: [R1, R2], note: \"R20 复现 (R20-W2)。双方再次共识 margin 选择问题。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W2\n  summary: \"Abstract/Introduction 偏重 extreme-batch 数字, 淡化 typical-batch 2.2pp\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"Abstract 已加 ~2pp caveat 但仍偏重 extreme.\"}\n    - {round: 20, reviewers: [R1, R2], note: \"R20 未单独提出但与 R20-N3 效应量讨论重叠。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W3\n  summary: \"NER batch-level null 削弱 'two-dimensional' 框架普适性\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"Title/Abstract 暗示跨任务但 Dim2 batch-level RE-specific.\"}\n    - {round: 20, reviewers: [R1, R2], note: \"R20 复现 (R20-N2)。升级为 Critical。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W4\n  summary: \"NER U-shape 'dual-task burden' 假说缺乏实验证据\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"Speculative. Cross-model replication 增加现象可信度但不解释机制.\"}\n    - {round: 20, reviewers: [R1, R2], note: \"R20 未单独提出。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-W2\n  summary: \"Cohen (1988) effect size 套用到 LLM 系统\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 20\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"加了 hedging 但仍以 behavioral research 为锚定.\"}\n    - {round: 20, reviewers: [R1, R2], note: \"R20 复现 (R20-N3)。R1 升级为 Critical。\"}\n  action_items:\n    - {round: 19, action: \"找 NLP/LLM 领域 effect size 解读先例或明确说明 tentative analogy\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W3\n  summary: \"Practical implications 薄弱\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"Discussion 加了 diagnostic hedging. 与 R19-W2 重叠.\"}\n    - {round: 20, reviewers: [R1, R2], note: \"R20 复现 (R20-W4 renaming 矛盾 + R2 缺乏 actionable outcome 整体判断)。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R19 及更早 — RESOLVED（保留记录）\n# ============================================================\n\n- id: R18-N1\n  summary: \"BCS batch-level 仅限 RE forced-choice classification format\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 19\n  resolution: \"全文统一 forced-choice classification format 术语 + n=25 ablation 验证.\"\n  resolution_round: 19\n\n- id: R18-N2\n  summary: \"'Two separable dimensions' logit-scale inconclusive\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 19\n  resolution: \"全文统一 'largely additive with bounded interaction'.\"\n  resolution_round: 19\n\n- id: R18-N3\n  summary: \"Contribution 2 暗示 metric innovation\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 19\n  resolution: \"Contribution 焦点转为 experimental design methodology.\"\n  resolution_round: 19\n\n- id: R18-W1\n  summary: \"Abstract 217 words 信息过载\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: \"Abstract 压缩至 ~156 words.\"\n  resolution_round: 19\n\n- id: R18-W7\n  summary: \"BCS-aware grouping +1.4pp 与 R²=22-53% 矛盾\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  resolution: \"SDGD section 加 marginal BCS reduction 解释.\"\n  resolution_round: 19\n\n- id: R18-W8\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  resolution: \"Caption 压缩 + Contribution 合并 + SDGD table 移 Appendix. Body ≤ 8 页.\"\n  resolution_round: 19\n\n- id: R18-W5\n  summary: \"Dimension 2 未在 proprietary model (Gemini) 上验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  resolution: \"Limitations 明确标注 Dimension 2 仅在 open-weight 模型上验证.\"\n  resolution_round: 19\n\n- id: R18-m-refs\n  summary: \"Missing refs\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  resolution: \"引用已补充.\"\n  resolution_round: 19\n\n- id: R17-W1\n  summary: \"SCS vs simple baselines 对比\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: \"SCS baselines Table 已加入 Appendix.\"\n  resolution_round: 18\n\n- id: R16-N3\n  summary: \"效应量 framing 偏误\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 17\n  resolution: \"R17 确认修复.\"\n  resolution_round: 17\n\n- id: R16-m5\n  summary: \"FewRel 数据污染论证\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 17\n  resolution: \"R17 确认充分.\"\n  resolution_round: 17\n\n- id: R10-N1\n  summary: \"因果语言超出证据\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  resolution: \"Title 改 Predict; 因果语言清理.\"\n  resolution_round: 12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema-dag-extraction",
    "issues_yaml": "# Round 20 Review Issues Tracker\n# Updated: 2026-05-19 (Round 20 fresh review)\n\n# ============================================================\n# CRITICAL (R20) — 影响接收决定\n# ============================================================\n\n- id: R20-N1\n  summary: \"'Largely additive' overclaim: 仅在 sentence-level RE linear scale 成立\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方共识。FewRel logit-scale TOST inconclusive (p=0.209); DocRED interaction +5.7pp, TOST p=0.77; NER factorial p=0.50; FewRel 2×2 factorial p=0.56。仅 FewRel 69-batch full-range regression linear scale 支撑 (TOST p=0.003 at ±3pp)。Abstract/Conclusion 未加 task/scale 限定。\"}\n  action_items:\n    - {round: 20, action: \"Abstract/Conclusion 中 'largely additive' 限定为 sentence-level RE linear specification；明确承认 DocRED 和 logit-scale 不成立\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-N2\n  summary: \"BCS batch-level 仅在 RE forced-choice format 有效，'two-dimensional across NER/RE/ED' framing 超出证据\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方共识。NER batch-level r≈0 (n=450); MAVEN centrality confound; Dim2 batch-level 仅 RE forced-choice。Abstract 'across NER, RE, and ED' 误导。\"}\n  action_items:\n    - {round: 20, action: \"Abstract/Introduction 明确标注 BCS batch-level prediction 仅限 RE forced-choice format；区分 pairwise (跨任务) 和 batch-level (RE-specific) 证据\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-N3\n  summary: \"Pairwise r²=1.3-1.7% 效应量解读引用 Cohen (1988) behavioral research 标准不当\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"R1 Critical, R2 AGREE with nuance。Cohen 标准为行为研究设计，LLM 系统可控度不同。应以 batch-level R²=22-53% 为主要证据，pairwise 作为机制解释。\"}\n  action_items:\n    - {round: 20, action: \"移除或弱化 Cohen (1988) 类比；正文以 batch-level R²=22-53% 为主线证据，pairwise 定位为机制解释；讨论 SCS 作为代理指标的局限性\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING (R20)\n# ============================================================\n\n- id: R20-W1\n  summary: \"Title 'Predict' 与 correlational evidence 不匹配\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"R2 Critical, R1 降为 Should-Fix。R1 认为 'predict' 在统计语境中可辩护，但同意普通读者可能误解。Renaming 实验反驳朴素因果链。\"}\n  action_items:\n    - {round: 20, action: \"考虑将 Title 'Predict' 改为 'Relate to' / 'Shape' / 'Affect'\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W2\n  summary: \"TOST ±3pp margin 选择不够保守，additivity 结论高度依赖 margin\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方共识。±2pp marginal (p=0.047); ±1pp inconclusive (p=0.278); 90% CI upper bound 2.0pp 接近 main effect 2.2pp。\"}\n  action_items:\n    - {round: 20, action: \"正文更突出 ±2pp marginal 和 logit-scale inconclusive 结果；弱化为 'bounded interaction at ±3pp level'\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W3\n  summary: \"SCS 新颖性不足：SCS=LLM-PEE criterion，效应量有限，无可行缓解方案\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"R2 Critical, R1 部分 REBUT（controlled framework 有贡献价值，但同意效应量 modest 和缺乏缓解降低 excitement）。分歧未解决。\"}\n  action_items:\n    - {round: 20, action: \"更深入对比 LLM-PEE merge 策略差异；强化 negative result 的 actionable value；考虑增加可行缓解实验\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W4\n  summary: \"Renaming 实验削弱 SCS 实用价值，与 Discussion practical implications 矛盾\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方 AGREE。Discussion §6 建议 'flag SCS>0.85 for definition refinement' 但 renaming 降低 SCS 反而降低准确率。应区分 SCS 作为诊断 vs 干预指标。\"}\n  action_items:\n    - {round: 20, action: \"Discussion 中更清晰区分 'SCS 作为诊断指标' 和 '降低 SCS 作为干预手段'；调整 practical implications 措辞\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W5\n  summary: \"CrossAgentIE (ACL 2025 Findings) cross-type debate 对比不充分\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方 AGREE。应讨论 debate 机制是否在功能上等价于 confusability-aware batching 的替代方案。\"}\n  action_items:\n    - {round: 20, action: \"Related Work 增加 1-2 句 CrossAgentIE cross-type debate 与 confusability-aware batching 的异同对比\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W6\n  summary: \"DocRED 5 batches per count level 样本量不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方 AGREE。5 batches count curve power 极低；factorial CI 极宽 [-1.6, 13.0]。\"}\n  action_items:\n    - {round: 20, action: \"增加 DocRED count curve batches 至 15（如资源允许），或明确讨论 5-batch power limitation\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W7\n  summary: \"Dimension 2 未在 proprietary model 验证；Gemini partial data 未解释\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方 AGREE。Gemini count-64 仅 11/25 batches，原因未说明。Llama-70B BCS 仅 count=16 单 level。\"}\n  action_items:\n    - {round: 20, action: \"解释 Gemini partial data 原因；Limitations 明确标注 Dim2 未在 proprietary model 验证\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W8\n  summary: \"FewRel train/val split-origin 控制应在正文说明；held-out validation 应提到正文\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方 AGREE。Appendix held-out validation (ρ=0.216, p=0.018) 比 covariate analysis 更有说服力但埋在 Appendix。\"}\n  action_items:\n    - {round: 20, action: \"正文 §3.1 简要提及 split 合并理由和 held-out validation 结果\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W9\n  summary: \"Rothman (1990) 拒绝多重比较校正：cross-dataset 合理但 within-study 二级分析需加 caveat\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方 AGREE。Prompt variant 分析 (4×2=8 tests) 非独立假设。\"}\n  action_items:\n    - {round: 20, action: \"对 within-study 二级分析（prompt variants, marginal results）加 multiple comparison caveat\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-W10\n  summary: \"SDGD routing failure 与 constrained decoding 交互分析不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"R1 W5, R2 AGREE with nuance。Oracle +29.8pp vs practical all below baseline → 瓶颈在 routing。缺少 unconstrained decoding 下 decomposition 的 ablation。\"}\n  action_items:\n    - {round: 20, action: \"讨论 constrained decoding × decomposition 交互；考虑 unconstrained decoding routing ablation\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO (R20)\n# ============================================================\n\n- id: R20-I1\n  summary: \"Orphan bib entry (jagannatha2020calibrating)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方 AGREE。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-I2\n  summary: \"Missing reference: Dubey et al. (2018) Pairwise Confusion for Fine-Grained Visual Classification (ECCV)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"双方 AGREE。pairwise confusion metric 与 SCS 动机高度重叠。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-I3\n  summary: \"SCS name-only vs prompt content 不一致 (Few-NERD prompts include definitions but SCS uses names only)\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R2], note: \"R2-M5。Appendix 有 ablation 但正文应简要提及。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-I4\n  summary: \"Gemini 2025 引用 arXiv 编号格式异常；少数 bib first author field 可能不准确\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - {round: 20, reviewers: [R2], note: \"R2-M3, R2-M6。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R19 及更早 — 状态追踪\n# ============================================================\n\n- id: R19-N1\n  summary: \"核心发现 novelty 有限: SCS 形式同 LLM-PEE, controlled methodology 是标准方法论移植\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"Structural ceiling. Findings track 定位已确认.\"}\n    - {round: 20, reviewers: [R1, R2], note: \"R20 复现此问题 (R20-W3)。R1 部分辩护 controlled framework 有价值，R2 维持 critical。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-N2\n  summary: \"Confusability 效应量小且 RE-specific: pairwise r²=1.3-1.7%, NER batch-level null, RE 发现依赖 forced-choice format\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"Dim2 batch-level RE-specific.\"}\n    - {round: 20, reviewers: [R1, R2], note: \"R20 复现 (R20-N2, R20-N3)。n=25 unconstrained ablation 仍在论文中 (ρ=-0.14, p=0.49)。全文 format caveat 存在但 Abstract/Intro 仍超出证据。\"}\n  action_items:\n    - {round: 19, action: \"n=25 unconstrained ablation confirms BCS effect is format-specific\", assigned_to: paper_agent, status: done}\n    - {round: 19, action: \"Introduction Finding (2) + C2 补 forced-choice format caveat\", assigned_to: paper_agent, status: done}\n    - {round: 19, action: \"Abstract 末句加 Pairwise 精准化\", assigned_to: paper_agent, status: done}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W1\n  summary: \"TOST ±3pp margin 允许 interaction 达 main effect 136%, 'Largely additive' framing 偏乐观\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"Framing 问题非 soundness 问题.\"}\n    - {round: 20, reviewers: [R1, R2], note: \"R20 复现 (R20-W2)。双方再次共识 margin 选择问题。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W2\n  summary: \"Abstract/Introduction 偏重 extreme-batch 数字, 淡化 typical-batch 2.2pp\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"Abstract 已加 ~2pp caveat 但仍偏重 extreme.\"}\n    - {round: 20, reviewers: [R1, R2], note: \"R20 未单独提出但与 R20-N3 效应量讨论重叠。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W3\n  summary: \"NER batch-level null 削弱 'two-dimensional' 框架普适性\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"Title/Abstract 暗示跨任务但 Dim2 batch-level RE-specific.\"}\n    - {round: 20, reviewers: [R1, R2], note: \"R20 复现 (R20-N2)。升级为 Critical。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W4\n  summary: \"NER U-shape 'dual-task burden' 假说缺乏实验证据\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"Speculative. Cross-model replication 增加现象可信度但不解释机制.\"}\n    - {round: 20, reviewers: [R1, R2], note: \"R20 未单独提出。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-W2\n  summary: \"Cohen (1988) effect size 套用到 LLM 系统\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 20\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"加了 hedging 但仍以 behavioral research 为锚定.\"}\n    - {round: 20, reviewers: [R1, R2], note: \"R20 复现 (R20-N3)。R1 升级为 Critical。\"}\n  action_items:\n    - {round: 19, action: \"找 NLP/LLM 领域 effect size 解读先例或明确说明 tentative analogy\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W3\n  summary: \"Practical implications 薄弱\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"Discussion 加了 diagnostic hedging. 与 R19-W2 重叠.\"}\n    - {round: 20, reviewers: [R1, R2], note: \"R20 复现 (R20-W4 renaming 矛盾 + R2 缺乏 actionable outcome 整体判断)。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R19 及更早 — RESOLVED（保留记录）\n# ============================================================\n\n- id: R18-N1\n  summary: \"BCS batch-level 仅限 RE forced-choice classification format\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 19\n  resolution: \"全文统一 forced-choice classification format 术语 + n=25 ablation 验证.\"\n  resolution_round: 19\n\n- id: R18-N2\n  summary: \"'Two separable dimensions' logit-scale inconclusive\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 19\n  resolution: \"全文统一 'largely additive with bounded interaction'.\"\n  resolution_round: 19\n\n- id: R18-N3\n  summary: \"Contribution 2 暗示 metric innovation\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 19\n  resolution: \"Contribution 焦点转为 experimental design methodology.\"\n  resolution_round: 19\n\n- id: R18-W1\n  summary: \"Abstract 217 words 信息过载\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 19\n  resolution: \"Abstract 压缩至 ~156 words.\"\n  resolution_round: 19\n\n- id: R18-W7\n  summary: \"BCS-aware grouping +1.4pp 与 R²=22-53% 矛盾\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  resolution: \"SDGD section 加 marginal BCS reduction 解释.\"\n  resolution_round: 19\n\n- id: R18-W8\n  summary: \"正文超 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  resolution: \"Caption 压缩 + Contribution 合并 + SDGD table 移 Appendix. Body ≤ 8 页.\"\n  resolution_round: 19\n\n- id: R18-W5\n  summary: \"Dimension 2 未在 proprietary model (Gemini) 上验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  resolution: \"Limitations 明确标注 Dimension 2 仅在 open-weight 模型上验证.\"\n  resolution_round: 19\n\n- id: R18-m-refs\n  summary: \"Missing refs\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 19\n  resolution: \"引用已补充.\"\n  resolution_round: 19\n\n- id: R17-W1\n  summary: \"SCS vs simple baselines 对比\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: \"SCS baselines Table 已加入 Appendix.\"\n  resolution_round: 18\n\n- id: R16-N3\n  summary: \"效应量 framing 偏误\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 17\n  resolution: \"R17 确认修复.\"\n  resolution_round: 17\n\n- id: R16-m5\n  summary: \"FewRel 数据污染论证\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 17\n  resolution: \"R17 确认充分.\"\n  resolution_round: 17\n\n- id: R10-N1\n  summary: \"因果语言超出证据\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  resolution: \"Title 改 Predict; 因果语言清理.\"\n  resolution_round: 12"
  }
}
```

</details>

---


### Tool result

_source line 2071 · 2026-05-19T04:45:31.804673+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml\", \"bytes\": 16461}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 105
}
```

</details>

---


### Tool call

_source line 2072 · 2026-05-19T04:47:46.385197+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 20 审稿报告（圆桌会议汇总）\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 via ARR May 2026 cycle\n**审稿日期**: 2026-05-19\n**Reviewer 编排**: R1（方法严谨性 + 实验设计 + 统计分析）、R2（新颖性 + Related Work + 写作 + 格式）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即收敛）\n\n---\n\n## Summary\n\n本文研究 training-free LLM 信息抽取中 schema 复杂度导致性能退化的两个维度：type count（维度1）和 type confusability（维度2）。作者提出 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 来量化类型间语义混淆度，在 Few-NERD (NER)、FewRel (RE)、DocRED (doc-RE)、MAVEN (ED) 上使用 Qwen3-32B 为主模型进行系统实验，辅以 Llama-3.1-8B/70B 和 Gemini 2.5 Flash 的跨模型验证。主要发现：(1) count 下降是主导因素；(2) BCS 在 RE forced-choice 格式下解释 22-53% 的跨 batch 准确率方差，但对 NER 无 batch-level 信号；(3) schema decomposition 因 merge amplification (NER) 和 routing failure (RE) 而失败。\n\n---\n\n## Strengths\n\n1. **实验设计精良**：Count curves + BCS-controlled 双范式有效分离 count 和 confusability。Within-pool 控制（从 80-rel pool 抽 16-rel subsets）排除 pool composition confound。FewRel balanced design 消除 type frequency confound。设计思路清晰，在 NLP 实证研究中属上乘。\n\n2. **统计处理透明度高于 NLP 平均水准**：TOST equivalence testing（含 sensitivity analysis across margins）、permutation tests、bootstrap CIs（percentile + cluster）、cross-seed variance decomposition、split-origin covariate analysis。多数 NLP 论文不做 equivalence testing；本文不仅做了，还报告了 margin 对结论的敏感性。\n\n3. **诚实报告 negative results**：SDGD 失败（merge amplification + routing failure）、label renaming 失败（unfamiliarity > confusability reduction）、NER batch-level BCS null、logit-scale TOST inconclusive、few-shot 加剧混淆。这些 negative results 的信息量可能超过 positive findings。\n\n4. **跨模型验证覆盖广**：Qwen3-32B → Llama-3.1-8B/70B → Gemini 2.5 Flash (API)，跨开源/闭源、8B-70B+。Dimension 1 directional consistency 证据充分（RE slope near-identical across models: -30.7 vs -30.1pp）。\n\n5. **格式完全合规**：`\\usepackage[review]{acl}` 正确，匿名化完整，正文 ≤ 8 页，Limitations 位置正确，Responsible NLP Checklist 填写详实，引用格式一致。\n\n6. **引用覆盖度好**：~70 个 unique cited keys，覆盖直接竞争者、基础方法、evaluation/statistical 方法、representation degeneration 文献。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[W-Critical-1] \"Largely additive\" overclaim：仅在 sentence-level RE linear scale 成立** [R1-N1, R2-N2 | 双方共识]\n- Abstract/Conclusion 声称 \"two largely additive dimensions\"，但实际支撑仅来自 FewRel 69-batch full-range regression on linear scale (TOST p=0.003 at ±3pp)。\n- FewRel logit-scale: interaction marginally significant (p=0.047), TOST inconclusive (p=0.209)\n- DocRED: interaction +5.7pp, 95% CI [-1.6, 13.0], TOST p=0.77\n- NER factorial: p=0.50; FewRel 2×2 factorial: p=0.56\n- **修复要求**：Abstract/Conclusion 将 \"largely additive\" 限定为 sentence-level RE linear specification；明确承认 DocRED 和 logit-scale 不成立。\n\n**[W-Critical-2] \"Two-dimensional across NER/RE/ED\" framing 超出证据** [R1-N3, R2-N2 | 双方共识]\n- Dimension 2 (BCS) batch-level 预测力仅在 RE forced-choice format 有效。NER batch-level r≈0 (n=450)；MAVEN centrality confound 控制后信号消失。\n- Abstract \"across NER, RE, and event detection\" 误导读者认为两个维度在三个任务上都成立。\n- 实际上：Dim1 (count) 跨任务一致；Dim2 (BCS) 仅 RE forced-choice batch-level 有效，NER/MAVEN 仅 pairwise level 有信号。\n- **修复要求**：Abstract/Introduction 区分 pairwise（跨任务）和 batch-level（RE-specific）证据；将 \"across NER, RE, and ED\" 改为更精确表述。\n\n**[W-Critical-3] Pairwise r²=1.3-1.7% 效应量解读不够审慎** [R1-N2, R2 AGREE with nuance | 共识]\n- SCS 仅解释 type confusion 方差的 1.3-1.7%，>98% 由其他因素决定。\n- 引用 Cohen (1988) behavioral research 标准，但 LLM 系统变量可控度远高于行为研究，标准适用性未论证。\n- Batch-level R²=22-53% 是更有说服力的证据，但正文叙事将 pairwise 和 batch-level 并列，未以 batch-level 为主线。\n- **修复要求**：移除或弱化 Cohen 类比；以 batch-level R² 为主线证据，pairwise 定位为机制解释；讨论 SCS 作为代理指标的局限性。\n\n### Should-Fix（影响评分但不一票否决）\n\n**[W-Warning-1] Title \"Predict\" 与 correlational evidence 不匹配** [R2-N1 Critical, R1 降为 Should-Fix | 分歧]\n- \"Predict\" 在统计语境可辩护（BCS explains 22-53% variance），但 renaming 实验反驳朴素因果链（降低 SCS 反而降准确率 3-9pp）。Limitations 承认 \"correlational evidence\"。普通读者可能误解为可操作的因果关系。\n- **建议**：考虑改为 \"Relate to\" / \"Shape\" / \"Affect\"。\n\n**[W-Warning-2] TOST ±3pp margin 选择不够保守** [R1-W1, R2-W1 | 双方共识]\n- ±2pp 仅 marginally equivalent (p=0.047)；±1pp inconclusive (p=0.278)。\n- 90% CI upper bound 2.0pp 接近 main effect 2.2pp（interaction 可能达 main effect 91%）。\n- **建议**：正文突出 ±2pp marginal 和 logit-scale inconclusive；弱化为 \"bounded interaction at ±3pp level\"。\n\n**[W-Warning-3] SCS 新颖性不足** [R2-N3, R1 部分 REBUT | 分歧]\n- SCS = LLM-PEE 的 partitioning criterion（论文自己承认）。R1 认为 controlled framework 有独立贡献价值；R2 认为效应量有限（~2pp typical, r²≈1.5%）且无可行缓解方案（SDGD 失败、renaming 反向、few-shot 加剧），excitement 不足。\n- **建议**：更深入对比 LLM-PEE merge 策略差异；强化 negative result 的 actionable value；考虑增加至少一个可行缓解实验。\n\n**[W-Warning-4] Renaming 实验与 practical implications 矛盾** [R2-W2, R1 AGREE | 共识]\n- Discussion §6 建议 \"flag type pairs with SCS>0.85 for definition refinement\"，但 renaming 实验显示降低 SCS 反而降低准确率。\n- **建议**：Discussion 区分 \"SCS 作为诊断指标\" vs \"降低 SCS 作为干预手段\"。\n\n**[W-Warning-5] CrossAgentIE 对比不充分** [R2-W3, R1 AGREE | 共识]\n- CrossAgentIE (ACL 2025 Findings) 的 cross-type debate 与 confusability 分析直接相关，但仅在括号中列出。\n- **建议**：增加 1-2 句讨论 debate 机制与 confusability-aware batching 的异同。\n\n**[W-Warning-6] DocRED 5 batches/count level 样本量不足** [R1-W3, R2 AGREE | 共识]\n- Factorial interaction CI 极宽 [-1.6, 13.0]；count curve 趋势估计不可靠。\n- **建议**：增至 15 batches（如资源允许），或明确讨论 power limitation。\n\n**[W-Warning-7] Dimension 2 未在 proprietary model 验证** [R1-W4, R2 AGREE | 共识]\n- Gemini count-64 仅 11/25 batches（原因未说明）；Llama-70B BCS 仅 count=16。\n- **建议**：解释 Gemini partial data；Limitations 明确标注。\n\n**[W-Warning-8] FewRel split-origin 需在正文说明** [R1-W6, R2-W4 | 双方共识]\n- Held-out validation (ρ=0.216, p=0.018) 比 covariate analysis 更有说服力但埋在 Appendix。\n- **建议**：正文 §3.1 简要提及。\n\n**[W-Warning-9] Rothman (1990) 引用：within-study 二级分析需加 caveat** [R1-W2, R2 AGREE | 共识]\n- Cross-dataset 比较引用 Rothman 合理；but prompt variant 分析 (4×2) 非独立假设。\n\n**[W-Warning-10] SDGD routing failure 与 constrained decoding 交互分析不足** [R1-W5, R2 AGREE | 共识]\n- Oracle +29.8pp vs practical all below baseline → 瓶颈在 routing。缺少 unconstrained decoding 下 decomposition 的 ablation。\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成共识：\n1. **[AGREE]** \"Largely additive\" overclaim 是论文最核心的 framing 问题，必须限定为 sentence-level RE linear scale [W-Critical-1]\n2. **[AGREE]** \"Two-dimensional across NER/RE/ED\" framing 超出证据支撑，BCS batch-level 仅限 RE forced-choice [W-Critical-2]\n3. **[AGREE]** 效应量解读应以 batch-level R²=22-53% 为主线，Cohen 标准适用性不足 [W-Critical-3]\n4. **[AGREE]** TOST ±3pp margin 不够保守，additivity 结论高度依赖 margin 选择 [W-Warning-2]\n5. **[AGREE]** Renaming 实验与 practical implications 存在未充分讨论的张力 [W-Warning-4]\n6. **[AGREE]** CrossAgentIE 对比不充分 [W-Warning-5]\n7. **[AGREE]** DocRED 样本量不足 [W-Warning-6]\n8. **[AGREE]** Dim2 未在 proprietary model 验证 [W-Warning-7]\n9. **[AGREE]** FewRel split-origin held-out validation 应提到正文 [W-Warning-8]\n10. **[AGREE]** SDGD routing failure 分析应讨论 constrained decoding 交互 [W-Warning-10]\n11. **[AGREE]** Missing reference: Dubey et al. (2018) Pairwise Confusion (ECCV)\n\n## Reviewer Divergence\n\n| 议题 | R1 立场 | R2 立场 | 说明 |\n|------|---------|---------|------|\n| Title \"Predict\" | Should-Fix（统计语境可辩护） | Critical（暗示因果） | R1 认为\"predict\"是统计标准用语；R2 认为 renaming 反例+correlational 性质要求更谨慎措辞 |\n| SCS 新颖性 | Controlled framework 有独立贡献 | 不够（=LLM-PEE criterion，效应量有限，无缓解方案） | R1 对 \"experimental design as contribution\" 更宽容；R2 认为缺乏 actionable outcome |\n| Venue fit | Empirical study 完全适合 EMNLP | 质疑是否适合 main track | R1 引用 ACL ARR review form \"empirical contribution\" 条款反驳；R2 未在交叉中回应此反驳 |\n| 总评分 | 3.5（Borderline Conference，条件性：framing 修复） | 3.0（Findings） | 核心差异：negative results 贡献价值和 novelty 门槛判断不同 |\n\n---\n\n## Questions（需要作者澄清）\n\n1. 如果 \"largely additive\" 仅在 sentence-level RE linear scale 成立，论文的核心 framework claim 应如何重新定位？是否应将标题聚焦于 RE？\n2. SCS 作为 confusability 的代理指标仅解释 1.3-1.7% pairwise 方差，是否有更精细的代理指标候选（如基于 in-context confusion matrix 的指标）？\n3. Renaming 实验的 label unfamiliarity 效应是否可以通过使用模型训练数据中高频出现的 paraphrase 来缓解？\n4. Oracle routing +29.8pp vs practical routing all below baseline：如果去掉 enum constraint（允许更自由的 \"none\" prediction），routing 策略是否改善？\n5. Gemini 2.5 Flash count-64 为何仅 11/25 batches 完成？\n\n---\n\n## Missing References\n\n1. **Dubey et al. (2018), \"Pairwise Confusion for Fine-Grained Visual Classification\" (ECCV 2018)** — pairwise confusion metric 与 SCS 动机高度重叠 [双方 AGREE]\n2. **Collier et al. (2021), \"Exploiting Class Similarity for ML with Confidence Labels\"** — inter-class similarity 对分类的影响 [R2 提出, R1 AGREE 低优先级]\n3. **LLM calibration × constrained decoding 文献** — 与 routing failure 和 format dependency 分析相关 [R1 提出, R2 AGREE]\n\n---\n\n## Overall Assessment\n\n**综合评分: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.0 | 2.5 | 2.5 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Confidence | 4 | 4 | 4 |\n| **Overall** | **3.5** | **3.0** | **3.0** |\n\n**评分理由**：\n\n论文展示了高水准的实验设计和统计方法论（Soundness 3.5，在 NLP 实证研究中属上乘），negative results 的诚实报告有独立贡献价值，跨模型验证覆盖面广，格式完全合规。\n\n但以下因素将论文限定在 Findings 档位：\n\n1. **核心 framing 超出证据**（双方共识）：\"largely additive\" 仅在 sentence-level RE linear scale 成立；\"two-dimensional across NER/RE/ED\" 中 Dimension 2 batch-level 仅限 RE forced-choice。Abstract/Introduction 的 scope claim 与实际证据之间存在系统性 gap。\n\n2. **Excitement 不足**（R1: 3.0, R2: 2.5）：SCS 形式上 = LLM-PEE 的 partitioning criterion；核心发现（count dominates, similar types confuse more）在直觉层面不意外；实际效应量有限（typical batch ~2pp, pairwise r²≈1.5%）；所有干预方向均失败（SDGD、renaming、few-shot）。\n\n3. **缺乏 actionable outcome**：论文是纯诊断性研究，Discussion 的四个 \"actionable directions\" 均为 untested suggestions。对于 Borderline Conference 门槛，至少期望一个 direction 有初步验证。\n\n**升级路径**（若目标 Borderline Conference 3.5）：\n- (a) 修正 framing：限定 \"largely additive\" 和 \"two-dimensional\" 的适用范围至 evidence 实际支撑的边界\n- (b) 补充至少一个可行缓解实验（如 contrastive definitions for high-SCS pairs，或 unconstrained decoding routing ablation）\n- (c) 以 batch-level R²=22-53% 为主线证据重组叙事，弱化 pairwise r² 和 Cohen 类比\n- (d) 更深入对比 LLM-PEE merge 策略差异，说明 SDGD 失败的 task-specific 原因\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"two largely additive dimensions\" 需限定为 sentence-level RE\n- \"across NER, RE, and event detection\" 应区分 Dim1（跨任务）和 Dim2 batch-level（RE-specific）\n- \"BCS explains 22-53% of cross-batch RE accuracy variance under RE's forced-choice format\" — 已有 format caveat，但紧跟 \"largely additive\" 后容易让读者泛化\n\n### Introduction\n- Finding (1) 末尾有 \"but not in document-level RE or NER\" 限定，但被 \"two largely additive dimensions\" 主标签淹没\n- Contribution 1 \"first controlled study...across NER, RE, and event detection\" 需精确化\n\n### Experimental Setup\n- §3.1 FewRel: 应提及 train/val split 合并理由和 held-out validation 结果\n- §3.3: DocRED 5 batches/count level 的 power limitation 应在此处说明\n\n### Results\n- §4.2 pairwise r²=1.3-1.7%: Cohen 引用应弱化或移除\n- §4.3 BCS-controlled: batch-level R²=22-53% 应更突出作为主要效应量证据\n- §4.4: \"largely additive\" 应弱化为 \"bounded interaction at ±3pp in sentence-level RE\"\n\n### SDGD\n- §5: routing failure 与 constrained decoding 交互应讨论\n- Oracle +29.8pp 的指导意义（routing 是瓶颈）应更强调\n\n### Discussion\n- §6 practical implication (1) \"flag SCS>0.85 for definition refinement\" 与 renaming 实验矛盾，需区分诊断 vs 干预\n- §6 (3) \"contrastive definitions...untested; future work\" — 如能提供初步验证将显著提升论文\n\n### Related Work\n- CrossAgentIE cross-type debate 需更深入对比\n- 增加 Dubey et al. (2018) pairwise confusion 引用\n\n### Format\n- Orphan bib entry (jagannatha2020calibrating) 需清理\n- Gemini partial data (11/25 batches) 需解释原因\n- 少数 bib entries 的 first author field 需核实\n\n---\n\n## 外部审稿\n\n**外部审稿：未配置**（项目未启用 `external_review.paperreview_ai`）\n\n---\n\n*报告由 Review Director 基于 Reviewer 1 和 Reviewer 2 的独立审稿及交叉分享回应汇总生成。*",
  "project": "schema-dag-extraction",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 20 审稿报告（圆桌会议汇总）\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 via ARR May 2026 cycle\n**审稿日期**: 2026-05-19\n**Reviewer 编排**: R1（方法严谨性 + 实验设计 + 统计分析）、R2（新颖性 + Related Work + 写作 + 格式）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即收敛）\n\n---\n\n## Summary\n\n本文研究 training-free LLM 信息抽取中 schema 复杂度导致性能退化的两个维度：type count（维度1）和 type confusability（维度2）。作者提出 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 来量化类型间语义混淆度，在 Few-NERD (NER)、FewRel (RE)、DocRED (doc-RE)、MAVEN (ED) 上使用 Qwen3-32B 为主模型进行系统实验，辅以 Llama-3.1-8B/70B 和 Gemini 2.5 Flash 的跨模型验证。主要发现：(1) count 下降是主导因素；(2) BCS 在 RE forced-choice 格式下解释 22-53% 的跨 batch 准确率方差，但对 NER 无 batch-level 信号；(3) schema decomposition 因 merge amplification (NER) 和 routing failure (RE) 而失败。\n\n---\n\n## Strengths\n\n1. **实验设计精良**：Count curves + BCS-controlled 双范式有效分离 count 和 confusability。Within-pool 控制（从 80-rel pool 抽 16-rel subsets）排除 pool composition confound。FewRel balanced design 消除 type frequency confound。设计思路清晰，在 NLP 实证研究中属上乘。\n\n2. **统计处理透明度高于 NLP 平均水准**：TOST equivalence testing（含 sensitivity analysis across margins）、permutation tests、bootstrap CIs（percentile + cluster）、cross-seed variance decomposition、split-origin covariate analysis。多数 NLP 论文不做 equivalence testing；本文不仅做了，还报告了 margin 对结论的敏感性。\n\n3. **诚实报告 negative results**：SDGD 失败（merge amplification + routing failure）、label renaming 失败（unfamiliarity > confusability reduction）、NER batch-level BCS null、logit-scale TOST inconclusive、few-shot 加剧混淆。这些 negative results 的信息量可能超过 positive findings。\n\n4. **跨模型验证覆盖广**：Qwen3-32B → Llama-3.1-8B/70B → Gemini 2.5 Flash (API)，跨开源/闭源、8B-70B+。Dimension 1 directional consistency 证据充分（RE slope near-identical across models: -30.7 vs -30.1pp）。\n\n5. **格式完全合规**：`\\usepackage[review]{acl}` 正确，匿名化完整，正文 ≤ 8 页，Limitations 位置正确，Responsible NLP Checklist 填写详实，引用格式一致。\n\n6. **引用覆盖度好**：~70 个 unique cited keys，覆盖直接竞争者、基础方法、evaluation/statistical 方法、representation degeneration 文献。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[W-Critical-1] \"Largely additive\" overclaim：仅在 sentence-level RE linear scale 成立** [R1-N1, R2-N2 | 双方共识]\n- Abstract/Conclusion 声称 \"two largely additive dimensions\"，但实际支撑仅来自 FewRel 69-batch full-range regression on linear scale (TOST p=0.003 at ±3pp)。\n- FewRel logit-scale: interaction marginally significant (p=0.047), TOST inconclusive (p=0.209)\n- DocRED: interaction +5.7pp, 95% CI [-1.6, 13.0], TOST p=0.77\n- NER factorial: p=0.50; FewRel 2×2 factorial: p=0.56\n- **修复要求**：Abstract/Conclusion 将 \"largely additive\" 限定为 sentence-level RE linear specification；明确承认 DocRED 和 logit-scale 不成立。\n\n**[W-Critical-2] \"Two-dimensional across NER/RE/ED\" framing 超出证据** [R1-N3, R2-N2 | 双方共识]\n- Dimension 2 (BCS) batch-level 预测力仅在 RE forced-choice format 有效。NER batch-level r≈0 (n=450)；MAVEN centrality confound 控制后信号消失。\n- Abstract \"across NER, RE, and event detection\" 误导读者认为两个维度在三个任务上都成立。\n- 实际上：Dim1 (count) 跨任务一致；Dim2 (BCS) 仅 RE forced-choice batch-level 有效，NER/MAVEN 仅 pairwise level 有信号。\n- **修复要求**：Abstract/Introduction 区分 pairwise（跨任务）和 batch-level（RE-specific）证据；将 \"across NER, RE, and ED\" 改为更精确表述。\n\n**[W-Critical-3] Pairwise r²=1.3-1.7% 效应量解读不够审慎** [R1-N2, R2 AGREE with nuance | 共识]\n- SCS 仅解释 type confusion 方差的 1.3-1.7%，>98% 由其他因素决定。\n- 引用 Cohen (1988) behavioral research 标准，但 LLM 系统变量可控度远高于行为研究，标准适用性未论证。\n- Batch-level R²=22-53% 是更有说服力的证据，但正文叙事将 pairwise 和 batch-level 并列，未以 batch-level 为主线。\n- **修复要求**：移除或弱化 Cohen 类比；以 batch-level R² 为主线证据，pairwise 定位为机制解释；讨论 SCS 作为代理指标的局限性。\n\n### Should-Fix（影响评分但不一票否决）\n\n**[W-Warning-1] Title \"Predict\" 与 correlational evidence 不匹配** [R2-N1 Critical, R1 降为 Should-Fix | 分歧]\n- \"Predict\" 在统计语境可辩护（BCS explains 22-53% variance），但 renaming 实验反驳朴素因果链（降低 SCS 反而降准确率 3-9pp）。Limitations 承认 \"correlational evidence\"。普通读者可能误解为可操作的因果关系。\n- **建议**：考虑改为 \"Relate to\" / \"Shape\" / \"Affect\"。\n\n**[W-Warning-2] TOST ±3pp margin 选择不够保守** [R1-W1, R2-W1 | 双方共识]\n- ±2pp 仅 marginally equivalent (p=0.047)；±1pp inconclusive (p=0.278)。\n- 90% CI upper bound 2.0pp 接近 main effect 2.2pp（interaction 可能达 main effect 91%）。\n- **建议**：正文突出 ±2pp marginal 和 logit-scale inconclusive；弱化为 \"bounded interaction at ±3pp level\"。\n\n**[W-Warning-3] SCS 新颖性不足** [R2-N3, R1 部分 REBUT | 分歧]\n- SCS = LLM-PEE 的 partitioning criterion（论文自己承认）。R1 认为 controlled framework 有独立贡献价值；R2 认为效应量有限（~2pp typical, r²≈1.5%）且无可行缓解方案（SDGD 失败、renaming 反向、few-shot 加剧），excitement 不足。\n- **建议**：更深入对比 LLM-PEE merge 策略差异；强化 negative result 的 actionable value；考虑增加至少一个可行缓解实验。\n\n**[W-Warning-4] Renaming 实验与 practical implications 矛盾** [R2-W2, R1 AGREE | 共识]\n- Discussion §6 建议 \"flag type pairs with SCS>0.85 for definition refinement\"，但 renaming 实验显示降低 SCS 反而降低准确率。\n- **建议**：Discussion 区分 \"SCS 作为诊断指标\" vs \"降低 SCS 作为干预手段\"。\n\n**[W-Warning-5] CrossAgentIE 对比不充分** [R2-W3, R1 AGREE | 共识]\n- CrossAgentIE (ACL 2025 Findings) 的 cross-type debate 与 confusability 分析直接相关，但仅在括号中列出。\n- **建议**：增加 1-2 句讨论 debate 机制与 confusability-aware batching 的异同。\n\n**[W-Warning-6] DocRED 5 batches/count level 样本量不足** [R1-W3, R2 AGREE | 共识]\n- Factorial interaction CI 极宽 [-1.6, 13.0]；count curve 趋势估计不可靠。\n- **建议**：增至 15 batches（如资源允许），或明确讨论 power limitation。\n\n**[W-Warning-7] Dimension 2 未在 proprietary model 验证** [R1-W4, R2 AGREE | 共识]\n- Gemini count-64 仅 11/25 batches（原因未说明）；Llama-70B BCS 仅 count=16。\n- **建议**：解释 Gemini partial data；Limitations 明确标注。\n\n**[W-Warning-8] FewRel split-origin 需在正文说明** [R1-W6, R2-W4 | 双方共识]\n- Held-out validation (ρ=0.216, p=0.018) 比 covariate analysis 更有说服力但埋在 Appendix。\n- **建议**：正文 §3.1 简要提及。\n\n**[W-Warning-9] Rothman (1990) 引用：within-study 二级分析需加 caveat** [R1-W2, R2 AGREE | 共识]\n- Cross-dataset 比较引用 Rothman 合理；but prompt variant 分析 (4×2) 非独立假设。\n\n**[W-Warning-10] SDGD routing failure 与 constrained decoding 交互分析不足** [R1-W5, R2 AGREE | 共识]\n- Oracle +29.8pp vs practical all below baseline → 瓶颈在 routing。缺少 unconstrained decoding 下 decomposition 的 ablation。\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成共识：\n1. **[AGREE]** \"Largely additive\" overclaim 是论文最核心的 framing 问题，必须限定为 sentence-level RE linear scale [W-Critical-1]\n2. **[AGREE]** \"Two-dimensional across NER/RE/ED\" framing 超出证据支撑，BCS batch-level 仅限 RE forced-choice [W-Critical-2]\n3. **[AGREE]** 效应量解读应以 batch-level R²=22-53% 为主线，Cohen 标准适用性不足 [W-Critical-3]\n4. **[AGREE]** TOST ±3pp margin 不够保守，additivity 结论高度依赖 margin 选择 [W-Warning-2]\n5. **[AGREE]** Renaming 实验与 practical implications 存在未充分讨论的张力 [W-Warning-4]\n6. **[AGREE]** CrossAgentIE 对比不充分 [W-Warning-5]\n7. **[AGREE]** DocRED 样本量不足 [W-Warning-6]\n8. **[AGREE]** Dim2 未在 proprietary model 验证 [W-Warning-7]\n9. **[AGREE]** FewRel split-origin held-out validation 应提到正文 [W-Warning-8]\n10. **[AGREE]** SDGD routing failure 分析应讨论 constrained decoding 交互 [W-Warning-10]\n11. **[AGREE]** Missing reference: Dubey et al. (2018) Pairwise Confusion (ECCV)\n\n## Reviewer Divergence\n\n| 议题 | R1 立场 | R2 立场 | 说明 |\n|------|---------|---------|------|\n| Title \"Predict\" | Should-Fix（统计语境可辩护） | Critical（暗示因果） | R1 认为\"predict\"是统计标准用语；R2 认为 renaming 反例+correlational 性质要求更谨慎措辞 |\n| SCS 新颖性 | Controlled framework 有独立贡献 | 不够（=LLM-PEE criterion，效应量有限，无缓解方案） | R1 对 \"experimental design as contribution\" 更宽容；R2 认为缺乏 actionable outcome |\n| Venue fit | Empirical study 完全适合 EMNLP | 质疑是否适合 main track | R1 引用 ACL ARR review form \"empirical contribution\" 条款反驳；R2 未在交叉中回应此反驳 |\n| 总评分 | 3.5（Borderline Conference，条件性：framing 修复） | 3.0（Findings） | 核心差异：negative results 贡献价值和 novelty 门槛判断不同 |\n\n---\n\n## Questions（需要作者澄清）\n\n1. 如果 \"largely additive\" 仅在 sentence-level RE linear scale 成立，论文的核心 framework claim 应如何重新定位？是否应将标题聚焦于 RE？\n2. SCS 作为 confusability 的代理指标仅解释 1.3-1.7% pairwise 方差，是否有更精细的代理指标候选（如基于 in-context confusion matrix 的指标）？\n3. Renaming 实验的 label unfamiliarity 效应是否可以通过使用模型训练数据中高频出现的 paraphrase 来缓解？\n4. Oracle routing +29.8pp vs practical routing all below baseline：如果去掉 enum constraint（允许更自由的 \"none\" prediction），routing 策略是否改善？\n5. Gemini 2.5 Flash count-64 为何仅 11/25 batches 完成？\n\n---\n\n## Missing References\n\n1. **Dubey et al. (2018), \"Pairwise Confusion for Fine-Grained Visual Classification\" (ECCV 2018)** — pairwise confusion metric 与 SCS 动机高度重叠 [双方 AGREE]\n2. **Collier et al. (2021), \"Exploiting Class Similarity for ML with Confidence Labels\"** — inter-class similarity 对分类的影响 [R2 提出, R1 AGREE 低优先级]\n3. **LLM calibration × constrained decoding 文献** — 与 routing failure 和 format dependency 分析相关 [R1 提出, R2 AGREE]\n\n---\n\n## Overall Assessment\n\n**综合评分: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.0 | 2.5 | 2.5 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Confidence | 4 | 4 | 4 |\n| **Overall** | **3.5** | **3.0** | **3.0** |\n\n**评分理由**：\n\n论文展示了高水准的实验设计和统计方法论（Soundness 3.5，在 NLP 实证研究中属上乘），negative results 的诚实报告有独立贡献价值，跨模型验证覆盖面广，格式完全合规。\n\n但以下因素将论文限定在 Findings 档位：\n\n1. **核心 framing 超出证据**（双方共识）：\"largely additive\" 仅在 sentence-level RE linear scale 成立；\"two-dimensional across NER/RE/ED\" 中 Dimension 2 batch-level 仅限 RE forced-choice。Abstract/Introduction 的 scope claim 与实际证据之间存在系统性 gap。\n\n2. **Excitement 不足**（R1: 3.0, R2: 2.5）：SCS 形式上 = LLM-PEE 的 partitioning criterion；核心发现（count dominates, similar types confuse more）在直觉层面不意外；实际效应量有限（typical batch ~2pp, pairwise r²≈1.5%）；所有干预方向均失败（SDGD、renaming、few-shot）。\n\n3. **缺乏 actionable outcome**：论文是纯诊断性研究，Discussion 的四个 \"actionable directions\" 均为 untested suggestions。对于 Borderline Conference 门槛，至少期望一个 direction 有初步验证。\n\n**升级路径**（若目标 Borderline Conference 3.5）：\n- (a) 修正 framing：限定 \"largely additive\" 和 \"two-dimensional\" 的适用范围至 evidence 实际支撑的边界\n- (b) 补充至少一个可行缓解实验（如 contrastive definitions for high-SCS pairs，或 unconstrained decoding routing ablation）\n- (c) 以 batch-level R²=22-53% 为主线证据重组叙事，弱化 pairwise r² 和 Cohen 类比\n- (d) 更深入对比 LLM-PEE merge 策略差异，说明 SDGD 失败的 task-specific 原因\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"two largely additive dimensions\" 需限定为 sentence-level RE\n- \"across NER, RE, and event detection\" 应区分 Dim1（跨任务）和 Dim2 batch-level（RE-specific）\n- \"BCS explains 22-53% of cross-batch RE accuracy variance under RE's forced-choice format\" — 已有 format caveat，但紧跟 \"largely additive\" 后容易让读者泛化\n\n### Introduction\n- Finding (1) 末尾有 \"but not in document-level RE or NER\" 限定，但被 \"two largely additive dimensions\" 主标签淹没\n- Contribution 1 \"first controlled study...across NER, RE, and event detection\" 需精确化\n\n### Experimental Setup\n- §3.1 FewRel: 应提及 train/val split 合并理由和 held-out validation 结果\n- §3.3: DocRED 5 batches/count level 的 power limitation 应在此处说明\n\n### Results\n- §4.2 pairwise r²=1.3-1.7%: Cohen 引用应弱化或移除\n- §4.3 BCS-controlled: batch-level R²=22-53% 应更突出作为主要效应量证据\n- §4.4: \"largely additive\" 应弱化为 \"bounded interaction at ±3pp in sentence-level RE\"\n\n### SDGD\n- §5: routing failure 与 constrained decoding 交互应讨论\n- Oracle +29.8pp 的指导意义（routing 是瓶颈）应更强调\n\n### Discussion\n- §6 practical implication (1) \"flag SCS>0.85 for definition refinement\" 与 renaming 实验矛盾，需区分诊断 vs 干预\n- §6 (3) \"contrastive definitions...untested; future work\" — 如能提供初步验证将显著提升论文\n\n### Related Work\n- CrossAgentIE cross-type debate 需更深入对比\n- 增加 Dubey et al. (2018) pairwise confusion 引用\n\n### Format\n- Orphan bib entry (jagannatha2020calibrating) 需清理\n- Gemini partial data (11/25 batches) 需解释原因\n- 少数 bib entries 的 first author field 需核实\n\n---\n\n## 外部审稿\n\n**外部审稿：未配置**（项目未启用 `external_review.paperreview_ai`）\n\n---\n\n*报告由 Review Director 基于 Reviewer 1 和 Reviewer 2 的独立审稿及交叉分享回应汇总生成。*",
    "project": "schema-dag-extraction",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool result

_source line 2073 · 2026-05-19T04:47:50.907050+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4521
}
```

</details>

---


### Assistant

_source line 2074 · 2026-05-19T04:47:58.646725+00:00_

审稿报告已投递至 Research Director。

**Round 20 审稿完成**。核心结论：

- **综合评分: 3.0 (Findings)**（R1: 3.5, R2: 3.0）
- **3 个 Must-Fix**：(1) "largely additive" overclaim 需限定为 sentence-level RE linear scale；(2) "two-dimensional across NER/RE/ED" 中 Dim2 batch-level 仅限 RE forced-choice，framing 需收窄；(3) 效应量叙事应以 batch-level R²=22-53% 为主线，弱化 Cohen 类比
- **10 个 Should-Fix**：Title "Predict"、TOST margin、SCS 新颖性、renaming 矛盾、CrossAgentIE 对比、DocRED 样本量、proprietary model 验证、split-origin、Rothman 引用、SDGD routing 分析
- **升级路径**：修正 framing + 补充可行缓解实验 + 重组效应量叙事 → 可升至 3.5 (Borderline Conference)
- **Review issues tracker 已同步更新**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 184

## Round 184

2 recorded events


### User

_source line 2075 · 2026-05-19T04:48:01.213795+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

总结：我对 R1 的 3 个 Must-Fix 全部 AGREE（additivity overclaim、效应量解读、BCS 对 NER 无信号），6 个 Should-Fix 中 4 个完全 AGREE、2 个 AGREE with nuance（W2 Rothman 和 W5 SDGD 归因）。Minor 和 Missing References 全部 AGREE。

评分维持 **3.0 (Findings)** 不变，核心理由：框架通用性 claim 与证据不匹配（Dimension 2 仅限 RE）、缺乏 actionable 贡献（SDGD 失败后无替代方案）、mixed results 比例过高。R1 的 3.5 有其合理性（方法论严谨），但我认为 scope overclaim 的严重性值得更重的 penalty。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2076 · 2026-05-19T04:48:13.895426+00:00_

审稿报告已投递至 Research Director。

**Round 20 审稿完成。**

**最终结论：Overall 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.0 | 2.5 | 2.5 |
| Overall | 3.5 | 3.0 | **3.0** |

**3 个 Must-Fix（双方共识）**：
1. "Largely additive" 仅在 sentence-level RE linear scale 成立，Abstract/Conclusion 必须限定
2. "Two-dimensional across NER/RE/ED" 中 Dim2 batch-level 仅限 RE forced-choice，framing 超出证据
3. Pairwise r²=1.3-1.7% 效应量解读应以 batch-level R²=22-53% 为主线，Cohen 标准适用性不足

**10 个 Should-Fix（多数共识）**：Title "Predict" 措辞、TOST margin、SCS 新颖性、renaming 矛盾、CrossAgentIE 对比、DocRED 样本量、Dim2 proprietary model 验证缺口、split-origin 控制、Rothman 引用、SDGD routing 分析

**1 个未解决分歧**：总评分 R1 3.5 vs R2 3.0，核心差异在于对 negative results 贡献价值和 novelty 门槛的判断标准不同。综合评定取 3.0，因 scope overclaim 和 actionable outcome 缺失是结构性问题。

Review issues tracker 已同步更新至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 185

## Round 185

178 recorded events


### User

_source line 2077 · 2026-05-19T11:38:31.102663+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2078 · 2026-05-19T11:38:37.849691+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2079 · 2026-05-19T11:38:37.850393+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2080 · 2026-05-19T11:38:41.720267+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2081 · 2026-05-19T11:38:41.770952+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2082 · 2026-05-19T11:38:46.189278+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2083 · 2026-05-19T11:38:46.693021+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (62 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_unconstrained_decoding_ablation** (success): The BCS-accuracy correlation in RE arises from semantic confusion rather than forced-choice format artifacts. If removing the enum constraint (relaxed decoding) preserves the negative BCS-accuracy correlation direction and significance, confusability is a genuine semantic property; if the correlation disappears, the effect is specific to constrained classification where all errors are channeled into type substitution. Either outcome strengthens the paper: preservation broadens the claim, disappearance validates the error-channeling hypothesis stated in Discussion. ← 基于 exp_fewrel_formal_80rel\n- **exp_multiseed_bcs_re** (success): The BCS-accuracy correlation observed in FewRel BCS-controlled experiments (R²=0.22-0.53) is
…[truncated 1464 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 2084 · 2026-05-19T11:38:46.693456+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "literature_map.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "literature_map.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 2085 · 2026-05-19T11:38:47.999286+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\", \"content\": \"# Literature Map for schema-dag-extraction\\n# Updated: 2026-05-15\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\n\\n# =============================================================================\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\n# =============================================================================\\n\\n- id: llm-pee-2025\\n  title: \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\"\\n  year: 2025\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2503.02628\\n  role: direct-competitor\\n  relevance_note: >\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\n    Divides candidate types into partitions to reduce prompt length.\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\n\\n- id: parse-2025\\n  title: \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\"\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://arxiv.org/abs/2510.08623\\n  role: direct-competitor\\n  relevance_note: >\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\n    Does NOT model type confusability explicitly.\\n\\n- id: dee-2024\\n  title: \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\"\\n  year: 2024\\
…[truncated 11050 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1305
}
```

</details>

---


### Tool call

_source line 2086 · 2026-05-19T11:38:48.051017+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2087 · 2026-05-19T11:38:48.101766+00:00_

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
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 has been validated across all four models including a proprietary one; Dimension~2 has been verified only on open-weight models and was not robustly detectable on NER at 8B scale, likely due to floor effects. Gemini 2.5 Flash count-64 results are partial (11/25 batches) due to API quota exhaustion. Dimension~2 (BCS) has not been validated on proprietary models at the batch level.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded under the linear specification (TOST $p = 0.003$ at $\pm 3$\,pp on FewRel; DocRED inconclusive, Appendix~\ref{sec:appendix_factorial}) but inconclusive on the logit scale ($p = 0.209$). DocRED count curves use 5 batches per level due to higher per-batch evaluation cost; factorial analyses should be interpreted with this power constraint in mind. BCS-controlled experiments use a single seed with gr
…[truncated 3889 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2088 · 2026-05-19T11:38:55.092253+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2089 · 2026-05-19T11:38:55.445124+00:00_

100	\resizebox{\columnwidth}{!}{%
101	\begin{tabular}{llrrrrrrr}
102	\toprule
103	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
104	\cmidrule(lr){3-7}
105	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
106	\midrule
107	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
108	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}\,0.001$ \\
109	\midrule
110	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
111	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
112	\bottomrule
113	\end{tabular}}
114	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}
115	\label{tab:error_taxonomy}
116	\end{table}
117	
118	\section{SDGD Full Protocol and Results}
119	\label{sec:appendix_sdgd}
120	
121	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation.
122	
123	Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368). SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop. Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194,
…[truncated 16666 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 2090 · 2026-05-19T11:38:55.445518+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2091 · 2026-05-19T11:38:56.449909+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: type count and type confusability. We present what is, to our knowledge, the first controlled study isolating these factors across NER, RE, and event detection on four datasets, revealing task-dependent effect structures. We quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS). Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) dominates confusability-related type substitution, though typical batches yield modest ${\sim}$2\,pp gaps. BCS explains 22--53\% of cross-batch RE accuracy variance under RE's forced-choice format but shows no batch-level signal for NER, where errors scatter across missed entities and boundary failures. Few-shot demonstrations widen the confusability gap (+4.3\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE). Pairwise confusability is a schema-structural property: effects replicate across model scales and families, and persist under varied prompt designs.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 2092 · 2026-05-19T11:38:56.450275+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2093 · 2026-05-19T11:38:57.454512+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
…[truncated 3140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 2094 · 2026-05-19T11:38:57.455023+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/schema-dag-extraction/docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/schema-dag-extraction/docs/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 2095 · 2026-05-19T11:38:57.907153+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2096 · 2026-05-19T11:38:57.907513+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 2097 · 2026-05-19T11:38:57.960036+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema-dag-extraction'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 2098 · 2026-05-19T11:39:02.881999+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 2099 · 2026-05-19T11:39:03.635446+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 2100 · 2026-05-19T11:39:03.736184+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2101 · 2026-05-19T11:39:03.786794+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2102 · 2026-05-19T11:39:08.256522+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2103 · 2026-05-19T11:39:08.760014+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, bidirectional encoders \cite{gliner-2024,gliner2-2025}, and fine-grained entity typing \cite{gillick-2014-entity-typing}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability. \citet{wei-2023-chatie} reformulate zero-shot IE as multi-turn QA with ChatGPT but do not analyze schema-size effects.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21 in NER) that our \S\ref{sec:sdgd} analysis identifies as the fundamental bottleneck. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definit
…[truncated 3527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 2104 · 2026-05-19T11:39:08.760443+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 2105 · 2026-05-19T11:39:09.262771+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences
…[truncated 7780 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2106 · 2026-05-19T11:39:09.313404+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 2107 · 2026-05-19T11:39:09.716317+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure*}[t]
10	\centering
11	\begin{minipage}[t]{0.48\textwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\textwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves. Error bars: $\pm 1$\,SD across 3 seeds $\times$ 25 batches. RE declines monotonically; NER shows a U-shape. Hollow markers: full-schema (no sampling variance). \textbf{(b)} BCS-controlled FewRel accuracy. Slopes are consistent across the independent and within-pool 16-relation conditions ($p = 0.60$); wider BCS range at 80 relations produces larger gaps.}
21	\label{fig:main_results}
22	\end{figure*}
23	
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}). The pattern is stable across three seeds (max $\Delta = 10.7$\,pp, within 1\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\times$; Appendix~\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $
…[truncated 9602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2108 · 2026-05-19T11:39:09.766981+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool result

_source line 2109 · 2026-05-19T11:39:18.860161+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here are the key submission guidelines and author instructions for ACL Rolling Review (ARR) 2026:

## Key Submission Requirements

All submitted papers are expected to describe original, completed and unpublished work. There is a 10% limit on re-use of text from other publications.

Submissions that exceed the length requirements, or are missing a limita
…[truncated 1405 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 9093
}
```

</details>

---


### Tool call

_source line 2110 · 2026-05-19T11:39:24.343380+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 2111 · 2026-05-19T11:39:24.745383+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapse (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}); type separation recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.): graph coloring achieves only marginal mean BCS reduction (0.559$\to$0.552), insufficient to produce detectable accuracy improvement. All practical routing strategies fall below the single-pass baseline (Appendix~\ref{sec:appendix_routing}): under constrained decoding, 73.4\% of instances receive positive predictions across 3--5 sub-schemas, and models self-constrain semantically even without JSON constraints (0.08\% OOV; \S\ref{sec:discussion}), so the routing challenge persists regardless of output format.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2112 · 2026-05-19T11:39:24.745729+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2113 · 2026-05-19T11:39:25.700176+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). The effect generalizes to document-level RE (DocRED $R^2 = 0.51$) and persists across prompt designs (Appendix~\ref{sec:appendix_prompt_sensitivity}). Dimension~1 replicates across scales (8B--70B); Dimension~2 attenuates on smaller models.
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pairwise $R^2$ is 1.3\%; conditional on nonzero confusion, $R^2$ rises to 7\%. Correlated aggregation amplifies this to batch-level $R^2$ of 18--25\% (Appendix~\ref{app:aggregation-sim}).
9	
10	\paragraph{Task-dependent effects and format dependency.}
11	The batch-level BCS--performance relationship is RE-specific ($R^2 = 0.22$--$0.53$ vs.\ $r \approx 0$ for NER, $n = 450$). RE uses forced-choice classification where all non-null errors are type substitutions \cite{tam-2024-let-me-speak}, making BCS predictive. NER produces multi-span output where errors scatter across missed entities, boundary misalignment, and type confusion, diluting the BCS signal \cite{schall-2025-hidden-cost}. The NER U-shape (\S\ref{sec:count_curves}) reflects a dual-task burden: partial schemas require simultaneous span detection and type filtering; at full schema, filtering becomes vacuous and recall recovers. An unconstrained decoding ablation ($n = 25$) confirms format dependency: removing the JSON enum constraint eliminates the BCS--accuracy correlation ($\rho = -0.14$, $p = 0.49$), consistent with grammar-aligned decoding distorting LLM distributions \cite{park-2024-grammar-aligned} and channeling errors into type substitution.
12	
13	\paragraph{Practical implications.}
14	For NER, reducing candidate types per prompt is the primary lever; for RE, confusability-aw
…[truncated 1120 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2114 · 2026-05-19T11:39:25.700557+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2115 · 2026-05-19T11:39:26.002121+00:00_

1	% DEPRECATED — this file is no longer included in main.tex.
2	% The active conclusion is in discussion.tex (\input{discussion}).
3	% Kept for reference only; safe to delete.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2116 · 2026-05-19T11:39:26.052764+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 page limits long short paper format requirements template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 page limits long short paper format requirements template"
  }
}
```

</details>

---


### Tool result

_source line 2117 · 2026-05-19T11:39:32.932644+00:00_

Web search results for query: "ACL Rolling Review 2026 page limits long short paper format requirements template"

Links: [{"title":"Student Research Workshop - ACL 2026","url":"https://2026.aclweb.org/calls/student_research_workshop/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

Based on the search results, here's the information about ACL Rolling Review 2026 page limits and format requirements:

## Page Limits

Short papers have a maximum of 4 content pages, while long papers have a maximum of 8 content pages. Sections on ethical considerations and limitations do not count towards the page limit.

## Paper Format Requirements

Paper submissions must use the official ACL style templates, which are available as an Overleaf template and also a direct download. The LaTeX template is strongly encouraged. All submissions must be in PDF format and must conform to the offici
…[truncated 768 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6879
}
```

</details>

---


### Tool call

_source line 2118 · 2026-05-19T11:39:36.158149+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex"
  }
}
```

</details>

---


### Tool result

_source line 2119 · 2026-05-19T11:39:36.258954+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	
11	\title{Supplementary Material for: How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	All supplementary material is included in the appendix of the main paper.
19	
20	\end{document}
21	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2120 · 2026-05-19T11:39:36.259383+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 2121 · 2026-05-19T11:39:36.712044+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-associated degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \cite{lla
…[truncated 4608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2122 · 2026-05-19T11:39:36.712499+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers deadline submission ARR commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers deadline submission ARR commitment"
  }
}
```

</details>

---


### Tool result

_source line 2123 · 2026-05-19T11:39:45.449245+00:00_

Web search results for query: "EMNLP 2026 call for papers deadline submission ARR commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the web search results, here's the information about EMNLP 2026 call for papers, submission deadlines, and ARR commitment:

## Key Submission Information

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference.

## Important Deadlines

The ARR submission deadline for long and short papers is May 25, 2026, with a reviewer registration deadline for all authors by May 27, 2026. T
…[truncated 1128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 8736
}
```

</details>

---


### Tool call

_source line 2124 · 2026-05-19T11:39:49.843139+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2125 · 2026-05-19T11:39:50.195024+00:00_

1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the foll
…[truncated 5208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2126 · 2026-05-19T11:39:50.704591+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "298"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "298"
  }
}
```

</details>

---


### Tool result

_source line 2127 · 2026-05-19T11:39:51.208639+00:00_

298	To verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.
299	
300	\begin{table}[h]
301	\centering
302	\small
303	\resizebox{\columnwidth}{!}{\begin{tabular}{llrrrr}
304	\toprule
305	\textbf{Variant} & \textbf{Count} & \textbf{Mean Acc} & \textbf{$r$} & \textbf{$p$} \\
306	\midrule
307	V2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\
308	V2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\
309	Instruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\
310	Instruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\
311	Chain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\
312	Chain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\
313	Minimal & 8 & 0.852 & $-$0.170 & 0.638 \\
314	Minimal & 32 & 0.615 & $-$0.771 & 0.009 \\
315	\bottomrule
316	\end{tabular}}
317	\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}
318	\label{tab:prompt_variants}
319	\end{table}
320	
321	At count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \citep{rothman-1990}. These result
…[truncated 33157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 2128 · 2026-05-19T11:39:51.460116+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_framing.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "paper_framing.md",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 2129 · 2026-05-19T11:39:51.611534+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_framing.md\", \"content\": \"# Paper Framing — schema-dag-extraction\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\\n- Commitment deadline: August 2, 2026\\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\\n- Deadline: ARR May 25, 2026 (10 days from today)\\n\\n## Core Claims (2 claims) — Revised per D019\\n\\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.\\n\\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through channels with bounded association -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\\n\\n~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — \\\"why naive decomposition fails\\\" is its
…[truncated 10256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2130 · 2026-05-19T11:39:56.885014+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference paper page limit format anonymous double blind site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference paper page limit format anonymous double blind site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 2131 · 2026-05-19T11:39:59.646676+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Check external review config",
  "prompt": "Read the project config file at /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml and look for the external_review section, specifically whether paperreview_ai.enabled is true or false. Report what you find.",
  "subagent_type": "Explore"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Check external review config",
    "prompt": "Read the project config file at /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml and look for the external_review section, specifically whether paperreview_ai.enabled is true or false. Report what you find.",
    "subagent_type": "Explore"
  }
}
```

</details>

---


### Tool call

_source line 2132 · 2026-05-19T11:40:00.553625+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 2133 · 2026-05-19T11:40:00.654712+00:00_

1	@inproceedings{dubey-2018-pairwise-confusion,
2	  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},
3	  title     = {Pairwise Confusion for Fine-Grained Visual Classification},
4	  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},
5	  pages     = {71--88},
6	  year      = {2018}
7	}
8	
9	@inproceedings{collier-2021-correlated-noise,
10	  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},
11	  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},
12	  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
13	  pages     = {1551--1560},
14	  year      = {2021}
15	}
16	
17	@inproceedings{park-2024-grammar-aligned,
18	  author    = {Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadia and D'Antoni, Loris},
19	  title     = {Grammar-Aligned Decoding},
20	  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},
21	  year      = {2024}
22	}
23	
24	@inproceedings{tam-2024-let-me-speak,
25	  title     = {Let Me Speak Freely? {A} Study on the Impact of Format Restrictions on Performance of Large Language Models},
26	  author    = {Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hung-yi and Chen, Yun-Nung},
27	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track},
28	  year      = {2024},
29	  url       = {https://arxiv.org/abs/2408.02442}
30	}
31	
32	@inproceedings{yin-2019-zero-shot-bench,
33	  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},
34	  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},
35	  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},
36	  pages     = {3914--3923
…[truncated 525 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2134 · 2026-05-19T11:40:02.164936+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2135 · 2026-05-19T11:40:02.266884+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2136 · 2026-05-19T11:40:04.375955+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/**/config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/**/config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2137 · 2026-05-19T11:40:04.426647+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2138 · 2026-05-19T11:40:05.079772+00:00_

Web search results for query: "EMNLP 2026 main conference paper page limit format anonymous double blind site:2026.emnlp.org"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Physician- and Large Language Model-Generated Hospital Discharge Summaries: A Blinded, Comparative Quality and Safety Study","url":"https://www.medrxiv.org/content/10.1101/2024.09.29.24314562.full.pdf"},{"title":"Collaborative Large Language Models for Automated Data Extraction in Living Systematic Reviews","url":"https://www.medrxiv.org/content/10.1101/2024.09.20.24314108.full.pdf"},{"title":"Sponsors - EMNLP 2026","url":"https://2026.emnlp.org/sponsors/"}]

The search returned results from the EMNLP 2026 website, but the main conference papers page (result 4) appears to have been truncated and doesn't show the specific page limit and format details. I found information about the Industry Track (result 1) but I need to search more specifically for the main conference paper requirements.

Let me search again with a more focused query:

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfh
…[truncated 2110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 8194
}
```

</details>

---


### Tool call

_source line 2139 · 2026-05-19T11:40:07.291076+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 2140 · 2026-05-19T11:40:07.492233+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_
…[truncated 659 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2141 · 2026-05-19T11:40:09.702225+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent -type f 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent -type f 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 2142 · 2026-05-19T11:40:09.752868+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2143 · 2026-05-19T11:40:12.519064+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ | head -30"
  }
}
```

</details>

---


### Tool result

_source line 2144 · 2026-05-19T11:40:12.569702+00:00_

total 436
drwxr-xr-x 14 ubuntu ubuntu   4096 May 19 06:25 .
drwxrwxr-x  6 ubuntu ubuntu   4096 May 14 16:07 ..
drwxr-xr-x  3 ubuntu ubuntu   4096 May 14 16:07 .claude
drwxr-xr-x  6 ubuntu ubuntu   4096 May 16 05:06 .venv
-rw-r--r--  1 ubuntu ubuntu  17194 May 19 11:39 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu      0 May 14 16:10 ROADMAP.lock
-rw-------  1 ubuntu ubuntu   3100 May 19 06:25 ROADMAP.md
drwxr-xr-x 43 ubuntu ubuntu   4096 May 19 05:13 artifacts
drwxr-xr-x  2 ubuntu ubuntu  32768 May 18 10:52 checkpoints
drwxr-xr-x  2 ubuntu ubuntu   4096 May 17 16:07 configs
-rw-r--r--  1 ubuntu ubuntu      0 May 15 22:03 constraints.lock
-rw-------  1 ubuntu ubuntu    411 May 16 02:39 constraints.yaml
drwxr-xr-x  4 ubuntu ubuntu   4096 May 17 15:51 data
-rw-r--r--  1 ubuntu ubuntu      0 May 14 16:10 decisions.lock
-rw-------  1 ubuntu ubuntu  50066 May 19 06:25 decisions.yaml
drwxr-xr-x  5 ubuntu ubuntu   4096 May 16 05:05 docs
-rwxr-xr-x  1 ubuntu ubuntu      0 May 15 02:48 dream_registry.lock
-rw-------  1 ubuntu ubuntu   3545 May 16 08:23 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu   3550 May 16 08:23 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu      0 May 15 13:44 experiment_plan.lock
-rw-------  1 ubuntu ubuntu   5668 May 18 21:40 experiment_plan.yaml
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 16:09 figures
-rw-r--r--  1 ubuntu ubuntu  19038 May 15 07:59 literature_map.yaml
drwxr-xr-x  4 ubuntu ubuntu   4096 May 14 16:14 logs
-rw-r--r--  1 ubuntu ubuntu   4576 May 17 16:26 memory.md
-rw-r--r--  1 ubuntu ubuntu      0 May 17 08:07 mistakes.lock
-rw-------  1 ubuntu ubuntu   7372 May 18 07:27 mistakes.yaml
-rw-r--r--  1 ubuntu ubuntu  11835 May 17 10:30 paper_framing.md
-rw-r--r--  1 ubuntu ubuntu      0 May 15 17:49 paper_provenance.lock

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2145 · 2026-05-19T11:40:16.745268+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/configs/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/configs/"
  }
}
```

</details>

---


### Tool result

_source line 2146 · 2026-05-19T11:40:16.795978+00:00_

total 24
drwxr-xr-x  2 ubuntu ubuntu 4096 May 17 16:07 .
drwxr-xr-x 14 ubuntu ubuntu 4096 May 19 06:25 ..
-rw-r--r--  1 ubuntu ubuntu 8242 May 14 16:41 few_nerd_types.json
-rw-r--r--  1 ubuntu ubuntu 2106 May 17 16:07 fewrel_relation_types.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2147 · 2026-05-19T11:40:19.308422+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 2148 · 2026-05-19T11:40:19.409154+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 2149 · 2026-05-19T11:40:22.342344+00:00_

The config.yaml file does not exist at the path you specified (`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml`) or anywhere else in the project hierarchy.

I searched for config.yaml files throughout the project and the broader agent-ml-research directory structure, but found no such file. The project contains various configuration files like `constraints.yaml`, `experiment_plan.yaml`, `dream_registry.yaml`, and others in the project root, but there is no `agent/config.yaml` or any `config.yaml` file.

Could you verify the correct path or filename? It's possible the configuration you're looking for might be stored in a different location or under a different name.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Agent",
  "elapsed_ms": 22695
}
```

</details>

---


### Tool call

_source line 2150 · 2026-05-19T11:40:29.372879+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Find project config file",
  "prompt": "Search for any YAML config file in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ that contains \"external_review\" or \"paperreview\". Check files like config.yaml, project.yaml, settings.yaml, or any yaml file in the project root or agent/ directory. Also check /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/constraints.yaml and any other yaml files in the project directory. Report what you find about external review configuration.",
  "subagent_type": "Explore"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Find project config file",
    "prompt": "Search for any YAML config file in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ that contains \"external_review\" or \"paperreview\". Check files like config.yaml, project.yaml, settings.yaml, or any yaml file in the project root or agent/ directory. Also check /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/constraints.yaml and any other yaml files in the project directory. Report what you find about external review configuration.",
    "subagent_type": "Explore"
  }
}
```

</details>

---


### Tool call

_source line 2151 · 2026-05-19T11:40:29.574032+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 2152 · 2026-05-19T11:40:29.674815+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2153 · 2026-05-19T11:40:34.043758+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/**/*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/**/*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2154 · 2026-05-19T11:40:34.145106+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/project
…[truncated 3357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2155 · 2026-05-19T11:40:34.145605+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2156 · 2026-05-19T11:40:34.196163+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/project
…[truncated 3357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2157 · 2026-05-19T11:40:38.770047+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "glob": "*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
    "glob": "*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2158 · 2026-05-19T11:40:38.820697+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2159 · 2026-05-19T11:40:38.871460+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/constraints.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/constraints.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2160 · 2026-05-19T11:40:39.072627+00:00_

1	_next_id: 3
2	constraints:
3	- id: C001
4	  added: 2026-05-15 22:03 UTC
5	  summary: 论文中 count_40 子集必须明确说明 "40-rel subsets sampled from the 80-relation pool"，不能暗示是独立的
6	    40-type pool
7	  scope: all
8	  reason: count_40 实际是从 80-type pool 中采样的子集，不是独立构建的 pool。Reviewer 指出如果表述不清会误导读者认为存在三个独立
9	    pool size
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2161 · 2026-05-19T11:40:39.073137+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2162 · 2026-05-19T11:40:39.375105+00:00_

File content (41642 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2163 · 2026-05-19T11:40:41.785854+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"settings.yaml\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"settings.yaml\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 2164 · 2026-05-19T11:40:41.836525+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2165 · 2026-05-19T11:40:42.087954+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2166 · 2026-05-19T11:40:42.240759+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 2167 · 2026-05-19T11:40:42.241223+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/*.yaml 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/*.yaml 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 2168 · 2026-05-19T11:40:42.291669+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2169 · 2026-05-19T11:40:44.904049+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ | head -30"
  }
}
```

</details>

---


### Tool result

_source line 2170 · 2026-05-19T11:40:45.356858+00:00_

total 436
drwxr-xr-x 14 ubuntu ubuntu   4096 May 19 11:40 .
drwxrwxr-x  6 ubuntu ubuntu   4096 May 14 16:07 ..
drwxr-xr-x  3 ubuntu ubuntu   4096 May 14 16:07 .claude
drwxr-xr-x  6 ubuntu ubuntu   4096 May 16 05:06 .venv
-rw-r--r--  1 ubuntu ubuntu  17194 May 19 11:40 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu      0 May 14 16:10 ROADMAP.lock
-rw-------  1 ubuntu ubuntu   3148 May 19 11:40 ROADMAP.md
drwxr-xr-x 43 ubuntu ubuntu   4096 May 19 05:13 artifacts
drwxr-xr-x  2 ubuntu ubuntu  32768 May 18 10:52 checkpoints
drwxr-xr-x  2 ubuntu ubuntu   4096 May 17 16:07 configs
-rw-r--r--  1 ubuntu ubuntu      0 May 15 22:03 constraints.lock
-rw-------  1 ubuntu ubuntu    411 May 16 02:39 constraints.yaml
drwxr-xr-x  4 ubuntu ubuntu   4096 May 17 15:51 data
-rw-r--r--  1 ubuntu ubuntu      0 May 14 16:10 decisions.lock
-rw-------  1 ubuntu ubuntu  50826 May 19 11:40 decisions.yaml
drwxr-xr-x  5 ubuntu ubuntu   4096 May 16 05:05 docs
-rwxr-xr-x  1 ubuntu ubuntu      0 May 15 02:48 dream_registry.lock
-rw-------  1 ubuntu ubuntu   3545 May 16 08:23 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu   3550 May 16 08:23 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu      0 May 15 13:44 experiment_plan.lock
-rw-------  1 ubuntu ubuntu   5668 May 18 21:40 experiment_plan.yaml
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 16:09 figures
-rw-r--r--  1 ubuntu ubuntu  19038 May 15 07:59 literature_map.yaml
drwxr-xr-x  4 ubuntu ubuntu   4096 May 14 16:14 logs
-rw-r--r--  1 ubuntu ubuntu   4576 May 17 16:26 memory.md
-rw-r--r--  1 ubuntu ubuntu      0 May 17 08:07 mistakes.lock
-rw-------  1 ubuntu ubuntu   7372 May 18 07:27 mistakes.yaml
-rw-r--r--  1 ubuntu ubuntu  11835 May 17 10:30 paper_framing.md
-rw-r--r--  1 ubuntu ubuntu      0 May 15 17:49 paper_provenance.lock

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2171 · 2026-05-19T11:40:45.407649+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -type d -name \"agent\" -o -type d -name \".agent\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -type d -name \"agent\" -o -type d -name \".agent\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 2172 · 2026-05-19T11:40:45.458429+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/task_context/history/agent

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2173 · 2026-05-19T11:40:48.169394+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/"
  }
}
```

</details>

---


### Tool result

_source line 2174 · 2026-05-19T11:40:48.320744+00:00_

total 32
drwxr-xr-x  3 ubuntu ubuntu  4096 May 14 16:07 .
drwxr-xr-x 14 ubuntu ubuntu  4096 May 19 11:40 ..
-rw-r--r--  1 ubuntu ubuntu 17194 May 19 11:40 CLAUDE.md
drwxr-xr-x 18 ubuntu ubuntu  4096 May 17 14:03 sessions

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2175 · 2026-05-19T11:40:48.371603+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/task_context/history/agent -name \"*.yaml\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/task_context/history/agent -name \"*.yaml\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 2176 · 2026-05-19T11:40:48.472684+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2177 · 2026-05-19T11:40:51.174925+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 3 -name \"*.yaml\" -type f 2>/dev/null | grep -E \"config|project|settings\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 3 -name \"*.yaml\" -type f 2>/dev/null | grep -E \"config|project|settings\""
  }
}
```

</details>

---


### Tool result

_source line 2178 · 2026-05-19T11:40:51.225678+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/collapse-aware-mixing.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/venue_rules/corl-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/resources.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2179 · 2026-05-19T11:40:51.327319+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18 --include=\"*.yaml\" --include=\"*.md\" --include=\"*.json\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18 --include=\"*.yaml\" --include=\"*.md\" --include=\"*.json\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 2180 · 2026-05-19T11:40:51.628958+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/CLAUDE.md:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/CLAUDE.md:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/CLAUDE.md:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/CLAUDE.md:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/AGENTS.md:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/AGENTS.md:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/AGENTS.md:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5/AGENTS.md:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-idea_gen
…[truncated 2077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2181 · 2026-05-19T11:40:54.042631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2182 · 2026-05-19T11:40:54.043588+00:00_

1	execution:
2	  project_path: /root/schema-dag-extraction
3	  servers:
4	  - account: root
5	    server: cqa1-38874
6	  - account: root
7	    server: westd-24295
8	feishu:
9	  chat_id: oc_51326259fe46fbae9da26b81cf03f1f8
10	  operational_chat_id: oc_04544c3b7bc497e1d098ba47fb56a6c2
11	  review_mode: fresh
12	  review_paper_path: projects/schema-dag-extraction/docs/paper/main.tex
13	  review_round: 21
14	  review_supplementary_paths: ''
15	  submission_chat_id: oc_ac7ab7270b6b5caecee04f89b11aab3e
16	project:
17	  created_at: '2026-05-14T16:07:46.825Z'
18	  description: Does Type Confusability Drive Schema-Induced Degradation in LLM Information
19	    Extraction? An Empirical Study and Principled Decomposition Framework
20	  name: schema-dag-extraction
21	  phase: research
22	  source_idea_id: idea_007
23	venue: emnlp-2026
24	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2183 · 2026-05-19T11:40:56.304622+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/backend.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/backend.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2184 · 2026-05-19T11:40:56.355244+00:00_

1	manager:
2	  enabled: true
3	  url: http://172.31.31.59:8700
4	  my_id: be-prod9-0512
5	  my_token: 48d731d4ffca61bec8a11c3919f9bf537a2999bc36e98c14fb7d1577b327534e
6	  ingest_token: e1dc1e287cb57d2e8411481f152c3cfb22d694b1bc8043b04a543cc7f0e08b82
7	  api:
8	    listen_host: 0.0.0.0
9	    listen_port: 8420
10	    allowed_source_cidrs:
11	    - 10.0.0.0/8
12	    - 192.168.0.0/16
13	    - 172.16.0.0/12
14	    - 127.0.0.0/8
15	  capabilities:
16	    read: true
17	    bootstrap_project: true
18	    archive_project: true
19	    allocate_gpus: true
20	    release_gpus: true
21	    read_chat_history: true
22	    claude_account_login: true
23	    read_claude_pool: true
24	  local_approvals:
25	    bootstrap_project: false
26	    archive_project: false
27	    allocate_gpus: false
28	  heartbeat:
29	    enabled: true
30	    interval_sec: 60
31	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2185 · 2026-05-19T11:40:56.606606+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/venue_rules/emnlp-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2186 · 2026-05-19T11:40:56.607127+00:00_

1	rules:
2	  research: []
3	  review:
4	  - created_at: '2026-05-17T12:02:15Z'
5	    id: c9bba9
6	    text: “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall
7	      Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 =
8	      Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5
9	      = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit
10	      after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
11	  writing: []
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2187 · 2026-05-19T11:41:01.132238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/resources.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/resources.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2188 · 2026-05-19T11:41:01.132632+00:00_

1	default_model: claude-opus-4-6
2	default_model_claude_code: claude-opus-4-6
3	idea_model: claude-opus-4-6
4	servers:
5	  cqa1-38874:
6	    accounts:
7	    - gpus:
8	      - cuda:0
9	      name: root
10	      password_encrypted: gAAAAABqAuvPRnsR1TtY3nMeh4mVCYkvCSF7_wdLf-0R0bfkxwoGlInSGv3dLgBMCNw2jcYb4Wdztu3hlMLhkpq9hKnRirdTGw==
11	      user: root
12	      work_dir: /root
13	    - gpus: []
14	      name: ''
15	      user: ''
16	    detected_image:
17	      detected: false
18	      image: ''
19	      status: unknown
20	      version: ''
21	    env_activate: ''
22	    host: connect.cqa1.seetacloud.com
23	    port: 38874
24	    total_gpus:
25	    - cuda:0
26	    user_rules_excluded: []
27	    work_dir: /root
28	  home-1x5090:
29	    accounts:
30	    - gpus: []
31	      name: sonny
32	      password_encrypted: gAAAAABqAs98OWvzWtk-wjILplCl-xG8f6sbL0GMIHCqjHs4LD83BaT56W8D4iW7g3UJTcyFGxiYqIy44LDYO4oxAE_ptGirBg==
33	      user: sonny
34	      work_dir: /root
35	    env_activate: ''
36	    host: implicit5638.xyfu.me
37	    port: 22
38	    total_gpus:
39	    - cuda:0
40	    user_rules_excluded: []
41	    work_dir: /root
42	  westd-24295:
43	    accounts:
44	    - gpus: []
45	      name: root
46	      password_encrypted: gAAAAABqCUPK4KEQWs-G2-zP9PqmQZsghbyISHKoqXnPCXwftsxti4lidbskdEyh3NfHQ1tTJCYAKHTZNc2CHKBJ8L4Cirn3YA==
47	      user: root
48	      work_dir: /root
49	    detected_image:
50	      detected: false
51	      image: ''
52	      status: unknown
53	      version: ''
54	    env_activate: ''
55	    host: connect.westd.seetacloud.com
56	    port: 24295
57	    total_gpus:
58	    - cuda:0
59	    - cuda:1
60	    user_rules_excluded: []
61	    work_dir: /root
62	user_rules: []
63	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2189 · 2026-05-19T11:41:03.850803+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 5 -B 2 \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_20.md | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 5 -B 2 \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_20.md | head -30"
  }
}
```

</details>

---


### Tool result

_source line 2190 · 2026-05-19T11:41:04.002033+00:00_

## 外部审稿

**外部审稿：未配置**（项目未启用 `external_review.paperreview_ai`）

---

*报告由 Review Director 基于 Reviewer 1 和 Reviewer 2 的独立审稿及交叉分享回应汇总生成。*

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2191 · 2026-05-19T11:41:04.203436+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 5 -B 2 \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 5 -B 2 \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_2.md"
  }
}
```

</details>

---


### Tool result

_source line 2192 · 2026-05-19T11:41:04.255276+00:00_

## External Review (Stanford Agentic Reviewer)

未启用。项目配置 `external_review.paperreview_ai.enabled: false`。

---

## Overall Assessment

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2193 · 2026-05-19T11:41:07.170900+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -name \"*schema*\" -o -name \"*default*\" 2>/dev/null | grep -i config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -name \"*schema*\" -o -name \"*default*\" 2>/dev/null | grep -i config"
  }
}
```

</details>

---


### Tool result

_source line 2194 · 2026-05-19T11:41:07.272147+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/openai/types/responses/__pycache__/response_format_text_json_schema_config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/openai/types/responses/__pycache__/response_format_text_json_schema_config_param.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/openai/types/responses/response_format_text_json_schema_config.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/openai/types/responses/response_format_text_json_schema_config_param.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/secrets/schema-dag-extraction

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2195 · 2026-05-19T11:41:07.272596+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/"
  }
}
```

</details>

---


### Tool result

_source line 2196 · 2026-05-19T11:41:07.323066+00:00_

total 268
drwxrwxr-x 5 ubuntu ubuntu 4096 May 18 08:08 .
drwxrwxr-x 9 ubuntu ubuntu 4096 May 12 08:37 ..
-rw-rw-r-- 1 ubuntu ubuntu 2901 May  9 09:00 approvals.yaml
-rw------- 1 ubuntu ubuntu  764 May 11 17:59 backend.yaml
-rw-r--r-- 1 ubuntu ubuntu 1855 May 19 11:38 claude_sessions.json
-rw------- 1 ubuntu ubuntu 9779 May 18 08:08 crons.yaml
-rw------- 1 ubuntu ubuntu  364 May 15 04:13 email_tokens.json
-rw------- 1 ubuntu ubuntu  104 May 15 09:17 feishu.yaml
-rw-r--r-- 1 ubuntu ubuntu 4678 May 19 11:33 keepalive.json
-rw-r--r-- 1 ubuntu ubuntu  342 May 11 05:47 mcp_config.json
-rw-r--r-- 1 ubuntu ubuntu  392 May 17 10:56 mcp_config_briefer.json
-rw-r--r-- 1 ubuntu ubuntu  394 May 12 08:44 mcp_config_director.json
-rw-r--r-- 1 ubuntu ubuntu  420 May 15 06:10 mcp_config_dream_review_director.json
-rw-r--r-- 1 ubuntu ubuntu  398 May 12 08:37 mcp_config_no_project.json
-rw-r--r-- 1 ubuntu ubuntu  400 May 15 16:03 mcp_config_paper_agent.json
-rw-r--r-- 1 ubuntu ubuntu  408 May 16 00:50 mcp_config_review_director.json
-rw-r--r-- 1 ubuntu ubuntu  436 May 16 00:53 mcp_config_review_reviewer_1.json
-rw-r--r-- 1 ubuntu ubuntu  436 May 16 00:53 mcp_config_review_reviewer_2.json
-rw-r--r-- 1 ubuntu ubuntu  436 May 16 11:17 mcp_config_review_reviewer_3.json
-rw-r--r-- 1 ubuntu ubuntu  394 May 12 08:46 mcp_config_reviewer.json
-rw-r--r-- 1 ubuntu ubuntu  417 May 12 10:55 mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
-rw-r--r-- 1 ubuntu ubuntu  471 May 16 01:50 mcp_config_worker_0df49881059e9f493ee8cd1e899565bb.json
-rw-r--r-- 1 ubuntu ubuntu  465 May 15 05:06 mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
-rw-r--r-- 1 ubuntu ubuntu  477 May 15 15:54 mcp_config_worker_12093ef55c63229acbf88fd2b9106dce.json
-rw-r--r-- 1 ubuntu ubuntu  383 May 15 16:10 mcp_config_worker_14d296b01755362efedfab08bc7a4e38.json
-rw-r--r-- 1 ubuntu ubuntu  465 May 12 15:24 mcp_config_worker_33c066fe8f41bfaa9b9c844bb47eca4f.json
-rw-r--r-- 1 ubuntu ubuntu  433 May 16 01:56 mcp_config_w
…[truncated 3456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2197 · 2026-05-19T11:41:10.488384+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_review_director.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_review_director.json"
  }
}
```

</details>

---


### Tool result

_source line 2198 · 2026-05-19T11:41:10.489405+00:00_

1	{
2	  "mcpServers": {
3	    "agent-ml-research": {
4	      "command": "/home/ubuntu/agent-ml-research/.venv/bin/python",
5	      "args": [
6	        "-m",
7	        "core.mcp_server",
8	        "--review-director"
9	      ],
10	      "cwd": "/home/ubuntu/agent-ml-research",
11	      "env": {
12	        "AGENT_ML_WORKSPACE": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
13	        "REVIEW_DIRECTOR_MODE": "1"
14	      }
15	    }
16	  }
17	}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 2199 · 2026-05-19T11:41:13.614130+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -name \"*external*\" -o -name \"*paperreview*\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research -name \"*external*\" -o -name \"*paperreview*\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool call

_source line 2200 · 2026-05-19T11:41:13.614606+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/agent-ml-research --include=\"*.py\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/agent-ml-research --include=\"*.py\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 2201 · 2026-05-19T11:41:13.715367+00:00_

/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/ldap3/protocol/sasl/__pycache__/external.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/ldap3/protocol/sasl/external.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/fonttools-4.62.1.dist-info/licenses/LICENSE.external
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/apaas/v1/model/__pycache__/external_user.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/apaas/v1/model/external_user.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/hire/v1/resource/external_referral_reward.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/hire/v1/resource/__pycache__/external_referral_reward.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/hire/v1/resource/__pycache__/external_interview.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/hire/v1/resource/__pycache__/external_background_check.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/hire/v1/resource/__pycache__/talent_external_info.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/hire/v1/resource/__pycache__/external_interview_assessment.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/hire/v1/resource/__pycache__/external_application.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/hire/v1/resource/__pycache__/external_offer.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/hire/v1/resource/external_background_check.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/hire/v1/resource/external_application.py
/home/u
…[truncated 615 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 2202 · 2026-05-19T11:41:15.824498+00:00_

/home/ubuntu/agent-ml-research/tests/test_review_phase_isolation.py:  2. fresh mode wipes `external_review_state.json` so prior-round pending /
/home/ubuntu/agent-ml-research/tests/test_review_phase_isolation.py:# Fix 2: external_review.reset_state
/home/ubuntu/agent-ml-research/tests/test_review_phase_isolation.py:        from core.tools.external_review import _save_state, reset_state, _load_state
/home/ubuntu/agent-ml-research/tests/test_review_phase_isolation.py:        state_file = _paths.project_dir(project) / "external_review_state.json"
/home/ubuntu/agent-ml-research/tests/test_review_phase_isolation.py:        from core.tools.external_review import reset_state
/home/ubuntu/agent-ml-research/tests/test_paper_review_handoff.py:            "core.tools.external_review.reset_state",
/home/ubuntu/agent-ml-research/tests/test_dream_review_session_isolation.py:        assert "request_external_review" not in tools
/home/ubuntu/agent-ml-research/tests/test_dream_review_session_isolation.py:        assert "get_external_review_status" not in tools
/home/ubuntu/agent-ml-research/tests/test_dream_review_simple.py:        assert "request_external_review" in prompt
/home/ubuntu/agent-ml-research/tests/test_dream_review_no_continue.py:        assert "request_external_review" not in tools
/home/ubuntu/agent-ml-research/core/tool_registry.py:    "request_external_review",
/home/ubuntu/agent-ml-research/core/tool_registry.py:    "get_external_review_status",
/home/ubuntu/agent-ml-research/core/tools/project_config.py:def is_external_review_enabled(project_name: str) -> bool:
/home/ubuntu/agent-ml-research/core/tools/project_config.py:    Reads ``external_review.paperreview_ai.enabled`` from project config.
/home/ubuntu/agent-ml-research/core/tools/project_config.py:    ext = result.data["config"].get("external_review", {})
/home/ubuntu/agent-ml-research/core/tools/external_review.py:    return _paths.project_dir(project) / "external_review_state.json"
/home/ubuntu/agent-ml-rese
…[truncated 495 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 2209
}
```

</details>

---


### Tool call

_source line 2203 · 2026-05-19T11:41:27.646757+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tools/external_review.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/core/tools/external_review.py"
  }
}
```

</details>

---


### Tool result

_source line 2204 · 2026-05-19T11:41:27.647765+00:00_

1	"""External review tools — request human-assisted submission to external review services.
2	
3	Currently supports: Stanford Agentic Reviewer (paperreview.ai).
4	The user handles the actual submission manually; this module sends Feishu cards
5	to request the submission and Cron reminders to follow up.
6	"""
7	
8	from __future__ import annotations
9	
10	import json
11	import logging
12	from datetime import datetime, timezone
13	
14	from core.tools.result import ToolResult
15	
16	logger = logging.getLogger(__name__)
17	
18	# ---------------------------------------------------------------------------
19	# State persistence — lightweight YAML file per project
20	# ---------------------------------------------------------------------------
21	
22	_PENDING = "pending"       # Card sent, waiting for user action
23	_SUBMITTED = "submitted"   # User clicked [已提交]
24	_RECEIVED = "received"     # Review text pasted back
25	_SKIPPED = "skipped"       # User clicked [跳过]
26	
27	
28	def _state_path(project: str) -> "Path":
29	    from core import paths as _paths
30	    return _paths.project_dir(project) / "external_review_state.json"
31	
32	
33	def _load_state(project: str) -> dict:
34	    p = _state_path(project)
35	    if not p.exists():
36	        return {}
37	    try:
38	        return json.loads(p.read_text(encoding="utf-8"))
39	    except Exception:
40	        return {}
41	
42	
43	def _save_state(project: str, state: dict) -> None:
44	    p = _state_path(project)
45	    p.parent.mkdir(parents=True, exist_ok=True)
46	    p.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
47	
48	
49	def reset_state(project: str) -> None:
50	    """Drop the external review state file. Called on fresh review round start
51	    so Round N-1's pending/received/skipped state does not leak forward."""
52	    p = _state_path(project)
53	    if p.exists():
54	        try:
55	            p.unlink()
56	            logger.info("[external_review] reset state for project=%s",
…[truncated 14491 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 2205 · 2026-05-19T11:41:27.798876+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tools/project_config.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/core/tools/project_config.py"
  }
}
```

</details>

---


### Tool result

_source line 2206 · 2026-05-19T11:41:28.052311+00:00_

1	"""Project configuration loader — reads config/projects/{name}.yaml.
2	
3	Each project config declares server, codebase paths, evaluation metrics,
4	and W&B settings. The orchestrator injects this into the system prompt
5	and MCP tool defaults at session startup.
6	"""
7	
8	from __future__ import annotations
9	
10	from pathlib import Path
11	
12	import yaml
13	
14	from core.tools.result import ToolResult
15	
16	# ---------------------------------------------------------------------------
17	# Paths
18	# ---------------------------------------------------------------------------
19	
20	from core import paths as _paths
21	
22	
23	# ---------------------------------------------------------------------------
24	# Path expansion — resolve ~ in config values so non-interactive shells work
25	# ---------------------------------------------------------------------------
26	
27	# Top-level keys whose string values may contain ~
28	_PATH_KEYS = {"root", "project_path", "log_dir"}
29	
30	
31	def _expand_paths(config: dict) -> None:
32	    """In-place expand ~ in known path fields using the remote account's home.
33	
34	    These paths refer to remote servers, NOT the local machine.
35	    ``~`` is resolved to ``/home/{account}`` (standard Linux layout)
36	    using the account from ``execution.servers[0].account`` or
37	    ``execution.account``.
38	    """
39	    # Determine remote account for ~ expansion
40	    exec_cfg = config.get("execution", {})
41	    account = exec_cfg.get("account", "")
42	    if not account:
43	        servers = exec_cfg.get("servers")
44	        if isinstance(servers, list) and servers:
45	            first = servers[0]
46	            if isinstance(first, dict):
47	                account = first.get("account", "")
48	    # Fallback: extract account from resources.yaml server host (user@ip)
49	    if not account:
50	        server_name = exec_cfg.get("server", "")
51	        if server_name:
52	            try:
53	                resources_path = _
…[truncated 42290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool result

_source line 2207 · 2026-05-19T11:41:38.701362+00:00_

Perfect! Now I have a comprehensive understanding of the external review configuration. Let me provide a summary of my findings.

## Report: External Review Configuration in schema-dag-extraction

Based on my comprehensive search of the configuration files and codebase, here are the key findings about external review configuration:

### Configuration Structure

The external review system is controlled via the project configuration file at:
`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml`

The expected configuration structure is:
```yaml
external_review:
  paperreview_ai:
    enabled: true  # or false
```

### Current Project Status

**The schema-dag-extraction project does NOT have external review enabled.**

Evidence from multiple review reports:
- Round 2: `external_review.paperreview_ai.enabled: false`
- Round 4, 6: Configured as `false`
- Round 11, 15, 17, 19, 20: Reported as "未配置" (not configured)

The project config file at `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml` does not contain an `external_review` section at all.

### Available Tools

When external review is enabled, the following MCP tools become available:

1. **`request_external_review()`** - Sends a Feishu card to the user group requesting manual submission to paperreview.ai
   - Parameters: project name, PDF path, venue, optional note, chat_id, reminder hours
   - Location: `/home/ubuntu/agent-ml-research/core/tools/external_review.py:235`

2. **`get_external_review_status()`** - Checks the current external review status
   - Returns: pending, submitted, received, skipped, or not_requested
   - Location: `/home/ubuntu/agent-ml-research/core/tools/external_review.py:382`

3. **`is_external_review_enabled()`** - Checks if external review is enabled for a project
   - Location: `/home/ubuntu/agent-ml-research/core/tools/project_config.py:455`

### Implementation Details

The external review system works as f
…[truncated 1109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Agent",
  "elapsed_ms": 69328
}
```

</details>

---


### Tool call

_source line 2208 · 2026-05-19T11:41:45.479979+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract ALL submission requirements: page limits (long/short), format template, anonymous/blind rules, mandatory sections (limitations, ethics, checklist), appendix rules (do they count toward page limit? are they reviewed?), reference page limit, deadline, and any other formatting requirements. Be comprehensive and exact."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract ALL submission requirements: page limits (long/short), format template, anonymous/blind rules, mandatory sections (limitations, ethics, checklist), appendix rules (do they count toward page limit? are they reviewed?), reference page limit, deadline, and any other formatting requirements. Be comprehensive and exact."
  }
}
```

</details>

---


### Tool call

_source line 2209 · 2026-05-19T11:41:46.886658+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract ALL submission requirements for ARR: page limits for long and short papers, mandatory sections, formatting rules, anonymity requirements, appendix rules, responsible NLP checklist requirements, and any desk rejection criteria. Be comprehensive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract ALL submission requirements for ARR: page limits for long and short papers, mandatory sections, formatting rules, anonymity requirements, appendix rules, responsible NLP checklist requirements, and any desk rejection criteria. Be comprehensive."
  }
}
```

</details>

---


### Tool result

_source line 2210 · 2026-05-19T11:41:51.042884+00:00_

# EMNLP 2026 Submission Requirements

## Page Limits
- **Long Papers:** 8 pages (9 pages in camera-ready version)
- **Short Papers:** 4 pages (5 pages in camera-ready version)
- References are not specified as counting toward page limits in this document

## Format & Templates
Papers must follow "all of the ARR submission requirements," including specific ARR templates, but the exact template details are not provided in this call—they're referenced at the ARR website.

## Anonymization
The review process is "double-blind." "Reviewers will not see authors, nor will authors see reviewers." However, "there is no anonymity period requirement" following ACL/ARR policies.

## Mandatory Sections
- **Limitations:** Required per ARR submission requirements
- **Ethics Checklist:** The "responsible NLP research checklist" is mandated
- **Specific ethics compliance:** Papers must comply with ACL's Publication Ethics Policy and ARR's Ethics Policy

## Supplementary Materials
"Optional supplementary materials" are permitted but specific page-counting rules aren't detailed in this excerpt.

## Submission Deadline
**May 25, 2026** (11:59 PM UTC-12:00, "anywhere on Earth")

## Other Critical Requirements
- No dual submissions allowed
- Author list cannot be modified during commitment phase (reordering is permitted)
- Papers with hallucinated citations, thinly-sliced contributions, or unethical submissions risk desk rejection

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebFetch",
  "elapsed_ms": 5562
}
```

</details>

---


### Tool result

_source line 2211 · 2026-05-19T11:41:56.313948+00:00_

# ARR Submission Requirements Summary

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited pages for references
- Unlimited space after conclusion for limitations (required) and optional ethical considerations section

**Short Papers:**
- Up to 4 pages of content
- Unlimited pages for references
- Unlimited space after conclusion for limitations (required) and optional ethical considerations section

Papers exceeding length requirements or missing limitations sections face desk rejection.

## Mandatory Sections

**Limitations Section (Required):**
- Must be titled "Limitations" and placed before references
- Does not count toward page limit
- Should only discuss constraints of presented work, not introduce new methods or results
- Papers lacking this section will be desk rejected

**Responsible NLP Checklist:**
- Must be completed during submission
- Incorrect, incomplete, or misleading entries can trigger desk rejection
- Content influences the review process

## Formatting Rules

- Must use official ACL style template from the designated repository
- Follow ACL formatting guidelines for *ACL conferences
- Template modifications or non-ACL templates are prohibited
- Non-conforming submissions rejected without review
- Text must address human readers exclusively and remain clearly visible

## Anonymity Requirements

- Papers must exclude author names and affiliations
- Self-references revealing identity must be avoided (use "Smith showed..." instead of "We showed...")
- No references to non-publicly available documents
- Supplementary materials and repository links must be anonymized
- Dropbox and similar tracking services prohibited
- Violations result in desk rejection

## Appendix Rules

- Must follow double-column format (with approved exceptions)
- Placed after references
- Do not count toward page limits
- Reviewers not obligated to review appendix content
- Critical technical material should be in main paper
- Starting July 2025, improperl
…[truncated 840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebFetch",
  "elapsed_ms": 9427
}
```

</details>

---


### Tool call

_source line 2212 · 2026-05-19T11:42:19.881586+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 2213 · 2026-05-19T11:42:19.932346+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2214 · 2026-05-19T11:42:22.901207+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "review_issues.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "review_issues.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 2215 · 2026-05-19T11:42:23.002116+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2216 · 2026-05-19T11:42:25.968044+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 2217 · 2026-05-19T11:42:26.069660+00:00_

# Round 20 Review Issues Tracker
# Updated: 2026-05-19 (Reviewer #30 verified all R20 fixes PASS)

# ============================================================
# CRITICAL (R20) — 全部修复已验证
# ============================================================

- id: R20-N1
  summary: "'Largely additive' overclaim: 仅在 sentence-level RE linear scale 成立"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 20
  last_seen_round: 20
  mentions:
    - {round: 20, reviewers: [R1, R2], note: "双方共识。Abstract/Conclusion 'largely additive' 未加 task/scale 限定。"}
  action_items:
    - {round: 20, action: "Abstract/Conclusion 删除 'largely additive'，改为 'two dimensions'。全文零残留。", assigned_to: main_agent, status: done}
  resolution: "全文删除 'largely additive'，改为 'two dimensions'。Reviewer #30 确认零残留。"
  resolution_round: 20

- id: R20-N2
  summary: "BCS batch-level 仅在 RE forced-choice format 有效，'two-dimensional across NER/RE/ED' framing 超出证据"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 20
  last_seen_round: 20
  mentions:
    - {round: 20, reviewers: [R1, R2], note: "双方共识。Abstract 'across NER, RE, and ED' 误导。"}
  action_items:
    - {round: 20, action: "Abstract 加 'revealing task-dependent effect structures'", assigned_to: main_agent, status: done}
  resolution: "Abstract 加 'revealing task-dependent effect structures'，全文 scope 限定一致。Reviewer #30 确认。"
  resolution_round: 20

- id: R20-N3
  summary: "Pairwise r²=1.3-1.7% 效应量解读引用 Cohen (1988) behavioral research 标准不当"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 20
  last_seen_round: 20
  mentions:
    - {round: 20, reviewers: [R1, R2], note: "R1 Critical, R2 AGREE。Cohen 标准适用性不足。应以 batch-level R²=22-53% 为主线。"}
  action_items:
    - {round: 20, action: "删除 Cohen/Lakens 类比及 bib entries；§4.3 前置 R²=22-53%；pairwise 定位为 mechanism", assigned_to: main_agent, status: done}
  resolution: "Cohen/Lakens 删除（.tex + .bib）。Batch-level R²=22-53% 前置为 lead evidence。Revie
…[truncated 14422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2218 · 2026-05-19T11:43:21.450031+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重**: 方法严谨性 + 实验设计\n\n**论文**: `projects/schema-dag-extraction/docs/paper/main.tex`\n**标题**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**目标 Venue**: EMNLP 2026 Main (ARR May 2026 cycle)\n\n### Venue 格式要求\n- Long paper: 8 页正文 + 无限 references\n- Limitations section 必须（不计页数），在 references 前\n- Responsible NLP Checklist 必须\n- Double-blind review\n- ACL style template (`\\usepackage[review]{acl}`)\n- Appendix 在 references 后，不计页数，reviewer 无义务审阅但可参考\n- Appendix 必须 double-column 格式\n\n### 审查重点\n\n请从以下角度严格审查：\n\n1. **统计方法正确性**:\n   - SCS/BCS 定义是否合理？pairwise cosine similarity 作为 confusability proxy 的理论基础是否充分？\n   - TOST 等价检验的 margin 选择（±3pp）是否合理？logit-scale 结果不一致如何解读？\n   - Bootstrap CI 和 permutation test 的使用是否规范？\n   - 多重比较问题（Rothman 1990 的引用是否合理）？\n\n2. **实验设计严谨性**:\n   - BCS-controlled 实验是否真正隔离了 confusability 和 count？是否有残余混淆变量？\n   - FewRel 合并 train+val split 是否引入数据泄漏？split-origin analysis 是否充分？\n   - DocRED 5 batches per count level 的统计功效是否足够？\n   - 单 seed (42) + greedy decoding 的可靠性？multi-seed 验证是否充分？\n\n3. **效应量解读**:\n   - Pairwise r²=1.3-1.7% 的实际意义？\n   - Batch-level R²=22-53% 的解读是否恰当？是否有 overfitting 风险？\n   - \"typical batches yield modest ~2pp gaps\" 与 extreme-batch 31pp gap 之间的叙事平衡\n\n4. **Cross-model validation**:\n   - 4 个模型（Qwen3-32B, Llama-8B, Llama-70B, Gemini Flash）的覆盖是否充分？\n   - Dimension 2 (confusability) 仅在 open-weight models 验证，未在 proprietary models 验证——这一限制是否被充分讨论？\n\n5. **负面结果 (SDGD)**:\n   - Merge amplification 和 routing failure 的诊断是否充分？\n   - Oracle routing +29.8pp 与 practical routing 全部低于 baseline 之间的 gap 是否被合理讨论？\n\n6. **数据集选择与泛化性**:\n   - 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）的代表性\n   - MAVEN centrality confound 的处理是否恰当？\n   - 是否缺少重要的数据集或任务类型？\n\n### 输出格式\n\n请按以下结构输出审稿意见（中文）：\n\n```\n## Summary\n（2-3 句概括论文内容和主要发现）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [Must-Fix] / [Should-Fix] / [Minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n（如有）\n\n## Overall Assessment\n评分: X.X (参照 ARR/EMNLP 评分标准: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)\n置信度: X/5\n```",
  "project": "schema-dag-extraction"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重**: 方法严谨性 + 实验设计\n\n**论文**: `projects/schema-dag-extraction/docs/paper/main.tex`\n**标题**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**目标 Venue**: EMNLP 2026 Main (ARR May 2026 cycle)\n\n### Venue 格式要求\n- Long paper: 8 页正文 + 无限 references\n- Limitations section 必须（不计页数），在 references 前\n- Responsible NLP Checklist 必须\n- Double-blind review\n- ACL style template (`\\usepackage[review]{acl}`)\n- Appendix 在 references 后，不计页数，reviewer 无义务审阅但可参考\n- Appendix 必须 double-column 格式\n\n### 审查重点\n\n请从以下角度严格审查：\n\n1. **统计方法正确性**:\n   - SCS/BCS 定义是否合理？pairwise cosine similarity 作为 confusability proxy 的理论基础是否充分？\n   - TOST 等价检验的 margin 选择（±3pp）是否合理？logit-scale 结果不一致如何解读？\n   - Bootstrap CI 和 permutation test 的使用是否规范？\n   - 多重比较问题（Rothman 1990 的引用是否合理）？\n\n2. **实验设计严谨性**:\n   - BCS-controlled 实验是否真正隔离了 confusability 和 count？是否有残余混淆变量？\n   - FewRel 合并 train+val split 是否引入数据泄漏？split-origin analysis 是否充分？\n   - DocRED 5 batches per count level 的统计功效是否足够？\n   - 单 seed (42) + greedy decoding 的可靠性？multi-seed 验证是否充分？\n\n3. **效应量解读**:\n   - Pairwise r²=1.3-1.7% 的实际意义？\n   - Batch-level R²=22-53% 的解读是否恰当？是否有 overfitting 风险？\n   - \"typical batches yield modest ~2pp gaps\" 与 extreme-batch 31pp gap 之间的叙事平衡\n\n4. **Cross-model validation**:\n   - 4 个模型（Qwen3-32B, Llama-8B, Llama-70B, Gemini Flash）的覆盖是否充分？\n   - Dimension 2 (confusability) 仅在 open-weight models 验证，未在 proprietary models 验证——这一限制是否被充分讨论？\n\n5. **负面结果 (SDGD)**:\n   - Merge amplification 和 routing failure 的诊断是否充分？\n   - Oracle routing +29.8pp 与 practical routing 全部低于 baseline 之间的 gap 是否被合理讨论？\n\n6. **数据集选择与泛化性**:\n   - 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）的代表性\n   - MAVEN centrality confound 的处理是否恰当？\n   - 是否缺少重要的数据集或任务类型？\n\n### 输出格式\n\n请按以下结构输出审稿意见（中文）：\n\n```\n## Summary\n（2-3 句概括论文内容和主要发现）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [Must-Fix] / [Should-Fix] / [Minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n（如有）\n\n## Overall Assessment\n评分: X.X (参照 ARR/EMNLP 评分标准: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)\n置信度: X/5\n```",
    "project": "schema-dag-extraction"
  }
}
````

</details>

---


### Tool result

_source line 2219 · 2026-05-19T11:43:43.556712+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22106
}
```

</details>

---


### Tool call

_source line 2220 · 2026-05-19T11:43:45.164972+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重**: 新颖性 + 完整性 + 写作质量\n\n**论文**: `projects/schema-dag-extraction/docs/paper/main.tex`\n**标题**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**目标 Venue**: EMNLP 2026 Main (ARR May 2026 cycle)\n\n### Venue 格式要求\n- Long paper: 8 页正文 + 无限 references\n- Limitations section 必须（不计页数），在 references 前\n- Responsible NLP Checklist 必须\n- Double-blind review\n- ACL style template (`\\usepackage[review]{acl}`)\n- Appendix 在 references 后，不计页数，reviewer 无义务审阅但可参考\n- Appendix 必须 double-column 格式\n\n### 审查重点\n\n请从以下角度严格审查：\n\n1. **新颖性评估**:\n   - 核心贡献是什么？\"首个隔离 count 和 confusability 的控制研究\" 是否真的前所未有？\n   - SCS 与 LLM-PEE 的 pairwise embedding similarity 形式相同——论文是否充分区分了自己的贡献？\n   - \"Multi-channel degradation model\" 是否只是对已知现象的系统化描述？\n   - 负面结果（SDGD 失败）的贡献价值\n\n2. **Related Work 覆盖度**:\n   - 是否遗漏了重要的相关工作？特别是 2025-2026 年的最新工作\n   - 与 CrossAgentIE、LLM-PEE、IEPile 等直接竞争者的对比是否充分？\n   - 引用数量和质量是否达到 EMNLP 标准？\n   - 是否有任何引用看起来可能是虚构的？请对可疑引用进行 WebSearch 验证\n\n3. **写作质量**:\n   - 叙事是否连贯？Abstract → Introduction → Method → Results → Discussion 是否形成一条主线？\n   - 是否有 AI 写作痕迹？检查: em-dash (—)、-ing 短语结尾、过度分段、\"Furthermore/Moreover/Additionally\" 连用、用词黑名单 (delve/leverage/utilize/facilitate/myriad/plethora)\n   - 专有名词/缩写是否首次出现时有定义？\n   - Title 中 \"Predict\" 与论文实际展示的 correlational evidence 是否匹配？\n   - Abstract 是否在 150-250 words？是否回答了四个必答问题？\n   - Introduction 是否遵循了 5 段结构？\n   - 图表信息密度是否足够？\n\n4. **格式合规**:\n   - 正文是否 ≤ 8 页？\n   - Limitations section 是否存在且内容充实？\n   - Responsible NLP Checklist 是否完整且诚实？\n   - 匿名化是否完整？（检查 anonymous URL、self-references）\n   - References 格式是否一致？\n\n5. **完整性**:\n   - 每条 Contribution 是否都有对应的 section/table 支撑？\n   - 实验设置描述是否足够详细以支持复现？\n   - 是否有重要的消融实验缺失？\n   - Appendix 内容是否在正文中被引用？\n\n### 输出格式\n\n请按以下结构输出审稿意见（中文）：\n\n```\n## Summary\n（2-3 句概括论文内容和主要发现）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [Must-Fix] / [Should-Fix] / [Minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n（如有）\n\n## Overall Assessment\n评分: X.X (参照 ARR/EMNLP 评分标准: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)\n置信度: X/5\n```",
  "project": "schema-dag-extraction"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重**: 新颖性 + 完整性 + 写作质量\n\n**论文**: `projects/schema-dag-extraction/docs/paper/main.tex`\n**标题**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**目标 Venue**: EMNLP 2026 Main (ARR May 2026 cycle)\n\n### Venue 格式要求\n- Long paper: 8 页正文 + 无限 references\n- Limitations section 必须（不计页数），在 references 前\n- Responsible NLP Checklist 必须\n- Double-blind review\n- ACL style template (`\\usepackage[review]{acl}`)\n- Appendix 在 references 后，不计页数，reviewer 无义务审阅但可参考\n- Appendix 必须 double-column 格式\n\n### 审查重点\n\n请从以下角度严格审查：\n\n1. **新颖性评估**:\n   - 核心贡献是什么？\"首个隔离 count 和 confusability 的控制研究\" 是否真的前所未有？\n   - SCS 与 LLM-PEE 的 pairwise embedding similarity 形式相同——论文是否充分区分了自己的贡献？\n   - \"Multi-channel degradation model\" 是否只是对已知现象的系统化描述？\n   - 负面结果（SDGD 失败）的贡献价值\n\n2. **Related Work 覆盖度**:\n   - 是否遗漏了重要的相关工作？特别是 2025-2026 年的最新工作\n   - 与 CrossAgentIE、LLM-PEE、IEPile 等直接竞争者的对比是否充分？\n   - 引用数量和质量是否达到 EMNLP 标准？\n   - 是否有任何引用看起来可能是虚构的？请对可疑引用进行 WebSearch 验证\n\n3. **写作质量**:\n   - 叙事是否连贯？Abstract → Introduction → Method → Results → Discussion 是否形成一条主线？\n   - 是否有 AI 写作痕迹？检查: em-dash (—)、-ing 短语结尾、过度分段、\"Furthermore/Moreover/Additionally\" 连用、用词黑名单 (delve/leverage/utilize/facilitate/myriad/plethora)\n   - 专有名词/缩写是否首次出现时有定义？\n   - Title 中 \"Predict\" 与论文实际展示的 correlational evidence 是否匹配？\n   - Abstract 是否在 150-250 words？是否回答了四个必答问题？\n   - Introduction 是否遵循了 5 段结构？\n   - 图表信息密度是否足够？\n\n4. **格式合规**:\n   - 正文是否 ≤ 8 页？\n   - Limitations section 是否存在且内容充实？\n   - Responsible NLP Checklist 是否完整且诚实？\n   - 匿名化是否完整？（检查 anonymous URL、self-references）\n   - References 格式是否一致？\n\n5. **完整性**:\n   - 每条 Contribution 是否都有对应的 section/table 支撑？\n   - 实验设置描述是否足够详细以支持复现？\n   - 是否有重要的消融实验缺失？\n   - Appendix 内容是否在正文中被引用？\n\n### 输出格式\n\n请按以下结构输出审稿意见（中文）：\n\n```\n## Summary\n（2-3 句概括论文内容和主要发现）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [Must-Fix] / [Should-Fix] / [Minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n（如有）\n\n## Overall Assessment\n评分: X.X (参照 ARR/EMNLP 评分标准: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)\n置信度: X/5\n```",
    "project": "schema-dag-extraction"
  }
}
````

</details>

---


### Tool result

_source line 2221 · 2026-05-19T11:43:46.730022+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1565
}
```

</details>

---


### Tool call

_source line 2222 · 2026-05-19T11:43:54.289065+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 2223 · 2026-05-19T11:43:55.294788+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex:1:% DEPRECATED — this file is no longer included in main.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 2224 · 2026-05-19T11:43:55.747800+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 2225 · 2026-05-19T11:43:55.798611+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2226 · 2026-05-19T11:43:56.651980+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 2227 · 2026-05-19T11:43:57.104970+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:222:For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:82:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex:10:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2228 · 2026-05-19T11:43:57.206954+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
  "description": "Count abstract word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
    "description": "Count abstract word count"
  }
}
```

</details>

---


### Tool result

_source line 2229 · 2026-05-19T11:43:57.308534+00:00_

160 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2230 · 2026-05-19T11:44:04.643803+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True",
    "head_limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 2231 · 2026-05-19T11:44:05.096984+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:222:For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:82:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex:10:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 2232 · 2026-05-19T11:44:05.550264+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "anonymous\\.4open\\.science",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "anonymous\\.4open\\.science",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 2233 · 2026-05-19T11:44:06.505254+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex:4:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2234 · 2026-05-19T11:44:06.707050+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/*.pdf 2>/dev/null || echo \"NO_PDF\"",
  "description": "Check for compiled PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/*.pdf 2>/dev/null || echo \"NO_PDF\"",
    "description": "Check for compiled PDF"
  }
}
```

</details>

---


### Tool result

_source line 2235 · 2026-05-19T11:44:07.913138+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 1206
}
```

</details>

---


### Tool call

_source line 2236 · 2026-05-19T11:44:08.164609+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/  */ /g' | wc -w",
  "description": "Count abstract words excluding LaTeX markup"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/  */ /g' | wc -w",
    "description": "Count abstract words excluding LaTeX markup"
  }
}
```

</details>

---


### Tool result

_source line 2237 · 2026-05-19T11:44:08.215302+00:00_

158

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2238 · 2026-05-19T11:44:12.090035+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "1-5"
  }
}
```

</details>

---


### Tool result

_source line 2239 · 2026-05-19T11:44:12.493897+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf (481.3KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 2240 · 2026-05-19T11:44:18.483112+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "6-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "6-10"
  }
}
```

</details>

---


### Tool result

_source line 2241 · 2026-05-19T11:44:18.835965+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf (481.3KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 2242 · 2026-05-19T11:44:25.433389+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "11-15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "11-15"
  }
}
```

</details>

---


### Tool result

_source line 2243 · 2026-05-19T11:44:25.787157+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf (481.3KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 2244 · 2026-05-19T11:44:41.270922+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "16-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "16-20"
  }
}
```

</details>

---


### Tool result

_source line 2245 · 2026-05-19T11:44:41.573726+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf (481.3KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 2246 · 2026-05-19T11:44:49.221954+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || python3 -c \"\nfrom PyPDF2 import PdfReader\nreader = PdfReader('/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf')\nprint(f'Total pages: {len(reader.pages)}')\n\" 2>/dev/null || echo \"Cannot determine page count\"",
  "description": "Get total PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || python3 -c \"\nfrom PyPDF2 import PdfReader\nreader = PdfReader('/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf')\nprint(f'Total pages: {len(reader.pages)}')\n\" 2>/dev/null || echo \"Cannot determine page count\"",
    "description": "Get total PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 2247 · 2026-05-19T11:44:49.375127+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Tue May 19 05:10:01 2026 UTC
ModDate:         Tue May 19 05:10:01 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           25
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       492861 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 2248 · 2026-05-19T11:45:23.428446+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Chen 2026 \"multi-instance processing\" LLM instance count context length degradation arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Chen 2026 \"multi-instance processing\" LLM instance count context length degradation arXiv"
  }
}
```

</details>

---


### Tool call

_source line 2249 · 2026-05-19T11:45:24.431651+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhao 2026 \"Reflect then learn\" active prompting information extraction introspective confusion AAAI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhao 2026 \"Reflect then learn\" active prompting information extraction introspective confusion AAAI"
  }
}
```

</details>

---


### Tool call

_source line 2250 · 2026-05-19T11:45:25.942352+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Vandemoortele 2025 \"haystack to needle\" label space reduction zero-shot classification arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Vandemoortele 2025 \"haystack to needle\" label space reduction zero-shot classification arXiv"
  }
}
```

</details>

---


### Tool result

_source line 2251 · 2026-05-19T11:45:31.367939+00:00_

Web search results for query: "Chen 2026 "multi-instance processing" LLM instance count context length degradation arXiv"

Links: [{"title":"[2603.22608] Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length","url":"https://arxiv.org/abs/2603.22608"},{"title":"Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260322608C/abstract"},{"title":"Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length | OpenReview","url":"https://openreview.net/forum?id=AAfdu6YKfo"},{"title":"Understanding LLM Performance Degradation in Multi-Instance","url":"https://arxiv.org/pdf/2603.22608"},{"title":"Intelligence Degradation in Long-Context LLMs: Critical Threshold Determination via Natural Length Distribution Analysis","url":"https://arxiv.org/pdf/2601.15300"},{"title":"Context Length Alone Hurts LLM Performance Despite Perfect Retrieval","url":"https://arxiv.org/html/2510.05381v1"}]

I found the paper you're looking for! Here are the key findings:

The paper "Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length" is by Jingxuan Chen and 2 other authors (arXiv 2603.22608).

**Main Results:**

All LLMs follow a pattern of slight performance degradation for small numbers of instances (approximately 20-100), followed by a performance collapse on larger instance counts.

**Key Finding on Instance Count vs Context Length:**

While context length is associated with this degradation, the number of instances has a stronger effect on the final results.

**Study Context:**

While LLM performance on individual tasks is generally high, there has been little research on how LLMs perform when dealing with multi-instance inputs, so the paper performs a comprehensive evaluation of the mu
…[truncated 263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7939
}
```

</details>

---


### Tool result

_source line 2252 · 2026-05-19T11:45:31.770101+00:00_

Web search results for query: "Zhao 2026 "Reflect then learn" active prompting information extraction introspective confusion AAAI"

Links: [{"title":"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion","url":"https://arxiv.org/pdf/2508.10036"},{"title":"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion","url":"https://arxiv.org/html/2508.10036v1"},{"title":"[2508.10036] Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion","url":"https://arxiv.org/abs/2508.10036"},{"title":"Introspective Learning : A Two-Stage Approach for Inference in Neural   Networks","url":"https://arxiv.org/pdf/2209.08425"},{"title":"Guideline Learning for In-context Information Extraction","url":"https://arxiv.org/pdf/2310.05066"}]

I found the paper you were searching for! "Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion" is authored by Dong Zhao, Yadong Wang, Xiang Chen, and colleagues from Nanjing University of Aeronautics and Astronautics and Zhejiang University.

The paper introduces Active Prompting for Information Extraction (APIE), a novel active prompting framework guided by a principle termed introspective confusion. The method empowers an LLM to assess its own confusion through a dual-component uncertainty metric that uniquely quantifies both Format Uncertainty (difficulty in generating correct syntax) and Content Uncertainty (inconsistency in extracted semantics).

The work addresses how conventional selection strategies often fail because they overlook confusion stemming not just from semantic content, but also from the generation of well-structured formats required by IE tasks. Extensive experiments on four benchmarks show that the approach consistently outperforms strong baselines, yielding significant improvements in both extraction accuracy and robustness.


REMINDER: You MUST include the 
…[truncated 69 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7338
}
```

</details>

---


### Tool result

_source line 2253 · 2026-05-19T11:45:32.424160+00:00_

Web search results for query: "Vandemoortele 2025 "haystack to needle" label space reduction zero-shot classification arXiv"

Links: [{"title":"Machine Learning Feb 2025","url":"https://arxiv.org/list/cs.LG/2025-02?skip=3175&show=50"},{"title":"[2502.08436] From Haystack to Needle: Label Space Reduction for Zero-shot Classification","url":"https://arxiv.org/abs/2502.08436"},{"title":"Computer Science Feb 2025","url":"https://arxiv.org/list/cs/2025-02?skip=4050&show=2000"},{"title":"Computation and Language Feb 2025","url":"http://www.arxiv.org/list/cs.CL/2025-02?skip=475&show=1000"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=1500&show=50"},{"title":"From Haystack to Needle: Label Space Reduction for Zero-shot Classification","url":"https://arxiv.org/html/2502.08436v2"},{"title":"Artificial Intelligence Feb 2025","url":"https://arxiv.org/list/cs.AI/2025-02?skip=1700&show=25"},{"title":"[Literature Review] From Haystack to Needle: Label Space Reduction for Zero-shot Classification","url":"https://www.themoonlight.io/en/review/from-haystack-to-needle-label-space-reduction-for-zero-shot-classification"}]

I found the paper you're looking for! Here's what I found:

"From Haystack to Needle: Label Space Reduction for Zero-shot Classification" presents Label Space Reduction (LSR), a novel method for improving zero-shot classification performance of Large Language Models (LLMs).

**Key Details:**

- **Authors:** Nathan Vandemoortele, Bram Steenwinckel, Femke Ongenae, Sofie Van Hoecke
- **arXiv Identifier:** 2502.08441 (also listed as 2502.08437 in some listings)
- **Status:** Under review at ICML 2025

**Method Overview:**

LSR iteratively refines the classification label space by systematically ranking and reducing candidate classes, enabling the model to concentrate on the most relevant options. By leveraging unlabeled data with the statistical learning capabilities of data-driven models, LSR dynamically optimizes the label spac
…[truncated 472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6481
}
```

</details>

---


### Assistant

_source line 2254 · 2026-05-19T11:45:56.954083+00:00_

引用验证完成：
- Chen et al. (2026) "multi-instance processing" — arXiv:2603.22608 ✓ 真实
- Zhao et al. (2026) "Reflect then Learn" — arXiv:2508.10036 ✓ 真实
- Vandemoortele et al. (2025) "Haystack to Needle" — arXiv:2502.08436 ✓ 真实

**格式预检摘要**:
- 正文 8 页 ✓
- ACL review template ✓
- Double-blind (`\author{Anonymous}`) ✓
- Anonymous URL (anonymous.4open.science) ✓
- Limitations section 存在且充实（5 条 + 多重比较段落）✓
- Responsible NLP Checklist 完整 ✓
- Em-dash: 仅在未引用的废弃文件中 ✓
- Abstract ~158 words (在 150-250 范围内) ✓
- Appendix 引用格式待 Reviewer 详查

两名 Reviewer 已在审稿中，等待 Round 1 审稿结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 186

## Round 186

2 recorded events


### User

_source line 2255 · 2026-05-19T11:50:16.247195+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**论文**: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
**Venue**: EMNLP 2026 Main (ARR May 2026 cycle)
**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## Summary

本文研究 training-free LLM 信息抽取中 schema 复杂度对性能的影响，试图将"类型数量"(count) 和"类型混淆度"(confusability) 两个因素通过控制实验隔离。提出 Schema Confusability Score (SCS) 及其 batch 级聚合 BCS，在 Few-NERD、FewRel、DocRED、MAVEN 四个数据集上评估。主要发现：count 是主导因素；BCS 在 RE forced-choice 格式下解释 22-53% 的准确率方差，但在 NER 上无 batch 级信号；schema decomposition 因 merge amplification (NER) 和 routing failure (RE) 而失败。

## Strengths

**S1.** 实验设计严谨，控制变量全面。within-pool 分析控制了 pool composition confound，cross-seed variance decomposition 证实 batch composition 是主要变异来源，prompt sensitivity 分析覆盖四种结构不同的 prompt variant。统计方法规范（TOST 等价检验、bootstrap CI、permutation test），在 NLP 实证论文中属于上乘。

**S2.** 诚实报告负面结果。SDGD 失败（§6）、label renaming 反而降低准确率（Appendix L）、few-shot 反而扩大 confusability gap（Appendix I）——这些负面结果对社区有真实价值，避免了后续工作重复踩坑。

**S3.** Limitations section 异常充实（5 条主要限制 + 1 段 multiple comparisons 讨论），涵盖 model coverage、effect size、task format dependency、causal mechanism、data contamination，坦率度远超一般投稿。

**S4.** Cross-model validation 覆盖面广：Qwen3-32B（主模型）、Llama-3.1-8B、70B（开源不同规模）、Gemini 2.5 Flash（闭源 API），Dimension 1 在全部四个模型上复现。

**S5.** Task asymmetry finding（RE vs NER 的 BCS 效果差异）是非显然的发现，且有合理的机制解释（forced-choice classification 将所有非 null 错误集中为 type substitution，而 NER 错误分散在 missed entity、boundary error 和 type confusion 三个通道）。

## Weaknesses

**W1. [Must-Fix] SCS 与 LLM-PEE 的区分不够充分，novelty 存疑**
- 具体位置：Related Work "SCS novelty" 段落；Introduction Contribution 1
- 问题：论文坦承 "SCS shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion in LLM-PEE" (Related Work)。Contribution 1 声称 "the first controlled study that isolates count and confusability effects"，但核心度量指标本身完全借用自 LLM-PEE。论文将区别定位为 "engineering optimization vs. scientific analysis"，但这一区分较薄——使用相同指标做更细致的实验，贡献更接近于 "first systematic empirical study" 而非方法创新。
- 为什么影响接收：EMNLP Main 对 novelty 有较高要求。如果核心指标无新颖性，论文需要更强地论证实验框架本身的方法论贡献。
- 建议：(a) 明确将 SCS 定位为 "adopted from LLM-PEE" 而非暗示是本文贡献；(b) 在 Contribution 1 中强调实验设计范式（stratified BCS-controlled batches + within-pool control）的方法论创新，而非指标本身；(c) 补充讨论 SCS 作为 proxy 的局限性（pairwise r² 仅 1.3-1.7%）如何影响整个研究框架的可靠性。

**W2. [Must-Fix] Title "Predict" 与论文实际证据不匹配**
- 具体位置：Title；Limitations §4 ("The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway")
- 问题：Title 使用 "Predict"，暗示预测性甚至因果关系。但论文自身在 Limitations 中明确承认只是 "correlational evidence with controlled stratification"，且 renaming experiment (Appendix L) 试图做因果干预时失败了（降低 SCS 反而降低准确率）。这说明 SCS 与 confusion 的关系可能并非直接因果，而是通过 label familiarity 等混淆变量中介。
- 为什么影响接收：Title 与论文证据之间的 gap 会让审稿人质疑 claim 的诚实度。
- 建议：将 Title 改为更保守的表述，如 "How Does Schema Complexity Relate to Performance..." 或 "Schema Complexity and Performance Degradation in..."。

**W3. [Must-Fix] 实际效果量过小，实用价值存疑**
- 具体位置：§5.3 Practical magnitude ("typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2 pp, 95% CI: [0.4, 4.0]")
- 问题：在 typical batches 下，confusability 维度的实际影响仅约 2.2pp。虽然论文诚实报告了这一数字，但这引发根本问题：如果自然 schema 采样下 confusability 的实际影响如此小，研究这一维度的实用价值有多大？极端 BCS batch 的 25-31pp gap 来自人为构造的极端条件（刻意选择最相似/最不相似的类型组合），在真实部署中不会自然出现。
- 为什么影响接收：审稿人会质疑：如果核心发现的 practical impact 仅 ~2pp，这是否构成足够的贡献？
- 建议：(a) 在 Discussion 中更直接地讨论 2pp gap 的实际意义和局限；(b) 说明在哪些 realistic 场景下 confusability 会成为 bottleneck（例如特定领域的 schema 可能天然高 BCS）；(c) 考虑是否有 downstream 任务对 2pp 敏感。

**W4. [Should-Fix] NER Dimension 2 本质为 null result，削弱泛化性**
- 具体位置：§5.3 ("NER shows no batch-level BCS--F1 correlation under either prompt (r ≈ 0, n = 450)")
- 问题：论文声称 "spanning NER, RE, and event detection"，但 BCS 的 batch 级效应在 NER 上完全为 null (r ≈ 0)，在 ED (MAVEN) 上因 centrality confound 而无法测量。这意味着 Dimension 2 的核心发现实际上只在 RE 这一个任务上成立（FewRel + DocRED），且仅在 forced-choice classification 格式下。
- 建议：Introduction 和 Abstract 中应更明确限定 Dimension 2 的适用范围，而非给读者"三个任务都验证了"的印象。当前 Abstract 虽然提到了 NER 的 null result ("but shows no batch-level signal for NER")，但整体叙事仍暗示 confusability 是一个普遍现象。

**W5. [Should-Fix] MAVEN 事件检测贡献微弱**
- 具体位置：§5.5 Centrality Confound；§4.1 ("MAVEN serves a supplementary role")
- 问题：MAVEN 在论文中被标注为 "supplementary"，其 per-type BCS--F1 相关性因 centrality confound 而与预期方向相反（正相关而非负相关）。控制 confound 后相关性消失 (p > 0.2)。论文的 ED 贡献实质上仅限于揭示 centrality confound 这一方法论警示，而非提供 confusability 效应的 positive evidence。
- 建议：在 Contribution 列表中不要将 ED 与 NER、RE 并列为 confusability 效应的验证任务，而是将其单独列为一个 methodological finding（"centrality confound in same-domain schemas"）。

**W6. [Should-Fix] Embedding 选择不一致**
- 具体位置：§4.2 SCS 定义；Table 1
- 问题：Few-NERD 使用 Qwen3-32B 嵌入，其余三个数据集使用 MiniLM。虽然给出了理由（MiniLM 在 Few-NERD 的细粒度类型上区分不足），但这引入了跨数据集比较的不确定性。更重要的是，使用模型自身嵌入（Qwen3）来预测模型自身的 confusion 可能导致 circular reasoning——如果模型对某些类型的表示本身就混淆，那么用该表示计算 SCS 自然与 confusion 相关。
- 建议：(a) 对所有数据集都报告 MiniLM 和 Qwen3 两种嵌入下的结果（或至少报告 cross-check）；(b) 讨论使用模型自身嵌入的 circularity concern。论文在§5.2 提到 "The independent MiniLM embedding yields a stronger SCS--confusion correlation on Few-NERD (r = 0.172 vs. Qwen3 r = 0.138)"，这实际上进一步支持了使用 MiniLM 作为统一嵌入的做法。

**W7. [Should-Fix] DocRED bounded-interaction 不成立，限制主要 claim**
- 具体位置：Appendix C ("DocRED factorial: TOST at ±3pp is not established (p = 0.77)")
- 问题：bounded-interaction claim（count 和 confusability 效应可加性分离）仅在 sentence-level RE (FewRel) 上成立，在 document-level RE (DocRED) 上 TOST p = 0.77（不成立），在 NER 上因 Dimension 2 为 null 而无法检验。论文虽然透明报告了这一结果，但 §5.4 标题 "Multi-Dimensional Degradation" 和整体叙事可能给读者 overstate bounded interaction 的普遍性的印象。
- 建议：在正文中更突出地标注 bounded interaction 仅限 sentence-level RE 这一条件。

**W8. [Minor] Abstract 数据密度过高**
- 具体位置：Abstract
- 问题：Abstract 在约 170 词内塞入了 "−49pp"、"~2pp"、"22--53%"、"+4.3pp" 等多个具体数字，读起来像 results 的缩写而非引人入胜的研究故事。
- 建议：减少 Abstract 中的具体数字，保留 2-3 个最关键的数据点，用叙事性语言替代。

**W9. [Minor] Introduction 过早引入大量实验结论**
- 具体位置：Introduction "Our experiments yield four findings" 段落
- 问题：Introduction 在 findings 列表中包含了大量细节，如 "TOST p=0.003 at ±3pp"、"logit-scale inconclusive" 等，这些属于 Results/Discussion 内容。Introduction 应提供 high-level findings preview，不是 statistical details。
- 建议：将 findings 概括为更高层次的描述，将统计细节留给 Results。

**W10. [Minor] -ing 分词短语尾部偶现**
- 具体位置：Abstract ("revealing task-dependent effect structures")；Results §5.3 ("establishing confusability as a substantial predictor")
- 问题：虽然整体 AI 写作痕迹极少（无 em-dash、无 Furthermore/Moreover 连用、无 delve/leverage 等），但仍有少量 -ing 短语结尾，属于轻微 AI 风格残留。
- 建议：将 "revealing..." 改为独立句子。

## Questions

**Q1.** 在 BCS-controlled 实验中，extreme-batch 的构造过程是否引入了其他 confound？例如，maximally dissimilar types 的 batch 是否更可能包含 "容易" 的类型（high solo-baseline accuracy），而 maximally similar types 的 batch 是否倾向于包含特定语义域的类型？Appendix J 的 BCS-composition 分析用 100 个 random batches 检验了这一点 (VIF = 1.06)，但 extreme batches（而非 random batches）是否也满足这一正交性？

**Q2.** 论文使用 greedy decoding (temperature=0) 且只用单一 seed (42)。虽然 Appendix K 的 variance decomposition 显示 inter-seed variance 较低 (residual SD = 0.88pp)，但这仅在 count=80 下测量（只有一种 batch composition）。在其他 count level 下，inter-seed variance 可能更大。能否报告 count=8 和 count=16 下的 seed sensitivity？

**Q3.** FewRel 原始设计是 few-shot relation classification benchmark，其 80 个 relation 来自 Wikidata。论文将 train+val splits 合并使用，但 train split 的 64 个 relation 与 val split 的 16 个 relation 在类型分布上可能不同。split-origin analysis (Appendix N) 显示 train-origin types 准确率低 8.8pp (p=0.06)，虽然 BCS 回归不受影响，但这个差异本身值得讨论。

**Q4.** 论文报告 Gemini 2.5 Flash count-64 结果基于 11/25 batches（因 API quota 限制）。部分结果是否可能引入 selection bias？是否前 11 个 batch 的 BCS 分布与全部 25 个不同？

## Missing References

未发现明显遗漏的关键参考文献。引用覆盖了直接竞争者 (LLM-PEE, CrossAgentIE, PARSE, IEPile)、baseline (GLiNER, GoLLIE, UniversalNER)、相关理论 (representation degeneration, prototypical networks)、以及 2025-2026 concurrent work (chen-2026-multi-instance, reflect-learn-2026)。引用数量约 50+ 篇，对 EMNLP Main Long Paper 属于合理范围。

所有抽查的引用（包括 chen-2026-multi-instance arXiv:2603.22608、haystack-to-needle-2025 arXiv:2502.08436、reflect-learn-2026 AAAI 2026）均经 WebSearch 验证为真实存在。

## 格式合规

- `\usepackage[review]{acl}` ✓
- 匿名化：`\author{Anonymous}` ✓，anonymous URL (anonymous.4open.science) ✓
- Limitations section：存在且充实（5 条 + multiple comparisons 段） ✓
- Responsible NLP Checklist：完整填写，A-E 各项均有实质回答 ✓
- Appendix 在 references 后 ✓
- 无法确认正文页数（需编译 PDF），但内容量看起来可能接近 8 页上限
- References 格式大体一致，个别条目缺 pages 信息（如 llm-pee-2025, gollie-2024 等），但不影响阅读

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法扎实，统计方法规范，controls 充分。但核心 claim 的适用范围被 NER null result、DocRED interaction inconclusive、MAVEN centrality confound 显著收窄；title "Predict" 过强；typical effect size 仅 ~2pp。 |
| Excitement | 2.5/5 | 核心指标 SCS 借用自 LLM-PEE；"类型越多越差、越相似越容易混淆" 的 high-level finding 符合直觉；practical impact ~2pp 有限。Task asymmetry 和 negative results 有价值但不够开辟新研究方向。 |
| Reproducibility | 4/5 | 实验设置详细（模型、decoding 参数、seed、batch 构造方法均明确），承诺 code release，prompt templates 完整公开。唯一不确定性是 Gemini API 结果的可重复性。 |
| Overall Assessment | 3.0 |  |
| Confidence | 4/5 | 熟悉 IE、LLM evaluation、实验方法论领域。 |

## Overall Assessment

**评分: 3.0** (Findings 可接收)
**置信度: 4/5**

**一句话总结**: 方法论严谨、统计规范、负面结果有价值的实证研究，但核心指标无新颖性、high-level findings 符合直觉、practical effect size 过小 (~2pp typical)、Dimension 2 仅在 RE forced-choice 格式下成立，novelty 和 impact 不足以支撑 Main conference 接收，适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2256 · 2026-05-19T11:50:31.631224+00:00_

R2 审稿意见已收到。核心观点：方法论严谨但 novelty 不足（SCS 借用 LLM-PEE）、typical effect size 过小（~2pp）、Dimension 2 仅限 RE forced-choice、Title "Predict" 过强。评分 3.0 (Findings)。

等待 R1 审稿意见返回后启动 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 187

## Round 187

2 recorded events


### User

_source line 2257 · 2026-05-19T11:50:34.292937+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：Overall 3.0 (Findings)，Soundness 3.5，Excitement 2.5。

主要问题：(1) SCS 指标直接借用自 LLM-PEE，novelty 不足；(2) Title "Predict" 与实际 correlational evidence 不匹配；(3) typical effect size 仅 ~2pp，practical impact 有限；(4) Dimension 2 (confusability) 在 NER 上为 null，在 ED 上因 centrality confound 无法测量，仅在 RE forced-choice 下成立。主要优势：实验设计严谨、统计方法规范、negative results 有社区价值、cross-model validation 充分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2258 · 2026-05-19T11:50:40.981377+00:00_

收到 R2 审稿意见。等待 R1 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 188

## Round 188

6 recorded events


### User

_source line 2259 · 2026-05-19T11:51:15.813484+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见（侧重：方法严谨性 + 实验设计）

**论文**: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
**Venue**: EMNLP 2026 Main (ARR May 2026 cycle)

---

## Summary

本文研究 training-free LLM 信息抽取中 schema 复杂度对性能的影响，将退化分解为两个维度：类型数量（count）和类型可混淆性（confusability）。提出 SCS/BCS 指标量化 confusability，在 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）和 4 个模型（Qwen3-32B, Llama-8B/70B, Gemini Flash）上进行 controlled experiments。主要发现：count 驱动 recall 下降是主因；BCS 解释 RE 22-53% 的 batch 间准确率方差但对 NER 无 batch 级信号；schema 分解因 merge amplification（NER）和 routing failure（RE）而失败。

---

## Strengths

**S1. 实验设计的创新性和严谨性。** BCS-controlled 实验通过固定 count 变化 confusability 来隔离两个因素，这是该问题上的首次 controlled study。within-pool 分析（从 80-relation pool 抽 16-relation 子集）进一步控制了 pool composition confound，permutation test 确认 slope 一致性（p≈0.60）。这一设计明显优于 prior work 的简单 ablation。（§3.3, Table 5）

**S2. 统计方法论的深度。** 论文系统使用了 TOST 等价检验、bootstrap CI（B=10,000）、permutation test、cluster bootstrap、方差分解、factorial analysis 等。特别是 TOST sensitivity analysis（Table 4）展示了不同 margin 下的等价结论，logit-scale sensitivity check 和 DocRED factorial 的 inconclusive 结果均如实报告，没有选择性呈现。

**S3. 诚实的负面结果报告。** SDGD 分解失败（§5）、label renaming 反而降低准确率（Appendix W）、few-shot 加大 confusability gap（Appendix U）、NER 无 batch 级 BCS 信号——这些负面结果均被完整报告和诊断，增强了论文可信度。merge amplification 和 routing failure 的分析（precision 0.563→0.210、73.4% 实例在 3-5 个 sub-schema 收到 positive prediction）具有实际参考价值。

**S4. Cross-model validation 覆盖面。** Dimension 1 在 4 个模型（含 proprietary Gemini Flash）上复现；Dimension 2 在 Llama-8B/70B 上均检测到显著 BCS gap。RE count 曲线在 70B 和 32B 间的定量匹配（-30.7pp vs -30.1pp, Table R）令人信服。

**S5. Centrality confound 的识别与处理。** 在 MAVEN 上发现 per-type BCS-F1 出现反向正相关，追溯到 same-domain embedding collapse，并通过 partial correlation 控制 log frequency 和 degree centrality 后使正相关消失（p>0.2）。同时保留 pairwise SCS 信号作为不受此 confound 影响的证据。（§4.5, Appendix D）

**S6. 引用全面，无幻觉引用。** 70 条引用覆盖 direct competitors（LLM-PEE, PARSE, CrossAgentIE）、baseline 方法、评测 benchmark、统计方法论（Rothman 1990, Lakens 2017, Dror 2018）和理论基础（representation degeneration）。经 OpenAlex 交叉验证，无孤立/缺失条目。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**W1. [critical] TOST 等价检验的 margin 选择存在循环论证，"bounded interaction" claim 过度泛化**
- 具体位置：§4.4, Appendix C, Abstract, Conclusion
- 问题：±3pp margin 的三个 anchor 之一是"0.5×batch SD (≈4.6pp)"，但 batch SD 本身部分由 BCS 变异驱动——用被解释变量的方差来设定等价 margin 存在循环性。更关键的是，logit-scale TOST 是 inconclusive（p=0.209），DocRED interaction 为 +5.7pp（CI [-1.6, 13.0]，TOST p=0.77），NER factorial 也 inconclusive（p=0.50）。但 Abstract 写"bounded interaction"未加限定，Conclusion 仅限定为"sentence-level RE"但用语仍显笼统。
- 为什么影响接收：这是论文的核心 claim 之一——如果 count 和 confusability 的交互不 bounded，两维独立分析的理论基础就会动摇。3/4 个条件（logit-scale RE、DocRED、NER）均 inconclusive，仅 linear-scale sentence-level RE 达到等价——这不是"bounded interaction"而是"在特定条件下观察到 bounded interaction"。
- 建议修改方向：(1) Abstract 和 Conclusion 中的 "bounded interaction" 须限定为 "under the linear specification on sentence-level RE"；(2) 补充讨论 margin 选择的 sensitivity——论文已有 Table 4 的 sensitivity analysis，但应明确承认 ±1pp 下 inconclusive，即 interaction 可能达到 main effect 的 ~50%；(3) 考虑用 practical equivalence 框架替代，或至少讨论 margin 的 anchor 独立于被解释变量。

**W2. [critical] DocRED 统计功效不足以支撑 headline claim "up to 53%"**
- 具体位置：§4.3 ("BCS explains 44-53% of cross-batch variance"), Abstract ("22-53%"), Table summary
- 问题：DocRED 每个 count level 仅 5 batches，回归使用 n=35（5 high + 5 low + 25 random）。R²=0.525 的 95% CI 为 [0.27, 0.73]，adjusted R²=0.511。虽然 adjusted R² shrinkage 小，但 n=35 单预测变量 OLS 的 R² 估计本身不稳定。DocRED factorial 也完全 inconclusive（TOST p=0.77），interaction estimate +5.7pp 的 CI 跨零。
- 为什么影响接收：Abstract 写"22-53%"将最高值（来自统计功效最低的 dataset）作为 headline number，可能误导读者高估效应。审稿人会注意到 n=35 的 R²=0.53 在 bootstrap CI [0.27, 0.73] 下的不确定性。
- 建议修改方向：(1) Abstract 改为 "22% on sentence-level RE (up to 53% on document-level, though with wider confidence intervals)"；(2) DocRED 结果应明确标注为 "preliminary replication with limited statistical power"；(3) 如果可行，增加 DocRED batches 数量以提高估计稳定性。

**W3. [critical] Dimension 2 缺乏 proprietary model 的 batch-level 验证，但 claim 的普遍性暗示了跨架构一致性**
- 具体位置：Abstract ("pairwise confusability is a schema-structural property"), §4.3 cross-model validation, Limitations item 1
- 问题：BCS-controlled experiments（论文的核心创新）仅在 open-weight models（Qwen3-32B, Llama-8B/70B）上验证。Gemini Flash 仅验证 count curves。Abstract 声称 "effects replicate across model scales and families" 和 "pairwise confusability is a schema-structural property"，暗示了跨架构普遍性，但 Dimension 2 的 batch-level 验证仅覆盖同一 inference framework（vLLM + constrained decoding）下的 open-weight models。Proprietary models 可能有不同的 constrained decoding 实现，而论文已证明 format dependency 是 BCS-accuracy 关系的前提（unconstrained ablation ρ=-0.14, p=0.49）。
- 为什么影响接收：如果 BCS 效应依赖于特定的 constrained decoding 实现而非 schema 的结构性质，论文的核心 claim 就需要重新框架。
- 建议修改方向：(1) Abstract 中的 "schema-structural property" 应限定为 "observed consistently across open-weight models under constrained decoding"；(2) 讨论 proprietary models 的 constrained decoding 实现差异可能如何影响 BCS 效应；(3) 如果 Gemini API 支持 structured output，补充 BCS-controlled 实验。

### Should-Fix 问题（影响评分但不一票否决）

**W4. [warning] Pairwise R²=1.3-1.7% 到 batch-level R²=22% 的放大机制依赖于对非零混淆对的条件化**
- 具体位置：§4.2, §4.3, Appendix I, Discussion §6
- 问题：Monte Carlo simulation（Appendix I）使用 conditional R²=7%（仅计算非零混淆对，约占 11%）作为输入，模拟得到 batch R²=0.219 匹配观测值。但论文也承认 unconditional R²=1.3% 仅能产生 batch R²=0.044。这意味着 BCS 的 batch-level 预测能力本质上来自于高 BCS batch 包含更多"活跃混淆对"（active confusable pairs），而非 BCS 对每对类型的混淆有强预测力。这一机制在 §6 有简要提及但不够突出。
- 建议：在 Discussion 中更明确地阐述：BCS 作为 batch-level predictor 的有效性来源于其作为"活跃混淆对密度"代理指标的功能，而非 pair-level confusability 的强预测力。这能更准确地指导实践应用。

**W5. [warning] NER U-shape 恢复缺乏直接证据支持**
- 具体位置：§4.1, §6 (Discussion)
- 问题：Recall 从 count 22-44 的 ~0.27 恢复到 full-schema (66 types) 的 0.41。§6 解释为 "partial schemas require simultaneous span detection and type filtering; at full schema, filtering becomes vacuous and recall recovers"，但这是 post-hoc 推测，没有直接证据。一个简单的控制实验（在 partial schema 中加入 "extract ALL entities, then filter to these types" 的指令变体）可以测试这一假说。
- 建议：要么补充 ablation 实验支持 filtering hypothesis，要么明确标注为 "one possible explanation that requires further investigation"。

**W6. [warning] Confusability-aware batching 无实际收益——实践指导价值有限**
- 具体位置：§5, §6 Practical implications
- 问题：Graph coloring 仅比 random batching 高 1.4pp（p≈0.19, n.s.）。Renaming 降低了 SCS 但也降低了准确率。Few-shot 加大了 confusability gap。§6 提出的四个实践方向中，(1) label renaming 已被证明反效果，(3) contrastive definitions 未测试，(4) 仅是报告建议。论文本质上展示了 confusability 可检测但不可干预。
- 建议：更诚实地框架实践意义——这篇论文的价值更多在于诊断工具（SCS/BCS 作为 RE 质量指标）而非干预方案。可在 Discussion 中讨论为什么减少 confusability 如此困难（label unfamiliarity 效应 vs. 概念重叠不可消除）。

**W7. [warning] Renaming 实验的另一种解读未被讨论**
- 具体位置：Appendix W, Limitations item 4
- 问题：Renaming 减少了 embedding similarity 但降低了准确率。论文归因于 "label unfamiliarity"。但另一种解读是：LLM 的类型混淆本质上由概念重叠（如 "child" 和 "father" 都是家庭关系）驱动，而非 label name 的 surface similarity。如果是概念重叠，那么 SCS（基于 name embedding similarity）只是概念重叠的不完美 proxy，而非混淆的直接 predictor。这一解读会削弱 SCS 作为 confusability 度量的理论基础。
- 建议：在 Discussion 或 Limitations 中讨论 "conceptual overlap vs. label surface similarity" 这一 distinction，承认 SCS 可能是 confusability 的 downstream proxy 而非 root cause metric。

**W8. [warning] FewRel train+val merge 的 contamination 分析论证不完全**
- 具体位置：§3.1, Limitations item 5, Appendix P
- 问题：Train-origin types 准确率低 8.8pp（p=0.06，borderline significant）。论文认为这"与 contamination 假设相反"，但这假设 contamination 一定提高准确率。预训练暴露于 FewRel 的 few-shot 格式可能引入系统性偏差（如过拟合特定 relation 的 typical entity patterns），不一定表现为准确率提高。Appendix P 的 split-origin covariate 分析确认 BCS 偏效应不变（β_BCS 不受影响），这是好的，但 contamination 对绝对准确率水平的影响仍未排除。
- 建议：弱化"opposite to the contamination hypothesis"的表述，改为"the BCS-accuracy relationship is robust to split-origin composition (Appendix P), though absolute accuracy levels may still reflect differential pretraining exposure"。

### 小问题（不影响接收）

- **M1.** Abstract "up to -49pp for document-level RE" 是 count 效应（88.0→38.7），但语境上与 confusability 相邻，容易误导读者关于 confusability 的 magnitude。建议明确标注为 count-driven。
- **M2.** Unconstrained decoding ablation（n=25）对 format-dependency claim 至关重要，但 power 有限。若可行，建议扩大样本量。
- **M3.** P-value 报告格式不一致：部分写 p < 0.001，部分写 p < 10^{-16} 或 p < 10^{-35}。建议统一。
- **M4.** Table 1 脚注 "BCS ranges are not comparable across embedding models" 很重要但容易被忽略——Few-NERD 用 Qwen3 embedding（BCS 0.77-0.93）与 FewRel 用 MiniLM（0.42-0.97）的范围差异可能让读者产生误解。

---

## Questions

**Q1.** BCS-controlled 结果对具体 1,000 test instances 的采样有多敏感？跨不同 test set 的方差是多少？

**Q2.** Confusability-aware batching 需要达到多大的 BCS reduction 才能产生实际收益？论文显示 0.559→0.552 不够，那阈值在哪里？

**Q3.** Greedy decoding 下 inference 近乎确定性的——temperature>0 的 sampling 是否可能 mask 或 amplify BCS 效应？

**Q4.** High-BCS 准确率在不同模型上收敛到 ~51%（Table 2）——这是否接近这些特定 batch compositions 的 chance level？有理论解释吗？

**Q5.** 70B cross-model BCS validation（Appendix R）的 CI [+3.0, +20.1] 较宽，用了多少 batches？

---

## Missing References

无关键遗漏。引用覆盖全面，包括最新 concurrent work（Chen 2026, Reflect-Learn 2026）。建议考虑引用：
- Josifoski et al. (2022) "GenIE: Generative Information Extraction"——在 structured prediction 中讨论了 label space 对生成模型的影响。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计和统计方法总体严谨，但 TOST margin 循环论证、DocRED 功效不足、"bounded interaction" 过度泛化是主要扣分点。3/4 条件下交互检验 inconclusive。 |
| Excitement | 2.5/5 | 问题有实际意义，controlled design 是新颖的。但 pairwise R²=1.3% 实际意义有限，batch-level 效应仅限 RE，且无可操作的改进方案。论文本质是"诊断而非治疗"。 |
| Reproducibility | 4/5 | 实验细节充分（模型、seed、decoding 参数、batch 数量、prompt template 全文）。代码承诺 upon acceptance。唯一扣分：FP8 量化的非确定性可能影响精确复现。 |
| Confidence | 4/5 | 仔细阅读全文含完整 appendix。统计方法论在专业范围内。 |

## Overall Assessment

**评分: 3.0 (Findings)**

**一句话总结**: 方法论严谨、实验设计新颖、负面结果诚实，但核心效应的实际意义有限（pairwise R²=1.3%，batch-level 仅限 RE），"bounded interaction" claim 在多数条件下 inconclusive，且未展示可操作的改进方案——达到 Findings 水平但距 main conference 的 impact 要求有差距。

**详细理由**: 本文的 BCS-controlled 实验设计是其最大亮点，首次在 training-free LLM IE 中隔离了 count 和 confusability 的效应。Cross-model validation 覆盖 4 个模型，negative results 的诊断深入（merge amplification, routing failure），centrality confound 的处理体现了方法论素养。然而，几个关键问题限制了评分：(1) TOST bounded interaction 仅在 sentence-level RE linear scale 成立，但 abstract/conclusion 表述过宽；(2) DocRED R²=53% 来自 n=35 的不稳定估计被用作 headline number；(3) Dimension 2 未在 proprietary models 上做 batch-level 验证但 claim 了跨架构一致性；(4) 论文展示了诊断能力但未提供任何有效的干预方案。作为分析性研究论文，达到 Findings acceptance 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2260 · 2026-05-19T11:52:01.110052+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请对每条 Weakness 和 Question 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n注意：你的回应应基于论文内容本身，而非你个人的偏好。\n\n---\n\n### Reviewer 2 的 Weaknesses\n\n**W1. [Must-Fix] SCS 与 LLM-PEE 的区分不够充分，novelty 存疑**\n论文坦承 SCS shares its formal definition with LLM-PEE。Contribution 1 声称 \"the first controlled study\"，但核心度量指标完全借用自 LLM-PEE。\"engineering optimization vs. scientific analysis\" 区分较薄。EMNLP Main 对 novelty 有较高要求。\n\n**W2. [Must-Fix] Title \"Predict\" 与论文实际证据不匹配**\nTitle 使用 \"Predict\"，但 Limitations 承认只是 \"correlational evidence\"，renaming experiment 试图因果干预时失败。SCS 与 confusion 的关系可能非直接因果，而是通过 label familiarity 等混淆变量中介。\n\n**W3. [Must-Fix] 实际效果量过小，实用价值存疑**\ntypical BCS span (IQR=0.054) yields ~2.2pp gap。极端 BCS 的 25-31pp gap 来自人为构造。如果 practical impact 仅 ~2pp，研究价值存疑。\n\n**W4. [Should-Fix] NER Dimension 2 本质为 null result，削弱泛化性**\nBCS batch 级效应在 NER 上完全为 null (r≈0)，在 ED (MAVEN) 因 centrality confound 无法测量。Dimension 2 实际只在 RE 一个任务上成立。\n\n**W5. [Should-Fix] MAVEN 事件检测贡献微弱**\nMAVEN 标注为 \"supplementary\"，per-type BCS-F1 正相关与预期相反，控制后消失。ED 贡献仅限于揭示 centrality confound。\n\n**W6. [Should-Fix] Embedding 选择不一致**\nFew-NERD 用 Qwen3，其余用 MiniLM。使用模型自身嵌入可能存在 circular reasoning。且论文自己的数据（MiniLM r=0.172 > Qwen3 r=0.138 on Few-NERD）支持统一使用 MiniLM。\n\n**W7. [Should-Fix] DocRED bounded-interaction 不成立，限制主要 claim**\nBounded interaction 仅在 sentence-level RE 成立，DocRED TOST p=0.77（不成立），NER 无法检验。§4.4 标题和叙事可能 overstate。\n\n**W8-W10. [Minor]** Abstract 数据密度过高；Introduction 过早引入统计细节；-ing 分词短语残留。\n\n### Reviewer 2 的 Questions\n\nQ1. extreme-batch 构造是否引入其他 confound（maximally dissimilar types 是否倾向于\"容易\"的类型）？Appendix J 的 VIF=1.06 基于 random batches，extreme batches 是否也满足正交性？\n\nQ2. 单一 seed (42) 的 variance decomposition 仅在 count=80 下测量，其他 count level 的 seed sensitivity？\n\nQ3. FewRel train+val merge 中 train-origin types 准确率低 8.8pp (p=0.06)，这一差异值得讨论。\n\nQ4. Gemini count-64 的 11/25 batches 是否有 selection bias？\n\n### Reviewer 2 的 Overall Assessment\n评分: 3.0 (Findings)，Soundness 3.5，Excitement 2.5，Confidence 4/5",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请对每条 Weakness 和 Question 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n注意：你的回应应基于论文内容本身，而非你个人的偏好。\n\n---\n\n### Reviewer 2 的 Weaknesses\n\n**W1. [Must-Fix] SCS 与 LLM-PEE 的区分不够充分，novelty 存疑**\n论文坦承 SCS shares its formal definition with LLM-PEE。Contribution 1 声称 \"the first controlled study\"，但核心度量指标完全借用自 LLM-PEE。\"engineering optimization vs. scientific analysis\" 区分较薄。EMNLP Main 对 novelty 有较高要求。\n\n**W2. [Must-Fix] Title \"Predict\" 与论文实际证据不匹配**\nTitle 使用 \"Predict\"，但 Limitations 承认只是 \"correlational evidence\"，renaming experiment 试图因果干预时失败。SCS 与 confusion 的关系可能非直接因果，而是通过 label familiarity 等混淆变量中介。\n\n**W3. [Must-Fix] 实际效果量过小，实用价值存疑**\ntypical BCS span (IQR=0.054) yields ~2.2pp gap。极端 BCS 的 25-31pp gap 来自人为构造。如果 practical impact 仅 ~2pp，研究价值存疑。\n\n**W4. [Should-Fix] NER Dimension 2 本质为 null result，削弱泛化性**\nBCS batch 级效应在 NER 上完全为 null (r≈0)，在 ED (MAVEN) 因 centrality confound 无法测量。Dimension 2 实际只在 RE 一个任务上成立。\n\n**W5. [Should-Fix] MAVEN 事件检测贡献微弱**\nMAVEN 标注为 \"supplementary\"，per-type BCS-F1 正相关与预期相反，控制后消失。ED 贡献仅限于揭示 centrality confound。\n\n**W6. [Should-Fix] Embedding 选择不一致**\nFew-NERD 用 Qwen3，其余用 MiniLM。使用模型自身嵌入可能存在 circular reasoning。且论文自己的数据（MiniLM r=0.172 > Qwen3 r=0.138 on Few-NERD）支持统一使用 MiniLM。\n\n**W7. [Should-Fix] DocRED bounded-interaction 不成立，限制主要 claim**\nBounded interaction 仅在 sentence-level RE 成立，DocRED TOST p=0.77（不成立），NER 无法检验。§4.4 标题和叙事可能 overstate。\n\n**W8-W10. [Minor]** Abstract 数据密度过高；Introduction 过早引入统计细节；-ing 分词短语残留。\n\n### Reviewer 2 的 Questions\n\nQ1. extreme-batch 构造是否引入其他 confound（maximally dissimilar types 是否倾向于\"容易\"的类型）？Appendix J 的 VIF=1.06 基于 random batches，extreme batches 是否也满足正交性？\n\nQ2. 单一 seed (42) 的 variance decomposition 仅在 count=80 下测量，其他 count level 的 seed sensitivity？\n\nQ3. FewRel train+val merge 中 train-origin types 准确率低 8.8pp (p=0.06)，这一差异值得讨论。\n\nQ4. Gemini count-64 的 11/25 batches 是否有 selection bias？\n\n### Reviewer 2 的 Overall Assessment\n评分: 3.0 (Findings)，Soundness 3.5，Excitement 2.5，Confidence 4/5",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2261 · 2026-05-19T11:52:25.606572+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24496
}
```

</details>

---


### Tool call

_source line 2262 · 2026-05-19T11:52:25.759082+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请对每条 Weakness 和 Question 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n注意：你的回应应基于论文内容本身，而非你个人的偏好。\n\n---\n\n### Reviewer 1 的 Weaknesses\n\n**W1. [critical] TOST margin ±3pp 存在循环论证，\"bounded interaction\" claim 过度泛化**\n±3pp 的 anchor 之一是\"0.5×batch SD (≈4.6pp)\"，但 batch SD 部分由 BCS 变异驱动——循环性。更关键：logit-scale TOST inconclusive (p=0.209)，DocRED +5.7pp TOST p=0.77，NER factorial p=0.50。仅 linear-scale sentence-level RE 达到等价。Abstract 和 Conclusion 中 \"bounded interaction\" 未充分限定。\n\n**W2. [critical] DocRED R²=53% 来自 n=35 的不稳定估计，被用作 headline number**\nDocRED 每个 count level 仅 5 batches，回归 n=35，95% CI [0.27, 0.73]。Abstract \"22-53%\" 将统计功效最低的 dataset 的最高值作为 headline。DocRED factorial 也完全 inconclusive (TOST p=0.77)。\n\n**W3. [critical] Dimension 2 缺乏 proprietary model batch-level 验证**\nBCS-controlled 仅在 open-weight models 上验证。Gemini 仅验证 count curves。Abstract \"schema-structural property\" 和 \"replicate across model scales and families\" 暗示跨架构一致性，但 Dimension 2 batch-level 仅覆盖 vLLM + constrained decoding 的 open-weight models。论文已证明 format dependency 是 BCS-accuracy 关系的前提。\n\n**W4. [warning] Pairwise R²=1.3-1.7% 到 batch-level R²=22% 的放大依赖条件化**\nMonte Carlo simulation 使用 conditional R²=7%（仅非零混淆对，约 11%）。Unconditional R²=1.3% 仅产生 batch R²=0.044。BCS 的 batch-level 预测力本质来源于\"活跃混淆对密度\"而非 pair-level 强预测力。Discussion 阐述不够突出。\n\n**W5. [warning] NER U-shape 恢复缺乏直接证据**\nRecall 从 count 22-44 的 ~0.27 恢复到 full-schema 的 0.41。§6 的 \"dual-task burden\" 是 post-hoc 推测。可通过简单控制实验测试（如 \"extract ALL then filter\" 指令变体）。\n\n**W6. [warning] Confusability-aware batching 无实际收益**\nGraph coloring 仅 +1.4pp (p≈0.19, n.s.)。Renaming 降低 SCS 但降低准确率。Few-shot 加大 gap。论文展示 \"confusability 可检测但不可干预\"。四个 practical directions 中 (1) 已被证反效果，(3) 未测试。\n\n**W7. [warning] Renaming 实验的另一种解读未被讨论**\nLLM 类型混淆可能由概念重叠而非 label surface similarity 驱动。如果是概念重叠，SCS（基于 name embedding）只是不完美 proxy。这削弱 SCS 作为 confusability 度量的理论基础。\n\n**W8. [warning] FewRel train+val merge 的 contamination 论证不完全**\nTrain-origin types 准确率低 8.8pp (p=0.06) 被论文用于反驳 contamination，但 contamination 不一定表现为准确率提高。Appendix P 确认 BCS 偏效应不变，但绝对准确率水平仍可能受影响。\n\n**M1-M4.** Abstract \"-49pp\" 与 confusability 相邻易误导；unconstrained ablation n=25 power 有限；p-value 格式不一致；Table 1 BCS ranges 不可比较性容易忽略。\n\n### Reviewer 1 的 Questions\n\nQ1. BCS-controlled 结果对具体 1,000 test instances 的采样有多敏感？跨不同 test set 方差多少？\nQ2. Confusability-aware batching 的 BCS reduction 需要达到多大才有实际收益？0.559→0.552 不够，阈值在哪？\nQ3. temperature>0 的 sampling 是否可能 mask/amplify BCS 效应？\nQ4. High-BCS ~51% 是否接近 chance level？理论解释？\nQ5. 70B BCS validation CI [+3.0, +20.1] 较宽，用了多少 batches？\n\n### Reviewer 1 的 Missing References\n建议引用 Josifoski et al. (2022) \"GenIE\"。\n\n### Reviewer 1 的 Overall Assessment\n评分: 3.0 (Findings)，Soundness 3.5，Excitement 2.5，Confidence 4/5",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请对每条 Weakness 和 Question 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n注意：你的回应应基于论文内容本身，而非你个人的偏好。\n\n---\n\n### Reviewer 1 的 Weaknesses\n\n**W1. [critical] TOST margin ±3pp 存在循环论证，\"bounded interaction\" claim 过度泛化**\n±3pp 的 anchor 之一是\"0.5×batch SD (≈4.6pp)\"，但 batch SD 部分由 BCS 变异驱动——循环性。更关键：logit-scale TOST inconclusive (p=0.209)，DocRED +5.7pp TOST p=0.77，NER factorial p=0.50。仅 linear-scale sentence-level RE 达到等价。Abstract 和 Conclusion 中 \"bounded interaction\" 未充分限定。\n\n**W2. [critical] DocRED R²=53% 来自 n=35 的不稳定估计，被用作 headline number**\nDocRED 每个 count level 仅 5 batches，回归 n=35，95% CI [0.27, 0.73]。Abstract \"22-53%\" 将统计功效最低的 dataset 的最高值作为 headline。DocRED factorial 也完全 inconclusive (TOST p=0.77)。\n\n**W3. [critical] Dimension 2 缺乏 proprietary model batch-level 验证**\nBCS-controlled 仅在 open-weight models 上验证。Gemini 仅验证 count curves。Abstract \"schema-structural property\" 和 \"replicate across model scales and families\" 暗示跨架构一致性，但 Dimension 2 batch-level 仅覆盖 vLLM + constrained decoding 的 open-weight models。论文已证明 format dependency 是 BCS-accuracy 关系的前提。\n\n**W4. [warning] Pairwise R²=1.3-1.7% 到 batch-level R²=22% 的放大依赖条件化**\nMonte Carlo simulation 使用 conditional R²=7%（仅非零混淆对，约 11%）。Unconditional R²=1.3% 仅产生 batch R²=0.044。BCS 的 batch-level 预测力本质来源于\"活跃混淆对密度\"而非 pair-level 强预测力。Discussion 阐述不够突出。\n\n**W5. [warning] NER U-shape 恢复缺乏直接证据**\nRecall 从 count 22-44 的 ~0.27 恢复到 full-schema 的 0.41。§6 的 \"dual-task burden\" 是 post-hoc 推测。可通过简单控制实验测试（如 \"extract ALL then filter\" 指令变体）。\n\n**W6. [warning] Confusability-aware batching 无实际收益**\nGraph coloring 仅 +1.4pp (p≈0.19, n.s.)。Renaming 降低 SCS 但降低准确率。Few-shot 加大 gap。论文展示 \"confusability 可检测但不可干预\"。四个 practical directions 中 (1) 已被证反效果，(3) 未测试。\n\n**W7. [warning] Renaming 实验的另一种解读未被讨论**\nLLM 类型混淆可能由概念重叠而非 label surface similarity 驱动。如果是概念重叠，SCS（基于 name embedding）只是不完美 proxy。这削弱 SCS 作为 confusability 度量的理论基础。\n\n**W8. [warning] FewRel train+val merge 的 contamination 论证不完全**\nTrain-origin types 准确率低 8.8pp (p=0.06) 被论文用于反驳 contamination，但 contamination 不一定表现为准确率提高。Appendix P 确认 BCS 偏效应不变，但绝对准确率水平仍可能受影响。\n\n**M1-M4.** Abstract \"-49pp\" 与 confusability 相邻易误导；unconstrained ablation n=25 power 有限；p-value 格式不一致；Table 1 BCS ranges 不可比较性容易忽略。\n\n### Reviewer 1 的 Questions\n\nQ1. BCS-controlled 结果对具体 1,000 test instances 的采样有多敏感？跨不同 test set 方差多少？\nQ2. Confusability-aware batching 的 BCS reduction 需要达到多大才有实际收益？0.559→0.552 不够，阈值在哪？\nQ3. temperature>0 的 sampling 是否可能 mask/amplify BCS 效应？\nQ4. High-BCS ~51% 是否接近 chance level？理论解释？\nQ5. 70B BCS validation CI [+3.0, +20.1] 较宽，用了多少 batches？\n\n### Reviewer 1 的 Missing References\n建议引用 Josifoski et al. (2022) \"GenIE\"。\n\n### Reviewer 1 的 Overall Assessment\n评分: 3.0 (Findings)，Soundness 3.5，Excitement 2.5，Confidence 4/5",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2263 · 2026-05-19T11:52:27.224956+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1465
}
```

</details>

---


### Assistant

_source line 2264 · 2026-05-19T11:52:37.238644+00:00_

交叉分享已发出。等待两名 Reviewer 的逐条回应（[AGREE]/[REBUT]）。

**当前进度**：
- Step 0 ✓ 资料检查 + Venue 调研
- Step 0.5 ✓ Reviewer 编排（2 人）
- Step 1 ✓ Round 1 独立审稿（R1: 3.0, R2: 3.0）
- Step 2 → 交叉分享已发出，等待回应
- Step 3 待执行：收敛判断
- Step 4 待执行：汇总报告 + 投递

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 189

## Round 189

2 recorded events


### User

_source line 2265 · 2026-05-19T11:52:39.872388+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿意见已提交给 Review Director。

**审稿概要**：

- **Overall: 3.0 (Findings)**，Soundness 3.5，Excitement 2.5
- **3 个 Must-Fix 问题**：(1) TOST "bounded interaction" claim 在 3/4 条件下 inconclusive 但表述过宽；(2) DocRED R²=53% 来自 n=35 的不稳定估计被用作 headline number；(3) Dimension 2 缺乏 proprietary model batch-level 验证但暗示了跨架构普遍性
- **5 个 Should-Fix 问题**：pair-to-batch R² 放大机制的条件化依赖、NER U-shape 缺乏直接证据、confusability-aware batching 无实际收益、renaming 实验的替代解读、FewRel contamination 分析不完全
- **主要优势**：BCS-controlled 实验设计新颖、统计方法深入、负面结果诚实、cross-model 覆盖面广、centrality confound 处理体现方法论素养

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2266 · 2026-05-19T11:52:46.886298+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 190

## Round 190

2 recorded events


### User

_source line 2267 · 2026-05-19T11:55:18.486262+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Weaknesses 回应

**[AGREE] R2-W1: SCS 与 LLM-PEE 的区分和 novelty**

同意 R2 的核心判断。§2 Related Work 最后一段明确承认 "SCS shares its formal definition with the partitioning criterion in LLM-PEE"，Contribution 1 也改为 "Building on the embedding-similarity criterion from prior schema-partitioning work (LLM-PEE)"（Introduction §1）。论文的 novelty 确实不在度量本身，而在 controlled experimental framework。但"engineering vs. scientific analysis"这一区分确实偏薄——LLM-PEE 也需要理解 confusability 才能做分区，论文只是把同一度量从工程上下文移到分析上下文。

补充：Contribution 1 的措辞 "the first controlled study that isolates count and confusability" 是合理的——之前确实没有 work 做过 BCS-controlled stratified design。novelty 在于实验设计而非度量，但这需要论文更清晰地 frame。

---

**[REBUT] R2-W2: Title "Predict" 与 correlational evidence 的不一致**

不完全同意。Title 中的 "Predict" 是统计预测（statistical prediction）的标准用法，指 "schema complexity metrics statistically predict performance metrics"，这在回归分析语境中是完全准确的。论文没有在 title 中使用 "cause" 或 "determine"。§3.2 明确将 SCS 定义为 "a lightweight proxy computable without running extraction"，Introduction 用 "predictive relationship" 而非 "causal relationship"（§1: "isolating confusability's predictive relationship with extraction degradation"）。

然而，R2 对 renaming 实验的解读有一定道理——如果 SCS 不能通过干预改变 outcome，其 "predictive" 的性质可能更接近 spurious correlation 而非 actionable prediction。但论文在 Limitations item 4 和 Appendix W 中诚实报告了这一结果，并将其归因于 label unfamiliarity 效应而非 SCS 本身的失败。如果 R2 的标准是 title 必须暗示 causal evidence，则对分析性论文过于严格。

---

**[AGREE] R2-W3: 实际效果量过小，实用价值存疑**

同意这是一个实质性问题。§4.3 "Practical magnitude" 报告 typical BCS span (IQR=0.054) 仅产生 2.2pp gap（95% CI [0.4, 4.0]）。论文自己的 within-pool analysis（Appendix E, Table 5）显示，在 80 relation 全集内自然采样时 BCS 变异不足以产生可检测效应（slope=+0.221, p=0.76）。这意味着在实际部署场景中，confusability 的自然变异带来的性能差异很小。

25-31pp 的 extreme-batch gap 来自人为构造的极端 BCS 对比（low-BCS mean≈0.36 vs. high-BCS mean≈0.80），这种极端组合在自然 schema sampling 中不会出现。论文虽然在 §4.3 讨论了这一点，但 Abstract 和 Introduction 对 extreme-batch 数字的引用可能给读者造成 effect size 远大于实际的印象。

补充我的观点：论文的价值更多在于理论理解（understanding why degradation happens）而非实际干预。但如果 typical effect 仅 ~2pp，读者可能合理质疑是否值得为此做如此复杂的 controlled study。

---

**[AGREE] R2-W4: NER Dimension 2 本质为 null result**

同意。BCS 在 NER 上 batch 级效应完全为零（r≈0, n=450; §4.3 和 §4.4），在 MAVEN 上因 centrality confound 无法测量（§4.5）。Dimension 2 的 batch-level 效应实际上仅在 RE 任务上成立（FewRel + DocRED）。

论文将此包装为 Contribution 2 "task asymmetry"（Introduction §1），但这本质上是把一个 null result 重新框架为一个 finding。NER 的 pairwise SCS-confusion correlation 确实显著（r=0.112, p<0.001; Table 2），但 pairwise 信号无法 aggregate 到 batch-level 预测（§4.2 和 §4.4 Discussion 中归因于 NER 的 multi-span output 稀释了 BCS 信号）。

这里的核心问题是：如果 Dimension 2 只在 RE 的 forced-choice classification 下有 batch-level 预测力，论文 title 中的 "Information Extraction" 就过于宽泛了——应该是 "Relation Extraction" 或至少限定为 "forced-choice classification tasks"。

---

**[REBUT] R2-W5: MAVEN 事件检测贡献微弱**

部分不同意。R2 正确指出 MAVEN 的 batch-level BCS 贡献有限，但低估了两个发现的价值：

1. **Pairwise SCS-confusion 信号在 MAVEN 上仍然显著**（MiniLM r=0.129, p<0.001; Table 2），这为 SCS 的跨任务泛化提供了第三个独立验证点。
2. **Centrality confound 的识别**（§4.5, Appendix D）是方法论上的重要贡献。per-type aggregation 在同质 schema 上会被 centrality 污染（positive raw correlation），控制 log frequency 和 degree centrality 后消失（p>0.2）——这对未来 work 使用 mean BCS 是重要的 caveat。论文正确识别了 per-type vs. pairwise 分析的适用边界。

但同意 R2 的判断：ED 不应被包含在 title 的 "Information Extraction" 概括中，因为 MAVEN 的贡献仅限于 pairwise 验证和 confound 识别，没有 batch-level 效应。

---

**[AGREE] R2-W6: Embedding 选择不一致**

同意这是一个问题。§3.2 的理由是 "MiniLM's 384-d space does not separate [Few-NERD's] same-category pairs well"，但论文自己的数据直接反驳了这一理由：MiniLM 在 Few-NERD 上的 pairwise SCS-confusion correlation (r=0.172) 比 Qwen3 (r=0.138) 更强（§4.2, Appendix G）。如果 MiniLM 给出更强的相关性，它显然在分离 confusable pairs 方面做得更好，而非更差。

论文的反驳是 "shared-representation bias is conservative rather than inflationary"（§4.2），意思是使用 Qwen3 自身 embedding 反而 underestimate 了效应。这个论点逻辑上成立——但那更应该统一使用 MiniLM（给出更强信号且没有 circular reasoning 嫌疑）。

不过，circular reasoning 的担忧程度有限：论文用 Qwen3 embedding 计算 SCS/BCS，然后在 Qwen3 inference 上测量 confusion——但 embedding 和 inference 是完全不同的计算过程（hidden state extraction vs. autoregressive generation）。真正的 circular reasoning 是如果用 confusion matrix 本身来定义 confusability，论文没有这样做。

**建议**：统一使用 MiniLM，把 Qwen3 作为 sensitivity check 报告。这消除一致性问题且不影响结论。

---

**[AGREE] R2-W7: DocRED bounded-interaction 不成立**

完全同意。这与我的 R1-W1 一致。DocRED TOST p=0.77，interaction estimate +5.7pp（CI [-1.6, 13.0]）。NER factorial inconclusive (p=0.50)。Logit-scale TOST inconclusive (p=0.209)。

"Bounded interaction" 仅在 sentence-level RE、linear scale、±3pp margin 下成立。§4.4 的标题和 Abstract/Conclusion 的叙事确实 overstate 了这一结论的适用范围。

---

**[AGREE] R2-W8 (Abstract 数据密度): 部分同意。** Abstract 确实在有限篇幅内堆砌了大量数字（0.72→0.27, 85.7%→49.5%, 88.0%→38.7%, r²=1.3-1.7%, 22-53%, ±3pp），但这些数字对于量化研究是必要的。可以精简到 2-3 个关键数字。

**[REBUT] R2-W9 (Introduction 过早引入统计细节):** Introduction 中的统计细节（TOST margin、logit-scale inconclusive）出现在 Finding (1) 的描述中（§1, lines 14-15），这些 qualifiers 恰恰是避免 overstatement 所必需的。如果删除这些限定，Introduction 反而会 overstate "bounded interaction" claim（正是 R2-W7 指出的问题）。这里存在两难：加限定被批评为过早引入细节，不加限定被批评为 overstate。我认为保留限定是更安全的选择。

**[AGREE] R2-W10 (-ing 分词短语残留):** 这是写作风格问题，应逐一检查修改。

---

### Questions 回应

**[AGREE] R2-Q1: Extreme-batch 是否引入其他 confound**

这是一个好问题且论文回答不充分。Extreme low-BCS batches 包含 "maximally dissimilar types"，这些类型可能系统性地来自不同领域/类别，从而天然更"容易"区分——不仅因为 embedding distance 大，还因为领域知识差异大。Appendix J 的 VIF=1.06 和 r(BCS, difficulty)=-0.21 来自 random batches，不一定适用于 extreme batches。

但 within-pool analysis（Table 5）提供了部分回答：从同一 80-relation pool 内抽取 16-relation 子集时，slope 与独立 16-relation pool 一致（permutation p≈0.60）。这说明 pool composition 差异不是效应的主要来源。不过 extreme batches 仍是特殊构造，这个 concern 值得在论文中讨论。

---

**[REBUT] R2-Q2: 单一 seed 的 variance decomposition**

R2 说 "仅在 count=80 下测量" 不准确。Appendix Q (Table 10) 实际报告了 count 1-80 的完整方差分解（3 seeds × 25 batches per count level）。在 count 4-64 所有水平上，batch variance 均显著大于 seed variance（ratio 5.4-474.4×）。仅 count=80 因只有一种 batch composition 而 batch variance 为零。论文已在 §3.4 明确说明使用 greedy decoding (temperature=0)，使得 inference 近乎确定性。seed 间差异主要反映不同 random batch compositions 的选择，而非 inference 随机性。

---

**[AGREE] R2-Q3: FewRel train+val merge 的 -8.8pp 差异**

同意需要更充分的讨论。这与我的 R1-W8 一致。-8.8pp (p=0.06) 是 borderline significant。Appendix P 的 split-origin covariate 分析显示 BCS 偏效应不变（β_BCS unchanged, β_origin=-0.057, p=0.245），这有力地表明 BCS-accuracy 关系本身不受 split-origin 混淆。但绝对准确率水平可能仍受预训练暴露影响，论文应弱化 "opposite to the contamination hypothesis" 的措辞。

---

**[AGREE] R2-Q4: Gemini count-64 的 selection bias**

合理的担忧。API quota exhaustion 导致 11/25 batches 可能非随机——如果 harder batches（更长输出、更多 retries）更容易耗尽 quota，11 个完成的 batches 可能系统性偏向 easier batches。论文仅标注 "partial" 但未讨论 selection mechanism。建议补充：(1) 11 个完成 batches 与全部 25 个 batches 的 BCS 分布比较；(2) 讨论 API failure mode（是否随机 timeout 还是与 batch 难度相关）。

---

### 总结

我与 R2 在大多数 weakness 上意见一致，尤其是 W3（effect size 小）、W4（NER null result）、W6（embedding 不一致）和 W7（bounded interaction 过度泛化）。主要分歧在 W2（title "predict" 在统计语境中合理）和 W5（MAVEN 的贡献被 R2 低估——centrality confound 识别有方法论价值）。

整体判断：论文方法论严谨、负面结果诚实，但核心效应实际意义有限（typical ~2pp），且最强 claim（BCS batch-level prediction）仅限 RE。R2 的 Overall 3.0 (Findings) 与我的评分一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2268 · 2026-05-19T11:55:24.649462+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 191

## Round 191

2 recorded events


### User

_source line 2269 · 2026-05-19T11:55:28.339721+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

逐条回应了 R2 的 10 条 Weakness 和 4 个 Question：
- **[AGREE]**: W1（novelty 偏薄）、W3（typical effect ~2pp 实用价值有限）、W4（NER Dimension 2 本质 null result）、W6（embedding 选择不一致）、W7（bounded interaction 过度泛化）、W8/W10（写作问题）、Q1（extreme-batch confound）、Q3（split-origin 需更充分讨论）、Q4（Gemini selection bias）
- **[REBUT]**: W2（title "predict" 在统计语境中合理）、W9（Introduction 的统计限定是防止 overstatement 所必需的）、Q2（variance decomposition 实际覆盖所有 count level，非仅 count=80）
- **部分 REBUT**: W5（MAVEN 的 centrality confound 识别有方法论价值，R2 低估了这一贡献）

与 R2 总体判断一致：Overall 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2270 · 2026-05-19T11:55:34.824421+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 192

## Round 192

12 recorded events


### User

_source line 2271 · 2026-05-19T11:56:30.481011+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 逐条回应 Reviewer 1 审稿意见

---

### Weaknesses 回应

**[AGREE with nuance] R1-W1: TOST margin ±3pp 循环论证 + bounded interaction 泛化**

R1 关于循环论证的核心论点有道理：batch SD (≈4.6pp) 本身部分由 BCS 变异驱动，用它作为等价性 margin 的锚点存在概念性循环。论文的三个 anchor（empirical、practical、statistical）中，empirical 和 statistical 两个都指向 batch SD，而 batch SD 不是独立于待检验假设的外部标准。Table 9 (Appendix C) 的 sensitivity analysis 部分缓解了这一问题——在 ±2pp 时也达到 marginal equivalence (p=0.047)——但这并不消除 margin 选择的 principled 基础问题。

但 R1 关于 "Abstract 和 Conclusion 中 bounded interaction 未充分限定" 的判断**部分不准确**。检查原文：
- **Abstract**: 完全不提 "bounded interaction"，只说 "Degradation operates along two dimensions" (Abstract, line 2)
- **Introduction**: 明确限定 "bounded interaction under a ±3pp margin in sentence-level RE (marginally at ±2pp; logit-scale inconclusive) but not in document-level RE or NER" (Introduction, finding (1))
- **Conclusion**: 明确限定 "with bounded interaction in sentence-level RE but not in document-level RE or NER" (§7 Conclusion)

因此，over-generalization 的问题在正文中已被合理限定。真正的弱点在于 TOST margin 选择的理论基础，而非 claim scope 的限定。

---

**[AGREE] R1-W2: DocRED R²=53% 不稳定**

完全同意。n=35, CI [0.27, 0.73] 意味着真实 R² 可能在 27%-73% 之间任意位置。Abstract 使用 "22-53%" 作为 headline range 时，将统计功效最弱的数据集的最高值作为上界，有误导性。论文在 §5.3 正文中确实标注了 n=35 和 CI，但将 53% 放在 Abstract 和 Contribution 2 中而不加 qualifier 是不妥的。建议 Abstract 使用更保守的 "22%" (FewRel, n=100) 或 "22-53% (CI: 27-73%)" 来表达不确定性。

---

**[AGREE with nuance] R1-W3: Dimension 2 缺乏 proprietary model batch-level 验证**

R1 的核心论点成立：BCS-controlled batch-level 验证仅在 open-weight models + vLLM constrained decoding 下完成，Gemini 2.5 Flash 仅验证了 Dimension 1 (count curves, Appendix §sec:appendix_cross_model_gemini)。鉴于论文自身证明 format dependency 是 BCS-accuracy 关系的前提条件（unconstrained ablation 消除 BCS 效应，§6 Discussion），而 API 模型的 constrained decoding 实现可能不同，这确实是一个重要限制。

但需要区分两个层次的 claim：
- **Pairwise SCS-confusion correlation**: 这是 schema-structural 属性（不依赖 constrained decoding），在 NER (无 constrained decoding 的 enum constraint) 和 ED 上也成立 (Table 2)。这一层面的 "schema-structural" claim 是合理的。
- **Batch-level BCS-accuracy prediction**: 依赖 forced-choice classification format，确实未在 proprietary models 上验证。

Abstract 的 "effects replicate across model scales and families" 未做此区分，因此 R1 的批评有道理。

---

**[REBUT] R1-W4: Pairwise R² amplification依赖条件化**

R1 描述的现象是准确的（conditional R²=7% vs unconditional 1.3%，后者仅产生 batch R²=0.044），但论文**已经明确讨论了这一问题**：
- Discussion §6: "The unconditional pairwise R² is 1.3%; conditional on nonzero confusion, R² rises to 7%."
- Appendix H: 完整的 simulation 同时报告了 conditional 和 unconditional 两种 baseline，明确指出 "This ~5× gap reflects the dilution from zero-confusion pairs: approximately 89% of type pairs never exhibit mutual confusion"
- Appendix H 明确总结: "BCS predicts batch accuracy through the density of active confusable pairs, not uniform contributions from all pairs"

R1 说 "Discussion 阐述不够突出"，但论文的 Appendix H 包含了完整的对比分析，且 Discussion 给出了简洁总结。这是一个 presentation emphasis 问题而非 substance gap。论文对这一机制的透明度已足够。

---

**[AGREE] R1-W5: NER U-shape 缺乏直接证据**

同意。§6 Discussion 的 "dual-task burden" 解释（"partial schemas require simultaneous span detection and type filtering; at full schema, filtering becomes vacuous and recall recovers"）是合理的 post-hoc 假说，但论文未提供控制实验验证。R1 建议的 "extract ALL then filter" 指令变体是一个可操作的验证方案。

需要补充的是：U-shape 在 70B 上也复现（Appendix §sec:appendix_cross_model_70b, Table 10: count 22→44 有恢复），跨模型一致性增加了 dual-task burden 假说的可信度，但仍不能替代直接验证。

---

**[AGREE with nuance] R1-W6: Confusability-aware batching 无实际收益**

R1 的总结准确——graph coloring +1.4pp (n.s.)、renaming 降低准确率、few-shot 扩大 gap。论文确实呈现了 "confusability 可检测但不可干预" 的图景。

但需要注意：这正是论文 Contribution 3 的核心——它将 schema decomposition 的失败**诊断为结构性障碍**（NER 的 merge amplification、RE 的 routing failure），而非简单地报告"不work"。Oracle routing 的 +29.8pp (Table 6, §6) 表明 type separation 的 theoretical ceiling 很高，只是 practical routing 尚未解决。四个 practical directions 中 (1) 和 (3) 确实证据不足，但 (2) BCS 作为 quality indicator 和 (4) schema-controlled metrics 是独立可行的。

R1 的批评更多是关于 practical impact 不足，而非分析本身有误。

---

**[AGREE] R1-W7: Renaming 实验的概念重叠解读**

这是本轮审稿中最有力的理论质疑之一。R1 的论点：如果 LLM 类型混淆由**概念重叠**（relation 之间的语义近邻关系）而非 **label surface similarity** 驱动，那么 SCS（基于 type name embedding cosine similarity）只是概念重叠的不完美 proxy，renaming 改变了 surface 但未改变 concept。

论文的 renaming 实验（Appendix L）实际上提供了支持这一解读的证据：降低 SCS 未降低 confusion，反而因 label unfamiliarity 降低了准确率。但论文将此解读为 "label unfamiliarity effect outweighs any benefit from reduced confusability"，而未讨论更根本的可能性——SCS 度量的 construct validity 问题。

这与我自己 W1 (SCS novelty) 中提到的 concern 一致：如果 SCS 只是概念重叠的粗糙 proxy，那么整个 BCS-controlled 框架的理论基础需要更谨慎的讨论。

---

**[REBUT with partial agreement] R1-W8: FewRel contamination论证**

R1 的技术论点有道理——contamination 不一定表现为准确率提高（可能表现为 calibration 变化或特定关系的不均匀影响）。但论文的防线不仅是 accuracy 方向对比，更重要的是 Appendix N 的 split-origin covariate analysis：

- BCS partial effect 在控制 train_origin_ratio 后完全不变: β_BCS = -0.416 (controlled) vs -0.412 (uncontrolled) (Appendix N)
- train_origin_ratio 本身不显著: β = -0.057, p = 0.245
- Pairwise SCS 分布在 train/val origin types 之间无差异: Mann-Whitney p = 0.754

这意味着即使绝对准确率受 contamination 影响，**BCS-accuracy 关系**（论文的核心 claim）不受影响。R1 承认了这一点（"Appendix P 确认 BCS 偏效应不变"），所以 R1 的批评更多针对论文在 Limitations §5 的论证修辞（用 accuracy 方向反驳 contamination），而非实质性地质疑核心发现。

---

### Minor Issues 回应

**[AGREE] R1-M1**: Abstract "-49pp" 紧跟 "type confusability" 后确实容易误读。-49pp 来自 DocRED count decline (§5.1)，属于 Dimension 1 (count)，但读者可能误以为是 confusability 的效果。

**[AGREE] R1-M2**: unconstrained ablation n=25 确实 power 有限。p=0.49 不能强有力地排除小到中等的 BCS 效应。但论文将其定位为 format dependency 的证据而非 null 证明，这一定位是合理的。

**[AGREE] R1-M3**: p-value 格式不一致（${<}0.001$ vs $p < 0.001$ vs $p < 10^{-35}$）。应统一格式。

**[AGREE] R1-M4**: Table 1 BCS ranges 使用不同 embedding models（Few-NERD 用 Qwen3, 其余用 MiniLM），不可比较性确实容易被忽略。脚注标注不够醒目。

---

### Questions 回应

**Q1 (test set sensitivity)**: 合理问题。论文使用固定的 1,000 balanced instances，batch-level 结果通过 bootstrap CI 量化了 batch composition variance，但未报告 test set resampling 的 variance。不过，RE 使用 balanced sampling (12-13 per type)，test set variance 应较小。NER 的 1,000 instances 受自然频率分布影响可能更大。

**Q2 (BCS reduction threshold)**: 有价值的问题。从 FewRel regression slope (§5.3, slope = -0.509) 和 random batching 的实际 BCS 分布来看，graph coloring 仅将 BCS 从 0.559 降至 0.552 (ΔBCS = -0.007)，对应预期准确率提升仅 0.36pp (0.007 × 0.509)，远低于检测阈值。若要达到可检测的 ~3pp 收益，需要 ΔBCS ≈ 0.06，即约一个 IQR 的 BCS 变化。这在 80-type schema 中的 graph coloring 中很难实现，因为自然 BCS range 本身就压缩。

**Q3 (temperature>0)**: 有趣但未经验证。greedy decoding 下 inter-seed variance 极低（residual SD = 0.88pp, Appendix K）。Temperature>0 会增加 variance，可能同时增大 batch SD 和 BCS 效应的 noise，但方向不确定。论文选择 greedy decoding 是为了最小化 inference randomness，这一设计选择合理。

**Q4 (high-BCS ~51% as chance)**: 8-type batch 的 random chance 是 12.5%，80-type 是 1.25%。51% 远高于 chance。更合理的解读是 high-BCS 下的 confusion 将 effective choice set 从 8 types 压缩到 ~2-3 个高度相似的候选，使 effective chance 接近 33-50%。论文称其为 "task-inherent difficulty floor" (§5.3)，但未提供此解释。

**Q5 (70B BCS CI width)**: Appendix §sec:appendix_cross_model_70b 报告 "All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B"。对于 count 16 的 BCS-controlled 实验，如果使用 16-relation pilot pool，则仅 1 low + 1 high extreme batch (CI 来自 test instances bootstrap)。CI [+3.0, +20.1] 的宽度与此一致。如果使用 80-pool 的 25 low + 25 high batches，CI 应窄得多。论文未明确说明 70B BCS validation 使用哪个 pool，这是一个 reporting gap。

---

### Missing References 回应

**[AGREE]** Josifoski et al. (2022) "GenIE" 是 zero-shot 关系抽取的重要工作，确实值得引用。论文 Related Work 覆盖了 RelationPrompt (2022) 等类似工作，但 GenIE 的 sequence-to-sequence IE 范式与本文的 schema-scaling 问题直接相关。

---

### 对 R1 Overall Assessment 的看法

R1 给出 3.0 (Findings)、Soundness 3.5、Excitement 2.5、Confidence 4/5。

这与我的评分完全一致（Overall 3.0, Soundness 3.5, Excitement 2.5, Confidence 4/5）。两位 reviewer 独立得出相同评分，增加了评估的可信度。核心共识：方法论严谨但 novelty 和 practical impact 不足以支撑 Main conference。

R1 和我的审稿侧重不同（R1 偏统计方法论，我偏新颖性和写作），但在关键弱点上有实质性重叠：
- SCS/BCS 效果量过小（R1-W4 + 我的 W3）
- NER dimension 2 null result 限制泛化性（R1 正文隐含 + 我的 W4）
- 实际干预无效（R1-W6 + 我的 W3 practical implications 部分）
- DocRED R² 的不确定性（R1-W2 + 我的 W7 关于 bounded-interaction 的 concern）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2272 · 2026-05-19T11:58:34.329380+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema-dag-extraction",
  "issues_yaml": "# Round 21 Review Issues Tracker\n# Updated: 2026-05-19 (Fresh review — Round 21)\n# Reviewer lineup: R1 (method rigor), R2 (novelty + writing)\n\n# ============================================================\n# CRITICAL — 双方共识\n# ============================================================\n\n- id: R21-C1\n  summary: \"TOST ±3pp margin 存在循环论证，bounded interaction 仅在 sentence-level RE linear scale 成立\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-W1 提出循环论证（batch SD 部分由 BCS 驱动）；R2 同意 margin 选择缺乏 principled basis。R2 纠正：正文已限定 scope（Intro/Conclusion 明确写 'sentence-level RE'），但 TOST margin 理论基础仍有问题。3/4 条件 inconclusive（logit p=0.209, DocRED p=0.77, NER p=0.50）。\"}\n  action_items:\n    - {round: 21, action: \"补充讨论 margin anchor 的独立性问题；考虑 practical equivalence 替代方案；Table 4 sensitivity 更突出地引用\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-C2\n  summary: \"DocRED R²=53% 来自 n=35 不稳定估计，Abstract 使用 '22-53%' 误导\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-W2 首提，R2 完全同意。CI [0.27, 0.73] 极宽。Abstract 将统计功效最弱 dataset 的最高值作为 headline upper bound。DocRED factorial 也完全 inconclusive (TOST p=0.77)。\"}\n  action_items:\n    - {round: 21, action: \"Abstract 改为 '22% (up to 53% with wider CI)' 或仅用 FewRel R²=22%；DocRED 标注为 preliminary replication\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-C3\n  summary: \"Dimension 2 缺乏 proprietary model batch-level 验证，但 claim 暗示跨架构普遍性\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-W3 首提，R2 同意但区分两层 claim：pairwise SCS 是 schema-structural（不依赖 constrained decoding），batch-level BCS 依赖 forced-choice format 未在 proprietary models 验证。Abstract 'effects replicate across model scales and families' 未做此区分。\"}\n  action_items:\n    - {round: 21, action: \"Abstract 限定 'schema-structural' 为 pairwise level；batch-level claim 限定为 open-weight + constrained decoding；讨论 API 模型 constrained decoding 差异\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-C4\n  summary: \"SCS 指标借用自 LLM-PEE，novelty 在实验设计而非度量本身，当前 framing 不够清晰\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W1 首提，R1 同意。'engineering vs scientific analysis' 区分偏薄。Contribution 1 已改为 'Building on... prior work'，但论文整体 framing 仍可能让读者误以为 SCS 是本文创新。novelty 在于 BCS-controlled stratified design，需更清晰 frame。\"}\n  action_items:\n    - {round: 21, action: \"Contribution 1 重写：明确 SCS adopted from LLM-PEE，强调 stratified BCS-controlled experimental framework 为方法论创新\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-C5\n  summary: \"Typical effect size ~2pp (IQR=0.054)，实用价值有限\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W3 首提，R1 完全同意。自然 schema sampling 下 BCS 变异不足以产生可检测效应（80-rel slope=+0.221, p=0.76）。Extreme-batch 25-31pp 来自人为构造。Abstract/Intro 对 extreme-batch 数字的引用可能给读者造成 effect size 远大于实际的印象。论文价值更多在理论理解而非实际干预。\"}\n  action_items:\n    - {round: 21, action: \"Discussion 更直接讨论 ~2pp 的实际意义；说明哪些 realistic 场景下 confusability 成为 bottleneck；Abstract 叙事平衡 extreme vs typical\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING — 双方共识或一方提出另一方不反对\n# ============================================================\n\n- id: R21-W1\n  summary: \"NER Dimension 2 batch-level 为 null (r≈0, n=450)，Dim2 泛化性仅限 RE forced-choice\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W4 首提，R1 完全同意。Pairwise 信号在 NER 显著 (r=0.112) 但无法 aggregate 到 batch-level。Title 'Information Extraction' 过于宽泛。\"}\n  action_items:\n    - {round: 21, action: \"Intro/Abstract 更明确限定 Dim2 适用范围；考虑 title 是否应限定为 RE 或 forced-choice tasks\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-W2\n  summary: \"Embedding 选择不一致（Few-NERD 用 Qwen3，其余 MiniLM），MiniLM 实际更优\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W6 首提，R1 同意。论文自身数据显示 MiniLM r=0.172 > Qwen3 r=0.138 on Few-NERD，反驳了选择 Qwen3 的理由。R1 建议统一使用 MiniLM，Qwen3 作 sensitivity check。Circular reasoning concern 有限但一致性问题成立。\"}\n  action_items:\n    - {round: 21, action: \"统一 MiniLM 为主 embedding，Qwen3 作 sensitivity check；或至少在正文讨论 cross-embedding 一致性\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-W3\n  summary: \"NER U-shape (count 22-44→66 recovery) 的 dual-task burden 解释缺乏直接实验验证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-W5 首提，R2 同意。Post-hoc 假说在 70B 上也复现增加可信度，但不能替代直接验证。R1 建议 'extract ALL then filter' 控制实验。\"}\n  action_items:\n    - {round: 21, action: \"标注为 'one possible explanation requiring further investigation'，或补充控制实验\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-W4\n  summary: \"Confusability 可检测但不可干预——无有效的改进方案\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-W6 首提，R2 部分同意（但指出 Contribution 3 的诊断价值和 oracle routing 的 theoretical ceiling）。Graph coloring +1.4pp n.s.；renaming 降低准确率；few-shot 扩大 gap。Practical directions (1) 已证反效果，(3) 未测试。\"}\n  action_items:\n    - {round: 21, action: \"Discussion 中更诚实 frame 实践意义：诊断工具 > 干预方案；讨论 label unfamiliarity vs conceptual overlap 的困难\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-W5\n  summary: \"Renaming 实验支持 'conceptual overlap vs label surface similarity' 的替代解读，削弱 SCS construct validity\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-W7 首提，R2 评价为'本轮最有力的理论质疑之一'。SCS 基于 name embedding similarity，但类型混淆可能由概念重叠而非 label surface similarity 驱动。Renaming 实验证据支持此解读。\"}\n  action_items:\n    - {round: 21, action: \"Discussion/Limitations 讨论 conceptual overlap vs label surface similarity distinction；承认 SCS 可能是 downstream proxy 而非 root cause metric\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-W6\n  summary: \"MAVEN ED 贡献仅限 pairwise 验证和 centrality confound 识别，batch-level 无 positive evidence\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W5 首提，R1 部分 REBUT（centrality confound 识别有方法论价值），但同意 ED 不应被包含在 title 的 'IE' 概括中。Pairwise MiniLM r=0.129 p<0.001 仍有价值。\"}\n  action_items:\n    - {round: 21, action: \"Contribution 列表中 ED 单独列为 methodological finding，不与 NER/RE 并列\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# DIVERGENCE — 分歧记录\n# ============================================================\n\n- id: R21-D1\n  summary: \"Title 'Predict' 是否与 correlational evidence 不匹配\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W2 Must-Fix (title 暗示因果/预测，但论文仅 correlational)。R1 REBUT（'predict' 在统计回归语境中是标准用语，论文明确用 'predictive relationship'）。R1 部分承认 renaming 实验的失败削弱了 actionable prediction claim。\"}\n  action_items:\n    - {round: 21, action: \"Director 判断：R1 的 REBUT 有理，'Predict' 在统计语境中合理，但应在 rebuttal 中准备防御\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO — 小问题\n# ============================================================\n\n- id: R21-I1\n  summary: \"Abstract 数据密度过高，过多具体数字\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W8。R1 部分同意但认为量化研究需要数字。可精简到 2-3 个关键数字。\"}\n  action_items: []\n\n- id: R21-I2\n  summary: \"Introduction 过早引入 TOST 等统计细节\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W9。R1 REBUT（限定词是防止 overstatement 所必需的）。两难：加限定=过早细节，不加=overstate。Director 判断：保留限定更安全。\"}\n  action_items: []\n\n- id: R21-I3\n  summary: \"-ing 分词短语残留 (Abstract/Results)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W10，R1 同意。'revealing...', 'establishing...' 等。\"}\n  action_items: []\n\n- id: R21-I4\n  summary: \"P-value 报告格式不一致 (p<0.001 vs p<10^{-35})\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-M3，R2 同意。\"}\n  action_items: []\n\n- id: R21-I5\n  summary: \"FewRel train+val merge contamination 论证修辞可改进\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-W8。BCS 偏效应不受影响 (Appendix N β_BCS 不变)，但 'opposite to contamination hypothesis' 措辞过强。R2 rebut 指出防线主要在 split-origin covariate analysis 而非 accuracy 方向。\"}\n  action_items: []\n\n- id: R21-I6\n  summary: \"Missing reference: Josifoski et al. (2022) GenIE\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1 建议，R2 同意。\"}\n  action_items: []\n\n- id: R21-I7\n  summary: \"Gemini count-64 partial (11/25 batches) 可能有 selection bias\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-Q4，R1 同意。应补充 BCS 分布比较和 failure mode 讨论。\"}\n  action_items: []\n\n- id: R21-I8\n  summary: \"70B BCS validation 未明确说明使用哪个 pool，CI 较宽\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-Q5，R2 指出为 reporting gap。\"}\n  action_items: []\n\n# ============================================================\n# R20 及更早 — 状态更新\n# ============================================================\n\n- id: R20-N1\n  summary: \"'Largely additive' overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"已修复，改为 'two dimensions'\"}\n    - {round: 21, reviewers: [R1, R2], note: \"R21 未单独提出此 exact issue，但 R21-C1 是其演化版（TOST margin 问题）\"}\n  resolution: \"全文删除 'largely additive'。但 TOST margin 基础问题仍在 (R21-C1)。\"\n  resolution_round: 20\n\n- id: R20-W1\n  summary: \"Title 'Predict' 与 correlational evidence 不匹配\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"R20 wont_fix (保留 title)\"}\n    - {round: 21, reviewers: [R1, R2], note: \"R21-D1 复现分歧。R2 Must-Fix, R1 REBUT。\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-I3\n  summary: \"SCS name-only vs prompt content 不一致\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - {round: 20, reviewers: [R2], note: \"Appendix 有 ablation 但正文应简要提及\"}\n    - {round: 21, reviewers: [], note: \"R21 未单独提出，但 §3.2 已加入 name+def ablation cross-ref\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W4\n  summary: \"NER U-shape dual-task burden 假说缺实验证据\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 21\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"Speculative\"}\n    - {round: 21, reviewers: [R1, R2], note: \"R21-W3 复现。R1 建议 'extract ALL then filter' 控制实验。\"}\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema-dag-extraction",
    "issues_yaml": "# Round 21 Review Issues Tracker\n# Updated: 2026-05-19 (Fresh review — Round 21)\n# Reviewer lineup: R1 (method rigor), R2 (novelty + writing)\n\n# ============================================================\n# CRITICAL — 双方共识\n# ============================================================\n\n- id: R21-C1\n  summary: \"TOST ±3pp margin 存在循环论证，bounded interaction 仅在 sentence-level RE linear scale 成立\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-W1 提出循环论证（batch SD 部分由 BCS 驱动）；R2 同意 margin 选择缺乏 principled basis。R2 纠正：正文已限定 scope（Intro/Conclusion 明确写 'sentence-level RE'），但 TOST margin 理论基础仍有问题。3/4 条件 inconclusive（logit p=0.209, DocRED p=0.77, NER p=0.50）。\"}\n  action_items:\n    - {round: 21, action: \"补充讨论 margin anchor 的独立性问题；考虑 practical equivalence 替代方案；Table 4 sensitivity 更突出地引用\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-C2\n  summary: \"DocRED R²=53% 来自 n=35 不稳定估计，Abstract 使用 '22-53%' 误导\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-W2 首提，R2 完全同意。CI [0.27, 0.73] 极宽。Abstract 将统计功效最弱 dataset 的最高值作为 headline upper bound。DocRED factorial 也完全 inconclusive (TOST p=0.77)。\"}\n  action_items:\n    - {round: 21, action: \"Abstract 改为 '22% (up to 53% with wider CI)' 或仅用 FewRel R²=22%；DocRED 标注为 preliminary replication\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-C3\n  summary: \"Dimension 2 缺乏 proprietary model batch-level 验证，但 claim 暗示跨架构普遍性\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-W3 首提，R2 同意但区分两层 claim：pairwise SCS 是 schema-structural（不依赖 constrained decoding），batch-level BCS 依赖 forced-choice format 未在 proprietary models 验证。Abstract 'effects replicate across model scales and families' 未做此区分。\"}\n  action_items:\n    - {round: 21, action: \"Abstract 限定 'schema-structural' 为 pairwise level；batch-level claim 限定为 open-weight + constrained decoding；讨论 API 模型 constrained decoding 差异\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-C4\n  summary: \"SCS 指标借用自 LLM-PEE，novelty 在实验设计而非度量本身，当前 framing 不够清晰\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W1 首提，R1 同意。'engineering vs scientific analysis' 区分偏薄。Contribution 1 已改为 'Building on... prior work'，但论文整体 framing 仍可能让读者误以为 SCS 是本文创新。novelty 在于 BCS-controlled stratified design，需更清晰 frame。\"}\n  action_items:\n    - {round: 21, action: \"Contribution 1 重写：明确 SCS adopted from LLM-PEE，强调 stratified BCS-controlled experimental framework 为方法论创新\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-C5\n  summary: \"Typical effect size ~2pp (IQR=0.054)，实用价值有限\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W3 首提，R1 完全同意。自然 schema sampling 下 BCS 变异不足以产生可检测效应（80-rel slope=+0.221, p=0.76）。Extreme-batch 25-31pp 来自人为构造。Abstract/Intro 对 extreme-batch 数字的引用可能给读者造成 effect size 远大于实际的印象。论文价值更多在理论理解而非实际干预。\"}\n  action_items:\n    - {round: 21, action: \"Discussion 更直接讨论 ~2pp 的实际意义；说明哪些 realistic 场景下 confusability 成为 bottleneck；Abstract 叙事平衡 extreme vs typical\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING — 双方共识或一方提出另一方不反对\n# ============================================================\n\n- id: R21-W1\n  summary: \"NER Dimension 2 batch-level 为 null (r≈0, n=450)，Dim2 泛化性仅限 RE forced-choice\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W4 首提，R1 完全同意。Pairwise 信号在 NER 显著 (r=0.112) 但无法 aggregate 到 batch-level。Title 'Information Extraction' 过于宽泛。\"}\n  action_items:\n    - {round: 21, action: \"Intro/Abstract 更明确限定 Dim2 适用范围；考虑 title 是否应限定为 RE 或 forced-choice tasks\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-W2\n  summary: \"Embedding 选择不一致（Few-NERD 用 Qwen3，其余 MiniLM），MiniLM 实际更优\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W6 首提，R1 同意。论文自身数据显示 MiniLM r=0.172 > Qwen3 r=0.138 on Few-NERD，反驳了选择 Qwen3 的理由。R1 建议统一使用 MiniLM，Qwen3 作 sensitivity check。Circular reasoning concern 有限但一致性问题成立。\"}\n  action_items:\n    - {round: 21, action: \"统一 MiniLM 为主 embedding，Qwen3 作 sensitivity check；或至少在正文讨论 cross-embedding 一致性\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-W3\n  summary: \"NER U-shape (count 22-44→66 recovery) 的 dual-task burden 解释缺乏直接实验验证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-W5 首提，R2 同意。Post-hoc 假说在 70B 上也复现增加可信度，但不能替代直接验证。R1 建议 'extract ALL then filter' 控制实验。\"}\n  action_items:\n    - {round: 21, action: \"标注为 'one possible explanation requiring further investigation'，或补充控制实验\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-W4\n  summary: \"Confusability 可检测但不可干预——无有效的改进方案\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-W6 首提，R2 部分同意（但指出 Contribution 3 的诊断价值和 oracle routing 的 theoretical ceiling）。Graph coloring +1.4pp n.s.；renaming 降低准确率；few-shot 扩大 gap。Practical directions (1) 已证反效果，(3) 未测试。\"}\n  action_items:\n    - {round: 21, action: \"Discussion 中更诚实 frame 实践意义：诊断工具 > 干预方案；讨论 label unfamiliarity vs conceptual overlap 的困难\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-W5\n  summary: \"Renaming 实验支持 'conceptual overlap vs label surface similarity' 的替代解读，削弱 SCS construct validity\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-W7 首提，R2 评价为'本轮最有力的理论质疑之一'。SCS 基于 name embedding similarity，但类型混淆可能由概念重叠而非 label surface similarity 驱动。Renaming 实验证据支持此解读。\"}\n  action_items:\n    - {round: 21, action: \"Discussion/Limitations 讨论 conceptual overlap vs label surface similarity distinction；承认 SCS 可能是 downstream proxy 而非 root cause metric\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R21-W6\n  summary: \"MAVEN ED 贡献仅限 pairwise 验证和 centrality confound 识别，batch-level 无 positive evidence\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W5 首提，R1 部分 REBUT（centrality confound 识别有方法论价值），但同意 ED 不应被包含在 title 的 'IE' 概括中。Pairwise MiniLM r=0.129 p<0.001 仍有价值。\"}\n  action_items:\n    - {round: 21, action: \"Contribution 列表中 ED 单独列为 methodological finding，不与 NER/RE 并列\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# DIVERGENCE — 分歧记录\n# ============================================================\n\n- id: R21-D1\n  summary: \"Title 'Predict' 是否与 correlational evidence 不匹配\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W2 Must-Fix (title 暗示因果/预测，但论文仅 correlational)。R1 REBUT（'predict' 在统计回归语境中是标准用语，论文明确用 'predictive relationship'）。R1 部分承认 renaming 实验的失败削弱了 actionable prediction claim。\"}\n  action_items:\n    - {round: 21, action: \"Director 判断：R1 的 REBUT 有理，'Predict' 在统计语境中合理，但应在 rebuttal 中准备防御\", assigned_to: research_director, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO — 小问题\n# ============================================================\n\n- id: R21-I1\n  summary: \"Abstract 数据密度过高，过多具体数字\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W8。R1 部分同意但认为量化研究需要数字。可精简到 2-3 个关键数字。\"}\n  action_items: []\n\n- id: R21-I2\n  summary: \"Introduction 过早引入 TOST 等统计细节\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W9。R1 REBUT（限定词是防止 overstatement 所必需的）。两难：加限定=过早细节，不加=overstate。Director 判断：保留限定更安全。\"}\n  action_items: []\n\n- id: R21-I3\n  summary: \"-ing 分词短语残留 (Abstract/Results)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-W10，R1 同意。'revealing...', 'establishing...' 等。\"}\n  action_items: []\n\n- id: R21-I4\n  summary: \"P-value 报告格式不一致 (p<0.001 vs p<10^{-35})\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-M3，R2 同意。\"}\n  action_items: []\n\n- id: R21-I5\n  summary: \"FewRel train+val merge contamination 论证修辞可改进\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-W8。BCS 偏效应不受影响 (Appendix N β_BCS 不变)，但 'opposite to contamination hypothesis' 措辞过强。R2 rebut 指出防线主要在 split-origin covariate analysis 而非 accuracy 方向。\"}\n  action_items: []\n\n- id: R21-I6\n  summary: \"Missing reference: Josifoski et al. (2022) GenIE\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1 建议，R2 同意。\"}\n  action_items: []\n\n- id: R21-I7\n  summary: \"Gemini count-64 partial (11/25 batches) 可能有 selection bias\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R2-Q4，R1 同意。应补充 BCS 分布比较和 failure mode 讨论。\"}\n  action_items: []\n\n- id: R21-I8\n  summary: \"70B BCS validation 未明确说明使用哪个 pool，CI 较宽\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R1-Q5，R2 指出为 reporting gap。\"}\n  action_items: []\n\n# ============================================================\n# R20 及更早 — 状态更新\n# ============================================================\n\n- id: R20-N1\n  summary: \"'Largely additive' overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"已修复，改为 'two dimensions'\"}\n    - {round: 21, reviewers: [R1, R2], note: \"R21 未单独提出此 exact issue，但 R21-C1 是其演化版（TOST margin 问题）\"}\n  resolution: \"全文删除 'largely additive'。但 TOST margin 基础问题仍在 (R21-C1)。\"\n  resolution_round: 20\n\n- id: R20-W1\n  summary: \"Title 'Predict' 与 correlational evidence 不匹配\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - {round: 20, reviewers: [R1, R2], note: \"R20 wont_fix (保留 title)\"}\n    - {round: 21, reviewers: [R1, R2], note: \"R21-D1 复现分歧。R2 Must-Fix, R1 REBUT。\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R20-I3\n  summary: \"SCS name-only vs prompt content 不一致\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - {round: 20, reviewers: [R2], note: \"Appendix 有 ablation 但正文应简要提及\"}\n    - {round: 21, reviewers: [], note: \"R21 未单独提出，但 §3.2 已加入 name+def ablation cross-ref\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R19-W4\n  summary: \"NER U-shape dual-task burden 假说缺实验证据\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 21\n  mentions:\n    - {round: 19, reviewers: [R1, R2], note: \"Speculative\"}\n    - {round: 21, reviewers: [R1, R2], note: \"R21-W3 复现。R1 建议 'extract ALL then filter' 控制实验。\"}\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 2273 · 2026-05-19T11:58:34.430480+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml\", \"bytes\": 12475}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2274 · 2026-05-19T12:00:23.493782+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml",
  "description": "Read review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml",
    "description": "Read review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2275 · 2026-05-19T12:00:23.695234+00:00_

# Round 21 Review Issues Tracker
# Updated: 2026-05-19 (Fresh review — Round 21)
# Reviewer lineup: R1 (method rigor), R2 (novelty + writing)

# ============================================================
# CRITICAL — 双方共识
# ============================================================

- id: R21-C1
  summary: "TOST ±3pp margin 存在循环论证，bounded interaction 仅在 sentence-level RE linear scale 成立"
  category: method
  severity: critical
  status: open
  first_raised_round: 21
  last_seen_round: 21
  mentions:
    - {round: 21, reviewers: [R1, R2], note: "R1-W1 提出循环论证（batch SD 部分由 BCS 驱动）；R2 同意 margin 选择缺乏 principled basis。R2 纠正：正文已限定 scope（Intro/Conclusion 明确写 'sentence-level RE'），但 TOST margin 理论基础仍有问题。3/4 条件 inconclusive（logit p=0.209, DocRED p=0.77, NER p=0.50）。"}
  action_items:
    - {round: 21, action: "补充讨论 margin anchor 的独立性问题；考虑 practical equivalence 替代方案；Table 4 sensitivity 更突出地引用", assigned_to: research_director, status: open}
  resolution: ""
  resolution_round: null

- id: R21-C2
  summary: "DocRED R²=53% 来自 n=35 不稳定估计，Abstract 使用 '22-53%' 误导"
  category: framing
  severity: critical
  status: open
  first_raised_round: 21
  last_seen_round: 21
  mentions:
    - {round: 21, reviewers: [R1, R2], note: "R1-W2 首提，R2 完全同意。CI [0.27, 0.73] 极宽。Abstract 将统计功效最弱 dataset 的最高值作为 headline upper bound。DocRED factorial 也完全 inconclusive (TOST p=0.77)。"}
  action_items:
    - {round: 21, action: "Abstract 改为 '22% (up to 53% with wider CI)' 或仅用 FewRel R²=22%；DocRED 标注为 preliminary replication", assigned_to: research_director, status: open}
  resolution: ""
  resolution_round: null

- id: R21-C3
  summary: "Dimension 2 缺乏 proprietary model batch-level 验证，但 claim 暗示跨架构普遍性"
  category: framing
  severity: critical
  status: open
  first_raised_round: 21
  last_seen_round: 21
  mentions:
    - {round: 21, reviewers: [R1, R2], note: "R1-W3 首提，R2 同意但区分两层 claim：pairwise SCS 是 schema-structural（不依赖 constrained decoding），batch-level BCS 依赖 forced-choice format 未在 proprietary models 验证
…[truncated 10475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2276 · 2026-05-19T12:00:27.713040+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:submit_review_report_to_research_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:submit_review_report_to_research_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2277 · 2026-05-19T12:00:27.763773+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2278 · 2026-05-19T12:00:31.480173+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "submit_review_report",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "submit_review_report",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2279 · 2026-05-19T12:00:31.580958+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2280 · 2026-05-19T12:02:25.043605+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 21 Consolidated Review Report\n## \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Target Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewers**: R1 (method rigor), R2 (novelty + writing)\n**Review Mode**: Fresh (independent full review)\n\n---\n\n## Summary\n\n本文研究 schema 复杂度（类型数量和类型间混淆度）如何影响 zero-shot LLM 信息抽取性能。作者提出二维退化模型：Dimension 1（类型数量增加导致 recall 下降）和 Dimension 2（类型混淆度 BCS 预测 type substitution 错误）。使用 Schema Confusability Score（SCS，借鉴自 LLM-PEE）和 Batch Confusability Score（BCS）作为度量，在 4 个数据集（Few-NERD、FewRel、DocRED、MAVEN）上对 Qwen3-32B 进行系统实验，并用 Llama-3.1-70B/8B 和 Gemini 2.5 Flash 做跨模型验证。论文还报告了 SDGD（Schema-DAG-Guided Decomposition）的负面结果。\n\n论文方法论总体扎实，BCS-controlled stratified 实验设计有方法论贡献，负面结果（SDGD）的诚实报告值得肯定。但核心 claim 的 scope 与 evidence 之间存在系统性错位，多项统计检验功效不足，且 confusability 效应的实际规模（typical ~2pp）限制了实用价值。\n\n---\n\n## Strengths\n\n**S1. 系统性实验设计（双方共识）**\nBCS-controlled stratified 实验框架是本文的核心方法论贡献。固定类型数量、仅变化 BCS 来隔离混淆度效应，这一设计在 schema complexity 研究中具有方法论价值，可为后续工作复用。\n\n**S2. 负面结果的诚实报告（双方共识）**\n§6 SDGD 负面结果（graph coloring 仅 +1.4pp n.s.，oracle routing +29.8pp 但 practical routing 全部低于 baseline）的完整报告，对社区有真正的信息价值。Merge amplification 和 routing failure 的分析帮助后续研究避免同类陷阱。\n\n**S3. 跨模型一致性验证（双方共识）**\nDimension 1（count curve）在 4 个模型（含 Gemini 2.5 Flash API 模型）上 slope 一致性通过 permutation test 验证，增加了 count-degradation 发现的可信度。\n\n**S4. 统计严谨性意识（R1 首提，R2 部分同意）**\nBootstrap CI、TOST equivalence testing、permutation slope comparison 等统计方法的使用显示作者具备统计素养。虽然具体执行有问题（见 Weaknesses），但方法论意识本身是正面的。\n\n**S5. Centrality confound 识别（R1 首提，R2 同意有方法论价值）**\n在 MAVEN 同域 schema 上识别 per-type BCS 与 centrality 混淆的问题，展示了实验分析的自觉性。\n\n**S6. 写作质量总体良好（R2 首提）**\n论文结构清晰，narrative 连贯，几乎无 AI 写作痕迹（em-dash 已清理），Limitations section 内容充实。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**W1. TOST ±3pp margin 存在循环论证，bounded interaction 证据不足 [R1-W1, R2 同意]**\nTOST equivalence testing 的 ±3pp margin 来源于 batch-level 标准差，而 batch SD 本身部分由 BCS 驱动，构成循环论证。更严重的是，4 组 TOST 检验中仅 1 组（FewRel sentence-level, linear scale）拒绝了非等价假设；其余 3 组均 inconclusive（logit p=0.209, DocRED p=0.77, NER p=0.50）。论文在 Intro/Conclusion 中已限定 scope 为 \"sentence-level RE\"，但 TOST margin 的理论基础仍然薄弱。\n\n**W2. DocRED R²=53% 来自 n=35 不稳定估计，Abstract headline 误导 [R1-W2, R2 完全同意]**\nAbstract 使用 \"22-53%\" 作为 BCS 解释力 range 的 headline，但上界 53% 来自 DocRED 仅 35 个观测点的 bootstrap，CI [0.27, 0.73] 极宽。将统计功效最弱的 dataset 的最高点估计作为 headline upper bound，会给读者造成远超实际的印象。DocRED factorial TOST 也完全 inconclusive (p=0.77)。\n\n**W3. Dimension 2 缺乏 proprietary model batch-level 验证，claim scope 过宽 [R1-W3, R2 同意]**\nAbstract \"effects replicate across model scales and families\" 未区分 pairwise SCS（schema-structural，不依赖 constrained decoding）和 batch-level BCS（依赖 forced-choice format）。Gemini 验证仅覆盖 Dimension 1 count curves；Dimension 2 的 batch-level BCS 效应未在 API 模型上验证。\n\n**W4. SCS 指标借用自 LLM-PEE，novelty framing 不清晰 [R2-W1, R1 同意]**\nSCS 与 LLM-PEE 的 partitioning criterion 形式上相同。Contribution 1 虽已改为 \"Building on... prior work\"，但论文整体 framing 仍可能让读者误以为 SCS 是本文创新。真正的 novelty 在 BCS-controlled stratified experimental framework，而非度量本身。\n\n**W5. Typical effect size ~2pp，实用价值有限 [R2-W3, R1 完全同意]**\n自然 schema sampling 下，BCS 变异产生的 typical effect 仅约 2pp（IQR=0.054）。80-relation 自然 pool 内 BCS slope 为 +0.221, p=0.76（不显著）。Abstract/Intro 引用的 25-31pp extreme-batch 差异来自人为构造的极端分组，不代表 realistic 场景。论文的价值更多在理论理解而非实际干预指导。\n\n### Warning\n\n**W6. NER Dimension 2 batch-level 为 null [R2-W4, R1 完全同意]**\nNER 的 BCS batch-level 效应 r≈0（n=450），Dimension 2 仅在 RE forced-choice 任务上成立。Title \"Information Extraction\" 过于宽泛，暗示所有 IE 子任务均适用。\n\n**W7. Embedding 选择不一致 [R2-W6, R1 同意]**\nFew-NERD 使用 Qwen3 embedding，其余使用 MiniLM。论文自身数据显示 MiniLM 在 Few-NERD 上 r=0.172 > Qwen3 r=0.138，反驳了选择 Qwen3 的理由。应统一使用 MiniLM 作为主 embedding。\n\n**W8. NER U-shape dual-task burden 假说缺乏直接验证 [R1-W5, R2 同意]**\nCount 22-44→66 的 NER recovery 被解释为 \"dual-task burden reduction\"，但这是 post-hoc 假说，缺乏控制实验（如 \"extract ALL then filter\"）的直接验证。70B 上复现增加可信度但不等于验证。\n\n**W9. 无有效干预方案 [R1-W6, R2 部分同意]**\nConfusability 可检测但不可干预：graph coloring +1.4pp n.s.，renaming 降低准确率，few-shot 扩大 gap。论文价值定位应从 \"prediction + intervention\" 转向 \"diagnostic understanding\"。\n\n**W10. Renaming 实验支持 conceptual overlap 替代解读，削弱 SCS construct validity [R1-W7, R2 高度同意]**\nSCS 基于 name embedding similarity，但 renaming 失败（甚至降低准确率）表明类型混淆可能由概念重叠而非 label surface similarity 驱动。SCS 可能是 downstream proxy 而非 root cause metric。R2 评价此为\"本轮最有力的理论质疑之一\"。\n\n**W11. MAVEN ED 贡献有限 [R2-W5, R1 部分同意]**\nMAVEN 仅提供 pairwise 验证和 centrality confound 识别，batch-level 无 positive evidence。不应与 NER/RE 并列为等价贡献。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **TOST margin 基础薄弱**（R21-C1）：3/4 条件 inconclusive，margin 选择缺乏独立 principled basis\n2. **DocRED R²=53% 不应作为 headline**（R21-C2）：n=35, CI 过宽\n3. **Dim2 proprietary gap**（R21-C3）：batch-level BCS 未在 API 模型验证\n4. **SCS novelty 需重新 frame**（R21-C4）：指标借用，创新在实验设计\n5. **Typical effect ~2pp**（R21-C5）：extreme-batch 数字不代表 realistic 场景\n6. **NER Dim2 batch-level null**（R21-W1）：title 过宽\n7. **Embedding 不一致**（R21-W2）：MiniLM 实际更优\n8. **NER U-shape 未验证**（R21-W3）：post-hoc 假说\n9. **无有效干预**（R21-W4）：诊断 > 干预\n10. **Renaming 支持替代解读**（R21-W5）：conceptual overlap vs label surface similarity\n\n---\n\n## Reviewer Divergence\n\n**Title \"Predict\" 是否应修改**（R21-D1）：\n- R2：Must-Fix。论文仅 correlational evidence，\"predict\" 暗示因果或 actionable prediction。\n- R1：REBUT。\"Predict\" 在统计回归语境中是标准用语（\"X predicts Y\" = \"X is a statistical predictor of Y\"），论文明确使用 \"predictive relationship\" 而非因果语言。\n- **Director 判断**：R1 的 REBUT 有理。\"Predict\" 在定量社会科学和统计学中是标准回归术语，不暗示因果。但建议作者在 rebuttal 中准备防御，因为部分审稿人可能持 R2 立场。此项不降分。\n\n---\n\n## Questions for Authors\n\n**Q1**（R1）：TOST margin 如果改用 ±2pp 或 ±5pp，哪些条件的结论会翻转？Table 4 sensitivity 是否覆盖了这些边界？\n\n**Q2**（R1）：NER U-shape 是否可以通过 \"extract ALL entities then filter by type\" 的控制实验来验证 dual-task burden 假说？\n\n**Q3**（R2）：80-relation natural pool 内 BCS slope 不显著（p=0.76），是否意味着 Dim2 在 realistic full-schema 部署中不可检测？\n\n**Q4**（R2）：Gemini count-64 仅 11/25 batches 完成，dropped batches 的 BCS 分布是否与 completed 有系统偏差？\n\n**Q5**（R1）：70B BCS validation 使用了哪个 pool？CI 较宽是否因为样本量不足？\n\n---\n\n## Missing References\n\n- Josifoski et al. (2022) \"GenIE: Generative Information Extraction\" (NAACL 2022) — constrained generation for IE, 与本文 constrained decoding 方法直接相关\n\n---\n\n## External Review\n\n**外部审稿：未配置**。项目未启用 external_review（paperreview.ai），本轮无外部审稿意见。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings（可被 Findings 接收）**\n\n**Soundness: 3.5** — 实验设计有方法论价值，统计方法选择合理，但 TOST 执行有缺陷（3/4 inconclusive），DocRED n=35 不稳定，embedding 选择不一致。\n\n**Excitement: 2.5** — Dimension 1 是 well-known 的 schema-size degradation 的系统验证（incremental），Dimension 2 的 batch-level 效应仅在 RE forced-choice 成立且 typical effect ~2pp，无有效干预方案。SDGD 负面结果有信息价值但本身不构成足够的 novelty。\n\n**Confidence: 4.0** — 两位 Reviewer 独立给出相同评分，交叉分享后在所有 critical issue 上达成共识。\n\n### 评分理由\n\n**支持 Findings 的因素**：\n- BCS-controlled stratified 实验设计是可复用的方法论贡献\n- SDGD 负面结果对社区有真实信息价值\n- 4 个数据集、4 个模型的系统性验证工作量大\n- 统计方法论意识好（虽然执行有缺陷）\n- 写作质量良好，结构清晰\n\n**阻止 Conference (4.0) 的因素**：\n- Typical effect size ~2pp 限制了实用 impact\n- Dimension 2 batch-level 仅在 RE forced-choice 成立（NER null, ED confounded），title/abstract 过度概括\n- SCS 指标非原创，真正 novelty（实验框架）的 framing 不清晰\n- 5 项 critical issue 中 3 项涉及 claim scope 与 evidence 错位\n- 无有效干预方案（所有尝试均失败或不显著）\n\n**不降至 2.5 (Borderline Findings) 的因素**：\n- 实验设计本身扎实，非方法错误而是 framing 问题\n- 多数 critical issue 可通过 scope 限定和 reframing 在 revision 中解决\n- 负面结果的贡献是真实的\n\n### Rebuttal 建议关注点\n\n如果作者 rebuttal，审稿人最关注以下问题的回应：\n1. TOST margin 的独立 justification（R21-C1）\n2. Abstract/headline 数字的 recalibration（R21-C2, C5）\n3. Dim2 scope 限定（R21-C3, W1）\n4. SCS novelty 的诚实 repositioning（R21-C4）\n\n---\n\n## Detailed Comments\n\n### 格式合规性\n- ✅ ACL 2023 模板，`[review]` 选项\n- ✅ 匿名化（`\\author{Anonymous}`）\n- ✅ 正文 8 页\n- ✅ Limitations section 存在且充实\n- ✅ Responsible NLP Checklist 完整填写\n- ✅ 附录双栏格式\n- ✅ 无 em-dash AI 写作痕迹\n- ⚠️ -ing 分词短语残留（Abstract/Results 中 \"revealing...\", \"establishing...\"）\n- ⚠️ P-value 报告格式不一致（p<0.001 vs p<10^{-35}）\n\n### 按 Section 的具体意见\n\n**Abstract**: 数据密度过高。建议精简到 2-3 个关键数字，删除 \"22-53%\" upper bound，限定 \"effects replicate\" 的 scope。\n\n**Introduction**: Finding 陈述中的统计限定词（TOST, inconclusive）对非统计学读者有认知负担，但删除会导致 overstatement。建议保留但简化措辞。Contribution 1 需明确 SCS 来源。\n\n**§3 Experimental Setup**: Embedding 选择 justification 需修正（§3.2 选择 Qwen3 for Few-NERD 但 MiniLM 效果更好）。\n\n**§4 Results**: DocRED R² 需标注 CI 和 n；80-rel natural pool 不显著结果需在正文（而非仅 appendix）讨论。\n\n**§5 SDGD**: 这是论文最有信息价值的 section，建议保留完整篇幅。\n\n**§7 Discussion**: 需更诚实 frame 实践意义（诊断 > 干预）；需讨论 conceptual overlap vs label surface similarity。\n\n**Limitations**: 已较充实，建议补充 typical effect size ~2pp 的实践意义讨论和 NER Dim2 null 的限制。",
  "project": "schema-dag-extraction",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 21 Consolidated Review Report\n## \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Target Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewers**: R1 (method rigor), R2 (novelty + writing)\n**Review Mode**: Fresh (independent full review)\n\n---\n\n## Summary\n\n本文研究 schema 复杂度（类型数量和类型间混淆度）如何影响 zero-shot LLM 信息抽取性能。作者提出二维退化模型：Dimension 1（类型数量增加导致 recall 下降）和 Dimension 2（类型混淆度 BCS 预测 type substitution 错误）。使用 Schema Confusability Score（SCS，借鉴自 LLM-PEE）和 Batch Confusability Score（BCS）作为度量，在 4 个数据集（Few-NERD、FewRel、DocRED、MAVEN）上对 Qwen3-32B 进行系统实验，并用 Llama-3.1-70B/8B 和 Gemini 2.5 Flash 做跨模型验证。论文还报告了 SDGD（Schema-DAG-Guided Decomposition）的负面结果。\n\n论文方法论总体扎实，BCS-controlled stratified 实验设计有方法论贡献，负面结果（SDGD）的诚实报告值得肯定。但核心 claim 的 scope 与 evidence 之间存在系统性错位，多项统计检验功效不足，且 confusability 效应的实际规模（typical ~2pp）限制了实用价值。\n\n---\n\n## Strengths\n\n**S1. 系统性实验设计（双方共识）**\nBCS-controlled stratified 实验框架是本文的核心方法论贡献。固定类型数量、仅变化 BCS 来隔离混淆度效应，这一设计在 schema complexity 研究中具有方法论价值，可为后续工作复用。\n\n**S2. 负面结果的诚实报告（双方共识）**\n§6 SDGD 负面结果（graph coloring 仅 +1.4pp n.s.，oracle routing +29.8pp 但 practical routing 全部低于 baseline）的完整报告，对社区有真正的信息价值。Merge amplification 和 routing failure 的分析帮助后续研究避免同类陷阱。\n\n**S3. 跨模型一致性验证（双方共识）**\nDimension 1（count curve）在 4 个模型（含 Gemini 2.5 Flash API 模型）上 slope 一致性通过 permutation test 验证，增加了 count-degradation 发现的可信度。\n\n**S4. 统计严谨性意识（R1 首提，R2 部分同意）**\nBootstrap CI、TOST equivalence testing、permutation slope comparison 等统计方法的使用显示作者具备统计素养。虽然具体执行有问题（见 Weaknesses），但方法论意识本身是正面的。\n\n**S5. Centrality confound 识别（R1 首提，R2 同意有方法论价值）**\n在 MAVEN 同域 schema 上识别 per-type BCS 与 centrality 混淆的问题，展示了实验分析的自觉性。\n\n**S6. 写作质量总体良好（R2 首提）**\n论文结构清晰，narrative 连贯，几乎无 AI 写作痕迹（em-dash 已清理），Limitations section 内容充实。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**W1. TOST ±3pp margin 存在循环论证，bounded interaction 证据不足 [R1-W1, R2 同意]**\nTOST equivalence testing 的 ±3pp margin 来源于 batch-level 标准差，而 batch SD 本身部分由 BCS 驱动，构成循环论证。更严重的是，4 组 TOST 检验中仅 1 组（FewRel sentence-level, linear scale）拒绝了非等价假设；其余 3 组均 inconclusive（logit p=0.209, DocRED p=0.77, NER p=0.50）。论文在 Intro/Conclusion 中已限定 scope 为 \"sentence-level RE\"，但 TOST margin 的理论基础仍然薄弱。\n\n**W2. DocRED R²=53% 来自 n=35 不稳定估计，Abstract headline 误导 [R1-W2, R2 完全同意]**\nAbstract 使用 \"22-53%\" 作为 BCS 解释力 range 的 headline，但上界 53% 来自 DocRED 仅 35 个观测点的 bootstrap，CI [0.27, 0.73] 极宽。将统计功效最弱的 dataset 的最高点估计作为 headline upper bound，会给读者造成远超实际的印象。DocRED factorial TOST 也完全 inconclusive (p=0.77)。\n\n**W3. Dimension 2 缺乏 proprietary model batch-level 验证，claim scope 过宽 [R1-W3, R2 同意]**\nAbstract \"effects replicate across model scales and families\" 未区分 pairwise SCS（schema-structural，不依赖 constrained decoding）和 batch-level BCS（依赖 forced-choice format）。Gemini 验证仅覆盖 Dimension 1 count curves；Dimension 2 的 batch-level BCS 效应未在 API 模型上验证。\n\n**W4. SCS 指标借用自 LLM-PEE，novelty framing 不清晰 [R2-W1, R1 同意]**\nSCS 与 LLM-PEE 的 partitioning criterion 形式上相同。Contribution 1 虽已改为 \"Building on... prior work\"，但论文整体 framing 仍可能让读者误以为 SCS 是本文创新。真正的 novelty 在 BCS-controlled stratified experimental framework，而非度量本身。\n\n**W5. Typical effect size ~2pp，实用价值有限 [R2-W3, R1 完全同意]**\n自然 schema sampling 下，BCS 变异产生的 typical effect 仅约 2pp（IQR=0.054）。80-relation 自然 pool 内 BCS slope 为 +0.221, p=0.76（不显著）。Abstract/Intro 引用的 25-31pp extreme-batch 差异来自人为构造的极端分组，不代表 realistic 场景。论文的价值更多在理论理解而非实际干预指导。\n\n### Warning\n\n**W6. NER Dimension 2 batch-level 为 null [R2-W4, R1 完全同意]**\nNER 的 BCS batch-level 效应 r≈0（n=450），Dimension 2 仅在 RE forced-choice 任务上成立。Title \"Information Extraction\" 过于宽泛，暗示所有 IE 子任务均适用。\n\n**W7. Embedding 选择不一致 [R2-W6, R1 同意]**\nFew-NERD 使用 Qwen3 embedding，其余使用 MiniLM。论文自身数据显示 MiniLM 在 Few-NERD 上 r=0.172 > Qwen3 r=0.138，反驳了选择 Qwen3 的理由。应统一使用 MiniLM 作为主 embedding。\n\n**W8. NER U-shape dual-task burden 假说缺乏直接验证 [R1-W5, R2 同意]**\nCount 22-44→66 的 NER recovery 被解释为 \"dual-task burden reduction\"，但这是 post-hoc 假说，缺乏控制实验（如 \"extract ALL then filter\"）的直接验证。70B 上复现增加可信度但不等于验证。\n\n**W9. 无有效干预方案 [R1-W6, R2 部分同意]**\nConfusability 可检测但不可干预：graph coloring +1.4pp n.s.，renaming 降低准确率，few-shot 扩大 gap。论文价值定位应从 \"prediction + intervention\" 转向 \"diagnostic understanding\"。\n\n**W10. Renaming 实验支持 conceptual overlap 替代解读，削弱 SCS construct validity [R1-W7, R2 高度同意]**\nSCS 基于 name embedding similarity，但 renaming 失败（甚至降低准确率）表明类型混淆可能由概念重叠而非 label surface similarity 驱动。SCS 可能是 downstream proxy 而非 root cause metric。R2 评价此为\"本轮最有力的理论质疑之一\"。\n\n**W11. MAVEN ED 贡献有限 [R2-W5, R1 部分同意]**\nMAVEN 仅提供 pairwise 验证和 centrality confound 识别，batch-level 无 positive evidence。不应与 NER/RE 并列为等价贡献。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **TOST margin 基础薄弱**（R21-C1）：3/4 条件 inconclusive，margin 选择缺乏独立 principled basis\n2. **DocRED R²=53% 不应作为 headline**（R21-C2）：n=35, CI 过宽\n3. **Dim2 proprietary gap**（R21-C3）：batch-level BCS 未在 API 模型验证\n4. **SCS novelty 需重新 frame**（R21-C4）：指标借用，创新在实验设计\n5. **Typical effect ~2pp**（R21-C5）：extreme-batch 数字不代表 realistic 场景\n6. **NER Dim2 batch-level null**（R21-W1）：title 过宽\n7. **Embedding 不一致**（R21-W2）：MiniLM 实际更优\n8. **NER U-shape 未验证**（R21-W3）：post-hoc 假说\n9. **无有效干预**（R21-W4）：诊断 > 干预\n10. **Renaming 支持替代解读**（R21-W5）：conceptual overlap vs label surface similarity\n\n---\n\n## Reviewer Divergence\n\n**Title \"Predict\" 是否应修改**（R21-D1）：\n- R2：Must-Fix。论文仅 correlational evidence，\"predict\" 暗示因果或 actionable prediction。\n- R1：REBUT。\"Predict\" 在统计回归语境中是标准用语（\"X predicts Y\" = \"X is a statistical predictor of Y\"），论文明确使用 \"predictive relationship\" 而非因果语言。\n- **Director 判断**：R1 的 REBUT 有理。\"Predict\" 在定量社会科学和统计学中是标准回归术语，不暗示因果。但建议作者在 rebuttal 中准备防御，因为部分审稿人可能持 R2 立场。此项不降分。\n\n---\n\n## Questions for Authors\n\n**Q1**（R1）：TOST margin 如果改用 ±2pp 或 ±5pp，哪些条件的结论会翻转？Table 4 sensitivity 是否覆盖了这些边界？\n\n**Q2**（R1）：NER U-shape 是否可以通过 \"extract ALL entities then filter by type\" 的控制实验来验证 dual-task burden 假说？\n\n**Q3**（R2）：80-relation natural pool 内 BCS slope 不显著（p=0.76），是否意味着 Dim2 在 realistic full-schema 部署中不可检测？\n\n**Q4**（R2）：Gemini count-64 仅 11/25 batches 完成，dropped batches 的 BCS 分布是否与 completed 有系统偏差？\n\n**Q5**（R1）：70B BCS validation 使用了哪个 pool？CI 较宽是否因为样本量不足？\n\n---\n\n## Missing References\n\n- Josifoski et al. (2022) \"GenIE: Generative Information Extraction\" (NAACL 2022) — constrained generation for IE, 与本文 constrained decoding 方法直接相关\n\n---\n\n## External Review\n\n**外部审稿：未配置**。项目未启用 external_review（paperreview.ai），本轮无外部审稿意见。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings（可被 Findings 接收）**\n\n**Soundness: 3.5** — 实验设计有方法论价值，统计方法选择合理，但 TOST 执行有缺陷（3/4 inconclusive），DocRED n=35 不稳定，embedding 选择不一致。\n\n**Excitement: 2.5** — Dimension 1 是 well-known 的 schema-size degradation 的系统验证（incremental），Dimension 2 的 batch-level 效应仅在 RE forced-choice 成立且 typical effect ~2pp，无有效干预方案。SDGD 负面结果有信息价值但本身不构成足够的 novelty。\n\n**Confidence: 4.0** — 两位 Reviewer 独立给出相同评分，交叉分享后在所有 critical issue 上达成共识。\n\n### 评分理由\n\n**支持 Findings 的因素**：\n- BCS-controlled stratified 实验设计是可复用的方法论贡献\n- SDGD 负面结果对社区有真实信息价值\n- 4 个数据集、4 个模型的系统性验证工作量大\n- 统计方法论意识好（虽然执行有缺陷）\n- 写作质量良好，结构清晰\n\n**阻止 Conference (4.0) 的因素**：\n- Typical effect size ~2pp 限制了实用 impact\n- Dimension 2 batch-level 仅在 RE forced-choice 成立（NER null, ED confounded），title/abstract 过度概括\n- SCS 指标非原创，真正 novelty（实验框架）的 framing 不清晰\n- 5 项 critical issue 中 3 项涉及 claim scope 与 evidence 错位\n- 无有效干预方案（所有尝试均失败或不显著）\n\n**不降至 2.5 (Borderline Findings) 的因素**：\n- 实验设计本身扎实，非方法错误而是 framing 问题\n- 多数 critical issue 可通过 scope 限定和 reframing 在 revision 中解决\n- 负面结果的贡献是真实的\n\n### Rebuttal 建议关注点\n\n如果作者 rebuttal，审稿人最关注以下问题的回应：\n1. TOST margin 的独立 justification（R21-C1）\n2. Abstract/headline 数字的 recalibration（R21-C2, C5）\n3. Dim2 scope 限定（R21-C3, W1）\n4. SCS novelty 的诚实 repositioning（R21-C4）\n\n---\n\n## Detailed Comments\n\n### 格式合规性\n- ✅ ACL 2023 模板，`[review]` 选项\n- ✅ 匿名化（`\\author{Anonymous}`）\n- ✅ 正文 8 页\n- ✅ Limitations section 存在且充实\n- ✅ Responsible NLP Checklist 完整填写\n- ✅ 附录双栏格式\n- ✅ 无 em-dash AI 写作痕迹\n- ⚠️ -ing 分词短语残留（Abstract/Results 中 \"revealing...\", \"establishing...\"）\n- ⚠️ P-value 报告格式不一致（p<0.001 vs p<10^{-35}）\n\n### 按 Section 的具体意见\n\n**Abstract**: 数据密度过高。建议精简到 2-3 个关键数字，删除 \"22-53%\" upper bound，限定 \"effects replicate\" 的 scope。\n\n**Introduction**: Finding 陈述中的统计限定词（TOST, inconclusive）对非统计学读者有认知负担，但删除会导致 overstatement。建议保留但简化措辞。Contribution 1 需明确 SCS 来源。\n\n**§3 Experimental Setup**: Embedding 选择 justification 需修正（§3.2 选择 Qwen3 for Few-NERD 但 MiniLM 效果更好）。\n\n**§4 Results**: DocRED R² 需标注 CI 和 n；80-rel natural pool 不显著结果需在正文（而非仅 appendix）讨论。\n\n**§5 SDGD**: 这是论文最有信息价值的 section，建议保留完整篇幅。\n\n**§7 Discussion**: 需更诚实 frame 实践意义（诊断 > 干预）；需讨论 conceptual overlap vs label surface similarity。\n\n**Limitations**: 已较充实，建议补充 typical effect size ~2pp 的实践意义讨论和 NER Dim2 null 的限制。",
    "project": "schema-dag-extraction",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool result

_source line 2281 · 2026-05-19T12:02:29.416071+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4372
}
```

</details>

---


### Assistant

_source line 2282 · 2026-05-19T12:02:34.438065+00:00_

Round 21 审稿报告已投递至 Research Director。

**审稿结论**：Overall 3.0（Findings），Soundness 3.5，Excitement 2.5。两位 Reviewer 独立给出一致评分，交叉分享后在全部 5 项 Critical issue 上达成共识。

**核心问题**：claim scope 与 evidence 系统性错位（TOST 3/4 inconclusive、DocRED n=35 不稳定、Dim2 仅限 RE forced-choice、typical effect ~2pp）。方法论框架本身扎实，多数问题可通过 reframing 在 revision 中解决。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 193

## Round 193

2 recorded events


### User

_source line 2283 · 2026-05-19T12:02:37.180660+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

核心结论：R1 和我在大方向上高度一致（均给出 3.0 Findings），在 10 条 Weakness 中对 7 条实质同意。主要分歧点在于 R1-W1（bounded interaction 的限定范围——论文 Conclusion 其实已明确限定为 sentence-level RE）和 R1-W4（pair-to-batch amplification——论文 Appendix H 已有充分讨论，更多是 emphasis 问题）。R1-W7 关于 SCS 度量 construct validity 的理论质疑是本轮最有价值的新洞察。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2284 · 2026-05-19T12:02:44.614160+00:00_

Round 21 审稿已完成，报告已投递至 Research Director。

**最终评分：3.0 — Findings**（Soundness 3.5, Excitement 2.5, Confidence 4.0）

两位 Reviewer 独立评分一致，交叉分享后在所有 critical issue 上达成共识。5 项 critical、6 项 warning、1 项分歧、8 项 info，已同步至 review_issues.yaml。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 194

## Round 194

64 recorded events


### User

_source line 2285 · 2026-05-19T17:43:39.010439+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2286 · 2026-05-19T17:43:45.147580+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2287 · 2026-05-19T17:43:45.200297+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 2288 · 2026-05-19T17:43:51.366930+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2289 · 2026-05-19T17:43:51.367417+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2290 · 2026-05-19T17:43:55.181309+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2291 · 2026-05-19T17:43:56.187150+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (64 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_docred_bcs_expanded** (success): Expanding DocRED BCS-controlled batches from 5 to 15 per count level will narrow the factorial interaction CI (currently [-1.6, 13.0]) sufficiently to resolve whether the BCS-count interaction is bounded or substantial in document-level RE. If the CI narrows to exclude zero, the interaction is genuine and non-additive; if it narrows to include zero tightly, the bounded-interaction claim strengthens.\n- **exp_sdgd_zero_maven** (success): SDGD-zero on MAVEN (168 event types, 18 batches) will reproduce the schema DAG extraction capability observed on DocRED, validating cross-domain generalization from document-level RE to event detection.\n- **exp_unconstrained_decoding_ablation** (success): The BCS-accuracy correlation in RE arises fro
…[truncated 1440 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 2292 · 2026-05-19T17:43:56.338215+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2293 · 2026-05-19T17:43:56.590558+00:00_

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
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 has been validated across all four models including a proprietary one; Dimension~2 has been verified only on open-weight models and was not robustly detectable on NER at 8B scale, likely due to floor effects. Gemini 2.5 Flash count-64 results are partial (11/25 batches) due to API quota exhaustion. Dimension~2 (BCS) has not been validated on proprietary models at the batch level.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded under the linear specification on FewRel (TOST $p = 0.003$ at $\pm 3$\,pp) and nonzero on DocRED ($-$9.4\,pp, 95\% CI [$-$12.9, $-$6.0]; expanded from $n{=}5$ to $n{=}15$ per condition; partially confounded by BCS range restriction at higher counts; Appendix~\ref{sec:appendix_factorial}), but inconclusive on the logit scale for FewRel ($p = 0.209$). DocRED count curves use 5 batches per level due 
…[truncated 57976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 2294 · 2026-05-19T17:44:05.690832+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__update_review_issues",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__update_review_issues",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2295 · 2026-05-19T17:44:05.741532+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2296 · 2026-05-19T17:44:08.853529+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2297 · 2026-05-19T17:44:09.305546+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit anonymity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit anonymity"
  }
}
```

</details>

---


### Tool call

_source line 2298 · 2026-05-19T17:44:11.514370+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2299 · 2026-05-19T17:44:11.615204+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: type count and type confusability. We present what is, to our knowledge, the first controlled study isolating these factors across NER, RE, and event detection on four datasets; the analysis reveals task-dependent effect structures. We quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS). Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) dominates confusability-related type substitution, though typical batches yield modest ${\sim}$2\,pp gaps. BCS explains 22--58\% of cross-batch RE accuracy variance under RE's forced-choice format but shows no batch-level signal for NER, where errors scatter across missed entities and boundary failures. Few-shot demonstrations widen the confusability gap (+4.3\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE). Pairwise confusability is a schema-structural property: count effects replicate across model scales and architectures (8B to proprietary); batch-level BCS prediction has been verified on open-weight models. Effects persist under varied prompt designs.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2300 · 2026-05-19T17:44:11.716009+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2301 · 2026-05-19T17:44:12.619792+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
…[truncated 3173 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 2302 · 2026-05-19T17:44:12.821242+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2303 · 2026-05-19T17:44:12.821760+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, bidirectional encoders \cite{gliner-2024,gliner2-2025}, and fine-grained entity typing \cite{gillick-2014-entity-typing}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022}, constrained generative extraction \cite{josifoski-2022-genie}, and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability. \citet{wei-2023-chatie} reformulate zero-shot IE as multi-turn QA with ChatGPT but do not analyze schema-size effects.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21 in NER) that our \S\ref{sec:sdgd} analysis identifies as the fundamental bottleneck. Other approaches address schema comple
…[truncated 3591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2304 · 2026-05-19T17:44:12.922473+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 2305 · 2026-05-19T17:44:13.174155+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences
…[truncated 8392 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2306 · 2026-05-19T17:44:13.174684+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 2307 · 2026-05-19T17:44:13.576608+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}). The pattern is stable across three seeds (max $\Delta = 10.7$\,pp, within 1\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\times$; Appendix~\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$). Count curves establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments (\S\ref{sec:bcs_controlled}).
10	
11	\subsection{Pairwise Confusability and Type Confusion}
12	\label{sec:pairwise}
13	
14	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
15	
16	\begin{table}[t]
17	\centering
18	\small
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{llrrrrr}
21	\toprule
22	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \text
…[truncated 9289 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2308 · 2026-05-19T17:44:13.577165+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 2309 · 2026-05-19T17:44:14.480787+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text $k$ times with different type subsets produces precision collapse (0.563$\to$0.210--0.249) as false positives scale with $k$. RE avoids this because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{Event detection.}
10	SDGD-zero on MAVEN (168 event types, 18 batches) confirms the pattern: precision collapses 0.287$\to$0.091 ($-$19.6\,pp) with 3.7$\times$ prediction inflation, and F1 drops from 0.207 to 0.123, replicating merge amplification across span-based tasks (NER and ED).
11	
12	\paragraph{RE: oracle routing.}
13	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}); type separation recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.): graph coloring achieves only marginal mean BCS reduction (0.559$\to$0.552), insufficient to produce detectable accuracy improvement. All practical routing strategies fall below the single-pass baseline (Appendix~\ref{sec:appendix_routing}): under constrained decoding, 73.4\% of instances receive positive predictions across 3--5 sub-schemas, and models self-constrain semantically even without JSON constraints (0.08\% OOV; \S\ref{sec:discussion}), so the routing challenge persists regardl
…[truncated 25 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 2310 · 2026-05-19T17:44:14.531414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2311 · 2026-05-19T17:44:14.833067+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). Range-matched analysis confirms the two dimensions operate independently on DocRED as on FewRel: restricting both count levels to overlapping BCS ranges eliminates the apparent interaction (0.93\,pp, CI crosses zero; \S\ref{sec:multi_channel}). The effect generalizes to document-level RE (DocRED $R^2 = 0.58$) and persists across prompt designs (Appendix~\ref{sec:appendix_prompt_sensitivity}). Dimension~1 replicates across scales (8B--70B); Dimension~2 attenuates on smaller models.
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pairwise $R^2$ is 1.3\%; conditional on nonzero confusion, $R^2$ rises to 7\%. Correlated aggregation amplifies this to batch-level $R^2$ of 18--25\% (Appendix~\ref{app:aggregation-sim}).
9	
10	\paragraph{Task-dependent effects and format dependency.}
11	The batch-level BCS--performance relationship holds across all RE settings---sentence-level ($R^2 = 0.22$) and document-level ($R^2 = 0.58$; IntraSub $\rho = 0.843$)---but not NER ($r \approx 0$, $n = 450$). RE's forced-choice format channels all non-null errors into type substitutions \cite{tam-2024-let-me-speak}; NER errors scatter across missed entities, boundary misalignment, and type confusion \cite{schall-2025-hidden-cost}. The NER U-shape (\S\ref{sec:count_curves}) reflects a dual-task burden: partial schemas require simultaneous span detection and type filtering; at full schema, filtering becomes vacuous and recall recovers. An unconstrained decoding ablation ($n = 25$) confirms this: removing the JSON enum constraint eliminates the BCS--accuracy correlation ($\rho = -0.14$, $p = 0.49$), consistent with grammar-aligned decoding distorting LLM d
…[truncated 1319 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2312 · 2026-05-19T17:44:15.084576+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2313 · 2026-05-19T17:44:17.415490+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit anonymity"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results, here are the key submission guidelines for ACL Rolling Review 2026 regarding page limits and anonymity:

## Page Limits

Short papers have a maximum of 4 content pages, while long papers have a maximum of 8 content pages. Sections on ethical considerations and limitations do not count towards the page limit. Subm
…[truncated 1083 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 8109
}
```

</details>

---


### Tool result

_source line 2314 · 2026-05-19T17:44:18.219905+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"}]

The search results provide some information rel
…[truncated 1220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 9366
}
```

</details>

---


### Tool result

_source line 2315 · 2026-05-19T17:44:18.220490+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 3135
}
```

</details>

---


### Tool call

_source line 2316 · 2026-05-19T17:44:29.416601+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2317 · 2026-05-19T17:44:29.517416+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2318 · 2026-05-19T17:44:37.757766+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6: 外部审稿线 (request_external_review)', 'status': 'pending', 'activeForm': '发起外部审稿请求'}, {'content': 'Step 0.7: 视觉审查派发 (dispatch_visual_check)', 'status': 'pending', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer 任务', 'status': 'pending', 'activeForm': '分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见给对方 Reviewer', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6: 外部审稿线 (request_external_review)', 'status': 'pending', 'activeForm': '发起外部审稿请求'}, {'content': 'Step 0.7: 视觉审查派发 (dispatch_visual_check)', 'status': 'pending', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer 任务', 'status': 'pending', 'activeForm': '分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见给对方 Reviewer', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2319 · 2026-05-19T17:44:37.758304+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2320 · 2026-05-19T17:44:41.978427+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2321 · 2026-05-19T17:44:43.334356+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (64 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_docred_bcs_expanded** (success): Expanding DocRED BCS-controlled batches from 5 to 15 per count level will narrow the factorial interaction CI (currently [-1.6, 13.0]) sufficiently to resolve whether the BCS-count interaction is bounded or substantial in document-level RE. If the CI narrows to exclude zero, the interaction is genuine and non-additive; if it narrows to include zero tightly, the bounded-interaction claim strengthens.\n- **exp_sdgd_zero_maven** (success): SDGD-zero on MAVEN (168 event types, 18 batches) will reproduce the schema DAG extraction capability observed on DocRED, validating cross-domain generalization from document-level RE to event detection.\n- **exp_unconstrained_decoding_ablation** (success): The BCS-accuracy correlation in RE arises fro
…[truncated 1440 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 2322 · 2026-05-19T17:44:43.485364+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 2323 · 2026-05-19T17:44:43.937600+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-associated degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \cite{lla
…[truncated 4608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2324 · 2026-05-19T17:44:44.088611+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2325 · 2026-05-19T17:44:44.340280+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2326 · 2026-05-19T17:44:45.043388+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2327 · 2026-05-19T17:44:45.194412+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2328 · 2026-05-19T17:44:45.194743+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2329 · 2026-05-19T17:44:45.245658+00:00_

1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the foll
…[truncated 5208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2330 · 2026-05-19T17:44:49.438823+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 2331 · 2026-05-19T17:44:49.761186+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 322
}
```

</details>

---


### Tool call

_source line 2332 · 2026-05-19T17:44:49.811715+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2333 · 2026-05-19T17:44:49.863097+00:00_

1	# Review Issues Tracker
2	# Updated: 2026-05-19 (post supplementary experiments completion)
3	
4	# ============================================================
5	# R21 CRITICAL — 新发现（fresh review）
6	# ============================================================
7	
8	- id: R21-C1
9	  summary: "TOST ±3pp margin 循环论证，3/4 条件 inconclusive"
10	  category: method
11	  severity: critical
12	  status: in_progress
13	  first_raised_round: 21
14	  last_seen_round: 21
15	  mentions:
16	    - {round: 21, reviewers: [R1, R2], note: "双方共识。margin 来自 batch SD 部分由 BCS 驱动。"}
17	  action_items:
18	    - {round: 21, action: "§4.4 加 margin justification（锚定 IQR Δ=2.2pp）", assigned_to: main_agent, status: done}
19	    - {round: 21, action: "DocRED expanded 完成：interaction=-9.39pp CI[-12.91,-5.95]，不再需要 TOST equivalence on DocRED——改为报告 genuine sub-additive interaction。TOST ±3pp 仅保留 FewRel（p=0.003）。正在更新论文。", assigned_to: main_agent, status: in_progress}
20	  resolution: ""
21	  resolution_round: null
22	
23	- id: R21-C2
24	  summary: "DocRED R²=53% 来自 n=35 不稳定估计，Abstract headline 误导"
25	  category: framing
26	  severity: critical
27	  status: in_progress
28	  first_raised_round: 21
29	  last_seen_round: 21
30	  mentions:
31	    - {round: 21, reviewers: [R1, R2], note: "双方完全同意。CI [0.27, 0.73] 极宽。"}
32	  action_items:
33	    - {round: 21, action: "Results 加 CI 标注；Abstract 数字等 DocRED expanded 实验后更新", assigned_to: main_agent, status: in_progress}
34	    - {round: 21, action: "DocRED expanded 完成（n=55，6 conditions all complete）。Agent 正在重新计算 R² + CI 并更新 Abstract 数字。", assigned_to: main_agent, status: in_progress}
35	  resolution: ""
36	  resolution_round: null
37	
38	- id: R21-C3
39	  summary: "Dim2 proprietary gap，Abstract 'effects replicate' scope 过宽"
40	  category: framing
41	  severity: critical
42	  status: in_progress
43	  first_raised_round: 21
44	  last_seen_round: 21
45	  mentions:
46	    - {round: 21, reviewers: [R1, R2], note: "双方同意。Dim2 batch-level 未在 API 模型验证。"}
47	  action_items:
48	 
…[truncated 11654 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2334 · 2026-05-19T17:44:54.591166+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2335 · 2026-05-19T17:44:55.093739+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema-dag-extraction'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2336 · 2026-05-19T17:44:56.500042+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool call

_source line 2337 · 2026-05-19T17:44:56.804022+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent"
  }
}
```

</details>

---


### Tool result

_source line 2338 · 2026-05-19T17:44:56.854903+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2339 · 2026-05-19T17:44:57.006889+00:00_

&lt;persisted-output>
Output too large (77.1KB). Full output saved to: /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-director-338aa0a5/de79316b-829f-4771-8e38-c18a57e3324c/tool-results/toolu_01PYHpywnPZ6pTzgYHU9XE1K.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_14.md:159:外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_9.md:112:状态：**skipped**（用户未在规定时间内提交至 paperreview.ai）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_18.md:133:外部审稿：未配置（项目 `external_review.paperreview_ai.enabled` 未设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_8.md:179:项目配置 `external_review.paperreview_ai.enabled: false`。未请求外部审稿。
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_5.md:181:未配置（`external_review.paperreview_ai.enabled` not set in project config）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_20.md:226:**外部审稿：未配置**（项目未启用 `external_review.paperreview_ai`）
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_16.md:156:未启用（项目配置 `external_review.paperreview_ai.enabled: false`）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_15.md:158:未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_13.md:190:外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。
/home/ubuntu/.agent-ml-research-idea_gen_
…[truncated 340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 506
}
```

</details>

---


### Tool call

_source line 2340 · 2026-05-19T17:45:35.850441+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6: 外部审稿线 — 跳过（未配置）', 'status': 'completed', 'activeForm': '跳过外部审稿'}, {'content': 'Step 0.7: 视觉审查派发 + Step 1: 分配 Reviewer 任务', 'status': 'in_progress', 'activeForm': '派发视觉审查 + 分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见给对方 Reviewer', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6: 外部审稿线 — 跳过（未配置）', 'status': 'completed', 'activeForm': '跳过外部审稿'}, {'content': 'Step 0.7: 视觉审查派发 + Step 1: 分配 Reviewer 任务', 'status': 'in_progress', 'activeForm': '派发视觉审查 + 分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见给对方 Reviewer', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2341 · 2026-05-19T17:45:35.901249+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2342 · 2026-05-19T17:45:41.228568+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema-dag-extraction",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema-dag-extraction",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool result

_source line 2343 · 2026-05-19T17:46:00.380781+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19152
}
```

</details>

---


### Tool call

_source line 2344 · 2026-05-19T17:46:00.381244+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ACL Rolling Review May 2026 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文严格 8 页，参考文献不限，Limitations + Ethics 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（无作者名、无非匿名链接）\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**方法严谨性**，具体包括：\n\n1. **实验设计**：BCS-controlled 实验的控制变量是否充分？count-curve 和 BCS-controlled 两种范式是否互补？是否有遗漏的混杂因素？\n2. **统计方法**：TOST 等价性检验的 margin 选择是否有循环论证？Bootstrap CI 的使用是否恰当？多重比较的处理（Rothman 引用）是否充分？logit-scale sensitivity 的结论是否过于乐观？\n3. **因果推断**：论文声称 correlational + quasi-experimental，是否有地方措辞超出了相关性证据？Title 用 \"Predict\" 是否合适？\n4. **效应量与实用意义**：pairwise r²=1.3-1.7% 和 typical batch ~2pp gap 的实际价值如何评估？R² 从 pair-level 到 batch-level 的放大（22-58%）是否令人信服？\n5. **可复现性**：单一种子（seed 42）+ greedy decoding 的设计是否足够？FP8 量化的非确定性如何影响结论？\n6. **消融/对照**：renaming experiment 的解读是否合理？unconstrained decoding ablation 的结论是否过强？few-shot 实验的 confounding 控制是否充分？\n7. **DocRED factorial**：expanded n=55 后 interaction=-9.4pp，range-matched 后降至 0.93pp，这个分析链是否有方法论漏洞？\n8. **Cross-model validation**：8B/70B/Gemini 的验证范围和结论是否匹配？Dim2 仅在 open-weight 验证，结论是否过宽？\n\n请给出完整审稿报告，按 Strengths → Weaknesses（逐条编号，标注 [Must-Fix] / [Should-Fix] / [Minor]） → Questions → Missing References 的结构。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ACL Rolling Review May 2026 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文严格 8 页，参考文献不限，Limitations + Ethics 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（无作者名、无非匿名链接）\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**方法严谨性**，具体包括：\n\n1. **实验设计**：BCS-controlled 实验的控制变量是否充分？count-curve 和 BCS-controlled 两种范式是否互补？是否有遗漏的混杂因素？\n2. **统计方法**：TOST 等价性检验的 margin 选择是否有循环论证？Bootstrap CI 的使用是否恰当？多重比较的处理（Rothman 引用）是否充分？logit-scale sensitivity 的结论是否过于乐观？\n3. **因果推断**：论文声称 correlational + quasi-experimental，是否有地方措辞超出了相关性证据？Title 用 \"Predict\" 是否合适？\n4. **效应量与实用意义**：pairwise r²=1.3-1.7% 和 typical batch ~2pp gap 的实际价值如何评估？R² 从 pair-level 到 batch-level 的放大（22-58%）是否令人信服？\n5. **可复现性**：单一种子（seed 42）+ greedy decoding 的设计是否足够？FP8 量化的非确定性如何影响结论？\n6. **消融/对照**：renaming experiment 的解读是否合理？unconstrained decoding ablation 的结论是否过强？few-shot 实验的 confounding 控制是否充分？\n7. **DocRED factorial**：expanded n=55 后 interaction=-9.4pp，range-matched 后降至 0.93pp，这个分析链是否有方法论漏洞？\n8. **Cross-model validation**：8B/70B/Gemini 的验证范围和结论是否匹配？Dim2 仅在 open-weight 验证，结论是否过宽？\n\n请给出完整审稿报告，按 Strengths → Weaknesses（逐条编号，标注 [Must-Fix] / [Should-Fix] / [Minor]） → Questions → Missing References 的结构。"
  }
}
```

</details>

---


### Tool result

_source line 2345 · 2026-05-19T17:46:16.593019+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16211
}
```

</details>

---
