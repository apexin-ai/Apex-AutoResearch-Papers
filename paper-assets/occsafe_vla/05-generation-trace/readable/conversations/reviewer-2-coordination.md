# Reviewer 2 coordination

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 184
- **Recorded user turns:** 4
- **Tool calls:** 88
- **Original source:** `logs/chats/feishu_group_oc_faa96524df7d6444f5c8cbc48d5a616b_reviewer_2.jsonl`
- **Structured JSON:** [`0620f9e9dbca61385021.json`](../../sessions/06/0620f9e9dbca61385021.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

92 recorded events

### User

_source line 1 · 2026-05-28T10:46:45.499540+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 写作质量 + 完整性**。

## Venue 信息
- **目标会议**: CoRL 2026
- **Deadline**: 2026-05-29
- **页数限制**: 8 页正文 + 无限参考文献
- **模板**: PMLR (corl_2026.sty)
- **匿名规则**: Double-blind
- **必须包含**: Limitations section（计入 8 页）

## 论文路径
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/submitted.pdf`

## 审查侧重

### 核心任务：验证上轮 resolved issue 是否确实修复

以下 issue 上轮标记为 resolved，请抽查确认：
- **R1-W5 [resolved]**: Table 1 Random OCC placement 位置/呈现 — 按 gradient flow 因子分组，检查是否逻辑清晰
- **R1-W6 [resolved]**: Appendix 'Detach worst' 表述 — 检查是否明确标注为 v1 scope
- **R1-W13 [resolved]**: Discussion 中 BN/CKA 分析矛盾 — 检查 CKA 定位 optimization dynamics 是否自洽
- **R1-W21 [resolved]**: Introduction overclaim — 检查当前版本措辞是否准确

对每条标注 [CONFIRMED_RESOLVED] 或 [REGRESSION] + 理由。

### 新颖性审查
1. "Normalization-dependent gradient flow effect" 作为核心贡献的新颖性评估
2. 与 PCGrad/CAGrad/GradNorm 等 MTL 方法的关系是否充分讨论？
3. 这是一个 **负面结果** 论文（spatial supervision 不提升安全性）——CoRL 社区对此类结果的接受度如何？
4. Factorial design 在 VLA 领域的方法论贡献是否足够？

### 写作质量审查
1. Abstract 是否准确概括核心发现？是否有 overclaim？
2. Introduction 的 narrative flow：问题动机 → gap → 方法 → 发现是否清晰？
3. Contribution list 是否与实际结果匹配？
4. Discussion 与 Conclusion 是否有冗余或矛盾？
5. Appendix 组织是否合理？是否有应在正文的内容被放到 appendix？
6. 参考文献格式是否一致？是否有遗漏的关键 related work？

### Related Work 覆盖
1. Spatial VLA 方法覆盖是否全面？（SpatialVLA, DepthVLA, OccVLA, PointVLA 等）
2. VLA Safety 方法覆盖是否全面？（VLSA, Co-FreeVLA, SafeVLA 等）
3. MTL/gradient conflict 文献是否充分？
4. BN/LN 规范化文献是否充分？
5. 是否遗漏 2025-2026 年的重要新工作？

### 格式检查
1. CoRL 2026 模板是否正确使用？
2. 正文是否 ≤ 8 页？
3. 匿名性：是否有去匿名化线索？
4. Limitations section 是否存在且充实？

请按 CoRL 标准严格评审，输出格式：Summary → Strengths → Weaknesses (逐条编号 W1, W2, ...) → Questions → Missing References。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-28T10:46:54.279557+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-28T10:46:55.797910+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/.claude/sessions/review_reviewer_2_59f1dca7.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1518
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-28T10:46:55.952597+00:00_

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
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
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

_source line 5 · 2026-05-28T10:46:55.977750+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 25
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-28T10:47:00.460741+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T10:47:02.574785+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/submitted.pdf",
  "project": "occsafe_vla",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/submitted.pdf",
    "project": "occsafe_vla",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T10:47:08.288013+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"}]

Based on the search results, I found information about CoRL 2026 reviewer requirements and some review guidelines:

## CoRL 2026 Reviewer Requirements

All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal. Additionally, every author with 3 or more submissions must agree to serve as a reviewer.

## Review Criteria and Guidelines

While I found detailed reviewer guidelines for CoRL 2023, the specific 2026 review form criteria were not fully available in the search results. However, based on CoRL 2023 guidelines, reviewers assess papers on:

- Relevance: Whether the paper addresses a problem in robot learning, applies or improves a learning-based method or learned model, whether the method is evaluated in simulation, on real robots, or both, and whether the CoRL audience would be interested in reading the paper

- CoRL papers are required to include a limitati
…[truncated 540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7827
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-28T10:47:09.845057+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 318.7}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 370.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 378.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 362.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 357.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 349.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 262.0}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 400.7}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p9.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 328.3}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_v
…[truncated 339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7270
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-28T10:47:17.373937+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scales for CoRL reviewer guidelines. Include all evaluation dimensions (soundness, significance, novelty, clarity, etc.) with their rating scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scales for CoRL reviewer guidelines. Include all evaluation dimensions (soundness, significance, novelty, clarity, etc.) with their rating scales."
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-28T10:47:18.688019+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, scoring dimensions, rating scales, and evaluation guidelines for CoRL 2024 reviewers. Include all dimensions like soundness, significance, novelty, clarity, overall score, confidence, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, scoring dimensions, rating scales, and evaluation guidelines for CoRL 2024 reviewers. Include all dimensions like soundness, significance, novelty, clarity, overall score, confidence, etc."
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-28T10:47:19.194846+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T10:47:19.797914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T10:47:20.303507+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1108
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T10:47:20.308696+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T10:47:20.912790+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1114
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T10:47:20.913198+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T10:47:21.118158+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 809
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T10:47:21.471937+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 558
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T10:47:23.027734+00:00_

# CoRL 2023 Reviewer Guidelines: Evaluation Criteria

Based on the provided content, CoRL uses a **six-dimensional evaluation framework** rather than traditional numeric rating scales. The guidelines specify these assessment areas:

## Evaluation Dimensions

1. **Originality**: Assessment of novelty in problems, methods, or combinations thereof, with attention to differentiation from prior work and citation completeness.

2. **Quality**: Evaluation of technical soundness, claim support through theory or experiments, methodological appropriateness, work completeness, and author honesty about strengths/weaknesses.

3. **Clarity**: Assessment of writing quality, organization, informativeness, and whether sufficient detail exists "for an expert reader to reproduce its results."

4. **Significance**: Determination of result importance, potential adoption by researchers/practitioners, advancement over prior work, and theoretical/experimental uniqueness.

5. **Relevance**: Evaluation of applicability to robot learning, learning-based methods, simulation/real robot evaluation, and audience interest.

6. **Limitations**: Appraisal of honestly reported limitations with appreciation, while identifying unreported shortcomings.

## Key Note

The document does **not specify explicit numeric rating scales**. Instead, it emphasizes writing constructive, evidence-based reviews with concrete suggestions and citations. The guidelines reference ICML and NeurIPS resources for additional reviewer instruction frameworks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5653
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-28T10:47:23.028237+00:00_

# CoRL 2024 Review Criteria Summary

Based on the provided webpage content, CoRL 2024 does **not include a detailed review form with specific scoring dimensions or rating scales**. 

The available guidance states that submissions will be evaluated on:

1. **Significance and Novelty** - "significance and novelty of the results, either theoretical or empirical"

2. **Validation** - "degree to which they have been objectively established and/or their potential for scientific and technological impact"

3. **Relevance** - applicability to robotic learning

## Key Requirement

All papers must demonstrate relevance to robot learning through either:
- **Intent**: "Explicitly address a learning question for physical robots" OR
- **Outcome**: "Test the proposed learning solution on physical robots"

## What's Missing

The document does not provide:
- Specific numerical rating scales
- Individual scoring dimensions (soundness, clarity, etc.)
- Confidence levels or other standard review metrics
- A complete review form template

**Note**: The webpage indicates this is an instruction page for reviewers, but it appears to focus on desk rejection criteria and reviewer qualifications rather than the detailed review rubric itself.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4340
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-28T10:47:29.899885+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-28T10:47:30.468821+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-28T10:47:30.925784+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1025
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-28T10:47:30.926405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-28T10:47:31.483836+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-28T10:47:32.292084+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1823
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-28T10:47:32.295012+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1368
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-28T10:47:32.295534+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-28T10:47:33.250487+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1766
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-28T10:47:33.252409+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-28T10:47:33.252967+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-28T10:47:33.756127+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-28T10:47:34.358527+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/submitted.pdf",
  "project": "occsafe_vla",
  "pages": "11-19",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/submitted.pdf",
    "project": "occsafe_vla",
    "pages": "11-19",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-28T10:47:35.255944+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p11.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 332.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p12.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 55.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p13.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 313.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p14.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 321.8}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p15.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 316.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p16.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 292.8}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p17.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 313.4}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p18.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 272.5}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p19.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 96.1}], \"total_pages\": 19, \"rendered_pages\": 9, \"dpi\": 150, \"output_dir\": 
…[truncated 146 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 897
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-28T10:47:40.373903+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-28T10:47:41.180289+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-28T10:47:41.381310+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-28T10:47:41.683316+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-28T10:47:41.834270+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-28T10:47:42.188455+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-28T10:47:42.645115+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 810
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-28T10:47:42.647557+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 459
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-28T10:47:42.647950+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-28T10:47:43.156357+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 508
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-28T10:47:43.156966+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-28T10:47:43.562372+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-28T10:47:50.188840+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-28T10:47:51.045169+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-28T10:47:51.045640+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-28T10:47:51.548679+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-28T10:47:51.549080+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-28T10:47:52.001981+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-28T10:47:52.002326+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-28T10:47:52.052886+00:00_

1	% OccSafe-VLA: Occupancy-Aware Safety for Vision-Language-Action Models
2	% Target: CoRL 2026
3	\documentclass{article}
4	
5	\usepackage[dvipsnames]{xcolor}
6	\usepackage{corl_2026}
7	
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb}
10	\usepackage{booktabs}
11	\usepackage{enumitem}
12	\usepackage{subcaption}
13	\usepackage{placeins}
14	
15	\title{Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer?\\ An Empirical Investigation}
16	
17	\author{
18	Anonymous Author(s)
19	}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	Fine-tuned Vision-Language-Action (VLA) models can achieve high task success yet remain behaviorally unsafe, with collision avoidance rates lagging task completion on safety-critical benchmarks.
26	We present a factorial study of twelve conditions varying five factors (gradient flow, label content, normalization type, spatial reference frame, and temporal extent) to isolate how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance.
27	Our central finding is a \textbf{normalization-dependent gradient flow effect}. Under Batch Normalization (BN), gradient flow degrades safety: Full OCC BN achieves a 0.725 Collision Avoidance Rate versus 0.767 for Detach BN (Cohen's $d = -0.93$, large), falling below the no-auxiliary-head Vanilla baseline (0.745). Under Layer Normalization (LN), gradient flow is benign: Full OCC LN reaches 0.773, above Vanilla (Cohen's $d = +1.07$, large). Two main effects drive this pattern: (1)~gradient flow under BN reduces CAR by 4.2\,pp ($d{=}0.93$), with BN + gradient flow as the sole configuration falling below the Vanilla baseline; (2)~LN provides a consistent 3.5--4.8\,pp safety advantage over BN ($d{\approx}1.05$--$1.47$, large to very large), regardless of gradient flow. A $2{\times}2$ ANOVA confirms additive main effects with negligible interaction ($\eta^2{<}0.01$). The BN + gradient flow cell is both the worst-performing and most unstable configurat
…[truncated 1213 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-28T10:47:58.932742+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-28T10:47:59.451016+00:00_

1	\section{Introduction}
2	
3	Vision-language-action (VLA) models map visual observations and language instructions to robot actions, and recent fine-tuning recipes achieve high task success on standard manipulation benchmarks~\cite{brohan2023rt2, kim2024openvla, kim2025oft}. Behavioral safety, however, does not follow from task completion. On SafeLIBERO Level~I~\cite{hu2025vlsa}, OpenVLA-7B fine-tuned with the OFT recipe~\cite{kim2025oft} reaches a Task Success Rate (TSR) of 87.8\% but a Collision Avoidance Rate (CAR) of only 74.5\%. On the three most constrained tasks, collision rates reach 43--93\%. These numbers expose a gap between what training objectives optimize for and what safe deployment requires: the robot completes the task but fails to avoid contact with surrounding objects. Identifying which fine-tuning design choices affect collision avoidance is a prerequisite for closing this gap.
4	
5	Two active research threads address related but distinct aspects of this problem. The first enriches VLA models with auxiliary spatial prediction (occupancy grids, depth maps, point clouds) to inject 3D geometric structure into vision encoders~\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla, liu2025occvla}. At least fifteen such methods have appeared in the past year~\cite{wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2025pointvla, sun2025geovla, bhat20253dcavla, li2025qdepthvla, abouzeid2025geoaware, rao2026augvla3d, li2026corridorvla}, all reporting improved task success. The implicit assumption in this literature is that better spatial awareness should also yield safer behavior, since the robot ``knows where things are.'' The second thread targets VLA safety directly through runtime action filtering~\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf} or constrained reinforcement learning~\cite{zhang2025safevla}. These two lines of work are disconnected: no spatial method evaluates its effect on collision avoidance, and no safety meth
…[truncated 4933 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 518
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-28T10:47:59.451539+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-28T10:48:00.164781+00:00_

1	
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	BatchNorm is not inherently harmful: Detach OCC (BN, gradient OFF) matches or slightly exceeds Vanilla (0.767 vs.\ 0.745, $p{=}0.28$). The damage is BN-specific: under BatchNorm, gradient flow drops CAR below the Vanilla baseline (0.725 vs.\ 0.745, $d{=}{-}0.93$), while under LayerNorm, gradient flow is benign (0.773 vs.\ 0.745, $d{=}{+}1.07$). Both normalization rows show within-row deficits from gradient flow ($-$4.2\,pp for BN, $-$2.9\,pp for LN), but only the BN row falls below the no-auxiliary baseline. CKA analysis confirms that encoder representations remain intact under all conditions (CKA $\geq$ 0.95 for both DINOv2 and SigLIP), ruling out representational drift and localizing the effect to optimization dynamics. The BN + gradient flow cell is both the worst-performing and the most unstable configuration ($\sigma{=}0.064$, ${\geq}\,2{\times}$ all other cells). We hypothesize that BatchNorm's running statistics introduce sensitivity to distributional shifts from auxiliary gradients, a coupling absent in LayerNorm's per-token computation. The numerical advantage of Detach OCC ($+$2.2\,pp, with 3 of 4 seeds exceeding the Vanilla mean) raises the possibility that detached auxiliary heads provide a mild regularization benefit, though larger samples are needed to confirm.
6	
7	\textbf{Normalization independently affects safety.} LN provides a consistent safety advantage over BN ($+$4.8\,pp under gradient flow, $d{=}1.05$; $+$3.5\,pp without), comparable in magnitude to the gradient flow effect. For practitioners who must retain gradient flow, LayerNorm converts the BN safety deficit into a gain, an architectural advantage, since label content does not detectably affect outcomes.
8	
9	\textbf{Additive protection model.} Cell~1 (BN + gradient flow) is the only factorial cell below Vanilla, confirming that safety degradation requires the joint presence of BatchNorm and gradient flow in this setting; removing ei
…[truncated 3161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 713
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-28T10:48:00.270689+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-28T10:48:00.271146+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-28T10:48:00.321797+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Main Results}
6	
7	Table~\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\times$ 10 tasks per seed). $\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\star$) uses v1 code but is included above the midrule as a factorial control; its $\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use permutation tests and Cohen's $d$ against the Vanilla baseline.
8	
9	\textbf{Gradient flow interacts with normalization type.} The four factorial cells reveal a normalization-dependent pattern. Under BatchNorm, gradient flow degrades safety: Full OCC (BN, gradient ON) is the worst-performing cell (CAR $0.725$, $\Delta{=}-2.0$\,pp vs.\ Vanilla) and the sole configuration falling below baseline, while Detach OCC (gradient OFF) exceeds it ($0.767$, $\Delta{=}+2.2$\,pp). Under LayerNorm, gradient flow is benign: Full OCC+LN ($0.773$, $\Delta{=}+2.8$\,pp) already exceeds Vanilla, and Detach+LN ($0.802 \pm 0.024$, $n{=}3$) yields the highest cell mean ($\Delta{=}+5.7$\,pp). Both LN cells exceed the Vanilla baseline, whereas only the gradient-OFF BN cell does so. The BN + gradient flow cell also exhibits the highest instability ($\sigma{=}0.064$, ${\geq}\,2{\times}$ all other cells). Spatial label content does not detectably affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$, observed under v1 codebase for Random OCC and Depth).
10	
11	\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell ($\sigma{=}0.064$, ${\geq}\,2{\times}$ that of all other cells; $\sigma \leq 0.027$ for all other cells): individual seeds range from $0.776$
…[truncated 7139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-28T10:48:00.322556+00:00_

1	
2	\section{Extended Per-Task Results}
3	\label{app:per_task}
4	
5	Table~\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.
6	
7	\begin{table}[h]
8	\centering
9	\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}
10	\label{tab:per_task}
11	\begin{tabular}{clccccccc}
12	\toprule
13	 & & \multicolumn{7}{c}{Mean CAR by Condition} \\
14	\cmidrule(lr){3-9}
15	Task & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\
16	\midrule
17	T0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\
18	T1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\
19	T2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\
20	T3 & Hard  & 0.38 & 0.37 & 0.31 & \textbf{0.11} & 0.44 & 0.50 & 0.55 \\
21	T4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\
22	T5 & Hard  & 0.07 & 0.17 & 0.23 & \textbf{0.05} & 0.12 & 0.08 & 0.04 \\
23	T6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\
24	T7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\
25	T8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\
26	T9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\
27	\midrule
28	\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\
29	\bottomrule
30	\end{tabular}
31	\end{table}
32	
33	\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\geq$ 0.89, leaving minimal room for au
…[truncated 19306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-28T10:48:06.182993+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-28T10:48:06.635988+00:00_

1	
2	\section{Related Work}
3	
4	\subsection{VLA Safety and Spatial Representations}
5	
6	Vision-language-action models achieve high task success but remain collision-prone~\cite{li2026vlasafety}. Existing safety approaches filter actions via control barrier functions or embed constraints during training~\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf, zhang2025safevla}; none examines whether spatial representations contribute to safety. A parallel line enriches VLAs with 3D structure (depth fusion, representation alignment, geometric encoding, or occupancy prediction)~\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware, yang2024depthanything, li2026spatialforcing, wu2025spatialvla, li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla, liu2025occvla, li2022bevformer, sima2023occnet, tian2023occ3d}, yet none evaluates collision avoidance. The occupancy branch of this line originated in autonomous driving: BEVFormer~\cite{li2022bevformer} introduced transformer-based bird's-eye-view estimation, and subsequent work formalized dense 3D occupancy as a unified scene representation~\cite{sima2023occnet, tian2023occ3d}. OccVLA~\cite{liu2025occvla} adapted this concept to robotics by supervising a VLA with implicit occupancy targets; our BEV occupancy auxiliary head follows the same principle but serves as a controlled experimental factor to isolate the safety effect of spatial supervision. SpatialVLA~\cite{wu2025spatialvla}, DepthVLA~\cite{yuan2025depthvla}, and OccVLA all report task success improvements from spatial auxiliary supervision but do not include safety metrics. The assumption that spatial awareness should improve safety because the robot ``knows where things are'' remains untested; we address this gap by directly measuring collision avoidance under controlled spatial supervision conditions.
7	
8	\subsection{Auxiliary Tasks and Multi-Task Gradient Dynamics}
9	

…[truncated 2412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-28T10:48:06.787265+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-28T10:48:07.038656+00:00_

1	
2	\section{Method}
3	
4	We fine-tune OpenVLA-7B~\cite{kim2024openvla} with the OFT recipe~\cite{kim2025oft}, which concatenates DINOv2~\cite{oquab2024dinov2} (1024-d) and SigLIP~\cite{zhai2023siglip} (1152-d) patch features into a 2176-dimensional representation per spatial token. We apply LoRA~\cite{hu2022lora} (rank 32, $\alpha{=}16$) and augment the action prediction loss with an auxiliary spatial prediction head:
5	\begin{equation}
6	\mathcal{L}_\text{total} = \mathcal{L}_\text{action} + \lambda(t) \cdot \mathcal{L}_\text{aux}(h(\phi_v(o_t)), s_t^*),
7	\quad \lambda(t) = 0.01 \cdot \exp(-t / 50000)
8	\end{equation}
9	where $h$ denotes the auxiliary head, $\phi_v$ the frozen-then-LoRA-adapted vision encoders, and $s_t^*$ the ground-truth spatial label at step $t$. The coefficient $\lambda(t)$ decays exponentially so that spatial gradients shape early representations without dominating late-stage action refinement. The auxiliary head is discarded at inference, incurring zero additional cost.
10	
11	\textbf{Bird's-eye view (BEV) occupancy head.} The head (1.2M parameters) maps the 256 patch tokens from the current observation frame to a $64{\times}64$ binary occupancy grid. A linear projection ($2176{\to}256$) is reshaped to $16{\times}16$, followed by two transposed convolutions ($256{\to}128{\to}64$, kernel 4, stride 2) each with BatchNorm2d and GELU, and a final $1{\times}1$ convolution with sigmoid activation. Ground-truth grids are rendered from MuJoCo simulator state replay by projecting object bounding boxes onto the table-plane BEV. Training uses focal loss~\cite{lin2017focal} ($\alpha{=}0.25$, $\gamma{=}2.0$) to handle class imbalance in the sparse occupancy signal. The initial auxiliary weight $\lambda_0{=}0.01$ is set to keep auxiliary gradients below 2\% of the action loss magnitude, avoiding interference with action learning.
12	
13	\textbf{Monocular depth head.} This head shares the same convolutional architecture but replaces the sigmoid with ReLU
…[truncated 4181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-28T10:48:07.089298+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-28T10:48:07.241826+00:00_

1	
2	\section{Conclusion}
3	
4	We presented a systematic factorial study of auxiliary spatial supervision during VLA fine-tuning. A $2{\times}2$ factorial reveals two large main effects: gradient flow under BatchNorm degrades collision avoidance below the Vanilla baseline ($d{=}{-}0.93$) and produces the highest training instability ($\sigma{=}0.064$); LayerNorm provides a consistent 3.5--4.8\,pp safety advantage ($d{\approx}1.05$). Only the BN + gradient flow combination harms safety; spatial label content showed no detectable effect. Practitioners should omit auxiliary spatial heads or, if required, use detached gradients with LayerNorm; avoid combining BatchNorm with gradient flow. CKA analysis localizes the degradation to optimization dynamics rather than representational capacity (CKA $\geq$ 0.95). Training-time collision avoidance may instead require approaches that directly encode safety constraints~\cite{zhang2025safevla}.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-28T10:48:13.416099+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-28T10:48:13.868230+00:00_

1	% References for OccSafe-VLA
2	% Bib key convention: {first_author_surname_lower}{year}{keyword_lower}
3	
4	% ============================================================
5	% VLA Safety
6	% ============================================================
7	
8	@article{hu2025vlsa,
9	  author    = {Songqiao Hu and Zeyi Liu and Shuang Liu and Jun Cen and Zihan Meng and Xiao He},
10	  title     = {{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},
11	  journal   = {arXiv preprint arXiv:2512.11891},
12	  year      = {2025},
13	  note      = {arXiv:2512.11891}
14	}
15	
16	@inproceedings{zhang2025safevla,
17	  author    = {Borong Zhang and others},
18	  title     = {{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},
19	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
20	  year      = {2025},
21	  note      = {Spotlight. arXiv:2503.03480}
22	}
23	
24	@article{zhai2026cofreevla,
25	  author    = {Xuanran Zhai and others},
26	  title     = {{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via {VLA} Model and Risk Estimation},
27	  journal   = {arXiv preprint arXiv:2601.21712},
28	  year      = {2026},
29	  note      = {arXiv:2601.21712}
30	}
31	
32	
33	@article{li2026vlasafety,
34	  author    = {Qi Li and others},
35	  title     = {Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},
36	  journal   = {arXiv preprint arXiv:2604.23775},
37	  year      = {2026},
38	  note      = {arXiv:2604.23775}
39	}
40	
41	% ============================================================
42	% Safety Mechanisms (barrier functions / occupancy-based safety)
43	% ============================================================
44	
45	
46	@article{raja2024ogmcbf,
47	  author    = {Golnaz Raja and Teemu M{\"o}kk{\"o}nen and Reza Ghabcheloo},
48	  title     = {Safe Robot Control using Occupancy Grid Map-based Control Barrier Function ({OGM-CBF})},
49	  journal   = {arXiv prepr
…[truncated 16600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-28T10:48:13.868703+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 review form scoring dimensions rating scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 review form scoring dimensions rating scale"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-28T10:48:19.942403+00:00_

Web search results for query: "CoRL 2026 review form scoring dimensions rating scale"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"ICLR 2026 Scores Released: Reviewers Call It \"Crazy\", DeepMind Researchers Show Comeback from Desperate Situation","url":"https://eu.36kr.com/en/p/3551362253731718"},{"title":"Can Small and Reasoning Large Language Models Score Journal Articles for Research Quality and Do Averaging and Few-shot Help?","url":"https://arxiv.org/pdf/2510.22389"},{"title":"Phase 3 Randomized, Double-Blind, Placebo-Controlled Study to Evaluate Sialic Acid in Patients With Glucosamine (UDP-N-acetyl)-2-epimerase Myopathy (GNEM) or Hereditary Inclusion Body Myopathy (HIBM)","url":"https://cdn.clinicaltrials.gov/large-docs/21/NCT02377921/SAP_001.pdf"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"}]

Based on my search results, I found some information about CoRL 2026's review process, though specific details about the complete review form scoring dimensions and rating scale are limited in the publicly available sources.

From the official CoRL 2026 instructions, papers that do not receive at least one score of weak accept or above from either a reviewer or the Area Chair will be candidates for first-round rejection without rebuttal. This indicates that the review scoring system includes categories like "weak accept," suggesting an ordinal scale system, though the full details of all scoring dimensions aren't explicitly provided in the search results.

The most detailed information about the review process appears to be available through
…[truncated 590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6073
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-28T10:48:38.302956+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference",
  "prompt": "Extract all review form criteria, scoring dimensions, rating scales, and reviewer evaluation guidelines for CoRL 2026. Look for dimensions like soundness, significance, novelty, clarity, overall recommendation, confidence level, etc. Include all rating scale options."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference",
    "prompt": "Extract all review form criteria, scoring dimensions, rating scales, and reviewer evaluation guidelines for CoRL 2026. Look for dimensions like soundness, significance, novelty, clarity, overall recommendation, confidence level, etc. Include all rating scale options."
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-28T10:48:40.862317+00:00_

# CoRL 2026 Review Form Criteria

Based on the provided web page content, I cannot extract the specific review form criteria, scoring dimensions, rating scales, or reviewer evaluation guidelines for CoRL 2026.

The page shown contains only navigation elements, footer information, and general site structure for OpenReview.net. It does not include the actual conference review form details, evaluation rubrics, or scoring systems that would be needed to answer your question.

To locate this information, you would need to:
- Access the CoRL 2026 conference page directly on OpenReview
- Review the "Call for Papers" or submission guidelines
- Check the reviewer instructions section of the conference venue

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 2559
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-28T10:48:45.041892+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2024 2025 openreview review form \"overall score\" \"soundness\" \"presentation\" rating scale 1-5 1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2024 2025 openreview review form \"overall score\" \"soundness\" \"presentation\" rating scale 1-5 1-10"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-28T10:49:01.354264+00:00_

Web search results for query: "CoRL 2024 2025 openreview review form "overall score" "soundness" "presentation" rating scale 1-5 1-10"

Links: [{"title":"Insights from the ICLR Peer Review and Rebuttal Process","url":"https://arxiv.org/pdf/2511.15462"},{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"ICML 2024 Reviewer Instructions","url":"https://icml.cc/Conferences/2024/ReviewerInstructions"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review","url":"https://arxiv.org/pdf/2509.25701"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"}]

I found some information about peer review forms from various conferences, but the search results don't contain specific details about the CoRL 2024 or 2025 review form rating scales. The OpenReview pages for both CoRL 2024 and CoRL 2025 appeared in the results but didn't provide the detailed review form information.

Let me search more specifically for CoRL review form details:

Links: [{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"CoRL 2025 Workshop Robot Data | OpenReview","url":"https:/
…[truncated 4313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 16312
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-28T10:49:07.247800+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete review form criteria, all scoring dimensions with their rating scales, and all evaluation questions that reviewers must answer. Include any numerical ratings, categories like soundness/novelty/clarity/significance, and the overall recommendation scale."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete review form criteria, all scoring dimensions with their rating scales, and all evaluation questions that reviewers must answer. Include any numerical ratings, categories like soundness/novelty/clarity/significance, and the overall recommendation scale."
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-28T10:49:11.463467+00:00_

# CoRL 2023 Reviewer Evaluation Criteria

Based on the provided guidelines, the review form addresses these key dimensions:

## Primary Evaluation Categories

The guidelines specify six main criteria reviewers must assess:

1. **Originality** - Whether problems/methods are novel or represent valuable combinations of existing techniques
2. **Quality** - Technical soundness and empirical/theoretical support for claims
3. **Clarity** - Writing quality, organization, and reproducibility of results
4. **Significance** - Importance of results and potential impact on the field
5. **Relevance** - Connection to robot learning and CoRL audience interest
6. **Limitations** - Honest acknowledgment of work constraints

## Additional Guidance

The document emphasizes that reviewers must write a "Summary of Paper" section restating contributions in their own words, followed by "Main Review" evaluating the six dimensions above.

**Note:** The provided content does not include specific numerical rating scales (e.g., 1-5 or 1-10), overall recommendation categories (e.g., Accept/Reject/Borderline), or a complete review form template. These details may exist in the full OpenReview submission system but are not detailed in this webpage excerpt.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4215
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-28T10:49:14.976604+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:openreview.net CoRL 2024 \"overall\" \"soundness\" \"presentation\" \"confidence\" review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:openreview.net CoRL 2024 \"overall\" \"soundness\" \"presentation\" \"confidence\" review"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-28T10:49:20.294791+00:00_

Web search results for query: "site:openreview.net CoRL 2024 "overall" "soundness" "presentation" "confidence" review"

Links: [{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"Insights from the ICLR Peer Review and Rebuttal Process","url":"https://arxiv.org/pdf/2511.15462"},{"title":"Paper Copilot: Tracking the Evolution of Peer Review in AI Conferences","url":"https://arxiv.org/html/2510.13201v1"},{"title":"ICML 2024 Reviewer Instructions","url":"https://icml.cc/Conferences/2024/ReviewerInstructions"},{"title":"OpenReviewer: A Specialized Large Language Model for Generating Critical Scientific Paper Reviews","url":"https://arxiv.org/html/2412.11948v3"},{"title":"CoRL 2024 Conference Submissions | OpenReview","url":"https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference"},{"title":"CoRL 2024 Workshop MRM-D Submissions","url":"https://openreview.net/submissions?page=2&venue=robot-learning.org/CoRL/2024/Workshop/MRM-D"},{"title":"What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review","url":"https://arxiv.org/pdf/2509.25701"}]

I found relevant information about CoRL 2024 on OpenReview. The search results show that CoRL 2024 Conference submissions are available on OpenReview with publication dates starting from September 5, 2024.

However, the search results don't provide detailed information about the specific review criteria you mentioned (overall, soundness, presentation, confidence). The results do show that these are standard review metrics used across ML conferences—for example, numerical scores are provided for soundness, presentation, contribution, confidence, and overall rating at ICLR.

To access the actual CoRL 2024 reviews with these specific metrics on OpenReview, you would need to visit the CoRL 2024 Conference
…[truncated 229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5318
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-28T10:49:24.658511+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference",
  "prompt": "Find any paper submission ID or URL for a CoRL 2024 paper that has reviews. I need to see the review form format including scoring dimensions and scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference",
    "prompt": "Find any paper submission ID or URL for a CoRL 2024 paper that has reviews. I need to see the review form format including scoring dimensions and scales."
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-28T10:49:28.441928+00:00_

Based on the webpage content provided, I cannot identify any paper submission that explicitly shows review form formats or scoring dimensions. The page lists 30 CoRL 2024 submissions with titles, authors, and publication dates, but doesn't display review information or assessment rubrics.

To access review details and scoring formats, you would need to:

1. Click on an individual paper link (e.g., the "Body Transformer" submission at `/forum?id=Oce2215aJE`)
2. Navigate to that paper's discussion forum page where reviews are typically posted

The current listing page only shows metadata about submissions themselves, not the review process or evaluation criteria used by CoRL 2024.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 3783
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-28T10:49:32.207639+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/forum?id=Oce2215aJE",
  "prompt": "Extract the review form dimensions and rating scales used by CoRL 2024 reviewers. Look for scoring fields like overall, soundness, presentation, contribution, confidence, etc. with their numerical scales (e.g., 1-5, 1-10). Show me the exact structure of the review form."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/forum?id=Oce2215aJE",
    "prompt": "Extract the review form dimensions and rating scales used by CoRL 2024 reviewers. Look for scoring fields like overall, soundness, presentation, contribution, confidence, etc. with their numerical scales (e.g., 1-5, 1-10). Show me the exact structure of the review form."
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-28T10:49:35.269574+00:00_

Based on the provided web page content, I cannot extract the review form dimensions and rating scales used by CoRL 2024 reviewers.

The page displays a paper abstract and metadata for "Body Transformer: Leveraging Robot Embodiment for Policy Learning," but it does not contain information about the conference's review form structure, scoring fields, or numerical rating scales.

To locate this information, you would need to access:
- The CoRL 2024 conference submission guidelines
- The actual review form template
- The conference's reviewer instructions page

These details are typically found in conference submission portals or author/reviewer guidelines rather than individual paper landing pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 3061
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-28T10:55:02.521970+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审查报告：Novelty + Writing Quality + Completeness\n\n## 上轮 Resolved Issue 抽查\n\n**R1-W5 [CONFIRMED_RESOLVED]**: Table 2（Main Results）已按 v2 factorial core 和 v1 supplementary 分区呈现，Random OCC 放在 midrule 以下的 supplementary 区域并标注 ★v1 code，ΔCAR 因 cross-codebase mismatch 标注为 \"---\"。Table 1（Ablation Design）按比较对分组，逻辑清晰。\n\n**R1-W6 [CONFIRMED_RESOLVED]**: Appendix per-task table caption 明确标注 \"This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table 2)\"。Additional Observations (Appendix D) 明确说明 \"this v1-specific pattern does not replicate under the controlled v2 factorial design...the v1 per-task pattern may reflect implementation-specific artifacts\"。v1 scope 标注清晰。\n\n**R1-W13 [CONFIRMED_RESOLVED]**: Discussion 中 CKA 分析逻辑自洽——\"CKA analysis confirms that encoder representations remain intact under all conditions (CKA ≥ 0.95)...ruling out representational drift and localizing the effect to optimization dynamics.\" BN 的假设聚焦于 running statistics 对优化轨迹的影响，与 CKA 显示的表征完整性不矛盾。\n\n**R1-W21 [CONFIRMED_RESOLVED]**: 当前版本措辞准确。Title 使用疑问句式（\"Does...?\"），核心发现用 \"associated with\"（非因果断言），结论限定为 \"under the conditions tested\"，每项 claim 附带 Cohen's d 及置信度标注。Contribution list 与实际结果匹配。\n\n---\n\n## 总体评分\n\n**Overall**: 5/10（Borderline Reject）\n\n**一句话总结**: 实验设计严谨的负面结果论文，但统计效力不足以支撑其核心主张，且关键发现的泛化性受单一架构/基准的严重限制。\n\n## 官方维度打分（基于 CoRL review framework）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 5/10 | BN + gradient flow 导致安全下降是已知 BN distributional sensitivity 在 VLA 场景的特例，非全新机制；factorial design 是标准统计方法的合理应用而非方法论贡献 |\n| Quality | 4/10 | n=3-4/cell，两个 main effect 均未达显著（p=0.104, p=0.060）；content irrelevance 仅在 v1 观察到；codebase v1→v2 shift 8.6pp 动摇结果稳定性 |\n| Clarity | 7/10 | 叙事结构清晰，factorial 呈现规范；但 abstract 过长过密，Contribution 2 为填充项 |\n| Significance | 4/10 | 实际指导意义局限于 OpenVLA+OFT+LoRA rank 32 + SafeLIBERO Level I 这一特定配置；缺乏机制验证使 guideline 的适用范围不明 |\n| Relevance | 8/10 | VLA safety 是 CoRL 核心议题，spatial supervision 与安全的关系是社区的 open question |\n| Limitations | 6/10 | 诚实列举了大量限制，但 Limitations section 放在 Appendix H 而非正文，违反 CoRL 2026 格式要求 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 统计效力不足以支撑核心主张\n- 具体位置：Section 4.2, Table 3, Appendix F\n- 问题：2×2 factorial 每 cell 仅 n=3-4（共 14 observations）。两个 main effect 均未达 α=0.05 显著性：gradient flow F(1,10)=3.20, p=0.104；normalization F(1,10)=4.49, p=0.060。论文主要依赖 Cohen's d 作为推断依据，但 n=3 时 d 的抽样方差极大（Hedges' correction 后 d 会进一步缩小），置信区间宽到几乎无法排除零效应。Abstract 和 Introduction 中 \"large effect\" 的措辞给读者造成的信心程度远超数据实际支持。\n- 为什么影响接收：论文的核心主张（BN + gradient flow 损害安全，LN 提供一致优势）建立在统计上不显著的效应之上。如果增加样本后效应消失，整篇论文的结论将被推翻。对于一篇以 empirical investigation 为题的论文，这是致命的。\n- 建议修改方向：(1) 每 cell 至少 n=8-10 seeds 以达到 80% power for d=1.0；(2) 或在 main text 更显著地限定结论的确定性，用 \"preliminary evidence suggests\" 而非隐含的确定性语气；(3) 报告 Hedges' g 而非 Cohen's d 以校正小样本偏差。\n\n**N2** [critical] Limitations section 不在正文内，违反 CoRL 2026 格式要求\n- 具体位置：Discussion 最后一句 \"Limitations are in Appendix H\"；Appendix Section H\n- 问题：CoRL 2026 明确要求 Limitations section 计入 8 页正文限制。当前论文的 Limitations 完全放在 Appendix H（第 18-19 页），正文仅有一句指引。这不满足 \"必须包含 Limitations section\" 的格式要求。\n- 为什么影响接收：格式违规可能导致 desk rejection。Limitations 是 reviewer 评估论文诚实性的关键部分，放在 appendix 降低了其可见性。\n- 建议修改方向：将 Appendix H 的核心限制（单一架构、单一 benchmark、LoRA 特异性、小样本、v1/v2 codebase sensitivity）压缩为 1 段放入正文 Discussion 或独立 Section，同时压缩其他正文内容以满足 8 页限制。\n\n**N3** [critical] 正文超过 8 页限制\n- 具体位置：Section 6 Conclusion 位于 PDF 第 9 页\n- 问题：正文 Sections 1-5（Introduction 到 Discussion）占满 8 页，Section 6 Conclusion 溢出到第 9 页。CoRL 2026 限制正文（含 Limitations）≤ 8 页，references 不限。当前结构 8.25 页正文 + 无 Limitations = 实际需要约 9 页正文。\n- 为什么影响接收：超页直接违反投稿规定。\n- 建议修改方向：压缩 Discussion（当前独占整页 8，有冗余）和 Introduction（Contribution list 过长），腾出空间给 Conclusion + Limitations。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Content irrelevance 核心发现仅来自 v1 codebase，未在 v2 复现\n- 具体位置：Abstract (\"Spatial label content...showed no detectable effect on safety (observed under v1 codebase)\")；Introduction line 16；Discussion line 13\n- 问题：论文三大核心发现之一——\"空间标签内容（structured vs. random vs. depth）对安全无可检测效应\"——仅在存在 batch-index resume bug 的 v1 代码下观察。该 bug 修复后（v2），同一 seed 的 CAR 偏移高达 8.6pp，且 v1 的 crossover 效应模式在 v2 下消失。Random OCC 和 Depth 均未在 v2 下重新训练。论文间接论证（gradient orthogonality analysis under v2 \"indirectly supports\"）不能替代直接复现。\n- 建议：在 v2 下重新训练 Random OCC 和 Depth 至少 3 seeds，或将此发现降级为 \"preliminary observation under v1\"，不放入 abstract。\n\n**W2** [warning] 单一架构/基准严重限制泛化性，与 title 的一般性提问不匹配\n- 具体位置：Title, Abstract, 整体\n- 问题：Title 问 \"Does Auxiliary Spatial Supervision Make VLAs Safer?\"——一个关于 VLA 类别的一般性问题。但所有实验仅使用 OpenVLA-7B + OFT + LoRA rank 32 在 SafeLIBERO Level I（10 个桌面任务）上进行。论文无法回答关于其他 VLA（RT-2, Octo, π₀）、其他 fine-tuning（full FT, different LoRA ranks, QLoRA）、其他 benchmark（real robot, RLBench, CALVIN）的安全问题。Discussion 中的 LoRA-specificity caveat 承认了这一点，但 title 仍然过于宽泛。\n- 建议：修改 title 限定范围，如 \"Does Auxiliary Spatial Supervision Make LoRA-Tuned VLAs Safer? A Factorial Study on SafeLIBERO\"。\n\n**W3** [warning] Codebase sensitivity (v1→v2) 实质上削弱而非加强论文主张\n- 具体位置：Discussion line 11；Appendix E\n- 问题：论文将 v1→v2 codebase sensitivity 定位为 \"an independent finding\"（Discussion: \"This level of sensitivity to non-hyperparameter implementation details has not been documented in prior multi-task learning work and constitutes an independent finding\"）。但这个发现实际上意味着：(1) 一个 batch-index bug 就能改变定性结论（crossover → additive）；(2) 同一 seed 在 v1/v2 间偏移 8.6pp；(3) 我们无法确认 v2 是否还有未发现的 bug。这更像是一个可靠性警告，而非独立贡献。\n- 建议：坦诚呈现此发现的双重含义——既是 fragility 的证据，也是结论不确定性的来源。\n\n**W4** [warning] Contribution 2 \"Factorial methodology for VLA auxiliary heads\" 不构成独立贡献\n- 具体位置：Introduction Contribution list item 2\n- 问题：Factorial design 是 Fisher (1935) 以来的标准统计方法。在 VLA auxiliary supervision 中应用它是合理的实验选择，但 \"introduce the first systematic factorial comparison\" 不等于方法论贡献。任何研究者都可以设计 2×2 factorial——这是实验设计，不是贡献。\n- 建议：删除或合并到 Contribution 1 中作为方法描述。\n\n**W5** [warning] 机制假设未经验证\n- 具体位置：Discussion, Section 4.3 \"Mechanism remains open\"\n- 问题：论文排除了 gradient conflict（cosine ≈ 0）和 gradient amplification（norms comparable），提出 \"BN running statistics\" 假设但未验证。可以通过以下方式直接测试：(1) 固定 BN running statistics（eval mode）观察效应是否消失；(2) 将 BN momentum 设为 0 或 1；(3) 比较 training/eval mode BN statistics 的 divergence。这些实验在现有框架下可以低成本完成，但未执行。\n- 建议：至少执行一个 BN running statistics 的消融实验来验证或否证假设。\n\n**W6** [warning] 与 MTL gradient methods 的对比讨论不够深入\n- 具体位置：Related Work Section 2.2；Discussion\n- 问题：论文引用了 PCGrad、CAGrad、GradNorm、NashMTL，但只用它们来说明 \"gradient conflict is not the mechanism here\"。然而，PCGrad/CAGrad 之外还有一类 MTL 方法关注 representation interference 和 task-specific normalization（如 MGDA [Sener & Koltun, 2018]、task-specific batch normalization [Bilen & Vedaldi, 2017]）。特别是 task-specific BN 文献直接相关——在 MTL 中为不同任务使用不同的 BN statistics 已是已知的解决方案。论文的发现（BN + auxiliary gradient flow 损害主任务）可以被视为 task-specific BN 文献的自然推论。\n- 建议：引用 task-specific BN 工作并讨论论文发现与该文献的关系。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Abstract 过长过密（约 280 词），包含大量具体数值（Cohen's d = -0.93, +1.07, σ=0.064, η²<0.01 等）。建议精简至 200 词以内，将详细数值移至正文。\n- **M2**: BibTeX key chen2026gstvla 的 author 字段为 \"Md Selim Sarowar and others\"，但 key 前缀为 \"chen2026\"，命名不一致。不影响渲染但反映疏忽。\n- **M3**: Contribution 3 (\"Actionable guidelines at zero cost\") 本质上是 Contribution 1 的实际推论，不构成独立贡献。三条贡献可压缩为两条。\n- **M4**: Figure 1 caption 很长（约 5 行），包含大量数值细节，可适当精简。\n- **M5**: Related Work Section 2.1 末尾的长引用列表（15+ 引用 [5-16]）读起来像清单，可以按类别分组叙述。\n\n---\n\n## 主要优势\n\n1. **严谨的实验设计**：2×2 factorial crossing gradient flow × normalization 是隔离交互效应的正确方法，优于 VLA 领域常见的单因子消融。12 个条件覆盖 5 个因子的设计空间较广。\n2. **诚实的不确定性报告**：论文坦承 v1/v2 codebase sensitivity、小样本限制、LoRA 特异性。这种坦诚在负面结果论文中尤其可贵。\n3. **实用且低成本的建议**：即使统计效力有限，\"避免 BN + gradient flow\" 的建议风险极低（改用 LN 或 detach 不增加推理成本），具有实用价值。\n4. **全面的 Appendix**：梯度分析、per-task breakdown、codebase sensitivity 分析、统计功效分析等 7 个 appendix section 提供了充分的支撑材料和透明度。\n5. **填补了空白**：首次直接测量 spatial auxiliary supervision 对 VLA collision avoidance 的效果，这个实验是该领域需要有人做的。\n\n---\n\n## Missing References\n\n1. **Sener & Koltun (2018)**, \"Multi-Task Learning as Multi-Objective Optimization\" (NeurIPS) — MGDA 方法，MTL 的重要基线\n2. **Bilen & Vedaldi (2017)**, \"Integrated Perception with Recurrent Multi-Task Neural Networks\" — task-specific BN 在 MTL 中的应用，与本文 BN 发现直接相关\n3. **Maninis et al. (2019)**, \"Attentive Single-Tasking of Multiple Tasks\" (CVPR) — 讨论 MTL 中 task-specific normalization\n4. **Rebuffi et al. (2018)**, \"Efficient Parametrization of Multi-Domain Deep Neural Networks\" (CVPR) — domain-specific BN adapters，与论文 BN sensitivity 发现相关\n5. **π₀ (Black et al., 2024)**, Physical Intelligence 的 VLA — 应在 Related Work 中讨论作为 alternative VLA architecture\n6. **Octo (Team Octo, 2024)** — 重要的开源 VLA 基础模型\n7. **LIBERO-Object** — 论文 Limitations 中提到但未引用作为 citation\n\n---\n\n## Questions to Authors\n\nQ1: 是否计划在 v2 codebase 下重新训练 Random OCC 和 Depth 条件？如果 content irrelevance 在 v2 下不成立，论文的核心叙事需要如何调整？\n\nQ2: 是否考虑过在 BN + gradient flow 条件下固定 BN 的 running statistics（设置为 eval mode 或 momentum=0）来直接验证 BN running statistics 假设？\n\nQ3: 如果将 LoRA rank 从 32 提高到 128 或 256（增加 capacity），BN + gradient flow 的负面效应是否可能消失（因为更大的 rank 可以 \"absorb\" dual-objective landscape）？论文在 Discussion 中提到这个可能性但未实验验证。\n\nQ4: 在 CoRL 2026 的 first-round rejection 标准中，如果没有 reviewer 给出 weak accept 或以上，论文将被候选 reject without rebuttal。鉴于统计效力的限制，作者如何论证当前证据足以支持发表？\n",
  "reviewer_id": "2",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审查报告：Novelty + Writing Quality + Completeness\n\n## 上轮 Resolved Issue 抽查\n\n**R1-W5 [CONFIRMED_RESOLVED]**: Table 2（Main Results）已按 v2 factorial core 和 v1 supplementary 分区呈现，Random OCC 放在 midrule 以下的 supplementary 区域并标注 ★v1 code，ΔCAR 因 cross-codebase mismatch 标注为 \"---\"。Table 1（Ablation Design）按比较对分组，逻辑清晰。\n\n**R1-W6 [CONFIRMED_RESOLVED]**: Appendix per-task table caption 明确标注 \"This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table 2)\"。Additional Observations (Appendix D) 明确说明 \"this v1-specific pattern does not replicate under the controlled v2 factorial design...the v1 per-task pattern may reflect implementation-specific artifacts\"。v1 scope 标注清晰。\n\n**R1-W13 [CONFIRMED_RESOLVED]**: Discussion 中 CKA 分析逻辑自洽——\"CKA analysis confirms that encoder representations remain intact under all conditions (CKA ≥ 0.95)...ruling out representational drift and localizing the effect to optimization dynamics.\" BN 的假设聚焦于 running statistics 对优化轨迹的影响，与 CKA 显示的表征完整性不矛盾。\n\n**R1-W21 [CONFIRMED_RESOLVED]**: 当前版本措辞准确。Title 使用疑问句式（\"Does...?\"），核心发现用 \"associated with\"（非因果断言），结论限定为 \"under the conditions tested\"，每项 claim 附带 Cohen's d 及置信度标注。Contribution list 与实际结果匹配。\n\n---\n\n## 总体评分\n\n**Overall**: 5/10（Borderline Reject）\n\n**一句话总结**: 实验设计严谨的负面结果论文，但统计效力不足以支撑其核心主张，且关键发现的泛化性受单一架构/基准的严重限制。\n\n## 官方维度打分（基于 CoRL review framework）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 5/10 | BN + gradient flow 导致安全下降是已知 BN distributional sensitivity 在 VLA 场景的特例，非全新机制；factorial design 是标准统计方法的合理应用而非方法论贡献 |\n| Quality | 4/10 | n=3-4/cell，两个 main effect 均未达显著（p=0.104, p=0.060）；content irrelevance 仅在 v1 观察到；codebase v1→v2 shift 8.6pp 动摇结果稳定性 |\n| Clarity | 7/10 | 叙事结构清晰，factorial 呈现规范；但 abstract 过长过密，Contribution 2 为填充项 |\n| Significance | 4/10 | 实际指导意义局限于 OpenVLA+OFT+LoRA rank 32 + SafeLIBERO Level I 这一特定配置；缺乏机制验证使 guideline 的适用范围不明 |\n| Relevance | 8/10 | VLA safety 是 CoRL 核心议题，spatial supervision 与安全的关系是社区的 open question |\n| Limitations | 6/10 | 诚实列举了大量限制，但 Limitations section 放在 Appendix H 而非正文，违反 CoRL 2026 格式要求 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 统计效力不足以支撑核心主张\n- 具体位置：Section 4.2, Table 3, Appendix F\n- 问题：2×2 factorial 每 cell 仅 n=3-4（共 14 observations）。两个 main effect 均未达 α=0.05 显著性：gradient flow F(1,10)=3.20, p=0.104；normalization F(1,10)=4.49, p=0.060。论文主要依赖 Cohen's d 作为推断依据，但 n=3 时 d 的抽样方差极大（Hedges' correction 后 d 会进一步缩小），置信区间宽到几乎无法排除零效应。Abstract 和 Introduction 中 \"large effect\" 的措辞给读者造成的信心程度远超数据实际支持。\n- 为什么影响接收：论文的核心主张（BN + gradient flow 损害安全，LN 提供一致优势）建立在统计上不显著的效应之上。如果增加样本后效应消失，整篇论文的结论将被推翻。对于一篇以 empirical investigation 为题的论文，这是致命的。\n- 建议修改方向：(1) 每 cell 至少 n=8-10 seeds 以达到 80% power for d=1.0；(2) 或在 main text 更显著地限定结论的确定性，用 \"preliminary evidence suggests\" 而非隐含的确定性语气；(3) 报告 Hedges' g 而非 Cohen's d 以校正小样本偏差。\n\n**N2** [critical] Limitations section 不在正文内，违反 CoRL 2026 格式要求\n- 具体位置：Discussion 最后一句 \"Limitations are in Appendix H\"；Appendix Section H\n- 问题：CoRL 2026 明确要求 Limitations section 计入 8 页正文限制。当前论文的 Limitations 完全放在 Appendix H（第 18-19 页），正文仅有一句指引。这不满足 \"必须包含 Limitations section\" 的格式要求。\n- 为什么影响接收：格式违规可能导致 desk rejection。Limitations 是 reviewer 评估论文诚实性的关键部分，放在 appendix 降低了其可见性。\n- 建议修改方向：将 Appendix H 的核心限制（单一架构、单一 benchmark、LoRA 特异性、小样本、v1/v2 codebase sensitivity）压缩为 1 段放入正文 Discussion 或独立 Section，同时压缩其他正文内容以满足 8 页限制。\n\n**N3** [critical] 正文超过 8 页限制\n- 具体位置：Section 6 Conclusion 位于 PDF 第 9 页\n- 问题：正文 Sections 1-5（Introduction 到 Discussion）占满 8 页，Section 6 Conclusion 溢出到第 9 页。CoRL 2026 限制正文（含 Limitations）≤ 8 页，references 不限。当前结构 8.25 页正文 + 无 Limitations = 实际需要约 9 页正文。\n- 为什么影响接收：超页直接违反投稿规定。\n- 建议修改方向：压缩 Discussion（当前独占整页 8，有冗余）和 Introduction（Contribution list 过长），腾出空间给 Conclusion + Limitations。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Content irrelevance 核心发现仅来自 v1 codebase，未在 v2 复现\n- 具体位置：Abstract (\"Spatial label content...showed no detectable effect on safety (observed under v1 codebase)\")；Introduction line 16；Discussion line 13\n- 问题：论文三大核心发现之一——\"空间标签内容（structured vs. random vs. depth）对安全无可检测效应\"——仅在存在 batch-index resume bug 的 v1 代码下观察。该 bug 修复后（v2），同一 seed 的 CAR 偏移高达 8.6pp，且 v1 的 crossover 效应模式在 v2 下消失。Random OCC 和 Depth 均未在 v2 下重新训练。论文间接论证（gradient orthogonality analysis under v2 \"indirectly supports\"）不能替代直接复现。\n- 建议：在 v2 下重新训练 Random OCC 和 Depth 至少 3 seeds，或将此发现降级为 \"preliminary observation under v1\"，不放入 abstract。\n\n**W2** [warning] 单一架构/基准严重限制泛化性，与 title 的一般性提问不匹配\n- 具体位置：Title, Abstract, 整体\n- 问题：Title 问 \"Does Auxiliary Spatial Supervision Make VLAs Safer?\"——一个关于 VLA 类别的一般性问题。但所有实验仅使用 OpenVLA-7B + OFT + LoRA rank 32 在 SafeLIBERO Level I（10 个桌面任务）上进行。论文无法回答关于其他 VLA（RT-2, Octo, π₀）、其他 fine-tuning（full FT, different LoRA ranks, QLoRA）、其他 benchmark（real robot, RLBench, CALVIN）的安全问题。Discussion 中的 LoRA-specificity caveat 承认了这一点，但 title 仍然过于宽泛。\n- 建议：修改 title 限定范围，如 \"Does Auxiliary Spatial Supervision Make LoRA-Tuned VLAs Safer? A Factorial Study on SafeLIBERO\"。\n\n**W3** [warning] Codebase sensitivity (v1→v2) 实质上削弱而非加强论文主张\n- 具体位置：Discussion line 11；Appendix E\n- 问题：论文将 v1→v2 codebase sensitivity 定位为 \"an independent finding\"（Discussion: \"This level of sensitivity to non-hyperparameter implementation details has not been documented in prior multi-task learning work and constitutes an independent finding\"）。但这个发现实际上意味着：(1) 一个 batch-index bug 就能改变定性结论（crossover → additive）；(2) 同一 seed 在 v1/v2 间偏移 8.6pp；(3) 我们无法确认 v2 是否还有未发现的 bug。这更像是一个可靠性警告，而非独立贡献。\n- 建议：坦诚呈现此发现的双重含义——既是 fragility 的证据，也是结论不确定性的来源。\n\n**W4** [warning] Contribution 2 \"Factorial methodology for VLA auxiliary heads\" 不构成独立贡献\n- 具体位置：Introduction Contribution list item 2\n- 问题：Factorial design 是 Fisher (1935) 以来的标准统计方法。在 VLA auxiliary supervision 中应用它是合理的实验选择，但 \"introduce the first systematic factorial comparison\" 不等于方法论贡献。任何研究者都可以设计 2×2 factorial——这是实验设计，不是贡献。\n- 建议：删除或合并到 Contribution 1 中作为方法描述。\n\n**W5** [warning] 机制假设未经验证\n- 具体位置：Discussion, Section 4.3 \"Mechanism remains open\"\n- 问题：论文排除了 gradient conflict（cosine ≈ 0）和 gradient amplification（norms comparable），提出 \"BN running statistics\" 假设但未验证。可以通过以下方式直接测试：(1) 固定 BN running statistics（eval mode）观察效应是否消失；(2) 将 BN momentum 设为 0 或 1；(3) 比较 training/eval mode BN statistics 的 divergence。这些实验在现有框架下可以低成本完成，但未执行。\n- 建议：至少执行一个 BN running statistics 的消融实验来验证或否证假设。\n\n**W6** [warning] 与 MTL gradient methods 的对比讨论不够深入\n- 具体位置：Related Work Section 2.2；Discussion\n- 问题：论文引用了 PCGrad、CAGrad、GradNorm、NashMTL，但只用它们来说明 \"gradient conflict is not the mechanism here\"。然而，PCGrad/CAGrad 之外还有一类 MTL 方法关注 representation interference 和 task-specific normalization（如 MGDA [Sener & Koltun, 2018]、task-specific batch normalization [Bilen & Vedaldi, 2017]）。特别是 task-specific BN 文献直接相关——在 MTL 中为不同任务使用不同的 BN statistics 已是已知的解决方案。论文的发现（BN + auxiliary gradient flow 损害主任务）可以被视为 task-specific BN 文献的自然推论。\n- 建议：引用 task-specific BN 工作并讨论论文发现与该文献的关系。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Abstract 过长过密（约 280 词），包含大量具体数值（Cohen's d = -0.93, +1.07, σ=0.064, η²<0.01 等）。建议精简至 200 词以内，将详细数值移至正文。\n- **M2**: BibTeX key chen2026gstvla 的 author 字段为 \"Md Selim Sarowar and others\"，但 key 前缀为 \"chen2026\"，命名不一致。不影响渲染但反映疏忽。\n- **M3**: Contribution 3 (\"Actionable guidelines at zero cost\") 本质上是 Contribution 1 的实际推论，不构成独立贡献。三条贡献可压缩为两条。\n- **M4**: Figure 1 caption 很长（约 5 行），包含大量数值细节，可适当精简。\n- **M5**: Related Work Section 2.1 末尾的长引用列表（15+ 引用 [5-16]）读起来像清单，可以按类别分组叙述。\n\n---\n\n## 主要优势\n\n1. **严谨的实验设计**：2×2 factorial crossing gradient flow × normalization 是隔离交互效应的正确方法，优于 VLA 领域常见的单因子消融。12 个条件覆盖 5 个因子的设计空间较广。\n2. **诚实的不确定性报告**：论文坦承 v1/v2 codebase sensitivity、小样本限制、LoRA 特异性。这种坦诚在负面结果论文中尤其可贵。\n3. **实用且低成本的建议**：即使统计效力有限，\"避免 BN + gradient flow\" 的建议风险极低（改用 LN 或 detach 不增加推理成本），具有实用价值。\n4. **全面的 Appendix**：梯度分析、per-task breakdown、codebase sensitivity 分析、统计功效分析等 7 个 appendix section 提供了充分的支撑材料和透明度。\n5. **填补了空白**：首次直接测量 spatial auxiliary supervision 对 VLA collision avoidance 的效果，这个实验是该领域需要有人做的。\n\n---\n\n## Missing References\n\n1. **Sener & Koltun (2018)**, \"Multi-Task Learning as Multi-Objective Optimization\" (NeurIPS) — MGDA 方法，MTL 的重要基线\n2. **Bilen & Vedaldi (2017)**, \"Integrated Perception with Recurrent Multi-Task Neural Networks\" — task-specific BN 在 MTL 中的应用，与本文 BN 发现直接相关\n3. **Maninis et al. (2019)**, \"Attentive Single-Tasking of Multiple Tasks\" (CVPR) — 讨论 MTL 中 task-specific normalization\n4. **Rebuffi et al. (2018)**, \"Efficient Parametrization of Multi-Domain Deep Neural Networks\" (CVPR) — domain-specific BN adapters，与论文 BN sensitivity 发现相关\n5. **π₀ (Black et al., 2024)**, Physical Intelligence 的 VLA — 应在 Related Work 中讨论作为 alternative VLA architecture\n6. **Octo (Team Octo, 2024)** — 重要的开源 VLA 基础模型\n7. **LIBERO-Object** — 论文 Limitations 中提到但未引用作为 citation\n\n---\n\n## Questions to Authors\n\nQ1: 是否计划在 v2 codebase 下重新训练 Random OCC 和 Depth 条件？如果 content irrelevance 在 v2 下不成立，论文的核心叙事需要如何调整？\n\nQ2: 是否考虑过在 BN + gradient flow 条件下固定 BN 的 running statistics（设置为 eval mode 或 momentum=0）来直接验证 BN running statistics 假设？\n\nQ3: 如果将 LoRA rank 从 32 提高到 128 或 256（增加 capacity），BN + gradient flow 的负面效应是否可能消失（因为更大的 rank 可以 \"absorb\" dual-objective landscape）？论文在 Discussion 中提到这个可能性但未实验验证。\n\nQ4: 在 CoRL 2026 的 first-round rejection 标准中，如果没有 reviewer 给出 weak accept 或以上，论文将被候选 reject without rebuttal。鉴于统计效力的限制，作者如何论证当前证据足以支持发表？\n",
    "reviewer_id": "2",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-28T10:55:06.556447+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4034
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-28T10:55:14.841443+00:00_

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
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
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

_source line 89 · 2026-05-28T10:55:14.892079+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-28T10:55:18.657508+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_1/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-28T10:55:18.759053+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 101
}
```

</details>

---

### Assistant

_source line 92 · 2026-05-28T10:55:29.498107+00:00_

审查报告已提交给 Review Director。

核心结论：**5/10 Borderline Reject**。

三个 Must-Fix 问题：
1. **统计效力不足**——n=3-4/cell，两个 main effect 均未达显著（p=0.104, p=0.060），Cohen's d 在小样本下不稳定
2. **Limitations section 放在 Appendix H**，违反 CoRL 2026 "Limitations 计入 8 页正文" 的格式要求
3. **正文超 8 页**——Conclusion 溢出到第 9 页，且尚未加入 Limitations

四个上轮 resolved issue 全部确认修复：R1-W5、R1-W6、R1-W13、R1-W21 均 [CONFIRMED_RESOLVED]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2"
}
```

</details>

---

## Round 2

4 recorded events

### User

_source line 93 · 2026-05-28T10:56:03.416627+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

以下是 Reviewer 1（方法严谨性 + 实验有效性）的完整审稿报告。请逐条回应其 Must-Fix 和 Should-Fix，每条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

### Reviewer 1 评分：5/10 (Borderline Reject)

### R1-C9 验证结果
- Table 1 factorial 全部 v2 [RESOLVED]
- v1 数据隔离到 supplementary [PARTIALLY RESOLVED]
- Random OCC (v1) 放在 factorial 区域 [STILL_OPEN]
- 跨 codebase ΔCAR 处理 [PARTIALLY RESOLVED] — Section 4.1 用 v1 的 Full OCC 和 Random OCC 比较来声称 content irrelevance，但 v2 下 Full OCC CAR 从 0.797 降到 0.725（7.2pp shift）
- 正文 v1/v2 混用声明 [STILL_OPEN] — Introduction 贡献(1) 和 Conclusion 的 content irrelevance 声明缺 v1 caveat

### Must-Fix
**N1** [critical] 内容无关性声明缺乏同代码库证据——"spatial label content shows no detectable effect" 完全基于 v1 数据。v1→v2 Full OCC CAR 偏移 7.2pp，v1 结论不可推广。Discussion 承认 "whether it persists under v2 remains open"，但 Abstract/Introduction/Conclusion 仍作为确立结论。建议：(a) v2 下重训 Random OCC 3 seeds；或 (b) 降级为 preliminary observation，从 contributions 移除。

**N2** [critical] 统计功效不足以支撑 "large effect" 的因果声明——ANOVA 两个主效应均未达显著（p=0.104, p=0.060），所有 Bonferroni pairwise 不显著。Cohen's d 在 n=3-4 下存在约 15-20% 正向偏差（Hedges 1981），全文未提及 Hedges' g。正文使用因果语言（"degrades"）超出数据支撑范围。

**N3** [critical] Table 1 中 Random OCC (v1) 位置误导——放在 midrule 上方 v2 section，CAR 0.789 与 v2 Full OCC 0.725 并列。但 v1 下 Full OCC 是 0.797（差异仅 0.8pp），当前布局放大了表观差异（6.4pp）。

### Should-Fix
**W1** Factorial 设计不完整——label content 仅在 BN+gradient flow ON (v1) 下测试，未在 LN 或 Detach 下测试。不是 "5 factors" factorial 而是 "2×2 factorial + 单因子 ablations"。

**W2** Cohen's d 小样本偏差未校正——Hedges' g correction factor J ≈ 0.82-0.87，d=0.93 实际约 g≈0.76-0.81（"large" → "medium-to-large"）。

**W3** λ(t) 指数衰减的功能形式未论证——线性/step/cosine 可能产生不同的 gradient flow 动态。

**W4** 碰撞检测阈值 10⁻³ 的合理性和敏感性未讨论——未提供物理解释，无阈值敏感性分析。

**W5** BN running statistics 假说缺乏直接证据——未做 eval mode、momentum=0 等消融。

**W6** 单一 benchmark + 单一架构限制泛化性——Abstract/Conclusion 的 practical guidelines 无限定条件。

### Missing References
Hedges (1981), Ioffe & Szegedy (2015), Wu & He (2018)

---

请对以上每条 Must-Fix (N1-N3) 和 Should-Fix (W1-W6) 逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-28T10:58:12.168120+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 交叉回应：对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix\n\n**[AGREE] R1-N1: Content irrelevance 声明缺乏同代码库证据**\n完全同意。我在自己的报告中将此列为 W1（Should-Fix），但经 R1 更详细的论证后，我认同将其升级为 Must-Fix 是合理的。关键证据链：(1) v1→v2 Full OCC CAR 从 0.797 降至 0.725（7.2pp shift，Appendix E）；(2) v1 的 crossover 效应模式在 v2 下完全消失（Appendix E: \"the normalization × gradient flow pattern appeared as a crossover (p=0.025); under v2, both rows slope in the same direction\"）；(3) Discussion line 13 自己承认 \"whether it persists under v2 remains open\"。在 v1 代码存在已知 bug 且定性结论已因 bug 修复而翻转的情况下，将 v1-only 的 content irrelevance 发现写入 Abstract 和 Contribution list 是不当的。R1 提出的两个修复方案（v2 重训 or 降级为 preliminary observation）均合理。\n\n**[AGREE] R1-N2: 统计功效不足以支撑 \"large effect\" 因果声明**\n完全同意。我在自己的报告中将此列为 N1（最高优先级 Must-Fix）。补充 R1 的分析：除了 Hedges' g 校正（R1 估计 d=0.93 校正为 g≈0.76-0.81）之外，n=3 时 Cohen's d 的 95% CI 极宽。对于 d=0.93, n₁=n₂=3，非中心 t 分布的近似 95% CI 约为 [-0.8, 2.7]，即不能排除零效应甚至反向效应。正文使用 \"degrades\"（Discussion line 5: \"gradient flow drops CAR below the Vanilla baseline\"）这类因果语言，超出了关联性证据的支撑范围。此外，ANOVA 两个主效应的 p-values（0.104 和 0.060）在任何常规标准下均不显著，论文主要靠效应量叙事来回避这一事实。\n\n**[REBUT] R1-N3: Table 中 Random OCC (v1) 位置误导**\n部分反驳。根据我对 PDF 第 5 页的阅读，Random OCC 确实位于 midrule **以下**的 supplementary 区域，并标注了 ★v1 code，ΔCAR 列显示 \"---\"（因 cross-codebase mismatch 不做差值比较）。我在自己的审查中将 R1-W5 标记为 [CONFIRMED_RESOLVED]，理由正是 Random OCC 已被正确隔离到 v1 supplementary section。\n\n但 R1 指出的**实质性问题**是成立的：即使分区正确，v1 Random OCC（CAR 0.789）和 v2 Full OCC（CAR 0.725）在同一表格中视觉上可比较，读者可能忽略 ★ 标记而直接比较数值，得到 6.4pp 差异的误导结论（同 codebase 差异仅 0.8pp）。建议的折中方案：保持当前分区，但在 table caption 中增加一句 \"v1 and v2 rows are not directly comparable due to codebase differences (see Appendix E)\"。\n\n将此条从 critical 降级为 warning 更合适——因为 midrule 分区、★ 标记和 ΔCAR=\"---\" 已提供了合理的防误读措施，只是不够醒目。\n\n---\n\n## Should-Fix\n\n**[AGREE] R1-W1: Factorial 设计不完整**\n同意。论文 Introduction 声称 \"twelve conditions varying five factors\"，但实际的完整 factorial crossing 仅限于 2×2（gradient flow × normalization）。Label content 仅在 BN + gradient flow ON 下测试（Full OCC vs Random OCC，均为 v1），未在 LN 或 Detach 条件下测试。Reference frame（BEV vs Depth）同样仅在 BN + gradient flow ON 下测试。Temporal extent 仅在 BN 下测试。这不是 5-factor factorial，而是 \"2×2 factorial core + 8 个单因子 ablations\"。论文 Method Section 3.1 的措辞应修正——\"systematic factorial comparison\" 仅适用于 2×2 核心，其余为单因子 ablation。我在自己报告中的 W4 也指出 Contribution 2 将 factorial methodology 列为独立贡献不恰当，此条进一步支持该观点。\n\n**[AGREE] R1-W2: Cohen's d 小样本偏差未校正**\n同意。Hedges' g 是小样本效应量报告的标准做法（Hedges, 1981），尤其在 n<20 时 Cohen's d 的正向偏差不可忽略。R1 给出的校正因子 J ≈ 0.82-0.87 合理（对 n₁=n₂=3，J = 1 - 3/(4(n₁+n₂-2)-1) ≈ 0.81）。d=0.93 校正后约 g≈0.75，从 \"large\" 边界滑入 \"medium-to-large\"。这不改变效应方向但改变叙事力度，论文应在 main text 报告 Hedges' g。\n\n**[REBUT] R1-W3: λ(t) 指数衰减的功能形式未论证**\n部分反驳。R1 的建议（测试 linear/step/cosine）在理论上有意义，但论文的核心发现是关于 gradient flow pathway（ON vs OFF）和 normalization type（BN vs LN）的交互，而非 loss weight schedule 的影响。λ(t) 衰减只控制 auxiliary gradient 的幅度随时间的变化，而 BN/LN 差异作用于 normalization statistics 的耦合机制——这两者在不同的 causal pathway 上。此外，Appendix 的 temporal analysis（Cutoff series）已间接涉及 gradient flow 持续时间的影响。将此列为 Should-Fix 偏重；作为 Limitations 中的 future work 更合适（论文 Appendix H 最后一句已提及：\"we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules\"）。\n\n**[AGREE] R1-W4: 碰撞检测阈值 10⁻³ 的合理性和敏感性未讨论**\n同意，但重要性较低。论文 Method Section 3.2 和 Appendix B 提到 \"a collision is registered when the L1 displacement of the obstacle's body_xpos exceeds 10⁻³\"，但未解释 10⁻³ 对应的物理尺度（是 mm？cm？MuJoCo 单位？），也未做阈值敏感性分析（如 10⁻², 10⁻⁴ 下结果是否一致）。不过这是 SafeLIBERO benchmark 自身定义的阈值（cite [14] hu2025vlsa），论文只是沿用而非自定义，责任主要在 benchmark 一方。建议在 Appendix 中添加一句物理尺度解释即可。\n\n**[AGREE] R1-W5: BN running statistics 假说缺乏直接证据**\n完全同意。我在自己报告中将此列为 W5 并提出了几乎相同的实验建议（eval mode、momentum=0 消融）。Discussion 的 BN hypothesis 是合理的推测，但论文既声称发现了 \"normalization-dependent gradient flow effect\" 作为核心贡献，又未验证所提出的机制，形成了 claim-evidence gap。在 v2 codebase 下固定 BN running statistics 是低成本实验，应执行。\n\n**[AGREE] R1-W6: 单一 benchmark + 单一架构限制泛化性**\n完全同意。我在自己报告中将此列为 W2（Should-Fix）。Abstract 的 \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer?\" 是关于整个 VLA 类别的问题，但实验仅覆盖 OpenVLA-7B + OFT + LoRA rank 32 + SafeLIBERO Level I。Conclusion 的 \"Practitioners should omit auxiliary spatial heads\" 作为无限定条件的建议过于宽泛。R1 的建议（在 Abstract/Conclusion 加限定）与我建议的修改 title 一致。\n\n---\n\n## 总结\n\nR1 的 3 条 Must-Fix 中，N1（content irrelevance v1-only）和 N2（统计功效）与我的核心关切高度一致，我认为这是论文最大的两个问题。N3（Random OCC 表格位置）的实质关切成立但严重性不及 critical——当前标注措施（★、---、midrule 分区）已部分缓解，但需加强 caption 提示。\n\nR1 的 6 条 Should-Fix 中，W1、W2、W5、W6 我完全同意；W4 同意但重要性较低；W3 部分反驳——loss weight schedule 不在核心 causal pathway 上，且论文已在 Limitations 中提及。\n\n两位 Reviewer 的共识焦点：**统计功效不足**和**v1 content irrelevance 不可作为确立结论**是最需要优先解决的问题。\n",
  "reviewer_id": "2",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 交叉回应：对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix\n\n**[AGREE] R1-N1: Content irrelevance 声明缺乏同代码库证据**\n完全同意。我在自己的报告中将此列为 W1（Should-Fix），但经 R1 更详细的论证后，我认同将其升级为 Must-Fix 是合理的。关键证据链：(1) v1→v2 Full OCC CAR 从 0.797 降至 0.725（7.2pp shift，Appendix E）；(2) v1 的 crossover 效应模式在 v2 下完全消失（Appendix E: \"the normalization × gradient flow pattern appeared as a crossover (p=0.025); under v2, both rows slope in the same direction\"）；(3) Discussion line 13 自己承认 \"whether it persists under v2 remains open\"。在 v1 代码存在已知 bug 且定性结论已因 bug 修复而翻转的情况下，将 v1-only 的 content irrelevance 发现写入 Abstract 和 Contribution list 是不当的。R1 提出的两个修复方案（v2 重训 or 降级为 preliminary observation）均合理。\n\n**[AGREE] R1-N2: 统计功效不足以支撑 \"large effect\" 因果声明**\n完全同意。我在自己的报告中将此列为 N1（最高优先级 Must-Fix）。补充 R1 的分析：除了 Hedges' g 校正（R1 估计 d=0.93 校正为 g≈0.76-0.81）之外，n=3 时 Cohen's d 的 95% CI 极宽。对于 d=0.93, n₁=n₂=3，非中心 t 分布的近似 95% CI 约为 [-0.8, 2.7]，即不能排除零效应甚至反向效应。正文使用 \"degrades\"（Discussion line 5: \"gradient flow drops CAR below the Vanilla baseline\"）这类因果语言，超出了关联性证据的支撑范围。此外，ANOVA 两个主效应的 p-values（0.104 和 0.060）在任何常规标准下均不显著，论文主要靠效应量叙事来回避这一事实。\n\n**[REBUT] R1-N3: Table 中 Random OCC (v1) 位置误导**\n部分反驳。根据我对 PDF 第 5 页的阅读，Random OCC 确实位于 midrule **以下**的 supplementary 区域，并标注了 ★v1 code，ΔCAR 列显示 \"---\"（因 cross-codebase mismatch 不做差值比较）。我在自己的审查中将 R1-W5 标记为 [CONFIRMED_RESOLVED]，理由正是 Random OCC 已被正确隔离到 v1 supplementary section。\n\n但 R1 指出的**实质性问题**是成立的：即使分区正确，v1 Random OCC（CAR 0.789）和 v2 Full OCC（CAR 0.725）在同一表格中视觉上可比较，读者可能忽略 ★ 标记而直接比较数值，得到 6.4pp 差异的误导结论（同 codebase 差异仅 0.8pp）。建议的折中方案：保持当前分区，但在 table caption 中增加一句 \"v1 and v2 rows are not directly comparable due to codebase differences (see Appendix E)\"。\n\n将此条从 critical 降级为 warning 更合适——因为 midrule 分区、★ 标记和 ΔCAR=\"---\" 已提供了合理的防误读措施，只是不够醒目。\n\n---\n\n## Should-Fix\n\n**[AGREE] R1-W1: Factorial 设计不完整**\n同意。论文 Introduction 声称 \"twelve conditions varying five factors\"，但实际的完整 factorial crossing 仅限于 2×2（gradient flow × normalization）。Label content 仅在 BN + gradient flow ON 下测试（Full OCC vs Random OCC，均为 v1），未在 LN 或 Detach 条件下测试。Reference frame（BEV vs Depth）同样仅在 BN + gradient flow ON 下测试。Temporal extent 仅在 BN 下测试。这不是 5-factor factorial，而是 \"2×2 factorial core + 8 个单因子 ablations\"。论文 Method Section 3.1 的措辞应修正——\"systematic factorial comparison\" 仅适用于 2×2 核心，其余为单因子 ablation。我在自己报告中的 W4 也指出 Contribution 2 将 factorial methodology 列为独立贡献不恰当，此条进一步支持该观点。\n\n**[AGREE] R1-W2: Cohen's d 小样本偏差未校正**\n同意。Hedges' g 是小样本效应量报告的标准做法（Hedges, 1981），尤其在 n<20 时 Cohen's d 的正向偏差不可忽略。R1 给出的校正因子 J ≈ 0.82-0.87 合理（对 n₁=n₂=3，J = 1 - 3/(4(n₁+n₂-2)-1) ≈ 0.81）。d=0.93 校正后约 g≈0.75，从 \"large\" 边界滑入 \"medium-to-large\"。这不改变效应方向但改变叙事力度，论文应在 main text 报告 Hedges' g。\n\n**[REBUT] R1-W3: λ(t) 指数衰减的功能形式未论证**\n部分反驳。R1 的建议（测试 linear/step/cosine）在理论上有意义，但论文的核心发现是关于 gradient flow pathway（ON vs OFF）和 normalization type（BN vs LN）的交互，而非 loss weight schedule 的影响。λ(t) 衰减只控制 auxiliary gradient 的幅度随时间的变化，而 BN/LN 差异作用于 normalization statistics 的耦合机制——这两者在不同的 causal pathway 上。此外，Appendix 的 temporal analysis（Cutoff series）已间接涉及 gradient flow 持续时间的影响。将此列为 Should-Fix 偏重；作为 Limitations 中的 future work 更合适（论文 Appendix H 最后一句已提及：\"we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules\"）。\n\n**[AGREE] R1-W4: 碰撞检测阈值 10⁻³ 的合理性和敏感性未讨论**\n同意，但重要性较低。论文 Method Section 3.2 和 Appendix B 提到 \"a collision is registered when the L1 displacement of the obstacle's body_xpos exceeds 10⁻³\"，但未解释 10⁻³ 对应的物理尺度（是 mm？cm？MuJoCo 单位？），也未做阈值敏感性分析（如 10⁻², 10⁻⁴ 下结果是否一致）。不过这是 SafeLIBERO benchmark 自身定义的阈值（cite [14] hu2025vlsa），论文只是沿用而非自定义，责任主要在 benchmark 一方。建议在 Appendix 中添加一句物理尺度解释即可。\n\n**[AGREE] R1-W5: BN running statistics 假说缺乏直接证据**\n完全同意。我在自己报告中将此列为 W5 并提出了几乎相同的实验建议（eval mode、momentum=0 消融）。Discussion 的 BN hypothesis 是合理的推测，但论文既声称发现了 \"normalization-dependent gradient flow effect\" 作为核心贡献，又未验证所提出的机制，形成了 claim-evidence gap。在 v2 codebase 下固定 BN running statistics 是低成本实验，应执行。\n\n**[AGREE] R1-W6: 单一 benchmark + 单一架构限制泛化性**\n完全同意。我在自己报告中将此列为 W2（Should-Fix）。Abstract 的 \"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer?\" 是关于整个 VLA 类别的问题，但实验仅覆盖 OpenVLA-7B + OFT + LoRA rank 32 + SafeLIBERO Level I。Conclusion 的 \"Practitioners should omit auxiliary spatial heads\" 作为无限定条件的建议过于宽泛。R1 的建议（在 Abstract/Conclusion 加限定）与我建议的修改 title 一致。\n\n---\n\n## 总结\n\nR1 的 3 条 Must-Fix 中，N1（content irrelevance v1-only）和 N2（统计功效）与我的核心关切高度一致，我认为这是论文最大的两个问题。N3（Random OCC 表格位置）的实质关切成立但严重性不及 critical——当前标注措施（★、---、midrule 分区）已部分缓解，但需加强 caption 提示。\n\nR1 的 6 条 Should-Fix 中，W1、W2、W5、W6 我完全同意；W4 同意但重要性较低；W3 部分反驳——loss weight schedule 不在核心 causal pathway 上，且论文已在 Limitations 中提及。\n\n两位 Reviewer 的共识焦点：**统计功效不足**和**v1 content irrelevance 不可作为确立结论**是最需要优先解决的问题。\n",
    "reviewer_id": "2",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-28T10:58:16.185930+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4017
}
```

