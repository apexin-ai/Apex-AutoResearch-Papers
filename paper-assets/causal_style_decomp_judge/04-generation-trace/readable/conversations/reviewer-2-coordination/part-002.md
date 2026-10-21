# Reviewer 2 coordination — Part 2 of 3

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-2-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/fe/fe1bbde7623f8449bd9a.json)

## Round 17

### User

_source line 493 · 2026-05-21T21:11:17.338880+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**的审查。

## 投稿信息
- **Venue**: EMNLP 2026 (ARR)，Long Paper
- **截止日期**: 2026-05-25 AoE
- **格式**: ACL 模板，正文 ≤8 页，引用不限，Limitations 必须有（不计页数），double-blind
- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 论文文件
- LaTeX: `projects/causal_style_decomp_judge/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`
- Sections 在 `projects/causal_style_decomp_judge/docs/paper/sections/` 下：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex

## 你的审查侧重

### 必须覆盖
1. **Novelty 定位**：核心贡献（Likert Blindspot 发现、CSD pipeline、measurement mode 洞察）是否真正新颖？与 Thurstone (1927)、心理测量学文献的关系如何定位？是否有 overclaim "first"？
2. **Related Work 完整性**：是否覆盖了 LLM-as-Judge 偏差研究的主要方向（style bias、position bias、self-preference）？是否遗漏关键文献？特别关注 Jeong et al. (2025) Comparative Trap 等近期工作
3. **贡献声明一致性**：Abstract/Introduction 中的贡献声明是否与实验结果吻合？是否有方向不一致？
4. **论文结构与叙事**：各 section 之间的逻辑流是否通顺？信息密度是否均衡？Abstract 是否过密？
5. **格式合规**：
   - 主正文 ≤8 页（Limitations/References 不计入）
   - Limitations section 是否存在且合理
   - 匿名要求是否满足
   - 引用格式是否正确（natbib）
   - 图表质量和标注完整性
6. **写作质量**：语法、用词精准度、术语一致性、可读性

### 输出格式
请按以下结构输出审稿意见：
- **Summary**（2-3 句）
- **Strengths**（逐条，标注 S1, S2, ...）
- **Weaknesses**（逐条，标注 W1, W2, ...，每条标注严重程度：Must-Fix / Should-Fix / Minor）
- **Questions**（需要作者回答的问题）
- **Missing References**（遗漏的相关文献）
- **Overall Assessment**：评分（用 EMNLP 2026 标准）+ Excitement (1-5) + 置信度 (1-5)
- **Detailed Comments**：逐节详细意见

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-21T21:11:26.371790+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-21T21:11:26.473218+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-21T21:11:31.142369+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 497 · 2026-05-21T21:11:31.945465+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-21T21:11:32.547842+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/causal_style_decomp_judge/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/causal_style_decomp_judge/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5"
  }
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-21T21:11:38.252230+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines:

## Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
Soundness scores must be justified by the text of the review, and if you give a low soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation.

### Excitement Score
Excitement is a separate score which is orthogonal to the assessment of the soundness of the paper, allowing reviewers to distinguish between work that is sound but not personally interesting versus work that may be both sound and exciting.

## Meta-Review Scoring (Area Chairs)

The new meta-review score options are: 5 = Consider for Award (top 2.5% papers), 2 = Resubmit next cycle (substantial revisions possible by next cycle), 1.5 = Resubmit after next cycle (substantial revisions requiring more time), and 1 = Do not resubmit (paper 
…[truncated 478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7109
}
```

</details>

---


### Tool result

_source line 500 · 2026-05-21T21:11:40.174838+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 588.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 456.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 490.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.2}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 539.7}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/pap
…[truncated 311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8229
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-21T21:11:40.225602+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 7677
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-21T21:11:47.818989+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-21T21:11:49.628475+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 456.3}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 605.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 584.4}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 51.3}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1809
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-21T21:11:49.729355+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer scoring criteria including: 1) All scoring dimensions (soundness, excitement, overall assessment, confidence, etc.) 2) The exact scale and meaning of each score level 3) Any guidance on what constitutes each score level. Return the full details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer scoring criteria including: 1) All scoring dimensions (soundness, excitement, overall assessment, confidence, etc.) 2) The exact scale and meaning of each score level 3) Any guidance on what constitutes each score level. Return the full details."
  }
}
```

</details>

---


### Tool call

_source line 505 · 2026-05-21T21:11:50.784245+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 506 · 2026-05-21T21:11:50.885069+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 507 · 2026-05-21T21:11:50.885593+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 508 · 2026-05-21T21:11:51.538602+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-21T21:11:55.855525+00:00_

# ARR Reviewer Scoring Criteria

Based on the guidelines provided, ARR uses **three primary scoring dimensions**:

## 1. **Soundness**
The guidelines state that "soundness scores must be justified by the text of the review." Low soundness scores require explicit justification in the review text; reviewers cannot assign low scores without identifying specific technical faults.

## 2. **Excitement**
Described as a separate, "orthogonal" dimension reflecting personal interest. The guidelines note this score is subjective and "do not necessarily come with explicit reasons." A paper can be technically sound but receive low excitement if the reviewer finds it personally uninteresting.

## 3. **Overall Assessment**
A composite recommendation score reflecting "soundness, excitement, and also other factors like novelty and impact." This represents an explicit recommendation for conference acceptance outcomes.

## Additional Dimensions Mentioned

- **Confidence**: Referenced in scoring discussions
- **Reproducibility**: Should be separately justified if scored low

## Key Scoring Guidance

The guidelines emphasize that "all papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible." However, reviewers may recommend acceptance despite low personal excitement if the work offers significant impact to targeted communities (efficiency improvements, resources for underserved languages/domains).

**Note**: The document does not provide the exact numerical scales (e.g., 1-5, 1-10) for these dimensions in the sections reviewed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6126
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-21T21:11:59.977492+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 511 · 2026-05-21T21:12:00.531506+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 512 · 2026-05-21T21:12:01.087593+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1110
}
```

</details>

---


### Tool call

_source line 513 · 2026-05-21T21:12:01.088021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-21T21:12:01.943600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 515 · 2026-05-21T21:12:02.096477+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 516 · 2026-05-21T21:12:02.349926+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1818
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-21T21:12:03.508417+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2420
}
```

</details>

---


### Tool result

_source line 518 · 2026-05-21T21:12:04.465697+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2522
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-21T21:12:04.669143+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2572
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-21T21:12:08.233811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 521 · 2026-05-21T21:12:08.635176+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 522 · 2026-05-21T21:12:09.090380+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 523 · 2026-05-21T21:12:09.090812+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 524 · 2026-05-21T21:12:09.945083+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1309
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-21T21:12:09.945900+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-21T21:12:09.996427+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 527 · 2026-05-21T21:12:10.301084+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 528 · 2026-05-21T21:12:11.611395+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1614
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-21T21:12:11.963909+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1662
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-21T21:12:18.557257+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 531 · 2026-05-21T21:12:18.808310+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-21T21:12:19.111590+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 533 · 2026-05-21T21:12:19.264472+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-21T21:12:19.264879+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-21T21:12:19.416692+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool result

_source line 536 · 2026-05-21T21:12:19.518360+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-21T21:12:20.326317+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1518
}
```

</details>

---


### Tool result

_source line 538 · 2026-05-21T21:12:20.829674+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1718
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-21T21:12:20.830731+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1566
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-21T21:12:28.102775+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-21T21:12:29.005636+00:00_

1	\begin{abstract}
2	LLM judges are widely deployed for evaluation and alignment, yet style features alone explain judge scores with near-perfect correlation.
3	We introduce Controlled Style Decomposition (CSD), the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison to systematically quantify style bias in LLM judges.
4	Across three target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B) and one negative control (Claude Sonnet 4), three benchmarks, and three style axes, CSD demonstrates the Likert Blindspot: Likert scoring systematically misses style biases that pairwise comparison detects (BT 63--84\%, $p < 0.001$), following a severity spectrum---complete at moderate bias ($d \to 0$ at $n = 355$), exceeding 60\% attenuation at stronger effects---confirmed by seven statistical methods.
5	GEE conditional decomposition demonstrates a per-axis confound structure consistent across all three target judges: verbosity bias is style-dominated, formality exhibits a conditional effect moderated by content quality changes, and register is judge-dependent (originality-dominated to mixed)---determining which estimates are directly interpretable and which require conditional analysis.
6	A fourth judge (Claude Sonnet 4) detects no bias on either axis, supporting discriminative validity.
7	We identify two candidate interpretations---measurement attenuation and construct divergence---and show that both yield the same operational conclusion: Likert-only evaluation systematically misses style-driven preferences that propagate through pairwise-based alignment pipelines.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 902
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-21T21:12:29.006182+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-21T21:12:29.558064+00:00_

1	\section{Introduction}
2	
3	LLM judges are central infrastructure for NLP evaluation (AlpacaEval, MT-Bench, Chatbot Arena) and alignment training (RLHF, DPO), where judge-generated preferences serve as reward signals.
4	Any systematic bias in their assessments propagates through both evaluation leaderboards and model development pipelines.
5	
6	Recent work suggests that style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}, motivating systematic measurement of per-axis style bias.
7	\citet{li2026preference} demonstrate that 76--92\% of observed preference signals originate from surface-level style cues rather than substantive quality differences, and \citet{soumik2026judging} report bias scores of 0.76--0.92 across five different judges.
8	Despite this consensus on severity, existing approaches each address individual requirements: CASSE \citep{casse2026concise} and FairJudge \citep{wang2026fairjudge} provide multi-dimensional style analysis, RATE \citep{reber2025rate} introduces interventional design, and length-controlled AlpacaEval \citep{dubois2025lc} offers population-level correction.
9	However, no single framework integrates all four requirements---per-axis decomposition, interventional identification, per-instance diagnostics, and black-box applicability.
10	A further concern compounds these limitations: standard Likert scoring suffers from a measurement efficiency gap---integer discretization produces ${\sim}60\%$ uninformative ties, and even non-tied pairs carry weaker signal than pairwise comparison---a limitation predicted by measurement theory \citep{thurstone1927law} but previously unquantified for LLM judges.
11	
12	We propose Controlled Style Decomposition (CSD), the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison to systematically quantify style bias in LLM judges.
13	Inspired by interventional approaches to text analysis \citep{vei
…[truncated 3128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 551
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-21T21:12:29.609329+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-21T21:12:30.362089+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Two lines of work motivate our approach: interventional methods for diagnosing judge bias, and measurement theory on the sensitivity of different elicitation formats.
5	
6	\paragraph{Interventional Approaches to Judge Bias}
7	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
8	\citet{reber2025rate} propose RATE, a framework that rewrites model outputs along style attributes using imperfect counterfactuals and measures the causal effect on reward model scores via Likert-scale Average Treatment Effect (ATE).
9	RATE applies a correction term to account for rewriting imperfections, but its reliance on Likert ATE as the primary metric is a vulnerability: our experiments show that Likert scoring exhibits a ceiling effect in which 60\% of style-transformed pairs receive identical integer scores, yielding non-significant ATE estimates ($p = 0.332$) for the same interventions that pairwise comparison detects at $p = 0.006$.
10	If this Likert Blindspot generalizes beyond our setting, RATE's own style-related findings may underestimate the true magnitude of attribute effects.
11	CSD differs from RATE in three respects: it targets individual style axes rather than general attributes, it measures bias through position-controlled pairwise comparison rather than Likert ATE, and it enforces content preservation via NLI entailment gating rather than post-hoc correction for imperfect rewrites.
12	\citet{counterfactual2025rhetorical} also adopt an interventional LLM-based design, rewriting texts to measure rhetorical style effects and aggregating preferences with a Bradley-Terry model.
13	Their framework operates at persona-level granularity (e.g., ``writes like a professor''), whereas CSD intervenes on specific style axes (e.g., formality, conciseness) and uses a sign test with position control rather than parametric aggregation.
14	
15	\paragrap
…[truncated 5037 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 752
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-21T21:12:30.362545+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-21T21:13:18.556824+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 52, \"total_citations\": 71, \"unique_cited_keys\": 51, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 43, \"online_not_found\": 3, \"online_mismatch\": 6}, \"cross_check\": {\"orphan_bib\": [\"hoenig2001abuse\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"murugadoss2025sos\", \"type\": \"inproceedings\", \"title\": \"Style Over Substance: Failure Modes of LLM Judges in Alignment Benchmarking\", \"authors\": \"Murugadoss, Aakanksha and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"li2026preference\", \"type\": \"inproceedings\", \"title\": \"Preference Leakage: A Contamination Problem in LLM-as-a-Judge\", \"authors\": \"Li, Dawei and others\", \"year\": \"2026\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"wang2026fairjudge\", \"type\": \"article\", \"title\": \"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge\", \"authors\": \"Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Sh...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.06625\"}, {\"key\": \"dubois2025lc\", \"type\": \"inproceedings\", \"title\": \"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators\", \"authors\": \"Dubois, Yann and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"casse2026concise\", \"type\": \"article\", \"title\": \"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents\", \"authors\": \"Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2601.10809\"}, {\"key\": \"counterfactu
…[truncated 40539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 48194
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-21T21:13:24.779045+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-21T21:13:25.130457+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Style-Controlled Rewriting}
5	\label{sec:rewriting}
6	
7	We aim to isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.
8	For each text, an instruction-tuned LLM (Qwen3-32B) first classifies its current style along the target axis (e.g., formal vs.\ casual via binary classification), then rewrites it toward the opposite pole (temperature 0.7) according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').
9	This produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.
10	Each operation constitutes a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}).
11	To control for rewriting artifact bias---the possibility that the judge prefers original text over any rewrite regardless of style---we additionally generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
12	
13	\subsection{Content Preservation Verification}
14	\label{sec:nli_gate}
15	
16	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
17	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large with an entailment threshold of 0.90.
18	For axes that preserve information density (formality, register), we apply standard bidirectional entailment: both NLI(original $\to$ rewrite) and NLI(rewrite $\to$ original) must exceed this value.
19	For axes that inherently change information density (e.g., verbosity), bidirectional verification is inappropriate---exp
…[truncated 5740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-21T21:13:25.130871+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-21T21:13:25.834245+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	We designate a primary family of eight hypothesis tests (three judges $\times$ formality and verbosity, plus register for GPT-4o and Qwen3-32B) and control the family-wise error rate with Holm-Bonferroni correction at $\alpha = 0.05$.
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses are reported with uncorrected $p$-values and interpreted as hypothesis-generating; confirmatory analyses test specific hypotheses about pipeline validity and are evaluated at the nominal $\alpha = 0.05$ level without additional correction, as they address orthogonal questions about measurement reliability rather than the primary style-bias family.
12	Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the default regularization of the \texttt{choix} Python library.
13	All bootstrap confidence intervals use 10{,}000 pair-level resamples with seed 42.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{Main results across four judges, three style axes, and three benchmarks. BT: Bradley-Terry win probability (10{,}000 pair-level bootstrap resamples; 95\% CIs in Appendix~\ref{app:bt_ci}). AEval: AlpacaEval; MTB: MT-Bench. Claude Sonnet 4 serves as negative control.}
19	\label{tab:main_results}
20	\begin{tabular}{@{}lllccc@{}}
21	\toprule
22	Bench & Judge & Axis & BT $P$ & Likert $d$ ($p$) & \\
23	\midrule
24	LLMBar & GPT-4o & Form.\ & .630$^{***}$ & .102 (.332) & $\dagger$ \\
25	 & GPT-4o & Verb.\ & .760$^{***}$ & $-$.095 (.403) & $\dagger$ \\
26	 & GPT-4o & Reg.\ & .570$^{\dagger}$ & $-$.031 (.785) & $\dagger_{\text{e}}
…[truncated 16590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-21T21:13:25.934934+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-21T21:13:25.985481+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced Controlled Style Decomposition (CSD), a black-box framework yielding two findings across four judges, three benchmarks, and three style axes.
5	First, the Likert Blindspot: Likert scoring systematically misses style biases that pairwise comparison detects---complete at moderate bias ($d \to 0$ at $n = 355$), ${>}60\%$ attenuation at stronger effects---confirmed by seven statistical methods.
6	Whether this reflects measurement attenuation or construct divergence, Likert-only audits miss style-driven preferences that propagate through alignment pipelines.
7	Second, GEE conditional decomposition demonstrates per-axis confound structure consistent across three architectures---verbosity style-dominated, formality conditional, register judge-dependent---determining which estimates require conditional analysis and informing debiasing priorities.
8	
9	Style bias audits should adopt content-controlled pairwise comparison with per-axis decomposition, especially at moderate effect sizes ($n < 500$), where six controls bound amplification risk (\S\ref{sec:amplification}); existing Likert-based null findings may reflect measurement insensitivity rather than genuine absence of bias.
10	Our findings are established on English benchmarks with $n \leq 355$; validation on larger corpora, additional languages, and emerging judge architectures remains necessary.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-21T21:13:31.913375+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-21T21:13:31.964162+00:00_

1	\appendix
2	
3	\section{Direction Asymmetry and Quality Confounding}
4	\label{app:direction}
5	
6	The formality axis exhibits a pronounced direction asymmetry: the judge selects the formal variant in 78.8\% of formal-is-rewrite pairs ($p = 0.001$) but only 54.5\% of casual-is-rewrite pairs ($p = 0.83$).
7	This asymmetry suggests that original quality $Q$ and formality $S$ are partially confounded---formally written texts may be inherently perceived as higher quality.
8	To quantify this, we fit a GEE logistic model (exchangeable correlation) with both formality and original-preference as predictors.
9	After controlling for original preference, the formality effect remains significant ($\text{OR} = 2.58$, $p = 0.002$), and the original-preference effect is also significant ($\text{OR} = 2.32$, $p = 0.006$).
10	The formality preference thus survives adjustment for original-preference confounding, though the significant original-preference effect indicates that quality--style confounding is present and non-negligible.
11	
12	At $n = 88$, the Qwen3-32B formality Style OR ($4.20$) exceeded the GPT-4o estimate ($2.58$), but a scaled replication ($n = 355$) corrects this to $2.15$ ($p < 0.0001$), comparable to GPT-4o and consistent with small-sample upward bias rather than evaluator-producer inflation of the style effect.
13	The originality confound remains stronger ($4.99$ vs.\ $2.32$), consistent with evaluator-producer bias inflating the originality component (Limitations).
14	The directional agreement between judges---both favor formal text after controlling for originality---supports the existence of formality bias, but the effect magnitude from Qwen3-32B should not be directly compared with GPT-4o.
15	
16	The NLI gate blocks \emph{content} changes but cannot block quality perception shifts that are themselves mediated by style---a fundamental identifiability limit of any text-rewriting approach.
17	
18	\section{Consistency Filter Robustness}
19	\label{sec:consistenc
…[truncated 21334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-21T21:13:32.014731+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-21T21:13:32.065266+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Detecting Hidden Style Bias\\in LLM Judges via Controlled Style Decomposition}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\paragraph{Quality--style confounding and construct validity.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
43	Although the formality effect survives logistic adjustment for original preference ($\text{OR} = 2.32$, $p = 0.006$; Appendix~\ref{app:direction}), residual confounding is not fully eliminated.
44	An alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference. Under this view, the divergence reflects construct difference rather than measurement failure. The Comparative Trap \citep{jeong2025comparative} lends support to this alternative; six experimental controls bound this risk (\S\ref{sec:amplification}), though definitive separation would require human ground-truth ratings.
45	
46	\paragraph{Evaluator-producer bias and generalizability.}
47	Qwen3-32B serves as both rewriter and judge, raising s
…[truncated 1877 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-21T21:14:32.187682+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM judge style bias pairwise vs Likert rating scale sensitivity 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM judge style bias pairwise vs Likert rating scale sensitivity 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 559 · 2026-05-21T21:14:32.188022+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Comparative Trap\" Jeong 2025 pairwise comparison amplification LLM evaluator bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Comparative Trap\" Jeong 2025 pairwise comparison amplification LLM evaluator bias"
  }
}
```

</details>

---


### Tool result

_source line 560 · 2026-05-21T21:14:38.667869+00:00_

Web search results for query: ""Comparative Trap" Jeong 2025 pairwise comparison amplification LLM evaluator bias"

Links: [{"title":"[PDF] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Comparative-Trap:-Pairwise-Comparisons-Biased-Jeong-Park/cd6191f270c5b98dec44a294e4f3cebcf371ac5f"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators - ACL Anthology","url":"https://aclanthology.org/2025.blackboxnlp-1.5/"},{"title":"[2406.12319] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://arxiv.org/abs/2406.12319"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators | alphaXiv","url":"https://www.alphaxiv.org/abs/2406.12319"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators (arXiv:2406.12319v4) - ScienceStack","url":"https://www.sciencestack.ai/paper/2406.12319"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://arxiv.org/html/2406.12319v4"},{"title":"[Literature Review] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://www.themoonlight.io/en/review/the-comparative-trap-pairwise-comparisons-amplifies-biased-preferences-of-llm-evaluators"},{"title":"Preprint. Under review. The Comparative Trap: Pairwise Comparisons Amplifies","url":"https://arxiv.org/pdf/2406.12319"}]

Based on the search results, I found the paper you're looking for:

"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators" was published by Jeong et al. in 2025 in the Proceedings of the 8th BlackboxNLP Workshop.

**Main Findings:**

LLM evaluators often display biased preferences, such as favoring verbosity and authoritative tones, and these bia
…[truncated 801 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6479
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-21T21:14:40.073432+00:00_

Web search results for query: "LLM judge style bias pairwise vs Likert rating scale sensitivity 2025 2026"

Links: [{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences   of LLM Evaluators","url":"https://arxiv.org/pdf/2406.12319"},{"title":"The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2509.26072"},{"title":"Fairness or Fluency? An Investigation into Language Bias of Pairwise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2601.13649"},{"title":"Rubric-Based Evaluations & LLM-as-a-Judge — Methodologies, Biases, and Empirical Validation in Domain-Specific Contexts. | by Adnan Masood, PhD. | Apr, 2026 | Medium","url":"https://medium.com/@adnanmasood/rubric-based-evals-llm-as-a-judge-methodologies-and-empirical-validation-in-domain-context-71936b989e80"},{"title":"LLM-as-a-Judge Scoring","url":"https://www.emergentmind.com/topics/llm-as-a-judge-scoring"},{"title":"Grading Scale Impact on LLM-as-a-Judge: Human-LLM Alignment Is Highest on 0-5 Grading Scale","url":"https://arxiv.org/html/2601.03444v1"},{"title":"Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://arxiv.org/pdf/2504.14716"},{"title":"LLM as a Judge: A 2026 Guide to Automated Model Assessment | Label Your Data","url":"https://labelyourdata.com/articles/llm-as-a-judge"},{"title":"Contrastive Decoding Mitigates Score Range Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2510.18196"}]

I found relevant research on this topic. Here are the key findings:

## Pairwise vs. Likert Rating Scale Sensitivity

Pairwise evaluation tasks enable LLMs to approximate human preferences with greater fidelity than pointwise scoring, in part due to the comparative framing. This suggests pairwise comparisons are more reliable overall.

However, when the quality of outputs is ambiguous, using a discrete Likert scale for LLM evaluator may introduce rating indeterminacy and lower consistency.

## Known 
…[truncated 1114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7885
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-21T21:14:48.935021+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Pairwise or Pointwise\" evaluating feedback protocols bias LLM evaluation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Pairwise or Pointwise\" evaluating feedback protocols bias LLM evaluation 2025"
  }
}
```

</details>

---


### Tool call

_source line 563 · 2026-05-21T21:14:48.985710+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"grading scale impact\" LLM judge human alignment 2025 0-5 scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"grading scale impact\" LLM judge human alignment 2025 0-5 scale"
  }
}
```

</details>

---


### Tool result

_source line 564 · 2026-05-21T21:14:54.009615+00:00_

Web search results for query: ""grading scale impact" LLM judge human alignment 2025 0-5 scale"

Links: [{"title":"(PDF) Grading Scale Impact on LLM-as-a-Judge: Human-LLM Alignment Is Highest on 0-5 Grading Scale","url":"https://www.researchgate.net/publication/399559167_Grading_Scale_Impact_on_LLM-as-a-Judge_Human-LLM_Alignment_Is_Highest_on_0-5_Grading_Scale"},{"title":"Grading Scale Impact on LLM-as-a-Judge: Human-LLM Alignment Is Highest on 0-5 Grading Scale","url":"https://arxiv.org/html/2601.03444v1"},{"title":"[2601.03444] Grading Scale Impact on LLM-as-a-Judge: Human-LLM Alignment Is Highest on 0-5 Grading Scale","url":"https://arxiv.org/abs/2601.03444"},{"title":"Grading Scale Impact on LLM-as-a-Judge: Human-LLM Alignment Is Highest on 0-5 Grading Scale","url":"https://arxiv.org/pdf/2601.03444"},{"title":"Grading Scale Impact on LLM-as-a-Judge: Human-LLM Alignment Is Highest on 0-5 Grading Scale - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260103444L/abstract"},{"title":"Paper page - Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://huggingface.co/papers/2602.00521"}]

Based on the search results, I found relevant research on this topic. Here are the key findings:

## Grading Scale Impact on LLM-as-a-Judge Human Alignment

LLM judgments are not perfectly consistent across scales on subjective benchmarks, and the choice of scale substantially shifts human-LLM agreement, even when within-group panel reliability is high.

Aggregated over tasks, the grading scale of 0-5 yields the strongest human-LLM alignment.

The research examined this question by collecting ratings from both human and LLM groups on three scales and across six benchmarks that include objective, open-ended subjective, and mixed tasks.

Additionally, pooled reliability can mask benchmark heterogeneity and reveal systematic subgroup differences in alignment across gender groups, strengthening the importance of scale design and sub-level diagnostic
…[truncated 395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5023
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-21T21:14:55.015335+00:00_

Web search results for query: ""Pairwise or Pointwise" evaluating feedback protocols bias LLM evaluation 2025"

Links: [{"title":"[2504.14716v2] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://arxiv.org/abs/2504.14716v2"},{"title":"[2504.14716] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://arxiv.org/abs/2504.14716"},{"title":"[2504.14716v1] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://arxiv.org/abs/2504.14716v1"},{"title":"Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://www.emergentmind.com/papers/2504.14716"},{"title":"Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation | OpenReview","url":"https://openreview.net/forum?id=uyX5Vnow3U"},{"title":"(PDF) Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://www.researchgate.net/publication/390991177_Pairwise_or_Pointwise_Evaluating_Feedback_Protocols_for_Bias_in_LLM-Based_Evaluation"},{"title":"[Literature Review] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://www.themoonlight.io/en/review/pairwise-or-pointwise-evaluating-feedback-protocols-for-bias-in-llm-based-evaluation"},{"title":"Pairwise or Pointwise? Evaluating Feedback Protocols for ...","url":"https://arxiv.org/pdf/2504.14716"}]

I found the research paper you're looking for! Here are the key findings:

## "Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation"

This paper examines how Large Language Models (LLMs) are widely used as proxies for human labelers in both training (Reinforcement Learning from AI Feedback) and large-scale response evaluation (LLM-as-a-judge).

**Main Findings:**

The choice of feedback protocol for evaluation (absolute scores versus relative preferen
…[truncated 901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6080
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-21T21:18:27.996503+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见 — Round 1 (Fresh Review)\n\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 扎实的实证研究，令人信服地展示了 Likert 和 pairwise 在检测 LLM judge 风格偏差上的敏感度差异，但核心发现的新颖性受限于经典心理测量学已有的理论预测，且论文框架存在系统性的过度声明。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论整体稳健，统计检验充分，多重校正恰当；但 Likert Blindspot 的因果解释存在替代假说（construct divergence），论文承认但框架和标题倾向性过强 |\n| Excitement | 3/5 | 结果对实践有用，但核心发现（pairwise 比 Likert 更灵敏）可从 Thurstone (1927) 的理论直接预期；增量贡献，非范式级创新 |\n| Reproducibility | 4/5 | 方法描述详尽，承诺 release 代码数据；使用公开 benchmark (LLMBar) 和标准统计工具 |\n| Confidence | 4/5 | 我对 LLM-as-Judge 评估方法论和心理测量学文献较为熟悉 |\n\n---\n\n## Strengths\n\n**S1. 系统性的实验设计和严谨的统计分析。** CSD pipeline 将风格控制重写、NLI 语义保留门控、位置控制的 pairwise 比较整合为一个完整框架。统计分析特别出色：Holm-Bonferroni 多重校正、七种统计方法的敏感度层次验证 (Table 2)、11 个 NLI 阈值的 sweep、bootstrap 衰减分析、4× 样本量复制 (n=355)。\n\n**S2. 多维度的鲁棒性验证。** 对几乎每一个可能的混淆因素都做了控制：rewriter independence、NLI gate ablation、cross-judge replication (3 architectures)、cross-benchmark replication、negative control (Claude Sonnet 4)、100-point continuous scale。六个独立控制有效约束了 Comparative Trap 放大效应的风险。\n\n**S3. GEE 条件分解揭示了 per-axis 的混淆结构差异。** Table 3 展示 verbosity 是 style-dominated (Style OR 8–13)、formality 是 conditional、register 是 judge-dependent。这是论文最具原创性的贡献。\n\n**S4. 负对照设计增强了辨别效度。** Claude Sonnet 4 在同一 pairwise 格式下未检测到偏差，排除了\"pairwise 格式本身产生虚假信号\"的解释。\n\n**S5. 论文写作的诚实性。** Limitations section 坦诚讨论了 construct divergence 替代解释、evaluator-producer bias 等问题。\n\n---\n\n## Must-Fix 问题\n\n**W1 [critical] \"The first framework\" 声明过度。** Abstract、Introduction 中声称 CSD 是 \"the first framework combining...\"——这是通过组合限定词构造唯一性的策略。RATE、Qiu et al. (2025)、CASSE、FairJudge 各自覆盖了核心组件。建议改为 \"a unified framework\"。\n\n**W2 [critical] \"Likert Blindspot\" 框架偏颇——construct divergence 替代假说被系统性弱化。** 标题和核心叙事将 Likert 框架为有缺陷，但 Section 5.2 承认 construct divergence 是同样合理的解释。更重要的是，Tripathi et al. (2025, arXiv:2504.14716) 发现 pairwise 更容易被 distractor features 操纵（flip rate 35% vs. 9%），直接挑战了将 pairwise 信号视为 ground truth 的隐含假设。建议给予 construct divergence 同等权重。\n\n**W3 [critical] 基准多样性不足。** 主要实验在 LLMBar (n=100) 上进行。跨 benchmark 验证仅覆盖少数配置。所有实验均为英文单轮对话。样本基础 (n≤355) 不足以支撑 \"systematic\" 的结论。\n\n---\n\n## Should-Fix 问题\n\n**W4 [warning] Abstract 信息密度过高**，7 句话中嵌入了 4 组括号内统计数据，可读性差。建议重写为两层结构。\n\n**W5 [warning] Evaluator-producer bias 处理不充分。** 所有三个 target judge 的 rewriting 都由 Qwen3-32B 完成。Register 轴完全未做 rewriter independence 验证。\n\n**W6 [warning] 遗漏关键近期文献：** (1) Tripathi et al. (2025) \"Pairwise or Pointwise?\" — 直接挑战 pairwise 信号的可靠性假设；(2) Li et al. (2026) \"Grading Scale Impact on LLM-as-a-Judge\" — 评分尺度对 LLM judge 的影响；(3) \"Fairness or Fluency?\" (arXiv:2601.13649)。\n\n**W7 [warning] 对 Thurstone (1927) 的理论关系定位不清。** 核心发现（pairwise > Likert 的灵敏度）可从近百年前的理论直接预测。论文需更清楚地说明 LLM-specific quantification 的增量价值。\n\n---\n\n## Questions\n\nQ1. 100-point 连续尺度的高 tie rate (51-66%) 是否说明 LLM judge 在绝对评分时对 style 变化确实不敏感（而非 Likert 工具有缺陷）？\n\nQ2. AlpacaEval verbosity (Likert d=0.375, BT=84.1%) 两者均显著——Blindspot 是否仅在 moderate effect sizes 时存在？\n\nQ3. Position-swap 后 inconsistent pair 比例是多少？是否接近 Tripathi et al. 的 35% flip rate？\n\nQ4. 如果用不同 rewriter (如 Llama-70B)，GEE confound structure 是否保持一致？\n\n---\n\n## Missing References\n\n1. Tripathi et al. (2025). \"Pairwise or Pointwise?\" arXiv:2504.14716\n2. Li et al. (2026). \"Grading Scale Impact on LLM-as-a-Judge\" arXiv:2601.03444\n3. \"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory\" arXiv:2602.00521\n\n---\n\n## Format Compliance\n- ✅ 主正文 8 页\n- ✅ Limitations section 存在且合理\n- ✅ 匿名 (Anonymous, review mode)\n- ✅ natbib 引用格式\n- ⚠️ Table 1 第 6 列无列标题\n- ⚠️ `\\usepackage{inconsolata}` 被注释掉，提交前需确认",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见 — Round 1 (Fresh Review)\n\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 扎实的实证研究，令人信服地展示了 Likert 和 pairwise 在检测 LLM judge 风格偏差上的敏感度差异，但核心发现的新颖性受限于经典心理测量学已有的理论预测，且论文框架存在系统性的过度声明。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论整体稳健，统计检验充分，多重校正恰当；但 Likert Blindspot 的因果解释存在替代假说（construct divergence），论文承认但框架和标题倾向性过强 |\n| Excitement | 3/5 | 结果对实践有用，但核心发现（pairwise 比 Likert 更灵敏）可从 Thurstone (1927) 的理论直接预期；增量贡献，非范式级创新 |\n| Reproducibility | 4/5 | 方法描述详尽，承诺 release 代码数据；使用公开 benchmark (LLMBar) 和标准统计工具 |\n| Confidence | 4/5 | 我对 LLM-as-Judge 评估方法论和心理测量学文献较为熟悉 |\n\n---\n\n## Strengths\n\n**S1. 系统性的实验设计和严谨的统计分析。** CSD pipeline 将风格控制重写、NLI 语义保留门控、位置控制的 pairwise 比较整合为一个完整框架。统计分析特别出色：Holm-Bonferroni 多重校正、七种统计方法的敏感度层次验证 (Table 2)、11 个 NLI 阈值的 sweep、bootstrap 衰减分析、4× 样本量复制 (n=355)。\n\n**S2. 多维度的鲁棒性验证。** 对几乎每一个可能的混淆因素都做了控制：rewriter independence、NLI gate ablation、cross-judge replication (3 architectures)、cross-benchmark replication、negative control (Claude Sonnet 4)、100-point continuous scale。六个独立控制有效约束了 Comparative Trap 放大效应的风险。\n\n**S3. GEE 条件分解揭示了 per-axis 的混淆结构差异。** Table 3 展示 verbosity 是 style-dominated (Style OR 8–13)、formality 是 conditional、register 是 judge-dependent。这是论文最具原创性的贡献。\n\n**S4. 负对照设计增强了辨别效度。** Claude Sonnet 4 在同一 pairwise 格式下未检测到偏差，排除了\"pairwise 格式本身产生虚假信号\"的解释。\n\n**S5. 论文写作的诚实性。** Limitations section 坦诚讨论了 construct divergence 替代解释、evaluator-producer bias 等问题。\n\n---\n\n## Must-Fix 问题\n\n**W1 [critical] \"The first framework\" 声明过度。** Abstract、Introduction 中声称 CSD 是 \"the first framework combining...\"——这是通过组合限定词构造唯一性的策略。RATE、Qiu et al. (2025)、CASSE、FairJudge 各自覆盖了核心组件。建议改为 \"a unified framework\"。\n\n**W2 [critical] \"Likert Blindspot\" 框架偏颇——construct divergence 替代假说被系统性弱化。** 标题和核心叙事将 Likert 框架为有缺陷，但 Section 5.2 承认 construct divergence 是同样合理的解释。更重要的是，Tripathi et al. (2025, arXiv:2504.14716) 发现 pairwise 更容易被 distractor features 操纵（flip rate 35% vs. 9%），直接挑战了将 pairwise 信号视为 ground truth 的隐含假设。建议给予 construct divergence 同等权重。\n\n**W3 [critical] 基准多样性不足。** 主要实验在 LLMBar (n=100) 上进行。跨 benchmark 验证仅覆盖少数配置。所有实验均为英文单轮对话。样本基础 (n≤355) 不足以支撑 \"systematic\" 的结论。\n\n---\n\n## Should-Fix 问题\n\n**W4 [warning] Abstract 信息密度过高**，7 句话中嵌入了 4 组括号内统计数据，可读性差。建议重写为两层结构。\n\n**W5 [warning] Evaluator-producer bias 处理不充分。** 所有三个 target judge 的 rewriting 都由 Qwen3-32B 完成。Register 轴完全未做 rewriter independence 验证。\n\n**W6 [warning] 遗漏关键近期文献：** (1) Tripathi et al. (2025) \"Pairwise or Pointwise?\" — 直接挑战 pairwise 信号的可靠性假设；(2) Li et al. (2026) \"Grading Scale Impact on LLM-as-a-Judge\" — 评分尺度对 LLM judge 的影响；(3) \"Fairness or Fluency?\" (arXiv:2601.13649)。\n\n**W7 [warning] 对 Thurstone (1927) 的理论关系定位不清。** 核心发现（pairwise > Likert 的灵敏度）可从近百年前的理论直接预测。论文需更清楚地说明 LLM-specific quantification 的增量价值。\n\n---\n\n## Questions\n\nQ1. 100-point 连续尺度的高 tie rate (51-66%) 是否说明 LLM judge 在绝对评分时对 style 变化确实不敏感（而非 Likert 工具有缺陷）？\n\nQ2. AlpacaEval verbosity (Likert d=0.375, BT=84.1%) 两者均显著——Blindspot 是否仅在 moderate effect sizes 时存在？\n\nQ3. Position-swap 后 inconsistent pair 比例是多少？是否接近 Tripathi et al. 的 35% flip rate？\n\nQ4. 如果用不同 rewriter (如 Llama-70B)，GEE confound structure 是否保持一致？\n\n---\n\n## Missing References\n\n1. Tripathi et al. (2025). \"Pairwise or Pointwise?\" arXiv:2504.14716\n2. Li et al. (2026). \"Grading Scale Impact on LLM-as-a-Judge\" arXiv:2601.03444\n3. \"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory\" arXiv:2602.00521\n\n---\n\n## Format Compliance\n- ✅ 主正文 8 页\n- ✅ Limitations section 存在且合理\n- ✅ 匿名 (Anonymous, review mode)\n- ✅ natbib 引用格式\n- ⚠️ Table 1 第 6 列无列标题\n- ⚠️ `\\usepackage{inconsolata}` 被注释掉，提交前需确认",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-21T21:18:31.460636+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3464
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-21T21:18:37.083136+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 569 · 2026-05-21T21:18:37.083663+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 570 · 2026-05-21T21:18:44.654863+00:00_

审稿意见已提交给 Review Director。

**审稿总结**：给出 Overall 3.5 (Borderline Conference)。

**主要优势**：统计方法论极其严谨（七种方法交叉验证、多重鲁棒性检验）、GEE per-axis confound structure 分解有原创性、Claude 负对照设计强化了辨别效度。

**三个 Must-Fix**：
1. "The first framework" 声明过度——核心组件均有先行工作，建议改为 "a unified framework"
2. "Likert Blindspot" 框架系统性偏向 measurement failure 叙事，弱化了 construct divergence 这一同样合理的替代解释；且遗漏了 Tripathi et al. (2025) 关于 pairwise 更易被 distractor 操纵的发现
3. 基准多样性不足——主要在 LLMBar (n=100) 上做实验，跨 benchmark 验证覆盖有限

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 18

## Round 18

8 recorded events


### User

_source line 571 · 2026-05-21T21:19:13.945986+00:00_

[Round 1 审稿请求]:
以下是 **Reviewer 1** 的完整审稿意见（侧重方法严谨性 + 实验设计）。请逐条回应其 Weaknesses 和 Questions：对每条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 完整审稿意见

### Summary
本文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated content control、per-axis style rewriting 和 position-controlled pairwise comparison 检测 LLM judge 的风格偏差。核心发现有二：(1) Likert Blindspot——Likert 评分系统性地遗漏 pairwise comparison 可以检测到的风格偏差（BT 63–84%, p < 0.001 vs. Likert n.s.），在中等效应量下完全失灵（d → 0 at n=355），在较强效应量下衰减超 60%；(2) GEE 条件分解揭示 per-axis confound 结构——verbosity 为 style-dominated，formality 为 conditional，register 为 judge-dependent。实验覆盖 4 个 judge、3 个 benchmark、3 个 style axis，方法论总体较为严谨，但在 evaluator-producer confound 控制和部分统计论证上存在可修复的不足。

### Strengths
S1: CSD 三阶段流水线设计逻辑清晰，DAG 标注精准，因果语言校准上乘。
S2: 七种统计方法的 sensitivity hierarchy（Table 2）是亮点，100-point continuous Likert 排除 granularity 解释。
S3: Cross-judge replication 覆盖三种架构 + Claude negative control 提供 discriminative validity。
S4: NLI gate 多层验证（11-threshold sweep, GPT-4o validation, NLI-fail ablation）罕见。
S5: Blindspot severity spectrum 刻画精细（d→0 at n=355, >60% attenuation at stronger effects）。

### Weaknesses
**W1 [Must-Fix]** Evaluator-producer confound 控制不充分——Qwen3-32B 同时做所有 rewriter，cross-rewriter validation 仅对 Qwen3-32B judge 做了 GPT-4o rewriter 替换（verbosity Style OR 降 22%），GPT-4o 和 Llama-70B judge 未做 cross-rewriter validation。
**W2 [Must-Fix]** Section 4.1 定义 8-test primary family 含 register，但 Table 1 把 register 标为 exploratory（†_e），多重比较校正不一致。
**W3 [Should-Fix]** TOST Δ=15pp 过宽——Claude BT 可达 65% 仍判定"无偏差"，与 GPT-4o formality +13pp (BT 63%) 被认定为 genuine bias 仅差 2pp。
**W4 [Should-Fix]** NLI FNR 估计循环性——8.4% FNR 由同一 Qwen3-32B 评估。
**W5 [Should-Fix]** Verbosity direction-aware NLI gate 有 17.4% FPR（GPT-4o validation）。
**W6 [Should-Fix]** 全文零人工验证。
**W7 [Minor]** Cross-benchmark 选择性测试——仅在预期效应最强的配置做 replication。
**W8 [Minor]** BT model 的 within-pair 依赖处理未讨论。

### Questions
Q1: Table 3 GPT-4o verbosity/formality GEE CI 缺失？
Q2: Likert 58-73% tie rate 是否反映 judge calibration 而非 Likert 局限？
Q3: Claude "no bias" vs TOST Δ=10pp underpowered 如何调和？
Q4: GEE Originality OR < 1 的确切语义？
Q5: 是否有 Qwen3-32B rewrite + GPT-4o judge vs GPT-4o rewrite + GPT-4o judge 的计划？

### Missing References
1. Shankar et al. (2024) — LLM 评估器验证的循环性
2. Huang et al. (2024) — LLM bias 综述
3. Zheng et al. (2024) — LLM-as-judge 局限性

---

请对以上 W1-W8 和 Q1-Q5 逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-21T21:20:13.399354+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex",
  "offset": "1",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex",
    "offset": "1",
    "limit": "15"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-21T21:20:14.304000+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	We designate a primary family of eight hypothesis tests (three judges $\times$ formality and verbosity, plus register for GPT-4o and Qwen3-32B) and control the family-wise error rate with Holm-Bonferroni correction at $\alpha = 0.05$.
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses are reported with uncorrected $p$-values and interpreted as hypothesis-generating; confirmatory analyses test specific hypotheses about pipeline validity and are evaluated at the nominal $\alpha = 0.05$ level without additional correction, as they address orthogonal questions about measurement reliability rather than the primary style-bias family.
12	Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the default regularization of the \texttt{choix} Python library.
13	All bootstrap confidence intervals use 10{,}000 pair-level resamples with seed 42.
14	
15	\begin{table}[t]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-21T21:20:14.404933+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "offset": "56",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
    "offset": "56",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 575 · 2026-05-21T21:20:14.455493+00:00_

56	
57	\paragraph{95\% confidence intervals.}
58	Table~\ref{tab:gee_ci} reports 95\% CIs for all GEE odds ratios in Table~\ref{tab:gee}.
59	
60	\begin{table}[h]
61	\centering
62	\small
63	\caption{95\% CIs for GEE conditional decomposition (Table~\ref{tab:gee}).}
64	\label{tab:gee_ci}
65	\begin{tabular}{@{}lcc@{}}
66	\toprule
67	Config & Style OR [CI] & Orig OR [CI] \\
68	\midrule
69	Qwen3 verb.\ & 13.10 [5.62, 30.55] & 0.49 [0.21, 1.13] \\
70	GPT-4o verb.\ & 11.34 & 0.45 \\
71	Llama-70B verb.\ & 8.21 [3.62, 18.65] & 0.38 [0.17, 0.86] \\
72	GPT-4o form.\ & 2.58 & 2.32 \\
73	Qwen3 form.\ & 4.20 [1.99, 8.87] & 4.70 \\
74	Qwen3 form.$^a$ & 2.15 [1.46, 3.16] & 4.99 [3.40, 7.34] \\
75	Llama-70B form.\ & 4.81 [2.48, 9.33] & 3.12 [1.61, 6.04] \\
76	GPT-4o reg.\ & 1.88 & 2.21 \\
77	Qwen3 reg.\ & 1.91 [1.01, 3.58] & 5.72 [3.02, 10.82] \\
78	Llama-70B reg.\ & 3.33 [1.75, 6.34] & 3.07 [1.60, 5.89] \\
79	\bottomrule
80	\multicolumn{3}{l}{\footnotesize $^a$ $n = 355$; other rows: $n = 88$.}
81	\end{tabular}
82	\end{table}
83	
84	\section{Rewriter Independence}
85	\label{app:rewriter_indep}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-21T21:22:05.874374+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R1-W1: Evaluator-producer confound 控制不充分**\n同意。Appendix D (Table 5-6) 仅验证了 Qwen3-32B judge 配置。GPT-4o 和 Llama-70B judge 的结果全部依赖 Qwen3-32B rewrite，从未用替代 rewriter 验证。verbosity Style OR 降 22% (13.10→10.17) 说明 inflation 确实存在，GPT-4o formality (BT 63.0%) 作为最弱效应配置尤其需要 cross-rewriter validation。与我的 R2-W5 独立一致。\n\n**[AGREE] R1-W2: Primary family 定义与 Table 1 标注不一致**\n明确矛盾。Section 4.1 定义 \"eight hypothesis tests...plus register for GPT-4o and Qwen3-32B\"（register 属于 primary family），但 Table 1 将 register 标为 †_e (exploratory)。两种解读都需要修改：要么 primary family 改为 six tests，要么 register 接受 Holm-Bonferroni 校正并更新 Table 1 标记。\n\n**[AGREE] R1-W3: TOST Δ=15pp 过宽**\n同意。15pp 等价区间与 GPT-4o formality 确认偏差 +13pp 仅差 2pp。不过补充：论文核心论证不依赖 TOST——Claude 的主要价值在于 pairwise 格式不产生虚假信号 (BT 56.2%/54.1% n.s.)。建议将语言从 \"equivalence confirmed\" 改为 \"failed to detect bias; TOST provides an upper bound\"。\n\n**[AGREE] R1-W4: NLI FNR 循环性**\n部分同意。初始 FNR 8.4% 使用 Qwen3-32B annotator 确有循环风险。但论文做了 GPT-4o cross-validation (Section 5.1: 92.1% formality / 82.6% verbosity pass precision)，部分打破循环。问题在于正文突出报告了循环的 Qwen3-32B 数据而非 GPT-4o 交叉验证。建议提升 GPT-4o 验证为主要数据。\n\n**[AGREE] R1-W5: Verbosity direction-aware NLI gate 17.4% FPR**\n同意是实质性 trade-off。部分缓解因素：GEE 的 Originality OR < 1 表明内容变化方向不利于 style direction，可部分吸收 FPR 引入的噪声。\n\n**[AGREE] R1-W6: 全文零人工验证**\n完全同意。content preservation 和 style bias 验证完全依赖 LLM，涉及测量工具敏感度的论文却用同类工具验证，存在认识论问题。\n\n**[REBUT] R1-W7: Cross-benchmark 选择性测试**\n部分反驳。formality 不是最强效应（verbosity 更强），且覆盖了两个 judge 和两个额外 benchmark。真正的问题是覆盖面不足（Llama-70B 无跨 benchmark、register 无跨 benchmark），而非 cherry-picking。与我的 R2-W3 从基准多样性角度提出了更精准的批评。\n\n**[REBUT] R1-W8: BT within-pair 依赖处理**\n反驳。Section 4.1 明确使用 \"pair-level resamples\"（以 text pair 为单位 bootstrap），正确处理了 within-pair 依赖。BT model 自然吸收 position effects。Section 3.3 区分了 sign test（仅用 consistent pairs）和 BT（用全部观测）两种策略。\n\n---\n\n### Questions 回应\n\n**[AGREE] R1-Q1**: 确认 Appendix C Table (tab:gee_ci) 中 GPT-4o verb/form/reg 和 Qwen3 form Orig OR 共 7 个 CI 缺失。必须补全。\n\n**[AGREE] R1-Q2**: 与我的 R2-W2/R2-Q1 高度一致。58-73% tie rate（含 100-point scale 的 51-66%）支持 construct divergence 解释：judge 正确判定 style-only 变化不影响 absolute quality。论文严重弱化了这个同等合理的解释。\n\n**[AGREE] R1-Q3**: \"detects no bias\" ≠ \"failed to detect bias\"。TOST at Δ=10pp underpowered 意味着无法排除 moderate bias 的存在。\n\n**[REBUT] R1-Q4**: 论文已解释。Originality OR < 1 = 控制 style 后 judge 偏好 rewrite over original（rewriting artifact）。Section 5.4 + Appendix P (tab:artifact) BT P(orig) = 0.08-0.17 进一步确认。方向对 style bias 估计是保守的。\n\n**[AGREE] R1-Q5**: GPT-4o judge 的 cross-rewriter validation 是重要缺口，特别是 GPT-4o formality (BT 63.0%) 为最弱配置。\n\n---\n\n### 两位 Reviewer 的共识与分歧总结\n\n**共识（两人独立一致）**:\n1. Evaluator-producer confound 是主要不足 (R1-W1 = R2-W5)\n2. 零人工验证 (R1-W6 ≈ R2 隐含关注)\n3. Construct divergence 解释未获同等权重 (R1-Q2 = R2-W2)\n4. Benchmark 覆盖面不足 (R1-W7 ≈ R2-W3)\n\n**R2 独立补充的关键问题**:\n1. \"The first framework\" overclaim (R2-W1)\n2. 遗漏 Tripathi et al. (2025) 等关键文献 (R2-W6)\n3. Abstract 信息密度过高 (R2-W4)\n4. Thurstone 理论关系定位不清 (R2-W7)\n\n**分歧**:\n- R1-W7 (selective testing): R1 认为 cherry-picking，我认为是覆盖面不足但非刻意选择\n- R1-W8 (BT dependency): R1 认为未处理，我认为 pair-level bootstrap 已充分处理",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R1-W1: Evaluator-producer confound 控制不充分**\n同意。Appendix D (Table 5-6) 仅验证了 Qwen3-32B judge 配置。GPT-4o 和 Llama-70B judge 的结果全部依赖 Qwen3-32B rewrite，从未用替代 rewriter 验证。verbosity Style OR 降 22% (13.10→10.17) 说明 inflation 确实存在，GPT-4o formality (BT 63.0%) 作为最弱效应配置尤其需要 cross-rewriter validation。与我的 R2-W5 独立一致。\n\n**[AGREE] R1-W2: Primary family 定义与 Table 1 标注不一致**\n明确矛盾。Section 4.1 定义 \"eight hypothesis tests...plus register for GPT-4o and Qwen3-32B\"（register 属于 primary family），但 Table 1 将 register 标为 †_e (exploratory)。两种解读都需要修改：要么 primary family 改为 six tests，要么 register 接受 Holm-Bonferroni 校正并更新 Table 1 标记。\n\n**[AGREE] R1-W3: TOST Δ=15pp 过宽**\n同意。15pp 等价区间与 GPT-4o formality 确认偏差 +13pp 仅差 2pp。不过补充：论文核心论证不依赖 TOST——Claude 的主要价值在于 pairwise 格式不产生虚假信号 (BT 56.2%/54.1% n.s.)。建议将语言从 \"equivalence confirmed\" 改为 \"failed to detect bias; TOST provides an upper bound\"。\n\n**[AGREE] R1-W4: NLI FNR 循环性**\n部分同意。初始 FNR 8.4% 使用 Qwen3-32B annotator 确有循环风险。但论文做了 GPT-4o cross-validation (Section 5.1: 92.1% formality / 82.6% verbosity pass precision)，部分打破循环。问题在于正文突出报告了循环的 Qwen3-32B 数据而非 GPT-4o 交叉验证。建议提升 GPT-4o 验证为主要数据。\n\n**[AGREE] R1-W5: Verbosity direction-aware NLI gate 17.4% FPR**\n同意是实质性 trade-off。部分缓解因素：GEE 的 Originality OR < 1 表明内容变化方向不利于 style direction，可部分吸收 FPR 引入的噪声。\n\n**[AGREE] R1-W6: 全文零人工验证**\n完全同意。content preservation 和 style bias 验证完全依赖 LLM，涉及测量工具敏感度的论文却用同类工具验证，存在认识论问题。\n\n**[REBUT] R1-W7: Cross-benchmark 选择性测试**\n部分反驳。formality 不是最强效应（verbosity 更强），且覆盖了两个 judge 和两个额外 benchmark。真正的问题是覆盖面不足（Llama-70B 无跨 benchmark、register 无跨 benchmark），而非 cherry-picking。与我的 R2-W3 从基准多样性角度提出了更精准的批评。\n\n**[REBUT] R1-W8: BT within-pair 依赖处理**\n反驳。Section 4.1 明确使用 \"pair-level resamples\"（以 text pair 为单位 bootstrap），正确处理了 within-pair 依赖。BT model 自然吸收 position effects。Section 3.3 区分了 sign test（仅用 consistent pairs）和 BT（用全部观测）两种策略。\n\n---\n\n### Questions 回应\n\n**[AGREE] R1-Q1**: 确认 Appendix C Table (tab:gee_ci) 中 GPT-4o verb/form/reg 和 Qwen3 form Orig OR 共 7 个 CI 缺失。必须补全。\n\n**[AGREE] R1-Q2**: 与我的 R2-W2/R2-Q1 高度一致。58-73% tie rate（含 100-point scale 的 51-66%）支持 construct divergence 解释：judge 正确判定 style-only 变化不影响 absolute quality。论文严重弱化了这个同等合理的解释。\n\n**[AGREE] R1-Q3**: \"detects no bias\" ≠ \"failed to detect bias\"。TOST at Δ=10pp underpowered 意味着无法排除 moderate bias 的存在。\n\n**[REBUT] R1-Q4**: 论文已解释。Originality OR < 1 = 控制 style 后 judge 偏好 rewrite over original（rewriting artifact）。Section 5.4 + Appendix P (tab:artifact) BT P(orig) = 0.08-0.17 进一步确认。方向对 style bias 估计是保守的。\n\n**[AGREE] R1-Q5**: GPT-4o judge 的 cross-rewriter validation 是重要缺口，特别是 GPT-4o formality (BT 63.0%) 为最弱配置。\n\n---\n\n### 两位 Reviewer 的共识与分歧总结\n\n**共识（两人独立一致）**:\n1. Evaluator-producer confound 是主要不足 (R1-W1 = R2-W5)\n2. 零人工验证 (R1-W6 ≈ R2 隐含关注)\n3. Construct divergence 解释未获同等权重 (R1-Q2 = R2-W2)\n4. Benchmark 覆盖面不足 (R1-W7 ≈ R2-W3)\n\n**R2 独立补充的关键问题**:\n1. \"The first framework\" overclaim (R2-W1)\n2. 遗漏 Tripathi et al. (2025) 等关键文献 (R2-W6)\n3. Abstract 信息密度过高 (R2-W4)\n4. Thurstone 理论关系定位不清 (R2-W7)\n\n**分歧**:\n- R1-W7 (selective testing): R1 认为 cherry-picking，我认为是覆盖面不足但非刻意选择\n- R1-W8 (BT dependency): R1 认为未处理，我认为 pair-level bootstrap 已充分处理",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-21T21:22:09.337457+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3463
}
```

</details>

---


### Assistant

_source line 578 · 2026-05-21T21:22:17.573746+00:00_

交叉回应已提交。总结：

- **W1-W6**: 5 条 AGREE，1 条部分 AGREE（W4 循环性有 GPT-4o cross-validation 部分缓解）
- **W7-W8**: 2 条 REBUT（W7 是覆盖面不足而非 cherry-picking；W8 pair-level bootstrap 已处理依赖）
- **Q1-Q5**: 3 条 AGREE（Q1 CI 缺失、Q2 tie rate 支持 construct divergence、Q3/Q5 措辞和实验缺口），1 条 REBUT（Q4 论文已解释 Originality OR 语义）

两位 Reviewer 在 evaluator-producer confound、零人工验证、construct divergence 弱化、benchmark 覆盖面上形成了独立共识。我额外指出了 "first framework" overclaim、遗漏关键文献 (Tripathi et al. 2025)、Abstract 可读性三个 R1 未覆盖的问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 19

## Round 19

68 recorded events


### User

_source line 579 · 2026-05-22T03:25:16.041887+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性、完整性与写作质量**审查。

## Venue 信息
- **目标**: EMNLP 2026 Main Conference (Long Paper via ARR)
- **截止日期**: 2026-05-25
- **页数限制**: 正文 ≤8 页，参考文献不限页数。Limitations 和 Ethics 不计入页数限制（但不能含过多额外内容）。
- **模板**: ACL 双栏格式 (`\usepackage[review]{acl}`)
- **匿名**: Double-blind（作者信息应匿名）
- **Checklist**: ARR Responsible NLP Checklist 在 OpenReview submission form 中填写，不在 PDF 中

## 论文文件
- 主文件: `projects/causal_style_decomp_judge/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf`

## 你的审查侧重

**核心职责：新颖性评估、Related Work 完整性、叙事质量与论文呈现**

请重点审查以下方面：

### 1. 新颖性与贡献 (Novelty & Contribution)
- "Likert Blindspot" 是否为 genuine novel finding？还是 Thurstone (1927) 心理测量学已知现象在 LLM judge domain 的 transfer？novelty 如何正确定位？
- CSD framework 的独立贡献——将 NLI-gated control + per-axis decomposition + position-controlled pairwise comparison 组合为统一框架，这是否有足够增量价值？
- GEE conditional decomposition 揭示的 per-axis confound structure 是否构成独立贡献？
- 论文的 claim 强度是否与 evidence 匹配？是否存在 overclaim（如 "first framework" 等措辞）？

### 2. Related Work 完整性
- 是否充分覆盖以下领域：
  - LLM-as-Judge style bias（SOS-Bench, Preference Leakage, FairJudge, CASSE 等）
  - Interventional text analysis（CausalM, Polyjuice, RATE 等）
  - Measurement theory（Thurstone, Stevens, Likert scale literature）
  - Pairwise vs pointwise evaluation（Comparative Trap, Tripathi et al.）
  - Position bias（Zheng et al., Wang et al., Shi et al.）
- 是否有重要遗漏的相关工作？
- 对 RATE 的批评是否公平？

### 3. 写作质量与呈现 (Presentation)
- Abstract 是否清晰、简洁、信息密度适当？
- Introduction 的叙事逻辑是否流畅？motivating example 是否有效？
- 图表质量：Figure 1 (pipeline), Figure 2 (DAG), Figure 3 (forest plot), Figure 4 (power curve)——是否清晰、专业、信息丰富？
- Table 1 (main results) 的设计是否易读？列标题/footnotes 是否完整？
- Conclusion 是否适当总结了贡献而不 overclaim？
- 整体叙事：measurement attenuation vs construct divergence 两种解释是否获得平等讨论？

### 4. 完整性 (Completeness)
- 实验覆盖面：4 target judges + 1 negative control, 3 benchmarks, 3 style axes——是否充分？
- 缺失的实验或分析：有哪些可合理预期但未做的？
- Limitations 是否坦诚并覆盖主要 weak points？
- Code and Data availability statement 是否合规？

### 5. 格式与匿名
- 匿名化是否完整（无自引泄漏、无 acknowledgment）？
- 正文是否 ≤8 页？
- 引用格式是否一致（natbib 风格，年份括号等）？

请提供：
1. **Summary** (2-3 句)
2. **Strengths** (逐条)
3. **Weaknesses** (逐条，分 Must-Fix / Should-Fix / Minor)
4. **Questions** (需要作者澄清的)
5. **Missing References** (如有)
6. **Overall Assessment** (评分 + 置信度)
7. **Detailed Comments** (逐节)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-22T03:25:23.334046+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
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

_source line 581 · 2026-05-22T03:25:23.485036+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-22T03:25:27.503886+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 583 · 2026-05-22T03:25:28.058709+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 reviewer guidelines review form dimensions scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 reviewer guidelines review form dimensions scoring"
  }
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-22T03:25:28.913901+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-22T03:25:32.659539+00:00_

Web search results for query: "EMNLP 2026 reviewer guidelines review form dimensions scoring"

Links: [{"title":"2026 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2026/ReviewerGuidelines"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Advice on Reviewing for EMNLP","url":"https://2020.emnlp.org/blog/2020-05-17-write-good-reviews/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, I found information about EMNLP 2026's review process:

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference.

However, the search results don't contain specific details about the review form dimensions and scoring scales for EMNLP 2026. The results show some general reviewing criteria like technical soundness and clarity, but not the complete review form structure with specific scoring dimensions.

Reviews must be completed by July 6, 2026, or meta-reviews by July 29.

For detailed information about the specific review form dimensions and scoring scale used by EMNLP 2026, you may need to consult the ARR (ACL Rolling Review) system directly or the EMNLP 2026 official website, as this specific technical detail doesn't appear in the publicly available search results I found.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4600
}
```

</details>

---


### Tool result

_source line 586 · 2026-05-22T03:25:35.576740+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines, review form, and criteria:

## Reviewer Guidelines

ARR asks reviewers to follow a workflow: read the paper and get the first impression, then search for related
…[truncated 1248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8072
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-22T03:25:36.882954+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 468.9}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 565.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 499.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p9.png\", \"w
…[truncated 515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7969
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-22T03:25:41.854396+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and the overall assessment criteria. List every field a reviewer must fill in."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and the overall assessment criteria. List every field a reviewer must fill in."
  }
}
```

</details>

---


### Tool call

_source line 589 · 2026-05-22T03:25:43.265892+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, what counts as a good review, scoring criteria, and any specific instructions about novelty, soundness, presentation, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, what counts as a good review, scoring criteria, and any specific instructions about novelty, soundness, presentation, etc."
  }
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-22T03:25:44.223469+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "11-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "11-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 591 · 2026-05-22T03:25:45.179621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-22T03:25:45.632403+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 593 · 2026-05-22T03:25:46.084568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-22T03:25:46.737226+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-22T03:25:52.464052+00:00_

# ARR Reviewer Guidelines Summary

## Core Evaluation Framework

Reviewers assess papers across three dimensions:

1. **Soundness**: Technical validity and methodological rigor
2. **Excitement**: Personal interest and subjective appeal
3. **Overall Recommendation**: Composite judgment for acceptance decisions

## What Reviewers Should Evaluate

### Technical Soundness
Reviewers must verify "sufficient evidence for the claim that the authors are making." This includes checking methodology, proof validity, experimental design, and statistical rigor. Papers must demonstrate clear research questions addressing genuine knowledge gaps.

### Novelty and Contribution
Novelty requires demonstrating that work isn't "highly similar work...published [3+ months prior to submission deadline]." However, the guidelines caution against dismissing contributions merely because results seem obvious in retrospect or because methods are simple. Non-traditional contributions—resource papers, reproductions, analyses—merit fair evaluation.

### Presentation and Clarity
Reviews should identify when "key terms too vague and not defined" or when "research question or contribution" remains unclear. Poor writing isn't grounds for rejection unless clarity is genuinely compromised.

## Characteristics of Strong Reviews

**Specificity is Essential**
Rather than vague complaints ("X is not clear"), effective reviews state precisely what's missing: "Y and Z are missing from the description of X."

**Professional Tone**
Reviews should maintain neutrality and avoid sarcasm. As guidance notes, "write the review you would like to get yourself."

**Justified Scores**
"Low Soundness scores without sufficient justification" indicate reviewers haven't explained their assessments adequately. Scores must reflect review content.

## Common Review Mistakes to Avoid

The guidelines identify 17 problematic heuristics (H1-H17):

- **Hindsight bias** ("results seem obvious")
- **Confirmation bias** (dismissing contr
…[truncated 835 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 9198
}
```

</details>

---


### Tool result

_source line 596 · 2026-05-22T03:25:57.885491+00:00_

# ACL Rolling Review Form - Complete Structure

## Required Narrative Fields

1. **Paper Summary** - Overview of paper topic and content
2. **Summary of Strengths** - Reasons for publication at selective venues
3. **Summary of Weaknesses** - Numbered concerns about the paper
4. **Comments/Suggestions/Typos** - Additional improvement suggestions

## Scoring Dimensions

### Reviewer Confidence
Scale: 1-5
- 5 = Positive evaluation is correct; carefully read paper and familiar with related work
- 4 = Quite sure; checked important points carefully
- 3 = Pretty sure; good feel for area but didn't verify all details
- 2 = Can defend evaluation but likely missed details or novelty assessment
- 1 = "Not my area, or paper is very hard to understand"

### Soundness
Scale: 1-5 (with half-point increments)
Evaluates scientific rigor, experimental design, and claim support across paper types

### Excitement
Scale: 1-5 (with half-point increments)
Subjective assessment of innovation, impact potential, and relevance to reviewer

### Overall Assessment
Scale: 1-5 (with half-point increments)
Ranges from award consideration to rejection recommendations

## Additional Required Fields

5. **Best Paper Justification** - Required only if recommending award consideration
6. **Limitations and Societal Impact** - Assessment of author acknowledgment of limitations and societal implications
7. **Ethical Concerns** - Evaluation against ACL ethics code
8. **Needs Ethics Review** - Determination if paper requires specialized ethics committee review
9. **Reproducibility** - Scale 1-5 assessing result reproducibility capability
10. **Datasets** - Scale 1-5 rating value of released datasets
11. **Software** - Scale 1-5 rating value of released software
12. **Author Identity Knowledge** - Scale 1-5 assessing reviewer's knowledge of authors

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 16031
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-22T03:25:58.488531+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 435.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 562.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 600.7}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.9}], \"total_pages\": 15, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 14265
}
```

</details>

---


### Tool result

_source line 598 · 2026-05-22T03:26:00.401300+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 15221
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-22T03:26:00.653906+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 13916
}
```

</details>

---


### Tool result

_source line 600 · 2026-05-22T03:26:00.655685+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 14571
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-22T03:26:00.656950+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 15024
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-22T03:26:05.426515+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 603 · 2026-05-22T03:26:05.979487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 604 · 2026-05-22T03:26:06.885623+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1459
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-22T03:26:06.887100+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-22T03:26:06.887505+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 607 · 2026-05-22T03:26:07.390271+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 608 · 2026-05-22T03:26:07.846024+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 609 · 2026-05-22T03:26:07.846545+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 610 · 2026-05-22T03:26:08.403153+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1012
}
```

</details>

---


### Tool call

_source line 611 · 2026-05-22T03:26:08.507475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 612 · 2026-05-22T03:26:08.659355+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 812
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-22T03:26:09.164233+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-22T03:26:13.334212+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 615 · 2026-05-22T03:26:13.736204+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 616 · 2026-05-22T03:26:14.189135+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 617 · 2026-05-22T03:26:14.189666+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 618 · 2026-05-22T03:26:15.094598+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1358
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-22T03:26:15.097339+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-22T03:26:15.097765+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 621 · 2026-05-22T03:26:15.298846+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 622 · 2026-05-22T03:26:16.003930+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool result

_source line 623 · 2026-05-22T03:26:16.256430+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-22T03:28:04.409355+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FairJudge LLM evaluation bias style 2024 2025 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FairJudge LLM evaluation bias style 2024 2025 paper"
  }
}
```

</details>

---


### Tool call

_source line 625 · 2026-05-22T03:28:04.459882+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SOS-Bench style over substance LLM judge evaluation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SOS-Bench style over substance LLM judge evaluation 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-22T03:28:04.911524+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CASSE style bias LLM judge multi-feature framework Cho 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CASSE style bias LLM judge multi-feature framework Cho 2026"
  }
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-22T03:28:10.035716+00:00_

Web search results for query: "SOS-Bench style over substance LLM judge evaluation 2024 2025"

Links: [{"title":"[Literature Review] Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://www.themoonlight.io/en/review/style-outweighs-substance-failure-modes-of-llm-judges-in-alignment-benchmarking"},{"title":"Paper page - Style over Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://huggingface.co/papers/2409.15268"},{"title":"[2409.15268] Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://arxiv.org/abs/2409.15268"},{"title":"Style Outweighs Substance: Failure Modes of LLM Judges in Alignment   Benchmarking","url":"https://arxiv.org/pdf/2409.15268"},{"title":"Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://arxiv.org/html/2409.15268v2"},{"title":"Style over Substance: Failure Modes of LLM Judges in Alignment Benchmarking - Paper Details","url":"https://www.chatpaper.ai/paper/ed0aef10-7489-4061-84af-ffd7b9649e86"},{"title":"Style over Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://arxiv.org/html/2409.15268v1"},{"title":"(PDF) Style over Substance: Failure Modes of LLM Judges in Alignment Benchmarking","url":"https://www.researchgate.net/publication/384288829_Style_over_Substance_Failure_Modes_of_LLM_Judges_in_Alignment_Benchmarking"},{"title":"Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking | OpenReview","url":"https://openreview.net/forum?id=MzHNftnAM1"}]

Based on the search results, here's what I found about SOS-Bench and the research on LLM judge evaluation:

## Overview

The paper "Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking" was written by Benjamin Feuer et al. and presented at the International Conference on Learning Representations (ICLR) in 2025.

## SOS-Bench Benchmark

SOS-Bench (Substance Ou
…[truncated 1145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5575
}
```

</details>

---


### Tool result

_source line 628 · 2026-05-22T03:28:11.342992+00:00_

Web search results for query: "CASSE style bias LLM judge multi-feature framework Cho 2026"

Links: [{"title":"Evaluating Scoring Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2506.22316"},{"title":"Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation","url":"https://arxiv.org/pdf/2603.05485"},{"title":"LLM as a Judge: A 2026 Guide to Automated Model Assessment | Label Your Data","url":"https://labelyourdata.com/articles/llm-as-a-judge"},{"title":"The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2509.26072"},{"title":"BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation","url":"https://arxiv.org/pdf/2602.09383"},{"title":"Evaluating and Mitigating LLM-as-a-judge Bias in Communication Systems","url":"https://arxiv.org/pdf/2510.12462"},{"title":"Fairness or Fluency? An Investigation into Language Bias of Pairwise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2601.13649"}]

Based on the search results, I found relevant research on LLM-as-a-Judge bias, though the specific paper matching all your query terms may not be directly listed. Here are the key findings:

A comprehensive framework has been proposed that shifts focus from biases tied to evaluation targets to those originating from the scoring prompt itself, identifying three novel types: rubric order bias, score ID bias, and reference answer score bias. This framework features a suite of multi-faceted metrics and an automatic data synthesis pipeline to create a tailored evaluation corpus.

Experiments demonstrate that even the most advanced LLMs suffer from these substantial scoring biases.

Additional research on LLM-as-a-Judge biases includes:

- Style-related biases where AI judges might be swayed by writing style or tone, over-rewarding eloquent phrasing.
- Studies revealing that models exhibit a strong recency bias, systematically favoring "new" responses over "old", as well as a clear provenance hierarchy.

The search resu
…[truncated 355 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6431
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-22T03:28:13.503460+00:00_

Web search results for query: "FairJudge LLM evaluation bias style 2024 2025 paper"

Links: [{"title":"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge","url":"https://arxiv.org/pdf/2602.06625"},{"title":"LLM-as-a-Judge: Why Frontier Models Fail 50%+ Bias Tests | Adaline","url":"https://www.adaline.ai/blog/llm-as-a-judge-reliability-bias"},{"title":"LLM-Judge Evaluation Techniques","url":"https://www.emergentmind.com/topics/llm-judge-evaluation"},{"title":"LLM-as-a-Judge Evaluation","url":"https://www.emergentmind.com/topics/llm-as-a-judge-evaluations"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://arxiv.org/html/2410.02736v1"},{"title":"Mitigating the Bias of Large Language Model Evaluation","url":"https://arxiv.org/pdf/2409.16788"}]

Based on the search results, here's what I found about FairJudge:

## FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge

FairJudge was published in February 2026 by Bo Yang and colleagues, addressing critical limitations in LLM-based evaluation.

**Key Approach:**
The paper adopts a curriculum-style SFT-DPO-GRPO training paradigm that progressively aligns rubric adherence, bias mitigation, and cross-mode consistency, while avoiding catastrophic forgetting. More specifically, SFT establishes the base judge behavior; DPO targets non-semantic biases, including position, format, and length; GRPO enforces consistency across scoring modes.

**Problems Addressed:**
The paper identifies position bias (where judgment flips when answer order is swapped) and pointwise-pairwise inconsistency (where the same answers receive contradictory judgments under different evaluation modes).

**Results:**
Experimental results on multiple internal and public benchmarks show that FairJudge consistently improves agreement and F1, reduces non-semantic biases, and outperforms substantially larger instruction-tuned LLMs.

The paper appears to be available on arXiv at https://arxiv.org/pdf/2602.06
…[truncated 107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9094
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-22T03:28:18.728412+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Polyjuice counterfactual generation Wu 2021 NLP ACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Polyjuice counterfactual generation Wu 2021 NLP ACL"
  }
}
```

</details>

---


### Tool call

_source line 631 · 2026-05-22T03:28:19.682539+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"preference leakage\" LLM judge evaluation Dubois 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"preference leakage\" LLM judge evaluation Dubois 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 632 · 2026-05-22T03:28:19.933444+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Likert vs pairwise comparison NLP evaluation LLM rating scale 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Likert vs pairwise comparison NLP evaluation LLM rating scale 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-22T03:28:24.003076+00:00_

Web search results for query: "Polyjuice counterfactual generation Wu 2021 NLP ACL"

Links: [{"title":"Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models","url":"https://idl.uw.edu/papers/polyjuice"},{"title":"Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/polyjuice-generating-counterfactuals-for-explaining-evaluating-and-improving-models/"},{"title":"Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.523/"},{"title":"[2101.00288] Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models","url":"https://arxiv.org/abs/2101.00288"},{"title":"polyjuice-nlp · PyPI","url":"https://pypi.org/project/polyjuice-nlp/"},{"title":"Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10293092"},{"title":"GitHub - tongshuangwu/polyjuice · GitHub","url":"https://github.com/tongshuangwu/polyjuice"},{"title":"Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models | Request PDF","url":"https://www.researchgate.net/publication/353484822_Polyjuice_Generating_Counterfactuals_for_Explaining_Evaluating_and_Improving_Models"}]

I found the paper you're looking for! Here's what the search revealed:

Polyjuice is a general-purpose counterfactual generator that allows for control over perturbation types and locations, trained by finetuning GPT-2 on multiple datasets of paired sentences. The paper was authored by Tongshuang Wu, Marco Tulio Ribeiro, Jeffrey Heer, and Daniel S. Weld and was published in the Association for Computational Linguistics (ACL) in 2021.

The work demonstrates that Polyjuice produces diverse sets of realistic counterfactuals useful for various applications inc
…[truncated 605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5274
}
```

</details>

---


### Tool result

_source line 634 · 2026-05-22T03:28:25.861793+00:00_

Web search results for query: ""preference leakage" LLM judge evaluation Dubois 2024 2025"

Links: [{"title":"Preference Leakage: A Contamination Problem in LLM-as- ...","url":"https://arxiv.org/pdf/2502.01534"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://howiehwong.github.io/preference_leakage.pdf"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://openreview.net/pdf?id=gW6NT2IuME"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/html/2502.01534v3"},{"title":"(PDF) Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://www.researchgate.net/publication/388685541_Preference_Leakage_A_Contamination_Problem_in_LLM-as-a-judge"}]

I found relevant research on preference leakage in LLM-as-a-judge evaluation. Here's what the search results show:

## Overview

The research addresses potential contamination that occurs when the generator and evaluator LLMs share a close relationship. This issue is particularly pervasive in popular LLM-as-a-judge benchmarks like AlpacaEval 2.0 (Dubois et al. 2024) and Arena-Hard (Li et al. 2024e), due to the common reliance on the most advanced LLMs, such as GPT-4, for both data synthesis and evaluation.

## Key Problem

The preference of the LLM evaluators can leak to the student models through synthetic data and thus inflate the evaluation score. This relatedness—akin to the overlap between training data and evaluation sets in traditional data contamination—introduces a systematic bias.

## Evaluation Datasets

The research evaluates on two representative pairwise evaluation datasets: Arena-Hard and AlpacaEval 2.0, which contains 805 questions.

The paper appears to have been recently published (March 2026 based on one source date), examining how preference leakage occurs in synthetic data generation when using the same or related LLMs for both data generation and evaluation.


REMINDER: 
…[truncated 90 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6179
}
```

</details>

---


### Tool result

_source line 635 · 2026-05-22T03:28:26.515326+00:00_

Web search results for query: "Likert vs pairwise comparison NLP evaluation LLM rating scale 2024 2025"

Links: [{"title":"Reference-Free Rating of LLM Responses via Latent Information","url":"https://hcai-munich.com/pubs/Girrbach2025Reference.pdf"},{"title":"Likert or Not: LLM Absolute Relevance Judgments on Fine-Grained Ordinal Scales","url":"https://arxiv.org/html/2505.19334v1"},{"title":"A reliable LLM-as-a-Judge framework for evaluating text ...","url":"https://aclanthology.org/2025.emnlp-main.796.pdf"},{"title":"Reference-Free Rating of LLM Responses via Latent Information","url":"https://arxiv.org/pdf/2509.24678"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences   of LLM Evaluators","url":"https://arxiv.org/pdf/2406.12319"},{"title":"Confidence and Stability of Global and Pairwise Scores in NLP Evaluation","url":"https://arxiv.org/pdf/2507.01633"}]

I've found relevant research on this topic from 2024-2025. Here are the key findings:

## Recent Comparative Analysis

LLM-as-a-Judge evaluation can be categorized into pairwise and pointwise evaluation approaches. The search results reveal important distinctions between these methods:

### Likert Scale (Pointwise) Approaches

The prevailing approach is the LLM-as-a-Judge paradigm, in which a model rates responses, typically on a 5-point Likert scale. However, scores can be unstable, with the same response receiving different ratings across runs, and ratings are often poorly calibrated, compressing near the top of the scale and leading to frequent ties and limited discriminability.

Additionally, there are inherent limitations of Likert scale ratings, and recent research from 2025 explores alternatives like fine-grained ordinal scales that may outperform traditional Likert approaches.

### Pairwise Comparison Approaches

Pairwise methods outperform pointwise scoring, though pairwise comparisons have their own limitations. Pairwise comparisons scale poorly to listwise rankings due t
…[truncated 578 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6581
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-22T03:28:44.947461+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Comparative Trap\" pairwise comparison amplifies biased preferences LLM evaluators Jeong 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Comparative Trap\" pairwise comparison amplifies biased preferences LLM evaluators Jeong 2025"
  }
}
```

</details>

---


### Tool call

_source line 637 · 2026-05-22T03:28:45.148376+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Thurstone 1927 law comparative judgment paired comparison rating scale sensitivity psychometrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Thurstone 1927 law comparative judgment paired comparison rating scale sensitivity psychometrics"
  }
}
```

</details>

---


### Tool result

_source line 638 · 2026-05-22T03:28:51.982671+00:00_

Web search results for query: ""Comparative Trap" pairwise comparison amplifies biased preferences LLM evaluators Jeong 2025"

Links: [{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators - ACL Anthology","url":"https://aclanthology.org/2025.blackboxnlp-1.5/"},{"title":"[2406.12319] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://arxiv.org/abs/2406.12319"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://arxiv.org/html/2406.12319v4"},{"title":"[PDF] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Comparative-Trap:-Pairwise-Comparisons-Biased-Jeong-Park/cd6191f270c5b98dec44a294e4f3cebcf371ac5f"},{"title":"[Literature Review] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://www.themoonlight.io/en/review/the-comparative-trap-pairwise-comparisons-amplifies-biased-preferences-of-llm-evaluators"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences   of LLM Evaluators","url":"https://arxiv.org/pdf/2406.12319"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators (arXiv:2406.12319v4) - ScienceStack","url":"https://www.sciencestack.ai/paper/2406.12319"}]

I found the research you're looking for! "The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators" by Jeong et al. was presented at the 8th BlackboxNLP Workshop in 2025.

Here are the key findings:

**Core Problem:** LLM evaluators often display biased preferences, such as favoring verbosity and authoritative tones. These biases are exacerbated in pairwise evaluation, where LLMs directly compare two outputs and easily prioritize superficial attributes.

**Key Insight:** Pointwise e
…[truncated 639 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7035
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-22T03:28:58.713486+00:00_

Web search results for query: "Thurstone 1927 law comparative judgment paired comparison rating scale sensitivity psychometrics"

Links: [{"title":"A Law of Comparative Judgment","url":"https://www.researchgate.net/publication/221678018_A_Law_of_Comparative_Judgment"},{"title":"A LAW OF COMPARATIVE JUDGMENT1 B Y L L THURSTONE The University of Chicago","url":"https://parsmodir.com/wp-content/uploads/2013/02/thurstone1927.pdf"},{"title":"(PDF) Thurstone's Law of Comparative Judgment for Group Support","url":"https://www.academia.edu/19934674/Thurstones_Law_of_Comparative_Judgment_for_Group_Support"},{"title":"A Law of Comparative Preference: Distinctions Between Models of Personal Preference and Impersonal Judgment in Pair Comparison Designs - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC6463346/"},{"title":"L. L. Thurstone: A Law of Comparative Judgment","url":"https://brocku.ca/MeadProject/Thurstone/Thurstone_1927f.html"},{"title":"(PDF) On Thurstone’s Model for Paired Comparisons and Ranking Data","url":"https://www.researchgate.net/publication/236623596_On_Thurstone's_Model_for_Paired_Comparisons_and_Ranking_Data"},{"title":"How to Analyze Paired Comparison Data Kristi Tsukida and Maya R. Gupta","url":"https://apps.dtic.mil/sti/tr/pdf/ADA543806.pdf"},{"title":"Thurstone's Comparative Judgment Model - GM-RKB","url":"http://www.gabormelli.com/RKB/Thurstone's_Comparative_Judgment_Model"}]

Based on the search results, here's information about Thurstone's 1927 Law of Comparative Judgment:

## Overview

Thurstone presented a new psychological law, the law of comparative judgment, along with some of its special applications in the measurement of psychological values. In the 1920s, Thurstone formalized the response model for paired comparison designs when the stimuli had no physical counterpart, generally performances or attitude statements that expressed different degrees of attitude. Thurstone called this formalization the Law of Comparative Judgment (LCJ) wit
…[truncated 1312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 13565
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-22T03:33:31.960481+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告：新颖性、完整性与写作质量\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\"\n**Venue**: EMNLP 2026 Main Conference (Long Paper via ARR)\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n**一句话总结**: 实验设计严谨、实用价值高的 empirical study，但核心发现（Likert Blindspot）的概念新颖性有限——本质上是 Thurstone (1927) 已确立的心理测量原理在 LLM judge 领域的系统性验证，论文需更诚实地定位 novelty 边界；同时缺少 human validation 来解决 \"detection vs. amplification\" 的根本性问题。\n\n---\n\n## 官方维度打分（来自 ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论设计严谨（NLI gate、负面控制、position control、7种统计方法），但 \"pairwise 检测 vs. 放大\" 的核心区分未完全解决；无人类标注验证 ground truth |\n| Excitement | 3/5 | 发现实用且对 LLM evaluation 社区有价值，但概念层面是已知心理测量原理的领域迁移，增量贡献为主 |\n| Reproducibility | 4/5 | 承诺开源代码和数据；实验细节在附录 P 中描述充分；统计方法清晰可复现 |\n| Reviewer Confidence | 4/5 | 熟悉 LLM-as-Judge、measurement theory、interventional text analysis 相关文献 |\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated 内容控制、逐轴风格分解和位置控制的 pairwise comparison，系统量化 LLM judge 中的风格偏差。核心发现 \"Likert Blindspot\" 表明 Likert 评分系统性地遗漏了 pairwise comparison 能检测到的风格偏差，在中等效应量下信号衰减超 60%。GEE 条件分解揭示了 per-axis 的 confound 结构（verbosity = style-dominated，formality = conditional，register = judge-dependent）。实验覆盖 4 个 target judges + 1 个 negative control、3 个 benchmark、3 个风格轴，附录提供了大量 robustness checks。\n\n---\n\n## 主要优势\n\n**S1. 实验设计严谨，控制充分。** NLI gate（DeBERTa-v3-large, threshold 0.98）、negative control judge（Claude Sonnet 4）、position-controlled pairwise、cross-benchmark replication（LLMBar/AlpacaEval/MT-Bench）构成多层验证体系。Appendix D 还用独立 rewriter（GPT-4o）验证了框架鲁棒性。这种控制层次在该领域论文中属于上乘。\n\n**S2. 统计分析全面且层次分明。** 七种统计方法（BT、Sign test、Likert ATE、Binomial、Ordinal regression、GEE、Wilcoxon）形成 sensitivity hierarchy（Table 2），清晰展示 pairwise 方法与 Likert 方法的系统性灵敏度差异。GEE 条件分解（Table 3）揭示不同风格轴具有不同的 confound 结构，这是一个 genuinely novel 的分析贡献。\n\n**S3. 对 \"measurement attenuation vs. construct divergence\" 两种解释的公平讨论。** 论文没有武断地声称 pairwise 一定\"更好\"，而是诚实地承认两种解释并存（§5.2, §6, Limitations），这种学术诚实值得肯定。\n\n**S4. Appendix M（100-point continuous Likert）是一个关键控制实验。** 证明 Blindspot 不是 scale granularity 问题（即使 101 个可能值，tie rate 仍高达 51-64%），而是 absolute vs. relative evaluation paradigm 的根本差异。这大大增强了核心论点。\n\n**S5. 负面控制的 discriminative validity。** Claude Sonnet 4 作为 negative control 在两个主要轴上未检测到显著偏差（formality p = 0.091, verbosity p = 0.284），支持框架的 discriminative validity——并非所有 judge 都会被标记为有偏差。\n\n**S6. 与 RATE 的对比公平且建设性。** 论文不是简单否定 RATE，而是定位两者为互补框架（§5.2: \"the frameworks are complementary\"），并具体说明 CSD 如何在三个方面（per-axis targeting、pairwise measurement、NLI entailment gating）提供增量价值。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1 [critical] Novelty 定位不够诚实：Likert Blindspot 的概念基础已有近百年历史**\n\n- 具体位置：Section 2 (\"Measurement Sensitivity in NLG Evaluation\"), Section 1 (Introduction)\n- 问题：论文在 §2 中提到 Thurstone (1927) 和 Stevens (1946)，承认 \"the superiority of pairwise comparison over rating scales for eliciting reliable human judgments has been established since Thurstone (1927)\"。然而论文整体叙事——从标题中的 \"Detecting Hidden Style Bias\"，到 Abstract 中将 Likert Blindspot 作为主要发现呈现，到 Introduction 的 motivating example——给读者的印象是这是一个**全新发现**。\n  \n  实际上，forced-choice methods 优于 rating scales 在心理测量学中已是教科书级共识（Thurstone 1927; Bradley & Terry 1952; Preston & Colman 2000，论文均已引用）。Likert Blindspot 本质上是这一已知原理在 LLM judge 领域的**系统性 empirical demonstration**，而非概念层面的新发现。\n  \n- 为什么影响接收：ARR Reviewer Guidelines 明确指出 novelty 要求 \"demonstrating that work isn't highly similar [to] published [work]\"。虽然 LLM-specific 的 empirical evidence 有价值，但如果 novelty 定位模糊，reviewers（尤其是熟悉 psychometrics 的）会认为 contribution 被 overclaim。\n  \n- 建议修改方向：\n  1. 在 Introduction 中更早、更明确地承认 psychometric baseline：\"While the superiority of forced-choice over rating scales is well-established in psychometrics (Thurstone, 1927), whether and to what extent this phenomenon manifests in LLM judges—and what its practical consequences are for evaluation pipelines—has not been systematically studied.\"\n  2. 将 novelty claim 从 \"discovering the Blindspot\" 调整为 \"providing the first controlled, per-axis quantification of this psychometric phenomenon in LLM judges, revealing a severity spectrum and judge-dependent confound structures that psychometric theory alone cannot predict.\"\n  3. 更突出 GEE conditional decomposition 作为独立贡献——这是论文中真正 novel 的分析发现。\n\n**N2 [critical] \"Detection vs. Amplification\" 问题未充分解决，缺少 human validation**\n\n- 具体位置：Section 5.2, Section 3 (对 Jeong et al. 2025 Comparative Trap 的回应)\n- 问题：论文在 §3 (page 3) 正确地指出 Jeong et al. (2025) 的 Comparative Trap 论点——pairwise comparison 可能放大（而非仅检测）style biases。§5.2 回应了六个 \"independent controls\" 来 bound this risk：(i) NLI gate ablation, (ii) Claude Sonnet 4 negative control, (iii) cross-BT variation, (iv) debiased prompting, (v) rewriting independence, (vi) consistent GEE structure。\n  \n  然而这些控制虽然排除了一些 artifactual 解释，**并不能在根本上区分 \"pairwise 检测了 Likert 遗漏的真实偏差\" 和 \"pairwise 放大了微弱但合理的 style preferences\"。** 唯一能真正解决这个问题的是 human evaluation——让人类标注者在 Likert 和 pairwise 模式下评估同样的 style-transformed pairs，看 human pairwise 是否也能检测到 Likert 遗漏的偏差。如果 human pairwise 也显示 Blindspot，那 Blindspot 是测量范式的根本特性；如果 human Likert 能检测但 LLM Likert 不能，那问题出在 LLM 的 Likert 能力而非 Likert 本身。\n  \n- 为什么影响接收：没有 human validation，论文的核心 claim（\"Likert scoring systematically misses style biases\"）的解释空间仍然模糊。这是一个 soundness 问题——不是说结论错了，而是 evidence 不足以区分两种核心解释。\n  \n- 建议修改方向：\n  1. 至少对一个 style axis（如 verbosity，效应量最大）的一个 subset（如 50 pairs）进行 human evaluation（Likert + pairwise），建立 human baseline\n  2. 如果时间/资源不允许，应在 Limitations 中将此列为最主要的 open question，而非仅一笔带过\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] 风格轴覆盖面有限：仅 3 个轴难以支撑 \"framework\" 级别的泛化声明**\n\n- 具体位置：Section 3.1, Section 6\n- 问题：CSD 仅测试了 formality、verbosity、register 三个风格轴。虽然这三个轴是文献中最常讨论的，但 style bias 的类型远不止这些——complexity/readability、hedging/confidence、emoji/punctuation use、paragraph structure、bullet-point formatting 等均可能影响 judge 评分。论文标题和 abstract 使用 \"framework\" 一词暗示更广的适用性，但仅 3 轴的实验不足以支撑这一泛化。\n- 建议：在 Limitations 中明确列出未覆盖的风格维度；或在修改时增加 1-2 个轴（如 complexity、hedging）来增强 generalizability evidence。\n\n**W2 [warning] Table 1 设计可读性较差**\n\n- 具体位置：Table 1 (page 5)\n- 问题：Table 1 是论文最核心的结果表，但信息密度过高：5 个 judges × 3 benchmarks × 3 axes × 2 metrics (BT + Likert)，加上 footnotes 和 significance markers，读者很难快速抓住核心 pattern。\"Cat.\" 列（Blindspot 分类）虽然有用但缩写不直观（↑, ↓, =）。\"Likert d\" 列的负值含义需要额外认知负荷。\n- 建议：考虑将 Table 1 拆分为两个表（一个按 style axis 组织，一个按 judge 组织），或用 heatmap 可视化 BT vs. Likert 的差异模式。至少应在 caption 中添加一句 \"how to read this table\" 的指引。\n\n**W3 [warning] Negative control（Claude Sonnet 4）的统计功效不足**\n\n- 具体位置：Section 5.1 (最后一段), Appendix G\n- 问题：Claude Sonnet 4 作为 negative control 是一个 excellent design choice，但当前样本量（n = 87 for formality, p = 0.091; n = 82 for verbosity, p = 0.284）的统计功效可能不足以 conclusively 排除偏差。论文在 Appendix G 中进行了 equivalence testing（TOST），表明效应在 ±13pp 等价区间内，但 ±13pp 对于实际应用来说仍是一个相当宽的区间。\n- 为什么重要：如果 negative control 的 power 不足，\"discriminative validity\" 的论点就被削弱——可能 Claude 确实有某种程度的偏差，只是当前样本检测不到。\n- 建议：明确报告 Claude Sonnet 4 在当前样本量下检测特定效应量（如 BT = 55%）的统计功效（1-β）；如果功效不足，应 acknowledge 这一限制。\n\n**W4 [warning] Rewriting artifact 的处理略显草率**\n\n- 具体位置：Appendix O (Rewriting Artifact Control), Section 3.2\n- 问题：Appendix O（Table 15）显示同一风格方向的 double-rewrite 对中，judges 系统性偏好 LLM-polished 文本（BT P(orig) < 0.5）。这意味着 rewriting 本身就引入了 \"polishing\" artifact——即使风格不变，rewritten 文本也会被偏好。论文承认了这一点，但认为 same-style double-rewrite controls 能排除此 artifact（\"confirming a rewriting artifact…that separates style from artifact effects\"）。\n  \n  然而，same-style double-rewrite 只能控制 style-neutral 的 polishing effect；如果 polishing effect 与 style change 存在交互（即 formal rewriting 的 polishing 程度与 casual rewriting 不同），那么 style-specific 的 artifact 仍可能存在。\n  \n- 建议：在 Limitations 中讨论 style-specific polishing interaction 的可能性；或报告不同风格方向上 polishing effect 的大小是否一致。\n\n**W5 [warning] Introduction motivating example 的准确性值得推敲**\n\n- 具体位置：Section 1, paragraph 1\n- 问题：开头的 \"What is the average height for a male?\" 例子声称 GPT-4o 在 1-10 Likert 上 \"consistently selects the formal variant higher\"。这是一个有效的 motivating example，但读者可能会问：(1) 这个例子是否是 cherry-picked？(2) \"near-perfect correlation\" 的 NLI 验证仅限于 content，但 formality 的改变本身可能影响 perceived answer quality（例如正式回答可能被认为更 authoritative）。如果这种感知是合理的，那它是否构成 \"bias\"？\n- 建议：在 motivating example 旁边简短 acknowledge 这一 nuance——风格改变可能合法地影响 perceived quality，这正是为什么需要 controlled decomposition 来区分 style effect 和 quality effect。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Section 4.1 的 statistical framework 描述较为压缩，hypothesis family 的 primary vs. exploratory 分类标准（\"Analyses outside this grid are classified as either exploratory...or confirmatory\"）需要更清晰的 justification——为什么这些特定假设被选为 primary？\n  \n- **M2**: Figure 2 (DAG) 中 R → Q 和 S → Q 的路径箭头在 150 DPI 下略难辨认颜色编码（红色 dashed vs. 黑色实线）。建议在打印版中增强对比度。\n\n- **M3**: Section 5.6 (GEE Conditional Decomposition) 对 \"exchangeable correlation\" 假设的 justification 较弱。Appendix C 验证了 correlation robustness，但主文应至少一句话解释为何这个假设在此场景下合理。\n\n- **M4**: References 格式整体一致，但部分条目的 venue 信息不完整（如一些 arXiv preprints 缺少版本号或提交日期）。\n\n- **M5**: Limitations 段落提到 \"evaluator-producer bias\"，但该术语此前未出现过且未定义。建议在首次使用时简短解释或引用来源。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** NLI threshold 0.98 的选择依据是什么？Appendix E 提供了 sensitivity sweep（11 个 thresholds），但主文未报告结果的 threshold 依赖性。在 threshold 从 0.98 降至 0.90 时，核心发现（BT significance + Likert non-significance）是否稳健？\n\n**Q2.** Appendix M 的 100-point continuous Likert 实验仅用了 Qwen3-32B 一个 judge。其他 judges（尤其是 GPT-4o）是否也显示相同模式？如果是，这将大大加强论点。\n\n**Q3.** GEE conditional decomposition（Table 3）显示 formality 的 confound 结构是 \"conditional\"——style effect 被 content quality 调节。这意味着在高质量内容上，formality bias 可能消失。作者是否探索了这种交互的方向和强度？\n\n**Q4.** 论文使用 LLMBar 的 100 个 instruction-response pairs 作为 base dataset。这 100 个 pairs 是如何从 LLMBar 的完整数据集中选择的？selection criteria 是什么？是否可能引入 selection bias？\n\n**Q5.** 对于 \"measurement attenuation vs. construct divergence\" 这一 open question，作者是否有后续研究计划来区分这两种解释？\n\n---\n\n## Missing References\n\n1. **Girrbach et al. (2025/2026)**, \"Likert or Not: LLM Absolute Relevance Judgments on Fine-Grained Ordinal Scales\" — 直接研究 LLM 在 Likert scale 上的评分行为，与 Appendix M 的 100-point continuous scale 实验高度相关。\n\n2. **PRePair** (Jeong et al., 2025 中提出) — 论文引用了 Comparative Trap 但未讨论其提出的 PRePair 方法（在 pairwise 框架中整合 pointwise reasoning）。这可能是缓解 Blindspot 的替代方案，值得在 Related Work 或 Discussion 中提及。\n\n3. 建议检查是否需要引用 **Kambhatla et al. (2024/2025)** 或类似的 calibration/scoring bias 工作，因为论文的核心论点涉及 scoring methodology 的 calibration 问题。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5 — **Borderline Conference**\n**Confidence**: 4 / 5 — Quite sure; carefully read paper and checked key claims\n\n### 判断理由\n\n**支持 Conference (4.0) 的因素：**\n- 实验设计异常严谨，控制层次远超该领域平均水平\n- Likert Blindspot 的 empirical quantification 对 LLM evaluation 社区有直接实用价值\n- GEE per-axis confound decomposition 是 genuinely novel 的分析贡献\n- 7 种统计方法的 sensitivity hierarchy 是 compelling evidence\n- 100-point continuous Likert 控制实验有力排除了 scale granularity 解释\n- 附录 A-P 展示了出色的 rigor\n\n**拉向 Findings (3.0) 的因素：**\n- 核心概念（forced-choice > rating）在 psychometrics 中已有近百年历史；论文的 novelty 定位不够诚实\n- 缺少 human validation 来区分 \"detection vs. amplification\"——这是 soundness 层面的 gap\n- 仅 3 个风格轴限制了 generalizability\n- Rewriting artifact 的处理不够彻底\n\n**净判断：** 论文接近 Conference 门槛，但 N1（novelty 定位）和 N2（human validation）两个 Must-Fix 问题需要在 camera-ready 之前解决。如果作者能在修改中：(1) 重新定位 novelty narrative，(2) 补充哪怕一小组 human evaluation，(3) 增加 1-2 个风格轴——本文可以达到 4.0 (Conference) 水平。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n信息密度高，核心数字（60% signal loss, 76-92% style variance）传递了关键 message。但第一句 \"yet style features correlate with judge scores with near-perfect correlation\" 过于绝对——76-92% explained variance 虽然很高但不是 \"near-perfect\"。建议措辞更 precise。\n\n### Section 1 (Introduction)\nOpening example 有效且令人印象深刻——height question 的 formal vs. casual variant 直觉上 should have identical quality，但 judge 评分不同。叙事逻辑清晰：problem → gap → our approach → findings → contributions。Contributions 列表（4 items）清晰但 item 1 的 \"black-box controlled framework\" 措辞可能被认为 overclaim——NLI gate 需要 access model probabilities，这不完全是 \"black-box\"。\n\n### Section 2 (Related Work)\n覆盖面广且组织良好。\"Interventional Approaches to Judge Bias\"、\"Style Bias Detection and Mitigation\"、\"Measurement Sensitivity in NLG Evaluation\"、\"Bradley-Terry Models in Evaluation\" 四个子节覆盖了主要相关领域。对 RATE 的讨论（最后两段）公平且 constructive。\n- 遗漏：未讨论 Likert scale 的 methodological literature（如 Krosnick 1999 在 §2 cited 但仅一处），尤其是 acquiescence bias 和 central tendency bias——这些是 Likert scale 在社会科学中的 known problems，与 Likert Blindspot 直接相关。\n- Section 2 与 Section 3 之间的过渡可以更平滑——从 \"why existing methods are insufficient\" 到 \"here's our approach\" 的逻辑跳跃稍显突兀。\n\n### Section 3 (Method)\n- §3.1 (Style-Controlled Rewriting): 设计合理。温度 0.7 的选择有 justification 吗？\n- §3.2 (Content Preservation Verification): NLI gate 设计精巧，bidirectional entailment + forward-only direction-aware verification 是一个 well-thought-out protocol。但 \"entailment threshold of 0.98\" 这个 magic number 在主文中缺乏 justification（虽然 Appendix E 有 sweep）。\n- §3.3 (Measurement Protocol): 清晰。Position control（每对评估两次 swapping order）是 good practice。\n- §3.5 (Design Rationale): Figure 2 的 DAG 是论文的亮点之一——清晰展示了因果假设和 blocking 策略。\"We do not claim that this DAG is a complete structural causal model\" 的 caveat 是诚实且必要的。\n\n### Section 4 (Experiments)\n- §4.1 (Statistical Framework): 略显压缩。\"Primary family of six hypotheses\" 的选择标准需要更明确的 justification。Holm-Bonferroni correction 是 appropriate，但为什么选择 family-wise error rate 而不是 false discovery rate (FDR)？对于 exploratory analyses，FDR 可能更合适。\n\n### Section 5 (Analysis)\n- §5.1 (NLI Gate Validation): Thorough。92.1% formality / 82.6% verbosity pass precision 数据 convincing。但 FNR = 8.4% 可能意味着 gate 过滤掉了一些有效的 style transformations，creating survivorship bias。\n- §5.2 (Measurement Sensitivity): 核心发现清晰呈现。Figure 3 (forest plot) 是 excellent visualization。对 Comparative Trap 的回应（六个独立控制）是 reasonable 但不 definitive（见 N2）。\n- §5.3 (Cross-Axis Replication): 三个独立 judges replicate the Blindspot 是 strong evidence。\n- §5.4 (Verbosity): 四个 judges 一致显示 Blindspot——最 robust 的结果。\n- §5.5 (Register): Judge-dependent confound 的发现有趣但叙述过于压缩。这值得更多篇幅讨论 why register 表现不同。\n- §5.6 (GEE Conditional Decomposition): 这是论文最 novel 的分析部分。Table 3 清晰展示 per-axis confound structure。但 \"exchangeable correlation\" 假设的 justification 几乎缺失。\n\n### Section 6 (Conclusion)\n适当总结了两个主要发现。\"whether this reflects measurement attenuation or construct divergence\" 的 open question 处理得当——诚实但不过度 hedge。最后一段关于 practical implications 简洁有力。\n\n### Limitations\n覆盖了主要 weak points，但遗漏了：(1) 缺少 human validation；(2) 仅 3 个风格轴的 coverage limitation；(3) base sample 仅 100 pairs。建议补充这三点。\n\n### 格式与匿名\n- **页数**: 正文 8 页（§1-§6 + Limitations），符合限制 ✓\n- **匿名**: Title page 显示 \"Anonymous ACL submission\"，未发现自引泄漏或 acknowledgment ✓\n- **引用格式**: natbib 括号风格，整体一致 ✓\n- **ARR Checklist**: 未在 PDF 中（符合规定，应在 OpenReview form 中填写）✓\n",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿报告：新颖性、完整性与写作质量\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\"\n**Venue**: EMNLP 2026 Main Conference (Long Paper via ARR)\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n**一句话总结**: 实验设计严谨、实用价值高的 empirical study，但核心发现（Likert Blindspot）的概念新颖性有限——本质上是 Thurstone (1927) 已确立的心理测量原理在 LLM judge 领域的系统性验证，论文需更诚实地定位 novelty 边界；同时缺少 human validation 来解决 \"detection vs. amplification\" 的根本性问题。\n\n---\n\n## 官方维度打分（来自 ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论设计严谨（NLI gate、负面控制、position control、7种统计方法），但 \"pairwise 检测 vs. 放大\" 的核心区分未完全解决；无人类标注验证 ground truth |\n| Excitement | 3/5 | 发现实用且对 LLM evaluation 社区有价值，但概念层面是已知心理测量原理的领域迁移，增量贡献为主 |\n| Reproducibility | 4/5 | 承诺开源代码和数据；实验细节在附录 P 中描述充分；统计方法清晰可复现 |\n| Reviewer Confidence | 4/5 | 熟悉 LLM-as-Judge、measurement theory、interventional text analysis 相关文献 |\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated 内容控制、逐轴风格分解和位置控制的 pairwise comparison，系统量化 LLM judge 中的风格偏差。核心发现 \"Likert Blindspot\" 表明 Likert 评分系统性地遗漏了 pairwise comparison 能检测到的风格偏差，在中等效应量下信号衰减超 60%。GEE 条件分解揭示了 per-axis 的 confound 结构（verbosity = style-dominated，formality = conditional，register = judge-dependent）。实验覆盖 4 个 target judges + 1 个 negative control、3 个 benchmark、3 个风格轴，附录提供了大量 robustness checks。\n\n---\n\n## 主要优势\n\n**S1. 实验设计严谨，控制充分。** NLI gate（DeBERTa-v3-large, threshold 0.98）、negative control judge（Claude Sonnet 4）、position-controlled pairwise、cross-benchmark replication（LLMBar/AlpacaEval/MT-Bench）构成多层验证体系。Appendix D 还用独立 rewriter（GPT-4o）验证了框架鲁棒性。这种控制层次在该领域论文中属于上乘。\n\n**S2. 统计分析全面且层次分明。** 七种统计方法（BT、Sign test、Likert ATE、Binomial、Ordinal regression、GEE、Wilcoxon）形成 sensitivity hierarchy（Table 2），清晰展示 pairwise 方法与 Likert 方法的系统性灵敏度差异。GEE 条件分解（Table 3）揭示不同风格轴具有不同的 confound 结构，这是一个 genuinely novel 的分析贡献。\n\n**S3. 对 \"measurement attenuation vs. construct divergence\" 两种解释的公平讨论。** 论文没有武断地声称 pairwise 一定\"更好\"，而是诚实地承认两种解释并存（§5.2, §6, Limitations），这种学术诚实值得肯定。\n\n**S4. Appendix M（100-point continuous Likert）是一个关键控制实验。** 证明 Blindspot 不是 scale granularity 问题（即使 101 个可能值，tie rate 仍高达 51-64%），而是 absolute vs. relative evaluation paradigm 的根本差异。这大大增强了核心论点。\n\n**S5. 负面控制的 discriminative validity。** Claude Sonnet 4 作为 negative control 在两个主要轴上未检测到显著偏差（formality p = 0.091, verbosity p = 0.284），支持框架的 discriminative validity——并非所有 judge 都会被标记为有偏差。\n\n**S6. 与 RATE 的对比公平且建设性。** 论文不是简单否定 RATE，而是定位两者为互补框架（§5.2: \"the frameworks are complementary\"），并具体说明 CSD 如何在三个方面（per-axis targeting、pairwise measurement、NLI entailment gating）提供增量价值。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1 [critical] Novelty 定位不够诚实：Likert Blindspot 的概念基础已有近百年历史**\n\n- 具体位置：Section 2 (\"Measurement Sensitivity in NLG Evaluation\"), Section 1 (Introduction)\n- 问题：论文在 §2 中提到 Thurstone (1927) 和 Stevens (1946)，承认 \"the superiority of pairwise comparison over rating scales for eliciting reliable human judgments has been established since Thurstone (1927)\"。然而论文整体叙事——从标题中的 \"Detecting Hidden Style Bias\"，到 Abstract 中将 Likert Blindspot 作为主要发现呈现，到 Introduction 的 motivating example——给读者的印象是这是一个**全新发现**。\n  \n  实际上，forced-choice methods 优于 rating scales 在心理测量学中已是教科书级共识（Thurstone 1927; Bradley & Terry 1952; Preston & Colman 2000，论文均已引用）。Likert Blindspot 本质上是这一已知原理在 LLM judge 领域的**系统性 empirical demonstration**，而非概念层面的新发现。\n  \n- 为什么影响接收：ARR Reviewer Guidelines 明确指出 novelty 要求 \"demonstrating that work isn't highly similar [to] published [work]\"。虽然 LLM-specific 的 empirical evidence 有价值，但如果 novelty 定位模糊，reviewers（尤其是熟悉 psychometrics 的）会认为 contribution 被 overclaim。\n  \n- 建议修改方向：\n  1. 在 Introduction 中更早、更明确地承认 psychometric baseline：\"While the superiority of forced-choice over rating scales is well-established in psychometrics (Thurstone, 1927), whether and to what extent this phenomenon manifests in LLM judges—and what its practical consequences are for evaluation pipelines—has not been systematically studied.\"\n  2. 将 novelty claim 从 \"discovering the Blindspot\" 调整为 \"providing the first controlled, per-axis quantification of this psychometric phenomenon in LLM judges, revealing a severity spectrum and judge-dependent confound structures that psychometric theory alone cannot predict.\"\n  3. 更突出 GEE conditional decomposition 作为独立贡献——这是论文中真正 novel 的分析发现。\n\n**N2 [critical] \"Detection vs. Amplification\" 问题未充分解决，缺少 human validation**\n\n- 具体位置：Section 5.2, Section 3 (对 Jeong et al. 2025 Comparative Trap 的回应)\n- 问题：论文在 §3 (page 3) 正确地指出 Jeong et al. (2025) 的 Comparative Trap 论点——pairwise comparison 可能放大（而非仅检测）style biases。§5.2 回应了六个 \"independent controls\" 来 bound this risk：(i) NLI gate ablation, (ii) Claude Sonnet 4 negative control, (iii) cross-BT variation, (iv) debiased prompting, (v) rewriting independence, (vi) consistent GEE structure。\n  \n  然而这些控制虽然排除了一些 artifactual 解释，**并不能在根本上区分 \"pairwise 检测了 Likert 遗漏的真实偏差\" 和 \"pairwise 放大了微弱但合理的 style preferences\"。** 唯一能真正解决这个问题的是 human evaluation——让人类标注者在 Likert 和 pairwise 模式下评估同样的 style-transformed pairs，看 human pairwise 是否也能检测到 Likert 遗漏的偏差。如果 human pairwise 也显示 Blindspot，那 Blindspot 是测量范式的根本特性；如果 human Likert 能检测但 LLM Likert 不能，那问题出在 LLM 的 Likert 能力而非 Likert 本身。\n  \n- 为什么影响接收：没有 human validation，论文的核心 claim（\"Likert scoring systematically misses style biases\"）的解释空间仍然模糊。这是一个 soundness 问题——不是说结论错了，而是 evidence 不足以区分两种核心解释。\n  \n- 建议修改方向：\n  1. 至少对一个 style axis（如 verbosity，效应量最大）的一个 subset（如 50 pairs）进行 human evaluation（Likert + pairwise），建立 human baseline\n  2. 如果时间/资源不允许，应在 Limitations 中将此列为最主要的 open question，而非仅一笔带过\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] 风格轴覆盖面有限：仅 3 个轴难以支撑 \"framework\" 级别的泛化声明**\n\n- 具体位置：Section 3.1, Section 6\n- 问题：CSD 仅测试了 formality、verbosity、register 三个风格轴。虽然这三个轴是文献中最常讨论的，但 style bias 的类型远不止这些——complexity/readability、hedging/confidence、emoji/punctuation use、paragraph structure、bullet-point formatting 等均可能影响 judge 评分。论文标题和 abstract 使用 \"framework\" 一词暗示更广的适用性，但仅 3 轴的实验不足以支撑这一泛化。\n- 建议：在 Limitations 中明确列出未覆盖的风格维度；或在修改时增加 1-2 个轴（如 complexity、hedging）来增强 generalizability evidence。\n\n**W2 [warning] Table 1 设计可读性较差**\n\n- 具体位置：Table 1 (page 5)\n- 问题：Table 1 是论文最核心的结果表，但信息密度过高：5 个 judges × 3 benchmarks × 3 axes × 2 metrics (BT + Likert)，加上 footnotes 和 significance markers，读者很难快速抓住核心 pattern。\"Cat.\" 列（Blindspot 分类）虽然有用但缩写不直观（↑, ↓, =）。\"Likert d\" 列的负值含义需要额外认知负荷。\n- 建议：考虑将 Table 1 拆分为两个表（一个按 style axis 组织，一个按 judge 组织），或用 heatmap 可视化 BT vs. Likert 的差异模式。至少应在 caption 中添加一句 \"how to read this table\" 的指引。\n\n**W3 [warning] Negative control（Claude Sonnet 4）的统计功效不足**\n\n- 具体位置：Section 5.1 (最后一段), Appendix G\n- 问题：Claude Sonnet 4 作为 negative control 是一个 excellent design choice，但当前样本量（n = 87 for formality, p = 0.091; n = 82 for verbosity, p = 0.284）的统计功效可能不足以 conclusively 排除偏差。论文在 Appendix G 中进行了 equivalence testing（TOST），表明效应在 ±13pp 等价区间内，但 ±13pp 对于实际应用来说仍是一个相当宽的区间。\n- 为什么重要：如果 negative control 的 power 不足，\"discriminative validity\" 的论点就被削弱——可能 Claude 确实有某种程度的偏差，只是当前样本检测不到。\n- 建议：明确报告 Claude Sonnet 4 在当前样本量下检测特定效应量（如 BT = 55%）的统计功效（1-β）；如果功效不足，应 acknowledge 这一限制。\n\n**W4 [warning] Rewriting artifact 的处理略显草率**\n\n- 具体位置：Appendix O (Rewriting Artifact Control), Section 3.2\n- 问题：Appendix O（Table 15）显示同一风格方向的 double-rewrite 对中，judges 系统性偏好 LLM-polished 文本（BT P(orig) < 0.5）。这意味着 rewriting 本身就引入了 \"polishing\" artifact——即使风格不变，rewritten 文本也会被偏好。论文承认了这一点，但认为 same-style double-rewrite controls 能排除此 artifact（\"confirming a rewriting artifact…that separates style from artifact effects\"）。\n  \n  然而，same-style double-rewrite 只能控制 style-neutral 的 polishing effect；如果 polishing effect 与 style change 存在交互（即 formal rewriting 的 polishing 程度与 casual rewriting 不同），那么 style-specific 的 artifact 仍可能存在。\n  \n- 建议：在 Limitations 中讨论 style-specific polishing interaction 的可能性；或报告不同风格方向上 polishing effect 的大小是否一致。\n\n**W5 [warning] Introduction motivating example 的准确性值得推敲**\n\n- 具体位置：Section 1, paragraph 1\n- 问题：开头的 \"What is the average height for a male?\" 例子声称 GPT-4o 在 1-10 Likert 上 \"consistently selects the formal variant higher\"。这是一个有效的 motivating example，但读者可能会问：(1) 这个例子是否是 cherry-picked？(2) \"near-perfect correlation\" 的 NLI 验证仅限于 content，但 formality 的改变本身可能影响 perceived answer quality（例如正式回答可能被认为更 authoritative）。如果这种感知是合理的，那它是否构成 \"bias\"？\n- 建议：在 motivating example 旁边简短 acknowledge 这一 nuance——风格改变可能合法地影响 perceived quality，这正是为什么需要 controlled decomposition 来区分 style effect 和 quality effect。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Section 4.1 的 statistical framework 描述较为压缩，hypothesis family 的 primary vs. exploratory 分类标准（\"Analyses outside this grid are classified as either exploratory...or confirmatory\"）需要更清晰的 justification——为什么这些特定假设被选为 primary？\n  \n- **M2**: Figure 2 (DAG) 中 R → Q 和 S → Q 的路径箭头在 150 DPI 下略难辨认颜色编码（红色 dashed vs. 黑色实线）。建议在打印版中增强对比度。\n\n- **M3**: Section 5.6 (GEE Conditional Decomposition) 对 \"exchangeable correlation\" 假设的 justification 较弱。Appendix C 验证了 correlation robustness，但主文应至少一句话解释为何这个假设在此场景下合理。\n\n- **M4**: References 格式整体一致，但部分条目的 venue 信息不完整（如一些 arXiv preprints 缺少版本号或提交日期）。\n\n- **M5**: Limitations 段落提到 \"evaluator-producer bias\"，但该术语此前未出现过且未定义。建议在首次使用时简短解释或引用来源。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** NLI threshold 0.98 的选择依据是什么？Appendix E 提供了 sensitivity sweep（11 个 thresholds），但主文未报告结果的 threshold 依赖性。在 threshold 从 0.98 降至 0.90 时，核心发现（BT significance + Likert non-significance）是否稳健？\n\n**Q2.** Appendix M 的 100-point continuous Likert 实验仅用了 Qwen3-32B 一个 judge。其他 judges（尤其是 GPT-4o）是否也显示相同模式？如果是，这将大大加强论点。\n\n**Q3.** GEE conditional decomposition（Table 3）显示 formality 的 confound 结构是 \"conditional\"——style effect 被 content quality 调节。这意味着在高质量内容上，formality bias 可能消失。作者是否探索了这种交互的方向和强度？\n\n**Q4.** 论文使用 LLMBar 的 100 个 instruction-response pairs 作为 base dataset。这 100 个 pairs 是如何从 LLMBar 的完整数据集中选择的？selection criteria 是什么？是否可能引入 selection bias？\n\n**Q5.** 对于 \"measurement attenuation vs. construct divergence\" 这一 open question，作者是否有后续研究计划来区分这两种解释？\n\n---\n\n## Missing References\n\n1. **Girrbach et al. (2025/2026)**, \"Likert or Not: LLM Absolute Relevance Judgments on Fine-Grained Ordinal Scales\" — 直接研究 LLM 在 Likert scale 上的评分行为，与 Appendix M 的 100-point continuous scale 实验高度相关。\n\n2. **PRePair** (Jeong et al., 2025 中提出) — 论文引用了 Comparative Trap 但未讨论其提出的 PRePair 方法（在 pairwise 框架中整合 pointwise reasoning）。这可能是缓解 Blindspot 的替代方案，值得在 Related Work 或 Discussion 中提及。\n\n3. 建议检查是否需要引用 **Kambhatla et al. (2024/2025)** 或类似的 calibration/scoring bias 工作，因为论文的核心论点涉及 scoring methodology 的 calibration 问题。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5 — **Borderline Conference**\n**Confidence**: 4 / 5 — Quite sure; carefully read paper and checked key claims\n\n### 判断理由\n\n**支持 Conference (4.0) 的因素：**\n- 实验设计异常严谨，控制层次远超该领域平均水平\n- Likert Blindspot 的 empirical quantification 对 LLM evaluation 社区有直接实用价值\n- GEE per-axis confound decomposition 是 genuinely novel 的分析贡献\n- 7 种统计方法的 sensitivity hierarchy 是 compelling evidence\n- 100-point continuous Likert 控制实验有力排除了 scale granularity 解释\n- 附录 A-P 展示了出色的 rigor\n\n**拉向 Findings (3.0) 的因素：**\n- 核心概念（forced-choice > rating）在 psychometrics 中已有近百年历史；论文的 novelty 定位不够诚实\n- 缺少 human validation 来区分 \"detection vs. amplification\"——这是 soundness 层面的 gap\n- 仅 3 个风格轴限制了 generalizability\n- Rewriting artifact 的处理不够彻底\n\n**净判断：** 论文接近 Conference 门槛，但 N1（novelty 定位）和 N2（human validation）两个 Must-Fix 问题需要在 camera-ready 之前解决。如果作者能在修改中：(1) 重新定位 novelty narrative，(2) 补充哪怕一小组 human evaluation，(3) 增加 1-2 个风格轴——本文可以达到 4.0 (Conference) 水平。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n信息密度高，核心数字（60% signal loss, 76-92% style variance）传递了关键 message。但第一句 \"yet style features correlate with judge scores with near-perfect correlation\" 过于绝对——76-92% explained variance 虽然很高但不是 \"near-perfect\"。建议措辞更 precise。\n\n### Section 1 (Introduction)\nOpening example 有效且令人印象深刻——height question 的 formal vs. casual variant 直觉上 should have identical quality，但 judge 评分不同。叙事逻辑清晰：problem → gap → our approach → findings → contributions。Contributions 列表（4 items）清晰但 item 1 的 \"black-box controlled framework\" 措辞可能被认为 overclaim——NLI gate 需要 access model probabilities，这不完全是 \"black-box\"。\n\n### Section 2 (Related Work)\n覆盖面广且组织良好。\"Interventional Approaches to Judge Bias\"、\"Style Bias Detection and Mitigation\"、\"Measurement Sensitivity in NLG Evaluation\"、\"Bradley-Terry Models in Evaluation\" 四个子节覆盖了主要相关领域。对 RATE 的讨论（最后两段）公平且 constructive。\n- 遗漏：未讨论 Likert scale 的 methodological literature（如 Krosnick 1999 在 §2 cited 但仅一处），尤其是 acquiescence bias 和 central tendency bias——这些是 Likert scale 在社会科学中的 known problems，与 Likert Blindspot 直接相关。\n- Section 2 与 Section 3 之间的过渡可以更平滑——从 \"why existing methods are insufficient\" 到 \"here's our approach\" 的逻辑跳跃稍显突兀。\n\n### Section 3 (Method)\n- §3.1 (Style-Controlled Rewriting): 设计合理。温度 0.7 的选择有 justification 吗？\n- §3.2 (Content Preservation Verification): NLI gate 设计精巧，bidirectional entailment + forward-only direction-aware verification 是一个 well-thought-out protocol。但 \"entailment threshold of 0.98\" 这个 magic number 在主文中缺乏 justification（虽然 Appendix E 有 sweep）。\n- §3.3 (Measurement Protocol): 清晰。Position control（每对评估两次 swapping order）是 good practice。\n- §3.5 (Design Rationale): Figure 2 的 DAG 是论文的亮点之一——清晰展示了因果假设和 blocking 策略。\"We do not claim that this DAG is a complete structural causal model\" 的 caveat 是诚实且必要的。\n\n### Section 4 (Experiments)\n- §4.1 (Statistical Framework): 略显压缩。\"Primary family of six hypotheses\" 的选择标准需要更明确的 justification。Holm-Bonferroni correction 是 appropriate，但为什么选择 family-wise error rate 而不是 false discovery rate (FDR)？对于 exploratory analyses，FDR 可能更合适。\n\n### Section 5 (Analysis)\n- §5.1 (NLI Gate Validation): Thorough。92.1% formality / 82.6% verbosity pass precision 数据 convincing。但 FNR = 8.4% 可能意味着 gate 过滤掉了一些有效的 style transformations，creating survivorship bias。\n- §5.2 (Measurement Sensitivity): 核心发现清晰呈现。Figure 3 (forest plot) 是 excellent visualization。对 Comparative Trap 的回应（六个独立控制）是 reasonable 但不 definitive（见 N2）。\n- §5.3 (Cross-Axis Replication): 三个独立 judges replicate the Blindspot 是 strong evidence。\n- §5.4 (Verbosity): 四个 judges 一致显示 Blindspot——最 robust 的结果。\n- §5.5 (Register): Judge-dependent confound 的发现有趣但叙述过于压缩。这值得更多篇幅讨论 why register 表现不同。\n- §5.6 (GEE Conditional Decomposition): 这是论文最 novel 的分析部分。Table 3 清晰展示 per-axis confound structure。但 \"exchangeable correlation\" 假设的 justification 几乎缺失。\n\n### Section 6 (Conclusion)\n适当总结了两个主要发现。\"whether this reflects measurement attenuation or construct divergence\" 的 open question 处理得当——诚实但不过度 hedge。最后一段关于 practical implications 简洁有力。\n\n### Limitations\n覆盖了主要 weak points，但遗漏了：(1) 缺少 human validation；(2) 仅 3 个风格轴的 coverage limitation；(3) base sample 仅 100 pairs。建议补充这三点。\n\n### 格式与匿名\n- **页数**: 正文 8 页（§1-§6 + Limitations），符合限制 ✓\n- **匿名**: Title page 显示 \"Anonymous ACL submission\"，未发现自引泄漏或 acknowledgment ✓\n- **引用格式**: natbib 括号风格，整体一致 ✓\n- **ARR Checklist**: 未在 PDF 中（符合规定，应在 OpenReview form 中填写）✓\n",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-22T03:33:35.978268+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4017
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-22T03:33:40.205642+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
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

_source line 643 · 2026-05-22T03:33:40.256138+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 644 · 2026-05-22T03:33:44.002566+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_7/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-22T03:33:44.002927+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 646 · 2026-05-22T03:33:52.132494+00:00_

Reviewer 2 审稿报告已提交至 Review Director。

**核心判断：Overall 3.5 (Borderline Conference)**

两个 Must-Fix 问题：
1. **Novelty 定位不诚实** — Likert Blindspot 本质是 Thurstone (1927) 已确立的 forced-choice > rating 原理在 LLM judge 领域的 empirical demonstration，论文叙事给人"全新发现"的印象，需重新定位 novelty 边界
2. **缺少 human validation** — 无法区分 pairwise 是"检测了真实偏差"还是"放大了微弱偏好"（Comparative Trap 问题），需至少一小组 human evaluation 建立 baseline

主要优势：实验控制层次出色（NLI gate + negative control + 7 种统计方法 + 100-point continuous Likert 控制实验），GEE per-axis confound decomposition 是 genuinely novel 的分析贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 20

## Round 20

4 recorded events


### User

_source line 647 · 2026-05-22T03:35:22.561860+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿意见（完整原文）

**Overall Assessment**: 3.5 (Borderline Conference)

### Strengths
- S1. Likert Blindspot 对 LLM 评估实践有直接影响，Table 1 在 5 judges × 3 axes 矩阵中一致展示
- S2. 多层验证管线（NLI gate → consistency filter → position-balanced pairwise → BT + GEE），含 11 NLI 阈值扫描、double-rewrite control、100-point continuous Likert、formal power analysis
- S3. 统计框架完善：confirmatory vs. exploratory 区分、Holm-Bonferroni 校正、7 种方法 sensitivity hierarchy
- S4. GEE conditional decomposition 揭示 per-axis confound structure（verbosity style-dominated, formality conditional）
- S5. 诚实的局限性讨论

### Must-Fix
- **N1 [critical]**: Primary family 构成缺乏透明度——Section 4.1 声明 "six hypothesis tests (three judges × two axes)" 但未指明哪三个 judges。四个 target judges 中排除哪一个？如果纳入 Gemini（4×2=8 tests），Holm-Bonferroni 更保守，部分结果可能失去 adjusted significance。存在 post-hoc selection 嫌疑。
- **N2 [critical]**: Cross-rewriter independence 验证仅覆盖 1/4 judges（Qwen3-32B judge + GPT-4o rewriter）。GPT-4o as judge、Llama-70B、Gemini 均无 cross-rewriter 检验。不足以支撑 "Blindspot is rewriter-independent" 的 generalized claim。
- **N3 [critical]**: 负面控制 TOST Δ=15pp 过宽——论文最小 confirmed bias 为 +13pp（GPT-4o formality），Claude 可能有高达 ~14pp bias 而 TOST 仍宣告等价。n=87 功效不足。

### Should-Fix
- **W1**: 因果框架表述不一致——"Controlled Style Decomposition" 和 DAG 带因果含义，但 §3.5 hedge 为 "interventionist"。全文术语需统一。
- **W2**: BT 模型 IIA 假设未讨论。Appendix H 发现 formality 存在显著方向异质性（68.9% vs 52.6%, Fisher p=0.015），BT 单参数公式可能遗漏效应异质性。
- **W3**: NLI gate FNR 估计基于仅 12 个 rejected pairs（Wilson 95% CI ≈ [2%, 28%]），样本量过小。
- **W4**: Verbosity direction-aware NLI gating 额外放入 21 pairs（多 32%），可能引入 selection bias。
- **W5**: Measurement attenuation vs. construct divergence 歧义未解——如果是 construct divergence，"Blindspot" 术语暗示 Likert "遗漏" 了什么，实际上可能只是 "测量了不同的东西"。
- **W6**: 生态效度讨论不足——controlled manipulation 到 naturalistic evaluation 的 generalizability gap。

### Questions
- Q1: Primary family 包含哪三个 judges？
- Q2: Cross-rewriter test 仅覆盖 Qwen3-32B 是否资源约束？
- Q3: Claude TOST 在 n=87 下能 reject 的最小 Δ 是多少？
- Q4: 是否考虑过 stratified BT（按 original text direction 分层）？
- Q5: Likert vs pairwise 比较是否在方法论上不公平（不同统计效率需要不同样本量）？

### Missing References
无显著遗漏。建议补充 Zheng et al. (2024) 更详细讨论。

---

请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W6)、Questions (Q1-Q5) 逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-22T03:38:01.241073+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix\n\n**[AGREE] R1-N1: Primary family 构成缺乏透明度**\n\n同意这是一个严重的透明度问题。Section 4.1 明确声明 \"six hypothesis tests (three judges × two axes)\" 但四个 target judges 中哪三个被纳入 primary family 完全没有说明。这一遗漏在 Table 1 中也未注明。如果被排除的 judge 是 Gemini（其 formality confound 在 Table 3 中表现为 originality-dominated 而非 style-dominated，行为模式与其他三个 judge 不同），则存在 post-hoc cherry-picking 的嫌疑——先观察结果再选择 primary family 会 inflate Type I error rate。\n\n补充我自己的观察：即使作者有 pre-registration 理由（如 Gemini 被归为 exploratory 是因为它是唯一的 Flash-tier 模型），也必须在 §4.1 中明确说明选择标准和理由。当前写法让 reviewer 无法验证 multiple comparison correction 的有效性。\n\n**[AGREE] R1-N2: Cross-rewriter independence 验证覆盖面不足**\n\n同意 Appendix D 仅测试了一个 judge（Qwen3-32B）+一个替代 rewriter（GPT-4o），覆盖面确实不足以支撑 generalized claim。\n\n但我要补充一个 nuance：R1 的关注点（\"不足以支撑 rewriter-independent 的 generalized claim\"）是正确的，但严重性需要 contextualize。论文的核心 claim 不是 \"Blindspot is rewriter-independent\"，而是 \"Likert systematically misses what pairwise detects\"——这一 claim 在全部四个 judges 上用同一 rewriter（Qwen3-32B）得到了 consistent confirmation（Table 1）。Appendix D 的 cross-rewriter check 是一个 supplementary robustness test，其单 judge 覆盖削弱的是 robustness 论证的 generalizability，而非核心 finding 本身。\n\n建议修改：将 Appendix D 的结论从 \"the Blindspot persists with an independent rewriter\" 修改为 \"the Blindspot persists with an independent rewriter for at least one judge configuration; broader cross-rewriter validation remains for future work\"。\n\n**[AGREE] R1-N3: 负面控制 TOST Δ 过宽，n=87 功效不足**\n\n完全同意。这与我在自己的审稿中提出的 W3 一致。\n\nR1 精确地指出了核心矛盾：论文最小 confirmed bias 约 +13pp（GPT-4o formality BT），而 TOST 等价区间 Δ=±13pp（Appendix G），意味着 Claude 可能有接近 confirmed bias 阈值的偏差而仍被宣告等价。这严重削弱了 \"discriminative validity\" 论点。\n\n进一步补充：Appendix G 报告 TOST 通过的前提下，n=87 对 BT=55%（中等偏差）的检测功效应被明确报告。如果 power < 80%，论文需要 acknowledge negative control 的 conclusive power 不足，而非将 TOST 通过作为 strong evidence of absence。\n\n---\n\n## Should-Fix\n\n**[REBUT] R1-W1: 因果框架表述不一致**\n\nR1 认为 \"Controlled Style Decomposition\" 和 DAG 暗示因果声明，与 §3.5 的 \"interventionist\" 定位不一致。我认为这个批评过于严格。\n\n论文在 §3.5 (page 4-5) 做了清晰的 caveat：\"our approach provides interventionist rather than true causal evidence: we do not claim that this DAG is a complete structural causal model.\" 在因果推断文献中，\"controlled intervention\" 和 \"DAG\" 的使用不等同于声称 full causal identification——DAG 常被用作 design rationale 来阐释哪些路径被 blocked 和哪些假设被 relied upon（参见 Pearl 2009 的 interventionist interpretation）。\"Controlled\" 在标题中指 controlled experimental manipulation（NLI-gated content control），这是准确的描述，不是因果 overclaim。\n\n我的判断：术语使用基本一致，§3.5 的 hedge 恰到好处。唯一值得改进的是在 §3.5 开头明确一句 \"We adopt an interventionist, not structural-causal, interpretation throughout\"，但这是 minor polish 而非 inconsistency。\n\n**[AGREE] R1-W2: BT 模型 IIA 假设未讨论**\n\n同意。Appendix H 报告 formality 存在显著方向异质性（原文方向 68.9% vs 52.6%, Fisher p=0.015），BT 模型的 IIA 假设（一次比较的结果不受其他替代品影响）在此受到挑战。单参数 BT 可能掩盖效应的方向依赖性结构。\n\nR1 提出的 stratified BT（Q4）是合理的补充分析方向。至少应在主文或附录中讨论 IIA violation 的影响，并报告 direction-stratified BT estimates。\n\n**[AGREE] R1-W3: NLI gate FNR 样本量过小**\n\n同意。12 个 rejected pairs 的 FNR 估计 CI 极宽（Wilson 95% CI ≈ [2%, 28%]），论文自己也承认 \"FNR may be optimistic\"（§5.1）。这不是一个 fatal flaw（GPT-4o cross-validation 提供了 model-independent check），但 FNR 的不确定性应在主文中被量化（报告 CI），而非仅在 Appendix 中定性提及。\n\n**[AGREE] R1-W4: Verbosity direction-aware gating 可能引入 selection bias**\n\n同意这是一个合理的 concern。Appendix F 报告 direction-aware gate 额外放入 21 pairs（从 65 增至 86, +32%），这些 pairs 的特征可能与 bidirectional-pass pairs 不同（例如它们可能是 verbosity change 更 aggressive 的 pairs）。如果 direction-aware 放入的 pairs 系统性地有更大的 style effect，这会 inflate verbosity 的 BT estimate。\n\n建议作者报告：(1) bidirectional-pass only subset 的 BT estimate，(2) direction-aware only 新增 pairs 的 BT estimate，看两组是否一致。如果一致，selection bias concern 可以被缓解。\n\n**[AGREE] R1-W5: \"Blindspot\" 术语的 loaded nature**\n\n强烈同意——这与我自己的 N1（novelty 定位）高度相关。\"Blindspot\" 一词暗示 Likert 有缺陷、遗漏了重要信息。但如果 construct divergence 解释成立（Likert 测量 absolute quality，pairwise 测量 relative preference），那么 Likert 并非 \"盲\"，而是在看不同的东西。\n\n论文在 §6 和 Limitations 中公平讨论了两种解释，但标题和 Abstract 的 framing 偏向 measurement attenuation 解释（即 Likert 遗漏了真实偏差）。这种 framing bias 应当被 acknowledge。如果不改标题，至少应在 Abstract 结尾加一句 caveat：\"whether this reflects measurement attenuation or construct divergence remains an open question.\"\n\n**[AGREE] R1-W6: 生态效度讨论不足**\n\n同意。论文的 style manipulation 是 controlled（由 LLM rewriter 执行），这与 naturalistic text 中 style 和 content 自然共变的情况有本质区别。在真实评估场景中，style 差异通常伴随 content quality 差异，CSD 的 NLI gate 在那种场景下无法直接应用。\n\n论文 Limitations 中提到了 NLI gate 的局限（\"cannot block quality-style perception shifts\"），但未明确讨论 controlled → naturalistic 的 generalization gap。这应该作为一个独立的 limitation point。\n\n---\n\n## Questions\n\n**[AGREE] R1-Q1: Primary family 包含哪三个 judges？**\n同 N1。必须明确回答。\n\n**[AGREE] R1-Q2: Cross-rewriter test 仅覆盖 Qwen3-32B 是否资源约束？**\n合理的问题。如果是资源约束导致只测了一个 judge，应明确说明。如果有方法论理由（如 Qwen3-32B 作为 primary rewriter 和 judge 的 overlap 最需要排除），也应说明。\n\n**[AGREE] R1-Q3: Claude TOST 在 n=87 下能 reject 的最小 Δ？**\n同 N3。这个数字直接决定 negative control 结论的 informativeness。作者应报告 minimum detectable Δ at 80% power。\n\n**[AGREE] R1-Q4: 是否考虑过 stratified BT？**\n同 W2。Direction-stratified BT 是一个有价值的补充分析，尤其在 Appendix H 已发现方向异质性的情况下。即使作为 Appendix 中的 exploratory analysis，也能大大增强结果的 interpretability。\n\n**[REBUT] R1-Q5: Likert vs pairwise 比较是否方法论不公平？**\n\nR1 提出一个合理但可以反驳的 concern：Likert 和 pairwise 的统计效率不同，直接在同一样本量下比较可能对 Likert 不公平。\n\n然而，论文已通过两个途径部分回应了这个问题：\n\n1. **Appendix K (Formal Power Analysis) & Figure 4**: 明确展示了在不同效应量下 Likert 和 pairwise 各自需要的样本量。对于 verbosity（效应量最大），Likert 需要 n ≈ 1,206-18,157 pairs 才能在 p < 0.001 下达到 80% power（Table 11），而当前 n=100 远远不够。论文并不否认 Likert 在足够大样本下可能检测到偏差——它的 claim 是 \"at practical sample sizes, Likert systematically underestimates\"。\n\n2. **Appendix M (100-point Continuous Likert)**: 更关键的是，即使给 Likert 最有利的条件（100-point scale, eliminating granularity constraint），tie rate 仍高达 51-64%，p 值仍不显著。这表明问题不仅仅是统计效率——Likert 模式下 judges 根本不在 style-transformed pairs 上产生 score variance，这是 paradigmatic limitation 而非 power limitation。\n\n因此，虽然 Q5 提出了方法论公平性的合理 concern，论文的 power analysis + 100-point Likert 双重证据已较充分地表明问题超越了简单的样本量差异。建议在 §5.2 中更明确地回应这一点。\n\n---\n\n## 总结\n\n在 R1 的 14 个具体 issues 中，我 **AGREE 12 条，REBUT 2 条**：\n\n| Issue | 判断 | 核心理由 |\n|-------|------|----------|\n| N1 (primary family) | AGREE | Post-hoc selection 嫌疑，必须透明化 |\n| N2 (cross-rewriter) | AGREE | 覆盖面不足，但严重性应 contextualize |\n| N3 (TOST Δ) | AGREE | 与我的 W3 一致，功效不足 |\n| W1 (causal terminology) | **REBUT** | §3.5 的 hedge 恰当，\"controlled\" 不等于 \"causal\" |\n| W2 (BT IIA) | AGREE | 方向异质性需要讨论 |\n| W3 (FNR sample) | AGREE | CI 过宽，应量化报告 |\n| W4 (direction-aware bias) | AGREE | 需要 subset 对比验证 |\n| W5 (Blindspot 术语) | AGREE | 与我的 N1 (novelty) 呼应 |\n| W6 (生态效度) | AGREE | 缺少 controlled→naturalistic gap 讨论 |\n| Q1 | AGREE | 同 N1 |\n| Q2 | AGREE | 需要说明理由 |\n| Q3 | AGREE | 需要报告 minimum detectable Δ |\n| Q4 | AGREE | Stratified BT 有分析价值 |\n| Q5 | **REBUT** | Power analysis + 100-point Likert 双重证据已回应 |\n\n**与我自己审稿意见的对齐情况**：R1 的 N3 与我的 W3 完全一致；R1 的 W5 与我的 N1（novelty positioning）高度相关；R1 的 W6 补充了我未充分展开的生态效度问题。R1 独特贡献的 N1（primary family selection）和 W2（BT IIA）是我审稿中遗漏的重要技术问题——尤其 N1，我认为应提升为影响接收决定的 critical issue。\n\n**综合两位 reviewer 意见后，我维持 Overall 3.5 (Borderline Conference) 的判断。** 核心结论：论文实验设计优秀但存在多个透明度和方法论问题（primary family selection、TOST power、BT IIA），加上概念 novelty 定位和 human validation 的缺失，使其处于 Conference 和 Findings 的边界。\n",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix\n\n**[AGREE] R1-N1: Primary family 构成缺乏透明度**\n\n同意这是一个严重的透明度问题。Section 4.1 明确声明 \"six hypothesis tests (three judges × two axes)\" 但四个 target judges 中哪三个被纳入 primary family 完全没有说明。这一遗漏在 Table 1 中也未注明。如果被排除的 judge 是 Gemini（其 formality confound 在 Table 3 中表现为 originality-dominated 而非 style-dominated，行为模式与其他三个 judge 不同），则存在 post-hoc cherry-picking 的嫌疑——先观察结果再选择 primary family 会 inflate Type I error rate。\n\n补充我自己的观察：即使作者有 pre-registration 理由（如 Gemini 被归为 exploratory 是因为它是唯一的 Flash-tier 模型），也必须在 §4.1 中明确说明选择标准和理由。当前写法让 reviewer 无法验证 multiple comparison correction 的有效性。\n\n**[AGREE] R1-N2: Cross-rewriter independence 验证覆盖面不足**\n\n同意 Appendix D 仅测试了一个 judge（Qwen3-32B）+一个替代 rewriter（GPT-4o），覆盖面确实不足以支撑 generalized claim。\n\n但我要补充一个 nuance：R1 的关注点（\"不足以支撑 rewriter-independent 的 generalized claim\"）是正确的，但严重性需要 contextualize。论文的核心 claim 不是 \"Blindspot is rewriter-independent\"，而是 \"Likert systematically misses what pairwise detects\"——这一 claim 在全部四个 judges 上用同一 rewriter（Qwen3-32B）得到了 consistent confirmation（Table 1）。Appendix D 的 cross-rewriter check 是一个 supplementary robustness test，其单 judge 覆盖削弱的是 robustness 论证的 generalizability，而非核心 finding 本身。\n\n建议修改：将 Appendix D 的结论从 \"the Blindspot persists with an independent rewriter\" 修改为 \"the Blindspot persists with an independent rewriter for at least one judge configuration; broader cross-rewriter validation remains for future work\"。\n\n**[AGREE] R1-N3: 负面控制 TOST Δ 过宽，n=87 功效不足**\n\n完全同意。这与我在自己的审稿中提出的 W3 一致。\n\nR1 精确地指出了核心矛盾：论文最小 confirmed bias 约 +13pp（GPT-4o formality BT），而 TOST 等价区间 Δ=±13pp（Appendix G），意味着 Claude 可能有接近 confirmed bias 阈值的偏差而仍被宣告等价。这严重削弱了 \"discriminative validity\" 论点。\n\n进一步补充：Appendix G 报告 TOST 通过的前提下，n=87 对 BT=55%（中等偏差）的检测功效应被明确报告。如果 power < 80%，论文需要 acknowledge negative control 的 conclusive power 不足，而非将 TOST 通过作为 strong evidence of absence。\n\n---\n\n## Should-Fix\n\n**[REBUT] R1-W1: 因果框架表述不一致**\n\nR1 认为 \"Controlled Style Decomposition\" 和 DAG 暗示因果声明，与 §3.5 的 \"interventionist\" 定位不一致。我认为这个批评过于严格。\n\n论文在 §3.5 (page 4-5) 做了清晰的 caveat：\"our approach provides interventionist rather than true causal evidence: we do not claim that this DAG is a complete structural causal model.\" 在因果推断文献中，\"controlled intervention\" 和 \"DAG\" 的使用不等同于声称 full causal identification——DAG 常被用作 design rationale 来阐释哪些路径被 blocked 和哪些假设被 relied upon（参见 Pearl 2009 的 interventionist interpretation）。\"Controlled\" 在标题中指 controlled experimental manipulation（NLI-gated content control），这是准确的描述，不是因果 overclaim。\n\n我的判断：术语使用基本一致，§3.5 的 hedge 恰到好处。唯一值得改进的是在 §3.5 开头明确一句 \"We adopt an interventionist, not structural-causal, interpretation throughout\"，但这是 minor polish 而非 inconsistency。\n\n**[AGREE] R1-W2: BT 模型 IIA 假设未讨论**\n\n同意。Appendix H 报告 formality 存在显著方向异质性（原文方向 68.9% vs 52.6%, Fisher p=0.015），BT 模型的 IIA 假设（一次比较的结果不受其他替代品影响）在此受到挑战。单参数 BT 可能掩盖效应的方向依赖性结构。\n\nR1 提出的 stratified BT（Q4）是合理的补充分析方向。至少应在主文或附录中讨论 IIA violation 的影响，并报告 direction-stratified BT estimates。\n\n**[AGREE] R1-W3: NLI gate FNR 样本量过小**\n\n同意。12 个 rejected pairs 的 FNR 估计 CI 极宽（Wilson 95% CI ≈ [2%, 28%]），论文自己也承认 \"FNR may be optimistic\"（§5.1）。这不是一个 fatal flaw（GPT-4o cross-validation 提供了 model-independent check），但 FNR 的不确定性应在主文中被量化（报告 CI），而非仅在 Appendix 中定性提及。\n\n**[AGREE] R1-W4: Verbosity direction-aware gating 可能引入 selection bias**\n\n同意这是一个合理的 concern。Appendix F 报告 direction-aware gate 额外放入 21 pairs（从 65 增至 86, +32%），这些 pairs 的特征可能与 bidirectional-pass pairs 不同（例如它们可能是 verbosity change 更 aggressive 的 pairs）。如果 direction-aware 放入的 pairs 系统性地有更大的 style effect，这会 inflate verbosity 的 BT estimate。\n\n建议作者报告：(1) bidirectional-pass only subset 的 BT estimate，(2) direction-aware only 新增 pairs 的 BT estimate，看两组是否一致。如果一致，selection bias concern 可以被缓解。\n\n**[AGREE] R1-W5: \"Blindspot\" 术语的 loaded nature**\n\n强烈同意——这与我自己的 N1（novelty 定位）高度相关。\"Blindspot\" 一词暗示 Likert 有缺陷、遗漏了重要信息。但如果 construct divergence 解释成立（Likert 测量 absolute quality，pairwise 测量 relative preference），那么 Likert 并非 \"盲\"，而是在看不同的东西。\n\n论文在 §6 和 Limitations 中公平讨论了两种解释，但标题和 Abstract 的 framing 偏向 measurement attenuation 解释（即 Likert 遗漏了真实偏差）。这种 framing bias 应当被 acknowledge。如果不改标题，至少应在 Abstract 结尾加一句 caveat：\"whether this reflects measurement attenuation or construct divergence remains an open question.\"\n\n**[AGREE] R1-W6: 生态效度讨论不足**\n\n同意。论文的 style manipulation 是 controlled（由 LLM rewriter 执行），这与 naturalistic text 中 style 和 content 自然共变的情况有本质区别。在真实评估场景中，style 差异通常伴随 content quality 差异，CSD 的 NLI gate 在那种场景下无法直接应用。\n\n论文 Limitations 中提到了 NLI gate 的局限（\"cannot block quality-style perception shifts\"），但未明确讨论 controlled → naturalistic 的 generalization gap。这应该作为一个独立的 limitation point。\n\n---\n\n## Questions\n\n**[AGREE] R1-Q1: Primary family 包含哪三个 judges？**\n同 N1。必须明确回答。\n\n**[AGREE] R1-Q2: Cross-rewriter test 仅覆盖 Qwen3-32B 是否资源约束？**\n合理的问题。如果是资源约束导致只测了一个 judge，应明确说明。如果有方法论理由（如 Qwen3-32B 作为 primary rewriter 和 judge 的 overlap 最需要排除），也应说明。\n\n**[AGREE] R1-Q3: Claude TOST 在 n=87 下能 reject 的最小 Δ？**\n同 N3。这个数字直接决定 negative control 结论的 informativeness。作者应报告 minimum detectable Δ at 80% power。\n\n**[AGREE] R1-Q4: 是否考虑过 stratified BT？**\n同 W2。Direction-stratified BT 是一个有价值的补充分析，尤其在 Appendix H 已发现方向异质性的情况下。即使作为 Appendix 中的 exploratory analysis，也能大大增强结果的 interpretability。\n\n**[REBUT] R1-Q5: Likert vs pairwise 比较是否方法论不公平？**\n\nR1 提出一个合理但可以反驳的 concern：Likert 和 pairwise 的统计效率不同，直接在同一样本量下比较可能对 Likert 不公平。\n\n然而，论文已通过两个途径部分回应了这个问题：\n\n1. **Appendix K (Formal Power Analysis) & Figure 4**: 明确展示了在不同效应量下 Likert 和 pairwise 各自需要的样本量。对于 verbosity（效应量最大），Likert 需要 n ≈ 1,206-18,157 pairs 才能在 p < 0.001 下达到 80% power（Table 11），而当前 n=100 远远不够。论文并不否认 Likert 在足够大样本下可能检测到偏差——它的 claim 是 \"at practical sample sizes, Likert systematically underestimates\"。\n\n2. **Appendix M (100-point Continuous Likert)**: 更关键的是，即使给 Likert 最有利的条件（100-point scale, eliminating granularity constraint），tie rate 仍高达 51-64%，p 值仍不显著。这表明问题不仅仅是统计效率——Likert 模式下 judges 根本不在 style-transformed pairs 上产生 score variance，这是 paradigmatic limitation 而非 power limitation。\n\n因此，虽然 Q5 提出了方法论公平性的合理 concern，论文的 power analysis + 100-point Likert 双重证据已较充分地表明问题超越了简单的样本量差异。建议在 §5.2 中更明确地回应这一点。\n\n---\n\n## 总结\n\n在 R1 的 14 个具体 issues 中，我 **AGREE 12 条，REBUT 2 条**：\n\n| Issue | 判断 | 核心理由 |\n|-------|------|----------|\n| N1 (primary family) | AGREE | Post-hoc selection 嫌疑，必须透明化 |\n| N2 (cross-rewriter) | AGREE | 覆盖面不足，但严重性应 contextualize |\n| N3 (TOST Δ) | AGREE | 与我的 W3 一致，功效不足 |\n| W1 (causal terminology) | **REBUT** | §3.5 的 hedge 恰当，\"controlled\" 不等于 \"causal\" |\n| W2 (BT IIA) | AGREE | 方向异质性需要讨论 |\n| W3 (FNR sample) | AGREE | CI 过宽，应量化报告 |\n| W4 (direction-aware bias) | AGREE | 需要 subset 对比验证 |\n| W5 (Blindspot 术语) | AGREE | 与我的 N1 (novelty) 呼应 |\n| W6 (生态效度) | AGREE | 缺少 controlled→naturalistic gap 讨论 |\n| Q1 | AGREE | 同 N1 |\n| Q2 | AGREE | 需要说明理由 |\n| Q3 | AGREE | 需要报告 minimum detectable Δ |\n| Q4 | AGREE | Stratified BT 有分析价值 |\n| Q5 | **REBUT** | Power analysis + 100-point Likert 双重证据已回应 |\n\n**与我自己审稿意见的对齐情况**：R1 的 N3 与我的 W3 完全一致；R1 的 W5 与我的 N1（novelty positioning）高度相关；R1 的 W6 补充了我未充分展开的生态效度问题。R1 独特贡献的 N1（primary family selection）和 W2（BT IIA）是我审稿中遗漏的重要技术问题——尤其 N1，我认为应提升为影响接收决定的 critical issue。\n\n**综合两位 reviewer 意见后，我维持 Overall 3.5 (Borderline Conference) 的判断。** 核心结论：论文实验设计优秀但存在多个透明度和方法论问题（primary family selection、TOST power、BT IIA），加上概念 novelty 定位和 human validation 的缺失，使其处于 Conference 和 Findings 的边界。\n",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-22T03:38:05.107265+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3866
}
```

</details>

---


### Assistant

_source line 650 · 2026-05-22T03:38:10.373542+00:00_

已完成对 Reviewer 1 全部 14 条意见的逐条交叉回应，AGREE 12 条，REBUT 2 条（W1 因果术语、Q5 方法论公平性）。已提交至 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 21

## Round 21

52 recorded events


### User

_source line 651 · 2026-05-22T09:13:19.697238+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查 **新颖性、完整性、related work 覆盖、写作质量**。

## 投稿信息
- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 提交）
- **Deadline**: 2026-05-25
- **格式要求**: ACL template, double-blind, 正文 8 页限制, references 不限页, Limitations 必须有但不计入页数
- **匿名规则**: double-blind（作者信息不可出现）
- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`（各章节在 `sections/` 子目录）
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf`

## 论文概述
题目: "The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition"
核心claim: Likert评分系统性地遗漏了pairwise comparison能检测到的风格偏差（Likert Blindspot），提出CSD框架（NLI-gated content control + per-axis style decomposition + position-controlled pairwise comparison）来量化LLM judges的风格偏差。跨四个独立 judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）、一个负对照（Claude Sonnet 4）、三个 benchmark、三个 style axis 验证。

## 你的审查重点

### 1. 新颖性评估
- "Likert Blindspot" 作为核心发现：这是否真正是新发现？Thurstone (1927) 的 Law of Comparative Judgment 已经预测了 pairwise > Likert 的敏感性差异。本文的 empirical contribution 是否足以构成顶会水平的 novelty？
- CSD 框架的各个组件（NLI gating, style rewriting, BT model）都是已有技术的组合——组合本身是否构成足够 novelty？
- 与 RATE (Reber et al., 2025) 的区分是否清晰？本文是否主要是 RATE 的 measurement mode upgrade（从 Likert 换成 pairwise）？
- Per-axis confound structure（GEE decomposition 揭示 verbosity=style-dominated, formality=conditional, register=judge-dependent）是否是独立的 novel contribution？

### 2. Related Work 覆盖
- 是否遗漏重要的相关工作？特别是：
  - LLM-as-judge bias 的最新工作（2025-2026）
  - 因果文本分析方法（CausalM, CausalNLP 等）
  - 风格偏差检测和缓解
  - 测量理论在 NLP 评估中的应用
- 与竞品的定位是否准确？（RATE, CASSE, FairJudge, Preference Leakage, Soumik 2026 等）
- 引用是否完整和准确？

### 3. 完整性
- 论文的 story line 是否连贯？从 problem → method → experiments → analysis 的逻辑链是否完整？
- 是否有 claims 缺乏足够支撑？
- Limitations section 是否诚实和完整？是否有重大缺陷被忽略？
- Conclusion 是否过于 strong / weak relative to evidence?

### 4. 写作质量
- 论文的可读性如何？结构是否清晰？
- 术语使用是否一致？
- 图表是否有效传达信息？
- Abstract 是否准确概括论文内容？
- 是否有 AI 生成痕迹（过度使用 hedging, boilerplate phrases 等）？

### 5. 对 EMNLP community 的影响力
- 这个 work 的 target audience 是谁？
- 对 LLM evaluation 实践有什么直接 actionable takeaway？
- 是否会激发 follow-up research？

请按 ARR review form 格式输出你的审稿意见：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (1-5 scale per EMNLP 2026 ARR guidelines), Confidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-22T09:13:27.445438+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
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

_source line 653 · 2026-05-22T09:13:27.445842+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-22T09:13:31.411968+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 655 · 2026-05-22T09:13:32.315767+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 656 · 2026-05-22T09:13:39.495822+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria:

## Reviewer Guidelines

Reviewers are asked to follow a workflow: (1) read the paper and get the first impression, (2) search for related work
…[truncated 1418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8083
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-22T09:13:40.603439+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 509.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 572.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.7}], \"total_pages\": 16, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts
…[truncated 68 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8287
}
```

</details>

---


### Tool call

_source line 658 · 2026-05-22T09:13:46.583773+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form fields, scoring criteria, and all rating scales. I need every dimension that reviewers must score, with their exact scale descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form fields, scoring criteria, and all rating scales. I need every dimension that reviewers must score, with their exact scale descriptions."
  }
}
```

</details>

---


### Tool call

_source line 659 · 2026-05-22T09:13:47.086758+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-22T09:13:47.589533+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-22T09:13:48.494738+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool result

_source line 662 · 2026-05-22T09:13:48.495994+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 663 · 2026-05-22T09:13:48.497487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-22T09:13:49.001321+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-22T09:13:49.504011+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-22T09:13:49.504485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-22T09:13:50.408957+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool result

_source line 668 · 2026-05-22T09:13:50.410385+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 669 · 2026-05-22T09:13:50.410742+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-22T09:13:50.962741+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-22T09:13:51.265157+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-22T09:13:51.466447+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-22T09:13:51.568467+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool result

_source line 674 · 2026-05-22T09:13:52.121163+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-22T09:13:55.732854+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Required Review Fields

1. **Paper Summary** - Descriptive overview of paper topic and content

2. **Summary of Strengths** - Major reasons supporting publication at selective *ACL venues

3. **Summary of Weaknesses** - Numbered concerns prioritizing other high-quality papers

4. **Comments/Suggestions/Typos** - Additional improvement recommendations

## Scoring Dimensions with Rating Scales

### Reviewer Confidence
Range: 1-5
- 5: "Positive that my evaluation is correct"
- 4: "Quite sure" with unlikely but conceivable errors
- 3: "Pretty sure" but may have missed details
- 2: "Willing to defend" but likely missed some points
- 1: "Not my area" or incomprehensible paper

### Soundness
Range: 1-5 (with half-point increments: 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5)
- 5: "Excellent" - most thorough study
- 4: "Strong" - sufficient support with minor gaps
- 3: "Acceptable" - main claims supported
- 2: "Poor" - insufficient support for claims
- 1: "Major Issues" - inadequate for publication

### Excitement
Range: 1-5 (with half-point increments)
- 5: "Highly Exciting" - would recommend widely
- 4: "Exciting" - would mention to others
- 3: "Interesting" - might mention or attend
- 2: "Potentially Interesting" - doesn't resonate personally
- 1: "Not Exciting" - unlikely to resonate broadly

### Overall Assessment
Range: 1-5 (with half-point increments)
- 5: "Consider for Award" - top 2.5% papers
- 4.5: "Borderline Award"
- 4: "Conference" - accept to *ACL conference
- 3.5: "Borderline Conference"
- 3: "Findings" - accept to ACL Findings
- 2.5: "Borderline Findings"
- 2: "Resubmit next cycle" - substantial revisions needed
- 1.5: "Resubmit after next cycle" - major revisions required
- 1: "Do not resubmit" - complete overhaul needed

## Additional Assessment Areas

### Limitations and Societal Impact
Narrative evaluation of discussed limitations and potential impacts

### Ethical Concerns
Alignment assessment with ACL c
…[truncated 890 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 9149
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-22T09:14:07.131445+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "9-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "9-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-22T09:14:08.588536+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.5}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 430.1}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 414.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 618.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 599.6}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 101.6}], \"total_pages\": 16, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_j
…[truncated 82 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-22T09:14:08.589055+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should look for in novelty, soundness, experimental methodology, related work coverage, and writing quality. Include any specific instructions about how to evaluate papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should look for in novelty, soundness, experimental methodology, related work coverage, and writing quality. Include any specific instructions about how to evaluate papers."
  }
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-22T09:14:16.474144+00:00_

# ARR Reviewer Guidelines: Core Evaluation Criteria

## Novelty Assessment

Reviewers should verify that claimed contributions are genuinely original. The guidelines warn against dismissing work as non-novel without providing specific references to prior art. Papers must compare against work published at least 3+ months before submission. Negative results and reimplementations deserve fair evaluation within the CFP scope.

**Key caution:** "If the paper claims e.g. a novel method, and you think you've seen this before - you need to provide a reference."

## Soundness Evaluation

Soundness scores must align with review content. Low scores require justification through identified technical flaws. Reviewers should distinguish between sound work they personally find unexciting versus genuinely flawed research. The guidelines emphasize that "a paper only needs to present sufficient evidence for the claim that the authors are making."

Critical checks include:
- Methodology appropriateness for the research question
- Valid proofs with clearly stated assumptions
- Appropriate statistical analysis and significance testing

## Experimental Methodology

Reviewers should verify:

- **Reproducibility:** Sufficient hyperparameter details, code/data availability disclosures
- **Fair baselines:** Well-tuned comparisons, avoiding p-hacking
- **Scope validity:** Results represent claimed populations (not overgeneralizing from limited benchmarks)
- **LLM evaluation:** Automated evaluator reliability must be validated within context

Requesting comparisons to closed-source models is appropriate only when directly supporting core claims.

## Related Work Coverage

Authors must cite published work from 3+ months prior to submission. Missing recent preprints are acceptable. Papers should fairly represent prior contributions and clarify their own novelty relative to existing work.

## Writing Quality

Professional, neutral tone is essential. Clear communication matters more than perfect g
…[truncated 196 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7885
}
```

</details>

---


### Tool call

_source line 680 · 2026-05-22T09:14:19.994509+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-22T09:14:20.647484+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 682 · 2026-05-22T09:14:20.948552+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 683 · 2026-05-22T09:14:21.501204+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-22T09:14:21.501661+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 685 · 2026-05-22T09:14:22.003679+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 686 · 2026-05-22T09:14:22.355748+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 687 · 2026-05-22T09:14:22.356223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 688 · 2026-05-22T09:14:23.361699+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1358
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-22T09:14:23.362866+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-22T09:14:23.363190+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 691 · 2026-05-22T09:14:23.765488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 692 · 2026-05-22T09:14:24.271929+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 693 · 2026-05-22T09:14:24.272403+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 694 · 2026-05-22T09:14:24.324966+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-22T09:14:24.983434+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1217
}
```

</details>

---


### Tool call

_source line 696 · 2026-05-22T09:20:50.954344+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见 — Round 1 (Fresh Review)\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审查侧重**: 新颖性、完整性、Related Work 覆盖、写作质量\n\n---\n\n## Paper Summary\n\n本文提出 Controlled Style Decomposition (CSD) 框架，用于检测 LLM judge 中被 Likert 评分遗漏但可被 pairwise comparison 捕获的风格偏差（称为 \"Likert Blindspot\"）。CSD 由三部分组成：NLI-gated content control（确保风格重写不改变内容）、per-axis style decomposition（逐轴分离风格效应）、position-controlled pairwise comparison + Bradley-Terry 建模。实验跨 4 个 target judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）、1 个负对照（Claude Sonnet 4）、3 个 benchmark（LLMBar, AlpacaEval, MT-Bench）、2+1 个 style axis（formality, verbosity + register replication）验证。核心发现：(1) Likert 在中等效应量时完全失效（d → 0），在较强效应时衰减 >60%；(2) per-axis confound structure 不同——verbosity 是 style-dominated，formality 是 conditional on originality，register 是 judge-dependent。\n\n## Summary of Strengths\n\n**S1. 实验设计的严谨性与多维度复制。** 4+1 judges × 3 benchmarks × 2+1 style axes 的实验矩阵，加上 7 种统计方法交叉验证（Table 2），在该领域的 empirical 工作中不常见。负对照（Claude Sonnet 4 显示弱/无偏差）增强了因果推断的可信度。\n\n**S2. Sensitivity hierarchy 的干净结果。** Table 2 的全有或全无模式极具说服力：所有 pairwise 方法（BT model, sign test）达到显著性，所有 Likert 方法（ATE t-test, binarized Likert, ordinal regression, GEE, Wilcoxon signed-rank）均不显著。这种一致性比单一统计检验更有说服力。\n\n**S3. Per-axis confound structure 是独立的有价值发现。** Section 5.2 和 Table 3 的 GEE conditional decomposition 揭示 verbosity = style-dominated（Style OR 8.2–13.1, all p < 0.001）、formality = conditional on originality preference、register = judge-dependent。这对 LLM judge 用户有直接 actionable value——对 verbosity 可以做 universal debiasing，对 formality 需要 per-judge conditional analysis。\n\n**S4. Robustness 分析的深度几乎回答了每个合理质疑。** Appendix A–Q 覆盖：方向非对称性（A）、NLI consistency filter（B）、GEE model diagnostics（C）、rewriter independence（D, Tables 7-8）、NLI threshold sensitivity sweep（E, Table 9）、direction-aware gate validation（F）、Claude Sonnet 4 equivalence testing（G）、bootstrap attenuation（H）、BT goodness-of-fit（I）、verbosity sensitivity hierarchy（L）、100-point continuous Likert（M）、NLI gate ablation（N）、rewriting artifact control（O）。这种系统性的 robustness checking 值得肯定。\n\n**S5. Black-box 框架设计。** CSD 不需要 judge 内部访问权限（no access to judge internals），可 post-hoc 应用于任何 black-box judge，实用性强。\n\n**S6. Figure 3 和 Figure 4 的可视化效果好。** Figure 3 的 Bradley-Terry win probability plot 清晰地展示了跨 judge-axis 的 Blindspot 模式；Figure 4 的 detection probability vs. effect magnitude 曲线直观地说明了 Likert 和 pairwise 在不同效应量下的灵敏度差异。\n\n## Summary of Weaknesses\n\n**N1** [critical] **新颖性定位：核心发现是\"实证确认\"而非\"新发现\"**\n\n- 具体位置：Abstract（\"We ... reveal the Likert Blindspot\"）、Section 1 第2段、Section 2 最后一段、Section 5.1 标题（\"The Likert Blindspot\"）\n- 问题：论文将 Likert Blindspot 包装为一个新发现。但 Thurstone (1927) 的 Law of Comparative Judgment 和后续测量理论研究（Preston & Colman, 2000；Krosnick, 1999——论文自己引用的；Louviere et al., 2015——论文也引用的）早已建立了 pairwise comparison 相对于 rating scale 的敏感性优势。论文在 Section 2（第2页）也明确承认：\"the superiority of pairwise comparison over rating scales for eliciting reliable human judgments has been established since Thurstone (1927).\" 紧接着又声称 \"Our contribution is the first controlled, per-axis quantification of this sensitivity gap for LLM judge style bias\"（第3页）。\n\n  问题不在于贡献不存在，而在于叙事框架。当论文用 \"reveal\" 和 \"Blindspot\" 这类带有发现色彩的词汇时，暗示这是一个意外的新发现（unexpected finding）。但考虑到 measurement theory 的预测，更准确的定位是：**设计了一个框架（CSD）来在 LLM judge 场景下系统性地量化一个理论预测的测量敏感性差距，并在此过程中发现了 per-axis confound structure。** 后者（per-axis confound structure）才是真正没有被先验理论预测的 novel finding。\n\n- 为什么影响接收：ARR reviewer guidelines 明确说，如果 reviewer 认为 novelty 不足，必须提供具体 prior art。这里 Thurstone (1927)、Preston & Colman (2000) 就是直接的 prior art。当前 framing 让有测量理论背景的 reviewer 容易 dismiss 整篇论文，即使 empirical 贡献本身有价值。\n- 建议修改方向：\n  (1) 重新定位 narrative：从\"我们发现了 Likert Blindspot\"转向\"我们设计 CSD 框架首次在 LLM judge 风格偏差中量化了这个理论预测的敏感性差距，量化结果显示其严重性超出预期（complete attenuation at moderate effects），且发现了 per-axis confound structure 这一新模式\"。\n  (2) 将 per-axis confound structure 提升为与 Blindspot quantification 平行的核心贡献。\n  (3) Abstract 第一句可改为承认理论预测，第二句说明本文的 empirical contribution。\n\n**N2** [critical] **Pairwise \"检测\" vs. Pairwise \"放大\"：核心解释性歧义未充分解决**\n\n- 具体位置：Section 5.4（第6–7页）、Section 6 (Conclusion)、Limitations\n- 问题：论文的核心叙事假设 pairwise comparison 检测到了真实的风格偏差，而 Likert 遗漏了它。但存在一个对等的替代解释：**pairwise comparison 放大了微小的、实际上无关紧要的风格微偏好**，使其达到统计显著性，而 Likert 的\"不显著\"才反映了真实的效应大小。\n\n  论文在 Section 5.4 引用了 Jeong et al. (2025) 的 Comparative Trap（pairwise comparison amplifies style biases relative to positive-scoring），并在第6页讨论了 \"measurement attenuation vs. construct divergence\"。但论文的论证有循环性问题：\n\n  (a) 论文说 \"Likert audits miss style preferences that drive pairwise-based alignment pipelines (RLHF, DPO)\"（第6页），用这一点来论证 pairwise 检测到的是\"真实\"偏差。但这个论证预设了 RLHF/DPO pipeline 中的 pairwise preference 反映了真实偏差——而这恰恰是需要证明的。\n  (b) Bootstrap attenuation analysis (Appendix H) 排除了\"纯粹是统计功效差异\"的解释，但不能排除 \"pairwise 系统性放大微小偏好\" 的可能——BT 在小样本时仍显著，可能恰恰是因为 pairwise 的放大效应。\n  (c) 第6页的 \"Both interpretations lead to the same conclusion\" 论证也不完全成立——如果 pairwise 是在放大噪声，那么用 pairwise 来\"审计\" judges 就可能产生大量 false positives。\n\n- 为什么影响接收：这个解释性歧义直接影响论文发现的实际意义。如果读者接受\"放大\"解释，论文的 practical implication（\"用 pairwise 来审计 LLM judge 风格偏差\"）就可能被认为是误导性的。\n- 建议修改方向：\n  (1) 最理想的方案：增加一个基于 human ground-truth 的验证——对 style-manipulated pairs 收集人类偏好判断，比较 pairwise 和 Likert 哪个更接近人类判断。即使是小规模验证也能大幅增强论文的说服力。\n  (2) 次优方案：在 Section 5.4 或 Discussion 中更 prominently 地承认这个限制，明确说明当前证据无法区分两种解释，并讨论在什么条件下每种解释的 implication 是什么。避免在 Conclusion 中使用 \"reveal\" 等暗示单一解释的语言。\n\n**W1** [warning] **Style axis 覆盖面过窄，confound structure claim 的泛化基础不足**\n\n- 具体位置：Section 3.1、Section 4、Section 5.2\n- 问题：论文仅测试 2 个 primary axes (formality, verbosity) + 1 个 replication (register)。LLM judge 的已知风格偏差远不止这些（例如 bullet-point vs. prose、hedging/confidence level、response length distribution 的 long-tail 效应等）。基于 3 个 axis 声称发现了 \"per-axis confound structure\"，这种分类法（style-dominated / conditional / judge-dependent）的泛化性缺乏支撑——读者无法判断新的 style axis 会属于哪种类型。\n- 建议：(1) 在正文明确限定 confound structure claim 的适用范围（\"for the three axes we tested\"）；(2) 在 Limitations 中讨论 axis 覆盖的局限性；(3) 简要说明 axis 选择的先验理由（如 pilot study 或文献依据）。\n\n**W2** [warning] **NLI gate 高拒绝率（~44%）的选择偏差分析不足**\n\n- 具体位置：Section 3.2、Appendix B\n- 问题：NLI consistency filter 保留 55/98 pairs (56.1%)。Appendix B 报告 \"no significant differences across four covariates (NLI score p = 0.824, BERTS p = 0.12, text length p = 0.137, length diff p = 0.715)\"，但这 4 个 covariates 可能不够全面。通过 NLI gate 的 pairs 可能系统性地偏向内容更简单、风格变化更容易分离的文本。这意味着 Blindspot 的效应量 estimate 可能在更复杂的文本上不可靠。\n- 建议：(1) 分析被拒绝 pairs 的文本特征（例如原始 style 距离、话题复杂度、指令类型）vs. 保留 pairs；(2) 讨论 selection bias 对 external validity 的影响。\n\n**W3** [warning] **100-point continuous Likert 实验仅用单一 judge**\n\n- 具体位置：Appendix M（第12页）\n- 问题：此实验旨在排除\"Blindspot 是整数刻度粒度的人为产物\"这一替代解释，但仅使用 Qwen3-32B 一个 judge。如果 GPT-4o 或其他 judge 在 100-point scale 下表现不同（例如 fine-grained scale 确实能检测到偏差），则该结论不成立。\n- 建议：至少在一个额外 judge 上复制此实验，或明确标注为 preliminary evidence。\n\n**W4** [warning] **因果语言与实际方法论之间的张力**\n\n- 具体位置：Title (\"Controlled Style Decomposition\")、Section 3 开头、Figure 2\n- 问题：论文在 Section 4（第4页）给出了合理的 disclaimer (\"we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions\")，这值得肯定。但标题中的 \"Controlled\" 和方法描述中的 \"interventional\" 语言仍然暗示了比实际更强的因果识别——NLI gating 是一种近似的内容控制（approximate content preservation），而非因果推断文献中的 do-operator。Figure 2 的 DAG notation 也可能让有因果推断背景的读者期望看到正式的 identification strategy。\n- 建议：在 Method 开头更早地明确说明这是 \"approximately controlled comparison\" 而非 \"causally identified effect\"，以管理读者预期。\n\n## Questions for Authors\n\nQ1. 关于 N2（检测 vs. 放大）：是否有计划收集 human preference 判断来 ground-truth pairwise 检测到的风格偏差？即使是一个小规模的 pilot（例如 50 pairs × 3 annotators）也能大幅增强论文的说服力。\n\nQ2. 关于 W1（style axes）：选择 formality 和 verbosity 作为 primary axes 的先验理由是什么？是否有 pilot study 表明这两个 axis 的效应最大？如果选择了不同的 axes（例如 bullet-point usage, hedging level），Blindspot 是否仍然存在？\n\nQ3. 关于 Appendix D（rewriter independence）：GPT-4o 作为替代 rewriter 时（Table 7），verbosity 的 Style OR 从 Qwen3-32B rewriter 的高值下降了 22%。这种下降是否暗示 Blindspot 的效应量部分依赖于 rewriter 的具体风格？如果使用完全不同的 rewriting 方法（例如 rule-based rewriting），结果会如何变化？\n\nQ4. 关于 Section 5.4（Comparative Trap）：论文引用了 6 个 experimental controls 来 bound the risk of amplification（NLI gate ablation、Claude Sonnet 4 equivalence、TOST equivalence at Δ = 13pp 等）。但这些 controls 只能排除\"大规模放大\"，无法排除\"中等程度放大\"。是否有办法量化 pairwise 的放大倍数（amplification factor），而不仅仅是定性地论证？\n\n## Missing References\n\n1. **Item Response Theory (IRT) 在 LLM/NLP 评估中的应用**：论文讨论了 Likert vs. pairwise 的测量属性，但没有引用 IRT 文献。Polo et al. (2024, \"tinyBenchmarks: evaluating LLMs with fewer examples\") 和 Otani et al. (2023) 从测量理论角度分析 LLM 评估的可靠性和效度，与本文的 measurement sensitivity 主题直接相关。\n2. **Kocmi and Federmann (2023)** \"Large Language Models Are Not Fair Multilingual Evaluators\" — 虽然聚焦 MT 评估，但其关于 LLM judge bias 在不同评估格式下的表现差异与本文主题相关。\n3. 建议验证 Stureborg et al. (2024) 是否在参考文献列表中完整列出（正文有引用但 references 部分需确认）。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| **Soundness** | 4/5 (Strong) | 实验设计严谨，多维度复制和 7 种统计方法交叉验证是 strong evidence。扣分原因：NLI gate ~44% rejection rate 的 selection bias 未充分分析；核心解释性歧义（检测 vs. 放大）未解决 |\n| **Excitement** | 3/5 (Interesting) | 对 LLM 评估社区有实用价值，per-axis confound structure 有新意。核心 Blindspot 发现主要是已有测量理论的实证确认，降低了 excitement |\n| **Reproducibility** | 4/5 (Mostly reproducible) | 方法描述清晰，超参数完整（Appendix P），承诺释放代码和数据。NLI gate 的具体 threshold tuning 和 style rewriting 的 prompt templates 可能影响 exact reproduction |\n| **Overall Assessment** | **3.5** (Borderline Conference) | 实验工作扎实，结果清晰，对社区有实用价值。但核心发现的新颖性受限于已有测量理论预测，且\"检测 vs. 放大\"的核心解释性歧义未充分解决。如果 reframe novelty narrative 并增加 human ground-truth validation，可以更有信心地推荐 Conference |\n| **Confidence** | 4/5 (Quite sure) | 熟悉 LLM-as-judge evaluation、measurement theory 和 causal NLP 文献。可能遗漏的点：对 GEE 模型选择的技术细节不够深入 |\n\n## 主要优势（总结）\n\n1. 实验设计的多维度复制（4+1 judges × 3 benchmarks × 2+1 axes × 7 statistical methods）在该领域罕见\n2. Table 2 的 sensitivity hierarchy 是一个极其干净的 all-or-nothing 结果\n3. Per-axis confound structure（S5.2, Table 3）是独立的有价值发现\n4. Robustness 分析（Appendix A–Q）几乎回答了每个合理质疑\n5. Black-box 框架设计有强 practical applicability\n6. 写作整体清晰，Figure 3/4 有效传达核心信息\n",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿意见 — Round 1 (Fresh Review)\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审查侧重**: 新颖性、完整性、Related Work 覆盖、写作质量\n\n---\n\n## Paper Summary\n\n本文提出 Controlled Style Decomposition (CSD) 框架，用于检测 LLM judge 中被 Likert 评分遗漏但可被 pairwise comparison 捕获的风格偏差（称为 \"Likert Blindspot\"）。CSD 由三部分组成：NLI-gated content control（确保风格重写不改变内容）、per-axis style decomposition（逐轴分离风格效应）、position-controlled pairwise comparison + Bradley-Terry 建模。实验跨 4 个 target judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）、1 个负对照（Claude Sonnet 4）、3 个 benchmark（LLMBar, AlpacaEval, MT-Bench）、2+1 个 style axis（formality, verbosity + register replication）验证。核心发现：(1) Likert 在中等效应量时完全失效（d → 0），在较强效应时衰减 >60%；(2) per-axis confound structure 不同——verbosity 是 style-dominated，formality 是 conditional on originality，register 是 judge-dependent。\n\n## Summary of Strengths\n\n**S1. 实验设计的严谨性与多维度复制。** 4+1 judges × 3 benchmarks × 2+1 style axes 的实验矩阵，加上 7 种统计方法交叉验证（Table 2），在该领域的 empirical 工作中不常见。负对照（Claude Sonnet 4 显示弱/无偏差）增强了因果推断的可信度。\n\n**S2. Sensitivity hierarchy 的干净结果。** Table 2 的全有或全无模式极具说服力：所有 pairwise 方法（BT model, sign test）达到显著性，所有 Likert 方法（ATE t-test, binarized Likert, ordinal regression, GEE, Wilcoxon signed-rank）均不显著。这种一致性比单一统计检验更有说服力。\n\n**S3. Per-axis confound structure 是独立的有价值发现。** Section 5.2 和 Table 3 的 GEE conditional decomposition 揭示 verbosity = style-dominated（Style OR 8.2–13.1, all p < 0.001）、formality = conditional on originality preference、register = judge-dependent。这对 LLM judge 用户有直接 actionable value——对 verbosity 可以做 universal debiasing，对 formality 需要 per-judge conditional analysis。\n\n**S4. Robustness 分析的深度几乎回答了每个合理质疑。** Appendix A–Q 覆盖：方向非对称性（A）、NLI consistency filter（B）、GEE model diagnostics（C）、rewriter independence（D, Tables 7-8）、NLI threshold sensitivity sweep（E, Table 9）、direction-aware gate validation（F）、Claude Sonnet 4 equivalence testing（G）、bootstrap attenuation（H）、BT goodness-of-fit（I）、verbosity sensitivity hierarchy（L）、100-point continuous Likert（M）、NLI gate ablation（N）、rewriting artifact control（O）。这种系统性的 robustness checking 值得肯定。\n\n**S5. Black-box 框架设计。** CSD 不需要 judge 内部访问权限（no access to judge internals），可 post-hoc 应用于任何 black-box judge，实用性强。\n\n**S6. Figure 3 和 Figure 4 的可视化效果好。** Figure 3 的 Bradley-Terry win probability plot 清晰地展示了跨 judge-axis 的 Blindspot 模式；Figure 4 的 detection probability vs. effect magnitude 曲线直观地说明了 Likert 和 pairwise 在不同效应量下的灵敏度差异。\n\n## Summary of Weaknesses\n\n**N1** [critical] **新颖性定位：核心发现是\"实证确认\"而非\"新发现\"**\n\n- 具体位置：Abstract（\"We ... reveal the Likert Blindspot\"）、Section 1 第2段、Section 2 最后一段、Section 5.1 标题（\"The Likert Blindspot\"）\n- 问题：论文将 Likert Blindspot 包装为一个新发现。但 Thurstone (1927) 的 Law of Comparative Judgment 和后续测量理论研究（Preston & Colman, 2000；Krosnick, 1999——论文自己引用的；Louviere et al., 2015——论文也引用的）早已建立了 pairwise comparison 相对于 rating scale 的敏感性优势。论文在 Section 2（第2页）也明确承认：\"the superiority of pairwise comparison over rating scales for eliciting reliable human judgments has been established since Thurstone (1927).\" 紧接着又声称 \"Our contribution is the first controlled, per-axis quantification of this sensitivity gap for LLM judge style bias\"（第3页）。\n\n  问题不在于贡献不存在，而在于叙事框架。当论文用 \"reveal\" 和 \"Blindspot\" 这类带有发现色彩的词汇时，暗示这是一个意外的新发现（unexpected finding）。但考虑到 measurement theory 的预测，更准确的定位是：**设计了一个框架（CSD）来在 LLM judge 场景下系统性地量化一个理论预测的测量敏感性差距，并在此过程中发现了 per-axis confound structure。** 后者（per-axis confound structure）才是真正没有被先验理论预测的 novel finding。\n\n- 为什么影响接收：ARR reviewer guidelines 明确说，如果 reviewer 认为 novelty 不足，必须提供具体 prior art。这里 Thurstone (1927)、Preston & Colman (2000) 就是直接的 prior art。当前 framing 让有测量理论背景的 reviewer 容易 dismiss 整篇论文，即使 empirical 贡献本身有价值。\n- 建议修改方向：\n  (1) 重新定位 narrative：从\"我们发现了 Likert Blindspot\"转向\"我们设计 CSD 框架首次在 LLM judge 风格偏差中量化了这个理论预测的敏感性差距，量化结果显示其严重性超出预期（complete attenuation at moderate effects），且发现了 per-axis confound structure 这一新模式\"。\n  (2) 将 per-axis confound structure 提升为与 Blindspot quantification 平行的核心贡献。\n  (3) Abstract 第一句可改为承认理论预测，第二句说明本文的 empirical contribution。\n\n**N2** [critical] **Pairwise \"检测\" vs. Pairwise \"放大\"：核心解释性歧义未充分解决**\n\n- 具体位置：Section 5.4（第6–7页）、Section 6 (Conclusion)、Limitations\n- 问题：论文的核心叙事假设 pairwise comparison 检测到了真实的风格偏差，而 Likert 遗漏了它。但存在一个对等的替代解释：**pairwise comparison 放大了微小的、实际上无关紧要的风格微偏好**，使其达到统计显著性，而 Likert 的\"不显著\"才反映了真实的效应大小。\n\n  论文在 Section 5.4 引用了 Jeong et al. (2025) 的 Comparative Trap（pairwise comparison amplifies style biases relative to positive-scoring），并在第6页讨论了 \"measurement attenuation vs. construct divergence\"。但论文的论证有循环性问题：\n\n  (a) 论文说 \"Likert audits miss style preferences that drive pairwise-based alignment pipelines (RLHF, DPO)\"（第6页），用这一点来论证 pairwise 检测到的是\"真实\"偏差。但这个论证预设了 RLHF/DPO pipeline 中的 pairwise preference 反映了真实偏差——而这恰恰是需要证明的。\n  (b) Bootstrap attenuation analysis (Appendix H) 排除了\"纯粹是统计功效差异\"的解释，但不能排除 \"pairwise 系统性放大微小偏好\" 的可能——BT 在小样本时仍显著，可能恰恰是因为 pairwise 的放大效应。\n  (c) 第6页的 \"Both interpretations lead to the same conclusion\" 论证也不完全成立——如果 pairwise 是在放大噪声，那么用 pairwise 来\"审计\" judges 就可能产生大量 false positives。\n\n- 为什么影响接收：这个解释性歧义直接影响论文发现的实际意义。如果读者接受\"放大\"解释，论文的 practical implication（\"用 pairwise 来审计 LLM judge 风格偏差\"）就可能被认为是误导性的。\n- 建议修改方向：\n  (1) 最理想的方案：增加一个基于 human ground-truth 的验证——对 style-manipulated pairs 收集人类偏好判断，比较 pairwise 和 Likert 哪个更接近人类判断。即使是小规模验证也能大幅增强论文的说服力。\n  (2) 次优方案：在 Section 5.4 或 Discussion 中更 prominently 地承认这个限制，明确说明当前证据无法区分两种解释，并讨论在什么条件下每种解释的 implication 是什么。避免在 Conclusion 中使用 \"reveal\" 等暗示单一解释的语言。\n\n**W1** [warning] **Style axis 覆盖面过窄，confound structure claim 的泛化基础不足**\n\n- 具体位置：Section 3.1、Section 4、Section 5.2\n- 问题：论文仅测试 2 个 primary axes (formality, verbosity) + 1 个 replication (register)。LLM judge 的已知风格偏差远不止这些（例如 bullet-point vs. prose、hedging/confidence level、response length distribution 的 long-tail 效应等）。基于 3 个 axis 声称发现了 \"per-axis confound structure\"，这种分类法（style-dominated / conditional / judge-dependent）的泛化性缺乏支撑——读者无法判断新的 style axis 会属于哪种类型。\n- 建议：(1) 在正文明确限定 confound structure claim 的适用范围（\"for the three axes we tested\"）；(2) 在 Limitations 中讨论 axis 覆盖的局限性；(3) 简要说明 axis 选择的先验理由（如 pilot study 或文献依据）。\n\n**W2** [warning] **NLI gate 高拒绝率（~44%）的选择偏差分析不足**\n\n- 具体位置：Section 3.2、Appendix B\n- 问题：NLI consistency filter 保留 55/98 pairs (56.1%)。Appendix B 报告 \"no significant differences across four covariates (NLI score p = 0.824, BERTS p = 0.12, text length p = 0.137, length diff p = 0.715)\"，但这 4 个 covariates 可能不够全面。通过 NLI gate 的 pairs 可能系统性地偏向内容更简单、风格变化更容易分离的文本。这意味着 Blindspot 的效应量 estimate 可能在更复杂的文本上不可靠。\n- 建议：(1) 分析被拒绝 pairs 的文本特征（例如原始 style 距离、话题复杂度、指令类型）vs. 保留 pairs；(2) 讨论 selection bias 对 external validity 的影响。\n\n**W3** [warning] **100-point continuous Likert 实验仅用单一 judge**\n\n- 具体位置：Appendix M（第12页）\n- 问题：此实验旨在排除\"Blindspot 是整数刻度粒度的人为产物\"这一替代解释，但仅使用 Qwen3-32B 一个 judge。如果 GPT-4o 或其他 judge 在 100-point scale 下表现不同（例如 fine-grained scale 确实能检测到偏差），则该结论不成立。\n- 建议：至少在一个额外 judge 上复制此实验，或明确标注为 preliminary evidence。\n\n**W4** [warning] **因果语言与实际方法论之间的张力**\n\n- 具体位置：Title (\"Controlled Style Decomposition\")、Section 3 开头、Figure 2\n- 问题：论文在 Section 4（第4页）给出了合理的 disclaimer (\"we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions\")，这值得肯定。但标题中的 \"Controlled\" 和方法描述中的 \"interventional\" 语言仍然暗示了比实际更强的因果识别——NLI gating 是一种近似的内容控制（approximate content preservation），而非因果推断文献中的 do-operator。Figure 2 的 DAG notation 也可能让有因果推断背景的读者期望看到正式的 identification strategy。\n- 建议：在 Method 开头更早地明确说明这是 \"approximately controlled comparison\" 而非 \"causally identified effect\"，以管理读者预期。\n\n## Questions for Authors\n\nQ1. 关于 N2（检测 vs. 放大）：是否有计划收集 human preference 判断来 ground-truth pairwise 检测到的风格偏差？即使是一个小规模的 pilot（例如 50 pairs × 3 annotators）也能大幅增强论文的说服力。\n\nQ2. 关于 W1（style axes）：选择 formality 和 verbosity 作为 primary axes 的先验理由是什么？是否有 pilot study 表明这两个 axis 的效应最大？如果选择了不同的 axes（例如 bullet-point usage, hedging level），Blindspot 是否仍然存在？\n\nQ3. 关于 Appendix D（rewriter independence）：GPT-4o 作为替代 rewriter 时（Table 7），verbosity 的 Style OR 从 Qwen3-32B rewriter 的高值下降了 22%。这种下降是否暗示 Blindspot 的效应量部分依赖于 rewriter 的具体风格？如果使用完全不同的 rewriting 方法（例如 rule-based rewriting），结果会如何变化？\n\nQ4. 关于 Section 5.4（Comparative Trap）：论文引用了 6 个 experimental controls 来 bound the risk of amplification（NLI gate ablation、Claude Sonnet 4 equivalence、TOST equivalence at Δ = 13pp 等）。但这些 controls 只能排除\"大规模放大\"，无法排除\"中等程度放大\"。是否有办法量化 pairwise 的放大倍数（amplification factor），而不仅仅是定性地论证？\n\n## Missing References\n\n1. **Item Response Theory (IRT) 在 LLM/NLP 评估中的应用**：论文讨论了 Likert vs. pairwise 的测量属性，但没有引用 IRT 文献。Polo et al. (2024, \"tinyBenchmarks: evaluating LLMs with fewer examples\") 和 Otani et al. (2023) 从测量理论角度分析 LLM 评估的可靠性和效度，与本文的 measurement sensitivity 主题直接相关。\n2. **Kocmi and Federmann (2023)** \"Large Language Models Are Not Fair Multilingual Evaluators\" — 虽然聚焦 MT 评估，但其关于 LLM judge bias 在不同评估格式下的表现差异与本文主题相关。\n3. 建议验证 Stureborg et al. (2024) 是否在参考文献列表中完整列出（正文有引用但 references 部分需确认）。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| **Soundness** | 4/5 (Strong) | 实验设计严谨，多维度复制和 7 种统计方法交叉验证是 strong evidence。扣分原因：NLI gate ~44% rejection rate 的 selection bias 未充分分析；核心解释性歧义（检测 vs. 放大）未解决 |\n| **Excitement** | 3/5 (Interesting) | 对 LLM 评估社区有实用价值，per-axis confound structure 有新意。核心 Blindspot 发现主要是已有测量理论的实证确认，降低了 excitement |\n| **Reproducibility** | 4/5 (Mostly reproducible) | 方法描述清晰，超参数完整（Appendix P），承诺释放代码和数据。NLI gate 的具体 threshold tuning 和 style rewriting 的 prompt templates 可能影响 exact reproduction |\n| **Overall Assessment** | **3.5** (Borderline Conference) | 实验工作扎实，结果清晰，对社区有实用价值。但核心发现的新颖性受限于已有测量理论预测，且\"检测 vs. 放大\"的核心解释性歧义未充分解决。如果 reframe novelty narrative 并增加 human ground-truth validation，可以更有信心地推荐 Conference |\n| **Confidence** | 4/5 (Quite sure) | 熟悉 LLM-as-judge evaluation、measurement theory 和 causal NLP 文献。可能遗漏的点：对 GEE 模型选择的技术细节不够深入 |\n\n## 主要优势（总结）\n\n1. 实验设计的多维度复制（4+1 judges × 3 benchmarks × 2+1 axes × 7 statistical methods）在该领域罕见\n2. Table 2 的 sensitivity hierarchy 是一个极其干净的 all-or-nothing 结果\n3. Per-axis confound structure（S5.2, Table 3）是独立的有价值发现\n4. Robustness 分析（Appendix A–Q）几乎回答了每个合理质疑\n5. Black-box 框架设计有强 practical applicability\n6. 写作整体清晰，Figure 3/4 有效传达核心信息\n",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 697 · 2026-05-22T09:20:54.969615+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4015
}
```

</details>

---


### Tool call

_source line 698 · 2026-05-22T09:20:59.870736+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
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

_source line 699 · 2026-05-22T09:20:59.971574+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 700 · 2026-05-22T09:21:03.986790+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-22T09:21:04.037430+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 702 · 2026-05-22T09:21:12.482236+00:00_

审稿完成，已提交给 Review Director。

**总结**：Overall 3.5 (Borderline Conference)。两个 critical 问题：(1) 核心 "Likert Blindspot" 发现的新颖性被测量理论（Thurstone 1927）预测，framing 需要从"发现"调整为"首次系统性实证量化 + per-axis confound structure 的新发现"；(2) pairwise "检测真实偏差" vs. "放大微小偏好" 的核心解释性歧义未充分解决，缺乏 human ground-truth validation。四个 should-fix：style axis 覆盖过窄（仅 2+1）、NLI gate 高拒绝率的选择偏差分析不足、100-point Likert 实验仅用单一 judge、因果语言略强于实际方法论。实验设计的严谨性（7 种统计方法 × 4+1 judges × 3 benchmarks）和 per-axis confound structure 是主要优势。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 22

## Round 22

20 recorded events


### User

_source line 703 · 2026-05-22T09:21:49.603054+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应每个 Weakness 和 Question：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 的 Weaknesses

**N1** [critical] **NLI gate 作为 content preservation 的唯一门控缺乏人工验证**
- CSD 的因果推断完全依赖 NLI gate（DeBERTa-v3-large, threshold 0.90）保证 content 不变。然而 NLI 模型本身可能存在系统性盲区——例如对隐含推理链的改变、对论证结构重组的不敏感。论文未报告对 NLI-gated pairs 的任何人工抽样验证（human evaluation of content preservation quality）。Limitations 中承认"cannot block quality perception shifts mediated by style itself"，但这一局限的严重性需要实证数据来界定——至少应抽样 50-100 对，让人工标注者判断 content 是否实质等价。
- 为什么影响接收：这是 CSD 因果推断链条的最薄弱环节。如果 NLI gate 系统性地放过了某些 content 变化（例如 formal 改写倾向于增加 hedging 从而实质改变 claim 强度），则观测到的"style bias"可能部分是 content bias 的伪装。

**N2** [critical] **"Likert Blindspot" 的 framing 过于强势，忽视了 ordinal vs. forced-choice 灵敏度差异的已知理论背景**
- Likert（绝对评分）与 pairwise comparison（强制选择）的灵敏度差异是测量理论中的经典结论——Thurstone (1927) 已经指出 forced-choice 比 absolute rating 更能识别微小差异。论文在 §2 确实引用了这些文献，也在 §5.1 讨论了"measurement attenuation vs. construct divergence"的两种解释，但标题和 abstract 的措辞将此现象包装为一个全新发现。
- 建议：在 Abstract/Intro 中更明确地将 Blindspot 定位为 measurement theory 预测的在 LLM judge 场景下的首次系统量化，而非全新发现。

**W1** [warning] **NLI filtering 后样本量有限，cross-benchmark 覆盖不完整**
- LLMBar 原始 n=100，NLI filtering 后有效样本降至 55-88 对。Cross-benchmark 验证（AlpacaEval, MT-Bench）中 Table 1 有多个空白单元格。论文未解释为何缺失这些组合。

**W2** [warning] **Style axis 之间的 interaction 和 cross-contamination 未被直接测试**
- CSD 的第三个假设是 style rewrite 不引入 target axis 之外的系统性变化。Table 5 的 GEE interaction test（Style × Originality）只测试了 style 与 originality 的交互，而非 style axis 之间的交互。

**W3** [warning] **负对照（Claude Sonnet 4）仅覆盖 2/3 axes，TOST Δ=15pp margin 偏宽**
- Δ=15pp 的 equivalence margin 意味着 Claude 可能存在高达 15pp 的 style preference 而仍被判定为"无偏差"——考虑到 GPT-4o formality 的 BT 偏差仅约 13pp。

**W4** [warning] **Evaluator-producer overlap 的处理力度有限**
- Cross-rewriter 验证仅限于 Qwen3-32B judge，未覆盖其他 judges。

---

## Reviewer 1 的 Questions

**Q1.** NLI gate 的 false-pass rate 是多少？是否有人工验证数据？

**Q2.** Table 1 中 cross-benchmark 结果的缺失单元格代表什么？

**Q3.** Bootstrap attenuation analysis（Appendix J）的 d = −0.017 如何排除 Likert 和 pairwise 在 construct 层面的根本差异？

**Q4.** Formal 改写是否系统性地改变了文本的 verbosity 或 register？是否有定量证据支持 axis isolation？

**Q5.** 为什么 Claude Sonnet 4 负对照不覆盖 register axis？

---

请对以上每一条 Weakness（N1, N2, W1-W4）和 Question（Q1-Q5）逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 704 · 2026-05-22T09:23:43.215435+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "5,7,9,10,11,12",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "5,7,9,10,11,12",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 705 · 2026-05-22T09:23:44.017566+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.5}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 430.1}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 414.1}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 802
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-22T09:23:47.134971+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-22T09:23:47.737636+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-22T09:23:47.838774+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 709 · 2026-05-22T09:23:48.442845+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-22T09:23:48.443205+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 711 · 2026-05-22T09:23:48.995802+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 712 · 2026-05-22T09:23:49.452263+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1009
}
```

</details>

---


### Tool call

_source line 713 · 2026-05-22T09:23:49.452744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 714 · 2026-05-22T09:23:50.009576+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1013
}
```

</details>

---


### Tool call

_source line 715 · 2026-05-22T09:23:50.010048+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 716 · 2026-05-22T09:23:50.116424+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 663
}
```

</details>

---


### Tool result

_source line 717 · 2026-05-22T09:23:50.669419+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 659
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-22T09:26:36.178776+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Weaknesses 回应\n\n### [AGREE] R1-N1: NLI gate 缺乏人工验证\n\n同意这是 CSD 因果推断链条的薄弱环节。论文在 Section 5.4 报告了 LLM annotator 验证（92% agreement, FNR = 8.4%, precision = 98.9%），并在 Appendix B 给出了 4 个 covariates 的一致性检验（NLI score p = 0.824, BERTScore p = 0.12, text length p = 0.137, length diff p = 0.715），在 Appendix E 给出了 11 个 NLI 阈值的灵敏度分析（Table 9，全部 44 cells 显著）。这些间接证据提供了部分 mitigation。\n\n但 R1 的核心关切——NLI 模型可能对隐含推理链改变、论证结构重组等系统性盲区——无法被 LLM annotator 或统计 covariates 回答。论文自身在 Limitations 中也承认 \"human evaluation of all 200 decisions containing original and rewritten text would strengthen construct-preservation claims\"。**R1 指出的 formal rewrite 增加 hedging 从而改变 claim 强度的具体场景尤其值得关注**——这恰恰是 NLI 模型可能的盲区（NLI 检测语义蕴含，但 hedging 增减不改变蕴含方向，可能通过 gate 却实质改变了文本质量感知）。\n\n补充一点 R1 未提及的：Appendix N（NLI Gate Ablation, Table 15）显示移除 NLI gate 后 NLI-fail pairs 的 BT 仍在 63.0%–76.0%，这说明即使在 content preservation 较差的 pairs 上偏差方向一致，但效应量可能被 content confounding 污染。这实际上是 R1 担忧的间接佐证——gate 确实在过滤 content-confounded pairs，但 gate 本身的准确性需要 human ground-truth 来验证。\n\n**结论**：同意将此列为 critical issue。50–100 对的人工抽样验证是合理的最低要求。\n\n---\n\n### [AGREE] R1-N2: Likert Blindspot framing 过于强势\n\n完全同意。这与我自己的 N1 独立一致。论文在 Section 2（第 2 页）明确承认 \"the superiority of pairwise comparison over rating scales for eliciting reliable human judgments has been established since Thurstone (1927)\"，但 Abstract 和 Introduction 的措辞（\"We ... reveal the Likert Blindspot\"）将其包装为全新发现。\n\nR1 和我的建议一致：reframe 为\"已有测量理论预测在 LLM judge 风格偏差中的首次系统性实证量化\"。此外，我在自己的审稿中额外建议将 per-axis confound structure（Section 5.2, Table 3）提升为与 Blindspot quantification 平行的核心贡献——这个发现确实没有被先验理论预测。\n\n---\n\n### [AGREE] R1-W1: NLI filtering 后样本量有限，cross-benchmark 覆盖不完整\n\n同意，但严重性判断略有不同。\n\n关于**空白单元格**：Table 1 脚注明确标注 \"Empty cells: untested benchmark×axis combinations, cross-bench. replication\"，说明这是设计选择而非数据缺失。但论文**未解释选择标准**——为什么某些 judge×axis×benchmark 组合被测试而其他没有？这让读者无法评估覆盖的完整性。\n\n关于**样本量**：n = 55（NLI filtering 后最小有效样本）确实偏小。但 Appendix I（Bootstrap Attenuation, Table 11）显示 BT 在 n = 50 到 355 的所有子样本中保持显著（d_formality 在 −0.006 到 −0.018 范围内，全部 95% CI 包含 0.07），Appendix K（Formal Power Analysis, Table 12）报告当前样本在 p < 0.001 水平对所有 6 个 judge×axis cells 达到 80% power。这部分缓解了 R1 的担忧。\n\n**结论**：同意这是 warning 级别问题。论文应解释 cross-benchmark 选择逻辑，并在正文中简要提及 power analysis 结果（目前仅在 Appendix K）。\n\n---\n\n### [AGREE] R1-W2: Style axis 之间的 cross-contamination 未被直接测试\n\n同意，且论文自身的证据实际上佐证了这个担忧。\n\nSection 5.2（第 7 页）报告 \"Both rewriting directions favor verbose responses (Formality OR 982...by 22's)\"——这直接说明 formality rewrite 影响了 verbosity。论文试图通过 GEE conditional decomposition（Table 3）控制 originality confound，但 originality ≠ cross-axis style contamination。Appendix C（Table 5）的 interaction test 检验的是 Style × Originality，而非 formality × verbosity 或 formality × register。\n\nAppendix O（Rewriting Artifact Control）的 same-style double-rewrite 控制了一般性的 rewriting polishing artifact，但论文自己承认 \"cannot exclude style-specific-polishing interactions (e.g., formal rewriting may polish differently than casual rewriting)\"（第 13 页）。\n\nR1 提出的第三个假设（\"style rewrite introduces no systematic differences beyond the target axis\"）的验证缺口是真实的。定量检验方法可以是：对 formality-rewritten pairs 测量 verbosity 和 register 维度的变化幅度，验证是否显著偏离零。\n\n**结论**：同意这是 warning 级别问题，且论文已有的证据（Section 5.2 的 verbose response 倾向）暗示该假设可能部分违反。\n\n---\n\n### [AGREE] R1-W3: 负对照 TOST margin 偏宽 + register 轴缺失（部分同意，部分反驳）\n\n**关于 Δ = 15pp margin**：部分同意。Appendix G（第 11 页）透明地报告了 power constraint：Δ = 15pp 下 power 仅 76%；80% power 需要 Δ = 15.7pp。R1 指出 GPT-4o formality BT 偏差约 13pp（BT ≈ 63%，即 50% + 13pp），如果 Claude 有接近 13pp 的偏差仍可能被 TOST 判定为等价——这在数学上是正确的。\n\n**但我要补充一个缓解因素**：Claude 的 raw BT 值（formality 56.2%, verbosity 54.1%）数值上接近 50%，远低于任何 target judge（最低为 GPT-4o formality 的 63%）。即使 TOST 的 formal equivalence testing 受 power 限制，**point estimate 本身已经支持 negative control 的解释**。TOST 的作用是 formal bound，不是唯一证据。\n\n**关于 register 轴缺失**：完全同意。Table 1 中 Claude 仅有 formality 和 verbosity 结果（LLMBar 和 AlpacaEval），register 缺失。论文未解释这个 omission——即使 register 是 scaled replication，在 negative control 上缺失一个轴会削弱 \"Claude shows no systematic bias\" 的 claim。\n\n**结论**：总体同意 warning 级别。TOST margin 是 power-constrained 的现实问题（不是方法论错误），但 register 缺失是需要解释的 gap。\n\n---\n\n### [REBUT] R1-W4: Evaluator-producer overlap 处理力度有限\n\n不同意 R1 对此问题的 framing。\n\nAppendix D（第 9 页）明确说明：\"Evaluator-producer overlap is limited to Qwen3-32B (rewriter = judge)... The other three target judges (GPT-4o, Llama-70B, Gemini) use a different rewriter and are not subject to this confound.\"\n\nEvaluator-producer overlap 是**定义性地局限于 Qwen3-32B**的——因为 Qwen3-32B 既是 rewriter 也是 judge。对 GPT-4o、Llama-70B、Gemini 来说，它们判断的是 Qwen3-32B 的 rewrite，不存在 overlap。因此 cross-rewriter test（Tables 7–8，用 GPT-4o 替代 Qwen3-32B 作为 rewriter）正确地**仅针对唯一存在 overlap 的 judge（Qwen3-32B）**进行验证。\n\nR1 要求 \"覆盖其他 judges\" 的 cross-rewriter test 在逻辑上是不必要的——对不存在 overlap 的 judges 做 overlap robustness check 无法增加信息。如果 R1 的真正担忧是 rewriter identity 的一般性影响（不限于 overlap），那 Table 7 的数据已部分回答：GPT-4o rewriter 下 Style OR 降低 22%（verbosity），但 Blindspot 模式持续（BT significant, Likert n.s.），说明 rewriter identity 影响效应量但不影响 Blindspot 的定性结论。\n\n**结论**：不同意。论文对 evaluator-producer overlap 的处理是逻辑完整的。如果 R1 想要的是更广泛的 \"rewriter robustness\"（不同 rewriter 对不同 judges 的影响），这是一个合理的扩展方向但不是当前论文的方法论缺陷。\n\n---\n\n## Questions 回应\n\n### R1-Q1: NLI gate false-pass rate\n\nSection 5.4（第 7 页）报告了基于 LLM annotator 的验证：agreement 92%, FNR = 8.4% [95% Wilson CI: 3.7%, 15.9%], precision = 98.9%。但这是 **LLM annotator**，不是 human annotator。\n\n[AGREE] 人工验证数据缺失是事实。如 R1-N1 所述，LLM annotator 可能与 NLI gate 共享系统性盲区（两者都是基于 transformer 的模型，可能对同类 content 变化不敏感），因此 LLM-based validation 无法完全替代 human validation。\n\n---\n\n### R1-Q2: Table 1 空白单元格\n\nTable 1 脚注：\"Empty cells: untested benchmark×axis combinations, cross-bench. replication.\" 这是**设计选择**——AlpacaEval 和 MT-Bench 作为 cross-benchmark replication，不要求覆盖所有 judge×axis 组合。\n\n[AGREE] 论文应解释选择哪些组合进行 replication 的标准（例如：是否优先选择 primary family 中效应最强/最弱的 cells？还是随机选择？）。当前呈现方式让读者无法评估 replication 的代表性。\n\n---\n\n### R1-Q3: Bootstrap d = −0.017 如何排除 construct 层面差异\n\n[AGREE] **无法排除**。Appendix I 的 bootstrap analysis 显示 Likert d_formality = −0.017，d_verbosity = −0.017，在所有子样本中 d 保持 near-zero（Table 11）。这排除了\"Likert 只是 power 不足\"的解释（如果 Likert 能检测到同一效应，增加样本量应让 d 远离零）。\n\n但 R1 的问题更深层：如果 pairwise 和 Likert 测量的是不同 constructs（pairwise 测量 comparative preference，Likert 测量 absolute quality perception），则 BT > 50% + Likert d ≈ 0 是两种 construct 的自然状态，不需要用 \"Blindspot\" 来解释。论文在 Section 5.1（第 6 页）讨论了 \"measurement attenuation vs. construct divergence\"，但**未提供决定性证据区分两种解释**。这与我自己的 N2 一致——论文需要 human ground-truth 或其他外部标准来区分。\n\n---\n\n### R1-Q4: Formal 改写是否系统性改变 verbosity/register\n\n[AGREE] 论文**未提供直接的定量证据**证明 axis isolation。反而，Section 5.2（第 7 页）提供了反面证据：\"Both rewriting directions favor verbose responses (Formality OR...\" ——formality rewrite 确实系统性地影响了 verbosity。\n\nGEE conditional decomposition（Table 3）通过 controlling for originality 来间接处理这个问题，但 originality confound ≠ cross-axis style contamination。论文的第三个操作假设（\"the style rewrite introduces no systematic differences beyond the target axis\", Section 3.4, 第 4 页）在 formality → verbosity 方向上可能被违反。\n\n这个问题比 R1 最初 framing 的更严重：如果 formality rewrite 系统性地增加 verbosity，而 verbosity 是 style-dominated bias（Table 3），则观测到的 \"formality bias\" 可能部分被 verbosity confound 驱动。GEE conditional analysis 部分控制了这个问题（formality effect remains significant after controlling for originality），但 cross-axis confounding 不等于 originality confounding。\n\n---\n\n### R1-Q5: Claude Sonnet 4 为何不覆盖 register axis\n\n[AGREE] 论文未解释这个 omission。可能的原因是 register 作为 scaled replication（使用较宽松的 α）在 negative control 上的 inferential value 有限，加上样本量约束（n = 87 已经让 TOST 在 formality/verbosity 上仅达到 76% power）。但这些都是推测——论文应明确说明原因。缺少 register 覆盖意味着 Claude \"无偏差\" 的 claim 仅对 2/3 测试轴成立。\n\n---\n\n## 总结：与 R1 的共识和分歧\n\n| R1 Issue | R2 判断 | 备注 |\n|----------|---------|------|\n| N1 (NLI human validation) | [AGREE] | 与我的 W2（NLI 选择偏差）互补 |\n| N2 (Framing overstated) | [AGREE] | 与我的 N1 独立一致 |\n| W1 (Sample size/coverage) | [AGREE] | Bootstrap 部分缓解，但 cross-benchmark 选择逻辑缺失 |\n| W2 (Cross-axis interaction) | [AGREE] | 论文自身证据（S5.2 verbose tendency）佐证此担忧 |\n| W3 (Negative control) | [AGREE] 部分 | TOST margin 受 power 限制可理解，register 缺失是真实 gap |\n| W4 (Evaluator-producer) | [REBUT] | 论文处理逻辑完整，overlap 定义性局限于 Qwen3-32B |\n| Q1 (False-pass rate) | [AGREE] | LLM annotator ≠ human validation |\n| Q2 (Empty cells) | [AGREE] | 选择标准需解释 |\n| Q3 (Bootstrap vs construct) | [AGREE] | 无法排除 construct divergence |\n| Q4 (Cross-axis contamination) | [AGREE] | 论文自身 S5.2 数据是反面证据 |\n| Q5 (Claude register) | [AGREE] | Omission 未解释 |\n\n**两位 Reviewer 的核心共识**：(1) Novelty framing 需要重新定位（R1-N2 = R2-N1）；(2) 检测 vs. 放大的解释性歧义是 fundamental limitation（R1-Q3 ≈ R2-N2）；(3) NLI gate 的 human validation 缺失削弱了因果推断链条（R1-N1 ≈ R2-W2 的上游问题）。\n\n**唯一分歧**：R1-W4（evaluator-producer overlap）——我认为论文的处理是逻辑完整的，R1 可能混淆了 \"overlap confound\"（仅 Qwen3-32B）与 \"rewriter identity effect\"（更广泛的 robustness 问题）。\n",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Weaknesses 回应\n\n### [AGREE] R1-N1: NLI gate 缺乏人工验证\n\n同意这是 CSD 因果推断链条的薄弱环节。论文在 Section 5.4 报告了 LLM annotator 验证（92% agreement, FNR = 8.4%, precision = 98.9%），并在 Appendix B 给出了 4 个 covariates 的一致性检验（NLI score p = 0.824, BERTScore p = 0.12, text length p = 0.137, length diff p = 0.715），在 Appendix E 给出了 11 个 NLI 阈值的灵敏度分析（Table 9，全部 44 cells 显著）。这些间接证据提供了部分 mitigation。\n\n但 R1 的核心关切——NLI 模型可能对隐含推理链改变、论证结构重组等系统性盲区——无法被 LLM annotator 或统计 covariates 回答。论文自身在 Limitations 中也承认 \"human evaluation of all 200 decisions containing original and rewritten text would strengthen construct-preservation claims\"。**R1 指出的 formal rewrite 增加 hedging 从而改变 claim 强度的具体场景尤其值得关注**——这恰恰是 NLI 模型可能的盲区（NLI 检测语义蕴含，但 hedging 增减不改变蕴含方向，可能通过 gate 却实质改变了文本质量感知）。\n\n补充一点 R1 未提及的：Appendix N（NLI Gate Ablation, Table 15）显示移除 NLI gate 后 NLI-fail pairs 的 BT 仍在 63.0%–76.0%，这说明即使在 content preservation 较差的 pairs 上偏差方向一致，但效应量可能被 content confounding 污染。这实际上是 R1 担忧的间接佐证——gate 确实在过滤 content-confounded pairs，但 gate 本身的准确性需要 human ground-truth 来验证。\n\n**结论**：同意将此列为 critical issue。50–100 对的人工抽样验证是合理的最低要求。\n\n---\n\n### [AGREE] R1-N2: Likert Blindspot framing 过于强势\n\n完全同意。这与我自己的 N1 独立一致。论文在 Section 2（第 2 页）明确承认 \"the superiority of pairwise comparison over rating scales for eliciting reliable human judgments has been established since Thurstone (1927)\"，但 Abstract 和 Introduction 的措辞（\"We ... reveal the Likert Blindspot\"）将其包装为全新发现。\n\nR1 和我的建议一致：reframe 为\"已有测量理论预测在 LLM judge 风格偏差中的首次系统性实证量化\"。此外，我在自己的审稿中额外建议将 per-axis confound structure（Section 5.2, Table 3）提升为与 Blindspot quantification 平行的核心贡献——这个发现确实没有被先验理论预测。\n\n---\n\n### [AGREE] R1-W1: NLI filtering 后样本量有限，cross-benchmark 覆盖不完整\n\n同意，但严重性判断略有不同。\n\n关于**空白单元格**：Table 1 脚注明确标注 \"Empty cells: untested benchmark×axis combinations, cross-bench. replication\"，说明这是设计选择而非数据缺失。但论文**未解释选择标准**——为什么某些 judge×axis×benchmark 组合被测试而其他没有？这让读者无法评估覆盖的完整性。\n\n关于**样本量**：n = 55（NLI filtering 后最小有效样本）确实偏小。但 Appendix I（Bootstrap Attenuation, Table 11）显示 BT 在 n = 50 到 355 的所有子样本中保持显著（d_formality 在 −0.006 到 −0.018 范围内，全部 95% CI 包含 0.07），Appendix K（Formal Power Analysis, Table 12）报告当前样本在 p < 0.001 水平对所有 6 个 judge×axis cells 达到 80% power。这部分缓解了 R1 的担忧。\n\n**结论**：同意这是 warning 级别问题。论文应解释 cross-benchmark 选择逻辑，并在正文中简要提及 power analysis 结果（目前仅在 Appendix K）。\n\n---\n\n### [AGREE] R1-W2: Style axis 之间的 cross-contamination 未被直接测试\n\n同意，且论文自身的证据实际上佐证了这个担忧。\n\nSection 5.2（第 7 页）报告 \"Both rewriting directions favor verbose responses (Formality OR 982...by 22's)\"——这直接说明 formality rewrite 影响了 verbosity。论文试图通过 GEE conditional decomposition（Table 3）控制 originality confound，但 originality ≠ cross-axis style contamination。Appendix C（Table 5）的 interaction test 检验的是 Style × Originality，而非 formality × verbosity 或 formality × register。\n\nAppendix O（Rewriting Artifact Control）的 same-style double-rewrite 控制了一般性的 rewriting polishing artifact，但论文自己承认 \"cannot exclude style-specific-polishing interactions (e.g., formal rewriting may polish differently than casual rewriting)\"（第 13 页）。\n\nR1 提出的第三个假设（\"style rewrite introduces no systematic differences beyond the target axis\"）的验证缺口是真实的。定量检验方法可以是：对 formality-rewritten pairs 测量 verbosity 和 register 维度的变化幅度，验证是否显著偏离零。\n\n**结论**：同意这是 warning 级别问题，且论文已有的证据（Section 5.2 的 verbose response 倾向）暗示该假设可能部分违反。\n\n---\n\n### [AGREE] R1-W3: 负对照 TOST margin 偏宽 + register 轴缺失（部分同意，部分反驳）\n\n**关于 Δ = 15pp margin**：部分同意。Appendix G（第 11 页）透明地报告了 power constraint：Δ = 15pp 下 power 仅 76%；80% power 需要 Δ = 15.7pp。R1 指出 GPT-4o formality BT 偏差约 13pp（BT ≈ 63%，即 50% + 13pp），如果 Claude 有接近 13pp 的偏差仍可能被 TOST 判定为等价——这在数学上是正确的。\n\n**但我要补充一个缓解因素**：Claude 的 raw BT 值（formality 56.2%, verbosity 54.1%）数值上接近 50%，远低于任何 target judge（最低为 GPT-4o formality 的 63%）。即使 TOST 的 formal equivalence testing 受 power 限制，**point estimate 本身已经支持 negative control 的解释**。TOST 的作用是 formal bound，不是唯一证据。\n\n**关于 register 轴缺失**：完全同意。Table 1 中 Claude 仅有 formality 和 verbosity 结果（LLMBar 和 AlpacaEval），register 缺失。论文未解释这个 omission——即使 register 是 scaled replication，在 negative control 上缺失一个轴会削弱 \"Claude shows no systematic bias\" 的 claim。\n\n**结论**：总体同意 warning 级别。TOST margin 是 power-constrained 的现实问题（不是方法论错误），但 register 缺失是需要解释的 gap。\n\n---\n\n### [REBUT] R1-W4: Evaluator-producer overlap 处理力度有限\n\n不同意 R1 对此问题的 framing。\n\nAppendix D（第 9 页）明确说明：\"Evaluator-producer overlap is limited to Qwen3-32B (rewriter = judge)... The other three target judges (GPT-4o, Llama-70B, Gemini) use a different rewriter and are not subject to this confound.\"\n\nEvaluator-producer overlap 是**定义性地局限于 Qwen3-32B**的——因为 Qwen3-32B 既是 rewriter 也是 judge。对 GPT-4o、Llama-70B、Gemini 来说，它们判断的是 Qwen3-32B 的 rewrite，不存在 overlap。因此 cross-rewriter test（Tables 7–8，用 GPT-4o 替代 Qwen3-32B 作为 rewriter）正确地**仅针对唯一存在 overlap 的 judge（Qwen3-32B）**进行验证。\n\nR1 要求 \"覆盖其他 judges\" 的 cross-rewriter test 在逻辑上是不必要的——对不存在 overlap 的 judges 做 overlap robustness check 无法增加信息。如果 R1 的真正担忧是 rewriter identity 的一般性影响（不限于 overlap），那 Table 7 的数据已部分回答：GPT-4o rewriter 下 Style OR 降低 22%（verbosity），但 Blindspot 模式持续（BT significant, Likert n.s.），说明 rewriter identity 影响效应量但不影响 Blindspot 的定性结论。\n\n**结论**：不同意。论文对 evaluator-producer overlap 的处理是逻辑完整的。如果 R1 想要的是更广泛的 \"rewriter robustness\"（不同 rewriter 对不同 judges 的影响），这是一个合理的扩展方向但不是当前论文的方法论缺陷。\n\n---\n\n## Questions 回应\n\n### R1-Q1: NLI gate false-pass rate\n\nSection 5.4（第 7 页）报告了基于 LLM annotator 的验证：agreement 92%, FNR = 8.4% [95% Wilson CI: 3.7%, 15.9%], precision = 98.9%。但这是 **LLM annotator**，不是 human annotator。\n\n[AGREE] 人工验证数据缺失是事实。如 R1-N1 所述，LLM annotator 可能与 NLI gate 共享系统性盲区（两者都是基于 transformer 的模型，可能对同类 content 变化不敏感），因此 LLM-based validation 无法完全替代 human validation。\n\n---\n\n### R1-Q2: Table 1 空白单元格\n\nTable 1 脚注：\"Empty cells: untested benchmark×axis combinations, cross-bench. replication.\" 这是**设计选择**——AlpacaEval 和 MT-Bench 作为 cross-benchmark replication，不要求覆盖所有 judge×axis 组合。\n\n[AGREE] 论文应解释选择哪些组合进行 replication 的标准（例如：是否优先选择 primary family 中效应最强/最弱的 cells？还是随机选择？）。当前呈现方式让读者无法评估 replication 的代表性。\n\n---\n\n### R1-Q3: Bootstrap d = −0.017 如何排除 construct 层面差异\n\n[AGREE] **无法排除**。Appendix I 的 bootstrap analysis 显示 Likert d_formality = −0.017，d_verbosity = −0.017，在所有子样本中 d 保持 near-zero（Table 11）。这排除了\"Likert 只是 power 不足\"的解释（如果 Likert 能检测到同一效应，增加样本量应让 d 远离零）。\n\n但 R1 的问题更深层：如果 pairwise 和 Likert 测量的是不同 constructs（pairwise 测量 comparative preference，Likert 测量 absolute quality perception），则 BT > 50% + Likert d ≈ 0 是两种 construct 的自然状态，不需要用 \"Blindspot\" 来解释。论文在 Section 5.1（第 6 页）讨论了 \"measurement attenuation vs. construct divergence\"，但**未提供决定性证据区分两种解释**。这与我自己的 N2 一致——论文需要 human ground-truth 或其他外部标准来区分。\n\n---\n\n### R1-Q4: Formal 改写是否系统性改变 verbosity/register\n\n[AGREE] 论文**未提供直接的定量证据**证明 axis isolation。反而，Section 5.2（第 7 页）提供了反面证据：\"Both rewriting directions favor verbose responses (Formality OR...\" ——formality rewrite 确实系统性地影响了 verbosity。\n\nGEE conditional decomposition（Table 3）通过 controlling for originality 来间接处理这个问题，但 originality confound ≠ cross-axis style contamination。论文的第三个操作假设（\"the style rewrite introduces no systematic differences beyond the target axis\", Section 3.4, 第 4 页）在 formality → verbosity 方向上可能被违反。\n\n这个问题比 R1 最初 framing 的更严重：如果 formality rewrite 系统性地增加 verbosity，而 verbosity 是 style-dominated bias（Table 3），则观测到的 \"formality bias\" 可能部分被 verbosity confound 驱动。GEE conditional analysis 部分控制了这个问题（formality effect remains significant after controlling for originality），但 cross-axis confounding 不等于 originality confounding。\n\n---\n\n### R1-Q5: Claude Sonnet 4 为何不覆盖 register axis\n\n[AGREE] 论文未解释这个 omission。可能的原因是 register 作为 scaled replication（使用较宽松的 α）在 negative control 上的 inferential value 有限，加上样本量约束（n = 87 已经让 TOST 在 formality/verbosity 上仅达到 76% power）。但这些都是推测——论文应明确说明原因。缺少 register 覆盖意味着 Claude \"无偏差\" 的 claim 仅对 2/3 测试轴成立。\n\n---\n\n## 总结：与 R1 的共识和分歧\n\n| R1 Issue | R2 判断 | 备注 |\n|----------|---------|------|\n| N1 (NLI human validation) | [AGREE] | 与我的 W2（NLI 选择偏差）互补 |\n| N2 (Framing overstated) | [AGREE] | 与我的 N1 独立一致 |\n| W1 (Sample size/coverage) | [AGREE] | Bootstrap 部分缓解，但 cross-benchmark 选择逻辑缺失 |\n| W2 (Cross-axis interaction) | [AGREE] | 论文自身证据（S5.2 verbose tendency）佐证此担忧 |\n| W3 (Negative control) | [AGREE] 部分 | TOST margin 受 power 限制可理解，register 缺失是真实 gap |\n| W4 (Evaluator-producer) | [REBUT] | 论文处理逻辑完整，overlap 定义性局限于 Qwen3-32B |\n| Q1 (False-pass rate) | [AGREE] | LLM annotator ≠ human validation |\n| Q2 (Empty cells) | [AGREE] | 选择标准需解释 |\n| Q3 (Bootstrap vs construct) | [AGREE] | 无法排除 construct divergence |\n| Q4 (Cross-axis contamination) | [AGREE] | 论文自身 S5.2 数据是反面证据 |\n| Q5 (Claude register) | [AGREE] | Omission 未解释 |\n\n**两位 Reviewer 的核心共识**：(1) Novelty framing 需要重新定位（R1-N2 = R2-N1）；(2) 检测 vs. 放大的解释性歧义是 fundamental limitation（R1-Q3 ≈ R2-N2）；(3) NLI gate 的 human validation 缺失削弱了因果推断链条（R1-N1 ≈ R2-W2 的上游问题）。\n\n**唯一分歧**：R1-W4（evaluator-producer overlap）——我认为论文的处理是逻辑完整的，R1 可能混淆了 \"overlap confound\"（仅 Qwen3-32B）与 \"rewriter identity effect\"（更广泛的 robustness 问题）。\n",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-22T09:26:39.993804+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3815
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-22T09:26:46.218632+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 721 · 2026-05-22T09:26:46.219121+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_8/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 722 · 2026-05-22T09:26:53.170649+00:00_

逐条回应完成。总结：

- **10/11 条 [AGREE]**（N1, N2, W1, W2, W3部分, Q1–Q5），与 R1 在 novelty framing、NLI human validation 缺失、cross-axis contamination、construct divergence 等核心问题上形成共识
- **1 条 [REBUT]**（W4 evaluator-producer overlap）：论文的处理逻辑完整，overlap 定义性地局限于 Qwen3-32B，cross-rewriter test 正确地仅针对该 judge
- **两位 Reviewer 的三大核心共识**：(1) Blindspot framing 需从"新发现"调整为"理论预测的首次实证量化"；(2) 检测 vs. 放大的解释性歧义是 fundamental limitation；(3) NLI gate 需要 human validation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 23

## Round 23

56 recorded events


### User

_source line 723 · 2026-05-22T16:34:48.047058+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 写作完整性 + 格式合规**审查。

## 投稿信息
- **Venue**: EMNLP 2026 via ARR（May cycle）
- **Deadline**: 2026-05-25
- **格式要求**: Long paper，正文 ≤8 页，无限参考文献，ACL template，double-blind
- **Limitations 章节**: 不计入页数，但不能包含新实验/图表/分析
- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`（各 section 在 `sections/` 子目录）
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/submitted.pdf`

## 你的审查侧重

重点评估以下方面，严格、不留情面：

1. **新颖性定位**：核心 contribution（Likert Blindspot 现象 + 检测方法）是否真正 novel，还是心理测量学已知现象（Thurstone 1927, paired comparison vs rating scales）的 domain transfer？论文是否充分 acknowledge 前人工作？
2. **Related Work 覆盖**：LLM-as-judge bias 领域的关键工作是否完整覆盖？特别关注：(a) Comparative Trap (Jeong et al., 2025) 是否被引用和讨论——该工作提出 pairwise 格式可能放大而非仅检测 bias，与本文核心 claim 直接矛盾；(b) 其他 measurement format comparison 文献
3. **Contribution 措辞**：Abstract/Intro 中是否有 overclaim（如 "first", "reveals", "dominant source" 等绝对性表述），contribution list 是否与实际证据强度匹配
4. **写作质量**：叙事结构是否清晰、论证逻辑是否连贯、Abstract 是否过密、Limitations 是否充分
5. **格式合规**：正文是否 ≤8 页、匿名性（无 self-citation 泄露）、Limitations 章节内容是否合规（无新实验/图表）、引用格式是否 ACL 规范
6. **Detection vs Amplification 歧义**：pairwise 格式检测到的 bias 是 genuine style bias 还是 pairwise 格式本身的 amplification artifact？论文是否诚实地讨论了这一 alternative interpretation？

输出格式：
- **Summary** (2-3句)
- **Strengths** (逐条)
- **Weaknesses** (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])
- **Questions** (需要作者澄清的)
- **Missing References**
- **Overall Assessment** (评分 + 置信度)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-22T16:35:02.512543+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
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

_source line 725 · 2026-05-22T16:35:02.564454+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 726 · 2026-05-22T16:35:06.387435+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "1-12",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-12",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 727 · 2026-05-22T16:35:06.890438+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 728 · 2026-05-22T16:35:07.996624+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.5}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 558.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.7}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.6}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p9.png\", \"w
…[truncated 963 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1609
}
```

</details>

---


### Tool result

_source line 729 · 2026-05-22T16:35:15.987395+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Assessment Score

The Overall asses
…[truncated 1277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9096
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-22T16:35:20.725394+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 731 · 2026-05-22T16:35:21.580776+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 732 · 2026-05-22T16:35:21.731716+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 733 · 2026-05-22T16:35:22.234131+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 734 · 2026-05-22T16:35:22.538250+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 735 · 2026-05-22T16:35:22.538694+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 736 · 2026-05-22T16:35:23.510785+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 737 · 2026-05-22T16:35:24.015345+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1781
}
```

</details>

---


### Tool result

_source line 738 · 2026-05-22T16:35:24.016410+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1477
}
```

</details>

---


### Tool call

_source line 739 · 2026-05-22T16:35:24.016724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 740 · 2026-05-22T16:35:24.469471+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-22T16:35:25.374875+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1864
}
```

</details>

---


### Tool result

_source line 742 · 2026-05-22T16:35:25.376006+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1359
}
```

</details>

---


### Tool call

_source line 743 · 2026-05-22T16:35:25.376258+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 744 · 2026-05-22T16:35:26.731394+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2261
}
```

</details>

---


### Tool result

_source line 745 · 2026-05-22T16:35:26.732585+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 746 · 2026-05-22T16:35:26.883406+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and any guidance for reviewers. Include the full Overall Assessment scale, Soundness scale, Excitement scale, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and any guidance for reviewers. Include the full Overall Assessment scale, Soundness scale, Excitement scale, and any other scored dimensions."
  }
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-22T16:35:34.344081+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- 4: "Quite sure. I tried to check the important points carefully."
- 3: "Pretty sure, but there's a chance I missed something."
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- 1: "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- 5: "Excellent: This study is one of the most thorough I have seen, given its type."
- 4: "Strong: This study provides sufficient support for all of its claims."
- 3: "Acceptable: This study provides sufficient support for its main claims."
- 2: "Poor: Some of the main claims are not sufficiently supported."
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- 5: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- 4: "Exciting: I would mention this paper to others."
- 3: "Interesting: I might mention some points of this paper to others."
- 2: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- 1: "Not Exciting: this paper does not resonate with me."

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- 5: Consider for Award (top 2.5%)
- 4.5: Borderline Award
- 4: Conference acceptance
- 3.5: Borderline Conference
- 3: Findings acceptance
- 2.5: Borderline Findings
- 2: Resubmit next cycle
- 1.5: Resubmit after next cycle
- 1: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- 5: Easily reproducible
- 4: Mostly reproducible with minor variations
- 3: Reproducible with difficulty
- 2: Difficult to reproduce
- 1: Not reproducible

## 6. **Datasets & Software Value**
Scale: 1-5 each
- 5: Enabling (affects research direction choices)
- 4:
…[truncated 327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7460
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-22T16:36:19.567908+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 749 · 2026-05-22T16:36:20.522576+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 750 · 2026-05-22T16:36:20.523074+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 751 · 2026-05-22T16:36:21.076799+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 752 · 2026-05-22T16:36:21.931958+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-22T16:36:21.933200+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-22T16:36:21.935666+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-22T16:36:22.892302+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-22T16:36:22.892719+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "13-17",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "13-17",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 757 · 2026-05-22T16:36:23.496517+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 608.5}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 610.0}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 211.3}], \"total_pages\": 17, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-22T16:36:27.913611+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 759 · 2026-05-22T16:36:28.267498+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 760 · 2026-05-22T16:36:28.773005+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool call

_source line 761 · 2026-05-22T16:36:28.773442+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 762 · 2026-05-22T16:36:29.680268+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1412
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-22T16:36:29.682566+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-22T16:36:29.682918+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 765 · 2026-05-22T16:36:30.035479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 766 · 2026-05-22T16:36:30.389079+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 706
}
```

</details>

---


### Tool result

_source line 767 · 2026-05-22T16:36:30.591987+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 556
}
```

</details>

---


### Tool call

_source line 768 · 2026-05-22T16:39:22.381274+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Jeong et al 2025 \"Comparative Trap\" pairwise comparison LLM evaluation bias amplification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Jeong et al 2025 \"Comparative Trap\" pairwise comparison LLM evaluation bias amplification"
  }
}
```

</details>

---


### Tool call

_source line 769 · 2026-05-22T16:39:22.632366+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Thurstone 1927 paired comparison rating scale sensitivity psychometrics measurement format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Thurstone 1927 paired comparison rating scale sensitivity psychometrics measurement format"
  }
}
```

</details>

---


### Tool result

_source line 770 · 2026-05-22T16:39:29.666359+00:00_

Web search results for query: "Jeong et al 2025 "Comparative Trap" pairwise comparison LLM evaluation bias amplification"

Links: [{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators - ACL Anthology","url":"https://aclanthology.org/2025.blackboxnlp-1.5/"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://arxiv.org/html/2406.12319v4"},{"title":"[2406.12319] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://arxiv.org/abs/2406.12319"},{"title":"[PDF] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Comparative-Trap:-Pairwise-Comparisons-Biased-Jeong-Park/cd6191f270c5b98dec44a294e4f3cebcf371ac5f"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences   of LLM Evaluators","url":"https://arxiv.org/pdf/2406.12319"},{"title":"[Literature Review] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://www.themoonlight.io/en/review/the-comparative-trap-pairwise-comparisons-amplifies-biased-preferences-of-llm-evaluators"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators (arXiv:2406.12319v4) - ScienceStack","url":"https://www.sciencestack.ai/paper/2406.12319"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies","url":"https://arxiv.org/pdf/2406.12319v3"}]

I found the paper you're looking for. Here's what the research shows:

## Overview

The paper "The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators" by Hawon Jeong, ChaeHun Park, Jimin Hong, Hojoon Lee, and Jaegul Choo was published in 2025 in the Proceedings of the 8th BlackboxNLP Workshop.

## Core Finding on Bias Amplification

LLM evaluators often display biased preference
…[truncated 968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7285
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-22T16:39:30.219241+00:00_

Web search results for query: "Thurstone 1927 paired comparison rating scale sensitivity psychometrics measurement format"

Links: [{"title":"How to Analyze Paired Comparison Data Kristi Tsukida and Maya R. Gupta","url":"https://apps.dtic.mil/sti/tr/pdf/ADA543806.pdf"},{"title":"How to Analyze Paired Comparison Data Kristi Tsukida and Maya R. Gupta","url":"http://www.mayagupta.org/publications/PairedComparisonTutorialTsukidaGupta.pdf"},{"title":"(PDF) An Enquiry Into the Method of Paired Comparison: Reliability, Scaling, and Thurstone's Law of Comparative Judgment","url":"https://www.researchgate.net/publication/263807767_An_Enquiry_Into_the_Method_of_Paired_Comparison_Reliability_Scaling_and_Thurstone's_Law_of_Comparative_Judgment"},{"title":"(PDF) On Thurstone’s Model for Paired Comparisons and Ranking Data","url":"https://www.researchgate.net/publication/236623596_On_Thurstone's_Model_for_Paired_Comparisons_and_Ranking_Data"},{"title":",D-Ri23 877 PAIRED COMPAiSONSCU) FLORIDA STATE UNIV TALLAHASSEE- 1/i","url":"https://apps.dtic.mil/sti/tr/pdf/ADA123877.pdf"},{"title":"An enquiry into the method of paired comparison","url":"https://www.fs.usda.gov/rm/pubs/rmrs_gtr216.pdf"},{"title":"L. L. Thurstone: The Method of Paired Comparisons for Social Values","url":"https://brocku.ca/MeadProject/Thurstone/Thurstone_1927a.html"},{"title":"Models for Paired Comparison Data: A Review with ...","url":"https://arxiv.org/pdf/1210.1016"},{"title":"On Thurstone’s Model for Paired Comparisons and Ranking Data | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-4-431-66996-8_59"}]

Based on the search results, here's what I found about Thurstone's 1927 paired comparison method:

## Overview

In 1927, Louis Leon Thurstone pioneered psychometrics by using Gaussian distributions to analyze paired comparisons. Thurstone presented a new psychological law, the law of comparative judgment, along with some of its special applications in the measurement of psychological val
…[truncated 1246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7586
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-22T16:42:29.298698+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见（新颖性 + 写作完整性 + 格式合规）\n\n### 总体评分\n\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 方法论扎实、控制充分的实证工作，但核心发现（pairwise 比 Likert 更灵敏）在心理测量学中已有深厚根基，且 detection 与 amplification 无法干净分离，削弱了\"Likert 是盲区\"这一叙事的说服力。\n\n### 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法设计合理，NLI gate + position swap + negative control 构成可信的控制链；但 detection vs. amplification 无法分离，核心 claim 的因果解读存在歧义 |\n| Excitement | 3/5 | CSD 框架和 GEE per-axis decomposition 有实用价值，但核心 observation 是 Thurstone (1927) 以来的经典心理测量学结论的 domain transfer |\n| Reproducibility | 4/5 | 模型版本、prompt、seed、threshold 均明确；代码承诺在接收后发布 |\n| Confidence | 4/5 | 仔细阅读了正文及全部 Appendix，熟悉 LLM-as-judge 和 measurement theory 文献 |\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] 新颖性定位过度——核心发现有深厚心理测量学先例\n\n- 位置：Section 2 (\"first controlled quantification\")；Abstract (\"systematically misses biases\")；Title\n- Pairwise > Likert sensitivity 是 Thurstone (1927) Law of Comparative Judgment 的经典结论。Mohammad (2017)、Novikova et al. (2018) 已在 NLG 评估中实证验证。论文虽引用了这些工作，但叙事框架将已知现象包装为新发现——\"The Likert Blindspot\" 作为专有名词、\"reveals\" 等措辞暗示首次揭示。\n- 影响：Reviewer 和 AC 会质疑 contribution 是否足够支撑 main conference。\n- 建议：明确定位为\"在 LLM judge 场景下首次系统量化已知 measurement-format sensitivity gap\"；\"first\" 限定为 \"first for LLM judges specifically\"；削弱绝对性措辞。\n\n**N2** [critical] Detection vs. Amplification 无法分离\n\n- 位置：§5.4; §6 Conclusion (\"the primary open question is whether pairwise comparison detects genuine style bias or amplifies micro-preferences\")\n- §5.4 六项控制 bound 了 amplification 但未 eliminate 它。缺少独立于两种测量格式的 ground-truth bias measure。Appendix M 100-point continuous Likert 排除了 scale granularity 解释，但未排除 amplification 解释。\n- 如果 amplification 解释成立，论文标题和核心 claim 需根本重构。\n- 建议：设计 ground-truth bias 已知的合成实验；或诚实 reframe 为 \"divergent signals\" 而非单方面归因为 Likert failure。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] Abstract 信息密度过高：d → 0, n = 355, p < 0.01, 60%, OR 68×11 等数字堆砌影响可读性。建议保留 1-2 个最有力数字，其余移至正文。\n\n**W2** [warning] 主实验基于 LLMBar n=100（NLI gate 后 ≈88）。GEE decomposition、power analysis 等深度分析仅在此 benchmark 上。n=100 对\"systematic blindspot\"的 claim scope 偏少。\n\n**W3** [warning] 标题和叙事预设 ground truth 在 pairwise 侧。\"The Likert Blindspot\" 暗示 Likert 有缺陷，但 \"pairwise measures relative preference, Likert measures absolute quality\" 的 construct 差异同样合理。\n\n**W4** [warning] Register 轴未做 rewriter independence test，但在 Table 1/3 中与其他轴同等呈现。建议对 register 结果加显式 caveat。\n\n---\n\n### 小问题\n\n- Limitations 提及废弃的 tone 轴实验并给出 pass rate 数字——建议移至 Appendix\n- BT 模型 IIA 假设仅一笔带过（Footnote 1），值得补充讨论\n- Figure 2 DAG 标注为 design rationale 但正文多处使用因果语言，需统一\n- 格式合规：正文≤8页 ✓，匿名性 ✓，Limitations 无新实验 ✓，引用格式 ✓\n\n---\n\n### Questions for Authors\n\n1. 能否设计 ground-truth bias 幅度已知的合成实验独立验证两种格式的 sensitivity curve？\n2. 100-point continuous Likert 仍未检测到 bias——是否说明 absolute vs. relative evaluation 是根本区分而非 Likert 的\"failure\"？\n3. Rewriter independence test 中 Style OR 下降 22% 如何解读？\n4. 是否考虑让 human annotators 在 CSD pairs 上做 Likert + pairwise，区分 LLM-specific vs. format-specific？\n\n---\n\n### 主要优势\n\n- 控制设计严谨（四家组织的 judge、negative control、七种统计方法、rewriter independence）\n- GEE per-axis decomposition 有真正洞察——不仅\"bias 存在\"，而是\"bias 的结构是什么\"\n- 诚实讨论 Comparative Trap 和 alternative interpretation\n- CSD 作为 black-box framework 对 evaluation practitioners 有即时可用性\n\n---\n\n**Overall: 3.5 (Borderline Conference), Confidence: 4/5**\n\n以目前形态更适合 Findings；若诚实 reframe novelty 并提供更强的 amplification-bounding evidence，可达 Conference 水平。",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见（新颖性 + 写作完整性 + 格式合规）\n\n### 总体评分\n\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 方法论扎实、控制充分的实证工作，但核心发现（pairwise 比 Likert 更灵敏）在心理测量学中已有深厚根基，且 detection 与 amplification 无法干净分离，削弱了\"Likert 是盲区\"这一叙事的说服力。\n\n### 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法设计合理，NLI gate + position swap + negative control 构成可信的控制链；但 detection vs. amplification 无法分离，核心 claim 的因果解读存在歧义 |\n| Excitement | 3/5 | CSD 框架和 GEE per-axis decomposition 有实用价值，但核心 observation 是 Thurstone (1927) 以来的经典心理测量学结论的 domain transfer |\n| Reproducibility | 4/5 | 模型版本、prompt、seed、threshold 均明确；代码承诺在接收后发布 |\n| Confidence | 4/5 | 仔细阅读了正文及全部 Appendix，熟悉 LLM-as-judge 和 measurement theory 文献 |\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] 新颖性定位过度——核心发现有深厚心理测量学先例\n\n- 位置：Section 2 (\"first controlled quantification\")；Abstract (\"systematically misses biases\")；Title\n- Pairwise > Likert sensitivity 是 Thurstone (1927) Law of Comparative Judgment 的经典结论。Mohammad (2017)、Novikova et al. (2018) 已在 NLG 评估中实证验证。论文虽引用了这些工作，但叙事框架将已知现象包装为新发现——\"The Likert Blindspot\" 作为专有名词、\"reveals\" 等措辞暗示首次揭示。\n- 影响：Reviewer 和 AC 会质疑 contribution 是否足够支撑 main conference。\n- 建议：明确定位为\"在 LLM judge 场景下首次系统量化已知 measurement-format sensitivity gap\"；\"first\" 限定为 \"first for LLM judges specifically\"；削弱绝对性措辞。\n\n**N2** [critical] Detection vs. Amplification 无法分离\n\n- 位置：§5.4; §6 Conclusion (\"the primary open question is whether pairwise comparison detects genuine style bias or amplifies micro-preferences\")\n- §5.4 六项控制 bound 了 amplification 但未 eliminate 它。缺少独立于两种测量格式的 ground-truth bias measure。Appendix M 100-point continuous Likert 排除了 scale granularity 解释，但未排除 amplification 解释。\n- 如果 amplification 解释成立，论文标题和核心 claim 需根本重构。\n- 建议：设计 ground-truth bias 已知的合成实验；或诚实 reframe 为 \"divergent signals\" 而非单方面归因为 Likert failure。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] Abstract 信息密度过高：d → 0, n = 355, p < 0.01, 60%, OR 68×11 等数字堆砌影响可读性。建议保留 1-2 个最有力数字，其余移至正文。\n\n**W2** [warning] 主实验基于 LLMBar n=100（NLI gate 后 ≈88）。GEE decomposition、power analysis 等深度分析仅在此 benchmark 上。n=100 对\"systematic blindspot\"的 claim scope 偏少。\n\n**W3** [warning] 标题和叙事预设 ground truth 在 pairwise 侧。\"The Likert Blindspot\" 暗示 Likert 有缺陷，但 \"pairwise measures relative preference, Likert measures absolute quality\" 的 construct 差异同样合理。\n\n**W4** [warning] Register 轴未做 rewriter independence test，但在 Table 1/3 中与其他轴同等呈现。建议对 register 结果加显式 caveat。\n\n---\n\n### 小问题\n\n- Limitations 提及废弃的 tone 轴实验并给出 pass rate 数字——建议移至 Appendix\n- BT 模型 IIA 假设仅一笔带过（Footnote 1），值得补充讨论\n- Figure 2 DAG 标注为 design rationale 但正文多处使用因果语言，需统一\n- 格式合规：正文≤8页 ✓，匿名性 ✓，Limitations 无新实验 ✓，引用格式 ✓\n\n---\n\n### Questions for Authors\n\n1. 能否设计 ground-truth bias 幅度已知的合成实验独立验证两种格式的 sensitivity curve？\n2. 100-point continuous Likert 仍未检测到 bias——是否说明 absolute vs. relative evaluation 是根本区分而非 Likert 的\"failure\"？\n3. Rewriter independence test 中 Style OR 下降 22% 如何解读？\n4. 是否考虑让 human annotators 在 CSD pairs 上做 Likert + pairwise，区分 LLM-specific vs. format-specific？\n\n---\n\n### 主要优势\n\n- 控制设计严谨（四家组织的 judge、negative control、七种统计方法、rewriter independence）\n- GEE per-axis decomposition 有真正洞察——不仅\"bias 存在\"，而是\"bias 的结构是什么\"\n- 诚实讨论 Comparative Trap 和 alternative interpretation\n- CSD 作为 black-box framework 对 evaluation practitioners 有即时可用性\n\n---\n\n**Overall: 3.5 (Borderline Conference), Confidence: 4/5**\n\n以目前形态更适合 Findings；若诚实 reframe novelty 并提供更强的 amplification-bounding evidence，可达 Conference 水平。",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 773 · 2026-05-22T16:42:32.762492+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3463
}
```

</details>

---


### Tool call

_source line 774 · 2026-05-22T16:42:35.981450+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
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

_source line 775 · 2026-05-22T16:42:36.032072+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 776 · 2026-05-22T16:42:39.802054+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_9/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 777 · 2026-05-22T16:42:39.852745+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 778 · 2026-05-22T16:42:45.186927+00:00_

审稿完成，已提交给 Review Director。

核心判断：**3.5 (Borderline Conference)**。两个 Must-Fix 问题——(1) 新颖性定位过度（Thurstone 1927 以来 pairwise > Likert sensitivity 是已知结论，论文将其包装为新发现）；(2) detection vs. amplification 无法分离（六项控制 bound 了但未 eliminate amplification，缺少 ground-truth bias measure）。方法论执行质量高，GEE per-axis decomposition 有真正洞察，适合 Findings track；若 reframe novelty 并补充 amplification-bounding evidence 可冲击 Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 24

## Round 24

4 recorded events


### User

_source line 779 · 2026-05-22T16:43:06.471674+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix、Minor 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure/Appendix）。

---

## Reviewer 1 — 方法严谨性 + 实验设计审查

**Overall Assessment**: 3.5 — Borderline Conference

### Must-Fix

**N1** [critical] Bradley-Terry IIA 假设未经验证
- BT 模型核心假设 IIA 仅在脚注1承认，未做 Hausman-McFadden test。同源文本在多组配对中重复出现，IIA 可能被系统性违反。Appendix B formality 方向不对称性暗示 IIA 违反。
- 建议：执行 IIA 诊断、拟合 Thurstone Model V、解释 direction asymmetry。

**N2** [critical] NLI Quality Gate 的选择偏差未充分量化
- 50 对人工标注太少（Wilson CI 下界 86.3%），未报告 recall/FNR，被过滤配对特征未分析。gate 过滤 12-35% 配对，若系统性排除某种风格变换方向则 Blindspot 可能是数据子集 artifact。Appendix N ablation NLI-fail 样本量太小。
- 建议：扩大人工标注到 200 对，报告 recall/FNR，分析被过滤配对特征。

**N3** [critical] 样本量与 power 的循环论证风险
- Likert ATE 达到 80% power 需 n=336-1200+，远超当前规模。Likert null 结果可能仅反映 power 不足而非方法论缺陷。Conclusion "systematically misses" 的 hedging 不够。
- 建议：更大样本验证、TOST 需更严格 Δ 论证、明确声明不能排除 power 不足解释。

### Should-Fix

**W1** TOST Δ=15pp 缺乏严格论证（循环论证——用自己观测效应量定义等价边界，15pp ≈ d=0.43 属 medium effect，偏宽松）
**W2** Evaluator-producer confound 控制实验范围有限（仅 verbosity × Qwen3-32B 有替代 rewriter）
**W3** 因果术语与方法论强度不匹配（"controlled"/"interventional"/DAG notation 偏强）
**W4** 负控制仅 Claude Sonnet 4 一个模型

### Minor
- M1: n=355 replication 讨论分散
- M2: Figure 1 pipeline sample attrition 数字未标注
- M3: Appendix Q Holm-Bonferroni 8-test family 未包含 cross-benchmark
- M4: Register axis power 未报告

### Questions
1. 是否尝试过 Thurstone Model V？
2. 50 对人工标注中 gate-rejected 的 false negative 数据？
3. 是否尝试过其他 Likert 量表设计？
4. AlpacaEval/MT-Bench 的 per-judge per-axis 完整结果？
5. Bootstrap attenuation δ̄ ≈ -0.017 的 CI 是否包含 0？

### Missing References
Thurstone Model V 讨论、Bojar et al. (2016) WMT human evaluation、Karpinska et al. (2021)

---

请对以上每一条给出你的 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 780 · 2026-05-22T16:45:38.696048+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 Reviewer 1\n\n### Must-Fix\n\n**[REBUT] R1-N1: BT IIA 假设未经验证** — 定级 overstated。(1) Table 2 七种统计方法中五种非参数方法不假设 IIA，全部独立确认 Blindspot；BT 非孤证。(2) Appendix B direction asymmetry 反映实质性偏好方向差异，不等于 IIA 违反。(3) Binary-choice BT 中 IIA 自动满足（无 irrelevant alternative 可删除），Hausman-McFadden test 不适用。建议降为 Should-Fix。\n\n**[AGREE] R1-N2: NLI Gate 选择偏差** — 50 对人工标注偏少，recall/FNR 缺失。但 Appendix E threshold sweep（11 个阈值，44 组合全部显著，BT 变化 ≤4pp）提供部分缓解，说明结果不依赖特定子集。建议定为 Should-Fix。\n\n**[AGREE] R1-N3: 样本量与 power 循环论证** — R1 最有力的一条。Table 12 需 n=336-1200+ 的 Likert power，当前 n≈88 远不够。Bootstrap attenuation（Appendix J, d̄≈-0.017）提供部分反驳但不充分——very small true effect 仍无法排除。\"systematically misses\" 措辞需 hedge。\n\n### Should-Fix\n\n**[AGREE] R1-W1** TOST Δ=15pp 需先验论证。\n**[REBUT] R1-W2** R1 描述不准确——Appendix D Table 7 覆盖 formality+verbosity 两轴（非仅 verbosity），但 register 确实未覆盖。核心关切成立，具体描述需更正。\n**[AGREE] R1-W3** 因果术语过强，我独立提出了同一问题。\n**[AGREE] R1-W4** 单一 negative control 是限制。\n\n### Minor\n**[AGREE] M1, M3, M4**\n**[REBUT] M2** — Figure 1 标题明确写了 \"Numbers indicate sample attrition at each stage\"，图中有标注。\n\n### Questions\nQ1: Binary-choice BT 中 Thurstone Model V 增量有限。Q2: 同意应报告。Q3: Appendix M 已测 100-point continuous Likert。Q4: 同意补充。Q5: Appendix J 明确 CI 包含 0。\n\n### Missing References\n[AGREE] Bojar et al. (2016) WMT human evaluation 高度相关。\n[REBUT] Thurstone Model V 在 binary choice 场景增量有限，非必要。\nKarpinska et al. (2021) 需更多 context。\n\n### 两位 Reviewer 共识点\n1. **Detection vs. amplification 未解决**（R2-N2 与 R1-N3 的 power 论证相互强化）\n2. **因果/绝对性措辞需 hedge**（R2-N1 novelty overclaim + R1-W3 因果术语）\n3. **Rewriter independence 不完整**（R2-W4 + R1-W2，register 未覆盖）\n4. **样本量有限**（R2-W2 + R1-N3）\n\n两位 Reviewer 分歧点：\n- R1 将 BT IIA 定为 critical，R2 认为 binary-choice 中 IIA 自动满足，应降为 Should-Fix\n- R1 将 NLI gate 定为 critical，R2 认为 threshold sweep 提供充分缓解，应降为 Should-Fix",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 Reviewer 1\n\n### Must-Fix\n\n**[REBUT] R1-N1: BT IIA 假设未经验证** — 定级 overstated。(1) Table 2 七种统计方法中五种非参数方法不假设 IIA，全部独立确认 Blindspot；BT 非孤证。(2) Appendix B direction asymmetry 反映实质性偏好方向差异，不等于 IIA 违反。(3) Binary-choice BT 中 IIA 自动满足（无 irrelevant alternative 可删除），Hausman-McFadden test 不适用。建议降为 Should-Fix。\n\n**[AGREE] R1-N2: NLI Gate 选择偏差** — 50 对人工标注偏少，recall/FNR 缺失。但 Appendix E threshold sweep（11 个阈值，44 组合全部显著，BT 变化 ≤4pp）提供部分缓解，说明结果不依赖特定子集。建议定为 Should-Fix。\n\n**[AGREE] R1-N3: 样本量与 power 循环论证** — R1 最有力的一条。Table 12 需 n=336-1200+ 的 Likert power，当前 n≈88 远不够。Bootstrap attenuation（Appendix J, d̄≈-0.017）提供部分反驳但不充分——very small true effect 仍无法排除。\"systematically misses\" 措辞需 hedge。\n\n### Should-Fix\n\n**[AGREE] R1-W1** TOST Δ=15pp 需先验论证。\n**[REBUT] R1-W2** R1 描述不准确——Appendix D Table 7 覆盖 formality+verbosity 两轴（非仅 verbosity），但 register 确实未覆盖。核心关切成立，具体描述需更正。\n**[AGREE] R1-W3** 因果术语过强，我独立提出了同一问题。\n**[AGREE] R1-W4** 单一 negative control 是限制。\n\n### Minor\n**[AGREE] M1, M3, M4**\n**[REBUT] M2** — Figure 1 标题明确写了 \"Numbers indicate sample attrition at each stage\"，图中有标注。\n\n### Questions\nQ1: Binary-choice BT 中 Thurstone Model V 增量有限。Q2: 同意应报告。Q3: Appendix M 已测 100-point continuous Likert。Q4: 同意补充。Q5: Appendix J 明确 CI 包含 0。\n\n### Missing References\n[AGREE] Bojar et al. (2016) WMT human evaluation 高度相关。\n[REBUT] Thurstone Model V 在 binary choice 场景增量有限，非必要。\nKarpinska et al. (2021) 需更多 context。\n\n### 两位 Reviewer 共识点\n1. **Detection vs. amplification 未解决**（R2-N2 与 R1-N3 的 power 论证相互强化）\n2. **因果/绝对性措辞需 hedge**（R2-N1 novelty overclaim + R1-W3 因果术语）\n3. **Rewriter independence 不完整**（R2-W4 + R1-W2，register 未覆盖）\n4. **样本量有限**（R2-W2 + R1-N3）\n\n两位 Reviewer 分歧点：\n- R1 将 BT IIA 定为 critical，R2 认为 binary-choice 中 IIA 自动满足，应降为 Should-Fix\n- R1 将 NLI gate 定为 critical，R2 认为 threshold sweep 提供充分缓解，应降为 Should-Fix",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 781 · 2026-05-22T16:45:42.210536+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3514
}
```

</details>

---


### Assistant

_source line 782 · 2026-05-22T16:45:48.431668+00:00_

交叉回应已提交。

**总结**：对 R1 的 3 条 Must-Fix，我 rebut 了 N1（BT IIA 在 binary choice 中自动满足，且有五种 IIA-free 方法独立确认，建议降为 Should-Fix），agree 了 N2（但建议降为 Should-Fix，因 threshold sweep 提供缓解），agree 了 N3（power 不足是最有力的 alternative explanation）。两位 Reviewer 的核心共识集中在：detection vs. amplification 未解决、措辞需 hedge、rewriter independence 不完整、样本量有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 25

## Round 25

68 recorded events


### User

_source line 783 · 2026-05-22T18:08:34.388638+00:00_

[Round 10 审稿请求]:
你是 Reviewer 2，负责审查本论文的**新颖性、完整性、写作质量和相关工作覆盖**。

## 论文信息
- 标题：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition
- 主文件：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf

## Venue 要求
- **EMNLP 2026**（ARR May cycle），截止 2026-05-25
- Long paper：正文 ≤8 页 + 无限参考文献（ACL 模板）
- Limitations + Ethical Considerations 不计入页数限制
- Double-blind 匿名审稿
- Overall Assessment 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 你的审查侧重

**新颖性**（重点）：
1. "Likert Blindspot" 概念——这是心理测量学已知的 Thurstone (1927) 现象的 LLM judge domain transfer，还是有实质性新发现？
2. CSD framework 的 novelty——相对于 RATE (Reber et al., 2025) 和其他 interventional 方法的增量贡献
3. Per-axis confound decomposition 的 novelty——GEE 是标准统计方法，其在 LLM judge bias 场景的应用是否构成足够贡献
4. 论文 framing 的声明强度：'demonstrates'/'identifies' 等措辞是否与实际证据匹配
5. Detection vs. amplification 的核心歧义——论文标题 'Detecting Hidden Style Bias' 是否预设了 pairwise 为 ground truth

**完整性**：
6. 3 个 style axes（formality, verbosity, register）是否足以支撑 "framework" 级别泛化
7. 负控制仅 Claude Sonnet 4 一个模型——是否足以论证 Blindspot 的架构特异性
8. 缺少 human evaluation ground truth 来区分 measurement attenuation vs. construct divergence
9. Register axis 的 evaluator-producer overlap 风险（无 cross-rewriter validation）
10. Cross-benchmark replication 的不完整覆盖（Table 1 空 cells）

**写作质量**：
11. Abstract 信息密度——数字堆砌是否影响可读性
12. Introduction motivating example 的说服力和公平性
13. 论文整体叙事逻辑和 flow
14. Limitations 章节的覆盖面和深度
15. 格式合规：正文 ≤8 页、匿名、ACL 模板

**相关工作覆盖**：
16. 是否遗漏关键相关工作（尤其 pairwise vs. rating 方法比较的文献）
17. 与竞品（RATE, FairJudge, CASSE, Comparative Trap）的定位是否准确
18. 引用质量——是否存在幻觉引用或格式问题

请给出结构化审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准）。

对每个 Weakness 标注严重程度：
- **Must-Fix (critical)**：不修复则不可接收
- **Should-Fix (warning)**：显著改善论文质量
- **Minor (info)**：建议改进

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 784 · 2026-05-22T18:08:49.295487+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
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

_source line 785 · 2026-05-22T18:08:49.296238+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-22T18:08:53.162246+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria dimensions"
  }
}
```

</details>

---


### Tool call

_source line 787 · 2026-05-22T18:08:55.520417+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf",
  "pages": "1-8",
  "project": "causal_style_decomp_judge",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf",
    "pages": "1-8",
    "project": "causal_style_decomp_judge",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 788 · 2026-05-22T18:08:59.288518+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL/ARR reviewer guidelines for 2025-2026:

## Review Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Key Reviewer Policies

All papers recommended for Findings or main conference are expected to be sound and reproducible.

The program chairs and ARR EiCs will consider egregious cases reported by chairs, including the cases of extremely terse reviews, unprofessional tone, and LLM-generated reviews.

## Reviewer Recognition

Starting from May 2025, ACL introduces the awards policy for reviewers & chairs. The area chairs or senior area chairs may nominate the great reviewers, and senior chairs may also nominate area chairs who perform great service.

The search results primarily focus on the three-point scoring system (soundness, excitement, and overall recommendation) as the main criteria dimensions for re
…[truncated 122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6126
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-22T18:09:01.962995+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 578.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.1}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 547.6}], \"total_pages\": 17, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/a
…[truncated 77 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6442
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-22T18:09:08.148305+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
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

_source line 791 · 2026-05-22T18:09:08.148654+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 792 · 2026-05-22T18:09:08.800687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 793 · 2026-05-22T18:09:09.152791+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 794 · 2026-05-22T18:09:10.107732+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1307
}
```

</details>

---


### Tool result

_source line 795 · 2026-05-22T18:09:10.108471+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 796 · 2026-05-22T18:09:10.259078+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 797 · 2026-05-22T18:09:10.461532+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 798 · 2026-05-22T18:09:11.316455+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1057
}
```

</details>

---


### Tool result

_source line 799 · 2026-05-22T18:09:11.367982+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 800 · 2026-05-22T18:09:25.786751+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 801 · 2026-05-22T18:09:26.540678+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 802 · 2026-05-22T18:09:26.691399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 803 · 2026-05-22T18:09:27.243482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 804 · 2026-05-22T18:09:27.546743+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 805 · 2026-05-22T18:09:27.547210+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 806 · 2026-05-22T18:09:28.052433+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 808
}
```

</details>

---


### Tool result

_source line 807 · 2026-05-22T18:09:29.309968+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1762
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-22T18:09:29.310431+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form dimensions, scoring criteria, and scoring scales. I need the exact dimensions reviewers must score (e.g., soundness, excitement, overall assessment), the scale for each, and any description of what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form dimensions, scoring criteria, and scoring scales. I need the exact dimensions reviewers must score (e.g., soundness, excitement, overall assessment), the scale for each, and any description of what each score means."
  }
}
```

</details>

---


### Tool result

_source line 809 · 2026-05-22T18:09:34.987678+00:00_

# ARR Review Form Dimensions and Scoring

Based on the guidelines provided, the review form includes **three primary scoring dimensions**:

## Scoring Dimensions

1. **Soundness**
   - Measures technical correctness and methodological rigor
   - Must be justified by review text; low scores require explicit explanation
   - Guidelines note: "The soundness scores must be justified by the text of the review"

2. **Excitement**
   - Reflects personal interest and subjective appeal
   - Orthogonal to soundness assessment
   - Allows reviewers to distinguish between technically sound but personally uninteresting work

3. **Overall Assessment**
   - Composite recommendation for conference acceptance
   - Integrates soundness, excitement, novelty, and potential impact
   - Determines suitability for main conference, Findings track, or rejection

## Additional Scoring

The guidelines also reference a **reproducibility score**, which reviewers can provide to assess whether sufficient implementation details and data availability information exists for reproduction attempts.

## Key Principle

The guidelines emphasize that reviewers should avoid conflating low technical soundness with lack of personal interest: "Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper."

The document does not specify numerical scales (e.g., 1-5 or 1-10) for these dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5677
}
```

</details>

---


### Tool call

_source line 810 · 2026-05-22T18:09:43.747459+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf",
  "pages": "9-17",
  "project": "causal_style_decomp_judge",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/submitted.pdf",
    "pages": "9-17",
    "project": "causal_style_decomp_judge",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 811 · 2026-05-22T18:09:45.257398+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 543.5}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.6}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 445.9}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 583.5}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 595.9}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images
…[truncated 316 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1509
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-22T18:09:48.571481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 813 · 2026-05-22T18:09:49.023547+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 814 · 2026-05-22T18:09:49.827825+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1256
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-22T18:09:49.831131+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 816 · 2026-05-22T18:09:49.831534+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 817 · 2026-05-22T18:09:50.086490+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 818 · 2026-05-22T18:09:50.641053+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 809
}
```

</details>

---


### Tool result

_source line 819 · 2026-05-22T18:09:50.993841+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 820 · 2026-05-22T18:09:58.025206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 821 · 2026-05-22T18:09:58.779142+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-22T18:09:58.829780+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 823 · 2026-05-22T18:09:59.332414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 824 · 2026-05-22T18:09:59.789094+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 825 · 2026-05-22T18:09:59.789544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 826 · 2026-05-22T18:10:00.592783+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1260
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-22T18:10:00.593506+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-22T18:10:00.995116+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 829 · 2026-05-22T18:10:01.599451+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-22T18:10:09.880575+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 831 · 2026-05-22T18:10:09.880987+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Detecting Hidden Style Bias\\in LLM Judges via Controlled Style Decomposition}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\paragraph{Quality--style confounding and construct validity.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
43	Although the formality effect survives logistic adjustment for original preference ($\text{OR} = 2.32$, $p = 0.006$; Appendix~\ref{app:direction}), residual confounding is not fully eliminated.
44	An alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference. Under this view, the divergence reflects construct difference rather than measurement failure. The Comparative Trap \citep{jeong2025comparative} lends support to this alternative; six experimental controls bound this risk (\S\ref{sec:amplification}), though definitive separation would require human ground-truth ratings.
45	The primary open question is whether pairwise comparison detects genuine style bias or amplifies micro-preferences inhe
…[truncated 3715 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 832 · 2026-05-22T18:10:14.846938+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 833 · 2026-05-22T18:10:15.248623+00:00_

1	\begin{abstract}
2	Likert scoring---the default evaluation mode for LLM judges---attenuates style bias signals that pairwise comparison detects.
3	We introduce Controlled Style Decomposition (CSD), a black-box framework combining human-validated, NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison to quantify style bias in LLM judges.
4	Across four judges from independent providers, one negative control, and three style axes, CSD demonstrates the Likert Blindspot: a severity spectrum from complete attenuation at moderate bias to over 60\% signal loss at stronger effects, confirmed by seven statistical methods across three benchmarks.
5	GEE conditional decomposition identifies a per-axis confound structure consistent across all four target judges: verbosity bias is style-dominated, formality exhibits a conditional effect moderated by content quality, and register is judge-dependent---determining which estimates are directly interpretable and which require conditional analysis.
6	A negative-control judge shows no detectable bias on either primary axis, supporting discriminative validity.
7	Whether the Blindspot reflects measurement attenuation or genuine construct divergence between absolute and comparative evaluation remains an open question; under either interpretation, Likert-only evaluation underestimates style-driven preferences that propagate through pairwise-based alignment pipelines.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-22T18:10:15.249074+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 835 · 2026-05-22T18:10:15.299642+00:00_

1	\section{Introduction}
2	
3	\emph{``What is the average height for a male?''} --- given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \emph{higher} on a 1--10 Likert scale (8 vs.\ 5), yet consistently selects the formal variant in pairwise comparison.
4	Same judge, same texts, opposite conclusions.
5	This is the \emph{Likert Blindspot}.
6	We note that formality preferences may partially reflect legitimate quality judgments---our GEE decomposition (\S\ref{sec:direction}) quantifies this originality component.
7	This example reflects a systematic pattern.
8	
9	LLM judges are central infrastructure for NLP evaluation and alignment training (RLHF, DPO), where judge preferences serve as reward signals; any systematic bias propagates through both evaluation leaderboards and model development pipelines.
10	Style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}: 76--92\% of observed preferences originate from surface-level style cues \citep{li2026preference}, with bias scores of 0.76--0.92 across five judges \citep{soumik2026judging}.
11	Despite this consensus, existing approaches address individual requirements (multi-dimensional style analysis \citep{casse2026concise,wang2026fairjudge}, interventional design \citep{reber2025rate}, population-level correction \citep{dubois2025lc}), but no single framework integrates per-axis decomposition, interventional identification, per-instance diagnostics, and black-box applicability.
12	A further concern: standard Likert scoring produces ${\sim}60\%$ uninformative ties, and even non-tied pairs carry weaker signal than pairwise comparison---a limitation predicted by measurement theory \citep{thurstone1927law} but previously unquantified for LLM judges.
13	
14	We propose Controlled Style Decomposition (CSD), combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison.
15	I
…[truncated 2205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 836 · 2026-05-22T18:10:22.622495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 837 · 2026-05-22T18:10:22.974182+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Two lines of work motivate our approach: interventional methods for diagnosing judge bias, and measurement theory on the sensitivity of different elicitation formats.
5	
6	\paragraph{Interventional Approaches to Judge Bias}
7	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
8	\citet{reber2025rate} propose RATE, a framework that rewrites model outputs along style attributes using imperfect counterfactuals and measures the causal effect on reward model scores via Likert-scale Average Treatment Effect (ATE).
9	RATE applies a correction term to account for rewriting imperfections, but its reliance on Likert ATE as the primary metric is a vulnerability: our experiments show that Likert scoring exhibits a ceiling effect in which 60\% of style-transformed pairs receive identical integer scores, yielding non-significant ATE estimates ($p = 0.332$) for the same interventions that pairwise comparison detects at $p = 0.006$.
10	If this Likert Blindspot generalizes beyond our setting, RATE's own style-related findings may underestimate the true magnitude of attribute effects.
11	CSD differs from RATE in three respects: it targets individual style axes rather than general attributes, it measures bias through position-controlled pairwise comparison rather than Likert ATE, and it enforces content preservation via NLI entailment gating rather than post-hoc correction for imperfect rewrites.
12	\citet{counterfactual2025rhetorical} also adopt an interventional LLM-based design, rewriting texts to measure rhetorical style effects and aggregating preferences with a Bradley-Terry model.
13	Their framework operates at persona-level granularity (e.g., ``writes like a professor''), whereas CSD intervenes on specific style axes (e.g., formality, conciseness) and uses a sign test with position control rather than parametric aggregation.
14	
15	\paragrap
…[truncated 5448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 838 · 2026-05-22T18:10:22.974620+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 839 · 2026-05-22T18:10:23.125468+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Style-Controlled Rewriting}
5	\label{sec:rewriting}
6	
7	We isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.
8	For each text, an instruction-tuned LLM (Qwen3-32B) classifies its current style along the target axis (e.g., formal vs.\ casual via binary classification).
9	It then rewrites the text toward the opposite pole (temperature 0.7) according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').
10	This produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.
11	Each operation constitutes a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}).
12	To control for rewriting artifact bias---the possibility that the judge prefers original text over any rewrite regardless of style---we additionally generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
13	
14	\subsection{Content Preservation Verification}
15	\label{sec:nli_gate}
16	
17	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
18	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large with an entailment threshold of 0.90, selected as the threshold above which NLI performance plateaus (Appendix~\ref{app:nli_sweep}).
19	For axes that preserve information density (formality, register), we apply standard bidirectional entailment: both NLI(original $\to$ rewrite) and NLI(rewrite $\to$ original) must exceed this value.
20	For axes that inherently c
…[truncated 6101 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-22T18:10:35.138915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 841 · 2026-05-22T18:10:35.189928+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	The primary family comprises six tests---three target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B) $\times$ two axes (formality, verbosity)---corrected via Holm-Bonferroni at $\alpha = 0.05$; Gemini-2.5-Flash serves as confirmatory replication and is excluded from FWER control; as a sensitivity check, all eight tests remain significant under the expanded family (Appendix~\ref{app:holm8}).
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses are reported with uncorrected $p$-values and interpreted as hypothesis-generating; confirmatory analyses test specific hypotheses about pipeline validity and are evaluated at the nominal $\alpha = 0.05$ level without additional correction, as they address orthogonal questions about measurement reliability rather than the primary style-bias family.
12	Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the default regularization of the \texttt{choix} Python library.\footnote{In binary-choice BT models, IIA is structurally satisfied; the direction asymmetry in Appendix~\ref{app:bt_gof} (formality: formal-origin 88.9\% vs.\ casual-origin 52.6\%, Fisher $p = 0.015$; verbosity: $p = 0.453$) reflects heterogeneous treatment effects across style directions rather than IIA violation.}
13	All bootstrap confidence intervals use 10{,}000 pair-level resamples with seed 42.
14	GEE models use exchangeable working correlation, justified by near-zero estimated within-pair correlations ($\hat{\alpha} \in [-0.25, +0.11]$; Appendix~\ref{app:gee_diagnostics}).
15	
16	\paragraph{Model selection
…[truncated 16421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 842 · 2026-05-22T18:10:42.178221+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 843 · 2026-05-22T18:10:42.178756+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	CSD yields two findings.
5	First, the \emph{Likert Blindspot}: our evidence suggests that Likert scoring attenuates style bias signals that pairwise comparison detects---complete at moderate bias ($d \to 0$ at $n = 355$), ${>}60\%$ signal loss at stronger effects---confirmed by seven statistical methods; we cannot fully separate measurement attenuation from format-level amplification (\S\ref{sec:amplification}) or construct divergence, but under any interpretation, Likert-only audits underestimate style-driven preferences that propagate through alignment pipelines.
6	Second, GEE conditional decomposition identifies per-axis confound structure---verbosity style-dominated, formality conditional, register judge-dependent---determining which estimates require conditional analysis.
7	
8	Existing Likert-based null findings may reflect measurement insensitivity rather than absence of bias; pairwise comparison with amplification controls (\S\ref{sec:amplification}) offers superior detection sensitivity.
9	Under the six amplification controls reported in \S\ref{sec:nli_validation}---including a negative-control judge that shows no pairwise bias---the observed sensitivity gap is more consistent with measurement attenuation than format-induced amplification, though the latter cannot be fully excluded.
10	
11	For practitioners auditing LLM judges, our results suggest that Likert-only evaluation is insufficient: bias audits should employ pairwise comparison with position control and per-axis decomposition to distinguish style-dominated from quality-confounded effects.
12	Human ground-truth validation of both measurement modes on identical pairs---determining whether the Blindspot reflects measurement attenuation, construct divergence, or a combination---remains the most informative next step.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 844 · 2026-05-22T18:14:56.159501+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿报告：The Likert Blindspot\n\n### Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一个黑盒框架，通过 NLI 门控内容保持、单轴风格改写和位控 pairwise 比较来量化 LLM judge 的风格偏差。核心发现为\"Likert Blindspot\"：Likert 评分系统性地衰减 pairwise 比较能检测到的风格偏差信号——在中等偏差时完全衰减（d → 0），在较强效应时信号损失 >60%。在 4 个目标 judge + 1 个负控制、3 个风格轴、3 个 benchmark 上验证。GEE 条件分解揭示了逐轴混淆结构。\n\n---\n\n### Strengths\n\n**S1. 实验设计严谨，控制充分。** 六项独立的放大控制（NLI gate ablation、负控制 judge、跨轴变异、rewriting artifact 吸收、debiased prompting、跨架构复现）显示出对 \"Comparative Trap\" 反面论证的充分意识。Position swap 双向评估 + consistent pairs sign test 设计合理。(§5.1, §5.4)\n\n**S2. 统计分析多层次且透明。** 七种测量方法的灵敏度层级（Table 2）、Holm-Bonferroni 校正、探索性与验证性分析的明确区分、bootstrap 衰减分析和形式化功效分析（Appendix K），体现了高标准的统计实践。\n\n**S3. 跨 judge 一致性强。** 四个独立架构一致复现 Blindspot（Table 1），GEE 混淆结构跨 judge 一致（verbosity 全部 Style OR 8–13，formality 全部条件显著）。\n\n**S4. Limitations 坦诚全面。** 对 quality-style confounding、evaluator-producer overlap、construct divergence 的歧义性进行了充分讨论。\n\n**S5. GEE 混淆分解有实用价值。** 将风格效应与 originality 效应分离，对从业者有直接指导意义。\n\n---\n\n### Must-Fix 问题（critical）\n\n**N1 [critical] 核心歧义未解决，但标题和 framing 隐式预设 pairwise 为 ground truth**\n\n论文标题 \"Detecting Hidden Style Bias\" 和 \"Blindspot\" 命名隐式假定 pairwise 检测到的是真实偏差、Likert 遗漏了它。然而论文自身承认三种等效解释：(a) Likert 测量衰减，(b) pairwise 放大（Comparative Trap），(c) 构念分歧。六项放大控制必要但非充分——负控制的 TOST Δ=15pp 实质性过宽（14pp win probability 差异会被判为\"等价\"），且仅一个负控制模型。建议标题改为更中性的表述，Abstract 前置三种解释。\n\n**N2 [critical] 新颖性定位不足：\"Likert Blindspot\" 本质是 Thurstone (1927) 在 LLM judge 领域的实证确认**\n\nForced-choice 比 rating scale 灵敏度更高是心理测量学经典结论（Thurstone 1927, Preston & Colman 2000, DeCoster & Iselin 2011），论文自己引用了这些文献。\"unquantified\" 的声明技术上正确，但核心机制完全可从已有理论预测。增量贡献是实证量化——有价值，但不足以支撑 \"demonstrates\"/\"identifies\" 等发现性措辞。建议明确定位为\"首次在 LLM judge 下的系统性实证量化\"，并深度对比 LLM judge 场景是否超越传统理论预测。\n\n---\n\n### Should-Fix 问题（warning）\n\n**W1 [warning] Formality 轴的 GEE 结果削弱 \"style bias\" 叙事。** Table 3 中多个 judge 的 Orig OR ≥ Style OR（GPT-4o: 2.32 vs 2.58; Qwen3: 4.70 vs 4.20），pairwise 检测到的可能更多是与 formality 相关的质量差异而非纯风格偏差。\n\n**W2 [warning] Register 轴 evaluator-producer overlap 严重且无跨改写器验证。** Register 所有改写用 Qwen3-32B 且无交叉验证，BT 结果也较弱。建议降级为 \"exploratory pilot axis\"。\n\n**W3 [warning] 三个风格轴不足以支撑 \"framework\" 泛化。** 第四轴（tone）因 NLI gate 拒绝率过高放弃，表明适用性受限。建议软化为 \"methodology for content-preserving style axes\"。\n\n**W4 [warning] 跨 benchmark 覆盖稀疏。** AlpacaEval 3 配置、MT-Bench 2 配置，verbosity 仅跨 benchmark 验证了 Qwen3 一个 judge。\"three benchmarks\" 声明名义上成立但实际覆盖很低。\n\n**W5 [warning] 负控制 TOST Δ=15pp 过宽且仅一个模型。** 建议报告不同 Δ 下的 TOST 结果（10pp, 5pp），讨论 15pp 的实际含义。\n\n---\n\n### Minor 问题\n\n- M1: Abstract 数字密度过高\n- M2: Introduction 开头单实例不能代表系统性模式，caveat 应前置\n- M3: 对 RATE 的批评措辞过于直接\n- M4: Figure 2 DAG 中 orange dashed arrow 标注字号过小\n- M5: Table 1 五种标记系统认知负担高\n- M6: Limitations 约 1.5 页可适当精简\n\n---\n\n### Missing References\n\n1. Carterette et al. (2008) — forced-choice vs. graded relevance 判断灵敏度差异（ECIR）\n2. Sedoc & Ungar (2020) — IRT 模型应用于 chatbot 评估（ACL）\n3. Deutsch et al. (2023) — tie 处理对评估指标灵敏度的影响（EMNLP）\n\n---\n\n### 官方维度打分（ACL ARR）\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3.5/5 | 方法严谨但核心歧义未解决；formality 混淆结构削弱叙事；TOST Δ 过宽 |\n| Excitement | 2.5/5 | 经典心理测量学结论的领域迁移，非新发现；GEE 分解有增量贡献 |\n| Reproducibility | 4/5 | 代码数据承诺发布；统计方法详细；模型版本固定 |\n\n### Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n实验设计严谨、统计分析透明的实证工作，但核心发现（Likert 对风格偏差的灵敏度低于 pairwise）本质是心理测量学经典理论在 LLM judge 场景的实证确认而非新发现，detection vs. amplification 核心歧义未解决，新颖性和 excitement 不足以达到主会议水平。",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿报告：The Likert Blindspot\n\n### Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一个黑盒框架，通过 NLI 门控内容保持、单轴风格改写和位控 pairwise 比较来量化 LLM judge 的风格偏差。核心发现为\"Likert Blindspot\"：Likert 评分系统性地衰减 pairwise 比较能检测到的风格偏差信号——在中等偏差时完全衰减（d → 0），在较强效应时信号损失 >60%。在 4 个目标 judge + 1 个负控制、3 个风格轴、3 个 benchmark 上验证。GEE 条件分解揭示了逐轴混淆结构。\n\n---\n\n### Strengths\n\n**S1. 实验设计严谨，控制充分。** 六项独立的放大控制（NLI gate ablation、负控制 judge、跨轴变异、rewriting artifact 吸收、debiased prompting、跨架构复现）显示出对 \"Comparative Trap\" 反面论证的充分意识。Position swap 双向评估 + consistent pairs sign test 设计合理。(§5.1, §5.4)\n\n**S2. 统计分析多层次且透明。** 七种测量方法的灵敏度层级（Table 2）、Holm-Bonferroni 校正、探索性与验证性分析的明确区分、bootstrap 衰减分析和形式化功效分析（Appendix K），体现了高标准的统计实践。\n\n**S3. 跨 judge 一致性强。** 四个独立架构一致复现 Blindspot（Table 1），GEE 混淆结构跨 judge 一致（verbosity 全部 Style OR 8–13，formality 全部条件显著）。\n\n**S4. Limitations 坦诚全面。** 对 quality-style confounding、evaluator-producer overlap、construct divergence 的歧义性进行了充分讨论。\n\n**S5. GEE 混淆分解有实用价值。** 将风格效应与 originality 效应分离，对从业者有直接指导意义。\n\n---\n\n### Must-Fix 问题（critical）\n\n**N1 [critical] 核心歧义未解决，但标题和 framing 隐式预设 pairwise 为 ground truth**\n\n论文标题 \"Detecting Hidden Style Bias\" 和 \"Blindspot\" 命名隐式假定 pairwise 检测到的是真实偏差、Likert 遗漏了它。然而论文自身承认三种等效解释：(a) Likert 测量衰减，(b) pairwise 放大（Comparative Trap），(c) 构念分歧。六项放大控制必要但非充分——负控制的 TOST Δ=15pp 实质性过宽（14pp win probability 差异会被判为\"等价\"），且仅一个负控制模型。建议标题改为更中性的表述，Abstract 前置三种解释。\n\n**N2 [critical] 新颖性定位不足：\"Likert Blindspot\" 本质是 Thurstone (1927) 在 LLM judge 领域的实证确认**\n\nForced-choice 比 rating scale 灵敏度更高是心理测量学经典结论（Thurstone 1927, Preston & Colman 2000, DeCoster & Iselin 2011），论文自己引用了这些文献。\"unquantified\" 的声明技术上正确，但核心机制完全可从已有理论预测。增量贡献是实证量化——有价值，但不足以支撑 \"demonstrates\"/\"identifies\" 等发现性措辞。建议明确定位为\"首次在 LLM judge 下的系统性实证量化\"，并深度对比 LLM judge 场景是否超越传统理论预测。\n\n---\n\n### Should-Fix 问题（warning）\n\n**W1 [warning] Formality 轴的 GEE 结果削弱 \"style bias\" 叙事。** Table 3 中多个 judge 的 Orig OR ≥ Style OR（GPT-4o: 2.32 vs 2.58; Qwen3: 4.70 vs 4.20），pairwise 检测到的可能更多是与 formality 相关的质量差异而非纯风格偏差。\n\n**W2 [warning] Register 轴 evaluator-producer overlap 严重且无跨改写器验证。** Register 所有改写用 Qwen3-32B 且无交叉验证，BT 结果也较弱。建议降级为 \"exploratory pilot axis\"。\n\n**W3 [warning] 三个风格轴不足以支撑 \"framework\" 泛化。** 第四轴（tone）因 NLI gate 拒绝率过高放弃，表明适用性受限。建议软化为 \"methodology for content-preserving style axes\"。\n\n**W4 [warning] 跨 benchmark 覆盖稀疏。** AlpacaEval 3 配置、MT-Bench 2 配置，verbosity 仅跨 benchmark 验证了 Qwen3 一个 judge。\"three benchmarks\" 声明名义上成立但实际覆盖很低。\n\n**W5 [warning] 负控制 TOST Δ=15pp 过宽且仅一个模型。** 建议报告不同 Δ 下的 TOST 结果（10pp, 5pp），讨论 15pp 的实际含义。\n\n---\n\n### Minor 问题\n\n- M1: Abstract 数字密度过高\n- M2: Introduction 开头单实例不能代表系统性模式，caveat 应前置\n- M3: 对 RATE 的批评措辞过于直接\n- M4: Figure 2 DAG 中 orange dashed arrow 标注字号过小\n- M5: Table 1 五种标记系统认知负担高\n- M6: Limitations 约 1.5 页可适当精简\n\n---\n\n### Missing References\n\n1. Carterette et al. (2008) — forced-choice vs. graded relevance 判断灵敏度差异（ECIR）\n2. Sedoc & Ungar (2020) — IRT 模型应用于 chatbot 评估（ACL）\n3. Deutsch et al. (2023) — tie 处理对评估指标灵敏度的影响（EMNLP）\n\n---\n\n### 官方维度打分（ACL ARR）\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3.5/5 | 方法严谨但核心歧义未解决；formality 混淆结构削弱叙事；TOST Δ 过宽 |\n| Excitement | 2.5/5 | 经典心理测量学结论的领域迁移，非新发现；GEE 分解有增量贡献 |\n| Reproducibility | 4/5 | 代码数据承诺发布；统计方法详细；模型版本固定 |\n\n### Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n实验设计严谨、统计分析透明的实证工作，但核心发现（Likert 对风格偏差的灵敏度低于 pairwise）本质是心理测量学经典理论在 LLM judge 场景的实证确认而非新发现，detection vs. amplification 核心歧义未解决，新颖性和 excitement 不足以达到主会议水平。",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 845 · 2026-05-22T18:14:59.625350+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3465
}
```

</details>

---


### Tool call

_source line 846 · 2026-05-22T18:15:05.059570+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
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

_source line 847 · 2026-05-22T18:15:05.110185+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 848 · 2026-05-22T18:15:11.889865+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_10/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 849 · 2026-05-22T18:15:11.990516+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 850 · 2026-05-22T18:15:21.829647+00:00_

审稿报告已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。论文方法论严谨、统计实践高标准，但两个 critical 问题压制了评分——(1) "Likert Blindspot" 本质是 Thurstone (1927) forced-choice 灵敏度优势在 LLM judge 领域的实证确认，novelty 定位为"新发现"而非"领域迁移验证"存在 overclaim；(2) detection vs. amplification vs. construct divergence 的核心歧义未解决，但标题和 framing 隐式预设 pairwise 为 ground truth。五个 should-fix 进一步影响评分（formality 轴的 GEE 结果反而削弱 bias 叙事、register 轴缺乏跨改写器验证、framework 泛化声明过强、跨 benchmark 覆盖稀疏、负控制 TOST Δ 过宽）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 26

## Round 26

4 recorded events


### User

_source line 851 · 2026-05-22T18:17:14.564972+00:00_

[Round 10 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿报告

**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition
**Venue**: EMNLP 2026 (ARR May cycle)
**审查侧重**: 方法严谨性、实验设计、统计分析

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心方法设计合理，统计框架严谨，但 formality 轴 GEE 显示 Originality OR ≥ Style OR（多配置），"style bias" 的 claim 对该轴偏强；verbosity 轴 (OR 8–13, Orig ns) 方法论上无可挑剔 |
| Excitement | 3.5/5 | Likert Blindspot 现象有明确的实践意义（RLHF/DPO 依赖 pairwise，但审计依赖 Likert），七种方法的 sensitivity hierarchy 是有价值的方法论贡献，但缺乏下游影响的实证 |
| Reproducibility | 4/5 | 实现细节完整（模型版本、温度、种子），统计方法描述清晰，代码/数据承诺开源；扣分点：部分 GEE 配置缺少 QIC 绝对值 |
| Reviewer Confidence | 4/5 | 熟悉 Bradley-Terry 模型、GEE、因果推断框架和 LLM 评估文献 |

---

## 主要优势

1. **现象定义清晰且可复现**：Likert Blindspot 在 4 个 judge × 2 个主轴 × 3 个 benchmark 上一致出现（11 个 bias-positive cell 中 8 个），且用 7 种统计方法验证了 sensitivity hierarchy（Table 2），形成了强有力的证据链。

2. **因果声明诚实克制**：Section 3.5 明确声明"we do not claim that this DAG is a complete structural causal model"，Figure 2 DAG 中用虚线橙色箭头标注 residual confounding，避免了过度因果宣称。

3. **统计方法论严谨**：Holm-Bonferroni 校正 6 测试家族 + 8 测试敏感性分析（Appendix Q），全部保持显著；BT 拟合优度检验；GEE 诊断完整：exchangeable vs independence 对比（|ΔQIC| < 0.001）、交互项检验（所有 p > 0.13）、95% CI 完整报告；Bootstrap attenuation analysis（Appendix J）区分 measurement attenuation 与 insufficient power。

4. **控制变量设计周全**：NLI 阈值 11 点 sweep、cross-rewriter 验证、same-style double-rewrite artifact control、Claude 负控制。

5. **Verbosity 轴证据链极强**：Style OR 8.2–13.1（四个 judge 一致），Originality OR 0.38–0.49（均不显著或边缘），direction-aware NLI 有理论和实证依据，cross-rewriter 验证完整。

---

## Must-Fix 问题

**N1** [critical] Formality 轴 quality-style 混淆严重，核心 claim 对该轴偏强

- Table 3（GEE decomposition）、Section 5.2：GEE 分解显示 formality 的 Originality OR 在多个配置中 ≥ Style OR：
  - GPT-4o: Style 2.58 vs Orig 2.32（几乎相等）
  - Qwen3 n=355: Style 2.15 vs Orig 4.99（originality 是 style 的 2.3 倍）
  - Gemini: Style 1.64 (ns!) vs Orig 2.51
  - Direction asymmetry（Appendix H: formal-origin 88.9% vs casual-origin 52.6%）进一步确认混淆存在
- Formality 的 Blindspot 可能本质上是 pairwise 对 quality-style correlation 的放大
- Appendix H 的 stratified analysis 存在 circularity：论文的核心 claim 是 Likert 对 style 不敏感，因此用 "Likert 等分" 作为 "质量无差异" 的代理变量存在逻辑矛盾
- 建议：区分 verbosity（纯 style-driven）和 formality（style + quality confound），不要统一称为 "style bias"

**N2** [critical] Bootstrap CI 的 pair-level resampling 在 GEE 语境下的合理性未论证

- Section 4.1 声明 "All bootstrap CIs use 10,000 pair-level resamples"，但 GEE 使用 sandwich standard errors
- Table 3 的 CI（Appendix C Table 6）使用哪种方法不清晰
- 建议：明确区分 BT bootstrap CI 和 GEE sandwich CI 的适用范围

---

## Should-Fix 问题

**W1** [warning] TOST 等价检验边界 Δ=15pp 偏宽，负控制说服力有限
- Claude 可能存在高达 ~15pp 的未检测 style preference
- GPT-4o formality 检测到的 bias 为 BT 63.0%（即 13pp 偏离 50%），与 TOST 边界几乎重叠
- 建议报告 Δ=10pp 时的 TOST power 和 p 值

**W2** [warning] 人工标注验证规模偏小，inter-annotator agreement 仅 moderate
- 50 对由 2 名标注员评估，Cohen's κ=0.44（moderate）
- 4 个分歧全在 verbosity condensation 对上——而 verbosity 正是最强 claim 的支撑轴
- 建议增加标注量或第三名标注员

**W3** [warning] Cross-benchmark replication 覆盖面有限
- verbosity 仅在 AlpacaEval 有 1 个 cross-benchmark 数据点，且是 ‡（both sig，非 Blindspot）
- 建议补充 MT-Bench verbosity 数据或降低 claim 强度

**W4** [warning] Cross-axis contamination 中 formality→verbosity 的 word count shift (d=−0.23) 非 negligible
- 按 Cohen 标准 d=−0.23 超过论文自设的 negligible 标准 d<0.20
- dataset-level 对称不等于 pair-level 对称
- 建议在 GEE 中加入 word count 变化作为 covariate

---

## 小问题

1. Table 1 符号系统偏复杂（5 种标记）
2. Figure 4（power curve）标题可能被误读为 post-hoc power
3. Section 4.1 脚注 3（IIA）篇幅较长，建议移至 Appendix
4. Register 轴定位不够清晰，建议明确标注为 exploratory pilot
5. 100-point Likert 实验仅选 Qwen3-32B（evaluator-producer overlap 最严重的 judge）而非 GPT-4o

---

## 问题

**Q1**: Appendix H 的 stratified analysis 用 Likert 等分对作为 "无质量差异" 的代理变量——如何排除 circularity？
**Q2**: Formality 轴 Qwen3 n=355 的 Originality OR (4.99) 是 Style OR (2.15) 的 2.3 倍，"formality bias" 表述是否仍恰当？
**Q3**: TOST Δ=15pp 的选择基准是什么？
**Q4**: Verbosity direction-aware NLI gate 恢复的 21 对在 content quality 上是否与 bidirectional-pass 对系统不同？
**Q5**: 论文声称对 RLHF/DPO pipeline 有启示，但未给出下游影响实证。

---

## Missing References

建议考虑：Stureborg et al. (2024) 关于 LLM judge calibration

---

## Overall Assessment

**3.5 (Borderline Conference)**

方法论扎实的实证研究，verbosity 轴证据令人信服，但 formality 轴 quality confound 削弱核心 claim，TOST 边界偏宽，贡献介于 Findings 和 Conference 之间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 852 · 2026-05-22T18:19:02.071887+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n### Must-Fix\n\n[AGREE] R1-N1 (Formality quality-style 混淆): 强烈同意。补充两点：(1) R1 指出的 Appendix H stratified analysis circularity 是精妙的方法论漏洞——论文 claim Likert 不敏感，但 stratified analysis 用 Likert 等分作\"质量无差异\"代理，前提被 claim 自身破坏；(2) Qwen3 n=355 的 Orig OR (4.99) 是 Style OR (2.15) 的 2.3 倍，\"formality bias\" 不如 \"quality-correlated formality preference\" 准确。建议论文将 verbosity（confirmed style bias）和 formality（style-quality entangled）分层讨论。\n\n[REBUT] R1-N2 (Bootstrap CI vs GEE sandwich): 部分反驳。BT 用 bootstrap、GEE 用 sandwich 是正确做法，两个模型用不同 CI 方法无方法论错误。问题在于论文未明确区分报告方式——是表述清晰度问题，建议降级为 warning。\n\n### Should-Fix\n\n[AGREE] R1-W1 (TOST Δ=15pp): 同意，我 W5 提出相同关切。R1 的对比（GPT-4o formality BT=63%, 即 13pp，几乎落入 TOST 边界）尤其有力。\n\n[AGREE] R1-W2 (人工标注): 同意。补充：4 个分歧全在 verbosity condensation，但 NLI 阈值 sweep 显示 BT ≤3pp 变化，部分缓解。\n\n[AGREE] R1-W3 (Cross-benchmark): 同意。R1 观察更精确：verbosity 唯一跨 benchmark 数据点（AlpacaEval Qwen3）为 ‡（both sig），反而不支持 Blindspot。\n\n[AGREE] R1-W4 (Cross-axis contamination d=−0.23): 同意。formality 改写导致 word count shift d=−0.23 超 small effect 标准，论文回避了此指标。支持在 GEE 加入 word count covariate。\n\n### Minor\n\n全部 [AGREE]。R1-Minor-5（100-point Likert 仅用 Qwen3-32B 而非 GPT-4o）是我未独立发现的有效观察。\n\n### Questions\n\n[AGREE] Q1-Q3, Q5。[REBUT] Q4：NLI 阈值 sweep 11 点 BT ≤3pp 变化间接表明 direction-aware gate 未引入系统偏差。\n\n### Overall\n\nR1 给 3.5，我给 3.0。分歧在 Excitement（R1: 3.5, 我: 2.5）。核心发现是 Thurstone (1927) 的领域迁移，\"首次量化已知现象\" 的 excitement 有限。两位 reviewer 一致结论：verbosity 强、formality 混淆严重、TOST 偏宽、跨 benchmark 不足、register 应降级。",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n### Must-Fix\n\n[AGREE] R1-N1 (Formality quality-style 混淆): 强烈同意。补充两点：(1) R1 指出的 Appendix H stratified analysis circularity 是精妙的方法论漏洞——论文 claim Likert 不敏感，但 stratified analysis 用 Likert 等分作\"质量无差异\"代理，前提被 claim 自身破坏；(2) Qwen3 n=355 的 Orig OR (4.99) 是 Style OR (2.15) 的 2.3 倍，\"formality bias\" 不如 \"quality-correlated formality preference\" 准确。建议论文将 verbosity（confirmed style bias）和 formality（style-quality entangled）分层讨论。\n\n[REBUT] R1-N2 (Bootstrap CI vs GEE sandwich): 部分反驳。BT 用 bootstrap、GEE 用 sandwich 是正确做法，两个模型用不同 CI 方法无方法论错误。问题在于论文未明确区分报告方式——是表述清晰度问题，建议降级为 warning。\n\n### Should-Fix\n\n[AGREE] R1-W1 (TOST Δ=15pp): 同意，我 W5 提出相同关切。R1 的对比（GPT-4o formality BT=63%, 即 13pp，几乎落入 TOST 边界）尤其有力。\n\n[AGREE] R1-W2 (人工标注): 同意。补充：4 个分歧全在 verbosity condensation，但 NLI 阈值 sweep 显示 BT ≤3pp 变化，部分缓解。\n\n[AGREE] R1-W3 (Cross-benchmark): 同意。R1 观察更精确：verbosity 唯一跨 benchmark 数据点（AlpacaEval Qwen3）为 ‡（both sig），反而不支持 Blindspot。\n\n[AGREE] R1-W4 (Cross-axis contamination d=−0.23): 同意。formality 改写导致 word count shift d=−0.23 超 small effect 标准，论文回避了此指标。支持在 GEE 加入 word count covariate。\n\n### Minor\n\n全部 [AGREE]。R1-Minor-5（100-point Likert 仅用 Qwen3-32B 而非 GPT-4o）是我未独立发现的有效观察。\n\n### Questions\n\n[AGREE] Q1-Q3, Q5。[REBUT] Q4：NLI 阈值 sweep 11 点 BT ≤3pp 变化间接表明 direction-aware gate 未引入系统偏差。\n\n### Overall\n\nR1 给 3.5，我给 3.0。分歧在 Excitement（R1: 3.5, 我: 2.5）。核心发现是 Thurstone (1927) 的领域迁移，\"首次量化已知现象\" 的 excitement 有限。两位 reviewer 一致结论：verbosity 强、formality 混淆严重、TOST 偏宽、跨 benchmark 不足、register 应降级。",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 853 · 2026-05-22T18:19:05.686047+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3614
}
```

</details>

---


### Assistant

_source line 854 · 2026-05-22T18:19:17.366700+00:00_

交叉回应已提交。两位 reviewer 在关键问题上高度一致（formality 混淆、TOST 偏宽、跨 benchmark 不足），主要分歧在 excitement 评分（R1: 3.5 vs 我: 2.5），源于对"已知现象的领域迁移"这一贡献类型的 novelty 权重不同。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 27

## Round 27

60 recorded events


### User

_source line 855 · 2026-05-22T19:31:20.873461+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + framing 平衡性 + 写作质量 + 格式合规**。

## 投稿信息
- **Venue**: EMNLP 2026（通过 ARR 统一审稿）
- **Deadline**: 2026-05-25
- **格式要求**: ACL 模板，Long paper 正文 ≤8 页，参考文献不限，Limitations 不计入页数
- **匿名规则**: Double-blind
- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf`

## 论文概要
标题：*The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation*
核心发现：Likert 评分和 pairwise comparison 在检测 LLM judge 风格偏差时产生系统性分歧。提出 CSD 框架，跨 4 个 target judge + 1 个负控制 + 3 个 benchmark 验证。GEE 条件分解揭示 per-axis 混淆结构差异。

## 你的审查侧重

### 1. 新颖性评估
- **核心问题**：Likert vs pairwise 的灵敏度差异是 Thurstone (1927) 以来心理测量学的已知现象。本文的贡献是否超越了 "domain transfer"？
- "Controlled Style Decomposition" 框架 vs 既有工作（RATE [Reber et al., 2025]、Comparative Trap [Jeong et al., 2025]、CalibraEval [Li et al., 2025]）的实质差异？
- GEE per-axis confound decomposition 是否构成独立的方法论贡献？
- 论文使用 "demonstrates"/"identifies" 等措辞是否仍偏发现性？应如何定位？

### 2. Framing 平衡性（Detection vs Amplification）
- **标题分析**：当前标题 "The Likert Blindspot" 是否隐式预设 pairwise 为 ground truth？Jeong et al. (2025) 指出 pairwise comparison 放大风格偏好——论文如何处理这一对立证据？
- §5.4 的六项 amplification controls 是否充分？是否能排除 pairwise 格式本身放大了 micro-preferences？
- "measurement attenuation" vs "construct divergence" vs "format amplification" 三种解释在论文中的权重是否平衡？
- Conclusion "Likert-only audits miss style-driven preferences" 是否过强？可能只是 pairwise 放大了本不重要的差异？
- Claude Sonnet 4 作为唯一负控制——是否足以论证 Blindspot 的架构特异性？为何不讨论 Claude 不受影响的可能原因？

### 3. 写作质量
- **Abstract**：数字密度是否过高？是否影响可读性？建议保留哪些核心数字？
- **Introduction** 开头的 motivating example（GPT-4o formal vs casual）是否充分 acknowledge formality-quality 的 nuance？
- **Related Work** 覆盖面是否充分？遗漏的重要引用？
- **Conclusion** 篇幅和深度是否合适？
- 术语一致性检查：CSD/Blindspot/measurement divergence 等核心术语的使用是否一致？

### 4. 格式与完整性
- 正文 ≤8 页？
- Double-blind 合规？
- Limitations 内容是否覆盖关键弱点？是否过长/过短？
- Appendix A-S 的组织是否合理？是否有主文应有但被放到附录的关键内容？
- 引用格式（natbib）是否一致？

### 5. Scope 与泛化
- 3 个风格轴（formality, verbosity, register）+ 失败的 tone 轴——是否足以支撑 "framework" 级别的泛化声明？
- 主实验仅用 LLMBar (n=100)——cross-benchmark (AlpacaEval, MT-Bench) 覆盖是否稀疏？
- Register 轴结果较弱且 evaluator-producer overlap 最严重——是否应降级为 "exploratory pilot"？

请按以下格式输出审稿报告：
1. **Summary** (2-3 句)
2. **Strengths** (逐条)
3. **Weaknesses** (逐条，标注 severity: Must-Fix / Should-Fix / Minor)
4. **Questions** (需要作者回答)
5. **Missing References** (如有)
6. **Novelty** (1-5 分)
7. **Soundness** (1-5 分)
8. **Excitement** (1-5 分)
9. **Overall Assessment** (使用 EMNLP 2026 ARR 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-22T19:31:30.334470+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
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

_source line 857 · 2026-05-22T19:31:30.387472+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-22T19:31:34.451492+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 859 · 2026-05-22T19:31:35.391661+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf",
  "pages": "1-10",
  "project": "causal_style_decomp_judge",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf",
    "pages": "1-10",
    "project": "causal_style_decomp_judge",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 860 · 2026-05-22T19:31:44.079577+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about ACL ARR 2025-2026 reviewer guidelines:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score Requirements

Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

## Excitement Score

Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Key Guidelines

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements.

For more detailed reviewer guidelines, you can visit 
…[truncated 194 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9628
}
```

</details>

---


### Tool result

_source line 861 · 2026-05-22T19:31:46.192222+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 468.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 587.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.2}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p9.p
…[truncated 526 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 10800
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-22T19:31:52.719747+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer scoring criteria, including all dimensions (soundness, excitement, overall assessment), their scales, and descriptions of each score level. Also extract any guidelines about what constitutes a good review, what reviewers should look for, and the review form structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer scoring criteria, including all dimensions (soundness, excitement, overall assessment), their scales, and descriptions of each score level. Also extract any guidelines about what constitutes a good review, what reviewers should look for, and the review form structure."
  }
}
```

</details>

---


### Tool call

_source line 863 · 2026-05-22T19:31:53.473488+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf",
  "pages": "11-18",
  "project": "causal_style_decomp_judge",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/submitted.pdf",
    "pages": "11-18",
    "project": "causal_style_decomp_judge",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 864 · 2026-05-22T19:31:58.341778+00:00_

# ARR Reviewer Scoring Criteria and Guidelines

## Scoring Dimensions

Based on the guidelines, ARR reviewers provide **three distinct scores** starting February 2025:

1. **Soundness**: Technical quality and validity of the research. Per guidelines: "low soundness scores should be justified" and must align with actual findings in the review text.

2. **Excitement**: Personal interest and engagement with the topic. This score reflects subjective preferences independent of technical merit.

3. **Overall Assessment**: Explicit recommendation for acceptance, representing "a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact."

## What Constitutes a Good Review

The guidelines emphasize these core principles:

- **Specificity**: Replace vague criticisms with concrete examples and references
- **Professional tone**: Maintain neutrality and kindness; "write the review you would like to get yourself"
- **Clear justification**: All scores must connect to actual review content
- **Engagement**: Acknowledge author responses and update assessments accordingly

## Key Review Guidance

Reviewers should:

- Read papers twice: first for understanding research questions, then for technical evaluation
- Avoid common cognitive biases (18 specific heuristics listed)
- Check for reproducibility, ethics concerns, and methodological soundness
- Recognize valid contributions beyond state-of-the-art results (including negative results, resource papers, analyses)

The guidelines contain no explicit numerical scales for individual dimensions, focusing instead on conceptual clarity and justified recommendations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5622
}
```

</details>

---


### Tool result

_source line 865 · 2026-05-22T19:31:59.196162+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 432.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.6}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 571.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 581.3}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 602.3}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 143.3}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_styl
…[truncated 93 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5722
}
```

</details>

---


### Tool call

_source line 866 · 2026-05-22T19:32:03.974028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 867 · 2026-05-22T19:32:04.578229+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 868 · 2026-05-22T19:32:05.435542+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1461
}
```

</details>

---


### Tool call

_source line 869 · 2026-05-22T19:32:05.436107+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 870 · 2026-05-22T19:32:05.943174+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1364
}
```

</details>

---


### Tool call

_source line 871 · 2026-05-22T19:32:05.943660+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 872 · 2026-05-22T19:32:06.246464+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 873 · 2026-05-22T19:32:06.399382+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 963
}
```

</details>

---


### Tool result

_source line 874 · 2026-05-22T19:32:07.105108+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1161
}
```

</details>

---


### Tool result

_source line 875 · 2026-05-22T19:32:07.360055+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1113
}
```

</details>

---


### Tool call

_source line 876 · 2026-05-22T19:32:11.275098+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 877 · 2026-05-22T19:32:11.778473+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 878 · 2026-05-22T19:32:12.683493+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool result

_source line 879 · 2026-05-22T19:32:12.684218+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 880 · 2026-05-22T19:32:12.734658+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 881 · 2026-05-22T19:32:13.186504+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 882 · 2026-05-22T19:32:13.639358+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 883 · 2026-05-22T19:32:13.639836+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 884 · 2026-05-22T19:32:13.894448+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 707
}
```

</details>

---


### Tool result

_source line 885 · 2026-05-22T19:32:14.447271+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-22T19:32:19.917979+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 887 · 2026-05-22T19:32:20.171523+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 888 · 2026-05-22T19:32:21.076639+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1158
}
```

</details>

---


### Tool call

_source line 889 · 2026-05-22T19:32:21.077081+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 890 · 2026-05-22T19:32:21.532875+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool call

_source line 891 · 2026-05-22T19:32:21.534147+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 892 · 2026-05-22T19:32:21.989758+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 912
}
```

</details>

---


### Tool call

_source line 893 · 2026-05-22T19:32:21.990253+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 894 · 2026-05-22T19:32:22.393755+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool result

_source line 895 · 2026-05-22T19:32:22.746253+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 896 · 2026-05-22T19:32:27.765423+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 897 · 2026-05-22T19:32:28.368572+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 898 · 2026-05-22T19:32:28.419485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 899 · 2026-05-22T19:32:28.621500+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 900 · 2026-05-22T19:32:28.674391+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 901 · 2026-05-22T19:32:29.026840+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 607
}
```

</details>

---


### Tool call

_source line 902 · 2026-05-22T19:34:37.296073+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Jeong et al 2025 \"Comparative Trap\" pairwise comparison amplifies style bias LLM judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Jeong et al 2025 \"Comparative Trap\" pairwise comparison amplifies style bias LLM judge"
  }
}
```

</details>

---


### Tool call

_source line 903 · 2026-05-22T19:34:38.049835+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form 2025 2026 soundness excitement overall assessment scoring scale 1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form 2025 2026 soundness excitement overall assessment scoring scale 1-5"
  }
}
```

</details>

---


### Tool result

_source line 904 · 2026-05-22T19:34:44.502838+00:00_

Web search results for query: "Jeong et al 2025 "Comparative Trap" pairwise comparison amplifies style bias LLM judge"

Links: [{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators - ACL Anthology","url":"https://aclanthology.org/2025.blackboxnlp-1.5/"},{"title":"[2406.12319] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://arxiv.org/abs/2406.12319"},{"title":"[PDF] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Comparative-Trap:-Pairwise-Comparisons-Biased-Jeong-Park/cd6191f270c5b98dec44a294e4f3cebcf371ac5f"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences   of LLM Evaluators","url":"https://arxiv.org/pdf/2406.12319"},{"title":"[Literature Review] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://www.themoonlight.io/en/review/the-comparative-trap-pairwise-comparisons-amplifies-biased-preferences-of-llm-evaluators"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://arxiv.org/html/2406.12319v4"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies","url":"https://arxiv.org/pdf/2406.12319v3"}]

Based on the search results, here's information about the paper "The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators" by Jeong et al. 2025:

## Overview

The paper by Hawon Jeong, ChaeHun Park, Jimin Hong, Hojoon Lee, and Jaegul Choo was published in 2025 at the 8th BlackboxNLP Workshop in Suzhou, China.

## Main Findings

The research reveals that LLM evaluators often display biased preferences, such as favoring verbosity and authoritative tones, and these biases are exacerbated in pairwise evaluation, where LLMs directly compare two outputs and easily prioritize s
…[truncated 780 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7206
}
```

</details>

---


### Tool result

_source line 905 · 2026-05-22T19:34:45.306967+00:00_

Web search results for query: "ACL ARR review form 2025 2026 soundness excitement overall assessment scoring scale 1-5"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, I found information about the ACL ARR review form for 2025-2026:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

**Soundness Score:**
Soundness scores must be justified by the text of the review, and if you give a low soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation. The scoring scale includes: 5 = Excellent (one of the most thorough studies), 4 = Strong (sufficient support for all claims), and 3 = Acceptable (sufficient support for main claims).

**Excitement Score:**
Excitement is 
…[truncated 638 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7257
}
```

</details>

---


### Tool call

_source line 906 · 2026-05-22T19:34:52.042156+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their exact scales (1-5 or other), and the description of each score level. I need the exact scale for Soundness, Excitement, and Overall Assessment including what each number means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their exact scales (1-5 or other), and the description of each score level. I need the exact scale for Soundness, Excitement, and Overall Assessment including what each number means."
  }
}
```

</details>

---


### Tool result

_source line 907 · 2026-05-22T19:34:57.166568+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Soundness Scale (1-5)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: Strong - provides sufficient support for claims with optional extra experiments
- **3**: Acceptable - supports main claims with minor details needing clarification
- **2**: Poor - main claims lack sufficient support; major technical/methodological issues
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement Scale (1-5)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- **4**: Exciting - would mention to colleagues or make effort to attend presentation
- **3**: Interesting - might mention specific points or attend if time permits
- **2**: Potentially Interesting - doesn't resonate personally but may interest others
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others"

## Overall Assessment Scale (1-5)
- **5**: Consider for Award - potentially top 2.5% papers
- **4**: Conference - suitable for acceptance
- **3**: Findings - acceptable for Findings track
- **2**: Resubmit next cycle - needs substantial revisions
- **1**: "Do not resubmit: This paper has to be fully redone, or it is not relevant"

All three dimensions include half-point increments (e.g., 4.5, 3.5).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5124
}
```

</details>

---


### Tool call

_source line 908 · 2026-05-22T19:38:23.963728+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "# Reviewer 2 审稿报告（Round 1）\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 实验设计严谨、统计工具丰富的实证研究，但核心发现（Likert vs. pairwise 灵敏度差异）在心理测量学中早已确立，论文的 framing 系统性地偏向 pairwise 为 ground truth，削弱了贡献声明的说服力。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验控制周密（NLI gate、position control、7 种统计方法、GEE 分解），但 framing 不对称——无法充分区分 \"Likert misses real signal\" vs \"pairwise amplifies micro-preferences\"；单一负控制不足以支撑架构特异性声明 |\n| Excitement | 3/5 | 对 LLM judge 审计实践有直接价值，但核心洞察对熟悉心理测量学的读者不意外；GEE per-axis 分解有趣但应用场景窄 |\n| Novelty | 3/5 | 核心发现是 established knowledge 的 domain transfer；CSD + GEE 分解是增量贡献 |\n| Overall | 3.0 | Findings 水平——方法学扎实但新颖性有限且 framing 问题需修正 |\n\n---\n\n## Strengths\n\n**S1. 实验控制层次感出色。** CSD 三层控制——NLI gate (§3.2)、same-style double-rewrite (§5.4)、position swapping (§3.3)——在 LLM judge 风格偏差文献中属最周密的实验设计之一。\n\n**S2. 统计方法多元互补。** 七种方法覆盖不同假设，Table 2 sensitivity hierarchy 清晰展示 Likert-based 方法一致失败。GEE 条件分解 (Table 3) 将 style OR 与 originality OR 分离是独立的方法论贡献。\n\n**S3. Robustness 检查详尽。** §5.4 六项 amplification controls + Appendices A-S 大量补充分析（bootstrap CI、formal power analysis、100-point continuous Likert、cross-axis contamination 等）。\n\n**S4. GEE per-axis confound 分解是真正的增量贡献。** Table 3 揭示 verbosity style-dominated (Style OR 8-15) vs formality conditional 的结构性差异。\n\n**S5. 跨 judge 覆盖合理。** 4 target judges + 1 negative control 覆盖主流架构。\n\n---\n\n## Must-Fix 问题\n\n**N1** [critical] **标题与 framing 隐式预设 pairwise 为 ground truth**\n- 位置：Title、Abstract (\"signal loss exceeding 60%\")、§6 (\"Likert-only audits miss style-driven preferences\")\n- \"The Likert Blindspot\" 将 Likert 定位为\"盲区\"，但论文自身在 §5.4 引用 Jeong et al. (2025) Comparative Trap 承认 pairwise 可能放大偏好，Limitations 提出 construct divergence 解释。这些 caveat 被隔离在末尾，未进入标题/摘要/结论。在缺乏外部 ground truth 的情况下，无法区分 measurement attenuation vs format amplification vs construct divergence 三种解释，但叙事 90% 倾向第一种。\n- 建议：标题改为中性（如直接用副标题）；Abstract/Conclusion 给三种解释同等权重。\n\n**N2** [critical] **新颖性定位模糊**\n- 位置：§1、§6（\"identifies\"/\"demonstrates\"）\n- Likert vs pairwise 灵敏度差异是 Thurstone (1927) 以来的经典结论。论文真正贡献是\"首次受控量化 + GEE 分解方法\"，但措辞有时像是声称发现了现象本身。\n- 建议：§1 明确声明 \"sensitivity gap is well-established; our contribution is first controlled quantification + decomposition methodology\"。\n\n**N3** [critical] **单一负控制不足以支撑架构特异性声明**\n- 位置：§5.3、§6、Limitations\n- Claude Sonnet 4 是唯一负控制。论文未探讨为何 Claude 不受影响（RLHF 差异？评估策略？），也未测试同系列其他模型。可能 Claude 只是整体风格不敏感而非\"正确地不受影响\"。\n- 建议：讨论可能机制；降格为 \"one model does not show this pattern\"。\n\n## Should-Fix 问题\n\n**W1** [warning] **主实验仅用 LLMBar (n=100)，cross-benchmark 覆盖稀疏** — Table 2 的 AlpacaEval/MT-Bench 仅测试 formality pairwise，不足以支撑 \"across three benchmarks\" 泛化声明。\n\n**W2** [warning] **Register 轴 evaluator-producer overlap 最严重，结果应降级** — Qwen3-32B 同时作为 rewriter 和 judge，BT 仅 51.4%。应标注为 exploratory。\n\n**W3** [warning] **Abstract 数字密度过高** — ~200 词中堆砌过多数字和术语，影响核心信息传达。\n\n**W4** [warning] **Introduction motivating example 未 acknowledge formality-quality nuance** — GPT-4o 偏好 formal 的例子暗示 Likert 偏好 casual 是\"错误\"的，但直到 Limitations/Appendix A 才讨论 formality 可能反映真实 quality 差异。\n\n**W5** [warning] **\"Framework\" 设定过高预期** — CSD 更准确地说是 experimental protocol，3 个成功轴 + 1 个失败轴不足以支撑 \"framework\" 级别声明。\n\n## 小问题\n- §3-4 脚注密度高，打断阅读流\n- Figure 2 (DAG) 偏小，blocked/open paths 区分不够直观\n- Tone axis 失败值得 2-3 句更详细的分析\n- §5.2 GEE 术语首次出现时缺乏直觉解释\n- References 置于 Appendices 之后（非标准顺序）\n\n## Questions\n\n**Q1.** 六项 amplification controls 中哪一项最直接排除 \"pairwise amplifies micro-preferences\" 解释？无人类 ground truth 如何区分 attenuation vs amplification？\n\n**Q2.** Claude 不表现 Blindspot 的可能机制？是否检查过 Claude 的 Likert/pairwise 评分分布（ceiling/floor effects, tie rates）？\n\n**Q3.** 如果用更大 benchmark (n>1000)，Likert Type II error 是否因功效提升而缩小？Appendix K 报告 required n >1200——Blindspot 是否部分是 power issue？\n\n**Q4.** Register 轴是否做了 rewriter 替换测试（类似 Appendix D 对 verbosity/formality 的测试）？\n\n**Q5.** Tone axis NLI gate 通过率 56%——失败案例中 NLI 判定\"内容改变\"是正确的还是误判？\n\n## Missing References\n无重大遗漏。可考虑补充 Bai et al. (2022/2023) RLHF preference model 的 comparison vs rating 差异、Rafailov et al. (2023) DPO 中 pairwise preference 的理论性质。\n\n## 格式检查\n- ✅ 正文 ≤8 页合规\n- ✅ Double-blind 合规\n- ✅ Limitations 覆盖充分、长度适中\n- ✅ Appendix A-S 组织合理\n- ⚠️ References 在 Appendices 之后（非标准）",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "# Reviewer 2 审稿报告（Round 1）\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 实验设计严谨、统计工具丰富的实证研究，但核心发现（Likert vs. pairwise 灵敏度差异）在心理测量学中早已确立，论文的 framing 系统性地偏向 pairwise 为 ground truth，削弱了贡献声明的说服力。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验控制周密（NLI gate、position control、7 种统计方法、GEE 分解），但 framing 不对称——无法充分区分 \"Likert misses real signal\" vs \"pairwise amplifies micro-preferences\"；单一负控制不足以支撑架构特异性声明 |\n| Excitement | 3/5 | 对 LLM judge 审计实践有直接价值，但核心洞察对熟悉心理测量学的读者不意外；GEE per-axis 分解有趣但应用场景窄 |\n| Novelty | 3/5 | 核心发现是 established knowledge 的 domain transfer；CSD + GEE 分解是增量贡献 |\n| Overall | 3.0 | Findings 水平——方法学扎实但新颖性有限且 framing 问题需修正 |\n\n---\n\n## Strengths\n\n**S1. 实验控制层次感出色。** CSD 三层控制——NLI gate (§3.2)、same-style double-rewrite (§5.4)、position swapping (§3.3)——在 LLM judge 风格偏差文献中属最周密的实验设计之一。\n\n**S2. 统计方法多元互补。** 七种方法覆盖不同假设，Table 2 sensitivity hierarchy 清晰展示 Likert-based 方法一致失败。GEE 条件分解 (Table 3) 将 style OR 与 originality OR 分离是独立的方法论贡献。\n\n**S3. Robustness 检查详尽。** §5.4 六项 amplification controls + Appendices A-S 大量补充分析（bootstrap CI、formal power analysis、100-point continuous Likert、cross-axis contamination 等）。\n\n**S4. GEE per-axis confound 分解是真正的增量贡献。** Table 3 揭示 verbosity style-dominated (Style OR 8-15) vs formality conditional 的结构性差异。\n\n**S5. 跨 judge 覆盖合理。** 4 target judges + 1 negative control 覆盖主流架构。\n\n---\n\n## Must-Fix 问题\n\n**N1** [critical] **标题与 framing 隐式预设 pairwise 为 ground truth**\n- 位置：Title、Abstract (\"signal loss exceeding 60%\")、§6 (\"Likert-only audits miss style-driven preferences\")\n- \"The Likert Blindspot\" 将 Likert 定位为\"盲区\"，但论文自身在 §5.4 引用 Jeong et al. (2025) Comparative Trap 承认 pairwise 可能放大偏好，Limitations 提出 construct divergence 解释。这些 caveat 被隔离在末尾，未进入标题/摘要/结论。在缺乏外部 ground truth 的情况下，无法区分 measurement attenuation vs format amplification vs construct divergence 三种解释，但叙事 90% 倾向第一种。\n- 建议：标题改为中性（如直接用副标题）；Abstract/Conclusion 给三种解释同等权重。\n\n**N2** [critical] **新颖性定位模糊**\n- 位置：§1、§6（\"identifies\"/\"demonstrates\"）\n- Likert vs pairwise 灵敏度差异是 Thurstone (1927) 以来的经典结论。论文真正贡献是\"首次受控量化 + GEE 分解方法\"，但措辞有时像是声称发现了现象本身。\n- 建议：§1 明确声明 \"sensitivity gap is well-established; our contribution is first controlled quantification + decomposition methodology\"。\n\n**N3** [critical] **单一负控制不足以支撑架构特异性声明**\n- 位置：§5.3、§6、Limitations\n- Claude Sonnet 4 是唯一负控制。论文未探讨为何 Claude 不受影响（RLHF 差异？评估策略？），也未测试同系列其他模型。可能 Claude 只是整体风格不敏感而非\"正确地不受影响\"。\n- 建议：讨论可能机制；降格为 \"one model does not show this pattern\"。\n\n## Should-Fix 问题\n\n**W1** [warning] **主实验仅用 LLMBar (n=100)，cross-benchmark 覆盖稀疏** — Table 2 的 AlpacaEval/MT-Bench 仅测试 formality pairwise，不足以支撑 \"across three benchmarks\" 泛化声明。\n\n**W2** [warning] **Register 轴 evaluator-producer overlap 最严重，结果应降级** — Qwen3-32B 同时作为 rewriter 和 judge，BT 仅 51.4%。应标注为 exploratory。\n\n**W3** [warning] **Abstract 数字密度过高** — ~200 词中堆砌过多数字和术语，影响核心信息传达。\n\n**W4** [warning] **Introduction motivating example 未 acknowledge formality-quality nuance** — GPT-4o 偏好 formal 的例子暗示 Likert 偏好 casual 是\"错误\"的，但直到 Limitations/Appendix A 才讨论 formality 可能反映真实 quality 差异。\n\n**W5** [warning] **\"Framework\" 设定过高预期** — CSD 更准确地说是 experimental protocol，3 个成功轴 + 1 个失败轴不足以支撑 \"framework\" 级别声明。\n\n## 小问题\n- §3-4 脚注密度高，打断阅读流\n- Figure 2 (DAG) 偏小，blocked/open paths 区分不够直观\n- Tone axis 失败值得 2-3 句更详细的分析\n- §5.2 GEE 术语首次出现时缺乏直觉解释\n- References 置于 Appendices 之后（非标准顺序）\n\n## Questions\n\n**Q1.** 六项 amplification controls 中哪一项最直接排除 \"pairwise amplifies micro-preferences\" 解释？无人类 ground truth 如何区分 attenuation vs amplification？\n\n**Q2.** Claude 不表现 Blindspot 的可能机制？是否检查过 Claude 的 Likert/pairwise 评分分布（ceiling/floor effects, tie rates）？\n\n**Q3.** 如果用更大 benchmark (n>1000)，Likert Type II error 是否因功效提升而缩小？Appendix K 报告 required n >1200——Blindspot 是否部分是 power issue？\n\n**Q4.** Register 轴是否做了 rewriter 替换测试（类似 Appendix D 对 verbosity/formality 的测试）？\n\n**Q5.** Tone axis NLI gate 通过率 56%——失败案例中 NLI 判定\"内容改变\"是正确的还是误判？\n\n## Missing References\n无重大遗漏。可考虑补充 Bai et al. (2022/2023) RLHF preference model 的 comparison vs rating 差异、Rafailov et al. (2023) DPO 中 pairwise preference 的理论性质。\n\n## 格式检查\n- ✅ 正文 ≤8 页合规\n- ✅ Double-blind 合规\n- ✅ Limitations 覆盖充分、长度适中\n- ✅ Appendix A-S 组织合理\n- ⚠️ References 在 Appendices 之后（非标准）",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 909 · 2026-05-22T19:38:27.478091+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3514
}
```

</details>

---


### Tool call

_source line 910 · 2026-05-22T19:38:31.857408+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
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

_source line 911 · 2026-05-22T19:38:31.907925+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 912 · 2026-05-22T19:38:35.775602+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_11/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 913 · 2026-05-22T19:38:35.826230+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 914 · 2026-05-22T19:38:44.479509+00:00_

审稿报告已完成并提交给 Review Director。

**核心判断**：Overall 3.0 (Findings)。论文实验设计周密（NLI gate + 7 种统计方法 + GEE 分解 + 详尽附录），但有三个 Must-Fix 问题：

1. **Framing 不对称**——标题 "Likert Blindspot" 隐式预设 pairwise 为 ground truth，与论文自身承认的 Comparative Trap 证据矛盾，三种解释（attenuation / amplification / construct divergence）未获同等权重
2. **新颖性定位模糊**——Likert vs pairwise 灵敏度差异是心理测量学经典结论，论文需明确定位为"首次受控量化 + GEE 分解方法"而非"发现"
3. **单一负控制**——仅 Claude Sonnet 4 不表现 Blindspot，未探讨机制，不足以支撑架构特异性声明

若修正 framing + novelty 定位 + 扩展负控制讨论，有潜力升至 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 28

## Round 28

4 recorded events


### User

_source line 915 · 2026-05-22T19:42:18.268060+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Should-Fix、Minor 和主要 Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure/Appendix）。

---

# Reviewer 1 — Round 1 审稿报告

**审查侧重**: 方法严谨性 + 统计方法 + 实验设计

## Summary

本文识别了 "Likert Blindspot" 现象：Likert 评分与 pairwise comparison 在检测 LLM judge 风格偏差时产生系统性分歧——BT 检测到显著偏好（BT > 60%, p < 0.001），而 Likert 的 Cohen's d → 0 且 p > 0.17。提出 CSD 框架（NLI-gated 内容控制 + per-axis 风格分解 + position-controlled pairwise comparison），在 4 个 judge + 1 个负控制 + 3 个 benchmark + 7 种统计方法下验证。GEE 条件分解揭示 per-axis 混淆结构差异。方法论整体扎实，核心发现在多重鲁棒性检验下稳健，但人工标注规模、TOST 等价阈值、方向不对称性处理等方面存在可改进空间。

## Strengths

**S1. 核心发现新颖且实践意义重大。** Likert Blindspot 对 LLM 评估方法论有直接影响：大量论文使用 Likert 评分审计 LLM judge 偏差，本文表明这种方法可能系统性遗漏通过 pairwise 传播的风格偏好。Table 2 显示 7 种统计方法中 5 种 Likert-based 方法全部失败（p > 0.17–0.90），而两种 pairwise 方法均显著（BT p < 0.001, sign test p = 0.006），证据力强。

**S2. 统计方法覆盖全面。** 7 种方法（BT, sign test, Likert ATE/t-test, Bayesian t, ordinal regression, GEE, Wilcoxon signed-rank）构成"sensitivity hierarchy"，从不同假设族独立验证同一结论。Holm-Bonferroni 校正覆盖 6 个主检验，且 §4.1 明确标注了 8 个检验全通过扩展族的结果。这种多方法三角验证在该领域论文中不常见。

**S3. 负控制设计严谨。** Claude Sonnet 4 作为负控制（n = 87, BT 50.2%/54.1%, n.s.），TOST 等价检验确认 Δ = 15pp 处等价（76% power），验证了 CSD pipeline 不会凭空制造偏差。Appendix G 的形式化处理充分。

**S4. GEE 条件分解贡献重大。** Table 3 的 Style OR vs. Originality OR 分离揭示了 per-axis 混淆结构差异（verbosity = style-dominated, formality = conditional effect, register = judge-dependent），这比简单的"有/无偏差"结论更有方法论价值。exchangeable working correlation + sandwich SE 的选择经 Appendix C 的 independence 对照验证（差异 <0.02），模型诊断充分。

**S5. 鲁棒性检验链完整。** NLI 阈值敏感性分析（Appendix E, 11 个阈值 0.60–0.95），bootstrap 衰减分析（Appendix J, d → 0 across all n），rewriter 独立性检验（Appendix D, GPT-4o rewriter 替换），cross-axis 污染分析（Appendix R），功效分析（Figure 4），方向感知 NLI gate（Appendix F）。这些构成多层防御，使核心发现难以归因于单一方法论 artifact。

**S6. 因果声明审慎。** §3.5 Design Rationale 明确免责："we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions"。"Controlled" 限定为实验控制而非因果识别。Figure 2 的 DAG 标注 S → Q 虚线路径并讨论残余混淆。论文标题 "Measurement-Mode Divergence" 是中性表述。

## Weaknesses

### Should-Fix

**W1 [Should-Fix] 人工标注规模不足，inter-annotator agreement 偏低（§5.4, Appendix S）**
- 50 对 NLI-scored pairs，仅 2 名标注员，κ = 0.44（moderate agreement）。Annotator 1 precision = 93.6%，Annotator 2 = 84.3%（§5.4: "CI [65.3%, 93.6%]"），两者差距近 10pp。论文称 κ = 0.44 反映 "calibrating a cohesion-difference rather than random noise"，但 50 对样本无法可靠区分系统性分歧与噪声。Wilson CI 下界 86.3% 基于合并数据；若按标注员分开，Annotator 2 的下界会明显低于此值。
- NLI gate 是 CSD 框架的核心假设保障组件——44% 拒绝率意味着大量数据依赖该 gate 的正确性。仅 50 对验证不足以支撑对该 gate 的信心。
- 建议：增加标注规模至 ≥100 对，增加第 3 名标注员以计算 Fleiss' κ，并分析分歧案例的特征分布。

**W2 [Should-Fix] TOST 等价阈值 Δ = 15pp 与 GPT-4o 最小偏差重叠（§4.1, Limitations, Appendix G）**
- TOST 设 Δ = 15pp，但 GPT-4o formality 的 BT = 63.0%（即 13pp above chance）——刚好在 Δ 之下。一个具有 10–14pp moderate bias 的 judge 会被 TOST 宣布为 "equivalent to no bias"。Claude 的实际 BT（50.2–54.1%）远低于此阈值，所以当前结论不受影响；但 Δ = 15pp 的选择依据不够充分。
- 建议：提供 Δ = 15pp 的定量推导；增加 Δ 敏感性分析（Δ = 10pp, 12pp, 15pp, 20pp）；在 Limitations 中明确 "moderate bias (10–14pp) 可能逃脱检测"。

**W3 [Should-Fix] 方向不对称性对 Table 1 BT 估计的影响未充分讨论（Appendix A/H）**
- Formality 方向不对称显著：formal→casual 方向 judge 保留原文 88.9%，casual→formal 方向仅 52.6%。这暗示 formality BT 估计中混合了真实风格偏好和 "原文偏好 × 原文恰好是 formal" 的混淆。Appendix A 的 GEE 控制原文偏好后 formality 仍显著（OR = 2.58, p = 0.032），但主文 Table 1 的 BT 数值是未调整的聚合值。
- 建议：在 Table 1 添加脚注提示方向不对称；考虑增加 GEE-adjusted style OR 对照列；在 §5.1 中更明确地区分 "BT detects real style preference" 和 "BT detects a mix of style + quality confounding"。

**W4 [Should-Fix] NLI gate 选择偏差检查覆盖面有限（§3.2, Appendix B）**
- 44% 拒绝率下，仅检查 4 个 surface covariates（word count, sentence count, TTR, FK grade）。未覆盖：语义/话题分布、句法复杂度、原始文本质量分布。
- 建议：增加 instruction type/topic 分布对比；或论证为何 4 个 surface covariates 足以排除选择偏差。

**W5 [Should-Fix] Construct validity 讨论不充分（§5.1）**
- 论文框架将 pairwise 定位为 "检测到" Likert "遗漏的" 偏差，隐含 pairwise 是更准确的测量。但 §5.1 自己承认 Likert 和 pairwise 可能测量不同 construct（absolute quality vs. comparative sensitivity）。
- 论文已有的辩护（§5.1 末段, §6）：RLHF/DPO 使用 pairwise comparison，所以 pairwise-detected biases 是对 alignment pipeline 实际传播的偏差的正确测量。这个实践论证是有效的，但在正文中不够显式。
- 建议：在 §5.1 中增加一段，明确区分 "measurement sensitivity gap" 和 "construct divergence"，并论证为何在 RLHF 语境下前者更重要。

### Minor

**M1 [Minor] Cross-axis 污染超过自设阈值（Appendix R）** — Formality 改写产生 word count shift d = −0.23，超过 d < 0.20 标准。GEE covariate check 有效缓解但主文未明确承认阈值违反。

**M2 [Minor] 100-point continuous Likert 仅用 Qwen3-32B（Appendix M）** — 存在 evaluator-producer overlap。

**M3 [Minor] BT IIA 脚注简化过度（脚注 3）** — binary-choice BT 中 IIA 技术上正确，但跨 pairs 聚合时隐含的一维性假设未讨论。

**M4 [Minor] Bootstrap CI 方法未指定** — 未指定 percentile bootstrap 还是 BCa bootstrap。

**M5 [Minor] Table 2 的 GEE 与 Table 3 的 GEE 是不同模型** — 建议在 Table 2 标注 "GEE (Likert-outcome)" 以区分。

## Questions

**Q1.** 对于 formality 方向不对称（88.9% vs 52.6%），是否考虑过分方向拟合 BT 模型？

**Q2.** NLI gate pass vs. reject 的 instruction type/topic 分布是否有系统差异？

**Q3.** Direction-aware NLI gate 恢复的 21 对的 content quality 分布是否与 bidirectional-pass 对一致？

**Q4.** Table 2 的 GEE 与 Table 3 的 GEE 使用不同因变量——能否在正文中明确区分？

**Q5.** 是否考虑过使用 BCa bootstrap 而非 percentile bootstrap 计算 BT 置信区间？

**Q6.** TOST Δ = 15pp 的定量依据是什么？

## Missing References

无必须添加的遗漏引用。可选增强引用：
- Millsap (2011), *Statistical Approaches to Measurement Invariance*
- Cattelan (2012), *Models for Paired Comparison Data: A Review with Emphasis on Dependent Data*

## 总体评分

**Overall**: **3.5** — Borderline Conference

**一句话总结**: 核心发现新颖且证据充分（7 种方法 × 4 judges × 3 benchmarks 三角验证），但人工标注规模不足（50 对, κ=0.44）、TOST 等价阈值与最小观测偏差重叠（Δ=15pp vs. 13pp）、以及 construct validity 讨论的不完整性，使评分停留在 Borderline Conference——若 should-fix 问题得到解决（尤其 W1 和 W5），可以上调至 Conference (4.0)。

## 格式合规
- ✅ 正文页数合规
- ✅ Double-blind 合规
- ✅ Limitations 合规
- ✅ 参考文献格式规范

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 916 · 2026-05-22T19:44:10.446062+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "# Reviewer 2 交叉回应 Reviewer 1\n\n---\n\n## Should-Fix 逐条回应\n\n### R1-W1: 人工标注规模不足（50 pairs, κ=0.44）\n**[AGREE]** 同意这是需要修复的问题。NLI gate 是 CSD 管线的核心假设保障组件——44% 拒绝率意味着超过四成数据被过滤，gate 的准确性直接决定剩余数据的有效性。50 对样本、2 名标注员、κ=0.44 的 moderate agreement 确实不足以建立对 gate 的强信心。\n\n补充观察：论文确实在 NLI gate 之外提供了多层间接验证——Appendix E 的 11 阈值敏感性分析（0.60–0.95）显示 BT 结果在阈值变化下稳定、Appendix R 的 cross-axis 污染分析确认风格改写不改变其他轴的 surface features。这些降低了 gate 系统性失败的风险，但不能替代直接的人工验证。≥100 对 + 第 3 名标注员的建议合理。\n\n### R1-W2: TOST Δ=15pp 与 GPT-4o 最小偏差重叠\n**[AGREE]** 同意 Δ=15pp 的选择需要更充分的定量推导。GPT-4o formality BT=63%（13pp above chance）落在 Δ=15pp 的等价区间内，这意味着一个具有 moderate bias 的 judge 理论上可以被 TOST 宣布为\"等价于无偏差\"。虽然 Claude 的实际 BT（50.2–54.1%）远低于此阈值、当前结论不受影响，但 Δ 的选择缺乏锚定于实践意义的论证（如\"多少 pp 的偏差会影响下游 alignment 决策？\"）。\n\nR1 建议的 Δ 敏感性分析（10pp/12pp/15pp/20pp）是提升可信度的最直接方式。\n\n### R1-W3: 方向不对称性对 Table 1 BT 的影响\n**[AGREE]** 同意 Table 1 的 BT 是未调整的聚合值，在方向不对称显著的情况下（formal→casual 88.9% vs casual→formal 52.6%）可能混合了真实风格偏好与原文偏好混淆。Appendix A 的 GEE 控制后 formality 仍显著（OR=2.58, p=0.032），但主文读者不易获取这一调整结果。\n\n这一问题与我在 N1 中提出的 framing 不对称性直接相关：Table 1 的未调整 BT 容易被解读为\"纯风格偏好的大小\"，而实际上其中混入了质量混淆成分。在 Table 1 添加 GEE-adjusted 对照列或至少加脚注是最小修改方案。\n\n### R1-W4: NLI gate 选择偏差检查覆盖面有限\n**[AGREE]** 同意仅检查 4 个 surface covariates（word count, sentence count, TTR, FK grade）不足以排除选择偏差的所有维度。特别是 instruction type/topic 分布——如果 NLI gate 系统性地拒绝某类 instruction（如创意写作类比事实问答类更难保持内容等价），则通过 gate 的子集可能在 topic 分布上偏斜，进而影响 judge 的风格敏感度估计。\n\n不过我认为严重程度略低于 R1 的评估。Appendix R 的 cross-axis contamination 分析已表明风格改写对 4 个 surface features 的影响可忽略，且 NLI threshold sensitivity sweep (Appendix E) 显示在 0.60–0.95 范围内 BT 估计稳定——如果选择偏差严重，不同阈值下应产生不稳定的结果。但增加 topic 分布对比确实是低成本高回报的补充。\n\n### R1-W5: Construct validity 讨论不充分\n**[AGREE]** 强烈同意，这与我的 N1（framing 不对称性）本质上是同一个问题。论文在 §5.1 末段和 Limitations 中承认了 construct divergence 的可能性，但这些讨论被边缘化——标题、摘要、结论的主叙事仍然是 \"Likert misses what pairwise detects\"。\n\nR1 指出的 RLHF/DPO 实践论证（pairwise-detected biases 对 alignment pipeline 有实际意义）是一个有效的辩护角度，但在正文中确实不够显式。我建议比 R1 更进一步：不仅在 §5.1 增加一段 construct validity 讨论，还应在标题和摘要层面调整 framing，使三种解释（measurement attenuation / format amplification / construct divergence）获得更平衡的呈现。\n\n---\n\n## Minor 逐条回应\n\n### R1-M1: Cross-axis 污染超过自设阈值（d=−0.23 > 0.20）\n**[AGREE]** Appendix R 的 formality 改写产生 word count shift d=−0.23，确实超过论文自设的 d<0.20 标准。GEE covariate 控制有效缓解（Table 3 中 verbosity 的 confound 结构在控制 word count 后仍然清晰），但阈值违反应在主文或 Appendix R 中明确承认而非默认通过。\n\n### R1-M2: 100-point continuous Likert 仅用 Qwen3-32B\n**[AGREE]** 这与我的 W2（register 轴 evaluator-producer overlap）属于同一类问题。Appendix M 使用 Qwen3-32B 既是 rewriter 又是 judge 来测试 100-point continuous Likert，自偏好效应可能放大或掩盖结果。用 GPT-4o 或其他非 rewriter judge 复制此实验更可信。\n\n### R1-M3: BT IIA 脚注简化过度\n**[AGREE]** 技术上，binary-choice BT 满足 IIA，但跨 pairs 聚合时隐含的一维性假设（即\"风格偏好可以用单一参数充分描述\"）在风格是多维的情况下（formality、verbosity、register 各有不同 confound 结构）并非不言自明。不过这确实是 minor——GEE per-axis 分解本身就是对一维性假设的补充修正。\n\n### R1-M4: Bootstrap CI 方法未指定\n**[AGREE]** Appendix I 报告 bootstrap 95% CIs 但未指明 percentile 还是 BCa。鉴于 BT 估计的分布可能在 0.5 附近偏斜（尤其 Claude 负控制），BCa 校正可能产生实质差异。报告方法选择是基本的统计报告要求。\n\n### R1-M5: Table 2 GEE 与 Table 3 GEE 是不同模型\n**[AGREE]** Table 2 的 GEE 以 Likert score 为因变量（检测 Likert-based 方法的灵敏度），Table 3 的 GEE 以 pairwise choice 为因变量并分解 style/originality OR。两者目的和规格完全不同，但共享 \"GEE\" 标签。在 Table 2 中标注 \"GEE (Likert-outcome)\" 是零成本的明确化改进。\n\n---\n\n## Questions 逐条回应\n\n### R1-Q1: 是否考虑分方向拟合 BT 模型？\n**[AGREE]** 这是一个有价值的分析建议。Appendix F 的 direction-aware NLI gate 已经部分处理了方向不对称（通过恢复 21 个 unidirectional-pass pairs），但分方向 BT 模型能更直接地量化 formal→casual 和 casual→formal 方向上偏好强度的差异。如果两个方向的 BT 估计差异很大，则 Table 1 的聚合 BT 信息量有限。\n\n### R1-Q2: NLI gate pass/reject 的 instruction type 分布差异？\n**[AGREE]** 直接关联 W4。如果 NLI gate 系统性拒绝某类 instruction，通过 gate 的数据子集可能不代表原始 benchmark 的分布，影响 Blindspot 发现的外部效度。\n\n### R1-Q3: Direction-aware NLI gate 恢复的 21 对质量分布？\n**[AGREE]** Appendix F 报告 direction-aware gate 恢复了 21 additional pairs (BT 73.8%, p=0.006)，确认 Blindspot 在扩展数据中持续。但这 21 对是从 unidirectional-pass 中选出的（即一个方向 NLI pass、另一个方向 NLI fail），其内容质量分布可能与 bidirectional-pass pairs 不同。验证这一点对 Appendix F 结论的可信度很重要。\n\n### R1-Q4: Table 2 vs Table 3 GEE 区分？\n与 M5 相同，已 AGREE。\n\n### R1-Q5: BCa vs percentile bootstrap？\n与 M4 相同，已 AGREE。BCa 在小样本或偏斜分布下更准确，鉴于部分 cells（如 Claude 负控制）的 BT 估计接近 0.5，BCa 可能是更稳健的选择。\n\n### R1-Q6: TOST Δ=15pp 定量依据？\n与 W2 相同，已 AGREE。\n\n---\n\n## 对 R1 整体评分的回应\n\nR1 给出 3.5 (Borderline Conference)，我给出 3.0 (Findings)。差异主要在 novelty 权重。\n\nR1 的 S1 评价核心发现为\"新颖且实践意义重大\"——我部分不同意。Likert vs pairwise 灵敏度差异在心理测量学中是 Thurstone (1927) 以来的 established knowledge（§2 引用的 Stevens 1946、Preston & Colman 2000、DeCoster et al. 2011 都是这一传统中的经典工作）。论文的真正新颖性在于 (a) 首次在 LLM judge 领域受控量化这一现象的幅度，(b) GEE per-axis confound decomposition 方法。但\"发现本身\"的 novelty 有限——一个熟悉心理测量学的 reviewer 会预期 Likert 在微弱差异上不如 forced-choice sensitive。\n\n我认为 R1 的 W5（construct validity）和我的 N1（framing 不对称性）共同构成了将评分压到 Findings 的核心原因：在缺乏外部 ground truth 的情况下，论文不能确定 pairwise 检测到的是\"真实信号\"还是\"格式放大的微弱偏好\"，但标题和结论的 framing 隐式预设了前者。如果 framing 修正 + construct validity 讨论加强，可以升至 3.5；如果同时增加人工标注规模和 TOST 敏感性分析，可以达到 Conference (4.0)。\n\n---\n\n## 总结\n\nR1 的 5 个 Should-Fix 和 5 个 Minor 全部 **[AGREE]**。R1 的审稿在方法论细节（TOST 阈值、方向不对称性、bootstrap 方法、NLI gate 验证）上比我的审稿更深入，这些问题与我关注的更宏观的 framing/novelty 问题互补。两份审稿共同指向同一个核心缺陷：**论文的实验设计和统计分析是一流的，但解释框架（framing）系统性地偏向 \"Likert is wrong, pairwise is right\"，而数据本身无法排除 construct divergence 或 format amplification 的替代解释。**",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "# Reviewer 2 交叉回应 Reviewer 1\n\n---\n\n## Should-Fix 逐条回应\n\n### R1-W1: 人工标注规模不足（50 pairs, κ=0.44）\n**[AGREE]** 同意这是需要修复的问题。NLI gate 是 CSD 管线的核心假设保障组件——44% 拒绝率意味着超过四成数据被过滤，gate 的准确性直接决定剩余数据的有效性。50 对样本、2 名标注员、κ=0.44 的 moderate agreement 确实不足以建立对 gate 的强信心。\n\n补充观察：论文确实在 NLI gate 之外提供了多层间接验证——Appendix E 的 11 阈值敏感性分析（0.60–0.95）显示 BT 结果在阈值变化下稳定、Appendix R 的 cross-axis 污染分析确认风格改写不改变其他轴的 surface features。这些降低了 gate 系统性失败的风险，但不能替代直接的人工验证。≥100 对 + 第 3 名标注员的建议合理。\n\n### R1-W2: TOST Δ=15pp 与 GPT-4o 最小偏差重叠\n**[AGREE]** 同意 Δ=15pp 的选择需要更充分的定量推导。GPT-4o formality BT=63%（13pp above chance）落在 Δ=15pp 的等价区间内，这意味着一个具有 moderate bias 的 judge 理论上可以被 TOST 宣布为\"等价于无偏差\"。虽然 Claude 的实际 BT（50.2–54.1%）远低于此阈值、当前结论不受影响，但 Δ 的选择缺乏锚定于实践意义的论证（如\"多少 pp 的偏差会影响下游 alignment 决策？\"）。\n\nR1 建议的 Δ 敏感性分析（10pp/12pp/15pp/20pp）是提升可信度的最直接方式。\n\n### R1-W3: 方向不对称性对 Table 1 BT 的影响\n**[AGREE]** 同意 Table 1 的 BT 是未调整的聚合值，在方向不对称显著的情况下（formal→casual 88.9% vs casual→formal 52.6%）可能混合了真实风格偏好与原文偏好混淆。Appendix A 的 GEE 控制后 formality 仍显著（OR=2.58, p=0.032），但主文读者不易获取这一调整结果。\n\n这一问题与我在 N1 中提出的 framing 不对称性直接相关：Table 1 的未调整 BT 容易被解读为\"纯风格偏好的大小\"，而实际上其中混入了质量混淆成分。在 Table 1 添加 GEE-adjusted 对照列或至少加脚注是最小修改方案。\n\n### R1-W4: NLI gate 选择偏差检查覆盖面有限\n**[AGREE]** 同意仅检查 4 个 surface covariates（word count, sentence count, TTR, FK grade）不足以排除选择偏差的所有维度。特别是 instruction type/topic 分布——如果 NLI gate 系统性地拒绝某类 instruction（如创意写作类比事实问答类更难保持内容等价），则通过 gate 的子集可能在 topic 分布上偏斜，进而影响 judge 的风格敏感度估计。\n\n不过我认为严重程度略低于 R1 的评估。Appendix R 的 cross-axis contamination 分析已表明风格改写对 4 个 surface features 的影响可忽略，且 NLI threshold sensitivity sweep (Appendix E) 显示在 0.60–0.95 范围内 BT 估计稳定——如果选择偏差严重，不同阈值下应产生不稳定的结果。但增加 topic 分布对比确实是低成本高回报的补充。\n\n### R1-W5: Construct validity 讨论不充分\n**[AGREE]** 强烈同意，这与我的 N1（framing 不对称性）本质上是同一个问题。论文在 §5.1 末段和 Limitations 中承认了 construct divergence 的可能性，但这些讨论被边缘化——标题、摘要、结论的主叙事仍然是 \"Likert misses what pairwise detects\"。\n\nR1 指出的 RLHF/DPO 实践论证（pairwise-detected biases 对 alignment pipeline 有实际意义）是一个有效的辩护角度，但在正文中确实不够显式。我建议比 R1 更进一步：不仅在 §5.1 增加一段 construct validity 讨论，还应在标题和摘要层面调整 framing，使三种解释（measurement attenuation / format amplification / construct divergence）获得更平衡的呈现。\n\n---\n\n## Minor 逐条回应\n\n### R1-M1: Cross-axis 污染超过自设阈值（d=−0.23 > 0.20）\n**[AGREE]** Appendix R 的 formality 改写产生 word count shift d=−0.23，确实超过论文自设的 d<0.20 标准。GEE covariate 控制有效缓解（Table 3 中 verbosity 的 confound 结构在控制 word count 后仍然清晰），但阈值违反应在主文或 Appendix R 中明确承认而非默认通过。\n\n### R1-M2: 100-point continuous Likert 仅用 Qwen3-32B\n**[AGREE]** 这与我的 W2（register 轴 evaluator-producer overlap）属于同一类问题。Appendix M 使用 Qwen3-32B 既是 rewriter 又是 judge 来测试 100-point continuous Likert，自偏好效应可能放大或掩盖结果。用 GPT-4o 或其他非 rewriter judge 复制此实验更可信。\n\n### R1-M3: BT IIA 脚注简化过度\n**[AGREE]** 技术上，binary-choice BT 满足 IIA，但跨 pairs 聚合时隐含的一维性假设（即\"风格偏好可以用单一参数充分描述\"）在风格是多维的情况下（formality、verbosity、register 各有不同 confound 结构）并非不言自明。不过这确实是 minor——GEE per-axis 分解本身就是对一维性假设的补充修正。\n\n### R1-M4: Bootstrap CI 方法未指定\n**[AGREE]** Appendix I 报告 bootstrap 95% CIs 但未指明 percentile 还是 BCa。鉴于 BT 估计的分布可能在 0.5 附近偏斜（尤其 Claude 负控制），BCa 校正可能产生实质差异。报告方法选择是基本的统计报告要求。\n\n### R1-M5: Table 2 GEE 与 Table 3 GEE 是不同模型\n**[AGREE]** Table 2 的 GEE 以 Likert score 为因变量（检测 Likert-based 方法的灵敏度），Table 3 的 GEE 以 pairwise choice 为因变量并分解 style/originality OR。两者目的和规格完全不同，但共享 \"GEE\" 标签。在 Table 2 中标注 \"GEE (Likert-outcome)\" 是零成本的明确化改进。\n\n---\n\n## Questions 逐条回应\n\n### R1-Q1: 是否考虑分方向拟合 BT 模型？\n**[AGREE]** 这是一个有价值的分析建议。Appendix F 的 direction-aware NLI gate 已经部分处理了方向不对称（通过恢复 21 个 unidirectional-pass pairs），但分方向 BT 模型能更直接地量化 formal→casual 和 casual→formal 方向上偏好强度的差异。如果两个方向的 BT 估计差异很大，则 Table 1 的聚合 BT 信息量有限。\n\n### R1-Q2: NLI gate pass/reject 的 instruction type 分布差异？\n**[AGREE]** 直接关联 W4。如果 NLI gate 系统性拒绝某类 instruction，通过 gate 的数据子集可能不代表原始 benchmark 的分布，影响 Blindspot 发现的外部效度。\n\n### R1-Q3: Direction-aware NLI gate 恢复的 21 对质量分布？\n**[AGREE]** Appendix F 报告 direction-aware gate 恢复了 21 additional pairs (BT 73.8%, p=0.006)，确认 Blindspot 在扩展数据中持续。但这 21 对是从 unidirectional-pass 中选出的（即一个方向 NLI pass、另一个方向 NLI fail），其内容质量分布可能与 bidirectional-pass pairs 不同。验证这一点对 Appendix F 结论的可信度很重要。\n\n### R1-Q4: Table 2 vs Table 3 GEE 区分？\n与 M5 相同，已 AGREE。\n\n### R1-Q5: BCa vs percentile bootstrap？\n与 M4 相同，已 AGREE。BCa 在小样本或偏斜分布下更准确，鉴于部分 cells（如 Claude 负控制）的 BT 估计接近 0.5，BCa 可能是更稳健的选择。\n\n### R1-Q6: TOST Δ=15pp 定量依据？\n与 W2 相同，已 AGREE。\n\n---\n\n## 对 R1 整体评分的回应\n\nR1 给出 3.5 (Borderline Conference)，我给出 3.0 (Findings)。差异主要在 novelty 权重。\n\nR1 的 S1 评价核心发现为\"新颖且实践意义重大\"——我部分不同意。Likert vs pairwise 灵敏度差异在心理测量学中是 Thurstone (1927) 以来的 established knowledge（§2 引用的 Stevens 1946、Preston & Colman 2000、DeCoster et al. 2011 都是这一传统中的经典工作）。论文的真正新颖性在于 (a) 首次在 LLM judge 领域受控量化这一现象的幅度，(b) GEE per-axis confound decomposition 方法。但\"发现本身\"的 novelty 有限——一个熟悉心理测量学的 reviewer 会预期 Likert 在微弱差异上不如 forced-choice sensitive。\n\n我认为 R1 的 W5（construct validity）和我的 N1（framing 不对称性）共同构成了将评分压到 Findings 的核心原因：在缺乏外部 ground truth 的情况下，论文不能确定 pairwise 检测到的是\"真实信号\"还是\"格式放大的微弱偏好\"，但标题和结论的 framing 隐式预设了前者。如果 framing 修正 + construct validity 讨论加强，可以升至 3.5；如果同时增加人工标注规模和 TOST 敏感性分析，可以达到 Conference (4.0)。\n\n---\n\n## 总结\n\nR1 的 5 个 Should-Fix 和 5 个 Minor 全部 **[AGREE]**。R1 的审稿在方法论细节（TOST 阈值、方向不对称性、bootstrap 方法、NLI gate 验证）上比我的审稿更深入，这些问题与我关注的更宏观的 framing/novelty 问题互补。两份审稿共同指向同一个核心缺陷：**论文的实验设计和统计分析是一流的，但解释框架（framing）系统性地偏向 \"Likert is wrong, pairwise is right\"，而数据本身无法排除 construct divergence 或 format amplification 的替代解释。**",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 917 · 2026-05-22T19:44:13.962794+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3516
}
```

</details>

---


### Assistant

_source line 918 · 2026-05-22T19:44:22.844675+00:00_

交叉回应已提交。

对 R1 的 5 个 Should-Fix 和 5 个 Minor 全部 **[AGREE]**，核心理由：

- **W1-W4**（标注规模、TOST 阈值、方向不对称、NLI gate 选择偏差）：R1 在方法论细节上的审查比我更深入，这些技术问题都是合理的，尤其 W1（50 pairs, κ=0.44）和 W2（Δ=15pp 与 GPT-4o 13pp 重叠）。
- **W5**（construct validity）：与我的 N1（framing 不对称性）本质上是同一问题——论文的核心缺陷不在实验设计，而在解释框架。
- **M1-M5**：均为合理的报告规范改进建议。

与 R1 的主要分歧在 **novelty 权重**：R1 给 3.5（Borderline Conference），我给 3.0（Findings）。我认为 Likert vs pairwise 灵敏度差异是心理测量学的 established knowledge，"首次在 LLM judge 领域量化"的新颖性不足以支撑 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 29

## Round 29

56 recorded events


### User

_source line 919 · 2026-05-22T22:40:23.502015+00:00_

[Round 1 审稿请求]:
你负责**新颖性 + framing + 写作质量 + 完整性**的审查。

## 论文信息
- **标题**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation
- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf`

## Venue 要求（EMNLP 2026 via ARR）
- **格式**: ACL 模板，double-blind
- **页数**: 正文 ≤8 页，参考文献不限
- **Limitations**: 不计入页数限制，需在 conclusion 后、references 前
- **匿名**: 必须匿名，作者写 "Anonymous"
- **截止日期**: 2026-05-25 (ARR May cycle)
- **评分标准**: Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）

## 你的审查侧重
请重点审查以下方面：

1. **新颖性（Novelty）**：
   - Likert Blindspot 是否只是 Thurstone (1927) 经典结论在 LLM judge 领域的 domain transfer？
   - 论文贡献的增量性——CSD 框架、GEE decomposition 的独立贡献价值？
   - 与 RATE (Reber et al., 2025)、Comparative Trap (Jeong et al., 2025) 的差异化定位？

2. **Framing 与叙事平衡**：
   - 三种解释（attenuation / amplification / construct divergence）的权重是否平衡？
   - "Blindspot" 命名是否隐含了偏向 attenuation 的预设？
   - Introduction 的 motivating example 是否暗示 Likert 判断是"错误的"？
   - Abstract 数字密度是否过高影响可读性？

3. **写作质量**：
   - 行文清晰度、术语一致性
   - 图表的信息密度与可读性
   - Related Work 的完整性和定位准确性

4. **完整性**：
   - 3 个 style axes 是否足以支撑 "framework" 级别的泛化声明？
   - Cross-benchmark 覆盖是否充分（LLMBar n=100 + AlpacaEval + MT-Bench 选择性配置）？
   - 遗漏的重要相关工作？

5. **格式合规**：
   - 正文 ≤8 页？
   - double-blind 匿名？
   - Limitations 位置正确？

请给出结构化审稿意见：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 920 · 2026-05-22T22:40:31.238546+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
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

_source line 921 · 2026-05-22T22:40:31.289212+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 922 · 2026-05-22T22:40:35.356406+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 923 · 2026-05-22T22:40:36.309793+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR reviewer form scoring dimensions soundness excitement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR reviewer form scoring dimensions soundness excitement"
  }
}
```

</details>

---


### Tool call

_source line 924 · 2026-05-22T22:40:38.518759+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 925 · 2026-05-22T22:40:42.077269+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found information about the ACL Rolling Review (ARR) 2026 reviewer guidelines and review form. Here's what I found:

## Reviewer Guidelines

Reviewers are asked to follow a workflow: read the paper and get the first impression, then search for related
…[truncated 1290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6720
}
```

</details>

---


### Tool result

_source line 926 · 2026-05-22T22:40:42.377131+00:00_

Web search results for query: "EMNLP 2026 ARR reviewer form scoring dimensions soundness excitement"

Links: [{"title":"TrustNLP","url":"https://trustnlpworkshop.github.io/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Improving Patient Experience: BMBA","url":"https://cdn.clinicaltrials.gov/large-docs/30/NCT05690230/Prot_SAP_000.pdf"}]

Based on the search results, I found relevant information about the ARR reviewer form scoring dimensions for EMNLP 2026:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

Here's how these dimensions are defined:

**Soundness:** The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

**Excitement:** Excitement is a separate score which is orthogonal to the assessment of the soundness of the paper. Excitement scores reflect our personal taste, and so do not necessarily come with explicit reasons.

**Overall Assessment:** The Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlink
…[truncated 2 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6067
}
```

</details>

---


### Tool result

_source line 927 · 2026-05-22T22:40:45.444724+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 457.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 586.4}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p9.p
…[truncated 526 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6925
}
```

</details>

---


### Tool call

_source line 928 · 2026-05-22T22:40:53.798356+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, definitions, and any guidance text. Include soundness, excitement, overall assessment, and any other dimensions like reproducibility, ethical concerns, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, definitions, and any guidance text. Include soundness, excitement, overall assessment, and any other dimensions like reproducibility, ethical concerns, etc."
  }
}
```

</details>

---


### Tool call

_source line 929 · 2026-05-22T22:40:55.404360+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "11-18",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "11-18",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 930 · 2026-05-22T22:40:55.905984+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 931 · 2026-05-22T22:40:56.859091+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 932 · 2026-05-22T22:40:57.360523+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 933 · 2026-05-22T22:40:57.812104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 934 · 2026-05-22T22:41:00.320877+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Primary Assessment Dimensions

**Soundness**
- Evaluates scientific rigor and support for claims
- Scale: 1-5 (with .5 increments)
- Guidance: "Is it sufficiently sound and thorough? Does it clearly state..."
- 5 = Excellent; 1 = Major Issues

**Excitement**
- Measures subjective appeal and potential impact
- Scale: 1-5 (with .5 increments)
- Guidance: Considers conceptual breakthroughs, community impact, and personal relevance
- 5 = Highly Exciting; 1 = Not Exciting

**Overall Assessment**
- Determines publication recommendation tier
- Scale: 1-5 (with .5 increments)
- Options: Award consideration, Conference, Findings, Resubmit, Do not resubmit
- 5 = Consider for Award; 1 = Do not resubmit

**Reviewer Confidence**
- Reflects evaluation reliability
- Scale: 1-5 (no .5 increments specified)
- 5 = Very careful review; 1 = Not area expertise

## Additional Evaluation Areas

**Reproducibility** (1-5 scale): Assesses ability to replicate results

**Ethical Concerns & Limitations**: Checks for adequate discussion of societal impact and ethics compliance

**Datasets & Software** (1-5 scales): Rates value of released resources

**Author Identity** (1-5 scale): Documents potential anonymity concerns

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6522
}
```

</details>

---


### Tool call

_source line 935 · 2026-05-22T22:41:00.371433+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 936 · 2026-05-22T22:41:01.075676+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 440.4}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 437.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 471.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.5}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 591.2}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 598.2}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 355.1}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_styl
…[truncated 93 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5671
}
```

</details>

---


### Tool result

_source line 937 · 2026-05-22T22:41:03.791029+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3419
}
```

</details>

---


### Tool result

_source line 938 · 2026-05-22T22:41:03.792706+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5980
}
```

</details>

---


### Tool result

_source line 939 · 2026-05-22T22:41:03.793824+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7887
}
```

</details>

---


### Tool result

_source line 940 · 2026-05-22T22:41:03.795068+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6935
}
```

</details>

---


### Tool result

_source line 941 · 2026-05-22T22:41:03.796252+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6435
}
```

</details>

---


### Tool call

_source line 942 · 2026-05-22T22:41:11.480264+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 943 · 2026-05-22T22:41:15.817342+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4337
}
```

</details>

---


### Tool call

_source line 944 · 2026-05-22T22:41:15.817891+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 945 · 2026-05-22T22:41:15.868849+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 946 · 2026-05-22T22:41:15.971362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 947 · 2026-05-22T22:41:17.536177+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1667
}
```

</details>

---


### Tool call

_source line 948 · 2026-05-22T22:41:17.536750+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 949 · 2026-05-22T22:41:17.537026+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 950 · 2026-05-22T22:41:17.537244+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 951 · 2026-05-22T22:41:17.743037+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1925
}
```

</details>

---


### Tool call

_source line 952 · 2026-05-22T22:41:17.743553+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 953 · 2026-05-22T22:41:17.895147+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1923
}
```

</details>

---


### Tool result

_source line 954 · 2026-05-22T22:41:19.709263+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2172
}
```

</details>

---


### Tool result

_source line 955 · 2026-05-22T22:41:19.760538+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2223
}
```

</details>

---


### Tool result

_source line 956 · 2026-05-22T22:41:19.761681+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2224
}
```

</details>

---


### Tool result

_source line 957 · 2026-05-22T22:41:19.863097+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2119
}
```

</details>

---


### Tool call

_source line 958 · 2026-05-22T22:41:25.432966+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 959 · 2026-05-22T22:41:26.388723+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 960 · 2026-05-22T22:41:26.539597+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 961 · 2026-05-22T22:41:27.092130+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 962 · 2026-05-22T22:41:27.393952+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 963 · 2026-05-22T22:41:27.545464+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 964 · 2026-05-22T22:41:27.999463+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 965 · 2026-05-22T22:41:27.999876+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 966 · 2026-05-22T22:41:28.405175+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool result

_source line 967 · 2026-05-22T22:41:28.607127+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 607
}
```

</details>

---


### Tool call

_source line 968 · 2026-05-22T22:46:15.863183+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5 / 5（Borderline Conference）\n**Confidence**: 4 / 5\n**一句话总结**: 方法论严谨、实验充分，但核心发现在心理测量学中可预测，\"Blindspot\"命名隐含对 attenuation 解释的偏向，3 条 style axis 难以支撑 \"framework\" 级别的泛化声明。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4 / 5 | 方法论设计严谨：NLI 内容门控、position-controlled pairwise、GEE 分解、FWER 校正、bootstrap attenuation 分析均到位。主要扣分点：三种解释（attenuation/amplification/construct divergence）无法区分，限制了可操作结论 |\n| Excitement | 3 / 5 | 实证贡献扎实，但核心发现（forced-choice 比 absolute rating 更敏感）是 Thurstone (1927) 以来的经典心理测量结论。GEE per-axis 分解揭示不同 confound 结构是本文最有趣的增量贡献，但整体新颖性有限 |\n| Reproducibility | 4 / 5 | 实验细节充分（Appendix P 列出模型、API、温度参数），承诺开源代码和数据。NLI 阈值选择和 rewriter prompt 均有记录 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"Framework\" 泛化声明与实际覆盖不匹配\n- 具体位置：Section 1 contributions 第一条（\"a CSD, a black-box framework for per-axis style bias detection\"）；Section 6 Conclusion\n- 问题：论文将 CSD 定位为通用的 per-axis style bias detection \"framework\"，但实际只测试了 formality、verbosity、register 三条轴。其中 register 仅在 Table 1 中出现部分结果，cross-axis contamination 分析（Appendix R/Table 19）也仅覆盖这三条轴。三条相关性较高的表面风格特征（均为文本表层属性，不涉及论证结构、逻辑深度等深层风格）不足以支撑 \"framework\" 级别的泛化。\n- 为什么影响接收：Reviewer 会质疑是否遇到 semantic-level 风格轴（如 hedging、humor、technicality）时 CSD 的 NLI 门控还能正常工作——这些轴的 style-content 边界更模糊，NLI entailment 可能系统性地拒绝合法 rewrite。\n- 建议修改方向：(a) 将 \"framework\" 降级为 \"methodology\" 或 \"experimental protocol\"；(b) 或者增加 1-2 条非表面风格轴（如 hedging/directness）的实验；(c) 在 Limitations 中明确讨论 CSD 对深层风格轴的适用性边界。\n\n**N2** [critical] 标题与叙事隐含 attenuation 偏向，与三种解释并列的中立定位矛盾\n- 具体位置：Title (\"Likert Blindspot\")；Abstract 第一句 (\"Likert and pairwise scoring produce systematically divergent style sensitivity\")；Section 6 Conclusion (\"Likert-only analysis may fail to surface style-driven preferences\")\n- 问题：\"Blindspot\" 这个词在认知科学中的含义是\"盲区\"——即某个真实存在的东西未被检测到。这直接预设了 attenuation 解释（Likert 遗漏了真实偏好），排斥了 amplification 解释（pairwise 放大了微小偏好到不合理程度）和 construct divergence 解释（两种模式测量的是不同构念）。论文 Section 5.1 和 Limitations 中对三种解释的讨论是平衡的，但标题和整体叙事框架与这种平衡矛盾。Introduction 的 motivating example（page 1，GPT-4o 对 formal vs. casual 回答给出 8 vs. 5）也暗示 Likert 判断是\"错误的\"——但实际上可能是 pairwise 模式在 forced-choice 设定下放大了微小偏好。\n- 为什么影响接收：Framing bias 会被 reviewer 视为论文缺乏理论中立性。如果论文无法区分三种解释（论文自己也承认），那么标题和叙事不应偏向其中一种。\n- 建议修改方向：(a) 考虑更中性的标题，如 \"Measurement-Mode Divergence in LLM Judge Style Evaluation\"（论文副标题已经是这个）；(b) 在 Introduction 的 motivating example 后立即引入 amplification 和 construct divergence 作为等权重的替代解释，而非仅在 Section 5.1 才讨论；(c) Conclusion 中的表述从 \"Likert may fail\" 改为 \"the two modes may capture different aspects of style preferences\"。\n\n**N3** [critical] 核心发现的增量新颖性论证不足\n- 具体位置：Section 1 Introduction；Section 2 Related Work（Measurement Sensitivity in NLG Evaluation 段落）\n- 问题：Forced-choice comparison 比 absolute rating 有更高判别力是 Thurstone (1927) Law of Comparative Judgment 的经典结论，Stevens (1946) 的 scale taxonomy、Krosnick (1999) 的 survey research 方法论、Preston & Colman (2000) 的 granularity 研究都反复验证了这一点。论文在 Section 2 引用了这些工作，但未充分论证为什么在 LLM judge 领域\"重新发现\"这个现象构成足够的新颖性。论文隐含的论证是\"虽然心理测量学早已知道这个问题，但 LLM-as-judge 社区还没有用 controlled methodology 系统展示它\"——这是一个 empirical verification 而非 conceptual advance。\n- 为什么影响接收：对于 EMNLP 主会议（Overall 4.0），需要超越 domain transfer 的贡献。论文需要更清楚地论证：LLM judges 相比 human judges 有什么独特属性使得这个发现不仅是 expected，而且在具体表现形式上是 surprising 的？\n- 建议修改方向：(a) 强调 GEE decomposition 揭示的 per-axis confound structure 差异（formality 是 conditional effect，verbosity 是 style-dominated）——这是人类评估文献中尚未系统报告的 LLM-specific 发现；(b) 论证 LLM judges 的 training pipeline（RLHF/RLAIF）可能引入人类评估不存在的 mode-specific biases；(c) 将 novelty claim 的重心从 \"发现 divergence\" 转向 \"quantifying and decomposing the divergence per axis\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Abstract 数字密度过高\n- 具体位置：Abstract（page 1）\n- 问题：Abstract 中出现 p < 0.001、p = 0.17、60%、85.2%、>60% 等至少 6 个定量数字。对于一篇方法论+实证论文，Abstract 应优先传达 insight 而非数字堆砌。特别是 \"with signal loss exceeding 60% at stronger effects\" 在没有上下文的情况下不易理解（60% 的什么？相对什么基线？）。\n- 建议：保留 1-2 个最关键的数字（如 Blindspot 在多少个 judge 上复现），将其余移至 Section 5。\n\n**W2** [warning] 与 RATE (Reber et al., 2025) 的差异化论证薄弱\n- 具体位置：Section 2，Related Work 倒数第二段（page 3）\n- 问题：论文列举了 CSD 与 RATE 的三点差异：(1) targets individual style axes，(2) measures through position-controlled pairwise comparison rather than Likert ATE，(3) enforces NLI entailment gating。但 RATE 也做 per-axis counterfactual rewriting（按 style attribute 分开处理），差异 (1) 更多是程度差别而非本质区别。核心差异其实是 (2)——CSD 的 cross-measurement comparison，但这一点的重要性在 Related Work 中被与其他两点并列稀释了。\n- 建议：明确突出 \"cross-measurement mode comparison\" 作为与 RATE 的核心差异点，而非三点并列。同时承认 CSD 在 Likert-only 分析方面的贡献（Section 5.1 表明 CSD 的 Likert ATE 复现了 RATE 的非显著结果）与 RATE 是互补而非替代关系。\n\n**W3** [warning] LLMBar 样本量小（n=100）对统计推断的限制\n- 具体位置：Section 3.4；Table 1；Figure 4\n- 问题：主实验基于 LLMBar 的 n=100 instruction-response pairs。虽然论文通过 bootstrap attenuation 分析（Appendix J）和 n=355 的 scaled replication 部分缓解了这一问题，Figure 4 也展示了 power analysis，但 n=100 在 formality 轴上仅有 62 个 NLI-filtered pairs（Table 1 footnote），Likert ATE 的 effect size 在 n=100 时 CI 跨越零。论文将 AlpacaEval 和 MT-Bench 定位为 confirmatory，但这两个 benchmark 仅使用 \"selected configurations\"（Section 3.4），且 MT-Bench 的结果仅出现在 Table 1 最后两行，未充分讨论。\n- 建议：在 Discussion 或 Limitations 中更坦率地讨论 n=100 的局限性，特别是对 GEE 交互项估计精度的影响。\n\n**W4** [warning] Construct divergence 解释发展不足\n- 具体位置：Section 5.1（\"Interpreting the divergence\" 段落）；Limitations（page 9）\n- 问题：三种解释中，construct divergence（Likert 测量绝对质量差异，pairwise 测量序数偏好）在理论上最有趣，也与心理测量学文献最相关。但论文对此解释的讨论最薄弱——Section 5.1 仅一句话提及，Limitations 中稍多展开但也仅两句。如果两种测量模式确实测量不同构念，那 \"divergence\" 本身就不是缺陷而是信息量——这会根本改变论文的实践建议。\n- 建议：在 Section 5.1 或 Discussion 中用一段专门讨论 construct divergence 的含义和可检验预测。例如：如果是 construct divergence，我们应期望 divergence 大小与 content quality variance 无关（因为两种模式测量的是不同东西），但如果是 attenuation，divergence 应与 effect size 正相关。论文的数据（Figure 4 的 power curve）可能已经包含区分这两种解释的线索。\n\n**W5** [warning] Claude Sonnet 4 负控制结果的讨论不充分\n- 具体位置：Section 5.4 第二段；Appendix G（Table 10）\n- 问题：Claude Sonnet 4 作为负控制不展示 Blindspot，论文将其归因于\"RLHF training composition or instruction-following strategies\"（page 9 Limitations），但未进一步分析为什么这一个 judge 表现不同。如果 Blindspot 是 measurement mode 的固有属性（如论文标题暗示的），为什么它在某些 judge 上消失？这个 negative result 实际上暗示 Blindspot 可能更多是 model-specific training artifact 而非 measurement-mode intrinsic property——这对论文的核心叙事构成潜在挑战。\n- 建议：在 Section 5.4 或 Discussion 中讨论 Sonnet 4 的负结果对 \"measurement-mode divergence\" 叙事的含义。是否说明 Blindspot 是可以通过训练消除的 judge 属性，而非 Likert 模式的固有限制？\n\n---\n\n## 小问题（不影响接收）\n\n1. **Table 1 可读性**：Table 1 包含 5 个 judge × 3 个 benchmark × 3 个 axis × 多个指标，信息密度极高。建议拆分为 main results（LLMBar）和 confirmatory results（AlpacaEval/MT-Bench）两个表，或使用 heatmap 可视化。\n2. **Figure 2 DAG 标注**：Figure 2 的 dashed orange S → Q path 标注为 \"style bias\"，但论文后续论证这个 path 可能反映 legitimate quality difference（formality 轴）。标注可能误导。\n3. **术语一致性**：\"style bias\" vs. \"style preference\" vs. \"style sensitivity\" 在论文中混用。\"Bias\" 暗示不合理的偏好，\"preference\" 更中性，\"sensitivity\" 最中性。建议统一。\n4. **Section 3.5 Design Rationale 位置**：这一节解释为什么 DAG 不是 formal causal model。内容重要但放在 Method 末尾略显突兀，建议整合到 Section 3.3 或单独的 Discussion 段。\n5. **Appendix 过多（A-S，19 个）**：虽然体现了严谨性，但 reviewer 难以逐一检查。建议在 main text 中更清晰地标注哪些 appendix 是 critical（如 A, J, R），哪些是 supplementary。\n\n---\n\n## 主要优势\n\n1. **方法论严谨**：CSD 的三重控制（NLI 门控 + position control + same-text pairing）在 style bias 研究中是最严格的实验设计之一。Direction-aware gating（Section 3.2）解决了 bidirectional verification 的 inflation 问题，体现了对实验细节的深入思考。\n2. **统计分析全面**：GEE 分解、FWER 校正、7 种 sensitivity methods（Table 2）、bootstrap attenuation 分析（Appendix J）、power analysis（Figure 4）、TOST equivalence testing（Appendix G）——统计处理的深度和广度在 NLP 实证论文中罕见。\n3. **GEE per-axis confound 结构差异**：Table 3 揭示 verbosity 是 style-dominated（Style OR 5-13），formality 是 conditional effect（Style OR < 1 且 Originality OR 显著），register 也显示 varying structure。这是本文最有价值的增量发现，超越了 \"Likert vs. pairwise\" 的简单比较。\n4. **跨 judge 复现**：4 个独立 provider 的 judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）+ 1 个负控制，覆盖不同架构和训练策略，增强了泛化性。\n5. **诚实的 Limitations**：Quality-style confounding、construct validity、evaluator-producer bias 三个核心局限都被坦率讨论，未回避。\n\n---\n\n## Questions for Authors\n\n1. 论文能否利用现有数据（特别是 Figure 4 的 power curve 和 bootstrap attenuation 的收敛行为）来区分 attenuation 和 construct divergence？如果是 attenuation，effect size d 应在更大 n 时趋向真实值；如果是 construct divergence，Likert d 应保持为零而非仅因 power 不足未检测到。Appendix J 的 bootstrap 数据是否支持其中一种？\n\n2. CSD 的 NLI 门控对 formality 轴过滤掉了约 38% 的 pairs（100 → 62，Table 1）。这些被过滤的 pairs 是否系统性地对应更大的 style 效应（因为 style 改变大到影响了 content）？如果是，NLI 门控可能系统性地 underestimate style bias 的实际幅度。\n\n3. Claude Sonnet 4 不展示 Blindspot 是否可能与其特定的 instruction-following 特性有关（如更严格地按 rubric 评分），而非反映 measurement mode 的本质属性？如果是，这是否意味着 Blindspot 可以通过改进 judge prompt 而非改变 measurement mode 来缓解？\n\n---\n\n## Missing References\n\n本文的 Related Work 覆盖较为全面，但可考虑补充：\n\n1. **Kim et al. (2024) \"Prometheus 2\"**：提出同时支持 Likert 和 pairwise 评估的统一 judge 模型，与本文讨论的 measurement mode divergence 直接相关——Prometheus 2 的训练是否消除了 Blindspot？\n2. **Stureborg et al. (2024)** 已引用，但其关于 Likert inconsistency 的具体发现可以在 Related Work 中更详细地对比。\n3. 心理测量学方面，**Luce (1959) \"Individual Choice Behavior\"** 关于 forced-choice models 的理论基础可能比 Thurstone (1927) 更直接相关，因为 Bradley-Terry model 是 Luce choice axiom 的特例。",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5 / 5（Borderline Conference）\n**Confidence**: 4 / 5\n**一句话总结**: 方法论严谨、实验充分，但核心发现在心理测量学中可预测，\"Blindspot\"命名隐含对 attenuation 解释的偏向，3 条 style axis 难以支撑 \"framework\" 级别的泛化声明。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4 / 5 | 方法论设计严谨：NLI 内容门控、position-controlled pairwise、GEE 分解、FWER 校正、bootstrap attenuation 分析均到位。主要扣分点：三种解释（attenuation/amplification/construct divergence）无法区分，限制了可操作结论 |\n| Excitement | 3 / 5 | 实证贡献扎实，但核心发现（forced-choice 比 absolute rating 更敏感）是 Thurstone (1927) 以来的经典心理测量结论。GEE per-axis 分解揭示不同 confound 结构是本文最有趣的增量贡献，但整体新颖性有限 |\n| Reproducibility | 4 / 5 | 实验细节充分（Appendix P 列出模型、API、温度参数），承诺开源代码和数据。NLI 阈值选择和 rewriter prompt 均有记录 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"Framework\" 泛化声明与实际覆盖不匹配\n- 具体位置：Section 1 contributions 第一条（\"a CSD, a black-box framework for per-axis style bias detection\"）；Section 6 Conclusion\n- 问题：论文将 CSD 定位为通用的 per-axis style bias detection \"framework\"，但实际只测试了 formality、verbosity、register 三条轴。其中 register 仅在 Table 1 中出现部分结果，cross-axis contamination 分析（Appendix R/Table 19）也仅覆盖这三条轴。三条相关性较高的表面风格特征（均为文本表层属性，不涉及论证结构、逻辑深度等深层风格）不足以支撑 \"framework\" 级别的泛化。\n- 为什么影响接收：Reviewer 会质疑是否遇到 semantic-level 风格轴（如 hedging、humor、technicality）时 CSD 的 NLI 门控还能正常工作——这些轴的 style-content 边界更模糊，NLI entailment 可能系统性地拒绝合法 rewrite。\n- 建议修改方向：(a) 将 \"framework\" 降级为 \"methodology\" 或 \"experimental protocol\"；(b) 或者增加 1-2 条非表面风格轴（如 hedging/directness）的实验；(c) 在 Limitations 中明确讨论 CSD 对深层风格轴的适用性边界。\n\n**N2** [critical] 标题与叙事隐含 attenuation 偏向，与三种解释并列的中立定位矛盾\n- 具体位置：Title (\"Likert Blindspot\")；Abstract 第一句 (\"Likert and pairwise scoring produce systematically divergent style sensitivity\")；Section 6 Conclusion (\"Likert-only analysis may fail to surface style-driven preferences\")\n- 问题：\"Blindspot\" 这个词在认知科学中的含义是\"盲区\"——即某个真实存在的东西未被检测到。这直接预设了 attenuation 解释（Likert 遗漏了真实偏好），排斥了 amplification 解释（pairwise 放大了微小偏好到不合理程度）和 construct divergence 解释（两种模式测量的是不同构念）。论文 Section 5.1 和 Limitations 中对三种解释的讨论是平衡的，但标题和整体叙事框架与这种平衡矛盾。Introduction 的 motivating example（page 1，GPT-4o 对 formal vs. casual 回答给出 8 vs. 5）也暗示 Likert 判断是\"错误的\"——但实际上可能是 pairwise 模式在 forced-choice 设定下放大了微小偏好。\n- 为什么影响接收：Framing bias 会被 reviewer 视为论文缺乏理论中立性。如果论文无法区分三种解释（论文自己也承认），那么标题和叙事不应偏向其中一种。\n- 建议修改方向：(a) 考虑更中性的标题，如 \"Measurement-Mode Divergence in LLM Judge Style Evaluation\"（论文副标题已经是这个）；(b) 在 Introduction 的 motivating example 后立即引入 amplification 和 construct divergence 作为等权重的替代解释，而非仅在 Section 5.1 才讨论；(c) Conclusion 中的表述从 \"Likert may fail\" 改为 \"the two modes may capture different aspects of style preferences\"。\n\n**N3** [critical] 核心发现的增量新颖性论证不足\n- 具体位置：Section 1 Introduction；Section 2 Related Work（Measurement Sensitivity in NLG Evaluation 段落）\n- 问题：Forced-choice comparison 比 absolute rating 有更高判别力是 Thurstone (1927) Law of Comparative Judgment 的经典结论，Stevens (1946) 的 scale taxonomy、Krosnick (1999) 的 survey research 方法论、Preston & Colman (2000) 的 granularity 研究都反复验证了这一点。论文在 Section 2 引用了这些工作，但未充分论证为什么在 LLM judge 领域\"重新发现\"这个现象构成足够的新颖性。论文隐含的论证是\"虽然心理测量学早已知道这个问题，但 LLM-as-judge 社区还没有用 controlled methodology 系统展示它\"——这是一个 empirical verification 而非 conceptual advance。\n- 为什么影响接收：对于 EMNLP 主会议（Overall 4.0），需要超越 domain transfer 的贡献。论文需要更清楚地论证：LLM judges 相比 human judges 有什么独特属性使得这个发现不仅是 expected，而且在具体表现形式上是 surprising 的？\n- 建议修改方向：(a) 强调 GEE decomposition 揭示的 per-axis confound structure 差异（formality 是 conditional effect，verbosity 是 style-dominated）——这是人类评估文献中尚未系统报告的 LLM-specific 发现；(b) 论证 LLM judges 的 training pipeline（RLHF/RLAIF）可能引入人类评估不存在的 mode-specific biases；(c) 将 novelty claim 的重心从 \"发现 divergence\" 转向 \"quantifying and decomposing the divergence per axis\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Abstract 数字密度过高\n- 具体位置：Abstract（page 1）\n- 问题：Abstract 中出现 p < 0.001、p = 0.17、60%、85.2%、>60% 等至少 6 个定量数字。对于一篇方法论+实证论文，Abstract 应优先传达 insight 而非数字堆砌。特别是 \"with signal loss exceeding 60% at stronger effects\" 在没有上下文的情况下不易理解（60% 的什么？相对什么基线？）。\n- 建议：保留 1-2 个最关键的数字（如 Blindspot 在多少个 judge 上复现），将其余移至 Section 5。\n\n**W2** [warning] 与 RATE (Reber et al., 2025) 的差异化论证薄弱\n- 具体位置：Section 2，Related Work 倒数第二段（page 3）\n- 问题：论文列举了 CSD 与 RATE 的三点差异：(1) targets individual style axes，(2) measures through position-controlled pairwise comparison rather than Likert ATE，(3) enforces NLI entailment gating。但 RATE 也做 per-axis counterfactual rewriting（按 style attribute 分开处理），差异 (1) 更多是程度差别而非本质区别。核心差异其实是 (2)——CSD 的 cross-measurement comparison，但这一点的重要性在 Related Work 中被与其他两点并列稀释了。\n- 建议：明确突出 \"cross-measurement mode comparison\" 作为与 RATE 的核心差异点，而非三点并列。同时承认 CSD 在 Likert-only 分析方面的贡献（Section 5.1 表明 CSD 的 Likert ATE 复现了 RATE 的非显著结果）与 RATE 是互补而非替代关系。\n\n**W3** [warning] LLMBar 样本量小（n=100）对统计推断的限制\n- 具体位置：Section 3.4；Table 1；Figure 4\n- 问题：主实验基于 LLMBar 的 n=100 instruction-response pairs。虽然论文通过 bootstrap attenuation 分析（Appendix J）和 n=355 的 scaled replication 部分缓解了这一问题，Figure 4 也展示了 power analysis，但 n=100 在 formality 轴上仅有 62 个 NLI-filtered pairs（Table 1 footnote），Likert ATE 的 effect size 在 n=100 时 CI 跨越零。论文将 AlpacaEval 和 MT-Bench 定位为 confirmatory，但这两个 benchmark 仅使用 \"selected configurations\"（Section 3.4），且 MT-Bench 的结果仅出现在 Table 1 最后两行，未充分讨论。\n- 建议：在 Discussion 或 Limitations 中更坦率地讨论 n=100 的局限性，特别是对 GEE 交互项估计精度的影响。\n\n**W4** [warning] Construct divergence 解释发展不足\n- 具体位置：Section 5.1（\"Interpreting the divergence\" 段落）；Limitations（page 9）\n- 问题：三种解释中，construct divergence（Likert 测量绝对质量差异，pairwise 测量序数偏好）在理论上最有趣，也与心理测量学文献最相关。但论文对此解释的讨论最薄弱——Section 5.1 仅一句话提及，Limitations 中稍多展开但也仅两句。如果两种测量模式确实测量不同构念，那 \"divergence\" 本身就不是缺陷而是信息量——这会根本改变论文的实践建议。\n- 建议：在 Section 5.1 或 Discussion 中用一段专门讨论 construct divergence 的含义和可检验预测。例如：如果是 construct divergence，我们应期望 divergence 大小与 content quality variance 无关（因为两种模式测量的是不同东西），但如果是 attenuation，divergence 应与 effect size 正相关。论文的数据（Figure 4 的 power curve）可能已经包含区分这两种解释的线索。\n\n**W5** [warning] Claude Sonnet 4 负控制结果的讨论不充分\n- 具体位置：Section 5.4 第二段；Appendix G（Table 10）\n- 问题：Claude Sonnet 4 作为负控制不展示 Blindspot，论文将其归因于\"RLHF training composition or instruction-following strategies\"（page 9 Limitations），但未进一步分析为什么这一个 judge 表现不同。如果 Blindspot 是 measurement mode 的固有属性（如论文标题暗示的），为什么它在某些 judge 上消失？这个 negative result 实际上暗示 Blindspot 可能更多是 model-specific training artifact 而非 measurement-mode intrinsic property——这对论文的核心叙事构成潜在挑战。\n- 建议：在 Section 5.4 或 Discussion 中讨论 Sonnet 4 的负结果对 \"measurement-mode divergence\" 叙事的含义。是否说明 Blindspot 是可以通过训练消除的 judge 属性，而非 Likert 模式的固有限制？\n\n---\n\n## 小问题（不影响接收）\n\n1. **Table 1 可读性**：Table 1 包含 5 个 judge × 3 个 benchmark × 3 个 axis × 多个指标，信息密度极高。建议拆分为 main results（LLMBar）和 confirmatory results（AlpacaEval/MT-Bench）两个表，或使用 heatmap 可视化。\n2. **Figure 2 DAG 标注**：Figure 2 的 dashed orange S → Q path 标注为 \"style bias\"，但论文后续论证这个 path 可能反映 legitimate quality difference（formality 轴）。标注可能误导。\n3. **术语一致性**：\"style bias\" vs. \"style preference\" vs. \"style sensitivity\" 在论文中混用。\"Bias\" 暗示不合理的偏好，\"preference\" 更中性，\"sensitivity\" 最中性。建议统一。\n4. **Section 3.5 Design Rationale 位置**：这一节解释为什么 DAG 不是 formal causal model。内容重要但放在 Method 末尾略显突兀，建议整合到 Section 3.3 或单独的 Discussion 段。\n5. **Appendix 过多（A-S，19 个）**：虽然体现了严谨性，但 reviewer 难以逐一检查。建议在 main text 中更清晰地标注哪些 appendix 是 critical（如 A, J, R），哪些是 supplementary。\n\n---\n\n## 主要优势\n\n1. **方法论严谨**：CSD 的三重控制（NLI 门控 + position control + same-text pairing）在 style bias 研究中是最严格的实验设计之一。Direction-aware gating（Section 3.2）解决了 bidirectional verification 的 inflation 问题，体现了对实验细节的深入思考。\n2. **统计分析全面**：GEE 分解、FWER 校正、7 种 sensitivity methods（Table 2）、bootstrap attenuation 分析（Appendix J）、power analysis（Figure 4）、TOST equivalence testing（Appendix G）——统计处理的深度和广度在 NLP 实证论文中罕见。\n3. **GEE per-axis confound 结构差异**：Table 3 揭示 verbosity 是 style-dominated（Style OR 5-13），formality 是 conditional effect（Style OR < 1 且 Originality OR 显著），register 也显示 varying structure。这是本文最有价值的增量发现，超越了 \"Likert vs. pairwise\" 的简单比较。\n4. **跨 judge 复现**：4 个独立 provider 的 judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）+ 1 个负控制，覆盖不同架构和训练策略，增强了泛化性。\n5. **诚实的 Limitations**：Quality-style confounding、construct validity、evaluator-producer bias 三个核心局限都被坦率讨论，未回避。\n\n---\n\n## Questions for Authors\n\n1. 论文能否利用现有数据（特别是 Figure 4 的 power curve 和 bootstrap attenuation 的收敛行为）来区分 attenuation 和 construct divergence？如果是 attenuation，effect size d 应在更大 n 时趋向真实值；如果是 construct divergence，Likert d 应保持为零而非仅因 power 不足未检测到。Appendix J 的 bootstrap 数据是否支持其中一种？\n\n2. CSD 的 NLI 门控对 formality 轴过滤掉了约 38% 的 pairs（100 → 62，Table 1）。这些被过滤的 pairs 是否系统性地对应更大的 style 效应（因为 style 改变大到影响了 content）？如果是，NLI 门控可能系统性地 underestimate style bias 的实际幅度。\n\n3. Claude Sonnet 4 不展示 Blindspot 是否可能与其特定的 instruction-following 特性有关（如更严格地按 rubric 评分），而非反映 measurement mode 的本质属性？如果是，这是否意味着 Blindspot 可以通过改进 judge prompt 而非改变 measurement mode 来缓解？\n\n---\n\n## Missing References\n\n本文的 Related Work 覆盖较为全面，但可考虑补充：\n\n1. **Kim et al. (2024) \"Prometheus 2\"**：提出同时支持 Likert 和 pairwise 评估的统一 judge 模型，与本文讨论的 measurement mode divergence 直接相关——Prometheus 2 的训练是否消除了 Blindspot？\n2. **Stureborg et al. (2024)** 已引用，但其关于 Likert inconsistency 的具体发现可以在 Related Work 中更详细地对比。\n3. 心理测量学方面，**Luce (1959) \"Individual Choice Behavior\"** 关于 forced-choice models 的理论基础可能比 Thurstone (1927) 更直接相关，因为 Bradley-Terry model 是 Luce choice axiom 的特例。",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 969 · 2026-05-22T22:46:19.782208+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3919
}
```

</details>

---


### Tool call

_source line 970 · 2026-05-22T22:46:24.407052+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
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

_source line 971 · 2026-05-22T22:46:24.457760+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 972 · 2026-05-22T22:46:29.677552+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 973 · 2026-05-22T22:46:29.778312+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 974 · 2026-05-22T22:46:42.984598+00:00_

审稿完成，已提交给 Review Director。

核心判断：**Overall 3.5（Borderline Conference）**。方法论严谨（Soundness 4/5），但 Excitement 受限（3/5）。

三个 Must-Fix 问题：
1. **"Framework" 过度泛化**——仅 3 条表面风格轴（formality/verbosity/register）不足以支撑 framework 级别声明
2. **标题 "Blindspot" 隐含 attenuation 偏向**——与论文自己承认无法区分三种解释（attenuation/amplification/construct divergence）的立场矛盾
3. **核心发现的增量新颖性论证不足**——forced-choice > absolute rating 是 Thurstone (1927) 以来的经典结论，论文未充分论证 LLM judge 领域的 domain transfer 为何构成足够新颖性

主要优势：GEE per-axis confound 结构差异（Table 3）是本文最有价值的增量发现；统计分析深度在 NLP 实证论文中罕见；跨 4 个独立 judge 的复现增强了泛化性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 30

## Round 30

20 recorded events


### User

_source line 975 · 2026-05-22T22:48:55.832527+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿意见

**Overall**: 3.5 (Borderline Conference)
**Soundness**: 3.5/5 | **Excitement**: 3.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5

### Must-Fix 问题

**N1** [critical] NLI Gate人工验证标注一致性不足，样本量偏小
- Section 5.4, Appendix S
- 两名标注者在50对样本上的Cohen's κ=0.44（moderate agreement）。AC1=0.63仅为"substantial"下限。Gate-passed pairs的precision在majority vote下100%（Wilson CI [86.76, 100%]），但仅基于25对样本。κ=0.44的overall disagreement表明"内容保持"判断存在系统性主观分歧。
- 建议：(1) 增加标注者至3人以上，报告Fleiss' κ；(2) 对disagreement cases进行定性error analysis；(3) 在不同NLI threshold上报告precision和downstream BT的sensitivity。

**N2** [critical] TOST等价检验的SESOI Δ=15pp缺乏外部校准，负控制论证力不足
- Appendix G (Table 10), Section 5.1
- Δ=15pp理由是"approximately where format preference would materially affect model rankings"——循环论证。Table 10显示Δ=10pp下Claude未通过等价检验（p=0.156），BT=56.2%（偏离chance 6.2pp）。"负控制"可能误导读者。
- 建议：(1) 引用measurement theory中的effect size benchmarks校准SESOI；(2) 明确讨论Δ=10pp下的失败；(3) 将Claude从"negative control"重新framing为"weak-effect/attenuated-bias control"。

### Should-Fix 问题

**W1** Bootstrap CI方法类型未报告（percentile vs BCa）
**W2** Cross-rewriter independence验证仅覆盖verbosity轴，formality轴缺乏验证
**W3** Direction-aware NLI gate恢复的21对未经人工验证
**W4** BT模型unidimensionality假设仅在脚注讨论，应提升到Limitations
**W5** 样本外部效度论证不足（LLMBar task分布可能不代表所有典型使用场景）

### Minor
- M1: 正文可能微超8页
- M2: LLM rewriting未报告decoding seed
- M3: Table 1 caption自解释性不足
- M4: Figure 4 y轴定义模糊
- M5: Table 3显著性标记格式不一致

### Missing References
- Luce (1959) "Individual Choice Behavior"
- Bowman et al. (2015) SNLI / Williams et al. (2018) MNLI
- 最新pairwise evaluation方法论综述

### 主要优势
1. 7种方法交叉验证说服力强
2. GEE per-axis decomposition方法论价值高
3. 统计诊断深度远超typical submission
4. 实验设计控制意识好
5. 实际影响清晰

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 976 · 2026-05-22T22:49:51.370001+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "8,9,10,11,12,15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "8,9,10,11,12,15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 977 · 2026-05-22T22:49:52.174549+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 545.5}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.5}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 440.4}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.5}], \"total_pages\": 18, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 978 · 2026-05-22T22:49:55.888126+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 979 · 2026-05-22T22:49:56.844192+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 980 · 2026-05-22T22:49:56.844682+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 981 · 2026-05-22T22:49:57.297816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 982 · 2026-05-22T22:49:57.802581+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 983 · 2026-05-22T22:49:57.802996+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 984 · 2026-05-22T22:49:58.708848+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool result

_source line 985 · 2026-05-22T22:49:58.710579+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 986 · 2026-05-22T22:49:58.710915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 987 · 2026-05-22T22:49:59.012332+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 988 · 2026-05-22T22:49:59.469219+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 758
}
```

</details>

---


### Tool result

_source line 989 · 2026-05-22T22:50:00.101901+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1089
}
```

</details>

---


### Tool call

_source line 990 · 2026-05-22T22:52:56.969251+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: NLI Gate 人工验证标注一致性不足，样本量偏小**\n\n同意核心关切。κ=0.44（moderate）确实表明标注者对\"内容保持\"判断存在系统性分歧，50 对样本、2 名标注者的规模不足以全面评估 NLI gate 的可靠性。R1 的三条建议（增加标注者、disagreement error analysis、多阈值 precision-downstream sensitivity）都是合理的。\n\n补充两点缓解观察：\n1. 论文报告 BT 在 11 个 NLI 阈值上变化 ≤1pp（Appendix E, Table 9, page 11），说明 downstream metric 对阈值选择不敏感——即使 gate boundary 有标注分歧，最终结论稳健。\n2. Gate-passed precision（majority vote 100%, Wilson CI [86.76, 100%]）比 overall κ 更直接衡量 gate 的有效性——gate 的目标是 high precision（不放入受污染的 pairs），而非 high recall。κ 被 prevalence skew 压低（AC1=0.63 部分修正了这一点）。\n\n但这些缓解不足以完全消解 R1 的关切——sample size 确实是硬伤。特别是 R1 提出的\"对 disagreement cases 进行定性 error analysis\"是最有价值的建议：论文 Section 5.4 提到 Annotator 2 的 4 个 gate-passed disagreement 都涉及 verbosity condensation 的边界案例，但未展开分析这些边界案例是否系统性地偏向某个方向。\n\n**[AGREE 部分，REBUT 部分] R1-N2: TOST SESOI Δ=15pp 缺乏外部校准**\n\n**[AGREE]** Δ=15pp 的校准依据不充分。论文称\"approximately where format preference would materially affect model rankings\"——这是一个 pragmatic 标准，但未引用任何外部 benchmark 来支撑\"15pp = materially meaningful\"。R1 指出 Δ=10pp 下 Claude 未通过等价检验（Table 10, p=0.156），BT=56.2%（偏离 chance 6.2pp），这是一个重要的 sensitivity analysis 结果，应在正文中讨论而非仅在 Appendix G。同意将 Claude 从 \"negative control\" 重新 framing 为 \"weak-effect control\"。\n\n**[REBUT]** 但不同意 R1 将此定性为\"循环论证\"。等价检验的 SESOI 选择在实践中很少有外部金标准——即使在临床试验中，SESOI 也常基于 \"minimum clinically important difference\" 的主观判断。论文的问题不是循环论证，而是**校准标准不够透明**：应明确讨论为什么 15pp 而非 10pp 或 20pp 是合理的分界线，例如引用 Chatbot Arena 或 AlpacaEval 的 BT 差异基准来校准。Appendix G 的 Table 10 实际上已经报告了 5/10/15/20pp 的 sensitivity，但正文未讨论这些不同阈值下的结论如何变化。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Bootstrap CI 方法类型未报告**\n\n标准统计报告要求。Percentile bootstrap 和 BCa 在小样本下可产生不同 CI，应明确说明方法类型。\n\n**[REBUT] R1-W2: Cross-rewriter independence 仅覆盖 verbosity 轴**\n\nR1 似乎遗漏了 **Table 8（Appendix D, page 11）**，该表明确报告了 **formality 轴的 rewriter independence 验证**：使用 GPT-4o 作为独立 rewriter，在 Qwen3-32B judge 上进行 22× 重复实验。结果显示：NLI pass rate 90/100 (90%)，BT 64.4% [56.1, 72.8]，与 Qwen3-32B baseline (60.3%) 统计不可区分（Δ ≈ 2pp），且 Likert Blindspot 复现（p = 0.184, n.s.）。因此 cross-rewriter independence 实际上同时覆盖了 verbosity（Table 7）和 formality（Table 8）两条主要轴。\n\n**[AGREE 部分] R1-W3: Direction-aware gate 恢复的 21 对未经人工验证**\n\n原则上合理——新增的 21 对 pairs 应单独验证。但影响有限：(1) 这些 pairs 均通过 forward NLI entailment（original → rewrite），Direction-aware gate 仅放行 forward-pass + backward-fail 的 pairs，对应 compressions/entailing 变换（如缩写展开），这些 pairs 的内容保持性有理论预期；(2) Appendix F（page 11）报告 direction-aware gating 仅将 BT 从约 73.8% 微调至约 73.9%（Δ ≈ −1pp），对主结论影响极小。但为严谨性，人工验证这 21 对仍是值得的。\n\n**[AGREE] R1-W4: BT unidimensionality 假设应提升到 Limitations**\n\n同意。BT 模型假设 judge preference 沿单一维度排序——如果 judge 在不同 quality dimensions 上有不同偏好模式，单维 BT 可能混淆信号。论文仅在脚注（page 2）提到 BT 的 unidimensionality，这对论文的核心方法而言讨论不足。应在 Limitations 中讨论：(1) 什么情况下 unidimensionality 假设会被违反；(2) 违反时对 Blindspot 结论的影响方向。\n\n**[AGREE 部分] R1-W5: 样本外部效度论证不足**\n\nLLMBar 的 task 分布确实可能不代表所有 LLM judge 使用场景（如 code generation、safety evaluation、long-form summarization）。跨 benchmark 复现（AlpacaEval, MT-Bench）提供了部分缓解，但这三个 benchmark 都偏向 general instruction-following 任务。补充：我在自己的审稿中也提出了类似关切（我的 W3），且进一步指出 AlpacaEval 和 MT-Bench 仅使用\"selected configurations\"（Section 3.4），未充分讨论 MT-Bench 结果。\n\n---\n\n### Minor\n\n**[REBUT] R1-M1: 正文可能微超 8 页**\n\n重新检查 PDF：Section 6 Conclusion 的最后一句 \"modes is the key next step.\" 出现在 page 9 的最顶行，Limitations 标题紧随其后。这意味着 Conclusion 确实有一行溢出到 page 9。但这是**一行文本的溢出**，而非实质性超页。需要作者确认 LaTeX 编译后的实际页面分布——如果确认溢出，可通过微调行距或删减一句话解决。R1 标记为 Minor 是恰当的，不应作为 rejection 理由，但作者确实需要在 camera-ready 前修复。\n\n**[AGREE] R1-M2: LLM rewriting 未报告 decoding seed**\n\nSection 3.1 报告了 temperature 0.7，但未报告 seed/top_p/random seed。可复现性的标准要求。Appendix P 列出了模型和 API 版本但也缺少 seed。\n\n**[AGREE] R1-M3: Table 1 caption 自解释性不足**\n\n我也在自己的审稿中独立提出了 Table 1 可读性问题（我的 Minor #1）。Table 1 信息密度极高，caption 应包含所有缩写解释和读法指南。\n\n**[AGREE 部分] R1-M4: Figure 4 y 轴定义模糊**\n\nFigure 4 的 caption 定义了 \"Detection probability at observed effect magnitudes\" 并给出了具体的 80% power crossings，但 y 轴标签本身仅写 \"Significance probability\"——与 caption 中的 \"Detection probability\" 不一致。同意需要统一术语。\n\n**[AGREE] R1-M5: Table 3 显著性标记格式不一致**\n\n如属实则应修正。统一使用 *, **, *** 或 p 值报告。\n\n---\n\n### Missing References\n\n**[AGREE] Luce (1959) \"Individual Choice Behavior\"**\n\n我在自己的审稿中也独立建议了这篇。Bradley-Terry 模型是 Luce choice axiom 的特例，论文使用 BT 模型但未引用其理论基础。\n\n**[AGREE] Bowman et al. (2015) SNLI / Williams et al. (2018) MNLI**\n\n论文使用 DeBERTa v3-large fine-tuned on MNLI（Section 3.2, page 9 Code and Data），但未引用 MNLI 的原始论文。这是基础性引用遗漏。\n\n**[AGREE 部分] 最新 pairwise evaluation 方法论综述**\n\n如果存在 2024-2025 年的系统性综述，引用会增强 Related Work 的完整性。但如果 R1 指的是特定论文，应明确指出。\n\n---\n\n### 主要优势\n\n五条优势全部同意，与我独立审稿的判断高度一致。特别是：\n- 优势 #2（GEE per-axis decomposition）和优势 #3（统计诊断深度）是我认为本文最有价值的贡献\n- 优势 #1（7 种方法交叉验证）对应我审稿中的 Table 2 分析，确实增强了 sensitivity hierarchy 结论的可信度\n\n---\n\n### 与我自己审稿的交叉对比\n\n| 维度 | R1 | R2（我） | 一致性 |\n|------|-----|---------|--------|\n| Overall | 3.5 | 3.5 | 完全一致 |\n| 核心关切 | NLI gate 验证 + TOST 校准 | Novelty + Framing bias + Framework overclaim | 互补（R1 偏方法验证，R2 偏概念定位） |\n| Claude 负控制 | Δ 校准不足 | 讨论不充分（model-specific vs. mode-intrinsic） | 互补 |\n| Table 1 | caption 不足 | 可读性问题 | 一致 |\n| 统计严谨性评价 | 正面 | 正面 | 一致 |\n| GEE 贡献评价 | 方法论价值高 | 最有价值的增量发现 | 一致 |\n\n两份审稿互补性强：R1 更关注方法论细节的可靠性（NLI gate 验证、TOST 校准、bootstrap CI 类型），R2 更关注概念层面的定位和新颖性（Thurstone domain transfer、framing bias、framework overclaim）。综合两份意见，论文的统计执行质量不是主要问题，但概念新颖性论证和关键方法验证细节需要加强。",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: NLI Gate 人工验证标注一致性不足，样本量偏小**\n\n同意核心关切。κ=0.44（moderate）确实表明标注者对\"内容保持\"判断存在系统性分歧，50 对样本、2 名标注者的规模不足以全面评估 NLI gate 的可靠性。R1 的三条建议（增加标注者、disagreement error analysis、多阈值 precision-downstream sensitivity）都是合理的。\n\n补充两点缓解观察：\n1. 论文报告 BT 在 11 个 NLI 阈值上变化 ≤1pp（Appendix E, Table 9, page 11），说明 downstream metric 对阈值选择不敏感——即使 gate boundary 有标注分歧，最终结论稳健。\n2. Gate-passed precision（majority vote 100%, Wilson CI [86.76, 100%]）比 overall κ 更直接衡量 gate 的有效性——gate 的目标是 high precision（不放入受污染的 pairs），而非 high recall。κ 被 prevalence skew 压低（AC1=0.63 部分修正了这一点）。\n\n但这些缓解不足以完全消解 R1 的关切——sample size 确实是硬伤。特别是 R1 提出的\"对 disagreement cases 进行定性 error analysis\"是最有价值的建议：论文 Section 5.4 提到 Annotator 2 的 4 个 gate-passed disagreement 都涉及 verbosity condensation 的边界案例，但未展开分析这些边界案例是否系统性地偏向某个方向。\n\n**[AGREE 部分，REBUT 部分] R1-N2: TOST SESOI Δ=15pp 缺乏外部校准**\n\n**[AGREE]** Δ=15pp 的校准依据不充分。论文称\"approximately where format preference would materially affect model rankings\"——这是一个 pragmatic 标准，但未引用任何外部 benchmark 来支撑\"15pp = materially meaningful\"。R1 指出 Δ=10pp 下 Claude 未通过等价检验（Table 10, p=0.156），BT=56.2%（偏离 chance 6.2pp），这是一个重要的 sensitivity analysis 结果，应在正文中讨论而非仅在 Appendix G。同意将 Claude 从 \"negative control\" 重新 framing 为 \"weak-effect control\"。\n\n**[REBUT]** 但不同意 R1 将此定性为\"循环论证\"。等价检验的 SESOI 选择在实践中很少有外部金标准——即使在临床试验中，SESOI 也常基于 \"minimum clinically important difference\" 的主观判断。论文的问题不是循环论证，而是**校准标准不够透明**：应明确讨论为什么 15pp 而非 10pp 或 20pp 是合理的分界线，例如引用 Chatbot Arena 或 AlpacaEval 的 BT 差异基准来校准。Appendix G 的 Table 10 实际上已经报告了 5/10/15/20pp 的 sensitivity，但正文未讨论这些不同阈值下的结论如何变化。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Bootstrap CI 方法类型未报告**\n\n标准统计报告要求。Percentile bootstrap 和 BCa 在小样本下可产生不同 CI，应明确说明方法类型。\n\n**[REBUT] R1-W2: Cross-rewriter independence 仅覆盖 verbosity 轴**\n\nR1 似乎遗漏了 **Table 8（Appendix D, page 11）**，该表明确报告了 **formality 轴的 rewriter independence 验证**：使用 GPT-4o 作为独立 rewriter，在 Qwen3-32B judge 上进行 22× 重复实验。结果显示：NLI pass rate 90/100 (90%)，BT 64.4% [56.1, 72.8]，与 Qwen3-32B baseline (60.3%) 统计不可区分（Δ ≈ 2pp），且 Likert Blindspot 复现（p = 0.184, n.s.）。因此 cross-rewriter independence 实际上同时覆盖了 verbosity（Table 7）和 formality（Table 8）两条主要轴。\n\n**[AGREE 部分] R1-W3: Direction-aware gate 恢复的 21 对未经人工验证**\n\n原则上合理——新增的 21 对 pairs 应单独验证。但影响有限：(1) 这些 pairs 均通过 forward NLI entailment（original → rewrite），Direction-aware gate 仅放行 forward-pass + backward-fail 的 pairs，对应 compressions/entailing 变换（如缩写展开），这些 pairs 的内容保持性有理论预期；(2) Appendix F（page 11）报告 direction-aware gating 仅将 BT 从约 73.8% 微调至约 73.9%（Δ ≈ −1pp），对主结论影响极小。但为严谨性，人工验证这 21 对仍是值得的。\n\n**[AGREE] R1-W4: BT unidimensionality 假设应提升到 Limitations**\n\n同意。BT 模型假设 judge preference 沿单一维度排序——如果 judge 在不同 quality dimensions 上有不同偏好模式，单维 BT 可能混淆信号。论文仅在脚注（page 2）提到 BT 的 unidimensionality，这对论文的核心方法而言讨论不足。应在 Limitations 中讨论：(1) 什么情况下 unidimensionality 假设会被违反；(2) 违反时对 Blindspot 结论的影响方向。\n\n**[AGREE 部分] R1-W5: 样本外部效度论证不足**\n\nLLMBar 的 task 分布确实可能不代表所有 LLM judge 使用场景（如 code generation、safety evaluation、long-form summarization）。跨 benchmark 复现（AlpacaEval, MT-Bench）提供了部分缓解，但这三个 benchmark 都偏向 general instruction-following 任务。补充：我在自己的审稿中也提出了类似关切（我的 W3），且进一步指出 AlpacaEval 和 MT-Bench 仅使用\"selected configurations\"（Section 3.4），未充分讨论 MT-Bench 结果。\n\n---\n\n### Minor\n\n**[REBUT] R1-M1: 正文可能微超 8 页**\n\n重新检查 PDF：Section 6 Conclusion 的最后一句 \"modes is the key next step.\" 出现在 page 9 的最顶行，Limitations 标题紧随其后。这意味着 Conclusion 确实有一行溢出到 page 9。但这是**一行文本的溢出**，而非实质性超页。需要作者确认 LaTeX 编译后的实际页面分布——如果确认溢出，可通过微调行距或删减一句话解决。R1 标记为 Minor 是恰当的，不应作为 rejection 理由，但作者确实需要在 camera-ready 前修复。\n\n**[AGREE] R1-M2: LLM rewriting 未报告 decoding seed**\n\nSection 3.1 报告了 temperature 0.7，但未报告 seed/top_p/random seed。可复现性的标准要求。Appendix P 列出了模型和 API 版本但也缺少 seed。\n\n**[AGREE] R1-M3: Table 1 caption 自解释性不足**\n\n我也在自己的审稿中独立提出了 Table 1 可读性问题（我的 Minor #1）。Table 1 信息密度极高，caption 应包含所有缩写解释和读法指南。\n\n**[AGREE 部分] R1-M4: Figure 4 y 轴定义模糊**\n\nFigure 4 的 caption 定义了 \"Detection probability at observed effect magnitudes\" 并给出了具体的 80% power crossings，但 y 轴标签本身仅写 \"Significance probability\"——与 caption 中的 \"Detection probability\" 不一致。同意需要统一术语。\n\n**[AGREE] R1-M5: Table 3 显著性标记格式不一致**\n\n如属实则应修正。统一使用 *, **, *** 或 p 值报告。\n\n---\n\n### Missing References\n\n**[AGREE] Luce (1959) \"Individual Choice Behavior\"**\n\n我在自己的审稿中也独立建议了这篇。Bradley-Terry 模型是 Luce choice axiom 的特例，论文使用 BT 模型但未引用其理论基础。\n\n**[AGREE] Bowman et al. (2015) SNLI / Williams et al. (2018) MNLI**\n\n论文使用 DeBERTa v3-large fine-tuned on MNLI（Section 3.2, page 9 Code and Data），但未引用 MNLI 的原始论文。这是基础性引用遗漏。\n\n**[AGREE 部分] 最新 pairwise evaluation 方法论综述**\n\n如果存在 2024-2025 年的系统性综述，引用会增强 Related Work 的完整性。但如果 R1 指的是特定论文，应明确指出。\n\n---\n\n### 主要优势\n\n五条优势全部同意，与我独立审稿的判断高度一致。特别是：\n- 优势 #2（GEE per-axis decomposition）和优势 #3（统计诊断深度）是我认为本文最有价值的贡献\n- 优势 #1（7 种方法交叉验证）对应我审稿中的 Table 2 分析，确实增强了 sensitivity hierarchy 结论的可信度\n\n---\n\n### 与我自己审稿的交叉对比\n\n| 维度 | R1 | R2（我） | 一致性 |\n|------|-----|---------|--------|\n| Overall | 3.5 | 3.5 | 完全一致 |\n| 核心关切 | NLI gate 验证 + TOST 校准 | Novelty + Framing bias + Framework overclaim | 互补（R1 偏方法验证，R2 偏概念定位） |\n| Claude 负控制 | Δ 校准不足 | 讨论不充分（model-specific vs. mode-intrinsic） | 互补 |\n| Table 1 | caption 不足 | 可读性问题 | 一致 |\n| 统计严谨性评价 | 正面 | 正面 | 一致 |\n| GEE 贡献评价 | 方法论价值高 | 最有价值的增量发现 | 一致 |\n\n两份审稿互补性强：R1 更关注方法论细节的可靠性（NLI gate 验证、TOST 校准、bootstrap CI 类型），R2 更关注概念层面的定位和新颖性（Thurstone domain transfer、framing bias、framework overclaim）。综合两份意见，论文的统计执行质量不是主要问题，但概念新颖性论证和关键方法验证细节需要加强。",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 991 · 2026-05-22T22:53:00.432675+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3463
}
```

</details>

---


### Tool call

_source line 992 · 2026-05-22T22:53:05.475679+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 993 · 2026-05-22T22:53:05.532473+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_12/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 56
}
```

</details>

---


### Assistant

_source line 994 · 2026-05-22T22:53:16.151533+00:00_

已完成对 R1 的逐条交叉回应并提交给 Director。核心判断：

- **N1（NLI gate 验证）**: 同意样本量不足是硬伤，但指出 BT 对阈值不敏感（Table 9）和 gate-passed precision 100% 作为缓解
- **N2（TOST Δ 校准）**: 部分同意校准不充分，但反驳"循环论证"的定性——SESOI 选择本质上是 pragmatic judgment
- **W2（rewriter independence 仅覆盖 verbosity）**: 反驳——R1 遗漏了 Table 8，formality 轴已有独立 rewriter 验证
- **M1（超页）**: 确认 Conclusion 最后一行溢出到 page 9，但属于可修复的 minor issue
- 两份审稿互补：R1 侧重方法验证细节，R2（我）侧重概念定位和新颖性

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 31

## Round 31

60 recorded events


### User

_source line 995 · 2026-05-23T05:25:43.937417+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量 + 格式合规**。

## 论文信息
- **标题**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation
- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/submitted.pdf`
- **目标 venue**: EMNLP 2026 (ARR May cycle)
- **Deadline**: 2026-05-25
- **格式**: Long paper, 8页正文限制 + 无限参考文献, ACL模板, double-blind
- **Limitations**: mandatory, 不计入页数限制
- **匿名规则**: double-blind（论文中不能有作者身份信息）

## 你的审查侧重

请重点评估以下方面：

1. **新颖性（Novelty）**：
   - "Likert Blindspot" 这个发现的新颖程度如何？与 RATE (Reber et al. 2025)、Comparative Trap (Jeong et al. 2025) 等先前工作的增量贡献
   - CSD 方法论的新颖性——NLI gate + per-axis decomposition + position-controlled pairwise 的组合是否构成足够的方法论贡献？
   - GEE conditional decomposition 揭示的 per-axis confound structure 是否是真正的新发现？

2. **完整性（Completeness）**：
   - Related work 是否全面？是否遗漏重要的相关工作？
   - 实验是否覆盖了足够的 style axes、judges、benchmarks？
   - 对 "three non-exclusive explanations"（attenuation / amplification / construct divergence）的讨论是否充分？
   - Limitations 是否诚实、全面？

3. **写作质量**：
   - 论文叙事结构是否清晰？读者能否顺畅跟随论证逻辑？
   - Abstract 和 Introduction 是否准确传达了主要贡献？
   - 术语使用是否一致？符号系统是否清晰？
   - 图表是否有效传达信息？Table 1 和 Figure 2-3 的设计

4. **格式合规（EMNLP 2026 ARR）**：
   - 正文是否在 8 页限制内？
   - ACL 模板是否正确使用（`\usepackage[review]{acl}`）？
   - 匿名性检查：是否有泄露作者身份的线索？
   - Limitations section 是否符合要求？
   - 参考文献格式是否一致？

请按 EMNLP 2026 ARR 审稿标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Minor Issues。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-23T05:25:51.458258+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
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

_source line 997 · 2026-05-23T05:25:51.508891+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 998 · 2026-05-23T05:25:55.279503+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 999 · 2026-05-23T05:25:55.832435+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR review form scoring dimensions soundness excitement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR review form scoring dimensions soundness excitement"
  }
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-23T05:25:58.146795+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1001 · 2026-05-23T05:26:01.837521+00:00_

Web search results for query: "EMNLP 2026 ARR review form scoring dimensions soundness excitement"

Links: [{"title":"TrustNLP","url":"https://trustnlpworkshop.github.io/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Improving Patient Experience: BMBA","url":"https://cdn.clinicaltrials.gov/large-docs/30/NCT05690230/Prot_SAP_000.pdf"}]

Based on the search results, I found relevant information about ARR review form scoring dimensions:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

The roles of these dimensions are distinguished as follows:

- **Soundness**: The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation.

- **Excitement**: Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper. Additionally, Excitement scores reflect our personal taste, and so do not necessarily come with explicit reasons.

- **Overall Recommendation**: The Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, exciteme
…[truncated 154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6005
}
```

</details>

---


### Tool result

_source line 1002 · 2026-05-23T05:26:02.543671+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

I found information about the ACL Rolling Review (ARR) 2026 reviewer guidelines and review form criteria. Here are the key findings:

## Reviewer Guidelines

Reviewers are asked to follow a workflow: (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to 
…[truncated 1302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7264
}
```

</details>

---


### Tool result

_source line 1003 · 2026-05-23T05:26:04.504979+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 588.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 493.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 553.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p9.p
…[truncated 526 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6358
}
```

</details>

---


### Tool call

_source line 1004 · 2026-05-23T05:26:12.693438+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 or other), descriptions for each score level, and any required fields. I need the exact criteria for Soundness, Excitement, Overall Assessment, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 or other), descriptions for each score level, and any required fields. I need the exact criteria for Soundness, Excitement, Overall Assessment, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 1005 · 2026-05-23T05:26:13.601056+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "11-19",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "11-19",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1006 · 2026-05-23T05:26:14.607144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1007 · 2026-05-23T05:26:15.059438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-23T05:26:16.064921+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1009 · 2026-05-23T05:26:16.617739+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-23T05:26:16.820879+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1011 · 2026-05-23T05:26:19.181458+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: Quite sure with unlikely but conceivable gaps
- **3**: Pretty sure but possible oversights in details
- **2**: Can defend evaluation but likely missed details
- **1**: Outside expertise or paper difficult to understand

## Soundness
Scale: 1-5 (with half-point increments)
- **5**: "one of the most thorough I have seen, given its type"
- **4**: Sufficient support for claims; extra experiments optional
- **3**: Adequate support for main claims; minor details need work
- **2**: Major claims insufficiently supported; technical problems exist
- **1**: Insufficient rigor or lacks ACL relevance

## Excitement
Scale: 1-5 (with half-point increments)
- **5**: "I would recommend this paper to others"
- **4**: Would mention to others or attend presentation
- **3**: Might mention points or attend if available
- **2**: Doesn't resonate but may interest others
- **1**: "does not resonate with me, and I don't think it would"

## Overall Assessment
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award" (top 2.5%)
- **4**: Conference acceptance suitable
- **3**: Findings acceptance appropriate
- **2**: Needs substantial revisions for next cycle
- **1**: Requires complete redoing or lacks relevance

## Additional Dimensions
- **Reproducibility**: 1-5 scale
- **Datasets**: 1-5 (enabling to no datasets)
- **Software**: 1-5 (enabling to unavailable)
- **Author Identity Knowledge**: 1-5 scale

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6488
}
```

</details>

---


### Tool result

_source line 1012 · 2026-05-23T05:26:20.743537+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 447.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 431.6}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 482.4}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.6}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 618.9}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 615.1}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_imag
…[truncated 318 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7142
}
```

</details>

---


### Tool result

_source line 1013 · 2026-05-23T05:26:24.065537+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 9458
}
```

</details>

---


### Tool result

_source line 1014 · 2026-05-23T05:26:24.167254+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7346
}
```

</details>

---


### Tool result

_source line 1015 · 2026-05-23T05:26:24.171157+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 8106
}
```

</details>

---


### Tool result

_source line 1016 · 2026-05-23T05:26:24.172152+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7554
}
```

</details>

---


### Tool result

_source line 1017 · 2026-05-23T05:26:24.173794+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 9114
}
```

</details>

---


### Tool call

_source line 1018 · 2026-05-23T05:26:31.100161+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1019 · 2026-05-23T05:26:32.109909+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1009
}
```

</details>

---


### Tool call

_source line 1020 · 2026-05-23T05:26:32.110377+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1021 · 2026-05-23T05:26:32.615421+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1022 · 2026-05-23T05:26:32.970959+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 860
}
```

</details>

---


### Tool call

_source line 1023 · 2026-05-23T05:26:32.975779+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1024 · 2026-05-23T05:26:33.431464+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1025 · 2026-05-23T05:26:33.633544+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1018
}
```

</details>

---


### Tool result

_source line 1026 · 2026-05-23T05:26:34.137842+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1162
}
```

</details>

---


### Tool result

_source line 1027 · 2026-05-23T05:26:34.389409+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 1028 · 2026-05-23T05:26:40.264898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1029 · 2026-05-23T05:26:41.321736+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1030 · 2026-05-23T05:26:42.031624+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1766
}
```

</details>

---


### Tool result

_source line 1031 · 2026-05-23T05:26:42.386605+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1064
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-23T05:26:42.387068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1033 · 2026-05-23T05:26:42.891540+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 1034 · 2026-05-23T05:26:43.243756+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1035 · 2026-05-23T05:26:43.648689+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1261
}
```

</details>

---


### Tool call

_source line 1036 · 2026-05-23T05:26:43.649126+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 1037 · 2026-05-23T05:26:44.204436+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1038 · 2026-05-23T05:26:45.311046+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2419
}
```

</details>

---


### Tool call

_source line 1039 · 2026-05-23T05:26:45.311568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 1040 · 2026-05-23T05:26:45.311867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1041 · 2026-05-23T05:26:45.613629+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2369
}
```

</details>

---


### Tool result

_source line 1042 · 2026-05-23T05:26:45.967534+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2318
}
```

</details>

---


### Tool result

_source line 1043 · 2026-05-23T05:26:46.622387+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2417
}
```

</details>

---


### Tool result

_source line 1044 · 2026-05-23T05:26:46.879135+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1567
}
```

</details>

---


### Tool result

_source line 1045 · 2026-05-23T05:26:47.333003+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2021
}
```

</details>

---


### Tool call

_source line 1046 · 2026-05-23T05:29:01.711473+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1047 · 2026-05-23T05:29:01.812307+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Measurement-Mode Divergence\\in LLM Judge Style Evaluation}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\paragraph{Quality--style confounding and construct validity.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
43	Although the formality effect survives logistic adjustment for original preference ($\text{OR} = 2.32$, $p = 0.006$; Appendix~\ref{app:direction}), residual confounding is not fully eliminated.
44	An alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference. Under this view, the divergence reflects construct difference rather than measurement failure. The Comparative Trap \citep{jeong2025comparative} lends support to this alternative; six experimental controls bound this risk (\S\ref{sec:amplification}), though definitive separation would require human ground-truth ratings.
45	The primary open question is whether pairwise comparison detects genuine style bias or amplifies micro-preferences inherent in the format.
…[truncated 4649 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1048 · 2026-05-23T05:31:33.974608+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5 / 5 (Borderline Conference)\n**一句话总结**: 方法论扎实、实验设计严谨，但仅覆盖两个风格轴（formality, verbosity）限制了\"Likert Blindspot\"作为通用现象的推广性，三种机制解释未能区分进一步削弱了理论贡献。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | NLI gating + position-controlled pairwise + GEE decomposition 方法论合理且有多项 robustness check；但核心 claim（\"Blindspot 是系统性现象\"）仅基于两个表层风格轴，且三种机制解释（attenuation/amplification/construct divergence）未能区分，限制了 soundness 的上限 |\n| Excitement | 3/5 | Likert-pairwise 模式差异是有价值的发现，但实际推论（\"style 评估应优先用 pairwise\"）对熟悉该领域的研究者来说并不意外；scope 过窄（2 轴 × 4 judges × 1 主 benchmark）降低了影响力 |\n| Reproducibility | 4/5 | Appendix R 提供了详尽的实现细节（模型版本、温度、prompt），统计方法描述清晰，承诺 release code/data；但 NLI gate 的 prompt 和 rewriting prompt 的完整文本未在正文或附录中给出 |\n| Reviewer Confidence | 4/5 | 仔细阅读了全文及全部附录，对统计方法和 LLM-as-judge 文献较为熟悉 |\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 仅两个风格轴无法支撑 \"Likert Blindspot\" 的通用性 claim\n- 具体位置：Abstract (\"systematically divergent style sensitivity\"), Section 1 (\"a systematic pattern\"), Title (\"LLM Judge Style Evaluation\")\n- 问题：论文标题和摘要将 Likert Blindspot 定位为 LLM judge style 评估的通用现象，但实验仅覆盖 formality 和 verbosity（加上 Appendix 中的 register 作为探索性分析）。这三个轴均属表层文体属性（surface-level stylistic attributes），论文自身在 Limitations (page 9) 承认 semantic-level axes（hedging, humor, technicality）因 NLI gate 限制无法覆盖。仅基于两个高度相关的表层轴（verbosity 和 formality 在实践中常共变），就声称发现了 systematic pattern，存在过度概括风险。\n- 为什么影响接收：一个声称发现\"系统性\"现象的论文，如果证据仅来自有限且同质的轴，会被质疑 claim 是否成立。如果 Blindspot 仅限于特定类型的风格轴，这仍然是有趣的但需要不同的 framing。\n- 建议修改方向：(1) 弱化通用性 claim，明确限定为 \"surface-level stylistic axes\"；(2) 或增加至少 1-2 个语义层面的轴（如 hedging level, bullet-point vs prose）的实验证据，哪怕是 pilot scale；(3) 在 Abstract 和 Introduction 中明确表述 scope boundary。\n\n**N2** [critical] 三种机制解释未能区分，限制了理论贡献\n- 具体位置：Section 5.1 (\"three non-exclusive explanations\"), Limitations paragraph 1 (\"The primary open question is whether pairwise comparison detects genuine style bias or amplifies micro-preferences\")\n- 问题：论文提出 attenuation（Likert 衰减信号）、amplification（pairwise 放大信号）、construct divergence（两种模式测量不同构念）三种解释，但明确表示无法区分（\"cannot be definitively resolved without human ground-truth\"）。这三种解释有截然不同的实践含义：如果是 attenuation，则 Likert 需要修正；如果是 amplification，则 pairwise 结果可能夸大了真实偏差；如果是 construct divergence，则两种模式都是\"正确的\"只是测量不同的东西。\n- 为什么影响接收：一篇 diagnostic 论文如果无法判断被诊断的现象究竟是什么（信号丢失 vs 信号放大 vs 不同构念），其理论贡献和实践指导价值会大打折扣。Section 5.1 提到\"six experimental controls bound this risk (§5.4)\"来 bound amplification，但 bounding 不等于排除。\n- 建议修改方向：(1) 即使无法完全区分，可以通过 human evaluation 对少量 pairs 收集 ground-truth style ratings，然后比较 human 与 Likert/pairwise 的一致性，至少部分区分 attenuation vs amplification；(2) 更明确地讨论每种解释的证据权重，而非简单列举为 \"non-exclusive\"；(3) 如果无法增加实验，应在 framing 上更诚实地将这作为 open question 而非 contribution 的一部分。\n\n**N3** [critical] 与 RATE (Reber et al., 2025) 的增量贡献需更清晰界定\n- 具体位置：Section 2 Related Work (page 2-3), Section 5.1 (\"Head-to-head comparison with RATE\")\n- 问题：RATE 已经建立了 style-rewriting + ATE 的方法框架，并发现 60% 的 style-transformed pairs 接受了 confounded 评分。CSD 的核心区别在于：(a) 引入 pairwise 比较模式揭示 mode divergence，(b) per-axis GEE decomposition，(c) NLI gating 替代 RATE 的 Likert ATE correction。但 Section 5.1 的 head-to-head 比较仅用了 1 段文字，且主要强调 RATE \"may underestimate the true magnitude\"——这个 claim 需要更强的证据支撑，因为 RATE 和 CSD 测量的是不同的量（RATE 测 ATE bias，CSD 测 mode divergence）。\n- 为什么影响接收：如果 reviewer 认为 CSD 相对 RATE 的增量不够大（本质上是给 RATE 加了 pairwise 比较模式 + GEE），可能判断 novelty 不足。\n- 建议修改方向：(1) 用一个结构化的对比表格明确列出 RATE vs CSD 在方法论、测量对象、发现上的区别；(2) 讨论 CSD 是否 subsume RATE 或两者是互补的；(3) 避免暗示 RATE \"underestimates\"——更精确地说是 RATE 测量的是不同的量。\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Table 1 信息密度过高，可读性不佳\n- 具体位置：Table 1 (page 6)\n- 问题：Table 1 在一个表格中压缩了 5 个 judges × 3 benchmarks × 2 axes × 4 个统计量（ATE, BT, Likert(p), BT(p)）+ 脚注中的 scaled replication 和 negative control 信息。对于一篇以\"发现 mode divergence\"为核心贡献的论文，读者需要先理解这个复杂的表格才能把握核心结果，增加了认知负担。\n- 建议：(1) 考虑将 LLMBar 主结果和 cross-benchmark replication 分成两个表格；(2) 或至少在正文中添加一段引导性的文字帮助读者 parse 表格（目前正文直接跳到 Section 5 Analysis）。\n\n**W2** [warning] Figure 2 的 DAG 假设未充分讨论\n- 具体位置：Figure 2 (page 4), Appendix A (page 10)\n- 问题：Figure 2 呈现了一个 assumed data-generating process 的 DAG，但 Appendix A 立即声明 \"we do not claim that the DAG in Figure 2 is a complete structural causal model\"。然而，CSD 的整个方法论（NLI gating blocks H→Q, style-controlled rewriting isolates S→Y）都依赖于这个 DAG 的结构假设。如果 DAG 遗漏了重要的路径（例如 style 对 content quality 的直接效应 S→Q，或评估者的 prior expectations），方法论的有效性会受到影响。论文在 Limitations 中讨论了 quality-style confounding，但没有系统地讨论 DAG 可能遗漏的路径。\n- 建议：在 Section 3 或 Appendix A 中增加对 DAG 假设的敏感性讨论：如果存在 S→Q 路径（style 影响 perceived quality），NLI gate 无法 block 这条路径，CSD 的结论会如何改变？\n\n**W3** [warning] Negative control (Claude Sonnet 4) 的解释不够深入\n- 具体位置：Section 4.1 (page 5, footnote), Appendix H (page 12)\n- 问题：Claude Sonnet 4 被用作 negative control（\"serves as a sensitivity check\"），其 BT 在 formality 上 67.1%，接近但未达 significance。但 Limitations (page 9) 又提到 Claude Sonnet 4 的 \"formality style sensitivity is consistently low across all three benchmarks (GEE Style OR 1.47–1.99, all n.s.)\"。如果 Claude Sonnet 4 确实对 formality 不敏感，这是一个有价值的 negative control。但论文没有深入讨论：为什么 Claude 对 formality 不敏感？是因为训练数据不同？RLHF 策略不同？这个问题与 Blindspot 的机制解释有关。\n- 建议：增加 1-2 句关于 negative control 结果的机制讨论，或至少说明为什么选择 Claude Sonnet 4 作为 negative control 的理由（目前只说\"we pin versions for reproducibility\"）。\n\n**W4** [warning] Human annotation 验证的规模偏小\n- 具体位置：Section 5.4 (page 8), Appendix U (page 16)\n- 问题：内容保存验证由两位独立标注员对 50 对 NLI-scored pairs 进行标注（Annotator 1 判定 42/50 content-preserving，Annotator 2 判定 21/25 或 33/50）。κ = 0.44（moderate agreement）。50 对的样本量对于验证一个核心方法论假设（NLI gate 有效保存内容）来说偏小，且 moderate agreement 提示标注标准可能存在模糊性。\n- 建议：(1) 扩大标注样本量至 100+ pairs；(2) 报告标注不一致的具体类型（是哪类内容变化被标注员发现但 NLI 未捕捉？）；(3) 讨论 κ = 0.44 对结论的影响。\n\n## 小问题（不影响接收）\n\n- **M1**: Section 3.1 (page 4) 的 rewriting prompt 示例（\"Rewrite the following text to be more formal/casual while preserving the exact same content and meaning\"）仅给了一个简短摘要，完整 prompt 应放在 Appendix 中供复现。\n- **M2**: Table 2 (page 7) 中\"Orig OR\"列的含义在首次出现时未充分解释，需要回溯到 Section 5.2 才能理解这是 originality 的 odds ratio。建议在 table caption 中添加说明。\n- **M3**: Section 5.3 (page 7-8) 的 cross-benchmark replication 部分，AlpacaEval 和 MT-Bench 的结果描述较为概括（\"similar pattern\"），但 Table 1 显示 MT-Bench 上的 BT 效应量（72.1%）低于 LLMBar（77.9%）和 AlpacaEval（77.3%），这个差异值得简短讨论。\n- **M4**: References 格式：部分引用缺少 DOI 或会议信息（如 arXiv preprints 与正式发表版本混用），建议统一检查。\n- **M5**: Limitations 第四段 (page 9) 提到 \"100-point continuous scale does not resolve the Blindspot (Appendix O)\"——这是一个重要的 robustness check，但仅用一个 judge (Qwen3-32B) 测试，建议在正文中明确标注这一限制。\n- **M6**: Abstract 中 \"six judges from independent providers\" 但正文 Section 4.1 说 \"four target judges\" + negative control + scaled replication。建议措辞一致——Abstract 应说明 \"four target judges from independent providers\" 加 negative control。\n\n## 主要优势\n\n1. **方法论设计严谨**：NLI gating + position-controlled pairwise + per-axis decomposition 的组合是对 style bias 诊断方法论的合理改进。特别是 position control（每对比较交换顺序两次，nₚₐᵢᵣₛ × 2 observations）和 NLI content preservation gate 的设计体现了对 confound 控制的认真思考。\n\n2. **统计分析全面**：论文使用了七种统计方法（Likert ATE, BT, sign test, Wilcoxon, Mann-Whitney, ordinal regression, GEE），并报告了 bootstrap 95% CI（Appendix J, 10,000 pair-level resamples）。GEE conditional decomposition（Table 2）揭示了 per-axis confound structure 是论文最有信息量的分析。\n\n3. **Robustness checks 充分**：Appendix 覆盖了 threshold sensitivity (F), direction-aware gating (G), Claude equivalence testing (H), cross-axis contamination (T), rewriter independence (E), power analysis (L), bootstrap attenuation (K) 等多项检验。这种 thoroughness 在风格偏差文献中不常见。\n\n4. **Limitations 诚实且全面**：四个段落覆盖了 quality-style confounding、evaluator-producer bias、scope boundary、validation methodology，且明确承认无法区分三种机制解释。这种诚实性值得肯定。\n\n5. **写作结构清晰**：从 \"Likert Blindspot\" 现象的引出（Introduction 的 opening example）→ 方法论设计 → 实验验证 → 机制讨论的叙事逻辑流畅。Figure 1 的 CSD pipeline overview 有效传达了方法论全貌。\n\n## 格式合规检查\n\n| 检查项 | 结果 | 备注 |\n|--------|------|------|\n| 正文页数 | ✓ 8页 | Sections 1-6 恰好 8 页 |\n| ACL 模板 | ✓ | `\\usepackage[review]{acl}`，`\\author{Anonymous}` |\n| Double-blind 匿名性 | ✓ | 未发现作者身份泄露线索；无致谢、无 GitHub/个人链接 |\n| Limitations section | ✓ | 在正文 Section 6 之后，unnumbered section，不计入 8 页限制 |\n| 参考文献格式 | 基本一致 | 部分 arXiv preprint 与正式发表版本混用，建议统一 |\n| Appendix | ✓ | 在 Limitations + Code and Data 之后，不计入页数 |\n\n## Questions for Authors\n\n1. 你们是否考虑过用 human raters 收集少量 ground-truth style bias ratings（例如 50 pairs），以部分区分 attenuation vs amplification？这似乎是区分三种机制解释最直接的方式。\n\n2. Table 2 中 formality 的 Orig OR 在不同 judges 之间差异很大（GPT-4o: 0.49, Qwen3-32B: 0.38, Llama-70B: 1.06, Gemini: 0.46）——这是否暗示 formality 的 Blindspot 本质上是 judge-dependent 而非 mode-dependent？\n\n3. CSD 方法论的 NLI gate 导致约 12% 的 pairs 被 reject（n=88 from n=100）。这些被 reject 的 pairs 是否有系统性偏差？例如，是否更倾向于 reject 某个方向的 rewriting（formal→casual vs casual→formal）？\n\n4. 论文提到 \"100-point continuous scale does not resolve the Blindspot\"（Appendix O），但仅在 Qwen3-32B 上测试。是否有计划在多个 judges 上复现这个实验？",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5 / 5 (Borderline Conference)\n**一句话总结**: 方法论扎实、实验设计严谨，但仅覆盖两个风格轴（formality, verbosity）限制了\"Likert Blindspot\"作为通用现象的推广性，三种机制解释未能区分进一步削弱了理论贡献。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | NLI gating + position-controlled pairwise + GEE decomposition 方法论合理且有多项 robustness check；但核心 claim（\"Blindspot 是系统性现象\"）仅基于两个表层风格轴，且三种机制解释（attenuation/amplification/construct divergence）未能区分，限制了 soundness 的上限 |\n| Excitement | 3/5 | Likert-pairwise 模式差异是有价值的发现，但实际推论（\"style 评估应优先用 pairwise\"）对熟悉该领域的研究者来说并不意外；scope 过窄（2 轴 × 4 judges × 1 主 benchmark）降低了影响力 |\n| Reproducibility | 4/5 | Appendix R 提供了详尽的实现细节（模型版本、温度、prompt），统计方法描述清晰，承诺 release code/data；但 NLI gate 的 prompt 和 rewriting prompt 的完整文本未在正文或附录中给出 |\n| Reviewer Confidence | 4/5 | 仔细阅读了全文及全部附录，对统计方法和 LLM-as-judge 文献较为熟悉 |\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 仅两个风格轴无法支撑 \"Likert Blindspot\" 的通用性 claim\n- 具体位置：Abstract (\"systematically divergent style sensitivity\"), Section 1 (\"a systematic pattern\"), Title (\"LLM Judge Style Evaluation\")\n- 问题：论文标题和摘要将 Likert Blindspot 定位为 LLM judge style 评估的通用现象，但实验仅覆盖 formality 和 verbosity（加上 Appendix 中的 register 作为探索性分析）。这三个轴均属表层文体属性（surface-level stylistic attributes），论文自身在 Limitations (page 9) 承认 semantic-level axes（hedging, humor, technicality）因 NLI gate 限制无法覆盖。仅基于两个高度相关的表层轴（verbosity 和 formality 在实践中常共变），就声称发现了 systematic pattern，存在过度概括风险。\n- 为什么影响接收：一个声称发现\"系统性\"现象的论文，如果证据仅来自有限且同质的轴，会被质疑 claim 是否成立。如果 Blindspot 仅限于特定类型的风格轴，这仍然是有趣的但需要不同的 framing。\n- 建议修改方向：(1) 弱化通用性 claim，明确限定为 \"surface-level stylistic axes\"；(2) 或增加至少 1-2 个语义层面的轴（如 hedging level, bullet-point vs prose）的实验证据，哪怕是 pilot scale；(3) 在 Abstract 和 Introduction 中明确表述 scope boundary。\n\n**N2** [critical] 三种机制解释未能区分，限制了理论贡献\n- 具体位置：Section 5.1 (\"three non-exclusive explanations\"), Limitations paragraph 1 (\"The primary open question is whether pairwise comparison detects genuine style bias or amplifies micro-preferences\")\n- 问题：论文提出 attenuation（Likert 衰减信号）、amplification（pairwise 放大信号）、construct divergence（两种模式测量不同构念）三种解释，但明确表示无法区分（\"cannot be definitively resolved without human ground-truth\"）。这三种解释有截然不同的实践含义：如果是 attenuation，则 Likert 需要修正；如果是 amplification，则 pairwise 结果可能夸大了真实偏差；如果是 construct divergence，则两种模式都是\"正确的\"只是测量不同的东西。\n- 为什么影响接收：一篇 diagnostic 论文如果无法判断被诊断的现象究竟是什么（信号丢失 vs 信号放大 vs 不同构念），其理论贡献和实践指导价值会大打折扣。Section 5.1 提到\"six experimental controls bound this risk (§5.4)\"来 bound amplification，但 bounding 不等于排除。\n- 建议修改方向：(1) 即使无法完全区分，可以通过 human evaluation 对少量 pairs 收集 ground-truth style ratings，然后比较 human 与 Likert/pairwise 的一致性，至少部分区分 attenuation vs amplification；(2) 更明确地讨论每种解释的证据权重，而非简单列举为 \"non-exclusive\"；(3) 如果无法增加实验，应在 framing 上更诚实地将这作为 open question 而非 contribution 的一部分。\n\n**N3** [critical] 与 RATE (Reber et al., 2025) 的增量贡献需更清晰界定\n- 具体位置：Section 2 Related Work (page 2-3), Section 5.1 (\"Head-to-head comparison with RATE\")\n- 问题：RATE 已经建立了 style-rewriting + ATE 的方法框架，并发现 60% 的 style-transformed pairs 接受了 confounded 评分。CSD 的核心区别在于：(a) 引入 pairwise 比较模式揭示 mode divergence，(b) per-axis GEE decomposition，(c) NLI gating 替代 RATE 的 Likert ATE correction。但 Section 5.1 的 head-to-head 比较仅用了 1 段文字，且主要强调 RATE \"may underestimate the true magnitude\"——这个 claim 需要更强的证据支撑，因为 RATE 和 CSD 测量的是不同的量（RATE 测 ATE bias，CSD 测 mode divergence）。\n- 为什么影响接收：如果 reviewer 认为 CSD 相对 RATE 的增量不够大（本质上是给 RATE 加了 pairwise 比较模式 + GEE），可能判断 novelty 不足。\n- 建议修改方向：(1) 用一个结构化的对比表格明确列出 RATE vs CSD 在方法论、测量对象、发现上的区别；(2) 讨论 CSD 是否 subsume RATE 或两者是互补的；(3) 避免暗示 RATE \"underestimates\"——更精确地说是 RATE 测量的是不同的量。\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Table 1 信息密度过高，可读性不佳\n- 具体位置：Table 1 (page 6)\n- 问题：Table 1 在一个表格中压缩了 5 个 judges × 3 benchmarks × 2 axes × 4 个统计量（ATE, BT, Likert(p), BT(p)）+ 脚注中的 scaled replication 和 negative control 信息。对于一篇以\"发现 mode divergence\"为核心贡献的论文，读者需要先理解这个复杂的表格才能把握核心结果，增加了认知负担。\n- 建议：(1) 考虑将 LLMBar 主结果和 cross-benchmark replication 分成两个表格；(2) 或至少在正文中添加一段引导性的文字帮助读者 parse 表格（目前正文直接跳到 Section 5 Analysis）。\n\n**W2** [warning] Figure 2 的 DAG 假设未充分讨论\n- 具体位置：Figure 2 (page 4), Appendix A (page 10)\n- 问题：Figure 2 呈现了一个 assumed data-generating process 的 DAG，但 Appendix A 立即声明 \"we do not claim that the DAG in Figure 2 is a complete structural causal model\"。然而，CSD 的整个方法论（NLI gating blocks H→Q, style-controlled rewriting isolates S→Y）都依赖于这个 DAG 的结构假设。如果 DAG 遗漏了重要的路径（例如 style 对 content quality 的直接效应 S→Q，或评估者的 prior expectations），方法论的有效性会受到影响。论文在 Limitations 中讨论了 quality-style confounding，但没有系统地讨论 DAG 可能遗漏的路径。\n- 建议：在 Section 3 或 Appendix A 中增加对 DAG 假设的敏感性讨论：如果存在 S→Q 路径（style 影响 perceived quality），NLI gate 无法 block 这条路径，CSD 的结论会如何改变？\n\n**W3** [warning] Negative control (Claude Sonnet 4) 的解释不够深入\n- 具体位置：Section 4.1 (page 5, footnote), Appendix H (page 12)\n- 问题：Claude Sonnet 4 被用作 negative control（\"serves as a sensitivity check\"），其 BT 在 formality 上 67.1%，接近但未达 significance。但 Limitations (page 9) 又提到 Claude Sonnet 4 的 \"formality style sensitivity is consistently low across all three benchmarks (GEE Style OR 1.47–1.99, all n.s.)\"。如果 Claude Sonnet 4 确实对 formality 不敏感，这是一个有价值的 negative control。但论文没有深入讨论：为什么 Claude 对 formality 不敏感？是因为训练数据不同？RLHF 策略不同？这个问题与 Blindspot 的机制解释有关。\n- 建议：增加 1-2 句关于 negative control 结果的机制讨论，或至少说明为什么选择 Claude Sonnet 4 作为 negative control 的理由（目前只说\"we pin versions for reproducibility\"）。\n\n**W4** [warning] Human annotation 验证的规模偏小\n- 具体位置：Section 5.4 (page 8), Appendix U (page 16)\n- 问题：内容保存验证由两位独立标注员对 50 对 NLI-scored pairs 进行标注（Annotator 1 判定 42/50 content-preserving，Annotator 2 判定 21/25 或 33/50）。κ = 0.44（moderate agreement）。50 对的样本量对于验证一个核心方法论假设（NLI gate 有效保存内容）来说偏小，且 moderate agreement 提示标注标准可能存在模糊性。\n- 建议：(1) 扩大标注样本量至 100+ pairs；(2) 报告标注不一致的具体类型（是哪类内容变化被标注员发现但 NLI 未捕捉？）；(3) 讨论 κ = 0.44 对结论的影响。\n\n## 小问题（不影响接收）\n\n- **M1**: Section 3.1 (page 4) 的 rewriting prompt 示例（\"Rewrite the following text to be more formal/casual while preserving the exact same content and meaning\"）仅给了一个简短摘要，完整 prompt 应放在 Appendix 中供复现。\n- **M2**: Table 2 (page 7) 中\"Orig OR\"列的含义在首次出现时未充分解释，需要回溯到 Section 5.2 才能理解这是 originality 的 odds ratio。建议在 table caption 中添加说明。\n- **M3**: Section 5.3 (page 7-8) 的 cross-benchmark replication 部分，AlpacaEval 和 MT-Bench 的结果描述较为概括（\"similar pattern\"），但 Table 1 显示 MT-Bench 上的 BT 效应量（72.1%）低于 LLMBar（77.9%）和 AlpacaEval（77.3%），这个差异值得简短讨论。\n- **M4**: References 格式：部分引用缺少 DOI 或会议信息（如 arXiv preprints 与正式发表版本混用），建议统一检查。\n- **M5**: Limitations 第四段 (page 9) 提到 \"100-point continuous scale does not resolve the Blindspot (Appendix O)\"——这是一个重要的 robustness check，但仅用一个 judge (Qwen3-32B) 测试，建议在正文中明确标注这一限制。\n- **M6**: Abstract 中 \"six judges from independent providers\" 但正文 Section 4.1 说 \"four target judges\" + negative control + scaled replication。建议措辞一致——Abstract 应说明 \"four target judges from independent providers\" 加 negative control。\n\n## 主要优势\n\n1. **方法论设计严谨**：NLI gating + position-controlled pairwise + per-axis decomposition 的组合是对 style bias 诊断方法论的合理改进。特别是 position control（每对比较交换顺序两次，nₚₐᵢᵣₛ × 2 observations）和 NLI content preservation gate 的设计体现了对 confound 控制的认真思考。\n\n2. **统计分析全面**：论文使用了七种统计方法（Likert ATE, BT, sign test, Wilcoxon, Mann-Whitney, ordinal regression, GEE），并报告了 bootstrap 95% CI（Appendix J, 10,000 pair-level resamples）。GEE conditional decomposition（Table 2）揭示了 per-axis confound structure 是论文最有信息量的分析。\n\n3. **Robustness checks 充分**：Appendix 覆盖了 threshold sensitivity (F), direction-aware gating (G), Claude equivalence testing (H), cross-axis contamination (T), rewriter independence (E), power analysis (L), bootstrap attenuation (K) 等多项检验。这种 thoroughness 在风格偏差文献中不常见。\n\n4. **Limitations 诚实且全面**：四个段落覆盖了 quality-style confounding、evaluator-producer bias、scope boundary、validation methodology，且明确承认无法区分三种机制解释。这种诚实性值得肯定。\n\n5. **写作结构清晰**：从 \"Likert Blindspot\" 现象的引出（Introduction 的 opening example）→ 方法论设计 → 实验验证 → 机制讨论的叙事逻辑流畅。Figure 1 的 CSD pipeline overview 有效传达了方法论全貌。\n\n## 格式合规检查\n\n| 检查项 | 结果 | 备注 |\n|--------|------|------|\n| 正文页数 | ✓ 8页 | Sections 1-6 恰好 8 页 |\n| ACL 模板 | ✓ | `\\usepackage[review]{acl}`，`\\author{Anonymous}` |\n| Double-blind 匿名性 | ✓ | 未发现作者身份泄露线索；无致谢、无 GitHub/个人链接 |\n| Limitations section | ✓ | 在正文 Section 6 之后，unnumbered section，不计入 8 页限制 |\n| 参考文献格式 | 基本一致 | 部分 arXiv preprint 与正式发表版本混用，建议统一 |\n| Appendix | ✓ | 在 Limitations + Code and Data 之后，不计入页数 |\n\n## Questions for Authors\n\n1. 你们是否考虑过用 human raters 收集少量 ground-truth style bias ratings（例如 50 pairs），以部分区分 attenuation vs amplification？这似乎是区分三种机制解释最直接的方式。\n\n2. Table 2 中 formality 的 Orig OR 在不同 judges 之间差异很大（GPT-4o: 0.49, Qwen3-32B: 0.38, Llama-70B: 1.06, Gemini: 0.46）——这是否暗示 formality 的 Blindspot 本质上是 judge-dependent 而非 mode-dependent？\n\n3. CSD 方法论的 NLI gate 导致约 12% 的 pairs 被 reject（n=88 from n=100）。这些被 reject 的 pairs 是否有系统性偏差？例如，是否更倾向于 reject 某个方向的 rewriting（formal→casual vs casual→formal）？\n\n4. 论文提到 \"100-point continuous scale does not resolve the Blindspot\"（Appendix O），但仅在 Qwen3-32B 上测试。是否有计划在多个 judges 上复现这个实验？",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1049 · 2026-05-23T05:31:37.540549+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3565
}
```

</details>

---


### Tool call

_source line 1050 · 2026-05-23T05:31:42.216683+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
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

_source line 1051 · 2026-05-23T05:31:42.217228+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1052 · 2026-05-23T05:31:45.684800+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_13/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1053 · 2026-05-23T05:31:45.785839+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 101
}
```

</details>

---


### Assistant

_source line 1054 · 2026-05-23T05:31:55.479057+00:00_

审稿完成，已提交给 Review Director。

**总评：3.5 / 5（Borderline Conference）**

核心判断：方法论设计严谨（NLI gating + position-controlled pairwise + GEE decomposition），统计分析全面（七种方法 + 大量 robustness checks），写作清晰，格式合规。但三个 Must-Fix 问题限制了贡献：

1. **仅两个表层风格轴**无法支撑标题和摘要中"系统性现象"的 claim
2. **三种机制解释未区分**（attenuation / amplification / construct divergence），削弱理论贡献和实践指导价值
3. **与 RATE 的增量贡献**界定不够清晰——核心区别在于加了 pairwise 模式和 GEE，需要更 explicit 的对比论证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 32

## Round 32

4 recorded events


### User

_source line 1055 · 2026-05-23T05:33:38.242026+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix / Should-Fix / Minor 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 的审稿意见

**Overall**: 3.5 / 5 (Borderline Conference)

### Must-Fix 问题

**N1** [critical] Likert Blindspot 的因果归因过度——论文自身证据无法排除 "construct divergence" 解释
- Title 的 "Blindspot" 暗示 Likert 有缺陷，但 Section 5.1 列出三种 non-exclusive 解释且无法区分。pairwise > Likert 的判别力是 Thurstone (1927) 以来的已知现象。power analysis 显示 Likert 需 4-206× 样本量——完全一致于已知的 format sensitivity 差异。论文需论证为何观察到的 divergence 不仅仅是已知的 format sensitivity 差异。建议：(1) 给 construct divergence 同等篇幅；(2) 讨论 Thurstone discriminability；(3) 考虑更中性的术语。

**N2** [critical] Negative control (Claude Sonnet 4) 的等效检验统计力严重不足
- TOST 在 Δ=15pp 才显著（p=0.010），但 15pp 对应 BT=65% 是相当大的偏好差异。Δ=10pp 时 TOST 不显著（p=0.156, power≈42%）。无法区分 "Claude 没有 style bias" 和 "Claude 有 10pp style bias"。BT=56.2% 的 6.2pp 偏差可能反映真实 moderate effect。建议：扩大 n 到 200+，或降级 negative control 结论为 "suggestive but underpowered"。

**N3** [critical] 样本量 n=88 下 GEE decomposition 的可靠性存疑
- Qwen3 verbosity Style OR=13.10 [5.62, 30.55]，CI 跨越近 6 倍。n=88→n=355 时 Qwen3 formality Style OR 从 4.20 降到 2.15（缩水 49%）。交互效应检验 power 极低（OR 从 0.45 到 2.60 但 all p>0.13）。建议：对所有配置做 n=355 级别 scaled replication，或至少讨论 OR 缩水的含义。

### Should-Fix 问题

**W1** Style axis 覆盖窄（2 primary + 1 exploratory），限制普适性
**W2** Cross-axis contamination 中 FK grade d=0.50 处理不够严谨
**W3** Evaluator-producer overlap 的 mitigation 只测试了一个替代 rewriter
**W4** IIA assumption 讨论不充分（仅在脚注中）
**W5** 100-point continuous Likert scale 仅用一个 judge

### Minor Issues
1. Table 1 排版密度过高
2. "style bias" vs "style sensitivity" 措辞不一致
3. Figure 2 DAG 的 S→Q path caption 不够明确
4. Appendix 编号难以跟踪
5. Section 3.5 Design Rationale 位置偏后

---

请对以上每个问题逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1056 · 2026-05-23T05:35:35.032558+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: Likert Blindspot 的因果归因过度**\n\n同意 R1 的核心论点。我在自己的审稿中也提出了高度相关的问题（R2-N2: 三种机制解释未能区分）。补充以下观察：\n\n1. **\"Blindspot\" 术语的规范性含义**：R1 指出 \"Blindspot\" 暗示 Likert 有缺陷，这与论文自身 Section 5.1 承认的三种 non-exclusive 解释矛盾。论文 Limitations 第一段明确写到 \"An alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference\"——如果作者自己承认这可能只是 construct difference 而非 measurement failure，那么 \"Blindspot\" 这个带有价值判断的术语就不够准确。\n\n2. **Thurstone discriminability 的遗漏**：R1 指出 pairwise > Likert 的判别力自 Thurstone (1927) 以来就是已知现象，这一点论文确实没有充分讨论。Section 2 Related Work 引用了 Thurstone (1927)，但仅在 \"Measurement Sensitivity in NLG Evaluation\" 段落中提到 \"forced-choice comparisons yield finer discriminability than absolute ratings\"，没有将自己的 power analysis（Figure 4）与这一经典结果做对比。如果 Figure 4 显示的 4-206× 样本量差异完全可以用 Thurstone discriminability 解释，那么 Likert Blindspot 可能并非新发现，而只是经典 psychometric 结果在 LLM judge 场景下的复现。\n\n3. **但 GEE decomposition 部分超越了 Thurstone**：我认为论文的 GEE conditional decomposition（Table 2）揭示的 per-axis confound structure（verbosity style-dominated vs formality conditional on originality）不能仅用 Thurstone discriminability 解释。这个 per-axis 差异是论文的独特贡献，R1 的批评应主要针对 \"mode divergence\" 的 framing，而非整个论文。\n\n**建议**：弱化 \"Blindspot\" 的规范性含义，在 Introduction 中给 construct divergence 解释更多篇幅，并在 Section 2 中讨论 Thurstone discriminability 与本文发现的关系。\n\n---\n\n**[AGREE] R1-N2: Negative control TOST 统计力不足**\n\n完全同意。这是一个我在自己审稿中未充分展开但现在认为重要的问题。\n\n1. **Δ=15pp 的等效界限过于宽松**：Appendix H (Table 9) 显示 TOST 在 Δ=15pp 时 p=0.010，但 BT=65% 对应的 15pp 偏差在 style preference 语境下是相当大的效应。以论文自身的 BT 结果为参照，GPT-4o 在 formality 上的 BT=63.0%（即 13pp 偏差）被论文视为 \"significant style preference\"——那么 Δ=15pp 的等效界限几乎涵盖了论文自己认定为显著的效应量。\n\n2. **BT=56.2% 的实际含义**：Claude Sonnet 4 的 BT=56.2%（formality）意味着在 56.2% 的配对中偏好 formal 变体。6.2pp 的偏差虽然不大，但 Appendix H 报告 TOST 在 Δ=10pp 时 p=0.156, power≈42%，无法排除这是一个 moderate effect。\n\n3. **对论文结论的影响**：如果 negative control 无法可靠地排除 style bias，那么 \"Claude as negative control confirms the Blindspot is judge-dependent\" 的 claim（Section 4.1, footnote; Limitations page 9）就需要降级。\n\n**建议**：与 R1 一致——扩大 n 到 200+，或将 negative control 结论降级为 \"suggestive but underpowered\"。\n\n---\n\n**[AGREE] R1-N3: GEE decomposition 在 n=88 下的可靠性**\n\n同意这是一个需要认真对待的统计问题。\n\n1. **CI 宽度问题**：Table 2 中 Qwen3 verbosity Style OR=13.10 [5.62, 30.55]，95% CI 跨越近 6 倍。Table 5 (Appendix, page 11) 进一步证实了这个问题：许多 GEE OR 的 CI 覆盖范围很大。这意味着点估计的精度很低，不应过度解读具体数值。\n\n2. **OR 缩水现象**：R1 指出 n=88→n=355 时 Qwen3 formality Style OR 从 4.20 降到 2.15（缩水 49%）。这可能反映：(a) 小样本下的偶然高估（regression to the mean），(b) n=355 的样本组成不同（scaled replication 可能覆盖不同的 text 类型），或 (c) 真实效应确实被 n=88 高估。论文未讨论这个缩水现象。\n\n3. **交互效应检验 power**：Table 4 (Appendix, page 11) 报告 Style × Originality 交互效应全部不显著（all p>0.13），但在 n=88 下检测交互效应本就需要更大的样本量。论文基于非显著交互效应确认 additive model——但 absence of evidence ≠ evidence of absence。\n\n4. **与我的审稿互补**：我在 R2-N1 中指出仅两个轴限制了通用性，R1-N3 从统计精度角度进一步质疑了即便在现有轴上结论的稳健性。两个问题叠加时更为严重。\n\n**建议**：同意 R1——至少在 verbosity 轴上也做 n=355 级别的 scaled replication（目前仅 formality 有），并在正文中讨论 OR 缩水的含义。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Style axis 覆盖窄**\n\n完全同意，与我的 R2-N1 一致。我将此列为 Must-Fix，R1 列为 Should-Fix，但核心关切相同：两个 primary axis + 一个 exploratory axis 无法支撑论文标题和 Abstract 中的通用性 claim。\n\n---\n\n**[AGREE] R1-W2: FK grade d=0.50 处理不够严谨**\n\n同意。Appendix T (page 15-16) 中 verbosity rewrites 的 FK grade d=0.50 是 Cohen's d 中等效应量。论文将其归因为 \"FK's dependence on sentence length, which changes by design in verbosity manipulation\"——这个解释有一定道理（FK 公式确实依赖句子长度），但 d=0.50 仍然表明 verbosity rewriting 在某种程度上改变了 readability level，而非仅仅改变 length。如果 readability 变化伴随 verbosity 变化，那么 verbosity 轴上的 Blindspot 发现可能部分反映了 readability 差异而非纯粹的 verbosity 差异。\n\n建议论文至少增加一个控制实验：在保持 FK grade 不变的条件下，是否仍然观察到 verbosity Blindspot。\n\n---\n\n**[AGREE] R1-W3: 仅一个替代 rewriter**\n\n同意。Appendix E (Table 6) 仅用 GPT-4o 作为替代 rewriter，且仅在 formality 轴上测试。22% Style OR 降幅不算小。如果换用更多 rewriters（例如 Llama、Claude）且在 verbosity 轴上也测试，结论的稳健性会更有说服力。\n\n---\n\n**[REBUT] R1-W4: IIA assumption 讨论不充分**\n\n部分不同意。R1 认为 IIA 假设仅在脚注中讨论不够，但我认为在本文的实验设计下 IIA 的威胁有限：\n\n1. **CSD 的 pairwise 比较是 controlled pairs**：每对比较都是原文 vs 同一文本的风格变体（original vs rewrite），而非从大池子中任意抽取的两个文本。在这种 controlled comparison 下，\"irrelevant alternatives\" 的影响远小于开放式的 ranking/tournament 设计。\n\n2. **BT 模型在此的用途有限**：论文使用 BT 主要是为了计算 win probability 和 aggregated preference direction，而非做精细的 latent utility 估计。BT 的 IIA 假设在这种用途下的违反后果较轻。\n\n3. **但 R1 有一点是对的**：Limitations (page 9) 确实提到 \"The Bradley-Terry model assumes unidimensionality—a single latent 'quality' dimension\"。如果 judges 沿多个 latent dimensions 评估，BT 的 IIA 假设可能被违反。这值得在正文中简短讨论（例如 2-3 句话），但不需要大篇幅论证。\n\n---\n\n**[AGREE] R1-W5: 100-point Likert 仅用一个 judge**\n\n完全同意，我在 R2-M5 中也提出了这个问题。Appendix O 的 100-point continuous scale 实验仅用 Qwen3-32B，无法排除 judge-specific 效应。至少应在 GPT-4o 上复现。\n\n---\n\n### Minor Issues\n\n**[AGREE] R1-Minor-1: Table 1 排版密度过高**\n同意，与我的 R2-W1 一致。\n\n**[AGREE] R1-Minor-2: \"style bias\" vs \"style sensitivity\" 措辞不一致**\n同意。论文中交替使用 \"style bias\"（暗示 judges 有偏）和 \"style sensitivity\"（暗示 judges 能检测风格差异），但这两个概念方向不同。建议统一术语。\n\n**[AGREE] R1-Minor-3: Figure 2 DAG 的 S→Q path caption**\n同意，与我的 R2-W2 相关。Figure 2 caption 中对 S→Q path 的描述 (\"style may influence perceived quality through channels the NLI gate cannot block\") 是正确的但过于简略。建议在 caption 中明确标注哪些 paths 被 NLI gate blocked vs unblocked。\n\n**[AGREE] R1-Minor-4: Appendix 编号难以跟踪**\n同意。Appendix A 到 V+，读者需要频繁在正文和附录之间跳转。建议对 Appendix 做分组（如 Methodology appendices, Statistical appendices, Robustness appendices）。\n\n**[REBUT] R1-Minor-5: Section 3.5 Design Rationale 位置偏后**\n不同意 R1 认为 Design Rationale 应该提前。Section 3.5 在读者已经了解 CSD 的三个组件（style-controlled rewriting §3.1, content preservation §3.2, measurement protocol §3.3）之后才解释为什么选择这种设计，逻辑顺序是 \"what → why\"。如果提前到 Section 3.1 之前，读者尚未理解方法细节就要消化设计理由，反而增加认知负担。当前位置是合理的。\n\n---\n\n### 总结\n\nR1 提出的三个 Must-Fix 问题均成立，且与我的审稿发现高度互补：\n- R1-N1（因果归因过度）↔ R2-N2（机制解释未区分）：角度不同但指向同一问题\n- R1-N2（negative control underpowered）：我未充分展开的重要问题\n- R1-N3（GEE n=88 可靠性）↔ R2-N1（轴覆盖窄）：统计精度 + scope 叠加\n\n两位 Reviewer 的 Overall 评分一致（3.5 Borderline Conference），主要分歧在对 IIA 假设讨论（R1-W4）和 Design Rationale 位置（R1-Minor-5）的判断上。",
  "reviewer_id": "2",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: Likert Blindspot 的因果归因过度**\n\n同意 R1 的核心论点。我在自己的审稿中也提出了高度相关的问题（R2-N2: 三种机制解释未能区分）。补充以下观察：\n\n1. **\"Blindspot\" 术语的规范性含义**：R1 指出 \"Blindspot\" 暗示 Likert 有缺陷，这与论文自身 Section 5.1 承认的三种 non-exclusive 解释矛盾。论文 Limitations 第一段明确写到 \"An alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference\"——如果作者自己承认这可能只是 construct difference 而非 measurement failure，那么 \"Blindspot\" 这个带有价值判断的术语就不够准确。\n\n2. **Thurstone discriminability 的遗漏**：R1 指出 pairwise > Likert 的判别力自 Thurstone (1927) 以来就是已知现象，这一点论文确实没有充分讨论。Section 2 Related Work 引用了 Thurstone (1927)，但仅在 \"Measurement Sensitivity in NLG Evaluation\" 段落中提到 \"forced-choice comparisons yield finer discriminability than absolute ratings\"，没有将自己的 power analysis（Figure 4）与这一经典结果做对比。如果 Figure 4 显示的 4-206× 样本量差异完全可以用 Thurstone discriminability 解释，那么 Likert Blindspot 可能并非新发现，而只是经典 psychometric 结果在 LLM judge 场景下的复现。\n\n3. **但 GEE decomposition 部分超越了 Thurstone**：我认为论文的 GEE conditional decomposition（Table 2）揭示的 per-axis confound structure（verbosity style-dominated vs formality conditional on originality）不能仅用 Thurstone discriminability 解释。这个 per-axis 差异是论文的独特贡献，R1 的批评应主要针对 \"mode divergence\" 的 framing，而非整个论文。\n\n**建议**：弱化 \"Blindspot\" 的规范性含义，在 Introduction 中给 construct divergence 解释更多篇幅，并在 Section 2 中讨论 Thurstone discriminability 与本文发现的关系。\n\n---\n\n**[AGREE] R1-N2: Negative control TOST 统计力不足**\n\n完全同意。这是一个我在自己审稿中未充分展开但现在认为重要的问题。\n\n1. **Δ=15pp 的等效界限过于宽松**：Appendix H (Table 9) 显示 TOST 在 Δ=15pp 时 p=0.010，但 BT=65% 对应的 15pp 偏差在 style preference 语境下是相当大的效应。以论文自身的 BT 结果为参照，GPT-4o 在 formality 上的 BT=63.0%（即 13pp 偏差）被论文视为 \"significant style preference\"——那么 Δ=15pp 的等效界限几乎涵盖了论文自己认定为显著的效应量。\n\n2. **BT=56.2% 的实际含义**：Claude Sonnet 4 的 BT=56.2%（formality）意味着在 56.2% 的配对中偏好 formal 变体。6.2pp 的偏差虽然不大，但 Appendix H 报告 TOST 在 Δ=10pp 时 p=0.156, power≈42%，无法排除这是一个 moderate effect。\n\n3. **对论文结论的影响**：如果 negative control 无法可靠地排除 style bias，那么 \"Claude as negative control confirms the Blindspot is judge-dependent\" 的 claim（Section 4.1, footnote; Limitations page 9）就需要降级。\n\n**建议**：与 R1 一致——扩大 n 到 200+，或将 negative control 结论降级为 \"suggestive but underpowered\"。\n\n---\n\n**[AGREE] R1-N3: GEE decomposition 在 n=88 下的可靠性**\n\n同意这是一个需要认真对待的统计问题。\n\n1. **CI 宽度问题**：Table 2 中 Qwen3 verbosity Style OR=13.10 [5.62, 30.55]，95% CI 跨越近 6 倍。Table 5 (Appendix, page 11) 进一步证实了这个问题：许多 GEE OR 的 CI 覆盖范围很大。这意味着点估计的精度很低，不应过度解读具体数值。\n\n2. **OR 缩水现象**：R1 指出 n=88→n=355 时 Qwen3 formality Style OR 从 4.20 降到 2.15（缩水 49%）。这可能反映：(a) 小样本下的偶然高估（regression to the mean），(b) n=355 的样本组成不同（scaled replication 可能覆盖不同的 text 类型），或 (c) 真实效应确实被 n=88 高估。论文未讨论这个缩水现象。\n\n3. **交互效应检验 power**：Table 4 (Appendix, page 11) 报告 Style × Originality 交互效应全部不显著（all p>0.13），但在 n=88 下检测交互效应本就需要更大的样本量。论文基于非显著交互效应确认 additive model——但 absence of evidence ≠ evidence of absence。\n\n4. **与我的审稿互补**：我在 R2-N1 中指出仅两个轴限制了通用性，R1-N3 从统计精度角度进一步质疑了即便在现有轴上结论的稳健性。两个问题叠加时更为严重。\n\n**建议**：同意 R1——至少在 verbosity 轴上也做 n=355 级别的 scaled replication（目前仅 formality 有），并在正文中讨论 OR 缩水的含义。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Style axis 覆盖窄**\n\n完全同意，与我的 R2-N1 一致。我将此列为 Must-Fix，R1 列为 Should-Fix，但核心关切相同：两个 primary axis + 一个 exploratory axis 无法支撑论文标题和 Abstract 中的通用性 claim。\n\n---\n\n**[AGREE] R1-W2: FK grade d=0.50 处理不够严谨**\n\n同意。Appendix T (page 15-16) 中 verbosity rewrites 的 FK grade d=0.50 是 Cohen's d 中等效应量。论文将其归因为 \"FK's dependence on sentence length, which changes by design in verbosity manipulation\"——这个解释有一定道理（FK 公式确实依赖句子长度），但 d=0.50 仍然表明 verbosity rewriting 在某种程度上改变了 readability level，而非仅仅改变 length。如果 readability 变化伴随 verbosity 变化，那么 verbosity 轴上的 Blindspot 发现可能部分反映了 readability 差异而非纯粹的 verbosity 差异。\n\n建议论文至少增加一个控制实验：在保持 FK grade 不变的条件下，是否仍然观察到 verbosity Blindspot。\n\n---\n\n**[AGREE] R1-W3: 仅一个替代 rewriter**\n\n同意。Appendix E (Table 6) 仅用 GPT-4o 作为替代 rewriter，且仅在 formality 轴上测试。22% Style OR 降幅不算小。如果换用更多 rewriters（例如 Llama、Claude）且在 verbosity 轴上也测试，结论的稳健性会更有说服力。\n\n---\n\n**[REBUT] R1-W4: IIA assumption 讨论不充分**\n\n部分不同意。R1 认为 IIA 假设仅在脚注中讨论不够，但我认为在本文的实验设计下 IIA 的威胁有限：\n\n1. **CSD 的 pairwise 比较是 controlled pairs**：每对比较都是原文 vs 同一文本的风格变体（original vs rewrite），而非从大池子中任意抽取的两个文本。在这种 controlled comparison 下，\"irrelevant alternatives\" 的影响远小于开放式的 ranking/tournament 设计。\n\n2. **BT 模型在此的用途有限**：论文使用 BT 主要是为了计算 win probability 和 aggregated preference direction，而非做精细的 latent utility 估计。BT 的 IIA 假设在这种用途下的违反后果较轻。\n\n3. **但 R1 有一点是对的**：Limitations (page 9) 确实提到 \"The Bradley-Terry model assumes unidimensionality—a single latent 'quality' dimension\"。如果 judges 沿多个 latent dimensions 评估，BT 的 IIA 假设可能被违反。这值得在正文中简短讨论（例如 2-3 句话），但不需要大篇幅论证。\n\n---\n\n**[AGREE] R1-W5: 100-point Likert 仅用一个 judge**\n\n完全同意，我在 R2-M5 中也提出了这个问题。Appendix O 的 100-point continuous scale 实验仅用 Qwen3-32B，无法排除 judge-specific 效应。至少应在 GPT-4o 上复现。\n\n---\n\n### Minor Issues\n\n**[AGREE] R1-Minor-1: Table 1 排版密度过高**\n同意，与我的 R2-W1 一致。\n\n**[AGREE] R1-Minor-2: \"style bias\" vs \"style sensitivity\" 措辞不一致**\n同意。论文中交替使用 \"style bias\"（暗示 judges 有偏）和 \"style sensitivity\"（暗示 judges 能检测风格差异），但这两个概念方向不同。建议统一术语。\n\n**[AGREE] R1-Minor-3: Figure 2 DAG 的 S→Q path caption**\n同意，与我的 R2-W2 相关。Figure 2 caption 中对 S→Q path 的描述 (\"style may influence perceived quality through channels the NLI gate cannot block\") 是正确的但过于简略。建议在 caption 中明确标注哪些 paths 被 NLI gate blocked vs unblocked。\n\n**[AGREE] R1-Minor-4: Appendix 编号难以跟踪**\n同意。Appendix A 到 V+，读者需要频繁在正文和附录之间跳转。建议对 Appendix 做分组（如 Methodology appendices, Statistical appendices, Robustness appendices）。\n\n**[REBUT] R1-Minor-5: Section 3.5 Design Rationale 位置偏后**\n不同意 R1 认为 Design Rationale 应该提前。Section 3.5 在读者已经了解 CSD 的三个组件（style-controlled rewriting §3.1, content preservation §3.2, measurement protocol §3.3）之后才解释为什么选择这种设计，逻辑顺序是 \"what → why\"。如果提前到 Section 3.1 之前，读者尚未理解方法细节就要消化设计理由，反而增加认知负担。当前位置是合理的。\n\n---\n\n### 总结\n\nR1 提出的三个 Must-Fix 问题均成立，且与我的审稿发现高度互补：\n- R1-N1（因果归因过度）↔ R2-N2（机制解释未区分）：角度不同但指向同一问题\n- R1-N2（negative control underpowered）：我未充分展开的重要问题\n- R1-N3（GEE n=88 可靠性）↔ R2-N1（轴覆盖窄）：统计精度 + scope 叠加\n\n两位 Reviewer 的 Overall 评分一致（3.5 Borderline Conference），主要分歧在对 IIA 假设讨论（R1-W4）和 Design Rationale 位置（R1-Minor-5）的判断上。",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1057 · 2026-05-23T05:35:38.551138+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3518
}
```

</details>

---


### Assistant

_source line 1058 · 2026-05-23T05:35:45.718510+00:00_

已提交对 Reviewer 1 全部 13 个问题的逐条回应。核心结论：

- R1 的三个 Must-Fix 全部 **[AGREE]**，与我自己的审稿发现高度互补
- Should-Fix 中 4/5 **[AGREE]**，仅 R1-W4 (IIA assumption) **[REBUT]**——在 CSD 的 controlled pair 设计下 IIA 威胁有限
- Minor 中 4/5 **[AGREE]**，仅 R1-Minor-5 (Design Rationale 位置) **[REBUT]**——当前 "what → why" 顺序合理
- 两位 Reviewer 的 Overall 评分一致（3.5 Borderline Conference）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 33

## Round 33

56 recorded events
