# Reviewer 1 coordination

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 250
- **Recorded user turns:** 8
- **Tool calls:** 117
- **Original source:** `logs/chats/feishu_group_oc_8b9aa92fafaf69b48d2c44b41c2fe9d9_reviewer_1.jsonl`
- **Structured JSON:** [`baed9ef37966affef3f3.json`](../../sessions/ba/baed9ef37966affef3f3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-24T14:55:51.263669+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查本文的**方法严谨性、实验设计和统计分析**。

## Venue 信息
- **目标**: EMNLP 2026 via ACL Rolling Review
- **Deadline**: 2026-05-25
- **格式**: Long paper, 8页正文限制, unlimited references, mandatory limitations section (不计入页数)
- **模板**: ACL template with [review] option
- **匿名规则**: Double-blind

## 论文信息
- **标题**: Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations
- **论文路径**: projects/clkc_mech_interp/docs/paper/main.tex
- **PDF**: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/submitted.pdf

## 你的审查侧重

请重点评估以下方面：

1. **实验设计的合理性**：
   - ConflictQA 数据集的使用是否合理？parametric knowledge verification 流程是否充分？
   - 跨语言翻译流程（Qwen3-8B pipeline）是否引入 confound？COMET 验证是否充分？
   - 三模型对比的公平性：样本量差异（Llama 1368 vs Qwen 966 vs Gemma 1590）是否影响结论？

2. **统计方法**：
   - Fisher's exact test + Bonferroni correction 的使用是否恰当？
   - Bootstrap CI (n=2000) 是否足够？paired bootstrap 的实现是否正确？
   - Steering 实验中 multiple comparison 的处理（k=10 alpha values, Bonferroni threshold 0.005）
   - 单种子实验的可靠性（probing 结果）

3. **因果推断的严谨性**：
   - Representation steering 的方法论是否充分支持因果声明？
   - Random direction control 是否是合适的对照？
   - L13 成功 vs L28 失败的解释是否有 confounding factors？
   - "Detection ≠ Decision" 的 claim 是否被数据充分支持？

4. **跨模型泛化性**：
   - Steering 仅在 Llama L13 成功，Qwen/Gemma 全部 negative——论文如何处理这个"N=1 模型"问题？
   - Gemma 匹配条件重跑的 N=88 是否 underpowered？

5. **Confound exclusion**：
   - COMET tercile ablation 是否充分排除了翻译质量 confound？
   - Token overlap analysis 是否全面？
   - XNLI baseline comparison 的设计是否能充分支持 "not conflict-specific" 的结论？

请按以下格式输出审稿意见：
- **Summary**: 2-3 句概述
- **Strengths**: 逐条列出（S1, S2, ...）
- **Weaknesses**: 逐条列出（W1, W2, ...），标注严重程度 [Critical/Major/Minor]
- **Questions**: 需要作者澄清的问题（Q1, Q2, ...）
- **Missing References**: 遗漏的重要相关工作
- **Overall Assessment**: 评分和简短理由

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-24T14:56:01.598044+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
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

_source line 3 · 2026-05-24T14:56:01.698837+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-24T14:56:11.299258+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/submitted.pdf",
  "project": "clkc_mech_interp",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/submitted.pdf",
    "project": "clkc_mech_interp",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T14:56:11.451089+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria dimensions"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T14:56:12.808079+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 451.9}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.1}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 546.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.6}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 480.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_
…[truncated 317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1508
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-24T14:56:19.437026+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

I found information about the ACL Rolling Review (ARR) 2026 reviewer guidelines and review form. Here's what the search results reveal:

## Reviewer Guidelines

If reviewers did not check some major parts such as proofs, they should state this in the review, as this information is helpful for the Area Chair to understand what aspects of the paper were not reviewed.

## Review Form Criteria

The review form includes several scoring dimensions:

- 5 = Consider for Award: Papers that could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)
- 2 = Resubmit next cycle: Papers needing substantial revisions that can be completed by the next ARR cycle

…[truncated 644 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7985
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-24T14:56:26.180761+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract ALL review form dimensions/criteria with their scoring scales. I need the complete list of evaluation dimensions (e.g., soundness, excitement, reproducibility, etc.), each with its full scoring scale description. Return everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract ALL review form dimensions/criteria with their scoring scales. I need the complete list of evaluation dimensions (e.g., soundness, excitement, reproducibility, etc.), each with its full scoring scale description. Return everything verbatim."
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T14:56:28.090036+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should evaluate, how to score each dimension, what constitutes a good review, and any specific instructions about methodology/experimental evaluation. Return the key points verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should evaluate, how to score each dimension, what constitutes a good review, and any specific instructions about methodology/experimental evaluation. Return the key points verbatim."
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T14:56:28.993577+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T14:56:29.497413+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T14:56:29.951278+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T14:56:29.951729+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T14:56:30.556977+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T14:56:30.557398+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T14:56:30.759089+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-24T14:56:31.312512+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T14:56:35.779224+00:00_

# ARR Reviewer Guidelines: Key Points

## What Reviewers Should Evaluate

Reviewers assess papers across multiple dimensions:

**Soundness**: Technical validity and methodological rigor. The guidelines state: "Soundness scores must be justified by the text of the review."

**Excitement**: Personal interest level, separate from soundness assessment. This reflects subjective taste rather than objective quality.

**Overall Recommendation**: Composite judgment on whether a paper merits acceptance, considering soundness, novelty, impact, and reproducibility.

## Scoring Requirements

Scores must align with review content. Per guidelines: "If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation."

Papers need sufficient soundness for Findings/main conference tracks, though reviewers may rate papers as significant despite lacking personal excitement.

## Characteristics of Strong Reviews

**Specificity is essential.** Instead of "missing relevant references," cite which ones: "missing references X, Y, Z."

**Professional tone matters.** Reviews should be constructive, not sarcastic. Guidelines note: "Write the review you would like to get yourself."

**Evidence-based critique.** Claims require justification. Generic criticisms like "not novel" demand specific prior work citations.

## Methodology/Experimental Evaluation

Reviewers should verify:

- **Reproducibility details**: Sufficient hyperparameters, code/data availability plans disclosed
- **Statistical rigor**: Confidence intervals, significance tests where appropriate
- **Fair baselines**: Adequately tuned comparisons; closed-source model comparisons only if directly relevant
- **Appropriate scope**: Claims match evidence presented; generalizations justified

Guidelines warn against requiring "extra experiments" beyond what substantiates the paper's actual claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7689
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-24T14:56:44.781875+00:00_

# ACL Rolling Review Form – Evaluation Dimensions

## 1. **Reviewer Confidence**
"5 = Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- 4 = Quite sure
- 3 = Pretty sure
- 2 = Willing to defend evaluation
- "1 = Not my area, or paper is very hard to understand."

## 2. **Soundness**
- "5 = Excellent: This study is one of the most thorough I have seen, given its type."
- 4 = Strong
- 3 = Acceptable
- "2 = Poor: Some of the main claims are not sufficiently supported."
- "1 = Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
- "5 = Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- 4 = Exciting
- 3 = Interesting
- 2 = Potentially Interesting
- "1 = Not Exciting: this paper does not resonate with me."

## 4. **Overall Assessment**
- "5 = Consider for Award: top 2.5% papers"
- 4.5 = Borderline Award
- 4 = Conference
- 3.5 = Borderline Conference
- 3 = Findings
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle
- 1.5 = Resubmit after next cycle
- "1 = Do not resubmit"

## 5. **Reproducibility**
- "5 = They could easily reproduce the results."
- 4 = Mostly reproducible
- 3 = Reproducible with difficulty
- "2 = They would be hard pressed to reproduce the results."
- "1 = They would not be able to reproduce the results."

## 6. **Datasets**
- "5 = Enabling: should affect other people's choice of research projects."
- 4 = Useful
- 3 = Potentially useful
- "2 = Documentary: useful to study or replicate research."
- "1 = No usable datasets submitted."

## 7. **Software**
- "5 = Enabling: should affect other people's choice of research projects."
- 4 = Useful
- 3 = Potentially useful
- "2 = Documentary: useful to study or replicate research."
- "1 = No usable software released."

## 8. **Author Identity Knowledge**
- "5 = From a violation of double-blind-submission rules, I know/can guess at least one author's name."
- 4 = F
…[truncated 119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 18601
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-24T14:56:52.751664+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T14:56:52.955048+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-24T14:56:53.005801+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-24T14:56:53.006270+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-24T14:56:53.963023+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-24T14:56:53.963439+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-24T14:56:54.417179+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1665
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-24T14:56:55.851092+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2896
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-24T14:56:55.952704+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2946
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-24T14:56:56.054678+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3048
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-24T14:56:56.257534+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2294
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-24T14:56:56.358662+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2395
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-24T14:58:53.431837+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-24T14:58:53.482691+00:00_

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
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	\usepackage{subcaption}
17	
18	\title{Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	\input{abstract}
27	\end{abstract}
28	
29	\input{introduction}
30	
31	\input{related_work}
32	
33	\input{method}
34	
35	\input{experiments}
36	
37	\input{discussion}
38	
39	\input{conclusion}
40	
41	\input{limitations}
42	
43	\appendix
44	
45	\section{Use of AI Assistants}
46	\label{app:ai-assistants}
47	
48	We used Claude (Anthropic) as an AI coding and writing assistant
49	throughout this work. Specifically:
50	\begin{itemize}
51	    \item \textbf{Code:} drafting experiment scripts, data-processing
52	    pipelines, and analysis utilities; debugging and refactoring.
53	    \item \textbf{Writing:} drafting and revising paper sections,
54	    polishing prose, and reformatting \LaTeX{}.
55	    \item \textbf{Literature:} summarizing related papers to inform
56	    related-work section.
57	\end{itemize}
58	
59	\section{Fine-Grained Causal Boundary Analysis}
60	\label{app:boundary}
61	
62	Table~\ref{tab:boundary} reports steering results across the full layer gradient from an independent replication ($N = 201$, Llama-3.1-8B-Instruct, RTX PRO 6000).
63	
64	\begin{table}[h]
65	\centering
66	\caption{Causal boundary steering results (independently sampled, $N = 201$, Llama-3.1-8B-Instruct). Bonf.\ Sig.\ $\alpha$s: number of $\alpha$ values reaching significance after Bonferroni correction out of 6 tested.}
67	\label{tab:boundary}
68	\small
69	\resizebox{\columnwidth}{!}{%
70	\begin{t
…[truncated 2623 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-24T14:58:58.805813+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-24T14:58:58.808333+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/acl_latex.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-24T14:59:02.423204+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-24T14:59:02.978629+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Our pipeline proceeds from data construction through probing and steering, formalized below.
5	
6	\subsection{Task Formulation}
7	\label{sec:task}
8	
9	Given a context passage $c$ and question $q$, the model produces an answer that is either \emph{contextual} (derived from $c$) or \emph{parametric} (from pre-trained knowledge).
10	When $c$ contradicts parametric knowledge, the choice constitutes a knowledge conflict.
11	We train a logistic regression probe $f_\theta(\mathbf{h}_l) = \sigma(\mathbf{w}_l^\top \mathbf{h}_l + b_l)$ on the last-token residual stream representation $\mathbf{h}_l \in \mathbb{R}^d$ at layer $l$ to predict a binary label $y \in \{\text{contextual}, \text{parametric}\}$.
12	
13	\subsection{Data Construction}
14	\label{sec:data}
15	
16	We build on ConflictQA \citep{xie2024adaptive}, which pairs questions with context passages contradicting the model's parametric knowledge.
17	We filter samples by querying each model without context and retaining only those answered correctly, yielding 1{,}368 samples for Llama \citep{grattafiori2024llama}, 966 for Qwen \citep{yang2024qwen25}, and 1{,}590 for Gemma \citep{team2024gemma} (80/20 train/test split with stratification).
18	For cross-lingual transfer, we translate all inputs into Chinese using a Qwen3-8B pipeline, with quality validated by COMET \citep{rei2020comet} back-translation scores used in confound analysis (\S\ref{sec:confound_method}).
19	
20	\subsection{Activation Extraction and Probing}
21	\label{sec:extraction}
22	
23	For each input, we construct English and Chinese versions and extract the last-token residual stream $\mathbf{h}_l \in \mathbb{R}^d$ at every layer $l$ ($L = 32$ for Llama, $36$ for Qwen, $42$ for Gemma; $d = 4096$ for Llama/Qwen, $3584$ for Gemma), following the last-token aggregation principle \citep{belinkov2022probing}.
24	We record the model's answer and assign binary labels (contextual vs.\ parametric).
25	
26	\label{sec:pro
…[truncated 2768 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 555
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-24T14:59:02.979666+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-24T14:59:03.532241+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We probe three instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \citep{grattafiori2024llama}, Qwen3-8B (36 layers, hidden dimension 4096) \citep{yang2024qwen25}, and Gemma-2-9B-IT (42 layers, hidden dimension 3584) \citep{team2024gemma}.
9	
10	\paragraph{Dataset.}
11	We use ConflictQA \citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.
12	After verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test), 966 for Qwen (773 train / 193 test), and 1{,}590 for Gemma (1{,}274 train / 316 test), split 80/20 with stratification.
13	
14	\paragraph{Translation.}
15	We translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\to$ZH), with quality validated by COMET \citep{rei2020comet} back-translation scores.
16	
17	\paragraph{Probing.}
18	For each layer $l$, we train a logistic regression probe on the last-token residual stream representation $\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.
19	We report balanced accuracy to account for class imbalance.
20	All confidence intervals (CIs) are computed via bootstrap resampling with paired differences for asymmetry estimation.
21	
22	\paragraph{Non-conflict baseline.}
23	To test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \citep{conneau2018xnli}, classifying entailment versus contradiction.
24	
25	\subsection{Within-Language Conflict Detection}
26	\label{sec:within_lang}
27	
28	Table~\ref{tab:main_results} reports balanced accuracy for al
…[truncated 13468 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-24T14:59:03.532801+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-24T14:59:03.884383+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Detection and decision occur at different layers.}
5	Our central mechanistic finding is a dissociation between where conflict signals become linearly readable and where they exert causal influence on model behavior.
6	In Llama, probe accuracy on EN$\to$EN peaks at layer~28 (88\% depth), yet representation steering succeeds only at layer~13 (41\% depth; Fisher $p = 0.002$), and all late-layer interventions produce no significant behavioral change ($p > 0.3$).
7	This dissociation has a cross-lingual counterpart: the Llama ZH$\to$ZH probe peaks at L13, the same layer where steering succeeds.
8	Mid-layers thus serve a dual role as the site of cross-lingual alignment \citep{muller2021first, wendler2024llamas} and the locus where conflict signals acquire causal force.
9	The EN$\to$EN peak at L28 is best understood as a diagnostic readout, a linearly readable trace of a decision that has already been made upstream.
10	A practical implication follows: the probe peak layer is not the causal layer, and intervention experiments that target only the highest-accuracy layer risk missing the computationally relevant site.
11	Cross-layer sweeps, as conducted here, are necessary to locate the true decision point.
12	Steering failed in both Qwen (L14, 39\%; $n = 131$, best $p = 0.785$) and Gemma (L17, 40\%; $n = 171$, best $p = 0.448$), with zero directional flips in both cases.
13	The Gemma result is particularly informative: its 88.9\% probe accuracy---the highest among all three models---rules out probe quality as a confound, since the direction that best separates conflict labels carries no causal influence despite being highly discriminative.
14	This establishes that the causal influence of the probe direction is architecture-specific, not a general property of mid-layer computation.
15	
16	\paragraph{Conflict signals are encoded in a general cross-lingual space.}
17	The ZH$\to$EN transfer advantage is consistent ac
…[truncated 4387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-24T14:59:03.985258+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-24T14:59:04.035795+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our study has three main limitations.
5	First, we evaluate only one language pair (English-Chinese).
6	While the consistent patterns across three architecturally distinct models are encouraging, typologically diverse language pairs (e.g., English-German, English-Japanese) are needed to assess the generality of our findings.
7	Second, causal steering succeeded only in Llama at L13.
8	Gemma L17 steering failed despite the highest probe accuracy among all three models (88.9\%, $n = 171$), ruling out probe quality as a confound and constituting an informative negative that confirms the architecture-specificity of the effect.
9	Qwen L14 ($n = 131$, probe accuracy 71.0\%) was also negative with zero directional flips.
10	Third, the effective dataset size (966 to 1,590 samples per model after parametric knowledge verification) is constrained by the requirement that each model must correctly answer the question without context.
11	This verification step is necessary to ensure genuine knowledge conflicts, but it limits the statistical power of our analyses, particularly for stratified comparisons such as the COMET tercile ablation.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-24T14:59:08.354512+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-24T14:59:08.505572+00:00_

1	When multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation can determine the model's answer. Behavioral studies attribute this to linguistic affinity, but the internal mechanism remains unknown: how is the conflict signal encoded, does it share structure with general cross-lingual representations, and does detectability imply causal influence on resolution?
2	
3	We probe residual stream representations in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT. Our analysis combines cross-lingual transfer, a non-conflict baseline on XNLI, confound exclusion for translation quality and token overlap, and representation steering. Conflict signals are linearly detectable across languages, and cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English ${\sim}$7 percentage points more accurately than the reverse. This asymmetry matches the XNLI non-conflict baseline in both magnitude and direction, with overlapping confidence intervals; it inherits from the model's general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision: in Llama, the probe signal peaks at late layers (88\% depth), but representation steering achieves causal influence only at a mid-layer (41\% depth); analogous Qwen and Gemma steering yields no significant effect. These findings demonstrate that linear detectability does not imply causal relevance, with direct implications for probe-based intervention research.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-24T14:59:08.506174+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-24T14:59:08.606921+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation can determine which answer the model produces.
5	\citet{zhao2026when} showed that linguistic affinity dominates conflict resolution in entity-centric factual conflicts, with models preferring answers from linguistically closer sources.
6	Yet the internal mechanism behind this behavior remains opaque: how does the model encode the conflict signal?
7	Can it be detected from internal representations?
8	And if detectable, does the detected signal causally influence the model's resolution strategy?
9	These questions sit at the intersection of mechanistic interpretability and multilingual NLP, and answering them requires moving beyond behavioral observations to probe model internals directly.
10	
11	Existing work on probing knowledge conflict signals has been limited to monolingual settings.
12	\citet{zhao2024analysing} showed that residual stream representations carry linearly detectable conflict signals in English, and \citet{brink2026probing} performed knowledge attribution probing to localize factual associations within model parameters.
13	Extending these approaches cross-lingually introduces additional challenges.
14	Translation quality may confound probe transfer: a poor translation could alter conflict detection for reasons unrelated to the conflict signal itself.
15	Token overlap between languages, even when minimal, could provide a shortcut for cross-lingual probes.
16	Observed asymmetries in transfer accuracy may reflect general cross-lingual properties rather than conflict-specific phenomena, and disentangling these sources requires careful baseline comparisons.
17	Beyond detectability, a fundamental limitation of probing is that it establishes correlation, not causation \citep{hewitt2019designing}.
18	\citet{basu2026interpretability} demonstrated that even near-perfect probe ac
…[truncated 3734 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-24T15:02:29.259362+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见（方法严谨性、实验设计和统计分析）\n\n### 总体评分\n\n**Overall Assessment**: 3.5 — Borderline Conference\n\n**一句话总结**: Probing 分析扎实且 confound exclusion 设计精心，但核心因果声明（Detection ≠ Decision）仅在单模型单层成立，多重比较校正方案存在争议，限制了结论的泛化性。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | Probing 实验设计合理，confound exclusion 系统化；但 steering 的多重比较校正不完整，\"非冲突特异\"声明缺乏正式等价性检验，单种子实验削弱可靠性 |\n| Excitement | 3/5 | 问题重要且及时，XNLI baseline 对比有方法论启示；但 steering 仅 Llama 成功，核心因果发现的泛化性大打折扣 |\n| Reproducibility | 3/5 | 提供了关键参数；但单种子、未公开代码/数据、probe 正则化系数未报告 |\n| Reviewer Confidence | 4/5 | 熟悉 probing methodology、representation steering 和跨语言 NLP |\n\n### Must-Fix 问题\n\n**N1** [Critical] **Steering 实验的多重比较校正不完整，核心 p=0.002 可能不保真**\n- 位置: Section 3.6, Section 4.6\n- 主实验在 3 个层（L13, L18, L28）各测试 k=10 个 α 值，共 30 次检验。Bonferroni 仅在层内应用（0.05/10=0.005），未跨层校正。若全 family 校正（0.05/30≈0.00167），L13 正方向 p=0.002 不再显著。独立复现（N=201）缓解但非预注册。\n- 建议: 明确说明为什么层间不需要校正（如预注册），或采用 FDR 校正，或报告完整 family-wise p 值。\n\n**N2** [Critical] **因果声明的泛化性：N=1 模型问题**\n- 位置: Abstract, Section 4.6 \"Detection ≠ Decision\", Discussion §5\n- Steering 仅 Llama L13 成功，Qwen/Gemma 全部阴性（零翻转）。但论文框架性表述暗示这是 general principle。无法区分：Llama 特有特征 vs 线性 steering 局限 vs 统计偶然。Gemma 88.9% probe accuracy 下零效应对 \"probe direction = causal direction\" 构成反证。\n- 建议: 将 \"Detection ≠ Decision\" 限定为 Llama-specific，讨论 Qwen/Gemma 失败是否意味着因果结构可能非线性。\n\n### Should-Fix 问题\n\n**W1** [Major] 单种子实验——Table 1 所有结果基于单次 split，未报告多种子 mean ± std，peak layer 可能因 split 变化。\n\n**W2** [Major] \"非冲突特异\"声明仅基于 CI 重叠，缺乏正式 TOST 等价性检验或 difference-in-differences 检验。\n\n**W3** [Major] COMET tercile 分析统计功效不足（每 tercile 64-91 样本），p=0.695/0.761 反映 power 不足而非无效应。Gemma 未报告。\n\n**W4** [Major] 跨模型比较在不同样本子集上进行（Llama 1368, Qwen 966, Gemma 1590），未在交集上验证。\n\n**W5** [Minor] 翻译模型（Qwen3-8B）与实验对象重叠，未讨论此 confound。\n\n**W6** [Minor] Table 3 caption \"p < 0.05\" 与正文 Bonferroni 阈值 0.005 不一致。\n\n### Questions\n\nQ1: Bonferroni 为什么按层而非按整个 steering 实验校正？是否有先验理由？\nQ2: 独立复现（N=201）是否在观察到 L13 主实验结果之后进行？\nQ3: Gemma L21 cross-task transfer dip（0.730）与 alternating attention 架构的关系？\nQ4: L13 和 L28 的 w_probe cosine similarity 是多少？\nQ5: Qwen Δ_asym CI 包含零，如何支撑 \"consistent across all three architectures\"？\n\n### Missing References\n- Turner, Thacker, and Fry (2023): \"Activation Addition\"——steering 核心方法论文献\n- Marks et al. (2024): \"Geometry of Truth\"——与跨任务 probe direction 共享分析直接相关\n\n### 主要优势\n- S1: 首次多架构/多语言知识冲突信号的系统性 probing 研究\n- S2: Confound exclusion pipeline 设计周全（COMET/token overlap/XNLI/EN-DE）\n- S3: XNLI baseline 对比有方法论启示价值\n- S4: 对 negative results 的诚实处理（Gemma informative negative）\n- S5: 独立复现（N=201）展示 causal gradient 空间精度\n- S6: 写作清晰，结构完整",
  "reviewer_id": "1",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见（方法严谨性、实验设计和统计分析）\n\n### 总体评分\n\n**Overall Assessment**: 3.5 — Borderline Conference\n\n**一句话总结**: Probing 分析扎实且 confound exclusion 设计精心，但核心因果声明（Detection ≠ Decision）仅在单模型单层成立，多重比较校正方案存在争议，限制了结论的泛化性。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | Probing 实验设计合理，confound exclusion 系统化；但 steering 的多重比较校正不完整，\"非冲突特异\"声明缺乏正式等价性检验，单种子实验削弱可靠性 |\n| Excitement | 3/5 | 问题重要且及时，XNLI baseline 对比有方法论启示；但 steering 仅 Llama 成功，核心因果发现的泛化性大打折扣 |\n| Reproducibility | 3/5 | 提供了关键参数；但单种子、未公开代码/数据、probe 正则化系数未报告 |\n| Reviewer Confidence | 4/5 | 熟悉 probing methodology、representation steering 和跨语言 NLP |\n\n### Must-Fix 问题\n\n**N1** [Critical] **Steering 实验的多重比较校正不完整，核心 p=0.002 可能不保真**\n- 位置: Section 3.6, Section 4.6\n- 主实验在 3 个层（L13, L18, L28）各测试 k=10 个 α 值，共 30 次检验。Bonferroni 仅在层内应用（0.05/10=0.005），未跨层校正。若全 family 校正（0.05/30≈0.00167），L13 正方向 p=0.002 不再显著。独立复现（N=201）缓解但非预注册。\n- 建议: 明确说明为什么层间不需要校正（如预注册），或采用 FDR 校正，或报告完整 family-wise p 值。\n\n**N2** [Critical] **因果声明的泛化性：N=1 模型问题**\n- 位置: Abstract, Section 4.6 \"Detection ≠ Decision\", Discussion §5\n- Steering 仅 Llama L13 成功，Qwen/Gemma 全部阴性（零翻转）。但论文框架性表述暗示这是 general principle。无法区分：Llama 特有特征 vs 线性 steering 局限 vs 统计偶然。Gemma 88.9% probe accuracy 下零效应对 \"probe direction = causal direction\" 构成反证。\n- 建议: 将 \"Detection ≠ Decision\" 限定为 Llama-specific，讨论 Qwen/Gemma 失败是否意味着因果结构可能非线性。\n\n### Should-Fix 问题\n\n**W1** [Major] 单种子实验——Table 1 所有结果基于单次 split，未报告多种子 mean ± std，peak layer 可能因 split 变化。\n\n**W2** [Major] \"非冲突特异\"声明仅基于 CI 重叠，缺乏正式 TOST 等价性检验或 difference-in-differences 检验。\n\n**W3** [Major] COMET tercile 分析统计功效不足（每 tercile 64-91 样本），p=0.695/0.761 反映 power 不足而非无效应。Gemma 未报告。\n\n**W4** [Major] 跨模型比较在不同样本子集上进行（Llama 1368, Qwen 966, Gemma 1590），未在交集上验证。\n\n**W5** [Minor] 翻译模型（Qwen3-8B）与实验对象重叠，未讨论此 confound。\n\n**W6** [Minor] Table 3 caption \"p < 0.05\" 与正文 Bonferroni 阈值 0.005 不一致。\n\n### Questions\n\nQ1: Bonferroni 为什么按层而非按整个 steering 实验校正？是否有先验理由？\nQ2: 独立复现（N=201）是否在观察到 L13 主实验结果之后进行？\nQ3: Gemma L21 cross-task transfer dip（0.730）与 alternating attention 架构的关系？\nQ4: L13 和 L28 的 w_probe cosine similarity 是多少？\nQ5: Qwen Δ_asym CI 包含零，如何支撑 \"consistent across all three architectures\"？\n\n### Missing References\n- Turner, Thacker, and Fry (2023): \"Activation Addition\"——steering 核心方法论文献\n- Marks et al. (2024): \"Geometry of Truth\"——与跨任务 probe direction 共享分析直接相关\n\n### 主要优势\n- S1: 首次多架构/多语言知识冲突信号的系统性 probing 研究\n- S2: Confound exclusion pipeline 设计周全（COMET/token overlap/XNLI/EN-DE）\n- S3: XNLI baseline 对比有方法论启示价值\n- S4: 对 negative results 的诚实处理（Gemma informative negative）\n- S5: 独立复现（N=201）展示 causal gradient 空间精度\n- S6: 写作清晰，结构完整",
    "reviewer_id": "1",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-24T15:02:33.177041+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3917
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-24T15:02:39.818076+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-24T15:02:39.871014+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 52
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-24T15:02:47.562596+00:00_

审稿完成，已提交给 Review Director。

核心判断：论文的 probing 分析（跨语言可检测性 + 方向不对称性 + confound exclusion）是扎实的，但两个 Critical 问题影响接收决定：(1) steering 实验的 Bonferroni 校正仅在层内而非跨层应用，导致 L13 p=0.002 在完整校正下可能不显著；(2) "Detection ≠ Decision" 作为论文核心贡献仅在 Llama 一个模型上成立，但论文的 framing 暗示其为 general principle。评分 3.5（Borderline Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1"
}
```

</details>

---

## Round 2

4 recorded events

### User

_source line 53 · 2026-05-24T15:03:12.295090+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿意见

### Overall: 3.0 / 5 — Findings

**N1** [Critical] Steering 仅在 Llama 成功，"Detection ≠ Decision" claim 的泛化性严重不足
- 论文最具新颖性的 claim 因果证据仅来自 Llama 一个模型。Qwen (p=0.785, 0 flips) 和 Gemma (p=0.448, 0 flips) 均完全失败。一个仅在 1/3 模型上成立的因果发现难以支撑一般性结论。
- 建议：(a) 尝试 activation patching / DAS 等替代方法排除是 linear steering 本身的局限；(b) 明确降低 claim 强度；(c) 补充对 steering 失败的 mechanistic 解释。

**N2** [Critical] 新颖性增量性
- Contribution 1 是 Zhao et al. (2024) 的直接跨语言扩展；不对称性可从 Wendler et al. (2024) 和 Kargaran et al. (2024) 直接预测。Contribution 3（Confound Pipeline）虽有用但单独不足以支撑 long paper。三个 contributions = "增量扩展" + "N=1 case study" + "methodological toolkit"。

**W1** [Major] Qwen3-8B 引用错误：论文使用 Qwen3-8B 但引用 Qwen2.5 Technical Report (yang2024qwen25)。正确引用应为 arXiv:2505.09388。

**W2** [Major] 仅一个语言对 (EN-ZH) 但标题使用 "Cross-Lingual" 暗示一般性。EN-DE 仅在 confound exclusion 中简要提及。

**W3** [Major] Single-seed probing：所有结果基于单次种子训练，未考虑探针训练随机性。

**W4** [Minor] Related Work 遗漏：Pires et al. 2019, Chi et al. 2020, Meng et al. 2022 (activation patching), Geiger et al. 2024 (DAS)。

**W5** [Minor] 多个 bib 条目使用 "and others" 格式，作者信息不完整。

**W6** [Minor] Abstract 恰好 200 words，位于限制边界。

### Missing References
1. Pires et al. (2019) "How Multilingual is Multilingual BERT"
2. Chi et al. (2020) "Finding Universal Grammatical Relations in Multilingual BERT"
3. Meng et al. (2022) "Locating and Editing Factual Associations in GPT"
4. Geiger et al. (2024) DAS
5. Qwen Team (2025) Qwen3 Technical Report (arXiv:2505.09388)

### 主要优势
- S1: 混淆排除设计系统全面
- S2: 诚实报告负面结果
- S3: XNLI baseline 比较实验设计巧妙
- S4: 统计实践严谨
- S5: Discussion 部分有深度思考

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-24T15:04:54.818383+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 的交叉回应\n\n### Must-Fix\n\n[AGREE] R2-N1 (Steering 泛化性): 与我的 N2 一致。补充：R2 建议尝试 DAS 等替代方法是建设性的；但 R2 可能低估了 Gemma informative negative 的价值（Section 4.6, 88.9% probe accuracy 下零翻转排除了 probe quality confound）。\n\n[REBUT] R2-N2 (新颖性增量): 部分不同意。(1) Contribution 1 不是 Zhao et al. (2024) 的简单扩展——方向不对称性 + XNLI 匹配是新发现，\"可预测\"≠\"已验证\"；(2) Contribution 3 不应独立评估，它是 Contribution 1 可靠性的支撑；(3) 但同意 Contribution 2 (N=1 因果) 偏弱。综合评估：novelty sufficient for Findings，可能 borderline Conference。\n\n### Should-Fix\n\n[AGREE] R2-W1 (Qwen3 引用错误): 事实性错误，必须更正。\n[AGREE] R2-W2 (单语言对 vs 标题): 标题应加限定。\n[AGREE] R2-W3 (Single-seed): 与我的 W1 一致。\n[REBUT] R2-W4 (Related Work): 4篇中仅 Meng (2022) 和 Geiger (2024) DAS 应引用；Pires (2019) 和 Chi (2020) 非必要，论文已引用更直接的后续工作。\n[AGREE] R2-W5 (Bib 格式): \"and others\" 截断需修复。\n[REBUT] R2-W6 (Abstract 200 words): 200 words 完全合规，≤200 是硬限制，200 满足条件。\n\n### Missing References\nMeng (2022) 和 Geiger (2024) DAS: [AGREE] 应引用。\nPires (2019) 和 Chi (2020): [REBUT] 非必要。\nQwen3 Tech Report: [AGREE] 必须更正。\n\n### 评分分歧\nR2=3.0 vs R1=3.5。差异源自新颖性评估：我认为 Contribution 1+3 的组合具备独立方法论贡献，不应仅因 Contribution 2 的 N=1 问题降级。但若去掉 L13 阳性结果，同意应降至 2.5-3.0。",
  "reviewer_id": "1",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 的交叉回应\n\n### Must-Fix\n\n[AGREE] R2-N1 (Steering 泛化性): 与我的 N2 一致。补充：R2 建议尝试 DAS 等替代方法是建设性的；但 R2 可能低估了 Gemma informative negative 的价值（Section 4.6, 88.9% probe accuracy 下零翻转排除了 probe quality confound）。\n\n[REBUT] R2-N2 (新颖性增量): 部分不同意。(1) Contribution 1 不是 Zhao et al. (2024) 的简单扩展——方向不对称性 + XNLI 匹配是新发现，\"可预测\"≠\"已验证\"；(2) Contribution 3 不应独立评估，它是 Contribution 1 可靠性的支撑；(3) 但同意 Contribution 2 (N=1 因果) 偏弱。综合评估：novelty sufficient for Findings，可能 borderline Conference。\n\n### Should-Fix\n\n[AGREE] R2-W1 (Qwen3 引用错误): 事实性错误，必须更正。\n[AGREE] R2-W2 (单语言对 vs 标题): 标题应加限定。\n[AGREE] R2-W3 (Single-seed): 与我的 W1 一致。\n[REBUT] R2-W4 (Related Work): 4篇中仅 Meng (2022) 和 Geiger (2024) DAS 应引用；Pires (2019) 和 Chi (2020) 非必要，论文已引用更直接的后续工作。\n[AGREE] R2-W5 (Bib 格式): \"and others\" 截断需修复。\n[REBUT] R2-W6 (Abstract 200 words): 200 words 完全合规，≤200 是硬限制，200 满足条件。\n\n### Missing References\nMeng (2022) 和 Geiger (2024) DAS: [AGREE] 应引用。\nPires (2019) 和 Chi (2020): [REBUT] 非必要。\nQwen3 Tech Report: [AGREE] 必须更正。\n\n### 评分分歧\nR2=3.0 vs R1=3.5。差异源自新颖性评估：我认为 Contribution 1+3 的组合具备独立方法论贡献，不应仅因 Contribution 2 的 N=1 问题降级。但若去掉 L13 阳性结果，同意应降至 2.5-3.0。",
    "reviewer_id": "1",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-24T15:04:58.732374+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3913
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-24T15:05:18.157517+00:00_

交叉回应已提交。总结：

- R2 的 7 条意见中，我 **AGREE** 4 条（N1 steering 泛化性、W1 引用错误、W2 标题 scope、W3 单种子、W5 bib 格式）
- **REBUT** 3 条（N2 新颖性评估过严、W4 仅部分遗漏相关、W6 abstract 200 words 合规）
- Missing References 5 篇中认同 3 篇（Meng 2022、Geiger 2024 DAS、Qwen3 Tech Report），不认为 Pires 2019 和 Chi 2020 是必要引用
- 评分分歧 0.5 分（R1=3.5 vs R2=3.0），核心在于对 Contribution 1+3 组合价值的判断

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1"
}
```

</details>

---

## Round 3

64 recorded events

### User

_source line 57 · 2026-05-24T16:32:06.599749+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析**。

## Venue 信息
- **目标**: EMNLP 2026 Long Paper (ARR May cycle)
- **截止日期**: 2026-05-25
- **格式**: ACL 模板，正文 8 页，参考文献不限，Limitations 必选不计入页数
- **匿名**: Double-blind
- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 论文文件
- LaTeX 源文件: `projects/clkc_mech_interp/docs/paper/main.tex`（各 section 通过 `\input{}` 引入）
- PDF: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf`

## 论文概要
标题: *Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations*

研究跨语言知识冲突信号在多语言 LLM 内部表征中的检测和因果影响。在 Llama-3.1-8B-Instruct、Qwen3-8B 和 Gemma-2-9B-IT 三个模型上进行 residual stream probing，发现：
1. 冲突信号可跨语言线性检测
2. ZH→EN 迁移优于 EN→ZH 约 7pp，与 XNLI 非冲突基线一致
3. 在 Llama 中存在 detection-decision 层分离：probe 峰值在 L28 (88% depth)，但 steering 仅在 L13 (41% depth) 有因果效应
4. Qwen 和 Gemma steering 无显著效果

## 你的审查重点

请重点审查以下方面：

1. **Probing pipeline 设计**：logistic regression probe 的训练/测试分割是否合理？单种子设计的风险？Balanced accuracy 作为指标是否充分？
2. **Steering 实验的因果推断**：Fisher exact test + Bonferroni 校正的应用是否正确？校正范围是否充分（层内 vs 跨层）？flip rate 作为因果效应的度量是否合适？
3. **多重比较问题**：论文在多个层、多个 alpha 值上测试——family-wise error rate 控制是否充分？
4. **Confound exclusion pipeline**：COMET tercile 分析和 token overlap 分析的统计功效是否足够？能否真正排除混淆变量？
5. **XNLI baseline 比较**：CI 重叠作为 "非冲突特异" 的论据是否充分？是否需要 formal equivalence testing？论文中的 TOST 检验是否正确执行？
6. **跨模型比较的有效性**：三个模型使用不同样本子集（Llama 1368, Qwen 966, Gemma 1590），这对比较的公平性有何影响？
7. **因果声明的泛化性**：Detection ≠ Decision 仅在 Llama 一个模型成立，Qwen/Gemma 零翻转——标题和 abstract 的 claim 是否过度泛化？
8. **独立复现**：Appendix 的 boundary-mapping replication (N=201) 是否真正独立？数据采样和实验条件是否充分描述？

请输出结构化审稿报告：Summary → Strengths → Weaknesses（按 severity 排序：Must-Fix / Should-Fix / Minor）→ Questions → Overall Assessment（含评分和置信度）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-24T16:32:19.836170+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
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

_source line 59 · 2026-05-24T16:32:19.886772+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-24T16:32:24.070872+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-24T16:32:25.078656+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf",
  "pages": "1-8",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf",
    "pages": "1-8",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-24T16:32:25.636009+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/clkc_mech_interp/docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod42"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/clkc_mech_interp/docs/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-prod42"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-24T16:32:29.777490+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) 2025-2026 reviewer guidelines:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Scoring Criteria

**Soundness:** The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

**Excitement:** Preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Expectations for Reviewers

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements.

The guidelines emphasize that reviewers should justify their scores and ensure their reviews provide faithful explanations of their
…[truncated 219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5706
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-24T16:32:31.038088+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.7}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 528.6}], \"total_pages\": 11, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5959
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-24T16:32:31.138926+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 5502
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-24T16:32:36.917865+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form dimensions/criteria, scoring scales (especially soundness, excitement, overall assessment), and any specific guidelines about what each score means. I need the full rubric."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form dimensions/criteria, scoring scales (especially soundness, excitement, overall assessment), and any specific guidelines about what each score means. I need the full rubric."
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-24T16:32:37.472811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-24T16:32:37.979028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-24T16:32:38.583618+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1110
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-24T16:32:38.584146+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-24T16:32:39.519090+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1540
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-24T16:32:40.026120+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1441
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-24T16:32:43.743066+00:00_

# ARR Review Form Dimensions and Scoring Rubric

Based on the ARR Reviewer Guidelines, here's what's specified about the review form structure:

## Primary Scoring Dimensions

The guidelines indicate three main scores are required (as of February 2025):

1. **Soundness** - Assesses technical rigor and validity
2. **Excitement** - Reflects personal interest and engagement with the work
3. **Overall Assessment** - Explicit recommendation for venue acceptance

## Soundness Score Guidance

The document states: "The _soundness_ scores must be justified by the text of the review. If you give a low _Soundness_ score without finding any major faults, this means that your review is not a faithful explanation of your recommendation" (I3 annotation).

Reviewers must identify specific technical issues to justify lower soundness ratings.

## Excitement Score Guidance

"Excitement scores reflect our personal taste, and so do not necessarily come with explicit reasons." This dimension captures subjective interest distinct from objective quality assessment.

## Overall Assessment Guidance

This composite score should reflect "soundness, excitement, and also other factors like novelty and impact." The guidelines note: "All papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible, but you may consider a paper worthy of the main conference even if you personally are not excited about it."

**Note:** The document doesn't provide specific numerical scales (e.g., 1-5 or 1-10) for these dimensions—those appear in the actual OpenReview form itself, which isn't included in these guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6825
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-24T16:32:48.371166+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-24T16:32:48.986908+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-24T16:32:49.894374+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1523
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-24T16:32:49.895087+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-24T16:32:49.895316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-24T16:32:50.397242+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-24T16:32:50.700112+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-24T16:32:50.700510+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-24T16:32:51.505641+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1108
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-24T16:32:51.708951+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1008
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-24T16:32:59.323021+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf",
  "pages": "9-11",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf",
    "pages": "9-11",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-24T16:33:00.290475+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 432.6}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 606.5}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 313.6}], \"total_pages\": 11, \"rendered_pages\": 3, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 967
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-24T16:33:01.960482+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Find LaTeX source files",
  "subagent_type": "Explore",
  "prompt": "Find all .tex files under /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/. The main file is main.tex which uses \\input{} to include section files. I need to know the full list of .tex files and their paths. Search breadth: medium."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "description": "Find LaTeX source files",
    "subagent_type": "Explore",
    "prompt": "Find all .tex files under /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/. The main file is main.tex which uses \\input{} to include section files. I need to know the full list of .tex files and their paths. Search breadth: medium."
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-24T16:33:04.187047+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-24T16:33:04.287971+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/acl_latex.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-24T16:33:07.003141+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-24T16:33:07.053832+00:00_

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
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	\usepackage{subcaption}
17	
18	\title{Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	\input{abstract}
27	\end{abstract}
28	
29	\input{introduction}
30	
31	\input{related_work}
32	
33	\input{method}
34	
35	\input{experiments}
36	
37	\input{discussion}
38	
39	\input{conclusion}
40	
41	\input{limitations}
42	
43	\appendix
44	
45	\section{Use of AI Assistants}
46	\label{app:ai-assistants}
47	
48	We used Claude (Anthropic) as an AI coding and writing assistant
49	throughout this work. Specifically:
50	\begin{itemize}
51	    \item \textbf{Code:} drafting experiment scripts, data-processing
52	    pipelines, and analysis utilities; debugging and refactoring.
53	    \item \textbf{Writing:} drafting and revising paper sections,
54	    polishing prose, and reformatting \LaTeX{}.
55	    \item \textbf{Literature:} summarizing related papers to inform
56	    related-work section.
57	\end{itemize}
58	
59	\section{Fine-Grained Causal Boundary Analysis}
60	\label{app:boundary}
61	
62	Table~\ref{tab:boundary} reports steering results across the full layer gradient from an independent replication ($N = 201$, Llama-3.1-8B-Instruct, RTX PRO 6000).
63	
64	\begin{table}[h]
65	\centering
66	\caption{Causal boundary steering results (independently sampled, $N = 201$, Llama-3.1-8B-Instruct). Bonf.\ Sig.\ $\alpha$s: number of $\alpha$ values reaching significance after Bonferroni correction out of 6 tested.}
67	\label{tab:boundary}
68	\small
69	\resizebox{\columnwidth}{!}{%
70	\begin{t
…[truncated 2623 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-24T16:33:13.514079+00:00_

Perfect! Now I have all the information. Let me compile the findings.

## Summary of .tex Files

I found **18 .tex files** in total under `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/`. Here's the complete list organized by location:

### Main Entry Point
- `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex` (root)

### Files Included via \input{} Commands (from main.tex)
These are the files actually referenced in main.tex via `\input{}` directives:
1. `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex`
2. `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex`
3. `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex`
4. `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex`
5. `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex`
6. `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex`
7. `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex`
8. `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex`

### Parallel Section Files in sections/ Directory
These appear to be alternate or duplicate versions organized in a subdirectory:
9. `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/abstract.tex`
10. `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/introduction.tex`
11. `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex`
12. `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/method.tex`
13. `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex`
14. `/home/ubuntu/.agent-ml-research-prod42/projects
…[truncated 749 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 11553
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-24T16:33:27.888510+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-24T16:33:28.704332+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-24T16:33:29.208831+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1320
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-24T16:33:29.209289+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-24T16:33:29.510972+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-24T16:33:29.511407+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-24T16:33:29.914226+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-24T16:33:29.914782+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Our pipeline proceeds from data construction through probing and steering, formalized below.
5	
6	\subsection{Task Formulation}
7	\label{sec:task}
8	
9	Given a context passage $c$ and question $q$, the model produces an answer that is either \emph{contextual} (derived from $c$) or \emph{parametric} (from pre-trained knowledge).
10	When $c$ contradicts parametric knowledge, the choice constitutes a knowledge conflict.
11	We train a logistic regression probe $f_\theta(\mathbf{h}_l) = \sigma(\mathbf{w}_l^\top \mathbf{h}_l + b_l)$ on the last-token residual stream representation $\mathbf{h}_l \in \mathbb{R}^d$ at layer $l$ to predict a binary label $y \in \{\text{contextual}, \text{parametric}\}$.
12	
13	\subsection{Data Construction}
14	\label{sec:data}
15	
16	We build on ConflictQA \citep{xie2024adaptive}, which pairs questions with context passages contradicting the model's parametric knowledge.
17	We filter samples by querying each model without context and retaining only those answered correctly, yielding 1{,}368 samples for Llama \citep{grattafiori2024llama}, 966 for Qwen \citep{yang2025qwen3}, and 1{,}590 for Gemma \citep{team2024gemma} (80/20 train/test split with stratification).
18	For cross-lingual transfer, we translate all inputs into Chinese using a Qwen3-8B pipeline, with quality validated by COMET \citep{rei2020comet} back-translation scores used in confound analysis (\S\ref{sec:confound_method}).
19	
20	\subsection{Activation Extraction and Probing}
21	\label{sec:extraction}
22	
23	For each input, we construct English and Chinese versions and extract the last-token residual stream $\mathbf{h}_l \in \mathbb{R}^d$ at every layer $l$ ($L = 32$ for Llama, $36$ for Qwen, $42$ for Gemma; $d = 4096$ for Llama/Qwen, $3584$ for Gemma), following the last-token aggregation principle \citep{belinkov2022probing}.
24	We record the model's answer and assign binary labels (contextual vs.\ parametric).
25	
26	\label{sec:prob
…[truncated 2948 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-24T16:33:34.254194+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-24T16:33:34.706823+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We probe three instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \citep{grattafiori2024llama}, Qwen3-8B (36 layers, hidden dimension 4096) \citep{yang2025qwen3}, and Gemma-2-9B-IT (42 layers, hidden dimension 3584) \citep{team2024gemma}.
9	
10	\paragraph{Dataset.}
11	We use ConflictQA \citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.
12	After verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test), 966 for Qwen (773 train / 193 test), and 1{,}590 for Gemma (1{,}274 train / 316 test), split 80/20 with stratification.
13	
14	\paragraph{Translation.}
15	We translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\to$ZH), with quality validated by COMET \citep{rei2020comet} back-translation scores.
16	
17	\paragraph{Probing.}
18	For each layer $l$, we train a logistic regression probe on the last-token residual stream representation $\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.
19	We report balanced accuracy to account for class imbalance.
20	All confidence intervals (CIs) are computed via bootstrap resampling with paired differences for asymmetry estimation.
21	
22	\paragraph{Non-conflict baseline.}
23	To test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \citep{conneau2018xnli}, classifying entailment versus contradiction.
24	
25	\subsection{Within-Language Conflict Detection}
26	\label{sec:within_lang}
27	
28	Table~\ref{tab:main_results} reports balanced accuracy for all
…[truncated 14341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-24T16:33:34.707228+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-24T16:33:34.757786+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Detection and decision occur at different layers.}
5	Our central mechanistic finding is a dissociation between where conflict signals become linearly readable and where they exert causal influence on model behavior.
6	In Llama, probe accuracy on EN$\to$EN peaks at layer~28 (88\% depth), yet representation steering succeeds only at layer~13 (41\% depth; Fisher $p = 0.002$), and all late-layer interventions produce no significant behavioral change ($p > 0.3$).
7	This dissociation has a cross-lingual counterpart: the Llama ZH$\to$ZH probe peaks at L13, the same layer where steering succeeds.
8	Mid-layers thus serve a dual role as the site of cross-lingual alignment \citep{muller2021first, wendler2024llamas} and the locus where conflict signals acquire causal force.
9	The EN$\to$EN peak at L28 is best understood as a diagnostic readout, a linearly readable trace of a decision that has already been made upstream.
10	A practical implication follows: the probe peak layer is not the causal layer, and intervention experiments that target only the highest-accuracy layer risk missing the computationally relevant site.
11	Cross-layer sweeps, as conducted here, are necessary to locate the true decision point.
12	Steering failed in both Qwen (L14, 39\%; $n = 131$, best $p = 0.785$) and Gemma (L17, 40\%; $n = 171$, best $p = 0.448$), with zero directional flips in both cases.
13	The Gemma result is particularly informative: its 88.9\% probe accuracy---the highest among all three models---rules out probe quality as a confound, since the direction that best separates conflict labels carries no causal influence despite being highly discriminative.
14	This establishes that the causal influence of the probe direction is architecture-dependent, not a general property of mid-layer computation.
15	
16	\paragraph{Conflict signals are encoded in a general cross-lingual space.}
17	The ZH$\to$EN transfer advantage is consistent a
…[truncated 4458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-24T16:33:44.196380+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-24T16:33:44.699632+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our study has three main limitations.
5	First, we evaluate only one language pair (English-Chinese) and causal steering succeeded only in Llama at L13; Gemma L17 failed despite 88.9\% probe accuracy ($n = 171$) and Qwen L14 ($n = 131$) was also negative.
6	Typologically diverse language pairs and alternative intervention methods are needed to assess generality.
7	Second, the effective dataset size (966 to 1,590 samples per model) is constrained by parametric knowledge verification, and Qwen3-8B serves as both the translation model and an experimental subject; while the COMET-based quality control and Llama/Gemma cross-validation mitigate this dual-role concern, a fully independent translation model would strengthen the Qwen-specific results.
8	Third, all probing results are based on a single train/test split with bootstrap confidence intervals capturing within-split variability; future work should verify stability across multiple random seeds and larger datasets to improve statistical power for stratified comparisons such as the COMET tercile ablation.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-24T16:33:44.750591+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-24T16:33:45.102981+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	This work investigated whether knowledge conflict signals in multilingual LLMs are detectable across languages and whether detected signals causally influence conflict resolution.
5	Through residual stream probing on Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT, we showed that conflict signals are linearly detectable both within and across languages, with balanced accuracies of 77.6\%, 75.0\%, and 76.2\% on English within-language detection and all cross-lingual transfer directions significantly exceeding chance (binomial $p < 0.001$).
6	The observed transfer asymmetry (ZH$\to$EN exceeding EN$\to$ZH by approximately 6--7~pp) is consistent across all three architectures and is consistent with the XNLI non-conflict baseline in magnitude and direction for all models, establishing that this pattern reflects the general cross-lingual representational structure of English-dominant models rather than conflict-specific encoding.
7	
8	A central finding is the dissociation between detection and decision.
9	Probe accuracy peaks at late layers (L28, 88\% depth), but representation steering succeeds only at a mid-layer (L13, 41\% depth; Fisher $p = 0.002$), and all late-layer interventions fail.
10	This result demonstrates that linear detectability does not imply causal influence, and that conflict resolution occurs upstream of where the outcome becomes linearly readable.
11	For probing-based intervention research, this dissociation implies that cross-layer sweeps are necessary to identify the computationally relevant site, as targeting the probe peak alone can miss the true decision point.
12	
13	Several directions remain open.
14	Steering failed in both Qwen (L14; $n = 131$, best $p = 0.785$) and Gemma (L17; $n = 171$, 88.9\% probe accuracy, best $p = 0.448$), with zero directional flips despite Gemma's probe accuracy exceeding Llama's, confirming that the causal influence of the probe direction is architecture-specifi
…[truncated 165 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-24T16:33:45.103460+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-24T16:33:45.155713+00:00_

1	When multilingual large language models (LLMs) encounter conflicting information across languages, presentation language can determine the answer. Behavioral studies attribute this to linguistic affinity, but the internal mechanism remains unknown: how is the conflict signal encoded, does it share structure with general cross-lingual representations, and does detectability imply causal influence on resolution?
2	
3	We probe residual stream representations in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT, focusing on English--Chinese conflicts. Our analysis combines cross-lingual transfer, XNLI non-conflict baselines, confound exclusion, and representation steering. Conflict signals are linearly detectable across languages, and cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English ${\sim}$7 percentage points more accurately than the reverse. This asymmetry is consistent with the XNLI non-conflict baseline in both magnitude and direction, with overlapping confidence intervals, inheriting from the model's general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision in Llama-3.1-8B-Instruct: the probe signal peaks at late layers (88\% depth), but representation steering achieves causal influence only at a mid-layer (41\% depth); analogous Qwen and Gemma steering yields no significant effect. These findings demonstrate that linear detectability does not imply causal relevance, with implications for probe-based intervention research.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-24T16:33:49.121436+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-24T16:33:49.725256+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation can determine which answer the model produces.
5	\citet{zhao2026when} showed that linguistic affinity dominates conflict resolution in entity-centric factual conflicts, with models preferring answers from linguistically closer sources.
6	Yet the internal mechanism behind this behavior remains opaque: how does the model encode the conflict signal?
7	Can it be detected from internal representations?
8	And if detectable, does the detected signal causally influence the model's resolution strategy?
9	These questions sit at the intersection of mechanistic interpretability and multilingual NLP, and answering them requires moving beyond behavioral observations to probe model internals directly.
10	
11	Existing work on probing knowledge conflict signals has been limited to monolingual settings.
12	\citet{zhao2024analysing} showed that residual stream representations carry linearly detectable conflict signals in English, and \citet{brink2026probing} performed knowledge attribution probing to localize factual associations within model parameters.
13	Extending these approaches cross-lingually introduces additional challenges.
14	Translation quality may confound probe transfer: a poor translation could alter conflict detection for reasons unrelated to the conflict signal itself.
15	Token overlap between languages, even when minimal, could provide a shortcut for cross-lingual probes.
16	Observed asymmetries in transfer accuracy may reflect general cross-lingual properties rather than conflict-specific phenomena, and disentangling these sources requires careful baseline comparisons.
17	Beyond detectability, a fundamental limitation of probing is that it establishes correlation, not causation \citep{hewitt2019designing}.
18	\citet{basu2026interpretability} demonstrated that even near-perfect probe ac
…[truncated 3750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-24T16:33:49.725618+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-24T16:33:49.777081+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Knowledge conflict detection.}
5	\citet{xie2024adaptive} introduced ConflictQA and showed that models exhibit context-dependent resolution strategies, and \citet{xu2024knowledge} provided a systematic conflict taxonomy (intra-memory, context-memory, inter-context).
6	Moving beyond behavioral observation, \citet{zhao2024analysing} demonstrated linearly separable conflict signals in English residual streams, \citet{brink2026probing} localized factual associations via probing, \citet{pham2026where} traced intra-memory conflict pathways, and \citet{li2025taming} proposed conflict mitigation methods.
7	These studies operate exclusively in monolingual settings; extending to cross-lingual scenarios introduces confounds (translation quality, token overlap, general transfer properties) that we address with a dedicated exclusion pipeline.
8	
9	\paragraph{Cross-lingual representations in multilingual models.}
10	Intermediate layers develop language-independent representations: \citet{wu2020emerging} showed cross-lingual structure emerges without explicit alignment, and \citet{muller2021first} found mid-layer alignment in multilingual BERT.
11	For decoder-only LLMs, \citet{wendler2024llamas} showed that Llama processes non-English inputs through an English-centric latent space, and \citet{kargaran2024mexa} quantified this bias across language pairs.
12	These findings predict our empirical observations: mid-layer steering success aligns with intermediate-layer language alignment, and the ZH$\to$EN transfer advantage reflects English-centric structure.
13	Behavioral consequences have been documented by \citet{wang2025lost}, \citet{zhao2026when} (CLEAR benchmark), and \citet{ifergan2024beneath, xing2024evaluating}; our work provides a mechanistic account of why such asymmetries arise.
14	
15	\paragraph{Representation steering and causal intervention.}
16	\citet{li2023iti} introduced Inference-Time Intervention for
…[truncated 1185 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-24T16:33:55.611442+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form 2025 soundness excitement scoring scale 1-5 rubric openreview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form 2025 soundness excitement scoring scale 1-5 rubric openreview"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-24T16:34:02.337159+00:00_

Web search results for query: "ACL ARR review form 2025 soundness excitement scoring scale 1-5 rubric openreview"

Links: [{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL ARR 2025 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"},{"title":"ACL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/acl-statistics/acl-2025-statistics/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on my search results, here's what I found about the ACL ARR review form for 2025:

## Scoring Framework

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score

The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

## Excitement Score

Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

…[truncated 538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6725
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-24T16:34:06.911684+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact scales (1-5 or whatever), and descriptions for each level. I need the full rubric for soundness, excitement, overall assessment, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact scales (1-5 or whatever), and descriptions for each level. I need the full rubric for soundness, excitement, overall assessment, confidence, and any other dimensions."
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-24T16:34:12.385803+00:00_

# ACL Rolling Review Form - Complete Rubric

## Reviewer Confidence
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

(Half-point increments available: 4.5, 3.5, 2.5, 1.5)

## Excitement
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me."

(Half-point increments available)

## Overall Assessment
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

(Half-point increments available: 4.5, 3.5, 2.5, 1.5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5474
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-24T16:38:42.993759+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告：方法严谨性 + 实验设计 + 统计分析\n\n### 总体评分\n\n**Overall Assessment**: 3.5 / 5 — Borderline Conference\n**Confidence**: 4 / 5\n**一句话总结**: 方法管线设计优于多数 probing 研究（含 confound exclusion 和 XNLI baseline），但因果发现仅在 1/3 模型成立、单种子设计低于当前标准、TOST 等价检验欠功效，削弱了两个核心贡献的说服力。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 主体方法合理，但单种子单 split 设计、TOST 欠功效却仍做等价结论、confound 分析缺 Gemma 数据构成方法论空缺 |\n| Excitement | 3 / 5 | Detection ≠ Decision 分离是有趣的 mechanistic 发现，XNLI baseline 设计巧妙，但因果部分仅 Llama 成立，asymmetry inheritance 本身偏 incremental |\n| Reproducibility | 3 / 5 | 单种子单 split，未公开代码/数据，bootstrap n=2000 偏低，Appendix 细节较充分但缺完整超参表 |\n\n---\n\n### Must-Fix 问题（3 个）\n\n**N1** [critical] 单种子单 split 设计——bootstrap CI 不能替代 multi-seed 验证\n\n- 具体位置：Section 3.3, Section 4.1, Limitations\n- 问题：所有 probing 结果基于一次 80/20 stratified split，bootstrap CI（n=2,000）仅捕获 split 内采样变异性，而非 split 间变异性。Logistic regression probe 对训练集组成敏感，不同 split 可能导致 peak layer 位置和 Δ_asym 估计值的实质变化。当前 probing 文献的标准实践是 ≥3 个随机种子取平均。\n- 为什么影响接收：Table 1 中所有数字（包括 Δ_asym 的 7.3/7.2/6.6 pp）以及 Figure 1 的 layer-wise 曲线可能不稳定。论文的核心声明（跨模型一致的 ~7pp 不对称性）依赖数值相似性。\n- 建议：至少运行 5 个不同 train/test split 种子，报告均值 ± 标准差。\n\n**N2** [critical] TOST 等价检验不显著，但结论按等价处理\n\n- 具体位置：Section 4.4, line 94-95\n- 问题：TOST（±2pp margin）三个模型均不显著（p=0.434, 0.366, 0.377），论文正确指出 SE≈4.37pp 导致 power 不足，但仍总结 \"The asymmetry thus reflects a general cross-lingual property\"。非显著 TOST = \"数据不足以区分等价与非等价\"，而非\"效应等价\"。±2pp margin 的选择亦缺乏 justification。\n- 为什么影响接收：Contribution 1（asymmetry inheritance）是论文标题核心声明。如等价性未被严格建立，标题的\"inherit\"缺乏统计支撑。\n- 建议：调整表述为 \"is consistent with\" 而非 \"reflects/inherits\"；justify margin 选择；或增大样本量。\n\n**N3** [critical] 因果声明仅 Llama 1/3 模型成立——泛化性不足\n\n- 具体位置：Contribution 2, Section 4.6, Table 3, Conclusion\n- 问题：Steering 在 Qwen（n=131, best p=0.785, 0 flips）和 Gemma（n=171, best p=0.448, 0 flips）完全失败。论文将 detection-decision dissociation 列为三大贡献之一，但仅在 1/3 模型成立。Qwen/Gemma 的零效应有两种解释：(a) 无 detection-decision 分离，(b) 线性 steering 不足以揭示非线性因果结构。论文选择 (a) 但未充分排除 (b)。\n- 建议：在 Discussion 讨论线性 steering 局限性作为替代解释；考虑降低 Contribution 2 的地位。\n\n---\n\n### Should-Fix 问题（6 个）\n\n**W1** Confound exclusion 缺 Gemma 数据（Table 2 仅报告 Qwen 和 Llama，Gemma 有最大数据集 1590 样本）\n\n**W2** Confound tercile 分析统计功效不足（每组仅 ~60-90 样本，Fisher exact test 的 p=0.695/0.761 不能解读为\"无混淆\"）。建议补充功效分析或改用连续回归。\n\n**W3** 三个模型使用 ConflictQA 不同子集（Llama 1368, Qwen 966, Gemma 1590），自选择偏差影响跨模型比较公平性。建议报告数据集重叠比例。\n\n**W4** Boundary-mapping replication（N=201）的\"独立性\"被夸大——相同模型/任务/方法/pipeline 下的重新采样是 validation 而非 replication。建议修改措辞。\n\n**W5** Steering 实验中定向翻转绝对数极少（4 p→c, 5 c→p），n_test=136。建议报告 Cohen's h 或 odds ratio 作为效应量。\n\n**W6** Qwen3-8B 翻译者-受试者双重角色——微妙偏差无法被 COMET 捕获。建议在独立翻译模型上验证 Qwen 结果。\n\n---\n\n### 小问题（5 个）\n\n- M1: Bootstrap n=2000 偏低，建议 n=10000\n- M2: EN-DE 对比分析细节不足（哪个模型？完整统计？）\n- M3: Table 1 脚注关于 Δ_asym 计算方式应提前说明\n- M4: 建议补充 AUROC 以便与 Basu et al. (2026) 直接比较\n- M5: Abstract ~198 词，合规但无余量\n\n---\n\n### 主要优势\n\n- S1: 方法管线完整性突出（probing + steering + confound exclusion + XNLI baseline + boundary replication）\n- S2: XNLI baseline 比较设计巧妙，有方法论贡献价值\n- S3: Detection ≠ Decision 分离对 probing-based intervention 社区有直接实践启示\n- S4: 写作清晰，claim 限定总体准确\n- S5: Confound exclusion pipeline 为跨语言 probing 研究提供可复用模板\n\n---\n\n### Questions for Authors\n\n1. 不同随机种子下 Llama L13 steering 显著性是否稳定？\n2. Gemma 的 COMET tercile 和 token overlap 结果？为什么 Table 2 省略？\n3. 三个模型 ConflictQA 子集重叠比例？\n4. Qwen/Gemma 是否尝试过非线性干预方法？\n5. TOST ±2pp margin 选择依据？",
  "reviewer_id": "1",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告：方法严谨性 + 实验设计 + 统计分析\n\n### 总体评分\n\n**Overall Assessment**: 3.5 / 5 — Borderline Conference\n**Confidence**: 4 / 5\n**一句话总结**: 方法管线设计优于多数 probing 研究（含 confound exclusion 和 XNLI baseline），但因果发现仅在 1/3 模型成立、单种子设计低于当前标准、TOST 等价检验欠功效，削弱了两个核心贡献的说服力。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 主体方法合理，但单种子单 split 设计、TOST 欠功效却仍做等价结论、confound 分析缺 Gemma 数据构成方法论空缺 |\n| Excitement | 3 / 5 | Detection ≠ Decision 分离是有趣的 mechanistic 发现，XNLI baseline 设计巧妙，但因果部分仅 Llama 成立，asymmetry inheritance 本身偏 incremental |\n| Reproducibility | 3 / 5 | 单种子单 split，未公开代码/数据，bootstrap n=2000 偏低，Appendix 细节较充分但缺完整超参表 |\n\n---\n\n### Must-Fix 问题（3 个）\n\n**N1** [critical] 单种子单 split 设计——bootstrap CI 不能替代 multi-seed 验证\n\n- 具体位置：Section 3.3, Section 4.1, Limitations\n- 问题：所有 probing 结果基于一次 80/20 stratified split，bootstrap CI（n=2,000）仅捕获 split 内采样变异性，而非 split 间变异性。Logistic regression probe 对训练集组成敏感，不同 split 可能导致 peak layer 位置和 Δ_asym 估计值的实质变化。当前 probing 文献的标准实践是 ≥3 个随机种子取平均。\n- 为什么影响接收：Table 1 中所有数字（包括 Δ_asym 的 7.3/7.2/6.6 pp）以及 Figure 1 的 layer-wise 曲线可能不稳定。论文的核心声明（跨模型一致的 ~7pp 不对称性）依赖数值相似性。\n- 建议：至少运行 5 个不同 train/test split 种子，报告均值 ± 标准差。\n\n**N2** [critical] TOST 等价检验不显著，但结论按等价处理\n\n- 具体位置：Section 4.4, line 94-95\n- 问题：TOST（±2pp margin）三个模型均不显著（p=0.434, 0.366, 0.377），论文正确指出 SE≈4.37pp 导致 power 不足，但仍总结 \"The asymmetry thus reflects a general cross-lingual property\"。非显著 TOST = \"数据不足以区分等价与非等价\"，而非\"效应等价\"。±2pp margin 的选择亦缺乏 justification。\n- 为什么影响接收：Contribution 1（asymmetry inheritance）是论文标题核心声明。如等价性未被严格建立，标题的\"inherit\"缺乏统计支撑。\n- 建议：调整表述为 \"is consistent with\" 而非 \"reflects/inherits\"；justify margin 选择；或增大样本量。\n\n**N3** [critical] 因果声明仅 Llama 1/3 模型成立——泛化性不足\n\n- 具体位置：Contribution 2, Section 4.6, Table 3, Conclusion\n- 问题：Steering 在 Qwen（n=131, best p=0.785, 0 flips）和 Gemma（n=171, best p=0.448, 0 flips）完全失败。论文将 detection-decision dissociation 列为三大贡献之一，但仅在 1/3 模型成立。Qwen/Gemma 的零效应有两种解释：(a) 无 detection-decision 分离，(b) 线性 steering 不足以揭示非线性因果结构。论文选择 (a) 但未充分排除 (b)。\n- 建议：在 Discussion 讨论线性 steering 局限性作为替代解释；考虑降低 Contribution 2 的地位。\n\n---\n\n### Should-Fix 问题（6 个）\n\n**W1** Confound exclusion 缺 Gemma 数据（Table 2 仅报告 Qwen 和 Llama，Gemma 有最大数据集 1590 样本）\n\n**W2** Confound tercile 分析统计功效不足（每组仅 ~60-90 样本，Fisher exact test 的 p=0.695/0.761 不能解读为\"无混淆\"）。建议补充功效分析或改用连续回归。\n\n**W3** 三个模型使用 ConflictQA 不同子集（Llama 1368, Qwen 966, Gemma 1590），自选择偏差影响跨模型比较公平性。建议报告数据集重叠比例。\n\n**W4** Boundary-mapping replication（N=201）的\"独立性\"被夸大——相同模型/任务/方法/pipeline 下的重新采样是 validation 而非 replication。建议修改措辞。\n\n**W5** Steering 实验中定向翻转绝对数极少（4 p→c, 5 c→p），n_test=136。建议报告 Cohen's h 或 odds ratio 作为效应量。\n\n**W6** Qwen3-8B 翻译者-受试者双重角色——微妙偏差无法被 COMET 捕获。建议在独立翻译模型上验证 Qwen 结果。\n\n---\n\n### 小问题（5 个）\n\n- M1: Bootstrap n=2000 偏低，建议 n=10000\n- M2: EN-DE 对比分析细节不足（哪个模型？完整统计？）\n- M3: Table 1 脚注关于 Δ_asym 计算方式应提前说明\n- M4: 建议补充 AUROC 以便与 Basu et al. (2026) 直接比较\n- M5: Abstract ~198 词，合规但无余量\n\n---\n\n### 主要优势\n\n- S1: 方法管线完整性突出（probing + steering + confound exclusion + XNLI baseline + boundary replication）\n- S2: XNLI baseline 比较设计巧妙，有方法论贡献价值\n- S3: Detection ≠ Decision 分离对 probing-based intervention 社区有直接实践启示\n- S4: 写作清晰，claim 限定总体准确\n- S5: Confound exclusion pipeline 为跨语言 probing 研究提供可复用模板\n\n---\n\n### Questions for Authors\n\n1. 不同随机种子下 Llama L13 steering 显著性是否稳定？\n2. Gemma 的 COMET tercile 和 token overlap 结果？为什么 Table 2 省略？\n3. 三个模型 ConflictQA 子集重叠比例？\n4. Qwen/Gemma 是否尝试过非线性干预方法？\n5. TOST ±2pp margin 选择依据？",
    "reviewer_id": "1",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-24T16:38:46.808396+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3814
}
```

</details>

---

### Assistant

_source line 120 · 2026-05-24T16:38:54.148066+00:00_

审稿报告已提交给 Review Director。

总结：给出 **3.5/5 Borderline Conference**。三个 Must-Fix 问题——(1) 单种子设计不满足当前 probing 标准，(2) TOST 等价检验无功效却做了等价结论，(3) 因果发现仅 1/3 模型成立但被列为主要贡献。六个 Should-Fix 包括 Gemma confound 数据缺失、tercile 分析功效不足、跨模型样本自选择偏差等。论文的方法管线设计（confound exclusion + XNLI baseline + boundary replication）和 Detection ≠ Decision 发现本身是优势。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1"
}
```

</details>

---

## Round 4

4 recorded events

### User

_source line 121 · 2026-05-24T16:40:33.555357+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿

请逐条阅读 Reviewer 2 的审稿意见，对每个 Must-Fix 和 Should-Fix 问题用 `[AGREE]` 或 `[REBUT]` 回应，附简要理由。重点关注你们之间的分歧点。

---

以下是 Reviewer 2 的完整审稿：

**Overall Assessment**: 3.0 (Findings)
**一句话总结**: 方法论扎实的跨语言 probing 实证研究，但标题和 abstract 对证据的过度泛化（单语言对声称 "Cross-Lingual"、相关性包装为因果 "Inherit"、单模型发现推广为通用结论）削弱了贡献的可信度。

### Must-Fix 问题

**N1** [critical] **标题 "Cross-Lingual" 过度泛化：仅测试 EN-ZH 一个语言对**
- 标题使用 "Cross-Lingual" 暗示跨语言通用性，但实验仅涉及英语-中文一个语言对。论文自身在 Limitations 承认这一点，但标题未作限定。ACL ARR 要求 claims match evidence。
- 建议：标题加 "English-Chinese" 限定，或增加 1-2 个语言对。

**N2** [critical] **"Inherit" 因果措辞缺乏因果证据**
- 标题核心动词 "Inherit" 意味因果关系，但实际证据仅是 CI 重叠的相关性。未提供任何因果实验（如 ablation 去除 cross-lingual alignment 后观察变化）。
- 建议：替换为 "Mirror" 或 "Parallel"，或设计因果实验。

**N3** [critical] **Steering 证据不足以支撑 detection-decision dissociation 作为通用发现**
- Steering 仅在 Llama L13 成功（Fisher p = 0.002），Qwen/Gemma 全面失败（zero directional flips）。但 abstract 用 "demonstrate" 暗示通用性。
- 建议：限定为 "in Llama" 或降级为 observation。

### Should-Fix 问题

**W1** 遗漏重要相关工作：Pokharel et al. 2026 "Cross-Lingual Activation Steering" (arXiv:2601.16390)、"Steering into New Embedding Spaces" (arXiv:2502.15639)、"Steering Knowledge Selection Behaviours" (arXiv:2410.15999)

**W2** Contribution 2（detection-decision dissociation）缺乏泛化性，仅在 Llama 观察到。

**W3** Confound exclusion pipeline 局限性未充分讨论：Qwen COMET tercile Δ = −1.7 pp (p = 0.061) 接近边界；Llama token overlap weak negative correlation (r = −0.15, p = 0.014)。

**W4** 对 Qwen/Gemma steering 失败的分析不足——高精度 probe 方向在 steering 时无效的 mechanistic 原因未讨论。

**W5** 新颖性相对 Zhao et al. 2024 的增量贡献需更明确定位。

### Questions for Authors
1. XNLI 和 conflict probing 的 CI 重叠能否排除不同机制碰巧量级相近？
2. Qwen/Gemma steering 失败是否可能是方法本身的局限而非反映 dissociation 缺失？
3. 模型间样本差异（Llama 1368 / Qwen 966 / Gemma 1590）是否影响跨模型比较公平性？
4. 翻译用 Qwen3-SB 与实验模型 Qwen3-8B 同系列，是否存在 tokenization 偏好风险？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-24T16:42:27.008161+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 Reviewer 2\n\n### Must-Fix\n\n**[AGREE] R2-N1 (标题 \"Cross-Lingual\" 过度泛化)**: 同意。仅 EN-ZH 一个语言对，EN-DE 分析仅涉及 token overlap 非完整 pipeline。标题应加限定或增加语言对。\n\n**[AGREE] R2-N2 (\"Inherit\" 因果措辞)**: 强烈同意。与我的 N2（TOST 不显著）直接相关。CI 重叠 + 方向一致仅是相关性，TOST 未通过。\"Mirror\"/\"Parallel\" 更准确。\n\n**[AGREE] R2-N3 (Steering 泛化性不足)**: 完全同意，与我的 N3 一致。Abstract 用 \"demonstrate\" 过强。\n\n### Should-Fix\n\n**[REBUT] R2-W1 (遗漏相关工作)**: 部分反驳。论文 Related Work 已覆盖主要 steering 和跨语言文献。R2 列出的 3 篇论文需验证真实性和相关性，且应说明具体对比点。\n\n**[AGREE] R2-W2 (Contribution 2 泛化性)**: 同意，与 N3 一致。\n\n**[REBUT] R2-W3 (Confound 局限性)**: 同意一般性关切（与我的 W2 一致），但 **R2 引用数据有误**：R2 称 \"Qwen COMET tercile Δ=−1.7pp (p=0.061)\"——Table 2 实际为 Qwen Δ=−5.6pp, p=0.695；Llama Δ=+1.7pp, p=0.761。R2 将 Llama 的数值误归 Qwen，p 值也不对应论文任何数字。Token overlap p=0.014 实际为 p=0.012。问题是 power 不足，非\"接近显著\"。\n\n**[AGREE] R2-W4 (Qwen/Gemma 失败 mechanistic 分析)**: 同意。论文应讨论可能原因（非线性机制、attention 架构差异、样本量限制）。\n\n**[REBUT] R2-W5 (相对 Zhao 2024 增量)**: 部分反驳。Zhao 2024 是单模型单语言 probing。本文的 confound exclusion pipeline、XNLI baseline 设计、多模型 steering 比较具有独立方法论价值，非简单\"换语言重跑\"。\n\n### 主要分歧\n\n| 议题 | R1 | R2 | 性质 |\n|------|----|----|------|\n| 新颖性 | 方法论扩展有价值 (REBUT) | 增量 | 实质分歧 |\n| 遗漏相关工作 | 需验证 (REBUT) | 列 3 篇 | 需澄清 |\n| Confound 数据 | R2 数据有误 (REBUT) | Qwen Δ=−1.7pp | 事实性分歧 |\n| Overall | 3.5 | 3.0 | R2 更严格 |\n\n0.5 分差异来自新颖性判断。如果作者修复标题 framing + multi-seed，Soundness 可提升至 4/5，整体可达 Conference。",
  "reviewer_id": "1",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 Reviewer 2\n\n### Must-Fix\n\n**[AGREE] R2-N1 (标题 \"Cross-Lingual\" 过度泛化)**: 同意。仅 EN-ZH 一个语言对，EN-DE 分析仅涉及 token overlap 非完整 pipeline。标题应加限定或增加语言对。\n\n**[AGREE] R2-N2 (\"Inherit\" 因果措辞)**: 强烈同意。与我的 N2（TOST 不显著）直接相关。CI 重叠 + 方向一致仅是相关性，TOST 未通过。\"Mirror\"/\"Parallel\" 更准确。\n\n**[AGREE] R2-N3 (Steering 泛化性不足)**: 完全同意，与我的 N3 一致。Abstract 用 \"demonstrate\" 过强。\n\n### Should-Fix\n\n**[REBUT] R2-W1 (遗漏相关工作)**: 部分反驳。论文 Related Work 已覆盖主要 steering 和跨语言文献。R2 列出的 3 篇论文需验证真实性和相关性，且应说明具体对比点。\n\n**[AGREE] R2-W2 (Contribution 2 泛化性)**: 同意，与 N3 一致。\n\n**[REBUT] R2-W3 (Confound 局限性)**: 同意一般性关切（与我的 W2 一致），但 **R2 引用数据有误**：R2 称 \"Qwen COMET tercile Δ=−1.7pp (p=0.061)\"——Table 2 实际为 Qwen Δ=−5.6pp, p=0.695；Llama Δ=+1.7pp, p=0.761。R2 将 Llama 的数值误归 Qwen，p 值也不对应论文任何数字。Token overlap p=0.014 实际为 p=0.012。问题是 power 不足，非\"接近显著\"。\n\n**[AGREE] R2-W4 (Qwen/Gemma 失败 mechanistic 分析)**: 同意。论文应讨论可能原因（非线性机制、attention 架构差异、样本量限制）。\n\n**[REBUT] R2-W5 (相对 Zhao 2024 增量)**: 部分反驳。Zhao 2024 是单模型单语言 probing。本文的 confound exclusion pipeline、XNLI baseline 设计、多模型 steering 比较具有独立方法论价值，非简单\"换语言重跑\"。\n\n### 主要分歧\n\n| 议题 | R1 | R2 | 性质 |\n|------|----|----|------|\n| 新颖性 | 方法论扩展有价值 (REBUT) | 增量 | 实质分歧 |\n| 遗漏相关工作 | 需验证 (REBUT) | 列 3 篇 | 需澄清 |\n| Confound 数据 | R2 数据有误 (REBUT) | Qwen Δ=−1.7pp | 事实性分歧 |\n| Overall | 3.5 | 3.0 | R2 更严格 |\n\n0.5 分差异来自新颖性判断。如果作者修复标题 framing + multi-seed，Soundness 可提升至 4/5，整体可达 Conference。",
    "reviewer_id": "1",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-24T16:42:31.025679+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4017
}
```

</details>

---

### Assistant

_source line 124 · 2026-05-24T16:42:36.615179+00:00_

交叉回应已提交给 Review Director。

核心判断：与 R2 在 3 个 Must-Fix 上完全一致（标题泛化、"Inherit" 因果措辞、steering 泛化性）。主要分歧在 Should-Fix 层面——R2 的 confound 数据引用有事实错误（Qwen/Llama 数值混淆），以及对 Zhao et al. 2024 增量性的判断（我认为 confound pipeline 和 XNLI baseline 有独立方法论价值，不应定性为增量）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1"
}
```

</details>

---

## Round 5

46 recorded events

### User

_source line 125 · 2026-05-25T04:18:54.770667+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性**审查。

## 论文信息
- 标题：English-Chinese Knowledge Conflict Signals Mirror General Cross-Lingual Asymmetries
- 论文路径：projects/clkc_mech_interp/docs/paper/main.tex
- PDF 路径：/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/submitted.pdf
- 目标 venue：EMNLP 2026（ARR Long Paper）

## Venue 要求
- ARR 提交截止：2026-05-25
- 正文 8 页限制 + 无限参考文献
- Limitations 章节必须有，不计入页数
- Double-blind 审稿
- ACL 模板

## 你的审查侧重

请从以下维度严格评审：

### 1. 探针方法论
- Logistic regression probe 的选择是否合理？是否讨论了 probe complexity 与表征信息的关系（Hewitt & Liang 2019 selectivity concern）？
- 单一 seed + bootstrap CI 是否足以支撑结论？论文承认单 split 局限但未做 cross-validation
- Balanced accuracy 作为唯一指标是否充分？是否需要 AUROC 或其他指标？
- Last-token aggregation 的选择是否充分论证？

### 2. 统计分析
- Fisher's exact test 用于 steering flip rate 对比是否合适？样本量（N=131-171）下的统计功效如何？
- Bonferroni 校正的 family-wise 定义是否合理（per-layer k=10 vs 全局 30 tests）？
- TOST 等价检验（±2pp margin）功效仅 1.4%——这是否削弱了"mirror"的核心主张？
- Qwen 的 $\Delta_{asym}$ CI 包含零——论文如何处理？

### 3. 混淆因素排除
- COMET tercile ablation 的功效分析（MDD=25.3pp）是否表明该分析无法排除翻译质量的影响？
- Qwen3-8B 同时作为翻译模型和实验对象——这一双重角色的风险是否充分讨论？
- Token overlap 分析仅使用 Jaccard similarity——是否存在更精细的词汇重叠度量？

### 4. Steering 实验设计
- $\alpha$ 值的选择（±1, ±2, ±5, ±10, ±20）是否有理论依据？
- Steering 仅在 Llama L13 成功，但论文标题暗示这是跨模型发现——这一张力如何评价？
- Random control 的设计是否充分？是否应该使用其他方向（如其他层的 probe direction）作为对照？
- "Coherence collapse" at α=+20 的处理是否充分？

### 5. 可复现性
- 代码/数据是否有可用性声明？
- 实验细节是否足以复现（hyperparameters、random seeds、compute requirements）？

请输出标准审稿格式：Summary → Strengths → Weaknesses（按 severity: Must-Fix / Should-Fix / Minor 分级）→ Questions → 建议评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-25T04:19:06.838452+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_1_cb1fcd17/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_1_cb1fcd17/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-25T04:19:06.839040+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_1_cb1fcd17.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-25T04:19:08.896800+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
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

_source line 129 · 2026-05-25T04:19:08.998499+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-25T04:19:13.988222+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-25T04:19:14.995382+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer form dimensions soundness excitement 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer form dimensions soundness excitement 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-25T04:19:16.803749+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/submitted.pdf",
  "project": "clkc_mech_interp",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/submitted.pdf",
    "project": "clkc_mech_interp",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-25T04:19:21.221764+00:00_

Web search results for query: "ACL Rolling Review reviewer form dimensions soundness excitement 2025 2026"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, I found information about the ACL Rolling Review (ARR) reviewer form dimensions for 2025 and 2026:

## Three Score Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Dimension

Soundness assesses whether the paper is sufficiently sound and thorough, clearly states scientific claims and provides adequate support for them, considering the depth and/or breadth of research questions investiga
…[truncated 787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6226
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-25T04:19:21.524276+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results for ACL ARR 2026 reviewer guidelines, here's what I found:

## Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Assessment Score

The Overall assessment score is an explicit recomme
…[truncated 1132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7536
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-25T04:19:23.035108+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 483.5}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_
…[truncated 317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6231
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-25T04:19:33.423888+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all dimensions, their scoring scales (1-5 or other), descriptions of each score level, and any additional questions reviewers must answer. Include the full text of soundness, excitement, and overall assessment scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all dimensions, their scoring scales (1-5 or other), descriptions of each score level, and any additional questions reviewers must answer. Include the full text of soundness, excitement, and overall assessment scales."
  }
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-25T04:19:33.875623+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-25T04:19:34.885279+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1009
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-25T04:19:34.885600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-25T04:19:35.396010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-25T04:19:36.000702+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-25T04:19:36.253089+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1367
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-25T04:19:36.253521+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-25T04:19:36.859917+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1463
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-25T04:19:37.669189+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1668
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-25T04:19:37.771655+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1518
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-25T04:19:44.848087+00:00_

# ACL Rolling Review Form - Complete Structure

## Core Review Dimensions

### 1. Paper Summary
Open-ended section requesting description of paper topic and clarification of any misunderstandings.

### 2. Summary of Strengths
Open-ended section asking reviewers to identify "major reasons to publish this paper at a selective *ACL venue."

### 3. Summary of Weaknesses
Numbered concerns about correctness, impact, clarity, or other factors that would prioritize other papers.

### 4. Comments/Suggestions/Typos
Open-ended section for improvement suggestions beyond addressing main concerns.

### 5. Reviewer Confidence
**Scale: 1-5**
- 5 = "Positive that my evaluation is correct"
- 4 = "Quite sure" with unlikely missed details
- 3 = "Pretty sure" but possible gaps in technical verification
- 2 = "Willing to defend" but likely missed some details
- 1 = Outside expertise or very difficult to understand

### 6. Soundness
**Scale: 1-5 (with .5 increments)**
- 5 = Most thorough study of its type
- 4 = Sufficient support for claims; extra experiments optional
- 3 = Sufficient main claim support; minor points need details
- 2 = Major claims lack support; significant technical problems
- 1 = Insufficient rigor or irrelevant to ACL

### 7. Excitement
**Scale: 1-5 (with .5 increments)**
- 5 = "Highly Exciting"; would recommend to others
- 4 = Would mention to colleagues; effort to attend presentation
- 3 = Might mention points; attend if time permits
- 2 = Doesn't resonate personally but potentially interesting to community
- 1 = Not exciting; unlikely to resonate with ACL community

### 8. Overall Assessment
**Scale: 1-5 (with .5 increments)**
- 5 = Award consideration (top 2.5% papers)
- 4.5 = Borderline award
- 4 = Conference acceptance
- 3.5 = Borderline conference
- 3 = Accept to Findings
- 2.5 = Borderline Findings
- 2 = Substantial revisions needed for next cycle
- 1.5 = Substantial revisions requiring longer timeline
- 1 = Do not resubmit; not relevant to computational lingui
…[truncated 1500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 11424
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-25T04:19:54.699492+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-25T04:19:55.254356+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-25T04:19:55.757786+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1058
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-25T04:19:55.758217+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-25T04:19:56.615967+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-25T04:19:56.619539+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 861
}
```

</details>

---

### Tool call

_source line 154 · 2026-05-25T04:19:56.621271+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-25T04:19:56.974068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-25T04:19:57.682278+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1060
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-25T04:19:57.884216+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-25T04:20:04.726573+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/submitted.pdf",
  "project": "clkc_mech_interp",
  "pages": "11",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/submitted.pdf",
    "project": "clkc_mech_interp",
    "pages": "11",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-25T04:20:05.230791+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.9}], \"total_pages\": 11, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 504
}
```

</details>

---

### Tool call

_source line 160 · 2026-05-25T04:20:07.190461+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what constitutes a sound paper, what reviewers should check regarding methodology, statistical analysis, reproducibility, and any specific instructions about how to assess experimental papers. Include any guidance on scoring standards."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what constitutes a sound paper, what reviewers should check regarding methodology, statistical analysis, reproducibility, and any specific instructions about how to assess experimental papers. Include any guidance on scoring standards."
  }
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-25T04:20:14.780336+00:00_

# ARR Reviewer Guidelines: Assessment Standards and Methodology

## Sound Paper Requirements

Papers should be **technically sound with appropriate scoping**. This requires:

- Clear research questions and contributions addressing identified knowledge gaps
- Complete assumptions and proofs (when applicable)
- Sufficient evidence supporting all claims, not mere speculation
- Appropriate statistical analysis with significance assessment when applicable

## Methodology Assessment (M-codes)

Reviewers should examine:

**M1 - LLM Evaluation**: "If LLMs are used as automated evaluators, is their reliability in this context sufficiently validated?"

**M2 - Reproducibility**: Check sufficient detail for experiment reproduction, including hyperparameters and code/data availability plans. This concerns *reproducibility* (running same experiments with similar results) rather than replicability.

**M3 - Data Quality**: Watch for undisclosed dataset issues not addressed in papers providing resources.

**M4 - Selection Justification**: Verify that model and benchmark selections align with contribution claims through clear motivation.

**M5 - Formal Completeness**: All assumptions must be clearly stated; theorems/proofs require complete supporting arguments.

## Statistical Analysis (R-code)

**R5 - Statistical Significance**: Main results should include error bars, confidence intervals, or significance tests with computational methodology disclosed.

Avoid p-hacking and presenting "best" results from unknown trial quantities, including prompt engineering variations.

## Experimental Results Assessment (R-codes)

**R1 - Analysis Issues**: Flag inappropriate statistics, misleading presentations, or insufficiently tuned baselines.

**R2 - Claims Scope**: Verify evaluations represent populations referenced in claims (e.g., few benchmarks ≠ general reasoning capability).

**R3 - Evidence-Based**: Ensure conclusions derive from provided evidence or cited work, not speculation.

**R4 - 
…[truncated 356 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7589
}
```

</details>

---

### Tool call

_source line 162 · 2026-05-25T04:20:17.494751+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-25T04:20:18.350538+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-25T04:24:26.895713+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — 方法严谨性审查\n\n## Paper Summary\n\n本文研究多语言 LLM 在英中知识冲突场景下的内部表征机制。基于 ConflictQA 数据集，作者在三个模型架构（Llama-3.1-8B-Instruct、Qwen3-8B、Gemma-2-9B-IT）上训练 L2 正则化 logistic regression 探针，分析冲突信号的可检测性和跨语言迁移模式。核心发现：(1) 冲突信号在残差流中线性可分；(2) 中→英探针迁移比英→中高约 7pp，呈方向性不对称；(3) 该不对称与 XNLI 非冲突基线一致，暗示反映的是通用跨语言结构而非冲突特异性编码；(4) 因果干预（steering）仅在 Llama L13 成功；(5) 可检测性不蕴含因果影响。\n\n## 主要优势\n\n- **系统性强**：三个架构、四个迁移方向的完整 probing 矩阵，加上 XNLI 非冲突基线和三类混淆排除（COMET tercile、token overlap、XNLI），实验设计有层次感。\n- **检测与因果的明确区分**：论文清晰地指出 probe accuracy ≠ causal relevance，并通过 steering 实验验证，发现仅 Llama L13 有因果效应。这一区分在 probing 文献中经常被忽略，值得肯定。\n- **透明报告统计局限**：TOST 功效仅 1.4%、COMET 消融 MDD=25.3pp、Qwen Δ_asym CI 包含零——这些弱点均被主动报告，而非隐藏。\n- **独立复制**（Appendix C）：用不同 seed（N=201）和不同 train/test split 复制了 L13 因果效应，增强了该特定发现的可信度。\n- **Matched-condition steering**（Appendix D）：在 matched 条件下确认三个架构均表现出与主实验一致的方向，排除了 confound 驱动的虚假因果效应。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5（Borderline Conference）\n\n**一句话总结**: 实验设计系统、统计报告透明，但核心 \"mirror\" 主张与统计证据之间存在显著张力——等价检验无功效、混淆排除无统计力、因果证据限于单模型。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要主张有支撑但关键统计检验（TOST、COMET 消融）功效不足，削弱核心等价主张 |\n| Excitement | 3/5 | 跨语言冲突机制是有价值的方向，但发现偏向描述性、因果洞察有限 |\n| Reproducibility | 3/5 | 超参数基本齐全，但缺乏明确的代码/数据开放声明，单 split 设计难以验证 |\n| Confidence | 4/5 | 对探针方法论和统计分析有扎实理解，仔细审查了全文及附录 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 标题 \"Mirror\" 主张与 TOST 等价检验结果之间的根本张力\n\n- 具体位置：Title、Section 4.4（Non-Conflict Baseline Comparison）、Figure 3\n- 问题：论文标题宣称冲突信号 \"mirror\" 通用跨语言不对称，但支撑这一等价主张的正式统计检验（TOST，±2pp margin）功效仅 1.4%（Section 4.4：\"post-hoc power analysis shows only 1.4% power at this margin\"）。达到 80% 功效需要 ±12.5pp margin，而观测到的 Δ_asym 本身才 ~7pp。这意味着 TOST 检验本质上是不可信息化的（uninformative）——它既无法支持等价，也无法否定等价。论文转而依赖 \"CI 重叠\"作为替代论据，但 CI 重叠不等同于等价检验（Schenker & Gentleman, 2001）。\n- 为什么影响接收：标题中的核心主张（\"mirror\"）缺乏形式化统计支撑。如果 TOST 无功效且论文不提供替代的等价检验方法，则 \"mirror\" 从断言降级为观察性假说。这直接影响论文的 novelty claim 和 contribution scope。\n- 建议修改方向：(a) 将标题从 \"mirror\" 改为更保守的措辞，如 \"resemble\" 或 \"are consistent with\"；(b) 或者，用更高 power 的等价检验方法（如 Bayesian equivalence testing with informative priors）提供正式证据；(c) 明确承认 \"mirror\" 是描述性观察而非统计结论。\n\n**N2** [critical] COMET tercile 消融的 MDD=25.3pp 使翻译质量混淆排除本质上无效\n\n- 具体位置：Section 4.5（Confound Exclusion — Translation quality）、Table 2\n- 问题：论文用 COMET 分数将样本分为高/中/低质量三等分，比较 EN→ZH probe accuracy 在高 vs 低 tercile 之间的差异。但 80% 功效下的最小可检测差异（MDD）为 25.3pp（每 tercile 仅约 56 个样本）。观测到的不对称效应本身只有 ~7pp。这意味着即使翻译质量解释了全部 7pp 不对称，这一分析也检测不到。特别值得注意的是 Gemma 的 Δ=+10.3pp（Table 2）——虽然不显著（p=0.278），但这一效应大小本身已经接近观测到的主效应，却因为 underpowered 而被标记为\"无显著影响\"。\n- 为什么影响接收：论文将此分析作为排除翻译质量混淆的主要证据（Section 4.5 第一段），但分析实际上无力排除任何合理大小的混淆效应。对于一篇以混淆排除为核心方法论贡献之一的论文，这一缺陷是实质性的。\n- 建议修改方向：(a) 明确标注此分析为 underpowered 且不能作为排除翻译质量混淆的充分证据（目前的表述 \"far exceeding observed effects\" 容易让读者误解为是好消息）；(b) 考虑使用连续的 COMET 分数作为回归协变量（而非离散化 tercile），以提高统计功效；(c) 或者增加样本量使 tercile 分析有意义。\n\n**N3** [critical] 因果证据限于单模型单层，与标题/摘要的跨模型叙事不匹配\n\n- 具体位置：Section 4.6、Section 5（Discussion）、Table 3、Abstract\n- 问题：Steering 仅在 Llama L13 产生显著因果效应（Fisher p=0.002），Qwen 和 Gemma 在所有层和所有 α 值上均无显著效应（Qwen: \"best p=0.785\"; Gemma: \"best p=0.148\"；Section 5 第 3 段）。论文标题和摘要的措辞（\"We probe residual stream representations in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT\"）给读者的印象是三个模型产生了对等的发现，但因果层面的核心发现实际上只属于 Llama。\n- 为什么影响接收：因果可干预性是论文超越纯相关性 probing 研究的关键差异化点。如果这一差异化点仅限于 3 个模型中的 1 个，则论文对 \"跨模型一般性\" 的暗示是误导性的。审稿人可能会质疑：Llama L13 的因果效应是否仅仅是架构特异性的巧合，而非可推广的机制性发现？\n- 建议修改方向：(a) 在摘要和结论中更清晰地区分 \"检测\"（跨模型一致）和 \"因果影响\"（仅 Llama）的范围；(b) 讨论 Qwen/Gemma steering 失败的可能原因时（Section 5 \"Why does steering fail\" 已有初步讨论），提供更系统的分析——例如是否因为这些模型的冲突解决机制涉及非线性交互或分布在多层上；(c) 考虑用其他因果干预方法（如 causal mediation analysis、activation patching）在 Qwen/Gemma 上寻找因果证据。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 单一 train/test split 的探针结果缺乏 cross-validation 验证\n\n- 具体位置：Section 3.3、Limitations\n- 问题：所有 probing 结果基于单一 train/test split + bootstrap CI（n=2,000）。Bootstrap CI 量化的是给定 split 下的估计不确定性，但不解决 split 依赖性问题。如果该 split 恰好有利于某些方向的迁移，所有不对称结论都可能被影响。Appendix C 的独立复制仅覆盖 steering（N=201），不覆盖 probing 精度。论文在 Limitations 中承认 \"all probing results are based on a single train/test split with bootstrap confidence intervals capturing within-split variability\"，但未采取行动。\n- 建议：报告 5-fold 或 10-fold cross-validation 的 probe accuracy，或至少在 3 个不同 random split 上复制主要 probing 结果（Table 1），以确认不对称方向和量级的稳定性。\n\n**W2** [warning] Qwen3-8B 同时作为翻译模型和实验对象的双重角色风险未充分控制\n\n- 具体位置：Section 3.2（Translation）、Limitations\n- 问题：Qwen3-8B 用于将所有英文输入翻译为中文（Section 3.2），同时也是三个被探测的模型之一。如果 Qwen 的翻译输出系统性地偏向其自身的处理模式（例如倾向于生成它自己更容易 \"理解\" 的表述），那么 Qwen 上的探针结果可能存在自我增强偏差。论文在 Limitations 中提及此问题但仅以 \"COMET-based quality control and Llama/Gemma cross-validation mitigate this dual-role concern\" 一笔带过。然而 COMET 只衡量翻译的总体质量，不衡量翻译是否偏向 Qwen 的 tokenization 或内部表征偏好。\n- 建议：(a) 使用另一个翻译模型（如 Google Translate API 或 NLLB）重新翻译一个子集，在 Qwen 上对比两组翻译的 probe accuracy 是否有显著差异；(b) 至少分析 Qwen 翻译的 self-BLEU 或其他指标，检查是否有系统性 \"self-favoring\" 模式。\n\n**W3** [warning] Probe selectivity（Hewitt & Liang, 2019）未被正式评估\n\n- 具体位置：Section 3.3\n- 问题：论文引用了 Hewitt & Liang (2019)（在 Section 1 和 Section 3.3），但未计算其提出的 selectivity 指标——即 probe 在 control task 上的精度与目标 task 之间的差异。XNLI 基线（Section 3.5）部分承担了这一角色，但其设计目的不同（它测试的是 \"不对称是否冲突特异\" 而非 \"probe 是否有选择性\"）。一个高 probe accuracy 可能仅仅反映残差流的高维几何特性，而非真正的冲突信号编码。\n- 建议：计算 control selectivity（例如用 random label 训练的 probe accuracy 作为基线），确认报告的 probe accuracy 显著高于 selectivity baseline。\n\n**W4** [warning] Balanced accuracy 作为唯一探针性能指标不够充分\n\n- 具体位置：Section 3.3、Table 1\n- 问题：论文仅报告 balanced accuracy（Section 3.3: \"We report balanced accuracy to account for class imbalance\"）。对于二分类 probing 任务，AUROC 是更信息丰富的指标——它不依赖于阈值选择，能更好地反映表征中的信号强度。尤其是在跨语言迁移场景下，不同方向的 probe 可能具有不同的校准特性，仅看 balanced accuracy 可能遗漏重要信息。\n- 建议：补充报告 AUROC（至少在附录中），确认不对称模式在不同指标下一致。\n\n**W5** [warning] Steering 实验的 α 值选择缺乏理论依据\n\n- 具体位置：Section 3.6\n- 问题：论文扫描 α ∈ {±1, ±2, ±5, ±10, ±20}（Section 3.6），但未解释这些值为何合理。α=±20 导致 coherence collapse（Section 4.6 和 Appendix Table 4），而 α=±1 基本无效应。有效范围（α=±5 到 ±10）的选择看起来是事后确定的。此外，α 的绝对值依赖于 probe 方向向量的 norm，而不同层的 norm 不同——是否做了归一化处理？\n- 建议：(a) 将 α 值相对于 probe direction 的 norm 归一化，报告 α/||w|| 以增强跨层可比性；(b) 讨论 α 选择的依据，或至少说明这是一个 grid search 并报告了所有结果（而非 cherry-picking）。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Section 3.2 提到 \"质量 validated by COMET\"，但 COMET 的具体版本（wmt20-comet-da? wmt22-comet-da?）和阈值未在正文中说明（仅在 \"quality-validated\" 中一带而过）。应明确 COMET model ID 和筛选标准。\n- **M2**: Token overlap 分析仅使用 Jaccard similarity（Section 4.5）。字符级或 BPE-aware 的重叠度量可能更准确地捕捉 tokenization 对跨语言迁移的影响。\n- **M3**: 代码和数据的可用性声明不清晰。Section A（AI Use）提到使用了 Claude 辅助编码，但未说明代码/数据是否会公开。ARR 的 reproducibility 维度（M2）明确要求 \"code/data availability plans\"。\n- **M4**: Random direction control（Section 3.6: \"a random direction vector of equal norm\"）是最低标准的控制。使用其他层的 probe direction 或 random subspace 中的方向作为额外对照，能更有力地排除 steering 效应是非特异性扰动的可能。\n- **M5**: Figure 3 的灰色 ±2pp 等价区间在视觉上暗示 TOST 是有效的等价检验，但实际上 TOST 在该 margin 下几乎无功效。建议在图注中明确标注 TOST 功效不足，或移除该视觉元素以避免误导。\n\n---\n\n## Questions for Authors\n\n1. 如果使用 5-fold cross-validation 替代单一 split，Δ_asym 的方向和量级是否稳定？是否有任何 fold 出现不对称方向翻转？\n2. Qwen 和 Gemma 上 steering 失败——作者是否尝试过 activation patching 或其他因果干预方法？如果 steering 的失败是由于非线性交互，这些替代方法可能更适用。\n3. COMET tercile 消融中 Gemma 的 Δ=+10.3pp 虽然不显著，但效应大小已接近主效应（~7pp）。作者如何解释这一数值？是否担心翻译质量可能在 Gemma 上部分解释了不对称？\n4. 论文使用 last-token aggregation——是否评估过其他 aggregation 策略（如 mean pooling、attention-weighted）？不同语言的最后一个 token 可能承载不同信息量。\n5. 对于 \"mirror\" 这一核心主张，作者能否提供一个 Bayesian equivalence testing 结果（例如 ROPE+HDI 方法），作为对 TOST 功效不足的补充？\n",
  "reviewer_id": "1",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — 方法严谨性审查\n\n## Paper Summary\n\n本文研究多语言 LLM 在英中知识冲突场景下的内部表征机制。基于 ConflictQA 数据集，作者在三个模型架构（Llama-3.1-8B-Instruct、Qwen3-8B、Gemma-2-9B-IT）上训练 L2 正则化 logistic regression 探针，分析冲突信号的可检测性和跨语言迁移模式。核心发现：(1) 冲突信号在残差流中线性可分；(2) 中→英探针迁移比英→中高约 7pp，呈方向性不对称；(3) 该不对称与 XNLI 非冲突基线一致，暗示反映的是通用跨语言结构而非冲突特异性编码；(4) 因果干预（steering）仅在 Llama L13 成功；(5) 可检测性不蕴含因果影响。\n\n## 主要优势\n\n- **系统性强**：三个架构、四个迁移方向的完整 probing 矩阵，加上 XNLI 非冲突基线和三类混淆排除（COMET tercile、token overlap、XNLI），实验设计有层次感。\n- **检测与因果的明确区分**：论文清晰地指出 probe accuracy ≠ causal relevance，并通过 steering 实验验证，发现仅 Llama L13 有因果效应。这一区分在 probing 文献中经常被忽略，值得肯定。\n- **透明报告统计局限**：TOST 功效仅 1.4%、COMET 消融 MDD=25.3pp、Qwen Δ_asym CI 包含零——这些弱点均被主动报告，而非隐藏。\n- **独立复制**（Appendix C）：用不同 seed（N=201）和不同 train/test split 复制了 L13 因果效应，增强了该特定发现的可信度。\n- **Matched-condition steering**（Appendix D）：在 matched 条件下确认三个架构均表现出与主实验一致的方向，排除了 confound 驱动的虚假因果效应。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5（Borderline Conference）\n\n**一句话总结**: 实验设计系统、统计报告透明，但核心 \"mirror\" 主张与统计证据之间存在显著张力——等价检验无功效、混淆排除无统计力、因果证据限于单模型。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要主张有支撑但关键统计检验（TOST、COMET 消融）功效不足，削弱核心等价主张 |\n| Excitement | 3/5 | 跨语言冲突机制是有价值的方向，但发现偏向描述性、因果洞察有限 |\n| Reproducibility | 3/5 | 超参数基本齐全，但缺乏明确的代码/数据开放声明，单 split 设计难以验证 |\n| Confidence | 4/5 | 对探针方法论和统计分析有扎实理解，仔细审查了全文及附录 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 标题 \"Mirror\" 主张与 TOST 等价检验结果之间的根本张力\n\n- 具体位置：Title、Section 4.4（Non-Conflict Baseline Comparison）、Figure 3\n- 问题：论文标题宣称冲突信号 \"mirror\" 通用跨语言不对称，但支撑这一等价主张的正式统计检验（TOST，±2pp margin）功效仅 1.4%（Section 4.4：\"post-hoc power analysis shows only 1.4% power at this margin\"）。达到 80% 功效需要 ±12.5pp margin，而观测到的 Δ_asym 本身才 ~7pp。这意味着 TOST 检验本质上是不可信息化的（uninformative）——它既无法支持等价，也无法否定等价。论文转而依赖 \"CI 重叠\"作为替代论据，但 CI 重叠不等同于等价检验（Schenker & Gentleman, 2001）。\n- 为什么影响接收：标题中的核心主张（\"mirror\"）缺乏形式化统计支撑。如果 TOST 无功效且论文不提供替代的等价检验方法，则 \"mirror\" 从断言降级为观察性假说。这直接影响论文的 novelty claim 和 contribution scope。\n- 建议修改方向：(a) 将标题从 \"mirror\" 改为更保守的措辞，如 \"resemble\" 或 \"are consistent with\"；(b) 或者，用更高 power 的等价检验方法（如 Bayesian equivalence testing with informative priors）提供正式证据；(c) 明确承认 \"mirror\" 是描述性观察而非统计结论。\n\n**N2** [critical] COMET tercile 消融的 MDD=25.3pp 使翻译质量混淆排除本质上无效\n\n- 具体位置：Section 4.5（Confound Exclusion — Translation quality）、Table 2\n- 问题：论文用 COMET 分数将样本分为高/中/低质量三等分，比较 EN→ZH probe accuracy 在高 vs 低 tercile 之间的差异。但 80% 功效下的最小可检测差异（MDD）为 25.3pp（每 tercile 仅约 56 个样本）。观测到的不对称效应本身只有 ~7pp。这意味着即使翻译质量解释了全部 7pp 不对称，这一分析也检测不到。特别值得注意的是 Gemma 的 Δ=+10.3pp（Table 2）——虽然不显著（p=0.278），但这一效应大小本身已经接近观测到的主效应，却因为 underpowered 而被标记为\"无显著影响\"。\n- 为什么影响接收：论文将此分析作为排除翻译质量混淆的主要证据（Section 4.5 第一段），但分析实际上无力排除任何合理大小的混淆效应。对于一篇以混淆排除为核心方法论贡献之一的论文，这一缺陷是实质性的。\n- 建议修改方向：(a) 明确标注此分析为 underpowered 且不能作为排除翻译质量混淆的充分证据（目前的表述 \"far exceeding observed effects\" 容易让读者误解为是好消息）；(b) 考虑使用连续的 COMET 分数作为回归协变量（而非离散化 tercile），以提高统计功效；(c) 或者增加样本量使 tercile 分析有意义。\n\n**N3** [critical] 因果证据限于单模型单层，与标题/摘要的跨模型叙事不匹配\n\n- 具体位置：Section 4.6、Section 5（Discussion）、Table 3、Abstract\n- 问题：Steering 仅在 Llama L13 产生显著因果效应（Fisher p=0.002），Qwen 和 Gemma 在所有层和所有 α 值上均无显著效应（Qwen: \"best p=0.785\"; Gemma: \"best p=0.148\"；Section 5 第 3 段）。论文标题和摘要的措辞（\"We probe residual stream representations in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT\"）给读者的印象是三个模型产生了对等的发现，但因果层面的核心发现实际上只属于 Llama。\n- 为什么影响接收：因果可干预性是论文超越纯相关性 probing 研究的关键差异化点。如果这一差异化点仅限于 3 个模型中的 1 个，则论文对 \"跨模型一般性\" 的暗示是误导性的。审稿人可能会质疑：Llama L13 的因果效应是否仅仅是架构特异性的巧合，而非可推广的机制性发现？\n- 建议修改方向：(a) 在摘要和结论中更清晰地区分 \"检测\"（跨模型一致）和 \"因果影响\"（仅 Llama）的范围；(b) 讨论 Qwen/Gemma steering 失败的可能原因时（Section 5 \"Why does steering fail\" 已有初步讨论），提供更系统的分析——例如是否因为这些模型的冲突解决机制涉及非线性交互或分布在多层上；(c) 考虑用其他因果干预方法（如 causal mediation analysis、activation patching）在 Qwen/Gemma 上寻找因果证据。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 单一 train/test split 的探针结果缺乏 cross-validation 验证\n\n- 具体位置：Section 3.3、Limitations\n- 问题：所有 probing 结果基于单一 train/test split + bootstrap CI（n=2,000）。Bootstrap CI 量化的是给定 split 下的估计不确定性，但不解决 split 依赖性问题。如果该 split 恰好有利于某些方向的迁移，所有不对称结论都可能被影响。Appendix C 的独立复制仅覆盖 steering（N=201），不覆盖 probing 精度。论文在 Limitations 中承认 \"all probing results are based on a single train/test split with bootstrap confidence intervals capturing within-split variability\"，但未采取行动。\n- 建议：报告 5-fold 或 10-fold cross-validation 的 probe accuracy，或至少在 3 个不同 random split 上复制主要 probing 结果（Table 1），以确认不对称方向和量级的稳定性。\n\n**W2** [warning] Qwen3-8B 同时作为翻译模型和实验对象的双重角色风险未充分控制\n\n- 具体位置：Section 3.2（Translation）、Limitations\n- 问题：Qwen3-8B 用于将所有英文输入翻译为中文（Section 3.2），同时也是三个被探测的模型之一。如果 Qwen 的翻译输出系统性地偏向其自身的处理模式（例如倾向于生成它自己更容易 \"理解\" 的表述），那么 Qwen 上的探针结果可能存在自我增强偏差。论文在 Limitations 中提及此问题但仅以 \"COMET-based quality control and Llama/Gemma cross-validation mitigate this dual-role concern\" 一笔带过。然而 COMET 只衡量翻译的总体质量，不衡量翻译是否偏向 Qwen 的 tokenization 或内部表征偏好。\n- 建议：(a) 使用另一个翻译模型（如 Google Translate API 或 NLLB）重新翻译一个子集，在 Qwen 上对比两组翻译的 probe accuracy 是否有显著差异；(b) 至少分析 Qwen 翻译的 self-BLEU 或其他指标，检查是否有系统性 \"self-favoring\" 模式。\n\n**W3** [warning] Probe selectivity（Hewitt & Liang, 2019）未被正式评估\n\n- 具体位置：Section 3.3\n- 问题：论文引用了 Hewitt & Liang (2019)（在 Section 1 和 Section 3.3），但未计算其提出的 selectivity 指标——即 probe 在 control task 上的精度与目标 task 之间的差异。XNLI 基线（Section 3.5）部分承担了这一角色，但其设计目的不同（它测试的是 \"不对称是否冲突特异\" 而非 \"probe 是否有选择性\"）。一个高 probe accuracy 可能仅仅反映残差流的高维几何特性，而非真正的冲突信号编码。\n- 建议：计算 control selectivity（例如用 random label 训练的 probe accuracy 作为基线），确认报告的 probe accuracy 显著高于 selectivity baseline。\n\n**W4** [warning] Balanced accuracy 作为唯一探针性能指标不够充分\n\n- 具体位置：Section 3.3、Table 1\n- 问题：论文仅报告 balanced accuracy（Section 3.3: \"We report balanced accuracy to account for class imbalance\"）。对于二分类 probing 任务，AUROC 是更信息丰富的指标——它不依赖于阈值选择，能更好地反映表征中的信号强度。尤其是在跨语言迁移场景下，不同方向的 probe 可能具有不同的校准特性，仅看 balanced accuracy 可能遗漏重要信息。\n- 建议：补充报告 AUROC（至少在附录中），确认不对称模式在不同指标下一致。\n\n**W5** [warning] Steering 实验的 α 值选择缺乏理论依据\n\n- 具体位置：Section 3.6\n- 问题：论文扫描 α ∈ {±1, ±2, ±5, ±10, ±20}（Section 3.6），但未解释这些值为何合理。α=±20 导致 coherence collapse（Section 4.6 和 Appendix Table 4），而 α=±1 基本无效应。有效范围（α=±5 到 ±10）的选择看起来是事后确定的。此外，α 的绝对值依赖于 probe 方向向量的 norm，而不同层的 norm 不同——是否做了归一化处理？\n- 建议：(a) 将 α 值相对于 probe direction 的 norm 归一化，报告 α/||w|| 以增强跨层可比性；(b) 讨论 α 选择的依据，或至少说明这是一个 grid search 并报告了所有结果（而非 cherry-picking）。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Section 3.2 提到 \"质量 validated by COMET\"，但 COMET 的具体版本（wmt20-comet-da? wmt22-comet-da?）和阈值未在正文中说明（仅在 \"quality-validated\" 中一带而过）。应明确 COMET model ID 和筛选标准。\n- **M2**: Token overlap 分析仅使用 Jaccard similarity（Section 4.5）。字符级或 BPE-aware 的重叠度量可能更准确地捕捉 tokenization 对跨语言迁移的影响。\n- **M3**: 代码和数据的可用性声明不清晰。Section A（AI Use）提到使用了 Claude 辅助编码，但未说明代码/数据是否会公开。ARR 的 reproducibility 维度（M2）明确要求 \"code/data availability plans\"。\n- **M4**: Random direction control（Section 3.6: \"a random direction vector of equal norm\"）是最低标准的控制。使用其他层的 probe direction 或 random subspace 中的方向作为额外对照，能更有力地排除 steering 效应是非特异性扰动的可能。\n- **M5**: Figure 3 的灰色 ±2pp 等价区间在视觉上暗示 TOST 是有效的等价检验，但实际上 TOST 在该 margin 下几乎无功效。建议在图注中明确标注 TOST 功效不足，或移除该视觉元素以避免误导。\n\n---\n\n## Questions for Authors\n\n1. 如果使用 5-fold cross-validation 替代单一 split，Δ_asym 的方向和量级是否稳定？是否有任何 fold 出现不对称方向翻转？\n2. Qwen 和 Gemma 上 steering 失败——作者是否尝试过 activation patching 或其他因果干预方法？如果 steering 的失败是由于非线性交互，这些替代方法可能更适用。\n3. COMET tercile 消融中 Gemma 的 Δ=+10.3pp 虽然不显著，但效应大小已接近主效应（~7pp）。作者如何解释这一数值？是否担心翻译质量可能在 Gemma 上部分解释了不对称？\n4. 论文使用 last-token aggregation——是否评估过其他 aggregation 策略（如 mean pooling、attention-weighted）？不同语言的最后一个 token 可能承载不同信息量。\n5. 对于 \"mirror\" 这一核心主张，作者能否提供一个 Bayesian equivalence testing 结果（例如 ROPE+HDI 方法），作为对 TOST 功效不足的补充？\n",
    "reviewer_id": "1",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-25T04:24:30.861707+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3965
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-25T04:24:36.115269+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
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

_source line 167 · 2026-05-25T04:24:36.165904+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-25T04:24:40.785122+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 169 · 2026-05-25T04:24:40.835716+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 170 · 2026-05-25T04:24:53.440304+00:00_

审稿完成。以下是核心结论摘要：

**Overall: 3.5（Borderline Conference）**

三个 Must-Fix 问题：

1. **"Mirror" 主张 vs TOST 功效 1.4%**：标题核心词 "mirror" 缺乏形式化统计支撑，等价检验本质上无信息量，建议改为 "resemble" 或提供 Bayesian equivalence testing。

2. **COMET tercile 消融 MDD=25.3pp**：主效应仅 ~7pp，但消融分析只能检测 >25pp 的混淆效应，翻译质量混淆实质上未被排除（Gemma Δ=+10.3pp 尤其值得注意）。

3. **因果证据仅限 Llama L13**：Qwen/Gemma steering 全部失败，但标题和摘要暗示跨模型一般性发现。

五个 Should-Fix：单 split 无 cross-validation、Qwen 双重角色、probe selectivity 未正式评估、缺 AUROC、α 值选择无理论依据。

论文实验设计系统性好、统计局限透明报告值得肯定，但 claims 与 evidence 之间的 calibration 需要调整。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1"
}
```

</details>

---

## Round 6

12 recorded events

### User

_source line 171 · 2026-05-25T04:27:26.495216+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 2 — 新颖性与完整性审查

## Must-Fix 问题

**N1** [critical] 核心发现 "Detection ≠ Decision" 的增量贡献不足
- "probe accuracy 不意味着 causal relevance" 已由 Basu et al. (2026) 在临床 NLP 任务中建立（98.2% AUROC + steering 完全失败）。本文的 "成功" 仅限于 1/3 模型的 1 个层；layer sweep 是方法论改进，不是新发现；2/3 模型的失败反而更接近 Basu et al. 的结论。
- 建议：重新定位贡献——强调跨语言维度的独特性，弱化 "detection ≠ decision" 作为独立 contribution。

**N2** [critical] Contribution 2 ("Architecture-dependent causal localization") 证据过弱
- 3 个模型中只有 1 个（Llama）在 1 个层（L13）显示显著效果。这不是 "architecture-dependent causal localization"，而是 "我们在一个模型找到了正面结果，两个模型是 null"。Multiple testing 的 family-wise error rate 需要跨模型评估。Discussion 中三个 hypotheses 全部是 untested speculation。
- 建议：将 claim 降级为 "exploratory finding"；或提供至少一个 hypothesis 的初步验证。

## Should-Fix 问题

**W1** [warning] Contribution 1（跨语言冲突可检测性）可能是 expected result
- 推理链：单语言可检测 + 共享跨语言空间 → 跨语言可检测。这是一个相当直接的推论。XNLI baseline 表明不对称不是冲突特异的——本质上是 null result。

**W2** [warning] 论文过度 Llama-centric，三模型设计的价值未充分实现
- Probing 部分三模型一致（好），steering 部分 2/3 是 null。核心叙事完全依赖 Llama。

**W3** [warning] 遗漏关键相关工作
- Ravichander et al. (2021) "Probing the Probing Paradigm"
- Gurgurov et al. (2026) "CLaS-Bench: Cross-Lingual Steering Benchmark"
- Pimentel &amp; Cotterell (2021) information-theoretic probing

**W4** [warning] Discussion 中三个 steering 失败 hypotheses 过于投机

## 小问题
M1: Abstract 198 words 接近上限
M2: Table 1 注释重要但容易被忽略
M3: Gemma COMET tercile Δ=+10.3pp 应在 Limitations 更明确提及
M4: Figure 1 信息量偏低
M5: Appendix A (AI Use) 措辞简短
M6: Marks &amp; Tegmark (2024) venue 可能有误（ICLR 2024 vs NeurIPS 2023）

## Missing References
1. Ravichander et al. (2021) — probing accuracy ≠ task relevance
2. Gurgurov et al. (2026) — CLaS-Bench cross-lingual steering benchmark
3. Pimentel &amp; Cotterell (2021) — information-theoretic probing

## 总体评分：3.0（Findings）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-25T04:28:04.694633+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/submitted.pdf",
  "project": "clkc_mech_interp",
  "pages": "1-2",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/submitted.pdf",
    "project": "clkc_mech_interp",
    "pages": "1-2",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-25T04:28:05.148566+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.9}], \"total_pages\": 11, \"rendered_pages\": 2, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 174 · 2026-05-25T04:28:08.260313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-25T04:28:08.612026+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-25T04:28:09.164488+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-25T04:28:09.667415+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1055
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-25T04:29:54.901216+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R2-N1: \"Detection ≠ Decision\" 增量贡献不足**\n\n同意核心判断，但需补充两点 nuance。\n\n同意理由：Basu et al. (2026) 已在单语临床 NLP 场景中建立了 \"98.2% AUROC + steering 完全失败\" 的范例。本文 Contribution 5（\"detectability does not predict causal relevance\"）确实是对已知原则的重复验证而非新发现。Section 1 第二段明确引用了 Basu et al. 的结论，这进一步表明作者自己也意识到这不是新洞察。\n\n但需要区分两个层面：(a) 作为独立 contribution 的 \"detection ≠ decision\" 原则——确实增量有限；(b) 在跨语言场景下的具体实例化——引入了单语场景不存在的混淆因素（翻译质量、token overlap、语言不对称），因此实验设计有独立价值。建议作者将 Contribution 5 合并到 Contribution 2/4 中作为支撑证据，而非独立贡献点。\n\n**[AGREE] R2-N2: Contribution 2 证据过弱**\n\n强烈同意。这与我的 N3 一致。\n\n补充发现：论文 Section 5 第三段对 Qwen/Gemma steering 失败给出三个假说（causal pathway 非线性、residual stream superposition、architectural differences），但三者均无任何初步验证。更严重的是，论文在 Page 2 将 \"Architecture-dependent causal localization\" 列为五个贡献之一，但 \"architecture-dependent\" 这一修饰语暗示了跨架构的系统性比较发现，而实际情况是：一个正面结果（Llama L13, p=0.002）加两个 null（Qwen best p=0.785, Gemma best p=0.148）。\n\nR2 提出的修改建议合理——降级为 \"exploratory finding\" 或提供假说的初步验证。我补充建议：如果保留此贡献，至少需要对 Qwen/Gemma 进行更精细的因果分析（如 activation patching），而非仅依赖 steering 这一单一方法。Steering 失败可能反映方法局限而非模型缺乏因果结构。\n\n---\n\n## Should-Fix 问题\n\n**[REBUT] R2-W1: 跨语言可检测性是 \"expected result\"**\n\nR2 的推理链（\"单语可检测 + 共享空间 → 跨语言可检测\"）在直觉上合理，但过于简化，忽略了论文的关键实证贡献。\n\n反驳证据：\n\n1. **方向性不对称是非平凡的**：如果跨语言可检测性仅仅是共享空间的推论，那么预期应该是对称的迁移。但论文发现 ZH→EN 迁移比 EN→ZH 高约 7pp（Table 1: Δ_asym = +7.3pp for Llama [0.4, 14.0], +7.2pp for Qwen, +6.6pp for Gemma [1.9, 11.1]），且这一不对称跨三个架构方向一致。这不是 \"expected\" 的。\n\n2. **XNLI 基线不是 \"null result\"**：R2 称 \"XNLI baseline 表明不对称不是冲突特异的——本质上是 null result\"。我不同意这一定性。XNLI 基线显示非冲突任务也存在相同方向的不对称（Section 4.4, Figure 3），这是一个**正面发现**——它将观测到的不对称归因到通用跨语言结构而非冲突编码的特异性。这一归因本身是有信息量的，排除了 \"冲突信号有独特跨语言编码\" 这一替代假说。\n\n3. **共享空间不保证线性可分**：跨语言共享空间的存在不意味着任务相关信号在该空间中是线性可分的。信号可能以非线性方式编码，或被语言特异性噪声掩盖。实证验证仍有价值。\n\n因此，虽然可检测性本身可能是预期的，但方向性不对称及其与通用跨语言结构的对应关系是论文的真正贡献，不能简单归为 \"expected\"。\n\n**[AGREE] R2-W2: 过度 Llama-centric**\n\n同意，与我的 N3 观点一致。Probing 三模型一致这一优势被 steering 的 Llama-only 叙事削弱。论文的主要叙事弧线（Abstract → Introduction → Discussion）在不经意间给出了三模型对等发现的印象，但 Section 5 的实质讨论几乎全部围绕 Llama L13 展开。\n\n**[REBUT] R2-W3: 遗漏关键相关工作（部分同意、部分反驳）**\n\n需要分开讨论三篇引用：\n\n1. **Pimentel & Cotterell (2021)** — [AGREE]：information-theoretic probing 框架对本文的 probe methodology 讨论是相关的。论文使用线性 probe 但未讨论信息论替代框架，补充引用合理。\n\n2. **Ravichander et al. (2021)** — [AGREE with caveat]：如果该论文确实讨论了 probing accuracy 与 task relevance 的脱节，则与本文主题相关。但建议 R2 确认此引用的准确性（标题、年份、venue），避免引入不存在的文献。\n\n3. **Gurgurov et al. (2026) \"CLaS-Bench\"** — [REBUT]：这是一篇据称 2026 年的论文。在双盲审稿中，我无法验证此文献是否已公开发表或可获取。如果这是一篇尚未正式发表的 preprint，要求作者引用它的合理性取决于其公开时间是否早于本文投稿截止日。此外，如果 CLaS-Bench 确实是跨语言 steering 的 benchmark，本文的 steering 实验设计（基于 probe direction 注入）与 benchmark 评测是不同的研究取向——遗漏引用可能影响完整性但不影响方法论有效性。\n\n**[AGREE] R2-W4: Discussion 假说过于投机**\n\n同意。Section 5 \"Why does steering fail in Qwen and Gemma?\" 提出三个假说但全部 untested。学术论文中提出未验证假说本身是允许的，但当这些假说用于支撑一个被列为独立贡献的发现时（Contribution 2: \"Architecture-dependent causal localization\"），要求更高的证据标准是合理的。\n\n建议：至少对假说 1（\"causal pathway may involve non-linear interactions\"）进行初步验证——例如检查 Qwen/Gemma 在 L13 附近的 probe direction 与 steering direction 之间的余弦相似度，或比较线性 vs 非线性 probe 的精度差异。\n\n---\n\n## 小问题\n\n**[AGREE] R2-M1**: Abstract 198 words 确实接近 200-word 上限但在合规范围内，不构成问题。\n\n**[AGREE] R2-M2**: Table 1 脚注（\"Δ_asym is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies\"）确实重要但容易被忽略。建议移入正文 Section 4.3 的段落中。\n\n**[AGREE] R2-M3**: Gemma COMET tercile Δ=+10.3pp 应在 Limitations 更明确讨论。这与我的 N2 一致——这一效应大小接近主效应（~7pp），在 Limitations 中仅被 COMET 分析的整体无显著性掩盖了。\n\n**[REBUT] R2-M4**: Figure 1 信息量偏低——我不完全同意。Figure 1 作为 pipeline overview figure 承担的是导航功能而非信息密度。对于一篇方法流程较复杂的论文（data construction → probing → steering → confound exclusion），一个清晰的概览图有助于读者快速理解实验设计。不过同意可以在图中补充更多细节（如样本量、关键超参数）以提高信息密度。\n\n**[AGREE] R2-M5**: AI Use 措辞简短，但 ARR 对此部分无字数要求，不构成格式问题。\n\n**[AGREE] R2-M6**: Marks & Tegmark (2024) 的 venue 应由作者核实。引用准确性是基本要求。\n\n---\n\n## 对 R2 总体评分的看法\n\nR2 给出 3.0（Findings）。结合我的评估（3.5, Borderline Conference），我认为合理区间在 3.0–3.5 之间。\n\nR2 的核心论点——贡献增量性不足——有一定道理，但 R2 低估了方向性不对称发现和混淆排除管线的实验设计价值。如果作者能 (a) 将 \"detection ≠ decision\" 从独立贡献降级为支撑证据，(b) 将 \"architecture-dependent causal localization\" 降级为 exploratory finding，(c) 强化标题中 \"mirror\" 的统计支撑，论文的贡献定位会更诚实，也更有说服力。当前版本的主要问题不是工作质量差，而是 claims 的范围超出了证据的支撑范围。\n",
  "reviewer_id": "1",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R2-N1: \"Detection ≠ Decision\" 增量贡献不足**\n\n同意核心判断，但需补充两点 nuance。\n\n同意理由：Basu et al. (2026) 已在单语临床 NLP 场景中建立了 \"98.2% AUROC + steering 完全失败\" 的范例。本文 Contribution 5（\"detectability does not predict causal relevance\"）确实是对已知原则的重复验证而非新发现。Section 1 第二段明确引用了 Basu et al. 的结论，这进一步表明作者自己也意识到这不是新洞察。\n\n但需要区分两个层面：(a) 作为独立 contribution 的 \"detection ≠ decision\" 原则——确实增量有限；(b) 在跨语言场景下的具体实例化——引入了单语场景不存在的混淆因素（翻译质量、token overlap、语言不对称），因此实验设计有独立价值。建议作者将 Contribution 5 合并到 Contribution 2/4 中作为支撑证据，而非独立贡献点。\n\n**[AGREE] R2-N2: Contribution 2 证据过弱**\n\n强烈同意。这与我的 N3 一致。\n\n补充发现：论文 Section 5 第三段对 Qwen/Gemma steering 失败给出三个假说（causal pathway 非线性、residual stream superposition、architectural differences），但三者均无任何初步验证。更严重的是，论文在 Page 2 将 \"Architecture-dependent causal localization\" 列为五个贡献之一，但 \"architecture-dependent\" 这一修饰语暗示了跨架构的系统性比较发现，而实际情况是：一个正面结果（Llama L13, p=0.002）加两个 null（Qwen best p=0.785, Gemma best p=0.148）。\n\nR2 提出的修改建议合理——降级为 \"exploratory finding\" 或提供假说的初步验证。我补充建议：如果保留此贡献，至少需要对 Qwen/Gemma 进行更精细的因果分析（如 activation patching），而非仅依赖 steering 这一单一方法。Steering 失败可能反映方法局限而非模型缺乏因果结构。\n\n---\n\n## Should-Fix 问题\n\n**[REBUT] R2-W1: 跨语言可检测性是 \"expected result\"**\n\nR2 的推理链（\"单语可检测 + 共享空间 → 跨语言可检测\"）在直觉上合理，但过于简化，忽略了论文的关键实证贡献。\n\n反驳证据：\n\n1. **方向性不对称是非平凡的**：如果跨语言可检测性仅仅是共享空间的推论，那么预期应该是对称的迁移。但论文发现 ZH→EN 迁移比 EN→ZH 高约 7pp（Table 1: Δ_asym = +7.3pp for Llama [0.4, 14.0], +7.2pp for Qwen, +6.6pp for Gemma [1.9, 11.1]），且这一不对称跨三个架构方向一致。这不是 \"expected\" 的。\n\n2. **XNLI 基线不是 \"null result\"**：R2 称 \"XNLI baseline 表明不对称不是冲突特异的——本质上是 null result\"。我不同意这一定性。XNLI 基线显示非冲突任务也存在相同方向的不对称（Section 4.4, Figure 3），这是一个**正面发现**——它将观测到的不对称归因到通用跨语言结构而非冲突编码的特异性。这一归因本身是有信息量的，排除了 \"冲突信号有独特跨语言编码\" 这一替代假说。\n\n3. **共享空间不保证线性可分**：跨语言共享空间的存在不意味着任务相关信号在该空间中是线性可分的。信号可能以非线性方式编码，或被语言特异性噪声掩盖。实证验证仍有价值。\n\n因此，虽然可检测性本身可能是预期的，但方向性不对称及其与通用跨语言结构的对应关系是论文的真正贡献，不能简单归为 \"expected\"。\n\n**[AGREE] R2-W2: 过度 Llama-centric**\n\n同意，与我的 N3 观点一致。Probing 三模型一致这一优势被 steering 的 Llama-only 叙事削弱。论文的主要叙事弧线（Abstract → Introduction → Discussion）在不经意间给出了三模型对等发现的印象，但 Section 5 的实质讨论几乎全部围绕 Llama L13 展开。\n\n**[REBUT] R2-W3: 遗漏关键相关工作（部分同意、部分反驳）**\n\n需要分开讨论三篇引用：\n\n1. **Pimentel & Cotterell (2021)** — [AGREE]：information-theoretic probing 框架对本文的 probe methodology 讨论是相关的。论文使用线性 probe 但未讨论信息论替代框架，补充引用合理。\n\n2. **Ravichander et al. (2021)** — [AGREE with caveat]：如果该论文确实讨论了 probing accuracy 与 task relevance 的脱节，则与本文主题相关。但建议 R2 确认此引用的准确性（标题、年份、venue），避免引入不存在的文献。\n\n3. **Gurgurov et al. (2026) \"CLaS-Bench\"** — [REBUT]：这是一篇据称 2026 年的论文。在双盲审稿中，我无法验证此文献是否已公开发表或可获取。如果这是一篇尚未正式发表的 preprint，要求作者引用它的合理性取决于其公开时间是否早于本文投稿截止日。此外，如果 CLaS-Bench 确实是跨语言 steering 的 benchmark，本文的 steering 实验设计（基于 probe direction 注入）与 benchmark 评测是不同的研究取向——遗漏引用可能影响完整性但不影响方法论有效性。\n\n**[AGREE] R2-W4: Discussion 假说过于投机**\n\n同意。Section 5 \"Why does steering fail in Qwen and Gemma?\" 提出三个假说但全部 untested。学术论文中提出未验证假说本身是允许的，但当这些假说用于支撑一个被列为独立贡献的发现时（Contribution 2: \"Architecture-dependent causal localization\"），要求更高的证据标准是合理的。\n\n建议：至少对假说 1（\"causal pathway may involve non-linear interactions\"）进行初步验证——例如检查 Qwen/Gemma 在 L13 附近的 probe direction 与 steering direction 之间的余弦相似度，或比较线性 vs 非线性 probe 的精度差异。\n\n---\n\n## 小问题\n\n**[AGREE] R2-M1**: Abstract 198 words 确实接近 200-word 上限但在合规范围内，不构成问题。\n\n**[AGREE] R2-M2**: Table 1 脚注（\"Δ_asym is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies\"）确实重要但容易被忽略。建议移入正文 Section 4.3 的段落中。\n\n**[AGREE] R2-M3**: Gemma COMET tercile Δ=+10.3pp 应在 Limitations 更明确讨论。这与我的 N2 一致——这一效应大小接近主效应（~7pp），在 Limitations 中仅被 COMET 分析的整体无显著性掩盖了。\n\n**[REBUT] R2-M4**: Figure 1 信息量偏低——我不完全同意。Figure 1 作为 pipeline overview figure 承担的是导航功能而非信息密度。对于一篇方法流程较复杂的论文（data construction → probing → steering → confound exclusion），一个清晰的概览图有助于读者快速理解实验设计。不过同意可以在图中补充更多细节（如样本量、关键超参数）以提高信息密度。\n\n**[AGREE] R2-M5**: AI Use 措辞简短，但 ARR 对此部分无字数要求，不构成格式问题。\n\n**[AGREE] R2-M6**: Marks & Tegmark (2024) 的 venue 应由作者核实。引用准确性是基本要求。\n\n---\n\n## 对 R2 总体评分的看法\n\nR2 给出 3.0（Findings）。结合我的评估（3.5, Borderline Conference），我认为合理区间在 3.0–3.5 之间。\n\nR2 的核心论点——贡献增量性不足——有一定道理，但 R2 低估了方向性不对称发现和混淆排除管线的实验设计价值。如果作者能 (a) 将 \"detection ≠ decision\" 从独立贡献降级为支撑证据，(b) 将 \"architecture-dependent causal localization\" 降级为 exploratory finding，(c) 强化标题中 \"mirror\" 的统计支撑，论文的贡献定位会更诚实，也更有说服力。当前版本的主要问题不是工作质量差，而是 claims 的范围超出了证据的支撑范围。\n",
    "reviewer_id": "1",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-25T04:29:58.669740+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3768
}
```

</details>

---

### Tool call

_source line 180 · 2026-05-25T04:30:03.395204+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 181 · 2026-05-25T04:30:03.395614+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 182 · 2026-05-25T04:30:15.086362+00:00_

交叉回应已提交。总结：

- **R2-N1 (Detection≠Decision 增量不足)**: [AGREE]，但指出跨语言维度的混淆排除设计有独立价值，建议将其从独立贡献合并为支撑证据
- **R2-N2 (Causal localization 证据弱)**: [AGREE]，与我的 N3 一致，补充建议尝试 activation patching 等替代因果方法
- **R2-W1 (跨语言可检测是 expected)**: [REBUT]，方向性不对称（~7pp, 三模型一致）不可从 "共享空间" 直接推出；XNLI 基线是正面发现而非 null result
- **R2-W2 (Llama-centric)**: [AGREE]
- **R2-W3 (遗漏引用)**: 部分同意 Pimentel & Cotterell，反驳 Gurgurov et al. (2026) 的引用要求需先确认其公开可获取性
- **R2-W4 (投机假说)**: [AGREE]，建议至少提供一个假说的初步验证
- 总体评分区间 3.0–3.5，核心问题是 claims 范围超出证据支撑

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1"
}
```

</details>

---

## Round 7

58 recorded events

### User

_source line 183 · 2026-05-25T21:15:33.170389+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性**审查。

## Venue 信息
- **目标**: EMNLP 2026 (via ARR)
- **Deadline**: 2026-06-15
- **格式**: ACL 模板，Long paper 正文 8 页限制（references 不限），Limitations 必需且不计页数
- **匿名**: Double-blind

## 论文文件
- LaTeX 源码: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex`（各章节为独立 .tex 文件同目录）
- PDF: `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/submitted.pdf`

## 你的审查侧重

请从以下维度严格评估：

1. **统计有效性**：p 值校正是否恰当（Bonferroni）、CI 解释是否正确、bootstrap 方法是否合理、样本量是否充分支撑所述结论
2. **因果声明**：steering 实验的因果推断是否成立、random control 是否充分、L13 单层单模型成功能否支撑"detection≠decision"这一跨模型 claim
3. **实验设计**：confound exclusion 的逻辑链是否完整（COMET tercile 功效问题、token overlap、EN-DE 对照）、单 train/test split 的局限性
4. **可重复性**：实验细节是否充分（超参、硬件、随机种子）、seed replication 是否充分验证
5. **多重比较**：全文共多少假设检验，family-wise error rate 控制是否恰当

请输出标准 ARR 审稿格式：
- Summary (2-3 句)
- Strengths (逐条)
- Weaknesses (逐条，标注 severity: critical/warning/info)
- Questions to Authors
- Missing References (如有)
- Overall Assessment (1-5 分，参照 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit)
- Confidence (1-5)

**严格评审，不留情面。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 184 · 2026-05-25T21:15:43.042816+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
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

_source line 185 · 2026-05-25T21:15:43.093506+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 186 · 2026-05-25T21:15:48.245218+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---

### Tool call

_source line 187 · 2026-05-25T21:15:50.155929+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/submitted.pdf",
  "project": "clkc_mech_interp",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/submitted.pdf",
    "project": "clkc_mech_interp",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 188 · 2026-05-25T21:15:55.040805+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

I found relevant information about ACL ARR 2026 reviewer guidelines. Here are the key details:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Review Form Scoring Scale

A score of 5 means "Consider for Award": the paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers). A score of 2 means "Resubmit next cycle" for papers needing substantial revisions that can be completed by the next ARR cycle
…[truncated 802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6795
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-25T21:15:56.851517+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 440.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 585.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 588.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 547.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 444.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 406.8}], \"total_pages\": 12, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6695
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-25T21:16:03.705187+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5), descriptions for each score level, and any instructions for reviewers. Include the exact wording for Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5), descriptions for each score level, and any instructions for reviewers. Include the exact wording for Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other scored dimensions."
  }
}
```

</details>

---

### Tool call

_source line 191 · 2026-05-25T21:16:04.156943+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 192 · 2026-05-25T21:16:04.762636+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-25T21:16:05.622113+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1465
}
```

</details>

---

### Tool call

_source line 194 · 2026-05-25T21:16:05.624297+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-25T21:16:05.775857+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1013
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-25T21:16:05.776268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 197 · 2026-05-25T21:16:07.238932+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1614
}
```

</details>

---

### Tool result

_source line 198 · 2026-05-25T21:16:07.541012+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1764
}
```

</details>

---

### Tool result

_source line 199 · 2026-05-25T21:16:10.008207+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence** (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness** (1-5 scale)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement** (1-5 scale)
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me."

## 4. **Overall Assessment** (1-5 scale)
- **5**: "Consider for Award"
- **4**: "Conference acceptance"
- **3**: "Findings acceptance"
- **2**: "Resubmit next cycle"
- **1**: "Do not resubmit"

## 5. **Reproducibility** (1-5 scale)
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard pressed to reproduce the results."
- **1**: "They would not be able to reproduce the results."

## 6. **Datasets & Software** (1-5 scales)
Both use identical frameworks: Enabling (5), Useful (4), Potentially useful (3), Documentary (2), None (1).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6303
}
```

</details>

---

### Tool call

_source line 200 · 2026-05-25T21:16:21.382424+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool call

_source line 201 · 2026-05-25T21:16:21.934615+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 202 · 2026-05-25T21:16:22.839308+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1456
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-25T21:16:22.845810+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 911
}
```

</details>

---

### Tool call

_source line 204 · 2026-05-25T21:16:22.847415+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool call

_source line 205 · 2026-05-25T21:16:23.751611+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 206 · 2026-05-25T21:16:24.310356+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1462
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-25T21:16:24.763719+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1012
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-25T21:16:24.814284+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/submitted.pdf",
  "project": "clkc_mech_interp",
  "pages": "9-12",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/submitted.pdf",
    "project": "clkc_mech_interp",
    "pages": "9-12",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-25T21:16:25.319063+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 566.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 603.6}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 184.2}], \"total_pages\": 12, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 504
}
```

</details>

---

### Tool call

_source line 210 · 2026-05-25T21:16:29.835780+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool call

_source line 211 · 2026-05-25T21:16:30.398205+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool call

_source line 212 · 2026-05-25T21:16:31.279178+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 213 · 2026-05-25T21:16:32.109712+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2273
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-25T21:16:32.161977+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-25T21:16:34.178650+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3780
}
```

</details>

---

### Tool result

_source line 216 · 2026-05-25T21:16:34.184231+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2022
}
```

</details>

---

### Tool result

_source line 217 · 2026-05-25T21:16:34.337582+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3058
}
```

</details>

---

### Tool call

_source line 218 · 2026-05-25T21:17:05.177193+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 219 · 2026-05-25T21:17:05.279040+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/acl_latex.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 220 · 2026-05-25T21:17:09.294908+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 221 · 2026-05-25T21:17:09.546452+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\vspace{-18pt}
7	\includegraphics[width=0.88\textwidth]{fig2_pipeline.pdf}
8	\vspace{-14pt}
9	\caption{Method overview. We construct parallel EN/ZH conflict data from ConflictQA with COMET-validated translations, extract per-layer residual stream representations, train logistic regression probes in four transfer directions (EN$\to$EN, ZH$\to$ZH, EN$\to$ZH, ZH$\to$EN), and apply confound exclusion controls before causal steering validation.}
10	\label{fig:pipeline}
11	\vspace{-20pt}
12	\end{figure*}
13	
14	Our pipeline proceeds from data construction through probing and steering (Figure~\ref{fig:pipeline}), formalized below.
15	
16	\subsection{Task Formulation}
17	\label{sec:task}
18	
19	Given a context passage $c$ and question $q$, the model produces an answer that is either \emph{contextual} (derived from $c$) or \emph{parametric} (from pre-trained knowledge).
20	When $c$ contradicts parametric knowledge, the choice constitutes a knowledge conflict.
21	We train a logistic regression probe $f_\theta(\mathbf{h}_l) = \sigma(\mathbf{w}_l^\top \mathbf{h}_l + b_l)$ on the last-token residual stream representation $\mathbf{h}_l \in \mathbb{R}^d$ at layer $l$ to predict a binary label $y \in \{\text{contextual}, \text{parametric}\}$.
22	
23	\subsection{Data Construction}
24	\label{sec:data}
25	
26	We build on ConflictQA \citep{xie2024adaptive}, which pairs questions with context passages contradicting the model's parametric knowledge.
27	We filter samples by querying each model without context and retaining only those answered correctly, yielding 1{,}368 samples for Llama \citep{grattafiori2024llama}, 966 for Qwen \citep{yang2025qwen3}, and 1{,}590 for Gemma \citep{team2024gemma} (80/20 train/test split with stratification).
28	For cross-lingual transfer, we translate all inputs into Chinese using a Qwen3-8B pipeline, with quality validated by COMET (Crosslingual Optimized Metric for Evaluation 
…[truncated 4969 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 222 · 2026-05-25T21:17:09.546944+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 223 · 2026-05-25T21:17:09.597707+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We probe three instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \citep{grattafiori2024llama}, Qwen3-8B (36 layers, hidden dimension 4096) \citep{yang2025qwen3}, and Gemma-2-9B-IT (42 layers, hidden dimension 3584) \citep{team2024gemma}.
9	
10	\paragraph{Dataset.}
11	We use ConflictQA \citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.
12	After verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test), 966 for Qwen (773 train / 193 test), and 1{,}590 for Gemma (1{,}274 train / 316 test), split 80/20 with stratification.
13	The three models were independently verified, yielding only 3.5\% three-way question overlap (23 questions); pairwise overlaps range from 7.2\% (Llama $\cap$ Gemma) to 24.8\% (Gemma $\cap$ Qwen), so the consistent asymmetry pattern across models constitutes largely independent replication.
14	
15	\paragraph{Translation.}
16	We translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\to$ZH), with quality validated by COMET (wmt22-comet-da; \citealt{rei2020comet}) back-translation scores.
17	
18	\paragraph{Probing.}
19	For each layer $l$, we train an $L_2$-regularized logistic regression probe ($C = 1.0$, scikit-learn default) on the last-token residual stream representation $\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.
20	We report balanced accuracy rather than AUROC, as our claims depend on cross-model directional comparisons; AUROC results are reported in Appendix~\ref{app:auroc}.
21	All CIs are computed via bootstrap resam
…[truncated 15596 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 224 · 2026-05-25T21:17:24.856498+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 225 · 2026-05-25T21:17:25.358745+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Causal influence is localized to L13 regardless of detection peak.}
5	In Llama, causal influence is localized to L13 (41\% depth; Fisher $p < 0.001$), near but distinct from the linear probe peak (L15, 47\%) and MLP probe peak (L18, 56\%), with upper-layer interventions producing no significant change ($p > 0.3$; Figure~\ref{fig:dissociation}).
6	L13 coincides with cross-lingual alignment sites \citep{muller2021first, wendler2024llamas}, suggesting mid-layers serve a dual role in alignment and conflict resolution.
7	The dissociation evidence is strongest for Gemma, where 88.9\% probe accuracy and 0.93 AUROC coexist with zero steering effects, ruling out probe quality as a confound; for Qwen, weaker probe performance (71.4\%) leaves the null result more ambiguous.
8	
9	\paragraph{Why does steering fail in Qwen and Gemma?}
10	Three hypotheses merit consideration: (1)~non-linear causal interactions \citep{elhage2022toy}, where MLP probes gain $+9.2$~pp over linear probes on conflict but $-0.5$~pp on XNLI; (2)~superposition \citep{templeton2024scaling}, where conflict and XNLI weight vectors are near-orthogonal yet cross-task language transfer is near-perfect; (3)~architectural differences, as Qwen and Gemma show mid-layer transfer dips absent in Llama.
11	Definitive validation requires activation patching \citep{meng2022locating}.
12	
13	\paragraph{Relation to prior work.}
14	The ZH$\to$EN advantage matches the XNLI baseline across all models, indicating that asymmetry piggybacks on general cross-lingual alignment \citep{zhao2026when, kargaran2024mexa, wendler2024llamas}.
15	\citet{basu2026interpretability} reported steering failure despite 98.2\% AUROC; our L13 succeeds because we steer at mid-layer rather than probe-peak, while our three-model design isolates architecture.
16	
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 226 · 2026-05-25T21:17:25.359118+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-25T21:17:25.560023+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our study has three main limitations.
5	First, we evaluate only one language pair (English-Chinese) and causal steering succeeded only in Llama at L13; Gemma L17 failed despite 88.9\% probe accuracy ($n = 171$) and Qwen L14 ($n = 131$) was also negative.
6	Typologically diverse language pairs and alternative intervention methods are needed to assess generality.
7	Null steering results in Qwen and Gemma may reflect limitations of single-direction linear steering rather than absence of causal structure; alternative methods such as activation patching \citep{meng2022locating} may reveal non-linear causal pathways that our approach cannot detect.
8	Second, the effective dataset size (966 to 1,590 samples per model) is constrained by parametric knowledge verification, which retains only questions where the model confidently knows the ground truth and may bias toward well-represented knowledge; additionally, Qwen3-8B serves as both the translation model and an experimental subject, though COMET-based quality control mitigates this concern, and the fact that Llama and Gemma, architecturally independent of the translation model, show the same asymmetry pattern ($\Delta_{\text{asym}} = +7.3$ and $+6.6$~pp, respectively) provides cross-validation that the effect is not an artifact of Qwen-specific translation biases.
9	Third, all probing results are based on a single train/test split with bootstrap confidence intervals capturing within-split variability; while peak balanced accuracy remains stable across seeds (Llama $\pm$0.12\%, Gemma $\pm$1.32\%, Qwen $\pm$1.90\%), the specific peak layer can shift.
10	We acknowledge that $k$-fold cross-validation would provide stronger stability guarantees \citep{belinkov2022probing}; given that our core claims rest on cross-model consistency and directional patterns rather than exact accuracy values, the current cross-seed stability analysis provides partial mitigation, and we commit
…[truncated 191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---

### Tool call

_source line 228 · 2026-05-25T21:17:25.560594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 229 · 2026-05-25T21:17:25.611205+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that knowledge conflict signals are linearly detectable across English and Chinese ($p < 0.001$, three architectures), with the ZH$\to$EN transfer advantage (${\sim}$7~pp) matching the XNLI baseline, indicating general cross-lingual alignment rather than conflict-specific encoding.
5	Causal intervention reveals a detection--decision dissociation: all three models detect conflict signals, yet only Llama yields significant steering at L13 ($p < 0.001$); Gemma fails despite 88.9\% probe accuracy, confirming detection alone is insufficient for mechanistic claims.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 230 · 2026-05-25T21:19:45.175795+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 231 · 2026-05-25T21:19:45.326707+00:00_

1	When multilingual large language models encounter conflicting information between languages, presentation language can determine the answer, but the internal mechanism remains unknown. We probe residual streams in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT on English--Chinese conflicts, combining cross-lingual transfer, XNLI non-conflict baselines, confound exclusion, and representation steering. Conflict signals are linearly detectable across both languages, and cross-lingual transfer exhibits a directional asymmetry: Chinese-trained probes transfer to English ${\sim}$7 percentage points more accurately than the reverse, matching the XNLI baseline and consistent with general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision: the probe signal is broadly distributed across mid-to-upper layers, yet representation steering achieves causal influence only at a mid-layer (L13, 41\% depth) in Llama; analogous Qwen and Gemma steering yields no significant effect. These findings indicate that linear detectability does not imply causal relevance, with implications for probe-based intervention\footnote{Code and data are available at \url{https://anonymous.4open.science/r/clkc_mech_interp-F894/}.}.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 232 · 2026-05-25T21:19:45.327105+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 233 · 2026-05-25T21:19:45.377506+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{fig1_hero.pdf}
7	\caption{Cross-lingual knowledge conflict in multilingual LLMs. When a context passage contradicts the model's parametric knowledge, the language of presentation (English vs.\ Chinese) can bias the answer toward different sources. We ask three questions: (1)~Is the conflict signal linearly detectable in the residual stream? (2)~Do probes transfer across languages, and is the transfer symmetric? (3)~Does detection imply causal influence on resolution?}
8	\label{fig:hero}
9	\end{figure*}
10	
11	When multilingual large language models (LLMs) encounter conflicting information between languages, the language of presentation can determine which answer the model produces \citep{zhao2026when}.
12	Yet the internal mechanism remains opaque: how does the model encode the conflict signal, can it be detected from internal representations, and does the detected signal causally influence resolution?
13	
14	Existing work on probing conflict signals has been limited to monolingual settings \citep{zhao2024analysing, brink2026probing}.
15	Extending cross-lingually introduces confounds (translation quality, token overlap, general transfer properties), and probing establishes correlation rather than causation \citep{hewitt2019designing}; \citet{basu2026interpretability} showed that near-perfect probe accuracy does not guarantee effective steering.
16	
17	Our work extends \citet{zhao2024analysing} in four directions: (1)~cross-lingual expansion from monolingual English to EN-ZH conflict probing; (2)~a systematic confound exclusion pipeline; (3)~the XNLI baseline revealing that asymmetry parallels general cross-lingual structure; and (4)~three-model causal intervention demonstrating that detectability does not predict causal relevance.
18	We combine residual stream probing with representation steering across Llama-3.1-8B-Instruct, Qwen3-8B, and Gem
…[truncated 1987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 234 · 2026-05-25T21:23:50.656966+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — 方法严谨性审查\n\n### Summary\n\n本文对三个多语言 LLM（Llama-3.1-8B、Qwen3-8B、Gemma-2-9B-IT）的残差流进行探测，研究英中跨语言知识冲突信号的可检测性、迁移不对称性及因果干预效果。主要发现：(1) 冲突信号在两种语言中均线性可分；(2) ZH→EN 迁移优势（~7pp）与 XNLI 非冲突基线一致，反映通用跨语言结构而非冲突特异编码；(3) 仅 Llama L13 层的 steering 产生因果效应，Qwen/Gemma steering 失败，据此提出\"detection ≠ decision\"论断。\n\n---\n\n### Strengths\n\n**S1. 三模型设计提供跨架构证据。** 使用三个参数量相当但架构不同的模型（Llama/Qwen/Gemma），且模型间问题重叠仅 3.5%，构成近似独立复制。方向一致性的二项检验（p = 0.016）是合理的统计策略。\n\n**S2. XNLI 非冲突基线控制得当。** 用相同 pipeline 在 XNLI 上运行探测，证明不对称性并非冲突特异，是本文最有说服力的控制实验之一。\n\n**S3. EN-DE 类型学控制巧妙。** 德语词汇重叠率约为中文的 4 倍（14.8% vs 3.8%），但 EN↔DE 不对称性接近零（Δ = +1.2pp, n.s.），有效排除了 token overlap 混淆。\n\n**S4. Selectivity control 规范。** 置换标签控制（N=131–201）产生近机会准确率（49.2–51.0%），selectivity gap 达 21–40pp，证实探测信号非任意线性可分。\n\n**S5. Steering 随机控制设计合理。** 注入等幅随机向量 r ~ N(0,I) 作为对照，将方向效应与幅度效应分离，方法上较先前工作有改进。\n\n**S6. Limitations 诚实。** 明确承认单 split 局限性并承诺 camera-ready 补充 5-fold CV，以及 steering 仅在 Llama 成功。\n\n---\n\n### Weaknesses\n\n**W1 [critical] \"Detection ≠ Decision\" 核心论断证据不足，存在过度概括。**\n- 具体位置：Abstract (\"these findings indicate that linear detectability does not imply causal relevance\")、Section 5 Discussion、Section 6 Conclusion\n- 问题：正面因果证据仅来自**一个模型（Llama）的一个层（L13）**。Qwen 和 Gemma 的负面结果可被多种替代假设解释：(a) 非线性因果通路（论文自己承认）；(b) 因果窗口在不同层（Llama 中因果窗口仅 ~4 层宽/L13-L16，但 Qwen 仅测 L14、Gemma 仅测 L17，遗漏相邻层的可能性大）；(c) 样本量不足（Qwen n=131、Gemma n=171，对微弱效应的检验功效有限）；(d) 线性 steering 本身的方法局限。Absence of evidence ≠ evidence of absence——论文将两个模型的 null result 提升为跨模型的一般性结论，逻辑跳跃过大。\n- 为什么影响接收：这是论文的第三个贡献点（Contribution 3），也是 abstract 和 conclusion 的核心 takeaway。如果此论断不成立，论文的新颖贡献大幅缩水，仅剩描述性发现（跨语言可检测性 + 不对称性）。\n- 建议修改方向：(1) 将 claim 降级为 Llama 特有观察，明确声明无法推广到其他架构；(2) 对 Qwen/Gemma 在至少 3-5 个相邻层进行 steering（而非仅 1 层），以确认负面结果的鲁棒性；(3) 补充 activation patching 实验作为线性 steering 的对照。\n\n**W2 [critical] Qwen 不对称性 CI 包含零，但被当作支持证据处理。**\n- 具体位置：Section 4.3, Table 1 — Qwen Δ_asym = +7.2, CI [−0.6, 13.7]\n- 问题：Qwen 的 95% CI 跨越零，意味着该模型的不对称性在 α=0.05 水平不显著。但论文在 Section 4.3 中写 \"the asymmetry is consistent in direction across all three architectures\" 并将 Qwen 与 Llama/Gemma 同等对待。进一步，如果对三个模型的不对称性检验做 Bonferroni 校正（阈值 0.017），Llama (p=0.038) 也不再显著，仅 Gemma (p=0.006) 幸存。\n- 为什么影响接收：不对称性的跨模型一致性是 Contribution 2 的基础。三个模型中两个不显著（校正后），严重削弱\"一致\"的论断。\n- 建议修改方向：(1) 明确报告 Qwen 不显著，不要用模糊的 \"marginally includes zero\"；(2) 讨论对三模型做多重比较校正后的结果；(3) 更多依赖方向一致性的二项检验（p=0.016）和 XNLI 的独立复制，而非个体模型的点估计。\n\n**W3 [critical] COMET tercile 分析严重欠功效，无法有效排除翻译质量混淆。**\n- 具体位置：Section 4.5, Table 2\n- 问题：论文自己报告 MDE = 25.3pp at 80% power（n≈56 per tercile）——即只有翻译质量造成 >25pp 的准确率差异时才能检测到。这使得该分析对中等大小的混淆效应完全不敏感。更令人担忧的是，Gemma 显示 Δ = +10.3pp 在混淆方向（高 COMET → 高准确率），虽然 p=0.278，但在这种低功效下不显著并不等于无效应。论文将此结果描述为 \"non-significant trend\"（Section 4.5），但一个 10pp 的点估计在混淆方向上是实质性的。\n- 为什么影响接收：如果翻译质量确实影响跨语言探测准确率，则 ZH→EN 不对称性可能是 artifact。COMET tercile 分析本应排除此混淆，但因欠功效而无法完成此任务。\n- 建议修改方向：(1) 增加样本量或使用连续回归（COMET score 作为连续变量 vs. 探测准确率），而非三分位比较，以提升功效；(2) 对 Gemma 的 +10.3pp 趋势做更深入调查；(3) 如果无法增加功效，诚实声明翻译质量混淆未被排除。\n\n**W4 [warning] TOST 等价性检验功效仅 1.4%，无信息量。**\n- 具体位置：Section 4.4 — \"TOST equivalence tests (±2 pp margin) are non-significant (p > 0.36, power = 1.4%)\"\n- 问题：1.4% 的功效意味着即使冲突不对称性与 XNLI 不对称性完全相同，该检验也几乎不可能检测到等价性。±2pp 的等价边界过于严格（考虑到各个 CI 宽度 >10pp）。报告一个注定失败的检验并用 \"reflecting insufficient power\" 一笔带过，有空洞分析之嫌。\n- 建议：要么选择合理的等价边界（如 ±5pp）并报告所需样本量，要么删除 TOST 分析，改用 CI 重叠的定性论证。\n\n**W5 [warning] 单 train/test split 贯穿全文，bootstrap CI 仅捕获 split 内变异性。**\n- 具体位置：Section 4.1, Limitations\n- 问题：所有探测结果基于单一 80/20 split。Bootstrap resampling（n=2,000）估计的 CI 是条件于该 split 的——它不能告诉我们换一个 split 结果会怎样。论文在 Limitations 中承认 seed 复制显示 peak layer 可能偏移（Qwen ±1.90%），但未在主要结果中使用 k-fold CV。论文承诺 camera-ready 补充 5-fold CV，但当前版本缺乏此验证。\n- 建议：至少报告 3-fold CV 的主要结果（Table 1），或在当前版本就完成 5-fold CV。\n\n**W6 [warning] 翻译模型（Qwen3-8B）同时作为实验对象。**\n- 具体位置：Section 3.2, Section 4.1\n- 问题：Qwen3-8B 既是翻译 pipeline 又是三个被探测模型之一。虽然论文指出 Llama/Gemma（与翻译模型架构独立）也显示相同模式以缓解担忧，但 Qwen 特有的翻译偏差可能使 Qwen 的跨语言迁移结果不可靠。\n- 建议：在正文中更显著地标注此利益冲突，或使用独立翻译模型（如 NLLB）作为额外验证。\n\n**W7 [warning] 全文多重假设检验缺乏整体 FWER 控制。**\n- 具体位置：全文\n- 问题：粗略统计，全文约 100+ 假设检验：12 个探测二项检验、6 个不对称性检验、3 个 TOST、5 个混淆检验、~78 个 steering 检验等。Bonferroni 仅应用于 steering 实验（per-layer k=10 或 30-test 校正），但探测二项检验、不对称性检验、混淆检验均未做多重比较校正。虽然不同分析模块可视为独立研究问题，但 Section 4.3 的三个不对称性检验属于同一族。\n- 建议：至少对同族检验（如三模型不对称性）应用 Bonferroni/Holm 校正并报告校正后结果。\n\n**W8 [warning] Steering 仅在英文 test data 上评估，未测试跨语言因果干预。**\n- 具体位置：Section 3.6 — \"Steering evaluation uses only the conflict-condition subset of the English test data\"\n- 问题：一篇关于跨语言冲突机制的论文，其因果干预实验仅在英文输入上进行。ZH→EN 探测不对称性是核心发现，但从未测试在中文输入上进行 steering 是否产生不同的因果模式。\n- 建议：至少在 Llama L13（已知有效的层）上测试中文输入的 steering 效果。\n\n**W9 [info] Fisher's exact test 用于 paired data 可能不当。**\n- 具体位置：Section 3.6, Section 4.6\n- 问题：Steering 实验中，相同测试样本分别接受 probe-direction 和 random-direction 注入。这是配对数据，但 Fisher's exact test 假设独立样本。McNemar's test 更适合配对二分类数据。在正相关情况下（容易翻转的样本在两种条件下都容易翻转），Fisher's test 可能是保守的，但这应予以说明。\n- 建议：补充 McNemar's test 结果，或论证 Fisher's exact test 的保守性。\n\n---\n\n### Questions to Authors\n\n**Q1.** Llama 中因果窗口仅 ~4 层宽（L13-L16）。对 Qwen 和 Gemma，你们仅测试了 1 个层（L14/L17）。如果因果窗口同样窄，遗漏相邻层完全可能。是否有 Appendix F 以外的多层 steering 结果？Appendix F 的 Table 6 是否覆盖了每个模型至少 3 个相邻层？\n\n**Q2.** Table 1 中 Δ_asym 脚注指出 \"Δ_asym is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies\"。以 Llama 为例：ZH→EN (70.6) − EN→ZH (59.6) = 11.0pp，但 bootstrap Δ_asym = +7.3pp。这 3.7pp 差异的来源是什么？这是否意味着 peak layer 在不同 bootstrap 样本中发生偏移？如果是，这本身就说明单 split 结果不稳定。\n\n**Q3.** Gemma COMET tercile Δ = +10.3pp 在混淆方向。你们将此归因于 \"near-chance baseline accuracy of the EN→ZH probe at L17 (58.8%)\"，但 58.8% 仍显著高于 chance（binomial p < 0.05 for n≈56）。能否提供 Gemma COMET score 与探测准确率的散点图或连续回归结果？\n\n**Q4.** Qwen3-8B 同时作为翻译模型和实验对象。你们是否验证过：在 Qwen 上，用外部翻译模型（如 NLLB）的翻译是否产生相似的跨语言迁移模式？\n\n**Q5.** Section 4.6 报告 L13 steering 的 all-position injection 与 last-token injection 产生 \"identical results\"。能否提供具体数字？\"Identical\" 是指 p-value 和 flip rate 完全相同，还是方向一致但幅度不同？\n\n---\n\n### Missing References\n\n无明显遗漏。论文引用了该领域的主要相关工作（Zhao et al. 2024/2026, Basu et al. 2026, Hewitt & Liang 2019, Belinkov 2022, Marks & Tegmark 2024 等）。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 2.5/5 | 核心因果论断证据不足（W1），不对称性统计证据不一致（W2），混淆排除欠功效（W3）。描述性发现（可检测性、XNLI 基线）较为扎实。 |\n| **Excitement** | 3/5 | 跨语言冲突机制解释是有意义的研究方向，\"detection ≠ decision\" 观察如能充分支撑会很有启发，但当前证据使其更像初步观察而非成熟结论。 |\n| **Reproducibility** | 3.5/5 | 超参（C=1.0）、硬件（RTX PRO 6000）、bootstrap n=2000 均有报告；匿名 repo 已提供。不足：主实验随机种子未明确报告；单 split 无 CV。 |\n\n---\n\n### Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n本文在跨语言冲突信号可检测性和迁移不对称性方面提供了有价值的描述性发现，XNLI 基线和 EN-DE 控制设计得当。但论文的核心机制性贡献（\"detection ≠ decision\"）基于一个模型一个层的正面证据和两个模型的方法学上可疑的负面证据，无法支撑 abstract 和 conclusion 中的概括性论断。不对称性的统计证据在三模型中不一致（Qwen CI 包含零，Bonferroni 校正后仅 Gemma 显著），混淆排除分析欠功效（COMET tercile MDE = 25.3pp）。这些方法论问题叠加后，使论文的 soundness 低于主会议标准。修改后适合 Findings。\n\n### Confidence\n\n**Confidence: 4/5** — 统计方法论和 probing/steering 实验设计是我的专长领域，仔细阅读了全文及附录。对论文所涉的具体模型架构细节稍不确定。",
  "reviewer_id": "1",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — 方法严谨性审查\n\n### Summary\n\n本文对三个多语言 LLM（Llama-3.1-8B、Qwen3-8B、Gemma-2-9B-IT）的残差流进行探测，研究英中跨语言知识冲突信号的可检测性、迁移不对称性及因果干预效果。主要发现：(1) 冲突信号在两种语言中均线性可分；(2) ZH→EN 迁移优势（~7pp）与 XNLI 非冲突基线一致，反映通用跨语言结构而非冲突特异编码；(3) 仅 Llama L13 层的 steering 产生因果效应，Qwen/Gemma steering 失败，据此提出\"detection ≠ decision\"论断。\n\n---\n\n### Strengths\n\n**S1. 三模型设计提供跨架构证据。** 使用三个参数量相当但架构不同的模型（Llama/Qwen/Gemma），且模型间问题重叠仅 3.5%，构成近似独立复制。方向一致性的二项检验（p = 0.016）是合理的统计策略。\n\n**S2. XNLI 非冲突基线控制得当。** 用相同 pipeline 在 XNLI 上运行探测，证明不对称性并非冲突特异，是本文最有说服力的控制实验之一。\n\n**S3. EN-DE 类型学控制巧妙。** 德语词汇重叠率约为中文的 4 倍（14.8% vs 3.8%），但 EN↔DE 不对称性接近零（Δ = +1.2pp, n.s.），有效排除了 token overlap 混淆。\n\n**S4. Selectivity control 规范。** 置换标签控制（N=131–201）产生近机会准确率（49.2–51.0%），selectivity gap 达 21–40pp，证实探测信号非任意线性可分。\n\n**S5. Steering 随机控制设计合理。** 注入等幅随机向量 r ~ N(0,I) 作为对照，将方向效应与幅度效应分离，方法上较先前工作有改进。\n\n**S6. Limitations 诚实。** 明确承认单 split 局限性并承诺 camera-ready 补充 5-fold CV，以及 steering 仅在 Llama 成功。\n\n---\n\n### Weaknesses\n\n**W1 [critical] \"Detection ≠ Decision\" 核心论断证据不足，存在过度概括。**\n- 具体位置：Abstract (\"these findings indicate that linear detectability does not imply causal relevance\")、Section 5 Discussion、Section 6 Conclusion\n- 问题：正面因果证据仅来自**一个模型（Llama）的一个层（L13）**。Qwen 和 Gemma 的负面结果可被多种替代假设解释：(a) 非线性因果通路（论文自己承认）；(b) 因果窗口在不同层（Llama 中因果窗口仅 ~4 层宽/L13-L16，但 Qwen 仅测 L14、Gemma 仅测 L17，遗漏相邻层的可能性大）；(c) 样本量不足（Qwen n=131、Gemma n=171，对微弱效应的检验功效有限）；(d) 线性 steering 本身的方法局限。Absence of evidence ≠ evidence of absence——论文将两个模型的 null result 提升为跨模型的一般性结论，逻辑跳跃过大。\n- 为什么影响接收：这是论文的第三个贡献点（Contribution 3），也是 abstract 和 conclusion 的核心 takeaway。如果此论断不成立，论文的新颖贡献大幅缩水，仅剩描述性发现（跨语言可检测性 + 不对称性）。\n- 建议修改方向：(1) 将 claim 降级为 Llama 特有观察，明确声明无法推广到其他架构；(2) 对 Qwen/Gemma 在至少 3-5 个相邻层进行 steering（而非仅 1 层），以确认负面结果的鲁棒性；(3) 补充 activation patching 实验作为线性 steering 的对照。\n\n**W2 [critical] Qwen 不对称性 CI 包含零，但被当作支持证据处理。**\n- 具体位置：Section 4.3, Table 1 — Qwen Δ_asym = +7.2, CI [−0.6, 13.7]\n- 问题：Qwen 的 95% CI 跨越零，意味着该模型的不对称性在 α=0.05 水平不显著。但论文在 Section 4.3 中写 \"the asymmetry is consistent in direction across all three architectures\" 并将 Qwen 与 Llama/Gemma 同等对待。进一步，如果对三个模型的不对称性检验做 Bonferroni 校正（阈值 0.017），Llama (p=0.038) 也不再显著，仅 Gemma (p=0.006) 幸存。\n- 为什么影响接收：不对称性的跨模型一致性是 Contribution 2 的基础。三个模型中两个不显著（校正后），严重削弱\"一致\"的论断。\n- 建议修改方向：(1) 明确报告 Qwen 不显著，不要用模糊的 \"marginally includes zero\"；(2) 讨论对三模型做多重比较校正后的结果；(3) 更多依赖方向一致性的二项检验（p=0.016）和 XNLI 的独立复制，而非个体模型的点估计。\n\n**W3 [critical] COMET tercile 分析严重欠功效，无法有效排除翻译质量混淆。**\n- 具体位置：Section 4.5, Table 2\n- 问题：论文自己报告 MDE = 25.3pp at 80% power（n≈56 per tercile）——即只有翻译质量造成 >25pp 的准确率差异时才能检测到。这使得该分析对中等大小的混淆效应完全不敏感。更令人担忧的是，Gemma 显示 Δ = +10.3pp 在混淆方向（高 COMET → 高准确率），虽然 p=0.278，但在这种低功效下不显著并不等于无效应。论文将此结果描述为 \"non-significant trend\"（Section 4.5），但一个 10pp 的点估计在混淆方向上是实质性的。\n- 为什么影响接收：如果翻译质量确实影响跨语言探测准确率，则 ZH→EN 不对称性可能是 artifact。COMET tercile 分析本应排除此混淆，但因欠功效而无法完成此任务。\n- 建议修改方向：(1) 增加样本量或使用连续回归（COMET score 作为连续变量 vs. 探测准确率），而非三分位比较，以提升功效；(2) 对 Gemma 的 +10.3pp 趋势做更深入调查；(3) 如果无法增加功效，诚实声明翻译质量混淆未被排除。\n\n**W4 [warning] TOST 等价性检验功效仅 1.4%，无信息量。**\n- 具体位置：Section 4.4 — \"TOST equivalence tests (±2 pp margin) are non-significant (p > 0.36, power = 1.4%)\"\n- 问题：1.4% 的功效意味着即使冲突不对称性与 XNLI 不对称性完全相同，该检验也几乎不可能检测到等价性。±2pp 的等价边界过于严格（考虑到各个 CI 宽度 >10pp）。报告一个注定失败的检验并用 \"reflecting insufficient power\" 一笔带过，有空洞分析之嫌。\n- 建议：要么选择合理的等价边界（如 ±5pp）并报告所需样本量，要么删除 TOST 分析，改用 CI 重叠的定性论证。\n\n**W5 [warning] 单 train/test split 贯穿全文，bootstrap CI 仅捕获 split 内变异性。**\n- 具体位置：Section 4.1, Limitations\n- 问题：所有探测结果基于单一 80/20 split。Bootstrap resampling（n=2,000）估计的 CI 是条件于该 split 的——它不能告诉我们换一个 split 结果会怎样。论文在 Limitations 中承认 seed 复制显示 peak layer 可能偏移（Qwen ±1.90%），但未在主要结果中使用 k-fold CV。论文承诺 camera-ready 补充 5-fold CV，但当前版本缺乏此验证。\n- 建议：至少报告 3-fold CV 的主要结果（Table 1），或在当前版本就完成 5-fold CV。\n\n**W6 [warning] 翻译模型（Qwen3-8B）同时作为实验对象。**\n- 具体位置：Section 3.2, Section 4.1\n- 问题：Qwen3-8B 既是翻译 pipeline 又是三个被探测模型之一。虽然论文指出 Llama/Gemma（与翻译模型架构独立）也显示相同模式以缓解担忧，但 Qwen 特有的翻译偏差可能使 Qwen 的跨语言迁移结果不可靠。\n- 建议：在正文中更显著地标注此利益冲突，或使用独立翻译模型（如 NLLB）作为额外验证。\n\n**W7 [warning] 全文多重假设检验缺乏整体 FWER 控制。**\n- 具体位置：全文\n- 问题：粗略统计，全文约 100+ 假设检验：12 个探测二项检验、6 个不对称性检验、3 个 TOST、5 个混淆检验、~78 个 steering 检验等。Bonferroni 仅应用于 steering 实验（per-layer k=10 或 30-test 校正），但探测二项检验、不对称性检验、混淆检验均未做多重比较校正。虽然不同分析模块可视为独立研究问题，但 Section 4.3 的三个不对称性检验属于同一族。\n- 建议：至少对同族检验（如三模型不对称性）应用 Bonferroni/Holm 校正并报告校正后结果。\n\n**W8 [warning] Steering 仅在英文 test data 上评估，未测试跨语言因果干预。**\n- 具体位置：Section 3.6 — \"Steering evaluation uses only the conflict-condition subset of the English test data\"\n- 问题：一篇关于跨语言冲突机制的论文，其因果干预实验仅在英文输入上进行。ZH→EN 探测不对称性是核心发现，但从未测试在中文输入上进行 steering 是否产生不同的因果模式。\n- 建议：至少在 Llama L13（已知有效的层）上测试中文输入的 steering 效果。\n\n**W9 [info] Fisher's exact test 用于 paired data 可能不当。**\n- 具体位置：Section 3.6, Section 4.6\n- 问题：Steering 实验中，相同测试样本分别接受 probe-direction 和 random-direction 注入。这是配对数据，但 Fisher's exact test 假设独立样本。McNemar's test 更适合配对二分类数据。在正相关情况下（容易翻转的样本在两种条件下都容易翻转），Fisher's test 可能是保守的，但这应予以说明。\n- 建议：补充 McNemar's test 结果，或论证 Fisher's exact test 的保守性。\n\n---\n\n### Questions to Authors\n\n**Q1.** Llama 中因果窗口仅 ~4 层宽（L13-L16）。对 Qwen 和 Gemma，你们仅测试了 1 个层（L14/L17）。如果因果窗口同样窄，遗漏相邻层完全可能。是否有 Appendix F 以外的多层 steering 结果？Appendix F 的 Table 6 是否覆盖了每个模型至少 3 个相邻层？\n\n**Q2.** Table 1 中 Δ_asym 脚注指出 \"Δ_asym is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies\"。以 Llama 为例：ZH→EN (70.6) − EN→ZH (59.6) = 11.0pp，但 bootstrap Δ_asym = +7.3pp。这 3.7pp 差异的来源是什么？这是否意味着 peak layer 在不同 bootstrap 样本中发生偏移？如果是，这本身就说明单 split 结果不稳定。\n\n**Q3.** Gemma COMET tercile Δ = +10.3pp 在混淆方向。你们将此归因于 \"near-chance baseline accuracy of the EN→ZH probe at L17 (58.8%)\"，但 58.8% 仍显著高于 chance（binomial p < 0.05 for n≈56）。能否提供 Gemma COMET score 与探测准确率的散点图或连续回归结果？\n\n**Q4.** Qwen3-8B 同时作为翻译模型和实验对象。你们是否验证过：在 Qwen 上，用外部翻译模型（如 NLLB）的翻译是否产生相似的跨语言迁移模式？\n\n**Q5.** Section 4.6 报告 L13 steering 的 all-position injection 与 last-token injection 产生 \"identical results\"。能否提供具体数字？\"Identical\" 是指 p-value 和 flip rate 完全相同，还是方向一致但幅度不同？\n\n---\n\n### Missing References\n\n无明显遗漏。论文引用了该领域的主要相关工作（Zhao et al. 2024/2026, Basu et al. 2026, Hewitt & Liang 2019, Belinkov 2022, Marks & Tegmark 2024 等）。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 2.5/5 | 核心因果论断证据不足（W1），不对称性统计证据不一致（W2），混淆排除欠功效（W3）。描述性发现（可检测性、XNLI 基线）较为扎实。 |\n| **Excitement** | 3/5 | 跨语言冲突机制解释是有意义的研究方向，\"detection ≠ decision\" 观察如能充分支撑会很有启发，但当前证据使其更像初步观察而非成熟结论。 |\n| **Reproducibility** | 3.5/5 | 超参（C=1.0）、硬件（RTX PRO 6000）、bootstrap n=2000 均有报告；匿名 repo 已提供。不足：主实验随机种子未明确报告；单 split 无 CV。 |\n\n---\n\n### Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n本文在跨语言冲突信号可检测性和迁移不对称性方面提供了有价值的描述性发现，XNLI 基线和 EN-DE 控制设计得当。但论文的核心机制性贡献（\"detection ≠ decision\"）基于一个模型一个层的正面证据和两个模型的方法学上可疑的负面证据，无法支撑 abstract 和 conclusion 中的概括性论断。不对称性的统计证据在三模型中不一致（Qwen CI 包含零，Bonferroni 校正后仅 Gemma 显著），混淆排除分析欠功效（COMET tercile MDE = 25.3pp）。这些方法论问题叠加后，使论文的 soundness 低于主会议标准。修改后适合 Findings。\n\n### Confidence\n\n**Confidence: 4/5** — 统计方法论和 probing/steering 实验设计是我的专长领域，仔细阅读了全文及附录。对论文所涉的具体模型架构细节稍不确定。",
    "reviewer_id": "1",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 235 · 2026-05-25T21:23:54.532049+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3875
}
```

</details>

---

### Tool call

_source line 236 · 2026-05-25T21:24:01.797593+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
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

_source line 237 · 2026-05-25T21:24:01.898293+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 238 · 2026-05-25T21:24:05.509073+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-25T21:24:05.559641+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 240 · 2026-05-25T21:24:14.735138+00:00_

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
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1"
}
```

</details>

---

## Round 8

10 recorded events

### User

_source line 241 · 2026-05-25T21:24:51.741239+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Weaknesses 和关键论点：对每条用 [AGREE] 表示同意（简述理由），或 [REBUT] 表示反驳（引用具体 Section/Table/Figure 提供证据）。

---

# Reviewer 2 审稿意见：新颖性与完整性

## Summary

本文将知识冲突信号的 probing 分析从单语（Zhao et al. 2024）扩展到跨语言（英-中）设置，使用三个 LLM（Llama-3.1-8B-Instruct��Qwen2.5-8B、Gemma-2-9B-IT）进行残差流探测、XNLI 非冲突基线对照、COMET 混淆因素排除和因果 steering 实验。主要发现：(1) 冲突信号在所有模型和方向上线性可检测；(2) ZH→EN 迁移优势约 7pp，与 XNLI 基线一致，反映一般跨语言结构而非冲突特异性；(3) 因果 steering 仅在 Llama L13（41% 深度）成功，Qwen/Gemma 无显著因果效应，表明检测不蕴含因果相关性。

## Strengths

**S1. 混淆因素控制设计出色。** COMET 翻译质量分层 + XNLI 非冲突基线的组合是一个真正的方法论贡献（Section 3.5, 4.4-4.5）。用 XNLI 作为非冲突对照来区分冲突特异性 vs. 一般跨语言不对称性，思路清晰且可复用。

**S2. 多模型验证增强泛化性。** 三个架构差异显著的模型（Llama/Qwen/Gemma）在检测能力上一致，强化了"冲突信号线性可检测"这一结论的可信度（Table 1, Figure 3）。

**S3. 统计方法规范。** Bootstrap CI（n=2000）、Bonferroni 校正（l=10 to α values）、Fisher 精确检验、matched-condition 控制，统计实践达到 top-venue 标准。

**S4. 诚实报告负面结果。** Qwen/Gemma steering 失败（Table 3）、asymmetry 非冲突特异性（Section 4.4）——这些负面结果的如实报告值得肯定，优于很多只报积极结果的论文。

**S5. Seed replication 加强因果 claim。** Appendix C 用独立 seed 复现了 Llama L13 steering 效果（N=201, 独立 train/test split），排除了单次 split 偶然性的可能。

## Weaknesses

### Must-Fix 问题

**N1 [critical] "Detection ≠ Decision" 核心 claim 支撑不足，且与 Basu et al. (2026) 差异化不清晰。**
- Basu et al. (2026) 已在单语设置中建立了 detection-steering 的 dissociation。本文跨语言扩展未清晰阐述相比单语设置的增量发现。
- Steering 仅在 Llama L13 产生显著因果效应，2/3 模型不支持任何因果影响。
- 相邻 L16 已无效（p>0.12），因果窗口极窄，可能是 fragile artifact。
- 将"steering 在 2/3 模型失败"框架为支持 dissociation，但也可能是 steering 方法太粗糙。

**N2 [critical] "General Cross-Lingual Asymmetries" 泛化声称仅基于单一语言对。**
- 标题声称 "General Cross-Lingual Asymmetries"，但实验仅覆盖英-中一个语言对。EN-DE 仅用于混淆因素检查，未作完整探测实验。

**N3 [critical] Contribution 2（asymmetry = general structure）本质是 null result 被包装为正面贡献。**
- 发现不对称性与 XNLI 基线一致 = 不是冲突特异的 = null result。将其列为独立贡献膨胀了贡献计数。

### Should-Fix 问题

**W1 [warning] 四个贡献的权重严重不均衡。**
**W2 [warning] 单一 train/test split，缺乏交叉验证。**
**W3 [warning] Steering 分析样本量小、多重比较负担重。**
**W4 [warning] 机制深度偏浅——定位偏 empirical probing，非 mechanistic interpretability。**
**W5 [warning] Related Work 缺少跨语言知识编辑文献。**
**W6 [info] 缺少独立 Conclusion 章节。**

## Missing References

1. "Editing Across Languages: A Survey of Multilingual Knowledge Editing" (2025)
2. CLM-Bench (2026)
3. BMIKE-53

## Overall Assessment: 3.0/5 (Findings)

---

请逐条回应上述 Weaknesses（N1-N3, W1-W6）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 242 · 2026-05-25T21:25:23.967808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool call

_source line 243 · 2026-05-25T21:25:23.968250+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 244 · 2026-05-25T21:25:30.495197+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Causal influence is localized to L13 regardless of detection peak.}
5	In Llama, causal influence is localized to L13 (41\% depth; Fisher $p < 0.001$), near but distinct from the linear probe peak (L15, 47\%) and MLP probe peak (L18, 56\%), with upper-layer interventions producing no significant change ($p > 0.3$; Figure~\ref{fig:dissociation}).
6	L13 coincides with cross-lingual alignment sites \citep{muller2021first, wendler2024llamas}, suggesting mid-layers serve a dual role in alignment and conflict resolution.
7	The dissociation evidence is strongest for Gemma, where 88.9\% probe accuracy and 0.93 AUROC coexist with zero steering effects, ruling out probe quality as a confound; for Qwen, weaker probe performance (71.4\%) leaves the null result more ambiguous.
8	
9	\paragraph{Why does steering fail in Qwen and Gemma?}
10	Three hypotheses merit consideration: (1)~non-linear causal interactions \citep{elhage2022toy}, where MLP probes gain $+9.2$~pp over linear probes on conflict but $-0.5$~pp on XNLI; (2)~superposition \citep{templeton2024scaling}, where conflict and XNLI weight vectors are near-orthogonal yet cross-task language transfer is near-perfect; (3)~architectural differences, as Qwen and Gemma show mid-layer transfer dips absent in Llama.
11	Definitive validation requires activation patching \citep{meng2022locating}.
12	
13	\paragraph{Relation to prior work.}
14	The ZH$\to$EN advantage matches the XNLI baseline across all models, indicating that asymmetry piggybacks on general cross-lingual alignment \citep{zhao2026when, kargaran2024mexa, wendler2024llamas}.
15	\citet{basu2026interpretability} reported steering failure despite 98.2\% AUROC; our L13 succeeds because we steer at mid-layer rather than probe-peak, while our three-model design isolates architecture.
16	
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6527
}
```

</details>

---

### Tool result

_source line 245 · 2026-05-25T21:25:30.495560+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that knowledge conflict signals are linearly detectable across English and Chinese ($p < 0.001$, three architectures), with the ZH$\to$EN transfer advantage (${\sim}$7~pp) matching the XNLI baseline, indicating general cross-lingual alignment rather than conflict-specific encoding.
5	Causal intervention reveals a detection--decision dissociation: all three models detect conflict signals, yet only Llama yields significant steering at L13 ($p < 0.001$); Gemma fails despite 88.9\% probe accuracy, confirming detection alone is insufficient for mechanistic claims.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6527
}
```

</details>

---

### Tool call

_source line 246 · 2026-05-25T21:25:30.646317+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 247 · 2026-05-25T21:25:30.646837+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Knowledge conflict detection.}
5	\citet{xie2024adaptive} introduced ConflictQA and showed that models exhibit context-dependent resolution strategies, and \citet{xu2024knowledge} provided a systematic conflict taxonomy (intra-memory, context-memory, inter-context).
6	Moving beyond behavioral observation, \citet{zhao2024analysing} demonstrated linearly separable conflict signals in English residual streams, and \citet{brink2026probing} localized factual associations via probing. More recently, \citet{pham2026where} traced intra-memory conflict pathways, while \citet{li2025taming} proposed conflict mitigation methods.
7	Information-theoretic approaches \citep{pimentel2021probing} offer complementary perspectives on probe expressiveness, and \citet{ravichander2021probing} raised concerns about whether probed information is task-relevant.
8	These studies operate exclusively in monolingual settings; extending to cross-lingual scenarios introduces confounds (translation quality, token overlap, general transfer properties) that we address with a dedicated exclusion pipeline.
9	
10	\paragraph{Cross-lingual representations in multilingual models.}
11	Intermediate layers develop language-independent representations: \citet{wu2020emerging} showed cross-lingual structure emerges without explicit alignment, and \citet{muller2021first} found mid-layer alignment in multilingual BERT.
12	For decoder-only LLMs, \citet{wendler2024llamas} showed that Llama processes non-English inputs through an English-centric latent space, and \citet{kargaran2024mexa} quantified this bias across language pairs.
13	These findings predict our empirical observations: mid-layer steering success aligns with intermediate-layer language alignment, and the ZH$\to$EN transfer advantage reflects English-centric structure.
14	Behavioral consequences have been documented by \citet{wang2025lost}, \citet{zhao2026when} (CLEAR cross-lingual conflic
…[truncated 1836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 248 · 2026-05-25T21:27:26.842714+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### N1 [critical] \"Detection ≠ Decision\" 核心 claim 支撑不足，与 Basu et al. (2026) 差异化不清晰\n\n**[AGREE] R2-N1**\n\n同意此为论文最大弱点。我在自己的 W1 中提出了几乎相同的判断。补充几点：\n\n1. **与 Basu et al. 的增量**：Section 5 第三段仅用一句话区分：\"our L13 succeeds because we steer at mid-layer rather than probe-peak, while our three-model design isolates architecture。\" 这个差异化论述过于单薄。公平地说，跨语言维度和三模型对比确实是增量，但核心 dissociation 观察（高 probe accuracy ≠ steering success）Basu et al. 已建立，本文的增量主要在于：(a) 跨语言设定、(b) 三模型对比、(c) 层级定位（mid-layer vs probe-peak），但 (a)(b) 是 setting 扩展而非 insight 扩展，(c) 是有趣的但仅基于 Llama 一个模型。\n\n2. **因果窗口窄的 fragility 问题**：R2 指出 L16 已无效（p>0.12），因果窗口极窄。我的补充证据来自 Appendix Table 4（boundary replication），L14 p=0.002, L16 p=0.005，到 L18 已不显著——这是约 4 层（~12% depth）的窗口。在 Qwen/Gemma 仅测 1 层（L14/L17）的情况下，遗漏相邻层的可能性确实存在。\n\n3. **方法粗糙 vs 真正 dissociation**：完全同意 R2 的判断——\"steering 方法太粗糙\" 是 Qwen/Gemma null result 的合理替代解释。Section 5 第二段虽列举了三个假设（non-linear interactions / superposition / architectural differences），但均未提供任何鉴别证据。\n\n---\n\n### N2 [critical] \"General Cross-Lingual Asymmetries\" 泛化声称仅基于单一语言对\n\n**[REBUT] R2-N2**\n\n部分反驳。R2 的批评基于对标题中 \"general\" 的语义理解偏差。\n\n标题原文是 \"English-Chinese Knowledge Conflict Signals **Are Consistent With** General Cross-Lingual Asymmetries\"——这里 \"general\" 修饰的是 asymmetries 的性质（一般跨语言结构 vs 冲突特异性），而非声称实验覆盖了多语言对。标题的 claim 是：EN-ZH 上观察到的不对称性**与已知的一般跨语言结构一致**，证据是 Section 4.4 的 XNLI 非冲突基线（6 个数据点：3 模型 × 2 任务，方向全部一致，binomial p = 0.016）。\n\n但我承认 R2 的担忧有部分道理：\n- 仅 EN-ZH 一对确实限制了泛化性。XNLI 基线证明的是 \"EN-ZH 不对称性不是冲突特异的\"，但不能证明\"同样的模式会出现在 EN-AR 或 EN-JA 上\"。\n- EN-DE 控制（Section 4.5, Table 2）仅用于混淆排除，未做完整探测实验。如果在 EN-DE 上也做完整四方向探测并观察到 Δ_asym ≈ 0（因为两种语言与英语的跨语言对齐程度相似），会更有说服力。\n\n总结：标题的语义学上没有过度声称，但实验覆盖确实有限。建议作者在 Limitations 中明确单语言对的泛化边界。\n\n---\n\n### N3 [critical] Contribution 2 本质是 null result 被包装为正面贡献\n\n**[REBUT] R2-N3**\n\n不同意将此定性为\"膨胀贡献计数\"。\n\n在 probing 和可解释性研究中，区分 task-specific encoding 与 general structural property 是一个有实质意义的发现。具体而言：\n- **无 XNLI 基线时**：读者会自然推断 ZH→EN 迁移优势是冲突编码的特有属性，可能据此设计冲突特异的干预策略。\n- **有 XNLI 基线后**：不对称性被归因于一般跨语言结构，改变了后续研究的方向——跨语言冲突干预不应从 asymmetry 入手，而应关注底层的语言对齐机制。\n\n这种 \"ruling out\" 型贡献在 NLP 中有先例：Hewitt & Liang (2019) 的 selectivity 控制本身是一个 \"null result\"（好的 probe 在置换标签下应失败），但它改变了整个 probing 方法论。\n\n然而，我同意此贡献的**统计证据不够强**——这是我自己 W2 和 W4 提出的：Qwen CI 包含零、TOST 功效仅 1.4%。如果统计证据更扎实（例如所有三个模型的 conflict 和 XNLI Δ_asym CI 都 exclude zero，且 TOST 通过合理等价边界），这个贡献就毫无争议了。当前状态下，Contribution 2 的 claim 比证据能支撑的更强。\n\n---\n\n### W1 [warning] 四个贡献的权重严重不均衡\n\n**[AGREE] R2-W1**\n\n同意。Contribution 1（跨语言可检测性）本质上是将 Zhao et al. (2024) 的方法扩展到 EN-ZH——是必要的基础工作但增量有限。Contribution 4（混淆排除 pipeline）更像方法论组件而非独立贡献。论文的核心价值集中在 Contribution 2 和 3，但前者统计证据不足（我的 W2），后者因果证据薄弱（我的 W1 / R2 的 N1）。\n\n---\n\n### W2 [warning] 单一 train/test split，缺乏交叉验证\n\n**[AGREE] R2-W2**\n\n完全同意，这也是我的 W5。补充一个 R2 未提及的技术点：Table 1 脚注指出 \"Δ_asym is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies\"。以 Llama 为例，算术差 = 70.6 − 59.6 = 11.0pp，但 bootstrap Δ_asym = +7.3pp，差距 3.7pp。这暗示 peak layer 在 bootstrap 样本间可能发生偏移，进一步说明单 split 结果不够稳定。\n\n---\n\n### W3 [warning] Steering 分析样本量小、多重比较负担重\n\n**[AGREE] R2-W3**\n\n同意。我在 W1 和 W7 中分别从样本量和全文 FWER 两个角度提出了相同担忧。Qwen n=131、Gemma n=171 的样本量对于检测微弱因果效应的功效有限。论文的 Bonferroni 校正仅限于 steering 内部（per-layer k=10），但跨分析模块的 ~100+ 检验未做整体校正。\n\n---\n\n### W4 [warning] 机制深度偏浅\n\n**[AGREE] R2-W4**\n\n部分同意。论文使用 logistic regression probing + linear steering，这在 mechanistic interpretability 谱系中属于较浅的方法。Section 5 Discussion 自己承认 \"definitive validation requires activation patching\"（第二段末），但未实际执行。论文更准确地说是 **probing-based analysis with causal validation attempt**，而非 full mechanistic interpretability。\n\n不过，我不认为这构成 rejection 理由——probing + steering 的组合在当前文献中已是 accepted practice（Li et al. 2023, Turner et al. 2023, Marks & Tegmark 2024）。问题不在于方法深度，而在于从有限的 steering 结果中过度概括（回到 N1）。\n\n---\n\n### W5 [warning] Related Work 缺少跨语言知识编辑文献\n\n**[REBUT] R2-W5**\n\n部分反驳。Related Work（Section 2）第三段已引用了跨语言 steering 的近期工作：Pokharel et al. (2026) 的 training-free cross-lingual activation steering、Sundar et al. (2025) 的 cross-lingual alignment shifts、Gurgurov et al. (2026) 的 CLASBench。\n\nR2 建议补充的三篇参考文献（Editing Across Languages survey / CLM-Bench / BMIKE-53）属于 **knowledge editing** 方向，而本文是 **probing + steering** 方向。两者虽有联系但方法论不同——knowledge editing（ROME, MEMIT 等）修改模型参数，steering 不修改参数而是在推理时干预激活。在 8 页限制下，不加区分地引用 editing 文献可能混淆读者对论文定位的理解。\n\n但如果 R2 建议的文献中有直接分析跨语言冲突信号表征的工作，则应该引用。建议作者在 camera-ready 中选择性引用最相关的 1-2 篇。\n\n---\n\n### W6 [info] 缺少独立 Conclusion 章节\n\n**[REBUT] R2-W6**\n\nR2 事实判断有误。论文有独立的 Section 6 Conclusion（PDF 第 8 页底部），包含两句话的总结。该章节确实简短（仅 2 句），但它存在。R2 可能因其篇幅过短而忽略了它，或将 Discussion（Section 5）与 Conclusion（Section 6）混淆。\n\n---\n\n### 总结\n\n与 R2 在核心判断上高度一致：**N1（detection ≠ decision 论断证据不足）** 是论文最大的弱点，我们两位 reviewer 独立达成了相同结论。N2（标题泛化性）我认为 R2 对标题语义有误读，但实验覆盖有限的担忧是合理的。N3（null result 作为贡献）我持不同意见——排除冲突特异性是有意义的发现，但当前统计证据确实偏弱。\n\n我维持自己的 **Overall 3.0 (Findings)** 评分不变。",
  "reviewer_id": "1",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### N1 [critical] \"Detection ≠ Decision\" 核心 claim 支撑不足，与 Basu et al. (2026) 差异化不清晰\n\n**[AGREE] R2-N1**\n\n同意此为论文最大弱点。我在自己的 W1 中提出了几乎相同的判断。补充几点：\n\n1. **与 Basu et al. 的增量**：Section 5 第三段仅用一句话区分：\"our L13 succeeds because we steer at mid-layer rather than probe-peak, while our three-model design isolates architecture。\" 这个差异化论述过于单薄。公平地说，跨语言维度和三模型对比确实是增量，但核心 dissociation 观察（高 probe accuracy ≠ steering success）Basu et al. 已建立，本文的增量主要在于：(a) 跨语言设定、(b) 三模型对比、(c) 层级定位（mid-layer vs probe-peak），但 (a)(b) 是 setting 扩展而非 insight 扩展，(c) 是有趣的但仅基于 Llama 一个模型。\n\n2. **因果窗口窄的 fragility 问题**：R2 指出 L16 已无效（p>0.12），因果窗口极窄。我的补充证据来自 Appendix Table 4（boundary replication），L14 p=0.002, L16 p=0.005，到 L18 已不显著——这是约 4 层（~12% depth）的窗口。在 Qwen/Gemma 仅测 1 层（L14/L17）的情况下，遗漏相邻层的可能性确实存在。\n\n3. **方法粗糙 vs 真正 dissociation**：完全同意 R2 的判断——\"steering 方法太粗糙\" 是 Qwen/Gemma null result 的合理替代解释。Section 5 第二段虽列举了三个假设（non-linear interactions / superposition / architectural differences），但均未提供任何鉴别证据。\n\n---\n\n### N2 [critical] \"General Cross-Lingual Asymmetries\" 泛化声称仅基于单一语言对\n\n**[REBUT] R2-N2**\n\n部分反驳。R2 的批评基于对标题中 \"general\" 的语义理解偏差。\n\n标题原文是 \"English-Chinese Knowledge Conflict Signals **Are Consistent With** General Cross-Lingual Asymmetries\"——这里 \"general\" 修饰的是 asymmetries 的性质（一般跨语言结构 vs 冲突特异性），而非声称实验覆盖了多语言对。标题的 claim 是：EN-ZH 上观察到的不对称性**与已知的一般跨语言结构一致**，证据是 Section 4.4 的 XNLI 非冲突基线（6 个数据点：3 模型 × 2 任务，方向全部一致，binomial p = 0.016）。\n\n但我承认 R2 的担忧有部分道理：\n- 仅 EN-ZH 一对确实限制了泛化性。XNLI 基线证明的是 \"EN-ZH 不对称性不是冲突特异的\"，但不能证明\"同样的模式会出现在 EN-AR 或 EN-JA 上\"。\n- EN-DE 控制（Section 4.5, Table 2）仅用于混淆排除，未做完整探测实验。如果在 EN-DE 上也做完整四方向探测并观察到 Δ_asym ≈ 0（因为两种语言与英语的跨语言对齐程度相似），会更有说服力。\n\n总结：标题的语义学上没有过度声称，但实验覆盖确实有限。建议作者在 Limitations 中明确单语言对的泛化边界。\n\n---\n\n### N3 [critical] Contribution 2 本质是 null result 被包装为正面贡献\n\n**[REBUT] R2-N3**\n\n不同意将此定性为\"膨胀贡献计数\"。\n\n在 probing 和可解释性研究中，区分 task-specific encoding 与 general structural property 是一个有实质意义的发现。具体而言：\n- **无 XNLI 基线时**：读者会自然推断 ZH→EN 迁移优势是冲突编码的特有属性，可能据此设计冲突特异的干预策略。\n- **有 XNLI 基线后**：不对称性被归因于一般跨语言结构，改变了后续研究的方向——跨语言冲突干预不应从 asymmetry 入手，而应关注底层的语言对齐机制。\n\n这种 \"ruling out\" 型贡献在 NLP 中有先例：Hewitt & Liang (2019) 的 selectivity 控制本身是一个 \"null result\"（好的 probe 在置换标签下应失败），但它改变了整个 probing 方法论。\n\n然而，我同意此贡献的**统计证据不够强**——这是我自己 W2 和 W4 提出的：Qwen CI 包含零、TOST 功效仅 1.4%。如果统计证据更扎实（例如所有三个模型的 conflict 和 XNLI Δ_asym CI 都 exclude zero，且 TOST 通过合理等价边界），这个贡献就毫无争议了。当前状态下，Contribution 2 的 claim 比证据能支撑的更强。\n\n---\n\n### W1 [warning] 四个贡献的权重严重不均衡\n\n**[AGREE] R2-W1**\n\n同意。Contribution 1（跨语言可检测性）本质上是将 Zhao et al. (2024) 的方法扩展到 EN-ZH——是必要的基础工作但增量有限。Contribution 4（混淆排除 pipeline）更像方法论组件而非独立贡献。论文的核心价值集中在 Contribution 2 和 3，但前者统计证据不足（我的 W2），后者因果证据薄弱（我的 W1 / R2 的 N1）。\n\n---\n\n### W2 [warning] 单一 train/test split，缺乏交叉验证\n\n**[AGREE] R2-W2**\n\n完全同意，这也是我的 W5。补充一个 R2 未提及的技术点：Table 1 脚注指出 \"Δ_asym is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies\"。以 Llama 为例，算术差 = 70.6 − 59.6 = 11.0pp，但 bootstrap Δ_asym = +7.3pp，差距 3.7pp。这暗示 peak layer 在 bootstrap 样本间可能发生偏移，进一步说明单 split 结果不够稳定。\n\n---\n\n### W3 [warning] Steering 分析样本量小、多重比较负担重\n\n**[AGREE] R2-W3**\n\n同意。我在 W1 和 W7 中分别从样本量和全文 FWER 两个角度提出了相同担忧。Qwen n=131、Gemma n=171 的样本量对于检测微弱因果效应的功效有限。论文的 Bonferroni 校正仅限于 steering 内部（per-layer k=10），但跨分析模块的 ~100+ 检验未做整体校正。\n\n---\n\n### W4 [warning] 机制深度偏浅\n\n**[AGREE] R2-W4**\n\n部分同意。论文使用 logistic regression probing + linear steering，这在 mechanistic interpretability 谱系中属于较浅的方法。Section 5 Discussion 自己承认 \"definitive validation requires activation patching\"（第二段末），但未实际执行。论文更准确地说是 **probing-based analysis with causal validation attempt**，而非 full mechanistic interpretability。\n\n不过，我不认为这构成 rejection 理由——probing + steering 的组合在当前文献中已是 accepted practice（Li et al. 2023, Turner et al. 2023, Marks & Tegmark 2024）。问题不在于方法深度，而在于从有限的 steering 结果中过度概括（回到 N1）。\n\n---\n\n### W5 [warning] Related Work 缺少跨语言知识编辑文献\n\n**[REBUT] R2-W5**\n\n部分反驳。Related Work（Section 2）第三段已引用了跨语言 steering 的近期工作：Pokharel et al. (2026) 的 training-free cross-lingual activation steering、Sundar et al. (2025) 的 cross-lingual alignment shifts、Gurgurov et al. (2026) 的 CLASBench。\n\nR2 建议补充的三篇参考文献（Editing Across Languages survey / CLM-Bench / BMIKE-53）属于 **knowledge editing** 方向，而本文是 **probing + steering** 方向。两者虽有联系但方法论不同——knowledge editing（ROME, MEMIT 等）修改模型参数，steering 不修改参数而是在推理时干预激活。在 8 页限制下，不加区分地引用 editing 文献可能混淆读者对论文定位的理解。\n\n但如果 R2 建议的文献中有直接分析跨语言冲突信号表征的工作，则应该引用。建议作者在 camera-ready 中选择性引用最相关的 1-2 篇。\n\n---\n\n### W6 [info] 缺少独立 Conclusion 章节\n\n**[REBUT] R2-W6**\n\nR2 事实判断有误。论文有独立的 Section 6 Conclusion（PDF 第 8 页底部），包含两句话的总结。该章节确实简短（仅 2 句），但它存在。R2 可能因其篇幅过短而忽略了它，或将 Discussion（Section 5）与 Conclusion（Section 6）混淆。\n\n---\n\n### 总结\n\n与 R2 在核心判断上高度一致：**N1（detection ≠ decision 论断证据不足）** 是论文最大的弱点，我们两位 reviewer 独立达成了相同结论。N2（标题泛化性）我认为 R2 对标题语义有误读，但实验覆盖有限的担忧是合理的。N3（null result 作为贡献）我持不同意见——排除冲突特异性是有意义的发现，但当前统计证据确实偏弱。\n\n我维持自己的 **Overall 3.0 (Findings)** 评分不变。",
    "reviewer_id": "1",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 249 · 2026-05-25T21:27:30.506335+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3663
}
```

</details>

---

### Assistant

_source line 250 · 2026-05-25T21:27:37.986346+00:00_

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
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_1"
}
```

</details>

---