</details>

---

### Assistant

_source line 96 · 2026-05-28T10:58:21.672422+00:00_

交叉回应已提交。对 R1 的 9 条意见：6 条 [AGREE]，2 条 [REBUT]（N3 表格位置的事实性争议、W3 loss schedule 不在核心因果路径上），1 条 [AGREE 但降低优先级]（W4 阈值问题）。两位 Reviewer 的核心共识：统计功效不足和 v1 content irrelevance 不可作为确立结论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2"
}
```

</details>

---

## Round 3

84 recorded events

### User

_source line 97 · 2026-05-28T11:34:45.659717+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2（贡献度与完整性）

### 论文信息
- **标题**: Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? An Empirical Investigation
- **目标 venue**: CoRL 2026（10th Conference on Robot Learning）
- **Deadline**: 2026-05-28
- **页数限制**: 正文 ≤ 8 页（致谢/参考文献/附录不计入）
- **匿名**: Double-blind
- **必须**: Limitations section 计入正文 8 页
- **页脚要求**: "10th Conference on Robot Learning (CoRL 2026), Austin, Texas, USA."
- **论文路径**: projects/occsafe_vla/docs/paper/main.tex
- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/submitted.pdf

### 你的审查侧重：贡献度与完整性

请重点审查以下方面：

1. **Novelty 评估**：这是一篇 empirical investigation（负面/警示结果），其贡献（normalization-dependent gradient flow effect + factorial methodology）是否达到 CoRL 顶会标准？"auxiliary spatial supervision doesn't improve safety" 这一发现的影响力如何？
2. **Related work 覆盖度**：
   - 空间 VLA 文献（SpatialVLA, DepthVLA, OccVLA 等 15+ 方法）是否全面引用？
   - Multi-task gradient dynamics（PCGrad, CAGrad, GradNorm 等）讨论是否充分？
   - VLA 安全相关工作（VLSA, SafeVLA, CoFreeVLA 等）是否遗漏重要方法？
   - 是否存在直接竞争的同期工作未被引用？
3. **写作质量**：
   - Abstract 是否准确反映了论文发现（特别是 "v2 verification pending" 等 caveat）？
   - 论文结构是否合理？Discussion 与 Results 是否有重复？
   - 行文是否清晰，是否存在过度/不足的声明？
4. **格式合规性（CoRL 2026）**：
   - 正文是否超过 8 页？（Conclusion 结束于 p9 上方，参考文献始于 p9）
   - Limitations section 在附录（Section H）而非正文——是否违反 CoRL 要求？
   - 页脚是否符合 "10th Conference on Robot Learning (CoRL 2026), Austin, Texas, USA." 格式？
   - 匿名是否完整？
5. **可复现性**：训练超参、评估协议、代码/数据的可获取性描述是否充分？
6. **图表质量**：Figure 1-5, Table 1-7 的信息密度、可读性、是否有冗余？

请按 Strengths / Weaknesses / Questions / Missing References 格式输出审稿意见，每个 Weakness 标注严重程度（[Critical] / [Major] / [Minor]）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-28T11:34:53.974259+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-28T11:34:55.279250+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/.claude/sessions/review_reviewer_2_59f1dca7.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1304
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-28T11:34:55.279584+00:00_

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
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
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

_source line 101 · 2026-05-28T11:34:55.330034+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-28T11:34:59.941544+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-28T11:35:02.362654+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/submitted.pdf",
  "project": "occsafe_vla",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/submitted.pdf",
    "project": "occsafe_vla",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-28T11:35:07.643930+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"}]

Based on the search results, I found some information about CoRL 2026, though specific detailed reviewer guidelines and review form criteria appear to be limited in the search results. Here's what I found:

## CoRL 2026 Reviewer Requirements

All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal.

## Review Criteria (from CoRL 2024)

While specific 2026 review form criteria weren't detailed in the results, the most recent available review criteria from CoRL 2024 indicates that submissions will be evaluated based on the significance and novelty of the results, either theoretical or empirical.

From CoRL 2023's reviewer guidelines, key evaluation areas included:

- Relevance: whether the paper addresses a problem in robot learning, applies or improves a learning-based method or learned model, and whether the method is evaluated in simulation, on real robots, o
…[truncated 545 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7702
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-28T11:35:08.974753+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 319.9}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 370.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 380.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 362.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 357.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 349.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 261.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 389.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p9.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 337.1}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_v
…[truncated 339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6612
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-28T11:35:17.006096+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, scoring dimensions, rating scales, and all evaluation guidelines for CoRL reviewers. Include all specific questions reviewers must answer, the rating scale descriptions, and any special instructions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, scoring dimensions, rating scales, and all evaluation guidelines for CoRL reviewers. Include all specific questions reviewers must answer, the rating scale descriptions, and any special instructions."
  }
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-28T11:35:18.414525+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract all review criteria, scoring dimensions, rating scales, and evaluation guidelines. Include specific questions reviewers must answer and any rubrics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract all review criteria, scoring dimensions, rating scales, and evaluation guidelines. Include specific questions reviewers must answer and any rubrics."
  }
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-28T11:35:19.869632+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/submitted.pdf",
  "project": "occsafe_vla",
  "pages": "11-19",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/submitted.pdf",
    "project": "occsafe_vla",
    "pages": "11-19",
    "dpi": "150"
  }
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-28T11:35:20.271349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-28T11:35:21.181870+00:00_

# CoRL 2024 Review Criteria Summary

Based on the provided content, the document outlines **review criteria and desk rejection guidelines** but does not include a complete review form with specific scoring dimensions or rating scales.

## Available Review Guidance

**Evaluation Focus for Regular Papers:**
The instruction states that submissions will be assessed on "the significance and novelty of the results, either theoretical or empirical" and considers "the degree to which they have been objectively established and/or their potential for scientific and technological impact, as well as their relevance to robotic learning."

**Scope Requirements:**
All CoRL submissions must demonstrate robot learning relevance through either:
- **Intent**: Explicitly addressing a learning question for physical robots, OR
- **Outcome**: Testing the proposed learning solution on physical robots

**Desk Rejection Grounds:**
Papers may be rejected at desk level for formatting issues, anonymity violations, or scope misalignment (such as lacking learning components or lacking robotic application).

## Limitations

The document does not provide:
- Specific numerical rating scales
- Detailed evaluation questions reviewers must answer
- Structured scoring rubrics
- Detailed assessment dimensions beyond significance and novelty

To obtain the complete review form, you would need to access the full submission platform or contact the CoRL 2024 organizing committee directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4175
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-28T11:35:21.182415+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-28T11:35:21.735740+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-28T11:35:22.189572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-28T11:35:22.591302+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-28T11:35:23.495026+00:00_

# CoRL 2023 Review Criteria and Evaluation Guidelines

## Primary Evaluation Dimensions

The reviewer guidelines specify six core assessment areas:

1. **Originality**: "Are the problems or methods new?" Reviewers assess novelty and whether the work represents a legitimate advancement or combination of existing techniques while properly citing related work.

2. **Quality**: Reviewers evaluate technical soundness, whether claims receive adequate support through theory or experiments, methodological appropriateness, and the authors' honesty in discussing both strengths and weaknesses.

3. **Clarity**: Assessment focuses on writing quality, organization, and whether the paper provides sufficient detail for expert reproducibility of results.

4. **Significance**: Determines whether results matter and could influence future research or practical applications in demonstrating state-of-the-art advancement.

5. **Relevance**: Examines whether the submission addresses robot learning problems using learning-based methods and whether the CoRL audience would find value in it.

6. **Limitations**: Reviewers should appreciate honestly disclosed limitations while critically identifying unreported shortcomings that impact the work's validity.

## Review Structure

The main review section asks reviewers to first provide a "Summary of Paper" restating contributions in their own words, then evaluate the paper using the six dimensions above.

**Note**: The document does not specify numerical rating scales, specific scoring rubrics, or detailed scoring ranges for these dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5080
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-28T11:35:24.351708+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p11.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 339.7}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p12.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 55.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p13.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 313.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p14.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 321.9}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p15.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 316.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p16.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 292.6}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p17.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 314.3}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p18.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 272.2}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p19.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 96.1}], \"total_pages\": 19, \"rendered_pages\": 9, \"dpi\": 150, \"output_dir\": 
…[truncated 146 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4482
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-28T11:35:26.620990+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4885
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-28T11:35:26.773714+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6502
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-28T11:35:26.826526+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5644
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-28T11:35:26.829153+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4639
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-28T11:35:26.831485+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4240
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-28T11:35:32.668311+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-28T11:35:33.071152+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-28T11:35:33.121779+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-28T11:35:33.575235+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-28T11:35:33.625852+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-28T11:35:34.028978+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-28T11:35:34.080249+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-28T11:35:34.635112+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-28T11:35:34.635548+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-28T11:35:35.089458+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-28T11:35:45.226832+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-28T11:35:46.134034+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-28T11:35:46.134445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-28T11:35:46.637006+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-28T11:35:46.637421+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-28T11:35:47.090930+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-28T11:35:47.091426+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-28T11:35:47.547485+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-28T11:35:47.598084+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-28T11:35:47.950935+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-28T11:35:53.468945+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-28T11:35:53.871807+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-28T11:35:53.872136+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-28T11:35:54.376250+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-28T11:35:54.376651+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-28T11:35:54.931933+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 555
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-28T11:35:55.484985+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-28T11:35:55.838240+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-28T11:37:23.428481+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SpatialVLA DepthVLA OccVLA spatial vision language action model 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SpatialVLA DepthVLA OccVLA spatial vision language action model 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-28T11:37:23.880152+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PCGrad CAGrad GradNorm multi-task gradient conflict optimization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PCGrad CAGrad GradNorm multi-task gradient conflict optimization"
  }
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-28T11:37:25.034839+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SafeVLA VLSA CoFreeVLA VLA safety collision avoidance robot learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SafeVLA VLSA CoFreeVLA VLA safety collision avoidance robot learning 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-28T11:37:25.035246+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 paper format limitations section requirement page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 paper format limitations section requirement page limit"
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-28T11:37:30.241743+00:00_

Web search results for query: "SpatialVLA DepthVLA OccVLA spatial vision language action model 2024 2025"

Links: [{"title":"DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning","url":"https://www.researchgate.net/publication/396516974_DepthVLA_Enhancing_Vision-Language-Action_Models_with_Depth-Aware_Spatial_Reasoning"},{"title":"DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning","url":"https://arxiv.org/html/2510.13375v1"},{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models","url":"https://spatialvla.github.io/"},{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models | Request PDF","url":"https://www.researchgate.net/publication/395370588_SpatialVLA_Exploring_Spatial_Representations_for_Visual-Language-Action_Models"},{"title":"GitHub - SpatialVLA/SpatialVLA: 🔥 SpatialVLA: a spatial-enhanced vision-language-action model that is trained on 1.1 Million real robot episodes. Accepted at RSS 2025.","url":"https://github.com/SpatialVLA/SpatialVLA"},{"title":"OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision","url":"https://arxiv.org/html/2509.05578v1"},{"title":"[2501.15830] SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model","url":"https://arxiv.org/abs/2501.15830"}]

Based on the search results, here's what I found about these spatial vision-language-action models from 2024-2025:

## SpatialVLA

SpatialVLA is a spatial-enhanced vision-language-action model trained on 1.1 Million real robot episodes, and it was accepted at RSS 2025. SpatialVLA introduces egocentric 3D position encodings that does not rely on camera extrinsics. SpatialVLA achieves state-of-the-art performance across a diverse range of evaluations and shows significantly faster inference speed with fewer tokens per action.

## DepthVLA

DepthVLA is a VLA architecture that explicitly incorporates spatial awareness 
…[truncated 814 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6813
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-28T11:37:30.242141+00:00_

Web search results for query: "CoRL 2026 paper format limitations section requirement page limit"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"}]

Based on the search results for CoRL 2026 paper format requirements:

The page limit for the main paper is 8 pages, and acknowledgments, references, and appendix (optional) will not count towards the page limit.

Regarding the Limitations section requirement: All submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments, and how these might be addressed in the future.

So in summary, the Limitations section is **required** and **does count toward** the 8-page main paper limit for CoRL 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5206
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-28T11:37:33.560944+00:00_

Web search results for query: "SafeVLA VLSA CoFreeVLA VLA safety collision avoidance robot learning 2024 2025"

Links: [{"title":"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation","url":"https://arxiv.org/pdf/2601.21712"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Safe Reinforcement Learning","url":"https://arxiv.org/html/2503.03480v1"},{"title":"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation","url":"https://arxiv.org/html/2601.21712v2"},{"title":"(PDF) VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://www.researchgate.net/publication/398721287_VLSA_Vision-Language-Action_Models_with_Plug-and-Play_Safety_Constraint_Layer"},{"title":"SafeVLA: Towards Safety Alignment of Vision- Language-Action Model via Constrained Learning","url":"https://arxiv.org/html/2503.03480v2"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer [Quick Review]","url":"https://liner.com/review/vlsa-visionlanguageaction-models-with-plugandplay-safety-constraint-layer"},{"title":"[2503.03480] SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning","url":"https://arxiv.org/abs/2503.03480"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://vlsa-aegis.github.io/"}]

Based on the search results, here's what I found about these Vision-Language-Action (VLA) safety approaches:

## **SafeVLA**

SafeVLA is an algorithm designed to integrate safety into VLAs, ensuring the protection of the environment, robot hardware and humans in real-world settings. It uses an integrated safety approach (ISA) that systematically models safety requirements, then actively elicits diverse unsafe behaviors, effectively constraining VLA policies via safe reinforcement learning. SafeVLA effectively balances safety a
…[truncated 1081 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8526
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-28T11:37:38.629439+00:00_

Web search results for query: "PCGrad CAGrad GradNorm multi-task gradient conflict optimization"

Links: [{"title":"Gradient Interference-Aware Graph Coloring for Multitask Learning","url":"https://arxiv.org/html/2509.16959v1"},{"title":"GCond: Gradient Conflict Resolution via Accumulation-based Stabilization for Large-Scale Multi-Task Learning","url":"https://arxiv.org/html/2509.07252v1"},{"title":"GCond: Gradient Conflict Resolution via Accumulation-based Stabilization for Large-Scale Multi-Task Learning","url":"https://arxiv.org/pdf/2509.07252"},{"title":"[2509.07252] GCond: Gradient Conflict Resolution via Accumulation-based Stabilization for Large-Scale Multi-Task Learning","url":"https://arxiv.org/abs/2509.07252"},{"title":"[2509.07252v1] GCond: Gradient Conflict Resolution via Accumulation-based Stabilization for Large-Scale Multi-Task Learning","url":"https://arxiv.org/abs/2509.07252v1"},{"title":"Gradient Surgery for Multi-Task Learning","url":"https://proceedings.neurips.cc/paper/2020/file/3fe78a8acf5fda99de95303940a2420c-Paper.pdf"},{"title":"Multi-Task Optimization in Neural Networks: Theory and Practice","url":"https://mlfrontiers.substack.com/p/multi-task-optimization-in-neural"},{"title":"Conflict-Averse Gradient Descent for Multi-task Learning","url":"https://arxiv.org/pdf/2110.14048"},{"title":"Gradient Descent in Multi-Task Learning Stanford CS224N Default Project","url":"https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/final-projects/DavidSaykinKfirShmuelDolev.pdf"}]

Based on the search results, here's information about PCGrad, CAGrad, and GradNorm in the context of multi-task gradient conflict optimization:

## Overview

Gradient conflict poses a significant challenge in multi-task learning (MTL), and effective methods for addressing this problem, including PCGrad, CAGrad, and GradNorm, are computationally demanding in their original implementations, which limits their application in modern large models and transformers.

## Key Meth
…[truncated 1466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 14749
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-28T11:37:50.276412+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract ALL formatting requirements including: page limits, limitations section requirements, anonymity rules, footer text requirements, font requirements, and any other submission format rules. Be comprehensive and exact."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/instruction-for-authors",
    "prompt": "Extract ALL formatting requirements including: page limits, limitations section requirements, anonymity rules, footer text requirements, font requirements, and any other submission format rules. Be comprehensive and exact."
  }
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-28T11:37:51.532089+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"3D-CoVLA\" OR \"AugVLA\" OR \"ObjVLA\" OR \"CrossFLA\" vision language action model spatial"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"3D-CoVLA\" OR \"AugVLA\" OR \"ObjVLA\" OR \"CrossFLA\" vision language action model spatial"
  }
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-28T11:37:55.198449+00:00_

# CoRL 2026 Formatting Requirements Summary

## Page Limits
- **Initial submission:** 8 pages maximum for main paper
- **Camera-ready submission:** 9 pages maximum for main text
- Acknowledgments, references, and appendix do not count toward page limits
- Video supplement: maximum 250 MB, suggested 3 minutes or less

## Content Requirements
- **Limitations section:** mandatory, counted within the 8-page limit, must explicitly describe limiting assumptions, failure modes, and potential future improvements
- **Anonymity:** double-blind for initial review; author names removed from submissions but included in camera-ready version

## Camera-Ready Specifications
- Footer on first page must read: "10th Conference on Robot Learning (CoRL 2026), Austin, Texas, USA."
- Use provided LaTeX template with `\usepackage[final]{corl_2026}`
- "Text density, fonts, and spacing should be the same as the provided template"
- "The margin should be the same as the provided template"
- OpenReview title must match PDF title exactly

## Supplementary Materials
- Submit as single zip file through OpenReview
- Appendix may be included with main paper or supplementary materials
- Reviewers not required to read appendix
- Videos, code, datasets should be hosted externally with links provided in main text

## Additional Policies
- No fabricated citations permitted
- Disclose generative AI tool usage during submission
- No dual submissions to other archival venues without prior approval

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4922
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-28T11:37:57.003229+00:00_

Web search results for query: ""3D-CoVLA" OR "AugVLA" OR "ObjVLA" OR "CrossFLA" vision language action model spatial"

Links: [{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models | Request PDF","url":"https://www.researchgate.net/publication/395370588_SpatialVLA_Exploring_Spatial_Representations_for_Visual-Language-Action_Models"},{"title":"AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2602.10698"},{"title":"Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding","url":"https://arxiv.org/pdf/2507.00416"},{"title":"AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.10698v1"},{"title":"From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors","url":"https://arxiv.org/pdf/2510.17439"},{"title":"[2602.10698] AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models","url":"https://arxiv.org/abs/2602.10698"},{"title":"AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/resources/2602.10698v1"},{"title":"3D CAVLA: Leveraging Depth and 3D Context to Generalize Vision Language Action Models for Unseen Tasks","url":"https://arxiv.org/pdf/2505.05800"}]

Based on the search results, here's what I found about these vision-language-action models with spatial understanding:

## AugVLA-3D

AugVLA-3D is a Vision-Language-Action (VLA) model framework that addresses the limitation of approaches that primarily rely on 2D images, which restricts their spatial understanding and action grounding in complex 3D environments. The framework integrates depth estimation into VLA models to enrich 3D feature representations, using a depth estimation baseline called VGGT to extract geometry-aware 3D cues from standard RGB inputs, enabling efficient utilization of existing large-scale 2D datas
…[truncated 880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5471
}
```

