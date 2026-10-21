# Reviewer coordination

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 98
- **Recorded user turns:** 2
- **Tool calls:** 47
- **Original source:** `logs/chats/feishu_group_oc_ec359a7b7a5e3b28b379b61588c6e853_reviewer_3.jsonl`
- **Structured JSON:** [`9806b6c42f3eab85f997.json`](../../sessions/98/9806b6c42f3eab85f997.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

94 recorded events

### User

_source line 1 · 2026-05-28T04:59:01.230628+00:00_

[Round 1 审稿请求]:
## 审稿任务 — Reviewer 3（写作质量 + 格式合规 + Limitations + 伦理）

### Venue 信息
- **目标会议**：CoRL 2026（Conference on Robot Learning）
- **截止日期**：2026-05-28 12:00 UTC
- **页数限制**：8 页正文 + acknowledgment + references + appendix（不计入页数）
- **模板**：corl_2026（PMLR 格式）
- **匿名规则**：Double-blind
- **Limitations section**：必须包含，计入 8 页

### 论文路径
- LaTeX 源码：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, claim1.tex, claim2.tex, claim3.tex, discussion.tex, appendix.tex）
- PDF：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/submitted.pdf`

### 你的审查侧重

**1. 格式合规性**
- 检查是否使用了正确的 `corl_2026` 模板
- 正文是否在 8 页以内（不含 acknowledgment/references/appendix）？
- 匿名要求：是否有任何泄露作者身份的信息（self-citation、GitHub 链接、项目名称等）？
- 引用格式是否一致（natbib / author-year）？
- Figure/Table 编号是否连续？caption 是否完整自含？
- 数学符号是否一致（特别是 τ_d, λ, d_max 等在全文中的使用）

**2. 写作质量**
- 整体可读性（clarity score 1-5）
- 逻辑流畅性：各节之间的过渡是否自然？
- 是否有 AI 写作痕迹（过度使用 "notably", "crucially", "it is worth noting", "we posit" 等）？
- 语法/拼写错误检查
- 术语一致性（如 "action collapse" vs "frozen episodes" 是否混用？"fake safety" 是否有明确定义？）
- 关键概念（dfCAR, action collapse, fake safety）是否在首次出现时有清晰定义？

**3. Limitations section**
- CoRL 2026 要求必须有 Limitations section 且计入 8 页
- 当前 Limitations 内容是否诚实、充分？
- 是否遗漏了重要限制（如：只用模拟环境、无真实机器人验证、benchmark 覆盖范围窄等）？
- Limitations 是否与 Discussion 重复或冲突？

**4. 图表质量**
- Figure 1（teaser）是否在第一页？是否直观传达核心信息？
- 所有图表是否清晰可读（字体大小、颜色方案、分辨率）？
- 图表是否有 redundancy？是否可以合并？
- Table 布局是否规范（booktabs 风格、无过多竖线）？

**5. 伦理与更广泛影响**
- 论文涉及机器人安全——是否充分讨论了声称"安全指标有缺陷"可能带来的负面影响？
- 是否有 responsible disclosure 考虑？（声称现有方法无效可能影响已发表工作的声誉）
- Broader Impact section 是否平衡？

**6. 引用完整性**
- 引用格式是否一致？是否有 arXiv 和 published version 混用？
- 自引（如有）是否匿名化？
- 是否缺少关键引用？

请按 CoRL 审稿标准评估，给出 Strengths / Weaknesses / Questions / Minor Issues，每条标注 [Must-Fix] 或 [Should-Fix] 或 [Minor]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "source": "review_reviewer_3"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-28T04:59:10.644998+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-28T04:59:11.502998+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/.claude/sessions/review_reviewer_3_b52c5137.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-28T04:59:11.656148+00:00_

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
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
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

_source line 5 · 2026-05-28T04:59:11.758553+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "ToolSearch",
  "elapsed_ms": 102
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-28T04:59:16.129624+00:00_

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
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T04:59:17.636631+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/submitted.pdf",
  "project": "diff_collision_sdf",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/submitted.pdf",
    "project": "diff_collision_sdf",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-28T04:59:17.838749+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-28T04:59:22.765836+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, I found some information about CoRL 2026 submission requirements and guidelines, though the specific reviewer guidelines and review form criteria aren't fully detailed in these results.

Here's what I found regarding CoRL 2026:

**Reviewer Requirements:**
All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal. Additionally, every author with 3 or more submissions must agree to serve as a reviewer.

**Review Criteria for Papers:**
While I found review criteria from CoRL 2024, the specific 2026 review form criteria aren't fully detailed in the search results. However, based on the call for papers, submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics.

For more detailed information about the specific reviewer guidelines and review form criteri
…[truncated 273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebSearch",
  "elapsed_ms": 6636
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T04:59:24.127379+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 309.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 297.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 345.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 283.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 233.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 250.5}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 244.8}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 363.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p9.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 321.8}, {
…[truncated 449 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6490
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-28T04:59:24.178080+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/_archive/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/_archive/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/_archive/conclusion_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/archive/analysis_claim4.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/archive/analysis_claim2.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/archive/analysis_claim1.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/archive/analysis_claim3.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/contingency_claim3.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/experimental_framework.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/d
…[truncated 41 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Glob",
  "elapsed_ms": 6339
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-28T04:59:31.472186+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, scoring dimensions, rating scales, and any specific guidelines for CoRL reviewers. Include all evaluation dimensions like soundness, significance, novelty, clarity, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, scoring dimensions, rating scales, and any specific guidelines for CoRL reviewers. Include all evaluation dimensions like soundness, significance, novelty, clarity, etc."
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T04:59:32.878733+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/call-for-papers",
  "prompt": "Extract submission requirements: page limits, template, anonymity rules, required sections (limitations, broader impact), formatting requirements, and any special instructions for CoRL 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/call-for-papers",
    "prompt": "Extract submission requirements: page limits, template, anonymity rules, required sections (limitations, broader impact), formatting requirements, and any special instructions for CoRL 2026."
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-28T04:59:33.882598+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-28T04:59:34.337883+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-28T04:59:34.338272+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T04:59:34.792634+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-28T04:59:34.793163+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T04:59:35.247514+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-28T04:59:35.298224+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-28T04:59:35.801191+00:00_

# CoRL 2024 Review Criteria Summary

Based on the provided webpage content, CoRL does not present a detailed review form with specific scoring dimensions or rating scales. Instead, the document outlines broader evaluation parameters:

## Primary Review Criteria

Papers are assessed on:
- **Significance and novelty** of results (theoretical or empirical)
- **Objective establishment** of findings and potential for scientific/technological impact
- **Relevance to robotic learning**

The conference states it takes "a broad view of robot learning" and welcomes submissions combining experimental and theoretical contributions.

## Scope Requirements

Submissions must demonstrate relevance to Robot Learning through either:
- **Intent**: "Explicitly address a learning question for physical robots" OR
- **Outcome**: "Test the proposed learning solution on physical robots"

## Notable Gaps

The document does not include:
- Specific numerical rating scales
- Individual evaluation dimensions (soundness, clarity, significance, etc.)
- Detailed reviewer scoring rubrics
- Guidance on comparative assessment between papers

The instructions focus primarily on desk rejection criteria and reviewer qualifications rather than providing a comprehensive scoring framework for accepted submissions under review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebFetch",
  "elapsed_ms": 4329
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T04:59:35.802881+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-28T04:59:35.803148+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-28T04:59:36.256943+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-28T04:59:37.362462+00:00_

# CoRL 2026 Submission Requirements

Based on the Call for Papers page, here are the identified submission requirements:

## Explicitly Stated Requirements

**Required Sections:**
- Limitations section mandatory: "All submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations"

**Content Focus:**
- Papers must address robotics problems with demonstrated relevance to the field
- Real-robot experiments strongly encouraged; simulation work needs "convincing evidence that simulation experiments are transferable to real robots"
- Submissions lacking robotics focus will be desk-rejected

**Supplementary Materials:**
- Video, code, and data submissions are encouraged but appear optional

## Not Specified on This Page

The following details are **not provided** on the Call for Papers page:

- Page limit/length restrictions
- Submission template requirements
- Anonymity/blind review policies
- Broader impact statement requirements
- Specific formatting guidelines (fonts, margins, citation style)
- Submission deadline and review timeline

**Where to Find Complete Details:**

The page directs authors to the [Instruction for Authors](/contributions/instruction-for-authors) section for "paper submission format and timeline," suggesting that comprehensive submission guidelines are documented elsewhere on the CoRL website.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebFetch",
  "elapsed_ms": 4483
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-28T04:59:42.802748+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract all formatting requirements: page limits, template name, anonymity rules, required sections, citation format, figure requirements, and any other submission formatting guidelines for CoRL 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/instruction-for-authors",
    "prompt": "Extract all formatting requirements: page limits, template name, anonymity rules, required sections, citation format, figure requirements, and any other submission formatting guidelines for CoRL 2026."
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-28T04:59:43.258068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-28T04:59:44.223981+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 965
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-28T04:59:44.227621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-28T04:59:44.730432+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-28T04:59:45.285953+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 1058
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-28T04:59:45.290115+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-28T04:59:45.652123+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 921
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-28T04:59:45.654548+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-28T04:59:46.865905+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 1575
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-28T04:59:47.323797+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 1669
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-28T04:59:47.625034+00:00_

# CoRL 2026 Formatting Requirements

## Page Limits
- **Initial submission:** 8 pages maximum for main paper
- **Camera-ready:** 9 pages maximum for main paper
- Acknowledgments, references, and optional appendix do not count toward page limits

## Template & Format
- Use the provided LaTeX template (available via Google Drive link)
- Camera-ready must include footer: "10th Conference on Robot Learning (CoRL 2026), Austin, Texas, USA."
- Match template specifications for text density, fonts, spacing, and margins

## Anonymity Requirements
- Initial submission must be double-blind and fully anonymized
- Camera-ready version removes anonymity and includes full author list

## Required Sections
- Main paper content
- **Limitations section** (mandatory, counts toward 8-page limit) describing "limiting assumptions, failure modes, and other limitations"
- Acknowledgments
- References
- Optional appendix

## Supplementary Materials
- Single zip file through OpenReview
- Video optional: maximum 250 MB, suggested 3-minute length
- Videos cannot be included in PMLR submission; host externally
- Appendix may be included with main paper or supplement

## Citation & Content Standards
- All citations must reference existing works
- Papers with non-existent citations face desk rejection
- Disclose generative AI tool usage during submission

## Other Requirements
- Authors must ensure reproducibility through detailed methodology
- Reciprocal reviewing requirement applies to qualified authors

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebFetch",
  "elapsed_ms": 4822
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-28T04:59:53.905186+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/submitted.pdf",
  "project": "diff_collision_sdf",
  "pages": "11-17",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/submitted.pdf",
    "project": "diff_collision_sdf",
    "pages": "11-17",
    "dpi": "150"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-28T04:59:54.508713+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-28T04:59:54.860138+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-28T04:59:55.313751+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-28T04:59:55.518223+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p11.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 218.7}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p12.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 256.5}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p13.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 268.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p14.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 314.3}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p15.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 330.9}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p16.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 278.9}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p17.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 148.3}], \"total_pages\": 17, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1613
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-28T04:59:55.518707+00:00_

1	\begin{abstract}
2	Vision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance.
3	On SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\% CAR while 99.6\% of its safe episodes exhibit end-effector (EE) displacement below 0.1\,mm. The robot is frozen, not safe.
4	We introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes. The bimodal displacement distribution makes dfCAR robust across a $[2, 200]$\,mm threshold range.
5	We further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance. At inference time, ground-truth oracle refinement reduces CAR below unrefined baselines because the SDF gradient drives unmonitored arm links into obstacles. During training, collision-free demonstrations alone account for all measured avoidance gains (${\sim}$26 percentage points). SDF supervision adds no measurable benefit across the full tested range $\lambda \in \{0.005, 0.01, 0.1\}$ ($p > 0.05$ for all; $\lambda = 0.1$: 57.00\%$\,\pm\,$2.18, 3 seeds).
6	Displacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision is fully redundant across a 20$\times$ loss-weight range, confirming that collision avoidance arises from demonstration data, not geometric supervision.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 658
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-28T04:59:55.569280+00:00_

1	\section{Introduction}\label{sec:intro}
2	
3	Collision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\cite{li2026vlasafety}. The SafeLIBERO benchmark~\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through SDF-augmented training~\cite{zhang2025safevla}, constraint-based planning~\cite{yang2025cape}, and collision-free demonstrations~\cite{cofreeevla2026}. Our SDF-augmented Pi0~\cite{black2024pi0} reaches 91.5\% CAR across 800 episodes. The problem appears close to solved.
4	
5	\begin{figure}[t]
6	\centering
7	\includegraphics[width=\linewidth]{fig1_teaser}
8	\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). dfCAR filters out action-collapsed episodes where displacement falls below $\tau_d$; Pi0+A1's 91.5\% safety score drops to ${\approx}$\,0\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\,mm in all safe episodes, and dfCAR equals raw CAR (right).}
9	\label{fig:teaser}
10	\end{figure}
11	
12	It is not (Figure~\ref{fig:teaser}). Of the 732 collision-free episodes, 99.6\% exhibit displacement below 0.1\,mm; TSR is 0\% across all 800 episodes. The robot is frozen, not safe. The same pattern holds across all Pi0 configurations (Section~\ref{sec:fake_safety}). We term this \emph{fake safety}: \emph{action collapse} (near-zero actions producing zero collisions) renders reported CAR illusory, and standard evaluation cannot distinguish inaction from deliberate avoidance~\cite{karwowski2024goodhart}.
13	
14	We present a systematic investigation of this problem across the Pi0 and Pi0.5~\cite{black2024pi0} model families on SafeLIBERO, spanning 100+ experiments and 6000+ evaluation episodes. Three findings emerge.
15	
16	\textbf{Fake safety is pervasive.} We int
…[truncated 2138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 255
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-28T04:59:55.569860+00:00_

1	\documentclass{article}
2	
3	\PassOptionsToPackage{dvipsnames}{xcolor}
4	\usepackage{corl_2026}
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{multirow}
10	\usepackage{subcaption}
11	\graphicspath{{../../artifacts/figures/}}
12	
13	\title{Rethinking VLA Safety Evaluation:\\When 98\% of Collision Avoidance is an Illusion}
14	
15	\author{
16	  Anonymous Authors
17	}
18	
19	\begin{document}
20	
21	\maketitle
22	
23	\input{abstract}
24	
25	\keywords{VLA safety, collision avoidance, action collapse, signed distance fields}
26	
27	\input{introduction}
28	
29	\input{related_work}
30	
31	\input{method}
32	
33	\input{claim1}
34	
35	\input{claim2}
36	
37	\input{claim3}
38	
39	\input{discussion}
40	
41	\bibliography{references}
42	
43	\appendix
44	\input{appendix}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 1061
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-28T05:00:00.343626+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-28T05:00:00.799176+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-28T05:00:00.849986+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-28T05:00:01.304340+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-28T05:00:01.304917+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-28T05:00:02.215056+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-28T05:00:02.216665+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-28T05:00:02.710949+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 494
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-28T05:00:02.711545+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-28T05:00:03.165981+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-28T05:00:03.166312+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-28T05:00:04.121933+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-28T05:00:04.122372+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-28T05:00:04.582810+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 460
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-28T05:00:04.583242+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-28T05:00:04.836221+00:00_

1	\section{Experimental Setup and Metrics}\label{sec:method}
2	
3	\subsection{Benchmark and Models}\label{sec:benchmark}
4	
5	We evaluate on SafeLIBERO~\cite{hu2025vlsa}, the \textit{object\_pudding} suite (Level~II): four tabletop pick-and-place tasks with collision hazards and per-timestep collision detection. Two VLA families are tested: \textbf{Pi0} (${\sim}$2.5B)~\cite{black2024pi0} with flow matching~\cite{lipman2023flow}, and \textbf{Pi0.5} with broader pre-training. Table~\ref{tab:configurations} lists all configurations. Each uses 50 episodes per task (200 total); Pi0.5 multi-seed runs use 3 seeds (600 episodes). All metrics are computed using a fixed evaluation seed (seed\,=\,7); the reported $\pm$ values reflect variance across training seeds, not evaluation stochasticity. We report Collision Avoidance Rate (CAR), the fraction of collision-free episodes, and Task Success Rate (TSR), the fraction of episodes that complete the task~\cite{hu2025vlsa,zhang2025safevla}.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Training configurations. Trainable parameters exclude the frozen backbone.}
10	\label{tab:configurations}
11	\vspace{2pt}
12	\small
13	\begin{tabular}{llr}
14	\toprule
15	Configuration & Description & Trainable Params \\
16	\midrule
17	Pi0 Full-FT & Full fine-tune, flow-matching loss & ${\sim}$2.5B \\
18	Pi0 LoRA & LoRA adapters only & ${\sim}$33.5M \\
19	Pi0+A1 (SDF aux)\textsuperscript{$\dagger$} & LoRA + SDF decoder + EE extractor & ${\sim}$658K \\
20	Pi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\sim}$34.2M \\
21	Pi0.5 (pre-trained) & No fine-tuning & 0 \\
22	Pi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\sim}$33.5M \\
23	Pi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\lambda \in \{0.005, 0.01, 0.1\}$ & ${\sim}$34.2M \\
24	\bottomrule
25	\end{tabular}
26	\vspace{2pt}
27	\raggedright\footnotesize\textsuperscript{$\dagger$}LoRA weights not loaded due to parameter-name mismatch; only auxiliary heads trained.
28	\end{table}
29	
30	
…[truncated 1646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-28T05:00:04.836679+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-28T05:00:04.887257+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\S\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\S\ref{sec:ee_only}); and collision-free demonstrations, not geometric supervision, account for the measured avoidance gains (\S\ref{sec:avoidance_source}).
4	
5	\paragraph{Why EE-only SDF fails.}
6	Two independent causes explain the null result. \textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\sim}$26\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\S\ref{sec:avoidance_source}). Even at $\lambda = 0.1$ (20$\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), confirming that Level~A signal masking is not the binding constraint---the failure is architectural. \textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \emph{reduces} CAR by 6--10\,pp below unrefined baselines (\S\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.
7	
8	\paragraph{Implications for evaluation.}
9	dfCAR corrects action-collapse contamination using only EE position l
…[truncated 1674 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-28T05:00:08.775343+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-28T05:00:09.231217+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Vision-Language-Action Models.}
4	VLA models combine pretrained vision-language backbones with action prediction for generalist manipulation~\cite{brohan2023rt2,black2024pi0,chi2023diffusionpolicy,kim2024openvla}. Recent work enhances spatial reasoning through auxiliary 3D supervision~\cite{li2025spatialforcing,li2025qdepth,depthvla2025}, but safety considerations remain largely absent: most VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance from incidental collision-free trajectories.
5	
6	\paragraph{Safety in Robot Learning.}
7	Safety-aware approaches span training-time constrained RL~\cite{zhang2025safevla} and test-time filters: control barrier functions~\cite{hu2025vlsa}, collision risk gating~\cite{cofreeevla2026}, inverse kinematics QP~\cite{spalter2024ikinqp}, and diffusion-process collision costs~\cite{li2024langguided,yang2025cape}. SafeDiffuser~\cite{xiao2025safediffuser} integrates control barrier functions directly into diffusion denoising to enforce safety invariance during planning; like other test-time shields, it does not learn intrinsic collision awareness within the policy. A recent survey~\cite{li2026vlasafety} categorizes these into runtime shields, constrained optimization, and representation-based methods. Common to all is that safety is imposed externally rather than learned within the policy's representations. This work tests whether auxiliary SDF supervision can produce intrinsic collision awareness.
8	
9	\paragraph{Signed Distance Functions in Robotics.}
10	SDFs encode minimum surface distance, where the sign indicates free space or penetration. Neural SDFs~\cite{park2019deepsdf} enable continuous shape representation; in robotics, SDFs serve perception~\cite{ortiz2022isdf}, planning~\cite{huang2023voxposer,vasilopoulos2023ramp}, and differentiable collision detection~\cite{zhi2021diffco}. CDF~\cite{li202
…[truncated 1445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-28T05:00:09.231639+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-28T05:00:09.733517+00:00_

1	\section{The Fake Safety Problem}\label{sec:fake_safety}
2	
3	Standard CAR assumes that collision-free episodes reflect deliberate avoidance. This assumption is systematically violated: in every Pi0 configuration tested, over 99\% of collision-free episodes are action-collapse artifacts (Table~\ref{tab:fake_safety}).\footnote{Pi0-family values report obstacle displacement from the original protocol; Pi0.5 reports EE displacement from the rotation-corrected protocol (\S\ref{sec:dfcar}). Sub-millimeter displacement indicates action collapse in both cases.} Applying dfCAR collapses all three to ${\approx}$\,0\%. Pi0+A1 achieves the \emph{highest} raw CAR (91.5\%) because more complete action collapse (from a parameter-name mismatch preventing LoRA loading; Table~\ref{tab:configurations}) yields higher fake safety. Pi0.5 validates the metric from the opposite direction: every safe episode exceeds 200\,mm displacement, and dfCAR equals raw CAR (28.5\%). The displacement distribution is sharply bimodal (Appendix~\ref{sec:appendix_displacement}), with a five-order-of-magnitude gap that makes $\tau_d$ robust.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Fake safety decomposition on SafeLIBERO. dfCAR excludes episodes with displacement $< \tau_d = 0.1$\,mm.}
8	\label{tab:fake_safety}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	Method & Ep. & CAR (\%) & TSR (\%) & Fake Safe (\%) & dfCAR (\%) \\
14	\midrule
15	Pi0 Full-FT  & 200 & 83.0 & 0.5 & 99.4 & $\approx$\,0 \\
16	Pi0 LoRA     & 200 & 82.0 & 0.0 & ${\sim}$99 & $\approx$\,0 \\
17	Pi0+A1 (SDF) & 800 & 91.5 & 0.0 & 99.6 & $\approx$\,0$^*$ \\
18	\midrule
19	Pi0.5  & 200 & 28.5 & 71.5 & 0.0 & 28.5 \\
20	\bottomrule
21	\end{tabular}
22	\vspace{1pt}
23	{\footnotesize $^*$\,3/732 safe episodes above threshold; denominator too small for reliable rate.}
24	\end{table}
25	
26	Figure~\ref{fig:tsr_car_scatter} reveals spatial structure in the TSR-CAR plane.\label{sec:anticorrelation} Pi0-family models cluster
…[truncated 867 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-28T05:00:09.733927+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-28T05:00:10.186235+00:00_

1	\section{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\label{sec:ee_only}
2	
3	Could a perfect SDF signal enable effective EE-only refinement? We replace the learned SDF with ground-truth distance fields from the simulation geometry (\S\ref{sec:oracle_setup}). Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_bar} show that all three oracle variants achieve \emph{lower} CAR than unrefined baselines: the best oracle (76.9\%) falls 5.1 points below LoRA (82.0\%). Refinement with perfect distance information produces more collisions, not fewer.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\ref{sec:appendix_pertask_oracle}.}
8	\label{tab:oracle}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccc}
12	\toprule
13	Method & CAR (\%) & Fake Safe (\%) & Refines/ep \\
14	\midrule
15	LoRA baseline (no refine) & 82.0 & 99.4 & -- \\
16	Full-FT baseline (no refine) & 83.0 & -- & -- \\
17	\midrule
18	Oracle-adaptive (GT, dyn.\ $\alpha$) & 75.0 & 98.3 & 14.2 \\
19	Oracle-fixed (GT, $\alpha{=}0.005$) & 73.1 & 98.3 & 14.8 \\
20	Oracle-feature (GT, feat.\ space) & 76.9 & 96.7 & 241.7 \\
21	\midrule
22	A3 learned SDF & 77.1 & -- & 0.0 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	\begin{figure}[t]
28	\centering
29	\includegraphics[width=0.85\linewidth]{fig_oracle_bar.pdf}
30	\caption{CAR for oracle SDF refinement versus unrefined baselines. All GT oracle variants underperform baselines despite perfect distance information.}
31	\label{fig:oracle_bar}
32	\end{figure}
33	
34	Per-task analysis reveals the mechanism (Appendix~\ref{sec:appendix_pertask_oracle}). On the one task where the EE is the primary collision body, oracle refinement helps (+9 points). On the remaining three, the SDF gradient pushes the EE away from obstacles but rotates intermediate arm links into obstacle volumes; the net effect is one collision trad
…[truncated 280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-28T05:00:10.186767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-28T05:00:10.688980+00:00_

1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\times$ range of loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO. SDF adds no measurable CAR beyond LoRA-only across the full tested range $\lambda \in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) \\
14	\midrule
15	Pi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\
16	\midrule
17	LoRA-only (no SDF) & 3 & 51.5\,$\pm$\,0.0 & 54.67\,$\pm$\,2.02 & 0.391 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.29 & 0.387 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.33\,$\pm$\,1.61 & 0.389 \\
20	LoRA+SDF $\lambda{=}0.1$ & 3 & 50.2\,$\pm$\,3.9 & 57.00\,$\pm$\,2.18 & 0.394 \\
21	\bottomrule
22	\end{tabular}
23	\vspace{1pt}
24	\end{table}
25	
26	Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.67\%) with zero frozen episodes and displacement above 0.37\,m, confirming genuine avoidance. Adding SDF supervision produces no measurable benefit across the full tested range: LoRA-only CAR (54.67\%) is statistically indistinguishable from all SDF conditions including $\lambda = 0.1$ (57.00\%, $p = 0.131$; Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,57.5\%\footnote{Single seed (s2); 
…[truncated 2334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-28T05:00:10.689562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-28T05:00:10.790779+00:00_

1	\section{Displacement Distribution}
2	\label{sec:appendix_displacement}
3	
4	\begin{figure}[h]
5	\centering
6	\includegraphics[width=\linewidth]{fig2_ee_displacement_distribution}
7	\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\,$\mu$m, while Pi0.5 episodes (orange) exceed 200\,mm. The five-order-of-magnitude gap makes $\tau_d$ robust to any value in $[2, 200]$\,mm.}
8	\label{fig:displacement}
9	\end{figure}
10	
11	\section{Displacement Threshold Sensitivity Analysis}
12	\label{sec:appendix_threshold}
13	
14	To validate the robustness of our displacement threshold $\tau_d$, we evaluate the frozen rate across four orders of magnitude. Table~\ref{tab:threshold_sensitivity} shows that the fake safety pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\% frozen rate even at the most conservative setting.
15	
16	\begin{table}[h]
17	\centering
18	\caption{Frozen rate (\% of episodes with $d_\mathrm{max} < \tau_d$) across threshold values.}
19	\label{tab:threshold_sensitivity}
20	\begin{tabular}{lccc}
21	\toprule
22	$\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\
23	\midrule
24	0.001 mm (1\,$\mu$m) & 73.9 & 0.0 & 0.0 \\
25	0.1 mm  & 99.6 & 0.0 & 0.0 \\
26	1.0 mm  & 100.0 & 0.0 & 0.0 \\
27	10 mm   & 100.0 & 0.0 & 0.0 \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	The choice of $\tau_d = 0.1$\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\,mm per step. Even at $\tau_d = 1$\,$\mu$m, 73.9\% of A1-LoRA safe episodes are classified as frozen, while all Pi0.5 episodes remain above threshold at every level tested.
33	
34	Table~\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\
…[truncated 22842 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-28T05:00:18.348065+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2025 2024 review form scoring dimensions soundness significance clarity rating scale OpenReview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2025 2024 review form scoring dimensions soundness significance clarity rating scale OpenReview"
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-28T05:00:20.005199+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract any reviewer form dimensions, scoring criteria, or review template information. Also look for any information about anonymity requirements, page limits, template specification, and required sections."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/instruction-for-authors",
    "prompt": "Extract any reviewer form dimensions, scoring criteria, or review template information. Also look for any information about anonymity requirements, page limits, template specification, and required sections."
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-28T05:00:24.372866+00:00_

# CoRL 2026 Author Instructions Summary

## Anonymity Requirements
The conference operates under **double-blind review**, requiring all submissions to be anonymized. Papers and reviews become public and de-anonymized after decisions are announced.

## Page Limits & Format
- **Initial submission**: 8 pages maximum for main text
- **Camera-ready version**: 9 pages (1 additional page to incorporate reviewer feedback)
- Acknowledgments, references, and optional appendix do not count toward page limits
- Required template available via Google Drive link
- Reviewers are not obligated to read appendices

## Required Sections
Authors must include:
- **Limitations section** (counted within the 8-page limit) describing assumptions, failure modes, and constraints
- Sufficient detail for reproducibility

## Supplementary Materials
- Single zip file through OpenReview
- Video submissions encouraged: maximum 250 MB, under 3 minutes suggested length
- Note: PMLR prohibits video submission as supplementary material for camera-ready versions; authors should host materials independently

## Reviewer Assignment Notes
The instructions note that "at least two reviewers per paper" is the target, though specific scoring rubrics or evaluation criteria are not detailed in this document.

## Reciprocal Reviewing
At least one author must qualify as a reviewer (prior publications at robotics/learning conferences or equivalent journals).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebFetch",
  "elapsed_ms": 4367
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-28T05:00:41.242832+00:00_

Web search results for query: "CoRL 2025 2024 review form scoring dimensions soundness significance clarity rating scale OpenReview"

Links: [{"title":"CoRL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review","url":"https://arxiv.org/pdf/2509.25701"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Can LLM feedback enhance review quality? A randomized study of 20K   reviews at ICLR 2025","url":"https://arxiv.org/pdf/2504.09737"}]

I found a reference to CoRL 2024 review instructions. Let me search for more specific information about the review form and scoring dimensions used by CoRL 2025.

Links: [{"title":"CoRL 2025 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2025"},{"title":"CoRL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"CoRL 2025 Workshop Open Hardware | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FWorkshop%2FOpen_Hardware"},{"title":"CoRL 2025 Workshop H2R | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FWorkshop%2FH2R"},{"title":"CoRL 2025 Demos | OpenReview","url":"https://openreview.ne
…[truncated 5782 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebSearch",
  "elapsed_ms": 22894
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-28T05:00:47.021183+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete review form: all scoring dimensions, rating scales (1-10 or whatever scale they use), definitions for each rating level, and any specific criteria. I need the exact dimensions like soundness, novelty, clarity, significance, etc. with their scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete review form: all scoring dimensions, rating scales (1-10 or whatever scale they use), definitions for each rating level, and any specific criteria. I need the exact dimensions like soundness, novelty, clarity, significance, etc. with their scales."
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-28T05:00:48.075615+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, all scoring dimensions, rating scales, and definitions. I need the exact dimensions and their rating scales used for CoRL 2024 reviews."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, all scoring dimensions, rating scales, and definitions. I need the exact dimensions and their rating scales used for CoRL 2024 reviews."
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-28T05:00:51.489054+00:00_

# CoRL 2024 Review Form Criteria

Based on the provided webpage content, **the specific review form criteria, scoring dimensions, and rating scales are not included in this document.**

The page only outlines:

## What IS Specified:

**Review Criteria for Regular Papers:**
- "significance and novelty of the results, either theoretical or empirical"
- Degree of objective establishment and potential scientific/technological impact
- Relevance to robotic learning

**Desk Rejection Criteria:**
Three grounds for rejection are listed: formatting issues, anonymity violations, and scope misalignment.

## What IS NOT Specified:

The document does not contain:
- Numerical rating scales (e.g., 1-5, 1-10)
- Specific scoring dimensions (e.g., "originality," "clarity," "impact")
- Detailed evaluation rubrics
- Point distributions or weighting schemes
- Reviewer confidence scales

**Conclusion:** To obtain the complete review form with exact dimensions and rating scales, you would need to access the actual review submission interface or contact the CoRL 2024 organizing committee directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebFetch",
  "elapsed_ms": 3413
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-28T05:00:51.590170+00:00_

# CoRL 2023 Review Form Analysis

Based on the provided guidelines, the document does **not include** the complete review form with specific scoring dimensions, rating scales, or numerical definitions.

## What IS Specified:

The guidelines identify **six evaluation dimensions** that reviewers should address:

1. **Originality** - "Are the problems or methods new?"
2. **Quality** - "Is the submission technically sound?"
3. **Clarity** - "Is the submission clearly written?"
4. **Significance** - "Are the results important?"
5. **Relevance** - "Does the paper address a problem in robot learning?"
6. **Limitations** - Assessment of how authors report constraints

## What IS NOT Provided:

- **Numerical rating scales** (e.g., 1-10, 1-5)
- **Rating level definitions** (e.g., "5=Excellent, 4=Good")
- **Complete review form template**
- **Specific scoring rubrics**

The document states reviewers will "receive information for each step and technical instructions by Email via the OpenReview system," suggesting the actual form with scales is distributed separately through OpenReview's platform rather than detailed in these guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebFetch",
  "elapsed_ms": 4568
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-28T05:04:32.825690+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2024 OpenReview review form \"soundness\" \"presentation\" \"contribution\" rating scale 1-4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2024 OpenReview review form \"soundness\" \"presentation\" \"contribution\" rating scale 1-4"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-28T05:04:47.232749+00:00_

Web search results for query: "CoRL 2024 OpenReview review form "soundness" "presentation" "contribution" rating scale 1-4"

Links: [{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"ICML 2024 Reviewer Instructions","url":"https://icml.cc/Conferences/2024/ReviewerInstructions"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"(PDF) Insights from the ICLR Peer Review and Rebuttal Process","url":"https://www.researchgate.net/publication/397780200_Insights_from_the_ICLR_Peer_Review_and_Rebuttal_Process"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"Insights from the ICLR Peer Review and Rebuttal Process","url":"https://arxiv.org/pdf/2511.15462"},{"title":"CoRL 2024 Conference Submissions | OpenReview","url":"https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"}]

Let me search more specifically for the CoRL 2024 review form details:

Links: [{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL 2024 - Lifelong Learning for Home Robots","url":"https://llhomerobots.github.io/"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"8th CoRL 2024: Munich, Germany","url":"https://dblp.org/db/conf/corl/corl2024.html"},{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"CoRL 2024","url":"https://2024.corl.org/"},{"title":"CoRL 2024 - Instruction for Authors","url":"https://2024.corl.org/contributions/instruction-for-authors"},{"title":"Peer assessment of outpatient consultation letters – feasibil
…[truncated 3573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebSearch",
  "elapsed_ms": 14407
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-28T05:04:54.011501+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference",
  "prompt": "Find any paper submission that has reviews. Extract the review form fields and rating scales used (e.g., soundness 1-4, presentation 1-4, contribution 1-4, overall rating 1-10, confidence 1-5). I need the exact dimensions and scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference",
    "prompt": "Find any paper submission that has reviews. Extract the review form fields and rating scales used (e.g., soundness 1-4, presentation 1-4, contribution 1-4, overall rating 1-10, confidence 1-5). I need the exact dimensions and scales."
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-28T05:04:57.245297+00:00_

I cannot extract the review form fields and rating scales you've requested based on the provided content. The webpage displays only the CoRL 2024 conference submissions list with paper titles, authors, and publication dates—it does not include any actual reviews or review form specifications.

To find this information, you would need to:
1. Click on individual paper forum links (e.g., the forum IDs like "Oce2215aJE")
2. Navigate to the reviews section within each paper's discussion page
3. Examine the actual review documents to identify the rating dimensions and scales used

The current page is a table of contents for submissions, not a review interface.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebFetch",
  "elapsed_ms": 3233
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-28T05:05:02.474408+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/forum?id=Oce2215aJE",
  "prompt": "Extract the review form dimensions and rating scales. I need to see what fields reviewers filled out: things like \"soundness\", \"presentation\", \"contribution\", \"overall\", \"confidence\", and what numerical scales each uses (e.g., 1-4, 1-5, 1-10). Extract the full review form structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/forum?id=Oce2215aJE",
    "prompt": "Extract the review form dimensions and rating scales. I need to see what fields reviewers filled out: things like \"soundness\", \"presentation\", \"contribution\", \"overall\", \"confidence\", and what numerical scales each uses (e.g., 1-4, 1-5, 1-10). Extract the full review form structure."
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-28T05:05:06.491566+00:00_

# Review Form Information Not Available

The provided webpage content does not contain review form dimensions or rating scales. The page displays metadata about the "Body Transformer" paper published at CoRL 2024, including the abstract, author names, and links to supplementary materials.

To access the actual review form structure, you would need to:

1. Navigate to the full paper review page on OpenReview
2. Check the venue's submission guidelines (CoRL 2024 Conference)
3. Contact OpenReview directly for review form specifications

The current content only shows publication details, not the reviewer evaluation criteria or numerical scales used during the peer review process.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "WebFetch",
  "elapsed_ms": 4017
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-28T05:06:52.374042+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 3 审稿报告（写作质量 + 格式合规 + Limitations + 伦理 + 图表 + 引用）\n\n---\n\n## 总体评分\n\n**Overall**: 6/10（Weak Accept / Borderline）\n\n**一句话总结**: 写作清晰、结构严谨的诊断性论文，dfCAR 定义精确且 threshold robustness 论证充分；但 Limitations 遗漏仿真限制、Broader Impact 严重不足、标题存在夸大倾向，这些问题在 CoRL 这一强调 real-robot relevance 的会议上尤为突出。\n\n---\n\n## 官方维度打分\n\n基于 CoRL 2023 Reviewer Guidelines 六维度（Originality, Quality, Clarity, Significance, Relevance, Limitations）+ OpenReview 通用量表：\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Clarity (Presentation) | 3/4 (Good) | 整体可读性强，叙事弧线清晰（诊断→机理→归因），概念首次出现即定义；但存在术语混用和 abstract 过度压缩 |\n| Relevance | 3/4 (Good) | 直接针对 VLA 安全评估问题，与机器人学习高度相关；但全部实验在仿真环境完成，无 sim-to-real 证据 |\n| Limitations | 2/4 (Fair) | Limitations 段存在但内容不完整——最关键的\"仅仿真\"未明确声明；Broader Impact 仅一句话 |\n| Contribution (从写作/呈现角度) | 3/4 (Good) | dfCAR 指标定义清晰、有方程式支撑、threshold sensitivity 分析充分（Appendix B）|\n\n注：Originality 和 Quality (Soundness) 不在我的审查范围内，由其他 Reviewer 评估。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Limitations 未明确声明\"全部实验仅在仿真环境完成，无真实机器人验证\"\n\n- 具体位置：Section 7, Limitations 段落（page 7-8）\n- 问题：Limitations 段提到\"tabletop setting with fixed-base manipulator and known obstacles may not generalize to mobile platforms\"，但从未明确说出\"所有实验均在 SafeLIBERO 仿真环境完成，未在真实机器人上验证\"这一事实。CoRL 2026 Call for Papers 明确要求：仿真工作需提供\"convincing evidence that simulation experiments are transferable to real robots\"（来源：[CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)）。论文未提供任何 sim-to-real transferability 证据，也未在 Limitations 中承认这一局限。\n- 为什么影响接收：CoRL 是机器人学习会议，强调 real-robot relevance。审稿人和 AC 会直接关注这个缺失。隐藏仿真限制而非正面讨论，会降低论文的可信度。\n- 建议修改方向：在 Limitations 段首句即声明\"All experiments are conducted in the SafeLIBERO simulation environment; real-robot validation remains future work.\" 并简要讨论仿真碰撞检测（MuJoCo contact detection）与真实接触感知的差异。\n\n**N2** [critical] Broader Impact 严重不足——仅一句话\n\n- 具体位置：Section 7, Broader Impact 段落（page 8）\n- 问题：全文：\"Contaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks. dfCAR exposes this gap with minimal changes to existing protocols.\" 仅此一句。\n- 为什么影响接收：本文核心 claim 是\"当前 VLA 安全评估根本性失效\"，标题直接宣称\"98% of Collision Avoidance is an Illusion\"。这一断言直接影响已发表工作（SafeVLA [3]、CoFreeVLA [5]、VLSA [2]）的声誉和可信度。对于一篇挑战现有安全评估范式的论文，Broader Impact 需要讨论：\n  (a) 对 downstream deployment 的潜在负面影响——读者可能过度解读为\"安全措施无用\"，从而减少对安全研究的投入；\n  (b) 对被批评方法的 responsible disclosure 考量——声称已发表方法无效是否需要更审慎的措辞和更完整的上下文；\n  (c) dfCAR 本身的局限（仅基于 EE displacement，是否可能产生新的 false negatives）。\n- 建议修改方向：扩展至 3-5 句，覆盖上述三方面。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 标题 \"When 98% of Collision Avoidance is an Illusion\" 有夸大倾向\n\n- 具体位置：Title（page 1）\n- 问题：98% 这个数字来自 Pi0+A1 配置（Table 2, page 4：99.6% fake safe rate），而该配置因 parameter-name mismatch 导致 LoRA 权重未加载（Section 3.3, method.tex line 44），实际上是一个 broken 配置（TSR=0%）。Pi0.5 的 28.5% CAR 全部来自真实避障（dfCAR = 28.5%）。标题暗示\"几乎所有碰撞避免都是假的\"，但这仅适用于 Pi0 系列的 action collapse 问题，而非 VLA 安全评估的普遍状况。\n- 建议：考虑更精确的标题，如 \"Rethinking VLA Safety Evaluation: Action Collapse Contaminates Collision Avoidance Metrics\" 或在标题中明确 Pi0 的范围。至少在 abstract 首句更快地限定 scope。\n\n**W2** [warning] 术语 \"frozen episodes\" 与 \"action-collapsed episodes\" 混用\n\n- 具体位置：全文多处，尤其 Section 4（claim1.tex）、Table 2 列名 \"Fake Safe (%)\"、Section 6 \"zero frozen episodes\"、Appendix B \"frozen rate\"\n- 问题：论文使用至少三种表述指代同一概念：\n  - \"action collapse\" / \"action-collapsed episodes\"（正式术语，Introduction 定义）\n  - \"frozen episodes\" / \"frozen rate\"（通俗表述，多处使用）\n  - \"fake safety\" / \"fake safe\"（Table 2 列名）\n  \n  虽然上下文通常可以消歧，但对首次阅读者而言，三套术语在 8 页内交替出现增加认知负担。特别是 Table 2 的列名\"Fake Safe (%)\"与正文定义的\"action-collapsed\"不完全等价——一个 frozen episode 是 fake safe，但概念上 fake safe 的范围可能更广。\n- 建议：在 Section 3.2 或 Section 4 首次使用时明确声明等价关系：\"We term such episodes *action-collapsed* (equivalently, *frozen*); their contribution to CAR constitutes *fake safety*.\" 之后在技术讨论中统一使用一个术语。\n\n**W3** [warning] Abstract 过度压缩，第 5 句信息密度过高\n\n- 具体位置：abstract.tex, line 5\n- 问题：该句将三个独立发现压缩为一个 195+ 词的长句（从 \"We further show\" 到 \"3 seeds).\"），包含：(i) EE-only SDF 无法 deliver collision avoidance，(ii) oracle refinement 降低 CAR，(iii) collision-free demonstrations 足以解释所有 avoidance gains，(iv) SDF supervision 冗余的统计证据。一个 abstract 句子不应承载四个独立 claim 加统计数据。\n- 建议：拆分为 2-3 句，每句对应一个核心发现。移除 abstract 中的具体 p-value 和 λ 值，留在正文。\n\n**W4** [warning] Figure 1（teaser）未出现在第一页\n\n- 具体位置：Figure 1, page 2\n- 问题：Teaser figure 的目的是在第一页即传达核心信息，但 Figure 1 被 LaTeX 排版推到第二页。第一页仅包含 title + abstract + keywords + introduction 开头文字，没有任何视觉元素。\n- 建议：压缩 abstract 长度（当前约 150 词，可精简至 120 词）或调整 figure placement（使用 `\\begin{figure*}[t!]` 或调整 introduction 首段长度），确保 teaser 出现在第一页。\n\n---\n\n## 小问题（不影响接收）\n\n- **[Minor-1]** Pi0.5 在全文中被广泛使用但仅通过 Pi0 的引用 `[black2024pi0]` 间接引用。如果 Pi0.5 有独立的技术报告或论文，应单独引用。如果是同一出处，应在首次提及时说明\"Pi0.5 [6], a successor model with broader pre-training\"。\n\n- **[Minor-2]** 引用 [7] Karwowski et al. 2024 \"Goodhart's law in reinforcement learning\" — ICLR 2024。需确认此引用是否真实存在（Goodhart's law 在 ML 文献中有多种引用方式）。\n\n- **[Minor-3]** 多个引用为 2026 年 arXiv preprint（[1] li2026vlasafety arXiv:2603, [5] cofreeevla2026 arXiv:2603, chen2026cssdfnet, snyder2026beyond）。如有已发表版本（如会议接收），应更新引用至正式出版版本。\n\n- **[Minor-4]** Section 7 的 Limitations 和 Broader Impact 是 Discussion 内的 `\\paragraph{}` 而非独立 `\\subsection{}`。虽然 CoRL 2026 未明确要求独立章节，但使用独立 subsection 能提高可见性和可读性。\n\n- **[Minor-5]** 数学符号：$\\tau_d$ 在 Section 3.2 首次定义为 0.1 mm（Eq. 1），但 Appendix B Table 5 又使用 $d_\\mathrm{max}$ 作为 threshold 值的下标符号，微小不一致。\n\n- **[Minor-6]** Table 1 脚注 \"$^\\dagger$ LoRA weights not loaded due to parameter-name mismatch; only auxiliary heads trained\" 是一个重要的实验说明（这直接导致了 Pi0+A1 的 action collapse），但脚注字体很小且不够醒目。建议在 Section 3.3 或 Section 4 正文中更显著地说明此点。\n\n- **[Minor-7]** 匿名性检查通过：作者标注为 \"Anonymous Authors\"，无 GitHub 链接、项目名称或可识别的自引。提到 \"OpenPi\" 是公开框架，不构成 de-anonymization。页脚正确标注 \"Submitted to the 10th Conference on Robot Learning (CoRL, 2026). Do not distribute.\" ✓\n\n- **[Minor-8]** 引用格式整体一致（numeric natbib），Figure/Table 编号连续（Figure 1-6, Table 1-15），booktabs 风格表格，无多余竖线。✓\n\n---\n\n## 主要优势\n\n1. **写作结构清晰**：论文遵循\"诊断→机理→归因\"的叙事弧线（Section 4→5→6），每节有明确的 claim 和对应 evidence，逻辑链条完整。Section 之间的过渡自然流畅。\n\n2. **关键概念定义完整**：dfCAR（Eq. 1, Section 3.2）、action collapse（Introduction paragraph 2）、fake safety（Introduction paragraph 2）均在首次出现时给出精确定义。dfCAR 的 threshold robustness 通过 Appendix B 的 5-order-of-magnitude sensitivity analysis 充分论证。\n\n3. **无明显 AI 写作痕迹**：通读全文未发现 \"notably\", \"crucially\", \"it is worth noting\", \"we posit\" 等典型 AI 写作标记。用词直接、数据驱动，符合实证研究论文的风格。\n\n4. **图表质量良好**：Figure 2（TSR-CAR scatter）直观展示了 Pi0 vs Pi0.5 的行为差异；Figure 4（lambda curve）清晰呈现 SDF 冗余性。所有表格使用 booktabs 风格，caption 自含。\n\n5. **Appendix 详尽**：17 页中 10 页为 appendix（Section A-L），包含 threshold sensitivity、per-task breakdown、null distribution 构建、step-wise checkpoint analysis、cross-scene validation、evaluation seed robustness 等。这些补充材料显著增强了主要 claims 的可信度。\n\n6. **格式基本合规**：使用 `corl_2026` 模板 ✓，正文 ≤8 页 ✓，双盲匿名 ✓，包含 Limitations ✓，引用格式一致 ✓。\n\n---\n\n## 格式合规清单\n\n| 检查项 | 状态 | 备注 |\n|--------|------|------|\n| 模板 corl_2026 | ✅ | `\\usepackage{corl_2026}` in main.tex |\n| 正文 ≤ 8 页 | ✅ | 主体内容 ~7.5 页，references 从 page 8 下半开始 |\n| 双盲匿名 | ✅ | \"Anonymous Authors\"，无 de-anonymizing 信息 |\n| Limitations section | ⚠️ | 存在但内容不完整（缺仿真限制声明）|\n| Figure/Table 编号连续 | ✅ | Fig 1-6, Table 1-15 |\n| 引用格式一致 | ✅ | Numeric natbib throughout |\n| 数学符号一致 | ✅ | τ_d, λ, d_max 使用一致（minor 例外见 Minor-5）|\n| Booktabs 表格 | ✅ | 全部表格使用 \\toprule/\\midrule/\\bottomrule |\n| Submission footer | ✅ | \"Submitted to the 10th Conference on Robot Learning (CoRL, 2026)\" |",
  "reviewer_id": "3",
  "project": "diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 3 审稿报告（写作质量 + 格式合规 + Limitations + 伦理 + 图表 + 引用）\n\n---\n\n## 总体评分\n\n**Overall**: 6/10（Weak Accept / Borderline）\n\n**一句话总结**: 写作清晰、结构严谨的诊断性论文，dfCAR 定义精确且 threshold robustness 论证充分；但 Limitations 遗漏仿真限制、Broader Impact 严重不足、标题存在夸大倾向，这些问题在 CoRL 这一强调 real-robot relevance 的会议上尤为突出。\n\n---\n\n## 官方维度打分\n\n基于 CoRL 2023 Reviewer Guidelines 六维度（Originality, Quality, Clarity, Significance, Relevance, Limitations）+ OpenReview 通用量表：\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Clarity (Presentation) | 3/4 (Good) | 整体可读性强，叙事弧线清晰（诊断→机理→归因），概念首次出现即定义；但存在术语混用和 abstract 过度压缩 |\n| Relevance | 3/4 (Good) | 直接针对 VLA 安全评估问题，与机器人学习高度相关；但全部实验在仿真环境完成，无 sim-to-real 证据 |\n| Limitations | 2/4 (Fair) | Limitations 段存在但内容不完整——最关键的\"仅仿真\"未明确声明；Broader Impact 仅一句话 |\n| Contribution (从写作/呈现角度) | 3/4 (Good) | dfCAR 指标定义清晰、有方程式支撑、threshold sensitivity 分析充分（Appendix B）|\n\n注：Originality 和 Quality (Soundness) 不在我的审查范围内，由其他 Reviewer 评估。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Limitations 未明确声明\"全部实验仅在仿真环境完成，无真实机器人验证\"\n\n- 具体位置：Section 7, Limitations 段落（page 7-8）\n- 问题：Limitations 段提到\"tabletop setting with fixed-base manipulator and known obstacles may not generalize to mobile platforms\"，但从未明确说出\"所有实验均在 SafeLIBERO 仿真环境完成，未在真实机器人上验证\"这一事实。CoRL 2026 Call for Papers 明确要求：仿真工作需提供\"convincing evidence that simulation experiments are transferable to real robots\"（来源：[CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)）。论文未提供任何 sim-to-real transferability 证据，也未在 Limitations 中承认这一局限。\n- 为什么影响接收：CoRL 是机器人学习会议，强调 real-robot relevance。审稿人和 AC 会直接关注这个缺失。隐藏仿真限制而非正面讨论，会降低论文的可信度。\n- 建议修改方向：在 Limitations 段首句即声明\"All experiments are conducted in the SafeLIBERO simulation environment; real-robot validation remains future work.\" 并简要讨论仿真碰撞检测（MuJoCo contact detection）与真实接触感知的差异。\n\n**N2** [critical] Broader Impact 严重不足——仅一句话\n\n- 具体位置：Section 7, Broader Impact 段落（page 8）\n- 问题：全文：\"Contaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks. dfCAR exposes this gap with minimal changes to existing protocols.\" 仅此一句。\n- 为什么影响接收：本文核心 claim 是\"当前 VLA 安全评估根本性失效\"，标题直接宣称\"98% of Collision Avoidance is an Illusion\"。这一断言直接影响已发表工作（SafeVLA [3]、CoFreeVLA [5]、VLSA [2]）的声誉和可信度。对于一篇挑战现有安全评估范式的论文，Broader Impact 需要讨论：\n  (a) 对 downstream deployment 的潜在负面影响——读者可能过度解读为\"安全措施无用\"，从而减少对安全研究的投入；\n  (b) 对被批评方法的 responsible disclosure 考量——声称已发表方法无效是否需要更审慎的措辞和更完整的上下文；\n  (c) dfCAR 本身的局限（仅基于 EE displacement，是否可能产生新的 false negatives）。\n- 建议修改方向：扩展至 3-5 句，覆盖上述三方面。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 标题 \"When 98% of Collision Avoidance is an Illusion\" 有夸大倾向\n\n- 具体位置：Title（page 1）\n- 问题：98% 这个数字来自 Pi0+A1 配置（Table 2, page 4：99.6% fake safe rate），而该配置因 parameter-name mismatch 导致 LoRA 权重未加载（Section 3.3, method.tex line 44），实际上是一个 broken 配置（TSR=0%）。Pi0.5 的 28.5% CAR 全部来自真实避障（dfCAR = 28.5%）。标题暗示\"几乎所有碰撞避免都是假的\"，但这仅适用于 Pi0 系列的 action collapse 问题，而非 VLA 安全评估的普遍状况。\n- 建议：考虑更精确的标题，如 \"Rethinking VLA Safety Evaluation: Action Collapse Contaminates Collision Avoidance Metrics\" 或在标题中明确 Pi0 的范围。至少在 abstract 首句更快地限定 scope。\n\n**W2** [warning] 术语 \"frozen episodes\" 与 \"action-collapsed episodes\" 混用\n\n- 具体位置：全文多处，尤其 Section 4（claim1.tex）、Table 2 列名 \"Fake Safe (%)\"、Section 6 \"zero frozen episodes\"、Appendix B \"frozen rate\"\n- 问题：论文使用至少三种表述指代同一概念：\n  - \"action collapse\" / \"action-collapsed episodes\"（正式术语，Introduction 定义）\n  - \"frozen episodes\" / \"frozen rate\"（通俗表述，多处使用）\n  - \"fake safety\" / \"fake safe\"（Table 2 列名）\n  \n  虽然上下文通常可以消歧，但对首次阅读者而言，三套术语在 8 页内交替出现增加认知负担。特别是 Table 2 的列名\"Fake Safe (%)\"与正文定义的\"action-collapsed\"不完全等价——一个 frozen episode 是 fake safe，但概念上 fake safe 的范围可能更广。\n- 建议：在 Section 3.2 或 Section 4 首次使用时明确声明等价关系：\"We term such episodes *action-collapsed* (equivalently, *frozen*); their contribution to CAR constitutes *fake safety*.\" 之后在技术讨论中统一使用一个术语。\n\n**W3** [warning] Abstract 过度压缩，第 5 句信息密度过高\n\n- 具体位置：abstract.tex, line 5\n- 问题：该句将三个独立发现压缩为一个 195+ 词的长句（从 \"We further show\" 到 \"3 seeds).\"），包含：(i) EE-only SDF 无法 deliver collision avoidance，(ii) oracle refinement 降低 CAR，(iii) collision-free demonstrations 足以解释所有 avoidance gains，(iv) SDF supervision 冗余的统计证据。一个 abstract 句子不应承载四个独立 claim 加统计数据。\n- 建议：拆分为 2-3 句，每句对应一个核心发现。移除 abstract 中的具体 p-value 和 λ 值，留在正文。\n\n**W4** [warning] Figure 1（teaser）未出现在第一页\n\n- 具体位置：Figure 1, page 2\n- 问题：Teaser figure 的目的是在第一页即传达核心信息，但 Figure 1 被 LaTeX 排版推到第二页。第一页仅包含 title + abstract + keywords + introduction 开头文字，没有任何视觉元素。\n- 建议：压缩 abstract 长度（当前约 150 词，可精简至 120 词）或调整 figure placement（使用 `\\begin{figure*}[t!]` 或调整 introduction 首段长度），确保 teaser 出现在第一页。\n\n---\n\n## 小问题（不影响接收）\n\n- **[Minor-1]** Pi0.5 在全文中被广泛使用但仅通过 Pi0 的引用 `[black2024pi0]` 间接引用。如果 Pi0.5 有独立的技术报告或论文，应单独引用。如果是同一出处，应在首次提及时说明\"Pi0.5 [6], a successor model with broader pre-training\"。\n\n- **[Minor-2]** 引用 [7] Karwowski et al. 2024 \"Goodhart's law in reinforcement learning\" — ICLR 2024。需确认此引用是否真实存在（Goodhart's law 在 ML 文献中有多种引用方式）。\n\n- **[Minor-3]** 多个引用为 2026 年 arXiv preprint（[1] li2026vlasafety arXiv:2603, [5] cofreeevla2026 arXiv:2603, chen2026cssdfnet, snyder2026beyond）。如有已发表版本（如会议接收），应更新引用至正式出版版本。\n\n- **[Minor-4]** Section 7 的 Limitations 和 Broader Impact 是 Discussion 内的 `\\paragraph{}` 而非独立 `\\subsection{}`。虽然 CoRL 2026 未明确要求独立章节，但使用独立 subsection 能提高可见性和可读性。\n\n- **[Minor-5]** 数学符号：$\\tau_d$ 在 Section 3.2 首次定义为 0.1 mm（Eq. 1），但 Appendix B Table 5 又使用 $d_\\mathrm{max}$ 作为 threshold 值的下标符号，微小不一致。\n\n- **[Minor-6]** Table 1 脚注 \"$^\\dagger$ LoRA weights not loaded due to parameter-name mismatch; only auxiliary heads trained\" 是一个重要的实验说明（这直接导致了 Pi0+A1 的 action collapse），但脚注字体很小且不够醒目。建议在 Section 3.3 或 Section 4 正文中更显著地说明此点。\n\n- **[Minor-7]** 匿名性检查通过：作者标注为 \"Anonymous Authors\"，无 GitHub 链接、项目名称或可识别的自引。提到 \"OpenPi\" 是公开框架，不构成 de-anonymization。页脚正确标注 \"Submitted to the 10th Conference on Robot Learning (CoRL, 2026). Do not distribute.\" ✓\n\n- **[Minor-8]** 引用格式整体一致（numeric natbib），Figure/Table 编号连续（Figure 1-6, Table 1-15），booktabs 风格表格，无多余竖线。✓\n\n---\n\n## 主要优势\n\n1. **写作结构清晰**：论文遵循\"诊断→机理→归因\"的叙事弧线（Section 4→5→6），每节有明确的 claim 和对应 evidence，逻辑链条完整。Section 之间的过渡自然流畅。\n\n2. **关键概念定义完整**：dfCAR（Eq. 1, Section 3.2）、action collapse（Introduction paragraph 2）、fake safety（Introduction paragraph 2）均在首次出现时给出精确定义。dfCAR 的 threshold robustness 通过 Appendix B 的 5-order-of-magnitude sensitivity analysis 充分论证。\n\n3. **无明显 AI 写作痕迹**：通读全文未发现 \"notably\", \"crucially\", \"it is worth noting\", \"we posit\" 等典型 AI 写作标记。用词直接、数据驱动，符合实证研究论文的风格。\n\n4. **图表质量良好**：Figure 2（TSR-CAR scatter）直观展示了 Pi0 vs Pi0.5 的行为差异；Figure 4（lambda curve）清晰呈现 SDF 冗余性。所有表格使用 booktabs 风格，caption 自含。\n\n5. **Appendix 详尽**：17 页中 10 页为 appendix（Section A-L），包含 threshold sensitivity、per-task breakdown、null distribution 构建、step-wise checkpoint analysis、cross-scene validation、evaluation seed robustness 等。这些补充材料显著增强了主要 claims 的可信度。\n\n6. **格式基本合规**：使用 `corl_2026` 模板 ✓，正文 ≤8 页 ✓，双盲匿名 ✓，包含 Limitations ✓，引用格式一致 ✓。\n\n---\n\n## 格式合规清单\n\n| 检查项 | 状态 | 备注 |\n|--------|------|------|\n| 模板 corl_2026 | ✅ | `\\usepackage{corl_2026}` in main.tex |\n| 正文 ≤ 8 页 | ✅ | 主体内容 ~7.5 页，references 从 page 8 下半开始 |\n| 双盲匿名 | ✅ | \"Anonymous Authors\"，无 de-anonymizing 信息 |\n| Limitations section | ⚠️ | 存在但内容不完整（缺仿真限制声明）|\n| Figure/Table 编号连续 | ✅ | Fig 1-6, Table 1-15 |\n| 引用格式一致 | ✅ | Numeric natbib throughout |\n| 数学符号一致 | ✅ | τ_d, λ, d_max 使用一致（minor 例外见 Minor-5）|\n| Booktabs 表格 | ✅ | 全部表格使用 \\toprule/\\midrule/\\bottomrule |\n| Submission footer | ✅ | \"Submitted to the 10th Conference on Robot Learning (CoRL, 2026)\" |",
    "reviewer_id": "3",
    "project": "diff_collision_sdf"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-28T05:06:56.237477+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3863
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-28T05:07:00.815620+00:00_

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
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
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

_source line 91 · 2026-05-28T05:07:00.866150+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-28T05:07:05.038798+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/review_round_1/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-28T05:07:05.139602+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---

### Assistant

_source line 94 · 2026-05-28T05:07:19.090686+00:00_

Reviewer 3 审稿完成。报告已提交至 Review Director，核心发现：

**Must-Fix（2 项）**：
1. Limitations 未声明"全部实验仅在仿真环境完成"——CoRL 强调 real-robot relevance，这是关键遗漏
2. Broader Impact 仅一句话，对于声称"安全评估根本性失效"的论文严重不足

**Should-Fix（4 项）**：标题 98% 数字来自 broken 配置有夸大倾向；"frozen"/"action-collapsed"/"fake safe" 三套术语混用；Abstract 第 5 句信息过载；Figure 1 teaser 未在首页

**格式合规**：模板、页数、匿名、引用格式、Figure/Table 编号均通过检查。

**写作质量**：整体 3/4 (Good)，无 AI 写作痕迹，叙事弧线清晰，Appendix 详尽。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3"
}
```

</details>

---

## Round 2

4 recorded events

### User

_source line 95 · 2026-05-28T05:08:21.859852+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 和 Reviewer 2 的审稿意见

请仔细阅读以下两位 Reviewer 的完整审稿意见，对每个 Must-Fix 和 Should-Fix 条目逐条回应：
- **[AGREE]**：同意该观点，并简要说明理由
- **[REBUT]**：反驳该观点，提供具体证据（引用论文中的 Section/Table/Figure）

---

## Reviewer 1 审稿报告（方法严谨性 + 实验设计 + 统计方法论）

**Overall**: 5/10（Borderline Reject）

### Must-Fix:

**N1** [critical] Permutation test 的 null distribution 构建存在循环论证
- 将 λ=0.005 纳入 null 是 post-hoc、data-dependent 决策。C(9,3)=84 粒度太粗。

**N2** [critical] 将 "fail to reject H0" 解读为 "SDF 无效" 是统计推断错误
- n=3 功效极低。Appendix J 显示 λ=0.1 在所有评估种子上一致高于 LoRA-only。暗示可能存在被漏检的小效应。论文需 TOST equivalence testing 或 reframe claim。

**N3** [critical] 实验范围过窄——4 tasks, 1 benchmark, 1 model family

### Should-Fix:

**W1** [warning] Oracle 实验在非功能性策略上进行（TSR≈0%），生态效度存疑

**W2** [warning] dfCAR 位移测量不一致（Pi0 obstacle displacement vs Pi0.5 EE displacement）

**W3** [warning] n=3 seeds 对 null claim 支撑力不足

**W4** [warning] spatial_bowl 交叉验证仅 1 seed, 无统计意义

**W5** [warning] SDF λ 搜索仅 3 个点

---

## Reviewer 2 审稿报告（新颖性 + 相关工作 + 贡献定位）

**Overall**: 5/10（Borderline lean reject）

### Must-Fix:

**N1** [critical] 实验范围过窄，无法支撑论文的强断言

**N2** [critical] 与 SafeVLA / VLSA 正向结果的矛盾未充分解释
- SafeVLA 用 CMDP + constrained RL，VLSA 用 control barrier functions，本文仅测试 auxiliary SDF loss。论文叙事暗示 SDF 方法普遍无效但实际仅否定了一种集成方式。

**N3** [critical] Claim 1 部分显而易见——action collapse 导致虚假 CAR 在概念上直觉

### Should-Fix:

**W1** [warning] 相关工作遗漏多个 2025-2026 重要文献（HazardArena, VLA-Risk, D2PPO 等）

**W2** [warning] dfCAR 方法论贡献有限——简单阈值过滤器，未与替代 filter 对比

**W3** [warning] 标题过于耸动

**W4** [warning] 建设性贡献不足——缺 proof-of-concept 解决方案

**W5** [warning] Claim 2 和 Claim 3 区分度不足

---

请逐条回应，格式为：

**对 R1-N1**: [AGREE/REBUT] 理由...
**对 R1-N2**: [AGREE/REBUT] 理由...
（依此类推）

**注意**：你的审查侧重是写作质量/格式/伦理，对方法和新颖性的评价请基于你在审稿过程中观察到的写作呈现层面的证据来回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "source": "review_reviewer_3"
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-28T05:10:53.333715+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 3 交叉回应 — 对 R1 和 R2 逐条回应\n\n---\n\n### 对 Reviewer 1（方法严谨性 + 实验设计 + 统计方法论）\n\n---\n\n**对 R1-N1** [AGREE] Permutation test null distribution 构建的写作透明度不足\n\n同意核心观点。从写作角度看，将 λ=0.005 纳入 null 的理由仅出现在 Appendix G（appendix.tex lines 173-176）：\"We treat these as exchangeable because SDF at λ = 0.005 produces no separation from LoRA-only\"——这是一个 post-hoc、data-dependent 的方法论选择，但论文将其埋在 appendix 中，主文 Section 6 未标注此决策的争议性。一个影响核心 claim 统计显著性的分析选择，应当在主文中明确声明并讨论替代方案（如仅用 LoRA-only 3 seeds 构建 null）。C(9,3)=84 的粒度问题也应在写作中承认为统计检验的局限。\n\n---\n\n**对 R1-N2** [AGREE] \"SDF 无效\" 的表述超越了统计证据的支撑范围\n\n这是我观察到的最显著的写作-证据不匹配。论文内部存在表述梯度的不一致：\n- Section 6 主文用了审慎措辞：\"SDF supervision adds **no measurable benefit**\"（claim3.tex line 3）——这是正确的统计语言\n- 但 abstract line 5：\"SDF supervision **fails to deliver** collision avoidance\"——更强\n- Section 7：\"the **failure is architectural**\"——最强，已是因果断言\n- 标题：\"98% of Collision Avoidance **is an Illusion**\"——暗示确定性结论\n\n更关键的是，Appendix J（appendix.tex lines 249-306, Table 13）的数据实际上对 R1 的观点构成强支撑：SDF λ=0.1 在所有 3 个评估种子上一致高于 LoRA-only（seed=7: 58.0 vs 56.5, seed=42: 59.0 vs 56.5, seed=123: 58.5 vs 53.0）。论文自身在 Appendix J 中报告了这一 pattern 但未在主文中讨论其含义。在 n=3 seeds 功效极低的前提下，将 p=0.131 解读为\"完全冗余\"而非\"未检测到的小效应\"，是从写作层面看最需要修正的 framing 问题。\n\n建议：主文 Section 6 应增加一段讨论 statistical power 限制和 effect size 的方向性趋势，将核心 claim 从\"SDF is redundant\"重新框定为\"SDF shows no statistically significant benefit at the tested sample size, though a consistent directional trend warrants investigation at larger scale\"。\n\n---\n\n**对 R1-N3** [AGREE] 与我的 N1 发现一致\n\n完全同意。这与我的 Must-Fix N1 直接对应——Limitations 段未明确声明实验范围的根本局限（仅 SafeLIBERO 仿真、4 tasks、2 model families）。论文在 Limitations 段（Section 7, discussion.tex line 12）提到了\"one benchmark suite (SafeLIBERO, four tasks) and two model families\"，但措辞过于轻描淡写，未充分讨论这一范围限制对核心 claims 普适性的影响。结合 CoRL 对 real-robot relevance 的要求，这是格式合规层面的关键缺失。\n\n---\n\n**对 R1-W1** [AGREE] Oracle 实验的生态效度问题在写作中未充分 flag\n\nOracle 实验基于 Pi0+A1（TSR≈0%），该配置因 parameter-name mismatch 导致 LoRA 未加载（method.tex line 44, Table 1 footnote）。论文在 Section 5 和 Appendix F 中报告了实验结果，但未在 Section 5 正文中明确讨论\"在一个几乎不产生动作的策略上测试碰撞避免的有效性\"这一 ecological validity 问题。Limitations 段虽提到\"Oracle experiments used a largely frozen model (Pi0+A1, TSR≈0%); testing on an actively moving policy would better isolate the structural limitation\"（discussion.tex line 12），但这一关键 caveat 应在 Section 5 正文中更突出，而非仅在 Limitations 一笔带过。\n\n---\n\n**对 R1-W2** [AGREE] 位移测量不一致的披露不够显著\n\n论文在 claim1.tex line 3 用脚注说明：\"Pi0-family values report obstacle displacement from the original protocol; Pi0.5 reports EE displacement from the rotation-corrected protocol (§3.2). Sub-millimeter displacement indicates action collapse in both cases.\" 从写作角度看，这是一个影响 dfCAR metric 内部一致性的核心方法论问题，仅用脚注处理是不够的。dfCAR 作为论文第一贡献，其测量基础的不一致应在 Section 3.2 正文中明确讨论并论证等价性（例如，两种位移度量在判断 action collapse 时为何可互换）。\n\n---\n\n**对 R1-W3** [AGREE] n=3 的局限在写作中处理不足\n\n与 R1-N2 一致。论文在 Section 6 Table 4 报告 3-seed 结果，但未在主文中讨论样本量的 power 限制。Appendix H（stepwise analysis）的 seed-0 checkpoint-to-checkpoint 波动达 8 pp（appendix.tex line 208），论文正确指出这与 binomial sampling noise 一致，但未将此观察上升到对主要 claim 统计信心的限定。\n\n---\n\n**对 R1-W4** [AGREE] spatial_bowl 跨场景验证的统计局限已披露但 claim 过强\n\n论文在 Appendix I（appendix.tex line 228）明确声明\"statistical power is limited\"，这是好的写作实践。但同段最后一句\"reinforcing the conclusion that EE-only SDF auxiliary supervision does not produce a meaningful collision avoidance benefit beyond LoRA-only fine-tuning\"——从 1 seed、200 episodes 的结果上升到\"reinforcing the conclusion\"措辞过强。建议改为\"consistent with the hypothesis\"。\n\n---\n\n**对 R1-W5** [REBUT] λ 搜索范围的表述基本准确，但\"full tested range\"措辞可商榷\n\n论文在 Section 6 (claim3.tex line 3) 使用\"across the full tested range λ ∈ [0.005, 0.1]\"——这是事实性陈述，指\"我们测试过的全部范围\"，并非声称覆盖了所有可能的 λ 值。但\"20× range\"的重复强调（出现 5+ 次：abstract, introduction, Section 6, Section 7, claim3.tex lines 32）在有限的 3 个数据点支撑下有 overselling 之嫌。不过，λ = 0.1 已经是 SDF loss 占 total loss 约 10% 的较大权重，继续增大可能干扰 action loss 的训练。论文对此范围选择的合理性在 Section 6 最后一段（claim3.tex lines 31-32）有简要论证。因此这不是一个纯写作问题，而是方法论判断——我保留给 R1 评估。\n\n---\n\n### 对 Reviewer 2（新颖性 + 相关工作 + 贡献定位）\n\n---\n\n**对 R2-N1** [AGREE] 与 R1-N3 和我的 N1 一致\n\n三位 Reviewer 在这一点上形成共识：实验范围（4 tasks, 1 benchmark, 2 model families, simulation only）无法支撑论文标题和 abstract 的普适性断言。从写作角度，这需要：(1) 在 Limitations 中明确声明，(2) 在标题/abstract 中限定 scope，(3) 在 Discussion 中更审慎地讨论 generalizability。\n\n---\n\n**对 R2-N2** [AGREE] 与 SafeVLA/VLSA 差异的写作定位不充分\n\n这是一个重要的写作/定位问题。论文在 Related Work（related_work.tex lines 6-7）提到 SafeVLA 使用 constrained RL、VLSA 使用 control barrier functions，但在实验和讨论中未解释为什么这些方法的正向结果不与本文发现矛盾。论文仅测试了\"auxiliary SDF loss as a training signal\"这一特定集成方式，但标题和 abstract 的叙事框架（\"98% of Collision Avoidance is an Illusion\"）暗示问题远比此宽泛。\n\nSection 7 Discussion（discussion.tex lines 5-6）确实提供了 architectural 层面的解释（\"EE monitoring cannot prevent full-body collisions\"），这对 auxiliary SDF loss 是一个清晰的机理论证。但论文未讨论：SafeVLA 的 CMDP 方法是否绕过了 EE-only 局限？VLSA 的 control barrier function 是否在 runtime 层面解决了此问题？如果这些方法有效恰恰是因为它们不依赖 EE-only SDF，那论文应当在 Related Work 或 Discussion 中明确这一区分，而非让读者自行推断。\n\n---\n\n**对 R2-N3** [REBUT] Claim 1 的贡献不在概念新颖性，而在系统性实证文档化\n\nR2 认为\"action collapse → inflated CAR\"在概念上直觉。从概念层面确实如此——一个不动的机器人当然不会碰撞。但论文的贡献在于：\n\n1. **实证规模**：100+ experiments, 6000+ episodes 的系统性文档化，Table 2 量化了 Pi0 全系列 99.4-99.6% 的 fake safe rate——这不是\"可能存在\"而是\"几乎全部\"\n2. **bimodal distribution 发现**：Appendix A Figure 5 显示位移分布存在 5-order-of-magnitude gap（<1μm vs >200mm），这使得 dfCAR 的 threshold 选择在 [2, 200]mm 范围内完全 robust（Appendix B Table 6）——这不是直觉能预测的\n3. **dfCAR metric**：一个具体的、有方程式定义（Eq. 1）、经过 8 个 model-seed 组合验证的诊断工具\n\n不过，R2 的批评在写作层面有一个合理的核心：论文的 framing 将 Claim 1 呈现为一个\"发现\"（\"The problem appears close to solved. It is not.\"——introduction.tex lines 3-4），而非\"已知可能性的首次大规模实证确认\"。后者的 framing 更准确且不减损贡献。\n\n---\n\n**对 R2-W1** [AGREE] 相关工作可能存在遗漏\n\n我无法独立验证 HazardArena、VLA-Risk、D2PPO 是否为已发表文献（超出我的信息范围）。但从写作完整性角度：论文的 Related Work 共 4 段约 27 引用，对于一篇声称重新审视 VLA 安全评估的论文，应当尽可能覆盖 2025-2026 的最新安全评估/安全训练文献。如果这些工作确实存在且相关，遗漏它们会削弱论文的 positioning。\n\n---\n\n**对 R2-W2** [REBUT] dfCAR 的价值在于诊断有效性而非方法复杂度\n\nR2 批评 dfCAR 是\"简单阈值过滤器\"。从写作角度看，论文对 dfCAR 的定位是恰当的——它被呈现为一个 diagnostic correction（Section 3.2, Eq. 1），而非一个 novel algorithmic contribution。论文的核心论证是：由于位移分布的 bimodal 特性（Appendix A），任何 τ_d ∈ [2, 200]mm 的阈值都给出相同结果（Appendix B Table 6），因此简单阈值已经足够，不需要更复杂的 filter。\n\n但 R2 关于\"未与替代 filter 对比\"的观点有合理之处：论文可以简要讨论为什么不使用 velocity-based filter 或 trajectory-complexity filter 作为替代方案，这会增强 dfCAR 选择的说服力。\n\n---\n\n**对 R2-W3** [AGREE] 与我的 W1 完全一致\n\n三位 Reviewer 在标题问题上形成共识。\"When 98% of Collision Avoidance is an Illusion\"中的 98% 来自 Pi0+A1 这一因参数错误而 broken 的配置（method.tex line 44），不代表 VLA 安全评估的普遍状况。标题需要更精确的 scope 限定。\n\n---\n\n**对 R2-W4** [AGREE] 建设性贡献在写作中确实单薄\n\nSection 7 \"Future work\"（discussion.tex lines 14-15）仅用三个半句列出方向：(1) full-body SDF supervision along the kinematic chain, (2) cross-architecture evaluation on OpenVLA, RT-2, (3) planning-layer safety constraints in joint space。每个方向一句话，无具体方案。对于一篇主要是\"拆解\"现有方法的论文，Discussion 中更具体的建设性展望（哪怕是 preliminary formulation）会显著提升论文的平衡感。\n\n不过，我不认为缺少 proof-of-concept 实现是 must-fix——诊断性论文（如 benchmark 分析、evaluation critique）在 ML 社区有其独立价值。但写作上应更明确地将论文定位为\"diagnostic contribution\"而非暗示已给出解决方案。\n\n---\n\n**对 R2-W5** [REBUT] Claim 2 和 Claim 3 在逻辑上是独立的，写作区分充分\n\nClaim 2（Section 5）论证的是 **architectural failure**：EE-only SDF 在 oracle（ground-truth）条件下仍然降低 CAR（Table 3），因为 SDF gradient 作用于单点但碰撞发生在 intermediate links。证据来自 oracle 实验（160 episodes, Table 10 per-task breakdown）。\n\nClaim 3（Section 6）论证的是 **signal redundancy**：即使架构问题被忽略，collision-free demonstrations 已经包含了全部避障信号，SDF training signal 在统计上无贡献。证据来自 LoRA-only vs LoRA+SDF 对比（Table 4, 600+ episodes）。\n\nSection 7 第一段（discussion.tex lines 5-6）明确将两者框定为\"two independent causes\"：\"(i) Demonstration data subsumes the SDF signal\" 和 \"(ii) EE monitoring cannot prevent full-body collisions\"。\n\n这两个 claim 回答不同的问题：Claim 2 = \"如果信号完美，EE-only 架构能否工作？\"（答：不能）。Claim 3 = \"SDF training signal 是否提供了 demonstrations 之外的信息？\"（答：在测试范围内，没有）。写作层面的区分是清晰的。",
  "reviewer_id": "3",
  "project": "diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 3 交叉回应 — 对 R1 和 R2 逐条回应\n\n---\n\n### 对 Reviewer 1（方法严谨性 + 实验设计 + 统计方法论）\n\n---\n\n**对 R1-N1** [AGREE] Permutation test null distribution 构建的写作透明度不足\n\n同意核心观点。从写作角度看，将 λ=0.005 纳入 null 的理由仅出现在 Appendix G（appendix.tex lines 173-176）：\"We treat these as exchangeable because SDF at λ = 0.005 produces no separation from LoRA-only\"——这是一个 post-hoc、data-dependent 的方法论选择，但论文将其埋在 appendix 中，主文 Section 6 未标注此决策的争议性。一个影响核心 claim 统计显著性的分析选择，应当在主文中明确声明并讨论替代方案（如仅用 LoRA-only 3 seeds 构建 null）。C(9,3)=84 的粒度问题也应在写作中承认为统计检验的局限。\n\n---\n\n**对 R1-N2** [AGREE] \"SDF 无效\" 的表述超越了统计证据的支撑范围\n\n这是我观察到的最显著的写作-证据不匹配。论文内部存在表述梯度的不一致：\n- Section 6 主文用了审慎措辞：\"SDF supervision adds **no measurable benefit**\"（claim3.tex line 3）——这是正确的统计语言\n- 但 abstract line 5：\"SDF supervision **fails to deliver** collision avoidance\"——更强\n- Section 7：\"the **failure is architectural**\"——最强，已是因果断言\n- 标题：\"98% of Collision Avoidance **is an Illusion**\"——暗示确定性结论\n\n更关键的是，Appendix J（appendix.tex lines 249-306, Table 13）的数据实际上对 R1 的观点构成强支撑：SDF λ=0.1 在所有 3 个评估种子上一致高于 LoRA-only（seed=7: 58.0 vs 56.5, seed=42: 59.0 vs 56.5, seed=123: 58.5 vs 53.0）。论文自身在 Appendix J 中报告了这一 pattern 但未在主文中讨论其含义。在 n=3 seeds 功效极低的前提下，将 p=0.131 解读为\"完全冗余\"而非\"未检测到的小效应\"，是从写作层面看最需要修正的 framing 问题。\n\n建议：主文 Section 6 应增加一段讨论 statistical power 限制和 effect size 的方向性趋势，将核心 claim 从\"SDF is redundant\"重新框定为\"SDF shows no statistically significant benefit at the tested sample size, though a consistent directional trend warrants investigation at larger scale\"。\n\n---\n\n**对 R1-N3** [AGREE] 与我的 N1 发现一致\n\n完全同意。这与我的 Must-Fix N1 直接对应——Limitations 段未明确声明实验范围的根本局限（仅 SafeLIBERO 仿真、4 tasks、2 model families）。论文在 Limitations 段（Section 7, discussion.tex line 12）提到了\"one benchmark suite (SafeLIBERO, four tasks) and two model families\"，但措辞过于轻描淡写，未充分讨论这一范围限制对核心 claims 普适性的影响。结合 CoRL 对 real-robot relevance 的要求，这是格式合规层面的关键缺失。\n\n---\n\n**对 R1-W1** [AGREE] Oracle 实验的生态效度问题在写作中未充分 flag\n\nOracle 实验基于 Pi0+A1（TSR≈0%），该配置因 parameter-name mismatch 导致 LoRA 未加载（method.tex line 44, Table 1 footnote）。论文在 Section 5 和 Appendix F 中报告了实验结果，但未在 Section 5 正文中明确讨论\"在一个几乎不产生动作的策略上测试碰撞避免的有效性\"这一 ecological validity 问题。Limitations 段虽提到\"Oracle experiments used a largely frozen model (Pi0+A1, TSR≈0%); testing on an actively moving policy would better isolate the structural limitation\"（discussion.tex line 12），但这一关键 caveat 应在 Section 5 正文中更突出，而非仅在 Limitations 一笔带过。\n\n---\n\n**对 R1-W2** [AGREE] 位移测量不一致的披露不够显著\n\n论文在 claim1.tex line 3 用脚注说明：\"Pi0-family values report obstacle displacement from the original protocol; Pi0.5 reports EE displacement from the rotation-corrected protocol (§3.2). Sub-millimeter displacement indicates action collapse in both cases.\" 从写作角度看，这是一个影响 dfCAR metric 内部一致性的核心方法论问题，仅用脚注处理是不够的。dfCAR 作为论文第一贡献，其测量基础的不一致应在 Section 3.2 正文中明确讨论并论证等价性（例如，两种位移度量在判断 action collapse 时为何可互换）。\n\n---\n\n**对 R1-W3** [AGREE] n=3 的局限在写作中处理不足\n\n与 R1-N2 一致。论文在 Section 6 Table 4 报告 3-seed 结果，但未在主文中讨论样本量的 power 限制。Appendix H（stepwise analysis）的 seed-0 checkpoint-to-checkpoint 波动达 8 pp（appendix.tex line 208），论文正确指出这与 binomial sampling noise 一致，但未将此观察上升到对主要 claim 统计信心的限定。\n\n---\n\n**对 R1-W4** [AGREE] spatial_bowl 跨场景验证的统计局限已披露但 claim 过强\n\n论文在 Appendix I（appendix.tex line 228）明确声明\"statistical power is limited\"，这是好的写作实践。但同段最后一句\"reinforcing the conclusion that EE-only SDF auxiliary supervision does not produce a meaningful collision avoidance benefit beyond LoRA-only fine-tuning\"——从 1 seed、200 episodes 的结果上升到\"reinforcing the conclusion\"措辞过强。建议改为\"consistent with the hypothesis\"。\n\n---\n\n**对 R1-W5** [REBUT] λ 搜索范围的表述基本准确，但\"full tested range\"措辞可商榷\n\n论文在 Section 6 (claim3.tex line 3) 使用\"across the full tested range λ ∈ [0.005, 0.1]\"——这是事实性陈述，指\"我们测试过的全部范围\"，并非声称覆盖了所有可能的 λ 值。但\"20× range\"的重复强调（出现 5+ 次：abstract, introduction, Section 6, Section 7, claim3.tex lines 32）在有限的 3 个数据点支撑下有 overselling 之嫌。不过，λ = 0.1 已经是 SDF loss 占 total loss 约 10% 的较大权重，继续增大可能干扰 action loss 的训练。论文对此范围选择的合理性在 Section 6 最后一段（claim3.tex lines 31-32）有简要论证。因此这不是一个纯写作问题，而是方法论判断——我保留给 R1 评估。\n\n---\n\n### 对 Reviewer 2（新颖性 + 相关工作 + 贡献定位）\n\n---\n\n**对 R2-N1** [AGREE] 与 R1-N3 和我的 N1 一致\n\n三位 Reviewer 在这一点上形成共识：实验范围（4 tasks, 1 benchmark, 2 model families, simulation only）无法支撑论文标题和 abstract 的普适性断言。从写作角度，这需要：(1) 在 Limitations 中明确声明，(2) 在标题/abstract 中限定 scope，(3) 在 Discussion 中更审慎地讨论 generalizability。\n\n---\n\n**对 R2-N2** [AGREE] 与 SafeVLA/VLSA 差异的写作定位不充分\n\n这是一个重要的写作/定位问题。论文在 Related Work（related_work.tex lines 6-7）提到 SafeVLA 使用 constrained RL、VLSA 使用 control barrier functions，但在实验和讨论中未解释为什么这些方法的正向结果不与本文发现矛盾。论文仅测试了\"auxiliary SDF loss as a training signal\"这一特定集成方式，但标题和 abstract 的叙事框架（\"98% of Collision Avoidance is an Illusion\"）暗示问题远比此宽泛。\n\nSection 7 Discussion（discussion.tex lines 5-6）确实提供了 architectural 层面的解释（\"EE monitoring cannot prevent full-body collisions\"），这对 auxiliary SDF loss 是一个清晰的机理论证。但论文未讨论：SafeVLA 的 CMDP 方法是否绕过了 EE-only 局限？VLSA 的 control barrier function 是否在 runtime 层面解决了此问题？如果这些方法有效恰恰是因为它们不依赖 EE-only SDF，那论文应当在 Related Work 或 Discussion 中明确这一区分，而非让读者自行推断。\n\n---\n\n**对 R2-N3** [REBUT] Claim 1 的贡献不在概念新颖性，而在系统性实证文档化\n\nR2 认为\"action collapse → inflated CAR\"在概念上直觉。从概念层面确实如此——一个不动的机器人当然不会碰撞。但论文的贡献在于：\n\n1. **实证规模**：100+ experiments, 6000+ episodes 的系统性文档化，Table 2 量化了 Pi0 全系列 99.4-99.6% 的 fake safe rate——这不是\"可能存在\"而是\"几乎全部\"\n2. **bimodal distribution 发现**：Appendix A Figure 5 显示位移分布存在 5-order-of-magnitude gap（<1μm vs >200mm），这使得 dfCAR 的 threshold 选择在 [2, 200]mm 范围内完全 robust（Appendix B Table 6）——这不是直觉能预测的\n3. **dfCAR metric**：一个具体的、有方程式定义（Eq. 1）、经过 8 个 model-seed 组合验证的诊断工具\n\n不过，R2 的批评在写作层面有一个合理的核心：论文的 framing 将 Claim 1 呈现为一个\"发现\"（\"The problem appears close to solved. It is not.\"——introduction.tex lines 3-4），而非\"已知可能性的首次大规模实证确认\"。后者的 framing 更准确且不减损贡献。\n\n---\n\n**对 R2-W1** [AGREE] 相关工作可能存在遗漏\n\n我无法独立验证 HazardArena、VLA-Risk、D2PPO 是否为已发表文献（超出我的信息范围）。但从写作完整性角度：论文的 Related Work 共 4 段约 27 引用，对于一篇声称重新审视 VLA 安全评估的论文，应当尽可能覆盖 2025-2026 的最新安全评估/安全训练文献。如果这些工作确实存在且相关，遗漏它们会削弱论文的 positioning。\n\n---\n\n**对 R2-W2** [REBUT] dfCAR 的价值在于诊断有效性而非方法复杂度\n\nR2 批评 dfCAR 是\"简单阈值过滤器\"。从写作角度看，论文对 dfCAR 的定位是恰当的——它被呈现为一个 diagnostic correction（Section 3.2, Eq. 1），而非一个 novel algorithmic contribution。论文的核心论证是：由于位移分布的 bimodal 特性（Appendix A），任何 τ_d ∈ [2, 200]mm 的阈值都给出相同结果（Appendix B Table 6），因此简单阈值已经足够，不需要更复杂的 filter。\n\n但 R2 关于\"未与替代 filter 对比\"的观点有合理之处：论文可以简要讨论为什么不使用 velocity-based filter 或 trajectory-complexity filter 作为替代方案，这会增强 dfCAR 选择的说服力。\n\n---\n\n**对 R2-W3** [AGREE] 与我的 W1 完全一致\n\n三位 Reviewer 在标题问题上形成共识。\"When 98% of Collision Avoidance is an Illusion\"中的 98% 来自 Pi0+A1 这一因参数错误而 broken 的配置（method.tex line 44），不代表 VLA 安全评估的普遍状况。标题需要更精确的 scope 限定。\n\n---\n\n**对 R2-W4** [AGREE] 建设性贡献在写作中确实单薄\n\nSection 7 \"Future work\"（discussion.tex lines 14-15）仅用三个半句列出方向：(1) full-body SDF supervision along the kinematic chain, (2) cross-architecture evaluation on OpenVLA, RT-2, (3) planning-layer safety constraints in joint space。每个方向一句话，无具体方案。对于一篇主要是\"拆解\"现有方法的论文，Discussion 中更具体的建设性展望（哪怕是 preliminary formulation）会显著提升论文的平衡感。\n\n不过，我不认为缺少 proof-of-concept 实现是 must-fix——诊断性论文（如 benchmark 分析、evaluation critique）在 ML 社区有其独立价值。但写作上应更明确地将论文定位为\"diagnostic contribution\"而非暗示已给出解决方案。\n\n---\n\n**对 R2-W5** [REBUT] Claim 2 和 Claim 3 在逻辑上是独立的，写作区分充分\n\nClaim 2（Section 5）论证的是 **architectural failure**：EE-only SDF 在 oracle（ground-truth）条件下仍然降低 CAR（Table 3），因为 SDF gradient 作用于单点但碰撞发生在 intermediate links。证据来自 oracle 实验（160 episodes, Table 10 per-task breakdown）。\n\nClaim 3（Section 6）论证的是 **signal redundancy**：即使架构问题被忽略，collision-free demonstrations 已经包含了全部避障信号，SDF training signal 在统计上无贡献。证据来自 LoRA-only vs LoRA+SDF 对比（Table 4, 600+ episodes）。\n\nSection 7 第一段（discussion.tex lines 5-6）明确将两者框定为\"two independent causes\"：\"(i) Demonstration data subsumes the SDF signal\" 和 \"(ii) EE monitoring cannot prevent full-body collisions\"。\n\n这两个 claim 回答不同的问题：Claim 2 = \"如果信号完美，EE-only 架构能否工作？\"（答：不能）。Claim 3 = \"SDF training signal 是否提供了 demonstrations 之外的信息？\"（答：在测试范围内，没有）。写作层面的区分是清晰的。",
    "reviewer_id": "3",
    "project": "diff_collision_sdf"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-28T05:10:57.253624+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3919
}
```

</details>

---

### Assistant

_source line 98 · 2026-05-28T05:11:04.665933+00:00_

交叉回应已提交给 Review Director。

总结：对 R1 的 8 条意见，我 AGREE 7 条、REBUT 1 条（W5 λ 范围表述）；对 R2 的 8 条意见，我 AGREE 5 条、REBUT 3 条（N3 Claim 1 贡献定位、W2 dfCAR 方法论、W5 Claim 2/3 区分度）。三位 Reviewer 在三个问题上形成共识：实验范围过窄（R1-N3/R2-N1/我的 N1）、标题夸大（R2-W3/我的 W1）、统计 claim 超越证据支撑（R1-N2/我从写作角度的观察）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ec359a7b7a5e3b28b379b61588c6e853:reviewer_3"
}
```

</details>

---
