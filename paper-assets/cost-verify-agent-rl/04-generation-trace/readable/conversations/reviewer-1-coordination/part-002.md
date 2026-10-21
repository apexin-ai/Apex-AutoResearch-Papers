# Reviewer 1 coordination — Part 2 of 2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-1-coordination.md) · [Structured JSON](../../../sessions/c3/c348c62bf1466d045bd6.json)

## Round 18

### User

_source line 461 · 2026-05-25T21:15:43.788008+00:00_

[Round 1 审稿请求]:
你是 EMNLP 2026 审稿圆桌的 Reviewer 1。请严格、客观地审稿。

## 论文信息
- **标题**: "Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction"
- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/submitted.pdf`
- **目标 venue**: EMNLP 2026 (via ARR May 2026 cycle)

## Venue 格式要求
- 正文 8 页限制（严格），参考文献不限
- Limitations 段必须在正文中，不算页数
- ACL 模板，double-blind 审稿
- Long/Short 走同一审稿系统
- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 你的审查侧重
**方法严谨性 + 理论分析 + 实验设计**

重点审查：
1. **理论分析**: Proposition 1 和 Proposition 2 的推导是否严谨？假设是否合理？Binary reward 理论与 ternary reward 实验之间的桥接是否充分？
2. **实验设计**: Partial factorial design 是否合理？Cell C 缺失对因果推断的影响？2 seeds per condition 的统计效力？11-seed episode-level 评估的分类标准？
3. **因果推断**: A→B→D 比较链是否足以支撑 dual mechanism 论断？每一步比较是否有混淆因素？
4. **数据完整性**: Table 1/2 数据报告标准是否一致？评估方法（RAGEN built-in vs D134 protocol）差异？
5. **统计检验**: Fisher exact test 用法、Wilson CI、Cohen's h 等是否恰当？

请输出标准审稿格式：
- Summary (2-3 句)
- Strengths (逐条，标 S1/S2/...)
- Weaknesses (逐条，标 W1/W2/...，区分 Must-Fix / Should-Fix / Minor，附严重性 Critical/Warning/Info)
- Questions (Q1/Q2/...)
- Missing References
- Overall Assessment (评分 + 置信度 + Excitement)
- Detailed Comments (逐节)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-25T21:15:50.735964+00:00_

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
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
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

_source line 463 · 2026-05-25T21:15:50.736376+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-25T21:15:54.219300+00:00_

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
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 465 · 2026-05-25T21:15:55.278843+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer form dimensions scoring rubric 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer form dimensions scoring rubric 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-25T21:15:57.438118+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/submitted.pdf",
  "project": "cost-verify-agent-rl",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/submitted.pdf",
    "project": "cost-verify-agent-rl",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-25T21:16:01.152654+00:00_

Web search results for query: "ACL Rolling Review reviewer form dimensions scoring rubric 2025 2026"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here's what I found about the ACL Rolling Review reviewer form dimensions and scoring rubric for 2025-2026:

## Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and o
…[truncated 1191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5873
}
```

</details>

---


### Tool result

_source line 468 · 2026-05-25T21:16:01.907905+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found comprehensive information about ACL ARR 2026 reviewer guidelines and review form criteria. Here's what I found:

## Review Form Criteria

For Findings papers, the main criteria are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

The review recommendation scores include:
- 5 = Consider for Award: papers that could be considere
…[truncated 1226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7688
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-25T21:16:03.615779+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 767.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 470.7}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 523.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 394.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 470.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 446.2}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 
…[truncated 460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6177
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-25T21:16:10.952243+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form fields, scoring dimensions, and rubrics. List every dimension name, its scale, and the description for each score level. Include soundness, excitement, overall assessment, confidence, and any other fields."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form fields, scoring dimensions, and rubrics. List every dimension name, its scale, and the description for each score level. Include soundness, excitement, overall assessment, confidence, and any other fields."
  }
}
```

</details>

---


### Tool call

_source line 471 · 2026-05-25T21:16:12.510533+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/submitted.pdf",
  "project": "cost-verify-agent-rl",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/submitted.pdf",
    "project": "cost-verify-agent-rl",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-25T21:16:13.515475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 473 · 2026-05-25T21:16:13.967433+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-25T21:16:14.471957+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 475 · 2026-05-25T21:16:14.924738+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 476 · 2026-05-25T21:16:24.844956+00:00_

# ACL Rolling Review Form - Complete Field Extract

## Core Review Sections

**Paper Summary**
Open-ended text field for describing paper topic and identifying misunderstandings.

**Summary of Strengths**
Open-ended text requesting reasons for publication at selective venues.

**Summary of Weaknesses**
Open-ended text requesting numbered concerns about the submission.

**Comments/Suggestions/Typos**
Open-ended text for improvement feedback.

## Scoring Dimensions

### Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct"
- **4**: "Quite sure" with unlikely but possible errors
- **3**: "Pretty sure" but chance of missed details
- **2**: "Willing to defend" but likely missed some content
- **1**: "Not my area" or incomprehensible work

### Soundness
Scale: 1-5 (with .5 increments)
- **5**: "Excellent" - most thorough for its type
- **4**: "Strong" - sufficient support with optional additions
- **3**: "Acceptable" - supports main claims with minor gaps
- **2**: "Poor" - insufficient support, major technical problems
- **1**: "Major Issues" - insufficiently thorough or irrelevant

### Excitement
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting" - would recommend widely
- **4**: "Exciting" - would mention to others
- **3**: "Interesting" - might mention selectively
- **2**: "Potentially Interesting" - personal disinterest only
- **1**: "Not Exciting" - no community resonance

### Overall Assessment
Scale: 1-5 (with .5 increments)
- **5**: Award consideration (top 2.5%)
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings track
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

## Additional Fields

**Best Paper Justification**
Required when scoring 5 or 4.5 on Overall Assessment.

**Limitations and Societal Impact**
Open-ended evaluation of adequacy.

**Ethical Concerns**
Open-ended assessment against ACL cod
…[truncated 611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 13892
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-25T21:16:26.004747+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.5}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.2}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 468.4}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 364.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 348.6}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 346.6}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 13494
}
```

</details>

---


### Tool result

_source line 478 · 2026-05-25T21:16:30.181980+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 16666
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-25T21:16:30.185131+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 15260
}
```

</details>

---


### Tool result

_source line 480 · 2026-05-25T21:16:30.237421+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 16269
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-25T21:16:30.238516+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 15766
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-25T21:16:35.375510+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 483 · 2026-05-25T21:16:35.927878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 484 · 2026-05-25T21:16:36.381234+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 485 · 2026-05-25T21:16:36.381683+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 486 · 2026-05-25T21:16:36.928239+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1000
}
```

</details>

---


### Tool call