</details>

---

### Tool call

_source line 162 · 2026-05-28T11:40:51.447578+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/submitted.pdf",
  "project": "occsafe_vla",
  "pages": "1",
  "dpi": "165",
  "output_dir": "/tmp/occsafe_hires"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/submitted.pdf",
    "project": "occsafe_vla",
    "pages": "1",
    "dpi": "165",
    "output_dir": "/tmp/occsafe_hires"
  }
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-28T11:40:51.949820+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/tmp/occsafe_hires/submitted_p1.png\", \"width\": 1403, \"height\": 1815, \"size_kb\": 361.9}], \"total_pages\": 19, \"rendered_pages\": 1, \"dpi\": 165, \"output_dir\": \"/tmp/occsafe_hires\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-28T11:40:52.501970+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/submitted.pdf",
  "project": "occsafe_vla",
  "pages": "9",
  "dpi": "165",
  "output_dir": "/tmp/occsafe_hires_p9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/submitted.pdf",
    "project": "occsafe_vla",
    "pages": "9",
    "dpi": "165",
    "output_dir": "/tmp/occsafe_hires_p9"
  }
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-28T11:40:52.653552+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/tmp/occsafe_hires_p9/submitted_p9.png\", \"width\": 1403, \"height\": 1815, \"size_kb\": 386.7}], \"total_pages\": 19, \"rendered_pages\": 1, \"dpi\": 165, \"output_dir\": \"/tmp/occsafe_hires_p9\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-28T11:40:55.616855+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/occsafe_hires/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/occsafe_hires/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-28T11:40:55.617355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/occsafe_hires_p9/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/occsafe_hires_p9/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-28T11:40:56.322701+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 705
}
```

</details>

---

### Tool result

_source line 169 · 2026-05-28T11:40:56.380987+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 763
}
```

