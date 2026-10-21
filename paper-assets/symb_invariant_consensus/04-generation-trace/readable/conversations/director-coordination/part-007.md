# Director coordination — Part 7 of 9

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

[← Part 6](part-006.md) · [Transcript overview](../director-coordination.md) · [Part 8 →](part-008.md) · [Structured JSON](../../../sessions/bd/bdd0e6c8e8a0a8a81e76.json)

## Round 144

### User

_source line 1977 · 2026-05-23T14:00:46.765778+00:00_

[Reviewer 2 审稿结果]:
## 逐条回应 Reviewer 1 审稿意见

---

### Must-Fix

**[AGREE] R1-N1: Capability-gap pattern n=6 且共享 verifier**

同意，且 R1 的分析比我的 N3 更精确。我的 N3 主要从"证据量不足"角度批评，R1 进一步指出 4/6 条件共享同一 DeBERTa verifier，实际有效自由度远小于 6——这是我遗漏的关键点。Table 3（Section 6）中 4 个 generator 全部 paired with 同一个 DeBERTa-large-mnli，Spearman ρ=1.0 的 n=4 排列检验在这种 shared-verifier 设计下几乎没有统计意义。此外，Section 6 的 domain-adapted verifier 结果（99.67% standalone）引入了 training，论文自己也承认这只是 "directional evidence"。两个 reviewer 均认为 Contribution 3 应降级为 preliminary observation，这一共识应被作者认真对待。

**[AGREE] R1-N2: Underpowered conditions 与标题表述**

同意，且我认为 R1 将此列为 Must-Fix（而非我的 Should-Fix W2）更为合理。回顾论文：标题 "No Detectable Improvement" + Abstract "We find no evidence of improvement" 构成了全文最核心的 claim，但 Appendix D Table 6 显示 10/16 条件的 observed power 低于 21%，MDE 在 1.86–4.84pp 之间。在这种 power profile 下，"no detectable" 和 "no evidence" 在统计学上不等同于 "equivalence established"——absence of evidence ≠ evidence of absence。R1 建议改为 "no evidence of improvement exceeding ~2pp" 或在 Discussion 中论证 <2pp 在 4.5× computational overhead 下无实际价值，这都是具体可操作的改进方向。我将我的 W2 升级为与 R1-N2 同级别的 Must-Fix。

---

### Should-Fix

**[AGREE] R1-W1: BR 与 Observation 1 的概念循环——与我的 W4 指向同一根本问题**

同意，且 R1 的分析比我的 W4 更精确、更致命。我的 W4 从命名层面质疑（"confirmation bias" 暗示 cognitive bias 类比，但实质是 structural limitation），R1 则从技术层面指出 BR > 1 在 source-attribution scoring 下是 trace-count 分布的**数学必然结果**——permutation test 证实 BR_excess ≈ 0 (p > 0.7, Section 5.1)，即 BR 完全由 trace-count 结构解释，不含来自 extraction 过程的额外 bias。

这意味着 R1-W1 和我的 W4 确实指向**同一根本问题的两个层面**：
- **技术层面**（R1-W1）：BR 作为诊断指标没有独立于 Observation 1 的增量信息——它度量的是 source-attribution scoring 的结构性质，不是 extraction 质量。
- **概念层面**（我的 W4）：将这一结构性质命名为 "bias" 暗示了可纠正的缺陷，但这是设计的内在属性。

两个 reviewer 从不同角度收敛到同一结论：SCB 的核心问题不在于 extraction 有偏，而在于 source-attribution scoring 使约束权重退化为答案频率的函数。论文应更清楚地将 "structural degeneration"（Observation 1 的必然后果）与 "extraction bias"（约束提取过程本身是否有偏）区分开来。目前论文混淆了这两者，使 BR 看起来提供了 Observation 1 之外的独立证据，但 R1 的 permutation test 引用表明它没有。

**[AGREE] R1-W2: "Pre-registered" 缺乏注册凭证**

完全同意。"Pre-registered" 在实证研究中有明确的操作定义（OSF、AsPredicted 等平台的正式预注册）。论文使用这一术语但未提供注册链接，在 double-blind 审稿中无法核实。这是我在初审中遗漏的问题。改为 "pre-specified" 或 "predetermined" 即可，修改成本很低但对方法论诚信重要。

**[AGREE with nuance] R1-W3: BH correction m=16 包含非独立条件**

同意 R1 的观察，但认为严重程度有限。BH correction 对 m 的膨胀是保守的（更多校正 → 更少 false positives），所以不会导致假阳性膨胀。但 R1 说得对，方法论上应更干净地区分 confirmatory 和 exploratory 条件。如果 16 个条件中包含了 seed aggregates 和 component seeds 的重叠，则部分条件之间存在统计依赖关系，严格来说违反了 BH 的独立性假设。建议采用 R1 的建议：在 Table 1 中标注哪些是 confirmatory conditions，哪些是 exploratory conditions，BH 校正仅应用于 confirmatory set。

**[AGREE] R1-W4: Observation 1 条件 (iii) 缺乏系统验证**

同意。Observation 1 是论文形式化分析的核心，其成立依赖三个条件同时满足。条件 (iii) "approximately uniform constraint yield per trace" 直接影响 degeneration 是否发生（如果不同 trace 产生的约束数量差异大，则加权后不一定退化为 majority vote）。论文在 Section 5.1 中讨论了 degeneration 的实证支持，但未系统报告 per-trace yield 的分布特征（均值、标准差、按 answer group 分层的差异）。这是一个合理的补充实验请求。

**[AGREE] R1-W5: Cross-architecture escape 可能只是 ensemble diversity 效应——独立于我的 N3**

同意，且这是一个**独立于**我 N3 的额外问题。我的 N3 关注证据数量（太少条件），R1-W5 关注证据解释（即使有更多条件，增益可能只是 ensemble diversity 而非 SCB escape）。两者同时成立且互相加强：

- **N3（量的问题）**：n=6 条件、1 个 verifier family 不足以确立 contribution 级别的 claim。
- **W5（质的问题）**：DeBERTa-NLI 与 decoder-only LLM 在架构、训练数据、任务形式上完全不同。任何两个充分不同的模型组成 ensemble 都可能产生增益——这是 ensemble diversity 的经典结果（Dietterich 2000），不需要 SCB escape 的解释。

论文需要一个关键的 ablation 来区分这两个假说：将 DeBERTa-NLI combo 的增益与简单的 **cross-model majority vote ensemble**（例如 Mistral-7B + Qwen2.5-14B 的 majority vote）进行对比。如果后者也产生类似增益，则 "escaping SCB" 的 narrative 不成立——增益来自 ensemble diversity，不是约束验证的结构独立性。

---

### 对 R1 主要优势的回应

**[AGREE]** R1 列出的 6 个优势我基本认可。特别是：
- Strength 1（统计方法论）和 Strength 2（Oracle control）是本文最突出的贡献
- Strength 4（形式化命名克制）确实值得肯定——使用 "Observation" 和 "Remark" 而非 "Theorem" 是恰当的
- Strength 6（Entropy decomposition, Appendix N）是一个我在初审中未充分关注的分析亮点

### Missing References

**[AGREE]** R1 指出的 Dietterich (2000) 和 Krogh & Vedelsby (1994) 确实应被引用，特别是在 Section 2 的 ensemble theory 段落和 Section 6 的 cross-architecture discussion 中。这与 R1-W5（ensemble diversity confound）直接相关——如果论文引用了这些经典工作，就需要更明确地回应 ensemble diversity 假说。

---

## 对 Director 提出的 5 个分歧点的回应

### 1. R1 的 3.5 vs 我的 3.0——R1 是否评分过高？

**R1 的 3.5 偏高，我维持 3.0。** 理由：

(a) **R1 未发现引用错误**（见下方第 5 点），而我的 N1 发现两条引用存在严重元数据错误（byerly2026 的作者名/年份/主题三重错误，dupo2025 的作者名/标题错误）。这直接影响 Soundness 评分。

(b) R1 给 Soundness 4.0/5，但考虑到：(i) 引用错误（N1）、(ii) underpowered conditions 下标题的 misleading claim（N2）、(iii) BR 的概念循环（W1），Soundness 应为 **3.5/5**。

(c) R1 和我在 Excitement 上一致（3.0/5），这是决定 Conference vs Findings 的关键维度。在 Excitement 仅 3.0 的情况下，除非 Soundness 特别突出（4.5+），否则难以支撑 3.5 的 Overall。

(d) R1 自己也认为 "核心正面贡献（cross-architecture escape）基于 n=6 且存在共享 verifier 问题"——如果最主要的正面贡献都被认定为 preliminary，那么论文的 overall profile 更接近 Findings 而非 Borderline Conference。

### 2. R1-W1 与我的 W4 是否指向同一根本问题？

**是的**，已在上方 R1-W1 回应中详细分析。两者从技术层面和概念层面分别收敛到同一结论：SCB 的 "bias" 框架混淆了 structural degeneration 和 extraction bias。R1 的 permutation test 引用（BR_excess ≈ 0）提供了比我的 W4 更锐利的技术论证。

### 3. R1-W5 是否独立于我的 N3？

**是的，完全独立。** 已在上方 R1-W5 回应中详细分析。N3 是 "证据不够多"（量的问题），W5 是 "证据的解释可能错误"（质的问题）。两者同时削弱 Contribution 3 的可信度，且需要不同的修改策略来解决（N3 需要更多实验，W5 需要 ablation 实验区分 ensemble diversity vs. SCB escape）。

### 4. 统计方法论是否足以弥补 novelty 不足？

**不足以。** 统计严谨性是必要条件而非充分条件。优秀的方法论使 negative result 更可信（从 "可能不 work" 到 "在这些条件下确实不 work"），但不改变这一结果的 surprise value。在 Huang et al. (2024) 和 Condorcet Jury Theorem 之后，"自提取约束无独立信号" 是一个 expected result 的高质量 confirmation——这正是 Findings 的定位：soundness 和 reproducibility 足够，但 excitement/novelty 不够 Conference。

ARR 的评分维度中，Findings 接收的主要标准是 soundness 和 reproducibility（本文在这两方面都很强），Conference 还需要 novelty 和 impact（本文在这方面不足）。统计方法论贡献于 soundness，不贡献于 excitement。

### 5. 我的 N1（引用错误）是否改变 Soundness 评价？

**是的。** 两条引用的元数据严重错误不是 typo 级别的问题：

- `byerly2026selfconsistency`：作者名（Nicholas→Adam）、年份（2026→2024）、标题主题（mathematical reasoning→positional bias on long-context）三重错误，涉及的实际论文讨论的是完全不同的话题。
- `dupo2025`：作者名（Yang Chenxu→Shuaijie She）、标题（Dual Process→Dual Preference）错误，Yang Chenxu 甚至不在实际论文的作者列表中。

这些错误的模式（真实的 arXiv ID 配上错误的元数据）高度暗示引用细节由 LLM 生成而未经人工核实。在 Related Work 中，byerly2026 被用来支持 "SC gains plateau" 的论点，dupo2025 被用来列举 training-based verification 的方法——如果这些引用实际上讨论的是不同话题，那么论点的文献支撑存在漏洞。

R1 给 Soundness 4.0/5 时未发现此问题。加入引用错误后，我认为 Soundness 应降至 **3.5/5**——方法论本身依然扎实，但文献综述的可信度受损，且引发了对论文其他引用准确性的 broader concern。建议作者对全部参考文献进行系统性交叉验证。

---

## 综合判断

经过与 R1 的交叉审议，我维持 **Overall 3.0 (Findings)** 的评分，但两个 reviewer 的共识区域很明确：

**共识**（两个 reviewer 均认为需要修改）：
1. Cross-architecture escape 应降级为 preliminary observation（R1-N1 = 我的 N3）
2. Underpowered conditions 下的 claim 需要更精确的表述（R1-N2 ≈ 我的 W2，我升级为 Must-Fix）
3. SCB/BR 的概念框架需要更清楚地区分 structural degeneration vs extraction bias（R1-W1 + 我的 W4）

**R2 独有的 Must-Fix**：
4. 两条引用元数据严重错误（我的 N1）——R1 未发现，但这是客观可验证的事实问题
5. "Advances beyond Huang et al." 的 claim 过度（我的 N2）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1978 · 2026-05-23T14:01:04.212000+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1979 · 2026-05-23T14:01:04.714504+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T13:45:46.380124+00:00\", \"completed_at\": \"2026-05-23T13:49:21.134597+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页为纯文本（Title/Abstract/Introduction），无 display item。Figure 1 出现在 page 2 顶部（SICA pipeline 架构图），在前 3 页内提供了清晰视觉锚点，传达核心方法流程，符合预期。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 为 figure* 全宽图，pipeline 流程用彩色方框标注（红色虚线=gold FOL，蓝色=约束提取，绿色=MAX-SAT），caption 自包含且详细。Title-Abstract-Figure 1 三者讲述同一个故事（自提取约束无效），一致性好。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2 散点图使用 4 种颜色区分模型族（蓝/橙/绿/紫），颜色区分度可接受。但图例文字偏小（约 6-7pt），建议适当放大图例字号以提升可读性。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1（主结果表）内容密集，字号偏小（估计 ~7pt），行数较多。整体可读但处于舒适阅读的下限。booktabs 风格正确，bold 标注显著结果，表头分区（Type C / Type A）清晰。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3（Causal DAG）尺寸明显偏小，仅占左栏顶部约 1/4 面积。作为因果推断的核心概念图，建议适当放大以增强可读性和视觉冲击力。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4 条形图中 x 轴标签和图例文字偏小，分类名称（Constrained prompting / Iterative refinement 等）在当前字号下需仔细辨认。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"\\\"Limitations\\\" section heading 出现在页面底部极端位置，后续仅跟随约 2 行正文，大部分 Limitations 内容在 page 9 顶部。存在 section heading 孤悬（orphan heading）风险，建议用 \\\\needspace 或手动调整使 heading 与至少 3-4 行正文保持在同一页。\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Appendix A 的 prompt templates 使用小号等宽字体，内容非常密集。虽然作为 appendix 可接受，但字号接近可读下限。\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"单页包含 4 个表格（Tables 4-7），密度极高。作为 appendix 的统计分析结果可接受，但视觉上略显拥挤。\"}, {\"severity\": \"info\", \"dimension\": \"page 26\", \"message\": \"末页（appendix 最后一页）内容占约 60% 页面，底部约 40% 空白。作为全文最后一页可接受，不构成问题。\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 9}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1980 · 2026-05-23T14:01:04.714921+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1981 · 2026-05-23T14:01:06.076436+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool call

_source line 1982 · 2026-05-23T14:01:06.178024+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | head -100",
  "description": "Read current review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | head -100",
    "description": "Read current review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1983 · 2026-05-23T14:01:06.581752+00:00_

# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
- id: "R1-C1"
  summary: "Method Stage 3 sat() implementation undescribed"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
  resolution_round: 3

- id: "R1-C2"
  summary: "Most experiments underpowered (n≤60), no power analysis"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
  resolution_round: 3

- id: "R1-C3"
  summary: "Oracle/upper-bound experiment missing"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
  resolution_round: 3

- id: "R1-C4"
  summary: "Huang et al. (ICLR 2024) not cited"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
  resolution_round: 2

- id: "R1-C5"
  summary: "Critical related work missing"
  category: writing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "~48 citations, 5 Related Work paragraphs."
  resolution_round: 3

- id: "R1-C9"
  summary: "Capability trap novelty unclear"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Reframed as regime-dependent analysis with CJT framework."
  resolution_round: 3

- id: "R3-N1"
  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 3
  last_seen_round: 4
  resolution: "Paper Agent added clarifying sentence in method.tex."
  resolution_round: 4

- id: "R3-N2"
  summary: "α va
…[truncated 603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 1984 · 2026-05-23T14:01:16.927092+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | wc -l",
  "description": "Count lines in review issues yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | wc -l",
    "description": "Count lines in review issues yaml"
  }
}
```

</details>

---


### Tool result

_source line 1985 · 2026-05-23T14:01:17.029186+00:00_

1224

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1986 · 2026-05-23T14:01:20.745386+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | grep -E \"^- id:|^  summary:|^  status:|^  severity:|^  category:|^  last_seen_round:\" | head -200",
  "description": "Extract key fields from all issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | grep -E \"^- id:|^  summary:|^  status:|^  severity:|^  category:|^  last_seen_round:\" | head -200",
    "description": "Extract key fields from all issues"
  }
}
```

</details>

---


### Tool result

_source line 1987 · 2026-05-23T14:01:20.846457+00:00_

- id: "R1-C1"
  summary: "Method Stage 3 sat() implementation undescribed"
  category: method
  severity: critical
  status: resolved
  last_seen_round: 3
- id: "R1-C2"
  summary: "Most experiments underpowered (n≤60), no power analysis"
  category: experiment
  severity: critical
  status: resolved
  last_seen_round: 1
- id: "R1-C3"
  summary: "Oracle/upper-bound experiment missing"
  category: experiment
  severity: critical
  status: resolved
  last_seen_round: 1
- id: "R1-C4"
  summary: "Huang et al. (ICLR 2024) not cited"
  category: framing
  severity: critical
  status: resolved
  last_seen_round: 2
- id: "R1-C5"
  summary: "Critical related work missing"
  category: writing
  severity: critical
  status: resolved
  last_seen_round: 1
- id: "R1-C9"
  summary: "Capability trap novelty unclear"
  category: framing
  severity: critical
  status: resolved
  last_seen_round: 3
- id: "R3-N1"
  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
  category: method
  severity: critical
  status: resolved
  last_seen_round: 4
- id: "R3-N2"
  summary: "α value never specified"
  category: method
  severity: critical
  status: resolved
  last_seen_round: 3
- id: "R9-W2"
  summary: "NLI combo weight parameter w 未交叉验证"
  category: experiment
  severity: warning
  status: in_progress
  last_seen_round: 18
- id: "R9-W3"
  summary: "Capability Gap Hypothesis 基于极小样本 (n=6)"
  category: experiment
  severity: critical
  status: in_progress
  last_seen_round: 18
- id: "R9-VL1"
  summary: "Pages 1-2 连续纯文本无 display item"
  category: format
  severity: warning
  status: in_progress
  last_seen_round: 18
- id: "R9-VL4"
  summary: "Discussion/Conclusion 展开不足"
  category: writing
  severity: warning
  status: in_progress
  last_seen_round: 18
- id: "R10-N1"
  summary: "Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem"
  category: method
  severity: critical
  status: resolved
  last_seen_round: 13
- id: "R10-N2"
  summary: "κ→K_eff 
…[truncated 2998 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1988 · 2026-05-23T14:01:27.427124+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | grep -E \"^- id:|^  status:\" | paste - - | grep -v resolved | grep -v wont_fix",
  "description": "List all open/in_progress issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | grep -E \"^- id:|^  status:\" | paste - - | grep -v resolved | grep -v wont_fix",
    "description": "List all open/in_progress issues"
  }
}
```

</details>

---


### Tool result

_source line 1989 · 2026-05-23T14:01:27.478030+00:00_

- id: "R9-W2"	  status: in_progress
- id: "R9-W3"	  status: in_progress
- id: "R9-VL1"	  status: in_progress
- id: "R9-VL4"	  status: in_progress
- id: "R10-N2"	  status: in_progress
- id: "R10-N3"	  status: in_progress
- id: "R10-W1"	  status: in_progress
- id: "R10-W2"	  status: in_progress
- id: "R10-W3"	  status: in_progress
- id: "R10-W4"	  status: in_progress
- id: "R10-W6"	  status: in_progress
- id: "R10-W7"	  status: in_progress
- id: "R10-W8"	  status: in_progress
- id: "R10-I1"	  status: in_progress
- id: "R10-I2"	  status: in_progress
- id: "R11-N1"	  status: in_progress
- id: "R11-N2"	  status: in_progress
- id: "R11-N3"	  status: in_progress
- id: "R11-W1"	  status: in_progress
- id: "R11-W2"	  status: in_progress
- id: "R11-W3"	  status: in_progress
- id: "R11-W4"	  status: in_progress
- id: "R11-W5"	  status: in_progress
- id: "R11-W7"	  status: in_progress
- id: "R12-N1"	  status: in_progress
- id: "R12-N2"	  status: in_progress
- id: "R12-W1"	  status: in_progress
- id: "R12-W4"	  status: in_progress
- id: "R12-EC1"	  status: in_progress
- id: "R13-N2"	  status: in_progress
- id: "R13-N3"	  status: in_progress
- id: "R13-W1"	  status: in_progress
- id: "R13-W2"	  status: in_progress
- id: "R13-W3"	  status: in_progress
- id: "R13-W4"	  status: in_progress
- id: "R14-N1"	  status: in_progress
- id: "R14-N2"	  status: in_progress
- id: "R14-W1"	  status: in_progress
- id: "R14-W2"	  status: in_progress
- id: "R14-W3"	  status: in_progress
- id: "R14-W5"	  status: in_progress
- id: "R14-W6"	  status: in_progress
- id: "R15-M3"	  status: open
- id: "R15-M4"	  status: open
- id: "R15-W1"	  status: in_progress
- id: "R16-N1"	  status: in_progress
- id: "R16-N2"	  status: in_progress
- id: "R16-W1"	  status: in_progress
- id: "R16-W2"	  status: in_progress
- id: "R16-SYS1"	  status: in_progress
- id: "R17-N1"	  status: in_progress
- id: "R17-N2"	  status: in_progress
- id: "R17-N4"	  status: in_progress
- id: "R17-N5"	  status: in_progress
- id: "R17-VL1"
…[truncated 269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1990 · 2026-05-23T14:01:38.419219+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
  "offset": "1150",
  "limit": "75"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
    "offset": "1150",
    "limit": "75"
  }
}
```

</details>

---


### Tool result

_source line 1991 · 2026-05-23T14:01:38.469842+00:00_

1150	      note: "R18(fresh) 未单独提及"
1151	
1152	# R18 new issues
1153	
1154	- id: "R18-N1"
1155	  summary: "Remark 1与Figure 3间存在claim升级——DPI trivial但C⊥Y|A未证明"
1156	  category: method
1157	  severity: major
1158	  status: in_progress
1159	  first_raised_round: 18
1160	  last_seen_round: 18
1161	  mentions:
1162	    - round: 18
1163	      reviewers: [1, 2]
1164	      note: "R1-W1 + R2交叉AGREE: Remark 1只证trivial DPI; Figure 3隐含更强的C⊥Y|A; 需在Prop 1条件下显式证明I(C;Y)≤I(A;Y)"
1165	
1166	- id: "R18-N2"
1167	  summary: "BR应重新框定为degeneration度量而非bias度量"
1168	  category: method
1169	  severity: major
1170	  status: in_progress
1171	  first_raised_round: 18
1172	  last_seen_round: 18
1173	  mentions:
1174	    - round: 18
1175	      reviewers: [1, 2]
1176	      note: "R1-W2 + R2交叉AGREE: permutation BR_null≈BR_obs意味着BR完全由base rate解释; 建议报告BR_excess并将BR角色从measuring bias转为measuring structural coupling"
1177	
1178	- id: "R18-M1"
1179	  summary: "遗漏引用: Xie et al. (2023) Self-Evaluation Guided Beam Search"
1180	  category: writing
1181	  severity: minor
1182	  status: in_progress
1183	  first_raised_round: 18
1184	  last_seen_round: 18
1185	  mentions:
1186	    - round: 18
1187	      reviewers: [1, 2]
1188	      note: "R2建议, R1 AGREE"
1189	
1190	- id: "R18-M2"
1191	  summary: "Table 1 Mistral-7B multi-seed行间关系不直观"
1192	  category: format
1193	  severity: minor
1194	  status: in_progress
1195	  first_raised_round: 18
1196	  last_seen_round: 18
1197	  mentions:
1198	    - round: 18
1199	      reviewers: [1]
1200	      note: "R1-M2: s123/s456/s789与3s(3-seed aggregated)关系需在caption/脚注说明"
1201	
1202	- id: "R18-M3"
1203	  summary: "56.4%零变量重叠的计算粒度未说明"
1204	  category: method
1205	  severity: minor
1206	  status: in_progress
1207	  first_raised_round: 18
1208	  last_seen_round: 18
1209	  mentions:
1210	    - round: 18
1211	      reviewers: [1]
1212	      note: "R1-M3: per-problem? per-dataset? per-constraint pair?"
1213	
1214	- id: "R18-VL1"
1215	  summary: "Table 1(page 5)数据字号偏小(7-8pt), 符号系统认知负荷高"
121
…[truncated 257 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1992 · 2026-05-23T14:04:34.062145+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "symb_invariant_consensus",
  "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9+ recurring issues\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 19\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及，但 cross-architecture escape 整体证据不足的共识间接涵盖\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 19\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-N3: 两位 reviewer 一致认为 n=6 且 4/6 共享 DeBERTa verifier，应降级为 preliminary observation。R2 补充 'generator < verifier 才有增益' 是 trivial condition\"\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 视觉审查: Figure 1 出现在 page 2 顶部，视觉锚点存在但仍在前 3 页范围内\"\n\n- id: \"R9-VL4\"\n  summary: \"Discussion/Conclusion 展开不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"R2-W5: Section 7 仅约 1/3 页，论文整体密度过高，\\enlargethispage{6\\baselineskip} 等排版 hack\"\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同，两位 reviewer 共识降级为 preliminary observation\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W5: 可能只是 ensemble diversity 效应而非 SCB escape。R2 AGREE 并建议 cross-model majority vote ablation\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-N2 + R2-W2(升级): 10/16 条件 underpowered，Abstract/标题的 blanket negative claim 超出统计证据范围\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-W2: 使用 'pre-registered' 但无 OSF 等注册凭证，应改为 'pre-specified'\"\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W4: 两位 reviewer 从不同角度收敛——R1 从技术层面(BR_excess≈0)、R2 从概念层面(structural limitation vs cognitive bias analogy)。共识：应区分 structural degeneration 和 extraction bias\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及\"\n\n- id: \"R10-I1\"\n  summary: \"'Symbolic Mirage' 概念新颖性——与 Huang/Wan 的 confirmation bias 区别\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-N2: 'advances beyond Huang et al.' claim 过度，核心洞见在 Huang + Condorcet 下可预见。R1 AGREE with nuance: scope extension + formalization 而非 fundamental advance\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: resolved\n  last_seen_round: 17\n  resolution: \"Figure 2, Figure 4 added in main text.\"\n  resolution_round: 17\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"95% bootstrap CIs added for BR.\"\n  resolution_round: 11\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"Renamed to Observation 1, conditions made explicit, empirical support section added.\"\n  resolution_round: 14\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R9-W3/R10-N3 同一问题群，R19 两位 reviewer 共识\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-N2: 建议 Abstract 改为 'no evidence exceeding ~2pp'。R2 升级为 Must-Fix\"\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-W2: 'pre-registered' 无注册凭证\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W1: BR>1 是 source-attribution 的数学必然，permutation BR_excess≈0。R2 AGREE: BR 度量 degeneration 而非 independent bias signal\"\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"R2-W4 相关: SCB 命名暗示 cognitive bias 类比但实质是 structural limitation\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-N2: 'advances beyond' 应改为 'extends and formalizes'。R1 AGREE with nuance\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及\"\n\n- id: \"R11-W7\"\n  summary: \"Ensemble diversity 文献缺失\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1 + R2 均指出缺少 Dietterich (2000), Krogh & Vedelsby (1994/1995)\"\n\n- id: \"R12-N1\"\n  summary: \"Capability-gap pattern 证据不足以支撑 top-level contribution\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群\"\n\n- id: \"R12-N2\"\n  summary: \"Underpowered tests 与 negative claim 之间存在 gap\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-N2 同一 issue\"\n\n- id: \"R12-W1\"\n  summary: \"Cross-architecture escape 可能是 ensemble diversity\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2 AGREE: 需 cross-model majority vote ablation 区分假说\"\n\n- id: \"R12-W4\"\n  summary: \"Observation 1 条件验证不完整\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-W4: 条件 (iii) uniform constraint yield 缺乏 per-trace 分布统计量验证\"\n\n- id: \"R12-EC1\"\n  summary: \"代码/数据可获取性声明缺失\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-M5: 无 'code will be released upon acceptance' 声明\"\n\n- id: \"R13-N2\"\n  summary: \"Novelty claim 相对 Huang et al. (2024) 的增量有限\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-N2: 'advances beyond' 过度声明。R1 AGREE: scope extension + formalization 而非 fundamental advance\"\n\n- id: \"R13-N3\"\n  summary: \"Abstract negative claim 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-N2 同一 issue\"\n\n- id: \"R13-W1\"\n  summary: \"SCB 命名过度——structural limitation 而非 bias\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W4: 共识指向同一根本问题\"\n\n- id: \"R13-W2\"\n  summary: \"BH 校正 m=16 包含非独立条件\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-W3: seed aggregates 与 component seeds 重叠，应区分 confirmatory vs exploratory\"\n\n- id: \"R13-W3\"\n  summary: \"Missing references: ensemble diversity 文献\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-W7 同一 issue\"\n\n- id: \"R13-W4\"\n  summary: \"论文密度过高，可读性受损\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"R2-W5: \\enlargethispage{6\\baselineskip} + 多处负 vspace，Section 7 仅 1/3 页\"\n\n- id: \"R14-N1\"\n  summary: \"Cross-architecture escape 证据不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群\"\n\n- id: \"R14-N2\"\n  summary: \"Underpowered negative claim\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-N2 同一 issue\"\n\n- id: \"R14-W1\"\n  summary: \"BR 循环论证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-W2 同一 issue\"\n\n- id: \"R14-W2\"\n  summary: \"Observation 1 条件 (iii) 未验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"与 R12-W4 同一 issue\"\n\n- id: \"R14-W3\"\n  summary: \"Novelty positioning vs Huang et al.\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R13-N2 同一 issue\"\n\n- id: \"R14-W5\"\n  summary: \"'Pre-registered' 无注册凭证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-W2: 应改为 'pre-specified'\"\n\n- id: \"R14-W6\"\n  summary: \"Missing references: OpenAI o1/o3\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"R2: o1/o3 是 test-time compute scaling 开创性工作，Section 2 应引用\"\n\n- id: \"R15-M3\"\n  summary: \"Abstract 词数超限\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-W1: 约 202 词，超过 EMNLP 2026 的 200 词硬约束。R1 AGREE\"\n\n- id: \"R15-M4\"\n  summary: \"代码/数据可获取性声明缺失\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-M5: 与 R12-EC1 同一 issue\"\n\n- id: \"R15-W1\"\n  summary: \"Turpin et al. 引用年份错误\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-W3: year={2024} 应为 2023。R1 AGREE\"\n\n- id: \"R16-N1\"\n  summary: \"Cross-architecture escape 过度声明\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群\"\n\n- id: \"R16-N2\"\n  summary: \"Underpowered negative claim\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-N2 同一 issue\"\n\n- id: \"R16-W1\"\n  summary: \"BR/SCB 概念循环\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-W2 同一 issue\"\n\n- id: \"R16-W2\"\n  summary: \"Novelty vs Huang et al.\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R13-N2 同一 issue\"\n\n- id: \"R16-SYS1\"\n  summary: \"论文密度过高\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"与 R13-W4 同一 issue\"\n\n- id: \"R17-N1\"\n  summary: \"Cross-architecture escape n=6\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群\"\n\n- id: \"R17-N2\"\n  summary: \"Underpowered negative claim\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-N2 同一 issue\"\n\n- id: \"R17-N4\"\n  summary: \"BR 循环论证\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-W2 同一 issue\"\n\n- id: \"R17-N5\"\n  summary: \"Novelty vs Huang et al.\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R13-N2 同一 issue\"\n\n- id: \"R17-VL1\"\n  summary: \"Figure 3 causal DAG 尺寸偏小\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 视觉审查 info: Figure 3 仅占左栏顶部约 1/4 面积\"\n\n- id: \"R17-VL2\"\n  summary: \"Figure 4 标签文字偏小\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 视觉审查 info: x轴标签和图例需仔细辨认\"\n\n- id: \"R18-N1\"\n  summary: \"Remark 1与Figure 3间存在claim升级——DPI trivial但C⊥Y|A未证明\"\n  category: method\n  severity: major\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2交叉AGREE\"\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未直接提及此具体 claim 升级问题\"\n\n- id: \"R18-N2\"\n  summary: \"BR应重新框定为degeneration度量而非bias度量\"\n  category: method\n  severity: major\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2交叉AGREE\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W4: BR_excess≈0 证实 BR 完全由 trace-count 结构解释，应区分 structural degeneration vs extraction bias\"\n\n- id: \"R18-M1\"\n  summary: \"遗漏引用: Xie et al. (2023) Self-Evaluation Guided Beam Search\"\n  category: writing\n  severity: minor\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R2建议, R1 AGREE\"\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及，但论文已在 Section 2 引用 xie2023selfevaluation\"\n\n- id: \"R18-M2\"\n  summary: \"Table 1 Mistral-7B multi-seed行间关系不直观\"\n  category: format\n  severity: minor\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及\"\n\n- id: \"R18-M3\"\n  summary: \"56.4%零变量重叠的计算粒度未说明\"\n  category: method\n  severity: minor\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [1]\n      note: \"R1-M3: per-problem? per-dataset? per-constraint pair?\"\n    - round: 19\n      reviewers: [1]\n      note: \"R1-M3 引用 §5.1 原文: 'per-problem average'——论文已说明但表述不够突出\"\n\n- id: \"R18-VL1\"\n  summary: \"Table 1(page 5)数据字号偏小(7-8pt), 符号系统认知负荷高\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: []\n      note: \"R18 视觉审查\"\n    - round: 19\n      reviewers: []\n      note: \"R19 视觉审查确认: Table 1 字号偏小(~7pt)，处于舒适阅读下限\"\n\n# R19 new issues\n\n- id: \"R19-N1\"\n  summary: \"两条引用存在严重元数据错误（byerly2026selfconsistency, dupo2025）\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-N1 发现，R1 交叉 AGREE: byerly2026 作者名(Nicholas→Adam)、年份(2026→2024)、主题三重错误; dupo2025 标题(Process→Preference)、作者(Yang Chenxu→Shuaijie She)错误。模式暗示 LLM-assisted hallucination\"\n\n- id: \"R19-N2\"\n  summary: \"Introduction 使用 'prove' 描述 Observation 1，但 Obs 1 依赖经验条件\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-M1: §1 'We prove this degeneration is structural (Observation 1)' 应改为 'show' 或 'demonstrate'\"\n\n- id: \"R19-W1\"\n  summary: \"Limitations section heading 孤悬（orphan heading）\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 视觉审查 warning: Limitations heading 在 page 8 底部极端位置，正文在 page 9 顶部\"\n\n- id: \"R19-M1\"\n  summary: \"Frontier model Table 2 中 Gemini n_err=12 的 BR 置信区间过宽需标注\"\n  category: experiment\n  severity: minor\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2 minor point 1: n_err=12 的 BR 不应与 n_err=90 的同等权重解读。Table 2 caption 已提及但正文应更突出\"\n\n- id: \"R19-M2\"\n  summary: \"gpt-4o self-extraction (^a) 的 API-based 实现应明确说明\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-M2: Table 2 标 ^a=self-extraction，但闭源 API 的 self-extraction 与开源模型有实现差异\"\n\n- id: \"R19-M3\"\n  summary: \"Section 5.1 中 83.3% vs Appendix Table 80.9% 数字不一致需标注定义差异\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-M3: 前者是 raw constraint fraction，后者是 MaxSAT-weighted，正文应明确标注\"\n\n- id: \"R19-M4\"\n  summary: \"ProcessSim 使用 TF-IDF 而非语义相似度的局限性应在正文提及\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-M4: Appendix R 有 SBERT 替代验证，但主文应简要提及 representation choice limitation\"\n\n- id: \"R19-M5\"\n  summary: \"Missing reference: OpenAI o1/o3 in test-time compute discussion\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"Table 2 包含 o3 结果但 Related Work Section 2 'test-time compute' 段未显式引用 o1/o3 的推理机制工作\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9+ recurring issues\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 19\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及，但 cross-architecture escape 整体证据不足的共识间接涵盖\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 19\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-N3: 两位 reviewer 一致认为 n=6 且 4/6 共享 DeBERTa verifier，应降级为 preliminary observation。R2 补充 'generator < verifier 才有增益' 是 trivial condition\"\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 视觉审查: Figure 1 出现在 page 2 顶部，视觉锚点存在但仍在前 3 页范围内\"\n\n- id: \"R9-VL4\"\n  summary: \"Discussion/Conclusion 展开不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"R2-W5: Section 7 仅约 1/3 页，论文整体密度过高，\\enlargethispage{6\\baselineskip} 等排版 hack\"\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同，两位 reviewer 共识降级为 preliminary observation\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W5: 可能只是 ensemble diversity 效应而非 SCB escape。R2 AGREE 并建议 cross-model majority vote ablation\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-N2 + R2-W2(升级): 10/16 条件 underpowered，Abstract/标题的 blanket negative claim 超出统计证据范围\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-W2: 使用 'pre-registered' 但无 OSF 等注册凭证，应改为 'pre-specified'\"\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W4: 两位 reviewer 从不同角度收敛——R1 从技术层面(BR_excess≈0)、R2 从概念层面(structural limitation vs cognitive bias analogy)。共识：应区分 structural degeneration 和 extraction bias\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及\"\n\n- id: \"R10-I1\"\n  summary: \"'Symbolic Mirage' 概念新颖性——与 Huang/Wan 的 confirmation bias 区别\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-N2: 'advances beyond Huang et al.' claim 过度，核心洞见在 Huang + Condorcet 下可预见。R1 AGREE with nuance: scope extension + formalization 而非 fundamental advance\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: resolved\n  last_seen_round: 17\n  resolution: \"Figure 2, Figure 4 added in main text.\"\n  resolution_round: 17\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"95% bootstrap CIs added for BR.\"\n  resolution_round: 11\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"Renamed to Observation 1, conditions made explicit, empirical support section added.\"\n  resolution_round: 14\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R9-W3/R10-N3 同一问题群，R19 两位 reviewer 共识\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-N2: 建议 Abstract 改为 'no evidence exceeding ~2pp'。R2 升级为 Must-Fix\"\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-W2: 'pre-registered' 无注册凭证\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W1: BR>1 是 source-attribution 的数学必然，permutation BR_excess≈0。R2 AGREE: BR 度量 degeneration 而非 independent bias signal\"\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"R2-W4 相关: SCB 命名暗示 cognitive bias 类比但实质是 structural limitation\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-N2: 'advances beyond' 应改为 'extends and formalizes'。R1 AGREE with nuance\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及\"\n\n- id: \"R11-W7\"\n  summary: \"Ensemble diversity 文献缺失\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1 + R2 均指出缺少 Dietterich (2000), Krogh & Vedelsby (1994/1995)\"\n\n- id: \"R12-N1\"\n  summary: \"Capability-gap pattern 证据不足以支撑 top-level contribution\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群\"\n\n- id: \"R12-N2\"\n  summary: \"Underpowered tests 与 negative claim 之间存在 gap\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-N2 同一 issue\"\n\n- id: \"R12-W1\"\n  summary: \"Cross-architecture escape 可能是 ensemble diversity\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2 AGREE: 需 cross-model majority vote ablation 区分假说\"\n\n- id: \"R12-W4\"\n  summary: \"Observation 1 条件验证不完整\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-W4: 条件 (iii) uniform constraint yield 缺乏 per-trace 分布统计量验证\"\n\n- id: \"R12-EC1\"\n  summary: \"代码/数据可获取性声明缺失\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-M5: 无 'code will be released upon acceptance' 声明\"\n\n- id: \"R13-N2\"\n  summary: \"Novelty claim 相对 Huang et al. (2024) 的增量有限\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-N2: 'advances beyond' 过度声明。R1 AGREE: scope extension + formalization 而非 fundamental advance\"\n\n- id: \"R13-N3\"\n  summary: \"Abstract negative claim 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-N2 同一 issue\"\n\n- id: \"R13-W1\"\n  summary: \"SCB 命名过度——structural limitation 而非 bias\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W4: 共识指向同一根本问题\"\n\n- id: \"R13-W2\"\n  summary: \"BH 校正 m=16 包含非独立条件\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-W3: seed aggregates 与 component seeds 重叠，应区分 confirmatory vs exploratory\"\n\n- id: \"R13-W3\"\n  summary: \"Missing references: ensemble diversity 文献\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-W7 同一 issue\"\n\n- id: \"R13-W4\"\n  summary: \"论文密度过高，可读性受损\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"R2-W5: \\enlargethispage{6\\baselineskip} + 多处负 vspace，Section 7 仅 1/3 页\"\n\n- id: \"R14-N1\"\n  summary: \"Cross-architecture escape 证据不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群\"\n\n- id: \"R14-N2\"\n  summary: \"Underpowered negative claim\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-N2 同一 issue\"\n\n- id: \"R14-W1\"\n  summary: \"BR 循环论证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-W2 同一 issue\"\n\n- id: \"R14-W2\"\n  summary: \"Observation 1 条件 (iii) 未验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"与 R12-W4 同一 issue\"\n\n- id: \"R14-W3\"\n  summary: \"Novelty positioning vs Huang et al.\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R13-N2 同一 issue\"\n\n- id: \"R14-W5\"\n  summary: \"'Pre-registered' 无注册凭证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-W2: 应改为 'pre-specified'\"\n\n- id: \"R14-W6\"\n  summary: \"Missing references: OpenAI o1/o3\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"R2: o1/o3 是 test-time compute scaling 开创性工作，Section 2 应引用\"\n\n- id: \"R15-M3\"\n  summary: \"Abstract 词数超限\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-W1: 约 202 词，超过 EMNLP 2026 的 200 词硬约束。R1 AGREE\"\n\n- id: \"R15-M4\"\n  summary: \"代码/数据可获取性声明缺失\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-M5: 与 R12-EC1 同一 issue\"\n\n- id: \"R15-W1\"\n  summary: \"Turpin et al. 引用年份错误\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-W3: year={2024} 应为 2023。R1 AGREE\"\n\n- id: \"R16-N1\"\n  summary: \"Cross-architecture escape 过度声明\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群\"\n\n- id: \"R16-N2\"\n  summary: \"Underpowered negative claim\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-N2 同一 issue\"\n\n- id: \"R16-W1\"\n  summary: \"BR/SCB 概念循环\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-W2 同一 issue\"\n\n- id: \"R16-W2\"\n  summary: \"Novelty vs Huang et al.\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R13-N2 同一 issue\"\n\n- id: \"R16-SYS1\"\n  summary: \"论文密度过高\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"与 R13-W4 同一 issue\"\n\n- id: \"R17-N1\"\n  summary: \"Cross-architecture escape n=6\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群\"\n\n- id: \"R17-N2\"\n  summary: \"Underpowered negative claim\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-N2 同一 issue\"\n\n- id: \"R17-N4\"\n  summary: \"BR 循环论证\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R11-W2 同一 issue\"\n\n- id: \"R17-N5\"\n  summary: \"Novelty vs Huang et al.\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"与 R13-N2 同一 issue\"\n\n- id: \"R17-VL1\"\n  summary: \"Figure 3 causal DAG 尺寸偏小\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 视觉审查 info: Figure 3 仅占左栏顶部约 1/4 面积\"\n\n- id: \"R17-VL2\"\n  summary: \"Figure 4 标签文字偏小\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 视觉审查 info: x轴标签和图例需仔细辨认\"\n\n- id: \"R18-N1\"\n  summary: \"Remark 1与Figure 3间存在claim升级——DPI trivial但C⊥Y|A未证明\"\n  category: method\n  severity: major\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2交叉AGREE\"\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未直接提及此具体 claim 升级问题\"\n\n- id: \"R18-N2\"\n  summary: \"BR应重新框定为degeneration度量而非bias度量\"\n  category: method\n  severity: major\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2交叉AGREE\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W4: BR_excess≈0 证实 BR 完全由 trace-count 结构解释，应区分 structural degeneration vs extraction bias\"\n\n- id: \"R18-M1\"\n  summary: \"遗漏引用: Xie et al. (2023) Self-Evaluation Guided Beam Search\"\n  category: writing\n  severity: minor\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R2建议, R1 AGREE\"\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及，但论文已在 Section 2 引用 xie2023selfevaluation\"\n\n- id: \"R18-M2\"\n  summary: \"Table 1 Mistral-7B multi-seed行间关系不直观\"\n  category: format\n  severity: minor\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19(fresh) 未单独提及\"\n\n- id: \"R18-M3\"\n  summary: \"56.4%零变量重叠的计算粒度未说明\"\n  category: method\n  severity: minor\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [1]\n      note: \"R1-M3: per-problem? per-dataset? per-constraint pair?\"\n    - round: 19\n      reviewers: [1]\n      note: \"R1-M3 引用 §5.1 原文: 'per-problem average'——论文已说明但表述不够突出\"\n\n- id: \"R18-VL1\"\n  summary: \"Table 1(page 5)数据字号偏小(7-8pt), 符号系统认知负荷高\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: []\n      note: \"R18 视觉审查\"\n    - round: 19\n      reviewers: []\n      note: \"R19 视觉审查确认: Table 1 字号偏小(~7pt)，处于舒适阅读下限\"\n\n# R19 new issues\n\n- id: \"R19-N1\"\n  summary: \"两条引用存在严重元数据错误（byerly2026selfconsistency, dupo2025）\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2-N1 发现，R1 交叉 AGREE: byerly2026 作者名(Nicholas→Adam)、年份(2026→2024)、主题三重错误; dupo2025 标题(Process→Preference)、作者(Yang Chenxu→Shuaijie She)错误。模式暗示 LLM-assisted hallucination\"\n\n- id: \"R19-N2\"\n  summary: \"Introduction 使用 'prove' 描述 Observation 1，但 Obs 1 依赖经验条件\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-M1: §1 'We prove this degeneration is structural (Observation 1)' 应改为 'show' 或 'demonstrate'\"\n\n- id: \"R19-W1\"\n  summary: \"Limitations section heading 孤悬（orphan heading）\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 视觉审查 warning: Limitations heading 在 page 8 底部极端位置，正文在 page 9 顶部\"\n\n- id: \"R19-M1\"\n  summary: \"Frontier model Table 2 中 Gemini n_err=12 的 BR 置信区间过宽需标注\"\n  category: experiment\n  severity: minor\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R2 minor point 1: n_err=12 的 BR 不应与 n_err=90 的同等权重解读。Table 2 caption 已提及但正文应更突出\"\n\n- id: \"R19-M2\"\n  summary: \"gpt-4o self-extraction (^a) 的 API-based 实现应明确说明\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-M2: Table 2 标 ^a=self-extraction，但闭源 API 的 self-extraction 与开源模型有实现差异\"\n\n- id: \"R19-M3\"\n  summary: \"Section 5.1 中 83.3% vs Appendix Table 80.9% 数字不一致需标注定义差异\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-M3: 前者是 raw constraint fraction，后者是 MaxSAT-weighted，正文应明确标注\"\n\n- id: \"R19-M4\"\n  summary: \"ProcessSim 使用 TF-IDF 而非语义相似度的局限性应在正文提及\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [1]\n      note: \"R1-M4: Appendix R 有 SBERT 替代验证，但主文应简要提及 representation choice limitation\"\n\n- id: \"R19-M5\"\n  summary: \"Missing reference: OpenAI o1/o3 in test-time compute discussion\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [2]\n      note: \"Table 2 包含 o3 结果但 Related Work Section 2 'test-time compute' 段未显式引用 o1/o3 的推理机制工作\"\n"
  }
}
```

</details>

---


### Tool result

_source line 1993 · 2026-05-23T14:04:34.266294+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml\", \"bytes\": 23674}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 204
}
```

</details>

---


### Tool call

_source line 1994 · 2026-05-23T14:07:38.534998+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "symb_invariant_consensus",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "report": "# 审稿报告 — Round 19 (Fresh)\n\n**论文**: Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n\n---\n\n## Summary\n\n本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取逻辑约束，通过 Z3 MAX-SAT 求解选择答案。核心发现是 negative result：SICA 在 6 个模型（7B–32B）、3 个推理数据集上均未显著优于 majority voting（Self-Consistency）。论文将此诊断为\"symbolic confirmation bias\"——自提取约束系统性地追踪模型自身的答案分布而非提供独立信号。27 种 training-free 修补策略均失败。形式化分析提供了 Observation 1（argmax preservation under degeneration）和 Remark 1（DPI information ceiling）。跨架构验证（DeBERTa NLI）在最弱生成器上显示初步逃逸（+6.67pp）。三个零成本诊断指标（K_eff, BR, C₀）在 60 个条件上 correctly characterize failure modes。\n\n---\n\n## Strengths\n\n1. **统计方法论极为扎实** [R1 Strength 1, R2 Strength 1, 共识]：McNemar paired test + BH FDR correction (m=16) + TOST equivalence testing + Bootstrap CI (10,000 resamples) + Power analysis + multi-seed replication 的完整组合在 NLP 论文中极为罕见。诚实报告 underpowered conditions 和 power limitations 体现了高水准的科学诚信。\n\n2. **Oracle control 设计精巧** [R1 Strength 2]：用 gold FOL/DSL 标注替换 self-extracted constraints 的对照实验（+29.90pp FOLIO, +17.17pp ProofWriter, p < 10⁻⁷）清晰地将问题定位在 extraction 而非 solver。这是本文最有说服力的实验设计。\n\n3. **27 种 remediation 变体的系统化测试** [R1 Strength 3, R2 Strength 3, 共识]：涵盖 prompt-level、method-level、paradigm、solver、input diversity、filtering 六个维度，彻底排除了 \"换个方法就行\" 的反驳。Independence-accuracy trade-off 的实证支持充分。\n\n4. **形式化声明命名克制得当** [R1 Strength 4]：使用 Observation 和 Remark 而非 Theorem/Proposition，诚实反映了其依赖经验条件的本质。\n\n5. **诊断框架有实践价值** [R1 Strength 5, R2 Strength 4]：C₀ < 5%, K_eff ≤ 1.30, BR + SC regime 三个 zero-cost diagnostics 在 60 个条件上 correctly characterize failure modes，prospective validation 在 held-out families (LLaMA, Qwen3) 上通过。对从业者有直接实用价值。\n\n6. **Entropy decomposition 分析精细** [R1 Strength 6]：low-entropy 问题 Δ ≈ 0、high-entropy 问题方向取决于 SC regime 的发现强化了 regime-dependent 叙事。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1** [critical, R2-N1, R1 交叉 AGREE] **两条引用存在严重元数据错误**\n\n- `byerly2026selfconsistency`：bib 记录作者 \"Nicholas Byerly and Daniel Khashabi, 2026\"，但 arXiv:2411.01101 实际作者是 **Adam Byerly**，发表于 **2024**，实际标题/主题（positional bias on long-context problems）与引用标题（mathematical reasoning）完全不同。作者名、年份、主题三重错误。\n- `dupo2025`：bib 记录标题 \"DuPO: Dual **Process** Optimization\"、一作 \"Yang, Chenxu\"，但 arXiv:2508.14460 实际标题是 \"DuPO: Enabling Reliable LLM Self-Verification via Dual **Preference** Optimization\"，一作为 **Shuaijie She**，Yang Chenxu 不在作者列表中。\n- 错误模式（真实 arXiv ID 配上错误元数据）高度暗示 LLM-assisted hallucination。byerly2026 在 Related Work 中支持 \"SC gains plateau\" 论点，dupo2025 在 training-based verification 段落中被引用——文献支撑存在漏洞。\n- **要求**：对全部参考文献进行系统性交叉验证，修正所有错误条目。\n\n**MF-2** [critical, R2-N2, R1 AGREE with nuance] **\"Advances beyond Huang et al. (2024)\" 的 claim 过度**\n\n- 论文在 Abstract、Section 1（Introduction）、Section 2（Related Work）、Section 7（Discussion）至少四处使用 \"advances beyond Huang et al. (2024)\" 措辞。\n- Huang et al. (ICLR 2024) 已建立 \"LLMs cannot self-correct reasoning without external feedback\" 核心结论。本文的贡献是 (a) 将此洞见扩展到 formal symbolic verification setting，(b) 提供 Markov chain 形式化（Observation 1, Remark 1），(c) 系统排除 27 种 remediation——这是 **scope extension + formalization**，而非 fundamental insight 上的 \"advance beyond\"。\n- 核心洞见（自提取信息因与答案来自同一信息源而缺乏独立性）在 Huang et al. + Condorcet Jury Theorem 框架下是可预见的。\n- **要求**：将 \"advances beyond\" 改为更精确的表述如 \"extends and formalizes ... in the context of formal self-verification\"。\n\n**MF-3** [critical, R1-N1 + R2-N3, 共识] **Cross-architecture escape 证据不足以支撑 top-level contribution**\n\n- Capability-gap pattern 仅基于 6 个 verifier-generator 组合（Spearman ρ=1.0, p=0.003），其中 **4/6 共享同一 DeBERTa verifier**，实际有效自由度远小于 n=6。\n- Table 3 的 n=4 generators 全部 paired with 同一 DeBERTa-large-mnli，排列空间仅 24 种。\n- \"Generator SC < verifier standalone accuracy 才有增益\" 可能是 **trivial condition**——本质上是 \"用更好的模型替代更差的模型\" 的必然结果，不需要 information independence 理论。\n- R1 额外指出：增益可能只是 **ensemble diversity 效应**（Dietterich 2000），而非 SCB escape。需要 cross-model majority vote ensemble 作为 ablation 区分两种假说。\n- Domain-adapted verifier (99.67% standalone) 引入了 training，与 training-free 叙事线矛盾。论文自己承认 \"directional evidence rather than a proposed method\"，但叙事结构仍将其作为 escape 证据呈现。\n- **要求**：将 Contribution 3 从并列贡献降级为 \"preliminary observation\"，或增加不同架构的 verifier + cross-model majority vote ablation。\n\n**MF-4** [critical, R1-N2 + R2-W2(升级), 共识] **10/16 条件 underpowered，中心论断表述超出统计证据范围**\n\n- Appendix D Table 6：3 个 confirmatory conditions 的 observed power 均低于 21%（Qwen-14B FOLIO+PW: 5.7%, LLaMA-8B StrategyQA: 20.6%, LLaMA-8B FOLIO: 18.6%）。MDE 为 1.86–4.84pp。\n- TOST 等价检验仅 4/16 条件确认等价（±2pp margin），10 条件 underpowered。\n- Abstract \"We find no evidence of improvement\" 和标题 \"No Detectable Improvement\" 构成 blanket negative claim，但统计证据仅能排除 >~2pp 的效果。\"Absence of evidence is not evidence of absence\" 在正文中有提及（Section 4），但 Abstract/标题层面的表述未反映这一 nuance。\n- **要求**：(a) Abstract 改为 \"no evidence of improvement exceeding ~2 percentage points\"；(b) 在 Discussion 中显式论证 <2pp 在 4.5× 计算开销下无实际价值，将 power limitation 转化为 practical insignificance 论证。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [warning, R1-W1 + R2-W4, 共识] **BR/SCB 概念框架混淆 structural degeneration 与 extraction bias**\n\n- R1 从技术层面指出：source-attribution scoring 下 BR > 1 是 trace-count 分布的**数学必然结果**。Permutation test 证实 BR_excess ≈ 0 (p > 0.7, §5.1)——BR 完全由 trace-count 结构解释，不含 extraction 过程的额外偏差。BR 度量的是 degeneration 程度，不是独立于 Observation 1 的 bias 证据。\n- R2 从概念层面指出：\"Symbolic **Confirmation Bias**\" 暗示 cognitive bias 类比（主动寻找支持性证据），但实际机制是 structural limitation（约束和答案来自同一信息源而结构性耦合）。\n- 两个批评收敛到同一结论：论文应更清楚地区分 \"structural degeneration\"（Observation 1 的后果）和 \"extraction bias\"（如果存在的话）。目前混淆使 BR 看起来提供了 Observation 1 之外的独立证据，但实际上没有。\n- **建议**：(a) 在首次定义 SCB 时明确说明这是 structural limitation 而非 cognitive bias 类比；(b) 报告 BR_excess 作为判断是否存在 extraction-level 额外偏差的指标；(c) 考虑更精确的术语如 \"symbolic information collapse\" 或 \"self-referential degeneration\"。\n\n**SF-2** [warning, R2-W1, R1 AGREE] **Abstract 超过 200 词限制**\n\n- 经去除 LaTeX 命令后词数统计约 202 词，超过 EMNLP 2026/ARR 的 200-word 硬约束。虽仅超出 2 词，但属明确格式违规。\n\n**SF-3** [warning, R1-W2, R2 AGREE] **\"Pre-registered\" margin ±2pp 无注册凭证**\n\n- Section 4 使用 \"pre-registered margin ±2 pp\" 但未提供 OSF/AsPredicted 等预注册链接。\"Pre-registered\" 在实证研究中有严格操作定义。改为 \"pre-specified\" 或 \"predetermined\" 即可。\n\n**SF-4** [warning, R1-W3, R2 AGREE with nuance] **BH correction m=16 包含非独立条件**\n\n- 16 个条件中包含 Mistral-7B×FOLIO 的 3 个单独 seed (s123, s456, s789) 和 1 个 3-seed aggregate，以及 Qwen2.5-14B×FOLIO 的 4-seed aggregate。Aggregate 是 component seeds 的函数，非独立检验。虽然更大的 m 使 BH 更保守，但方法论应更干净地区分 confirmatory vs exploratory 条件。\n\n**SF-5** [warning, R1-W4, R2 AGREE] **Observation 1 条件 (iii) \"approximately uniform constraint yield\" 缺乏系统验证**\n\n- 条件 (i) |C\\| ≈ 0 由 Z3 rejection rate 3.4% 实证支持，条件 (ii) source-attribution 是系统设计，但条件 (iii) 缺乏直接验证。论文未报告 per-trace constraint yield 的分布统计量（mean, std, CV），应按 answer group 分层报告。\n\n**SF-6** [warning, R2-W3, R1 AGREE] **Turpin et al. 引用年份错误**\n\n- references.bib 中 `turpin2024language` 记录 year={2024}，但 \"Language Models Don't Always Say What They Think\" 发表于 NeurIPS **2023**。\n\n**SF-7** [warning, R2-W5, R1 AGREE minor] **论文密度过高，可读性受损**\n\n- LaTeX source 含 `\\enlargethispage{6\\baselineskip}` (main.tex:72)、`\\vspace{-4mm}` (main.tex:76)、`\\vspace{-1.5mm}` (main.tex:73) 等排版 hacks。Section 7 (Discussion and Conclusion) 仅约 1/3 页。Figure 4 信息密度极高但难以快速 parse。建议将部分内容移入 appendix 以提升可读性。\n\n**SF-8** [warning, R1-M1] **Introduction 使用 \"prove\" 描述 Observation 1**\n\n- §1: \"We prove this degeneration is structural (Observation 1)\"——Observation 1 依赖经验条件 (iii)，\"prove\" 过强，应改为 \"show\" 或 \"demonstrate\"。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键判断上达成完全共识：\n\n1. **Overall 3.0 (Findings)**：R1 初评 3.5，交叉审议后被 R2 的 novelty 和引用论点说服，下调至 3.0。\n2. **Cross-architecture escape 应降级**：n=6（实际 <6 due to shared verifier）不足以支撑 top-level contribution。\"Generator < verifier 才有增益\" 可能是 trivial condition。可能只是 ensemble diversity 效应。\n3. **Underpowered claim 需精确化**：Abstract/标题的 blanket negative claim 超出统计证据范围。\n4. **SCB/BR 概念框架需澄清**：BR > 1 是 structural 而非 bias 证据；SCB 命名暗示 correctable deficiency 但实际是 structural limitation。\n5. **引用错误必须修正**：两条引用元数据严重错误，需系统性交叉验证全部参考文献。\n6. **\"Advances beyond Huang et al.\" 表述过度**：应改为 \"extends and formalizes\"。\n7. **统计方法论是论文最大优势**：McNemar + BH + TOST + Bootstrap + Power analysis 的完整组合在 NLP 论文中极为罕见，使 negative result 高度可信。\n8. **论文适合 Findings 而非 Conference**：贡献定位是 confirmation + formalization（用大规模实验确认并形式化了一个 expected result），而非 discovery。统计严谨性满足 Findings 的 soundness 要求，但 excitement/novelty 不够 Conference。\n\n---\n\n## Reviewer Divergence [REBUT]\n\n无重大分歧。R1 初始评分比 R2 高 0.5 分，但在交叉审议后被说服并下调，最终收敛。\n\n---\n\n## Questions\n\n1. **BR_excess ≈ 0 意味着什么？** Permutation test 显示经验 BR 完全由 trace-count 结构解释（BR_excess ≈ 0, p > 0.7）——如果没有超出 base-rate 的额外 extraction bias，\"symbolic confirmation bias\" 是否应该重新命名？\n2. **Observation 1 条件 (iii) 的验证数据？** 每条 trace 平均产生多少 constraints？标准差？不同 answer group 之间的 yield 差异？\n3. **为什么不测试 non-NLI independent verifier？** Cross-model majority vote ensemble 是否也能产生类似增益？这将区分 \"information independence\" 和 \"ensemble diversity\" 假说。\n4. **TOST margin 的 \"pre-registered\" 指什么？** 是否有 OSF 或类似平台的注册记录？\n5. **如果将约束用于 re-prompting 而非 MAX-SAT scoring，结果是否不同？** 27 种策略是否都在 extraction-aggregation paradigm 内？\n6. **Domain-adapted verifier 的增益 (+12.67pp) 是否主要来自 domain-specific training 而非 structural independence？**\n\n---\n\n## Missing References\n\n1. **Ensemble diversity 经典文献** [R1 + R2 共识]：Dietterich (2000) \"Ensemble Methods in Machine Learning\", Krogh & Vedelsby (1995) \"Neural Network Ensembles, Cross Validation, and Active Learning\"——Section 2 ensemble theory 段落和 Section 6 cross-architecture discussion 应引用并回应 ensemble diversity 假说。\n2. **OpenAI o1/o3 reasoning models** [R2]：Table 2 包含 o3 cross-model extraction 结果，但 Section 2 \"test-time compute\" 段落未显式讨论 o1/o3 内部推理链机制及 SICA paradigm 的适用性。\n3. **Cobbe et al. (2021) GSM8K verifier** [R1]：独立 verifier 提升推理性能的早期实例，与 Section 6 的 cross-architecture escape 直接相关。\n\n---\n\n## External Review\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（1 warning, 9 info）。\n\n**Warning:**\n- Limitations section heading 出现在 page 8 底部极端位置（orphan heading），后续仅 2 行正文在同一页，大部分 Limitations 内容在 page 9 顶部。建议用 `\\needspace` 调整。\n\n**Info（主要发现）:**\n- Figure 1 出现在 page 2 顶部，pipeline 架构图提供清晰视觉锚点，Title-Abstract-Figure 1 叙事一致性好。\n- Figure 2 散点图图例文字偏小（约 6-7pt），建议适当放大。\n- Table 1 字号偏小（~7pt），处于舒适阅读下限。booktabs 风格正确，表头分区清晰。\n- Figure 3 Causal DAG 尺寸明显偏小（仅占左栏 1/4 面积），作为核心概念图建议放大。\n- Figure 4 条形图 x 轴标签和图例文字偏小，分类名称需仔细辨认。\n- Appendix 单页含 4 个表格，密度极高但作为 appendix 可接受。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 — Findings（可被 Findings 接收）**\n\n**Reviewer 评分汇总：**\n\n| 维度 | R1 (交叉后) | R2 | 综合 |\n|------|------------|-----|------|\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 2.5/5 | 2.5/5 | 2.5/5 |\n| Reproducibility | 3/5 | 4/5 | 3.5/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n| **Overall** | **3.0** | **3.0** | **3.0** |\n\n**置信度：4/5**（两位 Reviewer 在各自专长领域（统计方法论 / 文献与 novelty）均有充分把握，且交叉审议后完全收敛）\n\n**理由：**\n\n这是一篇实验执行质量高、方法论严谨的 negative result 论文。60 个条件、9 个模型、27 种修补策略的系统排除确实超出了多数同类工作的证据标准。Oracle control 精巧，诊断框架有实用价值，统计方法论在 NLP 领域属顶级水准。\n\n但在 excitement 维度存在根本性限制：核心洞见（自提取信息因与答案来自同一信息源而缺乏独立性）在 Huang et al. (ICLR 2024) 和 Condorcet Jury Theorem 框架下是可预见的。论文的贡献更准确的定位是 confirmation（用大规模实验确认 expected result）+ formalization（Markov chain model, diagnostics），而非 discovery。Cross-architecture escape 作为唯一正面贡献过于初步（n=6, shared verifier, 可能只是 ensemble diversity）。两条引用的元数据严重错误进一步降低了整体学术质量评估。\n\n如果 MF-1（引用修正）、MF-2（novelty claim tempered）、MF-4（negative claim 精确化）得到修正，本文作为 Findings 论文是合适的——为社区提供了有价值的 negative evidence 和实用的诊断工具。但以目前的 novelty framing，不足以支撑 Conference main 接收。\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract (p.1):**\n- 约 202 词，超过 200 词限制 [SF-2]\n- \"advancing beyond Huang et al. (2024)'s findings\" → \"extending and formalizing\" [MF-2]\n- \"We find no evidence of improvement\" → \"no evidence of improvement exceeding ~2 percentage points\" [MF-4]\n- \"self-extracted\" 出现 4 次，可适当减少重复\n\n**Introduction (§1, p.1-2):**\n- \"We prove this degeneration is structural\" → \"We show\" [SF-8]\n- Contribution 3 (\"Cross-architecture escape\") 应标注 \"preliminary\" [MF-3]\n- Figure 1 pipeline 图清晰有效\n\n**Related Work (§2, p.2-3):**\n- 结构良好（5 段覆盖 5 个维度），引用密度高\n- byerly2026selfconsistency 和 dupo2025 需修正 [MF-1]\n- turpin2024language 年份 2024→2023 [SF-6]\n- 缺少 ensemble diversity 经典文献和 OpenAI o1/o3 引用\n\n**Method (§3, p.3-4):**\n- SICA pipeline 描述清晰完整，数学公式和算法规范\n- Observation 1 条件 (iii) 需系统验证 [SF-5]\n- BR 定义需与 \"structural degeneration\" 而非 \"bias\" 关联 [SF-1]\n- α=0.5 sensitivity 在 Appendix 有验证，正文可简要提及\n\n**Results (§4, p.4-5):**\n- Table 1 信息密集但结构清晰，regime 分类有效\n- \"pre-registered margin\" → \"pre-specified margin\" [SF-3]\n- BH m=16 应标注 confirmatory vs exploratory [SF-4]\n- Figure 2 regime scatter 有效传达了核心模式\n\n**Analysis (§5, p.5-7):**\n- §5.1 SCB 分析是论文最有洞察力的部分\n- 但 BR_excess ≈ 0 + permutation test 的含义未充分 reconcile with \"bias\" 叙事 [SF-1]\n- §5.2 Remediation 27 种变体的穷举测试令人信服\n- §5.3 Diagnostic framework 有实践价值，prospective validation 是加分项\n- Figure 3 Causal DAG 尺寸偏小 [视觉审查]\n- Figure 4 信息密度极高，考虑简化正文版本\n\n**Escaping the Bottleneck (§6, p.7-8):**\n- Cross-architecture escape 结果有趣但证据不足 [MF-3]\n- 需要 ensemble diversity ablation 区分假说\n- Domain-adapted verifier 与 training-free 叙事的张力需更明确讨论\n- Table 3 仅 4 个 generators 共享 1 个 verifier，统计说服力有限\n\n**Discussion (§7, p.8):**\n- 过于简短（~1/3 页），应更充分展开\n- \"advancing beyond Huang et al.\" → \"extending and formalizing\" [MF-2]\n- 缺少对 practical implications 和 future directions 的更具体讨论\n\n**Limitations (p.8-9):**\n- 内容合理（模型范围、语言、训练方法、statistical power），简短覆盖 3 个主要限制\n- Orphan heading 问题 [视觉审查 warning]\n\n**Appendix:**\n- 内容丰富（prompt templates, pseudocode, statistical analyses, case studies, ablations）\n- 对论文完整性有重要支撑\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "report": "# 审稿报告 — Round 19 (Fresh)\n\n**论文**: Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n\n---\n\n## Summary\n\n本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取逻辑约束，通过 Z3 MAX-SAT 求解选择答案。核心发现是 negative result：SICA 在 6 个模型（7B–32B）、3 个推理数据集上均未显著优于 majority voting（Self-Consistency）。论文将此诊断为\"symbolic confirmation bias\"——自提取约束系统性地追踪模型自身的答案分布而非提供独立信号。27 种 training-free 修补策略均失败。形式化分析提供了 Observation 1（argmax preservation under degeneration）和 Remark 1（DPI information ceiling）。跨架构验证（DeBERTa NLI）在最弱生成器上显示初步逃逸（+6.67pp）。三个零成本诊断指标（K_eff, BR, C₀）在 60 个条件上 correctly characterize failure modes。\n\n---\n\n## Strengths\n\n1. **统计方法论极为扎实** [R1 Strength 1, R2 Strength 1, 共识]：McNemar paired test + BH FDR correction (m=16) + TOST equivalence testing + Bootstrap CI (10,000 resamples) + Power analysis + multi-seed replication 的完整组合在 NLP 论文中极为罕见。诚实报告 underpowered conditions 和 power limitations 体现了高水准的科学诚信。\n\n2. **Oracle control 设计精巧** [R1 Strength 2]：用 gold FOL/DSL 标注替换 self-extracted constraints 的对照实验（+29.90pp FOLIO, +17.17pp ProofWriter, p < 10⁻⁷）清晰地将问题定位在 extraction 而非 solver。这是本文最有说服力的实验设计。\n\n3. **27 种 remediation 变体的系统化测试** [R1 Strength 3, R2 Strength 3, 共识]：涵盖 prompt-level、method-level、paradigm、solver、input diversity、filtering 六个维度，彻底排除了 \"换个方法就行\" 的反驳。Independence-accuracy trade-off 的实证支持充分。\n\n4. **形式化声明命名克制得当** [R1 Strength 4]：使用 Observation 和 Remark 而非 Theorem/Proposition，诚实反映了其依赖经验条件的本质。\n\n5. **诊断框架有实践价值** [R1 Strength 5, R2 Strength 4]：C₀ < 5%, K_eff ≤ 1.30, BR + SC regime 三个 zero-cost diagnostics 在 60 个条件上 correctly characterize failure modes，prospective validation 在 held-out families (LLaMA, Qwen3) 上通过。对从业者有直接实用价值。\n\n6. **Entropy decomposition 分析精细** [R1 Strength 6]：low-entropy 问题 Δ ≈ 0、high-entropy 问题方向取决于 SC regime 的发现强化了 regime-dependent 叙事。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1** [critical, R2-N1, R1 交叉 AGREE] **两条引用存在严重元数据错误**\n\n- `byerly2026selfconsistency`：bib 记录作者 \"Nicholas Byerly and Daniel Khashabi, 2026\"，但 arXiv:2411.01101 实际作者是 **Adam Byerly**，发表于 **2024**，实际标题/主题（positional bias on long-context problems）与引用标题（mathematical reasoning）完全不同。作者名、年份、主题三重错误。\n- `dupo2025`：bib 记录标题 \"DuPO: Dual **Process** Optimization\"、一作 \"Yang, Chenxu\"，但 arXiv:2508.14460 实际标题是 \"DuPO: Enabling Reliable LLM Self-Verification via Dual **Preference** Optimization\"，一作为 **Shuaijie She**，Yang Chenxu 不在作者列表中。\n- 错误模式（真实 arXiv ID 配上错误元数据）高度暗示 LLM-assisted hallucination。byerly2026 在 Related Work 中支持 \"SC gains plateau\" 论点，dupo2025 在 training-based verification 段落中被引用——文献支撑存在漏洞。\n- **要求**：对全部参考文献进行系统性交叉验证，修正所有错误条目。\n\n**MF-2** [critical, R2-N2, R1 AGREE with nuance] **\"Advances beyond Huang et al. (2024)\" 的 claim 过度**\n\n- 论文在 Abstract、Section 1（Introduction）、Section 2（Related Work）、Section 7（Discussion）至少四处使用 \"advances beyond Huang et al. (2024)\" 措辞。\n- Huang et al. (ICLR 2024) 已建立 \"LLMs cannot self-correct reasoning without external feedback\" 核心结论。本文的贡献是 (a) 将此洞见扩展到 formal symbolic verification setting，(b) 提供 Markov chain 形式化（Observation 1, Remark 1），(c) 系统排除 27 种 remediation——这是 **scope extension + formalization**，而非 fundamental insight 上的 \"advance beyond\"。\n- 核心洞见（自提取信息因与答案来自同一信息源而缺乏独立性）在 Huang et al. + Condorcet Jury Theorem 框架下是可预见的。\n- **要求**：将 \"advances beyond\" 改为更精确的表述如 \"extends and formalizes ... in the context of formal self-verification\"。\n\n**MF-3** [critical, R1-N1 + R2-N3, 共识] **Cross-architecture escape 证据不足以支撑 top-level contribution**\n\n- Capability-gap pattern 仅基于 6 个 verifier-generator 组合（Spearman ρ=1.0, p=0.003），其中 **4/6 共享同一 DeBERTa verifier**，实际有效自由度远小于 n=6。\n- Table 3 的 n=4 generators 全部 paired with 同一 DeBERTa-large-mnli，排列空间仅 24 种。\n- \"Generator SC < verifier standalone accuracy 才有增益\" 可能是 **trivial condition**——本质上是 \"用更好的模型替代更差的模型\" 的必然结果，不需要 information independence 理论。\n- R1 额外指出：增益可能只是 **ensemble diversity 效应**（Dietterich 2000），而非 SCB escape。需要 cross-model majority vote ensemble 作为 ablation 区分两种假说。\n- Domain-adapted verifier (99.67% standalone) 引入了 training，与 training-free 叙事线矛盾。论文自己承认 \"directional evidence rather than a proposed method\"，但叙事结构仍将其作为 escape 证据呈现。\n- **要求**：将 Contribution 3 从并列贡献降级为 \"preliminary observation\"，或增加不同架构的 verifier + cross-model majority vote ablation。\n\n**MF-4** [critical, R1-N2 + R2-W2(升级), 共识] **10/16 条件 underpowered，中心论断表述超出统计证据范围**\n\n- Appendix D Table 6：3 个 confirmatory conditions 的 observed power 均低于 21%（Qwen-14B FOLIO+PW: 5.7%, LLaMA-8B StrategyQA: 20.6%, LLaMA-8B FOLIO: 18.6%）。MDE 为 1.86–4.84pp。\n- TOST 等价检验仅 4/16 条件确认等价（±2pp margin），10 条件 underpowered。\n- Abstract \"We find no evidence of improvement\" 和标题 \"No Detectable Improvement\" 构成 blanket negative claim，但统计证据仅能排除 >~2pp 的效果。\"Absence of evidence is not evidence of absence\" 在正文中有提及（Section 4），但 Abstract/标题层面的表述未反映这一 nuance。\n- **要求**：(a) Abstract 改为 \"no evidence of improvement exceeding ~2 percentage points\"；(b) 在 Discussion 中显式论证 <2pp 在 4.5× 计算开销下无实际价值，将 power limitation 转化为 practical insignificance 论证。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [warning, R1-W1 + R2-W4, 共识] **BR/SCB 概念框架混淆 structural degeneration 与 extraction bias**\n\n- R1 从技术层面指出：source-attribution scoring 下 BR > 1 是 trace-count 分布的**数学必然结果**。Permutation test 证实 BR_excess ≈ 0 (p > 0.7, §5.1)——BR 完全由 trace-count 结构解释，不含 extraction 过程的额外偏差。BR 度量的是 degeneration 程度，不是独立于 Observation 1 的 bias 证据。\n- R2 从概念层面指出：\"Symbolic **Confirmation Bias**\" 暗示 cognitive bias 类比（主动寻找支持性证据），但实际机制是 structural limitation（约束和答案来自同一信息源而结构性耦合）。\n- 两个批评收敛到同一结论：论文应更清楚地区分 \"structural degeneration\"（Observation 1 的后果）和 \"extraction bias\"（如果存在的话）。目前混淆使 BR 看起来提供了 Observation 1 之外的独立证据，但实际上没有。\n- **建议**：(a) 在首次定义 SCB 时明确说明这是 structural limitation 而非 cognitive bias 类比；(b) 报告 BR_excess 作为判断是否存在 extraction-level 额外偏差的指标；(c) 考虑更精确的术语如 \"symbolic information collapse\" 或 \"self-referential degeneration\"。\n\n**SF-2** [warning, R2-W1, R1 AGREE] **Abstract 超过 200 词限制**\n\n- 经去除 LaTeX 命令后词数统计约 202 词，超过 EMNLP 2026/ARR 的 200-word 硬约束。虽仅超出 2 词，但属明确格式违规。\n\n**SF-3** [warning, R1-W2, R2 AGREE] **\"Pre-registered\" margin ±2pp 无注册凭证**\n\n- Section 4 使用 \"pre-registered margin ±2 pp\" 但未提供 OSF/AsPredicted 等预注册链接。\"Pre-registered\" 在实证研究中有严格操作定义。改为 \"pre-specified\" 或 \"predetermined\" 即可。\n\n**SF-4** [warning, R1-W3, R2 AGREE with nuance] **BH correction m=16 包含非独立条件**\n\n- 16 个条件中包含 Mistral-7B×FOLIO 的 3 个单独 seed (s123, s456, s789) 和 1 个 3-seed aggregate，以及 Qwen2.5-14B×FOLIO 的 4-seed aggregate。Aggregate 是 component seeds 的函数，非独立检验。虽然更大的 m 使 BH 更保守，但方法论应更干净地区分 confirmatory vs exploratory 条件。\n\n**SF-5** [warning, R1-W4, R2 AGREE] **Observation 1 条件 (iii) \"approximately uniform constraint yield\" 缺乏系统验证**\n\n- 条件 (i) |C\\| ≈ 0 由 Z3 rejection rate 3.4% 实证支持，条件 (ii) source-attribution 是系统设计，但条件 (iii) 缺乏直接验证。论文未报告 per-trace constraint yield 的分布统计量（mean, std, CV），应按 answer group 分层报告。\n\n**SF-6** [warning, R2-W3, R1 AGREE] **Turpin et al. 引用年份错误**\n\n- references.bib 中 `turpin2024language` 记录 year={2024}，但 \"Language Models Don't Always Say What They Think\" 发表于 NeurIPS **2023**。\n\n**SF-7** [warning, R2-W5, R1 AGREE minor] **论文密度过高，可读性受损**\n\n- LaTeX source 含 `\\enlargethispage{6\\baselineskip}` (main.tex:72)、`\\vspace{-4mm}` (main.tex:76)、`\\vspace{-1.5mm}` (main.tex:73) 等排版 hacks。Section 7 (Discussion and Conclusion) 仅约 1/3 页。Figure 4 信息密度极高但难以快速 parse。建议将部分内容移入 appendix 以提升可读性。\n\n**SF-8** [warning, R1-M1] **Introduction 使用 \"prove\" 描述 Observation 1**\n\n- §1: \"We prove this degeneration is structural (Observation 1)\"——Observation 1 依赖经验条件 (iii)，\"prove\" 过强，应改为 \"show\" 或 \"demonstrate\"。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键判断上达成完全共识：\n\n1. **Overall 3.0 (Findings)**：R1 初评 3.5，交叉审议后被 R2 的 novelty 和引用论点说服，下调至 3.0。\n2. **Cross-architecture escape 应降级**：n=6（实际 <6 due to shared verifier）不足以支撑 top-level contribution。\"Generator < verifier 才有增益\" 可能是 trivial condition。可能只是 ensemble diversity 效应。\n3. **Underpowered claim 需精确化**：Abstract/标题的 blanket negative claim 超出统计证据范围。\n4. **SCB/BR 概念框架需澄清**：BR > 1 是 structural 而非 bias 证据；SCB 命名暗示 correctable deficiency 但实际是 structural limitation。\n5. **引用错误必须修正**：两条引用元数据严重错误，需系统性交叉验证全部参考文献。\n6. **\"Advances beyond Huang et al.\" 表述过度**：应改为 \"extends and formalizes\"。\n7. **统计方法论是论文最大优势**：McNemar + BH + TOST + Bootstrap + Power analysis 的完整组合在 NLP 论文中极为罕见，使 negative result 高度可信。\n8. **论文适合 Findings 而非 Conference**：贡献定位是 confirmation + formalization（用大规模实验确认并形式化了一个 expected result），而非 discovery。统计严谨性满足 Findings 的 soundness 要求，但 excitement/novelty 不够 Conference。\n\n---\n\n## Reviewer Divergence [REBUT]\n\n无重大分歧。R1 初始评分比 R2 高 0.5 分，但在交叉审议后被说服并下调，最终收敛。\n\n---\n\n## Questions\n\n1. **BR_excess ≈ 0 意味着什么？** Permutation test 显示经验 BR 完全由 trace-count 结构解释（BR_excess ≈ 0, p > 0.7）——如果没有超出 base-rate 的额外 extraction bias，\"symbolic confirmation bias\" 是否应该重新命名？\n2. **Observation 1 条件 (iii) 的验证数据？** 每条 trace 平均产生多少 constraints？标准差？不同 answer group 之间的 yield 差异？\n3. **为什么不测试 non-NLI independent verifier？** Cross-model majority vote ensemble 是否也能产生类似增益？这将区分 \"information independence\" 和 \"ensemble diversity\" 假说。\n4. **TOST margin 的 \"pre-registered\" 指什么？** 是否有 OSF 或类似平台的注册记录？\n5. **如果将约束用于 re-prompting 而非 MAX-SAT scoring，结果是否不同？** 27 种策略是否都在 extraction-aggregation paradigm 内？\n6. **Domain-adapted verifier 的增益 (+12.67pp) 是否主要来自 domain-specific training 而非 structural independence？**\n\n---\n\n## Missing References\n\n1. **Ensemble diversity 经典文献** [R1 + R2 共识]：Dietterich (2000) \"Ensemble Methods in Machine Learning\", Krogh & Vedelsby (1995) \"Neural Network Ensembles, Cross Validation, and Active Learning\"——Section 2 ensemble theory 段落和 Section 6 cross-architecture discussion 应引用并回应 ensemble diversity 假说。\n2. **OpenAI o1/o3 reasoning models** [R2]：Table 2 包含 o3 cross-model extraction 结果，但 Section 2 \"test-time compute\" 段落未显式讨论 o1/o3 内部推理链机制及 SICA paradigm 的适用性。\n3. **Cobbe et al. (2021) GSM8K verifier** [R1]：独立 verifier 提升推理性能的早期实例，与 Section 6 的 cross-architecture escape 直接相关。\n\n---\n\n## External Review\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（1 warning, 9 info）。\n\n**Warning:**\n- Limitations section heading 出现在 page 8 底部极端位置（orphan heading），后续仅 2 行正文在同一页，大部分 Limitations 内容在 page 9 顶部。建议用 `\\needspace` 调整。\n\n**Info（主要发现）:**\n- Figure 1 出现在 page 2 顶部，pipeline 架构图提供清晰视觉锚点，Title-Abstract-Figure 1 叙事一致性好。\n- Figure 2 散点图图例文字偏小（约 6-7pt），建议适当放大。\n- Table 1 字号偏小（~7pt），处于舒适阅读下限。booktabs 风格正确，表头分区清晰。\n- Figure 3 Causal DAG 尺寸明显偏小（仅占左栏 1/4 面积），作为核心概念图建议放大。\n- Figure 4 条形图 x 轴标签和图例文字偏小，分类名称需仔细辨认。\n- Appendix 单页含 4 个表格，密度极高但作为 appendix 可接受。\n\n---\n\n## Overall Assessment\n\n**评分：3.0 — Findings（可被 Findings 接收）**\n\n**Reviewer 评分汇总：**\n\n| 维度 | R1 (交叉后) | R2 | 综合 |\n|------|------------|-----|------|\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 2.5/5 | 2.5/5 | 2.5/5 |\n| Reproducibility | 3/5 | 4/5 | 3.5/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n| **Overall** | **3.0** | **3.0** | **3.0** |\n\n**置信度：4/5**（两位 Reviewer 在各自专长领域（统计方法论 / 文献与 novelty）均有充分把握，且交叉审议后完全收敛）\n\n**理由：**\n\n这是一篇实验执行质量高、方法论严谨的 negative result 论文。60 个条件、9 个模型、27 种修补策略的系统排除确实超出了多数同类工作的证据标准。Oracle control 精巧，诊断框架有实用价值，统计方法论在 NLP 领域属顶级水准。\n\n但在 excitement 维度存在根本性限制：核心洞见（自提取信息因与答案来自同一信息源而缺乏独立性）在 Huang et al. (ICLR 2024) 和 Condorcet Jury Theorem 框架下是可预见的。论文的贡献更准确的定位是 confirmation（用大规模实验确认 expected result）+ formalization（Markov chain model, diagnostics），而非 discovery。Cross-architecture escape 作为唯一正面贡献过于初步（n=6, shared verifier, 可能只是 ensemble diversity）。两条引用的元数据严重错误进一步降低了整体学术质量评估。\n\n如果 MF-1（引用修正）、MF-2（novelty claim tempered）、MF-4（negative claim 精确化）得到修正，本文作为 Findings 论文是合适的——为社区提供了有价值的 negative evidence 和实用的诊断工具。但以目前的 novelty framing，不足以支撑 Conference main 接收。\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract (p.1):**\n- 约 202 词，超过 200 词限制 [SF-2]\n- \"advancing beyond Huang et al. (2024)'s findings\" → \"extending and formalizing\" [MF-2]\n- \"We find no evidence of improvement\" → \"no evidence of improvement exceeding ~2 percentage points\" [MF-4]\n- \"self-extracted\" 出现 4 次，可适当减少重复\n\n**Introduction (§1, p.1-2):**\n- \"We prove this degeneration is structural\" → \"We show\" [SF-8]\n- Contribution 3 (\"Cross-architecture escape\") 应标注 \"preliminary\" [MF-3]\n- Figure 1 pipeline 图清晰有效\n\n**Related Work (§2, p.2-3):**\n- 结构良好（5 段覆盖 5 个维度），引用密度高\n- byerly2026selfconsistency 和 dupo2025 需修正 [MF-1]\n- turpin2024language 年份 2024→2023 [SF-6]\n- 缺少 ensemble diversity 经典文献和 OpenAI o1/o3 引用\n\n**Method (§3, p.3-4):**\n- SICA pipeline 描述清晰完整，数学公式和算法规范\n- Observation 1 条件 (iii) 需系统验证 [SF-5]\n- BR 定义需与 \"structural degeneration\" 而非 \"bias\" 关联 [SF-1]\n- α=0.5 sensitivity 在 Appendix 有验证，正文可简要提及\n\n**Results (§4, p.4-5):**\n- Table 1 信息密集但结构清晰，regime 分类有效\n- \"pre-registered margin\" → \"pre-specified margin\" [SF-3]\n- BH m=16 应标注 confirmatory vs exploratory [SF-4]\n- Figure 2 regime scatter 有效传达了核心模式\n\n**Analysis (§5, p.5-7):**\n- §5.1 SCB 分析是论文最有洞察力的部分\n- 但 BR_excess ≈ 0 + permutation test 的含义未充分 reconcile with \"bias\" 叙事 [SF-1]\n- §5.2 Remediation 27 种变体的穷举测试令人信服\n- §5.3 Diagnostic framework 有实践价值，prospective validation 是加分项\n- Figure 3 Causal DAG 尺寸偏小 [视觉审查]\n- Figure 4 信息密度极高，考虑简化正文版本\n\n**Escaping the Bottleneck (§6, p.7-8):**\n- Cross-architecture escape 结果有趣但证据不足 [MF-3]\n- 需要 ensemble diversity ablation 区分假说\n- Domain-adapted verifier 与 training-free 叙事的张力需更明确讨论\n- Table 3 仅 4 个 generators 共享 1 个 verifier，统计说服力有限\n\n**Discussion (§7, p.8):**\n- 过于简短（~1/3 页），应更充分展开\n- \"advancing beyond Huang et al.\" → \"extending and formalizing\" [MF-2]\n- 缺少对 practical implications 和 future directions 的更具体讨论\n\n**Limitations (p.8-9):**\n- 内容合理（模型范围、语言、训练方法、statistical power），简短覆盖 3 个主要限制\n- Orphan heading 问题 [视觉审查 warning]\n\n**Appendix:**\n- 内容丰富（prompt templates, pseudocode, statistical analyses, case studies, ablations）\n- 对论文完整性有重要支撑\n"
  }
}
```

</details>

---


### Tool result

_source line 1995 · 2026-05-23T14:07:42.755073+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4220
}
```

</details>

---


### Assistant

_source line 1996 · 2026-05-23T14:07:50.874954+00:00_

审稿报告已投递。

**Round 19 审稿完成：**

- **Overall: 3.0 (Findings)**，两位 Reviewer 完全收敛
- **4 个 Must-Fix**：引用元数据错误（2 条 hallucinated）、"advances beyond Huang" 过度声明、cross-architecture escape 证据不足、underpowered negative claim
- **8 个 Should-Fix**：BR/SCB 概念循环、abstract 超 200 词、"pre-registered" 无凭证、BH m=16 非独立、Obs 1 条件 iii 未验证、Turpin 年份错误、论文密度过高、Introduction "prove" 过强
- **视觉审查**：1 warning（Limitations orphan heading）、9 info
- **Issue Tracker** 已同步更新

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 145

## Round 145

2 recorded events


### User

_source line 1997 · 2026-05-23T14:07:52.384800+00:00_

[Reviewer 1 审稿结果]:
已提交对 R2 的逐条回应。

核心结论：
- **R2-N1 (引用错误)**: [AGREE]，bib 中确认两条引用元数据存疑，Turpin 年份也有误
- **R2-N2 (overclaiming Huang et al.)**: [AGREE with nuance]，"advances beyond" 应改为 "extends and formalizes"
- **R2-N3 (cross-arch escape)**: [AGREE]，与我的 N1 指向同一问题，R2 额外提出的 "trivial condition" 论点有力
- **R2-W4 (naming) vs 我的 W1 (BR circularity)**: 确认指向同一根本问题——"bias" 暗示 extraction 引入偏差，但数据显示只是 scoring mechanism 的结构性后果
- **Overall**: 从 3.5 下调至 3.0 (Findings)，接受 R2 的 novelty 和引用质量论点

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1998 · 2026-05-23T14:08:04.901169+00:00_

审稿报告已成功投递给 Research Director。

**Round 19 审稿完成，总结：**

- **Overall: 3.0 (Findings)**，两位 Reviewer 完全收敛
- **4 个 Must-Fix**：引用元数据错误（2 条 hallucinated）、"advances beyond Huang" 过度声明、cross-architecture escape 证据不足以支撑 contribution、underpowered claim 表述超出统计证据
- **8 个 Should-Fix**：BR/SCB 概念框架混淆、abstract 超 200 词、"pre-registered" 无凭证、BH m=16 含非独立条件、Observation 1 条件 (iii) 未验证、Turpin 年份错误、论文密度过高、Introduction "prove" 过强
- **定位**：实验执行质量高、统计方法论顶级的 negative result 论文，适合 Findings 接收；novelty 不足以支撑 Conference main

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 146

## Round 146

74 recorded events


### User

_source line 1999 · 2026-05-23T19:02:19.040909+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: symb_invariant_consensus
- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2000 · 2026-05-23T19:02:25.593783+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2001 · 2026-05-23T19:02:25.645011+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2002 · 2026-05-23T19:02:36.893227+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2003 · 2026-05-23T19:02:37.245115+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2004 · 2026-05-23T19:02:45.128231+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 2005 · 2026-05-23T19:02:45.128659+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2006 · 2026-05-23T19:02:45.480846+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 2007 · 2026-05-23T19:02:45.982609+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (173 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-multi-seed-llama-pw-seed789-v2 | LLaMA-3.1-8B PW seed789 多种子复制（westd-30973 cuda:1 全新运行）。替代 16639 cuda:0 上的慢速运行（12/600）。验证 SCB 在 ProofWriter 上跨 seed 稳定性。 | — | — | — |\n| exp-multi-seed-llama-pw-seed456-v2 | LLaMA-3.1-8B PW seed456 多种子复制（westd-30973 cuda:2 全新运行）。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。 | — | — | — |\n| exp-multi-seed-qwen25-pw-seed789-v3 | Qwen2.5-14B PW seed789 多种子复制（westd-30973 cuda:0 全新运行）。替代 v2 在 16639 cuda:2 上的慢速运行（53/600）。验证 SCB 在 ProofWriter 上跨 seed 稳定性。 | — | — | — |\n\n## 待处理\n- exp-multi-seed-llama-pw-seed456: LLaMA-3.1-8B PW seed456 多种子复制。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。（排队等待 GPU）\n- exp-deberta-ft-combo: Fine-tuned DeBERTa-large on ProofWriter OWA depth-5 achieves near-perfect NLI accuracy (99.67%) and provides massive combo gains over SC baseline when used as external verifier, demonstrating that domain-specific NLI fine-tuning breaks the SCB ceiling by providing truly independent verification signal.（准备中）\n- exp-multi-seed-mistral-folio: Multi-seed replication (seeds 123,456,789) of Mistral-7B × FOLIO-20
…[truncated 1733 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 2008 · 2026-05-23T19:02:53.513502+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2009 · 2026-05-23T19:03:02.074890+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % removed: not available in this TeX distribution
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{tcolorbox}
14	\tcbuselibrary{skins}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{subcaption}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,calc,fit}
22	\usepackage{listings}
23	\usepackage{algorithm}
24	\usepackage{algpseudocode}
25	\usepackage{hyperref}
26	\usepackage{cleveref}
27	
28	\lstset{
29	  basicstyle=\small\ttfamily,
30	  breaklines=true,
31	  frame=single,
32	  xleftmargin=1em,
33	  xrightmargin=1em,
34	  aboveskip=0.5em,
35	  belowskip=0.5em,
36	}
37	
38	\graphicspath{{../figures/paper/}{figures/}}
39	
40	\title{Beyond Self-Consistency: Self-Extracted Constraints\\Provide No Detectable Improvement in LLM Reasoning}
41	
42	\author{Anonymous}
43	
44	\begin{document}
45	\maketitle
46	
47	% Tighten spacing for 8-page budget
48	\setlength{\textfloatsep}{5pt plus 2pt minus 4pt}
49	\setlength{\dbltextfloatsep}{5pt plus 2pt minus 4pt}
50	\setlength{\floatsep}{3pt plus 2pt minus 2pt}
51	\setlength{\dblfloatsep}{3pt plus 2pt minus 2pt}
52	\setlength{\abovecaptionskip}{2pt}
53	\setlength{\belowcaptionskip}{0pt}
54	\setlength{\abovedisplayskip}{4pt plus 1pt minus 2pt}
55	\setlength{\belowdisplayskip}{4pt plus 1pt minus 2pt}
56	\setlength{\intextsep}{5pt plus 1pt minus 2pt}
57	
58	\input{abstract}
59	
60	\input{introduction}
61	
62	\input{related_work}
63	
64	\input{method}
65	
66	\input{experiments}
67	
68	\input{analysis}
69	
70	\input{solutions}
71	
72	\input{discussion}
73	
74	\section*{Limitations}
75	\input{limitations_content}
76	
77	\bibliography{references}
78	
79	\appendix
80	\input{appendix}
81	
82	\end{
…[truncated 13 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 8561
}
```

</details>

---


### Tool call

_source line 2010 · 2026-05-23T19:03:02.125509+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines page limit template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines page limit template"
  }
}
```

</details>

---


### Tool call

_source line 2011 · 2026-05-23T19:03:02.125979+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool call

_source line 2012 · 2026-05-23T19:03:04.096736+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2013 · 2026-05-23T19:03:08.462195+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines page limit template"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, I found information about EMNLP 2026 ARR submissions. Here's what the guidelines specify:

## Page Limits

Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments. This indicates that the submission page limits are 8 pages for long papers and 4 pages for short papers.

## Submission Guidelines

EMNLP 2026 i
…[truncated 930 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6336
}
```

</details>

---


### Tool result

_source line 2014 · 2026-05-23T19:03:08.512990+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'symb_invariant_consensus'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6387
}
```

</details>

---


### Tool result

_source line 2015 · 2026-05-23T19:03:08.614077+00:00_

-rw-r--r-- 1 ubuntu ubuntu 659011 May 23 19:00 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 4517
}
```

</details>

---


### Tool call

_source line 2016 · 2026-05-23T19:03:17.096326+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines anonymity appendix supplementary material policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines anonymity appendix supplementary material policy"
  }
}
```

</details>

---


### Tool call

_source line 2017 · 2026-05-23T19:03:17.598469+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool call

_source line 2018 · 2026-05-23T19:03:18.552271+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_EXISTS\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_EXISTS\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool call

_source line 2019 · 2026-05-23T19:03:19.456379+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/*.tex 2>/dev/null",
  "description": "Count lines in all tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/*.tex 2>/dev/null",
    "description": "Count lines in all tex files"
  }
}
```

</details>

---


### Tool result

_source line 2020 · 2026-05-23T19:03:24.374378+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines anonymity appendix supplementary material policy"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Industry Track - ACL 2026","url":"https://2026.aclweb.org/calls/industry_track/"},{"title":"ACL Student Research Workshop (SRW) 2026","url":"https://acl2026-srw.github.io/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here are the key ACL Rolling Review 2026 submission guidelines regarding anonymity, appendix, and supplementary material policy:

## Anonymity Requirements

Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities, e.g., "We previously showed (Smith, 1991)…" must be avoided.

## Supplementary Material and Appendix Policy

Supplementary materi
…[truncated 843 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 7278
}
```

</details>

---


### Tool result

_source line 2021 · 2026-05-23T19:03:24.427831+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/decisions.yaml\", \"content\": \"_next_id: 156\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 08:47 UTC\\n  summary: MVP 验证方案：50 题 MATH-500 分层子集，SICA vs SC@K=12\\n  rationale: SICA 核心价值取决于两个前提：(1) 能从推理 trace 可靠提取符号约束；(2) 跨路径矛盾率足够高（>5%）使形式化验证有意义。Reviewer\\n    给 impact 3/5，核心担忧是\\\"若矛盾率<5%则动机不成立\\\"。MVP 直接验证这两个前提，50 题按难度分层可同时观察 Extraction-Verification\\n    Paradox（难题提取差但矛盾多）。Pass 则进入全量实验冲 EMNLP/AAAI，Fail 则及时止损。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 08:52 UTC\\n  summary: 拒绝 CRD pivot，要求回归 SICA 原始方案\\n  rationale: Reviewer critical 审查发现 Agent 实施的是\\\"跨表征分歧诊断\\\"(CRD)，与 IDEA_BRIEF 定义的 SICA\\n    完全不同：CRD 用双表征（FOL+SymPy）做单解分歧检测，无多路径采样、无 MAX-SAT 共识——这正是 SICA 区别于 VERGE/D&P 的核心创新点。CRD\\n    的 novelty 定位与 VERGE 高度重叠（单输出验证+修复），无法支撑 EMNLP 投稿。同时 MVP 标准被静默替换，ROADMAP 的三条 pass\\n    criteria 从未测试。98GB GPU 完全能跑 QwQ-32B，无理由换 Qwen3-32B-AWQ。必须回归 SICA：K=12 多路径采样 →\\n    符号约束提取 → Z3 加权 partial MAX-SAT → 不变量共识打分。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 08:54 UTC\\n  summary: MVP 标准 v2：三档判定 + 矛盾绝对数 ≥5 + accuracy ≥SC+2pp + ProofWriter sanity check\\n  rationale: Reviewer warning 指出：(1) 5% 矛盾率阈值在 50 题上仅 2.5 题，置信区间极宽——改为绝对数 ≥5 题；(2)\\n    ≥SC+0.1pp 也过关无意义——改为 ≥2pp 或 p<0.1；(3) 灰色区间无处理——新增 Inconclusive 档，触发扩展到 100 题重测；(4)\\n    单域 MATH-500 不够——加 10 题 ProofWriter 做逻辑域 sanity check；(5) 模型不能模糊——固定 QwQ-32B，不可替换。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP T=0.7 继续跑完（需要完整数据），diagnostic 自然结束后 GPU 带宽恢复；AIME 30 题排在 MVP 之后\\n  rationale: Temperature 诊断 4/5 题显示 T=0.7/0.9/1.0 均几乎不产生答案分歧——C2/C3 高风险 FAIL。但仍决定让\\n    MVP 跑完：(1) 50 题完整数据无论正负都有价值（负面结果=SICA 在强模型上无信号，本身是发现）；(2) GPU 已分配且无其他实验排队；(3)\\n    smoke test L5 有 3 条矛盾，50 题中 L4-5 有 20 题可能产生更多信号。MVP 完成后立即跑 AIME 30 题（QwQ-32B ~79.5%，分歧应更明显），作为\\\"高难度\\n    sweet
…[truncated 11002 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6829
}
```

</details>

---


### Tool result

_source line 2022 · 2026-05-23T19:03:24.478925+00:00_

     1 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex
   132 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex
  1507 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex
     4 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex
   160 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex
    12 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex
    52 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex
    61 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex
     1 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex
    82 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex
    60 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex
    21 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex
    38 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex
  2131 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 5022
}
```

</details>

---


### Tool result

_source line 2023 · 2026-05-23T19:03:24.479281+00:00_

-rw-r--r-- 1 ubuntu ubuntu 26872 May 23 14:21 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 5927
}
```

</details>

---


### Tool call

_source line 2024 · 2026-05-23T19:03:39.313669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2025 · 2026-05-23T19:03:39.665470+00:00_

1	Can symbolic verification via a provably sound solver improve Large Language Model (LLM) reasoning when constraints are self-extracted from the model's own traces? We find no detectable improvement exceeding ${\sim}$2\,pp under self-extraction. We introduce Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from chain-of-thought traces via weighted MAX-SAT. Despite Z3 validating 99\% of self-extracted constraints, SICA produces answers identical to majority voting on over 90\% of problems across six models (7B--32B) and three domains. No condition shows a significant positive effect after FDR control; four of six powered conditions confirm equivalence within $\pm$2\,pp (TOST); the remainder are underpowered for smaller effects. The failure is structural: self-extracted constraints track the majority answer---a property we term \emph{symbolic confirmation bias} (bias ratios $1.66$--$4.97\times$ across nine models, 7B to frontier). Under source-attribution scoring and degeneration, SICA reduces to majority vote (Observation~1); the $M{\to}T{\to}A{\to}C$ Markov chain bounds self-extracted information (Remark~1), extending and formalizing \citet{huang2024selfcorrect}'s findings for formal self-verification. Twenty-seven training-free variants fail due to a persistent independence-accuracy trade-off. Cross-architecture verification escapes the bias ($+6.67$\,pp on the weakest generator, $p < 0.001$). Three zero-cost diagnostics characterize failure modes across all tested conditions.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2026 · 2026-05-23T19:03:39.666073+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2027 · 2026-05-23T19:03:40.619188+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	\looseness=-1
4	Self-Consistency (SC) \citep{wang2023sc} selects the majority answer across $K$ chain-of-thought traces, a strategy grounded in the Condorcet Jury Theorem: independent voters converge to truth \citep{condorcet1785, ladha1992correlated}. In practice, SC's gains plateau for strong models \citep{loo2025reevaluating}, pointing to correlated traces that reduce the effective ensemble size. A natural remedy is to move beyond simple vote-counting: extract logical constraints from the traces and let a provably sound solver adjudicate. If the solver can filter contradictions and enforce logical consistency, it should recover information that raw majority voting discards.
5	
6	\looseness=-1
7	We test this intuition through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces (prompted as first-order logic; 99\% are propositional at the Z3 level) and selects answers via weighted partial MAX-SAT (\S\ref{sec:pipeline}; Figure~\ref{fig:pipeline}). Despite Z3 validating nearly all self-extracted constraints, SICA produces answers identical to majority voting on the vast majority of problems. Across six models (7B--32B), three reasoning domains, and multi-seed replication, no condition shows a significant positive effect after FDR control (Table~\ref{tab:main_results}). Four of six powered conditions confirm equivalence within $\pm$2\,pp (TOST); the remainder are underpowered for smaller effects.
8	
9	\looseness=-1
10	The failure is not in the solver but in the constraints it operates on. Self-extracted constraints systematically support the model's majority answer---a structural property of self-extraction pipelines we term \emph{symbolic confirmation bias} (\S\ref{sec:confirmation-bias}). Because each trace determines both an answer and its constraints, the formal channel reduces to a weighted echo of the majority vote. We show this degeneration is structural 
…[truncated 4167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 2028 · 2026-05-23T19:03:40.670479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2029 · 2026-05-23T19:03:41.374037+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\looseness=-1
5	\paragraph{Self-consistency and ensemble theory.}
6	Self-consistency (SC) selects the most frequent answer across chain-of-thought traces \citep{wang2023sc}. Extensions address free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting \citep{li2023diverse}, and reasoning-aware filtering \citep{wan2024rasc, toh2024notallvotes, kim2026reasc}. SC gains plateau early \citep{loo2025reevaluating, byerly2025selfconsistency}. The Condorcet Jury Theorem \citep{condorcet1785} guarantees majority-vote convergence under independence; ensemble theory \citep{dietterich2000ensemble, krogh1994neural} establishes that ensemble gain requires error diversity. \citet{ladha1992correlated} show correlated voters reduce effective ensemble size; our $K_\text{eff}$ adapts Fleiss' $\kappa$ from diversity metrics \citep{kuncheva2003measures, brown2005diversity} to quantify this compression (\S\ref{sec:pipeline}). \citet{kim2025correlated} demonstrate correlated errors in LLM outputs; \citet{kuai2026independent} propose cross-model independence auditing, complementary to our within-model process-$\kappa$.
7	
8	\looseness=-1
9	\paragraph{Neuro-symbolic reasoning.}
10	We distinguish three paradigms: \emph{specification-generation} \citep{pan2023logiclm, olausson2023linc, ye2024satlm} and \emph{program-generation} \citep{gao2023pal, chen2023program, lyu2023faithful} formalize \emph{before} answer generation; \emph{trace-extraction} (this work) operates post-hoc, inheriting confirmation bias (\S\ref{sec:confirmation-bias}). Recent extensions include symbolic planning and verified reasoning \citep{ryu2025clover, xu2026dylos, li2025aristotle, wang2025fover, singh2026verge, luo2025logicagent, miya2025eidoku}; \citet{amonkar2025realitycheck} show formalization quality degrades with problem complexity; \citet{chan2026position} argue logical soundness alone is unreliable. Prior stu
…[truncated 3325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 2030 · 2026-05-23T19:03:41.574962+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2031 · 2026-05-23T19:03:41.575420+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{SICA Pipeline}
5	\label{sec:pipeline}
6	\label{sec:condorcet}
7	\label{sec:effective-k}
8	
9	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. Under correlated traces (Fleiss' $\kappa$ \citep{fleiss1971kappa}), effective sample size reduces to
10	\begin{equation}
11	\label{eq:effk}
12	K_{\text{eff}} = K \,/\, [1 + (K{-}1) \cdot \kappa]
13	\end{equation}
14	(following \citet{ladha1992correlated}). Intuitively, $K_\text{eff}$ measures how many effectively independent votes $K$ correlated traces contribute; e.g., $K{=}12$ traces with $\kappa{=}0.69$ yield $K_\text{eff} \approx 1.3$, meaning twelve correlated traces carry no more independent information than 1.3 uncorrelated ones. This motivates constraint-based aggregation.
15	
16	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
17	
18	\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K\}$ at temperature $T = 0.7$. Each trace $t_i$ yields answer $a_i$.
19	
20	\looseness=-1
21	\paragraph{Constraint extraction.}\label{sec:constraint-extraction} The same LLM extracts logical constraints from each trace at $T_{\text{ext}} = 0.3$. The extraction prompt requests JSON output with constraint type, expression, and Z3-compatible formula (Appendix~\ref{app:prompts}); in practice, 99.0\% of extracted constraints are propositional at the Z3 level, with only 1.0\% using true quantifiers. The \emph{extraction rate} is the fraction of traces yielding at least one parseable constraint.
22	
23	\paragraph{Deduplication and MAX-SAT.} Constraints are deduplicated by syntactic equivalence (global average deduplication ratio: 46.0\%); each unique constraint $c_m$ receives weight $w_m$ equal to the number of source traces. The objective finds
…[truncated 3719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2032 · 2026-05-23T19:03:41.976667+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2033 · 2026-05-23T19:03:41.977221+00:00_

1	\section{Results}
2	\label{sec:results}
3	\label{sec:main-results}
4	
5	\looseness=-1 Table~\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. No condition shows a significant SICA effect after FDR control (BH, $m{=}6$ confirmatory conditions; multi-seed aggregates and extensions are exploratory). Two confirmatory conditions show nominally significant degradation: Mistral-7B on ProofWriter ($-2.83$\,pp, raw $p = 0.014$) and Qwen2.5-14B on ProofWriter ($-2.50$\,pp, raw $p = 0.011$); both reach adjusted $p = 0.066$. An aggregate sign test yields 8 positive and 7 negative $\Delta$ values ($p = 1.00$, two-sided). When SICA and SC disagree, SC selects the correct answer $2.6\times$ more often (139 vs.\ 53 across conditions), indicating that constraint-based reweighting introduces noise rather than corrective signal.
6	
7	\begin{table*}[t]
8	\centering
9	\small
10	\caption{SICA vs.\ SC across all non-degenerate self-extraction conditions (sorted by SC). No condition shows a significant gain after BH correction ($m{=}6$ confirmatory; remaining exploratory). $\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \textbf{bold}: $p < 0.05$; {*}\,uncorrected $p < 0.05$ (BH adj.\ $p = 0.066$); $^{3s}$\,3-seed aggregate; $^{4s}$\,4-seed confirmatory aggregate (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\%$ for $|\Delta| = 2$\,pp (Appendix~\ref{app:power}). Degenerate conditions ($C_0 < 5\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$; exploratory) yield $\Delta = 0$; oracle upper bounds in Appendix~\ref{app:oracle}.}
11	\label{tab:main_results}
12	\begin{tabular}{@{}llrrrrl@{}}
13	\toprule
14	Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & $p$ \\
15	\midrule
16	\multicolumn{7}{l}{\textit{Type C: error amplification (SC $\leq$ 40\%)}} \\
17	Mistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\mathbf{-2.83}$ & 0.014{*} \\
18	\midrule

…[truncated 3186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2034 · 2026-05-23T19:03:42.278305+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 2035 · 2026-05-23T19:03:42.278803+00:00_

1	\section{The Symbolic Mirage}
2	\label{sec:analysis}
3	
4	\subsection{Symbolic Confirmation Bias}
5	\label{sec:confirmation-bias}
6	
7	\looseness=-1 Self-extracted constraints systematically align with the model's majority answer---a structural limitation of self-extraction pipelines, not a cognitive bias analogy. On Mistral-7B FOLIO, when SICA errs, 83.3\% of constraints support the incorrect answer---bias ratio $4.97\times$ (Table~\ref{tab:cross-model-bias})---and 94\% of errors overlap with SC. Z3 rejects only 3.4\% of constraints, and MAX-SAT produces answers identical to count-only aggregation on $\geq$99\% of problems across all weight settings $\alpha$ (Table~\ref{tab:alpha-ablation}), confirming that the formal verification layer is vacuous (Eq.~\ref{eq:degenerate}): 99\% of constraints pass Z3 validation yet add no information beyond majority voting.
8	
9	\looseness=-1 Crucially, BR $> 1$ is not an independent finding but a corollary of the degeneration identified in Observation~1: under source-attribution scoring, constraint weight is proportional to trace count, so the majority answer necessarily receives more support. A permutation null model---randomizing constraint--answer associations while preserving per-trace counts (1{,}000 permutations)---confirms this: $\text{BR}_\text{null} \approx \text{BR}_\text{obs}$ ($\text{BR}_\text{excess} \approx 0$; $p > 0.7$) across all tested conditions. BR thus quantifies the degree of extraction degeneration---how completely constraints collapse to majority-vote equivalents---not an independent bias signal. On problems where SC is correct, constraints still track the majority ($\text{BR}_\text{correct}$ $1.29$--$3.64\times$), confirming that self-extracted constraints reflect distributional frequency rather than logical validity.
10	
11	\looseness=-1 The pattern generalizes across nine models from 7B to frontier (BR $1.66$--$4.97\times$; Table~\ref{tab:frontier-scb}) and all eight cells of a $2{\times}2$ generator$
…[truncated 11546 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2036 · 2026-05-23T19:03:42.630360+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
  }
}
```

</details>

---


### Tool result

_source line 2037 · 2026-05-23T19:03:43.032326+00:00_

1	\section{Escaping the Bottleneck}
2	\label{sec:solutions}
3	\label{sec:cross-arch}
4	
5	\paragraph{Motivation.}
6	\looseness=-1 No training-free self-extraction method achieves independence from the model's distributional prior (\S\ref{sec:remediation}). Remark~1 implies that any escape must break the self-extraction dependency: the information ceiling $I(C;Y) \leq I(T;Y)$ binds whenever constraints are deterministic functions of the generating model's traces. We test whether a structurally independent verifier, sharing neither architecture nor training data with the generator, provides corrective signal that escapes this bound.
7	
8	\paragraph{Method.}
9	\looseness=-1 We use DeBERTa-large \citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli}, to classify (premise, conclusion) pairs as entailment, contradiction, or neutral. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$).
10	
11	\paragraph{Zero-shot results.}
12	\looseness=-1 DeBERTa NLI alone achieves 49.51\% on FOLIO and 55.00\% on ProofWriter. Combo $w{=}3$ yields $+6.67$\,pp on ProofWriter for Mistral-7B ($p < 0.001$, significant after BH correction) and $+2.94$\,pp on FOLIO (n.s.); all generators with SC $\geq 72\%$ show no significant improvement ($\Delta \leq +0.83$\,pp). Same-model SICA \emph{degrades} ProofWriter ($-2.83$\,pp; Table~\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution.
13	
14	\paragraph{Capability gap.}
15	\looseness=-1 Four generators on ProofWriter ($n{=}600$), paired with DeBERTa-large-mnli (55.00\% standalone; Table~\ref{tab:cross_generator_nli}): only Mistral-7B (SC below the verifier) gains significantly ($+6.67$\,pp, $p < 0.001$). This \emph{capability-gap pattern}---gain decreasing monotonically with generator accuracy---holds across three NLI architectures ($\rho = 1.0$, $p 
…[truncated 2338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2038 · 2026-05-23T19:03:43.032792+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2039 · 2026-05-23T19:03:43.535014+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	\label{sec:conclusion}
4	
5	\looseness=-1
6	Our central finding is that the value of formal verification depends on the \emph{independence} of its inputs, not the soundness of its logic. \emph{SICA-specific}: under source-attribution scoring, SICA reduces to majority vote (Observation~1), and 27 training-free variants fail to escape. \emph{General}: the DPI bound (Remark~1) applies to any deterministic self-extraction, and symbolic confirmation bias---a structural property of self-extraction pipelines, not a cognitive bias analogy---holds across nine models (7B to frontier), suggesting the bottleneck is intrinsic to self-referential constraint generation. Three diagnostics ($K_\text{eff}$, BR, $C_0$) correctly characterize failure modes across all tested conditions, with boundaries generalizing to held-out families (\S\ref{sec:diagnostic-framework}).
7	
8	\looseness=-1
9	These results connect to ensemble diversity theory \citep{dietterich2000ensemble, krogh1994neural}: ensemble gain requires error independence, which $K_\text{eff}$ operationalizes for LLM trace aggregation. With $K_\text{eff} \leq 3.62$ for $K{=}12$, same-model traces scale redundancy, not information---extending and formalizing \citet{huang2024selfcorrect}'s empirical findings for formal self-verification. This has direct consequences for test-time compute scaling \citep{snell2025scaling}: increasing $K$ within a single model yields diminishing returns when traces share systematic biases, regardless of the aggregation mechanism applied.
10	
11	\looseness=-1
12	Escaping the bottleneck requires structural independence (\S\ref{sec:cross-arch}); cross-architecture NLI provides a proof of concept, but whether trained extractors or hybrid approaches can shift the boundary remains open. Our diagnostic framework offers a concrete tool: a $K{=}12$ pilot run with three zero-cost metrics predicts whether any self-extraction method will help befo
…[truncated 23 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2040 · 2026-05-23T19:03:43.585605+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
  }
}
```

</details>

---


### Tool result

_source line 2041 · 2026-05-23T19:03:43.636160+00:00_

1	\looseness=-1 Models range from 7B to 32B (frontier via cross-model extraction); all benchmarks are English logical reasoning. We do not evaluate trained extractors. Statistical power is limited for effects below ${\sim}$2\,pp; the capability-gap analysis rests on $n{=}6$ conditions (Appendix~\ref{app:limitations-extended}).
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2042 · 2026-05-23T19:03:52.467789+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2043 · 2026-05-23T19:03:52.919955+00:00_

1	\section{Prompt Templates}
2	\label{app:prompts}
3	
4	SICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).
5	
6	\paragraph{System Prompt.}
7	
8	\begin{lstlisting}
9	You are a constraint extraction tool. Output ONLY
10	valid JSON. Do NOT solve problems, reason about
11	correctness, or think step-by-step. Extract
12	constraints from the given trace exactly as stated.
13	\end{lstlisting}
14	
15	\paragraph{Mathematical Constraint Extraction (EXTRACTION\_PROMPT).}
16	
17	Used for GSM8K and AIME datasets. The placeholder \texttt{\{trace\}} is replaced with the reasoning trace at runtime.
18	
19	\begin{lstlisting}
20	Extract mathematical constraints from this reasoning
21	trace as a JSON object.
22	
23	Rules:
24	- type: "equation", "inequality", or "predicate"
25	- expression: human-readable, e.g. "x + y == 14"
26	- z3_formula: a single comparison expression in
27	  Python Z3 syntax
28	- source_step: step number where the constraint
29	  appears
30	- Use variable names from the trace
31	
32	z3_formula MUST follow these rules:
33	- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,
34	  /, **, %
35	- Use individual named variables: a1, a2, a3...
36	  NOT arrays a[1] or sets A
37	- Expand all sums explicitly:
38	  "a1 + a2 + a3 == 55" NOT "sum([a1,a2,a3])"
39	- NO Python builtins: sum(), len(), max(), min(),
40	  list(), set(), range(), int()
41	- Each z3_formula must be exactly ONE comparison
42	  (==, !=, <, >, <=, >=)
43	- For multiple values, write separate constraints
44	  for each
45	
46	Output ONLY the JSON below, nothing else:
47	{"constraints": [{"type": "equation",
48	  "expression": "x + y == 14",
49	 
…[truncated 6479 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2044 · 2026-05-23T19:03:53.422156+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf",
  "pages": "1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf",
    "pages": "1-5"
  }
}
```

</details>

---


### Tool result

_source line 2045 · 2026-05-23T19:03:54.377753+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf (643.6KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 2046 · 2026-05-23T19:03:54.388032+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml | head -100",
  "description": "Read first 100 lines of review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml | head -100",
    "description": "Read first 100 lines of review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2047 · 2026-05-23T19:03:54.489035+00:00_

# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
- id: "R1-C1"
  summary: "Method Stage 3 sat() implementation undescribed"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
  resolution_round: 3

- id: "R1-C2"
  summary: "Most experiments underpowered (n≤60), no power analysis"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
  resolution_round: 3

- id: "R1-C3"
  summary: "Oracle/upper-bound experiment missing"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
  resolution_round: 3

- id: "R1-C4"
  summary: "Huang et al. (ICLR 2024) not cited"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
  resolution_round: 2

- id: "R1-C5"
  summary: "Critical related work missing"
  category: writing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "~48 citations, 5 Related Work paragraphs."
  resolution_round: 3

- id: "R1-C9"
  summary: "Capability trap novelty unclear"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Reframed as regime-dependent analysis with CJT framework."
  resolution_round: 3

- id: "R3-N1"
  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 3
  last_seen_round: 4
  resolution: "Paper Agent added clarifying sentence in method.tex."
  resolution_round: 4

- id: "R3-N2"
  summary: "α va
…[truncated 655 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2048 · 2026-05-23T19:04:01.340610+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf",
  "pages": "6-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf",
    "pages": "6-10"
  }
}
```

</details>

---


### Tool result

_source line 2049 · 2026-05-23T19:04:01.694257+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf (643.6KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 2050 · 2026-05-23T19:04:08.369975+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf",
  "pages": "11-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf",
    "pages": "11-20"
  }
}
```

</details>

---


### Tool result

_source line 2051 · 2026-05-23T19:04:08.973268+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf (643.6KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 2052 · 2026-05-23T19:04:16.971818+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || echo \"pdfinfo not available\"",
  "description": "Get PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Get PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 2053 · 2026-05-23T19:04:17.886228+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Sat May 23 19:00:12 2026 UTC
ModDate:         Sat May 23 19:00:12 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           28
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       659011 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 914
}
```

</details>

---


### Tool call

_source line 2054 · 2026-05-23T19:04:17.898847+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf",
  "pages": "8-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf",
    "pages": "8-9"
  }
}
```

</details>

---


### Tool result

_source line 2055 · 2026-05-23T19:04:18.049918+00:00_

PDF pages extracted: 2 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf (643.6KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2056 · 2026-05-23T19:04:45.526601+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool call

_source line 2057 · 2026-05-23T19:04:45.778452+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 2058 · 2026-05-23T19:04:46.031383+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (173 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-multi-seed-llama-pw-seed789-v2 | LLaMA-3.1-8B PW seed789 多种子复制（westd-30973 cuda:1 全新运行）。替代 16639 cuda:0 上的慢速运行（12/600）。验证 SCB 在 ProofWriter 上跨 seed 稳定性。 | — | — | — |\n| exp-multi-seed-llama-pw-seed456-v2 | LLaMA-3.1-8B PW seed456 多种子复制（westd-30973 cuda:2 全新运行）。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。 | — | — | — |\n| exp-multi-seed-qwen25-pw-seed789-v3 | Qwen2.5-14B PW seed789 多种子复制（westd-30973 cuda:0 全新运行）。替代 v2 在 16639 cuda:2 上的慢速运行（53/600）。验证 SCB 在 ProofWriter 上跨 seed 稳定性。 | — | — | — |\n\n## 待处理\n- exp-multi-seed-llama-pw-seed456: LLaMA-3.1-8B PW seed456 多种子复制。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。（排队等待 GPU）\n- exp-deberta-ft-combo: Fine-tuned DeBERTa-large on ProofWriter OWA depth-5 achieves near-perfect NLI accuracy (99.67%) and provides massive combo gains over SC baseline when used as external verifier, demonstrating that domain-specific NLI fine-tuning breaks the SCB ceiling by providing truly independent verification signal.（准备中）\n- exp-multi-seed-mistral-folio: Multi-seed replication (seeds 123,456,789) of Mistral-7B × FOLIO-20
…[truncated 1733 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 504
}
```

</details>

---


### Tool result

_source line 2059 · 2026-05-23T19:04:46.031858+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 2060 · 2026-05-23T19:05:01.441191+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2061 · 2026-05-23T19:05:01.492032+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2062 · 2026-05-23T19:05:07.848066+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ -name \"config*\" -o -name \"project_config*\" 2>/dev/null | head -5",
  "description": "Find config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ -name \"config*\" -o -name \"project_config*\" 2>/dev/null | head -5",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 2063 · 2026-05-23T19:05:07.948997+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2064 · 2026-05-23T19:05:12.116095+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ 2>/dev/null | head -5 || echo \"NOT_FOUND\"",
  "description": "Search for paperreview config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ 2>/dev/null | head -5 || echo \"NOT_FOUND\"",
    "description": "Search for paperreview config"
  }
}
```

</details>

---


### Tool result

_source line 2065 · 2026-05-23T19:05:40.115053+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/chats/feishu_group_oc_c338e034cbffa10b9cc723e731d288d8_director.jsonl:{"ts": "2026-05-17T17:41:44.808222+00:00", "role": "tool_result", "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director", "text": "1\t---\n2\tname: review-director-session-start\n3\tdescription: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。\n4\tpriority: 9\n5\tscope: global\n6\ttags:\n7\t- workflow\n8\t- review\n9\t- session\n10\tversion: 3\n11\troles:\n12\t- review_director\n13\t---\n14\t\n15\t# Review Director Session 启动流程（圆桌会议模式）\n16\t\n17\t## 初始化\n18\t\n19\t1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）\n20\t2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在\n21\t3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）\n22\t4. 向用户简要汇报：\n23\t   - **投稿目标**：venue 和 deadline\n24\t   - **论文状态**：当前草稿位置和版本\n25\t   - **资料完整性**：提交的材料是否齐全\n26\t   - **下一步**：即将开始的圆桌审稿流程\n27\t\n28\t## 评审流程（收到论文提交后执行）\n29\t\n30\t### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）\n31\t\n32\t1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全\n33\t2. 确认目标投稿 venue（从提交消息中获取）\n34\t3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：\n35\t   - `\"&lt;venue name> 2026 call for papers\" site:aclweb.org`\n36\t   - `\"&lt;venue name> 2026 submission deadline\"`\n37\t   - `\"&lt;venue name> 2026 author guidelines\"`\n38\t4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续\n39\t5. 提取当前版本的格式要求：\n40\t   - 页数限制（正文 / 附录 / 参考文献）\n41\t   - 模板（ACL / IEEE / NeurIPS / ICML / ...）\n42\t   - 匿名规则（double-blind / single-blind / open）\n43\t   - 附录规则（是否允许、是否参与审稿）\n44\t   - 引用格式（natbib / biblatex / 特定 .bst）\n45\t6. 将以上信息作为上下文，随任务一起传递给 Reviewer\n46\t\n47\t⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。\n48\t\n49\t### Step 0.5 — 决定 Reviewer 编排\n50\t\n51\t根据 venue 类型和论文特点，决定：\n52\t- 需要几个 Reviewer（1-5 人）\n53\t- 每个 Reviewer 的审查侧重\n54\t\n55\t参考：\n56\t- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）\n57\t- **一般会议*
…[truncated 16156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 27998
}
```

</details>

---


### Tool call

_source line 2066 · 2026-05-23T19:05:59.626660+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "symb_invariant_consensus",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 2067 · 2026-05-23T19:06:29.991212+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 30364
}
```

</details>

---


### Tool call

_source line 2068 · 2026-05-23T19:06:30.493578+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验有效性**。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25（ARR May cycle）\n- **页数限制**: 正文 8 页，参考文献无限制，附录不限但不保证审稿人阅读\n- **模板**: ACL（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind（匿名提交）\n- **ARR 评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文信息\n- **标题**: \"Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning\"\n- **论文路径**: `projects/symb_invariant_consensus/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf`（28 页：正文 8 页 + 参考文献 3 页 + 附录 17 页）\n- **核心内容**: 提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理轨迹自提取逻辑约束，通过 Z3 weighted partial MAX-SAT 聚合答案。发现 SICA 在 6 个模型(7B-32B)、4 个推理领域上与 majority voting 结果几乎一致（>90% 问题答案相同），无统计显著正向效应。诊断原因为 \"symbolic confirmation bias\"——自提取约束系统性追随多数答案。27 种 training-free 变体均失败。Cross-architecture verification（DeBERTa NLI）在弱生成器上有效。提出三个零成本诊断指标。\n\n## 你的审查侧重\n\n**1. SICA Pipeline Soundness（重点）**\n- Eq.(1)-(4) 的数学推导是否完整、正确\n- Observation 1（Argmax Preservation）的条件和推导是否合理\n- Remark 1（Information Ceiling）中 DPI bound 的应用是否正确\n- Degeneration condition 的经验验证是否充分\n- σ(c, a) scoring function（Eq.3）中 source-attribution 的具体实现是否清晰可复现——特别是 domain constraint 变量和 answer assertion 变量在 Z3 中的关系\n- Algorithm 1 (MAX-SAT) 和 Algorithm 2 (Scoring) 的伪代码是否完整\n\n**2. 统计方法论**\n- McNemar exact test 的适用性（paired binary data）\n- Bootstrap CI 的方法和参数选择\n- FDR correction (BH) 的使用是否正确（m=6 confirmatory conditions 的选择依据）\n- TOST equivalence testing 的 margin 选择（±2pp）是否合理\n- Power analysis 和 MDE 计算的准确性\n- 多种子复制（multi-seed replication）的统计处理\n\n**3. 实验设计**\n- Oracle control 的设计是否能充分隔离自提取质量 vs 聚合机制\n- Oracle 结果是否仅限于 FOLIO 一个数据集（外部效度）\n- 27 种 remediation 策略的覆盖范围是否充分\n- Cross-architecture escape（DeBERTa NLI combo）的实验设计和因果推断\n- Capability-gap pattern 的证据强度（n=6 conditions, ρ=1.0）\n- Bias ratio (BR) 的 permutation null model 是否适当\n\n**4. 可复现性**\n- 超参数报告是否完整（K=12, T=0.7, T_ext=0.3, α=0.5, Z3 timeout 10s）\n- Prompt templates 是否完整文档化\n- 是否有未说明的数据处理步骤\n\n请按照 ARR reviewer guidelines 格式输出审稿意见：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-5 分)。",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验有效性**。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25（ARR May cycle）\n- **页数限制**: 正文 8 页，参考文献无限制，附录不限但不保证审稿人阅读\n- **模板**: ACL（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind（匿名提交）\n- **ARR 评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文信息\n- **标题**: \"Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning\"\n- **论文路径**: `projects/symb_invariant_consensus/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf`（28 页：正文 8 页 + 参考文献 3 页 + 附录 17 页）\n- **核心内容**: 提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理轨迹自提取逻辑约束，通过 Z3 weighted partial MAX-SAT 聚合答案。发现 SICA 在 6 个模型(7B-32B)、4 个推理领域上与 majority voting 结果几乎一致（>90% 问题答案相同），无统计显著正向效应。诊断原因为 \"symbolic confirmation bias\"——自提取约束系统性追随多数答案。27 种 training-free 变体均失败。Cross-architecture verification（DeBERTa NLI）在弱生成器上有效。提出三个零成本诊断指标。\n\n## 你的审查侧重\n\n**1. SICA Pipeline Soundness（重点）**\n- Eq.(1)-(4) 的数学推导是否完整、正确\n- Observation 1（Argmax Preservation）的条件和推导是否合理\n- Remark 1（Information Ceiling）中 DPI bound 的应用是否正确\n- Degeneration condition 的经验验证是否充分\n- σ(c, a) scoring function（Eq.3）中 source-attribution 的具体实现是否清晰可复现——特别是 domain constraint 变量和 answer assertion 变量在 Z3 中的关系\n- Algorithm 1 (MAX-SAT) 和 Algorithm 2 (Scoring) 的伪代码是否完整\n\n**2. 统计方法论**\n- McNemar exact test 的适用性（paired binary data）\n- Bootstrap CI 的方法和参数选择\n- FDR correction (BH) 的使用是否正确（m=6 confirmatory conditions 的选择依据）\n- TOST equivalence testing 的 margin 选择（±2pp）是否合理\n- Power analysis 和 MDE 计算的准确性\n- 多种子复制（multi-seed replication）的统计处理\n\n**3. 实验设计**\n- Oracle control 的设计是否能充分隔离自提取质量 vs 聚合机制\n- Oracle 结果是否仅限于 FOLIO 一个数据集（外部效度）\n- 27 种 remediation 策略的覆盖范围是否充分\n- Cross-architecture escape（DeBERTa NLI combo）的实验设计和因果推断\n- Capability-gap pattern 的证据强度（n=6 conditions, ρ=1.0）\n- Bias ratio (BR) 的 permutation null model 是否适当\n\n**4. 可复现性**\n- 超参数报告是否完整（K=12, T=0.7, T_ext=0.3, α=0.5, Z3 timeout 10s）\n- Prompt templates 是否完整文档化\n- 是否有未说明的数据处理步骤\n\n请按照 ARR reviewer guidelines 格式输出审稿意见：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-5 分)。",
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 2069 · 2026-05-23T19:06:56.452001+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25958
}
```

</details>

---


### Tool call

_source line 2070 · 2026-05-23T19:06:57.864067+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25（ARR May cycle）\n- **页数限制**: 正文 8 页，参考文献无限制，附录不限但不保证审稿人阅读\n- **模板**: ACL（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind（匿名提交）\n- **ARR 评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文信息\n- **标题**: \"Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning\"\n- **论文路径**: `projects/symb_invariant_consensus/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf`（28 页：正文 8 页 + 参考文献 3 页 + 附录 17 页）\n- **核心内容**: 负面结果论文。提出 SICA pipeline，发现自提取逻辑约束（经 Z3 验证）无法改善 LLM majority voting。将现象命名为 \"symbolic confirmation bias\" (SCB)——自提取约束系统性追随模型多数答案（bias ratio 1.66-4.97×, 9 models from 7B to frontier）。Observation 1 (Argmax Preservation) 和 Remark 1 (Information Ceiling via DPI) 提供结构性解释。27 种 training-free 变体均失败（independence-accuracy trade-off）。Cross-architecture escape (DeBERTa NLI) 提供初步证据。三个零成本诊断指标。\n\n## 你的审查侧重\n\n**1. 贡献新颖性（重点）**\n- \"Symbolic confirmation bias\" 概念是否有独立于已有工作的清晰新颖性\n- 与以下关键先行工作的差异化是否充分：\n  - Huang et al. (ICLR 2024): LLMs cannot self-correct without external feedback\n  - Stechly, Valmeekam & Kambhampati (ICLR 2025): self-verification limitations\n  - Chan et al. (2026): logical soundness alone is unreliable\n  - Wan et al. (2025): CoT confirmation bias\n- 负面结果的贡献定位是否清晰——\"我们证明了 X 不行\" vs \"我们解释了为什么 X 不行 + 提供了诊断工具\"\n- 三个贡献（symbolic mirage + diagnostic framework + cross-architecture escape）的独立新颖性\n- \"27 training-free variants\" 的穷举性是否构成独立贡献\n- 论文标题/Abstract 中 \"No Detectable Improvement\" 的 claim 强度是否与证据匹配\n\n**2. Related Work 完整性**\n- 检查是否遗漏了关键相关工作（特别是 neuro-symbolic reasoning、self-correction/verification、test-time compute scaling 领域的 2024-2026 重要论文）\n- Related Work §2 的分类和 positioning 是否准确\n- 与 Huang et al. (2024) 的关系——论文多次声称 \"extends and formalizes\" 其发现——这一 claim 是否准确\n- 是否有被引用但描述不准确的工作\n\n**3. 写作与呈现质量**\n- Abstract 是否在 200 words 以内（EMNLP 2026 硬要求）\n- Introduction 叙事流畅度和说服力\n- Figures/Tables 的信息密度和可读性\n- 正文 8 页内容是否完整自洽（不依赖附录才能理解核心论点）\n- 术语定义的一致性（如 \"symbolic confirmation bias\" vs \"SCB\", \"degeneration\" 等）\n- Limitations section 的覆盖范围和诚实度\n- 是否有 AI 写作痕迹、措辞不自然的段落\n\n**4. Framing 的一致性**\n- Abstract → Introduction → Results → Discussion 的故事线是否连贯\n- 贡献声明（Intro §1 最后三条）是否与实际结果一致\n- \"negative result\" 的 framing 是否恰当——是否存在过度推广（overclaiming）\n- Cross-architecture escape 的定位（正式贡献 vs 初步发现 vs future work）\n\n请按照 ARR reviewer guidelines 格式输出审稿意见：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-5 分)。",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25（ARR May cycle）\n- **页数限制**: 正文 8 页，参考文献无限制，附录不限但不保证审稿人阅读\n- **模板**: ACL（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind（匿名提交）\n- **ARR 评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文信息\n- **标题**: \"Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning\"\n- **论文路径**: `projects/symb_invariant_consensus/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_17/submitted.pdf`（28 页：正文 8 页 + 参考文献 3 页 + 附录 17 页）\n- **核心内容**: 负面结果论文。提出 SICA pipeline，发现自提取逻辑约束（经 Z3 验证）无法改善 LLM majority voting。将现象命名为 \"symbolic confirmation bias\" (SCB)——自提取约束系统性追随模型多数答案（bias ratio 1.66-4.97×, 9 models from 7B to frontier）。Observation 1 (Argmax Preservation) 和 Remark 1 (Information Ceiling via DPI) 提供结构性解释。27 种 training-free 变体均失败（independence-accuracy trade-off）。Cross-architecture escape (DeBERTa NLI) 提供初步证据。三个零成本诊断指标。\n\n## 你的审查侧重\n\n**1. 贡献新颖性（重点）**\n- \"Symbolic confirmation bias\" 概念是否有独立于已有工作的清晰新颖性\n- 与以下关键先行工作的差异化是否充分：\n  - Huang et al. (ICLR 2024): LLMs cannot self-correct without external feedback\n  - Stechly, Valmeekam & Kambhampati (ICLR 2025): self-verification limitations\n  - Chan et al. (2026): logical soundness alone is unreliable\n  - Wan et al. (2025): CoT confirmation bias\n- 负面结果的贡献定位是否清晰——\"我们证明了 X 不行\" vs \"我们解释了为什么 X 不行 + 提供了诊断工具\"\n- 三个贡献（symbolic mirage + diagnostic framework + cross-architecture escape）的独立新颖性\n- \"27 training-free variants\" 的穷举性是否构成独立贡献\n- 论文标题/Abstract 中 \"No Detectable Improvement\" 的 claim 强度是否与证据匹配\n\n**2. Related Work 完整性**\n- 检查是否遗漏了关键相关工作（特别是 neuro-symbolic reasoning、self-correction/verification、test-time compute scaling 领域的 2024-2026 重要论文）\n- Related Work §2 的分类和 positioning 是否准确\n- 与 Huang et al. (2024) 的关系——论文多次声称 \"extends and formalizes\" 其发现——这一 claim 是否准确\n- 是否有被引用但描述不准确的工作\n\n**3. 写作与呈现质量**\n- Abstract 是否在 200 words 以内（EMNLP 2026 硬要求）\n- Introduction 叙事流畅度和说服力\n- Figures/Tables 的信息密度和可读性\n- 正文 8 页内容是否完整自洽（不依赖附录才能理解核心论点）\n- 术语定义的一致性（如 \"symbolic confirmation bias\" vs \"SCB\", \"degeneration\" 等）\n- Limitations section 的覆盖范围和诚实度\n- 是否有 AI 写作痕迹、措辞不自然的段落\n\n**4. Framing 的一致性**\n- Abstract → Introduction → Results → Discussion 的故事线是否连贯\n- 贡献声明（Intro §1 最后三条）是否与实际结果一致\n- \"negative result\" 的 framing 是否恰当——是否存在过度推广（overclaiming）\n- Cross-architecture escape 的定位（正式贡献 vs 初步发现 vs future work）\n\n请按照 ARR reviewer guidelines 格式输出审稿意见：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-5 分)。",
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 2071 · 2026-05-23T19:06:59.179076+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1315
}
```

</details>

---


### Assistant

_source line 2072 · 2026-05-23T19:07:12.716943+00:00_

圆桌审稿已启动。当前状态：

| 任务 | 状态 |
|------|------|
| R1（方法严谨性 + 实验有效性） | 已派发，审稿中 |
| R2（新颖性 + 完整性） | 已派发，审稿中 |
| 视觉审查 Agent | 已启动，与 Reviewer 并行 |
| 外部审稿 | 未配置，跳过 |

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 147

## Round 147

2 recorded events


### User

_source line 2073 · 2026-05-23T19:13:52.608557+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 1

**论文**: "Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning"
**审查侧重**: 新颖性 + 完整性 + 写作质量 + Framing 一致性

---

## Summary

本文提出 SICA pipeline，将 LLM chain-of-thought 中的逻辑约束自提取、经 Z3 验证后通过加权 MAX-SAT 聚合，试图改进 majority voting。核心发现是负面的：自提取约束在 9 个模型（7B 至 frontier）、3 个逻辑推理数据集上均无法产生显著改进。作者将此现象命名为 "symbolic confirmation bias"（SCB），并通过 Observation 1（Argmax Preservation）和 Remark 1（DPI information ceiling）提供结构性解释。27 种 training-free 变体均因 independence-accuracy trade-off 而失败。Cross-architecture verification（DeBERTa NLI）在弱生成器上显示正面效果（+6.67 pp）。三个零成本诊断指标（C₀, K_eff, BR）用于预判 self-extraction 的失败模式。

---

## Strengths

**S1. 实验设计严谨且规模充分。** 9 个模型（Mistral-7B, LLaMA-3.1-8B/3-8B, Qwen2.5-7B/14B/32B, gpt-4.1, Gemini-2.5-Pro, R1-Distill-8B）× 3 数据集（FOLIO, ProofWriter, LogiQA）× 多种条件，统计方法完备：McNemar 检验、TOST 等价性检验（±2 pp margin）、bootstrap 95% CI、FDR 校正、power analysis（MDE 计算）。这在负面结果论文中极为罕见且值得称赞。（§3.2, §4, Table 1, Appendix D）

**S2. 结构性解释超越了纯经验观察。** Observation 1（source-attribution scoring + degeneration → argmax preservation）和 Remark 1（M→T→A→C Markov chain + DPI bound）将 "self-extraction doesn't work" 从经验发现提升为结构性不可能性结论——在 self-extraction 范式内，约束无法携带超越 trace 本身的信息。这是对 Huang et al. (2024) 的实质性推进：后者仅观察到 self-correction 失败，本文解释了*为什么*在最强验证设定（provably sound Z3）下仍然失败。（§5.1, §6, Figure 3）

**S3. 独立-准确率 trade-off 的发现具有实用价值。** 27 种 training-free 变体的系统探索（Figure 4, Table 14）揭示了一个基本矛盾：增加约束独立性的方法（diverse prompting、cross-model extraction 等）会破坏准确率，而保持准确率的方法使约束保持相关。这一 trade-off 对后续研究者有明确的指导意义。

**S4. 诊断框架可操作性强。** C₀（multi-candidate rate）、K_eff（effective ensemble size）、BR（bias ratio）三个指标均为零成本（无需 ground truth），且 Table 5/Figure 4 中的 Type A/B/C 分类能正确预测所有 60 个测试条件的失败模式。这为实践者提供了 "try before deploy" 的工具。

**S5. Cross-architecture escape 提供了建设性方向。** §6 中 DeBERTa NLI 作为外部验证器在 Mistral-7B 上取得 +6.67 pp（p < 0.001）的显著增益，验证了 "structural independence" 是打破 SCB 的关键——不是更好的 prompting，而是架构层面的独立性。

**S6. 写作质量整体良好。** 叙事从 "symbolic verification should help" → "it doesn't" → "here's why structurally" → "here's how to diagnose/escape" 逻辑连贯。Abstract 约 196 词，符合 EMNLP 200 词限制。术语使用一致（SCB/SICA 贯穿全文）。Limitations 简洁覆盖了主要局限。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1** [critical] 标题/Abstract "No Detectable Improvement" claim 与 cross-architecture 正面结果存在张力
- 具体位置：标题、Abstract 最后两句、§6
- 问题：标题 "Self-Extracted Constraints Provide No Detectable Improvement" 严格来说仅适用于 self-extraction 设定，但读者（包括检索系统）很可能将其理解为 "symbolic constraints don't help LLM reasoning"。而 §6 的 cross-architecture escape 恰好展示了 symbolic constraints *可以* 帮助——当约束来源独立于生成器时。Abstract 最后两句将 cross-architecture escape 和诊断并列在同一段中，削弱了两者的独立呈现。
- 为什么影响接收：标题是论文最重要的 claim，如果 claim 的 scope 不精确，reviewer/AC 会对整体 rigor 产生怀疑。负面结果论文的标题尤需精确界定 claim boundary。
- 建议修改方向：标题中加入 scope 限定词，如 "Self-Extracted Constraints Provide No Detectable Improvement *over Majority Voting* in LLM Reasoning"，或在 Abstract 中更早、更明确地区分 self-extracted vs. cross-architecture。

**N2** [critical] 新颖性相对于 Huang et al. (2024) 的差异化论述不够锐利
- 具体位置：§1 第3段（"extends and formalizes"）、§2 最后一段（"Distinction from CoT confirmation bias"）
- 问题：论文多次声称 "extends and formalizes" Huang et al. (2024)，但未充分阐明 *extension 的边际* 在哪里。Huang et al. 的核心 claim "LLMs cannot self-correct reasoning without external feedback" 在概念上已经涵盖了本文的主要发现——自提取约束是 self-correction 的一种形式，Z3 验证虽然是 "external" solver 但输入仍来自模型自身。读者可能会问：**如果我已经知道 Huang et al. 的结论，为什么还需要这篇论文？**
- 论文确实有独立贡献（Observation 1 的形式化、DPI bound、诊断框架、27 变体的 trade-off），但 Introduction 中这些贡献被 "extends and formalizes" 这一框架弱化了——给人的印象是 "confirmatory study" 而非 "independent discovery"。
- 为什么影响接收：对于负面结果论文，新颖性的论证是接收决定的核心。如果 reviewer 认为这只是 Huang et al. 在新 domain 的 replication，则贡献不足以达到 conference level。
- 建议修改方向：(1) 在 Introduction 中更明确地 frame *本文独有的* 贡献——不是 "extends" Huang 而是 "reveals a deeper structural mechanism (SCB) that Huang's empirical observation did not explain"；(2) 强调 Observation 1 + Remark 1 提供了 Huang et al. 所没有的 *explanatory power*——为什么 self-correction 失败，而不仅仅是 *that* it fails；(3) 强调诊断框架是 Huang et al. 没有提供的 *actionable toolkit*。

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Remark 1（DPI bound）的严谨性有提升空间
- 具体位置：§5.1, §6 第1段
- 问题：Remark 1 声称通过 M→T→A→C Markov chain 和 Data Processing Inequality 建立了信息上界 I(C;Y) ≤ I(T;Y) ≤ I(t_i;Y)。但 DPI 要求严格的 Markov 条件成立（即 C ⊥ M | A），论文仅通过经验证据间接支持这一假设（§5.1 中 99% 约束 propositional、degeneration condition |C*| ≈ 0）。论文将其标注为 "Remark" 而非 "Theorem" 是恰当的，但正文中使用 "bounds" 等语言暗示了比实际更强的形式化程度。
- 建议：(1) 在 Remark 1 后增加一句明确声明 Markov 条件为经验近似而非严格成立；(2) 可选地在 Appendix 中讨论 Markov 条件被违反时的 bound 松弛程度。

**W2** [warning] 数据集范围局限与 claim 泛化性之间的 gap
- 具体位置：标题（"LLM Reasoning"）、§3.2 Datasets、Limitations
- 问题：所有三个数据集（FOLIO n=204, ProofWriter depth-5 n=600, LogiQA n=600）都是形式/逻辑推理任务。标题说 "LLM Reasoning" 没有任何限定词，但结论可能不适用于数学推理（GSM8K/MATH）、常识推理、或代码生成等其他推理域。虽然 Limitations 提到 "all benchmarks are English logical reasoning"，但标题和 Abstract 的 claim scope 更广。
- 建议：标题或 Abstract 中增加 "logical reasoning" 或 "formal reasoning" 限定词；或在 §4 开头讨论为什么逻辑推理是 SCB 最可能被检测到的 domain（constraint formalization 最自然），从而论证如果连这里都失败，其他 domain 更可能失败。

**W3** [warning] "27 training-free variants" 的穷举性可能被高估
- 具体位置：Abstract（"Twenty-seven training-free variants fail"）、§5.2、Figure 4
- 问题：27 是一个令人印象深刻的数字，但细看 Figure 4 和 Table 14，许多 "变体" 是同一方法的参数调整（如不同 K 值、不同 α 值、不同 prompt template）。真正独立的方法类别只有约 4-5 种（paradigm-level: diverse prompting, cross-model, constraint set manipulation, scoring function, filtering）。这 27 个变体中可能还有其他有意义的方向被遗漏——例如 iterative constraint refinement（让模型看到 Z3 冲突后修正约束）或 constraint selection via LLM scoring（用另一个 LLM 评估约束质量）。
- 建议：在 §5.2 或 Appendix 中说明 27 个变体的分类方式和覆盖范围，讨论哪些方向被排除以及为什么。

**W4** [warning] Cross-architecture escape 的 capability-gap 依赖削弱了其一般性
- 具体位置：§6、Table 3
- 问题：DeBERTa NLI 的正面效果仅在弱生成器（Mistral-7B, SC ≤ 72%）上显著，强生成器（Qwen2.5-14B+）上无效甚至微降（Table 3）。论文将此归因于 "capability gap"（verifier 独立性只在 verifier 能力 > generator 时有用），但这意味着 cross-architecture escape 的实用价值局限于 "你有一个更强的外部验证器但不直接用它做推理" 的场景。这在实践中的应用场景较窄。
- 建议：讨论当 generator 和 verifier 都是强模型时（如 GPT-4 生成 + Claude 验证）是否仍存在 capability gap 效应；或者 capability gap 是否是 NLI 模型特有的（而非 LLM-based verifier 的一般性质）。

### Minor 问题（不影响接收）

- **M1**: "pp"（percentage points）在全文中广泛使用但未在首次出现时明确定义。
- **M2**: Figure 2 的散点图在灰度打印下可能难以区分模型颜色编码。建议增加 marker shape 差异或标注。
- **M3**: Table 2 信息密度极高（9 models × 3 datasets + bias metrics），建议考虑拆分或突出最关键的对比。
- **M4**: §5.1 中 "The pattern holds across nine models and 27 training-free variants (§5.1, §5.2)" 出现自引章节号，略显冗余。
- **M5**: Footnote 1 "Code and data will be released upon acceptance" — 对于负面结果论文，code/data 的可获取性对复现尤其重要。如果可能，建议在审稿阶段提供匿名 repo。
- **M6**: Figure 3 的 DAG 中 gold/gray 颜色区分较微妙，在小尺寸下不够清晰。

---

## Questions for Authors

**Q1**: Observation 1 证明了 trace-determined 约束在 source-attribution scoring 下必然 degenerate。但如果约束不通过 source-attribution scoring，而是通过语义相似度或 entailment 关系评分（即不追踪约束来自哪条 trace），Observation 1 是否仍然成立？换言之，source-attribution scoring 是 degeneration 的充分条件还是必要条件？

**Q2**: 论文在 §3.1 中设定 α = 0.5 作为 answer_assertion 权重。α 的选择是否经过系统搜索？如果 α → 0（完全不考虑 answer_assertion），SCB 是否会减弱？Table 41 和 Appendix L.2 中似乎有温度敏感性分析，但未看到 α 的系统消融。

**Q3**: 27 个 training-free 变体中，是否尝试过 "adversarial constraint generation"——即明确要求模型生成与当前多数答案*矛盾*的约束？这与 "diverse prompting" 不同——后者仅是提示多样化，而前者是显式鼓励反事实推理。

**Q4**: Cross-architecture escape 中 DeBERTa NLI 的 entailment/contradiction/neutral 三分类被映射为 NLI vote counts alongside SC votes（§6）。这个 combo 策略本质上是一个 ensemble——为什么不直接比较 DeBERTa standalone vs. DeBERTa+SICA combo？Table 3 有 standalone 数据（55.00%），但 combo 与 standalone 的差异分析不够充分。

---

## Missing References

1. **Snell et al. (2025)** "Scaling LLM Test-Time Compute Optimally" — 已引用 ✓
2. **Shala et al. (2025)** "Multi-agent verification" — 已引用 ✓
3. **Li et al. (AAAI 2026)** "A Survey on LLM Symbolic Reasoning" — 未引用。这是该领域迄今最全面的综述，包含了 symbolic reasoning + LLM 的系统性分类。建议在 §2 引用以提供更完整的 landscape。
4. **Qwen Team (2025)** "QwQ: Reflect on the boundaries of the unknown" — 已引用（§2, test-time compute）✓
5. **Ye et al. (2024) SatLM** — 已引用 ✓

整体相关工作覆盖度良好，未发现关键遗漏。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 实验方法严谨（McNemar/TOST/bootstrap/power analysis），9模型×3数据集规模充分。Observation 1 成立且有经验支持。Remark 1 的 Markov 条件为近似而非严格证明，但论文恰当地标注为 Remark。|
| Excitement | 3/5 | 负面结果对社区有价值（关闭了 "symbolic verification + self-extraction" 的乐观路径），诊断框架实用。但核心发现在概念上被 Huang et al. (2024) 预期，且仅覆盖逻辑推理域。Cross-architecture escape 有趣但初步。|
| Reproducibility | 4/5 | 实验细节详尽（Appendix A-K），prompt templates 完整（Appendix A），算法伪代码清晰（Algorithm 1-2）。代码承诺 release。|
| Confidence | 4/5 | 熟悉 LLM reasoning、self-consistency、neuro-symbolic 领域。仔细阅读了全文含附录。|

---

## 总体评分

**Overall**: 3.5 / 5（Borderline Conference）

**一句话总结**: 一篇实验严谨、结构解释有深度的负面结果论文，诊断框架具有实用价值，但核心发现对 Huang et al. (2024) 的增量有限，数据集范围仅限逻辑推理，cross-architecture escape 的一般性不足——整体处于 Conference 与 Findings 的边界。

**推荐理由**: 论文的主要价值在于 (1) 在 self-extraction 这一最强设定下验证了 self-correction 的结构性失败，(2) 提供了信息论层面的解释（DPI bound），(3) 给出了可操作的诊断工具。这些贡献超越了简单的 negative replication。但标题/claim 的泛化性超出了证据覆盖范围（仅逻辑推理），且与 Huang et al. 的 positioning 可以更锐利。如果作者能在 camera-ready 中 (a) 缩窄标题 scope，(b) 更鲜明地论述独立于 Huang et al. 的贡献，(c) 讨论 W2-W4 中的局限，我认为可以达到 Conference 水准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2074 · 2026-05-23T19:14:09.152086+00:00_

Reviewer 2 已提交审稿意见（3.5/5 Borderline Conference）。等待 Reviewer 1 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 148

## Round 148

2 recorded events


### User

_source line 2075 · 2026-05-23T19:14:11.659201+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审查结论**：Overall 3.5/5（Borderline Conference）。

核心判断：
- **Soundness 4/5**：实验方法论严谨，统计检验完备（McNemar/TOST/bootstrap/power analysis），9 模型规模充分
- **Excitement 3/5**：有价值的负面结果 + 诊断框架，但核心发现被 Huang et al. (2024) 概念性预期
- **两个 Must-Fix**：(N1) 标题 claim scope 与 cross-architecture 正面结果存在张力；(N2) 相对于 Huang et al. 的差异化论述需要更锐利
- **四个 Should-Fix**：Remark 1 的 DPI 严谨性、数据集范围 vs claim 泛化性、"27 variants" 穷举性高估、cross-architecture escape 的 capability-gap 局限

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2076 · 2026-05-23T19:14:26.025137+00:00_

R2 审稿收到（3.5/5 Borderline Conference）。等待 R1 审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 149

## Round 149

6 recorded events


### User

_source line 2077 · 2026-05-23T19:17:02.801225+00:00_

[Reviewer 1 审稿意见]:
## 总体评分

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 方法论严谨、统计分析透彻的负面结果论文，令人信服地展示了自提取符号约束在当前 LLM 上的退化现象，但 Observation 1 的形式化力度不足、oracle 证据的领域覆盖有限，削弱了核心因果主张的可推广性，constructive contribution 较薄弱。

## 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 统计方法论扎实（McNemar/Bootstrap/TOST/FDR），实验覆盖全面，但理论形式化为半形式化观察而非定理，oracle 证据领域受限 |
| Excitement | 3/5 | 重要的负面结果，对社区有实际价值（节省无效投入），但主要贡献是诊断性的，constructive contribution 仅限弱生成器上的 cross-architecture escape |
| Reproducibility | 4/5 | 超参数完整报告（K=12, T=0.7, T_ext=0.3, α=0.5, Z3 timeout 10s），Appendix A 提供完整 prompt templates，代码承诺接收后发布 |
| Confidence | 4/5 | 仔细阅读了全文 28 页（正文+附录），熟悉 SC、formal verification、LLM reasoning 相关工作 |

## Summary

本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought 推理轨迹中提取一阶逻辑约束，通过 Z3 weighted partial MAX-SAT 聚合答案。核心发现为负面结果：在 6 个模型（7B-32B）、多个推理领域（FOLIO, ProofWriter, LogiQA, StrategyQA/GSM8K/AIME）上，SICA 与 Self-Consistency 在 >90% 问题上答案一致，经 BH FDR 校正后无统计显著正向效应。作者将此诊断为 "symbolic confirmation bias"（SCB）——自提取约束系统性追随多数答案（BR > 1）。27 种 training-free remediation 策略均失败。Cross-architecture verification（DeBERTa NLI）仅在弱生成器上有效，受 capability-gap 规律支配。论文提出三个零成本诊断指标（C₀, K_eff, BR）。

## Strengths

**S1. 统计方法论严谨性远超同类工作。** McNemar exact test（paired binary data）、10,000 次 bootstrap CI（percentile method, seed 42; Table 7）、BH FDR correction（m=6 confirmatory conditions）、TOST equivalence testing（±2pp margin; Appendix U）、power analysis 与 MDE 计算（Table 6）、multi-seed replication（Table 42, 5 seeds）——每层统计检验都有清晰的方法论依据。这在 NLP 负面结果论文中非常少见。

**S2. 失败机制诊断清晰完整。** SCB 概念定义明确（BR 指标, Eq.5），经 9 个模型的跨域验证（Table 2, n=204）。DAG 因果图（Figure 3）直观展示了信息流瓶颈。Constraint ablation（Appendix H, Table 10：MAX-SAT=76.04%, count-only=76.22%, Random=75.87%）令人信服地证明约束未携带超越投票计数的信号。

**S3. 27 种 remediation 策略的系统性失败。** Figure 4 与 Table 14 覆盖 prompt-level（9 种）、method-level（3 种）、analytical conditions（17 种），spanning diverse prompting、iterative refinement、contrastive scoring、atom pipeline、UNSAT filtering 等。这种覆盖广度有力地证明退化是结构性的而非调参问题。

**S4. Cross-architecture escape 提供建设性方向。** Section 6 的 DeBERTa NLI 实验设计清晰——在 3 种 NLI 架构、108 种 verifier-generator-weight 组合（Figure 8）上验证 capability-gap pattern。CCR 指标（Appendix C, Eq.6）提供了量化评估框架。

**S5. 实用诊断框架。** C₀、K_eff、BR 三个零成本指标及其决策边界（Section 7, Appendix W）对从业者立即可用。SCB diagnostic toolkit 的 failure-mode 分类（degenerate / diversity-limited / confirmation-biased）可在 K=12 pilot run 后判断是否值得部署 self-extraction。

**S6. 写作质量。** 论文叙事结构清晰：问题定义（§3）→ 负面发现（§4）→ 机制诊断（§5）→ 失败证明（§5.2）→ 逃逸路径（§6）→ 实用工具（§7）。17 页附录提供了详尽的实验细节，主文保持了紧凑的 8 页结构。

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Oracle 实验仅限形式逻辑领域，核心因果主张的外部效度不足**
- 具体位置：Appendix G (Table 9, ProofWriter n=600), Section 1 contribution 3, Section 8 Limitations
- 问题：论文的核心因果推断之一是"瓶颈在于自提取质量而非聚合机制本身"。支撑该主张的直接证据是 oracle control——用 gold DSL 标注替换自提取约束后 SICA 表现提升。但 oracle 实验仅在 ProofWriter（Table 9）和 FOLIO（天然包含 FOL 标注）上进行，均为形式逻辑领域。对于 GSM8K、AIME、LogiQA，论文缺乏 oracle 约束。
- 替代假说未被排除：MAX-SAT 聚合机制可能对数学推理或常识推理中的约束类型天然不适用——例如数学等式约束之间的依赖关系可能无法被一阶逻辑的可满足性充分捕获。BR 分析（Table 2）提供了跨域间接证据，但 oracle 的直接因果证据是领域受限的。
- 为什么影响接收：Section 1 contribution 3 措辞暗示跨领域通用性（"Cross-architecture verification escapes the bias"），但 oracle 证据仅支持形式逻辑；若审稿人追问"聚合机制在数学推理上是否本身就有问题"，论文缺乏直接回应。
- 建议修改方向：(a) 在 GSM8K 上构建 partial oracle——利用人工标注的方程式约束（如 "x + 3 = 7" → Z3 约束）测试聚合机制在数学域的上界；(b) 或在 Limitations 中明确标注因果主张的领域限制，降低 Section 1 contribution 3 的普遍性表述。

**N2** [critical] **Observation 1 的形式化程度与其在论证链中的核心地位不匹配**
- 具体位置：Section 5.1 (page 6), Remark 2, Abstract, Introduction
- 问题：Observation 1（Argmax Preservation）给出三个退化条件：(i) |C'| ≈ 0, (ii) confirming |c| ≈ 1, (iii) approximately uniform constraint yield per trace。所有条件均使用"≈"且无误差界。Remark 2 (page 6) 承认这是 "an empirical conclusion building under degeneration, not an unconditional structural claim"。但 Abstract 中 "We show this degeneration is structural (Observation 1)" 和 Introduction 中的反复引用将其展示为理论贡献。半形式化观察被包装为结构性定理的程度之间存在落差。
- 为什么影响接收：理论方向的审稿人可能期望看到形式化界——例如"当 BR ≥ 1+δ 且 |C'|/|C| < ε 时，P(a*_SICA = a*_SC) ≥ 1 - f(δ,ε)"。当前表述在理论贡献可信度上存在风险。
- 建议修改方向：(a) 提供带宽松误差界的定理版本（附录中已有实证数据支撑，可以量化）；(b) 或调整措辞——在 Abstract/Introduction 中将 Observation 1 明确标记为"经验规律"而非"结构性结果"，避免 "structural" 一词的理论承诺。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Remark 1（DPI Information Ceiling）的理论贡献有限**
- 具体位置：Section 5.1 (page 6)
- 问题：Remark 1 援引 DPI 论证 I(C;Y) ≤ I(T(x);Y)。这是确定性后处理的一般性质——对任何函数 f(T) 都成立，并非 SICA 特有洞见。"Information Ceiling" 的命名暗示了特定于本方法的理论发现。
- 建议：或者降低展示权重（移至附录），或者补充实证量化 I(C;Y) 相对于 I(T(x);Y) 的具体损失比例（例如通过 mutual information estimation），使 DPI bound 的 tightness 可评估。

**W2** [warning] **Capability-gap pattern 基于 n=6 数据点**
- 具体位置：Section 6 (page 8), Figure 8
- 问题：monotonic capability-gap pattern 的核心证据为 n=6 generator-verifier 配对上的 Spearman ρ=1.0（exact permutation p=0.003）。108 种组合（Figure 8）扩展了覆盖面，但核心单调性主张仍依赖于少数不同能力水平的生成器。n=6 限制了因果推断强度。
- 建议：增加更多能力梯度的生成器（如 Phi-3-mini, Gemma-2-2B 等），或明确标注为初步证据。

**W3** [warning] **模型范围局限于开源 7B-32B**
- 具体位置：Section 3.2, Section 8
- 问题：前沿模型（GPT-4, Claude 等）可能具有更强的元认知能力和指令遵循能力，提取更高质量的约束。Table 2 的 closed-source 分析（gpt-4.1, Gemini-2.5-Pro 等）仅限 cross-model extraction 设置中的 BR 分析，未运行 full SICA pipeline。虽然 BR > 1 在所有模型上成立，但 BR 值的差异是否足以改变最终结果尚不明确。
- 建议：至少在一个前沿模型上运行 SICA full pipeline 的完整实验。

**W4** [warning] **BH FDR correction 的 m=6 选择标准可能存在后验偏差**
- 具体位置：Section 4 (Table 1)
- 问题：m=6 confirmatory conditions 的选择基于 C₀ < 5%, K_eff ≥ 1.30, SC < 80% 等阈值。这些阈值是否在观察结果之前确定？如果是数据驱动的选择，可能引入选择偏差。论文未说明这些标准是预注册还是后验确定。
- 建议：(a) 声明阈值的确定顺序（先验 vs. 后验）；(b) 提供全部条件（包括 degenerate 条件）的非校正 p 值作为 supplementary 参考。

## 小问题（不影响接收）

- **M1**: Figure 2 y 轴 "SICA Δ" 首次出现时未明确标注单位（百分点）。
- **M2**: Table 1 脚注符号密度较高（*,†,◦,●），可考虑简化。
- **M3**: Section 2 对 Huang et al. (2024) 的详细讨论（"三个方面的扩展"）偏长，可精简节省正文空间。
- **M4**: Appendix Z (Use of AI Assistants) 声明使用 Claude 辅助写作和代码，这符合 ARR 政策但应确认是否需要在 submission form 中额外声明。

## Questions

**Q1.** Appendix H (Table 10) 的 "Random" baseline 是如何构造的？随机打乱 constraint-trace 对应关系，还是生成随机约束？这对判断 source-attribution 的因果效应至关重要。

**Q2.** α=0.5 的选择依据？Table 14 显示 strategy #19 包含 "α variation"——α 取极端值（0 或 1）时退化程度如何变化？当 α→0（完全依赖 Z3 可满足性权重），source-attribution 的影响是否消失？

**Q3.** ProofWriter oracle（Appendix G）中，oracle 约束是否经过与自提取约束相同的 Z3 dedup 流程？若未经 dedup，则 oracle vs. self-extraction 的比较可能受 dedup 策略差异混淆。

**Q4.** Cross-architecture NLI verifier (Section 6) 中 DeBERTa 判断的粒度——是 constraint 级别还是 trace 级别？

**Q5.** 是否考虑过提取 trace 间 disagreement 而非 trace 内约束？若约束捕获的是"轨迹 i 与轨迹 j 在 X 上不一致"，source-attribution coupling 可能被打破。

## Missing References

- Weng et al. (2023) "Large Language Models are Better Reasoners with Self-Verification" 论文已引用但 Section 2 中未深入对比其 backward verification 方法与 SICA 的差异。
- 可考虑引用 process reward model (PRM) 相关工作（如 Math-Shepherd, Luo et al. 2024）作为替代性 trace-level 信号提取方法的对比。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2078 · 2026-05-23T19:17:47.673786+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见 — Round 1\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Soundness**: 4/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n### Strengths\nS1. 实验设计严谨且规模充分（9 模型 × 3 数据集，统计方法完备）\nS2. 结构性解释超越纯经验观察（Observation 1 + Remark 1 将经验发现提升为结构性不可能性结论，对 Huang et al. 2024 的实质推进）\nS3. 独立-准确率 trade-off 的发现具有实用价值（27 种变体的系统探索）\nS4. 诊断框架可操作性强（C₀, K_eff, BR 三指标，零成本，60 条件验证）\nS5. Cross-architecture escape 提供建设性方向（DeBERTa NLI +6.67pp）\nS6. 写作质量整体良好（叙事连贯，Abstract ~196 词符合限制）\n\n### Must-Fix\nN1. 标题/Abstract \"No Detectable Improvement\" claim 与 cross-architecture 正面结果存在张力——标题 scope 不精确，读者可能理解为 \"symbolic constraints don't help LLM reasoning\"，但 §6 恰好展示了 symbolic constraints 在 cross-architecture 下可以帮助。\nN2. 新颖性相对于 Huang et al. (2024) 的差异化论述不够锐利——\"extends and formalizes\" 框架弱化了论文的独立贡献，给人 \"confirmatory study\" 的印象。\n\n### Should-Fix\nW1. Remark 1（DPI bound）的严谨性有提升空间——DPI 要求严格 Markov 条件，论文仅通过经验证据间接支持。\nW2. 数据集范围局限与 claim 泛化性之间的 gap——所有数据集均为形式/逻辑推理，但标题说 \"LLM Reasoning\"。\nW3. \"27 training-free variants\" 的穷举性可能被高估——真正独立的方法类别约 4-5 种，且可能遗漏了 iterative constraint refinement 等方向。\nW4. Cross-architecture escape 的 capability-gap 依赖削弱一般性——仅在弱生成器（SC ≤ 72%）上显著。\n\n### Minor\nM1-M6：pp 未定义、Figure 2 灰度可读性、Table 2 信息密度、自引章节号冗余、匿名 repo 建议、Figure 3 颜色区分。\n\n### Questions\nQ1. 若不用 source-attribution scoring 而用语义相似度评分，Observation 1 是否仍成立？\nQ2. α=0.5 是否经过系统搜索？α→0 时 SCB 是否减弱？\nQ3. 是否尝试过 adversarial constraint generation（显式鼓励反事实推理）？\nQ4. DeBERTa NLI 判断的粒度——constraint 级别还是 trace 级别？combo vs standalone 差异分析不充分。\n\n### Missing References\n- Li et al. (AAAI 2026) \"A Survey on LLM Symbolic Reasoning\"\n\n---\n\n请对以上每个要点逐条回应 [AGREE] 或 [REBUT]。",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见 — Round 1\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Soundness**: 4/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n### Strengths\nS1. 实验设计严谨且规模充分（9 模型 × 3 数据集，统计方法完备）\nS2. 结构性解释超越纯经验观察（Observation 1 + Remark 1 将经验发现提升为结构性不可能性结论，对 Huang et al. 2024 的实质推进）\nS3. 独立-准确率 trade-off 的发现具有实用价值（27 种变体的系统探索）\nS4. 诊断框架可操作性强（C₀, K_eff, BR 三指标，零成本，60 条件验证）\nS5. Cross-architecture escape 提供建设性方向（DeBERTa NLI +6.67pp）\nS6. 写作质量整体良好（叙事连贯，Abstract ~196 词符合限制）\n\n### Must-Fix\nN1. 标题/Abstract \"No Detectable Improvement\" claim 与 cross-architecture 正面结果存在张力——标题 scope 不精确，读者可能理解为 \"symbolic constraints don't help LLM reasoning\"，但 §6 恰好展示了 symbolic constraints 在 cross-architecture 下可以帮助。\nN2. 新颖性相对于 Huang et al. (2024) 的差异化论述不够锐利——\"extends and formalizes\" 框架弱化了论文的独立贡献，给人 \"confirmatory study\" 的印象。\n\n### Should-Fix\nW1. Remark 1（DPI bound）的严谨性有提升空间——DPI 要求严格 Markov 条件，论文仅通过经验证据间接支持。\nW2. 数据集范围局限与 claim 泛化性之间的 gap——所有数据集均为形式/逻辑推理，但标题说 \"LLM Reasoning\"。\nW3. \"27 training-free variants\" 的穷举性可能被高估——真正独立的方法类别约 4-5 种，且可能遗漏了 iterative constraint refinement 等方向。\nW4. Cross-architecture escape 的 capability-gap 依赖削弱一般性——仅在弱生成器（SC ≤ 72%）上显著。\n\n### Minor\nM1-M6：pp 未定义、Figure 2 灰度可读性、Table 2 信息密度、自引章节号冗余、匿名 repo 建议、Figure 3 颜色区分。\n\n### Questions\nQ1. 若不用 source-attribution scoring 而用语义相似度评分，Observation 1 是否仍成立？\nQ2. α=0.5 是否经过系统搜索？α→0 时 SCB 是否减弱？\nQ3. 是否尝试过 adversarial constraint generation（显式鼓励反事实推理）？\nQ4. DeBERTa NLI 判断的粒度——constraint 级别还是 trace 级别？combo vs standalone 差异分析不充分。\n\n### Missing References\n- Li et al. (AAAI 2026) \"A Survey on LLM Symbolic Reasoning\"\n\n---\n\n请对以上每个要点逐条回应 [AGREE] 或 [REBUT]。",
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 2079 · 2026-05-23T19:18:08.972038+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21298
}
```

</details>

---


### Tool call

_source line 2080 · 2026-05-23T19:18:09.099163+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见 — Round 1\n\n**Overall**: 3.5 (Borderline Conference)\n**Soundness**: 4/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n### Strengths\nS1. 统计方法论严谨性远超同类（McNemar/Bootstrap/TOST/FDR/power analysis/multi-seed）\nS2. 失败机制诊断清晰完整（SCB 概念 + DAG + Constraint ablation 803/804 agreement）\nS3. 27 种 remediation 策略的系统性失败（Figure 4, Table 14）\nS4. Cross-architecture escape 提供建设性方向（108 种组合，CCR 指标）\nS5. 实用诊断框架（C₀, K_eff, BR，failure-mode 分类）\nS6. 写作质量好（叙事清晰，17 页附录详尽）\n\n### Must-Fix\nN1. Oracle 实验仅限形式逻辑领域（FOLIO + ProofWriter），核心因果主张\"瓶颈在自提取质量而非聚合机制\"的外部效度不足。替代假说未排除：MAX-SAT 对数学推理约束可能天然不适用。\nN2. Observation 1 的形式化程度与其核心地位不匹配——三个条件均用\"≈\"且无误差界，被 Abstract/Intro 包装为\"structural\"结果，但实际是半形式化经验观察。\n\n### Should-Fix\nW1. Remark 1（DPI Information Ceiling）理论贡献有限——DPI 是确定性后处理的一般性质，非 SICA 特有洞见，\"Information Ceiling\" 命名暗示特定理论发现。\nW2. Capability-gap pattern 基于 n=6 数据点（Spearman ρ=1.0, p=0.003），因果推断强度受限。\nW3. 模型范围局限于开源 7B-32B——前沿模型（GPT-4, Claude）可能有更强元认知能力，Table 2 的 closed-source 分析仅限 BR 分析未跑 full pipeline。\nW4. BH FDR correction 的 m=6 选择标准可能存在后验偏差——阈值（C₀ < 5%, K_eff ≥ 1.30, SC < 80%）是否预先确定未说明。\n\n### Minor\nM1-M4：Figure 2 y 轴单位、Table 1 脚注密度、Section 2 Huang et al. 讨论偏长、Appendix Z AI 辅助声明确认。\n\n### Questions\nQ1. Table 10 \"Random\" baseline 如何构造？随机打乱 constraint-trace 对应还是生成随机约束？\nQ2. α=0.5 选择依据？α 取极端值（0 或 1）时退化程度变化？α→0 时 source-attribution 影响是否消失？\nQ3. ProofWriter oracle 约束是否经过与自提取相同的 Z3 dedup 流程？\nQ4. DeBERTa NLI 判断粒度——constraint 级别还是 trace 级别？\nQ5. 是否考虑过提取 trace 间 disagreement 而非 trace 内约束？\n\n### Missing References\n- Weng et al. (2023) 的 backward verification 方法与 SICA 的差异未深入对比\n- PRM 相关工作（Math-Shepherd 等）作为替代 trace-level 信号提取\n\n---\n\n请对以上每个要点逐条回应 [AGREE] 或 [REBUT]。",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见 — Round 1\n\n**Overall**: 3.5 (Borderline Conference)\n**Soundness**: 4/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n### Strengths\nS1. 统计方法论严谨性远超同类（McNemar/Bootstrap/TOST/FDR/power analysis/multi-seed）\nS2. 失败机制诊断清晰完整（SCB 概念 + DAG + Constraint ablation 803/804 agreement）\nS3. 27 种 remediation 策略的系统性失败（Figure 4, Table 14）\nS4. Cross-architecture escape 提供建设性方向（108 种组合，CCR 指标）\nS5. 实用诊断框架（C₀, K_eff, BR，failure-mode 分类）\nS6. 写作质量好（叙事清晰，17 页附录详尽）\n\n### Must-Fix\nN1. Oracle 实验仅限形式逻辑领域（FOLIO + ProofWriter），核心因果主张\"瓶颈在自提取质量而非聚合机制\"的外部效度不足。替代假说未排除：MAX-SAT 对数学推理约束可能天然不适用。\nN2. Observation 1 的形式化程度与其核心地位不匹配——三个条件均用\"≈\"且无误差界，被 Abstract/Intro 包装为\"structural\"结果，但实际是半形式化经验观察。\n\n### Should-Fix\nW1. Remark 1（DPI Information Ceiling）理论贡献有限——DPI 是确定性后处理的一般性质，非 SICA 特有洞见，\"Information Ceiling\" 命名暗示特定理论发现。\nW2. Capability-gap pattern 基于 n=6 数据点（Spearman ρ=1.0, p=0.003），因果推断强度受限。\nW3. 模型范围局限于开源 7B-32B——前沿模型（GPT-4, Claude）可能有更强元认知能力，Table 2 的 closed-source 分析仅限 BR 分析未跑 full pipeline。\nW4. BH FDR correction 的 m=6 选择标准可能存在后验偏差——阈值（C₀ < 5%, K_eff ≥ 1.30, SC < 80%）是否预先确定未说明。\n\n### Minor\nM1-M4：Figure 2 y 轴单位、Table 1 脚注密度、Section 2 Huang et al. 讨论偏长、Appendix Z AI 辅助声明确认。\n\n### Questions\nQ1. Table 10 \"Random\" baseline 如何构造？随机打乱 constraint-trace 对应还是生成随机约束？\nQ2. α=0.5 选择依据？α 取极端值（0 或 1）时退化程度变化？α→0 时 source-attribution 影响是否消失？\nQ3. ProofWriter oracle 约束是否经过与自提取相同的 Z3 dedup 流程？\nQ4. DeBERTa NLI 判断粒度——constraint 级别还是 trace 级别？\nQ5. 是否考虑过提取 trace 间 disagreement 而非 trace 内约束？\n\n### Missing References\n- Weng et al. (2023) 的 backward verification 方法与 SICA 的差异未深入对比\n- PRM 相关工作（Math-Shepherd 等）作为替代 trace-level 信号提取\n\n---\n\n请对以上每个要点逐条回应 [AGREE] 或 [REBUT]。",
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 2081 · 2026-05-23T19:18:10.445086+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1345
}
```

</details>

---


### Assistant

_source line 2082 · 2026-05-23T19:18:26.293157+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 150

## Round 150

2 recorded events


### User

_source line 2083 · 2026-05-23T19:18:28.752333+00:00_

[Reviewer 1 审稿结果]:
PDF 临时图片已清理。审稿完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2084 · 2026-05-23T19:18:35.584394+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 151

## Round 151

2 recorded events


### User

_source line 2085 · 2026-05-23T19:21:11.909299+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Strengths 回应

[AGREE] R2-S1: 实验规模和统计方法完备。与我的 S1 一致。补充：论文的统计方法论（McNemar + Bootstrap CI + TOST + BH FDR + Power Analysis）是我在该领域审过的论文中最系统的之一。

[AGREE] R2-S2: 结构性解释超越纯经验观察。R2 的表述比我更积极——我在 N2 中指出 Observation 1 的形式化程度不足。但我同意论文在 Huang et al. (2024) 基础上做了实质推进，不仅是经验复制。Observation 1 + BR metric + degeneration condition 确实构成了一个连贯的结构性解释。

[AGREE] R2-S3: 独立-准确率 trade-off 有实用价值。27 种变体的系统性失败令人信服（Figure 4, Table 14）。

[AGREE] R2-S4: 诊断框架可操作。C₀、K_eff、BR 三指标的零成本特性和 60 条件验证使其立即可部署。

[AGREE] R2-S5: Cross-architecture escape 建设性。同我的 S4。

[AGREE] R2-S6: 写作质量良好。同意。叙事从负面发现→机制诊断→逃逸路径的弧线清晰。

---

### Must-Fix 回应

[REBUT] R2-N1: **标题 scope 不精确——"No Detectable Improvement" 与 cross-architecture 正面结果存在张力**

R2 的担忧有一定合理性，但我认为标题实际上是精确的，不构成 Must-Fix。

理由：
1. **标题限定词是 "Self-Extracted Constraints"**——cross-architecture escape（Section 6）使用 DeBERTa NLI 作为**外部**验证器。增益来源不是自提取约束本身，而是外部模型提供的**独立信号**。论文在 Section 7 明确指出："the value of formal verification depends on the independence of its inputs, not the soundness of its logic"（page 8）。也就是说，自提取约束的信息量确实为零（BR consistently > 1, Table 2），改善来自外部验证器打破了 confirmation bias。
2. **Section 6 的 combo mode 中**，DeBERTa NLI 的投票是**附加**在 SC 之上的（"each NLI-supporting vote counts as votes alongside SC's votes"），而非单纯依赖自提取约束。改善来自于 NLI verifier 的独立判断力，不是约束质量。
3. **然而**，我同意标题可能被快速阅读的读者误读为"symbolic constraints 在任何设置下都不帮助 LLM reasoning"。建议将此降级为 **Should-Fix**，可通过在 Abstract 中增加一句限定语解决（如"under self-extraction; cross-architecture verification escapes this limitation"），而非修改标题。

[REBUT] R2-N2: **新颖性相对于 Huang et al. (2024) 差异化论述不够锐利**

R2 认为 "extends and formalizes" 的措辞给人 confirmatory study 印象。我部分理解这一担忧，但认为论文的实际贡献远超 confirmation：

1. **方法论差异实质性大**：Huang et al. (2024) 测试的是非形式化的 self-verification（LLM 自己判断对错）；本文构建了完整的 formal pipeline——Z3 MAX-SAT solver + first-order logic extraction + source-attribution scoring（Algorithm 1-2, Appendix B）。这不是同一方法的重复验证，而是测试了一个**更强的假设**——即使有 provably sound solver（Z3），自提取约束仍然退化。
2. **独有贡献清单**（Huang et al. 完全没有的）：
   - Observation 1 的 argmax preservation 条件（Section 5.1）
   - BR metric 及其 permutation null model（Eq.5, Table 2）
   - 27 种 remediation 策略的系统探索（Figure 4, Table 14）
   - Cross-architecture escape + capability-gap pattern（Section 6, Figure 8）
   - C₀/K_eff/BR 诊断框架（Section 7）
3. **然而**，我同意论文的 framing 可以更锐利。"extends and formalizes" 确实低估了自己的贡献。建议将此降级为 **Should-Fix**——属于写作策略问题，不影响技术贡献的实质。

---

### Should-Fix 回应

[AGREE] R2-W1: **Remark 1 DPI bound 严谨性有提升空间**

与我的 W1 一致。DPI 要求严格 Markov 条件 Y→T(x)→C，但论文仅通过经验证据（ProcessSim, Table 21; BR 分析, Table 2）间接支持该链的成立。补充：即使 Markov 条件成立，DPI bound 对任何确定性后处理都成立（I(f(X);Y) ≤ I(X;Y)），因此 Remark 1 的特异性贡献有限。

[REBUT] R2-W2: **"所有数据集均为形式/逻辑推理"——事实不准确**

R2 声称所有数据集均为形式/逻辑推理，这与论文内容不符：
1. **论文明确包含非逻辑领域数据集**：GSM8K（数学推理, Section 3.2）、AIME 2024（竞赛数学）、StrategyQA（常识推理）、ARC-Challenge（科学问答）。Table 2（page 6）报告了 gpt-4.1/gpt-5.5/Gemini-2.5-Pro 在 5 个 frontier models 上的 cross-model extraction 结果，覆盖多个领域。
2. **然而**，R2 的关切有部分合理性——Table 1 的 6 个 confirmatory conditions（主要结论的统计基础）仅覆盖 FOLIO、PW-DS、LogiQA，均为逻辑推理。GSM8K 和 AIME 被归入 "degenerate regime"（C₀ < 5%），仅作为退化的例证而非 confirmatory 测试。
3. **我的立场**：R2 的事实判断有误（"所有"→实际上不是），但其底层关切（confirmatory 分析集中于逻辑领域）有效。建议保持 Should-Fix，但修正表述。

[AGREE] R2-W3: **27 种变体的穷举性可能被高估**

部分同意。Table 14 中许多策略是同一方法类别的参数变体（如不同 α 值、不同 threshold），真正独立的方法类别确实约 4-5 种（prompt variation、cross-model extraction、contrastive scoring、iterative refinement、analytical filtering）。

**但反驳 R2 关于遗漏 iterative constraint refinement 的具体判断**：Table 14 strategy #3 明确列出 "iterative self-improvement"（type: Incentive, target: Self improvement），strategy #22 "Bootstrapped gold" 也涉及迭代精炼。所以 iterative refinement 并未被遗漏。

补充我的观察：论文更大的遗漏可能是**未测试 fine-tuned constraint extractors**——所有 27 种策略均为 training-free，但 fine-tuned 提取器（如在少量 gold annotations 上训练）可能打破 SCB。论文在 Limitations 中未明确标注这一范围限制。

[AGREE] R2-W4: **Cross-architecture escape 的 capability-gap 依赖削弱一般性**

与我的 W2 一致。仅在弱生成器（SC ≤ 72%, Mistral-7B）上显著，强生成器（Qwen2.5-14B, SC ≥ 72%）上 combo gain ≤ +0.83pp（Table 3, page 8）甚至负向。这严重限制了 cross-architecture escape 的实际适用范围。

---

### Minor 回应

[AGREE] R2-M1: pp 应在首次使用时定义（percentage points）。

[AGREE] R2-M2: Figure 2 灰度可读性可改善。

[AGREE] R2-M3: Table 2 信息密度高，可考虑拆分或简化。

[AGREE] R2-M4: 自引章节号冗余。

[AGREE] R2-M5: 匿名 repo 对 reproducibility 有帮助。

[AGREE] R2-M6: Figure 3 颜色区分可改善。

---

### Questions 回应

[AGREE] R2-Q1: **语义相似度评分 vs source-attribution scoring 下 Observation 1 是否仍成立？**

优秀的问题。与我的 Q2（α sensitivity）高度相关。论文的 source-attribution scoring（σ(c,a)=1 iff c 来自支持 a 的 trace）**内建了**约束与源答案的耦合。如果改用语义相似度（如 embedding cosine similarity），耦合机制会不同。但论文通过 BR 分析（Table 2）间接论证了即使不用 source-attribution，约束本身也语义上追随多数答案——BR > 1 衡量的是约束内容（而非来源标签）与多数答案的对齐度。**然而**，该间接论证需要直接实验验证——替换 scoring function 后重新运行 pipeline。这是论文应回答的关键 ablation。

[AGREE] R2-Q2: **α=0.5 是否经过系统搜索？**

与我的 Q2 完全一致。Table 14 strategy #19 ("Scoring bias", α variation) 表明 α 被变体过，但具体结果未单独报告。特别是 α→0 时（完全依赖 Z3 可满足性权重，不用 source-attribution），退化是否减弱？这直接关系到 R2-Q1 的回答。

[AGREE] R2-Q3: **是否尝试过 adversarial constraint generation？**

好问题。Table 14 中 strategy #6 "Contrastive"（Multi-round, Consistency）和 strategy #4 "Devil's advocate" 是最接近的，但未见显式的"生成反驳多数答案的约束"的 adversarial prompting。这类策略可能通过强制生成反事实约束来打破 confirmation bias——如果 prompt 明确要求"列出当前答案可能错误的原因及其形式化约束"，提取的约束可能不再追随多数答案。

[AGREE] R2-Q4: **DeBERTa NLI 判断粒度——constraint vs trace level？**

与我的 Q4 一致。Section 6（page 7）描述："to classify (premise, conclusion) pairs as entailment, contradiction, or neutral. In combo mode, each NLI-supporting vote counts as votes alongside SC's votes." 但未明确 premise 是单个 constraint 还是整条 trace。这对理解 DeBERTa 如何打破 confirmation bias 至关重要——如果是 constraint 级别，DeBERTa 逐条独立评估约束与答案的蕴含关系，其判断不受 source-attribution 影响；如果是 trace 级别，DeBERTa 可能仍受 trace 内部答案一致性的影响。

---

### Missing References 回应

[REBUT] R2-Missing: **Li et al. (AAAI 2026) "A Survey on LLM Symbolic Reasoning"**

我无法验证该引用的真实性。AAAI 2026 的论文列表尚未完整公开（截至 2026-05-23），R2 应提供更具体的引用信息（作者全名、arXiv ID 等）以便核实。建议 Director 要求 R2 确认该引用来源。

---

### 总体评估

与 R2 的 Overall 3.5 一致。

**我与 R2 的主要分歧**：
1. **N1（标题张力）**：R2 列为 Must-Fix，我认为应降级为 Should-Fix——标题中 "Self-Extracted" 限定词已充分区分了自提取约束与 cross-architecture verification。
2. **N2（新颖性）**：R2 列为 Must-Fix，我认为应降级为 Should-Fix——论文实际贡献远超 confirmatory study（完整 formal pipeline + 27 strategies + escape + diagnostics），问题在于 framing 太谦虚而非贡献不足。
3. **W2（数据集范围）**：R2 的事实判断"所有数据集均为形式/逻辑推理"不准确——论文包含 GSM8K、AIME、StrategyQA、ARC-Challenge 等非逻辑领域数据集。但 confirmatory 分析集中于逻辑领域的关切是有效的。

**我与 R2 的一致点**：
- W1 (DPI), W3 (27 variants 穷举性), W4 (capability-gap 限制) 判断一致
- Q1-Q4 均为论文应回答的重要问题
- Minor issues 全部同意

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2086 · 2026-05-23T19:21:25.001183+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 152

## Round 152

2 recorded events


### User

_source line 2087 · 2026-05-23T19:21:28.449370+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

与 R2 的核心分歧在两个 Must-Fix 上：R2-N1（标题张力）和 R2-N2（新颖性），我均建议降级为 Should-Fix——标题的 "Self-Extracted" 限定词已足够精确，论文实际贡献远超 confirmatory study，问题在于 framing 过于谦虚。在 W2（数据集范围）上纠正了 R2 的事实错误（论文包含 GSM8K/AIME/StrategyQA 等非逻辑领域），但同意 confirmatory 分析集中于逻辑领域的关切。其余 Should-Fix 和 Questions 基本一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2088 · 2026-05-23T19:21:36.201339+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 153

## Round 153

18 recorded events


### User

_source line 2089 · 2026-05-23T19:21:37.710433+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的逐条回应

---

### Strengths

[AGREE] S1: 完全同意。统计方法论（McNemar / TOST / Bootstrap CI / FDR / Power analysis / multi-seed）的组合在 NLP 负面结果论文中极为罕见。尤其是 TOST 等价性检验（±2 pp margin）和 MDE 计算，真正做到了区分 "no effect detected" 和 "equivalence confirmed"。

[AGREE] S2: 完全同意。SCB 的诊断链条（BR > 1 → degeneration → argmax preservation → 803/804 agreement）逻辑自洽，Table 10 的 constraint ablation 是关键证据。

[AGREE] S3: 同意，但附带我自己的保留意见——27 种变体中真正独立的方法类别约 4-5 种，部分为参数调整（见我的 W3）。穷举性值得肯定，但 "27" 这个数字的宣传力度可能略高于实际方法多样性。

[AGREE] S4: 同意。CCR 指标（Appendix C）和 108 种 verifier-generator 组合的系统性是亮点。但我的 W4 与 R1 的 W2 观点一致——capability-gap 结论的数据基础较薄。

[AGREE] S5: 同意。C₀/K_eff/BR 三指标的零成本特性和 failure-mode 分类（Type A/B/C）在 Table 5 中的验证令人信服。

[AGREE] S6: 同意。叙事清晰，17 页附录详尽且有组织。

---

### Must-Fix

**[AGREE] R1-N1**: 外部效度（oracle 实验仅限形式逻辑）
同意这是一个实质性问题，且与我自己的 W2 互补。我的 W2 聚焦于标题/claim 的泛化性超出数据集范围（"LLM Reasoning" vs. 仅逻辑推理），R1-N1 进一步指出 oracle 实验的因果推断也受限。R1 提出的替代假说——"MAX-SAT 对数学推理约束可能天然不适用"——是合理的，因为数学推理的约束结构（数值等式/不等式）与逻辑推理的约束结构（命题/一阶逻辑）在 MAX-SAT 框架中的建模方式可能有本质差异。

不过，我认为论文 partially 回应了这一点：§F（Appendix, page 15-16）中 ProofWriter oracle 约束通过 DSL→Z3 的确定性映射验证了 MAX-SAT 聚合 *在给定好约束时* 能工作（97.14% accuracy on parseable problems）。这至少证明了聚合机制本身没问题——瓶颈确在提取端。但这一因果推断的适用域仅限于形式逻辑，R1 说得对。

**建议**：作者应在 Limitations 中明确讨论 oracle 实验的域局限性，并说明为什么逻辑推理是 SCB 最容易被检测到的 "best-case" domain（constraint formalization 最自然），从而论证 negative result 的下界意义。

---

**[AGREE] R1-N2**: Observation 1 的形式化程度与呈现强度不匹配
部分同意。R1 准确指出了三个条件中 "≈" 的使用和缺乏误差界。但我认为 R1 slightly overstates the issue：

1. 论文恰当地使用了 "Observation" 而非 "Theorem/Proposition"，这本身是对形式化程度的诚实标注。
2. 条件 (i) 的 degeneration 被量化为 |C*|/|C| ≤ 0.034（§5.1），不是纯粹的 "≈ 0"。
3. 条件 (ii) source-attribution scoring 是 SICA pipeline 的构造性定义（Eq. 3-4, §3.1），不是近似。

真正的问题在 R1 指出的 **presentation gap**：Abstract 说 "The failure is structural" 并引用 Observation 1，但 "structural" 这个词暗示了形式化证明的严谨性。建议作者在 Abstract 中使用 "empirically structural" 或 "systematic" 替代 "structural"，或在 Observation 1 后更明确地说明这是经验驱动的结构性发现，而非公理化推导。

---

### Should-Fix

**[AGREE] R1-W1**: Remark 1 (DPI) 理论贡献有限
完全同意，且与我自己的 W1 一致。DPI 是确定性后处理的教科书性质（Cover & Thomas, Ch. 2），"Information Ceiling" 这一命名暗示了特定理论发现（analogous to "information bottleneck"），但实际贡献是 *识别* SICA pipeline 实例化了这个 Markov chain，而非 DPI 本身。建议作者降低 Remark 1 的宣传力度，将重点放在 "identifying the Markov structure" 上，而非 "establishing a ceiling"。

**[AGREE] R1-W2**: Capability-gap 的 n=6 因果推断强度不足
同意，与我自己的 W4 互补。我的 W4 侧重于 capability-gap 仅在弱生成器上有效的实用价值局限，R1-W2 侧重于统计检验力不足。两个角度共同指向：cross-architecture escape 作为贡献三是有前景的方向，但目前证据不足以支撑强因果声明。Appendix C 的 CCR 分析虽然增加了 verifier-generator 组合数（8 种），但核心趋势仍依赖少数数据点。

**[REBUT] R1-W3**: 前沿模型未跑 full pipeline
R1 说 "Table 2 的 closed-source 分析仅限 BR 分析未跑 full pipeline"，这一描述不完全准确。Table 2（page 5）明确展示了 gpt-4.1 和 Gemini-2.5-Pro 在 FOLIO 上的 **完整 SICA pipeline 结果**：
- gpt-4.1: SC = 82.85%, SICA = 82.85%, Δ = 0.00
- Gemini-2.5-Pro: SC = 87.57%, SICA = 87.57% (Δ in BR column = 1.79 是 BR 值)

两个前沿模型的 SICA 均与 SC 完全一致，Δ = 0。所以 full pipeline *确实* 在前沿模型上运行了——至少在 FOLIO 上。R1 的合理关切是：(1) 前沿模型仅在 FOLIO (n=204) 上测试，未覆盖 ProofWriter/LogiQA；(2) FOLIO 本身规模较小。但 "未跑 full pipeline" 是事实性错误。

此外，Table 2 显示前沿模型的 BR 仍然 > 1（gpt-4.1: 1.66, Gemini-2.5-Pro: 1.79），虽然低于 7B 模型（Mistral-7B: 4.97），但 SCB 的存在不因模型规模而消失。这一证据支持了论文的泛化性声明。

**[AGREE] R1-W4**: BH FDR 阈值的预先指定问题
部分同意。论文在 §6（page 7, Figure 4 context）说明 "Decision boundaries (C₀ < 5%, K_eff ≤ 1.30, SC < 80%) were derived from Mistral-7B and Qwen2.5-14B"，并在 held-out 模型（LLaMA-3.1-8B, Qwen3-14B）上验证。这是一个 train/test split，mitigates post-hoc bias。但 training set 仅 2 个模型、test set 仅 2 个模型——样本量仍然很小。建议作者在 Appendix 中详细说明阈值选择的 cross-validation 过程，或报告阈值在不同切分下的稳定性。

---

### Minor

[AGREE] R1-M1: Figure 2 y 轴单位可以更清晰（我自己的 M2 也指出了散点图可读性问题）。
[AGREE] R1-M2: Table 1 脚注密度高，同意我自己的类似观察（M3 on Table 2）。
[AGREE] R1-M3: §2 中 Huang et al. 讨论偏长——但我的看法稍有不同：问题不是讨论太长，而是讨论方向偏了。§2 用大量篇幅解释 *差异*，但应该更多地论证 *本文独有的贡献*（见我的 N2）。
[AGREE] R1-M4: Appendix Z AI 辅助声明已确认（page 28），披露了 Claude (Anthropic) 的使用，涵盖代码、写作、文献三个方面。披露透明。

---

### Questions

**[AGREE] R1-Q1**: Table 10 "Random" baseline 的构造方式是一个合理的 clarification 请求。论文在 §H context（page 16）简要说明 "Random introduces random constraint-trace assignments while preserving the answer-distribution pairing"——即打乱 constraint-trace 对应关系但保持答案分布。这一信息存在于附录但不够显著，建议在正文 §5.1 提及。

**[AGREE] R1-Q2**: α=0.5 的选择依据。与我自己的 Q2 完全重合。论文在 §3.1 设定 α=0.5 作为 answer_assertion 权重，但未报告系统消融。Appendix L.2 有温度敏感性分析但缺少 α 消融。α→0 时 source-attribution scoring 的影响是否消失，是理解 Observation 1 条件 (ii) 必要性的关键实验——如果移除 answer_assertion 后 SCB 仍然存在，说明 source-attribution 不是唯一驱动因素。

**[AGREE] R1-Q3**: ProofWriter oracle 约束是否经过相同 Z3 dedup 流程。Appendix F（page 15-16）描述了 DSL→Z3 映射的完整流程，包括 Z3 satisfiability 检查。但是否经过与自提取约束完全相同的 deduplication pipeline（syntactic equivalence + global dedup ratio 46.0%）不完全清楚。如果 oracle 约束跳过了 dedup，则 oracle vs. self-extracted 的比较可能存在 confound。

**[AGREE] R1-Q4**: DeBERTa NLI 判断粒度。§6 说 "each NLI-supporting vote counts as times alongside SC's K votes"——这暗示 NLI 在 candidate answer 级别操作（每个候选答案获得一个 NLI 支持/反对票），但具体是对整个 trace 做 entailment 还是对单个 constraint 做 entailment 不够清晰。建议作者在 §6 或 Appendix 中澄清。

**[AGREE] R1-Q5**: 提取 trace 间 disagreement 而非 trace 内约束。这是一个有建设性的方向建议。当前 SICA 从每条 trace *独立* 提取约束，忽略了 trace 间的冲突信号。如果直接提取 "trace A 说 X，trace B 说 Y，它们在哪里矛盾"，可能产生更独立的信号。与我自己的 Q3（adversarial constraint generation）方向类似但不同——R1-Q5 是被动发现分歧，我的 Q3 是主动生成反事实。两个方向都值得作者讨论。

---

### Missing References

**[REBUT] PRM (Math-Shepherd)**: 论文已引用。Math-Shepherd (Wang et al., 2024) 出现在 page 11 参考文献列表中，§2 (page 3) 也在 "Training-based verification" 段落中讨论了 PRM 相关工作，包括 outcome and process reward models、dual preference optimization (She et al., 2025)、execution-based filtering (Li et al., 2022; Chen et al., 2023a)。R1 在此处的 "missing reference" 判断不准确。

**[AGREE] Weng et al. (2023) backward verification**: 同意这是一个相关但未深入对比的工作。Backward verification（从答案反推验证推理步骤）与 SICA 的 forward extraction（从推理提取约束验证答案）是互补方向。论文可以在 §2 简要讨论这一对比，说明为什么选择 forward extraction 路径。

---

### 整体评价一致性

R1 和我（R2）在以下方面高度一致：
1. **Overall 3.5 (Borderline Conference)** — 完全相同
2. **Soundness 4/5** — 完全相同
3. **Excitement 3/5** — 完全相同
4. **核心关切**：claim scope vs. evidence scope（R1-N1 ≈ 我的 W2），Observation 1 / Remark 1 的形式化与呈现差距（R1-N2/W1 ≈ 我的 N2/W1），α 消融缺失（R1-Q2 = 我的 Q2）

**主要分歧点**：R1-W3 关于前沿模型"未跑 full pipeline"——Table 2 证据表明 gpt-4.1 和 Gemini-2.5-Pro 确实在 FOLIO 上运行了完整 SICA pipeline（Δ = 0），R1 在此处有事实性错误。

**结论**：两位 reviewer 的评审意见高度一致，指向同一核心问题——新颖性定位需要更锐利（vs. Huang et al.），claim scope 需要缩窄以匹配证据，形式化呈现需要更审慎。论文的实验质量和诊断框架是明确的优势。3.5 (Borderline Conference) 的评分反映了 "excellent execution, moderate novelty" 的平衡。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2090 · 2026-05-23T19:22:06.461474+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 2091 · 2026-05-23T19:22:06.763189+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T19:06:03.013698+00:00\", \"completed_at\": \"2026-05-23T19:10:45.973383+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item（纯文本：Title/Abstract/Intro），第一个视觉锚点 Figure 1（SICA pipeline 流程图）出现在 page 2 顶部。在前 3 页内，符合预期。Figure 1 清晰传达核心方法流程，红色虚线框标注 verification variant，锚定效应正面。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title 较长（两行）但信息量明确，直接传达 negative finding。Abstract 排版整洁，长度适中（约 180-200 words），符合 EMNLP ≤200 words 约束。\\\"Anonymous ACL submission\\\" 标注正确。\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"布局节奏良好，无连续 2 页纯文本。Page 1（text）→ Page 2（Figure 1）→ Page 3（equations）→ Page 4（Figure 2）→ Page 5（Table 1）→ Page 6（Table 2 + Figure 3）→ Page 7（Figure 4）→ Page 8（Table 3 + Discussion + Limitations + References 开头）。Text-figure-table 三重奏交替均匀。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"最后一页（主文 page 8）内容填充完整，包含 Table 3、Discussion and Conclusion、Limitations、References 起始。页面利用率 >90%，无大面积空白。\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"主文 8 页包含 4 figures + 3 tables = 7 个 display items，密度 0.875/页。对实证为主的论文，处于 5-8 个的推荐范围内，密度适当。\"}, {\"severity\": \"info\", \"dimension\": \"pages 11-28\", \"message\": \"Appendix 18 页，包含 2 个 Algorithm 伪代码 + ~8 个 figures + ~30 个 tables，内容充实，体现实验彻底性。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（pipeline 流程图）：跨双栏全宽，箱体与箭头清晰，内部文字可读。红色虚线框标注 oracle variant 有效区分变体。Caption 自包含，说明了 SC → SICA → Z3 → MAX-SAT 的完整流程。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2（scatter plot）：单栏宽度，三种 Type（A/B/C）通过不同标记和色带区分。轴标签清晰（\\\"SC baseline accuracy (%)\\\" / \\\"SICA Δ\\\"）。对角虚线参考线辅助阅读。填充/空心标记区分样本量。颜色区分度可接受。\"}, {\"severity\": \"warning\", \"dimension\": \"page 4\", \"message\": \"Figure 2 的图例文字和标记（Type A/B/C 说明）在单栏宽度下偏小，打印时可能需要仔细辨认。建议适当放大 legend 字号或将 legend 移至图外
…[truncated 3017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2092 · 2026-05-23T19:22:06.813747+00:00_

called mcp__agent-ml-research__read_local_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_local_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2093 · 2026-05-23T19:22:06.814123+00:00_

&lt;tool_use_error>Error: No such tool available: mcp__agent-ml-research__read_local_file&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2094 · 2026-05-23T19:22:14.293439+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 2095 · 2026-05-23T19:22:14.394595+00:00_

1	# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
2	- id: "R1-C1"
3	  summary: "Method Stage 3 sat() implementation undescribed"
4	  category: method
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 1
8	  last_seen_round: 3
9	  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
10	  resolution_round: 3
11	
12	- id: "R1-C2"
13	  summary: "Most experiments underpowered (n≤60), no power analysis"
14	  category: experiment
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
20	  resolution_round: 3
21	
22	- id: "R1-C3"
23	  summary: "Oracle/upper-bound experiment missing"
24	  category: experiment
25	  severity: critical
26	  status: resolved
27	  first_raised_round: 1
28	  last_seen_round: 1
29	  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
30	  resolution_round: 3
31	
32	- id: "R1-C4"
33	  summary: "Huang et al. (ICLR 2024) not cited"
34	  category: framing
35	  severity: critical
36	  status: resolved
37	  first_raised_round: 1
38	  last_seen_round: 2
39	  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
40	  resolution_round: 2
41	
42	- id: "R1-C5"
43	  summary: "Critical related work missing"
44	  category: writing
45	  severity: critical
46	  status: resolved
47	  first_raised_round: 1
48	  last_seen_round: 1
49	  resolution: "~48 citations, 5 Related Work paragraphs."
50	  resolution_round: 3
51	
52	- id: "R1-C9"
53	  summary: "Capability trap novelty unclear"
54	  category: framing
55	  severity: critical
56	  status: resolved
57	  first_raised_round: 1
58	  last_seen_round: 3
59	  resolution: "Reframed as regime-dependent analysis with CJT framework."
60	  resolution_round: 3
61	
62	- id: "R3-N1"
63	  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
64	  category: method
65	  severity: critical

…[truncated 6862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2096 · 2026-05-23T19:22:22.726209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
  "offset": "300",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
    "offset": "300",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2097 · 2026-05-23T19:22:22.777459+00:00_

300	  first_raised_round: 10
301	  last_seen_round: 13
302	  resolution: "Renamed to Observation 1, conditions made explicit, empirical support section added."
303	  resolution_round: 14
304	
305	- id: "R11-N1"
306	  summary: "Spearman ρ=1.0 (n=6) 被过度使用"
307	  category: experiment
308	  severity: critical
309	  status: in_progress
310	  first_raised_round: 11
311	  last_seen_round: 19
312	  mentions:
313	    - round: 19
314	      reviewers: [1, 2]
315	      note: "与 R9-W3/R10-N3 同一问题群，R19 两位 reviewer 共识"
316	
317	- id: "R11-N2"
318	  summary: "中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强"
319	  category: framing
320	  severity: critical
321	  status: in_progress
322	  first_raised_round: 11
323	  last_seen_round: 19
324	  mentions:
325	    - round: 19
326	      reviewers: [1, 2]
327	      note: "R1-N2: 建议 Abstract 改为 'no evidence exceeding ~2pp'。R2 升级为 Must-Fix"
328	
329	- id: "R11-N3"
330	  summary: "TOST ±2pp margin 缺乏 principled 论证"
331	  category: experiment
332	  severity: warning
333	  status: in_progress
334	  first_raised_round: 11
335	  last_seen_round: 19
336	  mentions:
337	    - round: 19
338	      reviewers: [1]
339	      note: "R1-W2: 'pre-registered' 无注册凭证"
340	
341	- id: "R11-W1"
342	  summary: "DRC 评估不充分——仅PW完整"
343	  category: experiment
344	  severity: warning
345	  status: in_progress
346	  first_raised_round: 11
347	  last_seen_round: 18
348	  mentions:
349	    - round: 19
350	      reviewers: []
351	      note: "R19(fresh) 未单独提及"
352	
353	- id: "R11-W2"
354	  summary: "BR 指标存在循环论证倾向"
355	  category: method
356	  severity: critical
357	  status: in_progress
358	  first_raised_round: 11
359	  last_seen_round: 19
360	  mentions:
361	    - round: 19
362	      reviewers: [1, 2]
363	      note: "R1-W1: BR>1 是 source-attribution 的数学必然，permutation BR_excess≈0。R2 AGREE: BR 度量 degeneration 而非 independent bias signal"
364	
365	- id: "R11-W3"
366	  summary: "术语过度品牌化——'Symbolic Mirage' 偏 dramatic"
367	  category: writing
368	  severity: warning
369	  s
…[truncated 3672 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2098 · 2026-05-23T19:22:28.247671+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
  "offset": "498",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
    "offset": "498",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2099 · 2026-05-23T19:22:28.348701+00:00_

498	  summary: "SCB 命名过度——structural limitation 而非 bias"
499	  category: framing
500	  severity: warning
501	  status: in_progress
502	  first_raised_round: 13
503	  last_seen_round: 19
504	  mentions:
505	    - round: 19
506	      reviewers: [1, 2]
507	      note: "R1-W1 + R2-W4: 共识指向同一根本问题"
508	
509	- id: "R13-W2"
510	  summary: "BH 校正 m=16 包含非独立条件"
511	  category: experiment
512	  severity: warning
513	  status: in_progress
514	  first_raised_round: 13
515	  last_seen_round: 19
516	  mentions:
517	    - round: 19
518	      reviewers: [1]
519	      note: "R1-W3: seed aggregates 与 component seeds 重叠，应区分 confirmatory vs exploratory"
520	
521	- id: "R13-W3"
522	  summary: "Missing references: ensemble diversity 文献"
523	  category: writing
524	  severity: warning
525	  status: in_progress
526	  first_raised_round: 13
527	  last_seen_round: 19
528	  mentions:
529	    - round: 19
530	      reviewers: [1, 2]
531	      note: "与 R11-W7 同一 issue"
532	
533	- id: "R13-W4"
534	  summary: "论文密度过高，可读性受损"
535	  category: format
536	  severity: warning
537	  status: in_progress
538	  first_raised_round: 13
539	  last_seen_round: 19
540	  mentions:
541	    - round: 19
542	      reviewers: [2]
543	      note: "R2-W5: \enlargethispage{6\baselineskip} + 多处负 vspace，Section 7 仅 1/3 页"
544	
545	- id: "R14-N1"
546	  summary: "Cross-architecture escape 证据不足"
547	  category: experiment
548	  severity: critical
549	  status: in_progress
550	  first_raised_round: 14
551	  last_seen_round: 19
552	  mentions:
553	    - round: 19
554	      reviewers: [1, 2]
555	      note: "与 R9-W3 同一 issue 群"
556	
557	- id: "R14-N2"
558	  summary: "Underpowered negative claim"
559	  category: framing
560	  severity: critical
561	  status: in_progress
562	  first_raised_round: 14
563	  last_seen_round: 19
564	  mentions:
565	    - round: 19
566	      reviewers: [1, 2]
567	      note: "与 R11-N2 同一 issue"
568	
569	- id: "R14-W1"
570	  summary: "BR 循环论证"
571	  category: method
572	  severity: warning
573	  status: 
…[truncated 3299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2100 · 2026-05-23T19:23:57.620686+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission guidelines author instructions page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission guidelines author instructions page limit"
  }
}
```

</details>

---


### Tool result

_source line 2101 · 2026-05-23T19:24:04.649578+00:00_

Web search results for query: "EMNLP 2026 ARR submission guidelines author instructions page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Submission Checklist for Original, First Time Submissions | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/OriginalSubmissionChecklist"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 ARR submissions regarding page limits and author instructions:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

## Final Version Page Limits

Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Additional Important Guidelines

The standards expected by reviewers are those of a traditional direct submission as a long or short main conference paper to ACL (or the other major conferences operated by the ACL).

Authors will need to explicitly declare which conference they intend to commit to at subm
…[truncated 617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 7028
}
```

</details>

---


### Tool call

_source line 2102 · 2026-05-23T19:26:49.658477+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "symb_invariant_consensus",
  "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9+ recurring issues\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及，但 cross-architecture escape 整体 capability-gap 局限的共识间接涵盖\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2-W4: 两位 reviewer 一致。R1 指出 Spearman ρ=1.0 但 n=6 因果推断强度受限；R2 指出仅弱生成器(SC≤72%)上显著，实用价值局限\"\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 20\n  resolution: \"R20 视觉审查: Figure 1 出现在 page 2 顶部，布局节奏良好。无连续2页纯文本。\"\n  resolution_round: 20\n\n- id: \"R9-VL4\"\n  summary: \"Discussion/Conclusion 展开不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。视觉审查显示 page 8 内容填充完整(>90%利用率)，包含 Table 3 + Discussion + Limitations + References 起始\"\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一问题群。R1-W2: n=6 + 108 组合扩展覆盖面但核心趋势仍依赖少数点\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2-W4: 共识——仅弱生成器受益，强生成器(SC≥72%) Δ≤+0.83pp 甚至负向。cross-architecture escape 作为贡献有前景但证据不足\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。论文现已扩展到 multi-seed replication (Table 42)，并明确标注 underpowered conditions\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。论文现使用 'pre-specified' 而非 'pre-registered'\"\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。§2 现明确区分 specification-generation / program-generation / trace-extraction 三范式\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。§2 新增 'Distinction from CoT confirmation bias' 独立段落，明确区分 trace-level vs aggregation-level bias\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 20\n  resolution: \"R20 两位 reviewer 均认为 Related Work 覆盖良好(5段，~48引用)，未提出压缩问题\"\n  resolution_round: 20\n\n- id: \"R10-I1\"\n  summary: \"'Symbolic Mirage' 概念新颖性——与 Huang/Wan 的 confirmation bias 区别\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R2-N2: 'extends and formalizes' framing 弱化独立贡献。R1 REBUT: 实际贡献远超 confirmatory (formal pipeline + 27 strategies + escape + diagnostics)，问题在 framing 太谦虚\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: resolved\n  last_seen_round: 17\n  resolution: \"Figure 2, Figure 4 added in main text.\"\n  resolution_round: 17\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"95% bootstrap CIs added for BR.\"\n  resolution_round: 11\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"Renamed to Observation 1, conditions made explicit, empirical support section added.\"\n  resolution_round: 14\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"与 R9-W3/R10-N3 同一问题群，R20 两位 reviewer 共识\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R2-N1: 标题 'No Detectable Improvement' 与 cross-arch 正面结果存张力。R1 REBUT: 'Self-Extracted' 限定词已充分，建议降为 Should-Fix。R20 Director 判断: Should-Fix\"\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。论文现包含 permutation null model (BR_excess≈0, p>0.7)，明确标注 BR 度量 degeneration 而非 independent bias signal\"\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。Section 5 现标题为 'The Symbolic Mirage'，仍保留该命名\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R2-N2: 'extends and formalizes' 给人 confirmatory study 印象。R1 REBUT: 建议 frame 为 'reveals deeper structural mechanism that Huang's observation did not explain'\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及\"\n\n- id: \"R11-W7\"\n  summary: \"Ensemble diversity 文献缺失\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 20\n  resolution: \"Dietterich (2000), Krogh & Vedelsby (1994) 现已在 §2 和 §7 中引用和讨论\"\n  resolution_round: 20\n\n- id: \"R12-N1\"\n  summary: \"Capability-gap pattern 证据不足以支撑 top-level contribution\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群。两位 reviewer 共识: n=6 + capability-gap 仅弱生成器有效\"\n\n- id: \"R12-N2\"\n  summary: \"Underpowered tests 与 negative claim 之间存在 gap\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。论文现明确区分 confirmatory (m=6) vs exploratory conditions，并标注 'Absence of evidence is not evidence of absence for small effects'\"\n\n- id: \"R12-W1\"\n  summary: \"Cross-architecture escape 可能是 ensemble diversity\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。论文新增 cross-model voting vs cross-architecture NLI 对比(Table cross-model-ablation)——Mistral-7B cross voter degrades 3 generators, DeBERTa NLI 不退化任何 generator，区分了 ensemble diversity 和 structural independence\"\n\n- id: \"R12-W4\"\n  summary: \"Observation 1 条件验证不完整\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-N2: 三个条件均用 '≈' 且无误差界，Abstract 称 'structural' 但实为半形式化观察。R2 AGREE: 应使用 'empirically structural' 或 'systematic' 替代 'structural'\"\n\n- id: \"R12-EC1\"\n  summary: \"代码/数据可获取性声明缺失\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 20\n  resolution: \"Footnote 1 现已声明 'Code and data will be released upon acceptance.'\"\n  resolution_round: 20\n\n- id: \"R13-N2\"\n  summary: \"Novelty claim 相对 Huang et al. (2024) 的增量有限\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R2-N2(Must-Fix): 'extends and formalizes' 弱化独立贡献。R1(REBUT→Should-Fix): 实际贡献包括 formal pipeline + 27 strategies + escape + diagnostics，远超 confirmatory study。Director 判断: Should-Fix，framing 问题非实质性贡献缺失\"\n\n- id: \"R13-N3\"\n  summary: \"Abstract negative claim 过强\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"与 R11-N2 同一 issue。R20: Abstract 现称 'no detectable improvement exceeding ~2pp under self-extraction'，措辞已改善但 R2 仍指标题 scope 问题\"\n\n- id: \"R13-W1\"\n  summary: \"SCB 命名过度——structural limitation 而非 bias\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。论文现明确声明 'a structural property of self-extraction pipelines, not a cognitive bias analogy'\"\n\n- id: \"R13-W2\"\n  summary: \"BH 校正 m=16 包含非独立条件\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"R1-W4: m=6 选择标准(C₀<5%, K_eff≥1.30, SC<80%)是否预先确定未说明，可能存在后验偏差。但论文标注 train/test split (derived from Mistral-7B/Qwen2.5-14B, validated on LLaMA/Qwen3)\"\n\n- id: \"R13-W3\"\n  summary: \"Missing references: ensemble diversity 文献\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 20\n  resolution: \"与 R11-W7 同。Dietterich (2000), Krogh & Vedelsby (1994) 现已引用。\"\n  resolution_round: 20\n\n- id: \"R13-W4\"\n  summary: \"论文密度过高，可读性受损\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。视觉审查显示页面利用率>90%，text-figure-table 交替均匀，无大面积空白\"\n\n- id: \"R14-N1\"\n  summary: \"Cross-architecture escape 证据不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群\"\n\n- id: \"R14-N2\"\n  summary: \"Underpowered negative claim\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh): 论文现明确标注 power limitations，未被提为 Must-Fix\"\n\n- id: \"R14-W1\"\n  summary: \"BR 循环论证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。论文新增 permutation null model 回应\"\n\n- id: \"R14-W2\"\n  summary: \"Observation 1 条件 (iii) 未验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"与 R12-W4 同。R1-N2 指出条件(iii)仅以 '~5.7 constraints per trace' 概述，缺乏 per-answer-group 分布统计\"\n\n- id: \"R14-W3\"\n  summary: \"Novelty positioning vs Huang et al.\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"与 R13-N2 同一 issue\"\n\n- id: \"R14-W5\"\n  summary: \"'Pre-registered' 无注册凭证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 20\n  resolution: \"论文现使用 'pre-specified margin' 而非 'pre-registered'。\"\n  resolution_round: 20\n\n- id: \"R14-W6\"\n  summary: \"Missing references: OpenAI o1/o3\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 20\n  resolution: \"§2 现引用 'OpenAI o1/o3' 在 test-time compute 段落中\"\n  resolution_round: 20\n\n- id: \"R15-M3\"\n  summary: \"Abstract 词数超限\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 20\n  resolution: \"R20 R2 确认 Abstract ~196 词，符合 EMNLP 200 词限制。\"\n  resolution_round: 20\n\n- id: \"R15-M4\"\n  summary: \"代码/数据可获取性声明缺失\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 20\n  resolution: \"与 R12-EC1 同。Footnote 1 现已声明。\"\n  resolution_round: 20\n\n- id: \"R15-W1\"\n  summary: \"Turpin et al. 引用年份错误\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。待确认论文中 Turpin et al. 当前标注年份\"\n\n- id: \"R16-N1\"\n  summary: \"Cross-architecture escape 过度声明\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群\"\n\n- id: \"R16-N2\"\n  summary: \"Underpowered negative claim\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh): 与 R14-N2 同\"\n\n# Round 20 new issues\n\n- id: \"R20-N1\"\n  summary: \"Oracle 实验仅限形式逻辑领域(FOLIO+PW)，核心因果主张外部效度不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-N1(Must-Fix) + R2 AGREE: oracle 实验仅在形式逻辑数据集上进行(FOLIO gold FOL, ProofWriter DSL→Z3)，对 GSM8K/StrategyQA 等域的聚合机制 soundness 无直接因果证据。替代假说 'MAX-SAT 对数学约束天然不适用' 未排除。\"\n  action_items:\n    - round: 20\n      action: \"在 Limitations 中明确 oracle 因果推断的域局限性；或在 GSM8K 上构建 partial oracle\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R20-N2\"\n  summary: \"Observation 1 形式化程度与 Abstract/Intro 'structural' 呈现不匹配\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-N2(Must-Fix→Director降为Should-Fix): 三个条件用 '≈' 无误差界，Abstract 称 'structural' 但实为半形式化经验观察。R2 AGREE 但指出论文恰当使用 'Observation' 而非 'Theorem'，条件(i) |C*|/|C|≤0.034 有量化。建议: Abstract 用 'empirically structural' 替代 'structural'\"\n  action_items:\n    - round: 20\n      action: \"Abstract/Intro 中 'structural' 措辞改为 'empirically structural' 或 'systematic'；或在 Appendix 提供带误差界的定理版本\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R20-W1\"\n  summary: \"Remark 1 (DPI bound) 理论贡献有限——教科书性质非 SICA 特有\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W1: 共识。DPI 是确定性后处理的一般性质(Cover & Thomas Ch.2)，'Information Ceiling' 命名暗示特定理论发现但实际贡献是识别 M→T→A→C Markov chain 结构。建议降低展示权重或补充 tightness 量化\"\n\n- id: \"R20-W2\"\n  summary: \"BH FDR m=6 confirmatory conditions 选择标准的预先指定问题\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"R1-W4: 阈值(C₀<5%, K_eff≥1.30, SC<80%)是否预先确定未说明。论文有 train/test split(derived from Mistral-7B/Qwen2.5-14B, validated on LLaMA/Qwen3)，但样本量极小(train 2, test 2)\"\n\n- id: \"R20-W3\"\n  summary: \"27 training-free variants 的穷举性——真正独立方法类别约 4-5 种\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R2-W3 + R1 partial AGREE: 许多 'variants' 为同一方法的参数调整。R1 纠正: iterative refinement 未遗漏(Table 14 #3/#22)。R1 补充更大遗漏: fine-tuned constraint extractors 未测试\"\n\n- id: \"R20-Q1\"\n  summary: \"α 系统消融缺失——α→0 时 source-attribution 影响是否消失\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-Q2 + R2-Q2 完全重合: Table 11 显示 MAX-SAT vs count-only agreement ≥99% across α∈[0.1,0.9]，但这是 count-only 替换而非移除 answer_assertion。α 系统消融(特别是 α→0 完全依赖 Z3 满足性权重)未单独报告\"\n\n- id: \"R20-Q2\"\n  summary: \"Source-attribution vs semantic scoring ablation 缺失\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R2-Q1 + R1 AGREE: Observation 1 在 source-attribution scoring 下成立，但替换为语义相似度评分后是否仍退化？BR分析间接支持(约束内容语义追随多数答案)，但缺直接实验验证\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9+ recurring issues\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及，但 cross-architecture escape 整体 capability-gap 局限的共识间接涵盖\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2-W4: 两位 reviewer 一致。R1 指出 Spearman ρ=1.0 但 n=6 因果推断强度受限；R2 指出仅弱生成器(SC≤72%)上显著，实用价值局限\"\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 20\n  resolution: \"R20 视觉审查: Figure 1 出现在 page 2 顶部，布局节奏良好。无连续2页纯文本。\"\n  resolution_round: 20\n\n- id: \"R9-VL4\"\n  summary: \"Discussion/Conclusion 展开不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。视觉审查显示 page 8 内容填充完整(>90%利用率)，包含 Table 3 + Discussion + Limitations + References 起始\"\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一问题群。R1-W2: n=6 + 108 组合扩展覆盖面但核心趋势仍依赖少数点\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2-W4: 共识——仅弱生成器受益，强生成器(SC≥72%) Δ≤+0.83pp 甚至负向。cross-architecture escape 作为贡献有前景但证据不足\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。论文现已扩展到 multi-seed replication (Table 42)，并明确标注 underpowered conditions\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。论文现使用 'pre-specified' 而非 'pre-registered'\"\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。§2 现明确区分 specification-generation / program-generation / trace-extraction 三范式\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。§2 新增 'Distinction from CoT confirmation bias' 独立段落，明确区分 trace-level vs aggregation-level bias\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 20\n  resolution: \"R20 两位 reviewer 均认为 Related Work 覆盖良好(5段，~48引用)，未提出压缩问题\"\n  resolution_round: 20\n\n- id: \"R10-I1\"\n  summary: \"'Symbolic Mirage' 概念新颖性——与 Huang/Wan 的 confirmation bias 区别\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R2-N2: 'extends and formalizes' framing 弱化独立贡献。R1 REBUT: 实际贡献远超 confirmatory (formal pipeline + 27 strategies + escape + diagnostics)，问题在 framing 太谦虚\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: resolved\n  last_seen_round: 17\n  resolution: \"Figure 2, Figure 4 added in main text.\"\n  resolution_round: 17\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"95% bootstrap CIs added for BR.\"\n  resolution_round: 11\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"Renamed to Observation 1, conditions made explicit, empirical support section added.\"\n  resolution_round: 14\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"与 R9-W3/R10-N3 同一问题群，R20 两位 reviewer 共识\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R2-N1: 标题 'No Detectable Improvement' 与 cross-arch 正面结果存张力。R1 REBUT: 'Self-Extracted' 限定词已充分，建议降为 Should-Fix。R20 Director 判断: Should-Fix\"\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。论文现包含 permutation null model (BR_excess≈0, p>0.7)，明确标注 BR 度量 degeneration 而非 independent bias signal\"\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。Section 5 现标题为 'The Symbolic Mirage'，仍保留该命名\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R2-N2: 'extends and formalizes' 给人 confirmatory study 印象。R1 REBUT: 建议 frame 为 'reveals deeper structural mechanism that Huang's observation did not explain'\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及\"\n\n- id: \"R11-W7\"\n  summary: \"Ensemble diversity 文献缺失\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 20\n  resolution: \"Dietterich (2000), Krogh & Vedelsby (1994) 现已在 §2 和 §7 中引用和讨论\"\n  resolution_round: 20\n\n- id: \"R12-N1\"\n  summary: \"Capability-gap pattern 证据不足以支撑 top-level contribution\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群。两位 reviewer 共识: n=6 + capability-gap 仅弱生成器有效\"\n\n- id: \"R12-N2\"\n  summary: \"Underpowered tests 与 negative claim 之间存在 gap\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。论文现明确区分 confirmatory (m=6) vs exploratory conditions，并标注 'Absence of evidence is not evidence of absence for small effects'\"\n\n- id: \"R12-W1\"\n  summary: \"Cross-architecture escape 可能是 ensemble diversity\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。论文新增 cross-model voting vs cross-architecture NLI 对比(Table cross-model-ablation)——Mistral-7B cross voter degrades 3 generators, DeBERTa NLI 不退化任何 generator，区分了 ensemble diversity 和 structural independence\"\n\n- id: \"R12-W4\"\n  summary: \"Observation 1 条件验证不完整\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-N2: 三个条件均用 '≈' 且无误差界，Abstract 称 'structural' 但实为半形式化观察。R2 AGREE: 应使用 'empirically structural' 或 'systematic' 替代 'structural'\"\n\n- id: \"R12-EC1\"\n  summary: \"代码/数据可获取性声明缺失\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 20\n  resolution: \"Footnote 1 现已声明 'Code and data will be released upon acceptance.'\"\n  resolution_round: 20\n\n- id: \"R13-N2\"\n  summary: \"Novelty claim 相对 Huang et al. (2024) 的增量有限\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R2-N2(Must-Fix): 'extends and formalizes' 弱化独立贡献。R1(REBUT→Should-Fix): 实际贡献包括 formal pipeline + 27 strategies + escape + diagnostics，远超 confirmatory study。Director 判断: Should-Fix，framing 问题非实质性贡献缺失\"\n\n- id: \"R13-N3\"\n  summary: \"Abstract negative claim 过强\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"与 R11-N2 同一 issue。R20: Abstract 现称 'no detectable improvement exceeding ~2pp under self-extraction'，措辞已改善但 R2 仍指标题 scope 问题\"\n\n- id: \"R13-W1\"\n  summary: \"SCB 命名过度——structural limitation 而非 bias\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。论文现明确声明 'a structural property of self-extraction pipelines, not a cognitive bias analogy'\"\n\n- id: \"R13-W2\"\n  summary: \"BH 校正 m=16 包含非独立条件\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"R1-W4: m=6 选择标准(C₀<5%, K_eff≥1.30, SC<80%)是否预先确定未说明，可能存在后验偏差。但论文标注 train/test split (derived from Mistral-7B/Qwen2.5-14B, validated on LLaMA/Qwen3)\"\n\n- id: \"R13-W3\"\n  summary: \"Missing references: ensemble diversity 文献\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 20\n  resolution: \"与 R11-W7 同。Dietterich (2000), Krogh & Vedelsby (1994) 现已引用。\"\n  resolution_round: 20\n\n- id: \"R13-W4\"\n  summary: \"论文密度过高，可读性受损\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。视觉审查显示页面利用率>90%，text-figure-table 交替均匀，无大面积空白\"\n\n- id: \"R14-N1\"\n  summary: \"Cross-architecture escape 证据不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群\"\n\n- id: \"R14-N2\"\n  summary: \"Underpowered negative claim\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh): 论文现明确标注 power limitations，未被提为 Must-Fix\"\n\n- id: \"R14-W1\"\n  summary: \"BR 循环论证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。论文新增 permutation null model 回应\"\n\n- id: \"R14-W2\"\n  summary: \"Observation 1 条件 (iii) 未验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"与 R12-W4 同。R1-N2 指出条件(iii)仅以 '~5.7 constraints per trace' 概述，缺乏 per-answer-group 分布统计\"\n\n- id: \"R14-W3\"\n  summary: \"Novelty positioning vs Huang et al.\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"与 R13-N2 同一 issue\"\n\n- id: \"R14-W5\"\n  summary: \"'Pre-registered' 无注册凭证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 20\n  resolution: \"论文现使用 'pre-specified margin' 而非 'pre-registered'。\"\n  resolution_round: 20\n\n- id: \"R14-W6\"\n  summary: \"Missing references: OpenAI o1/o3\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 20\n  resolution: \"§2 现引用 'OpenAI o1/o3' 在 test-time compute 段落中\"\n  resolution_round: 20\n\n- id: \"R15-M3\"\n  summary: \"Abstract 词数超限\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 20\n  resolution: \"R20 R2 确认 Abstract ~196 词，符合 EMNLP 200 词限制。\"\n  resolution_round: 20\n\n- id: \"R15-M4\"\n  summary: \"代码/数据可获取性声明缺失\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 20\n  resolution: \"与 R12-EC1 同。Footnote 1 现已声明。\"\n  resolution_round: 20\n\n- id: \"R15-W1\"\n  summary: \"Turpin et al. 引用年份错误\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及。待确认论文中 Turpin et al. 当前标注年份\"\n\n- id: \"R16-N1\"\n  summary: \"Cross-architecture escape 过度声明\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群\"\n\n- id: \"R16-N2\"\n  summary: \"Underpowered negative claim\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh): 与 R14-N2 同\"\n\n# Round 20 new issues\n\n- id: \"R20-N1\"\n  summary: \"Oracle 实验仅限形式逻辑领域(FOLIO+PW)，核心因果主张外部效度不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-N1(Must-Fix) + R2 AGREE: oracle 实验仅在形式逻辑数据集上进行(FOLIO gold FOL, ProofWriter DSL→Z3)，对 GSM8K/StrategyQA 等域的聚合机制 soundness 无直接因果证据。替代假说 'MAX-SAT 对数学约束天然不适用' 未排除。\"\n  action_items:\n    - round: 20\n      action: \"在 Limitations 中明确 oracle 因果推断的域局限性；或在 GSM8K 上构建 partial oracle\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R20-N2\"\n  summary: \"Observation 1 形式化程度与 Abstract/Intro 'structural' 呈现不匹配\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-N2(Must-Fix→Director降为Should-Fix): 三个条件用 '≈' 无误差界，Abstract 称 'structural' 但实为半形式化经验观察。R2 AGREE 但指出论文恰当使用 'Observation' 而非 'Theorem'，条件(i) |C*|/|C|≤0.034 有量化。建议: Abstract 用 'empirically structural' 替代 'structural'\"\n  action_items:\n    - round: 20\n      action: \"Abstract/Intro 中 'structural' 措辞改为 'empirically structural' 或 'systematic'；或在 Appendix 提供带误差界的定理版本\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R20-W1\"\n  summary: \"Remark 1 (DPI bound) 理论贡献有限——教科书性质非 SICA 特有\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W1: 共识。DPI 是确定性后处理的一般性质(Cover & Thomas Ch.2)，'Information Ceiling' 命名暗示特定理论发现但实际贡献是识别 M→T→A→C Markov chain 结构。建议降低展示权重或补充 tightness 量化\"\n\n- id: \"R20-W2\"\n  summary: \"BH FDR m=6 confirmatory conditions 选择标准的预先指定问题\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"R1-W4: 阈值(C₀<5%, K_eff≥1.30, SC<80%)是否预先确定未说明。论文有 train/test split(derived from Mistral-7B/Qwen2.5-14B, validated on LLaMA/Qwen3)，但样本量极小(train 2, test 2)\"\n\n- id: \"R20-W3\"\n  summary: \"27 training-free variants 的穷举性——真正独立方法类别约 4-5 种\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R2-W3 + R1 partial AGREE: 许多 'variants' 为同一方法的参数调整。R1 纠正: iterative refinement 未遗漏(Table 14 #3/#22)。R1 补充更大遗漏: fine-tuned constraint extractors 未测试\"\n\n- id: \"R20-Q1\"\n  summary: \"α 系统消融缺失——α→0 时 source-attribution 影响是否消失\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-Q2 + R2-Q2 完全重合: Table 11 显示 MAX-SAT vs count-only agreement ≥99% across α∈[0.1,0.9]，但这是 count-only 替换而非移除 answer_assertion。α 系统消融(特别是 α→0 完全依赖 Z3 满足性权重)未单独报告\"\n\n- id: \"R20-Q2\"\n  summary: \"Source-attribution vs semantic scoring ablation 缺失\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R2-Q1 + R1 AGREE: Observation 1 在 source-attribution scoring 下成立，但替换为语义相似度评分后是否仍退化？BR分析间接支持(约束内容语义追随多数答案)，但缺直接实验验证\"\n"
  }
}
```

</details>

---


### Tool result

_source line 2103 · 2026-05-23T19:26:49.709571+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml\", \"bytes\": 20498}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2104 · 2026-05-23T19:29:36.894224+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "\n# 审稿报告：Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning\n\n**目标 venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**审稿轮次**: Round 20（fresh 重新审稿）\n**Reviewer 编排**: R1（方法严谨性+实验有效性）、R2（新颖性+完整性+写作质量）\n**交叉分享**: 完成，两位 Reviewer 均提交逐条 [AGREE]/[REBUT] 回应\n**格式检查**: 正文 8 页 ✓ | ACL review 模板 ✓ | Anonymous ✓ | Abstract ~196 词 ✓ | Limitations 在正文 ✓\n\n---\n\n## Summary\n\n本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought 轨迹中自提取逻辑约束，经 Z3 weighted partial MAX-SAT 聚合答案。核心发现为负面结果：在 6 个模型（7B-32B）、多个推理领域上，SICA 与 Self-Consistency 在 >90% 问题上答案一致，经 BH FDR 校正后无统计显著正向效应。作者将此诊断为 \"symbolic confirmation bias\"（SCB）——自提取约束系统性追随多数答案（bias ratio 1.66-4.97×，9 models from 7B to frontier）。Observation 1（Argmax Preservation）和 Remark 1（DPI Information Ceiling）提供结构性解释。27 种 training-free 变体均因 independence-accuracy trade-off 失败。Cross-architecture verification（DeBERTa NLI）仅在弱生成器上显著（+6.67 pp, p<0.001）。三个零成本诊断指标（C₀, K_eff, BR）预判失败模式。\n\n---\n\n## Strengths\n\n**S1. 统计方法论严谨性远超同类负面结果论文 [R1, R2 共识]**\nMcNemar exact test + 10,000 bootstrap CI + BH FDR correction (m=6 confirmatory) + TOST equivalence (±2pp) + power analysis (MDE) + multi-seed replication (3-5 seeds)。区分了 \"no effect detected\" 和 \"equivalence confirmed\"，在 NLP 负面结果论文中极为罕见。（§3.2, §4, Table 1, Appendix D-E）\n\n**S2. 失败机制诊断逻辑自洽 [R1, R2 共识]**\nSCB 诊断链条完整：BR > 1 → degeneration (|C\\|/|C| ≈ 0.034) → argmax preservation → 803/804 agreement (Table 10)。DAG 因果图（Figure 3）直观展示信息瓶颈。Constraint ablation（MAX-SAT vs count-only vs random-weight）令人信服地证明约束未携带超越投票计数的信号。\n\n**S3. 结构性解释超越纯经验观察 [R2 主要, R1 同意]**\nObservation 1 + Remark 1 将\"self-extraction doesn't work\"从经验发现提升为结构性解释——在 self-extraction 范式内，约束无法携带超越 trace 本身的信息。这是对 Huang et al. (2024) 的实质推进：解释了*为什么*即使在 provably sound solver (Z3) 下仍然失败。\n\n**S4. 27 种 remediation 策略的系统性失败 [R1, R2 共识]**\nFigure 4 + Table 14 覆盖 prompt-level (9)、method-level (3)、analytical conditions (17)，跨 diverse prompting、iterative refinement、contrastive scoring、atom pipeline、UNSAT filtering 等方向。有力地证明退化是结构性的而非调参问题。\n\n**S5. 诊断框架可操作性强 [R1, R2 共识]**\nC₀（multi-candidate rate）、K_eff（effective ensemble size）、BR（bias ratio）三指标零成本可计算（无需 ground truth），Type A/B/C 分类正确预测所有 60 个测试条件的失败模式。为从业者提供 K=12 pilot run 即可判断的 \"try before deploy\" 工具。（§5.3, Table 5）\n\n**S6. Cross-architecture escape 提供建设性方向 [R1, R2 共识]**\nDeBERTa NLI 在 Mistral-7B 上 +6.67 pp (p<0.001)，且 cross-model voting vs cross-architecture NLI 对比（Table cross-model-ablation）区分了 ensemble diversity 和 structural independence。CCR 指标（Appendix C）和 108 种 verifier-generator 组合提供量化框架。\n\n**S7. 写作质量整体良好 [R2 主要, R1 同意]**\n叙事从 \"symbolic verification should help\" → \"it doesn't\" → \"here's why structurally\" → \"here's how to diagnose/escape\" 连贯。Abstract ~196 词符合 EMNLP 限制。Related Work 5 段分类合理（SC/ensemble + neuro-symbolic + CoT bias distinction + test-time compute + training-based）。Limitations 简洁覆盖主要局限。\n\n---\n\n## Weaknesses\n\n### Must-Fix（1 项，Director 综合判定）\n\n**W1. Oracle 实验仅限形式逻辑领域，核心因果主张的外部效度不足 [R1-N1 Must-Fix, R2 AGREE]**\n- Oracle control（用 gold DSL/FOL 标注替换自提取约束）仅在 FOLIO 和 ProofWriter 上进行，均为形式逻辑领域。核心因果推断——\"瓶颈在自提取质量而非聚合机制本身\"——的直接证据领域受限。\n- 替代假说未排除：MAX-SAT 对数学推理或常识推理的约束类型可能天然不适用。\n- ProofWriter oracle 的 97.14% accuracy 证明了聚合机制在给定好约束时有效，但仅限形式逻辑。\n- Section 1 贡献声明暗示跨域通用性，但 oracle 证据不支撑。\n- **建议**：(a) Limitations 中明确 oracle 因果推断的域局限性；(b) 论证逻辑推理是 SCB 的 \"best-case\" domain（constraint formalization 最自然），因此 negative result 具有下界意义；(c) 或在 GSM8K 上构建 partial oracle。\n\n### Should-Fix（6 项）\n\n**W2. Observation 1 的形式化程度与 Abstract/Intro 呈现不匹配 [R1-N2 Must-Fix→Director 降为 Should-Fix, R2 AGREE]**\n- 三个退化条件均使用 \"≈\" 且无误差界。Abstract 称 \"The failure is structural (Observation 1)\"——\"structural\" 暗示形式化证明但实际是半形式化经验观察。\n- R2 指出论文恰当使用 \"Observation\" 而非 \"Theorem\"，条件(i) |C\\|/|C| ≤ 0.034 有量化。Director 同意 R2 评估，将此降为 Should-Fix。\n- **建议**：Abstract/Intro 使用 \"empirically structural\" 或 \"systematic\" 替代 \"structural\"。\n\n**W3. 新颖性相对于 Huang et al. (2024) 的差异化论述需更锐利 [R2-N2 Must-Fix→Director 降为 Should-Fix, R1 REBUT]**\n- 论文多次使用 \"extends and formalizes\" Huang et al.，给人 \"confirmatory study\" 印象。\n- R1 反驳：论文实际贡献远超 confirmation——完整 formal pipeline (Z3 MAX-SAT) + 27 strategies + escape + diagnostics，Huang et al. 完全没有。问题在 framing 太谦虚而非贡献不足。\n- Director 判断：同意 R1。论文实质贡献独立且充分。建议 frame 为 \"reveals a deeper structural mechanism that Huang's empirical observation did not explain\"，而非 \"extends and formalizes\"。\n\n**W4. 标题 \"No Detectable Improvement\" 的 scope 与 cross-architecture 正面结果存在张力 [R2-N1 Must-Fix→Director 降为 Should-Fix, R1 REBUT]**\n- R2 担忧读者可能理解为 \"symbolic constraints don't help LLM reasoning\"。\n- R1 反驳：标题限定词 \"Self-Extracted Constraints\" 已充分区分——cross-architecture escape 的增益来源是外部验证器的独立信号，不是自提取约束。\n- Director 判断：同意 R1，标题在技术上精确。但建议在 Abstract 中更早区分 self-extracted vs cross-architecture，减少误读风险。\n\n**W5. Capability-gap pattern 证据基础薄弱 [R1-W2 + R2-W4 共识]**\n- 核心单调性主张依赖 n=6 generator-verifier 配对（Spearman ρ=1.0, p=0.003）。\n- 108 种 verifier-generator-weight 组合（Figure 8）扩展覆盖面，但核心趋势仍受限。\n- 仅弱生成器（SC ≤ 72%）上显著，强生成器 Δ ≤ +0.83 pp 甚至负向。实用价值局限。\n- **建议**：增加更多能力梯度生成器，或明确标注为 \"preliminary evidence\"。\n\n**W6. Remark 1 (DPI bound) 理论贡献有限 [R1-W1 + R2-W1 共识]**\n- DPI（I(f(X);Y) ≤ I(X;Y)）是确定性后处理的教科书性质，非 SICA 特有。\n- \"Information Ceiling\" 命名暗示特定理论发现，但实际贡献是识别 M→T→A→C Markov chain 结构。\n- **建议**：降低展示权重，将重点放在 \"identifying the Markov structure\" 上。\n\n**W7. α 系统消融缺失 [R1-Q2 + R2-Q2 共识]**\n- Table 11 显示 MAX-SAT vs count-only agreement ≥99% across α ∈ [0.1, 0.9]，但这是 count-only 替换而非移除 answer_assertion。\n- α→0 时（完全依赖 Z3 可满足性权重，不用 source-attribution）退化是否减弱？这直接关系到 Observation 1 条件(ii) source-attribution 的必要性。\n- **建议**：在 Appendix 中报告 α 的完整消融，特别是 α=0 条件。\n\n### Minor（6 项）\n\n- M1. \"pp\"（percentage points）未在首次使用时定义 [R2-M1]\n- M2. Figure 2 散点图灰度打印可读性可改善（marker shape 差异不足）[R1-M1, R2-M2]\n- M3. Figure 4 策略名称文字较密集，部分长文本打印时约 6-7pt [视觉审查 warning]\n- M4. Figure 4 四个 category 灰度打印时颜色区分不足 [视觉审查 warning]\n- M5. Table 1 脚注符号密度较高（*,†,◦,●），可考虑简化 [R1-M2]\n- M6. 匿名 repo 建议——对负面结果论文的复现尤其重要 [R2-M5]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下关键问题两位 Reviewer 达成共识：\n1. **Oracle 领域覆盖不足**是核心缺陷（R1-N1 ≈ R2-W2 底层关切）\n2. **Observation 1 形式化与呈现差距**需要调整措辞（R1-N2, R2 AGREE with nuance）\n3. **DPI (Remark 1) 贡献有限**——教科书性质而非特有洞见（R1-W1 = R2-W1）\n4. **Capability-gap 证据薄弱** (n=6) + 实用价值局限（仅弱生成器受益）（R1-W2 ≈ R2-W4）\n5. **α 消融缺失**——理解 Observation 1 条件(ii) 必要性的关键实验（R1-Q2 = R2-Q2）\n6. **统计方法论优秀**——McNemar/TOST/bootstrap/FDR/power analysis 组合在同类论文中罕见（R1-S1 = R2-S1）\n7. **诊断框架实用**——C₀/K_eff/BR 零成本指标对从业者立即可部署（R1-S5 = R2-S4）\n8. **Overall 3.5/5 完全一致**\n\n## Reviewer Divergence [REBUT]\n\n以下问题存在分歧，由 Director 做出最终判定：\n\n1. **标题 scope（R2-N1）**：R2 列为 Must-Fix，R1 REBUT（\"Self-Extracted\" 限定词已足够精确）。**Director 判定**：同意 R1，降为 Should-Fix。标题在技术上精确，但建议在 Abstract 中更早区分 self-extracted vs cross-architecture 以减少误读。\n\n2. **新颖性 vs Huang et al.（R2-N2）**：R2 列为 Must-Fix（\"extends and formalizes\" 弱化贡献），R1 REBUT（贡献远超 confirmatory：formal pipeline + 27 strategies + escape + diagnostics）。**Director 判定**：同意 R1，降为 Should-Fix。实质性贡献充分，framing 调整即可（\"reveals structural mechanism\" 而非 \"extends\"）。\n\n3. **前沿模型 full pipeline（R1-W3）**：R1 称前沿模型\"未跑 full pipeline\"，R2 REBUT（Table 2 显示 gpt-4.1/Gemini-2.5-Pro 在 FOLIO 上运行了完整 SICA pipeline，Δ=0）。**Director 判定**：R2 事实性纠正成立。前沿模型确实跑了 full pipeline（至少在 FOLIO 上），R1 此处有事实错误。合理关切是前沿模型仅在 FOLIO (n=204) 上测试。\n\n4. **数据集范围（R2-W2）**：R2 声称\"所有数据集均为形式/逻辑推理\"，R1 REBUT（论文包含 GSM8K, AIME, StrategyQA, ARC-Challenge）。**Director 判定**：R1 事实性纠正成立——论文确实包含非逻辑领域数据集，但 confirmatory 分析集中于逻辑领域。底层关切有效但 R2 表述有误。\n\n---\n\n## Questions\n\n**Q1 [R1, R2 共识]**: α=0.5 的选择依据？α 取极端值（0 或 1）时退化程度如何变化？特别是 α→0（完全依赖 Z3 满足性权重，不用 source-attribution）时，SCB 是否减弱？\n\n**Q2 [R2 提出, R1 AGREE]**: 若不用 source-attribution scoring 而用语义相似度评分，Observation 1 是否仍然成立？Source-attribution scoring 是 degeneration 的充分条件还是必要条件？\n\n**Q3 [R1]**: ProofWriter oracle 约束是否经过与自提取约束相同的 Z3 dedup 流程？若未经 dedup，oracle vs. self-extraction 比较可能受 dedup 策略差异混淆。\n\n**Q4 [R1, R2 共识]**: DeBERTa NLI 判断的粒度——constraint 级别还是 trace 级别？这对理解 DeBERTa 如何打破 confirmation bias 至关重要。\n\n**Q5 [R2]**: 是否尝试过 adversarial constraint generation——显式要求模型生成与当前多数答案矛盾的约束？这与 diverse prompting 不同，是显式鼓励反事实推理。\n\n**Q6 [R1]**: 是否考虑过提取 trace 间 disagreement 而非 trace 内约束？若约束捕获 \"trace A 与 trace B 在 X 上不一致\"，source-attribution coupling 可能被打破。\n\n---\n\n## Missing References\n\n论文整体引用覆盖良好（~48 citations, 5 Related Work 段落）。以下为可选补充：\n\n- **[Optional]** Weng et al. (2023) \"Large Language Models are Better Reasoners with Self-Verification\" — backward verification 方法与 SICA forward extraction 的对比可在 §2 简要讨论\n- R2 建议的 \"Li et al. (AAAI 2026) Survey on LLM Symbolic Reasoning\" 无法验证真实性（R1 REBUT），不列为推荐引用\n\n**已在论文中引用的关键工作**：Huang et al. (ICLR 2024) ✓, Stechly et al. ✓ (implicitly via Wan et al. 2025 positioning), SatLM ✓, Math-Shepherd ✓, o1/o3 ✓, Dietterich (2000) ✓, Krogh & Vedelsby (1994) ✓\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置。项目 config 中无 `external_review.paperreview_ai.enabled` 设置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 3 warning, 26 info）。\n\n**Warnings**:\n1. Figure 2 图例文字和标记在单栏宽度下偏小，打印时可能需仔细辨认\n2. Figure 4 策略名称 y 轴标签较密集，部分长文本约 6-7pt\n3. Figure 4 四个 category 仅靠颜色区分时灰度打印可能难以辨认\n\n**Positive findings**:\n- 布局节奏良好：text-figure-table 交替均匀，无连续 2 页纯文本\n- 主文 8 页含 4 figures + 3 tables = 7 display items，密度 0.875/页（推荐范围内）\n- 所有 figure/table 在首次引用附近出现，无明显 float 漂移\n- Page 8 内容填充完整（>90% 利用率），无大面积空白\n- 公式渲染正确，编号连续，无 LaTeX 残留错误\n- Appendix 18 页（2 Algorithms + ~8 figures + ~30 tables），内容充实\n\n---\n\n## Overall Assessment\n\n**Overall Score**: 3.5 / 5（Borderline Conference）\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 4/5 | 统计方法论扎实，实验覆盖全面。Observation 1 成立且有经验支持，但形式化程度为半形式化观察。Oracle 因果推断领域受限 |\n| Excitement | 3/5 | 重要负面结果（关闭 self-extraction + formal verification 路径），诊断框架实用。但核心 insight 在概念上被 Huang et al. 部分预期，constructive contribution 仅限弱生成器 |\n| Reproducibility | 4/5 | 超参数完整报告，Appendix A 完整 prompt templates，Algorithm 1-2 伪代码清晰，代码承诺接收后发布 |\n| Confidence | 4/5 | 两位 Reviewer 均对 SC、formal verification、LLM reasoning 文献熟悉，仔细阅读全文 28 页 |\n\n**总评**：\n\n这是一篇实验方法论极为严谨的负面结果论文。核心优势在于：(1) 统计论证链的完整性（McNemar + Bootstrap CI + TOST + FDR + Power Analysis）在同类工作中罕见；(2) SCB 的诊断链条逻辑自洽（BR → degeneration → argmax preservation → constraint ablation 803/804 agreement）；(3) 诊断框架（C₀, K_eff, BR）对从业者有直接实用价值。\n\n主要问题：(1) Oracle 因果推断仅限形式逻辑领域，无法排除 MAX-SAT 对其他推理类型天然不适用的替代假说；(2) Observation 1 的 \"structural\" 呈现超出其半形式化观察的形式化程度；(3) 新颖性 framing（\"extends and formalizes\" Huang et al.）低估了论文的独立贡献；(4) Cross-architecture escape 的 capability-gap 依赖限制了其一般性。\n\n**建议处理优先级**：\n1. [Must-Fix] W1: Oracle 因果推断的域局限性——在 Limitations 中明确标注，或补充非逻辑域 oracle\n2. [Should-Fix] W2: Abstract/Intro \"structural\" 措辞调整\n3. [Should-Fix] W3: Novelty framing 从 \"extends and formalizes\" 改为 \"reveals structural mechanism\"\n4. [Should-Fix] W7: α 系统消融\n5. [Should-Fix] W4: Abstract 中更早区分 self-extracted vs cross-architecture\n6. [Should-Fix] W5-W6: Capability-gap 标注为 preliminary + DPI 展示权重降低\n\n如果 W1 得到充分解决（哪怕只是在 Limitations 中明确标注域局限性），W2-W3 的 framing 调整完成，本文适合 EMNLP 2026 Findings 发表。如果进一步解决 W5（更多 capability-gap 证据）和 W7（α 消融），可达 Conference 水准。\n\n---\n\n*报告由 Review Director 基于 Reviewer 1（方法严谨性+实验有效性）和 Reviewer 2（新颖性+完整性+写作质量）的独立审稿及交叉回应汇总生成。两位 Reviewer 评分完全一致（3.5/5），核心关切高度重合，分歧仅在严重程度分级上。*\n",
  "project": "symb_invariant_consensus",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "\n# 审稿报告：Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning\n\n**目标 venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**审稿轮次**: Round 20（fresh 重新审稿）\n**Reviewer 编排**: R1（方法严谨性+实验有效性）、R2（新颖性+完整性+写作质量）\n**交叉分享**: 完成，两位 Reviewer 均提交逐条 [AGREE]/[REBUT] 回应\n**格式检查**: 正文 8 页 ✓ | ACL review 模板 ✓ | Anonymous ✓ | Abstract ~196 词 ✓ | Limitations 在正文 ✓\n\n---\n\n## Summary\n\n本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought 轨迹中自提取逻辑约束，经 Z3 weighted partial MAX-SAT 聚合答案。核心发现为负面结果：在 6 个模型（7B-32B）、多个推理领域上，SICA 与 Self-Consistency 在 >90% 问题上答案一致，经 BH FDR 校正后无统计显著正向效应。作者将此诊断为 \"symbolic confirmation bias\"（SCB）——自提取约束系统性追随多数答案（bias ratio 1.66-4.97×，9 models from 7B to frontier）。Observation 1（Argmax Preservation）和 Remark 1（DPI Information Ceiling）提供结构性解释。27 种 training-free 变体均因 independence-accuracy trade-off 失败。Cross-architecture verification（DeBERTa NLI）仅在弱生成器上显著（+6.67 pp, p<0.001）。三个零成本诊断指标（C₀, K_eff, BR）预判失败模式。\n\n---\n\n## Strengths\n\n**S1. 统计方法论严谨性远超同类负面结果论文 [R1, R2 共识]**\nMcNemar exact test + 10,000 bootstrap CI + BH FDR correction (m=6 confirmatory) + TOST equivalence (±2pp) + power analysis (MDE) + multi-seed replication (3-5 seeds)。区分了 \"no effect detected\" 和 \"equivalence confirmed\"，在 NLP 负面结果论文中极为罕见。（§3.2, §4, Table 1, Appendix D-E）\n\n**S2. 失败机制诊断逻辑自洽 [R1, R2 共识]**\nSCB 诊断链条完整：BR > 1 → degeneration (|C\\|/|C| ≈ 0.034) → argmax preservation → 803/804 agreement (Table 10)。DAG 因果图（Figure 3）直观展示信息瓶颈。Constraint ablation（MAX-SAT vs count-only vs random-weight）令人信服地证明约束未携带超越投票计数的信号。\n\n**S3. 结构性解释超越纯经验观察 [R2 主要, R1 同意]**\nObservation 1 + Remark 1 将\"self-extraction doesn't work\"从经验发现提升为结构性解释——在 self-extraction 范式内，约束无法携带超越 trace 本身的信息。这是对 Huang et al. (2024) 的实质推进：解释了*为什么*即使在 provably sound solver (Z3) 下仍然失败。\n\n**S4. 27 种 remediation 策略的系统性失败 [R1, R2 共识]**\nFigure 4 + Table 14 覆盖 prompt-level (9)、method-level (3)、analytical conditions (17)，跨 diverse prompting、iterative refinement、contrastive scoring、atom pipeline、UNSAT filtering 等方向。有力地证明退化是结构性的而非调参问题。\n\n**S5. 诊断框架可操作性强 [R1, R2 共识]**\nC₀（multi-candidate rate）、K_eff（effective ensemble size）、BR（bias ratio）三指标零成本可计算（无需 ground truth），Type A/B/C 分类正确预测所有 60 个测试条件的失败模式。为从业者提供 K=12 pilot run 即可判断的 \"try before deploy\" 工具。（§5.3, Table 5）\n\n**S6. Cross-architecture escape 提供建设性方向 [R1, R2 共识]**\nDeBERTa NLI 在 Mistral-7B 上 +6.67 pp (p<0.001)，且 cross-model voting vs cross-architecture NLI 对比（Table cross-model-ablation）区分了 ensemble diversity 和 structural independence。CCR 指标（Appendix C）和 108 种 verifier-generator 组合提供量化框架。\n\n**S7. 写作质量整体良好 [R2 主要, R1 同意]**\n叙事从 \"symbolic verification should help\" → \"it doesn't\" → \"here's why structurally\" → \"here's how to diagnose/escape\" 连贯。Abstract ~196 词符合 EMNLP 限制。Related Work 5 段分类合理（SC/ensemble + neuro-symbolic + CoT bias distinction + test-time compute + training-based）。Limitations 简洁覆盖主要局限。\n\n---\n\n## Weaknesses\n\n### Must-Fix（1 项，Director 综合判定）\n\n**W1. Oracle 实验仅限形式逻辑领域，核心因果主张的外部效度不足 [R1-N1 Must-Fix, R2 AGREE]**\n- Oracle control（用 gold DSL/FOL 标注替换自提取约束）仅在 FOLIO 和 ProofWriter 上进行，均为形式逻辑领域。核心因果推断——\"瓶颈在自提取质量而非聚合机制本身\"——的直接证据领域受限。\n- 替代假说未排除：MAX-SAT 对数学推理或常识推理的约束类型可能天然不适用。\n- ProofWriter oracle 的 97.14% accuracy 证明了聚合机制在给定好约束时有效，但仅限形式逻辑。\n- Section 1 贡献声明暗示跨域通用性，但 oracle 证据不支撑。\n- **建议**：(a) Limitations 中明确 oracle 因果推断的域局限性；(b) 论证逻辑推理是 SCB 的 \"best-case\" domain（constraint formalization 最自然），因此 negative result 具有下界意义；(c) 或在 GSM8K 上构建 partial oracle。\n\n### Should-Fix（6 项）\n\n**W2. Observation 1 的形式化程度与 Abstract/Intro 呈现不匹配 [R1-N2 Must-Fix→Director 降为 Should-Fix, R2 AGREE]**\n- 三个退化条件均使用 \"≈\" 且无误差界。Abstract 称 \"The failure is structural (Observation 1)\"——\"structural\" 暗示形式化证明但实际是半形式化经验观察。\n- R2 指出论文恰当使用 \"Observation\" 而非 \"Theorem\"，条件(i) |C\\|/|C| ≤ 0.034 有量化。Director 同意 R2 评估，将此降为 Should-Fix。\n- **建议**：Abstract/Intro 使用 \"empirically structural\" 或 \"systematic\" 替代 \"structural\"。\n\n**W3. 新颖性相对于 Huang et al. (2024) 的差异化论述需更锐利 [R2-N2 Must-Fix→Director 降为 Should-Fix, R1 REBUT]**\n- 论文多次使用 \"extends and formalizes\" Huang et al.，给人 \"confirmatory study\" 印象。\n- R1 反驳：论文实际贡献远超 confirmation——完整 formal pipeline (Z3 MAX-SAT) + 27 strategies + escape + diagnostics，Huang et al. 完全没有。问题在 framing 太谦虚而非贡献不足。\n- Director 判断：同意 R1。论文实质贡献独立且充分。建议 frame 为 \"reveals a deeper structural mechanism that Huang's empirical observation did not explain\"，而非 \"extends and formalizes\"。\n\n**W4. 标题 \"No Detectable Improvement\" 的 scope 与 cross-architecture 正面结果存在张力 [R2-N1 Must-Fix→Director 降为 Should-Fix, R1 REBUT]**\n- R2 担忧读者可能理解为 \"symbolic constraints don't help LLM reasoning\"。\n- R1 反驳：标题限定词 \"Self-Extracted Constraints\" 已充分区分——cross-architecture escape 的增益来源是外部验证器的独立信号，不是自提取约束。\n- Director 判断：同意 R1，标题在技术上精确。但建议在 Abstract 中更早区分 self-extracted vs cross-architecture，减少误读风险。\n\n**W5. Capability-gap pattern 证据基础薄弱 [R1-W2 + R2-W4 共识]**\n- 核心单调性主张依赖 n=6 generator-verifier 配对（Spearman ρ=1.0, p=0.003）。\n- 108 种 verifier-generator-weight 组合（Figure 8）扩展覆盖面，但核心趋势仍受限。\n- 仅弱生成器（SC ≤ 72%）上显著，强生成器 Δ ≤ +0.83 pp 甚至负向。实用价值局限。\n- **建议**：增加更多能力梯度生成器，或明确标注为 \"preliminary evidence\"。\n\n**W6. Remark 1 (DPI bound) 理论贡献有限 [R1-W1 + R2-W1 共识]**\n- DPI（I(f(X);Y) ≤ I(X;Y)）是确定性后处理的教科书性质，非 SICA 特有。\n- \"Information Ceiling\" 命名暗示特定理论发现，但实际贡献是识别 M→T→A→C Markov chain 结构。\n- **建议**：降低展示权重，将重点放在 \"identifying the Markov structure\" 上。\n\n**W7. α 系统消融缺失 [R1-Q2 + R2-Q2 共识]**\n- Table 11 显示 MAX-SAT vs count-only agreement ≥99% across α ∈ [0.1, 0.9]，但这是 count-only 替换而非移除 answer_assertion。\n- α→0 时（完全依赖 Z3 可满足性权重，不用 source-attribution）退化是否减弱？这直接关系到 Observation 1 条件(ii) source-attribution 的必要性。\n- **建议**：在 Appendix 中报告 α 的完整消融，特别是 α=0 条件。\n\n### Minor（6 项）\n\n- M1. \"pp\"（percentage points）未在首次使用时定义 [R2-M1]\n- M2. Figure 2 散点图灰度打印可读性可改善（marker shape 差异不足）[R1-M1, R2-M2]\n- M3. Figure 4 策略名称文字较密集，部分长文本打印时约 6-7pt [视觉审查 warning]\n- M4. Figure 4 四个 category 灰度打印时颜色区分不足 [视觉审查 warning]\n- M5. Table 1 脚注符号密度较高（*,†,◦,●），可考虑简化 [R1-M2]\n- M6. 匿名 repo 建议——对负面结果论文的复现尤其重要 [R2-M5]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下关键问题两位 Reviewer 达成共识：\n1. **Oracle 领域覆盖不足**是核心缺陷（R1-N1 ≈ R2-W2 底层关切）\n2. **Observation 1 形式化与呈现差距**需要调整措辞（R1-N2, R2 AGREE with nuance）\n3. **DPI (Remark 1) 贡献有限**——教科书性质而非特有洞见（R1-W1 = R2-W1）\n4. **Capability-gap 证据薄弱** (n=6) + 实用价值局限（仅弱生成器受益）（R1-W2 ≈ R2-W4）\n5. **α 消融缺失**——理解 Observation 1 条件(ii) 必要性的关键实验（R1-Q2 = R2-Q2）\n6. **统计方法论优秀**——McNemar/TOST/bootstrap/FDR/power analysis 组合在同类论文中罕见（R1-S1 = R2-S1）\n7. **诊断框架实用**——C₀/K_eff/BR 零成本指标对从业者立即可部署（R1-S5 = R2-S4）\n8. **Overall 3.5/5 完全一致**\n\n## Reviewer Divergence [REBUT]\n\n以下问题存在分歧，由 Director 做出最终判定：\n\n1. **标题 scope（R2-N1）**：R2 列为 Must-Fix，R1 REBUT（\"Self-Extracted\" 限定词已足够精确）。**Director 判定**：同意 R1，降为 Should-Fix。标题在技术上精确，但建议在 Abstract 中更早区分 self-extracted vs cross-architecture 以减少误读。\n\n2. **新颖性 vs Huang et al.（R2-N2）**：R2 列为 Must-Fix（\"extends and formalizes\" 弱化贡献），R1 REBUT（贡献远超 confirmatory：formal pipeline + 27 strategies + escape + diagnostics）。**Director 判定**：同意 R1，降为 Should-Fix。实质性贡献充分，framing 调整即可（\"reveals structural mechanism\" 而非 \"extends\"）。\n\n3. **前沿模型 full pipeline（R1-W3）**：R1 称前沿模型\"未跑 full pipeline\"，R2 REBUT（Table 2 显示 gpt-4.1/Gemini-2.5-Pro 在 FOLIO 上运行了完整 SICA pipeline，Δ=0）。**Director 判定**：R2 事实性纠正成立。前沿模型确实跑了 full pipeline（至少在 FOLIO 上），R1 此处有事实错误。合理关切是前沿模型仅在 FOLIO (n=204) 上测试。\n\n4. **数据集范围（R2-W2）**：R2 声称\"所有数据集均为形式/逻辑推理\"，R1 REBUT（论文包含 GSM8K, AIME, StrategyQA, ARC-Challenge）。**Director 判定**：R1 事实性纠正成立——论文确实包含非逻辑领域数据集，但 confirmatory 分析集中于逻辑领域。底层关切有效但 R2 表述有误。\n\n---\n\n## Questions\n\n**Q1 [R1, R2 共识]**: α=0.5 的选择依据？α 取极端值（0 或 1）时退化程度如何变化？特别是 α→0（完全依赖 Z3 满足性权重，不用 source-attribution）时，SCB 是否减弱？\n\n**Q2 [R2 提出, R1 AGREE]**: 若不用 source-attribution scoring 而用语义相似度评分，Observation 1 是否仍然成立？Source-attribution scoring 是 degeneration 的充分条件还是必要条件？\n\n**Q3 [R1]**: ProofWriter oracle 约束是否经过与自提取约束相同的 Z3 dedup 流程？若未经 dedup，oracle vs. self-extraction 比较可能受 dedup 策略差异混淆。\n\n**Q4 [R1, R2 共识]**: DeBERTa NLI 判断的粒度——constraint 级别还是 trace 级别？这对理解 DeBERTa 如何打破 confirmation bias 至关重要。\n\n**Q5 [R2]**: 是否尝试过 adversarial constraint generation——显式要求模型生成与当前多数答案矛盾的约束？这与 diverse prompting 不同，是显式鼓励反事实推理。\n\n**Q6 [R1]**: 是否考虑过提取 trace 间 disagreement 而非 trace 内约束？若约束捕获 \"trace A 与 trace B 在 X 上不一致\"，source-attribution coupling 可能被打破。\n\n---\n\n## Missing References\n\n论文整体引用覆盖良好（~48 citations, 5 Related Work 段落）。以下为可选补充：\n\n- **[Optional]** Weng et al. (2023) \"Large Language Models are Better Reasoners with Self-Verification\" — backward verification 方法与 SICA forward extraction 的对比可在 §2 简要讨论\n- R2 建议的 \"Li et al. (AAAI 2026) Survey on LLM Symbolic Reasoning\" 无法验证真实性（R1 REBUT），不列为推荐引用\n\n**已在论文中引用的关键工作**：Huang et al. (ICLR 2024) ✓, Stechly et al. ✓ (implicitly via Wan et al. 2025 positioning), SatLM ✓, Math-Shepherd ✓, o1/o3 ✓, Dietterich (2000) ✓, Krogh & Vedelsby (1994) ✓\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置。项目 config 中无 `external_review.paperreview_ai.enabled` 设置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 3 warning, 26 info）。\n\n**Warnings**:\n1. Figure 2 图例文字和标记在单栏宽度下偏小，打印时可能需仔细辨认\n2. Figure 4 策略名称 y 轴标签较密集，部分长文本约 6-7pt\n3. Figure 4 四个 category 仅靠颜色区分时灰度打印可能难以辨认\n\n**Positive findings**:\n- 布局节奏良好：text-figure-table 交替均匀，无连续 2 页纯文本\n- 主文 8 页含 4 figures + 3 tables = 7 display items，密度 0.875/页（推荐范围内）\n- 所有 figure/table 在首次引用附近出现，无明显 float 漂移\n- Page 8 内容填充完整（>90% 利用率），无大面积空白\n- 公式渲染正确，编号连续，无 LaTeX 残留错误\n- Appendix 18 页（2 Algorithms + ~8 figures + ~30 tables），内容充实\n\n---\n\n## Overall Assessment\n\n**Overall Score**: 3.5 / 5（Borderline Conference）\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 4/5 | 统计方法论扎实，实验覆盖全面。Observation 1 成立且有经验支持，但形式化程度为半形式化观察。Oracle 因果推断领域受限 |\n| Excitement | 3/5 | 重要负面结果（关闭 self-extraction + formal verification 路径），诊断框架实用。但核心 insight 在概念上被 Huang et al. 部分预期，constructive contribution 仅限弱生成器 |\n| Reproducibility | 4/5 | 超参数完整报告，Appendix A 完整 prompt templates，Algorithm 1-2 伪代码清晰，代码承诺接收后发布 |\n| Confidence | 4/5 | 两位 Reviewer 均对 SC、formal verification、LLM reasoning 文献熟悉，仔细阅读全文 28 页 |\n\n**总评**：\n\n这是一篇实验方法论极为严谨的负面结果论文。核心优势在于：(1) 统计论证链的完整性（McNemar + Bootstrap CI + TOST + FDR + Power Analysis）在同类工作中罕见；(2) SCB 的诊断链条逻辑自洽（BR → degeneration → argmax preservation → constraint ablation 803/804 agreement）；(3) 诊断框架（C₀, K_eff, BR）对从业者有直接实用价值。\n\n主要问题：(1) Oracle 因果推断仅限形式逻辑领域，无法排除 MAX-SAT 对其他推理类型天然不适用的替代假说；(2) Observation 1 的 \"structural\" 呈现超出其半形式化观察的形式化程度；(3) 新颖性 framing（\"extends and formalizes\" Huang et al.）低估了论文的独立贡献；(4) Cross-architecture escape 的 capability-gap 依赖限制了其一般性。\n\n**建议处理优先级**：\n1. [Must-Fix] W1: Oracle 因果推断的域局限性——在 Limitations 中明确标注，或补充非逻辑域 oracle\n2. [Should-Fix] W2: Abstract/Intro \"structural\" 措辞调整\n3. [Should-Fix] W3: Novelty framing 从 \"extends and formalizes\" 改为 \"reveals structural mechanism\"\n4. [Should-Fix] W7: α 系统消融\n5. [Should-Fix] W4: Abstract 中更早区分 self-extracted vs cross-architecture\n6. [Should-Fix] W5-W6: Capability-gap 标注为 preliminary + DPI 展示权重降低\n\n如果 W1 得到充分解决（哪怕只是在 Limitations 中明确标注域局限性），W2-W3 的 framing 调整完成，本文适合 EMNLP 2026 Findings 发表。如果进一步解决 W5（更多 capability-gap 证据）和 W7（α 消融），可达 Conference 水准。\n\n---\n\n*报告由 Review Director 基于 Reviewer 1（方法严谨性+实验有效性）和 Reviewer 2（新颖性+完整性+写作质量）的独立审稿及交叉回应汇总生成。两位 Reviewer 评分完全一致（3.5/5），核心关切高度重合，分歧仅在严重程度分级上。*\n",
    "project": "symb_invariant_consensus",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 2105 · 2026-05-23T19:29:40.813178+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3918
}
```

</details>

---


### Assistant

_source line 2106 · 2026-05-23T19:29:51.097410+00:00_

审稿报告已投递给 Research Director。

**审稿完成总结**：

- **Overall**: 3.5/5（Borderline Conference）
- **两位 Reviewer 评分完全一致**，核心关切高度重合
- **1 个 Must-Fix**：Oracle 因果推断仅限形式逻辑领域
- **6 个 Should-Fix**：Observation 1 措辞、Huang et al. 差异化 framing、标题 scope 澄清、capability-gap 证据、DPI 展示权重、α 消融
- **结论**：实验方法论极为严谨的负面结果论文。如果 Must-Fix 解决 + framing 调整完成，适合 Findings 发表；若进一步补充 capability-gap 证据和 α 消融，可达 Conference 水准

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 154

## Round 154

2 recorded events


### User

_source line 2107 · 2026-05-23T19:29:53.601464+00:00_

[Reviewer 2 审稿结果]:
审稿交叉回应已提交。两位 Reviewer 在 Overall 3.5、Soundness 4/5、Excitement 3/5 上完全一致。主要共识集中在 claim scope 需缩窄、Huang et al. 差异化需更锐利、形式化呈现需更审慎。唯一实质性分歧是 R1-W3 关于前沿模型是否跑了 full pipeline——Table 2 证据表明 gpt-4.1/Gemini-2.5-Pro 确实在 FOLIO 上完成了完整 SICA pipeline（Δ=0），R1 的描述不准确。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2108 · 2026-05-23T19:30:04.893972+00:00_

审稿已完成。报告已投递给 Research Director。

**Round 20 审稿总结**：

- **Overall**: 3.5/5（Borderline Conference），两位 Reviewer 评分完全一致
- **1 个 Must-Fix**：Oracle 因果推断仅限形式逻辑领域，外部效度不足
- **6 个 Should-Fix**：Observation 1 "structural" 措辞、Huang et al. 差异化 framing、标题 scope、capability-gap 证据、DPI 展示权重、α 消融缺失
- **建议**：解决 Must-Fix + framing 调整后适合 Findings；进一步补强 capability-gap 证据和 α 消融可达 Conference

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 155

## Round 155

58 recorded events


### User

_source line 2109 · 2026-05-23T20:07:12.691539+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: symb_invariant_consensus
- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2110 · 2026-05-23T20:07:23.433483+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2111 · 2026-05-23T20:07:23.534830+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2112 · 2026-05-23T20:07:28.117905+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2113 · 2026-05-23T20:07:28.170049+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 2114 · 2026-05-23T20:07:36.853403+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 2115 · 2026-05-23T20:07:38.810421+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (173 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-multi-seed-llama-pw-seed789-v2 | LLaMA-3.1-8B PW seed789 多种子复制（westd-30973 cuda:1 全新运行）。替代 16639 cuda:0 上的慢速运行（12/600）。验证 SCB 在 ProofWriter 上跨 seed 稳定性。 | — | — | — |\n| exp-multi-seed-llama-pw-seed456-v2 | LLaMA-3.1-8B PW seed456 多种子复制（westd-30973 cuda:2 全新运行）。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。 | — | — | — |\n| exp-multi-seed-qwen25-pw-seed789-v3 | Qwen2.5-14B PW seed789 多种子复制（westd-30973 cuda:0 全新运行）。替代 v2 在 16639 cuda:2 上的慢速运行（53/600）。验证 SCB 在 ProofWriter 上跨 seed 稳定性。 | — | — | — |\n\n## 待处理\n- exp-multi-seed-llama-pw-seed456: LLaMA-3.1-8B PW seed456 多种子复制。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。（排队等待 GPU）\n- exp-deberta-ft-combo: Fine-tuned DeBERTa-large on ProofWriter OWA depth-5 achieves near-perfect NLI accuracy (99.67%) and provides massive combo gains over SC baseline when used as external verifier, demonstrating that domain-specific NLI fine-tuning breaks the SCB ceiling by providing truly independent verification signal.（准备中）\n- exp-multi-seed-mistral-folio: Multi-seed replication (seeds 123,456,789) of Mistral-7B × FOLIO-20
…[truncated 1733 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1957
}
```

</details>

---


### Tool call

_source line 2116 · 2026-05-23T20:07:38.810902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_18/submitted.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_18/submitted.pdf"
  }
}
```

</details>

---


### Tool result

_source line 2117 · 2026-05-23T20:07:38.961763+00:00_

This PDF has 28 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2118 · 2026-05-23T20:07:38.962163+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
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

_source line 2119 · 2026-05-23T20:07:39.062705+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2120 · 2026-05-23T20:07:46.700056+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_18/submitted.pdf",
  "pages": "1-15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_18/submitted.pdf",
    "pages": "1-15"
  }
}
```

</details>

---


### Tool call

_source line 2121 · 2026-05-23T20:07:47.691417+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 2122 · 2026-05-23T20:07:48.129666+00:00_

PDF pages extracted: 15 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_18/submitted.pdf (646.7KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 1429
}
```

</details>

---


### Tool call

_source line 2123 · 2026-05-23T20:07:48.278382+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2124 · 2026-05-23T20:07:48.479547+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % removed: not available in this TeX distribution
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{tcolorbox}
14	\tcbuselibrary{skins}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{subcaption}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,calc,fit}
22	\usepackage{listings}
23	\usepackage{algorithm}
24	\usepackage{algpseudocode}
25	\usepackage{hyperref}
26	\usepackage{cleveref}
27	
28	\lstset{
29	  basicstyle=\small\ttfamily,
30	  breaklines=true,
31	  frame=single,
32	  xleftmargin=1em,
33	  xrightmargin=1em,
34	  aboveskip=0.5em,
35	  belowskip=0.5em,
36	}
37	
38	\graphicspath{{../figures/paper/}{figures/}}
39	
40	\title{Beyond Self-Consistency: Self-Extracted Constraints\\Provide No Detectable Improvement in LLM Reasoning}
41	
42	\author{Anonymous}
43	
44	\begin{document}
45	\maketitle
46	
47	% Tighten spacing for 8-page budget
48	\setlength{\textfloatsep}{5pt plus 2pt minus 4pt}
49	\setlength{\dbltextfloatsep}{5pt plus 2pt minus 4pt}
50	\setlength{\floatsep}{3pt plus 2pt minus 2pt}
51	\setlength{\dblfloatsep}{3pt plus 2pt minus 2pt}
52	\setlength{\abovecaptionskip}{2pt}
53	\setlength{\belowcaptionskip}{0pt}
54	\setlength{\abovedisplayskip}{4pt plus 1pt minus 2pt}
55	\setlength{\belowdisplayskip}{4pt plus 1pt minus 2pt}
56	\setlength{\intextsep}{5pt plus 1pt minus 2pt}
57	
58	\input{abstract}
59	
60	\input{introduction}
61	
62	\input{related_work}
63	
64	\input{method}
65	
66	\input{experiments}
67	
68	\input{analysis}
69	
70	\input{solutions}
71	
72	\input{discussion}
73	
74	\section*{Limitations}
75	\input{limitations_content}
76	
77	\bibliography{references}
78	
79	\appendix
80	\input{appendix}
81	
82	\end{
…[truncated 13 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool result

_source line 2125 · 2026-05-23T20:07:54.448509+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

I've completed the web search for "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org". Here are the results:
…[truncated 1304 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6757
}
```

</details>

---


### Tool call

_source line 2126 · 2026-05-23T20:08:02.430143+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_18/submitted.pdf",
  "pages": "16-28"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_18/submitted.pdf",
    "pages": "16-28"
  }
}
```

</details>

---


### Tool call

_source line 2127 · 2026-05-23T20:08:03.185476+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool result

_source line 2128 · 2026-05-23T20:08:03.236143+00:00_

PDF pages extracted: 13 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_18/submitted.pdf (646.7KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool result

_source line 2129 · 2026-05-23T20:08:09.933011+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on the search results, here are the key submission guidelines for ACL Rolling Review (ARR) 2026:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

A section
…[truncated 865 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6747
}
```

</details>

---


### Tool call

_source line 2130 · 2026-05-23T20:08:36.728676+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,TodoWrite",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,TodoWrite",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 2131 · 2026-05-23T20:08:36.829825+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2132 · 2026-05-23T20:08:49.564304+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2133 · 2026-05-23T20:08:49.564708+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2134 · 2026-05-23T20:08:50.821412+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "review_issues.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "review_issues.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 2135 · 2026-05-23T20:08:50.972325+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2136 · 2026-05-23T20:08:50.972730+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 2137 · 2026-05-23T20:08:51.425058+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (173 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-multi-seed-llama-pw-seed789-v2 | LLaMA-3.1-8B PW seed789 多种子复制（westd-30973 cuda:1 全新运行）。替代 16639 cuda:0 上的慢速运行（12/600）。验证 SCB 在 ProofWriter 上跨 seed 稳定性。 | — | — | — |\n| exp-multi-seed-llama-pw-seed456-v2 | LLaMA-3.1-8B PW seed456 多种子复制（westd-30973 cuda:2 全新运行）。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。 | — | — | — |\n| exp-multi-seed-qwen25-pw-seed789-v3 | Qwen2.5-14B PW seed789 多种子复制（westd-30973 cuda:0 全新运行）。替代 v2 在 16639 cuda:2 上的慢速运行（53/600）。验证 SCB 在 ProofWriter 上跨 seed 稳定性。 | — | — | — |\n\n## 待处理\n- exp-multi-seed-llama-pw-seed456: LLaMA-3.1-8B PW seed456 多种子复制。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。（排队等待 GPU）\n- exp-deberta-ft-combo: Fine-tuned DeBERTa-large on ProofWriter OWA depth-5 achieves near-perfect NLI accuracy (99.67%) and provides massive combo gains over SC baseline when used as external verifier, demonstrating that domain-specific NLI fine-tuning breaks the SCB ceiling by providing truly independent verification signal.（准备中）\n- exp-multi-seed-mistral-folio: Multi-seed replication (seeds 123,456,789) of Mistral-7B × FOLIO-20
…[truncated 1733 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2138 · 2026-05-23T20:09:02.916409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2139 · 2026-05-23T20:09:03.569936+00:00_

1	# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
2	- id: "R1-C1"
3	  summary: "Method Stage 3 sat() implementation undescribed"
4	  category: method
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 1
8	  last_seen_round: 3
9	  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
10	  resolution_round: 3
11	
12	- id: "R1-C2"
13	  summary: "Most experiments underpowered (n≤60), no power analysis"
14	  category: experiment
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
20	  resolution_round: 3
21	
22	- id: "R1-C3"
23	  summary: "Oracle/upper-bound experiment missing"
24	  category: experiment
25	  severity: critical
26	  status: resolved
27	  first_raised_round: 1
28	  last_seen_round: 1
29	  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
30	  resolution_round: 3
31	
32	- id: "R1-C4"
33	  summary: "Huang et al. (ICLR 2024) not cited"
34	  category: framing
35	  severity: critical
36	  status: resolved
37	  first_raised_round: 1
38	  last_seen_round: 2
39	  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
40	  resolution_round: 2
41	
42	- id: "R1-C5"
43	  summary: "Critical related work missing"
44	  category: writing
45	  severity: critical
46	  status: resolved
47	  first_raised_round: 1
48	  last_seen_round: 1
49	  resolution: "~48 citations, 5 Related Work paragraphs."
50	  resolution_round: 3
51	
52	- id: "R1-C9"
53	  summary: "Capability trap novelty unclear"
54	  category: framing
55	  severity: critical
56	  status: resolved
57	  first_raised_round: 1
58	  last_seen_round: 3
59	  resolution: "Reframed as regime-dependent analysis with CJT framework."
60	  resolution_round: 3
61	
62	- id: "R3-N1"
63	  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
64	  category: method
65	  severity: critical

…[truncated 22721 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 2140 · 2026-05-23T20:09:03.570330+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR deadline May 2026 submission date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR deadline May 2026 submission date"
  }
}
```

</details>

---


### Tool result

_source line 2141 · 2026-05-23T20:09:08.544756+00:00_

Web search results for query: "EMNLP 2026 ARR deadline May 2026 submission date"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 Submitting to the May 19th ARR deadline? ✅ Make sure your profile is complete, including your DBLP link: https://t.co/jr60DoKZ2R 📄 Do not forget to review: (1) Author Guidelines https://t.co/QTDyAWZtKS (2) ACL Publication policy https://t.co/nImuaa9cez #NLProc #EMNLP25 #ARR\" / X","url":"https://x.com/emnlpmeeting/status/1923431912778895593"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"}]

Based on the search results, here is the information about EMNLP 2026 ARR deadl
…[truncated 842 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 4974
}
```

</details>

---


### Tool call

_source line 2142 · 2026-05-23T20:09:54.759251+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'in_progress', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'in_progress', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2143 · 2026-05-23T20:09:54.759640+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2144 · 2026-05-23T20:09:56.618030+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "symb_invariant_consensus",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool call

_source line 2145 · 2026-05-23T20:09:56.768964+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 2146 · 2026-05-23T20:10:00.238056+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3620
}
```

</details>

---


### Tool result

_source line 2147 · 2026-05-23T20:10:00.238461+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3469
}
```

</details>

---


### Tool call

_source line 2148 · 2026-05-23T20:10:14.292340+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/symb_invariant_consensus/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/symb_invariant_consensus/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3"
  }
}
```

</details>

---


### Tool result

_source line 2149 · 2026-05-23T20:10:14.342961+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2150 · 2026-05-23T20:10:22.568569+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/symb_invariant_consensus/**/config*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/symb_invariant_consensus/**/config*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3"
  }
}
```

</details>

---


### Tool result

_source line 2151 · 2026-05-23T20:10:22.721099+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 2152 · 2026-05-23T20:10:27.734286+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/projects.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/projects.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3"
  }
}
```

</details>

---


### Tool result

_source line 2153 · 2026-05-23T20:10:28.139243+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 2154 · 2026-05-23T20:10:32.791282+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/",
  "description": "List project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/",
    "description": "List project directory"
  }
}
```

</details>

---


### Tool result

_source line 2155 · 2026-05-23T20:10:32.943306+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
_last_visual_review.json
alpha_ablation_analysis.py
analysis_cegis_sica.py
analysis_confirmation_bias.py
analysis_deepconf_filter.py
analysis_problem_perturbation.py
analysis_process_kappa.py
artifacts
checkpoints
compute_r17_metrics.py
constraints.lock
constraints.yaml
decisions.lock
decisions.yaml
direction_f_blind_fol.py
direction_g_decoupling.py
direction_i_z3_filter.py
direction_j_bootstrap.py
direction_k_minority_report.py
direction_q_premise_mutation.py
direction_r_nli_verifier.py
direction_rg_combo.py
distill_tmp
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
exp_d126_crossmodel_sica.py
experiment_plan.lock
experiment_plan.yaml
figures
launch_d126.sh
literature_map.yaml
logiqa_nli_combo.py
logs
memory.md
mistakes.lock
mistakes.yaml
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
premise_formalization.py
reextract_bpe_fix.py
registry.lock
registry.yaml
report.md
review_visual_check_state.json
run_contrastive.py
run_debate.py
run_icg_v2.py
scripts
src
study_status.lock
task_context
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 2156 · 2026-05-23T20:10:37.663139+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "glob": "*.yaml",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
    "glob": "*.yaml",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 2157 · 2026-05-23T20:10:37.713859+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2158 · 2026-05-23T20:10:55.868761+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2159 · 2026-05-23T20:10:55.869367+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2160 · 2026-05-23T20:11:19.541525+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "你是 Reviewer 1，负责审查方法严谨性和实验有效性。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning\n- **论文路径**: projects/symb_invariant_consensus/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_18/submitted.pdf\n\n## 目标 Venue\n- **会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，引用不限页数，Limitations 不计入页数\n- **模板**: ACL style (review mode)\n- **匿名规则**: Double-blind（不得暴露作者身份）\n\n## 评分标准（EMNLP 2026 / ARR）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n\n**方法严谨性**：\n1. SICA pipeline 形式化质量（Eq.1-5, Algorithm 1-2, Observation 1, Remark 1）——条件是否清晰、验证是否充分、形式化程度与声称是否匹配\n2. \"Symbolic Confirmation Bias\" 的因果机制论证——M→T→A→C Markov chain 结构的合理性和证据强度\n3. Bias Ratio (BR) 指标设计——是否存在循环论证，permutation null model 是否充分\n\n**实验有效性**：\n4. 统计方法论（McNemar test, TOST ±2pp, BH FDR correction, bootstrap CIs, power analysis）——方法选择是否恰当，多重检验校正是否充分\n5. 实验规模和设计——6 模型 × 4 基准是否有足够覆盖度，seed replication 是否充分（3-4 seeds），underpowered conditions 的处理\n6. Cross-architecture escape (§6) 的证据强度——DeBERTa NLI verifier 结果是否支撑 contribution 3 的 claim，capability-gap pattern (n=6 rank correlation) 的推断强度\n7. 27 training-free variants 穷举性——覆盖度是否足够，是否遗漏重要方法类别\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix) → Questions → Missing References → Overall Assessment + Score + Confidence。\n\nWeaknesses 必须区分 Must-Fix（阻碍接收）和 Should-Fix（改善论文但不阻碍）。每条 weakness 必须引用具体的 Section/Table/Figure 作为证据。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "你是 Reviewer 1，负责审查方法严谨性和实验有效性。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning\n- **论文路径**: projects/symb_invariant_consensus/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_18/submitted.pdf\n\n## 目标 Venue\n- **会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，引用不限页数，Limitations 不计入页数\n- **模板**: ACL style (review mode)\n- **匿名规则**: Double-blind（不得暴露作者身份）\n\n## 评分标准（EMNLP 2026 / ARR）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n\n**方法严谨性**：\n1. SICA pipeline 形式化质量（Eq.1-5, Algorithm 1-2, Observation 1, Remark 1）——条件是否清晰、验证是否充分、形式化程度与声称是否匹配\n2. \"Symbolic Confirmation Bias\" 的因果机制论证——M→T→A→C Markov chain 结构的合理性和证据强度\n3. Bias Ratio (BR) 指标设计——是否存在循环论证，permutation null model 是否充分\n\n**实验有效性**：\n4. 统计方法论（McNemar test, TOST ±2pp, BH FDR correction, bootstrap CIs, power analysis）——方法选择是否恰当，多重检验校正是否充分\n5. 实验规模和设计——6 模型 × 4 基准是否有足够覆盖度，seed replication 是否充分（3-4 seeds），underpowered conditions 的处理\n6. Cross-architecture escape (§6) 的证据强度——DeBERTa NLI verifier 结果是否支撑 contribution 3 的 claim，capability-gap pattern (n=6 rank correlation) 的推断强度\n7. 27 training-free variants 穷举性——覆盖度是否足够，是否遗漏重要方法类别\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix) → Questions → Missing References → Overall Assessment + Score + Confidence。\n\nWeaknesses 必须区分 Must-Fix（阻碍接收）和 Should-Fix（改善论文但不阻碍）。每条 weakness 必须引用具体的 Section/Table/Figure 作为证据。"
  }
}
```

</details>

---


### Tool result

_source line 2161 · 2026-05-23T20:11:35.468067+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15926
}
```

</details>

---


### Tool call

_source line 2162 · 2026-05-23T20:11:35.619146+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "你是 Reviewer 2，负责审查新颖性、完整性和写作质量。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning\n- **论文路径**: projects/symb_invariant_consensus/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_18/submitted.pdf\n\n## 目标 Venue\n- **会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，引用不限页数，Limitations 不计入页数\n- **模板**: ACL style (review mode)\n- **匿名规则**: Double-blind（不得暴露作者身份）\n- **Abstract 限制**: 不超过 200 words\n\n## 评分标准（EMNLP 2026 / ARR）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n\n**新颖性**：\n1. 与 Huang et al. (2024) \"LLMs cannot self-correct reasoning yet\" 的关系——本文是 confirmatory study 还是有独立贡献？\"extends and formalizes\" 是否充分建立新颖性？\n2. \"Symbolic Confirmation Bias\" 概念——是否只是已知 confirmation bias 的特例？与 Wan et al. (2025), Turpin et al. (2023), Jhaveri et al. (2026) 的 CoT confirmation bias 区别是否清晰？\n3. 三个贡献（symbolic mirage + diagnostic framework + cross-architecture escape）的独立新颖性和影响力\n4. Remark 1 (DPI bound) 是否为教科书级结论而非论文贡献？\n\n**完整性**：\n5. Related Work 覆盖度——neuro-symbolic reasoning, self-consistency, ensemble diversity, test-time compute 等领域是否遗漏重要工作\n6. 实验覆盖度——模型家族、数据集领域（逻辑 vs 数学 vs 常识）、参数敏感性分析\n7. Limitations 是否诚实充分\n\n**写作质量**：\n8. Abstract 是否 ≤200 words，claim 强度是否与证据匹配（特别是标题 \"No Detectable Improvement\" 与 cross-architecture positive results 的张力）\n9. 叙事结构和可读性——8 页密度极高的论文，信息密度是否过载\n10. 术语使用——\"Symbolic Mirage\" 是否过于 dramatic，\"structural property\" vs 实际经验观察\n\n**格式合规**：\n11. 页数限制（8 页正文）、匿名性、引用格式、Limitations section 合规性\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix) → Questions → Missing References → Overall Assessment + Score + Confidence。\n\nWeaknesses 必须区分 Must-Fix（阻碍接收）和 Should-Fix（改善论文但不阻碍）。每条 weakness 必须引用具体的 Section/Table/Figure 作为证据。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "你是 Reviewer 2，负责审查新颖性、完整性和写作质量。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning\n- **论文路径**: projects/symb_invariant_consensus/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_18/submitted.pdf\n\n## 目标 Venue\n- **会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，引用不限页数，Limitations 不计入页数\n- **模板**: ACL style (review mode)\n- **匿名规则**: Double-blind（不得暴露作者身份）\n- **Abstract 限制**: 不超过 200 words\n\n## 评分标准（EMNLP 2026 / ARR）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n\n**新颖性**：\n1. 与 Huang et al. (2024) \"LLMs cannot self-correct reasoning yet\" 的关系——本文是 confirmatory study 还是有独立贡献？\"extends and formalizes\" 是否充分建立新颖性？\n2. \"Symbolic Confirmation Bias\" 概念——是否只是已知 confirmation bias 的特例？与 Wan et al. (2025), Turpin et al. (2023), Jhaveri et al. (2026) 的 CoT confirmation bias 区别是否清晰？\n3. 三个贡献（symbolic mirage + diagnostic framework + cross-architecture escape）的独立新颖性和影响力\n4. Remark 1 (DPI bound) 是否为教科书级结论而非论文贡献？\n\n**完整性**：\n5. Related Work 覆盖度——neuro-symbolic reasoning, self-consistency, ensemble diversity, test-time compute 等领域是否遗漏重要工作\n6. 实验覆盖度——模型家族、数据集领域（逻辑 vs 数学 vs 常识）、参数敏感性分析\n7. Limitations 是否诚实充分\n\n**写作质量**：\n8. Abstract 是否 ≤200 words，claim 强度是否与证据匹配（特别是标题 \"No Detectable Improvement\" 与 cross-architecture positive results 的张力）\n9. 叙事结构和可读性——8 页密度极高的论文，信息密度是否过载\n10. 术语使用——\"Symbolic Mirage\" 是否过于 dramatic，\"structural property\" vs 实际经验观察\n\n**格式合规**：\n11. 页数限制（8 页正文）、匿名性、引用格式、Limitations section 合规性\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix) → Questions → Missing References → Overall Assessment + Score + Confidence。\n\nWeaknesses 必须区分 Must-Fix（阻碍接收）和 Should-Fix（改善论文但不阻碍）。每条 weakness 必须引用具体的 Section/Table/Figure 作为证据。"
  }
}
```

</details>

---


### Tool result

_source line 2163 · 2026-05-23T20:11:37.027213+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool call

_source line 2164 · 2026-05-23T20:11:48.929797+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "270",
  "reason": "等待 Reviewer 1 和 Reviewer 2 完成 Round 1 独立审稿",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: symb_invariant_consensus\n- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "270",
    "reason": "等待 Reviewer 1 和 Reviewer 2 完成 Round 1 独立审稿",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: symb_invariant_consensus\n- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 2165 · 2026-05-23T20:11:49.110987+00:00_

Next wakeup scheduled for 20:16:00 (in 251s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 181
}
```

</details>

---


### Assistant

_source line 2166 · 2026-05-23T20:11:56.818352+00:00_

Reviewer 任务已派发，预计 ~4 分钟后检查返回状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 156

## Round 156

4 recorded events


### User

_source line 2167 · 2026-05-23T20:19:55.306639+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告（Round 1）

**论文**: Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning
**Venue**: EMNLP 2026 (ARR)

---

## Summary

本文研究"LLM 自提取的符号约束能否通过形式化验证提升推理准确率"这一问题。作者提出 SICA（Symbolic Invariant Consensus Aggregation），从 chain-of-thought traces 中提取逻辑约束，经 Z3 验证后用加权 MAX-SAT 选择答案。核心发现是否定的：在 9 个模型（7B–frontier）、4 个 benchmark、27 种 training-free 变体上，SICA 相对 Self-Consistency 无显著提升（FDR 校正后无条件显著，6 个有统计功效的条件中 4 个通过 TOST 确认等价于 ±2pp）。作者将此归因于"Symbolic Confirmation Bias"(SCB)——自提取约束系统性地追随多数票答案，并通过 Data Processing Inequality 论证了信息论上界（Remark 1）。论文还提供了三个零成本诊断指标（K_eff, BR, CCR），并展示跨架构验证（NLI verifier）可以打破自提取瓶颈。

---

## 总体评分

**Overall**: 3.5 / 5 — Borderline Conference
**一句话总结**: 实验规模大、统计分析严谨的重要否定结果论文，但理论贡献薄弱（Remark 1 本质是教科书级 DPI），且 SCB 作为独立于 CoT confirmation bias 的新概念缺乏充分的实证分离。

---

## 官方维度打分（来自 ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法论极为严谨（FDR、TOST、bootstrap CI、permutation test），但"structural property"断言超出实证所能支撑的范围；Remark 1 理论贡献有限 |
| Excitement | 3/5 | 重要的否定结果，对 neuro-symbolic 社区有实践意义；但高层信息（self-verification 无效）已被 Huang et al. (2024) 建立，本文提供的是机制深度而非全新发现 |
| Reproducibility | 4/5 | 方法细节充分（K=12, T=0.7, Z3 timeout 10s, prompt 模板见 Appendix A），模型公开可用，代码承诺发布 |
| Confidence | 4/5 | 仔细阅读全文 28 页，熟悉 self-consistency、neuro-symbolic reasoning、LLM self-correction 相关工作 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **"Structural property" 断言超出实证支撑**
- 具体位置：Abstract ("a structural property of self-extraction pipelines")、Section 5.1、Section 7
- 问题：论文将 SCB 定性为自提取管线的"结构性属性"，暗示其理论必然性。但支撑证据全部是经验性的（9 个模型 × 4 benchmark × 27 变体）。Remark 1 的 DPI 论证仅建立了信息上界 I(C;Y) ≤ I(T;Y)，并未证明此上界必然是紧的。所有测试的 27 种 remediation 策略均属同一类型（zero-shot template extraction），而论文在 Extended Discussion（Appendix Y, p.27）自己也承认"few-shot exemplars, chain-of-thought extraction, or iterative refinement might yield higher-quality constraints"——这恰恰说明"structural"这一修饰词过强。如果一种未测试的提取策略能打破 M→T→A→C 的 Markov 假设（例如 iterative multi-turn extraction），那"structural property"就不成立。
- 为什么影响接收：这是论文三大贡献之一的基础性声明。如果 SCB 只是"在当前测试的 zero-shot template extraction 策略下普遍观测到的现象"，其理论意义和泛化声明需要显著弱化。
- 建议修改方向：将"structural property"改为"robust empirical regularity"或"persistent pattern"，并在 Discussion 中明确讨论哪些条件下此 Markov 假设可能被打破。

**N2** [critical] **SCB 与 CoT confirmation bias 的实证分离不充分**
- 具体位置：Section 2 (p.2, "Distinction from CoT confirmation bias")、Section 5.1
- 问题：论文在概念上区分了 SCB（聚合层面：自提取约束集整体追随多数票）与 CoT confirmation bias（trace 层面：单条推理链不忠实）。但实验中未提供关键的分离测试：在产生**少数票答案**的 trace 中，提取的约束是支持该 trace 自身的少数票答案（CoT bias 的预测），还是支持全局多数票答案（SCB 的预测）？BR 指标（Section 5.1, Table 2）展示了整体约束偏向多数票，但这与"CoT bias 在 trace 层面运作、通过聚合传递到约束层面"的解释同样一致。Appendix O（Cross-Model Confirmation Bias）的 process similarity 分析提供了间接证据，但不在主文中，且仍非决定性分离测试。
- 为什么影响接收：SCB 是论文的核心概念贡献（contribution #1）。如果它实际上只是已知 CoT confirmation bias 的一个推论，而非独立现象，则论文的新颖性大幅下降。
- 建议修改方向：(a) 在主文中增加一个 per-trace 分析：对产生少数票答案的 trace，分别统计其约束对少数票 vs 多数票的支持率；(b) 如果数据显示约束主要支持各自 trace 的答案而非全局多数票，应诚实修正 SCB 的定义为 CoT bias 的约束层表现。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Remark 1 (DPI bound) 的贡献定位模糊**
- 具体位置：Section 5.1 (p.6), Remark 1
- 问题：Remark 1 本质是 Data Processing Inequality 对 M→T→A→C Markov chain 的直接应用。论文在 Remark 1 文本中确实承认 DPI 是"a standard result"，贡献在于"identifying the Markov chain structure"。但在 Abstract 和 Introduction 中，Remark 1 被与 Observation 1 和 diagnostic framework 并列为主要贡献，给人以理论创新的印象。识别这条 Markov chain 是一个有用的 framing，但称不上独立的理论贡献——任何确定性后处理都满足 DPI，这个 Markov chain 结构对熟悉信息论的读者来说是显而易见的。
- 建议：在 Introduction 中降低 Remark 1 的权重，将其作为解释性工具而非独立贡献呈现；或者增加对 Markov 假设成立条件的实证讨论，使其贡献更实质。

**W2** [warning] **缺少常识推理基准（commonsense reasoning benchmarks）**
- 具体位置：Section 3.2 (p.4, Datasets)、Limitations (p.9)
- 问题：所有 4 个 benchmark 都是逻辑/数学推理（FOLIO、ProofWriter 为一阶逻辑，LogiQA 为逻辑，GSM8K/AIME 为数学）。论文声称 SCB 是"across domains"的现象，但未测试常识推理（如 StrategyQA、CommonsenseQA、ARC）。对于常识推理，约束提取的性质可能根本不同——约束可能更难形式化为 Z3 可处理的命题，SCB 的表现模式可能不同。
- 建议：在 Limitations 中明确承认这一空白，或补充至少一个常识推理数据集的实验。

**W3** [warning] **信息密度过高，Section 5 论述压缩过度**
- 具体位置：Section 5 (pp.5-7)
- 问题：Section 5 在约 2.5 页内覆盖了：(a) Symbolic Confirmation Bias 的定义与实证（5.1），(b) Remark 1 与 DPI 论证，(c) 所有 27 种 remediation 策略为何失败（5.2），(d) 三个诊断指标的定义与验证（5.3）。每个子话题都值得更充分的展开。特别是 5.2 仅用一段话概括了 27 种策略的四类失败模式（Figure 4），读者很难从主文中理解每种失败模式的细节——几乎完全依赖附录。5.3 的诊断框架（K_eff, BR, CCR 的定义、阈值选择、验证）也极度压缩。
- 建议：考虑将 Section 5 拆分为两个 section（SCB mechanism + Diagnostic framework），或将 remediation 分析整合到 §4 Results 中，以提升可读性。

**W4** [warning] **标题与 cross-architecture 正面结果之间的张力**
- 具体位置：Title、Section 6、Table 3
- 问题：标题 "Self-Extracted Constraints Provide No Detectable Improvement" 技术上是准确的（cross-architecture 使用外部 verifier，不是 self-extraction）。但对于非仔细阅读的读者，标题传达的信息是"symbolic constraints for LLM reasoning don't work"，而 Section 6 展示了 DeBERTa NLI verifier 在 ProofWriter 上可达 +12.67pp 增益（Table 3）。这种张力在 Abstract 最后一句才提及 cross-architecture escape，且仅用半句话。
- 建议：在标题或 Abstract 中更平衡地传达双重发现——既有否定结果，也有建设性的逃逸路径。例如标题可改为 "The Symbolic Mirage: Self-Extracted Constraints Cannot Improve LLM Reasoning, but Cross-Architecture Verification Can"（仅为方向性建议）。

**W5** [warning] **与 test-time compute / PRM 文献的关系讨论不足**
- 具体位置：Section 2 (p.3, "Test-time compute and self-verification")
- 问题：Section 2 提到 process reward models (PRMs) 和 outcome reward models (ORMs) 作为 test-time compute scaling 的方法，但仅一句话指出它们"operate outside the pipeline of Observation 1"。SICA 本质上也是一种 test-time verification 方法，读者会自然地问：为什么不用学习过的 PRM 而用 Z3？论文应更明确地讨论 formal symbolic verification vs. learned verification 的 trade-off——前者不需要训练数据但受限于 SCB，后者需要监督信号但可能逃逸 DPI bound。这个对比会强化论文的信息。
- 建议：在 Related Work 或 Discussion 中增加 1-2 句，明确将 SICA 定位在 formal vs. learned verification 的 landscape 中。

---

## 小问题（不影响接收）

- **术语 "Symbolic Mirage"** (Section 5 标题)：比典型学术用语更 dramatic。term 定义清晰且使用一致，但部分 reviewer 可能认为过于修辞化。建议考虑替换为更中性的措辞（如 "Symbolic Confirmation Effect"），但这不是硬性要求。
- **Abstract 字数**：估计 ~190-195 words，接近但未超过 200 word 限制。合规。
- **页数合规**：主文正文在 page 8 结尾处 Discussion 有约 1 行溢出到 page 9（Limitations 之前）。极为边缘，但技术上可能构成违规。建议微调排版确保 Discussion 在 page 8 内结束。
- **Figure 3 (p.7, Causal DAG)**：图很小，节点标签在打印时可能难以辨认。建议增大或简化。
- **Table 1 (p.5)**：脚注符号（†, *, **）较多且密集，首次阅读时需要反复查找脚注定义。
- **Appendix Z (Use of AI Assistants)**：完整披露使用 Claude (Anthropic) 进行代码/写作辅助，合规。

---

## 主要优势

1. **实验规模与统计严谨性**：9 个模型（4 个家族）、4 个 benchmark、27 种 training-free 变体、完整的统计分析工具链（FDR、TOST、bootstrap CI、permutation test、McNemar、power analysis）。这在 NLP 否定结果论文中极为少见，为结论的可信度提供了坚实基础。

2. **清晰且可操作的否定结果**：论文不仅展示"什么不工作"，还解释"为什么不工作"（SCB mechanism），并提供"怎样可能工作"（cross-architecture escape, §6）。这使论文对 practitioners 有直接实用价值。

3. **诊断框架的实用性**：K_eff、BR、CCR 三个零成本指标（Section 5.3）可在实际部署前预测 self-extraction 方法是否有效，无需完整评估。K=12 pilot run 的建议（Figure 6）降低了使用门槛。

4. **Oracle control 和 cross-architecture 实验设计精良**：Oracle-SICA（Appendix G）验证了 MAX-SAT 机制本身是有效的（ProofWriter +29.90pp），将问题锁定在约束质量而非聚合机制上。Cross-architecture NLI（§6, Table 3）提供了概念验证级别的逃逸证据。

5. **Appendix 深度**：20 页附录覆盖了 prompt 模板、27 种 remediation 策略的详细结果、case studies（Appendix F）、power analysis（Appendix D）、hyperparameter sensitivity（Appendix I）、constraint ablation（Appendix H）、cross-model analysis（Appendix O-Q）等。材料足以支撑独立验证。

---

## Questions for Authors

1. 在产生**少数票答案**的 trace 中，提取的约束更倾向于支持该 trace 的少数票答案，还是全局多数票答案？这是区分 SCB（聚合层面偏差）与 CoT bias（trace 层面偏差传递到约束）的关键测试。

2. 27 种 remediation 策略全部使用 zero-shot template extraction。是否考虑过 few-shot extraction 或 iterative refinement？如果未测试，"structural property"的断言基础是什么？

3. Remark 1 的 Markov 假设 M→T→A→C 中，"constraints are trace-determined" (σ_c = f(t_i)) 在什么条件下可能不成立？论文是否有实验证据表明此假设近似成立（如 trace perturbation 实验）？

4. Cross-architecture NLI 实验（§6）仅使用 DeBERTa-large 和 RoBERTa-large 作为 verifier，且限于逻辑推理任务。这种 capability-gap pattern 是否在数学推理（GSM8K）上也成立？

5. Table 6 (Appendix D) 显示 7/11 条件的 MDE > 5pp。对于这些低功效条件，论文的结论是否应限定为"未检测到显著效果"而非暗示等价性？

---

## Missing References

- **Wang et al. (2024), "Math-shepherd: Verify and reinforce LLMs step-by-step without human annotations"**: 与 SICA 的 step-level verification 思路直接相关，且使用了不同的验证范式（learned process reward model vs. formal Z3），比较能强化 formal vs. learned verification 的讨论。
- **Khalifa et al. (2023), "GRACE: Discriminator-guided chain-of-thought reasoning"**: 使用判别器引导 CoT，是 learned verification 的另一个相关 baseline。
- **Weng et al. (2023), "Large language models are better reasoners with self-verification"**: 论文引用列表中似乎已包含（p.10），但 Related Work 讨论中对其与 SICA 的关系阐述不足——Weng et al. 也做自验证但声称有效，与本文的否定结论形成直接对比，值得在 Section 2 详细讨论。

---

## Overall Assessment

**Score: 3.5 / 5 (Borderline Conference)**

这是一篇实验设计严谨、规模充分的否定结果论文，对 neuro-symbolic reasoning 和 LLM self-improvement 社区有重要的实践意义。论文正确地遵循了 ARR 对否定结果论文的指引——不仅展示失败，还提供了机制解释和诊断工具。

主要顾虑集中在两点：(1) "structural property" 断言在纯经验证据基础上过强，Remark 1 的 DPI 论证是教科书级别应用而非独立理论贡献；(2) SCB 作为独立于 CoT confirmation bias 的新概念，缺乏关键的实证分离测试。如果作者能在 rebuttal 中回答 Question 1（per-trace 分析）并弱化"structural"措辞，论文的可接收性将显著提高。

次要顾虑包括：信息密度过高导致部分论述被过度压缩、缺少常识推理基准、与 PRM/learned verification 文献的讨论不足。

**Confidence: 4/5** — 仔细阅读全文 28 页，熟悉 self-consistency、neuro-symbolic reasoning、LLM self-correction 领域。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2168 · 2026-05-23T20:20:18.524561+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "180",
  "reason": "等待 Reviewer 1 返回 Round 1 审稿报告",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: symb_invariant_consensus\n- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "180",
    "reason": "等待 Reviewer 1 返回 Round 1 审稿报告",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: symb_invariant_consensus\n- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 2169 · 2026-05-23T20:20:18.575234+00:00_

Next wakeup scheduled for 20:24:00 (in 222s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 2170 · 2026-05-23T20:20:25.064801+00:00_

Reviewer 2 已返回（3.5/5 Borderline Conference）。核心问题：(1) "structural property" 断言过强，(2) SCB 与 CoT confirmation bias 实证分离不足。等待 Reviewer 1 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 157

## Round 157

4 recorded events


### User

_source line 2171 · 2026-05-23T20:20:27.546567+00:00_

[Reviewer 2 审稿结果]:
审稿完成。

**评分：3.5/5 (Borderline Conference)**，核心判断：

- **两个 Must-Fix**：(1) "structural property" 断言超出纯经验证据所能支撑的范围，Remark 1 只是 DPI 的教科书应用；(2) SCB 与 CoT confirmation bias 的实证分离不充分——缺少对少数票 trace 中约束偏向的关键测试。
- **五个 Should-Fix**：Remark 1 贡献定位模糊、缺少常识推理基准、Section 5 信息密度过高、标题与 cross-architecture 正面结果的张力、与 PRM 文献讨论不足。
- **主要优势**：实验规模和统计严谨性在 NLP 否定结果论文中极为突出（9 模型 × 4 benchmark × 27 变体，完整的 FDR/TOST/bootstrap/permutation/power analysis 工具链），诊断框架有实用价值，oracle control 和 cross-architecture 实验设计精良。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2172 · 2026-05-23T20:20:35.304118+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "180",
  "reason": "继续等待 Reviewer 1 返回 Round 1 审稿报告",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: symb_invariant_consensus\n- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "180",
    "reason": "继续等待 Reviewer 1 返回 Round 1 审稿报告",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: symb_invariant_consensus\n- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 2173 · 2026-05-23T20:20:35.455321+00:00_

Next wakeup scheduled for 20:24:00 (in 205s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 151
}
```

</details>

---


### Assistant

_source line 2174 · 2026-05-23T20:20:36.947491+00:00_

Reviewer 2 报告已收录。仍在等待 Reviewer 1 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 158

## Round 158

10 recorded events


### User

_source line 2175 · 2026-05-23T20:21:22.617132+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性与实验有效性

**论文**: Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning
**Venue**: EMNLP 2026 (ARR)

---

## Summary

本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取逻辑约束并通过加权 MAX-SAT 聚合答案，旨在超越 Self-Consistency (SC) 的简单多数投票。核心发现是否定性的：在 6 个模型（7B–32B）× 4 个基准上，SICA 相对 SC 无可检测的改进（FDR 校正后无条件显著为正）。论文将此归因于 Symbolic Confirmation Bias（SCB）——自提取约束继承生成模型的分布先验，导致 MAX-SAT 退化为多数投票。文章提出三项贡献：(1) SCB 的诊断与机制解释，(2) 三个零成本诊断指标（BR, K_eff, ProcessSim），(3) 跨架构 NLI verifier 的初步突破证据。

---

## Strengths

**S1. 重要且及时的否定结果。** Self-consistency 是 LLM 推理中最广泛使用的聚合方法之一，理解其符号化扩展的局限性对社区具有实际价值。否定结果论文在顶会中偏少但非常需要，本文填补了这一空白。

**S2. 统计方法论严谨性突出。** 论文采用了完整的否定结果论证工具链：McNemar 配对检验测显著性差异、TOST ±2pp 等价检验确认无差异、BH FDR 校正处理多重比较、10,000 次 bootstrap 重采样计算置信区间、以及基于 McNemar discordant pairs 的 power analysis 报告最小可检测效应（Table 6）。这套统计框架远超该领域平均水平，是本文最大的方法论优势。

**S3. Oracle 对照实验设计精巧。** Appendix G 的 oracle 对照（用 FOLIO gold FOL annotations 和 ProofWriter DSL 替换自提取约束）产生了显著增益（Mistral-7B FOLIO +29.90pp, Qwen2.5-14B ProofWriter +17.17pp），有力地证明了 MAX-SAT 框架本身有效——瓶颈在于提取质量而非聚合机制。这种 "framework works, extraction fails" 的对照设计是本文论证逻辑的关键支柱。

**S4. SCB 机制诊断清晰且可操作。** BR（Bias Ratio）、K_eff（有效样本量）、ProcessSim（过程相似度）三个零成本诊断指标构成了一个实用的预判工具：BR > 2 → 约束偏向多数票、K_eff < 3.62 → 聚合退化、ProcessSim > 0.6 → 推理路径同质化。§5.3 的决策边界在 K=12 pilot 上实现了跨模型泛化验证（held-out: LLaMA-3.1-8B, Qwen3-14B），具备部署前筛查的实用价值。

**S5. 实验覆盖度在约束提取范式内是充分的。** 27 个 training-free 变体（9 prompt-level × 3 method-level，Table 12-14）覆盖了退化型、多样性受限型、确认偏差型四大类，包括迭代精炼、选择性弃权、交叉模型提取、DPP 多样性采样等。在约束提取范式内，该穷举是系统性的。

**S6. 写作清晰、结构紧凑。** 否定结果 + 机制解释 + 诊断框架 + 突破方向的叙事弧完整。正文 8 页内信息密度高，附录提供了充分的细节支撑。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Contribution 3（Cross-architecture escape, §6）的证据强度不足以支撑主贡献声明

- **具体位置**: §6, Table 3, Table 4, Figure 8（Appendix V）
- **问题**: 论文将"跨架构 NLI verifier 可突破 self-extraction bound"列为三大贡献之一，但支撑证据存在多重局限：
  - (a) Capability-gap pattern 基于 **n=6 的 Spearman rank correlation**（6 个 generator-verifier 对的 SC 排序），这在统计上极不稳健——6 个数据点几乎任何单调趋势都会产生显著相关；
  - (b) 仅测试了**单一 verifier 架构**（DeBERTa-large-mnli），且该模型经过 MNLI 域内微调，因此观测到的增益部分来自域适配而非纯粹的架构独立性；
  - (c) 实验为 **K=12 pilot run**，作者自己在 Limitations 中承认"We do not evaluate trained extractors"；
  - (d) 增益仅在 generator SC < 72% 时显著（Table 3），这一阈值基于 6 个点拟合，泛化性未知。
- **为什么影响接收**: 三大贡献中有一个基于探索性证据（pilot-scale, single-architecture, n=6 correlation），与 Contribution 1-2 的严谨程度不匹配。审稿人和读者会质疑这是否足以构成独立贡献。
- **建议修改方向**: (1) 将 Contribution 3 显式降级为 "exploratory finding / future direction"，在 abstract 和 §1 中明确标注 "preliminary evidence"；或 (2) 补充至少 2-3 种 verifier 架构（如 RoBERTa-MNLI, BART-MNLI, 或非 NLI 的 verifier 如 reward model）和更多 generator-verifier 组合以加强 n。

**N2** [critical] Remark 1（Self-Extraction Bound）的理论贡献被高估——DPI bound 是平凡结论

- **具体位置**: §5.1, Remark 1, 以及 §7 Discussion 中引用该 bound 作为解释
- **问题**: Remark 1 声称"If constraints are trace-determined (c_i = f(t_i)), the data processing inequality gives I(C;Y) ≤ I(T;Y)"，并称之为 "Self-Extraction Bound"。但这是 DPI 对**任何确定性后处理**都成立的平凡结论——对任意函数 g，I(g(X);Y) ≤ I(X;Y) 恒成立。将其命名为 "bound" 并赋予 Remark 编号暗示了理论新颖性，但实际信息量为零。
  - 更关键的是，**DPI 不能解释 SICA 为何失败**。DPI 说约束的信息量不超过 traces，但 majority voting 只使用 argmax(answer frequencies)，而 MAX-SAT 使用约束的满足性结构。即使 I(C;Y) ≤ I(T;Y)，MAX-SAT 仍可能从相同信息中提取比简单计数更有用的投影。真正解释 SICA 退化的是经验发现（BR > 1, |C'| ≈ 0, degeneration condition Eq. 4），而非 DPI。
  - 论文确实在 Remark 1 后注释 "This is an empirical conclusion holding under degeneration, not an unconditional structural claim"——但 Remark 的标题 "Self-Extraction Bound" 和正文中多处引用（§7: "the DPI bound (Remark 1) applies to any deterministic self-extraction"）传达的信号与此限定不一致。
- **为什么影响接收**: 形式化应当增加论文的理论深度，而非制造深度的表象。审稿人熟悉 DPI 的读者会立即识别出这是平凡应用，削弱论文的可信度。
- **建议修改方向**: (1) 移除 "Self-Extraction Bound" 命名，将 Remark 1 改为对 DPI 的简短引用（一句话即可），明确说明 "this is a necessary condition, not a sufficient explanation"；(2) 将论证重心放在经验发现（Observation 1 + BR + degeneration condition）上作为 SICA 退化的实际解释。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 否定结果的普遍性声明强于统计证据支撑范围

- **具体位置**: Title, Abstract ("no detectable improvement"), Table 6
- **问题**: 标题 "Self-Extracted Constraints Provide No Detectable Improvement" 是一个普遍声明，但 Table 6 的 power analysis 显示：仅 4 个条件（n ≥ 200）通过了 TOST ±2pp 等价检验确认无差异；其余 7 个条件中，MDE 超过 5pp，无法排除中等效应的存在。论文在正文中确实区分了 "confirmatory" 和 "underpowered" 条件（§4, Limitations），但标题和 abstract 第一句未做此区分。
- **建议**: 在 abstract 中更早限定："across four confirmatory conditions (n ≥ 200)"，或在标题中加限定词如 "in tested conditions"。

**W2** [warning] Seed replication（3-4 seeds）对 null-result claim 的支撑偏弱

- **具体位置**: §3.2 Parameters, Table 1
- **问题**: 论文使用 3-4 个随机种子，每个种子产生 K=12 traces。McNemar 检验将 problem × seed 作为独立观测单元，但同一问题跨种子的回答存在相关性（同一模型在同一问题上的推理倾向一致）。这一相关性未被建模，可能导致有效样本量小于名义值。对于否定结果声明（需要比正面结果更强的证据），3-4 seeds 较为边缘。
- **建议**: 增加对跨种子相关性的讨论或敏感性分析（例如，per-seed McNemar 结果是否一致）。

**W3** [warning] GSM8K (n=30) 和 AIME (n=22) 对论证几乎无贡献

- **具体位置**: §3.2, Table 1 底部
- **问题**: 这两个数据集的样本量极小，McNemar 检验功效极低（MDE 远超 10pp），且被用于"probe the degenerate regime"——但退化现象在大样本数据集上已经充分展示。它们的存在可能给读者一种覆盖更广的错觉（"4 benchmarks"），而实际分析价值有限。
- **建议**: 在 abstract/introduction 中明确区分 "2 confirmatory benchmarks (FOLIO, ProofWriter) + 2 pilot benchmarks (GSM8K, AIME)"，或将 GSM8K/AIME 结果整体移至 appendix。

**W4** [warning] BR 的 permutation null model 描述不足

- **具体位置**: §3.1 Bias ratio (Eq. 5), §5.1
- **问题**: 论文声称 "We validate chance coupling beyond chance. BR = 1 indicates no coupling beyond chance" 并使用 permutation null model，但 permutation 的具体构造方式（是在同一问题内跨 traces 打乱 constraint-answer 关联，还是跨问题打乱？）未在正文或附录中充分描述。Permutation 范围直接影响 null distribution 和 p-value 的解释。
- **建议**: 在 §5.1 或附录中补充 permutation 步骤的伪代码或详细描述。

**W5** [warning] Observation 1 的 "approximately uniform constraint yield" 假设缺乏敏感性分析

- **具体位置**: §5.1 Observation 1, 条件 (ii)
- **问题**: Observation 1 的退化结论依赖于 "approximately uniform constraint yield per trace within each answer group"。论文在 Table 11（Appendix K）提供了经验支持，但未分析当此假设违反时（如某些 traces 产出显著更多约束）退化结论是否仍成立。如果高质量 traces 系统性地产出更多约束，SICA 可能通过约束数量差异隐式地进行质量加权，而非简单退化为多数投票。
- **建议**: 补充 constraint yield 变异系数（CV）分析，或构造 yield-skewed 的反例测试 Observation 1 的鲁棒性。

---

## 小问题（不影响接收）

- §3.1 Eq. 3 中 α = 0.5 的选择缺乏 justification。虽然 Appendix I 分析了 K 和 T 的敏感性，但未分析 α。鉴于 degeneration condition 下 α 影响不大（|C'| ≈ 0 时 penalty term 消失），可在 footnote 中简短说明。
- Figure 2 ("regime structure") 的三区划分（Type A/B/C）阈值（SC ≤ 40%, 40-60%, ≥ 60%）看起来是 post-hoc 确定的，建议说明是否经过交叉验证或基于先验。
- §2 Related Work 的 "Distinction from CoT confirmation bias" 段落可更精炼——当前版本在区分 SCB 和 CoT confirmation bias 时有些冗余。
- Table 1 中部分条件的 bootstrap CI 跨越零（如 Qwen2.5-7B FOLIO: [-1.50, +1.50]），但对应 TOST 结果未报告——建议在附录中补充所有条件的 TOST 结果。

---

## Questions for Authors

**Q1.** K=12 traces 是否可能不足以让 MAX-SAT 的约束交叉验证机制发挥作用？如果 K=50 或 K=100，degeneration condition（|C'| ≈ 0）是否仍成立？Appendix I.1 的 K-sensitivity 只测到 K=20，是否可以补充更大 K 的实验？

**Q2.** BR 在高精度模型上（SC > 90%）估计不稳定（n_maj 很小），这些条件下的 BR 值是否应排除在 cross-model 结论之外？

**Q3.** 27 个 training-free 变体聚焦于约束提取范式内部。如果将 Self-Consistency 与非约束的 self-improvement 方法（如 Self-Refine 的多轮迭代、Self-Debate 的对抗验证）组合，SCB 是否同样适用？这些方法是否超出了本文的 scope？

**Q4.** Cross-model extraction（Table 2, Mistral-7B 提取其他模型 traces 的 FOL）仍然产生 BR > 1。如果反过来——用更强的模型（如 GPT-4）作为 extractor 提取弱模型 traces 的约束——结果是否不同？论文的 Markov chain 论证预测不会改变（因为 SCB 是 trace-answer coupling 的属性），但这值得实验验证。

---

## Missing References

- **Universal Self-Consistency** (Chen et al., 2024, "Universal self-consistency for large language model generation") — 论文引用了此工作但未在 Related Work 中与 SICA 的区别进行充分讨论。USC 使用 LLM 自身作为 selector 而非约束求解器，两者的 failure mode 是否相同（均受 SCB 影响）值得讨论。
- **Self-Debate** (Liang et al., 2024 or Du et al., 2023, multi-agent debate) — 作为 training-free self-improvement 的一个重要类别，论文的 27 变体中未包含 debate-style 方法。即使超出 scope，也应在 Related Work 中说明排除理由。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法论严谨（TOST/FDR/bootstrap/power analysis），但 Remark 1 的理论贡献为平凡 DPI 应用，Contribution 3 的证据（n=6 correlation, single verifier）不足以支撑主贡献声明 |
| Excitement | 3.5/5 | 否定结果对社区有实际价值（预防无效方法的投入），诊断框架（BR/K_eff/ProcessSim）具备实用性，但 excitement 受限于结论的保守性——论文证明了什么不行，但对什么能行的指引有限 |
| Reproducibility | 4/5 | 实验设置详尽（Appendix A-B 提供完整 prompt templates, Algorithm 1-2 可复现），代码承诺开源，但当前版本代码/数据未附带 |
| Overall Assessment | **3.5** (Borderline Conference) | 一篇方法论严谨的否定结果论文，诊断框架有实际价值，但两个关键问题拖累整体：(1) Contribution 3 的证据强度不匹配主贡献声明，(2) Remark 1 的理论包装掩盖了平凡的 DPI 应用。如果 Contribution 3 被降级为 exploratory finding 并且 Remark 1 的呈现更诚实，Soundness 可上调至 4，整体可达 Conference 水平 |
| Confidence | 4/5 | 我仔细检查了所有方程、统计方法、实验设计和附录。对 DPI/TOST/McNemar/MAX-SAT 的技术细节有把握。 |

---

## 总体评分

**Overall**: 3.5 — Borderline Conference

**一句话总结**: 统计方法论一流的否定结果论文，SCB 诊断框架有实用价值，但 Contribution 3 证据不足且 Remark 1 的理论包装大于实质，需要调整贡献声明的粒度与证据的匹配度。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2176 · 2026-05-23T20:21:45.617508+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2177 · 2026-05-23T20:21:45.617962+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2178 · 2026-05-23T20:22:19.477099+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每条 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Must-Fix\n\n**N1** [critical] **\"Structural property\" 断言超出实证支撑**\n- Abstract (\"a structural property of self-extraction pipelines\")、Section 5.1、Section 7\n- Remark 1 的 DPI 论证仅建立信息上界 I(C;Y) ≤ I(T;Y)，未证明上界必然紧。27 种 remediation 策略均属同一类型（zero-shot template extraction），Appendix Y 自己承认 few-shot/iterative refinement 可能不同。如果未测试的提取策略能打破 M→T→A→C Markov 假设，\"structural property\" 就不成立。\n- 建议改为 \"robust empirical regularity\" 或 \"persistent pattern\"。\n\n**N2** [critical] **SCB 与 CoT confirmation bias 的实证分离不充分**\n- Section 2 \"Distinction from CoT confirmation bias\"、Section 5.1\n- 缺少关键分离测试：在少数票答案的 trace 中，提取的约束支持该 trace 自身的少数票答案（CoT bias 预测），还是全局多数票答案（SCB 预测）？BR 指标展示整体约束偏向多数票，但这与 \"CoT bias 在 trace 层面运作、通过聚合传递\" 的解释同样一致。Appendix O 的 process similarity 分析是间接证据，不在主文中，且非决定性。\n- 建议在主文增加 per-trace 少数票分析。\n\n### Should-Fix\n\n**W1** [warning] **Remark 1 (DPI bound) 贡献定位模糊** — DPI 是教科书级应用，识别 M→T→A→C Markov chain 是有用的 framing 但称不上独立理论贡献。建议降低 Remark 1 在 Introduction 中的权重。\n\n**W2** [warning] **缺少常识推理基准** — 4 个 benchmark 均为逻辑/数学推理，未测试常识推理（StrategyQA, CommonsenseQA, ARC）。论文声称 \"across domains\" 但域覆盖有限。\n\n**W3** [warning] **Section 5 信息密度过高** — 约 2.5 页内覆盖 SCB 定义、DPI 论证、27 种 remediation 失败、三个诊断指标。5.2 仅一段概括 27 种策略的四类失败模式，几乎完全依赖附录。\n\n**W4** [warning] **标题与 cross-architecture 正面结果的张力** — \"No Detectable Improvement\" 技术上准确但对非仔细阅读的读者传达 \"symbolic constraints don't work\" 的信息，而 §6 展示 DeBERTa NLI 在 ProofWriter 上 +12.67pp。\n\n**W5** [warning] **与 PRM/learned verification 文献讨论不足** — SICA 也是 test-time verification，应更明确讨论 formal vs. learned verification 的 trade-off。\n\n### Questions\n1. 少数票 trace 中约束偏向少数票还是全局多数票？\n2. 27 种策略全部 zero-shot template extraction，是否考虑过 few-shot 或 iterative refinement？\n3. Remark 1 的 Markov 假设在什么条件下不成立？\n4. Cross-architecture NLI 实验仅 DeBERTa-large 和 RoBERTa-large，capability-gap 在数学推理上成立吗？\n5. 7/11 低功效条件的结论是否应限定为\"未检测到显著效果\"？\n\n### Missing References\n- Wang et al. (2024) \"Math-shepherd\"\n- Khalifa et al. (2023) \"GRACE\"\n- Weng et al. (2023) self-verification 与 SICA 否定结论的对比讨论不足\n\n---\n\n请对以上每条 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，并说明理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每条 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Must-Fix\n\n**N1** [critical] **\"Structural property\" 断言超出实证支撑**\n- Abstract (\"a structural property of self-extraction pipelines\")、Section 5.1、Section 7\n- Remark 1 的 DPI 论证仅建立信息上界 I(C;Y) ≤ I(T;Y)，未证明上界必然紧。27 种 remediation 策略均属同一类型（zero-shot template extraction），Appendix Y 自己承认 few-shot/iterative refinement 可能不同。如果未测试的提取策略能打破 M→T→A→C Markov 假设，\"structural property\" 就不成立。\n- 建议改为 \"robust empirical regularity\" 或 \"persistent pattern\"。\n\n**N2** [critical] **SCB 与 CoT confirmation bias 的实证分离不充分**\n- Section 2 \"Distinction from CoT confirmation bias\"、Section 5.1\n- 缺少关键分离测试：在少数票答案的 trace 中，提取的约束支持该 trace 自身的少数票答案（CoT bias 预测），还是全局多数票答案（SCB 预测）？BR 指标展示整体约束偏向多数票，但这与 \"CoT bias 在 trace 层面运作、通过聚合传递\" 的解释同样一致。Appendix O 的 process similarity 分析是间接证据，不在主文中，且非决定性。\n- 建议在主文增加 per-trace 少数票分析。\n\n### Should-Fix\n\n**W1** [warning] **Remark 1 (DPI bound) 贡献定位模糊** — DPI 是教科书级应用，识别 M→T→A→C Markov chain 是有用的 framing 但称不上独立理论贡献。建议降低 Remark 1 在 Introduction 中的权重。\n\n**W2** [warning] **缺少常识推理基准** — 4 个 benchmark 均为逻辑/数学推理，未测试常识推理（StrategyQA, CommonsenseQA, ARC）。论文声称 \"across domains\" 但域覆盖有限。\n\n**W3** [warning] **Section 5 信息密度过高** — 约 2.5 页内覆盖 SCB 定义、DPI 论证、27 种 remediation 失败、三个诊断指标。5.2 仅一段概括 27 种策略的四类失败模式，几乎完全依赖附录。\n\n**W4** [warning] **标题与 cross-architecture 正面结果的张力** — \"No Detectable Improvement\" 技术上准确但对非仔细阅读的读者传达 \"symbolic constraints don't work\" 的信息，而 §6 展示 DeBERTa NLI 在 ProofWriter 上 +12.67pp。\n\n**W5** [warning] **与 PRM/learned verification 文献讨论不足** — SICA 也是 test-time verification，应更明确讨论 formal vs. learned verification 的 trade-off。\n\n### Questions\n1. 少数票 trace 中约束偏向少数票还是全局多数票？\n2. 27 种策略全部 zero-shot template extraction，是否考虑过 few-shot 或 iterative refinement？\n3. Remark 1 的 Markov 假设在什么条件下不成立？\n4. Cross-architecture NLI 实验仅 DeBERTa-large 和 RoBERTa-large，capability-gap 在数学推理上成立吗？\n5. 7/11 低功效条件的结论是否应限定为\"未检测到显著效果\"？\n\n### Missing References\n- Wang et al. (2024) \"Math-shepherd\"\n- Khalifa et al. (2023) \"GRACE\"\n- Weng et al. (2023) self-verification 与 SICA 否定结论的对比讨论不足\n\n---\n\n请对以上每条 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，并说明理由。"
  }
}
```

</details>

---


### Tool result

_source line 2179 · 2026-05-23T20:22:50.337394+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30860
}
```

</details>

---


### Tool call

_source line 2180 · 2026-05-23T20:22:50.489087+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每条 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Must-Fix\n\n**N1** [critical] **Contribution 3（Cross-architecture escape, §6）的证据强度不足以支撑主贡献声明**\n- §6, Table 3, Table 4, Figure 8（Appendix V）\n- 多重局限：(a) Capability-gap pattern 基于 n=6 Spearman rank correlation，统计上极不稳健；(b) 仅测试单一 verifier 架构（DeBERTa-large-mnli），增益部分来自域适配；(c) 实验为 K=12 pilot run；(d) 增益仅在 SC < 72% 时显著，阈值基于 6 个点拟合。\n- 建议将 Contribution 3 降级为 \"exploratory finding / future direction\"，或补充 2-3 种 verifier 架构。\n\n**N2** [critical] **Remark 1（Self-Extraction Bound）的理论贡献被高估——DPI bound 是平凡结论**\n- §5.1, Remark 1, §7 Discussion\n- DPI 对任何确定性后处理都成立（I(g(X);Y) ≤ I(X;Y)），命名为 \"Self-Extraction Bound\" 暗示理论新颖性但实际信息量为零。更关键的是，DPI 不能解释 SICA 为何失败——MAX-SAT 可能从相同信息中提取比简单计数更有用的投影。真正解释退化的是经验发现（BR > 1, |C'| ≈ 0, degeneration condition）。\n- 建议移除 \"Self-Extraction Bound\" 命名，将 Remark 1 改为一句话 DPI 引用，重心放在经验发现上。\n\n### Should-Fix\n\n**W1** [warning] **否定结果的普遍性声明强于统计证据** — 标题 \"No Detectable Improvement\" 是普遍声明，但仅 4 个条件通过 TOST ±2pp 等价检验，7 个条件 MDE > 5pp。标题和 abstract 未区分 confirmatory vs underpowered conditions。\n\n**W2** [warning] **Seed replication（3-4 seeds）对 null-result claim 偏弱** — 同一问题跨种子的回答存在相关性，未被建模。3-4 seeds 对否定结果声明较为边缘。\n\n**W3** [warning] **GSM8K (n=30) 和 AIME (n=22) 对论证几乎无贡献** — 样本量极小，McNemar 检验功效极低（MDE 远超 10pp）。建议明确区分 \"2 confirmatory + 2 pilot benchmarks\" 或将 GSM8K/AIME 移至 appendix。\n\n**W4** [warning] **BR permutation null model 描述不足** — 是在同一问题内跨 traces 打乱还是跨问题打乱？Permutation 范围直接影响 null distribution 和 p-value 的解释。\n\n**W5** [warning] **Observation 1 的 \"approximately uniform constraint yield\" 假设缺乏敏感性分析** — 未分析当假设违反时（某些 traces 产出显著更多约束）退化结论是否仍成立。如果高质量 traces 系统性地产出更多约束，SICA 可能通过约束数量差异隐式质量加权。\n\n### Questions\n1. K=12 是否可能不足以让 MAX-SAT 机制发挥作用？K=50/100 时 degeneration 仍成立吗？\n2. BR 在 SC > 90% 时估计不稳定，这些条件的 BR 是否应排除？\n3. 27 变体聚焦约束提取范式。Self-Refine/Self-Debate 等非约束方法是否超出 scope？\n4. 用更强模型（GPT-4）作为 extractor 提取弱模型 traces 的约束，结果是否不同？\n\n### Missing References\n- Universal Self-Consistency (Chen et al., 2024) — 与 SICA 的区别讨论不足\n- Self-Debate (Liang et al., 2024 / Du et al., 2023) — 27 变体中未包含 debate-style 方法\n\n---\n\n请对以上每条 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，并说明理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每条 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Must-Fix\n\n**N1** [critical] **Contribution 3（Cross-architecture escape, §6）的证据强度不足以支撑主贡献声明**\n- §6, Table 3, Table 4, Figure 8（Appendix V）\n- 多重局限：(a) Capability-gap pattern 基于 n=6 Spearman rank correlation，统计上极不稳健；(b) 仅测试单一 verifier 架构（DeBERTa-large-mnli），增益部分来自域适配；(c) 实验为 K=12 pilot run；(d) 增益仅在 SC < 72% 时显著，阈值基于 6 个点拟合。\n- 建议将 Contribution 3 降级为 \"exploratory finding / future direction\"，或补充 2-3 种 verifier 架构。\n\n**N2** [critical] **Remark 1（Self-Extraction Bound）的理论贡献被高估——DPI bound 是平凡结论**\n- §5.1, Remark 1, §7 Discussion\n- DPI 对任何确定性后处理都成立（I(g(X);Y) ≤ I(X;Y)），命名为 \"Self-Extraction Bound\" 暗示理论新颖性但实际信息量为零。更关键的是，DPI 不能解释 SICA 为何失败——MAX-SAT 可能从相同信息中提取比简单计数更有用的投影。真正解释退化的是经验发现（BR > 1, |C'| ≈ 0, degeneration condition）。\n- 建议移除 \"Self-Extraction Bound\" 命名，将 Remark 1 改为一句话 DPI 引用，重心放在经验发现上。\n\n### Should-Fix\n\n**W1** [warning] **否定结果的普遍性声明强于统计证据** — 标题 \"No Detectable Improvement\" 是普遍声明，但仅 4 个条件通过 TOST ±2pp 等价检验，7 个条件 MDE > 5pp。标题和 abstract 未区分 confirmatory vs underpowered conditions。\n\n**W2** [warning] **Seed replication（3-4 seeds）对 null-result claim 偏弱** — 同一问题跨种子的回答存在相关性，未被建模。3-4 seeds 对否定结果声明较为边缘。\n\n**W3** [warning] **GSM8K (n=30) 和 AIME (n=22) 对论证几乎无贡献** — 样本量极小，McNemar 检验功效极低（MDE 远超 10pp）。建议明确区分 \"2 confirmatory + 2 pilot benchmarks\" 或将 GSM8K/AIME 移至 appendix。\n\n**W4** [warning] **BR permutation null model 描述不足** — 是在同一问题内跨 traces 打乱还是跨问题打乱？Permutation 范围直接影响 null distribution 和 p-value 的解释。\n\n**W5** [warning] **Observation 1 的 \"approximately uniform constraint yield\" 假设缺乏敏感性分析** — 未分析当假设违反时（某些 traces 产出显著更多约束）退化结论是否仍成立。如果高质量 traces 系统性地产出更多约束，SICA 可能通过约束数量差异隐式质量加权。\n\n### Questions\n1. K=12 是否可能不足以让 MAX-SAT 机制发挥作用？K=50/100 时 degeneration 仍成立吗？\n2. BR 在 SC > 90% 时估计不稳定，这些条件的 BR 是否应排除？\n3. 27 变体聚焦约束提取范式。Self-Refine/Self-Debate 等非约束方法是否超出 scope？\n4. 用更强模型（GPT-4）作为 extractor 提取弱模型 traces 的约束，结果是否不同？\n\n### Missing References\n- Universal Self-Consistency (Chen et al., 2024) — 与 SICA 的区别讨论不足\n- Self-Debate (Liang et al., 2024 / Du et al., 2023) — 27 变体中未包含 debate-style 方法\n\n---\n\n请对以上每条 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT]，并说明理由。"
  }
}
```

</details>

---


### Tool result

_source line 2181 · 2026-05-23T20:22:51.801995+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1312
}
```

</details>

---


### Tool call

_source line 2182 · 2026-05-23T20:23:03.014512+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "270",
  "reason": "等待 Reviewer 1 和 Reviewer 2 完成交叉分享回应",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: symb_invariant_consensus\n- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "270",
    "reason": "等待 Reviewer 1 和 Reviewer 2 完成交叉分享回应",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: symb_invariant_consensus\n- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 2183 · 2026-05-23T20:23:03.065164+00:00_

Next wakeup scheduled for 20:27:00 (in 237s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 2184 · 2026-05-23T20:23:04.557780+00:00_

交叉分享已派发：
- Reviewer 1 收到 Reviewer 2 的完整审稿意见，正在逐条回应
- Reviewer 2 收到 Reviewer 1 的完整审稿意见，正在逐条回应

等待两位 Reviewer 返回交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 159

## Round 159

4 recorded events


### User

_source line 2185 · 2026-05-23T20:23:07.040411+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审查结论**：Overall 3.5（Borderline Conference）。两个 Must-Fix 问题：
1. **Contribution 3（跨架构 escape）证据不足**——n=6 rank correlation、单一 DeBERTa verifier、K=12 pilot，不应作为主贡献声明
2. **Remark 1（DPI bound）是平凡结论**——任何确定性后处理都满足 DPI，真正解释 SICA 退化的是经验发现（BR > 1, degeneration condition），而非信息论 bound

核心优势在于统计方法论（TOST/FDR/bootstrap/power analysis）远超领域平均水平，oracle 对照实验设计精巧，SCB 诊断框架有实用部署价值。若 Contribution 3 降级为 exploratory finding 且 Remark 1 表述更诚实，可上调至 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2186 · 2026-05-23T20:23:15.313248+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "180",
  "reason": "等待 Reviewer 1 和 Reviewer 2 的交叉分享回应",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: symb_invariant_consensus\n- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "180",
    "reason": "等待 Reviewer 1 和 Reviewer 2 的交叉分享回应",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: symb_invariant_consensus\n- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 2187 · 2026-05-23T20:23:15.363853+00:00_

Next wakeup scheduled for 20:27:00 (in 225s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 2188 · 2026-05-23T20:23:19.817606+00:00_

Reviewer 1 初审报告已收录。仍在等待两位 Reviewer 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 160

## Round 160

4 recorded events


### User

_source line 2189 · 2026-05-23T20:25:05.648031+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 回应

### R2-N1: "Structural property" 断言超出实证支撑

**[AGREE]** R2-N1: 同意 "structural property" 一词过强，但论文的经验证据比 R2 所述更有力。

**理由**: R2 正确指出 Remark 1 的 DPI 论证仅是平凡上界，不足以支撑 "structural" 的声明——这与我自己的 N2 一致。但 R2 将论文的证据简化为 "仅 DPI + 27 种同类策略" 低估了论文的实际论证链：

1. 论文提供了 **Observation 1（Argmax Preservation）** + **Eq. 4（Degeneration Condition）** + **BR > 1 across all 9 models** (Table 1, Table 2) + **|C'| ≈ 0 empirically**（§5.1: Z3 rejection rate ≈ 0）——这些共同构成了一个多层经验论证，远超单纯的 DPI 引用。
2. **Oracle 对照**（Appendix G: gold FOL/DSL 约束产生 +17–30pp 增益）证明框架本身有效，锁定瓶颈在提取质量——这是"提取是问题，不是聚合"的强证据。
3. **Cross-model extraction**（Table 2: Mistral-7B 提取其他模型 traces 的 FOL）仍产生 BR > 1，说明 SCB 不是特定 extractor 的 artifact。

但我同意 R2 的核心论点：Appendix Y 自己承认 few-shot/iterative refinement 可能打破 Markov 假设（因为引入了外部信号或多轮信息），这意味着 SCB 的适用边界未被充分界定。**"structural property" 应改为 "robust empirical regularity under zero-shot template extraction"**，因为 "structural" 暗示数学必然性，而论文的证据是经验性的。

---

### R2-N2: SCB 与 CoT confirmation bias 的实证分离不充分

**[AGREE]** R2-N2: 这是一个真正的分析缺口，我在自己的审稿中未充分识别。

**理由**: R2 提出的分离测试精准且可操作——在少数票（正确答案）trace 中，约束是支持 **该 trace 自身的少数票答案**（→ CoT bias 在 trace 层面运作）还是 **全局多数票答案**（→ SCB 是超越 trace 层面的聚合偏差）？

论文当前的 BR 指标（Eq. 5）条件于 a_M ≠ a*（多数票错误），计算所有约束对多数票 vs 正确答案的支持比。但这个 **aggregate-level** 度量无法区分两个假说：

- **假说 A（CoT bias 传播）**: 每条 trace 的约束忠实支持该 trace 自身的答案 → 多数 traces 答案错误 → 聚合后约束自然偏向多数错误答案。BR > 1 是 CoT bias 在 trace 层面的直接后果。
- **假说 B（SCB 是独立现象）**: 约束存在 **跨 trace 的系统偏差**——即使从少数票 trace 中提取的约束也偏向全局多数票答案，超越了该 trace 自身的推理。

论文在 §2 中声称 "SCB operates at the aggregation level"，但 **未提供假说 A vs B 的分离证据**。Appendix O 的 ProcessSim 分析（TF-IDF 过程相似度）是间接的——高过程相似度说明 traces 同质化，但不直接回答 per-trace 约束指向。

**建议补充分析**: 对于 a_M ≠ a* 的问题，计算少数票 trace 中约束支持 **自身答案** vs **全局多数票答案** 的比例。若前者 >> 后者，则 SCB 可被约化为 CoT bias 传播；若后者 ≥ 前者，则 SCB 存在 trace 层面 CoT bias 之外的独立机制。这个分析只需对现有数据做条件筛选，无需新实验。

---

## Should-Fix 回应

### R2-W1: Remark 1 (DPI bound) 贡献定位模糊

**[AGREE]** R2-W1: 与我的 N2 完全一致。DPI bound 是教科书级应用（∀ deterministic f, I(f(X);Y) ≤ I(X;Y)），命名为 "Self-Extraction Bound" 制造了不存在的理论贡献。M→T→A→C Markov chain 作为分析框架有用，但 Remark 1 本身应降权——在 Introduction 中一句话带过即可，不应作为独立编号的 Remark。

---

### R2-W2: 缺少常识推理基准

**[REBUT]** R2-W2: 论文的域选择是策略性的 "best-case scenario" 设计，缺少常识推理基准不构成显著缺陷。

**反驳证据**:
- 论文在 Limitations（p.9）中明确说明："All benchmarks are English logical reasoning. FOLIO and ProofWriter represent a best-case scenario for symbolic verification: problems are designed to have clean first-order logic representations"。
- SICA 的核心机制依赖于约束可以被形式化为 Z3 可处理的逻辑公式。在常识推理任务上（StrategyQA, CSQA），约束提取的质量只会更差（因为常识知识难以形式化为 first-order logic），SCB 只会更严重。
- 因此，**在最有利条件下证明失败** 比在不利条件下证明失败更有说服力——这是 "best-case falsification" 的标准论证策略。

**但我同意一个限定**：论文在 abstract 中使用 "four benchmarks" 而不加限定，可能给读者 "跨域泛化" 的印象。建议在 abstract 中明确 "four logical/mathematical reasoning benchmarks"。

---

### R2-W3: Section 5 信息密度过高

**[AGREE]** R2-W3: §5.2 确实过度压缩。一段话概括 27 种策略的四类失败模式，读者无法在正文中获得任何具体策略的细节。

**但有保留**: 论文已处于 8 页上限，压缩是不得已。建议的折中方案是在 §5.2 中至少展开 **两个代表性失败案例**（如一个 degenerate 类、一个 diversity-limited 类），用 2-3 行解释失败机制，而非仅列类别名称。将现有 §5.2 的部分诊断指标细节移至附录可腾出空间。

---

### R2-W4: 标题与 cross-architecture 正面结果的张力

**[REBUT]** R2-W4: 标题的限定词 "Self-Extracted Constraints" 已准确界定了否定结论的范围，§6 的正面结果不在此范围内。

**反驳证据**:
- 标题是 "**Self-Extracted** Constraints Provide No Detectable Improvement"——关键词是 "self-extracted"。
- §6 的 DeBERTa NLI 实验使用的是 **跨架构验证**（外部 verifier），这打破了 self-extraction 的定义边界（Remark 1 的 trace-determined 假设不再成立）。论文在 §6 开头明确说明："We test whether a structurally independent verifier... can break the self-extraction bound"。
- 因此标题是技术上准确的：在 self-extraction 范围内确实无改进；§6 展示的改进来自 **超越** self-extraction。

**但我同意存在传播风险**：非仔细阅读的读者（如浏览 proceedings 目录）可能将标题解读为 "symbolic constraints 整体无用"。建议在 abstract 中更突出 §6 的正面结果，平衡否定信号。不过这不构成标题需要修改的理由。

---

### R2-W5: 与 PRM/learned verification 文献讨论不足

**[AGREE]** R2-W5: 论文在 §2 Related Work 中提到了 reward models（"outcome and process reward models"）和 self-verification，但未系统讨论 **formal verification vs. learned verification** 的 trade-off。

- SICA 本质上是 test-time formal verification（Z3 求解器 + 逻辑约束），而 PRM/ORM 是 learned verification（训练打分模型）。两者的 failure mode 不同：SICA 受 SCB 限制（约束与 traces 耦合），PRM 受训练分布限制（OOD 泛化）。
- 论文的诊断框架（BR, K_eff, CCR）原则上可以适用于 learned verifiers——例如，一个 PRM 是否也存在 "偏向多数票推理过程" 的确认偏差？这个联系值得在 Related Work 或 Discussion 中讨论。
- Math-Shepherd（Wang et al., 2024）和 GRACE（Khalifa et al., 2023）确实是相关但缺失的引用。

---

## 总结

| R2 意见 | 我的判断 | 核心理由 |
|--------|---------|---------|
| N1 structural property | [AGREE] | 经验证据强但不足以支撑 "structural" 的数学含义，应改为 "robust empirical regularity" |
| N2 SCB vs CoT bias 分离 | [AGREE] | 缺少 per-trace 少数票分离测试，BR 指标无法区分两个竞争假说 |
| W1 Remark 1 定位 | [AGREE] | 与我的 N2 一致，DPI 是平凡应用 |
| W2 缺少常识基准 | [REBUT] | best-case scenario 论证策略有效，但 abstract 应限定域 |
| W3 §5 信息密度 | [AGREE] | 压缩过度，建议展开 2 个代表性失败案例 |
| W4 标题张力 | [REBUT] | "Self-Extracted" 限定词准确界定范围，§6 在此范围外 |
| W5 PRM 文献 | [AGREE] | formal vs. learned verification trade-off 值得讨论 |

**与我自己审稿意见的交叉**: R2-N1 与我的 N2（Remark 1 理论包装）一致但视角互补——我聚焦 DPI 的平凡性，R2 聚焦 "structural" 声明的过度性。R2-N2 是一个我未充分识别的重要缺口，我认同其优先级为 Must-Fix。R2-W2 和 R2-W4 我持不同意见，给出了具体的文本证据。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2190 · 2026-05-23T20:25:22.899416+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "180",
  "reason": "等待 Reviewer 2 交叉分享回应",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: symb_invariant_consensus\n- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "180",
    "reason": "等待 Reviewer 2 交叉分享回应",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: symb_invariant_consensus\n- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 2191 · 2026-05-23T20:25:22.899917+00:00_

Next wakeup scheduled for 20:29:00 (in 217s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 2192 · 2026-05-23T20:25:26.649492+00:00_

Reviewer 1 的交叉回应已返回。关键判断：
- **AGREE** R2-N1（structural 过强）、R2-N2（SCB/CoT 分离缺口）、R2-W1/W3/W5
- **REBUT** R2-W2（best-case scenario 论证有效）、R2-W4（标题 "Self-Extracted" 限定准确）

等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 161

## Round 161

4 recorded events


### User

_source line 2193 · 2026-05-23T20:25:29.152033+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。7 条意见中 5 条 [AGREE]、2 条 [REBUT]：

- **R2-N1**（structural property 过强）和 **R2-N2**（SCB vs CoT bias 分离不足）均同意为 Must-Fix，后者我补充了具体的分离测试设计（per-trace 少数票约束指向分析）
- **R2-W2**（缺常识基准）反驳——best-case scenario 论证策略有效
- **R2-W4**（标题张力）反驳——"Self-Extracted" 限定词已准确界定范围

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2194 · 2026-05-23T20:25:37.272319+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "150",
  "reason": "等待 Reviewer 2 交叉分享回应返回",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: symb_invariant_consensus\n- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "150",
    "reason": "等待 Reviewer 2 交叉分享回应返回",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: symb_invariant_consensus\n- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: ARR\n- 截止日期: 2026-05-25\n- **引用验证**: ❌ 未启用\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 2195 · 2026-05-23T20:25:37.272795+00:00_

Next wakeup scheduled for 20:29:00 (in 203s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 2196 · 2026-05-23T20:25:41.612191+00:00_

Reviewer 1 交叉回应已收录。继续等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 162

## Round 162

16 recorded events


### User

_source line 2197 · 2026-05-23T20:25:43.122177+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix

### R1-N1: Cross-architecture escape (§6) 证据不足以支撑主贡献声明

**[REBUT]** R1 的核心事实判断有误。R1 称"仅测试单一 verifier 架构（DeBERTa-large-mnli）"，但 Appendix V（p.23, Table 26-27）明确测试了**三种 NLI verifier 架构**：DeBERTa-MNLI、RoBERTa-MNLI、BART-MNLI，并在 Table 27 对 3 verifiers × 5 weights = 15 个条件做了 Benjamin-Hochberg 校正。此外，Appendix W（p.23, Table 28-30）进一步扩展到 3 种额外 NLI 架构与 4 个 generator 的完整组合。因此"单一 verifier"的批评不成立。

**但我部分同意 R1 的更广泛关切**：(a) Capability-gap pattern 的 Spearman rank correlation 基于 n=6 个 generator 确实统计功效极低，不应作为强结论呈现；(b) K=12 pilot run 的规模对支撑"主贡献"偏小。论文在主文 §6（p.8）实际上已使用了较为谨慎的措辞（"preliminary evidence"、"proof of concept"），这与 R1 建议的"exploratory finding"定位基本一致。

**综合判断**：R1 要求降级为 exploratory finding 的方向合理，但其"单一 verifier"的事实依据不成立，严重程度应从 critical 降为 warning。论文已在 Appendix 中提供了多 verifier 证据，主文应更明确地引用这些结果。

---

### R1-N2: Remark 1（DPI bound）是平凡结论

**[AGREE]** 完全同意，且 R1 的论证比我自己的审稿（R2-W1）更加锐利。

我的审稿（R2-W1）指出 Remark 1 是 DPI 的直接应用，贡献在于识别 Markov chain 结构而非 DPI 本身。R1 更进一步指出了一个关键理论缺陷：**DPI 仅说明约束不能包含比 traces 更多的信息，但不能解释 MAX-SAT 为何无法从相同信息中提取更有用的投影**。这一点非常重要——信息论上界的存在不等于该上界是紧的，也不等于所有在上界以下的信息提取方式效果相同。SICA 的失败需要用经验发现（BR > 1、degeneration condition |C*| ≈ 0、Observation 1）来解释，而非 DPI。

论文 Remark 1（p.6）自己也承认 DPI 是"a standard result"，但将其命名为"Self-Extraction Bound"确实暗示了不存在的理论新颖性。R1 建议将 Remark 1 降为一句话 DPI 引用、重心放在经验发现上，我认为这是完全正确的修改方向。

---

## Should-Fix

### R1-W1: 标题 "No Detectable Improvement" 强于统计证据

**[AGREE]** 同意。论文 Appendix D（Table 6, p.14）明确显示 7/11 条件的 MDE > 5pp，仅 4/6 有统计功效的条件通过了 TOST ±2pp 等价检验。标题和 Abstract 确实未区分 confirmatory conditions（FOLIO、ProofWriter 上的 Mistral-7B 和 Qwen2.5-14B）与 underpowered conditions（GSM8K、AIME、其他小样本条件）。

"No Detectable Improvement" 作为标题技术上可辩护（确实没有 DETECTED 到改进），但读者会自然理解为"已证明无改进"，这超出了统计证据的支撑范围。建议标题增加限定词，或在 Abstract 中明确说明"在 X 个有充分统计功效的条件中确认等价，其余条件 underpowered"。

---

### R1-W2: 3-4 seeds 对 null-result claim 偏弱

**[AGREE]**（但严重程度略低于 R1 的判断）。3-4 seeds 确实有限。但论文使用了多层统计补偿：(a) 10,000 bootstrap resamples（Table 7, Appendix E）；(b) FDR 校正跨所有条件；(c) per-problem McNemar test 而非仅 aggregate accuracy。这些在一定程度上弥补了 seed 数量的不足。

R1 提到的跨 seed 相关性（同一问题跨 seeds 的回答可能非独立）是一个有效的统计关切，但在当前 LLM 评估文献中，3-4 seeds 是常见做法而非异常偏低。我建议作者在 Limitations 中增加对 seed 数量局限性的讨论，但不认为这构成阻碍接收的问题。

---

### R1-W3: GSM8K (n=30) 和 AIME (n=22) 几乎无贡献

**[AGREE]** 完全同意。Appendix D（Table 6, p.14）显示 GSM8K 和 AIME 的 MDE 远超 10pp（GSM8K n=30 的 MDE 约 18pp，AIME n=22 更高）。在这种功效水平下，这两个数据集对否定结论的支撑接近于零——它们既不能证明 SICA 无效，也不能证明 SICA 有效。

R1 建议明确区分"2 confirmatory + 2 pilot benchmarks"或将 GSM8K/AIME 移至 appendix，这是合理的。将 GSM8K/AIME 在主文中与 FOLIO/ProofWriter 并列呈现，会给读者造成"4 个 benchmark 都支持否定结论"的错误印象，而实际上只有 FOLIO 和 ProofWriter 有足够的统计功效。

---

### R1-W4: BR permutation null model 描述不足

**[AGREE]** 同意。Section 5.1（p.5）对 permutation null model 的描述仅一句话："A permutation null model—randomizing constraint-answer associations while preserving per-trace count (1100 permutations)—confirms the degree of extraction degeneration..."。这里的关键歧义是：permutation 是在**同一问题内**跨 traces 打乱 constraint-answer 映射，还是跨**不同问题**打乱？

- 如果是 within-problem permutation：null 分布反映的是"在给定约束集和答案分布下，随机关联的 BR"，这是测试约束是否与特定答案非随机关联的正确 null。
- 如果是 across-problem permutation：null 分布混合了不同难度的问题，可能产生虚假的显著性。

这两种 permutation 方案的 null distribution 和 p-value 解释截然不同。论文应在主文或附录中明确说明 permutation 的精确范围和实现细节。

---

### R1-W5: "approximately uniform constraint yield" 假设缺乏敏感性分析

**[AGREE]**（附限定条件）。R1 的理论关切成立：如果高质量 traces（更可能产生正确答案的 traces）系统性地产出更多约束，SICA 可能通过约束**数量**差异实现隐式的质量加权，此时 degeneration condition（Eq. 4, p.4）可能不再成立。

然而，论文提供了部分间接证据：(a) Appendix K（p.17, Extraction Error Taxonomy）显示约束提取的高一致性——91.8% 的约束在 Z3 级别是 technically discriminative，且 extraction rate 在不同 traces 间相对稳定；(b) Table 1（p.5）的 "4-seed aggregation" 结果显示多 seed 聚合仍无显著改进，如果约束数量差异提供了有效信号，多 seed 应放大该信号。

但 R1 要求的**直接敏感性分析**（例如：模拟不同程度的约束数量不均匀性，观察 degeneration 结论是否仍成立）确实缺失。建议作者在 appendix 中补充此分析。

---

## 对 R1 Questions 的补充意见

**Q1（K=12 是否不足）**：有效的问题。论文 Appendix I.1（p.17, Figure 6）展示了 K 与 SICA Δ 的关系，显示 K=12 处 SICA accuracy 达到 plateau，K=20 恢复到 +1.90pp。但 K=12 的 plateau 可能反映 SCB 的饱和而非 MAX-SAT 机制的饱和——更多 traces 只是带来更多偏向多数票的约束。论文应区分这两种解释。

**Q3（Self-Refine/Self-Debate 是否超出 scope）**：我认为超出 scope。论文的研究问题是"self-extracted *constraints* + formal verification"，Self-Refine/Self-Debate 是不同的 self-improvement 范式（自然语言反馈 vs. 形式化约束）。论文在 Related Work（§2, p.3）已提及这些方法并做了定位区分。

**Q4（强模型作 extractor）**：这本质上是一种 cross-model extraction，与 §6 的 cross-architecture escape 方向一致。论文未测试此设定，但如果 GPT-4 作为 extractor 仍产生追随弱模型多数票的约束，则进一步支持 SCB 是 trace-determined 的（因为约束来自弱模型的 traces）；如果不追随，则 GPT-4 可能引入了独立信号，类似 cross-architecture 效应。值得补充但非必需。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2198 · 2026-05-23T20:26:37.706283+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2199 · 2026-05-23T20:26:37.706797+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2200 · 2026-05-23T20:26:37.757368+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 2201 · 2026-05-23T20:26:37.757904+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T20:09:59.979281+00:00\", \"completed_at\": \"2026-05-23T20:14:46.487541+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 9\", \"message\": \"主正文 Section 7 (Discussion and Conclusion) 溢出约 1 行到第 9 页顶部，之后才开始 Limitations。EMNLP 2026 严格 8 页限制，部分 AC 可能视为超页 desk reject 风险。建议缩紧正文（压缩 Section 7 或前文段落）使结论完整收在第 8 页内。\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Figure 4（27 种 training-free 策略汇总）为单栏图，策略名称和数值标注字号偏小（估计 ≤6pt），正常阅读距离下难以辨认。建议改为 figure*（全宽）或减少展示条目数（移部分到 appendix），提升可读性。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯 Title + Abstract + Intro 文本）。第一个 display item 是 Figure 1（页 2 顶部，全宽 pipeline 图），传达核心 SICA 流程，信息清晰——但若能将一个 teaser figure 或关键结果移至首页，可强化审稿人第一印象。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 caption 自包含性良好（解释了 pipeline 各环节、红色虚线框含义）。Pipeline 图颜色区分度高，箭头标注清晰。作为第一个 display item，有效传达核心方法。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2（SICA Δ scatter plot）使用不同颜色和形状标记区分 6 个模型系列，图例清晰，坐标轴标注可读。颜色方案（蓝/橙/绿/红/紫/棕）对色盲基本友好。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1（主结果表）使用 booktabs 风格，最优值加粗，显著性标注（†, *）齐全，小数位数一致。全宽排版合理，列数较多但无溢出。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 2 booktabs 格式整洁。Remark 1 使用框线突出，数学排版正确，与正文形成良好视觉层次。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3（Causal DAG）虽小但清晰可读，节点标签明确，caption 解释充分。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 3 格式规范。Section 6 和 7 紧凑排列，页面利用率高，无异常空白。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段落简短（约 3 个要点：模型规模、领域范围、统计效力），符合 EMNLP 要求。\"}, {\"severity\": \"info\", \"dimension\": \"pages 12-28\", \"message\": \"Appendix A-Z 共 26 个附录章节，内容极为丰富。附录中 Tables/Figures 密度高（如页 24-25 各含 4 个表格），但作为 supplementary material 可接受。Appendix 中所
…[truncated 248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2202 · 2026-05-23T20:26:37.808364+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "symb_invariant_consensus",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 2203 · 2026-05-23T20:26:41.473901+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3665
}
```

</details>

---


### Tool call

_source line 2204 · 2026-05-23T20:27:01.315045+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
  "offset": "0",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
    "offset": "0",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 2205 · 2026-05-23T20:27:01.365746+00:00_

0	# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
1	- id: "R1-C1"
2	  summary: "Method Stage 3 sat() implementation undescribed"
3	  category: method
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 1
7	  last_seen_round: 3
8	  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
9	  resolution_round: 3
10	
11	- id: "R1-C2"
12	  summary: "Most experiments underpowered (n≤60), no power analysis"
13	  category: experiment
14	  severity: critical
15	  status: resolved
16	  first_raised_round: 1
17	  last_seen_round: 1
18	  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
19	  resolution_round: 3
20	
21	- id: "R1-C3"
22	  summary: "Oracle/upper-bound experiment missing"
23	  category: experiment
24	  severity: critical
25	  status: resolved
26	  first_raised_round: 1
27	  last_seen_round: 1
28	  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
29	  resolution_round: 3
30	
31	- id: "R1-C4"
32	  summary: "Huang et al. (ICLR 2024) not cited"
33	  category: framing
34	  severity: critical
35	  status: resolved
36	  first_raised_round: 1
37	  last_seen_round: 2
38	  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
39	  resolution_round: 2
40	
41	- id: "R1-C5"
42	  summary: "Critical related work missing"
43	  category: writing
44	  severity: critical
45	  status: resolved
46	  first_raised_round: 1
47	  last_seen_round: 1
48	  resolution: "~48 citations, 5 Related Work paragraphs."
49	  resolution_round: 3

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2206 · 2026-05-23T20:30:20.121684+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "symb_invariant_consensus",
  "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9+ recurring issues\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及\"\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: 两位 reviewer 一致\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R1-N1 指出 n=6 Spearman rank correlation 统计不稳健。R2 部分同意但纠正'单一 verifier'事实错误(实际测试了3种)。双方共识降级为 exploratory finding\"\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 20\n  resolution: \"R20 视觉审查: Figure 1 出现在 page 2 顶部，布局节奏良好。无连续2页纯文本。\"\n  resolution_round: 20\n\n- id: \"R9-VL4\"\n  summary: \"Discussion/Conclusion 展开不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及\"\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及。视觉审查显示 Discussion 溢出约1行到 page 9\"\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一问题群。R21 双方共识: n=6 不足以支撑主贡献声明\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R1-N1 指出仅 SC<72% 有效，阈值基于6点拟合。R2 纠正多 verifier 事实但同意证据强度偏弱。共识: 降级为 exploratory finding\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1]\n      note: \"R21 R1-W2: 3-4 seeds 对 null-result 偏弱，跨seed相关性未建模。R2 AGREE 但认为严重程度较低\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 R2-N2(Must-Fix): SCB 与 CoT confirmation bias 的实证分离不充分——缺少 per-trace 少数票约束指向测试。R1 AGREE 并补充分离测试设计。双方共识: Must-Fix\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 20\n  resolution: \"R20 两位 reviewer 均认为 Related Work 覆盖良好(5段，~48引用)，未提出压缩问题\"\n  resolution_round: 20\n\n- id: \"R10-I1\"\n  summary: \"'Symbolic Mirage' 概念新颖性——与 Huang/Wan 的 confirmation bias 区别\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: 与 R10-W7 同一问题群。双方共识 SCB 概念需要 per-trace 实证分离\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: resolved\n  last_seen_round: 17\n  resolution: \"Figure 2, Figure 4 added in main text.\"\n  resolution_round: 17\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"95% bootstrap CIs added for BR.\"\n  resolution_round: 11\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"Renamed to Observation 1, conditions made explicit, empirical support section added.\"\n  resolution_round: 14\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"与 R9-W3/R10-N3 同一问题群。R21 双方共识: n=6 capability-gap 应降级为 exploratory\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 R1-W1 + R2 AGREE: 标题 'No Detectable Improvement' 技术上可辩护但读者理解为'已证明无改进'。7/11 条件 MDE>5pp。建议 abstract 限定 confirmatory conditions\"\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1]\n      note: \"R21 R1-W4: BR permutation null model 描述不足——permutation 是 within-problem 还是 across-problem 未说明。R2 AGREE\"\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [2]\n      note: \"R21 R2 小问题中提及: 比典型学术用语更 dramatic，但定义清晰且使用一致\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: 与 SCB/CoT 分离问题相关。R2-N2 直接要求实证分离测试\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R11-W7\"\n  summary: \"Ensemble diversity 文献缺失\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 20\n  resolution: \"Dietterich (2000), Krogh & Vedelsby (1994) 现已在 §2 和 §7 中引用和讨论\"\n  resolution_round: 20\n\n- id: \"R12-N1\"\n  summary: \"Capability-gap pattern 证据不足以支撑 top-level contribution\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 双方共识: n=6 + pilot-scale 不足以支撑主贡献。应降级为 exploratory finding\"\n\n- id: \"R12-N2\"\n  summary: \"Underpowered tests 与 negative claim 之间存在 gap\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 R1-W1 + R2 AGREE: abstract/title 应限定 confirmatory conditions\"\n\n- id: \"R12-W1\"\n  summary: \"Cross-architecture escape 可能是 ensemble diversity\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R12-W4\"\n  summary: \"Observation 1 条件验证不完整\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1]\n      note: \"R21 R1-W5: 'approximately uniform constraint yield' 假设缺乏敏感性分析。R2 AGREE 但指出间接证据存在(Appendix K)\"\n\n- id: \"R12-EC1\"\n  summary: \"代码/数据可获取性声明缺失\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 20\n  resolution: \"Footnote 1 现已声明 'Code and data will be released upon acceptance.'\"\n  resolution_round: 20\n\n- id: \"R13-N2\"\n  summary: \"Novelty claim 相对 Huang et al. (2024) 的增量有限\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [2]\n      note: \"R21: 与 SCB/CoT 分离问题相关。若 per-trace 分离测试显示 SCB 可约化为 CoT bias，则新颖性进一步受损\"\n  action_items:\n    - round: 20\n      action: \"Related Work 新增 Huang 对比专段 + Abstract/Intro/Discussion 'extends and formalizes' → 'reveals deeper structural mechanism'\"\n      assigned_to: paper_agent\n      status: done\n      resolution: \"§2 新增 'Relationship to Huang et al.' 段落\"\n\n- id: \"R13-N3\"\n  summary: \"Abstract negative claim 过强\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 R1-W1 + R2 AGREE: 与 R11-N2 同一 issue\"\n\n- id: \"R13-W1\"\n  summary: \"SCB 命名过度——structural limitation 而非 bias\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: 与 'structural property' 过强声明问题相关。双方共识改为 'robust empirical regularity'\"\n\n- id: \"R13-W2\"\n  summary: \"BH 校正 m=16 包含非独立条件\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R13-W3\"\n  summary: \"Missing references: ensemble diversity 文献\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 20\n  resolution: \"与 R11-W7 同。Dietterich (2000), Krogh & Vedelsby (1994) 现已引用。\"\n  resolution_round: 20\n\n- id: \"R13-W4\"\n  summary: \"论文密度过高，可读性受损\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 R2-W3 + R1 AGREE: Section 5 约 2.5 页覆盖 SCB+DPI+27策略+诊断框架，§5.2 压缩过度\"\n\n- id: \"R14-N1\"\n  summary: \"Cross-architecture escape 证据不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群。R21 共识: 降级为 exploratory\"\n\n- id: \"R14-N2\"\n  summary: \"Underpowered negative claim\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1]\n      note: \"R21 R1-W1: 标题/abstract 未区分 confirmatory vs underpowered\"\n\n- id: \"R14-W1\"\n  summary: \"BR 循环论证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 R1-W4 + R2 AGREE: permutation null model 精确构造方式未说明\"\n\n- id: \"R14-W2\"\n  summary: \"Observation 1 条件 (iii) 未验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1]\n      note: \"R21 R1-W5: constraint yield uniformity 缺乏敏感性分析\"\n\n- id: \"R14-W3\"\n  summary: \"Novelty positioning vs Huang et al.\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [2]\n      note: \"R21: 与 SCB/CoT 分离问题相关\"\n\n- id: \"R14-W5\"\n  summary: \"'Pre-registered' 无注册凭证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 20\n  resolution: \"论文现使用 'pre-specified margin' 而非 'pre-registered'。\"\n  resolution_round: 20\n\n- id: \"R14-W6\"\n  summary: \"Missing references: OpenAI o1/o3\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 20\n  resolution: \"§2 现引用 'OpenAI o1/o3' 在 test-time compute 段落中\"\n  resolution_round: 20\n\n- id: \"R15-M3\"\n  summary: \"Abstract 词数超限\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 20\n  resolution: \"R20 R2 确认 Abstract ~196 词，符合 EMNLP 200 词限制。\"\n  resolution_round: 20\n\n- id: \"R15-M4\"\n  summary: \"代码/数据可获取性声明缺失\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 20\n  resolution: \"与 R12-EC1 同。Footnote 1 现已声明。\"\n  resolution_round: 20\n\n- id: \"R15-W1\"\n  summary: \"Turpin et al. 引用年份错误\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及。待确认\"\n\n- id: \"R16-N1\"\n  summary: \"Cross-architecture escape 过度声明\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群。R21 共识: 降级为 exploratory\"\n\n- id: \"R16-N2\"\n  summary: \"Underpowered negative claim\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21: 与 R14-N2 同\"\n\n# Round 20 issues (carried forward)\n\n- id: \"R20-N1\"\n  summary: \"Oracle 实验仅限形式逻辑领域(FOLIO+PW)，核心因果主张外部效度不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  resolution: \"Limitations 已扩展: FOLIO/PW 为 best-case scenario, BR 提供 lower bound\"\n  resolution_round: 20\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及。R1 反驳 R2-W2(常识基准缺失)时引用 best-case scenario 论证\"\n\n- id: \"R20-N2\"\n  summary: \"Observation 1 形式化程度与 Abstract/Intro 'structural' 呈现不匹配\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 R2-N1(Must-Fix) + R1 AGREE: 'structural property' 应改为 'robust empirical regularity'。R20 已将 Abstract 'structural'→'systematic'，但 R21 认为仍不够——需全文一致使用 empirical 限定词\"\n\n- id: \"R20-W1\"\n  summary: \"Remark 1 (DPI bound) 理论贡献有限——教科书性质非 SICA 特有\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 R1-N2(Must-Fix) + R2 AGREE: DPI 是平凡结论，'Self-Extraction Bound' 命名制造不存在的理论新颖性。更关键: DPI 不能解释 SICA 退化——MAX-SAT 可能从相同信息提取更有用的投影。真正解释退化的是经验发现(BR>1, |C'|≈0)。应移除命名，降为一句话引用\"\n\n- id: \"R20-W2\"\n  summary: \"BH FDR m=6 confirmatory conditions 选择标准的预先指定问题\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 20\n\n- id: \"R20-W3\"\n  summary: \"27 training-free variants 的穷举性——真正独立方法类别约 4-5 种\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1]\n      note: \"R21 R1 在 Q3 中提及 Self-Refine/Self-Debate 未测试，但 R2 认为超出 scope\"\n\n- id: \"R20-Q1\"\n  summary: \"α 系统消融缺失——α→0 时 source-attribution 影响是否消失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  resolution: \"α=0.0/1.0 端点已加入 Table 11\"\n  resolution_round: 20\n  first_raised_round: 20\n  last_seen_round: 20\n\n- id: \"R20-Q2\"\n  summary: \"Source-attribution vs semantic scoring ablation 缺失\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 20\n\n# Round 21 new issues\n\n- id: \"R21-N1\"\n  summary: \"'Structural property' 断言超出纯经验证据——应改为 'robust empirical regularity'\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R2-N1(Must-Fix) + R1 AGREE: 27种策略均为 zero-shot template extraction，Appendix Y 承认 few-shot/iterative 可能不同。Remark 1 DPI 仅是平凡上界。'structural' 暗示数学必然性，但证据是经验性的。应改为 'robust empirical regularity under zero-shot template extraction'\"\n  action_items:\n    - round: 21\n      action: \"Abstract/Intro/§5/§7 中 'structural property' → 'robust empirical regularity' 或 'persistent pattern'；明确界定 SCB 适用边界(zero-shot template extraction)\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-N2\"\n  summary: \"SCB 与 CoT confirmation bias 缺乏 per-trace 实证分离——核心概念新颖性受威胁\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R2-N2(Must-Fix) + R1 AGREE: BR 指标是 aggregate-level，无法区分两个假说——(A) CoT bias 在 trace 层面运作通过聚合传递 vs (B) SCB 是超越 trace 层面的独立偏差。缺少关键测试: 少数票 trace 中约束支持自身答案 vs 全局多数票。此分析仅需对现有数据做条件筛选\"\n  action_items:\n    - round: 21\n      action: \"对 a_M≠a* 的问题，计算少数票 trace 中约束支持自身答案 vs 全局多数票的比例，在主文 §5.1 增加分离分析\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-N3\"\n  summary: \"Remark 1 'Self-Extraction Bound' 命名制造不存在的理论新颖性——DPI 是平凡结论\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-N2(Must-Fix) + R2 AGREE(升级自 R2-W1): DPI 对任何确定性后处理都成立。更关键: DPI 不能解释 SICA 退化——MAX-SAT 可能从相同信息中提取更有用的投影。真正解释退化的是经验发现。建议移除命名，降为一句话 DPI 引用\"\n  action_items:\n    - round: 21\n      action: \"移除 'Self-Extraction Bound' 命名；Remark 1 降为一句话 DPI 引用；Introduction 中降低权重；论证重心放在 Observation 1 + BR + degeneration condition\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-W1\"\n  summary: \"Cross-architecture escape (Contribution 3) 应降级为 exploratory finding\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-N1(Must-Fix→Director降为Should-Fix) + R2 partial REBUT: R2 纠正'单一 verifier'事实错误(Appendix V 测试了 DeBERTa/RoBERTa/BART 三种)，但同意 n=6 capability-gap 和 K=12 pilot 偏弱。主文 §6 已使用 'preliminary evidence'。Director 判断: Should-Fix——论文措辞已较谨慎，但 Abstract/Intro 应更明确标注 exploratory\"\n  action_items:\n    - round: 21\n      action: \"Abstract 和 §1 对 Contribution 3 增加 'preliminary/exploratory' 限定词；主文引用 Appendix V 多 verifier 结果\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-W2\"\n  summary: \"标题/Abstract 否定声明强于统计证据——仅 4/11 条件通过 TOST 等价检验\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2 AGREE: 7/11 条件 MDE>5pp。'No Detectable Improvement' 技术上可辩护但读者理解为'已证明无改进'。建议 abstract 限定 'across four confirmatory conditions (n≥200)' 或标题加限定词\"\n  action_items:\n    - round: 21\n      action: \"Abstract 中更早限定 confirmatory conditions 数量和范围\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-W3\"\n  summary: \"GSM8K (n=30) / AIME (n=22) 对否定论证几乎无贡献——应区分 confirmatory vs pilot\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-W3 + R2 AGREE: MDE 远超 10pp，与 FOLIO/ProofWriter 并列呈现造成覆盖更广的错觉。建议明确区分或移至 appendix\"\n  action_items:\n    - round: 21\n      action: \"Abstract/Intro 明确区分 '2 confirmatory + 2 pilot benchmarks'，或将 GSM8K/AIME 移至 appendix\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-W4\"\n  summary: \"BR permutation null model 构造方式未充分描述\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2 AGREE: within-problem vs across-problem permutation 的区别直接影响 null distribution 解释。建议补充伪代码或详细描述\"\n  action_items:\n    - round: 21\n      action: \"§5.1 或 appendix 补充 permutation 步骤的伪代码\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-W5\"\n  summary: \"Section 5 信息密度过高——§5.2 (27策略失败) 压缩过度\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R2-W3 + R1 AGREE: 一段话概括27种策略四类失败模式，读者无法在正文获得细节。R1 建议展开2个代表性失败案例。受8页限制，需从诊断指标细节移内容到附录腾出空间\"\n  action_items:\n    - round: 21\n      action: \"§5.2 展开至少2个代表性失败案例（degenerate + diversity-limited）；将部分诊断指标细节移至附录\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-W6\"\n  summary: \"与 PRM/learned verification 文献的 trade-off 讨论不足\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R2-W5 + R1 AGREE: SICA 是 formal verification，PRM/ORM 是 learned verification，两者 failure mode 不同。诊断框架可能适用于 learned verifiers。Math-Shepherd 和 GRACE 是缺失引用\"\n  action_items:\n    - round: 21\n      action: \"Related Work 或 Discussion 增加 formal vs learned verification trade-off 讨论(1-2句)；补引 Math-Shepherd, GRACE\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-W7\"\n  summary: \"Observation 1 'approximately uniform constraint yield' 假设缺乏敏感性分析\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2 AGREE(附限定): 如果高质量 traces 系统性产出更多约束，SICA 可能通过数量差异隐式质量加权。间接证据存在(Appendix K extraction rate 稳定)但直接敏感性分析缺失\"\n  action_items:\n    - round: 21\n      action: \"Appendix 补充 constraint yield CV 分析或 yield-skewed 反例测试\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-W8\"\n  summary: \"Seed replication (3-4 seeds) 对 null-result claim 偏弱，跨 seed 相关性未建模\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2 AGREE(较低严重度): 3-4 seeds 是领域常见做法但对否定结果声明边缘。论文有 bootstrap/FDR 补偿但跨 seed 相关性未讨论\"\n  action_items:\n    - round: 21\n      action: \"Limitations 增加 seed 数量局限性讨论\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-VL1\"\n  summary: \"Discussion 溢出约1行到 page 9——EMNLP 8页限制 desk reject 风险\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [2]\n      note: \"R2 小问题 + 视觉审查: Section 7 约1行溢出到第9页顶部（Limitations之前）。部分 AC 可能视为超页\"\n  action_items:\n    - round: 21\n      action: \"缩紧正文使 Discussion 完整收在第8页内\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-VL2\"\n  summary: \"Figure 4 (p.7) 策略名称字号过小(≤6pt)——打印时难以辨认\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"视觉审查: 单栏图，策略名称和数值标注 ≤6pt。建议改为 figure* 全宽或减少条目\"\n  action_items:\n    - round: 21\n      action: \"Figure 4 改为全宽或减少展示条目数\"\n      assigned_to: research_director\n      status: open\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9+ recurring issues\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及\"\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: 两位 reviewer 一致\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R1-N1 指出 n=6 Spearman rank correlation 统计不稳健。R2 部分同意但纠正'单一 verifier'事实错误(实际测试了3种)。双方共识降级为 exploratory finding\"\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 20\n  resolution: \"R20 视觉审查: Figure 1 出现在 page 2 顶部，布局节奏良好。无连续2页纯文本。\"\n  resolution_round: 20\n\n- id: \"R9-VL4\"\n  summary: \"Discussion/Conclusion 展开不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: []\n      note: \"R20(fresh) 未单独提及\"\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及。视觉审查显示 Discussion 溢出约1行到 page 9\"\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一问题群。R21 双方共识: n=6 不足以支撑主贡献声明\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R1-N1 指出仅 SC<72% 有效，阈值基于6点拟合。R2 纠正多 verifier 事实但同意证据强度偏弱。共识: 降级为 exploratory finding\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1]\n      note: \"R21 R1-W2: 3-4 seeds 对 null-result 偏弱，跨seed相关性未建模。R2 AGREE 但认为严重程度较低\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 R2-N2(Must-Fix): SCB 与 CoT confirmation bias 的实证分离不充分——缺少 per-trace 少数票约束指向测试。R1 AGREE 并补充分离测试设计。双方共识: Must-Fix\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 20\n  resolution: \"R20 两位 reviewer 均认为 Related Work 覆盖良好(5段，~48引用)，未提出压缩问题\"\n  resolution_round: 20\n\n- id: \"R10-I1\"\n  summary: \"'Symbolic Mirage' 概念新颖性——与 Huang/Wan 的 confirmation bias 区别\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: 与 R10-W7 同一问题群。双方共识 SCB 概念需要 per-trace 实证分离\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: resolved\n  last_seen_round: 17\n  resolution: \"Figure 2, Figure 4 added in main text.\"\n  resolution_round: 17\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"95% bootstrap CIs added for BR.\"\n  resolution_round: 11\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"Renamed to Observation 1, conditions made explicit, empirical support section added.\"\n  resolution_round: 14\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"与 R9-W3/R10-N3 同一问题群。R21 双方共识: n=6 capability-gap 应降级为 exploratory\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 R1-W1 + R2 AGREE: 标题 'No Detectable Improvement' 技术上可辩护但读者理解为'已证明无改进'。7/11 条件 MDE>5pp。建议 abstract 限定 confirmatory conditions\"\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1]\n      note: \"R21 R1-W4: BR permutation null model 描述不足——permutation 是 within-problem 还是 across-problem 未说明。R2 AGREE\"\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [2]\n      note: \"R21 R2 小问题中提及: 比典型学术用语更 dramatic，但定义清晰且使用一致\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: 与 SCB/CoT 分离问题相关。R2-N2 直接要求实证分离测试\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R11-W7\"\n  summary: \"Ensemble diversity 文献缺失\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 20\n  resolution: \"Dietterich (2000), Krogh & Vedelsby (1994) 现已在 §2 和 §7 中引用和讨论\"\n  resolution_round: 20\n\n- id: \"R12-N1\"\n  summary: \"Capability-gap pattern 证据不足以支撑 top-level contribution\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 双方共识: n=6 + pilot-scale 不足以支撑主贡献。应降级为 exploratory finding\"\n\n- id: \"R12-N2\"\n  summary: \"Underpowered tests 与 negative claim 之间存在 gap\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 R1-W1 + R2 AGREE: abstract/title 应限定 confirmatory conditions\"\n\n- id: \"R12-W1\"\n  summary: \"Cross-architecture escape 可能是 ensemble diversity\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R12-W4\"\n  summary: \"Observation 1 条件验证不完整\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1]\n      note: \"R21 R1-W5: 'approximately uniform constraint yield' 假设缺乏敏感性分析。R2 AGREE 但指出间接证据存在(Appendix K)\"\n\n- id: \"R12-EC1\"\n  summary: \"代码/数据可获取性声明缺失\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 20\n  resolution: \"Footnote 1 现已声明 'Code and data will be released upon acceptance.'\"\n  resolution_round: 20\n\n- id: \"R13-N2\"\n  summary: \"Novelty claim 相对 Huang et al. (2024) 的增量有限\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [2]\n      note: \"R21: 与 SCB/CoT 分离问题相关。若 per-trace 分离测试显示 SCB 可约化为 CoT bias，则新颖性进一步受损\"\n  action_items:\n    - round: 20\n      action: \"Related Work 新增 Huang 对比专段 + Abstract/Intro/Discussion 'extends and formalizes' → 'reveals deeper structural mechanism'\"\n      assigned_to: paper_agent\n      status: done\n      resolution: \"§2 新增 'Relationship to Huang et al.' 段落\"\n\n- id: \"R13-N3\"\n  summary: \"Abstract negative claim 过强\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 R1-W1 + R2 AGREE: 与 R11-N2 同一 issue\"\n\n- id: \"R13-W1\"\n  summary: \"SCB 命名过度——structural limitation 而非 bias\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: 与 'structural property' 过强声明问题相关。双方共识改为 'robust empirical regularity'\"\n\n- id: \"R13-W2\"\n  summary: \"BH 校正 m=16 包含非独立条件\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及\"\n\n- id: \"R13-W3\"\n  summary: \"Missing references: ensemble diversity 文献\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 20\n  resolution: \"与 R11-W7 同。Dietterich (2000), Krogh & Vedelsby (1994) 现已引用。\"\n  resolution_round: 20\n\n- id: \"R13-W4\"\n  summary: \"论文密度过高，可读性受损\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 R2-W3 + R1 AGREE: Section 5 约 2.5 页覆盖 SCB+DPI+27策略+诊断框架，§5.2 压缩过度\"\n\n- id: \"R14-N1\"\n  summary: \"Cross-architecture escape 证据不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群。R21 共识: 降级为 exploratory\"\n\n- id: \"R14-N2\"\n  summary: \"Underpowered negative claim\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1]\n      note: \"R21 R1-W1: 标题/abstract 未区分 confirmatory vs underpowered\"\n\n- id: \"R14-W1\"\n  summary: \"BR 循环论证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 R1-W4 + R2 AGREE: permutation null model 精确构造方式未说明\"\n\n- id: \"R14-W2\"\n  summary: \"Observation 1 条件 (iii) 未验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1]\n      note: \"R21 R1-W5: constraint yield uniformity 缺乏敏感性分析\"\n\n- id: \"R14-W3\"\n  summary: \"Novelty positioning vs Huang et al.\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [2]\n      note: \"R21: 与 SCB/CoT 分离问题相关\"\n\n- id: \"R14-W5\"\n  summary: \"'Pre-registered' 无注册凭证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 20\n  resolution: \"论文现使用 'pre-specified margin' 而非 'pre-registered'。\"\n  resolution_round: 20\n\n- id: \"R14-W6\"\n  summary: \"Missing references: OpenAI o1/o3\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 20\n  resolution: \"§2 现引用 'OpenAI o1/o3' 在 test-time compute 段落中\"\n  resolution_round: 20\n\n- id: \"R15-M3\"\n  summary: \"Abstract 词数超限\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 20\n  resolution: \"R20 R2 确认 Abstract ~196 词，符合 EMNLP 200 词限制。\"\n  resolution_round: 20\n\n- id: \"R15-M4\"\n  summary: \"代码/数据可获取性声明缺失\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 20\n  resolution: \"与 R12-EC1 同。Footnote 1 现已声明。\"\n  resolution_round: 20\n\n- id: \"R15-W1\"\n  summary: \"Turpin et al. 引用年份错误\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及。待确认\"\n\n- id: \"R16-N1\"\n  summary: \"Cross-architecture escape 过度声明\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"与 R9-W3 同一 issue 群。R21 共识: 降级为 exploratory\"\n\n- id: \"R16-N2\"\n  summary: \"Underpowered negative claim\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21: 与 R14-N2 同\"\n\n# Round 20 issues (carried forward)\n\n- id: \"R20-N1\"\n  summary: \"Oracle 实验仅限形式逻辑领域(FOLIO+PW)，核心因果主张外部效度不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  resolution: \"Limitations 已扩展: FOLIO/PW 为 best-case scenario, BR 提供 lower bound\"\n  resolution_round: 20\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"R21(fresh) 未单独提及。R1 反驳 R2-W2(常识基准缺失)时引用 best-case scenario 论证\"\n\n- id: \"R20-N2\"\n  summary: \"Observation 1 形式化程度与 Abstract/Intro 'structural' 呈现不匹配\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 R2-N1(Must-Fix) + R1 AGREE: 'structural property' 应改为 'robust empirical regularity'。R20 已将 Abstract 'structural'→'systematic'，但 R21 认为仍不够——需全文一致使用 empirical 限定词\"\n\n- id: \"R20-W1\"\n  summary: \"Remark 1 (DPI bound) 理论贡献有限——教科书性质非 SICA 特有\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 R1-N2(Must-Fix) + R2 AGREE: DPI 是平凡结论，'Self-Extraction Bound' 命名制造不存在的理论新颖性。更关键: DPI 不能解释 SICA 退化——MAX-SAT 可能从相同信息提取更有用的投影。真正解释退化的是经验发现(BR>1, |C'|≈0)。应移除命名，降为一句话引用\"\n\n- id: \"R20-W2\"\n  summary: \"BH FDR m=6 confirmatory conditions 选择标准的预先指定问题\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 20\n\n- id: \"R20-W3\"\n  summary: \"27 training-free variants 的穷举性——真正独立方法类别约 4-5 种\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1]\n      note: \"R21 R1 在 Q3 中提及 Self-Refine/Self-Debate 未测试，但 R2 认为超出 scope\"\n\n- id: \"R20-Q1\"\n  summary: \"α 系统消融缺失——α→0 时 source-attribution 影响是否消失\"\n  category: experiment\n  severity: warning\n  status: resolved\n  resolution: \"α=0.0/1.0 端点已加入 Table 11\"\n  resolution_round: 20\n  first_raised_round: 20\n  last_seen_round: 20\n\n- id: \"R20-Q2\"\n  summary: \"Source-attribution vs semantic scoring ablation 缺失\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 20\n\n# Round 21 new issues\n\n- id: \"R21-N1\"\n  summary: \"'Structural property' 断言超出纯经验证据——应改为 'robust empirical regularity'\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R2-N1(Must-Fix) + R1 AGREE: 27种策略均为 zero-shot template extraction，Appendix Y 承认 few-shot/iterative 可能不同。Remark 1 DPI 仅是平凡上界。'structural' 暗示数学必然性，但证据是经验性的。应改为 'robust empirical regularity under zero-shot template extraction'\"\n  action_items:\n    - round: 21\n      action: \"Abstract/Intro/§5/§7 中 'structural property' → 'robust empirical regularity' 或 'persistent pattern'；明确界定 SCB 适用边界(zero-shot template extraction)\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-N2\"\n  summary: \"SCB 与 CoT confirmation bias 缺乏 per-trace 实证分离——核心概念新颖性受威胁\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R2-N2(Must-Fix) + R1 AGREE: BR 指标是 aggregate-level，无法区分两个假说——(A) CoT bias 在 trace 层面运作通过聚合传递 vs (B) SCB 是超越 trace 层面的独立偏差。缺少关键测试: 少数票 trace 中约束支持自身答案 vs 全局多数票。此分析仅需对现有数据做条件筛选\"\n  action_items:\n    - round: 21\n      action: \"对 a_M≠a* 的问题，计算少数票 trace 中约束支持自身答案 vs 全局多数票的比例，在主文 §5.1 增加分离分析\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-N3\"\n  summary: \"Remark 1 'Self-Extraction Bound' 命名制造不存在的理论新颖性——DPI 是平凡结论\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-N2(Must-Fix) + R2 AGREE(升级自 R2-W1): DPI 对任何确定性后处理都成立。更关键: DPI 不能解释 SICA 退化——MAX-SAT 可能从相同信息中提取更有用的投影。真正解释退化的是经验发现。建议移除命名，降为一句话 DPI 引用\"\n  action_items:\n    - round: 21\n      action: \"移除 'Self-Extraction Bound' 命名；Remark 1 降为一句话 DPI 引用；Introduction 中降低权重；论证重心放在 Observation 1 + BR + degeneration condition\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-W1\"\n  summary: \"Cross-architecture escape (Contribution 3) 应降级为 exploratory finding\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-N1(Must-Fix→Director降为Should-Fix) + R2 partial REBUT: R2 纠正'单一 verifier'事实错误(Appendix V 测试了 DeBERTa/RoBERTa/BART 三种)，但同意 n=6 capability-gap 和 K=12 pilot 偏弱。主文 §6 已使用 'preliminary evidence'。Director 判断: Should-Fix——论文措辞已较谨慎，但 Abstract/Intro 应更明确标注 exploratory\"\n  action_items:\n    - round: 21\n      action: \"Abstract 和 §1 对 Contribution 3 增加 'preliminary/exploratory' 限定词；主文引用 Appendix V 多 verifier 结果\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-W2\"\n  summary: \"标题/Abstract 否定声明强于统计证据——仅 4/11 条件通过 TOST 等价检验\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2 AGREE: 7/11 条件 MDE>5pp。'No Detectable Improvement' 技术上可辩护但读者理解为'已证明无改进'。建议 abstract 限定 'across four confirmatory conditions (n≥200)' 或标题加限定词\"\n  action_items:\n    - round: 21\n      action: \"Abstract 中更早限定 confirmatory conditions 数量和范围\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-W3\"\n  summary: \"GSM8K (n=30) / AIME (n=22) 对否定论证几乎无贡献——应区分 confirmatory vs pilot\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-W3 + R2 AGREE: MDE 远超 10pp，与 FOLIO/ProofWriter 并列呈现造成覆盖更广的错觉。建议明确区分或移至 appendix\"\n  action_items:\n    - round: 21\n      action: \"Abstract/Intro 明确区分 '2 confirmatory + 2 pilot benchmarks'，或将 GSM8K/AIME 移至 appendix\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-W4\"\n  summary: \"BR permutation null model 构造方式未充分描述\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2 AGREE: within-problem vs across-problem permutation 的区别直接影响 null distribution 解释。建议补充伪代码或详细描述\"\n  action_items:\n    - round: 21\n      action: \"§5.1 或 appendix 补充 permutation 步骤的伪代码\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-W5\"\n  summary: \"Section 5 信息密度过高——§5.2 (27策略失败) 压缩过度\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R2-W3 + R1 AGREE: 一段话概括27种策略四类失败模式，读者无法在正文获得细节。R1 建议展开2个代表性失败案例。受8页限制，需从诊断指标细节移内容到附录腾出空间\"\n  action_items:\n    - round: 21\n      action: \"§5.2 展开至少2个代表性失败案例（degenerate + diversity-limited）；将部分诊断指标细节移至附录\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-W6\"\n  summary: \"与 PRM/learned verification 文献的 trade-off 讨论不足\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R2-W5 + R1 AGREE: SICA 是 formal verification，PRM/ORM 是 learned verification，两者 failure mode 不同。诊断框架可能适用于 learned verifiers。Math-Shepherd 和 GRACE 是缺失引用\"\n  action_items:\n    - round: 21\n      action: \"Related Work 或 Discussion 增加 formal vs learned verification trade-off 讨论(1-2句)；补引 Math-Shepherd, GRACE\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-W7\"\n  summary: \"Observation 1 'approximately uniform constraint yield' 假设缺乏敏感性分析\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2 AGREE(附限定): 如果高质量 traces 系统性产出更多约束，SICA 可能通过数量差异隐式质量加权。间接证据存在(Appendix K extraction rate 稳定)但直接敏感性分析缺失\"\n  action_items:\n    - round: 21\n      action: \"Appendix 补充 constraint yield CV 分析或 yield-skewed 反例测试\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-W8\"\n  summary: \"Seed replication (3-4 seeds) 对 null-result claim 偏弱，跨 seed 相关性未建模\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2 AGREE(较低严重度): 3-4 seeds 是领域常见做法但对否定结果声明边缘。论文有 bootstrap/FDR 补偿但跨 seed 相关性未讨论\"\n  action_items:\n    - round: 21\n      action: \"Limitations 增加 seed 数量局限性讨论\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-VL1\"\n  summary: \"Discussion 溢出约1行到 page 9——EMNLP 8页限制 desk reject 风险\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [2]\n      note: \"R2 小问题 + 视觉审查: Section 7 约1行溢出到第9页顶部（Limitations之前）。部分 AC 可能视为超页\"\n  action_items:\n    - round: 21\n      action: \"缩紧正文使 Discussion 完整收在第8页内\"\n      assigned_to: research_director\n      status: open\n\n- id: \"R21-VL2\"\n  summary: \"Figure 4 (p.7) 策略名称字号过小(≤6pt)——打印时难以辨认\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: []\n      note: \"视觉审查: 单栏图，策略名称和数值标注 ≤6pt。建议改为 figure* 全宽或减少条目\"\n  action_items:\n    - round: 21\n      action: \"Figure 4 改为全宽或减少展示条目数\"\n      assigned_to: research_director\n      status: open\n"
  }
}
```

</details>

---


### Tool result

_source line 2207 · 2026-05-23T20:30:20.222949+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml\", \"bytes\": 26049}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2208 · 2026-05-23T20:33:02.067281+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 21 (Fresh Review)\n\n**论文**: Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning\n**Venue**: EMNLP 2026 (ARR)\n**审稿模式**: 重新审稿 (fresh)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验有效性；R2: 新颖性+完整性+写作）\n**轮次**: Round 1（一轮收敛，无需第二轮）\n\n---\n\n## Summary\n\n本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取逻辑约束，经 Z3 MAX-SAT 验证后加权聚合答案，旨在超越 Self-Consistency 的多数投票。核心发现为否定性的：在 6-9 个模型（7B–frontier）、4 个 benchmark、27 种 training-free 变体上，SICA 相对 SC 无可检测的改进（FDR 校正后无条件显著为正）。论文将此归因于 \"Symbolic Confirmation Bias\"（SCB）——自提取约束系统性追随多数票答案，并提出三个零成本诊断指标（K_eff, BR, CCR）。附带展示跨架构 NLI verifier 可突破自提取瓶颈的初步证据。\n\n---\n\n## Strengths\n\n**S1. 实验规模与统计严谨性在 NLP 否定结果论文中极为突出。** 完整的统计工具链（McNemar 配对检验、TOST ±2pp 等价检验、BH FDR 校正、10,000 次 bootstrap CI、基于 discordant pairs 的 power analysis）远超该领域平均水平。[R1, R2 共识]\n\n**S2. Oracle 对照实验设计精巧。** Gold FOL/DSL 约束产生 +17–30pp 增益（Appendix G），有力证明 MAX-SAT 框架本身有效——瓶颈在提取质量。\"Framework works, extraction fails\" 的对照逻辑是论文论证的关键支柱。[R1]\n\n**S3. 清晰且可操作的否定结果。** 论文不仅展示\"什么不工作\"，还解释\"为什么不工作\"（SCB mechanism），并提供\"怎样可能工作\"（cross-architecture escape）。诊断框架（BR > 2, K_eff < 3.62, ProcessSim > 0.6）具备部署前筛查的实用价值。[R1, R2 共识]\n\n**S4. 在约束提取范式内穷举充分。** 27 个 training-free 变体覆盖四大失败类别（退化型、多样性受限型、确认偏差型等），系统性地封堵了\"也许换个 prompt 就行\"的反驳。[R1]\n\n**S5. Appendix 深度。** 20 页附录覆盖 prompt 模板、所有 27 种策略详细结果、case studies、power analysis、hyperparameter sensitivity、cross-model analysis 等，材料足以支撑独立验证。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（阻碍接收）\n\n**MF1. \"Structural property\" 断言超出纯经验证据所能支撑的范围** [R2-N1, R1 AGREE]\n- 位置：Abstract、§5.1、§7\n- 问题：论文将 SCB 定性为自提取管线的\"结构性属性\"，暗示理论必然性。但支撑证据全部是经验性的。27 种 remediation 策略均属同一类型（zero-shot template extraction），而 Appendix Y 自己承认 few-shot/iterative refinement 可能不同。如果未测试的提取策略能打破 M→T→A→C 的 Markov 假设，\"structural property\"就不成立。\n- 要求：将 \"structural property\" 改为 \"robust empirical regularity\" 或 \"persistent pattern under zero-shot template extraction\"，并在 Discussion 中明确界定 SCB 的适用边界。\n\n**MF2. SCB 与 CoT confirmation bias 的实证分离不充分——核心概念新颖性受威胁** [R2-N2, R1 AGREE]\n- 位置：§2 \"Distinction from CoT confirmation bias\"、§5.1\n- 问题：论文在概念上区分了 SCB（聚合层面）与 CoT confirmation bias（trace 层面），但缺少关键分离测试：在产生**少数票答案**的 trace 中，提取的约束支持该 trace 自身的少数票答案（CoT bias 预测），还是全局多数票答案（SCB 预测）？BR 指标是 aggregate-level，无法区分两个竞争假说。此分析仅需对现有数据做条件筛选，无需新实验。\n- 要求：在主文 §5.1 增加 per-trace 少数票约束指向分析。若约束主要支持各自 trace 答案而非全局多数票，应诚实修正 SCB 定义为 CoT bias 在约束层面的表现。\n\n**MF3. Remark 1 \"Self-Extraction Bound\" 命名制造不存在的理论新颖性** [R1-N2, R2 AGREE]\n- 位置：§5.1 Remark 1、§7 Discussion\n- 问题：DPI 对**任何**确定性后处理都成立（I(g(X);Y) ≤ I(X;Y)），这是信息论的基础定理。命名为 \"Self-Extraction Bound\" 并赋予 Remark 编号暗示了理论创新。更关键的是，DPI **不能解释** SICA 为何失败——DPI 仅说明约束信息量 ≤ traces，但 MAX-SAT 仍可能从相同信息中提取比简单计数更有用的投影。真正解释退化的是经验发现（BR > 1、|C'| ≈ 0、degeneration condition Eq. 4），而非 DPI。\n- 要求：移除 \"Self-Extraction Bound\" 命名；Remark 1 降为一句话 DPI 引用（\"By the data processing inequality...\"），明确声明 \"this is a necessary condition, not a sufficient explanation\"；论证重心放在 Observation 1 + BR + degeneration condition 上。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. Cross-architecture escape (Contribution 3) 应降级为 exploratory finding** [R1-N1 raised as Must-Fix; R2 partial REBUT + Director 降级为 Should-Fix]\n- 位置：Abstract、§1、§6、Table 3\n- 问题：Capability-gap pattern 基于 n=6 Spearman rank correlation；K=12 pilot run。R2 纠正了 R1 的事实错误——Appendix V 实际测试了 3 种 NLI verifier（DeBERTa/RoBERTa/BART），非\"单一 verifier\"。但 n=6 capability-gap 和 pilot 规模仍偏弱。主文 §6 已使用 \"preliminary evidence\" 措辞，但 Abstract/Intro 将其与 SCB 诊断并列为主贡献。\n- Director 判断：论文措辞已较谨慎且有多 verifier 证据支撑，严重程度从 R1 的 critical 降为 warning。但 Abstract/Intro 应更明确标注 \"preliminary/exploratory\"。\n\n**SF2. 标题/Abstract 否定声明强于统计证据支撑范围** [R1-W1, R2 AGREE]\n- 位置：Title、Abstract\n- 问题：仅 4/11 条件通过 TOST ±2pp 等价检验（n ≥ 200 的 confirmatory conditions），7/11 条件 MDE > 5pp（underpowered）。标题 \"No Detectable Improvement\" 技术上可辩护但读者自然理解为\"已证明无改进\"。\n- 建议：Abstract 中更早限定 \"across four confirmatory conditions (n ≥ 200)\"。\n\n**SF3. GSM8K (n=30) / AIME (n=22) 对否定论证几乎无贡献** [R1-W3, R2 AGREE]\n- MDE 远超 10pp，与 FOLIO/ProofWriter 并列呈现造成\"4 个 benchmark 都支持否定结论\"的错觉。\n- 建议：明确区分 \"2 confirmatory + 2 pilot benchmarks\" 或将 GSM8K/AIME 移至 appendix。\n\n**SF4. Section 5 信息密度过高——§5.2 压缩过度** [R2-W3, R1 AGREE]\n- 约 2.5 页覆盖 SCB 定义、DPI 论证、27 种策略失败、三个诊断指标。§5.2 仅一段话概括 27 种策略的四类失败模式。\n- 建议：展开至少 2 个代表性失败案例（如 degenerate 类 + diversity-limited 类）。\n\n**SF5. BR permutation null model 描述不足** [R1-W4, R2 AGREE]\n- Within-problem vs across-problem permutation 的区别直接影响 null distribution 和 p-value 的解释。\n- 建议：§5.1 或附录补充 permutation 步骤的伪代码。\n\n**SF6. 与 PRM/learned verification 文献的 trade-off 讨论不足** [R2-W5, R1 AGREE]\n- SICA 是 formal verification，PRM/ORM 是 learned verification，两者 failure mode 不同。诊断框架（BR/K_eff）可能适用于 learned verifiers。\n- 建议：Related Work 或 Discussion 增加 formal vs learned verification trade-off 讨论（1-2 句）。\n\n**SF7. Observation 1 \"approximately uniform constraint yield\" 假设缺乏敏感性分析** [R1-W5, R2 AGREE with caveats]\n- 如果高质量 traces 系统性产出更多约束，SICA 可能通过数量差异隐式质量加权。间接证据存在（Appendix K）但直接敏感性分析缺失。\n- 建议：Appendix 补充 constraint yield CV 分析。\n\n**SF8. Seed replication (3-4 seeds) 对 null-result claim 偏弱** [R1-W2, R2 AGREE at lower severity]\n- 跨 seed 相关性未建模。3-4 seeds 是领域常见做法但对否定结果声明边缘。\n- 建议：Limitations 增加 seed 数量局限性讨论。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Remark 1 (DPI) 是平凡结论**：双方一致认为 DPI 对任何确定性后处理都成立，命名 \"Self-Extraction Bound\" 制造不存在的理论新颖性。应降权。\n2. **\"Structural property\" 过强**：双方一致认为应改为 \"robust empirical regularity\"，因为所有证据是经验性的，且 SCB 适用边界（zero-shot template extraction）未被充分界定。\n3. **SCB/CoT bias 分离缺口**：双方一致认为需要 per-trace 少数票约束指向测试来区分两个竞争假说。R1 补充了具体分离测试设计。\n4. **n=6 capability-gap 统计不稳健**：双方一致认为 Contribution 3 应降级为 exploratory finding。\n5. **GSM8K/AIME 贡献有限**：双方一致认为应明确区分 confirmatory vs pilot benchmarks。\n6. **BR permutation 描述不足**：双方一致认为需补充精确构造方式。\n7. **统计严谨性是核心优势**：双方一致高度评价统计方法论（TOST/FDR/bootstrap/power analysis）。\n\n## Reviewer Divergence [REBUT]\n\n1. **常识推理基准缺失**（R2-W2 raised, R1 REBUT）：R1 认为论文的 \"best-case scenario\" 论证策略有效——在最有利条件（形式逻辑任务）下证明失败比在不利条件下证明失败更有说服力。**Director 判断**：R1 的反驳有说服力，降级为 minor（abstract 应限定 \"logical/mathematical reasoning benchmarks\"）。\n2. **标题与 cross-architecture 正面结果的张力**（R2-W4 raised, R1 REBUT）：R1 指出标题限定词 \"Self-Extracted\" 已准确界定范围，§6 的正面结果不在此范围内。**Director 判断**：R1 的反驳成立，标题无需修改；但 Abstract 应更突出 §6 正面结果。\n3. **Cross-architecture escape 严重程度**（R1 rated critical, R2 partial REBUT）：R2 纠正了 R1 的\"单一 verifier\"事实错误（实际 Appendix V 测试了 3 种 NLI verifier），但同意 n=6 和 pilot 规模偏弱。**Director 判断**：降级为 Should-Fix（warning），因为论文主文已使用 \"preliminary evidence\" 措辞且有多 verifier 证据。\n\n---\n\n## Questions for Authors\n\n1. **[关键]** 在产生少数票答案的 trace 中，提取的约束更倾向于支持该 trace 自身的少数票答案，还是全局多数票答案？这是区分 SCB（聚合层面偏差）与 CoT bias（trace 层面偏差传递到约束）的关键测试。[R2-Q1, R1 AGREE]\n\n2. K=12 traces 是否不足以让 MAX-SAT 交叉验证机制发挥作用？K=50/100 时 degeneration condition（|C'| ≈ 0）是否仍成立？Appendix I.1 的 K-sensitivity 仅测到 K=20。[R1-Q1]\n\n3. 27 种策略全部使用 zero-shot template extraction。是否考虑过 few-shot extraction 或 iterative refinement？如果未测试，\"structural property\" 的断言基础是什么？[R2-Q2]\n\n4. Remark 1 的 Markov 假设（constraints are trace-determined: c_i = f(t_i)）在什么条件下可能不成立？是否有 trace perturbation 实验验证此假设近似成立？[R2-Q3]\n\n5. BR 在高精度模型上（SC > 90%）估计不稳定。这些条件的 BR 值是否应排除在 cross-model 结论之外？[R1-Q2]\n\n6. 用更强模型（GPT-4）作为 extractor 提取弱模型 traces 的约束，结果是否不同？论文的 Markov chain 论证预测不会改变（SCB 是 trace-answer coupling 的属性），但值得实验验证。[R1-Q4]\n\n---\n\n## Missing References\n\n- **Wang et al. (2024), \"Math-shepherd\"**: step-level verification 的 learned 范式，与 SICA 的 formal verification 形成直接对比 [R2]\n- **Khalifa et al. (2023), \"GRACE\"**: 判别器引导 CoT，learned verification 的另一个相关 baseline [R2]\n- **Universal Self-Consistency (Chen et al., 2024)**: 论文已引用但 Related Work 中与 SICA 的 failure mode 对比讨论不足 [R1]\n- **Self-Debate (Du et al., 2023 / Liang et al., 2024)**: 作为 training-free self-improvement 的重要类别，应在 Related Work 中说明排除理由 [R1]\n\n---\n\n## External Review\n\n外部审稿未配置（`external_review.paperreview_ai.enabled: false`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时约 5 分钟）\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ warning | Page 9 | **Section 7 (Discussion) 溢出约 1 行到第 9 页顶部**（Limitations 之前）。EMNLP 2026 严格 8 页限制，部分 AC 可能视为超页 desk reject。建议缩紧正文使 Discussion 收在第 8 页内。 |\n| ⚠️ warning | Page 7 | **Figure 4（27 策略汇总）字号过小**（≤6pt），策略名称在打印时难以辨认。建议改为 figure*（全宽）或减少展示条目。 |\n| ℹ️ info | Page 1 | 首页无视觉锚点（纯文本），第一个 display item 是 Figure 1（p.2 顶部），pipeline 图清晰。 |\n| ℹ️ info | Pages 2-8 | Figure 1/2/3/4、Table 1/2/3 布局规范，booktabs 风格一致，颜色方案对色盲友好。 |\n| ℹ️ info | Page 9 | Limitations 简短（~3 个要点），符合 EMNLP 要求。 |\n| ℹ️ info | Pages 9-11 | 参考文献格式统一（author-year），无 [?] 未解析引用。 |\n| ℹ️ info | Pages 12-28 | Appendix A-Z（26 个附录）内容丰富，表格格式一致。 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n**综合评价**：这是一篇实验设计严谨、规模充分的否定结果论文，对 neuro-symbolic reasoning 和 LLM self-improvement 社区有重要实践意义。统计方法论（TOST/FDR/bootstrap/power analysis）远超领域平均水平，oracle 对照实验设计精巧，SCB 诊断框架有实用部署价值。\n\n三个 Must-Fix 问题阻碍当前版本达到 Conference（4.0）水平：\n1. **\"Structural property\" 断言过强**：需改为 \"robust empirical regularity\"，明确界定 SCB 适用边界\n2. **SCB 与 CoT bias 的实证分离缺失**：需补充 per-trace 少数票约束指向分析（仅需对现有数据做条件筛选）\n3. **Remark 1 DPI 命名制造虚假理论贡献**：需移除 \"Self-Extraction Bound\" 命名，降权处理\n\n若以上三项在 rebuttal/revision 中充分解决（特别是 #2 的实证分离测试），且 Contribution 3 被明确标注为 exploratory finding，论文有望上调至 **4.0（Conference）** 水平。\n\n**Soundness**: 3.5/5（统计方法论严谨，但理论包装有虚假成分）\n**Excitement**: 3.25/5（否定结果有实践价值+诊断框架可操作，但受限于结论保守性）\n**Reproducibility**: 4/5（方法细节充分，代码承诺开源）\n**Confidence**: 4/5\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"structural property of self-extraction pipelines\" → \"robust empirical regularity observed under zero-shot template extraction\"\n- Contribution 3 的表述应加 \"preliminary/exploratory\" 限定词\n- 三大贡献中 Remark 1 (DPI) 不应作为独立贡献列出\n\n### §2 Related Work\n- \"Distinction from CoT confirmation bias\" 段落：概念区分清晰但缺乏实证支撑——应在此预告 §5.1 中的分离分析\n- 补引 Math-Shepherd (Wang et al., 2024)、GRACE (Khalifa et al., 2023)\n- 增加 formal vs. learned verification trade-off 讨论\n\n### §3 Methodology\n- Eq. 5 (BR) 的 permutation null model 需补充构造细节（within-problem vs across-problem）\n\n### §4 Results\n- 明确区分 confirmatory conditions (FOLIO/ProofWriter, n ≥ 200) 与 pilot conditions (GSM8K/AIME, n ≤ 30)\n- 考虑将 GSM8K/AIME 结果移至 appendix\n\n### §5 The Symbolic Mirage\n- §5.1: 增加 per-trace 少数票约束指向分析（MF2 的核心要求）\n- §5.1 Remark 1: 移除 \"Self-Extraction Bound\" 命名，降为一句话 DPI 引用\n- §5.2: 展开至少 2 个代表性失败案例（当前一段话过于压缩）\n- §5.3: 诊断指标部分细节可移至 appendix 以腾出空间\n\n### §6 Cross-Architecture Escape\n- 主文应引用 Appendix V 的多 verifier 结果（DeBERTa/RoBERTa/BART），不应只提 DeBERTa\n- Capability-gap pattern 的 n=6 Spearman correlation 应标注统计局限性\n\n### §7 Discussion\n- 溢出约 1 行到 page 9，需缩紧以避免 desk reject 风险\n\n### Limitations\n- 增加 seed 数量局限性讨论\n- 增加 Observation 1 constraint yield uniformity 假设的局限性\n\n### Figures\n- Figure 4 (p.7): 改为 figure*（全宽）或减少条目数，当前字号 ≤6pt 打印难辨",
  "project": "symb_invariant_consensus",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 21 (Fresh Review)\n\n**论文**: Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning\n**Venue**: EMNLP 2026 (ARR)\n**审稿模式**: 重新审稿 (fresh)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验有效性；R2: 新颖性+完整性+写作）\n**轮次**: Round 1（一轮收敛，无需第二轮）\n\n---\n\n## Summary\n\n本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取逻辑约束，经 Z3 MAX-SAT 验证后加权聚合答案，旨在超越 Self-Consistency 的多数投票。核心发现为否定性的：在 6-9 个模型（7B–frontier）、4 个 benchmark、27 种 training-free 变体上，SICA 相对 SC 无可检测的改进（FDR 校正后无条件显著为正）。论文将此归因于 \"Symbolic Confirmation Bias\"（SCB）——自提取约束系统性追随多数票答案，并提出三个零成本诊断指标（K_eff, BR, CCR）。附带展示跨架构 NLI verifier 可突破自提取瓶颈的初步证据。\n\n---\n\n## Strengths\n\n**S1. 实验规模与统计严谨性在 NLP 否定结果论文中极为突出。** 完整的统计工具链（McNemar 配对检验、TOST ±2pp 等价检验、BH FDR 校正、10,000 次 bootstrap CI、基于 discordant pairs 的 power analysis）远超该领域平均水平。[R1, R2 共识]\n\n**S2. Oracle 对照实验设计精巧。** Gold FOL/DSL 约束产生 +17–30pp 增益（Appendix G），有力证明 MAX-SAT 框架本身有效——瓶颈在提取质量。\"Framework works, extraction fails\" 的对照逻辑是论文论证的关键支柱。[R1]\n\n**S3. 清晰且可操作的否定结果。** 论文不仅展示\"什么不工作\"，还解释\"为什么不工作\"（SCB mechanism），并提供\"怎样可能工作\"（cross-architecture escape）。诊断框架（BR > 2, K_eff < 3.62, ProcessSim > 0.6）具备部署前筛查的实用价值。[R1, R2 共识]\n\n**S4. 在约束提取范式内穷举充分。** 27 个 training-free 变体覆盖四大失败类别（退化型、多样性受限型、确认偏差型等），系统性地封堵了\"也许换个 prompt 就行\"的反驳。[R1]\n\n**S5. Appendix 深度。** 20 页附录覆盖 prompt 模板、所有 27 种策略详细结果、case studies、power analysis、hyperparameter sensitivity、cross-model analysis 等，材料足以支撑独立验证。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（阻碍接收）\n\n**MF1. \"Structural property\" 断言超出纯经验证据所能支撑的范围** [R2-N1, R1 AGREE]\n- 位置：Abstract、§5.1、§7\n- 问题：论文将 SCB 定性为自提取管线的\"结构性属性\"，暗示理论必然性。但支撑证据全部是经验性的。27 种 remediation 策略均属同一类型（zero-shot template extraction），而 Appendix Y 自己承认 few-shot/iterative refinement 可能不同。如果未测试的提取策略能打破 M→T→A→C 的 Markov 假设，\"structural property\"就不成立。\n- 要求：将 \"structural property\" 改为 \"robust empirical regularity\" 或 \"persistent pattern under zero-shot template extraction\"，并在 Discussion 中明确界定 SCB 的适用边界。\n\n**MF2. SCB 与 CoT confirmation bias 的实证分离不充分——核心概念新颖性受威胁** [R2-N2, R1 AGREE]\n- 位置：§2 \"Distinction from CoT confirmation bias\"、§5.1\n- 问题：论文在概念上区分了 SCB（聚合层面）与 CoT confirmation bias（trace 层面），但缺少关键分离测试：在产生**少数票答案**的 trace 中，提取的约束支持该 trace 自身的少数票答案（CoT bias 预测），还是全局多数票答案（SCB 预测）？BR 指标是 aggregate-level，无法区分两个竞争假说。此分析仅需对现有数据做条件筛选，无需新实验。\n- 要求：在主文 §5.1 增加 per-trace 少数票约束指向分析。若约束主要支持各自 trace 答案而非全局多数票，应诚实修正 SCB 定义为 CoT bias 在约束层面的表现。\n\n**MF3. Remark 1 \"Self-Extraction Bound\" 命名制造不存在的理论新颖性** [R1-N2, R2 AGREE]\n- 位置：§5.1 Remark 1、§7 Discussion\n- 问题：DPI 对**任何**确定性后处理都成立（I(g(X);Y) ≤ I(X;Y)），这是信息论的基础定理。命名为 \"Self-Extraction Bound\" 并赋予 Remark 编号暗示了理论创新。更关键的是，DPI **不能解释** SICA 为何失败——DPI 仅说明约束信息量 ≤ traces，但 MAX-SAT 仍可能从相同信息中提取比简单计数更有用的投影。真正解释退化的是经验发现（BR > 1、|C'| ≈ 0、degeneration condition Eq. 4），而非 DPI。\n- 要求：移除 \"Self-Extraction Bound\" 命名；Remark 1 降为一句话 DPI 引用（\"By the data processing inequality...\"），明确声明 \"this is a necessary condition, not a sufficient explanation\"；论证重心放在 Observation 1 + BR + degeneration condition 上。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. Cross-architecture escape (Contribution 3) 应降级为 exploratory finding** [R1-N1 raised as Must-Fix; R2 partial REBUT + Director 降级为 Should-Fix]\n- 位置：Abstract、§1、§6、Table 3\n- 问题：Capability-gap pattern 基于 n=6 Spearman rank correlation；K=12 pilot run。R2 纠正了 R1 的事实错误——Appendix V 实际测试了 3 种 NLI verifier（DeBERTa/RoBERTa/BART），非\"单一 verifier\"。但 n=6 capability-gap 和 pilot 规模仍偏弱。主文 §6 已使用 \"preliminary evidence\" 措辞，但 Abstract/Intro 将其与 SCB 诊断并列为主贡献。\n- Director 判断：论文措辞已较谨慎且有多 verifier 证据支撑，严重程度从 R1 的 critical 降为 warning。但 Abstract/Intro 应更明确标注 \"preliminary/exploratory\"。\n\n**SF2. 标题/Abstract 否定声明强于统计证据支撑范围** [R1-W1, R2 AGREE]\n- 位置：Title、Abstract\n- 问题：仅 4/11 条件通过 TOST ±2pp 等价检验（n ≥ 200 的 confirmatory conditions），7/11 条件 MDE > 5pp（underpowered）。标题 \"No Detectable Improvement\" 技术上可辩护但读者自然理解为\"已证明无改进\"。\n- 建议：Abstract 中更早限定 \"across four confirmatory conditions (n ≥ 200)\"。\n\n**SF3. GSM8K (n=30) / AIME (n=22) 对否定论证几乎无贡献** [R1-W3, R2 AGREE]\n- MDE 远超 10pp，与 FOLIO/ProofWriter 并列呈现造成\"4 个 benchmark 都支持否定结论\"的错觉。\n- 建议：明确区分 \"2 confirmatory + 2 pilot benchmarks\" 或将 GSM8K/AIME 移至 appendix。\n\n**SF4. Section 5 信息密度过高——§5.2 压缩过度** [R2-W3, R1 AGREE]\n- 约 2.5 页覆盖 SCB 定义、DPI 论证、27 种策略失败、三个诊断指标。§5.2 仅一段话概括 27 种策略的四类失败模式。\n- 建议：展开至少 2 个代表性失败案例（如 degenerate 类 + diversity-limited 类）。\n\n**SF5. BR permutation null model 描述不足** [R1-W4, R2 AGREE]\n- Within-problem vs across-problem permutation 的区别直接影响 null distribution 和 p-value 的解释。\n- 建议：§5.1 或附录补充 permutation 步骤的伪代码。\n\n**SF6. 与 PRM/learned verification 文献的 trade-off 讨论不足** [R2-W5, R1 AGREE]\n- SICA 是 formal verification，PRM/ORM 是 learned verification，两者 failure mode 不同。诊断框架（BR/K_eff）可能适用于 learned verifiers。\n- 建议：Related Work 或 Discussion 增加 formal vs learned verification trade-off 讨论（1-2 句）。\n\n**SF7. Observation 1 \"approximately uniform constraint yield\" 假设缺乏敏感性分析** [R1-W5, R2 AGREE with caveats]\n- 如果高质量 traces 系统性产出更多约束，SICA 可能通过数量差异隐式质量加权。间接证据存在（Appendix K）但直接敏感性分析缺失。\n- 建议：Appendix 补充 constraint yield CV 分析。\n\n**SF8. Seed replication (3-4 seeds) 对 null-result claim 偏弱** [R1-W2, R2 AGREE at lower severity]\n- 跨 seed 相关性未建模。3-4 seeds 是领域常见做法但对否定结果声明边缘。\n- 建议：Limitations 增加 seed 数量局限性讨论。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Remark 1 (DPI) 是平凡结论**：双方一致认为 DPI 对任何确定性后处理都成立，命名 \"Self-Extraction Bound\" 制造不存在的理论新颖性。应降权。\n2. **\"Structural property\" 过强**：双方一致认为应改为 \"robust empirical regularity\"，因为所有证据是经验性的，且 SCB 适用边界（zero-shot template extraction）未被充分界定。\n3. **SCB/CoT bias 分离缺口**：双方一致认为需要 per-trace 少数票约束指向测试来区分两个竞争假说。R1 补充了具体分离测试设计。\n4. **n=6 capability-gap 统计不稳健**：双方一致认为 Contribution 3 应降级为 exploratory finding。\n5. **GSM8K/AIME 贡献有限**：双方一致认为应明确区分 confirmatory vs pilot benchmarks。\n6. **BR permutation 描述不足**：双方一致认为需补充精确构造方式。\n7. **统计严谨性是核心优势**：双方一致高度评价统计方法论（TOST/FDR/bootstrap/power analysis）。\n\n## Reviewer Divergence [REBUT]\n\n1. **常识推理基准缺失**（R2-W2 raised, R1 REBUT）：R1 认为论文的 \"best-case scenario\" 论证策略有效——在最有利条件（形式逻辑任务）下证明失败比在不利条件下证明失败更有说服力。**Director 判断**：R1 的反驳有说服力，降级为 minor（abstract 应限定 \"logical/mathematical reasoning benchmarks\"）。\n2. **标题与 cross-architecture 正面结果的张力**（R2-W4 raised, R1 REBUT）：R1 指出标题限定词 \"Self-Extracted\" 已准确界定范围，§6 的正面结果不在此范围内。**Director 判断**：R1 的反驳成立，标题无需修改；但 Abstract 应更突出 §6 正面结果。\n3. **Cross-architecture escape 严重程度**（R1 rated critical, R2 partial REBUT）：R2 纠正了 R1 的\"单一 verifier\"事实错误（实际 Appendix V 测试了 3 种 NLI verifier），但同意 n=6 和 pilot 规模偏弱。**Director 判断**：降级为 Should-Fix（warning），因为论文主文已使用 \"preliminary evidence\" 措辞且有多 verifier 证据。\n\n---\n\n## Questions for Authors\n\n1. **[关键]** 在产生少数票答案的 trace 中，提取的约束更倾向于支持该 trace 自身的少数票答案，还是全局多数票答案？这是区分 SCB（聚合层面偏差）与 CoT bias（trace 层面偏差传递到约束）的关键测试。[R2-Q1, R1 AGREE]\n\n2. K=12 traces 是否不足以让 MAX-SAT 交叉验证机制发挥作用？K=50/100 时 degeneration condition（|C'| ≈ 0）是否仍成立？Appendix I.1 的 K-sensitivity 仅测到 K=20。[R1-Q1]\n\n3. 27 种策略全部使用 zero-shot template extraction。是否考虑过 few-shot extraction 或 iterative refinement？如果未测试，\"structural property\" 的断言基础是什么？[R2-Q2]\n\n4. Remark 1 的 Markov 假设（constraints are trace-determined: c_i = f(t_i)）在什么条件下可能不成立？是否有 trace perturbation 实验验证此假设近似成立？[R2-Q3]\n\n5. BR 在高精度模型上（SC > 90%）估计不稳定。这些条件的 BR 值是否应排除在 cross-model 结论之外？[R1-Q2]\n\n6. 用更强模型（GPT-4）作为 extractor 提取弱模型 traces 的约束，结果是否不同？论文的 Markov chain 论证预测不会改变（SCB 是 trace-answer coupling 的属性），但值得实验验证。[R1-Q4]\n\n---\n\n## Missing References\n\n- **Wang et al. (2024), \"Math-shepherd\"**: step-level verification 的 learned 范式，与 SICA 的 formal verification 形成直接对比 [R2]\n- **Khalifa et al. (2023), \"GRACE\"**: 判别器引导 CoT，learned verification 的另一个相关 baseline [R2]\n- **Universal Self-Consistency (Chen et al., 2024)**: 论文已引用但 Related Work 中与 SICA 的 failure mode 对比讨论不足 [R1]\n- **Self-Debate (Du et al., 2023 / Liang et al., 2024)**: 作为 training-free self-improvement 的重要类别，应在 Related Work 中说明排除理由 [R1]\n\n---\n\n## External Review\n\n外部审稿未配置（`external_review.paperreview_ai.enabled: false`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时约 5 分钟）\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ warning | Page 9 | **Section 7 (Discussion) 溢出约 1 行到第 9 页顶部**（Limitations 之前）。EMNLP 2026 严格 8 页限制，部分 AC 可能视为超页 desk reject。建议缩紧正文使 Discussion 收在第 8 页内。 |\n| ⚠️ warning | Page 7 | **Figure 4（27 策略汇总）字号过小**（≤6pt），策略名称在打印时难以辨认。建议改为 figure*（全宽）或减少展示条目。 |\n| ℹ️ info | Page 1 | 首页无视觉锚点（纯文本），第一个 display item 是 Figure 1（p.2 顶部），pipeline 图清晰。 |\n| ℹ️ info | Pages 2-8 | Figure 1/2/3/4、Table 1/2/3 布局规范，booktabs 风格一致，颜色方案对色盲友好。 |\n| ℹ️ info | Page 9 | Limitations 简短（~3 个要点），符合 EMNLP 要求。 |\n| ℹ️ info | Pages 9-11 | 参考文献格式统一（author-year），无 [?] 未解析引用。 |\n| ℹ️ info | Pages 12-28 | Appendix A-Z（26 个附录）内容丰富，表格格式一致。 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n**综合评价**：这是一篇实验设计严谨、规模充分的否定结果论文，对 neuro-symbolic reasoning 和 LLM self-improvement 社区有重要实践意义。统计方法论（TOST/FDR/bootstrap/power analysis）远超领域平均水平，oracle 对照实验设计精巧，SCB 诊断框架有实用部署价值。\n\n三个 Must-Fix 问题阻碍当前版本达到 Conference（4.0）水平：\n1. **\"Structural property\" 断言过强**：需改为 \"robust empirical regularity\"，明确界定 SCB 适用边界\n2. **SCB 与 CoT bias 的实证分离缺失**：需补充 per-trace 少数票约束指向分析（仅需对现有数据做条件筛选）\n3. **Remark 1 DPI 命名制造虚假理论贡献**：需移除 \"Self-Extraction Bound\" 命名，降权处理\n\n若以上三项在 rebuttal/revision 中充分解决（特别是 #2 的实证分离测试），且 Contribution 3 被明确标注为 exploratory finding，论文有望上调至 **4.0（Conference）** 水平。\n\n**Soundness**: 3.5/5（统计方法论严谨，但理论包装有虚假成分）\n**Excitement**: 3.25/5（否定结果有实践价值+诊断框架可操作，但受限于结论保守性）\n**Reproducibility**: 4/5（方法细节充分，代码承诺开源）\n**Confidence**: 4/5\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"structural property of self-extraction pipelines\" → \"robust empirical regularity observed under zero-shot template extraction\"\n- Contribution 3 的表述应加 \"preliminary/exploratory\" 限定词\n- 三大贡献中 Remark 1 (DPI) 不应作为独立贡献列出\n\n### §2 Related Work\n- \"Distinction from CoT confirmation bias\" 段落：概念区分清晰但缺乏实证支撑——应在此预告 §5.1 中的分离分析\n- 补引 Math-Shepherd (Wang et al., 2024)、GRACE (Khalifa et al., 2023)\n- 增加 formal vs. learned verification trade-off 讨论\n\n### §3 Methodology\n- Eq. 5 (BR) 的 permutation null model 需补充构造细节（within-problem vs across-problem）\n\n### §4 Results\n- 明确区分 confirmatory conditions (FOLIO/ProofWriter, n ≥ 200) 与 pilot conditions (GSM8K/AIME, n ≤ 30)\n- 考虑将 GSM8K/AIME 结果移至 appendix\n\n### §5 The Symbolic Mirage\n- §5.1: 增加 per-trace 少数票约束指向分析（MF2 的核心要求）\n- §5.1 Remark 1: 移除 \"Self-Extraction Bound\" 命名，降为一句话 DPI 引用\n- §5.2: 展开至少 2 个代表性失败案例（当前一段话过于压缩）\n- §5.3: 诊断指标部分细节可移至 appendix 以腾出空间\n\n### §6 Cross-Architecture Escape\n- 主文应引用 Appendix V 的多 verifier 结果（DeBERTa/RoBERTa/BART），不应只提 DeBERTa\n- Capability-gap pattern 的 n=6 Spearman correlation 应标注统计局限性\n\n### §7 Discussion\n- 溢出约 1 行到 page 9，需缩紧以避免 desk reject 风险\n\n### Limitations\n- 增加 seed 数量局限性讨论\n- 增加 Observation 1 constraint yield uniformity 假设的局限性\n\n### Figures\n- Figure 4 (p.7): 改为 figure*（全宽）或减少条目数，当前字号 ≤6pt 打印难辨",
    "project": "symb_invariant_consensus",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 2209 · 2026-05-23T20:33:03.623581+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 1556
}
```

</details>

---


### Tool call

_source line 2210 · 2026-05-23T20:33:15.528113+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2211 · 2026-05-23T20:33:15.528659+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 2212 · 2026-05-23T20:33:34.510991+00:00_

审稿完成。报告已投递至 Research Director。

**Round 21 审稿结论：3.5/5 (Borderline Conference)**

三个 Must-Fix：
1. **"Structural property" → "robust empirical regularity"**：所有证据是经验性的，SCB 适用边界未充分界定
2. **SCB vs CoT bias 实证分离缺失**：需 per-trace 少数票约束指向分析（仅需对现有数据条件筛选）
3. **Remark 1 DPI 命名移除**：平凡结论不应包装为理论贡献

八个 Should-Fix 涵盖 Contribution 3 降级、标题/Abstract claim 校准、GSM8K/AIME 区分、Section 5 密度、BR permutation 描述、PRM 文献、constraint yield 敏感性、seed 局限性。

两个视觉问题：Discussion 溢出 page 9（desk reject 风险）、Figure 4 字号过小。

若 Must-Fix 在 revision 中解决，论文有望上调至 4.0（Conference）。Issue Tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 163

## Round 163

2 recorded events


### User

_source line 2213 · 2026-05-23T20:33:37.027265+00:00_

[Reviewer 2 审稿结果]:
交叉回应已完成。总结：

- **R1-N1**（cross-architecture 证据不足）：**[REBUT]** — R1 称"仅测试单一 verifier"事实有误，Appendix V Table 26-27 测试了 3 种 NLI 架构。但部分同意证据仍属 exploratory 级别，建议降为 warning。
- **R1-N2**（Remark 1 DPI 平凡）：**[AGREE]** — 与我的 W1 一致，且 R1 额外指出 DPI 不能解释 MAX-SAT 为何无法提取更有用的信息投影，论证更锐利。
- **R1-W1~W5**：全部 **[AGREE]**，其中 W2（seed 数量）和 W5（uniform yield 假设）附加了限定条件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2214 · 2026-05-23T20:33:50.401314+00:00_

审稿报告已投递至 Research Director，Issue Tracker 已同步更新。

**Round 21 审稿完成**：

- **评分**：3.5/5（Borderline Conference）
- **3 个 Must-Fix**：(1) "structural property" → "robust empirical regularity"；(2) SCB 与 CoT bias 需 per-trace 实证分离测试；(3) Remark 1 DPI 移除 "Self-Extraction Bound" 命名
- **8 个 Should-Fix**：Contribution 3 降级为 exploratory、标题/Abstract claim 校准、GSM8K/AIME 区分 pilot、Section 5 压缩、BR permutation 描述、PRM 文献讨论、constraint yield 敏感性、seed 局限性
- **视觉审查**：Discussion 溢出 ~1 行到 page 9（desk reject 风险）、Figure 4 字号过小
- **升级路径**：若 3 个 Must-Fix 在 revision 中充分解决，论文有望上调至 4.0（Conference）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 164

## Round 164

68 recorded events


### User

_source line 2215 · 2026-05-24T22:49:42.252608+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: symb_invariant_consensus
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR (Main + Findings unified)
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2216 · 2026-05-24T22:49:47.962215+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2217 · 2026-05-24T22:49:48.013220+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2218 · 2026-05-24T22:49:56.083859+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 2219 · 2026-05-24T22:49:56.134476+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2220 · 2026-05-24T22:50:04.874689+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 2221 · 2026-05-24T22:50:05.979461+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (176 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-multi-seed-llama-pw-seed456: LLaMA-3.1-8B PW seed456 多种子复制。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。（排队等待 GPU）\n- exp-deberta-ft-combo: Fine-tuned DeBERTa-large on ProofWriter OWA depth-5 achieves near-perfect NLI accuracy (99.67%) and provides massive combo gains over SC baseline when used as external verifier, demonstrating that domain-specific NLI fine-tuning breaks the SCB ceiling by providing truly independent verification signal.（准备中）\n- exp-multi-seed-mistral-folio: Multi-seed replication (seeds 123,456,789) of Mistral-7B × FOLIO-204 shows consistent Δ(SICA-SC) direction across seeds. Baseline seed=42 already available. Combined with Mistral×PW and Qwen2.5×FOLIO/PW multi-seed, provides comprehensive reproducibility evidence for W4 reviewer response.（准备中）\n- exp-multi-seed-qwen25-7b-folio: Multi-seed replication (seeds 123,456,789) of Qwen2.5-7B × FOLIO-204 adds a fourth model family (beyond Qwen2.5-14B, Mistral-7B, LLaMA-8B) for cross-family consistency of SCB. If Δ(SICA-SC)≤0 holds across 7B-scale Qwen as well, it strengthens the scale+architecture invariance claim.（准备中）\n- exp-multi-seed-qwen25: Multi-seed replication (seeds 123,45
…[truncated 1730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 2222 · 2026-05-24T22:50:05.979927+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2223 · 2026-05-24T22:50:12.555620+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % removed: not available in this TeX distribution
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	% tcolorbox removed: unused in content
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{enumitem}
18	\usepackage{subcaption}
19	% tikz removed: figures now use external PDF/PNG
20	\usepackage{listings}
21	\usepackage{algorithm}
22	\usepackage{algpseudocode}
23	\usepackage{hyperref}
24	% cleveref removed: unused (\Cref/\cref not called)
25	
26	\lstset{
27	  basicstyle=\small\ttfamily,
28	  breaklines=true,
29	  frame=tb,
30	  framerule=0.4pt,
31	  rulecolor=\color{gray},
32	  backgroundcolor=\color{gray!5},
33	  xleftmargin=1em,
34	  xrightmargin=1em,
35	  aboveskip=0.8em,
36	  belowskip=1.2em,
37	}
38	
39	\graphicspath{{../figures/paper/}{figures/}}
40	
41	\title{Beyond Self-Consistency: Self-Extracted Constraints\\Provide No Measurable Improvement in LLM Reasoning}
42	
43	\author{Anonymous}
44	
45	\begin{document}
46	\maketitle
47	
48	% Tighten spacing for 8-page budget
49	\setlength{\textfloatsep}{5pt plus 2pt minus 4pt}
50	\setlength{\dbltextfloatsep}{5pt plus 2pt minus 4pt}
51	\setlength{\floatsep}{3pt plus 2pt minus 2pt}
52	\setlength{\dblfloatsep}{3pt plus 2pt minus 2pt}
53	\setlength{\abovecaptionskip}{2pt}
54	\setlength{\belowcaptionskip}{0pt}
55	\setlength{\abovedisplayskip}{4pt plus 1pt minus 2pt}
56	\setlength{\belowdisplayskip}{4pt plus 1pt minus 2pt}
57	\setlength{\intextsep}{5pt plus 1pt minus 2pt}
58	
59	\input{abstract}
60	
61	\input{introduction}
62	
63	\input{related_work}
64	
65	\input{method}
66	
67	\input{experiments}
68	
69	\input{analysis}
70	
71	\input{solutions}
72	
73	\input{discussion}
74	
75	\section*{Limitations}
76	\input{limitations_content}
…[truncated 96 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 6575
}
```

</details>

---


### Tool call

_source line 2224 · 2026-05-24T22:50:12.606366+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2225 · 2026-05-24T22:50:12.606706+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2226 · 2026-05-24T22:50:16.924335+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"MRL Workshop at EMNLP 2025: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/mrl-workshop-emnlp-2025-first-call-papers"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found information related to EMNLP 2026 and ARR submission deadlines. The most relevant information comes from workshop calls that are part of EMNLP 2026:

For the MINT Work
…[truncated 911 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 4317
}
```

</details>

---


### Tool result

_source line 2227 · 2026-05-24T22:50:16.975036+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4368
}
```

</details>

---


### Tool call

_source line 2228 · 2026-05-24T22:50:37.591710+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2229 · 2026-05-24T22:50:37.592165+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2230 · 2026-05-24T22:50:37.642648+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference submission deadline ARR cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference submission deadline ARR cycle"
  }
}
```

</details>

---


### Tool call

_source line 2231 · 2026-05-24T22:50:37.643045+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ARR 2026\" submission deadline June July cycle openreview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ARR 2026\" submission deadline June July cycle openreview"
  }
}
```

</details>

---


### Tool result

_source line 2232 · 2026-05-24T22:50:42.713450+00:00_

Web search results for query: "EMNLP 2026 main conference submission deadline ARR cycle"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here is the information about EMNLP 2026 main conference submission deadlines for the ARR cycle:

## EMNLP 2026 Main Conference - ARR Submission Deadlines

The ARR submission deadline for long and short papers is May 25, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

### Additional Key Dates

The reviewer registration deadline for all authors is May 27, 2026.

The author response and author-reviewer discussion period runs July 7-13, 2026, with meta-review released July 30, 2026. The EMNLP commitment dead
…[truncated 432 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 5070
}
```

</details>

---


### Tool result

_source line 2233 · 2026-05-24T22:50:49.490326+00:00_

Web search results for query: ""ARR 2026" submission deadline June July cycle openreview"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"}]

Based on the search results, here's what I found regarding ARR 2026 submission deadlines:

ARR switched to 10-week review cycles starting in May 2025, which means there are generally 5 cycles per year instead of 6.

The search results reference submission deadlines but don't provide complete details for the June-July cycle specifically. However, papers must be submitted by the ARR 2026 May cycle at the latest to be considered for EMNLP 2026. The results also mention that from October 2022 to February 2025, ARR ran 8-week review cycles with submission deadlines on the 15th of every second month, though this has changed with the new 10-week cycle schedule.

For more detailed information about specific June-July cycle deadlines, you may want to visit the official ARR dates and venues page at http://aclrollingreview.org/dates or check the OpenReview submission portal for the specific cycle you're interested in.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 11847
}
```

</details>

---


### Tool call

_source line 2234 · 2026-05-24T22:50:57.869010+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract ALL submission guidelines: page limits (long/short), template, anonymity rules, appendix rules, citation format, ethics requirements, supplementary material rules, and any other formatting requirements. Be comprehensive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract ALL submission guidelines: page limits (long/short), template, anonymity rules, appendix rules, citation format, ethics requirements, supplementary material rules, and any other formatting requirements. Be comprehensive."
  }
}
```

</details>

---


### Tool call

_source line 2235 · 2026-05-24T22:50:59.826749+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 2236 · 2026-05-24T22:51:00.780819+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2237 · 2026-05-24T22:51:00.982537+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 2238 · 2026-05-24T22:51:01.134014+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 2239 · 2026-05-24T22:51:03.257947+00:00_

# EMNLP 2026 Submission Guidelines

## Page Limits
- **Long Papers:** 8 pages of content
- **Short Papers:** 4 pages of content
- **Accepted papers:** Additional 1 page permitted in final version (9 pages for long; 5 pages for short) to address reviewer feedback

## Anonymity Requirements
The review process is "double-blind." Reviewers cannot see author identities, and authors cannot see reviewer identities. However, "there is no anonymity period requirement" following ACL and ARR policies. Authors may optionally make anonymized submissions publicly visible through ARR.

## Templates & Submission Format
Follow "all of the ARR submission requirements" including paper submission and templates available on the ARR website. Specific template details are referenced but not detailed in this document.

## Supplementary Materials
"Optional Supplementary Materials" including appendices, software, and data are permitted, with full guidelines available through ARR.

## Ethics & Responsible Research
Submissions must comply with:
- ACL's Publication Ethics Policy
- ARR's Ethics Policy
- The "responsible NLP research checklist"
- ACL's Disclosure Policy (for coordinated disclosure)

Papers may face desk rejection for hallucinated citations, thinly sliced contributions, or entirely AI-generated submissions.

## Other Key Requirements
- Two-way anonymized review instructions apply
- Citation and comparison guidelines follow ARR standards
- Writing assistance is permitted
- Limitations section required
- No author list modifications during commitment phase (reordering allowed)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "elapsed_ms": 5388
}
```

</details>

---


### Tool call

_source line 2240 · 2026-05-24T22:51:08.076627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2241 · 2026-05-24T22:51:08.428605+00:00_

1	\begin{abstract}
2	Self-Consistency (SC) improves large language model (LLM) reasoning via majority voting over chain-of-thought (CoT) traces.
3	A natural extension is to extract formal constraints from these traces and aggregate them with a symbolic solver---but does it work?
4	We test this through Symbolic Invariant Consensus Aggregation (SICA), which extracts first-order logic constraints and solves weighted partial Maximum Satisfiability (MAX-SAT).
5	Across six models (7B--32B), four reasoning benchmarks, and over 1,200 instances, SICA produces answers statistically equivalent to SC: no condition shows significant improvement after false discovery rate (FDR) control.
6	We diagnose this failure as \emph{symbolic confirmation bias}: self-extracted constraints systematically confirm their source trace's (potentially incorrect) answer, with bias ratios $1.66$--$4.97\times$ across nine models up to frontier scale.
7	We formalize the mechanism through effective ensemble size $K_\text{eff}$ derived from inter-trace agreement $\kappa$, showing that correlated traces collapse nominal $K{=}12$ to $K_\text{eff}$ as low as 1.20---far below the diversity threshold for aggregation gains.
8	Twenty-seven training-free remediation strategies across all intervention dimensions fail to break this bottleneck, establishing it as structural to same-model extraction.
9	A cross-architecture encoder-only verifier escapes the bias ($+6.67$\,pp, $p < 0.001$), demonstrating that architectural independence restores corrective signal.
10	Three zero-cost diagnostics predict failure modes from a single pilot run.
11	\end{abstract}
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2242 · 2026-05-24T22:51:08.429137+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2243 · 2026-05-24T22:51:08.479691+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	\looseness=-1
4	Self-Consistency (SC) \citep{wang2023sc} selects the majority answer across $K$ chain-of-thought traces, a strategy grounded in the Condorcet Jury Theorem: independent voters converge to truth \citep{condorcet1785, ladha1992correlated}. In practice, SC's gains plateau for strong models \citep{loo2025reevaluating, byerly2025selfconsistency}, and correlated LLM errors \citep{kim2025correlated} reduce the effective ensemble size \citep{dietterich2000ensemble}. A natural remedy is to move beyond simple vote-counting: extract logical constraints from the traces---as in neuro-symbolic approaches \citep{pan2023logiclm, olausson2023linc, ye2024satlm}---and let a provably sound solver adjudicate. If the solver can filter contradictions and enforce logical consistency, it should recover information that raw majority voting discards.
5	
6	\looseness=-1
7	We test this intuition through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces (prompted as first-order logic (FOL); 99\% are propositional at the level of the Z3 SMT solver) and selects answers via weighted partial MAX-SAT (\S\ref{sec:pipeline}; Figure~\ref{fig:pipeline}). Despite Z3 validating nearly all self-extracted constraints \citep[cf.][]{chan2026position}, SICA produces answers identical to majority voting on the vast majority of problems. Across six models (7B--32B), four benchmarks, and multi-seed replication, no condition shows a significant positive effect after FDR control (Table~\ref{tab:main_results}). Four of six powered conditions confirm equivalence within $\pm$2\,pp (Two One-Sided Tests; TOST); the remainder are underpowered for smaller effects.
8	
9	\looseness=-1
10	The failure is not in the solver but in the constraints it operates on. Self-extracted constraints systematically support the model's majority answer---a robust empirical regularity of zero-shot self-extraction pipelin
…[truncated 3184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2244 · 2026-05-24T22:51:08.831687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2245 · 2026-05-24T22:51:09.836473+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\looseness=-1
5	\paragraph{Self-consistency and ensemble theory.}
6	Self-consistency (SC) selects the majority answer across chain-of-thought traces \citep{wang2023sc}, with extensions for free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting \citep{li2023diverse}, and reasoning-aware filtering \citep{wan2024rasc, toh2024notallvotes, kim2026reasc}. SC gains plateau early \citep{loo2025reevaluating, byerly2025selfconsistency}. The Condorcet Jury Theorem \citep{condorcet1785} guarantees majority-vote convergence under independence; ensemble theory \citep{dietterich2000ensemble, krogh1994neural} requires error diversity. \citet{ladha1992correlated} show correlated voters reduce effective ensemble size; our $K_\text{eff}$ adapts Fleiss' $\kappa$ from diversity metrics \citep{kuncheva2003measures, brown2005diversity} to quantify this (\S\ref{sec:pipeline}). \citet{kim2025correlated} demonstrate correlated LLM errors; \citet{kuai2026independent} propose cross-model independence auditing.
7	
8	\looseness=-1
9	\paragraph{Neuro-symbolic reasoning.}
10	Three paradigms exist: \emph{specification-generation} \citep{pan2023logiclm, olausson2023linc, ye2024satlm} and \emph{program-generation} \citep{gao2023pal, chen2023program, lyu2023faithful} formalize before answer generation; \emph{trace-extraction} (this work) operates post-hoc, inheriting confirmation bias (\S\ref{sec:confirmation-bias}). Recent work extends symbolic planning and verified reasoning \citep{ryu2025clover, xu2026dylos, li2025aristotle, wang2025fover, singh2026verge, luo2025logicagent, miya2025eidoku}; \citet{amonkar2025realitycheck} show formalization quality degrades with complexity; \citet{chan2026position} argue logical soundness alone is unreliable. Prior studies note high formalization error rates but treat them as quality problems; we show they are \emph{systematically biased} toward the model'
…[truncated 2267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 2246 · 2026-05-24T22:51:09.836977+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2247 · 2026-05-24T22:51:10.339378+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{SICA Pipeline}
5	\label{sec:pipeline}
6	\label{sec:condorcet}
7	\label{sec:effective-k}
8	
9	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. Under correlated traces (Fleiss' $\kappa$ \citep{fleiss1971kappa}), the effective ensemble size $K_\text{eff}$ is
10	\begin{equation}
11	\label{eq:effk}
12	K_{\text{eff}} = K \,/\, [1 + (K{-}1) \cdot \kappa]
13	\end{equation}
14	(following \citet{ladha1992correlated}). Intuitively, $K_\text{eff}$ measures how many effectively independent votes $K$ correlated traces contribute; e.g., $K{=}12$ traces with $\kappa{=}0.69$ yield $K_\text{eff} \approx 1.3$, meaning twelve correlated traces carry no more independent information than 1.3 uncorrelated ones. This motivates constraint-based aggregation.
15	
16	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
17	
18	\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K\}$ at temperature $T = 0.7$. Each trace $t_i$ yields answer $a_i$.
19	
20	\looseness=-1
21	\paragraph{Constraint extraction.}\label{sec:constraint-extraction} The same LLM extracts logical constraints from each trace at $T_{\text{ext}} = 0.3$. The extraction prompt requests JSON output with constraint type, expression, and Z3-compatible formula (Appendix~\ref{app:prompts}); in practice, 99.0\% of extracted constraints are propositional at the Z3 level, with only 1.0\% using true quantifiers. The \emph{extraction rate} is the fraction of traces yielding at least one parseable constraint.
22	
23	\paragraph{Deduplication and MAX-SAT.} Constraints are deduplicated by syntactic equivalence (global average deduplication ratio: 46.0\%); each unique constraint $c_m$ receives weight $w_m$ equal to the number of source traces. The ob
…[truncated 3971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2248 · 2026-05-24T22:51:10.339852+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2249 · 2026-05-24T22:51:10.792099+00:00_

1	\section{Results}
2	\label{sec:results}
3	\label{sec:main-results}
4	
5	\looseness=-1 Table~\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. Two confirmatory conditions show significant degradation after Benjamini--Hochberg (BH) FDR control ($m{=}6$; multi-seed aggregates and extensions are exploratory): Mistral-7B on ProofWriter ($-2.83$\,pp, raw $p = 0.014$, adj.\ $p = 0.042$) and Qwen2.5-14B on ProofWriter ($-2.50$\,pp, raw $p = 0.011$, adj.\ $p = 0.042$). No condition shows a significant positive effect. An aggregate sign test yields 8 positive and 7 negative $\Delta$ values ($p = 1.00$, two-sided). When SICA and SC disagree, SC selects the correct answer $2.6\times$ more often (139 vs.\ 53 across conditions), indicating that constraint-based reweighting introduces noise rather than corrective signal (representative cases in Appendix~\ref{app:case-studies}).
6	
7	\begin{table*}[t]
8	\centering
9	\small
10	\caption{SICA vs.\ SC across all non-degenerate self-extraction conditions (sorted by SC). Two conditions show significant degradation after BH correction ($m{=}6$ confirmatory; remaining exploratory); no condition shows a significant gain. $\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \textbf{bold}: $p < 0.05$; {*}\,BH adj.\ $p = 0.042$; $^{3s}$\,3-seed aggregate; $^{4s}$\,4-seed confirmatory aggregate; $^\dagger$\,4-seed replication in Table~\ref{tab:multi-seed} (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\%$ for $|\Delta| = 2$\,pp (Appendix~\ref{app:power}). Degenerate conditions ($C_0 < 5\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$) yield $\Delta = 0$ and are reported separately in Appendix~\ref{app:oracle}.}
11	\label{tab:main_results}
12	\begin{tabular}{@{}llrrrrl@{}}
13	\toprule
14	Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & $p$ \\
15	\midrule
16	\multicolumn{7}{l}{\textit{Type C: e
…[truncated 3609 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2250 · 2026-05-24T22:51:10.842766+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 2251 · 2026-05-24T22:51:11.294791+00:00_

1	\section{The Symbolic Mirage}
2	\label{sec:analysis}
3	
4	\subsection{Symbolic Confirmation Bias}
5	\label{sec:confirmation-bias}
6	
7	\looseness=-1 Self-extracted constraints systematically align with the model's majority answer---a persistent empirical property of zero-shot self-extraction pipelines, not a cognitive bias analogy. On Mistral-7B FOLIO, when SICA errs, 83.3\% of constraints support the incorrect answer---bias ratio $4.97\times$ (Table~\ref{tab:cross-model-bias})---and 94\% of errors overlap with SC. Z3 rejects only 3.4\% of constraints, and MAX-SAT produces answers identical to count-only aggregation on ${\geq}99\%$ of problems across all weight settings $\alpha$ (Table~\ref{tab:alpha-ablation}), confirming that the formal verification layer is vacuous (Eq.~\ref{eq:degenerate}): 99\% of constraints pass Z3 validation yet add no information beyond majority voting.
8	
9	\looseness=-1 Crucially, BR $> 1$ is not an independent finding but a corollary of the degeneration identified in Observation~1: under source-attribution scoring, constraint weight is proportional to trace count, so the majority answer necessarily receives more support. A permutation null model---randomizing constraint--answer associations while preserving per-trace counts (1{,}000 permutations)---confirms this: $\text{BR}_\text{null} \approx \text{BR}_\text{obs}$ ($\text{BR}_\text{excess} \approx 0$; $p > 0.7$) across all tested conditions. BR thus quantifies the degree of extraction degeneration---how completely constraints collapse to majority-vote equivalents---not an independent bias signal. On problems where SC is correct, constraints still track the majority ($\text{BR}_\text{correct}$ $1.29$--$3.64\times$), confirming that self-extracted constraints reflect distributional frequency rather than logical validity.
10	
11	\looseness=-1 The pattern generalizes across nine models from 7B to frontier (BR $1.66$--$4.97\times$; Table~\ref{tab:frontier-scb} in Appendix~\ref{app:frontier
…[truncated 9706 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2252 · 2026-05-24T22:51:11.295224+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
  }
}
```

</details>

---


### Tool result

_source line 2253 · 2026-05-24T22:51:11.797334+00:00_

1	\section{Escaping the Bottleneck}
2	\label{sec:solutions}
3	\label{sec:cross-arch}
4	
5	\paragraph{Motivation.}
6	\looseness=-1 No training-free self-extraction method achieves independence from the model's distributional prior (\S\ref{sec:remediation}). We test whether a structurally independent verifier---sharing neither architecture nor training data with the generator---can escape the DPI bound $I(C;Y) \leq I(T;Y)$.
7	
8	\paragraph{Method.}
9	\looseness=-1 We use DeBERTa-large \citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli} for Natural Language Inference (NLI), to classify (premise, conclusion) pairs as entailment, contradiction, or neutral. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$).
10	
11	\paragraph{Zero-shot results.}
12	\looseness=-1 DeBERTa NLI alone achieves 49.51\% on FOLIO and 55.00\% on ProofWriter. Combo $w{=}3$ yields $+6.67$\,pp on ProofWriter for Mistral-7B ($p < 0.001$, significant after BH correction) and $+2.94$\,pp on FOLIO (n.s.); all generators with SC $\geq 72\%$ show no significant improvement ($\Delta \leq +1.47$\,pp). Same-model SICA \emph{degrades} ProofWriter ($-2.83$\,pp; Table~\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution.
13	
14	\paragraph{Capability gap.}
15	\looseness=-1 Across 108 conditions (three NLI architectures, four generators, three domains), gain decreases monotonically with generator accuracy---a \emph{capability-gap pattern} ($\rho = 1.0$, $p = 0.003$; Figure~\ref{fig:capability-gap}). All significant gains concentrate below the verifier's standalone accuracy; on ProofWriter ($n{=}600$; Table~\ref{tab:cross_generator_nli}), only Mistral-7B (SC below DeBERTa's 55.00\%) gains significantly ($+6.67$\,pp, $p < 0.001$; BART/RoBERTa \emph{degrade} strong generators at $w{=}5$; Appendix~\ref{app:multi-n
…[truncated 1729 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2254 · 2026-05-24T22:51:11.798088+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2255 · 2026-05-24T22:51:12.250188+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	\label{sec:conclusion}
4	
5	\looseness=-1
6	Our central finding is that formal verification's value depends on the \emph{independence} of its inputs, not the soundness of its logic. SICA reduces to majority vote under source-attribution scoring (Observation~1), and 27 training-free variants fail to escape---symbolic confirmation bias holds across nine models (7B to frontier), scaling redundancy rather than information. Three zero-cost diagnostics predict failure modes from a $K{=}12$ pilot run (\S\ref{sec:diagnostic-framework}). Cross-architecture verification provides a preliminary escape: gains follow a capability-gap pattern---positive only when the verifier exceeds the generator's accuracy (\S\ref{sec:cross-arch}), suggesting that future self-verification should prioritize \emph{architectural diversity} over scale.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2256 · 2026-05-24T22:51:12.301052+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
  }
}
```

</details>

---


### Tool result

_source line 2257 · 2026-05-24T22:51:13.156074+00:00_

1	\looseness=-1 Our locally-run models range from 7B to 32B; frontier coverage relies on cross-model extraction, so we cannot confirm identical SCB patterns at frontier scale. All benchmarks are English logical reasoning; FOLIO and ProofWriter represent a best-case for symbolic verification, and the observed bias ratios ($1.66$--$4.97\times$) likely represent a \emph{lower bound} on SCB in less structured domains. Statistical power is limited for effects below ${\sim}2$\,pp (MDE $1.86$--$4.84$\,pp across conditions); small positive effects cannot be ruled out. We do not evaluate trained extractors, which could potentially break the self-extraction bound by introducing external signal. The cross-architecture escape (\S\ref{sec:cross-arch}) is validated with a single NLI architecture (DeBERTa); whether the capability-gap pattern generalizes to other verifier types (e.g., code executors, proof assistants) remains open. Our formal analysis assumes source-attribution scoring; alternative attribution schemes that decouple constraints from their originating traces could alter the degeneration condition, though no such scheme has been proposed.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 2258 · 2026-05-24T22:51:13.156561+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool call

_source line 2259 · 2026-05-24T22:51:13.307670+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2260 · 2026-05-24T22:51:13.458756+00:00_

File content (40250 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool result

_source line 2261 · 2026-05-24T22:51:13.762843+00:00_

1	# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
2	- id: "R1-C1"
3	  summary: "Method Stage 3 sat() implementation undescribed"
4	  category: method
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 1
8	  last_seen_round: 3
9	  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
10	  resolution_round: 3
11	
12	- id: "R1-C2"
13	  summary: "Most experiments underpowered (n≤60), no power analysis"
14	  category: experiment
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
20	  resolution_round: 3
21	
22	- id: "R1-C3"
23	  summary: "Oracle/upper-bound experiment missing"
24	  category: experiment
25	  severity: critical
26	  status: resolved
27	  first_raised_round: 1
28	  last_seen_round: 1
29	  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
30	  resolution_round: 3
31	
32	- id: "R1-C4"
33	  summary: "Huang et al. (ICLR 2024) not cited"
34	  category: framing
35	  severity: critical
36	  status: resolved
37	  first_raised_round: 1
38	  last_seen_round: 2
39	  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
40	  resolution_round: 2
41	
42	- id: "R1-C5"
43	  summary: "Critical related work missing"
44	  category: writing
45	  severity: critical
46	  status: resolved
47	  first_raised_round: 1
48	  last_seen_round: 1
49	  resolution: "~48 citations, 5 Related Work paragraphs."
50	  resolution_round: 3
51	
52	- id: "R1-C9"
53	  summary: "Capability trap novelty unclear"
54	  category: framing
55	  severity: critical
56	  status: resolved
57	  first_raised_round: 1
58	  last_seen_round: 3
59	  resolution: "Reframed as regime-dependent analysis with CJT framework."
60	  resolution_round: 3
61	
62	- id: "R3-N1"
63	  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
64	  category: method
65	  severity: critical

…[truncated 27921 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 2262 · 2026-05-24T22:51:23.753114+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2263 · 2026-05-24T22:51:24.707156+00:00_

1	\section{Prompt Templates}
2	\label{app:prompts}
3	
4	SICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).
5	
6	\paragraph{System Prompt.}\leavevmode
7	
8	\begin{lstlisting}
9	You are a constraint extraction tool. Output ONLY
10	valid JSON. Do NOT solve problems, reason about
11	correctness, or think step-by-step. Extract
12	constraints from the given trace exactly as stated.
13	\end{lstlisting}
14	
15	\paragraph{Mathematical Constraint Extraction (EXTRACTION\_PROMPT).}
16	
17	Used for GSM8K and AIME datasets. The placeholder \texttt{\{trace\}} is replaced with the reasoning trace at runtime.
18	
19	\begin{lstlisting}
20	Extract mathematical constraints from this reasoning
21	trace as a JSON object.
22	
23	Rules:
24	- type: "equation", "inequality", or "predicate"
25	- expression: human-readable, e.g. "x + y == 14"
26	- z3_formula: a single comparison expression in
27	  Python Z3 syntax
28	- source_step: step number where the constraint
29	  appears
30	- Use variable names from the trace
31	
32	z3_formula MUST follow these rules:
33	- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,
34	  /, **, %
35	- Use individual named variables: a1, a2, a3...
36	  NOT arrays a[1] or sets A
37	- Expand all sums explicitly:
38	  "a1 + a2 + a3 == 55" NOT "sum([a1,a2,a3])"
39	- NO Python builtins: sum(), len(), max(), min(),
40	  list(), set(), range(), int()
41	- Each z3_formula must be exactly ONE comparison
42	  (==, !=, <, >, <=, >=)
43	- For multiple values, write separate constraints
44	  for each
45	
46	Output ONLY the JSON below, nothing else:
47	{"constraints": [{"type": "equation",
48	  "expression": "x + y =
…[truncated 6490 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2264 · 2026-05-24T22:51:25.211107+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_19/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_19/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2265 · 2026-05-24T22:51:26.616561+00:00_

-rw-r--r-- 1 ubuntu ubuntu 6982790 May 24 22:48 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_19/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 2266 · 2026-05-24T22:51:26.718072+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/config.yaml 2>/dev/null || grep -r \"paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/config.yaml 2>/dev/null || echo \"NOT_FOUND_IN_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/config.yaml 2>/dev/null || grep -r \"paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/config.yaml 2>/dev/null || echo \"NOT_FOUND_IN_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2267 · 2026-05-24T22:51:26.818919+00:00_

NOT_FOUND_IN_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2268 · 2026-05-24T22:51:30.986913+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/config.yaml 2>/dev/null; echo \"---\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/config.yaml 2>/dev/null | head -80",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/config.yaml 2>/dev/null; echo \"---\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/config.yaml 2>/dev/null | head -80",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2269 · 2026-05-24T22:51:31.089257+00:00_

---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2270 · 2026-05-24T22:51:33.292682+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10",
  "description": "Find config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 2271 · 2026-05-24T22:51:33.394235+00:00_

find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/’: No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2272 · 2026-05-24T22:51:39.217428+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ -name \"config*.yaml\" -o -name \"config*.yml\" 2>/dev/null | head -10",
  "description": "Find config files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ -name \"config*.yaml\" -o -name \"config*.yml\" 2>/dev/null | head -10",
    "description": "Find config files in project"
  }
}
```

</details>

---


### Tool result

_source line 2273 · 2026-05-24T22:51:39.418668+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.venv/lib/python3.14/site-packages/configs/config.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2274 · 2026-05-24T22:51:42.781950+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 2275 · 2026-05-24T22:51:43.233980+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (176 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-multi-seed-llama-pw-seed456: LLaMA-3.1-8B PW seed456 多种子复制。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。（排队等待 GPU）\n- exp-deberta-ft-combo: Fine-tuned DeBERTa-large on ProofWriter OWA depth-5 achieves near-perfect NLI accuracy (99.67%) and provides massive combo gains over SC baseline when used as external verifier, demonstrating that domain-specific NLI fine-tuning breaks the SCB ceiling by providing truly independent verification signal.（准备中）\n- exp-multi-seed-mistral-folio: Multi-seed replication (seeds 123,456,789) of Mistral-7B × FOLIO-204 shows consistent Δ(SICA-SC) direction across seeds. Baseline seed=42 already available. Combined with Mistral×PW and Qwen2.5×FOLIO/PW multi-seed, provides comprehensive reproducibility evidence for W4 reviewer response.（准备中）\n- exp-multi-seed-qwen25-7b-folio: Multi-seed replication (seeds 123,456,789) of Qwen2.5-7B × FOLIO-204 adds a fourth model family (beyond Qwen2.5-14B, Mistral-7B, LLaMA-8B) for cross-family consistency of SCB. If Δ(SICA-SC)≤0 holds across 7B-scale Qwen as well, it strengthens the scale+architecture invariance claim.（准备中）\n- exp-multi-seed-qwen25: Multi-seed replication (seeds 123,45
…[truncated 1730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2276 · 2026-05-24T22:52:34.281979+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "symb_invariant_consensus",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 2277 · 2026-05-24T22:52:53.569066+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19287
}
```

</details>

---


### Tool call

_source line 2278 · 2026-05-24T22:52:53.723050+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "symb_invariant_consensus",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## Venue 信息\n- **会议**: EMNLP 2026 (通过 ARR 统一审稿)\n- **Deadline**: 2026-05-25 AoE (ARR May cycle)\n- **页数限制**: Long paper, 8 页正文 + 无限参考文献。Limitations 和 ethical considerations 不计入页数。\n- **模板**: ACL template (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（无 anonymity period 要求）\n- **Abstract**: ≤ 200 words\n- **Overall Assessment 评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_19/submitted.pdf`\n\n## 你的审查侧重\n\n**核心任务：评估方法论严谨性和实验设计的充分性。**\n\n重点审查：\n1. **统计方法论**：McNemar 检验、BH FDR 校正（m=6 confirmatory）、TOST 等价检验的正确性和适当性。±2pp margin 是否有充分理由？统计功效是否足够支撑否定声明？\n2. **Observation 1 (Argmax Preservation) 形式化**：三个条件（degeneration, source-attribution, uniform yield）的验证是否充分？是否存在未验证的假设？\n3. **Bias Ratio (BR) 指标**：BR 是否存在循环论证？permutation null model 的构造方式是否清晰？BR excess ≈ 0 的解释是否合理？\n4. **多种子复制**：3-4 seeds 是否足够支撑 null-result claim？跨 seed 相关性是否建模？\n5. **Cross-architecture escape 证据强度**：capability-gap pattern 基于 n=6 数据点的 Spearman ρ=1.0 是否可靠？DeBERTa NLI combo 的实验设计是否充分？\n6. **实验覆盖面**：6 个模型、4 个基准 + 2 个 pilot、27 种 remediation 策略是否足够？GSM8K (n=30) / AIME (n=22) 对论证的贡献是否应该区分？\n7. **DPI/Markov chain 理论贡献**：DPI bound 是否 trivial？Remark 1 的理论新颖性如何？\n\n请提供完整审稿意见，包括：Summary, Strengths, Weaknesses (Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (评分 + 理由 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## Venue 信息\n- **会议**: EMNLP 2026 (通过 ARR 统一审稿)\n- **Deadline**: 2026-05-25 AoE (ARR May cycle)\n- **页数限制**: Long paper, 8 页正文 + 无限参考文献。Limitations 和 ethical considerations 不计入页数。\n- **模板**: ACL template (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（无 anonymity period 要求）\n- **Abstract**: ≤ 200 words\n- **Overall Assessment 评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_19/submitted.pdf`\n\n## 你的审查侧重\n\n**核心任务：评估方法论严谨性和实验设计的充分性。**\n\n重点审查：\n1. **统计方法论**：McNemar 检验、BH FDR 校正（m=6 confirmatory）、TOST 等价检验的正确性和适当性。±2pp margin 是否有充分理由？统计功效是否足够支撑否定声明？\n2. **Observation 1 (Argmax Preservation) 形式化**：三个条件（degeneration, source-attribution, uniform yield）的验证是否充分？是否存在未验证的假设？\n3. **Bias Ratio (BR) 指标**：BR 是否存在循环论证？permutation null model 的构造方式是否清晰？BR excess ≈ 0 的解释是否合理？\n4. **多种子复制**：3-4 seeds 是否足够支撑 null-result claim？跨 seed 相关性是否建模？\n5. **Cross-architecture escape 证据强度**：capability-gap pattern 基于 n=6 数据点的 Spearman ρ=1.0 是否可靠？DeBERTa NLI combo 的实验设计是否充分？\n6. **实验覆盖面**：6 个模型、4 个基准 + 2 个 pilot、27 种 remediation 策略是否足够？GSM8K (n=30) / AIME (n=22) 对论证的贡献是否应该区分？\n7. **DPI/Markov chain 理论贡献**：DPI bound 是否 trivial？Remark 1 的理论新颖性如何？\n\n请提供完整审稿意见，包括：Summary, Strengths, Weaknesses (Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (评分 + 理由 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 2279 · 2026-05-24T22:53:09.269048+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15545
}
```

</details>

---


### Tool call

_source line 2280 · 2026-05-24T22:53:09.420080+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "symb_invariant_consensus",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性/完整性 + 写作格式**审查。\n\n## Venue 信息\n- **会议**: EMNLP 2026 (通过 ARR 统一审稿)\n- **Deadline**: 2026-05-25 AoE (ARR May cycle)\n- **页数限制**: Long paper, 8 页正文 + 无限参考文献。Limitations 和 ethical considerations 不计入页数。\n- **模板**: ACL template (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（无 anonymity period 要求）\n- **Abstract**: ≤ 200 words\n- **Overall Assessment 评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_19/submitted.pdf`\n\n## 你的审查侧重\n\n**核心任务：评估论文新颖性、完整性、写作质量和格式合规性。**\n\n重点审查：\n1. **新颖性定位**：Symbolic Confirmation Bias (SCB) 概念相对于 Huang et al. (2024) 自我纠正失败、Wan et al. (2025) CoT confirmation bias 的增量贡献。SCB 是否构成独立新发现？是否与 CoT-level confirmation bias 有充分的实证分离？\n2. **Framing 强度**：标题 \"No Measurable Improvement\" 和 Abstract 的否定声明是否与统计证据匹配？仅 4/11 条件通过 TOST 等价检验。\"robust empirical regularity\" vs \"structural property\" 的措辞选择。\n3. **贡献定位**：三个贡献（symbolic mirage, diagnostic framework, cross-architecture escape）是否准确定位？Cross-architecture escape 是否应明确标注为 exploratory？\n4. **Related Work 覆盖**：是否遗漏重要相关工作？与 PRM/ORM/learned verification 的 trade-off 讨论是否充分？\n5. **写作质量**：Section 5 (~2.5 页覆盖 SCB+DPI+27策略+诊断框架) 是否过于压缩？论文整体可读性如何？术语（\"Symbolic Mirage\"）是否过于 dramatic？\n6. **格式合规**：8 页限制是否满足？Abstract 词数是否 ≤200？Limitations section 位置和长度？Figure/Table 质量和布局？\n7. **常识性基准缺失**：论文仅评估形式逻辑基准（FOLIO, ProofWriter）和 pilot 基准（GSM8K, AIME），是否需要常识推理基准（如 ARC, CommonsenseQA）？\n\n请提供完整审稿意见，包括：Summary, Strengths, Weaknesses (Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (评分 + 理由 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性/完整性 + 写作格式**审查。\n\n## Venue 信息\n- **会议**: EMNLP 2026 (通过 ARR 统一审稿)\n- **Deadline**: 2026-05-25 AoE (ARR May cycle)\n- **页数限制**: Long paper, 8 页正文 + 无限参考文献。Limitations 和 ethical considerations 不计入页数。\n- **模板**: ACL template (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（无 anonymity period 要求）\n- **Abstract**: ≤ 200 words\n- **Overall Assessment 评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_19/submitted.pdf`\n\n## 你的审查侧重\n\n**核心任务：评估论文新颖性、完整性、写作质量和格式合规性。**\n\n重点审查：\n1. **新颖性定位**：Symbolic Confirmation Bias (SCB) 概念相对于 Huang et al. (2024) 自我纠正失败、Wan et al. (2025) CoT confirmation bias 的增量贡献。SCB 是否构成独立新发现？是否与 CoT-level confirmation bias 有充分的实证分离？\n2. **Framing 强度**：标题 \"No Measurable Improvement\" 和 Abstract 的否定声明是否与统计证据匹配？仅 4/11 条件通过 TOST 等价检验。\"robust empirical regularity\" vs \"structural property\" 的措辞选择。\n3. **贡献定位**：三个贡献（symbolic mirage, diagnostic framework, cross-architecture escape）是否准确定位？Cross-architecture escape 是否应明确标注为 exploratory？\n4. **Related Work 覆盖**：是否遗漏重要相关工作？与 PRM/ORM/learned verification 的 trade-off 讨论是否充分？\n5. **写作质量**：Section 5 (~2.5 页覆盖 SCB+DPI+27策略+诊断框架) 是否过于压缩？论文整体可读性如何？术语（\"Symbolic Mirage\"）是否过于 dramatic？\n6. **格式合规**：8 页限制是否满足？Abstract 词数是否 ≤200？Limitations section 位置和长度？Figure/Table 质量和布局？\n7. **常识性基准缺失**：论文仅评估形式逻辑基准（FOLIO, ProofWriter）和 pilot 基准（GSM8K, AIME），是否需要常识推理基准（如 ARC, CommonsenseQA）？\n\n请提供完整审稿意见，包括：Summary, Strengths, Weaknesses (Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (评分 + 理由 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 2281 · 2026-05-24T22:53:10.786087+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1366
}
```

</details>

---


### Assistant

_source line 2282 · 2026-05-24T22:53:24.776087+00:00_

已派发所有审稿任务：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性+实验设计） | ✅ 已派发 |
| Reviewer 2（新颖性/完整性+写作格式） | ✅ 已派发 |
| 视觉审查 Agent | ✅ 已启动 |
| 外部审稿（Stanford Agentic Reviewer） | ⬜ 未配置，跳过 |

等待两位 Reviewer 返回初审意见后，进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 165

## Round 165

2 recorded events


### User

_source line 2283 · 2026-05-24T22:58:41.645967+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（方法严谨性 + 实验设计）

---

### Summary

本文提出 Symbolic Invariant Consensus Aggregation (SICA)，从 LLM 推理 trace 中提取 FOL 约束并通过加权 partial MAX-SAT 聚合，测试其能否超越 Self-Consistency (SC)。核心发现为**否定结果**：在 6 个模型（7B–32B）、4 个基准、1,200+ 实例上，SICA 与 SC 在 FDR 校正后无统计显著差异。论文将此诊断为"symbolic confirmation bias"（自提取约束系统性支持模型多数答案），提出 Observation 1（Argmax Preservation）形式化机制，测试 27 种 training-free 补救策略均失败，并展示 cross-architecture NLI verifier 的初步逃逸证据。

---

## 总体评分

**Overall**: 3.5 / 5（Borderline Conference）

**一句话总结**: 一项方法论扎实、实验覆盖面广的重要否定结果研究，但统计功效对小效应不足、理论贡献有限、cross-architecture escape 证据初步，整体处于主会议接收边界。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法论整体正确（McNemar、BH FDR、TOST、bootstrap），但 ±2pp TOST margin 缺乏充分论证，power 不足以排除 1–2pp 效应，这对否定结果论文是关键短板 |
| Excitement | 3/5 | 重要的否定结果，诊断框架有实用价值，但核心发现（同模型自提取约束继承分布先验）事后看具有可预见性，理论贡献（DPI bound + Markov chain）较为朴素 |
| Reproducibility | 4/5 | 实验细节充分（K=12, T=0.7, T_ext=0.3, α=0.5, Z3 timeout 10s），prompt 模板在 Appendix A 完整给出，代码承诺在接收后发布 |
| Confidence | 4/5 | 本审稿人在 LLM reasoning、neuro-symbolic methods、统计检验方面有扎实背景 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] ±2pp TOST 等价性 margin 缺乏充分论证

- 具体位置：§4 第 2 段；Appendix U
- 问题：论文使用 ±2pp 作为 TOST 等价性检验的预设 margin，声称 4 个条件通过等价性检验。但 ±2pp 这个 margin 的选择缺乏充分的先验论证——为什么 2pp 而不是 1pp 或 3pp？在实际应用中，对于 SC baseline 在 40%–86% 范围内的条件，2pp 的实际意义（practical significance）差异巨大。论文 Appendix U 提到 TOST 分类对 margin 选择是 robust 的（"regardless of the chosen margin, no condition shows a significant positive SICA effect"），但这只说明没有正向效应，不能证明 ±2pp 是合理的等价边界。
- 为什么影响接收：这是一篇**否定结果论文**，其核心贡献取决于"SICA 不优于 SC"的claim 强度。如果 margin 选择不当，等价性声明的可信度被削弱。论文标题 "No Measurable Improvement" 与实际统计功效不匹配——MDE 为 1.86–4.84pp（Appendix D），意味着 1–2pp 的小正效应无法被排除。
- 建议修改方向：(1) 提供 ±2pp margin 的先验论证（如参照 SC 改进的效应量文献、或实践中可忽略的精度差异阈值）；(2) 报告多个 margin（±1pp, ±2pp, ±3pp）下的 TOST 结果以展示 sensitivity；(3) 将标题/abstract 中的绝对否定语气软化为与实际功效匹配的表述（如 "no large improvement" 或 "no improvement detectable at our statistical power"）。

**N2** [critical] 否定结果的统计功效不足以支撑论文核心 claim 的强度

- 具体位置：§4 第 2 段；Table 1 caption；Appendix D (Table 5)
- 问题：Table 1 caption 承认 "All conditions have McNemar power < 80% for |Δ| = 2pp"。Appendix D 报告 MDE 为 1.86–4.84pp，最大样本量条件（n=801, Qwen2.5-14B FOLIO 4-seed）的 MDE 仍为 1.86pp。这意味着论文**不能排除** SICA 存在 1–2pp 正效应的可能性。对于宣称 "no measurable improvement" 的论文，这是根本性的统计短板。
- 特别地，Qwen3-14B 的 4-seed 均值 Δ = +0.92 ± 1.14pp（§4），如果效应确实在 ~1pp 量级，当前实验设计根本无法检测到。论文在 Limitations 中承认了这一点（"small positive effects cannot be ruled out"），但这一承认与标题/abstract 的措辞存在张力。
- 为什么影响接收：否定结果论文的价值与其排除正效应的能力直接成正比。当前功效水平只能排除 ≥2pp 的效应，但标题和 abstract 的措辞暗示排除了所有可测量的改进。
- 建议修改方向：(1) 增大样本量或增加 seeds 以提高功效（如将 FOLIO n=204 扩展到 n=500+）；(2) 如果不增加数据，至少在 abstract 中明确限定 claim 的范围（"no improvement exceeding ~2pp"）；(3) 考虑将多条件数据 pool 起来做 meta-analytic 功效分析。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Observation 1（Argmax Preservation）的理论贡献有限

- 具体位置：§5.1 Observation 1
- 问题：Observation 1 陈述"在退化条件（|C∖| ≈ 0）、source-attribution scoring、和近似均匀约束产出下，SICA 退化为多数投票"。这三个条件成立时，结论是 scoring 公式（Eq. 3）的直接代数推论——不需要额外的洞察。实际的贡献在于**实证验证这三个条件在实践中成立**（Z3 拒绝率 3.4%, 约束产出 CV=0.26, 96.1% argmax 一致），而不是"observation"本身。但论文将其包装为一个 formal observation，可能误导读者认为这是一个非平凡的理论结果。
- 建议：(1) 明确区分平凡的代数推论和非平凡的实证发现；(2) 将 CV=0.26 的约束产出均匀性讨论得更深入——0.26 的 CV 意味着约束产出存在 ~26% 的变异，这是否足以使 Observation 1 的近似有效？在什么 CV 阈值下近似会失效？

**W2** [warning] Capability-gap pattern 基于极少数据点

- 具体位置：§6 第 3 段；Table 2；Figure 8（Appendix）
- 问题：§6 声称 "gain decreases monotonically with generator accuracy—a capability-gap pattern (ρ = 1.0, p = 0.003; Figure 8)"。Spearman ρ = 1.0 且 p = 0.003 对应约 n = 6 个排名完全一致的数据点。虽然 "108 conditions" 被提及，但 ρ 显然是在聚合后的 generator-level 计算的（Table 2 仅有 4 个 generator），跨 3 个 NLI 架构 × 4 个 generator 可能得到 ~6 个有效独立比较点。用 6 个点的完美排名相关声称一个 general pattern 是过度推断的风险。
- 此外，capability-gap 的核心发现——"weaker generator + stronger verifier = gain"——本身并不令人惊讶，几乎是 ensemble learning 的基本原理。
- 建议：(1) 明确报告 ρ 的计算单位（是 generator-level 还是 condition-level）；(2) 讨论 overfitting 到少量数据点的风险；(3) 降低该 pattern 作为 contribution 的权重，或补充更多 verifier 类型的数据。

**W3** [warning] BR 指标与 Observation 1 的循环性

- 具体位置：§3.1（Eq. 5）；§5.1 第 5 段
- 问题：论文在 §5.1 明确承认 "BR > 1 is not an independent finding but a corollary of the degeneration identified in Observation 1"，并通过 permutation null model 确认 BR_excess ≈ 0。这意味着 BR 作为一个度量指标，在概念上不增加超越 Observation 1 的信息——它本质上是 trace-count geometry 的另一种量化。论文同时在 §3.1 引入 BR 作为方法论的一部分，又在 §5.1 承认其冗余性，这在叙事上造成混淆。
- 为什么影响评分：BR 在论文中占据显著篇幅（方法章节定义 + 分析章节大量使用 + 诊断框架纳入），但其独立贡献有限。这降低了论文的信息密度。
- 建议：(1) 在引入 BR 时即明确其与 Observation 1 的关系和定位——将其定位为 degeneration 程度的便捷度量而非独立发现；(2) 简化 BR 相关讨论，腾出空间给更实质性的分析。

**W4** [warning] Multi-seed replication 的 seed 数量对否定声明的支撑有限

- 具体位置：§4 第 3 段；Table 42（Appendix）
- 问题：Mistral-7B 使用 3 seeds，Qwen2.5-14B 和 Qwen3-14B 各 4 seeds。对于一个核心 claim 为"无改善"的论文，3–4 seeds 的变异性估计是粗糙的。Mistral-7B 三个 seed 的 Δ 分布为 [+2.94, 0.00, -2.45]pp（§4），标准差 2.70pp，这意味着该模型的单 seed 结果高度不可靠。如果再抽一个 seed 得到 Δ = +3pp，整体结论会受到影响。
- 特别地，跨 seed 相关性未被建模。3 个 seed 是独立的，但 seed 间的 trace 分布可能存在系统性模式（如某些 seed 倾向于更多样的 trace）。
- 建议：(1) 增加到 ≥5 seeds 以获得更可靠的变异性估计；(2) 报告 seed-level 的效应量置信区间（不仅是 mean ± std）；(3) 讨论 seed 间系统性差异的可能性。

**W5** [warning] GSM8K (n=30) 和 AIME (n=22) 的数据点过少，贡献定位不清

- 具体位置：§3.2；Appendix G
- 问题：GSM8K 仅 30 题，AIME 仅 22 题，用于验证 "degenerate regime"（C₀ < 5%）。在如此小样本上，任何统计检验都没有意义。论文将这两个数据集定位为 "pilot"（§3.2），但它们仍然出现在方法章节中，可能给读者造成它们是正式实验的一部分的印象。
- 建议：(1) 在正文中更明确地将 GSM8K/AIME 标记为 illustrative examples 而非 experimental conditions；(2) 如果这两个数据集的目的仅是展示 C₀ 诊断的有效性，考虑在 appendix 中用完整数据集（如 GSM8K 完整 1319 题）验证。

---

## 小问题（不影响接收）

- §3.1 Eq. 3 中 α = 0.5 的选择理由仅在 §3.1 末尾一句带过（"α = 0.5 is not critical (±0.49pp across α ∈ [0,1])"），建议将 sensitivity 结果放在更显眼的位置（如 Table 10 的交叉引用）。

- Abstract 第 4 句 "over 1,200 instances" 的计算：FOLIO 204 + ProofWriter 600 + LogiQA 200 + StrategyQA 200 = 1,204，但这是在最基本的 single-seed 配置下。考虑到多 seed 和多模型配置，实际 instance-model pairs 远多于此。"1,200 instances" 可能低估了工作量但也可能误导读者以为每个条件都有 1,200 个实例。

- Figure 2 caption 中 "shape encodes dataset" 的图例在 PDF 中较难辨认（●PW, ▲FOLIO, ■LogiQA 的符号在小尺寸下难以区分）。

- §5.1 第 9 段提到 "92.2% of non-unanimous problems contain cross-group shared formulas"——这个数字的意义可以更清楚地解释：它是否意味着共享公式在所有组中获得相同权重？

- Appendix S (§S) 的 "Constraint Quality Across Methods" 部分内容丰富但与主文的连接不够紧密。

---

## Questions to Authors

Q1: ±2pp 的 TOST margin 是否有预注册或先验论证？如果在看到数据后才选择此 margin，这构成 researcher degrees of freedom。

Q2: Observation 1 的条件 (iii)（近似均匀约束产出）中，CV = 0.26 是全局平均值。是否存在特定问题子集的 CV 显著更高（如 >0.5），从而 Observation 1 的近似失效？这些问题上 SICA 是否表现不同？

Q3: 论文在 §5.1 确认 BR_excess ≈ 0（permutation p > 0.7）。如果 BR 完全由 trace-count geometry 解释，那么 BR 作为诊断指标（§5.3）相比直接使用 trace-count 分布有何增量价值？

Q4: 27 种 remediation 策略中，few-shot extraction 和 iterative refinement 被明确排除在外（§5.1 末段："whether few-shot or iterative refinement approaches alter this pattern remains open"）。是否有初步实验或理论论证表明这些方法也会失败？如果没有，"structural to same-model extraction" 的 claim 可能过强。

Q5: Cross-architecture escape 中，DeBERTa 在 FOLIO 上 standalone accuracy 仅 49.51%，但 combo 模式在 Mistral-7B FOLIO 上产生 +2.94pp gain（n.s.）。如果将 verifier weight w 调得更高（如 w=5 或 w=10），是否能在 FOLIO 上也获得显著 gain？

---

## Missing References

- **Lightman et al. (2023)** "Let's Verify Step by Step"——process reward models 作为验证器的代表工作，与本文的 cross-architecture verifier 方向高度相关，但未在 related work 或 escape 章节中讨论。（注：论文参考文献列表中包含 Lightman et al.，但正文未引用。）

- **Cobbe et al. (2021)** "Training Verifiers to Solve Math Word Problems"——trained verifier 的经典工作，与论文 Limitations 中提到的 "trained extractors" 直接相关。（同样已在 references 中但正文引用不充分。）

---

## 主要优势

1. **重要的否定结果**：在 neuro-symbolic reasoning 社区中，"自提取约束是否有用"是一个广泛关注的问题。本文提供了迄今最系统的否定证据，具有 high practical value。

2. **实验覆盖面出色**：6 个模型（+3 个 frontier 跨模型验证）、4 个基准、27 种 remediation 策略、multi-seed replication、K/T sensitivity 分析、per-subtype breakdown——实验设计的广度和深度远超同类工作。

3. **统计方法论整体规范**：McNemar 配对检验、BH FDR 校正区分 confirmatory/exploratory、TOST 等价检验、bootstrap CIs、power analysis——对于一篇否定结果论文，统计处理达到了较高标准。

4. **诊断框架的实用性**：C₀, K_eff, BR 三个零成本诊断指标可以直接应用于其他 self-extraction 管线的预评估，具有直接的实践价值。

5. **问题解剖的层次性**：从"不 work"（§4）到"为什么不 work"（§5.1 SCB + Observation 1）到"能不能修"（§5.2, 27 策略失败）到"怎样才能 work"（§6, cross-arch escape），叙事逻辑清晰完整。

6. **写作质量高**：8 页正文信息密度极高，排版规范，figure 和 table 设计专业。22 页 appendix 提供了充分的细节支撑。

---

## Overall Assessment 详细理由

**评分：3.5（Borderline Conference）**

本文是一项严肃的否定结果研究，在 neuro-symbolic reasoning 社区有重要实践价值。实验覆盖面和统计方法论整体达到会议标准。

**支持 Conference 的因素**：
- 否定结果对社区有高 signaling value（避免大量后续工作重复验证）
- 实验设计的广度（27 interventions, 6+ models, multi-seed）是同类工作中最系统的
- 诊断框架有直接实用性
- 写作质量出色

**拉向 Findings 的因素**：
- 核心发现（self-extraction inherits distributional prior）事后看可预见——一旦意识到约束来自同一模型且 Z3 几乎不拒绝任何约束，degeneration 是自然推论
- 理论贡献有限：DPI bound 是标准结果，Observation 1 是代数平凡的，Markov chain identification 的深度有限
- 统计功效不足以支撑标题中 "No Measurable Improvement" 的强度——实际只能排除 ≥2pp 的效应
- Cross-architecture escape 基于单一架构（DeBERTa）和少量数据点（n=6 for ρ=1.0），初步性质明显
- ±2pp TOST margin 缺乏先验论证

**Confidence: 4/5**——对方法论和统计检验有充分把握，对 neuro-symbolic reasoning 领域的 novelty 标准有较好理解。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2284 · 2026-05-24T22:58:52.361395+00:00_

Reviewer 1 审稿意见已收到。评分 3.5（Borderline Conference），核心问题集中在 TOST margin 论证不足和统计功效与否定 claim 强度不匹配。

等待 Reviewer 2 审稿意见，收到后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 166

## Round 166

2 recorded events


### User

_source line 2285 · 2026-05-24T22:59:02.972312+00:00_

[Reviewer 1 审稿结果]:
审稿完成。已向 Review Director 提交完整审稿意见，评分 **Overall 3.5（Borderline Conference）**。

核心判断：
- **2 个 Must-Fix**：±2pp TOST margin 缺乏先验论证；统计功效不足以支撑标题中"No Measurable Improvement"的 claim 强度（MDE 1.86–4.84pp，无法排除 1–2pp 正效应）
- **5 个 Should-Fix**：Observation 1 理论贡献有限（代数平凡）、capability-gap pattern 仅基于 ~6 数据点、BR 与 Observation 1 循环、3–4 seeds 对否定声明支撑不足、GSM8K/AIME 样本过小
- **主要优势**：实验覆盖面出色（6 模型 + 27 interventions + multi-seed）、统计方法论整体规范、诊断框架有实用价值、叙事层次清晰

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2286 · 2026-05-24T22:59:10.307240+00:00_

Reviewer 1 审稿已收到（3.5 Borderline Conference）。等待 Reviewer 2 完成后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 167

## Round 167

6 recorded events


### User

_source line 2287 · 2026-05-24T22:59:54.839305+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（新颖性/完整性 + 写作格式）

---

## Paper Summary

本文研究了从 LLM 推理 trace 中提取形式化（FOL）约束并通过 MAX-SAT 求解器聚合是否能改进 Self-Consistency（多数投票）。作者提出 SICA（Symbolic Invariant Consensus Aggregation），在 6 个模型（7B–32B）、4 个推理基准、1200+ 实例上进行测试，发现 SICA 在 FDR 校正后无任何条件显著优于 SC。作者将此归因于 "Symbolic Confirmation Bias"（SCB）——自提取约束系统性地确认源 trace 的答案。论文通过有效集成规模 K_eff 和 DPI 形式化该机制，测试了 27 种无训练修复策略（均失败），并展示跨架构 NLI 验证器可打破此偏差。

---

## 总体评分

**Overall**: 3.5 / 5（Borderline Conference）

**一句话总结**: 方法论扎实、实验充分的否定性结果论文，实用价值明确，但 SCB 相对于已知现象的增量新颖性论证不足，是阻碍更高评分的核心障碍。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法（FDR、TOST、bootstrap CI、McNemar）得当，但 TOST 仅 4/11 条件确认等价，标题/摘要的否定声明存在过度概括风险；DPI 形式化依赖 source-attribution scoring 假设 |
| Excitement | 3.0/5 | 否定结果对社区有实用警示价值，诊断框架可直接部署，但核心洞察（自提取约束无效）可从 Huang et al. (2024) 的自纠正失败预期得到，变革性不足 |
| Reproducibility | 4.0/5 | 提供了详细的超参数、prompt 模板（Appendix A）、算法伪代码（Appendix B）、大量消融实验；代码/数据将在接收后发布 |
| Confidence | 4/5 | 熟悉相关领域（SC、neuro-symbolic reasoning、LLM self-correction），仔细检查了统计分析 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] SCB 与已知 CoT-level confirmation bias 的新颖性分离不足

- 具体位置：Section 5.1, Section Y（Extended Discussion, p.29）
- 问题：论文声称 SCB "is distinct from CoT unfaithfulness (Turpin et al., 2023) and CoT-level confirmation bias (Wan et al., 2025)"，但仅提供了**概念层面的区分**（"CoT unfaithfulness concerns whether stated reasoning reflects actual computation; SCB concerns whether self-extracted formal constraints mirror the model's answer distribution"），缺乏**直接的实证分离**。具体而言：
  - 如果 CoT trace 本身就是 unfaithful 的（Turpin et al., 2023），从 unfaithful trace 中提取的约束自然会继承该偏差——SCB 可能只是 CoT unfaithfulness 的下游效应，而非独立现象
  - 论文未设计消融实验验证：当 trace 是 faithful 的（如在 trace faithfulness 可控的合成设置下），SCB 是否仍然存在？
  - Wan et al. (2025) 的 CoT confirmation bias 已涵盖了 "推理过程系统性确认初始判断" 的核心机制，SCB 的增量贡献需要更强的实证而非仅靠概念区分
- 为什么影响接收：新颖性是论文能否被接收为 main conference 的关键考量。如果 SCB 可被归约为已知现象的实例化，则论文的贡献降级为 "在特定设置下验证已知现象"
- 建议修改方向：(1) 设计控制实验：在 trace faithfulness 可度量的设置下（如 ProofWriter 有完整推导链），比较 faithful trace 和 unfaithful trace 的 SCB 程度；(2) 或者诚实降低 novelty claim，将 SCB 定位为 "CoT confirmation bias 在 symbolic extraction 设置下的具体表现形式"，并强调诊断框架和 27-strategy exhaustive search 作为主要贡献

**N2** [critical] "No Measurable Improvement" 标题与统计证据的匹配度

- 具体位置：Title, Abstract（"no condition shows significant improvement after FDR control"）, Section 4 (Table 1), Appendix U (TOST analysis)
- 问题：
  - 标题宣称 "No Measurable Improvement"，但 TOST 等价检验仅在 **4/11 条件**确认 SICA ≈ SC（Appendix U, p.23）。其余 7 条件中 2 条显著退化、5 条统计功效不足（underpowered）
  - "No significant improvement after FDR" ≠ "No improvement exists"。前者是统计推断结果，后者是存在性声明。标题更接近后者的语义
  - MDE 分析（Appendix D, p.14）显示多数条件的 minimum detectable effect 为 1.86–4.84 pp，意味着 1–2 pp 的小正效应无法被检测到
  - 论文 p.5 自己承认 "Absence of evidence is not evidence of absence for small effects"，但标题未反映这一谨慎
- 为什么影响接收：标题是论文最重要的 framing 元素。如果标题过度概括统计证据，审稿人和读者会质疑论文的严谨性
- 建议修改方向：(1) 标题改为更精确的表述，如 "Self-Extracted Constraints Fail to Improve LLM Reasoning: Evidence for Symbolic Confirmation Bias"；(2) 或在 Abstract 中显式说明 "equivalence confirmed in 4 of 11 conditions; remaining conditions are underpowered for effects below ~2 pp"

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Section 5 信息密度过高，可读性受损

- 具体位置：Section 5（pp.5–7），约 2.5 页覆盖 SCB 定义 + 形式化（Observation 1, DPI）+ 27 策略失败 + 诊断框架
- 问题：
  - 27 种修复策略是论文的重要贡献之一（证明 bottleneck 是结构性的），但在正文中仅用一段 + Figure 5 引用处理，核心内容全部推到 Appendix I/J（pp.17–18）。读者无法从正文理解这些策略的分类逻辑和为何全部失败
  - DPI 形式化（Observation 1）的推导也高度压缩，从 degeneration condition 到 DPI bound 的推导在一段内完成
  - 诊断框架（BR, K_eff, CCR）三个指标各仅获得 1-2 句描述
- 建议：考虑将 Section 5 拆分为两个独立 section：(1) SCB 机制与形式化，(2) 修复策略失败与诊断框架。或者将 Figure 5 移入正文并增加分类讨论的段落

**W2** [warning] Cross-architecture escape 验证不充分，应明确标注为 exploratory

- 具体位置：Section 6（p.7–8），Table 2（p.8）
- 问题：
  - 仅使用一种 NLI 架构（DeBERTa），一个主要数据集（ProofWriter），验证样本有限
  - Table 2 显示仅 Mistral-7B (SC below verifier) 获得显著正向增益（+3 pp），其余条件 n.s.
  - Limitations（p.8）已承认 "validated with a single NLI architecture"，但正文 Section 6 和 Abstract 将其作为三大贡献之一呈现，给读者的印象是这是一个已验证的方案而非初步证据
- 建议：在 Section 6 开头和 Abstract 中明确标注 "preliminary evidence" 或 "exploratory"。当前 Abstract 表述 "A cross-architecture encoder-only verifier escapes the bias (+6.67 pp, p < 0.001)" 给人以为这是稳健结论的印象

**W3** [warning] 缺少与 PRM/ORM/learned verification 的系统性对比讨论

- 具体位置：Section 2（Related Work, p.2），Section 7（Discussion, p.8）
- 问题：
  - 论文在 Related Work 提到 "Trained verifiers can escape this bottleneck through external reward signals: outcome and process reward models (Cobbe et al., 2021; Lightman et al., 2024; Wang et al., 2024)"，但未讨论 PRM/ORM 与 symbolic verification 的 trade-off
  - 论文的核心论点是 same-model symbolic extraction 失败，cross-architecture verification 成功——这与 PRM/ORM 的成功机制（独立训练的验证信号）高度相关，但论文未建立这一联系
  - 读者自然会问：如果 symbolic verification 不行，PRM/ORM 是否是更好的替代？论文应提供系统性的 trade-off 分析
- 建议：在 Discussion 中增加一段讨论 symbolic vs. learned verification 的 trade-off（训练成本、可解释性、domain transferability）

**W4** [warning] "Symbolic Mirage" 术语的恰当性

- 具体位置：Section 5 标题，Abstract
- 问题：论文将自提取约束无效的现象命名为 "Symbolic Mirage"，暗示这些约束是 "幻象"。但根据论文自己的分析（Section 5.1, p.5-6），这些约束在 Z3 层面 99% 以上是命题级别的合法约束（propositional at Z3 level），只是它们系统性地与源 trace 的答案对齐。称合法但有偏差的约束为 "mirage" 有修辞过度之嫌
- 建议：不需要改名（术语已建立），但应在首次使用时加注释说明 "mirage" 指的是约束的 discriminative value 而非其 logical validity

---

## 小问题（不影响接收）

- **M1**: Abstract 词数约 193–200 words（经脚本统计 ~193 去除 LaTeX 命令后），处于限制边界。建议精简至 190 words 以下留有余量
- **M2**: Figure 2（p.5）x 轴标签 "Fleiss' κ (inter-trace agreement)" 与 y 轴 "Δ (pp) vs. Self-Consistency" 的含义需要在正文中更早引入 κ 的定义（当前首次出现在 Section 5 的 K_eff 公式中，但 Figure 2 在 Section 4）
- **M3**: Table 1（p.5）分为三个regime（Type C/Intermediate/Type A），但 regime 划分标准（SC accuracy 区间）仅在 Figure 2 caption 和 p.4-5 散见，建议在 Table 1 caption 中直接说明
- **M4**: Limitations section（p.8）为单段约 150 words，结构清晰覆盖 6 个要点，符合 EMNLP 2026 要求
- **M5**: 论文使用 `\usepackage[review]{acl}` 和 "Anonymous ACL submission"，double-blind 合规

---

## 主要优势

1. **实验设计的彻底性**：6 个模型 × 4 个基准 × 多种配置，加上 27 种修复策略的穷尽搜索，构成了对 "symbolic self-extraction for SC improvement" 这一研究方向的近乎完备的否定证据
2. **统计方法的严谨性**：FDR 校正、TOST 等价检验、bootstrap CI、McNemar test、permutation test 的组合使用超出了该领域论文的平均统计水平
3. **诊断框架的实用价值**：BR、K_eff、CCR 三个零成本指标可从单次 pilot run 预测全量实验结果，对 neuro-symbolic pipeline 的实践部署有直接指导意义
4. **形式化分析的深度**：通过 DPI 建立 self-extraction 的信息论 bottleneck，从 Observation 1（degeneration condition）到 K_eff 的推导链条完整
5. **附录质量高**：30 页附录包含 case studies（Appendix F）、per-subtype analysis（Appendix G-H）、constraint quality analysis（Appendix S）、multi-seed replication（Tables 42-44），为论文结论提供了充分的可追溯支撑

---

## Questions for Authors

1. 是否可以在 trace faithfulness 可控的设置下（如 ProofWriter 有完整推导链的子集）直接检验 SCB 是否独立于 CoT unfaithfulness？
2. Table 2 的 cross-architecture 结果中，为什么只有 "SC below verifier" 条件显著？这是否暗示 cross-architecture escape 本身也有结构性限制（只在 generator 较弱时有效）？
3. 27 种修复策略中，Cross-model 和 Generational 方法（Figure 5）产生了最大的正向效应（虽然 n.s.），这两类方法的共同点是什么？是否暗示 partial independence 可能在更大规模实验中产生显著效应？
4. 论文在 Section 3.2 提到 StrategyQA (n=320) 作为数据集之一，但 Table 4 (Appendix C) 注释显示 "extraction diagnostics were not computed (StrategyQA uses boolean answers without symbolic predicates)"。StrategyQA 上的约束提取具体如何实现？其 SCB 表现是否与 FOLIO/ProofWriter 一致？

---

## Missing References

- Wan et al. (2025) "Unveiling confirmation bias in chain-of-thought reasoning" — 已引用，但应更深入讨论其与 SCB 的关系
- 建议增引：Anthropic (2024) 或相关工作关于 LLM reasoning faithfulness 的系统性研究，可强化 SCB vs. CoT unfaithfulness 的讨论
- PRM 领域：Lightman et al. (2024) "Let's Verify Step by Step" 已引用，但缺少 Math-Shepherd (Wang et al., 2024) 等 process-level verification 的对比讨论

---

## 格式合规检查

| 检查项 | 结果 |
|--------|------|
| 页数（主文 ≤8页） | ✅ 主文 Sections 1-7 在第 8 页结束，Limitations 在第 8 页底部（不计入页数） |
| Abstract ≤200 words | ⚠️ ~193-200 words（边界），建议精简 |
| 模板 `[review]{acl}` | ✅ |
| Double-blind | ✅ "Anonymous ACL submission" |
| Limitations section | ✅ 单段，覆盖 6 个要点，位于正文末尾（References 前） |
| References 格式 | ✅ 使用 acl_natbib，格式一致 |

---

## Overall Assessment 详细理由

**3.5 (Borderline Conference)**

**支持接收的因素**：
- 否定结果对社区有重要警示价值，阻止了一个看似合理但实际无效的研究方向
- 实验设计和统计分析的彻底性超出领域平均水平
- 诊断框架有直接的实践部署价值

**阻碍更高评分的因素**：
- SCB 的新颖性论证是论文最大弱点——如果 SCB 只是 CoT confirmation bias 在 symbolic extraction 设置下的实例化，则核心贡献降级
- "No Measurable Improvement" 的 framing 与实际统计证据（4/11 TOST 确认）存在张力
- Cross-architecture escape 作为三大贡献之一，验证深度不足

**Confidence**: 4/5 — 对相关领域（SC, neuro-symbolic reasoning, LLM self-correction）有充分了解，仔细检查了统计分析方法和实验设计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2288 · 2026-05-24T23:00:48.019638+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "symb_invariant_consensus",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每个要点使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Summary\n\n本文提出 Symbolic Invariant Consensus Aggregation (SICA)，从 LLM 推理 trace 中提取 FOL 约束并通过加权 partial MAX-SAT 聚合，测试其能否超越 Self-Consistency (SC)。核心发现为否定结果：在 6 个模型（7B–32B）、4 个基准、1,200+ 实例上，SICA 与 SC 在 FDR 校正后无统计显著差异。论文将此诊断为\"symbolic confirmation bias\"（自提取约束系统性支持模型多数答案），提出 Observation 1（Argmax Preservation）形式化机制，测试 27 种 training-free 补救策略均失败，并展示 cross-architecture NLI verifier 的初步逃逸证据。\n\n### Overall: 3.5 / 5（Borderline Conference）\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] ±2pp TOST 等价性 margin 缺乏充分论证\n- 论文使用 ±2pp 作为 TOST 等价性检验的预设 margin，声称 4 个条件通过等价性检验。但 ±2pp 的选择缺乏先验论证——为什么 2pp 而不是 1pp 或 3pp？在 SC baseline 40%–86% 范围内，2pp 的实际意义差异巨大。Appendix U 说\"regardless of the chosen margin, no condition shows a significant positive SICA effect\"，但这只说明没有正向效应，不能证明 ±2pp 是合理的等价边界。\n- 否定结果论文的核心贡献取决于\"SICA 不优于 SC\"的 claim 强度。标题 \"No Measurable Improvement\" 与实际 MDE 1.86–4.84pp 不匹配。\n- 建议：提供 ±2pp 的先验论证；报告多 margin 下的 TOST 结果；将标题/abstract 否定语气软化。\n\n**N2** [critical] 否定结果的统计功效不足以支撑论文核心 claim 的强度\n- Table 1 caption 承认 \"All conditions have McNemar power < 80% for |Δ| = 2pp\"。MDE 为 1.86–4.84pp，不能排除 1–2pp 正效应。\n- Qwen3-14B 4-seed 均值 Δ = +0.92 ± 1.14pp，如果效应在 ~1pp 量级，当前设计无法检测。Limitations 承认 \"small positive effects cannot be ruled out\"，但与标题/abstract 矛盾。\n- 建议：增大样本量；在 abstract 中限定 claim 范围；考虑 meta-analytic 功效分析。\n\n---\n\n### Should-Fix 问题\n\n**W1** Observation 1 理论贡献有限——三个条件成立时结论是 Eq. 3 的直接代数推论，实际贡献在于实证验证条件成立。CV=0.26 的约束产出均匀性需更深入讨论。\n\n**W2** Capability-gap pattern 基于 ~6 数据点的 Spearman ρ=1.0，过度推断风险。\"weaker generator + stronger verifier = gain\" 本身是 ensemble learning 基本原理。\n\n**W3** BR 与 Observation 1 循环——BR_excess ≈ 0 意味着 BR 不增加超越 Observation 1 的信息。BR 在论文中占显著篇幅但独立贡献有限。\n\n**W4** 3-4 seeds 对否定声明支撑有限——Mistral-7B Δ 分布 [+2.94, 0.00, -2.45]pp，std=2.70pp，单 seed 结果高度不可靠。\n\n**W5** GSM8K (n=30) / AIME (n=22) 样本过少，应更明确标记为 illustrative examples。\n\n---\n\n### Questions\n\nQ1: ±2pp TOST margin 是否有预注册或先验论证？\nQ2: Observation 1 条件 (iii) 中 CV=0.26 是全局平均——是否存在特定问题子集 CV>0.5？这些问题上 SICA 是否表现不同？\nQ3: 如果 BR_excess ≈ 0，BR 作为诊断指标相比直接使用 trace-count 分布有何增量价值？\nQ4: few-shot extraction 和 iterative refinement 被排除——是否有初步实验或理论论证？\nQ5: DeBERTa 在 FOLIO 上 standalone 仅 49.51%，如果 w 调更高（w=5/10），能否在 FOLIO 上也获得显著 gain？\n\n---\n\n### Missing References\n- Lightman et al. (2023) \"Let's Verify Step by Step\" 和 Cobbe et al. (2021) 已在 references 但正文引用不充分。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每个要点使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Summary\n\n本文提出 Symbolic Invariant Consensus Aggregation (SICA)，从 LLM 推理 trace 中提取 FOL 约束并通过加权 partial MAX-SAT 聚合，测试其能否超越 Self-Consistency (SC)。核心发现为否定结果：在 6 个模型（7B–32B）、4 个基准、1,200+ 实例上，SICA 与 SC 在 FDR 校正后无统计显著差异。论文将此诊断为\"symbolic confirmation bias\"（自提取约束系统性支持模型多数答案），提出 Observation 1（Argmax Preservation）形式化机制，测试 27 种 training-free 补救策略均失败，并展示 cross-architecture NLI verifier 的初步逃逸证据。\n\n### Overall: 3.5 / 5（Borderline Conference）\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] ±2pp TOST 等价性 margin 缺乏充分论证\n- 论文使用 ±2pp 作为 TOST 等价性检验的预设 margin，声称 4 个条件通过等价性检验。但 ±2pp 的选择缺乏先验论证——为什么 2pp 而不是 1pp 或 3pp？在 SC baseline 40%–86% 范围内，2pp 的实际意义差异巨大。Appendix U 说\"regardless of the chosen margin, no condition shows a significant positive SICA effect\"，但这只说明没有正向效应，不能证明 ±2pp 是合理的等价边界。\n- 否定结果论文的核心贡献取决于\"SICA 不优于 SC\"的 claim 强度。标题 \"No Measurable Improvement\" 与实际 MDE 1.86–4.84pp 不匹配。\n- 建议：提供 ±2pp 的先验论证；报告多 margin 下的 TOST 结果；将标题/abstract 否定语气软化。\n\n**N2** [critical] 否定结果的统计功效不足以支撑论文核心 claim 的强度\n- Table 1 caption 承认 \"All conditions have McNemar power < 80% for |Δ| = 2pp\"。MDE 为 1.86–4.84pp，不能排除 1–2pp 正效应。\n- Qwen3-14B 4-seed 均值 Δ = +0.92 ± 1.14pp，如果效应在 ~1pp 量级，当前设计无法检测。Limitations 承认 \"small positive effects cannot be ruled out\"，但与标题/abstract 矛盾。\n- 建议：增大样本量；在 abstract 中限定 claim 范围；考虑 meta-analytic 功效分析。\n\n---\n\n### Should-Fix 问题\n\n**W1** Observation 1 理论贡献有限——三个条件成立时结论是 Eq. 3 的直接代数推论，实际贡献在于实证验证条件成立。CV=0.26 的约束产出均匀性需更深入讨论。\n\n**W2** Capability-gap pattern 基于 ~6 数据点的 Spearman ρ=1.0，过度推断风险。\"weaker generator + stronger verifier = gain\" 本身是 ensemble learning 基本原理。\n\n**W3** BR 与 Observation 1 循环——BR_excess ≈ 0 意味着 BR 不增加超越 Observation 1 的信息。BR 在论文中占显著篇幅但独立贡献有限。\n\n**W4** 3-4 seeds 对否定声明支撑有限——Mistral-7B Δ 分布 [+2.94, 0.00, -2.45]pp，std=2.70pp，单 seed 结果高度不可靠。\n\n**W5** GSM8K (n=30) / AIME (n=22) 样本过少，应更明确标记为 illustrative examples。\n\n---\n\n### Questions\n\nQ1: ±2pp TOST margin 是否有预注册或先验论证？\nQ2: Observation 1 条件 (iii) 中 CV=0.26 是全局平均——是否存在特定问题子集 CV>0.5？这些问题上 SICA 是否表现不同？\nQ3: 如果 BR_excess ≈ 0，BR 作为诊断指标相比直接使用 trace-count 分布有何增量价值？\nQ4: few-shot extraction 和 iterative refinement 被排除——是否有初步实验或理论论证？\nQ5: DeBERTa 在 FOLIO 上 standalone 仅 49.51%，如果 w 调更高（w=5/10），能否在 FOLIO 上也获得显著 gain？\n\n---\n\n### Missing References\n- Lightman et al. (2023) \"Let's Verify Step by Step\" 和 Cobbe et al. (2021) 已在 references 但正文引用不充分。"
  }
}
```

</details>

---


### Tool result

_source line 2289 · 2026-05-24T23:01:18.956068+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30936
}
```

</details>

---
