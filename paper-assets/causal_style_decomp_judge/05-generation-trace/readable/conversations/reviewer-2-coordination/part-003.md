# Reviewer 2 coordination — Part 3 of 3

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../reviewer-2-coordination.md) · [Structured JSON](../../../sessions/fe/fe1bbde7623f8449bd9a.json)

## Round 33

### User

_source line 1059 · 2026-05-23T06:42:03.052899+00:00_

[Round 1 审稿请求]:
你负责**新颖性与完整性**审查。

## Venue 信息
- **EMNLP 2026 via ARR** (May cycle)，截止 2026-05-25
- 正文 ≤8 页（不含 Limitations 和 References），ACL 模板，double-blind
- Overall Assessment 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit
- Limitations 章节必须有但不计入页数

## 论文路径
- LaTeX: `projects/causal_style_decomp_judge/docs/paper/main.tex`（sections/ 子目录有各章节）
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf`

## 审查侧重
请重点审查以下方面，给出逐条 Strengths / Weaknesses / Questions：

1. **Novelty 定位**：
   - "Likert Blindspot" 概念——Thurstone (1927) 以来已知 pairwise comparison 判别力优于 absolute rating，本文的增量贡献是什么？
   - 论文是否清晰区分了三种解释机制（attenuation / amplification / construct divergence）？Title "Blindspot" 是否暗示了对 Likert attenuation 的因果偏好？
   - GEE conditional decomposition 作为方法论贡献是否被充分突出？
   - 与 RATE (Reber et al. 2025) 的差异化是否清晰？

2. **Claim 与证据匹配**：
   - "systematic pattern" / "robust" 等措辞是否有足够证据支撑（仅 2 个表层风格轴 + 1 个 exploratory）？
   - Negative control 的 claim 边界——"discriminative validity" 在 TOST underpowered 条件下是否成立？
   - Cross-benchmark replication 中的 severity spectrum 解释是否 ad hoc？

3. **Related Work 覆盖度**：
   - 心理测量学文献（Thurstone, Stevens, 等）是否充分讨论了与本文发现的关系？
   - CASSE (2026), FairJudge (2026), Soumik (2026), Li (2026) 等近期竞品的定位是否准确？
   - 是否遗漏重要的 LLM judge bias 或 measurement theory 文献？

4. **展示质量**：
   - Table 1 信息密度——15 行 + 6 行脚注是否过载？是否应拆分？
   - 'style bias' vs 'style sensitivity' 措辞一致性
   - 论文叙事流畅度——从 Introduction 到 Conclusion 的逻辑链是否连贯？
   - Abstract 是否准确反映论文实际贡献（尤其是 construct divergence 是否得到同等讨论）？

5. **Scope 与 Limitations 充分性**：
   - Limitations 章节是否覆盖了所有关键限制？
   - "Code and Data" 承诺是否满足 venue 要求？

请严格评审，不留情面。输出格式：
```
## Summary
（2-3 句论文概述）

## Strengths
S1. ...
S2. ...

## Weaknesses
W1. [Must-Fix / Should-Fix / Minor] ...
W2. ...

## Questions
Q1. ...

## Missing References
...

## Overall Assessment
Score: X.X
Confidence: X/5
```

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

_source line 1060 · 2026-05-23T06:42:12.710574+00:00_

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

_source line 1061 · 2026-05-23T06:42:12.710951+00:00_



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

_source line 1062 · 2026-05-23T06:42:18.141679+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
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
    "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
  }
}
```

</details>

---


### Tool call

_source line 1063 · 2026-05-23T06:42:20.705459+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1064 · 2026-05-23T06:42:26.500820+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

## Review Scoring Scale

The review form uses the following scoring system:

- 5 = Consider for Award: Papers that could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)
- 2 = Resubmit next cy
…[truncated 899 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8359
}
```

</details>

---


### Tool result

_source line 1065 · 2026-05-23T06:42:27.715608+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 578.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.7}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 502.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 545.2}], \"total_pages\": 20, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/a
…[truncated 77 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7010
}
```

</details>

---


### Tool call

_source line 1066 · 2026-05-23T06:42:35.594921+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and any guidelines for each dimension. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions."
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
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and any guidelines for each dimension. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 1067 · 2026-05-23T06:42:36.103443+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p1.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1068 · 2026-05-23T06:42:37.058047+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p2.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1069 · 2026-05-23T06:42:37.560980+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool call

_source line 1070 · 2026-05-23T06:42:37.561419+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p3.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1071 · 2026-05-23T06:42:38.314639+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p4.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1072 · 2026-05-23T06:42:38.666497+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p5.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1073 · 2026-05-23T06:42:39.470521+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2412
}
```

</details>

---


### Tool call

_source line 1074 · 2026-05-23T06:42:39.471110+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p6.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1075 · 2026-05-23T06:42:40.183111+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p7.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1076 · 2026-05-23T06:42:41.142141+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3580
}
```

</details>

---


### Tool call

_source line 1077 · 2026-05-23T06:42:41.142585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p8.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 1078 · 2026-05-23T06:42:42.048618+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "9-20",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "9-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1079 · 2026-05-23T06:42:42.349785+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5: "Positive that my evaluation is correct"
- 4: Quite sure; unlikely major oversights
- 3: Pretty sure; possible missed details
- 2: Defensible but likely gaps in understanding
- 1: Outside expertise or incomprehensible

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- 5: "one of the most thorough I have seen"
- 4: Sufficient support; extra experiments optional
- 3: Adequate support for main claims
- 2: Major claims lack sufficient support
- 1: "not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
Evaluates subjective appeal through conceptual breakthroughs, community impact, or personal research relevance:
- 5: "I would recommend this paper to others"
- 4: Would mention to colleagues
- 3: Might mention key points
- 2: Doesn't resonate personally
- 1: "does not resonate...and I don't think it would with others"

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- 5: Consider for Award (top 2.5%)
- 4: Conference acceptance
- 3: Findings section acceptance
- 2: Substantial revisions needed
- 1: "not relevant to *ACL community"

## 5. **Reproducibility**
Scale: 1-5
- 5: Results easily reproducible
- 4: Mostly reproducible
- 3: Reproducible with difficulty
- 2: Hard to reproduce
- 1: Cannot be reproduced

## 6. **Datasets & Software**
Separate scales (1-5) assessing value to broader research community

## 7. **Additional Dimensions**
- Limitations and societal impact assessment
- Ethical concerns review
- Author identity knowledge (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6754
}
```

</details>

---


### Tool result

_source line 1080 · 2026-05-23T06:42:42.350981+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4036
}
```

</details>

---


### Tool result

_source line 1081 · 2026-05-23T06:42:43.906466+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5239
}
```

</details>

---


### Tool result

_source line 1082 · 2026-05-23T06:42:46.482243+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7011
}
```

</details>

---


### Tool result

_source line 1083 · 2026-05-23T06:42:46.706136+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6523
}
```

</details>

---


### Tool result

_source line 1084 · 2026-05-23T06:42:47.330458+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6187
}
```

</details>

---


### Tool result

_source line 1085 · 2026-05-23T06:42:49.691111+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 535.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 536.9}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.3}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 470.6}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 431.9}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 480.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.7}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images
…[truncated 992 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7642
}
```

</details>

---


### Tool call

_source line 1086 · 2026-05-23T06:42:54.161606+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p9.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1087 · 2026-05-23T06:42:54.666839+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p10.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1088 · 2026-05-23T06:42:55.175415+00:00_



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

_source line 1089 · 2026-05-23T06:42:55.177646+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p11.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1090 · 2026-05-23T06:42:56.237758+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1570
}
```

</details>

---


### Tool call

_source line 1091 · 2026-05-23T06:42:56.238214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p12.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1092 · 2026-05-23T06:42:56.591412+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1413
}
```

</details>

---


### Tool call

_source line 1093 · 2026-05-23T06:42:56.643434+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p13.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1094 · 2026-05-23T06:42:57.271699+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p14.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1095 · 2026-05-23T06:42:58.024679+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1786
}
```

</details>

---


### Tool call

_source line 1096 · 2026-05-23T06:42:58.025143+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p15.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 1097 · 2026-05-23T06:42:58.537524+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p16.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1098 · 2026-05-23T06:42:58.941030+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2297
}
```

</details>

---


### Tool call

_source line 1099 · 2026-05-23T06:42:58.941465+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p17.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 1100 · 2026-05-23T06:43:00.066731+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p18.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1101 · 2026-05-23T06:43:00.634092+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3362
}
```

</details>

---


### Tool call

_source line 1102 · 2026-05-23T06:43:00.634553+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p19.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool call

_source line 1103 · 2026-05-23T06:43:00.937465+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p20.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 1104 · 2026-05-23T06:43:01.441282+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3416
}
```

</details>

---


### Tool result

_source line 1105 · 2026-05-23T06:43:01.951761+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3414
}
```

</details>

---


### Tool result

_source line 1106 · 2026-05-23T06:43:02.204377+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3262
}
```

</details>

---


### Tool result

_source line 1107 · 2026-05-23T06:43:02.710484+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1773
}
```

</details>

---


### Tool result

_source line 1108 · 2026-05-23T06:43:02.914220+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2847
}
```

</details>

---


### Tool result

_source line 1109 · 2026-05-23T06:43:02.915241+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2280
}
```

</details>

---


### Tool call

_source line 1110 · 2026-05-23T06:46:29.222278+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一套针对 LLM judge 的黑盒诊断方法，用于量化 Likert 评分与 pairwise 比较在表层风格敏感度上的系统性差异（\"Likert Blindspot\"）。通过 NLI-gated 内容控制、单轴风格改写和位置控制的 pairwise 比较，在 4 个 judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）+ 1 个负控制（Claude Sonnet 4）、2 个主轴（formality, verbosity）+ 1 个探索轴（register）、3 个 benchmark 上展示了 pairwise 在 p < 0.001 处检测到风格偏好，而 Likert 无法检出（p > 0.17）。GEE conditional decomposition 揭示了不同轴的混淆结构差异。\n\n## Strengths\n\n**S1. 严谨的控制实验设计。** CSD 管线（Figure 2）将风格干预、内容保持、测量模式解耦的思路清晰。NLI gate 的双向验证（original→rewrite 且 rewrite→original 均需 entailment，Section 3.2）有效控制了改写引入的内容噪声。BERTScore 作为辅助监控而非门控决策变量，避免了度量堆叠的问题。\n\n**S2. GEE conditional decomposition 是真正的方法论贡献。** Section 5.2 将聚合偏好分解为 style-specific 和 quality-correlated 成分，发现 verbosity 跨全部四个 judge 为 style-dominated（Style OR 8–13, Orig OR < 1），而 formality 条件性地受 register/judge 依赖——这在 Thurstone 传统中没有对应物。Table 2 的 Style OR vs Originality OR 对比非常有信息量。\n\n**S3. 多维度复制增强可信度。** 4 judges × 3 benchmarks 的交叉复制（Section 5.3, Table 21），加上 7 种统计方法的一致性确认（Table 13–14），使核心发现不易被归因于特定 judge 或数据集的 artifact。\n\n**S4. Bradley-Terry 建模选择合理。** 使用 BT 模型处理 pairwise 数据而非简单胜率统计，通过 Appendix I 的 goodness-of-fit 检验验证了模型适用性。\n\n**S5. 详尽的附录。** 20 个附录（A–Y）覆盖 NLI 阈值敏感度、cross-axis 污染检查、长度控制回归、rewriter independence、formal power analysis 等，展现了方法论上的细致程度。\n\n## Weaknesses\n\n**W1. [Must-Fix] \"Systematic pattern\" 的 claim 基础过窄——仅 2 个主轴。**\n\nAbstract 和 Conclusion 反复使用 \"systematic\"（如 Abstract: \"systematically divergent sensitivity\"；Conclusion: \"systematic blind spots\"），但一手证据仅来自 formality 和 verbosity 两个轴，register 为探索性的且未在主表中报告。两个表层特征不足以支撑 \"systematic\" 这个词的 claim 强度。作为对比，Stureborg et al. (2024) 在类似研究中检验了更多维度。建议：(a) 将 \"systematic\" 降级为 \"consistent across tested axes\" 或类似措辞；(b) 或增加至少 1–2 个额外轴（如 conciseness vs. elaboration, technical register）的主要实验。\n\n**W2. [Must-Fix] 负控制的 discriminative validity claim 在 TOST underpowered 条件下不成立。**\n\nSection 5.1 和 Appendix H 将 Claude Sonnet 4 用作负控制，声称其展现 \"discriminative validity\"。然而 Appendix H 明确承认 TOST 功效不足（\"TOST is not significant (p = .156, power = 12%)\"）。在等价性检验功效仅 12% 的条件下，未能拒绝零假设不能解释为等价的证据——这是经典的 \"absence of evidence ≠ evidence of absence\" 错误。论文后文（Section 5.1）说 \"six controls ... bound the amplification factor\" 但这一结论的统计基础不牢固。建议：(a) 坦率承认负控制的结论是 suggestive 而非 definitive；(b) 报告达到 80% 功效所需的样本量（Appendix L 已有 formal power analysis，可直接引用）；(c) 考虑用 Bayesian equivalence testing 替代频率学 TOST。\n\n**W3. [Should-Fix] Novelty 定位模糊——Thurstone (1927) 以来的增量贡献未充分明确。**\n\nThurstone (1927) 已证明 pairwise comparison 在 discriminability 上优于 absolute rating，这在心理测量学中是教科书知识。Section 2 的 \"Measurement Sensitivity in NLG Evaluation\" 段虽引用了 Thurstone、Stevens (1946)、Preston and Colman (2000) 等，但未清晰回答：**在这些已知的测量理论基础上，本文的增量贡献到底是什么？** \n\n论文的实际增量包括：(a) 在 LLM judge 这个特定场景中量化该差距；(b) GEE 分解揭示 per-axis 混淆结构；(c) 三机制框架。但目前的叙事结构将 \"Likert Blindspot\" 这一已知现象包装为核心发现，而真正新颖的 GEE 分解（Section 5.2）被压缩在一个子节中。建议重组叙事，将 GEE decomposition 提升为一级贡献，\"Blindspot\" 降为动机/现象描述。\n\n**W4. [Should-Fix] Construct divergence 在正文中发展不足，与 abstract 承诺不匹配。**\n\nAbstract 提出三种非排他解释（attenuation / amplification / construct divergence），但正文对 construct divergence 的讨论零散且浅尝辄止。Section 5.1 最后一段简短提及 \"the two formats may measure genuinely different constructs—absolute quality versus ordinal preference\"，Section 6 再次一笔带过。相比之下，attenuation 获得了完整的 bootstrap 分析（Appendix K）和功效曲线（Figure 4）。如果论文声称三种解释并列，那么 construct divergence 需要同等深度的讨论——至少应包含一个操作性定义和可检验的预测。否则应在 abstract 中降低其地位。\n\n**W5. [Should-Fix] Cross-benchmark \"severity spectrum\" 解释为 post-hoc rationalization。**\n\nSection 5.3 将不同 benchmark（AlpacaEval, LLMBar, MT-Bench）上效果量差异解释为 \"severity spectrum\"（p.8: \"the diagnostic of GEE is sharpest on AlpacaEval\"），但这一解释是在观察到结果后构建的，没有预先假设或理论预测。为什么 AlpacaEval 的效应更强？论文归因于 \"cross-benchmark configurations targeting the strongest effects\"（Table 21），但这本身就是循环论证。建议：(a) 明确标记为 exploratory/post-hoc；(b) 提供 benchmark 特性差异（如指令长度、领域分布）的定量分析来支撑解释。\n\n**W6. [Minor] Title \"Blindspot\" 隐含因果偏好。**\n\n标题 \"The Likert Blindspot\" 将测量模式分歧框架为 Likert 的缺陷，但论文自身在 Limitations 和 Section 5.1 承认分歧可能源于 pairwise amplification（即 pairwise 过度放大风格差异）。标题创造了一个 framing bias，暗示 attenuation 是主要机制。Section 6 的 \"the Likert Blindspot\" 反复出现强化了这一印象。\n\n**W7. [Minor] Table 1 信息密度过高。**\n\nTable 1（p.6）在一张表中压缩了 4 judges × 3 axes 的 BT/Likert 结果 + 3 benchmarks 的交叉复制 + 6 条脚注。建议拆分为：(a) 主表：4 judges × 2 primary axes 的核心 Blindspot 结果；(b) 附表：cross-benchmark replication 和 register axis 结果。\n\n**W8. [Minor] 'style bias' 与 'style sensitivity' 混用。**\n\n论文在不同位置交替使用 \"style bias\"（暗示系统性偏差/错误）和 \"style sensitivity\"（中性描述）。例如 Section 1 用 \"style sensitivity\"，Abstract 用 \"sensitivity\"，但 Section 2 Related Work 标题用 \"Style Bias Detection and Mitigation\"，Section 5.1 内用 \"style preference\"。这三个术语有不同含义，应统一或明确区分。\n\n## Questions\n\n**Q1.** 为什么选择 formality 和 verbosity 作为主轴而非其他表层特征（如 sentence length variation, lexical diversity, hedging）？是否因为这两个轴最容易通过 NLI gate 后保持内容不变？如果是，这引入了一个选择偏差：论文可能只展示了 CSD 管线最有利的案例。\n\n**Q2.** GEE 分解中 exchangeable working correlation 的选择依据是什么（Appendix B 提到 robust standard errors）？如果 judge-level clustering 的真实相关结构不是 exchangeable，GEE 的点估计仍一致但效率可能损失。是否尝试过其他 correlation structures（AR(1), unstructured）？\n\n**Q3.** NLI gate 使用 DeBERTa-v3-large 且阈值 0.90。Table 8（Appendix F）显示阈值敏感度，但 NLI 模型本身的 bias 是否会引入系统性偏差？例如，DeBERTa 可能对某些改写方向（formal→casual）比另一方向更宽容，导致通过 gate 的样本在两个方向上不对称。Section 3.2 提到 \"bidirectional entailment\" 但 Table 12（Appendix G）显示 direction-aware gating 还额外放入了 21 pairs——这些 direction-dependent 的 pairs 是否引入了方向偏差？\n\n**Q4.** 论文使用的 4 个 target judges 均为 2024 年下半年的模型版本。LLM judges 的风格敏感度是否可能随模型迭代显著变化（如 RLHF 训练数据的风格分布变化）？论文是否考虑了时间效度问题？\n\n**Q5.** Formal power analysis（Appendix L, Table 12）显示对于 6 个 cells 中的 5 个，所需样本量 n ≥ 1,200——远超当前 n = 88。这意味着论文的主要结论实际上建立在 underpowered 的 Likert 实验上。换言之，Likert 的 \"failure\" 可能部分是样本量不足的 artifact 而非测量模式本身的限制。论文如何回应这一替代解释？\n\n## Missing References\n\n1. **Item Response Theory (IRT) 文献缺失。** 论文讨论 Likert 量表的测量属性但完全未引用 IRT 框架——现代心理测量学的核心工具。IRT 直接建模 item discrimination 和 difficulty，可以定量回答 \"Likert 为什么在某些效应量下失效\" 的问题。至少应引用 Embretson & Reise (2000) 或 de Ayala (2009) 并讨论 IRT 视角下的 Blindspot 解释。\n\n2. **Koo & Li (2016) — ICC 可靠性评估。** 论文用 inter-annotator agreement（Appendix V）但未引用 ICC 的标准参考文献。\n\n3. **Bojar et al. (2016) 仅在 Section 3 脚注中提及 WMT 从 ranking 到 rating 的转变，但未深入讨论 WMT 社区在此转变中积累的经验教训**——这与本文核心论点直接相关。\n\n## Overall Assessment\n\n**Score: 3.5 (Borderline Conference)**\n\n**Confidence: 4/5**\n\n**一句话总结：** 方法论设计严谨（尤其是 NLI-gated 控制和 GEE 分解），但核心发现（pairwise > Likert sensitivity）的增量新颖性不足以弥补 claim scope 过宽（2 axes → \"systematic\"）和关键统计论证缺陷（underpowered TOST → \"discriminative validity\"）的问题。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计careful，但 TOST underpowered、formal power analysis 显示主实验本身 underpowered for Likert，claim scope超证据 |\n| Excitement | 3.0/5 | 核心发现在心理测量学中已知近百年；GEE 分解有方法论价值但被 undersold；实践影响有限（诊断工具但无修复方案） |\n| Reproducibility | 4/5 | 详细的实现细节（Appendix R）、承诺开源代码和数据、统计方法充分描述；但人工标注流程细节（Appendix V）较简略 |\n| Overall Assessment | 3.5/5 | Borderline Conference — 修复 claim scope 和 TOST 论证后有望提升至 Conference 级别 |",
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
    "text": "## Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一套针对 LLM judge 的黑盒诊断方法，用于量化 Likert 评分与 pairwise 比较在表层风格敏感度上的系统性差异（\"Likert Blindspot\"）。通过 NLI-gated 内容控制、单轴风格改写和位置控制的 pairwise 比较，在 4 个 judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）+ 1 个负控制（Claude Sonnet 4）、2 个主轴（formality, verbosity）+ 1 个探索轴（register）、3 个 benchmark 上展示了 pairwise 在 p < 0.001 处检测到风格偏好，而 Likert 无法检出（p > 0.17）。GEE conditional decomposition 揭示了不同轴的混淆结构差异。\n\n## Strengths\n\n**S1. 严谨的控制实验设计。** CSD 管线（Figure 2）将风格干预、内容保持、测量模式解耦的思路清晰。NLI gate 的双向验证（original→rewrite 且 rewrite→original 均需 entailment，Section 3.2）有效控制了改写引入的内容噪声。BERTScore 作为辅助监控而非门控决策变量，避免了度量堆叠的问题。\n\n**S2. GEE conditional decomposition 是真正的方法论贡献。** Section 5.2 将聚合偏好分解为 style-specific 和 quality-correlated 成分，发现 verbosity 跨全部四个 judge 为 style-dominated（Style OR 8–13, Orig OR < 1），而 formality 条件性地受 register/judge 依赖——这在 Thurstone 传统中没有对应物。Table 2 的 Style OR vs Originality OR 对比非常有信息量。\n\n**S3. 多维度复制增强可信度。** 4 judges × 3 benchmarks 的交叉复制（Section 5.3, Table 21），加上 7 种统计方法的一致性确认（Table 13–14），使核心发现不易被归因于特定 judge 或数据集的 artifact。\n\n**S4. Bradley-Terry 建模选择合理。** 使用 BT 模型处理 pairwise 数据而非简单胜率统计，通过 Appendix I 的 goodness-of-fit 检验验证了模型适用性。\n\n**S5. 详尽的附录。** 20 个附录（A–Y）覆盖 NLI 阈值敏感度、cross-axis 污染检查、长度控制回归、rewriter independence、formal power analysis 等，展现了方法论上的细致程度。\n\n## Weaknesses\n\n**W1. [Must-Fix] \"Systematic pattern\" 的 claim 基础过窄——仅 2 个主轴。**\n\nAbstract 和 Conclusion 反复使用 \"systematic\"（如 Abstract: \"systematically divergent sensitivity\"；Conclusion: \"systematic blind spots\"），但一手证据仅来自 formality 和 verbosity 两个轴，register 为探索性的且未在主表中报告。两个表层特征不足以支撑 \"systematic\" 这个词的 claim 强度。作为对比，Stureborg et al. (2024) 在类似研究中检验了更多维度。建议：(a) 将 \"systematic\" 降级为 \"consistent across tested axes\" 或类似措辞；(b) 或增加至少 1–2 个额外轴（如 conciseness vs. elaboration, technical register）的主要实验。\n\n**W2. [Must-Fix] 负控制的 discriminative validity claim 在 TOST underpowered 条件下不成立。**\n\nSection 5.1 和 Appendix H 将 Claude Sonnet 4 用作负控制，声称其展现 \"discriminative validity\"。然而 Appendix H 明确承认 TOST 功效不足（\"TOST is not significant (p = .156, power = 12%)\"）。在等价性检验功效仅 12% 的条件下，未能拒绝零假设不能解释为等价的证据——这是经典的 \"absence of evidence ≠ evidence of absence\" 错误。论文后文（Section 5.1）说 \"six controls ... bound the amplification factor\" 但这一结论的统计基础不牢固。建议：(a) 坦率承认负控制的结论是 suggestive 而非 definitive；(b) 报告达到 80% 功效所需的样本量（Appendix L 已有 formal power analysis，可直接引用）；(c) 考虑用 Bayesian equivalence testing 替代频率学 TOST。\n\n**W3. [Should-Fix] Novelty 定位模糊——Thurstone (1927) 以来的增量贡献未充分明确。**\n\nThurstone (1927) 已证明 pairwise comparison 在 discriminability 上优于 absolute rating，这在心理测量学中是教科书知识。Section 2 的 \"Measurement Sensitivity in NLG Evaluation\" 段虽引用了 Thurstone、Stevens (1946)、Preston and Colman (2000) 等，但未清晰回答：**在这些已知的测量理论基础上，本文的增量贡献到底是什么？** \n\n论文的实际增量包括：(a) 在 LLM judge 这个特定场景中量化该差距；(b) GEE 分解揭示 per-axis 混淆结构；(c) 三机制框架。但目前的叙事结构将 \"Likert Blindspot\" 这一已知现象包装为核心发现，而真正新颖的 GEE 分解（Section 5.2）被压缩在一个子节中。建议重组叙事，将 GEE decomposition 提升为一级贡献，\"Blindspot\" 降为动机/现象描述。\n\n**W4. [Should-Fix] Construct divergence 在正文中发展不足，与 abstract 承诺不匹配。**\n\nAbstract 提出三种非排他解释（attenuation / amplification / construct divergence），但正文对 construct divergence 的讨论零散且浅尝辄止。Section 5.1 最后一段简短提及 \"the two formats may measure genuinely different constructs—absolute quality versus ordinal preference\"，Section 6 再次一笔带过。相比之下，attenuation 获得了完整的 bootstrap 分析（Appendix K）和功效曲线（Figure 4）。如果论文声称三种解释并列，那么 construct divergence 需要同等深度的讨论——至少应包含一个操作性定义和可检验的预测。否则应在 abstract 中降低其地位。\n\n**W5. [Should-Fix] Cross-benchmark \"severity spectrum\" 解释为 post-hoc rationalization。**\n\nSection 5.3 将不同 benchmark（AlpacaEval, LLMBar, MT-Bench）上效果量差异解释为 \"severity spectrum\"（p.8: \"the diagnostic of GEE is sharpest on AlpacaEval\"），但这一解释是在观察到结果后构建的，没有预先假设或理论预测。为什么 AlpacaEval 的效应更强？论文归因于 \"cross-benchmark configurations targeting the strongest effects\"（Table 21），但这本身就是循环论证。建议：(a) 明确标记为 exploratory/post-hoc；(b) 提供 benchmark 特性差异（如指令长度、领域分布）的定量分析来支撑解释。\n\n**W6. [Minor] Title \"Blindspot\" 隐含因果偏好。**\n\n标题 \"The Likert Blindspot\" 将测量模式分歧框架为 Likert 的缺陷，但论文自身在 Limitations 和 Section 5.1 承认分歧可能源于 pairwise amplification（即 pairwise 过度放大风格差异）。标题创造了一个 framing bias，暗示 attenuation 是主要机制。Section 6 的 \"the Likert Blindspot\" 反复出现强化了这一印象。\n\n**W7. [Minor] Table 1 信息密度过高。**\n\nTable 1（p.6）在一张表中压缩了 4 judges × 3 axes 的 BT/Likert 结果 + 3 benchmarks 的交叉复制 + 6 条脚注。建议拆分为：(a) 主表：4 judges × 2 primary axes 的核心 Blindspot 结果；(b) 附表：cross-benchmark replication 和 register axis 结果。\n\n**W8. [Minor] 'style bias' 与 'style sensitivity' 混用。**\n\n论文在不同位置交替使用 \"style bias\"（暗示系统性偏差/错误）和 \"style sensitivity\"（中性描述）。例如 Section 1 用 \"style sensitivity\"，Abstract 用 \"sensitivity\"，但 Section 2 Related Work 标题用 \"Style Bias Detection and Mitigation\"，Section 5.1 内用 \"style preference\"。这三个术语有不同含义，应统一或明确区分。\n\n## Questions\n\n**Q1.** 为什么选择 formality 和 verbosity 作为主轴而非其他表层特征（如 sentence length variation, lexical diversity, hedging）？是否因为这两个轴最容易通过 NLI gate 后保持内容不变？如果是，这引入了一个选择偏差：论文可能只展示了 CSD 管线最有利的案例。\n\n**Q2.** GEE 分解中 exchangeable working correlation 的选择依据是什么（Appendix B 提到 robust standard errors）？如果 judge-level clustering 的真实相关结构不是 exchangeable，GEE 的点估计仍一致但效率可能损失。是否尝试过其他 correlation structures（AR(1), unstructured）？\n\n**Q3.** NLI gate 使用 DeBERTa-v3-large 且阈值 0.90。Table 8（Appendix F）显示阈值敏感度，但 NLI 模型本身的 bias 是否会引入系统性偏差？例如，DeBERTa 可能对某些改写方向（formal→casual）比另一方向更宽容，导致通过 gate 的样本在两个方向上不对称。Section 3.2 提到 \"bidirectional entailment\" 但 Table 12（Appendix G）显示 direction-aware gating 还额外放入了 21 pairs——这些 direction-dependent 的 pairs 是否引入了方向偏差？\n\n**Q4.** 论文使用的 4 个 target judges 均为 2024 年下半年的模型版本。LLM judges 的风格敏感度是否可能随模型迭代显著变化（如 RLHF 训练数据的风格分布变化）？论文是否考虑了时间效度问题？\n\n**Q5.** Formal power analysis（Appendix L, Table 12）显示对于 6 个 cells 中的 5 个，所需样本量 n ≥ 1,200——远超当前 n = 88。这意味着论文的主要结论实际上建立在 underpowered 的 Likert 实验上。换言之，Likert 的 \"failure\" 可能部分是样本量不足的 artifact 而非测量模式本身的限制。论文如何回应这一替代解释？\n\n## Missing References\n\n1. **Item Response Theory (IRT) 文献缺失。** 论文讨论 Likert 量表的测量属性但完全未引用 IRT 框架——现代心理测量学的核心工具。IRT 直接建模 item discrimination 和 difficulty，可以定量回答 \"Likert 为什么在某些效应量下失效\" 的问题。至少应引用 Embretson & Reise (2000) 或 de Ayala (2009) 并讨论 IRT 视角下的 Blindspot 解释。\n\n2. **Koo & Li (2016) — ICC 可靠性评估。** 论文用 inter-annotator agreement（Appendix V）但未引用 ICC 的标准参考文献。\n\n3. **Bojar et al. (2016) 仅在 Section 3 脚注中提及 WMT 从 ranking 到 rating 的转变，但未深入讨论 WMT 社区在此转变中积累的经验教训**——这与本文核心论点直接相关。\n\n## Overall Assessment\n\n**Score: 3.5 (Borderline Conference)**\n\n**Confidence: 4/5**\n\n**一句话总结：** 方法论设计严谨（尤其是 NLI-gated 控制和 GEE 分解），但核心发现（pairwise > Likert sensitivity）的增量新颖性不足以弥补 claim scope 过宽（2 axes → \"systematic\"）和关键统计论证缺陷（underpowered TOST → \"discriminative validity\"）的问题。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计careful，但 TOST underpowered、formal power analysis 显示主实验本身 underpowered for Likert，claim scope超证据 |\n| Excitement | 3.0/5 | 核心发现在心理测量学中已知近百年；GEE 分解有方法论价值但被 undersold；实践影响有限（诊断工具但无修复方案） |\n| Reproducibility | 4/5 | 详细的实现细节（Appendix R）、承诺开源代码和数据、统计方法充分描述；但人工标注流程细节（Appendix V）较简略 |\n| Overall Assessment | 3.5/5 | Borderline Conference — 修复 claim scope 和 TOST 论证后有望提升至 Conference 级别 |",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1111 · 2026-05-23T06:46:32.838565+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3616
}
```

</details>

---


### Tool call

_source line 1112 · 2026-05-23T06:46:44.582596+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images"
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
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_14/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1113 · 2026-05-23T06:46:44.633203+00:00_

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

_source line 1114 · 2026-05-23T06:46:46.828760+00:00_

清理完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 34

## Round 34

4 recorded events


### User

_source line 1115 · 2026-05-23T06:49:56.254924+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 完整审稿意见

**Summary**: 本文提出 CSD，一种黑盒诊断方法，用于量化 LLM judge 在 pairwise comparison 与 Likert scoring 两种评测模式下对表面风格特征的敏感性差异。核心发现为"Likert Blindspot"：pairwise comparison 能检测到统计显著的风格偏好（BT p < 0.001），而 Likert 在同一数据上无法检测到（p > 0.17）。GEE 条件分解揭示了不同风格轴的混淆结构差异。

**Strengths**:
S1. 研究问题重要且新颖——测量模式对 LLM judge 风格敏感性的系统影响此前未被严格量化，对 RLHF/DPO pipeline 有直接实践意义。
S2. 统计框架全面且层次清晰——三层分析设计 + 七种统计方法的 sensitivity hierarchy。
S3. 多 judge、多 benchmark 的系统性复制——四个独立 judge 横跨四种架构，三个 benchmark。
S4. GEE 条件分解提供了超越"存在 bias"的结构性洞见——将 aggregate preference 分解为 style-specific 和 quality-correlated components。
S5. 论文组织和写作质量高——正文 8 页内容密度极高但逻辑清晰。

**Weaknesses**:
W1. [Must-Fix] NLI gate 的 content preservation 验证不充分——仅 50 pairs, κ=0.44, A2 pass precision 下界仅 65.3%。如果 ~35% NLI-passed pairs 存在 content contamination，pairwise 检测到的"style sensitivity"可能部分反映 content quality difference。
W2. [Must-Fix] Negative control (Claude Sonnet 4) TOST 等价性检验严重 underpowered——TOST Δ=10pp power 仅 42%，三条收敛证据（TOST Δ=15pp, GEE Style OR cross-benchmark, GPT-4o contrast）中每一条单独看都不具说服力。
W3. [Should-Fix] GEE OR 在 n=88→n=355 时出现 49% shrinkage——Table 2 报告的效应量可能严重高估。仅对一个条件（Qwen3 formality）有 scaled replication。
W4. [Should-Fix] Evaluator-producer overlap 缓解不充分——仅测试一个替代 rewriter (GPT-4o)，22% OR 降幅是 lower bound。
W5. [Should-Fix] FK grade d=0.50 cross-axis contamination 处理不够充分——length-controlled regression 控制了 word count 但未控制 readability 本身。
W6. [Should-Fix] 100-point continuous Likert 仅在 Qwen3-32B 上测试。
W7. [Minor] BT 模型 unidimensionality 假设与论文核心论点（judges 在多维度评估）存在张力。
W8. [Minor] 论文 framing 预设 pairwise 是"正确"测量模式。

**Questions**:
Q1. Table 2 中 Qwen3 verbosity Orig OR=0.49——是否暗示 verbose rewrites 系统性引入 quality improvement？
Q2. Direction-aware gating 新增的 21% pairs 是否在 style effect magnitude 上与原有 pairs 有系统性差异？
Q3. Formal power analysis 显示 Likert 需 n=1,473–18,157，Likert non-significance 可能仅反映 power 不足？
Q4. GEE 是否测试过 AR(1) 或 unstructured correlation？
Q5. 是否考虑过 base models 作为 judge——instruction tuning 本身可能引入 style preference？
Q6. Holm-Bonferroni 中 Gemini formality 的具体 margin？

**Missing References**: 无明显遗漏。可考虑补充 Zheng et al. (2024) Chatbot Arena 中 pairwise vs. rating 差异的大规模实证分析。

**Overall Assessment**: Score 3.5, Confidence 4/5

---

请对以上每个 Weakness（W1-W8）和 Question（Q1-Q6）逐条标注 [AGREE] 或 [REBUT]，并简要说明理由。

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

_source line 1116 · 2026-05-23T06:52:14.386875+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 交叉回应：Reviewer 2 对 Reviewer 1 审稿意见的逐条评议\n\n---\n\n### Strengths\n\n[AGREE] R1-S1: 研究问题确实重要——但我对\"新颖性\"的评估比 R1 更保守。Pairwise vs. rating 的 discriminability 差异自 Thurstone (1927) 起已知近百年，本文的增量贡献在于将其迁移到 LLM judge 场景并提供 GEE 分解工具。R1 将研究问题评为\"新颖\"可能过于宽容。\n\n[AGREE] R1-S2: 统计框架的层次设计（三层分析 + 七方法 sensitivity hierarchy, Table 13–14）确实是本文的亮点。我在自己的审稿中同样认可这一点。\n\n[AGREE] R1-S3: 多 judge × 多 benchmark 复制是本文最强的方法论资产。\n\n[AGREE] R1-S4: GEE conditional decomposition 是本文最重要的方法论贡献。我在自己的审稿中指出它被 undersold（我的 W3），R1 与我在此一致。\n\n[AGREE] R1-S5: 写作质量在 8 页限制内确实出色，但我同时指出 Table 1 信息密度过高（我的 W7）。\n\n---\n\n### Weaknesses\n\n**[AGREE] R1-W1: NLI gate content preservation 验证不充分。**\nR1 指出仅 50 pairs、κ=0.44、A2 pass precision 下界 65.3%。这是一个关键的 validity 威胁，我在审稿中未单独展开但完全同意。补充两点：(a) κ=0.44 在 Landis & Koch 标准下仅为 \"moderate agreement\"，对于核心 validity check 来说偏低；(b) 论文的 cross-axis contamination 分析（Appendix S, Table 19）显示 word count d=−0.03、type-token ratio d=−0.23，虽然效应量小，但 TTR 的 d=−0.23 并非完全可忽略。如果 NLI-passed pairs 中约 35% 存在 content contamination，pairwise 的更高敏感度可能部分源于它对 content 微妙差异的更强检测力——而非 style sensitivity 本身。这将从根本上威胁 \"Likert Blindspot\" 的因果归因。\n\n**[AGREE] R1-W2: Negative control TOST underpowered。**\n我在自己的审稿中将此列为 Must-Fix（我的 W2），与 R1 完全一致。补充：R1 指出三条收敛证据（TOST Δ=15pp, GEE Style OR cross-benchmark, GPT-4o contrast）\"每一条单独看都不具说服力\"——我同意这一判断。特别是 GEE Style OR cross-benchmark 的证据（Table 22, Claude Sonnet 4 formality Style OR 1.47/1.99/1.64）虽然比其他 judges 低，但仍然 >1，严格来说并未达到\"无效应\"的标准。论文将此解释为\"quality detection rather than style sensitivity\"（Section X, p.17），但这依赖于对 GEE 分解的特定解读，而非独立验证。两位 reviewer 一致认为负控制论证不成立，这应该被视为强信号。\n\n**[AGREE] R1-W3: GEE OR shrinkage 49%。**\nTable 2 的 Style OR（n=88）与 scaled replication（n=355）之间 49% 的萎缩（Section 5.2: \"Style OR drops from 4.20 to 2.15\"）是 winner's curse / small-sample upward bias 的经典表现。R1 正确指出仅 Qwen3 formality 一个条件有 scaled replication。这意味着 Table 2 中其他条件（特别是 Llama-70B verbosity 的 Style OR 4.01, Gemini verbosity 的 Style OR 8.96）可能同样存在严重的效应量膨胀。我在自己的审稿中因篇幅未展开此点，但完全认同。建议论文至少对 verbosity 轴也执行 scaled replication。\n\n**[AGREE] R1-W4: Evaluator-producer overlap 缓解不充分。**\nAppendix E 仅用 GPT-4o 作为替代 rewriter，22% OR 降幅是单一数据点。R1 称其为 \"lower bound\" 合理——如果用更不同的 rewriter（如开源模型、规则 baseline），overlap 效应可能更大。我补充一点：论文将 GPT-4o rewriter 的结果框架为\"Blindspot replicates with independent rewriter\"（p.11, Section E），但 GPT-4o 与目标 judge 之一（GPT-4o 自身）存在完全重叠，与其他 judges 也可能共享训练数据分布。真正的 independence 需要使用训练数据完全不同的 rewriter。\n\n**[AGREE] R1-W5: FK grade cross-axis contamination。**\nFK grade d=0.50 是 medium effect size。论文控制了 word count（Appendix T, Table 20）但 FK grade 是 sentence length × syllable count 的函数，word count 控制不等于 readability 控制。R1 的建议——直接将 FK grade 作为 GEE 协变量——是一个可行且必要的 robustness check。我同意这应列为 Should-Fix。\n\n**[REBUT] R1-W6: 100-point continuous Likert 仅在 Qwen3-32B 上测试。**\nR1 的关切合理（单 judge 泛化性有限），但我认为严重程度低于 R1 的评估。理由：(a) 100-point Likert 实验（Appendix O, Table 15）的目的是检验\"Blindspot 是否纯粹是量表粒度问题\"，而非全面复制主实验。在这个有限目标下，单 judge 足以作为 proof-of-concept：即使用 100 个可能得分值，pairwise BT 仍然 significant (p < 0.001) 而 Likert 仍然 non-significant——说明粒度不是唯一解释；(b) Qwen3-32B 在主实验中是 Likert 效应最强的 judge 之一（Table 1），如果连它都在 100-point 条件下仍然 non-significant，这实际上是对论文论点最保守的检验。但我同意，在 camera-ready 中增加至少一个 judge 的 100-point 复制会增强说服力。\n\n**[AGREE] R1-W7: BT unidimensionality 假设张力。**\nBT 模型假设单一潜在维度，但论文核心论点是 judges 同时受 style 和 quality 影响。这确实是一个概念张力。不过我注意到论文在 Limitations 第一段（p.9: \"the BT model assumes unidimensionality—a single latent...\"）有所讨论，承认 BT 不能分离多维影响，这正是引入 GEE 分解的动机。所以这个张力在论文架构中是被有意识地处理的，但 R1 指出在方法论章节缺乏预先讨论是正确的。\n\n**[AGREE] R1-W8: Framing 预设 pairwise 为\"正确\"模式。**\n与我的审稿 W6（Title \"Blindspot\" 隐含因果偏好）完全一致。标题和正文多处将分歧框架为 Likert 的\"盲点\"而非 pairwise 的\"过敏\"。两位 reviewer 一致指出这一 framing bias，强化了修改的必要性。\n\n---\n\n### Questions\n\n**[AGREE] R1-Q1: Qwen3 verbosity Orig OR=0.49 是否暗示 verbose rewrites 引入 quality improvement？**\n这是个好问题。Table 2 中 Orig OR < 1（verbosity 全部四个 judges）意味着 originality 维度上原文被偏好（即 verbose rewrite 降低了感知质量）。这实际上对论文有利：style preference（高 Style OR）和 quality preference（低 Orig OR）方向相反，说明 GEE 成功分离了两个成分。但 R1 的隐含关切是：如果 verbose rewrites 系统性地降低质量，那么 pairwise 模式可能更善于检测 quality 差异而非 style preference——这与 Blindspot 的归因相关。论文应明确讨论这一替代解释。\n\n**[AGREE] R1-Q2: Direction-aware gating 新增 21% pairs 的效应量差异。**\nAppendix G（Table 12, p.12）提到 direction-aware gating 额外放入 21 pairs（32%），但未报告这些 pairs 的 BT/Likert 效应量是否与原始 pairs 有系统差异。如果新增 pairs 的效应量更大/更小，这会影响对核心结果的解读。这是一个简单的 robustness check，应该执行。\n\n**[AGREE] R1-Q3: Likert non-significance 可能仅反映 power 不足。**\n这是我审稿中的 Q5，两位 reviewer 独立得出相同关切。Formal power analysis（Appendix L, Table 12）显示 Likert 在 5/6 cells 需要 n ≥ 1,200。当前 n=88，Likert 的 \"failure\" 可能是 underpowered 的数学必然而非 measurement mode 的本质局限。论文虽然提供了 bootstrap attenuation analysis（Appendix K）试图论证 \"Blindspot 是 structural 而非 merely power\"，但这一分析本身依赖于 pairwise 效应量作为 benchmark——循环论证的嫌疑。两位 reviewer 的一致判断增强了此关切的权重。\n\n**[AGREE] R1-Q4: GEE correlation structure。**\n与我的 Q2 一致。论文使用 exchangeable working correlation + robust sandwich SE（Appendix B, D），理论上 GEE 点估计在 correlation structure 误指定下仍一致，但效率损失可能影响 CI 宽度。至少应报告 AR(1) 和 unstructured 的敏感度比较。\n\n**[AGREE] R1-Q5: Base models 作为 judge。**\n有价值的建议。Instruction tuning 和 RLHF 可能引入 systematic style preferences（如偏好 formal/verbose 输出），这使得当前所有 target judges 共享一个潜在的 confound。使用 base models（如 Llama-3.3-70B-base）作为对照可以分离 alignment-induced vs. inherent style sensitivity。但我认为这更适合 future work 而非 Must-Fix——base models 通常无法可靠地遵循 judge instructions，实验可行性有限。\n\n**[REBUT] R1-Q6: Holm-Bonferroni 中 Gemini formality 的具体 margin。**\nR1 要求报告具体 margin，但 Appendix S（Table 18, p.15）已报告了 Holm-Bonferroni adjusted p-values，其中 Gemini formality 的 Holm-Bonferroni Threshold Adj 列有具体数值。论文称 \"All results remain significant under the expanded family\"。如果 R1 要求的是 equivalence margin 而非 significance margin，那这属于 Q2（TOST）的范畴，已在 Appendix H 讨论。此问题可能基于对附录细节的遗漏，信息已在论文中提供。\n\n---\n\n### 综合评价\n\nR1 的审稿与我的审稿在核心问题上高度一致：\n1. **TOST underpowered**（我的 W2 = R1 的 W2）：两位 reviewer 一致 Must-Fix\n2. **Claim scope 过宽**（我的 W1 \"systematic\" on 2 axes）：R1 未直接提但通过 W3/Q3 间接触及\n3. **Likert power 不足作为替代解释**（我的 Q5 = R1 的 Q3）：两位 reviewer 独立得出\n4. **Framing bias**（我的 W6 = R1 的 W8）：一致指出\n\nR1 补充了我未充分展开的几个重要技术点：NLI gate 验证不充分（W1）、GEE OR shrinkage（W3）、evaluator-producer overlap（W4）。这些加强了对方法论 soundness 的关切。\n\n两位 reviewer 的共同判断：论文方法论设计用心但多个关键统计论证存在 gap，核心 claim 强度超出证据支撑，Borderline Conference（3.5）。",
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
    "text": "## 交叉回应：Reviewer 2 对 Reviewer 1 审稿意见的逐条评议\n\n---\n\n### Strengths\n\n[AGREE] R1-S1: 研究问题确实重要——但我对\"新颖性\"的评估比 R1 更保守。Pairwise vs. rating 的 discriminability 差异自 Thurstone (1927) 起已知近百年，本文的增量贡献在于将其迁移到 LLM judge 场景并提供 GEE 分解工具。R1 将研究问题评为\"新颖\"可能过于宽容。\n\n[AGREE] R1-S2: 统计框架的层次设计（三层分析 + 七方法 sensitivity hierarchy, Table 13–14）确实是本文的亮点。我在自己的审稿中同样认可这一点。\n\n[AGREE] R1-S3: 多 judge × 多 benchmark 复制是本文最强的方法论资产。\n\n[AGREE] R1-S4: GEE conditional decomposition 是本文最重要的方法论贡献。我在自己的审稿中指出它被 undersold（我的 W3），R1 与我在此一致。\n\n[AGREE] R1-S5: 写作质量在 8 页限制内确实出色，但我同时指出 Table 1 信息密度过高（我的 W7）。\n\n---\n\n### Weaknesses\n\n**[AGREE] R1-W1: NLI gate content preservation 验证不充分。**\nR1 指出仅 50 pairs、κ=0.44、A2 pass precision 下界 65.3%。这是一个关键的 validity 威胁，我在审稿中未单独展开但完全同意。补充两点：(a) κ=0.44 在 Landis & Koch 标准下仅为 \"moderate agreement\"，对于核心 validity check 来说偏低；(b) 论文的 cross-axis contamination 分析（Appendix S, Table 19）显示 word count d=−0.03、type-token ratio d=−0.23，虽然效应量小，但 TTR 的 d=−0.23 并非完全可忽略。如果 NLI-passed pairs 中约 35% 存在 content contamination，pairwise 的更高敏感度可能部分源于它对 content 微妙差异的更强检测力——而非 style sensitivity 本身。这将从根本上威胁 \"Likert Blindspot\" 的因果归因。\n\n**[AGREE] R1-W2: Negative control TOST underpowered。**\n我在自己的审稿中将此列为 Must-Fix（我的 W2），与 R1 完全一致。补充：R1 指出三条收敛证据（TOST Δ=15pp, GEE Style OR cross-benchmark, GPT-4o contrast）\"每一条单独看都不具说服力\"——我同意这一判断。特别是 GEE Style OR cross-benchmark 的证据（Table 22, Claude Sonnet 4 formality Style OR 1.47/1.99/1.64）虽然比其他 judges 低，但仍然 >1，严格来说并未达到\"无效应\"的标准。论文将此解释为\"quality detection rather than style sensitivity\"（Section X, p.17），但这依赖于对 GEE 分解的特定解读，而非独立验证。两位 reviewer 一致认为负控制论证不成立，这应该被视为强信号。\n\n**[AGREE] R1-W3: GEE OR shrinkage 49%。**\nTable 2 的 Style OR（n=88）与 scaled replication（n=355）之间 49% 的萎缩（Section 5.2: \"Style OR drops from 4.20 to 2.15\"）是 winner's curse / small-sample upward bias 的经典表现。R1 正确指出仅 Qwen3 formality 一个条件有 scaled replication。这意味着 Table 2 中其他条件（特别是 Llama-70B verbosity 的 Style OR 4.01, Gemini verbosity 的 Style OR 8.96）可能同样存在严重的效应量膨胀。我在自己的审稿中因篇幅未展开此点，但完全认同。建议论文至少对 verbosity 轴也执行 scaled replication。\n\n**[AGREE] R1-W4: Evaluator-producer overlap 缓解不充分。**\nAppendix E 仅用 GPT-4o 作为替代 rewriter，22% OR 降幅是单一数据点。R1 称其为 \"lower bound\" 合理——如果用更不同的 rewriter（如开源模型、规则 baseline），overlap 效应可能更大。我补充一点：论文将 GPT-4o rewriter 的结果框架为\"Blindspot replicates with independent rewriter\"（p.11, Section E），但 GPT-4o 与目标 judge 之一（GPT-4o 自身）存在完全重叠，与其他 judges 也可能共享训练数据分布。真正的 independence 需要使用训练数据完全不同的 rewriter。\n\n**[AGREE] R1-W5: FK grade cross-axis contamination。**\nFK grade d=0.50 是 medium effect size。论文控制了 word count（Appendix T, Table 20）但 FK grade 是 sentence length × syllable count 的函数，word count 控制不等于 readability 控制。R1 的建议——直接将 FK grade 作为 GEE 协变量——是一个可行且必要的 robustness check。我同意这应列为 Should-Fix。\n\n**[REBUT] R1-W6: 100-point continuous Likert 仅在 Qwen3-32B 上测试。**\nR1 的关切合理（单 judge 泛化性有限），但我认为严重程度低于 R1 的评估。理由：(a) 100-point Likert 实验（Appendix O, Table 15）的目的是检验\"Blindspot 是否纯粹是量表粒度问题\"，而非全面复制主实验。在这个有限目标下，单 judge 足以作为 proof-of-concept：即使用 100 个可能得分值，pairwise BT 仍然 significant (p < 0.001) 而 Likert 仍然 non-significant——说明粒度不是唯一解释；(b) Qwen3-32B 在主实验中是 Likert 效应最强的 judge 之一（Table 1），如果连它都在 100-point 条件下仍然 non-significant，这实际上是对论文论点最保守的检验。但我同意，在 camera-ready 中增加至少一个 judge 的 100-point 复制会增强说服力。\n\n**[AGREE] R1-W7: BT unidimensionality 假设张力。**\nBT 模型假设单一潜在维度，但论文核心论点是 judges 同时受 style 和 quality 影响。这确实是一个概念张力。不过我注意到论文在 Limitations 第一段（p.9: \"the BT model assumes unidimensionality—a single latent...\"）有所讨论，承认 BT 不能分离多维影响，这正是引入 GEE 分解的动机。所以这个张力在论文架构中是被有意识地处理的，但 R1 指出在方法论章节缺乏预先讨论是正确的。\n\n**[AGREE] R1-W8: Framing 预设 pairwise 为\"正确\"模式。**\n与我的审稿 W6（Title \"Blindspot\" 隐含因果偏好）完全一致。标题和正文多处将分歧框架为 Likert 的\"盲点\"而非 pairwise 的\"过敏\"。两位 reviewer 一致指出这一 framing bias，强化了修改的必要性。\n\n---\n\n### Questions\n\n**[AGREE] R1-Q1: Qwen3 verbosity Orig OR=0.49 是否暗示 verbose rewrites 引入 quality improvement？**\n这是个好问题。Table 2 中 Orig OR < 1（verbosity 全部四个 judges）意味着 originality 维度上原文被偏好（即 verbose rewrite 降低了感知质量）。这实际上对论文有利：style preference（高 Style OR）和 quality preference（低 Orig OR）方向相反，说明 GEE 成功分离了两个成分。但 R1 的隐含关切是：如果 verbose rewrites 系统性地降低质量，那么 pairwise 模式可能更善于检测 quality 差异而非 style preference——这与 Blindspot 的归因相关。论文应明确讨论这一替代解释。\n\n**[AGREE] R1-Q2: Direction-aware gating 新增 21% pairs 的效应量差异。**\nAppendix G（Table 12, p.12）提到 direction-aware gating 额外放入 21 pairs（32%），但未报告这些 pairs 的 BT/Likert 效应量是否与原始 pairs 有系统差异。如果新增 pairs 的效应量更大/更小，这会影响对核心结果的解读。这是一个简单的 robustness check，应该执行。\n\n**[AGREE] R1-Q3: Likert non-significance 可能仅反映 power 不足。**\n这是我审稿中的 Q5，两位 reviewer 独立得出相同关切。Formal power analysis（Appendix L, Table 12）显示 Likert 在 5/6 cells 需要 n ≥ 1,200。当前 n=88，Likert 的 \"failure\" 可能是 underpowered 的数学必然而非 measurement mode 的本质局限。论文虽然提供了 bootstrap attenuation analysis（Appendix K）试图论证 \"Blindspot 是 structural 而非 merely power\"，但这一分析本身依赖于 pairwise 效应量作为 benchmark——循环论证的嫌疑。两位 reviewer 的一致判断增强了此关切的权重。\n\n**[AGREE] R1-Q4: GEE correlation structure。**\n与我的 Q2 一致。论文使用 exchangeable working correlation + robust sandwich SE（Appendix B, D），理论上 GEE 点估计在 correlation structure 误指定下仍一致，但效率损失可能影响 CI 宽度。至少应报告 AR(1) 和 unstructured 的敏感度比较。\n\n**[AGREE] R1-Q5: Base models 作为 judge。**\n有价值的建议。Instruction tuning 和 RLHF 可能引入 systematic style preferences（如偏好 formal/verbose 输出），这使得当前所有 target judges 共享一个潜在的 confound。使用 base models（如 Llama-3.3-70B-base）作为对照可以分离 alignment-induced vs. inherent style sensitivity。但我认为这更适合 future work 而非 Must-Fix——base models 通常无法可靠地遵循 judge instructions，实验可行性有限。\n\n**[REBUT] R1-Q6: Holm-Bonferroni 中 Gemini formality 的具体 margin。**\nR1 要求报告具体 margin，但 Appendix S（Table 18, p.15）已报告了 Holm-Bonferroni adjusted p-values，其中 Gemini formality 的 Holm-Bonferroni Threshold Adj 列有具体数值。论文称 \"All results remain significant under the expanded family\"。如果 R1 要求的是 equivalence margin 而非 significance margin，那这属于 Q2（TOST）的范畴，已在 Appendix H 讨论。此问题可能基于对附录细节的遗漏，信息已在论文中提供。\n\n---\n\n### 综合评价\n\nR1 的审稿与我的审稿在核心问题上高度一致：\n1. **TOST underpowered**（我的 W2 = R1 的 W2）：两位 reviewer 一致 Must-Fix\n2. **Claim scope 过宽**（我的 W1 \"systematic\" on 2 axes）：R1 未直接提但通过 W3/Q3 间接触及\n3. **Likert power 不足作为替代解释**（我的 Q5 = R1 的 Q3）：两位 reviewer 独立得出\n4. **Framing bias**（我的 W6 = R1 的 W8）：一致指出\n\nR1 补充了我未充分展开的几个重要技术点：NLI gate 验证不充分（W1）、GEE OR shrinkage（W3）、evaluator-producer overlap（W4）。这些加强了对方法论 soundness 的关切。\n\n两位 reviewer 的共同判断：论文方法论设计用心但多个关键统计论证存在 gap，核心 claim 强度超出证据支撑，Borderline Conference（3.5）。",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1117 · 2026-05-23T06:52:18.054961+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3668
}
```

</details>

---


### Assistant

_source line 1118 · 2026-05-23T06:52:26.185474+00:00_

交叉回应已提交。

对 R1 的 8 个 Weakness 中 7 个 [AGREE]、1 个 [REBUT]（W6: 100-point Likert 单 judge 测试——作为 proof-of-concept 足够）；6 个 Question 中 5 个 [AGREE]、1 个 [REBUT]（Q6: Holm-Bonferroni margin 已在 Appendix S 报告）。

两位 reviewer 独立收敛的核心问题：TOST underpowered、Likert power 不足作为替代解释、framing bias。综合判断维持 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 35

## Round 35

82 recorded events


### User

_source line 1119 · 2026-05-23T08:52:10.575185+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查**新颖性、完整性、写作质量、Related Work**。

## 论文信息
- **标题**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation
- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）
- **投稿类别**: ARR Long Paper
- **截止日期**: 2026-05-25
- **页数限制**: 正文 8 页 + 无限 references。Limitations 不计页。
- **模板**: ACL template（\usepackage[review]{acl}）
- **匿名规则**: Double-blind
- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex
- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/submitted.pdf

## EMNLP 2026 评分标准
5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit

## 你的审查侧重

重点审查以下方面，按优先级排列：

1. **新颖性评估**：Likert Blindspot 是 Thurstone (1927) 以来心理测量学已知的 measurement sensitivity gap 在 LLM judge 领域的 domain transfer。论文声称的 3 个 LLM-specific distinctions（per-axis structure、GEE source decomposition、binary divergence pattern）是否构成足够的增量贡献？GEE conditional decomposition 是否是真正的方法论创新？与 RATE (Reber et al., 2025)、CASSE (2026)、FairJudge (2026) 的差异化是否清晰？
2. **Claims vs Evidence 对齐**：Abstract/Intro 的 claims 是否被实验充分支撑？"consistently divergent" 基于 2 个轴 + 1 个 exploratory 轴是否过强？"across four judges" 是否遗漏了 Gemini 的较弱效应？Title "Blindspot" 是否预设了 Likert attenuation 解释而忽视了 construct divergence/pairwise amplification？
3. **写作质量**：信息密度是否合理（8 页正文承载 4 judges × 3 axes × 3 benchmarks + GEE + TOST + Bayesian 的复杂设计）？叙事流是否清晰？术语一致性？图表设计是否有效传达关键发现？
4. **Related Work 覆盖**：是否遗漏重要相关工作？特别关注 2025-2026 年的 LLM judge bias 工作、measurement theory 工作、interventional text analysis 工作。引用是否真实（非幻觉）？
5. **Limitations 章节**：是否充分讨论了关键局限？是否存在未提及的重要限制？
6. **格式合规**：是否符合 EMNLP 2026 / ARR 的格式要求？匿名是否到位？页数是否合规？

请给出完整审稿报告，包含 Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Overall Assessment（评分 + 置信度）。

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

_source line 1120 · 2026-05-23T08:52:19.605708+00:00_

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

_source line 1121 · 2026-05-23T08:52:19.656777+00:00_



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

_source line 1122 · 2026-05-23T08:52:23.426544+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
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
    "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
  }
}
```

</details>

---


### Tool call

_source line 1123 · 2026-05-23T08:52:25.786564+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/submitted.pdf",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/submitted.pdf",
    "pages": "1-8",
    "project": "causal_style_decomp_judge",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1124 · 2026-05-23T08:52:26.490055+00:00_

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

_source line 1125 · 2026-05-23T08:52:30.057080+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found information about ACL ARR 2026 reviewer guidelines and review form. Here are the key findings:

## Review Form Criteria and Dimensions

For Findings papers, the main criteria are soundness and reproducibility, while conference recomme
…[truncated 1123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6630
}
```

</details>

---


### Tool result

_source line 1126 · 2026-05-23T08:52:31.060818+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 457.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 574.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 546.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.5}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 536.0}], \"total_pages\": 21, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/a
…[truncated 77 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5274
}
```

</details>

---


### Tool result

_source line 1127 · 2026-05-23T08:52:31.061443+00:00_

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
…[truncated 5114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4571
}
```

</details>

---


### Tool call

_source line 1128 · 2026-05-23T08:52:41.563748+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p1.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1129 · 2026-05-23T08:52:42.065818+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p2.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1130 · 2026-05-23T08:52:42.972843+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool result

_source line 1131 · 2026-05-23T08:52:42.973564+00:00_



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

_source line 1132 · 2026-05-23T08:52:43.124408+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p3.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1133 · 2026-05-23T08:52:43.476013+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p4.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1134 · 2026-05-23T08:52:43.930107+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 1135 · 2026-05-23T08:52:44.131191+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p5.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1136 · 2026-05-23T08:52:44.834792+00:00_



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

_source line 1137 · 2026-05-23T08:52:44.835468+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 1138 · 2026-05-23T08:52:44.885881+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p6.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1139 · 2026-05-23T08:52:45.387527+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p7.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1140 · 2026-05-23T08:52:45.792575+00:00_



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

_source line 1141 · 2026-05-23T08:52:45.793021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p8.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1142 · 2026-05-23T08:52:46.697363+00:00_



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

_source line 1143 · 2026-05-23T08:52:46.698100+00:00_



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

_source line 1144 · 2026-05-23T08:52:46.698313+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form 2026 soundness excitement reproducibility overall assessment dimensions"
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
    "query": "ACL Rolling Review review form 2026 soundness excitement reproducibility overall assessment dimensions"
  }
}
```

</details>

---


### Tool result

_source line 1145 · 2026-05-23T08:52:54.234087+00:00_

Web search results for query: "ACL Rolling Review review form 2026 soundness excitement reproducibility overall assessment dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/anthology-files/anthology-files/anthology-files/report.pdf"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) review form and assessment dimensions for 2026:

## Review Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness
This dimension assesses whether the paper is sufficiently sound and thorough, and whether it clearly states scientific claims and provides adequate support for them. The soundness scores must be justified by the text of the review.

### Excitement
The excitement score is orthogonal to the assessment of the soundness of the paper and captures subjective prefere
…[truncated 599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7535
}
```

</details>

---


### Tool call

_source line 1146 · 2026-05-23T08:53:01.543071+00:00_

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

_source line 1147 · 2026-05-23T08:53:01.594023+00:00_



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

_source line 1148 · 2026-05-23T08:53:06.665446+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and detailed descriptions. Include soundness, excitement, overall assessment, reproducibility, and any other dimensions. Also extract the exact score descriptions for each level."
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
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and detailed descriptions. Include soundness, excitement, overall assessment, reproducibility, and any other dimensions. Also extract the exact score descriptions for each level."
  }
}
```

</details>

---


### Tool call

_source line 1149 · 2026-05-23T08:53:09.226442+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/submitted.pdf",
  "pages": "9-20",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/submitted.pdf",
    "pages": "9-20",
    "project": "causal_style_decomp_judge",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1150 · 2026-05-23T08:53:12.488063+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully..."
- **4**: "Quite sure. I tried to check the important points carefully..."
- **3**: "Pretty sure, but there's a chance I missed something..."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed..."
- **1**: "Not my area, or paper is very hard to understand..."

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen..."
- **4**: "Strong: This study provides sufficient support for all claims..."
- **3**: "Acceptable: This study provides sufficient support for main claims..."
- **2**: "Poor: Some main claims are not sufficiently supported..."
- **1**: "Major Issues: This study is not yet sufficiently thorough..."

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others..."
- **4**: "Exciting: I would mention this paper to others..."
- **3**: "Interesting: I might mention some points of this paper..."
- **2**: "Potentially Interesting: this paper does not resonate with me..."
- **1**: "Not Exciting: this paper does not resonate with me..."

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: "Consider for Award"
- **4**: "Conference"
- **3**: "Findings"
- **2**: "Resubmit next cycle"
- **1**: "Do not resubmit"

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results..."
- **4**: "They could mostly reproduce the results..."
- **3**: "They could reproduce with some difficulty..."
- **2**: "They would be hard pressed to reproduce..."
- **1**: "They would not be able to reproduce..."

## 6. **Datasets & Software**
Scale: 1-5 each
- **5**: "Enabling"
- **4**: "Useful"
- **3**: "Potentially useful"
- **2**: "Documentary"
- **1**: "No usable materials"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5822
}
```

</details>

---


### Tool result

_source line 1151 · 2026-05-23T08:53:13.792525+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 547.3}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 535.1}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 435.6}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 457.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.8}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 457.0}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.3}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images
…[truncated 992 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4566
}
```

</details>

---


### Tool call

_source line 1152 · 2026-05-23T08:53:19.163442+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p9.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1153 · 2026-05-23T08:53:20.068635+00:00_



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

_source line 1154 · 2026-05-23T08:53:20.169357+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p10.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 1155 · 2026-05-23T08:53:20.572078+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p11.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1156 · 2026-05-23T08:53:21.028192+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool call

_source line 1157 · 2026-05-23T08:53:21.028683+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p12.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1158 · 2026-05-23T08:53:21.983098+00:00_



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

_source line 1159 · 2026-05-23T08:53:21.984163+00:00_



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

_source line 1160 · 2026-05-23T08:53:21.986571+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p13.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1161 · 2026-05-23T08:53:22.441719+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p14.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 1162 · 2026-05-23T08:53:23.144460+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p15.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1163 · 2026-05-23T08:53:23.448086+00:00_



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

_source line 1164 · 2026-05-23T08:53:23.499458+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p16.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1165 · 2026-05-23T08:53:23.951867+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1510
}
```

</details>

---


### Tool result

_source line 1166 · 2026-05-23T08:53:24.506560+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1362
}
```

</details>

---


### Tool result

_source line 1167 · 2026-05-23T08:53:24.708512+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1209
}
```

</details>

---


### Tool call

_source line 1168 · 2026-05-23T08:53:31.736817+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p17.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1169 · 2026-05-23T08:53:32.390136+00:00_



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


### Tool call

_source line 1170 · 2026-05-23T08:53:32.390610+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p18.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 1171 · 2026-05-23T08:53:32.742319+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p19.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1172 · 2026-05-23T08:53:34.047555+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1656
}
```

</details>

---


### Tool result

_source line 1173 · 2026-05-23T08:53:34.048429+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1306
}
```

</details>

---


### Tool call

_source line 1174 · 2026-05-23T08:53:34.098820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p20.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 1175 · 2026-05-23T08:53:34.650831+00:00_



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

_source line 1176 · 2026-05-23T08:53:35.052003+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/submitted.pdf",
  "pages": "21",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/submitted.pdf",
    "pages": "21",
    "project": "causal_style_decomp_judge",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1177 · 2026-05-23T08:53:35.153548+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 187.0}], \"total_pages\": 21, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1178 · 2026-05-23T08:53:38.416687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p21.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 1179 · 2026-05-23T08:53:38.768848+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1180 · 2026-05-23T08:53:44.095872+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
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
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1181 · 2026-05-23T08:53:44.196604+00:00_

No files found

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

_source line 1182 · 2026-05-23T08:53:46.861391+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
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
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1183 · 2026-05-23T08:53:46.911995+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1184 · 2026-05-23T08:53:49.776719+00:00_

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

_source line 1185 · 2026-05-23T08:53:50.229001+00:00_

1	\begin{abstract}
2	Likert and pairwise scoring produce consistently divergent sensitivity across tested surface-level style axes when applied to LLM judges.
3	We introduce Controlled Style Decomposition (CSD), a black-box diagnostic methodology that quantifies this divergence under controlled conditions via human-validated, NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison.
4	Across four judges from independent providers, one low-sensitivity reference, and two primary axes (formality, verbosity), the divergence is robust: pairwise reaches significance ($p < 0.001$) where Likert does not ($p > 0.17$), with signal loss exceeding 60\% at stronger effects---replicated across three benchmarks and confirmed by seven statistical methods.
5	GEE conditional decomposition reveals qualitatively distinct per-axis confound structures: verbosity bias is style-dominated (Style OR $8$--$13$, Originality OR ${<}1$), while formality reflects a conditional effect where style and content quality contribute jointly---determining which pairwise estimates are directly interpretable and which require decomposition.
6	A low-sensitivity reference judge shows substantially weaker divergence on both primary axes (BT 55\% vs.\ 63--77\%), supporting discriminative validity.
7	This divergence admits three non-exclusive explanations---measurement attenuation, format amplification, or construct divergence---that our controlled design bounds but cannot definitively adjudicate; the practical consequence is unambiguous: Likert-only audits may fail to surface style-driven preferences that propagate through pairwise-based alignment pipelines.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1186 · 2026-05-23T08:53:50.229465+00:00_

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

_source line 1187 · 2026-05-23T08:53:50.681550+00:00_

1	\section{Introduction}
2	
3	\emph{``What is the average height for a male?''} --- given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \emph{higher} on a 1--10 Likert scale (8 vs.\ 5), yet consistently selects the formal variant in pairwise comparison.
4	Same judge, same texts, opposite conclusions.
5	We term this the \emph{Likert Blindspot}---an operational descriptor for the measurement-mode divergence where pairwise comparison detects statistically significant style sensitivity that Likert scoring fails to detect on the same data, without committing to a specific causal mechanism.
6	This divergence admits multiple non-exclusive explanations---Likert measurement attenuation, pairwise format amplification \citep{jeong2025comparative}, or construct-level differences between absolute and comparative evaluation---which our controlled design bounds but cannot definitively adjudicate (\S\ref{sec:likert_pairwise}).
7	Under construct divergence, pairwise and Likert modes may measure distinct constructs---comparative sensitivity versus absolute quality judgment---in which case the divergence reflects measurement scope rather than measurement failure, with different practical implications for audit design (\S\ref{sec:likert_pairwise}).
8	This example reflects a consistent pattern: surface-level style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}, with 76--92\% of preferences originating from style cues \citep{li2026preference,soumik2026judging}.
9	
10	LLM judges are central infrastructure for NLP evaluation and alignment training (RLHF, DPO), where judge preferences serve as reward signals; any systematic bias propagates through both evaluation leaderboards and model development pipelines.
11	Despite this, existing approaches address individual requirements (multi-dimensional style analysis \citep{casse2026concise,wang2026fairjudge}, interventional design \cit
…[truncated 3681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1188 · 2026-05-23T08:53:50.732091+00:00_

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

_source line 1189 · 2026-05-23T08:53:51.283833+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Two lines of work motivate our approach: interventional methods for diagnosing judge bias, and measurement theory on the sensitivity of different elicitation formats.
5	
6	\paragraph{Interventional Approaches to Judge Bias}
7	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
8	\citet{reber2025rate} propose RATE, a framework that rewrites model outputs along style attributes using imperfect counterfactuals and measures the causal effect on reward model scores via Likert-scale Average Treatment Effect (ATE).
9	RATE applies a correction term to account for rewriting imperfections, but its reliance on Likert ATE as the primary metric is a vulnerability: our experiments show that Likert scoring exhibits a ceiling effect in which 60\% of style-transformed pairs receive identical integer scores, yielding non-significant ATE estimates ($p = 0.332$) for the same interventions that pairwise comparison detects at $p = 0.006$.
10	Whether this format sensitivity extends to RATE's broader attribute space is an open question; our results motivate independent validation of Likert-based effect estimates alongside pairwise measures.
11	CSD differs from RATE in three respects: it targets individual style axes rather than general attributes, it measures bias through position-controlled pairwise comparison rather than Likert ATE, and it enforces content preservation via NLI entailment gating rather than post-hoc correction for imperfect rewrites.
12	\citet{counterfactual2025rhetorical} also adopt an interventional LLM-based design, rewriting texts to measure rhetorical style effects and aggregating preferences with a Bradley-Terry model.
13	Their framework operates at persona-level granularity (e.g., ``writes like a professor''), whereas CSD intervenes on specific style axes (e.g., formality, conciseness) and uses a sign test with position control r
…[truncated 6499 chars]

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

_source line 1190 · 2026-05-23T08:53:51.284173+00:00_

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

_source line 1191 · 2026-05-23T08:53:51.334730+00:00_

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
18	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large fine-tuned on MNLI \citep{williams2018broad} with an entailment threshold of 0.90, selected as the threshold above which NLI performance plateaus (Appendix~\ref{app:nli_sweep}).
19	For axes that preserve information density (formality, register), we apply standard bidirectional entailment: both NLI(original $\to$ rewrite) and NLI(rewrite $\to$ original) must exc
…[truncated 5426 chars]

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

_source line 1192 · 2026-05-23T08:53:56.708527+00:00_

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

_source line 1193 · 2026-05-23T08:53:57.281437+00:00_

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
11	Exploratory analyses use uncorrected $p$-values; confirmatory analyses (pipeline validity) are evaluated at $\alpha = 0.05$ without additional correction.
12	Bradley-Terry parameters \citep{bradley1952rank,luce1959individual} are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the default regularization of the \texttt{choix} Python library.
13	In binary-choice BT models, IIA is structurally satisfied; the direction asymmetry in Appendix~\ref{app:bt_gof} (formality: formal-origin 88.9\% vs.\ casual-origin 52.6\%, Fisher $p = 0.015$) reflects heterogeneous treatment effects rather than IIA violation.
14	All bootstrap confidence intervals are percentile CIs from 10{,}000 pair-level resamples with seed 42.
15	GEE models use exchangeable working correlation with sandwich standard errors (robust to correlation misspecification), justified by near-zero estimated within-pair correlations ($\hat{\alpha} \in [-0.25, +0.11]$; Appendix~\ref{app:gee_diagnostics}).
16	
17	\paragraph{Model selection.}
18	Target judges span four architectures: GPT-4o (2024-08-06), Qwen3-32B-Instruct (also serving as rewriter), Llama-3.3-70B-Instruct, 
…[truncated 15637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 572
}
```

</details>

---


### Tool call

_source line 1194 · 2026-05-23T08:53:57.336149+00:00_

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

_source line 1195 · 2026-05-23T08:53:57.336630+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	CSD yields two findings.
5	First, the \emph{Likert Blindspot}: pairwise comparison and Likert scoring produce consistently divergent verdicts---complete divergence at moderate bias ($d \to 0$ at $n = 355$), ${>}60\%$ signal loss at stronger effects---confirmed across four judges, three benchmarks, and seven statistical methods.
6	Second, GEE conditional decomposition reveals qualitatively distinct per-axis confound structures---verbosity is style-dominated, formality is a conditional effect, register is judge-dependent---disambiguating cases where aggregate preference reflects quality detection rather than style sensitivity.
7	Regardless of mechanism, single-format audits risk systematic blind spots; human ground-truth validation of both modes is the key next step.
8	

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

_source line 1196 · 2026-05-23T08:57:51.657548+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿报告\n\n**论文**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审查侧重**: 新颖性、完整性、写作质量、Related Work\n\n---\n\n## 总体评分\n**Overall Assessment**: 3.5 / 5 — Borderline Conference\n**Confidence**: 4 / 5 — Quite sure; I checked the important points carefully.\n**一句话总结**: 执行质量出色的实证研究，但核心发现（pairwise 比 Likert 对风格更敏感）在心理测量学中已被充分确立，LLM-specific 的增量贡献虽然存在但不够显著，且无法区分 attenuation 和 amplification 这一根本限制削弱了实际指导价值。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4 / 5 | 方法论严谨，六项实验控制、七种统计方法、跨 benchmark 复制，GEE 分解有诊断价值。但无法区分 attenuation 与 amplification（作者承认），且核心结论依赖 n=100 的 LLMBar 数据集。 |\n| Excitement | 3 / 5 | 对 LLM 评估社区有实用价值，但核心 insight（pairwise > rating for sensitivity）是 Thurstone (1927) 以来的经典结论。GEE per-axis decomposition 是最具新意的部分，但属于标准统计工具的领域应用。 |\n| Reproducibility | 4 / 5 | 方法描述详尽，统计框架清晰，附录提供模型参数和 prompt。承诺接收后释放代码和数据。 |\n| Overall | 3.5 / 5 | Borderline Conference — 执行达到会议水准，但新颖性不足以明确推荐主会议。适合 Findings。 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 新颖性定位不够诚实：核心发现是经典心理测量结论的领域迁移，三个 \"LLM-specific distinctions\" 的增量贡献被夸大\n\n- 具体位置：Section 1 (Introduction), p2 第 13 段 \"However, the LLM judge setting introduces distinctions beyond the classical framework: (a)...(b)...(c)...\"\n- 问题：论文声称的三个 LLM-specific distinctions 实际上并不构成对经典框架的本质超越：\n  - **(a) Per-axis structure**：Thurstone 的框架本身就不预测所有刺激维度具有相同的 discriminability gradient。不同 style axis 展现不同的 confound structure 是实证发现，不是方法论创新。经典 IRT 文献中 item-level discriminability variation 是标准现象。\n  - **(b) GEE source decomposition**：GEE (Liang & Zeger, 1986) 是成熟的纵向数据分析工具，将其应用于分解 style/quality 成分是合理的工程贡献，但不构成\"absent from the classical framework\"的方法论创新。经典心理测量中 factor analysis 和 structural equation modeling 长期承担类似功能。\n  - **(c) Binary divergence pattern**：所有七种 Likert 方法全部失败、所有 pairwise 方法全部成功的二元分裂，更可能反映效应量位于 Likert 的检测阈值以下（即经典 power analysis 所预测的），而非超越经典理论的新现象。论文自己的 Figure 4 power analysis 完全一致地解释了这一模式。\n- 为什么影响接收：这是论文新颖性论证的核心。如果三个 distinctions 都可以被经典框架解释，那么贡献就退化为\"在 LLM judge 上验证了已知现象\"，这对 EMNLP 主会议可能不够。\n- 建议修改方向：更诚实地定位为\"empirical characterization of a known phenomenon in a new domain\"，突出 GEE per-axis decomposition 的实用价值（这确实是有用的诊断工具），而非过度宣称方法论新颖性。将 Introduction 的 framing 从\"distinctions beyond the classical framework\"改为\"practical implications that the classical framework predicts but has not been quantified in the LLM setting\"。\n\n**N2** [critical] \"Consistently divergent\" claim 过强——基于 2 个主要轴 + 1 个 exploratory 轴，且 Gemini 效应显著弱于其他三个 judge\n\n- 具体位置：Abstract 第 1 句 \"consistently divergent sensitivity across tested surface-level style axes\"；Section 5.3 (p6-8)\n- 问题：\n  - \"consistently\" 的证据基础是 2 个 primary axes（formality, verbosity）+ 1 个 exploratory axis（register）。其中 register 明确标注为 exploratory，且 evaluator-producer overlap 最高（Limitations, p9）。如果排除 register，结论基于 2 个轴，这对\"consistently across axes\"的概括力有限。\n  - Gemini-2.5-Flash 的 formality 效应明显弱于其他三个 judge：Style OR 1.64 (n.s.)，BT 仅 57.4%（Table 1, Table 2）。Abstract 称 \"four judges from independent providers\" 但未提及 Gemini 的异质性。虽然 Section 5.3 第 150 行有提及 \"a weaker, originality-dominated formality pattern\"，但 Abstract 和 Conclusion 的措辞给人的印象是四个 judge 表现一致。\n  - 更根本的问题：论文选择了 formality 和 verbosity 这两个*已知*最容易产生 style bias 的轴（引用 Wu & Aji 2025; Saito et al. 2023），这是否存在 axis selection bias？在\"最容易\"产生偏差的轴上观察到偏差，说服力有限。Limitations p9 提到 tone axis pilot 因 NLI gate 拒绝率高达 55% 而失败——如果 CSD 只能处理 surface-level 轴，那么\"across style axes\"的概括性声明需要更大折扣。\n- 为什么影响接收：直接关系到论文核心 claim 的可信度。\n- 建议修改方向：将 Abstract 修改为\"across two primary and one exploratory style axes, with varying effect sizes across judges\"；在 Abstract/Conclusion 中明确提及 Gemini 的较弱效应；讨论 axis selection 的潜在偏差。\n\n**N3** [critical] Title \"Blindspot\" 预设了 Likert attenuation 解释，与论文自身承认的三种竞争解释不一致\n\n- 具体位置：Title; Section 5.1 §85-92 (三种解释的讨论)\n- 问题：\"Blindspot\"一词的语义预设是 Likert *遗漏*了真实存在的信号（即 attenuation 解释）。但论文明确承认三种非排他性解释：(a) Likert attenuation, (b) pairwise amplification, (c) construct divergence。在 (b) 下，pairwise 放大了微弱偏好；在 (c) 下，两种模式测量不同构念。这两种解释下，\"Blindspot\" 的比喻都不准确——Likert 没有\"盲点\"，它只是在测量一个不同的东西，或者 pairwise 在放大噪声。\n\n  论文在 Section 5.1 第 86-92 行做了详细讨论，但 Title/Abstract/Conclusion 的 framing 仍然偏向 attenuation 解释。特别是 Conclusion (Section 6, p8) 的表述 \"Likert-only audits may fail to surface style-driven preferences\" 暗示 pairwise 检测到的是\"真实的\" preferences，这仍然是在预设 attenuation。\n\n- 为什么影响接收：标题是论文最重要的 framing 决策。如果标题的隐含假设与论文自身的 nuanced discussion 矛盾，会引起 reviewer 和读者的不信任。\n- 建议修改方向：考虑更中性的标题，如 \"Measurement-Mode Divergence in LLM Judge Style Evaluation\" 或 \"The Likert-Pairwise Gap\"。或在 Abstract 中更早、更显著地承认 amplification 和 construct divergence 解释，使读者不会从标题获得单一方向的印象。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] GEE conditional decomposition 的解释力取决于 confounders 的完整性，但论文未讨论 omitted variable bias\n\n- 具体位置：Section 5.2 (p7), Table 2\n- 问题：GEE 模型仅包含两个 predictors（Style direction, Originality）。如果存在其他影响 judge 偏好的变量（如文本长度、难度、任务类型）且与 style 相关，则 Style OR 估计会有 omitted variable bias。虽然 Appendix T 有 cross-axis contamination analysis，Appendix 提到了 FK grade 和 sentence length 的控制，但主文中对 GEE 模型的完整性假设缺乏讨论。\n- 建议：在 Section 5.2 或 Limitations 中明确列出 GEE 模型的识别假设和可能遗漏的 confounders。\n\n**W2** [warning] Claude Sonnet 4 作为 low-sensitivity reference 的验证不够充分\n\n- 具体位置：Section 5.1 §88; Appendix H\n- 问题：Claude 被用作\"low-sensitivity reference\"来支持 Blindspot 的 discriminative validity，但这一角色缺乏 a priori justification。论文的逻辑是事后的：\"Claude 效应弱 → Claude 是 reference → Blindspot 有 discriminative validity\"。这存在循环论证风险。此外：\n  - Pooled TOST 在 Δ=10pp 处不显著（p > .05），仅在 Δ=12pp 处显著（p = .035）——equivalence margin 的选择缺乏先验依据\n  - Bayesian BF₀₁ = 0.80 是 inconclusive，不支持也不反对 null\n  - AEval verbosity Style OR = 4.76 (p < .001) 表明 Claude 并非在所有条件下都是 low-sensitivity\n- 建议：承认 Claude 作为 reference 的选择是 post-hoc 的；提供 equivalence margin 的先验理据；在讨论中降低对 Claude reference 论证的权重。\n\n**W3** [warning] 信息密度过高——8 页正文承载了过多实验维度，核心 narrative 被稀释\n\n- 具体位置：全文\n- 问题：正文需要传达 4 judges × 3 axes × 3 benchmarks + GEE + TOST + Bayesian + 7 种统计方法 + power analysis + Claude reference + rewriter independence。虽然 13 页附录帮助卸载了细节，但主文仍然在每个段落中压缩了大量数字和统计结果。例如 Section 5.1 (p6) 一个段落中包含了 TOST p-values、GEE Style ORs、GPT-4o 对照、Bayesian BF₀₁，读者需要同时 track 多个统计框架的结果。这降低了可读性和核心信息的传达效率。\n- 建议：考虑将 7 种统计方法比较、Claude TOST、Bayesian equivalence 全部移至附录，主文聚焦于 BT + GEE 的核心结果，释放空间加强 narrative coherence。\n\n**W4** [warning] 主要分析使用 LLMBar (n=100)，样本量对 GEE 估计的 small-sample bias 可能严重\n\n- 具体位置：Section 3.4, Section 5.2 (p7 \"Sample-size sensitivity\")\n- 问题：论文坦诚承认 n=88 的 GEE OR 存在 small-sample upward bias（Qwen3 formality Style OR 从 4.20 降至 2.15，~49% shrinkage at n=355）。这个 shrinkage 幅度非常大。但其他 judges 和 verbosity 轴没有 n=355 的验证——我们无法确定 verbosity Style OR 8-13 在更大样本上是否也会缩水 ~50%。论文在 p7 说\"Verbosity Style ORs (8-13) would remain style-dominated even under ~50% shrinkage (projected 4-6.5)\"，但这是推测而非实证。\n- 建议：明确标注 n=88 结果的 point estimates 可能存在 substantial upward bias，在 Table 2 caption 中加入此 caveat；在跨 benchmark 复制中对 verbosity 进行 n=355 级别的验证。\n\n**W5** [warning] 与 Comparative Trap (Jeong et al., 2025) 的关系处理不够充分\n\n- 具体位置：Section 5.4 §173-175; Section 2 §37\n- 问题：Jeong et al. (2025) 直接挑战了本文的核心前提——pairwise comparison amplifies style biases relative to pointwise scoring。论文用六个 controls 来 bound amplification risk，但这些 controls 不能排除 amplification，只能限制其幅度。更关键的是，论文没有量化 amplification factor 的可能范围。Section 5.4 列出的六个 controls 中：\n  - (i) NLI ablation 只证明 NLI gate 有效，不涉及 format amplification\n  - (ii) Claude reference 本身验证不足（见 W2）\n  - (iii-vi) 间接证据，不直接测量 amplification magnitude\n  Limitations p8 承认 \"we cannot quantify it precisely without a ground-truth bias magnitude\"——这个承认应该在主文中更加突出。\n- 建议：在 Section 5.4 中量化 amplification 的可能范围（即使是 rough bounds），或更明确地讨论如果 amplification factor 大于某个值，核心结论如何改变。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 1 的 footnote 解释系统在表格底部挤在一起，建议用更清晰的 legend 格式。特别是 $\\dagger$ / $\\dagger_e$ / $\\dagger_c$ / --- 的含义需要更直观的说明。\n- **M2**: Figure 2 (DAG) 中的 dashed orange $S \\to Q$ path 标注 \"residual confound.\" 字体太小，不易辨认。\n- **M3**: Section 2 Related Work 的 \"Mode-specific biases in LLM judges\" 段落（p4 §44-46）提出了一个有趣但未被充分发展的论点（RLHF 训练造成的 format-specific biases），建议在主文或附录中提供更多证据。\n- **M4**: Abstract 第 4 句 \"GEE conditional decomposition reveals qualitatively distinct per-axis confound structures\" 对不熟悉 GEE 的读者不够友好，建议用更直观的语言描述。\n- **M5**: \"Code and Data will be released upon acceptance\" — 建议提供匿名 repository 或至少在 supplementary material 中包含核心代码以提高可复现性。\n- **M6**: Section 3.1 (p4) 提到 temperature 0.7 用于 rewriting，但未说明选择依据。\n- **M7**: Limitations 中 \"tone axis pilot\" 的结果（NLI gate 拒绝 55%）很有信息量，但与正文的连接不够紧密——建议在 Method 或 Experiments 中简要提及 CSD 的 scope boundary。\n\n---\n\n## Questions to Authors\n\n1. 如果 pairwise amplification 是主要机制（而非 Likert attenuation），那么你们的方法学建议会如何改变？目前 Conclusion 的\"single-format audits risk systematic blind spots\"暗示应该添加 pairwise 模式，但如果 pairwise 是在放大微弱偏好，添加它反而会引入 false positives。请讨论在 amplification-dominant 情景下的 practical implications。\n\n2. 为什么不包含 human evaluation 来 ground-truth 两种测量模式？论文多次提到这是\"the key next step\"（Conclusion p8, Limitations p8），但对于一篇旨在区分两种测量模式的论文，缺乏人工评估数据是一个显著的方法论空缺。\n\n3. Qwen3-32B 在 formality Style OR 从 4.20 (n=88) 降至 2.15 (n=355)，~49% shrinkage。如果对 verbosity 进行同样的 scaling，Style OR 可能从 13.10 降至 ~6.5。这仍然 >1，但你们如何确保 small-sample bias 不会改变 Table 2 中其他 judges 的 regime classification？\n\n4. Cross-axis contamination analysis (Appendix T, p16) 报告 formality rewrites 产生 negligible sentence structure changes (|d| < 0.03)，但 verbosity rewrites 的 Flesch-Kincaid grade 有 elevated shift (d = 0.50, Table 21)。这是否意味着 verbosity 的 \"style bias\" 部分是 readability bias？FK grade 的 60% mediation by sentence length (p7) 进一步暗示了这一点。\n\n---\n\n## Missing References（可能遗漏的相关工作）\n\n1. **Gladkoff et al. (2024/2025)** — 关于 LLM judge 评分校准 (calibration) 的工作，与 Likert scale 的 ceiling effect 讨论相关。\n2. **Kocmi & Federmann (2023)** — GEMBA: Using GPT Models for Reference-Free MT Evaluation，涉及 LLM judge 在 Likert vs pairwise 上的比较。\n3. 论文引用了大量 2025-2026 年工作（RATE, CASSE, FairJudge, Comparative Trap, Preference Leakage），coverage 整体较好。建议确认 Reber et al. (2025) RATE 和 Jeong et al. (2025) Comparative Trap 的引用信息是否准确（arxiv preprint 可能已被接收并需要更新引用格式）。\n\n---\n\n## 主要优势\n\n1. **实验设计极其严谨**：六项实验控制（NLI ablation、Claude reference、cross-axis variation、rewriting artifact、debiased prompting、four-architecture replication）、七种统计方法、三个 benchmark 的交叉验证。这是 LLM judge bias 文献中方法论最严谨的工作之一。\n2. **GEE per-axis decomposition 有实用诊断价值**：分离 style-specific 和 quality-correlated components 的能力对评估 pipeline 的实际审计有直接用途。Verbosity 的 style-dominated 模式与 formality 的 conditional 模式的对比是真正有信息量的发现。\n3. **Limitations 章节极其诚实和全面**：讨论了 quality-style confounding、evaluator-producer bias、scope boundaries、validation methodology 等关键局限，几乎没有 reviewer 需要补充的未提及限制。这在 NLP 论文中非常少见。\n4. **Related Work 覆盖全面**：从经典心理测量学到最新 LLM judge bias 工作，引用覆盖面广且组织有序。与 RATE 和 Comparative Trap 的差异化讨论清晰。\n5. **统计方法论透明**：FWER 控制、exploratory vs confirmatory 分类、bootstrap CI 的计算细节都有详细说明。GEE 模型诊断（附录 D）提供了 correlation structure robustness 和 interaction tests。\n6. **Cross-benchmark replication** 加强了结果的 generalizability，三个 benchmark (LLMBar, AlpacaEval, MT-Bench) 覆盖不同的 evaluation scenarios。\n\n---\n\n## 总结\n\n这是一篇**执行质量非常高**的实证论文，方法论严谨程度在 LLM judge bias 文献中属于上乘。主要弱点在于**新颖性**：核心发现（pairwise 比 Likert 更敏感于 style differences）是心理测量学的经典结论，论文声称的三个 \"LLM-specific distinctions\" 不足以构成对经典框架的本质超越。此外，**无法区分 attenuation 和 amplification** 这一根本限制——尽管论文坦诚讨论——削弱了 practical implications 的确定性。标题 \"Blindspot\" 与论文自身承认的多种解释之间存在张力。\n\n推荐 **3.5 (Borderline Conference)**，执行质量支持主会议接收，但新颖性不足可能使其更适合 Findings track。如果作者在 rebuttal 中能够 (1) 更诚实地定位新颖性（实证 characterization 而非方法论创新），(2) 提供 human evaluation 数据或至少 pilot 结果来区分 attenuation 和 amplification，评分可能提升至 4.0。",
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
    "text": "## Reviewer 2 审稿报告\n\n**论文**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审查侧重**: 新颖性、完整性、写作质量、Related Work\n\n---\n\n## 总体评分\n**Overall Assessment**: 3.5 / 5 — Borderline Conference\n**Confidence**: 4 / 5 — Quite sure; I checked the important points carefully.\n**一句话总结**: 执行质量出色的实证研究，但核心发现（pairwise 比 Likert 对风格更敏感）在心理测量学中已被充分确立，LLM-specific 的增量贡献虽然存在但不够显著，且无法区分 attenuation 和 amplification 这一根本限制削弱了实际指导价值。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4 / 5 | 方法论严谨，六项实验控制、七种统计方法、跨 benchmark 复制，GEE 分解有诊断价值。但无法区分 attenuation 与 amplification（作者承认），且核心结论依赖 n=100 的 LLMBar 数据集。 |\n| Excitement | 3 / 5 | 对 LLM 评估社区有实用价值，但核心 insight（pairwise > rating for sensitivity）是 Thurstone (1927) 以来的经典结论。GEE per-axis decomposition 是最具新意的部分，但属于标准统计工具的领域应用。 |\n| Reproducibility | 4 / 5 | 方法描述详尽，统计框架清晰，附录提供模型参数和 prompt。承诺接收后释放代码和数据。 |\n| Overall | 3.5 / 5 | Borderline Conference — 执行达到会议水准，但新颖性不足以明确推荐主会议。适合 Findings。 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 新颖性定位不够诚实：核心发现是经典心理测量结论的领域迁移，三个 \"LLM-specific distinctions\" 的增量贡献被夸大\n\n- 具体位置：Section 1 (Introduction), p2 第 13 段 \"However, the LLM judge setting introduces distinctions beyond the classical framework: (a)...(b)...(c)...\"\n- 问题：论文声称的三个 LLM-specific distinctions 实际上并不构成对经典框架的本质超越：\n  - **(a) Per-axis structure**：Thurstone 的框架本身就不预测所有刺激维度具有相同的 discriminability gradient。不同 style axis 展现不同的 confound structure 是实证发现，不是方法论创新。经典 IRT 文献中 item-level discriminability variation 是标准现象。\n  - **(b) GEE source decomposition**：GEE (Liang & Zeger, 1986) 是成熟的纵向数据分析工具，将其应用于分解 style/quality 成分是合理的工程贡献，但不构成\"absent from the classical framework\"的方法论创新。经典心理测量中 factor analysis 和 structural equation modeling 长期承担类似功能。\n  - **(c) Binary divergence pattern**：所有七种 Likert 方法全部失败、所有 pairwise 方法全部成功的二元分裂，更可能反映效应量位于 Likert 的检测阈值以下（即经典 power analysis 所预测的），而非超越经典理论的新现象。论文自己的 Figure 4 power analysis 完全一致地解释了这一模式。\n- 为什么影响接收：这是论文新颖性论证的核心。如果三个 distinctions 都可以被经典框架解释，那么贡献就退化为\"在 LLM judge 上验证了已知现象\"，这对 EMNLP 主会议可能不够。\n- 建议修改方向：更诚实地定位为\"empirical characterization of a known phenomenon in a new domain\"，突出 GEE per-axis decomposition 的实用价值（这确实是有用的诊断工具），而非过度宣称方法论新颖性。将 Introduction 的 framing 从\"distinctions beyond the classical framework\"改为\"practical implications that the classical framework predicts but has not been quantified in the LLM setting\"。\n\n**N2** [critical] \"Consistently divergent\" claim 过强——基于 2 个主要轴 + 1 个 exploratory 轴，且 Gemini 效应显著弱于其他三个 judge\n\n- 具体位置：Abstract 第 1 句 \"consistently divergent sensitivity across tested surface-level style axes\"；Section 5.3 (p6-8)\n- 问题：\n  - \"consistently\" 的证据基础是 2 个 primary axes（formality, verbosity）+ 1 个 exploratory axis（register）。其中 register 明确标注为 exploratory，且 evaluator-producer overlap 最高（Limitations, p9）。如果排除 register，结论基于 2 个轴，这对\"consistently across axes\"的概括力有限。\n  - Gemini-2.5-Flash 的 formality 效应明显弱于其他三个 judge：Style OR 1.64 (n.s.)，BT 仅 57.4%（Table 1, Table 2）。Abstract 称 \"four judges from independent providers\" 但未提及 Gemini 的异质性。虽然 Section 5.3 第 150 行有提及 \"a weaker, originality-dominated formality pattern\"，但 Abstract 和 Conclusion 的措辞给人的印象是四个 judge 表现一致。\n  - 更根本的问题：论文选择了 formality 和 verbosity 这两个*已知*最容易产生 style bias 的轴（引用 Wu & Aji 2025; Saito et al. 2023），这是否存在 axis selection bias？在\"最容易\"产生偏差的轴上观察到偏差，说服力有限。Limitations p9 提到 tone axis pilot 因 NLI gate 拒绝率高达 55% 而失败——如果 CSD 只能处理 surface-level 轴，那么\"across style axes\"的概括性声明需要更大折扣。\n- 为什么影响接收：直接关系到论文核心 claim 的可信度。\n- 建议修改方向：将 Abstract 修改为\"across two primary and one exploratory style axes, with varying effect sizes across judges\"；在 Abstract/Conclusion 中明确提及 Gemini 的较弱效应；讨论 axis selection 的潜在偏差。\n\n**N3** [critical] Title \"Blindspot\" 预设了 Likert attenuation 解释，与论文自身承认的三种竞争解释不一致\n\n- 具体位置：Title; Section 5.1 §85-92 (三种解释的讨论)\n- 问题：\"Blindspot\"一词的语义预设是 Likert *遗漏*了真实存在的信号（即 attenuation 解释）。但论文明确承认三种非排他性解释：(a) Likert attenuation, (b) pairwise amplification, (c) construct divergence。在 (b) 下，pairwise 放大了微弱偏好；在 (c) 下，两种模式测量不同构念。这两种解释下，\"Blindspot\" 的比喻都不准确——Likert 没有\"盲点\"，它只是在测量一个不同的东西，或者 pairwise 在放大噪声。\n\n  论文在 Section 5.1 第 86-92 行做了详细讨论，但 Title/Abstract/Conclusion 的 framing 仍然偏向 attenuation 解释。特别是 Conclusion (Section 6, p8) 的表述 \"Likert-only audits may fail to surface style-driven preferences\" 暗示 pairwise 检测到的是\"真实的\" preferences，这仍然是在预设 attenuation。\n\n- 为什么影响接收：标题是论文最重要的 framing 决策。如果标题的隐含假设与论文自身的 nuanced discussion 矛盾，会引起 reviewer 和读者的不信任。\n- 建议修改方向：考虑更中性的标题，如 \"Measurement-Mode Divergence in LLM Judge Style Evaluation\" 或 \"The Likert-Pairwise Gap\"。或在 Abstract 中更早、更显著地承认 amplification 和 construct divergence 解释，使读者不会从标题获得单一方向的印象。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] GEE conditional decomposition 的解释力取决于 confounders 的完整性，但论文未讨论 omitted variable bias\n\n- 具体位置：Section 5.2 (p7), Table 2\n- 问题：GEE 模型仅包含两个 predictors（Style direction, Originality）。如果存在其他影响 judge 偏好的变量（如文本长度、难度、任务类型）且与 style 相关，则 Style OR 估计会有 omitted variable bias。虽然 Appendix T 有 cross-axis contamination analysis，Appendix 提到了 FK grade 和 sentence length 的控制，但主文中对 GEE 模型的完整性假设缺乏讨论。\n- 建议：在 Section 5.2 或 Limitations 中明确列出 GEE 模型的识别假设和可能遗漏的 confounders。\n\n**W2** [warning] Claude Sonnet 4 作为 low-sensitivity reference 的验证不够充分\n\n- 具体位置：Section 5.1 §88; Appendix H\n- 问题：Claude 被用作\"low-sensitivity reference\"来支持 Blindspot 的 discriminative validity，但这一角色缺乏 a priori justification。论文的逻辑是事后的：\"Claude 效应弱 → Claude 是 reference → Blindspot 有 discriminative validity\"。这存在循环论证风险。此外：\n  - Pooled TOST 在 Δ=10pp 处不显著（p > .05），仅在 Δ=12pp 处显著（p = .035）——equivalence margin 的选择缺乏先验依据\n  - Bayesian BF₀₁ = 0.80 是 inconclusive，不支持也不反对 null\n  - AEval verbosity Style OR = 4.76 (p < .001) 表明 Claude 并非在所有条件下都是 low-sensitivity\n- 建议：承认 Claude 作为 reference 的选择是 post-hoc 的；提供 equivalence margin 的先验理据；在讨论中降低对 Claude reference 论证的权重。\n\n**W3** [warning] 信息密度过高——8 页正文承载了过多实验维度，核心 narrative 被稀释\n\n- 具体位置：全文\n- 问题：正文需要传达 4 judges × 3 axes × 3 benchmarks + GEE + TOST + Bayesian + 7 种统计方法 + power analysis + Claude reference + rewriter independence。虽然 13 页附录帮助卸载了细节，但主文仍然在每个段落中压缩了大量数字和统计结果。例如 Section 5.1 (p6) 一个段落中包含了 TOST p-values、GEE Style ORs、GPT-4o 对照、Bayesian BF₀₁，读者需要同时 track 多个统计框架的结果。这降低了可读性和核心信息的传达效率。\n- 建议：考虑将 7 种统计方法比较、Claude TOST、Bayesian equivalence 全部移至附录，主文聚焦于 BT + GEE 的核心结果，释放空间加强 narrative coherence。\n\n**W4** [warning] 主要分析使用 LLMBar (n=100)，样本量对 GEE 估计的 small-sample bias 可能严重\n\n- 具体位置：Section 3.4, Section 5.2 (p7 \"Sample-size sensitivity\")\n- 问题：论文坦诚承认 n=88 的 GEE OR 存在 small-sample upward bias（Qwen3 formality Style OR 从 4.20 降至 2.15，~49% shrinkage at n=355）。这个 shrinkage 幅度非常大。但其他 judges 和 verbosity 轴没有 n=355 的验证——我们无法确定 verbosity Style OR 8-13 在更大样本上是否也会缩水 ~50%。论文在 p7 说\"Verbosity Style ORs (8-13) would remain style-dominated even under ~50% shrinkage (projected 4-6.5)\"，但这是推测而非实证。\n- 建议：明确标注 n=88 结果的 point estimates 可能存在 substantial upward bias，在 Table 2 caption 中加入此 caveat；在跨 benchmark 复制中对 verbosity 进行 n=355 级别的验证。\n\n**W5** [warning] 与 Comparative Trap (Jeong et al., 2025) 的关系处理不够充分\n\n- 具体位置：Section 5.4 §173-175; Section 2 §37\n- 问题：Jeong et al. (2025) 直接挑战了本文的核心前提——pairwise comparison amplifies style biases relative to pointwise scoring。论文用六个 controls 来 bound amplification risk，但这些 controls 不能排除 amplification，只能限制其幅度。更关键的是，论文没有量化 amplification factor 的可能范围。Section 5.4 列出的六个 controls 中：\n  - (i) NLI ablation 只证明 NLI gate 有效，不涉及 format amplification\n  - (ii) Claude reference 本身验证不足（见 W2）\n  - (iii-vi) 间接证据，不直接测量 amplification magnitude\n  Limitations p8 承认 \"we cannot quantify it precisely without a ground-truth bias magnitude\"——这个承认应该在主文中更加突出。\n- 建议：在 Section 5.4 中量化 amplification 的可能范围（即使是 rough bounds），或更明确地讨论如果 amplification factor 大于某个值，核心结论如何改变。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 1 的 footnote 解释系统在表格底部挤在一起，建议用更清晰的 legend 格式。特别是 $\\dagger$ / $\\dagger_e$ / $\\dagger_c$ / --- 的含义需要更直观的说明。\n- **M2**: Figure 2 (DAG) 中的 dashed orange $S \\to Q$ path 标注 \"residual confound.\" 字体太小，不易辨认。\n- **M3**: Section 2 Related Work 的 \"Mode-specific biases in LLM judges\" 段落（p4 §44-46）提出了一个有趣但未被充分发展的论点（RLHF 训练造成的 format-specific biases），建议在主文或附录中提供更多证据。\n- **M4**: Abstract 第 4 句 \"GEE conditional decomposition reveals qualitatively distinct per-axis confound structures\" 对不熟悉 GEE 的读者不够友好，建议用更直观的语言描述。\n- **M5**: \"Code and Data will be released upon acceptance\" — 建议提供匿名 repository 或至少在 supplementary material 中包含核心代码以提高可复现性。\n- **M6**: Section 3.1 (p4) 提到 temperature 0.7 用于 rewriting，但未说明选择依据。\n- **M7**: Limitations 中 \"tone axis pilot\" 的结果（NLI gate 拒绝 55%）很有信息量，但与正文的连接不够紧密——建议在 Method 或 Experiments 中简要提及 CSD 的 scope boundary。\n\n---\n\n## Questions to Authors\n\n1. 如果 pairwise amplification 是主要机制（而非 Likert attenuation），那么你们的方法学建议会如何改变？目前 Conclusion 的\"single-format audits risk systematic blind spots\"暗示应该添加 pairwise 模式，但如果 pairwise 是在放大微弱偏好，添加它反而会引入 false positives。请讨论在 amplification-dominant 情景下的 practical implications。\n\n2. 为什么不包含 human evaluation 来 ground-truth 两种测量模式？论文多次提到这是\"the key next step\"（Conclusion p8, Limitations p8），但对于一篇旨在区分两种测量模式的论文，缺乏人工评估数据是一个显著的方法论空缺。\n\n3. Qwen3-32B 在 formality Style OR 从 4.20 (n=88) 降至 2.15 (n=355)，~49% shrinkage。如果对 verbosity 进行同样的 scaling，Style OR 可能从 13.10 降至 ~6.5。这仍然 >1，但你们如何确保 small-sample bias 不会改变 Table 2 中其他 judges 的 regime classification？\n\n4. Cross-axis contamination analysis (Appendix T, p16) 报告 formality rewrites 产生 negligible sentence structure changes (|d| < 0.03)，但 verbosity rewrites 的 Flesch-Kincaid grade 有 elevated shift (d = 0.50, Table 21)。这是否意味着 verbosity 的 \"style bias\" 部分是 readability bias？FK grade 的 60% mediation by sentence length (p7) 进一步暗示了这一点。\n\n---\n\n## Missing References（可能遗漏的相关工作）\n\n1. **Gladkoff et al. (2024/2025)** — 关于 LLM judge 评分校准 (calibration) 的工作，与 Likert scale 的 ceiling effect 讨论相关。\n2. **Kocmi & Federmann (2023)** — GEMBA: Using GPT Models for Reference-Free MT Evaluation，涉及 LLM judge 在 Likert vs pairwise 上的比较。\n3. 论文引用了大量 2025-2026 年工作（RATE, CASSE, FairJudge, Comparative Trap, Preference Leakage），coverage 整体较好。建议确认 Reber et al. (2025) RATE 和 Jeong et al. (2025) Comparative Trap 的引用信息是否准确（arxiv preprint 可能已被接收并需要更新引用格式）。\n\n---\n\n## 主要优势\n\n1. **实验设计极其严谨**：六项实验控制（NLI ablation、Claude reference、cross-axis variation、rewriting artifact、debiased prompting、four-architecture replication）、七种统计方法、三个 benchmark 的交叉验证。这是 LLM judge bias 文献中方法论最严谨的工作之一。\n2. **GEE per-axis decomposition 有实用诊断价值**：分离 style-specific 和 quality-correlated components 的能力对评估 pipeline 的实际审计有直接用途。Verbosity 的 style-dominated 模式与 formality 的 conditional 模式的对比是真正有信息量的发现。\n3. **Limitations 章节极其诚实和全面**：讨论了 quality-style confounding、evaluator-producer bias、scope boundaries、validation methodology 等关键局限，几乎没有 reviewer 需要补充的未提及限制。这在 NLP 论文中非常少见。\n4. **Related Work 覆盖全面**：从经典心理测量学到最新 LLM judge bias 工作，引用覆盖面广且组织有序。与 RATE 和 Comparative Trap 的差异化讨论清晰。\n5. **统计方法论透明**：FWER 控制、exploratory vs confirmatory 分类、bootstrap CI 的计算细节都有详细说明。GEE 模型诊断（附录 D）提供了 correlation structure robustness 和 interaction tests。\n6. **Cross-benchmark replication** 加强了结果的 generalizability，三个 benchmark (LLMBar, AlpacaEval, MT-Bench) 覆盖不同的 evaluation scenarios。\n\n---\n\n## 总结\n\n这是一篇**执行质量非常高**的实证论文，方法论严谨程度在 LLM judge bias 文献中属于上乘。主要弱点在于**新颖性**：核心发现（pairwise 比 Likert 更敏感于 style differences）是心理测量学的经典结论，论文声称的三个 \"LLM-specific distinctions\" 不足以构成对经典框架的本质超越。此外，**无法区分 attenuation 和 amplification** 这一根本限制——尽管论文坦诚讨论——削弱了 practical implications 的确定性。标题 \"Blindspot\" 与论文自身承认的多种解释之间存在张力。\n\n推荐 **3.5 (Borderline Conference)**，执行质量支持主会议接收，但新颖性不足可能使其更适合 Findings track。如果作者在 rebuttal 中能够 (1) 更诚实地定位新颖性（实证 characterization 而非方法论创新），(2) 提供 human evaluation 数据或至少 pilot 结果来区分 attenuation 和 amplification，评分可能提升至 4.0。",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1197 · 2026-05-23T08:57:56.332111+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4674
}
```

</details>

---


### Tool call

_source line 1198 · 2026-05-23T08:58:01.610397+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images"
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
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_15/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1199 · 2026-05-23T08:58:01.610743+00:00_

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

_source line 1200 · 2026-05-23T08:58:10.970449+00:00_

审稿报告已提交给 Review Director。

**总结**：评分 **3.5 (Borderline Conference)**。

核心判断：
- **执行质量出色**：方法论严谨（六项实验控制、七种统计方法、三个 benchmark 交叉验证），Limitations 章节异常全面诚实
- **新颖性不足**：核心发现是 Thurstone (1927) 的经典结论在 LLM judge 上的验证，声称的三个 "LLM-specific distinctions" 可被经典框架解释
- **三个 Must-Fix**：(1) 新颖性定位过度宣称方法论创新；(2) "consistently divergent" 基于 2 个主要轴且 Gemini 效应显著弱；(3) 标题 "Blindspot" 预设 attenuation 解释，与论文自身承认的三种竞争解释矛盾
- GEE per-axis decomposition 是最有价值的贡献，具有实用诊断意义

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 36

## Round 36

16 recorded events


### User

_source line 1201 · 2026-05-23T08:58:56.622627+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix、Should-Fix、Minor 问题以及 Questions，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 的审稿报告

**Overall Assessment**: 3.5 / 5 (Borderline Conference)
**Confidence**: 4 / 5

### 维度打分
| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3.5/5 | 核心定性发现有充分支撑；定量 OR 估计受小样本偏差影响，GPT-4o formality 在 FK control 下失去显著性，Claude 负对照证据链内部矛盾 |
| Excitement | 3.5/5 | 问题重要且及时，GEE per-axis decomposition 是方法论推进，但 construct divergence vs attenuation 的 adjudication 留给未来工作 |
| Reproducibility | 4/5 | 实验细节充分，prompts 公开，代码数据承诺接收后释放 |

### Must-Fix

**N1** [critical] 小样本 OR 膨胀对主要定量结论的系统性影响未充分传播
- n=88→n=355 的 Qwen3-32B formality Style OR 从 4.20 缩水至 2.15（-49%），Table 2 中其他 11 个 n=88 cell 的 OR 以 face value 呈现。Verbosity Style OR 8–13 在 ~50% shrinkage 下预计为 4–6.5，论文做了文字推演但未提供 shrinkage-adjusted 估计。
- 建议：(a) Table 2 旁给出 shrinkage-adjusted projected ORs；(b) 明确声明所有 n=88 OR 应被视为上界估计。

**N2** [critical] GPT-4o formality Style OR 在控制 FK grade 后失去显著性
- FK grade change 作为 GEE 协变量后，GPT-4o Style OR 从 2.70→2.15（p=.132）。GPT-4o 是论文叙事的锚点 judge。当前处理：Appendix 一段话带过（"Two of three judges retain significant"）。
- 建议：(a) 正文 Section 5.2/5.3 明确提及；(b) 讨论 FK 是 mediator 还是 confounder。

**N3** [critical] Claude "low-sensitivity reference" 证据链存在内部矛盾
- 四条 convergent evidence 每条单独不成立：TOST underpowered, GEE MDE=1.56 无法排除 small effect, BF₀₁=0.80 inconclusive, AEval verbosity Style OR=4.76 与标签矛盾。Section 5.4 六项 controls 中 "(ii) Claude low-sensitivity reference (Style OR n.s.)" 选择性引用 LLMBar formality。
- 建议：(a) 降级为"lower-sensitivity judge"；(b) 更新 Section 5.4 的描述；(c) 正文讨论 AEval verbosity OR=4.76。

### Should-Fix

**W1** Evaluator-producer overlap 仅用一个替代 rewriter 验证。Qwen3-32B rewriter→judge overlap 仅用 GPT-4o 替代验证（22% OR 降幅），缺少 rule-based rewriter。Formality 替代 rewriter 未报告 GEE。

**W2** Cross-benchmark replication 是选择性的——24 cells 只填了 6 个（25%），选择最强 cell，可能向上偏倚。

**W3** TOST equivalence margin 缺乏独立依据——5 个 margin 无先验 justification。

**W4** 因果语言不够一致——Section 3.1 "constitutes a binary intervention" vs Section 3.5 "interventional rather than formal causal evidence"。

### Minor

**M1**: Table 1 "n=88" 与 verbosity 实际 n=86 不一致。
**M2**: Intro opening example 是 cherry-picked，应注明。
**M3**: DAG orange dashed line 黑白打印不可辨。
**M4**: Appendix Table 3 QIC 值显示"---"无实际数值。
**M5**: BT `choix` library "default regularization" 未说明具体形式。

### Questions

**Q1**: verbosity 做 scaled replication 预期 OR 缩水多少？会改变 regime classification 吗？
**Q2**: FK grade 是 mediator 还是 confounder？请提供 DAG 论据。
**Q3**: AEval verbosity Claude Style OR=4.76 如何调和 low-sensitivity reference？
**Q4**: Direction-aware gate 的 verbosity expansion 是否漏过 R→Q 路径？
**Q5**: BT regularization sensitivity analysis？

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

_source line 1202 · 2026-05-23T09:00:17.712656+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex",
  "offset": "140",
  "limit": "40"
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
    "offset": "140",
    "limit": "40"
  }
}
```

</details>

---


### Tool result

_source line 1203 · 2026-05-23T09:00:18.064232+00:00_

140	Same-style double-rewrite controls confirm a rewriting artifact (Appendix~\ref{app:artifact_control}), absorbed by GEE's originality term.
141	
142	\paragraph{Sample-size sensitivity.}
143	At $n = 355$, the Qwen3-32B formality Style OR drops from $4.20$ to $2.15$ $[1.46, 3.16]$ ($-49\%$), consistent with small-sample upward bias \citep{nemes2009bias}; the log-OR CI contracts by $1.94\times$ (close to $\sqrt{355/88} \approx 2.01$), and the regime classification remains stable---conditional at both sample sizes (both effects significant; Orig OR $4.70 \to 4.99$).
144	Verbosity Style ORs ($8$--$13$) would remain style-dominated even under ${\sim}50\%$ shrinkage (projected $4$--$6.5$, still ${\gg}$ Orig OR ${<}1$).
145	
146	\subsection{Cross-Judge and Cross-Axis Replication}
147	\label{sec:cross_judge}
148	
149	Two independent judges replicate the formality Blindspot: Qwen3-32B (BT 66.5\%, $p < 0.0001$; Likert $p = 0.908$) and Llama-3.3-70B (BT 69.5\%, $p = 0.0001$; Likert $p = 0.846$).
150	Gemini-2.5-Flash shows a weaker, originality-dominated formality pattern (confirmatory: BT 57.4\%, $p = 0.031$; Likert $d = {-}0.08$, n.s.; Style OR $= 1.64$, n.s.; Orig OR $= 2.51$, $p = 0.002$; \S\ref{sec:direction}).
151	
152	Verbosity provides the strongest Blindspot: all four target judges show consistent preference (GPT-4o 76.0\%, Qwen3-32B 77.3\%, Llama-70B 73.5\%, Gemini 70.8\%; all $p \leq 0.0001$), while Likert ATE remains non-significant for all ($p = 0.179$--$0.752$).
153	GEE confirms massive style effects (OR $8.2$--$13.1$, all $p < .0001$) with originality ORs below 1 ($0.38$--$0.49$; only Llama-70B significant at $p = .020$, yet Style OR exceeds Orig OR by $22\times$), confirming style dominance (Table~\ref{tab:gee}).
154	Both rewriting directions favor verbose responses (90.7\%/80.6\%); length-controlled Style OR is unchanged ($<$2\%), and an independent GPT-4o rewriter bounds evaluator-producer overlap to a 22\% reduction (Appendix~\ref{app:rewriter_indep}).
155	
…[truncated 2550 chars]

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

_source line 1204 · 2026-05-23T09:00:18.215031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "limit": "100"
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
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-23T09:00:18.365948+00:00_

1	\appendix
2	
3	\noindent\emph{Organization: design rationale (A$^*$), confound analysis (A--B), model diagnostics (C), independence tests (D), gate validation (E--F), equivalence testing (G), statistical details (H--K), sensitivity analyses (L--N), artifact controls (O), implementation (P), multiplicity (Q), cross-axis contamination (R), FK length-control (R$'$), human annotation agreement (S), cross-benchmark replication (T), Claude cross-benchmark (U), rewriting prompts (V).}
4	
5	\section{Design Rationale}
6	\label{app:design_rationale}
7	
8	Three variables govern the observed judge score $Y$: the style attribute $S$ (e.g., formality), the original content quality $Q$, and the judge's internal scoring function.
9	Both $S$ and $Q$ causally influence $Y$; the goal of CSD is to approximate the effect $S \to Y$ while blocking confounding through $Q$.
10	Style-controlled rewriting generates a text pair that differs along a single style axis, but any rewriting operation risks inadvertently altering content quality ($R \to Q$).
11	The NLI gate (\S\ref{sec:nli_gate}) blocks this path, yielding a controlled estimate of the $S \to Y$ effect.
12	Our approach provides interventional rather than formal causal evidence: we do not claim that the DAG in Figure~\ref{fig:dag} is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions from the potential outcomes framework.
13	``Controlled'' in this context refers to experimentally controlled rewriting conditions, not formal causal identification in the potential-outcomes sense.
14	Our identification rests on three operational assumptions: (i)~the NLI gate approximates content preservation, blocking the $R \to Q$ path; (ii)~position swapping controls for presentation-order effects; and (iii)~the style rewrite introduces no systematic differences beyond the target axis.
15	
16	\section{Direction Asymmetry and Quality Confounding}
17	\label{app:direction}
18	
19	The formality axis exhibits a pronounced 
…[truncated 6061 chars]

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

_source line 1206 · 2026-05-23T09:00:25.250832+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "offset": "100",
  "limit": "150"
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
    "offset": "100",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1207 · 2026-05-23T09:00:25.351772+00:00_

100	\begin{table}[h]
101	\centering
102	\small
103	\caption{95\% CIs for GEE conditional decomposition (Table~\ref{tab:gee}).}
104	\label{tab:gee_ci}
105	\begin{tabular}{@{}lcc@{}}
106	\toprule
107	Config & Style OR [CI] & Orig OR [CI] \\
108	\midrule
109	Qwen3 verb.\ & 13.10 [5.62, 30.55] & 0.49 [0.21, 1.14] \\
110	GPT-4o verb.\ & 11.34 [4.93, 26.10] & 0.45 [0.20, 1.04] \\
111	Llama-70B verb.\ & 8.21 [3.62, 18.65] & 0.38 [0.17, 0.86] \\
112	Gemini verb.\ & 8.98 [3.68, 21.94] & 0.46 [0.20, 1.04] \\
113	GPT-4o form.\ & 2.58 [1.41, 4.73] & 2.32 [1.27, 4.26] \\
114	Qwen3 form.\ & 4.20 [1.99, 8.87] & 4.70 [2.22, 9.96] \\
115	Qwen3 form.$^a$ & 2.15 [1.46, 3.16] & 4.99 [3.40, 7.34] \\
116	Llama-70B form.\ & 4.81 [2.48, 9.33] & 3.12 [1.61, 6.04] \\
117	Gemini form.\ & 1.64 [0.91, 2.98] & 2.51 [1.39, 4.54] \\
118	GPT-4o reg.\ & 1.88 [1.08, 3.28] & 2.21 [1.26, 3.86] \\
119	Qwen3 reg.\ & 1.91 [1.01, 3.58] & 5.72 [3.02, 10.82] \\
120	Llama-70B reg.\ & 3.33 [1.73, 6.42] & 3.07 [1.60, 5.92] \\
121	\bottomrule
122	\multicolumn{3}{l}{\footnotesize $^a$ $n = 355$; other rows: $n = 88$.}
123	\end{tabular}
124	\end{table}
125	
126	\section{Rewriter Independence}
127	\label{app:rewriter_indep}
128	
129	Evaluator-producer overlap is limited to Qwen3-32B (rewriter $=$ judge); the independence test below bounds this to a 22\% Style OR reduction. The other three target judges (GPT-4o, Llama-70B, Gemini) use a different rewriter and are not subject to this confound.
130	
131	To test whether the Blindspot depends on the rewriter's identity, we replace Qwen3-32B with GPT-4o as rewriter while keeping Qwen3-32B as judge.
132	
133	\paragraph{Verbosity (Table~\ref{tab:rewriter_indep}).}
134	The Style OR decreases by $22\%$ ($13.10 \to 10.17$), bounding evaluator-producer inflation of the style effect; the pure-style pattern (Originality n.s.) and Blindspot (BT significant, Likert n.s.) both persist.
135	
136	\begin{table}[h]
137	\centering
138	\small
139	\caption{Rewriter independence test: verb
…[truncated 5956 chars]

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

_source line 1208 · 2026-05-23T09:00:32.741054+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "FK.*grade.*covariate|fk_length|FK.*control",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-C": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "FK.*grade.*covariate|fk_length|FK.*control",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-C": "5"
  }
}
```

</details>

---


### Tool result

_source line 1209 · 2026-05-23T09:00:33.343208+00:00_

1-\appendix
2-
3:\noindent\emph{Organization: design rationale (A$^*$), confound analysis (A--B), model diagnostics (C), independence tests (D), gate validation (E--F), equivalence testing (G), statistical details (H--K), sensitivity analyses (L--N), artifact controls (O), implementation (P), multiplicity (Q), cross-axis contamination (R), FK length-control (R$'$), human annotation agreement (S), cross-benchmark replication (T), Claude cross-benchmark (U), rewriting prompts (V).}
4-
5-\section{Design Rationale}
6-\label{app:design_rationale}
7-
8-Three variables govern the observed judge score $Y$: the style attribute $S$ (e.g., formality), the original content quality $Q$, and the judge's internal scoring function.
--
587-Verbosity rewrites leave lexical diversity unchanged (TTR $d = -0.04$); the elevated FK grade ($d = 0.50$) is an artifact of FK's dependence on sentence length, which changes by design in verbosity manipulation.
588-These results confirm that cross-axis contamination is small to negligible for the proxies measured; the GEE originality term (\S\ref{sec:direction}) provides additional protection by absorbing any residual quality confound.
589-A robustness check adding word-count change as a GEE covariate leaves all Style ORs virtually unchanged ($\Delta < 12\%$, all covariate $p > .28$), confirming that the small cross-axis word-count shift does not confound formality estimates.
590-
591-\section{FK Length-Control Analysis}
592:\label{app:fk_length}
593-
594-The elevated FK grade shift for verbosity rewrites ($d = 0.50$; Table~\ref{tab:cross_axis}) could reflect genuine formality contamination or simply FK's structural dependence on sentence length.
595-We disentangle these via length-controlled regression and mediation analysis.
596-
597-\begin{table}[h]
--
609-Formality & Sent.\ length (words) & $-0.11$ & $-0.04$ \\
610-\bottomrule
611-\end{tabular}
612-\end{table}
613-
614:Regressing FK change on style axis without controls yields $\beta = 2.69$ 
…[truncated 1233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 1210 · 2026-05-23T09:00:33.695114+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "cross.bench|tab:cross_bench",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-C": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "cross.bench|tab:cross_bench",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-C": "10"
  }
}
```

</details>

---


### Tool result

_source line 1211 · 2026-05-23T09:00:33.749055+00:00_

1-\appendix
2-
3:\noindent\emph{Organization: design rationale (A$^*$), confound analysis (A--B), model diagnostics (C), independence tests (D), gate validation (E--F), equivalence testing (G), statistical details (H--K), sensitivity analyses (L--N), artifact controls (O), implementation (P), multiplicity (Q), cross-axis contamination (R), FK length-control (R$'$), human annotation agreement (S), cross-benchmark replication (T), Claude cross-benchmark (U), rewriting prompts (V).}
4-
5-\section{Design Rationale}
6-\label{app:design_rationale}
7-
8-Three variables govern the observed judge score $Y$: the style attribute $S$ (e.g., formality), the original content quality $Q$, and the judge's internal scoring function.
9-Both $S$ and $Q$ causally influence $Y$; the goal of CSD is to approximate the effect $S \to Y$ while blocking confounding through $Q$.
10-Style-controlled rewriting generates a text pair that differs along a single style axis, but any rewriting operation risks inadvertently altering content quality ($R \to Q$).
11-The NLI gate (\S\ref{sec:nli_gate}) blocks this path, yielding a controlled estimate of the $S \to Y$ effect.
12-Our approach provides interventional rather than formal causal evidence: we do not claim that the DAG in Figure~\ref{fig:dag} is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions from the potential outcomes framework.
13-``Controlled'' in this context refers to experimentally controlled rewriting conditions, not formal causal identification in the potential-outcomes sense.
--
643-All disagreements involve borderline meaning-equivalence judgments rather than clear content contamination.
644-
645-\paragraph{Comparison with 50-pair pilot.}
646-The expanded 100-pair annotation tightens the precision estimate from $84$--$100\%$ (individual annotators on 25 gate-passed pairs) to $98.6\%$ (both annotators concordant on 70 gate-passed pairs), and raises AC$_1$ from $0.65$ to $0.96$.
647-
648-\paragraph{
…[truncated 2596 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 1212 · 2026-05-23T09:00:38.373077+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "offset": "660",
  "limit": "50"
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
    "offset": "660",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1213 · 2026-05-23T09:00:38.774996+00:00_

660	\caption{Cross-benchmark replication on AlpacaEval (AEval) and MT-Bench (MTB). $\ddagger$: both BT and Likert significant; $\dagger$: Blindspot (BT significant, Likert not).}
661	\label{tab:cross_bench}
662	\begin{tabular}{@{}lllccc@{}}
663	\toprule
664	Bench & Judge & Axis & BT $P$ & Likert $d$ ($p$) & Cat.\ \\
665	\midrule
666	AEval & GPT-4o & Form.\ & .727$^{***}$ & .148 (.170) & $\dagger$ \\
667	 & Qwen3 & Form.\ & .657$^{***}$ & .081 (.198) & $\dagger$ \\
668	 & Qwen3 & Verb.\ & .841$^{***}$ & .375 (.0003) & $\ddagger$ \\
669	 & Llama-70B & Form.\ & .756$^{***}$ & 1.120 (${<}.001$) & $\ddagger$ \\
670	\midrule
671	MTB & GPT-4o & Form.\ & .692$^{***}$ & .167 (.016) & $\ddagger$ \\
672	 & Qwen3 & Form.\ & .712$^{***}$ & .149 (.007) & $\ddagger$ \\
673	\bottomrule
674	\multicolumn{6}{l}{\footnotesize $^{***}$ $p < 0.001$. $\ddagger$: both sig.;\; $\dagger$: Blindspot.}
675	\end{tabular}
676	\end{table}
677	
678	\section{Claude Cross-Benchmark Analysis}
679	\label{app:claude_crossbench}
680	
681	Claude Sonnet~4 serves as low-sensitivity reference on LLMBar (\S\ref{sec:amplification}; Appendix~\ref{app:claude_tost}).
682	Cross-benchmark GEE decomposition reveals that Claude's elevated aggregate BT on AEval/MT-Bench reflects quality detection rather than style preference.
683	Table~\ref{tab:claude_crossbench} reports results across all five tested configurations.
684	
685	\begin{table}[h]
686	\centering
687	\small
688	\caption{Claude Sonnet~4 cross-benchmark results with GEE decomposition. Formality Style OR is non-significant across all three benchmarks; elevated BT on AEval/MT-Bench is driven by Orig OR (quality detection). AEval verbosity is the sole genuine style effect.}
689	\label{tab:claude_crossbench}
690	\resizebox{\columnwidth}{!}{%
691	\begin{tabular}{@{}llccccc@{}}
692	\toprule
693	Bench & Axis & BT $P$ & Likert $d$ ($p$) & Style OR ($p$) & Orig OR ($p$) \\
694	\midrule
695	LLMBar & Form.\ & .562 & $-$.021 (.721) & 1.47 (.276) & 6.66 (${<}.001$) \\
69
…[truncated 843 chars]

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

_source line 1214 · 2026-05-23T09:03:21.827576+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R1-N1: 小样本 OR 膨胀对定量结论的系统性影响**\n\n同意这是一个重要问题。Qwen3-32B formality 的 49% shrinkage (Style OR 4.20 → 2.15, Section 5.2, p7) 是论文自己提供的最有力的 small-sample bias 证据。Table 2 中其余 11 个 n=88 cell 的 OR 确实以 face value 呈现，缺乏 shrinkage-adjusted 估计。\n\n我在自己的审稿中也提出了同样的问题（我的 W4），并进一步指出：论文的文字推演\"Verbosity Style ORs (8-13) would remain style-dominated even under ~50% shrinkage (projected 4-6.5)\"虽然逻辑上成立（4-6.5 >> Orig OR <1），但这是推测而非实证。Table 2 应明确标注 n=88 的 point estimates 为上界估计，或者提供 shrinkage-corrected projections。\n\n补充一点 R1 未提及的：Table 5 (Appendix C) 的 GEE CIs 显示 n=88 cells 的 95% CI 宽度非常大（如 GPT-4o verbosity Style OR 11.34 [4.93, 26.10]），这本身已经反映了估计精度的局限。CI 下界 4.93 仍然远高于 Orig OR 0.45，所以 regime classification 是稳健的——但论文应更突出地展示 CIs，而非仅在附录中报告。\n\n**[AGREE] R1-N2: GPT-4o formality Style OR 在 FK control 下失去显著性**\n\n同意这需要在正文中更明确地讨论。我确认了 Appendix R' 的具体数据：GPT-4o Style OR 从 2.70 降至 2.15 (p = .132)，确实不再显著。Qwen3-32B 从 4.20 降至 3.38 (p = .014)，Llama-70B 从 5.52 降至 2.69 (p = .037)——两个保留显著性。\n\nGPT-4o 作为论文叙事的锚点 judge（Introduction 的 opening example 使用 GPT-4o，Table 1 以 GPT-4o 开头），其 formality Style OR 在 FK control 下失去显著性是一个 material finding，不应仅在附录一句话带过。\n\n**但我补充一个 nuance（R1 在 Q2 中也提到了）**：FK grade 的角色是 mediator 还是 confounder 取决于 causal structure：\n- 如果 formality → FK grade → judge score（mediator），则 controlling for FK 是错误的（\"bad control\"，Pearl 2009），因为它移除了合法的因果效应通路\n- 如果 common cause → formality + FK grade（confounder），则 controlling 是正确的\n\n论文的 DAG (Figure 2) 显示 S → Y（style → judge score）是单一直接路径，没有通过 FK 的中介。如果 formality 变化本身导致 FK grade 变化（这是很可能的——更正式的文本倾向于使用更长的句子和更复杂的词汇），那么 FK 是 mediator，控制它会低估真实的 style effect。论文应明确讨论这一点，而非简单地将 FK-controlled 结果作为 robustness check 呈现。\n\n**[AGREE] R1-N3: Claude \"low-sensitivity reference\" 证据链的内部矛盾**\n\n完全同意。我在自己的审稿中也将此列为 Should-Fix (我的 W2)，但 R1 对证据链的逐条解构更加系统，说服我这应升级为更严重的问题。四条 convergent evidence 逐一审视：\n\n1. **TOST**: Per-axis 在 Δ=10pp 不显著 (p=.156, power ≈42%)，pooled 在 Δ=10pp 也不显著 (p=.100)——只在 Δ=12pp 处勉强显著 (p=.035)。Appendix G Table 9 确认了这一点。等价界限的选择缺乏先验依据。\n2. **GEE MDE**: MDE=1.56 at 80% power 意味着无法排除 OR 在 1.0-1.56 之间的 small but real effects。\n3. **BF₀₁=0.80**: 按 Jeffreys 标准，这是 anecdotal/inconclusive，不能作为 null 的证据。\n4. **AEval verbosity Style OR=4.76 (p<.001)**: 这直接打破了 \"low-sensitivity\" 标签——Claude 在至少一个 axis×benchmark 组合上展现了与 target judges 可比的 style sensitivity。\n\nR1 的建议合理：降级为 \"lower-sensitivity judge\"，并在 Section 5.4 的六项 controls 中更新 \"(ii)\" 的描述。我补充建议：在 Limitations 中已有的 Claude verbosity 讨论（p9 第 55 行：\"Verbosity sensitivity is benchmark-dependent (AEval Style OR = 4.76, p < .001; LLMBar n.s.)\"）应提升至正文 Section 5.3/5.4。\n\n---\n\n### Should-Fix\n\n**[AGREE] R1-W1: Evaluator-producer overlap 验证不充分**\n\n同意，但 scope 需要限定。Evaluator-producer overlap 问题仅影响 Qwen3-32B（rewriter = judge）。GPT-4o、Llama-70B、Gemini 使用独立 rewriter，不受此 confound 影响（Appendix E 第 129 行明确说明）。论文提供了 GPT-4o 作为替代 rewriter 的验证（Tables 6-7），展示 verbosity OR 降幅 22%、formality BT 降幅 2.1pp，且 Blindspot 均保持。\n\nR1 要求 rule-based rewriter 是理想化的——但实际上，rule-based formality rewriting 很难保证内容一致性（需要大量手工规则），且论文已在 Limitations (p9) 承认 \"all alternative rewriters are instruction-tuned LLMs that may share style preferences acquired during RLHF training\"。建议论文在 Limitations 中将 rule-based rewriter 作为明确的 future work direction。\n\n**formality GEE 未报告**是一个有效的具体缺失——Table 7 只有 BT 和 Likert 结果，没有 GEE decomposition。如果 GPT-4o rewriter 改变了 formality 的 confound structure（如 Style vs Originality 比例），这会影响对 evaluator-producer bias 的评估。\n\n**[AGREE] R1-W2: Cross-benchmark replication 的选择性**\n\n同意，并且我认为这一问题比 R1 的评级（Should-Fix）更严重。Table 22 (Appendix T) 仅覆盖 6/24 cells (25%)，且论文自己承认选择的是 \"selected configurations targeting the strongest effects\"（Appendix T 第 655 行）。但主文 Section 5.3 第 157 行的表述是 \"These per-axis patterns replicate across benchmarks\"——这暗示了比实际更广泛的复制。\n\n具体选择偏差风险：\n- AEval 的 4 个 cells 中，2 个是 Blindspot (†)，2 个是 both significant (‡)——后者其实*削弱*了 Blindspot 的 claim（Likert 也能检测到），但论文将其解释为 \"severity spectrum\" 的确认\n- Verbosity 仅在 AEval 上有一个 cross-benchmark cell (Qwen3)，没有 GPT-4o verbosity 的 cross-benchmark 数据\n- Gemini 完全缺失于 cross-benchmark replication\n\n建议论文承认选择性，并讨论缺失 cells 可能的影响方向。\n\n**[AGREE] R1-W3: TOST equivalence margin 缺乏先验依据**\n\n同意。Table 9 (Appendix G) 测试了 5 个 margins (Δ = 5, 10, 12, 15, 20pp)，但 12pp 作为 headline result 没有 a priori justification。在 equivalence testing 文献中 (Lakens, 2017)，margin 应基于 smallest effect size of interest (SESOI)，而非事后选择使 p < .05 的 margin。论文应讨论 12pp 在 BT scale 上对应什么程度的 style sensitivity——例如，12pp 意味着 judge 在 62% 的 pairwise 比较中选择 styled 文本，这在 RLHF 管道中是否构成\"practically meaningful\" bias？\n\n**[REBUT] R1-W4: 因果语言不一致**\n\n部分不同意。R1 引用的两处表述在不同层面操作：\n\n- Section 3.1 \"constitutes a binary intervention\"：描述的是**操作层面**——CSD 对文本进行了 controlled manipulation（改变一个 style axis），这在操作上确实是一个 intervention（与 observational study 相对）\n- Section 3.5 / Appendix A \"interventional rather than formal causal evidence\"：描述的是**推断层面**——论文不宣称达到 potential outcomes framework 下的 formal causal identification\n\n这两者并不矛盾：你可以执行一个 intervention（操作上）而不宣称它达到了 formal causal identification（推断上）。Randomized experiments 和 natural experiments 都是 interventional designs，但推断强度不同。\n\n**不过**，我承认对不熟悉因果推断文献的读者，这种区分可能造成困惑。建议在 Section 3.1 中将 \"constitutes a binary intervention\" 修改为 \"approximates a binary intervention\" 或 \"operationalizes a single-axis manipulation\"，避免与 formal causal intervention 的标准定义混淆。\n\n---\n\n### Minor\n\n**[AGREE] R1-M1**: 如果 verbosity 的 NLI gate 通过率不同导致实际 n≠88，Table 1 header 应准确标注。建议统一使用 \"n varies by axis; see Appendix\" 或逐行标注。\n\n**[REBUT] R1-M2**: 不同意 Intro opening example 需要标注为 \"cherry-picked\"。NLP 论文的 opening example 惯例上是选择性的、illustrative 的，用于建立 reader's intuition。论文随后提供了系统性的统计证据（Table 1, Figure 3, 七种统计方法），opening example 的功能是叙事性的而非论证性的。要求标注 \"cherry-picked\" 在学术写作规范中不常见，且可能暗示论文在隐瞒什么——但系统证据已经充分呈现。如果 R1 的担心是 example 的代表性，更好的做法是在附录提供该 example 的完整数据（NLI 分数、两个 judge 评分、position-swapped 结果），而非加标签。\n\n**[AGREE] R1-M3**: DAG 的 orange dashed line 在灰度打印下确实不可辨。建议使用不同的 line pattern (e.g., dash-dot) 或 annotation 来区分。\n\n**[AGREE] R1-M4**: Table 3 (Appendix C) 的 QIC \"---\" 应该报告实际数值或解释为什么省略。我在 PDF 中确认了这一点——所有 9 个 cells 都是 \"---\"，只有 |ΔQIC| 有值。\n\n**[AGREE] R1-M5**: choix library 的 \"default regularization\" 应说明具体形式（L2? pseudo-count? regularization strength?）。这是一个 minor 但 valid 的 reproducibility concern。\n\n---\n\n### Questions\n\n**R1-Q1**: verbosity scaled replication 预期 OR 缩水多少？\n我与 R1 有相同的疑问（我的 Q3）。论文推测 50% shrinkage 将 OR 8-13 降至 4-6.5，仍 style-dominated。但 shrinkage 幅度可能因 axis 而异——verbosity 的效应量大于 formality，large effects 的 shrinkage 百分比可能更小（Nemes & Huang, 2009 的 bias correction 与效应量的关系是 non-linear 的）。实证验证是必要的。\n\n**R1-Q2**: FK grade 是 mediator 还是 confounder？\n关键问题。我在回应 N2 时已详细分析。简要补充：\n- 论文的 DAG (Figure 2) 不包含 FK 作为中介节点——如果 FK 是 S→FK→Y 通路的一部分，控制 FK 会低估 style effect（over-control bias）\n- 但 FK 也可能与 formality 共享 common cause（如原始文本的写作水平），此时控制是正确的\n- 论文需要明确立场，或承认两种解释下的 GPT-4o Style OR 范围是 [2.15, 2.70]\n\n**R1-Q3**: AEval verbosity Claude Style OR=4.76 如何调和 low-sensitivity reference？\n我完全赞同这个质疑。Appendix U (Table 23) 和 Limitations (p9) 确认了这一数据。Claude 的 low-sensitivity 标签只在 LLMBar formality 上成立；AEval verbosity 的 Style OR 4.76 (p<.001) 与 GPT-4o verbosity Style OR 11.34 可比。论文应该承认 Claude 是 \"lower-sensitivity on formality/LLMBar\" 而非全局性的 \"low-sensitivity reference\"。\n\n**R1-Q4**: Direction-aware gate 的 verbosity expansion 是否漏过 R→Q 路径？\n这是一个好的技术问题，但我认为论文提供了充分的 empirical 回应：Appendix F (Section F, 第 212-217 行) 报告了 DA-only vs bidirectional-pass 子集的 BT 比较，无显著差异 (permutation p=.663, Δ=-1.1pp)。五个 judge 的 Fisher exact tests 均 p>.66。这些 empirical 验证表明 DA gate 没有系统性地漏过 quality-altering content。理论上的担忧是合理的，但 empirical evidence 充分缓解了这一风险。\n\n**R1-Q5**: BT regularization sensitivity analysis？\n同意应该提供。choix 的 default regularization (pseudo-count based) 可能对 small-n 估计有影响。建议作者报告无正则化或不同正则化强度下的 BT estimates，特别是对 n=88 的 cells。\n\n---\n\n### 总结\n\nR1 的审稿整体质量很高。三个 Must-Fix 中，我完全同意 N1（small-sample bias 未充分传播）和 N3（Claude reference 证据链矛盾），对 N2 同意需要更多透明度但补充了 mediator vs confounder 的 nuance。Should-Fix 中，W1-W3 我同意，W4 我认为因果语言并非真正不一致而是在不同层面操作，但同意措辞可以改进。Minor issues 除 M2 外均同意。\n\nR1 和我对论文的整体评价接近（均为 3.5 Borderline Conference），核心共识是：执行质量高，但新颖性不足（我比 R1 更强调这一点）、attenuation vs amplification 无法区分、以及 small-sample 定量估计的可靠性。",
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
    "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R1-N1: 小样本 OR 膨胀对定量结论的系统性影响**\n\n同意这是一个重要问题。Qwen3-32B formality 的 49% shrinkage (Style OR 4.20 → 2.15, Section 5.2, p7) 是论文自己提供的最有力的 small-sample bias 证据。Table 2 中其余 11 个 n=88 cell 的 OR 确实以 face value 呈现，缺乏 shrinkage-adjusted 估计。\n\n我在自己的审稿中也提出了同样的问题（我的 W4），并进一步指出：论文的文字推演\"Verbosity Style ORs (8-13) would remain style-dominated even under ~50% shrinkage (projected 4-6.5)\"虽然逻辑上成立（4-6.5 >> Orig OR <1），但这是推测而非实证。Table 2 应明确标注 n=88 的 point estimates 为上界估计，或者提供 shrinkage-corrected projections。\n\n补充一点 R1 未提及的：Table 5 (Appendix C) 的 GEE CIs 显示 n=88 cells 的 95% CI 宽度非常大（如 GPT-4o verbosity Style OR 11.34 [4.93, 26.10]），这本身已经反映了估计精度的局限。CI 下界 4.93 仍然远高于 Orig OR 0.45，所以 regime classification 是稳健的——但论文应更突出地展示 CIs，而非仅在附录中报告。\n\n**[AGREE] R1-N2: GPT-4o formality Style OR 在 FK control 下失去显著性**\n\n同意这需要在正文中更明确地讨论。我确认了 Appendix R' 的具体数据：GPT-4o Style OR 从 2.70 降至 2.15 (p = .132)，确实不再显著。Qwen3-32B 从 4.20 降至 3.38 (p = .014)，Llama-70B 从 5.52 降至 2.69 (p = .037)——两个保留显著性。\n\nGPT-4o 作为论文叙事的锚点 judge（Introduction 的 opening example 使用 GPT-4o，Table 1 以 GPT-4o 开头），其 formality Style OR 在 FK control 下失去显著性是一个 material finding，不应仅在附录一句话带过。\n\n**但我补充一个 nuance（R1 在 Q2 中也提到了）**：FK grade 的角色是 mediator 还是 confounder 取决于 causal structure：\n- 如果 formality → FK grade → judge score（mediator），则 controlling for FK 是错误的（\"bad control\"，Pearl 2009），因为它移除了合法的因果效应通路\n- 如果 common cause → formality + FK grade（confounder），则 controlling 是正确的\n\n论文的 DAG (Figure 2) 显示 S → Y（style → judge score）是单一直接路径，没有通过 FK 的中介。如果 formality 变化本身导致 FK grade 变化（这是很可能的——更正式的文本倾向于使用更长的句子和更复杂的词汇），那么 FK 是 mediator，控制它会低估真实的 style effect。论文应明确讨论这一点，而非简单地将 FK-controlled 结果作为 robustness check 呈现。\n\n**[AGREE] R1-N3: Claude \"low-sensitivity reference\" 证据链的内部矛盾**\n\n完全同意。我在自己的审稿中也将此列为 Should-Fix (我的 W2)，但 R1 对证据链的逐条解构更加系统，说服我这应升级为更严重的问题。四条 convergent evidence 逐一审视：\n\n1. **TOST**: Per-axis 在 Δ=10pp 不显著 (p=.156, power ≈42%)，pooled 在 Δ=10pp 也不显著 (p=.100)——只在 Δ=12pp 处勉强显著 (p=.035)。Appendix G Table 9 确认了这一点。等价界限的选择缺乏先验依据。\n2. **GEE MDE**: MDE=1.56 at 80% power 意味着无法排除 OR 在 1.0-1.56 之间的 small but real effects。\n3. **BF₀₁=0.80**: 按 Jeffreys 标准，这是 anecdotal/inconclusive，不能作为 null 的证据。\n4. **AEval verbosity Style OR=4.76 (p<.001)**: 这直接打破了 \"low-sensitivity\" 标签——Claude 在至少一个 axis×benchmark 组合上展现了与 target judges 可比的 style sensitivity。\n\nR1 的建议合理：降级为 \"lower-sensitivity judge\"，并在 Section 5.4 的六项 controls 中更新 \"(ii)\" 的描述。我补充建议：在 Limitations 中已有的 Claude verbosity 讨论（p9 第 55 行：\"Verbosity sensitivity is benchmark-dependent (AEval Style OR = 4.76, p < .001; LLMBar n.s.)\"）应提升至正文 Section 5.3/5.4。\n\n---\n\n### Should-Fix\n\n**[AGREE] R1-W1: Evaluator-producer overlap 验证不充分**\n\n同意，但 scope 需要限定。Evaluator-producer overlap 问题仅影响 Qwen3-32B（rewriter = judge）。GPT-4o、Llama-70B、Gemini 使用独立 rewriter，不受此 confound 影响（Appendix E 第 129 行明确说明）。论文提供了 GPT-4o 作为替代 rewriter 的验证（Tables 6-7），展示 verbosity OR 降幅 22%、formality BT 降幅 2.1pp，且 Blindspot 均保持。\n\nR1 要求 rule-based rewriter 是理想化的——但实际上，rule-based formality rewriting 很难保证内容一致性（需要大量手工规则），且论文已在 Limitations (p9) 承认 \"all alternative rewriters are instruction-tuned LLMs that may share style preferences acquired during RLHF training\"。建议论文在 Limitations 中将 rule-based rewriter 作为明确的 future work direction。\n\n**formality GEE 未报告**是一个有效的具体缺失——Table 7 只有 BT 和 Likert 结果，没有 GEE decomposition。如果 GPT-4o rewriter 改变了 formality 的 confound structure（如 Style vs Originality 比例），这会影响对 evaluator-producer bias 的评估。\n\n**[AGREE] R1-W2: Cross-benchmark replication 的选择性**\n\n同意，并且我认为这一问题比 R1 的评级（Should-Fix）更严重。Table 22 (Appendix T) 仅覆盖 6/24 cells (25%)，且论文自己承认选择的是 \"selected configurations targeting the strongest effects\"（Appendix T 第 655 行）。但主文 Section 5.3 第 157 行的表述是 \"These per-axis patterns replicate across benchmarks\"——这暗示了比实际更广泛的复制。\n\n具体选择偏差风险：\n- AEval 的 4 个 cells 中，2 个是 Blindspot (†)，2 个是 both significant (‡)——后者其实*削弱*了 Blindspot 的 claim（Likert 也能检测到），但论文将其解释为 \"severity spectrum\" 的确认\n- Verbosity 仅在 AEval 上有一个 cross-benchmark cell (Qwen3)，没有 GPT-4o verbosity 的 cross-benchmark 数据\n- Gemini 完全缺失于 cross-benchmark replication\n\n建议论文承认选择性，并讨论缺失 cells 可能的影响方向。\n\n**[AGREE] R1-W3: TOST equivalence margin 缺乏先验依据**\n\n同意。Table 9 (Appendix G) 测试了 5 个 margins (Δ = 5, 10, 12, 15, 20pp)，但 12pp 作为 headline result 没有 a priori justification。在 equivalence testing 文献中 (Lakens, 2017)，margin 应基于 smallest effect size of interest (SESOI)，而非事后选择使 p < .05 的 margin。论文应讨论 12pp 在 BT scale 上对应什么程度的 style sensitivity——例如，12pp 意味着 judge 在 62% 的 pairwise 比较中选择 styled 文本，这在 RLHF 管道中是否构成\"practically meaningful\" bias？\n\n**[REBUT] R1-W4: 因果语言不一致**\n\n部分不同意。R1 引用的两处表述在不同层面操作：\n\n- Section 3.1 \"constitutes a binary intervention\"：描述的是**操作层面**——CSD 对文本进行了 controlled manipulation（改变一个 style axis），这在操作上确实是一个 intervention（与 observational study 相对）\n- Section 3.5 / Appendix A \"interventional rather than formal causal evidence\"：描述的是**推断层面**——论文不宣称达到 potential outcomes framework 下的 formal causal identification\n\n这两者并不矛盾：你可以执行一个 intervention（操作上）而不宣称它达到了 formal causal identification（推断上）。Randomized experiments 和 natural experiments 都是 interventional designs，但推断强度不同。\n\n**不过**，我承认对不熟悉因果推断文献的读者，这种区分可能造成困惑。建议在 Section 3.1 中将 \"constitutes a binary intervention\" 修改为 \"approximates a binary intervention\" 或 \"operationalizes a single-axis manipulation\"，避免与 formal causal intervention 的标准定义混淆。\n\n---\n\n### Minor\n\n**[AGREE] R1-M1**: 如果 verbosity 的 NLI gate 通过率不同导致实际 n≠88，Table 1 header 应准确标注。建议统一使用 \"n varies by axis; see Appendix\" 或逐行标注。\n\n**[REBUT] R1-M2**: 不同意 Intro opening example 需要标注为 \"cherry-picked\"。NLP 论文的 opening example 惯例上是选择性的、illustrative 的，用于建立 reader's intuition。论文随后提供了系统性的统计证据（Table 1, Figure 3, 七种统计方法），opening example 的功能是叙事性的而非论证性的。要求标注 \"cherry-picked\" 在学术写作规范中不常见，且可能暗示论文在隐瞒什么——但系统证据已经充分呈现。如果 R1 的担心是 example 的代表性，更好的做法是在附录提供该 example 的完整数据（NLI 分数、两个 judge 评分、position-swapped 结果），而非加标签。\n\n**[AGREE] R1-M3**: DAG 的 orange dashed line 在灰度打印下确实不可辨。建议使用不同的 line pattern (e.g., dash-dot) 或 annotation 来区分。\n\n**[AGREE] R1-M4**: Table 3 (Appendix C) 的 QIC \"---\" 应该报告实际数值或解释为什么省略。我在 PDF 中确认了这一点——所有 9 个 cells 都是 \"---\"，只有 |ΔQIC| 有值。\n\n**[AGREE] R1-M5**: choix library 的 \"default regularization\" 应说明具体形式（L2? pseudo-count? regularization strength?）。这是一个 minor 但 valid 的 reproducibility concern。\n\n---\n\n### Questions\n\n**R1-Q1**: verbosity scaled replication 预期 OR 缩水多少？\n我与 R1 有相同的疑问（我的 Q3）。论文推测 50% shrinkage 将 OR 8-13 降至 4-6.5，仍 style-dominated。但 shrinkage 幅度可能因 axis 而异——verbosity 的效应量大于 formality，large effects 的 shrinkage 百分比可能更小（Nemes & Huang, 2009 的 bias correction 与效应量的关系是 non-linear 的）。实证验证是必要的。\n\n**R1-Q2**: FK grade 是 mediator 还是 confounder？\n关键问题。我在回应 N2 时已详细分析。简要补充：\n- 论文的 DAG (Figure 2) 不包含 FK 作为中介节点——如果 FK 是 S→FK→Y 通路的一部分，控制 FK 会低估 style effect（over-control bias）\n- 但 FK 也可能与 formality 共享 common cause（如原始文本的写作水平），此时控制是正确的\n- 论文需要明确立场，或承认两种解释下的 GPT-4o Style OR 范围是 [2.15, 2.70]\n\n**R1-Q3**: AEval verbosity Claude Style OR=4.76 如何调和 low-sensitivity reference？\n我完全赞同这个质疑。Appendix U (Table 23) 和 Limitations (p9) 确认了这一数据。Claude 的 low-sensitivity 标签只在 LLMBar formality 上成立；AEval verbosity 的 Style OR 4.76 (p<.001) 与 GPT-4o verbosity Style OR 11.34 可比。论文应该承认 Claude 是 \"lower-sensitivity on formality/LLMBar\" 而非全局性的 \"low-sensitivity reference\"。\n\n**R1-Q4**: Direction-aware gate 的 verbosity expansion 是否漏过 R→Q 路径？\n这是一个好的技术问题，但我认为论文提供了充分的 empirical 回应：Appendix F (Section F, 第 212-217 行) 报告了 DA-only vs bidirectional-pass 子集的 BT 比较，无显著差异 (permutation p=.663, Δ=-1.1pp)。五个 judge 的 Fisher exact tests 均 p>.66。这些 empirical 验证表明 DA gate 没有系统性地漏过 quality-altering content。理论上的担忧是合理的，但 empirical evidence 充分缓解了这一风险。\n\n**R1-Q5**: BT regularization sensitivity analysis？\n同意应该提供。choix 的 default regularization (pseudo-count based) 可能对 small-n 估计有影响。建议作者报告无正则化或不同正则化强度下的 BT estimates，特别是对 n=88 的 cells。\n\n---\n\n### 总结\n\nR1 的审稿整体质量很高。三个 Must-Fix 中，我完全同意 N1（small-sample bias 未充分传播）和 N3（Claude reference 证据链矛盾），对 N2 同意需要更多透明度但补充了 mediator vs confounder 的 nuance。Should-Fix 中，W1-W3 我同意，W4 我认为因果语言并非真正不一致而是在不同层面操作，但同意措辞可以改进。Minor issues 除 M2 外均同意。\n\nR1 和我对论文的整体评价接近（均为 3.5 Borderline Conference），核心共识是：执行质量高，但新颖性不足（我比 R1 更强调这一点）、attenuation vs amplification 无法区分、以及 small-sample 定量估计的可靠性。",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1215 · 2026-05-23T09:03:25.442787+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3615
}
```

</details>

---


### Assistant

_source line 1216 · 2026-05-23T09:03:34.721120+00:00_

已完成对 Reviewer 1 全部意见的逐条回应并提交给 Review Director。

总结：
- **Must-Fix**: N1（small-sample OR 膨胀）和 N3（Claude reference 矛盾）完全同意；N2（GPT-4o FK control）同意需要更多正文讨论，但补充了 FK 可能是 mediator 而非 confounder 的重要 nuance
- **Should-Fix**: W1-W3 同意；W4（因果语言）部分反驳——两处表述在不同层面（操作 vs 推断）运作，并不矛盾
- **Minor**: M2（intro cherry-picked）反驳——开头示例的 illustrative 功能是论文写作惯例；其余 M1/M3/M4/M5 同意
- **Questions**: Q1-Q3 与我自己的审稿提出了相同或相似的问题；Q4 我认为论文的 empirical validation（Appendix F, permutation p=.663）已充分回应

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 37

## Round 37

78 recorded events


### User

_source line 1217 · 2026-05-23T14:21:58.486818+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性与完整性**审查。

## 投稿信息
- **Venue**: EMNLP 2026（via ACL Rolling Review, May 2026 cycle）
- **格式**: ACL template, double-blind, Long paper 8 页正文 + unlimited references
- **Limitations**: 必须有，不计入页数限制
- **匿名规则**: Double-blind，禁止透露作者身份
- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/submitted.pdf`

## 你的审查侧重

重点审查以下方面，逐条给出评价（Must-Fix / Should-Fix / Minor / 无问题）：

### 1. 新颖性评估
- "Likert Blindspot" 概念的原创性——是否本质上是心理测量学已知现象（Thurstone 1927, Stevens 1946）在 LLM judge 领域的 domain transfer？
- CSD framework 的增量贡献：NLI-gated content control + per-axis decomposition + position-controlled pairwise 的组合是否足够新颖？
- GEE conditional decomposition 的方法论贡献：是否等同于 factor analysis/SEM？论文声称的三个 LLM-specific distinctions（per-axis structure, GEE decomposition, binary divergence）是否被夸大？
- 与 RATE (Reber et al., 2025) 的差异化是否充分论证？

### 2. Framing 与定位
- Title "The Likert Blindspot" 是否暗示 Likert 有缺陷（单一因果方向），与正文 nuanced 讨论（三种非排他解释）是否矛盾？
- Abstract 中 "consistently divergent" 的措辞——基于 2 primary + 1 exploratory axis，是否过于强势？
- Introduction 的三个 LLM-specific distinctions 是否被过度宣称（"complements" vs "surpasses"）？
- "Systematic pattern" / "consistent" 等用语是否被论文证据充分支撑？

### 3. Related Work 完整性
- 是否遗漏重要相关工作（特别是 LLM judge bias、psychometric evaluation、causal inference in NLP 领域）？
- 对 RATE、Comparative Trap (Jeong et al., 2025)、CASSE、FairJudge 等竞品的定位是否准确和公正？
- 引用格式是否一致（arXiv preprint vs 正式发表）？

### 4. 写作质量
- 论文结构和叙事流是否清晰？
- 信息密度是否合理（8 页内承载 5 judges × 3 axes × 3 benchmarks 的实验）？
- Figure/Table 设计：Figure 1（pipeline）、Figure 2（DAG）、Figure 3（forest plot）、Figure 4（power curve）、Figure 5（GEE bar chart）、Figure 6（heatmap）是否有效传达信息？
- 术语一致性（"style bias" vs "style sensitivity"）
- Abstract 是否超过 200 words（EMNLP 2026 硬约束）？

### 5. 格式合规
- 页数限制：正文是否 ≤ 8 页？
- Limitations section 是否存在且内容适当？
- 匿名性：是否有任何泄露作者身份的内容？
- 引用格式是否符合 ACL 标准？
- Appendix 结构是否合理？

请按照 ARR reviewer guidelines 格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Excitement (1-5) → Overall Assessment。

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

_source line 1218 · 2026-05-23T14:22:07.631735+00:00_

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

_source line 1219 · 2026-05-23T14:22:07.683439+00:00_



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

_source line 1220 · 2026-05-23T14:22:12.911661+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1221 · 2026-05-23T14:22:15.025152+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/submitted.pdf",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1222 · 2026-05-23T14:22:20.349280+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

I found information about the ACL Rolling Review 2026. Here are the key findings:

## Reviewer Guidelines and Policies

ARR developed detailed guidelines and suggestions for each step of the reviewing process, including a list of common problems in both reviews and NLP papers to watch out for.

The reviewer and AC guidelines include codes for (meta-)review issues (I1-I12) that can be reported by the authors.

## Review Form Criteria

ARR considers egregious cases reported by chairs, including the cases of extremely terse reviews, unprofessional tone, and LLM-generated reviews.

## Reviewer Responsibilities and Incentives

Starting from May 2025, ACL introduces an awards policy for reviewers & chairs where area chairs or senior area chairs may nominate great
…[truncated 639 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7437
}
```

</details>

---


### Tool result

_source line 1223 · 2026-05-23T14:22:21.405789+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.5}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 605.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 475.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 473.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 525.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 470.5}], \"total_pages\": 20, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/a
…[truncated 77 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6380
}
```

</details>

---


### Tool call

_source line 1224 · 2026-05-23T14:22:27.628722+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. I need: 1) All review form fields/dimensions (soundness, excitement, overall assessment, etc.) 2) The rating scales for each dimension 3) Any specific guidelines for what constitutes each score level 4) Guidelines on what reviewers should evaluate"
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
    "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. I need: 1) All review form fields/dimensions (soundness, excitement, overall assessment, etc.) 2) The rating scales for each dimension 3) Any specific guidelines for what constitutes each score level 4) Guidelines on what reviewers should evaluate"
  }
}
```

</details>

---


### Tool call

_source line 1225 · 2026-05-23T14:22:28.232469+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p1.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 1226 · 2026-05-23T14:22:29.086557+00:00_



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

_source line 1227 · 2026-05-23T14:22:29.087005+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p2.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1228 · 2026-05-23T14:22:29.640154+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p3.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1229 · 2026-05-23T14:22:30.042737+00:00_



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

_source line 1230 · 2026-05-23T14:22:30.043179+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p4.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1231 · 2026-05-23T14:22:30.448348+00:00_



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

_source line 1232 · 2026-05-23T14:22:30.800032+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---


### Tool result

_source line 1233 · 2026-05-23T14:22:33.058587+00:00_

# ARR Review Form Criteria and Scoring

Based on the guidelines, here are the key review form dimensions:

## Primary Scoring Dimensions

**1. Soundness**
- Assesses technical validity and methodological rigor
- Must be justified by review text; low scores require explicit explanation
- "Low soundness scores without finding any major faults" indicates the review lacks credibility

**2. Excitement**
- Reflects personal interest and subjective appeal
- Orthogonal to soundness assessment
- Does not require explicit justification
- Captures reviewer enthusiasm independent of technical quality

**3. Overall Recommendation**
- Composite score combining soundness, excitement, novelty, and impact
- Guides acceptance decisions for venues
- Papers can merit main conference consideration even if reviewer lacks personal enthusiasm, if contribution shows significant potential impact

## Evaluation Guidelines

Reviewers should assess papers across dimensions including:
- Technical soundness and proof validity
- Novelty and originality
- Contribution clarity and scope appropriateness
- Reproducibility and experimental rigor
- Ethical considerations
- Writing quality and clarity

## Key Assessment Principles

The guidelines emphasize that "all papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible," though excitement varies by reviewer preference.

**Note:** The document does not specify exact numerical scales (e.g., 1-5 or 1-10) for these dimensions, focusing instead on conceptual frameworks for evaluation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5429
}
```

</details>

---


### Tool call

_source line 1234 · 2026-05-23T14:22:39.537470+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p5.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1235 · 2026-05-23T14:22:40.441224+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1236 · 2026-05-23T14:22:40.592150+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p6.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1237 · 2026-05-23T14:22:40.945462+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p7.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1238 · 2026-05-23T14:22:41.548729+00:00_



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

_source line 1239 · 2026-05-23T14:22:41.549150+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p8.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1240 · 2026-05-23T14:22:42.506496+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1561
}
```

</details>

---


### Tool result

_source line 1241 · 2026-05-23T14:22:42.760111+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1210
}
```

</details>

---


### Tool call

_source line 1242 · 2026-05-23T14:22:49.234431+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/submitted.pdf",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "9-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1243 · 2026-05-23T14:22:50.743614+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 558.4}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 579.2}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 589.4}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 437.6}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 426.2}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 445.3}], \"total_pages\": 20, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_
…[truncated 91 chars]

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

_source line 1244 · 2026-05-23T14:22:56.515530+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p9.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1245 · 2026-05-23T14:22:56.968572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p10.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1246 · 2026-05-23T14:22:57.927274+00:00_



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

_source line 1247 · 2026-05-23T14:22:57.930222+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 961
}
```

</details>

---


### Tool call

_source line 1248 · 2026-05-23T14:22:57.930572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p11.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1249 · 2026-05-23T14:22:58.233839+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p12.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1250 · 2026-05-23T14:22:59.944736+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2014
}
```

</details>

---


### Tool result

_source line 1251 · 2026-05-23T14:23:00.902731+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2668
}
```

</details>

---


### Tool call

_source line 1252 · 2026-05-23T14:23:06.280872+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p13.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1253 · 2026-05-23T14:23:06.848081+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p14.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1254 · 2026-05-23T14:23:07.283870+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1002
}
```

</details>

---


### Tool call

_source line 1255 · 2026-05-23T14:23:07.284273+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p15.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 1256 · 2026-05-23T14:23:07.720613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p16.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1257 · 2026-05-23T14:23:08.537952+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1689
}
```

</details>

---


### Tool result

_source line 1258 · 2026-05-23T14:23:09.439314+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2155
}
```

</details>

---


### Tool result

_source line 1259 · 2026-05-23T14:23:09.591567+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1870
}
```

</details>

---


### Tool call

_source line 1260 · 2026-05-23T14:23:15.619023+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "17-20",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "17-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1261 · 2026-05-23T14:23:16.275696+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.9}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.3}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p19.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 445.1}, {\"page\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p20.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 301.2}], \"total_pages\": 20, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 1262 · 2026-05-23T14:23:20.689475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p17.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1263 · 2026-05-23T14:23:21.442651+00:00_



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

_source line 1264 · 2026-05-23T14:23:21.643933+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p18.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 1265 · 2026-05-23T14:23:21.995171+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p19.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1266 · 2026-05-23T14:23:22.299211+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 1267 · 2026-05-23T14:23:22.299699+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p20.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 1268 · 2026-05-23T14:23:23.007706+00:00_



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


### Tool result

_source line 1269 · 2026-05-23T14:23:23.012656+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 712
}
```

</details>

---


### Tool call

_source line 1270 · 2026-05-23T14:23:30.700064+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all dimensions, their exact rating scales (1-5, etc.), and what each score level means. I need the exact fields: soundness, excitement/novelty, overall assessment, confidence, and any other dimensions."
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
    "prompt": "Extract the complete review form with all dimensions, their exact rating scales (1-5, etc.), and what each score level means. I need the exact fields: soundness, excitement/novelty, overall assessment, confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 1271 · 2026-05-23T14:23:32.662195+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
  "limit": "100"
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
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1272 · 2026-05-23T14:23:32.662644+00:00_

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
41	\textbf{Residual confounding.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself.
43	Although formality effects survive logistic adjustment (OR $= 2.32$, $p = 0.006$), residual confounding is not fully eliminated; definitive resolution requires human ground-truth comparison of Likert and pairwise judgments on identical pairs.
44	
45	\textbf{Detection vs.\ amplification.}
46	The Blindspot may partly reflect pairwise format amplification \citep{jeong2025comparative} rather than pure detection.
47	Six controls bound this risk (\S\ref{sec:amplification}), but we cannot precisely quantify the amplification factor without a ground-truth bias magnitude.
48	
49	\textbf{Scope.}
50	CSD applies only to surface-level axes whose rewrites preserve semantic content; a tone pilot (assertive $\to$ hedging) was rejected by the NLI gate.
51	Primary analyses use LLMBar ($n = 100$) with five judges; generalization to additional axes, benchmarks, and judges remains open.
52	
53	\section*{Code and Data}
54	Code and data will be released upon acceptan
…[truncated 95 chars]

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


### Tool result

_source line 1273 · 2026-05-23T14:23:38.653542+00:00_

# ACL Rolling Review Form - Complete Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- 4: Quite sure; unlikely but possible to miss something affecting ratings
- 3: Pretty sure; may have missed details despite general familiarity
- 2: Willing to defend evaluation, but fairly likely missed details or novelty assessment uncertain
- 1: Outside expertise area or paper very difficult to understand

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- 5: "Excellent: This study is one of the most thorough I have seen, given its type."
- 4: Strong; provides sufficient support with optional extra experiments
- 3: Acceptable; sufficient support for main claims; minor points need details
- 2: Poor; main claims insufficiently supported; major technical problems
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- 5: "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- 4: Exciting; would mention to others or attend presentation
- 3: Interesting; might mention points or attend if time permits
- 2: Potentially Interesting; doesn't resonate personally but may appeal to community
- 1: "Not Exciting: this paper does not resonate with me, and I don't think it would with others"

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- 5: Consider for Award (top 2.5% papers)
- 4.5: Borderline Award
- 4: Conference acceptance
- 3.5: Borderline Conference
- 3: Findings acceptance
- 2.5: Borderline Findings
- 2: Resubmit next cycle with substantial revisions
- 1.5: Resubmit after next cycle; substantial revisions needed
- 1: "Do not resubmit: This paper has to be fully redone, or it is not relevant"

## 5. **Reproducibility**
Scale: 1-5
- 5: "They could easily reproduce the results."
- 4: Mostly reproducible; minor variation possible
- 3:
…[truncated 251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7953
}
```

</details>

---


### Tool call

_source line 1274 · 2026-05-23T14:23:42.720345+00:00_

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

_source line 1275 · 2026-05-23T14:23:43.173438+00:00_

1	\begin{abstract}
2	Likert and pairwise scoring produce divergent sensitivity across surface-level style axes when applied to LLM judges.
3	We define this divergence---the \emph{Likert Blindspot}---as significant pairwise sensitivity absent from Likert, admitting non-exclusive explanations including measurement attenuation, format amplification, and construct divergence.
4	We introduce Controlled Style Decomposition (CSD), a black-box diagnostic quantifying this divergence via NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison.
5	Across five judges from four providers and two primary axes (formality, verbosity), pairwise reaches significance ($p < 0.001$) where Likert does not ($p > 0.17$), with signal loss exceeding 60\%---replicated across three benchmarks and confirmed by seven statistical methods.
6	GEE decomposition reveals distinct per-axis confound structures: verbosity bias is style-dominated (Style OR $8$--$13$, Originality OR ${<}1$), while formality reflects joint style--quality contributions.
7	One judge (Claude Sonnet~4) exhibits benchmark-dependent sensitivity, illustrating bias as a judge$\times$benchmark interaction; non-tie concordance (76.6\%, $p < .001$) is more consistent with attenuation than construct divergence.
8	Likert-only audits may thus fail to surface style-driven preferences that propagate through pairwise-based alignment pipelines.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1276 · 2026-05-23T14:23:43.173745+00:00_

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

_source line 1277 · 2026-05-23T14:23:43.224141+00:00_

1	\section{Introduction}
2	
3	\emph{``What is the average height for a male?''} --- given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \emph{higher} on a 1--10 Likert scale (8 vs.\ 5), yet consistently selects the formal variant in pairwise comparison.
4	Same judge, same texts, opposite conclusions.
5	We term this the \emph{Likert Blindspot}---an operational descriptor for the measurement-mode divergence where pairwise comparison detects statistically significant style sensitivity that Likert scoring fails to detect on the same data, without committing to a specific causal mechanism.
6	This divergence admits multiple non-exclusive explanations---Likert measurement attenuation, pairwise format amplification \citep{jeong2025comparative}, or construct-level differences between absolute and comparative evaluation---which our controlled design bounds but cannot definitively adjudicate (\S\ref{sec:likert_pairwise}).
7	Under construct divergence, pairwise and Likert modes may measure distinct constructs---comparative sensitivity versus absolute quality judgment---in which case the divergence reflects measurement scope rather than measurement failure, with different practical implications for audit design (\S\ref{sec:likert_pairwise}).
8	This example reflects a consistent pattern: surface-level style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}, with 76--92\% of preferences originating from style cues \citep{li2026preference,soumik2026judging}.
9	
10	LLM judges are central infrastructure for NLP evaluation and alignment training (RLHF, DPO), where judge preferences serve as reward signals; any systematic bias propagates through both evaluation leaderboards and model development pipelines.
11	Despite this, existing approaches address individual requirements (multi-dimensional style analysis \citep{casse2026concise,wang2026fairjudge}, interventional design \cit
…[truncated 3702 chars]

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

_source line 1278 · 2026-05-23T14:23:48.846608+00:00_

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

_source line 1279 · 2026-05-23T14:23:49.147846+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Two lines of work motivate our approach: interventional methods for diagnosing judge bias, and measurement theory on the sensitivity of different elicitation formats.
5	
6	\paragraph{Interventional Approaches to Judge Bias}
7	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
8	\citet{reber2025rate} propose RATE, a framework that rewrites model outputs along style attributes using imperfect counterfactuals and measures the causal effect on reward model scores via Likert-scale Average Treatment Effect (ATE).
9	RATE applies a correction term to account for rewriting imperfections, but its reliance on Likert ATE as the primary metric is a vulnerability: our experiments show that Likert scoring exhibits a ceiling effect in which 60\% of style-transformed pairs receive identical integer scores, yielding non-significant ATE estimates ($p = 0.332$) for the same interventions that pairwise comparison detects at $p = 0.006$.
10	Whether this format sensitivity extends to RATE's broader attribute space is an open question; our results motivate independent validation of Likert-based effect estimates alongside pairwise measures.
11	CSD differs from RATE in three respects: it targets individual style axes rather than general attributes, it measures bias through position-controlled pairwise comparison rather than Likert ATE, and it enforces content preservation via NLI entailment gating rather than post-hoc correction for imperfect rewrites.
12	\citet{counterfactual2025rhetorical} also adopt an interventional LLM-based design, rewriting texts to measure rhetorical style effects and aggregating preferences with a Bradley-Terry model.
13	Their framework operates at persona-level granularity (e.g., ``writes like a professor''), whereas CSD intervenes on specific style axes (e.g., formality, conciseness) and uses a sign test with position control r
…[truncated 5573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1280 · 2026-05-23T14:23:49.198485+00:00_

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

_source line 1281 · 2026-05-23T14:23:49.249133+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Style-Controlled Rewriting}
5	\label{sec:rewriting}
6	
7	We isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.
8	For each text, an instruction-tuned LLM (Qwen3-32B) classifies its current style along the target axis (e.g., formal vs.\ casual via binary classification).
9	It then rewrites the text toward the opposite pole (temperature 0.7, selected to balance diversity with coherence in pilot experiments) according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').
10	This produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.
11	Each operation approximates a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}).
12	To control for rewriting artifact bias---the possibility that the judge prefers original text over any rewrite regardless of style---we additionally generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
13	
14	\subsection{Content Preservation Verification}
15	\label{sec:nli_gate}
16	
17	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
18	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large fine-tuned on MNLI \citep{williams2018broad} with an entailment threshold of 0.90, selected as the threshold above which NLI performance plateaus (Appendix~\ref{app:nli_sweep}).
19	For axes that preserve information density (formality, register), we apply standard bidirectional entailment: both 
…[truncated 5577 chars]

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

_source line 1282 · 2026-05-23T14:23:58.434479+00:00_

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

_source line 1283 · 2026-05-23T14:23:58.585488+00:00_

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
11	Exploratory analyses use uncorrected $p$-values; confirmatory analyses (pipeline validity) are evaluated at $\alpha = 0.05$ without additional correction.
12	Bradley-Terry parameters \citep{bradley1952rank,luce1959individual} are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the \texttt{choix} Python library's default L2 regularization ($\alpha = 10^{-6}$).
13	In binary-choice BT models, IIA is structurally satisfied; the direction asymmetry in Appendix~\ref{app:bt_gof} (formality: formal-origin 88.9\% vs.\ casual-origin 52.6\%, Fisher $p = 0.015$) reflects heterogeneous treatment effects rather than IIA violation.
14	All bootstrap confidence intervals are percentile CIs from 10{,}000 pair-level resamples with seed 42.
15	GEE models use exchangeable working correlation with sandwich standard errors (robust to correlation misspecification), justified by near-zero estimated within-pair correlations ($\hat{\alpha} \in [-0.25, +0.11]$; Appendix~\ref{app:gee_diagnostics}).
16	
17	\paragraph{Model selection.}
18	Target judges span four architectures: GPT-4o (2024-08-06), Qwen3-32B-Instruct (also serving as rewriter), Llama
…[truncated 16147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1284 · 2026-05-23T14:23:58.585837+00:00_

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

_source line 1285 · 2026-05-23T14:23:58.636421+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	CSD yields two findings.
5	First, the \emph{Likert Blindspot}: pairwise and Likert scoring produce divergent verdicts---complete at moderate bias ($d \to 0$ at $n = 355$), ${>}60\%$ signal loss at stronger effects---across four judges (Gemini weaker on formality), three benchmarks, and seven methods.
6	Second, GEE decomposition reveals distinct per-axis confound structures---verbosity is style-dominated, formality conditional, register judge-dependent.
7	Non-tie concordance (76.6\%, $p < .001$) is more consistent with attenuation than construct divergence; single-format audits risk systematic blind spots.
8	

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

_source line 1286 · 2026-05-23T14:26:16.644491+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/---/ /g; s/--/ /g; s/  */ /g' | wc -w",
  "description": "Count abstract word count roughly"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/---/ /g; s/--/ /g; s/  */ /g' | wc -w",
    "description": "Count abstract word count roughly"
  }
}
```

</details>

---


### Tool result

_source line 1287 · 2026-05-23T14:26:16.796809+00:00_

169

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1288 · 2026-05-23T14:28:39.752720+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见：新颖性与完整性\n\n## 论文信息\n- **Title**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n- **Venue**: EMNLP 2026 via ACL Rolling Review (May 2026 cycle)\n\n---\n\n## Summary\n\n本文定义了 \"Likert Blindspot\"——LLM judge 的 pairwise comparison 能检测到风格敏感性而 Likert scoring 检测不到的现象。提出 Controlled Style Decomposition (CSD) 框架，整合 NLI-gated 内容控制、per-axis 风格分解和 position-controlled pairwise comparison。在 4-5 个 judge、3 个 benchmark、2-3 个风格轴上实验，结果一致显示 Likert 失灵（7 种统计方法全部确认）。GEE 条件分解揭示 per-axis confound structure：verbosity 是 style-dominated（Style OR 8–13），formality 是 quality-confounded。论文坦诚提出三种非排他解释（attenuation, amplification, construct divergence），统计工作扎实。\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 / 5 — Borderline Conference\n\n**一句话总结**: 实验执行出色、统计严谨，但核心发现本质上是经典心理测量学原理（Thurstone 1927）在 LLM judge 领域的系统验证，新颖性为 moderate；per-axis confound structure 是唯一genuinely novel 的经验发现。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4 / 5 | 方法论严谨，多层控制设计（NLI gating, position swap, double-rewrite, debiased prompting），七种统计方法交叉验证，Holm-Bonferroni 校正。小样本和 rewriter-judge overlap 是次要问题。 |\n| Excitement | 3 / 5 | 对 LLM judge 审计实践有直接指导意义，GEE per-axis 分解是有用的方法贡献。但核心 insight（pairwise 比 Likert 更敏感）对熟悉测量理论的读者不新鲜。 |\n| Reproducibility | 4 / 5 | 方法描述详细，统计流程完整，承诺 code/data release。模型 API 版本明确（GPT-4o 2024-08-06 等）。 |\n| Confidence | 4 / 5 | 熟悉心理测量学文献、LLM judge 评估和因果推断方法。 |\n\n---\n\n## 主要优势\n\n**S1. 卓越的实验严谨性。** 六层控制设计（NLI gate, position swap, double-rewrite, debiased prompting, cross-rewriter validation, GEE confound decomposition）在 LLM judge bias 文献中属于最严格的方法控制之一。七种统计方法全部一致确认 Blindspot（Table 14, Appendix M），bootstrap CI、TOST equivalence testing、Bayesian equivalence testing 的组合使用展现了统计成熟度。\n\n**S2. Per-axis confound structure 是genuinely novel 的发现。** GEE decomposition 揭示 verbosity 是 style-dominated（Style OR 8–13, Originality OR < 1）而 formality 是 quality-confounded（两个 predictor 都显著），这种 per-axis 差异不是经典心理测量学能预测的，对 LLM judge 审计策略有直接实践意义——不同风格轴需要不同的审计方法。\n\n**S3. 诚实的 claim hedging。** 论文主动提出三种非排他解释（§5.1），明确承认 residual confounding 未完全消除（Limitations），用 \"complements\" 而非 \"surpasses\" 描述与经典框架的关系。这在 LLM 领域论文中属于少见的审慎态度。\n\n**S4. 跨 judge/benchmark 复制规模。** 5 judges × 3 benchmarks × 3 axes 的实验矩阵（虽然部分为 exploratory），加上 n=355 的 scaled replication，提供了远超单一实验的证据强度。Claude Sonnet 4 的 benchmark-dependent 结果（§5.3）是一个有价值的 discriminative validity 证据。\n\n**S5. 实践相关性强。** 结论直接指向 LLM alignment pipeline 的审计盲区——如果 Likert-based reward model 评估漏检了 pairwise 能发现的风格偏差，那么通过 RLHF/DPO 训练的模型可能继承未被检测的 style preferences。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 新颖性定位不够精确——核心发现是 Thurstone 1927 的 domain transfer，而非新现象\n\n- 具体位置：Title, Abstract, §1 Introduction (para 3-4), §5.1\n- 问题：论文的核心经验发现——pairwise comparison 比 Likert 更能检测 style sensitivity——本质上是 Thurstone (1927) Law of Comparative Judgment 在 LLM judge 领域的验证。论文在 §1 para 3 确实引用了 Thurstone 并说 \"quantitatively consistent\"，但 Title \"The Likert Blindspot\" 和 Abstract 的 framing 仍然暗示这是一个新发现的现象。Introduction 声称的三个 \"LLM-specific distinctions\" 中，(c) \"near-complete binary split\" 被论文自己承认 \"consistent with classical predictions when accounting for effect-size-dependent power\"——这不是一个 LLM-specific distinction，而是经典理论在该效应量下的预测结果。\n- 为什么影响接收：ARR Excitement 维度要求 novelty。如果审稿人熟悉测量理论，会认为核心 contribution 是一个 well-executed replication study 而非 discovery。这直接影响 Conference vs Findings 的定位。\n- 建议修改方向：(1) 将 Introduction 的三个 LLM-specific distinctions 缩减为两个，删除 (c) binary split 或将其降级为\"与经典理论一致的验证\"；(2) 更清晰地将 contribution 定位为 \"systematic empirical demonstration + per-axis structure discovery + practical diagnostic tool\"，而非 \"new phenomenon\"；(3) 考虑在 Title/Abstract 中添加类似 \"extends classical measurement theory to LLM evaluation\" 的表述。\n\n**N2** [critical] Scaled replication 覆盖不足——仅一个 cell 有大样本验证\n\n- 具体位置：§5.1 para 2, Table 1\n- 问题：n=355 的 scaled replication 仅覆盖 Qwen3-32B × formality 这一个 cell。这是论文最关键的论点支柱——用大样本证明 Likert 的 d→0 是结构性的而非 power 不足。但其他 11 个 primary/confirmatory cells（GPT-4o × formality/verbosity, Llama-70B × formality/verbosity, Gemini × formality/verbosity 等）都只有 n=86–88，无法排除这些 cells 的 Blindspot 仅仅是 power 问题。\n- 为什么影响接收：论文声称 \"consistent pattern rather than an isolated anomaly\"（§1 Contribution 2），但只有一个 cell 用大样本验证了这不是 power artifact。这是一个可证伪但未被充分验证的 claim。尤其 Gemini formality（BT 仅 57.4%，效应最弱）如果做 scaled replication 可能不复现 d→0 的结论。\n- 建议修改方向：(1) 对至少一个 verbosity cell 做 scaled replication（因为 verbosity 是最强效应，但 Likert d 也接近零——这可以更干净地证明结构性衰减）；(2) 如果资源限制无法做更多 replication，应在 Limitations 明确承认这一 coverage gap，并将 \"consistent pattern\" 的 claim 弱化为 \"observed pattern, with structural attenuation confirmed for one judge×axis cell\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Title \"The Likert Blindspot\" 暗示单一因果方向，与正文 nuanced 讨论矛盾\n\n- 具体位置：Title, §5.1 \"Interpreting the divergence\"\n- 问题：\"Blindspot\" 一词暗示 Likert 有缺陷（漏检），预设了 attenuation 解释为主导。但 §5.1 明确提出三种非排他解释，包括 pairwise amplification（可能是 pairwise 过度放大而非 Likert 漏检）和 construct divergence（两种模式测量不同构念）。如果 amplification 是主因，那么 \"Blindspot\" 的描述就不准确——Likert 没有\"盲点\"，只是 pairwise 有\"放大镜\"。\n- 建议：(1) 在 §1 更早处对 \"Blindspot\" 进行操作化定义（论文在 §1 para 2 做了，但可以更突出）；(2) 考虑在 Abstract 中加入一句明确的 hedge：e.g., \"which we term the Likert Blindspot as an operational descriptor without committing to a specific causal mechanism\"（部分已在正文中，但 Abstract 缺少）。实际上我看到 Introduction 第二段有这个 hedge，但 Abstract 和 Title 没有传达。\n\n**W2** [warning] Qwen3-32B 同时担任 rewriter 和 target judge 的循环依赖\n\n- 具体位置：§3.1, §4.1, Appendix E\n- 问题：Qwen3-32B 既是风格改写器又是被测 judge。虽然 Appendix E 展示了独立 GPT-4o rewriter 的验证（BT 从 66.5% 降至约 57%，降幅 22%），但这个 22% 的降幅本身值得关注——它说明 evaluator-producer overlap 确实 inflate 了效应量。论文报告的 Qwen3-32B 结果可能系统性偏高。\n- 建议：(1) 在 §4.1 或 Table 1 脚注中标注 Qwen3-32B 的 evaluator-producer overlap caveat；(2) 如果可能，对 Qwen3-32B 的所有主要分析使用 GPT-4o rewriter 数据作为 robustness check；(3) 考虑 Table 1 中标注 Qwen3-32B 结果可能有 ~20% 的上行偏差。\n\n**W3** [warning] Register 轴结果弱且 exploratory，但在 Abstract/Contribution 中占有隐含地位\n\n- 具体位置：Abstract (\"two primary axes\"), Table 1 (register rows), §5.3\n- 问题：Register 轴在 Table 1 中有 3 行结果（GPT-4o, Qwen3, Llama-70B），但 BT 仅 .553–.635，效应远弱于 formality (.574–.695) 和 verbosity (.708–.773)。更关键的是，register 的 GEE 结构（Table 2）显示 Originality OR 远高于 Style OR（Qwen3: 5.72 vs 1.91），说明 register 效应可能主要由 quality confounding 驱动。论文标注为 \"exploratory\"，但在 cross-benchmark heatmap (Figure 6) 和 GEE table (Table 2) 中占了相当篇幅。\n- 建议：将 register 结果完全移至 Appendix，正文只保留一句 \"an exploratory register axis yielded weaker, quality-confounded effects (Appendix X)\"。这会释放正文空间给更重要的 scaled replication 或 cross-benchmark 讨论。\n\n**W4** [warning] \"Systematic pattern\" / \"consistent\" 等措辞与例外情况的张力\n\n- 具体位置：§1 Contribution 2, §6 Conclusion\n- 问题：Contribution 2 声称 \"revealing measurement-mode divergence as a consistent pattern rather than an isolated anomaly\"。但实际数据中：(1) Claude Sonnet 4 不显示一般性 Blindspot（Table 1, BT .541–.562, n.s.）；(2) Gemini formality 效应弱（BT 57.4%, Style OR 1.64 n.s.）；(3) cross-benchmark replication 仅 6/24 cells 达到显著。论文用 \"three exceptions (‡)\" 处理例外，但 \"consistent\" 一词在有 ~30% exception rate 的情况下值得审慎使用。\n- 建议：将 \"consistent pattern\" 改为 \"predominant pattern\" 或 \"majority pattern\"；在 §6 Conclusion 中量化复制率（e.g., \"8/11 primary+confirmatory cells, 6/24 cross-benchmark cells\"）。\n\n---\n\n## Minor 问题（不影响接收）\n\n**M1.** 术语一致性：\"style bias\" 和 \"style sensitivity\" 在论文中交替使用（e.g., Abstract 用 \"sensitivity\"，§5.1 标题用 \"Blindspot\" 暗示 \"bias\"）。建议统一——鉴于论文立场是 agnostic about mechanism，\"style sensitivity\" 更准确。\n\n**M2.** Figure 5 (GEE bar chart, p.8) 的 y 轴标签 \"Odds Ratio\" 在 log scale 上可能对不熟悉 GEE 的读者造成困惑。建议添加 \"log scale\" 标注或在 caption 中明确说明。\n\n**M3.** §3.2 提到 \"DeBERTa-v3-large fine-tuned on MNLI\" 作为 NLI gate，但未说明该模型在 out-of-domain（非 MNLI distribution）文本上的性能是否经过验证。human annotation（§5.4）部分验证了这一点，但 NLI model 本身的 domain-shift robustness 未被讨论。\n\n**M4.** Table 1 的 \"Cat.\" 列标记（†, †_e, †_c, ---）需要读者频繁查阅脚注。建议直接使用文字标签如 \"Blind\", \"Expl\", \"Conf\", \"Neither\"。\n\n**M5.** §5.2 引用 Nemes et al. 2009 解释小样本上行偏差。这个引用是 meta-analysis 领域的，应用到 GEE OR 的 small-sample bias 上是否完全对应，可以补充说明。\n\n---\n\n## Questions to Authors\n\n**Q1.** §5.1 的 non-tie concordance analysis（76.6%, p < .001）是论文区分 attenuation 和 construct divergence 的关键证据。但 76.6% 的 concordance 意味着 23.4% 的 discordance——这个 discordance rate 是否足够低以排除 partial construct divergence？论文承认 \"partial construct divergence remains at weaker effect sizes\"，那么具体在哪个效应量阈值以下 construct divergence 可能成为主导解释？\n\n**Q2.** 100-point continuous Likert scale（Appendix O）仍然显示 p > 0.15。这是一个重要的 robustness check。但 Appendix O 是否控制了 judges 使用 continuous scale 时的行为变化（e.g., 是否有 evidence 表明 judges 真的利用了 continuous scale 的 granularity，而不是仍然只使用少数离散值）？\n\n**Q3.** 论文使用 Qwen3-32B 作为 style classifier（§3.1）判断文本当前风格。如果 classifier 本身有系统性偏差（e.g., 倾向于将高质量文本分类为 formal），这是否会在 data generation 阶段引入 confounding？\n\n**Q4.** GEE 的 exchangeable working correlation 假设在 paired comparison data 中是否合理？论文提到 within-pair correlations 接近零（α̂ ∈ [−0.25, +0.11]），但 −0.25 的估计值似乎不算\"接近零\"。这是否影响 sandwich standard errors 的可靠性？\n\n---\n\n## Missing References\n\n论文的 Related Work 相当全面（~40 引用），但以下方向可以加强：\n\n1. **Item Response Theory (IRT) 在 NLG evaluation 中的应用**：论文简短引用了 Embretson & Reise (2000)，但 IRT 提供了更正式的框架来量化不同 measurement mode 的信息函数差异。近期有 IRT 用于 LLM evaluation 的工作（e.g., Polo et al., 2024, \"TinyBenchmarks\"），可以补充讨论 IRT 视角下 Likert vs pairwise 的 information gain 差异。\n\n2. **Likert scale anchoring effects**：不同 LLM judge 可能以不同方式解释 1-10 scale 的锚点（e.g., 有些 judge 倾向使用中间值，有些使用极端值），这是 Likert 信号衰减的已知机制之一（Krosnick 1999 已引用，但 scale anchoring 的具体讨论较少）。\n\n3. **Pairwise comparison 在 RLHF 中的 amplification 问题**：除了 Jeong et al. (2025) Comparative Trap，还有 Munos et al. (2023) \"Nash Learning from Human Feedback\" 等讨论 pairwise preference 中的 noise amplification。\n\n---\n\n## Scoring Summary\n\n| 维度 | 分数 |\n|------|------|\n| **Soundness** | 4 / 5 |\n| **Excitement** | 3 / 5 |\n| **Overall Assessment** | 3.5 / 5 (Borderline Conference) |\n| **Reproducibility** | 4 / 5 |\n| **Confidence** | 4 / 5 |\n\n**Overall Justification**: 论文在实验设计和统计分析方面达到了很高的标准，per-axis confound structure 是一个有价值的发现，CSD 作为实用诊断工具有明确的应用价值。将其拉向 3.5 而非 3.0 的主要因素是：(1) 实验规模和控制的thoroughness 在同类工作中突出；(2) GEE per-axis 分解提供了超越 Thurstone 经典框架的 genuinely new insight；(3) 实践相关性强（directly actionable for RLHF/DPO pipeline audits）。阻止其达到 4.0 的因素是：(1) 核心现象是经典测量理论的 domain transfer，novelty ceiling 有限；(2) scaled replication 仅覆盖 1/12 cells；(3) \"consistent pattern\" 的 claim 与 ~30% exception rate 有张力。\n",
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
    "text": "\n# Reviewer 2 审稿意见：新颖性与完整性\n\n## 论文信息\n- **Title**: The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\n- **Venue**: EMNLP 2026 via ACL Rolling Review (May 2026 cycle)\n\n---\n\n## Summary\n\n本文定义了 \"Likert Blindspot\"——LLM judge 的 pairwise comparison 能检测到风格敏感性而 Likert scoring 检测不到的现象。提出 Controlled Style Decomposition (CSD) 框架，整合 NLI-gated 内容控制、per-axis 风格分解和 position-controlled pairwise comparison。在 4-5 个 judge、3 个 benchmark、2-3 个风格轴上实验，结果一致显示 Likert 失灵（7 种统计方法全部确认）。GEE 条件分解揭示 per-axis confound structure：verbosity 是 style-dominated（Style OR 8–13），formality 是 quality-confounded。论文坦诚提出三种非排他解释（attenuation, amplification, construct divergence），统计工作扎实。\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 / 5 — Borderline Conference\n\n**一句话总结**: 实验执行出色、统计严谨，但核心发现本质上是经典心理测量学原理（Thurstone 1927）在 LLM judge 领域的系统验证，新颖性为 moderate；per-axis confound structure 是唯一genuinely novel 的经验发现。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4 / 5 | 方法论严谨，多层控制设计（NLI gating, position swap, double-rewrite, debiased prompting），七种统计方法交叉验证，Holm-Bonferroni 校正。小样本和 rewriter-judge overlap 是次要问题。 |\n| Excitement | 3 / 5 | 对 LLM judge 审计实践有直接指导意义，GEE per-axis 分解是有用的方法贡献。但核心 insight（pairwise 比 Likert 更敏感）对熟悉测量理论的读者不新鲜。 |\n| Reproducibility | 4 / 5 | 方法描述详细，统计流程完整，承诺 code/data release。模型 API 版本明确（GPT-4o 2024-08-06 等）。 |\n| Confidence | 4 / 5 | 熟悉心理测量学文献、LLM judge 评估和因果推断方法。 |\n\n---\n\n## 主要优势\n\n**S1. 卓越的实验严谨性。** 六层控制设计（NLI gate, position swap, double-rewrite, debiased prompting, cross-rewriter validation, GEE confound decomposition）在 LLM judge bias 文献中属于最严格的方法控制之一。七种统计方法全部一致确认 Blindspot（Table 14, Appendix M），bootstrap CI、TOST equivalence testing、Bayesian equivalence testing 的组合使用展现了统计成熟度。\n\n**S2. Per-axis confound structure 是genuinely novel 的发现。** GEE decomposition 揭示 verbosity 是 style-dominated（Style OR 8–13, Originality OR < 1）而 formality 是 quality-confounded（两个 predictor 都显著），这种 per-axis 差异不是经典心理测量学能预测的，对 LLM judge 审计策略有直接实践意义——不同风格轴需要不同的审计方法。\n\n**S3. 诚实的 claim hedging。** 论文主动提出三种非排他解释（§5.1），明确承认 residual confounding 未完全消除（Limitations），用 \"complements\" 而非 \"surpasses\" 描述与经典框架的关系。这在 LLM 领域论文中属于少见的审慎态度。\n\n**S4. 跨 judge/benchmark 复制规模。** 5 judges × 3 benchmarks × 3 axes 的实验矩阵（虽然部分为 exploratory），加上 n=355 的 scaled replication，提供了远超单一实验的证据强度。Claude Sonnet 4 的 benchmark-dependent 结果（§5.3）是一个有价值的 discriminative validity 证据。\n\n**S5. 实践相关性强。** 结论直接指向 LLM alignment pipeline 的审计盲区——如果 Likert-based reward model 评估漏检了 pairwise 能发现的风格偏差，那么通过 RLHF/DPO 训练的模型可能继承未被检测的 style preferences。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 新颖性定位不够精确——核心发现是 Thurstone 1927 的 domain transfer，而非新现象\n\n- 具体位置：Title, Abstract, §1 Introduction (para 3-4), §5.1\n- 问题：论文的核心经验发现——pairwise comparison 比 Likert 更能检测 style sensitivity——本质上是 Thurstone (1927) Law of Comparative Judgment 在 LLM judge 领域的验证。论文在 §1 para 3 确实引用了 Thurstone 并说 \"quantitatively consistent\"，但 Title \"The Likert Blindspot\" 和 Abstract 的 framing 仍然暗示这是一个新发现的现象。Introduction 声称的三个 \"LLM-specific distinctions\" 中，(c) \"near-complete binary split\" 被论文自己承认 \"consistent with classical predictions when accounting for effect-size-dependent power\"——这不是一个 LLM-specific distinction，而是经典理论在该效应量下的预测结果。\n- 为什么影响接收：ARR Excitement 维度要求 novelty。如果审稿人熟悉测量理论，会认为核心 contribution 是一个 well-executed replication study 而非 discovery。这直接影响 Conference vs Findings 的定位。\n- 建议修改方向：(1) 将 Introduction 的三个 LLM-specific distinctions 缩减为两个，删除 (c) binary split 或将其降级为\"与经典理论一致的验证\"；(2) 更清晰地将 contribution 定位为 \"systematic empirical demonstration + per-axis structure discovery + practical diagnostic tool\"，而非 \"new phenomenon\"；(3) 考虑在 Title/Abstract 中添加类似 \"extends classical measurement theory to LLM evaluation\" 的表述。\n\n**N2** [critical] Scaled replication 覆盖不足——仅一个 cell 有大样本验证\n\n- 具体位置：§5.1 para 2, Table 1\n- 问题：n=355 的 scaled replication 仅覆盖 Qwen3-32B × formality 这一个 cell。这是论文最关键的论点支柱——用大样本证明 Likert 的 d→0 是结构性的而非 power 不足。但其他 11 个 primary/confirmatory cells（GPT-4o × formality/verbosity, Llama-70B × formality/verbosity, Gemini × formality/verbosity 等）都只有 n=86–88，无法排除这些 cells 的 Blindspot 仅仅是 power 问题。\n- 为什么影响接收：论文声称 \"consistent pattern rather than an isolated anomaly\"（§1 Contribution 2），但只有一个 cell 用大样本验证了这不是 power artifact。这是一个可证伪但未被充分验证的 claim。尤其 Gemini formality（BT 仅 57.4%，效应最弱）如果做 scaled replication 可能不复现 d→0 的结论。\n- 建议修改方向：(1) 对至少一个 verbosity cell 做 scaled replication（因为 verbosity 是最强效应，但 Likert d 也接近零——这可以更干净地证明结构性衰减）；(2) 如果资源限制无法做更多 replication，应在 Limitations 明确承认这一 coverage gap，并将 \"consistent pattern\" 的 claim 弱化为 \"observed pattern, with structural attenuation confirmed for one judge×axis cell\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Title \"The Likert Blindspot\" 暗示单一因果方向，与正文 nuanced 讨论矛盾\n\n- 具体位置：Title, §5.1 \"Interpreting the divergence\"\n- 问题：\"Blindspot\" 一词暗示 Likert 有缺陷（漏检），预设了 attenuation 解释为主导。但 §5.1 明确提出三种非排他解释，包括 pairwise amplification（可能是 pairwise 过度放大而非 Likert 漏检）和 construct divergence（两种模式测量不同构念）。如果 amplification 是主因，那么 \"Blindspot\" 的描述就不准确——Likert 没有\"盲点\"，只是 pairwise 有\"放大镜\"。\n- 建议：(1) 在 §1 更早处对 \"Blindspot\" 进行操作化定义（论文在 §1 para 2 做了，但可以更突出）；(2) 考虑在 Abstract 中加入一句明确的 hedge：e.g., \"which we term the Likert Blindspot as an operational descriptor without committing to a specific causal mechanism\"（部分已在正文中，但 Abstract 缺少）。实际上我看到 Introduction 第二段有这个 hedge，但 Abstract 和 Title 没有传达。\n\n**W2** [warning] Qwen3-32B 同时担任 rewriter 和 target judge 的循环依赖\n\n- 具体位置：§3.1, §4.1, Appendix E\n- 问题：Qwen3-32B 既是风格改写器又是被测 judge。虽然 Appendix E 展示了独立 GPT-4o rewriter 的验证（BT 从 66.5% 降至约 57%，降幅 22%），但这个 22% 的降幅本身值得关注——它说明 evaluator-producer overlap 确实 inflate 了效应量。论文报告的 Qwen3-32B 结果可能系统性偏高。\n- 建议：(1) 在 §4.1 或 Table 1 脚注中标注 Qwen3-32B 的 evaluator-producer overlap caveat；(2) 如果可能，对 Qwen3-32B 的所有主要分析使用 GPT-4o rewriter 数据作为 robustness check；(3) 考虑 Table 1 中标注 Qwen3-32B 结果可能有 ~20% 的上行偏差。\n\n**W3** [warning] Register 轴结果弱且 exploratory，但在 Abstract/Contribution 中占有隐含地位\n\n- 具体位置：Abstract (\"two primary axes\"), Table 1 (register rows), §5.3\n- 问题：Register 轴在 Table 1 中有 3 行结果（GPT-4o, Qwen3, Llama-70B），但 BT 仅 .553–.635，效应远弱于 formality (.574–.695) 和 verbosity (.708–.773)。更关键的是，register 的 GEE 结构（Table 2）显示 Originality OR 远高于 Style OR（Qwen3: 5.72 vs 1.91），说明 register 效应可能主要由 quality confounding 驱动。论文标注为 \"exploratory\"，但在 cross-benchmark heatmap (Figure 6) 和 GEE table (Table 2) 中占了相当篇幅。\n- 建议：将 register 结果完全移至 Appendix，正文只保留一句 \"an exploratory register axis yielded weaker, quality-confounded effects (Appendix X)\"。这会释放正文空间给更重要的 scaled replication 或 cross-benchmark 讨论。\n\n**W4** [warning] \"Systematic pattern\" / \"consistent\" 等措辞与例外情况的张力\n\n- 具体位置：§1 Contribution 2, §6 Conclusion\n- 问题：Contribution 2 声称 \"revealing measurement-mode divergence as a consistent pattern rather than an isolated anomaly\"。但实际数据中：(1) Claude Sonnet 4 不显示一般性 Blindspot（Table 1, BT .541–.562, n.s.）；(2) Gemini formality 效应弱（BT 57.4%, Style OR 1.64 n.s.）；(3) cross-benchmark replication 仅 6/24 cells 达到显著。论文用 \"three exceptions (‡)\" 处理例外，但 \"consistent\" 一词在有 ~30% exception rate 的情况下值得审慎使用。\n- 建议：将 \"consistent pattern\" 改为 \"predominant pattern\" 或 \"majority pattern\"；在 §6 Conclusion 中量化复制率（e.g., \"8/11 primary+confirmatory cells, 6/24 cross-benchmark cells\"）。\n\n---\n\n## Minor 问题（不影响接收）\n\n**M1.** 术语一致性：\"style bias\" 和 \"style sensitivity\" 在论文中交替使用（e.g., Abstract 用 \"sensitivity\"，§5.1 标题用 \"Blindspot\" 暗示 \"bias\"）。建议统一——鉴于论文立场是 agnostic about mechanism，\"style sensitivity\" 更准确。\n\n**M2.** Figure 5 (GEE bar chart, p.8) 的 y 轴标签 \"Odds Ratio\" 在 log scale 上可能对不熟悉 GEE 的读者造成困惑。建议添加 \"log scale\" 标注或在 caption 中明确说明。\n\n**M3.** §3.2 提到 \"DeBERTa-v3-large fine-tuned on MNLI\" 作为 NLI gate，但未说明该模型在 out-of-domain（非 MNLI distribution）文本上的性能是否经过验证。human annotation（§5.4）部分验证了这一点，但 NLI model 本身的 domain-shift robustness 未被讨论。\n\n**M4.** Table 1 的 \"Cat.\" 列标记（†, †_e, †_c, ---）需要读者频繁查阅脚注。建议直接使用文字标签如 \"Blind\", \"Expl\", \"Conf\", \"Neither\"。\n\n**M5.** §5.2 引用 Nemes et al. 2009 解释小样本上行偏差。这个引用是 meta-analysis 领域的，应用到 GEE OR 的 small-sample bias 上是否完全对应，可以补充说明。\n\n---\n\n## Questions to Authors\n\n**Q1.** §5.1 的 non-tie concordance analysis（76.6%, p < .001）是论文区分 attenuation 和 construct divergence 的关键证据。但 76.6% 的 concordance 意味着 23.4% 的 discordance——这个 discordance rate 是否足够低以排除 partial construct divergence？论文承认 \"partial construct divergence remains at weaker effect sizes\"，那么具体在哪个效应量阈值以下 construct divergence 可能成为主导解释？\n\n**Q2.** 100-point continuous Likert scale（Appendix O）仍然显示 p > 0.15。这是一个重要的 robustness check。但 Appendix O 是否控制了 judges 使用 continuous scale 时的行为变化（e.g., 是否有 evidence 表明 judges 真的利用了 continuous scale 的 granularity，而不是仍然只使用少数离散值）？\n\n**Q3.** 论文使用 Qwen3-32B 作为 style classifier（§3.1）判断文本当前风格。如果 classifier 本身有系统性偏差（e.g., 倾向于将高质量文本分类为 formal），这是否会在 data generation 阶段引入 confounding？\n\n**Q4.** GEE 的 exchangeable working correlation 假设在 paired comparison data 中是否合理？论文提到 within-pair correlations 接近零（α̂ ∈ [−0.25, +0.11]），但 −0.25 的估计值似乎不算\"接近零\"。这是否影响 sandwich standard errors 的可靠性？\n\n---\n\n## Missing References\n\n论文的 Related Work 相当全面（~40 引用），但以下方向可以加强：\n\n1. **Item Response Theory (IRT) 在 NLG evaluation 中的应用**：论文简短引用了 Embretson & Reise (2000)，但 IRT 提供了更正式的框架来量化不同 measurement mode 的信息函数差异。近期有 IRT 用于 LLM evaluation 的工作（e.g., Polo et al., 2024, \"TinyBenchmarks\"），可以补充讨论 IRT 视角下 Likert vs pairwise 的 information gain 差异。\n\n2. **Likert scale anchoring effects**：不同 LLM judge 可能以不同方式解释 1-10 scale 的锚点（e.g., 有些 judge 倾向使用中间值，有些使用极端值），这是 Likert 信号衰减的已知机制之一（Krosnick 1999 已引用，但 scale anchoring 的具体讨论较少）。\n\n3. **Pairwise comparison 在 RLHF 中的 amplification 问题**：除了 Jeong et al. (2025) Comparative Trap，还有 Munos et al. (2023) \"Nash Learning from Human Feedback\" 等讨论 pairwise preference 中的 noise amplification。\n\n---\n\n## Scoring Summary\n\n| 维度 | 分数 |\n|------|------|\n| **Soundness** | 4 / 5 |\n| **Excitement** | 3 / 5 |\n| **Overall Assessment** | 3.5 / 5 (Borderline Conference) |\n| **Reproducibility** | 4 / 5 |\n| **Confidence** | 4 / 5 |\n\n**Overall Justification**: 论文在实验设计和统计分析方面达到了很高的标准，per-axis confound structure 是一个有价值的发现，CSD 作为实用诊断工具有明确的应用价值。将其拉向 3.5 而非 3.0 的主要因素是：(1) 实验规模和控制的thoroughness 在同类工作中突出；(2) GEE per-axis 分解提供了超越 Thurstone 经典框架的 genuinely new insight；(3) 实践相关性强（directly actionable for RLHF/DPO pipeline audits）。阻止其达到 4.0 的因素是：(1) 核心现象是经典测量理论的 domain transfer，novelty ceiling 有限；(2) scaled replication 仅覆盖 1/12 cells；(3) \"consistent pattern\" 的 claim 与 ~30% exception rate 有张力。\n",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1289 · 2026-05-23T14:28:43.316756+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3564
}
```

</details>

---


### Tool call

_source line 1290 · 2026-05-23T14:28:46.235142+00:00_

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

_source line 1291 · 2026-05-23T14:28:46.286429+00:00_



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

_source line 1292 · 2026-05-23T14:28:50.655150+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images"
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
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_16/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1293 · 2026-05-23T14:28:50.705767+00:00_

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

_source line 1294 · 2026-05-23T14:29:09.141442+00:00_

审稿意见已提交给 Review Director。

**核心判断**：Overall 3.5（Borderline Conference）。实验执行和统计严谨性达到高标准，GEE per-axis confound structure（verbosity style-dominated vs formality quality-confounded）是genuinely novel的发现。但核心现象——pairwise 比 Likert 更敏感——本质上是 Thurstone 1927 的 domain transfer，novelty ceiling 有限。

**两个 Must-Fix**：
1. 新颖性定位需要更精确——Introduction 的三个"LLM-specific distinctions"中第(c)个(binary split)被论文自己承认与经典理论一致，不构成独立贡献
2. Scaled replication（n=355）仅覆盖 Qwen3-32B × formality 一个 cell，其他 11 个 cell 无法排除纯 power 问题

**四个 Should-Fix**：Title 暗示单一因果方向与正文矛盾；Qwen3-32B rewriter-judge overlap（~20% inflation）；Register 轴结果弱应移至 Appendix；"consistent pattern" 与 ~30% exception rate 的张力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 38

## Round 38

4 recorded events


### User

_source line 1295 · 2026-05-23T14:31:28.117170+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和关键问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 完整审稿意见

**Overall**: 3.5 / 5（Borderline Conference）

### Must-Fix

**N1** [critical] GEE 小样本膨胀严重，仅一个配置在 n=355 复制
- Qwen3-32B formality Style OR 从 n=88 的 4.20 降至 n=355 的 2.15，shrinkage 达 49%。但只对 9 个 judge×axis 配置中的 1 个做了 n=355 复制。GPT-4o formality Style OR 在 n=88 时为 2.58 [1.41, 4.73]——如果经历类似 49% shrinkage，将降至 ~1.32，CI 将跨越 1.0（即不显著）。论文对 verbosity 的推断是外推，未经实证验证。

**N2** [critical] 跨 benchmark 复制为确认偏差式选择（6/24 cells）
- 仅测试 24 个可能的 benchmark×judge 配置中的 6 个，且明确选择标准为「targeting the strongest effects」。3 个例外（‡ 行）被 post-hoc 解释为 effect-size dependence，未被前瞻性验证。

### Should-Fix

**W1** [warning] Likert Blindspot 缺少正式的 divergence 检验
- 论文分别展示「BT 显著」和「Likert 不显著」，但从未正式检验二者是否显著不同。Absence of evidence ≠ evidence of absence。

**W2** [warning] Qwen3-32B 的 evaluator-producer overlap
- 独立 rewriter 测试显示 verbosity Style OR 下降 22%（13.10 → 10.17）。22% 不是小数目。且 n=355 唯一复制恰好选用了有 overlap 的 Qwen3-32B。

**W3** [warning] Claude Sonnet 4 负对照不充分
- TOST 等价性仅在 Δ=12pp 时显著（p=.035），在 Δ=10pp 时不显著。贝叶斯因子 BF₀ < 3（inconclusive）。等价边界的选择缺乏独立于数据的先验理由。

**W4** [warning] FK grade 的 mediator vs. confounder 辨识不足
- Sobel 中介检验建立的是统计中介，不是因果中介。替代因果结构在统计上不可区分。

**W5** [warning] GEE 模型潜在的遗漏变量偏差
- GEE 仅含两个预测变量。建议报告 E-value 或 Rosenbaum bounds。

### Questions
1. n=355 复制是否使用相同 NLI gating threshold？
2. 各 judge 的 Likert 评分分布是什么？
3. 「76-92% of preferences originate from style cues」如何计算？
4. 为什么 n=355 复制只选了 Qwen3-32B formality？

### Missing References
- Likert (1932) 原始文献
- Schwarz (1999) Self-reports
- Johnson & Goldstein (2003) defaults in choice architecture

---

请逐条回应每个 Must-Fix 和 Should-Fix。

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

_source line 1296 · 2026-05-23T14:33:29.669243+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 回应\n\n### R1-N1: GEE 小样本膨胀严重，仅一个配置在 n=355 复制\n\n**[AGREE]** 同意这是论文的主要弱点之一，与我的 N2 指出的问题高度重叠。\n\n补充论证：\n- R1 的推算有说服力——GPT-4o formality Style OR 2.58 经历 49% shrinkage 后约为 1.32，CI 确实可能跨 1.0。这会从根本上动摇 GPT-4o formality 的 \"conditional style effect\" 结论。\n- 但需要区分两个 claim 的受影响程度不同：(1) **Blindspot 的存在性**（BT 显著 vs Likert 不显著）不依赖 GEE OR 的绝对值——BT win probability（Table 1）是非参数的，不受小样本 OR 膨胀影响；(2) **GEE per-axis confound structure** 的定量描述确实受影响。因此 N1 主要威胁的是 GEE 相关结论，而非 Blindspot 核心发现本身。\n- 论文在 §5.2 最后一段对 verbosity 的外推论证（\"even under ~50% shrinkage, projected 4–6.5, still ≫ Orig OR < 1\"）逻辑上成立但未经实证验证，R1 指出这一点是正确的。\n\n**结论**：应要求至少对一个 verbosity cell 做 scaled replication，或将 verbosity 的 GEE 定量结论明确标注为 \"projected, pending large-sample validation\"。\n\n---\n\n### R1-N2: 跨 benchmark 复制为确认偏差式选择（6/24 cells）\n\n**[AGREE]** 部分同意，但严重性判断略有不同。\n\n- R1 的批评——选择 \"targeting the strongest effects\" 构成确认偏差——在方法论上是正确的。如果只测试预期最强的 cells，6/24 的显著率无法代表 generalizability。\n- 但论文将 cross-benchmark 分析定位为 **exploratory**（§4.1 \"Gemini-2.5-Flash serves as confirmatory replication and is excluded from FWER control\"；Figure 6 caption 中 \"Grey ×: not tested\"），并未将其作为核心 contribution。论文的主要 claims 建立在 LLMBar 上，cross-benchmark 是补充证据。\n- 真正的问题是 §1 Contribution 2 的措辞——\"the first at this scale\"——暗示了比实际完成的更全面的 cross-benchmark 覆盖。如果改为 \"with selective cross-benchmark evidence\"，批评力度会大幅降低。\n- 3 个 ‡ exceptions 的 post-hoc \"severity spectrum\" 解释（§5.1 最后一段）确实缺乏 pre-registration，R1 的批评成立。\n\n**结论**：应将 Contribution 2 的措辞弱化，明确 cross-benchmark 的 exploratory 性质和选择标准。但这不应作为 Must-Fix，因为论文的主要 claims 不依赖于 cross-benchmark generalization。建议降级为 Should-Fix。\n\n---\n\n## Should-Fix 回应\n\n### R1-W1: Likert Blindspot 缺少正式的 divergence 检验\n\n**[AGREE]** 这是一个好的统计学观点，我的审稿遗漏了这一点。\n\n- R1 准确识别了一个逻辑缺口：论文分别展示 \"BT 显著\" 和 \"Likert 不显著\"，但从未检验两个 effect size 是否 statistically significantly different。\"Absence of evidence is not evidence of absence\" 在此完全适用。\n- 论文用 n=355 的 TOST equivalence testing（Appendix H, Δ=12pp 时 p=.035）和 bootstrap attenuation analysis（Appendix K, d 不随 n 增长而偏离零）间接回应了这一点，但正式的 measurement-mode interaction test（e.g., 将 measurement mode 作为 within-subject factor 的 mixed-effects model）确实缺失。\n- 这是可以在 revision 中补充的分析，且可能加强论文的论点。\n\n**结论**：同意应补充正式的 divergence 检验。一种方法是 bootstrap the difference in effect sizes between BT and Likert，检验该差异是否显著异于零。\n\n---\n\n### R1-W2: Qwen3-32B 的 evaluator-producer overlap\n\n**[AGREE]** 与我的 W2 一致。\n\n- 补充 R1 的论点：n=355 复制恰好选择了有 overlap 的 Qwen3-32B 这一点尤其值得警惕。如果 n=355 复制使用无 overlap 的 GPT-4o 作为 target judge（GPT-4o rewriter → GPT-4o judge 也有 overlap，但 Qwen3 rewriter → GPT-4o judge 无 overlap），结论会更 clean。\n- Appendix E 的独立 rewriter 验证（Table 6）显示 Blindspot 仍然存在（GPT-4o rewriter: Style OR = 10.17, p = 0.001; Blindspot: Yes），所以 overlap 影响的是效应量级而非现象存在性。\n\n**结论**：同意应更突出标注 overlap caveat，并建议至少一个 scaled replication 使用非 overlap 配置。\n\n---\n\n### R1-W3: Claude Sonnet 4 负对照不充分\n\n**[AGREE]** R1 的批评在技术上准确。\n\n- TOST 在 Δ=12pp 才显著（p=.035），在 Δ=10pp 时不显著——这意味着我们只能排除 ≥12pp 的效应，而 12pp 对于 BT win probability 来说是一个相当宽松的等价边界（对应约 .62 的 BT，接近某些弱 Blindspot cells 的效应量）。\n- BF₀ < 3 确实是 inconclusive by conventional Bayesian standards（Jeffreys scale 要求 BF > 3 为 moderate evidence）。\n- 等价边界 Δ=12pp 的选择在 Appendix H 中描述为 \"the smallest margin at which pooled significance is achieved\"——这是 data-driven 而非 a priori，R1 指出 \"缺乏独立于数据的先验理由\" 是正确的。\n- 但 Claude 的价值不完全取决于 equivalence testing。论文更多用 Claude 的 benchmark-dependent profile（LLMBar n.s., AEval verbosity OR = 4.76 significant）作为 discriminative validity 证据（§5.3），说明 CSD 不是 universal false positive machine。这个论证不依赖 TOST。\n\n**结论**：同意 TOST 分析的 boundary justification 不足，建议弱化 Claude 作为 \"negative control\" 的 claim，转而强调其 \"discriminative validity\" 角色——CSD 在不同 judges 上给出不同结论，这本身就说明框架不是 universal false positive。\n\n---\n\n### R1-W4: FK grade 的 mediator vs. confounder 辨识不足\n\n**[AGREE]** R1 的因果推理论点是正确的。\n\n- 论文在 §5.3 声称 \"FK lies on the causal pathway S → FK → Y: the intervention directly alters readability, making FK a mediator rather than a confounder\"。这个因果方向 claim 是 reasonable but not testable with observational data alone。\n- 替代因果结构确实存在：如果存在一个未观测的共因（e.g., text complexity）同时影响 FK grade 和 judge score，那么 FK 是 collider 而非 mediator，conditioning on it 会引入 collider bias。\n- 但从 domain knowledge 看，S → FK 的方向是 plausible 的——formality 的 rewriting 确实会改变 readability（formal text 倾向使用更复杂的句式）。这是 a priori reasonable 的因果方向，但论文应更清楚地标注这是 an assumed causal model。\n\n**结论**：同意应将 mediator claim 降级为 \"plausible under the assumed causal model\" 而非 definitive。\n\n---\n\n### R1-W5: GEE 模型潜在的遗漏变量偏差\n\n**[REBUT]** 部分反驳。\n\n- R1 建议报告 E-value 或 Rosenbaum bounds。这对于声称因果效应的观察性研究是标准做法，但论文在 Appendix A（Design Rationale）中明确声明 \"Our approach provides interventional rather than formal causal evidence\"，且 Limitations 第一条直接承认 residual confounding。\n- GEE 在论文中的角色是 **descriptive decomposition**（将 BT 效应分解为 style 和 originality 成分），而非因果推断工具。论文使用 \"conditional\" 而非 \"causal\"。在这个定位下，omitted variable bias 确实存在但不威胁论文的核心 claim——论文没有声称 GEE 给出因果效应。\n- 但 R1 的建议仍有价值：报告 E-value 不需要声称因果关系，它量化的是 \"需要多强的未观测混淆才能解释掉观测到的 association\"。对于 verbosity 的 Style OR = 8–13，E-value 会非常高（说明 extremely strong confounding 才能消除效应），这实际上会加强论文的论证。\n\n**结论**：论文定位 GEE 为 descriptive 而非 causal，omitted variable 批评的杀伤力有限。但同意报告 E-value 是一个 costless improvement，建议在 revision 中添加。\n\n---\n\n## Questions 回应\n\n### Q1: n=355 复制是否使用相同 NLI gating threshold？\n\n我在论文中未找到明确说明。§3.2 设定 threshold = 0.90，§4.2 提到 n=355 是 \"4× scaled replication\"——合理推测使用相同 threshold，但 R1 要求明确声明是正确的。Appendix F 的 NLI threshold sensitivity sweep 仅在 n=88 上做，未提及 n=355。\n\n### Q2: 各 judge 的 Likert 评分分布是什么？\n\n这是一个好的要求。论文在 §5.1 提到 \"Likert tie rates of 58–73%\"，但没有展示完整分布（e.g., histogram）。这些分布对于理解 tie inflation 机制至关重要——是 judges 倾向使用中间值（central tendency bias），还是整体集中在高分区（ceiling effect）？\n\n### Q3: 「76-92% of preferences originate from style cues」如何计算？\n\n这不是论文自己的计算，而是引用 li2026preference 和 soumik2026judging 的结论（§1 para 1）。但 R1 的问题合理——引用他人的 claim 时应注意该 claim 的 operationalization 是否与本文一致。\n\n### Q4: 为什么 n=355 复制只选了 Qwen3-32B formality？\n\n论文未解释选择理由。可能的原因：(1) Qwen3-32B 也是 rewriter，数据生成成本最低；(2) formality 是两个 primary axis 之一。但 R1 隐含的批评是正确的——这个选择引入了 evaluator-producer overlap，不是最 clean 的验证。\n\n---\n\n## Missing References 回应\n\n### Likert (1932)\n**[AGREE]** 引用 Likert 原始文献是合理的建议。论文大量讨论 Likert scale 的局限性，却未引用其原始提出者。虽然 Stevens (1946) 已被引用，但 Likert (1932) 作为 construct 的 origin 值得加入。\n\n### Schwarz (1999) Self-reports\n**[REBUT]** 边际相关。Schwarz 的 self-report 认知模型主要针对人类被试的 survey response，LLM judge 的 \"self-report\" 机制不同（不涉及 memory retrieval 或 social desirability）。可以在 Related Work 一句话提及，但非必须。\n\n### Johnson & Goldstein (2003) defaults in choice architecture\n**[REBUT]** 与论文主题距离较远。论文关注的是 measurement mode（Likert vs pairwise）的敏感性差异，不涉及 default option framing。Choice architecture 文献的相关性有限。\n\n---\n\n## 综合评估\n\nReviewer 1 的审稿意见整体质量很高，统计学功底扎实。两个 Must-Fix 中：\n- **N1（GEE 小样本膨胀）**：完全同意，但需要区分对 GEE 定量结论 vs Blindspot 存在性的影响\n- **N2（cross-benchmark 选择偏差）**：同意 concern，但建议降级为 Should-Fix（论文主 claims 不依赖 cross-benchmark）\n\n五个 Should-Fix 中，W1（缺少 formal divergence test）和 W3（Claude TOST boundary）是我审稿时遗漏的好观点。W5（GEE omitted variables）我部分反驳——论文定位 GEE 为 descriptive，omitted variable 批评的前提不完全成立，但报告 E-value 是低成本改进。\n\nR1 和我的 Overall 评分一致（3.5, Borderline Conference），且核心关切高度重叠：**scaled replication 覆盖不足**是两位 reviewer 共同识别的最大问题。\n",
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
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 回应\n\n### R1-N1: GEE 小样本膨胀严重，仅一个配置在 n=355 复制\n\n**[AGREE]** 同意这是论文的主要弱点之一，与我的 N2 指出的问题高度重叠。\n\n补充论证：\n- R1 的推算有说服力——GPT-4o formality Style OR 2.58 经历 49% shrinkage 后约为 1.32，CI 确实可能跨 1.0。这会从根本上动摇 GPT-4o formality 的 \"conditional style effect\" 结论。\n- 但需要区分两个 claim 的受影响程度不同：(1) **Blindspot 的存在性**（BT 显著 vs Likert 不显著）不依赖 GEE OR 的绝对值——BT win probability（Table 1）是非参数的，不受小样本 OR 膨胀影响；(2) **GEE per-axis confound structure** 的定量描述确实受影响。因此 N1 主要威胁的是 GEE 相关结论，而非 Blindspot 核心发现本身。\n- 论文在 §5.2 最后一段对 verbosity 的外推论证（\"even under ~50% shrinkage, projected 4–6.5, still ≫ Orig OR < 1\"）逻辑上成立但未经实证验证，R1 指出这一点是正确的。\n\n**结论**：应要求至少对一个 verbosity cell 做 scaled replication，或将 verbosity 的 GEE 定量结论明确标注为 \"projected, pending large-sample validation\"。\n\n---\n\n### R1-N2: 跨 benchmark 复制为确认偏差式选择（6/24 cells）\n\n**[AGREE]** 部分同意，但严重性判断略有不同。\n\n- R1 的批评——选择 \"targeting the strongest effects\" 构成确认偏差——在方法论上是正确的。如果只测试预期最强的 cells，6/24 的显著率无法代表 generalizability。\n- 但论文将 cross-benchmark 分析定位为 **exploratory**（§4.1 \"Gemini-2.5-Flash serves as confirmatory replication and is excluded from FWER control\"；Figure 6 caption 中 \"Grey ×: not tested\"），并未将其作为核心 contribution。论文的主要 claims 建立在 LLMBar 上，cross-benchmark 是补充证据。\n- 真正的问题是 §1 Contribution 2 的措辞——\"the first at this scale\"——暗示了比实际完成的更全面的 cross-benchmark 覆盖。如果改为 \"with selective cross-benchmark evidence\"，批评力度会大幅降低。\n- 3 个 ‡ exceptions 的 post-hoc \"severity spectrum\" 解释（§5.1 最后一段）确实缺乏 pre-registration，R1 的批评成立。\n\n**结论**：应将 Contribution 2 的措辞弱化，明确 cross-benchmark 的 exploratory 性质和选择标准。但这不应作为 Must-Fix，因为论文的主要 claims 不依赖于 cross-benchmark generalization。建议降级为 Should-Fix。\n\n---\n\n## Should-Fix 回应\n\n### R1-W1: Likert Blindspot 缺少正式的 divergence 检验\n\n**[AGREE]** 这是一个好的统计学观点，我的审稿遗漏了这一点。\n\n- R1 准确识别了一个逻辑缺口：论文分别展示 \"BT 显著\" 和 \"Likert 不显著\"，但从未检验两个 effect size 是否 statistically significantly different。\"Absence of evidence is not evidence of absence\" 在此完全适用。\n- 论文用 n=355 的 TOST equivalence testing（Appendix H, Δ=12pp 时 p=.035）和 bootstrap attenuation analysis（Appendix K, d 不随 n 增长而偏离零）间接回应了这一点，但正式的 measurement-mode interaction test（e.g., 将 measurement mode 作为 within-subject factor 的 mixed-effects model）确实缺失。\n- 这是可以在 revision 中补充的分析，且可能加强论文的论点。\n\n**结论**：同意应补充正式的 divergence 检验。一种方法是 bootstrap the difference in effect sizes between BT and Likert，检验该差异是否显著异于零。\n\n---\n\n### R1-W2: Qwen3-32B 的 evaluator-producer overlap\n\n**[AGREE]** 与我的 W2 一致。\n\n- 补充 R1 的论点：n=355 复制恰好选择了有 overlap 的 Qwen3-32B 这一点尤其值得警惕。如果 n=355 复制使用无 overlap 的 GPT-4o 作为 target judge（GPT-4o rewriter → GPT-4o judge 也有 overlap，但 Qwen3 rewriter → GPT-4o judge 无 overlap），结论会更 clean。\n- Appendix E 的独立 rewriter 验证（Table 6）显示 Blindspot 仍然存在（GPT-4o rewriter: Style OR = 10.17, p = 0.001; Blindspot: Yes），所以 overlap 影响的是效应量级而非现象存在性。\n\n**结论**：同意应更突出标注 overlap caveat，并建议至少一个 scaled replication 使用非 overlap 配置。\n\n---\n\n### R1-W3: Claude Sonnet 4 负对照不充分\n\n**[AGREE]** R1 的批评在技术上准确。\n\n- TOST 在 Δ=12pp 才显著（p=.035），在 Δ=10pp 时不显著——这意味着我们只能排除 ≥12pp 的效应，而 12pp 对于 BT win probability 来说是一个相当宽松的等价边界（对应约 .62 的 BT，接近某些弱 Blindspot cells 的效应量）。\n- BF₀ < 3 确实是 inconclusive by conventional Bayesian standards（Jeffreys scale 要求 BF > 3 为 moderate evidence）。\n- 等价边界 Δ=12pp 的选择在 Appendix H 中描述为 \"the smallest margin at which pooled significance is achieved\"——这是 data-driven 而非 a priori，R1 指出 \"缺乏独立于数据的先验理由\" 是正确的。\n- 但 Claude 的价值不完全取决于 equivalence testing。论文更多用 Claude 的 benchmark-dependent profile（LLMBar n.s., AEval verbosity OR = 4.76 significant）作为 discriminative validity 证据（§5.3），说明 CSD 不是 universal false positive machine。这个论证不依赖 TOST。\n\n**结论**：同意 TOST 分析的 boundary justification 不足，建议弱化 Claude 作为 \"negative control\" 的 claim，转而强调其 \"discriminative validity\" 角色——CSD 在不同 judges 上给出不同结论，这本身就说明框架不是 universal false positive。\n\n---\n\n### R1-W4: FK grade 的 mediator vs. confounder 辨识不足\n\n**[AGREE]** R1 的因果推理论点是正确的。\n\n- 论文在 §5.3 声称 \"FK lies on the causal pathway S → FK → Y: the intervention directly alters readability, making FK a mediator rather than a confounder\"。这个因果方向 claim 是 reasonable but not testable with observational data alone。\n- 替代因果结构确实存在：如果存在一个未观测的共因（e.g., text complexity）同时影响 FK grade 和 judge score，那么 FK 是 collider 而非 mediator，conditioning on it 会引入 collider bias。\n- 但从 domain knowledge 看，S → FK 的方向是 plausible 的——formality 的 rewriting 确实会改变 readability（formal text 倾向使用更复杂的句式）。这是 a priori reasonable 的因果方向，但论文应更清楚地标注这是 an assumed causal model。\n\n**结论**：同意应将 mediator claim 降级为 \"plausible under the assumed causal model\" 而非 definitive。\n\n---\n\n### R1-W5: GEE 模型潜在的遗漏变量偏差\n\n**[REBUT]** 部分反驳。\n\n- R1 建议报告 E-value 或 Rosenbaum bounds。这对于声称因果效应的观察性研究是标准做法，但论文在 Appendix A（Design Rationale）中明确声明 \"Our approach provides interventional rather than formal causal evidence\"，且 Limitations 第一条直接承认 residual confounding。\n- GEE 在论文中的角色是 **descriptive decomposition**（将 BT 效应分解为 style 和 originality 成分），而非因果推断工具。论文使用 \"conditional\" 而非 \"causal\"。在这个定位下，omitted variable bias 确实存在但不威胁论文的核心 claim——论文没有声称 GEE 给出因果效应。\n- 但 R1 的建议仍有价值：报告 E-value 不需要声称因果关系，它量化的是 \"需要多强的未观测混淆才能解释掉观测到的 association\"。对于 verbosity 的 Style OR = 8–13，E-value 会非常高（说明 extremely strong confounding 才能消除效应），这实际上会加强论文的论证。\n\n**结论**：论文定位 GEE 为 descriptive 而非 causal，omitted variable 批评的杀伤力有限。但同意报告 E-value 是一个 costless improvement，建议在 revision 中添加。\n\n---\n\n## Questions 回应\n\n### Q1: n=355 复制是否使用相同 NLI gating threshold？\n\n我在论文中未找到明确说明。§3.2 设定 threshold = 0.90，§4.2 提到 n=355 是 \"4× scaled replication\"——合理推测使用相同 threshold，但 R1 要求明确声明是正确的。Appendix F 的 NLI threshold sensitivity sweep 仅在 n=88 上做，未提及 n=355。\n\n### Q2: 各 judge 的 Likert 评分分布是什么？\n\n这是一个好的要求。论文在 §5.1 提到 \"Likert tie rates of 58–73%\"，但没有展示完整分布（e.g., histogram）。这些分布对于理解 tie inflation 机制至关重要——是 judges 倾向使用中间值（central tendency bias），还是整体集中在高分区（ceiling effect）？\n\n### Q3: 「76-92% of preferences originate from style cues」如何计算？\n\n这不是论文自己的计算，而是引用 li2026preference 和 soumik2026judging 的结论（§1 para 1）。但 R1 的问题合理——引用他人的 claim 时应注意该 claim 的 operationalization 是否与本文一致。\n\n### Q4: 为什么 n=355 复制只选了 Qwen3-32B formality？\n\n论文未解释选择理由。可能的原因：(1) Qwen3-32B 也是 rewriter，数据生成成本最低；(2) formality 是两个 primary axis 之一。但 R1 隐含的批评是正确的——这个选择引入了 evaluator-producer overlap，不是最 clean 的验证。\n\n---\n\n## Missing References 回应\n\n### Likert (1932)\n**[AGREE]** 引用 Likert 原始文献是合理的建议。论文大量讨论 Likert scale 的局限性，却未引用其原始提出者。虽然 Stevens (1946) 已被引用，但 Likert (1932) 作为 construct 的 origin 值得加入。\n\n### Schwarz (1999) Self-reports\n**[REBUT]** 边际相关。Schwarz 的 self-report 认知模型主要针对人类被试的 survey response，LLM judge 的 \"self-report\" 机制不同（不涉及 memory retrieval 或 social desirability）。可以在 Related Work 一句话提及，但非必须。\n\n### Johnson & Goldstein (2003) defaults in choice architecture\n**[REBUT]** 与论文主题距离较远。论文关注的是 measurement mode（Likert vs pairwise）的敏感性差异，不涉及 default option framing。Choice architecture 文献的相关性有限。\n\n---\n\n## 综合评估\n\nReviewer 1 的审稿意见整体质量很高，统计学功底扎实。两个 Must-Fix 中：\n- **N1（GEE 小样本膨胀）**：完全同意，但需要区分对 GEE 定量结论 vs Blindspot 存在性的影响\n- **N2（cross-benchmark 选择偏差）**：同意 concern，但建议降级为 Should-Fix（论文主 claims 不依赖 cross-benchmark）\n\n五个 Should-Fix 中，W1（缺少 formal divergence test）和 W3（Claude TOST boundary）是我审稿时遗漏的好观点。W5（GEE omitted variables）我部分反驳——论文定位 GEE 为 descriptive，omitted variable 批评的前提不完全成立，但报告 E-value 是低成本改进。\n\nR1 和我的 Overall 评分一致（3.5, Borderline Conference），且核心关切高度重叠：**scaled replication 覆盖不足**是两位 reviewer 共同识别的最大问题。\n",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1297 · 2026-05-23T14:33:35.390439+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5721
}
```

</details>

---


### Assistant

_source line 1298 · 2026-05-23T14:33:41.055501+00:00_

已完成对 Reviewer 1 审稿意见的逐条回应，汇报给 Director。

核心判断：
- **N1（GEE 小样本膨胀）**：完全同意，但区分了对 GEE 定量结论 vs Blindspot 存在性的不同影响
- **N2（cross-benchmark 选择偏差）**：同意 concern，建议降级为 Should-Fix
- **W1（缺 formal divergence test）**：同意，这是我遗漏的好观点
- **W3（Claude TOST）**、**W4（FK mediator）**：同意
- **W5（GEE omitted variables）**：部分反驳——论文定位 GEE 为 descriptive 而非 causal，但同意报告 E-value 是低成本改进

两位 Reviewer 的共识：**scaled replication 覆盖不足**是最大问题，Overall 评分一致（3.5, Borderline Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 39

## Round 39

80 recorded events


### User

_source line 1299 · 2026-05-25T21:18:41.557468+00:00_

[Round 1 审稿请求]:
## 审稿任务 — Round 1

**论文**: "The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation"
**目标 Venue**: EMNLP 2026 (Main Conference, Long Paper, via ARR)
**ARR Submission Deadline**: May 25, 2026
**Commitment Deadline**: August 2, 2026
**格式要求**: 8 页正文 + 无限参考文献，Limitations 必须放在正文中（不计入 8 页），double-blind，ACL 模板
**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/submitted.pdf` (20 pages, A4)
**LaTeX 源码**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`（各章节在 `sections/` 子目录）

### 你的审查侧重：新颖性/完整性

请重点审查以下方面：

1. **Novelty 评估**
   - "Likert Blindspot" 作为主要贡献是否具有足够的新颖性？Thurstone (1927) 以来 pairwise vs rating 的差异是心理测量学已知现象，本文在 LLM judge 领域的 domain transfer 是否构成足够的 novelty？
   - CSD 方法论相比 RATE (Reber et al., 2025) 的增量贡献是什么？差异化论证是否清晰有力？
   - GEE per-axis decomposition 作为贡献是否被充分强调？是否是本文真正的方法论亮点？
   - 三个 claimed contributions 的措辞是否精确？是否过度 claim？

2. **叙事逻辑与 Framing**
   - Title "The Likert Blindspot" 是否预设了 Likert attenuation 解释，与正文三种非排他解释（attenuation, amplification, construct divergence）存在张力？
   - Abstract 是否在 200 words 以内？是否准确反映了论文的贡献和限制？
   - Introduction 的 motivating example（"What is the average height for a male?"）是否具有代表性和说服力？
   - "consistent pattern" / "systematic" 等措辞是否与实际数据一致（考虑 Claude 的 null results 和 ~30% exception rate）？

3. **Related Work**
   - 对 RATE, CASSE, FairJudge, Comparative Trap 等关键工作的定位是否准确？
   - 是否遗漏了重要的相关工作？特别是 2025-2026 年的最新进展
   - LLM judge bias 文献覆盖是否全面？
   - 经典心理测量文献的引用是否恰当？

4. **写作质量**
   - 正文 8 页的信息密度和可读性？
   - Table 1 的设计——15 行 + 复杂脚注是否易于解读？
   - 图表（pipeline, DAG, forest plot, power curve, heatmap, GEE decomposition）是否清晰有效？
   - Appendix 组织是否合理？23 个 section 是否过于冗长？
   - Limitations section 是否恰当？（EMNLP 2026 要求放在正文中，不计入页数）

5. **完整性**
   - 仅两个主轴（formality, verbosity）+ 一个 exploratory（register），scope 是否足以支撑 claim？
   - 4 target judges + 1 discriminative validity，是否覆盖了主流 LLM judges？
   - Cross-benchmark replication 策略（选择最强 effects 的 6/24 cells）是否合理？
   - Anonymous code/data link 是否有效？

请按 EMNLP 2026 ARR 的标准出具审稿意见，结构如下：
- **Summary** (2-3 句)
- **Strengths** (逐条)
- **Weaknesses** (逐条，分 Must-Fix / Should-Fix / Minor)
- **Questions** (需要作者澄清的)
- **Missing References** (如有)
- **Excitement**: 1-5
- **Overall Assessment**: 使用 ARR 评分标准 (1-5)
- **Confidence**: 1-5

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

_source line 1300 · 2026-05-25T21:18:54.091680+00:00_

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

_source line 1301 · 2026-05-25T21:18:54.092176+00:00_



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

_source line 1302 · 2026-05-25T21:18:58.709483+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/submitted.pdf",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1303 · 2026-05-25T21:18:59.261773+00:00_

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


### Tool result

_source line 1304 · 2026-05-25T21:19:00.366859+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 549.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 714.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 602.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 528.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 475.6}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 490.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p9.p
…[truncated 526 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1657
}
```

</details>

---


### Tool result

_source line 1305 · 2026-05-25T21:19:08.193835+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here are the key ACL ARR 2025-2026 reviewer guidelines:

## Review Form Criteria and Scoring

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

**Soundness Score:**
The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

**Excitement Score:**
You may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Metareview Scoring

The ARR metareview score has changed in February 2025 to be more aligned with reviewer scores. Like with reviews, the score should be backed up by the meta-review text. The new options include: 5 = Consider for Award (for
…[truncated 466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8932
}
```

</details>

---


### Tool call

_source line 1306 · 2026-05-25T21:19:12.871450+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring scales (soundness, excitement, overall assessment), and detailed guidelines for each dimension. Include the specific numeric scales and what each number means."
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
    "prompt": "Extract the complete review form criteria, scoring scales (soundness, excitement, overall assessment), and detailed guidelines for each dimension. Include the specific numeric scales and what each number means."
  }
}
```

</details>

---


### Tool call

_source line 1307 · 2026-05-25T21:19:13.324158+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p1.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1308 · 2026-05-25T21:19:13.778175+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p2.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1309 · 2026-05-25T21:19:14.432895+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1108
}
```

</details>

---


### Tool call

_source line 1310 · 2026-05-25T21:19:14.433365+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p3.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1311 · 2026-05-25T21:19:14.484652+00:00_



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

_source line 1312 · 2026-05-25T21:19:15.038219+00:00_



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


### Tool result

_source line 1313 · 2026-05-25T21:19:18.551609+00:00_

# ARR Review Form Criteria and Scoring Scales

Based on the guidelines provided, ARR implements a **three-score review system** as of February 2025:

## The Three Scoring Dimensions

### 1. **Soundness**
This evaluates technical quality and methodological rigor. The guidelines emphasize that "soundness scores must be justified by the text of the review." Low soundness ratings require explicit evidence of flaws; vague criticism without concrete problems indicates the assessment lacks faithful representation of your reasoning.

### 2. **Excitement**
This captures subjective interest and personal engagement with the work. The document notes this score is "orthogonal to the assessment of the soundness of the paper," allowing reviewers to distinguish between technically solid work they find uninteresting versus flawed work they find compelling.

### 3. **Overall Assessment**
Described as "an explicit recommendation for the outcome of this paper," this composite score reflects soundness, excitement, novelty, and potential impact. The guidelines clarify that papers can merit main conference acceptance even if reviewers lack personal enthusiasm, particularly for high-impact contributions like resource creation or algorithmic efficiency improvements.

## Specific Numeric Scales

The document does not explicitly detail the numeric scale values (e.g., 1-5, 1-10) for each dimension. However, it references a detailed description available separately at the "review form" post on the ARR website.

## Key Evaluation Principles

Reviewers must ensure scores align with written justification and avoid common biases listed in the "Heuristic" section (H1-H17).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5680
}
```

</details>

---


### Tool call

_source line 1314 · 2026-05-25T21:19:24.923483+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p4.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1315 · 2026-05-25T21:19:25.325234+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p5.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1316 · 2026-05-25T21:19:26.281552+00:00_



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


### Tool call

_source line 1317 · 2026-05-25T21:19:26.282018+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p6.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1318 · 2026-05-25T21:19:26.838813+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1513
}
```

</details>

---


### Tool call

_source line 1319 · 2026-05-25T21:19:26.839268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p7.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1320 · 2026-05-25T21:19:27.291797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p8.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1321 · 2026-05-25T21:19:27.544677+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1262
}
```

</details>

---


### Tool result

_source line 1322 · 2026-05-25T21:19:29.208521+00:00_



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

_source line 1323 · 2026-05-25T21:19:29.410858+00:00_



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

_source line 1324 · 2026-05-25T21:19:35.986049+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p9.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1325 · 2026-05-25T21:19:36.839962+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1326 · 2026-05-25T21:19:36.940742+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p10.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1327 · 2026-05-25T21:19:37.796948+00:00_



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

_source line 1328 · 2026-05-25T21:19:38.301449+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/submitted.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "11-20",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/submitted.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1329 · 2026-05-25T21:19:40.165565+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.3}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 441.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 457.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 439.6}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.3}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.8}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.3}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.8}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_imag
…[truncated 544 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1864
}
```

</details>

---


### Tool call

_source line 1330 · 2026-05-25T21:19:40.166005+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form with all scoring dimensions, their numeric scales, and what each score level means. Include soundness, excitement, overall assessment, confidence scales."
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
    "prompt": "Extract the complete ARR review form with all scoring dimensions, their numeric scales, and what each score level means. Include soundness, excitement, overall assessment, confidence scales."
  }
}
```

</details>

---


### Tool result

_source line 1331 · 2026-05-25T21:19:45.383746+00:00_

# ARR Review Form Scoring Dimensions

## Reviewer Confidence
Scale 1-5:
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure; unlikely to have missed important details
- **3**: Reasonably confident but may have overlooked specifics
- **2**: Can defend evaluation but likely missed some details
- **1**: Outside expertise area; evaluation is educated guesswork

## Soundness
Scale 1-5 (with half-point increments):
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong support for claims; minor experiments could enhance
- **3**: Adequate support for main assertions; minor details need work
- **2**: Main claims lack sufficient support; major technical problems
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
Scale 1-5 (with half-point increments):
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: Would mention to colleagues; would attend presentation
- **3**: Might mention points; would attend if time permits
- **2**: Doesn't resonate personally but may interest others
- **1**: Unlikely to resonate with ACL community

## Overall Assessment
Scale 1-5 (with half-point increments):
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings track acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5217
}
```

</details>

---


### Tool call

_source line 1332 · 2026-05-25T21:19:49.399206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p11.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1333 · 2026-05-25T21:19:50.358176+00:00_



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

_source line 1334 · 2026-05-25T21:19:50.509104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p12.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 1335 · 2026-05-25T21:19:50.912336+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p13.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1336 · 2026-05-25T21:19:51.364809+00:00_



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

_source line 1337 · 2026-05-25T21:19:51.365259+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p14.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1338 · 2026-05-25T21:19:51.971351+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---


### Tool call

_source line 1339 · 2026-05-25T21:19:51.971790+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p15.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1340 · 2026-05-25T21:19:53.543575+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2178
}
```

</details>

---


### Tool result

_source line 1341 · 2026-05-25T21:19:54.052244+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2080
}
```

</details>

---


### Tool call

_source line 1342 · 2026-05-25T21:19:59.077072+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p16.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 1343 · 2026-05-25T21:19:59.429490+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p17.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1344 · 2026-05-25T21:19:59.884112+00:00_



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

_source line 1345 · 2026-05-25T21:19:59.886606+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p18.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1346 · 2026-05-25T21:20:00.843725+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1414
}
```

</details>

---


### Tool result

_source line 1347 · 2026-05-25T21:20:00.845222+00:00_



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

_source line 1348 · 2026-05-25T21:20:00.845584+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p19.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool call

_source line 1349 · 2026-05-25T21:20:01.147479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p20.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 1350 · 2026-05-25T21:20:01.758913+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 913
}
```

</details>

---


### Tool result

_source line 1351 · 2026-05-25T21:20:01.810589+00:00_



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


### Tool call

_source line 1352 · 2026-05-25T21:20:10.809432+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
  "limit": "100"
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
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1353 · 2026-05-25T21:20:11.110668+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
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
41	\noindent\textbf{Residual confounding.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself; residual confounding is not fully eliminated despite logistic adjustment.
43	
44	\noindent\textbf{Detection vs.\ amplification.}
45	The Blindspot may partly reflect pairwise format amplification \citep{jeong2025comparative} rather than pure detection; six controls bound this risk (\S\ref{sec:amplification}), but we cannot precisely quantify the amplification factor.
46	
47	\noindent\textbf{Scope.}
48	CSD applies only to surface-level axes whose rewrites preserve semantic content. Primary analyses use LLMBar ($n = 100$) with five judges; generalization to additional axes, benchmarks, and judges remains open.
49	
50	\bibliography{references}
51	
52	\input{sections/appendix}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1354 · 2026-05-25T21:20:11.111097+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
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
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1355 · 2026-05-25T21:20:11.211509+00:00_

No files found

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

_source line 1356 · 2026-05-25T21:20:14.627952+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
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
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1357 · 2026-05-25T21:20:14.630580+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 2
}
```

</details>

---


### Tool call

_source line 1358 · 2026-05-25T21:20:20.360843+00:00_

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

_source line 1359 · 2026-05-25T21:20:20.612026+00:00_

1	\begin{abstract}
2	Likert and pairwise scoring yield divergent style-sensitivity profiles in LLM judges.
3	We define the \emph{Likert Blindspot}: statistically significant pairwise sensitivity absent from Likert, admitting non-exclusive explanations (measurement attenuation, format amplification, construct divergence).
4	We introduce Controlled Style Decomposition (CSD), a black-box diagnostic combining natural language inference (NLI) gated content control, per-axis style decomposition, and position-controlled pairwise comparison.
5	Across four target judges and two axes (formality, verbosity), pairwise reaches significance ($p < 0.001$) where Likert does not ($p > 0.28$), selectively replicated across three benchmarks and confirmed by seven statistical methods; a fifth judge shows benchmark-dependent sensitivity.
6	At $n = 355$, Likert effect sizes collapse toward zero while pairwise remains stable; at $n = 330$, Likert begins detecting only the strongest effects, revealing a $3$--$4\times$ efficiency gap rather than absolute failure.
7	Generalized estimating equation (GEE) decomposition shows per-axis confound structures: verbosity is style-dominated (style odds ratio [OR] $8$--$13$ at $n{=}86$--$88$), while formality reflects joint style--quality confounding.
8	Non-tie concordance (76.6\%, $p < .001$) favors attenuation over construct divergence.
9	Likert-only audits risk missing style preferences that propagate through pairwise-based alignment pipelines\footnote{Code and data are available at \url{https://anonymous.4open.science/r/causal_style_decomp_judge-5EBE/}.}.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1360 · 2026-05-25T21:20:20.612425+00:00_

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

_source line 1361 · 2026-05-25T21:20:21.163919+00:00_

1	\section{Introduction}
2	
3	\emph{``What is the average height for a male?''} In our experiments, given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \emph{higher} on a 1--10 Likert scale (8 vs.\ 5), yet consistently selects the formal variant in pairwise comparison.
4	Same judge, same texts, opposite conclusions.
5	We term this the \emph{Likert Blindspot}, an operational descriptor for the measurement-mode divergence where pairwise comparison detects statistically significant style sensitivity that Likert scoring fails to detect on the same data, without committing to a specific causal mechanism.
6	This divergence admits multiple non-exclusive explanations (Likert measurement attenuation, pairwise format amplification \citep{jeong2025comparative}, or construct-level differences), which our controlled design bounds but cannot definitively adjudicate (\S\ref{sec:likert_pairwise}).
7	This example reflects a consistent pattern: surface-level style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}, with 76--92\% of preferences originating from style cues \citep{li2026preference,soumik2026judging}.
8	
9	LLM judges are central infrastructure for natural language processing (NLP) evaluation and alignment training (reinforcement learning from human feedback [RLHF], direct preference optimization [DPO]), where judge preferences serve as reward signals; any systematic bias propagates through both evaluation leaderboards and model development pipelines.
10	Despite this, existing approaches address individual requirements (multi-dimensional style analysis \citep{casse2026concise,wang2026fairjudge}, interventional design \citep{reber2025rate}, population-level correction \citep{dubois2025lc}), but no single framework integrates per-axis decomposition, interventional identification, confound-structure analysis, and black-box applicability.
11	Classical psychometrics es
…[truncated 2739 chars]

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

_source line 1362 · 2026-05-25T21:20:21.164392+00:00_

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

_source line 1363 · 2026-05-25T21:20:21.315066+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Interventional Approaches to Judge Bias}
5	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
6	\citet{reber2025rate} propose RATE, which rewrites outputs along style attributes and measures causal effects via Likert average treatment effect (ATE); however, our experiments show 60\% of style-transformed pairs receive identical Likert scores, yielding non-significant effects that pairwise comparison detects at $p = 0.006$.
7	CSD differs in targeting individual style axes, using position-controlled pairwise comparison, and enforcing content preservation via NLI gating.
8	\citet{counterfactual2025rhetorical} adopt a similar design at persona-level granularity, whereas CSD intervenes on specific style axes with position control.
9	
10	\paragraph{Style Bias in LLM Judges}
11	The foundational LLM-as-judge framework \citep{zheng2023judging} documented position bias; \citet{shi2024judging} study it across 15 judges, and \citet{ye2024justice} quantify 12 bias types, though neither isolates individual style effects.
12	Style bias as a separate source has received recent attention \citep{wu2023style,murugadoss2025sos,saito2023verbosity,li2026preference,soumik2026judging}; \citet{li2026preference} show that style-mediated \emph{preference leakage} propagates through evaluation pipelines.
13	Multi-feature frameworks such as CASSE \citep{casse2026concise} and FairJudge \citep{wang2026fairjudge} decompose style into finer dimensions but rely on correlational analyses that cannot distinguish causal style effects from content quality confounds.
14	\citet{jeong2025comparative} identify the Comparative Trap (pairwise comparison may amplify style biases), which we address in \S\ref{sec:amplification}.
15	Unlike human evaluators, LLM judges acquire format-specific biases through RLHF training: pairwise comparison serves as the reward signa
…[truncated 987 chars]

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

_source line 1364 · 2026-05-25T21:20:27.846924+00:00_

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

_source line 1365 · 2026-05-25T21:20:28.148776+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	The primary family comprises six tests (three target judges $\times$ two axes), corrected via Holm-Bonferroni at $\alpha = 0.05$; Gemini-2.5-Flash serves as confirmatory replication and is excluded from family-wise error rate (FWER) control; as a sensitivity check, all eight tests remain significant under the expanded family (Appendix~\ref{app:holm8}).
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses use uncorrected $p$-values; confirmatory analyses (pipeline validity) are evaluated at $\alpha = 0.05$ without additional correction.
12	Bradley-Terry parameters \citep{bradley1952rank,luce1959individual} are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the \texttt{choix} Python library's default L2 regularization ($\alpha = 10^{-6}$).
13	In binary-choice BT models, independence of irrelevant alternatives (IIA) is structurally satisfied; the direction asymmetry in Appendix~\ref{app:bt_gof} (formality: formal-origin 88.9\% vs.\ casual-origin 52.6\%, Fisher $p = 0.015$) reflects heterogeneous treatment effects rather than IIA violation.
14	All bootstrap confidence intervals are percentile CIs from 10{,}000 pair-level resamples with seed 42; we verify bootstrap stability by confirming that halving the resample count changes interval widths by $<$1pp.
15	GEE models use exchangeable working correlation with sandwich standard errors (robust to correlation misspecification), justified by near-zero estimated within-pair correlations ($\hat{\alpha} \in [-0.25, +0.11]$; Appendix~\ref{app:gee_diagnostics}).
16	A prospective power analysis 
…[truncated 19200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1366 · 2026-05-25T21:20:28.149188+00:00_

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

_source line 1367 · 2026-05-25T21:20:28.199641+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	CSD yields two findings: the \emph{Likert Blindspot} (8/8 primary cells, $d \!\to\! 0$ at $n{=}355$; concordance $p < .001$ favors attenuation) and per-axis confound structures via GEE (verbosity style-dominated, formality conditional).
4	Practically, Likert-only audits risk false negatives at benchmark sizes $n < 200$; per-axis decomposition reveals that verbosity preferences are predominantly style-driven while formality partially reflects quality differences---a distinction invisible to aggregate metrics and consequential for RLHF pipelines where pairwise judgments serve as reward signals.
5	CSD extends to any surface-level axis with content-preserving rewrites; deeper axes remain for future work.
6	

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

_source line 1368 · 2026-05-25T21:22:28.329067+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/\\\\//g' | wc -w",
  "description": "Count abstract words roughly"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/\\\\//g' | wc -w",
    "description": "Count abstract words roughly"
  }
}
```

</details>

---


### Tool result

_source line 1369 · 2026-05-25T21:22:28.531793+00:00_

176

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 1370 · 2026-05-25T21:22:40.676010+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM judge evaluation pairwise vs Likert rating measurement mode divergence 2025 2026"
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
    "query": "LLM judge evaluation pairwise vs Likert rating measurement mode divergence 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 1371 · 2026-05-25T21:22:41.780584+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"reward model\" style bias verbosity formality RLHF pairwise evaluation 2025 2026"
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
    "query": "\"reward model\" style bias verbosity formality RLHF pairwise evaluation 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 1372 · 2026-05-25T21:22:51.014709+00:00_

Web search results for query: ""reward model" style bias verbosity formality RLHF pairwise evaluation 2025 2026"

Links: [{"title":"One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models","url":"https://arxiv.org/html/2603.03291"},{"title":"Reward Modeling | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/05-reward-models"},{"title":"From Lists to Emojis: How Format Bias Affects Model Alignment","url":"https://arxiv.org/pdf/2409.11704"},{"title":"Rubric-Based Evaluations & LLM-as-a-Judge — Methodologies, Biases, and Empirical Validation in Domain-Specific Contexts. | by Adnan Masood, PhD. | Apr, 2026 | Medium","url":"https://medium.com/@adnanmasood/rubric-based-evals-llm-as-a-judge-methodologies-and-empirical-validation-in-domain-context-71936b989e80"},{"title":"A Unified Pairwise Framework for RLHF: Bridging","url":"https://arxiv.org/pdf/2504.04950"},{"title":"How to Evaluate Reward Models for RLHF","url":"https://arxiv.org/pdf/2410.14872"},{"title":"Bias Fitting to Mitigate Length Bias of Reward Model in RLHF","url":"https://arxiv.org/html/2505.12843v1"},{"title":"Mitigating Length Bias in RLHF through a Causal Lens","url":"https://arxiv.org/html/2511.12573"}]

Based on the search results, I found several recent papers and resources on reward models, style biases, and RLHF that are highly relevant to your query:

## Key Findings on Reward Models and Biases (2025-2026)

**Persistent Biases in Reward Models:**
Reward hacking during RLHF is a potential source of observed biases in language model behavior including length bias, position bias, overconfidence, and sycophantic user agreement.

**Verbosity and Style Issues:**
One prevalent form of reward hacking is the verbosity issue, where the policy generates unnecessarily lengthy responses in an attempt to appear more helpful or comprehensive. Additionally, recent studies reveal LLM evaluators exhibit inherent biases including self-preference for their own generat
…[truncated 990 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9234
}
```

</details>

---


### Tool result

_source line 1373 · 2026-05-25T21:22:59.107036+00:00_

Web search results for query: "LLM judge evaluation pairwise vs Likert rating measurement mode divergence 2025 2026"

Links: [{"title":"LLM-as-a-Judge Scoring","url":"https://www.emergentmind.com/topics/llm-as-a-judge-scoring"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://www.arxiv.org/pdf/2602.00521"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences   of LLM Evaluators","url":"https://arxiv.org/pdf/2406.12319"},{"title":"Evaluating AI Agents: Can LLM‑as‑a‑Judge Evaluators Be Trusted? | Microsoft Community Hub","url":"https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/evaluating-ai-agents-can-llm%E2%80%91as%E2%80%91a%E2%80%91judge-evaluators-be-trusted/4480110"},{"title":"The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2509.26072"},{"title":"Aligning with Human Judgement: The Role of Pairwise Preference in Large   Language Model Evaluators","url":"https://arxiv.org/pdf/2403.16950"},{"title":"Are We on the Right Way to Assessing LLM-as-a-Judge?","url":"https://arxiv.org/pdf/2512.16041"},{"title":"LLM-as-a-judge: a complete guide to using LLMs for evaluations","url":"https://www.evidentlyai.com/llm-guide/llm-as-a-judge"}]

Based on the search results, I found relevant information about LLM judge evaluation modes and their divergence:

## Key Findings on Pairwise vs. Likert Rating Evaluation

**Reliability Differences Between Modes:**

Pairwise evaluation tasks enable LLMs to approximate human preferences with greater fidelity than pointwise scoring, in part due to the comparative framing. In contrast, pointwise evaluation involves each candidate being independently assigned a score or correctness label, often on a Likert or fixed numerical scale.

**Measurement Mode Divergence:**

Recent research from 2025-2026 reveals significant divergence between scoring approaches. Agreement tends to be higher for binary scores, with the av
…[truncated 1045 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 18431
}
```

</details>

---


### Tool call

_source line 1374 · 2026-05-25T21:26:01.826608+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 2 — Round 1 审稿意见\n\n**论文**: \"The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\"\n**审查侧重**: 新颖性 / 完整性\n\n---\n\n### Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一种 black-box 诊断框架，通过 NLI 门控内容保持、单轴风格重写和位置控制的 pairwise 比较来检测 LLM judge 的风格敏感性。核心发现是 \"Likert Blindspot\"——在相同数据上 pairwise 比较能检测到的风格偏好在 Likert 评分中消失（8/8 primary cells），并通过 GEE 条件分解揭示不同风格轴的混杂结构差异（verbosity = style-dominated, formality = quality-confounded）。实验覆盖 4 个 target judges、2 个主轴、3 个 benchmark，并用 Claude Sonnet 4 提供 discriminative validity。\n\n---\n\n### Strengths\n\n**S1. GEE per-axis 分解是真正的方法论亮点。** Table 2 和 Figure 5 展示 verbosity 的 Style OR 8–13（Orig OR < 1）vs. formality 的双重显著效应，揭示了不同风格轴具有质性不同的混杂结构。这一发现对 bias mitigation 有直接实践指导意义（§5.2 最后一段明确指出了不同的应对策略），且此前未见于 LLM judge 文献。这比 \"Likert Blindspot\" 本身更具新颖性。\n\n**S2. 实验控制极其全面。** 六项 amplification 控制（§5.4: NLI ablation、Claude discriminative validity、cross-axis variation、GEE artifact absorption、debiased prompting bounds、four-architecture replication）系统性地约束了 pairwise amplification 的解释力。这种控制密度在同类工作中罕见。\n\n**S3. 统计方法论严谨。** Holm-Bonferroni FWER 控制、exploratory vs. confirmatory 分析的清晰分类（§4.1）、prospective power analysis（Figure 4, Appendix L）、bootstrap stability 验证、GEE sandwich SE——统计框架达到了高标准。特别是 n=355 scaled replication 区分 attenuation 与 insufficient power 的设计（d → -0.025 而非 non-zero）是有说服力的。\n\n**S4. Discriminative validity 设计。** Claude Sonnet 4 在 LLMBar 上 BT ≤ 0.562 (n.s.) 的结果（Table 1）证明 CSD 不会对所有 judge 均匀膨胀偏差估计。这有效排除了\"方法论 artifact 导致所有 judge 都显示 Blindspot\"的担忧。\n\n**S5. 实践意义清晰。** 论文直接指出：典型 benchmark 规模 (n=50-200) 下 Likert-only 审计系统性遗漏风格偏好，而这些偏好通过 RLHF/DPO 的 pairwise reward signal 传播到模型训练中。这对 alignment 社区有直接警示价值。\n\n**S6. 人类标注验证。** 两名标注者评估 100 对 NLI-scored pairs（§5.4），gate pass precision 98.6%，Gwet's AC₁ = 0.96。标注者仅判断 49-66% 的 NLI-passed pairs 有可检测到的风格变化，说明观察到的效应是真实风格敏感性的稀释下界——这个发现本身具有重要含义。\n\n---\n\n### Weaknesses\n\n#### Must-Fix 问题\n\n**N1** [critical] **标题与正文的 framing 张力**\n- 具体位置：Title, Abstract (第2句), §5.1 \"Interpreting the divergence\"\n- 问题：\"The Likert Blindspot\" 作为标题强烈暗示 Likert attenuation 是主因——Likert 有\"盲点\"，pairwise 看到了真相。然而正文 §5.1 明确列出三种非排他解释（attenuation, amplification, construct divergence），并承认 \"six controls bound the amplification factor but cannot eliminate it\"。标题的修辞倾向性与正文的审慎立场之间存在不可忽视的张力。读者的自然推断（\"Likert 有问题，pairwise 更好\"）与论文的实际结论（\"两种格式测量不同的东西，具体机制无法完全确定\"）不一致。\n- 为什么影响接收：Reviewer 和读者会质疑 framing 诚实性。如果论文无法确定 attenuation 是主因，标题不应预设这一解释。\n- 建议修改方向：(1) 在 Introduction 第一段更显著地承认心理测量学先驱（Thurstone 1927 已有引用，但应更明确说明 pairwise vs. rating 差异本身不新）；(2) 考虑更中性的标题如 \"Measurement-Mode Divergence in LLM Judge Style Evaluation\"；或 (3) 如果保留 \"Likert Blindspot\"，在 abstract 第一次出现时即加入 \"without committing to a specific causal mechanism\" 的限定（目前 abstract 第2句有此限定，但 \"Blindspot\" 本身的语义已预设了方向）。\n\n**N2** [critical] **核心新颖性定位不清晰——Thurstone (1927) 以来的增量贡献**\n- 具体位置：§1 Introduction 贡献列表, §2 Related Work \"Measurement Format Sensitivity\" 段\n- 问题：Pairwise comparison 比 rating scale 有更高 discriminability 是心理测量学自 Thurstone (1927) 以来的已知结论，被 Carterette & Allan (2008) 在 IR 中确认，被 Novikova et al. (2018) 在 NLG 中确认。论文引用了这些工作（§2 第三段），但贡献声明\"the first per-axis demonstration that pairwise and Likert formats yield qualitatively divergent style sensitivity profiles\"过度强调了\"first\"——在心理测量学意义上，这种 divergence 是预期的，不是发现。\n  真正的新贡献是：(a) 在 LLM judge 特有的上下文中（RLHF training 导致的 format-specific bias），这种 divergence 有质性不同的机制含义——不是人类 satisficing (Krosnick, 1999) 而是 training-induced format specificity；(b) GEE per-axis decomposition 揭示不同轴的混杂结构差异。但这两点在贡献声明中均未被突出。\n- 为什么影响接收：Novelty 是顶会接收的核心标准。如果论文被认为是\"已知心理测量效应的 domain transfer\"而没有充分的 domain-specific insight，可能被评为 incremental。\n- 建议修改方向：(1) 重新表述第一个贡献，明确为什么 LLM judge setting 与 human rater setting 有质性差异（RLHF/DPO 中 pairwise 作为 reward signal，Likert 用于 evaluation，两种格式在训练和评估中的角色不对称——这一点在 §2 最后一句提到但太简略）；(2) 将 GEE decomposition 提升为与 Likert Blindspot 并列甚至更突出的贡献。\n\n#### Should-Fix 问题\n\n**W1** [warning] **Rewriter-judge 重叠的处理不够显著**\n- 具体位置：Table 1 脚注 b, Appendix E\n- 问题：Qwen3-32B 同时作为 primary rewriter 和四个 target judges 之一。虽然 Appendix E 的 GPT-4o rewriter independence test 显示 Blindspot 仍然存在但 Style OR 降低 22%，这不是一个可以忽略的差距。Table 1 仅在脚注中提到 \"independent GPT-4o rewriter yields 22% lower Style OR\"，一个注意力分散的读者很容易忽略。\n- 建议：在正文 §5.4 或 §4 中用 1-2 句话正式讨论 rewriter-judge overlap 及其影响范围，而不是依赖表格脚注和 appendix。\n\n**W2** [warning] **Cross-benchmark replication 的选择性策略需要更强的辩护**\n- 具体位置：§5.3 最后一段, Figure 6, Table 23 (Appendix W)\n- 问题：Cross-benchmark validation 仅覆盖 6/24 possible cells（25%），且论文承认这是 \"targeting the strongest effects\"。这本质上是一种 cherry-picking 策略——在主要分析中发现最强效应后，选择性地在其他 benchmark 上验证这些最强效应。虽然论文的透明度值得肯定（明确声明了选择标准），但这极大地限制了 generalizability claims 的说服力。特别是，4 个 exception cells (†‡) 表明 Blindspot 的可复制性取决于 effect size，但论文对这些 exceptions 的讨论主要通过\"severity spectrum\"来解释，这更像是 post-hoc rationalization。\n- 建议：(1) 更明确地承认选择性 replication 的局限性；(2) 考虑在 Limitations 中加入一句关于 cross-benchmark coverage 不足的声明。\n\n**W3** [warning] **Table 1 信息密度过高，可读性受损**\n- 具体位置：Table 1 (第5页)\n- 问题：15 行数据 + 5 个不同标记符号 (***、*、†、†_e、†_c、---) + 3 个脚注（其中一个长达 2 行描述 direction asymmetry）。读者需要来回查阅脚注和正文才能理解各行的分类标准。Gemini 作为 \"confirmatory\" 和 Claude 作为 \"discriminative validity\" 的角色区分依赖于微小的下标符号。\n- 建议：(1) 将 exploratory register 结果移到 appendix，主表保留 primary + confirmatory 结果；(2) 或将 discriminative validity (Claude) 单独列为子表。\n\n**W4** [warning] **\"Consistent pattern\" 等措辞与实际数据的匹配度**\n- 具体位置：§1 (第1页 \"reflects a consistent pattern\"), Abstract (\"selectively replicated\"), §5.1 (\"manifests in 10/14 bias-positive cells\")\n- 问题：论文报告 Blindspot 出现在 10/14 bias-positive cells 中（~71%），4 个 exceptions。Claude 在 LLMBar 上两个轴均为 null。Cross-benchmark 仅 6/24 cells 被测试。\"Consistent pattern\" 的措辞在主文中出现，但 ~29% 的 exception rate 和 Claude 的完全 null 结果（后被重新 framed 为 \"discriminative validity\"）使 \"consistent\" 这个词的准确性可商榷。论文对 Claude 的处理很巧妙——将 null 结果转化为方法论优势——但这同时意味着该 phenomenon 是 model-specific 的，这与 \"consistent\" 的含义存在张力。\n- 建议：在 Introduction 中用更精确的措辞替代 \"consistent pattern\"，如 \"predominant pattern\" 或 \"majority pattern\"，并更早地引入 model-specific variation 的概念。\n\n**W5** [warning] **风格轴覆盖范围有限**\n- 具体位置：§3.4, Limitations §3\n- 问题：仅两个 primary axes（formality, verbosity）+ 一个 exploratory（register）。风格是多维的——tone、sentiment、readability、technical jargon level、hedging 等均为已知的 LLM judge 敏感维度。论文在 Limitations 中承认 \"CSD applies only to surface-level axes\"，但正文的 claim 措辞（\"per-axis demonstration\"）暗示了比实际覆盖更广的 scope。GEE decomposition 发现 formality 和 verbosity 有质性不同的混杂结构，这恰恰说明不能从两个轴外推到其他轴。\n- 建议：在贡献声明中更明确限定 scope，例如 \"across the two most commonly reported style axes\"。\n\n#### Minor 问题\n\n**M1** Appendix 组织：20 页中有约 10 页 appendix（pages 11-20），包含 A-Z 共 23+ 个 section。虽然 thoroughness 值得肯定，但部分 appendix（如 Appendix O \"100-Point Continuous Likert Scale\"、Appendix P \"NLI Gate Ablation\"）的内容可以合并或精简。建议用 hierarchical 编号（A.1, A.2）替代 flat structure。\n\n**M2** Figure 2 (DAG) 标注为 \"Assumed data-generating process (design rationale, not a claim of perfect identification)\"——这是好的科学实践，但 \"assumed\" 这个词在图题中可能暗示比实际更弱的信心。建议在正文中保留 caveat，图题简化为描述性标题。\n\n**M3** §5.1 \"Head-to-head comparison with RATE\" 段直接对比 RATE 方法论，措辞 \"our experiments show 60% of style-transformed pairs receive identical Likert scores\" 可能被 RATE 作者解读为不公平比较，因为 RATE 的设计意图和 CSD 不同（RATE 测量 ATE，CSD 测量 BT win probability）。建议更中性地表述为方法互补而非 CSD 优于 RATE。\n\n**M4** 论文末尾 (第20页) 的 \"Use of AI Assistants\" 声明提到使用 Claude (Anthropic) 进行代码、写作和文献总结。Claude Sonnet 4 同时是 discriminative validity judge。虽然这不构成利益冲突（Claude 显示 null results，如果有偏，应该偏向对 Claude 有利的结论），但建议在 Limitations 中简要提及这一双重角色。\n\n---\n\n### Questions（需要作者澄清）\n\n**Q1.** 为什么不对所有分析使用完全独立的 rewriter？Appendix E 的 GPT-4o rewriter 测试显示 Style OR 下降 22%，这暗示 Qwen3-32B 的 rewriter-judge overlap 对 effect size 有非 trivial 的贡献。如果资源允许，使用独立 rewriter 重跑全部分析是否会改变主要结论？\n\n**Q2.** Claude Sonnet 4 在 LLMBar 上显示 null results，但在 AEval verbosity 上 Style OR = 4.76 (p < .001)（§5.1 最后一段, Appendix H）。作者如何解释这一 benchmark-dependent 差异？是 LLMBar 的样本特性（100 条 instruction-response pairs）导致 power 不足，还是 Claude 确实对不同 benchmark 有不同的风格敏感性？这一模式对 \"Likert Blindspot\" 作为 general phenomenon 的 claim 有什么影响？\n\n**Q3.** 论文使用 NLI entailment threshold 0.90 作为 gate（§3.2）。Appendix F 的 threshold sweep 显示 BT 在 11 个 threshold 下 stable (≤3pp variation)。但 NLI gate 的 precision 和 recall 之间的 tradeoff 是否被充分探索？更严格的 threshold（如 0.95）会如何影响 sample size 和 power？\n\n**Q4.** Introduction 的 motivating example（\"What is the average height for a male?\"）中，GPT-4o 在 Likert 上给 casual version 更高分 (8 vs. 5)。这与 formality Blindspot 的整体方向一致（pairwise 选择 formal，Likert 无显著偏好）。但 Likert 反向偏好（casual 更高）是单个 example 的偶然现象还是系统性模式？如果是后者，这不是 \"Blindspot\"（Likert 看不到）而是 \"Likert Reversal\"（Likert 看到反方向），应该在叙事中更明确区分。\n\n**Q5.** GEE decomposition 中 formality 的 Originality OR 显著（Table 2: GPT-4o Orig OR = 2.32, p = .006）意味着 style-controlled rewriting 未能完全控制原始偏好。这是 NLI gate 的局限还是 formality 与 quality 之间的固有关联？如果是后者，per-axis decomposition 能否真正实现 causal identification？\n\n---\n\n### Missing References\n\n1. **IRT-based LLM judge reliability**: \"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory\" (arXiv:2602.00521, 2026) — 使用 Item Response Theory 分析 LLM judge reliability，与本文的 measurement methodology 讨论直接相关，提供了另一种诊断 measurement mode 差异的理论框架。\n\n2. **Length bias in RLHF reward models**: \"Mitigating Length Bias in RLHF through a Causal Lens\" (arXiv:2511.12573, 2025) 和 \"Bias Fitting to Mitigate Length Bias of Reward Model in RLHF\" (arXiv:2505.12843, 2025) — 这两篇直接用因果方法处理 RLHF 中的 length/verbosity bias，与本文的 causal framing 和 verbosity axis 发现高度相关。\n\n3. **Format bias in alignment**: \"From Lists to Emojis: How Format Bias Affects Model Alignment\" (arXiv:2409.11704, 2024) — 研究 format bias 如何影响 model alignment，与本文的 measurement-mode divergence 和 RLHF 影响讨论相关。\n\n4. **Pairwise preference in LLM evaluators**: \"Aligning with Human Judgement: The Role of Pairwise Preference in Large Language Model Evaluators\" (arXiv:2403.16950, 2024) — 直接研究 pairwise preference 在 LLM evaluator 中的角色，应在 Related Work §2 中被讨论。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 方法论整体严谨，统计框架达到高标准，controls 全面。但 rewriter-judge overlap 的 22% Style OR 下降表明核心 effect size 有非 trivial 的方法论敏感性；cross-benchmark replication 的选择性策略（6/24 cells）限制了 generalizability。Title/framing 与正文三种非排他解释之间的张力影响了 claim 的准确性。 |\n| **Excitement** | 3/5 | GEE per-axis decomposition 是有趣的方法论贡献，实践意义（RLHF pipeline 影响）清晰。但核心发现（pairwise > Likert in discriminability）是心理测量学已知效应的 domain transfer，novelty ceiling 受限。两个风格轴的覆盖不足以支撑更广泛的 claim。 |\n\n### Overall Assessment\n\n**3.5 — Borderline Conference**\n\n本文是一篇技术执行扎实、实验控制全面的工作。GEE per-axis decomposition 提供了 LLM judge bias 文献中未见的 insight（verbosity = style-dominated vs. formality = quality-confounded），discriminative validity 设计（Claude null results）增强了方法论可信度。统计方法论达到了顶会标准。\n\n主要顾虑集中在新颖性和 framing：(1) \"Likert Blindspot\" 的核心发现——pairwise 比 Likert 更敏感——是自 Thurstone (1927) 以来的已知心理测量效应，论文在 LLM judge domain 的 transfer 虽然有实践价值，但概念贡献有限；(2) 标题和叙事预设了 Likert attenuation 解释，与正文对三种非排他解释的审慎讨论不一致；(3) 两个 primary style axes + 选择性 cross-benchmark replication (6/24 cells) 的覆盖范围不足以支撑论文的 generalizability 暗示。\n\n如果作者能 (a) 更清晰地定位 LLM judge setting 相对于经典心理测量的质性差异（RLHF training-induced format specificity），(b) 将 GEE decomposition 提升为更显著的贡献，(c) 解决 title/framing 张力，本文有潜力达到 Conference acceptance 水平。\n\n### Confidence\n\n**4/5** — 熟悉 LLM judge evaluation、心理测量方法论和因果推断的相关文献。仔细阅读了全文 20 页及 LaTeX 源码。\n",
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
    "text": "\n## Reviewer 2 — Round 1 审稿意见\n\n**论文**: \"The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation\"\n**审查侧重**: 新颖性 / 完整性\n\n---\n\n### Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一种 black-box 诊断框架，通过 NLI 门控内容保持、单轴风格重写和位置控制的 pairwise 比较来检测 LLM judge 的风格敏感性。核心发现是 \"Likert Blindspot\"——在相同数据上 pairwise 比较能检测到的风格偏好在 Likert 评分中消失（8/8 primary cells），并通过 GEE 条件分解揭示不同风格轴的混杂结构差异（verbosity = style-dominated, formality = quality-confounded）。实验覆盖 4 个 target judges、2 个主轴、3 个 benchmark，并用 Claude Sonnet 4 提供 discriminative validity。\n\n---\n\n### Strengths\n\n**S1. GEE per-axis 分解是真正的方法论亮点。** Table 2 和 Figure 5 展示 verbosity 的 Style OR 8–13（Orig OR < 1）vs. formality 的双重显著效应，揭示了不同风格轴具有质性不同的混杂结构。这一发现对 bias mitigation 有直接实践指导意义（§5.2 最后一段明确指出了不同的应对策略），且此前未见于 LLM judge 文献。这比 \"Likert Blindspot\" 本身更具新颖性。\n\n**S2. 实验控制极其全面。** 六项 amplification 控制（§5.4: NLI ablation、Claude discriminative validity、cross-axis variation、GEE artifact absorption、debiased prompting bounds、four-architecture replication）系统性地约束了 pairwise amplification 的解释力。这种控制密度在同类工作中罕见。\n\n**S3. 统计方法论严谨。** Holm-Bonferroni FWER 控制、exploratory vs. confirmatory 分析的清晰分类（§4.1）、prospective power analysis（Figure 4, Appendix L）、bootstrap stability 验证、GEE sandwich SE——统计框架达到了高标准。特别是 n=355 scaled replication 区分 attenuation 与 insufficient power 的设计（d → -0.025 而非 non-zero）是有说服力的。\n\n**S4. Discriminative validity 设计。** Claude Sonnet 4 在 LLMBar 上 BT ≤ 0.562 (n.s.) 的结果（Table 1）证明 CSD 不会对所有 judge 均匀膨胀偏差估计。这有效排除了\"方法论 artifact 导致所有 judge 都显示 Blindspot\"的担忧。\n\n**S5. 实践意义清晰。** 论文直接指出：典型 benchmark 规模 (n=50-200) 下 Likert-only 审计系统性遗漏风格偏好，而这些偏好通过 RLHF/DPO 的 pairwise reward signal 传播到模型训练中。这对 alignment 社区有直接警示价值。\n\n**S6. 人类标注验证。** 两名标注者评估 100 对 NLI-scored pairs（§5.4），gate pass precision 98.6%，Gwet's AC₁ = 0.96。标注者仅判断 49-66% 的 NLI-passed pairs 有可检测到的风格变化，说明观察到的效应是真实风格敏感性的稀释下界——这个发现本身具有重要含义。\n\n---\n\n### Weaknesses\n\n#### Must-Fix 问题\n\n**N1** [critical] **标题与正文的 framing 张力**\n- 具体位置：Title, Abstract (第2句), §5.1 \"Interpreting the divergence\"\n- 问题：\"The Likert Blindspot\" 作为标题强烈暗示 Likert attenuation 是主因——Likert 有\"盲点\"，pairwise 看到了真相。然而正文 §5.1 明确列出三种非排他解释（attenuation, amplification, construct divergence），并承认 \"six controls bound the amplification factor but cannot eliminate it\"。标题的修辞倾向性与正文的审慎立场之间存在不可忽视的张力。读者的自然推断（\"Likert 有问题，pairwise 更好\"）与论文的实际结论（\"两种格式测量不同的东西，具体机制无法完全确定\"）不一致。\n- 为什么影响接收：Reviewer 和读者会质疑 framing 诚实性。如果论文无法确定 attenuation 是主因，标题不应预设这一解释。\n- 建议修改方向：(1) 在 Introduction 第一段更显著地承认心理测量学先驱（Thurstone 1927 已有引用，但应更明确说明 pairwise vs. rating 差异本身不新）；(2) 考虑更中性的标题如 \"Measurement-Mode Divergence in LLM Judge Style Evaluation\"；或 (3) 如果保留 \"Likert Blindspot\"，在 abstract 第一次出现时即加入 \"without committing to a specific causal mechanism\" 的限定（目前 abstract 第2句有此限定，但 \"Blindspot\" 本身的语义已预设了方向）。\n\n**N2** [critical] **核心新颖性定位不清晰——Thurstone (1927) 以来的增量贡献**\n- 具体位置：§1 Introduction 贡献列表, §2 Related Work \"Measurement Format Sensitivity\" 段\n- 问题：Pairwise comparison 比 rating scale 有更高 discriminability 是心理测量学自 Thurstone (1927) 以来的已知结论，被 Carterette & Allan (2008) 在 IR 中确认，被 Novikova et al. (2018) 在 NLG 中确认。论文引用了这些工作（§2 第三段），但贡献声明\"the first per-axis demonstration that pairwise and Likert formats yield qualitatively divergent style sensitivity profiles\"过度强调了\"first\"——在心理测量学意义上，这种 divergence 是预期的，不是发现。\n  真正的新贡献是：(a) 在 LLM judge 特有的上下文中（RLHF training 导致的 format-specific bias），这种 divergence 有质性不同的机制含义——不是人类 satisficing (Krosnick, 1999) 而是 training-induced format specificity；(b) GEE per-axis decomposition 揭示不同轴的混杂结构差异。但这两点在贡献声明中均未被突出。\n- 为什么影响接收：Novelty 是顶会接收的核心标准。如果论文被认为是\"已知心理测量效应的 domain transfer\"而没有充分的 domain-specific insight，可能被评为 incremental。\n- 建议修改方向：(1) 重新表述第一个贡献，明确为什么 LLM judge setting 与 human rater setting 有质性差异（RLHF/DPO 中 pairwise 作为 reward signal，Likert 用于 evaluation，两种格式在训练和评估中的角色不对称——这一点在 §2 最后一句提到但太简略）；(2) 将 GEE decomposition 提升为与 Likert Blindspot 并列甚至更突出的贡献。\n\n#### Should-Fix 问题\n\n**W1** [warning] **Rewriter-judge 重叠的处理不够显著**\n- 具体位置：Table 1 脚注 b, Appendix E\n- 问题：Qwen3-32B 同时作为 primary rewriter 和四个 target judges 之一。虽然 Appendix E 的 GPT-4o rewriter independence test 显示 Blindspot 仍然存在但 Style OR 降低 22%，这不是一个可以忽略的差距。Table 1 仅在脚注中提到 \"independent GPT-4o rewriter yields 22% lower Style OR\"，一个注意力分散的读者很容易忽略。\n- 建议：在正文 §5.4 或 §4 中用 1-2 句话正式讨论 rewriter-judge overlap 及其影响范围，而不是依赖表格脚注和 appendix。\n\n**W2** [warning] **Cross-benchmark replication 的选择性策略需要更强的辩护**\n- 具体位置：§5.3 最后一段, Figure 6, Table 23 (Appendix W)\n- 问题：Cross-benchmark validation 仅覆盖 6/24 possible cells（25%），且论文承认这是 \"targeting the strongest effects\"。这本质上是一种 cherry-picking 策略——在主要分析中发现最强效应后，选择性地在其他 benchmark 上验证这些最强效应。虽然论文的透明度值得肯定（明确声明了选择标准），但这极大地限制了 generalizability claims 的说服力。特别是，4 个 exception cells (†‡) 表明 Blindspot 的可复制性取决于 effect size，但论文对这些 exceptions 的讨论主要通过\"severity spectrum\"来解释，这更像是 post-hoc rationalization。\n- 建议：(1) 更明确地承认选择性 replication 的局限性；(2) 考虑在 Limitations 中加入一句关于 cross-benchmark coverage 不足的声明。\n\n**W3** [warning] **Table 1 信息密度过高，可读性受损**\n- 具体位置：Table 1 (第5页)\n- 问题：15 行数据 + 5 个不同标记符号 (***、*、†、†_e、†_c、---) + 3 个脚注（其中一个长达 2 行描述 direction asymmetry）。读者需要来回查阅脚注和正文才能理解各行的分类标准。Gemini 作为 \"confirmatory\" 和 Claude 作为 \"discriminative validity\" 的角色区分依赖于微小的下标符号。\n- 建议：(1) 将 exploratory register 结果移到 appendix，主表保留 primary + confirmatory 结果；(2) 或将 discriminative validity (Claude) 单独列为子表。\n\n**W4** [warning] **\"Consistent pattern\" 等措辞与实际数据的匹配度**\n- 具体位置：§1 (第1页 \"reflects a consistent pattern\"), Abstract (\"selectively replicated\"), §5.1 (\"manifests in 10/14 bias-positive cells\")\n- 问题：论文报告 Blindspot 出现在 10/14 bias-positive cells 中（~71%），4 个 exceptions。Claude 在 LLMBar 上两个轴均为 null。Cross-benchmark 仅 6/24 cells 被测试。\"Consistent pattern\" 的措辞在主文中出现，但 ~29% 的 exception rate 和 Claude 的完全 null 结果（后被重新 framed 为 \"discriminative validity\"）使 \"consistent\" 这个词的准确性可商榷。论文对 Claude 的处理很巧妙——将 null 结果转化为方法论优势——但这同时意味着该 phenomenon 是 model-specific 的，这与 \"consistent\" 的含义存在张力。\n- 建议：在 Introduction 中用更精确的措辞替代 \"consistent pattern\"，如 \"predominant pattern\" 或 \"majority pattern\"，并更早地引入 model-specific variation 的概念。\n\n**W5** [warning] **风格轴覆盖范围有限**\n- 具体位置：§3.4, Limitations §3\n- 问题：仅两个 primary axes（formality, verbosity）+ 一个 exploratory（register）。风格是多维的——tone、sentiment、readability、technical jargon level、hedging 等均为已知的 LLM judge 敏感维度。论文在 Limitations 中承认 \"CSD applies only to surface-level axes\"，但正文的 claim 措辞（\"per-axis demonstration\"）暗示了比实际覆盖更广的 scope。GEE decomposition 发现 formality 和 verbosity 有质性不同的混杂结构，这恰恰说明不能从两个轴外推到其他轴。\n- 建议：在贡献声明中更明确限定 scope，例如 \"across the two most commonly reported style axes\"。\n\n#### Minor 问题\n\n**M1** Appendix 组织：20 页中有约 10 页 appendix（pages 11-20），包含 A-Z 共 23+ 个 section。虽然 thoroughness 值得肯定，但部分 appendix（如 Appendix O \"100-Point Continuous Likert Scale\"、Appendix P \"NLI Gate Ablation\"）的内容可以合并或精简。建议用 hierarchical 编号（A.1, A.2）替代 flat structure。\n\n**M2** Figure 2 (DAG) 标注为 \"Assumed data-generating process (design rationale, not a claim of perfect identification)\"——这是好的科学实践，但 \"assumed\" 这个词在图题中可能暗示比实际更弱的信心。建议在正文中保留 caveat，图题简化为描述性标题。\n\n**M3** §5.1 \"Head-to-head comparison with RATE\" 段直接对比 RATE 方法论，措辞 \"our experiments show 60% of style-transformed pairs receive identical Likert scores\" 可能被 RATE 作者解读为不公平比较，因为 RATE 的设计意图和 CSD 不同（RATE 测量 ATE，CSD 测量 BT win probability）。建议更中性地表述为方法互补而非 CSD 优于 RATE。\n\n**M4** 论文末尾 (第20页) 的 \"Use of AI Assistants\" 声明提到使用 Claude (Anthropic) 进行代码、写作和文献总结。Claude Sonnet 4 同时是 discriminative validity judge。虽然这不构成利益冲突（Claude 显示 null results，如果有偏，应该偏向对 Claude 有利的结论），但建议在 Limitations 中简要提及这一双重角色。\n\n---\n\n### Questions（需要作者澄清）\n\n**Q1.** 为什么不对所有分析使用完全独立的 rewriter？Appendix E 的 GPT-4o rewriter 测试显示 Style OR 下降 22%，这暗示 Qwen3-32B 的 rewriter-judge overlap 对 effect size 有非 trivial 的贡献。如果资源允许，使用独立 rewriter 重跑全部分析是否会改变主要结论？\n\n**Q2.** Claude Sonnet 4 在 LLMBar 上显示 null results，但在 AEval verbosity 上 Style OR = 4.76 (p < .001)（§5.1 最后一段, Appendix H）。作者如何解释这一 benchmark-dependent 差异？是 LLMBar 的样本特性（100 条 instruction-response pairs）导致 power 不足，还是 Claude 确实对不同 benchmark 有不同的风格敏感性？这一模式对 \"Likert Blindspot\" 作为 general phenomenon 的 claim 有什么影响？\n\n**Q3.** 论文使用 NLI entailment threshold 0.90 作为 gate（§3.2）。Appendix F 的 threshold sweep 显示 BT 在 11 个 threshold 下 stable (≤3pp variation)。但 NLI gate 的 precision 和 recall 之间的 tradeoff 是否被充分探索？更严格的 threshold（如 0.95）会如何影响 sample size 和 power？\n\n**Q4.** Introduction 的 motivating example（\"What is the average height for a male?\"）中，GPT-4o 在 Likert 上给 casual version 更高分 (8 vs. 5)。这与 formality Blindspot 的整体方向一致（pairwise 选择 formal，Likert 无显著偏好）。但 Likert 反向偏好（casual 更高）是单个 example 的偶然现象还是系统性模式？如果是后者，这不是 \"Blindspot\"（Likert 看不到）而是 \"Likert Reversal\"（Likert 看到反方向），应该在叙事中更明确区分。\n\n**Q5.** GEE decomposition 中 formality 的 Originality OR 显著（Table 2: GPT-4o Orig OR = 2.32, p = .006）意味着 style-controlled rewriting 未能完全控制原始偏好。这是 NLI gate 的局限还是 formality 与 quality 之间的固有关联？如果是后者，per-axis decomposition 能否真正实现 causal identification？\n\n---\n\n### Missing References\n\n1. **IRT-based LLM judge reliability**: \"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory\" (arXiv:2602.00521, 2026) — 使用 Item Response Theory 分析 LLM judge reliability，与本文的 measurement methodology 讨论直接相关，提供了另一种诊断 measurement mode 差异的理论框架。\n\n2. **Length bias in RLHF reward models**: \"Mitigating Length Bias in RLHF through a Causal Lens\" (arXiv:2511.12573, 2025) 和 \"Bias Fitting to Mitigate Length Bias of Reward Model in RLHF\" (arXiv:2505.12843, 2025) — 这两篇直接用因果方法处理 RLHF 中的 length/verbosity bias，与本文的 causal framing 和 verbosity axis 发现高度相关。\n\n3. **Format bias in alignment**: \"From Lists to Emojis: How Format Bias Affects Model Alignment\" (arXiv:2409.11704, 2024) — 研究 format bias 如何影响 model alignment，与本文的 measurement-mode divergence 和 RLHF 影响讨论相关。\n\n4. **Pairwise preference in LLM evaluators**: \"Aligning with Human Judgement: The Role of Pairwise Preference in Large Language Model Evaluators\" (arXiv:2403.16950, 2024) — 直接研究 pairwise preference 在 LLM evaluator 中的角色，应在 Related Work §2 中被讨论。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 方法论整体严谨，统计框架达到高标准，controls 全面。但 rewriter-judge overlap 的 22% Style OR 下降表明核心 effect size 有非 trivial 的方法论敏感性；cross-benchmark replication 的选择性策略（6/24 cells）限制了 generalizability。Title/framing 与正文三种非排他解释之间的张力影响了 claim 的准确性。 |\n| **Excitement** | 3/5 | GEE per-axis decomposition 是有趣的方法论贡献，实践意义（RLHF pipeline 影响）清晰。但核心发现（pairwise > Likert in discriminability）是心理测量学已知效应的 domain transfer，novelty ceiling 受限。两个风格轴的覆盖不足以支撑更广泛的 claim。 |\n\n### Overall Assessment\n\n**3.5 — Borderline Conference**\n\n本文是一篇技术执行扎实、实验控制全面的工作。GEE per-axis decomposition 提供了 LLM judge bias 文献中未见的 insight（verbosity = style-dominated vs. formality = quality-confounded），discriminative validity 设计（Claude null results）增强了方法论可信度。统计方法论达到了顶会标准。\n\n主要顾虑集中在新颖性和 framing：(1) \"Likert Blindspot\" 的核心发现——pairwise 比 Likert 更敏感——是自 Thurstone (1927) 以来的已知心理测量效应，论文在 LLM judge domain 的 transfer 虽然有实践价值，但概念贡献有限；(2) 标题和叙事预设了 Likert attenuation 解释，与正文对三种非排他解释的审慎讨论不一致；(3) 两个 primary style axes + 选择性 cross-benchmark replication (6/24 cells) 的覆盖范围不足以支撑论文的 generalizability 暗示。\n\n如果作者能 (a) 更清晰地定位 LLM judge setting 相对于经典心理测量的质性差异（RLHF training-induced format specificity），(b) 将 GEE decomposition 提升为更显著的贡献，(c) 解决 title/framing 张力，本文有潜力达到 Conference acceptance 水平。\n\n### Confidence\n\n**4/5** — 熟悉 LLM judge evaluation、心理测量方法论和因果推断的相关文献。仔细阅读了全文 20 页及 LaTeX 源码。\n",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1375 · 2026-05-25T21:26:06.117876+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4291
}
```

</details>

---


### Tool call

_source line 1376 · 2026-05-25T21:26:14.967611+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images"
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
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1377 · 2026-05-25T21:26:14.968258+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/review_round_17/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

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

_source line 1378 · 2026-05-25T21:26:26.148400+00:00_

审稿意见已提交给 Review Director。

核心评判：**Overall 3.5（Borderline Conference）**。

主要发现：
- **两个 Must-Fix**：(1) 标题 "Likert Blindspot" 预设了 attenuation 解释，与正文三种非排他解释的审慎立场存在张力；(2) 核心新颖性定位不清——pairwise > Likert 是 Thurstone (1927) 以来的已知效应，论文需要更明确地阐述 LLM judge setting 的质性差异（RLHF format specificity）。
- **GEE per-axis decomposition** 是本文真正最强的贡献（verbosity = style-dominated vs. formality = quality-confounded），但在叙事中被 "Likert Blindspot" 遮蔽。
- **四个 Should-Fix**：rewriter-judge overlap 处理不够显著、cross-benchmark replication 选择性、Table 1 可读性、"consistent pattern" 措辞与 ~29% exception rate 的匹配。
- 建议补充 4 篇 missing references（IRT-based reliability、causal length bias in RLHF、format bias in alignment、pairwise preference in LLM evaluators）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---


## Round 40

## Round 40

18 recorded events


### User

_source line 1379 · 2026-05-25T21:27:35.592713+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1（方法严谨性侧重）的完整审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注 Reviewer 1 提出的你可能遗漏的问题，以及你们之间可能存在的分歧。

---

### Reviewer 1 完整审稿意见

**Summary**: 本文定义了 "Likert Blindspot"：在相同数据上，pairwise comparison 能检测到统计显著的风格敏感性，而 Likert 评分却无法检测。作者提出 CSD 框架，在 4 个目标 judge 和 1 个负对照 (Claude) 上验证了该现象。方法设计整体严谨，robustness 检查覆盖面广，但在统计效力分析的定位、跨基准复制的选择性、以及 evaluator-producer 重叠的处理上存在需修正的问题。

**Strengths**:
- S1: 实验设计的系统性与完备性（单轴干预 + NLI 门控 + 位置对消 + double-rewrite 控制）
- S2: Robustness 检查覆盖面异常广泛（11 个 NLI 阈值 sweep, direction-aware gating, rewriter independence, 100-point Likert, GEE 相关结构对比, interaction test, BT 正则化）
- S3: 统计方法选择总体恰当（BT + GEE + sandwich SE）
- S4: 因果语言的审慎使用（§5.2 和 Appendix A 的 disclaimer）
- S5: 负对照设计有意义（Claude TOST + Bayesian BF₁₀）
- S6: Human annotation validation 设计合理（AC₁ = 0.96）

**Must-Fix**:
- **N1 [critical]**: Power analysis 存在 post-hoc 循环论证风险。正文称 "prospective power analysis" 但 effect size 来自同一批数据——Hoenig & Heisey (2001)（论文自身引用）所批评的谬误。建议改为 "sensitivity power analysis"。
- **N2 [critical]**: 跨基准复制选择性构成确认偏差——仅选 24 cells 中效应最强的 6 个，未报告其余 18 cells。

**Should-Fix**:
- **W1**: GEE OR ~49% shrinkage (n=88→355) 讨论不足，Table 2 全部基于 n=88
- **W2**: Evaluator-producer overlap (Qwen3-32B) 残留 22% 膨胀
- **W3**: TOST 等价界 Δ=12pp 偏宽松——Blindspot 效应本身仅 ~13-18pp
- **W4**: Section 3.1 "per-axis causal attribution" 与 Appendix A disclaimer 语调不一致
- **W5**: Same-style double-rewrite 在 verbosity 轴暴露 rewriting artifact (BT P(orig)=0.082)

**Minor**:
- M1: BT 正则化参数 §4.1 (α=10⁻⁴) vs Appendix R (α=10⁻⁷) 不一致
- M2: GEE ρ∈[−0.25,+0.11]，ρ=−0.25 非 "near-zero"
- M3: Table 1 adjusted p-values 校正方法未说明
- M4: Figure 4 y轴 "at observed effect magnitudes" 强化 post-hoc 印象

**Questions**:
- Q1: Power analysis effect size 有 pilot/先验来源？
- Q2: 未测试的 18 cells 有结果可报告？
- Q3: Verbosity same-style rewrite artifact 在 GEE Orig OR 中被吸收多少？
- Q4: BT 正则化参数实际用的是哪个？
- Q5: n=355 GEE 估计可否并列报告？

**Scores**: Soundness 3.5/5, Excitement 3.5/5, Reproducibility 4/5, Overall 3.5 (Borderline Conference), Confidence 4/5

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

_source line 1380 · 2026-05-25T21:28:45.903617+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex",
  "offset": "10",
  "limit": "20"
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
    "offset": "10",
    "limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 1381 · 2026-05-25T21:28:46.305537+00:00_

10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses use uncorrected $p$-values; confirmatory analyses (pipeline validity) are evaluated at $\alpha = 0.05$ without additional correction.
12	Bradley-Terry parameters \citep{bradley1952rank,luce1959individual} are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the \texttt{choix} Python library's default L2 regularization ($\alpha = 10^{-6}$).
13	In binary-choice BT models, independence of irrelevant alternatives (IIA) is structurally satisfied; the direction asymmetry in Appendix~\ref{app:bt_gof} (formality: formal-origin 88.9\% vs.\ casual-origin 52.6\%, Fisher $p = 0.015$) reflects heterogeneous treatment effects rather than IIA violation.
14	All bootstrap confidence intervals are percentile CIs from 10{,}000 pair-level resamples with seed 42; we verify bootstrap stability by confirming that halving the resample count changes interval widths by $<$1pp.
15	GEE models use exchangeable working correlation with sandwich standard errors (robust to correlation misspecification), justified by near-zero estimated within-pair correlations ($\hat{\alpha} \in [-0.25, +0.11]$; Appendix~\ref{app:gee_diagnostics}).
16	A prospective power analysis (Appendix~\ref{app:power_analysis}) confirms that our sample sizes ($n = 86$--$88$ pairs) provide $>$90\% power to detect BT effects of the observed magnitude ($P \geq 0.63$), whereas Likert requires $4$--$206\times$ the sample size for equivalent power (Figure~\ref{fig:power_curve}).
17	
18	\paragraph{Model selection.}
19	Target judges span four architectures from independent providers: GPT-4o (\texttt{2024-08-06}; OpenAI), Qwen3-32B-Instruct (Alibaba; also serving as rewriter), Llama-3.3-70B-Instruct (Meta), and Gemini-2.5-Flash (Google).
20	This 
…[truncated 924 chars]

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

_source line 1382 · 2026-05-25T21:28:46.306014+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1383 · 2026-05-25T21:28:46.406929+00:00_

1	\appendix
2	
3	\noindent\emph{Organization: design rationale (A$^*$), confound analysis (A--B), model diagnostics (C), independence tests (D), gate validation (E--F), equivalence testing (G), statistical details (H--K), sensitivity analyses (L--N), artifact controls (O), implementation (P), multiplicity (Q), cross-axis contamination (R), FK length-control (R$'$), human annotation agreement (S), cross-benchmark replication (T), Claude cross-benchmark (U), rewriting prompts (V), non-tie concordance (W).}
4	
5	\section{Design Rationale}
6	\label{app:design_rationale}
7	
8	Three variables govern the observed judge score $Y$: the style attribute $S$ (e.g., formality), the original content quality $Q$, and the judge's internal scoring function.
9	Both $S$ and $Q$ causally influence $Y$; the goal of CSD is to approximate the effect $S \to Y$ while blocking confounding through $Q$.
10	Style-controlled rewriting generates a text pair that differs along a single style axis, but any rewriting operation risks inadvertently altering content quality ($R \to Q$).
11	The NLI gate (\S\ref{sec:nli_gate}) blocks this path, yielding a controlled estimate of the $S \to Y$ effect.
12	Our approach provides interventional rather than formal causal evidence: we do not claim that the DAG in Figure~\ref{fig:dag} is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions from the potential outcomes framework.
13	``Controlled'' in this context refers to experimentally controlled rewriting conditions, not formal causal identification in the potential-outcomes sense.
14	Our identification rests on three operational assumptions: (i)~the NLI gate approximates content preservation, blocking the $R \to Q$ path; (ii)~position swapping controls for presentation-order effects; and (iii)~the style rewrite introduces no systematic differences beyond the target axis.
15	
16	\section{Direction Asymmetry and Quality Confounding}
17	\label{app:direction}
18	
19	The formality ax
…[truncated 5424 chars]

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

_source line 1384 · 2026-05-25T21:28:55.200867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "offset": "80",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
    "offset": "80",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 1385 · 2026-05-25T21:28:55.251716+00:00_

80	\caption{GEE Style $\times$ Originality interaction terms. None are significant ($p > 0.13$), confirming the additive model specification.}
81	\label{tab:gee-interaction}
82	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}llccc@{}}
83	\toprule
84	Judge & Axis & Interaction OR & 95\% CI & $p$ \\
85	\midrule
86	GPT-4o & Formality & 0.661 & [0.18, 2.38] & .527 \\
87	GPT-4o & Verbosity & 1.269 & [0.37, 4.34] & .705 \\
88	GPT-4o & Register & 2.601 & [0.74, 9.15] & .136 \\
89	Qwen3-32B & Formality & 0.518 & [0.14, 1.89] & .320 \\
90	Qwen3-32B & Verbosity & 0.450 & [0.13, 1.62] & .221 \\
91	Qwen3-32B & Register & 0.555 & [0.15, 2.08] & .383 \\
92	Llama-70B & Formality & 0.968 & [0.25, 3.78] & .963 \\
93	Llama-70B & Verbosity & 1.103 & [0.34, 3.58] & .870 \\
94	\bottomrule
95	\end{tabular}}
96	\end{table}
97	
98	\paragraph{95\% confidence intervals.}
99	Table~\ref{tab:gee_ci} reports 95\% CIs for all GEE odds ratios in Table~\ref{tab:gee}.
100	
101	\begin{table}[h]
102	\centering
103	\small
104	\caption{95\% CIs for GEE conditional decomposition (Table~\ref{tab:gee}).}
105	\label{tab:gee_ci}
106	\begin{tabular}{@{}lcc@{}}
107	\toprule
108	Config & Style OR [CI] & Orig OR [CI] \\
109	\midrule
110	Qwen3 verb.\ & 13.10 [5.62, 30.55] & 0.49 [0.21, 1.14] \\
111	GPT-4o verb.\ & 11.34 [4.93, 26.10] & 0.45 [0.20, 1.04] \\
112	Llama-70B verb.\ & 8.21 [3.62, 18.65] & 0.38 [0.17, 0.86] \\
113	Gemini verb.\ & 8.98 [3.68, 21.94] & 0.46 [0.20, 1.04] \\
114	GPT-4o form.\ & 2.58 [1.41, 4.73] & 2.32 [1.27, 4.26] \\
115	Qwen3 form.\ & 4.20 [1.99, 8.87] & 4.70 [2.22, 9.96] \\
116	Qwen3 form.$^a$ & 2.15 [1.46, 3.16] & 4.99 [3.40, 7.34] \\
117	Llama-70B form.\ & 4.81 [2.48, 9.33] & 3.12 [1.61, 6.04] \\
118	Gemini form.\ & 1.64 [0.91, 2.98] & 2.51 [1.39, 4.54] \\
119	GPT-4o reg.\ & 1.88 [1.08, 3.28] & 2.21 [1.26, 3.86] \\
120	Qwen3 reg.\ & 1.91 [1.01, 3.58] & 5.72 [3.02, 10.82] \\
121	Llama-70B reg.\ & 3.33 [1.73, 6.42] & 3.07 [1.60, 5.92] \\
122	\bottomrule
123	\multicolumn{3}{l}{\footnotesiz
…[truncated 3634 chars]

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

_source line 1386 · 2026-05-25T21:29:02.286962+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "offset": "200",
  "limit": "150"
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
    "offset": "200",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1387 · 2026-05-25T21:29:02.337778+00:00_

200	.75 & .657 & .623 & .773 & .760 \\
201	.80 & .657 & .623 & .773 & .760 \\
202	.85 & .657 & .623 & .773 & .760 \\
203	.90 & .665 & .630 & .773 & .760 \\
204	.95 & .653 & .629 & .765 & .752 \\
205	.98 & .649 & .642 & .771 & .769 \\
206	\bottomrule
207	\end{tabular}
208	\end{table}
209	
210	\section{Direction-Aware Gate Validation}
211	\label{app:gate_validation}
212	
213	For verbosity, the direction-aware NLI gate admits 21 additional pairs (32\%) compared to strict bidirectional verification.
214	The two groups show no significant difference in BT win probability (78.5\% bidirectional vs.\ 73.8\% DA-only; permutation $p = .663$; $\Delta = {-}1.1$pp, 95\% CI $[{-}5.6, {+}3.0]$) or Likert $d$ ($0.038$ vs.\ $0.029$).
215	Both groups exhibit the Blindspot pattern (BT significant, Likert NS), confirming that direction-aware gating recovers valid pairs without inflating the effect or introducing selection bias.
216	Cross-judge validation on all 21 direction-aware pairs confirms this: Fisher exact tests comparing BT estimates between direction-aware and bidirectional-pass subsets are non-significant for all five judges ($p > 0.66$), indicating that the DA-gate does not differentially affect any judge's preference signal.
217	For formality, strict bidirectional verification is appropriate: a relaxed (direction-aware) gate would admit 9 additional pairs with reversed preference (BT 33.4\%), indicating content preservation failure rather than genuine style preference.
218	This asymmetry empirically justifies the axis-dependent gating strategy described in Section~\ref{sec:nli_gate}.
219	
220	\section{Claude Sonnet 4 Equivalence Testing}
221	\label{app:claude_tost}
222	
223	Claude Sonnet~4 exhibits benchmark-dependent sensitivity ($n = 88$; LLMBar BT 56.2\%/54.1\%, $p = 0.091$/$0.284$).
224	Formal equivalence testing \citep[TOST;][]{lakens2017equivalence} yields margin-dependent conclusions (Table~\ref{tab:tost_sensitivity}): per-axis equivalence is confirmed at $\Delta = 1
…[truncated 7145 chars]

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

_source line 1388 · 2026-05-25T21:29:08.440976+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "regularization|alpha.*10",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "regularization|alpha.*10",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1389 · 2026-05-25T21:29:08.971271+00:00_

555:Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm} using the \texttt{choix} Python library (default L2 regularization $\alpha = 10^{-6}$); varying $\alpha$ from $10^{-6}$ to $1.0$ changes all BT probabilities by ${<}0.002$.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 530
}
```

</details>

---


### Tool call

_source line 1390 · 2026-05-25T21:29:09.738532+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "same.style|double.rewrite|artifact",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "same.style|double.rewrite|artifact",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-C": "3"
  }
}
```

</details>

---


### Tool result

_source line 1391 · 2026-05-25T21:29:09.839205+00:00_

1-\appendix
2-
3:\noindent\emph{Organization: design rationale (A$^*$), confound analysis (A--B), model diagnostics (C), independence tests (D), gate validation (E--F), equivalence testing (G), statistical details (H--K), sensitivity analyses (L--N), artifact controls (O), implementation (P), multiplicity (Q), cross-axis contamination (R), FK length-control (R$'$), human annotation agreement (S), cross-benchmark replication (T), Claude cross-benchmark (U), rewriting prompts (V), non-tie concordance (W).}
4-
5-\section{Design Rationale}
6-\label{app:design_rationale}
--
277-
278-To assess robustness to originality confounding, we restrict to pairs where the judge assigned equal Likert scores to original and counterfactual texts (eliminating detectable quality differences).
279-Style preference persists: formality BT $= 67.3\%$ ($n = 55$, $\Delta = {+}0.8$pp from full sample, 95\% CI $[{-}11.0, {+}12.6]$); verbosity BT $= 76.0\%$ ($n = 50$, $\Delta = {-}1.3$pp, 95\% CI $[{-}13.3, {+}10.3]$).
280:In the anti-originality subset (pairs where the original never wins), effects strengthen (formality $75.0\%$, verbosity $86.1\%$), confirming that style preference is not an artifact of originality confounding.
281-
282-\section{Bradley-Terry Confidence Intervals}
283-\label{app:bt_ci}
--
513-\end{table}
514-
515-\section{Rewriting Artifact Control}
516:\label{app:artifact_control}
517-
518:Same-style double-rewrite (DR) controls quantify the rewriting artifact using BT models (consistent with all other pairwise analyses).
519:Table~\ref{tab:artifact} reports BT $P(\text{original})$, the probability the judge prefers the original over its same-style DR.
520:Both judges systematically prefer LLM-polished text across axes; for verbosity, BT $P(\text{original}) < 0.17$ indicates that rewriting quality dominates when content is held constant, validating the GEE decomposition that separates style from artifact effects.
521:Same-style double-rewrite controls for style-neutral polish
…[truncated 2175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1392 · 2026-05-25T21:29:17.878139+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
  "offset": "523",
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
    "offset": "523",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 1393 · 2026-05-25T21:29:17.978990+00:00_

523	\begin{table}[h]
524	\centering
525	\small
526	\caption{Rewriting artifact: BT $P(\text{orig})$ vs.\ same-style double-rewrite (bootstrap 95\% CI, 10{,}000 resamples). Values ${<}0.5$: judges prefer LLM-polished text.}
527	\label{tab:artifact}
528	\begin{tabular}{@{}llcc@{}}
529	\toprule
530	Axis & Judge & BT $P(\text{orig})$ [CI] & $p$ \\
531	\midrule
532	Form.\ & GPT-4o & .418 [.342, .500] & .037 \\
533	 & Qwen3 & .377 [.303, .451] & .0006 \\
534	\midrule
535	Verb.\ & GPT-4o & .167 [.084, .262] & ${<}.0001$ \\
536	 & Qwen3 & .082 [.035, .140] & ${<}.0001$ \\
537	\bottomrule
538	\end{tabular}
539	\end{table}
540	
541	\section{Implementation Details}
542	\label{app:implementation}
543	
544	\paragraph{Models and APIs.}
545	Style-controlled rewriting uses Qwen3-32B (temperature $0.7$, top-$p$ $0.9$).
546	Target judges: GPT-4o (\texttt{gpt-4o-2024-08-06}, accessed April--May 2026), Qwen3-32B (locally hosted), Llama-3.3-70B (locally hosted via vLLM).
547	Claude Sonnet 4 (\texttt{claude-sonnet-4-20250514}, accessed May 2026) provides discriminative validity evidence with benchmark-dependent sensitivity.
548	All judge calls use temperature $0$ and $\texttt{max\_tokens} = 2048$.
549	
550	\paragraph{NLI gate.}
551	Content preservation is verified using DeBERTa-v3-large \citep{he2021debertav3} fine-tuned on MNLI, with entailment threshold $\tau = 0.90$.
552	Bidirectional entailment is applied for formality and register; direction-aware entailment for verbosity (Section~\ref{sec:nli_gate}).

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

_source line 1394 · 2026-05-25T21:31:50.432557+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 审稿意见\n\n---\n\n### Strengths 回应\n\nR1 的 S1-S6 与我的评估高度一致。特别是 S2（robustness 检查覆盖面）和 S4（因果语言的审慎使用）是我也重点肯定的方面。我在 S6（人类标注验证）的基础上额外注意到标注者仅判定 49-66% 的 NLI-passed pairs 有可检测的风格变化（§5.4），这意味着观察到的效应是真实敏感性的稀释下界——R1 没有提及这一点，但我认为它增强了论文的可信度。\n\n---\n\n### Must-Fix 回应\n\n**[AGREE] R1-N1: Power analysis 的 \"prospective\" 标签存在循环论证风险**\n\n同意 R1 的核心判断。§4.1 称 \"A prospective power analysis (Appendix L) confirms that our sample sizes (n = 86–88 pairs) provide >90% power to detect BT effects of the observed magnitude (P ≥ 0.63)\"——使用同一数据集的 observed effect size 计算 power，这正是 Hoenig & Heisey (2001) 所批评的 post-hoc power fallacy。论文在 Figure 4 caption 中加了括号 disclaimer \"(not post-hoc power; cf. Hoenig & Heisey, 2001)\"，但用法与该引用的核心论点矛盾。\n\n补充：论文的实质分析（\"Likert 需要 4-206× 的样本量才能达到同等 power\"）作为 sensitivity analysis 仍有信息价值，但 \"prospective\" 标签不当。R1 建议改为 \"sensitivity power analysis\" 是准确的修改方向。Figure 4 的 y 轴标签 \"at observed effect magnitudes\" 进一步固化了 post-hoc 印象（与 R1-M4 一致）。\n\n**[AGREE] R1-N2: 跨基准复制的选择性构成确认偏差**\n\n强烈同意，这也是我的 W2。仅测试 24 cells 中效应最强的 6 个（25%），且论文明确称 \"targeting the strongest effects\"（§5.3 最后一段）。虽然透明度值得肯定，但策略本身是 cherry-picking 的一种形式。更关键的是：4 个 exception cells (‡) 的存在表明 Blindspot 的可复制性是 effect-size dependent 的，但论文用 \"severity spectrum\" 来解释这些 exceptions，这更接近 post-hoc rationalization 而非预先注册的分析框架。\n\n我额外注意到 R1 未提及的一点：未测试的 18 cells 可能包含反例（Likert 检测到而 pairwise 未检测到的情况），这将直接挑战 \"Likert Blindspot\" 的单向性叙事。R1 的 Q2（要求报告 18 cells 结果）因此尤为重要。\n\n---\n\n### Should-Fix 回应\n\n**[AGREE] R1-W1: GEE OR shrinkage 讨论不足**\n\n同意。Table 2 全部基于 n=88，而 n=355 的 scaled replication 显示 49-72% shrinkage（§5.2: Qwen3-32B formality Style OR 4.20 → 2.15）。虽然 Table 2 caption 提到了 shrinkage 范围，且 Appendix 有 n=355 数据，但主表的视觉印象仍以膨胀的 n=88 估计为主。R1 建议并列报告 n=88 和 n=355 估计（Q5）是合理的。\n\n补充：shrinkage 后 n=355 的 Style OR 仍显著（GPT-4o: 2.58, p=.002; Qwen3-32B: 2.15, p<.0001），说明核心结论不变，但 effect magnitude 的报告确实需要校正。\n\n**[AGREE] R1-W2: Evaluator-producer overlap 残留 22% 膨胀**\n\n同意，这也是我的 W1。Appendix E（Table 5-6）显示 GPT-4o 独立 rewriter 使 Style OR 从 13.10 降至 10.17（-22%），Blindspot 仍然存在但 effect size 缩减是 non-trivial 的。论文仅在 Table 1 脚注 b 中提及 \"independent GPT-4o rewriter yields 22% lower Style OR\"，正文 §5.4 未显著讨论。\n\n**[AGREE] R1-W3: TOST 等价界 Δ=12pp 偏宽松——我的审稿遗漏了这一问题**\n\n这是 R1 提出的、我完全遗漏的一个尖锐观察。Appendix H（Table 9）显示 Claude pooled TOST 在 Δ=12pp 时 p=.035，在 Δ=10pp 时 p=.100（不显著）。而 Blindspot 效应本身对最弱的 target judge（GPT-4o formality BT=63.0%）仅为 13pp。这意味着 TOST 的等价界几乎与最小的正效应重合——TOST 无法区分 \"Claude 真的无偏\" 和 \"Claude 的偏差略低于检测阈值\"。论文称 \"Δ=12pp corresponds to a small effect (Cohen's h=0.24)\"（Appendix H），但 Cohen's h 的解释在 BT probability 空间中的 substantive 含义未被讨论。\n\n建议作者：(1) 报告多个 Δ 的 TOST 结果（已做到，Table 9）；(2) 在正文中明确承认 Δ=12pp bound 的局限性，而不仅是在 appendix 中。\n\n**[AGREE] R1-W4: §3.1 \"per-axis causal attribution\" 与 Appendix A disclaimer 的语调不一致**\n\n同意。Appendix A 明确声明 \"Our approach provides interventional rather than formal causal evidence: we do not claim that the DAG in Figure 2 is a complete structural causal model\"（Appendix A, line 12），但 §3.1 的正文描述（\"a single-axis intervention design that enables per-axis causal attribution\"）使用了更强的因果语言。这种前后不一致会让 reviewer 质疑论文的 claim 边界。\n\n**[AGREE] R1-W5: Verbosity same-style double-rewrite 暴露严重 rewriting artifact——我的审稿遗漏了这一问题**\n\nR1 指出 BT P(orig)=0.082（Qwen3 verbosity，Table 19, Appendix O），意味着 judge 在 91.8% 的情况下偏好 LLM-polished 版本，即使风格没有改变。这是一个非常严重的 confound。论文声称这被 GEE 的 Originality term 吸收（§5.4: \"Same-style double-rewrite controls confirm that any residual rewriting artifact is absorbed by the GEE originality term\"），但 GEE verbosity 的 Orig OR=0.49 (n.s.) 表明吸收可能不完全——Orig OR 虽然不显著，但方向（<1，偏好 rewrite）与 same-style artifact 一致。\n\nR1 的 Q3（artifact 在 GEE Orig OR 中被吸收多少）是关键问题。如果 same-style rewrite artifact 的幅度（BT P=0.082，即强烈偏好 rewrite）远大于 GEE 能吸收的量，那么 verbosity 的 Style OR=13.10 可能仍包含未被控制的 polishing artifact。\n\n---\n\n### Minor 回应\n\n**[REBUT] R1-M1: BT 正则化参数不一致（§4.1 α=10⁻⁴ vs Appendix R α=10⁻⁷）**\n\n经核查 LaTeX 源码，§4.1（experiments.tex line 12）写的是 $\\alpha = 10^{-6}$，Appendix P Implementation Details（appendix.tex line 555）同样写的是 \"default L2 regularization α = 10⁻⁶; varying α from 10⁻⁶ to 1.0 changes all BT probabilities by <0.002\"。两处均为 10⁻⁶，不存在 R1 所述的 10⁻⁴ 与 10⁻⁷ 的不一致。R1 可能因 PDF 渲染中上标数字辨识困难而误读。此外，论文报告了 α 从 10⁻⁶ 到 1.0 的 sensitivity analysis（BT 变化 <0.002），说明正则化选择对结果无实质影响。\n\n**[AGREE] R1-M2: GEE ρ=−0.25 不是 \"near-zero\"**\n\n同意。§4.1 称 \"near-zero estimated within-pair correlations (α̂ ∈ [−0.25, +0.11])\"，但 ρ=−0.25 不符合 \"near-zero\" 的通常标准（通常 |ρ| < 0.1）。不过，Table 3（Appendix C）的 correlation structure robustness test 显示 exchangeable 与 independence 结构的 ΔQIC < 0.001，max coefficient change < 0.02，说明即使 ρ 不是 near-zero，结论对 correlation structure 的选择是 robust 的。建议将 \"near-zero\" 改为更准确的描述如 \"small in magnitude\"。\n\n**[REBUT] R1-M3: Table 1 adjusted p-values 校正方法未说明**\n\n§4.1 第1句明确写道 \"The primary family comprises six tests (three target judges × two axes), corrected via Holm-Bonferroni at α = 0.05\"（experiments.tex line 8），Table 1 脚注也标注 \"Holm-adj. for primary\"。校正方法已说明。但我同意 R1 的隐含关切：Table 1 未直接呈现 raw 和 adjusted p-values 的对照，尽管 §4.1 声称 \"Table 1 reports both raw and adjusted p-values\"。实际上 Table 1 的 BT 列只显示 significance markers (***、*)，Likert 列显示 d(p) 中的 raw p-value。adjusted p-values 的具体数值不可见。\n\n**[AGREE] R1-M4: Figure 4 y 轴 \"at observed effect magnitudes\" 强化 post-hoc 印象**\n\n同意，与 N1 一致。\n\n---\n\n### Questions 回应\n\n**R1-Q1 (Power analysis effect size 有 pilot/先验来源？)**：关键问题。如果没有独立先验，\"prospective\" 标签不成立。论文应在 revision 中明确说明。\n\n**R1-Q2 (未测试的 18 cells 有结果？)**：我认为这是最重要的问题。如果 18 cells 中有反例（Likert 检测到但 pairwise 未检测到），\"Blindspot\" 的单向性叙事将被严重削弱。\n\n**R1-Q3 (Verbosity same-style artifact 被 GEE Orig OR 吸收多少？)**：如上述 W5 分析，这是一个需要定量回答的核心问题。建议作者提供 same-style BT artifact 与 GEE Orig OR 的直接比较。\n\n**R1-Q4 (BT 正则化参数？)**：如 M1 回应所述，两处均为 10⁻⁶，不存在不一致。\n\n**R1-Q5 (n=355 GEE 估计并列报告？)**：支持。Table 2 应并列报告 n=88 和 n=355 估计以避免小样本膨胀的误导。\n\n---\n\n### 评分差异分析\n\nR1 和我的评分高度一致（Soundness 3.5, Overall 3.5），唯一显著差异在 **Excitement**（R1: 3.5, 我: 3.0）。\n\n我给 Excitement 3.0 的主要原因是：Pairwise vs. Likert discriminability 差异是自 Thurstone (1927) 以来的已知心理测量效应，本文的 domain transfer 到 LLM judge 虽然有实践价值，但概念新颖性有限。R1 未在其审稿中明确讨论这一心理测量学先驱问题，这可能是评分差异的来源。\n\n此外，我提出了两个 R1 未涉及的 Must-Fix 问题：\n1. **标题/framing 张力**（我的 N1）：\"The Likert Blindspot\" 预设了 Likert attenuation 解释，与正文三种非排他解释存在矛盾。R1 未将此标记为问题。\n2. **Novelty 定位不清晰**（我的 N2）：贡献声明 \"the first per-axis demonstration\" 的 \"first\" 在心理测量学背景下被过度强调。\n\n建议 Director 关注这两个额外的 framing/novelty 问题——它们可能在 AC 层面影响接收决定，即使技术执行扎实。\n\n---\n\n### 我遗漏的问题（感谢 R1 发现）\n\n1. **W3 (TOST Δ=12pp)**：R1 指出 TOST bound 几乎与最小正效应重合，这使 Claude discriminative validity 的说服力大打折扣。我在初审中完全遗漏了这一点。\n2. **W5 (Verbosity same-style artifact BT P(orig)=0.082)**：91.8% 的 rewrite 偏好是一个定量上非常严重的 confound。我在初审中提到了 rewriter-judge overlap 但未检查 same-style artifact 的具体幅度。\n3. **M2 (ρ=-0.25 不是 near-zero)**：有效的文本准确性问题，我遗漏了。\n",
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
    "text": "\n## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 审稿意见\n\n---\n\n### Strengths 回应\n\nR1 的 S1-S6 与我的评估高度一致。特别是 S2（robustness 检查覆盖面）和 S4（因果语言的审慎使用）是我也重点肯定的方面。我在 S6（人类标注验证）的基础上额外注意到标注者仅判定 49-66% 的 NLI-passed pairs 有可检测的风格变化（§5.4），这意味着观察到的效应是真实敏感性的稀释下界——R1 没有提及这一点，但我认为它增强了论文的可信度。\n\n---\n\n### Must-Fix 回应\n\n**[AGREE] R1-N1: Power analysis 的 \"prospective\" 标签存在循环论证风险**\n\n同意 R1 的核心判断。§4.1 称 \"A prospective power analysis (Appendix L) confirms that our sample sizes (n = 86–88 pairs) provide >90% power to detect BT effects of the observed magnitude (P ≥ 0.63)\"——使用同一数据集的 observed effect size 计算 power，这正是 Hoenig & Heisey (2001) 所批评的 post-hoc power fallacy。论文在 Figure 4 caption 中加了括号 disclaimer \"(not post-hoc power; cf. Hoenig & Heisey, 2001)\"，但用法与该引用的核心论点矛盾。\n\n补充：论文的实质分析（\"Likert 需要 4-206× 的样本量才能达到同等 power\"）作为 sensitivity analysis 仍有信息价值，但 \"prospective\" 标签不当。R1 建议改为 \"sensitivity power analysis\" 是准确的修改方向。Figure 4 的 y 轴标签 \"at observed effect magnitudes\" 进一步固化了 post-hoc 印象（与 R1-M4 一致）。\n\n**[AGREE] R1-N2: 跨基准复制的选择性构成确认偏差**\n\n强烈同意，这也是我的 W2。仅测试 24 cells 中效应最强的 6 个（25%），且论文明确称 \"targeting the strongest effects\"（§5.3 最后一段）。虽然透明度值得肯定，但策略本身是 cherry-picking 的一种形式。更关键的是：4 个 exception cells (‡) 的存在表明 Blindspot 的可复制性是 effect-size dependent 的，但论文用 \"severity spectrum\" 来解释这些 exceptions，这更接近 post-hoc rationalization 而非预先注册的分析框架。\n\n我额外注意到 R1 未提及的一点：未测试的 18 cells 可能包含反例（Likert 检测到而 pairwise 未检测到的情况），这将直接挑战 \"Likert Blindspot\" 的单向性叙事。R1 的 Q2（要求报告 18 cells 结果）因此尤为重要。\n\n---\n\n### Should-Fix 回应\n\n**[AGREE] R1-W1: GEE OR shrinkage 讨论不足**\n\n同意。Table 2 全部基于 n=88，而 n=355 的 scaled replication 显示 49-72% shrinkage（§5.2: Qwen3-32B formality Style OR 4.20 → 2.15）。虽然 Table 2 caption 提到了 shrinkage 范围，且 Appendix 有 n=355 数据，但主表的视觉印象仍以膨胀的 n=88 估计为主。R1 建议并列报告 n=88 和 n=355 估计（Q5）是合理的。\n\n补充：shrinkage 后 n=355 的 Style OR 仍显著（GPT-4o: 2.58, p=.002; Qwen3-32B: 2.15, p<.0001），说明核心结论不变，但 effect magnitude 的报告确实需要校正。\n\n**[AGREE] R1-W2: Evaluator-producer overlap 残留 22% 膨胀**\n\n同意，这也是我的 W1。Appendix E（Table 5-6）显示 GPT-4o 独立 rewriter 使 Style OR 从 13.10 降至 10.17（-22%），Blindspot 仍然存在但 effect size 缩减是 non-trivial 的。论文仅在 Table 1 脚注 b 中提及 \"independent GPT-4o rewriter yields 22% lower Style OR\"，正文 §5.4 未显著讨论。\n\n**[AGREE] R1-W3: TOST 等价界 Δ=12pp 偏宽松——我的审稿遗漏了这一问题**\n\n这是 R1 提出的、我完全遗漏的一个尖锐观察。Appendix H（Table 9）显示 Claude pooled TOST 在 Δ=12pp 时 p=.035，在 Δ=10pp 时 p=.100（不显著）。而 Blindspot 效应本身对最弱的 target judge（GPT-4o formality BT=63.0%）仅为 13pp。这意味着 TOST 的等价界几乎与最小的正效应重合——TOST 无法区分 \"Claude 真的无偏\" 和 \"Claude 的偏差略低于检测阈值\"。论文称 \"Δ=12pp corresponds to a small effect (Cohen's h=0.24)\"（Appendix H），但 Cohen's h 的解释在 BT probability 空间中的 substantive 含义未被讨论。\n\n建议作者：(1) 报告多个 Δ 的 TOST 结果（已做到，Table 9）；(2) 在正文中明确承认 Δ=12pp bound 的局限性，而不仅是在 appendix 中。\n\n**[AGREE] R1-W4: §3.1 \"per-axis causal attribution\" 与 Appendix A disclaimer 的语调不一致**\n\n同意。Appendix A 明确声明 \"Our approach provides interventional rather than formal causal evidence: we do not claim that the DAG in Figure 2 is a complete structural causal model\"（Appendix A, line 12），但 §3.1 的正文描述（\"a single-axis intervention design that enables per-axis causal attribution\"）使用了更强的因果语言。这种前后不一致会让 reviewer 质疑论文的 claim 边界。\n\n**[AGREE] R1-W5: Verbosity same-style double-rewrite 暴露严重 rewriting artifact——我的审稿遗漏了这一问题**\n\nR1 指出 BT P(orig)=0.082（Qwen3 verbosity，Table 19, Appendix O），意味着 judge 在 91.8% 的情况下偏好 LLM-polished 版本，即使风格没有改变。这是一个非常严重的 confound。论文声称这被 GEE 的 Originality term 吸收（§5.4: \"Same-style double-rewrite controls confirm that any residual rewriting artifact is absorbed by the GEE originality term\"），但 GEE verbosity 的 Orig OR=0.49 (n.s.) 表明吸收可能不完全——Orig OR 虽然不显著，但方向（<1，偏好 rewrite）与 same-style artifact 一致。\n\nR1 的 Q3（artifact 在 GEE Orig OR 中被吸收多少）是关键问题。如果 same-style rewrite artifact 的幅度（BT P=0.082，即强烈偏好 rewrite）远大于 GEE 能吸收的量，那么 verbosity 的 Style OR=13.10 可能仍包含未被控制的 polishing artifact。\n\n---\n\n### Minor 回应\n\n**[REBUT] R1-M1: BT 正则化参数不一致（§4.1 α=10⁻⁴ vs Appendix R α=10⁻⁷）**\n\n经核查 LaTeX 源码，§4.1（experiments.tex line 12）写的是 $\\alpha = 10^{-6}$，Appendix P Implementation Details（appendix.tex line 555）同样写的是 \"default L2 regularization α = 10⁻⁶; varying α from 10⁻⁶ to 1.0 changes all BT probabilities by <0.002\"。两处均为 10⁻⁶，不存在 R1 所述的 10⁻⁴ 与 10⁻⁷ 的不一致。R1 可能因 PDF 渲染中上标数字辨识困难而误读。此外，论文报告了 α 从 10⁻⁶ 到 1.0 的 sensitivity analysis（BT 变化 <0.002），说明正则化选择对结果无实质影响。\n\n**[AGREE] R1-M2: GEE ρ=−0.25 不是 \"near-zero\"**\n\n同意。§4.1 称 \"near-zero estimated within-pair correlations (α̂ ∈ [−0.25, +0.11])\"，但 ρ=−0.25 不符合 \"near-zero\" 的通常标准（通常 |ρ| < 0.1）。不过，Table 3（Appendix C）的 correlation structure robustness test 显示 exchangeable 与 independence 结构的 ΔQIC < 0.001，max coefficient change < 0.02，说明即使 ρ 不是 near-zero，结论对 correlation structure 的选择是 robust 的。建议将 \"near-zero\" 改为更准确的描述如 \"small in magnitude\"。\n\n**[REBUT] R1-M3: Table 1 adjusted p-values 校正方法未说明**\n\n§4.1 第1句明确写道 \"The primary family comprises six tests (three target judges × two axes), corrected via Holm-Bonferroni at α = 0.05\"（experiments.tex line 8），Table 1 脚注也标注 \"Holm-adj. for primary\"。校正方法已说明。但我同意 R1 的隐含关切：Table 1 未直接呈现 raw 和 adjusted p-values 的对照，尽管 §4.1 声称 \"Table 1 reports both raw and adjusted p-values\"。实际上 Table 1 的 BT 列只显示 significance markers (***、*)，Likert 列显示 d(p) 中的 raw p-value。adjusted p-values 的具体数值不可见。\n\n**[AGREE] R1-M4: Figure 4 y 轴 \"at observed effect magnitudes\" 强化 post-hoc 印象**\n\n同意，与 N1 一致。\n\n---\n\n### Questions 回应\n\n**R1-Q1 (Power analysis effect size 有 pilot/先验来源？)**：关键问题。如果没有独立先验，\"prospective\" 标签不成立。论文应在 revision 中明确说明。\n\n**R1-Q2 (未测试的 18 cells 有结果？)**：我认为这是最重要的问题。如果 18 cells 中有反例（Likert 检测到但 pairwise 未检测到），\"Blindspot\" 的单向性叙事将被严重削弱。\n\n**R1-Q3 (Verbosity same-style artifact 被 GEE Orig OR 吸收多少？)**：如上述 W5 分析，这是一个需要定量回答的核心问题。建议作者提供 same-style BT artifact 与 GEE Orig OR 的直接比较。\n\n**R1-Q4 (BT 正则化参数？)**：如 M1 回应所述，两处均为 10⁻⁶，不存在不一致。\n\n**R1-Q5 (n=355 GEE 估计并列报告？)**：支持。Table 2 应并列报告 n=88 和 n=355 估计以避免小样本膨胀的误导。\n\n---\n\n### 评分差异分析\n\nR1 和我的评分高度一致（Soundness 3.5, Overall 3.5），唯一显著差异在 **Excitement**（R1: 3.5, 我: 3.0）。\n\n我给 Excitement 3.0 的主要原因是：Pairwise vs. Likert discriminability 差异是自 Thurstone (1927) 以来的已知心理测量效应，本文的 domain transfer 到 LLM judge 虽然有实践价值，但概念新颖性有限。R1 未在其审稿中明确讨论这一心理测量学先驱问题，这可能是评分差异的来源。\n\n此外，我提出了两个 R1 未涉及的 Must-Fix 问题：\n1. **标题/framing 张力**（我的 N1）：\"The Likert Blindspot\" 预设了 Likert attenuation 解释，与正文三种非排他解释存在矛盾。R1 未将此标记为问题。\n2. **Novelty 定位不清晰**（我的 N2）：贡献声明 \"the first per-axis demonstration\" 的 \"first\" 在心理测量学背景下被过度强调。\n\n建议 Director 关注这两个额外的 framing/novelty 问题——它们可能在 AC 层面影响接收决定，即使技术执行扎实。\n\n---\n\n### 我遗漏的问题（感谢 R1 发现）\n\n1. **W3 (TOST Δ=12pp)**：R1 指出 TOST bound 几乎与最小正效应重合，这使 Claude discriminative validity 的说服力大打折扣。我在初审中完全遗漏了这一点。\n2. **W5 (Verbosity same-style artifact BT P(orig)=0.082)**：91.8% 的 rewrite 偏好是一个定量上非常严重的 confound。我在初审中提到了 rewriter-judge overlap 但未检查 same-style artifact 的具体幅度。\n3. **M2 (ρ=-0.25 不是 near-zero)**：有效的文本准确性问题，我遗漏了。\n",
    "reviewer_id": "2",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 1395 · 2026-05-25T21:31:54.052302+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3619
}
```

</details>

---


### Assistant

_source line 1396 · 2026-05-25T21:32:03.787228+00:00_

交叉回应已提交。

总结：与 R1 在 12/16 个具体问题上达成一致（10 个 AGREE，2 个 REBUT）。REBUT 的两点是：(1) M1 的 BT 正则化参数不一致——经核查 LaTeX 源码两处均为 10⁻⁶，R1 可能误读 PDF；(2) M3 的校正方法确实已在 §4.1 和 Table 1 脚注中说明。R1 提出了三个我初审遗漏的问题（TOST Δ=12pp 过宽、verbosity same-style artifact BT P(orig)=0.082、GEE ρ=-0.25 非 near-zero），均已确认并纳入。我提出了两个 R1 未涉及的额外问题：标题/framing 张力和 Thurstone 以来的 novelty 定位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_2"
}
```

</details>

---