</details>

---

### Tool call

_source line 170 · 2026-05-28T11:45:04.348615+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见 — Round 1（贡献度与完整性）\n\n**论文**: Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? An Empirical Investigation\n**Venue**: CoRL 2026\n\n---\n\n## 总体评分\n**Overall**: 4/10（倾向拒稿，存在多项 critical 问题需解决）\n**一句话总结**: 研究问题有价值、实验设计方法论较为严谨，但存在格式硬伤（Limitations 不在正文、页数超限）、核心发现的 \"v2 verification pending\" 严重削弱可信度，且单一模型/单一基准测试的范围过窄难以支撑其一般性声明。\n\n---\n\n## 官方维度打分（基于 CoRL 2023 Reviewer Guidelines 六维度）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 2/5 | 负面结果本身有价值，但 normalization-gradient flow 交互本质上是 multi-task learning 已知现象在 VLA 场景的复现，novelty 有限 |\n| Quality | 2.5/5 | Factorial 方法论严谨、统计分析（ANOVA + Cohen's d + CKA）扎实，但 n=3–4 seeds、v2 未验证、scope 过窄显著削弱结论强度 |\n| Clarity | 3/5 | 行文总体清晰，abstract 数据丰富；但 Discussion 与 Results 有重复，\"v2 verification pending\" 应更显著标注 |\n| Significance | 2/5 | 发现局限于 OpenVLA-7B + LoRA + SafeLIBERO 这一特定组合，难以外推；对社区的实际影响有限 |\n| Relevance | 4/5 | VLA 安全性是 CoRL 核心关注话题，研究问题高度相关 |\n| Limitations | 2/5 | Limitations 诚实详尽（Appendix H），但放在附录违反 CoRL 格式要求，应在正文 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [Critical] **Limitations section 不在正文，违反 CoRL 2026 格式要求**\n- 具体位置：Appendix H（pp.18–19）\n- 问题：CoRL 2026 Author Instructions 明确要求：\"All submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations.\" 本文将 Limitations 完全放在附录，不在正文 8 页内，属于格式违规。\n- 为什么影响接收：这是 desk rejection 级别的格式问题。CoRL 对 Limitations 的要求是硬性的——审稿人被明确告知 Limitations 必须在正文中。\n- 建议修改方向：将 Appendix H 的核心内容（至少关于 codebase version caveat、LoRA specificity、binary metric 局限、sample size）压缩后移入正文 Section 5 (Discussion) 末尾或 Section 6 (Conclusion) 之前，并相应压缩正文其他部分以满足页数限制。\n\n**N2** [Critical] **正文页数超过 8 页**\n- 具体位置：Section 6 (Conclusion) 位于第 9 页上方约 1/3 处，References 始于第 9 页\n- 问题：CoRL 2026 要求 \"8 pages maximum for main paper\"（acknowledgments, references, appendix 不计入）。当前 Sections 1–6 延伸至第 9 页，超出限制约 0.3 页。加上若将 Limitations 移入正文（N1 要求），页数压力更大。\n- 为什么影响接收：页数超限同样是 desk rejection 依据。\n- 建议修改方向：(1) 压缩 Discussion（Section 5）与 Results（Section 4）的重复内容——当前 Discussion 的多个要点（如 \"Normalization independently affects safety\"、\"Additive protection model\"）与 Section 4 高度重叠；(2) 考虑将 Table 1（12 条件全表）移入附录，正文仅保留 2×2 factorial 核心结果（Table 3）；(3) Figure 2 占据约半页，可考虑压缩。\n\n**N3** [Critical] **\"v2 verification pending\" 严重削弱核心发现可信度**\n- 具体位置：Abstract 第 12–13 行（\"no detectable effect on safety in preliminary v1 experiments (v2 verification pending)\"）；Section 6 Conclusion（\"spatial label content showed no detectable effect under the v1 codeline (v2 verification pending)\"）\n- 问题：论文的核心声明之一是 \"spatial label content (ground truth occupancy, random binary labels, egocentric depth maps) showed no detectable effect on safety\"。但这一发现被标注为 v1 实验、v2 尚未验证。对于一篇以实证结果为核心贡献的论文，呈现未经验证的结果是根本性问题——如果 v2 验证推翻了 v1 发现，论文的主要结论将不成立。\n- 为什么影响接收：(1) 审稿人无法评估一个作者自己都不确定的结论；(2) \"preliminary\" + \"pending\" 的措辞表明作者对结果的置信度不足；(3) v1 代码可能存在 bug 或实现缺陷导致 spatial content 无效果的假象。\n- 建议修改方向：要么 (a) 在投稿前完成 v2 验证并更新结果，要么 (b) 明确降级该发现为 \"preliminary observation\"，不将其作为论文的核心贡献之一呈现在 abstract/conclusion 中，并在正文 Limitations 中详细讨论 v1→v2 的差异风险。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Major] **泛化性严重受限：单模型 × 单基准 × 单训练配方**\n- 具体位置：Section 3（Method）；Appendix H Limitations\n- 问题：全部实验基于 OpenVLA-7B + OFT/LoRA 微调 + SafeLIBERO Level 1（7 tasks）。论文在 Discussion（p.8）提到 \"LoRA specificity caveat\"，在 Limitations（Appendix H）承认 \"our study uses a single architecture (OpenVLA OFT with LoRA rank 32)\"。然而论文的 practical guidelines（\"detach auxiliary gradients under BN architectures; gradient flow is safe under LN\"）以一般性口吻呈现，隐含可推广至其他 VLA 架构。\n- 建议：(1) 至少在第二个 VLA 模型（如 Octo、RT-2-X、π0）上验证 normalization-gradient flow 交互效应是否成立；(2) 如无法扩展实验，需在正文 guidelines 中明确限定适用范围为 \"OpenVLA-like LoRA fine-tuning\"；(3) 考虑在第二个基准测试（如 CALVIN、RLBench）上验证。\n\n**W2** [Major] **样本量不足，统计推断可靠性存疑**\n- 具体位置：Section 3.2（\"Each cell runs 50 rollouts per task\"）；Appendix F（Table 6: 2×2 factorial ANOVA）；Appendix H（\"n=3–4 seeds per cell, 14 total observations\"）\n- 问题：每个条件仅 3–4 个训练 seed。Cohen's d 的采样分布在小样本下极宽——例如 d=0.93（N1 中的 gradient flow effect）的 95% 置信区间在 n=3–4 时可能跨越 [−0.5, 2.4]。虽然论文报告了效应量而非仅 p 值（这是好的实践），但点估计的可靠性令人担忧。Appendix F 的 ANOVA（14 total observations, 2×2=4 cells）每个 cell 仅 3–4 个数据点，统计功效很低。\n- 建议：(1) 至少增加到 5–8 seeds 以缩小置信区间；(2) 在正文报告 Cohen's d 的置信区间而非仅点估计；(3) 如果计算资源有限，优先对 2×2 factorial 的 4 个 cell 增加 seeds，而非维持 12 个条件全覆盖。\n\n**W3** [Major] **Novelty 定位问题：normalization-gradient flow 交互是 multi-task learning 已知效应**\n- 具体位置：Section 2.2（Related Work on Multi-Task Gradient Dynamics）；Section 4.2–4.3\n- 问题：BatchNorm running statistics 被 auxiliary task gradients 扰动导致性能下降，这在 multi-task learning 文献中是已知现象。论文引用了 PCGrad [32]、CAGrad [33]、GradNorm [31] 等方法，但未充分区分本文的发现与这些已知效应的关系。具体而言：(1) Ioffe & Szegedy [36] 的 BatchNorm 论文和后续的 domain adaptation 文献（如 Li et al. \"Revisiting Batch Normalization for Practical Domain Adaptation\"）已讨论了 BN statistics shift 的问题；(2) ForkMerge [35] 明确处理 auxiliary task 的负迁移。本文的 \"normalization-dependent gradient flow effect\" 本质上是 BN statistics corruption 在 VLA 场景的特例。\n- 为什么影响评分：论文将这一发现作为 \"central finding\"，但如果这只是已知 multi-task learning 问题的确认，novelty 不足以支撑顶会贡献。\n- 建议：(1) 在 Related Work 中更深入地讨论 BN statistics shift 在 multi-task/domain adaptation 中的先例；(2) 明确论文的增量贡献是 \"在 VLA fine-tuning 的特定设置下量化了这一效应的严重程度\"，而非发现了新现象；(3) 提供 BN running statistics 的直接测量（如训练过程中 BN mean/variance 的漂移量），而不仅是间接的 CKA 分析。\n\n**W4** [Major] **Related Work 对近期空间 VLA 方法的覆盖度**\n- 具体位置：Section 2.1；References\n- 问题：论文引用了约 11 个空间 VLA 方法（SpatialVLA [7]、DepthVLA [6]、OccVLA [8]、3D-CoVLA [11]、AugVLA-3D [14?]、ST-VLA [9]、GST-VLA [10]、Spatial Fusing [5]、ObjVLA [12?]、GeoVerse [13?]、CrossFLA [15?]），覆盖度尚可。但以下可能遗漏：\n  - **3D-CAVLA**（arXiv 2505.05800, 2025）：使用 depth-aware perception 和 chain-of-thought 推理增强 VLA\n  - **Evo-0**（arXiv 2507.00416）：implicit spatial understanding for VLA\n  - 关于 multi-task gradient 方法，未引用 **MGDA**（Sener & Koltun, NeurIPS 2018, \"Multi-Task Learning as Multi-Objective Optimization\"），这是 PCGrad/CAGrad 的重要前驱工作\n  - 关于 BN statistics 问题的专门文献（如 **AdaBN**、**DSBN**）未在 Related Work 中讨论\n- 建议：补充上述遗漏引用，特别是 MGDA 和 BN domain shift 文献，后者与本文的核心发现直接相关。\n\n**W5** [Major] **Discussion 与 Results 内容重复**\n- 具体位置：Section 4.1–4.3（pp.5–7）vs Section 5（p.8）\n- 问题：Discussion（Section 5）的以下要点与 Results 重叠：\n  - \"Normalization independently affects safety\"（已在 Section 4.2 的 2×2 factorial 分析中完整讨论）\n  - \"Additive protection model\"（已在 Table 3 和 Section 4.2 的 ANOVA 分析中呈现）\n  - \"Mechanism remains open\"（已在 Section 4.3 Gradient Dynamics 中讨论）\n  这种重复导致正文页数膨胀，直接加剧了 N2（页数超限）问题。\n- 建议：合并 Discussion 中与 Results 重复的内容，Discussion 专注于 (1) 与 existing literature 的对比解读、(2) practical implications、(3) open questions。预计可节省 0.3–0.5 页。\n\n---\n\n## 小问题（不影响接收）\n\n- **碰撞指标过于粗糙**：CAR 使用 L1 displacement > 10^{-3} 的二值化阈值（Section 3.2），无法捕捉碰撞严重程度的连续变化。Limitations（Appendix H）提到 \"a continuous safety metric might reveal finer-grained differences\"，但此局限应在正文中提及。\n- **代码/数据可获取性**：论文未提及是否会公开代码、训练日志、模型检查点。对于以可复现性为核心的实证研究，这一信息应在正文中说明（即使是匿名审查阶段也可用 \"code will be released upon acceptance\" 的方式）。\n- **Figure 1 信息密度**：Figure 1 占据约 0.6 页（p.2），其中 (a) training setup 示意图对理解论文贡献并非必需（标准 VLA fine-tuning 架构读者已熟悉），可考虑缩小或移入附录以节省空间。\n- **页脚格式**：当前页脚为 \"Submitted to the 10th Conference on Robot Learning (CoRL 2026). Do not distribute.\"——这是审稿版的正确格式，camera-ready 需改为指定格式，此项合规。\n- **匿名合规**：使用 \"Anonymous Author(s)\" + 占位地址/邮箱，符合 double-blind 要求。\n- **Appendix A（Extended Per-Task Results, Table 4）**：单任务级别的 mean CAR 数据有参考价值，但 Table 4 的 7 tasks × ~10 conditions 的呈现略显杂乱，可考虑用 heatmap 可视化替代。\n- **Cutoff 实验（Appendix D–E）**：仅 1–3 seeds，conclusions 应标注为 \"preliminary\"——目前 Section 4.3 对 cutoff 结果的讨论语气过于确定。\n\n---\n\n## 主要优势\n\n1. **研究问题重要且及时**：随着 SpatialVLA/DepthVLA/OccVLA 等方法大量涌现，系统检验 \"空间 auxiliary supervision 是否改善安全性\" 是一个有价值的问题，且现有文献中无人正面回答。\n2. **Factorial 实验设计**：2×2 核心 factorial（normalization × gradient flow）+ 12 条件扩展设计，比典型的 \"add auxiliary head → report numbers\" 消融研究更有方法论深度。控制变量意识强。\n3. **统计分析超越平均值报告**：使用 ANOVA 分解主效应和交互效应、报告 Cohen's d 效应量、CKA 分析表征层表示变化。这在 robotics 论文中较为少见，体现了严谨的实证研究态度。\n4. **Practical guidelines 清晰可操作**：Abstract 和 Conclusion 提供了直接的工程建议（\"detach under BN; safe under LN; avoid BN + gradient flow\"），即使不完全接受论文的所有结论，这些 heuristics 对从业者有参考价值。\n5. **诚实的 caveat 披露**：明确标注 \"v2 verification pending\"，比隐藏未验证状态更诚实——虽然这反过来也成为 weakness。\n6. **Normalization 效应的独立发现**：LN 一致性地优于 BN 3.5–4.8 pp（large effect size），这一发现不依赖于 auxiliary head 的存在（Vanilla BN vs Vanilla LN 也有差异），具有独立的工程价值。\n\n---\n\n## Questions for Authors\n\nQ1: v2 codeline 与 v1 的具体差异是什么？是 bug fix、架构变更还是数据处理差异？如果是 bug fix，v1 的结果是否可能是 artifact？\n\nQ2: 是否测量了 BN running statistics（mean 和 variance）在训练过程中的实际漂移量？当前的 CKA 分析（Section 4.3, Appendix C）只间接证明了表示没有发生大的结构性变化（CKA > 0.95），但 BN statistics 漂移可以在 CKA 不变的情况下仍然影响下游输出。直接测量 BN stats drift 可以将 \"hypothesis\" 升级为 \"evidence\"。\n\nQ3: 论文使用固定的 loss weight λ₀=0.01（Appendix H, p.19）。是否考虑过 loss weight 对 gradient flow effect 的调节作用？λ₀ 从 0.01 变为 0.001 或 0.1 时，BN + gradient flow 的 safety degradation 是否仍然存在？\n\nQ4: SafeLIBERO Level 1 仅包含 7 个任务，且 \"only static obstacles\"（Appendix H）。如果换用动态障碍物或更复杂的安全场景，normalization-gradient flow 交互效应是否可能改变？\n\nQ5: Table 4（Appendix A）显示不同任务间 CAR 方差很大（如 T1 Easy 0.98 vs T7 Hard 1.00）。这种任务异质性是否意味着 aggregate-level 的 factorial 分析可能掩盖了任务级别的交互效应？\n\n---\n\n## Missing References（建议补充）\n\n1. **Sener & Koltun (2018)**. \"Multi-Task Learning as Multi-Objective Optimization.\" NeurIPS. — PCGrad/CAGrad 的重要前驱，定义了 multi-task gradient conflict 的优化框架。\n2. **Li et al. (2017/2018)**. \"Revisiting Batch Normalization for Practical Domain Adaptation.\" — BN statistics shift 在 domain/task adaptation 中的经典讨论，与本文核心发现直接相关。\n3. **Chang et al. (2019)**. \"Domain-Specific Batch Normalization for Unsupervised Domain Adaptation.\" CVPR. — 多任务场景中 BN 统计量分离的方法论，可作为本文 \"detach gradient\" 策略的理论佐证。\n4. **3D-CAVLA (2025)**. arXiv:2505.05800 — 使用 depth-aware perception 增强 VLA 的近期方法。\n5. **Kendall et al. (2018)**. \"Multi-Task Learning Using Uncertainty to Weigh Losses.\" CVPR. — 用 uncertainty 自动调节 multi-task loss weights 的经典方法，与本文固定 λ₀=0.01 的设计选择形成对照讨论。",
  "reviewer_id": "2",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见 — Round 1（贡献度与完整性）\n\n**论文**: Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? An Empirical Investigation\n**Venue**: CoRL 2026\n\n---\n\n## 总体评分\n**Overall**: 4/10（倾向拒稿，存在多项 critical 问题需解决）\n**一句话总结**: 研究问题有价值、实验设计方法论较为严谨，但存在格式硬伤（Limitations 不在正文、页数超限）、核心发现的 \"v2 verification pending\" 严重削弱可信度，且单一模型/单一基准测试的范围过窄难以支撑其一般性声明。\n\n---\n\n## 官方维度打分（基于 CoRL 2023 Reviewer Guidelines 六维度）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 2/5 | 负面结果本身有价值，但 normalization-gradient flow 交互本质上是 multi-task learning 已知现象在 VLA 场景的复现，novelty 有限 |\n| Quality | 2.5/5 | Factorial 方法论严谨、统计分析（ANOVA + Cohen's d + CKA）扎实，但 n=3–4 seeds、v2 未验证、scope 过窄显著削弱结论强度 |\n| Clarity | 3/5 | 行文总体清晰，abstract 数据丰富；但 Discussion 与 Results 有重复，\"v2 verification pending\" 应更显著标注 |\n| Significance | 2/5 | 发现局限于 OpenVLA-7B + LoRA + SafeLIBERO 这一特定组合，难以外推；对社区的实际影响有限 |\n| Relevance | 4/5 | VLA 安全性是 CoRL 核心关注话题，研究问题高度相关 |\n| Limitations | 2/5 | Limitations 诚实详尽（Appendix H），但放在附录违反 CoRL 格式要求，应在正文 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [Critical] **Limitations section 不在正文，违反 CoRL 2026 格式要求**\n- 具体位置：Appendix H（pp.18–19）\n- 问题：CoRL 2026 Author Instructions 明确要求：\"All submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations.\" 本文将 Limitations 完全放在附录，不在正文 8 页内，属于格式违规。\n- 为什么影响接收：这是 desk rejection 级别的格式问题。CoRL 对 Limitations 的要求是硬性的——审稿人被明确告知 Limitations 必须在正文中。\n- 建议修改方向：将 Appendix H 的核心内容（至少关于 codebase version caveat、LoRA specificity、binary metric 局限、sample size）压缩后移入正文 Section 5 (Discussion) 末尾或 Section 6 (Conclusion) 之前，并相应压缩正文其他部分以满足页数限制。\n\n**N2** [Critical] **正文页数超过 8 页**\n- 具体位置：Section 6 (Conclusion) 位于第 9 页上方约 1/3 处，References 始于第 9 页\n- 问题：CoRL 2026 要求 \"8 pages maximum for main paper\"（acknowledgments, references, appendix 不计入）。当前 Sections 1–6 延伸至第 9 页，超出限制约 0.3 页。加上若将 Limitations 移入正文（N1 要求），页数压力更大。\n- 为什么影响接收：页数超限同样是 desk rejection 依据。\n- 建议修改方向：(1) 压缩 Discussion（Section 5）与 Results（Section 4）的重复内容——当前 Discussion 的多个要点（如 \"Normalization independently affects safety\"、\"Additive protection model\"）与 Section 4 高度重叠；(2) 考虑将 Table 1（12 条件全表）移入附录，正文仅保留 2×2 factorial 核心结果（Table 3）；(3) Figure 2 占据约半页，可考虑压缩。\n\n**N3** [Critical] **\"v2 verification pending\" 严重削弱核心发现可信度**\n- 具体位置：Abstract 第 12–13 行（\"no detectable effect on safety in preliminary v1 experiments (v2 verification pending)\"）；Section 6 Conclusion（\"spatial label content showed no detectable effect under the v1 codeline (v2 verification pending)\"）\n- 问题：论文的核心声明之一是 \"spatial label content (ground truth occupancy, random binary labels, egocentric depth maps) showed no detectable effect on safety\"。但这一发现被标注为 v1 实验、v2 尚未验证。对于一篇以实证结果为核心贡献的论文，呈现未经验证的结果是根本性问题——如果 v2 验证推翻了 v1 发现，论文的主要结论将不成立。\n- 为什么影响接收：(1) 审稿人无法评估一个作者自己都不确定的结论；(2) \"preliminary\" + \"pending\" 的措辞表明作者对结果的置信度不足；(3) v1 代码可能存在 bug 或实现缺陷导致 spatial content 无效果的假象。\n- 建议修改方向：要么 (a) 在投稿前完成 v2 验证并更新结果，要么 (b) 明确降级该发现为 \"preliminary observation\"，不将其作为论文的核心贡献之一呈现在 abstract/conclusion 中，并在正文 Limitations 中详细讨论 v1→v2 的差异风险。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Major] **泛化性严重受限：单模型 × 单基准 × 单训练配方**\n- 具体位置：Section 3（Method）；Appendix H Limitations\n- 问题：全部实验基于 OpenVLA-7B + OFT/LoRA 微调 + SafeLIBERO Level 1（7 tasks）。论文在 Discussion（p.8）提到 \"LoRA specificity caveat\"，在 Limitations（Appendix H）承认 \"our study uses a single architecture (OpenVLA OFT with LoRA rank 32)\"。然而论文的 practical guidelines（\"detach auxiliary gradients under BN architectures; gradient flow is safe under LN\"）以一般性口吻呈现，隐含可推广至其他 VLA 架构。\n- 建议：(1) 至少在第二个 VLA 模型（如 Octo、RT-2-X、π0）上验证 normalization-gradient flow 交互效应是否成立；(2) 如无法扩展实验，需在正文 guidelines 中明确限定适用范围为 \"OpenVLA-like LoRA fine-tuning\"；(3) 考虑在第二个基准测试（如 CALVIN、RLBench）上验证。\n\n**W2** [Major] **样本量不足，统计推断可靠性存疑**\n- 具体位置：Section 3.2（\"Each cell runs 50 rollouts per task\"）；Appendix F（Table 6: 2×2 factorial ANOVA）；Appendix H（\"n=3–4 seeds per cell, 14 total observations\"）\n- 问题：每个条件仅 3–4 个训练 seed。Cohen's d 的采样分布在小样本下极宽——例如 d=0.93（N1 中的 gradient flow effect）的 95% 置信区间在 n=3–4 时可能跨越 [−0.5, 2.4]。虽然论文报告了效应量而非仅 p 值（这是好的实践），但点估计的可靠性令人担忧。Appendix F 的 ANOVA（14 total observations, 2×2=4 cells）每个 cell 仅 3–4 个数据点，统计功效很低。\n- 建议：(1) 至少增加到 5–8 seeds 以缩小置信区间；(2) 在正文报告 Cohen's d 的置信区间而非仅点估计；(3) 如果计算资源有限，优先对 2×2 factorial 的 4 个 cell 增加 seeds，而非维持 12 个条件全覆盖。\n\n**W3** [Major] **Novelty 定位问题：normalization-gradient flow 交互是 multi-task learning 已知效应**\n- 具体位置：Section 2.2（Related Work on Multi-Task Gradient Dynamics）；Section 4.2–4.3\n- 问题：BatchNorm running statistics 被 auxiliary task gradients 扰动导致性能下降，这在 multi-task learning 文献中是已知现象。论文引用了 PCGrad [32]、CAGrad [33]、GradNorm [31] 等方法，但未充分区分本文的发现与这些已知效应的关系。具体而言：(1) Ioffe & Szegedy [36] 的 BatchNorm 论文和后续的 domain adaptation 文献（如 Li et al. \"Revisiting Batch Normalization for Practical Domain Adaptation\"）已讨论了 BN statistics shift 的问题；(2) ForkMerge [35] 明确处理 auxiliary task 的负迁移。本文的 \"normalization-dependent gradient flow effect\" 本质上是 BN statistics corruption 在 VLA 场景的特例。\n- 为什么影响评分：论文将这一发现作为 \"central finding\"，但如果这只是已知 multi-task learning 问题的确认，novelty 不足以支撑顶会贡献。\n- 建议：(1) 在 Related Work 中更深入地讨论 BN statistics shift 在 multi-task/domain adaptation 中的先例；(2) 明确论文的增量贡献是 \"在 VLA fine-tuning 的特定设置下量化了这一效应的严重程度\"，而非发现了新现象；(3) 提供 BN running statistics 的直接测量（如训练过程中 BN mean/variance 的漂移量），而不仅是间接的 CKA 分析。\n\n**W4** [Major] **Related Work 对近期空间 VLA 方法的覆盖度**\n- 具体位置：Section 2.1；References\n- 问题：论文引用了约 11 个空间 VLA 方法（SpatialVLA [7]、DepthVLA [6]、OccVLA [8]、3D-CoVLA [11]、AugVLA-3D [14?]、ST-VLA [9]、GST-VLA [10]、Spatial Fusing [5]、ObjVLA [12?]、GeoVerse [13?]、CrossFLA [15?]），覆盖度尚可。但以下可能遗漏：\n  - **3D-CAVLA**（arXiv 2505.05800, 2025）：使用 depth-aware perception 和 chain-of-thought 推理增强 VLA\n  - **Evo-0**（arXiv 2507.00416）：implicit spatial understanding for VLA\n  - 关于 multi-task gradient 方法，未引用 **MGDA**（Sener & Koltun, NeurIPS 2018, \"Multi-Task Learning as Multi-Objective Optimization\"），这是 PCGrad/CAGrad 的重要前驱工作\n  - 关于 BN statistics 问题的专门文献（如 **AdaBN**、**DSBN**）未在 Related Work 中讨论\n- 建议：补充上述遗漏引用，特别是 MGDA 和 BN domain shift 文献，后者与本文的核心发现直接相关。\n\n**W5** [Major] **Discussion 与 Results 内容重复**\n- 具体位置：Section 4.1–4.3（pp.5–7）vs Section 5（p.8）\n- 问题：Discussion（Section 5）的以下要点与 Results 重叠：\n  - \"Normalization independently affects safety\"（已在 Section 4.2 的 2×2 factorial 分析中完整讨论）\n  - \"Additive protection model\"（已在 Table 3 和 Section 4.2 的 ANOVA 分析中呈现）\n  - \"Mechanism remains open\"（已在 Section 4.3 Gradient Dynamics 中讨论）\n  这种重复导致正文页数膨胀，直接加剧了 N2（页数超限）问题。\n- 建议：合并 Discussion 中与 Results 重复的内容，Discussion 专注于 (1) 与 existing literature 的对比解读、(2) practical implications、(3) open questions。预计可节省 0.3–0.5 页。\n\n---\n\n## 小问题（不影响接收）\n\n- **碰撞指标过于粗糙**：CAR 使用 L1 displacement > 10^{-3} 的二值化阈值（Section 3.2），无法捕捉碰撞严重程度的连续变化。Limitations（Appendix H）提到 \"a continuous safety metric might reveal finer-grained differences\"，但此局限应在正文中提及。\n- **代码/数据可获取性**：论文未提及是否会公开代码、训练日志、模型检查点。对于以可复现性为核心的实证研究，这一信息应在正文中说明（即使是匿名审查阶段也可用 \"code will be released upon acceptance\" 的方式）。\n- **Figure 1 信息密度**：Figure 1 占据约 0.6 页（p.2），其中 (a) training setup 示意图对理解论文贡献并非必需（标准 VLA fine-tuning 架构读者已熟悉），可考虑缩小或移入附录以节省空间。\n- **页脚格式**：当前页脚为 \"Submitted to the 10th Conference on Robot Learning (CoRL 2026). Do not distribute.\"——这是审稿版的正确格式，camera-ready 需改为指定格式，此项合规。\n- **匿名合规**：使用 \"Anonymous Author(s)\" + 占位地址/邮箱，符合 double-blind 要求。\n- **Appendix A（Extended Per-Task Results, Table 4）**：单任务级别的 mean CAR 数据有参考价值，但 Table 4 的 7 tasks × ~10 conditions 的呈现略显杂乱，可考虑用 heatmap 可视化替代。\n- **Cutoff 实验（Appendix D–E）**：仅 1–3 seeds，conclusions 应标注为 \"preliminary\"——目前 Section 4.3 对 cutoff 结果的讨论语气过于确定。\n\n---\n\n## 主要优势\n\n1. **研究问题重要且及时**：随着 SpatialVLA/DepthVLA/OccVLA 等方法大量涌现，系统检验 \"空间 auxiliary supervision 是否改善安全性\" 是一个有价值的问题，且现有文献中无人正面回答。\n2. **Factorial 实验设计**：2×2 核心 factorial（normalization × gradient flow）+ 12 条件扩展设计，比典型的 \"add auxiliary head → report numbers\" 消融研究更有方法论深度。控制变量意识强。\n3. **统计分析超越平均值报告**：使用 ANOVA 分解主效应和交互效应、报告 Cohen's d 效应量、CKA 分析表征层表示变化。这在 robotics 论文中较为少见，体现了严谨的实证研究态度。\n4. **Practical guidelines 清晰可操作**：Abstract 和 Conclusion 提供了直接的工程建议（\"detach under BN; safe under LN; avoid BN + gradient flow\"），即使不完全接受论文的所有结论，这些 heuristics 对从业者有参考价值。\n5. **诚实的 caveat 披露**：明确标注 \"v2 verification pending\"，比隐藏未验证状态更诚实——虽然这反过来也成为 weakness。\n6. **Normalization 效应的独立发现**：LN 一致性地优于 BN 3.5–4.8 pp（large effect size），这一发现不依赖于 auxiliary head 的存在（Vanilla BN vs Vanilla LN 也有差异），具有独立的工程价值。\n\n---\n\n## Questions for Authors\n\nQ1: v2 codeline 与 v1 的具体差异是什么？是 bug fix、架构变更还是数据处理差异？如果是 bug fix，v1 的结果是否可能是 artifact？\n\nQ2: 是否测量了 BN running statistics（mean 和 variance）在训练过程中的实际漂移量？当前的 CKA 分析（Section 4.3, Appendix C）只间接证明了表示没有发生大的结构性变化（CKA > 0.95），但 BN statistics 漂移可以在 CKA 不变的情况下仍然影响下游输出。直接测量 BN stats drift 可以将 \"hypothesis\" 升级为 \"evidence\"。\n\nQ3: 论文使用固定的 loss weight λ₀=0.01（Appendix H, p.19）。是否考虑过 loss weight 对 gradient flow effect 的调节作用？λ₀ 从 0.01 变为 0.001 或 0.1 时，BN + gradient flow 的 safety degradation 是否仍然存在？\n\nQ4: SafeLIBERO Level 1 仅包含 7 个任务，且 \"only static obstacles\"（Appendix H）。如果换用动态障碍物或更复杂的安全场景，normalization-gradient flow 交互效应是否可能改变？\n\nQ5: Table 4（Appendix A）显示不同任务间 CAR 方差很大（如 T1 Easy 0.98 vs T7 Hard 1.00）。这种任务异质性是否意味着 aggregate-level 的 factorial 分析可能掩盖了任务级别的交互效应？\n\n---\n\n## Missing References（建议补充）\n\n1. **Sener & Koltun (2018)**. \"Multi-Task Learning as Multi-Objective Optimization.\" NeurIPS. — PCGrad/CAGrad 的重要前驱，定义了 multi-task gradient conflict 的优化框架。\n2. **Li et al. (2017/2018)**. \"Revisiting Batch Normalization for Practical Domain Adaptation.\" — BN statistics shift 在 domain/task adaptation 中的经典讨论，与本文核心发现直接相关。\n3. **Chang et al. (2019)**. \"Domain-Specific Batch Normalization for Unsupervised Domain Adaptation.\" CVPR. — 多任务场景中 BN 统计量分离的方法论，可作为本文 \"detach gradient\" 策略的理论佐证。\n4. **3D-CAVLA (2025)**. arXiv:2505.05800 — 使用 depth-aware perception 增强 VLA 的近期方法。\n5. **Kendall et al. (2018)**. \"Multi-Task Learning Using Uncertainty to Weigh Losses.\" CVPR. — 用 uncertainty 自动调节 multi-task loss weights 的经典方法，与本文固定 λ₀=0.01 的设计选择形成对照讨论。",
    "reviewer_id": "2",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-28T11:45:08.162181+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3813
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-28T11:45:19.088876+00:00_

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
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
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