_source line 487 · 2026-05-25T21:16:36.928684+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 488 · 2026-05-25T21:16:37.369648+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 987
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-25T21:16:37.773362+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 844
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-25T21:16:45.352336+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 491 · 2026-05-25T21:16:45.955968+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 492 · 2026-05-25T21:16:46.359548+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-25T21:16:46.367800+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 411
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-25T21:16:46.368367+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 495 · 2026-05-25T21:16:46.972205+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 496 · 2026-05-25T21:16:47.024075+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-25T21:16:47.577790+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-25T21:16:53.512804+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 499 · 2026-05-25T21:16:53.965758+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 500 · 2026-05-25T21:16:54.525465+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1012
}
```

</details>

---


### Tool call

_source line 501 · 2026-05-25T21:16:54.526001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 502 · 2026-05-25T21:16:54.981235+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1015
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-25T21:16:54.984019+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 458
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-25T21:16:54.984404+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-25T21:16:55.387163+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-25T21:22:23.839801+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-25T21:22:24.056786+00:00_

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
13	\usepackage{amssymb}
14	\usepackage{amsthm}
15	\usepackage{enumitem}
16	
17	\title{Sign Misattribution in Step-Independent Agent RL:\\Dual Mechanism Diagnosis and Episode-Level Correction}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	Reinforcement learning (RL) for multi-turn large language model (LLM) agents requires credit assignment across long interaction trajectories. The dominant training paradigm decomposes these trajectories into fixed-size windows optimized independently via Group Relative Policy Optimization (GRPO), yet this design choice has received little scrutiny. We identify a structural credit assignment pathology driven by two distinct mechanisms: \textit{policy information loss}, which truncates cross-window context and imposes a constant performance ceiling, and \textit{advantage sign misattribution}, which causes a substantial fraction of gradient updates for locally correct actions to carry incorrect sign. A partial factorial experiment isolates each mechanism: removing sign misattribution converts catastrophic collapse into bounded learning; additionally removing information loss enables out-of-distribution (OOD) generalization. Direct sign measurement confirms the theoretical prediction, with credit agreement dropping to near-random levels. Episode-level GRPO, which treats the full trajectory as a single optimization sample, structurally eliminates both failure modes but remains seed-dependent: 17.7\% mean OOD success versus 6.72\% SFT baseline, though only 36\% of seeds achieve significant generalization, indicating that avoiding collapse is necessary but not sufficient. Cross-scale verification at 8B parameters and cross-environment
…[truncated 1368 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 216
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-25T21:22:27.017299+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-25T21:22:27.068666+00:00_

1	\section{Theoretical Analysis}
2	\label{sec:theory}
3	
4	Sign misattribution is the more fundamental failure mechanism because it causes active divergence, not merely slow convergence. We derive the probability of incorrect gradient direction below; full proofs appear in Appendix~\ref{app:theory_full}.
5	
6	\textbf{Definition 1} (Locally correct action). \textit{An action $a_t$ is \textbf{locally correct} if it would receive positive advantage under an oracle that observes the full episode history $h_t$ and has access to the true action-value function. Equivalently,\footnote{This equivalence is approximate; it holds exactly when all trajectories within an episode are equally likely under the reference policy, and approximately under the mild assumption that policy drift remains small during early training. This approximation is most accurate when the policy has not yet diverged significantly from initialization (here, $p \approx 12.5\%$); at higher success rates, the bound may loosen.} window $w$ contains locally correct actions if replacing them (holding all other windows fixed) would decrease the probability of episode success.}
7	
8	\textbf{Proposition 1.} \textit{Under step-independent training with binary episode reward $R_{\text{episode}} \in \{0, r_+\}$, the probability that window $w$'s advantage $\hat{A}_w$ has the correct sign (aligned with local action quality) approaches the base success rate $p$ as the number of rollouts $K$ per group increases.}
9	
10	\textit{Proof sketch.} In a failed episode ($R_{\text{episode}} = 0$), all windows receive $R_w = 0$. If any rollout in the group succeeded, $\mu > 0$, so every window in the failed episode receives $\hat{A}_w < 0$, including windows with locally correct actions. The probability of receiving the wrong sign in a failed episode is $1 - (1-p)^{K-1}$ (at least one group member succeeded). As $K$ grows, this approaches $1-p$, and the overall probability of correct sign approaches $p$. \hfill$\square$
11	
12	
…[truncated 5230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-25T21:22:31.948664+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-25T21:22:31.999305+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation and GRPO}
5	\label{sec:problem_formulation}
6	
7	We model the multi-turn agent as a partially observable Markov decision process (POMDP)~\citep{kaelbling1998planning} where the policy $\pi_\phi(a_t \mid h_t)$ generates actions conditioned on interaction history $h_t = (o_1, a_1, \ldots, o_t)$. Episodes of $T$ steps terminate with binary reward $R \in \{0, r_+\}$ (our experiments use a penalty variant with $r_- = -0.1$ per invalid action; Section~\ref{sec:setup}). GRPO~\citep{shao2024deepseekmath} samples $K$ rollouts per task and computes group-relative advantages:
8	\begin{align}
9	\hat{A}_k &= \frac{R_k - \mu}{\sigma + \epsilon}, \notag \\
10	\mu &= \frac{1}{K}\sum_{j=1}^K R_j, \quad \sigma = \sqrt{\frac{1}{K}\sum_{j=1}^K (R_j - \mu)^2}
11	\label{eq:grpo_advantage}
12	\end{align}
13	GRPO is episode-level by design: each rollout receives one return and one advantage, with no inherent temporal discounting.
14	
15	\subsection{Step-Independent Windowing}
16	\label{sec:step_independent}
17	
18	Agent RL frameworks must reconcile GRPO's episode-level design with the memory constraints of long trajectories. RAGEN~\citep{ragen2025} introduces \textbf{step-independent training}: the trajectory is partitioned into non-overlapping $h$-step windows, each receiving a discounted return:
19	\begin{equation}
20	R_w = \gamma^{(N - w)} \cdot R_{\text{episode}}
21	\label{eq:step_return}
22	\end{equation}
23	where $w \in \{1, \ldots, N\}$ indexes windows and $N = \lceil T/h \rceil$ is the number of windows. Each window is optimized as an independent GRPO sample. This reduces sequence length from $O(T)$ to $O(h)$ and multiplies the effective batch size, but structurally alters credit assignment.
24	
25	\subsection{Dual Mechanism Analysis}
26	\label{sec:dual_mechanism}
27	
28	Two mechanisms jointly cause training failure under step-independent optimization.
29	
30	\subsubsection{Mechanism 1: Policy Information 
…[truncated 3515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-25T21:22:35.912874+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-25T21:22:35.913555+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	Step-independent training collapses while episode-level training succeeds; a partial factorial design separates the two mechanisms; and window size $h$ modulates severity.
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	We evaluate on ALFWorld~\citep{shridhar2021alfworld}, a text-based household environment with six task types requiring sequential reasoning over up to 50 steps. The environment provides ternary reward ($r_- {=} {-}0.1$ per invalid action, $0$ for valid but unsuccessful, $r_+$ for success); our theory assumes simplified binary reward ($R \in \{0, r_+\}$), yielding an upper bound on sign misattribution (Section~\ref{sec:sign_verification} validates under both). The base policy is Qwen3-1.7B fine-tuned on expert demonstrations (SFT baseline: 12.5\% in-distribution), where Proposition~2 predicts the majority of gradient updates carry incorrect sign. All conditions use RAGEN~\citep{ragen2025} (v0.1)\footnote{Our implementation extends RAGEN v0.1 with episode-level training support. Code available upon acceptance.} with GRPO~\citep{shao2024deepseekmath} ($K{=}8$; Appendix~\ref{app:hyperparameters}). We report success rate on a 134-task OOD set (primary) and 32-task in-distribution set (secondary).
10	
11	\subsection{Partial Factorial Mechanism Separation}
12	\label{sec:factorial_experiments}
13	
14	We implement the partial factorial design from Section~\ref{sec:factorial_design} (3 of 4 cells; Cell~C excluded due to NaN instability; Appendix~\ref{app:cell_c}) with two seeds per condition. Cell~C's qualitatively different failure (divergence rather than gradual collapse) suggests information loss may unintentionally stabilize gradient variance, questioning exact separability (Section~\ref{sec:discussion}).
15	
16	\subsection{Results}
17	\label{sec:results}
18	
19	Cell~A collapses in two phases (Table~\ref{tab:main_results}): task success drops to ${\leq}$3\% by step~5 and reaches 0\% by step~15, while 
…[truncated 9421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-25T21:22:44.586222+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-25T21:22:45.038232+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Generality and mechanism interaction.}
5	Sign misattribution arises whenever step-level windowing, sparse binary reward, and group-relative normalization co-occur (Section~\ref{sec:theory}), though verified only on GRPO with ALFWorld and ScienceWorld. Cell~C's NaN divergence (full trajectory + step-level advantage) prevents empirical isolation of M2; our factorial interpretation assumes approximate separability, which the remaining three cells are consistent with but cannot definitively confirm. Cell~C's qualitatively different failure mode suggests M1 may unintentionally stabilize training by limiting gradient variance (Appendix~\ref{app:why_defaults}). Multi-seed evaluation reveals bimodal OOD transfer pointing to initialization sensitivity (Appendix~\ref{app:early_signal}).
6	
7	\paragraph{Concurrent methods.}
8	HCAPO~\citep{hcapo2026} and GiGPO~\citep{feng2025gigpo} succeed with $h{=}2$ by eliminating M2 through finer-grained credit, consistent with our framework's prediction (see Limitations). We provide a practical decision guide for selecting among episode-level and step-level methods based on which mechanisms are active in a given setting (Appendix~\ref{app:method_selection}).
9	
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-25T21:22:45.138948+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/appendix.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/appendix.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-25T21:22:45.239831+00:00_

1	\appendix
2	
3	\section{Theoretical Analysis: Full Derivations}
4	\label{app:theory_full}
5	
6	\subsection{Why Sign Misattribution is the Core Mechanism}
7	\label{app:sign_fundamental}
8	
9	The two mechanisms identified in Section~\ref{sec:dual_mechanism} operate at different layers and produce qualitatively different failures. Policy information loss (Mechanism 1) operates at the inference layer, restricting the observable context and establishing a structural performance ceiling that is constant across training. Sign misattribution (Mechanism 2) operates at the training layer, corrupting gradient directions and progressively degrading performance below this ceiling.
10	
11	\textit{Proof of Proposition 1.} Define ``correct sign'' as follows: for a window containing locally beneficial actions, the correct sign of $\hat{A}_w$ is positive (reinforcement); for a window containing locally detrimental actions, the correct sign is negative (suppression). Under binary reward, the return for window $w$ is $R_w = \gamma^{(N-w)} \cdot R_{\text{episode}}$ (Equation~\ref{eq:step_return}). In a failed episode ($R_{\text{episode}} = 0$), all windows receive $R_w = 0$ regardless of their local action quality. If the group contains at least one successful rollout, the group mean $\mu > 0$, and all windows in the failed episode receive negative advantages after normalization via Equation~\ref{eq:grpo_advantage}. This includes windows where the agent took locally correct actions. Now consider a window with locally correct actions. In a successful episode (probability $p$), the window receives positive $\hat{A}_w$, which is the correct sign. In a failed episode (probability $1 - p$), the window receives negative $\hat{A}_w$ whenever $\mu > 0$, which is the wrong sign. The probability that $\mu = 0$ (all $K$ rollouts in the group failed) is $(1-p)^K$, which shrinks exponentially with $K$. As $K$ grows, nearly every failed episode produces a non-zero group mean, and the window receive
…[truncated 15280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-25T21:22:51.261389+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/appendix.tex",
  "offset": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/appendix.tex",
    "offset": "150"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-25T21:22:51.312190+00:00_

150	
151	\begin{figure*}[t]
152	\centering
153	\includegraphics[width=\textwidth]{fig_additional_conditions.pdf}
154	\caption{(a)~Standard remedies for step-independent training: dense reward shaping and discount factor $\gamma{=}1.0$ both collapse to 0\%; REINFORCE++ matches the SFT baseline without improvement. Only episode-level training (Cell~D) exceeds baseline. (b)~Dense reward gaming: action validity rises from 60\% to 97.5\% while task success remains 0\%; the agent maximizes format-level rewards without solving tasks.}
155	\label{fig:additional_conditions}
156	\end{figure*}
157	
158	\paragraph{Cell~C attempt.}
159	\label{app:cell_c}
160	Cell~C (full observation + step-level advantage) would isolate M2 without M1. We attempted this configuration across six training runs with varying hyperparameters (KL penalty $\beta \in \{0.001, 0.01, 0.04\}$, learning rate $\in \{5{\times}10^{-7}, 10^{-6}\}$). All runs terminated due to training instability: KL divergence spiked above 10.0 within 2--3 steps, triggering NaN losses. We attribute this to the combination of full-length sequences ($>$4096 tokens) with step-level advantage normalization, which produces extreme advantage magnitudes at early window positions. Cell~C remains an important gap in the partial factorial; addressing it likely requires architectural changes (e.g., gradient clipping per window position) beyond the scope of this diagnostic study.
161	
162	
163	\section{Method Selection Guide}
164	\label{app:method_selection}
165	
166	The M1/M2 diagnostic framework guides practitioners toward the appropriate fix without exhaustive ablation. If only M2 is active (sign misattribution with sufficient observation context, e.g., $h$ large enough to preserve task-relevant information), per-step credit methods (Turn-PPO~\citep{turnppo2025}, HCAPO~\citep{hcapo2026}, GiGPO~\citep{feng2025gigpo}) directly address the failure mode. If only M1 is active (information loss without sign corruption), increasing $h$ or swit
…[truncated 6965 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-25T21:27:06.084863+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 审稿意见\n\n**论文**: \"Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n\n---\n\n## Summary\n\n本文诊断了 step-independent agent RL（具体为 GRPO + 固定窗口分解）的两种结构性失败机制：(1) Policy information loss (M1)——窗口截断导致策略无法获取跨窗口上下文，形成恒定性能天花板；(2) Advantage sign misattribution (M2)——基于组归一化的 advantage 符号由 episode 结果而非局部动作质量决定，导致大部分梯度更新方向错误。作者通过部分析因实验（3/4 cells）在 ALFWorld 上分离两种机制，并提出 episode-level GRPO 作为结构性修复。理论分析在 binary reward 假设下推导了错误符号梯度的上界。\n\n---\n\n## Strengths\n\n**S1. 清晰且有用的诊断框架。** M1/M2 双机制分解是对 \"GRPO collapse\" 现象的实质性概念贡献。将 information loss（恒定天花板）与 sign misattribution（累积退化）区分为不同层级（推理层 vs. 训练层）、不同时间特性的失败模式（Section 3.3），为从业者提供了有操作性的诊断思路。该框架能正确预测并发方法（HCAPO、GiGPO）的成功（Section 6），说明其泛化能力。\n\n**S2. 结构化的实验设计。** 部分析因设计（Section 3.5）比典型的 ablation study 更有方法论意识。A→B→D 比较链 + 三类验证指标（sign-episode correlation、credit agreement rate、P(correct|update)）（Section 5.4）构成了多角度的证据体系。Discount factor sweep（Appendix D）排除了折扣衰减作为替代解释的可能性。\n\n**S3. 诚实且有信息量的 11-seed 评估。** 11 seed 的 episode-level 评估（Table 2, Figure 5）超过了该领域常见的 3-5 seed 标准，揭示了重要的 seed-dependent 行为（仅 36% 泛化）。Seed 分类标准（Fisher exact test p<0.01）、Wilson CI、unified step-5 评估（Appendix F）、评估方差分析（Appendix G）均体现了严谨的统计意识。\n\n**S4. 理论与实验的对应。** Proposition 1-2 在 binary reward 假设下提供了 closed-form 上界（P(correct|update) ≤ 19.1% at p=12.5%, K=8），Section 5.4 的 sign-episode correlation (99.6%) 和 credit agreement (52.1%) 实证验证了理论预测。Break-even 比率分析（|Â_correct|/|Â_wrong| ≈ 2.6 < 4.2 = (1-P_c)/P_c）进一步排除了幅度补偿的可能。\n\n**S5. Limitations 部分坦诚。** 论文明确承认了 Cell C 缺失、单 seed 跨环境验证、36% 泛化率、以及未复现并发方法等局限性，未过度声称。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**W1 [Critical]: Cell C 缺失严重削弱 \"Dual Mechanism\" 因果声称**\n- **具体位置**: Section 3.5, Section 5.2, Section 6\n- **问题**: 论文标题声称 \"Dual Mechanism Diagnosis\"，但 2×2 析因设计缺少 Cell C（full trajectory + step-level advantage; only M2 active）。没有 Cell C：(a) 无法独立验证 M1 的效应（需要 C→D 比较）；(b) 无法估计 M1×M2 交互效应；(c) 无法确认两种机制是否真正可分离。论文在 Section 6 承认 \"our factorial interpretation assumes approximate separability, which the remaining three cells are consistent with but cannot definitively confirm\"，但标题和 abstract 的表述暗示了比证据更强的因果声称。\n- **Cell C 的 NaN 不稳定性本身也是一个信号**: Cell C 在六种超参数配置下均发散（Appendix D），论文将其归因于 \"full-length sequences with step-level advantage normalization produces extreme advantage magnitudes\"。这意味着 M1 可能在无意中通过限制梯度方差来稳定训练——即 M1 和 M2 之间存在 **非加性交互**。如果两种机制交互，则 A→B→D 链条的因果推断不成立。\n- **为什么影响接收**: 析因实验是本文核心方法论贡献，Cell C 缺失不仅是一个 gap，更可能反映了 M1/M2 不可分离的根本问题。\n- **建议**: (1) 弱化因果声称的措辞（如 \"dual mechanism hypothesis\" 而非 \"diagnosis\"）；(2) 正式讨论交互效应的可能性及其对解释的影响；(3) 如果可能，提供 Cell C 的替代实验（如 h>2 但 &lt;T 的中间设置，或加梯度裁剪的 Cell C 变体）。\n\n**W2 [Critical]: 析因条件仅 2 seeds，统计效力不足**\n- **具体位置**: Section 5.2, Table 1\n- **问题**: Cells A、B、D 各仅 2 seeds。n=2 无法计算有意义的标准误、置信区间或条件间显著性检验。Table 1 报告的是 \"best checkpoint per seed\" 的单点结果，而非带不确定性的汇总统计。尤其 Cell B 的 OOD 结果 (5.97%) 实际上仅基于 **单个 seed**（Table 1 脚注：\"Single seed; seed2 best checkpoint unavailable for re-evaluation\"）。n=1 的 OOD 评估不构成统计证据。\n- **为什么影响接收**: 即便是定性结论（collapse vs. bounded learning），n=2 也是勉强的底线——一个异常 seed 就会改变结论。论文的 11-seed episode-level 评估恰好展示了高 seed 间变异性（Table 2: OOD 从 8.2% 到 40.3%），这反过来说明 n=2 在析因条件下的结论非常脆弱。\n- **建议**: (1) 增加每个条件的 seed 数至 ≥5；(2) 或明确承认析因结果是 illustrative 而非 statistically validated，并相应弱化语言。\n\n**W3 [Critical]: Cell A 与 Cell B 的操作差异不够精确，\"消除 M2\" 的声称需要更严格的论证**\n- **具体位置**: Section 3.5, Section 5.3\n- **问题**: Cell A 使用 step-level advantage（per-window GRPO 归一化），Cell B 使用 episode-level advantage。但在 GRPO 框架下，由于 R_w = γ^(N-w) · R_episode，窗口级别的 group normalization 会让折扣因子在分子分母中抵消：\n  Â_{w,k} = (R_{w,k} − μ_w) / (σ_w + ε) ≈ (R_episode,k − μ_episode) / (σ_episode + ε')\n  这意味着 Cell A 的 advantage **符号** 与 Cell B 的 episode-level advantage 应该是近似相同的。论文声称 Cell B \"eliminates sign misattribution\"，但如果符号模式相同，则 A→B 的改善可能来自其他操作差异（如 per-window vs. per-episode KL penalty、不同的 effective batch size、或 ε 缩放效应），而非 M2 的消除。\n- **为什么影响接收**: 这是 A→B 比较（论文因果推断链的第一步）的解释基础。如果 Cell B 并非真正消除了 M2，而是改变了训练动态的其他方面，则 \"dual mechanism\" 叙事需要重新审视。\n- **建议**: (1) 提供 Cell A 和 Cell B 中实际 advantage 值的统计比较（sign 分布、magnitude 分布）；(2) 精确说明 Cell B 实现中与 Cell A 不同的所有操作细节；(3) 如果差异主要在 magnitude 而非 sign，则应修正对 M2 的描述。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W4 [Warning]: Binary reward 理论与 ternary reward 实验之间的桥接不够严格**\n- **具体位置**: Section 4 (Propositions 1-2), Section 5.4 (Extension to ternary reward)\n- **问题**: Propositions 1-2 在 binary reward (R ∈ {0, r_+}) 下推导，但实验使用 ternary reward (r ∈ {−0.1, 0, 1})。Section 4 最后一段论证 binary 是 worst case（increasing α relaxes sign-outcome coupling），但：(a) 缺乏形式化证明 binary 确为所有 penalty 结构的 worst case；(b) 实验测得的 credit agreement (52.1%) 与理论 bound (19.1%) \"measure different quantities\"（论文自己承认），两者的比较缺乏精确的数学桥接；(c) 52.1% 虽然 \"marginally above random\"，但仍远高于 19.1%，说明 ternary reward 下的失败机制与 binary case 有质的不同（从 deterministic misattribution 变为 near-random noise），理论分析对实验设置的解释力有限。\n- **建议**: (1) 提供 ternary reward 下 P(correct|update) 的 formal bound 或至少一个 empirical estimate（而非仅 credit agreement rate）；(2) 更清晰地区分三个指标各自衡量的内容及其互补关系。\n\n**W5 [Warning]: 跨环境验证过于薄弱**\n- **具体位置**: Section 5.6, Appendix C\n- **问题**: ScienceWorld 实验（Section 5.6）使用 **单 seed**，且与 ALFWorld 实验 scale 不同（8B vs. 1.7B）。这导致两个混淆因素：(1) 观察到的改善可能来自 scale 而非方法；(2) 单 seed 无统计基础支撑跨环境泛化声称。8B ALFWorld 实验同样是单 seed（Appendix C, Table 4）。\n- **建议**: 至少在 ScienceWorld 上用与 ALFWorld 相同的 1.7B 模型运行 2-3 seeds，以排除 scale 混淆。\n\n**W6 [Warning]: 未与解决相同问题的并发方法进行实验对比**\n- **具体位置**: Section 6, Limitations\n- **问题**: HCAPO (Tan et al., 2026)、GiGPO (Feng et al., 2025)、TurnPPO 均被提及为针对类似问题的方法，论文仅在 Section 6 讨论层面引用它们与 M1/M2 框架的一致性，未进行实验比较。Appendix D 的 baselines（Dense reward、REINFORCE++、discount sweep）均为简单 baselines，不构成对 state-of-the-art 的有效比较。\n- **建议**: 至少与一个并发方法（如 HCAPO 或 GiGPO）进行头对头实验比较，验证 M1/M2 框架的预测能力并展示 episode-level GRPO 的相对优劣。\n\n**W7 [Warning]: Proposition 1 中 \"base success rate p\" 的条件化不够精确**\n- **具体位置**: Section 4, Proposition 1; Appendix A.1\n- **问题**: Proposition 1 称 P(correct sign) → p as K → ∞，其中 p 是 \"base success rate\"。但证明中考虑的是 \"a window with locally correct actions\" 的情况。如果某窗口的局部正确动作提高了 episode 成功概率（即 P(episode success | locally correct at w) > p），则该窗口获得正确符号的概率应为 p_w > p，而非 p。Proposition 1 隐含假设了局部动作质量与 episode 结果的独立性，但这在因果意义上是不成立的（正确的局部动作应提高成功概率）。Definition 1 的脚注部分地讨论了这一点（\"approximately under the mild assumption that policy drift remains small\"），但 Proposition 的形式化表述未反映这一条件。\n- **建议**: 明确 Proposition 1 是在 p = P(episode success) 的无条件意义上成立（此时为下界而非精确极限），或添加独立性假设。\n\n### Minor 问题（不影响接收）\n\n**M1.** Table 1 的数据完整性问题：Cell A 的 OOD 栏为 \"---\"（未评估），Cell B 的 OOD 仅基于单 seed。考虑到 OOD 泛化是本文的 primary metric，main table 中关键条件缺失 OOD 数据是不理想的。\n\n**M2.** Section 5.4 中 Cohen's h = 0.041 被描述为 \"below the small-effect threshold\"，但未明确说明该 threshold 是 0.2（Cohen's conventional boundary）。建议显式引用。\n\n**M3.** Equation 6 的 cumulative divergence 分析假设 g+ 和 g- 有对称幅度（\"when P_c < 0.5, the expected gradient points away from good policies\"），但随后 Section 5.4 测量的幅度比 (2.6) 显示并非对称。论文确实提供了 break-even 分析，但 Equation 6 本身的表述可以更精确。\n\n**M4.** Abstract 中 \"17.7% mean OOD success versus 6.72% SFT baseline\" 的绝对数字较低，且 36% 泛化率意味着方法的 practical reliability 有限。建议在 abstract 中更明确地框定贡献为 diagnostic（诊断性的），而非将 episode-level GRPO 定位为一个 robust 的解决方案。\n\n**M5.** Appendix H 的 early training signal analysis (n=4 per group) 样本量太小，Welch t-test 在 n=4 下几乎没有检验效力。Cohen's d = 1.11 是一个大效应量但 p = 0.19，这恰恰说明需要更多 seeds。\n\n---\n\n## Questions\n\n**Q1.** Cell B 中 \"episode-level advantage\" 的精确实现是什么？是 (a) 对每个 episode 计算单个 Â = (R_episode − μ) / (σ + ε) 并应用于所有 tokens，还是 (b) 使用 episode-level 信息为每个 window 计算不同的 advantage？如果是 (a)，请解释为什么在 sign 模式与 Cell A 相同的情况下，Cell B 表现出质的不同。\n\n**Q2.** 11 seeds 中的 \"Collapsed\" seeds (27%) 的失败模式是什么？是回到了 step-independent 的 sign misattribution（不应该，因为 episode-level 训练消除了 M2），还是完全不同的失败机制（如 response length inflation，Appendix E 暗示）？如果是后者，这是否说明 M1/M2 之外存在第三种重要的失败机制？\n\n**Q3.** 论文使用 action validity 作为 local action quality 的 proxy（Definition 1）。在 ALFWorld 中，early training 阶段有多大比例的 actions 是 valid？如果绝大多数 actions 都是 valid（如 >80%），则 credit agreement rate 指标的 discriminative power 会非常低。\n\n**Q4.** 跨 scale 实验（8B）中 Cell D 达到 90.3% OOD vs. 1.7B 的 17.7% mean OOD。这个巨大差异是来自 scale 还是方法？如果 8B SFT baseline 已经是 80.6% OOD，那么 GRPO 的增量贡献 (~10pp) 与 1.7B 的增量 (~11pp) 其实相似。请明确讨论 scale 贡献与方法贡献的分离。\n\n---\n\n## Missing References\n\n- Ahmadian et al. (2024). \"Back to Basics: Revisiting REINFORCE-Style Optimization for Learning from Human Feedback in LLMs.\" — 与 REINFORCE++ baseline 和 episode-level GRPO 的关系值得讨论。\n- Yu et al. (2025). \"DAPO: An Open-Source LLM Reinforcement Learning System.\" — GRPO 变体中的 group normalization 改进可能与 M2 相关。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.0/5 | Main claims（dual mechanism diagnosis）有实验支撑，但 Cell C 缺失、2-seed 析因、Cell A/B 操作差异不精确等问题使因果声称未完全成立。理论分析在 binary reward 下 sound，但与 ternary 实验的桥接有 gap。|\n| **Excitement** | 3.0/5 | 问题重要且时效性强（step-independent training 是当前 agent RL 主流范式）。M1/M2 框架对从业者有实际指导价值。但修复方案（episode-level GRPO）较为直接且 36% 可靠性限制了实践影响。|\n| **Reproducibility** | 3.5/5 | 提供了匿名代码链接、超参数表（Appendix B）、实验 ID。但 Cell B 的实现细节不够精确，部分条件的 seed 数过少影响可复现性验证。|\n| **Confidence** | 4/5 | 熟悉 GRPO、agent RL、credit assignment 和实验设计方法论。对 RAGEN 框架的具体实现细节不完全确定。|\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n\n**一句话总结**: 论文提出了有用的 M1/M2 诊断框架来解释 step-independent agent RL 的训练崩溃，但核心因果声称受 Cell C 缺失、2-seed 析因统计效力不足、以及 Cell A/B 操作差异定义不精确的制约，证据强度更适合 Findings 而非主会议。\n\n**Justification**: 这是一篇以诊断/分析为主的论文，其核心贡献是 M1/M2 概念框架。该框架有解释力且对从业者有实际价值（S1）。但作为诊断性论文，其证据标准应当更高：(1) 析因设计缺少 Cell C 且每条件仅 2 seeds（W1, W2），因果推断链不完整；(2) Cell A 与 Cell B 的操作差异（W3）使 \"消除 M2\" 的声称需要更严格论证；(3) 理论与实验的 reward 设置不匹配（W4）。若能补充 Cell C（或其变体）、增加 seed 数、并精确化 Cell B 的操作定义，该论文有望提升至 Borderline Conference (3.5)。\n\n---\n\n## 主要优势\n- 对重要问题（step-independent agent RL 训练崩溃）的首个系统性诊断\n- M1/M2 框架有预测力（正确预测并发方法的成功）\n- 11-seed 评估的统计严谨性超过领域平均水平\n- 论文写作清晰，Limitations 坦诚\n",
  "reviewer_id": "1",
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 审稿意见\n\n**论文**: \"Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n\n---\n\n## Summary\n\n本文诊断了 step-independent agent RL（具体为 GRPO + 固定窗口分解）的两种结构性失败机制：(1) Policy information loss (M1)——窗口截断导致策略无法获取跨窗口上下文，形成恒定性能天花板；(2) Advantage sign misattribution (M2)——基于组归一化的 advantage 符号由 episode 结果而非局部动作质量决定，导致大部分梯度更新方向错误。作者通过部分析因实验（3/4 cells）在 ALFWorld 上分离两种机制，并提出 episode-level GRPO 作为结构性修复。理论分析在 binary reward 假设下推导了错误符号梯度的上界。\n\n---\n\n## Strengths\n\n**S1. 清晰且有用的诊断框架。** M1/M2 双机制分解是对 \"GRPO collapse\" 现象的实质性概念贡献。将 information loss（恒定天花板）与 sign misattribution（累积退化）区分为不同层级（推理层 vs. 训练层）、不同时间特性的失败模式（Section 3.3），为从业者提供了有操作性的诊断思路。该框架能正确预测并发方法（HCAPO、GiGPO）的成功（Section 6），说明其泛化能力。\n\n**S2. 结构化的实验设计。** 部分析因设计（Section 3.5）比典型的 ablation study 更有方法论意识。A→B→D 比较链 + 三类验证指标（sign-episode correlation、credit agreement rate、P(correct|update)）（Section 5.4）构成了多角度的证据体系。Discount factor sweep（Appendix D）排除了折扣衰减作为替代解释的可能性。\n\n**S3. 诚实且有信息量的 11-seed 评估。** 11 seed 的 episode-level 评估（Table 2, Figure 5）超过了该领域常见的 3-5 seed 标准，揭示了重要的 seed-dependent 行为（仅 36% 泛化）。Seed 分类标准（Fisher exact test p<0.01）、Wilson CI、unified step-5 评估（Appendix F）、评估方差分析（Appendix G）均体现了严谨的统计意识。\n\n**S4. 理论与实验的对应。** Proposition 1-2 在 binary reward 假设下提供了 closed-form 上界（P(correct|update) ≤ 19.1% at p=12.5%, K=8），Section 5.4 的 sign-episode correlation (99.6%) 和 credit agreement (52.1%) 实证验证了理论预测。Break-even 比率分析（|Â_correct|/|Â_wrong| ≈ 2.6 < 4.2 = (1-P_c)/P_c）进一步排除了幅度补偿的可能。\n\n**S5. Limitations 部分坦诚。** 论文明确承认了 Cell C 缺失、单 seed 跨环境验证、36% 泛化率、以及未复现并发方法等局限性，未过度声称。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**W1 [Critical]: Cell C 缺失严重削弱 \"Dual Mechanism\" 因果声称**\n- **具体位置**: Section 3.5, Section 5.2, Section 6\n- **问题**: 论文标题声称 \"Dual Mechanism Diagnosis\"，但 2×2 析因设计缺少 Cell C（full trajectory + step-level advantage; only M2 active）。没有 Cell C：(a) 无法独立验证 M1 的效应（需要 C→D 比较）；(b) 无法估计 M1×M2 交互效应；(c) 无法确认两种机制是否真正可分离。论文在 Section 6 承认 \"our factorial interpretation assumes approximate separability, which the remaining three cells are consistent with but cannot definitively confirm\"，但标题和 abstract 的表述暗示了比证据更强的因果声称。\n- **Cell C 的 NaN 不稳定性本身也是一个信号**: Cell C 在六种超参数配置下均发散（Appendix D），论文将其归因于 \"full-length sequences with step-level advantage normalization produces extreme advantage magnitudes\"。这意味着 M1 可能在无意中通过限制梯度方差来稳定训练——即 M1 和 M2 之间存在 **非加性交互**。如果两种机制交互，则 A→B→D 链条的因果推断不成立。\n- **为什么影响接收**: 析因实验是本文核心方法论贡献，Cell C 缺失不仅是一个 gap，更可能反映了 M1/M2 不可分离的根本问题。\n- **建议**: (1) 弱化因果声称的措辞（如 \"dual mechanism hypothesis\" 而非 \"diagnosis\"）；(2) 正式讨论交互效应的可能性及其对解释的影响；(3) 如果可能，提供 Cell C 的替代实验（如 h>2 但 &lt;T 的中间设置，或加梯度裁剪的 Cell C 变体）。\n\n**W2 [Critical]: 析因条件仅 2 seeds，统计效力不足**\n- **具体位置**: Section 5.2, Table 1\n- **问题**: Cells A、B、D 各仅 2 seeds。n=2 无法计算有意义的标准误、置信区间或条件间显著性检验。Table 1 报告的是 \"best checkpoint per seed\" 的单点结果，而非带不确定性的汇总统计。尤其 Cell B 的 OOD 结果 (5.97%) 实际上仅基于 **单个 seed**（Table 1 脚注：\"Single seed; seed2 best checkpoint unavailable for re-evaluation\"）。n=1 的 OOD 评估不构成统计证据。\n- **为什么影响接收**: 即便是定性结论（collapse vs. bounded learning），n=2 也是勉强的底线——一个异常 seed 就会改变结论。论文的 11-seed episode-level 评估恰好展示了高 seed 间变异性（Table 2: OOD 从 8.2% 到 40.3%），这反过来说明 n=2 在析因条件下的结论非常脆弱。\n- **建议**: (1) 增加每个条件的 seed 数至 ≥5；(2) 或明确承认析因结果是 illustrative 而非 statistically validated，并相应弱化语言。\n\n**W3 [Critical]: Cell A 与 Cell B 的操作差异不够精确，\"消除 M2\" 的声称需要更严格的论证**\n- **具体位置**: Section 3.5, Section 5.3\n- **问题**: Cell A 使用 step-level advantage（per-window GRPO 归一化），Cell B 使用 episode-level advantage。但在 GRPO 框架下，由于 R_w = γ^(N-w) · R_episode，窗口级别的 group normalization 会让折扣因子在分子分母中抵消：\n  Â_{w,k} = (R_{w,k} − μ_w) / (σ_w + ε) ≈ (R_episode,k − μ_episode) / (σ_episode + ε')\n  这意味着 Cell A 的 advantage **符号** 与 Cell B 的 episode-level advantage 应该是近似相同的。论文声称 Cell B \"eliminates sign misattribution\"，但如果符号模式相同，则 A→B 的改善可能来自其他操作差异（如 per-window vs. per-episode KL penalty、不同的 effective batch size、或 ε 缩放效应），而非 M2 的消除。\n- **为什么影响接收**: 这是 A→B 比较（论文因果推断链的第一步）的解释基础。如果 Cell B 并非真正消除了 M2，而是改变了训练动态的其他方面，则 \"dual mechanism\" 叙事需要重新审视。\n- **建议**: (1) 提供 Cell A 和 Cell B 中实际 advantage 值的统计比较（sign 分布、magnitude 分布）；(2) 精确说明 Cell B 实现中与 Cell A 不同的所有操作细节；(3) 如果差异主要在 magnitude 而非 sign，则应修正对 M2 的描述。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W4 [Warning]: Binary reward 理论与 ternary reward 实验之间的桥接不够严格**\n- **具体位置**: Section 4 (Propositions 1-2), Section 5.4 (Extension to ternary reward)\n- **问题**: Propositions 1-2 在 binary reward (R ∈ {0, r_+}) 下推导，但实验使用 ternary reward (r ∈ {−0.1, 0, 1})。Section 4 最后一段论证 binary 是 worst case（increasing α relaxes sign-outcome coupling），但：(a) 缺乏形式化证明 binary 确为所有 penalty 结构的 worst case；(b) 实验测得的 credit agreement (52.1%) 与理论 bound (19.1%) \"measure different quantities\"（论文自己承认），两者的比较缺乏精确的数学桥接；(c) 52.1% 虽然 \"marginally above random\"，但仍远高于 19.1%，说明 ternary reward 下的失败机制与 binary case 有质的不同（从 deterministic misattribution 变为 near-random noise），理论分析对实验设置的解释力有限。\n- **建议**: (1) 提供 ternary reward 下 P(correct|update) 的 formal bound 或至少一个 empirical estimate（而非仅 credit agreement rate）；(2) 更清晰地区分三个指标各自衡量的内容及其互补关系。\n\n**W5 [Warning]: 跨环境验证过于薄弱**\n- **具体位置**: Section 5.6, Appendix C\n- **问题**: ScienceWorld 实验（Section 5.6）使用 **单 seed**，且与 ALFWorld 实验 scale 不同（8B vs. 1.7B）。这导致两个混淆因素：(1) 观察到的改善可能来自 scale 而非方法；(2) 单 seed 无统计基础支撑跨环境泛化声称。8B ALFWorld 实验同样是单 seed（Appendix C, Table 4）。\n- **建议**: 至少在 ScienceWorld 上用与 ALFWorld 相同的 1.7B 模型运行 2-3 seeds，以排除 scale 混淆。\n\n**W6 [Warning]: 未与解决相同问题的并发方法进行实验对比**\n- **具体位置**: Section 6, Limitations\n- **问题**: HCAPO (Tan et al., 2026)、GiGPO (Feng et al., 2025)、TurnPPO 均被提及为针对类似问题的方法，论文仅在 Section 6 讨论层面引用它们与 M1/M2 框架的一致性，未进行实验比较。Appendix D 的 baselines（Dense reward、REINFORCE++、discount sweep）均为简单 baselines，不构成对 state-of-the-art 的有效比较。\n- **建议**: 至少与一个并发方法（如 HCAPO 或 GiGPO）进行头对头实验比较，验证 M1/M2 框架的预测能力并展示 episode-level GRPO 的相对优劣。\n\n**W7 [Warning]: Proposition 1 中 \"base success rate p\" 的条件化不够精确**\n- **具体位置**: Section 4, Proposition 1; Appendix A.1\n- **问题**: Proposition 1 称 P(correct sign) → p as K → ∞，其中 p 是 \"base success rate\"。但证明中考虑的是 \"a window with locally correct actions\" 的情况。如果某窗口的局部正确动作提高了 episode 成功概率（即 P(episode success | locally correct at w) > p），则该窗口获得正确符号的概率应为 p_w > p，而非 p。Proposition 1 隐含假设了局部动作质量与 episode 结果的独立性，但这在因果意义上是不成立的（正确的局部动作应提高成功概率）。Definition 1 的脚注部分地讨论了这一点（\"approximately under the mild assumption that policy drift remains small\"），但 Proposition 的形式化表述未反映这一条件。\n- **建议**: 明确 Proposition 1 是在 p = P(episode success) 的无条件意义上成立（此时为下界而非精确极限），或添加独立性假设。\n\n### Minor 问题（不影响接收）\n\n**M1.** Table 1 的数据完整性问题：Cell A 的 OOD 栏为 \"---\"（未评估），Cell B 的 OOD 仅基于单 seed。考虑到 OOD 泛化是本文的 primary metric，main table 中关键条件缺失 OOD 数据是不理想的。\n\n**M2.** Section 5.4 中 Cohen's h = 0.041 被描述为 \"below the small-effect threshold\"，但未明确说明该 threshold 是 0.2（Cohen's conventional boundary）。建议显式引用。\n\n**M3.** Equation 6 的 cumulative divergence 分析假设 g+ 和 g- 有对称幅度（\"when P_c < 0.5, the expected gradient points away from good policies\"），但随后 Section 5.4 测量的幅度比 (2.6) 显示并非对称。论文确实提供了 break-even 分析，但 Equation 6 本身的表述可以更精确。\n\n**M4.** Abstract 中 \"17.7% mean OOD success versus 6.72% SFT baseline\" 的绝对数字较低，且 36% 泛化率意味着方法的 practical reliability 有限。建议在 abstract 中更明确地框定贡献为 diagnostic（诊断性的），而非将 episode-level GRPO 定位为一个 robust 的解决方案。\n\n**M5.** Appendix H 的 early training signal analysis (n=4 per group) 样本量太小，Welch t-test 在 n=4 下几乎没有检验效力。Cohen's d = 1.11 是一个大效应量但 p = 0.19，这恰恰说明需要更多 seeds。\n\n---\n\n## Questions\n\n**Q1.** Cell B 中 \"episode-level advantage\" 的精确实现是什么？是 (a) 对每个 episode 计算单个 Â = (R_episode − μ) / (σ + ε) 并应用于所有 tokens，还是 (b) 使用 episode-level 信息为每个 window 计算不同的 advantage？如果是 (a)，请解释为什么在 sign 模式与 Cell A 相同的情况下，Cell B 表现出质的不同。\n\n**Q2.** 11 seeds 中的 \"Collapsed\" seeds (27%) 的失败模式是什么？是回到了 step-independent 的 sign misattribution（不应该，因为 episode-level 训练消除了 M2），还是完全不同的失败机制（如 response length inflation，Appendix E 暗示）？如果是后者，这是否说明 M1/M2 之外存在第三种重要的失败机制？\n\n**Q3.** 论文使用 action validity 作为 local action quality 的 proxy（Definition 1）。在 ALFWorld 中，early training 阶段有多大比例的 actions 是 valid？如果绝大多数 actions 都是 valid（如 >80%），则 credit agreement rate 指标的 discriminative power 会非常低。\n\n**Q4.** 跨 scale 实验（8B）中 Cell D 达到 90.3% OOD vs. 1.7B 的 17.7% mean OOD。这个巨大差异是来自 scale 还是方法？如果 8B SFT baseline 已经是 80.6% OOD，那么 GRPO 的增量贡献 (~10pp) 与 1.7B 的增量 (~11pp) 其实相似。请明确讨论 scale 贡献与方法贡献的分离。\n\n---\n\n## Missing References\n\n- Ahmadian et al. (2024). \"Back to Basics: Revisiting REINFORCE-Style Optimization for Learning from Human Feedback in LLMs.\" — 与 REINFORCE++ baseline 和 episode-level GRPO 的关系值得讨论。\n- Yu et al. (2025). \"DAPO: An Open-Source LLM Reinforcement Learning System.\" — GRPO 变体中的 group normalization 改进可能与 M2 相关。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.0/5 | Main claims（dual mechanism diagnosis）有实验支撑，但 Cell C 缺失、2-seed 析因、Cell A/B 操作差异不精确等问题使因果声称未完全成立。理论分析在 binary reward 下 sound，但与 ternary 实验的桥接有 gap。|\n| **Excitement** | 3.0/5 | 问题重要且时效性强（step-independent training 是当前 agent RL 主流范式）。M1/M2 框架对从业者有实际指导价值。但修复方案（episode-level GRPO）较为直接且 36% 可靠性限制了实践影响。|\n| **Reproducibility** | 3.5/5 | 提供了匿名代码链接、超参数表（Appendix B）、实验 ID。但 Cell B 的实现细节不够精确，部分条件的 seed 数过少影响可复现性验证。|\n| **Confidence** | 4/5 | 熟悉 GRPO、agent RL、credit assignment 和实验设计方法论。对 RAGEN 框架的具体实现细节不完全确定。|\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n\n**一句话总结**: 论文提出了有用的 M1/M2 诊断框架来解释 step-independent agent RL 的训练崩溃，但核心因果声称受 Cell C 缺失、2-seed 析因统计效力不足、以及 Cell A/B 操作差异定义不精确的制约，证据强度更适合 Findings 而非主会议。\n\n**Justification**: 这是一篇以诊断/分析为主的论文，其核心贡献是 M1/M2 概念框架。该框架有解释力且对从业者有实际价值（S1）。但作为诊断性论文，其证据标准应当更高：(1) 析因设计缺少 Cell C 且每条件仅 2 seeds（W1, W2），因果推断链不完整；(2) Cell A 与 Cell B 的操作差异（W3）使 \"消除 M2\" 的声称需要更严格论证；(3) 理论与实验的 reward 设置不匹配（W4）。若能补充 Cell C（或其变体）、增加 seed 数、并精确化 Cell B 的操作定义，该论文有望提升至 Borderline Conference (3.5)。\n\n---\n\n## 主要优势\n- 对重要问题（step-independent agent RL 训练崩溃）的首个系统性诊断\n- M1/M2 框架有预测力（正确预测并发方法的成功）\n- 11-seed 评估的统计严谨性超过领域平均水平\n- 论文写作清晰，Limitations 坦诚\n",
    "reviewer_id": "1",
    "project": "cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-25T21:27:09.902207+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3817
}
```

