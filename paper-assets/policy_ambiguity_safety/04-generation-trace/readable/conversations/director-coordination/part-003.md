# Director coordination — Part 3 of 11

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../director-coordination.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/0e/0e806c5d99edfa05e2ae.json)

## Round 58

### User

_source line 607 · 2026-05-21T15:44:58.299347+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: Authorization scope 测量可靠性过低**

同意这是一个实质性问题。Page 9 Cross-judge asymmetry 段落确认 authorization scope 的 cross-judge κ = 0.365，是六类中最低的。Table 9（Appendix G, Page 13）显示 human-LLM agreement 对 auth scope 为 κ = 0.644，虽然比 cross-judge 高，但仍是所有类型中最低的（对比 lexical κ = 0.962）。n = 34 的 per-type 样本量确实不足以产生精确估计。

**但需要补充一个重要 nuance**：matched-pair 设计意味着每个 model 的 ambiguous vs. unambiguous 对由同一 judge 评估，因此 auth scope 的 **Δpp（within-model treatment effect）** 受 judge 内部一致性保护，不完全取决于 cross-judge 一致性。"Canary type" claim 的核心是 auth scope 的 Δpp 在模型间变异最大（Claude 12% → GPT-5.4 64%，Figure 3 Page 7），而非其绝对违规率。Cross-judge disagreement 主要影响绝对率的置信区间，对 within-model Δpp 的影响较小。

尽管如此，R1 的建议（增加 human validation 样本、在 Abstract/Conclusion 加 measurement-uncertainty caveat）完全合理，应当采纳。

---

**[REBUT] R1-N2: Judge-model confounding — 部分反驳**

R1 的担忧对**跨模型比较（C3）有效**，但对**核心 claim（C1, C2）过度放大了威胁**。原因如下：

1. **Matched-pair design 的内建保护**：每个 model 的 treatment effect（Δpp = ambiguous − unambiguous violation rate）由同一 judge 评估。Judge systematic bias（如某 judge 偏严/偏松）在 Δpp 中完全抵消。这意味着 **C1（overall ambiguity effect）和 C2（type hierarchy within each model）不受 judge-model confounding 影响**，因为这两个 claim 都基于 within-model 的 paired comparison。

2. **C3 确实受影响，但论文已适当处理**：Section 5.4 明确将 C3（model×type interaction, 2.9% of variance）标注为 "exploratory"，Page 9 的 Cross-judge asymmetry 段落承认 "neither subgroup reaches significance for C3 individually (GPT-4.1-judged: p = 0.059; GPT-5.4-judged: p = 0.157)"。论文将 C3 定位为 exploratory finding 而非 confirmed claim，这是恰当的。

3. **关于 GPT-4.1 judging GPT-5.4 的能力不对称**：R1 说的方向可能相反——如果 lower-capability judge（GPT-4.1）judging frontier model（GPT-5.4），更可能的 bias 是**低估** GPT-5.4 的 subtle violations（因为 GPT-4.1 可能无法识别 frontier model 的 nuanced compliance failures）。这会使 GPT-5.4 的违规率被**低估**而非高估，即 confound 方向与论文的 "GPT-5.4 auth scope 最高 64%" 发现**相反**——如果有 bias，真实值可能更高，加强而非削弱结论。

4. **对 R1 建议的回应**："对所有 5 个 model 用两个 judge 分别评估 subset" 需要 2× 的 API 成本和 episode 数。作为 revision 可以做 subset overlap（如每个模型 50-100 episodes 双 judge），但全量 double-judge 不太现实。

**结论**：R1-N2 对 C3 有效（论文已 hedge），但不构成对 C1/C2 的威胁。建议在 Method 中增加一段 explicit 解释 matched-pair design 为何保护 within-model comparisons from judge bias。

---

**[AGREE] R1-N3: 缺少 a priori power analysis — 同意但需区分情况**

同意论文应报告 power analysis。但需要区分不同 claim 对 power 的依赖程度：

- **C1（overall ambiguity effect）**：effect size 极大（Δ = 34.0 pp, OR = 15.1, p < 10⁻¹⁶），n = 300 pairs × 5 models = 1,497 matched pairs（ambiguous-only vs. 1,500 unambiguous）。即使最保守的 power analysis 也会确认 n 远超所需。**Power 不是 C1 的问题。**

- **C2（type hierarchy）**：TOST equivalence testing 的 power 确实取决于 SESOI。R1 正确指出 ±10pp 时仅 3/6 mid-tier pairs equivalent（Appendix A, Page 11 TOST sensitivity analysis）。这不是 power 不足的问题，而是 SESOI 选择的问题——见 R1-W2。

- **Per-type per-model cells (n ≈ 50)**：这里 power 确实不足。论文在 Page 14（Appendix 末尾）也承认 "per-type estimates are imprecise due to small cell sizes (n = 32–34); type-level ranking should not be over-interpreted"。

建议：报告 post-hoc power analysis，至少对 C1、C2 的 TOST、和 per-type interaction 分别报告。对 C1 来说这会确认 power > 0.99；对 per-type cells 会诚实地显示 power 不足。这种分层报告比简单地说"缺少 power analysis"更有信息量。

---

### Should-Fix 问题

**[AGREE] R1-W1: Incompleteness confound hedging 在 Abstract/Conclusion 中不足**

强烈同意。这与我的 N2（information-addition confound）高度重合。Appendix F 提供了 logistic regression 控制 information delta 的分析，但主文 Abstract 和 Conclusion 中缺乏对应的 caveat。Incompleteness "universally dangerous" 的表述未加限定语，读者可能将其解读为 ambiguity effect 而非 information-absence effect。

建议：Abstract 中加入一句如 "though incompleteness effects may partially reflect information absence rather than ambiguity per se (Appendix F)"。

---

**[AGREE] R1-W2: TOST SESOI ±15pp 缺乏外部锚定**

同意。±15pp 作为 equivalence bound 的选择缺少 domain-specific 的 justification。论文 Section 4.5 提到 "this margin substantially exceeds the perturbation bound (6.67 pp CI upper bound)"，即用 perturbation control 的 CI 作为间接锚定——但这是循环论证（用自己的数据定义"什么算等价"）。

Appendix A 的 sensitivity analysis 是一个好的补充，但 R1 指出在 ±10pp 时仅 3/6 mid-tier pairs equivalent，这削弱了 "robust two-tier structure" 的 claim 强度。真正需要的是外部锚定——例如，policy compliance 领域中 "practically meaningful" 的违规率差异是什么？如果 ±10pp 是更合理的 SESOI，type hierarchy 就从 "two robust tiers" 变成 "one clear outlier (incompleteness) + a gradient"。

---

**[AGREE] R1-W3: ICC = 0.919 仅限 OpenAI 模型**

同意。Section 4.4 报告 ICC = 0.919 (95% CI [0.892, 0.940])，但 "ICC is computed within the OpenAI model family; cross-provider reproducibility is not directly measured"（Page 5）。论文诚实地承认了这一点，但 Appendix E 的 replication（Gemini, LLaMA）使用的是 GPT-5.4 作为 judge，未报告 replication models 之间的 ICC。跨 provider 的 ICC 是一个有价值的补充分析。

---

**[AGREE] R1-W4: Mitigation experiment (Table 2) 样本量过小**

同意，且这与我的 N1（页数超限）问题直接相关。Table 2 在 Page 9 占约 1/3 页空间，是导致主文超出 8 页限制的主要因素之一。每个 cell 约 50 episodes（"~50 per cell"，Page 9 Table 2 caption），其中 coreferential 未测试。将 Table 2 移至 Appendix 可以同时解决两个问题：(1) 释放主文空间修复页数超限；(2) 将 preliminary results 放在更适当的位置。主文保留 1-2 句总结（"Disambiguation instructions reduce violations by ~8.5 pp overall; detailed results in Appendix B"）即可。

---

**[AGREE] R1-W5: Failure mode taxonomy inter-coder κ = 0.52**

同意。κ = 0.52（moderate agreement）对于作为 Contribution 4 提出的 failure mode taxonomy 来说偏低。这与我的 W2（Contribution 4 与 Contribution 1 重叠）形成合力：如果 failure mode taxonomy 的 reliability 只有 moderate，且它本质上是 taxonomy 的 downstream finding 而非独立贡献，那么将其列为独立 contribution 就更难站住脚了。

建议：(1) 如果保留 Contribution 4，需要做 iterative coding 提高 reliability（至少达到 κ ≥ 0.67）；(2) 或者降级为 exploratory analysis 而非 contribution。

---

### R1 Questions 的回应

**Q1: 50 pairs/type 的决定依据？**
[AGREE] 论文未 justify 这个数字。应补充。如果基于 pilot study 或 resource constraints，应说明。

**Q2: Per-model judge agreement 分布？**
Appendix G Table 9（Page 13）提供了 per-type human-LLM agreement，但未按 per-model 拆分。R1 要求的是按每个 model 分别报告 judge agreement——这是一个合理的 request，特别是考虑到 N2 中 judge-model confounding 的担忧。

**Q3: Logistic regression 控制了哪些变量？**
Section 5.4（Page 5-6）提到 logistic regression with model×type interaction，但具体的 covariates 不够 explicit。从文本推断包括：condition（ambiguous/unambiguous）、model identity、ambiguity type、model×type interaction term。但是否控制了 episode-level features（如 policy complexity、task type）不清楚。应在 revision 中明确列出完整 model specification。

**Q4: Template-based pipeline 的 structural correlation？**
[AGREE] Section 4.1 提到 clause pairs 通过 "template-based pipeline" 生成，这可能引入 structural artifacts（所有同类型 pairs 共享生成模板，导致类内方差被低估）。Perturbation control（Section 4.5）控制了 non-ambiguity surface changes，但未直接控制 template-induced correlation。这是一个 valid concern，但严重性中等——template 保证了 type operationalization 的一致性（优势）的同时也引入了 structural dependence（代价）。

**Q5: 3 episodes API error 是否引入 selection bias？**
3/2,997 = 0.1%，可忽略不计。除非这 3 个 episode 在某种系统性维度上特殊（如特定 type 或 model），否则 selection bias 风险极小。应报告这 3 个 episode 的 type/model 分布以完全排除。

**Q6: C3 inconclusive 保留在主文的理由？**
[REBUT] 报告 null/inconclusive 结果是好的科学实践。C3 的 "model×type interaction explains only 2.9% of variance" 本身是一个有信息量的结论——它告诉读者 type hierarchy 主要由 type 而非 model 驱动。删除 C3 会使论文只报告 positive results，反而损害完整性。论文已将 C3 标注为 "exploratory"，这种处理是恰当的。

---

### 与 R1 的整体评分一致性评估

R1 和我均给出 **Overall 3.5（Borderline Conference）**，核心判断一致：
- **共识**：matched-pair causal design 是主要方法论贡献；incompleteness confound 需要更 explicit 的 hedging；page limit 违规需要修复
- **分歧**：R1 更关注 measurement reliability（judge confounding, power analysis），我更关注 novelty（Differential Nocuity 框架缺乏形式化、与 DRIP-R 的差异化）
- **互补**：R1 的 N2（judge-model confounding）和我的 N2（information-addition confound）分别从测量端和设计端指出了不同的威胁——两者结合构成了对 type hierarchy claim 的完整 challenge

如果作者能在 revision 中：(1) 修复页数超限，(2) 在主文 explicit 处理 incompleteness confound 并报告 effect size 变化，(3) 增加 auth scope 的 human validation 样本或加 uncertainty caveat，(4) 补充 power analysis——我认为论文可以从 3.5 提升到 4.0（Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-21T15:45:23.449900+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_local_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_local_file",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-21T15:45:23.500782+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-21T15:45:26.914140+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 611 · 2026-05-21T15:45:27.366349+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T15:31:46.064066+00:00\", \"completed_at\": \"2026-05-21T15:35:10.191303+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 9\", \"message\": \"主正文（至 Conclusion 末尾）延伸至第 9 页约 3/4 处，超出 EMNLP 2026 的 8 页正文限制（Limitations 不计页数但 Conclusion 仍在第 9 页），需压缩约 0.75 页\"}, {\"severity\": \"critical\", \"dimension\": \"page 14\", \"message\": \"最后一页仅 ~10 行文字（约 10% 填充），其余 ~90% 完全空白，视觉观感极差\"}, {\"severity\": \"warning\", \"dimension\": \"pages 3-5\", \"message\": \"连续 3 页纯文本无任何 display item（§3 Taxonomy + §4 Experimental Setup），审稿人容易在此段失去注意力。建议在 §3 添加 taxonomy 层级表/树状图，或将 §4 的实验设计可视化\"}, {\"severity\": \"warning\", \"dimension\": \"page 13\", \"message\": \"6 个表格（Tables 4-9）挤在同一页，字号过小，阅读体验差。建议拆分为 2 页或精简合并部分表格\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"纯文本页（Error Analysis §6 + Discussion §7 开头），与前面 pp6-7 的图表密集区形成对比，但 §6 属于定性分析，可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 子面板内的文字字号偏小（约为正文字号的 60-65%），建议适当增大或简化面板内文字\"}, {\"severity\": \"info\", \"dimension\": \"pages 6-7\", \"message\": \"Figure 2 和 Figure 3 的颜色方案不完全一致——Figure 2 用分组柱状图配色，Figure 3 用热力图梯度配色，同一 ambiguity type 在两图中的颜色语义不同，建议统一\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Table 2 中负值用负号标注但未用颜色或箭头辅助区分正负效果方向\"}], \"counts\": {\"critical\": 2, \"warning\": 3, \"info\": 3}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-21T15:45:27.366780+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-21T15:45:28.722077+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-21T15:45:28.823651+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Read existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Read existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-21T15:45:28.974958+00:00_

## Round 6 (Fresh) Review Issues — policy_ambiguity_safety
## Paper: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
## Venue: EMNLP 2026 via ARR May cycle
## Date: 2026-05-21
## Round 6 Score: 3.5 (Borderline Conference)
## Note: Fresh review session — prior rounds' resolutions re-evaluated from scratch

# ============================================================
# CRITICAL ISSUES
# ============================================================

- id: "MF3"
  summary: "Incompleteness confound — logistic regression 控制不充分，three-tier hierarchy 依赖 confounded type"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 6
  mentions:
    - round: 4
      note: "Previously marked resolved via §5.2 confound discussion + logistic regression + coreferential lower-bound"
    - round: 6
      note: "R1+R2 consensus: (1) coefficient change direction unreported; (2) token count is crude proxy for information content; (3) excluding incompleteness, omnibus p=0.079 non-significant → hierarchy degrades to two-tier; (4) coreferential 'lower bound' logic assumes information addition only increases violations"
  resolution: "Reframed from three-tier to 'robust two-tier structure among five types, with incompleteness as an upper bound partly reflecting an information-addition confound' across Abstract, Intro, §5.2, Figure 2, Conclusion. Honest about p=0.079 and confound."
  resolution_round: 6

- id: "MF4"
  summary: "C4 [Exploratory] 仍在 Discussion/Abstract 中做强因果推断"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 3
  last_seen_round: 6
  mentions:
    - round: 4
      note: "Previously marked resolved by adding [Exploratory] tag"
    - round: 6
      note: "R1+R2 consensus: (1) 'safety training does not uniformly reduce' is causal claim unsupported by cross-sectional design; (2) RLHF mechanism speculation lacks mechanistic evidence; (3) 'canary type' based on 5 models × 1 typ
…[truncated 8518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-21T15:47:17.611657+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Round 7 (Fresh) Review Issues — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Date: 2026-05-21\n## Round 7 Score: 3.5 (Borderline Conference)\n## Note: Fresh review session — all issues re-evaluated from scratch\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"主文超出 EMNLP 2026 8 页正文限制约 0.5-0.7 页\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R2 raised, R1 AGREE. Discussion 跨页到 Page 9, Table 2 + Conclusion 均在 Page 9. ARR desk reject 风险. 视觉审查同样标记为 critical.\"\n  action_items:\n    - round: 7\n      action: \"Table 2 移至 Appendix (省约 1/3 页); Discussion 压缩重复措辞 ('upper bound...confound' 逐字重复 ≥4 次); Introduction contribution list 精简\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N2\"\n  summary: \"Authorization scope 测量可靠性过低 (cross-judge κ=0.385) 无法充分支撑 canary type 主张\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R1 raised, R2 AGREE with nuance (matched-pair Δpp 受 within-judge 一致性保护, 但绝对率不确定性大). Per-type validation n=34 不足; human-LLM κ=0.644 CI=[0.35,0.91] 极宽. Abstract/Conclusion 突出 canary type 但无 measurement-uncertainty caveat.\"\n  action_items:\n    - round: 7\n      action: \"在 Abstract/Conclusion 对 canary type 加 measurement-uncertainty caveat; 增加 auth scope human validation 样本或报告 within-judge raw agreement + detection vs severity 分离分析\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N3\"\n  summary: \"Incompleteness information-addition confound 在 Abstract/Conclusion 中 hedging 不足\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R2 raised as critical (confound 未充分处理), R1 AGREE with nuance (分析控制已在但呈现方式需改善). 共识: Abstract 'universally dangerous' 和 Conclusion 'universal blind spot' 措辞过强; Appendix F 仅报告 'coefficient change <8%' 缺 OR 变化量.\"\n  action_items:\n    - round: 7\n      action: \"报告 logistic regression 控制前后 OR 变化量; Abstract/Conclusion 加限定语 ('though partly reflecting information-addition confound'); 考虑将 incompleteness 在 type hierarchy 排序中单独讨论\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N4\"\n  summary: \"缺少 a priori power analysis, 50 pairs/type 的样本量合理性未论证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R1 raised, R2 AGREE with nuance (C1 power 显然充足 >0.99, 但 TOST equivalence 和 per-type per-model cells n≈50 power 不明确). Two-tier structure 依赖 TOST null 结果, 无 power analysis 无法区分 'types equivalent' vs 'lack power'.\"\n  action_items:\n    - round: 7\n      action: \"报告 post-hoc power analysis: C1 (确认 >0.99), TOST equivalence (报告 detectable minimum effect), per-type interaction (诚实报告不足). 若 TOST power 不足则缩小 C2 claim.\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R7-W1\"\n  summary: \"Judge-model confounding 对 C4 model-level 结论的限制\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R1 raised as critical, R2 REBUT to warning: matched-pair design 保护 within-model C1/C2 (judge bias 在 Δpp 中抵消), 仅 C4 cross-model 比较受影响. GPT-4.1 judging GPT-5.4 的能力不对称方向与结论相反 (低估而非高估违规). 共识: 对 C1/C2 非威胁, 对 C4 需在 Method 中 explicit 解释.\"\n  action_items:\n    - round: 7\n      action: \"在 Method 增加一段解释 matched-pair 为何保护 within-model comparisons; C4 结论中明确标注 judge-model confounding 限制\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"Differential Nocuity 被呈现为 framework 但缺乏形式化\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R2 raised as critical, R1 REBUT: conceptual organizing principle (类似 good-enough processing) 不需要 formal model. 共识: 非 critical, 但 Discussion 应更明确阐述框架组成部分 (type hierarchy + channel availability + systematic nocuity).\"\n  action_items:\n    - round: 7\n      action: \"Discussion §7 开头用 2-3 句话明确 Differential Nocuity 的组成部分; 或降级为 empirical observation 而非 framework\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W3\"\n  summary: \"TOST SESOI ±15pp 缺乏外部锚定, tier structure 对 margin 选择敏感\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R1 raised, R2 AGREE. ±10pp 时仅 3/6 mid-tier pairs equivalent, ±12pp 时 5/6. 'Robust two-tier structure' 主要在 ≥15pp 成立. Perturbation CI 锚定有循环论证嫌疑.\"\n  action_items:\n    - round: 7\n      action: \"主文讨论 SESOI 敏感性; 报告 minimum SESOI at which two-tier emerges (~±12pp); 寻找外部锚定\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W4\"\n  summary: \"Table 2 (mitigation experiment) 样本量不足 (~50/cell) 却在主文 Discussion 占重要位置\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R1 W4 + R2 交叉 AGREE. DeepSeek scopal +2.0pp / incompleteness +4.0pp 显示 mitigation 不稳定. 移至 Appendix 同时解决页数超限问题.\"\n  action_items:\n    - round: 7\n      action: \"Table 2 移至 Appendix; 主文保留 1-2 句方向性总结\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W5\"\n  summary: \"与 DRIP-R (concurrent work) 差异化论述不够有力\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R2 raised, R1 部分同意. §2 仅两句话说明差异, 需要更 explicit 的 contribution delta (type overlap, conclusion consistency, beyond matched-pair design).\"\n  action_items:\n    - round: 7\n      action: \"Related Work 增加详细对比段落或表格\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W6\"\n  summary: \"Human validation 缺少 annotator blindness, disagreement distribution 等细节\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R2 raised, R1 AGREE. 缺: annotator 具体背景, blind to condition?, disagreement 按 type 分布, 100 episodes 抽样策略.\"\n  action_items:\n    - round: 7\n      action: \"补充 1-2 句 annotator selection, blindness, stratification\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W7\"\n  summary: \"Failure mode taxonomy inter-coder reliability 偏低 (Cohen's κ=0.52)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R1 raised, R2 AGREE. Moderate agreement; arbitrary rule selection κ=0.29. 作为 Contribution 之一 reliability 不够.\"\n  action_items:\n    - round: 7\n      action: \"报告 per-category AC₁; 在主文标注 failure mode analysis 为 tentative; 或降级为 exploratory analysis\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W8\"\n  summary: \"ICC=0.919 仅限 OpenAI 模型, cross-provider temporal reproducibility 未知\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R1 raised, R2 AGREE. 已有 caveat 但仍被标记.\"\n  action_items:\n    - round: 7\n      action: \"明确 ICC 仅反映 within-provider temporal stability\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W9\"\n  summary: \"引用 metadata 错误 (ferrari first author, lassiter year, levy year)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R1+R2 均标记. ferrari_defects_2018 first author 为 Rosadini; lassiter_goodman_2017 可能是 2015 online-first; levy_expectation_2008 可能是 2007.\"\n  action_items:\n    - round: 7\n      action: \"核实并修正 bib 条目\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W10\"\n  summary: \"遗漏重要相关工作: WSD survey (Navigli 2009), Agent-SafetyBench, AgentSpec\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R2 raised 4 missing refs, R1 agrees Navigli WSD survey 应补充. Agent-SafetyBench/SafeAgentBench 非必需 (已有 5 个同类引用). AgentSpec 需确认相关性.\"\n  action_items:\n    - round: 7\n      action: \"补充 Navigli (2009) WSD survey; 评估 Agent-SafetyBench 和 AgentSpec 是否需要\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# MINOR ISSUES\n# ============================================================\n\n- id: \"R7-M1\"\n  summary: \"Abstract 信息密度过高 (OR, V, p-value, pp range 堆积)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1]\n      note: \"R1 minor issue. 可选择精简.\"\n\n- id: \"R7-M2\"\n  summary: \"'Upper bound...information-addition confound' 措辞逐字重复 ≥4 次\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1]\n      note: \"压缩可同时缓解页数问题.\"\n\n- id: \"R7-M3\"\n  summary: \"Figure 1 子面板文字偏小; Figure 2/3 颜色方案不一致\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2, visual_check]\n      note: \"视觉审查 + R2 均标记 Figure 1 文字偏小. 视觉审查标记 Figure 2/3 颜色语义不一致.\"\n\n- id: \"R7-M4\"\n  summary: \"Pages 3-5 连续纯文本无 display item\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [visual_check]\n      note: \"视觉审查标记: §3 Taxonomy + §4 Method 连续 3 页无图表. 建议添加 taxonomy 层级表/树状图.\"\n\n- id: \"R7-M5\"\n  summary: \"Appendix Page 13 六个表格挤在同一页, 字号过小\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [visual_check]\n      note: \"Tables 4-9 挤在一页, 建议拆分或合并.\"\n\n- id: \"R7-M6\"\n  summary: \"最后一页 (Page 14) 仅 ~10 行文字, ~90% 空白\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [visual_check]\n      note: \"视觉观感极差, 建议填充或调整分页.\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Round 7 (Fresh) Review Issues — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Date: 2026-05-21\n## Round 7 Score: 3.5 (Borderline Conference)\n## Note: Fresh review session — all issues re-evaluated from scratch\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"主文超出 EMNLP 2026 8 页正文限制约 0.5-0.7 页\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R2 raised, R1 AGREE. Discussion 跨页到 Page 9, Table 2 + Conclusion 均在 Page 9. ARR desk reject 风险. 视觉审查同样标记为 critical.\"\n  action_items:\n    - round: 7\n      action: \"Table 2 移至 Appendix (省约 1/3 页); Discussion 压缩重复措辞 ('upper bound...confound' 逐字重复 ≥4 次); Introduction contribution list 精简\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N2\"\n  summary: \"Authorization scope 测量可靠性过低 (cross-judge κ=0.385) 无法充分支撑 canary type 主张\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R1 raised, R2 AGREE with nuance (matched-pair Δpp 受 within-judge 一致性保护, 但绝对率不确定性大). Per-type validation n=34 不足; human-LLM κ=0.644 CI=[0.35,0.91] 极宽. Abstract/Conclusion 突出 canary type 但无 measurement-uncertainty caveat.\"\n  action_items:\n    - round: 7\n      action: \"在 Abstract/Conclusion 对 canary type 加 measurement-uncertainty caveat; 增加 auth scope human validation 样本或报告 within-judge raw agreement + detection vs severity 分离分析\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N3\"\n  summary: \"Incompleteness information-addition confound 在 Abstract/Conclusion 中 hedging 不足\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R2 raised as critical (confound 未充分处理), R1 AGREE with nuance (分析控制已在但呈现方式需改善). 共识: Abstract 'universally dangerous' 和 Conclusion 'universal blind spot' 措辞过强; Appendix F 仅报告 'coefficient change <8%' 缺 OR 变化量.\"\n  action_items:\n    - round: 7\n      action: \"报告 logistic regression 控制前后 OR 变化量; Abstract/Conclusion 加限定语 ('though partly reflecting information-addition confound'); 考虑将 incompleteness 在 type hierarchy 排序中单独讨论\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N4\"\n  summary: \"缺少 a priori power analysis, 50 pairs/type 的样本量合理性未论证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R1 raised, R2 AGREE with nuance (C1 power 显然充足 >0.99, 但 TOST equivalence 和 per-type per-model cells n≈50 power 不明确). Two-tier structure 依赖 TOST null 结果, 无 power analysis 无法区分 'types equivalent' vs 'lack power'.\"\n  action_items:\n    - round: 7\n      action: \"报告 post-hoc power analysis: C1 (确认 >0.99), TOST equivalence (报告 detectable minimum effect), per-type interaction (诚实报告不足). 若 TOST power 不足则缩小 C2 claim.\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R7-W1\"\n  summary: \"Judge-model confounding 对 C4 model-level 结论的限制\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R1 raised as critical, R2 REBUT to warning: matched-pair design 保护 within-model C1/C2 (judge bias 在 Δpp 中抵消), 仅 C4 cross-model 比较受影响. GPT-4.1 judging GPT-5.4 的能力不对称方向与结论相反 (低估而非高估违规). 共识: 对 C1/C2 非威胁, 对 C4 需在 Method 中 explicit 解释.\"\n  action_items:\n    - round: 7\n      action: \"在 Method 增加一段解释 matched-pair 为何保护 within-model comparisons; C4 结论中明确标注 judge-model confounding 限制\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"Differential Nocuity 被呈现为 framework 但缺乏形式化\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R2 raised as critical, R1 REBUT: conceptual organizing principle (类似 good-enough processing) 不需要 formal model. 共识: 非 critical, 但 Discussion 应更明确阐述框架组成部分 (type hierarchy + channel availability + systematic nocuity).\"\n  action_items:\n    - round: 7\n      action: \"Discussion §7 开头用 2-3 句话明确 Differential Nocuity 的组成部分; 或降级为 empirical observation 而非 framework\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W3\"\n  summary: \"TOST SESOI ±15pp 缺乏外部锚定, tier structure 对 margin 选择敏感\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R1 raised, R2 AGREE. ±10pp 时仅 3/6 mid-tier pairs equivalent, ±12pp 时 5/6. 'Robust two-tier structure' 主要在 ≥15pp 成立. Perturbation CI 锚定有循环论证嫌疑.\"\n  action_items:\n    - round: 7\n      action: \"主文讨论 SESOI 敏感性; 报告 minimum SESOI at which two-tier emerges (~±12pp); 寻找外部锚定\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W4\"\n  summary: \"Table 2 (mitigation experiment) 样本量不足 (~50/cell) 却在主文 Discussion 占重要位置\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R1 W4 + R2 交叉 AGREE. DeepSeek scopal +2.0pp / incompleteness +4.0pp 显示 mitigation 不稳定. 移至 Appendix 同时解决页数超限问题.\"\n  action_items:\n    - round: 7\n      action: \"Table 2 移至 Appendix; 主文保留 1-2 句方向性总结\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W5\"\n  summary: \"与 DRIP-R (concurrent work) 差异化论述不够有力\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R2 raised, R1 部分同意. §2 仅两句话说明差异, 需要更 explicit 的 contribution delta (type overlap, conclusion consistency, beyond matched-pair design).\"\n  action_items:\n    - round: 7\n      action: \"Related Work 增加详细对比段落或表格\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W6\"\n  summary: \"Human validation 缺少 annotator blindness, disagreement distribution 等细节\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R2 raised, R1 AGREE. 缺: annotator 具体背景, blind to condition?, disagreement 按 type 分布, 100 episodes 抽样策略.\"\n  action_items:\n    - round: 7\n      action: \"补充 1-2 句 annotator selection, blindness, stratification\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W7\"\n  summary: \"Failure mode taxonomy inter-coder reliability 偏低 (Cohen's κ=0.52)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R1 raised, R2 AGREE. Moderate agreement; arbitrary rule selection κ=0.29. 作为 Contribution 之一 reliability 不够.\"\n  action_items:\n    - round: 7\n      action: \"报告 per-category AC₁; 在主文标注 failure mode analysis 为 tentative; 或降级为 exploratory analysis\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W8\"\n  summary: \"ICC=0.919 仅限 OpenAI 模型, cross-provider temporal reproducibility 未知\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R1 raised, R2 AGREE. 已有 caveat 但仍被标记.\"\n  action_items:\n    - round: 7\n      action: \"明确 ICC 仅反映 within-provider temporal stability\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W9\"\n  summary: \"引用 metadata 错误 (ferrari first author, lassiter year, levy year)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R1+R2 均标记. ferrari_defects_2018 first author 为 Rosadini; lassiter_goodman_2017 可能是 2015 online-first; levy_expectation_2008 可能是 2007.\"\n  action_items:\n    - round: 7\n      action: \"核实并修正 bib 条目\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W10\"\n  summary: \"遗漏重要相关工作: WSD survey (Navigli 2009), Agent-SafetyBench, AgentSpec\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2]\n      note: \"R2 raised 4 missing refs, R1 agrees Navigli WSD survey 应补充. Agent-SafetyBench/SafeAgentBench 非必需 (已有 5 个同类引用). AgentSpec 需确认相关性.\"\n  action_items:\n    - round: 7\n      action: \"补充 Navigli (2009) WSD survey; 评估 Agent-SafetyBench 和 AgentSpec 是否需要\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# MINOR ISSUES\n# ============================================================\n\n- id: \"R7-M1\"\n  summary: \"Abstract 信息密度过高 (OR, V, p-value, pp range 堆积)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1]\n      note: \"R1 minor issue. 可选择精简.\"\n\n- id: \"R7-M2\"\n  summary: \"'Upper bound...information-addition confound' 措辞逐字重复 ≥4 次\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1]\n      note: \"压缩可同时缓解页数问题.\"\n\n- id: \"R7-M3\"\n  summary: \"Figure 1 子面板文字偏小; Figure 2/3 颜色方案不一致\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [R1, R2, visual_check]\n      note: \"视觉审查 + R2 均标记 Figure 1 文字偏小. 视觉审查标记 Figure 2/3 颜色语义不一致.\"\n\n- id: \"R7-M4\"\n  summary: \"Pages 3-5 连续纯文本无 display item\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [visual_check]\n      note: \"视觉审查标记: §3 Taxonomy + §4 Method 连续 3 页无图表. 建议添加 taxonomy 层级表/树状图.\"\n\n- id: \"R7-M5\"\n  summary: \"Appendix Page 13 六个表格挤在同一页, 字号过小\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [visual_check]\n      note: \"Tables 4-9 挤在一页, 建议拆分或合并.\"\n\n- id: \"R7-M6\"\n  summary: \"最后一页 (Page 14) 仅 ~10 行文字, ~90% 空白\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [visual_check]\n      note: \"视觉观感极差, 建议填充或调整分页.\"\n"
  }
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-21T15:47:17.712709+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 11110}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 618 · 2026-05-21T15:49:24.799659+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "report": "# 审稿报告 — Round 7 (Fresh)\n\n**论文**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**审稿人**: Reviewer 1 (方法严谨性) + Reviewer 2 (新颖性/完整性)\n**审稿模式**: 重新审稿 (fresh)\n\n---\n\n## Summary\n\n本文通过 matched-pair 因果设计研究 LLM agent 在策略歧义下的安全违规。在 τ²-bench 上构建 300 组 clause pairs（6 种歧义类型，two-layer taxonomy），跨 5 个模型评估 2,997 episodes，另有 2 个模型族的 replication。核心发现：(1) 歧义条款使违规率增加 34.0pp（OR=15.1）；(2) 类型间存在显著层级（V=0.137），incompleteness 最高（46-62%），authorization scope 模型间差异最大（12-64%）；(3) agent 几乎不具备歧义识别能力（<11%）。论文提出 Differential Nocuity 框架。\n\n---\n\n## Strengths\n\n1. **Matched-pair causal design 是本文最大的方法论贡献**（R1+R2 共识）。相比 DRIP-R 等 correlational work，每对 clause pair 仅做 minimal edit + perturbation control（n=300, Δ=-0.67pp）显著增强因果推断可信度。这是首个将歧义类型与 agent 安全违规建立因果关系的研究。\n\n2. **统计分析全面且恰当**（R1+R2 共识）。McNemar's test（paired binary）、Fisher's exact（per-type）、TOST equivalence（区分 \"no difference\" vs \"equivalent\"）、Holm-Bonferroni 校正、效应量报告（OR, V, Δpp）均选择得当。Sensitivity analysis（7 个 SESOI margins, 2 个 severity thresholds）增加稳健性。\n\n3. **Cross-architecture replication 广泛**（R1+R2 共识）。5+2 个模型跨 6 个 provider，C1 在所有 7 个模型上 p < 10⁻⁶，C2 ranking ρ=0.90 (LLaMA)，大幅增强外部效度。\n\n4. **Taxonomy 有双重理论基础**（R2）。植根于 CL 文献（Li et al., 2024）和 RE 文献（Massey et al., 2014; Berry & Kamsties, 2004），操作性定义清晰。CL-first framing 适合 EMNLP。\n\n5. **Intellectual honesty**（R1）。主动标注 C3 inconclusive、C4 exploratory、incompleteness confound、per-type judge reliability 差异，在 NLP 论文中不常见。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[N1] 主文超出 EMNLP 2026 的 8 页正文限制**（R1 AGREE + R2 raised，视觉审查 confirmed）\n- 正文（Abstract → Conclusion）约 8.5-8.7 页，超限约 0.5-0.7 页\n- Table 2（mitigation experiment, ~50/cell, preliminary）和 Conclusion 均在 Page 9\n- ARR desk reject 风险\n- 修复路径：Table 2 移至 Appendix（省 ~1/3 页）+ Discussion 压缩重复措辞（\"upper bound...confound\" 逐字重复 ≥4 次）+ Introduction contribution list 精简\n\n**[N2] Authorization scope 测量可靠性过低，无法充分支撑 \"canary type\" 主张**（R1 raised, R2 AGREE with nuance）\n- Cross-judge κ=0.385（fair），所有类型中最低\n- Human-LLM κ=0.644，95% CI [0.35, 0.91] 极宽\n- Per-type validation n=34 不足\n- R2 补充 nuance：matched-pair 的 within-model Δpp 受 judge 内部一致性保护，cross-judge disagreement 主要影响绝对率而非 treatment effect。但 Abstract/Conclusion 突出 canary type 时缺乏 measurement-uncertainty caveat\n- 修复路径：Abstract/Conclusion 加 measurement-uncertainty 限定语；报告 within-judge raw agreement + detection vs severity 分离分析\n\n**[N3] Incompleteness information-addition confound 在 Abstract/Conclusion 中 hedging 不足**（R2 raised as critical, R1 AGREE with nuance）\n- Incompleteness 的 unambiguous variant 必须添加新政策内容，与其他 5 类结构性不同\n- Abstract \"universally dangerous\" 和 Conclusion \"universal blind spot\" 措辞过强\n- Appendix F 仅报告 \"coefficient change <8%\"，缺 OR 变化量\n- R1 nuance：论文已有多项控制（§3 预标注、§5.2 \"upper bound\"、coreferential lower bound、logistic regression），核心问题是呈现方式而非分析缺失\n- 修复路径：报告控制前后 OR 变化量；Abstract/Conclusion 加限定语\n\n**[N4] 缺少 a priori power analysis，50 pairs/type 的样本量合理性未论证**（R1 raised, R2 AGREE with nuance）\n- TOST equivalence 的 null 结果可信度取决于功效——当前无法区分 \"types are equivalent\" vs \"lack power to detect difference\"\n- Per-type per-model cells (n≈50) 估计不稳定\n- R2 nuance：C1 power 显然 >0.99 不是问题；关键在 TOST 和 per-type interaction\n- 修复路径：报告 post-hoc power analysis（C1 确认 >0.99，TOST 和 per-type 诚实报告）\n\n### Should-Fix（影响评分但不一票否决）\n\n**[W1] Judge-model confounding 对 C4 的限制**（R1 raised as critical, R2 REBUT to warning）\n- R2 提出有力反驳：matched-pair 设计保护 within-model 的 C1/C2（judge bias 在 Δpp 中抵消）；GPT-4.1 judging GPT-5.4 的 bias 方向与结论相反（低估而非高估）\n- 共识：对 C1/C2 非威胁，仅影响 C4 cross-model 比较\n- 修复路径：Method 中增加 explicit 解释 matched-pair 为何保护 within-model comparisons\n\n**[W2] \"Differential Nocuity\" 被呈现为 framework 但缺乏形式化**（R2 raised as critical, R1 REBUT to warning）\n- R1 反驳：conceptual organizing principle（类似 \"good-enough processing\"）不需要 formal model；框架连接了 type hierarchy + channel availability + systematic nocuity\n- 共识：非 critical，但 Discussion 应更明确阐述框架组成部分\n- 修复路径：Discussion 开头用 2-3 句话明确组成部分，或降级措辞\n\n**[W3] TOST SESOI ±15pp 缺乏外部锚定**（R1 raised, R2 AGREE）\n- ±10pp 时仅 3/6 mid-tier pairs equivalent，±12pp 时 5/6——\"robust two-tier structure\" 主要在 ≥15pp 成立\n- 修复路径：主文讨论 SESOI 敏感性，报告 minimum margin for two-tier emergence (~±12pp)\n\n**[W4] Table 2 (mitigation experiment) 样本量不足**（R1+R2 共识）\n- Per-cell ~50 episodes，DeepSeek 两个类型显示增加而非减少\n- 修复路径：移至 Appendix，主文保留 1-2 句方向性总结（同时缓解 N1 页数问题）\n\n**[W5] 与 DRIP-R 差异化论述不够有力**（R2 raised, R1 部分同意）\n- §2 仅两句话说明差异，需要更 explicit 的 contribution delta\n- 修复路径：Related Work 增加详细对比\n\n**[W6] Human validation 细节不足**（R1+R2 共识）\n- 缺少 annotator blindness、disagreement distribution、stratification strategy\n- 修复路径：补充 1-2 句\n\n**[W7] Failure mode taxonomy inter-coder κ=0.52**（R1 raised, R2 AGREE）\n- Moderate agreement 对独立 contribution 偏低；arbitrary rule selection κ=0.29\n- 修复路径：降级为 exploratory analysis，或报告 per-category AC₁\n\n**[W8] ICC=0.919 仅限 OpenAI 模型**（R1+R2 共识）\n- Cross-provider temporal reproducibility 未直接测量\n\n**[W9] 引用 metadata 错误**（R1+R2 共识）\n- ferrari_defects_2018 第一作者为 Rosadini；lassiter_goodman_2017 年份可能为 2015\n\n**[W10] 遗漏相关工作**（R2 raised, R1 部分同意）\n- WSD survey (Navigli 2009) 对 CL venue 是明显空白\n- Agent-SafetyBench, AgentSpec 可选\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成一致 [AGREE]：\n- 主文超出 8 页限制（必须修复）\n- Incompleteness confound 的 hedging 在 Abstract/Conclusion 不足\n- Authorization scope 需要 measurement-uncertainty caveat\n- 需要补充 power analysis\n- Table 2 应移至 Appendix\n- Matched-pair causal design 是主要方法论贡献\n- Human validation 细节需补充\n- 引用 metadata 需修正\n\n## Reviewer Divergence\n\n**Judge-model confounding 的严重性**\n- R1 认为 critical：每个 model 由单一 judge 评估，C4 model-level 结论受限\n- R2 REBUT to warning：matched-pair 设计保护 C1/C2，confounding 仅影响已标注 exploratory 的 C4\n- Director 判断：R2 的技术论证成立——within-model paired comparison 确实不受 judge systematic bias 影响。降级为 warning，但需在 Method 中 explicit 解释。\n\n**Differential Nocuity 形式化**\n- R2 认为 critical：缺乏 predictive/prescriptive model，overclaiming\n- R1 REBUT：conceptual framework 在 NLP 中常见，不需要 formal model\n- Director 判断：R1 的论点更有说服力——要求实证论文提供 formal model 标准偏高。但 Discussion 中应更清晰阐述框架组成部分。降级为 warning。\n\n**Excitement**\n- R1：4.0/5——首个 causal study + genuinely surprising findings（Ambiguity Blindness, systematic permissiveness bias）\n- R2：3.0/5——核心 insight \"不同类型有不同风险\" 较为 expected\n- Director 判断：R1 更准确。论文贡献不仅是发现差异，而是用严格因果设计量化差异并揭示 unexpected patterns（incompleteness 普遍性、0% conservative refusal、Qwen3/DeepSeek 0% disambiguation awareness）。综合 Excitement 3.5/5。\n\n---\n\n## Questions for Authors\n\n1. 50 clause pairs/type 的决定依据？基于 pilot study 还是资源约束？\n2. Cross-judge calibration 100 episodes 中 per-model judge agreement 分布？\n3. Logistic regression 控制 incompleteness confound 时具体控制了哪些变量？控制前后 OR 变化量？\n4. Template-based clause generation pipeline 的具体操作？同一 template 产生的多个 pairs 是否有 structural correlation？\n5. C3 (layer effect) inconclusive 但保留在主文的理由？（R2 反驳删除建议：报告 null results 是好的科学实践，但主文空间宝贵）\n6. \"Differential Nocuity\" 是否有超越 empirical observation 命名的理论预测力？\n\n---\n\n## Missing References\n\n- **Navigli (2009)** — WSD survey，与 lexical ambiguity type 直接相关，CL venue 空白（R1+R2 共识应补充）\n- **Agent-SafetyBench (Zhang et al., 2024)** — 2000 test cases, 8 safety risk categories（R2 建议，R1 认为可选）\n- **SafeAgentBench (Yin et al., 2024)** — embodied agent safety（R2 建议，R1 认为可选）\n- **AgentSpec (Poskitt et al., ICSE 2026)** — runtime enforcement for safe agents（R2 建议）\n\n引用真实性检查：38 条引用中 27 条 verified，7 条 not_found（tech report/新 arXiv，确认存在），4 条 minor metadata mismatch，0 条 fabricated。\n\n---\n\n## External Review\n\n外部审稿：未配置（项目配置中无 external_review section）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（2026-05-21 15:31 → 15:35，耗时约 3.5 分钟）\n\n发现（2 critical + 3 warning + 3 info）：\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| critical | Page 9 | 主正文延伸至第 9 页约 3/4 处，超出 8 页限制约 0.75 页 |\n| critical | Page 14 | 最后一页仅 ~10 行文字，~90% 空白 |\n| warning | Pages 3-5 | 连续 3 页纯文本无 display item（§3+§4），建议添加 taxonomy 图 |\n| warning | Page 13 | 6 个表格（Tables 4-9）挤在同一页，字号过小 |\n| warning | Page 8 | 纯文本页（§6+§7 开头），但属定性分析可接受 |\n| info | Page 2 | Figure 1 子面板文字偏小（约正文 60-65%） |\n| info | Pages 6-7 | Figure 2/3 颜色方案不一致（分组柱状 vs 热力图） |\n| info | Page 9 | Table 2 正负值无颜色/箭头辅助区分 |\n\n---\n\n## Overall Assessment\n\n**评分：3.5 / 5（Borderline Conference）**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | **3.5** |\n| Excitement | 4.0 | 3.0 | **3.5** |\n| Reproducibility | 3.0 | 3.5 | **3.25** |\n| Confidence | 4.0 | 4.0 | **4.0** |\n| **Overall** | **3.5** | **3.5** | **3.5** |\n\n**EMNLP 2026 评分标准对照**：3.5 = Borderline Conference（介于 Findings 可接收与主会议可接收之间）。\n\n**核心判断**：论文在研究问题（首个 causal, type-granularity ambiguity→safety mapping）和实验设计（matched-pair + perturbation control + 7-model replication）方面达到 Conference 水准。但四个 critical issues 共同削弱核心叙事的可信度：(1) 格式违规（desk reject 风险）；(2) 最突出的 type-specific 发现（auth scope canary type）建立在最低可靠性测量上；(3) 最高违规率的类型（incompleteness）受 information-addition confound 影响且 hedging 不足；(4) two-tier structure 的 equivalence claims 缺少 power analysis 支撑。\n\n**升分路径（3.5 → 4.0）**：\n1. 修复页数超限（N1）——必须，否则 desk reject\n2. Auth scope canary type 加 measurement-uncertainty caveat（N2）\n3. Incompleteness 在主文加限定语 + 报告 OR 变化量（N3）\n4. 补充 post-hoc power analysis（N4）\n5. Table 2 移至 Appendix（同时解决 N1 和 W4）\n\n这些修改均可在 revision 中完成，不需要新实验。\n\n**降分风险（3.5 → 3.0）**：\n- 页数超限被标记为 desk reject\n- Incompleteness confound 被认为根本性破坏 type hierarchy 解读\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution list 4 项偏多，C1（因果定量）和 C3（failure mode taxonomy）方法论层次不同但可精简表述\n- \"Differential Nocuity framework\" 措辞暗示 formal framework，建议在首次出现时明确定位为 conceptual framework / empirical observation\n\n### §3 Taxonomy\n- 双层结构理论支撑充分，但 authorization scope 的 linguistic vs specification 归类边界案例未讨论\n- 建议补充 taxonomy 可视化（树状图或层级表），缓解 Pages 3-5 连续纯文本问题\n\n### §4 Method\n- Matched-pair design 是核心优势，但缺少 power analysis（N4）\n- Cross-judge 设计需要 explicit 解释为何 within-model Δpp 不受 judge bias 影响（W1）\n- Human validation 需补充 annotator blindness 和 stratification 细节（W6）\n\n### §5 Results\n- C1、C2 证据强度充分\n- C3 inconclusive——两位 Reviewer 对是否保留存在分歧，但报告 null result 有价值\n- C4 exploratory 标签恰当，但 auth scope 相关结论需 measurement-uncertainty caveat\n\n### §6 Analysis\n- \"Ambiguity Blindness\" 是有价值的新观察（Qwen3/DeepSeek 0% awareness 尤其 striking）\n- Failure mode taxonomy inter-coder κ=0.52 偏低，建议降级为 exploratory\n\n### §7 Discussion\n- \"Why incompleteness resists safety training\" 推测合理但缺乏直接机制证据\n- Table 2 应移至 Appendix\n- Differential Nocuity 框架组成部分需更明确阐述\n\n### §8 Conclusion\n- 需压缩至 Page 8 以内\n- Incompleteness \"universal blind spot\" 需限定语\n\n### Limitations\n- 覆盖面良好（model coverage, domain scope, synthetic ambiguity, cross-judge asymmetry, failure mode analysis）\n- 建议增加：incompleteness information-addition confound、prompt sensitivity、per-type 样本量限制\n\n### References\n- 修正 ferrari_defects_2018、lassiter_goodman_2017 metadata\n- 补充 Navigli (2009) WSD survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "report": "# 审稿报告 — Round 7 (Fresh)\n\n**论文**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**审稿人**: Reviewer 1 (方法严谨性) + Reviewer 2 (新颖性/完整性)\n**审稿模式**: 重新审稿 (fresh)\n\n---\n\n## Summary\n\n本文通过 matched-pair 因果设计研究 LLM agent 在策略歧义下的安全违规。在 τ²-bench 上构建 300 组 clause pairs（6 种歧义类型，two-layer taxonomy），跨 5 个模型评估 2,997 episodes，另有 2 个模型族的 replication。核心发现：(1) 歧义条款使违规率增加 34.0pp（OR=15.1）；(2) 类型间存在显著层级（V=0.137），incompleteness 最高（46-62%），authorization scope 模型间差异最大（12-64%）；(3) agent 几乎不具备歧义识别能力（<11%）。论文提出 Differential Nocuity 框架。\n\n---\n\n## Strengths\n\n1. **Matched-pair causal design 是本文最大的方法论贡献**（R1+R2 共识）。相比 DRIP-R 等 correlational work，每对 clause pair 仅做 minimal edit + perturbation control（n=300, Δ=-0.67pp）显著增强因果推断可信度。这是首个将歧义类型与 agent 安全违规建立因果关系的研究。\n\n2. **统计分析全面且恰当**（R1+R2 共识）。McNemar's test（paired binary）、Fisher's exact（per-type）、TOST equivalence（区分 \"no difference\" vs \"equivalent\"）、Holm-Bonferroni 校正、效应量报告（OR, V, Δpp）均选择得当。Sensitivity analysis（7 个 SESOI margins, 2 个 severity thresholds）增加稳健性。\n\n3. **Cross-architecture replication 广泛**（R1+R2 共识）。5+2 个模型跨 6 个 provider，C1 在所有 7 个模型上 p < 10⁻⁶，C2 ranking ρ=0.90 (LLaMA)，大幅增强外部效度。\n\n4. **Taxonomy 有双重理论基础**（R2）。植根于 CL 文献（Li et al., 2024）和 RE 文献（Massey et al., 2014; Berry & Kamsties, 2004），操作性定义清晰。CL-first framing 适合 EMNLP。\n\n5. **Intellectual honesty**（R1）。主动标注 C3 inconclusive、C4 exploratory、incompleteness confound、per-type judge reliability 差异，在 NLP 论文中不常见。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[N1] 主文超出 EMNLP 2026 的 8 页正文限制**（R1 AGREE + R2 raised，视觉审查 confirmed）\n- 正文（Abstract → Conclusion）约 8.5-8.7 页，超限约 0.5-0.7 页\n- Table 2（mitigation experiment, ~50/cell, preliminary）和 Conclusion 均在 Page 9\n- ARR desk reject 风险\n- 修复路径：Table 2 移至 Appendix（省 ~1/3 页）+ Discussion 压缩重复措辞（\"upper bound...confound\" 逐字重复 ≥4 次）+ Introduction contribution list 精简\n\n**[N2] Authorization scope 测量可靠性过低，无法充分支撑 \"canary type\" 主张**（R1 raised, R2 AGREE with nuance）\n- Cross-judge κ=0.385（fair），所有类型中最低\n- Human-LLM κ=0.644，95% CI [0.35, 0.91] 极宽\n- Per-type validation n=34 不足\n- R2 补充 nuance：matched-pair 的 within-model Δpp 受 judge 内部一致性保护，cross-judge disagreement 主要影响绝对率而非 treatment effect。但 Abstract/Conclusion 突出 canary type 时缺乏 measurement-uncertainty caveat\n- 修复路径：Abstract/Conclusion 加 measurement-uncertainty 限定语；报告 within-judge raw agreement + detection vs severity 分离分析\n\n**[N3] Incompleteness information-addition confound 在 Abstract/Conclusion 中 hedging 不足**（R2 raised as critical, R1 AGREE with nuance）\n- Incompleteness 的 unambiguous variant 必须添加新政策内容，与其他 5 类结构性不同\n- Abstract \"universally dangerous\" 和 Conclusion \"universal blind spot\" 措辞过强\n- Appendix F 仅报告 \"coefficient change <8%\"，缺 OR 变化量\n- R1 nuance：论文已有多项控制（§3 预标注、§5.2 \"upper bound\"、coreferential lower bound、logistic regression），核心问题是呈现方式而非分析缺失\n- 修复路径：报告控制前后 OR 变化量；Abstract/Conclusion 加限定语\n\n**[N4] 缺少 a priori power analysis，50 pairs/type 的样本量合理性未论证**（R1 raised, R2 AGREE with nuance）\n- TOST equivalence 的 null 结果可信度取决于功效——当前无法区分 \"types are equivalent\" vs \"lack power to detect difference\"\n- Per-type per-model cells (n≈50) 估计不稳定\n- R2 nuance：C1 power 显然 >0.99 不是问题；关键在 TOST 和 per-type interaction\n- 修复路径：报告 post-hoc power analysis（C1 确认 >0.99，TOST 和 per-type 诚实报告）\n\n### Should-Fix（影响评分但不一票否决）\n\n**[W1] Judge-model confounding 对 C4 的限制**（R1 raised as critical, R2 REBUT to warning）\n- R2 提出有力反驳：matched-pair 设计保护 within-model 的 C1/C2（judge bias 在 Δpp 中抵消）；GPT-4.1 judging GPT-5.4 的 bias 方向与结论相反（低估而非高估）\n- 共识：对 C1/C2 非威胁，仅影响 C4 cross-model 比较\n- 修复路径：Method 中增加 explicit 解释 matched-pair 为何保护 within-model comparisons\n\n**[W2] \"Differential Nocuity\" 被呈现为 framework 但缺乏形式化**（R2 raised as critical, R1 REBUT to warning）\n- R1 反驳：conceptual organizing principle（类似 \"good-enough processing\"）不需要 formal model；框架连接了 type hierarchy + channel availability + systematic nocuity\n- 共识：非 critical，但 Discussion 应更明确阐述框架组成部分\n- 修复路径：Discussion 开头用 2-3 句话明确组成部分，或降级措辞\n\n**[W3] TOST SESOI ±15pp 缺乏外部锚定**（R1 raised, R2 AGREE）\n- ±10pp 时仅 3/6 mid-tier pairs equivalent，±12pp 时 5/6——\"robust two-tier structure\" 主要在 ≥15pp 成立\n- 修复路径：主文讨论 SESOI 敏感性，报告 minimum margin for two-tier emergence (~±12pp)\n\n**[W4] Table 2 (mitigation experiment) 样本量不足**（R1+R2 共识）\n- Per-cell ~50 episodes，DeepSeek 两个类型显示增加而非减少\n- 修复路径：移至 Appendix，主文保留 1-2 句方向性总结（同时缓解 N1 页数问题）\n\n**[W5] 与 DRIP-R 差异化论述不够有力**（R2 raised, R1 部分同意）\n- §2 仅两句话说明差异，需要更 explicit 的 contribution delta\n- 修复路径：Related Work 增加详细对比\n\n**[W6] Human validation 细节不足**（R1+R2 共识）\n- 缺少 annotator blindness、disagreement distribution、stratification strategy\n- 修复路径：补充 1-2 句\n\n**[W7] Failure mode taxonomy inter-coder κ=0.52**（R1 raised, R2 AGREE）\n- Moderate agreement 对独立 contribution 偏低；arbitrary rule selection κ=0.29\n- 修复路径：降级为 exploratory analysis，或报告 per-category AC₁\n\n**[W8] ICC=0.919 仅限 OpenAI 模型**（R1+R2 共识）\n- Cross-provider temporal reproducibility 未直接测量\n\n**[W9] 引用 metadata 错误**（R1+R2 共识）\n- ferrari_defects_2018 第一作者为 Rosadini；lassiter_goodman_2017 年份可能为 2015\n\n**[W10] 遗漏相关工作**（R2 raised, R1 部分同意）\n- WSD survey (Navigli 2009) 对 CL venue 是明显空白\n- Agent-SafetyBench, AgentSpec 可选\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成一致 [AGREE]：\n- 主文超出 8 页限制（必须修复）\n- Incompleteness confound 的 hedging 在 Abstract/Conclusion 不足\n- Authorization scope 需要 measurement-uncertainty caveat\n- 需要补充 power analysis\n- Table 2 应移至 Appendix\n- Matched-pair causal design 是主要方法论贡献\n- Human validation 细节需补充\n- 引用 metadata 需修正\n\n## Reviewer Divergence\n\n**Judge-model confounding 的严重性**\n- R1 认为 critical：每个 model 由单一 judge 评估，C4 model-level 结论受限\n- R2 REBUT to warning：matched-pair 设计保护 C1/C2，confounding 仅影响已标注 exploratory 的 C4\n- Director 判断：R2 的技术论证成立——within-model paired comparison 确实不受 judge systematic bias 影响。降级为 warning，但需在 Method 中 explicit 解释。\n\n**Differential Nocuity 形式化**\n- R2 认为 critical：缺乏 predictive/prescriptive model，overclaiming\n- R1 REBUT：conceptual framework 在 NLP 中常见，不需要 formal model\n- Director 判断：R1 的论点更有说服力——要求实证论文提供 formal model 标准偏高。但 Discussion 中应更清晰阐述框架组成部分。降级为 warning。\n\n**Excitement**\n- R1：4.0/5——首个 causal study + genuinely surprising findings（Ambiguity Blindness, systematic permissiveness bias）\n- R2：3.0/5——核心 insight \"不同类型有不同风险\" 较为 expected\n- Director 判断：R1 更准确。论文贡献不仅是发现差异，而是用严格因果设计量化差异并揭示 unexpected patterns（incompleteness 普遍性、0% conservative refusal、Qwen3/DeepSeek 0% disambiguation awareness）。综合 Excitement 3.5/5。\n\n---\n\n## Questions for Authors\n\n1. 50 clause pairs/type 的决定依据？基于 pilot study 还是资源约束？\n2. Cross-judge calibration 100 episodes 中 per-model judge agreement 分布？\n3. Logistic regression 控制 incompleteness confound 时具体控制了哪些变量？控制前后 OR 变化量？\n4. Template-based clause generation pipeline 的具体操作？同一 template 产生的多个 pairs 是否有 structural correlation？\n5. C3 (layer effect) inconclusive 但保留在主文的理由？（R2 反驳删除建议：报告 null results 是好的科学实践，但主文空间宝贵）\n6. \"Differential Nocuity\" 是否有超越 empirical observation 命名的理论预测力？\n\n---\n\n## Missing References\n\n- **Navigli (2009)** — WSD survey，与 lexical ambiguity type 直接相关，CL venue 空白（R1+R2 共识应补充）\n- **Agent-SafetyBench (Zhang et al., 2024)** — 2000 test cases, 8 safety risk categories（R2 建议，R1 认为可选）\n- **SafeAgentBench (Yin et al., 2024)** — embodied agent safety（R2 建议，R1 认为可选）\n- **AgentSpec (Poskitt et al., ICSE 2026)** — runtime enforcement for safe agents（R2 建议）\n\n引用真实性检查：38 条引用中 27 条 verified，7 条 not_found（tech report/新 arXiv，确认存在），4 条 minor metadata mismatch，0 条 fabricated。\n\n---\n\n## External Review\n\n外部审稿：未配置（项目配置中无 external_review section）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（2026-05-21 15:31 → 15:35，耗时约 3.5 分钟）\n\n发现（2 critical + 3 warning + 3 info）：\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| critical | Page 9 | 主正文延伸至第 9 页约 3/4 处，超出 8 页限制约 0.75 页 |\n| critical | Page 14 | 最后一页仅 ~10 行文字，~90% 空白 |\n| warning | Pages 3-5 | 连续 3 页纯文本无 display item（§3+§4），建议添加 taxonomy 图 |\n| warning | Page 13 | 6 个表格（Tables 4-9）挤在同一页，字号过小 |\n| warning | Page 8 | 纯文本页（§6+§7 开头），但属定性分析可接受 |\n| info | Page 2 | Figure 1 子面板文字偏小（约正文 60-65%） |\n| info | Pages 6-7 | Figure 2/3 颜色方案不一致（分组柱状 vs 热力图） |\n| info | Page 9 | Table 2 正负值无颜色/箭头辅助区分 |\n\n---\n\n## Overall Assessment\n\n**评分：3.5 / 5（Borderline Conference）**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | **3.5** |\n| Excitement | 4.0 | 3.0 | **3.5** |\n| Reproducibility | 3.0 | 3.5 | **3.25** |\n| Confidence | 4.0 | 4.0 | **4.0** |\n| **Overall** | **3.5** | **3.5** | **3.5** |\n\n**EMNLP 2026 评分标准对照**：3.5 = Borderline Conference（介于 Findings 可接收与主会议可接收之间）。\n\n**核心判断**：论文在研究问题（首个 causal, type-granularity ambiguity→safety mapping）和实验设计（matched-pair + perturbation control + 7-model replication）方面达到 Conference 水准。但四个 critical issues 共同削弱核心叙事的可信度：(1) 格式违规（desk reject 风险）；(2) 最突出的 type-specific 发现（auth scope canary type）建立在最低可靠性测量上；(3) 最高违规率的类型（incompleteness）受 information-addition confound 影响且 hedging 不足；(4) two-tier structure 的 equivalence claims 缺少 power analysis 支撑。\n\n**升分路径（3.5 → 4.0）**：\n1. 修复页数超限（N1）——必须，否则 desk reject\n2. Auth scope canary type 加 measurement-uncertainty caveat（N2）\n3. Incompleteness 在主文加限定语 + 报告 OR 变化量（N3）\n4. 补充 post-hoc power analysis（N4）\n5. Table 2 移至 Appendix（同时解决 N1 和 W4）\n\n这些修改均可在 revision 中完成，不需要新实验。\n\n**降分风险（3.5 → 3.0）**：\n- 页数超限被标记为 desk reject\n- Incompleteness confound 被认为根本性破坏 type hierarchy 解读\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution list 4 项偏多，C1（因果定量）和 C3（failure mode taxonomy）方法论层次不同但可精简表述\n- \"Differential Nocuity framework\" 措辞暗示 formal framework，建议在首次出现时明确定位为 conceptual framework / empirical observation\n\n### §3 Taxonomy\n- 双层结构理论支撑充分，但 authorization scope 的 linguistic vs specification 归类边界案例未讨论\n- 建议补充 taxonomy 可视化（树状图或层级表），缓解 Pages 3-5 连续纯文本问题\n\n### §4 Method\n- Matched-pair design 是核心优势，但缺少 power analysis（N4）\n- Cross-judge 设计需要 explicit 解释为何 within-model Δpp 不受 judge bias 影响（W1）\n- Human validation 需补充 annotator blindness 和 stratification 细节（W6）\n\n### §5 Results\n- C1、C2 证据强度充分\n- C3 inconclusive——两位 Reviewer 对是否保留存在分歧，但报告 null result 有价值\n- C4 exploratory 标签恰当，但 auth scope 相关结论需 measurement-uncertainty caveat\n\n### §6 Analysis\n- \"Ambiguity Blindness\" 是有价值的新观察（Qwen3/DeepSeek 0% awareness 尤其 striking）\n- Failure mode taxonomy inter-coder κ=0.52 偏低，建议降级为 exploratory\n\n### §7 Discussion\n- \"Why incompleteness resists safety training\" 推测合理但缺乏直接机制证据\n- Table 2 应移至 Appendix\n- Differential Nocuity 框架组成部分需更明确阐述\n\n### §8 Conclusion\n- 需压缩至 Page 8 以内\n- Incompleteness \"universal blind spot\" 需限定语\n\n### Limitations\n- 覆盖面良好（model coverage, domain scope, synthetic ambiguity, cross-judge asymmetry, failure mode analysis）\n- 建议增加：incompleteness information-addition confound、prompt sensitivity、per-type 样本量限制\n\n### References\n- 修正 ferrari_defects_2018、lassiter_goodman_2017 metadata\n- 补充 Navigli (2009) WSD survey"
  }
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-21T15:49:28.815980+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4016
}
```

</details>

---


### Assistant

_source line 620 · 2026-05-21T15:49:36.928443+00:00_

审稿报告已投递。

**Round 7 审稿完成**，总结：

**评分：3.5 / 5（Borderline Conference）**

4 个 Must-Fix：
1. **主文超 8 页**——Table 2 移至 Appendix + 压缩重复措辞即可修复
2. **Auth scope κ=0.385 支撑 canary type claim**——需加 measurement-uncertainty caveat
3. **Incompleteness confound hedging 不足**——Abstract/Conclusion 的 "universally dangerous" 需限定语
4. **缺 power analysis**——需报告 TOST 和 per-type interaction 的 post-hoc power

10 个 Should-Fix + 6 个 Minor。所有 critical issues 均可在 revision 中修复，不需要新实验。修复后可达 4.0（Conference）。

Issue Tracker 已同步更新至 `review_issues.yaml`（4 critical open + 10 warning open + 6 info open）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 59

## Round 59

2 recorded events


### User

_source line 621 · 2026-05-21T15:49:39.452072+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

总结：对 R1 的 3 个 Must-Fix 中，N1（auth scope reliability）和 N3（power analysis）**同意但加了 nuance**，N2（judge-model confounding）**部分反驳**——matched-pair 设计保护了核心 claim C1/C2，confound 仅影响 exploratory 的 C3。5 个 Should-Fix 全部**同意**。R1 的 6 个 Questions 中 Q6（C3 保留在主文）我**反驳**，报告 null results 是好的科学实践。两位 reviewer 的评分一致（3.5），但关注点互补——R1 侧重测量可靠性，我侧重新颖性和 confound 设计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 622 · 2026-05-21T15:49:49.779571+00:00_

审稿报告已投递给 Research Director。

**本轮审稿总结**：

- **Overall**: 3.5 / 5（Borderline Conference）
- **Reviewer**: R1（方法严谨性）3.5 + R2（新颖性/完整性）3.5
- **4 个 Must-Fix**: 页数超限、auth scope 测量可靠性不足、incompleteness confound hedging 不足、缺少 power analysis
- **10 个 Should-Fix**: judge-model confounding 对 C4 的限制、Differential Nocuity 形式化、TOST SESOI 锚定、Table 2 移至 Appendix、DRIP-R 差异化、human validation 细节、failure mode κ 偏低、ICC 局限、引用错误、遗漏 WSD 文献
- **升分路径明确**: 全部修复项可在 revision 中完成，不需新实验，修复后可达 4.0（Conference）

Issue Tracker 已同步更新至 `review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 60

## Round 60

52 recorded events


### User

_source line 623 · 2026-05-21T16:53:08.567016+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May cycle
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-21T16:53:14.500054+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-21T16:53:14.550995+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-21T16:53:23.383883+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
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

_source line 627 · 2026-05-21T16:53:23.384385+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-21T16:53:25.692926+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
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

_source line 629 · 2026-05-21T16:53:25.743528+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-21T16:53:31.715984+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-21T16:53:33.071706+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (16 个)\n\n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_009**: PREPARING — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_009: Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.（准备中）\n\n## 近期结论\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C1 causal inference ← 基于 plan_010\n  [plan_014_extended_perturbation_results](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/data/results.json) | [plan_014_perturbation_clauses_extended](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/data/clauses_perturbation_extended.json) | [plan_014_run_script](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/intermediate/run_plan014.py)\n- **plan_015** (success): Authorization scope violations are predominantly unauthorized escalation (granting excess permissions) rather than restriction, consistent across all 5 models, revealing systematic permissiveness bias under boundary ambiguity\n- **plan_013** (success): Binary ambiguity effect (C1: Δ >= 20pp) and type hierarchy (C2: at least partial rank consistency) re
…[truncated 247 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 632 · 2026-05-21T16:53:33.674751+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-21T16:53:34.628674+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-21T16:53:34.679235+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 635 · 2026-05-21T16:53:35.081060+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "memory.md"
  }
}
```

</details>

---


### Tool result

_source line 636 · 2026-05-21T16:53:41.956240+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"The 14th Joint Conference on Lexical and Computational Semantics | ACL Member Portal","url":"https://www.aclweb.org/portal/content/14th-joint-conference-lexical-and-computational-semantics"},{"title":"ACL Policy on Publication Ethics - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policy_on_Publication_Ethics"},{"title":"EACL 2026 - Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-call-system-demonstrations"}]

Based on the search results, here's information about ACL Rolling Review (ARR) 2026 submission guidelines and author instructions:

## Key Submission Guidelines

ACL Rolling Review (ARR) invites the submission of long and short papers on substantial, original, and unpublished research in all aspects of Computational Linguistics and Natural Language Processing.

## Template and Format Requirements

Paper submissions must use the official ACL style templates. The paper templates are available as an Overleaf template and can also be downloaded directly via https://aclrollingreview.org/cfp under 'Paper Submission Process, Criteria a
…[truncated 998 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 7277
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-21T16:53:42.006992+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/memory.md\", \"content\": \"# Memory — policy_ambiguity_safety\\n\\n## 竞品实验参考\\n（见 literature_map.yaml）\\n\\n## 经验教训\\n\\n### 5-Model Error Analysis 发现 (2026-05-21)\\n- **Layer mechanism 不是 clean dichotomy**：2-model 分析说 spec-layer = guess-and-act, linguistic-layer = misparse-and-apply。但 5-model 数据显示 conditional_precedence (spec-layer) 的 dominant FM 是 scope_misapplication（5/5 unanimous），与 linguistic-layer 一致。Failure mode 是 **type-specific** 而非 layer-specific。\\n- **Disambiguation awareness 有 model family 差异**：Claude 11.0%, GPT-4.1 10.7%（有一定 awareness），Qwen3 0%, DeepSeek 0%（完全 blind）。Overall 4.6%。\\n- **Claude conservative profile**：scope_misapplication dominant (50.5%), conservative_refusal highest (8.8%)，与低 violation rate (30.3%) 一致。\\n- **Inter-coder kappa 下降**：5-model κ=0.517 vs 2-model κ=0.594。新 3 模型的 traces 可能更难分类。\\n\\n### 已验证的模型 ID (OpenRouter proxy)\\n- `gpt-5.4` — 直接用，无 provider prefix\\n- `gpt-4.1` — 直接用\\n- `anthropic/claude-sonnet-4-6` — 需要 provider prefix\\n- `qwen/qwen3-235b-a22b` — 需要 provider prefix\\n- `deepseek/deepseek-chat-v3-0324` — 需要 provider prefix\\n- Base URL: `http://47.94.22.126/v1`\\n\\n### 运行脚本注意事项\\n- 必须用 `.venv/bin/python3` 而非系统 `python3`，因为 `core.crypto` 依赖 `cryptography` 包只在 venv 中\\n- 必须设置 `PYTHONUNBUFFERED=1` 否则 nohup 输出为空（Python stdout buffering）\\n- `core.crypto` 模块在 `/home/ubuntu/agent-ml-research/core/crypto.py`，脚本通过 `sys.path.insert(0, \\\"/home/ubuntu/agent-ml-research\\\")` 加载\\n\", \"total_chars\": 1360, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6925
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-21T16:53:49.334442+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 639 · 2026-05-21T16:53:50.288118+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limits long short paper format requirements aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limits long short paper format requirements aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-21T16:53:50.639731+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool call

_source line 641 · 2026-05-21T16:53:52.045292+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if paper PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 642 · 2026-05-21T16:53:55.513853+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline page limit format requirements"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here is the information about EMNLP 2026 submission requirements:

## Submission Deadline

The EMNLP 2026 paper submission deadline is May 25, 2026, 23:59:59 (UTC-12). All deadlines are 11:59 PM UTC-12:00 ("anywhere on Earth").

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Format Requirements

EMNLP uses the standard ACL style files, and the LaTeX te
…[truncated 462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 6179
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-21T16:53:55.965968+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limits long short paper format requirements aclrollingreview.org"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"}]

Based on the search results from the official ACL Rolling Review website, here are the key submission guidelines for 2026:

## Page Limits

**Long Papers:** Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references.

**Short Papers:** Short papers may consist of up to four (4) pages of content, plus unlimited pages of references.

## Format Requirements

All long, short a
…[truncated 875 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 5677
}
```

</details>

---


### Tool result

_source line 644 · 2026-05-21T16:53:55.966990+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/decisions.yaml\", \"content\": \"_next_id: 26\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 07:11 UTC\\n  summary: MVP 设计：3 类歧义 × 2 API 模型验证 type effect，不用 GPU\\n  rationale: 核心假设是\\\"歧义类型影响安全违规率\\\"。选 scopal/lexical/incompleteness 3 种假设差异最大的类型，用 frontier\\n    API 模型（免 GPU）快速验证信号存在性。60 条款 × 2 variants × 2 模型 = 240 runs，统计功效足够（χ² df=2, medium\\n    effect w=0.3, N=240 >> 所需 ~107）。Pass 条件：p<0.05 + V≥0.15。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 07:15 UTC\\n  summary: 采纳 Reviewer 3 条修正：增条款数、调阈值、补 fail path\\n  rationale: 'Reviewer WARNING: (1) pairwise N=80 对 V=0.15 功效仅 0.22，增至 30 条款/类（pairwise\\n    N=120）+ 提阈值至 V≥0.20 + 明确 MVP 只检测 medium+ effect；(2) 补 fail path 三级决策树（扩大N重测 →\\n    pivot binary story → full study）；(3) 加 judge 偏差检查点（scopal 低于预期时先排查 judge bias）。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 07:16 UTC\\n  summary: ROADMAP 补充 H1-H4 预测基准和 post-MVP 18 周路径骨架\\n  rationale: 'Reviewer WARNING: (1) ROADMAP 缺 post-MVP 骨架，ICLR DDL 18 周后，需提前规划 GPU\\n    申请时间点（W3 MVP pass 后立即申请，W5 开始 Phase 2b）；(2) H1-H4 方向性预测未落地到 ROADMAP，Agent 解读 MVP\\n    结果时需对照基准（H1: scopal 最高，H2: lexical 最低，null: binary effect story）。paper_framing.md\\n    保持在 MVP 后创建。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-20 07:23 UTC\\n  summary: MVP 分析改为双轨：ambiguous-only 跨类型比较（主）+ matched-pair within-type（辅）\\n  rationale: 'Reviewer WARNING: incompleteness matched pair 存在信息量不对称混淆——消歧必然添加信息，与\\n    scopal/lexical 的\\\"同信息不同措辞\\\"baseline 不可比。解法：(1) 主分析用 ambiguous-only 条件直接跨类型比较违规率（不受信息量混淆）；(2)\\n    matched-pair 降为辅助的 within-type 效应量度量；(3) 要求 Agent 修订 incompleteness pairs 只添加解决歧义的最小信息；(4)\\n    效度边界显式声明此不对称性。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-20 07:24 UTC\\n  summary: MVP 使用 τ²-
…[truncated 10954 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5327
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-21T16:53:56.118362+00:00_

-rw-r--r-- 1 ubuntu ubuntu 400509 May 21 16:52 /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 4073
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-21T16:54:11.224642+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-21T16:54:12.178997+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (16 个)\n\n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_009**: PREPARING — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_009: Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.（准备中）\n\n## 近期结论\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C1 causal inference ← 基于 plan_010\n  [plan_014_extended_perturbation_results](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/data/results.json) | [plan_014_perturbation_clauses_extended](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/data/clauses_perturbation_extended.json) | [plan_014_run_script](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/intermediate/run_plan014.py)\n- **plan_015** (success): Authorization scope violations are predominantly unauthorized escalation (granting excess permissions) rather than restriction, consistent across all 5 models, revealing systematic permissiveness bias under boundary ambiguity\n- **plan_013** (success): Binary ambiguity effect (C1: Δ >= 20pp) and type hierarchy (C2: at least partial rank consistency) re
…[truncated 247 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-21T16:54:12.681320+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -name \"*.yaml\" -path \"*/agent/*\" | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -name \"*.yaml\" -path \"*/agent/*\" | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-21T16:54:13.233838+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-21T16:54:13.536348+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/agent/config.yaml 2>/dev/null || echo \"NO_CONFIG\"",
  "description": "Read project agent config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/agent/config.yaml 2>/dev/null || echo \"NO_CONFIG\"",
    "description": "Read project agent config"
  }
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-21T16:54:13.586989+00:00_

NO_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-21T16:54:17.753728+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -name \"config*\" -o -name \"project*yaml\" -o -name \"project*json\" 2>/dev/null | head -10",
  "description": "Search for project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -name \"config*\" -o -name \"project*yaml\" -o -name \"project*json\" 2>/dev/null | head -10",
    "description": "Search for project config files"
  }
}
```

</details>

---


### Tool result

_source line 653 · 2026-05-21T16:54:18.707543+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pip/_internal/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pydantic/v1/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pydantic/v1/config.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pydantic/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pydantic/deprecated/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pydantic/deprecated/config.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/pydantic/config.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-21T16:54:18.808841+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -maxdepth 2 -name \"projects.yaml\" -o -name \"config.yaml\" 2>/dev/null | head -10",
  "description": "Search for global config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -maxdepth 2 -name \"projects.yaml\" -o -name \"config.yaml\" 2>/dev/null | head -10",
    "description": "Search for global config files"
  }
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-21T16:54:18.862493+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-21T16:54:26.995412+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -maxdepth 3 -name \"*.yaml\" -path \"*config*\" 2>/dev/null | head -10 && echo \"---\" && find /home/ubuntu/agent-ml-research -maxdepth 3 -name \"*.yaml\" -path \"*project*\" 2>/dev/null | head -10",
  "description": "Find config in agent-ml-research root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research -maxdepth 3 -name \"*.yaml\" -path \"*config*\" 2>/dev/null | head -10 && echo \"---\" && find /home/ubuntu/agent-ml-research -maxdepth 3 -name \"*.yaml\" -path \"*project*\" 2>/dev/null | head -10",
    "description": "Find config in agent-ml-research root"
  }
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-21T16:54:27.046075+00:00_

/home/ubuntu/agent-ml-research/workspace/config/approvals.yaml
/home/ubuntu/agent-ml-research/workspace/config/resources.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/aaai-2027.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/icml-2026.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/neurips-2026.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/acl-2026.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/iclr-2027.yaml
/home/ubuntu/agent-ml-research/config/ralph_loop.yaml
/home/ubuntu/agent-ml-research/config/images.yaml
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 658 · 2026-05-21T16:54:29.455526+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/config/venue_rules/emnlp-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-21T16:54:30.610337+00:00_

1	typesetting:
2	  layout: two_column
3	  max_pages: 8
4	  paper_size: a4
5	  column_width_cm: 7.7
6	  text_width_cm: 16.0
7	  column_sep_cm: 0.6
8	  template_sets:
9	    hyperref: true
10	  preamble_additions:
11	    packages: [microtype, booktabs, cleveref]
12	    float_params:
13	      topfraction: "0.85"
14	      bottomfraction: "0.85"
15	      textfraction: "0.15"
16	      floatpagefraction: "0.7"
17	    penalties:
18	      widowpenalty: "10000"
19	      clubpenalty: "10000"
20	  forbidden_packages: []
21	  required_sections:
22	    - name: Limitations
23	      severity: critical
24	    - name: Ethics Statement
25	      severity: warning
26	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 1154
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-21T16:54:30.761362+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/agent-ml-research/config/ /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/ --include=\"*.yaml\" --include=\"*.json\" -l 2>/dev/null | head -5",
  "description": "Find external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/agent-ml-research/config/ /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/ --include=\"*.yaml\" --include=\"*.json\" -l 2>/dev/null | head -5",
    "description": "Find external review config"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-21T16:54:30.863334+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 662 · 2026-05-21T16:54:35.882452+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/agent-ml-research/ --include=\"*.yaml\" --include=\"*.json\" --include=\"*.toml\" -l 2>/dev/null | head -10",
  "description": "Search for external review config anywhere"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/agent-ml-research/ --include=\"*.yaml\" --include=\"*.json\" --include=\"*.toml\" -l 2>/dev/null | head -10",
    "description": "Search for external review config anywhere"
  }
}
```

</details>

---


### Tool result

_source line 663 · 2026-05-21T16:54:37.087520+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 1205
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-21T16:54:37.288694+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NO_FILE\"",
  "description": "Check if review issues tracker exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NO_FILE\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-21T16:54:37.339355+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-21T16:54:39.748465+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml",
  "description": "Read existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml",
    "description": "Read existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-21T16:54:39.799384+00:00_

## Round 7 (Fresh) Review Issues — policy_ambiguity_safety
## Paper: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
## Venue: EMNLP 2026 via ARR May cycle
## Date: 2026-05-21
## Round 7 Score: 3.5 (Borderline Conference)
## Note: Fresh review session — all issues re-evaluated from scratch

# ============================================================
# CRITICAL ISSUES
# ============================================================

- id: "R7-N1"
  summary: "主文超出 EMNLP 2026 8 页正文限制约 0.5-0.7 页"
  category: format
  severity: critical
  status: resolved
  first_raised_round: 7
  last_seen_round: 7
  mentions:
    - round: 7
      reviewers: [R1, R2]
      note: "R2 raised, R1 AGREE. Discussion 跨页到 Page 9, Table 2 + Conclusion 均在 Page 9. ARR desk reject 风险."
  action_items:
    - round: 7
      action: "Table 2 移至 Appendix; Discussion 段落 2+3 合并压缩; Related Work 精简次要引用; Intro contribution list 压缩为 inline; Conclusion 从 5 行压到 3 行"
      assigned_to: author
      status: done
  resolution: "Table 2 moved to Appendix B; Discussion paragraphs merged (saved ~10 lines); Related Work psycholinguistics trimmed (saved ~4 lines); Intro compressed; Conclusion compressed. Compilation confirms Conclusion ends on page 8."
  resolution_round: 7

- id: "R7-N2"
  summary: "Authorization scope 测量可靠性过低 (cross-judge κ=0.385) 无法充分支撑 canary type 主张"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 7
  last_seen_round: 7
  mentions:
    - round: 7
      reviewers: [R1, R2]
      note: "R1 raised, R2 AGREE with nuance. Per-type validation n=34; human-LLM κ=0.644 CI=[0.35,0.91] 极宽."
  action_items:
    - round: 7
      action: "Abstract 加 measurement-uncertainty caveat; canary type 全文改为 'potential canary type'"
      assigned_to: author
      status: done
  resolution: "Abstract adds 'though authorization scope carries the widest measurement uncertainty among types'. All instances of 'canary type' changed to 'potential canary type' or
…[truncated 11576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-21T16:55:14.735231+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-21T16:55:37.325543+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 22590
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-21T16:55:37.476442+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-05-25\n- **类型**: Long paper\n- **页数限制**: 正文 ≤8 页，参考文献不限页\n- **模板**: ACL LaTeX (two-column, 11pt)\n- **匿名规则**: Double-blind（作者信息匿名）\n- **必须章节**: Limitations（不计入页数限制）\n- **附录**: 允许，但审稿人不强制阅读\n\n## 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n### 1. 统计方法与因果推理\n- 主要 claims（C1-C5）的统计检验是否合适？效应量/CI/p-value 报告是否完整？\n- TOST 等价性检验的 SESOI margin 选择是否有外部锚定和敏感性分析？\n- Matched-pair 设计能否真正控制混淆变量？incompleteness 的 information-addition confound 是否充分讨论？\n- Perturbation control 的样本量和 CI 宽度是否足以支撑因果推断？\n\n### 2. 测量可靠性\n- LLM-as-judge 的 inter-judge agreement（κ 值）是否足够支撑结论？\n- 人工标注验证的 sample size、annotator blindness、sampling strategy 是否充分报告？\n- Per-type reliability 是否有弱环（特别是 authorization scope）？\n- Error analysis 的 inter-coder reliability 是否支撑其作为贡献？\n\n### 3. 实验控制\n- Unambiguous baseline 的构建是否恰当？是否存在系统性偏差？\n- 跨模型比较是否有 judge-model confounding？如何处理？\n- Test-retest stability（ICC）是否覆盖所有模型家族？\n- 样本量 power analysis 是否充分？\n\n### 4. 可复现性\n- 数据集、代码、模型 API 的可复现性声明？\n- τ²-bench 修改是否充分记录？\n- 实验超参数是否完整报告？\n\n## Overall Assessment 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award, 4.5 = Borderline Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n请按以下格式输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 [MUST-FIX] 或 [SHOULD-FIX] 或 [MINOR])\n4. **Questions** (需要作者回答的)\n5. **Missing References**\n6. **Overall Assessment** (评分 + 置信度 high/medium/low + 1-2 句总评)\n7. **Detailed Comments** (逐节详细意见)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-05-25\n- **类型**: Long paper\n- **页数限制**: 正文 ≤8 页，参考文献不限页\n- **模板**: ACL LaTeX (two-column, 11pt)\n- **匿名规则**: Double-blind（作者信息匿名）\n- **必须章节**: Limitations（不计入页数限制）\n- **附录**: 允许，但审稿人不强制阅读\n\n## 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n### 1. 统计方法与因果推理\n- 主要 claims（C1-C5）的统计检验是否合适？效应量/CI/p-value 报告是否完整？\n- TOST 等价性检验的 SESOI margin 选择是否有外部锚定和敏感性分析？\n- Matched-pair 设计能否真正控制混淆变量？incompleteness 的 information-addition confound 是否充分讨论？\n- Perturbation control 的样本量和 CI 宽度是否足以支撑因果推断？\n\n### 2. 测量可靠性\n- LLM-as-judge 的 inter-judge agreement（κ 值）是否足够支撑结论？\n- 人工标注验证的 sample size、annotator blindness、sampling strategy 是否充分报告？\n- Per-type reliability 是否有弱环（特别是 authorization scope）？\n- Error analysis 的 inter-coder reliability 是否支撑其作为贡献？\n\n### 3. 实验控制\n- Unambiguous baseline 的构建是否恰当？是否存在系统性偏差？\n- 跨模型比较是否有 judge-model confounding？如何处理？\n- Test-retest stability（ICC）是否覆盖所有模型家族？\n- 样本量 power analysis 是否充分？\n\n### 4. 可复现性\n- 数据集、代码、模型 API 的可复现性声明？\n- τ²-bench 修改是否充分记录？\n- 实验超参数是否完整报告？\n\n## Overall Assessment 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award, 4.5 = Borderline Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n请按以下格式输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 [MUST-FIX] 或 [SHOULD-FIX] 或 [MINOR])\n4. **Questions** (需要作者回答的)\n5. **Missing References**\n6. **Overall Assessment** (评分 + 置信度 high/medium/low + 1-2 句总评)\n7. **Detailed Comments** (逐节详细意见)"
  }
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-21T16:56:00.193170+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22716
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-21T16:56:00.394359+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-05-25\n- **类型**: Long paper\n- **页数限制**: 正文 ≤8 页，参考文献不限页\n- **模板**: ACL LaTeX (two-column, 11pt)\n- **匿名规则**: Double-blind（作者信息匿名）\n- **必须章节**: Limitations（不计入页数限制）\n- **附录**: 允许，但审稿人不强制阅读\n\n## 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n### 1. 贡献新颖性与定位\n- 本文的核心贡献（taxonomy + empirical findings + differential nocuity framework）在当前 LLM safety + computational linguistics 文献中是否足够新颖？\n- 与最相关的 concurrent/prior work（如 DRIP-R, ToolEmu, AgentBench, R-Judge 等）的差异化是否清晰有力？\n- CL-first framing（从语言学歧义出发 → safety 应用）对 EMNLP 审稿人是否有说服力？\n- \"Uniformity null result\"（type effect 不显著）是否有独立价值？framing 是否恰当？\n\n### 2. Related Work 完整性\n- Ambiguity 方面：是否覆盖 WSD (Navigli 2009)、garden-path (Levy 2008)、good-enough processing (Ferreira & Patson 2007)？\n- LLM Safety 方面：是否覆盖主要 agent safety benchmarks 和 evaluation frameworks？\n- Policy/instruction following 方面：是否有遗漏的关键引用？\n- 引用数量和质量是否达标（EMNLP long paper 通常 ≥30 篇）？\n\n### 3. 论文结构与写作质量\n- Abstract 信息密度和可读性平衡是否恰当？\n- Introduction 的 motivation → gap → contribution 逻辑链是否清晰？\n- Taxonomy (§3) 的 two-layer 结构（linguistic + specification）是否有说服力？与传统 CL 分类的关系是否讨论？\n- Discussion 的 Differential Nocuity 概念是否过度声称？\n- Conclusion 是否简洁且准确反映结果？\n\n### 4. 格式合规性\n- 正文是否严格 ≤8 页？（Discussion 和 Conclusion 必须在 Page 8 结束之前）\n- Limitations 章节是否存在且不过长？\n- 是否遵守 double-blind（无作者姓名、无自引透露身份）？\n- 图表编号、引用格式、公式编号是否规范？\n- ACL template 使用是否正确（\\usepackage[review]{acl}）？\n\n### 5. Broader Impact / Ethics\n- 研究涉及 LLM agent 安全漏洞——是否有 responsible disclosure 考虑？\n- Policy clause 数据集是否有伦理风险（如含敏感内容）？\n- 是否需要 Ethics Statement？\n\n## Overall Assessment 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award, 4.5 = Borderline Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n请按以下格式输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 [MUST-FIX] 或 [SHOULD-FIX] 或 [MINOR])\n4. **Questions** (需要作者回答的)\n5. **Missing References**\n6. **Overall Assessment** (评分 + 置信度 high/medium/low + 1-2 句总评)\n7. **Detailed Comments** (逐节详细意见)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May cycle 提交）\n- **截止日期**: 2026-05-25\n- **类型**: Long paper\n- **页数限制**: 正文 ≤8 页，参考文献不限页\n- **模板**: ACL LaTeX (two-column, 11pt)\n- **匿名规则**: Double-blind（作者信息匿名）\n- **必须章节**: Limitations（不计入页数限制）\n- **附录**: 允许，但审稿人不强制阅读\n\n## 论文路径\n- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n### 1. 贡献新颖性与定位\n- 本文的核心贡献（taxonomy + empirical findings + differential nocuity framework）在当前 LLM safety + computational linguistics 文献中是否足够新颖？\n- 与最相关的 concurrent/prior work（如 DRIP-R, ToolEmu, AgentBench, R-Judge 等）的差异化是否清晰有力？\n- CL-first framing（从语言学歧义出发 → safety 应用）对 EMNLP 审稿人是否有说服力？\n- \"Uniformity null result\"（type effect 不显著）是否有独立价值？framing 是否恰当？\n\n### 2. Related Work 完整性\n- Ambiguity 方面：是否覆盖 WSD (Navigli 2009)、garden-path (Levy 2008)、good-enough processing (Ferreira & Patson 2007)？\n- LLM Safety 方面：是否覆盖主要 agent safety benchmarks 和 evaluation frameworks？\n- Policy/instruction following 方面：是否有遗漏的关键引用？\n- 引用数量和质量是否达标（EMNLP long paper 通常 ≥30 篇）？\n\n### 3. 论文结构与写作质量\n- Abstract 信息密度和可读性平衡是否恰当？\n- Introduction 的 motivation → gap → contribution 逻辑链是否清晰？\n- Taxonomy (§3) 的 two-layer 结构（linguistic + specification）是否有说服力？与传统 CL 分类的关系是否讨论？\n- Discussion 的 Differential Nocuity 概念是否过度声称？\n- Conclusion 是否简洁且准确反映结果？\n\n### 4. 格式合规性\n- 正文是否严格 ≤8 页？（Discussion 和 Conclusion 必须在 Page 8 结束之前）\n- Limitations 章节是否存在且不过长？\n- 是否遵守 double-blind（无作者姓名、无自引透露身份）？\n- 图表编号、引用格式、公式编号是否规范？\n- ACL template 使用是否正确（\\usepackage[review]{acl}）？\n\n### 5. Broader Impact / Ethics\n- 研究涉及 LLM agent 安全漏洞——是否有 responsible disclosure 考虑？\n- Policy clause 数据集是否有伦理风险（如含敏感内容）？\n- 是否需要 Ethics Statement？\n\n## Overall Assessment 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award, 4.5 = Borderline Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit\n\n请按以下格式输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 [MUST-FIX] 或 [SHOULD-FIX] 或 [MINOR])\n4. **Questions** (需要作者回答的)\n5. **Missing References**\n6. **Overall Assessment** (评分 + 置信度 high/medium/low + 1-2 句总评)\n7. **Detailed Comments** (逐节详细意见)"
  }
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-21T16:56:01.757021+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1362
}
```

</details>

---


### Assistant

_source line 674 · 2026-05-21T16:56:18.913946+00:00_

已派发完成：

| 任务 | 状态 |
|------|------|
| 视觉审查 Agent | ✅ 已启动（fire-and-forget） |
| Reviewer 1（方法严谨性 + 实验设计） | ✅ 已派发 |
| Reviewer 2（新颖性 + 完整性） | ✅ 已派发 |
| 外部审稿（Stanford Agentic Reviewer） | ⬜ 未配置（项目无 `external_review.paperreview_ai.enabled` 设置） |

等待两位 Reviewer 返回独立审稿意见，收齐后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 61

## Round 61

2 recorded events


### User

_source line 675 · 2026-05-21T17:02:46.970184+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 完整审稿意见（新颖性 + 完整性审查）

**Paper**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
**Venue**: EMNLP 2026 (ARR May cycle)

---

### 1. Summary

本文研究自然语言 policy specification 中不同类型歧义对 LLM agent 安全违规的因果影响。作者提出六类型、两层结构的歧义分类体系（linguistic: scopal/lexical/coreferential; specification: authorization scope/incompleteness/conditional precedence），在 τ²-bench 上构建 300 对 matched clause pairs，评估 5 个模型共 2,997 episodes。歧义整体增加 34.0 pp 违规率（OR=15.1），类型间存在显著层级差异（Cramér's V=0.137），incompleteness 持续最高（46–62%），并发现 "Ambiguity Blindness" 现象（<11% 的 agent 能识别歧义）。作者提出 Differential Nocuity 框架。

---

### 2. Strengths

**S1. CL-first framing 新颖且有说服力。** 从计算语言学歧义分类出发定位 agent safety 问题，而非从 safety benchmark 出发添加语言学标注。对 EMNLP 读者有独特吸引力，与 WSD/garden-path 文献形成有意义连接（§2, §6.1）。

**S2. Matched-pair 因果设计优于同期工作。** 相比 DRIP-R 的相关性设计，matched-pair + perturbation control（§4.2, §4.5）能更严格建立因果关系。Perturbation control（Δ_perturb = −0.67 pp, CI 含零）有效排除表层扰动解释。

**S3. 统计分析严谨且分层清晰。** C1–C4 按置信度递减排列，C3 inconclusive 诚实报告（§5.3），C4 明确标记 exploratory。TOST 等价性检验（Appendix A）系统验证了 two-tier 结构稳定性。

**S4. Ambiguity Blindness 有价值。** <11% awareness + 0% for Qwen3/DeepSeek（§6.2）具有直接工程意义。

**S5. 七模型六供应商覆盖面好。** 主实验 5 模型 + 复制 2 模型，C1 在全部 7 模型上显著。

**S6. Limitations 诚实全面。** 涵盖 model coverage、domain scope、synthetic ambiguity、cross-judge asymmetry、incompleteness confound 等主要限制。

---

### 3. Weaknesses

**W1 [MUST-FIX] Incompleteness confound 削弱 type hierarchy 核心 claim。**
- 位置：§3 line 18, §5.2, Appendix F
- Incompleteness 的 unambiguous variant 必须添加新 policy content，49.2 pp effect 混淆了"歧义消除"与"信息增加"。Logistic regression 控制 information delta（coefficient change <8%, p=0.022）不够充分：token count 只是信息量的粗略代理；regression 中 incompleteness 仍 significant 只说明残余效应存在，无法量化歧义效应 vs. 信息添加效应的比例。
- 直接影响 Table 1 中 incompleteness 作为 hierarchy 顶端的可信度，影响 Abstract/Conclusion 中 "type primarily determines severity" 的 claim。
- 建议：设计 information-matched control，或在 Abstract/Conclusion 显式降低对 incompleteness 排名的 claim 强度。

**W2 [MUST-FIX] Authorization scope 测量可靠性不足以支撑 "model-differentiating type" 论述。**
- 位置：§4.4, §5.4, Appendix G
- Authorization scope cross-judge κ=0.385（fair），human-LLM κ=0.644。论文将其作为 C4 核心发现（52 pp range），但测量工具不可靠时，模型间差异可能部分反映 judge 不稳定性。Within-judge analysis 只控制 judge identity，无法控制 per-instance inconsistency。
- 建议：明确标注该结论为 tentative，或增加 bootstrap CI 量化测量不确定性对模型排名的影响。

**W3 [SHOULD-FIX] Related Work 有 4 条 orphan bib 条目和若干遗漏。**
- Orphan（在 bib 未引用）：ferreira_patson_2007, levy_expectation_2008, lassiter_goodman_2017, poesio_artstein_2005——均为高度相关工作。
- 遗漏：(a) Constitutional AI/RLHF alignment 文献（C4 讨论 safety training 时需要）；(b) AgentBench；(c) 引用数 35 条偏少。

**W4 [SHOULD-FIX] Differential Nocuity 框架概念化不足。**
- 位置：§7, Abstract
- 被提升为核心贡献之一，但 Discussion 仅一段话展开。三因素（type, safety training, channel availability）交互关系未形式化；"channel availability"在论文中未直接测量（测量的是 awareness ≠ availability）；与 Berry & Kamsties (2004) 的理论推进关系不清晰。
- 建议：充分形式化或降级为观察性建议。

**W5 [SHOULD-FIX] Abstract 信息密度过高。**
- 包含 6 个统计量、嵌套括号、C1–C4 几乎所有结果的压缩。建议减少数字，保留 2-3 核心发现。

**W6 [SHOULD-FIX] C3 layer effect null result 讨论过于简短。**
- §5.3 仅 3 句话。如果 linguistic/specification 二分法不成立，two-layer taxonomy 的理论基础需要重新论证。可与 §6.1 failure mode 分析联动（conditional precedence 和 scopal 共享 structural misparse 模式）——这实际上是一个有价值的 null result。

**W7 [MINOR] ferrari_defects_2018 bib 条目第一作者不一致（实际为 Rosadini），年份标注 2018 但发表于 2019。**

**W8 [MINOR] 缺少 Ethics Statement。** 论文揭示 LLM agent 系统性安全漏洞（systematic nocuity 41.3%），但未讨论 responsible disclosure 或恶意利用风险。

---

### 4. Questions

**Q1.** Incompleteness 的 unambiguous variant 平均添加了多少 token？Information delta 的分布如何？Logistic regression 中 information delta 的 coefficient 和 CI？

**Q2.** Authorization scope 的 52 pp model range 中，Claude 12% 是否因 conservative refusal 倾向？Per-model failure mode 分布是什么？

**Q3.** 是否考虑过 information-addition perturbation（添加无关信息不消歧）作为 incompleteness confound 的更直接控制？

**Q4.** Template-based pipeline 的 template 设计是否公开？96% annotator pass rate 的 ~12 对 disagreement 是否集中在特定类型？

---

### 5. Missing References

- Levy (2008) "Expectation-based syntactic comprehension" — 在 bib 未引用
- Ferreira & Patson (2007) — 在 bib 未引用
- Constitutional AI / RLHF alignment 文献（Bai et al., 2022 等）
- AgentBench (Liu et al., 2023)
- Bender & Koller (2020) "Climbing towards NLU"

---

### 6. Overall Assessment

**Overall**: 3.5 (Borderline Conference)
**Soundness**: 3.5/5
**Excitement**: 3.5/5
**Reproducibility**: 4/5
**Confidence**: 4/5 (High)

**总评**: 研究问题有价值，CL-first framing 对 EMNLP 有独特贡献，实验设计严谨（matched-pair + perturbation control + 七模型复制）。主要问题：(1) incompleteness confound 削弱 type hierarchy 核心 claim（ranking 第一但因果解释最弱），(2) authorization scope 低测量可靠性削弱 model-differentiating 发现，(3) Differential Nocuity 框架概念化不足。若能加强 incompleteness confound 分析并适当降低 claim 强度，有达到 Conference 水平的潜力。

---

### 7. Detailed Comments（逐节）

**Abstract**: 统计量过多（6个数字），"information-addition confound"首次出现无上下文。建议保留 OR=15.1 + type hierarchy 定性描述。

**Introduction**: 开头 retail 场景好。Contribution (2) 中同时出现 confound 和 [exploratory] 标记可能给读者不确定感。

**Related Work**: Psycholinguistics 段论证链清晰。DRIP-R 差异化论述可更量化地比较 5 types vs. 6 types 重叠/互补。4 条 orphan bib 需处理。

**Taxonomy (§3)**: 结构清晰有例子。"frequency in operational policy documents"作为选择标准未报告具体频率数据。

**Method (§4)**: Cross-judge calibration 详尽是方法论强项。Model selection 未解释为何无 7B/13B 模型。

**Results (§5)**: C1 效应量大且显著（最强发现）。C2 TOST 是方法论亮点。C3 过于简短。C4 heatmap 有效但 auth scope 跳跃需更深入讨论。

**Error Analysis (§6)**: 三种 failure pattern 有意义。但 inter-coder reliability 仅 moderate 且完全基于 LLM coders 非 human coders。

**Discussion (§7)**: Differential Nocuity 三因素缺形式化。Mitigation experiment 的 across-model variance 未充分讨论。

**Conclusion**: 简洁但可能过于简短，未提 future work。

**Format**: 正文 8 页 ✓, Double-blind ✓, \usepackage[review]{acl} ✓, Limitations 存在且适当 ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 676 · 2026-05-21T17:02:57.089482+00:00_

Reviewer 2 审稿意见已收到（评分 3.5 Borderline Conference）。等待 Reviewer 1 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 62

## Round 62

6 recorded events


### User

_source line 677 · 2026-05-21T17:03:01.115938+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（方法严谨性 + 实验设计）

### 总体评分
**Overall**: 3.5 (Borderline Conference)
**置信度**: High (4/5)
**一句话总结**: 研究问题重要且实验设计整体严谨，但 TOST SESOI 缺乏外部锚定、authorization scope 的测量信度不足以支撑 C4 的关键声称、incompleteness confound 分析不够透明，这些方法论短板需要修补后才能稳定达到主会议水平。

### 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心 C1 claim 有充分支撑，但 C2 的 type hierarchy 依赖于争议性的 SESOI 选择；C4 exploratory claims 建立在信度最低的 type 之上 |
| Excitement | 3/5 | 研究问题及时且有实践价值，Differential Nocuity 框架有概念贡献，但整体是 Berry & Kamsties 框架在 LLM agent 上的经验延伸，novelty 中等 |
| Reproducibility | 3/5 | 平台和统计方法报告充分，但缺少 API 超参数（temperature 等）、无代码/数据发布声明、test-retest 仅覆盖 OpenAI 模型族 |
| Confidence | 4/5 | 仔细阅读了论文并熟悉相关统计方法和 agent safety 文献 |

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] TOST SESOI ±15 pp 缺乏外部锚定，two-tier structure 强烈依赖 margin 选择

- 具体位置：Section 4.6, Appendix A (Table 2)
- 问题：论文选择 SESOI = ±15 pp 的理由是 "a type producing ≥15 pp more violations warrants distinct policy handling"（§4.6），这仅是作者自行设定的实践显著性标准，缺乏独立的外部锚定（如领域专家调研、已有安全阈值文献等）。从 Table 2 的敏感性分析看：±10 pp 时仅 3/6 mid-tier pairs 达到等价，±12 pp 时 5/6，直到 ±15 pp 才 6/6。这意味着 "robust two-tier structure"（abstract, §5.2）的声称本质上取决于是否接受 15 pp 这一特定阈值。mid-tier cluster 本身的内部极差约 11 pp（coreferential 31.6% 到 lexical 42.8%），SESOI 大于这个极差才形成 cluster——这在方法论上是循环的。
- 为什么影响接收：Type hierarchy (C2) 是论文三大贡献之一，如果 two-tier structure 的稳健性不成立，论文的核心叙事 "Differential Nocuity" 的精细化程度大打折扣。
- 建议修改方向：(1) 提供 SESOI 的外部锚定（如 policy 领域的 minimal important difference 文献、安全工程的 risk threshold 标准）；(2) 明确承认 two-tier structure 在 ±10–12 pp 时不稳健；(3) 考虑使用 margin-free 的方法（如 Bayesian estimation 或 bootstrap cluster analysis）作为补充。

**N2** [critical] Authorization scope 的 judge agreement (κ = 0.385) 过低，无法支撑 C4 的 "model-differentiating type" 声称

- 具体位置：Section 4.4, Section 5.4, Appendix G (Table 8)
- 问题：论文将 authorization scope 定位为 "model-differentiating type"（§5.4, Figure 3），52 pp 跨模型变异是 C4 最突出的发现。然而：(1) cross-judge κ = 0.385 仅为 "fair"，是六个 type 中最低的；(2) human-LLM κ = 0.644，CI = [0.35, 0.91]，下界仅 0.35；(3) 论文辩称 "48 pp within-judge range far exceeds measurement noise"，但 κ = 0.385 意味着约 38.5% 的 judge agreement 超出 chance 水平——在这种信度下，52 pp 的跨模型变异中有多少是真实的 model difference、多少是测量噪声，无法可靠区分。
- 为什么影响接收：C4 是论文提出 "safety training selectively mitigates boundary-type ambiguities" 这一实践建议的核心依据。如果 auth scope 的测量不可靠，从 Discussion 到 Conclusion 的建议链条断裂。
- 建议修改方向：(1) 对 auth scope 增加人工标注样本量（当前 n=34 per type 过小），缩窄 CI；(2) 报告 within-judge analysis 的 auth scope 专项信度；(3) 对 C4 的 auth scope claims 降级为 "suggestive" 而非 "robust"。

**N3** [critical] Incompleteness confound 分析缺乏透明度

- 具体位置：Section 5.2, Appendix F
- 问题：论文承认 incompleteness resolution 必然添加 policy content，造成 information-addition confound（§3, §5.2）。logistic regression 控制 per-clause token delta 后报告 "coefficient change < 8%, p = 0.022"，但：(1) 未展示完整回归表（coefficients, SEs, model fit），读者无法评估回归质量；(2) token count 是 information content 的粗糙代理——添加一句 "customized items are final sale" 的信息量远超其 token 数所能捕捉；(3) 论文在 abstract 中将 incompleteness 列为 "consistently high (46–62%)" 的核心发现，但正文又承认这是 "upper bound partly reflecting an information-addition confound"——这两个表述在摘要中未分化，有误导读者之嫌。
- 为什么影响接收：Incompleteness 是 violation rate 最高的 type，是论文多个 practical implication 的基础。
- 建议修改方向：(1) 展示完整回归表；(2) 探索更好的 information content proxy；(3) 在 abstract 中明确标注 incompleteness 效应含 confound。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 缺少 API 超参数报告
- 具体位置：Section 4.3
- 论文未报告 temperature、max_tokens、top_p 等采样参数，对 reproducibility 有直接影响。

**W2** [warning] Test-retest stability (ICC) 仅在 OpenAI 模型族内测量
- 具体位置：Section 4.5
- ICC = 0.919 来自 GPT-5.4 和 GPT-4.1。跨 provider 的 test-retest 未测量。

**W3** [warning] Per-type human-LLM agreement 的 CI 极宽
- 具体位置：Appendix G (Table 8)
- Scopal CI = [0.00, 1.00]（完全无信息），Coreferential CI = [0.00, 0.84]。源于 per-type n = 32–34。建议在正文讨论此限制。

**W4** [warning] 无代码/数据可用性声明
- 论文未提及 300 clause pairs、代码或 evaluation pipeline 的发布计划。

**W5** [warning] Clause-level heterogeneity未充分分析
- 具体位置：Section 5.1
- Clause identity 解释 22.4% variance，但未分析 outlier clauses、type 内 clause-level variance 分布。50 clauses/type + high variance → type-level 估计可能不稳定。

**W6** [warning] 人工标注者是否对 condition 设盲？
- 具体位置：Section 4.4
- 报告了 blind to LLM labels，但未说明是否 blind to ambiguity condition。

---

### 小问题（不影响接收）

- **M1**: bib 有 4 个 orphan 条目（ferreira_patson_2007, lassiter_goodman_2017, levy_expectation_2008, poesio_artstein_2005）未引用。
- **M2**: ferrari_defects_2018 的 bib 一作为 Rosadini 但 key 暗示 Ferrari，可能引起混淆。
- **M3**: Error analysis 的 inter-coder κ = 0.52，minority category κ = 0.29，建议将 failure mode taxonomy 降级为 exploratory observation 而非 contribution。
- **M4**: C3 (layer effect) 在正文标为 inconclusive，但 abstract 未提及此 null result。

---

### Questions（需要作者回答）

**Q1**: SESOI = ±15 pp 是否有外部文献或专家调研支持？±10 pp 时 type hierarchy 如何变化？

**Q2**: 能否提供 within-judge subgroup 的 authorization scope 专项 κ？

**Q3**: Incompleteness confound 的 logistic regression 完整回归表？是否考虑过 information-theoretic measures 作为更好的 proxy？

**Q4**: Temperature 设置为多少？是否在 temperature > 0 下测试过 stability？

**Q5**: 300 clause pairs 是否计划公开？

---

### Missing References

- Kadavath et al. (2022) "Language Models (Mostly) Know What They Know" — 与 Ambiguity Blindness 相关
- Anvari & Lakens (2021) "Using Anchor-Based Methods to Determine the Smallest Effect Size of Interest" — 锚定 SESOI 选择
- Zheng et al. (2024) "Judging LLM-as-a-Judge" — LLM-as-judge 方法论

---

### 主要优势

- C1 (binary ambiguity effect) 有强力支撑：OR = 15.1, CI = [10.78, 21.17], 7 模型 replication
- Matched-pair design + perturbation control 的因果推理框架设计良好
- 诚实的 limitation 讨论（C3 inconclusive, C4 exploratory, incompleteness confound）
- Ambiguity Blindness (<11% awareness) 是一个直观但重要的经验发现
- TOST sensitivity analysis (Table 2) 虽然暴露了 margin 依赖性，但提供这一分析本身体现了方法论严谨性
- Two-model replication (Gemini, LLaMA) 增强了 C1 的外部效度

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-21T17:03:50.717372+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n### Weaknesses\n\n**W1 [MUST-FIX] Incompleteness confound 削弱 type hierarchy 核心 claim。**\n- Incompleteness 的 unambiguous variant 必须添加新 policy content，49.2 pp effect 混淆了\"歧义消除\"与\"信息增加\"。Logistic regression 控制 information delta（coefficient change <8%, p=0.022）不够充分：token count 只是信息量的粗略代理；regression 中 incompleteness 仍 significant 只说明残余效应存在，无法量化歧义效应 vs. 信息添加效应的比例。\n- 直接影响 Table 1 中 incompleteness 作为 hierarchy 顶端的可信度，影响 Abstract/Conclusion 中 \"type primarily determines severity\" 的 claim。\n- 建议：设计 information-matched control，或在 Abstract/Conclusion 显式降低对 incompleteness 排名的 claim 强度。\n\n**W2 [MUST-FIX] Authorization scope 测量可靠性不足以支撑 \"model-differentiating type\" 论述。**\n- Authorization scope cross-judge κ=0.385（fair），human-LLM κ=0.644。论文将其作为 C4 核心发现（52 pp range），但测量工具不可靠时，模型间差异可能部分反映 judge 不稳定性。\n- 建议：明确标注该结论为 tentative，或增加 bootstrap CI 量化测量不确定性对模型排名的影响。\n\n**W3 [SHOULD-FIX] Related Work 有 4 条 orphan bib 条目和若干遗漏。**\n- Orphan：ferreira_patson_2007, levy_expectation_2008, lassiter_goodman_2017, poesio_artstein_2005\n- 遗漏：Constitutional AI/RLHF alignment 文献、AgentBench、引用数 35 条偏少\n\n**W4 [SHOULD-FIX] Differential Nocuity 框架概念化不足。**\n- 三因素（type, safety training, channel availability）交互关系未形式化；\"channel availability\"在论文中未直接测量；与 Berry & Kamsties (2004) 的理论推进关系不清晰。\n\n**W5 [SHOULD-FIX] Abstract 信息密度过高。**\n- 包含 6 个统计量、嵌套括号、C1–C4 几乎所有结果的压缩。建议减少数字，保留 2-3 核心发现。\n\n**W6 [SHOULD-FIX] C3 layer effect null result 讨论过于简短。**\n- §5.3 仅 3 句话。如果 linguistic/specification 二分法不成立，two-layer taxonomy 的理论基础需要重新论证。\n\n**W7 [MINOR] ferrari_defects_2018 bib 条目第一作者不一致。**\n\n**W8 [MINOR] 缺少 Ethics Statement。**\n\n### Questions\nQ1. Incompleteness 的 unambiguous variant 平均添加了多少 token？\nQ2. Authorization scope 的 52 pp model range 中，Claude 12% 是否因 conservative refusal？\nQ3. 是否考虑过 information-addition perturbation 作为 incompleteness confound 的更直接控制？\nQ4. Template-based pipeline 的 template 设计是否公开？96% annotator pass rate 的 disagreement 是否集中在特定类型？\n\n### Missing References\n- Levy (2008), Ferreira & Patson (2007), Constitutional AI (Bai et al., 2022), AgentBench (Liu et al., 2023), Bender & Koller (2020)\n\n### Overall Assessment\n3.5 (Borderline Conference), Confidence 4/5 (High)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n### Weaknesses\n\n**W1 [MUST-FIX] Incompleteness confound 削弱 type hierarchy 核心 claim。**\n- Incompleteness 的 unambiguous variant 必须添加新 policy content，49.2 pp effect 混淆了\"歧义消除\"与\"信息增加\"。Logistic regression 控制 information delta（coefficient change <8%, p=0.022）不够充分：token count 只是信息量的粗略代理；regression 中 incompleteness 仍 significant 只说明残余效应存在，无法量化歧义效应 vs. 信息添加效应的比例。\n- 直接影响 Table 1 中 incompleteness 作为 hierarchy 顶端的可信度，影响 Abstract/Conclusion 中 \"type primarily determines severity\" 的 claim。\n- 建议：设计 information-matched control，或在 Abstract/Conclusion 显式降低对 incompleteness 排名的 claim 强度。\n\n**W2 [MUST-FIX] Authorization scope 测量可靠性不足以支撑 \"model-differentiating type\" 论述。**\n- Authorization scope cross-judge κ=0.385（fair），human-LLM κ=0.644。论文将其作为 C4 核心发现（52 pp range），但测量工具不可靠时，模型间差异可能部分反映 judge 不稳定性。\n- 建议：明确标注该结论为 tentative，或增加 bootstrap CI 量化测量不确定性对模型排名的影响。\n\n**W3 [SHOULD-FIX] Related Work 有 4 条 orphan bib 条目和若干遗漏。**\n- Orphan：ferreira_patson_2007, levy_expectation_2008, lassiter_goodman_2017, poesio_artstein_2005\n- 遗漏：Constitutional AI/RLHF alignment 文献、AgentBench、引用数 35 条偏少\n\n**W4 [SHOULD-FIX] Differential Nocuity 框架概念化不足。**\n- 三因素（type, safety training, channel availability）交互关系未形式化；\"channel availability\"在论文中未直接测量；与 Berry & Kamsties (2004) 的理论推进关系不清晰。\n\n**W5 [SHOULD-FIX] Abstract 信息密度过高。**\n- 包含 6 个统计量、嵌套括号、C1–C4 几乎所有结果的压缩。建议减少数字，保留 2-3 核心发现。\n\n**W6 [SHOULD-FIX] C3 layer effect null result 讨论过于简短。**\n- §5.3 仅 3 句话。如果 linguistic/specification 二分法不成立，two-layer taxonomy 的理论基础需要重新论证。\n\n**W7 [MINOR] ferrari_defects_2018 bib 条目第一作者不一致。**\n\n**W8 [MINOR] 缺少 Ethics Statement。**\n\n### Questions\nQ1. Incompleteness 的 unambiguous variant 平均添加了多少 token？\nQ2. Authorization scope 的 52 pp model range 中，Claude 12% 是否因 conservative refusal？\nQ3. 是否考虑过 information-addition perturbation 作为 incompleteness confound 的更直接控制？\nQ4. Template-based pipeline 的 template 设计是否公开？96% annotator pass rate 的 disagreement 是否集中在特定类型？\n\n### Missing References\n- Levy (2008), Ferreira & Patson (2007), Constitutional AI (Bai et al., 2022), AgentBench (Liu et al., 2023), Bender & Koller (2020)\n\n### Overall Assessment\n3.5 (Borderline Conference), Confidence 4/5 (High)"
  }
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-21T17:04:13.054355+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22336
}
```

</details>

---


### Tool call

_source line 680 · 2026-05-21T17:04:13.155365+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n### Must-Fix 问题\n\n**N1 [critical] TOST SESOI ±15 pp 缺乏外部锚定，two-tier structure 强烈依赖 margin 选择**\n- SESOI = ±15 pp 仅是作者自行设定的实践显著性标准，缺乏独立的外部锚定。\n- ±10 pp 时仅 3/6 mid-tier pairs 达到等价，±12 pp 时 5/6，直到 ±15 pp 才 6/6。\n- mid-tier cluster 本身的内部极差约 11 pp，SESOI 大于这个极差才形成 cluster——方法论上是循环的。\n- 建议：提供外部锚定、承认 ±10–12 pp 不稳健、考虑 margin-free 方法（Bayesian estimation / bootstrap cluster analysis）。\n\n**N2 [critical] Authorization scope 的 judge agreement (κ = 0.385) 过低，无法支撑 C4 \"model-differentiating type\" 声称**\n- cross-judge κ = 0.385 仅为 \"fair\"，human-LLM κ = 0.644 CI = [0.35, 0.91] 下界仅 0.35。\n- κ = 0.385 意味着约 38.5% 的 judge agreement 超出 chance 水平——52 pp 跨模型变异中真实 model difference vs. 测量噪声无法可靠区分。\n- 建议：增加人工标注样本量、报告 within-judge auth scope 专项信度、C4 auth scope claims 降级为 \"suggestive\"。\n\n**N3 [critical] Incompleteness confound 分析缺乏透明度**\n- 未展示完整回归表（coefficients, SEs, model fit）。\n- Token count 是 information content 的粗糙代理。\n- Abstract 中将 incompleteness 列为 \"consistently high (46–62%)\" 但正文又承认 \"upper bound partly reflecting an information-addition confound\"——未分化，有误导之嫌。\n- 建议：展示完整回归表、探索更好的 information content proxy、abstract 中明确标注 confound。\n\n### Should-Fix 问题\n\n**W1 [warning] 缺少 API 超参数报告** — temperature, max_tokens, top_p 未报告。\n**W2 [warning] ICC 仅在 OpenAI 模型族内测量** — 跨 provider test-retest 未测量。\n**W3 [warning] Per-type human-LLM agreement CI 极宽** — Scopal CI = [0.00, 1.00]，源于 per-type n = 32–34。\n**W4 [warning] 无代码/数据可用性声明**\n**W5 [warning] Clause-level heterogeneity 未充分分析** — Clause identity 解释 22.4% variance，但未分析 outlier clauses。\n**W6 [warning] 人工标注者是否对 condition 设盲？**\n\n### 小问题\n\n**M1**: 4 个 orphan bib 条目。\n**M2**: ferrari_defects_2018 一作问题。\n**M3**: Error analysis inter-coder κ = 0.52，minority category κ = 0.29，建议降级为 exploratory。\n**M4**: C3 layer effect null result 在 abstract 未提及。\n\n### Questions\nQ1: SESOI = ±15 pp 是否有外部文献支持？±10 pp 时 type hierarchy 如何变化？\nQ2: 能否提供 within-judge auth scope 专项 κ？\nQ3: Incompleteness logistic regression 完整回归表？information-theoretic measures 作为更好 proxy？\nQ4: Temperature 设置为多少？\nQ5: 300 clause pairs 是否计划公开？\n\n### Missing References\n- Kadavath et al. (2022), Anvari & Lakens (2021), Zheng et al. (2024)\n\n### Overall Assessment\n3.5 (Borderline Conference), Confidence 4/5 (High)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n### Must-Fix 问题\n\n**N1 [critical] TOST SESOI ±15 pp 缺乏外部锚定，two-tier structure 强烈依赖 margin 选择**\n- SESOI = ±15 pp 仅是作者自行设定的实践显著性标准，缺乏独立的外部锚定。\n- ±10 pp 时仅 3/6 mid-tier pairs 达到等价，±12 pp 时 5/6，直到 ±15 pp 才 6/6。\n- mid-tier cluster 本身的内部极差约 11 pp，SESOI 大于这个极差才形成 cluster——方法论上是循环的。\n- 建议：提供外部锚定、承认 ±10–12 pp 不稳健、考虑 margin-free 方法（Bayesian estimation / bootstrap cluster analysis）。\n\n**N2 [critical] Authorization scope 的 judge agreement (κ = 0.385) 过低，无法支撑 C4 \"model-differentiating type\" 声称**\n- cross-judge κ = 0.385 仅为 \"fair\"，human-LLM κ = 0.644 CI = [0.35, 0.91] 下界仅 0.35。\n- κ = 0.385 意味着约 38.5% 的 judge agreement 超出 chance 水平——52 pp 跨模型变异中真实 model difference vs. 测量噪声无法可靠区分。\n- 建议：增加人工标注样本量、报告 within-judge auth scope 专项信度、C4 auth scope claims 降级为 \"suggestive\"。\n\n**N3 [critical] Incompleteness confound 分析缺乏透明度**\n- 未展示完整回归表（coefficients, SEs, model fit）。\n- Token count 是 information content 的粗糙代理。\n- Abstract 中将 incompleteness 列为 \"consistently high (46–62%)\" 但正文又承认 \"upper bound partly reflecting an information-addition confound\"——未分化，有误导之嫌。\n- 建议：展示完整回归表、探索更好的 information content proxy、abstract 中明确标注 confound。\n\n### Should-Fix 问题\n\n**W1 [warning] 缺少 API 超参数报告** — temperature, max_tokens, top_p 未报告。\n**W2 [warning] ICC 仅在 OpenAI 模型族内测量** — 跨 provider test-retest 未测量。\n**W3 [warning] Per-type human-LLM agreement CI 极宽** — Scopal CI = [0.00, 1.00]，源于 per-type n = 32–34。\n**W4 [warning] 无代码/数据可用性声明**\n**W5 [warning] Clause-level heterogeneity 未充分分析** — Clause identity 解释 22.4% variance，但未分析 outlier clauses。\n**W6 [warning] 人工标注者是否对 condition 设盲？**\n\n### 小问题\n\n**M1**: 4 个 orphan bib 条目。\n**M2**: ferrari_defects_2018 一作问题。\n**M3**: Error analysis inter-coder κ = 0.52，minority category κ = 0.29，建议降级为 exploratory。\n**M4**: C3 layer effect null result 在 abstract 未提及。\n\n### Questions\nQ1: SESOI = ±15 pp 是否有外部文献支持？±10 pp 时 type hierarchy 如何变化？\nQ2: 能否提供 within-judge auth scope 专项 κ？\nQ3: Incompleteness logistic regression 完整回归表？information-theoretic measures 作为更好 proxy？\nQ4: Temperature 设置为多少？\nQ5: 300 clause pairs 是否计划公开？\n\n### Missing References\n- Kadavath et al. (2022), Anvari & Lakens (2021), Zheng et al. (2024)\n\n### Overall Assessment\n3.5 (Borderline Conference), Confidence 4/5 (High)"
  }
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-21T17:04:14.463863+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1308
}
```

</details>

---


### Assistant

_source line 682 · 2026-05-21T17:04:17.217471+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 63

## Round 63

2 recorded events


### User

_source line 683 · 2026-05-21T17:04:18.208102+00:00_

[Reviewer 2 审稿结果]:
审稿完成。已将完整审稿意见提交给 Review Director。

核心判断：**Overall 3.5 (Borderline Conference)**。

主要发现：
- **2 个 MUST-FIX**：incompleteness confound 削弱 type hierarchy 核心 claim；authorization scope 低测量可靠性（κ=0.385）削弱 model-differentiating 发现
- **4 个 SHOULD-FIX**：Related Work 有 4 条 orphan bib + 遗漏；Differential Nocuity 框架概念化不足；Abstract 信息密度过高；C3 null result 讨论过于简短
- **2 个 MINOR**：bib 条目 ferrari_defects_2018 作者/年份不一致；缺少 Ethics Statement

论文的 CL-first framing、matched-pair 因果设计和七模型复制是明确优势，若能解决 incompleteness confound 和 claim calibration 问题，有提升至 Conference 水平的潜力。

---

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：我以 Reviewer 1 身份完成了对论文 "Not All Policy Ambiguity Is Equal" 的方法严谨性 + 实验设计审查。**Overall 评分 3.5 (Borderline Conference)**。

核心判断：C1（ambiguity causes violations, OR=15.1）有充分支撑，但从 C1 到 "type-specific differential nocuity"（C2+C4）的推理链有三个关键短板：
1. **TOST SESOI ±15 pp 无外部锚定**，two-tier structure 在 ±10 pp 时不成立
2. **Authorization scope 的 judge κ=0.385 过低**，无法可靠支撑 52 pp 跨模型变异的解读
3. **Incompleteness confound regression 未展示完整回归表**，token count 作为 information content proxy 过于粗糙

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 684 · 2026-05-21T17:04:25.273551+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 64

## Round 64

2 recorded events


### User

_source line 685 · 2026-05-21T17:06:11.443029+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### W1 [MUST-FIX] Incompleteness confound 削弱 type hierarchy 核心 claim

**[AGREE] R2-W1**: 我在 N3 中提出了相同的核心关切。补充两点：

1. R2 精准指出了关键区分——"残余效应存在 ≠ 可量化歧义 vs. 信息比例"。Appendix F 的 logistic regression 报告 p=0.022 仅说明控制 token delta 后 incompleteness 仍 significant，但无法回答"49.2 pp 中多少归因于 ambiguity、多少归因于 information addition"。这是 partial-out 与 decomposition 的区别，论文混淆了二者。

2. 我进一步注意到 Appendix F 的一个额外问题：排除 incompleteness 后五类的 omnibus χ² 不显著（p=0.079），只有 pairwise contrasts 在 Holm-Bonferroni 后保留了 auth scope 和 lexical 相对 coreferential 的显著性。这意味着如果 incompleteness 排名确实受 confound 污染，剩余五类之间的 type hierarchy 本身也是 borderline 的（omnibus p=0.079），进一步削弱 "type primarily determines severity" 的 claim 强度。

**建议优先级一致**：information-matched control 或显式降级 Abstract/Conclusion 中的 claim。

---

### W2 [MUST-FIX] Authorization scope 测量可靠性不足

**[AGREE] R2-W2**: 与我的 N2 完全一致。补充一个 R2 未展开的角度：

论文在 §5.4 中辩称 "within-judge analysis" 控制了 judge identity（Claude 12%, Qwen3 26%, DeepSeek 60%, all judged by GPT-5.4）。但 within-judge 控制只解决了 cross-judge confounding，**不解决 per-type measurement noise**。κ=0.385 是 auth scope 这个 type 本身的 judge agreement，无论是哪个 judge 在评判——即 GPT-5.4 对 auth scope violations 的判定本身就不稳定。因此 within-judge 48 pp range 中仍然可能包含大量 measurement noise。

R2 建议的 "bootstrap CI 量化测量不确定性对模型排名的影响" 是一个很好的具体建议，优于我的 N2 中的一般性建议。

---

### W3 [SHOULD-FIX] Related Work orphan bib 和遗漏

**[AGREE] R2-W3 (orphan bib 部分)**: 4 条 orphan 条目应清理，我在 M1 中也指出了这一点。

**[REBUT] R2-W3 (遗漏部分，部分反驳)**:

- **Constitutional AI (Bai et al., 2022) / RLHF**: 论文的研究对象是 policy specification 中的 ambiguity 如何导致 violations，而非 alignment 方法本身。C4 关于 safety training 的讨论是 exploratory 的，明确标注为 [Exploratory]（§5.4 标题），且论文未 claim 研究 alignment 机制。要求引用 Constitutional AI 相当于要求论文扩大 scope——这不是一个审稿人应该要求的。
- **AgentBench (Liu et al., 2023)**: AgentBench 是通用 agent 能力 benchmark，不涉及 policy ambiguity 或 safety violations。论文已引用了多个直接相关的 agent safety benchmark（R-Judge, ToolEmu, InjecAgent, AgentAuditor, ShieldAgent），这些比 AgentBench 更 relevant。
- **Bender & Koller (2020)**: 关于语言理解的 stochastic parrots 论文与本文研究问题关联较远。
- **"引用数 35 条偏少"**: 引用数量不是评判标准。论文的 Related Work 覆盖了四个直接相关领域（NLP ambiguity, RE ambiguity, psycholinguistics, agent safety），每个领域都有代表性引用。质量优于数量。

---

### W4 [SHOULD-FIX] Differential Nocuity 框架概念化不足

**[AGREE] R2-W4 (部分同意)**: R2 指出的三个问题都成立：

1. 三因素交互未形式化——论文在 §7 用一段自然语言描述了 type × safety training × channel availability 的交互，但未提供任何形式化表达（如图、公式、或至少结构化的 prediction table）。
2. "Channel availability" 未直接测量——论文推断 incompleteness 缺乏 disambiguation channel（因为 gap-filling bypasses intervention points, §7），但这是事后解释而非实验证据。
3. 与 Berry & Kamsties (2004) 的推进关系确实不够清晰。

但我认为这应保持 SHOULD-FIX 而非升级为 MUST-FIX。论文的核心贡献是经验性的（C1-C4），Differential Nocuity 是在 Discussion 中提出的概念性框架，不是论文的 primary claim。要求完整形式化会改变论文的性质（从经验研究变为理论建模）。更合理的建议是：用一张简单的 2×3 table 展示三因素如何预测六种 type 的不同结果，使框架至少可被 falsifiable。

---

### W5 [SHOULD-FIX] Abstract 信息密度过高

**[REBUT] R2-W5**: 部分不同意。

重读 Abstract（§abstract），我统计了约 11 个数字（OR=15.1, V=0.137, p<10⁻⁴, ρ=0.90, p=0.037, ρ=0.60, 46-62%, 52 pp, 12%, 64%, 11%）。这确实密集，但：

1. 论文已经在 abstract 中对次要结果做了适度的 hedging——如 "though authorization scope carries the widest measurement uncertainty among types" 和 "partly reflecting an information-addition confound"。这说明作者意识到需要在 abstract 中传递 nuance。
2. 对于一篇以统计方法为核心的经验论文，abstract 中包含关键效应量和置信区间是合理的——如果删减到"2-3 核心发现"，readers 在浏览阶段无法判断效应量的实际大小。
3. 真正的问题不是数字太多，而是 incompleteness 的 confound caveat 在 abstract 中不够显眼（我在 N3 中已指出）。修复 N3 比减少数字更重要。

建议：保留核心统计量，但精简叙述结构——可以将 replication 结果移至 "Our results replicate across seven models" 一句，不列具体 ρ 值。

---

### W6 [SHOULD-FIX] C3 layer effect null result 讨论过于简短

**[AGREE] R2-W6 (部分同意)**: §5.3 确实过于简短（3 句话），但我认为这个问题的严重性低于 R2 的评估。

论文已给出了 C3 inconclusive 的三个理由：(1) 不survive Holm-Bonferroni 校正；(2) 控制 token delta 后方向反转；(3) cross-layer type overlap（conditional precedence 36.8% vs. scopal 39.4%）。这些理由充分解释了为什么 layer effect 不成立。

R2 的关键问题是对的：如果二分法不成立，two-layer taxonomy 的理论基础需要重新论证。但我认为论文的 taxonomy 价值在于**六种 type 的操作性区分**（每种对应不同 resolution mechanism，§3），而非层级分组。即使 layer 区分不成立，six-type taxonomy 仍然有效——它为 C2 的 type hierarchy 提供了分析框架。

建议：在 §5.3 补充 1-2 句话讨论 layer distinction 失败对 taxonomy 整体价值的影响，并在 §7 Discussion 中明确 taxonomy 的操作性价值独立于 layer 分组。

---

### W7 [MINOR] ferrari_defects_2018 bib 第一作者不一致

**[AGREE] R2-W7**: 与我的 M2 一致。应修正 bib key 或 author 列表。

---

### W8 [MINOR] 缺少 Ethics Statement

**[AGREE] R2-W8**: 论文涉及 LLM API 调用和人工标注（100 episodes, 两名标注者），应添加简短的 Ethics Statement。不过这是 camera-ready 级别的修正，不影响接收决定。

---

### R2 Questions 的补充意见

**Q1 (Incompleteness token delta)**: 同意这是一个必须回答的透明度问题。与我的 Q3 相关。

**Q2 (Claude 12% auth scope 是否因 conservative refusal)**: 这是一个很好的问题。§6.1 报告 auth scope violations 中 "69.2% involve unauthorized escalation with zero conservative refusals (p < 10⁻⁴)"，但这是 across all models 的统计。如果 Claude 的 auth scope violation rate 本身只有 12%（50 episodes 中约 6 个 violations），per-model 分析的统计力极有限。作者需要 (a) 提供 Claude 特定的 failure mode 分布，(b) 在 non-violation episodes 中 Claude 是否有 conservative refusal（即正确拒绝但理由错误）。

**Q3 (Information-addition perturbation)**: 与我的 N3 建议方向一致。

**Q4 (Template pipeline 透明度)**: 同意。这也关联我的 W4——如果 template 设计未公开，clause pair 质量依赖于信任。96% pass rate 中的 disagreement 类型分布也很重要——如果 disagreement 集中在特定 type（如 auth scope），这会加剧 N2 的信度问题。

---

### R2 Missing References 的补充意见

- **Levy (2008), Ferreira & Patson (2007)**: 这两篇在 bib 中但未被引用（orphan entries）。如果 R2 认为它们应该被引用，说明论文可能在某个版本中删除了相关讨论但忘记清理 bib。应当决定：引用它们（在 psycholinguistics 段落中有自然位置）或删除 bib 条目。
- **Constitutional AI, AgentBench, Bender & Koller**: 如我在 W3 rebut 中所述，前两者与论文 scope 不直接相关，后者关联较远。不认为这些是必要遗漏。

---

### 综合评估

R2 和我在三个核心问题上达成一致：**(1) incompleteness confound (R2-W1 / R1-N3)**, **(2) auth scope 信度 (R2-W2 / R1-N2)**, **(3) orphan bib (R2-W3 / R1-M1)**。我还额外提出了 **SESOI 外部锚定 (R1-N1)** 和 **API 超参数缺失 (R1-W1)** 这两个 R2 未覆盖的问题。

两位 reviewer 独立给出了相同的 Overall (3.5) 和 Confidence (4/5)，增强了评估的可信度。论文的 C1 (binary effect) 是 solid 的，但从 C1 到 C2/C4 的推理链条需要补强才能达到主会议水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 686 · 2026-05-21T17:06:24.656428+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 的交叉回应后进入收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 65

## Round 65

10 recorded events


### User

_source line 687 · 2026-05-21T17:06:25.650289+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的交叉回应

### Must-Fix

**[AGREE] R1-N1: TOST SESOI ±15 pp 缺乏外部锚定**
同意。§4.6 的锚定理由（practical significance + perturbation CI upper bound）存在逻辑跳跃。循环性问题成立：mid-tier cluster 内部极差 ~11 pp，选 ±15 pp 恰好让所有 mid-tier pairs 等价（Table 2/Appendix A）。±10 pp 时仅 3/6 等价，two-tier 结构会碎片化。补充：即使接受 ±15 pp，incompleteness 的分离也部分依赖 confound，真正 robust 的发现可能仅是 coreferential < 其余类型。建议 margin-free 方法作 sensitivity check。

**[AGREE] R1-N2: Authorization scope judge agreement 过低**
完全同意（与我的 W2 一致）。补充：(1) within-judge 只消除 judge identity 混淆，无法控制 per-instance inconsistency；(2) Appendix G auth scope human-LLM κ CI = [0.35, 0.91]，下界 0.35 进一步削弱所有定量结论。

**[AGREE with nuance] R1-N3: Incompleteness confound 透明度不足**
同意核心问题（与我的 W1 一致）。回归表未展示、Abstract 措辞不一致有误导。但对"完全重新设计实验"持保留：coreferential（information delta = 0, §5.2）提供了 confound-free lower bound（31.6%），确认纯歧义效应下界真实。问题是 incompleteness 在 hierarchy 中的确切位置不可信，非整体结论无效。

### Should-Fix

**[AGREE] R1-W1 (API 超参)**: 合理，temperature 可影响 conservative/permissive 行为。
**[AGREE] R1-W2 (ICC 跨 provider)**: C1 方向一致性 ≠ test-retest reliability。
**[AGREE] R1-W3 (Per-type CI 极宽)**: Scopal CI=[0.00,1.00] 统计上无信息量，caveat 未在正文出现。
**[AGREE] R1-W4 (无代码/数据声明)**: EMNLP 要求 reproducibility checklist。
**[AGREE with caveat] R1-W5 (Clause heterogeneity)**: 方向同意但严重程度略低——matched-pair 设计部分控制了 clause-level baseline。建议 leave-one-out sensitivity。
**[AGREE] R1-W6 (标注者 condition 设盲)**: §4.4 仅说 blind to LLM judge labels，未说 blind to condition。

### 小问题

**[AGREE] R1-M1/M2**: 与我的 W3/W7 一致。
**[AGREE with qualification] R1-M3**: §6 已标记 [Exploratory]。补充关注：error analysis 完全基于 LLM coders 而非 human coders，系统性偏差无法被 inter-coder κ 捕获。
**[AGREE] R1-M4**: 与我的 W6 一致，C3 null result 在 abstract 中被选择性省略。

### Missing References

- Kadavath et al. (2022): 低优先级，与 Ambiguity Blindness 联系不紧密。
- Anvari & Lakens (2021): 若保留 TOST，应引用方法论最佳实践。
- Zheng et al. (2024) "LLM-as-a-Judge": 与 §4.4 judge 设计直接相关，确实应引用。

### Overall Assessment

**[AGREE] 3.5 Borderline Conference**。两份审稿独立达成相同评分和 confidence。核心共识：C2（type hierarchy）面临三个独立方向的挑战——(1) SESOI 敏感性（R1-N1），(2) incompleteness confound（R1-N3/我的 W1），(3) auth scope 测量噪声（R1-N2/我的 W2）。论文最突出的贡献（type-specific risk）在当前形式下支撑不够稳固。

---

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

总结：对 R2 的 8 条 weakness 中，我 **[AGREE]** 了 W1, W2, W4(部分), W6(部分), W7, W8 共 6 条（与我自己的 N2, N3, M1, M2 一致），**[REBUT]** 了 W3 的遗漏引用部分（Constitutional AI/AgentBench/Bender & Koller 与论文 scope 不直接相关）和 W5（abstract 信息密度问题更在于 confound caveat 不够显眼，而非数字过多）。我额外补充了 R2 未涉及的两个发现：Appendix F 排除 incompleteness 后 omnibus p=0.079 进一步削弱 hierarchy claim、within-judge 控制不解决 per-type measurement noise。

---

[Reviewer 2 审稿结果]:
交叉回应已提交。两份审稿在核心问题上高度一致：incompleteness confound、authorization scope 测量可靠性、SESOI margin 选择。综合来看，C2（type hierarchy）从三个独立角度受到挑战，论文需要在这些方面加强才能达到 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-21T17:06:57.169781+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool call

_source line 689 · 2026-05-21T17:06:57.170226+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 690 · 2026-05-21T17:06:57.270985+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T16:55:18.189690+00:00\", \"completed_at\": \"2026-05-21T16:58:04.069092+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 3-5\", \"message\": \"连续 3 页纯文本（Section 3 Taxonomy → Section 4 Method → Section 5.1-5.2 Results），无任何 display item 穿插。Section 3 的六类 ambiguity taxonomy 是论文核心贡献之一，仅用 bullet-point 文字描述，缺少结构化的 taxonomy table 或 taxonomy figure 作为视觉锚点。审稿人翻过 Figure 1 后要连读 3 页纯文本才能看到下一个图表，节奏断裂\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"主文仅 4 个 display items（1 figure + 1 table + 2 figures），低于实证为主论文的典型密度（5-8 个）。建议增加：(1) taxonomy 结构表/图（Section 3），(2) matched-pair 示例表展示 ambiguous vs. unambiguous clause 对（Section 4.2），任选其一即可显著改善前半部分的视觉密度\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 三面板概览图内部文字偏小（尤其是 taxonomy 树的叶节点标签和中间面板的流程步骤文字），打印后可能难以辨认。建议增大面板内字号或简化标签\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 使用 booktabs 风格，最优值加粗，格式专业。但列数较多（5 models + Pooled + Δpp + p），单栏宽度下略显拥挤\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2 per-type effect sizes 柱状图带置信区间，颜色可区分，可读性良好\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 heatmap 百分比标注在格内，颜色梯度清晰。Caption 标注了 \\\"Ambiguous Condition, n = 2,997\\\"，自包含性好\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"附录页 Tables 3-7 密集排列，单页 5 张表格，个别表格（Table 5）行间距偏紧\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"最后一页仅填充约 55-60%，底部大面积空白。可考虑将部分附录内容调整以更充分利用空间\"}, {\"severity\": \"info\", \"dimension\": \"page 1-13\", \"message\": \"未发现 LaTeX 渲染错误、未解析引用 [?]、margin 溢出或 section heading 孤悬等问题，排版基础质量良好\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 7}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-21T17:06:57.271501+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 692 · 2026-05-21T17:08:41.720657+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Round 8 (Fresh) Review Issues — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Date: 2026-05-21\n## Round 8 Score: 3.5 (Borderline Conference)\n## Note: Fresh review session — all issues re-evaluated from scratch\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R8-N1\"\n  summary: \"TOST SESOI ±15pp 缺乏外部锚定，two-tier structure 在 ±10-12pp 时不稳健\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1 raised as N1, R2 AGREE. Mid-tier cluster 内部极差 ~11pp, ±15pp 恰好让所有 mid-tier pairs 等价——方法论循环。±10pp 时仅 3/6 等价, two-tier 结构碎片化。perturbation CI upper bound 作为锚定存在逻辑跳跃。\"\n  action_items:\n    - round: 8\n      action: \"提供 SESOI 外部锚定（领域文献/专家调研）；承认 ±10-12pp 时不稳健；考虑 margin-free 补充方法（Bayesian estimation / bootstrap cluster analysis）；引用 Anvari & Lakens (2021)\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N2\"\n  summary: \"Authorization scope cross-judge κ=0.385 过低，无法支撑 C4 'model-differentiating type' 声称\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-N2, R2-W2 独立提出. κ=0.385 仅 fair; human-LLM κ=0.644 CI=[0.35,0.91] 下界极低; within-judge 控制只解决 judge identity 混淆，无法控制 per-instance inconsistency; 52pp 跨模型变异中真实 model difference vs. 测量噪声无法可靠区分。\"\n  action_items:\n    - round: 8\n      action: \"C4 auth scope claims 降级为 'suggestive/tentative'; 增加 bootstrap CI 量化测量不确定性对模型排名影响; 报告 within-judge auth scope 专项信度; 考虑增加人工标注样本量\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N3\"\n  summary: \"Incompleteness confound 分析缺乏透明度，Abstract 措辞未分化\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-N3, R2-W1 独立提出. (1) Logistic regression 未展示完整回归表; (2) token count 是 information content 的粗糙代理; (3) Abstract 将 incompleteness 列为 'consistently high (46-62%)' 但正文承认 'upper bound partly reflecting confound'——未分化有误导; (4) R1 补充：排除 incompleteness 后 omnibus p=0.079, type hierarchy 本身 borderline。\"\n  action_items:\n    - round: 8\n      action: \"展示完整回归表（coefficients, SEs, model fit）; 探索更好 information content proxy; Abstract/Conclusion 中对 incompleteness 排名显式降级; 考虑 information-matched control\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R8-W1\"\n  summary: \"缺少 API 超参数报告（temperature, max_tokens, top_p）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-W1, R2 AGREE. Temperature 可影响 conservative/permissive 行为，直接影响 reproducibility。\"\n  action_items:\n    - round: 8\n      action: \"§4.3 补充所有 API 调用超参数\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"ICC=0.919 仅在 OpenAI 模型族内测量，跨 provider test-retest 未知\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-W2, R2 AGREE. C1 方向一致性 ≠ test-retest reliability。\"\n  action_items:\n    - round: 8\n      action: \"正文讨论此限制；或补充跨 provider ICC 数据\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W3\"\n  summary: \"Per-type human-LLM agreement CI 极宽（scopal CI=[0.00,1.00]），正文未讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-W3, R2 AGREE. Per-type n=32-34 过小，scopal CI 统计上无信息量。Caveat 仅在 Appendix G，正文未提及。\"\n  action_items:\n    - round: 8\n      action: \"正文讨论 per-type CI 宽度限制\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W4\"\n  summary: \"无代码/数据可用性声明\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-W4, R2 AGREE. 300 clause pairs, evaluation pipeline, analysis code 均未承诺发布。EMNLP 要求 reproducibility checklist。\"\n  action_items:\n    - round: 8\n      action: \"添加代码/数据可用性声明\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W5\"\n  summary: \"Clause-level heterogeneity 未充分分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-W5, R2 AGREE with caveat. Clause identity 解释 22.4% variance, 50 clauses/type + high variance → type-level 估计可能不稳定. R2: matched-pair 部分控制, 建议 leave-one-out sensitivity.\"\n  action_items:\n    - round: 8\n      action: \"分析 outlier clauses; 报告 type 内 clause-level variance 分布; 考虑 leave-one-out sensitivity analysis\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W6\"\n  summary: \"人工标注者是否对 ambiguity condition 设盲未说明\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-W6, R2 AGREE. §4.4 仅说 blind to LLM judge labels，未说 blind to ambiguity condition。\"\n  action_items:\n    - round: 8\n      action: \"§4.4 明确说明标注者是否对 condition 设盲\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W7\"\n  summary: \"Differential Nocuity 框架概念化不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R2-W4, R1 部分 AGREE. 三因素交互未形式化; channel availability 未直接测量; 与 Berry & Kamsties (2004) 理论推进关系不清. R1 建议保持 SHOULD-FIX, 用 2×3 table 使框架可 falsifiable。\"\n  action_items:\n    - round: 8\n      action: \"用 prediction table 或简单形式化展示三因素框架; 明确 channel availability 是推断而非测量; 降级或充分形式化\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W8\"\n  summary: \"C3 layer effect null result 讨论过于简短，abstract 未提及\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R2-W6 + R1-M4. §5.3 仅 3 句话; 如 linguistic/specification 二分法不成立, two-layer taxonomy 理论基础需重新论证. R1 部分同意: taxonomy 操作性价值独立于 layer 分组, 建议补充 1-2 句讨论。Abstract 选择性省略此 null result.\"\n  action_items:\n    - round: 8\n      action: \"§5.3 补充讨论 layer distinction 失败对 taxonomy 价值的影响; Abstract 简要提及 C3 inconclusive; §7 明确 taxonomy 操作性价值独立于 layer 分组\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W9\"\n  summary: \"4 条 orphan bib 条目 + Related Work 遗漏\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-M1, R2-W3. Orphan: ferreira_patson_2007, levy_expectation_2008, lassiter_goodman_2017, poesio_artstein_2005. 应决定引用或删除. 遗漏: Zheng et al. (2024) LLM-as-a-Judge 与 §4.4 直接相关 (两人共识); Anvari & Lakens (2021) 如保留 TOST 应引. R1 反驳 Constitutional AI/AgentBench/Bender & Koller 不在 scope 内.\"\n  action_items:\n    - round: 8\n      action: \"清理 4 条 orphan bib; 引用 Zheng et al. (2024); 考虑引用 Anvari & Lakens (2021)\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# MINOR ISSUES\n# ============================================================\n\n- id: \"R8-M1\"\n  summary: \"ferrari_defects_2018 bib key 暗示 Ferrari 但一作为 Rosadini\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-M2, R2-W7. Key 与实际一作不一致可能引起混淆。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M2\"\n  summary: \"缺少 Ethics Statement\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R2-W8, R1 AGREE. 论文揭示 LLM agent 系统性安全漏洞, 涉及 API 调用和人工标注. Camera-ready 级修正.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M3\"\n  summary: \"Error analysis inter-coder κ=0.52, minority category κ=0.29\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-M3, R2 partial AGREE. §6 已标 [Exploratory]. R2 补充: error analysis 完全基于 LLM coders, 系统性偏差无法被 inter-coder κ 捕获.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M4\"\n  summary: \"Abstract 信息密度高，incompleteness confound caveat 不够显眼\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R2-W5 raised, R1 REBUT 部分: 问题不在数字过多而在 confound caveat 不够显眼. R1 建议保留核心统计量但精简叙述结构.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Round 8 (Fresh) Review Issues — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Date: 2026-05-21\n## Round 8 Score: 3.5 (Borderline Conference)\n## Note: Fresh review session — all issues re-evaluated from scratch\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R8-N1\"\n  summary: \"TOST SESOI ±15pp 缺乏外部锚定，two-tier structure 在 ±10-12pp 时不稳健\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1 raised as N1, R2 AGREE. Mid-tier cluster 内部极差 ~11pp, ±15pp 恰好让所有 mid-tier pairs 等价——方法论循环。±10pp 时仅 3/6 等价, two-tier 结构碎片化。perturbation CI upper bound 作为锚定存在逻辑跳跃。\"\n  action_items:\n    - round: 8\n      action: \"提供 SESOI 外部锚定（领域文献/专家调研）；承认 ±10-12pp 时不稳健；考虑 margin-free 补充方法（Bayesian estimation / bootstrap cluster analysis）；引用 Anvari & Lakens (2021)\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N2\"\n  summary: \"Authorization scope cross-judge κ=0.385 过低，无法支撑 C4 'model-differentiating type' 声称\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-N2, R2-W2 独立提出. κ=0.385 仅 fair; human-LLM κ=0.644 CI=[0.35,0.91] 下界极低; within-judge 控制只解决 judge identity 混淆，无法控制 per-instance inconsistency; 52pp 跨模型变异中真实 model difference vs. 测量噪声无法可靠区分。\"\n  action_items:\n    - round: 8\n      action: \"C4 auth scope claims 降级为 'suggestive/tentative'; 增加 bootstrap CI 量化测量不确定性对模型排名影响; 报告 within-judge auth scope 专项信度; 考虑增加人工标注样本量\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N3\"\n  summary: \"Incompleteness confound 分析缺乏透明度，Abstract 措辞未分化\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-N3, R2-W1 独立提出. (1) Logistic regression 未展示完整回归表; (2) token count 是 information content 的粗糙代理; (3) Abstract 将 incompleteness 列为 'consistently high (46-62%)' 但正文承认 'upper bound partly reflecting confound'——未分化有误导; (4) R1 补充：排除 incompleteness 后 omnibus p=0.079, type hierarchy 本身 borderline。\"\n  action_items:\n    - round: 8\n      action: \"展示完整回归表（coefficients, SEs, model fit）; 探索更好 information content proxy; Abstract/Conclusion 中对 incompleteness 排名显式降级; 考虑 information-matched control\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R8-W1\"\n  summary: \"缺少 API 超参数报告（temperature, max_tokens, top_p）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-W1, R2 AGREE. Temperature 可影响 conservative/permissive 行为，直接影响 reproducibility。\"\n  action_items:\n    - round: 8\n      action: \"§4.3 补充所有 API 调用超参数\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"ICC=0.919 仅在 OpenAI 模型族内测量，跨 provider test-retest 未知\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-W2, R2 AGREE. C1 方向一致性 ≠ test-retest reliability。\"\n  action_items:\n    - round: 8\n      action: \"正文讨论此限制；或补充跨 provider ICC 数据\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W3\"\n  summary: \"Per-type human-LLM agreement CI 极宽（scopal CI=[0.00,1.00]），正文未讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-W3, R2 AGREE. Per-type n=32-34 过小，scopal CI 统计上无信息量。Caveat 仅在 Appendix G，正文未提及。\"\n  action_items:\n    - round: 8\n      action: \"正文讨论 per-type CI 宽度限制\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W4\"\n  summary: \"无代码/数据可用性声明\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-W4, R2 AGREE. 300 clause pairs, evaluation pipeline, analysis code 均未承诺发布。EMNLP 要求 reproducibility checklist。\"\n  action_items:\n    - round: 8\n      action: \"添加代码/数据可用性声明\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W5\"\n  summary: \"Clause-level heterogeneity 未充分分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-W5, R2 AGREE with caveat. Clause identity 解释 22.4% variance, 50 clauses/type + high variance → type-level 估计可能不稳定. R2: matched-pair 部分控制, 建议 leave-one-out sensitivity.\"\n  action_items:\n    - round: 8\n      action: \"分析 outlier clauses; 报告 type 内 clause-level variance 分布; 考虑 leave-one-out sensitivity analysis\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W6\"\n  summary: \"人工标注者是否对 ambiguity condition 设盲未说明\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-W6, R2 AGREE. §4.4 仅说 blind to LLM judge labels，未说 blind to ambiguity condition。\"\n  action_items:\n    - round: 8\n      action: \"§4.4 明确说明标注者是否对 condition 设盲\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W7\"\n  summary: \"Differential Nocuity 框架概念化不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R2-W4, R1 部分 AGREE. 三因素交互未形式化; channel availability 未直接测量; 与 Berry & Kamsties (2004) 理论推进关系不清. R1 建议保持 SHOULD-FIX, 用 2×3 table 使框架可 falsifiable。\"\n  action_items:\n    - round: 8\n      action: \"用 prediction table 或简单形式化展示三因素框架; 明确 channel availability 是推断而非测量; 降级或充分形式化\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W8\"\n  summary: \"C3 layer effect null result 讨论过于简短，abstract 未提及\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R2-W6 + R1-M4. §5.3 仅 3 句话; 如 linguistic/specification 二分法不成立, two-layer taxonomy 理论基础需重新论证. R1 部分同意: taxonomy 操作性价值独立于 layer 分组, 建议补充 1-2 句讨论。Abstract 选择性省略此 null result.\"\n  action_items:\n    - round: 8\n      action: \"§5.3 补充讨论 layer distinction 失败对 taxonomy 价值的影响; Abstract 简要提及 C3 inconclusive; §7 明确 taxonomy 操作性价值独立于 layer 分组\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W9\"\n  summary: \"4 条 orphan bib 条目 + Related Work 遗漏\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-M1, R2-W3. Orphan: ferreira_patson_2007, levy_expectation_2008, lassiter_goodman_2017, poesio_artstein_2005. 应决定引用或删除. 遗漏: Zheng et al. (2024) LLM-as-a-Judge 与 §4.4 直接相关 (两人共识); Anvari & Lakens (2021) 如保留 TOST 应引. R1 反驳 Constitutional AI/AgentBench/Bender & Koller 不在 scope 内.\"\n  action_items:\n    - round: 8\n      action: \"清理 4 条 orphan bib; 引用 Zheng et al. (2024); 考虑引用 Anvari & Lakens (2021)\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# MINOR ISSUES\n# ============================================================\n\n- id: \"R8-M1\"\n  summary: \"ferrari_defects_2018 bib key 暗示 Ferrari 但一作为 Rosadini\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-M2, R2-W7. Key 与实际一作不一致可能引起混淆。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M2\"\n  summary: \"缺少 Ethics Statement\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R2-W8, R1 AGREE. 论文揭示 LLM agent 系统性安全漏洞, 涉及 API 调用和人工标注. Camera-ready 级修正.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M3\"\n  summary: \"Error analysis inter-coder κ=0.52, minority category κ=0.29\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R1-M3, R2 partial AGREE. §6 已标 [Exploratory]. R2 补充: error analysis 完全基于 LLM coders, 系统性偏差无法被 inter-coder κ 捕获.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M4\"\n  summary: \"Abstract 信息密度高，incompleteness confound caveat 不够显眼\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"R2-W5 raised, R1 REBUT 部分: 问题不在数字过多而在 confound caveat 不够显眼. R1 建议保留核心统计量但精简叙述结构.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-21T17:08:41.821688+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 9462}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-21T17:11:24.016512+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85",
  "report": "# 审稿报告 — Round 8 (Fresh)\n\n**Paper**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**Reviewers**: R1 (方法严谨性 + 实验设计) / R2 (新颖性 + 完整性)\n**审稿模式**: Fresh (重新审稿)\n\n---\n\n## Summary\n\n本文研究自然语言 policy specification 中不同类型歧义对 LLM agent 安全违规的因果影响。提出六类型两层结构歧义分类体系（linguistic: scopal/lexical/coreferential; specification: authorization scope/incompleteness/conditional precedence），在 τ²-bench 上构建 300 对 matched clause pairs，评估 5 个模型共 2,997 episodes。核心发现：歧义整体增加 34.0 pp 违规率（OR=15.1, C1），类型间存在层级差异（Cramér's V=0.137, C2），layer effect inconclusive（C3），auth scope 跨模型变异最大（52 pp, C4 exploratory）。论文提出 Differential Nocuity 概念框架并报告 Ambiguity Blindness 现象（<11% awareness）。\n\n---\n\n## Strengths\n\n**S1. C1 binary ambiguity effect 有强力支撑。** OR=15.1, CI=[10.78, 21.17], McNemar p<10⁻⁵, 在全部 7 模型（含 2 个 replication 模型）上显著。Matched-pair design + perturbation control（Δ_perturb=−0.67 pp, CI 含零）有效排除表层扰动解释。这是论文最可靠的贡献。[R1, R2 共识]\n\n**S2. CL-first framing 对 EMNLP 有独特吸引力。** 从计算语言学歧义分类出发定位 agent safety 问题，与 WSD/garden-path 文献形成有意义连接。相比同期工作（如 DRIP-R 的相关性设计），因果推理框架设计更严格。[R2, R1 确认]\n\n**S3. 统计分析分层清晰、诚实。** C1–C4 按置信度递减排列，C3 inconclusive 坦诚报告，C4 明确标记 exploratory。TOST 敏感性分析（Table 2/Appendix A）虽暴露 margin 依赖性但体现方法论严谨。[R1, R2 共识]\n\n**S4. Ambiguity Blindness 有直接工程价值。** <11% awareness + 0% for Qwen3/DeepSeek 是一个直观且重要的经验发现，对 agent 部署有实践意义。[R2, R1 确认]\n\n**S5. 七模型六供应商覆盖增强外部效度。** 主实验 5 模型 + 2 模型 replication，C1 跨架构一致。Limitations 诚实全面。[R1, R2 共识]\n\n**S6. 因果设计优于同期工作。** Matched-pair + perturbation control 的双重因果推理框架是方法论贡献。DRIP-R 差异化论述（3 点）清晰。[R2, R1 确认]\n\n---\n\n## Weaknesses\n\n### Critical (Must-Fix)\n\n**N1. TOST SESOI ±15 pp 缺乏外部锚定，two-tier structure 强烈依赖 margin 选择。** [R1 raised, R2 AGREE]\n- §4.6 的锚定理由（practical significance + perturbation CI upper bound）仅是作者自行设定的标准，存在逻辑跳跃。\n- ±10 pp 时仅 3/6 mid-tier pairs 等价，±12 pp 时 5/6，直到 ±15 pp 才 6/6。Mid-tier cluster 内部极差 ~11 pp，SESOI 大于此极差才形成 cluster——方法论循环。\n- \"Robust two-tier structure\"（Abstract, §5.2）的声称本质上取决于是否接受 ±15 pp 这一特定阈值。\n- **影响**：C2 (type hierarchy) 是论文三大贡献之一，two-tier 稳健性不成立则 Differential Nocuity 精细化程度大打折扣。\n- **建议**：提供外部锚定（如 Anvari & Lakens 2021 的 anchor-based methods）；承认 ±10–12 pp 时不稳健；补充 margin-free 方法（Bayesian estimation / bootstrap cluster analysis）。\n\n**N2. Authorization scope cross-judge κ=0.385 过低，无法支撑 C4 \"model-differentiating type\" 声称。** [R1 raised, R2 AGREE]\n- cross-judge κ=0.385 仅 \"fair\"，是六类中最低；human-LLM κ=0.644, CI=[0.35, 0.91] 下界仅 0.35。\n- κ=0.385 意味着约 38.5% judge agreement 超出 chance，52 pp 跨模型变异中真实 model difference vs. 测量噪声无法可靠区分。\n- Within-judge 控制仅消除 judge identity 混淆，不解决 per-instance inconsistency（R1 补充，R2 确认）。\n- **影响**：C4 是 \"safety training selectively mitigates boundary-type ambiguities\" 的核心依据。测量不可靠则建议链条断裂。\n- **建议**：C4 auth scope claims 降级为 \"suggestive/tentative\"；增加 bootstrap CI 量化测量不确定性对模型排名的影响；考虑增加人工标注样本量。\n\n**N3. Incompleteness confound 分析缺乏透明度，Abstract 措辞有误导风险。** [R1 raised, R2 AGREE with nuance]\n- Logistic regression 控制 token delta 后 \"coefficient change <8%, p=0.022\"——但未展示完整回归表（coefficients, SEs, model fit），读者无法评估回归质量。\n- Token count 是 information content 的粗糙代理，\"残余效应存在 ≠ 可量化歧义 vs. 信息比例\"（R2 精确区分 partial-out vs. decomposition）。\n- Abstract 将 incompleteness 列为 \"consistently high (46–62%)\" 但正文承认 \"upper bound partly reflecting confound\"——未分化。\n- R1 补充：排除 incompleteness 后五类 omnibus χ² p=0.079，type hierarchy 本身 borderline。\n- R2 nuance：coreferential（information delta=0）提供 confound-free lower bound（31.6%），确认纯歧义效应下界真实——问题是 incompleteness 在 hierarchy 中的确切位置不可信，非整体结论无效。\n- **建议**：展示完整回归表；Abstract/Conclusion 对 incompleteness 排名显式降级；探索更好的 information proxy 或 information-matched control。\n\n### Warning (Should-Fix)\n\n**W1. 缺少 API 超参数报告。** [R1 raised, R2 AGREE] §4.3 未报告 temperature, max_tokens, top_p，直接影响 reproducibility。\n\n**W2. ICC=0.919 仅在 OpenAI 模型族内测量。** [R1 raised, R2 AGREE] 跨 provider test-retest 未测量。方向一致性 ≠ reliability。\n\n**W3. Per-type human-LLM agreement CI 极宽。** [R1 raised, R2 AGREE] Scopal CI=[0.00, 1.00]（统计上无信息量），源于 per-type n=32–34。正文未讨论此限制。\n\n**W4. 无代码/数据可用性声明。** [R1 raised, R2 AGREE] 300 clause pairs、evaluation pipeline、analysis code 均未承诺发布。EMNLP 要求 reproducibility checklist。\n\n**W5. Clause-level heterogeneity 未充分分析。** [R1 raised, R2 partial AGREE] Clause identity 解释 22.4% variance，但未分析 outlier clauses 或 type 内 clause-level variance 分布。50 clauses/type + high variance → type-level 估计可能不稳定。建议 leave-one-out sensitivity。\n\n**W6. 人工标注者是否对 ambiguity condition 设盲未说明。** [R1 raised, R2 AGREE] §4.4 仅说 blind to LLM judge labels。\n\n**W7. Differential Nocuity 框架概念化不足。** [R2 raised, R1 partial AGREE] 三因素交互未形式化；\"channel availability\" 未直接测量（推断 ≠ 测量）；与 Berry & Kamsties (2004) 理论推进关系不清。建议用 prediction table 使框架可 falsifiable，或降级为观察性建议。\n\n**W8. C3 layer effect null result 讨论过于简短，abstract 未提及。** [R2 raised, R1 partial AGREE] §5.3 仅 3 句话。如 linguistic/specification 二分法不成立，two-layer taxonomy 的理论基础需重新论证。R1 指出 taxonomy 操作性价值独立于 layer 分组。建议补充讨论 + abstract 简要提及。\n\n**W9. 4 条 orphan bib 条目 + 遗漏引用。** [R1+R2 共识] Orphan: ferreira_patson_2007, levy_expectation_2008, lassiter_goodman_2017, poesio_artstein_2005。应引用 Zheng et al. (2024) LLM-as-a-Judge（与 §4.4 直接相关）和 Anvari & Lakens (2021)（如保留 TOST）。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致：\n\n1. **[AGREE] C1 (binary effect) 是论文最可靠的贡献**，统计支撑充分，7 模型 replication 增强效度。\n2. **[AGREE] Incompleteness confound 是最严重的方法论问题**，影响 type hierarchy (C2) 核心 claim 的可信度。\n3. **[AGREE] Authorization scope κ=0.385 过低**，C4 claims 应降级。\n4. **[AGREE] TOST SESOI ±15 pp 选择方法论循环**，two-tier structure 在更严格 margin 下不稳健。\n5. **[AGREE] 缺少 API 超参数、代码/数据声明、标注者 condition blinding 细节**。\n6. **[AGREE] 4 条 orphan bib 应清理**。\n7. **[AGREE] Overall 3.5 (Borderline Conference)**, Confidence 4/5 (High)。\n\n---\n\n## Reviewer Divergence\n\n分歧较小，均为非关键问题：\n\n1. **[REBUT by R1] Missing references 范围**：R2 建议引用 Constitutional AI (Bai et al., 2022)、AgentBench (Liu et al., 2023)、Bender & Koller (2020)。R1 反驳这些不在论文 scope 内——Constitutional AI 是 alignment 方法非 policy ambiguity，AgentBench 是通用能力 benchmark 非 safety violations，Bender & Koller 关联较远。论文已引用 5+ 个直接相关 agent safety benchmark。**决议**：这些不列为必要遗漏。\n\n2. **[REBUT by R1] Abstract 信息密度**：R2 认为数字过多应减至 2-3 核心发现。R1 认为对经验论文保留效应量合理，真正问题在 incompleteness confound caveat 不够显眼。**决议**：问题降级为 info，重点是修复 confound caveat 可见度。\n\n---\n\n## Questions\n\n**Q1** [R1+R2]: Incompleteness 的 unambiguous variant 平均添加了多少 token？Information delta 分布？完整 logistic regression 回归表（coefficients, SEs, model fit）？\n\n**Q2** [R1]: SESOI = ±15 pp 是否有外部文献或专家调研支持？±10 pp 时 type hierarchy 如何变化？\n\n**Q3** [R1+R2]: 能否提供 within-judge subgroup 的 authorization scope 专项 κ？Claude 12% auth scope violation rate 中的 failure mode 分布？\n\n**Q4** [R1]: Temperature 设置为多少？是否在 temperature > 0 下测试过 stability？\n\n**Q5** [R1+R2]: 300 clause pairs 和 evaluation code 是否计划公开？\n\n**Q6** [R2]: 是否考虑过 information-addition perturbation（添加无关信息不消歧）作为 incompleteness confound 的更直接控制？\n\n**Q7** [R2]: Template-based pipeline 的 template 设计是否公开？96% annotator pass rate 的 disagreement 是否集中在特定类型？\n\n---\n\n## Missing References\n\n**两人共识应引用**：\n- Zheng et al. (2024) \"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\" — 与 §4.4 LLM-as-judge 设计直接相关\n- Anvari & Lakens (2021) \"Using Anchor-Based Methods to Determine the Smallest Effect Size of Interest\" — 若保留 TOST 方法应引用\n\n**R1 单独建议**：\n- Kadavath et al. (2022) \"Language Models (Mostly) Know What They Know\" — 与 Ambiguity Blindness 相关（低优先级）\n\n**R2 建议但 R1 反驳（不列为必要）**：\n- Constitutional AI (Bai et al., 2022) — 不在论文 scope 内\n- AgentBench (Liu et al., 2023) — 通用能力 benchmark，非 safety\n- Bender & Koller (2020) — 关联较远\n\n**Orphan entries 需处理**：\n- ferreira_patson_2007, levy_expectation_2008, lassiter_goodman_2017, poesio_artstein_2005 — 引用或删除\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（2026-05-21T16:55 → 16:58，耗时 ~3 分钟）\n\n**Findings (2 warning, 7 info)**：\n\n⚠️ **Warning**:\n1. **Pages 3-5**: 连续 3 页纯文本（§3 Taxonomy → §4 Method → §5.1-5.2），无 display item 穿插。§3 六类 taxonomy 仅用文字描述，缺少结构化 taxonomy table/figure 作为视觉锚点。\n2. **Pages 1-8**: 主文仅 4 个 display items（1 figure + 1 table + 2 figures），低于实证论文典型密度（5-8 个）。建议增加 taxonomy 结构表/图或 matched-pair 示例表。\n\nℹ️ **Info**:\n- Figure 1 子面板内部文字偏小，打印后可能难辨认。\n- Table 1 列数较多，单栏宽度下略显拥挤。\n- Figure 2 per-type effect sizes 柱状图可读性良好。\n- Figure 3 heatmap 颜色梯度清晰，caption 自包含性好。\n- 附录 Tables 3-7 密集排列，Table 5 行间距偏紧。\n- 最后一页填充约 55-60%，底部大面积空白。\n- 未发现 LaTeX 渲染错误、未解析引用 [?]、margin 溢出等问题，排版基础质量良好。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n**Confidence: High (4/5)**\n**两位 Reviewer 独立评分一致。**\n\n**总评**：论文研究问题重要且及时，CL-first framing 对 EMNLP 有独特贡献，C1 (binary ambiguity effect, OR=15.1) 有充分统计支撑和七模型 replication。Matched-pair + perturbation control 的因果推理框架是方法论亮点。\n\n但从 C1 到 \"type-specific differential nocuity\"（C2+C4）的推理链有三个关键短板：(1) TOST SESOI ±15 pp 无外部锚定，two-tier structure 在 ±10 pp 时碎片化；(2) authorization scope 的 judge κ=0.385 无法可靠支撑 52 pp 跨模型变异的解读；(3) incompleteness confound 的 logistic regression 不够透明，且排除 incompleteness 后 omnibus p=0.079。这三个问题从独立角度挑战 C2 (type hierarchy)——论文标题所承诺的 \"Not All Policy Ambiguity Is Equal\" 在当前数据下支撑不够稳固。\n\n若能：(a) 为 SESOI 提供外部锚定或补充 margin-free 方法，(b) 将 auth scope C4 claims 降级为 tentative，(c) 展示完整回归表并在 Abstract 中标注 incompleteness confound，论文有从 3.5 提升至 4.0 (Conference) 的潜力。当前状态建议 **Findings** 或 **Borderline Conference**。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 信息密度高但对经验论文可接受（R1 观点）。核心问题是 incompleteness confound caveat 不够显眼——\"consistently high (46–62%)\" 与 \"upper bound partly reflecting confound\" 应在同一句中出现。\n- C3 null result 未提及（R1-M4, R2-W6 共识），abstract 给人 type-specific 结论全部成立的印象。\n\n### Introduction\n- 开头 retail 场景有效。Contribution (2) 中同时出现 confound 和 [exploratory] 标记可能给读者不确定感。\n- Contribution list 应更 prominently 标注 C3 inconclusive / C4 exploratory。\n\n### Related Work (§2)\n- Psycholinguistics 段论证链清晰。DRIP-R 差异化论述（3 点）有效。\n- 4 条 orphan bib 需清理。应引用 Zheng et al. (2024)。\n\n### Taxonomy (§3)\n- 六类型结构清晰有例子。\"Frequency in operational policy documents\" 作为选择标准未报告具体频率数据。\n- 缺少视觉 taxonomy table/figure 是版面缺陷（视觉审查也标记）。\n\n### Method (§4)\n- Cross-judge calibration 详尽是方法论强项。\n- **缺失**：API 超参数（§4.3）、标注者 condition blinding（§4.4）、SESOI 外部锚定（§4.6）。\n- Model selection 未解释为何无 7B/13B 规模模型。\n\n### Results (§5)\n- C1 效应量大且显著——最强发现。\n- C2 TOST 是方法论亮点但 margin 依赖性是核心弱点。\n- **C3 过于简短**（3 句话），layer 二分法失败对 taxonomy 理论基础的影响未讨论。\n- C4 heatmap 有效但 auth scope 结论需降级。\n\n### Error Analysis (§6)\n- 三种 failure pattern 有意义，已标 [Exploratory]。\n- Inter-coder κ=0.52 (moderate)，minority category κ=0.29，完全基于 LLM coders——系统性偏差无法被 κ 捕获。\n\n### Discussion (§7)\n- Differential Nocuity 三因素缺形式化，channel availability 是推断非测量。\n- Mitigation experiment across-model variance 未充分讨论。\n\n### Conclusion\n- 简洁但可能过于简短，未提 future work。\n\n### Format Compliance\n- ✅ 正文 8 页\n- ✅ Double-blind（\\usepackage[review]{acl}, Anonymous author）\n- ✅ Limitations 存在且适当\n- ❌ 无 Ethics Statement（建议添加）\n- ❌ 无代码/数据可用性声明"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85",
    "report": "# 审稿报告 — Round 8 (Fresh)\n\n**Paper**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**Reviewers**: R1 (方法严谨性 + 实验设计) / R2 (新颖性 + 完整性)\n**审稿模式**: Fresh (重新审稿)\n\n---\n\n## Summary\n\n本文研究自然语言 policy specification 中不同类型歧义对 LLM agent 安全违规的因果影响。提出六类型两层结构歧义分类体系（linguistic: scopal/lexical/coreferential; specification: authorization scope/incompleteness/conditional precedence），在 τ²-bench 上构建 300 对 matched clause pairs，评估 5 个模型共 2,997 episodes。核心发现：歧义整体增加 34.0 pp 违规率（OR=15.1, C1），类型间存在层级差异（Cramér's V=0.137, C2），layer effect inconclusive（C3），auth scope 跨模型变异最大（52 pp, C4 exploratory）。论文提出 Differential Nocuity 概念框架并报告 Ambiguity Blindness 现象（<11% awareness）。\n\n---\n\n## Strengths\n\n**S1. C1 binary ambiguity effect 有强力支撑。** OR=15.1, CI=[10.78, 21.17], McNemar p<10⁻⁵, 在全部 7 模型（含 2 个 replication 模型）上显著。Matched-pair design + perturbation control（Δ_perturb=−0.67 pp, CI 含零）有效排除表层扰动解释。这是论文最可靠的贡献。[R1, R2 共识]\n\n**S2. CL-first framing 对 EMNLP 有独特吸引力。** 从计算语言学歧义分类出发定位 agent safety 问题，与 WSD/garden-path 文献形成有意义连接。相比同期工作（如 DRIP-R 的相关性设计），因果推理框架设计更严格。[R2, R1 确认]\n\n**S3. 统计分析分层清晰、诚实。** C1–C4 按置信度递减排列，C3 inconclusive 坦诚报告，C4 明确标记 exploratory。TOST 敏感性分析（Table 2/Appendix A）虽暴露 margin 依赖性但体现方法论严谨。[R1, R2 共识]\n\n**S4. Ambiguity Blindness 有直接工程价值。** <11% awareness + 0% for Qwen3/DeepSeek 是一个直观且重要的经验发现，对 agent 部署有实践意义。[R2, R1 确认]\n\n**S5. 七模型六供应商覆盖增强外部效度。** 主实验 5 模型 + 2 模型 replication，C1 跨架构一致。Limitations 诚实全面。[R1, R2 共识]\n\n**S6. 因果设计优于同期工作。** Matched-pair + perturbation control 的双重因果推理框架是方法论贡献。DRIP-R 差异化论述（3 点）清晰。[R2, R1 确认]\n\n---\n\n## Weaknesses\n\n### Critical (Must-Fix)\n\n**N1. TOST SESOI ±15 pp 缺乏外部锚定，two-tier structure 强烈依赖 margin 选择。** [R1 raised, R2 AGREE]\n- §4.6 的锚定理由（practical significance + perturbation CI upper bound）仅是作者自行设定的标准，存在逻辑跳跃。\n- ±10 pp 时仅 3/6 mid-tier pairs 等价，±12 pp 时 5/6，直到 ±15 pp 才 6/6。Mid-tier cluster 内部极差 ~11 pp，SESOI 大于此极差才形成 cluster——方法论循环。\n- \"Robust two-tier structure\"（Abstract, §5.2）的声称本质上取决于是否接受 ±15 pp 这一特定阈值。\n- **影响**：C2 (type hierarchy) 是论文三大贡献之一，two-tier 稳健性不成立则 Differential Nocuity 精细化程度大打折扣。\n- **建议**：提供外部锚定（如 Anvari & Lakens 2021 的 anchor-based methods）；承认 ±10–12 pp 时不稳健；补充 margin-free 方法（Bayesian estimation / bootstrap cluster analysis）。\n\n**N2. Authorization scope cross-judge κ=0.385 过低，无法支撑 C4 \"model-differentiating type\" 声称。** [R1 raised, R2 AGREE]\n- cross-judge κ=0.385 仅 \"fair\"，是六类中最低；human-LLM κ=0.644, CI=[0.35, 0.91] 下界仅 0.35。\n- κ=0.385 意味着约 38.5% judge agreement 超出 chance，52 pp 跨模型变异中真实 model difference vs. 测量噪声无法可靠区分。\n- Within-judge 控制仅消除 judge identity 混淆，不解决 per-instance inconsistency（R1 补充，R2 确认）。\n- **影响**：C4 是 \"safety training selectively mitigates boundary-type ambiguities\" 的核心依据。测量不可靠则建议链条断裂。\n- **建议**：C4 auth scope claims 降级为 \"suggestive/tentative\"；增加 bootstrap CI 量化测量不确定性对模型排名的影响；考虑增加人工标注样本量。\n\n**N3. Incompleteness confound 分析缺乏透明度，Abstract 措辞有误导风险。** [R1 raised, R2 AGREE with nuance]\n- Logistic regression 控制 token delta 后 \"coefficient change <8%, p=0.022\"——但未展示完整回归表（coefficients, SEs, model fit），读者无法评估回归质量。\n- Token count 是 information content 的粗糙代理，\"残余效应存在 ≠ 可量化歧义 vs. 信息比例\"（R2 精确区分 partial-out vs. decomposition）。\n- Abstract 将 incompleteness 列为 \"consistently high (46–62%)\" 但正文承认 \"upper bound partly reflecting confound\"——未分化。\n- R1 补充：排除 incompleteness 后五类 omnibus χ² p=0.079，type hierarchy 本身 borderline。\n- R2 nuance：coreferential（information delta=0）提供 confound-free lower bound（31.6%），确认纯歧义效应下界真实——问题是 incompleteness 在 hierarchy 中的确切位置不可信，非整体结论无效。\n- **建议**：展示完整回归表；Abstract/Conclusion 对 incompleteness 排名显式降级；探索更好的 information proxy 或 information-matched control。\n\n### Warning (Should-Fix)\n\n**W1. 缺少 API 超参数报告。** [R1 raised, R2 AGREE] §4.3 未报告 temperature, max_tokens, top_p，直接影响 reproducibility。\n\n**W2. ICC=0.919 仅在 OpenAI 模型族内测量。** [R1 raised, R2 AGREE] 跨 provider test-retest 未测量。方向一致性 ≠ reliability。\n\n**W3. Per-type human-LLM agreement CI 极宽。** [R1 raised, R2 AGREE] Scopal CI=[0.00, 1.00]（统计上无信息量），源于 per-type n=32–34。正文未讨论此限制。\n\n**W4. 无代码/数据可用性声明。** [R1 raised, R2 AGREE] 300 clause pairs、evaluation pipeline、analysis code 均未承诺发布。EMNLP 要求 reproducibility checklist。\n\n**W5. Clause-level heterogeneity 未充分分析。** [R1 raised, R2 partial AGREE] Clause identity 解释 22.4% variance，但未分析 outlier clauses 或 type 内 clause-level variance 分布。50 clauses/type + high variance → type-level 估计可能不稳定。建议 leave-one-out sensitivity。\n\n**W6. 人工标注者是否对 ambiguity condition 设盲未说明。** [R1 raised, R2 AGREE] §4.4 仅说 blind to LLM judge labels。\n\n**W7. Differential Nocuity 框架概念化不足。** [R2 raised, R1 partial AGREE] 三因素交互未形式化；\"channel availability\" 未直接测量（推断 ≠ 测量）；与 Berry & Kamsties (2004) 理论推进关系不清。建议用 prediction table 使框架可 falsifiable，或降级为观察性建议。\n\n**W8. C3 layer effect null result 讨论过于简短，abstract 未提及。** [R2 raised, R1 partial AGREE] §5.3 仅 3 句话。如 linguistic/specification 二分法不成立，two-layer taxonomy 的理论基础需重新论证。R1 指出 taxonomy 操作性价值独立于 layer 分组。建议补充讨论 + abstract 简要提及。\n\n**W9. 4 条 orphan bib 条目 + 遗漏引用。** [R1+R2 共识] Orphan: ferreira_patson_2007, levy_expectation_2008, lassiter_goodman_2017, poesio_artstein_2005。应引用 Zheng et al. (2024) LLM-as-a-Judge（与 §4.4 直接相关）和 Anvari & Lakens (2021)（如保留 TOST）。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致：\n\n1. **[AGREE] C1 (binary effect) 是论文最可靠的贡献**，统计支撑充分，7 模型 replication 增强效度。\n2. **[AGREE] Incompleteness confound 是最严重的方法论问题**，影响 type hierarchy (C2) 核心 claim 的可信度。\n3. **[AGREE] Authorization scope κ=0.385 过低**，C4 claims 应降级。\n4. **[AGREE] TOST SESOI ±15 pp 选择方法论循环**，two-tier structure 在更严格 margin 下不稳健。\n5. **[AGREE] 缺少 API 超参数、代码/数据声明、标注者 condition blinding 细节**。\n6. **[AGREE] 4 条 orphan bib 应清理**。\n7. **[AGREE] Overall 3.5 (Borderline Conference)**, Confidence 4/5 (High)。\n\n---\n\n## Reviewer Divergence\n\n分歧较小，均为非关键问题：\n\n1. **[REBUT by R1] Missing references 范围**：R2 建议引用 Constitutional AI (Bai et al., 2022)、AgentBench (Liu et al., 2023)、Bender & Koller (2020)。R1 反驳这些不在论文 scope 内——Constitutional AI 是 alignment 方法非 policy ambiguity，AgentBench 是通用能力 benchmark 非 safety violations，Bender & Koller 关联较远。论文已引用 5+ 个直接相关 agent safety benchmark。**决议**：这些不列为必要遗漏。\n\n2. **[REBUT by R1] Abstract 信息密度**：R2 认为数字过多应减至 2-3 核心发现。R1 认为对经验论文保留效应量合理，真正问题在 incompleteness confound caveat 不够显眼。**决议**：问题降级为 info，重点是修复 confound caveat 可见度。\n\n---\n\n## Questions\n\n**Q1** [R1+R2]: Incompleteness 的 unambiguous variant 平均添加了多少 token？Information delta 分布？完整 logistic regression 回归表（coefficients, SEs, model fit）？\n\n**Q2** [R1]: SESOI = ±15 pp 是否有外部文献或专家调研支持？±10 pp 时 type hierarchy 如何变化？\n\n**Q3** [R1+R2]: 能否提供 within-judge subgroup 的 authorization scope 专项 κ？Claude 12% auth scope violation rate 中的 failure mode 分布？\n\n**Q4** [R1]: Temperature 设置为多少？是否在 temperature > 0 下测试过 stability？\n\n**Q5** [R1+R2]: 300 clause pairs 和 evaluation code 是否计划公开？\n\n**Q6** [R2]: 是否考虑过 information-addition perturbation（添加无关信息不消歧）作为 incompleteness confound 的更直接控制？\n\n**Q7** [R2]: Template-based pipeline 的 template 设计是否公开？96% annotator pass rate 的 disagreement 是否集中在特定类型？\n\n---\n\n## Missing References\n\n**两人共识应引用**：\n- Zheng et al. (2024) \"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\" — 与 §4.4 LLM-as-judge 设计直接相关\n- Anvari & Lakens (2021) \"Using Anchor-Based Methods to Determine the Smallest Effect Size of Interest\" — 若保留 TOST 方法应引用\n\n**R1 单独建议**：\n- Kadavath et al. (2022) \"Language Models (Mostly) Know What They Know\" — 与 Ambiguity Blindness 相关（低优先级）\n\n**R2 建议但 R1 反驳（不列为必要）**：\n- Constitutional AI (Bai et al., 2022) — 不在论文 scope 内\n- AgentBench (Liu et al., 2023) — 通用能力 benchmark，非 safety\n- Bender & Koller (2020) — 关联较远\n\n**Orphan entries 需处理**：\n- ferreira_patson_2007, levy_expectation_2008, lassiter_goodman_2017, poesio_artstein_2005 — 引用或删除\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（2026-05-21T16:55 → 16:58，耗时 ~3 分钟）\n\n**Findings (2 warning, 7 info)**：\n\n⚠️ **Warning**:\n1. **Pages 3-5**: 连续 3 页纯文本（§3 Taxonomy → §4 Method → §5.1-5.2），无 display item 穿插。§3 六类 taxonomy 仅用文字描述，缺少结构化 taxonomy table/figure 作为视觉锚点。\n2. **Pages 1-8**: 主文仅 4 个 display items（1 figure + 1 table + 2 figures），低于实证论文典型密度（5-8 个）。建议增加 taxonomy 结构表/图或 matched-pair 示例表。\n\nℹ️ **Info**:\n- Figure 1 子面板内部文字偏小，打印后可能难辨认。\n- Table 1 列数较多，单栏宽度下略显拥挤。\n- Figure 2 per-type effect sizes 柱状图可读性良好。\n- Figure 3 heatmap 颜色梯度清晰，caption 自包含性好。\n- 附录 Tables 3-7 密集排列，Table 5 行间距偏紧。\n- 最后一页填充约 55-60%，底部大面积空白。\n- 未发现 LaTeX 渲染错误、未解析引用 [?]、margin 溢出等问题，排版基础质量良好。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n**Confidence: High (4/5)**\n**两位 Reviewer 独立评分一致。**\n\n**总评**：论文研究问题重要且及时，CL-first framing 对 EMNLP 有独特贡献，C1 (binary ambiguity effect, OR=15.1) 有充分统计支撑和七模型 replication。Matched-pair + perturbation control 的因果推理框架是方法论亮点。\n\n但从 C1 到 \"type-specific differential nocuity\"（C2+C4）的推理链有三个关键短板：(1) TOST SESOI ±15 pp 无外部锚定，two-tier structure 在 ±10 pp 时碎片化；(2) authorization scope 的 judge κ=0.385 无法可靠支撑 52 pp 跨模型变异的解读；(3) incompleteness confound 的 logistic regression 不够透明，且排除 incompleteness 后 omnibus p=0.079。这三个问题从独立角度挑战 C2 (type hierarchy)——论文标题所承诺的 \"Not All Policy Ambiguity Is Equal\" 在当前数据下支撑不够稳固。\n\n若能：(a) 为 SESOI 提供外部锚定或补充 margin-free 方法，(b) 将 auth scope C4 claims 降级为 tentative，(c) 展示完整回归表并在 Abstract 中标注 incompleteness confound，论文有从 3.5 提升至 4.0 (Conference) 的潜力。当前状态建议 **Findings** 或 **Borderline Conference**。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 信息密度高但对经验论文可接受（R1 观点）。核心问题是 incompleteness confound caveat 不够显眼——\"consistently high (46–62%)\" 与 \"upper bound partly reflecting confound\" 应在同一句中出现。\n- C3 null result 未提及（R1-M4, R2-W6 共识），abstract 给人 type-specific 结论全部成立的印象。\n\n### Introduction\n- 开头 retail 场景有效。Contribution (2) 中同时出现 confound 和 [exploratory] 标记可能给读者不确定感。\n- Contribution list 应更 prominently 标注 C3 inconclusive / C4 exploratory。\n\n### Related Work (§2)\n- Psycholinguistics 段论证链清晰。DRIP-R 差异化论述（3 点）有效。\n- 4 条 orphan bib 需清理。应引用 Zheng et al. (2024)。\n\n### Taxonomy (§3)\n- 六类型结构清晰有例子。\"Frequency in operational policy documents\" 作为选择标准未报告具体频率数据。\n- 缺少视觉 taxonomy table/figure 是版面缺陷（视觉审查也标记）。\n\n### Method (§4)\n- Cross-judge calibration 详尽是方法论强项。\n- **缺失**：API 超参数（§4.3）、标注者 condition blinding（§4.4）、SESOI 外部锚定（§4.6）。\n- Model selection 未解释为何无 7B/13B 规模模型。\n\n### Results (§5)\n- C1 效应量大且显著——最强发现。\n- C2 TOST 是方法论亮点但 margin 依赖性是核心弱点。\n- **C3 过于简短**（3 句话），layer 二分法失败对 taxonomy 理论基础的影响未讨论。\n- C4 heatmap 有效但 auth scope 结论需降级。\n\n### Error Analysis (§6)\n- 三种 failure pattern 有意义，已标 [Exploratory]。\n- Inter-coder κ=0.52 (moderate)，minority category κ=0.29，完全基于 LLM coders——系统性偏差无法被 κ 捕获。\n\n### Discussion (§7)\n- Differential Nocuity 三因素缺形式化，channel availability 是推断非测量。\n- Mitigation experiment across-model variance 未充分讨论。\n\n### Conclusion\n- 简洁但可能过于简短，未提 future work。\n\n### Format Compliance\n- ✅ 正文 8 页\n- ✅ Double-blind（\\usepackage[review]{acl}, Anonymous author）\n- ✅ Limitations 存在且适当\n- ❌ 无 Ethics Statement（建议添加）\n- ❌ 无代码/数据可用性声明"
  }
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-21T17:11:28.087333+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4070
}
```

</details>

---


### Assistant

_source line 696 · 2026-05-21T17:11:42.025137+00:00_

**审稿圆桌会议完成，报告已投递至 Research Director。**

**本轮审稿总结：**

| 维度 | 结果 |
|------|------|
| **Overall** | 3.5 (Borderline Conference) |
| **Confidence** | High (4/5) |
| **Reviewer 一致性** | 两人独立评分完全一致 |
| **交叉验证** | 所有 critical 问题达成 [AGREE]，无未解决 [REBUT] |

**3 个 Critical 问题**（均为两人共识）：
1. TOST SESOI ±15pp 无外部锚定，two-tier 结构在 ±10pp 碎片化
2. Authorization scope κ=0.385 无法支撑 C4 model-differentiating 声称
3. Incompleteness confound 回归不透明，排除后 omnibus p=0.079

**核心判断**：C1 (binary effect, OR=15.1) 稳固可靠，但 C2 (type hierarchy) 从三个独立方向受到挑战——论文标题 "Not All Policy Ambiguity Is Equal" 在当前形式下支撑不够稳固。修复 SESOI 锚定 + claim 降级 + 回归透明化后有提升至 Conference 的潜力。

Issue Tracker 已同步更新（3 critical / 9 warning / 4 info，全部 open）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 66

## Round 66

80 recorded events


### User

_source line 697 · 2026-05-21T17:36:22.262823+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May cycle
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 698 · 2026-05-21T17:36:29.501827+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-21T17:36:29.552778+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 700 · 2026-05-21T17:36:36.178258+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-21T17:36:36.178809+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-21T17:36:36.229308+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-21T17:36:36.229739+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 704 · 2026-05-21T17:36:45.066324+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 705 · 2026-05-21T17:36:45.167251+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (16 个)\n\n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_009**: PREPARING — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_009: Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.（准备中）\n\n## 近期结论\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C1 causal inference ← 基于 plan_010\n  [plan_014_extended_perturbation_results](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/data/results.json) | [plan_014_perturbation_clauses_extended](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/data/clauses_perturbation_extended.json) | [plan_014_run_script](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/intermediate/run_plan014.py)\n- **plan_015** (success): Authorization scope violations are predominantly unauthorized escalation (granting excess permissions) rather than restriction, consistent across all 5 models, revealing systematic permissiveness bias under boundary ambiguity\n- **plan_013** (success): Binary ambiguity effect (C1: Δ >= 20pp) and type hierarchy (C2: at least partial rank consistency) re
…[truncated 247 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-21T17:36:45.719518+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-21T17:36:45.770095+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'policy_ambiguity_safety'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-21T17:36:46.071648+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 709 · 2026-05-21T17:36:46.523752+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May cycle deadline author guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May cycle deadline author guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-21T17:36:47.176514+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 711 · 2026-05-21T17:36:47.227182+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 712 · 2026-05-21T17:36:52.698382+00:00_

Web search results for query: "ACL Rolling Review 2026 May cycle deadline author guidelines page limit"

Links: [{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's the information about the ACL Rolling Review 2026 May cycle:

## Page Limits

The paper follows page limits (8 for long, 4 for short, not including limitations and ethical considerations).

## Author Guidelines

The ACL Rolling Review has comprehensive author guidelines available at their website. Key points include:

- All authors must sign up as reviewers with assignments made based on qualifications, and reviewers who fail to fulfill their responsibilities may become ineligible to commit or (re-)submit papers in the following ARR cycle.

- After each submission deadline, all authors must complete the auth
…[truncated 612 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 6174
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-21T17:36:54.807715+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"}]

I've completed the web search for EMNLP 2026 call for papers and ARR submission guidelines
…[truncated 1187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 8736
}
```

</details>

---


### Tool call

_source line 714 · 2026-05-21T17:37:00.498352+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the complete submission guidelines for ARR 2026: page limits (long/short), formatting template, anonymity rules, appendix rules, citation format, May 2026 cycle deadline, and any other submission requirements. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract the complete submission guidelines for ARR 2026: page limits (long/short), formatting template, anonymity rules, appendix rules, citation format, May 2026 cycle deadline, and any other submission requirements. Be thorough."
  }
}
```

</details>

---


### Tool call

_source line 715 · 2026-05-21T17:37:02.010500+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.aclweb.org/calls/main_conference_papers/",
  "prompt": "Extract EMNLP 2026 or ACL 2026 submission guidelines: page limits, venue-specific requirements, commitment deadlines, review criteria, and any details about how ARR papers are committed to venues."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.aclweb.org/calls/main_conference_papers/",
    "prompt": "Extract EMNLP 2026 or ACL 2026 submission guidelines: page limits, venue-specific requirements, commitment deadlines, review criteria, and any details about how ARR papers are committed to venues."
  }
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-21T17:37:02.866199+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "decisions.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "decisions.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool call

_source line 717 · 2026-05-21T17:37:03.569227+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 718 · 2026-05-21T17:37:06.080221+00:00_

# ACL 2026 Submission Guidelines

## Page Limits
- **Long Papers:** 8 pages (final accepted versions receive 1 additional page, up to 9 pages)
- **Short Papers:** 4 pages (final accepted versions receive 1 additional page, up to 5 pages)

## Key Venue-Specific Requirements
Papers must adhere to "ARR submission requirements" including instructions for anonymized review, authorship policies, citation standards, ethics policies with a "responsible NLP research checklist," and limitations sections. Supplementary materials are optional.

## Commitment Deadlines
- **Submission to ARR:** January 5, 2026
- **Commitment to ACL 2026:** March 14, 2026
- **Acceptance Notification:** April 4, 2026
- **Camera-ready Due:** April 19, 2026

## Review Process
The conference uses ACL Rolling Review (ARR) where papers receive reviews and meta-reviews from ARR reviewers and area chairs. Senior Area Chairs and Program Chairs then make final acceptance decisions based on ARR feedback. The process maintains double-blind review standards.

## Special Requirements
All submitting authors must complete registration by January 7, 2026. Reviewers must submit reviews by February 7 and meta-reviews by March 3. "Papers without at least one presenting author registered by the early registration deadline may be subject to desk rejection."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebFetch",
  "elapsed_ms": 4069
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-21T17:37:09.995345+00:00_

# ARR 2026 Submission Guidelines Summary

## Page Limits

**Long Papers:** Up to 8 pages of content, plus unlimited space for required limitations section and optional ethical considerations, plus unlimited references.

**Short Papers:** Up to 4 pages of content, plus unlimited space for limitations and optional ethical considerations, plus unlimited references.

Both types require a dedicated "Limitations" section; submissions lacking this will be desk rejected.

## Formatting Requirements

Submissions must use "the official ACL style template" available on GitHub (acl-org/acl-style-files). Authors cannot modify style files or use templates from other conferences. Papers must conform to ACL formatting guidelines regarding page size, margins, and font sizes, or face rejection without review.

## Anonymity Rules

Papers must not include author names, affiliations, or self-identifying citations like "We previously showed (Smith, 1991)." Instead, use third-person construction: "Smith previously showed (Smith, 1991)." All supplementary materials, including repository links, must be anonymized. Dropbox and similar download-tracking services are prohibited. Violations result in desk rejection.

## Appendix Rules

Appendices follow main paper content and references, don't count toward page limits, and must be fully anonymized. They should use double-column formatting (with limited exceptions per ACLPUB guidelines). Reviewers aren't required to review appendices—critical material should appear in the main paper.

## Citation Format for Concurrent Submissions

For concurrently submitted related papers by overlapping author groups, use: "Anonymous (2026). Paper title. Under review."

## May 2026 Cycle Details

The document doesn't specify a May 2026 deadline, but describes a rolling submission system with "deadlines every two months." Author registration forms are due within 48 hours after submission deadlines.

## Additional Key Requirements

- **Responsible NLP Checklist:**
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebFetch",
  "elapsed_ms": 9496
}
```

</details>

---


### Tool result

_source line 720 · 2026-05-21T17:37:09.996087+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/decisions.yaml\", \"content\": \"_next_id: 26\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 07:11 UTC\\n  summary: MVP 设计：3 类歧义 × 2 API 模型验证 type effect，不用 GPU\\n  rationale: 核心假设是\\\"歧义类型影响安全违规率\\\"。选 scopal/lexical/incompleteness 3 种假设差异最大的类型，用 frontier\\n    API 模型（免 GPU）快速验证信号存在性。60 条款 × 2 variants × 2 模型 = 240 runs，统计功效足够（χ² df=2, medium\\n    effect w=0.3, N=240 >> 所需 ~107）。Pass 条件：p<0.05 + V≥0.15。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 07:15 UTC\\n  summary: 采纳 Reviewer 3 条修正：增条款数、调阈值、补 fail path\\n  rationale: 'Reviewer WARNING: (1) pairwise N=80 对 V=0.15 功效仅 0.22，增至 30 条款/类（pairwise\\n    N=120）+ 提阈值至 V≥0.20 + 明确 MVP 只检测 medium+ effect；(2) 补 fail path 三级决策树（扩大N重测 →\\n    pivot binary story → full study）；(3) 加 judge 偏差检查点（scopal 低于预期时先排查 judge bias）。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 07:16 UTC\\n  summary: ROADMAP 补充 H1-H4 预测基准和 post-MVP 18 周路径骨架\\n  rationale: 'Reviewer WARNING: (1) ROADMAP 缺 post-MVP 骨架，ICLR DDL 18 周后，需提前规划 GPU\\n    申请时间点（W3 MVP pass 后立即申请，W5 开始 Phase 2b）；(2) H1-H4 方向性预测未落地到 ROADMAP，Agent 解读 MVP\\n    结果时需对照基准（H1: scopal 最高，H2: lexical 最低，null: binary effect story）。paper_framing.md\\n    保持在 MVP 后创建。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-20 07:23 UTC\\n  summary: MVP 分析改为双轨：ambiguous-only 跨类型比较（主）+ matched-pair within-type（辅）\\n  rationale: 'Reviewer WARNING: incompleteness matched pair 存在信息量不对称混淆——消歧必然添加信息，与\\n    scopal/lexical 的\\\"同信息不同措辞\\\"baseline 不可比。解法：(1) 主分析用 ambiguous-only 条件直接跨类型比较违规率（不受信息量混淆）；(2)\\n    matched-pair 降为辅助的 within-type 效应量度量；(3) 要求 Agent 修订 incompleteness pairs 只添加解决歧义的最小信息；(4)\\n    效度边界显式声明此不对称性。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-20 07:24 UTC\\n  summary: MVP 使用 τ²-
…[truncated 3545 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7129
}
```

</details>

---


### Tool result

_source line 721 · 2026-05-21T17:37:10.147085+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 6577
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-21T17:37:15.617289+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-21T17:37:16.119475+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-21T17:37:16.119923+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 Budapest October call for papers commitment deadline ARR cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 Budapest October call for papers commitment deadline ARR cycle"
  }
}
```

</details>

---


### Tool call

_source line 725 · 2026-05-21T17:37:16.521575+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review May 2026 submission deadline dates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review May 2026 submission deadline dates"
  }
}
```

</details>

---


### Tool result

_source line 726 · 2026-05-21T17:37:20.987921+00:00_

Web search results for query: "ACL Rolling Review May 2026 submission deadline dates"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here are the ACL Rolling Review May 2026 submission deadline dates:

ACL Rolling Review switched to 10-week review cycles starting in May 2025, which means the May 2026 cycle follows this new schedule.

Unfortunately, the search results don't contain specific May 2026 submission deadline dates. However, the submission deadline is always the 15th of the month according to ARR's standard practice. This would suggest the May 2026 ARR deadline would be May 15, 2026, though this should be confirmed on the official ACL R
…[truncated 213 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 4466
}
```

</details>

---


### Tool result

_source line 727 · 2026-05-21T17:37:23.348402+00:00_

Web search results for query: "EMNLP 2026 Budapest October call for papers commitment deadline ARR cycle"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"LINGUIST List 37.1616 Confs: Workshop at EMNLP 2026: Multimodal Interaction in Face-to-Face Dialogue (Hungary)","url":"https://linguistlist.org/issues/37/1616/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here is the information about EMNLP 2026 in Budapest regarding the call for papers, ARR cycles, and commitment deadlines:

## Conference Details
EMNLP 2026 is being held in Budapest, Hungary on October 24 - 29, 2026.

## Submission and Commitment Deadlines
The ARR submission deadline for long and short papers is May 25, 2026, with the EMNLP commitment deadline on August 2, 2026. All deadlines are 11:59PM UTC-12:0
…[truncated 964 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 7228
}
```

</details>

---


### Tool call

_source line 728 · 2026-05-21T17:37:28.519541+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract ALL submission details: ARR submission deadline (May cycle), commitment deadline, page limits, formatting requirements, anonymity rules, appendix rules, and any other submission guidelines. Be thorough and precise with dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract ALL submission details: ARR submission deadline (May cycle), commitment deadline, page limits, formatting requirements, anonymity rules, appendix rules, and any other submission guidelines. Be thorough and precise with dates."
  }
}
```

</details>

---


### Tool call

_source line 729 · 2026-05-21T17:37:29.122080+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "Extract all dates for the May 2026 ARR cycle: submission deadline, review deadline, meta-review deadline, author response period, commitment deadline. List all 2026 cycles and their dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/dates",
    "prompt": "Extract all dates for the May 2026 ARR cycle: submission deadline, review deadline, meta-review deadline, author response period, commitment deadline. List all 2026 cycles and their dates."
  }
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-21T17:37:31.282339+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -path \"*/policy_ambiguity_safety/*config*\" -type f 2>/dev/null; find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -name \"project_configs.yaml\" -type f 2>/dev/null; find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -path \"*/config*\" -name \"*.yaml\" -type f 2>/dev/null | head -10",
  "description": "Find config files for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -path \"*/policy_ambiguity_safety/*config*\" -type f 2>/dev/null; find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -name \"project_configs.yaml\" -type f 2>/dev/null; find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -path \"*/config*\" -name \"*.yaml\" -type f 2>/dev/null | head -10",
    "description": "Find config files for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 731 · 2026-05-21T17:37:31.635646+00:00_

&lt;persisted-output>
Output too large (41.9KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0519-4-projects-policy-ambiguity-safety--claude-sessions-review-director-0e80b40a/a9f4635a-7da9-40f9-9182-b40341bb0b0a/tool-results/b9xn4zrqc.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/bin/numpy-config
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/openai/types/realtime/realtime_tool_choice_config.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/openai/types/realtime/realtime_audio_config_input.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/openai/types/realtime/realtime_tools_config_union_param.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/openai/types/realtime/__pycache__/realtime_tracing_config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/openai/types/realtime/__pycache__/realtime_tracing_config_param.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/openai/types/realtime/__pycache__/realtime_tools_config_union.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/openai/types/realtime/__pycache__/realtime_audio_config_param.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.venv/lib/python3.14/site-packages/openai/types/realtime/__pycache__/realtime_tool_choice_config_param.cpython-314.pyc
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/po
…[truncated 164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 353
}
```

</details>

---


### Tool result

_source line 732 · 2026-05-21T17:37:32.740065+00:00_

# May 2026 ARR Cycle Dates

Based on the reviewing schedule table provided:

- **Submission deadline:** May 25, 2026
- **Reviewer registration deadline:** May 27, 2026
- **Review submission deadline:** June 29, 2026
- **Author response period:** July 7-July 13, 2026
- **Meta-review release date:** July 30, 2026
- **Cycle end:** August 2, 2026
- **Commitment deadline (for EMNLP 2026 and AACL 2026):** August 2, 2026

# All 2026 ARR Cycles

The document lists three complete cycles scheduled for 2026:

1. **March 2026:** Submission March 16 through cycle end May 24
2. **May 2026:** Submission May 25 through cycle end August 2
3. **August 2026:** Submission August 3 with "cycle end October 11"
4. **October 2026:** Submission October 12 with "cycle end December 20"

The August and October cycles show limited detail, as several dates are marked "TBA" (to be announced).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebFetch",
  "elapsed_ms": 3617
}
```

</details>

---


### Tool result

_source line 733 · 2026-05-21T17:37:33.343031+00:00_

# EMNLP 2026 Submission Details

## Key Deadlines
- **ARR Submission Deadline:** May 25, 2026 (11:59 PM UTC-12:00)
- **Reviewer Registration:** May 27, 2026
- **Commitment Deadline:** August 2, 2026
- **Camera-Ready Due:** September 20, 2026

## Page Limits
- **Long Papers:** 8 pages (9 pages for final accepted versions)
- **Short Papers:** 4 pages (5 pages for final accepted versions)

## Core Requirements

**Anonymity:** "Following the ACL and ARR policies, there is no anonymity period requirement," though the review process itself remains double-blind.

**Author List:** Modification during commitment is prohibited, but author order changes are permitted.

**Formatting & Standards:** All submissions must comply with ARR submission requirements, including citation standards, authorship guidelines, and ethics policies outlined in the ACL Publication Ethics Policy.

**Supplementary Materials:** Optional appendices, software, and data are permitted per ARR guidelines.

**Writing Assistance:** AI-powered writing tools are permitted; however, entirely AI-generated papers are prohibited.

## Mandatory Reviewer Participation
All authors must register and participate in peer review. Failure to complete assigned reviews by the deadline may result in ineligibility for future submissions.

## Conference Presentation
"All accepted papers must be presented at the conference to appear in the proceedings." Virtual attendance options are available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebFetch",
  "elapsed_ms": 4823
}
```

</details>

---


### Tool call

_source line 734 · 2026-05-21T17:37:37.763369+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -maxdepth 3 -name \"*.yaml\" -path \"*/policy_ambiguity_safety/*\" -not -path \"*/.venv/*\" -not -path \"*/artifacts/*\" 2>/dev/null",
  "description": "Find YAML config files in project (excluding venv)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -maxdepth 3 -name \"*.yaml\" -path \"*/policy_ambiguity_safety/*\" -not -path \"*/.venv/*\" -not -path \"*/artifacts/*\" 2>/dev/null",
    "description": "Find YAML config files in project (excluding venv)"
  }
}
```

</details>

---


### Tool result

_source line 735 · 2026-05-21T17:37:37.813962+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/dream_registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/writing_plan.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/literature_map.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/mistakes.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/decisions.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 736 · 2026-05-21T17:37:41.028829+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -maxdepth 2 -name \"*.yaml\" -not -path \"*/projects/*\" -not -path \"*/.venv/*\" 2>/dev/null",
  "description": "Find top-level config YAML files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -maxdepth 2 -name \"*.yaml\" -not -path \"*/projects/*\" -not -path \"*/.venv/*\" 2>/dev/null",
    "description": "Find top-level config YAML files"
  }
}
```

</details>

---


### Tool result

_source line 737 · 2026-05-21T17:37:41.129682+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/global/approvals.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/approvals.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/backend.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/feishu.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/resources.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 738 · 2026-05-21T17:37:44.694082+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/workspace.yaml 2>/dev/null | head -50",
  "description": "Read workspace config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/workspace.yaml 2>/dev/null | head -50",
    "description": "Read workspace config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 739 · 2026-05-21T17:37:45.648588+00:00_

projects: {}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 740 · 2026-05-21T17:37:45.648966+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/ 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/workspace.yaml 2>/dev/null",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/ 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/workspace.yaml 2>/dev/null",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-21T17:37:45.699331+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 742 · 2026-05-21T17:37:52.727349+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/ 2>/dev/null",
  "description": "List paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/ 2>/dev/null",
    "description": "List paper sections"
  }
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-21T17:37:53.631333+00:00_

abstract.tex
analysis.tex
appendix.tex
conclusion.tex
discussion.tex
experiments.tex
introduction.tex
limitations.tex
method.tex
related_work.tex
taxonomy.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 744 · 2026-05-21T17:37:53.631802+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Read existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Read existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 745 · 2026-05-21T17:37:53.682625+00:00_

## Round 8 (Fresh) Review Issues — policy_ambiguity_safety
## Paper: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
## Venue: EMNLP 2026 via ARR May cycle
## Date: 2026-05-21
## Round 8 Score: 3.5 (Borderline Conference)
## Note: Fresh review session — all issues re-evaluated from scratch

# ============================================================
# CRITICAL ISSUES
# ============================================================

- id: "R8-N1"
  summary: "TOST SESOI ±15pp 缺乏外部锚定，two-tier structure 在 ±10-12pp 时不稳健"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 8
  last_seen_round: 8
  mentions:
    - round: 8
      reviewers: [R1, R2]
      note: "R1 raised as N1, R2 AGREE. Mid-tier cluster 内部极差 ~11pp, ±15pp 恰好让所有 mid-tier pairs 等价——方法论循环。±10pp 时仅 3/6 等价, two-tier 结构碎片化。perturbation CI upper bound 作为锚定存在逻辑跳跃。"
  action_items:
    - round: 8
      action: "提供 SESOI 外部锚定（领域文献/专家调研）；承认 ±10-12pp 时不稳健；考虑 margin-free 补充方法（Bayesian estimation / bootstrap cluster analysis）；引用 Anvari & Lakens (2021)"
      assigned_to: author
      status: in_progress
    - round: 9
      action: "已完成: (1) §4.6 添加 domain-relevant anchor 语言 + Anvari & Lakens 2021 引用; (2) 明确承认 margin dependence (3/6 at ±10pp); (3) 添加 Ward's bootstrap cluster analysis (B=10000) 作为 margin-free 补充; (4) C2 section 添加 bootstrap cluster 结果; (5) 去掉 'robust two-tier' 改为 'two-tier'; (6) 新增 Appendix H (Bootstrap Cluster Analysis)"
      assigned_to: author
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R8-N2"
  summary: "Authorization scope cross-judge κ=0.385 过低，无法支撑 C4 'model-differentiating type' 声称"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 8
  last_seen_round: 8
  mentions:
    - round: 8
      reviewers: [R1, R2]
      note: "R1-N2, R2-W2 独立提出. κ=0.385 仅 fair; human-LLM κ=0.644 CI=[0.35,0.91] 下界极低; within-judge 控制只解决 judge identity 混淆，无法控制 per-instance inconsistency; 52pp 跨模
…[truncated 10736 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 746 · 2026-05-21T17:38:01.974621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-21T17:38:02.527092+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type, two-layer ambiguity taxonomy, evaluated across five architecturally diverse models (2,997 episodes). Ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. A significant type hierarchy emerges (Cram\'{e}r's $V = 0.137$, $p < 10^{-4}$), with a two-tier structure among five types and incompleteness as an upper bound whose ranking partly reflects an information-addition confound (logistic regression controlling for information delta: $p = 0.022$, coefficient change $< 8\%$). The specification--linguistic layer distinction is inconclusive ($p = 0.017$, not surviving correction). The hierarchy replicates on two additional model families (LLaMA $\rho = 0.90$, $p = 0.037$; Gemini $\rho = 0.60$, directionally consistent): incompleteness is consistently high (46--62\% across seven models), while authorization scope varies 52 pp depending on the model (12\% for Claude to 64\% for GPT-5.4, though this type carries the widest measurement uncertainty, $\kappa = 0.385$), suggesting that safety training may differentially mitigate specific ambiguity types. Agents show fewer than 11\% disambiguation awareness. Our Differential Nocuity framework connects type-specific vulnerability to disambiguation channel availability and suggests both type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-21T17:38:02.527567+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 749 · 2026-05-21T17:38:02.979570+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
13	\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-
…[truncated 2017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 750 · 2026-05-21T17:38:03.030231+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 751 · 2026-05-21T17:38:03.432269+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit analogous garden-path effects. \citet{liu_ambiguity_2023} demonstrate that language models fail to represent ambiguity, collapsing multiple interpretations into a single output. These findings
…[truncated 2210 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 752 · 2026-05-21T17:38:03.432644+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-21T17:38:03.483123+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers, drawing on \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types), \citet{massey_ambiguity_re_2014}'s requirements engineering taxonomy (6 types), and the concurrent DRIP-R benchmark \citep{drip_r_2026} (5 types). We select types based on two criteria: frequency in operational policy documents (assessed via manual audit of $\tau^2$-bench policies) and theoretical distinctiveness (each type maps to a different resolution mechanism).
7	
8	\paragraph{Linguistic layer.} These types operate at the syntactic or semantic level and can, in principle, be resolved by parsing or contextual cues within the text.
9	\begin{itemize}
10	\item \textbf{Scopal}: quantifier, negation, or modal scope interactions (e.g., ``all items may not be returned'' admits universal-negation and negation-of-universal readings).
11	\item \textbf{Lexical}: polysemy or homonymy (e.g., ``charge'' as financial cost vs.\ penalty; ``party'' as individual vs.\ group).
12	\item \textbf{Coreferential}: unclear pronoun or noun-phrase reference (e.g., ``the agent should verify the customer's identity before processing their refund request, which must be approved by a supervisor'' where ``which'' could refer to the verification or the refund).
13	\end{itemize}
14	
15	\paragraph{Specification layer.} These types arise from pragmatic or discourse-level gaps that require domain knowledge or organizational context to resolve.
16	\begin{itemize}
17	\item \textbf{Authorization scope}: vague permission or role boundaries (e.g., ``authorized personnel may issue r
…[truncated 1121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-21T17:38:06.544737+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-21T17:38:06.997026+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% pass rate; disagreements were resolved by discussion. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We evaluate five models spanning four providers and two architecture families: GPT-5.4 and GPT-4.1 (OpenAI, pro
…[truncated 4803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-21T17:38:06.997445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 757 · 2026-05-21T17:38:07.449631+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type hierarchy (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). Clause identity explains 22.4\% of variance versus 1.0\% for model identity. A replication on two additional model families (Gemini-2.5-Flash, LLaMA-4-Scout; Appendix~\ref{app:model_expansion}) confirms the effect across seven models spanning six providers ($\Delta = +20.0$ to $+33.6$\,pp, both $p < 10^{-6}$).
9	
10	\subsection{Type Hierarchy (C2)}
11	
12	\begin{table*}[t]
13	\centering
14	\caption{Violation rates (\%) under ambiguous policy clauses by type and model. $\Delta$pp denotes the pooled difference between ambiguous and unambiguous conditions across all five models. All per-type differences are significant ($p < 10^{-5}$, Fisher's exact test).}
15	\label{tab:main_results}
16	\small
17	\begin{tabular}{llrrrrrrrr}
18	\toprule
19	Layer & Type & Pooled & GPT-5.4 & GPT-4.1 & Claude & Qwen3 & DeepSeek & $\Delta$pp & $p$ \\
20	\midrule
21	\multirow{3}{*}{\textcolor{speccolor}{Spec.}} & Incompleteness & 53.6 & 46.0 & 58.0 & 48.0 & 62.0 & 54.0 & +49.2 & $<10^{-37}$ \\
22	 & Auth.\ Scope & 41.6 & 64.0 & 46.0 & 12.0 & 26.0 & 60.0 & +36.0 & $<10^{-22}$ \\
23	 & Cond.\ Precedence 
…[truncated 5959 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-21T17:38:07.450098+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-21T17:38:08.002521+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes: unauthorized escalation, assumption-based action, scope misapplication, arbitrary rule selection, and conservative refusal. GPT-5.4 and GPT-4.1 serve as detailed annotation anchors because they span the judge boundary. Inter-coder reliability is substantial (Gwet's AC$_1$ $= 0.62$ \citep{gwet_2014}; Cohen's $\kappa = 0.52$ \citep{cohen_1960}; the gap reflects the prevalence paradox, as three categories account for ${\sim}$90\% of instances).
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse} (scope misapplication): the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002}---e.g., parsing ``items purchased with a coupon or during a sale are final'' as restricting only coupon purchases. This dominates scopal (all 5 models), conditional precedence (all 5), and coreferential (3/5).
13	
14	\emph{Information gap-filling} (assumption-based action): the agent fills missing information with plausible but incorrect defaults---e.g., inventing a 30-day return window when none is specified. This dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation} (unauthorized escalation): the agent exceeds permission boundaries when authorization scope is underspecified---e.g., issuing a refund above its stated limit rather than escalating; 69.2\% of such violations involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial test), revealing systematic permis
…[truncated 1696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 760 · 2026-05-21T17:38:08.003007+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 761 · 2026-05-21T17:38:08.053493+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential Nocuity.}
5	\citet{berry_kamsties_2004} distinguish nocuous from innocuous ambiguity by stakeholder divergence. Our results extend this to LLM agents: all six types are nocuous ($+34.0$ pp), but type primarily determines severity (22:1 clause-vs.-model variance ratio). We propose \emph{Differential Nocuity}: the risk of a policy ambiguity depends on three factors---ambiguity type (base vulnerability), safety training (selective mitigation of boundary-type ambiguities), and disambiguation channel availability (recovery possibility). This generates two testable predictions: (P1) types with explicit decision points (e.g., authorization scope) should show larger safety-training gains than implicit gap-filling types (e.g., incompleteness); (P2) disambiguation channels should reduce violations more for high-blindness types. Our mitigation experiment (Appendix~\ref{app:mitigation}) supports P1: $-18.0$\,pp for authorization scope vs.\ $-3.4$\,pp for incompleteness. Systematic nocuity---41.3\% of clauses trigger majority-convergent violations (\S\ref{sec:analysis})---makes such errors invisible in agreement-based evaluation.
6	
7	\paragraph{Practical implications.}
8	The C4 interaction provides suggestive evidence that incompleteness bypasses intervention points via gap-filling \citep{ferreira_good_enough_2002}, while authorization scope varies 48\,pp within a single judge (\S\ref{sec:c4}), consistent with boundary-targeted training. A proof-of-concept classifier (Appendix~\ref{app:detection}) achieves F1\,=\,0.81 for binary detection but only 0.34 for incompleteness. With $<$11\% agent self-awareness (\S\ref{sec:analysis}), type-aware auditing and externalized detection tools \citep{chantree_2006,ferrari_ambiguity_2019} remain necessary for policy-governed deployments.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 762 · 2026-05-21T17:38:13.022496+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-21T17:38:13.374253+00:00_

1	\section{Conclusion}
2	
3	Ambiguous policy clauses increase agent safety violations by 34.0\,pp (OR\,$=$\,15.1) across five models, with clause identity explaining 22$\times$ more variance than model identity. The two-tier type hierarchy replicates across seven models ($\rho = 0.60$--$0.90$). With $<$11\% disambiguation awareness, type-aware auditing and externalized detection are critical for policy-governed deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-21T17:38:13.374808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 765 · 2026-05-21T17:38:13.877179+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Model coverage.} We evaluate seven API-accessible models from six providers (four proprietary, three open-source; two in replication, Appendix~\ref{app:model_expansion}). Smaller open-source models (7B--70B parameters) may show different vulnerability patterns, and our findings may not generalize to models with fundamentally different training approaches.
5	
6	\paragraph{Domain scope.} $\tau^2$-bench covers retail and airline customer service. Policy ambiguity effects in other domains (healthcare, finance, legal) remain to be tested, though the within-study cross-domain consistency is encouraging: failure mode distributions share the same top-two modes (assumption-based action and unauthorized escalation) across domains, with individual mode base rates differing by up to 12.5 pp, likely reflecting domain policy structure rather than methodological artifacts.
7	
8	\paragraph{Synthetic ambiguity.} Our matched-pair design requires synthetic construction of ambiguous variants, which may not capture the full distribution of naturally occurring policy ambiguities. We mitigate this through expert review and a realism validation comparing ambiguous clauses against original $\tau^2$-bench policy text. Ambiguous clauses are indistinguishable from originals in lexical diversity (TTR, KS $p = 0.89$) and word length ($p = 0.09$). Readability is slightly higher (Flesch--Kincaid $d = 0.29$, $p = 0.006$) and sentence length moderately higher ($d = 0.74$), both reflecting the structural demands of encoding ambiguity in standalone clauses. Across matched pairs, disambiguation preserves readability (Flesch--Kincaid $d = 0.14$, $p = 0.10$), confirming that minimal edits change semantic precision without altering linguistic register.
9	
10	\paragraph{Cross-judge asymmetry.} Although our dual-judge calibration (\S\ref{sec:method}) shows no systematic bias ($p = 0.606$) and human validation confirms the LLM judge operates 
…[truncated 2739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 766 · 2026-05-21T17:38:13.877675+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 767 · 2026-05-21T17:38:14.329933+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). The treatment appends a type-specific disambiguation instruction to the agent's system prompt. Control rates are the matched 5-type subset from the full study (\S\ref{sec:results}).
30	
31	\begin{table*}[!ht]
32	\centering
33	\small
34	\caption{Violation rate change ($\Delta$pp) after adding type-specific disambiguation instructions. Negative values indicate reduction. Baseline violation rates are shown in parentheses. Coreferential was 
…[truncated 14206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 768 · 2026-05-21T17:38:14.681629+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 769 · 2026-05-21T17:38:14.882898+00:00_

1	@inproceedings{li_ambiguity_taxonomy_2024,
2	  title={A Taxonomy of Ambiguity Types for {NLP}},
3	  author={Li, Margaret Y. and Liu, Alisa and Wu, Zhaofeng and Smith, Noah A.},
4	  booktitle={Proceedings of EACL 2024},
5	  year={2024}
6	}
7	
8	@inproceedings{massey_ambiguity_re_2014,
9	  title={Identifying and Classifying Ambiguity for Regulatory Requirements},
10	  author={Massey, Aaron K. and Rutledge, Richard L. and Ant{\'o}n, Annie I. and Swire, Peter P.},
11	  booktitle={22nd IEEE International Requirements Engineering Conference (RE)},
12	  year={2014},
13	  doi={10.1109/RE.2014.6912250}
14	}
15	
16	@techreport{berry_kamsties_2004,
17	  title={From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity --- A Handbook},
18	  author={Berry, Daniel M. and Kamsties, Erik and Krieger, Michael M.},
19	  institution={University of Waterloo},
20	  year={2004}
21	}
22	
23	@inproceedings{chantree_2006,
24	  title={Identifying Nocuous Ambiguities in Natural Language Requirements},
25	  author={Chantree, Francis and Nuseibeh, Bashar and de Roeck, Anne and Willis, Alistair},
26	  booktitle={14th IEEE International Requirements Engineering Conference (RE)},
27	  year={2006}
28	}
29	
30	@incollection{wasow_ambiguity_2005,
31	  title={The Puzzle of Ambiguity},
32	  author={Wasow, Thomas and Perfors, Amy and Beaver, David},
33	  booktitle={Morphology and the Web of Grammar: Essays in Memory of Steven G. Lapointe},
34	  publisher={CSLI Publications},
35	  year={2005}
36	}
37	
38	@article{kennedy_vagueness_2007,
39	  title={Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives},
40	  author={Kennedy, Christopher},
41	  journal={Linguistics and Philosophy},
42	  volume={30},
43	  number={1},
44	  pages={1--45},
45	  year={2007},
46	  doi={10.1007/s10988-006-9008-0}
47	}
48	
49	@article{willis_nocuous_2008,
50	  title={Automatic Identification of Nocuous Ambiguity},
51	  author={Willis, Alistair and Chantree, Francis and De Roeck
…[truncated 1993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 770 · 2026-05-21T17:38:42.487454+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-21T17:38:59.819835+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 17332
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-21T17:39:00.825045+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验有效性**。\n\n## 论文信息\n- 标题: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n- 路径: projects/policy_ambiguity_safety/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf\n- 目标 venue: EMNLP 2026 via ARR May cycle (deadline: 2026-05-25)\n\n## Venue 格式要求\n- Long paper: 正文 ≤ 8 页, 参考文献不限, Limitations 必须有（不计入页数）\n- ACL 官方模板, double-blind\n- 附录不计入页数, reviewer 不强制阅读\n\n## 你的审查侧重\n请重点审查以下方面：\n\n1. **实验设计**：matched-pair design 的因果推断有效性，300 clause pairs × 5 models = 2,997 episodes 的统计功效是否充分，perturbation control 是否有效排除混淆因素\n2. **统计分析**：McNemar's test / χ² / Cramér's V / TOST equivalence testing 的选择和使用是否恰当，SESOI ±15pp 的锚定是否有外部依据，多重比较校正是否充分\n3. **评估管道**：cross-judge design 的偏差控制（GPT-5.4 judges Claude/Qwen3/DeepSeek, GPT-4.1 judges GPT-5.4），per-type κ 变异大（authorization scope κ=0.385 vs incompleteness κ=0.875），human validation 是否充分\n4. **Confound 控制**：incompleteness 的 information-addition confound 是否被充分控制（logistic regression p=0.022, coefficient change <8%），token count 作为 information content proxy 的有效性\n5. **Reproducibility**：ICC=0.919 仅 within OpenAI family，cross-provider stability 是否有直接证据；API 超参数是否完整报告；replication on 2 additional models 的样本量是否充分\n6. **Claims 与 evidence 的匹配度**：C1-C4 四个 claims 是否都有充分支撑，特别是 C3（inconclusive）和 C4（exploratory）的定位是否恰当\n\n请按 ARR 审稿标准输出完整审稿意见，包含 Summary / Strengths / Weaknesses / Questions / Missing References / Overall Assessment。Weaknesses 按严重程度标注 [MUST-FIX] / [SHOULD-FIX] / [MINOR]。",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验有效性**。\n\n## 论文信息\n- 标题: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n- 路径: projects/policy_ambiguity_safety/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf\n- 目标 venue: EMNLP 2026 via ARR May cycle (deadline: 2026-05-25)\n\n## Venue 格式要求\n- Long paper: 正文 ≤ 8 页, 参考文献不限, Limitations 必须有（不计入页数）\n- ACL 官方模板, double-blind\n- 附录不计入页数, reviewer 不强制阅读\n\n## 你的审查侧重\n请重点审查以下方面：\n\n1. **实验设计**：matched-pair design 的因果推断有效性，300 clause pairs × 5 models = 2,997 episodes 的统计功效是否充分，perturbation control 是否有效排除混淆因素\n2. **统计分析**：McNemar's test / χ² / Cramér's V / TOST equivalence testing 的选择和使用是否恰当，SESOI ±15pp 的锚定是否有外部依据，多重比较校正是否充分\n3. **评估管道**：cross-judge design 的偏差控制（GPT-5.4 judges Claude/Qwen3/DeepSeek, GPT-4.1 judges GPT-5.4），per-type κ 变异大（authorization scope κ=0.385 vs incompleteness κ=0.875），human validation 是否充分\n4. **Confound 控制**：incompleteness 的 information-addition confound 是否被充分控制（logistic regression p=0.022, coefficient change <8%），token count 作为 information content proxy 的有效性\n5. **Reproducibility**：ICC=0.919 仅 within OpenAI family，cross-provider stability 是否有直接证据；API 超参数是否完整报告；replication on 2 additional models 的样本量是否充分\n6. **Claims 与 evidence 的匹配度**：C1-C4 四个 claims 是否都有充分支撑，特别是 C3（inconclusive）和 C4（exploratory）的定位是否恰当\n\n请按 ARR 审稿标准输出完整审稿意见，包含 Summary / Strengths / Weaknesses / Questions / Missing References / Overall Assessment。Weaknesses 按严重程度标注 [MUST-FIX] / [SHOULD-FIX] / [MINOR]。",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 773 · 2026-05-21T17:39:17.007780+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16182
}
```

</details>

---


### Tool call

_source line 774 · 2026-05-21T17:39:17.158858+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性**。\n\n## 论文信息\n- 标题: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n- 路径: projects/policy_ambiguity_safety/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf\n- 目标 venue: EMNLP 2026 via ARR May cycle (deadline: 2026-05-25)\n\n## Venue 格式要求\n- Long paper: 正文 ≤ 8 页, 参考文献不限, Limitations 必须有（不计入页数）\n- ACL 官方模板, double-blind\n- 附录不计入页数, reviewer 不强制阅读\n\n## 你的审查侧重\n请重点审查以下方面：\n\n1. **新颖性与贡献**：six-type two-layer ambiguity taxonomy 相对于 Li et al. 2024 (11-type NLP taxonomy) / Massey et al. 2014 (6-type RE taxonomy) / DRIP-R 2026 (5-type) 的增量贡献是否显著；\"Differential Nocuity\" 框架是否超越 Berry & Kamsties 2004 的 nocuous/innocuous 二分；matched-pair causal design 在 agent safety 领域是否真正 novel\n2. **Related Work 覆盖**：是否遗漏重要相关工作（特别是 agent safety benchmarks, policy specification, ambiguity detection/resolution 领域），DRIP-R / PolicyBank / AgentPex / MANTRA 等并发工作的比较是否公允\n3. **Taxonomy 设计**：两层结构（linguistic vs specification）的理论基础是否充分——特别是 authorization scope 在 CL 传统中属于 vagueness 而非 ambiguity 的问题，conditional precedence 是规范冲突而非语言学歧义的问题；Wasow 2005 操作性定义是否足以覆盖所有 6 个类型\n4. **Writing 质量**：Abstract 信息密度、叙事结构、术语一致性、claim 措辞是否准确（特别是 incompleteness confound 的表述、C4 authorization scope 的 \"suggestive\" 定位）\n5. **格式合规**：正文是否 ≤ 8 页、匿名是否符合 double-blind、Limitations section 是否完整、引用格式是否符合 ACL 规范、是否有 orphan bib entries\n6. **Framing**：论文定位在 CL+safety 交叉领域是否适合 EMNLP，narrative 是否 CL-first（从 ambiguity detection/resolution 文献入手），还是过度偏向 safety/agent 应用\n\n请按 ARR 审稿标准输出完整审稿意见，包含 Summary / Strengths / Weaknesses / Questions / Missing References / Overall Assessment。Weaknesses 按严重程度标注 [MUST-FIX] / [SHOULD-FIX] / [MINOR]。",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性**。\n\n## 论文信息\n- 标题: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n- 路径: projects/policy_ambiguity_safety/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf\n- 目标 venue: EMNLP 2026 via ARR May cycle (deadline: 2026-05-25)\n\n## Venue 格式要求\n- Long paper: 正文 ≤ 8 页, 参考文献不限, Limitations 必须有（不计入页数）\n- ACL 官方模板, double-blind\n- 附录不计入页数, reviewer 不强制阅读\n\n## 你的审查侧重\n请重点审查以下方面：\n\n1. **新颖性与贡献**：six-type two-layer ambiguity taxonomy 相对于 Li et al. 2024 (11-type NLP taxonomy) / Massey et al. 2014 (6-type RE taxonomy) / DRIP-R 2026 (5-type) 的增量贡献是否显著；\"Differential Nocuity\" 框架是否超越 Berry & Kamsties 2004 的 nocuous/innocuous 二分；matched-pair causal design 在 agent safety 领域是否真正 novel\n2. **Related Work 覆盖**：是否遗漏重要相关工作（特别是 agent safety benchmarks, policy specification, ambiguity detection/resolution 领域），DRIP-R / PolicyBank / AgentPex / MANTRA 等并发工作的比较是否公允\n3. **Taxonomy 设计**：两层结构（linguistic vs specification）的理论基础是否充分——特别是 authorization scope 在 CL 传统中属于 vagueness 而非 ambiguity 的问题，conditional precedence 是规范冲突而非语言学歧义的问题；Wasow 2005 操作性定义是否足以覆盖所有 6 个类型\n4. **Writing 质量**：Abstract 信息密度、叙事结构、术语一致性、claim 措辞是否准确（特别是 incompleteness confound 的表述、C4 authorization scope 的 \"suggestive\" 定位）\n5. **格式合规**：正文是否 ≤ 8 页、匿名是否符合 double-blind、Limitations section 是否完整、引用格式是否符合 ACL 规范、是否有 orphan bib entries\n6. **Framing**：论文定位在 CL+safety 交叉领域是否适合 EMNLP，narrative 是否 CL-first（从 ambiguity detection/resolution 文献入手），还是过度偏向 safety/agent 应用\n\n请按 ARR 审稿标准输出完整审稿意见，包含 Summary / Strengths / Weaknesses / Questions / Missing References / Overall Assessment。Weaknesses 按严重程度标注 [MUST-FIX] / [SHOULD-FIX] / [MINOR]。",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 775 · 2026-05-21T17:39:18.415300+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1256
}
```

</details>

---


### Assistant

_source line 776 · 2026-05-21T17:39:22.879943+00:00_

Round 1 已启动：
- ✅ 视觉审查 Agent 已派发（fire-and-forget）
- ✅ Reviewer 1（方法严谨性 + 实验有效性）已分配
- ✅ Reviewer 2（新颖性 + 完整性）已分配

等待两位 Reviewer 返回独立初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 67

## Round 67

2 recorded events


### User

_source line 777 · 2026-05-21T17:44:44.164743+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见（方法严谨性 + 实验有效性）

**论文**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
**Venue**: EMNLP 2026 via ARR May cycle

---

## Summary

本文研究 LLM agent 在自然语言策略规范下，不同类型的歧义（ambiguity）如何因果性地导致安全违规。作者构建了一个六类型、双层（linguistic / specification）歧义分类体系，在 τ²-bench 上通过 matched-pair design 生成 300 对条款（ambiguous vs. unambiguous），在 5 个模型上运行 2,997 个 episodes。核心发现：(C1) 歧义条款使违规率增加 34.0 pp（OR=15.1）；(C2) 类型间存在显著层次结构（Cramér's V=0.137），呈两层模式；(C3) specification vs. linguistic 层级区分不显著（inconclusive）；(C4) model×type 交互显著但标记为 exploratory。论文还报告了 "Ambiguity Blindness"（<11% disambiguation awareness）和三种 type-specific failure mechanisms。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | C1 有充分因果支撑（perturbation control + replication），C2 合理但 SESOI 锚定缺乏外部依据，C3/C4 恰当标注为 inconclusive/exploratory。authorization scope κ=0.385 削弱了 C4 部分结论的可靠性。 |
| Excitement | 3.5/5 | 研究问题及时且实用（ambiguity→safety violation 的因果映射），matched-pair 因果设计在 agent safety 领域较新。但"歧义导致更多违规"的 broad finding 本身不意外；type-level 差异是更有价值的贡献。 |
| Reproducibility | 4/5 | API 超参完整（temp=0, top_p=1, max_tokens=4096），承诺公开 300 clause pairs + pipeline + traces。ICC=0.919 仅限 OpenAI family 是局限。 |
| Confidence | 4/5 | 我熟悉因果推断、agent safety evaluation 和 NLP ambiguity 文献。 |
| **Overall Assessment** | **3.5** | **Borderline Conference** — 方法论扎实、transparency 出色，但若干测量可靠性问题和 SESOI 锚定缺陷使 C2/C4 的说服力受限。 |

---

## 主要优势

**S1. 因果设计严谨（C1）。** Matched-pair design + perturbation control（Δ_perturb = −0.67 pp, CI 含零）是该领域少见的因果识别策略。perturbation control 排除了表层文本变化的混淆，使 34.0 pp 效应可归因于语义歧义（§4.2, §4.5）。在 7 个模型上的 replication（Appendix E）进一步增强了外部效度。

**S2. Confound 透明度极高。** Incompleteness 的 information-addition confound 在 §3（taxonomy 定义）就主动指出，§5.2 讨论，Appendix F 和 H 提供 logistic regression 控制（p=0.022, coefficient change <8%）和 coreferential lower bound。这种 self-critique 水平在 agent safety 论文中罕见。

**S3. Claims 层次清晰。** C1（primary, well-supported）→ C2（primary, with caveats）→ C3（inconclusive）→ C4（exploratory）的递进标注是良好科学实践，避免了 overclaim。

**S4. 分析深度充分。** Severity sensitivity（Appendix C）、TOST sensitivity across 7 margins（Appendix A）、bootstrap cluster analysis（Appendix I）、clause-level LOO variance（Appendix J）、failure mode taxonomy（§6）提供了多角度 robustness 检验。

**S5. 实际可操作性。** Differential Nocuity 框架将 ambiguity type mapping 到 failure mechanism，detection experiment（Appendix D）展示了 pipeline 原型（binary F1=0.81），mitigation experiment（Appendix B）量化了 type-specific intervention 效果。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **SESOI ±15 pp 缺乏外部锚定，C2 两层结构的稳健性不足**

- 具体位置：§4.6, Appendix A (Table 2)
- 问题：SESOI ±15 pp 的唯一理由是"a type producing ≥15 pp more violations warrants distinct policy handling in deployment"和"exceeds perturbation control bound by >2×"（§4.6）。前者是作者主观判断，缺乏外部文献或 domain expert 调研的支持；后者是循环论证——perturbation control bound 是本实验的产物而非独立标准。Table 2（Appendix A）显示，±10 pp 时仅 3/6 mid-tier pairs 等价，TOST power 降至 0.57。这意味着"两层结构"在合理的替代 margin 下部分瓦解。Bootstrap cluster 分析的 AU p-value=0.47（Appendix I）也表明 incompleteness singleton 边界并不尖锐。
- 为什么影响接收：C2 是论文的核心贡献之一（"Differential Nocuity"框架的基础）。如果两层结构高度依赖 margin 选择，framework 的 prescriptive value 就大打折扣。
- 建议修改方向：(1) 提供 deployment scenario 中 ±15 pp 阈值的外部依据（如 industry policy error tolerance survey、deployment cost-benefit analysis 文献）；(2) 在正文中更显著地呈现 sensitivity 结果，明确表述两层结构在 ±10–12 pp 时不完全成立；(3) 考虑降低对两层结构的 claim 强度，将其定位为 "one plausible clustering" 而非 "the hierarchy"。

**N2** [critical] **Authorization scope κ=0.385 下的 C4 结论可信度不足**

- 具体位置：§4.4（cross-judge calibration），§5.4（C4），Appendix G（Table 8）
- 问题：Authorization scope 的 cross-judge κ=0.385 仅为 "fair"（Landis-Koch），human-LLM κ=0.644，CI=[0.35, 0.91]。然而 C4 讨论中称 authorization scope 是 "most model-differentiating type"（52 pp range, Claude 12% → GPT-5.4 64%），并在 Discussion（§7）据此推测 safety training 差异化地 mitigate 了 boundary-type ambiguity。当测量工具的可靠性不足时，跨模型的 52 pp 变异中有多少是真实效应、多少是测量噪声难以分离。Figure 3 中 authorization scope 的突出视觉呈现进一步放大了读者对这一 pattern 的信心。
- 为什么影响接收：C4 虽标注为 exploratory，但 Discussion 和 Abstract 中的 framing 对 authorization scope 的 differential safety training 暗示过于确定。如果 κ=0.385 的 type 驱动了 framework 的核心 prediction (P1)，整个 Differential Nocuity narrative 的 evidentiary basis 就不够 solid。
- 建议修改方向：(1) 在 C4 讨论中加入 "given the low per-type agreement (κ=0.385), the authorization scope range should be interpreted as an upper bound on true between-model variance" 的显式 caveat；(2) Abstract 中 "authorization scope varies 52 pp" 应附带 measurement uncertainty qualification；(3) 验证 52 pp range 在 moderate+ vs. any-violation 阈值下是否稳定（Appendix C 仅报告 Cramér's V 和 Kendall τ，未报告 per-type range stability）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Token count 作为 information content proxy 的有效性未验证**

- 具体位置：Appendix F, Appendix H (Table 9)
- 问题：Incompleteness confound 的 logistic regression 使用 token count difference 作为 information content 的代理变量。但 token count 是信息量的粗糙近似——两个同样 token 数的条款可能信息含量差异很大（例如，添加一个 exception clause vs. 添加一个 padding phrase）。论文未讨论此 proxy 的 content validity，也未尝试替代度量（如 semantic similarity shift、clause-level entropy change）。
- 建议：(1) 讨论 token count 作为 proxy 的局限性；(2) 如有时间，补充至少一种替代 information content 度量以验证 robustness。

**W2** [warning] **Human validation 样本量偏小，per-type 估计不可靠**

- 具体位置：§4.4（Human validation），Appendix G (Table 8)
- 问题：100 episodes（2,997 的 3.3%），每种类型仅 32-34 个 episodes。Scopal 的 95% CI 是 [0.00, 1.00]，coreferential 是 [0.00, 0.84]——这些 CI 本质上是 uninformative 的。论文在 Limitations 中承认了这一点（§Limitations, "Per-type reliability"），但 §4.4 的正文呈现过于乐观地强调了 pooled κ=0.733 而淡化了 per-type 的不稳定性。
- 建议：(1) 在 §4.4 正文中更显著地呈现 per-type CI 宽度；(2) 如果可行，增加 human validation 样本量（尤其是 authorization scope 和 coreferential）。

**W3** [warning] **Cross-provider reproducibility 缺乏直接度量**

- 具体位置：§4.5（Reproducibility）
- 问题：ICC=0.919 仅在 OpenAI family（GPT-5.4, GPT-4.1）内计算，cross-provider stability 仅通过 "C1 consistency across all seven models" 间接论证。但 C1 consistency（所有模型都显示 significant Δ）是一个方向性声明，不等价于 effect size 的跨 provider 稳定性。论文甚至在 replication 中观察到 LLaMA 的 Δ=+20.0 pp 远小于主研究的 +25.7 to +39.0 pp range，且 LLaMA 的 unambiguous baseline 高达 17.6%，暗示跨 provider 的 effect 可能受 baseline instruction-following quality 调节。
- 建议：(1) 明确承认 ICC 仅为 within-provider；(2) 计算 replication models 与原始 5 个模型之间的 effect size correlation 或 agreement 统计量。

**W4** [warning] **"Ambiguity Blindness" 的归因问题**

- 具体位置：§6.2
- 问题：论文将 <11% disambiguation awareness 称为 "Ambiguity Blindness"，暗示这是 LLM agents 的认知局限。但论文的 experimental setup 中，agent 的 system prompt 并未指示其检测或报告歧义——4.6% 的 awareness rate 可能反映的是 default instruction-following 行为（"按 policy 执行"），而非 inability to detect ambiguity。事实上，mitigation experiment（Appendix B）显示添加 disambiguation instruction 后违规率下降 8.5 pp，暗示 agents 并非 "blind" 而是 "uninstructed"。
- 建议：讨论 "Blindness" vs. "Uninstructedness" 的区分。如果 system prompt 中明确要求 flag ambiguity，awareness rate 是否会大幅提升？这直接影响 practical implication 的方向（是改善 policy 本身，还是改善 agent 指令？）。

**W5** [warning] **多重比较校正策略不透明**

- 具体位置：§4.6
- 问题：论文提到 "Holm-Bonferroni correction is applied within three test families"，但未明确定义这三个 test families 的边界。正文中的检验包括：McNemar's test (C1)、χ² omnibus (C2)、per-type Fisher's exact (C2 pairwise)、TOST (C2)、χ² for layer effect (C3)、F-test for interaction (C4)、logistic regression LRT (C4)。如何将这些分配到三个 families 中，correction 后哪些检验变为 non-significant，读者无法验证。
- 建议：明确列出三个 test families 的成员，报告 corrected p-values（至少在 Appendix）。

---

## 小问题（不影响接收）

- **M1**: Abstract 提到 "coefficient change < 8%"——这个细节过于 technical，放在 abstract 中增加了认知负担。考虑简化。
- **M2**: §5.2 "the two-tier pattern emerges at ±12 pp (5/6 mid-tier pairs equivalent) and stabilizes at ±15 pp (6/6)"——"stabilizes" 一词暗示 ±15 pp 是自然 breakpoint，但这恰好是使所有 pairs 等价的最小 margin，换言之是 ceiling 而非 breakpoint。措辞应更中性。
- **M3**: Figure 1 overview 图中 "cross-judge" 评估流程的箭头方向不太清晰——GPT-5.4 judge 评估哪些模型、GPT-4.1 评估哪个模型的视觉区分可以更明确。
- **M4**: §6.1 failure mode taxonomy 使用了两种 reliability 指标（Gwet's AC₁=0.62, Cohen's κ=0.52）。对不熟悉 prevalence paradox 的读者，建议在正文而非仅在 Limitations 中简要解释为什么要报告 AC₁。
- **M5**: Limitations 中 "per-type reliability" 段放在最后，但这是一个影响正文 C2 和 C4 interpretation 的关键 caveat，建议位置提前。
- **M6**: §5.4 的 F(20)=1.97 交互检验——df=20 对应 (5-1)×(6-1) 但文中括号内已解释了，确认正确。不过 denominator df 未报告（应为 n-k 相关），建议补充完整 F-test specification。

---

## Questions for Authors

**Q1**: 如果使用 ±10 pp 作为 SESOI（一个更保守但同样合理的 margin），C2 的 "Differential Nocuity" framework 的核心 narrative 如何调整？两层结构变为什么？

**Q2**: 论文是否尝试过让 agent 在 system prompt 中被要求 "flag any ambiguity in the policy before acting"？如果有，disambiguation awareness 从 4.6% 提升到多少？如果没有，这是否应该作为一个 baseline condition 加入实验设计？

**Q3**: Appendix B 的 mitigation experiment 中，authorization scope 的 pooled 下降 −18.0 pp 与 incompleteness 的 −3.4 pp 之间的差异是否经过统计检验（如 interaction test）？Discussion 中称此结果 "supports P1"，但没有报告这一对比的 p-value。

**Q4**: 关于 cross-judge design——如果在 100 episode dual-judge calibration sample 上，per-type 的 authorization scope κ=0.385 已经很低，作者是否考虑过对 authorization scope 使用 majority vote from multiple judges 来降低测量噪声？

**Q5**: Table 1 中 DeepSeek-V3 的 overall violation rate (49.7%) 远高于 Claude (30.3%)。这 19.4 pp gap 中有多少可归因于 judge identity confound（DeepSeek 由 GPT-5.4 判，Claude 也由 GPT-5.4 判——等等，两者用的是同一个 judge，所以 judge identity 不应解释它们之间的差异）？请确认 judge assignment 逻辑。

---

## Missing References

- **Tamkin et al., 2023** — "Evaluating and Mitigating Discrimination in Language Model Decisions" (policy-governed decision-making)
- **Pan et al., 2024** — "Do LLMs Follow Instructions? The Role of Instruction Ambiguity" (直接研究 LLM 的 ambiguity following 行为)
- **Karpinska & Iyyer, 2023** — "Large Language Models Effectively Leverage Document-level Context for Literary Translation..." (关于 LLM 处理 contextual ambiguity 的能力)
- 建议检查 DRIP-R (Borokatos et al., 2026) 是否有更完整的 camera-ready version 可引用

---

## 总体评分

**Overall**: 3.5 — Borderline Conference

**一句话总结**: C1 因果效应（+34 pp）的方法论严谨性达到 conference 标准，但 C2 核心框架对 SESOI 选择的敏感性和 authorization scope 低 κ 下的 C4 over-interpretation 是主要隐患——修复后可达 Conference acceptance。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 778 · 2026-05-21T17:44:52.983483+00:00_

Reviewer 1 审稿意见已收到（3.5 Borderline Conference）。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 68

## Round 68

2 recorded events


### User

_source line 779 · 2026-05-21T17:44:55.948454+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：

- **Overall 3.5 (Borderline Conference)**
- **2 个 Must-Fix**：(1) SESOI ±15pp 缺乏外部锚定，C2 两层结构对 margin 选择敏感；(2) Authorization scope κ=0.385 下 C4 结论可信度不足，Discussion/Abstract 对 differential safety training 的暗示过于确定
- **5 个 Should-Fix**：token count proxy 有效性未验证、human validation 样本偏小、cross-provider ICC 缺乏直接度量、"Ambiguity Blindness" 归因问题（uninstructed vs. blind）、多重比较校正策略不透明
- **核心判断**：C1（+34pp 因果效应）方法论严谨，C3/C4 标注恰当，但 C2 的 Differential Nocuity 框架和 C4 的 authorization scope narrative 需要更审慎的 claim calibration

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 780 · 2026-05-21T17:45:03.879455+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 69

## Round 69

6 recorded events


### User

_source line 781 · 2026-05-21T17:45:20.991860+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（新颖性 + 完整性）

**论文**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
**Venue**: EMNLP 2026 via ARR May cycle

---

## 总体评分
**Overall Assessment**: 3.5 / 5 — Borderline Conference
**一句话总结**: 实验设计扎实（matched-pair causal design 是该领域首创），但 taxonomy 理论基础存在根本性混淆（将 ambiguity、vagueness、incompleteness 混为一谈），"Differential Nocuity"框架的增量贡献有限。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 实验方法严谨（matched-pair + perturbation control + cross-judge calibration + human validation + 7-model replication），但 taxonomy 层面存在理论问题：authorization scope 属于 vagueness 而非 ambiguity，conditional precedence 是规范冲突而非语言歧义，incompleteness 是信息缺失而非多义解读。C3 layer distinction 未通过校正。 |
| **Excitement** | 3/5 | 研究问题重要且实际，但核心发现（ambiguity 导致 violations）的方向性可预测；taxonomy 来自既有工作的选择组合而非原创；"Differential Nocuity"本质上是 Berry & Kamsties 2004 nocuous/innocuous 二分在 LLM agent 场景下的自然推论——缺乏 disambiguation channel → 所有 ambiguity 都 nocuous → 危害程度取决于 type。 |
| **Reproducibility** | 4/5 | 方法描述详尽（temperature、top_p、max_tokens、API 调用日期均报告），承诺公开 300 clause pairs + evaluation pipeline + analysis scripts。ICC = 0.919 的 replication 结果增强可信度。扣分原因：cross-judge 设计将 judge identity 与 model identity confound，且 coreferential 被排除在 replication/mitigation 之外。 |
| **Reviewer Confidence** | 4/5 | 熟悉 CL ambiguity 文献、RE ambiguity detection、agent safety benchmarks。仔细检查了统计方法和实验设计。 |

---

## Summary

本文通过 matched-pair 实验设计，在 τ²-bench 上测量六类 policy ambiguity 对 LLM agent 安全违规的因果影响。核心发现：ambiguous clauses 提升 violation rate 34.0 pp（OR = 15.1），type 决定 severity 的方差是 model 的 22 倍，incompleteness 一致性最高（46–62%），authorization scope 模型差异最大（12%–64%），agents 显示 <11% disambiguation awareness（"Ambiguity Blindness"）。

---

## 主要优势

1. **实验设计是本文最强贡献**。matched-pair causal design + perturbation control 是该领域首创——DRIP-R 做相关分析，PolicyBank 做迭代改进，本文是第一个建立因果关系的工作。Section 4.2 的 minimal-edit 设计、Section 4.5 的 perturbation control（Δ_perturb = −0.67 pp, CI containing zero）、以及 Appendix E 的 replication 共同构成了强有力的因果推断链。

2. **统计方法严谨且透明**。TOST equivalence testing + margin sensitivity analysis + bootstrap cluster analysis 三管齐下验证 type hierarchy；Appendix F 的 incompleteness confound analysis 用 logistic regression 控制 information delta；Limitations section 覆盖了 8 个具体局限。这种透明度在 agent safety 文献中罕见。

3. **关键发现具有实际价值**。Type 解释 22.4% 方差 vs. model 仅 1.0%（Section 5.1）意味着 policy auditing 应以 type 为导向而非 model 为导向——这对部署有直接指导意义。

4. **Honest reporting**。C3 layer distinction 未通过 Holm-Bonferroni 校正，作者如实报告为 "inconclusive"（Section 5.3）；C4 标注为 "[Exploratory]"；incompleteness 的 confound 在 abstract 中就提及。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Taxonomy 混淆了三个不同的语言学/逻辑现象**
- 具体位置：Section 3 (taxonomy.tex lines 1–22), Section 3 paragraph 1 (line 4)
- 问题：论文采用 Wasow et al. (2005) 的操作性定义（"admits multiple distinct interpretations"）并声称涵盖 vagueness（"including cases of vagueness where the boundary between interpretations is gradient rather than discrete"）。但 taxonomy 实际上混入了三个在形式语义学中根本不同的现象：
  - **Authorization scope** 是 *vagueness*（模糊的权限边界），不是 ambiguity（多义解读）。"Authorized personnel may issue refunds" 不存在多个离散的 interpretation——它的边界是 gradient 的，这正是 Kennedy (2007) 定义的 vagueness。论文引用了 Kennedy 但没有解释为何将 vagueness 归入 ambiguity taxonomy。
  - **Incompleteness** 是 *information absence*（缺失条件/例外），不是 present text 的多义性。论文自己承认 "incompleteness resolution requires adding new policy content"（taxonomy.tex line 18）——如果需要添加内容才能消解，说明原文不是"有多个 interpretation"，而是"缺少信息"。
  - **Conditional precedence** 是 *normative conflict*（规范冲突/优先级缺失），属于法律推理和 deontic logic 的经典问题。"Premium customers receive free shipping" 和 "orders under $50 require a shipping fee" 每条规则本身毫无歧义；问题是 policy 没有指定冲突解决规则——这更接近 incompleteness（缺少优先级规则）而非 ambiguity。
- 为什么影响接收：如果 6 个 type 中有 3 个不严格属于 ambiguity，那么论文的核心 claim——"ambiguity type predicts severity"——的理论基础被削弱。读者会质疑：你测量的到底是 ambiguity 的影响还是更广泛的 "policy specification defects" 的影响？
- 建议修改方向：(a) 将论文重新 framing 为 "policy specification defects"（涵盖 ambiguity + vagueness + incompleteness + normative conflict），taxonomy 名称相应调整；或 (b) 保留 ambiguity framing 但正面讨论这个理论张力——Section 3 需要一个 "Scope of 'ambiguity'" 段落，明确论证为何在操作层面将这三类现象统一处理是合理的（例如：对 LLM agent 而言它们的 downstream effect 相同——都导致 underdetermined action selection），同时承认这偏离了 CL 传统定义。

**N2** [critical] **"Differential Nocuity" 框架的增量贡献不清晰**
- 具体位置：Section 7 Discussion, Section 1 Introduction (contribution 2)
- 问题：Berry & Kamsties (2004) 提出 nocuous vs. innocuous ambiguity 的二分，基于 stakeholder divergence。本文的 "Differential Nocuity" 声称扩展了这个框架，提出 risk 取决于三个因素：ambiguity type、safety training、disambiguation channel availability。但这个扩展的逻辑链几乎是 trivial 的：
  - LLM agents 缺乏 disambiguation channels（human RE 有 colleague consultation、iterative clarification）→ 所有 ambiguity 对 LLM agents 都是 nocuous → 这只是 Berry & Kamsties 框架的直接推论，不需要实验就能得出
  - 不同 type 导致不同 severity → 这是 C2 的实验发现，本身很好，但将其包装为 "framework" 似乎过度
  - Safety training differentially mitigates specific types → 这基于 C4 的 [Exploratory] 结果，且 authorization scope 有最低的 judge agreement (κ = 0.385)
- 为什么影响接收：框架性贡献是 Introduction 中三个 contributions 之一，如果这只是实验发现的重新包装而非真正的理论贡献，论文的 novelty 需要 recalibrate。
- 建议修改方向：(a) 将 "Differential Nocuity" 降级为 Discussion 中的 interpretive lens 而非 contribution，将 contribution (2) 重写为纯实验发现（type hierarchy + variance decomposition）；或 (b) 如果要保留为框架贡献，需要展示它产生了 non-obvious predictions——当前的 P1 和 P2（Discussion, Section 7）太 vague，且 P1 的"支持证据"来自 Appendix B 的 mitigation experiment，该实验只有 1,256 episodes 且排除了 coreferential。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Abstract 信息过载，关键 message 被淹没**
- 具体位置：sections/abstract.tex
- 问题：Abstract 试图在一段中塞入 OR、CI、p-values、Cramér's V、coefficient change、κ 等大量数字。关键 takeaway（type matters more than model; incompleteness is consistently worst; agents are blind to ambiguity）被统计细节淹没。当前 abstract 读起来像 Results section 的压缩版而非独立的 narrative。
- 建议：将 abstract 重构为 problem → approach → key findings (2-3 highlights) → implication 的叙事结构，将具体数字精简到最有冲击力的 2-3 个。

**W2** [warning] **C3 Layer Distinction 的呈现有误导性**
- 具体位置：Section 5.3 (experiments.tex lines 47–49), Section 3 taxonomy structure
- 问题：C3（specification vs. linguistic layer）未通过 Holm-Bonferroni 校正且在控制 token delta 后方向翻转，但论文仍以这个 layer distinction 作为 taxonomy 的组织原则（Section 3 的 "Linguistic layer" 和 "Specification layer" 标题）。如果经验证据不支持 layer distinction，为何 taxonomy 仍以此为核心结构？这在逻辑上不一致。
- 建议：(a) 在 Section 3 引入 taxonomy 时就说明 layer 是 hypothesis 而非 established structure；(b) 或者放弃 two-layer framing，改为 flat six-type taxonomy with post-hoc clustering（这更诚实地反映了 C2 的 bootstrap cluster 结果）。

**W3** [warning] **与 DRIP-R 的 taxonomy 映射缺失**
- 具体位置：Section 2 Related Work (related_work.tex line 14), Section 3 (taxonomy.tex line 6)
- 问题：DRIP-R (Borkakoty et al., 2026) 是最接近的并发工作，也有 5 个 RE ambiguity types。论文 Section 2 列出了三点差异（causal design、safety violations、linguistic-layer types），但没有提供 type-level mapping：DRIP-R 的 5 个 types 如何对应本文的 6 个 types？哪些 overlap？哪些是新增？这对评估 taxonomy 的增量贡献至关重要。
- 建议：在 Section 3 或 Related Work 中加一个显式的 type mapping 比较（可以是一小段文字或脚注）。

**W4** [warning] **Coreferential ambiguity 被系统性地排除在多个分析之外**
- 具体位置：Appendix B (mitigation experiment), Appendix D (detection experiment), Appendix E (model expansion replication)
- 问题：Coreferential ambiguity 被排除在 mitigation experiment（"was not tested"）、detection experiment（"excluded because its variants are lexically identical"）和 model expansion replication（"disambiguation relies on benchmark-specific assertion structure"）之外。这意味着六类中有一类在三个附录分析中都缺席，削弱了 taxonomy 的"completeness"claim。如果 coreferential 的操作化高度依赖 τ²-bench 的 assertion structure，这暗示该 type 的 external validity 存疑。
- 建议：在 Limitations 中显式讨论 coreferential 的 operationalization 局限；或在正文中解释为何这不影响主要 claims。

**W5** [warning] **"Ambiguity Blindness" 的 framing 可能过度**
- 具体位置：Section 6.2 (analysis.tex lines 20–24)
- 问题：论文将 agents 不显式承认 ambiguity（<11% disambiguation awareness）称为 "Ambiguity Blindness"，并与 Hu et al. (2025) 的 "missing conceptual representations" 关联。但 Ferreira et al. (2002)——论文自己也引用——指出人类也默认采用 "good-enough" single parse 而不显式标记歧义。如果人类也"blind"，那 agents 的行为就不是 pathological 的，而是 default processing strategy 的自然延伸。"Blindness" 暗示了一种 deficit，但论文的数据只能支持 "agents default to single interpretations" 而非 "agents lack the capacity to represent ambiguity"。
- 建议：将 "Ambiguity Blindness" 重新定义为 "lack of *externalized* disambiguation"（agents 不主动 seek clarification），而非暗示 cognitive/representational deficit。或引用 Liu et al. (2023) "We're Afraid Language Models Aren't Modeling Ambiguity" 更精确地定位这个现象。

---

## 小问题（不影响接收）

- **引用 ferrari_defects_2018**：bib entry 列 "Rosadini, Benedetta" 为第一作者但 key 用 "ferrari_defects"，OpenAlex 验证显示 first_author mismatch (bib=rosadini vs api=ferrari)。应核实第一作者是否正确。
- **navigli_wsd_2009**：OpenAlex 显示 year mismatch (bib 2009 vs API 2015) 和 author mismatch——可能匹配到了不同版本/survey。建议核实。
- **Section 1 "seven models"**：Introduction 的 contribution (1) 说 "replicated across seven models" 但主实验只有 5 个 model，另外 2 个在 Appendix。措辞应更精确区分 main study vs. replication。
- **Figure 1 overview diagram**（page 2）：图中显示 "→ ±2.5 Δ" 和 "→ -2.5 Δ" 等标注，字体较小且不易理解其含义。建议增大字号或在 caption 中解释。
- **Equation-free paper**：整篇论文没有 numbered equations。虽然不是必需的，但 Differential Nocuity 框架如果有一个简单的形式化表达（even as a risk = f(type, training, channel) 的概念公式）会更清晰。

---

## Missing References（建议考虑）

1. **SafeAgentBench** (Yin et al., 2025) — 另一个重要的 agent safety benchmark，在 embodied agent 场景下评估安全性；与 R-Judge、ToolEmu 互补。
2. **AgentHarm** (Andriushchenko et al., 2024) — agent misuse benchmark，虽然关注恶意使用而非 policy ambiguity，但作为 agent safety evaluation 的重要工作应该在 Related Work 的 agent safety 段落中至少提及。
3. **Deontic logic / normative conflict resolution** 文献 — conditional precedence 本质上是 normative conflict，应引用 legal AI / deontic logic 文献（如 Prakken & Sartor 的 defeasible reasoning 工作）来支撑这个 type 的理论基础。

---

## Questions for Authors

1. 如果将 authorization scope、incompleteness、conditional precedence 从 taxonomy 中移除，只保留三个纯语言学 ambiguity type（scopal、lexical、coreferential），C1 和 C2 的结论是否仍然成立？请报告 three-type subset 的 Δpp 和 omnibus χ² 结果。
2. Clause pairs 的生成使用 "template-based pipeline"（Section 4.2）——templates 是什么样的？每种 type 有多少 templates？这决定了 300 clause pairs 的多样性。
3. Table 1 中 Claude 的 authorization scope violation rate 仅 12%（其他模型 26–64%），且 authorization scope 的 cross-judge κ = 0.385。如何排除这个 outlier 不是由 judge 差异而非 model 差异驱动的？

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| 正文 ≤ 8 页 | ✅ | Sections 1–8 在 pages 1–8 |
| Double-blind | ✅ | `\author{Anonymous}`, `\usepackage[review]{acl}` |
| Limitations section | ✅ | Page 9, 详尽（8 个具体局限） |
| 引用格式 | ✅ | citet/citep 使用正确，37 entries, 0 orphan, 0 missing |
| ACL 模板 | ✅ | acl.sty with review option |
| 匿名 URL | ✅ | github.com/anonymous/... |
| Appendix | ✅ | 10 个 appendix sections (A–J), 不计入页数 |
| Orphan bib entries | ✅ | 0 orphan entries |

---

## 总结

这是一篇在实验执行上达到高水准的论文——matched-pair causal design、perturbation control、cross-judge calibration、7-model replication、10 个附录分析——这在 agent safety 文献中并不常见。核心发现（ambiguity type 解释 22x 于 model 的方差；incompleteness 一致性最高；agents <11% disambiguation awareness）有实际部署价值。

但论文的理论基础存在根本性张力：一个名为 "ambiguity taxonomy" 的框架混入了 vagueness、information absence、normative conflict，而经验证据又不支持 taxonomy 的 two-layer 组织结构（C3 inconclusive）。"Differential Nocuity" 的增量贡献有限。如果作者能在 rebuttal 中 (a) 正面 address taxonomy 的理论混淆并调整 framing，(b) 将 Differential Nocuity 从 contribution 降级为 interpretive lens，这篇论文的评分可以上调。当前定位为 Borderline Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 782 · 2026-05-21T17:46:10.812398+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1（方法严谨性 + 实验有效性）的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每一条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 完整审稿意见\n\n## Overall: 3.5 — Borderline Conference\n\n## 主要优势\nS1. 因果设计严谨（C1）。Matched-pair design + perturbation control（Δ_perturb = −0.67 pp, CI 含零）是该领域少见的因果识别策略。在 7 个模型上的 replication 进一步增强了外部效度。\nS2. Confound 透明度极高。Incompleteness 的 information-addition confound 在 §3 就主动指出，§5.2 讨论，Appendix F 和 H 提供控制。\nS3. Claims 层次清晰。C1→C2→C3→C4 的递进标注是良好科学实践。\nS4. 分析深度充分。Severity sensitivity、TOST sensitivity、bootstrap cluster、clause-level LOO variance、failure mode taxonomy 提供了多角度 robustness 检验。\nS5. 实际可操作性。Detection experiment（binary F1=0.81）和 mitigation experiment 量化了 type-specific intervention 效果。\n\n## Must-Fix 问题\n\n**N1** [critical] **SESOI ±15 pp 缺乏外部锚定，C2 两层结构的稳健性不足**\n- §4.6, Appendix A: SESOI ±15 pp 唯一理由是作者主观判断和 perturbation control bound 的 2× 倍数（循环论证）。Table 2 显示 ±10 pp 时仅 3/6 mid-tier pairs 等价，TOST power 降至 0.57。Bootstrap cluster 的 AU p-value=0.47 也表明 incompleteness singleton 边界不尖锐。\n- C2 是 \"Differential Nocuity\" 框架的基础，如果两层结构高度依赖 margin 选择，framework 的 prescriptive value 大打折扣。\n- 建议：提供外部依据、正文更显著呈现 sensitivity 结果、降低 claim 强度。\n\n**N2** [critical] **Authorization scope κ=0.385 下的 C4 结论可信度不足**\n- §4.4, §5.4, Appendix G: cross-judge κ=0.385 仅为 fair，human-LLM κ=0.644 CI=[0.35,0.91]。C4 讨论称 authorization scope 是 \"most model-differentiating type\"（52 pp range），Discussion 据此推测 safety training 差异化 mitigation。测量工具可靠性不足时，52 pp 变异中真实效应 vs. 测量噪声难以分离。\n- 建议：加入显式 caveat、Abstract 附带 measurement uncertainty、验证 per-type range 在不同 severity 阈值下的稳定性。\n\n## Should-Fix 问题\n\n**W1** [warning] Token count 作为 information content proxy 的有效性未验证（Appendix F, H）\n**W2** [warning] Human validation 样本量偏小（100/2997 = 3.3%），per-type 估计不可靠（scopal CI [0.00,1.00]）\n**W3** [warning] Cross-provider reproducibility 缺乏直接度量（ICC=0.919 仅 within OpenAI family）\n**W4** [warning] \"Ambiguity Blindness\" 归因问题——4.6% awareness 可能反映 uninstructed 而非 inability；mitigation experiment 下降 8.5 pp 暗示 agents 并非 blind\n**W5** [warning] 多重比较校正策略不透明——\"three test families\" 未明确定义\n\n## 小问题\nM1: Abstract 中 \"coefficient change < 8%\" 过于 technical\nM2: \"stabilizes at ±15 pp\" 措辞暗示自然 breakpoint，实为 ceiling\nM3: Figure 1 cross-judge 箭头不清晰\nM4: §6.1 Gwet's AC₁ vs Cohen's κ 差异应在正文解释\nM5: Limitations 中 per-type reliability 位置应提前\nM6: §5.4 F(20)=1.97 缺少 denominator df\n\n## Questions\nQ1: ±10 pp 下 C2 narrative 如何调整？\nQ2: System prompt 中要求 flag ambiguity 后 awareness rate 变化？\nQ3: Appendix B mitigation 中 auth scope −18.0 pp vs incompleteness −3.4 pp 差异是否经过统计检验？\nQ4: 对 authorization scope 是否考虑 majority vote from multiple judges？\nQ5: Table 1 中 DeepSeek 49.7% vs Claude 30.3% 的 judge identity confound 确认？\n\n## Missing References\n- Tamkin et al. 2023, Pan et al. 2024, Karpinska & Iyyer 2023, DRIP-R camera-ready version",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1（方法严谨性 + 实验有效性）的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每一条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 完整审稿意见\n\n## Overall: 3.5 — Borderline Conference\n\n## 主要优势\nS1. 因果设计严谨（C1）。Matched-pair design + perturbation control（Δ_perturb = −0.67 pp, CI 含零）是该领域少见的因果识别策略。在 7 个模型上的 replication 进一步增强了外部效度。\nS2. Confound 透明度极高。Incompleteness 的 information-addition confound 在 §3 就主动指出，§5.2 讨论，Appendix F 和 H 提供控制。\nS3. Claims 层次清晰。C1→C2→C3→C4 的递进标注是良好科学实践。\nS4. 分析深度充分。Severity sensitivity、TOST sensitivity、bootstrap cluster、clause-level LOO variance、failure mode taxonomy 提供了多角度 robustness 检验。\nS5. 实际可操作性。Detection experiment（binary F1=0.81）和 mitigation experiment 量化了 type-specific intervention 效果。\n\n## Must-Fix 问题\n\n**N1** [critical] **SESOI ±15 pp 缺乏外部锚定，C2 两层结构的稳健性不足**\n- §4.6, Appendix A: SESOI ±15 pp 唯一理由是作者主观判断和 perturbation control bound 的 2× 倍数（循环论证）。Table 2 显示 ±10 pp 时仅 3/6 mid-tier pairs 等价，TOST power 降至 0.57。Bootstrap cluster 的 AU p-value=0.47 也表明 incompleteness singleton 边界不尖锐。\n- C2 是 \"Differential Nocuity\" 框架的基础，如果两层结构高度依赖 margin 选择，framework 的 prescriptive value 大打折扣。\n- 建议：提供外部依据、正文更显著呈现 sensitivity 结果、降低 claim 强度。\n\n**N2** [critical] **Authorization scope κ=0.385 下的 C4 结论可信度不足**\n- §4.4, §5.4, Appendix G: cross-judge κ=0.385 仅为 fair，human-LLM κ=0.644 CI=[0.35,0.91]。C4 讨论称 authorization scope 是 \"most model-differentiating type\"（52 pp range），Discussion 据此推测 safety training 差异化 mitigation。测量工具可靠性不足时，52 pp 变异中真实效应 vs. 测量噪声难以分离。\n- 建议：加入显式 caveat、Abstract 附带 measurement uncertainty、验证 per-type range 在不同 severity 阈值下的稳定性。\n\n## Should-Fix 问题\n\n**W1** [warning] Token count 作为 information content proxy 的有效性未验证（Appendix F, H）\n**W2** [warning] Human validation 样本量偏小（100/2997 = 3.3%），per-type 估计不可靠（scopal CI [0.00,1.00]）\n**W3** [warning] Cross-provider reproducibility 缺乏直接度量（ICC=0.919 仅 within OpenAI family）\n**W4** [warning] \"Ambiguity Blindness\" 归因问题——4.6% awareness 可能反映 uninstructed 而非 inability；mitigation experiment 下降 8.5 pp 暗示 agents 并非 blind\n**W5** [warning] 多重比较校正策略不透明——\"three test families\" 未明确定义\n\n## 小问题\nM1: Abstract 中 \"coefficient change < 8%\" 过于 technical\nM2: \"stabilizes at ±15 pp\" 措辞暗示自然 breakpoint，实为 ceiling\nM3: Figure 1 cross-judge 箭头不清晰\nM4: §6.1 Gwet's AC₁ vs Cohen's κ 差异应在正文解释\nM5: Limitations 中 per-type reliability 位置应提前\nM6: §5.4 F(20)=1.97 缺少 denominator df\n\n## Questions\nQ1: ±10 pp 下 C2 narrative 如何调整？\nQ2: System prompt 中要求 flag ambiguity 后 awareness rate 变化？\nQ3: Appendix B mitigation 中 auth scope −18.0 pp vs incompleteness −3.4 pp 差异是否经过统计检验？\nQ4: 对 authorization scope 是否考虑 majority vote from multiple judges？\nQ5: Table 1 中 DeepSeek 49.7% vs Claude 30.3% 的 judge identity confound 确认？\n\n## Missing References\n- Tamkin et al. 2023, Pan et al. 2024, Karpinska & Iyyer 2023, DRIP-R camera-ready version",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 783 · 2026-05-21T17:46:33.662845+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22850
}
```

</details>

---


### Tool call

_source line 784 · 2026-05-21T17:46:33.813676+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2（新颖性 + 完整性）的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每一条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 完整审稿意见\n\n## Overall: 3.5 — Borderline Conference\n\n## 主要优势\n1. 实验设计是最强贡献。matched-pair causal design + perturbation control 是该领域首创。\n2. 统计方法严谨且透明。TOST + margin sensitivity + bootstrap cluster 三管齐下。\n3. 关键发现有实际价值。Type 解释 22.4% 方差 vs. model 仅 1.0%。\n4. Honest reporting。C3 如实报告 inconclusive，C4 标注 [Exploratory]。\n\n## Must-Fix 问题\n\n**N1** [critical] **Taxonomy 混淆了三个不同的语言学/逻辑现象**\n- Section 3: taxonomy 将 ambiguity、vagueness、incompleteness 混为一谈。\n  - Authorization scope 是 vagueness（模糊权限边界），不是 ambiguity（多义解读）。Kennedy (2007) 定义的 gradient boundary。\n  - Incompleteness 是 information absence，不是 present text 的多义性。论文自己承认 \"resolution requires adding new policy content\"。\n  - Conditional precedence 是 normative conflict（规范冲突），每条规则本身毫无歧义，问题是缺少冲突解决规则。\n- 如果 6 个 type 中有 3 个不严格属于 ambiguity，核心 claim \"ambiguity type predicts severity\" 的理论基础被削弱。\n- 建议：(a) 重新 framing 为 \"policy specification defects\"；或 (b) 保留 ambiguity framing 但正面讨论理论张力。\n\n**N2** [critical] **\"Differential Nocuity\" 框架的增量贡献不清晰**\n- Section 7, Section 1 contribution (2): 框架声称 risk = f(ambiguity type, safety training, disambiguation channel availability)。但：\n  - LLM agents 缺乏 disambiguation channels → 所有 ambiguity 都 nocuous → Berry & Kamsties 2004 的直接推论，不需要实验\n  - 不同 type 导致不同 severity → C2 实验发现，将其包装为 \"framework\" 过度\n  - Safety training differentially mitigates → 基于 [Exploratory] 的 C4 + κ=0.385 的 authorization scope\n- 建议：降级为 interpretive lens 而非 contribution；或展示 non-obvious predictions。\n\n## Should-Fix 问题\n\n**W1** [warning] Abstract 信息过载，关键 message 被淹没。读起来像 Results 压缩版。\n**W2** [warning] C3 Layer Distinction 未通过校正但仍作为 taxonomy 组织原则——逻辑不一致。建议改为 flat six-type 或说明 layer 是 hypothesis。\n**W3** [warning] 与 DRIP-R 的 taxonomy 映射缺失——5 types 如何对应本文 6 types。\n**W4** [warning] Coreferential 被系统性排除在 mitigation/detection/replication 之外，削弱 taxonomy completeness。\n**W5** [warning] \"Ambiguity Blindness\" framing 过度——人类也默认 good-enough single parse（Ferreira 2002），如果人类也 blind 则 agents 行为不是 pathological。建议改为 \"lack of externalized disambiguation\"。\n\n## 小问题\n- ferrari_defects_2018 bib key vs first author mismatch\n- navigli_wsd_2009 year/author mismatch\n- Section 1 \"seven models\" 措辞应区分 main study vs. replication\n- Figure 1 标注字体过小\n- Differential Nocuity 缺少简单形式化表达\n\n## Missing References\n- SafeAgentBench (Yin et al. 2025), AgentHarm (Andriushchenko et al. 2024), deontic logic / normative conflict resolution 文献\n\n## Questions\nQ1: 移除 3 个 specification-layer types 后 C1/C2 是否成立？\nQ2: Clause pairs 的 templates 是什么样的？每种 type 多少 templates？\nQ3: Claude auth scope 12% outlier 如何排除是 judge 差异而非 model 差异？\n\n## 格式合规\n全部通过：正文 ≤8 页、double-blind、Limitations、ACL 模板、0 orphan bib entries。",
  "project": "policy_ambiguity_safety",
  "chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2（新颖性 + 完整性）的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每一条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 完整审稿意见\n\n## Overall: 3.5 — Borderline Conference\n\n## 主要优势\n1. 实验设计是最强贡献。matched-pair causal design + perturbation control 是该领域首创。\n2. 统计方法严谨且透明。TOST + margin sensitivity + bootstrap cluster 三管齐下。\n3. 关键发现有实际价值。Type 解释 22.4% 方差 vs. model 仅 1.0%。\n4. Honest reporting。C3 如实报告 inconclusive，C4 标注 [Exploratory]。\n\n## Must-Fix 问题\n\n**N1** [critical] **Taxonomy 混淆了三个不同的语言学/逻辑现象**\n- Section 3: taxonomy 将 ambiguity、vagueness、incompleteness 混为一谈。\n  - Authorization scope 是 vagueness（模糊权限边界），不是 ambiguity（多义解读）。Kennedy (2007) 定义的 gradient boundary。\n  - Incompleteness 是 information absence，不是 present text 的多义性。论文自己承认 \"resolution requires adding new policy content\"。\n  - Conditional precedence 是 normative conflict（规范冲突），每条规则本身毫无歧义，问题是缺少冲突解决规则。\n- 如果 6 个 type 中有 3 个不严格属于 ambiguity，核心 claim \"ambiguity type predicts severity\" 的理论基础被削弱。\n- 建议：(a) 重新 framing 为 \"policy specification defects\"；或 (b) 保留 ambiguity framing 但正面讨论理论张力。\n\n**N2** [critical] **\"Differential Nocuity\" 框架的增量贡献不清晰**\n- Section 7, Section 1 contribution (2): 框架声称 risk = f(ambiguity type, safety training, disambiguation channel availability)。但：\n  - LLM agents 缺乏 disambiguation channels → 所有 ambiguity 都 nocuous → Berry & Kamsties 2004 的直接推论，不需要实验\n  - 不同 type 导致不同 severity → C2 实验发现，将其包装为 \"framework\" 过度\n  - Safety training differentially mitigates → 基于 [Exploratory] 的 C4 + κ=0.385 的 authorization scope\n- 建议：降级为 interpretive lens 而非 contribution；或展示 non-obvious predictions。\n\n## Should-Fix 问题\n\n**W1** [warning] Abstract 信息过载，关键 message 被淹没。读起来像 Results 压缩版。\n**W2** [warning] C3 Layer Distinction 未通过校正但仍作为 taxonomy 组织原则——逻辑不一致。建议改为 flat six-type 或说明 layer 是 hypothesis。\n**W3** [warning] 与 DRIP-R 的 taxonomy 映射缺失——5 types 如何对应本文 6 types。\n**W4** [warning] Coreferential 被系统性排除在 mitigation/detection/replication 之外，削弱 taxonomy completeness。\n**W5** [warning] \"Ambiguity Blindness\" framing 过度——人类也默认 good-enough single parse（Ferreira 2002），如果人类也 blind 则 agents 行为不是 pathological。建议改为 \"lack of externalized disambiguation\"。\n\n## 小问题\n- ferrari_defects_2018 bib key vs first author mismatch\n- navigli_wsd_2009 year/author mismatch\n- Section 1 \"seven models\" 措辞应区分 main study vs. replication\n- Figure 1 标注字体过小\n- Differential Nocuity 缺少简单形式化表达\n\n## Missing References\n- SafeAgentBench (Yin et al. 2025), AgentHarm (Andriushchenko et al. 2024), deontic logic / normative conflict resolution 文献\n\n## Questions\nQ1: 移除 3 个 specification-layer types 后 C1/C2 是否成立？\nQ2: Clause pairs 的 templates 是什么样的？每种 type 多少 templates？\nQ3: Claude auth scope 12% outlier 如何排除是 judge 差异而非 model 差异？\n\n## 格式合规\n全部通过：正文 ≤8 页、double-blind、Limitations、ACL 模板、0 orphan bib entries。",
    "project": "policy_ambiguity_safety",
    "chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 785 · 2026-05-21T17:46:35.121110+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1307
}
```

</details>

---


### Assistant

_source line 786 · 2026-05-21T17:46:37.770733+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 70

## Round 70

2 recorded events


### User

_source line 787 · 2026-05-21T17:46:40.229791+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**核心判断：Overall 3.5 (Borderline Conference)**

关键发现：
- **两个 Must-Fix**：(1) Taxonomy 将 ambiguity、vagueness、incompleteness、normative conflict 混为一谈，理论基础有根本性问题；(2) "Differential Nocuity" 框架的增量贡献不清晰，基本是 Berry & Kamsties 2004 在 LLM 场景下的 trivial 推论
- **五个 Should-Fix**：Abstract 过载、C3 失败但仍以 layer 组织 taxonomy、与 DRIP-R 缺少 type mapping、coreferential 被系统性排除、"Ambiguity Blindness" framing 过度
- **主要优势**：matched-pair causal design 是该领域首创，统计方法严谨透明，type > model 的方差分解发现有实际价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 788 · 2026-05-21T17:46:45.678473+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 71

## Round 71

2 recorded events


### User

_source line 789 · 2026-05-21T17:48:00.920542+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: SESOI ±15 pp 缺乏外部锚定**

同意这是一个有效的方法论批评，但认为严重程度应适度下调。

理由：
1. R1 指出 ±15 pp 的唯一理由是 perturbation control bound 的 2× 倍数，属于循环论证——这一判断准确。Section 4.6 的原文是 "a type producing ≥15 pp more violations warrants distinct policy handling in deployment, and it exceeds the perturbation control bound (6.67 pp) by >2×"。前半句是 domain-relevance 论证但无外部来源支撑，后半句确实是循环的。
2. 然而，论文在这一点上的透明度已相当高：Section 4.6 明确写了 "we acknowledge margin dependence (Anvari and Lakens, 2021)"，Appendix A 提供了 ±5 到 ±20 pp 的完整 sensitivity analysis（Table 2），bootstrap cluster analysis（Appendix I）是 margin-free 的替代验证。
3. 关键证据：即使在 ±10 pp 下，incompleteness 仍然与所有 mid-tier types 分离（Table 2 shows Inc. sep. = ✓ at all margins ≤ ±18 pp）。C2 的核心 finding——incompleteness 是 upper bound——不受 margin 选择影响。受影响的是 mid-tier 内部的等价判定。
4. Bootstrap AU p-value = 0.47 确实表明 singleton 边界不尖锐（Appendix I），但 34.3% 是 most frequent partition，且 k=3 时 coreferential 额外分离，与 TOST 两层结构一致。

**结论**：同意需要外部锚定（如 agent deployment 中的 SLA 容忍度、行业 benchmark），但认为这不足以 invalidate C2——incompleteness 作为 upper bound 的结论在所有 margin 下都成立。建议将 N1 降为 [SHOULD-FIX]。

---

**[AGREE] R1-N2: Authorization scope κ=0.385 下的 C4 结论可信度**

完全同意，这也是我自己审稿意见中 N1（taxonomy 混淆）的一个下游表现。

理由：
1. κ=0.385 仅为 "fair" agreement。论文在 Section 4.4 报告了这一数字，Limitations 中也讨论了（"authorization scope has the lowest judge agreement"），但 C4 的 Discussion 仍然从这个 noisy measurement 推导出 safety training differential mitigation 的叙事（Section 7: "safety training (selective mitigation of boundary-type ambiguities)"）。
2. 更重要的是，Section 5.4 声称 "bootstrap ranking preservation: 99.5%" 来支持 authorization scope 排名的稳定性——但这个 bootstrap 是 within the GPT-5.4 judge subset，只能说明在同一 judge 下排名稳定，不能排除 judge-specific bias 造成的 52 pp range。
3. Human-LLM κ=0.644 [0.35, 0.91]（Appendix G, Table 8）的 CI 下界仅 0.35，进一步削弱对该 type 绝对值的信心。
4. 论文确实在 Section 5.4 末尾使用了 "suggestive rather than definitive" 的措辞，但 Introduction contribution (2) 和 Abstract 中的表述没有匹配这一 hedging。

**补充自己的发现**：这个问题与我的 N1（taxonomy 混淆）相互加强。Authorization scope 在语言学上属于 vagueness 而非 ambiguity（Section 3 的定义），且其 judge agreement 最低——两个独立的 weakness 同时作用于同一个 type，使得关于该 type 的所有 claim 都应被 heavily caveated。

---

### Should-Fix 问题

**[AGREE] R1-W1: Token count 作为 information content proxy 的有效性**

同意 token count 是粗糙的 proxy，但认为论文的处理已经 "good enough"。

理由：Appendix H 的 logistic regression 控制 token delta 后 incompleteness 仍显著（p=0.018, coefficient change <8%）。即使 token count 是不完美的 proxy，incompleteness 效应在控制后仅缩小 <8% 说明 information quantity 只能解释一小部分。更重要的是 coreferential（information delta = 0）提供了 confound-free lower bound（31.6% violation rate, 18.7 pp effect），这不依赖任何 proxy 选择。论文在 Appendix F 明确讨论了这一点。建议作者在 rebuttal 中承认 token count 的局限并讨论替代 proxy（如 semantic information units），但这不是 must-fix。

**[AGREE] R1-W2: Human validation 样本量偏小**

同意。100/2997 = 3.3% 的 human validation 确实偏小，per-type n=32-34 导致 CI 极宽（scopal [0.00, 1.00]，Table 8）。论文在 Limitations section 的 "Per-type reliability" 段落承认了这一点，但 R1 正确指出这些估计 "should not be over-interpreted at the individual type level" 的 caveat 在正文中不够显著——Section 4.4 的 human validation 段落给人以 "validation is thorough" 的印象，而实际上 per-type reliability 高度不确定。

**[AGREE] R1-W3: Cross-provider reproducibility**

同意，ICC=0.919 仅在 OpenAI family 内（Section 4.5: "ICC is computed within the OpenAI family"）。Cross-provider stability 的证据是间接的：C1 在所有 7 个模型上显著（Section 5.1），C2 type ranking 的 Spearman ρ 在 LLaMA 上 = 0.90（Appendix E）。但没有 cross-provider ICC 的直接度量。建议作者在 rebuttal 中计算跨 provider 的 type-ranking concordance（如 Kendall's W）作为补充。

**[AGREE] R1-W4: "Ambiguity Blindness" 归因问题**

强烈同意——这与我的 W5 高度一致。

理由：
1. Section 6.2 将 4.6% awareness 定义为 "acknowledging multiple interpretations, asking clarifying questions, or conditioning on ambiguity"，但实验中没有在 system prompt 里指示 agents 去 flag ambiguity——所以 4.6% 反映的是 uninstructed default behavior 而非 inability。
2. 关键矛盾证据来自论文自己的 Appendix B：mitigation experiment 通过添加 type-specific disambiguation instructions 将 violation rate 降低了 8.5 pp（Table 3）。如果 agents 真的 "blind" to ambiguity，instruction 不应该产生效果。−8.5 pp 的改善说明 agents CAN respond to ambiguity when prompted——"Blindness" 是 default behavior 而非 fundamental limitation。
3. 更精确的 framing 应该是 "Uninstructed Disambiguation Deficit" 或简单地说 agents 在默认情况下不 externalize ambiguity recognition。这与 Ferreira et al. (2002) 的 "good-enough processing" 平行——人类也默认采用 single parse，但这不叫 "blindness"。

**[AGREE] R1-W5: 多重比较校正策略不透明**

同意。Section 4.6 提到 "Holm-Bonferroni correction is applied within three test families" 但没有明确定义这三个 families 是什么。读者无法判断校正是否适当。这应该在正文或附录中显式列出：e.g., Family 1 = per-type C1 tests (6 tests), Family 2 = pairwise C2 comparisons (15 tests), Family 3 = ... 。

---

### 小问题

**[AGREE] R1-M1**: Abstract 中 "coefficient change < 8%" 过于 technical，同意——这个细节适合放在正文或附录，不适合 abstract。
**[AGREE] R1-M2**: "stabilizes at ±15 pp" 确实暗示了自然 breakpoint，但 Table 2 显示这只是 6/6 mid-tier pairs 等价的第一个 margin——更准确地说是 sensitivity analysis 的 ceiling。
**[AGREE] R1-M3**: Figure 1 cross-judge 箭头不清晰——我在自己的审稿中也标记了 Figure 1 标注字体过小。
**[AGREE] R1-M4**: Gwet's AC₁ vs Cohen's κ 差异确实应在正文解释，至少一句话说明 prevalence paradox 导致 κ 偏低。Section 6.1 有简短提及（"the gap reflects the prevalence paradox"）但不够充分。
**[AGREE] R1-M5**: Per-type reliability 在 Limitations 中的位置确实可以提前，让读者在看到 C4 结果时就意识到 measurement uncertainty。
**[REBUT] R1-M6**: Section 5.4 报告 "F(20)=1.97, p=0.006; df = (5−1) × (6−1) = 20"——numerator df 已给出为 20。R1 指出缺少 denominator df，这是对的，但 denominator df 可以从 N=2,997 和 predictor 数推算。建议作者补上但这是 trivial fix。

---

### Questions 回应

**R1-Q1 (±10 pp 下 C2 narrative)**: 好问题。Table 2 在 ±10 pp 下仅 3/6 mid-tier pairs 等价——此时 C2 应调整为 "three-tier structure"（incompleteness > auth scope + lexical > remaining）。论文应在正文中讨论 ±10 pp 下的替代 narrative。

**R1-Q2 (Instructed awareness)**: 与 W4 相关。Appendix B 的 mitigation experiment 部分回答了这个问题（添加 disambiguation instruction 后 violation 降低 8.5 pp），但没有直接报告 awareness rate 的变化。这是一个有价值的 follow-up analysis。

**R1-Q3 (Auth scope −18.0 vs incompleteness −3.4 的统计检验)**: 好问题——Appendix B 只报告了 per-type per-model Δpp，没有对 type 间差异做统计检验。n 数量也有限（每 type ~250 episodes）。如果这个差异未经检验，Discussion 中关于 P1 的 claim（"mitigation experiment supports P1"）就过强了。

**R1-Q4 (Multiple judges for auth scope)**: 合理建议。当前设计每个 agent model 只有一个 judge，对 auth scope 这种 κ 最低的 type 使用 majority vote 可以减少测量噪声。

**R1-Q5 (Judge identity confound)**: Section 4.4 明确指出 "the cross-judge asymmetry affects only absolute violation rates, not C1 or C2"——matched-pair 设计确保 within-model 比较不受 judge bias 影响。但 C4 的 cross-model 比较（DeepSeek 49.7% vs Claude 30.3%）确实受 judge identity confound 影响。论文 Limitations 中讨论了这一点，但 Q5 的核心关切是合理的。

---

### 总结评估

Reviewer 1 的审稿整体严谨且 well-calibrated。两个 Must-Fix 中：
- **N1 (SESOI)** 是有效批评但论文已有 partial mitigation（sensitivity analysis + bootstrap），建议降为 SHOULD-FIX
- **N2 (Auth scope κ)** 完全同意，与我的 N1 (taxonomy 混淆) 形成互相加强的 weakness

Should-Fix 中 W4 (Ambiguity Blindness) 最为重要，因为它影响论文的一个核心 coined term。

我与 R1 的评分一致：**Overall 3.5 (Borderline Conference)**。核心分歧在于 R1 侧重方法论问题（SESOI 选择、measurement reliability），我侧重理论基础问题（taxonomy 混淆、Differential Nocuity 增量有限）。两条线索指向同一个结论：实验执行优秀但概念框架需要加强。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 790 · 2026-05-21T17:48:07.538432+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 72

## Round 72

2 recorded events


### User

_source line 791 · 2026-05-21T17:48:10.038479+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- R1 的 2 个 Must-Fix 中，**N2（auth scope κ=0.385）** 完全同意且与我的 N1 互相加强；**N1（SESOI ±15 pp）** 同意但建议降级为 Should-Fix，因为论文已有 sensitivity analysis + margin-free bootstrap 作为 partial mitigation。
- 5 个 Should-Fix 全部同意，其中 **W4（Ambiguity Blindness 归因）** 最重要，与我的 W5 高度一致——mitigation experiment 的 −8.5 pp 改善直接反驳了 "blindness" 的 framing。
- 两位 reviewer 均给出 3.5（Borderline Conference），从不同角度（方法论 vs 理论基础）指向同一结论：实验执行优秀但概念框架需要加强。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 792 · 2026-05-21T17:48:14.499631+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 73

## Round 73

10 recorded events


### User

_source line 793 · 2026-05-21T17:49:01.001538+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 问题

### [AGREE with qualification] R2-N1: Taxonomy 混淆 ambiguity / vagueness / incompleteness

R2 指出 authorization scope 是 vagueness、incompleteness 是 information absence、conditional precedence 是 normative conflict，三者不严格属于 ambiguity。这一理论性批评有实质依据。

**同意理由**：

1. **Incompleteness 最成问题。** §3 自身承认 "resolution requires adding new policy content"，即问题不是 present text 的多义性而是 content absence。论文在 Appendix F 的 confound analysis 中也将其与其他类型区别对待，隐含承认了这一结构差异。如果最高违规率的 type（53.6%）不严格属于 ambiguity，"ambiguity type predicts severity" 这一 framing 确实存在理论张力。

2. **Conditional precedence 确实是 normative conflict。** R2 正确指出每条规则本身无歧义，问题是缺少 meta-rule。但我认为这在操作层面仍可理解为 "policy 整体在特定 scenario 下的 interpretation 不确定"——agent 面对两条冲突规则时行为确实是不确定的。

3. **Authorization scope 相对可防御。** §3 的操作定义（Wasow 2005）明确将 vagueness 纳入 ambiguity 范畴（"including cases of vagueness where the boundary between interpretations is gradient rather than discrete"），这在语言学文献中有先例。R2 引用 Kennedy (2007)，但论文已 cite 同一文献作为定义的一部分。

**但我认为 R2 的建议可能过度**：R2 提议 reframe 为 "policy specification defects"。这虽然理论上更精确，但 (a) 该 framing 失去了与 Berry & Kamsties (2004)、Massey et al. (2014) 等 ambiguity 文献的直接对话，削弱 related work 的连贯性；(b) 论文的 matched-pair design 和因果推断机制不依赖于 "ambiguity" 的严格分类——无论叫什么，六种 specification defects 导致不同违规率这一发现依然成立。

**我的建议**：选择 R2 的选项 (b)——保留 ambiguity framing，但在 §3 开头增加一段正面讨论理论张力，承认 incompleteness 和 conditional precedence 处于 ambiguity 定义的边界，并明确本文采用的是 operational/inclusive 定义。这比全面 reframe 的成本低且能回应 R2 的核心关切。

---

### [AGREE] R2-N2: Differential Nocuity 框架增量贡献不清晰

R2 的分析精准。

**同意理由**：

1. **"LLM agents 缺乏 disambiguation channels → all ambiguity nocuous" 确实是 Berry & Kamsties 2004 的直接推论。** 论文 §1 和 §7 都引用了这一逻辑链（§1: "LLM agents lack these disambiguation channels. They cannot consult colleagues..."），但将其包装为独立贡献是 overclaim。

2. **Framework 的三个因素中，只有 "ambiguity type" 有 C1+C2 的充分实验支撑。** "Safety training" 因素基于 [Exploratory] C4 和 κ=0.385 的 authorization scope（我在 R1-N2 中也指出了这一问题）。"Disambiguation channel availability" 因素基于 §6.2 的 <11% awareness rate，但正如我在 R1-W4 中指出的，这可能反映 "uninstructedness" 而非能力缺失。

3. **P1 和 P2 predictions 是 post-hoc rationalization。** P1 声称 "types with explicit decision points should show larger safety-training gains"，然后引用 Appendix B 的 mitigation experiment 作为支持（auth scope −18.0 pp vs. incompleteness −3.4 pp）。但这个 comparison 没有 formal statistical test（我在 R1 Q3 中也提出了这个问题），且 mitigation experiment 的设计目的不是 test P1。

**R2 建议将 framework 降级为 interpretive lens 是合理的。** 一个经验性观察（"不同 type 导致不同 severity"）配一个 interpretive discussion 比包装成 named framework 更诚实。如果要保留 framework 命名，至少需要展示 non-obvious predictions，例如设计实验直接 test P2（添加 disambiguation channel 对不同 type 的差异化效果）。

---

## Should-Fix 问题

### [AGREE] R2-W1: Abstract 信息过载

同意。Abstract 包含了 OR、Cramér's V、p-values、κ、logistic regression coefficient change、replication ρ 等大量统计细节。核心 message（"ambiguity causes violations, type matters more than model, agents are blind to ambiguity"）被淹没在技术指标中。我在 R1-M1 中也指出 "coefficient change < 8%" 放在 abstract 中增加了认知负担。建议将 abstract 精简到核心 narrative + 1-2 个关键数字，技术细节留在正文。

---

### [AGREE with qualification] R2-W2: C3 Layer Distinction 作为组织原则的逻辑不一致

R2 指出论文以 linguistic / specification layer 组织 taxonomy，但 C3 实验表明 layer 区分不显著。这确实是一个逻辑张力。

但我认为 R2 的替代方案（flat six-type）也不完全合理：两层组织在 §3 中有清晰的理论动机（"linguistic ambiguity can be partially resolved through tool responses, user context, or world knowledge, while specification ambiguity has no external resolution channel"）。C3 inconclusive 不等于 layer 无理论意义——它意味着 layer 的 operationalization 在本实验设计中无法被检测到，可能因为 τ²-bench 的 agent 实际上也没有外部 resolution channels 来利用。

**建议**：保留两层组织，但在 §3 末尾明确 "the layer distinction is a theoretical hypothesis, not an empirical finding of this study"，并在 §5.3 的 C3 讨论中强化这一点。这比 flat six-type 更有信息量。

---

### [AGREE] R2-W3: 与 DRIP-R 的 taxonomy 映射缺失

§2 讨论了 DRIP-R 的 3 个差异点但未提供 type-level 映射。DRIP-R 有 5 个 RE ambiguity types，本文有 6 个（3 linguistic + 3 specification）。读者无法判断哪些 types 重叠、哪些是本文新增。补充一个简短的映射表（可放 Appendix）不需要大量工作但对 reader 很有帮助。

---

### [AGREE with qualification] R2-W4: Coreferential 被系统性排除

事实确认：coreferential 被排除在 mitigation experiment（Appendix B）、detection experiment（Appendix D）、和 replication（Appendix E）之外。论文给出了每次排除的理由：
- Mitigation: 未解释为何排除（Table 3 caption 仅说 "Coreferential was excluded because it was not included in the mitigation experiment"——这是循环解释）
- Detection: "its variants are lexically identical to their unambiguous counterparts, making surface-level type detection inapplicable"（Appendix D）——合理
- Replication: "its disambiguation relies on benchmark-specific assertion structure rather than clause-level text changes"（Appendix E）——合理

核心问题是 mitigation 的排除缺乏解释。如果 6 type taxonomy 中有 1 个在 3 个 follow-up 分析中都被排除，读者有理由质疑 taxonomy 的完整性。但 detection 和 replication 的排除有技术合理性——coreferential 的特殊性（lexically identical variants）确实使其在这些分析中不可比。

**建议**：补充 mitigation 排除 coreferential 的理由，并在 Limitations 中增加一句承认 coreferential 的 follow-up 证据基础较薄弱。

---

### [AGREE] R2-W5: "Ambiguity Blindness" framing 过度

这与我在 R1-W4 中的观点一致。R2 额外指出了一个重要论点：Ferreira (2002) 的 good-enough processing 表明**人类也默认采用 single parse**，因此 agents 的行为不是 pathological 而是 default。如果人类也 "blind"（只是有社会渠道 recover），那么将 agents 的同样行为命名为 "Blindness" 暗示了一种 deficit framing，而实际上可能只是缺少 recovery mechanism。

R2 建议改为 "lack of externalized disambiguation"。我认为这更精确，也更好地与论文自身引用 Ferreira (2002) 的论述对齐（§2: "paralleling our observation that LLM agents adopt surface interpretations"）。

---

## R2 Questions 的补充意见

**Q1 (移除 3 个 specification types 后 C1/C2 是否成立)**：这是一个很好的 robustness check。如果 taxonomy 争议最终导致 specification types 被质疑（R2-N1），作者应准备好仅用 3 个 linguistic types 的分析。从 Table 1 数据推断，linguistic types 的 pooled violation rate 约 38%，与 unambiguous baseline 6.9% 相比 C1 仍应成立。C2 在 3 types 间的 differentiation 主要取决于 coreferential (31.6%) vs. lexical (42.8%) / scopal (39.4%) 的差异是否显著。

**Q2 (Template structure)**：我在 R1 审稿中未提及此问题，但 R2 的关注是合理的。§4.2 提到 "template-based pipeline" 但未描述 template 的结构和数量。如果每种 type 仅用少数 template 生成 50 个 pairs，clause-level variance 可能被 template structure 所约束，影响 generalizability。

**Q3 (Claude auth scope 12% outlier)**：这个问题我在 R1-N2 中已从 measurement reliability 角度讨论过。R2 从 judge confound 角度切入——Claude 和 DeepSeek 都由 GPT-5.4 judge 评估，但 auth scope 结果差异巨大（12% vs. 60%），说明 judge identity 不能解释该差异。但 κ=0.385 的低可靠性意味着 per-episode 判断噪声大，52 pp range 可能是 true effect + noise 的混合。论文在 §5.4 报告了 bootstrap ranking preservation (99.5%)，但 bootstrap 在同一 judge 内 resample，不能排除 judge-level systematic bias。

---

## 总结

R2 的两个 Must-Fix 中，N1（taxonomy 理论张力）是有实质性的批评，但我认为 reframing 为 "policy specification defects" 不是必要的——正面讨论理论张力即可。N2（Differential Nocuity 增量贡献）我完全同意——framework packaging 超出了实验证据的支撑范围。Should-Fix 中 W1、W3、W4、W5 我同意，W2 我部分同意但建议保留 layer 作为理论假设而非实验结论。

R2 的审稿侧重（新颖性 + 完整性）与我的侧重（方法严谨性 + 实验有效性）互补：R2 从理论 framing 角度挑战了论文的 contribution positioning，我从测量可靠性角度挑战了论文的数据支撑。两者共同指向一个一致的判断：C1 是 solid contribution，C2 合理但需要 caveat，framework-level claims 需要 downgrade。



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 794 · 2026-05-21T17:49:28.101896+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 795 · 2026-05-21T17:49:28.253421+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T17:38:45.999660+00:00\", \"completed_at\": \"2026-05-21T17:41:48.571980+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 3-5\", \"message\": \"连续 3 页纯文本无任何 display item（Related Work → Taxonomy → Method）。Section 3 描述了\\\"六类型、两层\\\"歧义分类体系，但全文主体没有对应的分类结构表或示意图。增加一个 taxonomy 表格或树形图可同时解决内容可视化和视觉节奏两个问题\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"主文最后一页（Discussion + Conclusion）为纯文本密集页，无任何视觉元素。与第 6-7 页的 figure/table 密集形成反差，整体节奏\\\"前松后紧再松\\\"\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 内部文字（box 标签、数字标注、箭头说明）字号偏小，建议放大关键数字或简化图内文字，确保打印时可读\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 使用 booktabs 风格，格式规范。部分最优值已加粗。Figure 2 条形图颜色可区分，caption 自包含\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 分组条形图展示 5 模型 × 6 类型违规率，颜色区分度良好，图例清晰。全宽 figure* 用法合理\"}, {\"severity\": \"info\", \"dimension\": \"page 1-8\", \"message\": \"主文 8 页内 4 个 display items（3 figure + 1 table），对于实证为主的论文偏少（通常 5-8 个）。Taxonomy 可视化（前述）和一个 method/data 摘要表可提升密度\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 中 \\\"Δpp\\\" 列的正负值精度统一（小数点后一位），格式一致\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 篇幅适当，涵盖模型覆盖、领域局限、合成数据等多个维度\"}, {\"severity\": \"info\", \"dimension\": \"page 10-11\", \"message\": \"参考文献格式统一，无 [?] 未解析引用，无明显截断或溢出\"}, {\"severity\": \"info\", \"dimension\": \"page 11-14\", \"message\": \"附录表格（Table 2-9）均使用 booktabs 风格，decimal 对齐，格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"末页内容约占 60-65%，底部有空白，但作为附录尾页可接受\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 9}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 796 · 2026-05-21T17:49:28.253955+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 797 · 2026-05-21T17:49:28.304642+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 798 · 2026-05-21T17:51:51.259562+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Round 9 (Fresh) Review Issues — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Date: 2026-05-21\n## Round 9 Score: 3.5 (Borderline Conference)\n## Note: Fresh review session — all issues re-evaluated from scratch\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R9-N1\"\n  summary: \"Taxonomy 将 ambiguity、vagueness、incompleteness、normative conflict 混为一谈，理论基础存在根本性混淆\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R2]\n      note: \"R2 raised as N1. Authorization scope 是 vagueness (Kennedy 2007)，incompleteness 是 information absence，conditional precedence 是 normative conflict。6 types 中 3 个不严格属于 ambiguity。R1 AGREE with qualification: incompleteness 最成问题，auth scope 可通过 Wasow 2005 操作性定义防御。两人共识：需在 §3 正面讨论理论张力。\"\n  action_items:\n    - round: 9\n      action: \"§3 增加 'Scope of ambiguity' 段落，正面讨论 ambiguity/vagueness/incompleteness 的理论边界；承认 incompleteness 和 conditional precedence 处于定义边界；明确本文采用 operational/inclusive 定义并论证合理性\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-N2\"\n  summary: \"Differential Nocuity 框架增量贡献不清晰，本质是 Berry & Kamsties 2004 的 trivial 推论\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R2, R1]\n      note: \"R2 raised as N2, R1 AGREE. 三因素中仅 'ambiguity type' 有 C1+C2 支撑；'safety training' 基于 exploratory C4 + κ=0.385；'disambiguation channel' 基于可能反映 uninstructedness 的 <11% awareness。P1/P2 是 post-hoc rationalization，P1 支持证据 (Appendix B) 无 formal statistical test。\"\n  action_items:\n    - round: 9\n      action: \"将 Differential Nocuity 从 contribution 降级为 Discussion 中的 interpretive lens；contribution (2) 重写为纯实验发现（type hierarchy + variance decomposition）；或保留 framework 但展示 non-obvious testable predictions\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-N3\"\n  summary: \"SESOI ±15pp 缺乏外部锚定，two-tier structure 在 ±10-12pp 时不稳健\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出。已添加 Anvari & Lakens 引用、bootstrap cluster analysis、承认 margin dependence。\"\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1 raised as N1 (MUST-FIX). R2 AGREE but suggests downgrade to SHOULD-FIX — incompleteness upper bound robust at all margins, only mid-tier clustering is margin-sensitive. Paper already has sensitivity analysis (Table 2) + bootstrap (Appendix I, AU p=0.47). Consensus: external anchor still needed, but partial mitigation acknowledged.\"\n  action_items:\n    - round: 8\n      action: \"已完成: domain-relevant anchor 语言, Anvari & Lakens 引用, Ward's bootstrap cluster, margin dependence 承认\"\n      assigned_to: author\n      status: in_progress\n    - round: 9\n      action: \"提供 deployment-scenario 外部依据（如 SLA 容忍度、行业 benchmark）；正文更显著呈现 ±10pp 替代 narrative（three-tier 而非 two-tier）；考虑将 'two-tier hierarchy' 措辞软化为 'one plausible clustering'\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-N4\"\n  summary: \"Authorization scope κ=0.385 过低，C4 'model-differentiating type' 声称可信度不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出。已降级 C4 为 suggestive，添加 bootstrap ranking stability，Abstract 添加 κ 注释。\"\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1 raised as N2 (MUST-FIX). R2 AGREE and reinforces: within-judge bootstrap (99.5%) 不能排除 judge-level systematic bias；human-LLM κ=0.644 CI lower bound 仅 0.35。两人共识：C4 的 auth scope narrative 和 Discussion 中 safety training 推测过于确定，与 'suggestive' hedging 不匹配。\"\n  action_items:\n    - round: 8\n      action: \"已完成: C4 降级为 suggestive, bootstrap ranking stability, Abstract κ 注释\"\n      assigned_to: author\n      status: in_progress\n    - round: 9\n      action: \"C4 正文加入 'auth scope range should be interpreted as upper bound on true between-model variance'；Abstract '52 pp' 附带 measurement uncertainty；验证 per-type range 在 moderate+ vs any-violation 下的稳定性；考虑 majority vote from multiple judges\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R9-W1\"\n  summary: \"Ambiguity Blindness framing 过度——可能反映 uninstructed default behavior 而非 inability\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1-W4 + R2-W5 独立提出，交叉回应中互相强化。Mitigation experiment −8.5pp 改善直接反驳 blindness。人类也默认 good-enough single parse (Ferreira 2002)，agents 行为不是 pathological。两人共识：改为 'lack of externalized disambiguation' 或 'Uninstructed Disambiguation Deficit'。\"\n  action_items:\n    - round: 9\n      action: \"重新定义 Ambiguity Blindness 为 'lack of externalized disambiguation'；讨论 uninstructed vs blind 区分；引用 Liu et al. 2023 更精确定位\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W2\"\n  summary: \"Abstract 信息过载，核心 message 被统计细节淹没\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R2-W1 raised, R1 AGREE (also R1-M1 re 'coefficient change <8%'). Abstract 包含 OR、V、κ、p、regression coefficient 等大量数字，读起来像 Results 压缩版。\"\n  action_items:\n    - round: 9\n      action: \"Abstract 重构为 problem→approach→key findings (2-3 highlights)→implication 叙事结构；精简到 2-3 个最有冲击力的数字，其余留正文\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W3\"\n  summary: \"C3 Layer Distinction 未通过校正但仍作为 taxonomy 组织原则\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R2, R1]\n      note: \"R2-W2 raised. R1 AGREE with qualification: layer 有理论动机，C3 inconclusive 可能因为 τ²-bench agents 也没有外部 resolution channels。两人共识：保留 layer 组织但在 §3 末明确 'layer distinction is a theoretical hypothesis, not an empirical finding'。\"\n  action_items:\n    - round: 9\n      action: \"§3 末尾和 §5.3 明确 layer 是理论假设而非本研究的实验发现\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W4\"\n  summary: \"Token count 作为 information content proxy 未验证有效性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1-W1 raised, R2 AGREE but notes partial mitigation: coefficient change <8% means proxy imperfection has limited impact; coreferential (delta=0) is confound-free lower bound.\"\n  action_items:\n    - round: 9\n      action: \"讨论 token count 作为 proxy 的局限性；考虑补充替代度量（semantic information units）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W5\"\n  summary: \"Human validation 样本量偏小（100/2997），per-type CI 极宽\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出 (R8-W3)。已在 Limitations 新增 per-type reliability 段落。\"\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1-W2 raised, R2 AGREE. §4.4 正文呈现仍过于乐观（强调 pooled κ=0.733 而淡化 per-type 不稳定性）。Scopal CI [0.00, 1.00] 本质上 uninformative。\"\n  action_items:\n    - round: 9\n      action: \"§4.4 更显著呈现 per-type CI 宽度；增加 human validation 样本量（尤其 auth scope 和 coreferential）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W6\"\n  summary: \"Cross-provider ICC 缺乏直接度量（仅 within OpenAI family）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出 (R8-W2)。已明确 ICC 限于 OpenAI family。\"\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1-W3 raised, R2 AGREE. LLaMA Δ=+20pp 远小于主研究 range (+25.7-39.0pp)，暗示跨 provider effect 受 baseline instruction-following quality 调节。\"\n  action_items:\n    - round: 9\n      action: \"计算跨 provider type-ranking concordance（Kendall's W）作为补充\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W7\"\n  summary: \"多重比较校正 'three test families' 未明确定义\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1-W5 raised, R2 AGREE. §4.6 未列出三个 families 的成员，读者无法验证校正适当性。\"\n  action_items:\n    - round: 9\n      action: \"正文或附录显式列出三个 test families 及其成员，报告 corrected p-values\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W8\"\n  summary: \"与 DRIP-R 的 taxonomy type-level 映射缺失\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R2, R1]\n      note: \"R2-W3 raised, R1 AGREE. DRIP-R 有 5 个 RE ambiguity types，本文 6 个，未提供显式映射。\"\n  action_items:\n    - round: 9\n      action: \"§2 或 §3 增加与 DRIP-R 的 type-level 映射（一段文字或脚注）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W9\"\n  summary: \"Coreferential 被系统性排除在 mitigation/detection/replication 之外\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R2, R1]\n      note: \"R2-W4 raised, R1 AGREE with qualification. Detection 和 replication 排除有技术合理性（lexically identical variants）。但 mitigation 排除理由为循环解释。\"\n  action_items:\n    - round: 9\n      action: \"补充 mitigation 排除 coreferential 的理由；Limitations 承认 coreferential follow-up 证据基础薄弱\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# PREVIOUSLY RESOLVED (from Round 8)\n# ============================================================\n\n- id: \"R8-W1-resolved\"\n  summary: \"缺少 API 超参数报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出\"\n    - round: 9\n      reviewers: []\n      note: \"已修复：§4.3 now reports temperature=0, top_p=1, max_tokens=4096。本轮未被任何 Reviewer 提及。\"\n  resolution: \"§4.3 添加完整 API 超参数\"\n  resolution_round: 9\n\n- id: \"R8-W4-resolved\"\n  summary: \"无代码/数据可用性声明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出\"\n    - round: 9\n      reviewers: []\n      note: \"已修复：Limitations 后添加 'Data and Code Availability' section。本轮未被任何 Reviewer 提及。\"\n  resolution: \"添加 Data and Code Availability section\"\n  resolution_round: 9\n\n- id: \"R8-W5-resolved\"\n  summary: \"Clause-level heterogeneity 未充分分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出\"\n    - round: 9\n      reviewers: []\n      note: \"已修复：新增 Appendix I (LOO range ≤2.1pp, max shift 1.4pp)。本轮未被任何 Reviewer 提及。\"\n  resolution: \"新增 Appendix I Clause-Level Variance 分析\"\n  resolution_round: 9\n\n- id: \"R8-W6-resolved\"\n  summary: \"人工标注者是否对 ambiguity condition 设盲未说明\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出\"\n    - round: 9\n      reviewers: []\n      note: \"已修复：§4.4 改为 'blind to both LLM judge labels and ambiguity condition'。本轮未被任何 Reviewer 提及。\"\n  resolution: \"§4.4 明确双盲设计\"\n  resolution_round: 9\n\n- id: \"R8-W9-resolved\"\n  summary: \"4 条 orphan bib + missing references\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出\"\n    - round: 9\n      reviewers: []\n      note: \"已修复：删除 4 条 orphan，添加 Zheng et al. 2024 和 Anvari & Lakens 2021。R2 格式检查确认 0 orphan entries。\"\n  resolution: \"清理 orphan bib entries，添加遗漏引用\"\n  resolution_round: 9\n\n# ============================================================\n# MINOR ISSUES\n# ============================================================\n\n- id: \"R9-M1\"\n  summary: \"ferrari_defects_2018 bib key 与实际一作 (Rosadini) 不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出 (R8-M1)\"\n    - round: 9\n      reviewers: [R2]\n      note: \"R2 再次标记。Bib key 'ferrari_defects_2018' 但一作为 Rosadini。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M2\"\n  summary: \"navigli_wsd_2009 年份/作者可能有误\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R2]\n      note: \"R2 发现 OpenAlex 显示 year mismatch (bib 2009 vs API 2015)。可能匹配不同版本。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M3\"\n  summary: \"Introduction 'seven models' 措辞应区分 main study (5) vs replication (2)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R2]\n      note: \"Contribution (1) 写 'replicated across seven models' 但主实验只有 5 个。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M4\"\n  summary: \"Figure 1 内部标注字体偏小，cross-judge 流程箭头不清晰\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1-M3 + R2 minor + 视觉审查均标记。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M5\"\n  summary: \"§5.2 'stabilizes at ±15pp' 措辞暗示自然 breakpoint，实为 ceiling\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R1]\n      note: \"R1-M2. Table 2 显示 ±15pp 是 6/6 mid-tier 等价的第一个 margin。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M6\"\n  summary: \"§6.1 Gwet's AC₁ vs Cohen's κ 差异应在正文解释 prevalence paradox\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1-M4, R2 AGREE. 当前仅有 parenthetical mention。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M7\"\n  summary: \"§5.4 F(20)=1.97 缺少 denominator df\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R1]\n      note: \"R1-M6. R2 REBUT: trivial fix, denominator computable from N=2997.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M8\"\n  summary: \"Pages 3-5 连续纯文本无 display item，缺少 taxonomy 可视化\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"视觉审查发现。Related Work → Taxonomy → Method 三页无图表。建议增加 taxonomy 表格或树形图。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Round 9 (Fresh) Review Issues — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Date: 2026-05-21\n## Round 9 Score: 3.5 (Borderline Conference)\n## Note: Fresh review session — all issues re-evaluated from scratch\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R9-N1\"\n  summary: \"Taxonomy 将 ambiguity、vagueness、incompleteness、normative conflict 混为一谈，理论基础存在根本性混淆\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R2]\n      note: \"R2 raised as N1. Authorization scope 是 vagueness (Kennedy 2007)，incompleteness 是 information absence，conditional precedence 是 normative conflict。6 types 中 3 个不严格属于 ambiguity。R1 AGREE with qualification: incompleteness 最成问题，auth scope 可通过 Wasow 2005 操作性定义防御。两人共识：需在 §3 正面讨论理论张力。\"\n  action_items:\n    - round: 9\n      action: \"§3 增加 'Scope of ambiguity' 段落，正面讨论 ambiguity/vagueness/incompleteness 的理论边界；承认 incompleteness 和 conditional precedence 处于定义边界；明确本文采用 operational/inclusive 定义并论证合理性\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-N2\"\n  summary: \"Differential Nocuity 框架增量贡献不清晰，本质是 Berry & Kamsties 2004 的 trivial 推论\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R2, R1]\n      note: \"R2 raised as N2, R1 AGREE. 三因素中仅 'ambiguity type' 有 C1+C2 支撑；'safety training' 基于 exploratory C4 + κ=0.385；'disambiguation channel' 基于可能反映 uninstructedness 的 <11% awareness。P1/P2 是 post-hoc rationalization，P1 支持证据 (Appendix B) 无 formal statistical test。\"\n  action_items:\n    - round: 9\n      action: \"将 Differential Nocuity 从 contribution 降级为 Discussion 中的 interpretive lens；contribution (2) 重写为纯实验发现（type hierarchy + variance decomposition）；或保留 framework 但展示 non-obvious testable predictions\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-N3\"\n  summary: \"SESOI ±15pp 缺乏外部锚定，two-tier structure 在 ±10-12pp 时不稳健\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出。已添加 Anvari & Lakens 引用、bootstrap cluster analysis、承认 margin dependence。\"\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1 raised as N1 (MUST-FIX). R2 AGREE but suggests downgrade to SHOULD-FIX — incompleteness upper bound robust at all margins, only mid-tier clustering is margin-sensitive. Paper already has sensitivity analysis (Table 2) + bootstrap (Appendix I, AU p=0.47). Consensus: external anchor still needed, but partial mitigation acknowledged.\"\n  action_items:\n    - round: 8\n      action: \"已完成: domain-relevant anchor 语言, Anvari & Lakens 引用, Ward's bootstrap cluster, margin dependence 承认\"\n      assigned_to: author\n      status: in_progress\n    - round: 9\n      action: \"提供 deployment-scenario 外部依据（如 SLA 容忍度、行业 benchmark）；正文更显著呈现 ±10pp 替代 narrative（three-tier 而非 two-tier）；考虑将 'two-tier hierarchy' 措辞软化为 'one plausible clustering'\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-N4\"\n  summary: \"Authorization scope κ=0.385 过低，C4 'model-differentiating type' 声称可信度不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出。已降级 C4 为 suggestive，添加 bootstrap ranking stability，Abstract 添加 κ 注释。\"\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1 raised as N2 (MUST-FIX). R2 AGREE and reinforces: within-judge bootstrap (99.5%) 不能排除 judge-level systematic bias；human-LLM κ=0.644 CI lower bound 仅 0.35。两人共识：C4 的 auth scope narrative 和 Discussion 中 safety training 推测过于确定，与 'suggestive' hedging 不匹配。\"\n  action_items:\n    - round: 8\n      action: \"已完成: C4 降级为 suggestive, bootstrap ranking stability, Abstract κ 注释\"\n      assigned_to: author\n      status: in_progress\n    - round: 9\n      action: \"C4 正文加入 'auth scope range should be interpreted as upper bound on true between-model variance'；Abstract '52 pp' 附带 measurement uncertainty；验证 per-type range 在 moderate+ vs any-violation 下的稳定性；考虑 majority vote from multiple judges\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R9-W1\"\n  summary: \"Ambiguity Blindness framing 过度——可能反映 uninstructed default behavior 而非 inability\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1-W4 + R2-W5 独立提出，交叉回应中互相强化。Mitigation experiment −8.5pp 改善直接反驳 blindness。人类也默认 good-enough single parse (Ferreira 2002)，agents 行为不是 pathological。两人共识：改为 'lack of externalized disambiguation' 或 'Uninstructed Disambiguation Deficit'。\"\n  action_items:\n    - round: 9\n      action: \"重新定义 Ambiguity Blindness 为 'lack of externalized disambiguation'；讨论 uninstructed vs blind 区分；引用 Liu et al. 2023 更精确定位\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W2\"\n  summary: \"Abstract 信息过载，核心 message 被统计细节淹没\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R2-W1 raised, R1 AGREE (also R1-M1 re 'coefficient change <8%'). Abstract 包含 OR、V、κ、p、regression coefficient 等大量数字，读起来像 Results 压缩版。\"\n  action_items:\n    - round: 9\n      action: \"Abstract 重构为 problem→approach→key findings (2-3 highlights)→implication 叙事结构；精简到 2-3 个最有冲击力的数字，其余留正文\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W3\"\n  summary: \"C3 Layer Distinction 未通过校正但仍作为 taxonomy 组织原则\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R2, R1]\n      note: \"R2-W2 raised. R1 AGREE with qualification: layer 有理论动机，C3 inconclusive 可能因为 τ²-bench agents 也没有外部 resolution channels。两人共识：保留 layer 组织但在 §3 末明确 'layer distinction is a theoretical hypothesis, not an empirical finding'。\"\n  action_items:\n    - round: 9\n      action: \"§3 末尾和 §5.3 明确 layer 是理论假设而非本研究的实验发现\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W4\"\n  summary: \"Token count 作为 information content proxy 未验证有效性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1-W1 raised, R2 AGREE but notes partial mitigation: coefficient change <8% means proxy imperfection has limited impact; coreferential (delta=0) is confound-free lower bound.\"\n  action_items:\n    - round: 9\n      action: \"讨论 token count 作为 proxy 的局限性；考虑补充替代度量（semantic information units）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W5\"\n  summary: \"Human validation 样本量偏小（100/2997），per-type CI 极宽\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出 (R8-W3)。已在 Limitations 新增 per-type reliability 段落。\"\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1-W2 raised, R2 AGREE. §4.4 正文呈现仍过于乐观（强调 pooled κ=0.733 而淡化 per-type 不稳定性）。Scopal CI [0.00, 1.00] 本质上 uninformative。\"\n  action_items:\n    - round: 9\n      action: \"§4.4 更显著呈现 per-type CI 宽度；增加 human validation 样本量（尤其 auth scope 和 coreferential）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W6\"\n  summary: \"Cross-provider ICC 缺乏直接度量（仅 within OpenAI family）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出 (R8-W2)。已明确 ICC 限于 OpenAI family。\"\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1-W3 raised, R2 AGREE. LLaMA Δ=+20pp 远小于主研究 range (+25.7-39.0pp)，暗示跨 provider effect 受 baseline instruction-following quality 调节。\"\n  action_items:\n    - round: 9\n      action: \"计算跨 provider type-ranking concordance（Kendall's W）作为补充\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W7\"\n  summary: \"多重比较校正 'three test families' 未明确定义\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1-W5 raised, R2 AGREE. §4.6 未列出三个 families 的成员，读者无法验证校正适当性。\"\n  action_items:\n    - round: 9\n      action: \"正文或附录显式列出三个 test families 及其成员，报告 corrected p-values\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W8\"\n  summary: \"与 DRIP-R 的 taxonomy type-level 映射缺失\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R2, R1]\n      note: \"R2-W3 raised, R1 AGREE. DRIP-R 有 5 个 RE ambiguity types，本文 6 个，未提供显式映射。\"\n  action_items:\n    - round: 9\n      action: \"§2 或 §3 增加与 DRIP-R 的 type-level 映射（一段文字或脚注）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W9\"\n  summary: \"Coreferential 被系统性排除在 mitigation/detection/replication 之外\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R2, R1]\n      note: \"R2-W4 raised, R1 AGREE with qualification. Detection 和 replication 排除有技术合理性（lexically identical variants）。但 mitigation 排除理由为循环解释。\"\n  action_items:\n    - round: 9\n      action: \"补充 mitigation 排除 coreferential 的理由；Limitations 承认 coreferential follow-up 证据基础薄弱\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# PREVIOUSLY RESOLVED (from Round 8)\n# ============================================================\n\n- id: \"R8-W1-resolved\"\n  summary: \"缺少 API 超参数报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出\"\n    - round: 9\n      reviewers: []\n      note: \"已修复：§4.3 now reports temperature=0, top_p=1, max_tokens=4096。本轮未被任何 Reviewer 提及。\"\n  resolution: \"§4.3 添加完整 API 超参数\"\n  resolution_round: 9\n\n- id: \"R8-W4-resolved\"\n  summary: \"无代码/数据可用性声明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出\"\n    - round: 9\n      reviewers: []\n      note: \"已修复：Limitations 后添加 'Data and Code Availability' section。本轮未被任何 Reviewer 提及。\"\n  resolution: \"添加 Data and Code Availability section\"\n  resolution_round: 9\n\n- id: \"R8-W5-resolved\"\n  summary: \"Clause-level heterogeneity 未充分分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出\"\n    - round: 9\n      reviewers: []\n      note: \"已修复：新增 Appendix I (LOO range ≤2.1pp, max shift 1.4pp)。本轮未被任何 Reviewer 提及。\"\n  resolution: \"新增 Appendix I Clause-Level Variance 分析\"\n  resolution_round: 9\n\n- id: \"R8-W6-resolved\"\n  summary: \"人工标注者是否对 ambiguity condition 设盲未说明\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出\"\n    - round: 9\n      reviewers: []\n      note: \"已修复：§4.4 改为 'blind to both LLM judge labels and ambiguity condition'。本轮未被任何 Reviewer 提及。\"\n  resolution: \"§4.4 明确双盲设计\"\n  resolution_round: 9\n\n- id: \"R8-W9-resolved\"\n  summary: \"4 条 orphan bib + missing references\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出\"\n    - round: 9\n      reviewers: []\n      note: \"已修复：删除 4 条 orphan，添加 Zheng et al. 2024 和 Anvari & Lakens 2021。R2 格式检查确认 0 orphan entries。\"\n  resolution: \"清理 orphan bib entries，添加遗漏引用\"\n  resolution_round: 9\n\n# ============================================================\n# MINOR ISSUES\n# ============================================================\n\n- id: \"R9-M1\"\n  summary: \"ferrari_defects_2018 bib key 与实际一作 (Rosadini) 不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [R1, R2]\n      note: \"Round 8 首次提出 (R8-M1)\"\n    - round: 9\n      reviewers: [R2]\n      note: \"R2 再次标记。Bib key 'ferrari_defects_2018' 但一作为 Rosadini。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M2\"\n  summary: \"navigli_wsd_2009 年份/作者可能有误\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R2]\n      note: \"R2 发现 OpenAlex 显示 year mismatch (bib 2009 vs API 2015)。可能匹配不同版本。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M3\"\n  summary: \"Introduction 'seven models' 措辞应区分 main study (5) vs replication (2)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R2]\n      note: \"Contribution (1) 写 'replicated across seven models' 但主实验只有 5 个。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M4\"\n  summary: \"Figure 1 内部标注字体偏小，cross-judge 流程箭头不清晰\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1-M3 + R2 minor + 视觉审查均标记。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M5\"\n  summary: \"§5.2 'stabilizes at ±15pp' 措辞暗示自然 breakpoint，实为 ceiling\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R1]\n      note: \"R1-M2. Table 2 显示 ±15pp 是 6/6 mid-tier 等价的第一个 margin。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M6\"\n  summary: \"§6.1 Gwet's AC₁ vs Cohen's κ 差异应在正文解释 prevalence paradox\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R1-M4, R2 AGREE. 当前仅有 parenthetical mention。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M7\"\n  summary: \"§5.4 F(20)=1.97 缺少 denominator df\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [R1]\n      note: \"R1-M6. R2 REBUT: trivial fix, denominator computable from N=2997.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M8\"\n  summary: \"Pages 3-5 连续纯文本无 display item，缺少 taxonomy 可视化\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"视觉审查发现。Related Work → Taxonomy → Method 三页无图表。建议增加 taxonomy 表格或树形图。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 799 · 2026-05-21T17:51:51.360905+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 15628}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 800 · 2026-05-21T17:54:23.144079+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "\n# 审稿报告 — Round 9 (Fresh Review)\n\n**论文**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 via ARR May cycle (deadline: 2026-05-25)\n**Reviewer 编排**: R1（方法严谨性 + 实验有效性）、R2（新颖性 + 完整性）\n**审稿模式**: Fresh（无上轮记忆）\n**交叉回应**: 完成，关键问题全部达成共识\n\n---\n\n## Summary\n\n本文通过 matched-pair 实验设计，在 τ²-bench 上测量六类 policy ambiguity 对 LLM agent 安全违规的因果影响。构建 300 对条款（ambiguous vs. unambiguous），覆盖六类型双层歧义分类体系，在 5 个模型上运行 2,997 episodes，并在额外 2 个模型上做 replication。核心发现：(C1) 歧义条款使违规率增加 34.0 pp (OR=15.1)；(C2) 类型间存在显著层次结构 (Cramér's V=0.137)，呈两层模式；(C3) specification vs. linguistic 层级区分不显著（inconclusive）；(C4, exploratory) model×type 交互显著但解释方差仅 2.9%。论文还报告了 \"Ambiguity Blindness\"（<11% disambiguation awareness）和三种 type-specific failure mechanisms。\n\n---\n\n## Strengths\n\n**S1. 因果设计是该领域首创。** Matched-pair design + perturbation control (Δ_perturb = −0.67 pp, CI containing zero) 在 agent safety 文献中首次建立了 policy ambiguity → safety violation 的因果关系。DRIP-R 做相关分析，PolicyBank 做迭代改进，本文是第一个因果推断工作。7 个模型跨 6 个 provider 的 replication 进一步增强外部效度。[R1-S1, R2-S1, 共识]\n\n**S2. Confound 处理和透明度出色。** Incompleteness 的 information-addition confound 在 §3（taxonomy 定义）就主动指出，§5.2 讨论，Appendix F/H 提供 logistic regression 控制 (p=0.022, coefficient change <8%) 和 coreferential confound-free lower bound (31.6%)。TOST sensitivity across 7 margins、bootstrap cluster analysis、clause-level LOO variance、severity threshold comparison 构成多角度 robustness 检验。[R1-S2/S4, R2-S2, 共识]\n\n**S3. Claims 标注层次清晰。** C1 (primary, well-supported) → C2 (primary, with caveats) → C3 (inconclusive) → C4 (exploratory) 的递进标注避免了 overclaim，C3 如实报告为 inconclusive 是良好科学实践。[R1-S3, R2-S4, 共识]\n\n**S4. Type > Model 的方差分解有实际价值。** Type 解释 22.4% variance vs. model 仅 1.0%，意味着 policy auditing 应以 type 为导向而非 model 为导向。Detection experiment (binary F1=0.81) 和 mitigation experiment 展示了 pipeline 原型。[R1-S5, R2-S3, 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. Taxonomy 将 ambiguity、vagueness、incompleteness、normative conflict 混为一谈。** [R2 raised, R1 AGREE with qualification]\n\n六类型中三个不严格属于 ambiguity：authorization scope 是 vagueness (Kennedy 2007)，incompleteness 是 information absence（论文自身承认 \"resolution requires adding new policy content\"），conditional precedence 是 normative conflict（每条规则本身无歧义）。Wasow (2005) 的操作性定义虽将 vagueness 纳入范畴，但 incompleteness 和 conditional precedence 不在该定义的自然覆盖范围内。\n\n如果最高违规率的 type (incompleteness, 53.6%) 不严格属于 ambiguity，\"ambiguity type predicts severity\" 的核心 framing 存在理论张力。\n\n两位 Reviewer 共识的修改方向：保留 ambiguity framing，但 §3 需增加 \"Scope of 'ambiguity'\" 段落，正面讨论理论边界，承认 incompleteness 和 conditional precedence 处于定义边界，明确论证为何 operational/inclusive 定义在 LLM agent 场景下合理。\n\n**N2. Differential Nocuity 框架的增量贡献不清晰。** [R2 raised, R1 AGREE]\n\n框架声称 risk = f(ambiguity type, safety training, disambiguation channel availability)。但：\n- \"LLM agents 缺乏 disambiguation channels → 所有 ambiguity 都 nocuous\" 是 Berry & Kamsties (2004) 的直接推论\n- 三因素中仅 \"ambiguity type\" 有 C1+C2 充分支撑；\"safety training\" 基于 [Exploratory] C4 + κ=0.385 的 authorization scope；\"disambiguation channel\" 基于可能反映 uninstructedness 的 <11% awareness\n- P1/P2 predictions 是 post-hoc rationalization，P1 支持证据 (Appendix B: auth scope −18.0 vs incompleteness −3.4) 无 formal statistical test\n\n两位 Reviewer 共识：将 Differential Nocuity 从 contribution 降级为 Discussion 中的 interpretive lens，或展示 non-obvious testable predictions with adequate statistical support。\n\n**N3. SESOI ±15 pp 缺乏外部锚定。** [R1 raised as MUST-FIX, R2 AGREE but suggests SHOULD-FIX]\n\n±15 pp 的理由是主观的 deployment-relevance 判断和 perturbation control bound 的 2× 倍数（循环论证）。±10 pp 时仅 3/6 mid-tier pairs 等价 (Table 2)，TOST power 降至 0.57。Bootstrap cluster AU p-value = 0.47 表明 incompleteness singleton 边界不尖锐。\n\n**Reviewer 分歧**：R1 认为 MUST-FIX，R2 认为论文已有 partial mitigation（sensitivity analysis + bootstrap cluster 作为 margin-free 补充；incompleteness upper bound 在所有 margin 下成立），建议降为 SHOULD-FIX。\n\nDirector 判断：incompleteness 作为 upper bound 的核心 finding 稳健，但 mid-tier clustering 对 margin 敏感。需要外部锚定和更显著的 sensitivity 呈现，但不 invalidate C2 整体。严重程度介于两位 Reviewer 判断之间。\n\n**N4. Authorization scope κ=0.385 下 C4 结论可信度不足。** [R1 raised, R2 AGREE]\n\nCross-judge κ=0.385 仅为 fair agreement，human-LLM κ=0.644 CI=[0.35, 0.91] lower bound 极低。然而 C4 Discussion 从这个 noisy measurement 推导出 safety training differential mitigation 叙事。Within-judge bootstrap (99.5%) 不能排除 judge-level systematic bias。Introduction contribution (2) 和 Abstract 中的表述与正文 \"suggestive\" hedging 不匹配。\n\n两位 Reviewer 共识：52 pp range 应标注为 \"upper bound on true between-model variance\"；Abstract 需附带 measurement uncertainty qualification。此问题与 N1 (taxonomy 混淆) 互相加强——authorization scope 同时存在理论定义争议和测量可靠性问题。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. \"Ambiguity Blindness\" framing 过度。** [R1-W4 + R2-W5, 共识]\n\n<11% awareness 反映 uninstructed default behavior 而非 inability。Mitigation experiment −8.5 pp 改善直接反驳 blindness framing（agents CAN respond when prompted）。人类也默认采用 good-enough single parse (Ferreira 2002)。建议改为 \"lack of externalized disambiguation\"。\n\n**W2. Abstract 信息过载。** [R2-W1, R1 AGREE]\n\nOR、V、κ、p-values、logistic regression coefficient change 等大量数字淹没核心 message。建议精简为 problem→approach→2-3 key findings→implication 结构。\n\n**W3. C3 layer distinction 与 taxonomy 组织原则的逻辑张力。** [R2-W2, R1 AGREE with qualification]\n\nC3 未通过 Holm-Bonferroni 校正但 taxonomy 仍以 linguistic/specification layer 为组织原则。R1 认为保留 layer 但标注为 hypothesis 是更好的方案（比 flat six-type 更有信息量）。建议 §3 末和 §5.3 明确 \"layer distinction is a theoretical hypothesis, not an empirical finding\"。\n\n**W4. Token count 作为 information content proxy 未验证。** [R1-W1, R2 AGREE]\n\nLogistic regression 使用 token count difference 作为 information content 代理变量，未讨论 content validity 或尝试替代度量。R2 指出 partial mitigation: coefficient change <8% 限制了 proxy 不完美性的影响。\n\n**W5. Human validation 样本偏小，per-type CI 极宽。** [R1-W2, R2 AGREE]\n\n100/2997 (3.3%)，per-type n=32-34，scopal CI [0.00, 1.00] 本质上 uninformative。§4.4 正文呈现过于乐观（强调 pooled κ=0.733 而淡化 per-type 不稳定性）。\n\n**W6. Cross-provider ICC 缺乏直接度量。** [R1-W3, R2 AGREE]\n\nICC=0.919 仅 within OpenAI family。LLaMA Δ=+20 pp 远小于主研究 range (+25.7–39.0 pp)，暗示跨 provider effect 可能受 baseline instruction-following quality 调节。\n\n**W7. 多重比较校正 \"three test families\" 未定义。** [R1-W5, R2 AGREE]\n\n§4.6 未列出成员，读者无法验证校正适当性。\n\n**W8. 与 DRIP-R 的 type-level 映射缺失。** [R2-W3, R1 AGREE]\n\nDRIP-R 有 5 个 RE ambiguity types，本文 6 个，未提供显式映射。\n\n**W9. Coreferential 被系统性排除在 3 个 follow-up 分析之外。** [R2-W4, R1 AGREE with qualification]\n\nDetection 和 replication 排除有技术合理性（lexically identical variants），但 mitigation 排除理由缺失（Appendix B caption 为循环解释）。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n- R1-N2 / R2 auth scope κ 问题 → C4 narrative 需 heavily caveat\n- R2-N2 / R1 Differential Nocuity 增量 → 应降级为 interpretive lens\n- Ambiguity Blindness → 应改为 lack of externalized disambiguation\n- Abstract 信息过载 → 需重构叙事\n- 多重比较校正不透明 → 需显式列出 test families\n- DRIP-R mapping 缺失 → 需补充\n- Coreferential exclusion → mitigation 排除理由需补充\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | Director 判断 |\n|------|-----|-----|--------------|\n| N3 SESOI severity | MUST-FIX | SHOULD-FIX (partial mitigation) | 介于两者之间：mid-tier clustering 确实 margin-sensitive，但 incompleteness upper bound 稳健 |\n| N1 Taxonomy: 修改方案 | Option (b): 保留 framing + 讨论张力 | Option (a) preferred: reframe to \"policy specification defects\" | 倾向 R1 方案：保留 ambiguity framing + 正面讨论理论张力，成本更低且可行 |\n| W3 C3 layer: 修改方案 | 保留 layer 作为 hypothesis | 改为 flat six-type | 倾向 R1：保留 layer 但明确标注为 hypothesis |\n\n---\n\n## Questions for Authors\n\n1. **[高优先级]** §3 Taxonomy: 如何回应 authorization scope = vagueness、incompleteness = information absence、conditional precedence = normative conflict 的理论质疑？是否愿意增加 \"Scope of 'ambiguity'\" 段落正面讨论？\n2. **[高优先级]** Differential Nocuity 框架中，P1 (auth scope −18.0 vs incompleteness −3.4 pp) 是否经过 formal statistical test？如果没有，Discussion 中 \"mitigation experiment supports P1\" 的 claim 是否应弱化？\n3. **[高优先级]** 如果使用 ±10 pp 作为 SESOI，C2 narrative 如何调整？mid-tier 变为 three-tier 结构是否影响核心结论？\n4. 移除 3 个 specification-layer types 后，仅用 linguistic types 的 C1/C2 是否仍然成立？\n5. Clause pairs 的 template-based pipeline 具体使用多少 templates per type？template 结构如何影响 clause-level variance？\n6. 是否尝试过在 system prompt 中要求 agents flag ambiguity？如果有，awareness rate 从 4.6% 提升到多少？\n7. Claude auth scope 12% vs GPT-5.4 64% — 两者均由 GPT-5.4 judge 评估，排除了 judge identity confound。但 κ=0.385 下 per-episode 噪声大——52 pp range 中真实 model difference 占比多少？\n\n---\n\n## Missing References\n\n两位 Reviewer 共同建议：\n- **Zheng et al. (2024)** \"Judging LLM-as-a-Judge\" — 与 §4.4 cross-judge design 直接相关 [已引用，确认]\n- **Anvari & Lakens (2021)** — TOST SESOI 选择的方法论文献 [已引用，确认]\n\nR1 建议：\n- Tamkin et al. (2023) — policy-governed decision-making\n- Pan et al. (2024) — LLM ambiguity following behavior\n- Karpinska & Iyyer (2023) — LLM contextual ambiguity processing\n\nR2 建议：\n- SafeAgentBench (Yin et al., 2025) — embodied agent safety\n- AgentHarm (Andriushchenko et al., 2024) — agent misuse benchmark\n- Deontic logic / normative conflict literature (Prakken & Sartor) — conditional precedence 理论基础\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 external_review.paperreview_ai.enabled）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2 warnings, 9 info）。主要发现：\n\n- **[Warning]** Pages 3-5 连续 3 页纯文本（Related Work → Taxonomy → Method），无任何 display item。Section 3 描述六类型分类体系但缺少对应的分类表格或树形图。建议增加 taxonomy 可视化。\n- **[Warning]** Page 8（Discussion + Conclusion）为纯文本密集页，与 pages 6-7 的 figure/table 密集形成反差，整体节奏 \"前松后紧再松\"。\n- **[Info]** Figure 1 内部标注字体偏小，打印时可能不可读。\n- **[Info]** 主文 8 页内 4 个 display items (3 figure + 1 table)，对实证论文偏少（通常 5-8 个）。\n- **[Info]** Table 1 格式规范（booktabs），Figure 2/3 颜色区分度良好。\n- **[Info]** Limitations 篇幅适当，参考文献格式统一无未解析引用。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 — Borderline Conference**\n\n**置信度: 4/5**（两位 Reviewer 分别熟悉因果推断/agent safety 和 CL ambiguity/RE 文献）\n\n**理由**：\n\n实验执行达到 conference 标准：matched-pair causal design 是 agent safety 领域首创，C1 (+34 pp, OR=15.1) 因果效应在 7 个模型上 replicated，统计方法严谨透明，confound 处理和 claims 标注层次清晰。Type > Model 的方差分解 (22:1) 有直接部署指导意义。\n\n但概念框架存在根本性张力：(1) taxonomy 将 ambiguity、vagueness、information absence、normative conflict 混为一谈，核心 framing \"ambiguity type predicts severity\" 的理论基础被削弱；(2) Differential Nocuity 框架的增量贡献有限，本质是既有理论在 LLM 场景下的直接推论加上 exploratory 实验发现的包装；(3) authorization scope 同时存在理论定义争议 (vagueness) 和测量可靠性问题 (κ=0.385)，使得关于该 type 的所有 claim 都需 heavily caveat。\n\n修复路径明确：(a) §3 正面讨论 taxonomy 理论边界、(b) Differential Nocuity 降级为 interpretive lens、(c) C4 auth scope narrative 加入 measurement uncertainty caveat、(d) Ambiguity Blindness 改为 lack of externalized disambiguation、(e) Abstract 精简叙事。这些修改在 rebuttal/revision 周期内可完成。\n\n**评分对标 (EMNLP 2026 ARR)**：\n- 3.5 = Borderline Conference：实验贡献 (C1) 达到 conference 水准，但 framing/framework 问题使整体 novelty 受限。若 rebuttal 能有效 address taxonomy 理论张力和 framework positioning，可上调至 4.0 (Conference)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution (1) \"replicated across seven models\" 应明确区分 main study (5 models) vs. replication (2 models)\n- Contribution (2) 将 Differential Nocuity 列为框架贡献——如降级为 interpretive lens，需重写\n\n### §2 Related Work\n- 缺少与 DRIP-R 的 type-level 映射\n- 建议增引：SafeAgentBench, AgentHarm, deontic logic 文献\n\n### §3 Taxonomy\n- 需增加 \"Scope of 'ambiguity'\" 段落讨论 ambiguity/vagueness/incompleteness/normative conflict 边界\n- 末尾应声明 layer distinction 是 theoretical hypothesis\n- 视觉审查建议增加 taxonomy 可视化（表格或树形图）以改善 pages 3-5 的视觉节奏\n\n### §4 Method\n- §4.2 \"template-based pipeline\" 未描述 template 结构和数量\n- §4.4 Human validation: 正文应更显著呈现 per-type CI 宽度（scopal [0.00, 1.00]）\n- §4.5 ICC 应计算跨 provider concordance（Kendall's W）作为补充\n- §4.6 \"three test families\" 需显式列出成员；\"stabilizes at ±15 pp\" 措辞应更中性\n- §4.6 SESOI 需外部锚定（deployment SLA、行业 benchmark）\n\n### §5 Results\n- §5.2 C2: 应在正文讨论 ±10 pp 下的替代 narrative（three-tier 而非 two-tier）\n- §5.3 C3: 应强化 \"layer distinction 是 hypothesis\" 的表述\n- §5.4 C4: auth scope \"most model-differentiating type\" 应附带 \"upper bound on true variance\" caveat；F(20)=1.97 补充 denominator df\n- §5.4: Abstract \"52 pp\" 需 measurement uncertainty qualification\n\n### §6 Analysis\n- §6.1: Gwet's AC₁ vs Cohen's κ 差异应在正文解释 prevalence paradox\n- §6.2: \"Ambiguity Blindness\" 改为 \"lack of externalized disambiguation\"；讨论 uninstructed vs blind 区分\n\n### §7 Discussion\n- Differential Nocuity: 降级为 interpretive lens 或加强 non-obvious predictions\n- P1 \"supports P1\" claim 需 formal statistical test 或弱化措辞\n- 视觉审查建议增加视觉元素以缓解纯文本密集\n\n### Appendix B (Mitigation)\n- 补充 coreferential 排除的理由\n- auth scope −18.0 vs incompleteness −3.4 的差异需 formal test\n\n### Appendix D (Detection)\n- Coreferential 排除理由合理（lexically identical）\n\n### Appendix E (Replication)\n- LLaMA unambiguous baseline 17.6% 异常高，应讨论原因\n\n### Bib\n- ferrari_defects_2018: 核实第一作者（Rosadini vs Ferrari）\n- navigli_wsd_2009: 核实年份（2009 vs 2015）\n\n### 格式\n- 正文 ≤ 8 页 ✅\n- Double-blind ✅\n- ACL 模板 ✅\n- Limitations ✅\n- 0 orphan bib ✅\n- Data and Code Availability ✅\n",
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "\n# 审稿报告 — Round 9 (Fresh Review)\n\n**论文**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 via ARR May cycle (deadline: 2026-05-25)\n**Reviewer 编排**: R1（方法严谨性 + 实验有效性）、R2（新颖性 + 完整性）\n**审稿模式**: Fresh（无上轮记忆）\n**交叉回应**: 完成，关键问题全部达成共识\n\n---\n\n## Summary\n\n本文通过 matched-pair 实验设计，在 τ²-bench 上测量六类 policy ambiguity 对 LLM agent 安全违规的因果影响。构建 300 对条款（ambiguous vs. unambiguous），覆盖六类型双层歧义分类体系，在 5 个模型上运行 2,997 episodes，并在额外 2 个模型上做 replication。核心发现：(C1) 歧义条款使违规率增加 34.0 pp (OR=15.1)；(C2) 类型间存在显著层次结构 (Cramér's V=0.137)，呈两层模式；(C3) specification vs. linguistic 层级区分不显著（inconclusive）；(C4, exploratory) model×type 交互显著但解释方差仅 2.9%。论文还报告了 \"Ambiguity Blindness\"（<11% disambiguation awareness）和三种 type-specific failure mechanisms。\n\n---\n\n## Strengths\n\n**S1. 因果设计是该领域首创。** Matched-pair design + perturbation control (Δ_perturb = −0.67 pp, CI containing zero) 在 agent safety 文献中首次建立了 policy ambiguity → safety violation 的因果关系。DRIP-R 做相关分析，PolicyBank 做迭代改进，本文是第一个因果推断工作。7 个模型跨 6 个 provider 的 replication 进一步增强外部效度。[R1-S1, R2-S1, 共识]\n\n**S2. Confound 处理和透明度出色。** Incompleteness 的 information-addition confound 在 §3（taxonomy 定义）就主动指出，§5.2 讨论，Appendix F/H 提供 logistic regression 控制 (p=0.022, coefficient change <8%) 和 coreferential confound-free lower bound (31.6%)。TOST sensitivity across 7 margins、bootstrap cluster analysis、clause-level LOO variance、severity threshold comparison 构成多角度 robustness 检验。[R1-S2/S4, R2-S2, 共识]\n\n**S3. Claims 标注层次清晰。** C1 (primary, well-supported) → C2 (primary, with caveats) → C3 (inconclusive) → C4 (exploratory) 的递进标注避免了 overclaim，C3 如实报告为 inconclusive 是良好科学实践。[R1-S3, R2-S4, 共识]\n\n**S4. Type > Model 的方差分解有实际价值。** Type 解释 22.4% variance vs. model 仅 1.0%，意味着 policy auditing 应以 type 为导向而非 model 为导向。Detection experiment (binary F1=0.81) 和 mitigation experiment 展示了 pipeline 原型。[R1-S5, R2-S3, 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. Taxonomy 将 ambiguity、vagueness、incompleteness、normative conflict 混为一谈。** [R2 raised, R1 AGREE with qualification]\n\n六类型中三个不严格属于 ambiguity：authorization scope 是 vagueness (Kennedy 2007)，incompleteness 是 information absence（论文自身承认 \"resolution requires adding new policy content\"），conditional precedence 是 normative conflict（每条规则本身无歧义）。Wasow (2005) 的操作性定义虽将 vagueness 纳入范畴，但 incompleteness 和 conditional precedence 不在该定义的自然覆盖范围内。\n\n如果最高违规率的 type (incompleteness, 53.6%) 不严格属于 ambiguity，\"ambiguity type predicts severity\" 的核心 framing 存在理论张力。\n\n两位 Reviewer 共识的修改方向：保留 ambiguity framing，但 §3 需增加 \"Scope of 'ambiguity'\" 段落，正面讨论理论边界，承认 incompleteness 和 conditional precedence 处于定义边界，明确论证为何 operational/inclusive 定义在 LLM agent 场景下合理。\n\n**N2. Differential Nocuity 框架的增量贡献不清晰。** [R2 raised, R1 AGREE]\n\n框架声称 risk = f(ambiguity type, safety training, disambiguation channel availability)。但：\n- \"LLM agents 缺乏 disambiguation channels → 所有 ambiguity 都 nocuous\" 是 Berry & Kamsties (2004) 的直接推论\n- 三因素中仅 \"ambiguity type\" 有 C1+C2 充分支撑；\"safety training\" 基于 [Exploratory] C4 + κ=0.385 的 authorization scope；\"disambiguation channel\" 基于可能反映 uninstructedness 的 <11% awareness\n- P1/P2 predictions 是 post-hoc rationalization，P1 支持证据 (Appendix B: auth scope −18.0 vs incompleteness −3.4) 无 formal statistical test\n\n两位 Reviewer 共识：将 Differential Nocuity 从 contribution 降级为 Discussion 中的 interpretive lens，或展示 non-obvious testable predictions with adequate statistical support。\n\n**N3. SESOI ±15 pp 缺乏外部锚定。** [R1 raised as MUST-FIX, R2 AGREE but suggests SHOULD-FIX]\n\n±15 pp 的理由是主观的 deployment-relevance 判断和 perturbation control bound 的 2× 倍数（循环论证）。±10 pp 时仅 3/6 mid-tier pairs 等价 (Table 2)，TOST power 降至 0.57。Bootstrap cluster AU p-value = 0.47 表明 incompleteness singleton 边界不尖锐。\n\n**Reviewer 分歧**：R1 认为 MUST-FIX，R2 认为论文已有 partial mitigation（sensitivity analysis + bootstrap cluster 作为 margin-free 补充；incompleteness upper bound 在所有 margin 下成立），建议降为 SHOULD-FIX。\n\nDirector 判断：incompleteness 作为 upper bound 的核心 finding 稳健，但 mid-tier clustering 对 margin 敏感。需要外部锚定和更显著的 sensitivity 呈现，但不 invalidate C2 整体。严重程度介于两位 Reviewer 判断之间。\n\n**N4. Authorization scope κ=0.385 下 C4 结论可信度不足。** [R1 raised, R2 AGREE]\n\nCross-judge κ=0.385 仅为 fair agreement，human-LLM κ=0.644 CI=[0.35, 0.91] lower bound 极低。然而 C4 Discussion 从这个 noisy measurement 推导出 safety training differential mitigation 叙事。Within-judge bootstrap (99.5%) 不能排除 judge-level systematic bias。Introduction contribution (2) 和 Abstract 中的表述与正文 \"suggestive\" hedging 不匹配。\n\n两位 Reviewer 共识：52 pp range 应标注为 \"upper bound on true between-model variance\"；Abstract 需附带 measurement uncertainty qualification。此问题与 N1 (taxonomy 混淆) 互相加强——authorization scope 同时存在理论定义争议和测量可靠性问题。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. \"Ambiguity Blindness\" framing 过度。** [R1-W4 + R2-W5, 共识]\n\n<11% awareness 反映 uninstructed default behavior 而非 inability。Mitigation experiment −8.5 pp 改善直接反驳 blindness framing（agents CAN respond when prompted）。人类也默认采用 good-enough single parse (Ferreira 2002)。建议改为 \"lack of externalized disambiguation\"。\n\n**W2. Abstract 信息过载。** [R2-W1, R1 AGREE]\n\nOR、V、κ、p-values、logistic regression coefficient change 等大量数字淹没核心 message。建议精简为 problem→approach→2-3 key findings→implication 结构。\n\n**W3. C3 layer distinction 与 taxonomy 组织原则的逻辑张力。** [R2-W2, R1 AGREE with qualification]\n\nC3 未通过 Holm-Bonferroni 校正但 taxonomy 仍以 linguistic/specification layer 为组织原则。R1 认为保留 layer 但标注为 hypothesis 是更好的方案（比 flat six-type 更有信息量）。建议 §3 末和 §5.3 明确 \"layer distinction is a theoretical hypothesis, not an empirical finding\"。\n\n**W4. Token count 作为 information content proxy 未验证。** [R1-W1, R2 AGREE]\n\nLogistic regression 使用 token count difference 作为 information content 代理变量，未讨论 content validity 或尝试替代度量。R2 指出 partial mitigation: coefficient change <8% 限制了 proxy 不完美性的影响。\n\n**W5. Human validation 样本偏小，per-type CI 极宽。** [R1-W2, R2 AGREE]\n\n100/2997 (3.3%)，per-type n=32-34，scopal CI [0.00, 1.00] 本质上 uninformative。§4.4 正文呈现过于乐观（强调 pooled κ=0.733 而淡化 per-type 不稳定性）。\n\n**W6. Cross-provider ICC 缺乏直接度量。** [R1-W3, R2 AGREE]\n\nICC=0.919 仅 within OpenAI family。LLaMA Δ=+20 pp 远小于主研究 range (+25.7–39.0 pp)，暗示跨 provider effect 可能受 baseline instruction-following quality 调节。\n\n**W7. 多重比较校正 \"three test families\" 未定义。** [R1-W5, R2 AGREE]\n\n§4.6 未列出成员，读者无法验证校正适当性。\n\n**W8. 与 DRIP-R 的 type-level 映射缺失。** [R2-W3, R1 AGREE]\n\nDRIP-R 有 5 个 RE ambiguity types，本文 6 个，未提供显式映射。\n\n**W9. Coreferential 被系统性排除在 3 个 follow-up 分析之外。** [R2-W4, R1 AGREE with qualification]\n\nDetection 和 replication 排除有技术合理性（lexically identical variants），但 mitigation 排除理由缺失（Appendix B caption 为循环解释）。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n- R1-N2 / R2 auth scope κ 问题 → C4 narrative 需 heavily caveat\n- R2-N2 / R1 Differential Nocuity 增量 → 应降级为 interpretive lens\n- Ambiguity Blindness → 应改为 lack of externalized disambiguation\n- Abstract 信息过载 → 需重构叙事\n- 多重比较校正不透明 → 需显式列出 test families\n- DRIP-R mapping 缺失 → 需补充\n- Coreferential exclusion → mitigation 排除理由需补充\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | Director 判断 |\n|------|-----|-----|--------------|\n| N3 SESOI severity | MUST-FIX | SHOULD-FIX (partial mitigation) | 介于两者之间：mid-tier clustering 确实 margin-sensitive，但 incompleteness upper bound 稳健 |\n| N1 Taxonomy: 修改方案 | Option (b): 保留 framing + 讨论张力 | Option (a) preferred: reframe to \"policy specification defects\" | 倾向 R1 方案：保留 ambiguity framing + 正面讨论理论张力，成本更低且可行 |\n| W3 C3 layer: 修改方案 | 保留 layer 作为 hypothesis | 改为 flat six-type | 倾向 R1：保留 layer 但明确标注为 hypothesis |\n\n---\n\n## Questions for Authors\n\n1. **[高优先级]** §3 Taxonomy: 如何回应 authorization scope = vagueness、incompleteness = information absence、conditional precedence = normative conflict 的理论质疑？是否愿意增加 \"Scope of 'ambiguity'\" 段落正面讨论？\n2. **[高优先级]** Differential Nocuity 框架中，P1 (auth scope −18.0 vs incompleteness −3.4 pp) 是否经过 formal statistical test？如果没有，Discussion 中 \"mitigation experiment supports P1\" 的 claim 是否应弱化？\n3. **[高优先级]** 如果使用 ±10 pp 作为 SESOI，C2 narrative 如何调整？mid-tier 变为 three-tier 结构是否影响核心结论？\n4. 移除 3 个 specification-layer types 后，仅用 linguistic types 的 C1/C2 是否仍然成立？\n5. Clause pairs 的 template-based pipeline 具体使用多少 templates per type？template 结构如何影响 clause-level variance？\n6. 是否尝试过在 system prompt 中要求 agents flag ambiguity？如果有，awareness rate 从 4.6% 提升到多少？\n7. Claude auth scope 12% vs GPT-5.4 64% — 两者均由 GPT-5.4 judge 评估，排除了 judge identity confound。但 κ=0.385 下 per-episode 噪声大——52 pp range 中真实 model difference 占比多少？\n\n---\n\n## Missing References\n\n两位 Reviewer 共同建议：\n- **Zheng et al. (2024)** \"Judging LLM-as-a-Judge\" — 与 §4.4 cross-judge design 直接相关 [已引用，确认]\n- **Anvari & Lakens (2021)** — TOST SESOI 选择的方法论文献 [已引用，确认]\n\nR1 建议：\n- Tamkin et al. (2023) — policy-governed decision-making\n- Pan et al. (2024) — LLM ambiguity following behavior\n- Karpinska & Iyyer (2023) — LLM contextual ambiguity processing\n\nR2 建议：\n- SafeAgentBench (Yin et al., 2025) — embodied agent safety\n- AgentHarm (Andriushchenko et al., 2024) — agent misuse benchmark\n- Deontic logic / normative conflict literature (Prakken & Sartor) — conditional precedence 理论基础\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 external_review.paperreview_ai.enabled）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2 warnings, 9 info）。主要发现：\n\n- **[Warning]** Pages 3-5 连续 3 页纯文本（Related Work → Taxonomy → Method），无任何 display item。Section 3 描述六类型分类体系但缺少对应的分类表格或树形图。建议增加 taxonomy 可视化。\n- **[Warning]** Page 8（Discussion + Conclusion）为纯文本密集页，与 pages 6-7 的 figure/table 密集形成反差，整体节奏 \"前松后紧再松\"。\n- **[Info]** Figure 1 内部标注字体偏小，打印时可能不可读。\n- **[Info]** 主文 8 页内 4 个 display items (3 figure + 1 table)，对实证论文偏少（通常 5-8 个）。\n- **[Info]** Table 1 格式规范（booktabs），Figure 2/3 颜色区分度良好。\n- **[Info]** Limitations 篇幅适当，参考文献格式统一无未解析引用。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 — Borderline Conference**\n\n**置信度: 4/5**（两位 Reviewer 分别熟悉因果推断/agent safety 和 CL ambiguity/RE 文献）\n\n**理由**：\n\n实验执行达到 conference 标准：matched-pair causal design 是 agent safety 领域首创，C1 (+34 pp, OR=15.1) 因果效应在 7 个模型上 replicated，统计方法严谨透明，confound 处理和 claims 标注层次清晰。Type > Model 的方差分解 (22:1) 有直接部署指导意义。\n\n但概念框架存在根本性张力：(1) taxonomy 将 ambiguity、vagueness、information absence、normative conflict 混为一谈，核心 framing \"ambiguity type predicts severity\" 的理论基础被削弱；(2) Differential Nocuity 框架的增量贡献有限，本质是既有理论在 LLM 场景下的直接推论加上 exploratory 实验发现的包装；(3) authorization scope 同时存在理论定义争议 (vagueness) 和测量可靠性问题 (κ=0.385)，使得关于该 type 的所有 claim 都需 heavily caveat。\n\n修复路径明确：(a) §3 正面讨论 taxonomy 理论边界、(b) Differential Nocuity 降级为 interpretive lens、(c) C4 auth scope narrative 加入 measurement uncertainty caveat、(d) Ambiguity Blindness 改为 lack of externalized disambiguation、(e) Abstract 精简叙事。这些修改在 rebuttal/revision 周期内可完成。\n\n**评分对标 (EMNLP 2026 ARR)**：\n- 3.5 = Borderline Conference：实验贡献 (C1) 达到 conference 水准，但 framing/framework 问题使整体 novelty 受限。若 rebuttal 能有效 address taxonomy 理论张力和 framework positioning，可上调至 4.0 (Conference)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution (1) \"replicated across seven models\" 应明确区分 main study (5 models) vs. replication (2 models)\n- Contribution (2) 将 Differential Nocuity 列为框架贡献——如降级为 interpretive lens，需重写\n\n### §2 Related Work\n- 缺少与 DRIP-R 的 type-level 映射\n- 建议增引：SafeAgentBench, AgentHarm, deontic logic 文献\n\n### §3 Taxonomy\n- 需增加 \"Scope of 'ambiguity'\" 段落讨论 ambiguity/vagueness/incompleteness/normative conflict 边界\n- 末尾应声明 layer distinction 是 theoretical hypothesis\n- 视觉审查建议增加 taxonomy 可视化（表格或树形图）以改善 pages 3-5 的视觉节奏\n\n### §4 Method\n- §4.2 \"template-based pipeline\" 未描述 template 结构和数量\n- §4.4 Human validation: 正文应更显著呈现 per-type CI 宽度（scopal [0.00, 1.00]）\n- §4.5 ICC 应计算跨 provider concordance（Kendall's W）作为补充\n- §4.6 \"three test families\" 需显式列出成员；\"stabilizes at ±15 pp\" 措辞应更中性\n- §4.6 SESOI 需外部锚定（deployment SLA、行业 benchmark）\n\n### §5 Results\n- §5.2 C2: 应在正文讨论 ±10 pp 下的替代 narrative（three-tier 而非 two-tier）\n- §5.3 C3: 应强化 \"layer distinction 是 hypothesis\" 的表述\n- §5.4 C4: auth scope \"most model-differentiating type\" 应附带 \"upper bound on true variance\" caveat；F(20)=1.97 补充 denominator df\n- §5.4: Abstract \"52 pp\" 需 measurement uncertainty qualification\n\n### §6 Analysis\n- §6.1: Gwet's AC₁ vs Cohen's κ 差异应在正文解释 prevalence paradox\n- §6.2: \"Ambiguity Blindness\" 改为 \"lack of externalized disambiguation\"；讨论 uninstructed vs blind 区分\n\n### §7 Discussion\n- Differential Nocuity: 降级为 interpretive lens 或加强 non-obvious predictions\n- P1 \"supports P1\" claim 需 formal statistical test 或弱化措辞\n- 视觉审查建议增加视觉元素以缓解纯文本密集\n\n### Appendix B (Mitigation)\n- 补充 coreferential 排除的理由\n- auth scope −18.0 vs incompleteness −3.4 的差异需 formal test\n\n### Appendix D (Detection)\n- Coreferential 排除理由合理（lexically identical）\n\n### Appendix E (Replication)\n- LLaMA unambiguous baseline 17.6% 异常高，应讨论原因\n\n### Bib\n- ferrari_defects_2018: 核实第一作者（Rosadini vs Ferrari）\n- navigli_wsd_2009: 核实年份（2009 vs 2015）\n\n### 格式\n- 正文 ≤ 8 页 ✅\n- Double-blind ✅\n- ACL 模板 ✅\n- Limitations ✅\n- 0 orphan bib ✅\n- Data and Code Availability ✅\n",
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 801 · 2026-05-21T17:54:27.211362+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4067
}
```

</details>

---


### Assistant

_source line 802 · 2026-05-21T17:54:42.195395+00:00_

审稿报告已投递至 Research Director。

**Round 9 审稿完成**。汇总：

- **Overall: 3.5 (Borderline Conference)**
- **4 个 Must-Fix**：(1) Taxonomy 混淆 ambiguity/vagueness/incompleteness/normative conflict；(2) Differential Nocuity 框架增量贡献不清晰；(3) SESOI ±15pp 缺乏外部锚定（R1/R2 对严重程度有轻微分歧）；(4) Authorization scope κ=0.385 下 C4 可信度不足
- **9 个 Should-Fix**：Ambiguity Blindness framing、Abstract 过载、C3 layer 逻辑张力、token count proxy、human validation 样本量、cross-provider ICC、多重比较校正、DRIP-R mapping、coreferential 排除
- **核心判断**：实验执行（C1 因果设计）达到 conference 标准，但概念框架（taxonomy 理论基础 + Differential Nocuity 增量）需要加强。修复路径明确，rebuttal 可完成。
- **Issue tracker** 和 **视觉审查** 结果均已同步更新

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 74

## Round 74

2 recorded events


### User

_source line 803 · 2026-05-21T17:54:44.712295+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **N1 (Taxonomy)**: 部分同意。Incompleteness 确实不严格属于 ambiguity，但建议保留 ambiguity framing 并正面讨论理论张力，而非 reframe 为 "policy specification defects"。
- **N2 (Differential Nocuity)**: 完全同意。Framework packaging 超出实验证据支撑，应降级为 interpretive lens。
- **W1-W5**: 基本同意，其中 W2 (layer 组织原则) 建议保留 layer 作为理论假设而非 flat six-type，W5 (Ambiguity Blindness) 与我 R1-W4 的观点一致。

两位 reviewer 的审稿互补——R2 从理论 framing 角度、我从测量可靠性角度——共同指向：C1 solid，C2 需 caveat，framework claims 需 downgrade。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 804 · 2026-05-21T17:54:55.841748+00:00_

审稿报告已投递给 Research Director。

**本轮审稿总结**：

- **评分**：3.5（Borderline Conference）
- **两位 Reviewer 均 3.5**，从不同角度（R1 方法论、R2 理论基础）达成一致
- **4 个 Critical Issues**：taxonomy 理论混淆、Differential Nocuity 增量有限、SESOI 缺乏外部锚定、auth scope κ=0.385 削弱 C4
- **9 个 Warning Issues**：Ambiguity Blindness framing、Abstract 过载、C3 layer 逻辑张力、token count proxy、human validation 样本量、cross-provider ICC、多重比较校正、DRIP-R 映射、coreferential 排除
- **核心判断**：实验执行达到 conference 标准（C1 因果设计是领域首创），但概念框架需要加强。修复路径明确，rebuttal 周期内可完成
- **Issue Tracker 已同步更新**（5 个 Round 8 issue 标记 resolved，新增 Round 9 issues）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 75

## Round 75

72 recorded events


### User

_source line 805 · 2026-05-21T18:56:17.092851+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR May cycle)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 806 · 2026-05-21T18:56:23.577735+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 807 · 2026-05-21T18:56:23.631250+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-21T18:56:30.359835+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 809 · 2026-05-21T18:56:30.410514+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 810 · 2026-05-21T18:56:35.178139+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
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

_source line 811 · 2026-05-21T18:56:35.278964+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-21T18:56:38.692187+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 813 · 2026-05-21T18:56:38.692655+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-21T18:56:43.214485+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-21T18:56:43.666689+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (16 个)\n\n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_009**: PREPARING — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_009: Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.（准备中）\n\n## 近期结论\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C1 causal inference ← 基于 plan_010\n  [plan_014_extended_perturbation_results](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/data/results.json) | [plan_014_perturbation_clauses_extended](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/data/clauses_perturbation_extended.json) | [plan_014_run_script](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_014/intermediate/run_plan014.py)\n- **plan_015** (success): Authorization scope violations are predominantly unauthorized escalation (granting excess permissions) rather than restriction, consistent across all 5 models, revealing systematic permissiveness bias under boundary ambiguity\n- **plan_013** (success): Binary ambiguity effect (C1: Δ >= 20pp) and type hierarchy (C2: at least partial rank consistency) re
…[truncated 247 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 816 · 2026-05-21T18:56:44.168875+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 817 · 2026-05-21T18:56:44.169275+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 818 · 2026-05-21T18:56:45.323328+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 819 · 2026-05-21T18:56:45.373994+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 820 · 2026-05-21T18:56:49.840256+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 821 · 2026-05-21T18:56:51.046332+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-21T18:56:51.749236+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
  }
}
```

</details>

---


### Tool call

_source line 823 · 2026-05-21T18:56:52.050644+00:00_

called mcp__agent-ml-research__read_local_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_local_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 824 · 2026-05-21T18:56:52.050990+00:00_

&lt;tool_use_error>Error: No such tool available: mcp__agent-ml-research__read_local_file&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 825 · 2026-05-21T18:56:57.077480+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here's information about EMNLP 2026's call for papers submission guidelines related to ARR:

## Submission Process and Guidelines

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

Papers must be submitted by the ARR 2026 May cycle, and papers that have received reviews and a meta-review from ARR may be committed to EMNLP via the commitment link.

## Important Dates

The ARR submission deadline for long and short papers is May 25, 2026, with the reviewer registration deadline for all authors on May 27, 2026, author response and author-reviewer discussion from July 7-13, 2026, meta review released July 30, 2026, and EMNLP commitment deadline August 2, 2026.

## Critical ARR Policy Update

Sin
…[truncated 603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 7237
}
```

</details>

---


### Tool result

_source line 826 · 2026-05-21T18:56:57.128234+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'policy_ambiguity_safety'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6081
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-21T18:56:57.128766+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Glob",
  "elapsed_ms": 5379
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-21T18:57:03.253788+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit template anonymity guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit template anonymity guidelines"
  }
}
```

</details>

---


### Tool call

_source line 829 · 2026-05-21T18:57:03.605298+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 830 · 2026-05-21T18:57:03.606627+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type ambiguity taxonomy, evaluated across five models (2,997 episodes). Three findings emerge. First, ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. Second, a two-tier type hierarchy separates incompleteness (46--62\% violation rate across seven models) from the remaining five types, with type identity explaining 22$\times$ more variance than model identity (22.4\% vs.\ 1.0\%). Third, authorization scope shows the widest cross-model range (52\,pp, though measured with the lowest inter-judge agreement, $\kappa = 0.385$), suggesting that safety training may differentially mitigate specific ambiguity types. Agents show fewer than 11\% disambiguation awareness, adopting surface interpretations without flagging uncertainty. These results motivate type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 831 · 2026-05-21T18:57:04.058820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 832 · 2026-05-21T18:57:04.460306+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
13	\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-
…[truncated 2016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 833 · 2026-05-21T18:57:04.661241+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 834 · 2026-05-21T18:57:10.183476+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit template anonymity guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, here's information about ACL Rolling Review 2026 submission requirements:

## Page Limits

Short papers have a maximum of 4 content pages, and long papers have a maximum of 8 content pages. Sections on ethical considerations and limitations do not count towards the page limit.

## Anonymity Guidelines

Papers must not include authors' names and affi
…[truncated 1165 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 6929
}
```

</details>

---


### Tool result

_source line 835 · 2026-05-21T18:57:10.184082+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/decisions.yaml\", \"content\": \"_next_id: 26\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 07:11 UTC\\n  summary: MVP 设计：3 类歧义 × 2 API 模型验证 type effect，不用 GPU\\n  rationale: 核心假设是\\\"歧义类型影响安全违规率\\\"。选 scopal/lexical/incompleteness 3 种假设差异最大的类型，用 frontier\\n    API 模型（免 GPU）快速验证信号存在性。60 条款 × 2 variants × 2 模型 = 240 runs，统计功效足够（χ² df=2, medium\\n    effect w=0.3, N=240 >> 所需 ~107）。Pass 条件：p<0.05 + V≥0.15。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 07:15 UTC\\n  summary: 采纳 Reviewer 3 条修正：增条款数、调阈值、补 fail path\\n  rationale: 'Reviewer WARNING: (1) pairwise N=80 对 V=0.15 功效仅 0.22，增至 30 条款/类（pairwise\\n    N=120）+ 提阈值至 V≥0.20 + 明确 MVP 只检测 medium+ effect；(2) 补 fail path 三级决策树（扩大N重测 →\\n    pivot binary story → full study）；(3) 加 judge 偏差检查点（scopal 低于预期时先排查 judge bias）。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 07:16 UTC\\n  summary: ROADMAP 补充 H1-H4 预测基准和 post-MVP 18 周路径骨架\\n  rationale: 'Reviewer WARNING: (1) ROADMAP 缺 post-MVP 骨架，ICLR DDL 18 周后，需提前规划 GPU\\n    申请时间点（W3 MVP pass 后立即申请，W5 开始 Phase 2b）；(2) H1-H4 方向性预测未落地到 ROADMAP，Agent 解读 MVP\\n    结果时需对照基准（H1: scopal 最高，H2: lexical 最低，null: binary effect story）。paper_framing.md\\n    保持在 MVP 后创建。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-20 07:23 UTC\\n  summary: MVP 分析改为双轨：ambiguous-only 跨类型比较（主）+ matched-pair within-type（辅）\\n  rationale: 'Reviewer WARNING: incompleteness matched pair 存在信息量不对称混淆——消歧必然添加信息，与\\n    scopal/lexical 的\\\"同信息不同措辞\\\"baseline 不可比。解法：(1) 主分析用 ambiguous-only 条件直接跨类型比较违规率（不受信息量混淆）；(2)\\n    matched-pair 降为辅助的 within-type 效应量度量；(3) 要求 Agent 修订 incompleteness pairs 只添加解决歧义的最小信息；(4)\\n    效度边界显式声明此不对称性。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-20 07:24 UTC\\n  summary: MVP 使用 τ²-
…[truncated 1453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5522
}
```

</details>

---


### Tool call

_source line 836 · 2026-05-21T18:57:21.129938+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if paper PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 837 · 2026-05-21T18:57:22.037075+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 838 · 2026-05-21T18:57:22.540688+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 839 · 2026-05-21T18:57:22.942854+00:00_

## Round 9 (Fresh) Review Issues — policy_ambiguity_safety
## Paper: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
## Venue: EMNLP 2026 via ARR May cycle
## Date: 2026-05-21
## Round 9 Score: 3.5 (Borderline Conference)
## Note: Fresh review session — all issues re-evaluated from scratch

# ============================================================
# CRITICAL ISSUES
# ============================================================

- id: "R9-N1"
  summary: "Taxonomy 将 ambiguity、vagueness、incompleteness、normative conflict 混为一谈，理论基础存在根本性混淆"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 9
  last_seen_round: 9
  mentions:
    - round: 9
      reviewers: [R2]
      note: "R2 raised as N1. Authorization scope 是 vagueness (Kennedy 2007)，incompleteness 是 information absence，conditional precedence 是 normative conflict。6 types 中 3 个不严格属于 ambiguity。R1 AGREE with qualification。两人共识：需在 §3 正面讨论理论张力。"
  action_items:
    - round: 9
      action: "§3 末尾新增 'Scope of Ambiguity' 段落 (~120 words)：承认 auth scope→vagueness, incompleteness→information absence, cond prec→normative conflict；论证 operational/inclusive 定义合理性（Wasow 2005 + Berry & Kamsties 2004）；LLM agent 场景下解析机制相同"
      assigned_to: agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R9-N2"
  summary: "Differential Nocuity 框架增量贡献不清晰，本质是 Berry & Kamsties 2004 的 trivial 推论"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 9
  last_seen_round: 9
  mentions:
    - round: 9
      reviewers: [R2, R1]
      note: "R2 raised as N2, R1 AGREE. 三因素中仅 'ambiguity type' 有 C1+C2 支撑；P1/P2 是 post-hoc rationalization。"
  action_items:
    - round: 9
      action: "DN 从 contribution list 移除→§7 Discussion interpretive lens；§1 contribution (2) 改为 type hierarchy + variance decomposition；Abstract/Conclusion 删除 DN 独立贡献；P1 'supports' → 'consistent with'"
      assigned_to: agent
      status: in_progress
  resolution: "
…[truncated 12414 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-21T18:57:23.495308+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 841 · 2026-05-21T18:57:23.947824+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 842 · 2026-05-21T18:57:24.449740+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 843 · 2026-05-21T18:57:24.751293+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type hierarchy (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). Clause identity explains 22.4\% of variance versus 1.0\% for model identity. A replication on two additional model families (Gemini-2.5-Flash, LLaMA-4-Scout; Appendix~\ref{app:model_expansion}) confirms the effect across seven models spanning six providers ($\Delta = +20.0$ to $+33.6$\,pp, both $p < 10^{-6}$).
9	
10	\subsection{Type Hierarchy (C2)}
11	
12	\begin{table*}[t]
13	\centering
14	\caption{Violation rates (\%) under ambiguous policy clauses by type and model. $\Delta$pp denotes the pooled difference between ambiguous and unambiguous conditions across all five models. All per-type differences are significant ($p < 10^{-5}$, Fisher's exact test).}
15	\label{tab:main_results}
16	\small
17	\begin{tabular}{llrrrrrrrr}
18	\toprule
19	Layer & Type & Pooled & GPT-5.4 & GPT-4.1 & Claude & Qwen3 & DeepSeek & $\Delta$pp & $p$ \\
20	\midrule
21	\multirow{3}{*}{\textcolor{speccolor}{Spec.}} & Incompleteness & 53.6 & 46.0 & 58.0 & 48.0 & 62.0 & 54.0 & +49.2 & $<10^{-37}$ \\
22	 & Auth.\ Scope & 41.6 & 64.0 & 46.0 & 12.0 & 26.0 & 60.0 & +36.0 & $<10^{-22}$ \\
23	 & Cond.\ Precedence 
…[truncated 5786 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 844 · 2026-05-21T18:57:24.801912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 845 · 2026-05-21T18:57:24.852651+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% pass rate; disagreements were resolved by discussion. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We evaluate five models spanning four providers and two architecture families: GPT-5.4 and GPT-4.1 (OpenAI, pro
…[truncated 4652 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 846 · 2026-05-21T18:57:31.327448+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -name \"config.yaml\" -o -name \"config.yml\" -o -name \"*.json\" -path \"*/agent/*\" 2>/dev/null | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -name \"config.yaml\" -o -name \"config.yml\" -o -name \"*.json\" -path \"*/agent/*\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 847 · 2026-05-21T18:57:32.281376+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 848 · 2026-05-21T18:57:32.432352+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 849 · 2026-05-21T18:57:32.834344+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers, drawing on \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types), \citet{massey_ambiguity_re_2014}'s requirements engineering taxonomy (6 types), and the concurrent DRIP-R benchmark \citep{drip_r_2026} (5 types). We select types based on two criteria: frequency in operational policy documents (assessed via manual audit of $\tau^2$-bench policies) and theoretical distinctiveness (each type maps to a different resolution mechanism).
7	
8	\paragraph{Linguistic layer.} These types operate at the syntactic or semantic level and can, in principle, be resolved by parsing or contextual cues within the text.
9	\begin{itemize}
10	\item \textbf{Scopal}: quantifier, negation, or modal scope interactions (e.g., ``all items may not be returned'' admits universal-negation and negation-of-universal readings).
11	\item \textbf{Lexical}: polysemy or homonymy (e.g., ``charge'' as financial cost vs.\ penalty; ``party'' as individual vs.\ group).
12	\item \textbf{Coreferential}: unclear pronoun or noun-phrase reference (e.g., ``the agent should verify the customer's identity before processing their refund request, which must be approved by a supervisor'' where ``which'' could refer to the verification or the refund).
13	\end{itemize}
14	
15	\paragraph{Specification layer.} These types arise from pragmatic or discourse-level gaps that require domain knowledge or organizational context to resolve.
16	\begin{itemize}
17	\item \textbf{Authorization scope}: vague permission or role boundaries (e.g., ``authorized personnel may issue r
…[truncated 2007 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 850 · 2026-05-21T18:57:32.834787+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 851 · 2026-05-21T18:57:32.935442+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes: unauthorized escalation, assumption-based action, scope misapplication, arbitrary rule selection, and conservative refusal. GPT-5.4 and GPT-4.1 serve as detailed annotation anchors because they span the judge boundary. Inter-coder reliability is substantial (Gwet's AC$_1$ $= 0.62$ \citep{gwet_2014}; Cohen's $\kappa = 0.52$ \citep{cohen_1960}). The gap reflects the prevalence paradox: three categories account for ${\sim}$90\% of instances, compressing the $\kappa$ denominator and yielding artificially low values despite high raw agreement.
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse} (scope misapplication): the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002}---e.g., parsing ``items purchased with a coupon or during a sale are final'' as restricting only coupon purchases. This dominates scopal (all 5 models), conditional precedence (all 5), and coreferential (3/5).
13	
14	\emph{Information gap-filling} (assumption-based action): the agent fills missing information with plausible but incorrect defaults---e.g., inventing a 30-day return window when none is specified. This dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation} (unauthorized escalation): the agent exceeds permission boundaries when authorization scope is underspecified---e.g., issuing a refund above its stated limit rather than escalating; 69.2\% of such violations involve unauthorized esc
…[truncated 2108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 852 · 2026-05-21T18:57:33.187052+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 853 · 2026-05-21T18:57:33.237757+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit analogous garden-path effects. \citet{liu_ambiguity_2023} demonstrate that language models fail to represent ambiguity, collapsing multiple interpretations into a single output. These findings
…[truncated 2322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 854 · 2026-05-21T18:57:36.650852+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-21T18:57:37.153049+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity.}
5	\citet{berry_kamsties_2004} distinguish nocuous from innocuous ambiguity. Our results can be interpreted through a \emph{differential nocuity} lens: risk depends on ambiguity type (base vulnerability), safety training (selective mitigation), and disambiguation channel availability. This generates two testable predictions: (P1) types with explicit decision points should show larger safety-training gains than gap-filling types; (P2) disambiguation channels should reduce violations more for high-deficit types. Our mitigation experiment (Appendix~\ref{app:mitigation}) is consistent with, though not a formal test of, P1 ($-18.0$\,pp for authorization scope vs.\ $-3.4$\,pp for incompleteness).
6	
7	\paragraph{Practical implications.}
8	A proof-of-concept classifier (Appendix~\ref{app:detection}) achieves F1\,=\,0.81 for binary ambiguity detection but only 0.34 for incompleteness---the highest-risk type is the hardest to detect. With agents exhibiting disambiguation deficit in $>$89\% of cases, type-aware auditing and externalized detection \citep{chantree_2006,ferrari_ambiguity_2019} are necessary for policy-governed deployments.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-21T18:57:37.153435+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 857 · 2026-05-21T18:57:38.107113+00:00_

1	\section{Conclusion}
2	
3	Ambiguous policy clauses increase agent safety violations by 34.0\,pp (OR\,$=$\,15.1) across five models, with clause identity explaining 22$\times$ more variance than model identity. The two-tier type hierarchy replicates across seven models ($\rho = 0.60$--$0.90$). With agents exhibiting disambiguation deficit in over 89\% of cases, type-aware auditing and externalized detection are critical for policy-governed deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-21T18:57:38.107490+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 859 · 2026-05-21T18:57:38.559472+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Model coverage.} We evaluate seven API-accessible models from six providers (four proprietary, three open-source; two in replication, Appendix~\ref{app:model_expansion}). Smaller open-source models (7B--70B parameters) may show different vulnerability patterns, and our findings may not generalize to models with fundamentally different training approaches.
5	
6	\paragraph{Domain scope.} $\tau^2$-bench covers retail and airline customer service. Policy ambiguity effects in other domains (healthcare, finance, legal) remain to be tested, though the within-study cross-domain consistency is encouraging: failure mode distributions share the same top-two modes (assumption-based action and unauthorized escalation) across domains, with individual mode base rates differing by up to 12.5 pp, likely reflecting domain policy structure rather than methodological artifacts.
7	
8	\paragraph{Synthetic ambiguity.} Our matched-pair design requires synthetic construction of ambiguous variants, which may not capture the full distribution of naturally occurring policy ambiguities. We mitigate this through expert review and a realism validation comparing ambiguous clauses against original $\tau^2$-bench policy text. Ambiguous clauses are indistinguishable from originals in lexical diversity (TTR, KS $p = 0.89$) and word length ($p = 0.09$). Readability is slightly higher (Flesch--Kincaid $d = 0.29$, $p = 0.006$) and sentence length moderately higher ($d = 0.74$), both reflecting the structural demands of encoding ambiguity in standalone clauses. Across matched pairs, disambiguation preserves readability (Flesch--Kincaid $d = 0.14$, $p = 0.10$), confirming that minimal edits change semantic precision without altering linguistic register.
9	
10	\paragraph{Cross-judge asymmetry.} Although our dual-judge calibration (\S\ref{sec:method}) shows no systematic bias ($p = 0.606$) and human validation confirms the LLM judge operates 
…[truncated 2965 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 860 · 2026-05-21T18:57:38.610207+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -name \"config.yaml\" -o -name \"project.yaml\" 2>/dev/null",
  "description": "Find project configuration files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -name \"config.yaml\" -o -name \"project.yaml\" 2>/dev/null",
    "description": "Find project configuration files"
  }
}
```

</details>

---


### Tool result

_source line 861 · 2026-05-21T18:57:38.761323+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-21T18:57:43.227044+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -maxdepth 3 -name \"*.yaml\" -path \"*policy_ambiguity*\" 2>/dev/null",
  "description": "Find YAML files in project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 -maxdepth 3 -name \"*.yaml\" -path \"*policy_ambiguity*\" 2>/dev/null",
    "description": "Find YAML files in project directory"
  }
}
```

</details>

---


### Tool result

_source line 863 · 2026-05-21T18:57:43.679195+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/dream_registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/writing_plan.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/literature_map.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/mistakes.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/decisions.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/projects/policy_ambiguity_safety.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 864 · 2026-05-21T18:57:43.731327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 865 · 2026-05-21T18:57:43.832085+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded because their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted mitigation instructions without revealing the experimental manipulation. The treatment appends a type-specific disambiguation instruction to the agent's system prompt. Control rates are the matched 5-type subset from the full study (\S\ref{sec:results}).
30	
31	\begin{table*}[!ht]
32	
…[truncated 3448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 866 · 2026-05-21T18:57:47.545965+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/projects/policy_ambiguity_safety.yaml 2>/dev/null | head -60",
  "description": "Read project configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/projects/policy_ambiguity_safety.yaml 2>/dev/null | head -60",
    "description": "Read project configuration"
  }
}
```

</details>

---


### Tool result

_source line 867 · 2026-05-21T18:57:47.948051+00:00_

execution:
  account: ubuntu
  project_path: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts
  servers:
  - localhost
feishu:
  chat_id: oc_10fa2e89afc5e9b8a13613245e008dd9
  operational_chat_id: oc_c58486bc9afb8c730ded5e31c0e7d639
  review_mode: fresh
  review_paper_path: projects/policy_ambiguity_safety/docs/paper/main.tex
  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf
  review_round: 10
  review_supplementary_paths: ''
  submission_chat_id: oc_967344d166ba485ad606d14379e69d85
project:
  created_at: '2026-05-20T07:09:49.941Z'
  description: 'From Ambiguity Type to Safety Severity: Causal Mapping of Linguistic
    Policy Ambiguities to Agent Safety Violations'
  name: policy_ambiguity_safety
  phase: research
  source_idea_id: idea_034
venue: emnlp-2026

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-21T18:57:47.948450+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-21T18:57:48.002573+00:00_

100	\end{table}
101	
102	Detection difficulty is inversely correlated with agent vulnerability: incompleteness, the most dangerous type (53.6\% violation rate, \S\ref{sec:results}), is the hardest to detect (F1\,=\,0.34), while conditional precedence (36.8\% violation rate) is the easiest (F1\,=\,0.94). This asymmetry arises because types with overt linguistic signals (e.g., conditional structures) are readily detectable but only moderately dangerous, whereas missing information leaves no surface trace for a classifier to exploit.
103	
104	The primary confusion pathway is authorization scope $\to$ lexical (48\% of authorization scope clauses): authorization boundary clauses frequently contain polysemous terms, causing the classifier to attribute the ambiguity to word-level rather than permission-level underspecification.
105	
106	These results position automated detection as a viable first-pass screening tool (binary F1\,=\,0.81) but an unreliable type classifier, particularly for the highest-risk types. The classifier was evaluated on synthetic clauses derived from $\tau^2$-bench; generalization to naturally occurring policy documents requires further validation.
107	
108	\section{Replication on Additional Model Families}
109	\label{app:model_expansion}
110	
111	To test cross-architecture generalization beyond the five main-study models, we replicate the core analyses on two additional model families: Gemini-2.5-Flash (Google) and LLaMA-4-Scout (Meta), each with 250 clause pairs $\times$ 2 conditions $= 500$ episodes judged by GPT-5.4. These models represent two additional providers not in the original study. We exclude coreferential ambiguity because its disambiguation relies on benchmark-specific assertion structure rather than clause-level text changes (\S\ref{sec:taxonomy}), limiting cross-benchmark generalizability. Tables~\ref{tab:expansion_overall} and~\ref{tab:expansion_pertype} report the results.
112	
113	\begin{table}[!ht]
114	\centering
115	\small
116	\
…[truncated 11014 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 54
}
```

</details>

---


### Tool call

_source line 870 · 2026-05-21T18:58:34.360854+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "review_chat_id": "oc_967344d166ba485ad606d14379e69d85"
  }
}
```

</details>

---


### Tool result

_source line 871 · 2026-05-21T18:58:54.654969+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20294
}
```

</details>

---


### Tool call

_source line 872 · 2026-05-21T18:58:54.906293+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "你是 Reviewer 1，负责**方法严谨性与实验设计**审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026 via ACL Rolling Review (ARR May cycle)\n- **截止日期**：2026-05-25\n- **页数限制**：Long paper，正文 8 页，参考文献无限，Limitations/Ethics 不计入页数\n- **模板**：ACL template (`\\usepackage[review]{acl}`)\n- **匿名规则**：Double-blind\n- **评分标准**：ARR Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit）\n\n## 论文路径\n- TeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**核心任务**：评估实验方法论的严谨性和统计分析的可靠性。\n\n请重点审查以下方面：\n\n1. **Matched-pair 实验设计**：\n   - 300 clause pairs × 5 models = 2,997 episodes 的样本量是否充足？\n   - Matched-pair 设计是否真正建立了因果关系？有无未控制的混淆变量？\n   - Incompleteness 类型的 information-addition confound 处理是否充分？\n\n2. **统计分析**：\n   - TOST 等价检验的 SESOI ±15pp 是否合理？margin 敏感性分析是否充分？\n   - 多重比较校正（Holm-Bonferroni, 3 test families）是否恰当？\n   - Bootstrap cluster analysis 与 TOST 的一致性\n   - Variance decomposition（type 22.4% vs model 1.0%）的计算和解读\n\n3. **评估管线**：\n   - Cross-judge 设计（GPT-5.4 判 Claude/Qwen3/DeepSeek，GPT-4.1 判 GPT-5.4）是否引入 bias？\n   - Human validation（100/2997 episodes）的代表性和 per-type 可靠性\n   - Authorization scope κ=0.385 对相关 claims 的影响\n   - 四级 severity scale 的 binary threshold 选择\n\n4. **控制实验**：\n   - Perturbation control（300 episodes, Δ=-0.67pp）是否充分排除了表面扰动的影响？\n   - Reproducibility（ICC=0.919）仅限 OpenAI family 的局限性\n   - Replication（Gemini + LLaMA）的设计和结论\n\n5. **格式合规**：\n   - 正文是否在 8 页以内？\n   - 是否符合 ACL template 格式？\n   - 匿名性是否保持？\n\n请按以下结构输出审稿意见：\n```\n## Summary（2-3 句）\n## Strengths（逐条）\n## Weaknesses（逐条，标注 [MUST-FIX] 或 [SHOULD-FIX] 或 [MINOR]）\n## Questions（需要作者澄清的问题）\n## Missing References（遗漏的重要相关工作）\n## Overall Assessment（评分 + 置信度 + 一句话总结）\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "你是 Reviewer 1，负责**方法严谨性与实验设计**审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026 via ACL Rolling Review (ARR May cycle)\n- **截止日期**：2026-05-25\n- **页数限制**：Long paper，正文 8 页，参考文献无限，Limitations/Ethics 不计入页数\n- **模板**：ACL template (`\\usepackage[review]{acl}`)\n- **匿名规则**：Double-blind\n- **评分标准**：ARR Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit）\n\n## 论文路径\n- TeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**核心任务**：评估实验方法论的严谨性和统计分析的可靠性。\n\n请重点审查以下方面：\n\n1. **Matched-pair 实验设计**：\n   - 300 clause pairs × 5 models = 2,997 episodes 的样本量是否充足？\n   - Matched-pair 设计是否真正建立了因果关系？有无未控制的混淆变量？\n   - Incompleteness 类型的 information-addition confound 处理是否充分？\n\n2. **统计分析**：\n   - TOST 等价检验的 SESOI ±15pp 是否合理？margin 敏感性分析是否充分？\n   - 多重比较校正（Holm-Bonferroni, 3 test families）是否恰当？\n   - Bootstrap cluster analysis 与 TOST 的一致性\n   - Variance decomposition（type 22.4% vs model 1.0%）的计算和解读\n\n3. **评估管线**：\n   - Cross-judge 设计（GPT-5.4 判 Claude/Qwen3/DeepSeek，GPT-4.1 判 GPT-5.4）是否引入 bias？\n   - Human validation（100/2997 episodes）的代表性和 per-type 可靠性\n   - Authorization scope κ=0.385 对相关 claims 的影响\n   - 四级 severity scale 的 binary threshold 选择\n\n4. **控制实验**：\n   - Perturbation control（300 episodes, Δ=-0.67pp）是否充分排除了表面扰动的影响？\n   - Reproducibility（ICC=0.919）仅限 OpenAI family 的局限性\n   - Replication（Gemini + LLaMA）的设计和结论\n\n5. **格式合规**：\n   - 正文是否在 8 页以内？\n   - 是否符合 ACL template 格式？\n   - 匿名性是否保持？\n\n请按以下结构输出审稿意见：\n```\n## Summary（2-3 句）\n## Strengths（逐条）\n## Weaknesses（逐条，标注 [MUST-FIX] 或 [SHOULD-FIX] 或 [MINOR]）\n## Questions（需要作者澄清的问题）\n## Missing References（遗漏的重要相关工作）\n## Overall Assessment（评分 + 置信度 + 一句话总结）\n```"
  }
}
````

</details>

---


### Tool result

_source line 873 · 2026-05-21T18:59:12.392658+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17486
}
```

</details>

---


### Tool call

_source line 874 · 2026-05-21T18:59:12.543703+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "你是 Reviewer 2，负责**新颖性、理论基础与完整性**审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026 via ACL Rolling Review (ARR May cycle)\n- **截止日期**：2026-05-25\n- **页数限制**：Long paper，正文 8 页，参考文献无限，Limitations/Ethics 不计入页数\n- **模板**：ACL template (`\\usepackage[review]{acl}`)\n- **匿名规则**：Double-blind\n- **评分标准**：ARR Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit）\n\n## 论文路径\n- TeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**核心任务**：评估论文的学术贡献、理论基础和整体完整性。\n\n请重点审查以下方面：\n\n1. **新颖性与贡献定位**：\n   - 三个 contributions（因果量化、type hierarchy、disambiguation deficit）的增量贡献有多大？\n   - 与 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026) 等 concurrent work 的区分是否清晰？\n   - Matched-pair causal design 是否真正是 \"first\"？是否有类似方法论的先驱工作被遗漏？\n\n2. **Taxonomy 理论基础**：\n   - 6 类型 taxonomy 的构建依据是否充分？选择标准（frequency + theoretical distinctiveness）是否有说服力？\n   - Authorization scope 是否严格属于 \"ambiguity\"？与 vagueness 的边界？\n   - Incompleteness（information absence）作为 ambiguity 类型的理论合理性\n   - Conditional precedence（normative conflict）与 ambiguity 的关系\n   - 两层结构（linguistic vs specification）的理论价值——C3 inconclusive 后还保留的合理性\n\n3. **Framing 与叙事一致性**：\n   - Abstract/Introduction 的 claims 与正文 evidence 是否匹配？\n   - \"Differential Nocuity\" 框架的增量贡献——是否只是 Berry & Kamsties (2004) 的 trivial 推论？\n   - \"Disambiguation Deficit\" 命名是否准确——是 inability 还是 uninstructed default？\n   - Contribution list 中各项的 evidence 强度是否匹配其表述力度？\n\n4. **Related Work 覆盖**：\n   - 是否遗漏重要的 ambiguity/safety/agent 文献？\n   - 与 psycholinguistics 文献（Ferreira 2002, garden-path）的类比是否过度？\n   - Requirements engineering 文献的覆盖是否充分？\n   - 引用的准确性——检查关键引用的 author/year/title 是否正确\n\n5. **写作质量与格式**：\n   - 论文整体结构是否清晰合理？\n   - Abstract 信息密度是否适当？\n   - Limitations 是否充分覆盖关键弱点？\n   - 匿名性是否保持（检查 GitHub URL 等）？\n\n请按以下结构输出审稿意见：\n```\n## Summary（2-3 句）\n## Strengths（逐条）\n## Weaknesses（逐条，标注 [MUST-FIX] 或 [SHOULD-FIX] 或 [MINOR]）\n## Questions（需要作者澄清的问题）\n## Missing References（遗漏的重要相关工作）\n## Overall Assessment（评分 + 置信度 + 一句话总结）\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "你是 Reviewer 2，负责**新颖性、理论基础与完整性**审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026 via ACL Rolling Review (ARR May cycle)\n- **截止日期**：2026-05-25\n- **页数限制**：Long paper，正文 8 页，参考文献无限，Limitations/Ethics 不计入页数\n- **模板**：ACL template (`\\usepackage[review]{acl}`)\n- **匿名规则**：Double-blind\n- **评分标准**：ARR Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit）\n\n## 论文路径\n- TeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**核心任务**：评估论文的学术贡献、理论基础和整体完整性。\n\n请重点审查以下方面：\n\n1. **新颖性与贡献定位**：\n   - 三个 contributions（因果量化、type hierarchy、disambiguation deficit）的增量贡献有多大？\n   - 与 DRIP-R (2026)、PolicyBank (2026)、AgentPex (2026) 等 concurrent work 的区分是否清晰？\n   - Matched-pair causal design 是否真正是 \"first\"？是否有类似方法论的先驱工作被遗漏？\n\n2. **Taxonomy 理论基础**：\n   - 6 类型 taxonomy 的构建依据是否充分？选择标准（frequency + theoretical distinctiveness）是否有说服力？\n   - Authorization scope 是否严格属于 \"ambiguity\"？与 vagueness 的边界？\n   - Incompleteness（information absence）作为 ambiguity 类型的理论合理性\n   - Conditional precedence（normative conflict）与 ambiguity 的关系\n   - 两层结构（linguistic vs specification）的理论价值——C3 inconclusive 后还保留的合理性\n\n3. **Framing 与叙事一致性**：\n   - Abstract/Introduction 的 claims 与正文 evidence 是否匹配？\n   - \"Differential Nocuity\" 框架的增量贡献——是否只是 Berry & Kamsties (2004) 的 trivial 推论？\n   - \"Disambiguation Deficit\" 命名是否准确——是 inability 还是 uninstructed default？\n   - Contribution list 中各项的 evidence 强度是否匹配其表述力度？\n\n4. **Related Work 覆盖**：\n   - 是否遗漏重要的 ambiguity/safety/agent 文献？\n   - 与 psycholinguistics 文献（Ferreira 2002, garden-path）的类比是否过度？\n   - Requirements engineering 文献的覆盖是否充分？\n   - 引用的准确性——检查关键引用的 author/year/title 是否正确\n\n5. **写作质量与格式**：\n   - 论文整体结构是否清晰合理？\n   - Abstract 信息密度是否适当？\n   - Limitations 是否充分覆盖关键弱点？\n   - 匿名性是否保持（检查 GitHub URL 等）？\n\n请按以下结构输出审稿意见：\n```\n## Summary（2-3 句）\n## Strengths（逐条）\n## Weaknesses（逐条，标注 [MUST-FIX] 或 [SHOULD-FIX] 或 [MINOR]）\n## Questions（需要作者澄清的问题）\n## Missing References（遗漏的重要相关工作）\n## Overall Assessment（评分 + 置信度 + 一句话总结）\n```"
  }
}
````

</details>

---


### Tool result

_source line 875 · 2026-05-21T18:59:13.853633+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1309
}
```

</details>

---


### Assistant

_source line 876 · 2026-05-21T18:59:24.632282+00:00_

Round 10 审稿已启动。当前状态：

- **视觉审查 Agent**：已派发，并行执行中
- **Reviewer 1**（方法严谨性）：已分配，独立审稿中
- **Reviewer 2**（新颖性/完整性）：已分配，独立审稿中

等待两位 Reviewer 返回初审意见，收到后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 76

## Round 76

2 recorded events


### User

_source line 877 · 2026-05-21T19:05:52.191760+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：新颖性、理论基础与完整性

## Summary（2-3 句）

本文在 τ²-bench 上构建 300 组 matched clause pairs，通过 5 个模型（2,997 episodes）因果量化了政策歧义对 LLM agent 安全的影响（+34.0pp，OR=15.1），并提出六类型两层 taxonomy、发现"disambiguation deficit"现象（<11% awareness）。实验设计严谨、统计方法全面（TOST、bootstrap cluster、Holm-Bonferroni），但 taxonomy 的理论基础存在概念混淆（将 incompleteness 和 normative conflict 归为 ambiguity），且声称的 two-tier hierarchy 的 bootstrap 稳定性不足（34.3%），部分贡献的框架性新颖度被过度表述。

---

## Strengths（逐条）

**S1. 严谨的因果实验设计。** Matched-pair design 是本文最大亮点。每组 clause pair 仅做 minimal edit，perturbation control（synonym substitution + clause reordering，Δ=-0.67pp, CI 含零）有效排除了表面扰动的混淆。Incompleteness 的 information-addition confound 通过 logistic regression（Appendix H）和 coreferential 下界（信息delta=0, 31.6%）双重控制。这种 causal identification strategy 在 agent safety 文献中确实少见。

**S2. 统计方法论全面且透明。** TOST equivalence testing 配合七级 margin 敏感性分析（Table 2, Appendix A），bootstrap cluster analysis（Ward's method, B=10,000），Holm-Bonferroni correction 分三个 test family 适用，ICC=0.919 的可复现性验证——这是近期 agent safety 论文中统计严谨度最高的之一。SESOI=±15pp 的 anchoring 有明确的 domain-relevant 理由（超过 perturbation bound 2倍以上），且给出完整敏感性分析让读者自行判断。

**S3. 诚实报告负面/不确定结果。** C3（layer effect）inconclusive 后仍保留并解释其理论价值而非删除；authorization scope 的低 κ=0.385 在正文和 Limitations 中反复标注；bootstrap AU p-value=0.47 明确报告。这种透明度在同行评审中非常值得肯定。

**S4. 实验规模充分，覆盖面广。** 2,997 episodes × 5 primary models + 2 replication models（跨 6 providers），human validation（100 episodes, 2 annotators, κ=0.798），cross-judge calibration（100 episodes, κ=0.653）——足以支撑主要结论。Replication 在 Gemini-2.5-Flash 和 LLaMA-4-Scout 上确认 C1，增强了 generalizability。

**S5. Concurrent work 的定位清晰。** 与 DRIP-R（2026）的三点区分（causality vs correlation, safety vs decision quality, taxonomy scope）具体且有说服力。Appendix L 的 category mapping 表明作者认真研究了 concurrent work。

**S6. Disambiguation Deficit 的发现有实用价值。** 4.6% 的 overall awareness rate 和跨模型一致的 surface adoption 行为，加上 mitigation experiment（-8.5pp，Appendix B）显示该行为可改善，为 policy-governed agent 部署提供了具体的工程建议。

---

## Weaknesses（逐条）

**W1 [MUST-FIX] Two-tier hierarchy (C2) 稳定性不足，声称强于证据。**
- 具体位置：§5.2, Appendix I (Bootstrap Cluster Analysis)
- 问题：Bootstrap cluster analysis 中 incompleteness singleton 仅在 34.3% 的 bootstrap samples 中出现，AU p-value=0.47（远低于常见的 0.95 显著阈值）。TOST 分析显示在 ±10pp margin 下仅 3/6 mid-tier pairs 达到 equivalence，margin dependence 明显。Kendall's W=0.398（p=0.072）在五模型下不显著，表明模型间对 type ranking 没有一致共识。
- 但 Abstract 称"a two-tier type hierarchy separates incompleteness from the remaining five types"，Introduction contribution (2) 称"a two-tier type hierarchy showing that incompleteness constitutes an upper-bound risk tier"，Conclusion 重复此表述——这些表述的确定性远超 34.3% bootstrap support 所能支撑的。
- 为什么影响接收：C2 是三个 primary contributions 之一。如果 hierarchy 不稳定，则论文的核心叙事需要重新校准。
- 建议修改方向：(a) 在 Abstract/Intro/Conclusion 中用更谨慎的措辞，如"incompleteness tends to cluster as the highest-risk type, though the tier boundary is not sharp"；(b) 报告 AU p-value 时明确解释其意义；(c) 考虑将 C2 的核心声明缩小为"incompleteness is consistently the highest-risk type"（这在 7 个模型中有 6 个支持），而非"two-tier hierarchy"。

**W2 [SHOULD-FIX] Taxonomy 的理论基础存在概念混淆——Incompleteness 和 Conditional Precedence 并非严格意义上的 ambiguity。**
- 具体位置：§3 (Ambiguity Taxonomy), 特别是 "Scope of 'ambiguity'" paragraph
- 问题：论文定义 ambiguity 为"admits multiple distinct interpretations available to a competent reader"（引 Wasow et al. 2005）。但：
  - **Incompleteness**（missing conditions/exceptions）不是"multiple interpretations"——而是 information absence。当政策没有说明损坏物品的退货规则时，这不是"two readings"，而是"no reading"。论文自身承认"resolution requires adding content"（§3），这恰恰说明它不是 ambiguity 的 resolution 而是 specification gap 的 filling。
  - **Conditional precedence**（conflicting rules）也不是 ambiguity——两条矛盾的规则各自是清晰的，问题在于 normative conflict 而非 interpretation uncertainty。论文承认这是"normative conflict between individually unambiguous rules"（§3）。
  - §3 的辩护是"LLM agents process all six types identically—committing to a single interpretation without flagging uncertainty"。但这是用行为结果反过来定义输入类型——循环论证。行为相似不意味着现象同质。
- 为什么影响评分：taxonomy 是 C2 hierarchy 的基础。如果 incompleteness 不属于 ambiguity，那 C2 的"ambiguity type hierarchy"就是在比较 apples 和 oranges。incompleteness 的 49.2pp 效应可能主要反映 information deficit 而非 ambiguity severity。
- 建议修改方向：(a) 明确将 taxonomy 定位为"policy specification defects"或"interpretation challenges"，而非严格的"ambiguity types"；(b) 在 §3 更充分地讨论 ambiguity vs incompleteness vs normative conflict 的理论边界；(c) 或者保持 broad definition 但在 Discussion 中更深入地讨论这种 definitional choice 的影响。

**W3 [SHOULD-FIX] "Differential Nocuity" 框架的增量贡献被过度表述。**
- 具体位置：§7 Discussion, "Differential nocuity" paragraph
- 问题：Berry & Kamsties (2004) 已经区分 nocuous vs innocuous ambiguity。Chantree et al. (2006) 和 Willis et al. (2008) 已经测量了不同 ambiguity types 的 nocuity 程度并训练了 nocuity classifiers。"Differential nocuity"（不同类型有不同危害程度）并非新概念——它是 nocuous ambiguity 研究的自然推论。
- 论文的真正贡献是**在 LLM agent 场景下实证验证了 differential nocuity**，并引入了 safety training 和 disambiguation channel 两个新调节变量。但 §7 的写法将 "differential nocuity" 框架化为一个新的理论贡献（"our results can be interpreted through a differential nocuity lens"），这忽略了已有文献中类似的 type-specific nocuity 分析。
- 建议修改方向：明确将"differential nocuity"定位为已有概念在新领域的验证和扩展，而非暗示性地作为新框架。可以写作"extending Berry and Kamsties' nocuous/innocuous distinction, our results reveal differential nocuity across types in the LLM agent context, modulated by two factors absent in human RE: safety training and disambiguation channel availability."

**W4 [SHOULD-FIX] "Disambiguation Deficit" 命名不准确——是 uninstructed default 还是 inability？**
- 具体位置：§6.2
- 问题："Deficit"暗示能力缺失。但 §6.2 自己承认："agents are not inherently incapable of disambiguation—our mitigation experiment shows -8.5pp improvement." 这说明不是 deficit（能力缺陷），而是 **uninstructed default behavior**——模型在没有被明确指示时默认采用 single-parse adoption。
- Mitigation 实验（Appendix B）进一步表明，仅通过 system prompt 添加 type-specific disambiguation instruction 就能减少违规，说明这更像是一个 prompting/design gap 而非模型的内在缺陷。
- "Deficit"这个术语可能误导读者认为这是一个需要模型层面修复的问题，而实际上它可能主要需要 prompt engineering 或 system design 层面的解决方案。
- 建议修改方向：考虑使用更精确的术语如 "Disambiguation Gap" 或 "Default Surface Adoption"；或者保留 "Deficit" 但在定义时明确它指的是 "absence of disambiguation behavior in default (uninstructed) settings" 而非 inability。

**W5 [SHOULD-FIX] Authorization scope 的结论可靠性受 low agreement 严重影响。**
- 具体位置：§5.2, §5.4, Table 1, Limitations
- 问题：Authorization scope 有全文最低的 cross-judge κ=0.385（§4.4），human-LLM κ=0.644（Appendix G, Table 8），且有最大的 52pp 跨模型范围。论文在多处标注了这一点，但 C4 的核心叙事仍然把 authorization scope 作为"most model-differentiating type"来讲——一个 measurement reliability 最差的维度上的最大差异，很可能部分反映了 measurement noise 而非 true signal。
- κ=0.385 在 Landis & Koch 分类中属于"fair agreement"，意味着 judge 之间在该类型上的一致性接近随机。52pp range 中有多少归因于真实的模型差异、多少归因于 judge noise，无法分离。
- 建议修改方向：(a) 在 §5.4 中更明确地将 auth scope 的 C4 分析标记为 tentative/unreliable，而不仅仅是 "suggestive"；(b) 考虑在 Abstract 中移除或弱化 "authorization scope vulnerability varies 52pp" 的表述（因为这个数字的可信度不够）。

**W6 [MINOR] Psycholinguistics 类比可能 over-extended。**
- 具体位置：§2 Related Work "Psycholinguistics of ambiguity processing", §6.1, §6.2
- 问题：将 LLM 的 surface adoption 比作 Frazier & Rayner (1982) 的 garden-path processing 和 Ferreira (2002) 的 good-enough representations 是有趣的，但 mechanistically misleading。LLM 的 autoregressive token-by-token generation 与人类增量句子解析在计算机制上完全不同。Garden-path effects 涉及人类有限的 working memory 和 reanalysis cost；LLM 的 single-parse adoption 更可能反映训练分布（大多数训练数据中 ambiguity 已被上下文解消）而非类似人类的 processing constraint。
- 论文用 "paralleling" 和 "analogous" 等措辞保持了一定的审慎，但 §6.2 将 disambiguation deficit "paralleling human good-enough processing" 作为核心框架可能让读者高估了类比的深度。
- 建议：加一句 caveat 如 "though the underlying mechanisms are likely distinct" 或降级为 illustrative analogy。

**W7 [MINOR] 引用问题。**
- `ferrari_defects_2018`：bib entry 的第一作者是 Rosadini, Benedetta，但 bib key 用 ferrari，OpenAlex 也确认第一作者不匹配。实际论文的第一作者是 Rosadini et al. (2019) 而非 Ferrari，且年份应为 2019（bib 标注 2019 但 key 写 2018）。
- 2 个 orphan bib entries（`tamkin_evaluating_2023`, `yin_safeagentbench_2025`）在正文中未被引用。
- `navigli_wsd_2009`：OpenAlex 匹配到不同年份/作者的论文，建议确认原始 Navigli (2009) ACM Computing Surveys 的准确性。

---

## Questions（需要作者澄清的问题）

**Q1.** §3 将 incompleteness 定义为 ambiguity，但 Wasow et al. (2005) 的 ambiguity 定义要求"multiple distinct interpretations"。当政策完全没有提及某个 edge case 时，何来"多种解读"？请解释为什么 information absence 满足 ambiguity 的定义，而不是一个独立的 specification defect 类别。

**Q2.** Bootstrap cluster analysis（Appendix I）中 incompleteness singleton 仅在 34.3% 的 samples 中出现。如果将 within-type variance 考虑在内，two-tier structure 的证据强度如何与 "more-of-a-continuum" 假说区分？

**Q3.** Mitigation experiment（Appendix B）中 coreferential 被排除。但 coreferential 是 information-delta=0 的"纯粹 ambiguity"类型，也是 violation rate 最低的类型（31.6%）。如果 mitigation 对这个最"纯粹"的 ambiguity 类型无效（或有效），将对 disambiguation deficit 的解释产生重要影响。是否有计划补充？

**Q4.** Clause pairs 通过 template-based pipeline 生成——是否存在某些 template patterns 系统性地比其他 patterns 更容易触发违规？Appendix J 的 LOO 分析显示 max shift 仅 1.4pp，但这是 type-level LOO。是否检查过 clause-level 的 per-template variation？

**Q5.** 关于 SESOI=±15pp 的选择：如果一个 ambiguity type 的 violation rate 差异为 12pp（低于 SESOI），在实际部署中这仍然可能代表数千个有害 interaction。±15pp 的 anchoring 可能对 high-stakes domain（医疗、金融）过于宽松。作者是否考虑过 domain-specific SESOI？

---

## Missing References（遗漏的重要相关工作）

1. **Dalpiaz, van der Schalk, & Lucassen (2018)**. "Pinpointing Ambiguity and Incompleteness in Requirements Engineering via Information Visualization and NLP." REFSQ 2018. 直接相关——该工作明确区分 ambiguity 和 incompleteness 作为两种不同的 requirements defects，与本文将 incompleteness 归为 ambiguity 的决定形成对比。

2. **Yu, Carroll, & Bentley (2026)**. "The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents." arXiv:2603.20320. Concurrent work，同样使用 matched-pair causal design 研究 LLM agent safety（IV 为 tool affordance 而非 ambiguity）。对本文 "first causal quantification" claim 需要更精确的 scoping。

3. **Lin et al. (2025)**. "Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue." arXiv:2509.15061. 与 disambiguation channel design 和 disambiguation deficit 的讨论相关。

4. 建议引用 Willis et al. (2008) 在 §7 Discussion 中讨论 differential nocuity 时不仅作为 detection 的引用（§2 已引），还需在 §7 中更明确地 credit 其对 type-specific nocuity 的先驱测量工作。

---

## Overall Assessment

**Overall**: 3.5（Borderline Conference）
**Confidence**: 4/5（仔细阅读全文、附录、引用核查，熟悉相关领域）

### 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | C1 实验设计严谨、控制充分，是本文最强的贡献。但 C2 hierarchy 的 bootstrap 稳定性不足（34.3%），taxonomy 将 non-ambiguity phenomena 归为 ambiguity 构成概念混淆，auth scope 的 low agreement 影响 C4 结论可靠性。 |
| Excitement | 3/5 | 研究问题重要且时机恰当——policy ambiguity 对 agent safety 的影响确实需要实证研究。但理论贡献有限（differential nocuity 是已有概念的 domain transfer，taxonomy 的 theoretical grounding 不够），且 C2 hierarchy 在实际部署指导中的 actionability 不清楚。 |
| Reproducibility | 4/5 | 方法描述详尽，数据/代码承诺开源，统计分析可复现。但依赖 commercial API models（temperature=0 但 API 行为可能随时间变化），且 clause pair 的 template-based generation pipeline 细节不足。 |
| Datasets/Software | 3.5/5 | 300 clause pairs + evaluation pipeline 对社区有用，但 (a) synthetic nature 限制了对 naturally-occurring ambiguity 的泛化，(b) 仅覆盖 retail/airline 两个 domain。 |

### 一句话总结

C1 的 causal finding（+34pp, OR=15.1）是扎实的实证贡献，但 taxonomy 的理论基础和 C2 hierarchy 的统计稳定性不足以支撑论文当前的 framing——建议缩小理论声明范围、增加对 taxonomy definitional choices 的讨论、弱化 hierarchy 的确定性表述，可升至 Conference 水平。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 878 · 2026-05-21T19:05:59.108352+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 77

## Round 77

2 recorded events


### User

_source line 879 · 2026-05-21T19:06:10.395189+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**核心判断：Overall 3.5（Borderline Conference）**

主要发现：
- **C1（+34pp causal effect）是本文最强的贡献**，matched-pair design + perturbation control 严谨
- **C2 two-tier hierarchy 声称过强**：bootstrap 仅 34.3% 支持，Kendall's W 五模型下不显著（p=0.072）
- **Taxonomy 理论基础有概念混淆**：incompleteness（information absence）和 conditional precedence（normative conflict）不满足 Wasow (2005) 对 ambiguity 的定义
- **Differential Nocuity 和 Disambiguation Deficit 的新颖度被过度表述**——前者是 Berry & Kamsties 的 domain transfer，后者是 uninstructed default 而非 inability
- Authorization scope 的 κ=0.385 严重影响 C4 中 52pp range 的可信度

标记了 1 个 MUST-FIX（C2 稳定性）、4 个 SHOULD-FIX、2 个 MINOR，附 5 个 Questions 和 4 个 Missing References。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 880 · 2026-05-21T19:06:16.955733+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 78

## Round 78

6 recorded events


### User

_source line 881 · 2026-05-21T19:06:48.273338+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性与实验设计

## Summary（2-3 句）

本文提出首个针对策略歧义（policy ambiguity）与 LLM agent 安全违规之间因果关系的 matched-pair 实验研究。基于 τ²-bench，构建 300 组 clause pairs（6 种歧义类型），在 5 个模型上运行 2,997 episodes，发现歧义使违规率上升 34 pp（OR=15.1），并呈现以 incompleteness 为上界的两层类型层级。实验设计整体严谨，统计分析覆盖面广（TOST 等价检验、bootstrap 聚类、logistic regression），对局限性的透明度在同类工作中属上乘；但 authorization scope 的测量可靠性不足以支撑其核心发现地位，incompleteness confound 仅部分控制，per-type 人工验证样本量偏小。

## Strengths（逐条）

**S1. 问题定位精准且新颖。** 将 RE（需求工程）中经典的歧义分类框架迁移到 LLM agent 安全领域，填补了"歧义类型→安全违规"因果映射的空白。Berry & Kamsties (2004) 的 nocuous/innocuous 区分在 agent 场景下的重新验证（所有歧义对 agent 均为 nocuous）是有理论价值的发现。

**S2. Matched-pair 设计是正确的因果推断策略。** 300 组 clause pairs × 2 conditions 构成了 within-clause 比较，每个 clause 既作为自己的 treatment 又作为 control，有效控制了 clause-level 混淆变量。perturbation control（Δ=-0.67 pp, CI 含零）进一步排除了表面扰动的影响。

**S3. 统计分析全面且方法得当。**
- TOST 等价检验配合 7 个 margin 的 sensitivity analysis（Table 2, Appendix A），避免了仅依赖 NHST 的常见问题。
- Bootstrap 聚类分析作为 margin-free 补充方法，与 TOST 结论一致。
- Holm-Bonferroni 校正在 3 个 pre-registered test families 内分别应用。
- Variance decomposition（type 22.4% vs model 1.0%）和 logistic regression 提供了多维度证据。
- Post-hoc power 分析报告（C1/C2 >0.99; TOST ±15pp 0.94）让读者可评估检测力。

**S4. 局限性透明度出色。** 论文在 Limitations 中主动讨论了：authorization scope κ=0.385、incompleteness information-addition confound、cross-judge asymmetry、per-type 小样本 CI、sentence length 差异等。许多同类论文不会如此坦诚。C3（layer effect）被明确标注为 inconclusive。

**S5. 跨模型复制增强泛化性。** 7 个模型覆盖 6 个 provider（4 proprietary + 3 open-source），其中 Gemini 和 LLaMA 作为独立复制。Incompleteness 在所有 7 个模型中均 ≥46%，这一致性强化了 C2。

**S6. Failure mode taxonomy 基于大规模经验证据。** 614 条 violation traces 的编码分析揭示了三种机制上不同的失败模式（structural misparse、information gap-filling、boundary violation），且与输入歧义类型形成可解释的对应关系。Gwet's AC₁=0.62 的 inter-coder 可靠性合理。

**S7. Disambiguation Deficit 是一个干净的新发现。** 整体 4.6% 的歧义识别率，特别是 Qwen3 和 DeepSeek 为零，是一个有实际影响的定量事实。

## Weaknesses（逐条）

**W1 [MUST-FIX] Authorization scope 发现的表述强度超出了测量可靠性所能支撑的范围。**
- 具体位置：Abstract、Section 1（Introduction）、Section 5.4（C4）、Figure 3
- 问题：Authorization scope 是论文的关键卖点之一——"the widest cross-model range (52 pp)"、"safety training may differentially mitigate specific ambiguity types"。但其 cross-judge κ=0.385（Section 4.4），低于通常的 "fair agreement" 门槛（0.40）。per-type human-LLM κ=0.644（Appendix G, Table 8），CI [0.35, 0.91]。这意味着该类型的绝对违规率比其他类型有显著更多的测量噪声。
- Abstract 中的括号注释 "though measured with the lowest inter-judge agreement, κ=0.385" 过于弱化——读者很容易忽略。在 Introduction 中复述 52 pp 时未提及可靠性。
- 为什么影响接收：这削弱了 C4 交互效应的一个核心论据。52 pp range 中有多少来自真实的模型差异、多少来自 judge 在 authorization boundary 判定上的不一致，无法区分。
- 建议修改方向：(1) 在 Abstract 中将 authorization scope 从"主要发现"降格为"初步发现"，明确标注不确定性；(2) 在 Introduction 中同等篇幅讨论可靠性限制；(3) 考虑在 C4 分析中展示去除 authorization scope 后的交互效应是否仍然显著。

**W2 [SHOULD-FIX] Incompleteness confound 的控制力度不足以支撑其在两层层级中的独立地位。**
- 具体位置：Section 5.2、Appendix E、Appendix F
- 问题：Incompleteness 的 unambiguous variant 必然添加新政策内容（如补充缺失的退货条件），这不仅仅是"token count difference"的问题——它改变了策略的语义覆盖范围。Logistic regression 控制 token delta（p=0.022, coefficient change <8%）使用的是 token count 这一"coarse proxy"（论文原文承认），而更细粒度的语义衡量（如命题内容数量）可能揭示不同的 confound 结构。
- 论文用 coreferential 的 31.6%（zero information delta）作为下界——这很巧妙，但它约束的是所有歧义的下界，而不是 incompleteness 的特定贡献。无法从中推断 incompleteness 的 49.2 pp 效应中有多少归因于歧义消解、多少归因于信息增补。
- 建议：(1) 设计信息量和歧义正交变化的 ablation（如添加同等信息量但不消解歧义的 control）；(2) 在当前版本中，将 incompleteness 在两层层级中的地位明确标注为 "conditional on confound assumptions"。

**W3 [SHOULD-FIX] 条件间句子长度差异（d=0.74）可能是未控制的混淆变量。**
- 具体位置：Limitations 段落 "Synthetic ambiguity"
- 问题：Ambiguous clauses 的句子长度 "moderately higher"（Cohen's d=0.74）。这是一个中等到大的效应量。更长的 clause 通常包含更多的处理负担，可能独立于歧义导致 agent 犯错。Perturbation control 使用 synonym substitution 和 clause reordering，这些变换不会系统性改变句长，因此不能排除长度 confound。
- 关键问题：句子长度是否与歧义类型相关？如果 incompleteness clauses 系统性更长，这会进一步加剧 W2 的问题。
- 建议：(1) 报告 per-type 句长分布和 condition×type 交互；(2) 在 logistic regression 中加入句长作为协变量。

**W4 [SHOULD-FIX] Per-type 人工验证严重不足，无法支撑 type-level 结论。**
- 具体位置：Section 4.4（Human validation）、Appendix G（Table 8）
- 问题：100 episodes / 6 types = 32-34 per type。Scopal 的 human-LLM κ CI 为 [0.00, 1.00]——完全无信息。Coreferential 为 [0.00, 0.84]——几乎无信息。这些 CIs 无法排除 human-LLM agreement 实际很差的可能性。
- 论文的核心贡献是 type-level 的差异化分析（C2），但 per-type 验证的精度远不足以支撑这一粒度。Overall κ=0.733 是可接受的，但 overall 验证不能替代 per-type 验证。
- 建议：(1) 扩大人工标注样本至每类 ≥80 episodes（总计 ≥480），以获得信息量充足的 per-type κ 估计；(2) 在当前版本中，至少在方法论章节（而非仅 Appendix）明确标注 per-type 验证的精度限制。

**W5 [SHOULD-FIX] Cross-judge 设计使 judge identity 与 model identity 混淆。**
- 具体位置：Section 4.4、Limitations
- 问题：GPT-5.4 判 3 个模型，GPT-4.1 判 1 个模型。论文论证 matched-pair 设计下 judge bias 在 Δpp 中抵消——这对 C1 是成立的。但 C2 的类型比较使用了跨模型的 pooled 绝对违规率（Table 1），这些数字受 judge identity 影响。
- 更具体地：within-judge-group C3 分析各自未达显著（GPT-4.1-judged p=0.059; GPT-5.4-judged p=0.157），暗示 pooled C3 结果可能部分反映 judge-level variance 而非真实的 layer effect。
- C4 中 authorization scope 的 Claude 12% vs GPT-5.4 64% 这一对比中，Claude 由 GPT-5.4 判，GPT-5.4 由 GPT-4.1 判——不同 judge 可能对"authorization boundary violation"有不同判定标准。论文用 within-judge bootstrap ranking preservation (99.5%) 部分缓解了这一担忧，但仅限于 GPT-5.4 作为 judge 的子集。
- 建议：(1) 补充双 judge 评估至少覆盖全部类型×模型组合的一个子集（不仅是 100 episodes 的 calibration）；(2) 报告 C2 的 within-judge-group 分析结果，验证类型层级是否在单一 judge 内复现。

**W6 [SHOULD-FIX] 两层层级的稳定性依赖于 margin 选择。**
- 具体位置：Section 5.2、Table 2 (Appendix A)
- 问题：在 ±10 pp 时只有 3/6 mid-tier pairs 等价（power=0.57）。两层结构直到 ±15 pp 才稳定（6/6）。Bootstrap 聚类的 AU p-value 为 0.47——这意味着在约一半的 bootstrap 样本中，incompleteness 不构成独立 cluster。
- 论文对此透明（"margin dependence"、完整 sensitivity table），但 ±15 pp 的选择对两层叙事有利。如果 SESOI 为 ±10 pp（一个同样可合理论证的 threshold），mid-tier 内部的等价性就不成立。
- 建议：(1) 在正文中更突出地讨论 margin 敏感性——目前完整 table 仅在 Appendix A；(2) 考虑将 ±10 pp 的结果（"three-tier" rather than "two-tier"）与 ±15 pp 的结果并列呈现，让读者自行判断。

**W7 [MINOR] Clause pair 构建的 inter-annotator agreement 报告不完整。**
- 具体位置：Section 4.2
- 问题：报告了 96% pass rate，但未报告 type assignment 的 Cohen's κ 或 Fleiss' κ。Pass rate 不区分 agreement 和 chance agreement。
- 建议：补充 type assignment 的标准可靠性指标。

**W8 [MINOR] 引用问题。**
- 2 个 orphan bib entries：tamkin_evaluating_2023、yin_safeagentbench_2025（在 .bib 中但未被引用）。
- `ferrari_defects_2018` 的 bib 条目第一作者为 Rosadini（非 Ferrari），但论文中引用为 Ferrari et al. / Rosadini et al.——需核实。

**W9 [MINOR] Reproducibility ICC 仅覆盖 OpenAI 模型族。**
- 具体位置：Section 4.5
- 问题：ICC=0.919 仅基于 GPT 模型族内的 30 clause pairs × 2 models × 3 replicates。跨 provider 的 test-retest 可靠性未测量。在 temperature=0 设置下，同一 provider 内的高 ICC 不令人意外；有意义的是跨 provider 稳定性。
- 建议：至少在 1-2 个非 OpenAI 模型上补充 test-retest data。

## Questions（需要作者澄清的问题）

**Q1.** Sentence length (d=0.74) 与 ambiguity type 的相关性如何？如果 incompleteness clauses 系统性更长，W2 和 W3 的 confound 将叠加。请报告 per-type 的条件间长度差异。

**Q2.** Variance decomposition 中 type 解释 22.4%，model 解释 1.0%——剩余约 76% 的方差来源是什么？是否主要是 clause-level heterogeneity？如果是，这是否意味着 type 内部的 clause 间变异远大于 type 间变异，从而削弱 type-level 概括的信度？

**Q3.** Perturbation control 的 300 episodes 覆盖了几个模型？是否在所有 5 个主模型上均匀分布？

**Q4.** Clause pair 标注中 96% pass rate 的评判标准是什么？两位标注者在 type assignment 上的 agreement κ 是多少？

**Q5.** 50 clause pairs per type 是否在两个 τ²-bench domain（retail + airline）间均匀分布？如果不是，domain 是否是一个混淆变量？

**Q6.** Mitigation experiment 中 coreferential 被排除的理由是 "impossible to craft targeted mitigation instructions without revealing the experimental manipulation"——但这种类型在主实验中有 31.6% 的违规率。是否可以设计不依赖于类型知识的通用 disambiguation prompt？

**Q7.** 论文声称 "all policy ambiguity is nocuous for LLM agents"（Introduction），但 coreferential 的效应量（18.7 pp）远小于 incompleteness（49.2 pp），且 coreferential 的 human-LLM κ CI 为 [0.00, 0.84]——在 confidence 如此低的情况下，对 coreferential 的 nocuity 声称是否过强？

## Missing References（遗漏的重要相关工作）

1. **Tamkin et al. (2023)** "Evaluating and Mitigating Discrimination in Language Model Decisions" — 已在 .bib 中但未被引用，与 authorization scope 下 agent 权限判定的偏差讨论相关。

2. **Mu et al. (2023)** "Can LLMs Follow Simple Rules?" 或类似的 rule-following compliance benchmark——与本文的 policy compliance 主题直接相关，可补充 Related Work 中 agent safety evaluation 段落。

3. 缺少对 **vagueness** 文献的更深入讨论。论文在 Section 3 承认 authorization scope 与 vagueness 重叠、incompleteness 与 information absence 重叠，但仅引用了 Kennedy (2007)。Deemter (2010) "Not Exactly: In Praise of Vagueness" 和 Lassiter & Goodman (2017) 的 probabilistic pragmatics 工作可以丰富理论基础。

## Overall Assessment

**Overall**: 3.5 / 5（Borderline Conference）
**Soundness**: 3.5 / 5
**Excitement**: 3.5 / 5
**Reproducibility**: 4 / 5
**Confidence**: 4 / 5（我仔细检查了实验设计、统计方法和关键数据，对相关领域较熟悉）

**一句话总结**：这是一项设计精心、分析全面的因果实验研究，核心发现（C1: 歧义整体致害性；C2: 类型层级，尤其 incompleteness 的一致性上界）在主实验和复制实验中都稳健；但 authorization scope 的低测量可靠性（κ=0.385）使得 C4 中的关键模式不够确定，incompleteness confound 仅有粗粒度控制，per-type 人工验证欠缺统计力度。修订 W1（降低 authorization scope claims 的表述强度）和 W4（扩大 per-type 验证样本）后，可达 Conference 水平。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 882 · 2026-05-21T19:07:26.342704+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应其 Weaknesses：对每条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。也请评论其 Questions 和 Missing References 中你认为重要的点。\n\n---\n\n# Reviewer 1 审稿意见：方法严谨性与实验设计\n\n## Summary（2-3 句）\n\n本文提出首个针对策略歧义（policy ambiguity）与 LLM agent 安全违规之间因果关系的 matched-pair 实验研究。基于 τ²-bench，构建 300 组 clause pairs（6 种歧义类型），在 5 个模型上运行 2,997 episodes，发现歧义使违规率上升 34 pp（OR=15.1），并呈现以 incompleteness 为上界的两层类型层级。实验设计整体严谨，统计分析覆盖面广（TOST 等价检验、bootstrap 聚类、logistic regression），对局限性的透明度在同类工作中属上乘；但 authorization scope 的测量可靠性不足以支撑其核心发现地位，incompleteness confound 仅部分控制，per-type 人工验证样本量偏小。\n\n## Strengths（逐条）\n\nS1. 问题定位精准且新颖。\nS2. Matched-pair 设计是正确的因果推断策略。\nS3. 统计分析全面且方法得当。\nS4. 局限性透明度出色。\nS5. 跨模型复制增强泛化性。\nS6. Failure mode taxonomy 基于大规模经验证据。\nS7. Disambiguation Deficit 是一个干净的新发现。\n\n## Weaknesses（逐条）\n\n**W1 [MUST-FIX] Authorization scope 发现的表述强度超出了测量可靠性所能支撑的范围。**\n- Authorization scope 的 cross-judge κ=0.385，低于 \"fair agreement\" 门槛（0.40）。per-type human-LLM κ=0.644，CI [0.35, 0.91]。\n- Abstract 中的括号注释过于弱化——读者很容易忽略。Introduction 中复述 52 pp 时未提及可靠性。\n- 建议：(1) 在 Abstract 中将 authorization scope 从\"主要发现\"降格为\"初步发现\"；(2) Introduction 中同等篇幅讨论可靠性限制；(3) 考虑展示去除 auth scope 后的 C4 交互效应是否仍然显著。\n\n**W2 [SHOULD-FIX] Incompleteness confound 的控制力度不足以支撑其在两层层级中的独立地位。**\n- Token count 是 \"coarse proxy\"，更细粒度的语义衡量可能揭示不同的 confound 结构。\n- Coreferential 的 31.6% 约束的是所有歧义的下界，而非 incompleteness 的特定贡献。\n- 建议：(1) 设计信息量和歧义正交变化的 ablation；(2) 将 incompleteness 标注为 \"conditional on confound assumptions\"。\n\n**W3 [SHOULD-FIX] 条件间句子长度差异（d=0.74）可能是未控制的混淆变量。**\n- 更长的 clause 可能独立于歧义导致 agent 犯错。Perturbation control 不能排除长度 confound。\n- 建议：(1) 报告 per-type 句长分布和 condition×type 交互；(2) 在 logistic regression 中加入句长作为协变量。\n\n**W4 [SHOULD-FIX] Per-type 人工验证严重不足。**\n- 100 episodes / 6 types = 32-34 per type。Scopal 的 CI 为 [0.00, 1.00]，完全无信息。\n- 建议：扩大人工标注至每类 ≥80 episodes。\n\n**W5 [SHOULD-FIX] Cross-judge 设计使 judge identity 与 model identity 混淆。**\n- C2 的类型比较使用了跨模型的 pooled 绝对违规率，受 judge identity 影响。\n- Within-judge-group C3 各自未达显著（GPT-4.1-judged p=0.059; GPT-5.4-judged p=0.157）。\n- 建议：(1) 补充双 judge 评估覆盖更多组合；(2) 报告 C2 的 within-judge-group 分析。\n\n**W6 [SHOULD-FIX] 两层层级的稳定性依赖于 margin 选择。**\n- ±10 pp 时只有 3/6 mid-tier pairs 等价（power=0.57）。Bootstrap AU p-value=0.47。\n- 建议：在正文中更突出地讨论 margin 敏感性，并列呈现 ±10 pp 的 \"three-tier\" 替代叙事。\n\n**W7 [MINOR] Clause pair 构建的 inter-annotator agreement 报告不完整。** 未报告 type assignment 的 κ。\n\n**W8 [MINOR] 引用问题。** 2 个 orphan bib entries + ferrari_defects_2018 作者不一致。\n\n**W9 [MINOR] Reproducibility ICC 仅覆盖 OpenAI 模型族。**\n\n## Questions\n\nQ1. Per-type sentence length 差异？\nQ2. Variance decomposition 中剩余 ~76% 方差来源？\nQ3. Perturbation control 的模型分布？\nQ4. Clause pair 标注 κ？\nQ5. Clause pairs 的 domain 分布？\nQ6. Coreferential 排除理由是否成立？\nQ7. Coreferential 的 nocuity 声称在低 κ CI 下是否过强？\n\n## Missing References\n\n1. Tamkin et al. (2023) — authorization scope 偏差相关\n2. Mu et al. (2023) \"Can LLMs Follow Simple Rules?\" — policy compliance 相关\n3. Deemter (2010), Lassiter & Goodman (2017) — vagueness 文献"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应其 Weaknesses：对每条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。也请评论其 Questions 和 Missing References 中你认为重要的点。\n\n---\n\n# Reviewer 1 审稿意见：方法严谨性与实验设计\n\n## Summary（2-3 句）\n\n本文提出首个针对策略歧义（policy ambiguity）与 LLM agent 安全违规之间因果关系的 matched-pair 实验研究。基于 τ²-bench，构建 300 组 clause pairs（6 种歧义类型），在 5 个模型上运行 2,997 episodes，发现歧义使违规率上升 34 pp（OR=15.1），并呈现以 incompleteness 为上界的两层类型层级。实验设计整体严谨，统计分析覆盖面广（TOST 等价检验、bootstrap 聚类、logistic regression），对局限性的透明度在同类工作中属上乘；但 authorization scope 的测量可靠性不足以支撑其核心发现地位，incompleteness confound 仅部分控制，per-type 人工验证样本量偏小。\n\n## Strengths（逐条）\n\nS1. 问题定位精准且新颖。\nS2. Matched-pair 设计是正确的因果推断策略。\nS3. 统计分析全面且方法得当。\nS4. 局限性透明度出色。\nS5. 跨模型复制增强泛化性。\nS6. Failure mode taxonomy 基于大规模经验证据。\nS7. Disambiguation Deficit 是一个干净的新发现。\n\n## Weaknesses（逐条）\n\n**W1 [MUST-FIX] Authorization scope 发现的表述强度超出了测量可靠性所能支撑的范围。**\n- Authorization scope 的 cross-judge κ=0.385，低于 \"fair agreement\" 门槛（0.40）。per-type human-LLM κ=0.644，CI [0.35, 0.91]。\n- Abstract 中的括号注释过于弱化——读者很容易忽略。Introduction 中复述 52 pp 时未提及可靠性。\n- 建议：(1) 在 Abstract 中将 authorization scope 从\"主要发现\"降格为\"初步发现\"；(2) Introduction 中同等篇幅讨论可靠性限制；(3) 考虑展示去除 auth scope 后的 C4 交互效应是否仍然显著。\n\n**W2 [SHOULD-FIX] Incompleteness confound 的控制力度不足以支撑其在两层层级中的独立地位。**\n- Token count 是 \"coarse proxy\"，更细粒度的语义衡量可能揭示不同的 confound 结构。\n- Coreferential 的 31.6% 约束的是所有歧义的下界，而非 incompleteness 的特定贡献。\n- 建议：(1) 设计信息量和歧义正交变化的 ablation；(2) 将 incompleteness 标注为 \"conditional on confound assumptions\"。\n\n**W3 [SHOULD-FIX] 条件间句子长度差异（d=0.74）可能是未控制的混淆变量。**\n- 更长的 clause 可能独立于歧义导致 agent 犯错。Perturbation control 不能排除长度 confound。\n- 建议：(1) 报告 per-type 句长分布和 condition×type 交互；(2) 在 logistic regression 中加入句长作为协变量。\n\n**W4 [SHOULD-FIX] Per-type 人工验证严重不足。**\n- 100 episodes / 6 types = 32-34 per type。Scopal 的 CI 为 [0.00, 1.00]，完全无信息。\n- 建议：扩大人工标注至每类 ≥80 episodes。\n\n**W5 [SHOULD-FIX] Cross-judge 设计使 judge identity 与 model identity 混淆。**\n- C2 的类型比较使用了跨模型的 pooled 绝对违规率，受 judge identity 影响。\n- Within-judge-group C3 各自未达显著（GPT-4.1-judged p=0.059; GPT-5.4-judged p=0.157）。\n- 建议：(1) 补充双 judge 评估覆盖更多组合；(2) 报告 C2 的 within-judge-group 分析。\n\n**W6 [SHOULD-FIX] 两层层级的稳定性依赖于 margin 选择。**\n- ±10 pp 时只有 3/6 mid-tier pairs 等价（power=0.57）。Bootstrap AU p-value=0.47。\n- 建议：在正文中更突出地讨论 margin 敏感性，并列呈现 ±10 pp 的 \"three-tier\" 替代叙事。\n\n**W7 [MINOR] Clause pair 构建的 inter-annotator agreement 报告不完整。** 未报告 type assignment 的 κ。\n\n**W8 [MINOR] 引用问题。** 2 个 orphan bib entries + ferrari_defects_2018 作者不一致。\n\n**W9 [MINOR] Reproducibility ICC 仅覆盖 OpenAI 模型族。**\n\n## Questions\n\nQ1. Per-type sentence length 差异？\nQ2. Variance decomposition 中剩余 ~76% 方差来源？\nQ3. Perturbation control 的模型分布？\nQ4. Clause pair 标注 κ？\nQ5. Clause pairs 的 domain 分布？\nQ6. Coreferential 排除理由是否成立？\nQ7. Coreferential 的 nocuity 声称在低 κ CI 下是否过强？\n\n## Missing References\n\n1. Tamkin et al. (2023) — authorization scope 偏差相关\n2. Mu et al. (2023) \"Can LLMs Follow Simple Rules?\" — policy compliance 相关\n3. Deemter (2010), Lassiter & Goodman (2017) — vagueness 文献"
  }
}
```

</details>

---


### Tool result

_source line 883 · 2026-05-21T19:07:59.597406+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 33254
}
```

</details>

---


### Tool call

_source line 884 · 2026-05-21T19:08:00.251318+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "policy_ambiguity_safety",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Weaknesses：对每条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。也请评论其 Questions 和 Missing References 中你认为重要的点。\n\n---\n\n# Reviewer 2 审稿意见：新颖性、理论基础与完整性\n\n## Summary（2-3 句）\n\n本文在 τ²-bench 上构建 300 组 matched clause pairs，通过 5 个模型（2,997 episodes）因果量化了政策歧义对 LLM agent 安全的影响（+34.0pp，OR=15.1），并提出六类型两层 taxonomy、发现\"disambiguation deficit\"现象（<11% awareness）。实验设计严谨、统计方法全面（TOST、bootstrap cluster、Holm-Bonferroni），但 taxonomy 的理论基础存在概念混淆（将 incompleteness 和 normative conflict 归为 ambiguity），且声称的 two-tier hierarchy 的 bootstrap 稳定性不足（34.3%），部分贡献的框架性新颖度被过度表述。\n\n## Weaknesses（逐条）\n\n**W1 [MUST-FIX] Two-tier hierarchy (C2) 稳定性不足，声称强于证据。**\n- Bootstrap cluster analysis 中 incompleteness singleton 仅在 34.3% 的 bootstrap samples 中出现，AU p-value=0.47。\n- Kendall's W=0.398（p=0.072）五模型下不显著。\n- Abstract/Intro/Conclusion 的表述确定性远超 34.3% bootstrap support。\n- 建议：(a) 更谨慎的措辞如\"incompleteness tends to cluster as the highest-risk type, though the tier boundary is not sharp\"；(b) 将 C2 缩小为\"incompleteness is consistently the highest-risk type\"。\n\n**W2 [SHOULD-FIX] Taxonomy 的理论基础存在概念混淆——Incompleteness 和 Conditional Precedence 并非严格意义上的 ambiguity。**\n- Incompleteness 是 information absence，不是\"multiple interpretations\"。\n- Conditional precedence 是 normative conflict，两条矛盾的规则各自是清晰的。\n- §3 用行为结果定义输入类型是循环论证。\n- 建议：(a) 定位为\"policy specification defects\"而非\"ambiguity types\"；(b) 更充分讨论理论边界。\n\n**W3 [SHOULD-FIX] \"Differential Nocuity\" 框架的增量贡献被过度表述。**\n- Berry & Kamsties (2004)、Chantree et al. (2006)、Willis et al. (2008) 已经测量了 type-specific nocuity。\n- 论文的贡献是在 LLM agent 场景的实证验证，但 §7 写法暗示新框架。\n- 建议：明确定位为已有概念在新领域的验证和扩展。\n\n**W4 [SHOULD-FIX] \"Disambiguation Deficit\" 命名不准确——是 uninstructed default 还是 inability？**\n- \"Deficit\"暗示能力缺失，但 mitigation experiment (-8.5pp) 证明可改善。\n- 建议：使用更精确术语或在定义中明确指 uninstructed settings。\n\n**W5 [SHOULD-FIX] Authorization scope 的结论可靠性受 low agreement 严重影响。**\n- κ=0.385 接近随机。52pp range 中真实差异 vs noise 无法分离。\n- 建议：在 §5.4 中更明确标记为 tentative/unreliable；考虑 Abstract 中移除或弱化 52pp 表述。\n\n**W6 [MINOR] Psycholinguistics 类比可能 over-extended。**\n- LLM autoregressive generation 与人类 incremental parsing 机制不同。\n- 建议：加 caveat \"though the underlying mechanisms are likely distinct\"。\n\n**W7 [MINOR] 引用问题。**\n- ferrari_defects_2018 作者不一致，2 orphan bib entries，navigli_wsd_2009 年份待确认。\n\n## Questions\n\nQ1. Incompleteness 满足 Wasow (2005) ambiguity 定义的理由？\nQ2. Bootstrap 34.3% 支持度 vs \"continuum\" 假说的区分？\nQ3. Coreferential 排除 mitigation 的影响？\nQ4. 是否有 template pattern 驱动的系统性偏差？\nQ5. Domain-specific SESOI 考虑？\n\n## Missing References\n\n1. Dalpiaz, van der Schalk, & Lucassen (2018) — 明确区分 ambiguity 和 incompleteness\n2. Yu, Carroll, & Bentley (2026) — concurrent matched-pair causal design for agent safety\n3. Lin et al. (2025) \"Ask-to-Clarify\" — disambiguation channel design\n4. Willis et al. (2008) 在 §7 中 credit type-specific nocuity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "policy_ambiguity_safety",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Weaknesses：对每条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。也请评论其 Questions 和 Missing References 中你认为重要的点。\n\n---\n\n# Reviewer 2 审稿意见：新颖性、理论基础与完整性\n\n## Summary（2-3 句）\n\n本文在 τ²-bench 上构建 300 组 matched clause pairs，通过 5 个模型（2,997 episodes）因果量化了政策歧义对 LLM agent 安全的影响（+34.0pp，OR=15.1），并提出六类型两层 taxonomy、发现\"disambiguation deficit\"现象（<11% awareness）。实验设计严谨、统计方法全面（TOST、bootstrap cluster、Holm-Bonferroni），但 taxonomy 的理论基础存在概念混淆（将 incompleteness 和 normative conflict 归为 ambiguity），且声称的 two-tier hierarchy 的 bootstrap 稳定性不足（34.3%），部分贡献的框架性新颖度被过度表述。\n\n## Weaknesses（逐条）\n\n**W1 [MUST-FIX] Two-tier hierarchy (C2) 稳定性不足，声称强于证据。**\n- Bootstrap cluster analysis 中 incompleteness singleton 仅在 34.3% 的 bootstrap samples 中出现，AU p-value=0.47。\n- Kendall's W=0.398（p=0.072）五模型下不显著。\n- Abstract/Intro/Conclusion 的表述确定性远超 34.3% bootstrap support。\n- 建议：(a) 更谨慎的措辞如\"incompleteness tends to cluster as the highest-risk type, though the tier boundary is not sharp\"；(b) 将 C2 缩小为\"incompleteness is consistently the highest-risk type\"。\n\n**W2 [SHOULD-FIX] Taxonomy 的理论基础存在概念混淆——Incompleteness 和 Conditional Precedence 并非严格意义上的 ambiguity。**\n- Incompleteness 是 information absence，不是\"multiple interpretations\"。\n- Conditional precedence 是 normative conflict，两条矛盾的规则各自是清晰的。\n- §3 用行为结果定义输入类型是循环论证。\n- 建议：(a) 定位为\"policy specification defects\"而非\"ambiguity types\"；(b) 更充分讨论理论边界。\n\n**W3 [SHOULD-FIX] \"Differential Nocuity\" 框架的增量贡献被过度表述。**\n- Berry & Kamsties (2004)、Chantree et al. (2006)、Willis et al. (2008) 已经测量了 type-specific nocuity。\n- 论文的贡献是在 LLM agent 场景的实证验证，但 §7 写法暗示新框架。\n- 建议：明确定位为已有概念在新领域的验证和扩展。\n\n**W4 [SHOULD-FIX] \"Disambiguation Deficit\" 命名不准确——是 uninstructed default 还是 inability？**\n- \"Deficit\"暗示能力缺失，但 mitigation experiment (-8.5pp) 证明可改善。\n- 建议：使用更精确术语或在定义中明确指 uninstructed settings。\n\n**W5 [SHOULD-FIX] Authorization scope 的结论可靠性受 low agreement 严重影响。**\n- κ=0.385 接近随机。52pp range 中真实差异 vs noise 无法分离。\n- 建议：在 §5.4 中更明确标记为 tentative/unreliable；考虑 Abstract 中移除或弱化 52pp 表述。\n\n**W6 [MINOR] Psycholinguistics 类比可能 over-extended。**\n- LLM autoregressive generation 与人类 incremental parsing 机制不同。\n- 建议：加 caveat \"though the underlying mechanisms are likely distinct\"。\n\n**W7 [MINOR] 引用问题。**\n- ferrari_defects_2018 作者不一致，2 orphan bib entries，navigli_wsd_2009 年份待确认。\n\n## Questions\n\nQ1. Incompleteness 满足 Wasow (2005) ambiguity 定义的理由？\nQ2. Bootstrap 34.3% 支持度 vs \"continuum\" 假说的区分？\nQ3. Coreferential 排除 mitigation 的影响？\nQ4. 是否有 template pattern 驱动的系统性偏差？\nQ5. Domain-specific SESOI 考虑？\n\n## Missing References\n\n1. Dalpiaz, van der Schalk, & Lucassen (2018) — 明确区分 ambiguity 和 incompleteness\n2. Yu, Carroll, & Bentley (2026) — concurrent matched-pair causal design for agent safety\n3. Lin et al. (2025) \"Ask-to-Clarify\" — disambiguation channel design\n4. Willis et al. (2008) 在 §7 中 credit type-specific nocuity"
  }
}
```

</details>

---


### Tool result

_source line 885 · 2026-05-21T19:08:01.560348+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1309
}
```

</details>

---


### Assistant

_source line 886 · 2026-05-21T19:08:04.057763+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 79

## Round 79

2 recorded events


### User

_source line 887 · 2026-05-21T19:08:06.568433+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**评分摘要**：Overall 3.5/5（Borderline Conference），Soundness 3.5，Excitement 3.5，Reproducibility 4，Confidence 4。

**核心判断**：实验设计整体严谨（matched-pair + perturbation control + 7 模型复制），统计分析覆盖面在同类工作中属上乘。C1（歧义整体致害 +34 pp）和 C2（incompleteness 一致性上界）的证据稳健。

**主要问题**：
- **[MUST-FIX]** Authorization scope 的 κ=0.385 不足以支撑其作为 C4 核心发现的地位，abstract/introduction 表述过强
- **[SHOULD-FIX]** Incompleteness confound 仅用 token count 粗粒度控制；条件间句长差异 d=0.74 未纳入 regression；per-type 人工验证（n=32-34/type）统计力度不足；cross-judge 混淆 judge×model identity；两层层级在 ±10 pp 处不稳定

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 888 · 2026-05-21T19:08:11.222775+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 80

## Round 80

2 recorded events


### User

_source line 889 · 2026-05-21T19:09:08.423789+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

## Weaknesses 逐条回应

**[AGREE] R1-W1: Authorization scope 表述强度超出测量可靠性。**
完全同意。我在自己的 W5 中提出了本质相同的问题。κ=0.385 在 Landis & Koch 分类中甚至低于"fair agreement"门槛（0.40），这意味着 judge 之间在该类型上的一致性接近随机水平。R1 提出的三点建议都合理，尤其是建议 (3)——展示去除 auth scope 后 C4 交互效应是否仍显著——这是一个可以快速完成且能大幅增强论文 robustness 的分析。补充：Abstract 中"though measured with the lowest inter-judge agreement, κ = 0.385"这个括号注释确实太容易被忽略（§Abstract, line 1）。52pp 这个数字在 Introduction（§1, line 19）中完全没有可靠性 caveat。

**[AGREE] R1-W2: Incompleteness confound 控制力度不足。**
同意核心判断，但补充一个 R1 未提及的角度。我在自己的 W2 中从**理论层面**质疑了 incompleteness 是否应该被归类为 ambiguity——它是 information absence 而非 multiple interpretations（§3 的 Wasow 2005 定义）。R1 从**方法层面**指出 token count 是 coarse proxy，两个批评是互补的。论文的 coreferential lower bound（31.6%, §5.2）确实只约束了 ambiguity 整体的下界，无法分离 incompleteness 的 information-addition component。R1 建议设计 information×ambiguity 正交 ablation 是理想方案，但在 revision 周期内可能不现实。更可行的是 R1 的建议 (2)：在所有涉及 incompleteness 的 hierarchy 声明中明确标注"conditional on confound assumptions"。

**[REBUT] R1-W3: 句子长度差异（d=0.74）作为未控制混淆变量。**
部分不同意。R1 的担忧有道理，但论文已有部分控制：
1. **Matched-pair design 本身控制了 between-clause variance**——每个 clause pair 的长度差异是该 pair 自身的特征，被 pair-level 控制所吸收。Δpp 比较的是同一 clause 的 ambiguous vs unambiguous variant，不是跨 clause 的长度比较。
2. **Appendix H 的 logistic regression 已包含 token delta 作为协变量**（Table 9, §Appendix H）。Token delta 显著（p<0.001）但 OR=1.022/token，magnitude 很小，且加入后 type effects 的 coefficient change <8%。
3. **d=0.74 的句长差异**（§Limitations, "Synthetic ambiguity" paragraph）反映的是 ambiguous variants 总体上比 unambiguous variants 稍长——这是 matched-pair 内的系统性差异，不是跨 pair 的 confound。

不过，R1 的建议 (1) 报告 per-type 句长分布仍然有价值——如果某些 type 的句长差异特别大（比如 incompleteness 因为需要"添加内容"），这可能加剧 W2 的 confound 问题。建议作者在 revision 中报告 per-type 的 token delta distribution。

**[AGREE] R1-W4: Per-type 人工验证样本量不足。**
同意。32-34 per type 确实太少。Scopal 的 κ CI [0.00, 1.00]（Table 8, Appendix G）在统计上等于"no information"——任何 κ 值从 0 到 1 都在置信区间内。这使得我们无法判断 scopal 类型的 judge reliability 是好是坏。R1 建议扩大到每类 ≥80 episodes 合理，但在 revision 周期内完成可能需要大量标注资源。作为最低要求，建议至少在正文中明确指出 per-type κ 因样本量不足而不具有类型间比较价值。

**[AGREE with nuance] R1-W5: Cross-judge 设计中 judge identity 与 model identity 混淆。**
基本同意，但有一个重要 nuance。论文在 §4.4 (Evaluation) 中明确论证了 **matched-pair design 消除了 Δpp 中的 judge bias**——因为同一 judge 评估同一 model 的 ambiguous 和 unambiguous 条件，systematic bias 在差值中被抵消。因此 **C1（binary ambiguity effect）和 C2 的 within-type Δpp 不受 judge identity confound 影响**。

R1 的担忧对 **C2 的 pooled absolute violation rates**（Table 1 的 Pooled 列）和 **C4 的跨模型比较** 是成立的。Within-judge-group 分析中 C3 各自未达显著（§Limitations, "Cross-judge asymmetry"：GPT-4.1-judged p=0.059; GPT-5.4-judged p=0.157）恰恰支持了这个担忧。

R1 建议 (1) 补充双 judge 评估更多组合是理想的但成本高。建议 (2) 报告 C2 的 within-judge-group 分析是可行且应做的——如果 C2 的 type ranking 在两个 judge subgroup 中一致，则 confound 的影响可忽略。

**[AGREE] R1-W6: 两层层级稳定性依赖于 margin 选择。**
完全同意。这与我自己的 W1（MUST-FIX）一致。Bootstrap AU p-value=0.47（Appendix I）和 ±10pp 下仅 3/6 mid-tier pairs 等价（§5.2）共同表明 two-tier structure 不够 robust。R1 建议并列呈现 ±10pp 的"three-tier"替代叙事是一个好建议——这比简单弱化措辞更有建设性，给读者提供了多个 granularity level 的解读。

**[AGREE] R1-W7: Clause pair 构建的 IAA 报告不完整。**
同意。§4.2 报告了"96% pass rate"但未报告 type assignment 的 κ。96% agreement 可能被 prevalence 膨胀（如果大多数 pairs 的 type 是显而易见的）。建议补充 κ。

**[AGREE] R1-W8: 引用问题。**
同意，与我自己的 W7 一致。

**[AGREE] R1-W9: Reproducibility ICC 仅覆盖 OpenAI 模型族。**
同意。论文在 §Limitations 中已承认（"Cross-provider test-retest reliability remains unmeasured; ICC=0.919 covers only OpenAI models"），但未提供其他 provider 的任何 stability evidence。至少可以报告 Qwen3 或 DeepSeek 的 small-scale replication。

---

## Questions 评论

**R1-Q1 (Per-type sentence length)**: 重要问题，与 W3 相关。如果 incompleteness 的句长差异远大于其他 type，则 W2 的 confound 问题更严重。

**R1-Q2 (Variance decomposition 中 ~76% 残余方差)**: 好问题。论文报告 type 解释 22.4%、model 解释 1.0%、interaction 解释 2.9%——剩余约 73.7% 很可能来自 clause-level idiosyncrasy（Appendix J 的 LOO 分析暗示了这一点）和 episode-level noise（多轮对话中 user simulator 的随机性）。作者应明确报告 clause-level random effect 的 variance component。

**R1-Q3 (Perturbation control 的模型分布)**: 次要问题。如果 perturbation control 只在部分模型上运行，其覆盖面不足可能影响 null result 的解释。

**R1-Q5 (Clause pairs 的 domain 分布)**: 有价值。τ²-bench 覆盖 retail 和 airline 两个 domain。如果 clause pairs 在两个 domain 间分布不均，domain-specific policy 结构可能混淆 type effects。

**R1-Q6 (Coreferential 排除理由)**: 与我自己的 Q3 相关。Coreferential 在 replication（Appendix E）和 mitigation（Appendix B）中都被排除，削弱了对这个"纯粹 ambiguity"类型的分析深度。排除理由（"disambiguation relies on benchmark-specific assertion structure"）需要更充分的解释。

**R1-Q7 (Coreferential nocuity 声称在低 κ CI 下是否过强)**: 有效质疑。Coreferential 的 human-LLM κ=0.479，CI [0.00, 0.84]（Table 8）。但需注意 coreferential 的 violation base rate 只有 8.8%（unambiguous condition），prevalence paradox 压缩了 κ 的 denominator（§Appendix G 已解释）。Raw agreement 85.3% 实际上是可接受的。因此我认为这个问题的严重程度低于 R1 暗示的。

---

## Missing References 评论

**R1-Ref1: Tamkin et al. (2023)** — 同意应该引用。该文研究 LLM 决策中的系统性偏差，与 authorization scope 的 permissiveness bias（§6.1, "69.2% of such violations involve unauthorized escalation with zero conservative refusals"）相关。注意该文已在 bib 中但是 orphan entry（`tamkin_evaluating_2023` 未被 cite）——作者可能最初打算引用但最终遗漏。

**R1-Ref2: Mu et al. (2023) "Can LLMs Follow Simple Rules?"** — 同意，与 policy compliance baseline 的讨论相关。

**R1-Ref3: Deemter (2010), Lassiter & Goodman (2017)** — 同意这些 vagueness 文献的引用是有价值的。论文在 §3 引用了 Kennedy (2007) 讨论 vagueness，但 Deemter 和 Lassiter & Goodman 的 computational/Bayesian approaches to vagueness 与 authorization scope 的 vagueness-like 特征更相关。

---

## 综合评估

R1 和 R2 的审稿意见在核心问题上高度一致：

1. **Authorization scope reliability**（R1-W1 = R2-W5）：两位 reviewer 都认为 52pp 声称缺乏可靠性支撑
2. **Two-tier hierarchy stability**（R1-W6 = R2-W1）：两位 reviewer 都认为 bootstrap 34.3% 和 margin 依赖性削弱了 hierarchy 声称
3. **Incompleteness confound**（R1-W2 ≈ R2-W2 的方法层面）：both reviewers 认为控制不够充分

R1 额外提出了 **句长 confound**（W3）和 **per-type 样本量**（W4）两个我未涉及的有效 methodological concerns。我额外提出了 **taxonomy 理论基础**（W2 的理论层面）和 **Disambiguation Deficit 命名准确性**（W4）两个 R1 未涉及的 conceptual concerns。

两份审稿互补，共同指向：**C1 是坚实的，但 C2 和 C4 的 claims 需要 downscale，taxonomy 和 framing 需要修正。** 如果作者能在 revision 中 (a) 弱化 hierarchy/auth scope claims，(b) 深化 taxonomy 的理论讨论，(c) 补充 R1-W3/W4 的分析，这篇论文有 Conference acceptance 的潜力。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 890 · 2026-05-21T19:09:15.543897+00:00_

Reviewer 2 的交叉回应已收到，等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 81

## Round 81

2 recorded events


### User

_source line 891 · 2026-05-21T19:09:18.066872+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。核心判断：与 R1 在三个关键问题（auth scope reliability、hierarchy stability、incompleteness confound）上高度一致。对 R1-W3（句长 confound）部分反驳——logistic regression 已含 token delta 且 matched-pair 设计本身控制了 within-pair variance，但建议补充 per-type 句长分布。两份审稿互补，共同指向 C1 坚实、C2/C4 需要 downscale claims。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 892 · 2026-05-21T19:09:22.482650+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 82

## Round 82

10 recorded events


### User

_source line 893 · 2026-05-21T19:10:03.431051+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 意见的逐条回应

## Weaknesses 回应

**[AGREE] R2-W1: Two-tier hierarchy (C2) 稳定性不足，声称强于证据。**

同意 R2 的判断。Bootstrap 34.3% 和 AU p=0.47 意味着 incompleteness singleton 不是一个稳定的聚类结构。Kendall's W=0.398（p=0.072）五模型下未达显著进一步削弱了 C2 的 cross-model generalizability。我在自己的 W6 中也独立提出了相同的 margin dependence 问题：在 ±10 pp 时仅 3/6 mid-tier pairs 等价。

R2 的建议（将 C2 缩小为"incompleteness is consistently the highest-risk type"）是务实的。这一缩窄后的声称有充分支撑：incompleteness 在全部 7 个模型中 ≥46%（Section 5.2, Appendix E Table 7），且 mean rank 始终最高（Appendix M）。但当前的"two-tier hierarchy"表述暗示一个清晰的二分结构，与 34.3% bootstrap support 不符。

**[REBUT] R2-W2: Taxonomy 概念混淆——Incompleteness 和 Conditional Precedence 非严格 ambiguity。**

R2 的理论关切有道理，但论文已在 Section 3 "Scope of 'ambiguity'" 段落中明确回应了这一问题。原文承认 incompleteness 与 "information absence"、conditional precedence 与 "normative conflict" 的重叠，并给出了采用 inclusive definition 的理由："LLM agents process all six types identically—committing to a single interpretation without flagging uncertainty—and the resulting safety violations are behaviorally indistinguishable (§5)"。

这不是循环论证，而是操作性定义（operational definition）：论文并非用行为结果来定义类型，而是用"admits multiple operationally distinct interpretations by an LLM agent"来界定范围，然后实证检验行为后果。这种操作性定义在实证研究中是标准做法。

但我同意 R2 的一个子观点：论文标题和 framing 中一贯使用 "ambiguity" 而非 "policy specification defects" 或 "policy specification issues" 确实可能导致语言学背景的读者产生误解。建议在 Section 3 中扩展理论边界的讨论，增加对 Dalpiaz et al. (2018) 区分 ambiguity/incompleteness 的引用，并在标题或 abstract 中添加更精确的限定。

**[AGREE] R2-W3: "Differential Nocuity" 框架增量贡献被过度表述。**

同意。Section 7 Discussion 中的 "differential nocuity" 段落确实写得像是提出了一个新框架，但核心贡献实际是将 Berry & Kamsties (2004) 的 nocuous/innocuous 区分在 LLM agent 场景中进行了类型粒度的实证检验。Willis et al. (2008) 已经在 RE 领域测量了 type-specific nocuity。论文的新增价值是：(1) agent 场景下所有歧义都是 nocuous（Berry & Kamsties 的 innocuous 类别消失），(2) type×model interaction 提供了 safety training 选择性缓解的证据。这些是有价值的实证贡献，但不构成 "new framework"。

建议：将 §7 第一段的 framing 从 "can be interpreted through a differential nocuity lens" 改为 "extends Berry & Kamsties' nocuous/innocuous distinction to LLM agents, where all ambiguity is nocuous but type-specific severity varies"。

**[AGREE with nuance] R2-W4: "Disambiguation Deficit" 命名不准确。**

部分同意。R2 正确指出 "deficit" 暗示能力缺失，而 mitigation experiment（-8.5 pp）证明可改善。但论文在 Section 6.2 中已明确澄清："Agents are not inherently incapable of disambiguation...but exhibit a disambiguation deficit: defaulting to single-parse adoption without explicit instruction"（第 25 行）。所以 "deficit" 在此指 uninstructed default behavior，而非 inability。

不过，术语选择确实容易引起误读。一个更精确的术语可能是 "disambiguation default" 或 "disambiguation neglect"，更好地传达 "有能力但默认不做" 的含义。

**[AGREE] R2-W5: Authorization scope 的结论可靠性受 low agreement 严重影响。**

强烈同意。这与我的 W1 (MUST-FIX) 完全一致。κ=0.385 的 cross-judge agreement 意味着 authorization scope 的绝对违规率有极大的测量不确定性。52 pp range 这一数字是论文最引人注目的发现之一，但也是最不可靠的。

我比 R2 更进一步：建议作者在 C4 分析中展示去除 authorization scope 后交互效应是否仍然显著，以测试这一类型是否在驱动整个 C4 结果。如果去除后交互效应消失，则 C4 的一般性声称需要大幅缩窄。

**[AGREE] R2-W6: Psycholinguistics 类比可能 over-extended。**

同意加 caveat 的建议。论文将 agent 的 surface adoption 类比为 Frazier & Rayner (1982) 的 garden-path processing 和 Ferreira et al. (2002) 的 good-enough representations。类比在 phenomenological level 是有启发性的（都是 early commitment to a single parse），但 autoregressive generation 和 incremental human parsing 的底层机制确实不同。Section 6.1 使用 "paralleling" 一词已经有一定距离感，但 §6.2 中 "paralleling human good-enough processing" 的措辞不够谨慎。加一句 mechanism-level caveat 即可，不影响论文的核心论证。

**[AGREE] R2-W7: 引用问题。**

与我的 W8 一致。ferrari_defects_2018 的第一作者确实应为 Rosadini；2 个 orphan entries 应清理。

## Questions 回应

**R2-Q1（Incompleteness 满足 Wasow 2005 定义的理由）：** 这是 W2 的核心，论文已在 Section 3 用操作性定义回应。如上所述，我认为论文的立场可辩护但需扩展讨论。

**R2-Q2（Bootstrap 34.3% vs continuum）：** 重要问题。34.3% 不足以排除 continuum 假说。论文应明确讨论：如果歧义类型的违规率分布是连续的（而非离散的两层），哪些结论需要修改？核心的 incompleteness 上界地位可能不变，但 "two-tier hierarchy" 这一结构性声称需要弱化。

**R2-Q3（Coreferential 排除 mitigation 的影响）：** 我在自己的 Q6 中也提出了类似问题。Coreferential 31.6% 的违规率不低，排除它使 mitigation 的完整性受损。

**R2-Q4（Template pattern bias）：** 我在 W7 中也提出了类似关切。96% pass rate 不等于 high inter-annotator κ。建议补充 type assignment 的标准 reliability 指标。

**R2-Q5（Domain-specific SESOI）：** 好问题。±15 pp 的 anchoring argument（"a type producing ≥15 pp more violations warrants distinct policy handling"，Section 4.6）是合理的实践性论证，但不同部署场景（医疗 vs 零售）的 tolerance 可能差异巨大。论文在 Limitations 中提到了 domain scope 限制，但未将此与 SESOI 选择联系起来。

## Missing References 回应

1. **Dalpiaz et al. (2018)**：重要。如果这项工作明确区分了 ambiguity 和 incompleteness，它直接关系到 W2 的理论讨论。论文应引用并回应。

2. **Yu, Carroll, & Bentley (2026)**：如果确实存在 concurrent matched-pair causal design for agent safety，这是高度相关的 concurrent work，必须在 Related Work 中讨论。我无法独立验证这篇论文是否存在，但如果 R2 能确认，作者应搜索并引用。

3. **Lin et al. (2025) "Ask-to-Clarify"**：与 Suri et al. (2025) 和 Sehwag et al. (2026)（论文已引用）属于同一 disambiguation channel 文献线。补充引用是合理的。

4. **Willis et al. (2008) 在 §7 中给予 credit**：同意 R2。Willis et al. 已在 Related Work 中被引用，但 §7 Discussion 中的 "differential nocuity" 讨论未提及他们在 type-specific nocuity 测量上的 prior work。这是一个归属问题，应修正。

## 总结

R2 的审查侧重理论基础和概念框架，与我侧重方法严谨性形成互补。我们在三个关键问题上高度一致：(1) authorization scope 的低可靠性（R2-W5 = 我的 W1）；(2) two-tier hierarchy 的稳定性不足（R2-W1 = 我的 W6）；(3) 引用问题（R2-W7 = 我的 W8）。

R2 的 W2（taxonomy 概念混淆）是一个有价值的理论视角，但论文已有部分回应（Section 3 "Scope of 'ambiguity'"）。我认为修订方向是扩展讨论而非改变 taxonomy 设计。R2 的 W3 和 W4 属于 framing/naming 问题，修订成本低且能提升精确度。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 894 · 2026-05-21T19:10:26.978184+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 895 · 2026-05-21T19:10:27.079095+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T18:58:37.760730+00:00\", \"completed_at\": \"2026-05-21T19:01:34.790853+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 3-5\", \"message\": \"连续 3 页纯文本（Ambiguity Taxonomy + Method + Statistical Analysis），无任何 display item 穿插。Taxonomy 部分（§3, page 3）尤其适合用一张汇总表或层级结构图打破纯文本节奏，帮助审稿人快速锚定 6 种 ambiguity 类型的层级关系\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"主文 8 页仅 4 个 display items（3 figures + 1 table），对于实证为主的论文偏少（通常 5–8 个）。建议考虑：(1) §3 Taxonomy 加一张类型汇总表，(2) §5 Results 中将部分行内统计数据提炼为 summary table\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 流程图中部分文字标签（如底层框内的 \\\"Fine-grained violation analysis\\\" 等）字号偏小，打印后可能难以辨认。建议适当增大关键标签字号或简化图内文字\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2（Per-type effect sizes 条形图）压缩在单栏内，axis labels 和 bar labels 可读但偏小。如果 effect size 是核心结果之一，可考虑改为 figure*（全宽）以增加可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 全宽 grouped bar chart 颜色区分度良好，6 种 ambiguity type 各有不同颜色+unambiguous 用斜线填充。建议确认色盲友好性（特别是如果有红绿相邻的 bar），并在图注中补充\\\"higher = more violations\\\"等阅读指引\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点。虽非硬性要求，但在 page 1 底部或 page 2 顶部放置一个能传达核心发现的 teaser figure（如不同 ambiguity type 的 violation rate 对比）可显著增强审稿人第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 使用 booktabs 风格，数字精度一致（一位小数），最优结果有标注。排版规范\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Appendix 中 Tables 3–6 密集排列在同一页，表格间距紧凑但可读，无溢出\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Limitations 段落简短（约半栏），覆盖 3 个要点（domain scope, synthetic ambiguity, cross-judge asymmetry），符合 EMNLP 要求\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 7}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 896 · 2026-05-21T19:10:27.129867+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 897 · 2026-05-21T19:10:27.130392+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 898 · 2026-05-21T19:12:59.376017+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "issues_yaml": "## Round 10 (Fresh) Review Issues — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Date: 2026-05-21\n## Round 10 Score: 3.5 (Borderline Conference)\n## Note: Fresh review session — all issues re-evaluated from scratch\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R10-C1\"\n  summary: \"Authorization scope κ=0.385 不足以支撑 C4 中 52pp range 作为核心发现\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R9-N4. Abstract/Introduction 表述与正文 suggestive hedging 不匹配。\"\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R1 MUST-FIX, R2 SHOULD-FIX. 两人完全共识: κ=0.385 低于 fair agreement 门槛(0.40), 52pp 中真实差异 vs noise 无法分离。Abstract 括号注释太弱, Introduction 复述 52pp 无 caveat。R1 建议展示去除 auth scope 后 C4 是否仍显著。\"\n  action_items:\n    - round: 9\n      action: \"Abstract 52pp 加 measurement uncertainty; §1 对齐 suggestive; §5.4 F-test 补 denominator df\"\n      assigned_to: agent\n      status: in_progress\n    - round: 10\n      action: \"(1) Abstract 将 auth scope 从主要发现降格为初步发现; (2) Introduction 同等篇幅讨论可靠性限制; (3) C4 分析展示去除 auth scope 后交互效应是否仍显著; (4) 52pp 标记为 upper bound with substantial measurement uncertainty\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C2\"\n  summary: \"Two-tier hierarchy (C2) bootstrap 仅 34.3% 支持, 声称强于证据\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R9-N3. SESOI ±15pp 缺乏外部锚定, two-tier 在 ±10-12pp 时不稳健。\"\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R2 MUST-FIX, R1 AGREE(W6). Bootstrap AU p=0.47, ±10pp 仅 3/6 mid-tier pairs 等价, Kendall's W=0.398(p=0.072) 不显著。Abstract/Intro/Conclusion 表述确定性远超证据。共识: 缩小 C2 为 'incompleteness is consistently the highest-risk type' 而非 'two-tier hierarchy'。\"\n  action_items:\n    - round: 9\n      action: \"§4.6 承认 pragmatic threshold; §5.2 加 ±10pp 替代 narrative\"\n      assigned_to: agent\n      status: in_progress\n    - round: 10\n      action: \"(1) Abstract/Intro/Conclusion 措辞弱化为 'incompleteness tends to cluster as highest-risk, though tier boundary is not sharp'; (2) 正文并列呈现 ±10pp three-tier 与 ±15pp two-tier 叙事; (3) 报告 AU p-value 并解释意义; (4) 考虑将 C2 核心声明缩窄\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R10-W1\"\n  summary: \"Taxonomy 理论基础: incompleteness(information absence) 和 conditional precedence(normative conflict) 不满足 strict ambiguity 定义\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R2]\n      note: \"R9-N1. §3 需正面讨论理论张力。\"\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"R2 SHOULD-FIX, R1 REBUT(部分). R2 认为是根本性概念混淆, §3 用行为结果定义类型是循环论证。R1 认为操作性定义可辩护但需扩展讨论, 增加 Dalpiaz et al. (2018) 引用。共识: 需要在 §3 中更充分讨论理论边界, 但不必改变 taxonomy 设计。\"\n  action_items:\n    - round: 10\n      action: \"(1) §3 扩展 'Scope of ambiguity' 段落, 更深入讨论 ambiguity vs incompleteness vs normative conflict 的理论边界; (2) 引用 Dalpiaz et al. (2018); (3) 考虑在标题/abstract 中添加更精确限定\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W2\"\n  summary: \"Incompleteness confound 仅 token count 粗粒度控制, 无法分离 information-addition component\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R9-W4. Token count proxy limitation.\"\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R1 SHOULD-FIX, R2 AGREE. Token count 是 coarse proxy, coreferential 下界约束整体而非 incompleteness 特定贡献。理想方案: information×ambiguity 正交 ablation; 最低要求: hierarchy 声明标注 'conditional on confound assumptions'。\"\n  action_items:\n    - round: 10\n      action: \"(1) 在涉及 incompleteness 的 hierarchy 声明中标注 conditional on confound assumptions; (2) 报告 per-type token delta distribution; (3) 如可行, 设计信息量和歧义正交变化的 ablation\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W3\"\n  summary: \"Differential Nocuity 框架增量贡献被过度表述, 实为已有概念的 domain transfer\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R2, R1]\n      note: \"R9-N2. DN 从 contribution list 移除→Discussion interpretive lens。\"\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"R2 SHOULD-FIX, R1 AGREE. Berry & Kamsties (2004), Chantree (2006), Willis (2008) 已测量 type-specific nocuity。§7 写法暗示新框架。共识: 定位为已有概念在 LLM agent 领域的验证和扩展。\"\n  action_items:\n    - round: 10\n      action: \"§7 第一段改为 'extends Berry & Kamsties distinction to LLM agents, where all ambiguity is nocuous but type-specific severity varies'; 明确 credit Willis et al. (2008) 的 prior type-specific nocuity measurement\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W4\"\n  summary: \"Disambiguation Deficit 命名暗示 inability, 实为 uninstructed default behavior\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R9-W1. 从 Ambiguity Blindness 改为 Disambiguation Deficit。\"\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"R2 SHOULD-FIX, R1 AGREE with nuance. Mitigation -8.5pp 证明可改善, 非 inability。R1 认为 §6.2 已有澄清但术语易误读。建议: 'Disambiguation Neglect' 或在定义中明确指 uninstructed default。\"\n  action_items:\n    - round: 10\n      action: \"§6.2 定义中明确 'absence of disambiguation behavior in default (uninstructed) settings, not inability'; 考虑更精确术语如 'Disambiguation Neglect'\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W5\"\n  summary: \"Per-type 人工验证样本量偏小(n=32-34/type), scopal CI [0.00, 1.00] 无信息\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R9-W5. §4.4 正文仍过于乐观。\"\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R1 SHOULD-FIX, R2 AGREE. 100/6=32-34 per type, scopal CI [0.00, 1.00] 完全无信息。理想: 扩大至每类≥80; 最低: 正文明确标注 per-type κ 不具类型间比较价值。\"\n  action_items:\n    - round: 10\n      action: \"(1) 正文 §4.4 明确标注 per-type κ 因样本量不足不具类型间比较价值; (2) 如有资源, 扩大人工标注至每类≥80\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W6\"\n  summary: \"Cross-judge 设计使 judge identity 与 model identity 混淆, 影响 C2 pooled rates 和 C4\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R9-W6. LLaMA Δ=+20pp 暗示跨 provider effect 受 instruction-following quality 调节。\"\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R1 SHOULD-FIX, R2 AGREE with nuance. Matched-pair 消除 Δpp 中的 bias(C1 safe), 但 C2 pooled absolute rates 和 C4 跨模型比较受影响。Within-judge-group C3 各自未达显著。建议报告 C2 within-judge-group 分析。\"\n  action_items:\n    - round: 10\n      action: \"(1) 报告 C2 type ranking 在两个 judge subgroup 内是否一致; (2) 如可行, 补充双 judge 评估更多组合\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W7\"\n  summary: \"条件间句子长度差异 d=0.74 需报告 per-type 分布\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R1 SHOULD-FIX, R2 partial REBUT. R2 指出 matched-pair 和 logistic regression 已有部分控制, 但同意需报告 per-type 句长分布, 特别是 incompleteness 是否系统性更长。\"\n  action_items:\n    - round: 10\n      action: \"报告 per-type 句长分布和 condition×type 交互; 如 incompleteness 系统性更长则在 confound 讨论中标注\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# MINOR ISSUES\n# ============================================================\n\n- id: \"R10-M1\"\n  summary: \"Clause pair 构建 96% pass rate 未报告 type assignment κ\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R1 MINOR(W7), R2 AGREE. 96% 不区分 agreement 和 chance agreement。\"\n  action_items:\n    - round: 10\n      action: \"补充 type assignment 的 Cohen's κ 或 Fleiss' κ\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M2\"\n  summary: \"引用问题: ferrari_defects_2018 作者不一致 + 2 orphan bib entries + navigli_wsd_2009 待确认\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R2]\n      note: \"R9-M1, R9-M2.\"\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"两人共识. ferrari_defects_2018 第一作者应为 Rosadini; tamkin_evaluating_2023 和 yin_safeagentbench_2025 为 orphan entries; navigli_wsd_2009 年份待核实。\"\n  action_items:\n    - round: 10\n      action: \"核实并修正 bib entries; 删除或引用 orphan entries; 确认 navigli 引用准确性\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M3\"\n  summary: \"Reproducibility ICC=0.919 仅覆盖 OpenAI 模型族, 跨 provider 稳定性未测量\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R9-W6 部分. Limitations 已承认。\"\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R1 MINOR(W9), R2 AGREE. temperature=0 下同 provider 高 ICC 不意外, 有意义的是跨 provider 稳定性。\"\n  action_items:\n    - round: 10\n      action: \"如可行, 至少在 1-2 个非 OpenAI 模型上补充 test-retest data\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M4\"\n  summary: \"Psycholinguistics 类比(garden-path, good-enough processing) 可能 over-extended\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"R2 MINOR(W6), R1 AGREE. Autoregressive generation 与 incremental parsing 机制不同。§6.2 'paralleling human good-enough processing' 需加 mechanism-level caveat。\"\n  action_items:\n    - round: 10\n      action: \"§6.2 加一句 'though the underlying mechanisms are likely distinct'\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M5\"\n  summary: \"Coreferential 被系统性排除在 mitigation 和 replication 之外, 削弱分析完整性\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R2, R1]\n      note: \"R9-W9.\"\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"两人均在 Questions 中提出(R1-Q6, R2-Q3). 排除理由需更充分解释。\"\n  action_items:\n    - round: 10\n      action: \"Appendix 补充 coreferential 排除的详细理由\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M6\"\n  summary: \"Pages 3-5 连续纯文本无 display item, Taxonomy 需可视化\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"R9-M8. 视觉审查发现。\"\n    - round: 10\n      reviewers: []\n      note: \"视觉审查再次标记: 连续 3 页纯文本, Taxonomy 适合汇总表或层级图。\"\n  action_items:\n    - round: 10\n      action: \"§3 Taxonomy 加一张类型汇总表打破纯文本节奏\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# PREVIOUSLY RESOLVED (confirmed in Round 10)\n# ============================================================\n\n- id: \"R8-W1-resolved\"\n  summary: \"缺少 API 超参数报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"§4.3 reports temperature=0, top_p=1, max_tokens=4096. 本轮未提及。\"\n  resolution: \"§4.3 添加完整 API 超参数\"\n  resolution_round: 9\n\n- id: \"R8-W4-resolved\"\n  summary: \"无代码/数据可用性声明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"Data and Code Availability section 已存在。本轮未提及。\"\n  resolution: \"添加 Data and Code Availability section\"\n  resolution_round: 9\n\n- id: \"R9-W7-resolved\"\n  summary: \"多重比较校正 three test families 未明确定义\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"Appendix L 已明确列出 3 families。本轮未提及。\"\n  resolution: \"Appendix L 新增 Multiple Comparison Correction 小节\"\n  resolution_round: 10\n\n- id: \"R9-W8-resolved\"\n  summary: \"与 DRIP-R 的 taxonomy type-level 映射缺失\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"Appendix L 有 DRIP-R mapping。R2 S5 肯定了 concurrent work 定位清晰。\"\n  resolution: \"Appendix L 新增 DRIP-R Category Mapping\"\n  resolution_round: 10\n\n- id: \"R9-M3-resolved\"\n  summary: \"Introduction 'seven models' 措辞应区分 main study (5) vs replication (2)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"§1 已改为 'five primary models and confirmed in two additional replication models'。本轮未提及。\"\n  resolution: \"措辞已修正\"\n  resolution_round: 10\n\n- id: \"R9-M7-resolved\"\n  summary: \"§5.4 F(20) 缺少 denominator df\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"§5.4 已改为 F(20, 2976)。本轮未提及。\"\n  resolution: \"F(20) → F(20, 2976)\"\n  resolution_round: 10\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "issues_yaml": "## Round 10 (Fresh) Review Issues — policy_ambiguity_safety\n## Paper: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n## Venue: EMNLP 2026 via ARR May cycle\n## Date: 2026-05-21\n## Round 10 Score: 3.5 (Borderline Conference)\n## Note: Fresh review session — all issues re-evaluated from scratch\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R10-C1\"\n  summary: \"Authorization scope κ=0.385 不足以支撑 C4 中 52pp range 作为核心发现\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R9-N4. Abstract/Introduction 表述与正文 suggestive hedging 不匹配。\"\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R1 MUST-FIX, R2 SHOULD-FIX. 两人完全共识: κ=0.385 低于 fair agreement 门槛(0.40), 52pp 中真实差异 vs noise 无法分离。Abstract 括号注释太弱, Introduction 复述 52pp 无 caveat。R1 建议展示去除 auth scope 后 C4 是否仍显著。\"\n  action_items:\n    - round: 9\n      action: \"Abstract 52pp 加 measurement uncertainty; §1 对齐 suggestive; §5.4 F-test 补 denominator df\"\n      assigned_to: agent\n      status: in_progress\n    - round: 10\n      action: \"(1) Abstract 将 auth scope 从主要发现降格为初步发现; (2) Introduction 同等篇幅讨论可靠性限制; (3) C4 分析展示去除 auth scope 后交互效应是否仍显著; (4) 52pp 标记为 upper bound with substantial measurement uncertainty\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C2\"\n  summary: \"Two-tier hierarchy (C2) bootstrap 仅 34.3% 支持, 声称强于证据\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R9-N3. SESOI ±15pp 缺乏外部锚定, two-tier 在 ±10-12pp 时不稳健。\"\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R2 MUST-FIX, R1 AGREE(W6). Bootstrap AU p=0.47, ±10pp 仅 3/6 mid-tier pairs 等价, Kendall's W=0.398(p=0.072) 不显著。Abstract/Intro/Conclusion 表述确定性远超证据。共识: 缩小 C2 为 'incompleteness is consistently the highest-risk type' 而非 'two-tier hierarchy'。\"\n  action_items:\n    - round: 9\n      action: \"§4.6 承认 pragmatic threshold; §5.2 加 ±10pp 替代 narrative\"\n      assigned_to: agent\n      status: in_progress\n    - round: 10\n      action: \"(1) Abstract/Intro/Conclusion 措辞弱化为 'incompleteness tends to cluster as highest-risk, though tier boundary is not sharp'; (2) 正文并列呈现 ±10pp three-tier 与 ±15pp two-tier 叙事; (3) 报告 AU p-value 并解释意义; (4) 考虑将 C2 核心声明缩窄\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R10-W1\"\n  summary: \"Taxonomy 理论基础: incompleteness(information absence) 和 conditional precedence(normative conflict) 不满足 strict ambiguity 定义\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R2]\n      note: \"R9-N1. §3 需正面讨论理论张力。\"\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"R2 SHOULD-FIX, R1 REBUT(部分). R2 认为是根本性概念混淆, §3 用行为结果定义类型是循环论证。R1 认为操作性定义可辩护但需扩展讨论, 增加 Dalpiaz et al. (2018) 引用。共识: 需要在 §3 中更充分讨论理论边界, 但不必改变 taxonomy 设计。\"\n  action_items:\n    - round: 10\n      action: \"(1) §3 扩展 'Scope of ambiguity' 段落, 更深入讨论 ambiguity vs incompleteness vs normative conflict 的理论边界; (2) 引用 Dalpiaz et al. (2018); (3) 考虑在标题/abstract 中添加更精确限定\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W2\"\n  summary: \"Incompleteness confound 仅 token count 粗粒度控制, 无法分离 information-addition component\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R9-W4. Token count proxy limitation.\"\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R1 SHOULD-FIX, R2 AGREE. Token count 是 coarse proxy, coreferential 下界约束整体而非 incompleteness 特定贡献。理想方案: information×ambiguity 正交 ablation; 最低要求: hierarchy 声明标注 'conditional on confound assumptions'。\"\n  action_items:\n    - round: 10\n      action: \"(1) 在涉及 incompleteness 的 hierarchy 声明中标注 conditional on confound assumptions; (2) 报告 per-type token delta distribution; (3) 如可行, 设计信息量和歧义正交变化的 ablation\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W3\"\n  summary: \"Differential Nocuity 框架增量贡献被过度表述, 实为已有概念的 domain transfer\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R2, R1]\n      note: \"R9-N2. DN 从 contribution list 移除→Discussion interpretive lens。\"\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"R2 SHOULD-FIX, R1 AGREE. Berry & Kamsties (2004), Chantree (2006), Willis (2008) 已测量 type-specific nocuity。§7 写法暗示新框架。共识: 定位为已有概念在 LLM agent 领域的验证和扩展。\"\n  action_items:\n    - round: 10\n      action: \"§7 第一段改为 'extends Berry & Kamsties distinction to LLM agents, where all ambiguity is nocuous but type-specific severity varies'; 明确 credit Willis et al. (2008) 的 prior type-specific nocuity measurement\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W4\"\n  summary: \"Disambiguation Deficit 命名暗示 inability, 实为 uninstructed default behavior\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R9-W1. 从 Ambiguity Blindness 改为 Disambiguation Deficit。\"\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"R2 SHOULD-FIX, R1 AGREE with nuance. Mitigation -8.5pp 证明可改善, 非 inability。R1 认为 §6.2 已有澄清但术语易误读。建议: 'Disambiguation Neglect' 或在定义中明确指 uninstructed default。\"\n  action_items:\n    - round: 10\n      action: \"§6.2 定义中明确 'absence of disambiguation behavior in default (uninstructed) settings, not inability'; 考虑更精确术语如 'Disambiguation Neglect'\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W5\"\n  summary: \"Per-type 人工验证样本量偏小(n=32-34/type), scopal CI [0.00, 1.00] 无信息\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R9-W5. §4.4 正文仍过于乐观。\"\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R1 SHOULD-FIX, R2 AGREE. 100/6=32-34 per type, scopal CI [0.00, 1.00] 完全无信息。理想: 扩大至每类≥80; 最低: 正文明确标注 per-type κ 不具类型间比较价值。\"\n  action_items:\n    - round: 10\n      action: \"(1) 正文 §4.4 明确标注 per-type κ 因样本量不足不具类型间比较价值; (2) 如有资源, 扩大人工标注至每类≥80\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W6\"\n  summary: \"Cross-judge 设计使 judge identity 与 model identity 混淆, 影响 C2 pooled rates 和 C4\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R9-W6. LLaMA Δ=+20pp 暗示跨 provider effect 受 instruction-following quality 调节。\"\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R1 SHOULD-FIX, R2 AGREE with nuance. Matched-pair 消除 Δpp 中的 bias(C1 safe), 但 C2 pooled absolute rates 和 C4 跨模型比较受影响。Within-judge-group C3 各自未达显著。建议报告 C2 within-judge-group 分析。\"\n  action_items:\n    - round: 10\n      action: \"(1) 报告 C2 type ranking 在两个 judge subgroup 内是否一致; (2) 如可行, 补充双 judge 评估更多组合\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W7\"\n  summary: \"条件间句子长度差异 d=0.74 需报告 per-type 分布\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R1 SHOULD-FIX, R2 partial REBUT. R2 指出 matched-pair 和 logistic regression 已有部分控制, 但同意需报告 per-type 句长分布, 特别是 incompleteness 是否系统性更长。\"\n  action_items:\n    - round: 10\n      action: \"报告 per-type 句长分布和 condition×type 交互; 如 incompleteness 系统性更长则在 confound 讨论中标注\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# MINOR ISSUES\n# ============================================================\n\n- id: \"R10-M1\"\n  summary: \"Clause pair 构建 96% pass rate 未报告 type assignment κ\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R1 MINOR(W7), R2 AGREE. 96% 不区分 agreement 和 chance agreement。\"\n  action_items:\n    - round: 10\n      action: \"补充 type assignment 的 Cohen's κ 或 Fleiss' κ\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M2\"\n  summary: \"引用问题: ferrari_defects_2018 作者不一致 + 2 orphan bib entries + navigli_wsd_2009 待确认\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R2]\n      note: \"R9-M1, R9-M2.\"\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"两人共识. ferrari_defects_2018 第一作者应为 Rosadini; tamkin_evaluating_2023 和 yin_safeagentbench_2025 为 orphan entries; navigli_wsd_2009 年份待核实。\"\n  action_items:\n    - round: 10\n      action: \"核实并修正 bib entries; 删除或引用 orphan entries; 确认 navigli 引用准确性\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M3\"\n  summary: \"Reproducibility ICC=0.919 仅覆盖 OpenAI 模型族, 跨 provider 稳定性未测量\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R1, R2]\n      note: \"R9-W6 部分. Limitations 已承认。\"\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"R1 MINOR(W9), R2 AGREE. temperature=0 下同 provider 高 ICC 不意外, 有意义的是跨 provider 稳定性。\"\n  action_items:\n    - round: 10\n      action: \"如可行, 至少在 1-2 个非 OpenAI 模型上补充 test-retest data\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M4\"\n  summary: \"Psycholinguistics 类比(garden-path, good-enough processing) 可能 over-extended\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [R2, R1]\n      note: \"R2 MINOR(W6), R1 AGREE. Autoregressive generation 与 incremental parsing 机制不同。§6.2 'paralleling human good-enough processing' 需加 mechanism-level caveat。\"\n  action_items:\n    - round: 10\n      action: \"§6.2 加一句 'though the underlying mechanisms are likely distinct'\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M5\"\n  summary: \"Coreferential 被系统性排除在 mitigation 和 replication 之外, 削弱分析完整性\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [R2, R1]\n      note: \"R9-W9.\"\n    - round: 10\n      reviewers: [R1, R2]\n      note: \"两人均在 Questions 中提出(R1-Q6, R2-Q3). 排除理由需更充分解释。\"\n  action_items:\n    - round: 10\n      action: \"Appendix 补充 coreferential 排除的详细理由\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M6\"\n  summary: \"Pages 3-5 连续纯文本无 display item, Taxonomy 需可视化\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"R9-M8. 视觉审查发现。\"\n    - round: 10\n      reviewers: []\n      note: \"视觉审查再次标记: 连续 3 页纯文本, Taxonomy 适合汇总表或层级图。\"\n  action_items:\n    - round: 10\n      action: \"§3 Taxonomy 加一张类型汇总表打破纯文本节奏\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# PREVIOUSLY RESOLVED (confirmed in Round 10)\n# ============================================================\n\n- id: \"R8-W1-resolved\"\n  summary: \"缺少 API 超参数报告\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"§4.3 reports temperature=0, top_p=1, max_tokens=4096. 本轮未提及。\"\n  resolution: \"§4.3 添加完整 API 超参数\"\n  resolution_round: 9\n\n- id: \"R8-W4-resolved\"\n  summary: \"无代码/数据可用性声明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"Data and Code Availability section 已存在。本轮未提及。\"\n  resolution: \"添加 Data and Code Availability section\"\n  resolution_round: 9\n\n- id: \"R9-W7-resolved\"\n  summary: \"多重比较校正 three test families 未明确定义\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"Appendix L 已明确列出 3 families。本轮未提及。\"\n  resolution: \"Appendix L 新增 Multiple Comparison Correction 小节\"\n  resolution_round: 10\n\n- id: \"R9-W8-resolved\"\n  summary: \"与 DRIP-R 的 taxonomy type-level 映射缺失\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"Appendix L 有 DRIP-R mapping。R2 S5 肯定了 concurrent work 定位清晰。\"\n  resolution: \"Appendix L 新增 DRIP-R Category Mapping\"\n  resolution_round: 10\n\n- id: \"R9-M3-resolved\"\n  summary: \"Introduction 'seven models' 措辞应区分 main study (5) vs replication (2)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"§1 已改为 'five primary models and confirmed in two additional replication models'。本轮未提及。\"\n  resolution: \"措辞已修正\"\n  resolution_round: 10\n\n- id: \"R9-M7-resolved\"\n  summary: \"§5.4 F(20) 缺少 denominator df\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"§5.4 已改为 F(20, 2976)。本轮未提及。\"\n  resolution: \"F(20) → F(20, 2976)\"\n  resolution_round: 10\n"
  }
}
```

</details>

---


### Tool result

_source line 899 · 2026-05-21T19:12:59.428810+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml\", \"bytes\": 13945}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 900 · 2026-05-21T19:15:47.513549+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "report": "# 审稿报告 — Round 10 (Fresh)\n\n**论文**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 via ARR May cycle (Deadline: 2026-05-25)\n**审稿模式**: Fresh（从头初审）\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）\n**轮次**: 1 轮初审 + 1 轮交叉回应（关键问题达成共识，无需第二轮）\n\n---\n\n## Summary\n\n本文在 τ²-bench 上构建 300 组 matched clause pairs（6 种歧义类型 × 50 pairs），通过 5 个模型运行 2,997 episodes，因果量化了政策歧义对 LLM agent 安全违规的影响。核心发现：歧义使违规率上升 34.0 pp（OR=15.1），incompleteness 在全部 7 个模型中稳居最高风险类型（≥46%），agents 在 >89% 的情况下展现 \"disambiguation deficit\"（不识别歧义直接执行）。实验设计采用 matched-pair causal identification + perturbation control，统计方法全面（TOST、bootstrap cluster、Holm-Bonferroni、logistic regression），局限性透明度在同类工作中属上乘。\n\n---\n\n## Strengths\n\n**S1. 严谨的因果实验设计。** Matched-pair design 是本文最大亮点——每组 clause pair 仅做 minimal edit，within-clause 比较有效控制 clause-level 混淆变量。Perturbation control（Δ=-0.67pp, CI 含零）排除表面扰动。Incompleteness 的 information-addition confound 通过 logistic regression + coreferential 下界双重控制。这种 causal identification strategy 在 agent safety 文献中确实少见。[R1-S2, R2-S1 共识]\n\n**S2. 统计方法论全面且透明。** TOST 等价检验 + 7 级 margin 敏感性分析 + margin-free bootstrap cluster analysis（Ward's method, B=10,000）+ Holm-Bonferroni 三 test families + ICC 可复现性验证。SESOI=±15pp 有明确 domain-relevant anchoring 且给出完整敏感性分析。这是近期 agent safety 论文中统计严谨度最高的之一。[R1-S3, R2-S2 共识]\n\n**S3. 诚实报告负面/不确定结果。** C3（layer effect）标注为 inconclusive；authorization scope κ=0.385 在正文和 Limitations 中反复标注；bootstrap AU p-value=0.47 明确报告；incompleteness 标注为 upper bound。这种透明度值得肯定。[R1-S4, R2-S3 共识]\n\n**S4. 跨模型复制增强泛化性。** 7 个模型覆盖 6 个 provider（4 proprietary + 3 open-source），Gemini 和 LLaMA 独立复制。Incompleteness 在全部 7 个模型中 ≥46%。[R1-S5, R2-S4 共识]\n\n**S5. Concurrent work 定位清晰。** 与 DRIP-R（2026）的三点区分具体有说服力，Appendix 的 category mapping 表明作者认真研究了 concurrent work。[R2-S5]\n\n**S6. Failure mode taxonomy 有经验证据支撑。** 614 条 violation traces 编码为三种机制不同的失败模式，与歧义类型形成可解释的对应。Disambiguation Deficit（4.6% overall awareness, Qwen3/DeepSeek 为零）是有实用价值的定量发现。[R1-S6, R1-S7, R2-S6]\n\n---\n\n## Weaknesses\n\n### MUST-FIX\n\n**[MUST-FIX-1] Authorization scope κ=0.385 不足以支撑 C4 中 52pp range 作为核心发现。** [R1-W1 = R2-W5, 两人完全共识]\n- Cross-judge κ=0.385 低于 fair agreement 门槛（0.40），human-LLM κ=0.644，CI [0.35, 0.91]。52pp range 中真实模型差异 vs 测量噪声无法分离。\n- Abstract 括号注释 \"though measured with the lowest inter-judge agreement, κ=0.385\" 过于弱化，读者易忽略。Introduction（§1）复述 52pp 时完全无可靠性 caveat。\n- **要求**: (1) Abstract 将 auth scope 从主要发现降格为初步发现，明确标注不确定性；(2) Introduction 同等篇幅讨论可靠性限制；(3) C4 分析展示去除 auth scope 后交互效应是否仍显著；(4) 52pp 标记为 upper bound with substantial measurement uncertainty。\n\n**[MUST-FIX-2] Two-tier hierarchy (C2) 的统计稳定性不足以支撑当前表述。** [R2-W1 = R1-W6, 两人完全共识]\n- Bootstrap cluster analysis 中 incompleteness singleton 仅在 34.3% 的 samples 中出现，AU p-value=0.47。TOST 在 ±10pp 时仅 3/6 mid-tier pairs 等价（power=0.57）。Kendall's W=0.398（p=0.072）五模型下不显著。\n- Abstract 称 \"a two-tier type hierarchy separates incompleteness from the remaining five types\"，Introduction/Conclusion 同样确定性表述——远超 34.3% bootstrap support。\n- **要求**: (1) 措辞弱化为 \"incompleteness tends to cluster as the highest-risk type, though the tier boundary is not sharp\"；(2) 正文并列呈现 ±10pp（three-tier）与 ±15pp（two-tier）叙事；(3) 考虑将 C2 核心声明缩窄为 \"incompleteness is consistently the highest-risk type\"（7/7 模型支持）。\n\n### SHOULD-FIX\n\n**[SHOULD-FIX-1] Taxonomy 理论基础需更充分讨论。** [R2-W2, R1 partial REBUT]\n- Incompleteness（information absence）和 conditional precedence（normative conflict）不满足 Wasow (2005) 对 ambiguity 的 strict 定义（\"multiple distinct interpretations\"）。§3 \"Scope of 'ambiguity'\" 段落已有初步讨论，但 R2 认为不够充分。R1 认为操作性定义可辩护，但同意需扩展讨论。\n- **分歧记录**: R2 认为这是根本性概念混淆（行为结果定义输入类型=循环论证），R1 认为操作性定义在实证研究中是标准做法。两人共识是需要更深入的理论讨论，但不必改变 taxonomy 设计。\n- **建议**: (1) §3 扩展理论边界讨论，引用 Dalpiaz et al. (2018)；(2) 考虑在标题/abstract 中使用更精确限定。\n\n**[SHOULD-FIX-2] Incompleteness confound 控制仅有粗粒度 proxy。** [R1-W2, R2 AGREE]\n- Token count 是 coarse proxy（论文自身承认），更细粒度语义衡量可能揭示不同 confound 结构。Coreferential 下界（31.6%）约束整体 ambiguity 的下界，无法分离 incompleteness 的 information-addition component。\n- **建议**: (1) hierarchy 声明中标注 \"conditional on confound assumptions\"；(2) 报告 per-type token delta distribution。\n\n**[SHOULD-FIX-3] Differential Nocuity 框架增量贡献被过度表述。** [R2-W3, R1 AGREE]\n- Berry & Kamsties (2004)、Willis et al. (2008) 已测量 type-specific nocuity。论文贡献是 LLM agent 场景的实证验证，但 §7 写法暗示新框架。\n- **建议**: 改为 \"extends Berry & Kamsties' distinction to LLM agents\"，明确 credit 先驱工作。\n\n**[SHOULD-FIX-4] Disambiguation Deficit 命名暗示 inability。** [R2-W4, R1 AGREE with nuance]\n- \"Deficit\" 暗示能力缺失，但 mitigation experiment（-8.5pp）证明可通过 prompt 改善。§6.2 已有澄清但术语易误读。\n- **建议**: 定义中明确指 \"absence of disambiguation behavior in default (uninstructed) settings, not inability\"；考虑 \"Disambiguation Neglect\" 等更精确术语。\n\n**[SHOULD-FIX-5] Per-type 人工验证样本量不足。** [R1-W4, R2 AGREE]\n- 100 episodes / 6 types = 32-34 per type。Scopal κ CI [0.00, 1.00] 完全无信息。C2 是 type-level 分析但 per-type 验证精度不足。\n- **建议**: 至少在正文 §4.4 明确标注 per-type κ 不具类型间比较价值；理想情况扩大至每类 ≥80。\n\n**[SHOULD-FIX-6] Cross-judge 设计中 judge identity 与 model identity 混淆。** [R1-W5, R2 AGREE with nuance]\n- Matched-pair 消除 Δpp 中的 judge bias（C1 safe），但 C2 pooled absolute rates 和 C4 跨模型比较受影响。Within-judge-group C3 各自未达显著。\n- **建议**: 报告 C2 type ranking 在两个 judge subgroup 内是否一致。\n\n**[SHOULD-FIX-7] 条件间句子长度差异需补充分析。** [R1-W3, R2 partial REBUT]\n- d=0.74 是中等到大效应量。R2 指出 matched-pair design 和 logistic regression（token delta, OR=1.022）已有部分控制，但两人同意需报告 per-type 句长分布，特别关注 incompleteness 是否系统性更长。\n\n### MINOR\n\n- **[MINOR-1]** Clause pair 构建 96% pass rate 未报告 type assignment κ（§4.2）。[R1-W7, R2 AGREE]\n- **[MINOR-2]** 引用问题：ferrari_defects_2018 第一作者应为 Rosadini；2 orphan bib entries（tamkin_evaluating_2023, yin_safeagentbench_2025）；navigli_wsd_2009 年份待核实。[R1-W8 = R2-W7]\n- **[MINOR-3]** ICC=0.919 仅覆盖 OpenAI 模型族，跨 provider 稳定性未测量。[R1-W9, R2 AGREE]\n- **[MINOR-4]** Psycholinguistics 类比（garden-path, good-enough processing）需加 mechanism-level caveat。[R2-W6, R1 AGREE]\n- **[MINOR-5]** Coreferential 被系统性排除在 mitigation 和 replication 之外，排除理由需更充分解释。[R1-Q6, R2-Q3]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识（标注 [AGREE]）：\n\n1. **C1 是坚实的核心贡献**——matched-pair design + perturbation control + 7 模型复制，因果推断策略正确\n2. **Authorization scope 52pp 不可靠**——κ=0.385 使得该类型的绝对违规率有极大测量不确定性，需大幅下调表述\n3. **Two-tier hierarchy 声称过强**——bootstrap 34.3%、margin 依赖性、Kendall's W 不显著，需缩窄为 \"incompleteness 一致性上界\"\n4. **Differential Nocuity 是 domain transfer 而非新框架**——需正确归属先驱工作\n5. **Per-type 人工验证不足**——32-34/type 的 κ 估计无统计力度\n6. **引用问题**——orphan entries + 作者/年份不一致\n\n## Reviewer Divergence\n\n1. **Taxonomy 概念混淆的严重程度**（轻微分歧）：\n   - R2 认为是根本性概念混淆——incompleteness/conditional precedence 不满足 ambiguity 定义，§3 的 operational defense 是循环论证\n   - R1 REBUT：操作性定义在实证研究中是标准做法，§3 已有初步回应，但同意需扩展讨论\n   - **Director 判断**: R1 的 REBUT 有理，但 R2 的理论关切对 CL-savvy 审稿人有说服力。建议扩展 §3 讨论并引用 Dalpiaz et al. (2018)，不改变 taxonomy 设计。\n\n2. **句子长度 confound 的严重程度**（轻微分歧）：\n   - R1 认为 d=0.74 是未控制的 confound\n   - R2 partial REBUT：matched-pair design 和 logistic regression（token delta）已有控制\n   - **Director 判断**: R2 的反驳合理——within-pair 控制确实吸收了 pair-level variance。但两人同意需报告 per-type 句长分布。\n\n---\n\n## Questions\n\n合并两位 Reviewer 提出的关键问题：\n\n1. **Per-type 句子长度分布**: incompleteness clauses 是否系统性更长？如果是，与 W2 confound 叠加。[R1-Q1]\n2. **Variance decomposition 残余 ~76% 方差来源**: 是否主要是 clause-level heterogeneity？如果 type 内 clause 间变异远大于 type 间变异，type-level 概括的信度如何？[R1-Q2]\n3. **Incompleteness 与 Wasow (2005) ambiguity 定义的兼容性**: information absence 如何满足 \"multiple interpretations\" 要求？[R2-Q1]\n4. **Bootstrap 34.3% vs continuum 假说**: 如果违规率分布是连续而非离散两层，哪些结论需要修改？[R2-Q2]\n5. **Domain-specific SESOI**: ±15pp 对 high-stakes domain（医疗/金融）是否过于宽松？[R2-Q5]\n6. **Coreferential 排除 mitigation 的理由**: 作为 information-delta=0 的纯粹 ambiguity 类型，其 mitigation 结果对 disambiguation deficit 解释有重要影响。[R1-Q6, R2-Q3]\n7. **Perturbation control 的模型分布**: 300 episodes 是否在 5 个主模型上均匀分布？[R1-Q3]\n8. **Clause pairs 的 domain 分布**: 是否在 retail/airline 间均匀分布？domain 是否混淆 type effects？[R1-Q5]\n\n---\n\n## Missing References\n\n两位 Reviewer 合并建议（去重后）：\n\n1. **Dalpiaz, van der Schalk, & Lucassen (2018)**. \"Pinpointing Ambiguity and Incompleteness in Requirements Engineering via Information Visualization and NLP.\" REFSQ 2018. 直接相关——明确区分 ambiguity 和 incompleteness 作为不同 requirements defects。[R2, R1 同意]\n2. **Yu, Carroll, & Bentley (2026)**. \"The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents.\" arXiv:2603.20320. Concurrent matched-pair causal design for agent safety，对 \"first causal quantification\" claim 需更精确 scoping。[R2, R1 同意需确认存在性]\n3. **Lin et al. (2025)**. \"Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue.\" 与 disambiguation channel design 讨论相关。[R2]\n4. **Willis et al. (2008)** — §7 Discussion 中需明确 credit 其 type-specific nocuity 先驱测量。[R2, R1 同意]\n5. **Tamkin et al. (2023)** \"Evaluating and Mitigating Discrimination in Language Model Decisions\" — 与 auth scope permissiveness bias 相关。已在 bib 中但为 orphan entry。[R1]\n6. **Mu et al. (2023)** \"Can LLMs Follow Simple Rules?\" — policy compliance benchmark。[R1]\n7. **Deemter (2010)** \"Not Exactly: In Praise of Vagueness\"; **Lassiter & Goodman (2017)** probabilistic pragmatics — vagueness 文献扩展。[R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时约 3 分钟）\n\n### Findings\n\n**Warnings (2)**:\n- **Pages 3-5**: 连续 3 页纯文本（Taxonomy + Method + Statistical Analysis），无任何 display item。Taxonomy 部分（§3, page 3）适合用汇总表或层级结构图打破纯文本节奏。\n- **Pages 1-8**: 主文 8 页仅 4 个 display items（3 figures + 1 table），对实证论文偏少（通常 5-8 个）。建议 §3 加类型汇总表，§5 提炼 summary table。\n\n**Info (7)**:\n- Figure 1 内部标签字号偏小（page 2）\n- Figure 2 压缩在单栏内，可考虑改为 figure*（page 6）\n- Figure 3 颜色区分度良好，建议确认色盲友好性（page 7）\n- 首页无视觉锚点，可考虑 teaser figure（page 1）\n- Table 1 排版规范（page 6）\n- Appendix Tables 紧凑但可读（page 12）\n- Limitations 段落简短覆盖 3 点，符合 EMNLP 要求（page 8）\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5（Borderline Conference）**\n**Soundness: 3.5 / 5**\n**Excitement: 3.25 / 5**（R1: 3.5, R2: 3.0 均值）\n**Reproducibility: 4 / 5**\n**Confidence: 4 / 5**\n\n### 评分理由\n\n**C1（Binary Ambiguity Effect）是扎实的实证贡献**——+34pp, OR=15.1, perturbation control 排除表面扰动, 7 模型复制, 这一因果发现在 agent safety 文献中确有新意，单独可支撑 Findings 水平。\n\n**C2（Type Hierarchy）的核心部分——incompleteness 一致性上界——是稳健的**（7/7 模型 ≥46%），但 \"two-tier hierarchy\" 的结构性声称统计支撑不足（bootstrap 34.3%, margin-dependent）。当前表述强于证据。\n\n**C4（Model×Type Interaction）受 authorization scope 低可靠性严重影响**——52pp range 这一最引人注目的数字也是最不可靠的。去除 auth scope 后 C4 是否仍显著未知。\n\n**Taxonomy 理论基础**有可辩护的操作性定义，但需要更充分的讨论来应对 CL-savvy 审稿人的质疑。\n\n**Disambiguation Deficit** 是有实用价值的发现（4.6% awareness, mitigation -8.5pp），但命名和框架需要微调。\n\n### 升分路径\n\n如果作者在修订中：(a) 大幅弱化 auth scope / hierarchy 的确定性表述，(b) 补充 C4 去除 auth scope 后的 robustness check，(c) 扩展 §3 理论讨论，(d) 报告 per-type 句长分布和 within-judge-group C2 分析——论文有 4.0（Conference acceptance）的潜力。核心实验设计和 C1 发现是 4.0 水平的贡献，当前拖累评分的主要是 claims 与 evidence 之间的 calibration gap。\n\n---\n\n## Detailed Comments\n\n### §Abstract\n- \"a two-tier type hierarchy separates incompleteness from the remaining five types\" → 弱化为 \"incompleteness consistently emerges as the highest-risk type, though tier boundaries are margin-dependent\"\n- \"authorization scope shows the widest cross-model range (52 pp, though measured with the lowest inter-judge agreement, κ = 0.385)\" → 括号内信息需提升为同等权重的正文表述，或删除 52pp 具体数字\n- 整体信息密度可接受，但 R2 认为偏密集\n\n### §1 Introduction\n- Contribution (2) \"a two-tier type hierarchy\" → 缩窄为 \"incompleteness as a consistent upper-bound risk type\"\n- 复述 52pp 时需同等篇幅讨论 κ=0.385 的可靠性限制\n- \"observed across five primary models and confirmed in two additional replication models\" ✓（已修正 R9 的 'seven models' 问题）\n\n### §3 Ambiguity Taxonomy\n- \"Scope of 'ambiguity'\" 段落方向正确，但需扩展：引用 Dalpiaz et al. (2018) 的 ambiguity/incompleteness 区分；更深入讨论 operational vs strict definition 的 tradeoff\n- Layer distinction 作为 theoretical organizing principle 保留合理（C3 已标注 inconclusive）\n- 视觉审查建议增加 taxonomy 汇总表（目前 pp.3-5 连续纯文本）\n\n### §4 Method\n- §4.2: 补充 type assignment 的 Cohen's κ（当前仅有 96% pass rate）\n- §4.4: 正文中标注 per-type κ 因样本量不足（n=32-34/type）不具类型间比较价值\n- §4.5: ICC 仅覆盖 OpenAI，在 Limitations 中已承认但可在此处也标注\n- §4.6: SESOI=±15pp 的 anchoring 合理，但建议在正文中更突出讨论 margin 敏感性\n\n### §5 Results\n- §5.2: 并列呈现 ±10pp three-tier 与 ±15pp two-tier 叙事\n- §5.2: incompleteness hierarchy 声明加 \"conditional on confound assumptions\" caveat\n- §5.4: 展示去除 authorization scope 后 C4 交互效应是否仍显著\n- §5.4: auth scope 52pp range 标记为 upper bound with substantial measurement uncertainty\n\n### §6 Error Analysis\n- §6.1: Gwet's AC₁ vs Cohen's κ 差异的 prevalence paradox 解释可再充实一句\n- §6.2: \"Disambiguation Deficit\" 定义加 \"in default (uninstructed) settings, not inability\" 限定\n- §6.2: \"paralleling human good-enough processing\" 加 mechanism-level caveat\n\n### §7 Discussion\n- \"Differential nocuity\" → \"extends Berry & Kamsties' distinction to LLM agents, where all ambiguity is nocuous but type-specific severity varies\"\n- 明确 credit Willis et al. (2008) 对 type-specific nocuity 的先驱测量\n\n### Limitations\n- 当前覆盖面合理（model coverage, domain scope, synthetic ambiguity, cross-judge, incompleteness confound, severity threshold, per-type reliability）\n- 建议补充 sentence length confound 和 SESOI domain-specificity 的讨论\n\n### References\n- 修正 ferrari_defects_2018（第一作者 Rosadini）\n- 删除或引用 tamkin_evaluating_2023, yin_safeagentbench_2025\n- 核实 navigli_wsd_2009 准确性\n- 补充 Dalpiaz et al. (2018), Willis et al. (2008) in §7, 以及其他建议引用\n\n### Appendix\n- Coreferential 排除理由需更充分解释（mitigation + replication 均排除）\n- 报告 per-type 句长分布\n- C2 within-judge-group 分析\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "policy_ambiguity_safety",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "report": "# 审稿报告 — Round 10 (Fresh)\n\n**论文**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 via ARR May cycle (Deadline: 2026-05-25)\n**审稿模式**: Fresh（从头初审）\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）\n**轮次**: 1 轮初审 + 1 轮交叉回应（关键问题达成共识，无需第二轮）\n\n---\n\n## Summary\n\n本文在 τ²-bench 上构建 300 组 matched clause pairs（6 种歧义类型 × 50 pairs），通过 5 个模型运行 2,997 episodes，因果量化了政策歧义对 LLM agent 安全违规的影响。核心发现：歧义使违规率上升 34.0 pp（OR=15.1），incompleteness 在全部 7 个模型中稳居最高风险类型（≥46%），agents 在 >89% 的情况下展现 \"disambiguation deficit\"（不识别歧义直接执行）。实验设计采用 matched-pair causal identification + perturbation control，统计方法全面（TOST、bootstrap cluster、Holm-Bonferroni、logistic regression），局限性透明度在同类工作中属上乘。\n\n---\n\n## Strengths\n\n**S1. 严谨的因果实验设计。** Matched-pair design 是本文最大亮点——每组 clause pair 仅做 minimal edit，within-clause 比较有效控制 clause-level 混淆变量。Perturbation control（Δ=-0.67pp, CI 含零）排除表面扰动。Incompleteness 的 information-addition confound 通过 logistic regression + coreferential 下界双重控制。这种 causal identification strategy 在 agent safety 文献中确实少见。[R1-S2, R2-S1 共识]\n\n**S2. 统计方法论全面且透明。** TOST 等价检验 + 7 级 margin 敏感性分析 + margin-free bootstrap cluster analysis（Ward's method, B=10,000）+ Holm-Bonferroni 三 test families + ICC 可复现性验证。SESOI=±15pp 有明确 domain-relevant anchoring 且给出完整敏感性分析。这是近期 agent safety 论文中统计严谨度最高的之一。[R1-S3, R2-S2 共识]\n\n**S3. 诚实报告负面/不确定结果。** C3（layer effect）标注为 inconclusive；authorization scope κ=0.385 在正文和 Limitations 中反复标注；bootstrap AU p-value=0.47 明确报告；incompleteness 标注为 upper bound。这种透明度值得肯定。[R1-S4, R2-S3 共识]\n\n**S4. 跨模型复制增强泛化性。** 7 个模型覆盖 6 个 provider（4 proprietary + 3 open-source），Gemini 和 LLaMA 独立复制。Incompleteness 在全部 7 个模型中 ≥46%。[R1-S5, R2-S4 共识]\n\n**S5. Concurrent work 定位清晰。** 与 DRIP-R（2026）的三点区分具体有说服力，Appendix 的 category mapping 表明作者认真研究了 concurrent work。[R2-S5]\n\n**S6. Failure mode taxonomy 有经验证据支撑。** 614 条 violation traces 编码为三种机制不同的失败模式，与歧义类型形成可解释的对应。Disambiguation Deficit（4.6% overall awareness, Qwen3/DeepSeek 为零）是有实用价值的定量发现。[R1-S6, R1-S7, R2-S6]\n\n---\n\n## Weaknesses\n\n### MUST-FIX\n\n**[MUST-FIX-1] Authorization scope κ=0.385 不足以支撑 C4 中 52pp range 作为核心发现。** [R1-W1 = R2-W5, 两人完全共识]\n- Cross-judge κ=0.385 低于 fair agreement 门槛（0.40），human-LLM κ=0.644，CI [0.35, 0.91]。52pp range 中真实模型差异 vs 测量噪声无法分离。\n- Abstract 括号注释 \"though measured with the lowest inter-judge agreement, κ=0.385\" 过于弱化，读者易忽略。Introduction（§1）复述 52pp 时完全无可靠性 caveat。\n- **要求**: (1) Abstract 将 auth scope 从主要发现降格为初步发现，明确标注不确定性；(2) Introduction 同等篇幅讨论可靠性限制；(3) C4 分析展示去除 auth scope 后交互效应是否仍显著；(4) 52pp 标记为 upper bound with substantial measurement uncertainty。\n\n**[MUST-FIX-2] Two-tier hierarchy (C2) 的统计稳定性不足以支撑当前表述。** [R2-W1 = R1-W6, 两人完全共识]\n- Bootstrap cluster analysis 中 incompleteness singleton 仅在 34.3% 的 samples 中出现，AU p-value=0.47。TOST 在 ±10pp 时仅 3/6 mid-tier pairs 等价（power=0.57）。Kendall's W=0.398（p=0.072）五模型下不显著。\n- Abstract 称 \"a two-tier type hierarchy separates incompleteness from the remaining five types\"，Introduction/Conclusion 同样确定性表述——远超 34.3% bootstrap support。\n- **要求**: (1) 措辞弱化为 \"incompleteness tends to cluster as the highest-risk type, though the tier boundary is not sharp\"；(2) 正文并列呈现 ±10pp（three-tier）与 ±15pp（two-tier）叙事；(3) 考虑将 C2 核心声明缩窄为 \"incompleteness is consistently the highest-risk type\"（7/7 模型支持）。\n\n### SHOULD-FIX\n\n**[SHOULD-FIX-1] Taxonomy 理论基础需更充分讨论。** [R2-W2, R1 partial REBUT]\n- Incompleteness（information absence）和 conditional precedence（normative conflict）不满足 Wasow (2005) 对 ambiguity 的 strict 定义（\"multiple distinct interpretations\"）。§3 \"Scope of 'ambiguity'\" 段落已有初步讨论，但 R2 认为不够充分。R1 认为操作性定义可辩护，但同意需扩展讨论。\n- **分歧记录**: R2 认为这是根本性概念混淆（行为结果定义输入类型=循环论证），R1 认为操作性定义在实证研究中是标准做法。两人共识是需要更深入的理论讨论，但不必改变 taxonomy 设计。\n- **建议**: (1) §3 扩展理论边界讨论，引用 Dalpiaz et al. (2018)；(2) 考虑在标题/abstract 中使用更精确限定。\n\n**[SHOULD-FIX-2] Incompleteness confound 控制仅有粗粒度 proxy。** [R1-W2, R2 AGREE]\n- Token count 是 coarse proxy（论文自身承认），更细粒度语义衡量可能揭示不同 confound 结构。Coreferential 下界（31.6%）约束整体 ambiguity 的下界，无法分离 incompleteness 的 information-addition component。\n- **建议**: (1) hierarchy 声明中标注 \"conditional on confound assumptions\"；(2) 报告 per-type token delta distribution。\n\n**[SHOULD-FIX-3] Differential Nocuity 框架增量贡献被过度表述。** [R2-W3, R1 AGREE]\n- Berry & Kamsties (2004)、Willis et al. (2008) 已测量 type-specific nocuity。论文贡献是 LLM agent 场景的实证验证，但 §7 写法暗示新框架。\n- **建议**: 改为 \"extends Berry & Kamsties' distinction to LLM agents\"，明确 credit 先驱工作。\n\n**[SHOULD-FIX-4] Disambiguation Deficit 命名暗示 inability。** [R2-W4, R1 AGREE with nuance]\n- \"Deficit\" 暗示能力缺失，但 mitigation experiment（-8.5pp）证明可通过 prompt 改善。§6.2 已有澄清但术语易误读。\n- **建议**: 定义中明确指 \"absence of disambiguation behavior in default (uninstructed) settings, not inability\"；考虑 \"Disambiguation Neglect\" 等更精确术语。\n\n**[SHOULD-FIX-5] Per-type 人工验证样本量不足。** [R1-W4, R2 AGREE]\n- 100 episodes / 6 types = 32-34 per type。Scopal κ CI [0.00, 1.00] 完全无信息。C2 是 type-level 分析但 per-type 验证精度不足。\n- **建议**: 至少在正文 §4.4 明确标注 per-type κ 不具类型间比较价值；理想情况扩大至每类 ≥80。\n\n**[SHOULD-FIX-6] Cross-judge 设计中 judge identity 与 model identity 混淆。** [R1-W5, R2 AGREE with nuance]\n- Matched-pair 消除 Δpp 中的 judge bias（C1 safe），但 C2 pooled absolute rates 和 C4 跨模型比较受影响。Within-judge-group C3 各自未达显著。\n- **建议**: 报告 C2 type ranking 在两个 judge subgroup 内是否一致。\n\n**[SHOULD-FIX-7] 条件间句子长度差异需补充分析。** [R1-W3, R2 partial REBUT]\n- d=0.74 是中等到大效应量。R2 指出 matched-pair design 和 logistic regression（token delta, OR=1.022）已有部分控制，但两人同意需报告 per-type 句长分布，特别关注 incompleteness 是否系统性更长。\n\n### MINOR\n\n- **[MINOR-1]** Clause pair 构建 96% pass rate 未报告 type assignment κ（§4.2）。[R1-W7, R2 AGREE]\n- **[MINOR-2]** 引用问题：ferrari_defects_2018 第一作者应为 Rosadini；2 orphan bib entries（tamkin_evaluating_2023, yin_safeagentbench_2025）；navigli_wsd_2009 年份待核实。[R1-W8 = R2-W7]\n- **[MINOR-3]** ICC=0.919 仅覆盖 OpenAI 模型族，跨 provider 稳定性未测量。[R1-W9, R2 AGREE]\n- **[MINOR-4]** Psycholinguistics 类比（garden-path, good-enough processing）需加 mechanism-level caveat。[R2-W6, R1 AGREE]\n- **[MINOR-5]** Coreferential 被系统性排除在 mitigation 和 replication 之外，排除理由需更充分解释。[R1-Q6, R2-Q3]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识（标注 [AGREE]）：\n\n1. **C1 是坚实的核心贡献**——matched-pair design + perturbation control + 7 模型复制，因果推断策略正确\n2. **Authorization scope 52pp 不可靠**——κ=0.385 使得该类型的绝对违规率有极大测量不确定性，需大幅下调表述\n3. **Two-tier hierarchy 声称过强**——bootstrap 34.3%、margin 依赖性、Kendall's W 不显著，需缩窄为 \"incompleteness 一致性上界\"\n4. **Differential Nocuity 是 domain transfer 而非新框架**——需正确归属先驱工作\n5. **Per-type 人工验证不足**——32-34/type 的 κ 估计无统计力度\n6. **引用问题**——orphan entries + 作者/年份不一致\n\n## Reviewer Divergence\n\n1. **Taxonomy 概念混淆的严重程度**（轻微分歧）：\n   - R2 认为是根本性概念混淆——incompleteness/conditional precedence 不满足 ambiguity 定义，§3 的 operational defense 是循环论证\n   - R1 REBUT：操作性定义在实证研究中是标准做法，§3 已有初步回应，但同意需扩展讨论\n   - **Director 判断**: R1 的 REBUT 有理，但 R2 的理论关切对 CL-savvy 审稿人有说服力。建议扩展 §3 讨论并引用 Dalpiaz et al. (2018)，不改变 taxonomy 设计。\n\n2. **句子长度 confound 的严重程度**（轻微分歧）：\n   - R1 认为 d=0.74 是未控制的 confound\n   - R2 partial REBUT：matched-pair design 和 logistic regression（token delta）已有控制\n   - **Director 判断**: R2 的反驳合理——within-pair 控制确实吸收了 pair-level variance。但两人同意需报告 per-type 句长分布。\n\n---\n\n## Questions\n\n合并两位 Reviewer 提出的关键问题：\n\n1. **Per-type 句子长度分布**: incompleteness clauses 是否系统性更长？如果是，与 W2 confound 叠加。[R1-Q1]\n2. **Variance decomposition 残余 ~76% 方差来源**: 是否主要是 clause-level heterogeneity？如果 type 内 clause 间变异远大于 type 间变异，type-level 概括的信度如何？[R1-Q2]\n3. **Incompleteness 与 Wasow (2005) ambiguity 定义的兼容性**: information absence 如何满足 \"multiple interpretations\" 要求？[R2-Q1]\n4. **Bootstrap 34.3% vs continuum 假说**: 如果违规率分布是连续而非离散两层，哪些结论需要修改？[R2-Q2]\n5. **Domain-specific SESOI**: ±15pp 对 high-stakes domain（医疗/金融）是否过于宽松？[R2-Q5]\n6. **Coreferential 排除 mitigation 的理由**: 作为 information-delta=0 的纯粹 ambiguity 类型，其 mitigation 结果对 disambiguation deficit 解释有重要影响。[R1-Q6, R2-Q3]\n7. **Perturbation control 的模型分布**: 300 episodes 是否在 5 个主模型上均匀分布？[R1-Q3]\n8. **Clause pairs 的 domain 分布**: 是否在 retail/airline 间均匀分布？domain 是否混淆 type effects？[R1-Q5]\n\n---\n\n## Missing References\n\n两位 Reviewer 合并建议（去重后）：\n\n1. **Dalpiaz, van der Schalk, & Lucassen (2018)**. \"Pinpointing Ambiguity and Incompleteness in Requirements Engineering via Information Visualization and NLP.\" REFSQ 2018. 直接相关——明确区分 ambiguity 和 incompleteness 作为不同 requirements defects。[R2, R1 同意]\n2. **Yu, Carroll, & Bentley (2026)**. \"The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents.\" arXiv:2603.20320. Concurrent matched-pair causal design for agent safety，对 \"first causal quantification\" claim 需更精确 scoping。[R2, R1 同意需确认存在性]\n3. **Lin et al. (2025)**. \"Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue.\" 与 disambiguation channel design 讨论相关。[R2]\n4. **Willis et al. (2008)** — §7 Discussion 中需明确 credit 其 type-specific nocuity 先驱测量。[R2, R1 同意]\n5. **Tamkin et al. (2023)** \"Evaluating and Mitigating Discrimination in Language Model Decisions\" — 与 auth scope permissiveness bias 相关。已在 bib 中但为 orphan entry。[R1]\n6. **Mu et al. (2023)** \"Can LLMs Follow Simple Rules?\" — policy compliance benchmark。[R1]\n7. **Deemter (2010)** \"Not Exactly: In Praise of Vagueness\"; **Lassiter & Goodman (2017)** probabilistic pragmatics — vagueness 文献扩展。[R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时约 3 分钟）\n\n### Findings\n\n**Warnings (2)**:\n- **Pages 3-5**: 连续 3 页纯文本（Taxonomy + Method + Statistical Analysis），无任何 display item。Taxonomy 部分（§3, page 3）适合用汇总表或层级结构图打破纯文本节奏。\n- **Pages 1-8**: 主文 8 页仅 4 个 display items（3 figures + 1 table），对实证论文偏少（通常 5-8 个）。建议 §3 加类型汇总表，§5 提炼 summary table。\n\n**Info (7)**:\n- Figure 1 内部标签字号偏小（page 2）\n- Figure 2 压缩在单栏内，可考虑改为 figure*（page 6）\n- Figure 3 颜色区分度良好，建议确认色盲友好性（page 7）\n- 首页无视觉锚点，可考虑 teaser figure（page 1）\n- Table 1 排版规范（page 6）\n- Appendix Tables 紧凑但可读（page 12）\n- Limitations 段落简短覆盖 3 点，符合 EMNLP 要求（page 8）\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5（Borderline Conference）**\n**Soundness: 3.5 / 5**\n**Excitement: 3.25 / 5**（R1: 3.5, R2: 3.0 均值）\n**Reproducibility: 4 / 5**\n**Confidence: 4 / 5**\n\n### 评分理由\n\n**C1（Binary Ambiguity Effect）是扎实的实证贡献**——+34pp, OR=15.1, perturbation control 排除表面扰动, 7 模型复制, 这一因果发现在 agent safety 文献中确有新意，单独可支撑 Findings 水平。\n\n**C2（Type Hierarchy）的核心部分——incompleteness 一致性上界——是稳健的**（7/7 模型 ≥46%），但 \"two-tier hierarchy\" 的结构性声称统计支撑不足（bootstrap 34.3%, margin-dependent）。当前表述强于证据。\n\n**C4（Model×Type Interaction）受 authorization scope 低可靠性严重影响**——52pp range 这一最引人注目的数字也是最不可靠的。去除 auth scope 后 C4 是否仍显著未知。\n\n**Taxonomy 理论基础**有可辩护的操作性定义，但需要更充分的讨论来应对 CL-savvy 审稿人的质疑。\n\n**Disambiguation Deficit** 是有实用价值的发现（4.6% awareness, mitigation -8.5pp），但命名和框架需要微调。\n\n### 升分路径\n\n如果作者在修订中：(a) 大幅弱化 auth scope / hierarchy 的确定性表述，(b) 补充 C4 去除 auth scope 后的 robustness check，(c) 扩展 §3 理论讨论，(d) 报告 per-type 句长分布和 within-judge-group C2 分析——论文有 4.0（Conference acceptance）的潜力。核心实验设计和 C1 发现是 4.0 水平的贡献，当前拖累评分的主要是 claims 与 evidence 之间的 calibration gap。\n\n---\n\n## Detailed Comments\n\n### §Abstract\n- \"a two-tier type hierarchy separates incompleteness from the remaining five types\" → 弱化为 \"incompleteness consistently emerges as the highest-risk type, though tier boundaries are margin-dependent\"\n- \"authorization scope shows the widest cross-model range (52 pp, though measured with the lowest inter-judge agreement, κ = 0.385)\" → 括号内信息需提升为同等权重的正文表述，或删除 52pp 具体数字\n- 整体信息密度可接受，但 R2 认为偏密集\n\n### §1 Introduction\n- Contribution (2) \"a two-tier type hierarchy\" → 缩窄为 \"incompleteness as a consistent upper-bound risk type\"\n- 复述 52pp 时需同等篇幅讨论 κ=0.385 的可靠性限制\n- \"observed across five primary models and confirmed in two additional replication models\" ✓（已修正 R9 的 'seven models' 问题）\n\n### §3 Ambiguity Taxonomy\n- \"Scope of 'ambiguity'\" 段落方向正确，但需扩展：引用 Dalpiaz et al. (2018) 的 ambiguity/incompleteness 区分；更深入讨论 operational vs strict definition 的 tradeoff\n- Layer distinction 作为 theoretical organizing principle 保留合理（C3 已标注 inconclusive）\n- 视觉审查建议增加 taxonomy 汇总表（目前 pp.3-5 连续纯文本）\n\n### §4 Method\n- §4.2: 补充 type assignment 的 Cohen's κ（当前仅有 96% pass rate）\n- §4.4: 正文中标注 per-type κ 因样本量不足（n=32-34/type）不具类型间比较价值\n- §4.5: ICC 仅覆盖 OpenAI，在 Limitations 中已承认但可在此处也标注\n- §4.6: SESOI=±15pp 的 anchoring 合理，但建议在正文中更突出讨论 margin 敏感性\n\n### §5 Results\n- §5.2: 并列呈现 ±10pp three-tier 与 ±15pp two-tier 叙事\n- §5.2: incompleteness hierarchy 声明加 \"conditional on confound assumptions\" caveat\n- §5.4: 展示去除 authorization scope 后 C4 交互效应是否仍显著\n- §5.4: auth scope 52pp range 标记为 upper bound with substantial measurement uncertainty\n\n### §6 Error Analysis\n- §6.1: Gwet's AC₁ vs Cohen's κ 差异的 prevalence paradox 解释可再充实一句\n- §6.2: \"Disambiguation Deficit\" 定义加 \"in default (uninstructed) settings, not inability\" 限定\n- §6.2: \"paralleling human good-enough processing\" 加 mechanism-level caveat\n\n### §7 Discussion\n- \"Differential nocuity\" → \"extends Berry & Kamsties' distinction to LLM agents, where all ambiguity is nocuous but type-specific severity varies\"\n- 明确 credit Willis et al. (2008) 对 type-specific nocuity 的先驱测量\n\n### Limitations\n- 当前覆盖面合理（model coverage, domain scope, synthetic ambiguity, cross-judge, incompleteness confound, severity threshold, per-type reliability）\n- 建议补充 sentence length confound 和 SESOI domain-specificity 的讨论\n\n### References\n- 修正 ferrari_defects_2018（第一作者 Rosadini）\n- 删除或引用 tamkin_evaluating_2023, yin_safeagentbench_2025\n- 核实 navigli_wsd_2009 准确性\n- 补充 Dalpiaz et al. (2018), Willis et al. (2008) in §7, 以及其他建议引用\n\n### Appendix\n- Coreferential 排除理由需更充分解释（mitigation + replication 均排除）\n- 报告 per-type 句长分布\n- C2 within-judge-group 分析\n"
  }
}
```

</details>

---


### Tool result

_source line 901 · 2026-05-21T19:15:51.628608+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4115
}
```

</details>

---


### Assistant

_source line 902 · 2026-05-21T19:16:03.066471+00:00_

审稿报告已投递。

**Round 10 审稿完成**：

- **Overall Score**: 3.5 / 5（Borderline Conference）
- **两位 Reviewer 一致评分**，核心共识：C1（+34pp causal effect）坚实，但 C2（two-tier hierarchy）和 C4（model×type interaction）的 claims 超出统计证据支撑范围
- **2 个 MUST-FIX**：auth scope 52pp 可靠性不足 + hierarchy bootstrap 34.3% 稳定性不足
- **7 个 SHOULD-FIX**：taxonomy 理论讨论、incompleteness confound、DN 过度表述、disambiguation deficit 命名、per-type validation、cross-judge confound、句长分布
- **升分路径**：弱化 claims calibration gap + 补充 robustness checks → 有 4.0（Conference）潜力
- **Issue Tracker 已同步更新**（2 critical, 7 warning, 6 info, 6 resolved）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 83

## Round 83

2 recorded events


### User

_source line 903 · 2026-05-21T19:16:05.591617+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Director。

核心判断：与 R2 在 3 个关键问题上高度一致（authorization scope 低可靠性、two-tier hierarchy 稳定性不足、引用问题）。对 R2-W2（taxonomy 概念混淆）持部分反驳——论文 Section 3 已用操作性定义回应，但确实需要扩展理论边界讨论。R2 的 W3/W4 属于 framing 修正，成本低、价值高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 904 · 2026-05-21T19:16:22.890660+00:00_

审稿报告已投递完成。

**Round 10 审稿总结**：

- **Overall Score**: 3.5（Borderline Conference）
- **两位 Reviewer 评分一致**，核心共识清晰
- **C1（+34pp causal effect）坚实**，是 Conference 水平的贡献
- **主要拖累**：C2 hierarchy 声称过强（bootstrap 34.3%）、auth scope 52pp 不可靠（κ=0.385）、taxonomy 理论讨论不充分
- **升分路径**：弱化 claims calibration gap + 补充 robustness checks → 可达 4.0

报告已通过 `submit_review_report_to_research_director` 投递至 Research Director。Issue Tracker 已同步更新（2 critical, 7 warning, 6 minor/info）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director"
}
```

</details>

---


## Round 84

## Round 84

62 recorded events


### User

_source line 905 · 2026-05-22T08:32:31.100109+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: policy_ambiguity_safety
- 论文路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May cycle
- 截止日期: 2026-06-15
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 906 · 2026-05-22T08:32:36.871325+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 907 · 2026-05-22T08:32:37.022662+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 908 · 2026-05-22T08:32:44.200991+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 909 · 2026-05-22T08:32:44.251657+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 910 · 2026-05-22T08:32:47.969255+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 911 · 2026-05-22T08:32:48.020000+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 912 · 2026-05-22T08:32:51.334070+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
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

_source line 913 · 2026-05-22T08:32:51.435026+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 914 · 2026-05-22T08:32:53.543635+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 915 · 2026-05-22T08:32:53.595563+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 916 · 2026-05-22T08:32:59.468712+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 917 · 2026-05-22T08:33:00.021635+00:00_

{"result":"# 项目 policy_ambiguity_safety 概况\n\n## 实验状态 (17 个)\n\n- **plan_014**: DONE (success) — \n- **plan_015**: DONE (success) — \n- **plan_013**: DONE (success) — \n- **plan_012**: DONE (success) — \n- **plan_011**: DONE (success) — \n- **plan_010**: DONE (success) — \n- **plan_004**: DONE (success) — \n- **plan_003b**: DONE (success) — \n- **plan_003a**: DONE (success) — \n- **plan_002c**: DONE (success) — \n- **plan_006**: DONE (success) — \n- **plan_005**: DONE (success) — \n- **plan_002**: DONE (negative) — \n- **diag_001**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_016** (negative): Type-specific mitigation prompts reduce violations more effectively than generic awareness prompts for their targeted ambiguity types, supporting the practical contribution that type-aware triage is necessary for policy-governed deployments\n- **plan_009** (success): Cross-judge LLM agreement (gpt-5.4 vs gpt-4.1) achieves substantial agreement (weighted κ ≥ 0.60) on violation level classification. LLM-human agreement should be comparable, validating the cross-judge evaluation design.\n  [plan_009_annotation_guidelines](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/annotation_guidelines.md) | [plan_009_annotation_sheet](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet.jsonl) | [plan_009_llm_agreement](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/report/llm_agreement.json) | [plan_009_annotation_sheet_clean](/api/workspace-files/projects/policy_ambiguity_safety/artifacts/plan_009/data/annotation_sheet_clean.jsonl)\n- **plan_014** (success): Expanding perturbation control from n=120 to n=300 will maintain non-significant Δ_perturb (CI containing zero) while narrowing CI upper bound from 13.3pp to ~8pp, strengthening SESOI justification for C
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 918 · 2026-05-22T08:33:00.022503+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
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

_source line 919 · 2026-05-22T08:33:00.022864+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 920 · 2026-05-22T08:33:01.529663+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 921 · 2026-05-22T08:33:01.580326+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 922 · 2026-05-22T08:33:06.599493+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool result

_source line 923 · 2026-05-22T08:33:14.832021+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here's information about EMNLP 2026's call for papers submission guidelines and ARR policy:

## General Submission Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived
…[truncated 1005 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "WebSearch",
  "elapsed_ms": 8232
}
```

</details>

---


### Tool call

_source line 924 · 2026-05-22T08:33:14.983085+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read all paper sections",
  "subagent_type": "Explore",
  "prompt": "Read the following files completely and return their FULL content (every line). These are sections of an academic paper. I need the complete text of each file, not summaries.\n\nFiles to read:\n1. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex\n2. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex\n3. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex\n4. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex\n5. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex\n6. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex\n7. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex\n8. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex\n9. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex\n10. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex\n11. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex\n12. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib\n\nReturn the FULL content of each file, clearly labeled with the filename. Do not summarize or truncate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Read all paper sections",
    "subagent_type": "Explore",
    "prompt": "Read the following files completely and return their FULL content (every line). These are sections of an academic paper. I need the complete text of each file, not summaries.\n\nFiles to read:\n1. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex\n2. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex\n3. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex\n4. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex\n5. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex\n6. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex\n7. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex\n8. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex\n9. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex\n10. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex\n11. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex\n12. /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib\n\nReturn the FULL content of each file, clearly labeled with the filename. Do not summarize or truncate."
  }
}
```

</details>

---


### Tool call

_source line 925 · 2026-05-22T08:33:15.334798+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 926 · 2026-05-22T08:33:15.385657+00:00_

1	## Round 10 (Fresh) Review Issues — policy_ambiguity_safety
2	## Paper: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
3	## Venue: EMNLP 2026 via ARR May cycle
4	## Date: 2026-05-21
5	## Round 10 Score: 3.5 (Borderline Conference)
6	## Note: Fresh review session — all issues re-evaluated from scratch
7	
8	# ============================================================
9	# CRITICAL ISSUES
10	# ============================================================
11	
12	- id: "R10-C1"
13	  summary: "Authorization scope κ=0.385 不足以支撑 C4 中 52pp range 作为核心发现"
14	  category: method
15	  severity: critical
16	  status: open
17	  first_raised_round: 8
18	  last_seen_round: 10
19	  mentions:
20	    - round: 9
21	      reviewers: [R1, R2]
22	      note: "R9-N4. Abstract/Introduction 表述与正文 suggestive hedging 不匹配。"
23	    - round: 10
24	      reviewers: [R1, R2]
25	      note: "R1 MUST-FIX, R2 SHOULD-FIX. 两人完全共识: κ=0.385 低于 fair agreement 门槛(0.40), 52pp 中真实差异 vs noise 无法分离。Abstract 括号注释太弱, Introduction 复述 52pp 无 caveat。R1 建议展示去除 auth scope 后 C4 是否仍显著。"
26	  action_items:
27	    - round: 9
28	      action: "Abstract 52pp 加 measurement uncertainty; §1 对齐 suggestive; §5.4 F-test 补 denominator df"
29	      assigned_to: agent
30	      status: in_progress
31	    - round: 10
32	      action: "(1) Abstract 将 auth scope 从主要发现降格为初步发现; (2) Introduction 同等篇幅讨论可靠性限制; (3) C4 分析展示去除 auth scope 后交互效应是否仍显著; (4) 52pp 标记为 upper bound with substantial measurement uncertainty"
33	      assigned_to: agent
34	      status: open
35	  resolution: ""
36	  resolution_round: null
37	
38	- id: "R10-C2"
39	  summary: "Two-tier hierarchy (C2) bootstrap 仅 34.3% 支持, 声称强于证据"
40	  category: method
41	  severity: critical
42	  status: open
43	  first_raised_round: 8
44	  last_seen_round: 10
45	  mentions:
46	    - round: 9
47	      reviewers: [R1, R2]
48	      note: "R9-N3. SESOI ±15pp 缺乏外部锚定, two-tier 在 ±10-12pp 时不稳健。"
49	    - round: 10
50	      reviewers: [R1, R2]
51	      note: "R2 MUS
…[truncated 13581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 927 · 2026-05-22T08:33:16.992214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 928 · 2026-05-22T08:33:17.144352+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type ambiguity taxonomy, evaluated across five models (2,997 episodes). Three findings emerge. First, ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. Second, incompleteness consistently ranks highest (46--62\% across seven models); the remaining five types show a risk gradient rather than sharp tiers. Third, error analysis of 614 violation traces reveals \emph{Disambiguation Neglect} ($\leq$11\% awareness) and \emph{systematic nocuity}---41.3\% of clauses triggering model-convergent violations---indicating clause-level rather than model-level risk factors. These results motivate type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 929 · 2026-05-22T08:33:17.195099+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---