_source line 173 · 2026-05-28T11:45:19.189983+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 174 · 2026-05-28T11:45:25.161722+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/review_round_2/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 175 · 2026-05-28T11:45:25.663974+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 176 · 2026-05-28T11:45:25.664360+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/tmp/occsafe_hires"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/tmp/occsafe_hires"
  }
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-28T11:45:26.116272+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"安全限制：只能清理 _pdf_images 目录，当前目标: occsafe_hires\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 451
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-28T11:45:26.116577+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/tmp/occsafe_hires_p9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/tmp/occsafe_hires_p9"
  }
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-28T11:45:26.217177+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"安全限制：只能清理 _pdf_images 目录，当前目标: occsafe_hires_p9\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---

### Assistant

_source line 180 · 2026-05-28T11:45:40.501649+00:00_

Round 1 审稿意见已提交给 Review Director。

**审稿要点总结**：
- **总体评分 4/10**（倾向拒稿），识别出 3 个 Critical 问题、5 个 Major 问题
- **Critical**: (1) Limitations 放在 Appendix H 而非正文，违反 CoRL 2026 硬性要求；(2) 正文超 8 页（Conclusion 在第 9 页）；(3) 核心发现 "spatial label content 无效果" 标注为 "v2 verification pending"，严重削弱可信度
- **Major**: 泛化性受限（单模型/单基准）、样本量不足（n=3–4 seeds）、novelty 定位模糊（BN statistics corruption 是 multi-task learning 已知现象）、Related Work 可补充 MGDA/BN domain shift 文献、Discussion 与 Results 重复
- **优势**: 研究问题及时重要、factorial 方法论严谨、统计分析超越常规、practical guidelines 可操作
- 补充了 5 篇建议引用和 5 个 Questions for Authors

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2"
}
```

</details>

---

## Round 4

4 recorded events

### User

_source line 181 · 2026-05-28T11:46:38.961040+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题。对每条标注：
- **[AGREE]** — 同意该观点，说明理由
- **[REBUT]** — 不同意或有补充，提供证据（引用具体 Section/Table/Figure）

特别关注以下你们可能有分歧或互补的点：
1. Reviewer 1 的 C1（中心主张与统计结果矛盾：interaction framing vs additive effects）——你的审稿未直接涉及此问题，是否同意这是 critical issue？
2. Reviewer 1 的 C2（v1/v2 codebase confound）——你的 N3 从 "v2 verification pending" 的可信度角度分析了类似问题，两者是否一致？是否有补充？
3. Reviewer 1 的 W3（梯度正交性与 gradient flow harmful 的矛盾）——你的 W3 从 novelty 角度指出 BN statistics corruption 是已知效应。这两个视角是否互补？
4. Reviewer 1 的 W1（Cohen's d 基准标签膨胀：d=0.50 标注为 "large"）——你是否注意到同一问题？

---

以下是 Reviewer 1 的完整审稿意见：

## Reviewer 1 审稿意见 — Round 1（方法与实验严谨性）

**Overall**: 3/5（Borderline lean reject）

**一句话总结**: 研究问题重要、实验设计有原则性，但中心主张（normalization-dependent gradient flow effect）与论文自身统计分析结果存在根本性矛盾——ANOVA 交互项不显著（p=0.753）却被叙述为条件性效应，加上 v1/v2 codebase 混淆和严重不足的统计效力，当前证据不足以支撑论文的核心结论。

### Must-Fix 问题

**C1** [Critical] **中心主张与统计分析结果之间的根本矛盾**
论文的核心叙事是 gradient flow 的效应取决于 normalization type（"harmful under BN, benign under LN"）。这在统计学上是交互效应。但 ANOVA 交互项完全不显著：F(1,10)=0.10, p=0.753, η²=0.010。从 cell means 看，BN 下 gradient flow penalty ≈ −3.4pp，LN 下 ≈ −2.9pp，幅度相近。LN 下 gradient flow 看似"benign"只是因为 LN 基线更高（normalization 主效应），penalty 后仍接近 Vanilla。这是 additive main effects 被错误叙述为 conditional/moderated effects 的框架性错误。Figure 2 两条线近似平行，视觉上也证实 additive pattern。

**C2** [Critical] **v1/v2 codebase confound 破坏跨条件比较**
v1→v2 同条件 CAR 偏移 ~8.6pp，核心 2×2 factorial 用 v2，5 个 supplementary conditions 用 v1。8.6pp 的 codebase 效应与论文报告的最大实验效应（~5-6pp）在同一数量级。涉及 v1 条件的所有结论（包括 spatial content 不重要的发现）可靠性存疑。

**C3** [Critical] **统计效力严重不足**
每个 cell n=3-4（总共 14 observations），残差 df=10。对 medium effect size 的 power <50%。Cohen's d 的 95% CI ≈ ±1.0-1.5。非显著结果不能解读为"无效应"。交互效应检测需要主效应 4 倍样本量——n=3-4 对交互的 power 可能 <20%，因此不能在 power 不足时声称"交互不显著 confirms additive"。

### Should-Fix 问题

**W1** [Major] Cohen's d = −0.50 在 abstract 标注为 "large"，Cohen (1988) 标准下应为 medium。可能系统性膨胀效应量标签。

**W2** [Major] ANOVA 前提假设（正态性、方差齐性）在 n=3-4 下不可验证。未提供非参数替代方案（如 permutation test）。

**W3** [Major] 梯度正交性发现与 gradient flow harmful 的主张存在张力——cosine similarity ≈ 0 across layers，但论文声称 gradient flow 有害。"Mechanism remains open" 的解释（"indirect effect through LoRA optimization trajectory"）纯属猜测，无支撑证据。

**W4** [Major] 单一 benchmark（SafeLIBERO Level I, 10 tasks）限制泛化性。Level II/III 任务有不同约束类型。

**W5** [Major] 固定 λ₀=0.01，缺乏超参数敏感度分析。Gradient flow 效应可能高度依赖此选择。

### Missing References
1. Montgomery — "Design and Analysis of Experiments"（factorial design 方法论基础）
2. Anderson (2001) — Permutation tests（非参数替代方案）
3. Li et al. (2016) / Ioffe (2017) — BN fine-tuning 场景下的已知问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 182 · 2026-05-28T11:48:51.872039+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 (R1) 审稿意见的逐条评议\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-C1: 中心主张与统计分析结果之间的根本矛盾**\n\n同意这是 critical issue，且我的 Round 1 审稿未充分识别此问题。R1 的分析精准：\n\n论文 abstract 声称 \"normalization-dependent gradient flow effect\"（即 gradient flow 的效应依赖于 normalization type），这在统计学上是一个交互效应（interaction effect）。但论文自身的 2×2 ANOVA（Appendix F, Table 6）报告交互项 F(1,10)=0.10, p=0.753, η²=0.010——完全不显著。Figure 2（p.7）的两条线（BN vs LN）近似平行，视觉上也确认是 additive pattern。\n\nR1 正确指出了问题的本质：LN 下 gradient flow 看似 \"benign\" 不是因为 LN 调节了 gradient flow 的效应，而是因为 LN 有更高的基线（normalization 主效应 ~3.5–4.8 pp），gradient flow penalty 叠加后仍高于 Vanilla。这是两个独立的 additive main effects，不是一个 conditional/moderated effect。\n\n**补充**：这一框架性错误不仅影响 abstract 和 conclusion 的措辞，还影响论文的 practical guidelines。当前建议 \"gradient flow is safe under LN\" 暗示 LN 本身消除了 gradient flow 的负面影响，但实际上 LN 下 gradient flow 同样有 ~2.9pp 的 penalty（Table 3: ON→OFF 差异），只是因为 LN 基线高所以最终 CAR 仍可接受。正确的表述应为：(1) LN 一致性地提高 safety（主效应 1）；(2) gradient flow 一致性地降低 safety 约 3–4pp（主效应 2）；(3) 两者独立叠加。这虽然在实际意义上不改变 engineering recommendation，但在科学表述上有本质区别。\n\n---\n\n**[AGREE] R1-C2: v1/v2 codebase confound 破坏跨条件比较**\n\n完全同意，且 R1 的分析比我的 N3 更深入。\n\n我的 N3 从 \"可信度\" 角度批评了 \"v2 verification pending\" 的措辞——即论文呈现了自身不确定的结论。R1 的 C2 更进一步，揭示了一个具体的 confound：v1→v2 同条件 CAR 偏移 ~8.6pp，而论文报告的最大实验效应（gradient flow penalty）仅 ~5–6pp。这意味着 codebase version 的效应量大于实验处理的效应量。任何涉及 v1 条件的跨条件比较（包括 \"spatial content 不重要\" 的核心发现）都被这一 confound 污染。\n\n**补充**：这一 confound 还加重了 C1 的问题。如果 12 条件中的部分用 v1、部分用 v2，那么 Table 1 中呈现的跨条件比较（12 conditions across 两个 codelines）混入了未控制的 codebase 变量。即使 2×2 factorial（Table 3）全部使用 v2，supplementary conditions 使用 v1 的事实也意味着论文无法可靠地对比 core 条件和 supplementary 条件。论文在 Section 4.1 中比较了 Full OCC、Random OCC、Depth 等条件，但如果这些来自不同 codelines，此类比较无效。\n\n---\n\n**[AGREE] R1-C3: 统计效力严重不足**\n\n同意，且 R1 的 power analysis 比我的 W2 更为具体。\n\n我的 W2 指出了 \"样本量不足，统计推断可靠性存疑\"，但仅泛泛提到 n=3–4 的问题。R1 的 C3 给出了关键的量化论据：\n- 对 medium effect size 的 power <50%\n- Cohen's d 的 95% CI 宽度 ≈ ±1.0–1.5\n- 交互效应检测需要主效应 4 倍样本量（经验法则）——n=3–4 对交互的 power 可能 <20%\n\n最后一点特别致命：如果交互效应的 power <20%，那么 p=0.753 的非显著结果不能被解读为 \"confirms additive\"（如论文 Abstract 所述 \"A 2×2 ANOVA confirms additive main effects with negligible interaction\"）。这是 \"absence of evidence ≠ evidence of absence\" 的典型案例。论文将 underpowered test 的非显著结果 interpret 为对 null hypothesis 的确认，这是统计推理错误。\n\n**补充**：结合 C1 和 C3，论文的核心叙事面临双重挑战——(1) interaction framing 与 ANOVA 结果矛盾（C1）；(2) 即使接受 \"无交互\" 的结论，当前 power 也不足以可靠地排除交互（C3）。这两个问题共同削弱了论文的中心贡献。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Cohen's d 基准标签膨胀**\n\n同意。Cohen (1988) 的标准为：small=0.20, medium=0.50, large=0.80。如果论文中存在 d=0.50 被标注为 \"large\" 的情况（R1 指出 abstract 中有此问题），这是效应量标签的系统性膨胀。\n\n我的 Round 1 审稿未专门检查 d 标签的准确性。回查 Section 4.2（p.6）的文本，论文确实对 normalization 主效应和 gradient flow 效应给出了多个 d 值及标签。若存在 d≈0.50 标注 \"large\" 的情况，需全文排查所有 Cohen's d 标签并按 Cohen 标准修正。\n\n**补充**：考虑到 n=3–4 时 Cohen's d 的采样变异极大（C3），建议论文报告 d 的置信区间或 bootstrapped 估计，而非仅给出点估计 + categorical label。一个看似 \"large\" 的 d=0.93 在 n=3 时的 95% CI 可能包含 medium 甚至 small 区间。\n\n---\n\n**[AGREE] R1-W2: ANOVA 前提假设不可验证**\n\n同意。n=3–4 下 Shapiro-Wilk 检验几乎无统计功效，Levene's test 同样不可靠。论文使用参数化 ANOVA 但未提供：(1) 残差分布的诊断图；(2) 非参数替代方案（如 permutation test / rank-based ANOVA）。\n\nR1 建议的 permutation test（Anderson 2001）是合理的补充方案。n=3–4 时 permutation test 的排列数有限（最多 4!×4!=576 种），但仍比依赖正态性假设的 F-test 更可靠。\n\n---\n\n**[AGREE] R1-W3: 梯度正交性与 gradient flow harmful 的矛盾**\n\n同意，且这一观点与我的 W3（BN statistics corruption 是已知效应）互补。\n\nR1 从论文内部一致性角度指出矛盾：Section 4.3（p.7）和 Appendix C 的梯度分析显示 action-auxiliary gradient cosine similarity ≈ 0（正交），这意味着不存在 PCGrad 意义上的 gradient conflict。然而论文声称 gradient flow 有害。论文的解释——\"indirect effect through LoRA optimization trajectory\"——无支撑证据。\n\n我的 W3 从外部文献角度指出：论文暗示的机制（BN running statistics corruption by auxiliary gradients）在 multi-task learning / domain adaptation 文献中是已知现象（Li et al. 2017, DSBN / Chang et al. 2019 等）。\n\n**两个视角的互补性**：R1 识别了 \"梯度正交但仍有害\" 这一表面矛盾；我的分析提供了一个可能的解释——BN statistics corruption 不需要梯度方向上的冲突，即使梯度正交，auxiliary path 的 forward pass 也会更新 BN 的 running mean/variance，从而改变主任务在推理时的 BN 行为。这一机制不依赖于 gradient conflict，因此与 cosine similarity ≈ 0 并不矛盾。但论文既未提出这一机制的清晰假设，也未提供直接证据（如 BN running stats 的训练过程漂移量测量）。两个视角共同指向论文在机制解释上的核心空白。\n\n---\n\n**[AGREE] R1-W4: 单一 benchmark 限制泛化性**\n\n同意，与我的 W1 一致。R1 额外指出 SafeLIBERO Level II/III 有不同的约束类型，这是一个有价值的具体建议。论文仅使用 Level I（static obstacles, 7 tasks），而 Level II/III 可能涉及动态障碍物或更复杂的安全约束，normalization-gradient flow 效应可能呈现不同模式。\n\n---\n\n**[AGREE] R1-W5: 固定 λ₀=0.01，缺乏超参数敏感度分析**\n\n同意，与我的 Question Q3 完全一致。λ₀ 直接控制 auxiliary gradient 的幅度——如果 λ₀ 极小（如 0.001），gradient flow 效应可能消失；如果 λ₀ 较大（如 0.1），效应可能更强。当前结果可能高度依赖于 λ₀=0.01 这一特定选择，论文需要至少 3 个 λ₀ 值的消融实验来验证发现的鲁棒性。\n\n---\n\n### Missing References\n\n**[AGREE]** R1 建议的三个 missing references 都合理：\n1. **Montgomery — Design and Analysis of Experiments**：论文使用 factorial design 作为方法论卖点，引用经典教材是必要的。\n2. **Anderson (2001) — Permutation tests**：与 W2 直接相关。\n3. **Li et al. (2016) / Ioffe (2017) — BN fine-tuning 问题**：与我建议的 BN domain shift 文献（Li et al. 2017 \"Revisiting BN for Practical Domain Adaptation\"、Chang et al. 2019 DSBN）互补。\n\n---\n\n### 总结：两位 Reviewer 的意见汇合\n\nR1 和 R2 的审稿意见在以下方面高度一致：\n1. **v1/v2 问题**是论文最致命的缺陷（R1-C2 + R2-N3），但 R1 揭示了更严重的 confound 问题（跨条件比较被污染），R2 侧重可信度\n2. **统计效力不足**（R1-C3 + R2-W2），R1 的分析更量化\n3. **泛化性受限**（R1-W4 + R2-W1），单一模型/基准\n4. **λ₀ 敏感度缺失**（R1-W5 + R2-Q3）\n5. **BN 机制的文献覆盖不足**（R1-Missing Ref 3 + R2-W4 + R2-Missing Ref 2-3）\n\nR1 独有的关键贡献：**C1（interaction framing 矛盾）**——这是我未识别的重要问题，直接动摇论文的中心叙事结构。\n\nR2 独有的关键贡献：**N1-N2（格式违规：Limitations 不在正文 + 页数超限）**——这是 desk rejection 级别的硬伤，R1 未涉及。\n\n两位 Reviewer 均认为论文在当前状态下不达接收标准，但研究问题有价值、方法论方向正确，如能解决上述问题（特别是 v2 验证、增加样本量、修正 interaction framing、修复格式）有 revision potential。",
  "reviewer_id": "2",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 (R1) 审稿意见的逐条评议\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-C1: 中心主张与统计分析结果之间的根本矛盾**\n\n同意这是 critical issue，且我的 Round 1 审稿未充分识别此问题。R1 的分析精准：\n\n论文 abstract 声称 \"normalization-dependent gradient flow effect\"（即 gradient flow 的效应依赖于 normalization type），这在统计学上是一个交互效应（interaction effect）。但论文自身的 2×2 ANOVA（Appendix F, Table 6）报告交互项 F(1,10)=0.10, p=0.753, η²=0.010——完全不显著。Figure 2（p.7）的两条线（BN vs LN）近似平行，视觉上也确认是 additive pattern。\n\nR1 正确指出了问题的本质：LN 下 gradient flow 看似 \"benign\" 不是因为 LN 调节了 gradient flow 的效应，而是因为 LN 有更高的基线（normalization 主效应 ~3.5–4.8 pp），gradient flow penalty 叠加后仍高于 Vanilla。这是两个独立的 additive main effects，不是一个 conditional/moderated effect。\n\n**补充**：这一框架性错误不仅影响 abstract 和 conclusion 的措辞，还影响论文的 practical guidelines。当前建议 \"gradient flow is safe under LN\" 暗示 LN 本身消除了 gradient flow 的负面影响，但实际上 LN 下 gradient flow 同样有 ~2.9pp 的 penalty（Table 3: ON→OFF 差异），只是因为 LN 基线高所以最终 CAR 仍可接受。正确的表述应为：(1) LN 一致性地提高 safety（主效应 1）；(2) gradient flow 一致性地降低 safety 约 3–4pp（主效应 2）；(3) 两者独立叠加。这虽然在实际意义上不改变 engineering recommendation，但在科学表述上有本质区别。\n\n---\n\n**[AGREE] R1-C2: v1/v2 codebase confound 破坏跨条件比较**\n\n完全同意，且 R1 的分析比我的 N3 更深入。\n\n我的 N3 从 \"可信度\" 角度批评了 \"v2 verification pending\" 的措辞——即论文呈现了自身不确定的结论。R1 的 C2 更进一步，揭示了一个具体的 confound：v1→v2 同条件 CAR 偏移 ~8.6pp，而论文报告的最大实验效应（gradient flow penalty）仅 ~5–6pp。这意味着 codebase version 的效应量大于实验处理的效应量。任何涉及 v1 条件的跨条件比较（包括 \"spatial content 不重要\" 的核心发现）都被这一 confound 污染。\n\n**补充**：这一 confound 还加重了 C1 的问题。如果 12 条件中的部分用 v1、部分用 v2，那么 Table 1 中呈现的跨条件比较（12 conditions across 两个 codelines）混入了未控制的 codebase 变量。即使 2×2 factorial（Table 3）全部使用 v2，supplementary conditions 使用 v1 的事实也意味着论文无法可靠地对比 core 条件和 supplementary 条件。论文在 Section 4.1 中比较了 Full OCC、Random OCC、Depth 等条件，但如果这些来自不同 codelines，此类比较无效。\n\n---\n\n**[AGREE] R1-C3: 统计效力严重不足**\n\n同意，且 R1 的 power analysis 比我的 W2 更为具体。\n\n我的 W2 指出了 \"样本量不足，统计推断可靠性存疑\"，但仅泛泛提到 n=3–4 的问题。R1 的 C3 给出了关键的量化论据：\n- 对 medium effect size 的 power <50%\n- Cohen's d 的 95% CI 宽度 ≈ ±1.0–1.5\n- 交互效应检测需要主效应 4 倍样本量（经验法则）——n=3–4 对交互的 power 可能 <20%\n\n最后一点特别致命：如果交互效应的 power <20%，那么 p=0.753 的非显著结果不能被解读为 \"confirms additive\"（如论文 Abstract 所述 \"A 2×2 ANOVA confirms additive main effects with negligible interaction\"）。这是 \"absence of evidence ≠ evidence of absence\" 的典型案例。论文将 underpowered test 的非显著结果 interpret 为对 null hypothesis 的确认，这是统计推理错误。\n\n**补充**：结合 C1 和 C3，论文的核心叙事面临双重挑战——(1) interaction framing 与 ANOVA 结果矛盾（C1）；(2) 即使接受 \"无交互\" 的结论，当前 power 也不足以可靠地排除交互（C3）。这两个问题共同削弱了论文的中心贡献。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Cohen's d 基准标签膨胀**\n\n同意。Cohen (1988) 的标准为：small=0.20, medium=0.50, large=0.80。如果论文中存在 d=0.50 被标注为 \"large\" 的情况（R1 指出 abstract 中有此问题），这是效应量标签的系统性膨胀。\n\n我的 Round 1 审稿未专门检查 d 标签的准确性。回查 Section 4.2（p.6）的文本，论文确实对 normalization 主效应和 gradient flow 效应给出了多个 d 值及标签。若存在 d≈0.50 标注 \"large\" 的情况，需全文排查所有 Cohen's d 标签并按 Cohen 标准修正。\n\n**补充**：考虑到 n=3–4 时 Cohen's d 的采样变异极大（C3），建议论文报告 d 的置信区间或 bootstrapped 估计，而非仅给出点估计 + categorical label。一个看似 \"large\" 的 d=0.93 在 n=3 时的 95% CI 可能包含 medium 甚至 small 区间。\n\n---\n\n**[AGREE] R1-W2: ANOVA 前提假设不可验证**\n\n同意。n=3–4 下 Shapiro-Wilk 检验几乎无统计功效，Levene's test 同样不可靠。论文使用参数化 ANOVA 但未提供：(1) 残差分布的诊断图；(2) 非参数替代方案（如 permutation test / rank-based ANOVA）。\n\nR1 建议的 permutation test（Anderson 2001）是合理的补充方案。n=3–4 时 permutation test 的排列数有限（最多 4!×4!=576 种），但仍比依赖正态性假设的 F-test 更可靠。\n\n---\n\n**[AGREE] R1-W3: 梯度正交性与 gradient flow harmful 的矛盾**\n\n同意，且这一观点与我的 W3（BN statistics corruption 是已知效应）互补。\n\nR1 从论文内部一致性角度指出矛盾：Section 4.3（p.7）和 Appendix C 的梯度分析显示 action-auxiliary gradient cosine similarity ≈ 0（正交），这意味着不存在 PCGrad 意义上的 gradient conflict。然而论文声称 gradient flow 有害。论文的解释——\"indirect effect through LoRA optimization trajectory\"——无支撑证据。\n\n我的 W3 从外部文献角度指出：论文暗示的机制（BN running statistics corruption by auxiliary gradients）在 multi-task learning / domain adaptation 文献中是已知现象（Li et al. 2017, DSBN / Chang et al. 2019 等）。\n\n**两个视角的互补性**：R1 识别了 \"梯度正交但仍有害\" 这一表面矛盾；我的分析提供了一个可能的解释——BN statistics corruption 不需要梯度方向上的冲突，即使梯度正交，auxiliary path 的 forward pass 也会更新 BN 的 running mean/variance，从而改变主任务在推理时的 BN 行为。这一机制不依赖于 gradient conflict，因此与 cosine similarity ≈ 0 并不矛盾。但论文既未提出这一机制的清晰假设，也未提供直接证据（如 BN running stats 的训练过程漂移量测量）。两个视角共同指向论文在机制解释上的核心空白。\n\n---\n\n**[AGREE] R1-W4: 单一 benchmark 限制泛化性**\n\n同意，与我的 W1 一致。R1 额外指出 SafeLIBERO Level II/III 有不同的约束类型，这是一个有价值的具体建议。论文仅使用 Level I（static obstacles, 7 tasks），而 Level II/III 可能涉及动态障碍物或更复杂的安全约束，normalization-gradient flow 效应可能呈现不同模式。\n\n---\n\n**[AGREE] R1-W5: 固定 λ₀=0.01，缺乏超参数敏感度分析**\n\n同意，与我的 Question Q3 完全一致。λ₀ 直接控制 auxiliary gradient 的幅度——如果 λ₀ 极小（如 0.001），gradient flow 效应可能消失；如果 λ₀ 较大（如 0.1），效应可能更强。当前结果可能高度依赖于 λ₀=0.01 这一特定选择，论文需要至少 3 个 λ₀ 值的消融实验来验证发现的鲁棒性。\n\n---\n\n### Missing References\n\n**[AGREE]** R1 建议的三个 missing references 都合理：\n1. **Montgomery — Design and Analysis of Experiments**：论文使用 factorial design 作为方法论卖点，引用经典教材是必要的。\n2. **Anderson (2001) — Permutation tests**：与 W2 直接相关。\n3. **Li et al. (2016) / Ioffe (2017) — BN fine-tuning 问题**：与我建议的 BN domain shift 文献（Li et al. 2017 \"Revisiting BN for Practical Domain Adaptation\"、Chang et al. 2019 DSBN）互补。\n\n---\n\n### 总结：两位 Reviewer 的意见汇合\n\nR1 和 R2 的审稿意见在以下方面高度一致：\n1. **v1/v2 问题**是论文最致命的缺陷（R1-C2 + R2-N3），但 R1 揭示了更严重的 confound 问题（跨条件比较被污染），R2 侧重可信度\n2. **统计效力不足**（R1-C3 + R2-W2），R1 的分析更量化\n3. **泛化性受限**（R1-W4 + R2-W1），单一模型/基准\n4. **λ₀ 敏感度缺失**（R1-W5 + R2-Q3）\n5. **BN 机制的文献覆盖不足**（R1-Missing Ref 3 + R2-W4 + R2-Missing Ref 2-3）\n\nR1 独有的关键贡献：**C1（interaction framing 矛盾）**——这是我未识别的重要问题，直接动摇论文的中心叙事结构。\n\nR2 独有的关键贡献：**N1-N2（格式违规：Limitations 不在正文 + 页数超限）**——这是 desk rejection 级别的硬伤，R1 未涉及。\n\n两位 Reviewer 均认为论文在当前状态下不达接收标准，但研究问题有价值、方法论方向正确，如能解决上述问题（特别是 v2 验证、增加样本量、修正 interaction framing、修复格式）有 revision potential。",
    "reviewer_id": "2",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-28T11:48:55.737452+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3865
}
```

</details>

---

### Assistant

_source line 184 · 2026-05-28T11:49:06.534736+00:00_

交叉回应已提交。核心判断：

- R1 的 C1（interaction framing 矛盾）是我 Round 1 未充分识别的关键问题，完全同意——ANOVA 交互项 p=0.753 与 "normalization-dependent" 的叙事框架存在根本矛盾
- R1 的 C2 比我的 N3 更深入，揭示了 v1/v2 偏移量（~8.6pp）大于实验效应量（~5-6pp）的 confound 问题
- R1-W3（梯度正交性矛盾）与我的 W3（BN stats corruption 是已知效应）互补：正交梯度排除了 PCGrad 式冲突，但不排除 BN running stats 被 auxiliary forward pass 污染
- 两位 Reviewer 在 v1/v2 问题、统计效力、泛化性、λ₀ 敏感度上高度一致，共同指向 "当前证据不足以支撑核心结论" 的判断

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_faa96524df7d6444f5c8cbc48d5a616b:reviewer_2"
}
```

</details>

---