</details>

---


### Assistant

_source line 522 · 2026-05-25T21:27:18.652490+00:00_

审稿意见已提交给 Review Director。

核心评判：**Overall 3.0 (Findings)**。

三个 Critical 问题：
1. **Cell C 缺失**——2×2 析因只有 3 cells，无法验证 M1/M2 可分离性，且 Cell C 的 NaN 发散反而暗示两者存在非加性交互
2. **2 seeds/条件**——统计效力严重不足，Cell B 的 OOD 甚至只有单 seed
3. **Cell A vs B 操作差异不精确**——GRPO 归一化中折扣因子抵消后，两者 advantage sign 应近似相同，"消除 M2" 的声称需更严格论证

三个 Should-Fix：binary/ternary 理论-实验 gap、单 seed 跨环境验证、缺少与并发方法的实验对比。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1"
}
```

</details>

---


## Round 19

## Round 19

4 recorded events


### User

_source line 523 · 2026-05-25T21:28:06.685840+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Strength/Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿意见

### Summary
本文诊断了 step-independent agent RL 训练中的两个失败机制：策略信息丢失（M1，上下文截断导致性能上限）和优势符号误归因（M2，group normalization 在 binary reward 下使梯度符号反映 episode 结果而非局部动作质量）。通过 2×2 部分析因实验分离两个机制的贡献，并提出 episode-level GRPO 作为结构性修复。诊断框架设计合理、实验方法学规范，但所提出的"修复"方法新颖性有限（本质是恢复标准 GRPO），且高 seed 变异性（仅 36% seed 泛化）削弱了实际影响力。

### Overall: 3.0 (Findings), Soundness 3.0, Excitement 2.5, Confidence 4/5

### Strengths
S1: 精心设计的部分析因实验（Section 3.5, 5.2-5.3）
S2: 科学诚实的报告标准——36% 泛化率、seed 变异性、Cell C 不稳定性均坦诚披露
S3: 理论与实验的对照验证——三项指标 + break-even magnitude ratio 分析
S4: 清晰的写作和可视化
S5: 跨环境和跨规模验证（虽为 single seed 但提供了初步证据）

### Must-Fix
W1 [Critical]: Episode-level GRPO 的方法论新颖性极为有限——"修复"本质是恢复 GRPO 原始设计，论文自身承认 "step-independent windowing is the deviation"。标题含 "Episode-Level Correction" 暗示方法论贡献，但实际是设计选择的回退。
W2 [Critical]: Abstract/Intro 的 overclaiming——"structurally eliminates both failure modes" vs 36% seed 泛化率矛盾；17.7% 均值被少数泛化 seed 拉高，中位数应更低；单 seed 8B (90.3% OOD) 证据强度极弱。

### Should-Fix
W3 [Warning]: Cell C 缺失削弱析因完整性——M1 可能无意中通过限制梯度方差稳定训练，暗示非加性交互
W4 [Warning]: 实验范围偏窄——单一主环境、无同期方法 head-to-head 对比、所有 OOD 评估为单次 τ=0.4
W5 [Warning]: 理论 binary reward 假设与 ternary 实验 gap——52.1% credit agreement vs 19.1% bound 差距巨大
W6 [Warning]: 与同期工作的关系停留在声明层面，缺乏实证验证框架预测能力

### Minor
M1: Table 1 Cell B OOD 仅单 seed
M2: Figure 3(b) h=10 两 seed 差异大，仅报告均值
M3: 12.5% SFT baseline 偏低，可能影响诊断普适性
M4: Equation 2 中 γ 值主文未给出
M5: AI assistance 声明透明度好

### Questions
Q1: 11 seed OOD 中位数是多少？
Q2: 8B 实验尝试了多少个 seed？
Q3: Cell C NaN 是否代表 M1/M2 框架外的独立现象？M1 是否有正则化作用？
Q4: 19.1% (binary) vs 52.1% (ternary) 哪个更准确描述实际训练动态？
Q5: 是否考虑过更密 reward 信号环境测试 M2 边界？
Q6: REINFORCE++ 为何不帮助？是 normalization 还是 reward sparsity？

### Missing References
1. RLOO (Ahmadian et al., 2024)
2. COMA (Foerster et al., 2018), QMIX (Rashid et al., 2020)

---

请逐条回应（[AGREE] 或 [REBUT]），并基于论文具体内容和你自己的专业判断给出理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-25T21:30:43.269842+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Strengths\n\n**[AGREE] R2-S1 (析因实验设计)**\n同意。部分析因设计是本文方法论上的亮点，比典型 ablation study 更有结构意识。我在自己的审稿中也将此列为 S2。\n\n**[AGREE] R2-S2 (科学诚实的报告)**\n同意。36% 泛化率、seed 变异性、Cell C 不稳定性的坦诚披露是值得肯定的。11-seed 评估本身就超过了领域平均水平。\n\n**[AGREE] R2-S3 (理论与实验对照)**\n同意。三项验证指标（sign-episode correlation、credit agreement、P(correct|update)）+ break-even magnitude ratio (2.6 < 4.2) 构成了多角度证据（Section 5.4）。\n\n**[AGREE] R2-S4 (写作和可视化)**\n同意。论文结构清晰，Figure 1 的示意图有效传达了核心思想。\n\n**[AGREE] R2-S5 (跨环境/规模验证)**\n同意。单 seed 是限制，但提供了 directional evidence。\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-W1: Episode-level GRPO 新颖性有限**\n同意这一判断，但我认为严重性应适当校准。\n\n理由：论文自身在 Section 3.4 明确写道 \"step-independent windowing is the deviation introduced by multi-turn agent frameworks\"，Section 6 也说 \"Episode-level GRPO is equivalent to REINFORCE where the group mean μ replaces b(s)\"（Appendix A.3）。这说明 \"correction\" 本质上是回退到标准 GRPO/REINFORCE，不是方法论创新。标题中 \"Episode-Level Correction\" 确实暗示了超出论文实际贡献的方法论新颖性。\n\n**但需校准**：如果论文定位为 **诊断/分析** 贡献而非方法贡献，则修复方案的简洁性反而是优势（Occam's razor——诊断准确了，修复自然简单）。问题在于标题和写作框架未能清晰地将贡献定位在诊断侧。建议将此评估为 **Should-Fix**（修改标题和定位措辞）而非 Critical Must-Fix，因为核心诊断贡献不受影响。\n\n**[AGREE] R2-W2: Abstract/Intro 的 overclaiming**\n强烈同意。这是我在 Minor M4 中也提到但严重性可能评估偏低的问题。R2 的分析更精确：\n\n补充关键证据：根据 Table 2 的数据，11 seed 的 OOD 中位数为 **12.69%**（排序后第 6 个值），远低于论文报告的 mean 17.7%。中位数仅比 SFT baseline (6.72%) 高 ~6pp，且对应的 seed (seed42/seed100) 均被分类为 \"Collapsed\" 或 \"Stagnant\"（Fisher exact test NS）。这意味着 **过半数 seeds 未达到统计显著的 OOD 改善**。\n\n\"structurally eliminates both failure modes\" 在技术上是正确的（episode-level 训练确实消除了 M1 和 M2 的结构性原因），但与 36% 泛化率并置时产生强烈的误导效果。Abstract 应报告 median 或明确说明 mean 被少数高 seed 拉高。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W3: Cell C 缺失削弱析因完整性**\n完全同意。我在自己的审稿中将此列为 W1 (Critical)，给出了更详细的分析。Cell C 的 NaN 不稳定性（Appendix D: 六种超参数配置均发散）本身暗示 M1 可能通过限制序列长度和梯度方差起到无意中的正则化作用——即 M1 和 M2 存在非加性交互。论文在 Section 6 承认 \"our factorial interpretation assumes approximate separability\"，但如果这一假设不成立，则整个 A→B→D 因果链的推断基础被动摇。\n\n**[AGREE] R2-W4: 实验范围偏窄**\n同意。我在自己的审稿中也提出了跨环境验证薄弱（my W5）和缺乏同期方法对比（my W6）的问题。补充一点：所有 OOD 评估均为单次 τ=0.4 是一个值得强调的限制——Appendix G 的评估方差分析仅基于 **一个 stagnant seed** (seed200)，不能代表 generalized seeds 的评估方差。\n\n**[AGREE] R2-W5: Binary theory vs ternary experiment gap**\n同意。我在 W4 中详细讨论了这一点。补充：19.1% 和 52.1% 不仅数值差距巨大，而且反映的是 **质的不同** 的失败模式——binary 下是 deterministic misattribution（符号几乎完全由 episode 结果决定），ternary 下是 near-random noise（52.1% ≈ 50%，advantage 符号几乎不携带局部信息）。论文的理论分析对实验设置的解释力因此受限。\n\n**[AGREE] R2-W6: 与同期工作关系缺乏实证验证**\n同意。Section 6 声称 \"HCAPO and GiGPO succeed with h=2 by eliminating M2 through finer-grained credit, consistent with our framework's prediction\"，但这只是事后解释（post-hoc rationalization），不是框架预测能力的验证。真正的验证需要：(a) 在相同设置下实验对比；(b) 或框架对新方法的 **先验预测**，而非对已发表结果的事后一致性声称。\n\n---\n\n### Minor\n\n**[AGREE] R2-M1: Table 1 Cell B OOD 仅单 seed**\n同意。我在 W2 和 M1 中也标记了这个问题。n=1 的 OOD 评估不构成统计证据，尤其考虑到 11-seed 评估展示了高 seed 间变异性。\n\n**[AGREE] R2-M2: Figure 3(b) h=10 报告方式**\n同意。h=10 的两 seed 差异（6.25% vs. 21.9%）非常大，仅报告均值 (14.1%) 掩盖了这种不确定性。论文应同时报告两个单 seed 值，或用 error bar 标注。实际上 Figure 3(b) 的 black dots 确实展示了个体 seed，这是好的，但主文讨论（Section 5.3 末尾）只提了均值。\n\n**[REBUT] R2-M3: 12.5% SFT baseline 偏低**\n部分不同意。\n\n理由：R2 认为低 baseline 可能限制诊断的普适性。但 Proposition 2 的分析恰恰表明 sign misattribution 的严重性 **随 p 下降而增加**（Equation 4: P(correct|update) 在 p=5% 时仅 14.9%，p=50% 时 50.2%）。论文在 Section 4 \"Severity scales with task difficulty\" 段落中明确讨论了这一点。因此，低 baseline 设置实际上是 **最能暴露 M2 问题的设置**，而非削弱诊断的设置。\n\n不过 R2 的隐含关切也有道理：论文需要证明 M2 在更高 baseline (p > 30%) 的设置中仍然是 **实际可观察的** 问题（而非仅理论预测）。8B 实验的 SFT baseline 为 80.6%，此时 P(correct|update) ≈ 80.6%，sign misattribution 应不再是主要问题——然而 8B Cell A 仍然崩溃。这意味着 collapse 在高 baseline 下可能由 M1 主导而非 M2，削弱了 \"dual mechanism\" 框架在不同 baseline 水平下的统一解释力。这一分析论文未展开讨论，我认为是一个有价值的延伸，但更适合作为 future work 而非 must-fix。\n\n**[AGREE] R2-M4: γ 值主文未给出**\n同意。Equation 2 使用了 γ 但 γ=0.95 仅在 Appendix B (Table 3) 给出。主文应在 Section 3.2 或 Section 5.1 中明确 γ 值。\n\n**[AGREE] R2-M5: AI assistance 声明**\n同意。Appendix H 的 AI 使用声明（Claude as coding/writing/literature assistant）透明度好。\n\n---\n\n### Questions\n\n**[AGREE] R2-Q1: 11 seed OOD 中位数**\n同意这是一个关键统计量。如上文计算，中位数为 **12.69%**，远低于 mean 17.7%。分布是右偏的（4 个 generalized seeds 拉高均值）。论文仅报告 mean 而未报告 median 确实不够透明。\n\n**[AGREE] R2-Q2: 8B seed 数**\n同意这是一个重要问题。论文明确说 \"single-seed\"（Section 5.6），但单 seed 的 90.3% OOD 被用作 cross-scale validation 的核心证据，证据强度极弱。\n\n**[AGREE] R2-Q3: Cell C NaN 与 M1/M2 框架**\n同意这是一个深层问题。我在自己的 W1 中也详细讨论了这一点。Cell C 的 NaN 可能代表：(a) M1 确实有正则化副作用（通过限制序列长度和梯度方差），即 M1 和 M2 存在交互而非独立；(b) 或者存在 M1/M2 框架之外的第三种机制（长序列 + per-window normalization 的数值不稳定性）。无论哪种解释，都挑战了论文的 \"两种独立机制\" 框架。论文在 Appendix D 将原因归结为 \"full-length sequences with step-level advantage normalization produces extreme advantage magnitudes\"，但未充分讨论这对框架本身的含义。\n\n**[REBUT] R2-Q4: 19.1% vs 52.1% 哪个更准确**\n我认为这个问题的答案比 R2 暗示的更微妙。\n\n理由：这两个数字衡量的是 **不同的量**（论文在 Section 5.4 和 Appendix A.2 中明确区分）：\n- 19.1% = P(correct | update)：binary reward 下，非零梯度更新中正确符号的比例上界。这是一个 **理论 bound**，衡量的是梯度方向的正确性。\n- 52.1% = credit agreement rate：ternary reward 下，valid-action windows 获得正确 advantage 符号的比例。这是一个 **经验指标**，衡量的是 advantage 符号与 action validity proxy 的一致性。\n\n两者不可直接比较。对实际训练动态而言，52.1%（ternary）更接近实验设置，但它衡量的不是梯度正确性（因为使用了 action validity 作为 proxy）。19.1%（binary）更 precisely 衡量梯度正确性，但假设与实验不符。**两者都不完美**——论文的贡献是从两个互补角度确认 credit assignment 失败，而非提供单一精确估计。\n\n**[AGREE] R2-Q5: Dense reward 环境测试 M2 边界**\n同意。论文的 dense reward 实验（Appendix D）是在 ALFWorld 中 **人工添加** per-step bonus (+0.15/valid action)，结果是 reward gaming（action validity ↑ 到 97.5%，task success 维持 0%）。但 R2 的问题更深入：在 **天然具有 dense reward 信号** 的环境中，M2 的严重程度是否降低？Proposition 2 的 bound 依赖于 binary episode reward 假设，如果环境提供真正的 per-step reward signal（而非人工 shaping），M2 可能不再是主要失败模式。论文未在此类环境中测试，这是一个有价值的 future work 方向。\n\n**[AGREE] R2-Q6: REINFORCE++ 为何不帮助**\n同意这是一个需要更深入解释的问题。论文在 Appendix D 的解释（\"per-token advantage normalization alone does not help when the per-token baseline lacks a learned value function\"）是推测性的，且论文自己承认 \"a definitive comparison would require matched compute budgets and hyperparameter sweeps\"。REINFORCE++ 的失败可能来自多种原因（per-token baseline 质量、normalization 方式、梯度方差），论文未能分离这些因素。此外，REINFORCE++ 实验未进行 OOD 评估，进一步削弱了其信息量。\n\n---\n\n### Missing References\n\n**[AGREE] R2-Ref1: RLOO (Ahmadian et al., 2024)**\n同意。RLOO 作为 REINFORCE 的 leave-one-out 变体，与 episode-level GRPO 的 group normalization 有直接关联。我在自己的审稿中也建议引用此工作（以 \"Back to Basics\" 标题）。\n\n**[REBUT] R2-Ref2: COMA, QMIX**\n部分不同意。论文在 Appendix A.3 已经讨论了 multi-agent credit assignment 的类比（\"Step-independent windows can be understood through cooperative multi-agent games\"），且引用了 counterfactual baselines 和 value decomposition 的概念。COMA 和 QMIX 作为具体方法可以补充引用以增强此讨论，但缺失它们不构成引用遗漏——论文的 contribution 不在 multi-agent RL 领域，Appendix A.3 的讨论足以建立概念联系。不过如果空间允许，加入 COMA/QMIX 引用确实能加强 Appendix A.3 的 scholarly completeness。\n\n---\n\n### 总体评估一致性\n\nR2 给出 Overall 3.0 (Findings), Soundness 3.0, Excitement 2.5。\n\n我给出 Overall 3.0 (Findings), Soundness 3.0, Excitement 3.0。\n\n**分歧点**：Excitement。R2 给 2.5，主要基于方法新颖性不足（W1）。我给 3.0，理由是：虽然 episode-level GRPO 本身不新颖，但 **M1/M2 诊断框架对从业者有实际指导价值**——它能帮助判断何时使用 step-level vs episode-level 方法，何时 M1 是瓶颈 vs M2 是瓶颈（Appendix E method selection guide）。对于一篇定位为诊断/分析的论文，excitement 应基于诊断的 insight 质量而非修复方案的新颖性。但 R2 的担忧也有道理：如果论文不能更清晰地将贡献定位在诊断侧，则 excitement 评估会被方法新颖性拉低。\n\n**一致点**：Soundness 3.0、Overall 3.0 (Findings) 完全一致。核心共识是——诊断有价值但证据不够完整（Cell C 缺失、2-seed 析因、overclaiming），适合 Findings 而非主会议。\n",
  "reviewer_id": "1",
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Strengths\n\n**[AGREE] R2-S1 (析因实验设计)**\n同意。部分析因设计是本文方法论上的亮点，比典型 ablation study 更有结构意识。我在自己的审稿中也将此列为 S2。\n\n**[AGREE] R2-S2 (科学诚实的报告)**\n同意。36% 泛化率、seed 变异性、Cell C 不稳定性的坦诚披露是值得肯定的。11-seed 评估本身就超过了领域平均水平。\n\n**[AGREE] R2-S3 (理论与实验对照)**\n同意。三项验证指标（sign-episode correlation、credit agreement、P(correct|update)）+ break-even magnitude ratio (2.6 < 4.2) 构成了多角度证据（Section 5.4）。\n\n**[AGREE] R2-S4 (写作和可视化)**\n同意。论文结构清晰，Figure 1 的示意图有效传达了核心思想。\n\n**[AGREE] R2-S5 (跨环境/规模验证)**\n同意。单 seed 是限制，但提供了 directional evidence。\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-W1: Episode-level GRPO 新颖性有限**\n同意这一判断，但我认为严重性应适当校准。\n\n理由：论文自身在 Section 3.4 明确写道 \"step-independent windowing is the deviation introduced by multi-turn agent frameworks\"，Section 6 也说 \"Episode-level GRPO is equivalent to REINFORCE where the group mean μ replaces b(s)\"（Appendix A.3）。这说明 \"correction\" 本质上是回退到标准 GRPO/REINFORCE，不是方法论创新。标题中 \"Episode-Level Correction\" 确实暗示了超出论文实际贡献的方法论新颖性。\n\n**但需校准**：如果论文定位为 **诊断/分析** 贡献而非方法贡献，则修复方案的简洁性反而是优势（Occam's razor——诊断准确了，修复自然简单）。问题在于标题和写作框架未能清晰地将贡献定位在诊断侧。建议将此评估为 **Should-Fix**（修改标题和定位措辞）而非 Critical Must-Fix，因为核心诊断贡献不受影响。\n\n**[AGREE] R2-W2: Abstract/Intro 的 overclaiming**\n强烈同意。这是我在 Minor M4 中也提到但严重性可能评估偏低的问题。R2 的分析更精确：\n\n补充关键证据：根据 Table 2 的数据，11 seed 的 OOD 中位数为 **12.69%**（排序后第 6 个值），远低于论文报告的 mean 17.7%。中位数仅比 SFT baseline (6.72%) 高 ~6pp，且对应的 seed (seed42/seed100) 均被分类为 \"Collapsed\" 或 \"Stagnant\"（Fisher exact test NS）。这意味着 **过半数 seeds 未达到统计显著的 OOD 改善**。\n\n\"structurally eliminates both failure modes\" 在技术上是正确的（episode-level 训练确实消除了 M1 和 M2 的结构性原因），但与 36% 泛化率并置时产生强烈的误导效果。Abstract 应报告 median 或明确说明 mean 被少数高 seed 拉高。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W3: Cell C 缺失削弱析因完整性**\n完全同意。我在自己的审稿中将此列为 W1 (Critical)，给出了更详细的分析。Cell C 的 NaN 不稳定性（Appendix D: 六种超参数配置均发散）本身暗示 M1 可能通过限制序列长度和梯度方差起到无意中的正则化作用——即 M1 和 M2 存在非加性交互。论文在 Section 6 承认 \"our factorial interpretation assumes approximate separability\"，但如果这一假设不成立，则整个 A→B→D 因果链的推断基础被动摇。\n\n**[AGREE] R2-W4: 实验范围偏窄**\n同意。我在自己的审稿中也提出了跨环境验证薄弱（my W5）和缺乏同期方法对比（my W6）的问题。补充一点：所有 OOD 评估均为单次 τ=0.4 是一个值得强调的限制——Appendix G 的评估方差分析仅基于 **一个 stagnant seed** (seed200)，不能代表 generalized seeds 的评估方差。\n\n**[AGREE] R2-W5: Binary theory vs ternary experiment gap**\n同意。我在 W4 中详细讨论了这一点。补充：19.1% 和 52.1% 不仅数值差距巨大，而且反映的是 **质的不同** 的失败模式——binary 下是 deterministic misattribution（符号几乎完全由 episode 结果决定），ternary 下是 near-random noise（52.1% ≈ 50%，advantage 符号几乎不携带局部信息）。论文的理论分析对实验设置的解释力因此受限。\n\n**[AGREE] R2-W6: 与同期工作关系缺乏实证验证**\n同意。Section 6 声称 \"HCAPO and GiGPO succeed with h=2 by eliminating M2 through finer-grained credit, consistent with our framework's prediction\"，但这只是事后解释（post-hoc rationalization），不是框架预测能力的验证。真正的验证需要：(a) 在相同设置下实验对比；(b) 或框架对新方法的 **先验预测**，而非对已发表结果的事后一致性声称。\n\n---\n\n### Minor\n\n**[AGREE] R2-M1: Table 1 Cell B OOD 仅单 seed**\n同意。我在 W2 和 M1 中也标记了这个问题。n=1 的 OOD 评估不构成统计证据，尤其考虑到 11-seed 评估展示了高 seed 间变异性。\n\n**[AGREE] R2-M2: Figure 3(b) h=10 报告方式**\n同意。h=10 的两 seed 差异（6.25% vs. 21.9%）非常大，仅报告均值 (14.1%) 掩盖了这种不确定性。论文应同时报告两个单 seed 值，或用 error bar 标注。实际上 Figure 3(b) 的 black dots 确实展示了个体 seed，这是好的，但主文讨论（Section 5.3 末尾）只提了均值。\n\n**[REBUT] R2-M3: 12.5% SFT baseline 偏低**\n部分不同意。\n\n理由：R2 认为低 baseline 可能限制诊断的普适性。但 Proposition 2 的分析恰恰表明 sign misattribution 的严重性 **随 p 下降而增加**（Equation 4: P(correct|update) 在 p=5% 时仅 14.9%，p=50% 时 50.2%）。论文在 Section 4 \"Severity scales with task difficulty\" 段落中明确讨论了这一点。因此，低 baseline 设置实际上是 **最能暴露 M2 问题的设置**，而非削弱诊断的设置。\n\n不过 R2 的隐含关切也有道理：论文需要证明 M2 在更高 baseline (p > 30%) 的设置中仍然是 **实际可观察的** 问题（而非仅理论预测）。8B 实验的 SFT baseline 为 80.6%，此时 P(correct|update) ≈ 80.6%，sign misattribution 应不再是主要问题——然而 8B Cell A 仍然崩溃。这意味着 collapse 在高 baseline 下可能由 M1 主导而非 M2，削弱了 \"dual mechanism\" 框架在不同 baseline 水平下的统一解释力。这一分析论文未展开讨论，我认为是一个有价值的延伸，但更适合作为 future work 而非 must-fix。\n\n**[AGREE] R2-M4: γ 值主文未给出**\n同意。Equation 2 使用了 γ 但 γ=0.95 仅在 Appendix B (Table 3) 给出。主文应在 Section 3.2 或 Section 5.1 中明确 γ 值。\n\n**[AGREE] R2-M5: AI assistance 声明**\n同意。Appendix H 的 AI 使用声明（Claude as coding/writing/literature assistant）透明度好。\n\n---\n\n### Questions\n\n**[AGREE] R2-Q1: 11 seed OOD 中位数**\n同意这是一个关键统计量。如上文计算，中位数为 **12.69%**，远低于 mean 17.7%。分布是右偏的（4 个 generalized seeds 拉高均值）。论文仅报告 mean 而未报告 median 确实不够透明。\n\n**[AGREE] R2-Q2: 8B seed 数**\n同意这是一个重要问题。论文明确说 \"single-seed\"（Section 5.6），但单 seed 的 90.3% OOD 被用作 cross-scale validation 的核心证据，证据强度极弱。\n\n**[AGREE] R2-Q3: Cell C NaN 与 M1/M2 框架**\n同意这是一个深层问题。我在自己的 W1 中也详细讨论了这一点。Cell C 的 NaN 可能代表：(a) M1 确实有正则化副作用（通过限制序列长度和梯度方差），即 M1 和 M2 存在交互而非独立；(b) 或者存在 M1/M2 框架之外的第三种机制（长序列 + per-window normalization 的数值不稳定性）。无论哪种解释，都挑战了论文的 \"两种独立机制\" 框架。论文在 Appendix D 将原因归结为 \"full-length sequences with step-level advantage normalization produces extreme advantage magnitudes\"，但未充分讨论这对框架本身的含义。\n\n**[REBUT] R2-Q4: 19.1% vs 52.1% 哪个更准确**\n我认为这个问题的答案比 R2 暗示的更微妙。\n\n理由：这两个数字衡量的是 **不同的量**（论文在 Section 5.4 和 Appendix A.2 中明确区分）：\n- 19.1% = P(correct | update)：binary reward 下，非零梯度更新中正确符号的比例上界。这是一个 **理论 bound**，衡量的是梯度方向的正确性。\n- 52.1% = credit agreement rate：ternary reward 下，valid-action windows 获得正确 advantage 符号的比例。这是一个 **经验指标**，衡量的是 advantage 符号与 action validity proxy 的一致性。\n\n两者不可直接比较。对实际训练动态而言，52.1%（ternary）更接近实验设置，但它衡量的不是梯度正确性（因为使用了 action validity 作为 proxy）。19.1%（binary）更 precisely 衡量梯度正确性，但假设与实验不符。**两者都不完美**——论文的贡献是从两个互补角度确认 credit assignment 失败，而非提供单一精确估计。\n\n**[AGREE] R2-Q5: Dense reward 环境测试 M2 边界**\n同意。论文的 dense reward 实验（Appendix D）是在 ALFWorld 中 **人工添加** per-step bonus (+0.15/valid action)，结果是 reward gaming（action validity ↑ 到 97.5%，task success 维持 0%）。但 R2 的问题更深入：在 **天然具有 dense reward 信号** 的环境中，M2 的严重程度是否降低？Proposition 2 的 bound 依赖于 binary episode reward 假设，如果环境提供真正的 per-step reward signal（而非人工 shaping），M2 可能不再是主要失败模式。论文未在此类环境中测试，这是一个有价值的 future work 方向。\n\n**[AGREE] R2-Q6: REINFORCE++ 为何不帮助**\n同意这是一个需要更深入解释的问题。论文在 Appendix D 的解释（\"per-token advantage normalization alone does not help when the per-token baseline lacks a learned value function\"）是推测性的，且论文自己承认 \"a definitive comparison would require matched compute budgets and hyperparameter sweeps\"。REINFORCE++ 的失败可能来自多种原因（per-token baseline 质量、normalization 方式、梯度方差），论文未能分离这些因素。此外，REINFORCE++ 实验未进行 OOD 评估，进一步削弱了其信息量。\n\n---\n\n### Missing References\n\n**[AGREE] R2-Ref1: RLOO (Ahmadian et al., 2024)**\n同意。RLOO 作为 REINFORCE 的 leave-one-out 变体，与 episode-level GRPO 的 group normalization 有直接关联。我在自己的审稿中也建议引用此工作（以 \"Back to Basics\" 标题）。\n\n**[REBUT] R2-Ref2: COMA, QMIX**\n部分不同意。论文在 Appendix A.3 已经讨论了 multi-agent credit assignment 的类比（\"Step-independent windows can be understood through cooperative multi-agent games\"），且引用了 counterfactual baselines 和 value decomposition 的概念。COMA 和 QMIX 作为具体方法可以补充引用以增强此讨论，但缺失它们不构成引用遗漏——论文的 contribution 不在 multi-agent RL 领域，Appendix A.3 的讨论足以建立概念联系。不过如果空间允许，加入 COMA/QMIX 引用确实能加强 Appendix A.3 的 scholarly completeness。\n\n---\n\n### 总体评估一致性\n\nR2 给出 Overall 3.0 (Findings), Soundness 3.0, Excitement 2.5。\n\n我给出 Overall 3.0 (Findings), Soundness 3.0, Excitement 3.0。\n\n**分歧点**：Excitement。R2 给 2.5，主要基于方法新颖性不足（W1）。我给 3.0，理由是：虽然 episode-level GRPO 本身不新颖，但 **M1/M2 诊断框架对从业者有实际指导价值**——它能帮助判断何时使用 step-level vs episode-level 方法，何时 M1 是瓶颈 vs M2 是瓶颈（Appendix E method selection guide）。对于一篇定位为诊断/分析的论文，excitement 应基于诊断的 insight 质量而非修复方案的新颖性。但 R2 的担忧也有道理：如果论文不能更清晰地将贡献定位在诊断侧，则 excitement 评估会被方法新颖性拉低。\n\n**一致点**：Soundness 3.0、Overall 3.0 (Findings) 完全一致。核心共识是——诊断有价值但证据不够完整（Cell C 缺失、2-seed 析因、overclaiming），适合 Findings 而非主会议。\n",
    "reviewer_id": "1",
    "project": "cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-25T21:30:47.137509+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3867
}
```

</details>

---


### Assistant

_source line 526 · 2026-05-25T21:30:55.008901+00:00_

已提交对 Reviewer 2 的逐条回应。

核心立场：与 R2 在 Soundness 3.0 和 Overall 3.0 (Findings) 上完全一致。两处分歧——(1) Excitement 我给 3.0 vs R2 的 2.5，因为诊断框架本身有实用价值；(2) M3 (低 baseline 普适性) 我部分反驳，因为低 p 恰好是 M2 最严重的区间，但同时指出 8B (p≈80%) 的 collapse 可能由 M1 主导，暗示框架在不同 baseline 下的解释力可能不统一。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1"
}
```

</details>

---
